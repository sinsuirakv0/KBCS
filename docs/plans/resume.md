# 再開メモ（2026-10-29 / mainの自動採番・Release公開）

- ユーザーの「version指定なしなら自動で上げる」依頼により、mainのpushでprepare→三環境build→Release公開へ接続する。Cargoで既存タグより上げてあればその版、指定がなければpatch+1、手動Actionsのversion入力でも指定可能。PR/他ブランチ/forkはビルドのみ。
- 自動コミットでCargo/Cargo.lock/README/説明を揃え、そのSHAを全buildとpublishへ渡す。既存タグは移動せず、新規タグは三環境の成功後。GITHUB_TOKENのpushは別workflowを起動しないため、同じrunで完結する。設計はscripts/docs/release.mdとcrates/kbcs-app/docs/build.md。
- mainにはbotコミットが加わるので、次回作業前にローカル変更を保持しながらfast-forwardで同期する。公開途中で失敗した場合は同じrunの再実行を使い、公開済みの版を上書きしない。
- ローカル4テスト（GitHub書込なし）、actionlint 1.7.12、隔離した実workspaceの3crateの版/lock一致が通過。mainの次のpushで自動採番から公開まで確認する。

# 再開メモ（2026-10-29 / Intel Mac CIの通信試験）

- ユーザー指定run40862502160/job123408981211はIntelのcargo testで101。ネイティブ23件・アプリ6件とデータの他7件は成功。旧本文期限のRecvBodyは発火済みで、テストのpartial非空assertだけが失敗した。同runのWindows/Apple Siliconは成功。
- 中間受信量への不必要な仮定を外し、本文期限のエラー型・低速取得の完全性・通信再試行・上限/part削除・破損検出を維持する。取得実装やworkflowには変更しない。資料はcrates/kbcs-data/docs/releases.md。CI修正の依頼としてmainへpushし、自動実行のIntel jobを確認する。
- ローカルのkbcs-data releaseテスト11件と同crate/all-targetsのrelease clippy（-D warnings）が通過。

# 再開メモ（2026-10-29 / Apple Silicon初回ZIP取得のtimeout）

- 初回アセット取得で `timeout: receive body` との報告。releases.rsのtimeout_recv_body=120秒が、無通信時間ではなく本文全体の期限だった。固定依存ureq 3.4.2のconfig.rs/timings.rsを確認し、ローカルHTTPで継続受信中でも同じRecvBodyエラーになる条件を短縮再現した。ARM64固有とは確認していない。
- JSON/manifestは全体30秒、ZIPは試行ごとに全体1800秒、接続20秒/応答ヘッダー60秒。本文だけの120秒期限を削除。通信エラーとHTTP408/429/5xxは最大3試行、1秒→2秒待機。途中EOFも対象、ディスク失敗・超過サイズ・SHA不一致は再試行しない。原本/本体の両ZIPが同じdownload関数を使う。
- partは失敗時に削除し、そのZIPを先頭から取得し直す。中断位置再開は実装していない。install_dataのpending削除/既存DB保持と、ホームのデータ管理からの再試行は従来通り。資料はcrates/kbcs-data/docs/releases.md。
- kbcs-dataのreleaseテスト11件、workspace/all-targetsのrelease clippy（-D warnings）が通過。既存C++警告11件は変更していない。旧期限のRecvBody再現、低速受信成功、切断後の再取得、3回失敗の打切り/part削除、SHA不一致では再試行しないこと、既存DB維持を確認。
- ユーザーが修正のコミット/pushを明示依頼。mainへのpushで自動ビルドへ渡し、実行状況や完了の確認は行わず終了する。タグ/版番号/リリースは今回変更しない。Mac実機の通信確認は未実施。

# 編成・取り込み・停止中操作の修正（2026-10-29）

ユーザーの「完了したらコミットしてpush、以後の自動ビルド確認は不要」に基づきmainへ反映する。今回はタグ/リリース作成・版番号変更は行わず、pushによる3環境の自動ビルドへ渡す。実画面の確認はユーザー担当。

- 準備の価格を円からさらに100除算していた誤りと、通常編成で本能値引きを使わない表示経路を修正。両画面とも既存C++ deploy_costへ接続。img031の出陣ボタンは入れ子SVGへCSSが広がる切抜き不良を修正し、原本cut10/11の画像と配置を維持。
- ニムエ(ID89)、10式戦車(54)、ネコでありんした(45)、ネコチーター(673)等の未使用行を最大形態として選ばない。通常キャラは画像/攻撃モーションのある形態をcatalogへ出し、旧保存は実効形態へ解決する。アイコンのない精霊876は正規の例外として残す。
- 一時5枠から通常枠へ長押しドラッグで入れ替える。相手も一時枠へ移し、Lv/本能/玉を保持する。元の番号背景を残し、共通描画と既存浮遊曲線を使う。空きへのクリック移動も維持。
- 操作盤の停止中は即生産チートだけを0tick入力でC++ deployへ渡す。通常は出撃せず、チートでは同じFで個体生成・支払う。0.1/0.2/0.25/0.5/0.75倍の再生を追加。
- 統合原本のテキストを最大8並列・本文128MiB以内で準備し、取り込み中だけ検証済み内容を共有。モーション画像の二重保存、同じ原本の再取得、同一完成DB確認での全キャラCSV再走査を削減。画像の実要求時のSHA照合・開発用Git原本の変更検出は維持。schema8/importer13を変えず旧DBも利用できる。
- 資料用のモーション全文と戦闘用のパス索引を分け、開始時のJSON本文複製・各clipでのcut/model再読込を削減。
- ローカルRust39件＋compile_fail1、JS3本、clippyを通過。隔離データで全件変換112.549秒、再利用0.549秒、DB480,440,320→226,963,456bytes。原本/DB件数を維持し、通常戦闘30/60/90Fは旧版とstate/runtime/layout/scene（RNG込み）が一致。停止0tickの味方数は通常0、チート1→2。初回計測はZIP取得/展開を含まない。最初の計測は検証側の300秒制限で中断し、キャッシュ改善後に全件を完了した。

記録.local/fix-verification.json、.local/fix-api-verification.json。検証DBは.local/import-performance、原本は.local/integrated-dataを共有参照。ユーザーのAppData/既存GUIは操作していない。詳細はui/docs/formation.md、ui/docs/stage-sortie.md、crates/kbcs-data/docs/releases.md、native/kbcs-core/docs/battle-screen.md。

# 公開完了（2026-10-29 / KBCS 0.1.36）

公開URL: https://github.com/sinsuirakv0/KBCS/releases/tag/kbcs-v0.1.36 。タグは`0d6a50ec3779a0ba424f80f2a492cbc7d577a1ba`。Windows x64・Mac arm64・Mac x64の3ZIPと各SHA/ビルドJSONを公開した。READMEとリリース説明にはOS別の直接リンク、Source code ZIP、導入手順を置いた。MacはmacOS 14以上・開発用署名で、Developer ID/公証は未設定。

- main CI 40815206591は3環境すべて成功。タグCI 40816291677も3ビルドで計算/データ39件＋compile_fail1、JS3本、clippy、配布物の実WebView接続/単独起動/署名/CPUを通過。コードと戦闘をOS別に複製していない。
- タグCIの公開stepでdraftのRESTタグ取得が404となったため、gh release viewのapiUrlからIDで取得する経路へ修正した。同じタグのCI成果物を再ビルド・タグ上書きせず、修正したpublish-release.pyで版/commit/全SHA・GitHubのサイズ/配布SHAを再検証して公開。修正はmainにも反映する。今後のタグは修正済み公開処理を使う。
- 匿名HTTPで3ZIPとSource code ZIPが200となり、公開ZIPの全SHA・サイズ、Windowsの同梱5ファイル、MacのMach-O CPU・実行ビット・Info.plistを確認した。記録.local/release-0.1.36-verification.json。公開Windows ZIPの実行ファイルで隔離済みJP15.7.4原本を使い、画像検査とC++戦闘30/60/90Fの再生も通過（同JSON/battle.json）。ユーザーのAppData/既存GUIを操作していない。
- 詳細はcrates/kbcs-app/docs/build.md/updates.md、ui/docs/README.md、GitHubの各jobログ。実画面の見た目・操作感はユーザー確認。以降のsource pushは自動ビルド、kbcs-vVERSIONタグでは全3ビルド成功後に公開開発版を作る。

# 再開メモ（2026-10-29 / Windows・Mac両CPU・CI配布）

ユーザー依頼でmacOS Apple Silicon/IntelとWindows x64の共通GUIへ移行し、0.1.36へ更新。READMEの3種類の入手リンク・環境・導入手順と、docs/releases/0.1.36.mdも更新した。今回のGitHubへのソースpush・CI実行・リリース公開は「README.mdごと更新」「リリースも、ユーザーが簡単に取得できる形で」という明示依頼による。

- desktop::runはWindows/macOS共通のtao/wry→Service→Rust/C++。Macの既定データは~/Library/Application Support/KBCS、WKWebViewは保存先別のdata-store identifier（macOS 14以上）。ヘルプは固定URLだけをopenで起動。runtimeはDarwinのCPU/メモリAPIも取得する。戦闘処理をOSごとに分岐させない。
- releases::app_asset_nameが3種類のZIPを選び、最新判定も当該CPUのZIPがある版に限定する。ZIP展開はUnix実行権限を保持。Mac更新はMach-O CPU/署名/SHA検査→親終了待機→同じ親の一時.appへ検証コピー→旧版退避/rename交換/失敗復旧→openで同じdata-dir/regionを引き継ぐ。署名済み.app内部へ検証索引を置かない。
- build.ymlはpush/PR/manualで3CPUのlocked releaseテスト・clippy・JS回帰・実WebView接続検査・ZIP作成を行う。タグkbcs-vVERSIONでは全ビルド成功後にpublish-release.pyが版/commit/SHAとGitHub側の配布SHAを確認し、ドラフトから公開開発版にする。公開済み版は上書きしない。Source codeはGitHubのタグarchiveを使う。
- package.pyはWindowsのDLL一式、MacのKBCS.app/Info.plistと署名を作る。Macは既定ad-hoc署名で、Developer ID/公証は未設定。初回のOS確認手順はREADMEへ記載。
- desktop-checkは非表示でES module/通信ID/PNG/POST本文/C++/WebGLを確認し、ゲームデータの取得・既存AppDataへの書込・画面操作をしない。WKWebView向けUUID生成はgetRandomValuesを共用し、ゲーム内RNGは変更しない。
- ローカルWindowsのworkspace39＋compile_fail1、JS3本、clippy、配布物help、実WebView接続検査を通過。Windowsの確認ZIPは.local/dist/0.1.36-local。C++の既存警告11件は残る。3環境の最終ログと配布SHAはGitHub Actionsの実行、およびkbcs-v0.1.36の配布JSON/SHAを参照する。設計はcrates/kbcs-app/docs/build.mdとupdates.md。

# 再開メモ（2026-10-29 / 統合リリース・データ/本体更新）

確認用 `.local/dist/0.1.35-updates/kbcs.exe`、SHA256 `2420462f1279f5bf87c992e6549fc776af971b5d36ee787c509ce7fed16569e6`。DLL/verification.jsonを同梱。確認用previewは4854、データは隔離した`.local/integrated-data`。GUI確認はユーザー担当。既存AppData/既存previewの編成や持ち物は変更していない。GitHub書込なし。前回までの未コミット変更を保持する。

- assets最新公開`integrated-jp-1507040-3-1` / 15.7.4 / commit40bc155ebbc2b096a4a2123028e08cdb075b5383の全10ZIP、830,048,026 bytesを取得・SHA検証し、54,338ファイル（909,580,871 bytes）へ展開した。キャラ882 / 2,618形態、ステージ1,298マップ / 6,476面。ID736は説明3行・能力2行であるため実在する能力行までを採用。Web補完の別称/海外版補完は原本ZIPに含まれず旧生成物から混ぜない。
- releases.rsがGitHub read-only確認・全ZIPストリーム受信・SHA/展開量/パス検証・採用元索引・原本フォルダ公開を共用。Sourceはrelease.jsonのある直下Data/res/Image等をGitなしで読める。公式schema8/importer13、ユーザーDB分離を維持。原本の管理パスはdata-dirからも解決し、移動前originへ固定しない。download.lock/update.lockはOS排他へ変更し、ファイル残存だけで更新不能にならない。
- ManagerはGUI/preview起動時に公開版を非同期確認。DB/原本なしは自動取得、導入済みは版/公開日時で確認してUIの選択へ。拒否はホームのデータ管理へ案内。CLI importの標準取得元も新リリースへ接続。ローカルGit原本は引き続き明示指定可能。本体はkbcs-v SemVerのみ（公開開発版を含みnative-vを除外）、Windows x64 ZIPを検証して展開し、再起動時に親終了待機→SHA再検証→置換/失敗復旧。現実行ファイルの本体更新試験は行わず、置換/復旧を隔離fixtureで検証。
- 15.7.2固定で新DBを拒否していた本能玉・計算・戦闘入口も接続。枠数は原本equipmentslot.csvをカタログ/編成保存/戦闘で共用。calculationVersionはsettings-catalog全27採用元SHAが一致するときだけ返す。戦闘入力4件と全効果時計、UI27参照のSHAも照合。ネイティブロジック自体は15.7.2参照のままで、15.7.4の全関数同一を意味しない。旧編成は一括変更せず現在DBへ出撃用に解決し、編集保存時にgameVersionを更新。
- 原本音声はassets→musicの順で採用し、APKのCAFを圧縮版へ置換しない。CAFは既存の無再量子化WAV変換を共用。画像/BGMは固定されたローカル原本へ接続する。
- workspace38＋compile_fail1、追加ストリーム取得1、clippy全target -D warnings、JS回帰が通過。実DBの初回自動再導入/最新判定、カタログ6経路、原本画像2件、音源8件、同梱UI11ファイルのbytes一致を確認。最終exeで15.7.4データを使い所有C++戦闘30/60/90F＋画像API検証を通過。記録は.local/update-*.json/log。ソース/仕様はcrates/kbcs-data/docs/releases.mdとcrates/kbcs-app/docs/updates.md。

# 再開メモ（2026-10-28 / 編成一時枠・戦闘チート・20倍指定）

確認用ビルド `.local/dist/0.1.35-formation-cheats/kbcs.exe`、SHA256 `25cb598b3e04ee074eb6815b0bfc3450c09c26e1c1692ef2ea89b13e80f6c7bf`。DLL/verification.jsonを同梱。旧4851/4852を停止せず、4853でpreviewを起動。GUI確認はユーザー担当。GitHub書込なし。前回の出撃準備等の変更を含め、現在は未コミット。

