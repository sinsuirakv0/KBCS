# 00bbace0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbac9c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbac9c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/high-0011.md#compare-8f7e8fe1d2bfa265a2430422e780df2c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbace0",
  "name": "__cxa_get_globals_fast",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f4ff2f89d9b652fda7a5978b4731454daade64a1b801b48d17bd5d4b38353565",
  "source_text_sha256": "f4ff2f89d9b652fda7a5978b4731454daade64a1b801b48d17bd5d4b38353565"
}
~~~

## 呼び出し元

- [00be1de0](../00be1/00be1de0.md)

## 呼び出し先

- [00bdd4a0](../00bdd/00bdd4a0.md)

## 疑似コード / UTF-8 786 bytes

~~~c

void __cxa_get_globals_fast(void)

{
                    /* catch() { ... } // from try @ 00bb7490 with catch @ 00bbace4 */
                    /* catch() { ... } // from try @ 00bb70dc with catch @ 00bbace8 */
                    /* catch() { ... } // from try @ 00bb6d28 with catch @ 00bbacec */
                    /* catch() { ... } // from try @ 00bb6974 with catch @ 00bbacf0 */
                    /* catch() { ... } // from try @ 00bb65c0 with catch @ 00bbacf4 */
  __emutls_get_address(&DAT_00c249a8);
                    /* catch() { ... } // from try @ 00bb620c with catch @ 00bbacf8 */
                    /* catch() { ... } // from try @ 00bb5e4c with catch @ 00bbacfc */
                    /* catch() { ... } // from try @ 00bb5a8c with catch @ 00bbad00 */
  return;
}

~~~
