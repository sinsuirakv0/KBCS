# 砲のSE・到達位置と敗北文字の移動（2026-11-05）

原本はJP15.7.2 / ARM64 / SHA256 `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`。保存済み疑似コードと同じSOの実命令を使用する。

## 砲の音

005d8f58の発射SEは従来の対応で一致していた。欠落は006eb464の城の行動更新。以下を同じ更新位置へ追加した。

|砲|行動更新の通知|
|---|---|
|通常砲|行動1の17F目で25停止。行動2で4Fごとに空き波動枠を確保できた時だけ26再生|
|かみなり砲|行動4でencoded[1]を超えた時に36再生|
|水鉄砲|行動7でencoded[1]を超えた時に83再生|
|エンジェル砲|行動9の17F目で84停止。行動10で空き枠確保時だけ85再生|
|キャノンブレイク砲|行動11の5F目で86再生。発射入口では鳴らさない|

26/85だけは005bc058が0の間に再生し、その他の上記再生・停止は同じ終了後ゲートを追加しない。スロウ・鉄壁・呪い砲を含む全8種の発射入口と状態遷移を比較した。005d6740/005d6c3cには追加の直接SE呼出はない。音源を推測で追加しない。

`BattleSoundScope` → `KbcsBattleSound` → Rustの借用記録 → `battle-audio.js`。`id >= 0`は従来通り再生、`id < 0`は`~id`を停止する内部命令とし、構造体の8バイトとABI5を維持した。停止は音量0でも適用し、未デコードの古い再生が停止後に始まらない。高速実行で再生・停止が1バッチでも元のF差で停止する。追加した音源は開始暗転中のpreloadへ含めた。

## 到達位置

006ddfb8の006dffb0..006e026c。009f65a4..009f6620の実命令は`img002.png`/`img002.imgcut`を作り、TextureContext+0x3d0へ格納する。既存の地域別素材では`Image/img002_ja.png`、`ImageData/img002_ja.imgcut`。部品0が地面の位置、部品1が上下する矢印。

描画条件は戦闘mode=0、unit mode有効の陣営、城word29が非0、word12が0。砲の種類だけから常時表示にしない。005bf658の整数除算後に陣営別±27を加え、射程word6×160、陣営別±92、カメラ左端 `(300-camera)/10+96`、viewport補正を原本順に適用する。部品0はY410、部品1は地面位置のX-30、alpha216、相手側は水平反転。矢印Yは0044aa9cのsinと006e0250の単精度FMADDを使う。

時計game+32f9bcは006db884で進む。論理速度ループに入る前の表示更新であり、所有`display()`の独立時計に対応する。ポーズ中は停止する。RustのSessionは画像・切り抜きを開始時に準備し、C++の描画命令を既存のscene zoom/段数変換で表示する。座標の計算をJSに複製しない。

## 敗北文字とヒント

005ecde0はタイトルYへgame+32e068を足す。005eb894..005eb8dcの実命令は、この値を10ずつ減らして-100で止める。現実装はコンティニュー不可のphase2→4の時計を移植しながら、その枝とは別の「ヒント」パネルを表示していたため、Y差分0の敗北文字と重なった。

phase0の20更新、phase1の44更新、phase2の80更新を維持し、その次から10更新で-100へ移動する。タイトルは242→142。その後にだけヒントを抽選し、0/50/80/90/100%で開く。タイトル移動中はヒントを生成・描画しない。phase4の次更新で原本のSE42を再生する。

本家のコンティニュー可能な枝は、移動終了後にphase3の購入・広告・中断メニューへ入り、ヒント操作の確定後にphase4となる。KBCSにはそのメニューを設けないため、移動が完了した境界で既存のヒントへ直接つなぐ。これはKBCSの接続方針であり、実アカウントや広告の処理まで再現したという意味ではない。phase2→4のコンティニュー不可用パネルとヒントを混同しない。

## 検証

- `research/verify/actor_cannon.py`：発射128、行動/SE1,352、命中288、接触24、雷砲32条件でARM64と一致。行動は両陣営・空き枠あり/なし・終了modeを含む。解析DLLの`kbcs_audit_cannon_action`で同じ所有SE通知を採取する。
- `research/verify/cannon_presentation.py`：カメラ・両陣営・射程・奇数viewport・充填/表示フラグ・sin位相の768条件。原本の描画呼出から部品・整数XY・alpha・反転を取得して比較。敗北は154更新を連続実行し、タイトル描画XYも005ecde0の実命令と比較。
- `battle-audio.test.mjs`：再生中/取得待ち/音量0の停止と、同一バッチの再生→停止。
- 所有Battleの既存砲テストに、17Fのビーム停止→波動音の順序を追加。

研究DLLは`tests/effect-state-probe.cpp`と通常ソース（actor.cppを除く）から生成する。出力・大きな実測結果はresearch/.localに置く。実行例：

```powershell
python research/verify/actor_cannon.py --python-libs research/.local/python-libs --library research/.local/cannon-presentation-20261105.dll
python research/verify/cannon_presentation.py --python-libs research/.local/python-libs --library research/.local/cannon-presentation-20261105.dll
```

ウィンドウ・音声ライブラリ・描画機器・ネットワーク等は局所実行用に制御した。GPU画素・実音源出力・全mainの連続実行の一致を証明する検査ではない。実画面は利用者が確認する。

最終チェック: bridge 37件＋文書試験1件、app 10件、SEと一覧のNode回帰、release clippy（-D warnings）、releaseビルドが成功。既存の生成C++由来の11警告は今回の変更外。確認用バイナリは`.local/dist/cannon-presentation-20261105/`へ必要な4 DLLとまとめ、ビルド出力とのSHA256一致を確認した。画面操作・GitHubへの書き込みは実施していない。
