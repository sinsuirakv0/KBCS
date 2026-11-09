# 00aeea4c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00aeea4c",
  "name": "FUN_00aeea4c",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "52d56190a7b0d47b894beedddb89f3d08431e4e73622eb1791baaa746905a3e6",
  "source_text_sha256": "52d56190a7b0d47b894beedddb89f3d08431e4e73622eb1791baaa746905a3e6"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 275 bytes

~~~c

long FUN_00aeea4c(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) !=
      "ZZN13MyApplication16UnitAdoptioninitEvENK3$_3clEP9NewButton20NewButtonChangeStateEUlP9NewDialogP9aGraphicsE_"
     ) {
    param_1 = 0;
  }
  return param_1;
}

~~~
