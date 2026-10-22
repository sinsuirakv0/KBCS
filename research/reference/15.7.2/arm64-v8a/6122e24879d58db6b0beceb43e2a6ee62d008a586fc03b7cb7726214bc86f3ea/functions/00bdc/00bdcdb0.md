# 00bdcdb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdcdb0.md)

## 関数情報

~~~json
{
  "address": "00bdcdb0",
  "name": "Botan::PKCS10_Request::is_CA",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6c12e23ce1c8e4c38110afcb76003a4135093e782caef58bf4aafdc335e8cb99",
  "source_text_sha256": "6c12e23ce1c8e4c38110afcb76003a4135093e782caef58bf4aafdc335e8cb99"
}
~~~
## 呼び出し元

- [004ede80](../004ed/004ede80.md)

## 呼び出し先

- [004ec73c](../004ec/004ec73c.md)

## 疑似コード 1/1 / UTF-8 127 bytes

~~~c

void __thiscall Botan::PKCS10_Request::is_CA(PKCS10_Request *this)

{
  (*(code *)PTR_is_CA_00c1cf10)();
  return;
}

~~~
