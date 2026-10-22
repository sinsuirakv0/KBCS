# 00bdcee0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdcee0.md)

## 関数情報

~~~json
{
  "address": "00bdcee0",
  "name": "Botan::BER_Decoder::decode_list<Botan::OID>",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "13cfd8b4ec0bde05cc9eaa691e8dc9ea65e89ee262689947c4fb9284919fea9a",
  "source_text_sha256": "13cfd8b4ec0bde05cc9eaa691e8dc9ea65e89ee262689947c4fb9284919fea9a"
}
~~~
## 呼び出し元

- [004f6e58](../004f6/004f6e58.md)

## 呼び出し先

- [004f6f28](../004f6/004f6f28.md)

## 疑似コード 1/1 / UTF-8 212 bytes

~~~c

BER_Decoder * __thiscall Botan::BER_Decoder::decode_list<Botan::OID>(void)

{
  BER_Decoder *pBVar1;
  
  pBVar1 = (BER_Decoder *)(*(code *)PTR_decode_list<Botan::OID>_00c1cfa8)();
  return pBVar1;
}

~~~
