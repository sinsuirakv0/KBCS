# 00ba9bbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00ba9bbc",
  "name": "_ZNKSt6__ndk15ctypeIwE9do_narrowEwc",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "590b8f031181af8f917db223e93be512f41f62e92b2e6ccfb3268efc8be1b5e3",
  "source_text_sha256": "590b8f031181af8f917db223e93be512f41f62e92b2e6ccfb3268efc8be1b5e3"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 163 bytes

~~~c

uint _ZNKSt6__ndk15ctypeIwE9do_narrowEwc(undefined8 param_1,uint param_2,uint param_3)

{
  if (param_2 < 0x80) {
    param_3 = param_2;
  }
  return param_3;
}

~~~
