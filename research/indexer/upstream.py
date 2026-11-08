import argparse
import json
import os
import re
import subprocess
import urllib.request

from indexer.apk import ASSETS, REPOSITORY, content, validate_split_source
from indexer.network import gh_json, http_status, retry
from indexer.store import LOCAL, read_json, write_json


PACKAGE = 'jp.co.ponos.battlecats'
ABI = 'arm64-v8a'
LIBRARY = 'libnative-lib.so'
SIGNER = 'baf876d554213331c6fe5f6bbf9ae9af2f95c20e82b14bc232b0ac3a77680cb1'


def version_identity(current):
    name, code = current['versionName'], current['versionCode']
    if (current.get('status'), current.get('sourceRegion')) != ('verified', 'jp'):
        raise ValueError('Assets current is not a verified JP publication')
    if not re.fullmatch(r'[1-9]\d\.\d{1,2}\.\d{1,2}', name) or type(code) is not int or code <= 0:
        raise ValueError('Invalid assets version')
    if not re.fullmatch(rf'jp-{code}-[a-f0-9]{{16}}', current['datasetId']):
        raise ValueError('Invalid assets dataset identity')
    return name, code


def source_input(current, proof):
    name, code = version_identity(current)
    archive = proof['sourceArchive']
    if (archive['provider'], archive['repository'], archive['tag']) != (
            'github-release', REPOSITORY, 'source-' + current['datasetId']):
        raise ValueError('Assets proof points to an unexpected archive')
    verified = proof['proof']
    if proof.get('schemaVersion') != 1 or verified['source'] != 'google-play':
        raise ValueError('Unsupported APK proof')
    base = {'packageName': PACKAGE, 'versionCode': code, 'versionName': name, 'split': ''}
    if proof['manifest'] != base:
        raise ValueError('Assets current and APK proof disagree')
    data = {'schemaVersion': 2, 'packageName': PACKAGE, 'versionName': name, 'versionCode': code,
            'compactVersion': ''.join(f'{int(part):02d}' for part in name.split('.')),
            'archiveTag': archive['tag'], 'archiveBytes': archive['size'], 'archiveSha256': archive['sha256'],
            'architecture': ABI, 'library': LIBRARY, 'source': 'google-play', 'signingCertificateSha256': SIGNER}
    for key, split in (('baseApk', ''), ('nativeApk', 'config.arm64_v8a')):
        entries = [entry for entry in verified['splits'] if entry['manifest']['split'] == split]
        expected = base if not split else base | {'versionName': '', 'split': split}
        if len(entries) != 1 or entries[0]['manifest'] != expected:
            raise ValueError(f'Invalid {key} identity in assets proof')
        entry = entries[0]
        if entry['signatureVerified'] is not True or entry['certificateSha256'] != SIGNER:
            raise ValueError(f'Unexpected {key} signing proof')
        data[key] = {'member': './' + entry['name'], 'bytes': entry['size'], 'sha256': entry['sha256']}
        if split:
            data[key]['split'] = split
    validate_split_source(data)
    return data


def snapshot(assets_commit=None):
    def read_public(url):
        with urllib.request.urlopen(url, timeout=30) as response:
            raw = response.read(2 * 1024**2 + 1)
        if len(raw) > 2 * 1024**2:
            raise ValueError('Assets metadata exceeds the size limit')
        return json.loads(raw.decode('utf-8-sig'))

    latest = retry(lambda: read_public(f'https://api.github.com/repos/{ASSETS}/git/ref/heads/main'), 'Assets main')['object']['sha']
    commit = assets_commit or latest
    if not re.fullmatch('[a-f0-9]{40}', commit):
        raise ValueError('Invalid assets commit')
    root = f'https://raw.githubusercontent.com/{ASSETS}/{commit}/metadata/jp'
    current = retry(lambda: read_public(f'{root}/current.json'), 'Assets current')
    _, code = version_identity(current)
    if commit != latest:
        canonical = retry(lambda: read_public(f'https://raw.githubusercontent.com/{ASSETS}/{latest}/metadata/jp/current.json'), 'Latest assets current')
        if (current['versionName'], current['datasetId']) != (canonical['versionName'], canonical['datasetId']):
            print(f'Assets event {commit} was superseded; the latest publication will be checked separately', flush=True)
            return None, commit
    proof = retry(lambda: read_public(f'{root}/versions/{code}.proof.json'), 'Assets proof')
    return source_input(current, proof), commit


