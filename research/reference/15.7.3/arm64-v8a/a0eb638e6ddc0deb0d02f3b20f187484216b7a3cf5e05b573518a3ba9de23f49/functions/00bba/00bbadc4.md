# 00bbadc4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbacfc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbacfc.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/high-0010.md#compare-b71d350f77db38cafd40d15b925aa9f4)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbadc4",
  "name": "_ZNSt20bad_array_new_lengthC1Ev",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b2bac531cebebd1cf0e356b9e453096abcd1b39821155444c9ba12c69b4ba796",
  "source_text_sha256": "b2bac531cebebd1cf0e356b9e453096abcd1b39821155444c9ba12c69b4ba796"
}
~~~

## 呼び出し元

- [00bdb190](../00bdb/00bdb190.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 575 bytes

~~~c

void _ZNSt20bad_array_new_lengthC1Ev(long *param_1)

{
                    /* catch() { ... } // from try @ 00bb4d50 with catch @ 00bbadc8 */
                    /* catch() { ... } // from try @ 00bb4d68 with catch @ 00bbadcc */
                    /* catch() { ... } // from try @ 00bb4988 with catch @ 00bbadd0 */
                    /* catch() { ... } // from try @ 00bb4970 with catch @ 00bbadd4 */
  *param_1 = (long)(PTR__ZTVSt20bad_array_new_length_00c1bfd0 + 0x10);
                    /* catch() { ... } // from try @ 00bb45c8 with catch @ 00bbadd8 */
  return;
}

~~~