- ユーザー確認: 一時5枠は選択時に手動移動、精霊召喚ボタンを隠す、上限解除は味方50体も対象。編成一覧は中央の戻るリンクの下、検索/形態は左、個別設定は右。追加は選択枠を上書きせず最小空き番号へ。満員時は本家の同じ1行分の描画を切り出した一時枠へ。正式10枠と一時枠を分離し、後者は編成ID別sessionStorage。空きを作るだけでは自動で移さない。
- 操作盤のチートボタンで資金/数量上限/即生産/精霊ボタンを設定。flagsはC++所有Battleへ渡し、JSで金額/再生産を上書きしない。通常APIのPOD/ABI4は維持する。精霊状態/既存の精霊は削除せず、非表示中は親を通常生産できる。速度はアイテムに従う、または通常1倍基準で1..20倍。3倍アイテムと掛け合わせず、論理Fを飛ばさない。FPS隣に停止/非表示を除く累積平均を表示。
- actor_pool.incが通常51枠に加えて必要分をdequeで保持。TLS scopeを公開所有API内で借り、通常の単体API形状/敵生成50枠を保持。追加個体の生成・時計・攻撃/対象列・被弾・保護・死亡・波動/烈波/爆波履歴・Rustの描画/診断まで共用。nativeの関数/所有関係はbattle-runtime.mdへ記録。原本にはないチートを本家と同一とは呼ばない。
- 個体仮想アドレスと陣営strideの生成アダプタを追加。初回の回帰で相対offset c810/c83c/c840を見落としていたことを修正した。actor_pool_source.pyでHEADの生成ソースから変更後が完全再現できる。原本researchファイルは変更していない。通常経路の元の整数/乱数順を維持。
- workspace33＋compile_fail1、clippy all-targets -D warnings、JS/SE/編成SVG8条件、BOM/diff検査を通過。最終の合成C++試験4条件は80体・1番/80番の同じ被弾HP（通常7500/波動6800/烈波5500/爆波5300）、即時入力/資金/ステージ数量上限、50体共通上限へのOFF復帰、精霊切替が通過。1F所有回帰と操作SEもrelease archiveから再検査。
- 最終exeで実DBの通常戦闘30観測（900Fまで）を旧sortie-uiと比較し、時間計測を除くstate/layout/runtimeと描画命令数が同一。GPU頂点/画素の比較ではない。750Fの観測で勝利。実DBでも80体、追加30個体の診断語、335描画命令を確認。CLIのmemory報酬Store/隔離データで、実所持品へ付与しない。
- 4853からUI変更18ファイルのbytes一致、静的import、編成/出撃準備ページの200応答を確認。記録はresearch/.local/formation-cheats-{normal-replay,80-input,80-replay,replay-check,serving-check}.json、同梱verification.json。見た目と大量個体時のGPU性能は未検査。

# 再開メモ（2026-10-28 / 出撃準備・BGMシーク・戦闘ペイン）

確認用ビルドは `.local/dist/0.1.35-sortie-ui/kbcs.exe`（13,144,576 bytes、SHA256 `f12075bbe88619d706c4090c9680560e16988bcad1e69f25d4f622bceceba455`）。DLLとverification.jsonを同梱。旧4851を停止/差替えず、新版previewを4852へ起動。GUI確認はユーザー担当。GitHub書込なし。今回のUI修正は未コミット。

- 戦闘開始時の左右ペイン強制閉鎖を廃止。下部情報パネルを中央editorの子へ移した。上部操作/状態/計測欄を広げ、比率はPixel 8相当20:9を初期値として保存。16:9/18:9/21:9/領域追従へ切替可能。固定比率の余りを中央下の折りたたみパネルへ配分。論理Fや乱数を変更しない。
- 注釈6件も反映。検索ギミックは横一列/横スクロール、最終編成を保存、既存編成SVGを共有、城体力の値をラベル付近へ、アイテムはmapicon ON/OFF画像、速度OFF→2→3→OFF。いざ出陣!!は007802c0/007acf88のimg031_ja cut10/11を使い、内部差分[38,6]を保持。準備画面へのホスト配置と原本部品の内部配置を区別する。
- BGMシークの先頭復帰はRange非対応応答への直src指定が原因。試聴と戦闘でBlob取得を共有し、ドラッグ中のtimeupdate上書きを停止。取消/画面切替で取得とURLを解放。編成切替中の旧deployment応答も世代で無効化。
- 原本ARM64の出陣配置24条件、編成編集の移動前後SVG8条件、preparation/battle-audio回帰、JS構文・BOM・diff検査が通過。releaseビルド完了。実DBの隔離リプレイは750Fの観測で勝利、900Fまで継続、PNG取得も検査。memory報酬Storeを用い、実ユーザー所持品は変更していない。
- 新previewから変更15ファイルの配信bytesがディスクと一致すること、静的import/HTML参照の200応答を確認。記録は research/.local/{sortie-ui-1572,sortie-ui-release-replay,sortie-ui-serving-check}.json と同梱verification.json。関数関係はui/docs/{stage-sortie,formation}.md、素材追加はscripts/docs/README.md。実画面/GPU画素/原本入力時計の全体一致を確認したという意味ではない。

# 再開メモ（2026-10-28 / 0.1.35公開準備）

ユーザーがバージョン更新とGitHubへのソース一式のPushを明示承認。0.1.35、タグ`kbcs-v0.1.35`で公開する。生成済みC++ inc、Rust、UI、検証コード/fixture、解析資料を含む。会話添付、AppData、ビルド/cache/巨大実験生成物は除外。アプリと同コミットのsource ZIPをReleaseへ添付する。

- 最終exe: `.local/dist/0.1.35/kbcs.exe`、SHA256 `388af72d2758693255816c50c47d70633a4350531c99e3791683d1ea3832a88d`、12677632 bytes。必要DLLとverification.jsonを同梱。バージョン以外の戦闘式は直前のscore-uiから変更していない。生成C++の空行末尾の空白6箇所だけ正規化し、生成器にも反映（C++ token列の同一を検査）。
- 新版でworkspace33＋compile_fail1、clippy all-targets warnings禁止、WebAudioライフサイクル、N000実DBの750F勝利/PNG取得が通過。diff空白/BOM/credential検査も通過。GUIを起動せず、ユーザーの実行中アプリ/タブや実所持品は操作していない。
- [GPT調査用の現状と残課題](review-v0.1.35.md)を追加。README/architecture/native入口の古い未接続/ABI記述を現在の所有Battleと区別した。主な残りは自作マップ、levelSealの戦闘接続、専用controllerの残分岐、一部画面揺れ/専用演出/動的SE。未検証の全main/全F/GPU/可変共有モデル境界と分ける。
- 後続の公開結果はGitのmain/tagとGitHub Releaseを正とする。取得済み原本キャッシュとローカル実験報告はresearch/.localに保持し、削除していない。

# 再開メモ（2026-10-28 / 道場上部UI・ステージ名・結果帯）

画面確認はユーザー担当。起動中アプリ/タブは操作・再起動・差替えなし。GitHub書込なし。以前の大量の未コミット作業は保持している。

- 確認用アプリ: `.local/dist/0.1.34-score-ui/kbcs.exe`。SHA256 `6ca2745c5d3d11ea247b0fdeb19be3999b2cb6574a052597ca428662d8be4ff4`、12677120 bytes。前回の1F/SE修正を含む。DLLと試験/制約のハッシュは同梱verification.jsonへ保存。
- `actor_top.inc`追加。006ddfb8/006e11f0..1b9cからタイトル(x62/y10)、道場Score/残時間、PR Pt/残時間/FeverをC++共用描画へ接続。死亡時の表示phaseを受け、表示hook5で補間/拡縮を進める。原本img001/FeverEffectの部品/数字/横伸縮を使い、JSに式を複製しない。
- タイトルPNGはsource_fileにbytesがなくasset_referenceにだけあるため、旧存在確認ではnullになっていた。両表を確認し、既存SHA固定asset取得→scene.texture→暗転中のtextures読込へ接続。宇宙編kind -7/-14/-15/-25はsc。DB再取込不要。タイトルをスコア枠より先に同じGPUへ描き、終了時陰影/帯の下へ置く。
- 結果横帯は005e97d8/005ee758の乗算mode2/RGB40,40,77/alpha255。透明HUD Canvasへ合成していたため不透明に見えた。C++overlay→同じGPU描画先の単色geometryへblendを渡す。敗北陰影も移した。任意の透明率で代用しない。
- スコア式の追加差分は監査で見つからなかった。ScoreBonusMap全12マップ・20種・対象数5通りの1200条件、撃破720、道場時計40、PR Pt204/Fever800/時計72等を原本ARMへ比較。実マップのraw定義→Rules.bonus→同期scope→word232→protect後加点の契約を保持する。全mainや全能力組合せまで一致済みとは扱わない。
- 原本描画の補間128/配置152条件一致。数字formatter/9分割は実命令、gfx出力を捕捉。幅960/1280、900F境界、mode0/4、Fever点滅を含む。probeは解決済みの所有表示状態を入れる描画専用fixture。最新DLL SHA `e627b3ac603821726b98b893d40ef7f7d390cfe9de422ed081a9eff0806c544a`、probe `ef54256e99375ab927d7b3eee77f86f13645215ce12ca15ad4292d3e12e77ffc`。
- 最終exeで実DB接続18ケース: 全12ボーナス定義をRulesと照合、T000は9000F/mode4、R030は5400F/mode4、PR通常/Feverは5400F/mode1、S060は9092点、N000は勝利。画像PNG検査も全通過。初期HP/資金/編成を制御し、battle-replayのmemory報酬Storeを使用。実ユーザー所持品は増やさない。
- workspace33件＋compile_fail1、all-target clippy warnings禁止、JS4ファイル構文検査、diff空白検査通過。日本語変更ファイルはBOM付きUTF-8（rustfmt後に復元）。実画面/Android GPU画素/全ステージ連続の一致はユーザー確認と今後の課題であり「スコア完璧」と主張しない。
- 関数関係はnative/docs/battle-screen.md、battle-result.md、stage-score.md、render.md、data/docs/README.md、ui/docs/stage-sortie.mdへ追記。大きい入力/報告はresearch/.local/battle-score-*、battle-top-1572.json。古い「UI未接続」の記述は日付時点の履歴として読む。

# 再開メモ（2026-10-28 / 戦闘操作・終了境界のSE）

ユーザーが画面確認を担当。起動中アプリ/タブは操作・再起動・差替えしていない。GitHub書込なし。

- 確認用アプリ: `.local/dist/0.1.34-battle-audio/kbcs.exe`。EXE SHA256 `5c6d6a5b19f17b9446ceda4785336544b5652ab0dd169b302da557269adc5290`、12663808 bytes。verification.jsonへ検証を保存。下記の1F修正も含む。
- `battle_screen.cpp`→音源hook→所有Battleのframe/id通知。財布成功19/最大・資金不足15、砲種別音＋19/充填・行動中15/充填完了28、押下10、ポーズ・アイテム・オプション解放11を接続。音量は原本callback3の解放時に変更し、SE0/復帰時の11もその音量を使う。5表示更新の操作待機は維持。振動は無効。
- `00459f04`のgame modeゲートが共通ラッパーから欠落していたため修正。effects/areasも原本のf04/efcを区別。死亡23/24・反射召喚159等のefc呼出を終了後一律に削除しない。勝敗時の00459bb4(-1)はBGMのみ停止する。
- 通常命中は全被弾を集計し、勝敗判定後、mode0なら城22か個体20/21の一回抽選。無音でもRNGを消費。勝利Fは命中音抽選なし。1F所有試験にもHP1のFで22/勝利Fで22なしを追加。
- WebAudioは同じ音源の再生し直しとloopを適用。終了/ミュート後に古い取得待ちが鳴ること、新しい終了音が古い取得待ちに塞がれることを防止。既に鳴っている全SEを勝敗時に停止しない。51音の索引を確認。
- 原本ARM局所130条件一致、C++所有入力回帰、WebAudio mock、1F通常/倍速、workspace全テストとclippy warnings禁止、JS構文検査が通過。音声デバイス/全mainの連続実行は未確認。Android priority/voice資源解放、ID29の動的差替えは既存制約として残る。詳しくはresearch/docs/audio-1572.mdとnativeのbattle-screen/runtime docs。

# 再開メモ（2026-10-28 / 1Fの実戦接続修正）

ユーザー再指摘: ボス衝撃波も一瞬の出現/魂も起きない。KBC-webは再現できている。原本・Web・C++を再比較した。

- 前回の局所試験は城100→50→0で、未出現ボス前の致死攻撃を通していなかった。下の古い「1F確認済み」はこの不足した試験を指す。今回の情報を優先する。
- 原因: 原本006d9e44..9fc0の出現予定走査とgame+39a228の接続が欠落。healthのHP1保持分岐はあるが所有Battleが常に0を渡していた。WebにはbossPendingでHP1を残す簡略処理がある。
- `kbcs_core_stage_castle_guard`を追加し、保護後/特殊城HP複写前に原本の条件で旗を立て、healthへ渡した。HP>1、残り出現回数、boss非0、保留ダメージ後HP/特殊累積ダメージを使用。待機や撃破条件は加えない。32bit演算を保持。006d7208同様、表示更新の先頭だけで旗をresetする。
- 旧DLLと新DLLで同じ`native/kbcs-core/tests/battle-one-frame.cpp`を実行。通常出撃/実際の2段攻撃を通し、旧は7Fで城破壊/ボスraw0、新は7FでHP1→8Fでボス生成/味方行動7/ボス行動4/HP0/時計0/SE45/shock描画要求/勝利。倍速は同一表示内の旗保持も検査。
- ARM走査1024条件一致、更新した局所2F試験8更新一致。Webの既存battle.test.js通過。詳細: native/kbcs-core/docs/battle-result.md。確認用ビルド: .local/dist/0.1.34-one-frame/kbcs.exe。実画面はユーザーが確認し、起動中アプリ/ブラウザは操作しない。

# 再開メモ（2026-10-28 / 原本の結果画面・報酬保存・1F境界）

確認用releaseは `.local/dist/0.1.34-battle-results/kbcs.exe`（12,658,176 bytes、SHA256 `98b8cc0920eeef2593300b795a27d5edd6927404062feb6b883fe49447b349ac`）。同フォルダのverification.jsonへDLL/EXEのハッシュと検証を記録。画面確認はユーザーが担当。起動中のユーザーアプリ/タブは操作・再起動・差替えしていない。GitHub書込なし。原本JP15.7.2/1507021/arm64-v8a/SHA6122e248…を継続する。

- 最新補足: 特定のキャラ/ステージではなく、ボス衝撃波開始Fと城HP0が重なる条件を再現する。`battle_one_frame.py`が出現→衝撃波→HP反映→城判定を2F連続で比較。味方行動7と勝利mode1が同じFに成立し、城HP1/衝撃波無効の対照も一致。一律の1F遅延は追加しない。攻撃/生成入力は制御した局所連続試験で、全mainの実行ではない。
- `actor_ending.inc`が通常/PR/敗北/道場の時計・カメラ・通知を所有する。通常下部移動82、道場96（旧640記述を訂正）、2段終了zoom8803。phase7のボタンは006ddfb8側のimg101 cut3＋img006_ja cut1。道場img101_nekoDojo。押下と5表示更新後の遷移を接続。
- 通知は独自の画像modalを廃止し、005e53dc/005e82fc/00885170の原本文字列、img005_1の9分割、y401/文字30/行間36/開く倍率[0,50,80,90,100]へ接続。phase8、SE29/11、閉じ5更新。素材は4種類ずつ2種類で改行、回数報酬はbackstage_result1。
- キャラ所持を保存して再現することはユーザー明示承認済み。user/inventory.sqliteのcharacterとclaimへ基本Lv/＋値/所持/第3・第4解放/共有入手旗を保存。編成の最大設定と独立。006e34b0の正規1000/1100番台では入手済みresult1へ進み、＋値を勝手に増やさない。存在する加算コードだけからの推測を撤回し、ARM48条件で一致。報酬1002は独立旗、drop_chara列1の別名は共有旗。
- `inventory::Store::finish`が表示数/累計/所持/初回旗/結果を同じtransactionで確定。同戦闘番号の再取得は保存済み結果。表示数は自由設定、累計は独立。ホームに持ち物、2タブ。API/catalogの1128件を実DBで取得。CSVはGatyaitembuy見出し/コメント列12以降とdrop_chara見出しを除外し、不正セルの原因を修正。追加報酬の末尾空欄も未定義として処理する。
- `Receipt`はDBのステージを再取得して検査し、XP/通常・重み報酬/素材/スコア/回数報酬を解決。保存失敗はreceiptErrorと再試行へ。battle-replayはmemory Storeを使用し、実所持数を増やさない。通常previewの接続確認はresearch/.local/battle-results-previewだけを使った。
- BGMは敵城HP crossing停止→45論理F後に後半曲、開始待機は表示F、Sound_settingのloopを使用。既定終了SE8/9、道場57/189、eventDisplayDataのtype0抽選/type1全再生。optionsの音量永続化は維持。
- 検証: workspace全テスト、clippy warnings禁止、JS構文検査。battle_ending.py（controller/zoom/BGM50条件/popup配置16＋時計16）、battle_result.py、character_reward.py48条件、battle_one_frame.py8更新がARM一致。実DBの通常勝利/スコア勝利/道場5400F/PR勝利をheadless実行。S139を2回勝利し、初回入手＋再取得非加算と表示12/累計0の独立を検査。通知4件→OK→5更新後action302、結果再取得で二重加算なし。
- 大きい報告はresearch/.local/{battle-ending-1572,battle-one-frame-1572,character-reward-1572,result-release-replays,result-persistence-connection,result-popup-connection}.json。原本のアカウント全進行・通信/広告通知・Androidフォント字形までの完全一致を主張しない。全mainの連続実行と同一ではなく、制御した局所比較と実DBの接続検査を区別する。詳しい関数/部品はnative/kbcs-core/docs/battle-result.mdとdata/docs。

