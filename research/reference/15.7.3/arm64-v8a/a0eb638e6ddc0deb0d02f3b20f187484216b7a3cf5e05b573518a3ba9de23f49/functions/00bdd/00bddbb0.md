# 00bddbb0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bddb00`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb00.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/high-0016.md#compare-4b04f36d641c3886d694830301d033b3)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddbb0",
  "name": "_ZN8firebase4auth4User8GetTokenEb",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "500a36ce26870dd7ef6cc883766c4e7fa177b616cc65594f467b254adffacc10",
  "source_text_sha256": "500a36ce26870dd7ef6cc883766c4e7fa177b616cc65594f467b254adffacc10"
}
~~~

## 呼び出し元

- [00848250](../00848/00848250.md)
- [00ad4ff4](../00ad4/00ad4ff4.md)
- [00b7262c](../00b72/00b7262c.md)

## 呼び出し先

- [00b6eeac](../00b6e/00b6eeac.md)

## 疑似コード / UTF-8 125 bytes

~~~c

void _ZN8firebase4auth4User8GetTokenEb(void)

{
  (*(code *)PTR__ZN8firebase4auth4User8GetTokenEb_00c1d668)();
  return;
}

~~~
