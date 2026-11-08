# 00bd4edc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bd4edc",
  "name": "_ZdlPvm",
  "size": 8,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6ee23e25e11c22a68d0bed0484bd491af8b12fd397235adcb58dbfe335a9dcda",
  "source_text_sha256": "6ee23e25e11c22a68d0bed0484bd491af8b12fd397235adcb58dbfe335a9dcda"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)

## 疑似コード / UTF-8 138 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void _ZdlPvm(void *__ptr)

{
  _ZdlPv(__ptr);
  return;
}

~~~
