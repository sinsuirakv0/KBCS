# 00bff3bc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bff3bc",
  "name": "_ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEEC1EPNS_15basic_streambufIcS2_EE",
  "size": 116,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "56096bb493ee35ec396e865a055d0393d523d44e25b98ac74dcc88b2ee8b13d4",
  "source_text_sha256": "56096bb493ee35ec396e865a055d0393d523d44e25b98ac74dcc88b2ee8b13d4"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57de0](../00c57/00c57de0.md)

## 疑似コード / UTF-8 687 bytes

~~~c

void _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEEC1EPNS_15basic_streambufIcS2_EE
               (long *param_1)

{
  undefined *puVar1;
  
  puVar1 = 
  PTR__ZTCNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEEE0_NS_13basic_istreamIcS2_EE_00c9b720;
  param_1[9] = 0;
  param_1[3] = (long)(puVar1 + 0x40);
  *param_1 = (long)(puVar1 + 0x18);
  param_1[1] = 0;
  _ZNSt6__ndk18ios_base4initEPv(param_1 + 3);
  puVar1 = PTR__ZTVNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEEE_00c9b728;
  *(undefined4 *)(param_1 + 0x15) = 0xffffffff;
  param_1[0x14] = 0;
  *param_1 = (long)(puVar1 + 0x18);
  param_1[2] = (long)(puVar1 + 0x40);
  param_1[3] = (long)(puVar1 + 0x68);
  return;
}

~~~
