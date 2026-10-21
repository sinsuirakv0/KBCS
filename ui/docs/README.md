# Web UIの再利用

ユーザー指定により既存kbc-webのHTML/CSS・検索UIをそのまま基準にする。元Webのcheckoutは読取専用。`scripts/sync-ui.py` が必要な依存41ファイルと検索HTMLを同期し、元ファイルのSHAをupstream.jsonへ記録する。UI全体のNode/Viteビルドは不要。

## 編集箇所

- `src/shared/ui`: 元Webのtokens・共通レイアウト・DB・キャラ表CSS。
- `src/features/units/search.js` / model.js / view.js / filters.js: 元Webの検索、絞込、ソート、比較、CSV、アイコン。通常の変更は上流と同期規則を確認してから行う。
- `src/shared/game/units.js`: Rustの/api/catalogへ接続する小アダプタ。
- `src/shared/game/unit-view.js`: 元Webの切り抜きを維持し、アイコンは/api/assetからオフライン取得。
- `detail.js`: 元Webの表構造・共通描画/計算関数を使う詳細画面。最終形態の表に本能Lv、ON/OFF、一括操作、NP内訳を表示する。
- `talent-effects.js`: lab/unit-db/battle.mjsからapplyUnitTalentsと必要なヘルパーだけを同期する。手で編集せず、同期元のSHAをupstream.jsonで追跡する。
- `talents.js`: 共通成長計算→本能による形態補正→HP/攻撃補正→DPSの表示用アダプタ。検索と詳細で共有する。
- `home.js` / native.css: 小さい機能ボタン、データ管理、更新進捗。
- `native-state.js`: 検索・詳細の条件をsessionStorageへ保存する。検索条件は画面ごと、詳細の計算・編成・比較条件はIDごとに復元する。詳細へ移動するときの条件引継ぎも共通化する。URLには内部移動用のID・形態だけを残す。

本能は第3形態以上、超本能はさらに合計Lv60以上のとき反映する。初回表示でLvを自動変更しない。超本能の明示選択・一括最大操作では元Webと同様にLv60へ調整する。低Lvへ戻すと適用を解除し、欄内に必要Lvを示す。詳細・NPは「本能詳細」で開く。設定は同じセッション内で再読込しても復元する。

同期は `python scripts/sync-ui.py <kbc-web> <lab/unit-db>`。ダメージ計算ラボ・装着玉は未実装。更新後はRust実行ファイルを再ビルドする。同じHTML/CSS/JSがネイティブ版とpreviewの両方に埋め込まれる。プレビューを公開ホスティングへ送らない。

WebDBは将来訂正されるため、再利用コードの版・元CSVとの照合・未対応範囲を追跡する。コード同期時に原本データやresearch資産を変更しない。

## 進化・コンボ・成長

入手・進化条件は元Webと同じ詳細行に表示し、素材は実PNGを使う。複数の通常ステージ報酬は代替経路として並べる。

`src/features/units/growth.js`は元Webの成長グラフ・Lv調整・チェックポイント表。detailのbuildRowsから共通のお宝/本能計算を渡す。形態タブでグラフの対象を切り替える。形態比較も同じcalculateTalentStatsの数値を使う。

`combo-builder.js` / `combo-model.js`は元Webの5枠編成・同時発動・効果量・検索を再利用する。詳細のコンボ一覧から編成へ追加でき、選択コンボと形態をアプリ内に保存する。表・成長の数値には元Webと同じくコンボ補正を掛けない。

## 敵・画像保存

敵はWebのtunit-search / tunit-detail、検索・詳細・比較・倍率・クリスタル・会計力を使用する。enemies.jsの接続先を/api/enemiesへ変更し、補完アイコンのimportをローカルパスへ置換する。リンクコピー・外部データ元リンクは設けず、条件はnative-state.jsでアプリ内に保持する。ホームと共通ナビから敵検索へ移動できる。

capture.jsも共通化し、敵の表/比較・味方の表/成長/形態比較をPNG保存できる。html2canvasのESMとMITライセンスをvendorへ同梱し、Node.jsや外部CDNは使わない。版・元SHAはupstream.jsonへ記録する。

