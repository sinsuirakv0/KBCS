# その他モーション（0.1.17）

2026-10-23。味方・敵とは別にその他モーションの入口を追加し、同じビューア/姿勢/WebGLを流用。ユーザー指定に従い、形式・演出は既存の検証済み処理を使って軽く照合した。

## 公開物

- `.local/dist/0.1.17/kbcs.exe`、schema8/importer12、ABI2/ruleset1507021。
- DB：`C:/Users/ABC/AppData/Local/KBCS/official/jp-c59d3381716e75249c6ebda4a38a00da42915248a1e7ee6849af2a1e011769ca.sqlite`。旧snapshotと`.local/current-before-0.1.17.json`を保持。
- 通常プレビュー4817、PID13584（停止時に実行元/引数/非表示を再確認）。試験用4822は停止済み。
- 433モデル、386件の素材対応を解決。47件は切り出し対応不明として一覧に残し、選択不可。未知の対応を推測しない。

## 構成

effects::importはその他の定義と対応画像、param.tsvを原本hash付きで保存。effects::catalog/manifest → Service → 既存viewer.jsへ接続。CLI catalog --kind effects / motion --kind effectも共通。素材所有は最長stem、skill画像はmodelパーツid、敵専用maanim優先、単一モデルは静止表示。ヘッダーのskill999等は同名PNGより優先しない。一方bg06→bg102等、同名PNGがない場合は実在するヘッダー画像へ結ぶ。

ホームのその他モーションと対象切替からアクセス。名称/ID/分類、ファイル/分割/パーツ、1F・拡縮・反転・表示マスク・PNGを流用。波動/小波動・烈波/小烈波・爆波は素材単体と一連の演出を切替。Lv1〜20が即時反映。バリアは通常/ブレイカー/破壊を選択できる。生き残り・バリア・城バリア・悪魔シールドを区別し、悪魔シールドをファイル名だけで味方と表示しない。

## 検証

- workspace18＋compile_fail1、clippy全target、release、CLI verify、JS syntax、diffチェック。
- 既存取り込み試験へ、誤ったskill999ヘッダーよりmodel idの画像優先、敵専用maanimの分離、別名PNG、静止モデル、不正IDを追加。試験関数は増やしていない。
- 既存15.7.1 ARM32の演出境界72件を照合。現版15.7.2 ARM64の009f560cで烈波/バリアの素材xrefを軽く確認。版/SHAはモーション領域docsに保持。
- 現snapshotの代表16素材、493姿勢、10013描画packet。旧DBの全source_file path/SHAが残り、キャラ/敵/ステージ/報酬/候補の件数も一致。
- 実ブラウザーで波動11Fの3片、烈波20Fの52パーツ、Lv20→424F、生き残り10Fの10→9パーツ表示、バリア破壊/45分割、敵わんこの2パーツ、分類、ファイルを確認。consoleエラー/警告なし。

`.local/effect-resource-report.json`、`effect-pose-report.json`、`effect-sequence-report.json`と`publication-0.1.17.json`が根拠。最終画面は`.local/effect-motion-workspace-0.1.17.png`。

## 境界

閲覧用の素材・演出時計であり、当たり判定・ダメージ・状態発動/解除・キャラ追従・音声・戦闘ランタイムは別。共通JavaScript姿勢評価のC++移植も引き続き未完。形式の全命令/全素材の実機ピクセル一致は今回再監査しない。GitHub書込・外部公開・PC終了は行っていない。
