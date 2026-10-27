# KBCS 0.1.35 調査用の現状（2026-10-28）

この版は開発途中の戦闘シミュレーターを含む。ソース一式（C++/Rust/HTML/CSS/JavaScript、生成済みinc、数値fixture、検証スクリプト、保存済み参照ページ）を同じコミットへ保存する。GitHub ReleaseにWindows x64アプリと同じコミットのsource ZIPを置く。AppDataのユーザーDB・取得済み原本キャッシュ・大きいローカル実験生成物・会話添付はソフトウェアのソースに含めない。

アプリ/3クレートは0.1.35、C ABIは4、公式DB schema8/importer13。根拠はJP15.7.2 / 1507021 / arm64-v8a / SO SHA256 `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`。描画の旧版由来部分はrender.mdの個別出典に従い、すべてが現版ARM照合済みとは扱わない。

過去のdocsは各版時点の構築記録で、「未接続」のまま後続の追記で実装されたものがある。まずこの一覧と対象の最新追記を読み、未実装と未検証を分けて調査する。

## 調査の入口

|領域|主要な実装|関係・出典|
|---|---|---|
|画面/API/所有|[battle-screen.js](../../ui/battle-screen.js)、[Session](../../crates/kbcs-app/src/battle.rs)、[bridge Battle](../../crates/kbcs-bridge/src/battle.rs)、[actor_battle.inc](../../native/kbcs-core/src/actor_battle.inc)|入力→Rust原本解決/排他→C++所有Battle→共用GPU命令。[更新順](../../native/kbcs-core/docs/battle-runtime.md)|
|個体/命中/効果|[actor.cpp](../../native/kbcs-core/src/actor.cpp)、[actor_generated.inc](../../native/kbcs-core/src/actor_generated.inc)、[actor_secondary.inc](../../native/kbcs-core/src/actor_secondary.inc)|[命中の制御入力と照合範囲](../../native/kbcs-core/docs/hit-runtime.md)、[二次攻撃](../../native/kbcs-core/docs/secondary.md)。生成済みincもソースへ含む|
|出現/生産/砲|[stage.cpp](../../native/kbcs-core/src/stage.cpp)、[production.cpp](../../native/kbcs-core/src/production.cpp)、[actor_cannon.inc](../../native/kbcs-core/src/actor_cannon.inc)、[actor_sniper.inc](../../native/kbcs-core/src/actor_sniper.inc)|候補→構築→間隔抽選→commitのRNG、支払い/再生産/枠制限。原本のtickとcommitの分岐を同一視しない|
|勝敗/スコア/報酬|[actor_result.inc](../../native/kbcs-core/src/actor_result.inc)、[actor_points.inc](../../native/kbcs-core/src/actor_points.inc)、[actor_ending.inc](../../native/kbcs-core/src/actor_ending.inc)、[battle_rewards.rs](../../crates/kbcs-app/src/battle_rewards.rs)|[結果と制限](../../native/kbcs-core/docs/battle-result.md)、[特殊戦闘](../../native/kbcs-core/docs/battle-special.md)。通常時間/道場/PRは別式|
|上部/終了UI/音|[actor_top.inc](../../native/kbcs-core/src/actor_top.inc)、[battle-results.js](../../ui/battle-results.js)、[battle-audio.js](../../ui/battle-audio.js)|[HUD](../../native/kbcs-core/docs/battle-screen.md)、[音源と発音条件](../../research/docs/audio-1572.md)。数字/座標/時計はC++、GPU/音声デバイスはUI|
|保存|[inventory.rs](../../crates/kbcs-data/src/inventory.rs)、[battle_options.rs](../../crates/kbcs-data/src/battle_options.rs)|報酬transaction/重複claim防止、表示数と累計を分離、キャラ所持/解放、音量/段数。編成と公式DBから分離|
|原本/再生成|[research](../../research/README.md)、[生成器](../../research/cli/export_actor.py)、[検証群](../../research/verify)|版/ABI/SHAを固定。巨大Ghidraキャッシュや局所実験の報告本体はresearch/.localでGit除外。公開済み原本参照ページと取得手順はresearchに保存|

