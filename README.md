# KBCS

今回の実装範囲は、独立した[Ghidra解析キャッシュ基盤](research/README.md)です。
初期対象は15.7.2。戦闘エンジン、Rust制御、UIは含みません。

APK・SO・Ghidraプロジェクト・SQLite・疑似コードは `research/.local/` に保存し、Gitから除外します。

全関数の参考資料・検索DB・復元用プロジェクトは、このPrivateリポジトリのReleaseへ保存します。[取得・復元手順](research/docs/github-storage.md)を参照してください。

全件処理の最終結果は[全関数キャッシュ実測・保存報告](research/docs/complete-report.md)を参照してください。

[保存済み解析資料（Private Release）](https://github.com/sinsuirakv0/KBCS/releases/tag/native-v15.7.2)
