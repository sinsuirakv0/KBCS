# kbcs-bridge

`build.rs`→native/kbcs-coreのC++20をccで静的ビルド。ABI=3、ruleset=1507021。固定幅PODの借用は呼出中だけで、所有権と例外を渡さない。

`stat`、`unit_hit / unit_damage`、`enemy_hit / enemy_damage`、`unit_metal_killer`、`enemy_poison`が安全なラッパー。4つの命中結果の期待値はC++から返す。割合予約の結果VecはRustが所有し、C++へは1件ごとの固定幅値だけを渡す。

計算・出現・XP・開始・素材・敵基礎値・報酬の乱数を含む8つの回帰テストで実命令由来のfixtureを照合する。入力の上限外と整数上限も拒否する。意味・単位・根拠は[nativeの設計](../../../native/kbcs-core/docs/README.md)。状態を所有する未使用の戦闘APIは追加しない。

`stage::tick`はRow/State/Contextを借用したPendingSpawnを返す。生成成功時に候補のcommit(self, ...)を1回だけ呼ぶ。長さ・候補番号をRustでも検査し、C++のエラー値を返す。状態の所有権・乱数の所有権は呼出側に残す。敵生成が成功してからcommitする関係は[出現処理](../../../native/kbcs-core/docs/stages.md)。UIやHTTP計算APIには未接続。

`experience::legend`は0番台XPの固定幅入力を借用して5段階を返す。C++で演算順と整数境界を共用し、UI専用のXP数式は追加しない。

`stage::initialize`は入力検査後に行状態を初期化し、敵城行を返す。`materials::plan/pick`は同じ固定16枠の入力から理論値と実抽選を分けて呼ぶ。乱数消費順と所有権は呼出側が管理する。

`enemy::stat`は敵基礎値の3段階、`reward::legend_pick`は通常報酬の候補・比較乱数消費数・取得済み記録要求・レーダーによる打切りを返す。入力乱数/セーブ/取得済み状態は呼出側が所有する。現在は乱数も含む8テスト（workspace全体11件、Service境界を含む）と候補再利用のcompile_fail 1件。同版実命令のfixture比較をまとめ、入力不正時の部分更新がないことも確認する。

0.1.11はexperience::event、reward::stage_pick / weight_total / weight_pickを追加。acquiredは先頭の報酬種別に応じた保存フラグ/所有判定を解決して渡す。重み合計→乱数1回→選択の所有順と未実装境界は[native設計](../../../native/kbcs-core/docs/event-rewards.md)。既存の2つの回帰テストへ追加した。

0.1.12はscore::calculateとreward::weight_finishを追加。前者は数値と新規報酬mask、後者は履歴/付与要求を返す。保存と付与を所有しない。[関数の関係と実行順](../../../native/kbcs-core/docs/stage-score.md)。bridge9件/workspace12件とcompile_fail 1件。

## 0.1.13の追補

[所持数・保存先・時計・EX抽選](../../../native/kbcs-core/docs/inventory-ex.md)。スコア旗309面のうち保存番号なし8面は原本が処理を省き、有効301面へ訂正。通常取得済みもヘッダー専用保存番号を使う。旧版の照合件数を実対象の完成数と混同しない。実所持数の数値245定義とEX抽選を追加し、専用通貨・解放・永続化・期間判定は別途確認する。

0.1.14の[39000番台までの共通入口・実測・未確認範囲](../../../research/docs/stages/all-bands.md)。stage_source、stage::Row::decode、experience::stageを追加。原本の分類とファイル選択を、専用戦闘ランタイムの完成と混同しない。

`actor::Pool`は2陣営×51枠の個体をRust側で所有し、各呼出中だけC++へ借用する。initialize/contact/matches/roll/effects/clock/begin/walk/motion/resume/damage/protect/health/react/transition/unit_knockback/enemy_displacement/enemy_knockback/retire/intent/attack_wait/attackは同版の状態関数。内部ポインタを保持せず、RNGはRandomを共有する。health/reactの中間状態を原本のフェーズ順で接続する責務は呼出側に残る。[原本・入力契約・照合範囲](../../../native/kbcs-core/docs/actors.md)。GUIやHTTPへ個体を生成する接続はまだない。

`actor::emit_direct`はattackの同期callbackから同じ個体配列/RNGを再借用できる。`actor::Waves`は200枠と51対象の命中履歴を所有し、直接命中後の抽選結果から波動を生成する。その後`actor::emit_area`で烈波→爆波の生成記録を取得し、次の攻撃段より前にC++所有の`actor::Areas`へappendする。数値部分のみを渡し、原本の生ポインタ/履歴木の内部表現はABIへ含めない。

`Areas::step`はSurges→Reflections→Explosionsの順に呼び、共通のpanic捕捉callbackから個体/RNGを同期借用する。反射/再命中/寿命/区画履歴とSE/振動を所有し、`retirement_blocked`はWavesも含む原本の経路別走査を返す。エラー/panic後は同じ所有状態の継続を拒否する。詳細と原本へ照合した範囲は[二次攻撃](../../../native/kbcs-core/docs/secondary.md)。命中関数内部と全戦闘の所有ランタイム/画面接続は残る。


2026-10-27: 所有BattleのComputerとpricesはC++保持値のsnapshot。表示更新の判断と論理更新を区別する。原本/ABI/局所照合は../../../native/kbcs-core/docs/computer.md。


所有Battleのoutcome/deploymentはC++の結果・同時数・総生産数・警告時計を取得する。RulesはDB解決値、Outcome/Deploymentは所有者の読取専用スナップショット。ScreenState末尾battle_modeは旧JSONで省略可能だが、FFI利用者は同時に再ビルドする。[関係と未接続範囲](../../../native/kbcs-core/docs/battle-result.md)。

ABI4: battle::RulesへPt/Fever/追加生産/対象別コンボ、Profileへplain再生産とProductionCostを追加。C++と同時ビルド。extras()/points()はC++所有状態の読取。未使用の固定配列をJSONへ送らない。[関数関係](../../../native/kbcs-core/docs/battle-special.md)。