def reference_at(repository, ref, version, architecture, library):
    root = f'research/reference/{version}/{architecture}'
    try:
        dirs = gh_json(f'repos/{repository}/contents/{root}?ref={ref}')
    except subprocess.CalledProcessError as error:
        if http_status(error) == 404:
            return None
        raise
    if len(dirs) != 1 or dirs[0]['type'] != 'dir' or not re.fullmatch('[a-f0-9]{64}', dirs[0]['name']):
        raise ValueError('Unexpected published reference layout')
    sha = dirs[0]['name']
    manifest = content(repository, f'{root}/{sha}/manifest.json?ref={ref}')
    if manifest['format'] != 2 or (manifest['version'], manifest['architecture'], manifest['sha256'], manifest['library']) != (
            version, architecture, sha, library):
        raise ValueError('Published reference identity mismatch')
    return manifest


def matching_publication(data, repository, inputs):
    ref = gh_json(f'repos/{repository}/git/ref/heads/main')['object']['sha']
    manifest = reference_at(repository, ref, data['versionName'], data['architecture'], data['library'])
    if manifest is None:
        return None
    if 'source_archive_sha256' in manifest:
        if (manifest['source_archive_sha256'], manifest['source_version_code']) == (data['archiveSha256'], data['versionCode']):
            return manifest
        return None
    # 既存の公開版は固定台帳とSOの組で照合する。
    for path in inputs.glob('jp-*.json'):
        previous = read_json(path)
        if (previous['versionCode'], previous['archiveSha256'], previous['librarySha256']) == (
                data['versionCode'], data['archiveSha256'], manifest['sha256']):
            return manifest
    return None


def previous_references(data, repository, limit=2):
    def version_key(name):
        return tuple(map(int, name.split('.')))

    ref = gh_json(f'repos/{repository}/git/ref/heads/main')['object']['sha']
    current = version_key(data['versionName'])
    entries = gh_json(f'repos/{repository}/contents/research/reference?ref={ref}')
    versions = [entry['name'] for entry in entries if entry['type'] == 'dir'
                and re.fullmatch(r'\d+\.\d+\.\d+', entry['name'])
                and version_key(entry['name']) < current]
    result = []
    for version in sorted(versions, key=version_key, reverse=True):
        previous = reference_at(repository, ref, version, data['architecture'], data['library'])
        if previous:
            result.append(previous)
            if len(result) == limit:
                break
    return list(reversed(result))


def tracking_sources(versions):
    return [{key: version[key] for key in ('version', 'architecture', 'sha256', 'analysis_revision')}
            for version in versions]


def main():
    from indexer.ci import REPO, RESEARCH, public_only

    parser = argparse.ArgumentParser()
    parser.add_argument('--check-only', action='store_true')
    parser.add_argument('--assets-commit')
    args = parser.parse_args()
    public_only()
    data, commit = snapshot(args.assets_commit)
    if data is None:
        return
    manifest = matching_publication(data, REPO, RESEARCH / 'inputs')
    state = 'new' if manifest is None else manifest.get('comparison_state', 'complete')
    if manifest and state != 'pending':
        expected = tracking_sources([*previous_references(data, REPO), manifest])
        if manifest.get('tracking_format') != 2 or manifest.get('tracking_sources') != expected:
            state = 'pending'
    print(f"Assets {data['versionName']} / {data['versionCode']} at {commit}; state: {state}", flush=True)
    if args.check_only:
        return
    with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as output:
        if state == 'new':
            write_json(LOCAL / 'ci-upstream.json', data)
            output.write('needed=true\n')
        elif state == 'pending':
            revision = manifest['analysis_revision']
            if not re.fullmatch('[a-f0-9]{16}', revision):
                raise ValueError('Invalid published revision')
            output.write(f"checkpoint=native-analysis-{data['versionName']}-{data['architecture']}-{revision}\n")
            output.write('match_only=true\n')


if __name__ == '__main__':
    main()
