# 関数対応 15.7.2 → 15.7.4

[旧版の解析資料](../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md) · [新版の解析資料](README.md) · [検索用SQLite](https://github.com/sinsuirakv0/KBCS/releases/download/native-analysis-15.7.4-arm64-v8a-6cf79e30b2bdfc73/function-matches-54f34cb09a8bc06d5bef1696.sqlite)

内部関数の採用 23,120 組。旧版側の候補あり 2,112 件、候補なし 1 件。
名前を隠した検証は正解 1,350、誤対応 0、保留 127 件。

対応先と根拠を調べるには `python -m cli.match show <旧アドレス> --db <SQLite>` を使う。`--side new` で新版から検索できる。
本文差は復元表現の差を含む。候補がない関数も削除・追加とは断定しない。

SQLite SHA-256 `54f34cb09a8bc06d5bef16963bb829267950f0332a63e04ab1de8f1599a7e1dc`
