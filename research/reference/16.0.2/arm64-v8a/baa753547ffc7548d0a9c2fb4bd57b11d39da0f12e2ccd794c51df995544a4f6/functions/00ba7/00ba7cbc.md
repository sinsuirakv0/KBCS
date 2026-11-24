# 00ba7cbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00ba7c20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba7/00ba7c20.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0078.md#compare-8dedf88a218b8df79e4717c5732ad510)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00ba8cb0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ba8/00ba8cb0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0034.md#compare-5c37b22c9d1b7abe79c9e7ac7988e7e4)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ba7cbc",
  "name": "_ZNSt6__ndk115__inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection10SchemaFileEEEPNS1_6OffsetIS6_EEEEvT0_SC_SC_T_NS_15iterator_traitsISC_E15difference_typeESG_PNSF_10value_typeEl",
  "size": 1064,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e30ef4e2cbfd5685746e0eba2e7b0459913034516d26dadc07462ba18cb9691b",
  "source_text_sha256": "e30ef4e2cbfd5685746e0eba2e7b0459913034516d26dadc07462ba18cb9691b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ba7cbc",
        "00ba80e3"
      ]
    ],
    "bytes_sha256": "2453fa9be8332b4a412d59a9fcd3a07f7b7fd5666a181ac72924238bf4b9d6b9",
    "instruction_count": 266,
    "instruction_bytes": 1064,
    "body_bytes": 1064,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5cc50](../00c5c/00c5cc50.md)

## 呼び出し先

- [00ba86b0](../00ba8/00ba86b0.md)
- [00c58120](../00c58/00c58120.md)
- [00c5cc50](../00c5c/00c5cc50.md)
- [00c5ce10](../00c5c/00c5ce10.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 7925 bytes

~~~c

void _ZNSt6__ndk115__inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection10SchemaFileEEEPNS1_6OffsetIS6_EEEEvT0_SC_SC_T_NS_15iterator_traitsISC_E15difference_typeESG_PNSF_10value_typeEl
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
                    /* try { // try from 00ba80c8 to 00ca80fb has its CatchHandler @ 00ba8250 */
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
                    /* try { // try from 00ba7d6c to 00ca7d77 has its CatchHandler @ 00ba8324 */
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
                    /* try { // try from 00ba7dd8 to 00ca7ddf has its CatchHandler @ 00ba8328 */
      lVar14 = param_6;
                    /* try { // try from 00ba7de0 to 00ca7e4f has its CatchHandler @ 00ba7950 */
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
                    /* try { // try from 00ba7e50 to 00ca7e63 has its CatchHandler @ 00ba818c */
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
                    /* try { // try from 00ba7fac to 00ca7fb7 has its CatchHandler @ 00ba81f0 */
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
                    /* try { // try from 00ba7f10 to 00ca7f23 has its CatchHandler @ 00ba8188 */
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
                    /* try { // try from 00ba7f74 to 00ca7f7f has its CatchHandler @ 00ba8214 */
          if (!bVar8) {
            puVar13 = puVar12;
            uVar15 = uVar17;
          }
          puVar12 = puVar13;
        } while (uVar15 != 0);
      }
      lVar14 = (long)puVar13 - (long)param_2 >> 2;
    }
                    /* try { // try from 00ba7fcc to 00ca7fd7 has its CatchHandler @ 00ba81d8 */
    lVar18 = (param_5 - lVar11) - lVar16;
    param_1 = puVar13;
    if ((puVar20 != param_2) && (param_1 = puVar20, param_2 != puVar13)) {
                    /* try { // try from 00ba7ff8 to 00ca8003 has its CatchHandler @ 00ba81cc */
      param_1 = (uint *)FUN_00ba86b0(puVar20,param_2,puVar13);
    }
                    /* try { // try from 00ba801c to 00ca8027 has its CatchHandler @ 00ba81c8 */
    if (lVar14 + lVar11 < ((param_6 + param_5) - (lVar14 + lVar11)) - lVar16) {
                    /* try { // try from 00ba8030 to 00ca803b has its CatchHandler @ 00ba81c0 */
      _ZNSt6__ndk115__inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection10SchemaFileEEEPNS1_6OffsetIS6_EEEEvT0_SC_SC_T_NS_15iterator_traitsISC_E15difference_typeESG_PNSF_10value_typeEl
                (puVar19,puVar20,param_1,param_4,lVar11,lVar14,param_7,param_8);
      param_2 = puVar13;
      param_6 = param_6 - lVar14;
      param_5 = lVar18;
    }
    else {
                    /* try { // try from 00ba8050 to 00ca805b has its CatchHandler @ 00ba81ac */
                    /* try { // try from 00ba805c to 00ca8067 has its CatchHandler @ 00ba81a8 */
      _ZNSt6__ndk115__inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection10SchemaFileEEEPNS1_6OffsetIS6_EEEEvT0_SC_SC_T_NS_15iterator_traitsISC_E15difference_typeESG_PNSF_10value_typeEl
                (param_1,puVar13,param_3,param_4,lVar18,param_6 - lVar14,param_7,param_8);
                    /* try { // try from 00ba8068 to 00ca8073 has its CatchHandler @ 00ba81a4 */
      param_3 = param_1;
      param_2 = puVar20;
      param_6 = lVar14;
      param_5 = lVar11;
      param_1 = puVar19;
    }
  }
                    /* try { // try from 00ba8088 to 00ca80c3 has its CatchHandler @ 00ba8224 */
  _ZNSt6__ndk124__buffered_inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection10SchemaFileEEEPNS1_6OffsetIS6_EEEEvT0_SC_SC_T_NS_15iterator_traitsISC_E15difference_typeESG_PNSF_10value_typeE
            (param_1,param_2,param_3,param_4,param_5,param_6,param_7);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ba7cbc"></a> `00ba7cbc` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00ba7cc0"></a> `00ba7cc0` | `fc 6f 05 a9` | stp x28,x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ba7cc4"></a> `00ba7cc4` | `fa 67 06 a9` | stp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ba7cc8"></a> `00ba7cc8` | `f8 5f 07 a9` | stp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ba7ccc"></a> `00ba7ccc` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00ba7cd0"></a> `00ba7cd0` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00ba7cd4"></a> `00ba7cd4` | `fd 7b 0a a9` | stp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00ba7cd8"></a> `00ba7cd8` | `fd 83 02 91` | add x29,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00ba7cdc"></a> `00ba7cdc` | `e3 9f 02 a9` | stp x3,x7,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00ba7ce0"></a> `00ba7ce0` | `e6 8b 01 a9` | stp x6,x2,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ba7ce4"></a> `00ba7ce4` | `e1 97 03 a9` | stp x1,x5,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00ba7ce8"></a> `00ba7ce8` | `e5 1e 00 b4` | cbz x5,0x00ba80c4 | `CONDITIONAL_JUMP`
