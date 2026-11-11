# ネイティブ関数のバージョン間追跡

[追跡SQLite](https://github.com/sinsuirakv0/KBCS/releases/download/native-analysis-16.0.1-arm64-v8a-711084564ddd8b14/native-tracking-36c86d03017a729217bc7303.sqlite) · [集計と出典](summary.json)

SQLite SHA-256 `083bb3ddf223597a80714a144465839bdd70c4758d17b2be444da99a3ba92e78`

関係は根拠付きの推定です。変更候補は検査範囲と合わせて読みます。
構造とP-codeの一致だけで実行時の挙動は確定しません。

## 連続版の比較

- [v15.7.4 → v16.0.0](0-1/README.md)
- [v16.0.0 → v16.0.1](1-2/README.md)

## 3版経路の検証

直接経路は検証に用います。一致した経路も共通の解析器に依存します。

~~~json
{
  "consistent": 17879,
  "gap_candidate": 38,
  "partial": 113,
  "temporary_change_candidate": 8
}
~~~


[矛盾・再登場・一時変化候補](cycles/README.md)
