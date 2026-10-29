# GitHubへ書き込まず、ローカルbareリポジトリで自動採番と再実行を確認する。
import importlib.util
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import tomllib
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("prepare_release", Path(__file__).resolve().parents[1] / "prepare-release.py")
release = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(release)
PUBLISH_SPEC = importlib.util.spec_from_file_location("publish_release", Path(__file__).resolve().parents[1] / "publish-release.py")
publisher = importlib.util.module_from_spec(PUBLISH_SPEC)
PUBLISH_SPEC.loader.exec_module(publisher)


class ReleaseTest(unittest.TestCase):
    def test_version_selection(self):
        tags = ["native-v15.7.2", "kbcs-v0.1.8", "kbcs-v0.1.36"]
        self.assertEqual(release.select_version("0.1.36", tags)[0], "0.1.37")
        self.assertEqual(release.select_version("0.2.0", tags)[0], "0.2.0")
        self.assertEqual(release.select_version("0.1.36", tags, "1.0.0")[0], "1.0.0")
        for invalid in ["0.1.36", "0.1.30", "v0.2.0", "0.02.0", "0.2.0\nother"]:
            with self.subTest(version=invalid), self.assertRaises(ValueError):
                release.select_version("0.1.36", tags, invalid)

    def test_prepare_commit_retry_and_explicit_version(self):
        with tempfile.TemporaryDirectory(prefix="kbcs-release-") as temporary:
            base = Path(temporary)
            remote, root = base / "remote.git", base / "source"
            release.git(base, "init", "--bare", str(remote))
            release.git(base, "init", "--initial-branch=main", str(root))
            release.git(root, "config", "user.name", "Fixture")
            release.git(root, "config", "user.email", "fixture@example.invalid")
            release.git(root, "config", "core.autocrlf", "false")
            (root / "Cargo.toml").write_text('[workspace]\nmembers = ["crates/a", "crates/b"]\n[workspace.package]\nversion = "0.1.36"\n', encoding="utf-8")
            for name in ["a", "b"]:
                folder = root / "crates" / name
                folder.mkdir(parents=True)
                (folder / "Cargo.toml").write_text(f'[package]\nname = "kbcs-{name}"\nversion.workspace = true\n', encoding="utf-8")
            (root / "Cargo.lock").write_text('version = 4\n\n[[package]]\nname = "kbcs-a"\nversion = "0.1.36"\n\n[[package]]\nname = "kbcs-b"\nversion = "0.1.36"\n', encoding="utf-8")
            (root / "README.md").write_text('インストールファイル（v0.1.36）\nkbcs-v0.1.36/KBCS-0.1.36-macos-x64.zip\n', encoding="utf-8-sig")
            release.git(root, "add", ".")
            release.git(root, "commit", "-m", "fixture")
            release.git(root, "tag", "kbcs-v0.1.36")
            (root / "feature.txt").write_text("new source\n", encoding="ascii")
            release.git(root, "add", "feature.txt")
            release.git(root, "commit", "-m", "feature")
            release.git(root, "remote", "add", "origin", str(remote))
            release.git(root, "push", "origin", "main", "--tags")
            source = release.git(root, "rev-parse", "HEAD")
            prepared = release.prepare(root, source=source, publish_branch=True)
            self.assertEqual(prepared["version"], "0.1.37")
            self.assertNotEqual(prepared["commit"], source)
            self.assertEqual(release.git(root, "rev-parse", "HEAD^"), source)
            self.assertEqual(release.git(root, "ls-remote", "origin", "refs/heads/main").split()[0], prepared["commit"])
            lock = tomllib.loads((root / "Cargo.lock").read_text(encoding="utf-8"))
            self.assertEqual({p["version"] for p in lock["package"]}, {"0.1.37"})
            self.assertIn("kbcs-v0.1.37/KBCS-0.1.37", (root / "README.md").read_text(encoding="utf-8-sig"))
            self.assertTrue((root / "docs/releases/0.1.37.md").read_bytes().startswith(b"\xef\xbb\xbf"))

            release.git(root, "checkout", "--detach", source)
            self.assertEqual(release.prepare(root, source=source, publish_branch=True), prepared)
            changed = release.prepare(root, source=prepared["commit"], publish_branch=True, requested="0.2.0")
            self.assertEqual(changed["version"], "0.2.0")
            with self.assertRaisesRegex(ValueError, "main"):
                release.git(root, "checkout", "--detach", source)
                release.prepare(root, source=source, publish_branch=True)

    def test_readonly_and_tag_contract(self):
        with tempfile.TemporaryDirectory(prefix="kbcs-release-readonly-") as temporary:
            root = Path(temporary)
            release.git(root, "init")
            (root / "Cargo.toml").write_text('[workspace.package]\nversion = "0.1.36"\n', encoding="utf-8")
            release.git(root, "add", ".")
            release.git(root, "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-m", "fixture")
            result = release.prepare(root)
            self.assertEqual(result["publish"], "false")
            self.assertEqual(release.prepare(root, tag="kbcs-v0.1.36")["publish"], "true")
            with self.assertRaises(ValueError):
                release.prepare(root, tag="kbcs-v0.1.37")
            self.assertEqual(release.git(root, "status", "--porcelain"), "")

    def test_publish_checks_source_tag_and_remote_hash_before_publication(self):
        with tempfile.TemporaryDirectory(prefix="kbcs-publish-") as temporary:
            root, commit = Path(temporary), "a" * 40
            (root / "Cargo.toml").write_text('[workspace.package]\nversion = "0.1.37"\n', encoding="utf-8")
            (root / "docs/releases").mkdir(parents=True)
            (root / "docs/releases/0.1.37.md").write_text("fixture\n", encoding="utf-8-sig")
            folder = root / ".local/release"
            folder.mkdir(parents=True)
            assets = []
            for platform in ["windows-x64", "macos-arm64", "macos-x64"]:
                name = f"KBCS-0.1.37-{platform}"
                data = platform.encode("ascii")
                digest = hashlib.sha256(data).hexdigest()
                (folder / (name + ".zip")).write_bytes(data)
                (folder / (name + ".json")).write_text(json.dumps({"version": "0.1.37", "commit": commit, "sha256": digest}), encoding="utf-8")
                (folder / (name + ".zip.sha256")).write_text(f"{digest}  {name}.zip\n", encoding="ascii")
                assets.append({"name": name + ".zip", "size": len(data), "digest": "sha256:" + digest})
            environment = {"GITHUB_REF_NAME": "main", "GITHUB_SHA": "b" * 40, "GITHUB_REPOSITORY": "sinsuirakv0/KBCS",
                           "KBCS_RELEASE_TAG": "kbcs-v0.1.37", "KBCS_RELEASE_COMMIT": commit}
            for scenario in ["success", "different-tag", "corrupt-remote"]:
                with self.subTest(scenario=scenario):
                    state = {"tag": scenario == "different-tag", "draft": False, "published": False, "created": False}

                    def gh(*args, check=True):
                        output, code = {}, 0
                        if args[0] == "api":
                            url = args[1]
                            if "/git/ref/tags/" in url:
                                if state["tag"]:
                                    output = {"object": {"type": "commit", "sha": "c" * 40 if scenario == "different-tag" else commit}}
                                else:
                                    code = 1
                            elif url.endswith("/git/refs"):
                                self.assertIn("sha=" + commit, args)
                                state["tag"] = True
                            else:
                                output = {"assets": [{**asset, "digest": "sha256:wrong"} if scenario == "corrupt-remote" else asset for asset in assets]}
                        elif args[1] == "view":
                            if not state["created"]:
                                code = 1
                            else:
                                output = {"isDraft": True, "apiUrl": "https://api.github.com/repos/sinsuirakv0/KBCS/releases/1", "url": "fixture"}
                        elif args[1] == "create":
                            state.update(created=True, draft=True)
                        elif args[1] == "edit":
                            state.update(published=True, draft=False)
                        return subprocess.CompletedProcess(args, code, json.dumps(output), "")

                    with patch.object(publisher, "ROOT", root), patch.object(publisher, "gh", gh), patch.object(publisher.subprocess, "check_output", return_value=commit), patch.dict(publisher.os.environ, environment):
                        if scenario == "success":
                            publisher.main()
                            self.assertTrue(state["published"])
                        else:
                            with self.assertRaises(ValueError):
                                publisher.main()
                            self.assertFalse(state["published"])
                            self.assertEqual(state["draft"], scenario == "corrupt-remote")


if __name__ == "__main__":
    unittest.main()