## 現在接続されている範囲

- 通常の出撃/敵出現、レベル/本能/玉/お宝/施設/コンボの入力解決、移動/攻撃/命中/HP/KB/死亡/退場、各種妨害/保護/二次攻撃を所有Battleで進める。精霊、城砲、スニャイパー、ボス衝撃波、CPU、追加生産も接続済み。単体カーネルの照合と、全条件の実戦一致は別。
- 既存ステージ検索→準備→暗転中の素材読込→戦闘操作/一時停止/コマ送り→勝敗→結果/通知→報酬/記録保存。持ち物の表示数と獲得累計、キャラ所持状態を保存する。
- T/R道場の時計/撃破Score/マップ別能力ボーナス、通常時間スコア、PRのPt/Fever/時間勝利。戦闘上部のScore/Pt/残時間/Fever、左上の原本ステージ名画像を接続した。
- 致死攻撃時の未出現ボス前の城HP1保持、次Fのボス/衝撃波/城破壊/死亡/勝利の順序を修正。結果帯は原本の乗算描画。操作/命中/勝敗/結果通知のSE条件と非同期音声取得の境界も修正した。

## 未実装・接続が残るもの

1. 自作マップの編集/保存/出撃。現行stage-playの「自作マップから」はdisabled。
2. ステージ固有のLv封印と専用進行controllerの残分岐。例: DemonCastlelimit.csvはDB詳細のlevelSealへ出るが、Sessionの実効Lv計算にはまだ接続されていない。ステージDB全29系列が揃っていることは、全系列の戦闘専用進行の完成を意味しない。
3. 一部の専用演出/画面揺れ。ボス衝撃波の押し戻し/画像/SEは接続済みだが、actor_bossのshakes回数を画面へ反映する経路はない。PRの上部Feverゲージは接続済みであり、ゲージ全体を未実装扱いしない。専用モデル/終了過程すべての再現は未完了。
4. 音声ID29の原本同様の動的差替え、Androidのpriority/音声資源管理との一致。SEの発音条件やWebAudioの基本接続自体は実装済み。通信/広告等のアカウント専用通知は再現範囲外。
5. APK出力/AI制御など将来機能。物理振動はユーザー指定で実装対象外とし、不具合には数えない。

## 実装はあるが照合が終わっていないもの

- 原本main全体と同じ初期状態から全Fを連続比較する試験、全マップ・全能力組合せの実戦照合。
- 可変共有モデル/直前姿勢による当たり境界と全階層、Android GPU画素/フォント字形、全専用結果画面/アカウント進行との照合。
- 全負荷/全PCで30FPSを保つ保証。操作・計測欄とAPI最適化は実装済みだが、現在のAPI計測をGPU実行時間や実機同一性の証明にはしない。

## この版に含める検証

前回の同じロジックの確認ではworkspace33件＋compile_fail1、clippy all-targets warnings禁止が通過。原本局所比較は命中1245条件、撃破720条件、ScoreBonusMapの全12マップ1200条件、上部描画の補間128/配置152条件など。制御したgetter/入力/描画捕捉と、全mainの連続実行を区別する。

最新UI接続は実DBの18ケース（12ボーナスマップ、T000/R030の時間終了、PR通常/Fever、S060スコア、N000勝利）と画像取得をheadless確認。資金/城HP/編成を制御したfixtureであり、battle-replayはmemory報酬Storeを使う。原本比較の詳細や実験ハッシュは各領域docsと[再開記録](resume.md)に残す。0.1.35の配布にはビルド/検証記録を同梱する。

ビルドはREADMEとscripts/build.ps1、最小回帰は`cargo test --workspace --locked`、`cargo clippy --workspace --all-targets --locked -- -D warnings`、`node ui/tests/battle-audio.test.mjs`。検証スクリプトの原本再実行には別取得の対応版キャッシュとUnicorn等が必要。画面確認はユーザーが担当し、今回の公開準備で起動中アプリは操作しない。
