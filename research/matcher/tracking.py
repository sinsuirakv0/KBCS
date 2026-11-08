import argparse
import json
import re
import shutil
import sqlite3
import tempfile
import time
from argparse import Namespace
from collections import Counter, defaultdict
from contextlib import closing
from pathlib import Path

from indexer.reference import function_path, reference_path
from indexer.run import headless, locked
from indexer.store import LOCAL, configure_output, digest, read_json, write_json
from matcher import logic, report, structure, tracking_pair


FORMAT = 2
DDL = """
CREATE TABLE metadata(key TEXT PRIMARY KEY,value TEXT NOT NULL);
CREATE TABLE datasets(id INTEGER PRIMARY KEY,version TEXT,abi TEXT,sha256 TEXT,revision TEXT,
    index_sha256 TEXT,structure_sha256 TEXT,reference TEXT,UNIQUE(version,abi,sha256,revision));
CREATE TABLE nodes(dataset INTEGER,address TEXT,name TEXT,external INTEGER,confidence TEXT,
    cache_state TEXT,structure_state TEXT,reference TEXT,PRIMARY KEY(dataset,address),
    FOREIGN KEY(dataset) REFERENCES datasets(id));
CREATE TABLE xrefs(dataset INTEGER,owner TEXT,site TEXT,target TEXT,kind TEXT,source TEXT,callee TEXT,
    symbol TEXT,datatype TEXT,FOREIGN KEY(dataset,owner) REFERENCES nodes(dataset,address));
CREATE INDEX xrefs_owner ON xrefs(dataset,owner,site);
CREATE INDEX xrefs_callee ON xrefs(dataset,callee,site);
CREATE TABLE node_structure(dataset INTEGER,address TEXT,ranges TEXT,cfg TEXT,instruction_count INTEGER,
    operations INTEGER,unresolved_flows INTEGER,bytes_sha256 TEXT,PRIMARY KEY(dataset,address),
    FOREIGN KEY(dataset,address) REFERENCES nodes(dataset,address));
CREATE TABLE pairs(pair TEXT PRIMARY KEY,older INTEGER,newer INTEGER,role TEXT,summary TEXT,
    FOREIGN KEY(older) REFERENCES datasets(id), FOREIGN KEY(newer) REFERENCES datasets(id));
CREATE TABLE relations(pair TEXT,old TEXT,new TEXT,reason TEXT,verdict TEXT,evidence TEXT,
    PRIMARY KEY(pair,old,new,reason), FOREIGN KEY(pair) REFERENCES pairs(pair));
CREATE UNIQUE INDEX accepted_old ON relations(pair,old) WHERE verdict='accepted';
CREATE UNIQUE INDEX accepted_new ON relations(pair,new) WHERE verdict='accepted';
CREATE TABLE candidates(pair TEXT,old TEXT,new TEXT,rank INTEGER,score REAL,eligible TEXT,evidence TEXT,
    PRIMARY KEY(pair,old,new),FOREIGN KEY(pair) REFERENCES pairs(pair));
CREATE INDEX candidates_new ON candidates(pair,new,rank);
CREATE TABLE logic(pair TEXT,old TEXT,new TEXT,status TEXT,evidence TEXT,PRIMARY KEY(pair,old),
    FOREIGN KEY(pair) REFERENCES pairs(pair));
CREATE TABLE review(pair TEXT,side INTEGER,address TEXT,kind TEXT,targets TEXT,evidence TEXT,
    FOREIGN KEY(pair) REFERENCES pairs(pair));
CREATE INDEX review_address ON review(pair,side,address);
CREATE TABLE layout(pair TEXT,old_start TEXT,old_end TEXT,new_start TEXT,new_end TEXT,status TEXT,old_count INTEGER,new_count INTEGER,
    FOREIGN KEY(pair) REFERENCES pairs(pair));
CREATE TABLE cycles(older INTEGER,middle INTEGER,newer INTEGER,old TEXT,middle_address TEXT,via TEXT,direct TEXT,
    state TEXT,temporal TEXT,evidence TEXT,PRIMARY KEY(older,middle,newer,old));
CREATE TABLE conflict_edges(pair TEXT,old TEXT,new TEXT,PRIMARY KEY(pair,old,new));
CREATE TABLE manual_decisions(pair TEXT,old TEXT,new TEXT,action TEXT,note TEXT,
    PRIMARY KEY(pair,old,new,action),FOREIGN KEY(pair) REFERENCES pairs(pair));
"""


