# 00bb2afc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bb2afc",
  "name": "_ZN11flatbuffers14StripExtensionERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e3a1df851eaefe306625f99c503fd260bcdaf0a0f8640fe408c9de2a594b5b43",
  "source_text_sha256": "e3a1df851eaefe306625f99c503fd260bcdaf0a0f8640fe408c9de2a594b5b43"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5b1b0](../00c5b/00c5b1b0.md)
- [00c5b3f0](../00c5b/00c5b3f0.md)

## 疑似コード / UTF-8 852 bytes

~~~c

void _ZN11flatbuffers14StripExtensionERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
               (undefined8 param_1,byte *param_2)

{
  byte *pbVar1;
  long lVar2;
  ulong uVar3;
  
  uVar3 = *(ulong *)(param_2 + 8);
  pbVar1 = *(byte **)(param_2 + 0x10);
  if ((*param_2 & 1) == 0) {
    pbVar1 = param_2 + 1;
    uVar3 = (ulong)(*param_2 >> 1);
  }
  if (uVar3 != 0) {
    do {
      if (uVar3 == 0) goto LAB_00bb2b4c;
      lVar2 = uVar3 - 1;
      uVar3 = uVar3 - 1;
    } while (pbVar1[lVar2] != 0x2e);
    if (uVar3 != 0xffffffffffffffff) {
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_
                (param_1,param_2,0,uVar3,param_2);
      return;
    }
  }
LAB_00bb2b4c:
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_(param_1);
  return;
}

~~~
