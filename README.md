# KBCS インストールガイド

## 推奨動作環境

以下は快適に利用するための推奨目安です。

| 項目 | 推奨環境 |
| --- | --- |
| OS | Windows 11・64ビット（x64） |
| CPU | x64対応・4コア以上 |
| メモリ | 16GB以上 |
| グラフィックス | WebGL 2.0対応GPU |
| ストレージ | SSD・空き容量5GB以上（データ・画像・BGMの保存用） |
| 必要なソフト | Microsoft Edge WebView2 Runtime（Evergreen） |
| 通信環境 | インターネット接続（初回データ取得・更新・画像やBGMの読み込み用） |

## インストール手順

1. [KBCS 0.1.35のWindows版ZIPをダウンロード](https://github.com/sinsuirakv0/KBCS/releases/download/kbcs-v0.1.35/KBCS-0.1.35-windows-x64.zip)します。
2. ダウンロードしたZIPを右クリックし、**「すべて展開」**を選びます。展開された`kbcs.exe`とDLLファイルは、同じフォルダーにまとめて置きます。
3. WebView2 Runtimeが未導入の場合は、[Microsoft公式配布ページ](https://developer.microsoft.com/ja-jp/microsoft-edge/webview2/)から**「エバーグリーン ブートストラップ」**をダウンロードして実行します。
4. 展開先の**`kbcs.exe`**をダブルクリックして起動します。
5. ホームの**「データ管理」→「データ取得・更新」**を押し、データの取得・取り込みが完了するまで待ちます。

データ・編成・設定は、通常`%LOCALAPPDATA%\KBCS`へ自動保存されます。アプリを更新するときは、新しいWindows版ZIPを展開して`kbcs.exe`を起動すると、保存済みのデータ・編成・設定を引き継げます。
