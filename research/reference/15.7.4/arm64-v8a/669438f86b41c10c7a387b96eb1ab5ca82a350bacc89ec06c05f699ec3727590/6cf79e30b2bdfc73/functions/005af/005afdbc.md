# 005afdbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](005afdbc.md)

## 関数情報

~~~json
{
  "address": "005afdbc",
  "name": "FUN_005afdbc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f9534ea9bb0f58e3b25ff44d0596ad1d0e4e8324ee9f9e779a40d81d41b48681",
  "source_text_sha256": "f9534ea9bb0f58e3b25ff44d0596ad1d0e4e8324ee9f9e779a40d81d41b48681"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)

## 疑似コード 1/1 / UTF-8 273 bytes

~~~c

void FUN_005afdbc(long *param_1)

{
  long *plVar1;
  
  plVar1 = (long *)param_1[1];
  *param_1 = (long)(PTR__ZTVNSt6__ndk116__owns_one_stateIcEE_00c1b5b0 + 0x10);
  if (plVar1 != (long *)0x0) {
    (**(code **)(*plVar1 + 8))(plVar1);
  }
  _ZdlPv(param_1);
  return;
}

~~~
