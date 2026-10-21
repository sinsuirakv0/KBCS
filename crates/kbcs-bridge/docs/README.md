# kbcs-bridge

`build.rs`→native/kbcs-coreのC++20をccで静的ビルド。ABI=2、ruleset=1507021。固定幅PODの借用は呼出中だけで、所有権と例外を渡さない。

`stat`、`unit_hit / unit_damage`、`enemy_hit / enemy_damage`、`unit_metal_killer`、`enemy_poison`が安全なラッパー。4つの命中結果の期待値はC++から返す。割合予約の結果VecはRustが所有し、C++へは1件ごとの固定幅値だけを渡す。

計算・出現・XP・開始・素材の5つの回帰テストで実命令由来のfixtureを照合する。入力の上限外と整数上限も拒否する。意味・単位・根拠は[nativeの設計](../../../native/kbcs-core/docs/README.md)。状態を所有する未使用の戦闘APIは追加しない。

`stage::tick / commit`は借用したRow/State/ContextをC++へ渡す。長さ・候補番号をRustでも検査し、C++のエラー値を返す。状態の所有権・乱数の所有権は呼出側に残す。敵生成が成功してからcommitする関係は[出現処理](../../../native/kbcs-core/docs/stages.md)。UIやHTTP計算APIには未接続。

`experience::legend`は0番台XPの固定幅入力を借用して5段階を返す。C++で演算順と整数境界を共用し、UI専用のXP数式は追加しない。

`stage::initialize`は入力検査後に行状態を初期化し、敵城行を返す。`materials::plan/pick`は同じ固定16枠の入力から理論値と実抽選を分けて呼ぶ。乱数消費順と所有権は呼出側が管理する。
