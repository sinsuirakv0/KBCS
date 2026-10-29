#!/usr/bin/env python3
# mainの配布版を確定し、三環境が同じ版・同じコミットをビルドする。
import json
import os
from pathlib import Path
import re
import subprocess
import tomllib

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "sinsuirakv0/KBCS"
VERSION = r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)"


def git(root, *args, check=True):
    result = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, encoding="utf-8")
    if check and result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    return result.stdout.strip()


def version_key(value):
    if not re.fullmatch(VERSION, value):
        raise ValueError("バージョンはX.Y.Z形式で指定してください: " + value)
    return tuple(map(int, value.split(".")))


def current_version(root):
    return tomllib.loads((root / "Cargo.toml").read_text(encoding="utf-8-sig"))["workspace"]["package"]["version"]


def select_version(current, tags, requested=""):
    current_key = version_key(current)
    versions = [tag.removeprefix("kbcs-v") for tag in tags if re.fullmatch("kbcs-v" + VERSION, tag)]
    latest = max(versions, key=version_key, default="0.0.0")
    latest_key = version_key(latest)
    if requested:
        if version_key(requested) < current_key or version_key(requested) <= latest_key:
            raise ValueError("指定版は現在の版以上、既存タグより新しい版にしてください")
        return requested, ("kbcs-v" + latest if versions else "")
    if current_key < latest_key:
        raise ValueError("Cargo.tomlが既存の配布版より古いため、自動採番を中止します")
    if current_key == latest_key:
        return f"{current_key[0]}.{current_key[1]}.{current_key[2] + 1}", "kbcs-v" + latest
    # Cargo.tomlで明示的に上げた版、または前回ビルド未完了の版を尊重する。
    return current, ("kbcs-v" + latest if versions else "")


def update_files(root, version, previous):
    manifest_path = root / "Cargo.toml"
    manifest = manifest_path.read_text(encoding="utf-8-sig")
    updated, count = re.subn(r'(?m)(^\[workspace\.package\]\s*\nversion\s*=\s*")[^"]+("\s*$)',
                             lambda m: m[1] + version + m[2], manifest, count=1)
    if count != 1:
        raise ValueError("workspace.package.versionを特定できません")
    manifest_path.write_text(updated, encoding="utf-8")
    members = tomllib.loads(updated)["workspace"]["members"]
    names = {tomllib.loads((root / member / "Cargo.toml").read_text(encoding="utf-8-sig"))["package"]["name"] for member in members}
    lock_path = root / "Cargo.lock"
    blocks = lock_path.read_text(encoding="utf-8").split("[[package]]")
    found = set()
    for index, block in enumerate(blocks[1:], 1):
        package = tomllib.loads("[[package]]" + block)["package"][0]
        if package["name"] in names:
            blocks[index], count = re.subn(r'(?m)^version = "[^"]+"$', f'version = "{version}"', block, count=1)
            if count != 1 or package["name"] in found:
                raise ValueError("workspaceのlockエントリーが重複または不正です")
            found.add(package["name"])
    if found != names:
        raise ValueError("workspaceのlockエントリーが不足しています")
    lock_path.write_text("[[package]]".join(blocks), encoding="utf-8")
    readme_path = root / "README.md"
    readme = readme_path.read_text(encoding="utf-8-sig")
    readme = re.sub(r"(?<=kbcs-v)" + VERSION, version, readme)
    readme = re.sub(r"(?<=KBCS-)" + VERSION, version, readme)
    readme = re.sub(r"(?<=インストールファイル（v)" + VERSION, version, readme)
    readme_path.write_text(readme, encoding="utf-8-sig")
    notes = root / "docs/releases" / (version + ".md")
    if not notes.exists():
        tag = "kbcs-v" + version
        base = f"https://github.com/{REPOSITORY}"
        lines = [f"# KBCS {version}", "", "Windows・Apple Silicon Mac・Intel Mac用の自動ビルドです。", ""]
        for label, platform in [("Windows", "windows-x64"), ("Mac・Mシリーズ", "macos-arm64"), ("Mac・Intel", "macos-x64")]:
            filename = f"KBCS-{version}-{platform}.zip"
            lines.append(f"- **{label}**: [{filename}]({base}/releases/download/{tag}/{filename})")
        lines += ["", f"[インストール手順]({base}/blob/{tag}/README.md)", "",
                  "三環境のテスト・ビルド・単独起動検査を通過してから公開しています。ZIPのSHA-256とビルド情報JSONを添付し、全ソースはSource codeから取得できます。"]
        if previous:
            lines += ["", f"[前回からの変更]({base}/compare/{previous}...{tag})"]
        notes.parent.mkdir(parents=True, exist_ok=True)
        notes.write_text("\n".join(lines) + "\n", encoding="utf-8-sig")


