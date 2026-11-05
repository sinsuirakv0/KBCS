import argparse
import contextlib
import hashlib
import json
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import tarfile
import time
import urllib.request
import zipfile
from pathlib import Path

from indexer.apk import acquire
from indexer.complete import build_reference
from indexer.reference import export_cache
from indexer.run import headless, locked
from indexer.store import LOCAL, configure_output, digest, import_index, read_json, sync_results, write_json

REPO = 'sinsuirakv0/KBCS'
RESEARCH = Path(__file__).resolve().parents[1]
STATE = {'ci-plan.json', 'ci-status.json', 'identity.json', 'index.jsonl', 'results.jsonl',
         'cache.sqlite', 'reference-summary.json', 'analysis-complete.json', 'catalog.tsv',
         'external-functions.tsv', 'README.md', 'memory-events.jsonl', 'index.log', 'decompile.log'}


def command(args, **kwargs):
    return subprocess.check_output(args, **kwargs)


def api(path):
    return json.loads(command(['gh', 'api', path], stderr=subprocess.DEVNULL))


def public_only():
    # 有料実行への移行や、他repoへの書込を暗黙に許可しない。
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('RUNNER_ENVIRONMENT') != 'github-hosted':
        raise RuntimeError('Only the standard hosted Actions workflow may run this command')
    if os.environ.get('GITHUB_REPOSITORY') != REPO or api(f'repos/{REPO}')['private']:
        raise RuntimeError('Public KBCS is required; private execution is disabled')


def setup():
    root = LOCAL / 'runtime'
    root.mkdir(parents=True, exist_ok=True)
    runtime = read_json(RESEARCH / 'ghidra/runtime.json')
    for name in ('ghidra', 'apktool'):
        item = runtime[name]
        if not item['url'].startswith('https://github.com/') or not re.fullmatch('[a-f0-9]{64}', item['sha256']):
            raise ValueError('Invalid pinned runtime')
        target = root / ('ghidra.zip' if name == 'ghidra' else 'apktool.jar')
        if not target.exists():
            with urllib.request.urlopen(item['url'], timeout=120) as source, target.with_suffix('.partial').open('wb') as output:
                shutil.copyfileobj(source, output, 1024 * 1024)
            target.with_suffix('.partial').replace(target)
        if digest(target) != item['sha256']:
            raise ValueError('Runtime SHA-256 mismatch')
    ghidra = root / f"ghidra_{runtime['ghidra_version']}_PUBLIC"
    if not (ghidra / 'Ghidra/application.properties').exists():
        with zipfile.ZipFile(root / 'ghidra.zip') as archive:
            for member in archive.infolist():
                if not (root / member.filename).resolve().is_relative_to(root.resolve()) or (member.external_attr >> 16) & 0o170000 == 0o120000:
                    raise ValueError('Unsafe runtime ZIP member')
            archive.extractall(root)
        # ZIP展開時にUnix実行属性が失われるため、公式のnative実行物だけに付ける。
        for directory in ghidra.glob('Ghidra/*/*/os/linux_*'):
            for path in directory.iterdir():
                if path.is_file():
                    path.chmod(path.stat().st_mode | 0o111)
    with open(os.environ['GITHUB_ENV'], 'a', encoding='utf-8') as output:
        output.write(f'GHIDRA_HOME={ghidra.resolve()}\nAPKTOOL={root.resolve() / "apktool.jar"}\n')


