# 戦闘エフェクトの状態監査（2026-10-30）

## 結論と対象

表示座標の調整では解決しない実装差を6件確認し修正した。報告された2症状に直結するのは、呪いの素材誤登録と、被弾時のバリア/悪魔シールド表示時計の欠落。ゾンビキラー死亡プールの漏れを今回の症状の原因と断定する証拠は得ていない。

原本はJP15.7.2、1507021、arm64-v8a、SO SHA-256 `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`。保存済み完全キャッシュと同じSOの実命令を使用した。Ghidraプロジェクト・参照assetsリポジトリは変更していない。ユーザー報告のクアラルン池は現在のDBで `NA033-2`、イングリッスは敵ID412。実戦の編成/操作列は未取得で、当該プレイの完全再現とは区別する。

## 確定した差分

|番号|重要度|変更前の実装差|影響・修正箇所|
|---|---|---|---|
|A1|高|呪いの時計0x2dc8/0x2e00が両方ともskill_zombie_strong.maanimを参照|呪われた生存キャラに、ゾンビキラーの絵が追従して表示される。export_battle_inputs.pyとbattle-inputs.jsonを修正|
|A2|高|006d951c..006d95dcのバリア/盾の表示時計を所有logicalが呼んでいない|非破壊の被弾後、表示フラグがON・表示Fが0のまま残る。actor_protection_clockを追加し、砲/二次攻撃後・保護確定前へ接続|
|A3|中|Rustの本体clip選択が行動14等でcontinueし、所有する全二次演出まで省略|本体を描かない蘇生待ちでも、原本は後続の波動/烈波/反射待ち/爆波描画へ進む。本体の選択をOptionにし、所有演出の走査を継続|
|A4|高|行動21に通常死亡の本体と通常魂を描く|死亡時烈波は専用battle_demonsoul_01/00。C++のkind10で専用モデル/時計を返し、通常死亡4の本体・魂と分離|
|A5|中|死亡4/21にもkind7の状態表示を出す|原本006ddfb8の死亡列は状態異常描画列を通らず、魂の後に所有二次演出へ進む。フラグを勝手に消さず、描画要求だけを除外|
|A6|低|クリティカル終了時はactivityだけを消し、座標と時計が残る|原本005bb4dcはX/Y/Fも0にする。固定プール終了処理を修正。非表示枠の残値なので、これ自体をゾンビキラー誤表示の原因とはしない|

### A1: 呪いとゾンビキラーを混同した入口

009f560cは0x2dc8へ `skill_curse.maanim`、0x2e00へ `skill_curse_e.maanim` を読む。009a61a4は同じ2枠を陣営別に選ぶ。旧抽出器は直前のヒープ文字列を採用していたが、この2箇所ではlocal_f0へ短い文字列を直接構築し直していた。local_1e0からのコピー00469f7cと直接構築を区別し、明示された全byteを読めない場合は停止するよう修正した。

`battle_effect_state.py`は009fa2bc..009fa3b8のADRP/LDR/STRを実行し、0044ba98へ実際に渡る文字列を捕捉する。ロード/モデル準備だけを制御し、名前をテスト側の戻り値として注入していない。更新後の39時計を再生成した結果、変更はこの2枠だけ。各長さも0044beb4/0044bf2cへ再照合し、誤登録の[-1,25]から正しい[-1,32]へ修正した。

死亡演出はkind6/phase0x2248、キャラへ追従する呪いはkind7/phase0x2dc8または0x2e00。誤登録時は異なる内部要求が同じ絵に見える。イングリッスが攻撃中も付けているという症状の有力な原因だが、当該操作列を採取していないため個別の発生を断定しない。

### A2: 耐久と被弾表示は別状態

バリア耐久はword130、破壊印は131。被弾表示のON/OFFは133、表示時計は134。悪魔シールドは最大184/現在190/破壊印191、表示種別192/時計193。原本は表示種別1/2/3に応じて0x2478/0x24b0/0x24e8のencoded長を使う。

原本の順番は、砲005d6740→表示時計→メタルキラー予約処理→protect→被弾表示/RNG→health→react。通常のactor_clockより後なので、そちらへ混ぜて早く更新してはいけない。表示時計は空き枠も含む全枠を走査する。encoded=-1をplainへ置換する分岐も、この箇所には存在しない。

修正前、被弾済みの生存個体を同一シードで1/2/30論理F進めると、次の最初の差が出た。耐久やHPを減らす補正はしていない。

|更新|原本 バリア表示/時計|旧C++ バリア表示/時計|原本 盾表示/時計|旧C++ 盾表示/時計|
|---|---|---|---|---|
|初期|1/0|1/0|1/0|1/0|
|1F|1/1|1/0|1/1|1/0|
|2F|1/2|1/0|1/2|1/0|
|30F|0/26|1/0|0/14|1/0|

