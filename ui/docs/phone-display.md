# AndroidへのUSB出力

ホームの「スマホに接続」から、USBデバッグを許可したAndroidを1台接続する。PCにはAndroid SDK Platform-Toolsのadbが必要。SDKの環境変数、標準SDKフォルダ、PATHの順に探す。AndroidではChromeで表示と操作を行う。［[Platform-Tools](https://developer.android.com/tools/releases/platform-tools)・[USB転送](https://developer.android.com/develop/ui/views/layout/webapps/access-local-server)］

## 出撃と操作

PCでステージを選ぶとスマホは待機画面から出撃準備へ進む。編成・冠・アイテムの選択と出撃はどちらの端末からでも行える。PCから出撃した場合、その時点の出撃準備の内容をスマホに渡す。スマホの暗転中もPCは出撃準備を表示する。戦闘開始後はPCの中央だけを黒にし、上部の操作盤、敵・味方の一覧、下部の詳細を同じ戦闘セッションに接続する。PCの操作は`Exchange::commands`からスマホの既存操作へ届く。PCは個体一覧と選んだ個体のプレビューだけを描き、中央の戦闘用Canvasや音声を初期化しない。

戦闘前に`Session::new`が確定した画像索引を使い、背景・城・キャラ・エフェクト・UIをスマホへ転送する。BGMは対象ステージの切替曲を含め、SEは音声設定とステージ原本の開始・勝敗設定を使い、ダウンロードとSEのデコードが完了してから戦闘を開始する。版付き素材URLは同じUSB接続内で再利用する。戦闘中は入力・音声ID・数値・描画命令を転送し、端末に準備済みの画像・音声を使う。報酬通知の配置も数値で取得する。

`Session::new`は背景演出の定義と画像索引を確定してから出撃応答を返す。`Scene::draw_with_castle_state`は確定済みの背景・モデル・演出状態を使う。報酬保存の`Receipt::settle`は勝敗と抽選結果を受け取り、受領記録と通知を作る。

`KBP1`は既存の戦闘フレームから画像パスの繰り返しと未使用頂点を省く。描画頂点は倍精度のまま。 端末がgzipを受け付ける場合、USBサーバーは16 KiBを超える応答をHTTPで可逆圧縮する。圧縮で縮む応答に`Content-Encoding: gzip`を付ける。Chromeは受信中に展開し、旧来と同じKBP1を描画処理へ渡す。USB側の固定長レスポンスはContent-Lengthで送る。PCの一覧データは約75ms間隔で別経路に取り出し、スマホの描画フレームには付けない。スマホの論理画面高は640。`phoneCanvasSize`は画面内に収まる描画領域のCSS寸法と端末のDPRからCanvasの物理画素数を求める。出撃準備の回帰テストではDPR 3で800×360 CSS pxが2400×1080、1920×640 CSS pxが5760×1920になることを確認する。

USBの戦闘フレームでは `phone::respond` がHTTPヘッダーと本文をまとめて書き込む。`createBattleFrameClient` がChromeのヘッダー受信までと本文受信・HTTP展開を別々に計測し、`service_reply` が計測したgzip判定・圧縮の時間と合わせてPCの「転送」欄のツールチップと診断JSONに載せる。

## 全画面と端末の余白

「横向き全画面」をスマホで押すと、Chromeの全画面表示と横向き固定を要求する。横向きにできなかったときの案内は5秒で消える。`phone-display.js`は全画面の開始時にChromeの案内の上へ横スワイプの説明を出す。Chrome側の案内を閉じた通知はページに届かないため、KBCSの説明は4秒後か全画面解除時に消す。全画面中の操作は説明の下にも届く。［[Chromiumの全画面案内](https://chromium.googlesource.com/chromium/src/tools/+/202afc1279188dbb134b0329e19ab0f4dceb5a82)］

戦闘中は左右の余白も含めて背景を描画する。`phoneHudInsets`はChromeの左右の安全幅から描画領域の外側にある余白を差し引き、論理画面の座標へ換算する。15.7.2の`005d2408`、`005d1f2c`、`00449c34`、`00449c84`で確認した左右別の基準を財布と砲の表示・入力へ使う。ステージ名には16.0.3の`0046ce6c`と`0070b4b4`に従って左の安全幅を加える。

## 接続と解放

`Phone::navigate`がPCの表示先を渡し、スマホの待機画面は同一オリジンのiframeに出撃準備を載せる。サーバーはPCのループバックだけにバインドし、adb reverseでスマホのローカルポートへ転送する。使い切りURLの後はHttpOnly Cookieで認証する。USB側には出撃準備と戦闘に必要なAPIだけを公開する。PCで他のページに移動するとスマホは待機画面へ戻る。「スマホ接続を終了」でUSB接続を終了できる。

## ブラウザ向け戦闘コアの検証

Rust 1.98.1とEmscripten 5.0.3で`kbcs-bridge`を`wasm32-unknown-emscripten`向けにビルドし、Node 24で戦闘・描画を含む既存の50テストを実行した。実行時のスタックは検証用に8 MiBを確保した。C++側は`build.rs`でRust標準ライブラリと同じWebAssembly例外を使う。現行のChrome接続は引き続きPCから戦闘フレームを受け取る。出撃時の入力を渡す処理と、戦闘終了・コンテニュー時のPC保存を接続してから、ブラウザを戦闘の実行主体に切り替える。

アプリの試験ビルドではTLS依存とHTTPワーカープールを外し、Nodeの`NODEFS`で公式DBと素材を読み込んだ。同一の出撃リプレイ91更新（798論理Fまで）で、Windows版とWebAssembly版の戦闘状態・HUDの数値・画面配置・描画命令数が一致した。Chromeの端末エミュレーションではUSB接続用サーバーから出撃し、960×432 CSS px、DPR 2.5で2400×1080のCanvasと左安全幅の適用を確認した。
