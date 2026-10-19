# Private GitHubへの保存と復元

ソースと設計資料はPrivateリポジトリ `sinsuirakv0/KBCS` のGitへ保存します。大容量資料は同じPrivateリポジトリのReleaseへ保存し、`research/.local/` はGitから除外します。

## 保存内容

- 全関数索引、SQLite、関数別疑似コード、失敗関数の逆アセンブル、計測・実行記録。
- 自動解析完了後のGhidraプロジェクトZIPと初期試験時のZIP。作業用projectディレクトリはZIPと重複するため除外。
- 旧版15.7.1の参照用GZF、環境調査、APKの版・ハッシュ・manifest検証資料。
- APK・SOの単体ファイルは既定では除外。取得元Private Releaseからハッシュを照合して再取得可能。

認証情報、Python一時ファイル、apktoolの不要な旧版展開物、スクリプトコンパイル用一時物は保存しません。Ghidraプロジェクトには元ライブラリのバイトも含まれます。

## 取得と検索

リポジトリをcloneしたフォルダで実行します。Releaseの実際のタグはリポジトリのRelease一覧を参照してください。

```powershell
gh release download native-v15.7.2 --repo sinsuirakv0/KBCS --dir research/.local/downloads
Get-FileHash research/.local/downloads/native-v15.7.2-materials.tar.gz -Algorithm SHA256
tar -xzf research/.local/downloads/native-v15.7.2-materials.tar.gz
$cache = (Get-ChildItem research/.local/cache/15.7.2/arm64-v8a -Directory | Where-Object Name -Like '*-complete').FullName
python research/cli/cache.py --cache $cache stats
python research/cli/cache.py --cache $cache find appUpdateDraw
```

ダウンロードしたアーカイブのSHA-256は同梱manifest JSONの `sha256` と照合します。manifestには内部ファイルの相対パス・サイズ・SHA-256もあります。
保存時の `.local/reference.json` やidentity/configには元PCの絶対パスが残ります。別PCの検索では上記の `--cache` を指定します。解析を再開するときはGhidra/JDK、binary/snapshotなどのパスを新環境へ設定し、`backup-project.zip` を新しい作業先の `project/` に展開してください。保存済み資料の検索だけならGhidraもAPKも不要です。

## 再梱包

Ghidra・索引生成・デコンパイルの書込処理を終了してから実行します。

```powershell
$env:PYTHONPATH = (Resolve-Path research).Path
python -m indexer.materials --output research/.local/publish/native-v15.7.2-materials.tar.gz
```

既存出力は上書きしません。APK・SOも必要な保存先に含める場合は `--include-binaries` を付けます。このツールはアップロードせず、選択した資料のアーカイブとmanifestだけを生成します。Releaseの可視性がPrivateであることを確認してから `gh release create/upload` で保存します。
