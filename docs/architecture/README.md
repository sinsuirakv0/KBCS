# アーキテクチャ

## 現在の責務

使用する3クレートだけを作成した。RustがGUIホスト・SQLite・原本検証・変換・更新を担当し、C++20は将来の戦闘・姿勢計算専用とする。data/domain/importはkbcs-data内にまとめ、必要になったときに抽出する。

GUIはユーザーの指示により、Webと同じHTML/CSS・検索処理をそのまま再利用する。eguiによる近似UIは廃止した。tao + wryでWindowsのWebView2 Runtimeを使い、ブラウザ本体やElectronを同梱しない。CLIとデータ層はWebViewへ依存しない。Windows以外のGUIは今回未対応。

`main` → `desktop::run` → WebView2 → 埋込みui、または `main preview` → ループバックHTTP → 同じui。両方とも `Service::handle` → `Database` / `import` を呼ぶ。GUI本体ではHTTPポートを開かず、kbcs専用プロトコルから応答する。

データ経路は `Source::dataset` → `import::build` → `store::insert_form` → SQLite。`view::catalog` はキャラ検索用のschema9、`enemies::catalog` は敵検索用のschema1の表示アダプタを生成する。キャラ詳細の体力・攻撃力と直接命中は、現版ネイティブで照合したC++へ渡す。コスト・時間・敵検索等の既存Web表示値を、未検証のまま戦闘の確定仕様へ転用しない。

