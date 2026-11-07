# 00bbacac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00bbaba0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbaba0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00bbacac",
  "name": "<EXTERNAL>::free",
  "size": 8,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b8fd70a8ac556fc9b873b3c2800c5037ab7af09085d945013b493eba6b8a34b9",
  "source_text_sha256": "b8fd70a8ac556fc9b873b3c2800c5037ab7af09085d945013b493eba6b8a34b9"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb810](../00bdb/00bdb810.md)

## 疑似コード / UTF-8 220 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void free(void *__ptr)

{
                    /* catch() { ... } // from try @ 00bb610c with catch @ 00bbacb0 */
  free(__ptr);
  return;
}

~~~
