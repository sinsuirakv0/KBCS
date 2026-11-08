# 00bdebc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00bdebc0",
  "name": "<EXTERNAL>::sem_post",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c0b40cdb8de053778cb5916603c90554c22babbe36452958aceb615f481e1187",
  "source_text_sha256": "c0b40cdb8de053778cb5916603c90554c22babbe36452958aceb615f481e1187"
}
~~~

## 呼び出し元

- [00afc2ac](../00afc/00afc2ac.md)
- [00afc300](../00afc/00afc300.md)

## 呼び出し先

- [010a55e0](../010a5/010a55e0.md)

## 疑似コード / UTF-8 200 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int sem_post(sem_t *__sem)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_sem_post_00c1de18)((int)__sem);
  return iVar1;
}

~~~
