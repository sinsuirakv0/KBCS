# 00baeeec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00baeeec",
  "name": "_ZNKSt6__ndk120__codecvt_utf8_utf16IDiE13do_max_lengthEv",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "42a48ba87cda711be1de7615e4191bc32e3b7e4b76e4f16526a7b324b3ecfeff",
  "source_text_sha256": "42a48ba87cda711be1de7615e4191bc32e3b7e4b76e4f16526a7b324b3ecfeff"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 206 bytes

~~~c

undefined4 _ZNKSt6__ndk120__codecvt_utf8_utf16IDiE13do_max_lengthEv(long param_1)

{
  undefined4 uVar1;
  
  uVar1 = 4;
  if ((*(byte *)(param_1 + 0x18) & 4) != 0) {
    uVar1 = 7;
  }
  return uVar1;
}

~~~
