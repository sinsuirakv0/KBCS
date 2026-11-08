# ネイティブ関数のバージョン間追跡

[追跡SQLite](https://github.com/sinsuirakv0/KBCS/releases/download/native-analysis-15.7.4-arm64-v8a-6cf79e30b2bdfc73/native-tracking-b06830b06ac477b7d113c0be.sqlite) · [集計と出典](summary.json)

SQLite SHA-256 `24f9d4a65fbefee261f30109ff119a7959189b6949611cccc1ec66be17c29dda`

関係は根拠付きの推定です。変更候補は検査範囲と合わせて読みます。
構造とP-codeの一致だけで実行時の挙動は確定しません。

## 連続版の比較

- [v15.7.2 → v15.7.3](0-1/README.md)
- [v15.7.3 → v15.7.4](1-2/README.md)

## 3版経路の検証

直接経路は検証に用います。一致した経路も共通の解析器に依存します。

~~~json
{
  "consistent": 23372,
  "gap_candidate": 36,
  "partial": 274,
  "temporary_change_candidate": 56
}
~~~


[矛盾・再登場・一時変化候補](cycles/README.md)
