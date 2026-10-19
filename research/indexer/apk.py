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

from indexer.store import LOCAL, configure_output, digest, read_json, write_json

REPOSITORY = 'sinsuirakv0/battlecats-apk'
ASSETS = 'sinsuirakv0/KBC-rakv0-assets'
TAG = 'battlecats-jp-history'


def gh_json(endpoint):
    result = subprocess.run(['gh', 'api', endpoint], capture_output=True, check=True, timeout=90)
    return json.loads(result.stdout)


def content(repository, path):
    response = gh_json(f'repos/{repository}/contents/{path}')
    return json.loads(base64.b64decode(response['content']).decode('utf-8-sig'))


def manifest(apk, output, apktool, java):
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
    if not code or not name:
        raise ValueError('Cannot read manifest versionInfo')
    return {'packageName': root.attrib['package'],
            'versionName': root.attrib.get(namespace + 'versionName', name.group(1)),
            'versionCode': int(root.attrib.get(namespace + 'versionCode', code.group(1)))}


def acquire(apktool, java):
    version = content(ASSETS, 'jp/version.json')
    compact = str(version['compactVersion'])
    if not re.fullmatch(r'\d{6}', compact) or version['packageName'] != 'jp.co.ponos.battlecats':
        raise ValueError('Unexpected version metadata')
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
            if b'HTTP 404' not in (error.stderr or b''):
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
        archive = root / name
        if not archive.exists():
            staging = root / 'download'
            staging.mkdir(exist_ok=True)
            subprocess.run(['gh', 'release', 'download', TAG, '--repo', REPOSITORY,
                            '--pattern', name, '--dir', str(staging), '--clobber'],
                           check=True, timeout=900, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
    libraries = []
    with zipfile.ZipFile(apk) as source:
        for item in source.infolist():
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
            if header[:4] != b'\x7fELF':
                raise ValueError('Invalid ELF library')
            libraries.append({'architecture': parts[1], 'library': parts[2], 'sha256': digest(target),
                              'bytes': target.stat().st_size, 'elf_class': header[4],
                              'elf_machine': int.from_bytes(header[18:20], 'little' if header[5] == 1 else 'big'),
                              'path': str(target), 'container': 'merged app.apk'})
    report = {'version': version, 'manifest': actual, 'archive': archive_info,
              'reused_apk': reused, 'libraries': libraries, 'source_repository': REPOSITORY}
    write_json(root / 'verified.json', report)
    print(json.dumps(report, ensure_ascii=False, indent=2))


def main():
    configure_output()
    parser = argparse.ArgumentParser()
    parser.add_argument('--apktool', required=True, type=Path)
    parser.add_argument('--java', default='java')
    args = parser.parse_args()
    acquire(args.apktool.resolve(), args.java)


if __name__ == '__main__':
    main()