# 再開メモ（2026-10-27 / 追加生産・PR・対象限定コンボ）

確認用release: `.local/dist/0.1.34-battle-special/kbcs.exe`（12,129,280 bytes、SHA256 `e77fe965d766ace14c0f472eeb70c36ecd5689c7423401c2b7d848abfdc98319`）。必要DLLとverification.jsonを同梱。ABI4。起動中アプリ/ブラウザ/プレビューは操作・再起動・差替えなし。GitHub書込なし。既存の大きな作業ツリー/添付/researchを保持する。

- 最新要望は不足を見つけて順に埋めること。今ターンは追加生産、条件付き本能玉/再生産・価格、PR専用Pt/Fever/時間勝利/敗北mode7、対象限定コンボ、DB計算のABI番号不一致を修正。詳細と関数関係は `native/kbcs-core/docs/battle-special.md`。
- JP15.7.2/1507021/arm64-v8a/SHA6122e248…を継続。0044a8d8等の戦闘RNGを共有。ルール8は通常生成成功時に予約し、次のlogicalの時間判定前に末尾から更新。待機1→0のFには生成しない。満員失敗でも消費し、生産数を一時的に1減らして構築し復元する。余分な費用/再生産/通常生産総数を加えない。敗北で予約clear、勝利時に一律停止しない。
- 005c2f88のkind/periodはparam.tsvから解決。構築前と通常生産成功後の呼出を分け、初期能力と次回待機へ反映する。本能玉5..等の条件付き初期能力、19の短縮、22のコスト。固定時間ルール1は短縮を迂回する。普通の属性玉0..4の命中効果はこの生産条件で無効にしない。
- 00aa0568をproduction_costへ接続。原本loaded cost/本能25/章/率を使い、固定4→本能玉22→個別コンボ27→レア度5の整数化。現在価格をHUD/CPU/支払い/返金で共用し、その後で動的価格11を掛ける。UIの初期コストを所有戦闘の確定値にしない。
- NyancomboData.csv列2→0088fde0 object+0x10。group!=-1は009e4e14のCharagroup type3所属を要求。既存source_fileから読むためDB再生成なし。現版group10は831..836/857/858。全体と対象別を分け、Rules.unit_combos/同期BattleRulesScopeで速度/stat/命中getter、Rustの再生産combo11、順序付き価格combo27へつなぐ。固定配列の未使用枠をJSONへ展開しない。
- PR000(nativeKind-26/id39000)はPointStageSettingsの対応を確認。旧DBに原本bytesがなければasset_referenceの固定revision/SHAからAppDataへ取得。StagePointRulesMapの区間率で出撃/最終撃破Ptを計算する。有限時間の実命令はFCVTZS W20で、疑似コードのuintではない。
- ルール12の4番目はFever用の別ルールID6であり6F固定ではない。現版は600Fの間6レア度の再生産率が0。logical先頭で00645288、表示Fで00645444、表示末尾hook5で0064556cを進め、描画/HTTP batch回数で差を作らない。SE194。勝敗時00645630相当でending=1、表示phaseを5へ進める。
- PRのtimerは00a0cdbc、期限は006d7e6cから勝利mode1。5400Fでelapsed5399。城敗北はmode7。結果画面の所持Pt/報酬保存は別。ホスト常設欄へPt/時間/Fever/追加予約を追加した。
- DBのnative-calculation.jsに古いABI2判定が残っていた。サービス/コア/橋/診断/テストをABI4へ揃えた。CLIの画像検査はtexturesの予約null枠を飛ばす。
- battle_special.py: C++へ3364件（condition48/plan216/queue80/cost1944/Pt204/Fever800/PR時計72）一致。さらに原本の対象getter45件を採取し、実DBのRulesと比較。勝敗654、CPU2560更新も最終DLLへ再照合。DLL SHA `100909b9d4e5b3aa2393ee15df70952663574831850c580ccbbd0b957833cd95`。
- 最終exeのPR0は5400F/24657Ptで勝利、Fever編成は5400F/102886Ptで勝利・SE194/600F切替と復帰、空編成の城破壊は919Fでmode7。SR017/027は追加予約/生成あり。group10の5キャラと対象外94で価格/初期速度を検査。--validate-assetsも通過。接続報告はresearch/.local/battle-special-connection-report.json。
- 最終exeのFever5700F（70対2100応答）とSR017 3150F（35対1050応答）は全state/個体251語/RNG/SE順/結果/予約/Ptがbatch対1表示Fで一致。初期資金/自城HP等を制御した実DB接続fixtureで、本家全Fの証明ではない。
- workspace31＋compile_fail1、all-target clippy -D warnings、rustfmt、JS構文、NodeでABI4受理/ABI3拒否が通過。日本語変更ファイルはBOM付きUTF-8。大きい原本/入力/報告はresearch/.local。GUIの目視確認はユーザー担当。

残り: 本家の結果画面全体/結果音声、報酬抽選・所持数/最高記録の保存、Feverの原本ゲージ/モデル描画、ステージ固有Lv封印・専用controllerの残分岐、可変共有モデル境界/画面振動/全mainとGPU画素の照合。今回の接続を全完成と扱わない。

Fever描画の次の入口: 006ddfb8、BattleTextureContext+0x16598のImage/FeverEffect.pngとimgcut、+0x165a8のmamodel、+0x16650のmaanim（実asset_referenceに4ファイルあり）。006455fcがframe、00645604がphaseによるroot値、中央viewportWidth/2・height/2へ00448e7c。モデルroot+0x7cの値を差替えるため、既存poseのどの欄かを推測せず確認する。HUDはcut8/9、mask7、overlay6。既存描画/座標へ憶測で追加しない。

---

# 再開メモ（2026-10-27 / 勝敗・道場Score・出撃制限）

確認用release: `.local/dist/0.1.34-battle-result/kbcs.exe`（12,083,200 bytes、SHA256 `c0fe8856ff5f5e0f6b513ac2bcf1cf38f5aa0c1d38cbfd03a6db771f6d9d1ad6`）。必要なDLLとverification.jsonも同フォルダ。起動中のアプリ/ブラウザ/プレビューは操作・停止・差替えなし。GitHub書込なし。既存の大きな作業ツリー/添付を保持。画面はユーザーが確認する。

- 最新要望: 勝敗、道場系Score、特殊な出撃制限を接続。`native/kbcs-core/docs/battle-result.md`へ原本・順序・関数関係・検証範囲を記録。
- JP15.7.2/1507021/ARM64/SHA6122e248…。新しいactor_result.incに勝敗/時計/動的制限/ボーナスgetterを置き、owner→bridge→Session→常設操作欄へ接続。stage nativeKindをnativeModeと分ける。C++/RustのConfigへRules、ScreenState末尾へbattle_mode（旧JSONは省略時0）。FFIは同時再ビルドする。
- 原本006db46cは敵城破壊が先。同時0なら味方城を1に戻してmode1。敵城が非0で味方城0ならmode2、T/R道場はmode4。勝利の通常敵は行動4/時計0/HP0へ。特殊城はword111が0のとき行動17。005e02b0の味方散開はDAT002b2bb0=(4,0)、個体ごとに5回RNGを消費する。
- 行動前に道場timer、health後に城判定。終了後も個体/二次攻撃/演出時計を継続する一方、出現/出撃/CPU/財布・砲操作を止め、収入・砲充填・再生産時計は戦闘中の末尾に限定。次の表示Fから速度を通常へ。stateless画面APIの経済更新は維持。
- 道場はnativeKind3/4の005e1400通常経路。timer/limit/score/mode/quietを既存enemy_knockbackへ渡す。普通の道場とScoreBonusMapありの入金分岐、固定資金で入金なしも分ける。実ボーナス点数÷対象数を命中getterで解決し、word232をprotect後に加算/解除。同期thread_local scopeで単体命中のイベント捕捉契約を保持する。
- 通常スコア報酬はscoreRewards＋有効scoreIdの勝利時に既存stage_scoreを呼ぶ。nativeKind−6は原本の時間二乗スコア。WebのscoreModeや正のtimeLimitだけでPR(−26)を道場にしない。
- 動的制限は009e57b8のraw>1かつ生産slot<10をレア度別に数え、死/魂の枠もraw0まで数える。ルール3は0無制限、7は通常生産総数で0出撃不可/なし−1。ルール0ありなら009e583cは資金だけを判定し3/7を通らない。ステージ上限0と物理50枠を区別し、上限を50へ置換しない。精霊召喚も静的/ステージ同時数条件は通す。
- 表示Fごとに生産警告(wait,status)を更新しCPU modeへ接続。上限時(0,1)、入口拒否(30,2)。手動/CPU/HUDで可否を共用。runtime.result/deployment/rulesを追加、JSに式を複製しない。
- battle_result.pyの同版ARM64局所654件（bonus36、limit486、城優先36、敗北個体/RNG48、勝利個体8、時計40）が一致。敵死亡720件とCPU2560更新も再照合。報酬/セーブhandlerとgetter/既存seen treeは制御した比較で、全main一致の主張ではない。
- 最終exeの実DB接続: N000勝利761F/敗北536F、S060は908FでScore9092、R030は5400Fで時間終了/elapsed5399/Score31072。SR002はレア度同時数1を守り退場後に再生産、SR005は総生産60で止まり物理50枠も通過した。
- 6ケースのbatch対1表示Fが全state/個体251語/RNG/結果/制限/SE順まで一致（900/660/1050/5430/2400/870F）。速度3の道場締切後も演出を継続し結果を固定。CPU既存fixtureも3390Fで一致（勝敗で倍速が解除されるため旧4140Fとは異なる）。初期資金/自城HP/価格を一部制御した接続fixtureで、本家全フレーム比較ではない。
- 最終DLL: research/.local/battle-result.dll、SHA `4e2cbc736a401775aecf08cdb147eb77248a65627a37491aa3264fd1d3ddbc7f`。workspace31＋compile_fail1、all-target clippy -D warnings、rustfmt、JS構文通過。日本語変更ファイルはBOM付きUTF-8。大きい入力/報告はresearch/.local。

残り: 本家結果画面全体/結果音声、報酬付与・保存・報酬抽選RNG、PR専用の記録/フィーバー/終了controllerとmode7等、ルール8の追加生産予約。可変共有モデルの境界、残る特殊VFX/画面振動と全main/GPU画素の照合も別。今回の勝敗/道場/ルール3・7接続と、これらの完成を混同しない。

---

# 再開メモ（2026-10-27 / ニャンピュータ・生産価格）

確認用release: `.local/dist/0.1.34-battle-control/kbcs.exe`（12,066,816 bytes、SHA256 `2e100a1891932f916029831a1d5ab842ee0bd0784e8cdcf30a6b091bb6fadea4`）。DLLとverification.jsonも同フォルダ。起動中アプリ/ブラウザ/プレビューは操作・停止・差替えしていない。GitHub書込なし。既存の大きな作業ツリー/添付は保持。ユーザーが画面を確認する。

- 最新要望: 未完了部分を続行。通常のニャンピュータと、生産ごとに変わる価格をC++所有戦闘へ接続した。
- 原本はJP15.7.2/1507021/ARM64/SHA6122e248…。006ee6c8をactor_computer.incの67行へ正規化し、kbcs_battle.hのInput/State/Outputを追加。候補保持、30%の財布側選択、候補数1の抽選、砲の150待機→2抽選、城付近の別判定、ページ待ち/逆転、精霊activeの除外を維持する。原本の発射失敗は選択1を保持、成功したfire側だけが解除する。
- battle_screenのhook 3は表示更新ごとに一度、論理Fループ後・ガード後・手動入力前。一時停止/暗転/押下ガード中は呼ばない。倍速の各論理Fへ自動判断を増やさない。通常のdeploy/fireを共有し、CPUの構築/発射失敗通知は原本指定に合わせて抑止する。
- battle_computer.py: 640条件×4=2,560更新を同版ARM64の006ee6c8へ比較。全候補/保持値/砲判断/ページ要求/操作/RNGが一致。射程helper005bf6c8/005bf658も実行。可否/プロフィール/財布/価格/再生産、生成/発射、音声、009e57b8集計は制御した局所照合。全main一致の証明ではない。
- 005be130→production_price→KbcsBattle::costへ特殊ルール11を追加。last_cost=0ならbase（生産回数の非0ではない）。mode0/1の整数化とcapを保持。非0last_costで3列不足はエラー1/出力不変。実データA081（24081）は[0,200,99999]。価格の120正常条件/72不正列条件が原本と一致。
- 価格は実支払い、CPU判断、返金getter、runtime.costsで共用。手動押下を初期価格だけで事前拒否せず、所有deployで再検査する。JSのコスト表示/金欠判定もruntime.costs（1/100円）。statsへcomputer/produced/lastCostsを追加した。
- 最終exeでCPU試験4,140F（74batch対2,202単F）が全永続状態/個体251語/RNG/通知順まで一致。初期財布0→Lv8、下段7/9枠の自動出撃、1段/ページ待ち、2倍/3倍/通常、CPU OFF/ON、一時停止、砲通番2を通過。battle-computer-input-session-report.json。
- A081実DBの1,500F（51対1,512）が一致。出撃数[4,14,1,1]で次価格[540000,1740000,1341000,1485000]、直前価格と生産数からの更新も全応答で検査。battle-price-input-session-report.json、battle-control-connection-report.json。既存の手動入力/二次攻撃1,539F（66対1,562）も一致（battle-effects-input-session-report.jsonは今回のexeへ更新）。
- 最終DLLはresearch/.local/battle-control.dll、SHA a5525a4810e63ea587c55d8cf76ce0829d32ff9c8ef452c52f527f6e2b3aeef8。workspace31＋compile_fail1、全target clippy -D warnings、変更JS構文、git diff --checkを通過。日本語ファイルはBOM付きUTF-8。

詳細: native/kbcs-core/docs/computer.md、battle-runtime.md、production.md。

残り: computer Input.modeは原本game+2971f0（生産警告時計）を受けるが、所有側は通常0。特殊な生産拒否警告の時計、全レア度別/総生産制限、追加生産は未接続。勝敗/時間制限/報酬、可変共有モデルの境界、全main/GPU画素、残る特殊演出/音声backendの資源圧迫条件も未完了。下の「ニャンピュータ/特殊価格未接続」は今回の通常接続で更新する。

次の原本入口: 006db46cは敵城HP=0を先に判定（同時0なら味方城を1へ）して005d996c、敵城非0/味方城0なら005e02b0。通常mode1/2のほか特殊mode4/7。制限時間は論理更新前で005bbba0=9ee64×1800、005e1400の開始flag/特殊種別/71a0c4条件も追う。HP0で全処理を凍結する近似を入れず、結果演出中の個体/時計も原本照合してから接続する。

