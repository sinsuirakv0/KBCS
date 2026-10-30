# KBCS インストールガイド

## インストールファイル

| 使用する端末 | ZIPのファイル名 |
| --- | --- |
| Windows 64ビット | `KBCS-<バージョン>-windows-x64.zip` |
| Mac・Mシリーズ | `KBCS-<バージョン>-macos-arm64.zip` |
| Mac・Intel | `KBCS-<バージョン>-macos-x64.zip` |

[リリースページ](https://github.com/sinsuirakv0/KBCS/releases)の **Assets** から、自分の端末用ZIPがある最新のKBCS版をダウンロードします。OSごとにビルドが成功し次第公開するため、最新リリースに対応ZIPがない場合は一つ前以降のリリースを確認してください。アプリ内の更新も、端末に対応した最新版を案内します。

## 推奨動作環境

以下は快適に利用するための推奨目安です。

| 項目 | Windows | Mac |
| --- | --- | --- |
| OS | Windows 11・64ビット（x64） | macOS 14以降 |
| CPU | x64対応・4コア以上 | Apple Silicon（Mシリーズ・arm64）またはIntel（x64） |
| メモリ | 16GB以上 | 16GB以上 |
| グラフィックス | WebGL 2.0対応GPU | WebGL 2.0対応GPU |
| ストレージ | SSD・空き容量5GB以上 | SSD・空き容量5GB以上 |
| 必要なソフト | Microsoft Edge WebView2 Runtime（Evergreen） | OS付属のWebKitを使用 |
| 通信環境 | 初回データ取得・更新時にインターネット接続 | 初回データ取得・更新時にインターネット接続 |

## インストール手順

### Windows

1. [Releases](https://github.com/sinsuirakv0/KBCS/releases)でWindows用ZIPがある最新のKBCS版から、`KBCS-<バージョン>-windows-x64.zip`をダウンロードします。
2. ZIPを右クリックし、**「すべて展開」**を選びます。`kbcs.exe`とDLLファイルは同じフォルダーに置きます。
3. WebView2 Runtimeが未導入の場合は、[Microsoft公式配布ページ](https://developer.microsoft.com/ja-jp/microsoft-edge/webview2/)から**「エバーグリーン ブートストラップ」**をダウンロードして実行します。
4. 展開先の**`kbcs.exe`**をダブルクリックして起動します。

### Mac

1. Appleメニューの**「このMacについて」**を開き、チップの種類を確認します。
2. [Releases](https://github.com/sinsuirakv0/KBCS/releases)で自分のMac用ZIPがある最新のKBCS版から、Mシリーズは`KBCS-<バージョン>-macos-arm64.zip`、Intelは`KBCS-<バージョン>-macos-x64.zip`をダウンロードします。
3. ZIPを展開し、**`KBCS.app`**を自分のホーム内の**`Applications`**フォルダーへ移動します。フォルダーがなければFinderで作成してください。
4. 移動した**`KBCS.app`**をダブルクリックして起動します。
5. 現在のMac用自動ビルドは開発用署名です。開発元を確認できないと表示された場合は、配布元を確認し、**「システム設定」→「プライバシーとセキュリティ」→「このまま開く」**から起動します。[Appleの案内](https://support.apple.com/ja-jp/102445)

### 最新の自動ビルドを使う場合

[Actions](https://github.com/sinsuirakv0/KBCS/actions/workflows/build.yml)の最新の**「Build Windows and macOS」**を開き、自分の端末のbuildジョブが成功していれば、Artifactsから`KBCS-windows-x64`・`KBCS-macos-arm64`・`KBCS-macos-x64`をダウンロードできます。他のOSの失敗により実行全体が赤くなっていても、成功した端末の成果物を利用できます。ArtifactsのダウンロードにはGitHubへのログインが必要です。外側のZIPを展開し、中の`KBCS-<バージョン>-<端末>.zip`を上記の手順で展開します。

### 初回データ取得・更新

初回起動時は必要なデータを自動取得します。取得が完了するまで待ってください。失敗した場合はホームの**「設定 → データ管理」**（旧版は「データ管理」）から再試行できます。

データ・編成・設定は、Windowsでは`%LOCALAPPDATA%\KBCS`、Macでは`~/Library/Application Support/KBCS`へ保存されます。本体を入れ替えても同じ場所のデータを引き継ぎます。新しい本体・データの公開時は起動時に通知します。後回しにした更新は、ホームの**「設定 → データ管理」**（旧版は「データ管理」）から実行できます。
