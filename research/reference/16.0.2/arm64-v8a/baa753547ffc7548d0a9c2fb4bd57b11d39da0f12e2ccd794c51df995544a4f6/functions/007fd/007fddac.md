# 007fddac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "007fddac",
  "name": "FUN_007fddac",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "99b716b5be241d3d7c224233d58a778eb0b88fdc7b70ac13aa0da151a3808c20",
  "source_text_sha256": "99b716b5be241d3d7c224233d58a778eb0b88fdc7b70ac13aa0da151a3808c20"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 268 bytes

~~~c

long FUN_007fddac(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) !=
      "ZZZN13MyApplication9MapUpdateEvENK4$_67clEP9NewDialog20NewDialogChangeStateiENKUlbE_clEbEUlS2_S3_iE0_"
     ) {
    param_1 = 0;
  }
  return param_1;
}

~~~
