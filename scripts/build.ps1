param(
    [string]$LlvmBin = $env:KBCS_LLVM_BIN,
    [switch]$DebugBuild,
    [string]$OutputDirectory = '.local/dist/0.1.17'
)

$ErrorActionPreference = 'Stop'
$workspace = Split-Path $PSScriptRoot -Parent
Push-Location $workspace
try {
    if ($LlvmBin) {
        $compilerPath = (Resolve-Path -LiteralPath $LlvmBin).Path
        if (-not (Test-Path -LiteralPath (Join-Path $compilerPath 'clang++.exe'))) {
            throw 'LLVM-MinGWのbinフォルダを指定してください。'
        }
        $env:PATH = $compilerPath + ';' + $env:PATH
        $env:CC = 'clang'
        $env:CXX = 'clang++'
        $env:AR = 'llvm-ar'
    }
    $profile = if ($DebugBuild) { 'debug' } else { 'release' }
    $buildArguments = @('build', '--workspace', '--locked')
    if (-not $DebugBuild) { $buildArguments += '--release' }
    & cargo @buildArguments
    if ($LASTEXITCODE -ne 0) { throw 'Cargoビルドに失敗しました。' }
    $destination = Join-Path $workspace $OutputDirectory
    New-Item -ItemType Directory -Force -Path $destination | Out-Null
    $targetDirectory = if ($env:CARGO_TARGET_DIR) { $env:CARGO_TARGET_DIR } else { Join-Path $workspace 'target' }
    Copy-Item -LiteralPath (Join-Path $targetDirectory "$profile/kbcs.exe") -Destination $destination
    $hostTarget = (& rustc -vV | Select-String '^host:').ToString().Split(':', 2)[1].Trim()
    $metadata = (& cargo metadata --format-version 1 --locked --filter-platform $hostTarget | ConvertFrom-Json)
    if ($LASTEXITCODE -ne 0) { throw '依存パッケージ情報の取得に失敗しました。' }
    $webviewPackage = $metadata.packages | Where-Object name -EQ 'webview2-com-sys' | Select-Object -First 1
    if ($webviewPackage) {
        $loaderArchitecture = if ($hostTarget.StartsWith('aarch64')) { 'arm64' } elseif ($hostTarget.StartsWith('i686')) { 'x86' } else { 'x64' }
        $loader = Join-Path (Split-Path $webviewPackage.manifest_path -Parent) "$loaderArchitecture/WebView2Loader.dll"
        Copy-Item -LiteralPath $loader -Destination $destination
    }
    if ($LlvmBin) {
        foreach ($name in @('libunwind.dll', 'libc++.dll', 'libwinpthread-1.dll')) {
            $runtimePath = Join-Path $compilerPath $name
            if (Test-Path -LiteralPath $runtimePath) { Copy-Item -LiteralPath $runtimePath -Destination $destination }
        }
    }
    Write-Host "起動: $destination/kbcs.exe"
} finally {
    Pop-Location
}
