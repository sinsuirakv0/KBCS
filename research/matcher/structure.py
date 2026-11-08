import gzip
import hashlib
import json
import re
import shutil
import sqlite3
import zlib
from collections import defaultdict
from contextlib import closing
from pathlib import Path

from indexer.run import locked
from indexer.store import digest


EXPORTER = Path(__file__).resolve().parents[1] / 'ghidra/ExportStructure.java'
SCHEMA = 1
ADDRESS = re.compile(r'[0-9a-f]{4,16}')
CONTROL = {'BRANCH', 'CBRANCH', 'CALL'}
MAX_ROW = 96 * 1024**2


def pack(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))


def fingerprint(value):
    return hashlib.sha256(pack(value).encode()).hexdigest()


def reader(path):
    return closing(sqlite3.connect(path.resolve().as_uri() + '?mode=ro', uri=True))


def ordinal_addresses(addresses):
    return {int(address, 16): n for n, address in enumerate(addresses)}


def cfg(row):
    blocks = sorted(row['blocks'], key=lambda block: int(block[0], 16))
    index = ordinal_addresses(block[0] for block in blocks)
    return tuple(tuple(sorted((kind, index.get(int(target, 16), -1) if ADDRESS.fullmatch(target) else -1)
                              for kind, _, target in edges)) for _, _, edges in blocks)


def indexed_refs(row):
    refs = defaultdict(dict)
    for source, target, kind, _, callee, name, datatype in row['refs']:
        if ADDRESS.fullmatch(target):
            refs[source][int(target, 16)] = (kind, callee, name, datatype)
    return refs


def operations(row, targets=None, *, search=False):
    # 指紋探索用の参照省略は、詳細比較や同等判定には使わない。
    blocks = ordinal_addresses(block[0] for block in sorted(row['blocks'], key=lambda block: int(block[0], 16)))
    insns = ordinal_addresses(instruction[0] for instruction in row['instructions'])
    refs = indexed_refs(row)
    targets = targets or {}
    result = []
    for site, mnemonic, flow, instructions in row['instructions']:
        unique = {}
        site_refs = refs.get(site, {})

        def storage(value, is_control=False):
            if value is None:
                return None
            space, offset, width = value.rsplit(':', 2)
            if space == 'unique':
                return f'tmp:{unique.setdefault(offset, len(unique))}:{width}'
            if space in ('ram', 'const'):
                number = int(offset, 16)
                if is_control and space == 'ram' and number in insns:
                    dest = f'b{blocks[number]}' if number in blocks else f'i{insns[number]}'
                    return f'local:{dest}:{width}'
                if number in site_refs:
                    kind, callee, _, _ = site_refs[number]
                    if is_control and callee in targets:
                        return f'callee:{targets[callee]}:{width}'
                    if search:
                        return f'ref:{kind}:{width}'
            return value

        for name, output, inputs in instructions:
            args = tuple(storage(value, i == 0 and name in CONTROL) for i, value in enumerate(inputs))
            result.append((site, (name, storage(output), args)))
    return result


def load_metadata(db, address):
    hit = db.execute('SELECT metadata FROM functions WHERE address=?', (address,)).fetchone()
    return json.loads(hit[0]) if hit else None


def load_row(db, address):
    hit = db.execute('SELECT metadata,instructions FROM functions WHERE address=?', (address,)).fetchone()
    if hit is None:
        return None
    return json.loads(hit[0]) | {'instructions': json.loads(zlib.decompress(hit[1]))}


def structure_header(archive):
    with gzip.open(archive, 'rb') as stream:
        header = json.loads(stream.readline(MAX_ROW))
    if header.get('type') != 'program' or header.get('schema') != SCHEMA:
        raise ValueError('Unsupported Ghidra structure export')
    return header


