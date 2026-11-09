# 00aeeacc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00aeeacc",
  "name": "_ZdlPv",
  "size": 4,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "050de354a304d20d89565178e1d92eee41fcba688f5779bbf9e31257ad5390bd",
  "source_text_sha256": "050de354a304d20d89565178e1d92eee41fcba688f5779bbf9e31257ad5390bd"
}
~~~

## 呼び出し元

- [00ad075c](../00ad0/00ad075c.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 243 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void _ZdlPv(void *__ptr)

{
                    /* catch() { ... } // from try @ 00aee834 with catch @ 00aeeacc */
  (*(code *)PTR__ZdlPv_00c9bb18)();
  return;
}

~~~
