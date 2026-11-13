# 007ffdec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "007ffdec",
  "name": "FUN_007ffdec",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "183d26fc3f1396c840855269d7f02e24eaf7adcaf163032ca9fb8d53d58de55a",
  "source_text_sha256": "183d26fc3f1396c840855269d7f02e24eaf7adcaf163032ca9fb8d53d58de55a"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 469 bytes

~~~c

long FUN_007ffdec(long param_1,long param_2)

{
                    /* catch() { ... } // from try @ 007ff99c with catch @ 007ffdf8
                       catch() { ... } // from try @ 007ffa80 with catch @ 007ffdf8
                       catch() { ... } // from try @ 007ffb24 with catch @ 007ffdf8 */
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) != "ZN13MyApplication33stageSelect_createTreasureGauguUIEvE3$_2") {
    param_1 = 0;
  }
  return param_1;
}

~~~
