# 007cbdac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "007cbdac",
  "name": "FUN_007cbdac",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7ab2accf7eb7fdeea749ff2dbbb47c62c103a48a3a729e7b54c25075f43471d7",
  "source_text_sha256": "7ab2accf7eb7fdeea749ff2dbbb47c62c103a48a3a729e7b54c25075f43471d7"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)

## 疑似コード / UTF-8 329 bytes

~~~c

void FUN_007cbdac(undefined8 *param_1)

{
  void *__ptr;
  
  __ptr = (void *)param_1[2];
  *param_1 = &PTR_FUN_00bffff8;
  if (__ptr != (void *)0x0) {
    param_1[3] = __ptr;
    _ZdlPv(__ptr);
  }
                    /* try { // try from 007cbde8 to 008cbe0f has its CatchHandler @ 007cde44 */
  _ZdlPv(param_1);
  return;
}

~~~
