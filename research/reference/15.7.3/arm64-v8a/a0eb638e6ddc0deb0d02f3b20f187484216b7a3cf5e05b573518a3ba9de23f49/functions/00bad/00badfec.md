# 00badfec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00badfec",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IDsLb0EE13do_max_lengthEv",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b3af60aa7eaada101652b4de89987cd2a29babc64321954abb8ab805970a01d9",
  "source_text_sha256": "b3af60aa7eaada101652b4de89987cd2a29babc64321954abb8ab805970a01d9"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 205 bytes

~~~c

undefined4 _ZNKSt6__ndk115__codecvt_utf16IDsLb0EE13do_max_lengthEv(long param_1)

{
  undefined4 uVar1;
  
  uVar1 = 2;
  if ((*(byte *)(param_1 + 0x18) & 4) != 0) {
    uVar1 = 4;
  }
  return uVar1;
}

~~~
