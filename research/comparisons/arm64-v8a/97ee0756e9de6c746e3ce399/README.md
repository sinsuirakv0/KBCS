# ネイティブ関数のバージョン間追跡

[追跡SQLite](https://github.com/sinsuirakv0/KBCS/releases/download/native-analysis-15.7.3-arm64-v8a-45565ee9c155ae02/native-tracking-92445ee9094944231366a70a.sqlite.gz) · [集計と出典](summary.json)

SQLite SHA-256 `268faae4010579b653606813caa0a3dc3041ea62a3d172f732b9bd4a6d5e0576`

関係は根拠付きの推定です。変更候補は検査範囲と合わせて読みます。
構造とP-codeの一致だけで実行時の挙動は確定しません。

## 連続版の比較

- [v15.7.2 → v15.7.3](0-1/README.md)
- [v15.7.3 → v15.7.4](1-2/README.md)

## 3版経路の検証

直接経路は検証に用います。一致した経路も共通の解析器に依存します。

~~~json
{
  "consistent": 23251,
  "gap_candidate": 43,
  "partial": 276,
  "temporary_change_candidate": 56
}
~~~


[矛盾・再登場・一時変化候補](cycles/README.md)