API根拠: [wry](https://docs.rs/wry/0.57.0/wry/)、[tao](https://docs.rs/tao/0.37.1/tao/)、[rusqlite](https://docs.rs/rusqlite/0.40.2/rusqlite/)。実際の版はCargo.lockで固定する。

## UI・プレビュー・更新

入口のキャラデータはWebのunit-search。アイコン付きレア度・属性・特性フィルター、ページングした一覧、列ソート、比較、CSVを再利用する。詳細は別画面のWebと同じ表へ移動する。技術的な説明・原本は折りたたみ、通常画面を占有しない。

`ui/src` の再利用元とSHAは `ui/upstream.json`。同期は `python scripts/sync-ui.py <kbc-webのフォルダ>`。検索ロジック・CSS・共通設定など必要な依存だけをコピーし、参照元には書き込まない。通常の配布・起動は元WebのcheckoutやNode.jsに依存しない。ES modules/CSSをそのまま埋め込むため、npmビルドも不要。

本能はRustでCSVを正規化し、UIのtalents.jsがWeb由来のapplyUnitTalentsと共通の成長計算を組み合わせて表へ反映する。C++の直接命中・割合攻撃へダメージ計算を接続する。装着玉の状態管理等を含む戦闘ランタイムは未実装。修正は同期スクリプトの小さいアダプタとui/detail.jsに局所化する。共通の色・表・アイコン切り抜きのCSSは元Webから維持する。workspace.js/native.cssがPC用の枠と要素配置を受け持ち、ページ専用の一覧・絞り込みを左、計算・表示条件を右へ置く。中央は残りの幅・高さを使い、全機能ナビはホームにまとめ、上部はホーム・履歴の戻る/次へ・再読み込みにする。検索・比較・編成の状態はnative-state.jsのsessionStorageへ保存し、リンクコピーや外部データ元リンクは画面に置かない。

更新はServiceがworkerを起動し、UIはstatusをポーリングする。現在のDBを閲覧したまま新snapshotを検証・公開できる。current切替後は表示キャッシュを破棄し、新しいDBから取得する。画像とアトラスも検証済み原本をSQLiteへ保持する。

## Rust/C++境界と将来設計

現行ABIは3。0.1.30で戦闘画面状態とSceneInput/Layoutを拡張したため、ホストとコアを同時に更新する。固定幅整数のPODを呼出中だけ借用し、C++は状態やポインタを保持しない。Serviceの計算APIからkbcs-bridgeの安全なラッパーを経由し、基礎値・味方命中・敵命中・味方メタルキラー・敵毒撃の入口を分ける。基礎値は全Lvを一括計算してUI側で参照する。出現待機と候補選択も借用状態へのtick/commitとして追加したが、UIやHTTPには接続していない。根拠と関数関係は[nativeの設計](../../native/kbcs-core/docs/README.md)に記録する。

戦闘追加時はC++が独立したシミュレーション状態を所有し、Rustはopaque handleの生成・破棄を対にする。バッチ入力・結果取得を基本とし、細かいFFI往復とフレームごとの不要コピーを避ける。借用バッファを返す場合は次のstep/破棄まで等の寿命をAPI契約で定義する。C++例外は境界内で捕捉してエラー値へ変換する。状態を所有する戦闘APIは今回作成せず、明示した入出力の計算と出現待機だけを先に共用する。

同じC++コアをGUI再生とheadlessバッチから呼び、固定ステップ・明示した初期条件とシードで結果を再現する。コアは描画・GUI・SQLiteを呼ばない。状態と乱数はシミュレーションごとに独立させる。姿勢計算もコア側へ置き、Rustは計算結果を描画する。ゲーム時間・判定・補間の仕様は解析根拠が揃うまで確定しない。

敵・ステージはdata、将来の戦闘はnative、APK出力とAI制御は必要時にRustの独立領域へ追加する。公式snapshotを編集用DBとして開かない。

0.1.7ではstages::import/catalogが0番台の6表とWeb表示を接続する。検索・詳細は共通Serviceの/api/stagesを使用し、XPはcalculateNative→Service→experience::legend→C++へ渡す。DBの版と定義・コアの版を照合する。出現tick/commitの状態、乱数、敵個体の生成を閲覧UIは所有しない。


0.1.15は全29系列のステージDBを公開する。検索は`/api/stages`の軽量索引、詳細は`?map=KEY`でマップ単位に取得する。DBパスごとにキャッシュを無効化し、索引と詳細のbuildId/revision一致をUIでも検査する。`/api/stage-variant`はDBの候補関係を検証してから返す。XPはstageExperienceを64件ずつ共通C++入口へ渡し、章/内部種別による入口を保持する。出現・抽選・報酬のゲーム内状態を閲覧UIで勝手に進めない。


0.1.16のモーション閲覧は、Rustの保存済み原本manifestとC++のKB/魂時計、既存JavaScriptの整数姿勢評価/WebGL描画を接続する。パーツ表示マスクと描画を分離し、非表示の親も座標計算へ残す。姿勢評価自体のC++移植は今後であり、現時点の閲覧用評価器を戦闘ランタイムの完成扱いにしない。詳細はui/src/features/motion/docs。

0.1.17のその他モーションも既存の同一姿勢/描画エンジンを使用。Rustはeffectsの素材対応と原本、JavaScriptの既存effect-sequenceは演出の時計と描画インスタンスだけを返す。戦闘状態や当たり判定と結合しない。

0.1.18ではキャラ検索と敵検索/詳細/ステージ内のHP・攻撃も共通C++へ接続した。敵の行倍率と冠倍率を分離して整数化順を保持する。盾/所持金/時間等の表示補助とモーション評価は引き続きWeb由来。ステージ索引は明細を組み立てず集約SQLから生成し、Serviceのキャッシュロック中に生成しない。検証範囲は[外部評価対応](../plans/review-20261023.md)。

0.1.20では通常取得を既存GitHub assetsの固定commitへ向け、原本をAppData/assetsのSHAキャッシュへ永続保存する。source_fileの既存原本も再利用し、アプリ版と原本/変換器版を分ける。DBと原本の保管先はexe更新から独立する。

0.1.21はステージの姿勢・カメラ・背景/城・背景演出をC++へ接続した。描画コアの命令はGUIとCLIで共用し、GPUへの転送をUIへ残す。演出Runtimeだけはopaque handle内に状態を所有し、作成/破棄・Mutex・独立シードを契約化する。従来の純粋計算PODの借用契約は維持する。詳細は[native描画](../../native/kbcs-core/docs/render.md)。

0.1.22の編成はService→formations::Store→独立したユーザーSQLiteへ保存する。公式更新はuser領域へ触れない。UIの編成専用profileは既存DB閲覧のlocalStorageと分離する。原本画像・上部座標・関数対応は[編成UI](../../ui/docs/formation.md)。

0.1.26の既存ステージ出撃準備は検索を流用し、独立したstage-sortieへ進む。城体力・スニャイパーの到達済み命中・速度の基礎関数はC++/Rustで共用し、ローカルARM64の局所実行で整数と乱数幅を照合する。出撃は素材ロードと0F初期盤面までで、戦闘進行は未接続。[出撃準備](../../ui/docs/stage-sortie.md)、[戦闘補助](../../native/kbcs-core/docs/battle-support.md)を参照。


0.1.27では出撃可否・生産コストもC++のPOD入力へ共用する。JSON由来の条件選択と文書保存はRust/JavaScript、数値判定はnative。静的な編成可否と戦闘中の同時数・資金・生産総数を分ける。編成用の本能玉枠メタデータは採用元SHA付きの同版定義をRust catalog/保存検査で共用し、既存公式DBの一括再生成を要求しない。

0.1.29はbattle_screenのPODへ暗転・HUDの時計・経済・入力待ちと配置を共用する。生成要求の成功をUIが仮定せず、個体構築との接続を残す。[戦闘画面](../../native/kbcs-core/docs/battle-screen.md)。
