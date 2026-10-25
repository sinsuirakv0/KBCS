from pathlib import Path
import argparse
import hashlib
import json
import re
import subprocess

# 固定commitの検証済み索引から、APKに同梱されたBGMだけを補う。
parser = argparse.ArgumentParser()
parser.add_argument('--revision', required=True)
args = parser.parse_args()
assert re.fullmatch(r'[0-9a-f]{40}', args.revision)
root = Path(__file__).resolve().parents[1]
repository = 'sinsuirakv0/KBC-rakv0-assets'
cache = root / 'research/.local/music-index' / args.revision
cache.mkdir(parents=True, exist_ok=True)

def read(path):
    target = cache / hashlib.sha256(path.encode()).hexdigest()
    if not target.exists():
        data = subprocess.check_output(['gh', 'api', f'repos/{repository}/contents/{path}?ref={args.revision}', '-H', 'Accept: application/vnd.github.raw+json'])
        target.write_bytes(data)
    return target.read_bytes()

def checked(path, descriptor):
    data = read(path)
    assert hashlib.sha256(data).hexdigest() == descriptor['sha256'], path
    assert 'size' not in descriptor or len(data) == descriptor['size'], path
    return data

current = json.loads(read('metadata/jp/current.json'))
assert current['status'] == 'verified' and current['versionName'] == '15.7.2'
base = current['generatedPath']
manifest = json.loads(checked(base+'/manifest.json', {'sha256': current['manifestSha256']}))
index = json.loads(checked(base+'/indexes/assets.json', manifest['artifacts']['indexes/assets.json']))
assert index['header'] == manifest['header']
settings = index['files']['Data/Sound_setting.tsv']
rows = checked(settings['path'], settings).decode('utf-8-sig').splitlines()[1:]
target = root / 'crates/kbcs-data/resources/stage-music.json'
catalog = json.loads(target.read_text(encoding='utf-8-sig'))
native = {}
for logical, descriptor in index['files'].items():
    match = re.fullmatch(r'assets/snd(\d+)\.ogg', logical)
    if not match:
        continue
    number = int(match[1])
    assert rows[number].split('\t')[0] == '1', logical
    track = catalog['tracks'].get(str(number), {'id': number, 'name': ''}).copy()
    track.update(repository=repository, revision=args.revision, path=descriptor['path'], sha256=descriptor['sha256'], size=descriptor['size'], mime='audio/ogg', loop=rows[number].split('\t')[1] == '1', url=f"https://raw.githubusercontent.com/{repository}/{args.revision}/{descriptor['path']}")
    catalog['tracks'][str(number)] = track
    native[str(number)] = descriptor
catalog['nativeSource'] = {'repository': repository, 'revision': args.revision, 'buildId': current['buildId'], 'manifestSha256': current['manifestSha256'], 'indexSha256': manifest['artifacts']['indexes/assets.json']['sha256'], 'settings': settings, 'tracks': native}
target.write_text(json.dumps(catalog, ensure_ascii=False, indent=2)+'\n', encoding='utf-8-sig')
print(json.dumps({'nativeBgm': len(native), 'ids': list(map(int, native))}))
