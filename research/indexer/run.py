import argparse
import contextlib
import ctypes
import json
import os
import re
import subprocess
import time
import urllib.parse
import urllib.request
import zipfile
import shutil
from pathlib import Path

from indexer.store import LOCAL, configure_output, connect, digest, import_index, read_json, sync_results, write_json
from indexer.memory import enforce_memory


@contextlib.contextmanager
def locked(path):
    # OSロックなのでプロセス終了時には解除される。
    with Path(path).open('a+b') as stream:
        if stream.seek(0, 2) == 0:
            stream.write(b'0')
            stream.flush()
        stream.seek(0)
        if os.name == 'nt':
            import msvcrt
            msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl
            fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        try:
            yield
        finally:
            if os.name == 'nt':
                stream.seek(0)
                msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)


def mcp(config, endpoint, body):
    url = urllib.parse.urlparse(config['mcp_url'])
    if url.scheme != 'http' or url.hostname not in ('localhost', '127.0.0.1', '::1'):
        raise ValueError('Only loopback MCP endpoints are allowed')
    request = urllib.request.Request(config['mcp_url'].rstrip('/') + endpoint,
                                     json.dumps(body).encode(), {'Content-Type': 'application/json'})
    with urllib.request.urlopen(request, timeout=180) as response:
        result = json.load(response)
    if result.get('error'):
        raise RuntimeError(result['error'])
    return result


def peak_memory(process):
    if os.name != 'nt':
        return None
    from ctypes import wintypes

    class Counters(ctypes.Structure):
        _fields_ = [('cb', wintypes.DWORD), ('faults', wintypes.DWORD)] + [
            (name, ctypes.c_size_t) for name in ('peak', 'working', 'pool_peak', 'pool',
                                               'nonpaged_peak', 'nonpaged', 'pagefile', 'pagefile_peak')]
    counters = Counters()
    counters.cb = ctypes.sizeof(counters)
    call = ctypes.windll.psapi.GetProcessMemoryInfo
    call.argtypes = [wintypes.HANDLE, ctypes.c_void_p, wintypes.DWORD]
    if call(wintypes.HANDLE(int(process._handle)), ctypes.byref(counters), counters.cb):
        return counters.peak
    return None


def stop_process(process):
    if os.name == 'nt':
        subprocess.run(['taskkill', '/PID', str(process.pid), '/T', '/F'],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=20)
    else:
        process.kill()


def headless(config, root, snapshot, mode, timeout, initialize=False, analyze_existing=False):
    ghidra = Path(config['ghidra_home'])
    java = Path(config['java_home']) / 'bin' / ('java.exe' if os.name == 'nt' else 'java')
    heap = config.get('heap', '512M')
    if not re.fullmatch(r'\d+[mMgG]', heap):
        raise ValueError('Invalid heap value')
    # Ghidraは先頭ドットを含むプロジェクト親パスを拒否するため、実体を.localに保つ別名を使う。
    alias = LOCAL.parent / 'ghidra-workspace'
    target = LOCAL / 'cache'
    if not alias.exists():
        if os.name == 'nt':
            env = os.environ | {'CACHE_ALIAS_PATH': str(alias), 'CACHE_TARGET_PATH': str(target)}
            subprocess.run(['powershell', '-NoProfile', '-NonInteractive', '-Command',
                            'New-Item -ItemType Junction -Path $env:CACHE_ALIAS_PATH -Target $env:CACHE_TARGET_PATH | Out-Null'],
                           env=env, check=True, capture_output=True, timeout=30)
        else:
            alias.symlink_to(target, target_is_directory=True)
    if alias.resolve() != target.resolve():
        raise ValueError('Unexpected ghidra-workspace junction target')
    project = alias / root.relative_to(target) / 'project'
    project.mkdir(exist_ok=True)
    existing = project / 'cache.gpr'
    if not existing.exists() and snapshot.suffix == '.zip':
        raise RuntimeError('Project is missing; restore backup-project.zip to the project directory first')
    arguments = (['-process', config['program']] + ([] if analyze_existing else ['-readOnly'])) if existing.exists() else ['-import', str(snapshot)]
    analysis_limit = config.get('analysis_timeout_seconds', 600)
    analysis = (['-analysisTimeoutPerFile', str(analysis_limit)] if analysis_limit else []) if initialize or analyze_existing else ['-noanalysis']
    script = Path(__file__).resolve().parents[1] / 'ghidra'
    command = [str(java), '-Djava.system.class.loader=ghidra.GhidraClassLoader',
               '-Dfile.encoding=UTF8', '-Djava.awt.headless=true', '-Xmx' + heap,
               '-XX:ParallelGCThreads=1', '-XX:CICompilerCount=2',
               '-cp', str(ghidra / 'Ghidra/Framework/Utility/lib/Utility.jar'),
               'ghidra.Ghidra', 'ghidra.app.util.headless.AnalyzeHeadless',
               str(project), 'cache', *arguments, *analysis, '-max-cpu', '1',
               '-scriptPath', str(script), '-postScript', 'ExportCache.java', str(root), mode, str(timeout)]
    command.append(config.get('decompiler_style', 'decompile'))
    log = root / ('full-analysis.log' if analyze_existing else 'initial-analysis.log' if initialize else f'{mode}.log')
    tick = time.perf_counter()
    peak = 0
    native_peak = 0
    next_memory_check = tick
    # JVMを直接起動して対象プロセスだけのメモリを測る。子孫デコンパイラは含まない。
    with log.open('w', encoding='utf-8') as output:
        priority = subprocess.BELOW_NORMAL_PRIORITY_CLASS if os.name == 'nt' else 0
        process = subprocess.Popen(command, stdout=output, stderr=subprocess.STDOUT, creationflags=priority)
        try:
            batch_limit = config.get('batch_timeout_seconds', 900)
            deadline = tick + batch_limit if batch_limit else None
            while process.poll() is None:
                peak = max(peak, peak_memory(process) or 0)
                if time.perf_counter() >= next_memory_check:
                    native_private, _ = enforce_memory(process.pid, root, config.get('native_memory_limit_mb', 1536))
                    native_peak = max(native_peak, native_private)
                    next_memory_check = time.perf_counter() + 2
                if deadline is not None and time.perf_counter() > deadline:
                    stop_process(process)
                    raise TimeoutError('Batch timed out; completed journal entries can be resumed')
                time.sleep(0.5)
            if process.returncode:
                raise RuntimeError(f'Headless failed; inspect {log}')
        finally:
            if process.poll() is None:
                stop_process(process)
            process.wait()
    # Ghidraはスクリプト失敗でも終了値0を返すことがある。
    text = log.read_text(encoding='utf-8', errors='replace')
    marker = 'Cache index:' if mode == 'index' else 'Cache decompilation complete'
    if marker not in text:
        raise RuntimeError(f'Export script did not complete; inspect {log}')
    return {'wall_seconds': time.perf_counter()-tick, 'jvm_peak_working_set_bytes': peak,
            'heap_limit': heap, 'decompiler_child_memory_included': False,
            'native_observed_peak_private_bytes': native_peak,
            'native_memory_limit_mb': config.get('native_memory_limit_mb', 1536),
            'decompiler_style': config.get('decompiler_style', 'decompile')}


