# 00aefa5c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00aefa5c",
  "name": "FUN_00aefa5c",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b24897e3b73ff1792f1ddf601a084f03cf706ada442ee0f1e608fa70af632da1",
  "source_text_sha256": "b24897e3b73ff1792f1ddf601a084f03cf706ada442ee0f1e608fa70af632da1"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 264 bytes

~~~c

long FUN_00aefa5c(long param_1,long param_2)

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
