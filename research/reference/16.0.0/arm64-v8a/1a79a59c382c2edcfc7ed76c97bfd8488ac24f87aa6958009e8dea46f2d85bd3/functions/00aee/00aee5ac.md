# 00aee5ac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00aee5ac",
  "name": "FUN_00aee5ac",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a21a30abd9d45ed294973aedf9b38ab5d93cd541285839f8cffa5feecbc8bd6f",
  "source_text_sha256": "a21a30abd9d45ed294973aedf9b38ab5d93cd541285839f8cffa5feecbc8bd6f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 311 bytes

~~~c

long FUN_00aee5ac(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) !=
      "ZZZN13MyApplication16UnitAdoptioninitEvENK3$_3clEP9NewButton20NewButtonChangeStateENKUlP9NewDialog20NewDialogChangeStateiE_clES5_S6_iEUlS2_S3_E_"
     ) {
    param_1 = 0;
  }
  return param_1;
}

~~~
