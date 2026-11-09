# 00aefb2c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00aefb2c",
  "name": "FUN_00aefb2c",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "054ab7f1d90526a8a8b431445220863fef3944bad231536b26bfc7110b2ecb16",
  "source_text_sha256": "054ab7f1d90526a8a8b431445220863fef3944bad231536b26bfc7110b2ecb16"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 259 bytes

~~~c

long FUN_00aefb2c(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) !=
      "ZZN13MyApplication16UnitAdoptioninitEvENK3$_5clEP9NewButton20NewButtonChangeStateEUlS2_S3_E_"
     ) {
    param_1 = 0;
  }
  return param_1;
}

~~~
