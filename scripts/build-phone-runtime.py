import argparse
import os
from pathlib import Path
import shutil
import subprocess


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    output = args.output.resolve()
    target = "wasm32-unknown-emscripten"
    target_dir = Path(os.environ.get("CARGO_TARGET_DIR", root / "target")).resolve()
    exports = [
        "_kbcs_phone_input", "_kbcs_phone_output", "_kbcs_phone_length", "_kbcs_phone_call"
    ]
    flags = [
        "-fwasm-exceptions",
        "-sMODULARIZE=1",
        "-sEXPORT_ES6=1",
        "-sENVIRONMENT=worker,node",
        "-sALLOW_MEMORY_GROWTH=1",
        "-sSTACK_SIZE=8388608",
        "-sFILESYSTEM=0",
        "-sEXPORTED_RUNTIME_METHODS=HEAPU8",
        "-sEXPORTED_FUNCTIONS=" + ",".join(exports),
    ]
    subprocess.run(
        ["cargo", "rustc", "--locked", "--release", "--target", target, "-p", "kbcs-app",
         "--features", "phone-wasm", "--bin", "kbcs-phone", "--",
         *(argument for flag in flags for argument in ("-C", f"link-arg={flag}"))],
        check=True,
        cwd=root,
    )
    output.mkdir(parents=True, exist_ok=True)
    built = target_dir / target / "release"
    shutil.copy2(built / "kbcs-phone.js", output / "kbcs-phone.mjs")
    shutil.copy2(built / "kbcs_phone.wasm", output / "kbcs_phone.wasm")


if __name__ == "__main__":
    main()
