# 00bbab7c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbab7c.md)

## 関数情報

~~~json
{
  "address": "00bbab7c",
  "name": "std::set_new_handler",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f4560864020222f055a09a3c9e6d57f0dd56b6bd168084de40c5107814be294c",
  "source_text_sha256": "f4560864020222f055a09a3c9e6d57f0dd56b6bd168084de40c5107814be294c"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bd6cd0](../00bd6/00bd6cd0.md)

## 疑似コード 1/1 / UTF-8 952 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */
/* std::set_new_handler(void (*)()) */

void std::set_new_handler(_func_void *param_1)

{
                    /* catch() { ... } // from try @ 00bb42a8 with catch @ 00bbab80 */
                    /* catch() { ... } // from try @ 00bb3ebc with catch @ 00bbab84 */
                    /* catch() { ... } // from try @ 00bb3a9c with catch @ 00bbab88 */
                    /* catch() { ... } // from try @ 00bb7634 with catch @ 00bbab8c */
                    /* catch() { ... } // from try @ 00bb7284 with catch @ 00bbab90 */
  FUN_00bd6cd0(param_1,PTR___cxa_new_handler_00c1bf08);
                    /* catch() { ... } // from try @ 00bb6ed0 with catch @ 00bbab94 */
                    /* catch() { ... } // from try @ 00bb6b1c with catch @ 00bbab98 */
                    /* catch() { ... } // from try @ 00bb6768 with catch @ 00bbab9c */
  return;
}

~~~