---

# 再開メモ（2026-10-27 / ボス衝撃波・境界・VFX/SE・スニャイパー画像）

確認用release: `.local/dist/0.1.34-battle-effects/kbcs.exe`（12,055,552 bytes、SHA256 `349c98ae4e10949b374290ff6c5f602ed722c30c09f20ab1d08fcee57f0aa36c`）。同フォルダに必要なDLLとverification.json。ユーザーが表示確認を担当する。起動中アプリ/ブラウザ/プレビューは操作・停止・差替えしていない。GitHub書込なし。前からの巨大な作業ツリー/添付を保持。

- 今回の要望: 城HPの左値がslashへ重なる、召喚OKの青色、ボス衝撃波、敵ボスと味方の後退限界、特性/被弾演出とSE。追加で、スニャイパー付き開始時の `The source image cannot be decoded.` を修正。
- HP右端の14px二重補正を除去。召喚可能アイコンを原本005d0a68のRGB(157,215,255)で乗算し、OK画像の明滅もwait由来にした。
- actor_bossを所有logicalの攻撃後・波動前へ置いた。初回SE45、無効/行動条件、行動7、時計更新/上限。actor_boss.pyで同版ARM64の288更新が一致。表示基点boss_effect_anchorも006e042c..006e0588の108条件が一致。Yのscale補正を10で二重に割らない。
- 00a9490cのボス限定の敵城補正を追加。既存knockback/displacement検証をモデル点だけ制御して00a9490c本体も実行する形へ拡張し、味方mode1152＋敵mode3456条件が一致。初期モデル点を使う現状と、可変共有モデル/全mainの連続照合は区別する。
- 所有VFX: critical200、ゾンビキラー/バリア/悪魔シールド各30、渾身/毒撃/メタルキラー/遅延の可変リスト。固定poolはplain、可変リストはencodedの時計。12F被弾の000_a、色/加算、妨害・生き残り・強化・無効・持続barrier/shieldと反射烈波の召喚待ちを接続。status→波動→烈波→反射待ち→爆波の順も維持。描画命令colors[3]=1をtexture乗算色の指定に使う。
- 位置抽選RNGをcritical確保→渾身→毒撃→メタルキラー→critical座標→通常被弾→healthの順に追加した。音声・表示の有無で省略しない。SEは原本helperを同期scopeで捕捉し、runtime.soundsへ当該advanceのframe/id通知を返す。batch試験は単F区間のSEを連結して通知順も比較する。battle-audio.jsは取得/decodeで戦闘を待たせない。
- 009f560cからclocks39本を解決。actor_motion_lengths.pyは試験側のtrackメモリ重複を訂正（C++の長さ式はそのまま）、135人工＋39実ファイルが一致。バリア3/シールド5の書式文字列ループもexporterへ記録。
- スニャイパー失敗の原因はImage/img043.pngがasset_referenceにだけありsource_fileにないこと。/api/assetが500 JSONを返しImage.decodeで失敗していた。source::assetはDB metadataの固定origin/revisionと索引SHAからAppData/assets/objects/<SHA>へ遅延取得する。公式DB再構築/書換なし、最新HEADへ切り替えない。最終exeのbattle-replay --validate-assetsを通し、img043のSHA、全PNG chunk CRC、IDAT展開(256×128 RGBA)を確認。report=research/.local/battle-sniper-assets-report.json。
- 同版CAF9本を音源索引へ追加。LPCM16 little-endian/1〜2chをWAVへ包み直す。原本9本と返却WAVのPCMがbyte一致（audio-pcm-report.json）。SE65/137/139も原本を優先。キャッシュは元CAFとSHAを保存。
- 最終releaseで通常入力1539Fのbatch66応答対単F1562応答が全個体語/状態/描画記録/通知順まで一致。ND032実編成は4800F/841応答、最大27個体、衝撃波と妨害/生き残り表示を含め停止なし。reports=battle-effects-input-session-report.json、battle-effects-nd032-final-report.json。
- N045-2/DM000-0/NA021-5を各2012F進め、critical、バリア、シールド破壊/再展開、毒撃を通過。別N045入力でbarrier breaker0x2398/SE70も確認。これは実DBへ人工的な低コストを与えた接続試験で、実機全戦闘との比較ではない。reports=battle-visual-cases-report.json、battle-visual-barrier-report.json。
- workspace31試験＋compile_fail1、全target clippy -D warnings、変更JS構文、git diff --checkを通過。日本語ファイルのBOMを復元した。

詳細はnative/kbcs-core/docs/battle-runtime.md、render.md、crates/kbcs-data/docs/README.md、research/docs/audio-1572.md。全main連続実行、GPU最終画素、可変モデルの接触境界、残る特殊演出/画面振動、Android音声バックエンドの資源圧迫時priority/voice解放は未証明。ニャンピュータ、特殊価格、勝敗/時間制限/報酬の接続も以前から残る。表示確認はユーザーが行う。下の過去メモの「ボス/全SE未接続」は今回の追加で更新する。

---

# 再開メモ（2026-10-27 / ND032停止・上下位置・HUD・城砲接続）

配布候補 `.local/dist/0.1.34-battle-session-fix/kbcs.exe`（release）。ユーザーが表示確認を担当し、起動中アプリ/ブラウザ/プレビューは操作・停止・差替えしていない。GitHub書込なし。既存の大きな作業ツリーと添付ファイルを保持。

- ユーザー報告: 0.1.34-battle-session、ND032-0「バラバラバラン草原」で約2700F後に暗転/更新停止、エマ/天使ゴンザレスの上下位置が違う。
- 原因1: `render.cpp`が106_s02.maanim（カイ）の逆順キー47→46を拒否。旧exeへ保存済みエマ入り編成を通すと初攻撃でエラー1を再現（人工入力では397F/398F。時点は出撃/資金次第であり2700F固定ではない）。0044c884の原本順の区間探索へ変更した。
- 原因2: 0044b854の4c/54等は原点の基礎/加算値だった。位置まで引いていたのを訂正。0044af4cの根matrixは位置加算だけで、モデル基礎X/Yを含めない。エマ559_sの基準点[-72,0]、天使ゴンザレス115_eの[125,153]を原本に比較。`model_contact.py`は実メモリレイアウトを使う試験へ訂正、300条件+実モデル2+カイ145Fが一致。旧「位置と原点を両方引く」解釈を使わない。
- releaseのND032回帰は原本コスト/保存編成で4800F、味方最大21/敵最大17、対象のraw117/561を含み停止なし。旧exeの同入力は397F後にエラー1。別入力のdebugビルドは9975F/最大計53個体も通過。reports: `research/.local/battle-nd032-regression-report.json`、`battle-nd032-regression-input-session-report.json`。
- スニャイパー: actor_sniper.inc、005ce564/005ced48の照準・弾・煙・命中を所有battleへ接続。3720更新/8発/480命中のARM64局所比較と有効アイテムの1539F batch/single比較。城MAXHP/20、メタル1。GPU画素/全SEは未検証。
- 城砲: actor_cannon.inc/actor_cannon_draw.inc、bridge cannon.rs、App Sessionへ8種を接続。0063a050等の原本表を同版SHA付きbattle-inputs.jsonへ追加。古い公式DBにCSV bytesがない場合も使う。005d6740のint* +0xfbを1004byteへ直し、鉄壁寿命はword117へ書く。216命中/676行動/128発射/24複数対象接触がARM64と一致。全8種のUI入力→所有状態→描画命令を402Fヘッドレス実行、発射通番1と鉄壁生成を確認。setup成長全域/全main/GPUの完全一致とは区別する。
- 精霊再召喚も所有battleへ接続済み（actor_summon.py 216条件、既存headless proof）。
- HUD: 専用ステージ名画像・再生産・城HP・精霊可否。battle_hud.pyの318矩形条件。BGM/SE/段数はAppData/user/battle-options.sqliteへ保存。振動なし。通知を上部固定行へ移し押下でCanvasサイズが変わらないようにした。エラー時にメニューhiddenを解除せず、上部へ文面/診断JSONを出す。
- `cargo test --workspace --locked`31件+compile_fail1、全target clippy -D warnings、変更JSの構文検査が通過。日本語ファイルBOMを保持。最終exeのSHAと証跡はresearch/.localのreportと配布フォルダを参照。

次に残るのはニャンピュータ、ボス城衝撃/全体制御、特殊価格ルール、勝敗/時間制限/報酬、全被弾VFX/SE、全mainの連続照合とGPU画素。描画と戦闘の状態/RNGは分離し、原本15.7.2 ARM64/SHA6122e248…を固定する。下の古いメモに残る「精霊/砲/スニャイパー未接続」はこの追補で更新。

---

# 再開メモ（2026-10-26 / 命中本体・C++所有戦闘・画面接続）

0.1.34へ追加。起動中アプリ/プレビューは操作・停止・差替えしていない。GitHub書込なし。既存の性能/API/DB/編成/描画/転送の変更を保持。テスト用releaseは `.local/dist/0.1.34-battle-session/kbcs.exe`、SHA256 `5cc893f13444694af0c93cb2ab12db441ab3f068955a8f80b51f0696dce63e8c`。同フォルダのDLLと一緒に使用する。

[所有状態・API・入力・描画・残り](../../native/kbcs-core/docs/battle-runtime.md)、[命中本体](../../native/kbcs-core/docs/hit-runtime.md)。006e4aec/006e79bc/006e60f0をactor_hit_source.py→export_actor.py→actor_generated.incへ移植（生成586関数）。従来の21段階数値APIはDB用のまま、実命中は入口/回避/無効/対象/妨害/予約を含む原本本体へ接続。Hitsはメタルキラー列と生成通番別寄与者列を所有する。

actor_battle.incが102個体、出現行/再生産、RNG、命中/波動/烈波/反射待ち/爆波と死亡烈波21を所有する。Rust battle::Sessionは版/SHA確認、実DB/編成/宝/コンボ/本能/玉/土台/装飾/param/モデルの解決、排他、描画転送を担当。battle-screen.js→POST /api/battle-session→/frameへ接続し、暗転中に追加画像をデコードする。返却されたHP・個体数・再生産待ちを表示。DELETE/pagehideで解放。JSから個体/財布状態を毎回上書きせず、HUD内部の各論理Fと出撃要求hookで処理する。

重要な入力補正: raw=DB ID+2、unit row=0、読込済みcells6はコスト1/100円/敵報酬、cells7は再生産F、再生産コンボ11。宝maximumEffect=0は品質自体を加算し、章限定/クリスタルを他章へ持ち出さない。Lv1段別攻撃と相手属性に一致する玉を命中ごとに解決。特殊敵城49列とword112の条件、財布加算直後の上限、砲の最大word11/現在word12を区別する。共通魂と復帰演出のファイル/時計を共用しない。

現版JP15.7.2/1507021/ARM64/SHA6122e248…へ命中1,245条件（40代表fixture）、波動32条件/4,800更新/68命中呼出、モーション長135人工条件/12実ファイル、基準点300単一部品条件を局所照合。全251語×102枠/RNG/該当履歴等を比較する。魔女/使徒などの単独特性、コンボ0/99/100、城slot0への城破壊＋クリティカル/渾身も含む。全main連続一致や全姿勢の証明ではない。research/.local/actor-{hit,wave-step}-1572.json、model-contact-1572.json等にDLL SHAと制御境界を保存。

最終releaseで効果編成N000を1,539F、66 batch応答対1,562単F応答で比較し、全個体語/永続HUD/待機/RNG/二次描画記録が一致。一時停止/コマ送り、波動/烈波/小烈波/爆波を含む。ゾンビ実ステージN033は3,920F/最大12敵、潜行11..15/復帰16を確認。通常編成1,920F/106対1,932応答の一致は前のdebug実行ファイルによる記録。レポートはbattle-effects-input-session-report.json、battle-zombie-session-report.json、battle-replay-input-session-report.json。CLIは描画packetを件数へ省略するのでpacket一致とは扱わない。

workspace31試験＋compile_fail1、全target clippy -D warnings、JS構文/差分確認を通過。再実行は `battle-replay --input research/.local/battle-effects-input.json`、batch比較は `python research/verify/battle_session.py --executable .local/dist/0.1.34-battle-session/kbcs.exe --input research/.local/battle-effects-input.json`。GUIを起動・操作しない。大容量実測はresearch/.local、代表値だけnative/testsへ保存。日本語ファイルはBOM付きUTF-8。

次に残るのは精霊再召喚、にゃんこ砲、スニャイパー/ニャンピュータ、ボスの城衝撃/全体制御、特殊ステージの生産回数別価格、勝敗/制限時間/報酬への遷移、全被弾演出/SE。精霊を通常生産で代用しない（エラー4）。モデル境界は初期姿勢を使用しており、可変共有モデルと全mainの連続順序を追加照合する。通常出撃と命中の画面接続済みを、全戦闘完成・実機完全一致と報告しない。以下の「命中本体/GUIが次」は過去の記録。

---

# 再開メモ（2026-10-26 / 烈波・反射待ち・爆波の所有状態）

0.1.34へソース追加。起動中アプリ/プレビュー/UIは操作・停止・差替えしていない。既存の性能/API/DB/編成/描画/転送変更を保持し、GitHub書込なし。全特性の画面接続は未完了。

[二次攻撃の契約・原本・検証](../../native/kbcs-core/docs/secondary.md)。actor_secondary.incをactor.cpp内へ追加し、C++ opaque KbcsActorAreasが烈波/反射待ち/爆波と対象履歴を所有する。Rust actor/secondary.rsのAreasはcreate/Drop、append、step、snapshot、retirement_blockedを提供。既存apply_hit<F,H>へpanic捕捉を共通化した。失敗後はAreasのappend/stepを拒否し、部分状態で戦闘を継続しない。

006d6d04の005d3af8→005d4158→005d4988を同じFでSurges→Reflections→Explosionsの順に呼ぶ。命中は同期callbackで006eaef0/006eb364の引数を返す。SecondaryHit.attack_typeは原本param2（烈波2/爆波3）、hit.kindはparam6（通常0/小烈波2）。既存の21段階ダメージ数値コアだけを接続して入口条件を省略しない。

烈波の周期別履歴と、爆波の5区画別履歴を対象slot1..50の配列へ正規化。原本の生成通番へ変更しない。applied偽でも命中履歴を登録。反射は成功/未履歴/kind1以外/対象212の条件を保持し、239が真なら212/239を解除。反射烈波はその次Fから進める。反射待ちは生成Fに寿命判定を飛ばす。frame/width/damageはparam.tsvから取得する明示入力、Defaultの0を本家設定として使わない。

同版15.7.2 ARM64/SHA6122e248…へ96条件、17424phase更新、1258命中呼出を照合して全個体・効果・履歴・SE/振動・RNGが一致。report=research/.local/actor-secondary-1572.json（actor-test-secondary.dllのSHA）。命中本体、model/param getter、allocator/文字列/SE等は制御した比較で、全戦闘ではない。代表11ケース258チェックポイント（個体は初期値からの差分）を既存Rust1試験へ追加した。

退場待ちは原本の経路差を保持。味方経路は波動state1/烈波、敵経路は波動state2/烈波/反射待ち。波動のsideを追加条件にしない。爆波はこの原本区間の走査対象にないため独自に足さない。actor_owner.pyで512条件が一致、report=actor-owner-1572.json（actor-test-owner.dllのSHA）。代表16件とcallbackエラー/panic後の再実行拒否を同じRust1試験へ統合。bridge23＋compile_fail1と全target clippy -D warningsが通過。生成関数531。外部資料/原本/Ghidraプロジェクトは変更しない。

