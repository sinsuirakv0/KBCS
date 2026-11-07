import bisect
import difflib
import html
import json
import os
import re
import sqlite3
from contextlib import closing
from itertools import chain
from pathlib import Path

from indexer.reference import GIT_FILE_LIMIT, fenced, function_path, reference_path
from indexer.store import digest, read_json, write_json
from matcher.features import ADDRESS, TOKEN, VARIABLE


DIRECTIONS = {'previous': 'next', 'next': 'previous'}
COMPARISON_LINK = '[直前の公開版との関数対応](comparison.md)'
BUILD_PATH = re.compile(rb'^(")(/Users/battlecats/\.jenkins/workspace/Battlecats-Jp-Android/release_jp-android-)\d+\.\d+\.\d+(/Source/[^\"]+\.(?:cpp|h)")$')
HEX_NUMBER = re.compile(rb'0x[0-9a-fA-F]+')
PACKED_POINTER = re.compile(rb'(?m)^[ \t]*(?:local|uStack)_([0-9a-f]+) = (0x[0-9a-f]+);[ \t]*\r?\n'
                            rb'[ \t]*uStack_([0-9a-f]+) = (0x[0-9a-f]+);')


def packed_pointers(content, data_targets):
    result = {}
    for match in PACKED_POINTER.finditer(content):
        first, low, second, high = (int(value, 16) for value in match.groups())
        pointer = low | (high << 8)
        # 連続するスタック位置と実際のデータ参照が揃う場合だけ、分割アドレスとみなす。
        if first - second == 1 and low <= 255 and pointer in data_targets:
            result[match.start(2)] = (pointer, b'-low')
            result[match.start(4)] = (pointer, b'-high')
    return result


def body_lines(content, targets, data_targets):
    raw_lines = [line.removesuffix('\r') for line in content.decode('utf-8-sig').split('\n')]
    ends = [match.start() for match in re.finditer(b'\n', content)]
    keys = [[] for _ in raw_lines]
    labels, variables, pointers = {}, {}, {}
    packed = packed_pointers(content, data_targets)
    body = False
    for match in TOKEN.finditer(content):
        if match['comment']:
            continue
        value = match[0]
        if not body:
            body = value == b'{'
            continue
        if match['literal']:
            value = BUILD_PATH.sub(rb'\1\2<VERSION>\3', value)
        else:
            stripped = value.lstrip(b'_')
            address = ADDRESS.fullmatch(stripped)
            if address:
                kind, number = address.groups()
                target = targets.get(number.lower()) if kind in (b'FUN', b'thunk_FUN', b'SUB') else None
                kind = value[:len(value) - len(stripped)] + kind
                value = (kind + b'@function:' + target if target else
                         kind + b'@label:' + str(labels.setdefault(value, len(labels))).encode())
            elif VARIABLE.fullmatch(value) and not value.startswith(b'param_'):
                value = b'variable@' + str(variables.setdefault(value, len(variables))).encode()
            elif HEX_NUMBER.fullmatch(value):
                pointer, part = packed.get(match.start(), (int(value, 16), b''))
                if pointer in data_targets:
                    value = b'pointer@' + str(pointers.setdefault(pointer, len(pointers))).encode() + part
        keys[bisect.bisect_right(ends, match.start())].append(value)
    return raw_lines, [tuple(line) for line in keys]


def code_changes(old, new, old_targets, new_targets, old_data=(), new_data=()):
    old_lines, old_keys = body_lines(old, old_targets, old_data)
    new_lines, new_keys = body_lines(new, new_targets, new_data)
    if list(chain.from_iterable(old_keys)) == list(chain.from_iterable(new_keys)):
        return ''
    blocks = []
    for group in difflib.SequenceMatcher(None, old_keys, new_keys).get_grouped_opcodes(2):
        _, old_start, _, new_start, _ = group[0]
        _, _, old_end, _, new_end = group[-1]
        if list(chain.from_iterable(old_keys[old_start:old_end])) == list(chain.from_iterable(new_keys[new_start:new_end])):
            continue
        lines = [f'@@ -{old_start + 1},{old_end - old_start} +{new_start + 1},{new_end - new_start} @@']
        for operation, i, j, k, l in group:
            if operation == 'equal' or list(chain.from_iterable(old_keys[i:j])) == list(chain.from_iterable(new_keys[k:l])):
                lines.extend(' ' + line for line in old_lines[i:j])
            else:
                lines.extend('-' + line for line in old_lines[i:j])
                lines.extend('+' + line for line in new_lines[k:l])
        blocks.extend(lines)
    return '\n'.join(blocks)


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


def known_calls(cache, targets):
    calls = {}
    with closing(sqlite3.connect((cache / 'cache.sqlite').resolve().as_uri() + '?mode=ro', uri=True)) as db:
        for owner, callee in db.execute("""SELECT owner,callee FROM refs WHERE callee IS NOT NULL
            AND (is_call=1 OR kind IN ('UNCONDITIONAL_JUMP','CONDITIONAL_JUMP')) ORDER BY owner,source,callee"""):
            if callee in targets:
                calls.setdefault(owner, []).append(targets[callee])
    return calls


def referenced_data(cache, owners):
    result = {}
    with closing(sqlite3.connect((cache / 'cache.sqlite').resolve().as_uri() + '?mode=ro', uri=True)) as db:
        for owner, target in db.execute("SELECT owner,target FROM refs WHERE kind IN ('DATA','READ','WRITE','PARAM')"):
            if owner in owners and target and re.fullmatch('[0-9a-fA-F]{6,16}', target):
                result.setdefault(owner, set()).add(int(target, 16))
    return result


