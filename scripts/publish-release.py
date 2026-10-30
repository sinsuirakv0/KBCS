#!/usr/bin/env python3
# 成功した環境だけを公開し、公開済みの配布物は変更しない。
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tomllib

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {
    "windows-x64": "x86_64-pc-windows-gnullvm",
    "macos-arm64": "aarch64-apple-darwin",
    "macos-x64": "x86_64-apple-darwin",
}


def gh(*args, check=True):
    result = subprocess.run(["gh", *map(str, args)], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    if check and result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    return result


def package_files(folder, version, commit, platform):
    if platform not in TARGETS:
        raise ValueError("公開対象の環境が不正です: " + platform)
    name = f"KBCS-{version}-{platform}"
    archive = folder / (name + ".zip")
    with archive.open("rb") as stream:
        digest = hashlib.file_digest(stream, "sha256").hexdigest()
    metadata = json.loads((folder / (name + ".json")).read_text(encoding="utf-8"))
    checksum = (folder / (name + ".zip.sha256")).read_text(encoding="ascii").split()
    expected = {"version": version, "commit": commit, "sha256": digest,
                "target": TARGETS[platform], "archive": archive.name}
    if any(metadata.get(key) != value for key, value in expected.items()) or checksum != [digest, archive.name]:
        raise ValueError("成果物の版・commit・CPU・SHAが一致しません: " + name)
    # 更新確認はZIPの存在を使う。公開済みリリースへの追加でも、付属情報を先に完成させる。
    files = [folder / (name + ".json"), folder / (name + ".zip.sha256"), archive]
    hashes = {}
    for path in files:
        with path.open("rb") as stream:
            hashes[path.name] = (path.stat().st_size, "sha256:" + hashlib.file_digest(stream, "sha256").hexdigest())
    return files, hashes


def asset_hashes(release):
    return {asset["name"]: (asset["size"], asset.get("digest")) for asset in release["assets"]}


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
    files, hashes = package_files(folder, version, commit, os.environ["KBCS_RELEASE_PLATFORM"])
    repository = os.environ["GITHUB_REPOSITORY"]
    # 同じrunの全環境を同じソースへ固定する。既存タグは移動させない。
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
    existing = gh("release", "view", tag, "--json", "isDraft,apiUrl", check=False)
    if existing.returncode:
        gh("release", "create", tag, "--verify-tag", "--draft", "--prerelease", "--title", "KBCS " + version, "--notes-file", notes)
        existing = gh("release", "view", tag, "--json", "isDraft,apiUrl")
    # ドラフトはタグのREST取得では404になるため、CLIで解決したrelease IDを使う。
    info = json.loads(existing.stdout)
    draft, api_url = info["isDraft"], info["apiUrl"]
    if not api_url.startswith(f"https://api.github.com/repos/{repository}/releases/"):
        raise ValueError("リリースの取得先が一致しません")
    release = json.loads(gh("api", api_url).stdout)
    # 中断されたアップロードの空ZIPは配布物ではない。同じ環境の再実行で回復させる。
    if any(a["name"] == files[-1].name and a.get("state") == "starter" for a in release["assets"]):
        gh("release", "delete-asset", tag, files[-1].name, "--yes")
        release = json.loads(gh("api", api_url).stdout)
    actual = asset_hashes(release)
    complete = files[-1].name in actual
    if not draft and complete and any(name in actual and actual[name] != value for name, value in hashes.items()):
        raise ValueError("公開済みの成果物は上書きしません。サイズ・SHAが一致しません")
    new_archive = files[-1] if files[-1].name not in actual else None
    try:
        for path in files:
            if actual.get(path.name) != hashes[path.name]:
                if path == files[-1]:
                    ready = asset_hashes(json.loads(gh("api", api_url).stdout))
                    if any(ready.get(p.name) != hashes[p.name] for p in files[:-1]):
                        raise ValueError("GitHubの付属情報のサイズ・SHAが一致しません")
                replace = draft or (not complete and path != files[-1] and path.name in actual)
                gh("release", "upload", tag, path, *(["--clobber"] if replace else []))
        actual = asset_hashes(json.loads(gh("api", api_url).stdout))
        if any(actual.get(name) != value for name, value in hashes.items()):
            raise ValueError("GitHubの成果物のサイズ・SHAが一致しません")
    except Exception:
        # 他環境の公開済みZIPを保ったまま、今回の未検証ZIPだけを更新候補から外す。
        if not draft and new_archive is not None:
            gh("release", "delete-asset", tag, new_archive.name, "--yes", check=False)
        raise
    if draft:
        gh("release", "edit", tag, "--draft=false", "--prerelease", "--notes-file", notes)
    print(gh("release", "view", tag, "--json", "url", "--jq", ".url").stdout.strip())


if __name__ == "__main__":
    main()
