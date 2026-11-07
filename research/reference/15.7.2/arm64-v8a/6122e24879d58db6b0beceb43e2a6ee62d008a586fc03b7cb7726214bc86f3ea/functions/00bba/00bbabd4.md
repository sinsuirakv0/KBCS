# 00bbabd4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00bbace0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbace0.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00bbabd4",
  "name": "__cxa_get_globals_fast",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "454f2618440951def784c9f3f68bcb87c5cc95ede6b9665b02bfa21a225ab47c",
  "source_text_sha256": "454f2618440951def784c9f3f68bcb87c5cc95ede6b9665b02bfa21a225ab47c"
}
~~~

## 呼び出し元

- [00be1ce0](../00be1/00be1ce0.md)

## 呼び出し先

- [00bdd3a0](../00bdd/00bdd3a0.md)

## 疑似コード / UTF-8 786 bytes

~~~c

void __cxa_get_globals_fast(void)

{
                    /* catch() { ... } // from try @ 00bb7384 with catch @ 00bbabd8 */
                    /* catch() { ... } // from try @ 00bb6fd0 with catch @ 00bbabdc */
                    /* catch() { ... } // from try @ 00bb6c1c with catch @ 00bbabe0 */
                    /* catch() { ... } // from try @ 00bb6868 with catch @ 00bbabe4 */
                    /* catch() { ... } // from try @ 00bb64b4 with catch @ 00bbabe8 */
  __emutls_get_address(&DAT_00c248a8);
                    /* catch() { ... } // from try @ 00bb6100 with catch @ 00bbabec */
                    /* catch() { ... } // from try @ 00bb5d40 with catch @ 00bbabf0 */
                    /* catch() { ... } // from try @ 00bb5980 with catch @ 00bbabf4 */
  return;
}

~~~
