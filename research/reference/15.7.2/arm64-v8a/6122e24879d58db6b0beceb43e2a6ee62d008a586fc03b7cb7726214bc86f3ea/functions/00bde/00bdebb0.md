# 00bdebb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

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
  "source_sha256": "6143c32a165334363f60c97fa7bcae665bf3718aa816100988f12f196f66aa66",
  "source_text_sha256": "6143c32a165334363f60c97fa7bcae665bf3718aa816100988f12f196f66aa66"
}
~~~

## 呼び出し元

- [00afbb64](../00afb/00afbb64.md)

## 呼び出し先

- [010a55d8](../010a5/010a55d8.md)

## 疑似コード / UTF-8 245 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int sem_init(sem_t *__sem,int __pshared,uint __value)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_sem_init_00c1de10)((int)__sem,__pshared,__value);
  return iVar1;
}

~~~
