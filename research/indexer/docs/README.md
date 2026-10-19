# ローカル制御・取込

- `apk.gh_json/content`：gh認証を再利用して版情報とRelease情報を読む。
- `apk.manifest/acquire`：manifest三値・ハッシュを照合し、ABI別にSOを保存する。
- `run.mcp`：loopback限定のGZF出力API。通常検索には不要。
- `run.locked`：書込排他。`headless`：JVM起動・時間制限・ログ完了判定・メモリ計測。
- `run.main`：新規初回解析、既存スナップショット準備、索引、未保存関数要求を組み立てる。
- `store.digest/read_json/write_json`：ハッシュ・BOM対応JSON入出力。
- `store.connect/import_index/sync_results`：スキーマ、索引の原子的取込、再開可能な状態同期。
- `test_store`：中途索引のロールバックとジャーナル再開/ファイル消失だけを検証。
- `complete.main`：独立リビジョンを複製し、時間制限なしの自動解析と全件デコンパイルを段階的に再開する。`build_reference`：外部関数の区別、TSV索引、件数整合、既定参照資料の準備。
- `complete.recover_failed`：失敗関数のみ、構文木なしの標準設定・conservative・minimalの有限3段階で再試行する。追加設定の復旧結果は低確度として区別する。
- `memory.processes/enforce_memory`：Windowsのプロセス親子関係とPrivate Bytesを調べ、起動したJVM直下のデコンパイラだけにメモリ保護を適用する。`memory.main`は既に実行中の自分のJVMへ同じ監視を付ける補助手段。

データの相互関係と限界は[共通設計](../../docs/architecture.md)を参照。

- `materials.selected_files/main`：保存対象を限定し、重複プロジェクト・一時物を除いたアーカイブとSHA-256一覧を作る。アップロードは行わない。
