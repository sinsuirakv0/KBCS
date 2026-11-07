import csv
import ctypes
import hashlib
import json
import os
import sqlite3
import time
from contextlib import closing
from pathlib import Path

from indexer.memory import MemoryCounters
from indexer.reference import function_path, reference_path
from indexer.run import locked
from indexer.store import LOCAL, digest, read_json, write_json
from matcher import engine, features, relations


def peak_memory():
    if os.name == 'nt':
        counters = MemoryCounters()
        counters.size = ctypes.sizeof(counters)
        kernel = ctypes.windll.kernel32
        kernel.GetCurrentProcess.restype = ctypes.c_void_p
        query = ctypes.windll.psapi.GetProcessMemoryInfo
        query.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ulong]
        if query(kernel.GetCurrentProcess(), ctypes.byref(counters), counters.size):
            return counters.peak_working
        return None
    import resource
    import sys
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * (1 if sys.platform == 'darwin' else 1024)


def validate(old, new):
    expected = engine.holdout_pairs(old, engine.symbol_pairs(old, new))
    result = engine.match(old, new, withheld=expected,
                          progress=lambda row: print(json.dumps({'holdout': row}), flush=True))
    correct, wrong, missing, examples = 0, 0, 0, []
    for address, target in expected.items():
        item = result['accepted'].get(address)
        if not item:
            missing += 1
        elif item['new'] == target:
            correct += 1
        else:
            wrong += 1
            examples.append({'old': address, 'expected': target, **item})
    return {'hidden_symbols': len(expected), 'correct': correct, 'wrong': wrong, 'abstained': missing,
            'wrong_examples': examples[:20], 'scope': 'Named functions only; not a proof for unnamed functions'}


def reference(identity, address):
    return (Path('research/reference') / reference_path(identity) / function_path(address)).as_posix()


def review_reason(side, address, row, status, result):
    if status == 'accepted':
        return ''
    if row['status'] == 'failed':
        return 'decompilation_failed'
    if row['confidence'] == 'low':
        return 'low_decompilation_confidence'
    if status == 'unresolved':
        return 'no_candidate_with_available_features'
    if side == 'new':
        return 'candidate_for_unmatched_old_function'
    best = result['candidates'][address][0]
    if not best['eligible']:
        return 'insufficient_independent_evidence'
    if not best['evidence']['reciprocal_best'] or best['evidence']['reverse_margin'] < 8:
        return 'competing_old_functions'
    return 'competing_candidates' if best['evidence']['margin'] < 8 else 'round_limit'


