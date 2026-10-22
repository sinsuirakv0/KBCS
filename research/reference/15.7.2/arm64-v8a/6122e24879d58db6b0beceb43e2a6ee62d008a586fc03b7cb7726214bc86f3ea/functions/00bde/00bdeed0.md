# 00bdeed0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdeed0.md)

## 関数情報

~~~json
{
  "address": "00bdeed0",
  "name": "<EXTERNAL>::pthread_mutex_init",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "321fd9b5cac3af7ba51f385e1286bdcf6d2b4e720a359afa83b04adf347c11f2",
  "source_text_sha256": "321fd9b5cac3af7ba51f385e1286bdcf6d2b4e720a359afa83b04adf347c11f2"
}
~~~
## 呼び出し元

- [00b052c8](../00b05/00b052c8.md)
- [00b7d228](../00b7d/00b7d228.md)

## 呼び出し先

- [010a5610](../010a5/010a5610.md)

## 疑似コード 1/1 / UTF-8 279 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int pthread_mutex_init(pthread_mutex_t *__mutex,pthread_mutexattr_t *__mutexattr)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_pthread_mutex_init_00c1dfa0)((int)__mutex);
  return iVar1;
}

~~~
