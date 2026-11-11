# 00aed5bc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00aed5bc",
  "name": "FUN_00aed5bc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1fb77b1b64edd5a1306dfcf492891afc1f12eed05e6cf5b23338b1d2767fdf6d",
  "source_text_sha256": "1fb77b1b64edd5a1306dfcf492891afc1f12eed05e6cf5b23338b1d2767fdf6d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 197 bytes

~~~c

long FUN_00aed5bc(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) != "ZN13MyApplication16UnitAdoptioninitEvE3$_0") {
    param_1 = 0;
  }
  return param_1;
}

~~~
