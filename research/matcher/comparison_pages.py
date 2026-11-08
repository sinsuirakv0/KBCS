import os
import re
from pathlib import Path

from indexer.reference import GIT_FILE_LIMIT, function_path, reference_path
from indexer.store import read_json, write_json


DIRECTIONS = {'previous': 'next', 'next': 'previous'}
COMPARISON_LINK = '[直前の公開版との関数対応](comparison.md)'


def relative_link(target, page):
    return Path(os.path.relpath(target, page.parent)).as_posix()


def overlay(path, direction, link, heading):
    if path.is_symlink() or path.parent.resolve() != path.parent.absolute():
        raise ValueError(f'Unsafe reference page path: {path}')
    before = path.read_bytes()
    text = before.decode('utf-8-sig')
    header, separator, body = text.partition(heading)
    if not separator:
        raise ValueError(f'Unexpected reference page format: {path}')
    start, end = f'<!-- kbcs-version-{direction} -->', f'<!-- /kbcs-version-{direction} -->'
    block = f'{start}\n{link}\n{end}\n\n' if link else ''
    header, replaced = re.subn(rf'^{start}\n.*?^{end}\n\n', lambda _: block, header, flags=re.MULTILINE | re.DOTALL)
    if not replaced:
        header += block
    content = (header + separator + body).encode('utf-8-sig')
    if len(content) > GIT_FILE_LIMIT:
        raise ValueError(f'Linked page exceeds Git file limit: {path}')
    if content != before:
        path.write_bytes(content)


def catalog_path(source, direction):
    return source / 'version-links' / (direction + '.json')


def render_links(source, direction, catalog, previous=None):
    own = Path(*source.parts[-3:])
    previous_addresses = {row[0] for row in previous['rows']} if previous else set()
    rows = {row[0]: row[1:] for row in catalog['rows']} if catalog else {}
    index_link = ''
    if catalog:
        peer = reference_path(catalog['peer'])
        newer = own if direction == 'previous' else peer
        change_index = newer / 'changes/README.md'
        version = catalog['peer']['version']
        label = '前の版からの変更' if direction == 'previous' else '次の版への変更'
        index_link = f'- [{label} · v{version}]({relative_link(change_index, own / "README.md")})'
    for address in sorted(previous_addresses | rows.keys()):
        page = own / function_path(address)
        link = ''
        if address in rows:
            other, changed = rows[address]
            link = f'**別版の対応** [v{version} `{other}`]({relative_link(peer / function_path(other), page)})'
            if changed:
                diff_address = address if direction == 'previous' else other
                diff = newer / 'changes' / (diff_address + '.md')
                link += f' · [本文差分]({relative_link(diff, page)})'
        overlay(source / function_path(address), direction, link, '## 関数情報\n')
    overlay(source / 'README.md', direction, index_link, '## アドレス索引\n')


def remove_change_pages(source, catalog):
    changes = source / 'changes'
    if changes.resolve() != changes.absolute():
        raise ValueError(f'Unsafe change directory: {changes}')
    for address, _, changed in catalog['rows']:
        if changed:
            (changes / function_path(address).name).unlink(missing_ok=True)
    (changes / 'README.md').unlink(missing_ok=True)


def disconnect(reference, source, direction, *, replacing=False):
    path = catalog_path(source, direction)
    if not path.is_file():
        return
    catalog = read_json(path)
    peer = reference / reference_path(catalog['peer'])
    inverse = DIRECTIONS[direction]
    peer_path = catalog_path(peer, inverse)
    if not replacing:
        render_links(source, direction, None, catalog)
        if direction == 'previous':
            remove_change_pages(source, catalog)
        path.unlink()
    if peer_path.is_file():
        reciprocal = read_json(peer_path)
        if reference_path(reciprocal['peer']) == Path(*source.parts[-3:]):
            render_links(peer, inverse, None, reciprocal)
            peer_path.unlink()
            if inverse == 'previous':
                remove_change_pages(peer, reciprocal)
                (peer / 'comparison.md').unlink(missing_ok=True)
                readme = peer / 'README.md'
                text = readme.read_bytes().replace(('\n' + COMPARISON_LINK + '\n').encode(), b'')
                readme.write_bytes(text)
                manifest = read_json(peer / 'manifest.json')
                manifest['comparison_state'] = 'pending'
                write_json(peer / 'manifest.json', manifest)


def carry_links(previous, source):
    for direction in DIRECTIONS:
        path = catalog_path(previous, direction)
        if path.is_file():
            catalog = read_json(path)
            if direction == 'previous':
                changes = source / 'changes'
                changes.mkdir(exist_ok=True)
                for name in ['README.md', *(function_path(a).name for a, _, changed in catalog['rows'] if changed)]:
                    (changes / name).write_bytes((previous / 'changes' / name).read_bytes())
            render_links(source, direction, catalog)
            write_json(catalog_path(source, direction), catalog)
