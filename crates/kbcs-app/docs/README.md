# kbcs-app

mainがGUI・CLI・previewを選ぶ。desktop::runはtaoでWindowを作り、wry/WebView2で埋込みuiを表示する。service::Serviceは専用プロトコルとHTTPプレビューの共通処理を持つ。

- GET /api/catalog: SQLite → view::catalog。公開snapshotごとの表示キャッシュ。
- GET /api/asset/<logical path>: 保存済みPNG。原本のフォルダやネットワークは不要。
- GET /api/source?id=: 選択キャラの原本CSV・SHA・出典。
- GET /api/status / POST /api/import: 更新workerの状態と開始。

通常起動は専用プロトコルでポートを使わない。previewコマンドはループバックだけで待ち受け、同じ画面をサイドパネルで確認できる。画面の責務と再利用元は[uiの資料](../../../ui/docs/README.md)。戦闘ロジックをここへ追加しない。

POST /api/calculateにenemyStats（最大4000件）とlegendRewards（最大64件）を追加。Service→kbcs-bridge::enemy::stat/reward::legend_pick→C++。未知キーと件数超過・POD入力範囲を拒否し、ABI/rulesetを既存の計算と同じ応答へ含める。表示側のキャッシュや所持数を書き換えるAPIではない。

Serviceの1テストで現版fixture96条件を直接handleへ渡し、応答の型・件数・ABI/ruleset・全出力と未知キー拒否を検証する。HTTPや外部アプリに依存せず、GUI専用プロトコル/previewが呼ぶ同じ入口を試験する。


0.1.15：ステージ検索schema2。`/api/stages`は全系列の軽量索引、`?map=KEY`は詳細、`/api/stage-variant?map=KEY&stage=N&source=PATH`は保存済み候補だけを返す。キャッシュキーは文字列でDBパス切替時に全破棄する。stageExperienceはmode/kind/stageを含む最大64入力を共通bridgeへ渡す。Service既存試験で原本XPベクトルも照合する。

0.1.16：GET /api/motion?kind=unit|enemy&id=N&form=0..3は保存済み本体/魂の原本一覧を返す。POST /api/motion-timelineはsoulFrames/specialFramesからC++の時計を取得する。未知項目・負値・30000F超を拒否し、Service既存試験に境界を追加した。CLI motionも同じdata::motions::manifestを呼ぶ。

0.1.17：/api/motion-effectsの一覧は既存のDBパス別カタログキャッシュを共用。/api/motion?kind=effect&id=STEMとCLI motion --kind effectはdata::effects::manifest、catalog --kind effectsは同catalogへ接続する。画像は既存/api/asset、演出用param.tsvも原本一覧に含む。

## 0.1.18: キャッシュと計算入口

Serviceのcatalogキャッシュmutexは参照/挿入時だけ保持し、DB生成とJSON化中は解放する。他カテゴリを同じロックで待たせない。DBパスをキーに含めるため、生成中にDBが切り替わっても旧結果を新DBへ流用しない。同じキーへの同時初回要求は重複生成し得る。CLI catalog --kind stage-indexで索引だけを測定できる。HP/攻撃のUI一括要求は既存calculateNativeのバッチ入口を共用する。


## 0.1.19: 素材読込

/api/motion-choices?kind=unit|enemyを追加。キャッシュキーにkindとDBパスを含め、名前と形態だけを返す。モーション画面は/api/catalog・/api/enemiesを読み込まず、他種のカタログ生成を待たない。


## 0.1.20: 原本の永続保存

通常のデータ取得ボタンはDEFAULT_SOURCEのGitHub原本を使う。手動取り込みは折りたたみで従来のsource指定を維持する。statusはdataDir/assetDir/updateSourceを返す。exe更新で保存先を変えず、CLIの--data-dir/環境変数指定も従来どおり。

## 0.1.21: 共用シーン

POST /api/stage-sceneは背景ID・幅・城・フレーム・カメラ条件から描画命令を返す。scene::SceneはRustの原本解析とテクスチャ対応を担当し、姿勢・配置・演出更新はC++へ渡す。DBパスと素材条件で最大16シーンを保持しMutexで保護する。失敗した状態は破棄する。GET /api/stage-audio/ID.mp3は固定索引の音源だけを取得・保存し、専用Mutexで二重取得を防ぐ。

CLI `scene --input conditions.json [--summary]` は同じ描画処理をGUIなしで呼ぶ。入力は/api/stage-sceneと同じ条件のJSON配列、出力は1条件1行JSON。summaryは命令数・不足素材・静止モデル件数だけを出す。フレームを戻すと同シードから再生し直す。将来シミュレーターは同じC ABIを使い、戦闘状態の更新と表示を分離する。

/api/calculateのrewardPoliciesは既存C++報酬入口を条件表示に利用する最大128件の要求。ユーザーの報酬受取状況は保存しない。

POST /api/motion-poseはkind/id/form/resource/clip/frames/facingを受け、共通Model::poseの整数頂点を返す。32F以下のバッチ、原本manifestの既知クリップのみ許可。DBパスを含む最大64モデルをキャッシュし、計算中にキャッシュロックを保持しない。城型の敵もmotion_pose::resource_modelを共用する。UIは16Fごとに先読みし、パーツ数に応じた上限で破棄する。

## 編成 0.1.22

GET /api/formations?current=ID&direction=-1|0|1 は前/現在/次、POSTは{id,revision,document}で保存。Service→formations::Store。件数制限なし、revision競合を拒否。GET /api/formation-equipmentは原本IDと既存の報酬用名前・画像を返す。


0.1.31の/api/stage-audio/IDは実MIME(audio/oggまたはaudio/mpeg)を返す。.mp3/.ogg付きの旧経路も同じIDとして受ける。POST /api/asset-hashesは最大64の論理パスについて、現在DBのasset_referenceのSHAだけを返す。buildIdが音源追加等で変わっても、同梱UI画像/imgcutを全照合して再利用するための読取API。