def key(i, j):
    return f'{i}-{j}'


def version_key(identity):
    return tuple(map(int, identity['version'].split('.')))


def load_dataset(cache, binary, archive, metrics=None):
    identity = read_json(cache / 'identity.json')
    reference_path(identity)
    if not re.fullmatch('[a-f0-9]{16}', identity['analysis_revision']):
        raise ValueError('A verified analysis revision is required')
    if digest(binary) != identity['sha256'] or structure.structure_header(archive)['sha256'] != identity['sha256']:
        raise ValueError('Analysis binary or structure SHA-256 does not match the cache')
    return {'identity': identity, 'cache': cache, 'binary': binary, 'archive': archive, 'metrics': metrics or {}}


def configuration(datasets, decisions):
    modules = (structure, logic, tracking_pair, report, report.features, report.relations, report.engine)
    code = {Path(module.__file__).name: digest(Path(module.__file__)) for module in modules}
    code[Path(__file__).name] = digest(Path(__file__))
    code['tracking_pages.py'] = digest(Path(__file__).with_name('tracking_pages.py'))
    reviews = {path.name: digest(path) for path in sorted(decisions.glob('*.json'))} if decisions else {}
    sources = [(reference_path(entry['identity']).as_posix(), entry['identity']['analysis_revision'],
                digest(entry['cache'] / 'cache.sqlite'), digest(entry['archive'])) for entry in datasets]
    return structure.fingerprint([sources, code, reviews])[:24], code


def backfill(cache, binary, config, output):
    identity = read_json(cache / 'identity.json')
    sha = digest(binary)
    if sha != identity['sha256'] or output.resolve().is_relative_to(cache.resolve()):
        raise ValueError('Backfill requires the verified SO and a separate output directory')
    source = {'identity': identity, 'index': digest(cache / 'index.jsonl'), 'extractor': digest(structure.EXPORTER)}
    directory = output / structure.fingerprint(source)[:24]
    directory.mkdir(parents=True, exist_ok=True)
    final, receipt = (directory / name for name in ('structure.jsonl.gz', 'structure-metrics.json'))
    work = LOCAL / 'cache'
    work.mkdir(parents=True, exist_ok=True)
    with locked(directory / 'writer.lock'):
        if final.is_file() and receipt.is_file():
            metadata = read_json(receipt)
            if metadata['source'] == source and metadata['sha256'] == digest(final):
                return final
        with tempfile.TemporaryDirectory(prefix='tracking-backfill-', dir=work) as temporary:
            root = Path(temporary)
            settings = config | {'program': identity['library'], 'sha256': sha, 'analysis_timeout_seconds': 0,
                                 'batch_timeout_seconds': max(2400, config.get('batch_timeout_seconds', 0))}
            metrics = headless(settings, root, binary.resolve(), 'structure', 0, initialize=True)
            partial = final.with_suffix('.partial')
            shutil.copyfile(root / final.name, partial)
            if structure.structure_header(partial)['sha256'] != sha:
                raise ValueError('Backfill output has the wrong program SHA-256')
            checksum = digest(partial)
            partial.replace(final)
            write_json(receipt, {'source': source, 'sha256': checksum, 'metrics': metrics})
    return final


