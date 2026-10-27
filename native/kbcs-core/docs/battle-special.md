# 追加生産・イベントPt・対象限定コンボ

原本: JP15.7.2/1507021、arm64-v8a、SHA256 `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`。保存済み疑似コードと同じELFの局所実行を使う。ABI4のRules/Profile/ProductionCostはRustと同時にビルドする。既存DBの再生成は不要。DB詳細等のnative-calculation.jsに残っていたABI2判定と戦闘診断のABI3表記も4へ揃える。

## 追加生産と生産回数条件

`009f4a74`の特殊ルール8は `[レア度mask,追加数,間隔F]`。通常生成成功時にslotと間隔×1..Nを予約する。費用・生産総数・通常生産数・SE19は通常生成に対して一度。現データのSR008/012/017/022/026/027が対象。

`006d7c38..006d7dc4`は論理Fの時間判定より前に予約を後ろから走査する。待機1は0に減るだけで、その次のFに生成する。生成前にslotの通常生産数を1減らし、構築後に復元する。通常の支払い・可否・再生産待ち・生産総数・精霊セットアップを通さず、満員の構築失敗でも予約を消費する。原本の敗北処理005e02b0は予約を空にする。勝利時には予約処理を一律停止しない。

関数関係: `KbcsBattle::deploy`→`production_extra_plan`→所有extras、`logical`→`production_extra_tick`→同期construct→`actor_initialize`。独立した戦闘RNGを共用し、生成失敗時にRNGを巻き戻さない。

`005c2f88`は次の通常生産番号(produced+1)とレア度別periodを比較する。kind0は余り0、それ以外は番号一致。period0もARMのSDIV0による余りを再現する。`005c2ec0/005c2f30`の形態条件を合わせて本能玉へ渡す。構築前の生産数と、成功後の「次回の再生産短縮」の生産数を混同しない。短縮はword250の固有値を先に使い、なければ本能玉19。固定生産時間ルール1なら迂回する。`production_wait`を通常生産と所有側で共用する。

## 生産価格と対象限定コンボ

`production_cost`は00aa0568の0.01円単位を維持する。固定価格4は早期return。通常値は本能25減算→章/マップ倍率→条件付き本能玉22→対象を解決したコンボ27を一つずつ→レア度率5→非負化。乗算の32bit幅と修飾ごとの整数化を保つ。率0の本能玉取得分岐でも端数の整数化は省略しない。動的価格11の005be130は、この都度計算した価格とlast_costを既存production_priceへ渡す。HUD/CPU/支払い/返金のcost getterを共有する。UIの初期価格スナップショットを戦闘の確定価格にしない。

0088fde0/008900xxはNyancomboData.csvの列2をobject+0x10の対象グループへ入れる。0088f9e4/0088faecはactiveの効果だけを走査し、groupが-1でなければ009e4e14を呼ぶ。009e4e14はCharagroup.csvのtype3・明示IDリストへの所属を要求する。現版group10は831..836/857/858。レア度制限用type0/2のグループと混同しない。

`combos::read`は既存source_fileからgroup列を補う。DBのテーブル追加や公式snapshotの書換えを行わない。Rustは全体コンボと対象別コンボを分離し、Rules.unit_combosへ解決済みの加算値、Profile.priceへ対象別の価格コンボ順を保持する。初期速度・stat・命中内のgetterは同期BattleRulesScope中に対象IDを照合し、通常のコンボへ加える。再生産値も当該キャラのcombo11で解決する。単体カーネルのenvironment.combos契約は維持する。Rulesの未使用固定配列はJSONへ展開しない。

## PRのPt・フィーバー・終了

PR000(nativeKind=-26、nativeId39000)はT/R道場の式を流用しない。Data/PointStageSettings.jsonのPointID→MapID対応とStagePointRulesMapのステージ別rawを確認する。前者が旧DBのsource_fileになくても、asset_referenceの固定Git revision/SHAからAppDataの原本キャッシュへ取得する。

00a0cdf4/00a0cfecのevent0は、通常出撃の元コスト（本能や割引前、章倍率あり）に00a0d874の区間率を掛け、100で整数除算する。区間は前の閾値より大きく、今回の閾値以下。0や最終閾値を超える値は最後の率へ入る。event1は敵の最終撃破に対し、money_base/100＋出現行score、残時間比、基本率を使う。蘇生途中の死亡へ加算しない。有限時間はdouble演算後に**実命令FCVTZS W20**で符号付き32bitへ飽和する（疑似コードのuint表記だけを信用しない）。無制限は別の整数経路。合計の上限999999999と32bit加算を保つ。

00645288は各論理Fの最初、mode0だけでFeverのゲージ平滑化・開始・終了を更新する。開始でSE194、wait=600、frame/phase/ending=0、gauge=-1。終了でorigin=現在Ptを保存する。00645444のframe/phaseは表示Fごと。005d996c/005e02b0→00645630は勝敗決定時にending=1を設定し、残るwaitとは別に表示phaseを5まで進めて専用演出を消す。0064556cの初回ゲージ確定は表示末尾のhook5へ置き、HTTPのbatch分割で描画回数に依存させない。

現版のルール12 `[0,25000,600,6,0,0,0,0,0,0]` は先頭3値がFever条件で、4番目はFever中の**別ルールID6**、以降は6レア度の再生産率。固定6Fではない。所有側は通常の研究力/お宝/コンボによるplain再生産値へFever率を掛ける。既存の待機の補正、次の生産、被弾による生産遅延、HUDゲージで同じgetterを使う。原本の006453acは既存個体の速度を再取得するが、現版alternate6は速度を変更しない。他のalternateルールが新設された場合の速度更新まで実装済みとは扱わない。

00a0cdbcの時計は有限limitまで進み、006d7e6cで期限へ達すると行動前に005d996cの勝利mode1へ進む（道場のmode4ではない）。elapsedは締切Fに増やさない。城破壊敗北は005e02b0のmode7。常設操作欄へPt、残り時間、Fever残り、追加生産予約を返す。

## 照合と残り

`research/verify/battle_special.py`は生産条件48、予約計画216、逆順予約80、価格1944、Pt204、Fever800更新、PR時計72をC++へ比較する。加えて対象コンボgetter45件の原本値を採取し、実DB接続のRulesと比較する。ルール/プロフィール・構築/レベル取得・Ptテーブル取得/確保・Feverの音声/速度再取得を制御した局所実行である。全mainの連続比較ではない。

大きい接続fixture/reportはresearch/.localへ保存。PRの通常終了/敗北/Fever、SR017/027の追加生成、対象内と対象外の編成を実DBからheadless再生し、batchと1表示Fの全個体/RNG/SE/結果/予約/Pt状態を比較する。画面はユーザーが確認する。

残りは本家の結果画面全体・結果音声・報酬抽選/保存、Feverの原本ゲージ/専用モデルの描画、ステージ固有のLv封印・専用controllerの残分岐、可変共有モデル境界、画面振動など。今回の数値・状態接続をこれらの完成や、本家との全F/GPU画素一致の証明としない。
