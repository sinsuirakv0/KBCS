# 005afdbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `005afdbc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afdbc.md)
<!-- /kbcs-version-next -->

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
  "source_sha256": "1af74dfae23699aba18ef616db4a9ee78b98eabc9c2e598ba18778b9a799fd72",
  "source_text_sha256": "1af74dfae23699aba18ef616db4a9ee78b98eabc9c2e598ba18778b9a799fd72"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)

## 疑似コード / UTF-8 273 bytes

~~~c

void FUN_005afdbc(long *param_1)

{
  long *plVar1;
  
  plVar1 = (long *)param_1[1];
  *param_1 = (long)(PTR__ZTVNSt6__ndk116__owns_one_stateIcEE_00c1b4b0 + 0x10);
  if (plVar1 != (long *)0x0) {
    (**(code **)(*plVar1 + 8))(plVar1);
  }
  _ZdlPv(param_1);
  return;
}

~~~
