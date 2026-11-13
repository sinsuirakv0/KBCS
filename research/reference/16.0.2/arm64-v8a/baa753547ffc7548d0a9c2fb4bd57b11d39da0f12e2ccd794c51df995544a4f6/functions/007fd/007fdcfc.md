# 007fdcfc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "007fdcfc",
  "name": "FUN_007fdcfc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1aa77734ce3dc2752d83916513b2db6d24c87e797f4383ba42892df4126e80af",
  "source_text_sha256": "1aa77734ce3dc2752d83916513b2db6d24c87e797f4383ba42892df4126e80af"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 267 bytes

~~~c

long FUN_007fdcfc(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) !=
      "ZZZN13MyApplication9MapUpdateEvENK4$_67clEP9NewDialog20NewDialogChangeStateiENKUlbE_clEbEUlS2_S3_iE_"
     ) {
    param_1 = 0;
  }
  return param_1;
}

~~~
