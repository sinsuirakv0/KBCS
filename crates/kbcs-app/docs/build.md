# Windows・macOSのビルド（2026-10-29）

## 関係する処理

`main`はWindows/macOSで共通の`desktop::run`を起動する。taoのウィンドウとwryの専用プロトコルにより、同じ埋込みUI・Service・Rust/C++の戦闘カーネルを使う。WindowsはWebView2、MacはOS付属のWKWebView。戦闘処理や論理フレームのOS別分岐は追加しない。MacはApple SiliconとIntelをそれぞれのCPUでビルド・テストする。Universal化やRosettaへの依存はない。

`default_data_dir`はKBCS_DATA_DIR/--data-dirの指定を維持し、既定ではWindowsのLOCALAPPDATA/KBCSとMacのHOME/Library/Application Support/KBCSを使う。MacのWKWebViewはdata_directory非対応なので、その保存先をSHA-256にした先頭16bytesをdata-store identifierに使う。macOS 14以上を対象とし、設定をアプリ再ビルドごとに初期化しない。ヘルプだけを固定URLで外部ブラウザへ渡し、専用画面の任意外部遷移を許可しない。

`runtime::Monitor`はWindowsの既存API、Macのhost_statistics/host_statistics64・sysctlbyname・proc_pidinfoからCPU/メモリを取得する。MacのmemoryAvailableは空き＋非活性ページの概算。ページサイズを問い合わせ、Apple Siliconを4KiBと決め打ちしない。host portを毎回解放する。論理フレーム・戦闘結果は監視値で変更しない。

## 自動ビルド

[build.yml](../../../.github/workflows/build.yml)はpush・pull_request・手動起動で動く。ローカルcommitだけではGitHubは起動できず、pushが必要。既存の研究/ゲーム原本への接続・データ自動取得・原本への書込はCIで行わない。

| runner | Rust target | 配布名 |
| --- | --- | --- |
| windows-2022 | x86_64-pc-windows-gnullvm | KBCS-VERSION-windows-x64.zip |
| macos-15 | aarch64-apple-darwin | KBCS-VERSION-macos-arm64.zip |
| macos-15-intel | x86_64-apple-darwin | KBCS-VERSION-macos-x64.zip |

RunnerのCPUは[GitHubの一覧](https://docs.github.com/en/actions/reference/runners/github-hosted-runners)を確認した。macos-latestへの暗黙依存を避ける。Rust 1.98.1、WindowsのLLVM-MinGW 20260922を固定し、LLVM配布ZIPのSHA-256を照合する。C++20・ffp-contract=off・fwrapvは既存bridge/build.rsを共用する。MacのMACOSX_DEPLOYMENT_TARGETとInfo.plistは14.0を揃える。

各jobはCargo.lock固定のworkspace releaseテスト、clippy、既存JS回帰、releaseビルドを実行し、package.pyが成果物のCPU種別・単独help起動・SHA-256を確認する。C++の同じ原本照合ベクトルを全CPUで使う。UIの見た目やWKWebViewの実機操作まで検証したことにはしない。

ActionsのArtifactsは14日保存し、ZIP・SHA・版/commit/コンパイラ情報JSONを含む。`kbcs-vVERSION`タグのpushでは、全build成功後にrelease jobが3種類のZIP・SHA・JSONを収集する。publish-release.pyがCargoの版、commit、ローカルSHA、アップロード後のGitHubのSHA/サイズを照合し、ドラフトから公開開発版へ切り替える。途中失敗は公開しない。公開済み同名リリースは上書きしない。本体更新機能が参照するのはReleasesであり、ActionsのArtifactを直接更新配布元にはしない。配布時はCargo.tomlのversion・READMEの入手リンク・docs/releases/VERSION.mdを更新してからタグをpushする。公開・push・workflow実行にはリポジトリの承認方針を適用する。今回のv0.1.36公開はユーザーの明示依頼による。

## 配布パッケージ

`scripts/package.py --target TARGET`はビルド済み`target/TARGET/release/kbcs(.exe)`を収集する。`--binary`・`--output`・`--llvm-bin`でローカルの既存ビルド場所を指定できる。WindowsはWebView2LoaderとLLVM-MinGWの3DLLをまとめ、MacはKBCS.app/Contents/MacOS/kbcsとInfo.plistを生成する。Macはシステム以外のdylib依存があれば失敗する。

MacのZIPはUnixの実行権限を保持する。コード署名後にバンドル内部へ検証JSON等を書き足さない。コードとUIは実行ファイルへ同梱し、外部research・元Web checkout・Python・Node.jsは実行時に不要。

Macは既定でad-hoc署名しcodesign --verify --deep --strictで検証する。これはDeveloper ID署名/Apple公証ではない。初回起動ではOSの確認が必要になることがある。配布者があらかじめkeychainへDeveloper IDを導入した環境ではKBCS_MACOS_SIGN_IDENTITYで署名先を指定できるが、CIへ証明書を導入する設定や公証は今回自動化していない。[Appleの配布要件](https://developer.apple.com/documentation/security/notarizing-macos-software-before-distribution)を参照。Gatekeeperを無効にする処理は追加しない。

Macでの手動ビルド例（Rust・Xcode Command Line Tools・Python 3.11以上を導入済み）:

```sh
export MACOSX_DEPLOYMENT_TARGET=14.0
# Apple Siliconの場合。Intelではx86_64-apple-darwinへ読み替える。
cargo build --workspace --release --locked --target aarch64-apple-darwin
python3 scripts/package.py --target aarch64-apple-darwin
```

Windowsの従来のscripts/build.ps1も維持する。CIと同じZIPを作るには同じgnullvm targetでビルドしpackage.pyを呼ぶ。


`desktop-check`はCI用の非表示ウィンドウで、実際のWebView上からES module・暗号学的通信ID・PNG・JSON POST本文・C++のモーション時計・WebGL contextを検査する。自動更新の開始を省略し、40秒で応答がなければ失敗する。check-desktop.pyは隔離した一時data-dirを使い、画面操作や実ゲームデータのダウンロードは行わない。通常起動の経路は同じbuilder/serviceを使う。WKWebViewの専用スキームではrandomUUIDの提供を前提にせず、getRandomValuesによるUUID生成を共用する。ゲーム内のRNGとは別物。
