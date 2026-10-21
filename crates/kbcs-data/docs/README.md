# kbcs-data

- `source`: Source::open → dataset → checked。Git SHA固定、採用元/生成物のsize/hash/版の検証。
- `model`: CSV・maanim解析、検索正規化、Form/Attack/Property。必須列の欠測はエラー。
- `import`: importが排他・一時DB・公開を管理し、build/read_asset/retainで原本と型付き値を保存する。
- `store`: insert_formで書込、Databaseのsearch/form/source/metadataで閲覧、validateで公開前整合性検証。
- `view`: 正規化済みSQLiteをWeb schema9の表示用形式へ変換。
- `talents`: importで本能・各Lv効果・NPを正規化し、readで表示向けのTalentを組み立てる。効果IDの解釈はresources/talent-effects.json。
- `progression`: 図鑑・unitbuy・通常報酬・drop_charaを結び、入手/進化条件と素材を保存する。代替ステージは重複を除き、元MapStageDataの行へ戻せる。
- `combos`: 有効コンボ・必要キャラ/形態・効果量を正規化し、read/effectsからWebの表示・編成UIへ渡す。
- `schema.sql`: 正規化・原本・asset参照のschema6。本能の元行/列、進化素材の元列、報酬ステージの元行を保持する。

データ仕様・列・更新契約は[共通データ資料](../../../docs/data/README.md)へ集約する。仕様修正時はIMPORTER_VERSION、スキーマ変更時はSCHEMA_VERSIONとSQLを更新し、原本を使って再生成する。

検証はtests/import.rsの2件。欠測/0/空欄、不正パス、Git原本からの取り込み、再実行、地域の分離、hash不一致、旧読取connectionの維持、原本を外しての閲覧に加え、本能補間の整数化・1段階本能・追加属性・超本能・NP保存を確認する。実データとの照合は[実測報告](../../../docs/plans/initial-foundation.md)。

- `enemies`: importが敵専用CSVと攻撃maanim/アイコンを保持し、readが型付きEnemy/Attackを返す。catalogは敵専用の属性・能力・表示値を構築する。原本列の解釈と確度は[データ契約](../../../docs/data/README.md)。

0.1.6：CSV118の素の偶数生産時短縮をpropertyへ追加し、view::abilityがpercentを表示する。IMPORTER_VERSION=6、SCHEMA_VERSION=5。既存の取り込み試験で元列118と値50が失われないことを確認する。

- `stages::import`は0番台の原本を読んで6表へ正規化する。rowsは元の行番号・空欄を保持し、Map_optionの説明列だけ数値解析の対象から外す。`stages::catalog`は同じSQLiteからWeb向けの索引・詳細を一括生成する。待機×2はnative配列構築時だけ行い、保存列は原値のままとする。
- 既存の取り込み試験へ0番台の小さいfixtureを追加。負待機、倍率0/負攻撃値、重複敵、終端、末尾空欄、小数難易度、冠、制限、PR39000を確認する。実データの全324面の比較はresearch/verify/stage_database.py。

- `stage_materials::import/read`は開発素材の原本を4表へ保存し、Webのmap.materialsへ戻す。元データのfloat値と原セルを両方保持し、素材IDをGatyaitembuyの列6/7から結ぶ。確率は共通C++で動的に導出する。既存取り込み試験に係数0.75、重み0、元スロットと素材ID、報酬絞り込みへの接続を追加した。schema7/importer8。
