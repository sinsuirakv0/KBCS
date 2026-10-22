# 00bdeef0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdeef0.md)

## 関数情報

~~~json
{
  "address": "00bdeef0",
  "name": "<EXTERNAL>::pthread_mutexattr_init",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c143fd1608bbe4cfea84d28da5f95fe22ae5b983ad258c073c6ee09ab88b19bc",
  "source_text_sha256": "c143fd1608bbe4cfea84d28da5f95fe22ae5b983ad258c073c6ee09ab88b19bc"
}
~~~
## 呼び出し元

- [00b052c8](../00b05/00b052c8.md)
- [00b7d228](../00b7d/00b7d228.md)

## 呼び出し先

- [010a5620](../010a5/010a5620.md)

## 疑似コード 1/1 / UTF-8 256 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int pthread_mutexattr_init(pthread_mutexattr_t *__attr)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_pthread_mutexattr_init_00c1dfb0)((int)__attr);
  return iVar1;
}

~~~
