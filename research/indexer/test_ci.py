import hashlib
import io
import json
import os
import tarfile
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from indexer import ci, memory


class CiTests(unittest.TestCase):
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

    def test_checkpoint_roundtrip_and_traversal_rejected(self):
        # 実tarを使い、許可データの復元と境界外パスの拒否を確認する。
        with tempfile.TemporaryDirectory() as directory:
            local = Path(directory)
            staging = local / 'ci-download'
            staging.mkdir()
            name = 'checkpoint-1-1-0.tgz'
            revision = 'a' * 16

            def prepare(unsafe=False):
                entries = {'ci-plan.json': json.dumps({'revision': revision}).encode(),
                           '../outside' if unsafe else 'code/00100000.c': b'void f() {}\n'}
                archive = staging / name
                with tarfile.open(archive, 'w:gz') as target:
                    for path, data in entries.items():
                        member = tarfile.TarInfo(path)
                        member.size = len(data)
                        target.addfile(member, io.BytesIO(data))
                sidecar = staging / (name + '.json')
                sidecar.write_text(json.dumps({'revision': revision, 'sha256': ci.digest(archive),
                    'files': [{'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()} for path, data in entries.items()]}))
                return {'assets': [{'name': path.name, 'state': 'uploaded', 'digest': 'sha256:' + ci.digest(path),
                                    'created_at': '2026-11-06T00:00:00Z'} for path in (archive, sidecar)]}

            release = prepare()
            root = local / 'cache'
            with patch.object(ci, 'LOCAL', local), patch.object(ci, 'api', return_value=release), patch.object(ci.subprocess, 'run'):
                ci.restore(root, 'test', revision)
            self.assertEqual((root / 'code/00100000.c').read_bytes(), b'void f() {}\n')
            release = prepare(True)
            with patch.object(ci, 'LOCAL', local), patch.object(ci, 'api', return_value=release), patch.object(ci.subprocess, 'run'):
                with self.assertRaises(ValueError):
                    ci.restore(local / 'bad-cache', 'test', revision)
            self.assertFalse((local / 'outside').exists())

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
