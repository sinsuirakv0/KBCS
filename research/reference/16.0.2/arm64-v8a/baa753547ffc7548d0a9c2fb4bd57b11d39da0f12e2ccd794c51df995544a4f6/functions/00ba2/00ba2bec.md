# 00ba2bec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00ba2b50`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba2/00ba2b50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0038.md#compare-7a906da7fc0e42887a733fc52fc5b4da)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00ba3be0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba3/00ba3be0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0034.md#compare-9a8f56a66ed438bee101f9eee44fc2b6)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ba2bec",
  "name": "_ZNSt6__ndk115__inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS6_EEEEvT0_SC_SC_T_NS_15iterator_traitsISC_E15difference_typeESG_PNSF_10value_typeEl",
  "size": 1064,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d0cecbae78d0128a563b7ec71565a8bc282124c064a0fc4d654f8923b5be610a",
  "source_text_sha256": "d0cecbae78d0128a563b7ec71565a8bc282124c064a0fc4d654f8923b5be610a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ba2bec",
        "00ba3013"
      ]
    ],
    "bytes_sha256": "020059878f1fc3e75051760b28ba54ef7c1406bef5a79cc79024dc564300c8b3",
    "instruction_count": 266,
    "instruction_bytes": 1064,
    "body_bytes": 1064,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5cc70](../00c5c/00c5cc70.md)

## 呼び出し先

