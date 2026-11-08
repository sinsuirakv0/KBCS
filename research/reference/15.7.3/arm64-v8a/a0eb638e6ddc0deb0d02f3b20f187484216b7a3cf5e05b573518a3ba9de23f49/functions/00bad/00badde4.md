# 00badde4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00badde4",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IwLb1EE13do_max_lengthEv",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c576fe512f5773049e5eb747299a130e78932f72f5526c854a9257f40724ba7c",
  "source_text_sha256": "c576fe512f5773049e5eb747299a130e78932f72f5526c854a9257f40724ba7c"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 204 bytes

~~~c

undefined4 _ZNKSt6__ndk115__codecvt_utf16IwLb1EE13do_max_lengthEv(long param_1)

{
  undefined4 uVar1;
  
  uVar1 = 4;
  if ((*(byte *)(param_1 + 0x20) & 4) != 0) {
    uVar1 = 6;
  }
  return uVar1;
}

~~~
