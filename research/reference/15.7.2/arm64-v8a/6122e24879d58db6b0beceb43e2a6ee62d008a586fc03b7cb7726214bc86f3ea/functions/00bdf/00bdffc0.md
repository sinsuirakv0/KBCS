# 00bdffc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdffc0.md)

## 関数情報

~~~json
{
  "address": "00bdffc0",
  "name": "std::__ndk1::vector<flatbuffers::EnumDef*,std::__ndk1::allocator<flatbuffers::EnumDef*>>::assign<flatbuffers::EnumDef**>",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5ab40835d14800b188e3efb641ecbf2039de0fd34301e9f9c10300b956e60e12",
  "source_text_sha256": "5ab40835d14800b188e3efb641ecbf2039de0fd34301e9f9c10300b956e60e12"
}
~~~
## 呼び出し元

- [00b1cedc](../00b1c/00b1cedc.md)

## 呼び出し先

- [00b2eb24](../00b2e/00b2eb24.md)

## 疑似コード 1/1 / UTF-8 636 bytes

~~~c

void __thiscall
std::__ndk1::vector<flatbuffers::EnumDef*,std::__ndk1::allocator<flatbuffers::EnumDef*>>::
assign<flatbuffers::EnumDef**>
          (vector<flatbuffers::EnumDef*,std::__ndk1::allocator<flatbuffers::EnumDef*>> *this,
          EnumDef **param_1,EnumDef **param_2)

{
                    /* try { // try from 00bdffcc to 00cdffe3 has its CatchHandler @ 00bdffcc
                       catch() { ... } // from try @ 00bdffcc with catch @ 00bdffcc
                       catch() { ... } // from try @ 00bdffec with catch @ 00bdffcc */
  (*(code *)PTR_assign<flatbuffers::EnumDef**>_00c1e818)();
  return;
}

~~~
