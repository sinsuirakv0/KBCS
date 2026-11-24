# 00bb7cec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bb7c50`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb7c50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0039.md#compare-7c4256d9a2e5d367b1dd128541624d30)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bb8ce0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb8ce0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-8af222353c2558815b69855fa570b0e7)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_text_sha256": "cbc513f903df76ce671e09350551bbd1cb167e908bcc4ecf80680ee3ec2c5f49",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bb7cec",
        "00bb7f07"
      ]
    ],
    "bytes_sha256": "b44071c7862a4f9adc8016ce515fc4d15e738ed6a1f09aede2fe3e30581c476e",
    "instruction_count": 135,
    "instruction_bytes": 540,
    "body_bytes": 540,
    "indirect": 0,
    "unresolved": 0
  }
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bb7cec"></a> `00bb7cec` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bb7cf0"></a> `00bb7cf0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb7cf4"></a> `00bb7cf4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb7cf8"></a> `00bb7cf8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bb7cfc"></a> `00bb7cfc` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bb7d00"></a> `00bb7d00` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bb7d04"></a> `00bb7d04` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-00bb7d08"></a> `00bb7d08` | `c0 08 00 54` | b.eq 0x00bb7e20 | `CONDITIONAL_JUMP`
<a id="insn-00bb7d0c"></a> `00bb7d0c` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-00bb7d10"></a> `00bb7d10` | `8a a6 40 a9` | ldp x10,x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bb7d14"></a> `00bb7d14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb7d18"></a> `00bb7d18` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb7d1c"></a> `00bb7d1c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb7d20"></a> `00bb7d20` | `21 15 94 9a` | csinc x1,x9,x20,ne | `FALL_THROUGH`
<a id="insn-00bb7d24"></a> `00bb7d24` | `62 01 8a 9a` | csel x2,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00bb7d28"></a> `00bb7d28` | `16 8d 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bb7d2c"></a> `00bb7d2c` | `88 62 40 39` | ldrb w8,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00bb7d30"></a> `00bb7d30` | `89 2a 42 a9` | ldp x9,x10,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00bb7d34"></a> `00bb7d34` | `8b 66 00 91` | add x11,x20,#0x19 | `FALL_THROUGH`
<a id="insn-00bb7d38"></a> `00bb7d38` | `60 62 00 91` | add x0,x19,#0x18 | `FALL_THROUGH`
<a id="insn-00bb7d3c"></a> `00bb7d3c` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb7d40"></a> `00bb7d40` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb7d44"></a> `00bb7d44` | `61 01 8a 9a` | csel x1,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00bb7d48"></a> `00bb7d48` | `82 01 89 9a` | csel x2,x12,x9,eq | `FALL_THROUGH`
<a id="insn-00bb7d4c"></a> `00bb7d4c` | `0d 8d 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bb7d50"></a> `00bb7d50` | `88 c2 40 39` | ldrb w8,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00bb7d54"></a> `00bb7d54` | `89 aa 43 a9` | ldp x9,x10,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00bb7d58"></a> `00bb7d58` | `8b c6 00 91` | add x11,x20,#0x31 | `FALL_THROUGH`
<a id="insn-00bb7d5c"></a> `00bb7d5c` | `60 c2 00 91` | add x0,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bb7d60"></a> `00bb7d60` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb7d64"></a> `00bb7d64` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb7d68"></a> `00bb7d68` | `61 01 8a 9a` | csel x1,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00bb7d6c"></a> `00bb7d6c` | `82 01 89 9a` | csel x2,x12,x9,eq | `FALL_THROUGH`
<a id="insn-00bb7d70"></a> `00bb7d70` | `04 8d 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bb7d74"></a> `00bb7d74` | `81 26 40 f9` | ldr x1,[x20, #0x48] | `FALL_THROUGH`
<a id="insn-00bb7d78"></a> `00bb7d78` | `60 22 01 91` | add x0,x19,#0x48 | `FALL_THROUGH`
<a id="insn-00bb7d7c"></a> `00bb7d7c` | `82 42 01 91` | add x2,x20,#0x50 | `FALL_THROUGH`
<a id="insn-00bb7d80"></a> `00bb7d80` | `8f 0e e6 97` | bl 0x0053b7bc | `UNCONDITIONAL_CALL`
<a id="insn-00bb7d84"></a> `00bb7d84` | `81 0a 46 a9` | ldp x1,x2,[x20, #0x60] | `FALL_THROUGH`
<a id="insn-00bb7d88"></a> `00bb7d88` | `60 82 01 91` | add x0,x19,#0x60 | `FALL_THROUGH`
<a id="insn-00bb7d8c"></a> `00bb7d8c` | `01 96 02 94` | bl 0x00c5d590 | `UNCONDITIONAL_CALL`
<a id="insn-00bb7d90"></a> `00bb7d90` | `88 e2 41 39` | ldrb w8,[x20, #0x78] | `FALL_THROUGH`
<a id="insn-00bb7d94"></a> `00bb7d94` | `89 2a 48 a9` | ldp x9,x10,[x20, #0x80] | `FALL_THROUGH`
<a id="insn-00bb7d98"></a> `00bb7d98` | `8b e6 01 91` | add x11,x20,#0x79 | `FALL_THROUGH`
<a id="insn-00bb7d9c"></a> `00bb7d9c` | `60 e2 01 91` | add x0,x19,#0x78 | `FALL_THROUGH`
<a id="insn-00bb7da0"></a> `00bb7da0` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb7da4"></a> `00bb7da4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb7da8"></a> `00bb7da8` | `61 01 8a 9a` | csel x1,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00bb7dac"></a> `00bb7dac` | `82 01 89 9a` | csel x2,x12,x9,eq | `FALL_THROUGH`
<a id="insn-00bb7db0"></a> `00bb7db0` | `f4 8c 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bb7db4"></a> `00bb7db4` | `88 42 42 39` | ldrb w8,[x20, #0x90] | `FALL_THROUGH`
<a id="insn-00bb7db8"></a> `00bb7db8` | `89 aa 49 a9` | ldp x9,x10,[x20, #0x98] | `FALL_THROUGH`
<a id="insn-00bb7dbc"></a> `00bb7dbc` | `8b 46 02 91` | add x11,x20,#0x91 | `FALL_THROUGH`
<a id="insn-00bb7dc0"></a> `00bb7dc0` | `60 42 02 91` | add x0,x19,#0x90 | `FALL_THROUGH`
<a id="insn-00bb7dc4"></a> `00bb7dc4` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb7dc8"></a> `00bb7dc8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb7dcc"></a> `00bb7dcc` | `61 01 8a 9a` | csel x1,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00bb7dd0"></a> `00bb7dd0` | `82 01 89 9a` | csel x2,x12,x9,eq | `FALL_THROUGH`
<a id="insn-00bb7dd4"></a> `00bb7dd4` | `eb 8c 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bb7dd8"></a> `00bb7dd8` | `88 a2 42 39` | ldrb w8,[x20, #0xa8] | `FALL_THROUGH`
<a id="insn-00bb7ddc"></a> `00bb7ddc` | `89 2a 4b a9` | ldp x9,x10,[x20, #0xb0] | `FALL_THROUGH`
<a id="insn-00bb7de0"></a> `00bb7de0` | `8b a6 02 91` | add x11,x20,#0xa9 | `FALL_THROUGH`
<a id="insn-00bb7de4"></a> `00bb7de4` | `60 a2 02 91` | add x0,x19,#0xa8 | `FALL_THROUGH`
<a id="insn-00bb7de8"></a> `00bb7de8` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb7dec"></a> `00bb7dec` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb7df0"></a> `00bb7df0` | `61 01 8a 9a` | csel x1,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00bb7df4"></a> `00bb7df4` | `82 01 89 9a` | csel x2,x12,x9,eq | `FALL_THROUGH`
<a id="insn-00bb7df8"></a> `00bb7df8` | `e2 8c 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bb7dfc"></a> `00bb7dfc` | `88 82 44 39` | ldrb w8,[x20, #0x120] | `FALL_THROUGH`
<a id="insn-00bb7e00"></a> `00bb7e00` | `89 aa 52 a9` | ldp x9,x10,[x20, #0x128] | `FALL_THROUGH`
<a id="insn-00bb7e04"></a> `00bb7e04` | `8b 86 04 91` | add x11,x20,#0x121 | `FALL_THROUGH`
<a id="insn-00bb7e08"></a> `00bb7e08` | `60 82 04 91` | add x0,x19,#0x120 | `FALL_THROUGH`
<a id="insn-00bb7e0c"></a> `00bb7e0c` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb7e10"></a> `00bb7e10` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb7e14"></a> `00bb7e14` | `61 01 8a 9a` | csel x1,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00bb7e18"></a> `00bb7e18` | `82 01 89 9a` | csel x2,x12,x9,eq | `FALL_THROUGH`
<a id="insn-00bb7e1c"></a> `00bb7e1c` | `d9 8c 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bb7e20"></a> `00bb7e20` | `88 9e 40 f9` | ldr x8,[x20, #0x138] | `FALL_THROUGH`
<a id="insn-00bb7e24"></a> `00bb7e24` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00bb7e28"></a> `00bb7e28` | `68 9e 00 f9` | str x8,[x19, #0x138] | `FALL_THROUGH`
<a id="insn-00bb7e2c"></a> `00bb7e2c` | `88 c2 40 b9` | ldr w8,[x20, #0xc0] | `FALL_THROUGH`
<a id="insn-00bb7e30"></a> `00bb7e30` | `68 c2 00 b9` | str w8,[x19, #0xc0] | `FALL_THROUGH`
<a id="insn-00bb7e34"></a> `00bb7e34` | `60 02 00 54` | b.eq 0x00bb7e80 | `CONDITIONAL_JUMP`
<a id="insn-00bb7e38"></a> `00bb7e38` | `89 22 43 39` | ldrb w9,[x20, #0xc8] | `FALL_THROUGH`
<a id="insn-00bb7e3c"></a> `00bb7e3c` | `8a 2e 4d a9` | ldp x10,x11,[x20, #0xd0] | `FALL_THROUGH`
<a id="insn-00bb7e40"></a> `00bb7e40` | `88 22 03 91` | add x8,x20,#0xc8 | `FALL_THROUGH`
<a id="insn-00bb7e44"></a> `00bb7e44` | `60 22 03 91` | add x0,x19,#0xc8 | `FALL_THROUGH`
<a id="insn-00bb7e48"></a> `00bb7e48` | `2c fd 41 d3` | lsr x12,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bb7e4c"></a> `00bb7e4c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bb7e50"></a> `00bb7e50` | `61 15 88 9a` | csinc x1,x11,x8,ne | `FALL_THROUGH`
<a id="insn-00bb7e54"></a> `00bb7e54` | `82 01 8a 9a` | csel x2,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bb7e58"></a> `00bb7e58` | `ca 8c 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bb7e5c"></a> `00bb7e5c` | `88 82 43 39` | ldrb w8,[x20, #0xe0] | `FALL_THROUGH`
<a id="insn-00bb7e60"></a> `00bb7e60` | `89 aa 4e a9` | ldp x9,x10,[x20, #0xe8] | `FALL_THROUGH`
<a id="insn-00bb7e64"></a> `00bb7e64` | `8b 86 03 91` | add x11,x20,#0xe1 | `FALL_THROUGH`
<a id="insn-00bb7e68"></a> `00bb7e68` | `60 82 03 91` | add x0,x19,#0xe0 | `FALL_THROUGH`
<a id="insn-00bb7e6c"></a> `00bb7e6c` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb7e70"></a> `00bb7e70` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb7e74"></a> `00bb7e74` | `61 01 8a 9a` | csel x1,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00bb7e78"></a> `00bb7e78` | `82 01 89 9a` | csel x2,x12,x9,eq | `FALL_THROUGH`
<a id="insn-00bb7e7c"></a> `00bb7e7c` | `c1 8c 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bb7e80"></a> `00bb7e80` | `75 7e 40 f9` | ldr x21,[x19, #0xf8] | `FALL_THROUGH`
<a id="insn-00bb7e84"></a> `00bb7e84` | `b5 00 00 b4` | cbz x21,0x00bb7e98 | `CONDITIONAL_JUMP`
<a id="insn-00bb7e88"></a> `00bb7e88` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bb7e8c"></a> `00bb7e8c` | `45 95 02 94` | bl 0x00c5d3a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb7e90"></a> `00bb7e90` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bb7e94"></a> `00bb7e94` | `3b 80 02 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00bb7e98"></a> `00bb7e98` | `96 7e 40 f9` | ldr x22,[x20, #0xf8] | `FALL_THROUGH`
<a id="insn-00bb7e9c"></a> `00bb7e9c` | `f6 00 00 b4` | cbz x22,0x00bb7eb8 | `CONDITIONAL_JUMP`
<a id="insn-00bb7ea0"></a> `00bb7ea0` | `00 25 80 52` | mov w0,#0x128 | `FALL_THROUGH`
<a id="insn-00bb7ea4"></a> `00bb7ea4` | `2f 80 02 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00bb7ea8"></a> `00bb7ea8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bb7eac"></a> `00bb7eac` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bb7eb0"></a> `00bb7eb0` | `38 95 02 94` | bl 0x00c5d390 | `UNCONDITIONAL_CALL`
<a id="insn-00bb7eb4"></a> `00bb7eb4` | `02 00 00 14` | b 0x00bb7ebc | `UNCONDITIONAL_JUMP`
<a id="insn-00bb7eb8"></a> `00bb7eb8` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00bb7ebc"></a> `00bb7ebc` | `75 7e 00 f9` | str x21,[x19, #0xf8] | `FALL_THROUGH`
<a id="insn-00bb7ec0"></a> `00bb7ec0` | `88 02 44 39` | ldrb w8,[x20, #0x100] | `FALL_THROUGH`
<a id="insn-00bb7ec4"></a> `00bb7ec4` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00bb7ec8"></a> `00bb7ec8` | `68 02 04 39` | strb w8,[x19, #0x100] | `FALL_THROUGH`
<a id="insn-00bb7ecc"></a> `00bb7ecc` | `40 01 00 54` | b.eq 0x00bb7ef4 | `CONDITIONAL_JUMP`
<a id="insn-00bb7ed0"></a> `00bb7ed0` | `89 22 44 39` | ldrb w9,[x20, #0x108] | `FALL_THROUGH`
<a id="insn-00bb7ed4"></a> `00bb7ed4` | `8a 2e 51 a9` | ldp x10,x11,[x20, #0x110] | `FALL_THROUGH`
<a id="insn-00bb7ed8"></a> `00bb7ed8` | `88 22 04 91` | add x8,x20,#0x108 | `FALL_THROUGH`
<a id="insn-00bb7edc"></a> `00bb7edc` | `60 22 04 91` | add x0,x19,#0x108 | `FALL_THROUGH`
<a id="insn-00bb7ee0"></a> `00bb7ee0` | `2c fd 41 d3` | lsr x12,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bb7ee4"></a> `00bb7ee4` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bb7ee8"></a> `00bb7ee8` | `61 15 88 9a` | csinc x1,x11,x8,ne | `FALL_THROUGH`
<a id="insn-00bb7eec"></a> `00bb7eec` | `82 01 8a 9a` | csel x2,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bb7ef0"></a> `00bb7ef0` | `a4 8c 02 94` | bl 0x00c5b180 | `UNCONDITIONAL_CALL`
<a id="insn-00bb7ef4"></a> `00bb7ef4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb7ef8"></a> `00bb7ef8` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb7efc"></a> `00bb7efc` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb7f00"></a> `00bb7f00` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bb7f04"></a> `00bb7f04` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bb7cec`](#insn-00bb7cec) 範囲 `[['00bb7cec', '00bb7d0b']]`
  - `CONDITIONAL_JUMP` [`00bb7d08`](#insn-00bb7d08) → [`00bb7e20`](#insn-00bb7e20)
  - `FALL_THROUGH` [`00bb7d08`](#insn-00bb7d08) → [`00bb7d0c`](#insn-00bb7d0c)
- ブロック [`00bb7d0c`](#insn-00bb7d0c) 範囲 `[['00bb7d0c', '00bb7e1f']]`
  - `FALL_THROUGH` [`00bb7e1c`](#insn-00bb7e1c) → [`00bb7e20`](#insn-00bb7e20)
- ブロック [`00bb7e20`](#insn-00bb7e20) 範囲 `[['00bb7e20', '00bb7e37']]`
  - `CONDITIONAL_JUMP` [`00bb7e34`](#insn-00bb7e34) → [`00bb7e80`](#insn-00bb7e80)
  - `FALL_THROUGH` [`00bb7e34`](#insn-00bb7e34) → [`00bb7e38`](#insn-00bb7e38)
- ブロック [`00bb7e38`](#insn-00bb7e38) 範囲 `[['00bb7e38', '00bb7e7f']]`
  - `FALL_THROUGH` [`00bb7e7c`](#insn-00bb7e7c) → [`00bb7e80`](#insn-00bb7e80)
- ブロック [`00bb7e80`](#insn-00bb7e80) 範囲 `[['00bb7e80', '00bb7e87']]`
  - `CONDITIONAL_JUMP` [`00bb7e84`](#insn-00bb7e84) → [`00bb7e98`](#insn-00bb7e98)
  - `FALL_THROUGH` [`00bb7e84`](#insn-00bb7e84) → [`00bb7e88`](#insn-00bb7e88)
- ブロック [`00bb7e88`](#insn-00bb7e88) 範囲 `[['00bb7e88', '00bb7e97']]`
  - `FALL_THROUGH` [`00bb7e94`](#insn-00bb7e94) → [`00bb7e98`](#insn-00bb7e98)
- ブロック [`00bb7e98`](#insn-00bb7e98) 範囲 `[['00bb7e98', '00bb7e9f']]`
  - `CONDITIONAL_JUMP` [`00bb7e9c`](#insn-00bb7e9c) → [`00bb7eb8`](#insn-00bb7eb8)
  - `FALL_THROUGH` [`00bb7e9c`](#insn-00bb7e9c) → [`00bb7ea0`](#insn-00bb7ea0)
- ブロック [`00bb7ea0`](#insn-00bb7ea0) 範囲 `[['00bb7ea0', '00bb7eb7']]`
  - `UNCONDITIONAL_JUMP` [`00bb7eb4`](#insn-00bb7eb4) → [`00bb7ebc`](#insn-00bb7ebc)
- ブロック [`00bb7eb8`](#insn-00bb7eb8) 範囲 `[['00bb7eb8', '00bb7ebb']]`
  - `FALL_THROUGH` [`00bb7eb8`](#insn-00bb7eb8) → [`00bb7ebc`](#insn-00bb7ebc)
- ブロック [`00bb7ebc`](#insn-00bb7ebc) 範囲 `[['00bb7ebc', '00bb7ecf']]`
  - `CONDITIONAL_JUMP` [`00bb7ecc`](#insn-00bb7ecc) → [`00bb7ef4`](#insn-00bb7ef4)
  - `FALL_THROUGH` [`00bb7ecc`](#insn-00bb7ecc) → [`00bb7ed0`](#insn-00bb7ed0)
- ブロック [`00bb7ed0`](#insn-00bb7ed0) 範囲 `[['00bb7ed0', '00bb7ef3']]`
  - `FALL_THROUGH` [`00bb7ef0`](#insn-00bb7ef0) → [`00bb7ef4`](#insn-00bb7ef4)
- ブロック [`00bb7ef4`](#insn-00bb7ef4) 範囲 `[['00bb7ef4', '00bb7f07']]`

## 命令位置別の参照

- [`00bb7cec`](#insn-00bb7cec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb7cf0`](#insn-00bb7cf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb7cf4`](#insn-00bb7cf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb7d08`](#insn-00bb7d08) → [`00bb7e20`](#insn-00bb7e20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb7d28`](#insn-00bb7d28) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bb7d4c`](#insn-00bb7d4c) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bb7d70`](#insn-00bb7d70) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bb7d80`](#insn-00bb7d80) → [`0053b7bc`](../0053b/0053b7bc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0053b7bc` · 推定シンボル `None` · 推定型 `None`
- [`00bb7d8c`](#insn-00bb7d8c) → [`00c5d590`](../00c5d/00c5d590.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d590` · 推定シンボル `None` · 推定型 `None`
- [`00bb7db0`](#insn-00bb7db0) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bb7dd4`](#insn-00bb7dd4) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bb7df8`](#insn-00bb7df8) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bb7e1c`](#insn-00bb7e1c) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bb7e34`](#insn-00bb7e34) → [`00bb7e80`](#insn-00bb7e80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb7e58`](#insn-00bb7e58) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bb7e7c`](#insn-00bb7e7c) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bb7e84`](#insn-00bb7e84) → [`00bb7e98`](#insn-00bb7e98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb7e8c`](#insn-00bb7e8c) → [`00c5d3a0`](../00c5d/00c5d3a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d3a0` · 推定シンボル `None` · 推定型 `None`
- [`00bb7e94`](#insn-00bb7e94) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00bb7e9c`](#insn-00bb7e9c) → [`00bb7eb8`](#insn-00bb7eb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb7ea4`](#insn-00bb7ea4) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00bb7eb0`](#insn-00bb7eb0) → [`00c5d390`](../00c5d/00c5d390.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d390` · 推定シンボル `None` · 推定型 `None`
- [`00bb7eb4`](#insn-00bb7eb4) → [`00bb7ebc`](#insn-00bb7ebc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb7ecc`](#insn-00bb7ecc) → [`00bb7ef4`](#insn-00bb7ef4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb7ef0`](#insn-00bb7ef0) → [`00c5b180`](../00c5b/00c5b180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b180` · 推定シンボル `None` · 推定型 `None`
- [`00bb7ef8`](#insn-00bb7ef8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb7efc`](#insn-00bb7efc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bb7cec`](#insn-00bb7cec)

~~~json
{
  "source": "00bb7cec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb7cf0`](#insn-00bb7cf0)

~~~json
{
  "source": "00bb7cf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb7cf4`](#insn-00bb7cf4)

~~~json
{
  "source": "00bb7cf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb7d08`](#insn-00bb7d08)

~~~json
{
  "source": "00bb7d08",
  "target": "00bb7e20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb7d28`](#insn-00bb7d28)

~~~json
{
  "source": "00bb7d28",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb7d4c`](#insn-00bb7d4c)

~~~json
{
  "source": "00bb7d4c",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb7d70`](#insn-00bb7d70)

~~~json
{
  "source": "00bb7d70",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb7d80`](#insn-00bb7d80)

~~~json
{
  "source": "00bb7d80",
  "target": "0053b7bc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb7d8c`](#insn-00bb7d8c)

~~~json
{
  "source": "00bb7d8c",
  "target": "00c5d590",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb7db0`](#insn-00bb7db0)

~~~json
{
  "source": "00bb7db0",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb7dd4`](#insn-00bb7dd4)

~~~json
{
  "source": "00bb7dd4",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb7df8`](#insn-00bb7df8)

~~~json
{
  "source": "00bb7df8",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb7e1c`](#insn-00bb7e1c)

~~~json
{
  "source": "00bb7e1c",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb7e34`](#insn-00bb7e34)

~~~json
{
  "source": "00bb7e34",
  "target": "00bb7e80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb7e58`](#insn-00bb7e58)

~~~json
{
  "source": "00bb7e58",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb7e7c`](#insn-00bb7e7c)

~~~json
{
  "source": "00bb7e7c",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb7e84`](#insn-00bb7e84)

~~~json
{
  "source": "00bb7e84",
  "target": "00bb7e98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb7e8c`](#insn-00bb7e8c)

~~~json
{
  "source": "00bb7e8c",
  "target": "00c5d3a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb7e94`](#insn-00bb7e94)

~~~json
{
  "source": "00bb7e94",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb7e9c`](#insn-00bb7e9c)

~~~json
{
  "source": "00bb7e9c",
  "target": "00bb7eb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb7ea4`](#insn-00bb7ea4)

~~~json
{
  "source": "00bb7ea4",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb7eb0`](#insn-00bb7eb0)

~~~json
{
  "source": "00bb7eb0",
  "target": "00c5d390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb7eb4`](#insn-00bb7eb4)

~~~json
{
  "source": "00bb7eb4",
  "target": "00bb7ebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb7ecc`](#insn-00bb7ecc)

~~~json
{
  "source": "00bb7ecc",
  "target": "00bb7ef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb7ef0`](#insn-00bb7ef0)

~~~json
{
  "source": "00bb7ef0",
  "target": "00c5b180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb7ef8`](#insn-00bb7ef8)

~~~json
{
  "source": "00bb7ef8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb7efc`](#insn-00bb7efc)

~~~json
{
  "source": "00bb7efc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
