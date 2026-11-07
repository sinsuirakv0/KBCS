# 00bbab7c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00bbac88`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac88.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00bbab7c",
  "name": "_ZSt15set_new_handlerPFvvE",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f9d651763cedec1950563350dc0815a15185c682364fd85914efd5dd7f9f7a63",
  "source_text_sha256": "f9d651763cedec1950563350dc0815a15185c682364fd85914efd5dd7f9f7a63"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bd6cd0](../00bd6/00bd6cd0.md)

## 疑似コード / UTF-8 821 bytes

~~~c

void _ZSt15set_new_handlerPFvvE(undefined8 param_1)

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
