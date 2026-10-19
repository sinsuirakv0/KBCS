import json
import tempfile
import unittest
from contextlib import closing
from pathlib import Path

from indexer.store import connect, import_index, sync_results


class StoreTests(unittest.TestCase):
    def test_incomplete_import_rolls_back(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            rows = [{'type': 'program', 'sha256': 'abc'},
                    {'type': 'function', 'address': '0010', 'name': 'first', 'size': 8,
                     'external': False, 'thunk': False, 'name_source': 'DEFAULT', 'confidence': 'unreviewed'},
                    {'type': 'complete', 'functions': 1, 'seconds': 0.01}]
            path = root / 'index.jsonl'
            path.write_text('\n'.join(map(json.dumps, rows)), encoding='utf-8-sig')
            import_index(root, {'sha256': 'abc'})
            rows[1]['name'] = 'changed'
            path.write_text('\n'.join(map(json.dumps, rows[:-1])), encoding='utf-8')
            with self.assertRaises(ValueError):
                import_index(root, {'sha256': 'abc'})
            with closing(connect(root / 'cache.sqlite')) as db, db:
                self.assertEqual(db.execute('SELECT name FROM functions').fetchone()[0], 'first')

    def test_resume_journal_and_missing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with closing(connect(root / 'cache.sqlite')) as db, db:
                db.execute("INSERT INTO functions(address,name,size) VALUES('0010','first',8)")
            (root / 'code').mkdir()
            code = root / 'code/0010.c'
            code.write_text('void first() {}', encoding='utf-8')
            result = {'address': '0010', 'status': 'cached', 'error': '', 'file': 'code/0010.c', 'seconds': 0.1}
            (root / 'results.jsonl').write_text(json.dumps(result) + '\n{', encoding='utf-8')
            sync_results(root)
            sync_results(root)
            with closing(connect(root / 'cache.sqlite')) as db, db:
                self.assertEqual(db.execute('SELECT status FROM functions').fetchone()[0], 'cached')
            code.unlink()
            sync_results(root)
            with closing(connect(root / 'cache.sqlite')) as db, db:
                self.assertEqual(db.execute('SELECT status FROM functions').fetchone()[0], 'pending')


if __name__ == '__main__':
    unittest.main()
