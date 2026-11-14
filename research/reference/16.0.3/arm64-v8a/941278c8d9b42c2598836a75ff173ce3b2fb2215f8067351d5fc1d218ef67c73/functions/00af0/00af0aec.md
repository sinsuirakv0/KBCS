# 00af0aec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00af0aec",
  "name": "FUN_00af0aec",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1b9a93d68fdbf4fa6140f94aefbfd891ae66eff9d45e64260df54d919e926a23",
  "source_text_sha256": "1b9a93d68fdbf4fa6140f94aefbfd891ae66eff9d45e64260df54d919e926a23"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 264 bytes

~~~c

long FUN_00af0aec(long param_1,long param_2)

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
