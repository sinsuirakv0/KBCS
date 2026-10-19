# Ghidra側

`ExportCache.run` はindex/decompileの2モードを持つ。indexはFunctionManagerとReferenceManagerを走査しJSONLへ直接保存する。バックアップはJVM終了後にPython側で行う。
decompileは要求ファイルを順番に処理し、DecompInterfaceをバッチ内で再利用して最後にdisposeする。
`row` は小さなJSONレコード、`emit` は1行出力、`key` はアドレス文字列表現を共通化する。
元プログラムの名前・型・コメント・バイトを変更しない。詳細は[共通設計](../../docs/architecture.md)。
