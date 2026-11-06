# GitHub Actions自動解析 v1

## 対象と現在の状態

最初の対象はJP15.7.2 / versionCode 1507021 / arm64-v8a / libnative-lib.so。入力の版・APK/アーカイブ/SO SHA-256は `research/inputs/jp-1507021.json` に固定する。2026-10-20に確認した原本の再生成であり、最新版の版番号を推測しない。上流の取得workflowは起動・変更しない。

Python 3.13、Ghidra 12.1.2、Temurin JDK 21.0.11+10、apktool 2.12.1を使用する。Ghidra/apktoolの公式配布URLとSHA-256は `research/ghidra/runtime.json`。解析・抽出・資料生成はPython/Javaで実行し、AI APIは使わない。比較、関数の版間対応、意味の推測は対象外。

2026-11-06に15.7.2の[GitHub Actions実行](https://github.com/sinsuirakv0/KBCS/actions/runs/42078163411)が正常終了した。対象はarm64-v8aの `libnative-lib.so`、解析IDは `5ed057380ac853a2`。取得・解析・検証・公開のステップは92分06秒。検出25,525件のうち内部25,233件の疑似コードを保存し、失敗0件、外部292件。代替設定で抽出した3件は確度low。資料は26,145ページ、ページ合計83,806,897バイト。[関数資料](https://github.com/sinsuirakv0/KBCS/tree/main/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/5ed057380ac853a2)と[チェックポイントのRelease](https://github.com/sinsuirakv0/KBCS/releases/tag/native-analysis-15.7.2-arm64-v8a-5ed057380ac853a2)に保存済み。

次の対象はJP15.7.4 / versionCode 1507040。上流の版情報は [metadata/jp/current.json](https://github.com/sinsuirakv0/KBC-rakv0-assets/blob/main/metadata/jp/current.json) に移った。版別の[検証記録](https://github.com/sinsuirakv0/KBC-rakv0-assets/blob/main/metadata/jp/versions/1507040.proof.json)に記載されたPrivate Releaseの `source.tar` を用い、`research/inputs/jp-1507040.json` で原本とライブラリを固定する。base APKにはSOが存在せず、`config.arm64_v8a` のSplitにarm64-v8aの `libnative-lib.so` が存在することを実物で確認済み。

## 無料運用の境界

- Publicのsinsuirakv0/KBCS、main、標準 `ubuntu-24.04` に限定。ジョブのifと実行スクリプトの両方でPublicを確認する。forkやPrivateでの実行は停止する。
- runnerラベルを入力から指定できない。大型runner・自動的な有料環境への切替・AI API・有料ストレージ・Git LFSを使用しない。
- Actionsのupload-artifact、actions/cache、Packages、カスタムイメージを使用しない。途中成果は通常のGitHub Releaseへ保存する。アプリ配布のlatestは切り替えず、`native-analysis-*` のprereleaseにする。
- 条件を満たさない、空きRAM/ディスクが足りない、GitHub制限に達した場合は停止する。課金による継続は行わない。

現行の[公式料金条件](https://docs.github.com/en/billing/concepts/product-billing/github-actions)ではPublicの標準runnerは無料で、大型runnerはPublicでも課金対象。Artifacts/キャッシュ等には別の保存条件があるため本workflowでは利用しない。[通常Releaseの公式条件](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)は1ファイル2GiB未満・1Release最大1000アセットであり、総サイズと帯域の上限はない。
将来のGitHub料金改定や、この解析以外の既存workflow・他repoの課金までをコードから保証する意味ではない。アカウント側でも有料利用停止の予算設定を確認する。既存アプリCIのArtifacts等をこの変更で削除・変更しない。

## Secretと公開内容

KBCSのActions Secret `BATTLECATS_APK_READ_TOKEN` は設定済み。Private `sinsuirakv0/battlecats-apk` のみ、ContentsとMetadataのreadに限定した無期限の専用トークンを使う。取得元workflowの実行権限は不要。トークン自体をチャット・設定ファイル・ログへ書かない。KBCSへの保存は自動提供のGITHUB_TOKENを使う。

旧台帳（schemaVersion 1）は統合APKのアーカイブdigest・APK SHA-256・manifestのpackage/版・SO SHA-256を検証する。新台帳（schemaVersion 2）はアーカイブとbase/ABI Splitをそれぞれハッシュ照合し、baseのpackage/版とABI Splitのpackage/versionCode/split名を確認する。ABI Splitから取り出したSOはELF種別とSHA-256を確認する。署名は上流の検証記録に基づき、各原本のハッシュを照合する。

Publicへ保存できるのは、疑似コード、逆アセンブル、索引、SQLiteの関数/参照/metadata、計測・状態・テキストログ。APK・SO・Ghidraプロジェクト・project ZIP・環境変数・認証情報はcheckpointに入れない。原本とGhidraプロジェクトは実行機内だけで使用する。Private APK保存先へは書き込まない。

## 実行入力

workflowは `.github/workflows/native-analysis.yml`。

| 入力 | 既定値 | 意味 |
| --- | --- | --- |
| source_manifest | research/inputs/jp-1507021.json | リポジトリ内の検証済み入力台帳 |
| revision_label | ci-v1 | 同じ値で再開、変更すると別リビジョンを作成 |
| publish_reference | true | 完了した新リビジョンだけmainへ追記 |

`workflow_dispatch`と、認証された上流からの`repository_dispatch: native-analysis-request`を入口にする。後者のclient_payloadは同名のsource_manifest/revision_label/publish_referenceを使用し、publish_reference省略時はmainへ反映しない。上流での更新検知・通知設定と、無人での定期再実行は今回追加しない。自動解析の安定性を確認してから接続する。

同じ入力でも、ツール・スクリプト・JDK・メモリ設定・ラベルが変わると別の解析IDになる。台帳の誤りや未知の版を名前から補完して実行しない。

15.7.4を解析するときは `source_manifest=research/inputs/jp-1507040.json` を指定する。公開済みの15.7.2は別リビジョンで保持する。ローカルで原本の検証とSO抽出だけをする場合は `python -m indexer.apk --manifest research/inputs/jp-1507040.json --apktool <apktool.jar> --java <java>` を使う（`PYTHONPATH=research`）。自動紐づけの前に両版の資料を参照し、共通化に使う根拠を調べる。

## 処理と再開

1. Public条件とSecret・台帳を確認し、最小テストを実行する。
2. 配布物のハッシュを確認する。Ghidraは一時領域に展開し、起動に必要なJARを確認してから配置する。
3. 計画から16桁の解析IDを作る。同じIDの最新3組までを新しい順に確認する。Releaseのdigest・アーカイブと各ファイルのSHA-256・展開先を照合し、検証が完了した一式を作業領域へ移す。保存済みの組がすべて不正なら停止する。
4. 未完了ならPrivate Releaseから対象APKを取得・検証する。Ghidraの独立プロジェクトを新規作成し、自動解析と全件索引を作る。
5. 1000関数以下を1バッチとして逐次デコンパイルする。プロセス中断時も、書き終えた関数があれば同期・保存して残りへ進む。進捗0の場合は時間に余裕があれば1回だけ再起動する。保存時はGitHub側のsize/digestも照合する。
6. 標準→conservative→minimalの有限3設定で未保存分を処理する。過去に同じ設定で処理した失敗関数を自動反復しない。
7. 未処理0を確認して最終checkpointを保存し、Git閲覧用の資料を生成する。失敗関数は理由と逆アセンブルを残し、成功件数へ加算しない。
8. publish_reference=trueなら、最新mainの独立worktreeへ新規リビジョンだけ追加してpushする。非fast-forwardや権限エラーでは停止し、解析成果はReleaseに残る。

checkpointにはGhidraプロジェクトを含めない。そのため未完了の再開時は元APKからプロジェクトを再解析する。以前と新しい索引を、実行パスや所要時間を除いた構造ハッシュで照合し、一致した場合だけ保存済み疑似コードを再利用する。不一致時は停止し、別ラベルで新規生成する。完了checkpointからの再開では、同じ解析IDの資料生成・反映から再試行できる。Actionsの結果と `ci-status.json` の `complete` で、関数処理と資料公開の状態を区別する。

ジョブは340分で上限、解析1プロセスは60分で保護、1関数900秒、スクリプトは約20分ごとの関数境界で終了する。関数実行分の超過はあり得る。実行開始から210分を超えた時点で次のバッチを控え、未完了なら再開が必要と表示して失敗終了する。[GitHub管理runnerの1ジョブ上限は6時間](https://docs.github.com/en/actions/reference/limits)。中止時は最後にアップロード・検証できたcheckpointまで戻る。再開は同じ入力・ラベル・ツールで行う。強制終了時は進行中のバッチを再処理する場合がある。

一時的な通信エラーは取得・公開とも最大3回の試行に抑える。認証エラーや原本ハッシュの不一致では停止する。アップロード応答が失われた場合はRelease側のsize/digestを照合し、完了済みならそのまま進む。片方しか届かなかった場合は別名で再送し、既存アセットを上書きしない。

JVMヒープ1GiB、native RSS上限は `min(8GiB, 実行機RAM−3GiB)`。実行機RAMが6GiB未満なら停止する。Linuxは2秒ごとに自分のJVM直下のdecompileだけを監視し、上限超過または空きRAMが768MiB未満ならその子だけを停止する。RSSはWindowsのPrivate Bytesと異なる指標で、観測間隔に伴う一時的な超過もある。初回実測を基に設定を調整する。

## 成果物と従来資料の保全

実行機内: `research/.local/cache/<版>/<ABI>/<SO SHA>-ci-<解析ID>/`。
Gitへ追記する資料: `research/reference/<版>/<ABI>/<SO SHA>/<解析ID>/`。
Release: `native-analysis-<版>-<ABI>-<解析ID>`。checkpointアーカイブと全ファイルのSHA-256一覧をバッチ単位で追記する。以前のcheckpointを上書き・削除しない。

旧来の `research/reference/<版>/<ABI>/<SO SHA>/` 配下の資料を移動・削除・置換しない。新旧双方を入口から選べる。ローカルの既定参照先や既存Ghidraプロジェクトも変更しない。新資料は機械抽出結果であり、意味・型・名前は未確認。追加設定で復旧したものはlowとして表示する。

資料だけのmain更新でアプリの版が上がらないよう、アプリbuildのpush/pull_requestに `research/reference/**` のpaths-ignoreを追加する。手動のアプリビルドや、解析ツール自体の変更時の従来ビルドは維持する。

## 関数の関係と検証

- `ci.setup`：ハッシュ固定の公式配布物だけを準備する。
- `ci.load_input/plan`：台帳の境界検証、無料条件、解析ID・メモリ設定の作成。
- `ci.run`：取得→索引→バッチ→資料生成を調整する。`run.headless`と既存ExportCacheを共用する。
- `ci.allowed/restore/checkpoint`：配布可能なファイルを限定し、パス・サイズ・各ハッシュ・GitHubのdigestを検証する。
- `network.retry/download_asset`：一時的なエラーの判定と、APK・解析配布物の取得の再試行を共用する。
- `ci.decompile_batch`：途中で止まった処理のジャーナルを同期し、再開する関数を選ぶ。
- `ci.index_digest/select_functions`：再解析時の一致確認と、処理済み試行の再実行防止。
- `memory.linux_memory`：Linuxの所有子プロセスだけをRSS/空きRAMで保護する。
- `ci.publish_reference`：アプリ作業とは別のworktreeで、新規リビジョンだけをmainへ追加する。
- `reference.export_cache`：解析IDがある場合だけ版/ABI/SHAの下へ追加階層を作る。従来の出力形式も維持する。

最初のジョブはsetup-javaの版解決で停止した。配布元の正確な `21.0.11+10.0.LTS` 表記へ直した後、上記の実ジョブで起動から公開まで確認した。復旧処理はローカルテストで、壊れた保存からの切替、通信失敗後のアセット照合、ジャーナルの部分保存、進捗0での停止を検証する。復旧処理を加えた後の実環境での通し運転は別途確認する。
