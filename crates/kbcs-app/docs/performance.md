# 戦闘の操作・計測と負荷分離（0.1.32〜0.1.34）

評価資料は2026-10-25、対象56914943。静的レビューの指摘と実測を区別する。実装対象は常時操作バー、ステージ描画の待機/コピー、要求スレッド/共有ロック、BGM待機とキャッシュの追い出し。戦闘の整数化・乱数消費・計算順を高速化名目で変更しない。

## 経路

workspaceの戦闘タブにbattle-controlsを移動し、戦闘中は常に表示。停止/再開、1F/10F、ネイティブオプション、段数、枠切替、カメラ初期化、準備へ戻る、診断JSON。ホストの停止は本家オプションのpausedと別。control10は指定した更新数を1更新1論理Fで進め、速度アイテムの値を変更しない。停止中のカメラ再描画は0F。native pausedを閉じる更新と手動ステップは分離する。30F固定の未処理時間を保持し、FPS維持を理由に時計/乱数/更新を飛ばさない。

battle-monitorは実際にHUDを描いた回数のFPS、論理F/実秒の進行比、更新API・背景API・背景計算・WebGL提出の時間、遅れF、画像キャッシュ/読込数を1秒間隔で表示。GPU処理時間や実キャラ生成数を仮表示しない。/api/runtimeはPCのCPUと物理RAM、RustホストのWorkingSet、要求キュー/キャッシュ統計を返す。WebView/GPUの別プロセスメモリをRustホストの値へ混ぜない。診断JSONはこれらと版/ABIだけを保存し、編成・ユーザーファイルのパスを入れない。

CPUはGetSystemTimesの差分（kernelにidleを含む）、物理RAMはGlobalMemoryStatusEx、ホストはK32GetProcessMemoryInfo。初回や取得不能はnull。750ms以内の再要求は計測値を共用する。参考: https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getsystemtimes 。これは監視機能であり、CPU使用率だけから最適速度/FPSを保証する機能ではない。

## バックエンド

workers::WorkersはGUIプロトコル/HTTP共通の固定ワーカー。軽いUI2、計算2〜6（利用可能論理CPU数で上限）、I/O2に分離、各待ちキュー64件。満杯は即503で返し、GUIスレッドで重処理しない。実行中/待機/拒否を計測する。要求パニックでワーカーを失わないが、処理途中の全状態復旧まで保証したものではない。更新の専用スレッドはbusyで1件に限定する従来方式。

cache::Cacheは件数/バイト上限つきLRU。カタログは128件/128MiB、シーン16件、モデル64件。シーン/モデルのMapは検索・空スロット作成だけをロック。構築はスロット単位で一度だけ行い、別のキーは並行処理。同じシーンは状態更新/出力まで直列化し、同じ乱数状態を並列に進めない。battle sessionをキーへ加え、別戦闘で同じ背景の時計を共有しない。シーン/モデルのネイティブ内部メモリ全量をバイト計測したわけではなく、この二つは件数制限。

Scene::Frameは型付きのlayout/commandsとテクスチャ/不足情報の借用を直接Serializeする。毎Fの巨大なserde_json::Value中間ツリーを廃止。CLIは同じFrameを必要に応じValueへ変換する。音源のロックは曲単位のWeak<Mutex>へ分離し、同曲の取得をまとめる。開始BGMだけを暗転中に待ち、後の曲は取消可能なバックグラウンド取得へ。途中切替の実発動は戦闘本体との接続時に読込完了/失敗を確認する。

## 描画

createStagePainterが戦闘専用のWebGL面を所有し、その上の透明2D面にHUDを描く。C++の命令順・頂点・UV・ブレンドは共用。WebGL→2D→最終2Dのコピーを外し、フレーム毎のcanvas.width/height再代入も避ける。ライブ面だけpreserveDrawingBuffer=false、DBの画像保存経路は従来値。戻るとGPUリソース/イベントを解放。context lostをpreventDefaultし、復旧時にシェーダー/テクスチャを作り直す。全モーション画面の復旧を今回対応した意味ではない。

## 検査と残る項目

最小試験は固定ワーカーと64件キュー、LRU容量/最終参照、3倍設定中の1F/10Fと既存の原本ベクトル。前後の同じ入力・フレームの描画命令をJSONとして厳密比較する（計測値だけ除外）。API時間は同じPC・DB・PR000/1422幅で測る。画面/GPU/FPSの実表示確認はユーザー担当。API待ち時間の改善だけで画面FPS改善を断定しない。

索引キャッシュ破損の自動隔離、更新中断ロックの起動時刻照合、エラー分類、全モーションfitの一括境界API、研究資料の再配置は今回の変更対象外。既存DB・ユーザー編成・解析資産は保全する。全戦闘の個体生成/移動/攻撃の実装状況は従来の再開メモどおり。