def reconcile(db, pair_maps, count):
    totals = Counter()
    for i in range(count - 2):
        ab, bc, ac = (key(i, i + 1), key(i + 1, i + 2), key(i, i + 2))
        first, second, direct = (pair_maps[pair] for pair in (ab, bc, ac))
        inv_first, inv_second, inv_direct = ({b: a for a, b in pairs.items()} for pairs in (first, second, direct))
        statuses = {pair: dict(db.execute('SELECT old,status FROM logic WHERE pair=?', (pair,)))
                    for pair in (ab, bc, ac)}
        for a in sorted(first.keys() | direct.keys()):
            b, c = first.get(a), direct.get(a)
            via = second.get(b)
            alt_b = inv_second.get(c)
            alt_a = inv_direct.get(via)
            mismatch = ((via is not None and c is not None and via != c)
                        or (b is not None and alt_b is not None and b != alt_b)
                        or (alt_a is not None and alt_a != a)
                        or (alt_b in inv_first and inv_first[alt_b] != a))
            if mismatch:
                state = 'conflict'
                involved = {(ab, a, b), (bc, b, via), (ac, a, c),
                            (ac, alt_a, via), (ab, inv_first.get(alt_b), alt_b), (bc, alt_b, c)}
                db.executemany('INSERT OR IGNORE INTO conflict_edges VALUES(?,?,?)',
                               (row for row in involved if row[1] is not None and row[2] is not None))
            elif via is not None and c == via:
                state = 'consistent'
            elif c is not None and b is None and alt_b is None:
                state = 'gap_candidate'
            else:
                state = 'partial'
            logic_status = (statuses[ab].get(a), statuses[bc].get(b), statuses[ac].get(a))
            temporal = ('temporary_change_candidate' if state == 'consistent'
                        and logic_status[:2] == ('logic_change_candidate',) * 2
                        and logic_status[2] in ('no_difference_in_scope', 'machine_only_observed') else '')
            if temporal:
                totals[temporal] += 1
            totals[state] += 1
            db.execute('INSERT INTO cycles VALUES(?,?,?,?,?,?,?,?,?,?)',
                       (i, i + 1, i + 2, a, b, via, c, state, temporal, structure.pack({
                           'logic_status': logic_status, 'other_middle': alt_b, 'other_old': alt_a,
                           'direct_other_old': inv_first.get(alt_b)})))
    return dict(totals)


def add_dataset(db, dataset, number):
    identity, cache, indexed = (dataset[k] for k in ('identity', 'cache', 'index'))
    directory = Path('research/reference') / reference_path(identity)
    provenance = dataset['structure']['source']
    db.execute('INSERT INTO datasets VALUES(?,?,?,?,?,?,?,?)', (
        number, identity['version'], identity['architecture'], identity['sha256'], identity['analysis_revision'],
        provenance['cache_sha256'], provenance['structure_sha256'], directory.as_posix()))
    with structure.reader(cache / 'cache.sqlite') as source, structure.reader(indexed) as extracted:
        states = dict(extracted.execute('SELECT address,state FROM functions'))
        for address, name, external, confidence, status in source.execute(
                'SELECT address,name,external,confidence,status FROM functions ORDER BY address'):
            path = directory / function_path(address)
            db.execute('INSERT INTO nodes VALUES(?,?,?,?,?,?,?,?)', (number, address, name, external, confidence, status,
                states.get(address, 'external' if external else 'missing_in_backfill'), path.as_posix()))
        for address, graph, operations, raw in extracted.execute(
                'SELECT address,cfg,operations,metadata FROM functions ORDER BY address'):
            row = json.loads(raw)
            db.execute('INSERT INTO node_structure VALUES(?,?,?,?,?,?,?,?)', (
                number, address, structure.pack(row['ranges']), graph, row['instruction_count'], operations,
                row['unresolved'], row['bytes_sha256']))
            refs = row['refs']
            recorded = {site for site, _, kind, *_ in refs if 'CALL' in kind}
            db.executemany('INSERT INTO xrefs VALUES(?,?,?,?,?,?,?,?,?)',
                           ((number, address, *item) for item in refs))
            db.executemany('INSERT INTO xrefs VALUES(?,?,?,?,?,?,?,?,?)',
                           ((number, address, site, None, flow, 'PCODE_FLOW', None, None, None)
                            for site, flow in row['call_positions'] if site not in recorded))


