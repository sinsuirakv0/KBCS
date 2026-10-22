# 00bdcca0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdcca0.md)

## 関数情報

~~~json
{
  "address": "00bdcca0",
  "name": "Botan::BER_Decoder::decode_optional<Botan::Extensions>",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5fae78eff9ecfa79a612803bb72765561b1249c36cb34ac9f2fbdc4366b6944a",
  "source_text_sha256": "5fae78eff9ecfa79a612803bb72765561b1249c36cb34ac9f2fbdc4366b6944a"
}
~~~
## 呼び出し元

- [004e6d3c](../004e6/004e6d3c.md)
- [004e9fdc](../004e9/004e9fdc.md)

## 呼び出し先

- [004e82ac](../004e8/004e82ac.md)

## 疑似コード 1/1 / UTF-8 332 bytes

~~~c

BER_Decoder * __thiscall Botan::BER_Decoder::decode_optional<Botan::Extensions>(void)

{
  BER_Decoder *pBVar1;
  
                    /* try { // try from 00bdcca0 to 00cdccbf has its CatchHandler @ 00bdd1a4 */
  pBVar1 = (BER_Decoder *)(*(code *)PTR_decode_optional<Botan::Extensions>_00c1ce88)();
  return pBVar1;
}

~~~
