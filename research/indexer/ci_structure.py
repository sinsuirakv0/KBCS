import os
import shutil
import subprocess
import tarfile
import tempfile
from pathlib import Path

from indexer.ci import ASSET_BYTES, REPO, index_digest, release_state
from indexer.network import download_asset, gh, retry
from indexer.run import headless
from indexer.store import LOCAL, digest, read_json, write_json
from matcher.structure import EXPORTER, structure_header


STRUCTURE = 'structure.jsonl.gz'
RECEIPT = 'structure-metrics.json'


def get_asset(tag, name, destination):
    state = release_state(tag)
    assets = state['assets'] if state else ()
    asset = next((row for row in assets if row['name'] == name and row['state'] == 'uploaded'), None)
    if not asset:
        return None
    if not 0 < asset['size'] < ASSET_BYTES:
        raise ValueError('Release asset size is outside the permitted range')
    destination.mkdir(parents=True, exist_ok=True)
    path = destination / name
    if not path.is_file():
        download_asset(REPO, tag, name, destination)
    if (path.stat().st_size, 'sha256:' + digest(path)) != (asset['size'], asset.get('digest')):
        raise ValueError('Release asset failed size or SHA-256 verification')
    return path


def deliver_asset(tag, path):
    checksum = digest(path)
    size = path.stat().st_size
    if not 0 < size < ASSET_BYTES:
        raise ValueError('Release asset exceeds the permitted size')

    def exists():
        state = release_state(tag)
        if state is None:
            raise ValueError('Analysis Release is missing')
        found = next((row for row in state['assets'] if row['name'] == path.name and row['state'] == 'uploaded'), None)
        if found and (found['size'], found.get('digest')) != (size, 'sha256:' + checksum):
            raise ValueError('Release already has a different asset under this name')
        return found is not None

    def upload():
        if not exists():
            try:
                gh('release', 'upload', tag, str(path), '--repo', REPO, timeout=300)
            except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
                if not exists():
                    raise
        if not exists():
            raise ConnectionError('Upload has no verified asset')

    retry(upload, 'Deliver checked analysis asset')


def source_id(cache, identity):
    return {'schema': 1, 'index_sha256': index_digest(cache / 'index.jsonl'), 'extractor_sha256': digest(EXPORTER),
            'identity': {k: identity[k] for k in ('version', 'architecture', 'sha256', 'analysis_revision')}}


def unpack(path, root, source):
    root.mkdir(parents=True, exist_ok=True)
    with tarfile.open(path, 'r:') as archive:
        entries = archive.getmembers()
        if {member.name for member in entries} != {RECEIPT, STRUCTURE} or len(entries) != 2 or any(
                not member.isfile() or not 0 < member.size < ASSET_BYTES for member in entries):
            raise ValueError('Invalid structure checkpoint inventory')
        if archive.getmember(RECEIPT).size > 16384:
            raise ValueError('Structure receipt is too large')
        for member in entries:
            with archive.extractfile(member) as stream, (root / member.name).open('wb') as output:
                shutil.copyfileobj(stream, output, 1024**2)
    metadata = read_json(root / RECEIPT)
    export = root / STRUCTURE
    if (metadata['source'] != source or metadata['sha256'] != digest(export)
            or structure_header(export)['sha256'] != source['identity']['sha256']):
        raise ValueError('Structure checkpoint does not match this analysis')
    return export, metadata['metrics']


def structure_checkpoint(cache, binary, data, identity, tag, destination, *, config=None, publish=False):
    source = source_id(cache, identity)
    name = 'native-structure-' + source['extractor_sha256'][:20] + '.tar'
    recovered = get_asset(tag, name, destination)
    if recovered:
        print(f'Restored structure checkpoint {tag}/{name}', flush=True)
        return unpack(recovered, destination, source)
    binary = binary() if callable(binary) else binary
    if digest(binary) != source['identity']['sha256']:
        raise ValueError('Structure extraction binary has the wrong SHA-256')
    if config is None:
        config = {'ghidra_home': os.environ['GHIDRA_HOME'], 'java_home': os.environ['JAVA_HOME'],
                  'program': data['library'], 'heap': '1536M', 'analysis_timeout_seconds': 0,
                  'batch_timeout_seconds': 2400, 'native_memory_limit_mb': 4096}
    destination.mkdir(parents=True, exist_ok=True)
    work = LOCAL / 'cache'
    work.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='structure-', dir=work) as temporary:
        # 完成済みの古い解析は隔離したGhidraプロジェクトで構造だけを復元する。
        root = cache if (cache / 'project/cache.gpr').is_file() else Path(temporary)
        metrics = headless(config | {'sha256': identity['sha256']}, root, binary, 'structure', 0,
                           initialize=root != cache)
        export = root / STRUCTURE
        metadata = {'source': source, 'sha256': digest(export), 'metrics': metrics}
        write_json(destination / RECEIPT, metadata)
        path = destination / name
        with tarfile.open(path, 'w') as archive:
            archive.add(export, arcname=STRUCTURE)
            archive.add(destination / RECEIPT, arcname=RECEIPT)
        result = unpack(path, destination, source)
        if publish:
            deliver_asset(tag, path)
        print(f'Structure saved: {tag}/{name} · {metrics["wall_seconds"]:.1f}s', flush=True)
    return result
