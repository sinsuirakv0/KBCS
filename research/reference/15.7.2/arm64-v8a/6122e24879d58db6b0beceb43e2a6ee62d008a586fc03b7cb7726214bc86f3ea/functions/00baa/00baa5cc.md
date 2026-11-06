# 00baa5cc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00baa5cc",
  "name": "_ZNKSt6__ndk112ctype_bynameIcE10do_tolowerEc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6abe2d79e77477c07583e790e8d814fea40c15477b5500538b8c384a327298c6",
  "source_text_sha256": "6abe2d79e77477c07583e790e8d814fea40c15477b5500538b8c384a327298c6"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 214 bytes

~~~c

uint _ZNKSt6__ndk112ctype_bynameIcE10do_tolowerEc(undefined8 param_1,uint param_2)

{
  uint uVar1;
  
  uVar1 = param_2 | 0x20;
  if (0x19 < (param_2 & 0xff) - 0x41) {
    uVar1 = param_2;
  }
  return uVar1;
}

~~~