def initial_pair(datasets, i, j, output, pair_dbs, decisions):
    left, right = datasets[i], datasets[j]
    pair = key(i, j)
    choice = None
    if decisions:
        versions = [item['identity']['version'] for item in (left, right)]
        path = decisions / ('--'.join(versions) + '.json')
        if path.is_file():
            choice = path
    initial = pair_dbs.get(pair)
    if initial is None:
        initial = report.build(Namespace(old_cache=left['cache'], new_cache=right['cache'],
            old_binary=left['binary'], new_binary=right['binary'], features=output / 'features',
            output=None, decisions=choice, validate=True, reuse=True))
    with structure.reader(initial) as db:
        metadata = {k: json.loads(v) for k, v in db.execute('SELECT key,value FROM metadata')}
    for side, dataset in (('old', left), ('new', right)):
        expected = dataset['identity']
        if reference_path(metadata['identities'][side]) != reference_path(expected) or (
                metadata['sources'][side] != dataset['structure']['source']['cache_sha256']):
            raise ValueError(f'PASS 1 input does not match the tracking window: {pair}')
    if choice and metadata['decisions'] != read_json(choice)['decisions']:
        raise ValueError('PASS 1 input disagrees with manual decisions')
    if metadata.get('quality_gate') != 'passed_named_holdout':
        raise ValueError(f'PASS 1 validation failed for {pair}')
    return initial, metadata


def build(datasets, output, *, decisions=None, pair_dbs=None):
    started = time.monotonic()
    datasets = sorted(datasets, key=lambda entry: version_key(entry['identity']))
    if len(datasets) < 2 or len({entry['identity']['version'] for entry in datasets}) != len(datasets):
        raise ValueError('Tracking requires at least two distinct versions')
    if len({(entry['identity']['architecture'], entry['identity']['library']) for entry in datasets}) != 1:
        raise ValueError('All versions must describe the same ABI and library')
    output = output.resolve()
    if any(output.is_relative_to(entry['cache'].resolve()) for entry in datasets):
        raise ValueError('Tracking results must be separate from analysis inputs')
    for dataset in datasets:
        dataset['index'] = structure.build_index(dataset['archive'], dataset['cache'], output / 'structures')
        with structure.reader(dataset['index']) as db:
            dataset['structure'] = {k: json.loads(v) for k, v in db.execute('SELECT key,value FROM meta')}
    routes = [(i, i + distance) for distance in (1, 2) for i in range(len(datasets) - distance)]
    seeds = {key(i, j): initial_pair(datasets, i, j, output, pair_dbs or {}, decisions) for i, j in routes}
    config_id, code = configuration(datasets, decisions)
    sources = [entry['structure']['source'] | {'identity': entry['identity']} for entry in datasets]
    run = structure.fingerprint([sources, code, {p: digest(value[0]) for p, value in seeds.items()}])[:24]
    root = output / run
    root.mkdir(parents=True, exist_ok=True)
    final = root / 'tracking.sqlite'
    with locked(root / 'writer.lock'):
        if final.exists():
            with structure.reader(final) as db:
                metadata = json.loads(db.execute("SELECT value FROM metadata WHERE key='result'").fetchone()[0])
                if metadata['run'] != run or db.execute('PRAGMA quick_check').fetchone()[0] != 'ok':
                    raise ValueError('Existing tracking database failed integrity validation')
                write_json(root / 'summary.json', metadata)
            return final
        space = sum((entry['cache'] / 'cache.sqlite').stat().st_size for entry in datasets)
        if shutil.disk_usage(root).free < space * 1.5 + 128 * 1024**2:
            raise OSError('Insufficient disk space for the tracking result; select a different output directory')
        temporary = root / 'tracking.partial.sqlite'
        temporary.unlink(missing_ok=True)
        temporary.with_name(temporary.name + '-journal').unlink(missing_ok=True)
        with closing(sqlite3.connect(temporary)) as db:
            db.execute('PRAGMA foreign_keys=ON')
            db.executescript(DDL)
            for i, dataset in enumerate(datasets):
                add_dataset(db, dataset, i)
            pair_maps, summaries = {}, {}
            for i, j in routes:
                pair = key(i, j)
                begin = time.monotonic()
                initial, metadata = seeds[pair]
                db.execute('INSERT INTO pairs VALUES(?,?,?,?,?)', (pair, i, j, 'adjacent' if j == i + 1 else 'validation', '{}'))
                db.executemany('INSERT INTO manual_decisions VALUES(?,?,?,?,?)', (
                    (pair, item['old'], item['new'], item['action'], item['note']) for item in metadata['decisions']))
                force_detail = []
                if j == i + 2:
                    force_detail = [row[0] for row in db.execute("""
                        SELECT first.old FROM logic first JOIN logic second ON first.new=second.old
                        WHERE first.pair=? AND second.pair=? AND first.status='logic_change_candidate'
                        AND second.status='logic_change_candidate'""", (key(i, i+1), key(i+1, j)))]
                pair_maps[pair], summaries[pair] = tracking_pair.audit(
                    initial, datasets[i]['index'], datasets[j]['index'], db, pair,
                    lambda text: print(text, flush=True), force_detail)
                summaries[pair]['seconds'] = time.monotonic() - begin
                summaries[pair]['initial_timing'] = metadata.get('timing')
                db.execute('UPDATE pairs SET summary=? WHERE pair=?', (structure.pack(summaries[pair]), pair))
            cycles = reconcile(db, pair_maps, len(datasets))
            metadata = {'format': FORMAT, 'run': run, 'configuration': config_id, 'complete': True, 'sources': sources, 'engine': code,
                        'pairs': summaries, 'cycles': cycles,
                        'structure': [entry['structure'] | {'process_metrics': entry['metrics']} for entry in datasets],
                        'seconds': time.monotonic() - started, 'peak_rss_bytes': report.peak_memory()}
            db.execute('INSERT INTO metadata VALUES(?,?)', ('result', structure.pack(metadata)))
            db.commit()
            if db.execute('PRAGMA quick_check').fetchone()[0] != 'ok' or db.execute('PRAGMA foreign_key_check').fetchone():
                raise RuntimeError('Tracking database failed integrity validation')
        temporary.replace(final)
        write_json(root / 'summary.json', metadata)
        print(f'PASS 5: {cycles}; complete database {final}', flush=True)
    return final


