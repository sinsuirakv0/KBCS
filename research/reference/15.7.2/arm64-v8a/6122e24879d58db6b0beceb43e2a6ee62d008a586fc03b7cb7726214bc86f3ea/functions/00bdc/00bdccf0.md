# 00bdccf0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdccf0.md)

## 関数情報

~~~json
{
  "address": "00bdccf0",
  "name": "Botan::X509_Certificate::allowed_extended_usage",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "79f8dc55617561a8106144fa70725cbd1f3ccb47308f64fc52f262b25568e7a6",
  "source_text_sha256": "79f8dc55617561a8106144fa70725cbd1f3ccb47308f64fc52f262b25568e7a6"
}
~~~
## 呼び出し元

- [004e8a14](../004e8/004e8a14.md)
- [004ffc88](../004ff/004ffc88.md)

## 呼び出し先

- [004e9148](../004e9/004e9148.md)

## 疑似コード 1/1 / UTF-8 188 bytes

~~~c

void __thiscall
Botan::X509_Certificate::allowed_extended_usage(X509_Certificate *this,basic_string *param_1)

{
  (*(code *)PTR_allowed_extended_usage_00c1ceb0)();
  return;
}

~~~
