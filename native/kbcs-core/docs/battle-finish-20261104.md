# 蘇生待ち・敗北ヒント・結果からの暗転（2026-11-04）

原本はJP15.7.2 / ARM64 / SHA256 `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`。保存済み疑似コードと同じSOの実命令を使用する。

## 蘇生待ちの骨

006ddfb8の00a9441cは個体word205を返す。unit modeの別経路では0。正なら通常本体を共通の骨へ置換し、行動3/6はback、それ以外はdown。死亡4/21とワープ待機19はこの列に入らない。行動15は本体を描かず、15/16はreviveを追加描画する。16では既に戻った本体とreviveを併せて描く。14だけを条件に骨を表示する実装では、この前後を再現できない。

|TextureContext offset|009f560cのロード先|encoded / plain|
|---|---|---|
|0x1258|set_enemy001_zombie_down.maanim|17 / 16|
|0x1290|set_enemy001_zombie_revive.maanim|41 / 40|
|0x12c8|set_enemy001_zombie_back.maanim|1 / 0|

009f8ed4..009f8ff0の文字列構築と0044ba98への引数を実行して対応を取得し、0044beb4/0044bf2cで長さを照合した。battle-inputsのclocksへ追加。Sessionの既存effect catalogから画像・imgcut・mamodelを取得し、開始暗転中のtexturesへ含める。公式DBの再取り込みは不要。

kbcs_core_battle_visualsのkind12は本体置換、kind13は復活の追加描画。word2の時計と同じ個体の座標・レイヤーを使い、独立した残留タイマーを作らない。Rustは共通モデルを通常の本体用基準点へ再配置せず描く。波動等の所有演出の走査は継続する。

## 敗北ヒント

Rustはres/Lose_ja.csvとData/LoseTextSetting.csvをDBの採用原本から読み、文面と数値条件へ分ける。CSVの先頭は分類ID、後続は最大5行。全角＠で打ち切り、途中の空文字は行として保持する。

kbcs_core_battle_hint_candidatesは00701164→007013b8/0070195cに対応。章・冠・特殊モードの条件を満たす一般候補を順に集め、列27/28以降のステージ指定（1=map×100+面、2=map）が初めて成立したら一般候補を消す。以降は専用候補だけを保持する。候補は分類IDではなくLoseの行番号。

利用者指定により、KBCSでは全章解放・通常の進行済み状態を採用する。HintContext.progress/cosmosは原本game+334048/+334056の解決入力で、今回は両方1。nativeMode・nativeId・面・冠は実ステージから取得する。0065054cの特殊条件はnativeKind=-19またはnativeKind=-8かつmap番号42。アカウントの進行状態を編成レベルや所持数から推定しない。

候補と行数は0Fに所有C++へ渡す。既存の敗北結果がphase4へ入る際、00701b78どおり非空候補なら共通RNGを1回消費して選択（1件でも消費）。空なら行0へ戻りRNGを消費しない。描画取得で再抽選しない。

005ecde0のヒント背景はTextureContext+8、00adcbccで読むimg005の部品0。中央X、中央Y440、690×229、拡大率0/50/80/90/100%。文字は30px、36px間隔、先頭Y=440−行数×18。kbcs_core_battle_hintが矩形と時計を返し、battle-results.jsが原本文面を描く。コンティニュー・広告・統率力返却の専用パネルや実アカウントの進行保存は今回の対象外。

## OKからの暗転

kbcs_core_battle_screen_fadeへ006994e8の幕の頂点生成を共用した。開始時の幕が晴れる区間は従来どおり。結果のOKは既存の押下/releaseと5更新のguardを通し、その後は所有return_frameの0〜11で覆う区間だけを進める。全面黒になる11までrequest_action=302を返さない。段数・viewportの変更でも同じ共通関数を使う。既存PODのレイアウトとABI5は維持する。

battle-screen.jsは結果画面の早期returnにも幕を重ねる。302を受けたフレームは最後の盤面と全面黒を描き、次のrequestAnimationFrameでSession破棄・出撃準備への復帰を行う。画面が黒になる前にDOMを切り替えない。

## 検証

research/verify/battle_finish.pyは骨のロード名/長さ、006df35c/006df5ecのモデル選択・F・座標、00701164の候補順、所有advanceの終了要求を検査する。effect-state-probe.cppは研究専用DLLで、実デスクトップや所持数を操作しない。--publishは小さい優先順fixtureと素材のclocksを更新し、大きい結果はresearch/.localへ保存する。

```
python research/verify/battle_finish.py --python-libs research/.local/python-libs --assets D:/KBC/KBC-rakv0-assets --library research/.local/battle-finish-20261104-v2.dll --publish
```

実データのヒント候補26条件、骨描画54条件、所有advanceの暗転終了20条件を通過した。

CIはbattle-hint-vectorsで専用候補への切替と順番を検査し、既存のARM64由来battle-screen-vectorsで共用した幕の全24Fを比較する。局所実行ではメモリ確保・vectorコピー・画像ロード・描画デバイス呼出を制御している。全本家mainの連続実行、GPU画素・実フォントの完全一致を証明するものではない。実画面は利用者が確認する。

2026-11-05追記: 敗北タイトルの上方移動を追加し、ヒントとの接続順を訂正。[原本分岐と検証](cannon-presentation-20261105.md)を参照。
