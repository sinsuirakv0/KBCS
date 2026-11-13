# 00aef8ec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00aef8ec",
  "name": "FUN_00aef8ec",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c1ac2931b6d313382ddae1afa142e6efe89206e43497b88b9c408dcbdb37aa78",
  "source_text_sha256": "c1ac2931b6d313382ddae1afa142e6efe89206e43497b88b9c408dcbdb37aa78"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 197 bytes

~~~c

long FUN_00aef8ec(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) != "ZN13MyApplication16UnitAdoptioninitEvE3$_5") {
    param_1 = 0;
  }
  return param_1;
}

~~~
