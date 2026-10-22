# 00bdccb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdccb0.md)

## 関数情報

~~~json
{
  "address": "00bdccb0",
  "name": "Botan::OCSP::Response::verify_signature",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "701acf932b8a128eeff98d64339a85fce2f42e0379d2ffff37dcc382121e5579",
  "source_text_sha256": "701acf932b8a128eeff98d64339a85fce2f42e0379d2ffff37dcc382121e5579"
}
~~~
## 呼び出し元

- [004e8a14](../004e8/004e8a14.md)

## 呼び出し先

- [004e85ec](../004e8/004e85ec.md)

## 疑似コード 1/1 / UTF-8 143 bytes

~~~c

void Botan::OCSP::Response::verify_signature(X509_Certificate *param_1)

{
  (*(code *)PTR_verify_signature_00c1ce90)();
  return;
}

~~~
