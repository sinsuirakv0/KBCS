# 音源の取得・再生経路（JP15.7.2）

対象はARM64、SO SHA-256 `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`。research/.local/reference.jsonの完全版を検索CLIで読み、既存Ghidra/参照リポジトリを変更していない。以下は保存済み疑似コードの静的追跡であり、AndroidのJNI/音声デバイス/通信を実行した結果ではない。

## 設定から再生まで

|関数|役割・関係|
|---|---|
|00ac8f8c|初期データ読込から00457e1cの音声管理へSound_setting.tsvを渡し、00458038で設定|
|00458038|ヘッダーを読み飛ばし、bgm=1をbit0、それ以外をbit1、loop=1をbit2へ格納。priorityは別の配列|
|00458974|音源の事前準備。効果音はAPKのsnd%03d.cafを確認し、なければgetFilesDir側の%03d.cafへ。00565c20でサンプルを準備|
|00459170|共通再生入口。BGM/効果音のビットとミュート状態で分岐。BGMはsnd%03d.oggを確認、なければgetFilesDir/%03d.oggを組み、00549ac8へ。効果音は準備済みサンプルからプレイヤーを作る|
|00549ac8→0055aad0|ストリームを作る。0055aad0はAAssetManager_openを先に試し、失敗時にfopenへ進む|
|0055b540|ファイル存在確認。statに成功するか、0055aad0でAPKのassetを開けるか|
|0055b5fc|空の基準パスを返す（APK assets内の相対名を渡すため）|
|0055b95c|JNIでgetFilesDir→getAbsolutePath。アプリ内部ファイル領域を返す|

BGMはAPK内の `assets/sndNNN.ogg` と、追加取得済み内部ファイル `NNN.ogg` の二つの経路。SEは同様に `sndNNN.caf` / `NNN.caf`。画像のLocal/Server packの中に音源を仮定しない。00458974には内部sndNNN.oggを削除する準備もあり、読込経路をそのファイル名だけから誤認しない。00459170はID29の動的差替えも持つが、KBCSの全場面の選曲ロジックを今回再現した意味ではない。

## 追加取得

00421b40は配信ファイル一覧と内部ファイルのサイズを確認する。.ogg/.cafの場合はAPK側にsnd付きのファイルがあるかも確認し、同梱済み音源の重複取得を避ける経路がある。004222e0は `https://nyanko-assets.ponosgames.com/iphone/battlecats/download/` と版/パック番号の名前からZIP取得URLを組む。高い版番号用の名前形式にも分岐する。00423798は一時download.zipのパスを組む。音源個別のストリーミングURLを毎回再生する構造ではない。対象の配信パック、要求ヘッダー、展開/移動の全処理は未検証であり、本家サーバーへ今回アクセスしていない。

## KBCSへの適用（0.1.31）

元のKBCS音源索引は別Webの188曲のMP3補完だった。ユーザー指定assetsの固定commit `8e9dca31e3845e3c7dcdc515e6c85d5480538fc0` では、同版のAPK内音源27件（BGM18 Ogg、SE9 CAF）がassets索引に追加されていた。scripts/sync-stage-music.pyはcurrent→manifest→assets index→Sound_settingのSHA/size/headerを検証し、bgm=1のOgg18件を優先採用する。0,34,174〜187,193,195。CAFはBGM索引へ混ぜない。

stage_media::audioは曲ごとのcommit/size/SHA/形式を検証し、AppData/KBCS/assets/music/<revision>/NNN.oggへ保存。APIは拡張子なしIDと実MIMEを返す。既存MP3は補完として保持し、以前のcommitディレクトリのキャッシュも再利用する。元音源がMP3であるという主張や、全SEをKBCSで再生可能にしたという意味ではない。今回の追加音源に公式DBの再構築は不要。


## SE接続（2026-10-27）

sync-stage-music.pyは同じ固定commitのCAF9本もSEとして索引へ追加する（BGM18＋SE9）。stage_media::audioはCAFの非圧縮little-endian PCM16を検証し、WAVへ包み直してブラウザへ返す。ID65/137/139も変換済みMP3より原本CAFを優先する。原本9本と返却WAVのPCMがbyte単位で一致した。変換後を別の音源として配布・GitHubへ書き込む処理ではない。

