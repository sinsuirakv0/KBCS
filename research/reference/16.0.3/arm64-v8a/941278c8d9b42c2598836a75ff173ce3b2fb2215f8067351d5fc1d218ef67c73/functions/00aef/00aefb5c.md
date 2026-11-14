# 00aefb5c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00aefb5c",
  "name": "FUN_00aefb5c",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9336c376cdaeeecf21f68ad58f17b779a3769636669b5e5071028d01134af6e7",
  "source_text_sha256": "9336c376cdaeeecf21f68ad58f17b779a3769636669b5e5071028d01134af6e7"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 312 bytes

~~~c

long FUN_00aefb5c(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) !=
      "ZZZN13MyApplication16UnitAdoptioninitEvENK3$_3clEP9NewButton20NewButtonChangeStateENKUlP9NewDialog20NewDialogChangeStateiE_clES5_S6_iEUlS2_S3_E0_"
     ) {
    param_1 = 0;
  }
  return param_1;
}

~~~
