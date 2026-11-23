# 00bbad3c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbacf8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/inspection-0017.md#compare-c4ccec6db878d90ad1d5ab078291a010)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbad3c",
  "name": "_ZNSt9exceptionD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a69cc739bb19806e21f63ebb43917b0670c9bd383e65023cf9bccfee24461acd",
  "source_text_sha256": "a69cc739bb19806e21f63ebb43917b0670c9bd383e65023cf9bccfee24461acd"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00be1e40](../00be1/00be1e40.md)

## 疑似コード / UTF-8 1487 bytes

~~~c

void _ZNSt9exceptionD0Ev(void *param_1)

{
                    /* catch() { ... } // from try @ 00bb3a08 with catch @ 00bbad40 */
                    /* catch() { ... } // from try @ 00bb4204 with catch @ 00bbad44 */
                    /* catch() { ... } // from try @ 00bb3e18 with catch @ 00bbad48 */
                    /* catch() { ... } // from try @ 00bb39f8 with catch @ 00bbad4c */
                    /* catch() { ... } // from try @ 00bba2dc with catch @ 00bbad50
                       catch() { ... } // from try @ 00bba42c with catch @ 00bbad50 */
  _ZNSt20bad_array_new_lengthD1Ev();
                    /* catch() { ... } // from try @ 00bba2c4 with catch @ 00bbad54
                       catch() { ... } // from try @ 00bba414 with catch @ 00bbad54 */
                    /* catch() { ... } // from try @ 00bba2ac with catch @ 00bbad58
                       catch() { ... } // from try @ 00bba3fc with catch @ 00bbad58 */
                    /* catch() { ... } // from try @ 00bba294 with catch @ 00bbad5c
                       catch() { ... } // from try @ 00bba3e4 with catch @ 00bbad5c */
                    /* catch() { ... } // from try @ 00bba27c with catch @ 00bbad60
                       catch() { ... } // from try @ 00bba3cc with catch @ 00bbad60 */
                    /* catch() { ... } // from try @ 00bba264 with catch @ 00bbad64
                       catch() { ... } // from try @ 00bba3b4 with catch @ 00bbad64 */
  _ZdlPv(param_1);
  return;
}

~~~
