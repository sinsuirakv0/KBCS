# 00a9afac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00a9afac",
  "name": "FUN_00a9afac",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fb8b2381eff41e871fd35714a7925815a0a15ac865598adf004a0a5fdaf00510",
  "source_text_sha256": "fb8b2381eff41e871fd35714a7925815a0a15ac865598adf004a0a5fdaf00510"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 201 bytes

~~~c

long FUN_00a9afac(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) != "ZN13MyApplication20TitleUpdateLabyrinthEvE3$_0") {
    param_1 = 0;
  }
  return param_1;
}

~~~