次は006e4aec/006e79bc本体の入口/回避/無効/対象外・攻撃種別と状態更新を既存数値コアへ接続する。波動005d287c/005d2c18の進行/命中/遮断、死亡烈波21の生成、精霊、実プロフィール、C++全戦闘所有者、陣営の実dispatchとGUI接続も残る。反射待ちstate1の除去分岐は保持したが書込元は未特定（005d4824は描画のみ、009eadc8は初期化時の解放）。原本のbool引数はSTRBなので、Unicornの命中ABI捕捉ではスタック上位byteをフラグへ含めない。

---

# 再開メモ（2026-10-26 / 烈波・爆波生成まで）

0.1.34へソース追加。起動中アプリ/プレビュー/画面は操作・停止・差替えしていない。GitHub書込なし。既存の性能/API/DB/編成/描画/転送の変更を保持する。全特性の戦闘接続は未完了。[状態・原本・照合範囲](../../native/kbcs-core/docs/actors.md)。

C++ actor_emit_areaとRust actor::emit_areaを追加。攻撃callback中にemit_direct→Waves::emit→emit_areaを同じ個体/RNGで同期実行する。生成記録は次の攻撃段より前に所有者へ登録する。烈波48byte/爆波36byteの数値部分と生成の有無を返し、原本末尾の空の履歴木や生ポインタはABIへ含めない。所有ランタイム・寿命/命中/反射の実装は残る。

0044ab70→0044a8d8はabs(span)を直接渡す。+1を補わない。幅0は位置RNG不変、幅1は進む。INT_MINは32bit CNEG後も負のままで非正範囲。味方X−offset/敵X＋offsetを基準に、正のspanでは味方減算/敵加算、非正では逆。烈波174..177/mini211、爆波224..226。12フラグの保存順と、直接命中前のparameter保存を保つ。

research/verify/actor_area.pyで同版15.7.2 ARM64の006e92bc/006ea1c0を先頭から最後まで、2016条件×2回連続=4032更新で照合。全個体・波動200枠/命中履歴・烈波/爆波の生成byte（内部ポインタを正規化）・既存記録・RNGが一致。内部vectorの空/拡張/空き容量も実行。実際の命中内部はapplied/発生元/RNG変更を制御した比較であり、全戦闘の一致ではない。確保失敗も未照合。report=research/.local/actor-area-1572.json、DLL=actor-test-area.dll（SHAをreportへ保存）。代表92記録を既存Rust1試験へ追加。bridge23＋compile_fail1と全target clippy -D warningsが通過。

次は命中006e4aec/006e79bcの入口条件/攻撃種別/回避等と、既存21段階のダメージ数値コアを接続する。波動の進行/命中/ストッパー/反射、烈波005d3af8→006eaef0の履歴木/命中/反射、爆波の寿命/命中、死亡烈波21も残る。死亡烈波は006eb464/006eccf4の行動21に別経路があり、通常攻撃の生成確率やkind0を流用しない。開始時刻battle_death_volcano_timeと専用getter00a98b00/00a98b8c/00a98c18/00a98d30を確認する。

版固定export_actor.pyは524関数。4箇所のgetter→abs→RNGの連続BL命令も同版SOに対して検査する。命中数値だけを先に流用して分岐を省略しない。GUI個体生成への接続、実プロフィール/編成入力の取得、C++所有ランタイム、全体dispatchと論理F順序も未完了。以前の再開メモの「烈波/爆波生成が次」はこの追補で更新する。

---

# 再開メモ（2026-10-26 / 攻撃段・対象選出・直接命中入口・波動生成）

0.1.34のソース追加。起動中GUI/プレビュー/画面は操作・停止・差替えせず、GitHubへ書込なし。全特性の戦闘接続は未完了。[原本・更新順・契約・検証範囲](../../native/kbcs-core/docs/actors.md)。既存の性能改善、DB/編成/描画/転送の変更を保持した。

C++ actor_attack（006d8584/006d8cf8）、actor_emit_direct（006e92bc/006ea1c0の直接命中区間）、actor_emit_wave（続く波動生成）を追加。Rust Pool::attack→同期callback→actor::emit_direct→Waves::emitで同じ個体配列/RNGを借用できる。命中callbackのエラー/panicで後続段を止める。C++例外を境界外へ出さず、Rust panicはC ABIを抜けてから再開する。途中の戦闘は継続しない。

同版ARM64へ攻撃段/対象選出1888、直接命中入口864、波動生成までの連続区間720の計3472条件が一致。実測はresearch/.local/actor-{attack,direct,wave}-1572.json（各DLLのSHA・制御helperを保持）。代表48/29/19件は既存Rustの1試験へ統合。命中関数006e4aec/006e79bcは引数捕捉とapplied/状態/RNG更新の制御であり、命中内部の一致とは区別する。波動は200枠の全byte・51×200命中履歴・RNGを比較。無効段の関数returnも終端とした。bridge23試験＋compile_fail1、全target clippy -D warningsを通過。Rust検証結果は集計actor-validation-1572.jsonへ保存。

攻撃段数は21/121/122の先頭からの分岐を保持。最初0なら段数0、2段目0なら3段目非0でも段数1。味方は最初の一致段だけ、敵は同時刻の複数段をcallback後に再確認。最終段では対象なしでも基準12→待機18と正の115減算を先に行う。単体は対象のX±14の選択ソート→先頭同率の数でRNG、範囲は0〜50の走査順。1候補でもRNGを省略しない。待機→攻撃2の同じF更新も前回から維持。

直接命中の12抽選は対象間で共有。味方の直接命中へ敵専用の毒撃9/遅延11を渡さず、後続効果用には元の12値を保存する。parameter218は味方のみ対象走査前に取得。appliedの時だけ対象96を更新し、味方198/対象行動14の別経路も保持する。kind0/rate100の直接命中入口だけで、波動等の別攻撃種別を流用しない。

波動は効果段フラグ有効かつ確率39>0で乱数100を先に取得。成功ならkind/stateの両方0の最初の枠を確保し、満杯でも抽選は消費。初期kind/stateは味方1/敵2、miniは182==1。レコード48byte、flags順は抽選順と異なる[0,1,2,3,4,6,8,7,5,9,10,11]。予約3byteを残し、当該枠の51対象の履歴だけを解除。同版SOの002b2820=1/002b2938=2をexporterで検査する。

次は同じ発生関数の烈波（味方006e9768〜/敵006ea62c〜）と爆波（味方006e999c〜/敵006ea860〜）。00a98838、00a988c4/00a98950、00a989dc、00a987f8と、00a98f70、00a98ffc/00a99088の取得を追う。Ghidraが省略した0044ab70→0044a8d8の引数を実命令で復元し、座標の向きと抽選範囲、元の12値/parameterを保持する。現在は直接命中→波動までで、烈波/爆波のRNGはまだ進めていない。全発生をつなぐ前に画面へ生成を接続しない。

その後、命中006e4aec/006e79bcの入口条件/攻撃種別/回避等を数値カーネルと連結し、波動の進行/命中/ストッパー/反射、死亡烈波21、効果所有者の寿命/解放保留、精霊、砲・スニャイパー、実プロフィール生成とC++所有ランタイムを進める。全体の行動dispatchは陣営0を直接006eb464、陣営1を006eccf4→unit-modeなら006eb464へ委譲する。mode別抽出カーネルの検証を全体dispatchの検証と混同しない。

---
# 再開メモ（2026-10-26 / 敵KB終了・死亡・潜行/攻撃待機）

0.1.34へソース追加。起動中アプリ/プレビュー/画面を操作・停止・差替えしていない。既存API/描画/転送/DB/編成は維持し、GitHub書込なし。直近の指示は「全特性を原本の条件・分岐を見落とさず実装」「再開」。全特性の戦闘接続は未完了。

[状態コアの契約・原本・再実行](../../native/kbcs-core/docs/actors.md)。actor_enemy_knockbackは敵3の移動/終了、ゾンビキラー/有限・無限蘇生、盾再生成、寄与者の撃破数・報酬選出、スコア/記録/財布要求。actor_retireは通常死亡4の時計・解放保留、味方の同ID確認/生産印解除、砲待機短縮要求。actor_intentは両陣営の行動後の待機/寿命/潜行開始と城への潜行終了。actor_attack_waitは陣営別の待機1から攻撃2等への遷移。C++と安全なRust Pool入口を追加した。

JP15.7.2 / 1507021 / ARM64 / SHA6122e248…の実命令へ、敵KB720・通常死亡640・行動後判定432・攻撃待機864の計2656条件を比較し一致。全個体と該当する報酬/記録/スコア/通知/生産/砲待機、RNG不変を確認。元DLLのSHAと制御getter/入口レジスタ等はresearch/.local/actor-{enemy-death,retirement,intent,wait}-1572.jsonに保存。代表値はRust既存の1試験へまとめた。追加前からの歩行3216/味方KB1152/敵ふっとばし3456も同版と一致済み。fixture再投入を含むworkspace31＋compile_fail1、その後のbridge23＋compile_fail1、全target clippy -D warningsを通過。

重要な接続順: 出現→clock→個体ごとのbegin/行動（味方全体→敵全体）→intent→各個体のattack_wait→同じFの攻撃2時計/段発生/対象選出→命中→保護/HP/死亡集計/react。待機1で時計を進めても、2へ移った同じFに攻撃時計を更新する。敵の加算玉243を解除するのは敵の全51枠走査後。寄与者通番は重複を除かず、空き枠への一致も原本どおり数える。retireのblockedは攻撃効果の所有者/寿命から求め、単なる表示OFFで解放しない。

次は006d6d04の攻撃2（味方006d8584〜、敵006d8cf8〜）の段発生・対象列挙/単体抽選と、006e92bc/006ea1c0→006e4aec/006e79bcを接続する。単体選択の同距離候補数1でもRNGを省略しない。城/攻撃対象限定・能力/種別の入口分岐を残す。死亡烈波21、所有効果の寿命/解放保留取得、精霊009f4a74、波動/烈波/爆波・砲・スニャイパー、実プロフィール生成と画面の所有ランタイムは未接続。

全体の行動dispatchはmainが陣営0を直接006eb464、陣営1を006eccf4へ渡し、後者だけがunit-modeで006eb464へ委譲する。既存の借用walk/begin/retireはmode別抽出の検証入口。全体接続でunit_modesだけを見てdispatchを決めない。実ステージのmode取得/呼出経路と連続実行を確認してから接続する。

版固定のexport_actor.py→actor_generated.inc/actor_rom.inc。原本の分岐・getter関係を保持し、配布にPython/SO/Unicornを要求しない。Context未解決エラーは戦闘を停止する。研究原本/旧全件検証3658条件は保持。日本語ファイルのBOMはcargo fmt後に復元する。

---
# 再開メモ（2026-10-25 / 個体の生成・特性・被弾後状態）

0.1.34へソースのみ追加。配布アプリ/起動中GUI/プレビューは差替え・操作していない。HTTP戦闘API/描画/ワイヤ/DB/編成を維持し、GitHub書込なし。直近の指示は「全特性を順に、原本の条件・分岐を見落とさず実装」「再開」。全特性の戦闘接続は未完了であり、ここを完成扱いしない。

[状態コアの設計・入力・再実行](../../native/kbcs-core/docs/actors.md)。actor.cppは版固定Context、actor_generated.incはexport_actor.pyによる原本分岐の出力、actor_rom.incは同版定数。Rust actor::Poolは原本251語×2陣営×51枠を所有し、各入口だけ借用する。将来のC++所有ランタイムとは別。配布時にPython/SO/Unicornは不要。

009f1e64全体の構築、数値ローダー、通常/遠方/全方位の捕捉、属性/呪い、12種の抽選、7妨害と耐性/装飾/超賢者、妨害等の時計、個体更新前の保存/解除、モーション時計/行動復帰、被弾予約/城無敵、バリア/盾の吸収、HP/再生産遅延/生存、KB/ふっとばし/ワープと魂の共通遷移を追加した。本能・玉・宝・コンボ・装飾・モデル等は明示した解決済み入力。編成からこれらを作る取得経路全体は未接続。

JP15.7.2/1507021/ARM64、SO SHA6122e248…を検査して照合。全原本を含む生成3658条件は既存のall-assets-final記録（その時点のDLLのSHAを保持）。最終DLLでは境界生成248、捕捉/属性/抽選/妨害、時計48更新、モーション1584、復帰264、共通遷移720、更新前192、被弾予約58、保護864、HP1068、KB804、原本ローダー味方4/敵804枠が一致。全102枠×251語、該当区間の乱数/SE/表示要求/集計要求を比較する。ローカル入口・外部getterを制御した検証で、全フレーム戦闘の証明ではない。

workspace31試験＋compile_fail1、全target clippy -D warningsを通過。代表値の再投入はRustの1試験actor::tests::native_actor_statesへまとめた。実測記録research/.local/actor-validation-1572.json、actors-1572.json、actor-{loaders,protection,health,reaction}-1572.json。大きい全原本報告はresearch/.local、代表fixtureのみnative/testsへ保存。

次は個体の全行動/攻撃のスケジュール、命中入口006e4aec/006e79bcの全条件と型別攻撃、死亡/KB/蘇生/潜行/精霊、波動/烈波/爆波等の発生・伝播をつなぐ。006eb464/006eccf4の未移植部分、009f4a74の精霊/連続生産、編成/本能玉等の実プロフィール生成も残る。prepareだけの成功や、任意の簡易移動・攻撃で穴を埋めない。

接続順は006d6d04を守る。各論理Fの出現→clock→個体ごとのbegin→行動→命中/予約→保護→被弾表示/RNG→health→HP0丸め/死亡集計→react→生産待ち等。healthのprevious_hpはKB比較に保持。バリア等の妨害差戻しはbeginで保存した残りへ戻す。生存の抽選は非致死/使用済みでも消費する経路がある。死亡時表示は30枠の空きでRNG消費が変わるため、表示OFFでも演出の状態/確保を省略しない。画面への生成は既存HUDバッチの最後のrequest_slotを処理する接続にせず、論理/入力tickの内部へ置く。

word7=maxHP/8=currentHP、73=生存率/77=使用状態、246=遅延確率/248=予約遅延。モーション境界は00a9490cのモデル・城を含む取得経路から解決する。Ghidraの省略引数/void戻り値を実命令で補った箇所はexporterとactors.mdへ記録。00a9490cの取得経路本体はまだ移植していない。

---
# 再開メモ（2026-10-25 / 出撃・敵出現のC++入口）

0.1.34へのソース追加。実行中GUI/プレビュー4850等は操作・停止・差替えしていない。ユーザーの実測は戦闘API28.5ms/p95 37.2ms。今回の戦闘API/描画/ワイヤ/DB/編成に変更なし、GitHub書込なし。

native/kbcs-core/include/kbcs_production.h、src/production.cpp、bridge::productionを追加。[契約・原本との差・確認範囲](../../native/kbcs-core/docs/production.md)。009f1e64の枠探索/初期座標/レイヤー抽選、ボス位置、00aa08f8→0058c05cの再生産値、009f4a74の通常生産成功後の資金/回数/待機、再生産時計をC++へ移植。敵はstage_tick→実構築callback→全体/行RNG→commit→seenを単一入口にした。敵城初期化は失敗でも最初の一致行だけを消費する。

15.7.2 ARM64/SHA6122e248…の実命令37条件をresearch/verify/production.pyで採取。production-vectors.jsonと既存連続出現3×3tickをRustの2試験で比較。workspace30試験+compile_fail1、追加後の関連2試験、全target clippy通過。完全な個体構築の照合ではない。記録はresearch/.local/production-1572.json。

次は009f1e64の能力/本能玉/バリア・盾/初期行動と、009f4a74の精霊・連続生産。構築callbackをprepareの成功だけで返さない。現在のGUIは従来どおり個体未接続。画面へ接続するときはC++所有ランタイムの各論理F/入力tick内で実行する。まとめたbattle_screen::frameの最後のrequest_slotだけを処理すると時刻がずれるため、その接続はしない。