所有戦闘のSE通知はBattleSoundScope→battle_sounds→runtime.sounds→battle-audio.jsへ渡る。waveのSEは26、bossは45。00459170のAndroidバックエンドの優先度/メモリ制限・ID29差替え・全場面の選曲をWebAudioへ完全移植した意味ではない。音声の取得やdecodeが論理F/RNGを停止しない。

## 戦闘の操作・終了時のSE整理（2026-10-28）

同じ原本JP15.7.2/arm64-v8a/SHA6122e248…を使用。画面・音声デバイスの確認はユーザーが担当し、起動中のアプリを操作していない。

- `00459f04`は`005bc058`（game+83e34）が0以外なら再生しない。`00459efc`にはこの制限がない。`actor.cpp`の共通ラッパーで所有戦闘のmodeを参照し、単体APIでは入力にmodeがある場合だけ同じ判定をする。protect/蘇生/特性の通知をまとめて黙らせる判定をUIへ追加しない。
- `005ccda8/005cd3e0/005cd614/005cda6c`のcritical44/渾身90/毒撃110/遅延188もf04経路。effectClockの寿命は続けてSEだけを抑止する。`005d3af8`の烈波111/112と`005d4988`の爆波167〜169は同じ制限。`005d4158`の反射召喚159はefcなので保持する。通常死亡23/24など、原本のefc呼出は終了後も一律に削除しない。
- `00459bb4(-1)`はBGMのみ停止、-2はSEのみ、-3は両方。勝敗入口`005d996c/005e02b0`は-1を呼ぶため、終了時に既に鳴っている全SEを切る方式は採らない。既定8/9、道場57/189、eventDisplayDataの終了音選択は従来のC++経路を使う。
- `006da760`の被弾走査は通常個体=1、城0/敵の特殊城個体=2をフレーム全体で集計し、勝敗判定後`006db4f8..006db624`でmode=0の時だけ発音。2なら22、1なら原本のRNGを一回消費して20/21。無音設定でも論理RNGを省かず、勝敗が決まったFは命中音の抽選自体を行わない。`006db83c`の砲充填完了は28。

操作は`battle_screen.cpp`からhookの`KBCS_BATTLE_SCREEN_SOUND + id`で所有Battleへ渡す。既存イベント0..5、POD、ABI4を変更しない。

|操作|原本と接続|
|---|---|
|砲/財布/ポーズ/キャラ枠の押下|006dca34..006dcf80の領域へ入った時に10。長押し継続で繰り返さない|
|財布を離す|006dcc04/006dd17c。昇級成功19、最大/資金不足15|
|砲を離す|005d8f58。充填中/行動中15。発射は種別ごとの25/60/61/37/65/84/無音/124と共通19|
|アイテム|006dcd68。説明の押下は無音。速度/CPU/スニャイパーの切替解放で11、効果変更までの5表示更新は保持|
|オプション|008fef58/008ff0d8/008ff260/008ff388/008ffb80。callback0の押下10、3の解放11、4は待機後の動作|
|BGM/SE音量|008ff260/008ff388は解放時に音量を変えてから11。音量0なら11も無音、0→25%ならその音量で鳴る。振動は無効のまま|

`battle-audio.js`は同じIDにつき一つの再生を使い、00459170の再生し直しをWebAudioのstop/startへ正規化。Sound_settingのloopを使用し、独自の同時16音制限やフレーム内の通知削除は加えない。ダウンロードは並行、通知順に発音する。終了/ミュート/ホスト停止を跨いで未デコード通知が遅れて鳴るのを世代で防ぎ、新しい終了音を古い取得待ちで塞がない。既に再生中の音の音量はgainで変更する（0045a244）。通常命中・死亡・砲種別を含む51音の先読み索引が存在することを確認。取得失敗は従来どおり診断へ表示する。

検証: `research/verify/battle_audio.py`でf04の5mode、実オプションcallbackの80条件、命中音/RNGの45条件、計130条件を原本ARM64実行。描画/音声デバイス/解決済み音量getterだけ制御し、native乱数は実命令。C++入力→通知は`native/kbcs-core/tests/battle-audio.cpp`、遅延decode/同一SE/ミュート/破棄は`ui/tests/battle-audio.test.mjs`。1Fの所有戦闘試験にも、HP1保持Fの22と勝利Fで22が出ないことを追加した。全main/Android音声デバイスの連続一致、priorityでの資源解放、ID29の動的差替えまで検証した意味ではない。
