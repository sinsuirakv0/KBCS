# 00bdefb0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bdefb0",
  "name": "<EXTERNAL>::pthread_mutexattr_settype",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "df5ddcade338351fa579962aae2409f3863a3cb69a3b29bd0c37f62335615ab0",
  "source_text_sha256": "df5ddcade338351fa579962aae2409f3863a3cb69a3b29bd0c37f62335615ab0"
}
~~~

## 呼び出し元

- [00b05390](../00b05/00b05390.md)
- [00b7d2f0](../00b7d/00b7d2f0.md)

## 呼び出し先

- [010a5628](../010a5/010a5628.md)

## 疑似コード / UTF-8 268 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int pthread_mutexattr_settype(pthread_mutexattr_t *__attr,int __kind)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_pthread_mutexattr_settype_00c1e068)((int)__attr,__kind);
  return iVar1;
}

~~~
