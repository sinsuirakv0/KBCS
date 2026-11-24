# 00ba6dcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00ba69a4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba6/00ba69a4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0009.md#compare-1111338817fc7b0baaffc96034a3bf70)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00ba6e68`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba6/00ba6e68.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0078.md#compare-1c7dbdee20d776f1c1354a09c5207c0e)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ba6dcc",
  "name": "_ZNSt6__ndk124__buffered_inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6OffsetIS6_EEEEvT0_SC_SC_T_NS_15iterator_traitsISC_E15difference_typeESG_PNSF_10value_typeE",
  "size": 732,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a24903bdc1405163a1d78b3c10a4fd1dee92dfa296f13a7c8bc312bd1ee2d89b",
  "source_text_sha256": "a24903bdc1405163a1d78b3c10a4fd1dee92dfa296f13a7c8bc312bd1ee2d89b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ba6dcc",
        "00ba70a7"
      ]
    ],
    "bytes_sha256": "ce80c8c57e090689d777925d0ab419e36fe1a4aa512d2350761c911aaa6d717b",
    "instruction_count": 183,
    "instruction_bytes": 732,
    "body_bytes": 732,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5cd80](../00c5c/00c5cd80.md)

## 呼び出し先

- [00c57ee0](../00c57/00c57ee0.md)
- [00c58050](../00c58/00c58050.md)
- [00c5ccc0](../00c5c/00c5ccc0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 7968 bytes

~~~c

void _ZNSt6__ndk124__buffered_inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6OffsetIS6_EEEEvT0_SC_SC_T_NS_15iterator_traitsISC_E15difference_typeESG_PNSF_10value_typeE
               (uint *param_1,uint *param_2,uint *param_3,long *param_4,long param_5,long param_6,
               uint *param_7)

{
  ulong uVar1;
  uint uVar2;
  uint uVar3;
  uint uVar4;
  uint uVar5;
  uint uVar6;
  long lVar7;
  bool bVar8;
  int iVar9;
  uint *puVar10;
  uint *puVar11;
  uint *puVar12;
  int *piVar13;
  uint *puVar14;
  long lVar15;
  int *piVar16;
  ulong uVar17;
  ulong uVar18;
  undefined8 uVar19;
  undefined8 uVar20;
  undefined8 uVar21;
  long local_70;
  long local_68;
  
                    /* try { // try from 00ba6dd4 to 00ca6def has its CatchHandler @ 00ba6f48 */
  lVar7 = tpidr_el0;
  local_68 = *(long *)(lVar7 + 0x28);
                    /* try { // try from 00ba6e08 to 00ca6e13 has its CatchHandler @ 00ba6ec4 */
                    /* try { // try from 00ba6e14 to 00ca6e1f has its CatchHandler @ 00ba6ec0 */
  if (param_5 <= param_6) {
    puVar11 = param_7;
    if (param_1 != param_2) {
      uVar17 = (long)param_2 + (-4 - (long)param_1);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00ba6e5c with catch @ 00ba6fa0
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00ba7098 with catch @ 00ba6fa4
                        */
      uVar1 = (uVar17 >> 2) + 1;
      puVar10 = param_7;
      puVar14 = param_1;
      if ((7 < uVar1) &&
         ((lVar15 = (uVar17 & 0xfffffffffffffffc) + 4, (uint *)((long)param_1 + lVar15) <= param_7
          || ((uint *)((long)param_7 + lVar15) <= param_1)))) {
        uVar18 = uVar1 & 0x7ffffffffffffff8;
                    /* try { // try from 00ba6fe4 to 00ca6fef has its CatchHandler @ 00ba70d4 */
        puVar10 = param_7 + 4;
        puVar11 = param_7 + uVar18;
        puVar14 = param_1 + 4;
        uVar17 = uVar18;
        do {
          puVar12 = puVar14 + -2;
          uVar19 = *(undefined8 *)(puVar14 + -4);
          uVar21 = *(undefined8 *)(puVar14 + 2);
          uVar20 = *(undefined8 *)puVar14;
          uVar17 = uVar17 - 8;
          puVar14 = puVar14 + 8;
                    /* try { // try from 00ba7008 to 00ca7013 has its CatchHandler @ 00ba70d0 */
          *(undefined8 *)(puVar10 + -2) = *(undefined8 *)puVar12;
          *(undefined8 *)(puVar10 + -4) = uVar19;
          *(undefined8 *)(puVar10 + 2) = uVar21;
          *(undefined8 *)puVar10 = uVar20;
          puVar10 = puVar10 + 8;
        } while (uVar17 != 0);
        puVar10 = puVar11;
        puVar14 = param_1 + uVar18;
        if (uVar1 == uVar18) goto LAB_00ba702c;
      }
      do {
        puVar12 = puVar14 + 1;
        puVar11 = puVar10 + 1;
        *puVar10 = *puVar14;
        puVar10 = puVar11;
        puVar14 = puVar12;
      } while (param_2 != puVar12);
    }
LAB_00ba702c:
                    /* try { // try from 00ba7030 to 00ca703b has its CatchHandler @ 00ba70c0 */
    local_70 = *param_4;
    _ZNSt6__ndk120__half_inplace_mergeIN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6OffsetIS6_EESA_SA_EEvT0_SB_T1_SC_T2_T_
              (param_7,puVar11,param_2,param_3,param_1,&local_70);
    goto LAB_00ba704c;
  }
  if (param_2 == param_3) goto LAB_00ba704c;
                    /* try { // try from 00ba6e20 to 00ca6e2b has its CatchHandler @ 00ba6ebc */
  uVar17 = (long)param_3 + (-4 - (long)param_2);
  uVar1 = (uVar17 >> 2) + 1;
                    /* try { // try from 00ba6e3c to 00ca6e5b has its CatchHandler @ 00ba6f1c */
  puVar11 = param_2;
  puVar10 = param_7;
                    /* try { // try from 00ba6e5c to 00ca6e93 has its CatchHandler @ 00ba6fa0 */
  if ((uVar1 < 8) ||
     ((lVar15 = (uVar17 & 0xfffffffffffffffc) + 4, param_7 < (uint *)((long)param_2 + lVar15) &&
      (param_2 < (uint *)((long)param_7 + lVar15))))) {
LAB_00ba6ea4:
    do {
      puVar12 = puVar11 + 1;
      puVar14 = puVar10 + 1;
      *puVar10 = *puVar11;
      puVar11 = puVar12;
      puVar10 = puVar14;
    } while (param_3 != puVar12);
  }
  else {
    uVar18 = uVar1 & 0x7ffffffffffffff8;
    puVar11 = param_7 + 4;
    puVar10 = param_2 + 4;
    uVar17 = uVar18;
    do {
      puVar14 = puVar10 + -2;
      uVar19 = *(undefined8 *)(puVar10 + -4);
      uVar21 = *(undefined8 *)(puVar10 + 2);
      uVar20 = *(undefined8 *)puVar10;
      uVar17 = uVar17 - 8;
      puVar10 = puVar10 + 8;
      *(undefined8 *)(puVar11 + -2) = *(undefined8 *)puVar14;
      *(undefined8 *)(puVar11 + -4) = uVar19;
      *(undefined8 *)(puVar11 + 2) = uVar21;
      *(undefined8 *)puVar11 = uVar20;
                    /* try { // try from 00ba6e94 to 00ca6fa3 has its CatchHandler @ 00ba6cb8 */
      puVar11 = puVar11 + 8;
    } while (uVar17 != 0);
    puVar11 = param_2 + uVar18;
    puVar10 = param_7 + uVar18;
    puVar14 = param_7 + uVar18;
    if (uVar1 != uVar18) goto LAB_00ba6ea4;
  }
  while (puVar14 != param_7) {
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00ba6e08 with catch @ 00ba6ec4
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00ba6e20 with catch @ 00ba6ebc
                        */
    param_3 = param_3 + -1;
    if (param_2 == param_1) {
      lVar15 = 0;
      do {
        *(undefined4 *)((long)param_3 + lVar15) = *(undefined4 *)((long)puVar14 + lVar15 + -4);
        lVar15 = lVar15 + -4;
                    /* try { // try from 00ba7098 to 00ca711b has its CatchHandler @ 00ba6fa4 */
      } while ((long)param_7 - (long)puVar14 != lVar15);
      break;
    }
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00ba6d74 with catch @ 00ba6ef0
                        */
    uVar3 = param_2[-1];
    uVar4 = puVar14[-1];
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00ba6d50 with catch @ 00ba6f00
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00ba6d24 with catch @ 00ba6f08
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00ba6d00 with catch @ 00ba6f0c
                        */
    lVar15 = *(long *)(*param_4 + 0x38) + *(long *)(*param_4 + 0x28);
    piVar16 = (int *)(lVar15 - (ulong)uVar4);
    piVar13 = (int *)(lVar15 - (ulong)uVar3);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00ba6e3c with catch @ 00ba6f1c
                        */
    puVar11 = (uint *)((long)piVar16 + (ulong)*(ushort *)((long)piVar16 + (4 - (long)*piVar16)));
    puVar10 = (uint *)((long)piVar13 + (ulong)*(ushort *)((long)piVar13 + (4 - (long)*piVar13)));
    puVar11 = (uint *)((long)puVar11 + (ulong)*puVar11);
    puVar10 = (uint *)((long)puVar10 + (ulong)*puVar10);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00ba6dd4 with catch @ 00ba6f48
                        */
    uVar5 = *puVar11;
    uVar6 = *puVar10;
    uVar2 = uVar6;
    if (uVar5 <= uVar6) {
      uVar2 = uVar5;
    }
    iVar9 = memcmp(puVar11 + 1,puVar10 + 1,(ulong)uVar2);
    bVar8 = uVar5 < uVar6;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00ba6d38 with catch @ 00ba6f68
                        */
    if (iVar9 != 0) {
      bVar8 = iVar9 < 0;
    }
    if (bVar8) {
      *param_3 = uVar3;
      param_2 = param_2 + -1;
    }
    else {
      *param_3 = uVar4;
      puVar14 = puVar14 + -1;
    }
  }
LAB_00ba704c:
                    /* try { // try from 00ba7050 to 00ca705b has its CatchHandler @ 00ba70bc */
                    /* try { // try from 00ba705c to 00ca707b has its CatchHandler @ 00ba70e8 */
  if (*(long *)(lVar7 + 0x28) != local_68) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
                    /* try { // try from 00ba707c to 00ca7097 has its CatchHandler @ 00ba70e4 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ba6dcc"></a> `00ba6dcc` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00ba6dd0"></a> `00ba6dd0` | `fc 6f 03 a9` | stp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba6dd4"></a> `00ba6dd4` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ba6dd8"></a> `00ba6dd8` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ba6ddc"></a> `00ba6ddc` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ba6de0"></a> `00ba6de0` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ba6de4"></a> `00ba6de4` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00ba6de8"></a> `00ba6de8` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00ba6dec"></a> `00ba6dec` | `e3 0b 00 f9` | str x3,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba6df0"></a> `00ba6df0` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00ba6df4"></a> `00ba6df4` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ba6df8"></a> `00ba6df8` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00ba6dfc"></a> `00ba6dfc` | `fa 03 06 aa` | mov x26,x6 | `FALL_THROUGH`
<a id="insn-00ba6e00"></a> `00ba6e00` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00ba6e04"></a> `00ba6e04` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00ba6e08"></a> `00ba6e08` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ba6e0c"></a> `00ba6e0c` | `9f 00 05 eb` | cmp x4,x5 | `FALL_THROUGH`
<a id="insn-00ba6e10"></a> `00ba6e10` | `e8 17 00 f9` | str x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00ba6e14"></a> `00ba6e14` | `cd 0b 00 54` | b.le 0x00ba6f8c | `CONDITIONAL_JUMP`
<a id="insn-00ba6e18"></a> `00ba6e18` | `bf 02 03 eb` | cmp x21,x3 | `FALL_THROUGH`
<a id="insn-00ba6e1c"></a> `00ba6e1c` | `80 11 00 54` | b.eq 0x00ba704c | `CONDITIONAL_JUMP`
<a id="insn-00ba6e20"></a> `00ba6e20` | `68 00 15 cb` | sub x8,x3,x21 | `FALL_THROUGH`
<a id="insn-00ba6e24"></a> `00ba6e24` | `0a 11 00 d1` | sub x10,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00ba6e28"></a> `00ba6e28` | `48 fd 42 d3` | lsr x8,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00ba6e2c"></a> `00ba6e2c` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ba6e30"></a> `00ba6e30` | `3f 1d 00 f1` | cmp x9,#0x7 | `FALL_THROUGH`
<a id="insn-00ba6e34"></a> `00ba6e34` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00ba6e38"></a> `00ba6e38` | `f8 03 1a aa` | mov x24,x26 | `FALL_THROUGH`
<a id="insn-00ba6e3c"></a> `00ba6e3c` | `49 03 00 54` | b.ls 0x00ba6ea4 | `CONDITIONAL_JUMP`
<a id="insn-00ba6e40"></a> `00ba6e40` | `48 f5 7e 92` | and x8,x10,#-0x4 | `FALL_THROUGH`
<a id="insn-00ba6e44"></a> `00ba6e44` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00ba6e48"></a> `00ba6e48` | `aa 02 08 8b` | add x10,x21,x8 | `FALL_THROUGH`
<a id="insn-00ba6e4c"></a> `00ba6e4c` | `5f 01 1a eb` | cmp x10,x26 | `FALL_THROUGH`
<a id="insn-00ba6e50"></a> `00ba6e50` | `c9 00 00 54` | b.ls 0x00ba6e68 | `CONDITIONAL_JUMP`
<a id="insn-00ba6e54"></a> `00ba6e54` | `48 03 08 8b` | add x8,x26,x8 | `FALL_THROUGH`
<a id="insn-00ba6e58"></a> `00ba6e58` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00ba6e5c"></a> `00ba6e5c` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00ba6e60"></a> `00ba6e60` | `f8 03 1a aa` | mov x24,x26 | `FALL_THROUGH`
<a id="insn-00ba6e64"></a> `00ba6e64` | `08 02 00 54` | b.hi 0x00ba6ea4 | `CONDITIONAL_JUMP`
<a id="insn-00ba6e68"></a> `00ba6e68` | `2a ed 7d 92` | and x10,x9,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-00ba6e6c"></a> `00ba6e6c` | `4c f5 7e d3` | lsl x12,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00ba6e70"></a> `00ba6e70` | `4b 43 00 91` | add x11,x26,#0x10 | `FALL_THROUGH`
<a id="insn-00ba6e74"></a> `00ba6e74` | `a8 02 0c 8b` | add x8,x21,x12 | `FALL_THROUGH`
<a id="insn-00ba6e78"></a> `00ba6e78` | `58 03 0c 8b` | add x24,x26,x12 | `FALL_THROUGH`
<a id="insn-00ba6e7c"></a> `00ba6e7c` | `ac 42 00 91` | add x12,x21,#0x10 | `FALL_THROUGH`
<a id="insn-00ba6e80"></a> `00ba6e80` | `ed 03 0a aa` | mov x13,x10 | `FALL_THROUGH`
<a id="insn-00ba6e84"></a> `00ba6e84` | `80 85 7f ad` | ldp q0,q1,[x12, #-0x10] | `FALL_THROUGH`
<a id="insn-00ba6e88"></a> `00ba6e88` | `ad 21 00 f1` | subs x13,x13,#0x8 | `FALL_THROUGH`
<a id="insn-00ba6e8c"></a> `00ba6e8c` | `8c 81 00 91` | add x12,x12,#0x20 | `FALL_THROUGH`
<a id="insn-00ba6e90"></a> `00ba6e90` | `60 85 3f ad` | stp q0,q1,[x11, #-0x10] | `FALL_THROUGH`
<a id="insn-00ba6e94"></a> `00ba6e94` | `6b 81 00 91` | add x11,x11,#0x20 | `FALL_THROUGH`
<a id="insn-00ba6e98"></a> `00ba6e98` | `61 ff ff 54` | b.ne 0x00ba6e84 | `CONDITIONAL_JUMP`
<a id="insn-00ba6e9c"></a> `00ba6e9c` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00ba6ea0"></a> `00ba6ea0` | `a0 00 00 54` | b.eq 0x00ba6eb4 | `CONDITIONAL_JUMP`
<a id="insn-00ba6ea4"></a> `00ba6ea4` | `09 45 40 b8` | ldr w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00ba6ea8"></a> `00ba6ea8` | `7f 00 08 eb` | cmp x3,x8 | `FALL_THROUGH`
<a id="insn-00ba6eac"></a> `00ba6eac` | `09 47 00 b8` | str w9,[x24], #0x4 | `FALL_THROUGH`
<a id="insn-00ba6eb0"></a> `00ba6eb0` | `a1 ff ff 54` | b.ne 0x00ba6ea4 | `CONDITIONAL_JUMP`
<a id="insn-00ba6eb4"></a> `00ba6eb4` | `1f 03 1a eb` | cmp x24,x26 | `FALL_THROUGH`
<a id="insn-00ba6eb8"></a> `00ba6eb8` | `a0 0c 00 54` | b.eq 0x00ba704c | `CONDITIONAL_JUMP`
<a id="insn-00ba6ebc"></a> `00ba6ebc` | `79 10 00 d1` | sub x25,x3,#0x4 | `FALL_THROUGH`
<a id="insn-00ba6ec0"></a> `00ba6ec0` | `e8 03 18 aa` | mov x8,x24 | `FALL_THROUGH`
<a id="insn-00ba6ec4"></a> `00ba6ec4` | `bf 02 13 eb` | cmp x21,x19 | `FALL_THROUGH`
<a id="insn-00ba6ec8"></a> `00ba6ec8` | `21 01 00 54` | b.ne 0x00ba6eec | `CONDITIONAL_JUMP`
<a id="insn-00ba6ecc"></a> `00ba6ecc` | `6d 00 00 14` | b 0x00ba7080 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba6ed0"></a> `00ba6ed0` | `e8 03 18 aa` | mov x8,x24 | `FALL_THROUGH`
<a id="insn-00ba6ed4"></a> `00ba6ed4` | `37 03 00 b9` | str w23,[x25] | `FALL_THROUGH`
<a id="insn-00ba6ed8"></a> `00ba6ed8` | `1f 01 1a eb` | cmp x8,x26 | `FALL_THROUGH`
<a id="insn-00ba6edc"></a> `00ba6edc` | `39 13 00 d1` | sub x25,x25,#0x4 | `FALL_THROUGH`
<a id="insn-00ba6ee0"></a> `00ba6ee0` | `60 0b 00 54` | b.eq 0x00ba704c | `CONDITIONAL_JUMP`
<a id="insn-00ba6ee4"></a> `00ba6ee4` | `bf 02 13 eb` | cmp x21,x19 | `FALL_THROUGH`
<a id="insn-00ba6ee8"></a> `00ba6ee8` | `c0 0c 00 54` | b.eq 0x00ba7080 | `CONDITIONAL_JUMP`
<a id="insn-00ba6eec"></a> `00ba6eec` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ba6ef0"></a> `00ba6ef0` | `fb 03 15 aa` | mov x27,x21 | `FALL_THROUGH`
<a id="insn-00ba6ef4"></a> `00ba6ef4` | `7c cf 5f b8` | ldr w28,[x27, #-0x4]! | `FALL_THROUGH`
<a id="insn-00ba6ef8"></a> `00ba6ef8` | `17 cf 5f b8` | ldr w23,[x24, #-0x4]! | `FALL_THROUGH`
<a id="insn-00ba6efc"></a> `00ba6efc` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba6f00"></a> `00ba6f00` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ba6f04"></a> `00ba6f04` | `09 1d 40 f9` | ldr x9,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00ba6f08"></a> `00ba6f08` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00ba6f0c"></a> `00ba6f0c` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00ba6f10"></a> `00ba6f10` | `09 01 17 cb` | sub x9,x8,x23 | `FALL_THROUGH`
<a id="insn-00ba6f14"></a> `00ba6f14` | `08 01 1c cb` | sub x8,x8,x28 | `FALL_THROUGH`
<a id="insn-00ba6f18"></a> `00ba6f18` | `2a 01 80 b9` | ldrsw x10,[x9] | `FALL_THROUGH`
<a id="insn-00ba6f1c"></a> `00ba6f1c` | `0b 01 80 b9` | ldrsw x11,[x8] | `FALL_THROUGH`
<a id="insn-00ba6f20"></a> `00ba6f20` | `2a 01 0a cb` | sub x10,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba6f24"></a> `00ba6f24` | `0b 01 0b cb` | sub x11,x8,x11 | `FALL_THROUGH`
<a id="insn-00ba6f28"></a> `00ba6f28` | `4a 09 40 79` | ldrh w10,[x10, #0x4] | `FALL_THROUGH`
<a id="insn-00ba6f2c"></a> `00ba6f2c` | `6b 09 40 79` | ldrh w11,[x11, #0x4] | `FALL_THROUGH`
<a id="insn-00ba6f30"></a> `00ba6f30` | `29 01 0a 8b` | add x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba6f34"></a> `00ba6f34` | `08 01 0b 8b` | add x8,x8,x11 | `FALL_THROUGH`
<a id="insn-00ba6f38"></a> `00ba6f38` | `2a 01 40 b9` | ldr w10,[x9] | `FALL_THROUGH`
<a id="insn-00ba6f3c"></a> `00ba6f3c` | `0b 01 40 b9` | ldr w11,[x8] | `FALL_THROUGH`
<a id="insn-00ba6f40"></a> `00ba6f40` | `20 01 0a 8b` | add x0,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba6f44"></a> `00ba6f44` | `01 01 0b 8b` | add x1,x8,x11 | `FALL_THROUGH`
<a id="insn-00ba6f48"></a> `00ba6f48` | `16 44 40 b8` | ldr w22,[x0], #0x4 | `FALL_THROUGH`
<a id="insn-00ba6f4c"></a> `00ba6f4c` | `34 44 40 b8` | ldr w20,[x1], #0x4 | `FALL_THROUGH`
<a id="insn-00ba6f50"></a> `00ba6f50` | `9f 02 16 6b` | cmp w20,w22 | `FALL_THROUGH`
<a id="insn-00ba6f54"></a> `00ba6f54` | `82 32 96 1a` | csel w2,w20,w22,cc | `FALL_THROUGH`
<a id="insn-00ba6f58"></a> `00ba6f58` | `3e c4 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00ba6f5c"></a> `00ba6f5c` | `df 02 14 6b` | cmp w22,w20 | `FALL_THROUGH`
<a id="insn-00ba6f60"></a> `00ba6f60` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00ba6f64"></a> `00ba6f64` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00ba6f68"></a> `00ba6f68` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00ba6f6c"></a> `00ba6f6c` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00ba6f70"></a> `00ba6f70` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ba6f74"></a> `00ba6f74` | `e1 fa ff 54` | b.ne 0x00ba6ed0 | `CONDITIONAL_JUMP`
<a id="insn-00ba6f78"></a> `00ba6f78` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ba6f7c"></a> `00ba6f7c` | `3c 03 00 b9` | str w28,[x25] | `FALL_THROUGH`
<a id="insn-00ba6f80"></a> `00ba6f80` | `f5 03 1b aa` | mov x21,x27 | `FALL_THROUGH`
<a id="insn-00ba6f84"></a> `00ba6f84` | `f8 03 08 aa` | mov x24,x8 | `FALL_THROUGH`
<a id="insn-00ba6f88"></a> `00ba6f88` | `d4 ff ff 17` | b 0x00ba6ed8 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba6f8c"></a> `00ba6f8c` | `7f 02 15 eb` | cmp x19,x21 | `FALL_THROUGH`
<a id="insn-00ba6f90"></a> `00ba6f90` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00ba6f94"></a> `00ba6f94` | `c0 04 00 54` | b.eq 0x00ba702c | `CONDITIONAL_JUMP`
<a id="insn-00ba6f98"></a> `00ba6f98` | `a8 02 13 cb` | sub x8,x21,x19 | `FALL_THROUGH`
<a id="insn-00ba6f9c"></a> `00ba6f9c` | `0a 11 00 d1` | sub x10,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00ba6fa0"></a> `00ba6fa0` | `48 fd 42 d3` | lsr x8,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00ba6fa4"></a> `00ba6fa4` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ba6fa8"></a> `00ba6fa8` | `3f 1d 00 f1` | cmp x9,#0x7 | `FALL_THROUGH`
<a id="insn-00ba6fac"></a> `00ba6fac` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00ba6fb0"></a> `00ba6fb0` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00ba6fb4"></a> `00ba6fb4` | `49 03 00 54` | b.ls 0x00ba701c | `CONDITIONAL_JUMP`
<a id="insn-00ba6fb8"></a> `00ba6fb8` | `48 f5 7e 92` | and x8,x10,#-0x4 | `FALL_THROUGH`
<a id="insn-00ba6fbc"></a> `00ba6fbc` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00ba6fc0"></a> `00ba6fc0` | `6a 02 08 8b` | add x10,x19,x8 | `FALL_THROUGH`
<a id="insn-00ba6fc4"></a> `00ba6fc4` | `5f 01 1a eb` | cmp x10,x26 | `FALL_THROUGH`
<a id="insn-00ba6fc8"></a> `00ba6fc8` | `c9 00 00 54` | b.ls 0x00ba6fe0 | `CONDITIONAL_JUMP`
<a id="insn-00ba6fcc"></a> `00ba6fcc` | `48 03 08 8b` | add x8,x26,x8 | `FALL_THROUGH`
<a id="insn-00ba6fd0"></a> `00ba6fd0` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00ba6fd4"></a> `00ba6fd4` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00ba6fd8"></a> `00ba6fd8` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00ba6fdc"></a> `00ba6fdc` | `08 02 00 54` | b.hi 0x00ba701c | `CONDITIONAL_JUMP`
<a id="insn-00ba6fe0"></a> `00ba6fe0` | `2a ed 7d 92` | and x10,x9,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-00ba6fe4"></a> `00ba6fe4` | `4c f5 7e d3` | lsl x12,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00ba6fe8"></a> `00ba6fe8` | `4b 43 00 91` | add x11,x26,#0x10 | `FALL_THROUGH`
<a id="insn-00ba6fec"></a> `00ba6fec` | `68 02 0c 8b` | add x8,x19,x12 | `FALL_THROUGH`
<a id="insn-00ba6ff0"></a> `00ba6ff0` | `41 03 0c 8b` | add x1,x26,x12 | `FALL_THROUGH`
<a id="insn-00ba6ff4"></a> `00ba6ff4` | `6c 42 00 91` | add x12,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00ba6ff8"></a> `00ba6ff8` | `ed 03 0a aa` | mov x13,x10 | `FALL_THROUGH`
<a id="insn-00ba6ffc"></a> `00ba6ffc` | `80 85 7f ad` | ldp q0,q1,[x12, #-0x10] | `FALL_THROUGH`
<a id="insn-00ba7000"></a> `00ba7000` | `ad 21 00 f1` | subs x13,x13,#0x8 | `FALL_THROUGH`
<a id="insn-00ba7004"></a> `00ba7004` | `8c 81 00 91` | add x12,x12,#0x20 | `FALL_THROUGH`
<a id="insn-00ba7008"></a> `00ba7008` | `60 85 3f ad` | stp q0,q1,[x11, #-0x10] | `FALL_THROUGH`
<a id="insn-00ba700c"></a> `00ba700c` | `6b 81 00 91` | add x11,x11,#0x20 | `FALL_THROUGH`
<a id="insn-00ba7010"></a> `00ba7010` | `61 ff ff 54` | b.ne 0x00ba6ffc | `CONDITIONAL_JUMP`
<a id="insn-00ba7014"></a> `00ba7014` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00ba7018"></a> `00ba7018` | `a0 00 00 54` | b.eq 0x00ba702c | `CONDITIONAL_JUMP`
<a id="insn-00ba701c"></a> `00ba701c` | `09 45 40 b8` | ldr w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00ba7020"></a> `00ba7020` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00ba7024"></a> `00ba7024` | `29 44 00 b8` | str w9,[x1], #0x4 | `FALL_THROUGH`
<a id="insn-00ba7028"></a> `00ba7028` | `a1 ff ff 54` | b.ne 0x00ba701c | `CONDITIONAL_JUMP`
<a id="insn-00ba702c"></a> `00ba702c` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba7030"></a> `00ba7030` | `e5 83 00 91` | add x5,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ba7034"></a> `00ba7034` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00ba7038"></a> `00ba7038` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00ba703c"></a> `00ba703c` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ba7040"></a> `00ba7040` | `e4 03 13 aa` | mov x4,x19 | `FALL_THROUGH`
<a id="insn-00ba7044"></a> `00ba7044` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba7048"></a> `00ba7048` | `1e d7 02 94` | bl 0x00c5ccc0 | `UNCONDITIONAL_CALL`
<a id="insn-00ba704c"></a> `00ba704c` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ba7050"></a> `00ba7050` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00ba7054"></a> `00ba7054` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00ba7058"></a> `00ba7058` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ba705c"></a> `00ba705c` | `41 02 00 54` | b.ne 0x00ba70a4 | `CONDITIONAL_JUMP`
<a id="insn-00ba7060"></a> `00ba7060` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00ba7064"></a> `00ba7064` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ba7068"></a> `00ba7068` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ba706c"></a> `00ba706c` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ba7070"></a> `00ba7070` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ba7074"></a> `00ba7074` | `fc 6f 43 a9` | ldp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba7078"></a> `00ba7078` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00ba707c"></a> `00ba707c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ba7080"></a> `00ba7080` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00ba7084"></a> `00ba7084` | `49 03 18 cb` | sub x9,x26,x24 | `FALL_THROUGH`
<a id="insn-00ba7088"></a> `00ba7088` | `0a 13 00 d1` | sub x10,x24,#0x4 | `FALL_THROUGH`
<a id="insn-00ba708c"></a> `00ba708c` | `4b 69 68 b8` | ldr w11,[x10, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ba7090"></a> `00ba7090` | `2b 6b 28 b8` | str w11,[x25, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ba7094"></a> `00ba7094` | `08 11 00 d1` | sub x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00ba7098"></a> `00ba7098` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00ba709c"></a> `00ba709c` | `81 ff ff 54` | b.ne 0x00ba708c | `CONDITIONAL_JUMP`
<a id="insn-00ba70a0"></a> `00ba70a0` | `eb ff ff 17` | b 0x00ba704c | `UNCONDITIONAL_JUMP`
<a id="insn-00ba70a4"></a> `00ba70a4` | `8f c3 02 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ba6dcc`](#insn-00ba6dcc) 範囲 `[['00ba6dcc', '00ba6dd3']]`
  - `FALL_THROUGH` [`00ba6dd0`](#insn-00ba6dd0) → [`00ba6dd4`](#insn-00ba6dd4)
- ブロック [`00ba6dd4`](#insn-00ba6dd4) 範囲 `[['00ba6dd4', '00ba6e07']]`
  - `FALL_THROUGH` [`00ba6e04`](#insn-00ba6e04) → [`00ba6e08`](#insn-00ba6e08)
- ブロック [`00ba6e08`](#insn-00ba6e08) 範囲 `[['00ba6e08', '00ba6e13']]`
  - `FALL_THROUGH` [`00ba6e10`](#insn-00ba6e10) → [`00ba6e14`](#insn-00ba6e14)
- ブロック [`00ba6e14`](#insn-00ba6e14) 範囲 `[['00ba6e14', '00ba6e17']]`
  - `CONDITIONAL_JUMP` [`00ba6e14`](#insn-00ba6e14) → [`00ba6f8c`](#insn-00ba6f8c)
  - `FALL_THROUGH` [`00ba6e14`](#insn-00ba6e14) → [`00ba6e18`](#insn-00ba6e18)
- ブロック [`00ba6e18`](#insn-00ba6e18) 範囲 `[['00ba6e18', '00ba6e1f']]`
  - `CONDITIONAL_JUMP` [`00ba6e1c`](#insn-00ba6e1c) → [`00ba704c`](#insn-00ba704c)
  - `FALL_THROUGH` [`00ba6e1c`](#insn-00ba6e1c) → [`00ba6e20`](#insn-00ba6e20)
- ブロック [`00ba6e20`](#insn-00ba6e20) 範囲 `[['00ba6e20', '00ba6e3b']]`
  - `FALL_THROUGH` [`00ba6e38`](#insn-00ba6e38) → [`00ba6e3c`](#insn-00ba6e3c)
- ブロック [`00ba6e3c`](#insn-00ba6e3c) 範囲 `[['00ba6e3c', '00ba6e3f']]`
  - `CONDITIONAL_JUMP` [`00ba6e3c`](#insn-00ba6e3c) → [`00ba6ea4`](#insn-00ba6ea4)
  - `FALL_THROUGH` [`00ba6e3c`](#insn-00ba6e3c) → [`00ba6e40`](#insn-00ba6e40)
- ブロック [`00ba6e40`](#insn-00ba6e40) 範囲 `[['00ba6e40', '00ba6e53']]`
  - `CONDITIONAL_JUMP` [`00ba6e50`](#insn-00ba6e50) → [`00ba6e68`](#insn-00ba6e68)
  - `FALL_THROUGH` [`00ba6e50`](#insn-00ba6e50) → [`00ba6e54`](#insn-00ba6e54)
- ブロック [`00ba6e54`](#insn-00ba6e54) 範囲 `[['00ba6e54', '00ba6e5b']]`
  - `FALL_THROUGH` [`00ba6e58`](#insn-00ba6e58) → [`00ba6e5c`](#insn-00ba6e5c)
- ブロック [`00ba6e5c`](#insn-00ba6e5c) 範囲 `[['00ba6e5c', '00ba6e67']]`
  - `CONDITIONAL_JUMP` [`00ba6e64`](#insn-00ba6e64) → [`00ba6ea4`](#insn-00ba6ea4)
  - `FALL_THROUGH` [`00ba6e64`](#insn-00ba6e64) → [`00ba6e68`](#insn-00ba6e68)
- ブロック [`00ba6e68`](#insn-00ba6e68) 範囲 `[['00ba6e68', '00ba6e83']]`
  - `FALL_THROUGH` [`00ba6e80`](#insn-00ba6e80) → [`00ba6e84`](#insn-00ba6e84)
- ブロック [`00ba6e84`](#insn-00ba6e84) 範囲 `[['00ba6e84', '00ba6e93']]`
  - `FALL_THROUGH` [`00ba6e90`](#insn-00ba6e90) → [`00ba6e94`](#insn-00ba6e94)
- ブロック [`00ba6e94`](#insn-00ba6e94) 範囲 `[['00ba6e94', '00ba6e9b']]`
  - `CONDITIONAL_JUMP` [`00ba6e98`](#insn-00ba6e98) → [`00ba6e84`](#insn-00ba6e84)
  - `FALL_THROUGH` [`00ba6e98`](#insn-00ba6e98) → [`00ba6e9c`](#insn-00ba6e9c)
- ブロック [`00ba6e9c`](#insn-00ba6e9c) 範囲 `[['00ba6e9c', '00ba6ea3']]`
  - `CONDITIONAL_JUMP` [`00ba6ea0`](#insn-00ba6ea0) → [`00ba6eb4`](#insn-00ba6eb4)
  - `FALL_THROUGH` [`00ba6ea0`](#insn-00ba6ea0) → [`00ba6ea4`](#insn-00ba6ea4)
- ブロック [`00ba6ea4`](#insn-00ba6ea4) 範囲 `[['00ba6ea4', '00ba6eb3']]`
  - `CONDITIONAL_JUMP` [`00ba6eb0`](#insn-00ba6eb0) → [`00ba6ea4`](#insn-00ba6ea4)
  - `FALL_THROUGH` [`00ba6eb0`](#insn-00ba6eb0) → [`00ba6eb4`](#insn-00ba6eb4)
- ブロック [`00ba6eb4`](#insn-00ba6eb4) 範囲 `[['00ba6eb4', '00ba6ebb']]`
  - `CONDITIONAL_JUMP` [`00ba6eb8`](#insn-00ba6eb8) → [`00ba704c`](#insn-00ba704c)
  - `FALL_THROUGH` [`00ba6eb8`](#insn-00ba6eb8) → [`00ba6ebc`](#insn-00ba6ebc)
- ブロック [`00ba6ebc`](#insn-00ba6ebc) 範囲 `[['00ba6ebc', '00ba6ebf']]`
  - `FALL_THROUGH` [`00ba6ebc`](#insn-00ba6ebc) → [`00ba6ec0`](#insn-00ba6ec0)
- ブロック [`00ba6ec0`](#insn-00ba6ec0) 範囲 `[['00ba6ec0', '00ba6ec3']]`
  - `FALL_THROUGH` [`00ba6ec0`](#insn-00ba6ec0) → [`00ba6ec4`](#insn-00ba6ec4)
- ブロック [`00ba6ec4`](#insn-00ba6ec4) 範囲 `[['00ba6ec4', '00ba6ecb']]`
  - `CONDITIONAL_JUMP` [`00ba6ec8`](#insn-00ba6ec8) → [`00ba6eec`](#insn-00ba6eec)
  - `FALL_THROUGH` [`00ba6ec8`](#insn-00ba6ec8) → [`00ba6ecc`](#insn-00ba6ecc)
- ブロック [`00ba6ecc`](#insn-00ba6ecc) 範囲 `[['00ba6ecc', '00ba6ecf']]`
  - `UNCONDITIONAL_JUMP` [`00ba6ecc`](#insn-00ba6ecc) → [`00ba7080`](#insn-00ba7080)
- ブロック [`00ba6ed0`](#insn-00ba6ed0) 範囲 `[['00ba6ed0', '00ba6ed7']]`
  - `FALL_THROUGH` [`00ba6ed4`](#insn-00ba6ed4) → [`00ba6ed8`](#insn-00ba6ed8)
- ブロック [`00ba6ed8`](#insn-00ba6ed8) 範囲 `[['00ba6ed8', '00ba6edb']]`
  - `FALL_THROUGH` [`00ba6ed8`](#insn-00ba6ed8) → [`00ba6edc`](#insn-00ba6edc)
- ブロック [`00ba6edc`](#insn-00ba6edc) 範囲 `[['00ba6edc', '00ba6edf']]`
  - `FALL_THROUGH` [`00ba6edc`](#insn-00ba6edc) → [`00ba6ee0`](#insn-00ba6ee0)
- ブロック [`00ba6ee0`](#insn-00ba6ee0) 範囲 `[['00ba6ee0', '00ba6ee3']]`
  - `CONDITIONAL_JUMP` [`00ba6ee0`](#insn-00ba6ee0) → [`00ba704c`](#insn-00ba704c)
  - `FALL_THROUGH` [`00ba6ee0`](#insn-00ba6ee0) → [`00ba6ee4`](#insn-00ba6ee4)
- ブロック [`00ba6ee4`](#insn-00ba6ee4) 範囲 `[['00ba6ee4', '00ba6eeb']]`
  - `CONDITIONAL_JUMP` [`00ba6ee8`](#insn-00ba6ee8) → [`00ba7080`](#insn-00ba7080)
  - `FALL_THROUGH` [`00ba6ee8`](#insn-00ba6ee8) → [`00ba6eec`](#insn-00ba6eec)
- ブロック [`00ba6eec`](#insn-00ba6eec) 範囲 `[['00ba6eec', '00ba6eef']]`
  - `FALL_THROUGH` [`00ba6eec`](#insn-00ba6eec) → [`00ba6ef0`](#insn-00ba6ef0)
- ブロック [`00ba6ef0`](#insn-00ba6ef0) 範囲 `[['00ba6ef0', '00ba6eff']]`
  - `FALL_THROUGH` [`00ba6efc`](#insn-00ba6efc) → [`00ba6f00`](#insn-00ba6f00)
- ブロック [`00ba6f00`](#insn-00ba6f00) 範囲 `[['00ba6f00', '00ba6f07']]`
  - `FALL_THROUGH` [`00ba6f04`](#insn-00ba6f04) → [`00ba6f08`](#insn-00ba6f08)
- ブロック [`00ba6f08`](#insn-00ba6f08) 範囲 `[['00ba6f08', '00ba6f0b']]`
  - `FALL_THROUGH` [`00ba6f08`](#insn-00ba6f08) → [`00ba6f0c`](#insn-00ba6f0c)
- ブロック [`00ba6f0c`](#insn-00ba6f0c) 範囲 `[['00ba6f0c', '00ba6f1b']]`
  - `FALL_THROUGH` [`00ba6f18`](#insn-00ba6f18) → [`00ba6f1c`](#insn-00ba6f1c)
- ブロック [`00ba6f1c`](#insn-00ba6f1c) 範囲 `[['00ba6f1c', '00ba6f47']]`
  - `FALL_THROUGH` [`00ba6f44`](#insn-00ba6f44) → [`00ba6f48`](#insn-00ba6f48)
- ブロック [`00ba6f48`](#insn-00ba6f48) 範囲 `[['00ba6f48', '00ba6f67']]`
  - `FALL_THROUGH` [`00ba6f64`](#insn-00ba6f64) → [`00ba6f68`](#insn-00ba6f68)
- ブロック [`00ba6f68`](#insn-00ba6f68) 範囲 `[['00ba6f68', '00ba6f77']]`
  - `CONDITIONAL_JUMP` [`00ba6f74`](#insn-00ba6f74) → [`00ba6ed0`](#insn-00ba6ed0)
  - `FALL_THROUGH` [`00ba6f74`](#insn-00ba6f74) → [`00ba6f78`](#insn-00ba6f78)
- ブロック [`00ba6f78`](#insn-00ba6f78) 範囲 `[['00ba6f78', '00ba6f8b']]`
  - `UNCONDITIONAL_JUMP` [`00ba6f88`](#insn-00ba6f88) → [`00ba6ed8`](#insn-00ba6ed8)
- ブロック [`00ba6f8c`](#insn-00ba6f8c) 範囲 `[['00ba6f8c', '00ba6f97']]`
  - `CONDITIONAL_JUMP` [`00ba6f94`](#insn-00ba6f94) → [`00ba702c`](#insn-00ba702c)
  - `FALL_THROUGH` [`00ba6f94`](#insn-00ba6f94) → [`00ba6f98`](#insn-00ba6f98)
- ブロック [`00ba6f98`](#insn-00ba6f98) 範囲 `[['00ba6f98', '00ba6f9f']]`
  - `FALL_THROUGH` [`00ba6f9c`](#insn-00ba6f9c) → [`00ba6fa0`](#insn-00ba6fa0)
- ブロック [`00ba6fa0`](#insn-00ba6fa0) 範囲 `[['00ba6fa0', '00ba6fa3']]`
  - `FALL_THROUGH` [`00ba6fa0`](#insn-00ba6fa0) → [`00ba6fa4`](#insn-00ba6fa4)
- ブロック [`00ba6fa4`](#insn-00ba6fa4) 範囲 `[['00ba6fa4', '00ba6fb7']]`
  - `CONDITIONAL_JUMP` [`00ba6fb4`](#insn-00ba6fb4) → [`00ba701c`](#insn-00ba701c)
  - `FALL_THROUGH` [`00ba6fb4`](#insn-00ba6fb4) → [`00ba6fb8`](#insn-00ba6fb8)
- ブロック [`00ba6fb8`](#insn-00ba6fb8) 範囲 `[['00ba6fb8', '00ba6fcb']]`
  - `CONDITIONAL_JUMP` [`00ba6fc8`](#insn-00ba6fc8) → [`00ba6fe0`](#insn-00ba6fe0)
  - `FALL_THROUGH` [`00ba6fc8`](#insn-00ba6fc8) → [`00ba6fcc`](#insn-00ba6fcc)
- ブロック [`00ba6fcc`](#insn-00ba6fcc) 範囲 `[['00ba6fcc', '00ba6fdf']]`
  - `CONDITIONAL_JUMP` [`00ba6fdc`](#insn-00ba6fdc) → [`00ba701c`](#insn-00ba701c)
  - `FALL_THROUGH` [`00ba6fdc`](#insn-00ba6fdc) → [`00ba6fe0`](#insn-00ba6fe0)
- ブロック [`00ba6fe0`](#insn-00ba6fe0) 範囲 `[['00ba6fe0', '00ba6fe3']]`
  - `FALL_THROUGH` [`00ba6fe0`](#insn-00ba6fe0) → [`00ba6fe4`](#insn-00ba6fe4)
- ブロック [`00ba6fe4`](#insn-00ba6fe4) 範囲 `[['00ba6fe4', '00ba6ffb']]`
  - `FALL_THROUGH` [`00ba6ff8`](#insn-00ba6ff8) → [`00ba6ffc`](#insn-00ba6ffc)
- ブロック [`00ba6ffc`](#insn-00ba6ffc) 範囲 `[['00ba6ffc', '00ba7007']]`
  - `FALL_THROUGH` [`00ba7004`](#insn-00ba7004) → [`00ba7008`](#insn-00ba7008)
- ブロック [`00ba7008`](#insn-00ba7008) 範囲 `[['00ba7008', '00ba7013']]`
  - `CONDITIONAL_JUMP` [`00ba7010`](#insn-00ba7010) → [`00ba6ffc`](#insn-00ba6ffc)
  - `FALL_THROUGH` [`00ba7010`](#insn-00ba7010) → [`00ba7014`](#insn-00ba7014)
- ブロック [`00ba7014`](#insn-00ba7014) 範囲 `[['00ba7014', '00ba701b']]`
  - `CONDITIONAL_JUMP` [`00ba7018`](#insn-00ba7018) → [`00ba702c`](#insn-00ba702c)
  - `FALL_THROUGH` [`00ba7018`](#insn-00ba7018) → [`00ba701c`](#insn-00ba701c)
- ブロック [`00ba701c`](#insn-00ba701c) 範囲 `[['00ba701c', '00ba702b']]`
  - `CONDITIONAL_JUMP` [`00ba7028`](#insn-00ba7028) → [`00ba701c`](#insn-00ba701c)
  - `FALL_THROUGH` [`00ba7028`](#insn-00ba7028) → [`00ba702c`](#insn-00ba702c)
- ブロック [`00ba702c`](#insn-00ba702c) 範囲 `[['00ba702c', '00ba702f']]`
  - `FALL_THROUGH` [`00ba702c`](#insn-00ba702c) → [`00ba7030`](#insn-00ba7030)
- ブロック [`00ba7030`](#insn-00ba7030) 範囲 `[['00ba7030', '00ba704b']]`
  - `FALL_THROUGH` [`00ba7048`](#insn-00ba7048) → [`00ba704c`](#insn-00ba704c)
- ブロック [`00ba704c`](#insn-00ba704c) 範囲 `[['00ba704c', '00ba704f']]`
  - `FALL_THROUGH` [`00ba704c`](#insn-00ba704c) → [`00ba7050`](#insn-00ba7050)
- ブロック [`00ba7050`](#insn-00ba7050) 範囲 `[['00ba7050', '00ba705b']]`
  - `FALL_THROUGH` [`00ba7058`](#insn-00ba7058) → [`00ba705c`](#insn-00ba705c)
- ブロック [`00ba705c`](#insn-00ba705c) 範囲 `[['00ba705c', '00ba705f']]`
  - `CONDITIONAL_JUMP` [`00ba705c`](#insn-00ba705c) → [`00ba70a4`](#insn-00ba70a4)
  - `FALL_THROUGH` [`00ba705c`](#insn-00ba705c) → [`00ba7060`](#insn-00ba7060)
- ブロック [`00ba7060`](#insn-00ba7060) 範囲 `[['00ba7060', '00ba707b']]`
  - `FALL_THROUGH` [`00ba7078`](#insn-00ba7078) → [`00ba707c`](#insn-00ba707c)
- ブロック [`00ba707c`](#insn-00ba707c) 範囲 `[['00ba707c', '00ba707f']]`
- ブロック [`00ba7080`](#insn-00ba7080) 範囲 `[['00ba7080', '00ba708b']]`
  - `FALL_THROUGH` [`00ba7088`](#insn-00ba7088) → [`00ba708c`](#insn-00ba708c)
- ブロック [`00ba708c`](#insn-00ba708c) 範囲 `[['00ba708c', '00ba7097']]`
  - `FALL_THROUGH` [`00ba7094`](#insn-00ba7094) → [`00ba7098`](#insn-00ba7098)
- ブロック [`00ba7098`](#insn-00ba7098) 範囲 `[['00ba7098', '00ba709f']]`
  - `CONDITIONAL_JUMP` [`00ba709c`](#insn-00ba709c) → [`00ba708c`](#insn-00ba708c)
  - `FALL_THROUGH` [`00ba709c`](#insn-00ba709c) → [`00ba70a0`](#insn-00ba70a0)
- ブロック [`00ba70a0`](#insn-00ba70a0) 範囲 `[['00ba70a0', '00ba70a3']]`
  - `UNCONDITIONAL_JUMP` [`00ba70a0`](#insn-00ba70a0) → [`00ba704c`](#insn-00ba704c)
- ブロック [`00ba70a4`](#insn-00ba70a4) 範囲 `[['00ba70a4', '00ba70a7']]`

## 命令位置別の参照

- [`00ba6dd0`](#insn-00ba6dd0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6dd4`](#insn-00ba6dd4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6dd8`](#insn-00ba6dd8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6ddc`](#insn-00ba6ddc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6de0`](#insn-00ba6de0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6de4`](#insn-00ba6de4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6dec`](#insn-00ba6dec) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6df4`](#insn-00ba6df4) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6e10`](#insn-00ba6e10) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6e14`](#insn-00ba6e14) → [`00ba6f8c`](#insn-00ba6f8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6e1c`](#insn-00ba6e1c) → [`00ba704c`](#insn-00ba704c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6e3c`](#insn-00ba6e3c) → [`00ba6ea4`](#insn-00ba6ea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6e50`](#insn-00ba6e50) → [`00ba6e68`](#insn-00ba6e68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6e64`](#insn-00ba6e64) → [`00ba6ea4`](#insn-00ba6ea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6e98`](#insn-00ba6e98) → [`00ba6e84`](#insn-00ba6e84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6ea0`](#insn-00ba6ea0) → [`00ba6eb4`](#insn-00ba6eb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6eb0`](#insn-00ba6eb0) → [`00ba6ea4`](#insn-00ba6ea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6eb8`](#insn-00ba6eb8) → [`00ba704c`](#insn-00ba704c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6ec8`](#insn-00ba6ec8) → [`00ba6eec`](#insn-00ba6eec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6ecc`](#insn-00ba6ecc) → [`00ba7080`](#insn-00ba7080) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6ee0`](#insn-00ba6ee0) → [`00ba704c`](#insn-00ba704c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6ee8`](#insn-00ba6ee8) → [`00ba7080`](#insn-00ba7080) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6eec`](#insn-00ba6eec) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6efc`](#insn-00ba6efc) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6f58`](#insn-00ba6f58) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00ba6f74`](#insn-00ba6f74) → [`00ba6ed0`](#insn-00ba6ed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6f78`](#insn-00ba6f78) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6f88`](#insn-00ba6f88) → [`00ba6ed8`](#insn-00ba6ed8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6f94`](#insn-00ba6f94) → [`00ba702c`](#insn-00ba702c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6fb4`](#insn-00ba6fb4) → [`00ba701c`](#insn-00ba701c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6fc8`](#insn-00ba6fc8) → [`00ba6fe0`](#insn-00ba6fe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6fdc`](#insn-00ba6fdc) → [`00ba701c`](#insn-00ba701c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7010`](#insn-00ba7010) → [`00ba6ffc`](#insn-00ba6ffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7018`](#insn-00ba7018) → [`00ba702c`](#insn-00ba702c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7028`](#insn-00ba7028) → [`00ba701c`](#insn-00ba701c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba702c`](#insn-00ba702c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7044`](#insn-00ba7044) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7048`](#insn-00ba7048) → [`00c5ccc0`](../00c5c/00c5ccc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ccc0` · 推定シンボル `None` · 推定型 `None`
- [`00ba704c`](#insn-00ba704c) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7054`](#insn-00ba7054) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba705c`](#insn-00ba705c) → [`00ba70a4`](#insn-00ba70a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7060`](#insn-00ba7060) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7064`](#insn-00ba7064) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7068`](#insn-00ba7068) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba706c`](#insn-00ba706c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7070`](#insn-00ba7070) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba7074`](#insn-00ba7074) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba709c`](#insn-00ba709c) → [`00ba708c`](#insn-00ba708c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba70a0`](#insn-00ba70a0) → [`00ba704c`](#insn-00ba704c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba70a4`](#insn-00ba70a4) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ba6dd0`](#insn-00ba6dd0)

~~~json
{
  "source": "00ba6dd0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6dd4`](#insn-00ba6dd4)

~~~json
{
  "source": "00ba6dd4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6dd8`](#insn-00ba6dd8)

~~~json
{
  "source": "00ba6dd8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6ddc`](#insn-00ba6ddc)

~~~json
{
  "source": "00ba6ddc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6de0`](#insn-00ba6de0)

~~~json
{
  "source": "00ba6de0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6de4`](#insn-00ba6de4)

~~~json
{
  "source": "00ba6de4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6dec`](#insn-00ba6dec)

~~~json
{
  "source": "00ba6dec",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6df4`](#insn-00ba6df4)

~~~json
{
  "source": "00ba6df4",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6e10`](#insn-00ba6e10)

~~~json
{
  "source": "00ba6e10",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6e14`](#insn-00ba6e14)

~~~json
{
  "source": "00ba6e14",
  "target": "00ba6f8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6e1c`](#insn-00ba6e1c)

~~~json
{
  "source": "00ba6e1c",
  "target": "00ba704c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6e3c`](#insn-00ba6e3c)

~~~json
{
  "source": "00ba6e3c",
  "target": "00ba6ea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6e50`](#insn-00ba6e50)

~~~json
{
  "source": "00ba6e50",
  "target": "00ba6e68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6e64`](#insn-00ba6e64)

~~~json
{
  "source": "00ba6e64",
  "target": "00ba6ea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6e98`](#insn-00ba6e98)

~~~json
{
  "source": "00ba6e98",
  "target": "00ba6e84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6ea0`](#insn-00ba6ea0)

~~~json
{
  "source": "00ba6ea0",
  "target": "00ba6eb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6eb0`](#insn-00ba6eb0)

~~~json
{
  "source": "00ba6eb0",
  "target": "00ba6ea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6eb8`](#insn-00ba6eb8)

~~~json
{
  "source": "00ba6eb8",
  "target": "00ba704c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6ec8`](#insn-00ba6ec8)

~~~json
{
  "source": "00ba6ec8",
  "target": "00ba6eec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6ecc`](#insn-00ba6ecc)

~~~json
{
  "source": "00ba6ecc",
  "target": "00ba7080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6ee0`](#insn-00ba6ee0)

~~~json
{
  "source": "00ba6ee0",
  "target": "00ba704c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6ee8`](#insn-00ba6ee8)

~~~json
{
  "source": "00ba6ee8",
  "target": "00ba7080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6eec`](#insn-00ba6eec)

~~~json
{
  "source": "00ba6eec",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6efc`](#insn-00ba6efc)

~~~json
{
  "source": "00ba6efc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6f58`](#insn-00ba6f58)

~~~json
{
  "source": "00ba6f58",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba6f74`](#insn-00ba6f74)

~~~json
{
  "source": "00ba6f74",
  "target": "00ba6ed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6f78`](#insn-00ba6f78)

~~~json
{
  "source": "00ba6f78",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6f88`](#insn-00ba6f88)

~~~json
{
  "source": "00ba6f88",
  "target": "00ba6ed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6f94`](#insn-00ba6f94)

~~~json
{
  "source": "00ba6f94",
  "target": "00ba702c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6fb4`](#insn-00ba6fb4)

~~~json
{
  "source": "00ba6fb4",
  "target": "00ba701c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6fc8`](#insn-00ba6fc8)

~~~json
{
  "source": "00ba6fc8",
  "target": "00ba6fe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6fdc`](#insn-00ba6fdc)

~~~json
{
  "source": "00ba6fdc",
  "target": "00ba701c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7010`](#insn-00ba7010)

~~~json
{
  "source": "00ba7010",
  "target": "00ba6ffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7018`](#insn-00ba7018)

~~~json
{
  "source": "00ba7018",
  "target": "00ba702c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7028`](#insn-00ba7028)

~~~json
{
  "source": "00ba7028",
  "target": "00ba701c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba702c`](#insn-00ba702c)

~~~json
{
  "source": "00ba702c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7044`](#insn-00ba7044)

~~~json
{
  "source": "00ba7044",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7048`](#insn-00ba7048)

~~~json
{
  "source": "00ba7048",
  "target": "00c5ccc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba704c`](#insn-00ba704c)

~~~json
{
  "source": "00ba704c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7054`](#insn-00ba7054)

~~~json
{
  "source": "00ba7054",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba705c`](#insn-00ba705c)

~~~json
{
  "source": "00ba705c",
  "target": "00ba70a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7060`](#insn-00ba7060)

~~~json
{
  "source": "00ba7060",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7064`](#insn-00ba7064)

~~~json
{
  "source": "00ba7064",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7068`](#insn-00ba7068)

~~~json
{
  "source": "00ba7068",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba706c`](#insn-00ba706c)

~~~json
{
  "source": "00ba706c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7070`](#insn-00ba7070)

~~~json
{
  "source": "00ba7070",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba7074`](#insn-00ba7074)

~~~json
{
  "source": "00ba7074",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba709c`](#insn-00ba709c)

~~~json
{
  "source": "00ba709c",
  "target": "00ba708c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba70a0`](#insn-00ba70a0)

~~~json
{
  "source": "00ba70a0",
  "target": "00ba704c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba70a4`](#insn-00ba70a4)

~~~json
{
  "source": "00ba70a4",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
