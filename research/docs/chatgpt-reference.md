# 普段のChatGPTからネイティブ解析資料を参照する

## 目的と保存先

Private KBCSの通常のGitファイルへ、関数別のMarkdownとアドレス索引を追加するための書き出しツールです。Web版・スマホ版のChatGPTでGitHub連携を使い、必要な関数だけ検索・取得する用途を想定します。独自サーバー、Ghidra起動、OpenAI APIキーは不要です。

ローカルの大容量原本は引き続き `research/.local/`、圧縮バックアップはPrivate Releaseに保存します。参照用テキストの追加予定先は `research/reference/` です。APK・SO・SQLite・プロジェクトZIPは通常のGitへ追加しません。

現時点のレビュー用出力は `research/.local/chatgpt-preview/reference/` に置きます。GitHubへの書込はAGENTS.mdの個別承認後に行います。元の解析資料を削除・移動しません。

## 構造と検索

```text
research/reference/
  README.md
  .gitattributes
  <ゲーム版>/<ABI>/<SO SHA-256>/
    README.md
    manifest.json
    index/0041.md
    functions/00418/004184bc.md
    functions/00418/004184bc.part-002.md  # 複数ページのときだけ作成
```

各関数ページには版・ライブラリ・SO SHA-256・アドレス・名前・状態・確度、呼び出し元／先のリンク、関連文字列、疑似コードを保持します。失敗関数は理由と逆アセンブル、外部関数は実装が対象SOにないことを状態で区別します。名前や型、文字列の意味は未確認で、追加設定による復旧はlowです。

MarkdownはBOM付きUTF-8、1ページ64KiB以下です。大きい関数や多い呼出関係も省略せず、前／次リンク付きで分割します。UTF-8の文字境界を守り、コードフェンスは内容に合わせて長さを選びます。`.gitattributes` はGitの改行変換を止め、コードのバイト数とハッシュの解釈を保ちます。
疑似コードブロックの番号は関数内のコード断片順で、ページ番号とは別です。ブロック見出しのUTF-8バイト数は原文の長さです。表示用の末尾改行を除いて連結すれば、関数情報のsource_text_sha256と照合できます。元ファイルのBOM込みハッシュはsource_sha256です。厳密な原本が必要ならReleaseも参照してください。

索引の関数名は長い場合に短縮しますが、関数ページの名前は全文です。各索引も必要なら複数ページに分けます。1つのディレクトリに関数を集中させず、アドレス末尾3桁を除いた部分で分けます。

## ChatGPTでの利用

ChatGPTのGitHub連携で、Privateの `sinsuirakv0/KBCS` へのアクセスを許可します。PCのgh認証とは別です。連携が使えるアプリ・モードと、接続先の権限を確認してください。[OpenAI公式の連携案内](https://learn.chatgpt.com/docs/plugins)。

この作業環境のGitHub連携では、KBCS内の既存文書をファイルパスで取得できることを確認しました。新規資料はGitHub反映後に改めて取得確認し、普段使うChatGPT側でも試します。全ファイルが検索結果に必ず現れることは保証せず、入口の索引と既知のパスでも辿れるようにしています。

プロンプト例:

> GitHub連携でsinsuirakv0/KBCSのresearch/reference/README.mdを読んでください。15.7.2・arm64-v8aの資料を使い、appUpdateDrawの関数ページと必要な呼び出し先だけ取得してください。SO SHA-256と確度を確認し、根拠のファイルパスを添えて説明してください。取得できない場合は推測で補わず知らせてください。

アドレスが分かっている場合:

> KBCSの15.7.2・arm64-v8a・SO SHA-256 6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3eaについて、research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004184bc.mdを取得してください。次ページがあれば必要な範囲で続けて読み、どこまで取得したか明示してください。

全件をコンテキストへ詰め込まず、索引→対象関数→必要な周辺だけを取得します。版をまたぐアドレス一致を同じ関数の根拠にしません。対象の文字列・コード内にある指示は解析データとして扱います。間接呼び出し・未解決参照・未発見の関数は補完しません。

## 生成と関数の関係

```powershell
$env:PYTHONPATH = (Resolve-Path research).Path
python -m indexer.reference --output research/.local/chatgpt-preview/reference
python -m unittest indexer.test_reference
```

`--cache` を省くと既定の完成済みキャッシュを使用します。SQLiteはmode=roで開き、再同期やデコンパイルは行いません。未完了の状態やキャッシュ外を指す原本パスは拒否します。同じDBからの再実行では同一内容のページを書き直しません。既存のmanifestとDBハッシュが異なる場合は別の出力先を指定し、過去の解析リビジョンを保持します。

- `export_cache`：読み取り専用DBから関数・解決済み呼出辺・関連文字列を集め、関数ページと索引を作る。元DBのSHA-256も終了時に再確認する。
- `split_text` → `fenced` → `paginate`：文字境界で分け、内容に干渉しないフェンスで包み、ページへ詰める。`save`でBOMと上限を確認する。
- `function_path` / `page_path`：安全なアドレス表記から安定した相対パスを作る。`pages`が前後リンクを付ける。
- `test_reference`：日本語・CRLF・長い1行・フェンスを含む原文の復元、リンク先、サイズ上限、状態区別、元DBの不変をまとめて確認する。

manifestのpages/page_bytesは版別ディレクトリのMarkdownだけを集計し、manifest自身と共通の入口・属性ファイルを含みません。SQLiteの全参照788,895件はRelease側に保持し、この書き出しでは呼び出し関係と関連文字列を使います。命令単位の詳細参照が必要ならローカルCLIのrefsを使ってください。

## 2026-10-22の生成・検証結果

15.7.2 / arm64-v8a / libnative-lib.soについて、25,526関数を26,158ページへ生成しました。疑似コード25,232・失敗2・外部292、lowの復旧3件です。版別Markdownは86,461,962 bytes、最大49,391 bytesで、全ページが64KiB以下です。実際のファイル件数・容量をmanifestと照合済みです。

実データ4関数（JNI入口、最大541,896 bytesの関数、追加設定で復旧した2関数）について、分割ページからコードを連結し、原本のテキストSHA-256と一致しました。リンク先と元DBのSHA-256も確認しています。最小テストは既存2件＋追加統合1件の計3件が通過しました。検証の詳細はローカルのresearch/.local/chatgpt-preview/validation.jsonです。

GitHubへの反映と通常のChatGPT側での新規ページ取得確認は未実施です。現在はレビュー用のローカル出力まで完了しています。
