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