def trace(paths, version, address, limit):
    neighbors, blocked, gaps = defaultdict(set), defaultdict(set), defaultdict(set)
    entries = {}
    for path in paths:
        with structure.reader(path) as db:
            dataset = {i: (ver, abi, sha, revision) for i, ver, abi, sha, revision in
                       db.execute('SELECT id,version,abi,sha256,revision FROM datasets')}
            for i, a, ref in db.execute('SELECT dataset,address,reference FROM nodes'):
                entries[(*dataset[i], a)] = ref
            for i, j, a, b, state in db.execute("""
                    SELECT p.older,p.newer,r.old,r.new,CASE WHEN c.pair IS NULL THEN 'accepted' ELSE 'conflict' END
                    FROM relations r JOIN pairs p USING(pair)
                    LEFT JOIN conflict_edges c ON c.pair=r.pair AND c.old=r.old AND c.new=r.new
                    WHERE r.verdict='accepted' AND p.role='adjacent'
                    UNION ALL SELECT older,newer,old,direct,'gap_candidate' FROM cycles WHERE state='gap_candidate'"""):
                left, right = (*dataset[i], a), (*dataset[j], b)
                table = {'accepted': neighbors, 'conflict': blocked, 'gap_candidate': gaps}[state]
                table[left].add(right)
                table[right].add(left)
    for node, related in neighbors.items():
        # 保存されたウィンドウ間でも、同じ対象版・原本への競合は保留する。
        groups = defaultdict(set)
        for other in related:
            groups[other[:-1]].add(other)
        for alternatives in groups.values():
            if len(alternatives) > 1:
                for other in alternatives:
                    blocked[node].add(other)
                    blocked[other].add(node)
    queue = sorted(node for node in entries if node[0] == version and node[-1] == address)
    if not queue:
        raise ValueError('No function at the requested version and address')
    found = set()
    while queue and len(found) < limit:
        node = queue.pop(0)
        if node in found:
            continue
        found.add(node)
        queue.extend(sorted(neighbors[node] - blocked[node] - found))
    return {'nodes': [{'identity': node, 'reference': entries[node], 'conflicts': sorted(blocked[node]),
                       'gap_candidates': sorted(gaps[node] - blocked[node]),
                       'relationships': sorted(neighbors[node] - blocked[node])} for node in sorted(found)],
            'truncated': bool(queue)}


