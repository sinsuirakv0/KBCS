# 00bb7cec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bb7cec",
  "name": "_ZN8firebase9messaging7MessageaSERKS1_",
  "size": 540,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cbc513f903df76ce671e09350551bbd1cb167e908bcc4ecf80680ee3ec2c5f49",
  "source_text_sha256": "cbc513f903df76ce671e09350551bbd1cb167e908bcc4ecf80680ee3ec2c5f49"
}
~~~

## 呼び出し元

- [00c5d4d0](../00c5d/00c5d4d0.md)

## 呼び出し先

- [0053b7bc](../0053b/0053b7bc.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c5b180](../00c5b/00c5b180.md)
- [00c5d390](../00c5d/00c5d390.md)
- [00c5d3a0](../00c5d/00c5d3a0.md)
- [00c5d590](../00c5d/00c5d590.md)

## 疑似コード / UTF-8 4422 bytes

~~~c

byte * _ZN8firebase9messaging7MessageaSERKS1_(byte *param_1,byte *param_2)

{
  ulong uVar1;
  byte *pbVar2;
  undefined8 uVar3;
  void *__ptr;
  long lVar4;
  
  if (param_1 != param_2) {
    uVar1 = *(ulong *)(param_2 + 8);
    pbVar2 = *(byte **)(param_2 + 0x10);
    if ((*param_2 & 1) == 0) {
      pbVar2 = param_2 + 1;
      uVar1 = (ulong)(*param_2 >> 1);
    }
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (param_1,pbVar2,uVar1);
    uVar1 = (ulong)(param_2[0x18] >> 1);
    pbVar2 = param_2 + 0x19;
    if ((param_2[0x18] & 1) != 0) {
      uVar1 = *(ulong *)(param_2 + 0x20);
      pbVar2 = *(byte **)(param_2 + 0x28);
    }
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (param_1 + 0x18,pbVar2,uVar1);
    uVar1 = (ulong)(param_2[0x30] >> 1);
    pbVar2 = param_2 + 0x31;
    if ((param_2[0x30] & 1) != 0) {
      uVar1 = *(ulong *)(param_2 + 0x38);
      pbVar2 = *(byte **)(param_2 + 0x40);
    }
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (param_1 + 0x30,pbVar2,uVar1);
    FUN_0053b7bc(param_1 + 0x48,*(undefined8 *)(param_2 + 0x48),param_2 + 0x50);
    _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6assignIPhEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_traitsIS7_E9referenceEEE5valueEvE4typeES7_S7_
              (param_1 + 0x60,*(undefined8 *)(param_2 + 0x60),*(undefined8 *)(param_2 + 0x68));
    uVar1 = (ulong)(param_2[0x78] >> 1);
    pbVar2 = param_2 + 0x79;
    if ((param_2[0x78] & 1) != 0) {
      uVar1 = *(ulong *)(param_2 + 0x80);
      pbVar2 = *(byte **)(param_2 + 0x88);
    }
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (param_1 + 0x78,pbVar2,uVar1);
    uVar1 = (ulong)(param_2[0x90] >> 1);
    pbVar2 = param_2 + 0x91;
    if ((param_2[0x90] & 1) != 0) {
      uVar1 = *(ulong *)(param_2 + 0x98);
      pbVar2 = *(byte **)(param_2 + 0xa0);
    }
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (param_1 + 0x90,pbVar2,uVar1);
    uVar1 = (ulong)(param_2[0xa8] >> 1);
    pbVar2 = param_2 + 0xa9;
    if ((param_2[0xa8] & 1) != 0) {
      uVar1 = *(ulong *)(param_2 + 0xb0);
      pbVar2 = *(byte **)(param_2 + 0xb8);
    }
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (param_1 + 0xa8,pbVar2,uVar1);
    uVar1 = (ulong)(param_2[0x120] >> 1);
    pbVar2 = param_2 + 0x121;
    if ((param_2[0x120] & 1) != 0) {
      uVar1 = *(ulong *)(param_2 + 0x128);
      pbVar2 = *(byte **)(param_2 + 0x130);
    }
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (param_1 + 0x120,pbVar2,uVar1);
  }
  *(undefined8 *)(param_1 + 0x138) = *(undefined8 *)(param_2 + 0x138);
  *(undefined4 *)(param_1 + 0xc0) = *(undefined4 *)(param_2 + 0xc0);
  if (param_1 != param_2) {
    uVar1 = *(ulong *)(param_2 + 0xd0);
    pbVar2 = *(byte **)(param_2 + 0xd8);
    if ((param_2[200] & 1) == 0) {
      pbVar2 = param_2 + 0xc9;
      uVar1 = (ulong)(param_2[200] >> 1);
    }
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (param_1 + 200,pbVar2,uVar1);
    uVar1 = (ulong)(param_2[0xe0] >> 1);
    pbVar2 = param_2 + 0xe1;
    if ((param_2[0xe0] & 1) != 0) {
      uVar1 = *(ulong *)(param_2 + 0xe8);
      pbVar2 = *(byte **)(param_2 + 0xf0);
    }
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (param_1 + 0xe0,pbVar2,uVar1);
  }
  __ptr = *(void **)(param_1 + 0xf8);
  if (__ptr != (void *)0x0) {
    _ZN8firebase9messaging12NotificationD2Ev(__ptr);
    _ZdlPv(__ptr);
  }
  lVar4 = *(long *)(param_2 + 0xf8);
  if (lVar4 == 0) {
    uVar3 = 0;
  }
  else {
    uVar3 = _Znwm(0x128);
    _ZN8firebase9messaging12NotificationC2ERKS1_(uVar3,lVar4);
  }
  *(undefined8 *)(param_1 + 0xf8) = uVar3;
  param_1[0x100] = param_2[0x100];
  if (param_1 != param_2) {
    uVar1 = *(ulong *)(param_2 + 0x110);
    pbVar2 = *(byte **)(param_2 + 0x118);
    if ((param_2[0x108] & 1) == 0) {
      pbVar2 = param_2 + 0x109;
      uVar1 = (ulong)(param_2[0x108] >> 1);
    }
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (param_1 + 0x108,pbVar2,uVar1);
  }
  return param_1;
}

~~~
