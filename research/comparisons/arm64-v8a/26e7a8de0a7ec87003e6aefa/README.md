# ネイティブ関数のバージョン間追跡

[追跡SQLite](https://github.com/sinsuirakv0/KBCS/releases/download/native-analysis-16.0.3-arm64-v8a-9afc4f9e264e1fda/native-tracking-94b38b17a38d0d931d7a8a95.sqlite) · [集計と出典](summary.json)

SQLite SHA-256 `54653a77a313227100f4eb8ea952e01fb881aa5702c5f8de9e7fe12fb66eb22b`

関係は根拠付きの推定です。変更候補は検査範囲と合わせて読みます。
構造とP-codeの一致だけで実行時の挙動は確定しません。

## 連続版の比較

- [v16.0.1 → v16.0.2](0-1/README.md)
- [v16.0.2 → v16.0.3](1-2/README.md)

## 3版経路の検証

直接経路は検証に用います。一致した経路も共通の解析器に依存します。

~~~json
{
  "consistent": 22722,
  "gap_candidate": 173,
  "partial": 276,
  "temporary_change_candidate": 3
}
~~~


[矛盾・再登場・一時変化候補](cycles/README.md)
