# 00bbaba0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00bbacac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbacac.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00bbaba0",
  "name": "<EXTERNAL>::free",
  "size": 8,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ba3e95dc159abd55cac64525c1826dca67f95f81e233ebaf03b306948f419a1c",
  "source_text_sha256": "ba3e95dc159abd55cac64525c1826dca67f95f81e233ebaf03b306948f419a1c"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb710](../00bdb/00bdb710.md)

## 疑似コード / UTF-8 220 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void free(void *__ptr)

{
                    /* catch() { ... } // from try @ 00bb6000 with catch @ 00bbaba4 */
  free(__ptr);
  return;
}

~~~