def load_input(path):
    path = path.resolve()
    if not path.is_relative_to((RESEARCH / 'inputs').resolve()):
        raise ValueError('Input must be a checked-in research/inputs manifest')
    data = read_json(path)
    if data.get('schemaVersion') != 1:
        raise ValueError('Unsupported source manifest schema')
    for key in ('mergedApkSha256', 'archiveSha256', 'librarySha256'):
        if not re.fullmatch('[a-f0-9]{64}', data[key]):
            raise ValueError(f'Invalid {key}')
    if data['packageName'] != 'jp.co.ponos.battlecats' or not re.fullmatch(r'\d+\.\d+\.\d+', data['versionName']):
        raise ValueError('Invalid package/version')
    if not re.fullmatch(r'\d{6}', str(data['compactVersion'])) or (type(data['versionCode']) is not int or data['versionCode'] <= 0):
        raise ValueError('Invalid version code')
    if not re.fullmatch(r'[A-Za-z0-9_-]+', data['architecture']) or not re.fullmatch(r'lib[A-Za-z0-9_-]+\.so', data['library']):
        raise ValueError('Invalid ABI/library')
    return data


def plan(data, label, java_version, total_mb):
    if not re.fullmatch(r'[A-Za-z0-9_-]{1,40}', label):
        raise ValueError('Invalid revision label')
    if total_mb < 6144:
        raise RuntimeError('At least 6 GiB RAM is required; no paid runner fallback')
    hashes = {str(path.relative_to(RESEARCH)): digest(path) for path in [
        *sorted((RESEARCH / 'indexer').glob('*.py')), RESEARCH / 'ghidra/ExportCache.java',
        RESEARCH / 'ghidra/runtime.json'] if not path.name.startswith('test_')}
    result = {'input': data, 'label': label, 'java': java_version, 'tools': hashes,
              'heap': '1024M', 'native_memory_limit_mb': min(8192, total_mb - 3072),
              'function_timeout_seconds': 900, 'script_batch_seconds': 1200, 'schema': 1}
    result['revision'] = hashlib.sha256(json.dumps(result, sort_keys=True).encode()).hexdigest()[:16]
    return result


def allowed(name):
    return name in STATE or bool(re.fullmatch(r'(code/[0-9a-f]+\.c|assembly/[0-9a-f]+\.asm)', name))


def index_digest(path):
    result = hashlib.sha256()
    with path.open(encoding='utf-8-sig') as source:
        for line in source:
            row = json.loads(line)
            if row['type'] == 'complete':
                continue
            if row['type'] == 'program':
                row = {key: row[key] for key in ('type', 'sha256', 'language', 'image_base', 'ghidra', 'function_count')}
            result.update(json.dumps(row, sort_keys=True, ensure_ascii=False).encode('utf-8'))
            result.update(b'\n')
    return result.hexdigest()


def restore(root, tag, revision):
    try:
        release = api(f'repos/{REPO}/releases/tags/{tag}')
    except subprocess.CalledProcessError as error:
        # 404だけを未作成と扱い、認証・通信障害を新規実行に置き換えない。
        probe = subprocess.run(['gh', 'api', f'repos/{REPO}/releases/tags/{tag}'], capture_output=True)
        if b'HTTP 404' in probe.stderr:
            return
        raise error
    assets = {asset['name']: asset for asset in release['assets'] if asset['state'] == 'uploaded'}
    names = sorted((name for name in assets if re.fullmatch(r'checkpoint-\d+-\d+-\d+\.tgz', name) and name + '.json' in assets),
                   key=lambda name: assets[name]['created_at'], reverse=True)
    if not names:
        return
    staging = LOCAL / 'ci-download'
    staging.mkdir(exist_ok=True)
    name = names[0]
    for filename in (name, name + '.json'):
        subprocess.run(['gh', 'release', 'download', tag, '--repo', REPO, '--pattern', filename,
                        '--dir', str(staging), '--clobber'], check=True, stdout=subprocess.DEVNULL)
        if assets[filename].get('digest') != 'sha256:' + digest(staging / filename):
            raise ValueError('Checkpoint asset digest mismatch')
    manifest = read_json(staging / (name + '.json'))
    if manifest['revision'] != revision or digest(staging / name) != manifest['sha256']:
        raise ValueError('Checkpoint identity mismatch')
    expected = {entry['path']: entry for entry in manifest['files']}
    seen, total = set(), 0
    with tarfile.open(staging / name, 'r|gz') as archive:
        for member in archive:
            total += member.size
            if not member.isfile() or not allowed(member.name) or member.name not in expected or member.name in seen or total > 4 * 1024**3:
                raise ValueError('Unsafe checkpoint member')
            target = (root / member.name).resolve()
            if not target.is_relative_to(root.resolve()) or member.size != expected[member.name]['bytes']:
                raise ValueError('Checkpoint path/size mismatch')
            target.parent.mkdir(parents=True, exist_ok=True)
            with archive.extractfile(member) as source, target.open('wb') as output:
                shutil.copyfileobj(source, output, 1024 * 1024)
            if digest(target) != expected[member.name]['sha256']:
                raise ValueError('Checkpoint file digest mismatch')
            seen.add(member.name)
    if seen != expected.keys() or read_json(root / 'ci-plan.json')['revision'] != revision:
        raise ValueError('Incomplete checkpoint')


