# 007feeec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "007feeec",
  "name": "FUN_007feeec",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a0260f4b6b5c41e61ef793e15d4ac6b2e964beb4c5b5e517911fc30ae1a536f2",
  "source_text_sha256": "a0260f4b6b5c41e61ef793e15d4ac6b2e964beb4c5b5e517911fc30ae1a536f2"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 287 bytes

~~~c

long FUN_007feeec(long param_1,long param_2)

{
  param_1 = param_1 + 8;
                    /* try { // try from 007fef00 to 008fef1b has its CatchHandler @ 007ff000 */
  if (*(char **)(param_2 + 8) != "ZN13MyApplication9MapUpdateEvE4$_69") {
    param_1 = 0;
  }
  return param_1;
}

~~~
