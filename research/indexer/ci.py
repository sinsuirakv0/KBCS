import argparse
import contextlib
import hashlib
import http.client
import itertools
import json
import os
import re
import shutil
import sqlite3
import subprocess
import tarfile
import tempfile
import time
import urllib.request
import zipfile
import zlib
from pathlib import Path

from indexer.apk import acquire, validate_split_source
from indexer.complete import build_reference
from indexer.network import ATTEMPTS, download_asset, gh, gh_json as api, http_status, retry, transient
from indexer.reference import export_cache, replace_reference
from indexer.run import headless, locked
from indexer.store import LOCAL, configure_output, digest, import_index, read_json, sync_results, write_json

REPO = 'sinsuirakv0/KBCS'
RESEARCH = Path(__file__).resolve().parents[1]
STATE = {'ci-plan.json', 'ci-status.json', 'identity.json', 'index.jsonl', 'results.jsonl',
         'cache.sqlite', 'reference-summary.json', 'analysis-complete.json', 'catalog.tsv',
         'external-functions.tsv', 'README.md', 'memory-events.jsonl', 'index.log', 'decompile.log'}
CHECKPOINT_NAME = re.compile(r'checkpoint-(\d+)-(\d+)-(\d+)\.tgz')
REQUIRED_STATE = {'ci-plan.json', 'identity.json', 'index.jsonl', 'cache.sqlite', 'analysis-complete.json'}
CHECKPOINT_BYTES = 4 * 1024**3
ASSET_BYTES = 2 * 1024**3
INVENTORY_BYTES = 64 * 1024**2


def public_only():
    # 有料実行への移行や、他repoへの書込を暗黙に許可しない。
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('RUNNER_ENVIRONMENT') != 'github-hosted':
        raise RuntimeError('Only the standard hosted Actions workflow may run this command')
    if os.environ.get('GITHUB_REPOSITORY') != REPO or api(f'repos/{REPO}')['private']:
        raise RuntimeError('Public KBCS is required; private execution is disabled')


def download_runtime(url, target):
    partial = target.with_suffix('.partial')
    with urllib.request.urlopen(url, timeout=120) as source, partial.open('wb') as output:
        shutil.copyfileobj(source, output, 1024 * 1024)
        length = source.headers.get('Content-Length')
        if length is not None and output.tell() < int(length):
            raise http.client.IncompleteRead(b'', int(length) - output.tell())
    return partial


def setup():
    root = LOCAL / 'runtime'
    root.mkdir(parents=True, exist_ok=True)
    runtime = read_json(RESEARCH / 'ghidra/runtime.json')
    for name in ('ghidra', 'apktool'):
        item = runtime[name]
        if not item['url'].startswith('https://github.com/') or not re.fullmatch('[a-f0-9]{64}', item['sha256']):
            raise ValueError('Invalid pinned runtime')
        target = root / ('ghidra.zip' if name == 'ghidra' else 'apktool.jar')
        downloaded = target if target.exists() else retry(lambda: download_runtime(item['url'], target), name)
        if digest(downloaded) != item['sha256']:
            raise ValueError('Runtime SHA-256 mismatch')
        if downloaded != target:
            downloaded.replace(target)
    ghidra = root / f"ghidra_{runtime['ghidra_version']}_PUBLIC"
    utility = Path('Ghidra/Framework/Utility/lib/Utility.jar')
    if not ghidra.exists():
        with tempfile.TemporaryDirectory(prefix='.runtime-', dir=root) as directory:
            staging = Path(directory).resolve()
            with zipfile.ZipFile(root / 'ghidra.zip') as archive:
                for member in archive.infolist():
                    if not (staging / member.filename).resolve().is_relative_to(staging) or (member.external_attr >> 16) & 0o170000 == 0o120000:
                        raise ValueError('Unsafe runtime ZIP member')
                archive.extractall(staging)
            extracted = staging / ghidra.name
            if not (extracted / utility).is_file():
                raise RuntimeError('Ghidra runtime is incomplete')
            # ZIP展開時にUnix実行属性が失われるため、公式のnative実行物だけに付ける。
            for folder in extracted.glob('Ghidra/*/*/os/linux_*'):
                for path in folder.iterdir():
                    if path.is_file():
                        path.chmod(path.stat().st_mode | 0o111)
            extracted.rename(ghidra)
    if not (ghidra / utility).is_file():
        raise RuntimeError('Ghidra runtime is incomplete')
    with open(os.environ['GITHUB_ENV'], 'a', encoding='utf-8') as output:
        output.write(f'GHIDRA_HOME={ghidra.resolve()}\nAPKTOOL={root.resolve() / "apktool.jar"}\n')


