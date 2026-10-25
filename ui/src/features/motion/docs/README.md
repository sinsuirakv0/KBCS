# モーションワークスペース

0.1.16。キャラ/敵の共通UI。`viewer.js`が選択・再生時計・表示マスク・ファイル/分割一覧・検査を管理し、`motion-engine.js`はDOMに依存せず形式解析と整数姿勢を評価する。`native-webgl-renderer.js`は4合成のpacketだけを描画する。元コードとSHAはupstream.json。参照repositoryは変更しない。

## データと状態

`GET /api/motion`→Rustのmotions::manifest→保存済みsource_file。キャラの共有ID/タマゴmはform.motion_pathを起点とする。Number/{stem}.pngを使い、imgcutに残る制作PCのパスを読まない（現版005bcea8の%s.png）。元textは書き換えずファイル詳細に残す。画像・model・cut・全maanim・共通の魂を同じsnapshotから読む。

左はキャラと形態、パーツ/ファイル/分割画像。中央はWebGL、右はパーツの現在値とキー・モデル設定点、下はフレーム時計。親パーツを非表示にしても親子変換は残し、最終packetだけを除く。単独表示と子まとめて操作は表示マスクで実現する。原本のパーツ値や親子関係は変更しない。切り出しPNGは必要時にCanvasで生成する。

KB→魂は`POST /api/motion-timeline`→bridge::motion→C++のmotion.cppが24Fの体力KB、最長の共通/専用魂、退場の時計と変位を返す。専用_soulは番号08と取り違えない。共通魂は地面基準−97に置き、maanim以外の上昇/フェードを足さない。参照は15.7.1 ARM32のknockback/deathの限定照合。現版ではファイル選択を軽く確認し、全戦闘の死亡/蘇生/参照待ち/KB上限を実装したとは扱わない。

## 境界と検証

形式・補間・姿勢の既存コードは15.5.0/15.7.1の解析資料由来。ユーザーの指示により全面再解析は行わず、現版の代表6素材（通常/制作パス/専用魂/敵/共通魂）の120姿勢で整数頂点と描画値を確認。JS姿勢評価はC++へ移す作業が残るため、戦闘用の確定した姿勢APIと混同しない。描画には現在の共通評価器を使い、Rust/C++の時計はGUIから独立させる。

再生は30F/秒、補間表示は任意。フレーム送り/停止では整数フレームを検査できる。UIの画面座標・ズーム・反転・パーツ表示は戦闘座標やゲーム状態へ書き戻さない。DBの原本も変更しない。

## その他モーション（0.1.17）

effect-motionも同じviewer.js / motion-engine.js / NativeWebGLRendererを使う。味方・敵・その他の切替、名称/IDと分類での絞り込みを共通化。素材のmodel/cut/画像/maanimをRustのeffects::manifestから読み、ファイル・分割・パーツ操作を再利用する。アニメーションなしは静止モデルとして表示。

effects::import → 全定義と対応画像をhash検証保存 → effects::catalog / manifest → Serviceの/api/motion-effects / /api/motion?kind=effect。CLI catalog --kind effects と motion --kind effect --id STEMも同じ入口。schema8のsource_file/asset_referenceを流用、importer12へ更新。

素材選択はreadonlyのlab/motion/effects/catalog.mjsを移植。skillのmodelパーツidからskill%03d.imgcut/PNGへ対応し、skill999.png等の制作時ヘッダーを優先しない。敵専用maanimがあれば共有版を混ぜず、なければ共有版へ接続。モデルstemが最長一致する所有関係により別素材のmaanimを混ぜない。critical/boss_welcome/rainは000_aの共通アトラス。同名PNGがない場合だけ、同じ索引に実在するimgcutヘッダー名を試す（bg06→bg102等）。制作PCの絶対パスは解決しない。対応不明は一覧に残して選択不可にし、別の画像を推測しない。

生き残り=skill_shield、バリア=skill_barrier_e、城バリア=skill_guard_e、悪魔シールド=skill_demonshieldを区別する。ユーザー指定で検証は軽くし、現在のJP15.7.2 ARM64の009f560cに烈波・バリアの素材文字列xrefがあることを確認。詳細な制御の出典はlab/motion/effects/docs、15.7.1 ARM32 SHA7226cbdf9f9ea9a521b4e4c3a78a72141a31410aa9293a03bb45717d1682ac79。

effect-sequence.jsはsave/motion/frontendから無変更で流用。波動/小波動はLv個の伝播、烈波/小烈波は開始15F→20×Lv→終了10F、爆波は00→01を再生する。現snapshotのData/param.tsvから小波動間隔・爆波の各Fを読み、絶対時刻で無限トラックを評価する。Lv1〜20は閲覧用制御。素材単体も選択可。戦闘の当たり判定・ダメージ・追従・音声・状態の発動/解除はこの閲覧画面で追加しない。状態演出を一律の持続時間で継ぎ合わせない。

選択パーツの黄色い枠は初期非表示。右の「選択枠を表示」で必要な場合だけ切り替える。選択や表示マスク、元の描画packetには影響しない。

## 0.1.19: 素材読込の待機を減らす

viewer.jsは選択中の種類だけの選択肢とmanifestを並行取得する。unit/enemyの選択肢は/api/motion-choices?kind=unit|enemyで名前/ID/形態だけを読む。数値・本能・コンボを含む全カタログの生成を初期表示の前提にしない。その他の一覧は従来/api/motion-effectsを使う。種類を変えたときだけ未取得の選択肢を読む。

ページ内のmanifestを最大16件、画像デコード/モデル/アニメーション解析結果を最大8件・見積32MiBで保持する。画像の見積はRGBA寸法と原本size、解析JSオブジェクトの実メモリ上限を保証する値ではない。原本SHAとresourceをキーにし、失敗は保存しない。切替時のGPU texture解放は継続する。ページ再読込でキャッシュは消える。DBを更新したときはページを再読込する。

Rustのeffects::manifestは全素材の所有関係を解決するが、model/cutの内容は選択した1素材だけ解析する。他モデル由来maanimとの最長一致ルールは維持する。PNGのdescriptorはlength(bytes)と出典だけを取得し、manifest生成のために画像BLOBを読み出さない。実画像は従来asset APIから取得する。DB/schema/importerと素材の中身は変えない。

## 0.1.21: C++姿勢への接続

viewer.jsの描画・自動フィットはnative-pose.js→/api/motion-pose→render::Model→kbcs_core_poseを使用する。整数フレームの頂点を16Fずつ先読みし、パーツ数に応じて上限を絞る。UIは表示マスク・画面操作・UV転送を担当する。旧evaluateMotionは選択パーツの解析表示だけに使う。KB/魂の時計は従来のC++、複数エフェクトを並べる段取りは既存effect-sequenceである。表示補間は無効にし、検証済みの整数フレームで再生する。
