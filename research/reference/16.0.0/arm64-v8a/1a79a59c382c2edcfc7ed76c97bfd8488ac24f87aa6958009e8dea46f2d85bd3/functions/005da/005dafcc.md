# 005dafcc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "005dafcc",
  "name": "FUN_005dafcc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "47bfe4609e6dca840ef34e21ea20c67d681f37b650d660fa3d93e507b7109013",
  "source_text_sha256": "47bfe4609e6dca840ef34e21ea20c67d681f37b650d660fa3d93e507b7109013"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 396 bytes

~~~c

long FUN_005dafcc(long param_1,long param_2)

{
                    /* try { // try from 005dafd0 to 006db053 has its CatchHandler @ 005da668 */
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) !=
      "ZZZN12AwakenWindow4openEiENK3$_0clEP9NewButton20NewButtonChangeStateENKUlP9NewDialog20NewDialogChangeStateiE0_clES5_S6_iEUlS5_S6_iE_"
     ) {
    param_1 = 0;
  }
  return param_1;
}

~~~
