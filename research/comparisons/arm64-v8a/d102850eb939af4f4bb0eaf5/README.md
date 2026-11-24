# ネイティブ関数のバージョン間追跡

[追跡SQLite](https://github.com/sinsuirakv0/KBCS/releases/download/native-analysis-16.0.3-arm64-v8a-9afc4f9e264e1fda/native-tracking-ace1af3c956b7abe25bf44c2.sqlite.gz) · [集計と出典](summary.json)

SQLite SHA-256 `156ff506eb9653420c46ba23b42f87f38737760cf18e0c6b23028e97546cc11c`

関係は根拠付きの推定です。変更候補は検査範囲と合わせて読みます。
構造とP-codeの一致だけで実行時の挙動は確定しません。

## 連続版の比較

- [v16.0.1 → v16.0.2](0-1/README.md)
- [v16.0.2 → v16.0.3](1-2/README.md)

## 3版経路の検証

直接経路は検証に用います。一致した経路も共通の解析器に依存します。

~~~json
{
  "consistent": 22564,
  "gap_candidate": 175,
  "partial": 279,
  "temporary_change_candidate": 3
}
~~~


[矛盾・再登場・一時変化候補](cycles/README.md)
