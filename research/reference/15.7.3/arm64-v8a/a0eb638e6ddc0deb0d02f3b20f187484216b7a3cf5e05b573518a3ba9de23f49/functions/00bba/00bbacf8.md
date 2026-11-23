# 00bbacf8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbac30`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbac30.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/inspection-0006.md#compare-026383cd41d1f819165735de3e296007)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbacf8",
  "name": "_ZNSt9exceptionD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "91ebc617da88d03cd05fa623b4417b5d8a5fbeb1a1f78db9997d5a879008e22a",
  "source_text_sha256": "91ebc617da88d03cd05fa623b4417b5d8a5fbeb1a1f78db9997d5a879008e22a"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)
- [00be1df0](../00be1/00be1df0.md)

## 疑似コード / UTF-8 1487 bytes

~~~c

void _ZNSt9exceptionD0Ev(void *param_1)

{
                    /* catch() { ... } // from try @ 00bb39c4 with catch @ 00bbacfc */
                    /* catch() { ... } // from try @ 00bb41c0 with catch @ 00bbad00 */
                    /* catch() { ... } // from try @ 00bb3dd4 with catch @ 00bbad04 */
                    /* catch() { ... } // from try @ 00bb39b4 with catch @ 00bbad08 */
                    /* catch() { ... } // from try @ 00bba298 with catch @ 00bbad0c
                       catch() { ... } // from try @ 00bba3e8 with catch @ 00bbad0c */
  _ZNSt20bad_array_new_lengthD1Ev();
                    /* catch() { ... } // from try @ 00bba280 with catch @ 00bbad10
                       catch() { ... } // from try @ 00bba3d0 with catch @ 00bbad10 */
                    /* catch() { ... } // from try @ 00bba268 with catch @ 00bbad14
                       catch() { ... } // from try @ 00bba3b8 with catch @ 00bbad14 */
                    /* catch() { ... } // from try @ 00bba250 with catch @ 00bbad18
                       catch() { ... } // from try @ 00bba3a0 with catch @ 00bbad18 */
                    /* catch() { ... } // from try @ 00bba238 with catch @ 00bbad1c
                       catch() { ... } // from try @ 00bba388 with catch @ 00bbad1c */
                    /* catch() { ... } // from try @ 00bba220 with catch @ 00bbad20
                       catch() { ... } // from try @ 00bba370 with catch @ 00bbad20 */
  _ZdlPv(param_1);
  return;
}

~~~
