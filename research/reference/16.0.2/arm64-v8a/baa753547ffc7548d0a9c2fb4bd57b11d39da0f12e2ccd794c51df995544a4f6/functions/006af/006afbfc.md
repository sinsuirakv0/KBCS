# 006afbfc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "006afbfc",
  "name": "FUN_006afbfc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7f14a4a27eb5f2b2d55acf157eccd97c30ce79b907dfd3155759b7b76ebef5cf",
  "source_text_sha256": "7f14a4a27eb5f2b2d55acf157eccd97c30ce79b907dfd3155759b7b76ebef5cf"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 184 bytes

~~~c

long FUN_006afbfc(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) != "ZN12EvolveWindow4openEibE3$_0") {
    param_1 = 0;
  }
  return param_1;
}

~~~
