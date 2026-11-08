# 00badcdc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00badcdc",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IwLb1EE9do_lengthER9mbstate_tPKcS5_m",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "62a6c645bd8fbb15be1f1586487dcf33a68d3e4b6085c3a366532171f3f4515a",
  "source_text_sha256": "62a6c645bd8fbb15be1f1586487dcf33a68d3e4b6085c3a366532171f3f4515a"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00badcfc](../00bad/00badcfc.md)

## 疑似コード / UTF-8 332 bytes

~~~c

void _ZNKSt6__ndk115__codecvt_utf16IwLb1EE9do_lengthER9mbstate_tPKcS5_m
               (long param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 param_5)

{
  FUN_00badcfc(param_3,param_4,param_5,*(undefined8 *)(param_1 + 0x18),
               *(undefined4 *)(param_1 + 0x20));
  return;
}

~~~