def save_database(path, sources, result, metadata):
    with closing(sqlite3.connect(path)) as db:
        db.executescript('''
            CREATE TABLE metadata(key TEXT PRIMARY KEY,value TEXT NOT NULL);
            CREATE TABLE functions(side TEXT,address TEXT,name TEXT,size INTEGER,external INTEGER,
                status TEXT,review_reason TEXT,confidence TEXT,cache_status TEXT,cache_error TEXT,reference TEXT,PRIMARY KEY(side,address));
            CREATE TABLE matches(old TEXT PRIMARY KEY,new TEXT UNIQUE NOT NULL,reason TEXT,round INTEGER,
                change TEXT,evidence TEXT NOT NULL);
            CREATE TABLE candidates(old TEXT,new TEXT,rank INTEGER,score REAL,eligible TEXT,evidence TEXT,
                PRIMARY KEY(old,new));
            CREATE INDEX candidates_new ON candidates(new,score DESC);
            CREATE INDEX functions_status ON functions(side,status,address);
            CREATE TABLE gaps(old_start TEXT,old_end TEXT,new_start TEXT,new_end TEXT,status TEXT);
        ''')
        accepted = result['accepted']
        paired = {'old': set(accepted), 'new': {r['new'] for r in accepted.values()}}
        proposed = {'old': {a for a, rows in result['candidates'].items() if rows},
                    'new': {r['new'] for rows in result['candidates'].values() for r in rows}}
        for side, source in sources.items():
            for address, row in source['functions'].items():
                status = 'accepted' if address in paired[side] else 'review' if address in proposed[side] else 'unresolved'
                db.execute('INSERT INTO functions VALUES(?,?,?,?,?,?,?,?,?,?,?)',
                           (side, address, row['name'], row['size'], row['external'], status,
                            review_reason(side, address, row, status, result), row['confidence'],
                            row['status'], row.get('error'), reference(source['metadata'], address)))
        for a, item in accepted.items():
            first, second = sources['old']['functions'][a], sources['new']['functions'][item['new']]
            change = ('external' if first['external'] else 'unavailable' if not first['shape'] or not second['shape']
                      else 'text_equal' if first['code_sha256'] == second['code_sha256']
                      else 'normalized_equal' if first['shape'] == second['shape'] else 'different')
            db.execute('INSERT INTO matches VALUES(?,?,?,?,?,?)',
                       (a, item['new'], item['reason'], item['round'], change, json.dumps(item['evidence'], sort_keys=True)))
        for a, rows in result['candidates'].items():
            for rank, row in enumerate(rows, 1):
                db.execute('INSERT INTO candidates VALUES(?,?,?,?,?,?)',
                           (a, row['new'], rank, row['score'], row['eligible'], json.dumps(row['evidence'], sort_keys=True)))
        db.executemany('INSERT INTO gaps VALUES(?,?,?,?,?)', result['gaps'])
        metadata['coverage'] = [dict(zip(('side', 'external', 'status', 'count'), row)) for row in db.execute(
            'SELECT side,external,status,count(*) FROM functions GROUP BY side,external,status ORDER BY 1,2,3')]
        metadata['reasons'] = dict(db.execute('SELECT reason,count(*) FROM matches GROUP BY reason'))
        metadata['changes'] = dict(db.execute('SELECT change,count(*) FROM matches GROUP BY change'))
        db.executemany('INSERT INTO metadata VALUES(?,?)', [(k, json.dumps(v, ensure_ascii=False, sort_keys=True)) for k, v in metadata.items()])
        db.commit()
        if db.execute('PRAGMA quick_check').fetchone()[0] != 'ok':
            raise RuntimeError('Matching database failed integrity check')


def export_tables(db_path, output):
    with closing(sqlite3.connect(db_path.as_uri() + '?mode=ro', uri=True)) as db:
        for name in ('matches', 'candidates', 'functions', 'gaps'):
            with (output / (name + '.tsv')).open('w', encoding='utf-8-sig', newline='') as stream:
                rows = db.execute('SELECT * FROM ' + name + ' ORDER BY 1,2')
                writer = csv.writer(stream, delimiter='\t')
                writer.writerow(column[0] for column in rows.description)
                writer.writerows(rows)


