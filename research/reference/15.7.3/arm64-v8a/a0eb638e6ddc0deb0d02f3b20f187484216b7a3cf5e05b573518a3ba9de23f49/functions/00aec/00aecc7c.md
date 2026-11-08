# 00aecc7c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00aecc7c",
  "name": "_ZN8firebase4util22parcel_file_descriptor11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8b9363002133eb015ecce41961113ad81b452e2df5fd1ed3b6c7969892508022",
  "source_text_sha256": "8b9363002133eb015ecce41961113ad81b452e2df5fd1ed3b6c7969892508022"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde130](../00bde/00bde130.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

## 疑似コード / UTF-8 250 bytes

~~~c

undefined8 _ZN8firebase4util22parcel_file_descriptor11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return *(undefined8 *)(&DAT_010a0978 + (ulong)param_1 * 8);
}

~~~
