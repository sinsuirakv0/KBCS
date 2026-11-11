# 00aed6fc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00aed6fc",
  "name": "FUN_00aed6fc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3d0a335e8ef9105bd1e63516588af611b3e39927ced216a076ecf83f3c3588ee",
  "source_text_sha256": "3d0a335e8ef9105bd1e63516588af611b3e39927ced216a076ecf83f3c3588ee"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 197 bytes

~~~c

long FUN_00aed6fc(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) != "ZN13MyApplication16UnitAdoptioninitEvE3$_1") {
    param_1 = 0;
  }
  return param_1;
}

~~~
