import os
import re
import shutil
import subprocess
from argparse import Namespace
from pathlib import Path

from indexer.ci import REPO, acquire_input, release_state
from indexer.ci_delivery import link_comparison, restore_completed
from indexer.network import gh, retry
from indexer.reference import reference_path
from indexer.store import LOCAL, digest, read_json
from indexer.upstream import previous_reference
from matcher.report import build


def deliver_database(database, tag):
    checksum = digest(database)
    size = database.stat().st_size
    if not 0 < size < 2 * 1024**3:
        raise ValueError('Comparison database exceeds the Release asset limit')
    asset = database.with_name(f'function-matches-{checksum[:24]}.sqlite')
    shutil.copyfile(database, asset)

    def uploaded():
        release = release_state(tag)
        if release is None:
            raise RuntimeError('Comparison Release is missing')
        found = next((row for row in release['assets'] if row['name'] == asset.name and row['state'] == 'uploaded'), None)
        if found and (found['size'], found.get('digest')) != (size, 'sha256:' + checksum):
            raise ValueError('Comparison asset digest mismatch')
        return bool(found)

    def upload():
        if uploaded():
            return
        try:
            gh('release', 'upload', tag, str(asset), '--repo', REPO, timeout=300)
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            if not uploaded():
                raise
            return
        if not uploaded():
            raise ConnectionError('Comparison asset not visible after upload')

    retry(upload, 'Upload function matches')
    return asset.name, checksum


def write_comparison(source, metadata, tag, asset, checksum):
    old, new = (metadata['identities'][side] for side in ('old', 'new'))
    old_path = reference_path(old)
    old_link = Path(os.path.relpath(source.parents[2] / old_path / 'README.md', source)).as_posix()
    counts = {(row['external'], row['status']): row['count'] for row in metadata['coverage'] if row['side'] == 'old'}
    validation = metadata['validation']
    link = f'https://github.com/{REPO}/releases/download/{tag}/{asset}'
    lines = [f"# 関数対応 {old['version']} → {new['version']}", '',
             f"[旧版の解析資料]({old_link}) · [新版の解析資料](README.md) · [検索用SQLite]({link})", '',
             f"内部関数の採用 {counts.get((0, 'accepted'), 0):,} 組。旧版側の候補あり {counts.get((0, 'review'), 0):,} 件、候補なし {counts.get((0, 'unresolved'), 0):,} 件。",
             f"名前を隠した検証は正解 {validation['correct']:,}、誤対応 {validation['wrong']:,}、保留 {validation['abstained']:,} 件。", '',
             '対応先と根拠を調べるには `python -m cli.match show <旧アドレス> --db <SQLite>` を使う。`--side new` で新版から検索できる。',
             '本文差は復元表現の差を含む。候補がない関数も削除・追加とは断定しない。', '', f'SQLite SHA-256 `{checksum}`', '']
    (source / 'comparison.md').write_text('\n'.join(lines), encoding='utf-8-sig')
    link_comparison(source)


def build_comparison(data, root, source, tag):
    previous = previous_reference(data, REPO)
    if previous is None:
        print('No earlier published reference for this ABI', flush=True)
        return None
    revision = previous['analysis_revision']
    if not re.fullmatch('[a-f0-9]{16}', revision):
        raise ValueError('Invalid comparison baseline revision')
    old_tag = f"native-analysis-{previous['version']}-{previous['architecture']}-{revision}"
    old_root = root.with_name('previous')
    old_data, _ = restore_completed(old_tag, old_root)
    if digest(old_root / 'cache.sqlite') != previous['source_database_sha256']:
        raise ValueError('Published comparison baseline has no matching completed checkpoint')
    if old_data['librarySha256'] != previous['sha256']:
        raise ValueError('Comparison baseline library differs from the published reference')
    java_home = Path(os.environ['JAVA_HOME'])
    old_binary = Path(acquire_input(old_data, java_home)['path']).resolve()
    binary = Path(acquire_input(data, java_home)['path']).resolve()
    database = build(Namespace(old_cache=old_root, new_cache=root, old_binary=old_binary, new_binary=binary,
                               features=LOCAL / 'matching/features', output=None, decisions=None, validate=True))
    metadata = read_json(database.with_name('summary.json'))
    asset, checksum = deliver_database(database, tag)
    write_comparison(source, metadata, tag, asset, checksum)
    return previous
