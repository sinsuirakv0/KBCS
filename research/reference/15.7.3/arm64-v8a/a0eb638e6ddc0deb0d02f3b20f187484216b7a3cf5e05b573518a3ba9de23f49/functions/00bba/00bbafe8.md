# 00bbafe8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bbafe8",
  "name": "_ZNSt11range_errorD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "32873c4fc9e475488aba629eac6cc38d36f8c956b295d983558fcb6f9301ba97",
  "source_text_sha256": "32873c4fc9e475488aba629eac6cc38d36f8c956b295d983558fcb6f9301ba97"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)
- [00bdda20](../00bdd/00bdda20.md)

## 疑似コード / UTF-8 110 bytes

~~~c

void _ZNSt11range_errorD0Ev(void *param_1)

{
  _ZNSt14overflow_errorD1Ev();
  _ZdlPv(param_1);
  return;
}

~~~
