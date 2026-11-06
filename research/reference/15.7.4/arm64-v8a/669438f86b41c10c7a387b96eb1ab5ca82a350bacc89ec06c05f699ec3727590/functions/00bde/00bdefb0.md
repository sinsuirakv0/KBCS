# 00bdefb0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00bdefb0",
  "name": "<EXTERNAL>::strcpy",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "07839c24d0b53c82d00ecc00588220aa67473be43d17a8dea4df0d85cc680388",
  "source_text_sha256": "07839c24d0b53c82d00ecc00588220aa67473be43d17a8dea4df0d85cc680388"
}
~~~

## 呼び出し元

- [00b02ec0](../00b02/00b02ec0.md)

## 呼び出し先

- [010a5608](../010a5/010a5608.md)

## 疑似コード / UTF-8 214 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

char * strcpy(char *__dest,char *__src)

{
  char *pcVar1;
  
  pcVar1 = (char *)(*(code *)PTR_strcpy_00c1e090)();
  return pcVar1;
}

~~~
