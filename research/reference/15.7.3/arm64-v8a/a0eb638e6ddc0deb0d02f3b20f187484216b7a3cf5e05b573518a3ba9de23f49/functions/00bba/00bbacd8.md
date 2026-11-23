# 00bbacd8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbac10`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbac10.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/high-0010.md#compare-56ebe19c96f4c16b37e474a75eefaae7)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbacd8",
  "name": "__cxa_deleted_virtual",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e3b3897887f50e4fda770934f06cf0ca9e4ba99690801a0a87724c8e7e826c71",
  "source_text_sha256": "e3b3897887f50e4fda770934f06cf0ca9e4ba99690801a0a87724c8e7e826c71"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bbb158](../00bbb/00bbb158.md)

## 関連文字列（未確認候補）

~~~text
"Deleted virtual function called!"
~~~

## 疑似コード / UTF-8 589 bytes

~~~c

void __cxa_deleted_virtual(void)

{
                    /* catch() { ... } // from try @ 00bb42d4 with catch @ 00bbacdc */
                    /* catch() { ... } // from try @ 00bb3ee8 with catch @ 00bbace0 */
                    /* catch() { ... } // from try @ 00bb3ac8 with catch @ 00bbace4 */
                    /* catch() { ... } // from try @ 00bb41e8 with catch @ 00bbace8 */
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00bb41d0 with catch @ 00bbacec */
  FUN_00bbb158("Deleted virtual function called!");
}

~~~
