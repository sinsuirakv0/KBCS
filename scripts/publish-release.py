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
    result = subprocess.run(["gh", *map(str, args)], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    if check and result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    return result


def main():
    version = tomllib.loads((ROOT / "Cargo.toml").read_text(encoding="utf-8-sig"))["workspace"]["package"]["version"]
    tag = os.environ.get("KBCS_RELEASE_TAG") or os.environ["GITHUB_REF_NAME"]
    commit = os.environ.get("KBCS_RELEASE_COMMIT") or os.environ["GITHUB_SHA"]
    if subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip() != commit:
        raise ValueError("公開対象とcheckoutのコミットが一致しません")
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
        if metadata["version"] != version or metadata["commit"] != commit or metadata["sha256"] != digest or checksum != [digest, archive.name]:
            raise ValueError("成果物の版・commit・SHAが一致しません: " + name)
        hashes[archive.name] = (archive.stat().st_size, "sha256:" + digest)
        files.extend([archive, folder / (name + ".json"), folder / (name + ".zip.sha256")])
    repository = os.environ["GITHUB_REPOSITORY"]
    # GITHUB_TOKENで作ったタグは別のworkflowを起動しない。このrunの三環境を検証して公開する。
    ref_url = f"repos/{repository}/git/ref/tags/{tag}"
    reference = gh("api", ref_url, check=False)
    if reference.returncode:
        gh("api", f"repos/{repository}/git/refs", "--method", "POST", "-f", "ref=refs/tags/" + tag, "-f", "sha=" + commit)
        reference = gh("api", ref_url)
    target = json.loads(reference.stdout)["object"]
    while target["type"] == "tag":
        target = json.loads(gh("api", f"repos/{repository}/git/tags/{target['sha']}").stdout)["object"]
    if target["type"] != "commit" or target["sha"] != commit:
        raise ValueError("既存タグが別のコミットを指しています。タグを変更せず中止します")
    existing = gh("release", "view", tag, "--json", "isDraft", check=False)
    if existing.returncode == 0:
        if not json.loads(existing.stdout)["isDraft"]:
            raise ValueError("公開済みリリースは変更しません")
    else:
        gh("release", "create", tag, "--verify-tag", "--draft", "--prerelease", "--title", "KBCS " + version, "--notes-file", notes)
    gh("release", "upload", tag, *files, "--clobber")
    # ドラフトはタグのREST取得では404になるため、CLIで解決したrelease IDを使う。
    api_url = json.loads(gh("release", "view", tag, "--json", "apiUrl").stdout)["apiUrl"]
    if not api_url.startswith(f"https://api.github.com/repos/{repository}/releases/"):
        raise ValueError("リリースの取得先が一致しません")
    release = json.loads(gh("api", api_url).stdout)
    actual = {asset["name"]: (asset["size"], asset.get("digest")) for asset in release["assets"]}
    if any(actual.get(name) != value for name, value in hashes.items()):
        raise ValueError("GitHubの配布ZIPのサイズ・SHAが一致しません。ドラフトを維持します")
    gh("release", "edit", tag, "--draft=false", "--prerelease", "--notes-file", notes)
    print(gh("release", "view", tag, "--json", "url", "--jq", ".url").stdout.strip())


if __name__ == "__main__":
    main()
