# 00bdefd0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00bdeed0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeed0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00bdefd0",
  "name": "<EXTERNAL>::pthread_mutex_init",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7c1f39b721aebd8f13284d17f4769fa6d1fa5a610c3a6e6fc85bf19e627913cf",
  "source_text_sha256": "7c1f39b721aebd8f13284d17f4769fa6d1fa5a610c3a6e6fc85bf19e627913cf"
}
~~~

## 呼び出し元

- [00b053d4](../00b05/00b053d4.md)
- [00b7d334](../00b7d/00b7d334.md)

## 呼び出し先

- [010a5610](../010a5/010a5610.md)

## 疑似コード / UTF-8 267 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int pthread_mutex_init(pthread_mutex_t *__mutex,pthread_mutexattr_t *__mutexattr)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_pthread_mutex_init_00c1e0a0)((int)__mutex);
  return iVar1;
}

~~~
