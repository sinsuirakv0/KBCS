# 共用描画コア（0.1.21）

`render.cpp` は原本を正規化したPODから姿勢・整数頂点・カメラ・背景・城の描画命令を作る。`scene_effects.cpp` は背景演出の独立した時計を所有する。GPU、SQLite、ファイル、GUI、戦闘判定には依存しない。

## 呼出関係

Rust `render::Model::parse` がimgcut/mamodel/maanimを読み、`kbcs_core_pose` が補間、親子変換、スケール・不透明度、アンカー、反転、Z順を評価する。`kbcs_core_scene_layout/paint` が背景と城を配置し、`scene_transform/sprite/instance` が世界座標を画面頂点へ変換する。`weather_draw` は雨・雪・星等の形状を作る。ホストはテクスチャIDを対応付け、UIは頂点・UV・ブレンド命令をGPUへ送る。

`effect_create` は正規化パラメータをコピーし、opaque handleを返す。`effect_frame` は指定フレームまで進め、巻戻し時は同じシードで再初期化する。RustのRuntime::Dropが`effect_destroy`を必ず呼ぶ。Sendのみ許可し、ServiceのMutexで直列化する。戦闘用RNGを共有していない。背景試写のシードは0x12345678、Xorshift32の13/17/15であり、原本の全乱数消費との一致は未確認。

## 原本と検証の境界

背景・城・演出の根拠は参照リポジトリstage-db/research/native-v1571の003a9bd0、003987f8、00398af4、003a8bfc、00217ae4、00218618、00861104、00840f70、004da7a8と、同docs/backgrounds.md。版は15.7.1 ARM32、SHA 7226cbdf9f9ea9a521b4e4c3a78a72141a31410aa9293a03bb45717d1682ac79。姿勢の既存調査には15.5.0 ARM32（SHA e28ae3aefea402f28cf4c95e5fd947e2fd09984b3d376d4c2623dce1256ff0c8）の007e375c/007e1b6c/007e24e8も含む。JP15.7.2 ARM64の戦闘カーネル証跡と混同しない。

現在のJP15.7.2素材を旧整数評価器と照合したpose-vectors.jsonは4素材×6フレーム×ループ2×反転2の96条件。頂点・分割・ブレンドを完全比較する。scene-effect-vectors.jsonは4背景×6時点（巻戻し含む）の個数と代表粒子を比較する。これは既存解釈の移植回帰試験であり、新規の全ARM実行照合・GPU画像一致の証明ではない。

浮動小数の積和融合を無効にし、float32化の位置を保持する。乱数幅の切捨て後の+1はdoubleで行う。floatのまま22530000+1を計算すると丸めで抽選幅が変わるため、演算型も契約の一部となる。

モデルをアニメーションとして参照する原本は静止姿勢として扱い、issuesへ件数を返す。味方・敵・その他モーション画面も同じC++姿勢APIへ接続した。JSの旧評価器はパーツ詳細の解析表示と回帰資料にだけ残し、描画頂点には使わない。連続演出の段取りとパーツ選択UIは引き続きホストの責務。完全な戦闘描画・当たり判定・全版の同一性は未実装。


0.1.30の戦闘画面はJP15.7.2 ARM64の005c8a6c/005c8548を追加参照。SceneInputのviewport_width/battle_rowsとSceneLayoutのviewport_width/y_origin/y_offsetを拡張（ABI3）。幅0/段数0は旧DB試写の960幅を維持。戦闘2段はアンカー505・基礎補正-15からスロットとの重なりを減算し、ズーム1で-51。下地は画像下端から680まで描き、論理画面640でクリップする。城も同じ座標変換を共用し、HUDの段数変更だけで背景を単純移動しない。局所ARMカメラ照合はbattle-controls-vectors.json。


0.1.31で戦闘画面のframeを演出Runtimeへ連続接続。描画フレームとカメラ要求を分け、停止中の位置変更で演出時計を進めない。005cb0e0の通常上限10000に合わせ、battle_rowsありはzoom<=1、DBの拡大試写は<=2を維持。大きい城による個別上限と慣性を含むAndroid入力の完全移植ではない。既存の背景Runtime/姿勢計算を使い、JSへ演出の抽選や位置更新式を重複実装しない。
