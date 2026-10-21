# 調査資産と参照先

既存 `research/` は移動・削除せず保存する。入口は [research/README.md](../../research/README.md)。検索は `python research/cli/cache.py stats/find/strings/code` を使い、必要な関数だけ読む。

2026-10-21にstatsを実行して、15.7.2 / versionCode 1507021 / arm64-v8a / SO SHA-256 `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`、内部25,234、疑似コード25,232、失敗2を再確認した。既存MCPの15.7.1 ARM32とは別物。今回、Ghidraプロジェクトは開いていない。

|資料|将来の利用|
|---|---|
|[全関数報告](../../research/docs/complete-report.md)|対象版・SHA・保存率・失敗・限界|
|[解析設計](../../research/docs/architecture.md)|索引・呼出関係・版別資料の仕組み|
|[保存と復元](../../research/docs/github-storage.md)|Private Release・元APK・独立プロジェクトの取得|
|`research/.local/reference.json`|ローカル検索CLIの対象登録（Git除外）|
|`research/cli` / `indexer` / `ghidra`|検索、抽出、原本追跡の既存実装|

Web側の実際の解釈元は隣接 `KBC-rakv0-lab/unit-db/compile.mjs`、`source.mjs`、`overrides.mjs`。`kbc-web/tools/unit-data.js` は生成済みschema9 JSONを配信するだけ。Web UIの実装は `src/features/units/{model,detail,calculator,view}.js` と `src/shared/game/unit-stats.js`。配色は `src/shared/ui/tokens.css`。

敵はlab/enemy-db/compile.mjsで味方と異なる列配置を使う。ステージはlab/stage-db/compile.mjsおよびdefinition/catalogで階層・出現・制限を処理する。ID単独で統一せず地域・グループ・階層・variantを将来の設計で扱う。今回はこれらのDBを生成していない。

モーションはlab/unit-db/compile.mjsのanimationLength、Webの `shared/game/character-motion.js`、`motion-project.js` を確認。imgcut/mamodel/maanimとPNGの関連、共通ID・mコードを参考にした。完全な姿勢計算・補間・再生は未移植。補完素材の入手先とゲーム原本を混同しない。

labの `unit-db/docs/native-verification.md` は15.7.1 ARM32の命令実行と制御データによる計算順の調査で、15.7.2 ARM64の戦闘全体の証明ではない。今後のC++実装では対象版の検索CLIから根拠関数を選び直す。今回の表示用参考値を本家戦闘仕様として昇格させない。

ステージの現版調査は[番台別の記録](../../research/docs/stages/README.md)へ分離した。分類関数・章例外・0番台の全定義と通常城の出現判定を照合済み。報酬・敵城・制限の全挙動は未確認。調査結果を即座に確定DBへ移すことはせず、各番台の分岐と未確認事項を残す。

続きでは、敵城指定と原CSVフラグを分けた出現判定、レア度制限、ボスフラグと通常報酬比較を追加照合した。借用状態へ適用する待機・候補選択・生成成功後更新は[共通C++](../../native/kbcs-core/docs/stages.md)へ実装。敵生成・初期化・報酬の取得済み分岐は残っており、戦闘全体の再現ではない。
