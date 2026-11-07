# 00bdeee0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00bdefe0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefe0.md)
<!-- /kbcs-version-next -->

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
  "source_sha256": "3096491db32c9b1ea026963d03e8a8d14bf5517f6a9bac0b6ec9daa234eaa9e7",
  "source_text_sha256": "3096491db32c9b1ea026963d03e8a8d14bf5517f6a9bac0b6ec9daa234eaa9e7"
}
~~~

## 呼び出し元

- [00b052c8](../00b05/00b052c8.md)
- [00b7d228](../00b7d/00b7d228.md)

## 呼び出し先

- [010a5618](../010a5/010a5618.md)

## 疑似コード / UTF-8 250 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int pthread_mutexattr_destroy(pthread_mutexattr_t *__attr)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_pthread_mutexattr_destroy_00c1dfa8)((int)__attr);
  return iVar1;
}

~~~
