import collections
import re
import sqlite3
import hashlib
import struct
from contextlib import closing
from pathlib import Path

from indexer.store import digest


def enrich(source):
    path = Path(source['cache']) / 'cache.sqlite'
    functions = source['functions']
    for row in functions.values():
        row.update(data_refs=set(), tail_calls=set())
    with closing(sqlite3.connect(path.as_uri() + '?mode=ro', uri=True)) as db:
        for owner, target, kind, callee in db.execute('SELECT DISTINCT owner,target,kind,callee FROM refs WHERE is_call=0'):
            if owner not in functions:
                continue
            if kind in ('UNCONDITIONAL_JUMP', 'CONDITIONAL_JUMP') and callee in functions and owner != callee:
                functions[owner]['calls'].add(('out', callee))
                functions[callee]['calls'].add(('in', owner))
                functions[owner]['tail_calls'].add(('out', callee))
                functions[callee]['tail_calls'].add(('in', owner))
            elif kind in ('READ', 'WRITE', 'DATA', 'PARAM') and not callee and re.fullmatch('[a-fA-F0-9]{8,16}', target):
                functions[owner]['data_refs'].add((kind, target))
    if digest(path) != source['source_sha256']:
        raise RuntimeError('Source index changed while reading reference relationships')


def straight_leaf(data):
    if not 8 <= len(data) <= 128 or len(data) % 4:
        return False
    words = [value[0] for value in struct.iter_unpack('<I', data)]
    # 最後のRET以外に分岐・例外・システム命令がある場合は保守的に対象外にする。
    return words[-1] & 0xfffffc1f == 0xd65f0000 and not any(word & 0x1c000000 == 0x14000000 for word in words[:-1])


def leaf_bytes(source, binary):
    if not binary:
        return
    data = binary.read_bytes()
    if hashlib.sha256(data).hexdigest() != source['metadata']['sha256']:
        raise ValueError('ELF changed before leaf verification')
    phoff = struct.unpack_from('<Q', data, 32)[0]
    phsize, phnum = struct.unpack_from('<HH', data, 54)
    if data[:6] != b'\x7fELF\x02\x01' or struct.unpack_from('<H', data, 18)[0] != 183 or phsize != 56:
        raise ValueError('Leaf verification requires ELF64 AArch64')
    loads = [struct.unpack_from('<IIQQQQQQ', data, phoff + number * phsize) for number in range(phnum)]
    loads = [row for row in loads if row[0] == 1]
    offset = int(source['metadata']['image_base'], 16) - min(row[3] for row in loads)
    for address, row in source['functions'].items():
        if row['external'] or not 8 <= row['size'] <= 128:
            continue
        value = int(address, 16) - offset
        for _, flags, position, vaddr, _, length, _, _ in loads:
            if flags & 1 and vaddr <= value and value + row['size'] <= vaddr + length:
                start = position + value - vaddr
                content = data[start:start + row['size']]
                # Ghidraの本体サイズが、入口から最初のRETまでの一本道と一致する場合だけ使う。
                if straight_leaf(content):
                    row['leaf_bytes'] = hashlib.sha256(content).hexdigest()
                break


def data_pairs(old, new, anchors):
    used = set(anchors.values())
    def signatures(functions, mapping):
        owners = collections.defaultdict(set)
        for address, row in functions.items():
            if address in mapping:
                for kind, target in row.get('data_refs', ()):
                    owners[target].add((mapping[address], kind))
        result = collections.defaultdict(list)
        for target, references in owners.items():
            # 2関数以上の対応済み参照が必要。同じ参照者集合の複数フィールドは曖昧なので除く。
            if len({address for address, _ in references}) >= 2:
                result[tuple(sorted(references))].append(target)
        return result
    left, right = signatures(old, anchors), signatures(new, {address: address for address in used})
    pairs, evidence = {}, {}
    for signature, targets in left.items():
        if len(targets) == len(right.get(signature, ())) == 1:
            pairs[targets[0]] = right[signature][0]
            evidence[targets[0]] = sorted({address for address, _ in signature})[:3]
    return pairs, evidence


def context_pairs(old, new, anchors):
    used = set(anchors.values())
    def signatures(functions, mapping):
        result = collections.defaultdict(list)
        for address, row in functions.items():
            edges = tuple(sorted((kind, mapping[target]) for kind, target in row['calls'] if target in mapping))
            if row['shape'] and edges and not row['external']:
                result[(row['shape'], edges)].append(address)
        return result
    left, right = signatures(old, anchors), signatures(new, {address: address for address in used})
    return {addresses[0]: right[key][0] for key, addresses in left.items()
            if len(addresses) == len(right.get(key, ())) == 1}
