# データ契約と更新

## 実際の取得元

初期対象はJP。`KBC-rakv0-assets/metadata/jp/current.json` のschemaVersion=1、status=verifiedからbuildId・datasetId・versionCode・versionNameを読む。manifestのSHA-256、各索引のsize/SHA-256、全ヘッダーの一致を検証し、`indexes/assets.json` の論理名→採用元ファイル対応を使う。パスやID対応をファイル名の印象から推測しない。

上流の `battlecats-apk/engine` は元split APKの署名検証・必要9群の抽出・復号・索引生成を担当する。KBCSは復号やAPK取得を重複実装せず、生成済みデータの消費側となる。APK署名をKBCS自身が再検証したという意味ではない。

ローカルのGitフォルダまたは公開GitHubリポジトリから取得する。ローカルはHEADと未コミット追跡ファイルの有無を確認。HTTPはHEADを最初に40桁SHAへ固定して以後すべて同じrevisionから取得する。manifestと採用元hashが保証する範囲を検証し、信用の起点となるcurrent自体の外部署名検証は行わない。

- `jp/Local/<datasetId>/`: APK由来原本。
- `jp/server/`: Server由来原本。採用優先度の決定は上流に委譲。
- `overrides/jp/characters/{data,aliases}.json`: 表示名・形態・別称などの手動補完。
- `overrides/jp/assets/`: 補完画像・モーション。
- `generated/jp/datasets/<buildId>/site/characters.json`: 補完を適用済みのキャラ名・形態索引。

名前・形態は生成索引を採用する。数値はunitCSVから直接読む。原本の説明CSVと手動補完も別々に保存し、生成索引の解釈を後で訂正できる。敵・ステージの仕様は調査資料へ記録し、未確認のテーブルは作成しない。

## 保存とスキーマ7

公式snapshotは `<data-dir>/official/<region>-<digest>.sqlite`。`current.json` にregion→filenameを保存する。同じIDでも主キーは地域・キャラID・形態を組み合わせる。将来の複数版同時比較はsnapshot単位で開く。ユーザーの自作領域は `<data-dir>/user/` を予約するだけで、今回の公式更新コードは一切アクセスしない。

|テーブル|内容|
|---|---|
|metadata|地域・ゲーム版・Git SHA・buildId・取得元・変換器版|
|source_file|原本bytes、元パス、sourceKind、SHA-256。索引・manifest・補完も保存|
|asset_reference|全採用元の論理名・実パス・種別・size・SHA。キャラアイコンと特性アトラスの実体はsource_file、他の画像/モーションは参照のみ|
|unit|地域・キャラID・レア度・別称・上限Lv・種類・精霊判定|
|growth|キャラ別の各10Lv区間の成長率。空欄はNULL|
|talent / talent_level|キャラ別の本能・元行/列・追加対象マスクと、各Lvの効果4値/NP費用|
|form|形態名・説明・検索文字列・基本数値・攻撃周期・原本参照・icon_path・raw_cells|
|attack|攻撃段ごとの威力・発生・能力有効列・符号を保持した始点/終点|
|property / property_parameter|解釈した対象属性・能力と、元列番号/元値の対応|

HP・速度・射程・コスト等はINTEGER、欠測可能な発生・モーション長はNULL。すべてをJSONで保存しない。`raw_cells` は列数・空欄を保持する可変拡張領域で、原本bytesも別に保持する。ゼロ、空欄、未収録列（配列の範囲外）を区別する。負値・無効値の意味を勝手に消さない。JSONのraw_cellsはコメントを除いた数値行、原本bytesにはコメント・改行・BOMも残る。

`PRAGMA user_version=7` と `IMPORTER_VERSION=8` を別々に管理。公式DBは再生成方式で、未知スキーマは拒否して再取り込みを案内する。変換仕様を修正したらIMPORTER_VERSIONも上げる。同じsnapshotを黙って古い解釈で再利用しない。ユーザーDBは将来別のマイグレーション体系を設計する。現時点で自作DBの表や空実装は追加しない。

## フィールド対応（列番号は0始まり）

`Data/unit{ID+1:03}.csv` の行0〜3がf/c/s/u。存在する形態はcharacter索引と数値行を照合する。索引より数値行が多い場合も原本は保存し、未実装形態を勝手に公開しない。

