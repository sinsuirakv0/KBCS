# 00bc2dcc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bc2dcc",
  "name": "FUN_00bc2dcc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fecf6a93aeac42f2d0dcb3e0722320fe23987e2639263f38087af2c44d1d1da5",
  "source_text_sha256": "fecf6a93aeac42f2d0dcb3e0722320fe23987e2639263f38087af2c44d1d1da5"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 264 bytes

~~~c

void FUN_00bc2dcc(long param_1)

{
  if ((*(byte *)(param_1 + 0x20) & 1) == 0) {
    *(undefined1 *)(param_1 + 0x20) = 1;
    (**(code **)(**(long **)(param_1 + 0x18) + 0x18))(*(long **)(param_1 + 0x18));
    *(undefined1 *)(param_1 + 0x20) = 0;
  }
  return;
}

~~~
