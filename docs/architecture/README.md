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

本能はRustでCSVを正規化し、UIのtalents.jsがWeb由来のapplyUnitTalentsと共通の成長計算を組み合わせて表へ反映する。C++の直接命中・割合攻撃へダメージ計算を接続する。装着玉の状態管理等を含む戦闘ランタイムは未実装。修正は同期スクリプトの小さいアダプタとui/detail.jsに局所化する。共通の色・表・アイコン切り抜きのCSSは元Webから維持する。workspace.js/native.cssがPC用の枠と要素配置を受け持ち、ページ専用の一覧・絞り込みを左、計算・表示条件を右へ置く。中央は残りの幅・高さを使い、全機能ナビは上部にまとめる。検索・比較・編成の状態はnative-state.jsのsessionStorageへ保存し、リンクコピーや外部データ元リンクは画面に置かない。

更新はServiceがworkerを起動し、UIはstatusをポーリングする。現在のDBを閲覧したまま新snapshotを検証・公開できる。current切替後は表示キャッシュを破棄し、新しいDBから取得する。画像とアトラスも検証済み原本をSQLiteへ保持する。

## Rust/C++境界と将来設計

現行ABIは2。固定幅整数のPODを呼出中だけ借用し、C++は状態やポインタを保持しない。Serviceの計算APIからkbcs-bridgeの安全なラッパーを経由し、基礎値・味方命中・敵命中・味方メタルキラー・敵毒撃の入口を分ける。基礎値は全Lvを一括計算してUI側で参照する。出現待機と候補選択も借用状態へのtick/commitとして追加したが、UIやHTTPには接続していない。根拠と関数関係は[nativeの設計](../../native/kbcs-core/docs/README.md)に記録する。

戦闘追加時はC++が独立したシミュレーション状態を所有し、Rustはopaque handleの生成・破棄を対にする。バッチ入力・結果取得を基本とし、細かいFFI往復とフレームごとの不要コピーを避ける。借用バッファを返す場合は次のstep/破棄まで等の寿命をAPI契約で定義する。C++例外は境界内で捕捉してエラー値へ変換する。状態を所有する戦闘APIは今回作成せず、明示した入出力の計算と出現待機だけを先に共用する。

同じC++コアをGUI再生とheadlessバッチから呼び、固定ステップ・明示した初期条件とシードで結果を再現する。コアは描画・GUI・SQLiteを呼ばない。状態と乱数はシミュレーションごとに独立させる。姿勢計算もコア側へ置き、Rustは計算結果を描画する。ゲーム時間・判定・補間の仕様は解析根拠が揃うまで確定しない。

敵・ステージはdata、将来の戦闘はnative、APK出力とAI制御は必要時にRustの独立領域へ追加する。公式snapshotを編集用DBとして開かない。

0.1.7ではstages::import/catalogが0番台の6表とWeb表示を接続する。検索・詳細は共通Serviceの/api/stagesを使用し、XPはcalculateNative→Service→experience::legend→C++へ渡す。DBの版と定義・コアの版を照合する。出現tick/commitの状態、乱数、敵個体の生成を閲覧UIは所有しない。


0.1.15は全29系列のステージDBを公開する。検索は`/api/stages`の軽量索引、詳細は`?map=KEY`でマップ単位に取得する。DBパスごとにキャッシュを無効化し、索引と詳細のbuildId/revision一致をUIでも検査する。`/api/stage-variant`はDBの候補関係を検証してから返す。XPはstageExperienceを64件ずつ共通C++入口へ渡し、章/内部種別による入口を保持する。出現・抽選・報酬のゲーム内状態を閲覧UIで勝手に進めない。


0.1.16のモーション閲覧は、Rustの保存済み原本manifestとC++のKB/魂時計、既存JavaScriptの整数姿勢評価/WebGL描画を接続する。パーツ表示マスクと描画を分離し、非表示の親も座標計算へ残す。姿勢評価自体のC++移植は今後であり、現時点の閲覧用評価器を戦闘ランタイムの完成扱いにしない。詳細はui/src/features/motion/docs。

0.1.17のその他モーションも既存の同一姿勢/描画エンジンを使用。Rustはeffectsの素材対応と原本、JavaScriptの既存effect-sequenceは演出の時計と描画インスタンスだけを返す。戦闘状態や当たり判定と結合しない。
