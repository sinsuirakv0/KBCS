# 00bbaa5c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bba994`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba994.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/high-0010.md#compare-e9d0b69549f9cb0aed9b718d00f7a5e5)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbaa5c",
  "name": "_ZSt15get_new_handlerv",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "283548e1d42701c0b083c1595b0dc48e0badd092f6f7ddc10da1873cd034228d",
  "source_text_sha256": "283548e1d42701c0b083c1595b0dc48e0badd092f6f7ddc10da1873cd034228d"
}
~~~

## 呼び出し元

- [00be1dd0](../00be1/00be1dd0.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 277 bytes

~~~c

undefined8 _ZSt15get_new_handlerv(void)

{
                    /* catch() { ... } // from try @ 00bb3480 with catch @ 00bbaa68 */
                    /* catch() { ... } // from try @ 00bb344c with catch @ 00bbaa6c */
  return *(undefined8 *)PTR___cxa_new_handler_00c1bfb8;
}

~~~
