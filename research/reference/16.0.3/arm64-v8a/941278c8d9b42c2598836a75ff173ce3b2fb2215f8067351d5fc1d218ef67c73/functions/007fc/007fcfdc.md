# 007fcfdc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "007fcfdc",
  "name": "FUN_007fcfdc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cd0434818067c7ee2c48f0eaa0a140f8af4b008ce800d7e12817ed71453dbec9",
  "source_text_sha256": "cd0434818067c7ee2c48f0eaa0a140f8af4b008ce800d7e12817ed71453dbec9"
}
~~~

## 呼び出し元

- [007cdea8](../007cd/007cdea8.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 190 bytes

~~~c

long FUN_007fcfdc(long param_1,long param_2)

{
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) != "ZN13MyApplication9MapUpdateEvE4$_43") {
    param_1 = 0;
  }
  return param_1;
}

~~~
