# kbcs-app

mainがGUI・CLI・previewを選ぶ。desktop::runはtaoでWindowを作り、wry/WebView2で埋込みuiを表示する。service::Serviceは専用プロトコルとHTTPプレビューの共通処理を持つ。

- GET /api/catalog: SQLite → view::catalog。公開snapshotごとの表示キャッシュ。
- GET /api/asset/<logical path>: 保存済みPNG。原本のフォルダやネットワークは不要。
- GET /api/source?id=: 選択キャラの原本CSV・SHA・出典。
- GET /api/status / POST /api/import: 更新workerの状態と開始。

通常起動は専用プロトコルでポートを使わない。previewコマンドはループバックだけで待ち受け、同じ画面をサイドパネルで確認できる。画面の責務と再利用元は[uiの資料](../../../ui/docs/README.md)。戦闘ロジックをここへ追加しない。
