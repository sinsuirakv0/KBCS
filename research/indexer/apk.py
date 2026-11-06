import argparse
import base64
import json
import re
import shutil
import subprocess
import tarfile
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path, PurePosixPath

from indexer.network import download_asset, gh_json, http_status
from indexer.store import LOCAL, configure_output, digest, read_json, write_json

REPOSITORY = 'sinsuirakv0/battlecats-apk'
ASSETS = 'sinsuirakv0/KBC-rakv0-assets'
TAG = 'battlecats-jp-history'


def content(repository, path):
    response = gh_json(f'repos/{repository}/contents/{path}')
    return json.loads(base64.b64decode(response['content']).decode('utf-8-sig'))


def manifest(apk, output, apktool, java, include_split=False):
    # manifestだけの小さなZIPを渡し、apktoolによるAPK全体のコピーを避ける。
    minimal = output.parent / (output.name + '.apk')
    with zipfile.ZipFile(apk) as source, zipfile.ZipFile(minimal, 'w') as target:
        target.writestr('AndroidManifest.xml', source.read('AndroidManifest.xml'))
    subprocess.run([java, '-Xmx256M', '-jar', str(apktool), 'd', '--only-manifest',
                    '--no-src', '--no-assets', '--jobs', '1', '-f',
                    '-o', str(output), str(minimal)], stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, check=True, timeout=180)
    root = ET.parse(output / 'AndroidManifest.xml').getroot()
    namespace = '{http://schemas.android.com/apk/res/android}'
    # apktoolはmanifestの版属性をapktool.ymlのversionInfoへ移す。
    info = (output / 'apktool.yml').read_text(encoding='utf-8')
    code = re.search(r'^  versionCode: [\'\"]?(\d+)[\'\"]?\s*$', info, re.MULTILINE)
    name = re.search(r'^  versionName: [\'\"]?(\d+\.\d+\.\d+)[\'\"]?\s*$', info, re.MULTILINE)
    split = root.attrib.get('split', '')
    if not code or (not name and not (include_split and split)):
        raise ValueError('Cannot read manifest versionInfo')
    result = {'packageName': root.attrib['package'],
              'versionName': root.attrib.get(namespace + 'versionName', name.group(1) if name else ''),
              'versionCode': int(root.attrib.get(namespace + 'versionCode', code.group(1)))}
    if include_split:
        result['split'] = split
    return result


def validate_split_source(version):
    if not re.fullmatch(rf"source-jp-{version['versionCode']}-[a-f0-9]{{16}}", version['archiveTag']):
        raise ValueError('Invalid split source Release tag')
    entries = (version['baseApk'], version['nativeApk'])
    if entries[0]['member'] == entries[1]['member']:
        raise ValueError('Expected distinct base and ABI APK members')
    for entry in entries:
        path = PurePosixPath(entry['member'])
        if not re.fullmatch(r'(?:\./)?[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\.apk', entry['member']) or '..' in path.parts:
            raise ValueError('Invalid APK member')
        if not re.fullmatch('[a-f0-9]{64}', entry['sha256']) or not 0 < entry['bytes'] < 2 * 1024**3:
            raise ValueError('Invalid APK member proof')
    if version['architecture'] != 'arm64-v8a' or version['nativeApk']['split'] != 'config.arm64_v8a':
        raise ValueError('Unsupported ABI split')
    if not 0 < version['archiveBytes'] < 2 * 1024**3 or not re.fullmatch('[a-f0-9]{64}', version['archiveSha256']):
        raise ValueError('Invalid source archive proof')


