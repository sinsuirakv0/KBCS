# 00bdecb0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00bdecb0.md)

## 関数情報

~~~json
{
  "address": "00bdecb0",
  "name": "<EXTERNAL>::sem_init",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "510a183291f3856358637a3cf111a12290c4017b3f4271c075e8bcf884499c07",
  "source_text_sha256": "510a183291f3856358637a3cf111a12290c4017b3f4271c075e8bcf884499c07"
}
~~~
## 呼び出し元

- [00afbc70](../00afb/00afbc70.md)

## 呼び出し先

- [010a55d8](../010a5/010a55d8.md)

## 疑似コード 1/1 / UTF-8 245 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int sem_init(sem_t *__sem,int __pshared,uint __value)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_sem_init_00c1df10)((int)__sem,__pshared,__value);
  return iVar1;
}

~~~
