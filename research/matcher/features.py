import collections
import hashlib
import json
import re
import sqlite3
import struct
import time
from contextlib import closing
from pathlib import Path

from indexer.run import locked
from indexer.store import digest

TOKEN = re.compile(
    rb'(?P<literal>"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\')|(?P<comment>/\*.*?\*/|//[^\n]*)|'
    rb'[A-Za-z_][A-Za-z0-9_]*|[0-9]+[A-Za-z0-9_.]*|>>=|<<=|\+\+|--|->|&&|\|\||<<|>>|[+*/%=!<>&|^-]=|\.\.\.|\S',
    re.DOTALL)
ADDRESS = re.compile(rb'((?:thunk_)?(?:FUN|DAT|LAB|UNK|SUB|EXT|switchD|caseD)|(?:PTR|s)_[A-Za-z0-9_]*|PTR)_([a-fA-F0-9]{6,16})$')
VARIABLE = re.compile(rb'(?:[a-z]+Var\d+|local_[a-fA-F0-9]+|param_\d+|[a-z]+Stack_[a-fA-F0-9]+)$')


def signature(text):
    tokens, relaxed, addresses, variables = [], [], {}, {}
    body = False
    for match in TOKEN.finditer(text):
        token = match[0]
        if match['comment']:
            continue
        if not body:
            body = token == b'{'
            continue
        relocation = ADDRESS.fullmatch(token) if not match['literal'] else None
        if relocation:
            prefix = relocation[1]
            token = prefix + b'@' + str(addresses.setdefault(token, len(addresses))).encode()
        tokens.append(token)
        if not match['literal'] and VARIABLE.fullmatch(token):
            token = b'variable@' + str(variables.setdefault(token, len(variables))).encode()
        relaxed.append(token)
    def hashed(values):
        return hashlib.sha256(b' '.join(values)).hexdigest() if values else ''
    # 表記差を許す候補探索に使う。数値・文字列・演算子は保持する。
    grams = sorted({hashlib.blake2b(b' '.join(relaxed[i:i + 4]), digest_size=8).hexdigest()
                    for i in range(max(0, len(relaxed) - 3))})[:128]
    return {'shape': hashed(tokens), 'relaxed': hashed(relaxed), 'tokens': len(tokens), 'sketch': grams,
            'diversity': len(set(tokens))}


def read_elf(path, image_base):
    data = path.read_bytes()
    if data[:6] != b'\x7fELF\x02\x01' or struct.unpack_from('<H', data, 18)[0] != 183:
        raise ValueError('Expected a little-endian AArch64 ELF')
    def unpack(fmt, offset):
        return struct.unpack_from(fmt, data, offset)
    phoff, shoff = unpack('<QQ', 32)
    phsize, phnum, shsize, shnum = unpack('<HHHH', 54)
    if phsize != 56 or shsize != 64 or not shnum:
        raise ValueError('Unsupported ELF table layout')
    segments = [unpack('<IIQQQQQQ', phoff + i * phsize) for i in range(phnum)]
    loads = [(r[2], r[3], r[5]) for r in segments if r[0] == 1]
    offset = image_base - min(vaddr for _, vaddr, _ in loads)
    sections = [unpack('<IIQQQQIIQQ', shoff + i * shsize) for i in range(shnum)]
    result = collections.defaultdict(list)
    for section in sections:
        if section[1] != 11:
            continue
        strings = sections[section[6]]
        names = data[strings[4]:strings[4] + strings[5]]
        if section[9] != 24 or section[5] % 24:
            raise ValueError('Invalid dynamic symbol table')
        for position in range(section[4], section[4] + section[5], 24):
            name, info, _, index, value, size = unpack('<IBBHQQ', position)
            if not index or info & 15 not in (2, 10) or not value:
                continue
            end = names.find(b'\0', name)
            if end < 0:
                raise ValueError('Invalid ELF symbol name')
            raw = ''
            for file_offset, vaddr, length in loads:
                if size and vaddr <= value and value + size <= vaddr + length:
                    start = file_offset + value - vaddr
                    raw = hashlib.sha256(data[start:start + size]).hexdigest()
                    break
            result[f'{value + offset:08x}'].append((names[name:end].decode('utf-8'), raw, size))
    return result


