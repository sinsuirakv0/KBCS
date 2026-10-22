# 00bbaba0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbaba0.md)

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
  "source_sha256": "dc17f3b268614c8edcede856d7f130fd09408bc879dc3779d38242ba99fe2447",
  "source_text_sha256": "dc17f3b268614c8edcede856d7f130fd09408bc879dc3779d38242ba99fe2447"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb710](../00bdb/00bdb710.md)

## 疑似コード 1/1 / UTF-8 231 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void free(void *__ptr)

{
                    /* catch() { ... } // from try @ 00bb6000 with catch @ 00bbaba4 */
  free(__ptr);
  return;
}

~~~
