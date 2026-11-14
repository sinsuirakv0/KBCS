# 006dabfc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "006dabfc",
  "name": "FUN_006dabfc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5bd8641f282bdb8ef86129e6e5a69453f83418627e4dd51c5f5971bec0e38110",
  "source_text_sha256": "5bd8641f282bdb8ef86129e6e5a69453f83418627e4dd51c5f5971bec0e38110"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 181 bytes

~~~c

long FUN_006dabfc(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) != "ZN10FilterMenu4openEvE3$_8") {
    param_1 = 0;
  }
  return param_1;
}

~~~
