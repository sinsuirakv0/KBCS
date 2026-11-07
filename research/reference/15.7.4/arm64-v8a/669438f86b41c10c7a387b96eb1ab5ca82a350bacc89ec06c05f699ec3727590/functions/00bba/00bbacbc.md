# 00bbacbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00bbabb0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbabb0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00bbacbc",
  "name": "__cxa_get_globals",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "998c20d0a12841ce6181cf7234e24858eab4c86da47408bb0a3e0fc8674f0045",
  "source_text_sha256": "998c20d0a12841ce6181cf7234e24858eab4c86da47408bb0a3e0fc8674f0045"
}
~~~

## 呼び出し元

- [00be1dd0](../00be1/00be1dd0.md)

## 呼び出し先

- [00bdd4a0](../00bdd/00bdd4a0.md)

## 疑似コード / UTF-8 3712 bytes

~~~c

void __cxa_get_globals(void)

{
                    /* catch() { ... } // from try @ 00bb4e34 with catch @ 00bbacc0 */
                    /* catch() { ... } // from try @ 00bb4a54 with catch @ 00bbacc4 */
                    /* catch() { ... } // from try @ 00bb4694 with catch @ 00bbacc8 */
  __emutls_get_address(&DAT_00c249a8);
                    /* catch() { ... } // from try @ 00bba020 with catch @ 00bbacd8 */
                    /* catch() { ... } // from try @ 00bb36c0 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb389c with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb3c2c with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb404c with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb4438 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb4818 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb4bd8 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb4fb8 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb5398 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb54f8 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb5750 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb5b10 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb5ed0 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb6290 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb6644 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb69f8 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb6dac with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb7160 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb7514 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb78c4 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb7968 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb7a18 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb7ac4 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb7b74 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb7e70 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb80b8 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb87c8 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb8aa0 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb8c7c with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb8d30 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb8e9c with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb8f40 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb9218 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb94f0 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb974c with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb9acc with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb9bfc with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bba0ac with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bba508 with catch @ 00bbacdc */
  return;
}

~~~
