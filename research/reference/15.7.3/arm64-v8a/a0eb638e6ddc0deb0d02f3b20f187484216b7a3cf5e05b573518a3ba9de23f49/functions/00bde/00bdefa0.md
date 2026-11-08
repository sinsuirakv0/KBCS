# 00bdefa0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bdefa0",
  "name": "<EXTERNAL>::pthread_mutexattr_init",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1459ae1f0e236c49b4d0e26fb49fc98e9b7da4848dd2ff7798f2a28a6e47af54",
  "source_text_sha256": "1459ae1f0e236c49b4d0e26fb49fc98e9b7da4848dd2ff7798f2a28a6e47af54"
}
~~~

## 呼び出し元

- [00b05390](../00b05/00b05390.md)
- [00b7d2f0](../00b7d/00b7d2f0.md)

## 呼び出し先

- [010a5620](../010a5/010a5620.md)

## 疑似コード / UTF-8 244 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int pthread_mutexattr_init(pthread_mutexattr_t *__attr)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_pthread_mutexattr_init_00c1e060)((int)__attr);
  return iVar1;
}

~~~