修正後の所有logicalと実命令の288条件は一致し、シード0x12345678も変わらない。新たな被弾は後続protectで表示時計を再び0へ戻す。通常破壊/ブレイカーは元の解除と破壊プール要求を通す。雷砲に無条件破壊や特定敵の例外を加えていない。

### A3〜A5: 本体・状態表示・所有演出を独立させる

006ddfb8は本体を描かない行動14にも後続の005d3910/005d3f6c/005d4824/005d57d0を呼ぶ。旧Rustはclipがないだけで個体全体をcontinueしていた。修正後は本体だけを省略する。

一方、通常死亡4と死亡時烈波21は原本の死亡列へ入り、状態異常の4枠/無効表示/バリア/盾の持続表示を描かない。二次演出は引き続き呼ぶ。状態の消去を描画へ追加する変更ではない。

行動21は0x27f8+side*0x38、個体のword2を使い、X=word3/10、Y=word4/10+layer*4−97へ専用魂を描く。006de8e4..006de9d0の実命令へ両陣営の値を渡し、モデルoffset・F・基点がC++要求と一致することを確認した。Rustは同じ要求のkind10を状態表示より前に描く。正常な通常死亡4の本体/魂は維持する。最終GPU画素と全レイヤー順の連続比較は未実施。

## その他の生成・更新・消滅の監査

|対象|原本と現在の経路・判定|今回の結論と検証の限界|
|---|---|---|
|バリア/盾の破壊|006d97dc..006d9da0→actor_protect→各30枠|通常破壊とブレイカーの種別/被弾差戻しは864条件で一致。持続時計はA2で修正|
|ゾンビキラー|命中006e4aec等→00a9dce8の印→reactのHP0/KB分岐→30枠|通常命中は攻撃側の特性と対象のゾンビ条件を通す。敵初期化は印を0へ戻す。reactの804条件/RNGが一致。新たな印の誤継承・死亡プール漏れは確認していない|
|ゾンビキラープール|005ccf40でplain25F、005ccfb8で保存した座標へ描画|状態表示と独立し、死亡地点に残るため他のキャラと重なること自体はあり得る。固定プールの寿命と解放は新規比較で一致。実戦の全再利用列は未取得|
|クリティカル|命中印→200枠→005ccda8|空き確保後に座標RNG。満員時に先頭の座標へ書く原本の分岐は独自に修正しない。終了時の消去だけA6で修正|
|渾身/毒撃/メタルキラー/再生産遅延|印166/173/219等→可変リスト→005cd3e0/614/848/da6c|群の順序、逆順更新、encoded長による消去を追跡。新規40条件でリストの時計/残数/順序が実命令と一致。全生成元と音声デバイスの連続照合ではない|
|停止/鈍足/弱体/強化/生き残り/呪い/回避|actor_effects/clock→表示枠のkind7|前Fの解除→付与→描画の所有順を追跡。呪いの素材A1と死亡時の描画A5を修正。全組合せの実戦照合ではない|
|波動/小波動|emit_wave→waves_step→kind0/1|005d3910の6区間と所有者指定を照合資料/実装で追跡。味方/敵の4素材を0044beb4/0044bf2cへ直接渡し、いずれもencoded13/plain12。陣営間で同じ長さを使う点に差はない。既存ARM試験は更新・履歴・制御した命中戻り値。所有者行動14のRust欠落はA3で修正|
|烈波/小烈波/反射待ち/爆波|emit_area→areas_step→kind2/3/9/4|開始/持続/末尾、反射待ち、負Fの爆波非表示、所有者への紐付けを追跡。既存ARM試験の一部は命中本体をcallbackで制御し、全相互作用は保証しない|
|通常死亡/死亡時烈波|health→react→KB/retire/deathSurge→描画|HP0、KB終了、通常魂と専用魂を分離。A4/A5を修正。死亡/所有者解放/再利用を含む全mainの完全比較は未実施|

RustのServiceはセッションを排他に保持し、advance→stats/debug→drawの同じ状態を使う。描画側のcore.visualsとrender.cppの姿勢/頂点変換は戦闘RNGを取得しない。今回render.cppに症状を隠す座標補正は入れていない。

## 既存テストが保証していなかった点

