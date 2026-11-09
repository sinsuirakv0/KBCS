# 00aed4ac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00aed4ac",
  "name": "FUN_00aed4ac",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8cb80034ed9d87ba333556dfdaf0b5421919e759005c8071c654d1572c16ba71",
  "source_text_sha256": "8cb80034ed9d87ba333556dfdaf0b5421919e759005c8071c654d1572c16ba71"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 294 bytes

~~~c

long FUN_00aed4ac(long param_1,long param_2)

{
  param_1 = param_1 + 8;
                    /* try { // try from 00aed4c0 to 00bed4cb has its CatchHandler @ 00aed924 */
  if (*(char **)(param_2 + 8) != "ZN13MyApplication16UnitAdoptioninitEvE3$_2") {
    param_1 = 0;
  }
  return param_1;
}

~~~