def build(args):
    started = time.monotonic()
    source_paths = [getattr(args, side + '_cache').resolve(strict=True) for side in ('old', 'new')]
    destinations = [args.features.resolve(), (args.output or LOCAL / 'matching').resolve()]
    if any(destination.is_relative_to(source) for destination in destinations for source in source_paths):
        raise ValueError('Generated files must be outside the source caches')
    sources = {side: features.load(getattr(args, side + '_cache'), getattr(args, side + '_binary'), args.features)
               for side in ('old', 'new')}
    for side, source in sources.items():
        relations.enrich(source)
        relations.leaf_bytes(source, getattr(args, side + '_binary'))
    if sources['old']['metadata']['architecture'] != sources['new']['metadata']['architecture']:
        raise ValueError('Match the same architecture; cross-architecture matching is not implemented')
    identities = {side: {key: source['metadata'][key] for key in ('version', 'architecture', 'sha256')}
                  for side, source in sources.items()}
    source_hashes = {side: source['source_sha256'] for side, source in sources.items()}
    decisions = read_json(args.decisions) if args.decisions else {'sources': source_hashes, 'decisions': []}
    if decisions['sources'] != source_hashes:
        raise ValueError('Review decisions belong to different source indexes')
    code_hashes = {path.name: digest(path) for path in (Path(features.__file__), Path(engine.__file__), Path(relations.__file__), Path(__file__))}
    fingerprints = {side: hashlib.sha256(''.join(a + r['code_sha256'] for a, r in source['functions'].items()).encode()).hexdigest()
                    for side, source in sources.items()}
    run_key = hashlib.sha256(json.dumps([identities, source_hashes, fingerprints, code_hashes, decisions,
                                        bool(args.old_binary), bool(args.new_binary), args.validate], sort_keys=True).encode()).hexdigest()[:24]
    output = (args.output or LOCAL / 'matching' / run_key).resolve()
    if any(output.is_relative_to(source) for source in source_paths):
        raise ValueError('Output would modify a source cache')
    output.mkdir(parents=True, exist_ok=True)
    target = output / 'matches.sqlite'
    with locked(output / 'build.lock'):
        if target.exists():
            with closing(sqlite3.connect(target.as_uri() + '?mode=ro', uri=True)) as db:
                previous = db.execute("SELECT value FROM metadata WHERE key='run_key'").fetchone()
            if not previous or json.loads(previous[0]) != run_key:
                raise ValueError('Output contains a different run; choose another directory')
        old, new = (sources[side]['functions'] for side in ('old', 'new'))
        print(json.dumps({'matching': 'started', 'old': len(old), 'new': len(new)}), flush=True)
        match_started = time.monotonic()
        result = engine.match(old, new, decisions['decisions'],
                              progress=lambda row: print(json.dumps({'matching': row}), flush=True))
        match_seconds = time.monotonic() - match_started
        print(json.dumps({'accepted': len(result['accepted']), 'matching_seconds': match_seconds, 'validation': args.validate}), flush=True)
        validation_started = time.monotonic()
        validation = validate(old, new) if args.validate else None
        metadata = {'format': 1, 'run_key': run_key, 'identities': identities, 'sources': source_hashes,
                    'code_hashes': code_hashes, 'fingerprints': fingerprints, 'validation': validation,
                    'history': result['history'], 'decisions': decisions['decisions'],
                    'quality_gate': ('passed_named_holdout' if validation['correct'] and not validation['wrong'] else 'failed') if validation else 'not_run',
                    'timing': {'matching_seconds': match_seconds, 'validation_seconds': time.monotonic() - validation_started,
                               'features': {side: {'seconds': src['feature_seconds'], 'reused': src['reused']} for side, src in sources.items()},
                               'total_before_export_seconds': time.monotonic() - started}, 'peak_rss_bytes': peak_memory()}
        temporary = output / 'matches.partial.sqlite'
        # 中断時の未完成DBだけを再作成し、公開済みのDBは完成後に置き換える。
        temporary.unlink(missing_ok=True)
        temporary.with_name(temporary.name + '-journal').unlink(missing_ok=True)
        save_database(temporary, sources, result, metadata)
        temporary.replace(target)
        export_tables(target, output)
        write_json(output / 'review-template.json', {'sources': source_hashes, 'decisions': []})
        write_json(output / 'summary.json', metadata)
        lines = ['# 関数対応の実測', '', '| 対象 | 外部関数 | 状態 | 件数 |', '|---|---:|---|---:|']
        lines += [f"| {r['side']} | {r['external']} | {r['status']} | {r['count']} |" for r in metadata['coverage']]
        lines += ['', '採用した対応は推定です。スコアは確率ではありません。未確定を追加・削除と断定しません。',
                  'normalized_equalはアドレス表記等の正規化後に同一という意味で、動作の同一性を証明しません。',
                  '', '## 検証・再現情報', '', '```json', json.dumps(metadata, ensure_ascii=False, indent=2), '```', '']
        (output / 'report.md').write_text('\n'.join(lines), encoding='utf-8-sig')
    print(json.dumps({'database': str(target), 'coverage': metadata['coverage'], 'validation': validation}, ensure_ascii=False))
    if metadata['quality_gate'] == 'failed':
        raise ValueError('Named holdout validation failed; diagnostic results were saved, review before using matches')
    return target
