# データ・本体の更新（2026-10-29）

GUI/preview起動→Service::start_updates→updates::Manager::check。CLIのService::newだけではネットワーク処理を始めない。データと本体の確認エラーは独立させる。公式DBが開けない初回はデータの自動取得を始める。既存DBはversion_codeとrelease_tag/release_publishedを比較する。ホームの再確認でも同じ状態を使う。

UIは全ページのmain.js→updates.jsが初回通知を管理する。startup claimはプロセス内で1回だけで、ページ再読み込みごとに確認し直さない。「いいえ」は自動取得をせず、ホームのデータ管理から実行できる案内を出す。初回取得は進捗、バックグラウンド継続、失敗時の再試行案内を表示する。home.jsは同じ状態を購読する。

API: GET /api/updates（確認/進捗/導入済み版）、POST /check、/startup、/download {kind:data|app}、/apply。先頭はすべて/api/updates。旧/api/importの標準GitHub URLも統合リリースへ接続し、明示したローカルGit原本の手動取り込みを維持する。処理はバックグラウンド。DB snapshotを切り替え、snapshot名を含む既存キャッシュキーを利用する。

本体はKBCSリポジトリの`kbcs-v<SemVer>`だけを比較し、公開済み開発版を含む。`native-v15.7.2`等をアプリ最新版として扱わない。対象はOS/CPUに応じた`KBCS-<version>-windows-x64.zip`・`-macos-arm64.zip`・`-macos-x64.zip`。当該CPU向けZIPのある公開版を比較する。Source ZIPを実行ファイルとして使わない。GitHubのsize/SHA-256と、展開したkbcs.exeのPEヘッダーを確認する。

ダウンロードは`<data-dir>/updates/<tag>/`へ展開し、適用用ファイル一覧と各SHAを保存する。「再起動して更新」はGUI内だけで利用可能。Manager::apply→展開済み新kbcs.exeのapply-update CLI→親PID終了待機→ファイルSHA再検証→旧exe/DLLの退避→置換→元の起動先を再起動、の順。IPCは更新応答後の終了通知のみ。ブラウザpreviewではダウンロードまでとする。

置換失敗時は変更済み全ファイルを戻して元アプリを起動する。書込権限/他プロセスによる実行ファイル占有等はupdates/apply-error.txtへ記録し、次回ホームで表示する。所持品/編成を更新ZIPに含めず、元data-dir/regionを再起動へ引き継ぐ。GitHubへのpushやrelease作成はこの仕組みでは行わない。

最小試験はZIPのパス/量/SHA/OSロック、Gitなし統合取り込みと失敗時の旧DB維持、本体の複数ファイル置換の成功/途中失敗時の全復旧、JSの通知拒否/受諾/ホームからの取得/再起動要求。実行中のユーザー環境へ本体置換を行って試験しない。

apply-updateのCLI名とApplyPlanのsource/target/root/region/parentは、旧アプリが新アプリを起動するための互換契約。今後の本体更新でもこの入口を維持する。


## macOS（0.1.36）

Managerはupdates_macos::prepare/applyを使う。同じ配布アセット命名をCIのpackage.pyと共用する。ZIPのSHA/size・パス・展開量を検証し、Mach-OのCPU種別とcodesign --verify --deep --strictを確認する。抽出時にUnix実行権限を保存し、特殊権限は除去する。検証索引はKBCS.appの外に置き、署名を壊さない。

適用CLIは新しく展開したKBCS.appの実行ファイルから起動する。kill(pid,0)で元プロセスの終了を待ち、SHA再検証→インストール先と同じ親に一時.appを作成→署名再検証→旧版を退避→renameで交換する。交換失敗時は旧版を戻す。成功後に/usr/bin/open -n ... --argsで同じdata-dir/regionを引き継ぎ起動する。元アプリが読み取り専用の場所にある場合は更新を失敗させ、~/Applicationsへ移動する案内を保存する。親のアプリを強制終了しない。実行中本体やユーザーDBを書き換えて試す検証は行わない。

配布Mac版は既定で開発用ad-hoc署名。Developer ID署名/Apple公証とは区別する。build.mdに配布と初回OS確認の関係を記録する。


## OS別の部分公開（2026-10-30）

CIは各OSのbuildとpublishを独立実行する。先に成功した環境のZIPを公開し、後から成功した環境を同じソース/タグへ追加できる。公開処理はJSON/チェックサムのGitHub側検証を先に済ませ、ZIPを最後に置く。対応ZIPのないOSへ他CPUの版を案内しない。

releases::latest_app → latest_app_forは、ドラフト・本体以外のタグ・対象OS/CPUのZIPなし・size=0・不正/欠落SHAを除外してSemVer最大を選ぶ。Windowsのみ新版が成功した場合はWindowsへ新版、Macへ最後に成功した版を返す。Macの追加公開は次の起動/手動checkで検出する。実際のダウンロード時のsize/SHA/CPU/署名検査は従来通りで、更新ファイル形式とapply-update CLIを変えない。旧アプリにもOS/CPU別ZIPの選択は既にあるため、この公開方式を使うための先行更新を必須にしない。