- [00ba35e0](../00ba3/00ba35e0.md)
- [00c58120](../00c58/00c58120.md)
- [00c5cc70](../00c5c/00c5cc70.md)
- [00c5ce30](../00c5c/00c5ce30.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6349 bytes

~~~c

void _ZNSt6__ndk115__inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS6_EEEEvT0_SC_SC_T_NS_15iterator_traitsISC_E15difference_typeESG_PNSF_10value_typeEl
               (uint *param_1,uint *param_2,uint *param_3,long *param_4,long param_5,long param_6,
               undefined8 param_7,long param_8)

{
  uint *puVar1;
  ulong uVar2;
  uint uVar3;
  uint uVar4;
  uint uVar5;
  uint uVar6;
  uint uVar7;
  bool bVar8;
  int iVar9;
  int *piVar10;
  long lVar11;
  uint *puVar12;
  uint *puVar13;
  long lVar14;
  ulong uVar15;
  long lVar16;
  ulong uVar17;
  long lVar18;
  uint *puVar19;
  uint *puVar20;
  
  while( true ) {
    if (param_6 == 0) {
      return;
    }
    if ((param_6 <= param_8) || (param_5 <= param_8)) break;
    if (param_5 == 0) {
      return;
    }
    lVar14 = 0;
    lVar16 = 0;
    uVar3 = *param_2;
    lVar18 = *(long *)(*param_4 + 0x38) + *(long *)(*param_4 + 0x28);
    piVar10 = (int *)(lVar18 - (ulong)uVar3);
    puVar19 = (uint *)((long)piVar10 + (ulong)*(ushort *)((long)piVar10 + (4 - (long)*piVar10)));
    puVar19 = (uint *)((long)puVar19 + (ulong)*puVar19);
    uVar4 = *puVar19;
    while( true ) {
      uVar7 = param_1[lVar16];
      piVar10 = (int *)(lVar18 - (ulong)uVar7);
      puVar13 = (uint *)((long)piVar10 + (ulong)*(ushort *)((long)piVar10 + (4 - (long)*piVar10)));
      puVar13 = (uint *)((long)puVar13 + (ulong)*puVar13);
      uVar5 = *puVar13;
      uVar6 = uVar5;
      if (uVar4 <= uVar5) {
        uVar6 = uVar4;
      }
      iVar9 = memcmp(puVar19 + 1,puVar13 + 1,(ulong)uVar6);
      bVar8 = uVar4 < uVar5;
      if (iVar9 != 0) {
        bVar8 = iVar9 < 0;
      }
      if (bVar8) break;
      lVar16 = lVar16 + 1;
      lVar14 = lVar14 + -4;
      if (param_5 == lVar16) {
        return;
      }
    }
    lVar11 = param_5 - lVar16;
    puVar19 = (uint *)((long)param_1 - lVar14);
    if (lVar11 < param_6) {
      lVar14 = param_6;
      if (param_6 < 0) {
        lVar14 = param_6 + 1;
      }
      lVar14 = lVar14 >> 1;
      puVar13 = param_2 + lVar14;
      puVar20 = puVar19;
      if ((long)param_2 - (long)puVar19 != 0) {
        uVar15 = (long)param_2 - (long)puVar19 >> 2;
        piVar10 = (int *)(lVar18 - (ulong)*puVar13);
        puVar1 = (uint *)((long)piVar10 + (ulong)*(ushort *)((long)piVar10 + (4 - (long)*piVar10)));
        puVar1 = (uint *)((long)puVar1 + (ulong)*puVar1);
        uVar3 = *puVar1;
        do {
          uVar17 = uVar15 >> 1;
          piVar10 = (int *)(lVar18 - (ulong)puVar20[uVar17]);
          puVar12 = (uint *)((long)piVar10 +
                            (ulong)*(ushort *)((long)piVar10 + (4 - (long)*piVar10)));
          puVar12 = (uint *)((long)puVar12 + (ulong)*puVar12);
          uVar6 = *puVar12;
          uVar4 = uVar6;
          if (uVar3 <= uVar6) {
            uVar4 = uVar3;
          }
          iVar9 = memcmp(puVar1 + 1,puVar12 + 1,(ulong)uVar4);
          bVar8 = uVar3 < uVar6;
          if (iVar9 != 0) {
            bVar8 = iVar9 < 0;
          }
          uVar2 = uVar15 + ~uVar17;
          uVar15 = uVar17;
          if (!bVar8) {
            puVar20 = puVar20 + uVar17 + 1;
            uVar15 = uVar2;
          }
        } while (uVar15 != 0);
      }
      lVar11 = (long)puVar20 - (long)puVar19 >> 2;
    }
    else {
      if (param_5 + -1 == lVar16) {
        param_1[lVar16] = uVar3;
        *param_2 = uVar7;
        return;
      }
      if (lVar11 < 0) {
        lVar11 = lVar11 + 1;
      }
      lVar11 = lVar11 >> 1;
      puVar20 = (uint *)((long)param_1 + (lVar11 * 4 - lVar14));
      puVar13 = param_2;
      if ((long)param_3 - (long)param_2 != 0) {
        uVar15 = (long)param_3 - (long)param_2 >> 2;
        piVar10 = (int *)(lVar18 - (ulong)param_1[lVar11 + lVar16]);
        puVar1 = (uint *)((long)piVar10 + (ulong)*(ushort *)((long)piVar10 + (4 - (long)*piVar10)));
        puVar1 = (uint *)((long)puVar1 + (ulong)*puVar1);
        uVar3 = *puVar1;
        puVar12 = param_2;
        do {
          uVar17 = uVar15 >> 1;
          piVar10 = (int *)(lVar18 - (ulong)puVar12[uVar17]);
          puVar13 = (uint *)((long)piVar10 +
                            (ulong)*(ushort *)((long)piVar10 + (4 - (long)*piVar10)));
          puVar13 = (uint *)((long)puVar13 + (ulong)*puVar13);
          uVar6 = *puVar13;
          uVar4 = uVar3;
          if (uVar6 <= uVar3) {
            uVar4 = uVar6;
          }
          iVar9 = memcmp(puVar13 + 1,puVar1 + 1,(ulong)uVar4);
          bVar8 = uVar6 < uVar3;
          if (iVar9 != 0) {
            bVar8 = iVar9 < 0;
          }
          puVar13 = puVar12 + uVar17 + 1;
          uVar15 = uVar15 + ~uVar17;
          if (!bVar8) {
            puVar13 = puVar12;
            uVar15 = uVar17;
          }
          puVar12 = puVar13;
        } while (uVar15 != 0);
      }
      lVar14 = (long)puVar13 - (long)param_2 >> 2;
    }
    lVar18 = (param_5 - lVar11) - lVar16;
    param_1 = puVar13;
    if ((puVar20 != param_2) && (param_1 = puVar20, param_2 != puVar13)) {
      param_1 = (uint *)FUN_00ba35e0(puVar20,param_2,puVar13);
    }
    if (lVar14 + lVar11 < ((param_6 + param_5) - (lVar14 + lVar11)) - lVar16) {
      _ZNSt6__ndk115__inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS6_EEEEvT0_SC_SC_T_NS_15iterator_traitsISC_E15difference_typeESG_PNSF_10value_typeEl
                (puVar19,puVar20,param_1,param_4,lVar11,lVar14,param_7,param_8);
      param_2 = puVar13;
      param_6 = param_6 - lVar14;
      param_5 = lVar18;
    }
    else {
      _ZNSt6__ndk115__inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS6_EEEEvT0_SC_SC_T_NS_15iterator_traitsISC_E15difference_typeESG_PNSF_10value_typeEl
                (param_1,puVar13,param_3,param_4,lVar18,param_6 - lVar14,param_7,param_8);
      param_3 = param_1;
      param_2 = puVar20;
      param_6 = lVar14;
      param_5 = lVar11;
      param_1 = puVar19;
    }
  }
  _ZNSt6__ndk124__buffered_inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS6_EEEEvT0_SC_SC_T_NS_15iterator_traitsISC_E15difference_typeESG_PNSF_10value_typeE
            (param_1,param_2,param_3,param_4,param_5,param_6,param_7);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ba2bec"></a> `00ba2bec` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00ba2bf0"></a> `00ba2bf0` | `fc 6f 05 a9` | stp x28,x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ba2bf4"></a> `00ba2bf4` | `fa 67 06 a9` | stp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ba2bf8"></a> `00ba2bf8` | `f8 5f 07 a9` | stp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ba2bfc"></a> `00ba2bfc` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00ba2c00"></a> `00ba2c00` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00ba2c04"></a> `00ba2c04` | `fd 7b 0a a9` | stp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00ba2c08"></a> `00ba2c08` | `fd 83 02 91` | add x29,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00ba2c0c"></a> `00ba2c0c` | `e3 9f 02 a9` | stp x3,x7,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00ba2c10"></a> `00ba2c10` | `e6 8b 01 a9` | stp x6,x2,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ba2c14"></a> `00ba2c14` | `e1 97 03 a9` | stp x1,x5,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00ba2c18"></a> `00ba2c18` | `e5 1e 00 b4` | cbz x5,0x00ba2ff4 | `CONDITIONAL_JUMP`
<a id="insn-00ba2c1c"></a> `00ba2c1c` | `f7 03 04 aa` | mov x23,x4 | `FALL_THROUGH`
<a id="insn-00ba2c20"></a> `00ba2c20` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00ba2c24"></a> `00ba2c24` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba2c28"></a> `00ba2c28` | `e5 23 40 f9` | ldr x5,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ba2c2c"></a> `00ba2c2c` | `bf 00 08 eb` | cmp x5,x8 | `FALL_THROUGH`
<a id="insn-00ba2c30"></a> `00ba2c30` | `2d 1c 00 54` | b.le 0x00ba2fb4 | `CONDITIONAL_JUMP`
<a id="insn-00ba2c34"></a> `00ba2c34` | `ff 02 08 eb` | cmp x23,x8 | `FALL_THROUGH`
<a id="insn-00ba2c38"></a> `00ba2c38` | `ed 1b 00 54` | b.le 0x00ba2fb4 | `CONDITIONAL_JUMP`
<a id="insn-00ba2c3c"></a> `00ba2c3c` | `d7 1d 00 b4` | cbz x23,0x00ba2ff4 | `CONDITIONAL_JUMP`
<a id="insn-00ba2c40"></a> `00ba2c40` | `e8 17 40 f9` | ldr x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00ba2c44"></a> `00ba2c44` | `ea 1f 40 f9` | ldr x10,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00ba2c48"></a> `00ba2c48` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00ba2c4c"></a> `00ba2c4c` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00ba2c50"></a> `00ba2c50` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ba2c54"></a> `00ba2c54` | `58 01 40 b9` | ldr w24,[x10] | `FALL_THROUGH`
<a id="insn-00ba2c58"></a> `00ba2c58` | `09 1d 40 f9` | ldr x9,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00ba2c5c"></a> `00ba2c5c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00ba2c60"></a> `00ba2c60` | `2a 01 08 8b` | add x10,x9,x8 | `FALL_THROUGH`
<a id="insn-00ba2c64"></a> `00ba2c64` | `48 01 18 cb` | sub x8,x10,x24 | `FALL_THROUGH`
<a id="insn-00ba2c68"></a> `00ba2c68` | `09 01 80 b9` | ldrsw x9,[x8] | `FALL_THROUGH`
<a id="insn-00ba2c6c"></a> `00ba2c6c` | `09 01 09 cb` | sub x9,x8,x9 | `FALL_THROUGH`
<a id="insn-00ba2c70"></a> `00ba2c70` | `29 09 40 79` | ldrh w9,[x9, #0x4] | `FALL_THROUGH`
<a id="insn-00ba2c74"></a> `00ba2c74` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00ba2c78"></a> `00ba2c78` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00ba2c7c"></a> `00ba2c7c` | `13 01 09 8b` | add x19,x8,x9 | `FALL_THROUGH`
<a id="insn-00ba2c80"></a> `00ba2c80` | `7c 46 40 b8` | ldr w28,[x19], #0x4 | `FALL_THROUGH`
<a id="insn-00ba2c84"></a> `00ba2c84` | `d9 7a 75 b8` | ldr w25,[x22, x21, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00ba2c88"></a> `00ba2c88` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba2c8c"></a> `00ba2c8c` | `fb 03 0a aa` | mov x27,x10 | `FALL_THROUGH`
<a id="insn-00ba2c90"></a> `00ba2c90` | `48 01 19 cb` | sub x8,x10,x25 | `FALL_THROUGH`
<a id="insn-00ba2c94"></a> `00ba2c94` | `09 01 80 b9` | ldrsw x9,[x8] | `FALL_THROUGH`
<a id="insn-00ba2c98"></a> `00ba2c98` | `09 01 09 cb` | sub x9,x8,x9 | `FALL_THROUGH`
<a id="insn-00ba2c9c"></a> `00ba2c9c` | `29 09 40 79` | ldrh w9,[x9, #0x4] | `FALL_THROUGH`
<a id="insn-00ba2ca0"></a> `00ba2ca0` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00ba2ca4"></a> `00ba2ca4` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00ba2ca8"></a> `00ba2ca8` | `01 01 09 8b` | add x1,x8,x9 | `FALL_THROUGH`
<a id="insn-00ba2cac"></a> `00ba2cac` | `3a 44 40 b8` | ldr w26,[x1], #0x4 | `FALL_THROUGH`
<a id="insn-00ba2cb0"></a> `00ba2cb0` | `5f 03 1c 6b` | cmp w26,w28 | `FALL_THROUGH`
<a id="insn-00ba2cb4"></a> `00ba2cb4` | `42 33 9c 1a` | csel w2,w26,w28,cc | `FALL_THROUGH`
<a id="insn-00ba2cb8"></a> `00ba2cb8` | `1a d5 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00ba2cbc"></a> `00ba2cbc` | `9f 03 1a 6b` | cmp w28,w26 | `FALL_THROUGH`
<a id="insn-00ba2cc0"></a> `00ba2cc0` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00ba2cc4"></a> `00ba2cc4` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00ba2cc8"></a> `00ba2cc8` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00ba2ccc"></a> `00ba2ccc` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00ba2cd0"></a> `00ba2cd0` | `e8 00 00 37` | tbnz w8,#0x0,0x00ba2cec | `CONDITIONAL_JUMP`
<a id="insn-00ba2cd4"></a> `00ba2cd4` | `b5 06 00 91` | add x21,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00ba2cd8"></a> `00ba2cd8` | `ff 02 15 eb` | cmp x23,x21 | `FALL_THROUGH`
<a id="insn-00ba2cdc"></a> `00ba2cdc` | `94 12 00 d1` | sub x20,x20,#0x4 | `FALL_THROUGH`
<a id="insn-00ba2ce0"></a> `00ba2ce0` | `ea 03 1b aa` | mov x10,x27 | `FALL_THROUGH`
<a id="insn-00ba2ce4"></a> `00ba2ce4` | `01 fd ff 54` | b.ne 0x00ba2c84 | `CONDITIONAL_JUMP`
<a id="insn-00ba2ce8"></a> `00ba2ce8` | `c3 00 00 14` | b 0x00ba2ff4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba2cec"></a> `00ba2cec` | `fa 23 40 f9` | ldr x26,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ba2cf0"></a> `00ba2cf0` | `e8 02 15 cb` | sub x8,x23,x21 | `FALL_THROUGH`
<a id="insn-00ba2cf4"></a> `00ba2cf4` | `ea 03 17 aa` | mov x10,x23 | `FALL_THROUGH`
<a id="insn-00ba2cf8"></a> `00ba2cf8` | `dc 02 14 cb` | sub x28,x22,x20 | `FALL_THROUGH`
<a id="insn-00ba2cfc"></a> `00ba2cfc` | `1f 01 1a eb` | cmp x8,x26 | `FALL_THROUGH`
<a id="insn-00ba2d00"></a> `00ba2d00` | `fc 0b 00 f9` | str x28,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba2d04"></a> `00ba2d04` | `ca 06 00 54` | b.ge 0x00ba2ddc | `CONDITIONAL_JUMP`
<a id="insn-00ba2d08"></a> `00ba2d08` | `e1 1f 40 f9` | ldr x1,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00ba2d0c"></a> `00ba2d0c` | `5f 03 00 f1` | cmp x26,#0x0 | `FALL_THROUGH`
<a id="insn-00ba2d10"></a> `00ba2d10` | `48 a7 9a 9a` | cinc x8,x26,lt | `FALL_THROUGH`
<a id="insn-00ba2d14"></a> `00ba2d14` | `14 fd 41 93` | asr x20,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ba2d18"></a> `00ba2d18` | `28 00 1c eb` | subs x8,x1,x28 | `FALL_THROUGH`
<a id="insn-00ba2d1c"></a> `00ba2d1c` | `33 08 14 8b` | add x19,x1,x20, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ba2d20"></a> `00ba2d20` | `40 0d 00 54` | b.eq 0x00ba2ec8 | `CONDITIONAL_JUMP`
<a id="insn-00ba2d24"></a> `00ba2d24` | `69 02 40 b9` | ldr w9,[x19] | `FALL_THROUGH`
<a id="insn-00ba2d28"></a> `00ba2d28` | `f4 07 00 f9` | str x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ba2d2c"></a> `00ba2d2c` | `eb 03 1b aa` | mov x11,x27 | `FALL_THROUGH`
<a id="insn-00ba2d30"></a> `00ba2d30` | `14 fd 42 93` | asr x20,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00ba2d34"></a> `00ba2d34` | `69 03 09 cb` | sub x9,x27,x9 | `FALL_THROUGH`
<a id="insn-00ba2d38"></a> `00ba2d38` | `2a 01 80 b9` | ldrsw x10,[x9] | `FALL_THROUGH`
<a id="insn-00ba2d3c"></a> `00ba2d3c` | `2a 01 0a cb` | sub x10,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba2d40"></a> `00ba2d40` | `4a 09 40 79` | ldrh w10,[x10, #0x4] | `FALL_THROUGH`
<a id="insn-00ba2d44"></a> `00ba2d44` | `29 01 0a 8b` | add x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba2d48"></a> `00ba2d48` | `2a 01 40 b9` | ldr w10,[x9] | `FALL_THROUGH`
<a id="insn-00ba2d4c"></a> `00ba2d4c` | `29 01 0a 8b` | add x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba2d50"></a> `00ba2d50` | `36 45 40 b8` | ldr w22,[x9], #0x4 | `FALL_THROUGH`
<a id="insn-00ba2d54"></a> `00ba2d54` | `e9 27 00 f9` | str x9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00ba2d58"></a> `00ba2d58` | `99 fe 41 d3` | lsr x25,x20,#0x1 | `FALL_THROUGH`
<a id="insn-00ba2d5c"></a> `00ba2d5c` | `9a 0b 19 8b` | add x26,x28,x25, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ba2d60"></a> `00ba2d60` | `48 47 40 b8` | ldr w8,[x26], #0x4 | `FALL_THROUGH`
<a id="insn-00ba2d64"></a> `00ba2d64` | `68 01 08 cb` | sub x8,x11,x8 | `FALL_THROUGH`
<a id="insn-00ba2d68"></a> `00ba2d68` | `09 01 80 b9` | ldrsw x9,[x8] | `FALL_THROUGH`
<a id="insn-00ba2d6c"></a> `00ba2d6c` | `09 01 09 cb` | sub x9,x8,x9 | `FALL_THROUGH`
<a id="insn-00ba2d70"></a> `00ba2d70` | `29 09 40 79` | ldrh w9,[x9, #0x4] | `FALL_THROUGH`
<a id="insn-00ba2d74"></a> `00ba2d74` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00ba2d78"></a> `00ba2d78` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00ba2d7c"></a> `00ba2d7c` | `01 01 09 8b` | add x1,x8,x9 | `FALL_THROUGH`
<a id="insn-00ba2d80"></a> `00ba2d80` | `38 44 40 b8` | ldr w24,[x1], #0x4 | `FALL_THROUGH`
<a id="insn-00ba2d84"></a> `00ba2d84` | `e0 27 40 f9` | ldr x0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00ba2d88"></a> `00ba2d88` | `1f 03 16 6b` | cmp w24,w22 | `FALL_THROUGH`
<a id="insn-00ba2d8c"></a> `00ba2d8c` | `02 33 96 1a` | csel w2,w24,w22,cc | `FALL_THROUGH`
<a id="insn-00ba2d90"></a> `00ba2d90` | `e4 d4 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00ba2d94"></a> `00ba2d94` | `df 02 18 6b` | cmp w22,w24 | `FALL_THROUGH`
<a id="insn-00ba2d98"></a> `00ba2d98` | `e9 27 9f 1a` | cset w9,cc | `FALL_THROUGH`
<a id="insn-00ba2d9c"></a> `00ba2d9c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00ba2da0"></a> `00ba2da0` | `ea a7 9f 1a` | cset w10,lt | `FALL_THROUGH`
<a id="insn-00ba2da4"></a> `00ba2da4` | `e8 03 39 aa` | mvn x8,x25 | `FALL_THROUGH`
<a id="insn-00ba2da8"></a> `00ba2da8` | `29 01 8a 1a` | csel w9,w9,w10,eq | `FALL_THROUGH`
<a id="insn-00ba2dac"></a> `00ba2dac` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00ba2db0"></a> `00ba2db0` | `3f 01 00 71` | cmp w9,#0x0 | `FALL_THROUGH`
<a id="insn-00ba2db4"></a> `00ba2db4` | `eb 03 1b aa` | mov x11,x27 | `FALL_THROUGH`
<a id="insn-00ba2db8"></a> `00ba2db8` | `34 13 88 9a` | csel x20,x25,x8,ne | `FALL_THROUGH`
<a id="insn-00ba2dbc"></a> `00ba2dbc` | `9c 13 9a 9a` | csel x28,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00ba2dc0"></a> `00ba2dc0` | `d4 fc ff b5` | cbnz x20,0x00ba2d58 | `CONDITIONAL_JUMP`
<a id="insn-00ba2dc4"></a> `00ba2dc4` | `e8 1b 41 a9` | ldp x8,x6,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba2dc8"></a> `00ba2dc8` | `e7 07 43 a9` | ldp x7,x1,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba2dcc"></a> `00ba2dcc` | `fa 23 40 f9` | ldr x26,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ba2dd0"></a> `00ba2dd0` | `f4 07 40 f9` | ldr x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ba2dd4"></a> `00ba2dd4` | `ea 03 17 aa` | mov x10,x23 | `FALL_THROUGH`
<a id="insn-00ba2dd8"></a> `00ba2dd8` | `3f 00 00 14` | b 0x00ba2ed4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba2ddc"></a> `00ba2ddc` | `49 05 00 d1` | sub x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00ba2de0"></a> `00ba2de0` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00ba2de4"></a> `00ba2de4` | `20 10 00 54` | b.eq 0x00ba2fe8 | `CONDITIONAL_JUMP`
<a id="insn-00ba2de8"></a> `00ba2de8` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00ba2dec"></a> `00ba2dec` | `08 a5 88 9a` | cinc x8,x8,lt | `FALL_THROUGH`
<a id="insn-00ba2df0"></a> `00ba2df0` | `04 fd 41 93` | asr x4,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ba2df4"></a> `00ba2df4` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba2df8"></a> `00ba2df8` | `e1 1f 40 f9` | ldr x1,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00ba2dfc"></a> `00ba2dfc` | `c9 0a 04 8b` | add x9,x22,x4, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ba2e00"></a> `00ba2e00` | `3c 01 14 cb` | sub x28,x9,x20 | `FALL_THROUGH`
<a id="insn-00ba2e04"></a> `00ba2e04` | `08 01 01 eb` | subs x8,x8,x1 | `FALL_THROUGH`
<a id="insn-00ba2e08"></a> `00ba2e08` | `c0 06 00 54` | b.eq 0x00ba2ee0 | `CONDITIONAL_JUMP`
<a id="insn-00ba2e0c"></a> `00ba2e0c` | `29 79 75 b8` | ldr w9,[x9, x21, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00ba2e10"></a> `00ba2e10` | `e4 07 00 f9` | str x4,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ba2e14"></a> `00ba2e14` | `eb 03 1b aa` | mov x11,x27 | `FALL_THROUGH`
<a id="insn-00ba2e18"></a> `00ba2e18` | `16 fd 42 93` | asr x22,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00ba2e1c"></a> `00ba2e1c` | `69 03 09 cb` | sub x9,x27,x9 | `FALL_THROUGH`
<a id="insn-00ba2e20"></a> `00ba2e20` | `2a 01 80 b9` | ldrsw x10,[x9] | `FALL_THROUGH`
<a id="insn-00ba2e24"></a> `00ba2e24` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00ba2e28"></a> `00ba2e28` | `2a 01 0a cb` | sub x10,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba2e2c"></a> `00ba2e2c` | `4a 09 40 79` | ldrh w10,[x10, #0x4] | `FALL_THROUGH`
<a id="insn-00ba2e30"></a> `00ba2e30` | `29 01 0a 8b` | add x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba2e34"></a> `00ba2e34` | `2a 01 40 b9` | ldr w10,[x9] | `FALL_THROUGH`
<a id="insn-00ba2e38"></a> `00ba2e38` | `29 01 0a 8b` | add x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba2e3c"></a> `00ba2e3c` | `34 45 40 b8` | ldr w20,[x9], #0x4 | `FALL_THROUGH`
<a id="insn-00ba2e40"></a> `00ba2e40` | `e9 27 00 f9` | str x9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00ba2e44"></a> `00ba2e44` | `d8 fe 41 d3` | lsr x24,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00ba2e48"></a> `00ba2e48` | `79 0a 18 8b` | add x25,x19,x24, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ba2e4c"></a> `00ba2e4c` | `28 47 40 b8` | ldr w8,[x25], #0x4 | `FALL_THROUGH`
<a id="insn-00ba2e50"></a> `00ba2e50` | `68 01 08 cb` | sub x8,x11,x8 | `FALL_THROUGH`
<a id="insn-00ba2e54"></a> `00ba2e54` | `09 01 80 b9` | ldrsw x9,[x8] | `FALL_THROUGH`
<a id="insn-00ba2e58"></a> `00ba2e58` | `09 01 09 cb` | sub x9,x8,x9 | `FALL_THROUGH`
<a id="insn-00ba2e5c"></a> `00ba2e5c` | `29 09 40 79` | ldrh w9,[x9, #0x4] | `FALL_THROUGH`
<a id="insn-00ba2e60"></a> `00ba2e60` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00ba2e64"></a> `00ba2e64` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00ba2e68"></a> `00ba2e68` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00ba2e6c"></a> `00ba2e6c` | `1a 44 40 b8` | ldr w26,[x0], #0x4 | `FALL_THROUGH`
<a id="insn-00ba2e70"></a> `00ba2e70` | `e1 27 40 f9` | ldr x1,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00ba2e74"></a> `00ba2e74` | `9f 02 1a 6b` | cmp w20,w26 | `FALL_THROUGH`
<a id="insn-00ba2e78"></a> `00ba2e78` | `82 32 9a 1a` | csel w2,w20,w26,cc | `FALL_THROUGH`
<a id="insn-00ba2e7c"></a> `00ba2e7c` | `a9 d4 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00ba2e80"></a> `00ba2e80` | `5f 03 14 6b` | cmp w26,w20 | `FALL_THROUGH`
<a id="insn-00ba2e84"></a> `00ba2e84` | `e9 27 9f 1a` | cset w9,cc | `FALL_THROUGH`
<a id="insn-00ba2e88"></a> `00ba2e88` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00ba2e8c"></a> `00ba2e8c` | `ea a7 9f 1a` | cset w10,lt | `FALL_THROUGH`
<a id="insn-00ba2e90"></a> `00ba2e90` | `e8 03 38 aa` | mvn x8,x24 | `FALL_THROUGH`
<a id="insn-00ba2e94"></a> `00ba2e94` | `29 01 8a 1a` | csel w9,w9,w10,eq | `FALL_THROUGH`
<a id="insn-00ba2e98"></a> `00ba2e98` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00ba2e9c"></a> `00ba2e9c` | `3f 01 00 71` | cmp w9,#0x0 | `FALL_THROUGH`
<a id="insn-00ba2ea0"></a> `00ba2ea0` | `eb 03 1b aa` | mov x11,x27 | `FALL_THROUGH`
<a id="insn-00ba2ea4"></a> `00ba2ea4` | `16 11 98 9a` | csel x22,x8,x24,ne | `FALL_THROUGH`
<a id="insn-00ba2ea8"></a> `00ba2ea8` | `33 13 93 9a` | csel x19,x25,x19,ne | `FALL_THROUGH`
<a id="insn-00ba2eac"></a> `00ba2eac` | `d6 fc ff b5` | cbnz x22,0x00ba2e44 | `CONDITIONAL_JUMP`
<a id="insn-00ba2eb0"></a> `00ba2eb0` | `e6 0f 40 f9` | ldr x6,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ba2eb4"></a> `00ba2eb4` | `e7 07 43 a9` | ldp x7,x1,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba2eb8"></a> `00ba2eb8` | `fa 23 40 f9` | ldr x26,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ba2ebc"></a> `00ba2ebc` | `e4 07 40 f9` | ldr x4,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ba2ec0"></a> `00ba2ec0` | `ea 03 17 aa` | mov x10,x23 | `FALL_THROUGH`
<a id="insn-00ba2ec4"></a> `00ba2ec4` | `0a 00 00 14` | b 0x00ba2eec | `UNCONDITIONAL_JUMP`
<a id="insn-00ba2ec8"></a> `00ba2ec8` | `e7 1b 40 f9` | ldr x7,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba2ecc"></a> `00ba2ecc` | `e6 0f 40 f9` | ldr x6,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ba2ed0"></a> `00ba2ed0` | `e8 03 1c aa` | mov x8,x28 | `FALL_THROUGH`
<a id="insn-00ba2ed4"></a> `00ba2ed4` | `88 03 08 cb` | sub x8,x28,x8 | `FALL_THROUGH`
<a id="insn-00ba2ed8"></a> `00ba2ed8` | `04 fd 42 93` | asr x4,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00ba2edc"></a> `00ba2edc` | `06 00 00 14` | b 0x00ba2ef4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba2ee0"></a> `00ba2ee0` | `e7 1b 40 f9` | ldr x7,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba2ee4"></a> `00ba2ee4` | `e6 0f 40 f9` | ldr x6,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ba2ee8"></a> `00ba2ee8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00ba2eec"></a> `00ba2eec` | `68 02 01 cb` | sub x8,x19,x1 | `FALL_THROUGH`
<a id="insn-00ba2ef0"></a> `00ba2ef0` | `14 fd 42 93` | asr x20,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00ba2ef4"></a> `00ba2ef4` | `48 01 04 cb` | sub x8,x10,x4 | `FALL_THROUGH`
<a id="insn-00ba2ef8"></a> `00ba2ef8` | `9f 03 01 eb` | cmp x28,x1 | `FALL_THROUGH`
<a id="insn-00ba2efc"></a> `00ba2efc` | `1b 01 15 cb` | sub x27,x8,x21 | `FALL_THROUGH`
<a id="insn-00ba2f00"></a> `00ba2f00` | `59 03 14 cb` | sub x25,x26,x20 | `FALL_THROUGH`
<a id="insn-00ba2f04"></a> `00ba2f04` | `f6 03 13 aa` | mov x22,x19 | `FALL_THROUGH`
<a id="insn-00ba2f08"></a> `00ba2f08` | `c0 01 00 54` | b.eq 0x00ba2f40 | `CONDITIONAL_JUMP`
<a id="insn-00ba2f0c"></a> `00ba2f0c` | `3f 00 13 eb` | cmp x1,x19 | `FALL_THROUGH`
<a id="insn-00ba2f10"></a> `00ba2f10` | `f6 03 1c aa` | mov x22,x28 | `FALL_THROUGH`
<a id="insn-00ba2f14"></a> `00ba2f14` | `60 01 00 54` | b.eq 0x00ba2f40 | `CONDITIONAL_JUMP`
<a id="insn-00ba2f18"></a> `00ba2f18` | `e0 03 1c aa` | mov x0,x28 | `FALL_THROUGH`
<a id="insn-00ba2f1c"></a> `00ba2f1c` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00ba2f20"></a> `00ba2f20` | `f6 03 04 aa` | mov x22,x4 | `FALL_THROUGH`
<a id="insn-00ba2f24"></a> `00ba2f24` | `f8 03 07 aa` | mov x24,x7 | `FALL_THROUGH`
<a id="insn-00ba2f28"></a> `00ba2f28` | `ae 01 00 94` | bl 0x00ba35e0 | `UNCONDITIONAL_CALL`
<a id="insn-00ba2f2c"></a> `00ba2f2c` | `e6 0f 40 f9` | ldr x6,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ba2f30"></a> `00ba2f30` | `e7 03 18 aa` | mov x7,x24 | `FALL_THROUGH`
<a id="insn-00ba2f34"></a> `00ba2f34` | `e4 03 16 aa` | mov x4,x22 | `FALL_THROUGH`
<a id="insn-00ba2f38"></a> `00ba2f38` | `ea 03 17 aa` | mov x10,x23 | `FALL_THROUGH`
<a id="insn-00ba2f3c"></a> `00ba2f3c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00ba2f40"></a> `00ba2f40` | `88 02 04 8b` | add x8,x20,x4 | `FALL_THROUGH`
<a id="insn-00ba2f44"></a> `00ba2f44` | `49 03 0a 8b` | add x9,x26,x10 | `FALL_THROUGH`
<a id="insn-00ba2f48"></a> `00ba2f48` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-00ba2f4c"></a> `00ba2f4c` | `29 01 15 cb` | sub x9,x9,x21 | `FALL_THROUGH`
<a id="insn-00ba2f50"></a> `00ba2f50` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ba2f54"></a> `00ba2f54` | `0a 01 00 54` | b.ge 0x00ba2f74 | `CONDITIONAL_JUMP`
<a id="insn-00ba2f58"></a> `00ba2f58` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba2f5c"></a> `00ba2f5c` | `e3 17 40 f9` | ldr x3,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00ba2f60"></a> `00ba2f60` | `e1 03 1c aa` | mov x1,x28 | `FALL_THROUGH`
<a id="insn-00ba2f64"></a> `00ba2f64` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00ba2f68"></a> `00ba2f68` | `e5 03 14 aa` | mov x5,x20 | `FALL_THROUGH`
<a id="insn-00ba2f6c"></a> `00ba2f6c` | `41 e7 02 94` | bl 0x00c5cc70 | `UNCONDITIONAL_CALL`
<a id="insn-00ba2f70"></a> `00ba2f70` | `0d 00 00 14` | b 0x00ba2fa4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba2f74"></a> `00ba2f74` | `e2 0f 42 a9` | ldp x2,x3,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba2f78"></a> `00ba2f78` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00ba2f7c"></a> `00ba2f7c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00ba2f80"></a> `00ba2f80` | `f3 03 04 aa` | mov x19,x4 | `FALL_THROUGH`
<a id="insn-00ba2f84"></a> `00ba2f84` | `e4 03 1b aa` | mov x4,x27 | `FALL_THROUGH`
<a id="insn-00ba2f88"></a> `00ba2f88` | `e5 03 19 aa` | mov x5,x25 | `FALL_THROUGH`
<a id="insn-00ba2f8c"></a> `00ba2f8c` | `39 e7 02 94` | bl 0x00c5cc70 | `UNCONDITIONAL_CALL`
<a id="insn-00ba2f90"></a> `00ba2f90` | `f6 13 00 f9` | str x22,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba2f94"></a> `00ba2f94` | `f6 0b 40 f9` | ldr x22,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba2f98"></a> `00ba2f98` | `f9 03 14 aa` | mov x25,x20 | `FALL_THROUGH`
<a id="insn-00ba2f9c"></a> `00ba2f9c` | `fb 03 13 aa` | mov x27,x19 | `FALL_THROUGH`
<a id="insn-00ba2fa0"></a> `00ba2fa0` | `f3 03 1c aa` | mov x19,x28 | `FALL_THROUGH`
<a id="insn-00ba2fa4"></a> `00ba2fa4` | `f7 03 1b aa` | mov x23,x27 | `FALL_THROUGH`
<a id="insn-00ba2fa8"></a> `00ba2fa8` | `f3 e7 03 a9` | stp x19,x25,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00ba2fac"></a> `00ba2fac` | `d9 e3 ff b5` | cbnz x25,0x00ba2c24 | `CONDITIONAL_JUMP`
<a id="insn-00ba2fb0"></a> `00ba2fb0` | `11 00 00 14` | b 0x00ba2ff4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba2fb4"></a> `00ba2fb4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00ba2fb8"></a> `00ba2fb8` | `e1 1f 40 f9` | ldr x1,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00ba2fbc"></a> `00ba2fbc` | `e2 0f 42 a9` | ldp x2,x3,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba2fc0"></a> `00ba2fc0` | `e4 03 17 aa` | mov x4,x23 | `FALL_THROUGH`
<a id="insn-00ba2fc4"></a> `00ba2fc4` | `e6 0f 40 f9` | ldr x6,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ba2fc8"></a> `00ba2fc8` | `fd 7b 4a a9` | ldp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00ba2fcc"></a> `00ba2fcc` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00ba2fd0"></a> `00ba2fd0` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00ba2fd4"></a> `00ba2fd4` | `f8 5f 47 a9` | ldp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ba2fd8"></a> `00ba2fd8` | `fa 67 46 a9` | ldp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ba2fdc"></a> `00ba2fdc` | `fc 6f 45 a9` | ldp x28,x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ba2fe0"></a> `00ba2fe0` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00ba2fe4"></a> `00ba2fe4` | `93 e7 02 14` | b 0x00c5ce30 | `CALL_TERMINATOR`
<a id="insn-00ba2fe8"></a> `00ba2fe8` | `e8 1f 40 f9` | ldr x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00ba2fec"></a> `00ba2fec` | `d8 7a 35 b8` | str w24,[x22, x21, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00ba2ff0"></a> `00ba2ff0` | `19 01 00 b9` | str w25,[x8] | `FALL_THROUGH`
<a id="insn-00ba2ff4"></a> `00ba2ff4` | `fd 7b 4a a9` | ldp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00ba2ff8"></a> `00ba2ff8` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00ba2ffc"></a> `00ba2ffc` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00ba3000"></a> `00ba3000` | `f8 5f 47 a9` | ldp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ba3004"></a> `00ba3004` | `fa 67 46 a9` | ldp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ba3008"></a> `00ba3008` | `fc 6f 45 a9` | ldp x28,x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ba300c"></a> `00ba300c` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00ba3010"></a> `00ba3010` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ba2bec`](#insn-00ba2bec) 範囲 `[['00ba2bec', '00ba2c1b']]`
  - `CONDITIONAL_JUMP` [`00ba2c18`](#insn-00ba2c18) → [`00ba2ff4`](#insn-00ba2ff4)
  - `FALL_THROUGH` [`00ba2c18`](#insn-00ba2c18) → [`00ba2c1c`](#insn-00ba2c1c)
- ブロック [`00ba2c1c`](#insn-00ba2c1c) 範囲 `[['00ba2c1c', '00ba2c23']]`
  - `FALL_THROUGH` [`00ba2c20`](#insn-00ba2c20) → [`00ba2c24`](#insn-00ba2c24)
- ブロック [`00ba2c24`](#insn-00ba2c24) 範囲 `[['00ba2c24', '00ba2c33']]`
  - `CONDITIONAL_JUMP` [`00ba2c30`](#insn-00ba2c30) → [`00ba2fb4`](#insn-00ba2fb4)
  - `FALL_THROUGH` [`00ba2c30`](#insn-00ba2c30) → [`00ba2c34`](#insn-00ba2c34)
- ブロック [`00ba2c34`](#insn-00ba2c34) 範囲 `[['00ba2c34', '00ba2c3b']]`
  - `CONDITIONAL_JUMP` [`00ba2c38`](#insn-00ba2c38) → [`00ba2fb4`](#insn-00ba2fb4)
  - `FALL_THROUGH` [`00ba2c38`](#insn-00ba2c38) → [`00ba2c3c`](#insn-00ba2c3c)
- ブロック [`00ba2c3c`](#insn-00ba2c3c) 範囲 `[['00ba2c3c', '00ba2c3f']]`
  - `CONDITIONAL_JUMP` [`00ba2c3c`](#insn-00ba2c3c) → [`00ba2ff4`](#insn-00ba2ff4)
  - `FALL_THROUGH` [`00ba2c3c`](#insn-00ba2c3c) → [`00ba2c40`](#insn-00ba2c40)
- ブロック [`00ba2c40`](#insn-00ba2c40) 範囲 `[['00ba2c40', '00ba2c83']]`
  - `FALL_THROUGH` [`00ba2c80`](#insn-00ba2c80) → [`00ba2c84`](#insn-00ba2c84)
- ブロック [`00ba2c84`](#insn-00ba2c84) 範囲 `[['00ba2c84', '00ba2cd3']]`
  - `CONDITIONAL_JUMP` [`00ba2cd0`](#insn-00ba2cd0) → [`00ba2cec`](#insn-00ba2cec)
  - `FALL_THROUGH` [`00ba2cd0`](#insn-00ba2cd0) → [`00ba2cd4`](#insn-00ba2cd4)
- ブロック [`00ba2cd4`](#insn-00ba2cd4) 範囲 `[['00ba2cd4', '00ba2ce7']]`
  - `CONDITIONAL_JUMP` [`00ba2ce4`](#insn-00ba2ce4) → [`00ba2c84`](#insn-00ba2c84)
  - `FALL_THROUGH` [`00ba2ce4`](#insn-00ba2ce4) → [`00ba2ce8`](#insn-00ba2ce8)
- ブロック [`00ba2ce8`](#insn-00ba2ce8) 範囲 `[['00ba2ce8', '00ba2ceb']]`
  - `UNCONDITIONAL_JUMP` [`00ba2ce8`](#insn-00ba2ce8) → [`00ba2ff4`](#insn-00ba2ff4)
- ブロック [`00ba2cec`](#insn-00ba2cec) 範囲 `[['00ba2cec', '00ba2d07']]`
  - `CONDITIONAL_JUMP` [`00ba2d04`](#insn-00ba2d04) → [`00ba2ddc`](#insn-00ba2ddc)
  - `FALL_THROUGH` [`00ba2d04`](#insn-00ba2d04) → [`00ba2d08`](#insn-00ba2d08)
- ブロック [`00ba2d08`](#insn-00ba2d08) 範囲 `[['00ba2d08', '00ba2d23']]`
  - `CONDITIONAL_JUMP` [`00ba2d20`](#insn-00ba2d20) → [`00ba2ec8`](#insn-00ba2ec8)
  - `FALL_THROUGH` [`00ba2d20`](#insn-00ba2d20) → [`00ba2d24`](#insn-00ba2d24)
- ブロック [`00ba2d24`](#insn-00ba2d24) 範囲 `[['00ba2d24', '00ba2d57']]`
  - `FALL_THROUGH` [`00ba2d54`](#insn-00ba2d54) → [`00ba2d58`](#insn-00ba2d58)
- ブロック [`00ba2d58`](#insn-00ba2d58) 範囲 `[['00ba2d58', '00ba2dc3']]`
  - `CONDITIONAL_JUMP` [`00ba2dc0`](#insn-00ba2dc0) → [`00ba2d58`](#insn-00ba2d58)
  - `FALL_THROUGH` [`00ba2dc0`](#insn-00ba2dc0) → [`00ba2dc4`](#insn-00ba2dc4)
- ブロック [`00ba2dc4`](#insn-00ba2dc4) 範囲 `[['00ba2dc4', '00ba2ddb']]`
  - `UNCONDITIONAL_JUMP` [`00ba2dd8`](#insn-00ba2dd8) → [`00ba2ed4`](#insn-00ba2ed4)
- ブロック [`00ba2ddc`](#insn-00ba2ddc) 範囲 `[['00ba2ddc', '00ba2de7']]`
  - `CONDITIONAL_JUMP` [`00ba2de4`](#insn-00ba2de4) → [`00ba2fe8`](#insn-00ba2fe8)
  - `FALL_THROUGH` [`00ba2de4`](#insn-00ba2de4) → [`00ba2de8`](#insn-00ba2de8)
- ブロック [`00ba2de8`](#insn-00ba2de8) 範囲 `[['00ba2de8', '00ba2e0b']]`
  - `CONDITIONAL_JUMP` [`00ba2e08`](#insn-00ba2e08) → [`00ba2ee0`](#insn-00ba2ee0)
  - `FALL_THROUGH` [`00ba2e08`](#insn-00ba2e08) → [`00ba2e0c`](#insn-00ba2e0c)
- ブロック [`00ba2e0c`](#insn-00ba2e0c) 範囲 `[['00ba2e0c', '00ba2e43']]`
  - `FALL_THROUGH` [`00ba2e40`](#insn-00ba2e40) → [`00ba2e44`](#insn-00ba2e44)
- ブロック [`00ba2e44`](#insn-00ba2e44) 範囲 `[['00ba2e44', '00ba2eaf']]`
  - `CONDITIONAL_JUMP` [`00ba2eac`](#insn-00ba2eac) → [`00ba2e44`](#insn-00ba2e44)
  - `FALL_THROUGH` [`00ba2eac`](#insn-00ba2eac) → [`00ba2eb0`](#insn-00ba2eb0)
- ブロック [`00ba2eb0`](#insn-00ba2eb0) 範囲 `[['00ba2eb0', '00ba2ec7']]`
  - `UNCONDITIONAL_JUMP` [`00ba2ec4`](#insn-00ba2ec4) → [`00ba2eec`](#insn-00ba2eec)
- ブロック [`00ba2ec8`](#insn-00ba2ec8) 範囲 `[['00ba2ec8', '00ba2ed3']]`
  - `FALL_THROUGH` [`00ba2ed0`](#insn-00ba2ed0) → [`00ba2ed4`](#insn-00ba2ed4)
- ブロック [`00ba2ed4`](#insn-00ba2ed4) 範囲 `[['00ba2ed4', '00ba2edf']]`
  - `UNCONDITIONAL_JUMP` [`00ba2edc`](#insn-00ba2edc) → [`00ba2ef4`](#insn-00ba2ef4)
- ブロック [`00ba2ee0`](#insn-00ba2ee0) 範囲 `[['00ba2ee0', '00ba2eeb']]`
  - `FALL_THROUGH` [`00ba2ee8`](#insn-00ba2ee8) → [`00ba2eec`](#insn-00ba2eec)
- ブロック [`00ba2eec`](#insn-00ba2eec) 範囲 `[['00ba2eec', '00ba2ef3']]`
  - `FALL_THROUGH` [`00ba2ef0`](#insn-00ba2ef0) → [`00ba2ef4`](#insn-00ba2ef4)
- ブロック [`00ba2ef4`](#insn-00ba2ef4) 範囲 `[['00ba2ef4', '00ba2f0b']]`
  - `CONDITIONAL_JUMP` [`00ba2f08`](#insn-00ba2f08) → [`00ba2f40`](#insn-00ba2f40)
  - `FALL_THROUGH` [`00ba2f08`](#insn-00ba2f08) → [`00ba2f0c`](#insn-00ba2f0c)
- ブロック [`00ba2f0c`](#insn-00ba2f0c) 範囲 `[['00ba2f0c', '00ba2f17']]`
  - `CONDITIONAL_JUMP` [`00ba2f14`](#insn-00ba2f14) → [`00ba2f40`](#insn-00ba2f40)
  - `FALL_THROUGH` [`00ba2f14`](#insn-00ba2f14) → [`00ba2f18`](#insn-00ba2f18)
- ブロック [`00ba2f18`](#insn-00ba2f18) 範囲 `[['00ba2f18', '00ba2f3f']]`
  - `FALL_THROUGH` [`00ba2f3c`](#insn-00ba2f3c) → [`00ba2f40`](#insn-00ba2f40)
- ブロック [`00ba2f40`](#insn-00ba2f40) 範囲 `[['00ba2f40', '00ba2f57']]`
  - `CONDITIONAL_JUMP` [`00ba2f54`](#insn-00ba2f54) → [`00ba2f74`](#insn-00ba2f74)
  - `FALL_THROUGH` [`00ba2f54`](#insn-00ba2f54) → [`00ba2f58`](#insn-00ba2f58)
- ブロック [`00ba2f58`](#insn-00ba2f58) 範囲 `[['00ba2f58', '00ba2f73']]`
  - `UNCONDITIONAL_JUMP` [`00ba2f70`](#insn-00ba2f70) → [`00ba2fa4`](#insn-00ba2fa4)
- ブロック [`00ba2f74`](#insn-00ba2f74) 範囲 `[['00ba2f74', '00ba2fa3']]`
  - `FALL_THROUGH` [`00ba2fa0`](#insn-00ba2fa0) → [`00ba2fa4`](#insn-00ba2fa4)
- ブロック [`00ba2fa4`](#insn-00ba2fa4) 範囲 `[['00ba2fa4', '00ba2faf']]`
  - `CONDITIONAL_JUMP` [`00ba2fac`](#insn-00ba2fac) → [`00ba2c24`](#insn-00ba2c24)
  - `FALL_THROUGH` [`00ba2fac`](#insn-00ba2fac) → [`00ba2fb0`](#insn-00ba2fb0)
- ブロック [`00ba2fb0`](#insn-00ba2fb0) 範囲 `[['00ba2fb0', '00ba2fb3']]`
  - `UNCONDITIONAL_JUMP` [`00ba2fb0`](#insn-00ba2fb0) → [`00ba2ff4`](#insn-00ba2ff4)
- ブロック [`00ba2fb4`](#insn-00ba2fb4) 範囲 `[['00ba2fb4', '00ba2fe7']]`
- ブロック [`00ba2fe8`](#insn-00ba2fe8) 範囲 `[['00ba2fe8', '00ba2ff3']]`
  - `FALL_THROUGH` [`00ba2ff0`](#insn-00ba2ff0) → [`00ba2ff4`](#insn-00ba2ff4)
- ブロック [`00ba2ff4`](#insn-00ba2ff4) 範囲 `[['00ba2ff4', '00ba3013']]`

## 命令位置別の参照

- [`00ba2bf0`](#insn-00ba2bf0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2bf4`](#insn-00ba2bf4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2bf8`](#insn-00ba2bf8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2bfc`](#insn-00ba2bfc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2c00`](#insn-00ba2c00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2c04`](#insn-00ba2c04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2c0c`](#insn-00ba2c0c) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2c10`](#insn-00ba2c10) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2c14`](#insn-00ba2c14) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2c18`](#insn-00ba2c18) → [`00ba2ff4`](#insn-00ba2ff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2c24`](#insn-00ba2c24) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2c28`](#insn-00ba2c28) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2c30`](#insn-00ba2c30) → [`00ba2fb4`](#insn-00ba2fb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2c38`](#insn-00ba2c38) → [`00ba2fb4`](#insn-00ba2fb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2c3c`](#insn-00ba2c3c) → [`00ba2ff4`](#insn-00ba2ff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2c40`](#insn-00ba2c40) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2c44`](#insn-00ba2c44) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2cb8`](#insn-00ba2cb8) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00ba2cd0`](#insn-00ba2cd0) → [`00ba2cec`](#insn-00ba2cec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2ce4`](#insn-00ba2ce4) → [`00ba2c84`](#insn-00ba2c84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2ce8`](#insn-00ba2ce8) → [`00ba2ff4`](#insn-00ba2ff4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2cec`](#insn-00ba2cec) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2d00`](#insn-00ba2d00) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2d04`](#insn-00ba2d04) → [`00ba2ddc`](#insn-00ba2ddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2d08`](#insn-00ba2d08) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2d20`](#insn-00ba2d20) → [`00ba2ec8`](#insn-00ba2ec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2d28`](#insn-00ba2d28) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2d54`](#insn-00ba2d54) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2d84`](#insn-00ba2d84) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2d90`](#insn-00ba2d90) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00ba2dc0`](#insn-00ba2dc0) → [`00ba2d58`](#insn-00ba2d58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2dc4`](#insn-00ba2dc4) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2dc8`](#insn-00ba2dc8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2dcc`](#insn-00ba2dcc) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2dd0`](#insn-00ba2dd0) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2dd8`](#insn-00ba2dd8) → [`00ba2ed4`](#insn-00ba2ed4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2de4`](#insn-00ba2de4) → [`00ba2fe8`](#insn-00ba2fe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2df4`](#insn-00ba2df4) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2df8`](#insn-00ba2df8) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2e08`](#insn-00ba2e08) → [`00ba2ee0`](#insn-00ba2ee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2e10`](#insn-00ba2e10) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2e40`](#insn-00ba2e40) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2e70`](#insn-00ba2e70) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2e7c`](#insn-00ba2e7c) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00ba2eac`](#insn-00ba2eac) → [`00ba2e44`](#insn-00ba2e44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2eb0`](#insn-00ba2eb0) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2eb4`](#insn-00ba2eb4) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2eb8`](#insn-00ba2eb8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2ebc`](#insn-00ba2ebc) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2ec4`](#insn-00ba2ec4) → [`00ba2eec`](#insn-00ba2eec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2ec8`](#insn-00ba2ec8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2ecc`](#insn-00ba2ecc) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2edc`](#insn-00ba2edc) → [`00ba2ef4`](#insn-00ba2ef4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2ee0`](#insn-00ba2ee0) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2ee4`](#insn-00ba2ee4) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f08`](#insn-00ba2f08) → [`00ba2f40`](#insn-00ba2f40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f14`](#insn-00ba2f14) → [`00ba2f40`](#insn-00ba2f40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f28`](#insn-00ba2f28) → [`00ba35e0`](../00ba3/00ba35e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba35e0` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f2c`](#insn-00ba2f2c) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f54`](#insn-00ba2f54) → [`00ba2f74`](#insn-00ba2f74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f58`](#insn-00ba2f58) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f5c`](#insn-00ba2f5c) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f6c`](#insn-00ba2f6c) → [`00c5cc70`](../00c5c/00c5cc70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cc70` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f70`](#insn-00ba2f70) → [`00ba2fa4`](#insn-00ba2fa4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f74`](#insn-00ba2f74) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f8c`](#insn-00ba2f8c) → [`00c5cc70`](../00c5c/00c5cc70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cc70` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f90`](#insn-00ba2f90) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2f94`](#insn-00ba2f94) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2fa8`](#insn-00ba2fa8) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2fac`](#insn-00ba2fac) → [`00ba2c24`](#insn-00ba2c24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2fb0`](#insn-00ba2fb0) → [`00ba2ff4`](#insn-00ba2ff4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2fb8`](#insn-00ba2fb8) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2fbc`](#insn-00ba2fbc) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2fc4`](#insn-00ba2fc4) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2fc8`](#insn-00ba2fc8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2fcc`](#insn-00ba2fcc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2fd0`](#insn-00ba2fd0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2fd4`](#insn-00ba2fd4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2fd8`](#insn-00ba2fd8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2fdc`](#insn-00ba2fdc) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2fe4`](#insn-00ba2fe4) → [`00c5ce30`](../00c5c/00c5ce30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ce30` · 推定シンボル `None` · 推定型 `None`
- [`00ba2fe8`](#insn-00ba2fe8) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2ff4`](#insn-00ba2ff4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2ff8`](#insn-00ba2ff8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba2ffc`](#insn-00ba2ffc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba3000`](#insn-00ba3000) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba3004`](#insn-00ba3004) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba3008`](#insn-00ba3008) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ba2bf0`](#insn-00ba2bf0)

~~~json
{
  "source": "00ba2bf0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2bf4`](#insn-00ba2bf4)

~~~json
{
  "source": "00ba2bf4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2bf8`](#insn-00ba2bf8)

~~~json
{
  "source": "00ba2bf8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2bfc`](#insn-00ba2bfc)

~~~json
{
  "source": "00ba2bfc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2c00`](#insn-00ba2c00)

~~~json
{
  "source": "00ba2c00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2c04`](#insn-00ba2c04)

~~~json
{
  "source": "00ba2c04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2c0c`](#insn-00ba2c0c)

~~~json
{
  "source": "00ba2c0c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2c10`](#insn-00ba2c10)

~~~json
{
  "source": "00ba2c10",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2c14`](#insn-00ba2c14)

~~~json
{
  "source": "00ba2c14",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2c18`](#insn-00ba2c18)

~~~json
{
  "source": "00ba2c18",
  "target": "00ba2ff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2c24`](#insn-00ba2c24)

~~~json
{
  "source": "00ba2c24",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2c28`](#insn-00ba2c28)

~~~json
{
  "source": "00ba2c28",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2c30`](#insn-00ba2c30)

~~~json
{
  "source": "00ba2c30",
  "target": "00ba2fb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2c38`](#insn-00ba2c38)

~~~json
{
  "source": "00ba2c38",
  "target": "00ba2fb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2c3c`](#insn-00ba2c3c)

~~~json
{
  "source": "00ba2c3c",
  "target": "00ba2ff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2c40`](#insn-00ba2c40)

~~~json
{
  "source": "00ba2c40",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2c44`](#insn-00ba2c44)

~~~json
{
  "source": "00ba2c44",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2cb8`](#insn-00ba2cb8)

~~~json
{
  "source": "00ba2cb8",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba2cd0`](#insn-00ba2cd0)

~~~json
{
  "source": "00ba2cd0",
  "target": "00ba2cec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2ce4`](#insn-00ba2ce4)

~~~json
{
  "source": "00ba2ce4",
  "target": "00ba2c84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2ce8`](#insn-00ba2ce8)

~~~json
{
  "source": "00ba2ce8",
  "target": "00ba2ff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2cec`](#insn-00ba2cec)

~~~json
{
  "source": "00ba2cec",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2d00`](#insn-00ba2d00)

~~~json
{
  "source": "00ba2d00",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2d04`](#insn-00ba2d04)

~~~json
{
  "source": "00ba2d04",
  "target": "00ba2ddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2d08`](#insn-00ba2d08)

~~~json
{
  "source": "00ba2d08",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2d20`](#insn-00ba2d20)

~~~json
{
  "source": "00ba2d20",
  "target": "00ba2ec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2d28`](#insn-00ba2d28)

~~~json
{
  "source": "00ba2d28",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2d54`](#insn-00ba2d54)

~~~json
{
  "source": "00ba2d54",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2d84`](#insn-00ba2d84)

~~~json
{
  "source": "00ba2d84",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2d90`](#insn-00ba2d90)

~~~json
{
  "source": "00ba2d90",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba2dc0`](#insn-00ba2dc0)

~~~json
{
  "source": "00ba2dc0",
  "target": "00ba2d58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2dc4`](#insn-00ba2dc4)

~~~json
{
  "source": "00ba2dc4",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2dc8`](#insn-00ba2dc8)

~~~json
{
  "source": "00ba2dc8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2dcc`](#insn-00ba2dcc)

~~~json
{
  "source": "00ba2dcc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2dd0`](#insn-00ba2dd0)

~~~json
{
  "source": "00ba2dd0",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2dd8`](#insn-00ba2dd8)

~~~json
{
  "source": "00ba2dd8",
  "target": "00ba2ed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2de4`](#insn-00ba2de4)

~~~json
{
  "source": "00ba2de4",
  "target": "00ba2fe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2df4`](#insn-00ba2df4)

~~~json
{
  "source": "00ba2df4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2df8`](#insn-00ba2df8)

~~~json
{
  "source": "00ba2df8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2e08`](#insn-00ba2e08)

~~~json
{
  "source": "00ba2e08",
  "target": "00ba2ee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2e10`](#insn-00ba2e10)

~~~json
{
  "source": "00ba2e10",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2e40`](#insn-00ba2e40)

~~~json
{
  "source": "00ba2e40",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2e70`](#insn-00ba2e70)

~~~json
{
  "source": "00ba2e70",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2e7c`](#insn-00ba2e7c)

~~~json
{
  "source": "00ba2e7c",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba2eac`](#insn-00ba2eac)

~~~json
{
  "source": "00ba2eac",
  "target": "00ba2e44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2eb0`](#insn-00ba2eb0)

~~~json
{
  "source": "00ba2eb0",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2eb4`](#insn-00ba2eb4)

~~~json
{
  "source": "00ba2eb4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2eb8`](#insn-00ba2eb8)

~~~json
{
  "source": "00ba2eb8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2ebc`](#insn-00ba2ebc)

~~~json
{
  "source": "00ba2ebc",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2ec4`](#insn-00ba2ec4)

~~~json
{
  "source": "00ba2ec4",
  "target": "00ba2eec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2ec8`](#insn-00ba2ec8)

~~~json
{
  "source": "00ba2ec8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2ecc`](#insn-00ba2ecc)

~~~json
{
  "source": "00ba2ecc",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2edc`](#insn-00ba2edc)

~~~json
{
  "source": "00ba2edc",
  "target": "00ba2ef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2ee0`](#insn-00ba2ee0)

~~~json
{
  "source": "00ba2ee0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2ee4`](#insn-00ba2ee4)

~~~json
{
  "source": "00ba2ee4",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2f08`](#insn-00ba2f08)

~~~json
{
  "source": "00ba2f08",
  "target": "00ba2f40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2f14`](#insn-00ba2f14)

~~~json
{
  "source": "00ba2f14",
  "target": "00ba2f40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2f28`](#insn-00ba2f28)

~~~json
{
  "source": "00ba2f28",
  "target": "00ba35e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba2f2c`](#insn-00ba2f2c)

~~~json
{
  "source": "00ba2f2c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2f54`](#insn-00ba2f54)

~~~json
{
  "source": "00ba2f54",
  "target": "00ba2f74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2f58`](#insn-00ba2f58)

~~~json
{
  "source": "00ba2f58",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2f5c`](#insn-00ba2f5c)

~~~json
{
  "source": "00ba2f5c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2f6c`](#insn-00ba2f6c)

~~~json
{
  "source": "00ba2f6c",
  "target": "00c5cc70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba2f70`](#insn-00ba2f70)

~~~json
{
  "source": "00ba2f70",
  "target": "00ba2fa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2f74`](#insn-00ba2f74)

~~~json
{
  "source": "00ba2f74",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2f8c`](#insn-00ba2f8c)

~~~json
{
  "source": "00ba2f8c",
  "target": "00c5cc70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba2f90`](#insn-00ba2f90)

~~~json
{
  "source": "00ba2f90",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2f94`](#insn-00ba2f94)

~~~json
{
  "source": "00ba2f94",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2fa8`](#insn-00ba2fa8)

~~~json
{
  "source": "00ba2fa8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2fac`](#insn-00ba2fac)

~~~json
{
  "source": "00ba2fac",
  "target": "00ba2c24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2fb0`](#insn-00ba2fb0)

~~~json
{
  "source": "00ba2fb0",
  "target": "00ba2ff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2fb8`](#insn-00ba2fb8)

~~~json
{
  "source": "00ba2fb8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2fbc`](#insn-00ba2fbc)

~~~json
{
  "source": "00ba2fbc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2fc4`](#insn-00ba2fc4)

~~~json
{
  "source": "00ba2fc4",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2fc8`](#insn-00ba2fc8)

~~~json
{
  "source": "00ba2fc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2fcc`](#insn-00ba2fcc)

~~~json
{
  "source": "00ba2fcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2fd0`](#insn-00ba2fd0)

~~~json
{
  "source": "00ba2fd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2fd4`](#insn-00ba2fd4)

~~~json
{
  "source": "00ba2fd4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2fd8`](#insn-00ba2fd8)

~~~json
{
  "source": "00ba2fd8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2fdc`](#insn-00ba2fdc)

~~~json
{
  "source": "00ba2fdc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2fe4`](#insn-00ba2fe4)

~~~json
{
  "source": "00ba2fe4",
  "target": "00c5ce30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba2fe8`](#insn-00ba2fe8)

~~~json
{
  "source": "00ba2fe8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2ff4`](#insn-00ba2ff4)

~~~json
{
  "source": "00ba2ff4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2ff8`](#insn-00ba2ff8)

~~~json
{
  "source": "00ba2ff8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba2ffc`](#insn-00ba2ffc)

~~~json
{
  "source": "00ba2ffc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba3000`](#insn-00ba3000)

~~~json
{
  "source": "00ba3000",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba3004`](#insn-00ba3004)

~~~json
{
  "source": "00ba3004",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba3008`](#insn-00ba3008)

~~~json
{
  "source": "00ba3008",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