## PC用ワークスペース（0.1.4）

workspace.jsは共通main.jsから先に初期化する。既存の画面要素を複製せず移動し、左はページに関係するもの、中央はデータ、右は計算・表示の設定、下は状態と注記に使う。全体の機能移動は上部の小さいナビに残す。表とフィルターは別々にスクロールし、一覧のヘッダーとページ切替を常時操作できる。

- initializeWorkspace → createPanelで枠を作成 → ページごとの要素配置 → applyでパネルの開閉・幅・ARIA状態を反映する。
- move / moveLabelはIDと既存イベントを保持した要素移動。associateFormは元フォームの外に出る検索の計算項目へform属性を付ける。同期アダプタのinput/change処理はevent.target.formで判定し、検索条件と計算条件のどちらからでも元の再計算を呼ぶ。
- 敵詳細のinput/change/captureはworkspace-bodyの範囲で扱い、右へ移した現在の敵の条件も同じupdateで反映する。
- addOutlineは既存セクションへ移動してdetailsを開く。非表示のコンボ項目を案内に出さない。キャラの形態一覧は実アイコンと選択中の罫線を使う。
- 右は初回に閉じて中央の幅を確保する。左右の幅・開閉はkbcs:workspaceへ保存する。境界をドラッグ、またはフォーカスして左右矢印で幅変更。下は通常24pxの状態表示とし、開いたときだけ補足を表示する。
- 元Webの配色・線の濃さ・拡大率を利用する。PCの通常幅では横並び、注釈用の800px未満の表示ではパネルを重ね、中央を幅0にしない。通常のネイティブ最小幅は760px。

CSSはnative.cssに局所化し、元WebのCSSを上書きして同期しない。UIだけの変更なのでDBスキーマ5・原本・計算式は変更しない。

## 施設と章別お宝（0.1.5）

右の計算・表示に、閉じた状態の「施設Lv」「お宝」を全ページで配置する。施設は10項目の通常Lvと＋値、お宝は日本/未来/宇宙の各3章×11効果グループで99項目。元ゲームの名称と青玉画像を使う。お宝の名前/効果、編、章、100%未満で絞り込み、絞り込みに一致する項目だけ一括変更できる。

- settings-catalog.js: scripts/sync-settings.pyで検証・生成した定義。原本、版、上限はこの成果物へ集約する。
- simulation-profile.js: normalizeSimulationProfileで範囲を正規化、migrateSimulationProfileで旧合計と旧合計Lvを引継ぎ、deriveSimulationSettingsで現在の表が使う値を導出する。通常Lvと＋値は別々に保存する。研究力等の旧合計Lv30は20+10へ変換する。旧お宝合計は1章から順に100%まで配分する。元の章別取得状況を推定した意味ではない。
- simulation-store.js: kbcs:simulation-profileにschemaVersion/catalogVersionと全個別値を保存する。既存の表示設定と公式SQLiteは変更しない。
- simulation-settings.js: 共通編集UI。入力・対象分プリセット→保存→kbcs:simulation-changeで各画面の再計算を呼ぶ。編/章の各グループを配列位置から勝手に名称推測しない。施設Lv・お宝の展開状態はページを開くと閉じる。
- readGameSettings→章別プロフィールを継承したreadUnitSettings/readEnemySettings→既存の表/成長/本能の計算。setup付きの旧セッション値で章別プロフィールを上書きしない。比較の施設・お宝も同じプロフィールを使う。

HP/攻撃は各章の最大加算50へ取得率を掛け、章ごとに整数化してから合計する。45/45/45→66と100/35/0→67を区別する。研究力は施設と章別の原本最大30F、会計は施設と最大50%を用いる。既存最大設定の264F・3.95倍は維持。クリスタルは各色×章を合計し、仮面は章別に保持する。未実装の戦闘・統率力等の効果を表へ混ぜず、入力値を保存し、反映範囲を折りたたみで示す。WebViewと注釈ブラウザーは異なる保存originを持つ。設定の保存領域はモードごとである。

共通ダイアログの旧合計入力は右の詳細設定へ導線を統合した。表示/土台/装飾の既存設定は維持。従来の設定文字列の対象は表示・基本設定のみで、個別プロフィールを含まないことを明示する。

