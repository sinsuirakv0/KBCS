# 00bfbcc0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bfbcc0",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEEC1EPNS_15basic_streambufIcS2_EE",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cba33e4d2c036e6bc5b084ae2774b2c4fe91d08fa1c01da78f2d759d4831ec5f",
  "source_text_sha256": "cba33e4d2c036e6bc5b084ae2774b2c4fe91d08fa1c01da78f2d759d4831ec5f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57de0](../00c57/00c57de0.md)

## 疑似コード / UTF-8 463 bytes

~~~c

void _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEEC1EPNS_15basic_streambufIcS2_EE
               (long *param_1)

{
  undefined *puVar1;
  
  puVar1 = PTR__ZTVNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEEE_00c9ae30;
  param_1[8] = 0;
  param_1[2] = (long)(puVar1 + 0x40);
  *param_1 = (long)(puVar1 + 0x18);
  param_1[1] = 0;
  _ZNSt6__ndk18ios_base4initEPv(param_1 + 2);
  param_1[0x13] = 0;
  *(undefined4 *)(param_1 + 0x14) = 0xffffffff;
  return;
}

~~~
