# 007ffdbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "007ffdbc",
  "name": "FUN_007ffdbc",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2cf6f922c85739d71783c64bb8d583b46fac61aea83d31f25f6e2ab93d39a777",
  "source_text_sha256": "2cf6f922c85739d71783c64bb8d583b46fac61aea83d31f25f6e2ab93d39a777"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [008b9134](../008b9/008b9134.md)

## 疑似コード / UTF-8 155 bytes

~~~c

void FUN_007ffdbc(undefined8 param_1,undefined8 *param_2,int *param_3)

{
  if (*param_3 == 2) {
    FUN_008b9134(*param_2);
    return;
  }
  return;
}

~~~
