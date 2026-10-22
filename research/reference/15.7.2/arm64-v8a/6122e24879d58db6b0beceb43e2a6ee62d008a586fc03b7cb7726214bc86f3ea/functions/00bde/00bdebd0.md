# 00bdebd0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdebd0.md)

## 関数情報

~~~json
{
  "address": "00bdebd0",
  "name": "<EXTERNAL>::sem_wait",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6490961c11d9fab57a4ecf2f5d40ed319aa7bd80def94982cd97b6876f07ada5",
  "source_text_sha256": "6490961c11d9fab57a4ecf2f5d40ed319aa7bd80def94982cd97b6876f07ada5"
}
~~~
## 呼び出し元

- [00afbb64](../00afb/00afbb64.md)

## 呼び出し先

- [010a55e8](../010a5/010a55e8.md)

## 疑似コード 1/1 / UTF-8 212 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int sem_wait(sem_t *__sem)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_sem_wait_00c1de20)((int)__sem);
  return iVar1;
}

~~~
