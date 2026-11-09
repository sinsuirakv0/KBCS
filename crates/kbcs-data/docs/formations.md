# ユーザー編成

formations::Storeは公式snapshotから独立した `<data-dir>/user/formations.sqlite`（user_version=1）を扱う。保存件数の上限は設けない。公式schema8/importer13は変更しない。

Documentはformat/schemaVersion/region/gameVersion/name/slotName/10枠/cannon/profileを持つ。MemberはunitId/form/level/plus/talents/orbs。profileは編成専用の章×お宝効果・施設・土台・装飾設定。公式原本の版をファイルに残し、将来版の未知フォーマットを黙って変換しない。

readは現在/前/次の1件と件数・位置を返し、端で循環する。writeは新規INSERTまたはid/region/revision条件付きUPDATE。競合時に上書きせずエラーを返す。1件のSQLite更新で書類全体を保存し、別編成の値を共有しない。入力は1MB以内、固定10枠・同一キャラ重複・型/範囲を検査する。

stages::equipment_catalogは原本equipmentlist全IDを既存rewards::decorateへ渡す。名前やアイコンの対応を複製しない。GET /api/formation-equipmentはこれを公開する。

最小限の実DBテストで保存/再オープン、別編成と地域の分離、循環、旧revision拒否、未知schema拒否を確認する。

0.1.26ではcannon.developmentLevel（1〜30）を追加。欠測時は30で旧ファイルを読める。JSON文書内の追加なのでSQLite schemaは1を維持する。listは出撃準備の選択用にID/revision/name/slotNameを返し、全編成の巨大なprofileを列挙しない。


0.1.27では版・採用元SHA付きの原本をresources/unit-equipment-slots.jsonへ保持した。公式DBに枠定義がない同版のときに使う。元CSVにないキャラは0枠。

## 本能玉の装着記録と有効条件

`equipment::Catalog` が公式DBで採用した `equipmentlist.json`・`equipment_attribute.csv`・`equipmentslot.csv` を読む。`source_file` に原本がなければ `asset_reference` の固定SHAで取得する。編成文書は既存の `orbs: [ID | null, ...]` を維持し、途中の空欄を詰めない。DB・ファイルの形式変更は不要。

原本 `00661b30` / `0063e8b4` に従い、条件コード0は追加のレベル条件なし、1は合計Lv60以上。`0065f258` は玉2〜4で対応能力と属性を確認し、玉17では烈波無効、玉19では正の固有再生産短縮を除外する。KBCSの新規候補は現在の実効形態について判定する。原本では別形態が条件を満たす場合に事前装着できる経路もある。`Member::effective_form` / `active_talent_level` と `Catalog::eligibility` を候補API、保存、出撃で共用する。

`Store::write` は現版DBの枠数・ID・実効形態を検査し、変更した玉だけに新規装着の条件を要求する。形態・本能・レベルを変えても既存の玉IDは保持する。ファイルと一時枠からの復元は `Store::restore` を通り、既知の休眠玉を復元できる。出撃時はどちらの経路も `Eligibility::active` により再判定する。旧文書にある欠測IDや余剰枠は読み込み時に消去せず、明示的に外す。原本に存在しないID・枠を保存や出撃には渡さない。

計算と照合範囲は[本能玉の戦闘処理](../../../native/kbcs-core/docs/equipment.md)を参照。
