# 00baefe4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00baefe4",
  "name": "_ZNSt6__ndk18numpunctIwEC2Em",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8a9cbf042b9bcd6035f61e0017617699c16fc76875a2775e6593f0b0519c2afb",
  "source_text_sha256": "8a9cbf042b9bcd6035f61e0017617699c16fc76875a2775e6593f0b0519c2afb"
}
~~~

## 呼び出し元

- [00be17d0](../00be1/00be17d0.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 335 bytes

~~~c

void _ZNSt6__ndk18numpunctIwEC2Em(long *param_1,long param_2)

{
  long lVar1;
  undefined *puVar2;
  
  puVar2 = PTR__ZTVNSt6__ndk18numpunctIwEE_00c1bf70;
  lVar1 = DAT_002b2b98;
  param_1[4] = 0;
  param_1[5] = 0;
  param_1[3] = 0;
  param_1[2] = lVar1;
  *param_1 = (long)(puVar2 + 0x10);
  param_1[1] = param_2 + -1;
  return;
}

~~~
