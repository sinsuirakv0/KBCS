# 00bd4eec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bd4eec",
  "name": "_ZdaPvRKSt9nothrow_t",
  "size": 8,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e2876ab7b631af70d6c85e618aa2bec825a629fcb334ffa102f0e709dd2c2424",
  "source_text_sha256": "e2876ab7b631af70d6c85e618aa2bec825a629fcb334ffa102f0e709dd2c2424"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdef40](../00bde/00bdef40.md)

## 疑似コード / UTF-8 151 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void _ZdaPvRKSt9nothrow_t(void *__ptr)

{
  _ZdaPv(__ptr);
  return;
}

~~~