def publish_links(reference, database, old_cache, new_cache):
    with closing(sqlite3.connect(database.resolve().as_uri() + '?mode=ro', uri=True)) as db:
        metadata = {key: json.loads(value) for key, value in db.execute('SELECT key,value FROM metadata')}
        pairs = db.execute('SELECT old,new,change FROM matches ORDER BY old').fetchall()
        names = dict(db.execute("SELECT address,name FROM functions WHERE side='new'"))
    if metadata['quality_gate'] != 'passed_named_holdout':
        raise ValueError('A validated match database is required')
    old_id, new_id = (metadata['identities'][side] for side in ('old', 'new'))
    old, new = (reference / reference_path(identity) for identity in (old_id, new_id))
    for side, dataset, cache, identity in (('old', old, old_cache, old_id), ('new', new, new_cache, new_id)):
        manifest = read_json(dataset / 'manifest.json')
        if (reference_path(manifest) != reference_path(identity)
                or manifest['source_database_sha256'] != metadata['sources'][side]
                or digest(cache / 'cache.sqlite') != metadata['sources'][side]):
            raise ValueError(f'{side} reference does not belong to this comparison')
    old_targets = {a: b for a, b, _ in pairs}
    new_targets = {b: b for _, b, _ in pairs}
    old_calls, new_calls = known_calls(old_cache, old_targets), known_calls(new_cache, new_targets)
    old_functions = {a.encode(): b.encode() for a, b in old_targets.items() if not a.startswith('EXTERNAL:')}
    new_functions = {b.encode(): b.encode() for b in new_targets if not b.startswith('EXTERNAL:')}
    candidates = [(a, b) for a, b, change in pairs if change not in ('external', 'unavailable')
                  and (change == 'different' or old_calls.get(a) != new_calls.get(b))]
    old_data = referenced_data(old_cache, {a for a, _ in candidates})
    new_data = referenced_data(new_cache, {b for _, b in candidates})
    changed_pages = {}
    for a, b in candidates:
        first = (old_cache / 'code' / function_path(a).with_suffix('.c').name).read_bytes()
        second = (new_cache / 'code' / function_path(b).with_suffix('.c').name).read_bytes()
        diff = code_changes(first, second, old_functions, new_functions, old_data.get(a, ()), new_data.get(b, ()))
        if diff:
            changed_pages[b] = (a, diff)
    changes = new / 'changes'
    if changes.resolve() != changes.absolute():
        raise ValueError(f'Unsafe change directory: {changes}')
    for source, direction, peer in ((old, 'next', new_id), (new, 'previous', old_id)):
        path = catalog_path(source, direction)
        if path.is_file() and reference_path(read_json(path)['peer']) != reference_path(peer):
            disconnect(reference, source, direction)
    changes.mkdir(exist_ok=True)
    old_catalog_path = catalog_path(new, 'previous')
    if old_catalog_path.is_file():
        remove_change_pages(new, read_json(old_catalog_path))
    index = [f"# 処理の変更候補 v{old_id['version']} → v{new_id['version']}", '',
             f'疑似コード本体に差分が残った対応は {len(changed_pages):,} 組です。',
             'アドレスの移動、空白、コメント、復元時の変数名、既知のビルドパスの版表記を正規化しました。数値がアドレスを表す場合は、解析索引のデータ参照で裏付けられたものだけを正規化しました。動作の確認には差分と両版の関数資料を参照してください。',
             '', '| 旧版 | 新版 | 新版の関数名 | 変更箇所 |', '| --- | --- | --- | --- |']
    for b, (a, diff) in sorted(changed_pages.items()):
        page = Path(*new.parts[-3:]) / 'changes' / function_path(b).name
        a_link = relative_link(Path(*old.parts[-3:]) / function_path(a), page)
        b_link = relative_link(Path(*new.parts[-3:]) / function_path(b), page)
        name = html.escape(names[b][:180]).replace('|', '&#124;').replace('\n', ' ').replace('\r', ' ')
        index.append(f'| [`{a}`]({a_link}) | [`{b}`]({b_link}) | {name} | [本文差分]({page.name}) |')
        content = (f'# `{a}` → `{b}` の本文差分\n\n[旧版の関数資料]({a_link}) · [新版の関数資料]({b_link}) · [変更一覧](README.md)\n\n'
                   '行番号は各疑似コード原本に対応します。`-` は旧版、`+` は新版の抜粋です。\n\n' + fenced(diff, 'diff'))
        (changes / page.name).write_text(content, encoding='utf-8-sig', newline='\n')
    (changes / 'README.md').write_text('\n'.join(index) + '\n', encoding='utf-8-sig', newline='\n')
    for source, direction, peer, rows in (
            (old, 'next', new_id, [[a, b, b in changed_pages] for a, b, _ in pairs]),
            (new, 'previous', old_id, [[b, a, b in changed_pages] for a, b, _ in pairs])):
        path = catalog_path(source, direction)
        prior = read_json(path) if path.is_file() else None
        catalog = {'peer': peer, 'rows': rows}
        render_links(source, direction, catalog, prior)
        write_json(path, catalog)
    return len(pairs), len(changed_pages)
