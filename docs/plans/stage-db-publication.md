# ステージDB公開の完了記録（2026-10-23）

依頼「DB完成＋公開まで」は、同版に存在する全系列の閲覧DBとローカルアプリ/プレビューの公開まで完了した。GitHub書込・外部ホスティングは行っていない。

## 公開物

- 実行版：`.local/dist/0.1.15/kbcs.exe`と同梱DLL。schema8/importer9、ABI2/ruleset1507021。
- 通常DB：`C:/Users/ABC/AppData/Local/KBCS/official/jp-fb87935b9bee241e538b0222a3c4af6739a54c16d6a47573d1f809a7cb165411.sqlite`。
- 通常プレビュー：127.0.0.1:4817、PID18548。実行元・引数・非表示窓を再確認して更新する。試験用4820/4821/4822は停止済み。
- 前ポインタ`.local/current-before-0.1.15.json`と旧snapshotは保持。実験v1/v2/v3は途中生成物であり公開しない。最終候補は`.local/full-stage-db-v4`。

## 内容と検証

全29系列、1298マップ6476面、6333戦闘定義62488出現行、3088候補。通常5771/重み3673/スコア2706/クリア回数44の計12194報酬。未来編144面315スコア報酬、固定編成10preset、本能玉164種類の名称/合成画像を接続した。

`all_stage_database.py`で公開先の全ヘッダー/出現・7631原本・一覧メタ/物理値・全報酬と、preset10件/本能玉原本9件を比較。一致。`stage_database.py`で0番台324面2924行/196冠と素材の回帰も一致。workspace17＋compile_fail1、clippy全target、JS構文、release、CLI verifyが通過。

実ブラウザーは全系列検索、G002固定編成/Lv15、ITF1スコア報酬、L/D候補切替、PRのPt/時間/XP、A055本能玉7アイコン、COTCZ-I、N000の4冠/素材確率を確認しconsole警告/エラーなし。`.local/verify-stage-search.mjs`で29系列の抽出とD000の別候補を跨ぐAND誤一致防止、本能玉報酬検索を確認した。

主要関数はimporter→定義/一覧/報酬、extras→条件/固定編成/候補、rewards→本能玉の表示原本。search_catalog→軽量索引、catalog_map→詳細、variant→許可候補だけ返す。stageExperienceは章/内部種別を保つ共通C++経路。docs/data/README.mdと各領域docsへ契約を保存した。

## 残る別領域

原本がない日本編ゾンビ2/3章の月、一覧外定義の統率力/XP、廃止/未使用報酬の名前は欠測として保持する。期間/解禁、クエストの実抽選、迷宮の編成消耗、戦闘全体、報酬実付与・セーブは閲覧DBと分離して今後実装する。原本にない仕様を推測しない。

Windows Store版pythonはAppDataを仮想化するため通常DBを参照できない。通常保存先の検証には`C:/Users/ABC/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`を使う。大報告はresearch/.local、研究原本と参照リポジトリは保全した。

公開画面の確認画像は`.local/stage-db-0.1.15.png`。DB/実行ファイルのSHAと旧snapshot保全の記録は`.local/publication-0.1.15.json`。
