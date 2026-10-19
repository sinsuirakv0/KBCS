import hashlib
import json
import sqlite3
import sys
from pathlib import Path

LOCAL = Path(__file__).resolve().parents[1] / '.local'


def configure_output():
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8')


def digest(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.partial')
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8-sig')
    temp.replace(path)


def connect(path):
    db = sqlite3.connect(path, timeout=10)
    db.row_factory = sqlite3.Row
    db.executescript('''
        PRAGMA foreign_keys=ON;
        CREATE TABLE IF NOT EXISTS metadata(key TEXT PRIMARY KEY,value TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS functions(
            address TEXT PRIMARY KEY,name TEXT NOT NULL,size INTEGER NOT NULL,
            external INTEGER,thunk INTEGER,name_source TEXT,confidence TEXT,
            status TEXT NOT NULL DEFAULT 'pending',error TEXT,file TEXT,seconds REAL);
        CREATE INDEX IF NOT EXISTS function_name ON functions(name COLLATE NOCASE);
        CREATE TABLE IF NOT EXISTS refs(
            owner TEXT NOT NULL,source TEXT NOT NULL,target TEXT NOT NULL,kind TEXT NOT NULL,
            is_call INTEGER NOT NULL,callee TEXT,string TEXT,
            UNIQUE(owner,source,target,kind));
        CREATE INDEX IF NOT EXISTS ref_owner ON refs(owner);
        CREATE INDEX IF NOT EXISTS ref_callee ON refs(callee,is_call);
        CREATE INDEX IF NOT EXISTS ref_target ON refs(target);
    ''')
    return db


def import_index(root, identity):
    # 完了印のあるファイルのみトランザクションで取り込み、再取込でも疑似コード状態を保持する。
    root = Path(root)
    db = connect(root / 'cache.sqlite')
    complete = False
    count = 0
    try:
        with db, (root / 'index.jsonl').open(encoding='utf-8-sig') as stream:
            db.execute('DELETE FROM refs')
            for line in stream:
                record = json.loads(line)
                kind = record.pop('type')
                if kind == 'program':
                    if record['sha256'].lower() != identity['sha256'].lower():
                        raise ValueError('Ghidra executable hash mismatch')
                    for key, value in (record | identity).items():
                        db.execute('INSERT OR REPLACE INTO metadata VALUES(?,?)', (key, json.dumps(value)))
                elif kind == 'function':
                    db.execute('''INSERT INTO functions(address,name,size,external,thunk,name_source,confidence)
                        VALUES(:address,:name,:size,:external,:thunk,:name_source,:confidence)
                        ON CONFLICT(address) DO UPDATE SET name=excluded.name,size=excluded.size,
                        external=excluded.external,thunk=excluded.thunk,name_source=excluded.name_source''', record)
                    count += 1
                elif kind == 'reference':
                    db.execute('INSERT OR IGNORE INTO refs VALUES(?,?,?,?,?,?,?)',
                               (record['function'], record['source'], record['target'], record['kind'],
                                record['call'], record.get('callee'), record.get('string')))
                elif kind == 'complete':
                    complete = record['functions'] == count
                    db.execute('INSERT OR REPLACE INTO metadata VALUES(?,?)', ('index_seconds', json.dumps(record['seconds'])))
            if not complete:
                raise ValueError('Incomplete index')
        return count
    finally:
        db.close()


def sync_results(root):
    root = Path(root)
    db = connect(root / 'cache.sqlite')
    journal = root / 'results.jsonl'
    try:
        with db:
            if journal.exists():
                with journal.open(encoding='utf-8') as stream:
                    for line in stream:
                        try:
                            record = json.loads(line)
                        except json.JSONDecodeError:
                            continue
                        if record['status'] == 'cached' and not (root / record['file']).is_file():
                            continue
                        db.execute('UPDATE functions SET status=:status,error=:error,file=:file,seconds=:seconds WHERE address=:address', record)
            # 手動削除や中断により消えたファイルは再取得可能に戻す。
            for row in db.execute("SELECT address,file FROM functions WHERE status='cached'"):
                if not row['file'] or not (root / row['file']).is_file():
                    db.execute("UPDATE functions SET status='pending',file=NULL WHERE address=?", (row['address'],))
    finally:
        db.close()