- actor_protection.pyは保護区間の状態・SE・表示要求を比較するが、直前の表示時計を実行しない。これが通っていてもA2は検出できなかった。
- actor_reaction.pyは死亡表示の空きを入力で指定する。死亡プールの実寿命・次Fの空きへつながることは別の検証が必要。
- actor_cannon.pyの旧「barrier」はword117を設定しており、実際の耐久word130を試していなかった。word130へ修正し、表示中バリア・盾と、雷砲の5..15Fの境界条件を追加した。
- actor_motion_lengths.pyは渡されたファイルの長さを保証する。どのoffsetがそのファイルを読むかは保証せず、A1の誤登録も長さ計算の比較には通っていた。
- battle_session.pyのまとめ更新/1F更新一致はKBCS同士の比較。原本の省略分岐や、同じ誤った素材選択を検出する保証にはならない。

## 再実行・証拠

`research/verify/battle_effect_state.py`と`tests/effect-state-probe.cpp`を追加した。後者はactor.cppを含む解析専用DLLで、配布アプリには入らない。全mainを短絡して「完全一致」とする用途ではない。

解析DLLはLLVM-MinGWのclang++をPATHへ置き、リポジトリ直下で次のように作る。actor.cppはprobeが一度だけ取り込むため、通常のソース一覧から除く。

```powershell
$sourceFiles = Get-ChildItem -LiteralPath native/kbcs-core/src -Filter '*.cpp' | Where-Object Name -ne actor.cpp | ForEach-Object FullName
clang++ -shared -std=c++20 -O1 -fwrapv -ffp-contract=off -I native/kbcs-core/include native/kbcs-core/tests/effect-state-probe.cpp @sourceFiles -o research/.local/effects-audit-complete.dll
```

```
python research/verify/battle_effect_state.py --python-libs research/.local/python-libs --library research/.local/effects-audit-complete.dll --publish
python research/verify/actor_protection.py --python-libs research/.local/python-libs --library research/.local/effects-audit-complete.dll
python research/verify/actor_reaction.py --python-libs research/.local/python-libs --library research/.local/effects-audit-complete.dll
python research/verify/actor_cannon.py --python-libs research/.local/python-libs --library research/.local/effects-audit-complete.dll
```

修正前は`effect-state-effects-audit-before.json`、修正後は`effect-state-effects-audit-complete.json`をresearch/.localへ保存する。論理F、種類/プール枠、side/slot/raw/action/HP、関連フラグ、シードと最初の差が残る。小さい実命令由来の表示時計48件と素材名2件をeffect-state-vectors.jsonへ保存し、通常のRust/CI試験でも検査する。

修正後の再実行結果は、所有時計288条件・固定プール20条件・可変プール40条件・描画要求8条件が成功。死亡時烈波は両陣営2条件で原本の描画呼出まで比較した。保護864条件、react804条件、砲の命中288/行動676/発射128/接触24/雷砲境界32条件も成功。全workspaceのRust試験42件とcompile-fail文書試験1件、workspace/all-targetsのclippy（-D warnings）が成功した。既存C++警告11件は変更していない。条件数の合計を全戦闘の網羅率として扱わない。

Windows releaseビルドも成功。確認用バイナリと必要DLLを`.local/dist/effects-audit-review/`へ置き、版は0.1.37のまま、SHAと検証ログ一覧を`research/.local/effect-audit-verification.json`へ保存した。解析probeは同梱しない。稼働アプリの画面確認は行っていない。

## 残る不確実性と次の検証

クアラルン池の同一編成・入力列による全Fの原本再生、GPU画素/クリップ/全レイヤー順、全妨害の重複、死亡/蘇生と二次攻撃/終了画面の全組合せは未検証。ここを「一致確認済み」とは扱わない。

既存debug要求ではwords/visuals/actors/seedを取得でき、kind7の呪いとkind6の死亡演出を区別できる。ただし固定プールは原本同様に座標を保存し、現在のスロットを所有しないため、実戦の生成元raw/serialや生成理由の全履歴は保存していない。現在その場所にいるキャラを発生元として逆算すると誤る。

追加の実戦トレースは、戦闘単位・有効時のみの上限つきリングへ、生成/解放/再利用・phase・pool index・論理F・対象side/slot/raw/生成通番word240・行動/HP/印・理由を生成時点でコピーする設計が適切。描画要求のたびに生成履歴を作ったり、ログのために乱数を取得してはいけない。今回は本番の常時計測は追加せず、原本とC++の最初の不一致を上記検証器で特定できるようにした。

優先する次の連続試験は、雷砲→非破壊バリア→無被弾26F、同Fの再被弾/破壊、盾の再生種別3、満員30枠での死亡→解放直後の次死亡、ゾンビの死亡/待機14/蘇生15〜16と所有烈波の重なり。単体の戻り値だけでなく、生成原因・印・空き・RNG・描画要求を各フェーズの同じ位置で比較する。
