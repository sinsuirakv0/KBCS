# 00bdebd0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

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
  "source_sha256": "dc6ecfab8a150ea8403b1c95f9f2ec8af2c0d2956dd4a328750c82b6974c9757",
  "source_text_sha256": "dc6ecfab8a150ea8403b1c95f9f2ec8af2c0d2956dd4a328750c82b6974c9757"
}
~~~

## 呼び出し元

- [00afbb64](../00afb/00afbb64.md)

## 呼び出し先

- [010a55e8](../010a5/010a55e8.md)

## 疑似コード / UTF-8 200 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int sem_wait(sem_t *__sem)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_sem_wait_00c1de20)((int)__sem);
  return iVar1;
}

~~~
