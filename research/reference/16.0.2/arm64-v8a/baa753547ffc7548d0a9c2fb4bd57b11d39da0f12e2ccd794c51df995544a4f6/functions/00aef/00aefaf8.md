# 00aefaf8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00aefaf8",
  "name": "FUN_00aefaf8",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c4c5d147a6312966c9267d5e3673302d9467332eecb03a431ac76aff564fbbec",
  "source_text_sha256": "c4c5d147a6312966c9267d5e3673302d9467332eecb03a431ac76aff564fbbec"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 264 bytes

~~~c

long FUN_00aefaf8(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) !=
      "ZZN13MyApplication16UnitAdoptioninitEvENK3$_5clEP9NewButton20NewButtonChangeStateEUlP9NewDialogE_"
     ) {
    param_1 = 0;
  }
  return param_1;
}

~~~
