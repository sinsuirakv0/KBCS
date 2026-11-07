import argparse
import sqlite3
import tempfile
import unittest
from pathlib import Path
from contextlib import closing

from cli.match import query
from matcher.engine import match, order_candidates
from matcher.features import signature
from matcher.report import build, save_database
from matcher.relations import data_pairs, straight_leaf


def function(code, symbols=(), calls=()):
    feature = signature(code.encode())
    return dict(feature, sketch=set(feature['sketch']), name='FUN', symbols=list(symbols), calls=set(calls),
                size=len(code), external=0, confidence='unreviewed', strings=set(), raw='', raw_size=0,
                code_sha256='test', status='cached')


class MatchingTests(unittest.TestCase):
    def test_leaf_requires_return_without_earlier_control_flow(self):
        self.assertTrue(straight_leaf(bytes.fromhex('00008052c0035fd6')))
        for invalid in ('00000094c0035fd6', 'c0035fd6c0035fd6', '00008052', '0000805200000014'):
            self.assertFalse(straight_leaf(bytes.fromhex(invalid)))

    def test_output_inside_source_is_rejected_before_writing(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory)
            destination = source / 'generated'
            args = argparse.Namespace(old_cache=source, new_cache=source, features=destination, output=None)
            with self.assertRaisesRegex(ValueError, 'outside the source caches'):
                build(args)
            self.assertFalse(destination.exists())

    def test_relocations_preserve_literals_operators_and_aliases(self):
        old = b'void FUN_00100000(){thunk_FUN_00200000(s_price_00300000,PTR__ZTV3Cat_00400000);}'
        new = b'void FUN_00500000(){thunk_FUN_00600000(s_price_00700000,PTR__ZTV3Cat_00800000);}'
        self.assertEqual(signature(old)['shape'], signature(new)['shape'])
        for first, second in ((b'f(){return "FUN_00100000";}', b'f(){return "FUN_00200000";}'),
                              (b'f(){return 10;}', b'f(){return 20;}'),
                              (b'f(){return a++ + b;}', b'f(){return a + ++b;}'),
                              (b'f(){FUN_00100000();FUN_00100000();}', b'f(){FUN_00200000();FUN_00300000();}')):
            self.assertNotEqual(signature(first)['shape'], signature(second)['shape'])

    def test_equal_count_without_code_or_calls_remains_candidate(self):
        old = {'00100000': function('f(){return 0;}', ['start']),
               '00100010': function('f(){return 1;}'), '00100020': function('f(){return 1;}'),
               '00100030': function('f(){return 3;}', ['end'])}
        new = {f'{int(a,16)+256:08x}': function('g(){return 1;}' if not r['symbols'] else 'g(){return 3;}', r['symbols'])
               for a, r in old.items()}
        result = match(old, new)
        self.assertEqual(len(result['accepted']), 2)
        self.assertTrue(result['candidates']['00100010'][0]['evidence']['order'])

    def test_local_leaf_uniqueness_does_not_seed_further_matches(self):
        old = {f'{a:08x}': function('f(){return 0;}', [f'anchor_{a}']) for a in (16, 48, 80)}
        for address in ('00000020', '00000040'):
            old[address] = dict(function('f(){return 1;}'), leaf_bytes='same-leaf')
        new = {f'{int(a,16)+256:08x}': dict(row) for a, row in old.items()}
        result = match(old, new)
        self.assertEqual(len(result['accepted']), 5)
        self.assertEqual(result['accepted']['00000020']['reason'], 'leaf_bytes_and_local_order')
        self.assertEqual(result['history'][-1]['anchors'], 3)

    def test_insertion_does_not_zip_unequal_intervals(self):
        old = {f'{a:08x}': function('f(){return 0;}') for a in (16, 32, 48, 64)}
        new = {f'{a:08x}': function('f(){return 0;}') for a in (256, 272, 288, 304, 320)}
        candidates, gaps = order_candidates(old, new, {'00000010': '00000100', '00000040': '00000140'})
        self.assertEqual(gaps[0][-1], 'changed_count')
        self.assertFalse(any(r['order'] for rows in candidates.values() for r in rows.values()))
        _, crossed = order_candidates(old, new, {'00000010': '00000140', '00000040': '00000100'})
        self.assertEqual(crossed[0][-1], 'crossing')

    def test_call_context_promotes_unique_code_and_reject_is_respected(self):
        code = 'f(){' + ''.join(f'x = x + {i};' for i in range(20)) + 'return x;}'
        old = {'00100000': function('f(){return 0;}', ['anchor']),
               '00100010': function(code, calls=[('out', '00100000')])}
        new = {'00200000': function('f(){return 0;}', ['anchor']),
               '00200010': function(code, calls=[('out', '00200000')])}
        old['00100000']['calls'].add(('in', '00100010'))
        new['00200000']['calls'].add(('in', '00200010'))
        result = match(old, new)
        self.assertEqual(result['accepted']['00100010']['new'], '00200010')
        rejected = [{'old': '00100010', 'new': '00200010', 'action': 'reject', 'note': 'reviewed'}]
        self.assertNotIn('00100010', match(old, new, rejected)['accepted'])
        with self.assertRaises(ValueError):
            match(old, new, rejected + [dict(rejected[0], action='accept')])
        for rows, address in ((old, '00100010'), (new, '00200010')):
            row = rows[address]
            feature = signature(b'f(){return FUN_00000100();}')
            row.update(feature, sketch=set(feature['sketch']))
        self.assertEqual(match(old, new)['accepted']['00100010']['reason'], 'code_and_unique_call_neighborhood')

    def test_shared_data_requires_unique_multiple_owner_signature(self):
        old = {f'{a:08x}': function('f(){return 0;}', [f'anchor_{a}']) for a in (16, 48)}
        new = {f'{int(a,16)+256:08x}': function('f(){return 0;}', row['symbols']) for a, row in old.items()}
        for row in old.values():
            row['data_refs'] = {('READ', '0000aaa0')}
        for row in new.values():
            row['data_refs'] = {('READ', '0000bbb0')}
        anchors = {'00000010': '00000110', '00000030': '00000130'}
        self.assertEqual(data_pairs(old, new, anchors)[0], {'0000aaa0': '0000bbb0'})
        self.assertFalse(data_pairs(old, new, {'00000010': '00000110'})[0])
        old['00000020'] = function('f(){return DAT_0000aaa0;}')
        new['00000120'] = function('f(){return DAT_0000bbb0;}')
        old['00000020']['data_refs'] = {('READ', '0000aaa0')}
        new['00000120']['data_refs'] = {('READ', '0000bbb0')}
        self.assertEqual(match(old, new)['accepted']['00000020']['reason'], 'code_order_and_references')
        for row in old.values():
            row['data_refs'].add(('READ', '0000ccc0'))
        self.assertFalse(data_pairs(old, new, anchors)[0])

    def test_database_tracks_every_function_and_reverse_lookup(self):
        old = {'00100000': function('f(){return 1;}', ['known']), '00100004': function('f(){return 7;}')}
        new = {'00200000': function('g(){return 1;}', ['known']), '00200004': function('g(){return 8;}')}
        sources = {side: {'metadata': {'version': version, 'architecture': 'arm64-v8a', 'sha256': 'a'*64}, 'functions': rows}
                   for side, version, rows in (('old', '1.0.0', old), ('new', '1.0.1', new))}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'matches.sqlite'
            metadata = {}
            save_database(path, sources, match(old, new), metadata)
            self.assertEqual(sum(r['count'] for r in metadata['coverage']), 4)
            response = query(argparse.Namespace(command='show', db=path, side='new', address='0x200000', limit=5))
            self.assertEqual(response['matches'][0]['old'], '00100000')
            self.assertTrue(response['matches'][0]['old_reference'].endswith('/00100000.md'))
            with closing(sqlite3.connect(path)) as db:
                self.assertEqual(db.execute('PRAGMA integrity_check').fetchone()[0], 'ok')
                with self.assertRaises(sqlite3.IntegrityError):
                    db.execute("INSERT INTO matches VALUES('other','00200000','test',0,'x','{}')")

    def test_changed_body_needs_multiple_calls_and_layout(self):
        body = 'f(){' + ''.join(f'x = x + {i};' for i in range(40)) + 'return x;}'
        old = {f'{address:08x}': function('f(){return 0;}', [f'anchor_{address}']) for address in (16, 48, 64)}
        new = {f'{int(address,16)+256:08x}': function('f(){return 0;}', row['symbols']) for address, row in old.items()}
        old['00000020'] = function(body, calls=[('out', address) for address in old])
        new['00000120'] = function(body.replace('x + 39', 'x + 49'), calls=[('out', address) for address in new])
        for rows, target in ((old, '00000020'), (new, '00000120')):
            for address, row in rows.items():
                if address != target:
                    row['calls'].add(('in', target))
        result = match(old, new)
        self.assertEqual(result['accepted']['00000020']['reason'], 'similar_code_order_and_calls')
        self.assertFalse(result['accepted']['00000020']['evidence']['shape'])


if __name__ == '__main__':
    unittest.main()
