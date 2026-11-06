import contextlib
import hashlib
import io
import json
import re
import tempfile
import unittest
from pathlib import Path

from indexer.reference import export_cache, replace_reference
from indexer.store import connect, digest


class ReferenceTest(unittest.TestCase):
    def test_complete_export_preserves_unicode_code_and_source(self):
        # 長い日本語の1行とコードフェンスを分割せず保存できるか確認する。
        with tempfile.TemporaryDirectory() as temporary:
            cache = Path(temporary) / 'cache'
            (cache / 'code').mkdir(parents=True)
            (cache / 'assembly').mkdir()
            code = 'void example() {\r\n/*' + '日本語~~~' * 14000 + '*/\r\n}\r\n'
            (cache / 'code/00100000.c').write_bytes(b'\xef\xbb\xbf' + code.encode('utf-8'))
            (cache / 'assembly/00100004.asm').write_text('00100004  nop\n', encoding='utf-8')
            db = connect(cache / 'cache.sqlite')
            with db:
                for key, value in {'version': '1.2.3', 'architecture': 'arm64-v8a', 'sha256': 'a' * 64,
                                   'library': 'libexample.so', 'ghidra': '12.1.2'}.items():
                    db.execute('INSERT INTO metadata VALUES(?,?)', (key, json.dumps(value)))
                db.executemany('INSERT INTO functions(address,name,size,external,thunk,confidence,status,error,file) VALUES(?,?,?,?,?,?,?,?,?)', [
                    ('00100000', 'example', 4, 0, 0, 'low', 'cached', '', 'code/00100000.c'),
                    ('00100004', 'failed', 4, 0, 0, 'unreviewed', 'failed', 'memory limit', 'assembly/00100004.asm'),
                    ('EXTERNAL:00000001', 'puts', 0, 1, 0, 'unreviewed', 'external', '', None),
                ])
                db.execute('INSERT INTO refs VALUES(?,?,?,?,?,?,?)', ('00100000', '00100000', 'EXTERNAL:00000001', 'call', 1, 'EXTERNAL:00000001', '関連文字列'))
            db.close()
            before = digest(cache / 'cache.sqlite')
            with contextlib.redirect_stdout(io.StringIO()):
                root, summary = export_cache(cache, Path(temporary) / 'export')
            self.assertEqual(before, digest(cache / 'cache.sqlite'))
            self.assertEqual((summary['cached'], summary['failed'], summary['external'], summary['low_confidence']), (1, 1, 1, 1))
            for page in root.rglob('*.md'):
                data = page.read_bytes()
                self.assertTrue(data.startswith(b'\xef\xbb\xbf'))
                self.assertNotIn('.part-', page.name)
                text = data.decode('utf-8-sig')
                for link in re.findall(r'\]\(([^)]+\.md)\)', text):
                    self.assertTrue((page.parent / link).is_file(), link)
            entry = (root / 'functions/00100/00100000.md').read_bytes().decode('utf-8-sig')
            match = re.search(r'^## 疑似コード / UTF-8 (\d+) bytes\n\n~+c\n', entry, re.MULTILINE)
            restored = entry[match.end():].encode('utf-8')[:int(match[1])]
            self.assertEqual(hashlib.sha256(restored).hexdigest(), hashlib.sha256(code.encode('utf-8')).hexdigest())
            self.assertGreater(summary['max_page_bytes'], 64 * 1024)
            self.assertIn('../external/EXTERNAL-00000001.md', entry)
            self.assertIn('関連文字列', entry)
            self.assertEqual(summary['pages'], len(list(root.rglob('*.md'))))
            db = connect(cache / 'cache.sqlite')
            with db:
                db.execute('INSERT INTO metadata VALUES(?,?)', ('analysis_revision', json.dumps('b' * 16)))
                db.execute('UPDATE metadata SET value=? WHERE key=?', (json.dumps('c' * 64), 'sha256'))
            db.close()
            with contextlib.redirect_stdout(io.StringIO()):
                revised, report = export_cache(cache, Path(temporary) / 'new-export')
            self.assertEqual(revised.name, 'c' * 64)
            self.assertEqual(report['analysis_revision'], 'b' * 16)
            reference = Path(temporary) / 'export'
            sibling = reference / '1.2.3/x86/keep.txt'
            sibling.parent.mkdir()
            sibling.write_text('keep')
            replace_reference(revised, reference)
            self.assertFalse(root.exists())
            self.assertTrue((root.with_name('c' * 64) / 'manifest.json').is_file())
            self.assertEqual(sibling.read_text(), 'keep')


if __name__ == '__main__':
    unittest.main()
