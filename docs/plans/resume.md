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