|元ファイル・列|内部/表示|扱い|
|---|---|---|
|unitbuy.csv 行ID・13|rarity|元整数|
|unitlevel.csv 行ID|growth|10Lv区間の成長率、元列を保持|
|unitCSV 0 / 1 / 2|hp / knockbacks / speed|元整数|
|3 / 59 / 60|attack.damage|第1段、正値の第2・第3段。元全列も保存|
|13 / 61 / 62|attack.foreswing|元F。未収録はNULL|
|63 / 64 / 65|attack.ability_enabled|元整数、未収録はNULL|
|4|interval_raw|元値、参考表示は×2 F|
|5 / 6 / 7|range / cost / respawn_raw|元値。参考コストは日本編2章×1.5切捨て、時間は×2 F|
|12|area|0か非0。raw_cellsには元整数を保存|
|44 / 45|第1範囲|始点と幅を始点/終点へ変換、符号を保持|
|99,100,101 / 102,103,104|第2・第3範囲|有効指定があれば別範囲、なければ第1範囲|
|unitbuy 61 / 62|共通モーションID|第1・第2形態で非負ならmコードを使う|
|採用されたattack.maanim|animation_length / attack_cycle|長さ=最終キーF+1、周期=max(最大発生+間隔×2−1,長さ)。素材なしはNULL|

対象属性・能力の全対応は `import::PROPERTY_FIELDS` を正本とし、`properties` が有効なものと元値を生成する。精霊召喚は列110が存在して非負の場合だけ有効にし、未収録を0へ補完して召喚扱いにしない。全方位は負の幅、遠方は有効幅がすべて正の場合を識別する。

波動/小波動は35・36・94、烈波/小烈波は86〜89・108、爆波は113〜115等を保存し、パラメータ欄では元値を表示する。確率・継続F・幅の1/4換算・加算倍率等を同じ単位の値として表示しない。本能はSkillAcquisition/SkillLevel/SkillDescriptionsの原本を保持し、talent・talent_levelへ正規化する。

キャラ詳細の体力・攻撃力は現版ARM64で照合したC++の成長・お宝・コンボ・本能の段階を使用する。検索等に残るWeb表示値は戦闘仕様とは区別する。進化条件は図鑑・unitbuy・通常報酬から表示する。本能は第3形態以上、超本能は合計Lv60以上に適用する。時間の30FPS解釈・攻撃周期・能力名はゲーム挙動を独立に証明したものではない。Webの修正時は変換器を訂正し、保存済み原本から検証できる。

## 更新時の関数と失敗対策

1. `import`: create_newでupdate.lockを取得し、更新の多重実行を防ぐ。
2. `Source::open/dataset`: source版固定、manifest・索引・パス・hash検証。
3. `build/read_asset`: 必要原本を都度検証して保存し、1トランザクションで正規化。
4. `store::validate`: schema、integrity_check、foreign_key_check、形態件数を確認。
5. 書込可能ハンドルのsync_all後、完成DBを不変名へrename。
6. currentの地域マップを一時ファイルへ保存・syncし、renameで置換。

失敗時はcurrentと旧DBに触れない。公開前の一時DBは削除し、完成後のDBと過去snapshotは残す。異常終了で残るupdate.lockはPIDを確認して手動除去する。突然の電源断に対するWindowsファイルシステム全体の永続性保証とは区別する。同じrevision/build/hash/変換器版なら検証済みsnapshotを再利用する。時刻をDBへ埋め込まない。

将来の再解釈は保存したsource_fileを入力にするアダプタを追加できる。現在のCLIはassetsからの再取り込み方式で、DBだけからの再生成コマンドは未実装。取得履歴は不変snapshotのmetadataで追跡する。

## Web表示アダプタ

`view::catalog` は型付きSQLiteからWebのschema9に対応する検索・詳細データを生成する。元Webのdatabase.jsonを配布物へコピーしない。成長率、攻撃段、能力パラメータ、対象属性、上限Lv、種類、原本PNGへの参照を引き渡す。精霊名は召喚能力の実際の親形態から組み立てる。

特性のアトラスはimg015.pngとimg015.imgcutの原本を使い、対応の正本をresources/property-icons.jsonへ保存した（lab/unit-db/icons.mjsの確定マップを移植）。座標やアイコンを想像で作らない。手動補完は上流の採用元マップを通し、原本のkindとhashを維持する。

キャラアイコンと特性アトラスは今回の閲覧に必要な小画像だけをsource_fileへ追加する。全スプライトや全モーション画像をBLOBへ入れない。`view`のJSONは表示アダプタの出力であり、原本や正規化済みDBの代わりに正本扱いしない。本能はRust側で正規化し、共通の表示アダプタへ渡す。装着玉は未実装。コンボは正規化し、編成UIへ渡す。

