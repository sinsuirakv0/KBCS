# 自動操作と生産価格（2026-10-27）

JP15.7.2 / 1507021 / arm64-v8a、SO SHA256 `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`。参照リポジトリとGhidraプロジェクトは変更しない。

## 呼出と所有

`battle_screen::advance` → 表示tickのhook 3 → `KbcsBattle::automatic` → `kbcs_core_battle_computer`。原本は006d6d04の論理Fループ後に006ee6c8を一度呼ぶ。速度2/3でも自動判断を論理Fごとへ増やさない。暗転、一時停止、押下後の5tickガード中は呼ばない。GUI操作と自動操作は同じdeploy/fireを使用する。構築失敗時のSEは原本param_4/param_2の通知指定を保持する。

C++所有者が選択action、抽選添字、候補10/圧縮候補10、財布強化時の保持値、砲の判断段階/待機を保持する。bridgeのComputerは読取専用snapshotで、Rust stats → runtime.computerへ返す。JSに別の選択器・時計・乱数を追加しない。

006ee6c8の外部getterだけをKbcsComputerInputへ解決する。空枠、可否、再生産、精霊active、資金、財布、価格、砲の現在値、ページ状態、相手51枠を渡す。rawはDB ID+2。`mode`は原本game+0x2971f0の生産警告時計に対応し、通常は0。所有接続も[結果と制限](battle-result.md)で原本の警告時計を渡し、ルール3/7と固定資金の例外をeligibleへ反映する。解決済みeligibleの局所照合を、それらの完全な呼出元検証と扱わない。

## 判断の順序

1. action未選択時に出撃可能候補を作り、RNG(100)で財布側/通常側を選ぶ。候補数1でもRNGを省かない。選択した出撃枠を資金待ち・ページ待ちの間保持する。
2. 砲が充填済み・非発射中なら相手1..50を走査。射程内の判定→RNG(150)待機→RNG(2)の2段階判断を行う。自城付近の別走査では行動4を除外しない。
3. 選択枠が反対のページなら切替開始/逆向きからの戻しを要求する。既存の5tickページ描画を使い、瞬間的に選択ページを書き換えない。2段表示を理由にこの分岐を削除しない。
4. 財布強化、砲、出撃の原本分岐を実行する。砲発射失敗は選択1を保持し、成功した005d8f58側だけが解除する。出撃は009f4a74呼出後に解除する。

005bf6c8/005bf658は `(worldX-camera)/10` をそれぞれ整数化して比較する。先にworld座標の差へまとめると端数が変わる。砲の距離表00c24400の160、城の27/89/200も原本値。C++の共通random_boundedを使用し、描画・音の有無で本体RNG消費を省略しない。

## 生産価格

005be130 → `kbcs_core_production_price` → `KbcsBattle::cost`を共用する。rule11はcountと原本順の3整数。現版の実例はA081（内部24081）、`[0,200,99999]`。Rustは実DBのmap.rulesから渡す。

- ルールなし、またはlast_cost=0ならbase。生産回数が非0かどうかへ置き換えない。
- mode0はlast_costに `((base/100 × percent)/100) ×100` を加算。
- mode1はlast_costに `((last_cost/100 × percent)/100) ×100` を加算。
- 原本順に上限（3列目×100）を適用する。浮動小数へ置換しない。
- 非0last_costで3列未満なら原本は境界失敗に進む。C ABIは出力を変更せずエラー1を返す。

価格は1/100円で統一する。実支払い、次の候補判断、返金の価格getter、runtime.costsを同じ関数へつなぐ。UIはruntime.costs/100の整数部を表示し、初期deployment.costで上書きしない。C++所有時の手動押下は古い初期価格で事前拒否せず、実deploy側でその時の価格/資金を再検査する。成功後だけlast_costが更新される。

## 照合

`research/verify/battle_computer.py`は640条件×4呼出で、006ee6c8の全候補/保持値・操作要求・ページ要求・RNGを比較する。砲のrange helperも実命令を実行する。外部のプロフィール/可否/財布/価格/再生産、個体生成/発射、音声、009e57b8の集計は制御した比較。全main連続一致の証明ではない。

`production_price.py`は005be130の原本分岐・整数化・cap・不正な列数を比較する。詳細の件数と最終DLL SHAはresearch/.local/battle-computer-1572.json、production-price-1572.jsonへ保存する。

所有接続のbatch/単F比較はbattle-computer-input.json（財布0→自動強化、下段の枠、1段、速度/CPU ON/OFF、一時停止）とbattle-price-input.json（実DBのA081）を使う。画面はユーザーが確認する。通常勝敗・T/R道場・警告時計・動的ルール3/7は[結果と制限](battle-result.md)で接続。報酬/専用controllerと追加生産ルールは未完了。