def load_input(path):
    path = path.resolve()
    if not path.is_relative_to((RESEARCH / 'inputs').resolve()):
        raise ValueError('Input must be a checked-in research/inputs manifest')
    data = read_json(path)
    if data.get('schemaVersion') not in (1, 2):
        raise ValueError('Unsupported source manifest schema')
    hashes = ('archiveSha256', 'librarySha256')
    if data['schemaVersion'] == 1:
        hashes += ('mergedApkSha256',)
    for key in hashes:
        if not re.fullmatch('[a-f0-9]{64}', data[key]):
            raise ValueError(f'Invalid {key}')
    if data['packageName'] != 'jp.co.ponos.battlecats' or not re.fullmatch(r'\d+\.\d+\.\d+', data['versionName']):
        raise ValueError('Invalid package/version')
    if not re.fullmatch(r'\d{6}', str(data['compactVersion'])) or (type(data['versionCode']) is not int or data['versionCode'] <= 0):
        raise ValueError('Invalid version code')
    if not re.fullmatch(r'[A-Za-z0-9_-]+', data['architecture']) or not re.fullmatch(r'lib[A-Za-z0-9_-]+\.so', data['library']):
        raise ValueError('Invalid ABI/library')
    if data['schemaVersion'] == 2:
        validate_split_source(data)
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


def release_state(tag):
    try:
        return api(f'repos/{REPO}/releases/tags/{tag}')
    except subprocess.CalledProcessError as error:
        if http_status(error) != 404:
            raise
        return None


def unpack_checkpoint(staging, name, assets, tag, revision):
    root = staging / 'cache'
    hashes = {}
    for filename, limit in ((name + '.json', INVENTORY_BYTES), (name, ASSET_BYTES)):
        if not 0 < assets[filename]['size'] < limit:
            raise ValueError('Checkpoint asset size out of bounds')
        download_asset(REPO, tag, filename, staging)
        path = staging / filename
        hashes[filename] = digest(path)
        if assets[filename].get('digest') != 'sha256:' + hashes[filename] or path.stat().st_size != assets[filename]['size']:
            raise ValueError('Checkpoint asset digest mismatch')
    manifest = read_json(staging / (name + '.json'))
    if manifest['revision'] != revision or hashes[name] != manifest['sha256']:
        raise ValueError('Checkpoint identity mismatch')
    expected = {entry['path']: entry for entry in manifest['files']}
    if len(expected) != len(manifest['files']) or not REQUIRED_STATE <= expected.keys():
        raise ValueError('Incomplete checkpoint inventory')
    seen, total = set(), 0
    with tarfile.open(staging / name, 'r|gz') as archive:
        for member in archive:
            total += member.size
            if not member.isfile() or not allowed(member.name) or member.name not in expected or member.name in seen or member.size < 0 or total > CHECKPOINT_BYTES:
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
    return root


def restore(root, tag, revision):
    release = release_state(tag)
    if release is None:
        return
    assets = {asset['name']: asset for asset in release['assets'] if asset['state'] == 'uploaded'}
    candidates = []
    for name, asset in assets.items():
        match = CHECKPOINT_NAME.fullmatch(name)
        if match and name + '.json' in assets:
            candidates.append((asset['created_at'], tuple(map(int, match.groups())), name))
    for _, _, name in sorted(candidates, reverse=True)[:3]:
        # 正常な一式が揃うまで、作業ディレクトリには一切反映しない。
        with tempfile.TemporaryDirectory(prefix='.checkpoint-', dir=root.parent) as directory:
            try:
                restored = unpack_checkpoint(Path(directory), name, assets, tag, revision)
            except (ValueError, KeyError, TypeError, tarfile.TarError, EOFError, zlib.error) as error:
                print(f'Rejected invalid checkpoint: {name} ({type(error).__name__})', flush=True)
                continue
            restored.rename(root)
            print(f'Restored checkpoint: {name}', flush=True)
            return
    if candidates:
        raise RuntimeError('No valid checkpoint among the latest three pairs; existing Release data was retained')