## 最終ビルドでの実測

同じ粒子群の各個体で不変なローカル姿勢は群ごとに一度だけ解決し、個体ごとのinstance変換・出力順は維持する。空の群では姿勢計算もしない。ライブ背景は暗転中にデコードした画像を共用し、同画像の再デコードを避ける。GPUハンドルの強参照追跡はライブ背景だけに限定し、既存モーション描画のWeakMapによる寿命管理を変えない。

最終0.1.32と専用の旧0.1.31プレビューで、PR000/N000各0〜30F、幅1422/2段の62出力が計測値を除き完全一致。独立sessionの並行16要求も一致。3倍設定のまま1F進行をHTTPで確認。公開ソース7ファイルの配信バイトも最終ビルドと一致した。

このPCでのAPI往復中央値はPR000 60.53→45.74ms、N000 12.25→12.75ms。PR000のサーバー計算中央値7.20ms、N000 4.43ms。負荷のあるPCの単回標本であり、全ステージの改善や30FPSを保証しない。描画/GPU/FPSの目視確認は実施していない。検査の原記録は.local/checks-0.1.32.json。

workspace全試験の後、追加したワーカー試験を含むapp3試験と、最終Rust変更後のall-targets clippyを通過。関連試験計27件とcompile_fail1件、最終JS5モジュールの構文、releaseビルド、差分空白検査を通過。

## 0.1.33: 実アプリのFPS確認と要求の統合

ユーザー依頼により2026-10-25、実行中の0.1.32ネイティブGUI（http://kbcs.localhost、PR000、2段）を確認。観測例は19.0/19.9/22.9/27.1FPS、論理進行0.97〜1.04倍。更新API7.1〜8.8ms、背景API22.9〜33.9ms、背景計算7.7〜10.9ms、描画提出0.5〜1.2ms。サンプルは瞬間値でGPU実行時間ではない。キュー待機0、画像未読込0、RAM約7.0/7.9GB。CPU/メモリだけを原因とせず、直列の2要求と、その完了後に次のrequestAnimationFrameを待つ構成を調査した。

/api/battle-frameは既存battle_screen::frameを呼び、その出力の論理F・段数・画面幅で同じScene::drawを呼ぶ。HUD更新と背景が1往復で返る。従来の/api/battle-screenと/api/stage-sceneは残し、DB閲覧も共通scene_replyを使う。背景の先行生成や補間は行わず、状態/乱数/頂点の式を変えない。coreMsはC++更新計算だけ、戦闘API表示は背景も含む往復時間へ変更する。

scene_replyのLRUスロットは読取専用DatabaseとSceneを対で所有する。毎フレームのDB再接続を省き、同じロックで直列使用する。current.jsonは毎要求確認し、snapshotのパス変更は別キーとして開く。LRU最大16スロットで古い接続も解放される。

ユーザーが操作を担当する指定後は一切入力せず、起動中0.1.33/PR000の表示値を記録した。13点のFPSは22.0〜30.1、中央値28.0。戦闘API21.7〜60.3ms、背景計算4.9〜11.7ms、描画提出0.6〜1.7ms。進行比0.94〜1.04、CPU47〜59%、RAM約6.5〜6.6/7.9GB。30FPS安定には未達。これは瞬間表示の観測で、ユーザー操作で条件も変わり、厳密な版間比較ではない。原記録は.local/runtime-observations-20261025.json。最終ビルド後の追加API負荷試験は、操作中の計測を乱さないため実施していない。

統合APIの初回ビルドでは78件のstate/layout/sceneが旧2要求の出力と厳密一致し、scene省略2件も一致。続けて静止背景の再利用時にも段数変更を必ず反映するcached指定を追加し、clippyと最終releaseを通過。ユーザー操作中のGUIは初回0.1.33であり、最終cached指定の通信試験は未実施。C++計算/ABI自体は0.1.32から変更していない。

## 0.1.34: 戦闘フレームの転送と一時確保

createBattleFrameClient → /api/battle-frame(packed:true) → 既存のbattle_screen::frame / Scene::draw → battle_wire::encode → decodeBattleFrame → 共用NativeWebGLRenderer。packed未指定のJSON入口は維持する。変えるのは受渡形式とバッファ寿命で、戦闘更新・背景時計・乱数消費・描画順・頂点計算には手を入れない。

KBF1はC ABIの構造体メモリをコピーせず、固定LE形式で明示的に出力する。32バイトのヘッダーはmagic4、JSON長u32、命令数u32、レコード長u32(192)、サーバー時間f64、変換時間f64。続いてUTF-8の小さなメタデータJSON（state/layout/scene、commandsは空）、8バイト境界までの0詰め、192バイト×命令数。各命令はtexture/layer/count/blendのi32×4、opacityのf64、pointsのf64×16、cutのi32×4、colorsのi32×6。新しい形式の版でありC ABI3とは独立。対象のWindows x64/ARM64とJS TypedArrayはLE。精度を下げず、float32化は従来どおりGPU転送直前だけ。

