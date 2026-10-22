# 00bbabb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbabb0.md)

## 関数情報

~~~json
{
  "address": "00bbabb0",
  "name": "__cxa_get_globals",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "77b7c464d03a458ad19ee056a3f4fa0b44a930ec01879c82a2a71287370b68fd",
  "source_text_sha256": "77b7c464d03a458ad19ee056a3f4fa0b44a930ec01879c82a2a71287370b68fd"
}
~~~
## 呼び出し元

- [00be1cd0](../00be1/00be1cd0.md)

## 呼び出し先

- [00bdd3a0](../00bdd/00bdd3a0.md)

## 疑似コード 1/1 / UTF-8 3763 bytes

~~~c

void __cxa_get_globals(void)

{
                    /* catch() { ... } // from try @ 00bb4d28 with catch @ 00bbabb4 */
                    /* catch() { ... } // from try @ 00bb4948 with catch @ 00bbabb8 */
                    /* catch() { ... } // from try @ 00bb4588 with catch @ 00bbabbc */
  __emutls_get_address(&DAT_00c248a8);
                    /* catch() { ... } // from try @ 00bb9f14 with catch @ 00bbabcc */
                    /* catch() { ... } // from try @ 00bb35b4 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb3790 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb3b20 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb3f40 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb432c with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb470c with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb4acc with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb4eac with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb528c with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb53ec with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb5644 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb5a04 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb5dc4 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb6184 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb6538 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb68ec with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb6ca0 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb7054 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb7408 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb77b8 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb785c with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb790c with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb79b8 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb7a68 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb7d64 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb7fac with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb86bc with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb8994 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb8b70 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb8c24 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb8d90 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb8e34 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb910c with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb93e4 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb9640 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb99c0 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb9af0 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb9fa0 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bba3fc with catch @ 00bbabd0 */
  return;
}

~~~
