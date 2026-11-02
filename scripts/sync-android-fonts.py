"""AOSP Android 16の標準欧文・日本語フォントを、字形を変えずWOFF2へ格納する。"""
import base64
from concurrent.futures import ThreadPoolExecutor
import hashlib
import io
import json
from pathlib import Path
from urllib.request import urlopen

from fontTools.ttLib import TTFont

root = Path(__file__).resolve().parents[1]
destination = root / 'ui/fonts'
cache = root / 'research/.local/font-1572/downloads'
destination.mkdir(exist_ok=True)
cache.mkdir(exist_ok=True)
sources = [
    ('roboto-fonts', 'c50938f329a44707b06b336166c95ec2aa49c331', 'Roboto-Regular.ttf', 'Roboto.woff2', None),
    ('noto-fonts', 'f1fe27f9777986e0f5973b4e6dda8be9dae49a95', 'notosanscjk/NotoSansCJK-Regular.ttc', 'NotoSansCJKJP.woff2', 0),
]


def download(repo, revision, path):
    url = f'https://android.googlesource.com/platform/external/{repo}/+/{revision}/{path}?format=TEXT'
    local = cache / (repo + '-' + Path(path).name)
    if not local.exists():
        local.write_bytes(base64.b64decode(urlopen(url, timeout=120).read()))
    return url, local.read_bytes()


def convert(source):
    repo, revision, path, output, index = source
    url, data = download(repo, revision, path)
    font = TTFont(io.BytesIO(data), fontNumber=index if index is not None else -1)
    font.recalcTimestamp = False
    font.flavor = 'woff2'
    font.save(destination / output)
    notice_path = str(Path(path).parent / 'NOTICE').replace('\\', '/')
    notice_url, notice = download(repo, revision, notice_path)
    (destination / (repo + '-NOTICE.txt')).write_bytes(notice)
    return {'source': url, 'sha256': hashlib.sha256(data).hexdigest(), 'collectionIndex': index,
            'output': output, 'outputSha256': hashlib.sha256((destination / output).read_bytes()).hexdigest(),
            'notice': notice_url}


with ThreadPoolExecutor(max_workers=2) as pool:
    records = list(pool.map(convert, sources))
(destination / 'sources.json').write_text(json.dumps(records, indent=2) + '\n', encoding='utf-8')
print(json.dumps(records, indent=2))
