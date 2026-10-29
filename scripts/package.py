#!/usr/bin/env python3
# ビルド済み実行ファイルを、更新機能と共通の命名・配置で配布する。
import argparse
import hashlib
import json
import os
from pathlib import Path
import plistlib
import shutil
import struct
import subprocess
import sys
import tempfile
import tomllib
import zipfile

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {
    "x86_64-pc-windows-gnullvm": "windows-x64",
    "aarch64-apple-darwin": "macos-arm64",
    "x86_64-apple-darwin": "macos-x64",
}


def run(*args):
    return subprocess.check_output([str(arg) for arg in args], cwd=ROOT, text=True, encoding="utf-8").strip()


def check_binary(path, target):
    with path.open("rb") as stream:
        header = stream.read(64)
        if "windows" in target:
            if header[:2] != b"MZ":
                raise ValueError("Windowsの実行ファイルではありません")
            stream.seek(struct.unpack_from("<I", header, 60)[0])
            if stream.read(6) != b"PE\0\0\x64\x86":
                raise ValueError("Windows x64ではありません")
        else:
            cpu = 0x0100000C if target.startswith("aarch64") else 0x01000007
            if header[:8] != struct.pack("<II", 0xFEEDFACF, cpu):
                raise ValueError("MacのCPU種別が一致しません")


def windows_files(binary, folder, target, llvm_bin):
    shutil.copy2(binary, folder / "kbcs.exe")
    metadata = json.loads(run("cargo", "metadata", "--format-version", "1", "--locked", "--filter-platform", target))
    package = next(p for p in metadata["packages"] if p["name"] == "webview2-com-sys")
    loader = Path(package["manifest_path"]).parent / "x64/WebView2Loader.dll"
    shutil.copy2(loader, folder / loader.name)
    if not llvm_bin:
        compiler = shutil.which("clang++")
        if not compiler:
            raise ValueError("LLVM-MinGWのbinを--llvm-binで指定してください")
        llvm_bin = str(Path(compiler).parent)
    for name in ("libc++.dll", "libunwind.dll", "libwinpthread-1.dll"):
        shutil.copy2(Path(llvm_bin) / name, folder / name)
    return folder / "kbcs.exe"


def macos_files(binary, folder, version):
    app = folder / "KBCS.app"
    executable = app / "Contents/MacOS/kbcs"
    executable.parent.mkdir(parents=True)
    shutil.copy2(binary, executable)
    executable.chmod(0o755)
    info = {
        "CFBundleIdentifier": "io.github.sinsuirakv0.kbcs",
        "CFBundleName": "KBCS", "CFBundleDisplayName": "KBCS",
        "CFBundleExecutable": "kbcs", "CFBundlePackageType": "APPL",
        "CFBundleShortVersionString": version.split("-")[0].split("+")[0],
        "CFBundleVersion": version.split("-")[0].split("+")[0],
        "KBCSVersion": version, "LSMinimumSystemVersion": "14.0",
        "NSHighResolutionCapable": True, "NSPrincipalClass": "NSApplication",
        "NSSupportsAutomaticGraphicsSwitching": True,
    }
    with (app / "Contents/Info.plist").open("wb") as stream:
        plistlib.dump(info, stream)
    # 全コードとUIは単一バイナリ内。システム以外のdylibへの依存を許可しない。
    libraries = run("/usr/bin/otool", "-L", executable).splitlines()[1:]
    for library in libraries:
        if not library.strip().startswith(("/usr/lib/", "/System/Library/")):
            raise ValueError("同梱されていないライブラリ: " + library)
    identity = os.environ.get("KBCS_MACOS_SIGN_IDENTITY", "-")
    args = ["/usr/bin/codesign", "--force", "--sign", identity, "--identifier", info["CFBundleIdentifier"]]
    if identity != "-":
        args += ["--options", "runtime", "--timestamp"]
    run(*args, app)
    run("/usr/bin/codesign", "--verify", "--deep", "--strict", app)
    return executable


def main():
    parser = argparse.ArgumentParser(description="Windows/Mac配布ZIPを作成し、単独起動を検査")
    parser.add_argument("--target", choices=TARGETS, required=True)
    parser.add_argument("--binary", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT / ".local/dist")
    parser.add_argument("--llvm-bin", default=os.environ.get("KBCS_LLVM_BIN"))
    args = parser.parse_args()
    version = tomllib.loads((ROOT / "Cargo.toml").read_text(encoding="utf-8-sig"))["workspace"]["package"]["version"]
    target_dir = Path(os.environ.get("CARGO_TARGET_DIR", ROOT / "target"))
    binary = (args.binary or target_dir / args.target / "release" / ("kbcs.exe" if "windows" in args.target else "kbcs")).resolve()
    check_binary(binary, args.target)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    name = f"KBCS-{version}-{TARGETS[args.target]}"
    archive = output / (name + ".zip")
    with tempfile.TemporaryDirectory(prefix="kbcs-package-", dir=output) as temporary:
        folder = Path(temporary)
        if "windows" in args.target:
            executable = windows_files(binary, folder, args.target, args.llvm_bin)
        else:
            executable = macos_files(binary, folder, version)
        # データ取得・GUI起動をせず、配布物だけで依存ライブラリを解決できるか確認。
        result = subprocess.run([str(executable), "help"], cwd=folder, capture_output=True, timeout=30)
        if result.returncode or b"kbcs [" not in result.stdout:
            raise RuntimeError(f"配布物の起動に失敗: {result.returncode}: {result.stderr!r}")
        print(run(sys.executable, ROOT / "scripts/check-desktop.py", "--binary", executable))
        with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zipped:
            for path in sorted(folder.rglob("*")):
                if path.is_file():
                    zipped.write(path, path.relative_to(folder).as_posix())
    with archive.open("rb") as stream:
        digest = hashlib.file_digest(stream, "sha256").hexdigest()
    (output / (name + ".zip.sha256")).write_text(f"{digest}  {archive.name}\n", encoding="ascii")
    (output / (name + ".json")).write_text(json.dumps({
        "version": version, "target": args.target, "archive": archive.name,
        "sha256": digest, "commit": run("git", "rev-parse", "HEAD"),
        "rust": run("rustc", "--version"), "macosSigning": os.environ.get("KBCS_MACOS_SIGN_IDENTITY", "ad-hoc") if "apple" in args.target else None,
    }, indent=2) + "\n", encoding="utf-8")
    print(archive)


if __name__ == "__main__":
    main()
