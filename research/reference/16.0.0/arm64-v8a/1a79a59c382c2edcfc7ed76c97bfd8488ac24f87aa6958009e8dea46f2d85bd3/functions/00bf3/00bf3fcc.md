# 00bf3fcc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bf3fcc",
  "name": "FUN_00bf3fcc",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fc0a66bb4e5c7940a94dc44d63c144f2622f62b16de045a618ecc2d5e9667bd9",
  "source_text_sha256": "fc0a66bb4e5c7940a94dc44d63c144f2622f62b16de045a618ecc2d5e9667bd9"
}
~~~

## 呼び出し元

- [00bf3fc4](../00bf3/00bf3fc4.md)

## 呼び出し先

- [00bf2f78](../00bf2/00bf2f78.md)
- [00c5dc00](../00c5d/00c5dc00.md)

## 疑似コード / UTF-8 157 bytes

~~~c

void FUN_00bf3fcc(undefined8 param_1,wchar_t *param_2)

{
  size_t sVar1;
  
  sVar1 = wcslen(param_2);
  FUN_00bf2f78(param_1,param_2,sVar1);
  return;
}

~~~
