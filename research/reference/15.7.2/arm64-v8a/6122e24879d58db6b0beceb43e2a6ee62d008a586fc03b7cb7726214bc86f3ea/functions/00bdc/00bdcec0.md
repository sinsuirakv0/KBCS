# 00bdcec0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdcec0.md)

## 関数情報

~~~json
{
  "address": "00bdcec0",
  "name": "Botan::BER_Decoder::decode_optional<bool>",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fb89f466443c6cb7f8319b29ede5858013c677550c36d53f6e3482f89602f91d",
  "source_text_sha256": "fb89f466443c6cb7f8319b29ede5858013c677550c36d53f6e3482f89602f91d"
}
~~~
## 呼び出し元

- [004f4778](../004f4/004f4778.md)
- [004f52c8](../004f5/004f52c8.md)

## 呼び出し先

- [004f4ba8](../004f4/004f4ba8.md)

## 疑似コード 1/1 / UTF-8 208 bytes

~~~c

BER_Decoder * __thiscall Botan::BER_Decoder::decode_optional<bool>(void)

{
  BER_Decoder *pBVar1;
  
  pBVar1 = (BER_Decoder *)(*(code *)PTR_decode_optional<bool>_00c1cf98)();
  return pBVar1;
}

~~~