def upload_checkpoint(tag, archive, sidecar, archive_hash):
    for attempt in range(ATTEMPTS):
        expected = {archive.name: (archive.stat().st_size, archive_hash),
                    sidecar.name: (sidecar.stat().st_size, digest(sidecar))}
        try:
            gh('release', 'upload', tag, str(archive), str(sidecar), '--repo', REPO, timeout=300)
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as error:
            if not transient(error):
                raise
        release = release_state(tag)
        if release is None:
            raise RuntimeError('Checkpoint Release disappeared during upload')
        uploaded = {asset['name']: asset for asset in release['assets'] if asset['name'] in expected and asset['state'] == 'uploaded'}
        if any((asset['size'], asset.get('digest')) != (expected[name][0], 'sha256:' + expected[name][1])
               for name, asset in uploaded.items()):
            raise ValueError('Uploaded checkpoint verification failed')
        if uploaded.keys() == expected.keys():
            archive.unlink()
            sidecar.unlink()
            return
        if attempt + 1 < ATTEMPTS:
            # GitHub側に途中アセットが残っても、既存名を上書きせず別名で送る。
            print(f'Checkpoint upload incomplete, retrying ({attempt + 2}/{ATTEMPTS})', flush=True)
            time.sleep(2 ** (attempt + 1))
            prefix, sequence = archive.stem.rsplit('-', 1)
            next_archive = archive.with_name(f'{prefix}-{int(sequence) + 1}.tgz')
            next_sidecar = next_archive.with_name(next_archive.name + '.json')
            archive.rename(next_archive)
            sidecar.rename(next_sidecar)
            archive, sidecar = next_archive, next_sidecar
    raise RuntimeError('Checkpoint upload incomplete after bounded retries')


def checkpoint(root, tag, sequence):
    public_only()
    output = LOCAL / 'ci-delivery'
    output.mkdir(exist_ok=True)
    run_id, attempt = os.environ['GITHUB_RUN_ID'], os.environ['GITHUB_RUN_ATTEMPT']
    if not run_id.isdigit() or not attempt.isdigit():
        raise ValueError('Invalid run identity')
    archive = output / f'checkpoint-{run_id}-{attempt}-{sequence * ATTEMPTS}.tgz'
    files = []
    with tarfile.open(archive, 'w:gz', compresslevel=1) as target:
        for path in sorted(root.rglob('*')):
            name = path.relative_to(root).as_posix()
            if path.is_file() and allowed(name):
                files.append({'path': name, 'bytes': path.stat().st_size, 'sha256': digest(path)})
                target.add(path, arcname=name, recursive=False)
    if archive.stat().st_size >= ASSET_BYTES or sum(entry['bytes'] for entry in files) > CHECKPOINT_BYTES:
        raise RuntimeError('Checkpoint exceeds the free Release asset size limit; no paid fallback')
    sidecar = archive.with_name(archive.name + '.json')
    archive_hash = digest(archive)
    write_json(sidecar, {'revision': read_json(root / 'ci-plan.json')['revision'],
                        'sha256': archive_hash, 'files': files})
    if sidecar.stat().st_size >= INVENTORY_BYTES:
        raise RuntimeError('Checkpoint inventory exceeds the restore memory budget')
    upload_checkpoint(tag, archive, sidecar, archive_hash)


def select_functions(root, style):
    attempted = set()
    journal = root / 'results.jsonl'
    if journal.exists():
        with journal.open(encoding='utf-8') as stream:
            for line in stream:
                try:
                    row = json.loads(line)
                    if row.get('style') == style and row['status'] == 'failed':
                        attempted.add(row['address'])
                except ValueError:
                    continue
    sync_results(root)
    with contextlib.closing(sqlite3.connect(root / 'cache.sqlite')) as db:
        candidates = db.execute("SELECT address FROM functions WHERE external=0 AND status!='cached' ORDER BY address")
        return list(itertools.islice((row[0] for row in candidates if row[0] not in attempted), 1000))


def decompile_batch(config, root, binary, style, selected, timeout, deadline):
    (root / 'requests.txt').write_text('\n'.join(selected), encoding='utf-8')
    for attempt in range(2):
        try:
            metrics = headless(config | {'decompiler_style': style}, root, binary, 'decompile', timeout)
        except (RuntimeError, TimeoutError) as error:
            metrics = {'interrupted': True, 'reason': type(error).__name__}
        pending = select_functions(root, style)
        if pending != selected:
            if metrics.get('interrupted'):
                print(f'{style}: preserving completed functions after a batch interruption', flush=True)
            return pending, metrics
        if attempt or time.monotonic() >= deadline:
            raise RuntimeError(f'{style}: no function progress; resume from the last checkpoint')
        print(f'{style}: no function progress; restarting the batch once', flush=True)


def ensure_release(tag, version, revision):
    def create():
        if release_state(tag) is None:
            gh('release', 'create', tag, '--repo', REPO, '--target', os.environ['GITHUB_SHA'], '--prerelease', '--latest=false',
               '--title', f'Native analysis {version} / {revision}', '--notes',
               '機械抽出資料。意味は未確認。APK・SO・Ghidraプロジェクトを含みません。')

    retry(create, 'Create checkpoint Release')