<a id="insn-00ba7cec"></a> `00ba7cec` | `f7 03 04 aa` | mov x23,x4 | `FALL_THROUGH`
<a id="insn-00ba7cf0"></a> `00ba7cf0` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00ba7cf4"></a> `00ba7cf4` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba7cf8"></a> `00ba7cf8` | `e5 23 40 f9` | ldr x5,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ba7cfc"></a> `00ba7cfc` | `bf 00 08 eb` | cmp x5,x8 | `FALL_THROUGH`
<a id="insn-00ba7d00"></a> `00ba7d00` | `2d 1c 00 54` | b.le 0x00ba8084 | `CONDITIONAL_JUMP`
<a id="insn-00ba7d04"></a> `00ba7d04` | `ff 02 08 eb` | cmp x23,x8 | `FALL_THROUGH`
<a id="insn-00ba7d08"></a> `00ba7d08` | `ed 1b 00 54` | b.le 0x00ba8084 | `CONDITIONAL_JUMP`
<a id="insn-00ba7d0c"></a> `00ba7d0c` | `d7 1d 00 b4` | cbz x23,0x00ba80c4 | `CONDITIONAL_JUMP`
<a id="insn-00ba7d10"></a> `00ba7d10` | `e8 17 40 f9` | ldr x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00ba7d14"></a> `00ba7d14` | `ea 1f 40 f9` | ldr x10,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00ba7d18"></a> `00ba7d18` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00ba7d1c"></a> `00ba7d1c` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00ba7d20"></a> `00ba7d20` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ba7d24"></a> `00ba7d24` | `58 01 40 b9` | ldr w24,[x10] | `FALL_THROUGH`
<a id="insn-00ba7d28"></a> `00ba7d28` | `09 1d 40 f9` | ldr x9,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00ba7d2c"></a> `00ba7d2c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00ba7d30"></a> `00ba7d30` | `2a 01 08 8b` | add x10,x9,x8 | `FALL_THROUGH`
<a id="insn-00ba7d34"></a> `00ba7d34` | `48 01 18 cb` | sub x8,x10,x24 | `FALL_THROUGH`
<a id="insn-00ba7d38"></a> `00ba7d38` | `09 01 80 b9` | ldrsw x9,[x8] | `FALL_THROUGH`
<a id="insn-00ba7d3c"></a> `00ba7d3c` | `09 01 09 cb` | sub x9,x8,x9 | `FALL_THROUGH`
<a id="insn-00ba7d40"></a> `00ba7d40` | `29 09 40 79` | ldrh w9,[x9, #0x4] | `FALL_THROUGH`
<a id="insn-00ba7d44"></a> `00ba7d44` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00ba7d48"></a> `00ba7d48` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00ba7d4c"></a> `00ba7d4c` | `13 01 09 8b` | add x19,x8,x9 | `FALL_THROUGH`
<a id="insn-00ba7d50"></a> `00ba7d50` | `7c 46 40 b8` | ldr w28,[x19], #0x4 | `FALL_THROUGH`
<a id="insn-00ba7d54"></a> `00ba7d54` | `d9 7a 75 b8` | ldr w25,[x22, x21, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00ba7d58"></a> `00ba7d58` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba7d5c"></a> `00ba7d5c` | `fb 03 0a aa` | mov x27,x10 | `FALL_THROUGH`
<a id="insn-00ba7d60"></a> `00ba7d60` | `48 01 19 cb` | sub x8,x10,x25 | `FALL_THROUGH`
<a id="insn-00ba7d64"></a> `00ba7d64` | `09 01 80 b9` | ldrsw x9,[x8] | `FALL_THROUGH`
<a id="insn-00ba7d68"></a> `00ba7d68` | `09 01 09 cb` | sub x9,x8,x9 | `FALL_THROUGH`
<a id="insn-00ba7d6c"></a> `00ba7d6c` | `29 09 40 79` | ldrh w9,[x9, #0x4] | `FALL_THROUGH`
<a id="insn-00ba7d70"></a> `00ba7d70` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00ba7d74"></a> `00ba7d74` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00ba7d78"></a> `00ba7d78` | `01 01 09 8b` | add x1,x8,x9 | `FALL_THROUGH`
<a id="insn-00ba7d7c"></a> `00ba7d7c` | `3a 44 40 b8` | ldr w26,[x1], #0x4 | `FALL_THROUGH`
<a id="insn-00ba7d80"></a> `00ba7d80` | `5f 03 1c 6b` | cmp w26,w28 | `FALL_THROUGH`
<a id="insn-00ba7d84"></a> `00ba7d84` | `42 33 9c 1a` | csel w2,w26,w28,cc | `FALL_THROUGH`
<a id="insn-00ba7d88"></a> `00ba7d88` | `e6 c0 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00ba7d8c"></a> `00ba7d8c` | `9f 03 1a 6b` | cmp w28,w26 | `FALL_THROUGH`
<a id="insn-00ba7d90"></a> `00ba7d90` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00ba7d94"></a> `00ba7d94` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00ba7d98"></a> `00ba7d98` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00ba7d9c"></a> `00ba7d9c` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00ba7da0"></a> `00ba7da0` | `e8 00 00 37` | tbnz w8,#0x0,0x00ba7dbc | `CONDITIONAL_JUMP`
<a id="insn-00ba7da4"></a> `00ba7da4` | `b5 06 00 91` | add x21,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00ba7da8"></a> `00ba7da8` | `ff 02 15 eb` | cmp x23,x21 | `FALL_THROUGH`
<a id="insn-00ba7dac"></a> `00ba7dac` | `94 12 00 d1` | sub x20,x20,#0x4 | `FALL_THROUGH`
<a id="insn-00ba7db0"></a> `00ba7db0` | `ea 03 1b aa` | mov x10,x27 | `FALL_THROUGH`
<a id="insn-00ba7db4"></a> `00ba7db4` | `01 fd ff 54` | b.ne 0x00ba7d54 | `CONDITIONAL_JUMP`
<a id="insn-00ba7db8"></a> `00ba7db8` | `c3 00 00 14` | b 0x00ba80c4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba7dbc"></a> `00ba7dbc` | `fa 23 40 f9` | ldr x26,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ba7dc0"></a> `00ba7dc0` | `e8 02 15 cb` | sub x8,x23,x21 | `FALL_THROUGH`
<a id="insn-00ba7dc4"></a> `00ba7dc4` | `ea 03 17 aa` | mov x10,x23 | `FALL_THROUGH`
<a id="insn-00ba7dc8"></a> `00ba7dc8` | `dc 02 14 cb` | sub x28,x22,x20 | `FALL_THROUGH`
<a id="insn-00ba7dcc"></a> `00ba7dcc` | `1f 01 1a eb` | cmp x8,x26 | `FALL_THROUGH`
<a id="insn-00ba7dd0"></a> `00ba7dd0` | `fc 0b 00 f9` | str x28,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba7dd4"></a> `00ba7dd4` | `ca 06 00 54` | b.ge 0x00ba7eac | `CONDITIONAL_JUMP`
<a id="insn-00ba7dd8"></a> `00ba7dd8` | `e1 1f 40 f9` | ldr x1,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00ba7ddc"></a> `00ba7ddc` | `5f 03 00 f1` | cmp x26,#0x0 | `FALL_THROUGH`
<a id="insn-00ba7de0"></a> `00ba7de0` | `48 a7 9a 9a` | cinc x8,x26,lt | `FALL_THROUGH`
<a id="insn-00ba7de4"></a> `00ba7de4` | `14 fd 41 93` | asr x20,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ba7de8"></a> `00ba7de8` | `28 00 1c eb` | subs x8,x1,x28 | `FALL_THROUGH`
<a id="insn-00ba7dec"></a> `00ba7dec` | `33 08 14 8b` | add x19,x1,x20, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ba7df0"></a> `00ba7df0` | `40 0d 00 54` | b.eq 0x00ba7f98 | `CONDITIONAL_JUMP`
<a id="insn-00ba7df4"></a> `00ba7df4` | `69 02 40 b9` | ldr w9,[x19] | `FALL_THROUGH`
<a id="insn-00ba7df8"></a> `00ba7df8` | `f4 07 00 f9` | str x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ba7dfc"></a> `00ba7dfc` | `eb 03 1b aa` | mov x11,x27 | `FALL_THROUGH`
<a id="insn-00ba7e00"></a> `00ba7e00` | `14 fd 42 93` | asr x20,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00ba7e04"></a> `00ba7e04` | `69 03 09 cb` | sub x9,x27,x9 | `FALL_THROUGH`
<a id="insn-00ba7e08"></a> `00ba7e08` | `2a 01 80 b9` | ldrsw x10,[x9] | `FALL_THROUGH`
<a id="insn-00ba7e0c"></a> `00ba7e0c` | `2a 01 0a cb` | sub x10,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba7e10"></a> `00ba7e10` | `4a 09 40 79` | ldrh w10,[x10, #0x4] | `FALL_THROUGH`
<a id="insn-00ba7e14"></a> `00ba7e14` | `29 01 0a 8b` | add x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba7e18"></a> `00ba7e18` | `2a 01 40 b9` | ldr w10,[x9] | `FALL_THROUGH`
<a id="insn-00ba7e1c"></a> `00ba7e1c` | `29 01 0a 8b` | add x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba7e20"></a> `00ba7e20` | `36 45 40 b8` | ldr w22,[x9], #0x4 | `FALL_THROUGH`
<a id="insn-00ba7e24"></a> `00ba7e24` | `e9 27 00 f9` | str x9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00ba7e28"></a> `00ba7e28` | `99 fe 41 d3` | lsr x25,x20,#0x1 | `FALL_THROUGH`
<a id="insn-00ba7e2c"></a> `00ba7e2c` | `9a 0b 19 8b` | add x26,x28,x25, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ba7e30"></a> `00ba7e30` | `48 47 40 b8` | ldr w8,[x26], #0x4 | `FALL_THROUGH`
<a id="insn-00ba7e34"></a> `00ba7e34` | `68 01 08 cb` | sub x8,x11,x8 | `FALL_THROUGH`
<a id="insn-00ba7e38"></a> `00ba7e38` | `09 01 80 b9` | ldrsw x9,[x8] | `FALL_THROUGH`
<a id="insn-00ba7e3c"></a> `00ba7e3c` | `09 01 09 cb` | sub x9,x8,x9 | `FALL_THROUGH`
<a id="insn-00ba7e40"></a> `00ba7e40` | `29 09 40 79` | ldrh w9,[x9, #0x4] | `FALL_THROUGH`
<a id="insn-00ba7e44"></a> `00ba7e44` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00ba7e48"></a> `00ba7e48` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00ba7e4c"></a> `00ba7e4c` | `01 01 09 8b` | add x1,x8,x9 | `FALL_THROUGH`
<a id="insn-00ba7e50"></a> `00ba7e50` | `38 44 40 b8` | ldr w24,[x1], #0x4 | `FALL_THROUGH`
<a id="insn-00ba7e54"></a> `00ba7e54` | `e0 27 40 f9` | ldr x0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00ba7e58"></a> `00ba7e58` | `1f 03 16 6b` | cmp w24,w22 | `FALL_THROUGH`
<a id="insn-00ba7e5c"></a> `00ba7e5c` | `02 33 96 1a` | csel w2,w24,w22,cc | `FALL_THROUGH`
<a id="insn-00ba7e60"></a> `00ba7e60` | `b0 c0 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00ba7e64"></a> `00ba7e64` | `df 02 18 6b` | cmp w22,w24 | `FALL_THROUGH`
<a id="insn-00ba7e68"></a> `00ba7e68` | `e9 27 9f 1a` | cset w9,cc | `FALL_THROUGH`
<a id="insn-00ba7e6c"></a> `00ba7e6c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00ba7e70"></a> `00ba7e70` | `ea a7 9f 1a` | cset w10,lt | `FALL_THROUGH`
<a id="insn-00ba7e74"></a> `00ba7e74` | `e8 03 39 aa` | mvn x8,x25 | `FALL_THROUGH`
<a id="insn-00ba7e78"></a> `00ba7e78` | `29 01 8a 1a` | csel w9,w9,w10,eq | `FALL_THROUGH`
<a id="insn-00ba7e7c"></a> `00ba7e7c` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00ba7e80"></a> `00ba7e80` | `3f 01 00 71` | cmp w9,#0x0 | `FALL_THROUGH`
<a id="insn-00ba7e84"></a> `00ba7e84` | `eb 03 1b aa` | mov x11,x27 | `FALL_THROUGH`
<a id="insn-00ba7e88"></a> `00ba7e88` | `34 13 88 9a` | csel x20,x25,x8,ne | `FALL_THROUGH`
<a id="insn-00ba7e8c"></a> `00ba7e8c` | `9c 13 9a 9a` | csel x28,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00ba7e90"></a> `00ba7e90` | `d4 fc ff b5` | cbnz x20,0x00ba7e28 | `CONDITIONAL_JUMP`
<a id="insn-00ba7e94"></a> `00ba7e94` | `e8 1b 41 a9` | ldp x8,x6,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba7e98"></a> `00ba7e98` | `e7 07 43 a9` | ldp x7,x1,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba7e9c"></a> `00ba7e9c` | `fa 23 40 f9` | ldr x26,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ba7ea0"></a> `00ba7ea0` | `f4 07 40 f9` | ldr x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ba7ea4"></a> `00ba7ea4` | `ea 03 17 aa` | mov x10,x23 | `FALL_THROUGH`
<a id="insn-00ba7ea8"></a> `00ba7ea8` | `3f 00 00 14` | b 0x00ba7fa4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba7eac"></a> `00ba7eac` | `49 05 00 d1` | sub x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00ba7eb0"></a> `00ba7eb0` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00ba7eb4"></a> `00ba7eb4` | `20 10 00 54` | b.eq 0x00ba80b8 | `CONDITIONAL_JUMP`
<a id="insn-00ba7eb8"></a> `00ba7eb8` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00ba7ebc"></a> `00ba7ebc` | `08 a5 88 9a` | cinc x8,x8,lt | `FALL_THROUGH`
<a id="insn-00ba7ec0"></a> `00ba7ec0` | `04 fd 41 93` | asr x4,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ba7ec4"></a> `00ba7ec4` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba7ec8"></a> `00ba7ec8` | `e1 1f 40 f9` | ldr x1,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00ba7ecc"></a> `00ba7ecc` | `c9 0a 04 8b` | add x9,x22,x4, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ba7ed0"></a> `00ba7ed0` | `3c 01 14 cb` | sub x28,x9,x20 | `FALL_THROUGH`
<a id="insn-00ba7ed4"></a> `00ba7ed4` | `08 01 01 eb` | subs x8,x8,x1 | `FALL_THROUGH`
<a id="insn-00ba7ed8"></a> `00ba7ed8` | `c0 06 00 54` | b.eq 0x00ba7fb0 | `CONDITIONAL_JUMP`
<a id="insn-00ba7edc"></a> `00ba7edc` | `29 79 75 b8` | ldr w9,[x9, x21, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00ba7ee0"></a> `00ba7ee0` | `e4 07 00 f9` | str x4,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ba7ee4"></a> `00ba7ee4` | `eb 03 1b aa` | mov x11,x27 | `FALL_THROUGH`
<a id="insn-00ba7ee8"></a> `00ba7ee8` | `16 fd 42 93` | asr x22,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00ba7eec"></a> `00ba7eec` | `69 03 09 cb` | sub x9,x27,x9 | `FALL_THROUGH`
<a id="insn-00ba7ef0"></a> `00ba7ef0` | `2a 01 80 b9` | ldrsw x10,[x9] | `FALL_THROUGH`
<a id="insn-00ba7ef4"></a> `00ba7ef4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00ba7ef8"></a> `00ba7ef8` | `2a 01 0a cb` | sub x10,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba7efc"></a> `00ba7efc` | `4a 09 40 79` | ldrh w10,[x10, #0x4] | `FALL_THROUGH`
<a id="insn-00ba7f00"></a> `00ba7f00` | `29 01 0a 8b` | add x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba7f04"></a> `00ba7f04` | `2a 01 40 b9` | ldr w10,[x9] | `FALL_THROUGH`
<a id="insn-00ba7f08"></a> `00ba7f08` | `29 01 0a 8b` | add x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba7f0c"></a> `00ba7f0c` | `34 45 40 b8` | ldr w20,[x9], #0x4 | `FALL_THROUGH`
<a id="insn-00ba7f10"></a> `00ba7f10` | `e9 27 00 f9` | str x9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00ba7f14"></a> `00ba7f14` | `d8 fe 41 d3` | lsr x24,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00ba7f18"></a> `00ba7f18` | `79 0a 18 8b` | add x25,x19,x24, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ba7f1c"></a> `00ba7f1c` | `28 47 40 b8` | ldr w8,[x25], #0x4 | `FALL_THROUGH`
<a id="insn-00ba7f20"></a> `00ba7f20` | `68 01 08 cb` | sub x8,x11,x8 | `FALL_THROUGH`
<a id="insn-00ba7f24"></a> `00ba7f24` | `09 01 80 b9` | ldrsw x9,[x8] | `FALL_THROUGH`
<a id="insn-00ba7f28"></a> `00ba7f28` | `09 01 09 cb` | sub x9,x8,x9 | `FALL_THROUGH`
<a id="insn-00ba7f2c"></a> `00ba7f2c` | `29 09 40 79` | ldrh w9,[x9, #0x4] | `FALL_THROUGH`
<a id="insn-00ba7f30"></a> `00ba7f30` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00ba7f34"></a> `00ba7f34` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00ba7f38"></a> `00ba7f38` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00ba7f3c"></a> `00ba7f3c` | `1a 44 40 b8` | ldr w26,[x0], #0x4 | `FALL_THROUGH`
<a id="insn-00ba7f40"></a> `00ba7f40` | `e1 27 40 f9` | ldr x1,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00ba7f44"></a> `00ba7f44` | `9f 02 1a 6b` | cmp w20,w26 | `FALL_THROUGH`
<a id="insn-00ba7f48"></a> `00ba7f48` | `82 32 9a 1a` | csel w2,w20,w26,cc | `FALL_THROUGH`
<a id="insn-00ba7f4c"></a> `00ba7f4c` | `75 c0 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00ba7f50"></a> `00ba7f50` | `5f 03 14 6b` | cmp w26,w20 | `FALL_THROUGH`
<a id="insn-00ba7f54"></a> `00ba7f54` | `e9 27 9f 1a` | cset w9,cc | `FALL_THROUGH`
<a id="insn-00ba7f58"></a> `00ba7f58` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00ba7f5c"></a> `00ba7f5c` | `ea a7 9f 1a` | cset w10,lt | `FALL_THROUGH`
<a id="insn-00ba7f60"></a> `00ba7f60` | `e8 03 38 aa` | mvn x8,x24 | `FALL_THROUGH`
<a id="insn-00ba7f64"></a> `00ba7f64` | `29 01 8a 1a` | csel w9,w9,w10,eq | `FALL_THROUGH`
<a id="insn-00ba7f68"></a> `00ba7f68` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00ba7f6c"></a> `00ba7f6c` | `3f 01 00 71` | cmp w9,#0x0 | `FALL_THROUGH`
<a id="insn-00ba7f70"></a> `00ba7f70` | `eb 03 1b aa` | mov x11,x27 | `FALL_THROUGH`
<a id="insn-00ba7f74"></a> `00ba7f74` | `16 11 98 9a` | csel x22,x8,x24,ne | `FALL_THROUGH`
<a id="insn-00ba7f78"></a> `00ba7f78` | `33 13 93 9a` | csel x19,x25,x19,ne | `FALL_THROUGH`
<a id="insn-00ba7f7c"></a> `00ba7f7c` | `d6 fc ff b5` | cbnz x22,0x00ba7f14 | `CONDITIONAL_JUMP`
<a id="insn-00ba7f80"></a> `00ba7f80` | `e6 0f 40 f9` | ldr x6,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ba7f84"></a> `00ba7f84` | `e7 07 43 a9` | ldp x7,x1,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba7f88"></a> `00ba7f88` | `fa 23 40 f9` | ldr x26,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ba7f8c"></a> `00ba7f8c` | `e4 07 40 f9` | ldr x4,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ba7f90"></a> `00ba7f90` | `ea 03 17 aa` | mov x10,x23 | `FALL_THROUGH`
<a id="insn-00ba7f94"></a> `00ba7f94` | `0a 00 00 14` | b 0x00ba7fbc | `UNCONDITIONAL_JUMP`
<a id="insn-00ba7f98"></a> `00ba7f98` | `e7 1b 40 f9` | ldr x7,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba7f9c"></a> `00ba7f9c` | `e6 0f 40 f9` | ldr x6,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ba7fa0"></a> `00ba7fa0` | `e8 03 1c aa` | mov x8,x28 | `FALL_THROUGH`
<a id="insn-00ba7fa4"></a> `00ba7fa4` | `88 03 08 cb` | sub x8,x28,x8 | `FALL_THROUGH`
<a id="insn-00ba7fa8"></a> `00ba7fa8` | `04 fd 42 93` | asr x4,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00ba7fac"></a> `00ba7fac` | `06 00 00 14` | b 0x00ba7fc4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba7fb0"></a> `00ba7fb0` | `e7 1b 40 f9` | ldr x7,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba7fb4"></a> `00ba7fb4` | `e6 0f 40 f9` | ldr x6,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ba7fb8"></a> `00ba7fb8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00ba7fbc"></a> `00ba7fbc` | `68 02 01 cb` | sub x8,x19,x1 | `FALL_THROUGH`
<a id="insn-00ba7fc0"></a> `00ba7fc0` | `14 fd 42 93` | asr x20,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00ba7fc4"></a> `00ba7fc4` | `48 01 04 cb` | sub x8,x10,x4 | `FALL_THROUGH`
<a id="insn-00ba7fc8"></a> `00ba7fc8` | `9f 03 01 eb` | cmp x28,x1 | `FALL_THROUGH`
<a id="insn-00ba7fcc"></a> `00ba7fcc` | `1b 01 15 cb` | sub x27,x8,x21 | `FALL_THROUGH`
<a id="insn-00ba7fd0"></a> `00ba7fd0` | `59 03 14 cb` | sub x25,x26,x20 | `FALL_THROUGH`
<a id="insn-00ba7fd4"></a> `00ba7fd4` | `f6 03 13 aa` | mov x22,x19 | `FALL_THROUGH`
<a id="insn-00ba7fd8"></a> `00ba7fd8` | `c0 01 00 54` | b.eq 0x00ba8010 | `CONDITIONAL_JUMP`
<a id="insn-00ba7fdc"></a> `00ba7fdc` | `3f 00 13 eb` | cmp x1,x19 | `FALL_THROUGH`
<a id="insn-00ba7fe0"></a> `00ba7fe0` | `f6 03 1c aa` | mov x22,x28 | `FALL_THROUGH`
<a id="insn-00ba7fe4"></a> `00ba7fe4` | `60 01 00 54` | b.eq 0x00ba8010 | `CONDITIONAL_JUMP`
<a id="insn-00ba7fe8"></a> `00ba7fe8` | `e0 03 1c aa` | mov x0,x28 | `FALL_THROUGH`
<a id="insn-00ba7fec"></a> `00ba7fec` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00ba7ff0"></a> `00ba7ff0` | `f6 03 04 aa` | mov x22,x4 | `FALL_THROUGH`
<a id="insn-00ba7ff4"></a> `00ba7ff4` | `f8 03 07 aa` | mov x24,x7 | `FALL_THROUGH`
<a id="insn-00ba7ff8"></a> `00ba7ff8` | `ae 01 00 94` | bl 0x00ba86b0 | `UNCONDITIONAL_CALL`
<a id="insn-00ba7ffc"></a> `00ba7ffc` | `e6 0f 40 f9` | ldr x6,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ba8000"></a> `00ba8000` | `e7 03 18 aa` | mov x7,x24 | `FALL_THROUGH`
<a id="insn-00ba8004"></a> `00ba8004` | `e4 03 16 aa` | mov x4,x22 | `FALL_THROUGH`
<a id="insn-00ba8008"></a> `00ba8008` | `ea 03 17 aa` | mov x10,x23 | `FALL_THROUGH`
<a id="insn-00ba800c"></a> `00ba800c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00ba8010"></a> `00ba8010` | `88 02 04 8b` | add x8,x20,x4 | `FALL_THROUGH`
<a id="insn-00ba8014"></a> `00ba8014` | `49 03 0a 8b` | add x9,x26,x10 | `FALL_THROUGH`
<a id="insn-00ba8018"></a> `00ba8018` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-00ba801c"></a> `00ba801c` | `29 01 15 cb` | sub x9,x9,x21 | `FALL_THROUGH`
<a id="insn-00ba8020"></a> `00ba8020` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ba8024"></a> `00ba8024` | `0a 01 00 54` | b.ge 0x00ba8044 | `CONDITIONAL_JUMP`
<a id="insn-00ba8028"></a> `00ba8028` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba802c"></a> `00ba802c` | `e3 17 40 f9` | ldr x3,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00ba8030"></a> `00ba8030` | `e1 03 1c aa` | mov x1,x28 | `FALL_THROUGH`
<a id="insn-00ba8034"></a> `00ba8034` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00ba8038"></a> `00ba8038` | `e5 03 14 aa` | mov x5,x20 | `FALL_THROUGH`
<a id="insn-00ba803c"></a> `00ba803c` | `05 d3 02 94` | bl 0x00c5cc50 | `UNCONDITIONAL_CALL`
<a id="insn-00ba8040"></a> `00ba8040` | `0d 00 00 14` | b 0x00ba8074 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba8044"></a> `00ba8044` | `e2 0f 42 a9` | ldp x2,x3,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba8048"></a> `00ba8048` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00ba804c"></a> `00ba804c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00ba8050"></a> `00ba8050` | `f3 03 04 aa` | mov x19,x4 | `FALL_THROUGH`
<a id="insn-00ba8054"></a> `00ba8054` | `e4 03 1b aa` | mov x4,x27 | `FALL_THROUGH`
<a id="insn-00ba8058"></a> `00ba8058` | `e5 03 19 aa` | mov x5,x25 | `FALL_THROUGH`
<a id="insn-00ba805c"></a> `00ba805c` | `fd d2 02 94` | bl 0x00c5cc50 | `UNCONDITIONAL_CALL`
<a id="insn-00ba8060"></a> `00ba8060` | `f6 13 00 f9` | str x22,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba8064"></a> `00ba8064` | `f6 0b 40 f9` | ldr x22,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba8068"></a> `00ba8068` | `f9 03 14 aa` | mov x25,x20 | `FALL_THROUGH`
<a id="insn-00ba806c"></a> `00ba806c` | `fb 03 13 aa` | mov x27,x19 | `FALL_THROUGH`
<a id="insn-00ba8070"></a> `00ba8070` | `f3 03 1c aa` | mov x19,x28 | `FALL_THROUGH`
<a id="insn-00ba8074"></a> `00ba8074` | `f7 03 1b aa` | mov x23,x27 | `FALL_THROUGH`
<a id="insn-00ba8078"></a> `00ba8078` | `f3 e7 03 a9` | stp x19,x25,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00ba807c"></a> `00ba807c` | `d9 e3 ff b5` | cbnz x25,0x00ba7cf4 | `CONDITIONAL_JUMP`
<a id="insn-00ba8080"></a> `00ba8080` | `11 00 00 14` | b 0x00ba80c4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba8084"></a> `00ba8084` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00ba8088"></a> `00ba8088` | `e1 1f 40 f9` | ldr x1,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00ba808c"></a> `00ba808c` | `e2 0f 42 a9` | ldp x2,x3,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba8090"></a> `00ba8090` | `e4 03 17 aa` | mov x4,x23 | `FALL_THROUGH`
<a id="insn-00ba8094"></a> `00ba8094` | `e6 0f 40 f9` | ldr x6,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ba8098"></a> `00ba8098` | `fd 7b 4a a9` | ldp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00ba809c"></a> `00ba809c` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00ba80a0"></a> `00ba80a0` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00ba80a4"></a> `00ba80a4` | `f8 5f 47 a9` | ldp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ba80a8"></a> `00ba80a8` | `fa 67 46 a9` | ldp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ba80ac"></a> `00ba80ac` | `fc 6f 45 a9` | ldp x28,x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ba80b0"></a> `00ba80b0` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00ba80b4"></a> `00ba80b4` | `57 d3 02 14` | b 0x00c5ce10 | `CALL_TERMINATOR`
<a id="insn-00ba80b8"></a> `00ba80b8` | `e8 1f 40 f9` | ldr x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00ba80bc"></a> `00ba80bc` | `d8 7a 35 b8` | str w24,[x22, x21, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00ba80c0"></a> `00ba80c0` | `19 01 00 b9` | str w25,[x8] | `FALL_THROUGH`
<a id="insn-00ba80c4"></a> `00ba80c4` | `fd 7b 4a a9` | ldp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00ba80c8"></a> `00ba80c8` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00ba80cc"></a> `00ba80cc` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00ba80d0"></a> `00ba80d0` | `f8 5f 47 a9` | ldp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ba80d4"></a> `00ba80d4` | `fa 67 46 a9` | ldp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ba80d8"></a> `00ba80d8` | `fc 6f 45 a9` | ldp x28,x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ba80dc"></a> `00ba80dc` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00ba80e0"></a> `00ba80e0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ba7cbc`](#insn-00ba7cbc) 範囲 `[['00ba7cbc', '00ba7ceb']]`
  - `CONDITIONAL_JUMP` [`00ba7ce8`](#insn-00ba7ce8) → [`00ba80c4`](#insn-00ba80c4)
  - `FALL_THROUGH` [`00ba7ce8`](#insn-00ba7ce8) → [`00ba7cec`](#insn-00ba7cec)
- ブロック [`00ba7cec`](#insn-00ba7cec) 範囲 `[['00ba7cec', '00ba7cf3']]`
  - `FALL_THROUGH` [`00ba7cf0`](#insn-00ba7cf0) → [`00ba7cf4`](#insn-00ba7cf4)
- ブロック [`00ba7cf4`](#insn-00ba7cf4) 範囲 `[['00ba7cf4', '00ba7d03']]`
  - `CONDITIONAL_JUMP` [`00ba7d00`](#insn-00ba7d00) → [`00ba8084`](#insn-00ba8084)
  - `FALL_THROUGH` [`00ba7d00`](#insn-00ba7d00) → [`00ba7d04`](#insn-00ba7d04)
- ブロック [`00ba7d04`](#insn-00ba7d04) 範囲 `[['00ba7d04', '00ba7d0b']]`
  - `CONDITIONAL_JUMP` [`00ba7d08`](#insn-00ba7d08) → [`00ba8084`](#insn-00ba8084)
  - `FALL_THROUGH` [`00ba7d08`](#insn-00ba7d08) → [`00ba7d0c`](#insn-00ba7d0c)
- ブロック [`00ba7d0c`](#insn-00ba7d0c) 範囲 `[['00ba7d0c', '00ba7d0f']]`
  - `CONDITIONAL_JUMP` [`00ba7d0c`](#insn-00ba7d0c) → [`00ba80c4`](#insn-00ba80c4)
  - `FALL_THROUGH` [`00ba7d0c`](#insn-00ba7d0c) → [`00ba7d10`](#insn-00ba7d10)
- ブロック [`00ba7d10`](#insn-00ba7d10) 範囲 `[['00ba7d10', '00ba7d53']]`
  - `FALL_THROUGH` [`00ba7d50`](#insn-00ba7d50) → [`00ba7d54`](#insn-00ba7d54)
- ブロック [`00ba7d54`](#insn-00ba7d54) 範囲 `[['00ba7d54', '00ba7d6b']]`
  - `FALL_THROUGH` [`00ba7d68`](#insn-00ba7d68) → [`00ba7d6c`](#insn-00ba7d6c)
- ブロック [`00ba7d6c`](#insn-00ba7d6c) 範囲 `[['00ba7d6c', '00ba7da3']]`
  - `CONDITIONAL_JUMP` [`00ba7da0`](#insn-00ba7da0) → [`00ba7dbc`](#insn-00ba7dbc)
  - `FALL_THROUGH` [`00ba7da0`](#insn-00ba7da0) → [`00ba7da4`](#insn-00ba7da4)
- ブロック [`00ba7da4`](#insn-00ba7da4) 範囲 `[['00ba7da4', '00ba7db7']]`
  - `CONDITIONAL_JUMP` [`00ba7db4`](#insn-00ba7db4) → [`00ba7d54`](#insn-00ba7d54)
  - `FALL_THROUGH` [`00ba7db4`](#insn-00ba7db4) → [`00ba7db8`](#insn-00ba7db8)
- ブロック [`00ba7db8`](#insn-00ba7db8) 範囲 `[['00ba7db8', '00ba7dbb']]`
  - `UNCONDITIONAL_JUMP` [`00ba7db8`](#insn-00ba7db8) → [`00ba80c4`](#insn-00ba80c4)
- ブロック [`00ba7dbc`](#insn-00ba7dbc) 範囲 `[['00ba7dbc', '00ba7dd7']]`
  - `CONDITIONAL_JUMP` [`00ba7dd4`](#insn-00ba7dd4) → [`00ba7eac`](#insn-00ba7eac)
  - `FALL_THROUGH` [`00ba7dd4`](#insn-00ba7dd4) → [`00ba7dd8`](#insn-00ba7dd8)
- ブロック [`00ba7dd8`](#insn-00ba7dd8) 範囲 `[['00ba7dd8', '00ba7ddf']]`
  - `FALL_THROUGH` [`00ba7ddc`](#insn-00ba7ddc) → [`00ba7de0`](#insn-00ba7de0)
- ブロック [`00ba7de0`](#insn-00ba7de0) 範囲 `[['00ba7de0', '00ba7df3']]`
  - `CONDITIONAL_JUMP` [`00ba7df0`](#insn-00ba7df0) → [`00ba7f98`](#insn-00ba7f98)
  - `FALL_THROUGH` [`00ba7df0`](#insn-00ba7df0) → [`00ba7df4`](#insn-00ba7df4)
- ブロック [`00ba7df4`](#insn-00ba7df4) 範囲 `[['00ba7df4', '00ba7e27']]`
  - `FALL_THROUGH` [`00ba7e24`](#insn-00ba7e24) → [`00ba7e28`](#insn-00ba7e28)
- ブロック [`00ba7e28`](#insn-00ba7e28) 範囲 `[['00ba7e28', '00ba7e4f']]`
  - `FALL_THROUGH` [`00ba7e4c`](#insn-00ba7e4c) → [`00ba7e50`](#insn-00ba7e50)
- ブロック [`00ba7e50`](#insn-00ba7e50) 範囲 `[['00ba7e50', '00ba7e93']]`
  - `CONDITIONAL_JUMP` [`00ba7e90`](#insn-00ba7e90) → [`00ba7e28`](#insn-00ba7e28)
  - `FALL_THROUGH` [`00ba7e90`](#insn-00ba7e90) → [`00ba7e94`](#insn-00ba7e94)
- ブロック [`00ba7e94`](#insn-00ba7e94) 範囲 `[['00ba7e94', '00ba7e9b']]`
  - `FALL_THROUGH` [`00ba7e98`](#insn-00ba7e98) → [`00ba7e9c`](#insn-00ba7e9c)
- ブロック [`00ba7e9c`](#insn-00ba7e9c) 範囲 `[['00ba7e9c', '00ba7eab']]`
  - `UNCONDITIONAL_JUMP` [`00ba7ea8`](#insn-00ba7ea8) → [`00ba7fa4`](#insn-00ba7fa4)
- ブロック [`00ba7eac`](#insn-00ba7eac) 範囲 `[['00ba7eac', '00ba7eb7']]`
  - `CONDITIONAL_JUMP` [`00ba7eb4`](#insn-00ba7eb4) → [`00ba80b8`](#insn-00ba80b8)
  - `FALL_THROUGH` [`00ba7eb4`](#insn-00ba7eb4) → [`00ba7eb8`](#insn-00ba7eb8)
- ブロック [`00ba7eb8`](#insn-00ba7eb8) 範囲 `[['00ba7eb8', '00ba7edb']]`
  - `CONDITIONAL_JUMP` [`00ba7ed8`](#insn-00ba7ed8) → [`00ba7fb0`](#insn-00ba7fb0)
  - `FALL_THROUGH` [`00ba7ed8`](#insn-00ba7ed8) → [`00ba7edc`](#insn-00ba7edc)
- ブロック [`00ba7edc`](#insn-00ba7edc) 範囲 `[['00ba7edc', '00ba7f0f']]`
  - `FALL_THROUGH` [`00ba7f0c`](#insn-00ba7f0c) → [`00ba7f10`](#insn-00ba7f10)
- ブロック [`00ba7f10`](#insn-00ba7f10) 範囲 `[['00ba7f10', '00ba7f13']]`
  - `FALL_THROUGH` [`00ba7f10`](#insn-00ba7f10) → [`00ba7f14`](#insn-00ba7f14)
- ブロック [`00ba7f14`](#insn-00ba7f14) 範囲 `[['00ba7f14', '00ba7f73']]`
  - `FALL_THROUGH` [`00ba7f70`](#insn-00ba7f70) → [`00ba7f74`](#insn-00ba7f74)
- ブロック [`00ba7f74`](#insn-00ba7f74) 範囲 `[['00ba7f74', '00ba7f7f']]`
  - `CONDITIONAL_JUMP` [`00ba7f7c`](#insn-00ba7f7c) → [`00ba7f14`](#insn-00ba7f14)
  - `FALL_THROUGH` [`00ba7f7c`](#insn-00ba7f7c) → [`00ba7f80`](#insn-00ba7f80)
- ブロック [`00ba7f80`](#insn-00ba7f80) 範囲 `[['00ba7f80', '00ba7f97']]`
  - `UNCONDITIONAL_JUMP` [`00ba7f94`](#insn-00ba7f94) → [`00ba7fbc`](#insn-00ba7fbc)
- ブロック [`00ba7f98`](#insn-00ba7f98) 範囲 `[['00ba7f98', '00ba7fa3']]`
  - `FALL_THROUGH` [`00ba7fa0`](#insn-00ba7fa0) → [`00ba7fa4`](#insn-00ba7fa4)
- ブロック [`00ba7fa4`](#insn-00ba7fa4) 範囲 `[['00ba7fa4', '00ba7fab']]`
  - `FALL_THROUGH` [`00ba7fa8`](#insn-00ba7fa8) → [`00ba7fac`](#insn-00ba7fac)
- ブロック [`00ba7fac`](#insn-00ba7fac) 範囲 `[['00ba7fac', '00ba7faf']]`
  - `UNCONDITIONAL_JUMP` [`00ba7fac`](#insn-00ba7fac) → [`00ba7fc4`](#insn-00ba7fc4)
- ブロック [`00ba7fb0`](#insn-00ba7fb0) 範囲 `[['00ba7fb0', '00ba7fbb']]`
  - `FALL_THROUGH` [`00ba7fb8`](#insn-00ba7fb8) → [`00ba7fbc`](#insn-00ba7fbc)
- ブロック [`00ba7fbc`](#insn-00ba7fbc) 範囲 `[['00ba7fbc', '00ba7fc3']]`
  - `FALL_THROUGH` [`00ba7fc0`](#insn-00ba7fc0) → [`00ba7fc4`](#insn-00ba7fc4)
- ブロック [`00ba7fc4`](#insn-00ba7fc4) 範囲 `[['00ba7fc4', '00ba7fcb']]`
  - `FALL_THROUGH` [`00ba7fc8`](#insn-00ba7fc8) → [`00ba7fcc`](#insn-00ba7fcc)
- ブロック [`00ba7fcc`](#insn-00ba7fcc) 範囲 `[['00ba7fcc', '00ba7fdb']]`
  - `CONDITIONAL_JUMP` [`00ba7fd8`](#insn-00ba7fd8) → [`00ba8010`](#insn-00ba8010)
  - `FALL_THROUGH` [`00ba7fd8`](#insn-00ba7fd8) → [`00ba7fdc`](#insn-00ba7fdc)
- ブロック [`00ba7fdc`](#insn-00ba7fdc) 範囲 `[['00ba7fdc', '00ba7fe7']]`
  - `CONDITIONAL_JUMP` [`00ba7fe4`](#insn-00ba7fe4) → [`00ba8010`](#insn-00ba8010)
  - `FALL_THROUGH` [`00ba7fe4`](#insn-00ba7fe4) → [`00ba7fe8`](#insn-00ba7fe8)
- ブロック [`00ba7fe8`](#insn-00ba7fe8) 範囲 `[['00ba7fe8', '00ba7ff7']]`
  - `FALL_THROUGH` [`00ba7ff4`](#insn-00ba7ff4) → [`00ba7ff8`](#insn-00ba7ff8)
- ブロック [`00ba7ff8`](#insn-00ba7ff8) 範囲 `[['00ba7ff8', '00ba800f']]`
  - `FALL_THROUGH` [`00ba800c`](#insn-00ba800c) → [`00ba8010`](#insn-00ba8010)
- ブロック [`00ba8010`](#insn-00ba8010) 範囲 `[['00ba8010', '00ba801b']]`
  - `FALL_THROUGH` [`00ba8018`](#insn-00ba8018) → [`00ba801c`](#insn-00ba801c)
- ブロック [`00ba801c`](#insn-00ba801c) 範囲 `[['00ba801c', '00ba8027']]`
  - `CONDITIONAL_JUMP` [`00ba8024`](#insn-00ba8024) → [`00ba8044`](#insn-00ba8044)
  - `FALL_THROUGH` [`00ba8024`](#insn-00ba8024) → [`00ba8028`](#insn-00ba8028)
- ブロック [`00ba8028`](#insn-00ba8028) 範囲 `[['00ba8028', '00ba802f']]`
  - `FALL_THROUGH` [`00ba802c`](#insn-00ba802c) → [`00ba8030`](#insn-00ba8030)
- ブロック [`00ba8030`](#insn-00ba8030) 範囲 `[['00ba8030', '00ba8043']]`
  - `UNCONDITIONAL_JUMP` [`00ba8040`](#insn-00ba8040) → [`00ba8074`](#insn-00ba8074)
- ブロック [`00ba8044`](#insn-00ba8044) 範囲 `[['00ba8044', '00ba804f']]`
  - `FALL_THROUGH` [`00ba804c`](#insn-00ba804c) → [`00ba8050`](#insn-00ba8050)
- ブロック [`00ba8050`](#insn-00ba8050) 範囲 `[['00ba8050', '00ba805b']]`
  - `FALL_THROUGH` [`00ba8058`](#insn-00ba8058) → [`00ba805c`](#insn-00ba805c)
- ブロック [`00ba805c`](#insn-00ba805c) 範囲 `[['00ba805c', '00ba8067']]`
  - `FALL_THROUGH` [`00ba8064`](#insn-00ba8064) → [`00ba8068`](#insn-00ba8068)
- ブロック [`00ba8068`](#insn-00ba8068) 範囲 `[['00ba8068', '00ba8073']]`
  - `FALL_THROUGH` [`00ba8070`](#insn-00ba8070) → [`00ba8074`](#insn-00ba8074)
- ブロック [`00ba8074`](#insn-00ba8074) 範囲 `[['00ba8074', '00ba807f']]`
  - `CONDITIONAL_JUMP` [`00ba807c`](#insn-00ba807c) → [`00ba7cf4`](#insn-00ba7cf4)
  - `FALL_THROUGH` [`00ba807c`](#insn-00ba807c) → [`00ba8080`](#insn-00ba8080)
- ブロック [`00ba8080`](#insn-00ba8080) 範囲 `[['00ba8080', '00ba8083']]`
  - `UNCONDITIONAL_JUMP` [`00ba8080`](#insn-00ba8080) → [`00ba80c4`](#insn-00ba80c4)
- ブロック [`00ba8084`](#insn-00ba8084) 範囲 `[['00ba8084', '00ba8087']]`
  - `FALL_THROUGH` [`00ba8084`](#insn-00ba8084) → [`00ba8088`](#insn-00ba8088)
- ブロック [`00ba8088`](#insn-00ba8088) 範囲 `[['00ba8088', '00ba80b7']]`
- ブロック [`00ba80b8`](#insn-00ba80b8) 範囲 `[['00ba80b8', '00ba80c3']]`
  - `FALL_THROUGH` [`00ba80c0`](#insn-00ba80c0) → [`00ba80c4`](#insn-00ba80c4)
- ブロック [`00ba80c4`](#insn-00ba80c4) 範囲 `[['00ba80c4', '00ba80c7']]`
  - `FALL_THROUGH` [`00ba80c4`](#insn-00ba80c4) → [`00ba80c8`](#insn-00ba80c8)
- ブロック [`00ba80c8`](#insn-00ba80c8) 範囲 `[['00ba80c8', '00ba80e3']]`

## 命令位置別の参照

- [`00ba7cc0`](#insn-00ba7cc0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7cc4`](#insn-00ba7cc4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7cc8`](#insn-00ba7cc8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7ccc`](#insn-00ba7ccc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7cd0`](#insn-00ba7cd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7cd4`](#insn-00ba7cd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7cdc`](#insn-00ba7cdc) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7ce0`](#insn-00ba7ce0) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7ce4`](#insn-00ba7ce4) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7ce8`](#insn-00ba7ce8) → [`00ba80c4`](#insn-00ba80c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7cf4`](#insn-00ba7cf4) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7cf8`](#insn-00ba7cf8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7d00`](#insn-00ba7d00) → [`00ba8084`](#insn-00ba8084) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7d08`](#insn-00ba7d08) → [`00ba8084`](#insn-00ba8084) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7d0c`](#insn-00ba7d0c) → [`00ba80c4`](#insn-00ba80c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7d10`](#insn-00ba7d10) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7d14`](#insn-00ba7d14) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7d88`](#insn-00ba7d88) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00ba7da0`](#insn-00ba7da0) → [`00ba7dbc`](#insn-00ba7dbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7db4`](#insn-00ba7db4) → [`00ba7d54`](#insn-00ba7d54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7db8`](#insn-00ba7db8) → [`00ba80c4`](#insn-00ba80c4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7dbc`](#insn-00ba7dbc) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7dd0`](#insn-00ba7dd0) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7dd4`](#insn-00ba7dd4) → [`00ba7eac`](#insn-00ba7eac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7dd8`](#insn-00ba7dd8) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7df0`](#insn-00ba7df0) → [`00ba7f98`](#insn-00ba7f98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7df8`](#insn-00ba7df8) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7e24`](#insn-00ba7e24) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7e54`](#insn-00ba7e54) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7e60`](#insn-00ba7e60) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00ba7e90`](#insn-00ba7e90) → [`00ba7e28`](#insn-00ba7e28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7e94`](#insn-00ba7e94) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7e98`](#insn-00ba7e98) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7e9c`](#insn-00ba7e9c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7ea0`](#insn-00ba7ea0) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7ea8`](#insn-00ba7ea8) → [`00ba7fa4`](#insn-00ba7fa4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7eb4`](#insn-00ba7eb4) → [`00ba80b8`](#insn-00ba80b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7ec4`](#insn-00ba7ec4) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7ec8`](#insn-00ba7ec8) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7ed8`](#insn-00ba7ed8) → [`00ba7fb0`](#insn-00ba7fb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7ee0`](#insn-00ba7ee0) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7f10`](#insn-00ba7f10) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7f40`](#insn-00ba7f40) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7f4c`](#insn-00ba7f4c) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00ba7f7c`](#insn-00ba7f7c) → [`00ba7f14`](#insn-00ba7f14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7f80`](#insn-00ba7f80) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7f84`](#insn-00ba7f84) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7f88`](#insn-00ba7f88) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7f8c`](#insn-00ba7f8c) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7f94`](#insn-00ba7f94) → [`00ba7fbc`](#insn-00ba7fbc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7f98`](#insn-00ba7f98) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7f9c`](#insn-00ba7f9c) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7fac`](#insn-00ba7fac) → [`00ba7fc4`](#insn-00ba7fc4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7fb0`](#insn-00ba7fb0) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7fb4`](#insn-00ba7fb4) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7fd8`](#insn-00ba7fd8) → [`00ba8010`](#insn-00ba8010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7fe4`](#insn-00ba7fe4) → [`00ba8010`](#insn-00ba8010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7ff8`](#insn-00ba7ff8) → [`00ba86b0`](../00ba8/00ba86b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba86b0` · 推定シンボル `None` · 推定型 `None`
- [`00ba7ffc`](#insn-00ba7ffc) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba8024`](#insn-00ba8024) → [`00ba8044`](#insn-00ba8044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba8028`](#insn-00ba8028) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba802c`](#insn-00ba802c) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba803c`](#insn-00ba803c) → [`00c5cc50`](../00c5c/00c5cc50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cc50` · 推定シンボル `None` · 推定型 `None`
- [`00ba8040`](#insn-00ba8040) → [`00ba8074`](#insn-00ba8074) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba8044`](#insn-00ba8044) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba805c`](#insn-00ba805c) → [`00c5cc50`](../00c5c/00c5cc50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cc50` · 推定シンボル `None` · 推定型 `None`
- [`00ba8060`](#insn-00ba8060) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba8064`](#insn-00ba8064) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba8078`](#insn-00ba8078) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba807c`](#insn-00ba807c) → [`00ba7cf4`](#insn-00ba7cf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba8080`](#insn-00ba8080) → [`00ba80c4`](#insn-00ba80c4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba8088`](#insn-00ba8088) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba808c`](#insn-00ba808c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba8094`](#insn-00ba8094) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba8098`](#insn-00ba8098) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba809c`](#insn-00ba809c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba80a0`](#insn-00ba80a0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba80a4`](#insn-00ba80a4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba80a8`](#insn-00ba80a8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba80ac`](#insn-00ba80ac) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba80b4`](#insn-00ba80b4) → [`00c5ce10`](../00c5c/00c5ce10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ce10` · 推定シンボル `None` · 推定型 `None`
- [`00ba80b8`](#insn-00ba80b8) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba80c4`](#insn-00ba80c4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba80c8`](#insn-00ba80c8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba80cc`](#insn-00ba80cc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba80d0`](#insn-00ba80d0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba80d4`](#insn-00ba80d4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba80d8`](#insn-00ba80d8) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ba7cc0`](#insn-00ba7cc0)

~~~json
{
  "source": "00ba7cc0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7cc4`](#insn-00ba7cc4)

~~~json
{
  "source": "00ba7cc4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7cc8`](#insn-00ba7cc8)

~~~json
{
  "source": "00ba7cc8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7ccc`](#insn-00ba7ccc)

~~~json
{
  "source": "00ba7ccc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7cd0`](#insn-00ba7cd0)

~~~json
{
  "source": "00ba7cd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7cd4`](#insn-00ba7cd4)

~~~json
{
  "source": "00ba7cd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7cdc`](#insn-00ba7cdc)

~~~json
{
  "source": "00ba7cdc",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7ce0`](#insn-00ba7ce0)

~~~json
{
  "source": "00ba7ce0",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7ce4`](#insn-00ba7ce4)

~~~json
{
  "source": "00ba7ce4",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7ce8`](#insn-00ba7ce8)

~~~json
{
  "source": "00ba7ce8",
  "target": "00ba80c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7cf4`](#insn-00ba7cf4)

~~~json
{
  "source": "00ba7cf4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7cf8`](#insn-00ba7cf8)

~~~json
{
  "source": "00ba7cf8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7d00`](#insn-00ba7d00)

~~~json
{
  "source": "00ba7d00",
  "target": "00ba8084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7d08`](#insn-00ba7d08)

~~~json
{
  "source": "00ba7d08",
  "target": "00ba8084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7d0c`](#insn-00ba7d0c)

~~~json
{
  "source": "00ba7d0c",
  "target": "00ba80c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7d10`](#insn-00ba7d10)

~~~json
{
  "source": "00ba7d10",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7d14`](#insn-00ba7d14)

~~~json
{
  "source": "00ba7d14",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7d88`](#insn-00ba7d88)

~~~json
{
  "source": "00ba7d88",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba7da0`](#insn-00ba7da0)

~~~json
{
  "source": "00ba7da0",
  "target": "00ba7dbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7db4`](#insn-00ba7db4)

~~~json
{
  "source": "00ba7db4",
  "target": "00ba7d54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7db8`](#insn-00ba7db8)

~~~json
{
  "source": "00ba7db8",
  "target": "00ba80c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7dbc`](#insn-00ba7dbc)

~~~json
{
  "source": "00ba7dbc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7dd0`](#insn-00ba7dd0)

~~~json
{
  "source": "00ba7dd0",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7dd4`](#insn-00ba7dd4)

~~~json
{
  "source": "00ba7dd4",
  "target": "00ba7eac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7dd8`](#insn-00ba7dd8)

~~~json
{
  "source": "00ba7dd8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7df0`](#insn-00ba7df0)

~~~json
{
  "source": "00ba7df0",
  "target": "00ba7f98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7df8`](#insn-00ba7df8)

~~~json
{
  "source": "00ba7df8",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7e24`](#insn-00ba7e24)

~~~json
{
  "source": "00ba7e24",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7e54`](#insn-00ba7e54)

~~~json
{
  "source": "00ba7e54",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7e60`](#insn-00ba7e60)

~~~json
{
  "source": "00ba7e60",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba7e90`](#insn-00ba7e90)

~~~json
{
  "source": "00ba7e90",
  "target": "00ba7e28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7e94`](#insn-00ba7e94)

~~~json
{
  "source": "00ba7e94",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7e98`](#insn-00ba7e98)

~~~json
{
  "source": "00ba7e98",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7e9c`](#insn-00ba7e9c)

~~~json
{
  "source": "00ba7e9c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7ea0`](#insn-00ba7ea0)

~~~json
{
  "source": "00ba7ea0",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7ea8`](#insn-00ba7ea8)

~~~json
{
  "source": "00ba7ea8",
  "target": "00ba7fa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7eb4`](#insn-00ba7eb4)

~~~json
{
  "source": "00ba7eb4",
  "target": "00ba80b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7ec4`](#insn-00ba7ec4)

~~~json
{
  "source": "00ba7ec4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7ec8`](#insn-00ba7ec8)

~~~json
{
  "source": "00ba7ec8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7ed8`](#insn-00ba7ed8)

~~~json
{
  "source": "00ba7ed8",
  "target": "00ba7fb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7ee0`](#insn-00ba7ee0)

~~~json
{
  "source": "00ba7ee0",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7f10`](#insn-00ba7f10)

~~~json
{
  "source": "00ba7f10",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7f40`](#insn-00ba7f40)

~~~json
{
  "source": "00ba7f40",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7f4c`](#insn-00ba7f4c)

~~~json
{
  "source": "00ba7f4c",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba7f7c`](#insn-00ba7f7c)

~~~json
{
  "source": "00ba7f7c",
  "target": "00ba7f14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7f80`](#insn-00ba7f80)

~~~json
{
  "source": "00ba7f80",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7f84`](#insn-00ba7f84)

~~~json
{
  "source": "00ba7f84",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7f88`](#insn-00ba7f88)

~~~json
{
  "source": "00ba7f88",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7f8c`](#insn-00ba7f8c)

~~~json
{
  "source": "00ba7f8c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7f94`](#insn-00ba7f94)

~~~json
{
  "source": "00ba7f94",
  "target": "00ba7fbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7f98`](#insn-00ba7f98)

~~~json
{
  "source": "00ba7f98",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7f9c`](#insn-00ba7f9c)

~~~json
{
  "source": "00ba7f9c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7fac`](#insn-00ba7fac)

~~~json
{
  "source": "00ba7fac",
  "target": "00ba7fc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7fb0`](#insn-00ba7fb0)

~~~json
{
  "source": "00ba7fb0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7fb4`](#insn-00ba7fb4)

~~~json
{
  "source": "00ba7fb4",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7fd8`](#insn-00ba7fd8)

~~~json
{
  "source": "00ba7fd8",
  "target": "00ba8010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7fe4`](#insn-00ba7fe4)

~~~json
{
  "source": "00ba7fe4",
  "target": "00ba8010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7ff8`](#insn-00ba7ff8)

~~~json
{
  "source": "00ba7ff8",
  "target": "00ba86b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba7ffc`](#insn-00ba7ffc)

~~~json
{
  "source": "00ba7ffc",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba8024`](#insn-00ba8024)

~~~json
{
  "source": "00ba8024",
  "target": "00ba8044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba8028`](#insn-00ba8028)

~~~json
{
  "source": "00ba8028",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba802c`](#insn-00ba802c)

~~~json
{
  "source": "00ba802c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba803c`](#insn-00ba803c)

~~~json
{
  "source": "00ba803c",
  "target": "00c5cc50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba8040`](#insn-00ba8040)

~~~json
{
  "source": "00ba8040",
  "target": "00ba8074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba8044`](#insn-00ba8044)

~~~json
{
  "source": "00ba8044",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba805c`](#insn-00ba805c)

~~~json
{
  "source": "00ba805c",
  "target": "00c5cc50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba8060`](#insn-00ba8060)

~~~json
{
  "source": "00ba8060",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba8064`](#insn-00ba8064)

~~~json
{
  "source": "00ba8064",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba8078`](#insn-00ba8078)

~~~json
{
  "source": "00ba8078",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba807c`](#insn-00ba807c)

~~~json
{
  "source": "00ba807c",
  "target": "00ba7cf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba8080`](#insn-00ba8080)

~~~json
{
  "source": "00ba8080",
  "target": "00ba80c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba8088`](#insn-00ba8088)

~~~json
{
  "source": "00ba8088",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba808c`](#insn-00ba808c)

~~~json
{
  "source": "00ba808c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba8094`](#insn-00ba8094)

~~~json
{
  "source": "00ba8094",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba8098`](#insn-00ba8098)

~~~json
{
  "source": "00ba8098",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba809c`](#insn-00ba809c)

~~~json
{
  "source": "00ba809c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba80a0`](#insn-00ba80a0)

~~~json
{
  "source": "00ba80a0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba80a4`](#insn-00ba80a4)

~~~json
{
  "source": "00ba80a4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba80a8`](#insn-00ba80a8)

~~~json
{
  "source": "00ba80a8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba80ac`](#insn-00ba80ac)

~~~json
{
  "source": "00ba80ac",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba80b4`](#insn-00ba80b4)

~~~json
{
  "source": "00ba80b4",
  "target": "00c5ce10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba80b8`](#insn-00ba80b8)

~~~json
{
  "source": "00ba80b8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba80c4`](#insn-00ba80c4)

~~~json
{
  "source": "00ba80c4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba80c8`](#insn-00ba80c8)

~~~json
{
  "source": "00ba80c8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba80cc`](#insn-00ba80cc)

~~~json
{
  "source": "00ba80cc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba80d0`](#insn-00ba80d0)

~~~json
{
  "source": "00ba80d0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba80d4`](#insn-00ba80d4)

~~~json
{
  "source": "00ba80d4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba80d8`](#insn-00ba80d8)

~~~json
{
  "source": "00ba80d8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