decodeBattleFrameはヘッダー・長さ・レコード数・所属を検査し、座標/切抜/色をArrayBufferへのTypedArrayビューとして借用する。座標配列のJSON化/復元/再コピーを省き、古いフレーム参照が消えるとバッファも回収可能。rasterはTypedArrayのsubarrayを使い、色の0〜1変換を整数TypedArray.mapで切り捨てない。GPU命令は従来と共用する。

Runtime::frameの粒子出力はRuntimeが16384件のバッファを一度だけ確保し、次のframe呼出までスライスを貸す。C++は呼出後にポインタを保持しない。毎Fの大きなVec確保/0埋め/解放を省く。最大16シーンのLRUと同じ寿命で、破棄時はnative handleとバッファを解放する。既存の単調進行/巻戻し証跡で値を照合する。

APIバーのp95/最大は直近120要求のリングバッファから1秒ごとに集計する。tooltip/診断にはサーバー時間（変換を含む）、変換、復元、受渡・待機の差分、バイト数を追加。受渡・待機にはワーカー待ち・WebView/HTTP・ブラウザー側の時間も含み、ネットワークだけの測定ではない。GPU実行時間や将来の全個体処理性能を意味しない。描画の補間、先行フレーム、論理Fの間引きは追加していない。

render::paintにも毎回Command×16384（約3MiB）の初期化が残っていたため、Sceneのpaint_bufferを呼出側所有のスライスとして貸す。C++が返したwritten件だけをフレームVecへコピーし、上限用の巨大な容量を毎回返却/解放しない。C++の16384上限は維持し、失敗時はスライスを返さない。Runtimeの粒子バッファと合わせた最大保管量はシーンLRU16件で有界。ここで原本の式をRustへ重複実装しない。

転送区間の追跡では、非圧縮HTTPの1199要求中6件で本文待ち301〜330msを観測した（ヘッダー6〜18ms、サーバー5〜12ms）。同じ実行のNodeイベントループ最大遅延44ms、20ms超のGC報告0。サーバー計算とは区別できるが、TCPの個別機構やネイティブWebViewでの原因をこれだけで断定しない。.local/profile-wire-tail-uncompressed.jsonが原記録。

compressed:trueを明示したクライアントへは、8KiBより大きく圧縮で小さくなる本文をgzip fastで可逆圧縮したKBG1も返せる。先頭32バイトの意味はKBF1と同じで、メタデータ以降だけを圧縮する。サーバー/変換時間には圧縮時間を含める。unpackBattleFrameは展開後のバッファをそのままparseBattleFrameへ貸し、ヘッダーと合体する再コピーをしない。KBF1とJSONの既存入口は残す。

ブラウザーの標準DecompressionStreamを機能検出してからcompressedを指定する。未対応ならKBF1を要求する。Content-Encodingの処理を独自プロトコルへ仮定せず、WebView/HTTPとも同じ明示形式を使う。参照: [MDN DecompressionStream](https://developer.mozilla.org/en-US/docs/Web/API/DecompressionStream)。

### 最終検査（0.1.34-release）

旧0.1.33/新0.1.34を同じPC・DB・PR000・幅1422・2段で交互に1000要求。本文受信完了までの中央値17.08→10.47ms、p95 21.20→14.14ms、p99 23.32→17.93ms、最大326.56→26.04ms。PR000の別の99標本では194758→23388bytes（約88%減）。小さいN000は圧縮せず、p95 9.46→5.07ms。原記録.local/checks-0.1.34.json。旧版は比較用4847、新版は4850。これはHTTP API単体の同一PC計測であり、ネイティブWebViewの実FPSや全負荷の保証ではない。

さらに新版1199要求のヘッダー/本文を分けて追跡。受信p95 14.68ms、p99 19.46ms、最大28.29ms。展開・復元までを含むクライアント時間はp95 23.27ms、p99 30.01ms、最大44.72ms。50ms超の要求0件、本文300ms級の停止も今回の再計測では0件。永続的な解消やGPU表示一致を証明した意味ではない。.local/profile-wire-tail.jsonに保存。圧縮前の観測も*-uncompressed.jsonとして保持する。

PR000/N000のstate/layout/scene全値216ケースを旧経路へ厳密比較し一致（計測値だけ除外）。速度3倍、1F/10F、停止、段数/枠変更を含む。圧縮・非圧縮・省略したscene、長さ/版不正、壊れたgzip、同じArrayBufferの借用、120件リングも検査。workspace28件+compile_fail1、変更後のbridge/app・最終app試験、all-targets clippy、JS構文、最終ビルドの配信8ファイル一致を通過。UI入力・画面切替・再読み込みは行っていない。
