# 00bbace0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

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
