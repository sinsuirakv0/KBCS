# 00ba4bdc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00ba4b40`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba4/00ba4b40.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0078.md#compare-5eeaa396997e5950b467de9b1c492b83)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00ba5bd0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba5/00ba5bd0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0034.md#compare-030fad3d7bb9cc01cf9de143e6a50b88)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ba4bdc",
  "name": "_ZNSt6__ndk113__stable_sortIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6_EEEEvT0_SC_T_NS_15iterator_traitsISC_E15difference_typeEPNSF_10value_typeEl",
  "size": 1228,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7b2326e1c30c2a46ab609e209b74a6bc1caa3be273311aec186d2dbae627b4c8",
  "source_text_sha256": "7b2326e1c30c2a46ab609e209b74a6bc1caa3be273311aec186d2dbae627b4c8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ba4bdc",
        "00ba50a7"
      ]
    ],
    "bytes_sha256": "8dd6da24ec0c1480f50b9083bec353f0c6300572892bb7daf631607558e88f94",
    "instruction_count": 307,
    "instruction_bytes": 1228,
    "body_bytes": 1228,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5cbd0](../00c5c/00c5cbd0.md)

## 呼び出し先

- [00c58120](../00c58/00c58120.md)
- [00c5cbd0](../00c5c/00c5cbd0.md)
- [00c5cc60](../00c5c/00c5cc60.md)
- [00c5cd00](../00c5c/00c5cd00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 11740 bytes

~~~c

void _ZNSt6__ndk113__stable_sortIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6_EEEEvT0_SC_T_NS_15iterator_traitsISC_E15difference_typeEPNSF_10value_typeEl
               (uint *param_1,uint *param_2,long *param_3,ulong param_4,uint *param_5,long param_6)

{
  long lVar1;
  uint *puVar2;
  uint *puVar3;
  uint *puVar4;
  uint *puVar5;
  undefined8 *puVar6;
  undefined8 *puVar7;
  uint uVar8;
  uint uVar9;
  uint uVar10;
  uint uVar11;
  uint uVar12;
  bool bVar13;
  int iVar14;
  int *piVar15;
  ulong uVar16;
  uint *puVar17;
  uint *puVar18;
  int *piVar19;
  ulong uVar20;
  long lVar21;
  ulong uVar22;
  long lVar23;
  long lVar24;
  undefined8 uVar25;
  undefined8 uVar26;
  undefined8 uVar27;
  
  if (1 < param_4) {
    if (param_4 == 2) {
      uVar10 = param_2[-1];
      uVar8 = *param_1;
      lVar21 = *(long *)(*param_3 + 0x38) + *(long *)(*param_3 + 0x28);
      piVar19 = (int *)(lVar21 - (ulong)uVar10);
      piVar15 = (int *)(lVar21 - (ulong)uVar8);
      puVar18 = (uint *)((long)piVar19 + (ulong)*(ushort *)((long)piVar19 + (4 - (long)*piVar19)));
                    /* try { // try from 00ba4c54 to 00ca4c6f has its CatchHandler @ 00ba562c */
      puVar17 = (uint *)((long)piVar15 + (ulong)*(ushort *)((long)piVar15 + (4 - (long)*piVar15)));
      puVar18 = (uint *)((long)puVar18 + (ulong)*puVar18);
      puVar17 = (uint *)((long)puVar17 + (ulong)*puVar17);
      uVar11 = *puVar18;
      uVar12 = *puVar17;
      uVar9 = uVar12;
                    /* try { // try from 00ba4c74 to 00ca4c7f has its CatchHandler @ 00ba55d0 */
      if (uVar11 <= uVar12) {
        uVar9 = uVar11;
      }
      iVar14 = memcmp(puVar18 + 1,puVar17 + 1,(ulong)uVar9);
                    /* try { // try from 00ba4c80 to 00ca4c8b has its CatchHandler @ 00ba5578 */
      bVar13 = uVar11 < uVar12;
                    /* try { // try from 00ba4c8c to 00ca4cbf has its CatchHandler @ 00ba57c4 */
      if (iVar14 != 0) {
        bVar13 = iVar14 < 0;
      }
      if (bVar13) {
        *param_1 = uVar10;
        param_2[-1] = uVar8;
      }
    }
    else if ((long)param_4 < 0x81) {
      if ((param_1 != param_2) && (puVar18 = param_1 + 1, puVar18 != param_2)) {
                    /* try { // try from 00ba4cc4 to 00ca4ccf has its CatchHandler @ 00ba552c */
        lVar21 = 0;
        do {
          uVar9 = *puVar18;
          puVar17 = param_1;
          if (puVar18 != param_1) {
            lVar1 = *(long *)(*param_3 + 0x38) + *(long *)(*param_3 + 0x28);
            piVar15 = (int *)(lVar1 - (ulong)uVar9);
            lVar23 = lVar21;
            do {
              uVar12 = *(uint *)((long)param_1 + lVar23);
                    /* try { // try from 00ba4d20 to 00ca4d3f has its CatchHandler @ 00ba56ec */
              piVar19 = (int *)(lVar1 - (ulong)uVar12);
              puVar2 = (uint *)((long)piVar15 +
                               (ulong)*(ushort *)((long)piVar15 + (4 - (long)*piVar15)));
                    /* try { // try from 00ba4d40 to 00ca4d73 has its CatchHandler @ 00ba595c */
              puVar3 = (uint *)((long)piVar19 +
                               (ulong)*(ushort *)((long)piVar19 + (4 - (long)*piVar19)));
              puVar2 = (uint *)((long)puVar2 + (ulong)*puVar2);
              uVar10 = *puVar2;
              puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3);
              uVar11 = *puVar3;
              uVar8 = uVar11;
              if (uVar10 <= uVar11) {
                uVar8 = uVar10;
              }
              iVar14 = memcmp(puVar2 + 1,puVar3 + 1,(ulong)uVar8);
              bVar13 = uVar10 < uVar11;
                    /* try { // try from 00ba4d78 to 00ca4d93 has its CatchHandler @ 00ba5628 */
              if (iVar14 != 0) {
                bVar13 = iVar14 < 0;
              }
              if (!bVar13) {
                    /* try { // try from 00ba4cd0 to 00ca4cdb has its CatchHandler @ 00ba54d8 */
                puVar17 = (uint *)((long)param_1 + lVar23 + 4);
                break;
              }
              lVar24 = lVar23 + -4;
              *(uint *)((long)param_1 + lVar23 + 4) = uVar12;
              lVar23 = lVar24;
            } while (lVar24 != -4);
          }
                    /* try { // try from 00ba4cdc to 00ca4cef has its CatchHandler @ 00ba5470 */
          puVar18 = puVar18 + 1;
          lVar21 = lVar21 + 4;
          *puVar17 = uVar9;
        } while (puVar18 != param_2);
      }
    }
    else {
      uVar22 = param_4 >> 1;
      puVar18 = param_1 + uVar22;
                    /* try { // try from 00ba4da4 to 00ca4daf has its CatchHandler @ 00ba5570 */
                    /* try { // try from 00ba4db0 to 00ca4de3 has its CatchHandler @ 00ba578c */
      if (param_6 < (long)param_4) {
        _ZNSt6__ndk113__stable_sortIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6_EEEEvT0_SC_T_NS_15iterator_traitsISC_E15difference_typeEPNSF_10value_typeEl
                  (param_1,puVar18,param_3,uVar22,param_5,param_6);
                    /* try { // try from 00ba4de8 to 00ca4df3 has its CatchHandler @ 00ba5528 */
        _ZNSt6__ndk113__stable_sortIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6_EEEEvT0_SC_T_NS_15iterator_traitsISC_E15difference_typeEPNSF_10value_typeEl
                  (puVar18,param_2,param_3,param_4 - uVar22,param_5,param_6);
                    /* try { // try from 00ba4df4 to 00ca4dff has its CatchHandler @ 00ba54c0 */
                    /* try { // try from 00ba4e00 to 00ca4e13 has its CatchHandler @ 00ba5460 */
        _ZNSt6__ndk115__inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6_EEEEvT0_SC_SC_T_NS_15iterator_traitsISC_E15difference_typeESG_PNSF_10value_typeEl
                  (param_1,puVar18,param_2,param_3,uVar22,param_4 - uVar22,param_5,param_6);
        return;
      }
      _ZNSt6__ndk118__stable_sort_moveIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6_EEEEvT0_SC_T_NS_15iterator_traitsISC_E15difference_typeEPNSF_10value_typeE
                (param_1,puVar18,param_3,uVar22,param_5);
                    /* try { // try from 00ba4e44 to 00ca4e63 has its CatchHandler @ 00ba56e8 */
      puVar2 = param_5 + uVar22;
      _ZNSt6__ndk118__stable_sort_moveIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6_EEEEvT0_SC_T_NS_15iterator_traitsISC_E15difference_typeEPNSF_10value_typeE
                (puVar18,param_2,param_3,param_4 - uVar22,puVar2);
                    /* try { // try from 00ba4e64 to 00ca4e97 has its CatchHandler @ 00ba5958 */
      puVar3 = param_5 + param_4;
      puVar17 = puVar2;
      puVar18 = param_5;
      do {
        if (puVar17 == puVar3) {
          if (puVar18 == puVar2) {
            return;
          }
          uVar16 = (long)param_5 + (uVar22 * 4 - (long)puVar18) + -4;
          uVar22 = (uVar16 >> 2) + 1;
                    /* try { // try from 00ba4fc0 to 00ca4fcb has its CatchHandler @ 00ba5558 */
          if ((7 < uVar22) &&
             ((uVar16 = uVar16 & 0xfffffffffffffffc, (uint *)((long)puVar18 + uVar16 + 4) <= param_1
              || ((uint *)((long)param_1 + uVar16 + 4) <= puVar18)))) {
            uVar20 = uVar22 & 0x7ffffffffffffff8;
            lVar21 = 0;
            uVar16 = uVar20;
            do {
              puVar6 = (undefined8 *)((long)puVar18 + lVar21);
                    /* try { // try from 00ba5054 to 00ca5063 has its CatchHandler @ 00ba544c */
              uVar25 = *puVar6;
              uVar27 = puVar6[3];
              uVar26 = puVar6[2];
              puVar7 = (undefined8 *)((long)param_1 + lVar21);
              uVar16 = uVar16 - 8;
              lVar21 = lVar21 + 0x20;
                    /* try { // try from 00ba5064 to 00ca5077 has its CatchHandler @ 00ba5424 */
              puVar7[1] = puVar6[1];
              *puVar7 = uVar25;
              puVar7[3] = uVar27;
              puVar7[2] = uVar26;
            } while (uVar16 != 0);
            puVar18 = puVar18 + uVar20;
            param_1 = param_1 + (uVar22 & 0x3ffffffffffffff8);
            if (uVar22 == uVar20) {
              return;
            }
          }
          do {
            puVar17 = puVar18 + 1;
            *param_1 = *puVar18;
            puVar18 = puVar17;
            param_1 = param_1 + 1;
          } while (puVar2 != puVar17);
          return;
        }
                    /* try { // try from 00ba4e98 to 00ca4f9b has its CatchHandler @ 00ba3e94 */
        uVar8 = *puVar17;
        uVar10 = *puVar18;
        lVar21 = *(long *)(*param_3 + 0x38) + *(long *)(*param_3 + 0x28);
        piVar19 = (int *)(lVar21 - (ulong)uVar8);
        piVar15 = (int *)(lVar21 - (ulong)uVar10);
        puVar4 = (uint *)((long)piVar19 + (ulong)*(ushort *)((long)piVar19 + (4 - (long)*piVar19)));
        puVar5 = (uint *)((long)piVar15 + (ulong)*(ushort *)((long)piVar15 + (4 - (long)*piVar15)));
        puVar4 = (uint *)((long)puVar4 + (ulong)*puVar4);
        puVar5 = (uint *)((long)puVar5 + (ulong)*puVar5);
        uVar11 = *puVar4;
        uVar12 = *puVar5;
        uVar9 = uVar12;
        if (uVar11 <= uVar12) {
          uVar9 = uVar11;
        }
        iVar14 = memcmp(puVar4 + 1,puVar5 + 1,(ulong)uVar9);
        bVar13 = uVar11 < uVar12;
        if (iVar14 != 0) {
          bVar13 = iVar14 < 0;
        }
        if (bVar13) {
          *param_1 = uVar8;
          puVar17 = puVar17 + 1;
        }
        else {
          puVar18 = puVar18 + 1;
          *param_1 = uVar10;
        }
        param_1 = param_1 + 1;
      } while (puVar18 != puVar2);
      if (puVar17 == puVar3) {
        return;
      }
      uVar16 = (long)param_5 + (param_4 * 4 - (long)puVar17) + -4;
      uVar22 = (uVar16 >> 2) + 1;
                    /* try { // try from 00ba4f9c to 00ca4fab has its CatchHandler @ 00ba5610 */
      if ((7 < uVar22) &&
         ((uVar16 = uVar16 & 0xfffffffffffffffc, (uint *)((long)puVar17 + uVar16 + 4) <= param_1 ||
          ((uint *)((long)param_1 + uVar16 + 4) <= puVar17)))) {
                    /* try { // try from 00ba4fec to 00ca4fff has its CatchHandler @ 00ba553c */
        uVar20 = uVar22 & 0x7ffffffffffffff8;
        lVar21 = 0;
                    /* try { // try from 00ba5000 to 00ca500f has its CatchHandler @ 00ba5538 */
        uVar16 = uVar20;
        do {
          puVar6 = (undefined8 *)((long)puVar17 + lVar21);
          uVar25 = *puVar6;
          uVar27 = puVar6[3];
          uVar26 = puVar6[2];
                    /* try { // try from 00ba5010 to 00ca5023 has its CatchHandler @ 00ba5514 */
          puVar7 = (undefined8 *)((long)param_1 + lVar21);
          uVar16 = uVar16 - 8;
          lVar21 = lVar21 + 0x20;
          puVar7[1] = puVar6[1];
          *puVar7 = uVar25;
          puVar7[3] = uVar27;
          puVar7[2] = uVar26;
        } while (uVar16 != 0);
                    /* try { // try from 00ba5024 to 00ca5033 has its CatchHandler @ 00ba54a8 */
        puVar17 = puVar17 + uVar20;
        param_1 = param_1 + (uVar22 & 0x3ffffffffffffff8);
        if (uVar22 == uVar20) {
          return;
        }
      }
      do {
        puVar18 = puVar17 + 1;
                    /* try { // try from 00ba4fac to 00ca4fbf has its CatchHandler @ 00ba55b0 */
        *param_1 = *puVar17;
        puVar17 = puVar18;
        param_1 = param_1 + 1;
      } while (puVar3 != puVar18);
    }
  }
                    /* try { // try from 00ba5088 to 00ca5093 has its CatchHandler @ 00ba540c */
                    /* try { // try from 00ba5094 to 00ca50d3 has its CatchHandler @ 00ba3e94 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ba4bdc"></a> `00ba4bdc` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00ba4be0"></a> `00ba4be0` | `fc 6f 02 a9` | stp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba4be4"></a> `00ba4be4` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba4be8"></a> `00ba4be8` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ba4bec"></a> `00ba4bec` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ba4bf0"></a> `00ba4bf0` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ba4bf4"></a> `00ba4bf4` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ba4bf8"></a> `00ba4bf8` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00ba4bfc"></a> `00ba4bfc` | `7f 08 00 f1` | cmp x3,#0x2 | `FALL_THROUGH`
<a id="insn-00ba4c00"></a> `00ba4c00` | `e4 0b 01 a9` | stp x4,x2,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba4c04"></a> `00ba4c04` | `23 24 00 54` | b.cc 0x00ba5088 | `CONDITIONAL_JUMP`
<a id="insn-00ba4c08"></a> `00ba4c08` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00ba4c0c"></a> `00ba4c0c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ba4c10"></a> `00ba4c10` | `a1 04 00 54` | b.ne 0x00ba4ca4 | `CONDITIONAL_JUMP`
<a id="insn-00ba4c14"></a> `00ba4c14` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ba4c18"></a> `00ba4c18` | `b4 c2 5f b8` | ldur w20,[x21, #-0x4] | `FALL_THROUGH`
<a id="insn-00ba4c1c"></a> `00ba4c1c` | `76 02 40 b9` | ldr w22,[x19] | `FALL_THROUGH`
<a id="insn-00ba4c20"></a> `00ba4c20` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ba4c24"></a> `00ba4c24` | `09 1d 40 f9` | ldr x9,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00ba4c28"></a> `00ba4c28` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00ba4c2c"></a> `00ba4c2c` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00ba4c30"></a> `00ba4c30` | `09 01 14 cb` | sub x9,x8,x20 | `FALL_THROUGH`
<a id="insn-00ba4c34"></a> `00ba4c34` | `08 01 16 cb` | sub x8,x8,x22 | `FALL_THROUGH`
<a id="insn-00ba4c38"></a> `00ba4c38` | `2a 01 80 b9` | ldrsw x10,[x9] | `FALL_THROUGH`
<a id="insn-00ba4c3c"></a> `00ba4c3c` | `0b 01 80 b9` | ldrsw x11,[x8] | `FALL_THROUGH`
<a id="insn-00ba4c40"></a> `00ba4c40` | `2a 01 0a cb` | sub x10,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba4c44"></a> `00ba4c44` | `0b 01 0b cb` | sub x11,x8,x11 | `FALL_THROUGH`
<a id="insn-00ba4c48"></a> `00ba4c48` | `4a 09 40 79` | ldrh w10,[x10, #0x4] | `FALL_THROUGH`
<a id="insn-00ba4c4c"></a> `00ba4c4c` | `6b 09 40 79` | ldrh w11,[x11, #0x4] | `FALL_THROUGH`
<a id="insn-00ba4c50"></a> `00ba4c50` | `29 01 0a 8b` | add x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba4c54"></a> `00ba4c54` | `08 01 0b 8b` | add x8,x8,x11 | `FALL_THROUGH`
<a id="insn-00ba4c58"></a> `00ba4c58` | `2a 01 40 b9` | ldr w10,[x9] | `FALL_THROUGH`
<a id="insn-00ba4c5c"></a> `00ba4c5c` | `0b 01 40 b9` | ldr w11,[x8] | `FALL_THROUGH`
<a id="insn-00ba4c60"></a> `00ba4c60` | `20 01 0a 8b` | add x0,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba4c64"></a> `00ba4c64` | `01 01 0b 8b` | add x1,x8,x11 | `FALL_THROUGH`
<a id="insn-00ba4c68"></a> `00ba4c68` | `17 44 40 b8` | ldr w23,[x0], #0x4 | `FALL_THROUGH`
<a id="insn-00ba4c6c"></a> `00ba4c6c` | `38 44 40 b8` | ldr w24,[x1], #0x4 | `FALL_THROUGH`
<a id="insn-00ba4c70"></a> `00ba4c70` | `1f 03 17 6b` | cmp w24,w23 | `FALL_THROUGH`
<a id="insn-00ba4c74"></a> `00ba4c74` | `02 33 97 1a` | csel w2,w24,w23,cc | `FALL_THROUGH`
<a id="insn-00ba4c78"></a> `00ba4c78` | `2a cd 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00ba4c7c"></a> `00ba4c7c` | `ff 02 18 6b` | cmp w23,w24 | `FALL_THROUGH`
<a id="insn-00ba4c80"></a> `00ba4c80` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00ba4c84"></a> `00ba4c84` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00ba4c88"></a> `00ba4c88` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00ba4c8c"></a> `00ba4c8c` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00ba4c90"></a> `00ba4c90` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ba4c94"></a> `00ba4c94` | `a1 1f 00 54` | b.ne 0x00ba5088 | `CONDITIONAL_JUMP`
<a id="insn-00ba4c98"></a> `00ba4c98` | `74 02 00 b9` | str w20,[x19] | `FALL_THROUGH`
<a id="insn-00ba4c9c"></a> `00ba4c9c` | `b6 c2 1f b8` | stur w22,[x21, #-0x4] | `FALL_THROUGH`
<a id="insn-00ba4ca0"></a> `00ba4ca0` | `fa 00 00 14` | b 0x00ba5088 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba4ca4"></a> `00ba4ca4` | `f8 03 03 aa` | mov x24,x3 | `FALL_THROUGH`
<a id="insn-00ba4ca8"></a> `00ba4ca8` | `7f 00 02 f1` | cmp x3,#0x80 | `FALL_THROUGH`
<a id="insn-00ba4cac"></a> `00ba4cac` | `8c 07 00 54` | b.gt 0x00ba4d9c | `CONDITIONAL_JUMP`
<a id="insn-00ba4cb0"></a> `00ba4cb0` | `7f 02 15 eb` | cmp x19,x21 | `FALL_THROUGH`
<a id="insn-00ba4cb4"></a> `00ba4cb4` | `a0 1e 00 54` | b.eq 0x00ba5088 | `CONDITIONAL_JUMP`
<a id="insn-00ba4cb8"></a> `00ba4cb8` | `76 12 00 91` | add x22,x19,#0x4 | `FALL_THROUGH`
<a id="insn-00ba4cbc"></a> `00ba4cbc` | `df 02 15 eb` | cmp x22,x21 | `FALL_THROUGH`
<a id="insn-00ba4cc0"></a> `00ba4cc0` | `40 1e 00 54` | b.eq 0x00ba5088 | `CONDITIONAL_JUMP`
<a id="insn-00ba4cc4"></a> `00ba4cc4` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00ba4cc8"></a> `00ba4cc8` | `f5 07 00 f9` | str x21,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ba4ccc"></a> `00ba4ccc` | `09 00 00 14` | b 0x00ba4cf0 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba4cd0"></a> `00ba4cd0` | `68 02 1b 8b` | add x8,x19,x27 | `FALL_THROUGH`
<a id="insn-00ba4cd4"></a> `00ba4cd4` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00ba4cd8"></a> `00ba4cd8` | `f5 07 40 f9` | ldr x21,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ba4cdc"></a> `00ba4cdc` | `d6 12 00 91` | add x22,x22,#0x4 | `FALL_THROUGH`
<a id="insn-00ba4ce0"></a> `00ba4ce0` | `df 02 15 eb` | cmp x22,x21 | `FALL_THROUGH`
<a id="insn-00ba4ce4"></a> `00ba4ce4` | `f7 12 00 91` | add x23,x23,#0x4 | `FALL_THROUGH`
<a id="insn-00ba4ce8"></a> `00ba4ce8` | `18 01 00 b9` | str w24,[x8] | `FALL_THROUGH`
<a id="insn-00ba4cec"></a> `00ba4cec` | `e0 1c 00 54` | b.eq 0x00ba5088 | `CONDITIONAL_JUMP`
<a id="insn-00ba4cf0"></a> `00ba4cf0` | `d8 02 40 b9` | ldr w24,[x22] | `FALL_THROUGH`
<a id="insn-00ba4cf4"></a> `00ba4cf4` | `df 02 13 eb` | cmp x22,x19 | `FALL_THROUGH`
<a id="insn-00ba4cf8"></a> `00ba4cf8` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00ba4cfc"></a> `00ba4cfc` | `00 ff ff 54` | b.eq 0x00ba4cdc | `CONDITIONAL_JUMP`
<a id="insn-00ba4d00"></a> `00ba4d00` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ba4d04"></a> `00ba4d04` | `fb 03 17 aa` | mov x27,x23 | `FALL_THROUGH`
<a id="insn-00ba4d08"></a> `00ba4d08` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ba4d0c"></a> `00ba4d0c` | `09 1d 40 f9` | ldr x9,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00ba4d10"></a> `00ba4d10` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00ba4d14"></a> `00ba4d14` | `39 01 08 8b` | add x25,x9,x8 | `FALL_THROUGH`
<a id="insn-00ba4d18"></a> `00ba4d18` | `3a 03 18 cb` | sub x26,x25,x24 | `FALL_THROUGH`
<a id="insn-00ba4d1c"></a> `00ba4d1c` | `7c 6a 7b b8` | ldr w28,[x19, x27, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ba4d20"></a> `00ba4d20` | `48 03 80 b9` | ldrsw x8,[x26] | `FALL_THROUGH`
<a id="insn-00ba4d24"></a> `00ba4d24` | `29 03 1c cb` | sub x9,x25,x28 | `FALL_THROUGH`
<a id="insn-00ba4d28"></a> `00ba4d28` | `2a 01 80 b9` | ldrsw x10,[x9] | `FALL_THROUGH`
<a id="insn-00ba4d2c"></a> `00ba4d2c` | `48 03 08 cb` | sub x8,x26,x8 | `FALL_THROUGH`
<a id="insn-00ba4d30"></a> `00ba4d30` | `08 09 40 79` | ldrh w8,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00ba4d34"></a> `00ba4d34` | `2a 01 0a cb` | sub x10,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba4d38"></a> `00ba4d38` | `4a 09 40 79` | ldrh w10,[x10, #0x4] | `FALL_THROUGH`
<a id="insn-00ba4d3c"></a> `00ba4d3c` | `48 03 08 8b` | add x8,x26,x8 | `FALL_THROUGH`
<a id="insn-00ba4d40"></a> `00ba4d40` | `0b 01 40 b9` | ldr w11,[x8] | `FALL_THROUGH`
<a id="insn-00ba4d44"></a> `00ba4d44` | `29 01 0a 8b` | add x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba4d48"></a> `00ba4d48` | `2a 01 40 b9` | ldr w10,[x9] | `FALL_THROUGH`
<a id="insn-00ba4d4c"></a> `00ba4d4c` | `00 01 0b 8b` | add x0,x8,x11 | `FALL_THROUGH`
<a id="insn-00ba4d50"></a> `00ba4d50` | `14 44 40 b8` | ldr w20,[x0], #0x4 | `FALL_THROUGH`
<a id="insn-00ba4d54"></a> `00ba4d54` | `21 01 0a 8b` | add x1,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba4d58"></a> `00ba4d58` | `35 44 40 b8` | ldr w21,[x1], #0x4 | `FALL_THROUGH`
<a id="insn-00ba4d5c"></a> `00ba4d5c` | `bf 02 14 6b` | cmp w21,w20 | `FALL_THROUGH`
<a id="insn-00ba4d60"></a> `00ba4d60` | `a2 32 94 1a` | csel w2,w21,w20,cc | `FALL_THROUGH`
<a id="insn-00ba4d64"></a> `00ba4d64` | `ef cc 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00ba4d68"></a> `00ba4d68` | `9f 02 15 6b` | cmp w20,w21 | `FALL_THROUGH`
<a id="insn-00ba4d6c"></a> `00ba4d6c` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00ba4d70"></a> `00ba4d70` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00ba4d74"></a> `00ba4d74` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00ba4d78"></a> `00ba4d78` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00ba4d7c"></a> `00ba4d7c` | `a8 fa 07 36` | tbz w8,#0x0,0x00ba4cd0 | `CONDITIONAL_JUMP`
<a id="insn-00ba4d80"></a> `00ba4d80` | `68 02 1b 8b` | add x8,x19,x27 | `FALL_THROUGH`
<a id="insn-00ba4d84"></a> `00ba4d84` | `7b 13 00 d1` | sub x27,x27,#0x4 | `FALL_THROUGH`
<a id="insn-00ba4d88"></a> `00ba4d88` | `7f 13 00 b1` | cmn x27,#0x4 | `FALL_THROUGH`
<a id="insn-00ba4d8c"></a> `00ba4d8c` | `1c 05 00 b9` | str w28,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00ba4d90"></a> `00ba4d90` | `61 fc ff 54` | b.ne 0x00ba4d1c | `CONDITIONAL_JUMP`
<a id="insn-00ba4d94"></a> `00ba4d94` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00ba4d98"></a> `00ba4d98` | `d0 ff ff 17` | b 0x00ba4cd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba4d9c"></a> `00ba4d9c` | `19 ff 41 d3` | lsr x25,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00ba4da0"></a> `00ba4da0` | `7a 0a 19 8b` | add x26,x19,x25, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ba4da4"></a> `00ba4da4` | `f6 03 05 aa` | mov x22,x5 | `FALL_THROUGH`
<a id="insn-00ba4da8"></a> `00ba4da8` | `1f 03 05 eb` | cmp x24,x5 | `FALL_THROUGH`
<a id="insn-00ba4dac"></a> `00ba4dac` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba4db0"></a> `00ba4db0` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00ba4db4"></a> `00ba4db4` | `ed 03 00 54` | b.le 0x00ba4e30 | `CONDITIONAL_JUMP`
<a id="insn-00ba4db8"></a> `00ba4db8` | `f7 53 41 a9` | ldp x23,x20,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba4dbc"></a> `00ba4dbc` | `e3 03 19 aa` | mov x3,x25 | `FALL_THROUGH`
<a id="insn-00ba4dc0"></a> `00ba4dc0` | `e5 03 16 aa` | mov x5,x22 | `FALL_THROUGH`
<a id="insn-00ba4dc4"></a> `00ba4dc4` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00ba4dc8"></a> `00ba4dc8` | `e4 03 17 aa` | mov x4,x23 | `FALL_THROUGH`
<a id="insn-00ba4dcc"></a> `00ba4dcc` | `81 df 02 94` | bl 0x00c5cbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00ba4dd0"></a> `00ba4dd0` | `18 03 19 cb` | sub x24,x24,x25 | `FALL_THROUGH`
<a id="insn-00ba4dd4"></a> `00ba4dd4` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00ba4dd8"></a> `00ba4dd8` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba4ddc"></a> `00ba4ddc` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00ba4de0"></a> `00ba4de0` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00ba4de4"></a> `00ba4de4` | `e4 03 17 aa` | mov x4,x23 | `FALL_THROUGH`
<a id="insn-00ba4de8"></a> `00ba4de8` | `e5 03 16 aa` | mov x5,x22 | `FALL_THROUGH`
<a id="insn-00ba4dec"></a> `00ba4dec` | `79 df 02 94` | bl 0x00c5cbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00ba4df0"></a> `00ba4df0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba4df4"></a> `00ba4df4` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00ba4df8"></a> `00ba4df8` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00ba4dfc"></a> `00ba4dfc` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00ba4e00"></a> `00ba4e00` | `e4 03 19 aa` | mov x4,x25 | `FALL_THROUGH`
<a id="insn-00ba4e04"></a> `00ba4e04` | `e5 03 18 aa` | mov x5,x24 | `FALL_THROUGH`
<a id="insn-00ba4e08"></a> `00ba4e08` | `e6 03 17 aa` | mov x6,x23 | `FALL_THROUGH`
<a id="insn-00ba4e0c"></a> `00ba4e0c` | `e7 03 16 aa` | mov x7,x22 | `FALL_THROUGH`
<a id="insn-00ba4e10"></a> `00ba4e10` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ba4e14"></a> `00ba4e14` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ba4e18"></a> `00ba4e18` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ba4e1c"></a> `00ba4e1c` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ba4e20"></a> `00ba4e20` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba4e24"></a> `00ba4e24` | `fc 6f 42 a9` | ldp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba4e28"></a> `00ba4e28` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00ba4e2c"></a> `00ba4e2c` | `8d df 02 14` | b 0x00c5cc60 | `CALL_TERMINATOR`
<a id="insn-00ba4e30"></a> `00ba4e30` | `f7 53 41 a9` | ldp x23,x20,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba4e34"></a> `00ba4e34` | `e3 03 19 aa` | mov x3,x25 | `FALL_THROUGH`
<a id="insn-00ba4e38"></a> `00ba4e38` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00ba4e3c"></a> `00ba4e3c` | `e4 03 17 aa` | mov x4,x23 | `FALL_THROUGH`
<a id="insn-00ba4e40"></a> `00ba4e40` | `b0 df 02 94` | bl 0x00c5cd00 | `UNCONDITIONAL_CALL`
<a id="insn-00ba4e44"></a> `00ba4e44` | `f6 0a 19 8b` | add x22,x23,x25, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ba4e48"></a> `00ba4e48` | `03 03 19 cb` | sub x3,x24,x25 | `FALL_THROUGH`
<a id="insn-00ba4e4c"></a> `00ba4e4c` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00ba4e50"></a> `00ba4e50` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba4e54"></a> `00ba4e54` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00ba4e58"></a> `00ba4e58` | `e4 03 16 aa` | mov x4,x22 | `FALL_THROUGH`
<a id="insn-00ba4e5c"></a> `00ba4e5c` | `f9 03 00 f9` | str x25,[sp] | `FALL_THROUGH`
<a id="insn-00ba4e60"></a> `00ba4e60` | `a8 df 02 94` | bl 0x00c5cd00 | `UNCONDITIONAL_CALL`
<a id="insn-00ba4e64"></a> `00ba4e64` | `f5 0a 18 8b` | add x21,x23,x24, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ba4e68"></a> `00ba4e68` | `fa 03 17 aa` | mov x26,x23 | `FALL_THROUGH`
<a id="insn-00ba4e6c"></a> `00ba4e6c` | `fb 03 16 aa` | mov x27,x22 | `FALL_THROUGH`
<a id="insn-00ba4e70"></a> `00ba4e70` | `7f 03 15 eb` | cmp x27,x21 | `FALL_THROUGH`
<a id="insn-00ba4e74"></a> `00ba4e74` | `21 01 00 54` | b.ne 0x00ba4e98 | `CONDITIONAL_JUMP`
<a id="insn-00ba4e78"></a> `00ba4e78` | `2c 00 00 14` | b 0x00ba4f28 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba4e7c"></a> `00ba4e7c` | `5a 13 00 91` | add x26,x26,#0x4 | `FALL_THROUGH`
<a id="insn-00ba4e80"></a> `00ba4e80` | `79 02 00 b9` | str w25,[x19] | `FALL_THROUGH`
<a id="insn-00ba4e84"></a> `00ba4e84` | `5f 03 16 eb` | cmp x26,x22 | `FALL_THROUGH`
<a id="insn-00ba4e88"></a> `00ba4e88` | `73 12 00 91` | add x19,x19,#0x4 | `FALL_THROUGH`
<a id="insn-00ba4e8c"></a> `00ba4e8c` | `80 06 00 54` | b.eq 0x00ba4f5c | `CONDITIONAL_JUMP`
<a id="insn-00ba4e90"></a> `00ba4e90` | `7f 03 15 eb` | cmp x27,x21 | `FALL_THROUGH`
<a id="insn-00ba4e94"></a> `00ba4e94` | `a0 04 00 54` | b.eq 0x00ba4f28 | `CONDITIONAL_JUMP`
<a id="insn-00ba4e98"></a> `00ba4e98` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ba4e9c"></a> `00ba4e9c` | `7c 03 40 b9` | ldr w28,[x27] | `FALL_THROUGH`
<a id="insn-00ba4ea0"></a> `00ba4ea0` | `59 03 40 b9` | ldr w25,[x26] | `FALL_THROUGH`
<a id="insn-00ba4ea4"></a> `00ba4ea4` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ba4ea8"></a> `00ba4ea8` | `09 1d 40 f9` | ldr x9,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00ba4eac"></a> `00ba4eac` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00ba4eb0"></a> `00ba4eb0` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00ba4eb4"></a> `00ba4eb4` | `09 01 1c cb` | sub x9,x8,x28 | `FALL_THROUGH`
<a id="insn-00ba4eb8"></a> `00ba4eb8` | `08 01 19 cb` | sub x8,x8,x25 | `FALL_THROUGH`
<a id="insn-00ba4ebc"></a> `00ba4ebc` | `2a 01 80 b9` | ldrsw x10,[x9] | `FALL_THROUGH`
<a id="insn-00ba4ec0"></a> `00ba4ec0` | `0b 01 80 b9` | ldrsw x11,[x8] | `FALL_THROUGH`
<a id="insn-00ba4ec4"></a> `00ba4ec4` | `2a 01 0a cb` | sub x10,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba4ec8"></a> `00ba4ec8` | `0b 01 0b cb` | sub x11,x8,x11 | `FALL_THROUGH`
<a id="insn-00ba4ecc"></a> `00ba4ecc` | `4a 09 40 79` | ldrh w10,[x10, #0x4] | `FALL_THROUGH`
<a id="insn-00ba4ed0"></a> `00ba4ed0` | `6b 09 40 79` | ldrh w11,[x11, #0x4] | `FALL_THROUGH`
<a id="insn-00ba4ed4"></a> `00ba4ed4` | `29 01 0a 8b` | add x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba4ed8"></a> `00ba4ed8` | `08 01 0b 8b` | add x8,x8,x11 | `FALL_THROUGH`
<a id="insn-00ba4edc"></a> `00ba4edc` | `2a 01 40 b9` | ldr w10,[x9] | `FALL_THROUGH`
<a id="insn-00ba4ee0"></a> `00ba4ee0` | `0b 01 40 b9` | ldr w11,[x8] | `FALL_THROUGH`
<a id="insn-00ba4ee4"></a> `00ba4ee4` | `20 01 0a 8b` | add x0,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba4ee8"></a> `00ba4ee8` | `01 01 0b 8b` | add x1,x8,x11 | `FALL_THROUGH`
<a id="insn-00ba4eec"></a> `00ba4eec` | `14 44 40 b8` | ldr w20,[x0], #0x4 | `FALL_THROUGH`
<a id="insn-00ba4ef0"></a> `00ba4ef0` | `37 44 40 b8` | ldr w23,[x1], #0x4 | `FALL_THROUGH`
<a id="insn-00ba4ef4"></a> `00ba4ef4` | `ff 02 14 6b` | cmp w23,w20 | `FALL_THROUGH`
<a id="insn-00ba4ef8"></a> `00ba4ef8` | `e2 32 94 1a` | csel w2,w23,w20,cc | `FALL_THROUGH`
<a id="insn-00ba4efc"></a> `00ba4efc` | `89 cc 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00ba4f00"></a> `00ba4f00` | `9f 02 17 6b` | cmp w20,w23 | `FALL_THROUGH`
<a id="insn-00ba4f04"></a> `00ba4f04` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00ba4f08"></a> `00ba4f08` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00ba4f0c"></a> `00ba4f0c` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00ba4f10"></a> `00ba4f10` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00ba4f14"></a> `00ba4f14` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ba4f18"></a> `00ba4f18` | `21 fb ff 54` | b.ne 0x00ba4e7c | `CONDITIONAL_JUMP`
<a id="insn-00ba4f1c"></a> `00ba4f1c` | `7c 02 00 b9` | str w28,[x19] | `FALL_THROUGH`
<a id="insn-00ba4f20"></a> `00ba4f20` | `7b 13 00 91` | add x27,x27,#0x4 | `FALL_THROUGH`
<a id="insn-00ba4f24"></a> `00ba4f24` | `d8 ff ff 17` | b 0x00ba4e84 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba4f28"></a> `00ba4f28` | `5f 03 16 eb` | cmp x26,x22 | `FALL_THROUGH`
<a id="insn-00ba4f2c"></a> `00ba4f2c` | `e0 0a 00 54` | b.eq 0x00ba5088 | `CONDITIONAL_JUMP`
<a id="insn-00ba4f30"></a> `00ba4f30` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba4f34"></a> `00ba4f34` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00ba4f38"></a> `00ba4f38` | `08 09 09 8b` | add x8,x8,x9, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ba4f3c"></a> `00ba4f3c` | `08 01 1a cb` | sub x8,x8,x26 | `FALL_THROUGH`
<a id="insn-00ba4f40"></a> `00ba4f40` | `08 11 00 d1` | sub x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00ba4f44"></a> `00ba4f44` | `09 fd 42 d3` | lsr x9,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00ba4f48"></a> `00ba4f48` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00ba4f4c"></a> `00ba4f4c` | `3f 21 00 f1` | cmp x9,#0x8 | `FALL_THROUGH`
<a id="insn-00ba4f50"></a> `00ba4f50` | `82 03 00 54` | b.cs 0x00ba4fc0 | `CONDITIONAL_JUMP`
<a id="insn-00ba4f54"></a> `00ba4f54` | `e8 03 1a aa` | mov x8,x26 | `FALL_THROUGH`
<a id="insn-00ba4f58"></a> `00ba4f58` | `48 00 00 14` | b 0x00ba5078 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba4f5c"></a> `00ba4f5c` | `7f 03 15 eb` | cmp x27,x21 | `FALL_THROUGH`
<a id="insn-00ba4f60"></a> `00ba4f60` | `40 09 00 54` | b.eq 0x00ba5088 | `CONDITIONAL_JUMP`
<a id="insn-00ba4f64"></a> `00ba4f64` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba4f68"></a> `00ba4f68` | `08 09 18 8b` | add x8,x8,x24, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ba4f6c"></a> `00ba4f6c` | `08 01 1b cb` | sub x8,x8,x27 | `FALL_THROUGH`
<a id="insn-00ba4f70"></a> `00ba4f70` | `08 11 00 d1` | sub x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00ba4f74"></a> `00ba4f74` | `09 fd 42 d3` | lsr x9,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00ba4f78"></a> `00ba4f78` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00ba4f7c"></a> `00ba4f7c` | `3f 1d 00 f1` | cmp x9,#0x7 | `FALL_THROUGH`
<a id="insn-00ba4f80"></a> `00ba4f80` | `49 01 00 54` | b.ls 0x00ba4fa8 | `CONDITIONAL_JUMP`
<a id="insn-00ba4f84"></a> `00ba4f84` | `08 f5 7e 92` | and x8,x8,#-0x4 | `FALL_THROUGH`
<a id="insn-00ba4f88"></a> `00ba4f88` | `0a 01 1b 8b` | add x10,x8,x27 | `FALL_THROUGH`
<a id="insn-00ba4f8c"></a> `00ba4f8c` | `4a 11 00 91` | add x10,x10,#0x4 | `FALL_THROUGH`
<a id="insn-00ba4f90"></a> `00ba4f90` | `7f 02 0a eb` | cmp x19,x10 | `FALL_THROUGH`
<a id="insn-00ba4f94"></a> `00ba4f94` | `c2 02 00 54` | b.cs 0x00ba4fec | `CONDITIONAL_JUMP`
<a id="insn-00ba4f98"></a> `00ba4f98` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00ba4f9c"></a> `00ba4f9c` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00ba4fa0"></a> `00ba4fa0` | `7f 03 08 eb` | cmp x27,x8 | `FALL_THROUGH`
<a id="insn-00ba4fa4"></a> `00ba4fa4` | `42 02 00 54` | b.cs 0x00ba4fec | `CONDITIONAL_JUMP`
<a id="insn-00ba4fa8"></a> `00ba4fa8` | `e8 03 1b aa` | mov x8,x27 | `FALL_THROUGH`
<a id="insn-00ba4fac"></a> `00ba4fac` | `09 45 40 b8` | ldr w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00ba4fb0"></a> `00ba4fb0` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00ba4fb4"></a> `00ba4fb4` | `69 46 00 b8` | str w9,[x19], #0x4 | `FALL_THROUGH`
<a id="insn-00ba4fb8"></a> `00ba4fb8` | `a1 ff ff 54` | b.ne 0x00ba4fac | `CONDITIONAL_JUMP`
<a id="insn-00ba4fbc"></a> `00ba4fbc` | `33 00 00 14` | b 0x00ba5088 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba4fc0"></a> `00ba4fc0` | `08 f5 7e 92` | and x8,x8,#-0x4 | `FALL_THROUGH`
<a id="insn-00ba4fc4"></a> `00ba4fc4` | `0a 01 1a 8b` | add x10,x8,x26 | `FALL_THROUGH`
<a id="insn-00ba4fc8"></a> `00ba4fc8` | `4a 11 00 91` | add x10,x10,#0x4 | `FALL_THROUGH`
<a id="insn-00ba4fcc"></a> `00ba4fcc` | `7f 02 0a eb` | cmp x19,x10 | `FALL_THROUGH`
<a id="insn-00ba4fd0"></a> `00ba4fd0` | `22 03 00 54` | b.cs 0x00ba5034 | `CONDITIONAL_JUMP`
<a id="insn-00ba4fd4"></a> `00ba4fd4` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00ba4fd8"></a> `00ba4fd8` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00ba4fdc"></a> `00ba4fdc` | `5f 03 08 eb` | cmp x26,x8 | `FALL_THROUGH`
<a id="insn-00ba4fe0"></a> `00ba4fe0` | `a2 02 00 54` | b.cs 0x00ba5034 | `CONDITIONAL_JUMP`
<a id="insn-00ba4fe4"></a> `00ba4fe4` | `e8 03 1a aa` | mov x8,x26 | `FALL_THROUGH`
<a id="insn-00ba4fe8"></a> `00ba4fe8` | `24 00 00 14` | b 0x00ba5078 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba4fec"></a> `00ba4fec` | `28 f5 7e d3` | lsl x8,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00ba4ff0"></a> `00ba4ff0` | `2a ed 7d 92` | and x10,x9,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-00ba4ff4"></a> `00ba4ff4` | `08 e9 7b 92` | and x8,x8,#-0x20 | `FALL_THROUGH`
<a id="insn-00ba4ff8"></a> `00ba4ff8` | `eb 03 1f aa` | mov x11,xzr | `FALL_THROUGH`
<a id="insn-00ba4ffc"></a> `00ba4ffc` | `6c 02 08 8b` | add x12,x19,x8 | `FALL_THROUGH`
<a id="insn-00ba5000"></a> `00ba5000` | `68 0b 0a 8b` | add x8,x27,x10, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ba5004"></a> `00ba5004` | `ed 03 0a aa` | mov x13,x10 | `FALL_THROUGH`
<a id="insn-00ba5008"></a> `00ba5008` | `6e 03 0b 8b` | add x14,x27,x11 | `FALL_THROUGH`
<a id="insn-00ba500c"></a> `00ba500c` | `c0 05 40 ad` | ldp q0,q1,[x14] | `FALL_THROUGH`
<a id="insn-00ba5010"></a> `00ba5010` | `6e 02 0b 8b` | add x14,x19,x11 | `FALL_THROUGH`
<a id="insn-00ba5014"></a> `00ba5014` | `ad 21 00 f1` | subs x13,x13,#0x8 | `FALL_THROUGH`
<a id="insn-00ba5018"></a> `00ba5018` | `6b 81 00 91` | add x11,x11,#0x20 | `FALL_THROUGH`
<a id="insn-00ba501c"></a> `00ba501c` | `c0 05 00 ad` | stp q0,q1,[x14] | `FALL_THROUGH`
<a id="insn-00ba5020"></a> `00ba5020` | `41 ff ff 54` | b.ne 0x00ba5008 | `CONDITIONAL_JUMP`
<a id="insn-00ba5024"></a> `00ba5024` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00ba5028"></a> `00ba5028` | `f3 03 0c aa` | mov x19,x12 | `FALL_THROUGH`
<a id="insn-00ba502c"></a> `00ba502c` | `01 fc ff 54` | b.ne 0x00ba4fac | `CONDITIONAL_JUMP`
<a id="insn-00ba5030"></a> `00ba5030` | `16 00 00 14` | b 0x00ba5088 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba5034"></a> `00ba5034` | `2c f5 7e d3` | lsl x12,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00ba5038"></a> `00ba5038` | `2a ed 7d 92` | and x10,x9,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-00ba503c"></a> `00ba503c` | `8c e9 7b 92` | and x12,x12,#-0x20 | `FALL_THROUGH`
<a id="insn-00ba5040"></a> `00ba5040` | `eb 03 1f aa` | mov x11,xzr | `FALL_THROUGH`
<a id="insn-00ba5044"></a> `00ba5044` | `48 0b 0a 8b` | add x8,x26,x10, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ba5048"></a> `00ba5048` | `6c 02 0c 8b` | add x12,x19,x12 | `FALL_THROUGH`
<a id="insn-00ba504c"></a> `00ba504c` | `ed 03 0a aa` | mov x13,x10 | `FALL_THROUGH`
<a id="insn-00ba5050"></a> `00ba5050` | `4e 03 0b 8b` | add x14,x26,x11 | `FALL_THROUGH`
<a id="insn-00ba5054"></a> `00ba5054` | `c0 05 40 ad` | ldp q0,q1,[x14] | `FALL_THROUGH`
<a id="insn-00ba5058"></a> `00ba5058` | `6e 02 0b 8b` | add x14,x19,x11 | `FALL_THROUGH`
<a id="insn-00ba505c"></a> `00ba505c` | `ad 21 00 f1` | subs x13,x13,#0x8 | `FALL_THROUGH`
<a id="insn-00ba5060"></a> `00ba5060` | `6b 81 00 91` | add x11,x11,#0x20 | `FALL_THROUGH`
<a id="insn-00ba5064"></a> `00ba5064` | `c0 05 00 ad` | stp q0,q1,[x14] | `FALL_THROUGH`
<a id="insn-00ba5068"></a> `00ba5068` | `41 ff ff 54` | b.ne 0x00ba5050 | `CONDITIONAL_JUMP`
<a id="insn-00ba506c"></a> `00ba506c` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00ba5070"></a> `00ba5070` | `f3 03 0c aa` | mov x19,x12 | `FALL_THROUGH`
<a id="insn-00ba5074"></a> `00ba5074` | `a0 00 00 54` | b.eq 0x00ba5088 | `CONDITIONAL_JUMP`
<a id="insn-00ba5078"></a> `00ba5078` | `09 45 40 b8` | ldr w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00ba507c"></a> `00ba507c` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00ba5080"></a> `00ba5080` | `69 46 00 b8` | str w9,[x19], #0x4 | `FALL_THROUGH`
<a id="insn-00ba5084"></a> `00ba5084` | `a1 ff ff 54` | b.ne 0x00ba5078 | `CONDITIONAL_JUMP`
<a id="insn-00ba5088"></a> `00ba5088` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ba508c"></a> `00ba508c` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ba5090"></a> `00ba5090` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ba5094"></a> `00ba5094` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ba5098"></a> `00ba5098` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba509c"></a> `00ba509c` | `fc 6f 42 a9` | ldp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba50a0"></a> `00ba50a0` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00ba50a4"></a> `00ba50a4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ba4bdc`](#insn-00ba4bdc) 範囲 `[['00ba4bdc', '00ba4c07']]`
  - `CONDITIONAL_JUMP` [`00ba4c04`](#insn-00ba4c04) → [`00ba5088`](#insn-00ba5088)
  - `FALL_THROUGH` [`00ba4c04`](#insn-00ba4c04) → [`00ba4c08`](#insn-00ba4c08)
- ブロック [`00ba4c08`](#insn-00ba4c08) 範囲 `[['00ba4c08', '00ba4c13']]`
  - `CONDITIONAL_JUMP` [`00ba4c10`](#insn-00ba4c10) → [`00ba4ca4`](#insn-00ba4ca4)
  - `FALL_THROUGH` [`00ba4c10`](#insn-00ba4c10) → [`00ba4c14`](#insn-00ba4c14)
- ブロック [`00ba4c14`](#insn-00ba4c14) 範囲 `[['00ba4c14', '00ba4c53']]`
  - `FALL_THROUGH` [`00ba4c50`](#insn-00ba4c50) → [`00ba4c54`](#insn-00ba4c54)
- ブロック [`00ba4c54`](#insn-00ba4c54) 範囲 `[['00ba4c54', '00ba4c73']]`
  - `FALL_THROUGH` [`00ba4c70`](#insn-00ba4c70) → [`00ba4c74`](#insn-00ba4c74)
- ブロック [`00ba4c74`](#insn-00ba4c74) 範囲 `[['00ba4c74', '00ba4c7f']]`
  - `FALL_THROUGH` [`00ba4c7c`](#insn-00ba4c7c) → [`00ba4c80`](#insn-00ba4c80)
- ブロック [`00ba4c80`](#insn-00ba4c80) 範囲 `[['00ba4c80', '00ba4c8b']]`
  - `FALL_THROUGH` [`00ba4c88`](#insn-00ba4c88) → [`00ba4c8c`](#insn-00ba4c8c)
- ブロック [`00ba4c8c`](#insn-00ba4c8c) 範囲 `[['00ba4c8c', '00ba4c97']]`
  - `CONDITIONAL_JUMP` [`00ba4c94`](#insn-00ba4c94) → [`00ba5088`](#insn-00ba5088)
  - `FALL_THROUGH` [`00ba4c94`](#insn-00ba4c94) → [`00ba4c98`](#insn-00ba4c98)
- ブロック [`00ba4c98`](#insn-00ba4c98) 範囲 `[['00ba4c98', '00ba4ca3']]`
  - `UNCONDITIONAL_JUMP` [`00ba4ca0`](#insn-00ba4ca0) → [`00ba5088`](#insn-00ba5088)
- ブロック [`00ba4ca4`](#insn-00ba4ca4) 範囲 `[['00ba4ca4', '00ba4caf']]`
  - `CONDITIONAL_JUMP` [`00ba4cac`](#insn-00ba4cac) → [`00ba4d9c`](#insn-00ba4d9c)
  - `FALL_THROUGH` [`00ba4cac`](#insn-00ba4cac) → [`00ba4cb0`](#insn-00ba4cb0)
- ブロック [`00ba4cb0`](#insn-00ba4cb0) 範囲 `[['00ba4cb0', '00ba4cb7']]`
  - `CONDITIONAL_JUMP` [`00ba4cb4`](#insn-00ba4cb4) → [`00ba5088`](#insn-00ba5088)
  - `FALL_THROUGH` [`00ba4cb4`](#insn-00ba4cb4) → [`00ba4cb8`](#insn-00ba4cb8)
- ブロック [`00ba4cb8`](#insn-00ba4cb8) 範囲 `[['00ba4cb8', '00ba4cc3']]`
  - `CONDITIONAL_JUMP` [`00ba4cc0`](#insn-00ba4cc0) → [`00ba5088`](#insn-00ba5088)
  - `FALL_THROUGH` [`00ba4cc0`](#insn-00ba4cc0) → [`00ba4cc4`](#insn-00ba4cc4)
- ブロック [`00ba4cc4`](#insn-00ba4cc4) 範囲 `[['00ba4cc4', '00ba4ccf']]`
  - `UNCONDITIONAL_JUMP` [`00ba4ccc`](#insn-00ba4ccc) → [`00ba4cf0`](#insn-00ba4cf0)
- ブロック [`00ba4cd0`](#insn-00ba4cd0) 範囲 `[['00ba4cd0', '00ba4cd7']]`
  - `FALL_THROUGH` [`00ba4cd4`](#insn-00ba4cd4) → [`00ba4cd8`](#insn-00ba4cd8)
- ブロック [`00ba4cd8`](#insn-00ba4cd8) 範囲 `[['00ba4cd8', '00ba4cdb']]`
  - `FALL_THROUGH` [`00ba4cd8`](#insn-00ba4cd8) → [`00ba4cdc`](#insn-00ba4cdc)
- ブロック [`00ba4cdc`](#insn-00ba4cdc) 範囲 `[['00ba4cdc', '00ba4cef']]`
  - `CONDITIONAL_JUMP` [`00ba4cec`](#insn-00ba4cec) → [`00ba5088`](#insn-00ba5088)
  - `FALL_THROUGH` [`00ba4cec`](#insn-00ba4cec) → [`00ba4cf0`](#insn-00ba4cf0)
- ブロック [`00ba4cf0`](#insn-00ba4cf0) 範囲 `[['00ba4cf0', '00ba4cff']]`
  - `CONDITIONAL_JUMP` [`00ba4cfc`](#insn-00ba4cfc) → [`00ba4cdc`](#insn-00ba4cdc)
  - `FALL_THROUGH` [`00ba4cfc`](#insn-00ba4cfc) → [`00ba4d00`](#insn-00ba4d00)
- ブロック [`00ba4d00`](#insn-00ba4d00) 範囲 `[['00ba4d00', '00ba4d1b']]`
  - `FALL_THROUGH` [`00ba4d18`](#insn-00ba4d18) → [`00ba4d1c`](#insn-00ba4d1c)
- ブロック [`00ba4d1c`](#insn-00ba4d1c) 範囲 `[['00ba4d1c', '00ba4d1f']]`
  - `FALL_THROUGH` [`00ba4d1c`](#insn-00ba4d1c) → [`00ba4d20`](#insn-00ba4d20)
- ブロック [`00ba4d20`](#insn-00ba4d20) 範囲 `[['00ba4d20', '00ba4d3f']]`
  - `FALL_THROUGH` [`00ba4d3c`](#insn-00ba4d3c) → [`00ba4d40`](#insn-00ba4d40)
- ブロック [`00ba4d40`](#insn-00ba4d40) 範囲 `[['00ba4d40', '00ba4d77']]`
  - `FALL_THROUGH` [`00ba4d74`](#insn-00ba4d74) → [`00ba4d78`](#insn-00ba4d78)
- ブロック [`00ba4d78`](#insn-00ba4d78) 範囲 `[['00ba4d78', '00ba4d7f']]`
  - `CONDITIONAL_JUMP` [`00ba4d7c`](#insn-00ba4d7c) → [`00ba4cd0`](#insn-00ba4cd0)
  - `FALL_THROUGH` [`00ba4d7c`](#insn-00ba4d7c) → [`00ba4d80`](#insn-00ba4d80)
- ブロック [`00ba4d80`](#insn-00ba4d80) 範囲 `[['00ba4d80', '00ba4d93']]`
  - `CONDITIONAL_JUMP` [`00ba4d90`](#insn-00ba4d90) → [`00ba4d1c`](#insn-00ba4d1c)
  - `FALL_THROUGH` [`00ba4d90`](#insn-00ba4d90) → [`00ba4d94`](#insn-00ba4d94)
- ブロック [`00ba4d94`](#insn-00ba4d94) 範囲 `[['00ba4d94', '00ba4d97']]`
  - `FALL_THROUGH` [`00ba4d94`](#insn-00ba4d94) → [`00ba4d98`](#insn-00ba4d98)
- ブロック [`00ba4d98`](#insn-00ba4d98) 範囲 `[['00ba4d98', '00ba4d9b']]`
  - `UNCONDITIONAL_JUMP` [`00ba4d98`](#insn-00ba4d98) → [`00ba4cd8`](#insn-00ba4cd8)
- ブロック [`00ba4d9c`](#insn-00ba4d9c) 範囲 `[['00ba4d9c', '00ba4da3']]`
  - `FALL_THROUGH` [`00ba4da0`](#insn-00ba4da0) → [`00ba4da4`](#insn-00ba4da4)
- ブロック [`00ba4da4`](#insn-00ba4da4) 範囲 `[['00ba4da4', '00ba4daf']]`
  - `FALL_THROUGH` [`00ba4dac`](#insn-00ba4dac) → [`00ba4db0`](#insn-00ba4db0)
- ブロック [`00ba4db0`](#insn-00ba4db0) 範囲 `[['00ba4db0', '00ba4db7']]`
  - `CONDITIONAL_JUMP` [`00ba4db4`](#insn-00ba4db4) → [`00ba4e30`](#insn-00ba4e30)
  - `FALL_THROUGH` [`00ba4db4`](#insn-00ba4db4) → [`00ba4db8`](#insn-00ba4db8)
- ブロック [`00ba4db8`](#insn-00ba4db8) 範囲 `[['00ba4db8', '00ba4de7']]`
  - `FALL_THROUGH` [`00ba4de4`](#insn-00ba4de4) → [`00ba4de8`](#insn-00ba4de8)
- ブロック [`00ba4de8`](#insn-00ba4de8) 範囲 `[['00ba4de8', '00ba4df3']]`
  - `FALL_THROUGH` [`00ba4df0`](#insn-00ba4df0) → [`00ba4df4`](#insn-00ba4df4)
- ブロック [`00ba4df4`](#insn-00ba4df4) 範囲 `[['00ba4df4', '00ba4dff']]`
  - `FALL_THROUGH` [`00ba4dfc`](#insn-00ba4dfc) → [`00ba4e00`](#insn-00ba4e00)
- ブロック [`00ba4e00`](#insn-00ba4e00) 範囲 `[['00ba4e00', '00ba4e2f']]`
- ブロック [`00ba4e30`](#insn-00ba4e30) 範囲 `[['00ba4e30', '00ba4e43']]`
  - `FALL_THROUGH` [`00ba4e40`](#insn-00ba4e40) → [`00ba4e44`](#insn-00ba4e44)
- ブロック [`00ba4e44`](#insn-00ba4e44) 範囲 `[['00ba4e44', '00ba4e63']]`
  - `FALL_THROUGH` [`00ba4e60`](#insn-00ba4e60) → [`00ba4e64`](#insn-00ba4e64)
- ブロック [`00ba4e64`](#insn-00ba4e64) 範囲 `[['00ba4e64', '00ba4e77']]`
  - `CONDITIONAL_JUMP` [`00ba4e74`](#insn-00ba4e74) → [`00ba4e98`](#insn-00ba4e98)
  - `FALL_THROUGH` [`00ba4e74`](#insn-00ba4e74) → [`00ba4e78`](#insn-00ba4e78)
- ブロック [`00ba4e78`](#insn-00ba4e78) 範囲 `[['00ba4e78', '00ba4e7b']]`
  - `UNCONDITIONAL_JUMP` [`00ba4e78`](#insn-00ba4e78) → [`00ba4f28`](#insn-00ba4f28)
- ブロック [`00ba4e7c`](#insn-00ba4e7c) 範囲 `[['00ba4e7c', '00ba4e83']]`
  - `FALL_THROUGH` [`00ba4e80`](#insn-00ba4e80) → [`00ba4e84`](#insn-00ba4e84)
- ブロック [`00ba4e84`](#insn-00ba4e84) 範囲 `[['00ba4e84', '00ba4e8f']]`
  - `CONDITIONAL_JUMP` [`00ba4e8c`](#insn-00ba4e8c) → [`00ba4f5c`](#insn-00ba4f5c)
  - `FALL_THROUGH` [`00ba4e8c`](#insn-00ba4e8c) → [`00ba4e90`](#insn-00ba4e90)
- ブロック [`00ba4e90`](#insn-00ba4e90) 範囲 `[['00ba4e90', '00ba4e97']]`
  - `CONDITIONAL_JUMP` [`00ba4e94`](#insn-00ba4e94) → [`00ba4f28`](#insn-00ba4f28)
  - `FALL_THROUGH` [`00ba4e94`](#insn-00ba4e94) → [`00ba4e98`](#insn-00ba4e98)
- ブロック [`00ba4e98`](#insn-00ba4e98) 範囲 `[['00ba4e98', '00ba4f1b']]`
  - `CONDITIONAL_JUMP` [`00ba4f18`](#insn-00ba4f18) → [`00ba4e7c`](#insn-00ba4e7c)
  - `FALL_THROUGH` [`00ba4f18`](#insn-00ba4f18) → [`00ba4f1c`](#insn-00ba4f1c)
- ブロック [`00ba4f1c`](#insn-00ba4f1c) 範囲 `[['00ba4f1c', '00ba4f27']]`
  - `UNCONDITIONAL_JUMP` [`00ba4f24`](#insn-00ba4f24) → [`00ba4e84`](#insn-00ba4e84)
- ブロック [`00ba4f28`](#insn-00ba4f28) 範囲 `[['00ba4f28', '00ba4f2f']]`
  - `CONDITIONAL_JUMP` [`00ba4f2c`](#insn-00ba4f2c) → [`00ba5088`](#insn-00ba5088)
  - `FALL_THROUGH` [`00ba4f2c`](#insn-00ba4f2c) → [`00ba4f30`](#insn-00ba4f30)
- ブロック [`00ba4f30`](#insn-00ba4f30) 範囲 `[['00ba4f30', '00ba4f53']]`
  - `CONDITIONAL_JUMP` [`00ba4f50`](#insn-00ba4f50) → [`00ba4fc0`](#insn-00ba4fc0)
  - `FALL_THROUGH` [`00ba4f50`](#insn-00ba4f50) → [`00ba4f54`](#insn-00ba4f54)
- ブロック [`00ba4f54`](#insn-00ba4f54) 範囲 `[['00ba4f54', '00ba4f5b']]`
  - `UNCONDITIONAL_JUMP` [`00ba4f58`](#insn-00ba4f58) → [`00ba5078`](#insn-00ba5078)
- ブロック [`00ba4f5c`](#insn-00ba4f5c) 範囲 `[['00ba4f5c', '00ba4f63']]`
  - `CONDITIONAL_JUMP` [`00ba4f60`](#insn-00ba4f60) → [`00ba5088`](#insn-00ba5088)
  - `FALL_THROUGH` [`00ba4f60`](#insn-00ba4f60) → [`00ba4f64`](#insn-00ba4f64)
- ブロック [`00ba4f64`](#insn-00ba4f64) 範囲 `[['00ba4f64', '00ba4f83']]`
  - `CONDITIONAL_JUMP` [`00ba4f80`](#insn-00ba4f80) → [`00ba4fa8`](#insn-00ba4fa8)
  - `FALL_THROUGH` [`00ba4f80`](#insn-00ba4f80) → [`00ba4f84`](#insn-00ba4f84)
- ブロック [`00ba4f84`](#insn-00ba4f84) 範囲 `[['00ba4f84', '00ba4f97']]`
  - `CONDITIONAL_JUMP` [`00ba4f94`](#insn-00ba4f94) → [`00ba4fec`](#insn-00ba4fec)
  - `FALL_THROUGH` [`00ba4f94`](#insn-00ba4f94) → [`00ba4f98`](#insn-00ba4f98)
- ブロック [`00ba4f98`](#insn-00ba4f98) 範囲 `[['00ba4f98', '00ba4f9b']]`
  - `FALL_THROUGH` [`00ba4f98`](#insn-00ba4f98) → [`00ba4f9c`](#insn-00ba4f9c)
- ブロック [`00ba4f9c`](#insn-00ba4f9c) 範囲 `[['00ba4f9c', '00ba4fa7']]`
  - `CONDITIONAL_JUMP` [`00ba4fa4`](#insn-00ba4fa4) → [`00ba4fec`](#insn-00ba4fec)
  - `FALL_THROUGH` [`00ba4fa4`](#insn-00ba4fa4) → [`00ba4fa8`](#insn-00ba4fa8)
- ブロック [`00ba4fa8`](#insn-00ba4fa8) 範囲 `[['00ba4fa8', '00ba4fab']]`
  - `FALL_THROUGH` [`00ba4fa8`](#insn-00ba4fa8) → [`00ba4fac`](#insn-00ba4fac)
- ブロック [`00ba4fac`](#insn-00ba4fac) 範囲 `[['00ba4fac', '00ba4fbb']]`
  - `CONDITIONAL_JUMP` [`00ba4fb8`](#insn-00ba4fb8) → [`00ba4fac`](#insn-00ba4fac)
  - `FALL_THROUGH` [`00ba4fb8`](#insn-00ba4fb8) → [`00ba4fbc`](#insn-00ba4fbc)
- ブロック [`00ba4fbc`](#insn-00ba4fbc) 範囲 `[['00ba4fbc', '00ba4fbf']]`
  - `UNCONDITIONAL_JUMP` [`00ba4fbc`](#insn-00ba4fbc) → [`00ba5088`](#insn-00ba5088)
- ブロック [`00ba4fc0`](#insn-00ba4fc0) 範囲 `[['00ba4fc0', '00ba4fd3']]`
  - `CONDITIONAL_JUMP` [`00ba4fd0`](#insn-00ba4fd0) → [`00ba5034`](#insn-00ba5034)
  - `FALL_THROUGH` [`00ba4fd0`](#insn-00ba4fd0) → [`00ba4fd4`](#insn-00ba4fd4)
- ブロック [`00ba4fd4`](#insn-00ba4fd4) 範囲 `[['00ba4fd4', '00ba4fe3']]`
  - `CONDITIONAL_JUMP` [`00ba4fe0`](#insn-00ba4fe0) → [`00ba5034`](#insn-00ba5034)
  - `FALL_THROUGH` [`00ba4fe0`](#insn-00ba4fe0) → [`00ba4fe4`](#insn-00ba4fe4)
- ブロック [`00ba4fe4`](#insn-00ba4fe4) 範囲 `[['00ba4fe4', '00ba4feb']]`
  - `UNCONDITIONAL_JUMP` [`00ba4fe8`](#insn-00ba4fe8) → [`00ba5078`](#insn-00ba5078)
- ブロック [`00ba4fec`](#insn-00ba4fec) 範囲 `[['00ba4fec', '00ba4fff']]`
  - `FALL_THROUGH` [`00ba4ffc`](#insn-00ba4ffc) → [`00ba5000`](#insn-00ba5000)
- ブロック [`00ba5000`](#insn-00ba5000) 範囲 `[['00ba5000', '00ba5007']]`
  - `FALL_THROUGH` [`00ba5004`](#insn-00ba5004) → [`00ba5008`](#insn-00ba5008)
- ブロック [`00ba5008`](#insn-00ba5008) 範囲 `[['00ba5008', '00ba500f']]`
  - `FALL_THROUGH` [`00ba500c`](#insn-00ba500c) → [`00ba5010`](#insn-00ba5010)
- ブロック [`00ba5010`](#insn-00ba5010) 範囲 `[['00ba5010', '00ba5023']]`
  - `CONDITIONAL_JUMP` [`00ba5020`](#insn-00ba5020) → [`00ba5008`](#insn-00ba5008)
  - `FALL_THROUGH` [`00ba5020`](#insn-00ba5020) → [`00ba5024`](#insn-00ba5024)
- ブロック [`00ba5024`](#insn-00ba5024) 範囲 `[['00ba5024', '00ba502f']]`
  - `CONDITIONAL_JUMP` [`00ba502c`](#insn-00ba502c) → [`00ba4fac`](#insn-00ba4fac)
  - `FALL_THROUGH` [`00ba502c`](#insn-00ba502c) → [`00ba5030`](#insn-00ba5030)
- ブロック [`00ba5030`](#insn-00ba5030) 範囲 `[['00ba5030', '00ba5033']]`
  - `UNCONDITIONAL_JUMP` [`00ba5030`](#insn-00ba5030) → [`00ba5088`](#insn-00ba5088)
- ブロック [`00ba5034`](#insn-00ba5034) 範囲 `[['00ba5034', '00ba504f']]`
  - `FALL_THROUGH` [`00ba504c`](#insn-00ba504c) → [`00ba5050`](#insn-00ba5050)
- ブロック [`00ba5050`](#insn-00ba5050) 範囲 `[['00ba5050', '00ba5053']]`
  - `FALL_THROUGH` [`00ba5050`](#insn-00ba5050) → [`00ba5054`](#insn-00ba5054)
- ブロック [`00ba5054`](#insn-00ba5054) 範囲 `[['00ba5054', '00ba5063']]`
  - `FALL_THROUGH` [`00ba5060`](#insn-00ba5060) → [`00ba5064`](#insn-00ba5064)
- ブロック [`00ba5064`](#insn-00ba5064) 範囲 `[['00ba5064', '00ba506b']]`
  - `CONDITIONAL_JUMP` [`00ba5068`](#insn-00ba5068) → [`00ba5050`](#insn-00ba5050)
  - `FALL_THROUGH` [`00ba5068`](#insn-00ba5068) → [`00ba506c`](#insn-00ba506c)
- ブロック [`00ba506c`](#insn-00ba506c) 範囲 `[['00ba506c', '00ba5077']]`
  - `CONDITIONAL_JUMP` [`00ba5074`](#insn-00ba5074) → [`00ba5088`](#insn-00ba5088)
  - `FALL_THROUGH` [`00ba5074`](#insn-00ba5074) → [`00ba5078`](#insn-00ba5078)
- ブロック [`00ba5078`](#insn-00ba5078) 範囲 `[['00ba5078', '00ba5087']]`
  - `CONDITIONAL_JUMP` [`00ba5084`](#insn-00ba5084) → [`00ba5078`](#insn-00ba5078)
  - `FALL_THROUGH` [`00ba5084`](#insn-00ba5084) → [`00ba5088`](#insn-00ba5088)
- ブロック [`00ba5088`](#insn-00ba5088) 範囲 `[['00ba5088', '00ba5093']]`
  - `FALL_THROUGH` [`00ba5090`](#insn-00ba5090) → [`00ba5094`](#insn-00ba5094)
- ブロック [`00ba5094`](#insn-00ba5094) 範囲 `[['00ba5094', '00ba50a7']]`

## 命令位置別の参照

- [`00ba4be0`](#insn-00ba4be0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4be4`](#insn-00ba4be4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4be8`](#insn-00ba4be8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4bec`](#insn-00ba4bec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4bf0`](#insn-00ba4bf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4bf4`](#insn-00ba4bf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4c00`](#insn-00ba4c00) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4c04`](#insn-00ba4c04) → [`00ba5088`](#insn-00ba5088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4c10`](#insn-00ba4c10) → [`00ba4ca4`](#insn-00ba4ca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4c14`](#insn-00ba4c14) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4c78`](#insn-00ba4c78) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00ba4c94`](#insn-00ba4c94) → [`00ba5088`](#insn-00ba5088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4ca0`](#insn-00ba4ca0) → [`00ba5088`](#insn-00ba5088) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4cac`](#insn-00ba4cac) → [`00ba4d9c`](#insn-00ba4d9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4cb4`](#insn-00ba4cb4) → [`00ba5088`](#insn-00ba5088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4cc0`](#insn-00ba4cc0) → [`00ba5088`](#insn-00ba5088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4cc8`](#insn-00ba4cc8) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4ccc`](#insn-00ba4ccc) → [`00ba4cf0`](#insn-00ba4cf0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4cd8`](#insn-00ba4cd8) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4cec`](#insn-00ba4cec) → [`00ba5088`](#insn-00ba5088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4cfc`](#insn-00ba4cfc) → [`00ba4cdc`](#insn-00ba4cdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4d00`](#insn-00ba4d00) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4d64`](#insn-00ba4d64) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00ba4d7c`](#insn-00ba4d7c) → [`00ba4cd0`](#insn-00ba4cd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4d90`](#insn-00ba4d90) → [`00ba4d1c`](#insn-00ba4d1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4d98`](#insn-00ba4d98) → [`00ba4cd8`](#insn-00ba4cd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4db4`](#insn-00ba4db4) → [`00ba4e30`](#insn-00ba4e30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4db8`](#insn-00ba4db8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4dcc`](#insn-00ba4dcc) → [`00c5cbd0`](../00c5c/00c5cbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cbd0` · 推定シンボル `None` · 推定型 `None`
- [`00ba4dec`](#insn-00ba4dec) → [`00c5cbd0`](../00c5c/00c5cbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cbd0` · 推定シンボル `None` · 推定型 `None`
- [`00ba4e10`](#insn-00ba4e10) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4e14`](#insn-00ba4e14) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4e18`](#insn-00ba4e18) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4e1c`](#insn-00ba4e1c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4e20`](#insn-00ba4e20) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4e24`](#insn-00ba4e24) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4e2c`](#insn-00ba4e2c) → [`00c5cc60`](../00c5c/00c5cc60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cc60` · 推定シンボル `None` · 推定型 `None`
- [`00ba4e30`](#insn-00ba4e30) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4e40`](#insn-00ba4e40) → [`00c5cd00`](../00c5c/00c5cd00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cd00` · 推定シンボル `None` · 推定型 `None`
- [`00ba4e5c`](#insn-00ba4e5c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4e60`](#insn-00ba4e60) → [`00c5cd00`](../00c5c/00c5cd00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cd00` · 推定シンボル `None` · 推定型 `None`
- [`00ba4e74`](#insn-00ba4e74) → [`00ba4e98`](#insn-00ba4e98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4e78`](#insn-00ba4e78) → [`00ba4f28`](#insn-00ba4f28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4e8c`](#insn-00ba4e8c) → [`00ba4f5c`](#insn-00ba4f5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4e94`](#insn-00ba4e94) → [`00ba4f28`](#insn-00ba4f28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4e98`](#insn-00ba4e98) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4efc`](#insn-00ba4efc) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00ba4f18`](#insn-00ba4f18) → [`00ba4e7c`](#insn-00ba4e7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4f24`](#insn-00ba4f24) → [`00ba4e84`](#insn-00ba4e84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4f2c`](#insn-00ba4f2c) → [`00ba5088`](#insn-00ba5088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4f30`](#insn-00ba4f30) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4f34`](#insn-00ba4f34) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4f50`](#insn-00ba4f50) → [`00ba4fc0`](#insn-00ba4fc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4f58`](#insn-00ba4f58) → [`00ba5078`](#insn-00ba5078) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4f60`](#insn-00ba4f60) → [`00ba5088`](#insn-00ba5088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4f64`](#insn-00ba4f64) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4f80`](#insn-00ba4f80) → [`00ba4fa8`](#insn-00ba4fa8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4f94`](#insn-00ba4f94) → [`00ba4fec`](#insn-00ba4fec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4fa4`](#insn-00ba4fa4) → [`00ba4fec`](#insn-00ba4fec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4fb8`](#insn-00ba4fb8) → [`00ba4fac`](#insn-00ba4fac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4fbc`](#insn-00ba4fbc) → [`00ba5088`](#insn-00ba5088) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4fd0`](#insn-00ba4fd0) → [`00ba5034`](#insn-00ba5034) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4fe0`](#insn-00ba4fe0) → [`00ba5034`](#insn-00ba5034) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba4fe8`](#insn-00ba4fe8) → [`00ba5078`](#insn-00ba5078) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5020`](#insn-00ba5020) → [`00ba5008`](#insn-00ba5008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba502c`](#insn-00ba502c) → [`00ba4fac`](#insn-00ba4fac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5030`](#insn-00ba5030) → [`00ba5088`](#insn-00ba5088) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5068`](#insn-00ba5068) → [`00ba5050`](#insn-00ba5050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5074`](#insn-00ba5074) → [`00ba5088`](#insn-00ba5088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5084`](#insn-00ba5084) → [`00ba5078`](#insn-00ba5078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5088`](#insn-00ba5088) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba508c`](#insn-00ba508c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5090`](#insn-00ba5090) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5094`](#insn-00ba5094) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5098`](#insn-00ba5098) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba509c`](#insn-00ba509c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ba4be0`](#insn-00ba4be0)

~~~json
{
  "source": "00ba4be0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4be4`](#insn-00ba4be4)

~~~json
{
  "source": "00ba4be4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4be8`](#insn-00ba4be8)

~~~json
{
  "source": "00ba4be8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4bec`](#insn-00ba4bec)

~~~json
{
  "source": "00ba4bec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4bf0`](#insn-00ba4bf0)

~~~json
{
  "source": "00ba4bf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4bf4`](#insn-00ba4bf4)

~~~json
{
  "source": "00ba4bf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4c00`](#insn-00ba4c00)

~~~json
{
  "source": "00ba4c00",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4c04`](#insn-00ba4c04)

~~~json
{
  "source": "00ba4c04",
  "target": "00ba5088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4c10`](#insn-00ba4c10)

~~~json
{
  "source": "00ba4c10",
  "target": "00ba4ca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4c14`](#insn-00ba4c14)

~~~json
{
  "source": "00ba4c14",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4c78`](#insn-00ba4c78)

~~~json
{
  "source": "00ba4c78",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba4c94`](#insn-00ba4c94)

~~~json
{
  "source": "00ba4c94",
  "target": "00ba5088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4ca0`](#insn-00ba4ca0)

~~~json
{
  "source": "00ba4ca0",
  "target": "00ba5088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4cac`](#insn-00ba4cac)

~~~json
{
  "source": "00ba4cac",
  "target": "00ba4d9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4cb4`](#insn-00ba4cb4)

~~~json
{
  "source": "00ba4cb4",
  "target": "00ba5088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4cc0`](#insn-00ba4cc0)

~~~json
{
  "source": "00ba4cc0",
  "target": "00ba5088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4cc8`](#insn-00ba4cc8)

~~~json
{
  "source": "00ba4cc8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4ccc`](#insn-00ba4ccc)

~~~json
{
  "source": "00ba4ccc",
  "target": "00ba4cf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4cd8`](#insn-00ba4cd8)

~~~json
{
  "source": "00ba4cd8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4cec`](#insn-00ba4cec)

~~~json
{
  "source": "00ba4cec",
  "target": "00ba5088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4cfc`](#insn-00ba4cfc)

~~~json
{
  "source": "00ba4cfc",
  "target": "00ba4cdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4d00`](#insn-00ba4d00)

~~~json
{
  "source": "00ba4d00",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4d64`](#insn-00ba4d64)

~~~json
{
  "source": "00ba4d64",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba4d7c`](#insn-00ba4d7c)

~~~json
{
  "source": "00ba4d7c",
  "target": "00ba4cd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4d90`](#insn-00ba4d90)

~~~json
{
  "source": "00ba4d90",
  "target": "00ba4d1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4d98`](#insn-00ba4d98)

~~~json
{
  "source": "00ba4d98",
  "target": "00ba4cd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4db4`](#insn-00ba4db4)

~~~json
{
  "source": "00ba4db4",
  "target": "00ba4e30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4db8`](#insn-00ba4db8)

~~~json
{
  "source": "00ba4db8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4dcc`](#insn-00ba4dcc)

~~~json
{
  "source": "00ba4dcc",
  "target": "00c5cbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba4dec`](#insn-00ba4dec)

~~~json
{
  "source": "00ba4dec",
  "target": "00c5cbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba4e10`](#insn-00ba4e10)

~~~json
{
  "source": "00ba4e10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4e14`](#insn-00ba4e14)

~~~json
{
  "source": "00ba4e14",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4e18`](#insn-00ba4e18)

~~~json
{
  "source": "00ba4e18",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4e1c`](#insn-00ba4e1c)

~~~json
{
  "source": "00ba4e1c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4e20`](#insn-00ba4e20)

~~~json
{
  "source": "00ba4e20",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4e24`](#insn-00ba4e24)

~~~json
{
  "source": "00ba4e24",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4e2c`](#insn-00ba4e2c)

~~~json
{
  "source": "00ba4e2c",
  "target": "00c5cc60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba4e30`](#insn-00ba4e30)

~~~json
{
  "source": "00ba4e30",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4e40`](#insn-00ba4e40)

~~~json
{
  "source": "00ba4e40",
  "target": "00c5cd00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba4e5c`](#insn-00ba4e5c)

~~~json
{
  "source": "00ba4e5c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4e60`](#insn-00ba4e60)

~~~json
{
  "source": "00ba4e60",
  "target": "00c5cd00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba4e74`](#insn-00ba4e74)

~~~json
{
  "source": "00ba4e74",
  "target": "00ba4e98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4e78`](#insn-00ba4e78)

~~~json
{
  "source": "00ba4e78",
  "target": "00ba4f28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4e8c`](#insn-00ba4e8c)

~~~json
{
  "source": "00ba4e8c",
  "target": "00ba4f5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4e94`](#insn-00ba4e94)

~~~json
{
  "source": "00ba4e94",
  "target": "00ba4f28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4e98`](#insn-00ba4e98)

~~~json
{
  "source": "00ba4e98",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4efc`](#insn-00ba4efc)

~~~json
{
  "source": "00ba4efc",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba4f18`](#insn-00ba4f18)

~~~json
{
  "source": "00ba4f18",
  "target": "00ba4e7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4f24`](#insn-00ba4f24)

~~~json
{
  "source": "00ba4f24",
  "target": "00ba4e84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4f2c`](#insn-00ba4f2c)

~~~json
{
  "source": "00ba4f2c",
  "target": "00ba5088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4f30`](#insn-00ba4f30)

~~~json
{
  "source": "00ba4f30",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4f34`](#insn-00ba4f34)

~~~json
{
  "source": "00ba4f34",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4f50`](#insn-00ba4f50)

~~~json
{
  "source": "00ba4f50",
  "target": "00ba4fc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4f58`](#insn-00ba4f58)

~~~json
{
  "source": "00ba4f58",
  "target": "00ba5078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4f60`](#insn-00ba4f60)

~~~json
{
  "source": "00ba4f60",
  "target": "00ba5088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4f64`](#insn-00ba4f64)

~~~json
{
  "source": "00ba4f64",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4f80`](#insn-00ba4f80)

~~~json
{
  "source": "00ba4f80",
  "target": "00ba4fa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4f94`](#insn-00ba4f94)

~~~json
{
  "source": "00ba4f94",
  "target": "00ba4fec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4fa4`](#insn-00ba4fa4)

~~~json
{
  "source": "00ba4fa4",
  "target": "00ba4fec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4fb8`](#insn-00ba4fb8)

~~~json
{
  "source": "00ba4fb8",
  "target": "00ba4fac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4fbc`](#insn-00ba4fbc)

~~~json
{
  "source": "00ba4fbc",
  "target": "00ba5088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4fd0`](#insn-00ba4fd0)

~~~json
{
  "source": "00ba4fd0",
  "target": "00ba5034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4fe0`](#insn-00ba4fe0)

~~~json
{
  "source": "00ba4fe0",
  "target": "00ba5034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba4fe8`](#insn-00ba4fe8)

~~~json
{
  "source": "00ba4fe8",
  "target": "00ba5078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5020`](#insn-00ba5020)

~~~json
{
  "source": "00ba5020",
  "target": "00ba5008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba502c`](#insn-00ba502c)

~~~json
{
  "source": "00ba502c",
  "target": "00ba4fac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5030`](#insn-00ba5030)

~~~json
{
  "source": "00ba5030",
  "target": "00ba5088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5068`](#insn-00ba5068)

~~~json
{
  "source": "00ba5068",
  "target": "00ba5050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5074`](#insn-00ba5074)

~~~json
{
  "source": "00ba5074",
  "target": "00ba5088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5084`](#insn-00ba5084)

~~~json
{
  "source": "00ba5084",
  "target": "00ba5078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5088`](#insn-00ba5088)

~~~json
{
  "source": "00ba5088",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba508c`](#insn-00ba508c)

~~~json
{
  "source": "00ba508c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5090`](#insn-00ba5090)

~~~json
{
  "source": "00ba5090",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5094`](#insn-00ba5094)

~~~json
{
  "source": "00ba5094",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5098`](#insn-00ba5098)

~~~json
{
  "source": "00ba5098",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba509c`](#insn-00ba509c)

~~~json
{
  "source": "00ba509c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
