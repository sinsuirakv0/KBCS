# 00af0eac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00af0eac",
  "name": "_ZdlPv",
  "size": 4,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "581af68db4fb4f3584fa721cd4857b87bee003b569c87f194078b7d61ba03aa0",
  "source_text_sha256": "581af68db4fb4f3584fa721cd4857b87bee003b569c87f194078b7d61ba03aa0"
}
~~~

## 呼び出し元

- [00ad6d50](../00ad6/00ad6d50.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 243 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void _ZdlPv(void *__ptr)

{
                    /* catch() { ... } // from try @ 00af1004 with catch @ 00af0eac */
  (*(code *)PTR__ZdlPv_00c9bb18)();
  return;
}

~~~
