# 00bdeba0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdeba0.md)

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
  "source_sha256": "92779da8c891e9fa262f66b02315012bba8b3f2c803071a0acda86547865fb9f",
  "source_text_sha256": "92779da8c891e9fa262f66b02315012bba8b3f2c803071a0acda86547865fb9f"
}
~~~
## 呼び出し元

- [00afbb64](../00afb/00afbb64.md)

## 呼び出し先

- [010a55d0](../010a5/010a55d0.md)

## 疑似コード 1/1 / UTF-8 218 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int sem_destroy(sem_t *__sem)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_sem_destroy_00c1de08)((int)__sem);
  return iVar1;
}

~~~
