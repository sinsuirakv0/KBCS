# 00bdebb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdebb0.md)

## 関数情報

~~~json
{
  "address": "00bdebb0",
  "name": "<EXTERNAL>::sem_init",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eea1f4591775afd651f15f3fe9d4805e614131bd2d2de57d8146f184d5fa6015",
  "source_text_sha256": "eea1f4591775afd651f15f3fe9d4805e614131bd2d2de57d8146f184d5fa6015"
}
~~~
## 呼び出し元

- [00afbb64](../00afb/00afbb64.md)

## 呼び出し先

- [010a55d8](../010a5/010a55d8.md)

## 疑似コード 1/1 / UTF-8 257 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int sem_init(sem_t *__sem,int __pshared,uint __value)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_sem_init_00c1de10)((int)__sem,__pshared,__value);
  return iVar1;
}

~~~
