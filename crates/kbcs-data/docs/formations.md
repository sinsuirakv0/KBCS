# ユーザー編成

formations::Storeは公式snapshotから独立した `<data-dir>/user/formations.sqlite`（user_version=1）を扱う。保存件数の上限は設けない。公式schema8/importer13は変更しない。

Documentはformat/schemaVersion/region/gameVersion/name/slotName/10枠/cannon/profileを持つ。MemberはunitId/form/level/plus/talents/orbs。profileは編成専用の章×お宝効果・施設・土台・装飾設定。公式原本の版をファイルに残し、将来版の未知フォーマットを黙って変換しない。

readは現在/前/次の1件と件数・位置を返し、端で循環する。writeは新規INSERTまたはid/region/revision条件付きUPDATE。競合時に上書きせずエラーを返す。1件のSQLite更新で書類全体を保存し、別編成の値を共有しない。入力は1MB以内、固定10枠・同一キャラ重複・型/範囲を検査する。各キャラの解禁・レベル上限や本能玉枠の戦闘上の合法性検証は今後のランタイム入力組立で扱う。

stages::equipment_catalogは原本equipmentlist全IDを既存rewards::decorateへ渡す。名前やアイコンの対応を複製しない。GET /api/formation-equipmentはこれを公開する。

最小限の実DBテストで保存/再オープン、別編成と地域の分離、循環、旧revision拒否、未知schema拒否を確認する。

0.1.26ではcannon.developmentLevel（1〜30）を追加。欠測時は30で旧ファイルを読める。JSON文書内の追加なのでSQLite schemaは1を維持する。listは出撃準備の選択用にID/revision/name/slotNameを返し、全編成の巨大なprofileを列挙しない。


0.1.27：equipment::capacityはresources/unit-equipment-slots.jsonの版・採用元SHA付き原本から最大枠を返す。view::catalogのorbSlotsとDocument::validateが共用し、UIの追加・外部ファイルの取込・保存のいずれでも最大枠を超えない。191キャラ、最大2枠。元CSVにないキャラは0枠。原本の解放条件列も資産へ残すが、KBCSではユーザー指定どおり全解放の最大枠を使う。schema1と既存ユーザー文書を一括書換しない。
