# 00baafe4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00baafe4",
  "name": "_ZNKSt6__ndk112ctype_bynameIwE10do_tolowerEw",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "28f80e5a3fb3b3f6a405f54888dd37d0634cb68ba9fdb110b4e705e7da43af5f",
  "source_text_sha256": "28f80e5a3fb3b3f6a405f54888dd37d0634cb68ba9fdb110b4e705e7da43af5f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1aa0](../00be1/00be1aa0.md)

## 疑似コード / UTF-8 186 bytes

~~~c

wint_t _ZNKSt6__ndk112ctype_bynameIwE10do_tolowerEw(long param_1,wint_t param_2)

{
  wint_t wVar1;
  
  wVar1 = towlower_l(param_2,*(__locale_t *)(param_1 + 0x10));
  return wVar1;
}

~~~