def prepare(root, requested="", source="", publish_branch=False, tag="", reuse_tag=True):
    source = source or git(root, "rev-parse", "HEAD")
    if git(root, "rev-parse", "HEAD") != source:
        raise ValueError("開始コミットがworkflowの対象と一致しません")
    current = current_version(root)
    if tag:
        if tag != "kbcs-v" + current:
            raise ValueError("タグとCargo.tomlのバージョンが一致しません")
        return {"commit": source, "version": current, "tag": tag, "publish": "true"}
    if not publish_branch:
        return {"commit": source, "version": current, "tag": "", "publish": "false"}
    if git(root, "status", "--porcelain"):
        raise ValueError("変更済みの作業ツリーでは配布版を準備できません")
    git(root, "fetch", "origin", "refs/heads/main:refs/remotes/origin/main", "--tags")
    tip = git(root, "rev-parse", "refs/remotes/origin/main")
    marker = "KBCS-Release-Source: " + source
    if tip != source:
        # 同じrunの再実行では、前回の自動コミットを再利用して採番を重ねない。
        if git(root, "rev-parse", tip + "^") != source or marker not in git(root, "log", "-1", "--format=%B", tip).splitlines():
            raise ValueError("mainが更新されたため、古いコミットからの公開を中止します")
        git(root, "checkout", "--detach", tip)
        version = current_version(root)
        if requested and requested != version:
            raise ValueError("再実行で別の版には変更できません。新しい手動実行で指定してください")
        return {"commit": tip, "version": version, "tag": "kbcs-v" + version, "publish": "true"}
    tags = git(root, "tag", "--list", "kbcs-v*").splitlines()
    existing = "kbcs-v" + current
    if (requested or reuse_tag) and existing in tags and git(root, "rev-parse", existing + "^{commit}") == source and (not requested or requested == current):
        return {"commit": source, "version": current, "tag": existing, "publish": "true"}
    version, previous = select_version(current, tags, requested)
    update_files(root, version, previous)
    git(root, "add", "--", "Cargo.toml", "Cargo.lock", "README.md", f"docs/releases/{version}.md")
    git(root, "-c", "user.name=github-actions[bot]", "-c", "user.email=41898282+github-actions[bot]@users.noreply.github.com",
        "commit", "--allow-empty", "-m", f"chore: release {version}", "-m", marker)
    git(root, "push", "origin", "HEAD:refs/heads/main")
    return {"commit": git(root, "rev-parse", "HEAD"), "version": version, "tag": "kbcs-v" + version, "publish": "true"}


def main():
    ref = os.environ.get("GITHUB_REF", "")
    trusted = os.environ.get("GITHUB_REPOSITORY") == REPOSITORY
    result = prepare(ROOT, requested=os.environ.get("KBCS_RELEASE_VERSION", ""), source=os.environ.get("GITHUB_SHA", ""),
                     publish_branch=trusted and ref == "refs/heads/main",
                     tag=ref.removeprefix("refs/tags/") if trusted and ref.startswith("refs/tags/kbcs-v") else "",
                     reuse_tag=os.environ.get("GITHUB_EVENT_NAME") == "push")
    if output := os.environ.get("GITHUB_OUTPUT"):
        with open(output, "a", encoding="utf-8") as stream:
            for name, value in result.items():
                stream.write(f"{name}={value}\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
