# ネイティブ関数のバージョン間追跡

[追跡SQLite](https://github.com/sinsuirakv0/KBCS/releases/download/native-analysis-16.0.0-arm64-v8a-70b5c9c0dcc036b2/native-tracking-1688bc2c2fa91324b446a495.sqlite.gz) · [集計と出典](summary.json)

SQLite SHA-256 `d1a7b87d646467baf466fb71b5809174629ba7618fbccadc8d5995c275591e14`

関係は根拠付きの推定です。変更候補は検査範囲と合わせて読みます。
構造とP-codeの一致だけで実行時の挙動は確定しません。

## 連続版の比較

- [v15.7.3 → v15.7.4](0-1/README.md)
- [v15.7.4 → v16.0.0](1-2/README.md)
- [v16.0.0 → v16.0.1](2-3/README.md)

## 3版経路の検証

直接経路は検証に用います。一致した経路も共通の解析器に依存します。

~~~json
{
  "consistent": 35444,
  "gap_candidate": 48,
  "partial": 6051,
  "temporary_change_candidate": 3
}
~~~


[矛盾・再登場・一時変化候補](cycles/README.md)