def show(path, version, address, limit):
    with structure.reader(path) as db:
        db.row_factory = sqlite3.Row
        item = db.execute("""SELECT d.version,d.abi,d.sha256,d.revision,n.*,s.ranges,
             s.instruction_count,s.operations,s.unresolved_flows FROM datasets d JOIN nodes n ON d.id=n.dataset
             LEFT JOIN node_structure s USING(dataset,address) WHERE d.version=? AND n.address=?""",
            (version, address)).fetchone()
        if item is None:
            raise ValueError('No function at the requested version and address')
        dataset = item['dataset']
        links = [dict(row) for row in db.execute("""
            SELECT pair,old,new,reason,verdict,evidence FROM relations JOIN pairs USING(pair)
            WHERE (older=? AND old=?) OR (newer=? AND new=?) ORDER BY verdict,pair LIMIT ?""",
            (dataset, address, dataset, address, limit))]
        for relation in links:
            relation['evidence'] = json.loads(relation['evidence'])
            difference = db.execute('SELECT evidence FROM logic WHERE pair=? AND old=? AND new=?',
                                     (relation['pair'], relation['old'], relation['new'])).fetchone()
            if difference:
                relation['logic'] = json.loads(difference[0])
                relation['logic']['details'] = relation['logic'].get('details', [])[:3]
        refs = [dict(row) for row in db.execute("""SELECT owner,site,target,kind,source,callee,symbol,datatype
            FROM xrefs WHERE dataset=? AND (owner=? OR callee=?) ORDER BY owner,site LIMIT ?""",
            (dataset, address, address, limit))]
        return {'function': dict(item), 'relations': links, 'references': refs, 'limit': limit}


def main():
    configure_output()
    parser = argparse.ArgumentParser(description='Evidence-based native tracking across versions')
    sub = parser.add_subparsers(dest='command', required=True)
    run = sub.add_parser('build')
    run.add_argument('--dataset', nargs=3, action='append', type=Path, required=True, metavar=('CACHE', 'SO', 'STRUCTURE'))
    run.add_argument('--output', type=Path, default=LOCAL / 'tracking')
    run.add_argument('--decisions', type=Path)
    run.add_argument('--pair-db', nargs=2, action='append', metavar=('PAIR', 'SQLITE'))
    extract = sub.add_parser('backfill')
    extract.add_argument('--cache', type=Path, required=True)
    extract.add_argument('--binary', type=Path, required=True)
    extract.add_argument('--config', type=Path, required=True)
    extract.add_argument('--output', type=Path, default=LOCAL / 'tracking/backfill')
    for command in ('trace', 'show'):
        query = sub.add_parser(command)
        query.add_argument('version')
        query.add_argument('address')
        query.add_argument('--db', type=Path, action='append' if command == 'trace' else 'store', required=True)
        query.add_argument('--limit', type=int, choices=range(1, 51), default=12)
    args = parser.parse_args()
    if args.command == 'build':
        build([load_dataset(*entry) for entry in args.dataset], args.output, decisions=args.decisions,
              pair_dbs={pair: Path(path) for pair, path in args.pair_db or ()})
    elif args.command == 'backfill':
        print(backfill(args.cache, args.binary, read_json(args.config), args.output))
    elif args.command == 'trace':
        print(json.dumps(trace(args.db, args.version, args.address, args.limit), ensure_ascii=False, indent=2))
    else:
        print(json.dumps(show(args.db, args.version, args.address, args.limit), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
