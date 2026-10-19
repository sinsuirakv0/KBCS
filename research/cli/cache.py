import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from indexer.store import LOCAL, configure_output, connect, read_json, sync_results


def main():
    configure_output()
    parser = argparse.ArgumentParser(description='Local Ghidra cache query')
    parser.add_argument('--cache', type=Path)
    parser.add_argument('--limit', type=int, default=10)
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ('find', 'strings'):
        sub.add_parser(name).add_argument('query')
    for name in ('callers', 'callees', 'refs', 'code', 'assembly'):
        child = sub.add_parser(name)
        child.add_argument('address')
        if name in ('code', 'assembly'):
            child.add_argument('--max-chars', type=int, default=4000)
    sub.add_parser('pending')
    sub.add_parser('failures')
    sub.add_parser('external')
    sub.add_parser('stats')
    args = parser.parse_args()
    reference = read_json(LOCAL / 'reference.json') if (LOCAL / 'reference.json').exists() else {}
    if args.cache is None and not reference:
        parser.error('Specify --cache; no completed default reference has been published')
    root = (args.cache or Path(reference['cache'])).resolve()
    if not (root / 'cache.sqlite').is_file():
        parser.error('cache.sqlite not found')
    if reference.get('cache') != str(root):
        sync_results(root)
    tick = time.perf_counter()
    db = connect(root / 'cache.sqlite')
    limit = max(1, min(args.limit, 100))
    address = getattr(args, 'address', '').removeprefix('0x')
    if address and '::' not in address:
        width = db.execute('SELECT length(address) FROM functions WHERE address NOT LIKE ? LIMIT 1', ('%::%',)).fetchone()
        address = address.lower().zfill(width[0] if width else 8)
    params = ()
    if args.command == 'find':
        query = args.query.removeprefix('0x')
        sql = 'SELECT address,name,size,status,confidence FROM functions WHERE name LIKE ? OR address=? OR address=? LIMIT ?'
        width = db.execute('SELECT length(address) FROM functions WHERE address NOT LIKE ? LIMIT 1', ('%::%',)).fetchone()
        params = ('%' + args.query + '%', query, query.lower().zfill(width[0] if width else 8), limit)
    elif args.command == 'strings':
        sql = '''SELECT DISTINCT f.address,f.name,substr(r.string,1,240) AS string
                 FROM refs r JOIN functions f ON f.address=r.owner WHERE r.string LIKE ? LIMIT ?'''
        params = ('%' + args.query + '%', limit)
    elif args.command in ('callers', 'callees', 'refs'):
        if args.command == 'callers':
            sql = '''SELECT DISTINCT f.address,f.name FROM refs r JOIN functions f ON f.address=r.owner
                     WHERE r.is_call=1 AND (r.callee=? OR r.target=?) LIMIT ?'''
            params = (address, address, limit)
        elif args.command == 'callees':
            sql = '''SELECT DISTINCT r.target,r.callee,f.name FROM refs r LEFT JOIN functions f ON f.address=r.callee
                     WHERE r.is_call=1 AND r.owner=? LIMIT ?'''
            params = (address, limit)
        else:
            sql = 'SELECT source,target,kind,substr(string,1,240) AS string FROM refs WHERE owner=? LIMIT ?'
            params = (address, limit)
    elif args.command in ('pending', 'failures', 'external'):
        condition = "external=1" if args.command == 'external' else "status='failed' AND external=0" if args.command == 'failures' else "status!='cached' AND external=0"
        sql = f'SELECT address,name,status,error,file,thunk FROM functions WHERE {condition} LIMIT ?'
        params = (limit,)
    elif args.command in ('code', 'assembly'):
        row = db.execute('SELECT status,error,file FROM functions WHERE address=?', (address,)).fetchone()
        readable = row and row['file'] and (root / row['file']).is_file() and (
            row['status'] == 'cached' if args.command == 'code' else row['file'].endswith('.asm'))
        if readable:
            text = (root / row['file']).read_text(encoding='utf-8-sig')
            bound = max(1, min(args.max_chars, 100000))
            print(text[:bound])
            if len(text) > bound:
                print(f'\n[truncated; total={len(text)} chars; file={root / row["file"]}]')
        else:
            print(json.dumps(dict(row) if row else {'error': 'not found'}))
        db.close()
        return
    else:
        counts = dict(db.execute('SELECT status,count(*) FROM functions GROUP BY status'))
        metadata = {row[0]: json.loads(row[1]) for row in db.execute('SELECT * FROM metadata')}
        metadata = {key: metadata[key] for key in ('version', 'version_code', 'architecture', 'sha256',
                    'library', 'language', 'ghidra', 'function_count', 'index_seconds',
                    'analysis_timed_out', 'analysis_marked_complete', 'string_extraction') if key in metadata}
        average = db.execute("SELECT avg(seconds) FROM functions WHERE status='cached' AND seconds>0").fetchone()[0]
        result = {'counts': counts, 'metadata': metadata,
                  'eligible_internal_functions': db.execute('SELECT count(*) FROM functions WHERE external=0').fetchone()[0],
                  'non_thunk_internal_functions': db.execute('SELECT count(*) FROM functions WHERE external=0 AND thunk=0').fetchone()[0],
                  'mean_successful_decompile_seconds': average,
                  'cache_bytes': sum(p.stat().st_size for p in root.rglob('*') if p.is_file()),
                  'code_bytes': sum(p.stat().st_size for p in (root / 'code').glob('*.c')),
                  'query_ms': (time.perf_counter()-tick)*1000}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        db.close()
        return
    print(json.dumps([dict(row) for row in db.execute(sql, params)], ensure_ascii=False, indent=2))
    db.close()


if __name__ == '__main__':
    main()
