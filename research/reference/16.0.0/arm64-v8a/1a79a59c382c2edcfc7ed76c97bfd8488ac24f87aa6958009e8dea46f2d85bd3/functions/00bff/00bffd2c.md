# 00bffd2c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bffd2c",
  "name": "_ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEEC2EPNS_15basic_streambufIwS2_EE",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2ee055061aaad9efab2704480d25b8bdf2f02265acdc37cc20f51c627aac9f9c",
  "source_text_sha256": "2ee055061aaad9efab2704480d25b8bdf2f02265acdc37cc20f51c627aac9f9c"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57de0](../00c57/00c57de0.md)

## 疑似コード / UTF-8 545 bytes

~~~c

void _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEEC2EPNS_15basic_streambufIwS2_EE
               (long *param_1,long *param_2,undefined8 param_3)

{
  long lVar1;
  long lVar2;
  
  lVar1 = *param_2;
  *param_1 = lVar1;
  lVar1 = *(long *)(lVar1 + -0x18);
  lVar2 = param_2[1];
  param_1[1] = 0;
  *(long *)((long)param_1 + lVar1) = lVar2;
  lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
  _ZNSt6__ndk18ios_base4initEPv(lVar1,param_3);
  *(undefined8 *)(lVar1 + 0x88) = 0;
  *(undefined4 *)(lVar1 + 0x90) = 0xffffffff;
  return;
}

~~~