def checkpoint(root, tag, sequence):
    public_only()
    output = LOCAL / 'ci-delivery'
    output.mkdir(exist_ok=True)
    run_id, attempt = os.environ['GITHUB_RUN_ID'], os.environ['GITHUB_RUN_ATTEMPT']
    if not run_id.isdigit() or not attempt.isdigit():
        raise ValueError('Invalid run identity')
    archive = output / f'checkpoint-{run_id}-{attempt}-{sequence}.tgz'
    files = []
    with tarfile.open(archive, 'w:gz', compresslevel=1) as target:
        for path in sorted(root.rglob('*')):
            name = path.relative_to(root).as_posix()
            if path.is_file() and allowed(name):
                files.append({'path': name, 'bytes': path.stat().st_size, 'sha256': digest(path)})
                target.add(path, arcname=name, recursive=False)
    if archive.stat().st_size >= 2 * 1024**3:
        raise RuntimeError('Checkpoint exceeds the free Release asset size limit; no paid fallback')
    sidecar = archive.with_name(archive.name + '.json')
    write_json(sidecar, {'revision': read_json(root / 'ci-plan.json')['revision'],
                        'sha256': digest(archive), 'files': files})
    subprocess.run(['gh', 'release', 'upload', tag, str(archive), str(sidecar), '--repo', REPO], check=True)
    release = api(f'repos/{REPO}/releases/tags/{tag}')
    for path in (archive, sidecar):
        asset = next(item for item in release['assets'] if item['name'] == path.name)
        if asset['state'] != 'uploaded' or asset['size'] != path.stat().st_size or asset.get('digest') != 'sha256:' + digest(path):
            raise ValueError('Uploaded checkpoint verification failed')
    # 自分の配信用一時ファイルだけを除去し、実行機のディスクを圧迫しない。
    archive.unlink()
    sidecar.unlink()


def select_functions(root, style):
    attempted = set()
    journal = root / 'results.jsonl'
    if journal.exists():
        for line in journal.read_text(encoding='utf-8').splitlines():
            try:
                row = json.loads(line)
                if row.get('style') == style:
                    attempted.add(row['address'])
            except ValueError:
                continue
    sync_results(root)
    with contextlib.closing(sqlite3.connect(root / 'cache.sqlite')) as db:
        candidates = db.execute("SELECT address FROM functions WHERE external=0 AND status!='cached' ORDER BY address")
        return [row[0] for row in candidates if row[0] not in attempted][:1000]