## 本能の正規化（schema3）

SkillAcquisitionの先頭2列はキャラIDと追加対象マスク、以降は14列単位。本能ID・最大Lv・4組の初期/最終値・説明ID・NP表ID・追加対象指定・超本能指定を解釈する。talentには元行（1起点、ヘッダー含む）・元列（0起点）も保持し、talent_levelは各Lvの4値と当該LvのNP費用を保持する。原本の列は書き換えない。

補間は `first + trunc((last-first)*(level-1)/(maxLevel-1))`。最大Lv1はlastを採用する。NPの欠測・非正値、未対応の本能ID、途中で切れた14列ブロックは更新を失敗させる。未対応効果を無効果として公開しない。

効果IDの対応表はlab/unit-db/talents.mjsの68定義をresources/talent-effects.jsonへ移植した。同期時の元SHAはui/upstream.jsonのcompilerSha256。同期スクリプトはこの元SHAが変わるとコピー前に停止し、Rust側の対応表の確認を促す。対応表を直す場合はRustの変換器版と同期スクリプトのSHAも更新する。talents::import → talent/talent_level → talents::read → view::catalog → UIのcalculateTalentStatsで検索・詳細の数値を共通化する。

保存済みschema2は書き換えず、変換器3で新しい不変snapshotを作成する。Webと同じ効果の解釈・表示演算を再現するもので、本家の戦闘挙動を独立に検証した結果ではない。

## 進化・入手・コンボ（schema4）

nyankoPictureBookの各形態3セルを一つの説明へ結合し、＠/@は空欄として扱う。unitbuyの第2形態Lvは21列、第3は20/25列の最大、第4は26列。XPは27/38列、素材は28/39列から5組のID/個数を読む（列は0起点）。GatyaitemNameの名称とgatyaitemDの実PNGを使い、画像が未収録なら名称を表示する。

MapStageDataの通常報酬・追加報酬から報酬IDとステージを対応させ、drop_charaから入手キャラ、第3形態はunitbuyの23列から進化報酬へ接続する。同じマップ・ステージを重複表示せず、複数経路は残す。-2が並ぶ時刻報酬形式は除外する。マップ種別対応はlabのprogression.mjsと同じ範囲。ステージ名・マップ名・図鑑・drop表・報酬表を原本として保持し、progression_stageは元ファイルと行番号を持つ。

コンボはNyancomboDataの行番号をIDとし、列1が非負の有効行だけを公開する。必要メンバーは列3から5組のID/最低形態、効果種別/段階は列13/14。Nyancomboと名称/段階の説明、NyancomboParam.tsvの各段階数値を保持する。参照先キャラが未収録でも元IDを失わないようcombo_memberからunitへの外部キーは置かない。編成UIは元Webの対象となる効果だけを扱う。

関数経路はimport::build → progression::import / combos::import → 正規化表 → read / effects → view::catalog → detail.js・元Webのgrowth/combo-builder。CSVとHTMLの平文化はmodel::csv_rows / plain_textを本能と共有する。

実測ではMapStageDataS_072/081/273/320/325に、//の付かない末尾説明が41行ある。CSVではない単独セルの非数値行だけを除外し、カンマを含む不正な数値行はエラーにする。元の物理行番号を保持し、説明行を架空のステージとして数えない。

## 敵（schema5）

Data/t_unit.csvの先頭2予約行を除き、表示ID0から連番で保持する。Enemyname.tsvの行番号とEnemyPictureBookの各行を対応させる。enemyは基本数値・元セル・原本参照・攻撃モーション参照、enemy_attackは段ごとの威力・発生・効果フラグ・符号を保持した範囲を保存する。属性・能力の表示アダプタは敵専用の列対応を使用し、元セルから解釈する。味方の列定義は流用しない。

敵用の列/名称・補完城ID・アイコン対応はresources/enemy-fields.json。lab/enemy-db/compile.mjsとcastles.mjsのSHAを含み、UI同期時に変化を検出するとコピー前に停止する。補完城分類は上流が確認した分類の移植で、元の城フラグはraw_cellsに保持する。敵用の色付き種族アイコンと味方の特効アイコンは分ける。城・潜行・蘇生の補完PNGはWebの確認済みファイルを出典とSHA付きでコピーする。

