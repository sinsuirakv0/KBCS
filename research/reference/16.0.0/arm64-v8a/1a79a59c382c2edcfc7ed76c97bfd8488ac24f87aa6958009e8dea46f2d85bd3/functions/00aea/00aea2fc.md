# 00aea2fc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0162.md#review-e828b7aa5a1fbc91ce9f003f067133e0)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aea724`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aea/00aea724.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0064.md#compare-15394dd5d92be8ebf066c2f0928f6a23)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aea2fc",
  "name": "FUN_00aea2fc",
  "size": 1400,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a8590865c3f077d31cc3c14a80e2e7fc523e2f0878e8e654813f87bfed858e3c",
  "source_text_sha256": "a8590865c3f077d31cc3c14a80e2e7fc523e2f0878e8e654813f87bfed858e3c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aea2fc",
        "00aea873"
      ]
    ],
    "bytes_sha256": "864aa2c151842e3502dd8b62e0a8cd4c33f4c3624641a35eade7aa017970a3d8",
    "instruction_count": 350,
    "instruction_bytes": 1400,
    "body_bytes": 1400,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae0e64](../00ae0/00ae0e64.md)
- [00af0928](../00af0/00af0928.md)

## 呼び出し先

- [00467820](../00467/00467820.md)
- [00467ab0](../00467/00467ab0.md)
- [00467aec](../00467/00467aec.md)
- [00467b20](../00467/00467b20.md)
- [00467f14](../00467/00467f14.md)
- [00468b9c](../00468/00468b9c.md)
- [00468f48](../00468/00468f48.md)
- [00469bc4](../00469/00469bc4.md)
- [0046da7c](../0046d/0046da7c.md)
- [005c04b0](../005c0/005c04b0.md)
- [00743d50](../00743/00743d50.md)
- [00743eec](../00743/00743eec.md)
- [00744158](../00744/00744158.md)
- [007441c8](../00744/007441c8.md)
- [00a41e38](../00a41/00a41e38.md)
- [00a41ec4](../00a41/00a41ec4.md)
- [00a41f9c](../00a41/00a41f9c.md)
- [00adee94](../00ade/00adee94.md)
- [00b09234](../00b09/00b09234.md)
- [00b0a8ec](../00b0a/00b0a8ec.md)
- [00c58210](../00c58/00c58210.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 9624 bytes

~~~c

void FUN_00aea2fc(long param_1,uint param_2)

{
  int iVar1;
  byte *pbVar2;
  long lVar3;
  int iVar4;
  int iVar5;
  undefined4 uVar6;
  long lVar7;
  undefined8 uVar8;
  ulong uVar9;
  long lVar10;
  undefined8 uVar11;
  undefined8 uVar12;
  long lVar13;
  long lVar14;
  ulong uVar15;
  
                    /* try { // try from 00aea2fc to 00bea31f has its CatchHandler @ 00aea780 */
                    /* try { // try from 00aea320 to 00bea3bf has its CatchHandler @ 00aea1c8 */
  if (DAT_00ca4578 == 0) {
    lVar7 = 0;
  }
  else {
    lVar7 = __dynamic_cast(DAT_00ca4578,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65a58,
                           &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c8d550,0);
  }
  uVar8 = FUN_00467820();
  if (*(int *)((long)&fde_table_entry_00333a88.initial_loc + param_1) - 1U == param_2) {
    return;
  }
  lVar14 = param_1 + 0xc5b8;
  uVar15 = -(ulong)(param_2 >> 0x1f) & 0xfffffffc00000000 | (ulong)param_2 << 2;
  lVar13 = lVar14 + (long)*(int *)((long)&DWORD_0039b97c + param_1) * 0x2c;
  pbVar2 = (byte *)(lVar13 + uVar15);
                    /* try { // try from 00aea3c0 to 00bea3cf has its CatchHandler @ 00aea744 */
  if (((uint)(*(byte *)(lVar13 + 0x2a) ^ pbVar2[2]) << 0x10 |
       (uint)(*(byte *)(lVar13 + 0x2b) ^ pbVar2[3]) << 0x18 |
       (uint)(*(byte *)(lVar13 + 0x29) ^ pbVar2[1]) << 8 |
      (uint)(*(byte *)(lVar13 + 0x28) ^ *pbVar2)) == 0xffffffff) {
    return;
  }
                    /* try { // try from 00aea3e0 to 00bea3e7 has its CatchHandler @ 00aea758 */
  lVar13 = (long)(int)param_2;
  uVar9 = FUN_00adee94(param_1,param_2);
  if ((uVar9 & 1) == 0) {
    iVar5 = 0xff;
    lVar10 = *(long *)(lVar7 + lVar13 * 0x10 + 0x340);
    iVar4 = 0xff;
    if (lVar10 != 0) goto LAB_00aea454;
  }
  else {
    iVar5 = FUN_0046da7c(*(int *)(param_1 + 0x1188) * -0x11 + 0xff,0);
    lVar3 = lVar7 + lVar13 * 0x10;
    lVar10 = *(long *)(lVar3 + 0x340);
    if (lVar10 != 0) {
      iVar4 = iVar5;
      if (iVar5 < 0xff) {
        FUN_00468b9c(uVar8,iVar5);
        lVar10 = *(long *)(lVar3 + 0x340);
                    /* try { // try from 00aea440 to 00bea447 has its CatchHandler @ 00aea750 */
      }
LAB_00aea454:
      iVar5 = iVar4;
                    /* try { // try from 00aea484 to 00bea4cf has its CatchHandler @ 00aea77c */
      FUN_00469bc4(uVar8,lVar10,
                   *(int *)((long)&(&fde_table_entry_00333a90)[lVar13 * 2].initial_loc + param_1) +
                   *(int *)((long)&(&fde_table_entry_00333a38)[lVar13].initial_loc + param_1),
                   *(int *)((long)&(&fde_table_entry_00333a90)[lVar13 * 2].data_loc + param_1) +
                   *(int *)((long)&(&fde_table_entry_00333a38)[lVar13].data_loc + param_1),0x6e,0x55
                   ,0);
      FUN_00467b20(uVar8,0xff,0xff,0xff,0xff);
    }
  }
  if ((*(uint *)(param_1 + 0x3398) & 0xfffffffe) == 2) {
    uVar6 = FUN_00a41e38((long)&DWORD_00347348 + param_1);
    uVar9 = FUN_00a41ec4((long)&DWORD_00347348 + param_1,uVar6);
    if (((uVar9 & 1) == 0) ||
       (uVar9 = FUN_00a41f9c((long)&DWORD_00347348 + param_1,param_2,1), (uVar9 & 1) != 0)) {
      lVar10 = lVar14 + (long)*(int *)((long)&DWORD_0039b97c + param_1) * 0x2c;
                    /* try { // try from 00aea500 to 00bea523 has its CatchHandler @ 00aea74c */
      pbVar2 = (byte *)(lVar10 + uVar15);
      iVar4 = CONCAT13(*(byte *)(lVar10 + 0x2b) ^ pbVar2[3],
                       CONCAT12(*(byte *)(lVar10 + 0x2a) ^ pbVar2[2],
                                CONCAT11(*(byte *)(lVar10 + 0x29) ^ pbVar2[1],
                                         *(byte *)(lVar10 + 0x28) ^ *pbVar2))) + -2;
      uVar9 = FUN_007441c8(param_1 + 0xbe0);
      if ((((uVar9 & 1) == 0) || (uVar9 = FUN_00743d50(param_1 + 0xbe0,iVar4), (uVar9 & 1) != 0)) &&
         ((uVar9 = FUN_00b09234(param_1 + 0x3d8), (uVar9 & 1) == 0 ||
          (uVar9 = FUN_00b0a8ec(param_1 + 0x3d8,iVar4), (uVar9 & 1) != 0)))) goto LAB_00aea744;
    }
    lVar10 = lVar14 + (long)*(int *)((long)&DWORD_0039b97c + param_1) * 0x2c;
    pbVar2 = (byte *)(lVar10 + uVar15);
                    /* try { // try from 00aea5a4 to 00bea5af has its CatchHandler @ 00aea740 */
                    /* try { // try from 00aea5b0 to 00bea6fb has its CatchHandler @ 00aea1c8 */
    iVar4 = CONCAT13(*(byte *)(lVar10 + 0x2b) ^ pbVar2[3],
                     CONCAT12(*(byte *)(lVar10 + 0x2a) ^ pbVar2[2],
                              CONCAT11(*(byte *)(lVar10 + 0x29) ^ pbVar2[1],
                                       *(byte *)(lVar10 + 0x28) ^ *pbVar2))) + -2;
    uVar9 = FUN_007441c8(param_1 + 0xbe0);
    if ((((uVar9 & 1) == 0) || (uVar9 = FUN_00743d50(param_1 + 0xbe0,iVar4), (uVar9 & 1) != 0)) &&
       ((uVar9 = FUN_00b09234(param_1 + 0x3d8), (uVar9 & 1) == 0 ||
        (uVar9 = FUN_00b0a8ec(param_1 + 0x3d8,iVar4), (uVar9 & 1) != 0)))) {
      iVar5 = 0xff - iVar5;
      iVar4 = (iVar5 * 0x35) / 0xff + 0xca;
      iVar1 = (iVar5 * 0x6b) / 0xff + 0x94;
      iVar5 = (iVar5 * 0x71) / 0xff + 0x8e;
    }
    else {
      iVar5 = 0xff - iVar5;
      iVar4 = (iVar5 * 0x71) / 0xff + 0x8e;
      iVar1 = (iVar5 * 0x56) / 0xff + 0xa9;
      iVar5 = (iVar5 * 0x7b) / 0xff + 0x84;
    }
    FUN_00467aec(uVar8,iVar4,iVar1,iVar5,0xff);
                    /* try { // try from 00aea6fc to 00bea6ff has its CatchHandler @ 00aea798 */
                    /* try { // try from 00aea700 to 00bea727 has its CatchHandler @ 00aea1c8 */
    FUN_00467ab0(uVar8,2);
                    /* try { // try from 00aea728 to 00bea72b has its CatchHandler @ 00aea77c */
    FUN_00467f14(uVar8,*(int *)((long)&(&fde_table_entry_00333a90)[lVar13 * 2].initial_loc + param_1
                               ) +
                       *(int *)((long)&(&fde_table_entry_00333a38)[lVar13].initial_loc + param_1),
                 *(int *)((long)&(&fde_table_entry_00333a90)[lVar13 * 2].data_loc + param_1) +
                 *(int *)((long)&(&fde_table_entry_00333a38)[lVar13].data_loc + param_1),0x6e,0x55);
                    /* try { // try from 00aea73c to 00bea73f has its CatchHandler @ 00aea758 */
                    /* catch() { ... } // from try @ 00aea5a4 with catch @ 00aea740
                       try { // try from 00aea740 to 00bea7d7 has its CatchHandler @ 00aea1c8 */
    FUN_00467ab0(uVar8,0);
  }
LAB_00aea744:
                    /* catch() { ... } // from try @ 00aea3c0 with catch @ 00aea744 */
  uVar9 = FUN_007441c8(param_1 + 0xbe0);
                    /* catch() { ... } // from try @ 00aea500 with catch @ 00aea74c */
  if ((uVar9 & 1) != 0) {
                    /* catch() { ... } // from try @ 00aea440 with catch @ 00aea750 */
                    /* catch() { ... } // from try @ 00aea3e0 with catch @ 00aea758
                       catch() { ... } // from try @ 00aea73c with catch @ 00aea758 */
    uVar6 = FUN_00744158(param_1 + 0xbe0,param_2);
    uVar9 = FUN_00743eec(param_1 + 0xbe0,uVar6);
    if ((uVar9 & 1) != 0) {
      uVar11 = *(undefined8 *)(lVar7 + 0x118);
                    /* catch() { ... } // from try @ 00aea484 with catch @ 00aea77c
                       catch() { ... } // from try @ 00aea728 with catch @ 00aea77c */
                    /* catch() { ... } // from try @ 00aea2fc with catch @ 00aea780 */
      iVar5 = *(int *)((long)&(&fde_table_entry_00333a38)[lVar13].initial_loc + param_1) +
              *(int *)((long)&(&fde_table_entry_00333a90)[lVar13 * 2].initial_loc + param_1);
                    /* catch() { ... } // from try @ 00aea224 with catch @ 00aea790 */
      iVar4 = *(int *)((long)&(&fde_table_entry_00333a38)[lVar13].data_loc + param_1) +
              *(int *)((long)&(&fde_table_entry_00333a90)[lVar13 * 2].data_loc + param_1);
      uVar12 = 0x83;
      goto LAB_00aea83c;
    }
  }
  lVar14 = lVar14 + (long)*(int *)((long)&DWORD_0039b97c + param_1) * 0x2c;
  pbVar2 = (byte *)(lVar14 + uVar15);
                    /* try { // try from 00aea7d8 to 00bea823 has its CatchHandler @ 00aea7d8
                       catch() { ... } // from try @ 00aea7d8 with catch @ 00aea7d8
                       catch() { ... } // from try @ 00aea8ac with catch @ 00aea7d8
                       catch() { ... } // from try @ 00aeabd0 with catch @ 00aea7d8
                       catch() { ... } // from try @ 00aead28 with catch @ 00aea7d8 */
  uVar15 = FUN_005c04b0(param_1 + 0x4a0,(long)*(int *)((long)&DWORD_0039b97c + param_1),
                        CONCAT13(*(byte *)(lVar14 + 0x2b) ^ pbVar2[3],
                                 CONCAT12(*(byte *)(lVar14 + 0x2a) ^ pbVar2[2],
                                          CONCAT11(*(byte *)(lVar14 + 0x29) ^ pbVar2[1],
                                                   *(byte *)(lVar14 + 0x28) ^ *pbVar2))) + -2);
  if ((uVar15 & 1) == 0) {
                    /* try { // try from 00aea858 to 00bea86b has its CatchHandler @ 00aead84 */
    return;
  }
  uVar11 = *(undefined8 *)(lVar7 + 0x118);
                    /* try { // try from 00aea824 to 00bea82b has its CatchHandler @ 00aeada0 */
  iVar5 = *(int *)((long)&(&fde_table_entry_00333a38)[lVar13].initial_loc + param_1) +
          *(int *)((long)&(&fde_table_entry_00333a90)[lVar13 * 2].initial_loc + param_1);
  iVar4 = *(int *)((long)&(&fde_table_entry_00333a38)[lVar13].data_loc + param_1) +
          *(int *)((long)&(&fde_table_entry_00333a90)[lVar13 * 2].data_loc + param_1);
  uVar12 = 0x8e;
LAB_00aea83c:
                    /* catch() { ... } // from try @ 00aea268 with catch @ 00aea798
                       catch() { ... } // from try @ 00aea6fc with catch @ 00aea798 */
  FUN_00468f48(uVar8,uVar11,iVar5 + 2,iVar4 + 2,uVar12);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aea2fc"></a> `00aea2fc` | `fd 7b ba a9` | stp x29,x30,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00aea300"></a> `00aea300` | `fc 6f 01 a9` | stp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aea304"></a> `00aea304` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aea308"></a> `00aea308` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aea30c"></a> `00aea30c` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aea310"></a> `00aea310` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aea314"></a> `00aea314` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aea318"></a> `00aea318` | `c8 0d 00 d0` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-00aea31c"></a> `00aea31c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00aea320"></a> `00aea320` | `13 51 87 52` | mov w19,#0x3a88 | `FALL_THROUGH`
<a id="insn-00aea324"></a> `00aea324` | `00 bd 42 f9` | ldr x0,[x8, #0x578] | `FALL_THROUGH`
<a id="insn-00aea328"></a> `00aea328` | `f6 03 01 2a` | mov w22,w1 | `FALL_THROUGH`
<a id="insn-00aea32c"></a> `00aea32c` | `73 06 a0 72` | movk w19,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00aea330"></a> `00aea330` | `20 01 00 b4` | cbz x0,0x00aea354 | `CONDITIONAL_JUMP`
<a id="insn-00aea334"></a> `00aea334` | `c1 0b 00 f0` | adrp x1,0xc65000 | `FALL_THROUGH`
<a id="insn-00aea338"></a> `00aea338` | `21 60 29 91` | add x1,x1,#0xa58 | `FALL_THROUGH`
<a id="insn-00aea33c"></a> `00aea33c` | `02 0d 00 f0` | adrp x2,0xc8d000 | `FALL_THROUGH`
<a id="insn-00aea340"></a> `00aea340` | `42 40 15 91` | add x2,x2,#0x550 | `FALL_THROUGH`
<a id="insn-00aea344"></a> `00aea344` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00aea348"></a> `00aea348` | `b2 b7 05 94` | bl 0x00c58210 | `UNCONDITIONAL_CALL`
<a id="insn-00aea34c"></a> `00aea34c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aea350"></a> `00aea350` | `02 00 00 14` | b 0x00aea358 | `UNCONDITIONAL_JUMP`
<a id="insn-00aea354"></a> `00aea354` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00aea358"></a> `00aea358` | `32 f5 e5 97` | bl 0x00467820 | `UNCONDITIONAL_CALL`
<a id="insn-00aea35c"></a> `00aea35c` | `a8 6a 73 b8` | ldr w8,[x21, x19, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aea360"></a> `00aea360` | `08 05 00 51` | sub w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aea364"></a> `00aea364` | `1f 01 16 6b` | cmp w8,w22 | `FALL_THROUGH`
<a id="insn-00aea368"></a> `00aea368` | `80 27 00 54` | b.eq 0x00aea858 | `CONDITIONAL_JUMP`
<a id="insn-00aea36c"></a> `00aea36c` | `88 2f 97 52` | mov w8,#0xb97c | `FALL_THROUGH`
<a id="insn-00aea370"></a> `00aea370` | `09 b7 98 52` | mov w9,#0xc5b8 | `FALL_THROUGH`
<a id="insn-00aea374"></a> `00aea374` | `8a 05 80 52` | mov w10,#0x2c | `FALL_THROUGH`
<a id="insn-00aea378"></a> `00aea378` | `28 07 a0 72` | movk w8,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00aea37c"></a> `00aea37c` | `bb 02 09 8b` | add x27,x21,x9 | `FALL_THROUGH`
<a id="insn-00aea380"></a> `00aea380` | `d9 7e 7e 93` | sbfiz x25,x22,#0x2,#0x20 | `FALL_THROUGH`
<a id="insn-00aea384"></a> `00aea384` | `a8 6a a8 b8` | ldrsw x8,[x21, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aea388"></a> `00aea388` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00aea38c"></a> `00aea38c` | `08 6d 2a 9b` | smaddl x8,w8,w10,x27 | `FALL_THROUGH`
<a id="insn-00aea390"></a> `00aea390` | `09 01 19 8b` | add x9,x8,x25 | `FALL_THROUGH`
<a id="insn-00aea394"></a> `00aea394` | `0b a9 40 39` | ldrb w11,[x8, #0x2a] | `FALL_THROUGH`
<a id="insn-00aea398"></a> `00aea398` | `0c ad 40 39` | ldrb w12,[x8, #0x2b] | `FALL_THROUGH`
<a id="insn-00aea39c"></a> `00aea39c` | `2a 09 40 39` | ldrb w10,[x9, #0x2] | `FALL_THROUGH`
<a id="insn-00aea3a0"></a> `00aea3a0` | `2d 05 40 39` | ldrb w13,[x9, #0x1] | `FALL_THROUGH`
<a id="insn-00aea3a4"></a> `00aea3a4` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00aea3a8"></a> `00aea3a8` | `2b 0d 40 39` | ldrb w11,[x9, #0x3] | `FALL_THROUGH`
<a id="insn-00aea3ac"></a> `00aea3ac` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00aea3b0"></a> `00aea3b0` | `4a 3d 10 53` | lsl w10,w10,#0x10 | `FALL_THROUGH`
<a id="insn-00aea3b4"></a> `00aea3b4` | `8b 01 0b 4a` | eor w11,w12,w11 | `FALL_THROUGH`
<a id="insn-00aea3b8"></a> `00aea3b8` | `0c a5 40 39` | ldrb w12,[x8, #0x29] | `FALL_THROUGH`
<a id="insn-00aea3bc"></a> `00aea3bc` | `08 a1 40 39` | ldrb w8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aea3c0"></a> `00aea3c0` | `4a 61 0b 2a` | orr w10,w10,w11, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00aea3c4"></a> `00aea3c4` | `8b 01 0d 4a` | eor w11,w12,w13 | `FALL_THROUGH`
<a id="insn-00aea3c8"></a> `00aea3c8` | `08 01 09 4a` | eor w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00aea3cc"></a> `00aea3cc` | `4a 21 0b 2a` | orr w10,w10,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00aea3d0"></a> `00aea3d0` | `48 01 08 2a` | orr w8,w10,w8 | `FALL_THROUGH`
<a id="insn-00aea3d4"></a> `00aea3d4` | `1f 05 00 31` | cmn w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aea3d8"></a> `00aea3d8` | `00 24 00 54` | b.eq 0x00aea858 | `CONDITIONAL_JUMP`
<a id="insn-00aea3dc"></a> `00aea3dc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aea3e0"></a> `00aea3e0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00aea3e4"></a> `00aea3e4` | `e1 03 16 2a` | mov w1,w22 | `FALL_THROUGH`
<a id="insn-00aea3e8"></a> `00aea3e8` | `d7 7e 40 93` | sxtw x23,w22 | `FALL_THROUGH`
<a id="insn-00aea3ec"></a> `00aea3ec` | `aa d2 ff 97` | bl 0x00adee94 | `UNCONDITIONAL_CALL`
<a id="insn-00aea3f0"></a> `00aea3f0` | `bc 0e 17 8b` | add x28,x21,x23, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00aea3f4"></a> `00aea3f4` | `ba 12 17 8b` | add x26,x21,x23, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00aea3f8"></a> `00aea3f8` | `60 02 00 36` | tbz w0,#0x0,0x00aea444 | `CONDITIONAL_JUMP`
<a id="insn-00aea3fc"></a> `00aea3fc` | `a8 8a 51 b9` | ldr w8,[x21, #0x1188] | `FALL_THROUGH`
<a id="insn-00aea400"></a> `00aea400` | `e9 1f 80 52` | mov w9,#0xff | `FALL_THROUGH`
<a id="insn-00aea404"></a> `00aea404` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aea408"></a> `00aea408` | `08 11 08 0b` | add w8,w8,w8, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00aea40c"></a> `00aea40c` | `20 01 08 4b` | sub w0,w9,w8 | `FALL_THROUGH`
<a id="insn-00aea410"></a> `00aea410` | `9b 0d e6 97` | bl 0x0046da7c | `UNCONDITIONAL_CALL`
<a id="insn-00aea414"></a> `00aea414` | `88 12 17 8b` | add x8,x20,x23, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00aea418"></a> `00aea418` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00aea41c"></a> `00aea41c` | `01 a1 41 f9` | ldr x1,[x8, #0x340] | `FALL_THROUGH`
<a id="insn-00aea420"></a> `00aea420` | `01 04 00 b4` | cbz x1,0x00aea4a0 | `CONDITIONAL_JUMP`
<a id="insn-00aea424"></a> `00aea424` | `ff fa 03 71` | cmp w23,#0xfe | `FALL_THROUGH`
<a id="insn-00aea428"></a> `00aea428` | `6c 01 00 54` | b.gt 0x00aea454 | `CONDITIONAL_JUMP`
<a id="insn-00aea42c"></a> `00aea42c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aea430"></a> `00aea430` | `e1 03 17 2a` | mov w1,w23 | `FALL_THROUGH`
<a id="insn-00aea434"></a> `00aea434` | `18 01 0d 91` | add x24,x8,#0x340 | `FALL_THROUGH`
<a id="insn-00aea438"></a> `00aea438` | `d9 f9 e5 97` | bl 0x00468b9c | `UNCONDITIONAL_CALL`
<a id="insn-00aea43c"></a> `00aea43c` | `01 03 40 f9` | ldr x1,[x24] | `FALL_THROUGH`
<a id="insn-00aea440"></a> `00aea440` | `05 00 00 14` | b 0x00aea454 | `UNCONDITIONAL_JUMP`
<a id="insn-00aea444"></a> `00aea444` | `88 12 17 8b` | add x8,x20,x23, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00aea448"></a> `00aea448` | `f7 1f 80 52` | mov w23,#0xff | `FALL_THROUGH`
<a id="insn-00aea44c"></a> `00aea44c` | `01 a1 41 f9` | ldr x1,[x8, #0x340] | `FALL_THROUGH`
<a id="insn-00aea450"></a> `00aea450` | `81 02 00 b4` | cbz x1,0x00aea4a0 | `CONDITIONAL_JUMP`
<a id="insn-00aea454"></a> `00aea454` | `88 cf 4c 91` | add x8,x28,#0x333, LSL #12 | `FALL_THROUGH`
<a id="insn-00aea458"></a> `00aea458` | `49 cf 4c 91` | add x9,x26,#0x333, LSL #12 | `FALL_THROUGH`
<a id="insn-00aea45c"></a> `00aea45c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aea460"></a> `00aea460` | `08 e1 28 91` | add x8,x8,#0xa38 | `FALL_THROUGH`
<a id="insn-00aea464"></a> `00aea464` | `29 41 2a 91` | add x9,x9,#0xa90 | `FALL_THROUGH`
<a id="insn-00aea468"></a> `00aea468` | `c4 0d 80 52` | mov w4,#0x6e | `FALL_THROUGH`
<a id="insn-00aea46c"></a> `00aea46c` | `0a 21 40 29` | ldp w10,w8,[x8] | `FALL_THROUGH`
<a id="insn-00aea470"></a> `00aea470` | `2b 25 40 29` | ldp w11,w9,[x9] | `FALL_THROUGH`
<a id="insn-00aea474"></a> `00aea474` | `a5 0a 80 52` | mov w5,#0x55 | `FALL_THROUGH`
<a id="insn-00aea478"></a> `00aea478` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-00aea47c"></a> `00aea47c` | `62 01 0a 0b` | add w2,w11,w10 | `FALL_THROUGH`
<a id="insn-00aea480"></a> `00aea480` | `23 01 08 0b` | add w3,w9,w8 | `FALL_THROUGH`
<a id="insn-00aea484"></a> `00aea484` | `d0 fd e5 97` | bl 0x00469bc4 | `UNCONDITIONAL_CALL`
<a id="insn-00aea488"></a> `00aea488` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aea48c"></a> `00aea48c` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-00aea490"></a> `00aea490` | `e2 1f 80 52` | mov w2,#0xff | `FALL_THROUGH`
<a id="insn-00aea494"></a> `00aea494` | `e3 1f 80 52` | mov w3,#0xff | `FALL_THROUGH`
<a id="insn-00aea498"></a> `00aea498` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-00aea49c"></a> `00aea49c` | `a1 f5 e5 97` | bl 0x00467b20 | `UNCONDITIONAL_CALL`
<a id="insn-00aea4a0"></a> `00aea4a0` | `a8 9a 73 b9` | ldr w8,[x21, #0x3398] | `FALL_THROUGH`
<a id="insn-00aea4a4"></a> `00aea4a4` | `08 79 1f 12` | and w8,w8,#0xfffffffe | `FALL_THROUGH`
<a id="insn-00aea4a8"></a> `00aea4a8` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00aea4ac"></a> `00aea4ac` | `c1 14 00 54` | b.ne 0x00aea744 | `CONDITIONAL_JUMP`
<a id="insn-00aea4b0"></a> `00aea4b0` | `18 69 8e 52` | mov w24,#0x7348 | `FALL_THROUGH`
<a id="insn-00aea4b4"></a> `00aea4b4` | `98 06 a0 72` | movk w24,#0x34, LSL #16 | `FALL_THROUGH`
<a id="insn-00aea4b8"></a> `00aea4b8` | `a0 02 18 8b` | add x0,x21,x24 | `FALL_THROUGH`
<a id="insn-00aea4bc"></a> `00aea4bc` | `5f 5e fd 97` | bl 0x00a41e38 | `UNCONDITIONAL_CALL`
<a id="insn-00aea4c0"></a> `00aea4c0` | `e1 03 00 2a` | mov w1,w0 | `FALL_THROUGH`
<a id="insn-00aea4c4"></a> `00aea4c4` | `a0 02 18 8b` | add x0,x21,x24 | `FALL_THROUGH`
<a id="insn-00aea4c8"></a> `00aea4c8` | `7f 5e fd 97` | bl 0x00a41ec4 | `UNCONDITIONAL_CALL`
<a id="insn-00aea4cc"></a> `00aea4cc` | `c0 00 00 36` | tbz w0,#0x0,0x00aea4e4 | `CONDITIONAL_JUMP`
<a id="insn-00aea4d0"></a> `00aea4d0` | `a0 02 18 8b` | add x0,x21,x24 | `FALL_THROUGH`
<a id="insn-00aea4d4"></a> `00aea4d4` | `e1 03 16 2a` | mov w1,w22 | `FALL_THROUGH`
<a id="insn-00aea4d8"></a> `00aea4d8` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00aea4dc"></a> `00aea4dc` | `b0 5e fd 97` | bl 0x00a41f9c | `UNCONDITIONAL_CALL`
<a id="insn-00aea4e0"></a> `00aea4e0` | `c0 04 00 36` | tbz w0,#0x0,0x00aea578 | `CONDITIONAL_JUMP`
<a id="insn-00aea4e4"></a> `00aea4e4` | `88 2f 97 52` | mov w8,#0xb97c | `FALL_THROUGH`
<a id="insn-00aea4e8"></a> `00aea4e8` | `89 05 80 52` | mov w9,#0x2c | `FALL_THROUGH`
<a id="insn-00aea4ec"></a> `00aea4ec` | `a0 82 2f 91` | add x0,x21,#0xbe0 | `FALL_THROUGH`
<a id="insn-00aea4f0"></a> `00aea4f0` | `28 07 a0 72` | movk w8,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00aea4f4"></a> `00aea4f4` | `a8 6a a8 b8` | ldrsw x8,[x21, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aea4f8"></a> `00aea4f8` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00aea4fc"></a> `00aea4fc` | `08 6d 29 9b` | smaddl x8,w8,w9,x27 | `FALL_THROUGH`
<a id="insn-00aea500"></a> `00aea500` | `09 01 19 8b` | add x9,x8,x25 | `FALL_THROUGH`
<a id="insn-00aea504"></a> `00aea504` | `0a a1 40 39` | ldrb w10,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aea508"></a> `00aea508` | `0c a5 40 39` | ldrb w12,[x8, #0x29] | `FALL_THROUGH`
<a id="insn-00aea50c"></a> `00aea50c` | `2b 01 40 39` | ldrb w11,[x9] | `FALL_THROUGH`
<a id="insn-00aea510"></a> `00aea510` | `2d 05 40 39` | ldrb w13,[x9, #0x1] | `FALL_THROUGH`
<a id="insn-00aea514"></a> `00aea514` | `4a 01 0b 4a` | eor w10,w10,w11 | `FALL_THROUGH`
<a id="insn-00aea518"></a> `00aea518` | `8b 01 0d 4a` | eor w11,w12,w13 | `FALL_THROUGH`
<a id="insn-00aea51c"></a> `00aea51c` | `2c 09 40 39` | ldrb w12,[x9, #0x2] | `FALL_THROUGH`
<a id="insn-00aea520"></a> `00aea520` | `0d a9 40 39` | ldrb w13,[x8, #0x2a] | `FALL_THROUGH`
<a id="insn-00aea524"></a> `00aea524` | `4a 21 0b 2a` | orr w10,w10,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00aea528"></a> `00aea528` | `29 0d 40 39` | ldrb w9,[x9, #0x3] | `FALL_THROUGH`
<a id="insn-00aea52c"></a> `00aea52c` | `08 ad 40 39` | ldrb w8,[x8, #0x2b] | `FALL_THROUGH`
<a id="insn-00aea530"></a> `00aea530` | `ab 01 0c 4a` | eor w11,w13,w12 | `FALL_THROUGH`
<a id="insn-00aea534"></a> `00aea534` | `4a 41 0b 2a` | orr w10,w10,w11, LSL #0x10 | `FALL_THROUGH`
<a id="insn-00aea538"></a> `00aea538` | `08 01 09 4a` | eor w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00aea53c"></a> `00aea53c` | `48 61 08 2a` | orr w8,w10,w8, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00aea540"></a> `00aea540` | `18 09 00 51` | sub w24,w8,#0x2 | `FALL_THROUGH`
<a id="insn-00aea544"></a> `00aea544` | `21 67 f1 97` | bl 0x007441c8 | `UNCONDITIONAL_CALL`
<a id="insn-00aea548"></a> `00aea548` | `a0 00 00 36` | tbz w0,#0x0,0x00aea55c | `CONDITIONAL_JUMP`
<a id="insn-00aea54c"></a> `00aea54c` | `a0 82 2f 91` | add x0,x21,#0xbe0 | `FALL_THROUGH`
<a id="insn-00aea550"></a> `00aea550` | `e1 03 18 2a` | mov w1,w24 | `FALL_THROUGH`
<a id="insn-00aea554"></a> `00aea554` | `ff 65 f1 97` | bl 0x00743d50 | `UNCONDITIONAL_CALL`
<a id="insn-00aea558"></a> `00aea558` | `00 01 00 36` | tbz w0,#0x0,0x00aea578 | `CONDITIONAL_JUMP`
<a id="insn-00aea55c"></a> `00aea55c` | `a0 62 0f 91` | add x0,x21,#0x3d8 | `FALL_THROUGH`
<a id="insn-00aea560"></a> `00aea560` | `35 7b 00 94` | bl 0x00b09234 | `UNCONDITIONAL_CALL`
<a id="insn-00aea564"></a> `00aea564` | `00 0f 00 36` | tbz w0,#0x0,0x00aea744 | `CONDITIONAL_JUMP`
<a id="insn-00aea568"></a> `00aea568` | `a0 62 0f 91` | add x0,x21,#0x3d8 | `FALL_THROUGH`
<a id="insn-00aea56c"></a> `00aea56c` | `e1 03 18 2a` | mov w1,w24 | `FALL_THROUGH`
<a id="insn-00aea570"></a> `00aea570` | `df 80 00 94` | bl 0x00b0a8ec | `UNCONDITIONAL_CALL`
<a id="insn-00aea574"></a> `00aea574` | `80 0e 00 37` | tbnz w0,#0x0,0x00aea744 | `CONDITIONAL_JUMP`
<a id="insn-00aea578"></a> `00aea578` | `88 2f 97 52` | mov w8,#0xb97c | `FALL_THROUGH`
<a id="insn-00aea57c"></a> `00aea57c` | `89 05 80 52` | mov w9,#0x2c | `FALL_THROUGH`
<a id="insn-00aea580"></a> `00aea580` | `a0 82 2f 91` | add x0,x21,#0xbe0 | `FALL_THROUGH`
<a id="insn-00aea584"></a> `00aea584` | `28 07 a0 72` | movk w8,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00aea588"></a> `00aea588` | `a8 6a a8 b8` | ldrsw x8,[x21, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aea58c"></a> `00aea58c` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00aea590"></a> `00aea590` | `08 6d 29 9b` | smaddl x8,w8,w9,x27 | `FALL_THROUGH`
<a id="insn-00aea594"></a> `00aea594` | `09 01 19 8b` | add x9,x8,x25 | `FALL_THROUGH`
<a id="insn-00aea598"></a> `00aea598` | `0a a1 40 39` | ldrb w10,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aea59c"></a> `00aea59c` | `0c a5 40 39` | ldrb w12,[x8, #0x29] | `FALL_THROUGH`
<a id="insn-00aea5a0"></a> `00aea5a0` | `2b 01 40 39` | ldrb w11,[x9] | `FALL_THROUGH`
<a id="insn-00aea5a4"></a> `00aea5a4` | `2d 05 40 39` | ldrb w13,[x9, #0x1] | `FALL_THROUGH`
<a id="insn-00aea5a8"></a> `00aea5a8` | `4a 01 0b 4a` | eor w10,w10,w11 | `FALL_THROUGH`
<a id="insn-00aea5ac"></a> `00aea5ac` | `8b 01 0d 4a` | eor w11,w12,w13 | `FALL_THROUGH`
<a id="insn-00aea5b0"></a> `00aea5b0` | `2c 09 40 39` | ldrb w12,[x9, #0x2] | `FALL_THROUGH`
<a id="insn-00aea5b4"></a> `00aea5b4` | `0d a9 40 39` | ldrb w13,[x8, #0x2a] | `FALL_THROUGH`
<a id="insn-00aea5b8"></a> `00aea5b8` | `4a 21 0b 2a` | orr w10,w10,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00aea5bc"></a> `00aea5bc` | `29 0d 40 39` | ldrb w9,[x9, #0x3] | `FALL_THROUGH`
<a id="insn-00aea5c0"></a> `00aea5c0` | `08 ad 40 39` | ldrb w8,[x8, #0x2b] | `FALL_THROUGH`
<a id="insn-00aea5c4"></a> `00aea5c4` | `ab 01 0c 4a` | eor w11,w13,w12 | `FALL_THROUGH`
<a id="insn-00aea5c8"></a> `00aea5c8` | `4a 41 0b 2a` | orr w10,w10,w11, LSL #0x10 | `FALL_THROUGH`
<a id="insn-00aea5cc"></a> `00aea5cc` | `08 01 09 4a` | eor w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00aea5d0"></a> `00aea5d0` | `48 61 08 2a` | orr w8,w10,w8, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00aea5d4"></a> `00aea5d4` | `18 09 00 51` | sub w24,w8,#0x2 | `FALL_THROUGH`
<a id="insn-00aea5d8"></a> `00aea5d8` | `fc 66 f1 97` | bl 0x007441c8 | `UNCONDITIONAL_CALL`
<a id="insn-00aea5dc"></a> `00aea5dc` | `a0 00 00 36` | tbz w0,#0x0,0x00aea5f0 | `CONDITIONAL_JUMP`
<a id="insn-00aea5e0"></a> `00aea5e0` | `a0 82 2f 91` | add x0,x21,#0xbe0 | `FALL_THROUGH`
<a id="insn-00aea5e4"></a> `00aea5e4` | `e1 03 18 2a` | mov w1,w24 | `FALL_THROUGH`
<a id="insn-00aea5e8"></a> `00aea5e8` | `da 65 f1 97` | bl 0x00743d50 | `UNCONDITIONAL_CALL`
<a id="insn-00aea5ec"></a> `00aea5ec` | `a0 04 00 36` | tbz w0,#0x0,0x00aea680 | `CONDITIONAL_JUMP`
<a id="insn-00aea5f0"></a> `00aea5f0` | `a0 62 0f 91` | add x0,x21,#0x3d8 | `FALL_THROUGH`
<a id="insn-00aea5f4"></a> `00aea5f4` | `10 7b 00 94` | bl 0x00b09234 | `UNCONDITIONAL_CALL`
<a id="insn-00aea5f8"></a> `00aea5f8` | `a0 00 00 36` | tbz w0,#0x0,0x00aea60c | `CONDITIONAL_JUMP`
<a id="insn-00aea5fc"></a> `00aea5fc` | `a0 62 0f 91` | add x0,x21,#0x3d8 | `FALL_THROUGH`
<a id="insn-00aea600"></a> `00aea600` | `e1 03 18 2a` | mov w1,w24 | `FALL_THROUGH`
<a id="insn-00aea604"></a> `00aea604` | `ba 80 00 94` | bl 0x00b0a8ec | `UNCONDITIONAL_CALL`
<a id="insn-00aea608"></a> `00aea608` | `c0 03 00 36` | tbz w0,#0x0,0x00aea680 | `CONDITIONAL_JUMP`
<a id="insn-00aea60c"></a> `00aea60c` | `e8 1f 80 52` | mov w8,#0xff | `FALL_THROUGH`
<a id="insn-00aea610"></a> `00aea610` | `a9 06 80 52` | mov w9,#0x35 | `FALL_THROUGH`
<a id="insn-00aea614"></a> `00aea614` | `6a 0d 80 52` | mov w10,#0x6b | `FALL_THROUGH`
<a id="insn-00aea618"></a> `00aea618` | `08 01 17 4b` | sub w8,w8,w23 | `FALL_THROUGH`
<a id="insn-00aea61c"></a> `00aea61c` | `2b 0e 80 52` | mov w11,#0x71 | `FALL_THROUGH`
<a id="insn-00aea620"></a> `00aea620` | `2c 10 90 52` | mov w12,#0x8081 | `FALL_THROUGH`
<a id="insn-00aea624"></a> `00aea624` | `09 7d 09 1b` | mul w9,w8,w9 | `FALL_THROUGH`
<a id="insn-00aea628"></a> `00aea628` | `0c 10 b0 72` | movk w12,#0x8080, LSL #16 | `FALL_THROUGH`
<a id="insn-00aea62c"></a> `00aea62c` | `0a 7d 0a 1b` | mul w10,w8,w10 | `FALL_THROUGH`
<a id="insn-00aea630"></a> `00aea630` | `08 7d 0b 1b` | mul w8,w8,w11 | `FALL_THROUGH`
<a id="insn-00aea634"></a> `00aea634` | `2b 7d 2c 9b` | smull x11,w9,w12 | `FALL_THROUGH`
<a id="insn-00aea638"></a> `00aea638` | `4d 7d 2c 9b` | smull x13,w10,w12 | `FALL_THROUGH`
<a id="insn-00aea63c"></a> `00aea63c` | `0c 7d 2c 9b` | smull x12,w8,w12 | `FALL_THROUGH`
<a id="insn-00aea640"></a> `00aea640` | `6b fd 60 d3` | lsr x11,x11,#0x20 | `FALL_THROUGH`
<a id="insn-00aea644"></a> `00aea644` | `ad fd 60 d3` | lsr x13,x13,#0x20 | `FALL_THROUGH`
<a id="insn-00aea648"></a> `00aea648` | `8c fd 60 d3` | lsr x12,x12,#0x20 | `FALL_THROUGH`
<a id="insn-00aea64c"></a> `00aea64c` | `69 01 09 0b` | add w9,w11,w9 | `FALL_THROUGH`
<a id="insn-00aea650"></a> `00aea650` | `aa 01 0a 0b` | add w10,w13,w10 | `FALL_THROUGH`
<a id="insn-00aea654"></a> `00aea654` | `2b 7d 07 13` | asr w11,w9,#0x7 | `FALL_THROUGH`
<a id="insn-00aea658"></a> `00aea658` | `88 01 08 0b` | add w8,w12,w8 | `FALL_THROUGH`
<a id="insn-00aea65c"></a> `00aea65c` | `4c 7d 07 13` | asr w12,w10,#0x7 | `FALL_THROUGH`
<a id="insn-00aea660"></a> `00aea660` | `0d 7d 07 13` | asr w13,w8,#0x7 | `FALL_THROUGH`
<a id="insn-00aea664"></a> `00aea664` | `69 7d 49 0b` | add w9,w11,w9, LSR #0x1f | `FALL_THROUGH`
<a id="insn-00aea668"></a> `00aea668` | `8a 7d 4a 0b` | add w10,w12,w10, LSR #0x1f | `FALL_THROUGH`
<a id="insn-00aea66c"></a> `00aea66c` | `a8 7d 48 0b` | add w8,w13,w8, LSR #0x1f | `FALL_THROUGH`
<a id="insn-00aea670"></a> `00aea670` | `21 29 03 11` | add w1,w9,#0xca | `FALL_THROUGH`
<a id="insn-00aea674"></a> `00aea674` | `42 51 02 11` | add w2,w10,#0x94 | `FALL_THROUGH`
<a id="insn-00aea678"></a> `00aea678` | `03 39 02 11` | add w3,w8,#0x8e | `FALL_THROUGH`
<a id="insn-00aea67c"></a> `00aea67c` | `1d 00 00 14` | b 0x00aea6f0 | `UNCONDITIONAL_JUMP`
<a id="insn-00aea680"></a> `00aea680` | `e8 1f 80 52` | mov w8,#0xff | `FALL_THROUGH`
<a id="insn-00aea684"></a> `00aea684` | `29 0e 80 52` | mov w9,#0x71 | `FALL_THROUGH`
<a id="insn-00aea688"></a> `00aea688` | `ca 0a 80 52` | mov w10,#0x56 | `FALL_THROUGH`
<a id="insn-00aea68c"></a> `00aea68c` | `08 01 17 4b` | sub w8,w8,w23 | `FALL_THROUGH`
<a id="insn-00aea690"></a> `00aea690` | `6b 0f 80 52` | mov w11,#0x7b | `FALL_THROUGH`
<a id="insn-00aea694"></a> `00aea694` | `2c 10 90 52` | mov w12,#0x8081 | `FALL_THROUGH`
<a id="insn-00aea698"></a> `00aea698` | `09 7d 09 1b` | mul w9,w8,w9 | `FALL_THROUGH`
<a id="insn-00aea69c"></a> `00aea69c` | `0c 10 b0 72` | movk w12,#0x8080, LSL #16 | `FALL_THROUGH`
<a id="insn-00aea6a0"></a> `00aea6a0` | `0a 7d 0a 1b` | mul w10,w8,w10 | `FALL_THROUGH`
<a id="insn-00aea6a4"></a> `00aea6a4` | `08 7d 0b 1b` | mul w8,w8,w11 | `FALL_THROUGH`
<a id="insn-00aea6a8"></a> `00aea6a8` | `2b 7d 2c 9b` | smull x11,w9,w12 | `FALL_THROUGH`
<a id="insn-00aea6ac"></a> `00aea6ac` | `4d 7d 2c 9b` | smull x13,w10,w12 | `FALL_THROUGH`
<a id="insn-00aea6b0"></a> `00aea6b0` | `0c 7d 2c 9b` | smull x12,w8,w12 | `FALL_THROUGH`
<a id="insn-00aea6b4"></a> `00aea6b4` | `6b fd 60 d3` | lsr x11,x11,#0x20 | `FALL_THROUGH`
<a id="insn-00aea6b8"></a> `00aea6b8` | `ad fd 60 d3` | lsr x13,x13,#0x20 | `FALL_THROUGH`
<a id="insn-00aea6bc"></a> `00aea6bc` | `8c fd 60 d3` | lsr x12,x12,#0x20 | `FALL_THROUGH`
<a id="insn-00aea6c0"></a> `00aea6c0` | `69 01 09 0b` | add w9,w11,w9 | `FALL_THROUGH`
<a id="insn-00aea6c4"></a> `00aea6c4` | `aa 01 0a 0b` | add w10,w13,w10 | `FALL_THROUGH`
<a id="insn-00aea6c8"></a> `00aea6c8` | `2b 7d 07 13` | asr w11,w9,#0x7 | `FALL_THROUGH`
<a id="insn-00aea6cc"></a> `00aea6cc` | `88 01 08 0b` | add w8,w12,w8 | `FALL_THROUGH`
<a id="insn-00aea6d0"></a> `00aea6d0` | `4c 7d 07 13` | asr w12,w10,#0x7 | `FALL_THROUGH`
<a id="insn-00aea6d4"></a> `00aea6d4` | `0d 7d 07 13` | asr w13,w8,#0x7 | `FALL_THROUGH`
<a id="insn-00aea6d8"></a> `00aea6d8` | `69 7d 49 0b` | add w9,w11,w9, LSR #0x1f | `FALL_THROUGH`
<a id="insn-00aea6dc"></a> `00aea6dc` | `8a 7d 4a 0b` | add w10,w12,w10, LSR #0x1f | `FALL_THROUGH`
<a id="insn-00aea6e0"></a> `00aea6e0` | `a8 7d 48 0b` | add w8,w13,w8, LSR #0x1f | `FALL_THROUGH`
<a id="insn-00aea6e4"></a> `00aea6e4` | `21 39 02 11` | add w1,w9,#0x8e | `FALL_THROUGH`
<a id="insn-00aea6e8"></a> `00aea6e8` | `42 a5 02 11` | add w2,w10,#0xa9 | `FALL_THROUGH`
<a id="insn-00aea6ec"></a> `00aea6ec` | `03 11 02 11` | add w3,w8,#0x84 | `FALL_THROUGH`
<a id="insn-00aea6f0"></a> `00aea6f0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aea6f4"></a> `00aea6f4` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-00aea6f8"></a> `00aea6f8` | `fd f4 e5 97` | bl 0x00467aec | `UNCONDITIONAL_CALL`
<a id="insn-00aea6fc"></a> `00aea6fc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aea700"></a> `00aea700` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-00aea704"></a> `00aea704` | `eb f4 e5 97` | bl 0x00467ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00aea708"></a> `00aea708` | `88 cf 4c 91` | add x8,x28,#0x333, LSL #12 | `FALL_THROUGH`
<a id="insn-00aea70c"></a> `00aea70c` | `49 cf 4c 91` | add x9,x26,#0x333, LSL #12 | `FALL_THROUGH`
<a id="insn-00aea710"></a> `00aea710` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aea714"></a> `00aea714` | `08 e1 28 91` | add x8,x8,#0xa38 | `FALL_THROUGH`
<a id="insn-00aea718"></a> `00aea718` | `29 41 2a 91` | add x9,x9,#0xa90 | `FALL_THROUGH`
<a id="insn-00aea71c"></a> `00aea71c` | `c3 0d 80 52` | mov w3,#0x6e | `FALL_THROUGH`
<a id="insn-00aea720"></a> `00aea720` | `0a 21 40 29` | ldp w10,w8,[x8] | `FALL_THROUGH`
<a id="insn-00aea724"></a> `00aea724` | `2b 25 40 29` | ldp w11,w9,[x9] | `FALL_THROUGH`
<a id="insn-00aea728"></a> `00aea728` | `a4 0a 80 52` | mov w4,#0x55 | `FALL_THROUGH`
<a id="insn-00aea72c"></a> `00aea72c` | `61 01 0a 0b` | add w1,w11,w10 | `FALL_THROUGH`
<a id="insn-00aea730"></a> `00aea730` | `22 01 08 0b` | add w2,w9,w8 | `FALL_THROUGH`
<a id="insn-00aea734"></a> `00aea734` | `f8 f5 e5 97` | bl 0x00467f14 | `UNCONDITIONAL_CALL`
<a id="insn-00aea738"></a> `00aea738` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aea73c"></a> `00aea73c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aea740"></a> `00aea740` | `dc f4 e5 97` | bl 0x00467ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00aea744"></a> `00aea744` | `a0 82 2f 91` | add x0,x21,#0xbe0 | `FALL_THROUGH`
<a id="insn-00aea748"></a> `00aea748` | `a0 66 f1 97` | bl 0x007441c8 | `UNCONDITIONAL_CALL`
<a id="insn-00aea74c"></a> `00aea74c` | `c0 02 00 36` | tbz w0,#0x0,0x00aea7a4 | `CONDITIONAL_JUMP`
<a id="insn-00aea750"></a> `00aea750` | `a0 82 2f 91` | add x0,x21,#0xbe0 | `FALL_THROUGH`
<a id="insn-00aea754"></a> `00aea754` | `e1 03 16 2a` | mov w1,w22 | `FALL_THROUGH`
<a id="insn-00aea758"></a> `00aea758` | `80 66 f1 97` | bl 0x00744158 | `UNCONDITIONAL_CALL`
<a id="insn-00aea75c"></a> `00aea75c` | `e1 03 00 2a` | mov w1,w0 | `FALL_THROUGH`
<a id="insn-00aea760"></a> `00aea760` | `a0 82 2f 91` | add x0,x21,#0xbe0 | `FALL_THROUGH`
<a id="insn-00aea764"></a> `00aea764` | `e2 65 f1 97` | bl 0x00743eec | `UNCONDITIONAL_CALL`
<a id="insn-00aea768"></a> `00aea768` | `e0 01 00 36` | tbz w0,#0x0,0x00aea7a4 | `CONDITIONAL_JUMP`
<a id="insn-00aea76c"></a> `00aea76c` | `88 cf 4c 91` | add x8,x28,#0x333, LSL #12 | `FALL_THROUGH`
<a id="insn-00aea770"></a> `00aea770` | `49 cf 4c 91` | add x9,x26,#0x333, LSL #12 | `FALL_THROUGH`
<a id="insn-00aea774"></a> `00aea774` | `81 8e 40 f9` | ldr x1,[x20, #0x118] | `FALL_THROUGH`
<a id="insn-00aea778"></a> `00aea778` | `08 e1 28 91` | add x8,x8,#0xa38 | `FALL_THROUGH`
<a id="insn-00aea77c"></a> `00aea77c` | `29 41 2a 91` | add x9,x9,#0xa90 | `FALL_THROUGH`
<a id="insn-00aea780"></a> `00aea780` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aea784"></a> `00aea784` | `0a 21 40 29` | ldp w10,w8,[x8] | `FALL_THROUGH`
<a id="insn-00aea788"></a> `00aea788` | `2b 25 40 29` | ldp w11,w9,[x9] | `FALL_THROUGH`
<a id="insn-00aea78c"></a> `00aea78c` | `4a 01 0b 0b` | add w10,w10,w11 | `FALL_THROUGH`
<a id="insn-00aea790"></a> `00aea790` | `08 01 09 0b` | add w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00aea794"></a> `00aea794` | `42 09 00 11` | add w2,w10,#0x2 | `FALL_THROUGH`
<a id="insn-00aea798"></a> `00aea798` | `03 09 00 11` | add w3,w8,#0x2 | `FALL_THROUGH`
<a id="insn-00aea79c"></a> `00aea79c` | `64 10 80 52` | mov w4,#0x83 | `FALL_THROUGH`
<a id="insn-00aea7a0"></a> `00aea7a0` | `27 00 00 14` | b 0x00aea83c | `UNCONDITIONAL_JUMP`
<a id="insn-00aea7a4"></a> `00aea7a4` | `88 2f 97 52` | mov w8,#0xb97c | `FALL_THROUGH`
<a id="insn-00aea7a8"></a> `00aea7a8` | `a0 82 12 91` | add x0,x21,#0x4a0 | `FALL_THROUGH`
<a id="insn-00aea7ac"></a> `00aea7ac` | `28 07 a0 72` | movk w8,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00aea7b0"></a> `00aea7b0` | `a1 6a a8 b8` | ldrsw x1,[x21, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aea7b4"></a> `00aea7b4` | `88 05 80 52` | mov w8,#0x2c | `FALL_THROUGH`
<a id="insn-00aea7b8"></a> `00aea7b8` | `28 6c 28 9b` | smaddl x8,w1,w8,x27 | `FALL_THROUGH`
<a id="insn-00aea7bc"></a> `00aea7bc` | `09 01 19 8b` | add x9,x8,x25 | `FALL_THROUGH`
<a id="insn-00aea7c0"></a> `00aea7c0` | `0a a1 40 39` | ldrb w10,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aea7c4"></a> `00aea7c4` | `0c a5 40 39` | ldrb w12,[x8, #0x29] | `FALL_THROUGH`
<a id="insn-00aea7c8"></a> `00aea7c8` | `2b 01 40 39` | ldrb w11,[x9] | `FALL_THROUGH`
<a id="insn-00aea7cc"></a> `00aea7cc` | `2d 05 40 39` | ldrb w13,[x9, #0x1] | `FALL_THROUGH`
<a id="insn-00aea7d0"></a> `00aea7d0` | `4a 01 0b 4a` | eor w10,w10,w11 | `FALL_THROUGH`
<a id="insn-00aea7d4"></a> `00aea7d4` | `8b 01 0d 4a` | eor w11,w12,w13 | `FALL_THROUGH`
<a id="insn-00aea7d8"></a> `00aea7d8` | `2c 09 40 39` | ldrb w12,[x9, #0x2] | `FALL_THROUGH`
<a id="insn-00aea7dc"></a> `00aea7dc` | `0d a9 40 39` | ldrb w13,[x8, #0x2a] | `FALL_THROUGH`
<a id="insn-00aea7e0"></a> `00aea7e0` | `4a 21 0b 2a` | orr w10,w10,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00aea7e4"></a> `00aea7e4` | `29 0d 40 39` | ldrb w9,[x9, #0x3] | `FALL_THROUGH`
<a id="insn-00aea7e8"></a> `00aea7e8` | `08 ad 40 39` | ldrb w8,[x8, #0x2b] | `FALL_THROUGH`
<a id="insn-00aea7ec"></a> `00aea7ec` | `ab 01 0c 4a` | eor w11,w13,w12 | `FALL_THROUGH`
<a id="insn-00aea7f0"></a> `00aea7f0` | `4a 41 0b 2a` | orr w10,w10,w11, LSL #0x10 | `FALL_THROUGH`
<a id="insn-00aea7f4"></a> `00aea7f4` | `08 01 09 4a` | eor w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00aea7f8"></a> `00aea7f8` | `48 61 08 2a` | orr w8,w10,w8, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00aea7fc"></a> `00aea7fc` | `02 09 00 51` | sub w2,w8,#0x2 | `FALL_THROUGH`
<a id="insn-00aea800"></a> `00aea800` | `2c 57 eb 97` | bl 0x005c04b0 | `UNCONDITIONAL_CALL`
<a id="insn-00aea804"></a> `00aea804` | `a0 02 00 36` | tbz w0,#0x0,0x00aea858 | `CONDITIONAL_JUMP`
<a id="insn-00aea808"></a> `00aea808` | `88 cf 4c 91` | add x8,x28,#0x333, LSL #12 | `FALL_THROUGH`
<a id="insn-00aea80c"></a> `00aea80c` | `49 cf 4c 91` | add x9,x26,#0x333, LSL #12 | `FALL_THROUGH`
<a id="insn-00aea810"></a> `00aea810` | `81 8e 40 f9` | ldr x1,[x20, #0x118] | `FALL_THROUGH`
<a id="insn-00aea814"></a> `00aea814` | `08 e1 28 91` | add x8,x8,#0xa38 | `FALL_THROUGH`
<a id="insn-00aea818"></a> `00aea818` | `29 41 2a 91` | add x9,x9,#0xa90 | `FALL_THROUGH`
<a id="insn-00aea81c"></a> `00aea81c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aea820"></a> `00aea820` | `0a 21 40 29` | ldp w10,w8,[x8] | `FALL_THROUGH`
<a id="insn-00aea824"></a> `00aea824` | `2b 25 40 29` | ldp w11,w9,[x9] | `FALL_THROUGH`
<a id="insn-00aea828"></a> `00aea828` | `4a 01 0b 0b` | add w10,w10,w11 | `FALL_THROUGH`
<a id="insn-00aea82c"></a> `00aea82c` | `08 01 09 0b` | add w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00aea830"></a> `00aea830` | `42 09 00 11` | add w2,w10,#0x2 | `FALL_THROUGH`
<a id="insn-00aea834"></a> `00aea834` | `03 09 00 11` | add w3,w8,#0x2 | `FALL_THROUGH`
<a id="insn-00aea838"></a> `00aea838` | `c4 11 80 52` | mov w4,#0x8e | `FALL_THROUGH`
<a id="insn-00aea83c"></a> `00aea83c` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aea840"></a> `00aea840` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aea844"></a> `00aea844` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aea848"></a> `00aea848` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aea84c"></a> `00aea84c` | `fc 6f 41 a9` | ldp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aea850"></a> `00aea850` | `fd 7b c6 a8` | ldp x29,x30,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00aea854"></a> `00aea854` | `bd f9 e5 17` | b 0x00468f48 | `CALL_TERMINATOR`
<a id="insn-00aea858"></a> `00aea858` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aea85c"></a> `00aea85c` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aea860"></a> `00aea860` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aea864"></a> `00aea864` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aea868"></a> `00aea868` | `fc 6f 41 a9` | ldp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aea86c"></a> `00aea86c` | `fd 7b c6 a8` | ldp x29,x30,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00aea870"></a> `00aea870` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aea2fc`](#insn-00aea2fc) 範囲 `[['00aea2fc', '00aea31f']]`
  - `FALL_THROUGH` [`00aea31c`](#insn-00aea31c) → [`00aea320`](#insn-00aea320)
- ブロック [`00aea320`](#insn-00aea320) 範囲 `[['00aea320', '00aea333']]`
  - `CONDITIONAL_JUMP` [`00aea330`](#insn-00aea330) → [`00aea354`](#insn-00aea354)
  - `FALL_THROUGH` [`00aea330`](#insn-00aea330) → [`00aea334`](#insn-00aea334)
- ブロック [`00aea334`](#insn-00aea334) 範囲 `[['00aea334', '00aea353']]`
  - `UNCONDITIONAL_JUMP` [`00aea350`](#insn-00aea350) → [`00aea358`](#insn-00aea358)
- ブロック [`00aea354`](#insn-00aea354) 範囲 `[['00aea354', '00aea357']]`
  - `FALL_THROUGH` [`00aea354`](#insn-00aea354) → [`00aea358`](#insn-00aea358)
- ブロック [`00aea358`](#insn-00aea358) 範囲 `[['00aea358', '00aea36b']]`
  - `CONDITIONAL_JUMP` [`00aea368`](#insn-00aea368) → [`00aea858`](#insn-00aea858)
  - `FALL_THROUGH` [`00aea368`](#insn-00aea368) → [`00aea36c`](#insn-00aea36c)
- ブロック [`00aea36c`](#insn-00aea36c) 範囲 `[['00aea36c', '00aea3bf']]`
  - `FALL_THROUGH` [`00aea3bc`](#insn-00aea3bc) → [`00aea3c0`](#insn-00aea3c0)
- ブロック [`00aea3c0`](#insn-00aea3c0) 範囲 `[['00aea3c0', '00aea3db']]`
  - `CONDITIONAL_JUMP` [`00aea3d8`](#insn-00aea3d8) → [`00aea858`](#insn-00aea858)
  - `FALL_THROUGH` [`00aea3d8`](#insn-00aea3d8) → [`00aea3dc`](#insn-00aea3dc)
- ブロック [`00aea3dc`](#insn-00aea3dc) 範囲 `[['00aea3dc', '00aea3df']]`
  - `FALL_THROUGH` [`00aea3dc`](#insn-00aea3dc) → [`00aea3e0`](#insn-00aea3e0)
- ブロック [`00aea3e0`](#insn-00aea3e0) 範囲 `[['00aea3e0', '00aea3fb']]`
  - `CONDITIONAL_JUMP` [`00aea3f8`](#insn-00aea3f8) → [`00aea444`](#insn-00aea444)
  - `FALL_THROUGH` [`00aea3f8`](#insn-00aea3f8) → [`00aea3fc`](#insn-00aea3fc)
- ブロック [`00aea3fc`](#insn-00aea3fc) 範囲 `[['00aea3fc', '00aea423']]`
  - `CONDITIONAL_JUMP` [`00aea420`](#insn-00aea420) → [`00aea4a0`](#insn-00aea4a0)
  - `FALL_THROUGH` [`00aea420`](#insn-00aea420) → [`00aea424`](#insn-00aea424)
- ブロック [`00aea424`](#insn-00aea424) 範囲 `[['00aea424', '00aea42b']]`
  - `CONDITIONAL_JUMP` [`00aea428`](#insn-00aea428) → [`00aea454`](#insn-00aea454)
  - `FALL_THROUGH` [`00aea428`](#insn-00aea428) → [`00aea42c`](#insn-00aea42c)
- ブロック [`00aea42c`](#insn-00aea42c) 範囲 `[['00aea42c', '00aea43f']]`
  - `FALL_THROUGH` [`00aea43c`](#insn-00aea43c) → [`00aea440`](#insn-00aea440)
- ブロック [`00aea440`](#insn-00aea440) 範囲 `[['00aea440', '00aea443']]`
  - `UNCONDITIONAL_JUMP` [`00aea440`](#insn-00aea440) → [`00aea454`](#insn-00aea454)
- ブロック [`00aea444`](#insn-00aea444) 範囲 `[['00aea444', '00aea453']]`
  - `CONDITIONAL_JUMP` [`00aea450`](#insn-00aea450) → [`00aea4a0`](#insn-00aea4a0)
  - `FALL_THROUGH` [`00aea450`](#insn-00aea450) → [`00aea454`](#insn-00aea454)
- ブロック [`00aea454`](#insn-00aea454) 範囲 `[['00aea454', '00aea483']]`
  - `FALL_THROUGH` [`00aea480`](#insn-00aea480) → [`00aea484`](#insn-00aea484)
- ブロック [`00aea484`](#insn-00aea484) 範囲 `[['00aea484', '00aea49f']]`
  - `FALL_THROUGH` [`00aea49c`](#insn-00aea49c) → [`00aea4a0`](#insn-00aea4a0)
- ブロック [`00aea4a0`](#insn-00aea4a0) 範囲 `[['00aea4a0', '00aea4af']]`
  - `CONDITIONAL_JUMP` [`00aea4ac`](#insn-00aea4ac) → [`00aea744`](#insn-00aea744)
  - `FALL_THROUGH` [`00aea4ac`](#insn-00aea4ac) → [`00aea4b0`](#insn-00aea4b0)
- ブロック [`00aea4b0`](#insn-00aea4b0) 範囲 `[['00aea4b0', '00aea4cf']]`
  - `CONDITIONAL_JUMP` [`00aea4cc`](#insn-00aea4cc) → [`00aea4e4`](#insn-00aea4e4)
  - `FALL_THROUGH` [`00aea4cc`](#insn-00aea4cc) → [`00aea4d0`](#insn-00aea4d0)
- ブロック [`00aea4d0`](#insn-00aea4d0) 範囲 `[['00aea4d0', '00aea4e3']]`
  - `CONDITIONAL_JUMP` [`00aea4e0`](#insn-00aea4e0) → [`00aea578`](#insn-00aea578)
  - `FALL_THROUGH` [`00aea4e0`](#insn-00aea4e0) → [`00aea4e4`](#insn-00aea4e4)
- ブロック [`00aea4e4`](#insn-00aea4e4) 範囲 `[['00aea4e4', '00aea4ff']]`
  - `FALL_THROUGH` [`00aea4fc`](#insn-00aea4fc) → [`00aea500`](#insn-00aea500)
- ブロック [`00aea500`](#insn-00aea500) 範囲 `[['00aea500', '00aea54b']]`
  - `CONDITIONAL_JUMP` [`00aea548`](#insn-00aea548) → [`00aea55c`](#insn-00aea55c)
  - `FALL_THROUGH` [`00aea548`](#insn-00aea548) → [`00aea54c`](#insn-00aea54c)
- ブロック [`00aea54c`](#insn-00aea54c) 範囲 `[['00aea54c', '00aea55b']]`
  - `CONDITIONAL_JUMP` [`00aea558`](#insn-00aea558) → [`00aea578`](#insn-00aea578)
  - `FALL_THROUGH` [`00aea558`](#insn-00aea558) → [`00aea55c`](#insn-00aea55c)
- ブロック [`00aea55c`](#insn-00aea55c) 範囲 `[['00aea55c', '00aea567']]`
  - `CONDITIONAL_JUMP` [`00aea564`](#insn-00aea564) → [`00aea744`](#insn-00aea744)
  - `FALL_THROUGH` [`00aea564`](#insn-00aea564) → [`00aea568`](#insn-00aea568)
- ブロック [`00aea568`](#insn-00aea568) 範囲 `[['00aea568', '00aea577']]`
  - `CONDITIONAL_JUMP` [`00aea574`](#insn-00aea574) → [`00aea744`](#insn-00aea744)
  - `FALL_THROUGH` [`00aea574`](#insn-00aea574) → [`00aea578`](#insn-00aea578)
- ブロック [`00aea578`](#insn-00aea578) 範囲 `[['00aea578', '00aea5a3']]`
  - `FALL_THROUGH` [`00aea5a0`](#insn-00aea5a0) → [`00aea5a4`](#insn-00aea5a4)
- ブロック [`00aea5a4`](#insn-00aea5a4) 範囲 `[['00aea5a4', '00aea5af']]`
  - `FALL_THROUGH` [`00aea5ac`](#insn-00aea5ac) → [`00aea5b0`](#insn-00aea5b0)
- ブロック [`00aea5b0`](#insn-00aea5b0) 範囲 `[['00aea5b0', '00aea5df']]`
  - `CONDITIONAL_JUMP` [`00aea5dc`](#insn-00aea5dc) → [`00aea5f0`](#insn-00aea5f0)
  - `FALL_THROUGH` [`00aea5dc`](#insn-00aea5dc) → [`00aea5e0`](#insn-00aea5e0)
- ブロック [`00aea5e0`](#insn-00aea5e0) 範囲 `[['00aea5e0', '00aea5ef']]`
  - `CONDITIONAL_JUMP` [`00aea5ec`](#insn-00aea5ec) → [`00aea680`](#insn-00aea680)
  - `FALL_THROUGH` [`00aea5ec`](#insn-00aea5ec) → [`00aea5f0`](#insn-00aea5f0)
- ブロック [`00aea5f0`](#insn-00aea5f0) 範囲 `[['00aea5f0', '00aea5fb']]`
  - `CONDITIONAL_JUMP` [`00aea5f8`](#insn-00aea5f8) → [`00aea60c`](#insn-00aea60c)
  - `FALL_THROUGH` [`00aea5f8`](#insn-00aea5f8) → [`00aea5fc`](#insn-00aea5fc)
- ブロック [`00aea5fc`](#insn-00aea5fc) 範囲 `[['00aea5fc', '00aea60b']]`
  - `CONDITIONAL_JUMP` [`00aea608`](#insn-00aea608) → [`00aea680`](#insn-00aea680)
  - `FALL_THROUGH` [`00aea608`](#insn-00aea608) → [`00aea60c`](#insn-00aea60c)
- ブロック [`00aea60c`](#insn-00aea60c) 範囲 `[['00aea60c', '00aea67f']]`
  - `UNCONDITIONAL_JUMP` [`00aea67c`](#insn-00aea67c) → [`00aea6f0`](#insn-00aea6f0)
- ブロック [`00aea680`](#insn-00aea680) 範囲 `[['00aea680', '00aea6ef']]`
  - `FALL_THROUGH` [`00aea6ec`](#insn-00aea6ec) → [`00aea6f0`](#insn-00aea6f0)
- ブロック [`00aea6f0`](#insn-00aea6f0) 範囲 `[['00aea6f0', '00aea6fb']]`
  - `FALL_THROUGH` [`00aea6f8`](#insn-00aea6f8) → [`00aea6fc`](#insn-00aea6fc)
- ブロック [`00aea6fc`](#insn-00aea6fc) 範囲 `[['00aea6fc', '00aea6ff']]`
  - `FALL_THROUGH` [`00aea6fc`](#insn-00aea6fc) → [`00aea700`](#insn-00aea700)
- ブロック [`00aea700`](#insn-00aea700) 範囲 `[['00aea700', '00aea727']]`
  - `FALL_THROUGH` [`00aea724`](#insn-00aea724) → [`00aea728`](#insn-00aea728)
- ブロック [`00aea728`](#insn-00aea728) 範囲 `[['00aea728', '00aea73b']]`
  - `FALL_THROUGH` [`00aea738`](#insn-00aea738) → [`00aea73c`](#insn-00aea73c)
- ブロック [`00aea73c`](#insn-00aea73c) 範囲 `[['00aea73c', '00aea73f']]`
  - `FALL_THROUGH` [`00aea73c`](#insn-00aea73c) → [`00aea740`](#insn-00aea740)
- ブロック [`00aea740`](#insn-00aea740) 範囲 `[['00aea740', '00aea743']]`
  - `FALL_THROUGH` [`00aea740`](#insn-00aea740) → [`00aea744`](#insn-00aea744)
- ブロック [`00aea744`](#insn-00aea744) 範囲 `[['00aea744', '00aea74b']]`
  - `FALL_THROUGH` [`00aea748`](#insn-00aea748) → [`00aea74c`](#insn-00aea74c)
- ブロック [`00aea74c`](#insn-00aea74c) 範囲 `[['00aea74c', '00aea74f']]`
  - `CONDITIONAL_JUMP` [`00aea74c`](#insn-00aea74c) → [`00aea7a4`](#insn-00aea7a4)
  - `FALL_THROUGH` [`00aea74c`](#insn-00aea74c) → [`00aea750`](#insn-00aea750)
- ブロック [`00aea750`](#insn-00aea750) 範囲 `[['00aea750', '00aea757']]`
  - `FALL_THROUGH` [`00aea754`](#insn-00aea754) → [`00aea758`](#insn-00aea758)
- ブロック [`00aea758`](#insn-00aea758) 範囲 `[['00aea758', '00aea76b']]`
  - `CONDITIONAL_JUMP` [`00aea768`](#insn-00aea768) → [`00aea7a4`](#insn-00aea7a4)
  - `FALL_THROUGH` [`00aea768`](#insn-00aea768) → [`00aea76c`](#insn-00aea76c)
- ブロック [`00aea76c`](#insn-00aea76c) 範囲 `[['00aea76c', '00aea77b']]`
  - `FALL_THROUGH` [`00aea778`](#insn-00aea778) → [`00aea77c`](#insn-00aea77c)
- ブロック [`00aea77c`](#insn-00aea77c) 範囲 `[['00aea77c', '00aea77f']]`
  - `FALL_THROUGH` [`00aea77c`](#insn-00aea77c) → [`00aea780`](#insn-00aea780)
- ブロック [`00aea780`](#insn-00aea780) 範囲 `[['00aea780', '00aea78f']]`
  - `FALL_THROUGH` [`00aea78c`](#insn-00aea78c) → [`00aea790`](#insn-00aea790)
- ブロック [`00aea790`](#insn-00aea790) 範囲 `[['00aea790', '00aea797']]`
  - `FALL_THROUGH` [`00aea794`](#insn-00aea794) → [`00aea798`](#insn-00aea798)
- ブロック [`00aea798`](#insn-00aea798) 範囲 `[['00aea798', '00aea7a3']]`
  - `UNCONDITIONAL_JUMP` [`00aea7a0`](#insn-00aea7a0) → [`00aea83c`](#insn-00aea83c)
- ブロック [`00aea7a4`](#insn-00aea7a4) 範囲 `[['00aea7a4', '00aea7d7']]`
  - `FALL_THROUGH` [`00aea7d4`](#insn-00aea7d4) → [`00aea7d8`](#insn-00aea7d8)
- ブロック [`00aea7d8`](#insn-00aea7d8) 範囲 `[['00aea7d8', '00aea807']]`
  - `CONDITIONAL_JUMP` [`00aea804`](#insn-00aea804) → [`00aea858`](#insn-00aea858)
  - `FALL_THROUGH` [`00aea804`](#insn-00aea804) → [`00aea808`](#insn-00aea808)
- ブロック [`00aea808`](#insn-00aea808) 範囲 `[['00aea808', '00aea823']]`
  - `FALL_THROUGH` [`00aea820`](#insn-00aea820) → [`00aea824`](#insn-00aea824)
- ブロック [`00aea824`](#insn-00aea824) 範囲 `[['00aea824', '00aea83b']]`
  - `FALL_THROUGH` [`00aea838`](#insn-00aea838) → [`00aea83c`](#insn-00aea83c)
- ブロック [`00aea83c`](#insn-00aea83c) 範囲 `[['00aea83c', '00aea857']]`
- ブロック [`00aea858`](#insn-00aea858) 範囲 `[['00aea858', '00aea873']]`

## 命令位置別の参照

- [`00aea2fc`](#insn-00aea2fc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea300`](#insn-00aea300) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea304`](#insn-00aea304) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea308`](#insn-00aea308) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea30c`](#insn-00aea30c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea310`](#insn-00aea310) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea324`](#insn-00aea324) → `00ca4578`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aea330`](#insn-00aea330) → [`00aea354`](#insn-00aea354) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea338`](#insn-00aea338) → `00c65a58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00aea340`](#insn-00aea340) → `00c8d550`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00aea348`](#insn-00aea348) → [`00c58210`](../00c58/00c58210.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58210` · 推定シンボル `None` · 推定型 `None`
- [`00aea350`](#insn-00aea350) → [`00aea358`](#insn-00aea358) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea358`](#insn-00aea358) → [`00467820`](../00467/00467820.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467820` · 推定シンボル `None` · 推定型 `None`
- [`00aea35c`](#insn-00aea35c) → `00333a88`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aea368`](#insn-00aea368) → [`00aea858`](#insn-00aea858) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea384`](#insn-00aea384) → `0039b97c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aea3d8`](#insn-00aea3d8) → [`00aea858`](#insn-00aea858) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea3ec`](#insn-00aea3ec) → [`00adee94`](../00ade/00adee94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adee94` · 推定シンボル `None` · 推定型 `None`
- [`00aea3f8`](#insn-00aea3f8) → [`00aea444`](#insn-00aea444) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea410`](#insn-00aea410) → [`0046da7c`](../0046d/0046da7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046da7c` · 推定シンボル `None` · 推定型 `None`
- [`00aea420`](#insn-00aea420) → [`00aea4a0`](#insn-00aea4a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea428`](#insn-00aea428) → [`00aea454`](#insn-00aea454) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea438`](#insn-00aea438) → [`00468b9c`](../00468/00468b9c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468b9c` · 推定シンボル `None` · 推定型 `None`
- [`00aea440`](#insn-00aea440) → [`00aea454`](#insn-00aea454) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea450`](#insn-00aea450) → [`00aea4a0`](#insn-00aea4a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea46c`](#insn-00aea46c) → `00333a38`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aea46c`](#insn-00aea46c) → `00333a3c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aea470`](#insn-00aea470) → `00333a90`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aea470`](#insn-00aea470) → `00333a94`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aea484`](#insn-00aea484) → [`00469bc4`](../00469/00469bc4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469bc4` · 推定シンボル `None` · 推定型 `None`
- [`00aea49c`](#insn-00aea49c) → [`00467b20`](../00467/00467b20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467b20` · 推定シンボル `None` · 推定型 `None`
- [`00aea4ac`](#insn-00aea4ac) → [`00aea744`](#insn-00aea744) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea4bc`](#insn-00aea4bc) → [`00a41e38`](../00a41/00a41e38.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a41e38` · 推定シンボル `None` · 推定型 `None`
- [`00aea4c8`](#insn-00aea4c8) → [`00a41ec4`](../00a41/00a41ec4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a41ec4` · 推定シンボル `None` · 推定型 `None`
- [`00aea4cc`](#insn-00aea4cc) → [`00aea4e4`](#insn-00aea4e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea4dc`](#insn-00aea4dc) → [`00a41f9c`](../00a41/00a41f9c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a41f9c` · 推定シンボル `None` · 推定型 `None`
- [`00aea4e0`](#insn-00aea4e0) → [`00aea578`](#insn-00aea578) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea4f4`](#insn-00aea4f4) → `0039b97c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aea544`](#insn-00aea544) → [`007441c8`](../00744/007441c8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007441c8` · 推定シンボル `None` · 推定型 `None`
- [`00aea548`](#insn-00aea548) → [`00aea55c`](#insn-00aea55c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea554`](#insn-00aea554) → [`00743d50`](../00743/00743d50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00743d50` · 推定シンボル `None` · 推定型 `None`
- [`00aea558`](#insn-00aea558) → [`00aea578`](#insn-00aea578) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea560`](#insn-00aea560) → [`00b09234`](../00b09/00b09234.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b09234` · 推定シンボル `None` · 推定型 `None`
- [`00aea564`](#insn-00aea564) → [`00aea744`](#insn-00aea744) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea570`](#insn-00aea570) → [`00b0a8ec`](../00b0a/00b0a8ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b0a8ec` · 推定シンボル `None` · 推定型 `None`
- [`00aea574`](#insn-00aea574) → [`00aea744`](#insn-00aea744) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea588`](#insn-00aea588) → `0039b97c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aea5d8`](#insn-00aea5d8) → [`007441c8`](../00744/007441c8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007441c8` · 推定シンボル `None` · 推定型 `None`
- [`00aea5dc`](#insn-00aea5dc) → [`00aea5f0`](#insn-00aea5f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea5e8`](#insn-00aea5e8) → [`00743d50`](../00743/00743d50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00743d50` · 推定シンボル `None` · 推定型 `None`
- [`00aea5ec`](#insn-00aea5ec) → [`00aea680`](#insn-00aea680) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea5f4`](#insn-00aea5f4) → [`00b09234`](../00b09/00b09234.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b09234` · 推定シンボル `None` · 推定型 `None`
- [`00aea5f8`](#insn-00aea5f8) → [`00aea60c`](#insn-00aea60c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea604`](#insn-00aea604) → [`00b0a8ec`](../00b0a/00b0a8ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b0a8ec` · 推定シンボル `None` · 推定型 `None`
- [`00aea608`](#insn-00aea608) → [`00aea680`](#insn-00aea680) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea67c`](#insn-00aea67c) → [`00aea6f0`](#insn-00aea6f0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea6f8`](#insn-00aea6f8) → [`00467aec`](../00467/00467aec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467aec` · 推定シンボル `None` · 推定型 `None`
- [`00aea704`](#insn-00aea704) → [`00467ab0`](../00467/00467ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467ab0` · 推定シンボル `None` · 推定型 `None`
- [`00aea720`](#insn-00aea720) → `00333a38`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aea720`](#insn-00aea720) → `00333a3c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aea724`](#insn-00aea724) → `00333a90`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aea724`](#insn-00aea724) → `00333a94`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aea734`](#insn-00aea734) → [`00467f14`](../00467/00467f14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467f14` · 推定シンボル `None` · 推定型 `None`
- [`00aea740`](#insn-00aea740) → [`00467ab0`](../00467/00467ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467ab0` · 推定シンボル `None` · 推定型 `None`
- [`00aea748`](#insn-00aea748) → [`007441c8`](../00744/007441c8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007441c8` · 推定シンボル `None` · 推定型 `None`
- [`00aea74c`](#insn-00aea74c) → [`00aea7a4`](#insn-00aea7a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea758`](#insn-00aea758) → [`00744158`](../00744/00744158.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00744158` · 推定シンボル `None` · 推定型 `None`
- [`00aea764`](#insn-00aea764) → [`00743eec`](../00743/00743eec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00743eec` · 推定シンボル `None` · 推定型 `None`
- [`00aea768`](#insn-00aea768) → [`00aea7a4`](#insn-00aea7a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea784`](#insn-00aea784) → `00333a38`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aea784`](#insn-00aea784) → `00333a3c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aea788`](#insn-00aea788) → `00333a90`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aea788`](#insn-00aea788) → `00333a94`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aea7a0`](#insn-00aea7a0) → [`00aea83c`](#insn-00aea83c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea7b0`](#insn-00aea7b0) → `0039b97c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aea800`](#insn-00aea800) → [`005c04b0`](../005c0/005c04b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c04b0` · 推定シンボル `None` · 推定型 `None`
- [`00aea804`](#insn-00aea804) → [`00aea858`](#insn-00aea858) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea820`](#insn-00aea820) → `00333a38`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aea820`](#insn-00aea820) → `00333a3c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aea824`](#insn-00aea824) → `00333a90`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aea824`](#insn-00aea824) → `00333a94`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aea83c`](#insn-00aea83c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea840`](#insn-00aea840) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea844`](#insn-00aea844) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea848`](#insn-00aea848) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea84c`](#insn-00aea84c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea850`](#insn-00aea850) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea854`](#insn-00aea854) → [`00468f48`](../00468/00468f48.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468f48` · 推定シンボル `None` · 推定型 `None`
- [`00aea858`](#insn-00aea858) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea85c`](#insn-00aea85c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea860`](#insn-00aea860) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea864`](#insn-00aea864) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea868`](#insn-00aea868) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea86c`](#insn-00aea86c) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aea2fc`](#insn-00aea2fc)

~~~json
{
  "source": "00aea2fc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea300`](#insn-00aea300)

~~~json
{
  "source": "00aea300",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea304`](#insn-00aea304)

~~~json
{
  "source": "00aea304",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea308`](#insn-00aea308)

~~~json
{
  "source": "00aea308",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea30c`](#insn-00aea30c)

~~~json
{
  "source": "00aea30c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea310`](#insn-00aea310)

~~~json
{
  "source": "00aea310",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea324`](#insn-00aea324)

~~~json
{
  "source": "00aea324",
  "target": "00ca4578",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4578",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aea330`](#insn-00aea330)

~~~json
{
  "source": "00aea330",
  "target": "00aea354",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea338`](#insn-00aea338)

~~~json
{
  "source": "00aea338",
  "target": "00c65a58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c65a58",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aea340`](#insn-00aea340)

~~~json
{
  "source": "00aea340",
  "target": "00c8d550",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8d550",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aea348`](#insn-00aea348)

~~~json
{
  "source": "00aea348",
  "target": "00c58210",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea350`](#insn-00aea350)

~~~json
{
  "source": "00aea350",
  "target": "00aea358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea358`](#insn-00aea358)

~~~json
{
  "source": "00aea358",
  "target": "00467820",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea35c`](#insn-00aea35c)

~~~json
{
  "source": "00aea35c",
  "target": "00333a88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333a88",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "c8c96a00747b0900",
  "capture_start": "00333a88",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aea368`](#insn-00aea368)

~~~json
{
  "source": "00aea368",
  "target": "00aea858",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea384`](#insn-00aea384)

~~~json
{
  "source": "00aea384",
  "target": "0039b97c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b97c",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "348b5000",
  "capture_start": "0039b97c",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aea3d8`](#insn-00aea3d8)

~~~json
{
  "source": "00aea3d8",
  "target": "00aea858",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea3ec`](#insn-00aea3ec)

~~~json
{
  "source": "00aea3ec",
  "target": "00adee94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea3f8`](#insn-00aea3f8)

~~~json
{
  "source": "00aea3f8",
  "target": "00aea444",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea410`](#insn-00aea410)

~~~json
{
  "source": "00aea410",
  "target": "0046da7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea420`](#insn-00aea420)

~~~json
{
  "source": "00aea420",
  "target": "00aea4a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea428`](#insn-00aea428)

~~~json
{
  "source": "00aea428",
  "target": "00aea454",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea438`](#insn-00aea438)

~~~json
{
  "source": "00aea438",
  "target": "00468b9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea440`](#insn-00aea440)

~~~json
{
  "source": "00aea440",
  "target": "00aea454",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea450`](#insn-00aea450)

~~~json
{
  "source": "00aea450",
  "target": "00aea4a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea46c`](#insn-00aea46c)

~~~json
{
  "source": "00aea46c",
  "target": "00333a38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333a38",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "c0c26a00987a0900",
  "capture_start": "00333a38",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aea46c`](#insn-00aea46c)

~~~json
{
  "source": "00aea46c",
  "target": "00333a3c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333a38",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "c0c26a00987a0900",
  "capture_start": "00333a38",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aea470`](#insn-00aea470)

~~~json
{
  "source": "00aea470",
  "target": "00333a90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333a90",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "d8c96a00887b0900",
  "capture_start": "00333a90",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aea470`](#insn-00aea470)

~~~json
{
  "source": "00aea470",
  "target": "00333a94",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333a90",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "d8c96a00887b0900",
  "capture_start": "00333a90",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aea484`](#insn-00aea484)

~~~json
{
  "source": "00aea484",
  "target": "00469bc4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea49c`](#insn-00aea49c)

~~~json
{
  "source": "00aea49c",
  "target": "00467b20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea4ac`](#insn-00aea4ac)

~~~json
{
  "source": "00aea4ac",
  "target": "00aea744",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea4bc`](#insn-00aea4bc)

~~~json
{
  "source": "00aea4bc",
  "target": "00a41e38",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea4c8`](#insn-00aea4c8)

~~~json
{
  "source": "00aea4c8",
  "target": "00a41ec4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea4cc`](#insn-00aea4cc)

~~~json
{
  "source": "00aea4cc",
  "target": "00aea4e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea4dc`](#insn-00aea4dc)

~~~json
{
  "source": "00aea4dc",
  "target": "00a41f9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea4e0`](#insn-00aea4e0)

~~~json
{
  "source": "00aea4e0",
  "target": "00aea578",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea4f4`](#insn-00aea4f4)

~~~json
{
  "source": "00aea4f4",
  "target": "0039b97c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b97c",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "348b5000",
  "capture_start": "0039b97c",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aea544`](#insn-00aea544)

~~~json
{
  "source": "00aea544",
  "target": "007441c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea548`](#insn-00aea548)

~~~json
{
  "source": "00aea548",
  "target": "00aea55c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea554`](#insn-00aea554)

~~~json
{
  "source": "00aea554",
  "target": "00743d50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea558`](#insn-00aea558)

~~~json
{
  "source": "00aea558",
  "target": "00aea578",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea560`](#insn-00aea560)

~~~json
{
  "source": "00aea560",
  "target": "00b09234",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea564`](#insn-00aea564)

~~~json
{
  "source": "00aea564",
  "target": "00aea744",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea570`](#insn-00aea570)

~~~json
{
  "source": "00aea570",
  "target": "00b0a8ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea574`](#insn-00aea574)

~~~json
{
  "source": "00aea574",
  "target": "00aea744",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea588`](#insn-00aea588)

~~~json
{
  "source": "00aea588",
  "target": "0039b97c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b97c",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "348b5000",
  "capture_start": "0039b97c",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aea5d8`](#insn-00aea5d8)

~~~json
{
  "source": "00aea5d8",
  "target": "007441c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea5dc`](#insn-00aea5dc)

~~~json
{
  "source": "00aea5dc",
  "target": "00aea5f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea5e8`](#insn-00aea5e8)

~~~json
{
  "source": "00aea5e8",
  "target": "00743d50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea5ec`](#insn-00aea5ec)

~~~json
{
  "source": "00aea5ec",
  "target": "00aea680",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea5f4`](#insn-00aea5f4)

~~~json
{
  "source": "00aea5f4",
  "target": "00b09234",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea5f8`](#insn-00aea5f8)

~~~json
{
  "source": "00aea5f8",
  "target": "00aea60c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea604`](#insn-00aea604)

~~~json
{
  "source": "00aea604",
  "target": "00b0a8ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea608`](#insn-00aea608)

~~~json
{
  "source": "00aea608",
  "target": "00aea680",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea67c`](#insn-00aea67c)

~~~json
{
  "source": "00aea67c",
  "target": "00aea6f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea6f8`](#insn-00aea6f8)

~~~json
{
  "source": "00aea6f8",
  "target": "00467aec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea704`](#insn-00aea704)

~~~json
{
  "source": "00aea704",
  "target": "00467ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea720`](#insn-00aea720)

~~~json
{
  "source": "00aea720",
  "target": "00333a38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333a38",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "c0c26a00987a0900",
  "capture_start": "00333a38",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aea720`](#insn-00aea720)

~~~json
{
  "source": "00aea720",
  "target": "00333a3c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333a38",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "c0c26a00987a0900",
  "capture_start": "00333a38",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aea724`](#insn-00aea724)

~~~json
{
  "source": "00aea724",
  "target": "00333a90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333a90",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "d8c96a00887b0900",
  "capture_start": "00333a90",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aea724`](#insn-00aea724)

~~~json
{
  "source": "00aea724",
  "target": "00333a94",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333a90",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "d8c96a00887b0900",
  "capture_start": "00333a90",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aea734`](#insn-00aea734)

~~~json
{
  "source": "00aea734",
  "target": "00467f14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea740`](#insn-00aea740)

~~~json
{
  "source": "00aea740",
  "target": "00467ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea748`](#insn-00aea748)

~~~json
{
  "source": "00aea748",
  "target": "007441c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea74c`](#insn-00aea74c)

~~~json
{
  "source": "00aea74c",
  "target": "00aea7a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea758`](#insn-00aea758)

~~~json
{
  "source": "00aea758",
  "target": "00744158",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea764`](#insn-00aea764)

~~~json
{
  "source": "00aea764",
  "target": "00743eec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea768`](#insn-00aea768)

~~~json
{
  "source": "00aea768",
  "target": "00aea7a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea784`](#insn-00aea784)

~~~json
{
  "source": "00aea784",
  "target": "00333a38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333a38",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "c0c26a00987a0900",
  "capture_start": "00333a38",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aea784`](#insn-00aea784)

~~~json
{
  "source": "00aea784",
  "target": "00333a3c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333a38",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "c0c26a00987a0900",
  "capture_start": "00333a38",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aea788`](#insn-00aea788)

~~~json
{
  "source": "00aea788",
  "target": "00333a90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333a90",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "d8c96a00887b0900",
  "capture_start": "00333a90",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aea788`](#insn-00aea788)

~~~json
{
  "source": "00aea788",
  "target": "00333a94",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333a90",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "d8c96a00887b0900",
  "capture_start": "00333a90",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aea7a0`](#insn-00aea7a0)

~~~json
{
  "source": "00aea7a0",
  "target": "00aea83c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea7b0`](#insn-00aea7b0)

~~~json
{
  "source": "00aea7b0",
  "target": "0039b97c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039b97c",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "348b5000",
  "capture_start": "0039b97c",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aea800`](#insn-00aea800)

~~~json
{
  "source": "00aea800",
  "target": "005c04b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea804`](#insn-00aea804)

~~~json
{
  "source": "00aea804",
  "target": "00aea858",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea820`](#insn-00aea820)

~~~json
{
  "source": "00aea820",
  "target": "00333a38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333a38",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "c0c26a00987a0900",
  "capture_start": "00333a38",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aea820`](#insn-00aea820)

~~~json
{
  "source": "00aea820",
  "target": "00333a3c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333a38",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "c0c26a00987a0900",
  "capture_start": "00333a38",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aea824`](#insn-00aea824)

~~~json
{
  "source": "00aea824",
  "target": "00333a90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333a90",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "d8c96a00887b0900",
  "capture_start": "00333a90",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aea824`](#insn-00aea824)

~~~json
{
  "source": "00aea824",
  "target": "00333a94",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333a90",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "d8c96a00887b0900",
  "capture_start": "00333a90",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aea83c`](#insn-00aea83c)

~~~json
{
  "source": "00aea83c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea840`](#insn-00aea840)

~~~json
{
  "source": "00aea840",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea844`](#insn-00aea844)

~~~json
{
  "source": "00aea844",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea848`](#insn-00aea848)

~~~json
{
  "source": "00aea848",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea84c`](#insn-00aea84c)

~~~json
{
  "source": "00aea84c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea850`](#insn-00aea850)

~~~json
{
  "source": "00aea850",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea854`](#insn-00aea854)

~~~json
{
  "source": "00aea854",
  "target": "00468f48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea858`](#insn-00aea858)

~~~json
{
  "source": "00aea858",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea85c`](#insn-00aea85c)

~~~json
{
  "source": "00aea85c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea860`](#insn-00aea860)

~~~json
{
  "source": "00aea860",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea864`](#insn-00aea864)

~~~json
{
  "source": "00aea864",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea868`](#insn-00aea868)

~~~json
{
  "source": "00aea868",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea86c`](#insn-00aea86c)

~~~json
{
  "source": "00aea86c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
