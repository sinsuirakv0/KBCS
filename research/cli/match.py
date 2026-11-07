import argparse
import json
import sqlite3
from contextlib import closing
from pathlib import Path

from indexer.store import LOCAL, configure_output
from matcher.report import build


def query(args):
    with closing(sqlite3.connect(args.db.resolve(strict=True).as_uri() + '?mode=ro', uri=True)) as db:
        db.row_factory = sqlite3.Row
        metadata = {r['key']: json.loads(r['value']) for r in db.execute('SELECT * FROM metadata')}
        if args.command == 'stats':
            return {key: metadata[key] for key in ('identities', 'coverage', 'reasons', 'changes', 'validation', 'quality_gate', 'timing', 'peak_rss_bytes')}
        if args.command == 'gaps':
            return [dict(row) for row in db.execute('''SELECT gaps.*,
                (SELECT count(*) FROM functions WHERE side='old' AND external=0 AND address>old_start AND address<old_end) AS old_count,
                (SELECT count(*) FROM functions WHERE side='new' AND external=0 AND address>new_start AND address<new_end) AS new_count
                FROM gaps WHERE status=? ORDER BY old_start LIMIT ? OFFSET ?''', (args.status, args.limit, args.offset))]
        if args.command == 'find':
            sql, values = 'SELECT * FROM functions WHERE side=?', [args.side]
            if args.status:
                sql += ' AND status=?'
                values.append(args.status)
            if args.text:
                sql += ' AND (instr(lower(name),lower(?))>0 OR instr(lower(address),lower(?))>0)'
                values += [args.text, args.text]
            values += [args.limit, args.offset]
            return [dict(row) for row in db.execute(sql + ' ORDER BY address LIMIT ? OFFSET ?', values)]
        address = args.address.lower().removeprefix('0x')
        if address.startswith('external:'):
            address = 'EXTERNAL:' + address.split(':', 1)[1]
        elif all(c in '0123456789abcdef' for c in address) and address:
            address = address.zfill(8)
        row = db.execute('SELECT * FROM functions WHERE side=? AND address=?', (args.side, address)).fetchone()
        if not row:
            raise ValueError('Address does not exist in this side of the comparison')
        match = db.execute('SELECT * FROM matches WHERE ' + args.side + '=?', (address,)).fetchone()
        matches = [dict(match)] if match else [dict(r) for r in db.execute(
            'SELECT * FROM candidates WHERE ' + args.side + '=? ORDER BY score DESC,old,new LIMIT ?', (address, args.limit))]
        for item in matches:
            item['evidence'] = json.loads(item['evidence'])
            for side in ('old', 'new'):
                counterpart = db.execute('SELECT name,reference FROM functions WHERE side=? AND address=?', (side, item[side])).fetchone()
                item[side + '_name'], item[side + '_reference'] = counterpart
        return {'function': dict(row), 'matches' if match else 'candidates': matches}


def main():
    configure_output()
    parser = argparse.ArgumentParser(description='Cross-version function search with evidence and bounded output')
    commands = parser.add_subparsers(dest='command', required=True)
    create = commands.add_parser('build')
    for side in ('old', 'new'):
        create.add_argument('--' + side + '-cache', type=Path, required=True)
        create.add_argument('--' + side + '-binary', type=Path)
    create.add_argument('--features', type=Path, default=LOCAL / 'matching/features')
    create.add_argument('--output', type=Path)
    create.add_argument('--decisions', type=Path)
    create.add_argument('--validate', action='store_true')
    for command in ('stats', 'find', 'show', 'gaps'):
        child = commands.add_parser(command)
        child.add_argument('--db', type=Path, required=True)
        if command in ('find', 'show'):
            child.add_argument('--side', choices=('old', 'new'), default='old')
        if command != 'stats':
            child.add_argument('--limit', type=int, default=5)
        if command == 'find':
            child.add_argument('text', nargs='?', default='')
            child.add_argument('--status', choices=('accepted', 'review', 'unresolved'))
            child.add_argument('--offset', type=int, default=0)
        elif command == 'show':
            child.add_argument('address')
        elif command == 'gaps':
            child.add_argument('--status', choices=('changed_count', 'crossing', 'equal'), default='changed_count')
            child.add_argument('--offset', type=int, default=0)
    args = parser.parse_args()
    if not 1 <= getattr(args, 'limit', 5) <= 20 or getattr(args, 'offset', 0) < 0:
        parser.error('limit must be 1..20; offset must be nonnegative')
    try:
        if args.command == 'build':
            build(args)
        else:
            print(json.dumps(query(args), ensure_ascii=False, indent=2))
    except (ValueError, OSError, sqlite3.Error) as error:
        parser.exit(1, str(error) + '\n')


if __name__ == '__main__':
    main()
