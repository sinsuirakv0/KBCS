param([string]$Destination = (Join-Path $env:RUNNER_TEMP 'kbcs-llvm'))
$ErrorActionPreference = 'Stop'
# ローカルの検証済みビルドと同じコンパイラを固定し、配布元のSHAも照合する。
$version = '20260922'
$name = "llvm-mingw-$version-ucrt-x86_64.zip"
$sha = 'e3ad77d117a4bea19a7a3b333341824d79a5a371004a10e25b8504e7b3047666'
New-Item -ItemType Directory -Force -Path $Destination | Out-Null
$archive = Join-Path $Destination $name
Invoke-WebRequest -Uri "https://github.com/mstorsjo/llvm-mingw/releases/download/$version/$name" -OutFile $archive
if ((Get-FileHash -LiteralPath $archive -Algorithm SHA256).Hash.ToLowerInvariant() -ne $sha) {
    throw 'LLVM-MinGWのSHA-256が一致しません。'
}
Expand-Archive -LiteralPath $archive -DestinationPath $Destination -Force
$compiler = Join-Path $Destination "llvm-mingw-$version-ucrt-x86_64/bin"
$compiler | Out-File -FilePath $env:GITHUB_PATH -Append -Encoding utf8
@("KBCS_LLVM_BIN=$compiler", 'CC=clang', 'CXX=clang++', 'AR=llvm-ar') |
    Out-File -FilePath $env:GITHUB_ENV -Append -Encoding utf8
