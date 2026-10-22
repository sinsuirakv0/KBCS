import contextlib
import hashlib
import io
import json
import re
import tempfile
import unittest
from pathlib import Path

from indexer.reference import PAGE_BYTES, export_cache
from indexer.store import connect, digest


class ReferenceTest(unittest.TestCase):
    def test_complete_export_preserves_unicode_code_and_source(self):
        # 長い日本語の1行・コードフェンス・呼出関係を含む実ファイルで分割を確認する。
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
            parts = {}
            for page in root.rglob('*.md'):
                data = page.read_bytes()
                self.assertTrue(data.startswith(b'\xef\xbb\xbf'))
                self.assertLessEqual(len(data), PAGE_BYTES)
                text = data.decode('utf-8-sig')
                for link in re.findall(r'\]\(([^)]+\.md)\)', text):
                    self.assertTrue((page.parent / link).is_file(), link)
                for match in re.finditer(r'^## 疑似コード (\d+)/\d+ / UTF-8 (\d+) bytes\n\n~+c\n', text, re.MULTILINE):
                    parts[int(match[1])] = text[match.end():].encode('utf-8')[:int(match[2])]
            restored = b''.join(parts[number] for number in sorted(parts))
            self.assertEqual(hashlib.sha256(restored).hexdigest(), hashlib.sha256(code.encode('utf-8')).hexdigest())
            self.assertGreater(len(parts), 1)
            entry = (root / 'functions/00100/00100000.md').read_text(encoding='utf-8-sig')
            self.assertIn('../external/EXTERNAL-00000001.md', entry)
            self.assertIn('関連文字列', entry)
            self.assertEqual(summary['pages'], len(list(root.rglob('*.md'))))


if __name__ == '__main__':
    unittest.main()
