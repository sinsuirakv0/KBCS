# 00aeeca0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00aeeca0",
  "name": "FUN_00aeeca0",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "04aa4e547abdd357dd8a4df46b131e094d9883f40d86b10402ce5ca6e4c58626",
  "source_text_sha256": "04aa4e547abdd357dd8a4df46b131e094d9883f40d86b10402ce5ca6e4c58626"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 248 bytes

~~~c

long FUN_00aeeca0(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) !=
      "ZZN13MyApplication16UnitAdoptioninitEvENK3$_4clEP9NewButton20NewButtonChangeStateEUlvE_") {
    param_1 = 0;
  }
  return param_1;
}

~~~
