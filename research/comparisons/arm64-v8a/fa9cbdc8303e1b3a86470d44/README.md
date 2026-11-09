# ネイティブ関数のバージョン間追跡

[追跡SQLite](https://github.com/sinsuirakv0/KBCS/releases/download/native-analysis-16.0.0-arm64-v8a-70b5c9c0dcc036b2/native-tracking-a52fad719fac68325aff5ff6.sqlite) · [集計と出典](summary.json)

SQLite SHA-256 `762bf1af8ff19b0df0a358a5a880b8db20d03167967b0f9b5b0419430e5d658b`

関係は根拠付きの推定です。変更候補は検査範囲と合わせて読みます。
構造とP-codeの一致だけで実行時の挙動は確定しません。

## 連続版の比較

- [v15.7.3 → v15.7.4](0-1/README.md)
- [v15.7.4 → v16.0.0](1-2/README.md)

## 3版経路の検証

直接経路は検証に用います。一致した経路も共通の解析器に依存します。

~~~json
{
  "consistent": 17949,
  "gap_candidate": 6,
  "partial": 5855,
  "temporary_change_candidate": 2
}
~~~


[矛盾・再登場・一時変化候補](cycles/README.md)
