# 00bdeee0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdeee0.md)

## 関数情報

~~~json
{
  "address": "00bdeee0",
  "name": "<EXTERNAL>::pthread_mutexattr_destroy",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "51da251e73b5da5cb8547528a5f4e7cfe9ba67b123a102393537822487af8cfc",
  "source_text_sha256": "51da251e73b5da5cb8547528a5f4e7cfe9ba67b123a102393537822487af8cfc"
}
~~~
## 呼び出し元

- [00b052c8](../00b05/00b052c8.md)
- [00b7d228](../00b7d/00b7d228.md)

## 呼び出し先

- [010a5618](../010a5/010a5618.md)

## 疑似コード 1/1 / UTF-8 262 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int pthread_mutexattr_destroy(pthread_mutexattr_t *__attr)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_pthread_mutexattr_destroy_00c1dfa8)((int)__attr);
  return iVar1;
}

~~~
