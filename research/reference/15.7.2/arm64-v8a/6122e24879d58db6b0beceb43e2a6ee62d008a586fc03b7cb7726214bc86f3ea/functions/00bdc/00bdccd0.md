# 00bdccd0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdccd0.md)

## 関数情報

~~~json
{
  "address": "00bdccd0",
  "name": "Botan::OCSP::Response::check_signature",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "94f5edd51a4be58f743728fb35262122e9b4391c974b6f50148282688669f794",
  "source_text_sha256": "94f5edd51a4be58f743728fb35262122e9b4391c974b6f50148282688669f794"
}
~~~
## 呼び出し元

- [00504f50](../00504/00504f50.md)

## 呼び出し先

- [004e8a14](../004e8/004e8a14.md)

## 疑似コード 1/1 / UTF-8 174 bytes

~~~c

void __thiscall
Botan::OCSP::Response::check_signature(Response *this,vector *param_1,vector *param_2)

{
  (*(code *)PTR_check_signature_00c1cea0)();
  return;
}

~~~
