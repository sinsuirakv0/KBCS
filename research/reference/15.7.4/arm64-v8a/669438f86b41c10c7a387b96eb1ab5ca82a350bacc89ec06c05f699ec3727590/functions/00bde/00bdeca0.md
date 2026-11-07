# 00bdeca0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00bdeba0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeba0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00bdeca0",
  "name": "<EXTERNAL>::sem_destroy",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2213a170358708f11df441da0611a231f1eff5ce789c1e48a0947e44b29a4e79",
  "source_text_sha256": "2213a170358708f11df441da0611a231f1eff5ce789c1e48a0947e44b29a4e79"
}
~~~

## 呼び出し元

- [00afbc70](../00afb/00afbc70.md)

## 呼び出し先

- [010a55d0](../010a5/010a55d0.md)

## 疑似コード / UTF-8 206 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int sem_destroy(sem_t *__sem)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_sem_destroy_00c1df08)((int)__sem);
  return iVar1;
}

~~~