def acquire_split(apktool, java, version):
    validate_split_source(version)
    root = LOCAL / 'apk' / str(version['compactVersion'])
    root.mkdir(parents=True, exist_ok=True)
    archive = root / 'source.tar'
    tag, expected = version['archiveTag'], version['archiveSha256']
    downloaded = archive
    if not archive.exists():
        release = gh_json(f'repos/{REPOSITORY}/releases/tags/{tag}')
        asset = next((asset for asset in release['assets'] if asset['name'] == archive.name), None)
        if not asset or (asset['state'], asset['size'], asset.get('digest')) != ('uploaded', version['archiveBytes'], f'sha256:{expected}'):
            raise ValueError('Private Release does not match the pinned source archive')
        staging = root / 'download'
        staging.mkdir(exist_ok=True)
        download_asset(REPOSITORY, tag, archive.name, staging)
        downloaded = staging / archive.name
    if downloaded.stat().st_size != version['archiveBytes'] or digest(downloaded) != expected:
        raise ValueError('Source archive size/SHA-256 mismatch')
    if downloaded != archive:
        downloaded.replace(archive)
    with tarfile.open(archive, 'r:') as source:
        members = source.getmembers()
        for kind in ('base', 'native'):
            proof = version[kind + 'Apk']
            matched = [member for member in members if member.name == proof['member']]
            if len(matched) != 1 or not matched[0].isfile() or matched[0].size != proof['bytes']:
                raise ValueError(f'Invalid {kind} APK member')
            apk = root / (kind + '.apk')
            if not apk.exists() or digest(apk) != proof['sha256']:
                partial = apk.with_suffix('.partial')
                with source.extractfile(matched[0]) as stream, partial.open('wb') as output:
                    shutil.copyfileobj(stream, output, 1024 * 1024)
                if digest(partial) != proof['sha256']:
                    raise ValueError(f'{kind} APK SHA-256 mismatch')
                partial.replace(apk)
            actual = manifest(apk, root / (kind + '-manifest'), apktool, java, include_split=True)
            identity = {'packageName': version['packageName'], 'versionCode': version['versionCode'],
                        'versionName': version['versionName'] if kind == 'base' else '',
                        'split': proof.get('split', '')}
            if actual != identity:
                raise ValueError(f'{kind} APK manifest mismatch')
    entry = f"lib/{version['architecture']}/{version['library']}"
    libraries = extract_libraries(root / 'native.apk', root, version['nativeApk']['member'], entry)
    library = libraries[0]
    if library['sha256'] != version['librarySha256'] or (library['elf_class'], library['elf_machine']) != (2, 183):
        raise ValueError('AArch64 library does not match its pinned ELF/SHA-256')
    report = {'version': version, 'libraries': libraries, 'source_repository': REPOSITORY}
    write_json(root / 'verified.json', report)
    return report


