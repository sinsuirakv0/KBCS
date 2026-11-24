# 009bfdcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `009bee20`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009be/009bee20.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0059.md#compare-ce418602beed6fb297723eaa58fa4d1c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009bfdcc",
  "name": "FUN_009bfdcc",
  "size": 1096,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f48f40826f1bc3d2697e59dba8ffe363602ddfbf3d55df2a29c35ae049ebdb9b",
  "source_text_sha256": "f48f40826f1bc3d2697e59dba8ffe363602ddfbf3d55df2a29c35ae049ebdb9b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009bfdcc",
        "009c0213"
      ]
    ],
    "bytes_sha256": "bda0a9b4e7c29e8175f140bdf318a956d0809c4962d1e7d66458fb5cb1780b75",
    "instruction_count": 274,
    "instruction_bytes": 1096,
    "body_bytes": 1096,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0085ab5c](../0085a/0085ab5c.md)

## 呼び出し先

- [00467ec0](../00467/00467ec0.md)
- [00468f3c](../00468/00468f3c.md)
- [00468fc0](../00468/00468fc0.md)
- [004692e8](../00469/004692e8.md)
- [00469f64](../00469/00469f64.md)
- [0046cd24](../0046c/0046cd24.md)
- [0046cde4](../0046c/0046cde4.md)
- [0046dcd4](../0046d/0046dcd4.md)
- [0046dd0c](../0046d/0046dd0c.md)
- [008524fc](../00852/008524fc.md)
- [008624b4](../00862/008624b4.md)
- [009bf2e0](../009bf/009bf2e0.md)
- [00aca7e0](../00aca/00aca7e0.md)
- [00c596b0](../00c59/00c596b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6207 bytes

~~~c

void FUN_009bfdcc(long param_1,undefined8 param_2)

{
  int *piVar1;
  uint uVar2;
  int iVar3;
  int iVar4;
  uint uVar5;
  undefined *puVar6;
  int iVar7;
  undefined4 uVar8;
  long lVar9;
  undefined8 uVar10;
  float fVar11;
  
                    /* try { // try from 009bfde4 to 00abfe73 has its CatchHandler @ 009beb04 */
  if ((DAT_00ca5a38 != 0) &&
     (lVar9 = __dynamic_cast(DAT_00ca5a38,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c66ef8,
                             &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c8a720,0),
     lVar9 != 0)) {
    piVar1 = (int *)((long)&fde_table_entry_00333cc8.data_loc + param_1);
    FUN_00467ec0(param_2,0x5c,0x9a,0x4a,0xff);
    uVar10 = *(undefined8 *)(lVar9 + 0x108);
    iVar7 = FUN_0046cd24(param_1);
    FUN_008524fc();
    uVar8 = FUN_0046cde4();
                    /* try { // try from 009bfe74 to 00abfe77 has its CatchHandler @ 009c0358 */
    FUN_00469f64(param_2,uVar10,0xffffffd8,0,iVar7 + 0x50,uVar8,0);
                    /* try { // try from 009bfe9c to 00abfecf has its CatchHandler @ 009c0338 */
    FUN_00467ec0(param_2,0x6e,0xa6,0x59,0xff);
    fVar11 = (float)FUN_0046dd0c((float)*(int *)((long)&fde_table_entry_00333f98.data_loc + param_1)
                                );
                    /* try { // try from 009bfed0 to 00abffdb has its CatchHandler @ 009beb04 */
    FUN_00468f3c(param_2,(int)(fVar11 * 115.0) + 0x8c);
    uVar10 = *(undefined8 *)(lVar9 + 0x118);
    uVar8 = FUN_0046cd24(param_1);
    FUN_00469f64(param_2,uVar10,0,0,uVar8,0x330,0);
    FUN_00467ec0(param_2,0xff,0xff,0xff,0xff);
    FUN_00468fc0(param_2,0);
    FUN_008624b4(param_1,*(undefined8 *)(lVar9 + 200),0,0);
    uVar10 = *(undefined8 *)(lVar9 + 200);
    uVar8 = FUN_0046cd24(param_1);
    FUN_00469f64(param_2,uVar10,0,0,uVar8,0x37,0);
    FUN_00468fc0(param_2,2);
    uVar10 = *(undefined8 *)(lVar9 + 200);
    uVar8 = FUN_0046cd24(param_1);
    FUN_00469f64(param_2,uVar10,0,0x249,uVar8,0x37,0);
    FUN_00468fc0(param_2,0);
    FUN_004692e8(param_2,*(undefined8 *)(lVar9 + 0x108),
                 8 - *(int *)((long)&fde_table_entry_00334170.initial_loc + param_1),3,6);
                    /* try { // try from 009bffdc to 00abfff3 has its CatchHandler @ 009c0330 */
    if (((((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1) & 1) == 0) &&
         ((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 1) & 1) == 0)) &&
        ((*(byte *)((long)&fde_table_entry_00332a28.data_loc + param_1 + 1) & 1) == 0)) &&
       ((((*(byte *)((long)&fde_table_entry_00332a30.initial_loc + param_1 + 1) & 1) == 0 &&
         ((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 2) & 1) == 0)) &&
        (((*(byte *)((long)&fde_table_entry_00332060.initial_loc + param_1) & 1) == 0 &&
         (*(char *)((long)&fde_table_entry_00332a28.data_loc + param_1 + 2) != '\0')))))) {
      uVar2 = *(uint *)((long)&fde_table_entry_00333f98.initial_loc + param_1);
      uVar5 = -uVar2;
                    /* try { // try from 009c0018 to 00ac0053 has its CatchHandler @ 009c039c */
      uVar2 = uVar2 & 3;
      if (-1 < (int)uVar5) {
        uVar2 = -(uVar5 & 3);
      }
      FUN_00469f64(param_2,*(undefined8 *)(lVar9 + 0xa8),3,0x21c,0x60,0x60,
                   ((uint)(int)(char)((char)uVar2 + (char)((uVar2 & 0x80) >> 7)) >> 1) + 0xc & 0xff)
      ;
    }
    puVar6 = PTR_DAT_00c9c548;
                    /* try { // try from 009c0054 to 00ac019f has its CatchHandler @ 009beb04 */
    iVar3 = *(int *)(PTR_DAT_00c9c548 +
                    (long)*(int *)((long)&fde_table_entry_00333dc0.initial_loc + param_1) * 4);
    iVar7 = iVar3;
    if (iVar3 < 0) {
      iVar7 = iVar3 + 1;
    }
    FUN_00469f64(param_2,*(undefined8 *)(lVar9 + 0xa8),*piVar1 - (iVar7 >> 1),
                 *(int *)((long)&fde_table_entry_00333cd0.initial_loc + param_1) - (iVar7 >> 1),
                 *(int *)((long)&fde_table_entry_00333cd0.data_loc + param_1) + iVar3,
                 *(int *)((long)&fde_table_entry_00333cd8.initial_loc + param_1) + iVar3,9);
    iVar4 = *(int *)(puVar6 + (long)*(int *)((long)&fde_table_entry_00333dc0.initial_loc + param_1)
                              * 4);
    iVar7 = iVar4 + 0x54;
    iVar3 = iVar4 + 0x3c;
    if (iVar4 < 0) {
      iVar4 = iVar4 + 1;
    }
    FUN_00469f64(param_2,*(undefined8 *)(lVar9 + 0xa8),(*piVar1 - (iVar4 >> 1)) + 4,
                 (*(int *)((long)&fde_table_entry_00333cd0.initial_loc + param_1) - (iVar4 >> 1)) +
                 0x11,iVar7,iVar3,3);
    FUN_00aca7e0((long)&fde_table_entry_00337d90.initial_loc + param_1,
                 *(undefined8 *)(lVar9 + 0x138),*(undefined8 *)(lVar9 + 0x178));
    FUN_00467ec0(param_2,0xff,0xff,0xff,0xff);
    FUN_00468f3c(param_2,0x72);
    if (0 < *(int *)((long)&fde_table_entry_00337670.initial_loc + param_1)) {
      uVar10 = *(undefined8 *)(lVar9 + 0xa8);
      fVar11 = (float)FUN_0046dcd4((float)(*(int *)((long)&fde_table_entry_00333f98.initial_loc +
                                                   param_1) * 0x1e));
      FUN_004692e8(param_2,uVar10,(int)(fVar11 * 10.0 + 24.0),0x11a,8);
    }
    FUN_00468fc0(param_2,1);
    if (*(int *)((long)&fde_table_entry_00337670.initial_loc + param_1) <
        *(int *)((long)&fde_table_entry_00335f78.initial_loc + param_1) + -1) {
      uVar10 = *(undefined8 *)(lVar9 + 0xa8);
      iVar7 = FUN_0046cd24(param_1);
      fVar11 = (float)FUN_0046dcd4((float)(*(int *)((long)&fde_table_entry_00333f98.initial_loc +
                                                   param_1) * 0x1e));
                    /* try { // try from 009c01a0 to 00ac01ab has its CatchHandler @ 009c0524 */
      FUN_004692e8(param_2,uVar10,(int)((float)(iVar7 + -0x56) + fVar11 * -10.0),0x11a,8);
    }
    FUN_00468fc0(param_2,0);
                    /* try { // try from 009c01c0 to 00ac01df has its CatchHandler @ 009c0418 */
    FUN_00468f3c(param_2,0xff);
    FUN_009bf2e0((long)&fde_table_entry_00337630.initial_loc + param_1);
    return;
  }
                    /* try { // try from 009c01f4 to 00ac01fb has its CatchHandler @ 009c03f4 */
                    /* try { // try from 009c0210 to 00ac0217 has its CatchHandler @ 009c03f0 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009bfdcc"></a> `009bfdcc` | `e8 0f 1a fc` | str d8,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-009bfdd0"></a> `009bfdd0` | `fd fb 00 a9` | stp x29,x30,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009bfdd4"></a> `009bfdd4` | `fb 0f 00 f9` | str x27,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009bfdd8"></a> `009bfdd8` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009bfddc"></a> `009bfddc` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009bfde0"></a> `009bfde0` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009bfde4"></a> `009bfde4` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009bfde8"></a> `009bfde8` | `fd 23 00 91` | add x29,sp,#0x8 | `FALL_THROUGH`
<a id="insn-009bfdec"></a> `009bfdec` | `28 17 00 d0` | adrp x8,0xca5000 | `FALL_THROUGH`
<a id="insn-009bfdf0"></a> `009bfdf0` | `08 1d 45 f9` | ldr x8,[x8, #0xa38] | `FALL_THROUGH`
<a id="insn-009bfdf4"></a> `009bfdf4` | `08 20 00 b4` | cbz x8,0x009c01f4 | `CONDITIONAL_JUMP`
<a id="insn-009bfdf8"></a> `009bfdf8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-009bfdfc"></a> `009bfdfc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-009bfe00"></a> `009bfe00` | `21 15 00 f0` | adrp x1,0xc66000 | `FALL_THROUGH`
<a id="insn-009bfe04"></a> `009bfe04` | `21 e0 3b 91` | add x1,x1,#0xef8 | `FALL_THROUGH`
<a id="insn-009bfe08"></a> `009bfe08` | `42 16 00 f0` | adrp x2,0xc8a000 | `FALL_THROUGH`
<a id="insn-009bfe0c"></a> `009bfe0c` | `42 80 1c 91` | add x2,x2,#0x720 | `FALL_THROUGH`
<a id="insn-009bfe10"></a> `009bfe10` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-009bfe14"></a> `009bfe14` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-009bfe18"></a> `009bfe18` | `26 66 0a 94` | bl 0x00c596b0 | `UNCONDITIONAL_CALL`
<a id="insn-009bfe1c"></a> `009bfe1c` | `c0 1e 00 b4` | cbz x0,0x009c01f4 | `CONDITIONAL_JUMP`
<a id="insn-009bfe20"></a> `009bfe20` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-009bfe24"></a> `009bfe24` | `19 ce 8e 52` | mov w25,#0x7670 | `FALL_THROUGH`
<a id="insn-009bfe28"></a> `009bfe28` | `68 ce 4c 91` | add x8,x19,#0x333, LSL #12 | `FALL_THROUGH`
<a id="insn-009bfe2c"></a> `009bfe2c` | `69 ca 4c 91` | add x9,x19,#0x332, LSL #12 | `FALL_THROUGH`
<a id="insn-009bfe30"></a> `009bfe30` | `1a ef 8b 52` | mov w26,#0x5f78 | `FALL_THROUGH`
<a id="insn-009bfe34"></a> `009bfe34` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bfe38"></a> `009bfe38` | `81 0b 80 52` | mov w1,#0x5c | `FALL_THROUGH`
<a id="insn-009bfe3c"></a> `009bfe3c` | `42 13 80 52` | mov w2,#0x9a | `FALL_THROUGH`
<a id="insn-009bfe40"></a> `009bfe40` | `43 09 80 52` | mov w3,#0x4a | `FALL_THROUGH`
<a id="insn-009bfe44"></a> `009bfe44` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-009bfe48"></a> `009bfe48` | `79 06 a0 72` | movk w25,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-009bfe4c"></a> `009bfe4c` | `7a 06 a0 72` | movk w26,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-009bfe50"></a> `009bfe50` | `18 31 33 91` | add x24,x8,#0xccc | `FALL_THROUGH`
<a id="insn-009bfe54"></a> `009bfe54` | `3b 81 01 91` | add x27,x9,#0x60 | `FALL_THROUGH`
<a id="insn-009bfe58"></a> `009bfe58` | `1a a0 ea 97` | bl 0x00467ec0 | `UNCONDITIONAL_CALL`
<a id="insn-009bfe5c"></a> `009bfe5c` | `b6 86 40 f9` | ldr x22,[x21, #0x108] | `FALL_THROUGH`
<a id="insn-009bfe60"></a> `009bfe60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009bfe64"></a> `009bfe64` | `b0 b3 ea 97` | bl 0x0046cd24 | `UNCONDITIONAL_CALL`
<a id="insn-009bfe68"></a> `009bfe68` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-009bfe6c"></a> `009bfe6c` | `a4 49 fa 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-009bfe70"></a> `009bfe70` | `dd b3 ea 97` | bl 0x0046cde4 | `UNCONDITIONAL_CALL`
<a id="insn-009bfe74"></a> `009bfe74` | `e5 03 00 2a` | mov w5,w0 | `FALL_THROUGH`
<a id="insn-009bfe78"></a> `009bfe78` | `e4 42 01 11` | add w4,w23,#0x50 | `FALL_THROUGH`
<a id="insn-009bfe7c"></a> `009bfe7c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bfe80"></a> `009bfe80` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-009bfe84"></a> `009bfe84` | `e2 04 80 12` | mov w2,#0xffffffd8 | `FALL_THROUGH`
<a id="insn-009bfe88"></a> `009bfe88` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-009bfe8c"></a> `009bfe8c` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-009bfe90"></a> `009bfe90` | `35 a8 ea 97` | bl 0x00469f64 | `UNCONDITIONAL_CALL`
<a id="insn-009bfe94"></a> `009bfe94` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bfe98"></a> `009bfe98` | `c1 0d 80 52` | mov w1,#0x6e | `FALL_THROUGH`
<a id="insn-009bfe9c"></a> `009bfe9c` | `c2 14 80 52` | mov w2,#0xa6 | `FALL_THROUGH`
<a id="insn-009bfea0"></a> `009bfea0` | `23 0b 80 52` | mov w3,#0x59 | `FALL_THROUGH`
<a id="insn-009bfea4"></a> `009bfea4` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-009bfea8"></a> `009bfea8` | `06 a0 ea 97` | bl 0x00467ec0 | `UNCONDITIONAL_CALL`
<a id="insn-009bfeac"></a> `009bfeac` | `00 d3 42 bd` | ldr s0,[x24, #0x2d0] | `FALL_THROUGH`
<a id="insn-009bfeb0"></a> `009bfeb0` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-009bfeb4"></a> `009bfeb4` | `96 b7 ea 97` | bl 0x0046dd0c | `UNCONDITIONAL_CALL`
<a id="insn-009bfeb8"></a> `009bfeb8` | `c8 5c a8 52` | mov w8,#0x42e60000 | `FALL_THROUGH`
<a id="insn-009bfebc"></a> `009bfebc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bfec0"></a> `009bfec0` | `01 01 27 1e` | fmov s1,w8 | `FALL_THROUGH`
<a id="insn-009bfec4"></a> `009bfec4` | `00 08 21 1e` | fmul s0,s0,s1 | `FALL_THROUGH`
<a id="insn-009bfec8"></a> `009bfec8` | `08 00 38 1e` | fcvtzs w8,s0 | `FALL_THROUGH`
<a id="insn-009bfecc"></a> `009bfecc` | `01 31 02 11` | add w1,w8,#0x8c | `FALL_THROUGH`
<a id="insn-009bfed0"></a> `009bfed0` | `1b a4 ea 97` | bl 0x00468f3c | `UNCONDITIONAL_CALL`
<a id="insn-009bfed4"></a> `009bfed4` | `b6 8e 40 f9` | ldr x22,[x21, #0x118] | `FALL_THROUGH`
<a id="insn-009bfed8"></a> `009bfed8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009bfedc"></a> `009bfedc` | `92 b3 ea 97` | bl 0x0046cd24 | `UNCONDITIONAL_CALL`
<a id="insn-009bfee0"></a> `009bfee0` | `e4 03 00 2a` | mov w4,w0 | `FALL_THROUGH`
<a id="insn-009bfee4"></a> `009bfee4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bfee8"></a> `009bfee8` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-009bfeec"></a> `009bfeec` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-009bfef0"></a> `009bfef0` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-009bfef4"></a> `009bfef4` | `05 66 80 52` | mov w5,#0x330 | `FALL_THROUGH`
<a id="insn-009bfef8"></a> `009bfef8` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-009bfefc"></a> `009bfefc` | `1a a8 ea 97` | bl 0x00469f64 | `UNCONDITIONAL_CALL`
<a id="insn-009bff00"></a> `009bff00` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bff04"></a> `009bff04` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-009bff08"></a> `009bff08` | `e2 1f 80 52` | mov w2,#0xff | `FALL_THROUGH`
<a id="insn-009bff0c"></a> `009bff0c` | `e3 1f 80 52` | mov w3,#0xff | `FALL_THROUGH`
<a id="insn-009bff10"></a> `009bff10` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-009bff14"></a> `009bff14` | `eb 9f ea 97` | bl 0x00467ec0 | `UNCONDITIONAL_CALL`
<a id="insn-009bff18"></a> `009bff18` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bff1c"></a> `009bff1c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-009bff20"></a> `009bff20` | `28 a4 ea 97` | bl 0x00468fc0 | `UNCONDITIONAL_CALL`
<a id="insn-009bff24"></a> `009bff24` | `a1 66 40 f9` | ldr x1,[x21, #0xc8] | `FALL_THROUGH`
<a id="insn-009bff28"></a> `009bff28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009bff2c"></a> `009bff2c` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-009bff30"></a> `009bff30` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-009bff34"></a> `009bff34` | `60 89 fa 97` | bl 0x008624b4 | `UNCONDITIONAL_CALL`
<a id="insn-009bff38"></a> `009bff38` | `b6 66 40 f9` | ldr x22,[x21, #0xc8] | `FALL_THROUGH`
<a id="insn-009bff3c"></a> `009bff3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009bff40"></a> `009bff40` | `79 b3 ea 97` | bl 0x0046cd24 | `UNCONDITIONAL_CALL`
<a id="insn-009bff44"></a> `009bff44` | `e4 03 00 2a` | mov w4,w0 | `FALL_THROUGH`
<a id="insn-009bff48"></a> `009bff48` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bff4c"></a> `009bff4c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-009bff50"></a> `009bff50` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-009bff54"></a> `009bff54` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-009bff58"></a> `009bff58` | `e5 06 80 52` | mov w5,#0x37 | `FALL_THROUGH`
<a id="insn-009bff5c"></a> `009bff5c` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-009bff60"></a> `009bff60` | `01 a8 ea 97` | bl 0x00469f64 | `UNCONDITIONAL_CALL`
<a id="insn-009bff64"></a> `009bff64` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bff68"></a> `009bff68` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-009bff6c"></a> `009bff6c` | `15 a4 ea 97` | bl 0x00468fc0 | `UNCONDITIONAL_CALL`
<a id="insn-009bff70"></a> `009bff70` | `b6 66 40 f9` | ldr x22,[x21, #0xc8] | `FALL_THROUGH`
<a id="insn-009bff74"></a> `009bff74` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009bff78"></a> `009bff78` | `6b b3 ea 97` | bl 0x0046cd24 | `UNCONDITIONAL_CALL`
<a id="insn-009bff7c"></a> `009bff7c` | `e4 03 00 2a` | mov w4,w0 | `FALL_THROUGH`
<a id="insn-009bff80"></a> `009bff80` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bff84"></a> `009bff84` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-009bff88"></a> `009bff88` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-009bff8c"></a> `009bff8c` | `23 49 80 52` | mov w3,#0x249 | `FALL_THROUGH`
<a id="insn-009bff90"></a> `009bff90` | `e5 06 80 52` | mov w5,#0x37 | `FALL_THROUGH`
<a id="insn-009bff94"></a> `009bff94` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-009bff98"></a> `009bff98` | `f3 a7 ea 97` | bl 0x00469f64 | `UNCONDITIONAL_CALL`
<a id="insn-009bff9c"></a> `009bff9c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bffa0"></a> `009bffa0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-009bffa4"></a> `009bffa4` | `07 a4 ea 97` | bl 0x00468fc0 | `UNCONDITIONAL_CALL`
<a id="insn-009bffa8"></a> `009bffa8` | `08 a7 44 b9` | ldr w8,[x24, #0x4a4] | `FALL_THROUGH`
<a id="insn-009bffac"></a> `009bffac` | `a1 86 40 f9` | ldr x1,[x21, #0x108] | `FALL_THROUGH`
<a id="insn-009bffb0"></a> `009bffb0` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-009bffb4"></a> `009bffb4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bffb8"></a> `009bffb8` | `63 00 80 52` | mov w3,#0x3 | `FALL_THROUGH`
<a id="insn-009bffbc"></a> `009bffbc` | `c4 00 80 52` | mov w4,#0x6 | `FALL_THROUGH`
<a id="insn-009bffc0"></a> `009bffc0` | `22 01 08 4b` | sub w2,w9,w8 | `FALL_THROUGH`
<a id="insn-009bffc4"></a> `009bffc4` | `c9 a4 ea 97` | bl 0x004692e8 | `UNCONDITIONAL_CALL`
<a id="insn-009bffc8"></a> `009bffc8` | `68 13 67 39` | ldrb w8,[x27, #0x9c4] | `FALL_THROUGH`
<a id="insn-009bffcc"></a> `009bffcc` | `e8 03 00 37` | tbnz w8,#0x0,0x009c0048 | `CONDITIONAL_JUMP`
<a id="insn-009bffd0"></a> `009bffd0` | `68 17 67 39` | ldrb w8,[x27, #0x9c5] | `FALL_THROUGH`
<a id="insn-009bffd4"></a> `009bffd4` | `a8 03 00 37` | tbnz w8,#0x0,0x009c0048 | `CONDITIONAL_JUMP`
<a id="insn-009bffd8"></a> `009bffd8` | `68 37 67 39` | ldrb w8,[x27, #0x9cd] | `FALL_THROUGH`
<a id="insn-009bffdc"></a> `009bffdc` | `68 03 00 37` | tbnz w8,#0x0,0x009c0048 | `CONDITIONAL_JUMP`
<a id="insn-009bffe0"></a> `009bffe0` | `68 47 67 39` | ldrb w8,[x27, #0x9d1] | `FALL_THROUGH`
<a id="insn-009bffe4"></a> `009bffe4` | `28 03 00 37` | tbnz w8,#0x0,0x009c0048 | `CONDITIONAL_JUMP`
<a id="insn-009bffe8"></a> `009bffe8` | `68 1b 67 39` | ldrb w8,[x27, #0x9c6] | `FALL_THROUGH`
<a id="insn-009bffec"></a> `009bffec` | `e8 02 00 37` | tbnz w8,#0x0,0x009c0048 | `CONDITIONAL_JUMP`
<a id="insn-009bfff0"></a> `009bfff0` | `68 03 40 39` | ldrb w8,[x27] | `FALL_THROUGH`
<a id="insn-009bfff4"></a> `009bfff4` | `a8 02 00 37` | tbnz w8,#0x0,0x009c0048 | `CONDITIONAL_JUMP`
<a id="insn-009bfff8"></a> `009bfff8` | `68 3b 67 39` | ldrb w8,[x27, #0x9ce] | `FALL_THROUGH`
<a id="insn-009bfffc"></a> `009bfffc` | `68 02 00 34` | cbz w8,0x009c0048 | `CONDITIONAL_JUMP`
<a id="insn-009c0000"></a> `009c0000` | `08 cf 42 b9` | ldr w8,[x24, #0x2cc] | `FALL_THROUGH`
<a id="insn-009c0004"></a> `009c0004` | `a1 56 40 f9` | ldr x1,[x21, #0xa8] | `FALL_THROUGH`
<a id="insn-009c0008"></a> `009c0008` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009c000c"></a> `009c000c` | `62 00 80 52` | mov w2,#0x3 | `FALL_THROUGH`
<a id="insn-009c0010"></a> `009c0010` | `83 43 80 52` | mov w3,#0x21c | `FALL_THROUGH`
<a id="insn-009c0014"></a> `009c0014` | `04 0c 80 52` | mov w4,#0x60 | `FALL_THROUGH`
<a id="insn-009c0018"></a> `009c0018` | `e9 03 08 6b` | negs w9,w8 | `FALL_THROUGH`
<a id="insn-009c001c"></a> `009c001c` | `08 05 00 12` | and w8,w8,#0x3 | `FALL_THROUGH`
<a id="insn-009c0020"></a> `009c0020` | `05 0c 80 52` | mov w5,#0x60 | `FALL_THROUGH`
<a id="insn-009c0024"></a> `009c0024` | `29 05 00 12` | and w9,w9,#0x3 | `FALL_THROUGH`
<a id="insn-009c0028"></a> `009c0028` | `08 45 89 5a` | csneg w8,w8,w9,mi | `FALL_THROUGH`
<a id="insn-009c002c"></a> `009c002c` | `09 01 19 12` | and w9,w8,#0x80 | `FALL_THROUGH`
<a id="insn-009c0030"></a> `009c0030` | `08 1d 49 0b` | add w8,w8,w9, LSR #0x7 | `FALL_THROUGH`
<a id="insn-009c0034"></a> `009c0034` | `08 1d 00 13` | sxtb w8,w8 | `FALL_THROUGH`
<a id="insn-009c0038"></a> `009c0038` | `08 7d 01 53` | lsr w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-009c003c"></a> `009c003c` | `08 31 00 11` | add w8,w8,#0xc | `FALL_THROUGH`
<a id="insn-009c0040"></a> `009c0040` | `06 1d 00 12` | and w6,w8,#0xff | `FALL_THROUGH`
<a id="insn-009c0044"></a> `009c0044` | `c8 a7 ea 97` | bl 0x00469f64 | `UNCONDITIONAL_CALL`
<a id="insn-009c0048"></a> `009c0048` | `f6 16 00 90` | adrp x22,0xc9c000 | `FALL_THROUGH`
<a id="insn-009c004c"></a> `009c004c` | `08 f7 80 b9` | ldrsw x8,[x24, #0xf4] | `FALL_THROUGH`
<a id="insn-009c0050"></a> `009c0050` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009c0054"></a> `009c0054` | `d6 a6 42 f9` | ldr x22,[x22, #0x548] | `FALL_THROUGH`
<a id="insn-009c0058"></a> `009c0058` | `a1 56 40 f9` | ldr x1,[x21, #0xa8] | `FALL_THROUGH`
<a id="insn-009c005c"></a> `009c005c` | `26 01 80 52` | mov w6,#0x9 | `FALL_THROUGH`
<a id="insn-009c0060"></a> `009c0060` | `0a 2f 40 29` | ldp w10,w11,[x24] | `FALL_THROUGH`
<a id="insn-009c0064"></a> `009c0064` | `c8 7a 68 b8` | ldr w8,[x22, x8, LSL #0x2] | `FALL_THROUGH`
<a id="insn-009c0068"></a> `009c0068` | `0c 37 41 29` | ldp w12,w13,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-009c006c"></a> `009c006c` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-009c0070"></a> `009c0070` | `09 a5 88 1a` | cinc w9,w8,lt | `FALL_THROUGH`
<a id="insn-009c0074"></a> `009c0074` | `29 7d 01 13` | asr w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-009c0078"></a> `009c0078` | `84 01 08 0b` | add w4,w12,w8 | `FALL_THROUGH`
<a id="insn-009c007c"></a> `009c007c` | `a5 01 08 0b` | add w5,w13,w8 | `FALL_THROUGH`
<a id="insn-009c0080"></a> `009c0080` | `42 01 09 4b` | sub w2,w10,w9 | `FALL_THROUGH`
<a id="insn-009c0084"></a> `009c0084` | `63 01 09 4b` | sub w3,w11,w9 | `FALL_THROUGH`
<a id="insn-009c0088"></a> `009c0088` | `b7 a7 ea 97` | bl 0x00469f64 | `UNCONDITIONAL_CALL`
<a id="insn-009c008c"></a> `009c008c` | `08 f7 80 b9` | ldrsw x8,[x24, #0xf4] | `FALL_THROUGH`
<a id="insn-009c0090"></a> `009c0090` | `a1 56 40 f9` | ldr x1,[x21, #0xa8] | `FALL_THROUGH`
<a id="insn-009c0094"></a> `009c0094` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009c0098"></a> `009c0098` | `0a 2f 40 29` | ldp w10,w11,[x24] | `FALL_THROUGH`
<a id="insn-009c009c"></a> `009c009c` | `c8 7a 68 b8` | ldr w8,[x22, x8, LSL #0x2] | `FALL_THROUGH`
<a id="insn-009c00a0"></a> `009c00a0` | `66 00 80 52` | mov w6,#0x3 | `FALL_THROUGH`
<a id="insn-009c00a4"></a> `009c00a4` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-009c00a8"></a> `009c00a8` | `04 51 01 11` | add w4,w8,#0x54 | `FALL_THROUGH`
<a id="insn-009c00ac"></a> `009c00ac` | `05 f1 00 11` | add w5,w8,#0x3c | `FALL_THROUGH`
<a id="insn-009c00b0"></a> `009c00b0` | `09 a5 88 1a` | cinc w9,w8,lt | `FALL_THROUGH`
<a id="insn-009c00b4"></a> `009c00b4` | `29 7d 01 13` | asr w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-009c00b8"></a> `009c00b8` | `4a 01 09 4b` | sub w10,w10,w9 | `FALL_THROUGH`
<a id="insn-009c00bc"></a> `009c00bc` | `69 01 09 4b` | sub w9,w11,w9 | `FALL_THROUGH`
<a id="insn-009c00c0"></a> `009c00c0` | `42 11 00 11` | add w2,w10,#0x4 | `FALL_THROUGH`
<a id="insn-009c00c4"></a> `009c00c4` | `23 45 00 11` | add w3,w9,#0x11 | `FALL_THROUGH`
<a id="insn-009c00c8"></a> `009c00c8` | `a7 a7 ea 97` | bl 0x00469f64 | `UNCONDITIONAL_CALL`
<a id="insn-009c00cc"></a> `009c00cc` | `a1 9e 40 f9` | ldr x1,[x21, #0x138] | `FALL_THROUGH`
<a id="insn-009c00d0"></a> `009c00d0` | `a2 be 40 f9` | ldr x2,[x21, #0x178] | `FALL_THROUGH`
<a id="insn-009c00d4"></a> `009c00d4` | `68 de 4c 91` | add x8,x19,#0x337, LSL #12 | `FALL_THROUGH`
<a id="insn-009c00d8"></a> `009c00d8` | `00 41 36 91` | add x0,x8,#0xd90 | `FALL_THROUGH`
<a id="insn-009c00dc"></a> `009c00dc` | `c1 29 04 94` | bl 0x00aca7e0 | `UNCONDITIONAL_CALL`
<a id="insn-009c00e0"></a> `009c00e0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009c00e4"></a> `009c00e4` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-009c00e8"></a> `009c00e8` | `e2 1f 80 52` | mov w2,#0xff | `FALL_THROUGH`
<a id="insn-009c00ec"></a> `009c00ec` | `e3 1f 80 52` | mov w3,#0xff | `FALL_THROUGH`
<a id="insn-009c00f0"></a> `009c00f0` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-009c00f4"></a> `009c00f4` | `73 9f ea 97` | bl 0x00467ec0 | `UNCONDITIONAL_CALL`
<a id="insn-009c00f8"></a> `009c00f8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009c00fc"></a> `009c00fc` | `41 0e 80 52` | mov w1,#0x72 | `FALL_THROUGH`
<a id="insn-009c0100"></a> `009c0100` | `8f a3 ea 97` | bl 0x00468f3c | `UNCONDITIONAL_CALL`
<a id="insn-009c0104"></a> `009c0104` | `68 6a 79 b8` | ldr w8,[x19, x25, LSL #0x0] | `FALL_THROUGH`
<a id="insn-009c0108"></a> `009c0108` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-009c010c"></a> `009c010c` | `0b 02 00 54` | b.lt 0x009c014c | `CONDITIONAL_JUMP`
<a id="insn-009c0110"></a> `009c0110` | `08 cf 42 b9` | ldr w8,[x24, #0x2cc] | `FALL_THROUGH`
<a id="insn-009c0114"></a> `009c0114` | `b6 56 40 f9` | ldr x22,[x21, #0xa8] | `FALL_THROUGH`
<a id="insn-009c0118"></a> `009c0118` | `09 69 1b 53` | lsl w9,w8,#0x5 | `FALL_THROUGH`
<a id="insn-009c011c"></a> `009c011c` | `28 05 08 4b` | sub w8,w9,w8, LSL #0x1 | `FALL_THROUGH`
<a id="insn-009c0120"></a> `009c0120` | `00 01 22 1e` | scvtf s0,w8 | `FALL_THROUGH`
<a id="insn-009c0124"></a> `009c0124` | `ec b6 ea 97` | bl 0x0046dcd4 | `UNCONDITIONAL_CALL`
<a id="insn-009c0128"></a> `009c0128` | `01 10 27 1e` | fmov s1,0x41c00000 | `FALL_THROUGH`
<a id="insn-009c012c"></a> `009c012c` | `02 90 24 1e` | fmov s2,0x41200000 | `FALL_THROUGH`
<a id="insn-009c0130"></a> `009c0130` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009c0134"></a> `009c0134` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-009c0138"></a> `009c0138` | `43 23 80 52` | mov w3,#0x11a | `FALL_THROUGH`
<a id="insn-009c013c"></a> `009c013c` | `04 01 80 52` | mov w4,#0x8 | `FALL_THROUGH`
<a id="insn-009c0140"></a> `009c0140` | `00 04 02 1f` | fmadd s0,s0,s2,s1 | `FALL_THROUGH`
<a id="insn-009c0144"></a> `009c0144` | `02 00 38 1e` | fcvtzs w2,s0 | `FALL_THROUGH`
<a id="insn-009c0148"></a> `009c0148` | `68 a4 ea 97` | bl 0x004692e8 | `UNCONDITIONAL_CALL`
<a id="insn-009c014c"></a> `009c014c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009c0150"></a> `009c0150` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-009c0154"></a> `009c0154` | `9b a3 ea 97` | bl 0x00468fc0 | `UNCONDITIONAL_CALL`
<a id="insn-009c0158"></a> `009c0158` | `68 6a 7a b8` | ldr w8,[x19, x26, LSL #0x0] | `FALL_THROUGH`
<a id="insn-009c015c"></a> `009c015c` | `69 6a 79 b8` | ldr w9,[x19, x25, LSL #0x0] | `FALL_THROUGH`
<a id="insn-009c0160"></a> `009c0160` | `08 05 00 51` | sub w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-009c0164"></a> `009c0164` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-009c0168"></a> `009c0168` | `6a 02 00 54` | b.ge 0x009c01b4 | `CONDITIONAL_JUMP`
<a id="insn-009c016c"></a> `009c016c` | `b5 56 40 f9` | ldr x21,[x21, #0xa8] | `FALL_THROUGH`
<a id="insn-009c0170"></a> `009c0170` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009c0174"></a> `009c0174` | `ec b2 ea 97` | bl 0x0046cd24 | `UNCONDITIONAL_CALL`
<a id="insn-009c0178"></a> `009c0178` | `08 cf 42 b9` | ldr w8,[x24, #0x2cc] | `FALL_THROUGH`
<a id="insn-009c017c"></a> `009c017c` | `09 58 01 51` | sub w9,w0,#0x56 | `FALL_THROUGH`
<a id="insn-009c0180"></a> `009c0180` | `28 01 22 1e` | scvtf s8,w9 | `FALL_THROUGH`
<a id="insn-009c0184"></a> `009c0184` | `0a 69 1b 53` | lsl w10,w8,#0x5 | `FALL_THROUGH`
<a id="insn-009c0188"></a> `009c0188` | `48 05 08 4b` | sub w8,w10,w8, LSL #0x1 | `FALL_THROUGH`
<a id="insn-009c018c"></a> `009c018c` | `00 01 22 1e` | scvtf s0,w8 | `FALL_THROUGH`
<a id="insn-009c0190"></a> `009c0190` | `d1 b6 ea 97` | bl 0x0046dcd4 | `UNCONDITIONAL_CALL`
<a id="insn-009c0194"></a> `009c0194` | `01 90 34 1e` | fmov s1,0xc1200000 | `FALL_THROUGH`
<a id="insn-009c0198"></a> `009c0198` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009c019c"></a> `009c019c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-009c01a0"></a> `009c01a0` | `43 23 80 52` | mov w3,#0x11a | `FALL_THROUGH`
<a id="insn-009c01a4"></a> `009c01a4` | `04 01 80 52` | mov w4,#0x8 | `FALL_THROUGH`
<a id="insn-009c01a8"></a> `009c01a8` | `00 20 01 1f` | fmadd s0,s0,s1,s8 | `FALL_THROUGH`
<a id="insn-009c01ac"></a> `009c01ac` | `02 00 38 1e` | fcvtzs w2,s0 | `FALL_THROUGH`
<a id="insn-009c01b0"></a> `009c01b0` | `4e a4 ea 97` | bl 0x004692e8 | `UNCONDITIONAL_CALL`
<a id="insn-009c01b4"></a> `009c01b4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009c01b8"></a> `009c01b8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-009c01bc"></a> `009c01bc` | `81 a3 ea 97` | bl 0x00468fc0 | `UNCONDITIONAL_CALL`
<a id="insn-009c01c0"></a> `009c01c0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009c01c4"></a> `009c01c4` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-009c01c8"></a> `009c01c8` | `5d a3 ea 97` | bl 0x00468f3c | `UNCONDITIONAL_CALL`
<a id="insn-009c01cc"></a> `009c01cc` | `68 de 4c 91` | add x8,x19,#0x337, LSL #12 | `FALL_THROUGH`
<a id="insn-009c01d0"></a> `009c01d0` | `00 c1 18 91` | add x0,x8,#0x630 | `FALL_THROUGH`
<a id="insn-009c01d4"></a> `009c01d4` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009c01d8"></a> `009c01d8` | `fb 0f 40 f9` | ldr x27,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009c01dc"></a> `009c01dc` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009c01e0"></a> `009c01e0` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009c01e4"></a> `009c01e4` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009c01e8"></a> `009c01e8` | `fd fb 40 a9` | ldp x29,x30,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009c01ec"></a> `009c01ec` | `e8 07 46 fc` | ldr d8,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-009c01f0"></a> `009c01f0` | `3c fc ff 17` | b 0x009bf2e0 | `CALL_TERMINATOR`
<a id="insn-009c01f4"></a> `009c01f4` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009c01f8"></a> `009c01f8` | `fb 0f 40 f9` | ldr x27,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009c01fc"></a> `009c01fc` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009c0200"></a> `009c0200` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009c0204"></a> `009c0204` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009c0208"></a> `009c0208` | `fd fb 40 a9` | ldp x29,x30,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009c020c"></a> `009c020c` | `e8 07 46 fc` | ldr d8,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-009c0210"></a> `009c0210` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009bfdcc`](#insn-009bfdcc) 範囲 `[['009bfdcc', '009bfde3']]`
  - `FALL_THROUGH` [`009bfde0`](#insn-009bfde0) → [`009bfde4`](#insn-009bfde4)
- ブロック [`009bfde4`](#insn-009bfde4) 範囲 `[['009bfde4', '009bfdf7']]`
  - `CONDITIONAL_JUMP` [`009bfdf4`](#insn-009bfdf4) → [`009c01f4`](#insn-009c01f4)
  - `FALL_THROUGH` [`009bfdf4`](#insn-009bfdf4) → [`009bfdf8`](#insn-009bfdf8)
- ブロック [`009bfdf8`](#insn-009bfdf8) 範囲 `[['009bfdf8', '009bfe1f']]`
  - `CONDITIONAL_JUMP` [`009bfe1c`](#insn-009bfe1c) → [`009c01f4`](#insn-009c01f4)
  - `FALL_THROUGH` [`009bfe1c`](#insn-009bfe1c) → [`009bfe20`](#insn-009bfe20)
- ブロック [`009bfe20`](#insn-009bfe20) 範囲 `[['009bfe20', '009bfe73']]`
  - `FALL_THROUGH` [`009bfe70`](#insn-009bfe70) → [`009bfe74`](#insn-009bfe74)
- ブロック [`009bfe74`](#insn-009bfe74) 範囲 `[['009bfe74', '009bfe9b']]`
  - `FALL_THROUGH` [`009bfe98`](#insn-009bfe98) → [`009bfe9c`](#insn-009bfe9c)
- ブロック [`009bfe9c`](#insn-009bfe9c) 範囲 `[['009bfe9c', '009bfecf']]`
  - `FALL_THROUGH` [`009bfecc`](#insn-009bfecc) → [`009bfed0`](#insn-009bfed0)
- ブロック [`009bfed0`](#insn-009bfed0) 範囲 `[['009bfed0', '009bffcf']]`
  - `CONDITIONAL_JUMP` [`009bffcc`](#insn-009bffcc) → [`009c0048`](#insn-009c0048)
  - `FALL_THROUGH` [`009bffcc`](#insn-009bffcc) → [`009bffd0`](#insn-009bffd0)
- ブロック [`009bffd0`](#insn-009bffd0) 範囲 `[['009bffd0', '009bffd7']]`
  - `CONDITIONAL_JUMP` [`009bffd4`](#insn-009bffd4) → [`009c0048`](#insn-009c0048)
  - `FALL_THROUGH` [`009bffd4`](#insn-009bffd4) → [`009bffd8`](#insn-009bffd8)
- ブロック [`009bffd8`](#insn-009bffd8) 範囲 `[['009bffd8', '009bffdb']]`
  - `FALL_THROUGH` [`009bffd8`](#insn-009bffd8) → [`009bffdc`](#insn-009bffdc)
- ブロック [`009bffdc`](#insn-009bffdc) 範囲 `[['009bffdc', '009bffdf']]`
  - `CONDITIONAL_JUMP` [`009bffdc`](#insn-009bffdc) → [`009c0048`](#insn-009c0048)
  - `FALL_THROUGH` [`009bffdc`](#insn-009bffdc) → [`009bffe0`](#insn-009bffe0)
- ブロック [`009bffe0`](#insn-009bffe0) 範囲 `[['009bffe0', '009bffe7']]`
  - `CONDITIONAL_JUMP` [`009bffe4`](#insn-009bffe4) → [`009c0048`](#insn-009c0048)
  - `FALL_THROUGH` [`009bffe4`](#insn-009bffe4) → [`009bffe8`](#insn-009bffe8)
- ブロック [`009bffe8`](#insn-009bffe8) 範囲 `[['009bffe8', '009bffef']]`
  - `CONDITIONAL_JUMP` [`009bffec`](#insn-009bffec) → [`009c0048`](#insn-009c0048)
  - `FALL_THROUGH` [`009bffec`](#insn-009bffec) → [`009bfff0`](#insn-009bfff0)
- ブロック [`009bfff0`](#insn-009bfff0) 範囲 `[['009bfff0', '009bfff7']]`
  - `CONDITIONAL_JUMP` [`009bfff4`](#insn-009bfff4) → [`009c0048`](#insn-009c0048)
  - `FALL_THROUGH` [`009bfff4`](#insn-009bfff4) → [`009bfff8`](#insn-009bfff8)
- ブロック [`009bfff8`](#insn-009bfff8) 範囲 `[['009bfff8', '009bffff']]`
  - `CONDITIONAL_JUMP` [`009bfffc`](#insn-009bfffc) → [`009c0048`](#insn-009c0048)
  - `FALL_THROUGH` [`009bfffc`](#insn-009bfffc) → [`009c0000`](#insn-009c0000)
- ブロック [`009c0000`](#insn-009c0000) 範囲 `[['009c0000', '009c0017']]`
  - `FALL_THROUGH` [`009c0014`](#insn-009c0014) → [`009c0018`](#insn-009c0018)
- ブロック [`009c0018`](#insn-009c0018) 範囲 `[['009c0018', '009c0047']]`
  - `FALL_THROUGH` [`009c0044`](#insn-009c0044) → [`009c0048`](#insn-009c0048)
- ブロック [`009c0048`](#insn-009c0048) 範囲 `[['009c0048', '009c0053']]`
  - `FALL_THROUGH` [`009c0050`](#insn-009c0050) → [`009c0054`](#insn-009c0054)
- ブロック [`009c0054`](#insn-009c0054) 範囲 `[['009c0054', '009c010f']]`
  - `CONDITIONAL_JUMP` [`009c010c`](#insn-009c010c) → [`009c014c`](#insn-009c014c)
  - `FALL_THROUGH` [`009c010c`](#insn-009c010c) → [`009c0110`](#insn-009c0110)
- ブロック [`009c0110`](#insn-009c0110) 範囲 `[['009c0110', '009c014b']]`
  - `FALL_THROUGH` [`009c0148`](#insn-009c0148) → [`009c014c`](#insn-009c014c)
- ブロック [`009c014c`](#insn-009c014c) 範囲 `[['009c014c', '009c016b']]`
  - `CONDITIONAL_JUMP` [`009c0168`](#insn-009c0168) → [`009c01b4`](#insn-009c01b4)
  - `FALL_THROUGH` [`009c0168`](#insn-009c0168) → [`009c016c`](#insn-009c016c)
- ブロック [`009c016c`](#insn-009c016c) 範囲 `[['009c016c', '009c019f']]`
  - `FALL_THROUGH` [`009c019c`](#insn-009c019c) → [`009c01a0`](#insn-009c01a0)
- ブロック [`009c01a0`](#insn-009c01a0) 範囲 `[['009c01a0', '009c01b3']]`
  - `FALL_THROUGH` [`009c01b0`](#insn-009c01b0) → [`009c01b4`](#insn-009c01b4)
- ブロック [`009c01b4`](#insn-009c01b4) 範囲 `[['009c01b4', '009c01bf']]`
  - `FALL_THROUGH` [`009c01bc`](#insn-009c01bc) → [`009c01c0`](#insn-009c01c0)
- ブロック [`009c01c0`](#insn-009c01c0) 範囲 `[['009c01c0', '009c01f3']]`
- ブロック [`009c01f4`](#insn-009c01f4) 範囲 `[['009c01f4', '009c020f']]`
  - `FALL_THROUGH` [`009c020c`](#insn-009c020c) → [`009c0210`](#insn-009c0210)
- ブロック [`009c0210`](#insn-009c0210) 範囲 `[['009c0210', '009c0213']]`

## 命令位置別の参照

- [`009bfdcc`](#insn-009bfdcc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bfdd0`](#insn-009bfdd0) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bfdd4`](#insn-009bfdd4) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bfdd8`](#insn-009bfdd8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bfddc`](#insn-009bfddc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bfde0`](#insn-009bfde0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bfde4`](#insn-009bfde4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bfdf0`](#insn-009bfdf0) → `00ca5a38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009bfdf4`](#insn-009bfdf4) → [`009c01f4`](#insn-009c01f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bfe04`](#insn-009bfe04) → `00c66ef8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`009bfe0c`](#insn-009bfe0c) → `00c8a720`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`009bfe18`](#insn-009bfe18) → [`00c596b0`](../00c59/00c596b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c596b0` · 推定シンボル `None` · 推定型 `None`
- [`009bfe1c`](#insn-009bfe1c) → [`009c01f4`](#insn-009c01f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bfe58`](#insn-009bfe58) → [`00467ec0`](../00467/00467ec0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467ec0` · 推定シンボル `None` · 推定型 `None`
- [`009bfe64`](#insn-009bfe64) → [`0046cd24`](../0046c/0046cd24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046cd24` · 推定シンボル `None` · 推定型 `None`
- [`009bfe6c`](#insn-009bfe6c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`009bfe70`](#insn-009bfe70) → [`0046cde4`](../0046c/0046cde4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046cde4` · 推定シンボル `None` · 推定型 `None`
- [`009bfe90`](#insn-009bfe90) → [`00469f64`](../00469/00469f64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469f64` · 推定シンボル `None` · 推定型 `None`
- [`009bfea8`](#insn-009bfea8) → [`00467ec0`](../00467/00467ec0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467ec0` · 推定シンボル `None` · 推定型 `None`
- [`009bfeac`](#insn-009bfeac) → `00333f9c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009bfeb4`](#insn-009bfeb4) → [`0046dd0c`](../0046d/0046dd0c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046dd0c` · 推定シンボル `None` · 推定型 `None`
- [`009bfed0`](#insn-009bfed0) → [`00468f3c`](../00468/00468f3c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468f3c` · 推定シンボル `None` · 推定型 `None`
- [`009bfedc`](#insn-009bfedc) → [`0046cd24`](../0046c/0046cd24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046cd24` · 推定シンボル `None` · 推定型 `None`
- [`009bfefc`](#insn-009bfefc) → [`00469f64`](../00469/00469f64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469f64` · 推定シンボル `None` · 推定型 `None`
- [`009bff14`](#insn-009bff14) → [`00467ec0`](../00467/00467ec0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467ec0` · 推定シンボル `None` · 推定型 `None`
- [`009bff20`](#insn-009bff20) → [`00468fc0`](../00468/00468fc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468fc0` · 推定シンボル `None` · 推定型 `None`
- [`009bff34`](#insn-009bff34) → [`008624b4`](../00862/008624b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008624b4` · 推定シンボル `None` · 推定型 `None`
- [`009bff40`](#insn-009bff40) → [`0046cd24`](../0046c/0046cd24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046cd24` · 推定シンボル `None` · 推定型 `None`
- [`009bff60`](#insn-009bff60) → [`00469f64`](../00469/00469f64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469f64` · 推定シンボル `None` · 推定型 `None`
- [`009bff6c`](#insn-009bff6c) → [`00468fc0`](../00468/00468fc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468fc0` · 推定シンボル `None` · 推定型 `None`
- [`009bff78`](#insn-009bff78) → [`0046cd24`](../0046c/0046cd24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046cd24` · 推定シンボル `None` · 推定型 `None`
- [`009bff98`](#insn-009bff98) → [`00469f64`](../00469/00469f64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469f64` · 推定シンボル `None` · 推定型 `None`
- [`009bffa4`](#insn-009bffa4) → [`00468fc0`](../00468/00468fc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468fc0` · 推定シンボル `None` · 推定型 `None`
- [`009bffa8`](#insn-009bffa8) → `00334170`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009bffc4`](#insn-009bffc4) → [`004692e8`](../00469/004692e8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004692e8` · 推定シンボル `None` · 推定型 `None`
- [`009bffc8`](#insn-009bffc8) → `00332a24`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009bffcc`](#insn-009bffcc) → [`009c0048`](#insn-009c0048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bffd0`](#insn-009bffd0) → `00332a25`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009bffd4`](#insn-009bffd4) → [`009c0048`](#insn-009c0048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bffd8`](#insn-009bffd8) → `00332a2d`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009bffdc`](#insn-009bffdc) → [`009c0048`](#insn-009c0048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bffe0`](#insn-009bffe0) → `00332a31`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009bffe4`](#insn-009bffe4) → [`009c0048`](#insn-009c0048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bffe8`](#insn-009bffe8) → `00332a26`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009bffec`](#insn-009bffec) → [`009c0048`](#insn-009c0048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bfff0`](#insn-009bfff0) → `00332060`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009bfff4`](#insn-009bfff4) → [`009c0048`](#insn-009c0048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bfff8`](#insn-009bfff8) → `00332a2e`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009bfffc`](#insn-009bfffc) → [`009c0048`](#insn-009c0048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009c0000`](#insn-009c0000) → `00333f98`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009c0044`](#insn-009c0044) → [`00469f64`](../00469/00469f64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469f64` · 推定シンボル `None` · 推定型 `None`
- [`009c004c`](#insn-009c004c) → `00333dc0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009c0054`](#insn-009c0054) → `00c9c548`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`009c0060`](#insn-009c0060) → `00333ccc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009c0060`](#insn-009c0060) → `00333cd0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009c0064`](#insn-009c0064) → `00ca5524`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009c0068`](#insn-009c0068) → `00333cd4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009c0068`](#insn-009c0068) → `00333cd8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009c0088`](#insn-009c0088) → [`00469f64`](../00469/00469f64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469f64` · 推定シンボル `None` · 推定型 `None`
- [`009c008c`](#insn-009c008c) → `00333dc0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009c0098`](#insn-009c0098) → `00333ccc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009c0098`](#insn-009c0098) → `00333cd0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009c009c`](#insn-009c009c) → `00ca5524`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009c00c8`](#insn-009c00c8) → [`00469f64`](../00469/00469f64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469f64` · 推定シンボル `None` · 推定型 `None`
- [`009c00dc`](#insn-009c00dc) → [`00aca7e0`](../00aca/00aca7e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aca7e0` · 推定シンボル `None` · 推定型 `None`
- [`009c00f4`](#insn-009c00f4) → [`00467ec0`](../00467/00467ec0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467ec0` · 推定シンボル `None` · 推定型 `None`
- [`009c0100`](#insn-009c0100) → [`00468f3c`](../00468/00468f3c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468f3c` · 推定シンボル `None` · 推定型 `None`
- [`009c0104`](#insn-009c0104) → `00337670`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009c010c`](#insn-009c010c) → [`009c014c`](#insn-009c014c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009c0110`](#insn-009c0110) → `00333f98`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009c0124`](#insn-009c0124) → [`0046dcd4`](../0046d/0046dcd4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046dcd4` · 推定シンボル `None` · 推定型 `None`
- [`009c0148`](#insn-009c0148) → [`004692e8`](../00469/004692e8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004692e8` · 推定シンボル `None` · 推定型 `None`
- [`009c0154`](#insn-009c0154) → [`00468fc0`](../00468/00468fc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468fc0` · 推定シンボル `None` · 推定型 `None`
- [`009c0158`](#insn-009c0158) → `00335f78`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009c015c`](#insn-009c015c) → `00337670`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009c0168`](#insn-009c0168) → [`009c01b4`](#insn-009c01b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009c0174`](#insn-009c0174) → [`0046cd24`](../0046c/0046cd24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046cd24` · 推定シンボル `None` · 推定型 `None`
- [`009c0178`](#insn-009c0178) → `00333f98`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009c0190`](#insn-009c0190) → [`0046dcd4`](../0046d/0046dcd4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046dcd4` · 推定シンボル `None` · 推定型 `None`
- [`009c01b0`](#insn-009c01b0) → [`004692e8`](../00469/004692e8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004692e8` · 推定シンボル `None` · 推定型 `None`
- [`009c01bc`](#insn-009c01bc) → [`00468fc0`](../00468/00468fc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468fc0` · 推定シンボル `None` · 推定型 `None`
- [`009c01c8`](#insn-009c01c8) → [`00468f3c`](../00468/00468f3c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468f3c` · 推定シンボル `None` · 推定型 `None`
- [`009c01d4`](#insn-009c01d4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009c01d8`](#insn-009c01d8) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009c01dc`](#insn-009c01dc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009c01e0`](#insn-009c01e0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009c01e4`](#insn-009c01e4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009c01e8`](#insn-009c01e8) → `Stack[-0x58]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009c01f0`](#insn-009c01f0) → [`009bf2e0`](009bf2e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009bf2e0` · 推定シンボル `None` · 推定型 `None`
- [`009c01f4`](#insn-009c01f4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009c01f8`](#insn-009c01f8) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009c01fc`](#insn-009c01fc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009c0200`](#insn-009c0200) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009c0204`](#insn-009c0204) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009c0208`](#insn-009c0208) → `Stack[-0x58]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009bfdcc`](#insn-009bfdcc)

~~~json
{
  "source": "009bfdcc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bfdd0`](#insn-009bfdd0)

~~~json
{
  "source": "009bfdd0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bfdd4`](#insn-009bfdd4)

~~~json
{
  "source": "009bfdd4",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bfdd8`](#insn-009bfdd8)

~~~json
{
  "source": "009bfdd8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bfddc`](#insn-009bfddc)

~~~json
{
  "source": "009bfddc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bfde0`](#insn-009bfde0)

~~~json
{
  "source": "009bfde0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bfde4`](#insn-009bfde4)

~~~json
{
  "source": "009bfde4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bfdf0`](#insn-009bfdf0)

~~~json
{
  "source": "009bfdf0",
  "target": "00ca5a38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5a38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009bfdf4`](#insn-009bfdf4)

~~~json
{
  "source": "009bfdf4",
  "target": "009c01f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bfe04`](#insn-009bfe04)

~~~json
{
  "source": "009bfe04",
  "target": "00c66ef8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c66ef8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009bfe0c`](#insn-009bfe0c)

~~~json
{
  "source": "009bfe0c",
  "target": "00c8a720",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8a720",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009bfe18`](#insn-009bfe18)

~~~json
{
  "source": "009bfe18",
  "target": "00c596b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bfe1c`](#insn-009bfe1c)

~~~json
{
  "source": "009bfe1c",
  "target": "009c01f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bfe58`](#insn-009bfe58)

~~~json
{
  "source": "009bfe58",
  "target": "00467ec0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bfe64`](#insn-009bfe64)

~~~json
{
  "source": "009bfe64",
  "target": "0046cd24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bfe6c`](#insn-009bfe6c)

~~~json
{
  "source": "009bfe6c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bfe70`](#insn-009bfe70)

~~~json
{
  "source": "009bfe70",
  "target": "0046cde4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bfe90`](#insn-009bfe90)

~~~json
{
  "source": "009bfe90",
  "target": "00469f64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bfea8`](#insn-009bfea8)

~~~json
{
  "source": "009bfea8",
  "target": "00467ec0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bfeac`](#insn-009bfeac)

~~~json
{
  "source": "009bfeac",
  "target": "00333f9c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f98",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "009e6c00108d0900",
  "capture_start": "00333f98",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009bfeb4`](#insn-009bfeb4)

~~~json
{
  "source": "009bfeb4",
  "target": "0046dd0c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bfed0`](#insn-009bfed0)

~~~json
{
  "source": "009bfed0",
  "target": "00468f3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bfedc`](#insn-009bfedc)

~~~json
{
  "source": "009bfedc",
  "target": "0046cd24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bfefc`](#insn-009bfefc)

~~~json
{
  "source": "009bfefc",
  "target": "00469f64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bff14`](#insn-009bff14)

~~~json
{
  "source": "009bff14",
  "target": "00467ec0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bff20`](#insn-009bff20)

~~~json
{
  "source": "009bff20",
  "target": "00468fc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bff34`](#insn-009bff34)

~~~json
{
  "source": "009bff34",
  "target": "008624b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bff40`](#insn-009bff40)

~~~json
{
  "source": "009bff40",
  "target": "0046cd24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bff60`](#insn-009bff60)

~~~json
{
  "source": "009bff60",
  "target": "00469f64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bff6c`](#insn-009bff6c)

~~~json
{
  "source": "009bff6c",
  "target": "00468fc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bff78`](#insn-009bff78)

~~~json
{
  "source": "009bff78",
  "target": "0046cd24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bff98`](#insn-009bff98)

~~~json
{
  "source": "009bff98",
  "target": "00469f64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bffa4`](#insn-009bffa4)

~~~json
{
  "source": "009bffa4",
  "target": "00468fc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bffa8`](#insn-009bffa8)

~~~json
{
  "source": "009bffa8",
  "target": "00334170",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334170",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "180b6d0038950900",
  "capture_start": "00334170",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009bffc4`](#insn-009bffc4)

~~~json
{
  "source": "009bffc4",
  "target": "004692e8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bffc8`](#insn-009bffc8)

~~~json
{
  "source": "009bffc8",
  "target": "00332a24",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "d406690034470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009bffcc`](#insn-009bffcc)

~~~json
{
  "source": "009bffcc",
  "target": "009c0048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bffd0`](#insn-009bffd0)

~~~json
{
  "source": "009bffd0",
  "target": "00332a25",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 5,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "d406690034470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009bffd4`](#insn-009bffd4)

~~~json
{
  "source": "009bffd4",
  "target": "009c0048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bffd8`](#insn-009bffd8)

~~~json
{
  "source": "009bffd8",
  "target": "00332a2d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a28",
  "offset": 5,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e006690048470900",
  "capture_start": "00332a28",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009bffdc`](#insn-009bffdc)

~~~json
{
  "source": "009bffdc",
  "target": "009c0048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bffe0`](#insn-009bffe0)

~~~json
{
  "source": "009bffe0",
  "target": "00332a31",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a30",
  "offset": 1,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e40669005c470900",
  "capture_start": "00332a30",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009bffe4`](#insn-009bffe4)

~~~json
{
  "source": "009bffe4",
  "target": "009c0048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bffe8`](#insn-009bffe8)

~~~json
{
  "source": "009bffe8",
  "target": "00332a26",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 6,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "d406690034470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009bffec`](#insn-009bffec)

~~~json
{
  "source": "009bffec",
  "target": "009c0048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bfff0`](#insn-009bfff0)

~~~json
{
  "source": "009bfff0",
  "target": "00332060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332060",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "0c0b62008c230900",
  "capture_start": "00332060",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009bfff4`](#insn-009bfff4)

~~~json
{
  "source": "009bfff4",
  "target": "009c0048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bfff8`](#insn-009bfff8)

~~~json
{
  "source": "009bfff8",
  "target": "00332a2e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a28",
  "offset": 6,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e006690048470900",
  "capture_start": "00332a28",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009bfffc`](#insn-009bfffc)

~~~json
{
  "source": "009bfffc",
  "target": "009c0048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009c0000`](#insn-009c0000)

~~~json
{
  "source": "009c0000",
  "target": "00333f98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f98",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "009e6c00108d0900",
  "capture_start": "00333f98",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009c0044`](#insn-009c0044)

~~~json
{
  "source": "009c0044",
  "target": "00469f64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009c004c`](#insn-009c004c)

~~~json
{
  "source": "009c004c",
  "target": "00333dc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333dc0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "40596b00a0840900",
  "capture_start": "00333dc0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009c0054`](#insn-009c0054)

~~~json
{
  "source": "009c0054",
  "target": "00c9c548",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c548",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009c0060`](#insn-009c0060)

~~~json
{
  "source": "009c0060",
  "target": "00333ccc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333cc8",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "28e36a00ec800900",
  "capture_start": "00333cc8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009c0060`](#insn-009c0060)

~~~json
{
  "source": "009c0060",
  "target": "00333cd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333cd0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "2ce36a0000810900",
  "capture_start": "00333cd0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009c0064`](#insn-009c0064)

~~~json
{
  "source": "009c0064",
  "target": "00ca5524",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009c0068`](#insn-009c0068)

~~~json
{
  "source": "009c0068",
  "target": "00333cd4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333cd0",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "2ce36a0000810900",
  "capture_start": "00333cd0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009c0068`](#insn-009c0068)

~~~json
{
  "source": "009c0068",
  "target": "00333cd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333cd8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "60e36a0028810900",
  "capture_start": "00333cd8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009c0088`](#insn-009c0088)

~~~json
{
  "source": "009c0088",
  "target": "00469f64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009c008c`](#insn-009c008c)

~~~json
{
  "source": "009c008c",
  "target": "00333dc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333dc0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "40596b00a0840900",
  "capture_start": "00333dc0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009c0098`](#insn-009c0098)

~~~json
{
  "source": "009c0098",
  "target": "00333ccc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333cc8",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "28e36a00ec800900",
  "capture_start": "00333cc8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009c0098`](#insn-009c0098)

~~~json
{
  "source": "009c0098",
  "target": "00333cd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333cd0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "2ce36a0000810900",
  "capture_start": "00333cd0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009c009c`](#insn-009c009c)

~~~json
{
  "source": "009c009c",
  "target": "00ca5524",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009c00c8`](#insn-009c00c8)

~~~json
{
  "source": "009c00c8",
  "target": "00469f64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009c00dc`](#insn-009c00dc)

~~~json
{
  "source": "009c00dc",
  "target": "00aca7e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009c00f4`](#insn-009c00f4)

~~~json
{
  "source": "009c00f4",
  "target": "00467ec0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009c0100`](#insn-009c0100)

~~~json
{
  "source": "009c0100",
  "target": "00468f3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009c0104`](#insn-009c0104)

~~~json
{
  "source": "009c0104",
  "target": "00337670",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00337670",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "38f17a00f4490a00",
  "capture_start": "00337670",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009c010c`](#insn-009c010c)

~~~json
{
  "source": "009c010c",
  "target": "009c014c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009c0110`](#insn-009c0110)

~~~json
{
  "source": "009c0110",
  "target": "00333f98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f98",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "009e6c00108d0900",
  "capture_start": "00333f98",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009c0124`](#insn-009c0124)

~~~json
{
  "source": "009c0124",
  "target": "0046dcd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009c0148`](#insn-009c0148)

~~~json
{
  "source": "009c0148",
  "target": "004692e8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009c0154`](#insn-009c0154)

~~~json
{
  "source": "009c0154",
  "target": "00468fc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009c0158`](#insn-009c0158)

~~~json
{
  "source": "009c0158",
  "target": "00335f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335f78",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "6875750094fe0900",
  "capture_start": "00335f78",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009c015c`](#insn-009c015c)

~~~json
{
  "source": "009c015c",
  "target": "00337670",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00337670",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "38f17a00f4490a00",
  "capture_start": "00337670",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009c0168`](#insn-009c0168)

~~~json
{
  "source": "009c0168",
  "target": "009c01b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009c0174`](#insn-009c0174)

~~~json
{
  "source": "009c0174",
  "target": "0046cd24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009c0178`](#insn-009c0178)

~~~json
{
  "source": "009c0178",
  "target": "00333f98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f98",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "009e6c00108d0900",
  "capture_start": "00333f98",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009c0190`](#insn-009c0190)

~~~json
{
  "source": "009c0190",
  "target": "0046dcd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009c01b0`](#insn-009c01b0)

~~~json
{
  "source": "009c01b0",
  "target": "004692e8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009c01bc`](#insn-009c01bc)

~~~json
{
  "source": "009c01bc",
  "target": "00468fc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009c01c8`](#insn-009c01c8)

~~~json
{
  "source": "009c01c8",
  "target": "00468f3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009c01d4`](#insn-009c01d4)

~~~json
{
  "source": "009c01d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009c01d8`](#insn-009c01d8)

~~~json
{
  "source": "009c01d8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009c01dc`](#insn-009c01dc)

~~~json
{
  "source": "009c01dc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009c01e0`](#insn-009c01e0)

~~~json
{
  "source": "009c01e0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009c01e4`](#insn-009c01e4)

~~~json
{
  "source": "009c01e4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009c01e8`](#insn-009c01e8)

~~~json
{
  "source": "009c01e8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009c01f0`](#insn-009c01f0)

~~~json
{
  "source": "009c01f0",
  "target": "009bf2e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009c01f4`](#insn-009c01f4)

~~~json
{
  "source": "009c01f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009c01f8`](#insn-009c01f8)

~~~json
{
  "source": "009c01f8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009c01fc`](#insn-009c01fc)

~~~json
{
  "source": "009c01fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009c0200`](#insn-009c0200)

~~~json
{
  "source": "009c0200",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009c0204`](#insn-009c0204)

~~~json
{
  "source": "009c0204",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009c0208`](#insn-009c0208)

~~~json
{
  "source": "009c0208",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
