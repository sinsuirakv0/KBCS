# 00bdcce0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdcce0.md)

## 関数情報

~~~json
{
  "address": "00bdcce0",
  "name": "Botan::X509_Certificate::subject_public_key_bitstring_sha1",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8b1afc228aeb9ca6220d4ea68efdd053acf0ea9cb0e80d3fd29369cf8bd37fb5",
  "source_text_sha256": "8b1afc228aeb9ca6220d4ea68efdd053acf0ea9cb0e80d3fd29369cf8bd37fb5"
}
~~~
## 呼び出し元

- [004e8a14](../004e8/004e8a14.md)

## 呼び出し先

- [004e8fec](../004e8/004e8fec.md)

## 疑似コード 1/1 / UTF-8 187 bytes

~~~c

void __thiscall Botan::X509_Certificate::subject_public_key_bitstring_sha1(X509_Certificate *this)

{
  (*(code *)PTR_subject_public_key_bitstring_sha1_00c1cea8)();
  return;
}

~~~
