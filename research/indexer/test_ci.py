import hashlib
import io
import json
import os
import shutil
import subprocess
import tarfile
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from indexer import ci, memory, network, upstream
from indexer.store import connect


class CiTests(unittest.TestCase):
    def test_assets_proof_requires_the_verified_source_and_splits(self):
        expected = ci.load_input(ci.RESEARCH / 'inputs/jp-1507040.json')
        identity = {key: expected[key] for key in ('packageName', 'versionName', 'versionCode')} | {'split': ''}
        current = {key: expected[key] for key in ('versionName', 'versionCode')} | {
            'status': 'verified', 'sourceRegion': 'jp', 'datasetId': expected['archiveTag'].removeprefix('source-')}
        splits = []
        for entry in (expected['baseApk'], expected['nativeApk']):
            split = entry.get('split', '')
            manifest = identity if not split else identity | {'split': split, 'versionName': ''}
            splits.append({'manifest': manifest, 'name': entry['member'].removeprefix('./'), 'size': entry['bytes'],
                           'sha256': entry['sha256'], 'signatureVerified': True, 'certificateSha256': upstream.SIGNER})
        proof = {'schemaVersion': 1, 'manifest': identity, 'proof': {'source': 'google-play', 'splits': splits},
                 'sourceArchive': {'provider': 'github-release', 'repository': upstream.REPOSITORY,
                                   'tag': expected['archiveTag'], 'size': expected['archiveBytes'],
                                   'sha256': expected['archiveSha256']}}
        self.assertEqual(upstream.source_input(current, proof), {
            key: value for key, value in expected.items() if key not in ('librarySha256', 'provenance')})
        with self.assertRaises(ValueError):
            upstream.source_input(current | {'versionCode': current['versionCode'] + 1}, proof)
        splits[1]['signatureVerified'] = False
        with self.assertRaises(ValueError):
            upstream.source_input(current, proof)

    def test_same_version_with_new_source_is_not_skipped(self):
        source = ci.load_input(ci.RESEARCH / 'inputs/jp-1507040.json')
        reference = {'sha256': source['librarySha256'], 'source_archive_sha256': source['archiveSha256'],
                     'source_version_code': source['versionCode']}
        with patch.object(upstream, 'gh_json', return_value={'object': {'sha': 'a' * 40}}), \
                patch.object(upstream, 'reference_at', return_value=reference):
            self.assertTrue(upstream.published(source, ci.REPO, ci.RESEARCH / 'inputs'))
            self.assertFalse(upstream.published(source | {'archiveSha256': 'a' * 64}, ci.REPO, ci.RESEARCH / 'inputs'))

    def test_budget_identity_and_public_guard(self):
        data = ci.load_input(ci.RESEARCH / 'inputs/jp-1507021.json')
        first = ci.plan(data, 'test', 'JDK21', 16384)
        self.assertEqual(first['native_memory_limit_mb'], 8192)
        self.assertEqual(first, ci.plan(data, 'test', 'JDK21', 16384))
        self.assertNotEqual(first['revision'], ci.plan(data, 'another', 'JDK21', 16384)['revision'])
        with self.assertRaises(RuntimeError):
            ci.plan(data, 'test', 'JDK21', 4096)
        env = {'GITHUB_ACTIONS': 'true', 'RUNNER_ENVIRONMENT': 'github-hosted', 'GITHUB_REPOSITORY': ci.REPO}
        with patch.dict(os.environ, env), patch.object(ci, 'api', return_value={'private': True}):
            with self.assertRaises(RuntimeError):
                ci.public_only()
        for name in ('project/cache.gpr', 'backup-project.zip', 'app.apk', 'libnative-lib.so', '../code/1.c', 'code/../identity.json'):
            self.assertFalse(ci.allowed(name), name)

    def test_restore_falls_back_without_exposing_unverified_files(self):
        # 同じ秒に保存した場合も、数値で新しい方を先に試す。
        with tempfile.TemporaryDirectory() as directory:
            local = Path(directory)
            revision = 'a' * 16

            def prepare(sequence, entries):
                files = {name: b'{}' for name in ci.REQUIRED_STATE} | entries
                files['ci-plan.json'] = json.dumps({'revision': revision}).encode()
                archive = local / f'checkpoint-1-1-{sequence}.tgz'
                with tarfile.open(archive, 'w:gz') as target:
                    for path, data in files.items():
                        member = tarfile.TarInfo(path)
                        member.size = len(data)
                        target.addfile(member, io.BytesIO(data))
                sidecar = archive.with_name(archive.name + '.json')
                ci.write_json(sidecar, {'revision': revision, 'sha256': ci.digest(archive),
                    'files': [{'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()} for path, data in files.items()]})
                return [{'name': path.name, 'state': 'uploaded', 'size': path.stat().st_size,
                         'digest': 'sha256:' + ci.digest(path), 'created_at': '2026-11-06T00:00:00Z'} for path in (archive, sidecar)]

            valid = prepare(9, {'code/00100000.c': b'void f() {}\n'})
            invalid = prepare(10, {'code/00100001.c': b'partial', '../outside': b'bad'})

            def download(_repository, _tag, filename, target):
                shutil.copyfile(local / filename, target / filename)

            root = local / 'cache'
            with patch.object(ci, 'release_state', side_effect=[{'assets': valid + invalid}, {'assets': invalid}]), \
                    patch.object(ci, 'download_asset', side_effect=download) as transfer:
                ci.restore(root, 'test', revision)
                self.assertEqual(transfer.call_args_list[0].args[2], 'checkpoint-1-1-10.tgz.json')
                with self.assertRaisesRegex(RuntimeError, 'No valid checkpoint'):
                    ci.restore(local / 'bad-cache', 'test', revision)
            self.assertEqual((root / 'code/00100000.c').read_bytes(), b'void f() {}\n')
            self.assertFalse((root / 'code/00100001.c').exists())
            self.assertFalse((local / 'bad-cache').exists())
            self.assertFalse((local / 'outside').exists())

    def test_release_retry_and_ambiguous_upload(self):
        temporary = subprocess.CalledProcessError(1, ['gh'], stderr=b'HTTP 503')
        denied = subprocess.CalledProcessError(1, ['gh'], stderr=b'HTTP 403')
        with patch.object(network, 'gh', side_effect=[temporary, b'{}', denied]) as call, \
                patch.object(network.time, 'sleep'):
            self.assertEqual(network.gh_json('test'), {})
            with self.assertRaises(subprocess.CalledProcessError):
                network.gh_json('test')
            self.assertEqual(call.call_count, 3)

        for uploaded_count, transfers in ((2, 1), (1, 2)):
            with self.subTest(uploaded_count=uploaded_count), tempfile.TemporaryDirectory() as directory:
                archive = Path(directory) / 'checkpoint-1-1-0.tgz'
                sidecar = archive.with_name(archive.name + '.json')
                for path in (archive, sidecar):
                    path.write_bytes(b'fixture')
                checksum = ci.digest(archive)
                assets = []

                def upload(_release, _upload, _tag, *args, **_kwargs):
                    paths = list(map(Path, args[:2]))
                    count = uploaded_count if not assets else 2
                    assets.extend({'name': path.name, 'size': path.stat().st_size, 'digest': 'sha256:' + ci.digest(path),
                                   'state': 'uploaded'} for path in paths[:count])
                    if count == uploaded_count and len(assets) == count:
                        raise temporary

                with patch.object(ci, 'gh', side_effect=upload) as send, \
                        patch.object(ci, 'release_state', return_value={'assets': assets}), patch.object(ci.time, 'sleep'):
                    ci.upload_checkpoint('test', archive, sidecar, checksum)
                self.assertEqual(send.call_count, transfers)
                self.assertEqual(len({asset['name'] for asset in assets}), len(assets))
                self.assertEqual(list(Path(directory).iterdir()), [])

    def test_batch_keeps_journal_progress_and_stops_repeated_no_progress(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            db = connect(root / 'cache.sqlite')
            with db:
                db.executemany('INSERT INTO functions(address,name,size,external) VALUES (?, ?, 1, 0)', [('1', 'f'), ('2', 'g')])
            db.close()

            def interrupt(*_args):
                record = {'address': '1', 'status': 'cached', 'error': '', 'file': 'code/1.c',
                          'seconds': 1, 'style': 'decompile'}
                (root / 'code').mkdir()
                (root / record['file']).write_text('void f() {}')
                (root / 'results.jsonl').write_text(json.dumps(record) + '\n{', encoding='utf-8')
                raise TimeoutError()

            with patch.object(ci, 'headless', side_effect=interrupt) as process:
                pending, metrics = ci.decompile_batch({}, root, root / 'binary', 'decompile', ['1', '2'], 1, float('inf'))
            process.assert_called_once()
            self.assertEqual(pending, ['2'])
            self.assertTrue(metrics['interrupted'])
            with patch.object(ci, 'headless', side_effect=TimeoutError) as process:
                with self.assertRaisesRegex(RuntimeError, 'no function progress'):
                    ci.decompile_batch({}, root, root / 'binary', 'decompile', pending, 1, float('inf'))
            self.assertEqual(process.call_count, 2)

    def test_linux_guard_only_stops_owned_native_child(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            proc = root / 'proc'
            proc.mkdir()
            (proc / 'meminfo').write_text('MemAvailable: 8000000 kB\n')
            (proc / '42').mkdir()
            for pid, parent in ((111, 42), (222, 99)):
                (proc / str(pid)).mkdir()
                (proc / str(pid) / 'status').write_text(f'Name:\tdecompile\nPPid:\t{parent}\nVmRSS:\t4096 kB\n')
            with patch.object(memory.os, 'kill') as kill:
                peak, alive = memory.linux_memory(42, root, 1, proc)
            self.assertTrue(alive)
            self.assertEqual(peak, 4096 * 1024)
            kill.assert_called_once_with(111, 9)


if __name__ == '__main__':
    unittest.main()
