# 00afb6ac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00afb6ac",
  "name": "_ZN8firebase6Logger11SetLogLevelENS_8LogLevelE",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aaf0b7208af50a56cf3cd9deb525559ff08931c2b98bb336a944f97d21ac2651",
  "source_text_sha256": "aaf0b7208af50a56cf3cd9deb525559ff08931c2b98bb336a944f97d21ac2651"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 147 bytes

~~~c

void _ZN8firebase6Logger11SetLogLevelENS_8LogLevelE(long param_1,undefined4 param_2)

{
  *(undefined4 *)(param_1 + 0x10) = param_2;
  return;
}

~~~