def publish_reference(source, revision):
    public_only()
    # 最新mainの独立worktreeへ資料だけを追記する。アプリの差分を混ぜない。
    subprocess.run(['git', 'fetch', 'origin', 'main'], check=True)
    work = Path(os.environ['RUNNER_TEMP']) / ('native-publish-' + revision)
    subprocess.run(['git', 'worktree', 'add', '--detach', str(work), 'origin/main'], check=True)
    target = work / 'research/reference' / source.relative_to(LOCAL / 'ci-reference')
    if target.exists():
        left = {p.relative_to(source).as_posix(): digest(p) for p in source.rglob('*') if p.is_file()}
        right = {p.relative_to(target).as_posix(): digest(p) for p in target.rglob('*') if p.is_file()}
        if left != right:
            raise ValueError('Published revision is immutable; choose another revision label')
        return
    shutil.copytree(source, target)
    reference = work / 'research/reference'
    datasets = sorted([*reference.glob('*/*/*/manifest.json'), *reference.glob('*/*/*/*/manifest.json')])
    text = '# ネイティブ解析資料\n\n' + ''.join(f'- [{p.parent.relative_to(reference).as_posix()}]({p.parent.relative_to(reference).as_posix()}/README.md)\n' for p in datasets)
    (reference / 'README.md').write_text(text, encoding='utf-8-sig')
    shutil.copyfile(LOCAL / 'ci-reference/.gitattributes', reference / '.gitattributes')
    subprocess.run(['gh', 'auth', 'setup-git'], check=True)
    for args in (['config', 'user.name', 'github-actions[bot]'], ['config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com'],
                 ['add', '--', 'research/reference']):
        subprocess.run(['git', '-C', str(work), *args], check=True)
    subprocess.run(['git', '-C', str(work), 'commit', '-q', '-m', f'Add native analysis revision {revision}'], check=True)
    subprocess.run(['git', '-C', str(work), '-c', 'pack.threads=1', 'push', 'origin', 'HEAD:main'], check=True)


