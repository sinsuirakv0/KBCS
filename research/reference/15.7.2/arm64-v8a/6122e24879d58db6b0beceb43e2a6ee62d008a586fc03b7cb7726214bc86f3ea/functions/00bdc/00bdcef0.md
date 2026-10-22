# 00bdcef0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdcef0.md)

## 関数情報

~~~json
{
  "address": "00bdcef0",
  "name": "Botan::BER_Decoder::decode_list<Botan::GeneralSubtree>",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ba781f9d00c471352f55a80db866d6b11940994d1e5906fc0e40fa24bb39e9b9",
  "source_text_sha256": "ba781f9d00c471352f55a80db866d6b11940994d1e5906fc0e40fa24bb39e9b9"
}
~~~
## 呼び出し元

- [004f73a8](../004f7/004f73a8.md)

## 呼び出し先

- [004f78a4](../004f7/004f78a4.md)

## 疑似コード 1/1 / UTF-8 332 bytes

~~~c

BER_Decoder * __thiscall Botan::BER_Decoder::decode_list<Botan::GeneralSubtree>(void)

{
  BER_Decoder *pBVar1;
  
                    /* try { // try from 00bdcef4 to 00cdceff has its CatchHandler @ 00bdd18c */
  pBVar1 = (BER_Decoder *)(*(code *)PTR_decode_list<Botan::GeneralSubtree>_00c1cfb0)();
  return pBVar1;
}

~~~
