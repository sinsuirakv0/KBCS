# 00aefff0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00aefff0",
  "name": "FUN_00aefff0",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "58d43225d725f6c3d6e2c508d76b2010cc50c933f0bab9638c986dfc74ef04f1",
  "source_text_sha256": "58d43225d725f6c3d6e2c508d76b2010cc50c933f0bab9638c986dfc74ef04f1"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 356 bytes

~~~c

long FUN_00aefff0(long param_1,long param_2)

{
                    /* try { // try from 00aefff0 to 00bf011b has its CatchHandler @ 00aefe3c */
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) !=
      "ZZN13MyApplication16UnitAdoptioninitEvENK3$_5clEP9NewButton20NewButtonChangeStateEUlS2_S3_E_"
     ) {
    param_1 = 0;
  }
  return param_1;
}

~~~
