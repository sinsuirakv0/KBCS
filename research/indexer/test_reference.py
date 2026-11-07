import contextlib
import hashlib
import io
import json
import re
import sqlite3
import tempfile
import unittest
from pathlib import Path

from indexer.reference import export_cache, function_path, reference_path, replace_reference
from indexer.store import connect, digest, read_json, write_json
from matcher.comparison_pages import carry_links, code_changes, disconnect, publish_links


class ReferenceTest(unittest.TestCase):
    def test_body_diff_ignores_relocation_and_build_metadata_but_keeps_logic(self):
        old = (b'void FUN_00100000() {\n  local_8 = FUN_00120000(param_1);\n'
               b'  debug("/Users/battlecats/.jenkins/workspace/Battlecats-Jp-Android/release_jp-android-15.7.2/Source/src/test.cpp");\n'
               b'  if (local_8 < 5) return 1;\n}\n')
        new = (old.replace(b'00100000', b'00200000').replace(b'00120000', b'00220000')
               .replace(b'local_8', b'local_10').replace(b'15.7.2', b'15.7.4'))
        old_targets = {b'00120000': b'00220000'}
        new_targets = {b'00220000': b'00220000', b'00220004': b'00220004'}
        self.assertEqual(code_changes(old, new, old_targets, new_targets), '')
        self.assertIn('+  if (local_10 <= 5)', code_changes(old, new.replace(b'< 5', b'<= 5'), old_targets, new_targets))
        self.assertIn('+  local_10 = FUN_00220004', code_changes(old, new.replace(b'00220000', b'00220004'), old_targets, new_targets))
        old_pointer = b'f() {\n  local_a0 = 0xb0;\n  uStack_9f = 0xbe6c;\n  return _DAT_00c24cdc;\n}\n'
        new_pointer = old_pointer.replace(b'0xbe6c', b'0xbe6d').replace(b'00c24cdc', b'00c24ddc')
        self.assertEqual(code_changes(old_pointer, new_pointer, {}, {}, {0xbe6cb0}, {0xbe6db0}), '')
        self.assertIn('+  uStack_9f = 0xbe6d;', code_changes(old_pointer, new_pointer, {}, {}))

    def test_version_links_are_bidirectional_and_survive_reference_replay(self):
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary).resolve()
            reference = workspace / 'reference'
            identities = {side: {'version': version, 'architecture': 'arm64-v8a', 'sha256': sha * 64}
                          for side, version, sha in (('old', '1.2.3', 'a'), ('new', '1.2.4', 'b'))}
            addresses = {'old': '00100000', 'new': '00200000'}
            metadata = {'identities': identities, 'sources': {}, 'quality_gate': 'passed_named_holdout'}
            roots, caches = {}, {}
            page_body = '# Function\n\n## 関数情報\n\nCode\n'
            readme = '# Dataset\n\n## アドレス索引\n'
            for side in ('old', 'new'):
                address = addresses[side]
                cache = caches[side] = workspace / side
                (cache / 'code').mkdir(parents=True)
                (cache / 'code' / (address + '.c')).write_text('f() { return ' + ('1' if side == 'old' else '2') + '; }')
                connect(cache / 'cache.sqlite').close()
                source_sha = metadata['sources'][side] = digest(cache / 'cache.sqlite')
                root = roots[side] = reference / reference_path(identities[side])
                page = root / function_path(address)
                page.parent.mkdir(parents=True)
                page.write_bytes(page_body.encode('utf-8-sig'))
                (root / 'README.md').write_bytes(readme.encode('utf-8-sig'))
                write_json(root / 'manifest.json', identities[side] | {'source_database_sha256': source_sha, 'comparison_state': 'complete'})
            database = workspace / 'matches.sqlite'
            db = sqlite3.connect(database)
            with db:
                db.execute('CREATE TABLE metadata(key,value)')
                db.execute('CREATE TABLE matches(old,new,change)')
                db.execute('CREATE TABLE functions(address,name,side)')
                db.executemany('INSERT INTO metadata VALUES (?,?)', [(key, json.dumps(value)) for key, value in metadata.items()])
                db.execute('INSERT INTO matches VALUES (?,?,?)', (addresses['old'], addresses['new'], 'different'))
                db.execute("INSERT INTO functions VALUES (?, 'example', 'new')", (addresses['new'],))
            db.close()
            for _ in range(2):
                self.assertEqual(publish_links(reference, database, caches['old'], caches['new']), (1, 1))
            for side, peer in (('old', 'new'), ('new', 'old')):
                page = roots[side] / function_path(addresses[side])
                body = page.read_text(encoding='utf-8-sig')
                self.assertEqual(body.count('**別版の対応**'), 1)
                self.assertIn(f"v{identities[peer]['version']} `{addresses[peer]}`", body)
                for path in re.findall(r'\]\(([^)]+\.md)\)', body):
                    self.assertTrue((page.parent / path).is_file(), path)
            replay = workspace / 'replay' / reference_path(identities['new'])
            page = replay / function_path(addresses['new'])
            page.parent.mkdir(parents=True)
            page.write_bytes(page_body.encode('utf-8-sig'))
            (replay / 'README.md').write_bytes(readme.encode('utf-8-sig'))
            carry_links(roots['new'], replay)
            self.assertIn('v1.2.3', page.read_text(encoding='utf-8-sig'))
            self.assertTrue((replay / 'changes/00200000.md').is_file())
            disconnect(reference, roots['old'], 'next', replacing=True)
            self.assertEqual((roots['new'] / function_path(addresses['new'])).read_text(encoding='utf-8-sig'), page_body)
            self.assertEqual(read_json(roots['new'] / 'manifest.json')['comparison_state'], 'pending')

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
