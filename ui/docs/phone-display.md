# AndroidへのUSB出力

ホームの「スマホに接続」から、USBデバッグを許可したAndroidを1台接続する。PCにはAndroid SDK Platform-Toolsのadbが必要。SDKの環境変数、標準SDKフォルダ、PATHの順に探す。AndroidではChromeで表示と操作を行う。［[Platform-Tools](https://developer.android.com/tools/releases/platform-tools)・[USB転送](https://developer.android.com/develop/ui/views/layout/webapps/access-local-server)］

## 出撃と操作

PCでステージを選ぶとスマホは待機画面から出撃準備へ進む。編成・冠・アイテムの選択と出撃はどちらの端末からでも行える。PCから出撃した場合、その時点の出撃準備の内容をスマホに渡す。スマホの暗転中もPCは出撃準備を表示する。戦闘開始後はPCの中央だけを黒にし、上部の操作盤、敵・味方の一覧、下部の詳細を同じ戦闘セッションに接続する。PCの操作は`Exchange::commands`からスマホの既存操作へ届く。PCは個体一覧と選んだ個体のプレビューだけを描き、中央の戦闘用Canvasや音声を初期化しない。

戦闘前に`Session::prepare`でステージの入力、画像索引、モデル、背景演出を確定する。BGMは対象ステージの切替曲を含め、SEは音声設定とステージ原本の開始・勝敗設定を使い、暗転中に素材を準備する。版付き素材URLは同じUSB接続内で再利用する。

配布版は出撃の応答に`Prepared`を含む。ChromeのWorkerが`Prepared::start`で所有する戦闘と演出の状態を作り、`Session::frame`で戦闘計算・HUD・描画命令を生成する。描画フレームはWorkerから端末内のCanvasへ`KBP1`のArrayBufferとして移す。通知の配置計算も同じWorkerを使う。PCは暗転中に準備した報酬保存の`Receipt`を所有し、勝敗確定とコンテニュー操作の結果だけを別要求で返す。同じコンテニュー要求を再送しても、同じ戦闘で同じ回数を二度支払わない。

スマホはステージの要約、敵・味方の一覧、選択した個体の表示、計測値を`/api/phone/sample`で通常200 ms間隔に送る。送信中は追加のスナップショットを並べず、応答後にその時点の状態を送る。PCからの入力と表示項目は従来の操作待機経由。下部の「スマホ」タブは端末内フレーム、C++更新、Workerの待機、WebGL・HUDの提出、FPSを表示する。CPUとRAMは「動作・PC」に表示する。

WebAssemblyを同梱していない開発ビルドではPCが戦闘フレームを計算する。`KBP1`は画像パスの繰り返しと未使用頂点を省き、倍精度の座標を保持する。USBサーバーは16 KiBを超えた出撃データ・戦闘フレームで、Chromeが対応していればgzipを使う。PC計算時のKBP1はHTTPヘッダーと本文をまとめて書き込み、ヘッダー待ち・本文受信・gzipの計測を診断JSONに載せる。

スマホの論理画面高は640。`phoneCanvasSize`は画面内に収まるCSS寸法とDPRからCanvasの物理画素数を求める。回帰テストではDPR 3で800×360 CSS pxが2400×1080、1920×640 CSS pxが5760×1920になることを確認する。

## 全画面と端末の余白

「横向き全画面」をスマホで押すと、Chromeの全画面表示と横向き固定を要求する。横向きにできなかったときの案内は5秒で消える。`phone-display.js`は全画面の開始時にChromeの案内の上へ横スワイプの説明を出す。Chrome側の案内を閉じた通知はページに届かないため、KBCSの説明は4秒後か全画面解除時に消す。全画面中の操作は説明の下にも届く。［[Chromiumの全画面案内](https://chromium.googlesource.com/chromium/src/tools/+/202afc1279188dbb134b0329e19ab0f4dceb5a82)］

戦闘中は左右の余白も含めて背景を描画する。`phoneHudInsets`はChromeの左右の安全幅から描画領域の外側にある余白を差し引き、論理画面の座標へ換算する。15.7.2の`005d2408`、`005d1f2c`、`00449c34`、`00449c84`で確認した左右別の基準を財布と砲の表示・入力へ使う。ステージ名には16.0.3の`0046ce6c`と`0070b4b4`に従って左の安全幅を加える。

## 接続と解放

`Phone::navigate`がPCの表示先を渡し、スマホの待機画面は同一オリジンのiframeに出撃準備を載せる。サーバーはPCのループバックだけにバインドし、adb reverseでスマホのローカルポートへ転送する。使い切りURLの後はHttpOnly Cookieで認証する。USB側には出撃準備と戦闘に必要なAPIだけを公開する。PCで他のページに移動するとスマホは待機画面へ戻る。「スマホ接続を終了」でUSB接続を終了できる。

## ブラウザ向け戦闘コアの検証

Rust 1.98.1とEmscripten 5.0.3で`scripts/build-phone-runtime.py --output .local/phone-runtime`を実行し、Windows・macOSの配布向けに共通の成果物を生成する。開発機では`KBCS_PHONE_WASM_DIR`に成果物の絶対パスを設定してアプリをビルドする。C++の例外方式をRust標準ライブラリと揃え、実行時のスタックに8 MiBを確保する。

アプリの試験ビルドではTLS依存とHTTPワーカープールを外し、Nodeの`NODEFS`で公式DBと素材を読み込んだ。同一の出撃リプレイ91更新（798論理Fまで）で、Windows版とWebAssembly版の戦闘状態・HUDの数値・画面配置・描画命令数が一致した。Chromeの端末エミュレーションではUSB接続用サーバーから出撃し、960×432 CSS px、DPR 2.5で2400×1080のCanvasと左安全幅の適用を確認した。

接続経路の検証ではN000を同じ出撃データ・入力91更新（798論理F）で再生し、ヘッドレスChromiumのWorkerとWindows版の戦闘状態、HUD、描画命令数を照合した。浮動小数の差は最大約5.7×10⁻¹⁴。監視応答を保留した状態で戦闘更新が継続すること、端末の描画データをWebGLへ提出できること、「スマホ」タブ、通知配置のローカル呼び出しも確認した。Pixel 8での実戦FPSは未計測。
