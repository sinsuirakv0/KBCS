# 00af0ecc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00af0ecc",
  "name": "FUN_00af0ecc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d07b6df17fad9e9b8877c7f064a140ca156048b51c4e54513182d9ecb234e0a3",
  "source_text_sha256": "d07b6df17fad9e9b8877c7f064a140ca156048b51c4e54513182d9ecb234e0a3"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 199 bytes

~~~c

long FUN_00af0ecc(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) != "ZN13MyApplication18UnitAdoptionUpdateEvE3$_2") {
    param_1 = 0;
  }
  return param_1;
}

~~~