def run(input_path, label, publish):
    public_only()
    data = load_input(input_path)
    total_mb = int(next(line.split()[1] for line in Path('/proc/meminfo').read_text().splitlines() if line.startswith('MemTotal:'))) // 1024
    java_home = Path(os.environ['JAVA_HOME'])
    java_version = command([str(java_home / 'bin/java'), '-version'], stderr=subprocess.STDOUT).decode()
    settings = plan(data, label, java_version, total_mb)
    revision = settings['revision']
    root = LOCAL / 'cache' / data['versionName'] / data['architecture'] / (data['librarySha256'] + '-ci-' + revision)
    root.mkdir(parents=True, exist_ok=True)
    tag = f"native-analysis-{data['versionName']}-{data['architecture']}-{revision}"
    with locked(root / 'writer.lock'):
        restore(root, tag, revision)
        if (root / 'ci-plan.json').exists() and read_json(root / 'ci-plan.json') != settings:
            raise ValueError('Restored plan does not match this input and tool configuration')
        write_json(root / 'ci-plan.json', settings)
        config = {'ghidra_home': os.environ['GHIDRA_HOME'], 'java_home': str(java_home), 'heap': settings['heap'],
                  'program': data['library'], 'native_memory_limit_mb': settings['native_memory_limit_mb'],
                  'analysis_timeout_seconds': 0, 'batch_timeout_seconds': 3600, 'script_batch_seconds': settings['script_batch_seconds']}
        sequence, completed = 0, False
        started = time.monotonic()
        try:
            status = read_json(root / 'ci-status.json') if (root / 'ci-status.json').exists() else {}
            if not status.get('complete'):
                token = os.environ.get('BATTLECATS_APK_READ_TOKEN')
                if not token:
                    raise RuntimeError('BATTLECATS_APK_READ_TOKEN is required (source repository read only)')
                previous = os.environ.get('GH_TOKEN')
                try:
                    os.environ['GH_TOKEN'] = token
                    verified = acquire(Path(os.environ['APKTOOL']), str(java_home / 'bin/java'), data)
                finally:
                    if previous is None:
                        os.environ.pop('GH_TOKEN', None)
                    else:
                        os.environ['GH_TOKEN'] = previous
                library = next(row for row in verified['libraries'] if row['architecture'] == data['architecture'] and row['library'] == data['library'])
                if library['sha256'] != data['librarySha256']:
                    raise ValueError('Pinned native library SHA-256 mismatch')
                binary = Path(library['path']).resolve()
                if shutil.disk_usage(root).free < 3 * 1024**3:
                    raise RuntimeError('Insufficient runner disk; no paid storage fallback')
                if not (root / 'project/cache.gpr').exists():
                    old_index = index_digest(root / 'index.jsonl') if (root / 'index.jsonl').exists() else None
                    metrics = headless(config, root, binary, 'index', 900, initialize=True)
                    with (root / 'index.jsonl').open(encoding='utf-8-sig') as stream:
                        header = json.loads(stream.readline())
                    if header['analysis_timed_out'] or not header['analysis_marked_complete']:
                        raise RuntimeError('Ghidra analysis did not complete')
                    if old_index and old_index != index_digest(root / 'index.jsonl'):
                        raise RuntimeError('Rebuilt index changed; refuse to reuse cached pseudocode')
                    identity = {'version': data['versionName'], 'version_code': data['versionCode'], 'architecture': data['architecture'],
                                'sha256': library['sha256'], 'library': data['library'], 'analysis_revision': revision,
                                'analysis_timed_out': False, 'snapshot_format': 'ephemeral_project', 'source_manifest': data}
                    import_index(root, identity)
                    write_json(root / 'identity.json', identity)
                    write_json(root / 'analysis-complete.json', metrics | {'index_sha256': index_digest(root / 'index.jsonl')})
                exists = subprocess.run(['gh', 'release', 'view', tag, '--repo', REPO], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
                if not exists:
                    subprocess.run(['gh', 'release', 'create', tag, '--repo', REPO, '--target', os.environ['GITHUB_SHA'], '--prerelease', '--latest=false',
                                    '--title', f"Native analysis {data['versionName']} / {revision}", '--notes', '機械抽出資料。意味は未確認。APK・SO・Ghidraプロジェクトを含みません。'], check=True)
                checkpoint(root, tag, sequence)
                sequence += 1
                for style in ('decompile', 'conservative', 'minimal'):
                    while time.monotonic() - started < 210 * 60:
                        selected = select_functions(root, style)
                        if not selected:
                            break
                        (root / 'requests.txt').write_text('\n'.join(selected), encoding='utf-8')
                        try:
                            metrics = headless(config | {'decompiler_style': style}, root, binary, 'decompile', settings['function_timeout_seconds'])
                        finally:
                            sync_results(root)
                        write_json(root / 'ci-status.json', {'complete': False, 'style': style, 'last_batch': metrics})
                        checkpoint(root, tag, sequence)
                        sequence += 1
                    if time.monotonic() - started >= 210 * 60:
                        break
                remaining = any(select_functions(root, style) for style in ('decompile', 'conservative', 'minimal'))
                if remaining:
                    print('Checkpoint saved. Re-run the same input and revision label to continue.', flush=True)
                    return
                report = build_reference(root)
                if report['internal'].get('pending', 0):
                    raise RuntimeError('Pending functions remain')
                write_json(root / 'ci-status.json', {'complete': True, 'report': report})
            source, report = export_cache(root, LOCAL / 'ci-reference')
            checkpoint(root, tag, sequence)
            completed = True
            if publish:
                publish_reference(source, revision)
            print(json.dumps({'complete': True, 'revision': revision, 'release': tag, 'reference': str(source), 'summary': report}, ensure_ascii=False))
        finally:
            # 強制終了に備え、各バッチ直後の検証済みcheckpointもReleaseに残す。
            if not completed and (root / 'identity.json').exists():
                print('The last uploaded checkpoint remains available; partial local state is not published.', flush=True)


def main():
    configure_output()
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=('setup', 'run'))
    parser.add_argument('--manifest', type=Path, default=RESEARCH / 'inputs/jp-1507021.json')
    parser.add_argument('--label', default='ci-v1')
    parser.add_argument('--publish', action='store_true')
    args = parser.parse_args()
    if args.action == 'setup':
        public_only()
        setup()
    else:
        run(args.manifest, args.label, args.publish)


if __name__ == '__main__':
    main()
