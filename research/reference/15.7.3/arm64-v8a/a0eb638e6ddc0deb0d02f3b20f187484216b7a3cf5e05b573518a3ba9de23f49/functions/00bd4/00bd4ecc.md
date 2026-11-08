# 00bd4ecc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bd4ecc",
  "name": "_ZdlPv",
  "size": 8,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bcd67d1a60fc94360f12ccc2efea0f8e2d22398f91874eedfb07b95c3036d690",
  "source_text_sha256": "bcd67d1a60fc94360f12ccc2efea0f8e2d22398f91874eedfb07b95c3036d690"
}
~~~

## 呼び出し元

- [00bdb010](../00bdb/00bdb010.md)

## 呼び出し先

- [00bdb7c0](../00bdb/00bdb7c0.md)

## 疑似コード / UTF-8 135 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void _ZdlPv(void *__ptr)

{
  free(__ptr);
  return;
}

~~~
