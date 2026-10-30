# 自動採番・OS別公開（2026-10-30）

## 呼出しと責務

`build.yml` のprepareが版とソースSHAを確定する。UI回帰チェックはprepareと並列。公開用Python試験はprepareで、PR等ではchecksで実行し、共通試験をOSごとに繰り返さない。prepareは版・lock・README・説明だけを変更するため、UIチェックは開始SHA、各OSのビルドと公開はprepare.outputs.commitを使う。

`build`はmatrixから`build-platform.yml`を呼ぶ。Windows、Apple Silicon、Intelごとにbuild → publishが独立し、他OSの成功・終了を待たない。fail-fast=falseで一つの失敗から他OSを中断しない。各buildはread権限、公開jobだけがwrite権限を使う。呼出し元は再利用workflowへwriteを渡すが、fork PRのtokenはGitHubによりreadへ制限され、PRの公開条件もfalseになる。

採番はprepare-release.pyのselect_version。X.Y.Zの数値順でkbcs-vタグだけを比較する。入力なしでCargoが最新タグと同じ版ならpatch+1、未公開の予約版なら維持。明示版はCargo以上・既存タグより新しい版だけを許可する。workspace memberのCargo.lockだけを書き換える。README・日本語の説明はUTF-8 BOM。説明の自動生成は存在しない場合のみで、全OS成功という未確認の記述や、まだ存在しない配布物へのリンクを作らない。

prepareは開始SHAとremote mainを比較し、github-actions[bot]のコミットをfast-forwardでpushする。同じ開始SHAを親に持つKBCS-Release-Sourceトレーラー付きbotコミットは再実行で再利用する。それ以上mainが進んでいれば古い実行を止める。元イベントのGITHUB_SHAと採番コミットは異なるため、package.pyのgit HEADと公開jobのKBCS_RELEASE_COMMITを一致させる。タグ指定では採番せずCargoとの一致を確認する。PR・他ブランチ・forkは公開しない。

GITHUB_TOKENのpushは新たなpush workflowを起動しないため、同じrunで採番・ビルド・公開を完了する。[GitHubのイベント規則](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow#triggering-a-workflow-from-a-workflow)。

## ビルド時間と失敗対策

Rust 1.98.1、LLVM-MinGW 20260922、macOS 14.0 deployment targetを維持する。workspaceのreleaseテスト → 全ターゲットのrelease clippy → releaseビルド → 単独起動検査を行う。先にテスト依存をコード生成し、clippyでもその成果物を再利用する。型エラーのためだけの別プロファイルや重複したcargo checkは追加しない。C++のcc parallel機能はCargoのjobserverに従い、同じ最適化・浮動小数点・整数フラグのまま翻訳単位を並列にコンパイルする。配布物のthin LTOを省略して速くする変更はしていない。[ccの仕様](https://docs.rs/cc/latest/cc/#parallel)。

Cargo registry/git/targetをOS・CPU・Rust/LLVM・lock・ソースSHA・run_attemptでキャッシュする。過去の同OS/CPUキャッシュも復元し、Cargoが必要な差分を再構築する。restore/saveを分け、コンパイル失敗後にも有効な途中成果物を保存する。キャンセル時は保存しない。run_attemptを含め、失敗した同じrunの再実行でも新しいキャッシュを保存できる。キー世代をv2へ変更した最初の実行はコールドビルドになる。Cargo --timingsのHTMLを7日保存し、以降の時間改善を実測できるようにする。インストーラは14日保存。

## 部分公開と再実行

publish-release.pyはKBCS_RELEASE_PLATFORMの一環境を必須とし、ZIP・JSON・checksumの三点を検査する。版・commit・CPU target・archive名・SHA-256をpackage_filesで照合する。既存タグは注釈付きもcommitまで辿り、異なるソースなら移動させず停止する。

公開jobは共通のconcurrency groupで短い公開処理だけを直列化する。`queue: max`で三環境の待機jobを保持し、既定の「待機一件を後着jobで置換」による公開取り消しを防ぐ。[GitHub公式のqueue仕様](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency)。actionlint 1.7.12はこのキーが未対応のため、そのキーに対する診断だけを除外して検証する。残りの構文・式・再利用workflowの入力は同ツールで確認する。

最初の成功OSがドラフトを作る。JSON・checksumを先にアップロードしてGitHub側のsize/digestも検査し、最後にZIPを置く。三点のsize/digestが一致してから公開開発版へ切り替える。以降のOSは同じタグ/ソースの公開版へ追加する。ZIPが完成している環境の既存三点は上書きしない。同じ成果物の再実行はアップロードを省く。

まだZIPがない環境の途中の付属情報だけは再送可能。中断されたstate=starterの同環境ZIPは削除して再試行する。公開済み版への新ZIPの検査失敗時は、その未検証ZIPだけを除き、先に成功した環境を保持する。ドラフトの失敗は非公開を維持し再実行で回復する。公開後のソース修正は別の版でビルドし、既存タグを付け替えない。

アプリのlatest_app_forは自分のOS/CPUに対応する、正のsizeと有効なSHA-256を持つZIPがある公開版だけを数値版で比較する。Windowsのみ0.1.38が成功すればWindowsへ案内し、Macは0.1.37を選ぶ。後からMacのZIPが追加されると、次の起動時/手動の更新確認で同じ0.1.38を案内する。新しい配布フォーマットの導入はなく、旧アプリも元からOS別ZIPで選択する。

## 原因と検証範囲

[run 41013298009](https://github.com/sinsuirakv0/KBCS/actions/runs/41013298009)はWindows成功・Mac両CPU失敗。Darwin libc 0.2.191のstatvfsはfsblkcnt_tがu32、f_frsizeがu64であり、storage::spaceのsaturating_mulが型不一致だった。ブロック数をu64へ広げてから乗算する。フレーム計算・ゲーム仕様の変更ではない。

最小回帰試験はローカルbare Gitで採番/同じrun再利用/古いmainの拒否、GitHub模擬応答で一環境だけの公開・後続OS追加・同一成果物再実行・別ソース/CPU/不足物拒否・配布済み成果物の不変性・付属情報破損・中断・失敗時の他OS保持を確認する。外部GitHubへ書き込んで試験しない。Rustは部分公開時のOS別選択・Mac ZIP追加・ドラフト/不正SHA除外を確認する。

ローカルWindowsではstorage.rsとappのruntime.rsそのものを隔離crateへ参照し、Apple Silicon/Intelの実ターゲットと同じlibc/mach2を使ってclippyの型チェックを通した。Macアプリ全体のリンク・WKWebView起動はMac runner上のテスト/単独起動検査で確認する。WindowsでMacの実機動作を確認したとは扱わない。
