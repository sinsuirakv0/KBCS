# 00bdefe0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00bdeee0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeee0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00bdefe0",
  "name": "<EXTERNAL>::pthread_mutexattr_destroy",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ae8b5842b5a9f1ddb4293020035cad571d220c22d6e2827ebba9772b08dc079d",
  "source_text_sha256": "ae8b5842b5a9f1ddb4293020035cad571d220c22d6e2827ebba9772b08dc079d"
}
~~~

## 呼び出し元

- [00b053d4](../00b05/00b053d4.md)
- [00b7d334](../00b7d/00b7d334.md)

## 呼び出し先

- [010a5618](../010a5/010a5618.md)

## 疑似コード / UTF-8 250 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int pthread_mutexattr_destroy(pthread_mutexattr_t *__attr)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_pthread_mutexattr_destroy_00c1e0a8)((int)__attr);
  return iVar1;
}

~~~
