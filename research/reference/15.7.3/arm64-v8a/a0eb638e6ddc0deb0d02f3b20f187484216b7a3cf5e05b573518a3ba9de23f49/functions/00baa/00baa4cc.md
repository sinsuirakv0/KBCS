# 00baa4cc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00baa4cc",
  "name": "_ZNKSt6__ndk112ctype_bynameIcE10do_toupperEc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a596d79d4ad0d3131aa2d854781da41d82b6241e066f296238dae2d505a5f028",
  "source_text_sha256": "a596d79d4ad0d3131aa2d854781da41d82b6241e066f296238dae2d505a5f028"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 214 bytes

~~~c

uint _ZNKSt6__ndk112ctype_bynameIcE10do_toupperEc(undefined8 param_1,uint param_2)

{
  uint uVar1;
  
  uVar1 = param_2 ^ 0x20;
  if (0x19 < (param_2 & 0xff) - 0x61) {
    uVar1 = param_2;
  }
  return uVar1;
}

~~~
