# 00bdeeb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00bdeeb0",
  "name": "<EXTERNAL>::strcpy",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8e8bcabc1f496521e68abd31b98fb13a9166f592e346f4fea5b6dd1dbaf76be6",
  "source_text_sha256": "8e8bcabc1f496521e68abd31b98fb13a9166f592e346f4fea5b6dd1dbaf76be6"
}
~~~

## 呼び出し元

- [00b02db4](../00b02/00b02db4.md)

## 呼び出し先

- [010a5608](../010a5/010a5608.md)

## 疑似コード / UTF-8 214 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

char * strcpy(char *__dest,char *__src)

{
  char *pcVar1;
  
  pcVar1 = (char *)(*(code *)PTR_strcpy_00c1df90)();
  return pcVar1;
}

~~~
