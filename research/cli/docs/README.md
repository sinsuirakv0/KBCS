# 検索CLI

`cache.main` が引数を解析し、既存SQLiteを検索する。関数名/アドレス、文字列、呼出元/先、参照、疑似コード、未キャッシュ一覧、統計を提供する。
SQLパラメータをバインドし、既定10件・最大100件、文字列240文字、疑似コード4000文字に抑える。
起動時の `store.sync_results` はGhidraが中断した場合の結果ジャーナルを同期する。
使い方は[research README](../../README.md)、保存構造は[共通設計](../../docs/architecture.md)を参照。