def build_index(archive, cache, output):
    archive, cache, output = archive.resolve(), cache.resolve(), output.resolve()
    if output.is_relative_to(cache) or output == archive:
        raise ValueError('Structure index must be separate from analysis inputs')
    with reader(cache / 'cache.sqlite') as source:
        expected = dict(source.execute('SELECT address,size FROM functions WHERE external=0'))
    with (cache / 'index.jsonl').open(encoding='utf-8-sig') as stream:
        original = json.loads(stream.readline())
    header = structure_header(archive)
    if (header['sha256'], header['language'], header['image_base']) != (
            original['sha256'], original['language'], original['image_base']):
        raise ValueError('Structure export does not match the indexed program')
    source = {'cache_sha256': digest(cache / 'cache.sqlite'), 'structure_sha256': digest(archive),
              'schema': SCHEMA, 'indexer_sha256': digest(Path(__file__))}
    output.mkdir(parents=True, exist_ok=True)
    target = output / (fingerprint(source)[:24] + '.sqlite')
    with locked(target.with_suffix('.lock')):
        if target.exists():
            with reader(target) as db:
                if db.execute('PRAGMA quick_check').fetchone()[0] == 'ok':
                    return target
        if shutil.disk_usage(output).free < archive.stat().st_size * 6 + 64 * 1024**2:
            raise OSError('Insufficient disk space for the structure index; select an output on another drive')
        temporary = target.with_suffix('.partial')
        temporary.unlink(missing_ok=True)
        temporary.with_name(temporary.name + '-journal').unlink(missing_ok=True)
        with closing(sqlite3.connect(temporary)) as db, gzip.open(archive, 'rb') as stream:
            db.executescript("""
                CREATE TABLE meta(key TEXT PRIMARY KEY,value TEXT NOT NULL);
                CREATE TABLE functions(address TEXT PRIMARY KEY,state TEXT NOT NULL,shape TEXT NOT NULL,
                    operations INTEGER NOT NULL, cfg TEXT NOT NULL, bytes_sha256 TEXT NOT NULL,
                    metadata TEXT NOT NULL,instructions BLOB NOT NULL);
            """)
            stream.readline(MAX_ROW)
            seen, counts, complete = set(), defaultdict(int), None
            while raw := stream.readline(MAX_ROW + 1):
                if len(raw) > MAX_ROW or complete is not None:
                    raise ValueError('Invalid structure record size or footer')
                row = json.loads(raw)
                if row['type'] == 'complete':
                    complete = row
                    continue
                address = row['address']
                if row['type'] != 'function' or not ADDRESS.fullmatch(address) or address in seen:
                    raise ValueError('Invalid or duplicate structure function')
                seen.add(address)
                if address not in expected:
                    counts['extra_in_backfill'] += 1
                    continue
                graph = cfg(row)
                ops = operations(row, search=True)
                if not row['instruction_count'] or not ops:
                    state = 'no_instructions'
                elif row['instruction_bytes'] != row['body_bytes'] or row['body_bytes'] != expected[address]:
                    state = 'boundary_mismatch'
                else:
                    state = 'available'
                counts[state] += 1
                counts['indirect_flows'] += row['indirect']
                counts['unresolved_indirect_flows'] += row['unresolved']
                instructions = row.pop('instructions')
                row['call_positions'] = [(site, flow) for site, _, flow, pcode in instructions
                                         if 'CALL' in flow or any(op[0] in ('CALL', 'CALLIND') for op in pcode)]
                db.execute('INSERT INTO functions VALUES(?,?,?,?,?,?,?,?)',
                           (address, state, fingerprint([graph, [op for _, op in ops]]), len(ops),
                            pack(graph), row['bytes_sha256'], pack(row),
                            zlib.compress(pack(instructions).encode(), 3)))
            if complete is None or complete['functions'] != len(seen):
                raise ValueError('Incomplete structure export')
            counts['missing_in_backfill'] = len(expected.keys() - seen)
            db.executemany('INSERT INTO meta VALUES(?,?)', ((key, pack(value)) for key, value in
                {'source': source, 'program': header, 'coverage': counts, 'export_seconds': complete['seconds']}.items()))
            db.commit()
            if db.execute('PRAGMA quick_check').fetchone()[0] != 'ok':
                raise ValueError('Invalid structure index')
        temporary.replace(target)
    return target
