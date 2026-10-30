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


class PublisherTest(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="kbcs-publish-")
        self.addCleanup(temporary.cleanup)
        self.root, self.commit = Path(temporary.name), "a" * 40
        (self.root / "Cargo.toml").write_text('[workspace.package]\nversion = "0.1.38"\n', encoding="utf-8")
        notes = self.root / "docs/releases/0.1.38.md"
        notes.parent.mkdir(parents=True)
        notes.write_text("fixture\n", encoding="utf-8-sig")
        self.folder = self.root / ".local/release"
        self.folder.mkdir(parents=True)
        for platform, target in publisher.TARGETS.items():
            name = f"KBCS-0.1.38-{platform}"
            data = platform.encode("ascii")
            digest = hashlib.sha256(data).hexdigest()
            (self.folder / (name + ".zip")).write_bytes(data)
            (self.folder / (name + ".json")).write_text(json.dumps({
                "version": "0.1.38", "commit": self.commit, "sha256": digest,
                "target": target, "archive": name + ".zip"}), encoding="utf-8")
            (self.folder / (name + ".zip.sha256")).write_text(f"{digest}  {name}.zip\n", encoding="ascii")
        self.environment = {"GITHUB_REPOSITORY": "sinsuirakv0/KBCS", "KBCS_RELEASE_TAG": "kbcs-v0.1.38",
                            "KBCS_RELEASE_COMMIT": self.commit, "KBCS_RELEASE_PLATFORM": "windows-x64"}
        self.tag_commit, self.created, self.draft = None, False, True
        self.assets, self.uploads, self.deleted = {}, [], []
        self.corrupt = ""

    def gh(self, *args, check=True):
        output, code = {}, 0
        if args[0] == "api":
            url = args[1]
            if "/git/ref/tags/" in url:
                code = 0 if self.tag_commit else 1
                output = {"object": {"type": "commit", "sha": self.tag_commit}}
            elif url.endswith("/git/refs"):
                self.assertIn("sha=" + self.commit, args)
                self.tag_commit = self.commit
            else:
                output = {"assets": list(self.assets.values())}
        elif args[1] == "view":
            code = 0 if self.created else 1
            output = {"isDraft": self.draft, "apiUrl": "https://api.github.com/repos/sinsuirakv0/KBCS/releases/1", "url": "fixture"}
        elif args[1] == "create":
            self.created = True
        elif args[1] == "upload":
            path = Path(args[3])
            if not self.draft:
                if "--clobber" in args:
                    self.assertFalse(path.name.endswith(".zip"))
                    archive = path.name.removesuffix(".json").removesuffix(".zip.sha256") + ".zip"
                    self.assertNotIn(archive, self.assets)
                else:
                    self.assertNotIn(path.name, self.assets)
            self.uploads.append(path.name)
            self.assets[path.name] = {"name": path.name, "size": path.stat().st_size,
                                      "digest": "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()}
            if path.name.endswith(self.corrupt) and self.corrupt:
                self.assets[path.name]["digest"] = "sha256:wrong"
        elif args[1] == "delete-asset":
            self.deleted.append(args[3])
            self.assets.pop(args[3], None)
        elif args[1] == "edit":
            self.draft = False
        else:
            self.fail("Unexpected GitHub call: " + str(args))
        return subprocess.CompletedProcess(args, code, json.dumps(output), "")

    def publish(self, platform="windows-x64"):
        environment = {**self.environment, "KBCS_RELEASE_PLATFORM": platform}
        with patch.object(publisher, "ROOT", self.root), patch.object(publisher, "gh", self.gh), \
                patch.object(publisher.subprocess, "check_output", return_value=self.commit), \
                patch.dict(publisher.os.environ, environment), patch("builtins.print"):
            publisher.main()

    def test_platforms_publish_independently_and_retry_without_overwriting(self):
        for index, platform in enumerate(publisher.TARGETS, 1):
            self.publish(platform)
            self.assertFalse(self.draft)
            self.assertEqual(len(self.assets), index * 3)
            self.assertEqual(self.uploads[-3:], [f"KBCS-0.1.38-{platform}{suffix}"
                                               for suffix in [".json", ".zip.sha256", ".zip"]])
            count = len(self.uploads)
            self.publish(platform)
            self.assertEqual(len(self.uploads), count)

    def test_wrong_source_and_cpu_are_rejected_before_upload(self):
        self.tag_commit = "b" * 40
        with self.assertRaisesRegex(ValueError, "コミット"):
            self.publish()
        self.assertFalse(self.created)
        self.tag_commit = None
        path = self.folder / "KBCS-0.1.38-windows-x64.json"
        metadata = json.loads(path.read_text(encoding="utf-8"))
        metadata["target"] = "aarch64-apple-darwin"
        path.write_text(json.dumps(metadata), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "CPU"):
            self.publish()
        self.assertEqual(self.uploads, [])

    def test_incomplete_package_is_rejected_before_release_creation(self):
        (self.folder / "KBCS-0.1.38-windows-x64.zip.sha256").unlink()
        with self.assertRaises(FileNotFoundError):
            self.publish()
        self.assertFalse(self.created)

    def test_public_assets_are_immutable(self):
        self.publish()
        self.assets[self.uploads[-1]]["digest"] = "sha256:wrong"
        with self.assertRaisesRegex(ValueError, "上書き"):
            self.publish()
        self.assertEqual(len(self.uploads), 3)
        self.assertEqual(self.deleted, [])

    def test_bad_sidecar_keeps_first_release_private_and_retry_repairs_draft(self):
        self.corrupt = ".json"
        with self.assertRaisesRegex(ValueError, "付属情報"):
            self.publish()
        self.assertTrue(self.draft)
        self.assertFalse(any(name.endswith(".zip") for name in self.assets))
        self.corrupt = ""
        self.publish()
        self.assertFalse(self.draft)
        self.assertEqual(len(self.assets), 3)

    def test_failed_mac_addition_removes_only_its_unverified_zip(self):
        self.publish()
        windows = dict(self.assets)
        self.corrupt = ".zip"
        with self.assertRaisesRegex(ValueError, "SHA"):
            self.publish("macos-arm64")
        self.assertFalse(self.draft)
        self.assertEqual(self.deleted, ["KBCS-0.1.38-macos-arm64.zip"])
        for name, asset in windows.items():
            self.assertEqual(self.assets[name], asset)
        self.corrupt = ""
        self.publish("macos-arm64")
        self.assertEqual(len(self.assets), 6)

    def test_incomplete_public_sidecars_and_interrupted_upload_can_be_retried(self):
        self.publish()
        self.corrupt = ".json"
        with self.assertRaisesRegex(ValueError, "付属情報"):
            self.publish("macos-arm64")
        name = "KBCS-0.1.38-macos-arm64.zip"
        self.assets[name] = {"name": name, "state": "starter", "size": 0, "digest": None}
        self.corrupt = ""
        self.publish("macos-arm64")
        self.assertEqual(len(self.assets), 6)
        self.assertEqual(self.assets[name]["size"], len(b"macos-arm64"))


if __name__ == "__main__":
    unittest.main()
