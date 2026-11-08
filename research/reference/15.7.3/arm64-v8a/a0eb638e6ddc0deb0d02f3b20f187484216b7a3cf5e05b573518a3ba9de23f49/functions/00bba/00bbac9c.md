# 00bbac9c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bbac9c",
  "name": "__cxa_get_globals_fast",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "680138874b5c4801104343cc0650f30ac6e261b798b76086a50d518f724c56c7",
  "source_text_sha256": "680138874b5c4801104343cc0650f30ac6e261b798b76086a50d518f724c56c7"
}
~~~

## 呼び出し元

- [00be1d90](../00be1/00be1d90.md)

## 呼び出し先

- [00bdd450](../00bdd/00bdd450.md)

## 疑似コード / UTF-8 786 bytes

~~~c

void __cxa_get_globals_fast(void)

{
                    /* catch() { ... } // from try @ 00bb744c with catch @ 00bbaca0 */
                    /* catch() { ... } // from try @ 00bb7098 with catch @ 00bbaca4 */
                    /* catch() { ... } // from try @ 00bb6ce4 with catch @ 00bbaca8 */
                    /* catch() { ... } // from try @ 00bb6930 with catch @ 00bbacac */
                    /* catch() { ... } // from try @ 00bb657c with catch @ 00bbacb0 */
  __emutls_get_address(&DAT_00c24958);
                    /* catch() { ... } // from try @ 00bb61c8 with catch @ 00bbacb4 */
                    /* catch() { ... } // from try @ 00bb5e08 with catch @ 00bbacb8 */
                    /* catch() { ... } // from try @ 00bb5a48 with catch @ 00bbacbc */
  return;
}

~~~