---
# 再開メモ（2026-10-25 / 0.1.34 戦闘APIの確保・転送）

最新版は`.local/dist/0.1.34-release/kbcs.exe`、プレビュー4850/PID6276。`.local/publication-0.1.34.json`にSHA/検査結果。初期0.1.34（4848）と非圧縮最終試作（4849）は比較用で、確認には4850/releaseを使う。ユーザーが操作する指定を維持し、このターンはUI入力・画面切替・再読み込みを行っていない。既存アプリ/プレビュー・公式DB・編成は維持、GitHub書込なし。

/api/battle-frameのpacked:trueは明示LEのKBF1。大きな本文はcompressed:trueの時だけgzip可逆圧縮のKBG1にできる。32バイトの計測ヘッダーを残し、JSは機能検出したDecompressionStreamで本文を展開、TypedArrayで借用する。JSON/非圧縮入口は維持。Rustの粒子出力と背景paintの最大領域（後者約3MiB）を所有者ごとに再利用し、毎Fの大きな確保/0埋め/解放を省く。C++の式・更新順・乱数・ABI3は変更しない。[仕様と計測](../../crates/kbcs-app/docs/performance.md)。

PR000の1000要求（旧0.1.33/新0.1.34、HTTP単体）でp95 21.20→14.14ms、最大326.56→26.04ms。転送は約195KB→23KB。追加1199要求の受信最大28.29ms、展開/復元込みp95 23.27ms、最大44.72ms。300ms級の本文待ちは再計測で0件。実WebView/GPUのFPS保証ではない。state/layout/scene216ケース一致、関連28試験+compile_fail1、clippy/JS/release/配信8ファイル一致。原記録.local/checks-0.1.34.json、.local/profile-wire-tail.json。圧縮前記録も保持。

個体生成・移動・攻撃・砲撃等の未接続項目は従来どおり。次にユーザーが新しいアプリを操作する場合も、こちらから操作せず、依頼された計測を記録する。

---
# 再開メモ（2026-10-25 / 0.1.33 FPS観測と統合API）

起動中0.1.32をユーザー依頼で確認し、更新APIと背景APIの直列待ちを確認。/api/battle-frameへ統合、シーンごとの読取専用DB接続を再利用。初回0.1.33の78出力が旧経路と一致。静止背景のcached指定/段数変更保証を加えた最終ビルドは`.local/dist/0.1.33-final/kbcs.exe`、clippy/release通過。初回0.1.33のプレビューは4847（PIDは.local/preview-0.1.33.pid）。既存4845/4846等は維持、GitHub書込なし。

最後の指示は「私が操作します、あなたは記録だけ」。以後こちらからUI入力/再起動/画面切替はしない。初回`.local/dist/0.1.33/kbcs.exe`のGUIでユーザーがPR000を操作中。旧0.1.32 GUIは比較前にこちらが一時停止した。最終版GUIへの差し替えやcached指定のAPI追加試験はしていない。ユーザー操作中の負荷を乱さず、次の指示を待つ。

記録は`.local/runtime-observations-20261025.json`、配布記録`.local/publication-0.1.33.json`。表示13点は22.0〜30.1FPS、中央値28.0、API21.7〜60.3ms。30FPSの安定化は未完了。瞬間表示の記録であり、操作条件固定のA/B試験ではない。[性能設計](../../crates/kbcs-app/docs/performance.md)に関数関係と未検証範囲を記載。

---
# 再開メモ（2026-10-25 / 0.1.32 戦闘の常時操作・計測と負荷分離）

最新アプリは`.local/dist/0.1.32-final/kbcs.exe`、プレビュー4846/PID21716。旧4845/PID9776は維持。画面確認はユーザー担当で、今回はこちらから画面操作・スクリーンショット検査は実施しない。公式DB・編成の再構築/変更、GitHub書込なし。mainの既存公開済みcommitは56914943。今回の変更は未コミット。記録は`.local/publication-0.1.32.json`。

戦闘viewbarへ常時表示の操作/情報バーを追加。ホスト停止、1F/10F、オプション、段数/枠切替、カメラ初期化、診断JSON、準備へ戻る。FPS、進行比、API/描画提出時間、遅れF、CPU/RAM、画像/要求キュー。ネイティブcontrol10による手動更新は速度アイテム設定を保ったまま1更新1F。停止はネイティブオプションと区別し、停止中のカメラは0F。既存ABI3を維持。詳細は[性能設計](../../crates/kbcs-app/docs/performance.md)。

要求ごとのスレッド作成を固定UI/計算/I/Oワーカーと上限64キューへ置換。容量つきLRU、シーン/モデル/音源の個別ロック、session単位の背景状態。型付き借用FrameからJSONへ直接出力し、同粒子群のローカル姿勢を共用。ライブ背景を専用WebGL面へ、HUDは透明2Dへ分離し、コピー/毎Fのcanvas再確保/画像の二重デコードを削減。暗転は開始BGMだけを待ち、後の曲は取消可能な別取得。途中BGM切替の本体接続は未実装。

旧版とPR000/N000各0〜30Fの描画命令62件が一致、独立session16要求一致、3倍中1F一致。API往復中央値はPR000 60.53→45.74ms、N000 12.25→12.75ms。画面FPS改善や全ステージの速度保証ではない。関連試験計27件+compile_fail1件、clippy、最終JS5構文、release、配信7ファイル一致を確認。原記録`.local/checks-0.1.32.json`。0.1.31以前の個体生成・移動・攻撃等の未接続項目は引き続き残る。

---
# 再開メモ（2026-10-25 / 0.1.31 背景・カメラ・音源）

最新は`.local/dist/0.1.31/kbcs.exe`、プレビュー4845/PID9776。PR000のルートを確認用に開く。旧4844/PID19572と旧アプリ、公式DB、ユーザー編成は維持。GitHub書込/公式DB再構築なし。`.local/publication-0.1.31.json`にSHA/検査記録。画面はユーザーが確認し、こちらは操作/スクリーンショット検査を行わない。

battle-screenは開始時1枚の背景から、C++の論理frameに合わせたscene API/共用演出Runtime/WebGLへ接続。停止中はframeを変えない。盤面のドラッグ、ホイール/ピンチでパン/拡縮。スロット領域では従来のページスワイプ/ホイール。sceneGestureViewをDB試写と共用し、ワイド幅の入力倍率を修正。005cb0e0の上限10000を受け戦闘はzoom<=1、DB試写は<=2を維持。個別の大型城上限・Android慣性の全再現は残る。

[本家の音源経路](../../research/docs/audio-1572.md)を静的追跡。00ac8f8c→00458038がSound_setting、00458974がSE準備、00459170がBGM/SEの再生入口。APK assetsのsndNNN.ogg/cafを先に確認し、欠測時はgetFilesDirのNNN.ogg/caf。0055aad0がAAssetManager_open→fopen。004222e0はPONOS配信ZIPのURLを組む。Android/JNI/本家通信の実行検証ではない。

ユーザー指定assets commit8e9dca31e3845e3c7dcdc515e6c85d5480538fc0の検証済みcurrent→manifest→index→Sound_settingからBGM18 Oggを採用。SE9 CAFは混ぜない。scripts/sync-stage-music.pyで生成、既存MP3補完は残す。stage_media::audioが実MIME/size/SHAを確認しAppData/assets/music/<曲のcommit>へ保存。PR000開始曲193も対応。暗転中に曲を取得し、終了/取消でBlob URLを解放する。

音源追加のassets buildId変更でも、戦闘HUD画像/imgcutの全12SHAが現在DBへ一致すれば利用可能。POST /api/asset-hashesで参照。最新索引の12SHA一致も確認。変換器/スキーマ/ABIは13/8/3を維持。今回追加BGMは公式DBの再取り込み不要。

workspace25テスト+compile_fail1、clippy、4JS構文、入力座標/境界/解除の最小Node検証、releaseを通過。HTTPで18曲26,140,867bytes/実MIME/原本SHA、193のキャッシュ再利用、旧MP3、PR000背景の0→60F、同じ60Fでカメラ変更、1422幅、ズーム上限を確認。前回のABI3に対しService試験だけABI2を期待していた箇所も修正。画素一致/聴覚確認はしていない。

個体生成・移動・攻撃・生成成功時の残高/再生産確定・砲撃/ニャンピュータ/スニャイパー、停止メニューの特性アイコン行/離脱確認と返還/SE出力、ステージ特殊上書きは引き続き残る。背景やBGMが動くことを戦闘ランタイム完成と混同しない。

---
# 再開メモ（2026-10-25 / 0.1.30 戦闘HUDの原本照合）

最新アプリは`.local/dist/0.1.30/kbcs.exe`、プレビュー4844/PID19572。旧4843/PID23756と旧アプリ・編成・公式DBは維持。GitHub書込なし。配布記録は`.local/publication-0.1.30.json`。ユーザー指定で画面操作・スクリーンショット確認は行わず、ARM64局所照合、Rustテスト、構文、release、HTTP経由の実出力で検査する。

ユーザー訂正: 財布MAXは点滅せず黄色固定、LEVEL8を表示する。砲の準備完了は3表示更新ごとの2相、財布昇級後の金額だけは13からの短い白点滅。空き枠uni cut0、1段縦スワイプ（25pxと原本整数角度）、PCホイール、アイテム説明/拡縮、OFF→2倍→3倍→OFFを接続。UIの画面高640・可変幅、C++の二段カメラ-51、画像下端から680までの地面描画を追加。HUD/scene POD拡張でABI3。

停止メニューは008f9e20/008fb5f4の戦闘専用img100へ置換し、配置/音量4段階/段数/閉じる/キャラ確認のボタンをC++へ集約。img015がキャラ確認/選択枠。BGMはstage-audio、ヘルプはユーザー指定URL。キャラ確認の全特性アイコン行006a4e9c、離脱確認/返還008ff4a8→00887e18、SE実出力は残る。現在の離脱は生成前の準備へ戻るだけで、本家所持品を消費しない。

research/verify/battle_controls.pyとbattle-controls-vectors.jsonを追加。スワイプ8、カメラ2、停止描画960/1280、金額15、砲2相、財布MAX、音量テーブルを制御ARM64で確認。既存native_screen_witnessesへ統合し、MAX静止6時計・説明待機・確認終了時の段数復元も検査。HTTP配信PNG6枚の元SHA、1422幅/1・2段カメラ、財布6時計、砲2相、速度循環を検査。全入力/全戦闘/GPU画素一致の証明ではない。[原本と境界](../../native/kbcs-core/docs/battle-screen.md)、[UI](../../ui/docs/stage-sortie.md)。

敵/味方の生成、移動、攻撃、生成成功時の残高/再生産確定、砲撃・ニャンピュータ・スニャイパー本体、全特殊ステージ上書き、カメラ操作/背景連続演出は引き続き未接続。実装済みDB/計算と完成戦闘セッションを混同しない。

---
# 再開メモ（2026-10-25 / 0.1.29 戦闘画面の初期基盤）

最新アプリは`.local/dist/0.1.29-final/kbcs.exe`、プレビュー4843/PID23756。旧プレビュー・ユーザー編成・公式DBは維持、GitHub書込なし。配布情報は`.local/publication-0.1.29.json`。HUD3枚が既存DBのsource_fileにない問題を修正し、検証済みPNGを同梱。releaseビルドとHTTP配信SHA照合を通過。ユーザーが画面確認するため、追加の画面操作・スクリーンショット確認は行わない。

出撃後のHUDと暗転を追加。ユーザーへ向きを確認し、「幕が左へ抜け、右側から画面が見える」原本通りを採用。006994e8の24F分全頂点を実ARM64へ比較。005d026cのページ切替24更新、009a6f44の四辺を含む7境界、財布/収入/昇級費6条件、砲充填4条件も局所比較。RustのC++照合テストとclippyを通過。全戦闘の照合ではない。

battle_screen.cpp→bridge→/api/battle-screenを追加。解放後5回の入力更新で生成要求、長押し14更新で説明表示と解放の抑制、1/2段・ページ拡縮と描画順を実装。速度は経済・充填の論理更新だけを1/2/3回進め、入力待ちを短縮しない。全必要素材のデコード完了まで全面暗転、その後C++頂点で退出する。ステージのサイドバーは戦闘中に非表示・一時閉鎖し、戻ると復元する。

キャラ・敵の実生成、移動、砲撃本体、再生産待機の開始/確定、ニャンピュータ・スニャイパーの実行は未接続。生成成功を仮定して残高を消費しない。一時停止はKBCSの再開/段数/ページ/準備へ戻るメニューで、本家全オプションの配置移植ではない。特別なスロット・スワイプ・可変ズーム・固定編成/施設上書き・連続背景演出/BGMも残る。[原本と境界](../../native/kbcs-core/docs/battle-screen.md)、[UI](../../ui/docs/stage-sortie.md)。

---
# 再開メモ（2026-10-25 / 0.1.28 出撃準備と共通計算）

最新アプリは`.local/dist/0.1.28/kbcs.exe`、プレビュー4841/PID14452。旧プレビュー・ユーザー保存編成・公式DBを維持。GitHub書込なし。実行ファイルと確認結果は`.local/publication-0.1.28.json`。0.1.28 releaseビルド・JS構文・差分空白検査を通過。画面で中央の操作、右の詳細、6アイテム、出撃有効、敵一覧の初期折りたたみを確認。console errors 0。

ユーザー確認により、コンボなし通常最大城体力は236000で正しい。施設78000＋城開発116000＋日本/未来のお宝42000。城開発Lv1〜30を編成単位で保存する。施設・お宝入力→Rust bridge→C++の経路で統一。原本JP15.7.2 ARM64の城体力・スニャイパー・速度・出撃制限・生産コストを追跡。制御したARM64呼出52件、C++照合の代表テストとclippyを通過。全フレーム戦闘の照合ではない。[計算設計](../../native/kbcs-core/docs/battle-support.md)。

出撃準備は左がマップ内ステージ一覧、中央が簡易情報・冠・折りたたんだ敵一覧・使用編成・アイテム・出撃、右が詳細情報・有効な制限・特殊条件・固定編成・背景/城/BGM試聴。DBのstageRulesHtml/stageMediaHtmlを再利用。原本の最後に一致する制限行をC++へ渡す。禁止枠にはimg029 cut139を重ね、編成編集にも同じmap/stage/crownを渡す。[出撃準備](../../ui/docs/stage-sortie.md)。

編成一覧は名前を追従し「新しい編成/」を除去。キャラ一覧は整列し表示形態を切替可能。本能は存在するキャラだけ表示、本能玉は原本のユニット別容量0/1/2へ制限（古い超過設定を一括変更しない）。全ページにHome/戻る/次へ/再読み込み、両サイドパネルを用意し、初回は表示。狭幅で両パネルを重ねない。[編成](../../ui/docs/formation.md)。

出撃ボタンは暗転中の画像デコード→C++の0F盤面まで。継続戦闘、移動/命中/生成/資金/アイテムの時計、固定編成・施設上書きや可変生産条件の実適用は未接続。現在のsnapshotを完成済み戦闘ランタイムとみなさない。次の実装は原本の初期化と状態管理を確認してから進める。

---
# 再開メモ（2026-10-24 / 0.1.25 編成の形態・描画）

最新は`.local/dist/0.1.25/kbcs.exe`、プレビュー4837/PID18728。ユーザー保存先は共通AppData。旧プレビューは停止していない。GitHub書込・公式DB移行なし。

追加時の形態はunit.formsの最大index。超激の第四形態は基礎Lv60未満ではresolveFormationMemberで第三形態として扱う。保存済みの手動選択を一括変更しない。

