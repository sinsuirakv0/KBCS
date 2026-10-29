#!/usr/bin/env python3
# 三環境の成果物とGitHub側のSHAを検証してから、公開開発版へ切り替える。
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tomllib

ROOT = Path(__file__).resolve().parents[1]


def gh(*args, check=True):
    return subprocess.run(["gh", *map(str, args)], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", check=check)


def main():
    version = tomllib.loads((ROOT / "Cargo.toml").read_text(encoding="utf-8-sig"))["workspace"]["package"]["version"]
    tag = os.environ["GITHUB_REF_NAME"]
    if tag != "kbcs-v" + version:
        raise ValueError("タグとCargo.tomlのバージョンが一致しません")
    notes = ROOT / "docs/releases" / (version + ".md")
    if not notes.is_file():
        raise ValueError("この版のリリース説明がありません")
    folder = ROOT / ".local/release"
    files, hashes = [], {}
    for platform in ("windows-x64", "macos-arm64", "macos-x64"):
        name = f"KBCS-{version}-{platform}"
        archive = folder / (name + ".zip")
        with archive.open("rb") as stream:
            digest = hashlib.file_digest(stream, "sha256").hexdigest()
        metadata = json.loads((folder / (name + ".json")).read_text(encoding="utf-8"))
        checksum = (folder / (name + ".zip.sha256")).read_text(encoding="ascii").split()
        if metadata["version"] != version or metadata["commit"] != os.environ["GITHUB_SHA"] or metadata["sha256"] != digest or checksum != [digest, archive.name]:
            raise ValueError("成果物の版・commit・SHAが一致しません: " + name)
        hashes[archive.name] = (archive.stat().st_size, "sha256:" + digest)
        files.extend([archive, folder / (name + ".json"), folder / (name + ".zip.sha256")])
    existing = gh("release", "view", tag, "--json", "isDraft", check=False)
    if existing.returncode == 0:
        if not json.loads(existing.stdout)["isDraft"]:
            raise ValueError("公開済みリリースは変更しません")
    else:
        gh("release", "create", tag, "--verify-tag", "--draft", "--prerelease", "--title", "KBCS " + version, "--notes-file", notes)
    gh("release", "upload", tag, *files, "--clobber")
    repository = os.environ["GITHUB_REPOSITORY"]
    release = json.loads(gh("api", f"repos/{repository}/releases/tags/{tag}").stdout)
    actual = {asset["name"]: (asset["size"], asset.get("digest")) for asset in release["assets"]}
    if any(actual.get(name) != value for name, value in hashes.items()):
        raise ValueError("GitHubの配布ZIPのサイズ・SHAが一致しません。ドラフトを維持します")
    gh("release", "edit", tag, "--draft=false", "--prerelease")
    print(gh("release", "view", tag, "--json", "url", "--jq", ".url").stdout.strip())


if __name__ == "__main__":
    main()