def acquire(apktool, java, version=None):
    version = version if version is not None else content(ASSETS, 'jp/version.json')
    compact = str(version['compactVersion'])
    if not re.fullmatch(r'\d{6}', compact) or version['packageName'] != 'jp.co.ponos.battlecats':
        raise ValueError('Unexpected version metadata')
    if version.get('schemaVersion') == 2:
        return acquire_split(apktool, java, version)
    if not re.fullmatch(r'[a-f0-9]{64}', version['mergedApkSha256']):
        raise ValueError('Invalid APK hash')
    root = LOCAL / 'apk' / compact
    root.mkdir(parents=True, exist_ok=True)
    write_json(root / 'version.json', version)
    apk = root / 'app.apk'
    expected = version['mergedApkSha256']
    reused = apk.exists() and digest(apk) == expected
    archive_info = None
    if not reused:
        try:
            release = gh_json(f'repos/{REPOSITORY}/releases/tags/{TAG}')
        except subprocess.CalledProcessError as error:
            if http_status(error) != 404:
                raise
            release = {'assets': []}
        name = f'battlecats-jp-{compact}.tar.gz'
        asset = next((a for a in release['assets'] if a['name'] == name), None)
        if asset is None:
            # 実行履歴は読むだけで、ワークフローの起動は行わない。
            history = []
            for workflow in ('monitor-battlecats.yml', 'download-battlecats.yml'):
                runs = gh_json(f'repos/{REPOSITORY}/actions/workflows/{workflow}/runs?per_page=3')
                history.extend({k: run.get(k) for k in ('name', 'status', 'conclusion', 'html_url')}
                               for run in runs['workflow_runs'])
            write_json(root / 'workflow-status.json', history)
            raise RuntimeError('Archive missing; inspect workflow-status.json. No workflow dispatched.')
        checksum = (asset.get('digest') or '').removeprefix('sha256:')
        if not re.fullmatch(r'[a-f0-9]{64}', checksum):
            raise ValueError('Release SHA-256 digest missing')
        if version.get('archiveSha256') and checksum != version['archiveSha256']:
            raise ValueError('Pinned archive SHA-256 mismatch')
        archive = root / name
        if not archive.exists():
            staging = root / 'download'
            staging.mkdir(exist_ok=True)
            download_asset(REPOSITORY, TAG, name, staging)
            (staging / name).replace(archive)
        if archive.stat().st_size != asset['size'] or digest(archive) != checksum:
            raise ValueError('Archive size/SHA-256 mismatch; retained for inspection')
        archive_info = {'name': name, 'sha256': checksum, 'bytes': asset['size']}
        # 全体展開は避ける。tarfileの抽出先解決を使わずapp.apkだけをコピーする。
        candidates = []
        with tarfile.open(archive, 'r|gz') as source:
            for member in source:
                if PurePosixPath(member.name).name == 'app.apk' and member.isfile():
                    candidates.append(member.name)
                    if len(candidates) > 1:
                        raise ValueError('Ambiguous app.apk members')
                    if member.size > 2 * 1024**3:
                        raise ValueError('APK exceeds 2 GiB limit')
                    with source.extractfile(member) as stream, apk.with_suffix('.partial').open('wb') as target:
                        shutil.copyfileobj(stream, target, 1024 * 1024)
        if not candidates or digest(apk.with_suffix('.partial')) != expected:
            raise ValueError('Merged APK missing or SHA-256 mismatch')
        apk.with_suffix('.partial').replace(apk)
    actual = manifest(apk, root / 'manifest', apktool, java)
    if any(actual[key] != version[key] for key in actual):
        raise ValueError('Manifest identity mismatch')
    if archive_info is None and (root / 'verified.json').exists():
        archive_info = read_json(root / 'verified.json').get('archive')
    libraries = extract_libraries(apk, root, 'merged app.apk')
    report = {'version': version, 'manifest': actual, 'archive': archive_info,
              'reused_apk': reused, 'libraries': libraries, 'source_repository': REPOSITORY}
    write_json(root / 'verified.json', report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return report


def extract_libraries(apk, root, container, entry=None):
    libraries = []
    with zipfile.ZipFile(apk) as source:
        members = source.infolist()
        if entry is not None:
            members = [item for item in members if item.filename == entry]
            if len(members) != 1:
                raise ValueError('Expected a unique native library member')
        for item in members:
            parts = PurePosixPath(item.filename).parts
            if len(parts) != 3 or parts[0] != 'lib' or not parts[2].endswith('.so'):
                continue
            if not all(re.fullmatch(r'[A-Za-z0-9_.-]+', part) and part not in ('.', '..') for part in parts):
                raise ValueError('Unsafe library path')
            if item.file_size > 256 * 1024**2:
                raise ValueError('Library exceeds 256 MiB limit')
            target = root / 'libraries' / parts[1] / parts[2]
            target.parent.mkdir(parents=True, exist_ok=True)
            with source.open(item) as stream, target.with_suffix('.partial').open('wb') as output:
                shutil.copyfileobj(stream, output, 1024 * 1024)
            target.with_suffix('.partial').replace(target)
            with target.open('rb') as stream:
                header = stream.read(20)
            if len(header) != 20 or header[:4] != b'\x7fELF':
                raise ValueError('Invalid ELF library')
            libraries.append({'architecture': parts[1], 'library': parts[2], 'sha256': digest(target),
                              'bytes': target.stat().st_size, 'elf_class': header[4],
                              'elf_machine': int.from_bytes(header[18:20], 'little' if header[5] == 1 else 'big'),
                              'path': str(target), 'container': container})
    return libraries


def main():
    configure_output()
    parser = argparse.ArgumentParser()
    parser.add_argument('--apktool', required=True, type=Path)
    parser.add_argument('--java', default='java')
    parser.add_argument('--manifest', type=Path)
    args = parser.parse_args()
    acquire(args.apktool.resolve(), args.java, read_json(args.manifest) if args.manifest else None)


if __name__ == '__main__':
    main()