## 注釈UIの補正

キャラ詳細のLvを中央上部へ移動し、WebのcreateLevelControlを再利用してスライダー・±1/±10・現在値・上限を置く。form属性とinputの委譲で元のrenderを呼び、kbcs:level-syncで最大本能等からのLv変更も追従する。

本能欄はviewport幅ではなく中央のinline-sizeコンテナーを基準に切替する。中央740px以下で1列。アイコン・名前・Lvを列指定し、文字に残る幅を確保する。884pxの表示で名前の幅158px、1列288pxを実測し、1文字ずつの縦崩れを解消した。


## 0.1.6 C++計算への接続

`detail::render`→`native-calculation::createNativeStatistics.prepare`は形態×全Lvの成長・章別お宝・HP/攻撃コンボ・本能入力をまとめ、POST /api/calculate→kbcs-bridge→C++を呼ぶ。同じ条件のLv操作では結果を再利用する。非同期結果はrenderVersionで古い画面を上書きしない。表・形態比較・成長グラフが同じ結果を参照する。グラフのキャッシュキーには章別丸めの合計とコンボも含める。

`damage-calculator`は右の折畳み条件→味方のunitDamage／敵のenemyDamageへ分ける。毒撃はpoison、メタルキラーはmetalKillerへ分け、通常攻撃へ混ぜない。対象・果実・特殊種別・呪い・本能・コンボを同じ現在のprofileから組み立てる。条件はキャラごとにsessionStorageへ保存する。内訳は折りたたみ、通常画面に技術説明を増やさない。

施設・お宝の保存profileにcannon（base/decorationのIDとLv）を追加。未保存時は旧設定から移行し、値を正規化する。`deriveSimulationSettings`が属性ごとのfruitByTargetとパーツ設定を返し、全画面のprofile変更イベントを共用する。土台・装飾の選択は独立した折畳みに集約し、旧モーダル側の重複入力を削除した。

「相手の属性を適用」は敵名候補から属性・種別を移す。敵の攻撃は一撃の明示入力。直接DPSへ波動等の追加発生を加算しない。メタルキラーは入力した現在HPに対する有効な1撃を表示し、別FのHP推移を擬似的に足さない。未実装の状態は[nativeの監査](../../native/kbcs-core/docs/ability-audit.md)に記録する。

## ステージ閲覧とXP（0.1.7）

sync-ui.pyがWebのstages/search・model・view・rewards・CSSと冠画像を同期する。上流のSHAをupstream.jsonで保持する。loaderは/api/stagesからオフラインのDBを読み、未検証の抽選・シーン再生モジュールは読み込まない。元Webの報酬確率推定は使用せず、比較値を元データの折りたたみへ置く。

stage-detail.jsはマップとステージの選択・冠・時間・詳細列・画像保存を制御し、Webの表とアイコンを再利用する。workspace.jsは検索フィルターを左、詳細の同一マップ内一覧を左、冠/時間/XP条件を右へ移動する。native-state.jsは詳細をmapキーごとに保存し、元の出現行と冠の倍率を敵詳細へ引き継ぐ。通常は全ステージ、左の一覧で1面にも絞れる。

XPは共通calculateNative→Rust→C++のlegend_experienceを使う。クリア済み回数、XPコンボ合計、おかめを右で設定し、勉強力Lvと6章のお宝設定は共通プロファイルから導出する。UIは計算式を重複実装せず、返された5段階を折りたたみに記す。非同期の古い応答は破棄する。DB・定義・コアの版が異なると計算しない。

## 開発素材（0.1.8）

stage-detail.jsのrenderCalculationsがXPとmaterialDropsを同じバッチで計算し、WebのstageRewardsHtmlへ素材の確率・期待個数を渡す。素材表は閉じた状態で、冠を変更すると回数と理論値を再取得する。素材の重みやハズレをJSで再計算しない。native計算とDB/定義の版照合、古い非同期応答の破棄をXPと共有する。元のDropItem行は計算内訳の折りたたみへ保持し、報酬選択に素材アイコン・名前も含める。
