# 007ffedc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "007ffedc",
  "name": "FUN_007ffedc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5d877520a858ce47219ab375c9754a4aa8fd38cc8fba3a4e5e4cdd6039194ef8",
  "source_text_sha256": "5d877520a858ce47219ab375c9754a4aa8fd38cc8fba3a4e5e4cdd6039194ef8"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 284 bytes

~~~c

long FUN_007ffedc(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) !=
      "ZZN13MyApplication13loadEnemyListEbENK3$_0clEP9NewButton20NewButtonChangeStateEUlP9NewDialog20NewDialogChangeStateiE_"
     ) {
    param_1 = 0;
  }
  return param_1;
}

~~~
