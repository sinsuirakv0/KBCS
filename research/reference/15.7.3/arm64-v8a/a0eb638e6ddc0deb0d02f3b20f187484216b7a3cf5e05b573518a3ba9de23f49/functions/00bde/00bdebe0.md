# 00bdebe0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdeb30`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeb30.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/high-0019.md#compare-fd7f19bb20a665238c84777537f2d54c)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdebe0",
  "name": "_ZN8firebase8callback11AddCallbackEPNS0_8CallbackE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c42dbc6dcde9d2fe2aeca7bf48ea2b2858d10cdaac0c27e880aa74506564bbdf",
  "source_text_sha256": "c42dbc6dcde9d2fe2aeca7bf48ea2b2858d10cdaac0c27e880aa74506564bbdf"
}
~~~

## 呼び出し元

- [00afbba4](../00afb/00afbba4.md)
- [00afbc2c](../00afb/00afbc2c.md)

## 呼び出し先

- [00afba04](../00afb/00afba04.md)

## 疑似コード / UTF-8 159 bytes

~~~c

void _ZN8firebase8callback11AddCallbackEPNS0_8CallbackE(void)

{
  (*(code *)PTR__ZN8firebase8callback11AddCallbackEPNS0_8CallbackE_00c1de80)();
  return;
}

~~~