アイコン縮小の原因はcatalogにiconCropがない場合の余白付き画像全体の縮小だった。常にuni.imgcut=[9,21,110,85]を切り抜き、SVG imageの自然寸法を使う。番号背景は00a82394どおり10枠を固定背景として先に描き、キャラだけを移動する。

名前欄は00a71320→00a25380→00a2386c、00a82394→00a254bc→00a24618を確認。img029 cut120/121、147×27、y=100、中心x=badgeX+73、文字上端102、18px白、最大幅125で横圧縮。ブラウザフォントの画素一致は未保証。出典と注意は[編成](../../ui/docs/formation.md)。

構文・最大形態/単一形態/配列順/基礎Lv59・60の最小検証とreleaseビルド済み。画面確認はユーザー希望により最低限。

---
# 再開メモ（2026-10-24 / 0.1.24 編成の初期値と解放条件）

最新アプリは`.local/dist/0.1.24/kbcs.exe`。更新プレビュー4836/PID21056。以前の4834を停止・上書きせず、新版を別ポートで起動した。ユーザー保存領域は共通AppData。GitHub送信なし、公式DBの再構築なし。

左下img029 cut132は全キャラ解除へ修正。ファイル操作はスロットメニューのみ。追加時は基本/EX/レアがLvと＋上限、激レア50＋0、超激レア60＋0、伝説レア50＋0。特殊上限は守る。本能・超本能は全レアリティで収録済みを初期最大。

超激の超本能と第四形態は基礎Lv60から有効（ユーザー回答、＋値は含めない）。Lv59以下では第四形態を第三形態、超本能を0として扱う。設定値を保持し、60に戻すと復帰する。共通のresolveFormationMemberで実効値を取得する。今後の戦闘入口も設定値を直接使わず同関数を通す。通常の本能は無効化しない。詳細は[編成](../../ui/docs/formation.md)。保存済みレベルや本能の一括書換は行わない。

最小検証は初期値（各レアリティ・特殊上限・本能最大）、基礎Lv59/60境界、＋値の除外、設定保持、JavaScript構文、releaseビルド。画面の詳細確認はユーザー希望により省略。

---
# 再開メモ（2026-10-24 / 0.1.23 編成修正）

編成上部の10点を削除。原本15.7.2 ARM64の00a72648/00a7888c/00a82394を追い、周辺配置、img023金額、uni.imgcutを修正。長押し5更新、40%拡大・半透明、挿入並替え、整数で戻る処理を実装。詳細と未移植範囲は[編成](../../ui/docs/formation.md)。スクリーンショットから補った座標を原本照合済みとした旧説明は訂正。

最終アプリは`.local/dist/0.1.23-final/kbcs.exe`。4834/PID20932は中央揃えの最終整数修正前の0.1.23。停止・置換・再起動の操作が自動承認レビューに拒否された（blocked by policy）ため、勝手に別経路で差替えない。ユーザー指定で画面確認は最低限に限定。GitHub送信なし。DB移行・再取得は不要。研究の中間コピーはresearch/.local/formation-native、既存Ghidraプロジェクトと参照repoは変更していない。

---
# 再開メモ（2026-10-24 / 0.1.20）

最新は`.local/dist/0.1.20/KBCS.lnk`。通常保存先はAppData/KBCS、既存GitHub assetsの原本をassetsへ永続保存。詳細は[persistent-assets](persistent-assets.md)。同一原本/変換器版では構築済みDBを再利用し、アプリ版だけで再取得/再構築しない。20＋compile_fail1、clippy、実GitHubのキャッシュ更新確認を通過。

試験4827/PID9264は.local/update-cache-proofのDBコピーで動作。通常保存先のユーザー更新（作業開始時PID20068/update.lock）は終了しておらず、ロックを勝手に削除していない。旧4817/4824/4826とアプリも維持。今後の停止前に実行元/引数/所有者を確認する。今回GitHubへ書込していない。変更は作業ツリーに残す。

---

# 再開メモ（2026-10-23 / 0.1.19）

素材読込を改善済み。[変更と測定](material-loading.md)。最新アプリは`.local/dist/0.1.19/KBCS.lnk`、プレビューは4826/PID5636。4817は旧版なので混同しない。選択中の種類の軽量一覧だけを読み、その他のmanifestは対象1素材を解析する。再選択時の画像と解析結果を小さくキャッシュする。schema8/importer12と既存DBを維持。測定/公開記録は`.local/publication-0.1.19.json`。

既存19＋compile_fail1、clippy、代表manifest/全素材一覧の旧版比較、実ブラウザーで味方/敵/その他/形態/再選択を確認。GitHubへ新規送信していない。前回評価対応と今回の変更は作業ツリーに残る。旧アプリは閉じていない。

---

# 再開メモ（2026-10-23 / 0.1.18）

最新は`.local/dist/0.1.18-final/kbcs.exe`、schema8/importer12/ABI2/ruleset1507021。4817は旧0.1.17のまま。検証プレビュー4824は初期0.1.18ビルド。最終版への差替え/追加起動は自動承認レビューで拒否され、実行ファイルの作成まで完了。DBと旧snapshotは保全し、再取り込み不要。実PID/SHAは`.local/publication-0.1.18.json`。旧0.1.17のテストアプリは閉じていない。

[外部評価対応](review-20261023.md)を参照。ARM64連続3tick×3条件でcommitの過剰再検査を修正。キャラ検索/敵検索・詳細/ステージのHP・攻撃を共通C++へ接続。一覧スクロールと評価中の検索/候補/保存/索引生成の問題を修正。workspace19＋compile_fail1、clippy、全DB回帰、索引全6476面差分0を確認。

盾HP・所持金・時間/コスト等の表示補助、モーション評価、個体構築全体と戦闘状態の統合は残る。新規のGitHub Pushは行っていない。前回のmain/da4fff44は送信済み。今回の修正は作業ツリーに残す。再開時は最新の指示を読み、範囲を推測で拡大しない。

---

# 再開メモ（2026-10-23 / 0.1.17）

その他モーションを通常プレビューへ反映済み。最新は`.local/dist/0.1.17/kbcs.exe`、schema8/importer12、ABI2/ruleset1507021。4817/PID13584。DBは`C:/Users/ABC/AppData/Local/KBCS/official/jp-c59d3381716e75249c6ebda4a38a00da42915248a1e7ee6849af2a1e011769ca.sqlite`。旧snapshotを保持。詳細は[effect-motion-workspace.md](effect-motion-workspace.md)。

味方・敵・その他で同じエンジン。433モデル中386件を解決、47件は素材対応未確認。波動/烈波/爆波の既存一連演出とLv、生き残り・バリア・城バリア・悪魔シールドを追加。ファイル/分割/パーツ操作を流用。テスト18＋compile_fail1、代表16素材と既存演出境界72件、実ブラウザー確認済み。

姿勢評価のC++移植と完全な戦闘状態は残る。外部ホスティング・PC終了は未実施。ソースのGitHub Pushは2026-10-23のユーザー指示で承認済み（再確認不要）。試験4822は停止済み。再開前に新規の指示を確認し、広い追加機能を推測しない。

テスト用Windowsアプリは`.local/dist/0.1.17-app/KBCS.lnk`。選択パーツの黄色い枠は初期OFFで、右の「選択枠を表示」で切り替える。調査はREADME、docs/architecture、docs/data、各領域docsから開始する。Gitへはソース・設計・検証スクリプト/fixtureを含め、ローカルDB・実行ファイル・解析キャッシュは含めない。

---

# 再開メモ（2026-10-23 / 0.1.16）

モーションの初期ワークスペースを公開済み。最新は`.local/dist/0.1.16/kbcs.exe`、schema8/importer10、ABI2/ruleset1507021。通常previewは4817/PID15960。DBは`C:/Users/ABC/AppData/Local/KBCS/official/jp-71e42b90c517b9103aa1a9dcedf592fb2b380646547b6d7f7fcba1f493124423.sqlite`。旧snapshot/ポインタを保持。最新の関数・UI・範囲は[motion-workspace.md](motion-workspace.md)。

- ステージ検索の出現敵列は初期非表示。右の表示設定で切替可能。
- キャラ/敵の再生、1F/10F、反転/ズーム、パーツの個別/子/単独表示、読込原本と分割画像一覧、KB→通常/専用魂を追加。
- モデル2950件・アニメーション11744件・スプライト2950枚をオフライン保持。PNG選択はimgcutの制作PCパスを使わず、現版と同じstemを採る。
- ユーザーは「最近モーションは変わっていないので軽めの検証でよい」と指示。代表6素材120姿勢と実ブラウザーを確認。workspace18＋compile_fail1、clippy、CLI/release、importer10のステージ全件回帰が通過。
- 姿勢評価は既存JSの整数評価器。C++はKB/魂の時計と変位を共用。姿勢C++化と戦闘全状態は今後。既存のnative解析資料は版/SHAを混同せず保全する。
- ブラウザー検証はCUAのみ。Windows Store PythonはAppDataが仮想化されるので、通常DB確認はbundled Pythonを使う。

# 0.1.15までの再開メモ（履歴）

0.1.15で全29系列の閲覧DBとUIを通常保存先へ公開済み。DB完成＋ローカル公開の依頼は完了。GitHubへの書込・外部ホスティングは行っていない。

## 現在の動作版

- `.local/dist/0.1.15/kbcs.exe`、ABI2 / ruleset1507021、schema8 / importer9。
- 通常プレビューは127.0.0.1:4817、PID18548で非表示起動。終了/更新時は実行パス・preview引数・窓を再確認。試験用4820/4821/4822は実行元を確認して停止済み。
- 実使用DB：`C:/Users/ABC/AppData/Local/KBCS/official/jp-fb87935b9bee241e538b0222a3c4af6739a54c16d6a47573d1f809a7cb165411.sqlite`。旧DBは保持、前ポインタは`.local/current-before-0.1.15.json`。
- 同版原本6333戦闘定義62488行、一覧1298マップ6476面、報酬12194行、候補関係3088件。未来編144面315スコア報酬、固定編成10preset、本能玉164報酬名/3層アイコンを接続。
- `research/verify/all_stage_database.py`が全定義/原本7631件/一覧メタ/物理列/全報酬を比較。0番台324面2924行も回帰一致。レポートは`research/.local/all-stage-database-0.1.15.json`と`stage-database-0.1.15-band0.json`。
- workspace17件＋compile_fail1、clippy全target、JS構文、release/CLI verify、実ブラウザーを確認。全29系列の検索と候補内ANDは`.local/verify-stage-search.mjs`。本能玉、固定編成、未来編、Pt、L/D切替、ゾンビ襲来を実画面で確認。
- Windows Store版pythonはAppDataを仮想化して通常DBが見えない。通常DB検証では`C:/Users/ABC/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`を使用する。

## 関数と残る範囲

`stages/importer.rs`→全定義/一覧/4種類報酬、`extras.rs`→補助設定/固定編成/候補、`rewards.rs`→本能玉の原本名/アイコン。`search_catalog`→検索索引、`catalog_map`→マップ詳細、`variant`→許可候補。ServiceのstageExperience→bridge→C++で章/内部種別を保つ。設計はdocs/dataとcrates/kbcs-data/docs。

原本にない2面（日本編ゾンビ2/3章の月）は欠測表示、一覧外7定義は未収録の統率力/XPをNULLにして保持。廃止ID1002/未対応進化権10214等の名前を捏造しない。閲覧DB完成と、全戦闘/期間解禁/クエスト抽選/迷宮編成消耗/報酬実付与・セーブの実装完成は区別する。次の実装では保存済み疑似コードの版/ABI/SHAを照合し、専用状態を順に追加する。

## 以前の動作版（0.1.14の記録）

- `.local/dist/0.1.14/kbcs.exe`、ABI2 / ruleset1507021、schema7 / importer8。
- 通常プレビューは0.1.14で127.0.0.1:4817、今回PID19112で非表示起動。終了・更新時は実行パスと引数を再確認する。旧0.1.13/PID14152は実行元・引数・非表示窓を確認し停止/WaitForExit済み。
- 実使用DB：`C:/Users/ABC/AppData/Local/KBCS/official/jp-e63a79e7efc54c515d1e9f8ae3a3f9d8b50665ce8b798cf27333139eab0ad1bc.sqlite`。
- 旧DBは保持。切替前ポインタは`.local/current-before-0.1.8.json`。検証用データ`.local/stage-0.1.8`、比較結果`research/.local/stage-database-0.1.8.json`。

- 今回は共通C++/APIの更新で、UIソースは変更していない。旧画面確認画像は`.local/stage-materials-0.1.8.png`。新しい敵基礎値を旧Web表示へ全面接続する作業は残っている。

## 完了した範囲

0番台49マップ・324面・出現2924行・冠196値・原本378件を全件比較。0.1.7のXP、検索と表、冠、左右パネル、共通お宝・施設は維持した。

0.1.8はDropItemの49プロフィール・196冠係数・392回数枠・392重みを保存。素材IDはGatyaitembuyの種別7/スロットを同版の006f308cと16件照合した。抽選回数1568条件、2段階抽選7条件が現版命令と一致。C++のmaterials::plan/pickを共用し、表示は一様独立抽選の理論確率。素材の所持数加算や乱数器全体は未実装。素材は報酬検索へ追加し、詳細の素材表は初期状態で折りたたむ。

009eadc8の待機初期化と敵城行の消費を局所実行し、全324面と境界6条件を確認。loaded列2の負待機を維持、敵城の最初の一致行だけwait=1/spawned=1、生成helper失敗時にも消費する。stage::initializeへ追加した。通常出現のcommit成功時限定規則と混ぜない。敵個体の生成・HP/姿勢や戦闘全体の初期化は未実装。

workspace7テスト、clippy全target、実データ比較、JS構文、BOM、release/CLIを確認。画面はN000の1冠2回/2冠3回、素材確率・期待数、レンガで47マップ312面、画像欠損とconsole警告/エラーなしを確認した。素材名原本は正常なUTF-8で、ターミナルの文字化けを原本破損と誤認しない。

## 0.1.9の追加

- 敵HP/各攻撃：行倍率で四捨五入→冠で切捨て→クリスタル不足分の整数加算。敵城の攻撃だけ冠を除外。enemy_stats.pyで境界48、全2924行×4冠を覆う8416プロフィール。C++のenemy::statとServiceのenemyStatsへ接続。通常Webの合成倍率とは212プロフィールで異なる。
- 0番台通常報酬：kind3/通常フラグ0/特殊分類0/mode−1または1。取得済みの先頭が当選した場合、通常は次候補、レーダーは補助フラグ1/候補なしで打切り。比較乱数は取得済み・レーダーでも消費。境界48、実324面の2592条件。reward::legend_pickとServiceのlegendRewardsへ接続。所持数や取得済み状態の実書込み、レーダー返却は未実装。
- C++へ現版報告の8464敵値/2640報酬選択を再投入して全一致。bridge7+data2+Service1のworkspace10テストとclippy全targetが通過。release/CLI verify、同版DBの継続利用、ループバック待受、埋込UIとBOMも確認。Serviceは共通handleへfixture96条件を直接渡し、全出力・件数・ABI/ruleset・未知キー拒否を確認する。
- 完全な報告はresearch/.local/enemy-stats-1572.jsonとrewards-1572.json。小fixtureだけ追跡。関数関係・入力・制御helper・限界はnative/kbcs-core/docs/stages.md。

## 0.1.10：外部評価と1000番台

