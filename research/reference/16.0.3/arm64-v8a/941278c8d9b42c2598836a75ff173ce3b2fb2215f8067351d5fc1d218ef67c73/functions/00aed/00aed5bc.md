# 00aed5bc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00aed5bc",
  "name": "FUN_00aed5bc",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4ae2a36994eec5eb70190b1a5fde2c70cd58c0224006e448b6e05a80a74baf3d",
  "source_text_sha256": "4ae2a36994eec5eb70190b1a5fde2c70cd58c0224006e448b6e05a80a74baf3d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00aed33c](../00aed/00aed33c.md)
- [00c58f50](../00c58/00c58f50.md)

## 疑似コード / UTF-8 87 bytes

~~~c

void FUN_00aed5bc(void *param_1)

{
  FUN_00aed33c();
  _ZdlPv(param_1);
  return;
}

~~~
