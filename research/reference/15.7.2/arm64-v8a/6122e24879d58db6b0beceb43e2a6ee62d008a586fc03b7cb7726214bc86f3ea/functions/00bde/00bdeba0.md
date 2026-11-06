# 00bdeba0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00bdeba0",
  "name": "<EXTERNAL>::sem_destroy",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b863ec7bf4da1f413df9350c8f8665c95ede46157819314ad89688772bd1879c",
  "source_text_sha256": "b863ec7bf4da1f413df9350c8f8665c95ede46157819314ad89688772bd1879c"
}
~~~

## 呼び出し元

- [00afbb64](../00afb/00afbb64.md)

## 呼び出し先

- [010a55d0](../010a5/010a55d0.md)

## 疑似コード / UTF-8 206 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int sem_destroy(sem_t *__sem)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_sem_destroy_00c1de08)((int)__sem);
  return iVar1;
}

~~~