攻撃周期は最大発生+待機列×2−1と実maanim長の最大。maanim未収録なら周期はNULL。敵アイコンも実在する原本のみ保存し、未収録画像や別版の数値を補わない。モーション再生は後続のため表示アダプタのmotionはnullにする。

この版では味方の図鑑説明も原本Unit_Explanationの3セルを改行して採用し、原本がない場合のみ生成索引へフォールバックする。

説明原本との照合では、既存WebのCSVパーサーが引用符を落とす箇所と旧データの空説明により37形態の表示差がある。KBCSは原本の引用符とダミーの仮説明も保持する。Webと違うからといって原本の数値や文を上書きしない。呪いアイコンは最新の確認済み切り出し289へ訂正し、本能玉の背景291も対応表へ追加した。

## 0.1.6の計算・取り込み補足

CSV118の素の`alternate-respawn`を型付きpropertyへ追加した。値は短縮%。15.7.2の00aa5f84は列118と本能72を加算する。いなばの白うさぎの2形態の50/75を確認し、IMPORTER_VERSIONだけ6へ更新してsnapshotを再生成した。SQLの構造はschema5のまま。旧snapshotは保持する。

章×効果グループ99件と施設10件、土台・装飾各7種の定義は、同じverified current/manifest/indexからscripts/sync-settings.pyが検証して配布用メタデータへ変換する。土台・装飾の原本値は1/10000の整数で保持する。原本param.tsvの超獣・超賢者倍率を採用し、逆コンパイルに見える既定値で上書きしない。

## 0番台ステージ（0.1.7）

対象はN系列49マップ・324面。stage_mapは名前と元MapStageData、先頭2行、Map_option原値・元行を保持する。stage_crownは現版で照合した各冠の倍率、stage_limitはStage_optionの冠・ステージ・レア度マスクと全原値・元行を保存する。stageは統率力・基礎XP・表示幅・城HP・全体出現間隔・背景・上限数・敵城原ID・時間原値・城バリア・コンテ不可を型付きで保存し、設定/ヘッダー/報酬の全セルを別に保持する。difficultyは小数の原表示値なのでREAL、欠測はNULL。

stage_spawnは出現順を主キーにし、同じ敵の複数行を統合しない。14列の整数を個別保存し、元行と空欄を含む全セルも保持する。catalogへ渡すnative配列だけ列2/3/4を×2する。負値・倍率0・非0の攻撃倍率列11・ボス1/2を保持する。stage_rewardは候補順・比較値・報酬ID・個数・元列を保存し、最終取得確率は生成しない。キャラ報酬はdrop_chara、進化権はunitbuy23、他はGatyaitemNameから名称と画像を結ぶ。

原本はsource_fileでオフライン保持。調査レポートを製品の入力には使わない。stages::importは採用元から直接変換し、stages::catalogはDBから表示を組み立てる。Serviceの/api/stagesとcatalog --kind stagesが同じ変換を呼ぶ。progressionのPR番台は現版39000へ訂正した。

出現行・冠倍率の全件照合はresearch/verify/stage_database.py、元の実命令照合はresearch/verify/stages.py。Web由来の検索と表示は、戦闘状態や報酬取得を完全に再現した証明にはしない。1000番台以降の詳細公開は、番台ごとの確認後に追加する。

## 開発素材（0.1.8）

stage_material_profileは0番台49マップのハズレ値、DropItem.csvの元行・全セル・原本参照を保存する。stage_material_crownは4冠の係数、stage_material_countは8枠の抽選基準回数、stage_material_weightは16以内のスロット・素材ID・重みを分離して保持する。係数と回数は原本をf32で読み、REALへ格納する。通常報酬の比較値や冠の敵倍率と混同しない。

素材IDはGatyaitembuy.csvの種別列6=7とスロット列7から導出し、同版006f308cの16件に一致した。ID配列をRustへ固定していない。原本2ファイルと使用する素材アイコンを保持し、catalogへmap.materialsと名称・画像を出す。素材IDもステージ検索の報酬条件へ含める。

stage_materials::importはstages::importのマップ・ステージ作成後に実行し、readは保存値から表示用の入力を組む。確率はDBへ固定しない。calculateNativeのmaterialDrops配列→Service→kbcs-bridge::materials::plan→C++が冠・ステージ別の抽選回数と確率を計算する。実データの全49行・冠196値・回数392値・重み・原本SHAはstage_database.pyで比較する。
