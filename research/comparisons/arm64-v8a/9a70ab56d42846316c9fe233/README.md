# ネイティブ関数のバージョン間追跡

[追跡SQLite](https://github.com/sinsuirakv0/KBCS/releases/download/native-analysis-16.0.2-arm64-v8a-ea0159f06d493a87/native-tracking-b66f6538900ba90adf8d51d5.sqlite) · [集計と出典](summary.json)

SQLite SHA-256 `3c1c14427641660465a452ed864d6aad374b755d2ee060484196731dbb03ac91`

関係は根拠付きの推定です。変更候補は検査範囲と合わせて読みます。
構造とP-codeの一致だけで実行時の挙動は確定しません。

## 連続版の比較

- [v16.0.0 → v16.0.1](0-1/README.md)
- [v16.0.1 → v16.0.2](1-2/README.md)

## 3版経路の検証

直接経路は検証に用います。一致した経路も共通の解析器に依存します。

~~~json
{
  "consistent": 22596,
  "gap_candidate": 172,
  "partial": 203,
  "temporary_change_candidate": 4
}
~~~


[矛盾・再登場・一時変化候補](cycles/README.md)
