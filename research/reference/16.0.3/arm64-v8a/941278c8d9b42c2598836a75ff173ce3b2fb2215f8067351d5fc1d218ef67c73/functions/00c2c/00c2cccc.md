# 00c2cccc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00c2cccc",
  "name": "_ZNKSt6__ndk120__codecvt_utf8_utf16IDsE9do_lengthER9mbstate_tPKcS5_m",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "83261b419ffbed6ea324e6d5d185f288a5265a4d6bd6e5b70d3d1e7ab1bc317d",
  "source_text_sha256": "83261b419ffbed6ea324e6d5d185f288a5265a4d6bd6e5b70d3d1e7ab1bc317d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c2a308](../00c2a/00c2a308.md)

## 疑似コード / UTF-8 334 bytes

~~~c

void _ZNKSt6__ndk120__codecvt_utf8_utf16IDsE9do_lengthER9mbstate_tPKcS5_m
               (long param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 param_5)

{
  FUN_00c2a308(param_3,param_4,param_5,*(undefined8 *)(param_1 + 0x10),
               *(undefined4 *)(param_1 + 0x18));
  return;
}

~~~
