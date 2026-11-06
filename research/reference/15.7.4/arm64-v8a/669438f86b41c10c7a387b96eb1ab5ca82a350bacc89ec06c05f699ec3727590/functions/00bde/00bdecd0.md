# 00bdecd0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00bdecd0",
  "name": "<EXTERNAL>::sem_wait",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "17c1c91aa7a1966f81d229c4a99c69923e16e9c2f98e011e8d726f813ea9028d",
  "source_text_sha256": "17c1c91aa7a1966f81d229c4a99c69923e16e9c2f98e011e8d726f813ea9028d"
}
~~~

## 呼び出し元

- [00afbc70](../00afb/00afbc70.md)

## 呼び出し先

- [010a55e8](../010a5/010a55e8.md)

## 疑似コード / UTF-8 200 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int sem_wait(sem_t *__sem)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_sem_wait_00c1df20)((int)__sem);
  return iVar1;
}

~~~