def publish_reference(source, revision):
    public_only()
    # 最新mainの独立worktreeで、対象の版とABIの資料だけを更新する。
    git_remote(['git', 'fetch', 'origin', 'main'])
    work = Path(os.environ['RUNNER_TEMP']) / ('native-publish-' + revision)
    subprocess.run(['git', 'worktree', 'add', '--detach', str(work), 'origin/main'], check=True)
    replace_reference(source, work / 'research/reference')
    subprocess.run(['git', '-C', str(work), 'add', '--', 'research/reference'], check=True)
    diff = subprocess.run(['git', '-C', str(work), 'diff', '--cached', '--quiet', '--', 'research/reference'])
    if not diff.returncode:
        return
    if diff.returncode != 1:
        diff.check_returncode()
    subprocess.run(['gh', 'auth', 'setup-git'], check=True)
    for args in (['config', 'user.name', 'github-actions[bot]'], ['config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com']):
        subprocess.run(['git', '-C', str(work), *args], check=True)
    subprocess.run(['git', '-C', str(work), 'commit', '-q', '-m', f'Publish native analysis revision {revision}'], check=True)
    git_remote(['git', '-C', str(work), '-c', 'pack.threads=1', 'push', 'origin', 'HEAD:main'])


def git_remote(args):
    try:
        retry(lambda: subprocess.run(args, check=True, capture_output=True, timeout=300), 'Git reference delivery')
    except subprocess.CalledProcessError as error:
        if any(message in error.stderr for message in (b'non-fast-forward', b'fetch first')):
            raise RuntimeError('Main advanced during reference publication; re-run the same inputs') from error
        raise


def run(input_path, label, publish):
    public_only()
    data = load_input(input_path)
    total_mb = int(next(line.split()[1] for line in Path('/proc/meminfo').read_text().splitlines() if line.startswith('MemTotal:'))) // 1024
    java_home = Path(os.environ['JAVA_HOME'])
    java_version = subprocess.check_output([str(java_home / 'bin/java'), '-version'], stderr=subprocess.STDOUT, timeout=30).decode()
    settings = plan(data, label, java_version, total_mb)
    revision = settings['revision']
    root = LOCAL / 'cache' / data['versionName'] / data['architecture'] / (data['librarySha256'] + '-ci-' + revision)
    root.parent.mkdir(parents=True, exist_ok=True)
    tag = f"native-analysis-{data['versionName']}-{data['architecture']}-{revision}"
    with locked(root.with_suffix('.lock')):
        if root.exists():
            raise RuntimeError('Expected a fresh CI cache directory; start a new hosted run to restore the Release')
        restore(root, tag, revision)
        root.mkdir(exist_ok=True)
        if (root / 'ci-plan.json').exists() and read_json(root / 'ci-plan.json') != settings:
            raise ValueError('Restored plan does not match this input and tool configuration')
        write_json(root / 'ci-plan.json', settings)
        config = {'ghidra_home': os.environ['GHIDRA_HOME'], 'java_home': str(java_home), 'heap': settings['heap'],
                  'program': data['library'], 'native_memory_limit_mb': settings['native_memory_limit_mb'],
                  'analysis_timeout_seconds': 0, 'batch_timeout_seconds': 3600, 'script_batch_seconds': settings['script_batch_seconds']}
        sequence = 0
        deadline = time.monotonic() + 210 * 60
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
                ensure_release(tag, data['versionName'], revision)
                if not status:
                    write_json(root / 'ci-status.json', {'complete': False})
                    checkpoint(root, tag, sequence)
                    sequence += 1
                for style in ('decompile', 'conservative', 'minimal'):
                    selected = select_functions(root, style)
                    while selected and time.monotonic() < deadline:
                        selected, metrics = decompile_batch(config, root, binary, style, selected, settings['function_timeout_seconds'], deadline)
                        write_json(root / 'ci-status.json', {'complete': False, 'style': style, 'last_batch': metrics})
                        checkpoint(root, tag, sequence)
                        sequence += 1
                    if time.monotonic() >= deadline:
                        break
                if any(select_functions(root, style) for style in ('decompile', 'conservative', 'minimal')):
                    raise RuntimeError('Analysis incomplete. Re-run the same input and revision label to continue from the last checkpoint.')
                report = build_reference(root)
                if report['internal'].get('pending', 0):
                    raise RuntimeError('Pending functions remain')
                write_json(root / 'ci-status.json', {'complete': True, 'report': report})
                checkpoint(root, tag, sequence)
            source, report = export_cache(root, LOCAL / 'ci-reference')
            if publish:
                publish_reference(source, revision)
            print(json.dumps({'complete': True, 'revision': revision, 'release': tag, 'reference': str(source), 'summary': report}, ensure_ascii=False))
        except Exception:
            # 強制終了に備え、各バッチ直後の検証済みcheckpointもReleaseに残す。
            print(f'Check the last verified checkpoint in Release {tag} before retrying.', flush=True)
            raise


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
