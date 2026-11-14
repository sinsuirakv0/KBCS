# 00aeedf4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00aeedf4",
  "name": "FUN_00aeedf4",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7514b171198451ee6b2dbeda461698b971f738a004faf7be3f6c1ea6de445aae",
  "source_text_sha256": "7514b171198451ee6b2dbeda461698b971f738a004faf7be3f6c1ea6de445aae"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 197 bytes

~~~c

long FUN_00aeedf4(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) != "ZN13MyApplication16UnitAdoptioninitEvE3$_3") {
    param_1 = 0;
  }
  return param_1;
}

~~~
