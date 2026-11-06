# 00bddae0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00bddae0.md)

## 関数情報

~~~json
{
  "address": "00bddae0",
  "name": "<EXTERNAL>::atoi",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "501d8539eefe3e735eabf2255a9ffc5fb9e84ac9e10e75bd38157f3546ca59cf",
  "source_text_sha256": "501d8539eefe3e735eabf2255a9ffc5fb9e84ac9e10e75bd38157f3546ca59cf"
}
~~~
## 呼び出し元

- [007e5fa4](../007e5/007e5fa4.md)
- [00b12820](../00b12/00b12820.md)
- [00b17160](../00b17/00b17160.md)
- [00b18d1c](../00b18/00b18d1c.md)
- [00b195a8](../00b19/00b195a8.md)
- [00b218b0](../00b21/00b218b0.md)
- [00b22320](../00b22/00b22320.md)

## 呼び出し先

- [010a5560](../010a5/010a5560.md)

## 疑似コード 1/1 / UTF-8 193 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int atoi(char *__nptr)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_atoi_00c1d628)((int)__nptr);
  return iVar1;
}

~~~
