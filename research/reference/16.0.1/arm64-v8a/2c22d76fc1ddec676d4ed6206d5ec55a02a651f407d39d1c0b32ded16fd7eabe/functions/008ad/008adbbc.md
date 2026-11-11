# 008adbbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "008adbbc",
  "name": "FUN_008adbbc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aaa97ef6a449ae44509417b41d1440f2f7ed747785275dd0498449ed3aa2818b",
  "source_text_sha256": "aaa97ef6a449ae44509417b41d1440f2f7ed747785275dd0498449ed3aa2818b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 287 bytes

~~~c

long FUN_008adbbc(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) !=
      "ZN17MyUtilityListener22nekokanBrowserFunctionERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEE3$_1"
     ) {
    param_1 = 0;
  }
  return param_1;
}

~~~
