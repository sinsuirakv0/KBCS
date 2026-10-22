# 00bdebc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdebc0.md)

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
  "source_sha256": "4f732ac4053be3eb6016800ef53491d3807ccecd62ca8f34b61cad3c14cbc755",
  "source_text_sha256": "4f732ac4053be3eb6016800ef53491d3807ccecd62ca8f34b61cad3c14cbc755"
}
~~~
## 呼び出し元

- [00afc2ac](../00afc/00afc2ac.md)
- [00afc300](../00afc/00afc300.md)

## 呼び出し先

- [010a55e0](../010a5/010a55e0.md)

## 疑似コード 1/1 / UTF-8 212 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int sem_post(sem_t *__sem)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_sem_post_00c1de18)((int)__sem);
  return iVar1;
}

~~~