- 対応表と関数の関係はnative/kbcs-core/docs/audit-20261022.md。評価の数値カーネルの指摘と、ランタイム未実装を区別した。
- 非0明示シードのxorshift13/17/15をrandom.cppへ追加。範囲1も状態更新する。実命令32段階、個体枠/レイヤー5条件、生成成否後の間隔/seen2条件を確認。生成全体やOSのseed0初期化は対象外。
- Rust tickの結果をPendingSpawnとし、commit(self)で1回消費する。生C ABIも生成数上限/撃破/城を再検証するが、C++所有ランタイムでの候補管理は今後必要。
- 有効な超獣/超賢者/怪人の倍率0を拒否。stat/命中/毒撃は成功時だけ出力へ代入する。攻撃種別param_6=0/1/2の準備を別入口に追加。命中48条件×21段階、準備18条件をnative-vectorsで比較。対象外/呪いの全状態入口、全個体初期化、波動等の伝播は未実装。
- workspace11テスト、compile_fail 1件、clippy全targetが通過。releaseを.local/dist/0.1.10へ配置し、既存DBのCLI verify（importer8/ABI2）成功。通常プレビューを更新した。既存UIとschema7/importer8は変更していない。
- events.pyでS000..S435、メタ1213面/RS定義1215件、出現11024行・有効冠566値を棚卸し。報酬mode7種。孤立定義S268-1/S325-5、数値「.」1セル、数値終端なし206ファイルを原文のまま記録。S279-0の撃破解禁30/90/210も確認。詳細はresearch/docs/stages/01000.md、大きい報告はresearch/.local/stages-1572-band1000.json。DB/UI公開はまだ行わない。

## 0.1.11：1000番台の報酬・XP

- 設計と再実行はnative/kbcs-core/docs/event-rewards.md。event_rewards.pyで候補数決定を含めて9704条件を照合した。通常mode−2/−1/0/1/2はstage_pick、重みmode−3/−4はweight_total→乱数1回→weight_pickを使う。負modeの通常候補数は1。レーダーでも比較乱数を消費する。
- 先頭報酬分類0の保存フラグと分類1/2/3の所持判定を区別してacquiredを解決する。実205IDと境界の分類getter、4分類の所有状態192条件、mode2だけ冠別に使う取得済みバイトgetter/setter8条件を確認。所持判定の全内部状態・特殊フラグ1の格納元は今後。
- XPはkind1で×9/クリア数減衰を通らない。EventInputはclearsなし。6境界と実2426条件を、減衰helperを呼ぶと失敗する設定で照合。共通C++は以降の勉強力/お宝/コンボ/おかめの整数化を共有した。
- 配布版は.local/dist/0.1.11。releaseビルドと実DBのCLI verify（importer8/ABI2）成功。UIの変更はない。
- C++へ通常選択656・正常重み56・XP2426を再投入して全一致。小fixtureは通常60/重み67/XP6。11枠使い切りはネイティブでは乱数を消費して候補なしになるが、製品APIでは拒否。workspace11件とcompile_fail 1件、clippy全targetを維持する。
- mode−2の追加報酬、mode−3の履歴、実付与/所持数、解禁/期間/連戦は未実装。DB/schema/importerとUI公開範囲は0番台のまま。0.1.11は共通計算の更新であり、1000番台全体の完成ではない。

## 0.1.12：スコアと重み確定（2026-10-23）

- 追加セル群は原本15列=1で有効なスコア報酬。309面（mode−2が301/−3が7/−4が1）。game+83e74の計測値からスコアを計算し、oldBest<threshold<=scoreの各枠を原本順に要求する。33境界と実4156条件を局所実行した。elapsedを画面の秒と推測しない。
- score::calculate→kbcs_core_stage_scoreはscore/best/improved/reward_maskを返す。付与helperが1ならスコアの結果行を除外するが最高は更新する。保存更新は要求の処理後。
- reward::weight_finish→kbcs_core_reward_weight_finishはmode−3の初回だけ履歴記録と付与を要求し、既記録ならスキップ（レーダー時打切り）。mode−4は毎回付与要求。履歴は付与前に書き、付与結果1でも重み報酬の結果行を残す。既存treeノードで実getterと本体48条件を実行し、書込み順も確認した。
- 大報告はresearch/.local/stage-score-1572.json、reward-finish-1572.json。小fixtureは34/48件。C++へ4189スコア/48確定を再投入して全一致。workspace12件（bridge9/data2/Service1）とcompile_fail 1件、clippy全targetが通過。
- releaseを.local/dist/0.1.12へ配置。実DBのCLI verifyはimporter8/ABI2で成功し、同じDBを継続利用する。UIソースの変更はない。
- 関数・単位・入力責務はnative/kbcs-core/docs/stage-score.md。新規tree挿入、実所持数の上限/変換/解放、保存先選択、時計の加算元、期間/解禁/連戦は未実装。schema7/importer8とUIは維持。

## 0.1.13：保存先・所持数・時計・EX（2026-10-23）

- 詳細はnative/kbcs-core/docs/inventory-ex.md。通常取得済みはヘッダー列1（0..399）、スコアは列2（0..199）。009a3a30の正規化245条件、実通常報酬9704条件を再確認。元modeで候補数を決定後、保存番号なしの取得済み処理を省く。
- 旧309スコア面のうち8面は処理対象外。有効301面3988条件＋時間境界33、無効8を検証。旧報告はresearch/.local/*-before-save-context.jsonとして保持。旧0.1.12の4156件は保存先を人工的に与えた数値比較であり、有効面数を示さない。
- score::advanceはphase0の受理更新で1加算、30000で飽和。現版24境界を照合。壁時計の秒や外側の速度を確定したものではない。
- inventory::addは通常数値245定義の2205条件、実報酬入口374条件、多段変換2条件を照合。所持数を含む合計への後続倍率も再現。残る30定義の専用処理、通知、特殊キャラ、永続化は未実装。
- transition::selectは追加候補→直接EX確率→当選時の面抽選の順で同じRandomを借用。現版RNGを実行し、1213面×6seedの7278条件、全EX_group選択器340条件、小fixture29件の出力/消費順/更新後seedを比較。
- EX_optionは抽選と別の条件付きRE表差替え。009a3a30は有効フラグ等を確認し、mapの有効面vectorが非空ならRE表を読み、各面membershipが真の行だけ差し替える。有効vectorの生成は未確認。3設定行だけを見て全ステージへ差替えを適用しない。
- 現版報告をC++へ再投入し、所持数2579/通常報酬2656/スコア4021/EX7647件が一致。.local/verify-stage-0.1.13.cppが再投入用。workspace14件とcompile_fail 1件、clippy全targetが通過。
- releaseを.local/dist/0.1.13へ配置し、実使用DBへのCLI verifyが成功（importer8/ABI2）。通常プレビューも同じDBで更新した。
- DBはschema7/importer8の同じsnapshot。UI公開は0番台のまま。S取込みにはEOF終端・「.」・孤立2定義・通常/重み/スコアの区別と保存番号の根拠を必要とし、単純なglob拡大をしない。

## 0.1.14：39000番台まで（2026-10-23）

- research/verify/stage_bands.pyは6333戦闘定義・62488有効出現行、終端含む67911読込行（異なる入力47248）を現版00a06ae4へ照合した。原本hashと物理行をresearch/.local/stage-bands-1572.jsonへ保存。真レジェンドの一覧外5定義、Sの2定義、迷宮113テンプレートを保持。
- stage_sources.pyはID0..39999の40000条件、現在種別168、参照先選択144。クエストは抽選済みRN参照、迷宮は選択済みテンプレート、EXは専用座標を要求。参照元を推測して既定値で埋めない。
- band_experience.pyは全種別と章/EX304境界、実表10788条件。9倍/4回/5の減衰はkind0/−9/−22、章は面から元値生成/13回/14の減衰、他とEXは元値のまま。既存の補正を共有し旧ABI入力は維持する。
- RA068-1/RSR021-2は再出現max<min。原本は非正boundで0、乱数状態を進めずminを保存する。C++/Rust乱数とtick/commitを修正し、実RNG付きの2条件を回帰追加。bound1は消費する。
- C++再投入は出現行47237、ID40000、現在種別168、XP11092で全一致。.local/verify-bands-0.1.14.cpp。小fixtureは出現行106、ID境界91/参照先144/現在種別168、XP304。
- 最終workspace17件とcompile_fail 1件、clippy全target、差分/日本語BOM、配布releaseと実使用DBのCLI verify（importer8/ABI2）が成功。プレビューを0.1.14へ更新し127.0.0.1:4817のみの待受を確認。
- 共通C++: map.cppのdecode/encode/current_kind/row_decode、stage.cppのstage_experience。Rust: stage_source::{decode,encode,current_kind,resolve}、stage::Row::decode、experience::stage。DB schema7/importer8とUI公開範囲は変更しない。

## 次に調べる箇所

1. enemy::statを敵検索/詳細・ステージ個体の表示へ接続する。出現行倍率と冠を保存状態で分けて受け渡し、旧Webの合成倍率へ戻さない。今回まだUIへ全面反映していない。
2. 0番台の報酬005d996cの006e34b0以降の実付与、取得済み保存の冠別格納、レーダー返却、素材所持数加算。通常分岐の結果を全報酬形式へ一般化しない。
3. 009eadc8の残る個体初期化、冠倍率の個体HP/攻撃への適用順、コンテニュー。今回の2区間の検証を全初期化へ拡大解釈しない。
4. 006d6d04のボス2だけの005c1404追加イベント。ボス1/2の衝撃波経路は静的確認済みだがフレーム全体の実行ではない。
5. 1000番台の残る30アイテムの専用処理・特殊キャラ、EX_option有効面vectorの生成、解禁/期間/EX戦闘初期化を確認する。スコア/重みの要求と実付与を混ぜず、別番台を検証済みにしない。

現版はJP15.7.2 ARM64 / 1507021、SO SHAはresearch/docs/stages/README.mdとresearch/.local/reference.jsonで確認する。MCPの旧15.7.1 ARM32、読み取り専用の参照リポジトリ、既存Ghidraプロジェクトを混同・変更しない。GitHubへの書込は個別承認が必要。

## GitHub保存と再起動後の再開

前回の保存先は既存の非公開リポジトリsinsuirakv0/KBCS。0.1.8のソースはmainの1cbd7d6、動作版と検証結果はRelease `kbcs-v0.1.8`へ送信・ハッシュ照合済み。今回の0.1.9〜0.1.14は未コミット・未送信。既存の大容量ネイティブ資料はRelease `native-v15.7.2`を維持する。実使用DBと旧snapshotはローカルに保全し、必要なら同じassets版から再生成できる。

```powershell
./.local/dist/0.1.14/kbcs.exe preview --bind 127.0.0.1:4817 | Out-Host
```

## 再実行

```powershell
$env:CARGO_TARGET_DIR='C:/Temp/kbcs-build-20261021'
$env:PATH='D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin;C:/Users/ABC/.rustup/toolchains/stable-x86_64-pc-windows-gnullvm/bin;'+$env:PATH
cargo test --workspace --locked
cargo clippy --workspace --all-targets --locked -- -D warnings
python research/verify/stage_database.py --data-dir D:/KBC/KBCS/.local/stage-0.1.8
python research/verify/materials.py --assets D:/KBC/KBC-rakv0-assets --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/stage_start.py --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/enemy_stats.py --assets D:/KBC/KBC-rakv0-assets --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/rewards.py --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/rng.py --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/events.py --assets D:/KBC/KBC-rakv0-assets --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs
python research/verify/event_rewards.py --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/experience.py --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/stage_score.py --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/reward_finish.py --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/inventory.py --assets D:/KBC/KBC-rakv0-assets --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/ex_transition.py --assets D:/KBC/KBC-rakv0-assets --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/stage_sources.py --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/stage_bands.py --assets D:/KBC/KBC-rakv0-assets --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/band_experience.py --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
./scripts/build.ps1 -LlvmBin 'D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin'
```

cargo fmt後は日本語ファイルのBOMを復元する。起動中の配布exeは上書きせず、対象の検証・停止・WaitForExit後に更新する。0.1.8までの基盤は前回コミット済み。0.1.9〜0.1.14の変更は未送信。今回の変更をreset・削除しない。この再開作業ではcommit・GitHub書込は行っていない。

公開画面の確認画像は`.local/stage-db-0.1.15.png`。DB/実行ファイルのSHAと旧snapshot保全の記録は`.local/publication-0.1.15.json`。

公開確認画像は`.local/motion-workspace-0.1.16.png`。DB/実行ファイルのSHAと旧snapshot保全は`.local/publication-0.1.16.json`。試験用4820/4821は停止済み。

## 2026-10-24: 0.1.21 ステージ詳細とC++描画

配布: `.local/dist/0.1.21/KBCS.lnk` / kbcs.exe。通常AppDataを共用し、現在のスキーマ8/変換器13のDBは `jp-9bf0ddccfec99076e741e8a25bf198035d407e5f77cb1ca7373f89c8e46e06b9.sqlite`。背景・城原本631件を追加。update.lockなし。ユーザーの旧GUIは停止していない。

最新プレビュー: http://127.0.0.1:4832/、PID14316。今回作成した4828/4829/4830/4831の旧テストサーバーは停止した。ユーザーの4817は変更していない。GitHubへの書込は行っていない。

共通C++の姿勢・背景/城・背景演出を、ステージ拡大と味方/敵/その他モーションへ接続。rand=2の冠別保存枠、取得済みとレーダーの判定を既存C++から表示する。個人の受取状態は保存しない。詳しくはstage-details-native-render.md、native/kbcs-core/docs/render.md。

22試験+compile_fail1、clippy、JS構文検査成功。姿勢96条件、演出時計24時点、372背景×4時点+城型3条件=1491条件、全6476面/6333定義/62488出現行/12194報酬行を確認。背景185の画像は原本未収録、1079は5素材が静止モデル。全ネイティブ画像の新規一致確認ではない。receiptは `.local/publication-0.1.21.json`、一括背景の報告は `.local/native-scene-0.1.21-final.json`。

初回の空bg1001.jsonとCSVヘッダーを修正済み。開発機の不足原本504件33,128,490 bytesは、同じ固定snapshotのローカル原本から索引SHAを検証してAppDataの原本キャッシュへ補完した。coldネットワーク全件の速度測定ではない。音源31は実際のネットワーク取得・再生・停止・保存を確認した。

## 2026-10-24: 0.1.22 編成UI

配布 `.local/dist/0.1.22/KBCS.lnk` / kbcs.exe。最新プレビュー http://127.0.0.1:4834/pages/formation/、PID7824。通常AppDataのuser/formations.sqliteへ独立保存し、公式schema8/importer13は変更していない。QAは `.local/formation-qa` の別ユーザーDB、公式DBだけjunctionで共有。検証用4833/4835は停止、既存4832/4817・ユーザーGUIは停止していない。GitHub書込なし。

ステージPlayの縦メニューと編成を追加。矢印の循環切替、10枠の選択/交換、レベル・形態・本能・本能玉・城砲・お宝/施設の編成別保存、コピーのファイル書出しと置き換えのPCファイル読込。保存競合をrevisionで拒否し、非同期保存の応答で編集内容を戻さない。

上部は原本5アトラスとimgcut。00827ba0→00a82394の空枠/背景/ページ、00a8b028の110×85キャラ、00446784の9分割選択枠を参照。Data/param.tsvのJPページoffset=31も照合。出典と関数関係はui/docs/formation.md、保存契約はcrates/kbcs-data/docs/formations.md。画像・設定の元SHAはui/images/native-formation/manifest.json。

23試験+compile_fail1、clippy、JS構文検査成功。ブラウザでキャラ追加・保存・矢印切替・再読込・書出し・PCファイルによる置き換えを確認。配布版は通常AppDataで新規編成の作成と表示を確認。記録 `.local/publication-0.1.22.json`、表示 `.local/formation-0.1.22.png`。IAB初回ナビゲーションのタイムアウト後は再読込で正常表示、コンソールエラーなし。

次は編成の装着解禁/戦闘入力の合法性検証と、既存/自作ステージの選択、必要素材の一覧確定→暗転中に読込→C++戦闘ランタイム開始。今回の編成保存を戦闘の実装完了とは扱わない。