def load(cache, binary, feature_root):
    cache = cache.resolve(strict=True)
    source_hash = digest(cache / 'cache.sqlite')
    feature_root.mkdir(parents=True, exist_ok=True)
    key = hashlib.sha256((source_hash + digest(Path(__file__))).encode()).hexdigest()[:24]
    output = feature_root / (key + '.sqlite')
    started = time.monotonic()
    with closing(sqlite3.connect((cache / 'cache.sqlite').as_uri() + '?mode=ro', uri=True)) as db:
        db.row_factory = sqlite3.Row
        metadata = {r['key']: json.loads(r['value']) for r in db.execute('SELECT * FROM metadata')}
        functions = {r['address']: dict(r) for r in db.execute('SELECT * FROM functions ORDER BY address')}
        if any(r['status'] not in ('cached', 'failed', 'external') for r in functions.values()):
            raise ValueError('Use a completed decompilation cache')
        for row in functions.values():
            row.update(calls=set(), strings=set(), symbols=[], raw='', raw_size=0)
        for owner, callee in db.execute('SELECT DISTINCT owner,callee FROM refs WHERE is_call=1 AND callee IS NOT NULL'):
            if owner in functions and callee in functions and owner != callee:
                functions[owner]['calls'].add(('out', callee))
                functions[callee]['calls'].add(('in', owner))
        for owner, string in db.execute('SELECT DISTINCT owner,string FROM refs WHERE string IS NOT NULL'):
            if owner in functions and 6 <= len(string) <= 160:
                functions[owner]['strings'].add(string)
    if binary:
        if digest(binary) != metadata['sha256']:
            raise ValueError('ELF SHA-256 differs from the source cache')
        symbols = read_elf(binary, int(metadata['image_base'], 16))
        for address, entries in symbols.items():
            if address in functions:
                functions[address]['symbols'] = sorted(name for name, _, _ in entries)
                functions[address]['raw'], functions[address]['raw_size'] = entries[0][1:]
    for row in functions.values():
        if row['external']:
            row['symbols'] = [row['name']]
    reused = 0
    with locked(output.with_suffix('.lock')), closing(sqlite3.connect(output)) as db:
        db.execute('CREATE TABLE IF NOT EXISTS features(address TEXT PRIMARY KEY, stamp TEXT, data TEXT)')
        try:
            for number, (address, row) in enumerate(functions.items(), 1):
                path = (cache / row['file']).resolve() if row['status'] == 'cached' else None
                if path and not path.is_relative_to(cache):
                    raise ValueError('Pseudocode path escapes cache')
                stat = path.stat() if path else None
                stamp = str((stat.st_size, stat.st_mtime_ns)) if stat else ''
                saved = db.execute('SELECT stamp,data FROM features WHERE address=?', (address,)).fetchone()
                if saved and saved[0] == stamp:
                    feature = json.loads(saved[1])
                    reused += 1
                else:
                    content = path.read_bytes().removeprefix(b'\xef\xbb\xbf') if path else b''
                    feature = signature(content)
                    feature['code_sha256'] = hashlib.sha256(content).hexdigest()
                    if path and (path.stat().st_size, path.stat().st_mtime_ns) != (stat.st_size, stat.st_mtime_ns):
                        raise RuntimeError('Pseudocode changed during extraction')
                    db.execute('INSERT OR REPLACE INTO features VALUES(?,?,?)', (address, stamp, json.dumps(feature)))
                row.update(feature)
                row['sketch'] = set(row['sketch'])
                if number % 256 == 0:
                    db.commit()
                if number % 4000 == 0:
                    print(json.dumps({'features': metadata['version'], 'processed': number, 'total': len(functions)}), flush=True)
            db.commit()
        except BaseException:
            db.rollback()
            raise
    if digest(cache / 'cache.sqlite') != source_hash:
        raise RuntimeError('Source index changed during feature extraction')
    return {'metadata': metadata, 'functions': functions, 'source_sha256': source_hash,
            'cache': str(cache), 'feature_seconds': time.monotonic() - started, 'reused': reused}