def main():
    configure_output()
    parser = argparse.ArgumentParser(description='Snapshot-based Ghidra cache extraction')
    parser.add_argument('--config', type=Path, required=True)
    sub = parser.add_subparsers(dest='command', required=True)
    initialize = sub.add_parser('init-latest')
    initialize.add_argument('--verified', required=True, type=Path)
    initialize.add_argument('--architecture', required=True)
    initialize.add_argument('--library', default='libnative-lib.so')
    prepare = sub.add_parser('prepare')
    prepare.add_argument('--binary', type=Path, required=True)
    prepare.add_argument('--version', required=True)
    prepare.add_argument('--version-code', required=True, type=int)
    prepare.add_argument('--architecture', required=True)
    prepare.add_argument('--snapshot', type=Path)
    prepare.add_argument('--evidence', type=Path, required=True)
    for name in ('index', 'decompile'):
        child = sub.add_parser(name)
        child.add_argument('--cache', type=Path, required=True)
        if name == 'index':
            child.add_argument('--refresh', action='store_true')
        if name == 'decompile':
            child.add_argument('--all', action='store_true')
            child.add_argument('--limit', type=int, default=30)
            child.add_argument('--address', action='append')
            child.add_argument('--retry-failed', action='store_true')
    args = parser.parse_args()
    config = read_json(args.config)
    if args.command == 'init-latest':
        verified = read_json(args.verified)
        config = config | {'program': args.library}
        version = verified['version']
        if not re.fullmatch(r'\d+\.\d+\.\d+', version['versionName']) or not re.fullmatch(r'[A-Za-z0-9_-]+', args.architecture):
            raise ValueError('Invalid version/architecture')
        library = next(item for item in verified['libraries']
                       if item['architecture'] == args.architecture and item['library'] == args.library)
        binary = Path(library['path'])
        if digest(binary) != library['sha256']:
            raise ValueError('Verified library checksum mismatch')
        root = LOCAL / 'cache' / version['versionName'] / args.architecture / library['sha256']
        root.mkdir(parents=True, exist_ok=True)
        with locked(root / 'writer.lock'):
            if (root / 'identity.json').exists():
                print(json.dumps({'cache': str(root), 'reused': True}))
                return
            existing_project = (root / 'project/cache.gpr').exists()
            if existing_project and not (root / 'initial-analysis.log').exists() and (root / 'index.log').exists():
                shutil.copyfile(root / 'index.log', root / 'initial-analysis.log')
            metrics = headless(config, root, binary, 'index', config.get('timeout_seconds', 20), initialize=not existing_project)
            backup = root / 'backup-project.zip'
            if not backup.exists():
                temporary = backup.with_suffix('.partial')
                with zipfile.ZipFile(temporary, 'w', compression=zipfile.ZIP_STORED) as archive:
                    for path in (root / 'project').rglob('*'):
                        if path.is_file():
                            archive.write(path, path.relative_to(root / 'project'))
                temporary.replace(backup)
            analysis_log = root / 'initial-analysis.log'
            timed_out = analysis_log.exists() and 'Analysis timed out' in analysis_log.read_text(encoding='utf-8', errors='replace')
            identity = {'version': version['versionName'], 'version_code': version['versionCode'],
                        'architecture': args.architecture, 'sha256': library['sha256'],
                        'binary': str(binary), 'library': args.library, 'snapshot': str(backup), 'snapshot_format': 'project_zip',
                        'snapshot_sha256': digest(backup), 'evidence': verified, 'analysis_timed_out': timed_out}
            metrics['functions'] = import_index(root, identity)
            write_json(root / 'identity.json', identity)
            metrics['analysis_timed_out'] = timed_out
            write_json(root / 'initial-analysis-metrics.json', metrics)
        print(json.dumps({'cache': str(root), 'metrics': metrics}, indent=2))
        return
    if args.command == 'prepare':
        if not re.fullmatch(r'\d+\.\d+\.\d+', args.version) or not re.fullmatch(r'[A-Za-z0-9_-]+', args.architecture):
            parser.error('Invalid version/architecture')
        sha = digest(args.binary)
        root = LOCAL / 'cache' / args.version / args.architecture / sha
        root.mkdir(parents=True, exist_ok=True)
        with locked(root / 'writer.lock'):
            if (root / 'identity.json').exists():
                print(root)
                return
            evidence = read_json(args.evidence)
            if evidence.get('sha256') != sha or evidence.get('versionName') != args.version or evidence.get('versionCode') != args.version_code:
                raise ValueError('Evidence does not match binary/version')
            snapshot = args.snapshot.resolve() if args.snapshot else root / 'backup.gzf'
            if not args.snapshot:
                mcp(config, '/export_program', {'program_name': config['program'],
                    'output_dir': str(root), 'output_name': snapshot.name})
            identity = {'version': args.version, 'version_code': args.version_code,
                        'architecture': args.architecture, 'sha256': sha,
                        'binary': str(args.binary.resolve()), 'snapshot': str(snapshot),
                        'snapshot_sha256': digest(snapshot), 'evidence': evidence}
            write_json(root / 'identity.json', identity)
        print(root)
        return
    root = args.cache.resolve()
    identity = read_json(root / 'identity.json')
    config = config | {'program': identity.get('library', config['program'])}
    snapshot = Path(identity['snapshot'])
    with locked(root / 'writer.lock'):
        if args.command == 'index':
            if (root / 'index.jsonl').exists() and not args.refresh:
                count = import_index(root, identity)
                print(json.dumps({'reused_index': True, 'functions': count}))
                return
            if digest(snapshot) != identity['snapshot_sha256']:
                raise ValueError('Backup checksum mismatch')
            metrics = headless(config, root, snapshot, 'index', config.get('timeout_seconds', 20))
            metrics['functions'] = import_index(root, identity)
            write_json(root / 'index-metrics.json', metrics)
        else:
            sync_results(root)
            db = connect(root / 'cache.sqlite')
            limit = max(1, min(args.limit, 100))
            status = "status!='cached'" if args.retry_failed else "status='pending'"
            sql = f'SELECT address FROM functions WHERE {status} AND external=0'
            params = []
            if args.address:
                sql += ' AND address IN (' + ','.join('?' for _ in args.address) + ')'
                params.extend(args.address)
            elif not args.all:
                # アドレス順の等間隔サンプルで前半のthunk偏重を避ける。
                sql += ' AND thunk=0'
            sql += ' ORDER BY address'
            candidates = [row[0] for row in db.execute(sql, params)]
            db.close()
            selected = candidates if args.all else (candidates if args.address else
                        [candidates[i * len(candidates) // min(limit, len(candidates))]
                         for i in range(min(limit, len(candidates)))])[:limit]
            if not selected:
                print(json.dumps({'requested': 0, 'reused': True}))
                return
            if digest(snapshot) != identity['snapshot_sha256']:
                raise ValueError('Backup checksum mismatch')
            (root / 'requests.txt').write_text('\n'.join(selected), encoding='utf-8')
            tick = time.time_ns()
            try:
                metrics = headless(config, root, snapshot, 'decompile', config.get('timeout_seconds', 20))
            finally:
                sync_results(root)
            metrics['requested'] = len(selected)
            write_json(root / f'decompile-metrics-{tick}.json', metrics)
        print(json.dumps(metrics, indent=2))


if __name__ == '__main__':
    main()
