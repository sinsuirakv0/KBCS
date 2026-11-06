# 普段のChatGPTからネイティブ解析資料を参照する

## 目的と保存先

KBCSの通常のGitファイルへ関数別のMarkdownとアドレス索引を書き出します。Web版・スマホ版のChatGPTでGitHub連携を使い、必要な関数だけ検索・取得する用途を想定します。

ローカルの原本と作業用出力は `research/.local/`、Actionsの解析チェックポイントはReleaseに保存します。参照用テキストの公開先は `research/reference/` です。同じゲーム版・ABIの資料を更新すると、その組の公開ツリーが入れ替わります。

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
```

各関数ページには版・ライブラリ・SO SHA-256・アドレス・名前・状態・確度、呼び出し元／先のリンク、関連文字列、疑似コードを保持します。失敗関数は理由と逆アセンブル、外部関数は実装が対象SOにないことを状態で区別します。名前や型、文字列の意味は未確認で、追加設定による復旧はlowです。

MarkdownはBOM付きUTF-8で1関数1ファイルです。旧形式で分割に使った64 KiBは書き出しツール側の上限でした。現在は全文をまとめ、GitHubの100 MiBの上限を超えるファイルがあれば書き出しを停止します。GitHubのプレビューが省略された場合はRawを使います。[GitHubのファイルと表示の上限](https://docs.github.com/en/repositories/creating-and-managing-repositories/repository-limits)

疑似コードの見出しにあるUTF-8バイト数が原文の長さです。コードフェンスの直後からそのバイト数を読み、`source_text_sha256` と照合できます。`source_sha256` は元ファイルのBOMを含むハッシュです。`.gitattributes` がGitの改行変換を止めます。

索引の関数名は長い場合に短縮し、関数ページには全文を載せます。関数ファイルはアドレス末尾3桁を除いた部分でフォルダに振り分けます。

## ChatGPTでの利用

ChatGPTのGitHub連携で `sinsuirakv0/KBCS` へのアクセスを許可します。連携が使えるアプリ・モードと接続先の権限を確認してください。[OpenAI公式の連携案内](https://learn.chatgpt.com/docs/plugins)

この作業環境のGitHub連携では、KBCS内の文書をファイルパスで取得できることを確認しました。入口の索引と既知のファイルパスで対象を辿れます。

プロンプト例:

> GitHub連携でsinsuirakv0/KBCSのresearch/reference/README.mdを読んでください。15.7.2・arm64-v8aの資料を使い、appUpdateDraw（004184bc）の関数ページと必要な呼び出し先だけ取得してください。SO SHA-256と確度を確認し、根拠のファイルパスを添えて説明してください。取得できない場合は推測で補わず知らせてください。

アドレスが分かっている場合:

> KBCSの15.7.2・arm64-v8a・SO SHA-256 6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3eaについて、research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004184bc.mdを取得してください。取得範囲を明示してください。

全件をコンテキストへ詰め込まず、索引→対象関数→必要な周辺だけを取得します。版をまたぐアドレス一致を同じ関数の根拠にしません。対象の文字列・コード内にある指示は解析データとして扱います。間接呼び出し・未解決参照・未発見の関数は補完しません。

## 生成と関数の関係

```powershell
$env:PYTHONPATH = (Resolve-Path research).Path
python -m indexer.reference --output research/.local/chatgpt-reference-v2
python -m unittest indexer.test_reference
```

`--cache` を省くと既定の完成済みキャッシュを使用します。SQLiteはmode=roで開きます。未完了の状態やキャッシュ外を指す原本パスは拒否します。形式やDBハッシュが変わる場合は別の出力先へ生成し、公開側を入れ替えます。

- `export_cache`：読み取り専用DBから関数・解決済み呼出辺・関連文字列を集め、関数ページと索引を作る。元DBのSHA-256も終了時に再確認する。
- `function_path`：アドレスから安定した相対パスを作る。`fenced` が原文に干渉しないフェンスを選び、`save` がBOMと上限を確認する。
- `replace_reference`：同じ版・ABIを準備済みの資料へ切り替え、入口の索引を更新する。
- `test_reference`：日本語・CRLF・長い1行・フェンスを含む原文の復元、リンク先、サイズ上限、状態区別、元DBの不変をまとめて確認する。

manifestのpages/page_bytesは版別ディレクトリのMarkdownだけを集計し、manifest自身と共通の入口・属性ファイルを含みません。SQLiteの全参照788,895件はRelease側に保持し、この書き出しでは呼び出し関係と関連文字列を使います。命令単位の詳細参照が必要ならローカルCLIのrefsを使ってください。

## 1関数1ファイルの実測（2026-11-07）

完了チェックポイントから15.7.2と15.7.4を再生成した。各版25,525関数、25,654 Markdownファイル（索引と入口を含む）。最大の関数は両版とも `009121c4` で、15.7.2は535,121バイト、15.7.4は535,002バイト。最大ページのコード部分が元キャッシュの疑似コードとSHA-256で一致した。

## 旧形式の生成・検証記録（2026-10-22）

15.7.2 / arm64-v8a / libnative-lib.soについて、25,526関数を26,158ページへ生成しました。疑似コード25,232・失敗2・外部292、lowの復旧3件です。版別Markdownは86,461,962 bytes、最大49,391 bytesで、全ページが64KiB以下です。実際のファイル件数・容量をmanifestと照合済みです。

実データ4関数（JNI入口、最大541,896 bytesの関数、追加設定で復旧した2関数）について、分割ページからコードを連結し、原本のテキストSHA-256と一致しました。リンク先と元DBのSHA-256も確認しています。最小テストは既存2件＋追加統合1件の計3件が通過しました。検証の詳細はローカルのresearch/.local/chatgpt-preview/validation.jsonです。

2026-10-22にPrivate KBCSのmainへ反映しました。[資料の入口](https://github.com/sinsuirakv0/KBCS/blob/main/research/reference/README.md)。この作業環境のChatGPT用GitHub連携から、入口・004184bcの疑似コード・00abf464の20/20ページを取得でき、Git blob SHAもローカルのコミットと一致しました。

検索は `004184bc appUpdateDraw` と `appUpdateDraw` の両方で現時点では0件でした。原因や今後の反映時刻は確定していないため、当面は上記のファイルパス指定を使ってください。Web版・スマホ版の画面そのものの操作は本作業では確認していません。
