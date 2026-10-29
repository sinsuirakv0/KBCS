#!/usr/bin/env python3
# 実画面の操作・ゲーム原本の取得をせず、隠したWebViewで接続を検査する。
import argparse
import json
from pathlib import Path
import subprocess
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument("--binary", type=Path, required=True)
args = parser.parse_args()
with tempfile.TemporaryDirectory(prefix="kbcs-desktop-check-", ignore_cleanup_errors=True) as temporary:
    result = subprocess.run([str(args.binary.resolve()), "desktop-check", "--data-dir", temporary],
        capture_output=True, timeout=60, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    logs = result.stderr.decode("utf-8", errors="replace")
    records = [json.loads(line.split("KBCS desktop check: ", 1)[1]) for line in logs.splitlines() if "KBCS desktop check: " in line]
    if result.returncode or not records or not records[-1].get("ok"):
        raise RuntimeError(f"WebView接続失敗: {result.returncode}\n{logs}")
    print("WebView module/PNG/POST/C++/WebGL:", records[-1])
