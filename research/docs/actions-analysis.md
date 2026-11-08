# GitHub Actions自動解析 v1

## 対象と現在の状態

最初の対象はJP15.7.2 / versionCode 1507021 / arm64-v8a / libnative-lib.so。入力の版・APK/アーカイブ/SO SHA-256は `research/inputs/jp-1507021.json` に固定する。2026-10-20に確認した原本の再生成であり、最新版の版番号を推測しない。上流の取得workflowは起動・変更しない。

Python 3.13、Ghidra 12.1.2、Temurin JDK 21.0.11+10、apktool 2.12.1を使用する。Ghidra/apktoolの公式配布URLとSHA-256は `research/ghidra/runtime.json`。解析・抽出・資料生成はPython/Javaで実行し、AI APIは使わない。関数の由来と構造差は [追跡v2](../matcher/docs/tracking-v2.md) で作成する。

2026-11-06に15.7.2の[GitHub Actions実行](https://github.com/sinsuirakv0/KBCS/actions/runs/42078163411)が正常終了した。対象はarm64-v8aの `libnative-lib.so`、解析IDは `5ed057380ac853a2`。取得・解析・検証・公開は92分06秒。検出25,525件のうち内部25,233件の疑似コードを保存し、失敗0件、外部292件。代替設定で抽出した3件は確度low。[チェックポイントのRelease](https://github.com/sinsuirakv0/KBCS/releases/tag/native-analysis-15.7.2-arm64-v8a-5ed057380ac853a2)

JP15.7.4 / versionCode 1507040の[GitHub Actions実行](https://github.com/sinsuirakv0/KBCS/actions/runs/42211867789)も2026-11-06に正常終了した。解析IDは `6cf79e30b2bdfc73`。取得・解析・検証・公開は73分06秒。検出25,525件、内部疑似コード25,233件、失敗0件、外部292件、確度lowは2件。[チェックポイントのRelease](https://github.com/sinsuirakv0/KBCS/releases/tag/native-analysis-15.7.4-arm64-v8a-6cf79e30b2bdfc73)

15.7.4は上流の版別検証記録に載るPrivate Releaseの `source.tar` を使い、`research/inputs/jp-1507040.json` で原本とライブラリを固定する。base APKにはSOがなく、`config.arm64_v8a` のSplitに対象が入っている。[版情報](https://github.com/sinsuirakv0/KBC-rakv0-assets/blob/main/metadata/jp/current.json)・[版別検証記録](https://github.com/sinsuirakv0/KBC-rakv0-assets/blob/main/metadata/jp/versions/1507040.proof.json)

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

Publicへ保存する対象は、疑似コード、逆アセンブル、索引、CFG・raw P-code、SQLiteの関数・参照・追跡情報、計測・状態・テキストログ。APK、SO、Ghidraプロジェクト、認証情報は実行機内で扱う。

## 実行入力

workflowは `.github/workflows/native-analysis.yml`。

| 入力 | 既定値 | 意味 |
| --- | --- | --- |
| source_manifest | 空 | assetsの検証済み最新版。旧版を指定する場合は `research/inputs` 内の固定台帳 |
| assets_commit | 空 | assetsの公開通知に含まれるコミットSHA。新しいJPデータセットに置き換わった通知は処理を終える |
| checkpoint | 空 | 処理済みの `native-analysis-*` Releaseタグ。指定時は保存済み解析から開始 |
| stage | all | `analyze` は解析のみ、`references` と `match` は完成checkpointからその段階だけを実行 |
| check_only | false | 台帳と公開状態だけを確認。解析、Release書込、Git公開を行わない |
| revision_label | ci-v1 | 同じ値で再開、変更すると別リビジョンを作成 |
| publish_reference | true | 完成した資料でmain上の同じゲーム版・ABIを更新 |

上流のPlay更新検知・APK取得・展開・検証が完了し、`metadata/jp/current.json` がassetsのmainへ公開された版を対象にする。assetsの `notify-native-analysis.yml` がコミットSHA付きでKBCSを起動し、受付応答で終了する。既存のZIP配布と通知は独立。即時起動にはassets側の `KBCS_ACTIONS_TOKEN` が必要で、権限はKBCSへの `Actions: write` に限定する。[GitHubのworkflow dispatch権限](https://docs.github.com/en/rest/actions/workflows#create-a-workflow-dispatch-event)

KBCSのmainでも毎時23分にassetsを確認し、通知の未着や失敗を拾う。`current.json` と版別 `proof.json` は同じコミットから読む。全段階が済んだ原本はスキップし、資料公開済みで照合待ちの原本は `match` ジョブだけを再開する。GitHubの定期実行には遅延があり、定期実行は起動時点のcurrentを処理する。[GitHub Actionsのschedule仕様](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)

新規版では保全済みのPrivate Releaseを取得し、アーカイブ、署名検証記録、base/ABI SplitのSHA-256、実APKのmanifestを照合する。検証済みABI Splitから抽出したSOのSHA-256を解析計画に固定する。同じ版でも原本アーカイブが変われば新規入力として扱う。v1の結果しか存在しない場合や、直前2版の構成・リビジョンが変わった場合は、公開済みcheckpointから追跡を実行する。

手動確認は `workflow_dispatch` の `check_only=true`、最新版をすぐ確認・処理するには入力台帳を空にして通常起動する。`repository_dispatch: native-analysis-request` は従来どおり同名のclient_payloadを受け取り、`publish_reference` 省略時はmainへ反映しない。定期実行では完成資料をmainへ公開する。解析中のジョブは後着の定期実行で中断しない。GitHubの同時実行制御で待機中のジョブが置き換わった場合は手動で再起動できる。

同じ入力でも、ツール・スクリプト・JDK・メモリ設定・ラベルが変わると別の解析IDになる。台帳の誤りや未知の版を名前から補完して実行しない。

15.7.4を指定して再解析するときは `source_manifest=research/inputs/jp-1507040.json` を使う。公開済みの15.7.2は別リビジョンで保持する。ローカルで原本の検証とSO抽出だけをする場合は `python -m indexer.apk --manifest research/inputs/jp-1507040.json --apktool <apktool.jar> --java <java>` を使う（`PYTHONPATH=research`）。

初回の追跡対象は15.7.2・15.7.3・15.7.4。15.7.3の取得元は `research/inputs/jp-1507030.json` に固定した。

## 処理と再開

1. Public条件と台帳を確認する。解析する場合だけSecretを利用し、テストとセットアップへ進む。
2. 配布物のハッシュを確認する。Ghidraは一時領域に展開し、起動に必要なJARを確認してから配置する。
3. 計画から16桁の解析IDを作る。同じIDの最新3組までを新しい順に確認する。Releaseのdigest・アーカイブと各ファイルのSHA-256・展開先を照合し、検証が完了した一式を作業領域へ移す。保存済みの組がすべて不正なら停止する。
4. 未完了ならPrivate Releaseから対象APKを取得・検証する。Ghidraの独立プロジェクトで自動解析と全件索引を作り、同じプロジェクトを読み取り専用で開いて構造・raw P-codeのsidecarを保存する。
5. 1000関数以下を1バッチとして逐次デコンパイルする。プロセス中断時も、書き終えた関数があれば同期・保存して残りへ進む。進捗0の場合は時間に余裕があれば1回だけ再起動する。保存時はGitHub側のsize/digestも照合する。
6. 標準→conservative→minimalの有限3設定で未保存分を処理する。過去に同じ設定で処理した失敗関数を自動反復しない。
7. `analyze` は未処理0を確認して最終checkpointを保存し、Releaseタグを後続へ渡す。失敗関数は理由と逆アセンブルを残し、成功件数へ加算しない。
8. `references` はそのcheckpointから資料を生成する。`publish_reference=true` ならmainの同じゲーム版・ABIを差し替え、manifestに `comparison_state=pending` を記録する。
9. `match` は対象と同じABIの直前2公開版を復元する。構造sidecarがない旧版だけ隔離プロジェクトでバックフィルする。連続比較と直接検証を集約し、SQLiteを解析Releaseに保存してsizeとSHA-256を照合する。全リンクの検査後、`research/comparisons/` の公開、版目次への導線、旧比較資料の廃止を同一コミットで行う。比較元がなければ `no_baseline`、追跡公開後は `complete` を版のmanifestに記録する。

15.7.2・15.7.3・15.7.4の既存資料から初回追跡を実行する場合は、`checkpoint=native-analysis-15.7.4-arm64-v8a-6cf79e30b2bdfc73`、`stage=match`、`publish_reference=true` を指定する。資料生成だけなら `stage=references` を使う。追跡を再実行すると、検証済み構造sidecarと、同じ入力・エンジン・手動判断で完成した追跡SQLiteを再利用する。上流currentが進んだ後に旧版の未完了解析を再開する場合は、checkpointの `ci-plan.json` に記録された `input` を固定台帳として指定する。

checkpointにはGhidraプロジェクトを含めない。そのため未完了の再開時は元APKからプロジェクトを再解析する。以前と新しい索引を、実行パスや所要時間を除いた構造ハッシュで照合し、一致した場合だけ保存済み疑似コードを再利用する。不一致時は停止し、別ラベルで新規生成する。完了checkpointからの再開では、同じ解析IDの資料生成・反映から再試行できる。Actionsの結果と `ci-status.json` の `complete` で、関数処理と資料公開の状態を区別する。

ジョブ上限は解析235分、資料作成30分、追跡90分で、合計355分。ジョブ待機時間は別途発生する。解析プロセスは60分、1関数は900秒。開始から210分を超えると次のバッチを控え、未完了の場合は再開を促す。中断時は最後に照合済みのcheckpointから、同じ入力・ラベル・ツールで再開する。追跡でバックフィルの時間が不足した場合も、先に保存した版のsidecarを再利用できる。[GitHub管理runnerの上限](https://docs.github.com/en/actions/reference/limits)

一時的な通信エラーは取得・公開とも最大3回の試行に抑える。認証エラーや原本ハッシュの不一致では停止する。アップロード応答が失われた場合はRelease側のsize/digestを照合し、完了済みならそのまま進む。片方しか届かなかった場合は別名で再送し、既存アセットを上書きしない。

JVMヒープ1GiB、native RSS上限は `min(8GiB, 実行機RAM−3GiB)`。実行機RAMが6GiB未満なら停止する。Linuxは2秒ごとに自分のJVM直下のdecompileだけを監視し、上限超過または空きRAMが768MiB未満ならその子だけを停止する。RSSはWindowsのPrivate Bytesと異なる指標で、観測間隔に伴う一時的な超過もある。初回実測を基に設定を調整する。

## 成果物と従来資料の保全

実行機内: `research/.local/cache/<版>/<ABI>/<SO SHA>-ci-<解析ID>/`。
Gitで閲覧する資料: `research/reference/<版>/<ABI>/<SO SHA>/`。1関数につきMarkdown 1ファイル。解析IDは `manifest.json` に記録する。
Release: `native-analysis-<版>-<ABI>-<解析ID>`。checkpointアーカイブと全ファイルのSHA-256一覧をバッチ単位で追記する。以前のcheckpointを上書き・削除しない。

同じ版・ABIの公開ツリーには今回のSO SHAの資料一式を置く。同一checkpointから資料を再生成する場合は追跡資料への導線を引き継ぐ。過去の追跡ウィンドウから関数資料へのリンクは公開時のGitコミットに固定する。過去のGitコミット、解析Releaseのcheckpoint、ローカルのGhidraプロジェクトを保全する。

資料だけのmain更新でアプリの版が上がらないよう、アプリbuildのpush/pull_requestに `research/reference/**` のpaths-ignoreを追加する。手動のアプリビルドや、解析ツール自体の変更時の従来ビルドは維持する。

## 関数の関係と検証

- `ci.setup`：ハッシュ固定の公式配布物だけを準備する。
- `upstream.snapshot/source_input/matching_publication`：assetsの同一コミットの検証記録から入力を作り、公開済みのAPK原本を照合して重複解析を省く。
- `ci.load_input/plan`：台帳の境界検証、無料条件、解析ID・メモリ設定の作成。
- `ci.analyze`：取得→索引→バッチ→完成checkpointを調整する。`run.headless`と既存ExportCacheを共用する。
- `ci.allowed/restore/checkpoint`：配布可能なファイルを限定し、パス・サイズ・各ハッシュ・GitHubのdigestを検証する。
- `network.retry/download_asset`：一時的なエラーの判定と、APK・解析配布物の取得の再試行を共用する。
- `ci.decompile_batch`：途中で止まった処理のジャーナルを同期し、再開する関数を選ぶ。
- `ci.index_digest/select_functions`：再解析時の一致確認と、処理済み試行の再実行防止。
- `memory.linux_memory`：Linuxの所有子プロセスだけをRSS/空きRAMで保護する。
- `ci_delivery.restore_completed/publish_materials/publish_comparison`：完成checkpointの版・ABI・解析ID・SOを確認し、資料と比較を独立して公開する。
- `ci_structure.structure_checkpoint`：Ghidra構造エクスポートを解析Releaseの個別アセットに保存する。
- `ci_tracking.publish_tracking`：復元、追跡DBの再利用、Markdown生成、旧資料の移行を管理する。
- `reference.export_cache`：完成済みキャッシュから版・ABI・SO SHA配下へ1関数1ファイルで書き出す。
- `reference.replace_reference`：新しい一式を準備してから対象を切り替え、入口を更新する。

最初のジョブはsetup-javaの版解決で停止した。配布元の正確な `21.0.11+10.0.LTS` 表記へ直し、上記の実ジョブで起動から公開まで確認した。復旧処理はローカルテストで、壊れた保存からの切替、通信失敗後のアセット照合、ジャーナルの部分保存、進捗0での停止を検証する。公開形式の変更は両版の完了チェックポイントからの再生成で検証する。

2026-11-07の接続検証では、公開assetsの15.7.4からPrivate Releaseのdigestを照合し、実APKから既知のARM64 SOを抽出した。公開済み版のスキップと15.7.2の完成checkpointの復元を確認した。比較資料の生成とSQLiteの送信後照合は、両索引のSHA-256に一致する保存済みの照合結果を使い、送信先をローカルで模擬して確認した。構文検査と20件のテストを実行した。

3段階への分離後は、両版の実checkpointと保存済み照合結果を使って、資料公開、照合失敗時の `pending` 維持、照合だけの再実行、SQLite配布と `complete` 更新をローカルで確認した。GitHubへの送信は模擬した。

v2の検査範囲、結果の読み方、独立したARM64 ELFの試験は [追跡v2](../matcher/docs/tracking-v2.md) を参照。
