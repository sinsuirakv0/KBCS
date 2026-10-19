# 設計と相互関係

## データの流れ

`indexer.apk.acquire` → GitHub版情報・Release検証 → manifest確認 → ABI別SO保存 → verified.json。

`indexer.run.main(init-latest)` → verified.jsonとSOハッシュ照合 → 独立Ghidraプロジェクトで初回解析 → `ExportCache.run(index)` → JSONL → JVM終了後にプロジェクトZIPバックアップ → `store.import_index` → SQLite。

`run.main(decompile)` → `store.sync_results` → 未保存・未失敗関数の要求一覧 → `run.headless` → `ExportCache.run(decompile)` → 関数別Cファイル・結果ジャーナル → SQLite状態更新。

`cli/cache.py` → ローカルSQLiteと必要な疑似コードだけを読む。検索にはGhidraもネットワークも不要。

## 同一性とスキーマ

データベースをゲーム版・ABI・SO SHA-256で物理分離する。`metadata` は版、ライブラリ、言語、image base、Ghidra版、取得根拠、スナップショットハッシュを保持する。
`functions` はアドレス、名前、bodyサイズ、外部/thunk属性、名前の由来、確度、デコンパイル状態と失敗理由を保持する。
`refs` は関数、参照元命令、参照先、参照種別、call属性、解決済み呼出先、関連文字列を保持する。
呼出元/先は同じrefsを逆方向/順方向に検索するため、重複したグラフを作らない。

確度は既定 `unreviewed`。Ghidraの検出を人間による意味確認と同一視しない。
関連文字列は参照先を含むGhidra定義済み文字列を優先する。未定義の場合は、初期化済み非実行領域から最大256バイトのNUL終端UTF-8/UTF-16LEを読み取り、厳格なデコードと制御文字検査を行う。この補助抽出は未確認の候補であり、誤検出を含み得る。Ghidraに文字列データを新規定義しない。
ポインタ多段参照、未解決間接呼出し、動的dispatchは推測しない。
索引はGhidraが認識した関数の全件であり、バイナリの全実行コードが発見済みであることを保証しない。
解析スナップショットを更新する場合は別ディレクトリへ作り直す。v1は同一バイナリの解析改訂の自動マージを行わない。`index --refresh` は同じ解析状態から索引だけを再抽出し、デコンパイル済み状態を保持する。

## 障害・負荷の扱い

- 逐次抽出。索引のJSONLはストリーム書込み、SQLite取込は単一トランザクション。
- 完了印のない索引を取り込まない。取込失敗は既存SQLiteをロールバックする。
- 疑似コードは一時ファイルから置換後、ジャーナルを1関数ずつflushする。
- 再開時はジャーナルを再読込。破損途中行を無視し、実ファイルが消えたcached状態をpendingへ戻す。
- failedは明示指定時だけ再試行し、無限リトライを避ける。
- 同一キャッシュへの書込はOSファイルロックで排他。別ABIを含む複数同時バッチは起動しない運用とする。
- バッチ上限は900秒。JVM停止後は完了済み関数だけを同期する。スクリプト完了ログも確認し、終了値0だけで成功扱いしない。
- 全件用の `indexer.complete` は別リビジョンを作り、ユーザー指定により自動解析・バッチ・1関数の時間上限を0（制限なし）にする。メモリ上限・1バッチ・失敗記録・再開は維持する。
- JVMのピークWorking SetをOS APIで測る。デコンパイラ子プロセスやOS全体のメモリを含まない。
- 大容量の索引・疑似コードはMCP応答に返さない。APIにはGZFの出力指示だけを渡す。

GhidraScriptの実行中はトランザクションが開かれており、`saveToPackedFile` はロック取得に失敗する。そのため新規解析のバックアップはJVM終了後のプロジェクト全体をZIPへ保存する。既存MCPのGZFエクスポートAPIはこの制約を適切に扱うため、そのまま利用する。
WindowsのJava起動では `-process *` が作業ディレクトリのファイルへ展開されるため、対象プログラム名を明示する。

完全版は初期キャッシュと別の `-complete` リビジョンに保存する。`analysis-complete.json` までは自動解析と索引作成、その後は内部関数をthunk込みで全件処理する。解析が改訂されるため初期疑似コードは移植しない。
構文木は保存しないため、DecompilerのtoggleSyntaxTree(false)で不要な転送を省く。decompileCompleted()はHighFunctionの有無で判定するAPIなので構文木なしでは使わず、C出力が存在し、開始失敗・取消・タイムアウトがないことを成功条件にする。
失敗分だけを構文木なしの標準設定、推論・分割を抑えたconservative設定、読み取り専用データの推論も抑えるminimal設定で有限回再試行する。追加設定は通常と解析条件が異なるためconfidence=lowで区別する。normalize/paramidも実験したが、同梱ghidra_process.ccではdecompile Action以外にCを返さないため復旧候補から除外した。復旧できなければfailed状態とアセンブリを保持する。
Windowsの `indexer.memory.enforce_memory` は、起動したJVM直下のdecompile.exeだけのPrivate Bytesを監視する。既定1536MiBを超えた子プロセスだけを終了し、memory-events.jsonlへ記録する。時間で中断する処理ではない。JVM側の関数失敗記録・再起動可能なDecompInterfaceにより、残りの関数を進める。
完了時に `catalog.tsv`、`external-functions.tsv`、`reference-summary.json` を作り、`.local/reference.json` を既定参照先へ更新する。既定参照資料の検索時は完了ジャーナルの再読込・全ファイル検査を省き、SQLiteを直接使う。

## APK取得と信頼境界

毎回GitHub上のversion.jsonを読む。Release assetのサイズ・SHA-256 digest、gzip/tar読取、統合APK SHA-256、manifest三値を照合する。
tarを丸ごと展開せず、唯一のapp.apkを固定パスへ取り出す。検証済みAPKは毎回SHA-256を再確認して再利用する。
manifestだけの小さなZIPを既存apktoolへ渡す。apktool.ymlのversionInfoはmanifestから取り出された版属性で、元APKの同一性はSHA-256で保証する。
workflowは読取のみ。署名検証・Split統合の信頼根拠は既存公開workflowと確定済みmerged hashであり、v1で署名検証器を重複実装しない。
通常の解析ではAPKや疑似コードを外部へ送らない。今回のユーザー指示によるPrivate KBCSへの資料保存は別途行い、大容量資料をPrivate Releaseへ保存する。認証情報は成果物へ含めない。

## 将来の版差分

新しいversion.jsonを取得し、同様に別の版/ABI/SHAディレクトリを作る。旧SQLiteをATTACHして関数名、サイズ、文字列アンカー、呼出関係を候補比較に使う。
次段階では関数bodyのバイトハッシュ、正規化命令/P-codeハッシュ、手動確認済み対応表を追加できる。アドレス一致だけで対応付けず、根拠と確度を別テーブルへ残す。
将来のengine/data/appは検証済み知見を成果物として参照し、Ghidra実行をランタイム依存にしない。
