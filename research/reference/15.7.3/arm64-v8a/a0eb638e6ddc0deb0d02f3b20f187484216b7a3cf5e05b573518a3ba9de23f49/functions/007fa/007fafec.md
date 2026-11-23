# 007fafec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `007fafec`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fa/007fafec.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/detail_skipped-0013.md#compare-fc02860733667830c9256063c5891077)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007fafec",
  "name": "FUN_007fafec",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c1bd3a7b0aff5d7a4f97e42440eef4951f64b116686ab12ffb1e3c68e1a3c494",
  "source_text_sha256": "c1bd3a7b0aff5d7a4f97e42440eef4951f64b116686ab12ffb1e3c68e1a3c494"
}
~~~

## 呼び出し元

- [007e5fa4](../007e5/007e5fa4.md)

## 呼び出し先

- [007faff8](../007fa/007faff8.md)

## 疑似コード / UTF-8 168 bytes

~~~c

void FUN_007fafec(long param_1)

{
                    /* catch() { ... } // from try @ 007fa778 with catch @ 007faff0 */
  FUN_007faff8(param_1 + 0x18);
  return;
}

~~~
