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
