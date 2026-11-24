# 009fbbcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `009fac20`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fa/009fac20.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0061.md#compare-8d0f4ed0302d4c26134609df6af67913)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009fbbcc",
  "name": "FUN_009fbbcc",
  "size": 1848,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3beb7bc2f1b253d5e0384a49f1d83f6f35d15744e1a77c2c588c4a9f66a9cec1",
  "source_text_sha256": "3beb7bc2f1b253d5e0384a49f1d83f6f35d15744e1a77c2c588c4a9f66a9cec1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009fbbcc",
        "009fc2ff"
      ],
      [
        "009fc448",
        "009fc44b"
      ]
    ],
    "bytes_sha256": "bc8a334f57d889e5dd0575ca777046c3813b78f6b04d23d0f10160bd2f49d8f8",
    "instruction_count": 462,
    "instruction_bytes": 1848,
    "body_bytes": 1848,
    "indirect": 10,
    "unresolved": 6
  }
}
~~~

## 呼び出し元

- [007f4664](../007f4/007f4664.md)
- [009fec50](../009fe/009fec50.md)
- [00a022f4](../00a02/00a022f4.md)
- [00a068bc](../00a06/00a068bc.md)

## 呼び出し先

- [0046de54](../0046d/0046de54.md)
- [0047e96c](../0047e/0047e96c.md)
- [005d8fb8](../005d8/005d8fb8.md)
- [008524fc](../00852/008524fc.md)
- [008b7ff0](../008b7/008b7ff0.md)
- [008ba29c](../008ba/008ba29c.md)
- [008ba504](../008ba/008ba504.md)
- [008ba5d0](../008ba/008ba5d0.md)
- [008ba6a8](../008ba/008ba6a8.md)
- [008ba85c](../008ba/008ba85c.md)
- [008bb86c](../008bb/008bb86c.md)
- [009e3f94](../009e3/009e3f94.md)
- [009f8478](../009f8/009f8478.md)
- [009fa2c8](../009fa/009fa2c8.md)
- [009fa81c](../009fa/009fa81c.md)
- [00a023a8](../00a02/00a023a8.md)
- [00a023ac](../00a02/00a023ac.md)
- [00a024ec](../00a02/00a024ec.md)
- [00a032d0](../00a03/00a032d0.md)
- [00a032d4](../00a03/00a032d4.md)
- [00a036fc](../00a03/00a036fc.md)
- [00a03700](../00a03/00a03700.md)
- [00a477cc](../00a47/00a477cc.md)
- [00a47944](../00a47/00a47944.md)
- [00a48594](../00a48/00a48594.md)
- [00a83a34](../00a83/00a83a34.md)
- [00a842c4](../00a84/00a842c4.md)
- [00a844b0](../00a84/00a844b0.md)
- [00ac9e74](../00ac9/00ac9e74.md)
- [00ac9eb8](../00ac9/00ac9eb8.md)
- [00c54d90](../00c54/00c54d90.md)
- [00c58ed0](../00c58/00c58ed0.md)
- [00c58ef0](../00c58/00c58ef0.md)
- [00c58f10](../00c58/00c58f10.md)
- [00c58f20](../00c58/00c58f20.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c596b0](../00c59/00c596b0.md)

## 関連文字列（未確認候補）

~~~text
"9.imgcut"
"img029.imgcut"
"img029.png"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 11943 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_009fbbcc(long param_1)

{
  long lVar1;
  undefined8 uVar2;
  undefined *puVar3;
  undefined *puVar4;
  undefined6 uVar5;
  int iVar6;
  int iVar7;
  long lVar8;
  long lVar9;
  undefined8 uVar10;
  long *plVar11;
  undefined ***pppuVar12;
  long *plVar13;
  long *plVar14;
  int iVar15;
  float fVar16;
  undefined1 auVar17 [16];
  undefined8 local_198;
  undefined8 uStack_190;
  byte local_188;
  undefined5 uStack_187;
  undefined2 uStack_182;
  char cStack_180;
  char acStack_17f [5];
  undefined1 local_17a;
  void *local_178;
  long *local_170;
  long *plStack_168;
  byte local_158;
  char cStack_157;
  undefined6 uStack_156;
  char cStack_150;
  undefined2 local_14f;
  undefined1 local_14d;
  void *local_148;
  undefined **local_140;
  undefined8 uStack_138;
  undefined ***local_120;
  undefined **local_110;
  long lStack_108;
  long local_100;
  undefined ***local_f0;
  long local_e0 [4];
  long *local_c0;
  undefined **local_b0 [4];
  undefined ***local_90;
  long local_80;
  
  lVar1 = tpidr_el0;
  local_80 = *(long *)(lVar1 + 0x28);
  if (DAT_00ca5a38 == 0) {
    lVar8 = 0;
  }
  else {
    lVar8 = __dynamic_cast(DAT_00ca5a38,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c66ef8,
                           &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c72a30,0);
  }
  lVar9 = FUN_008524fc();
                    /* try { // try from 009fbc44 to 00afbc4f has its CatchHandler @ 009fbd00 */
  FUN_00a842c4(lVar9 + 0x3078,0x2a);
  lVar9 = FUN_008524fc();
  FUN_00a842c4(lVar9 + 0x3078,0x2b);
  lVar9 = FUN_008524fc();
  FUN_009fa2c8(&local_158);
                    /* try { // try from 009fbc68 to 00afbc8b has its CatchHandler @ 009fbd10 */
  FUN_00a844b0(lVar9 + 0x3078,0x2a,&local_158,0x1a,0x2c8);
  if ((local_158 & 1) != 0) {
                    /* try { // try from 009fbc8c to 00afbd93 has its CatchHandler @ 009fbb90 */
    _ZdlPv(local_148);
  }
  lVar9 = FUN_008524fc();
  FUN_009fa81c(&local_158);
  FUN_00a844b0(lVar9 + 0x3078,0x2b,&local_158,0x1a,0x2c8);
  if ((local_158 & 1) != 0) {
    _ZdlPv(local_148);
  }
  if (((DAT_00ca5ff8 & 1) == 0) && (iVar6 = __cxa_guard_acquire(&DAT_00ca5ff8), iVar6 != 0)) {
                    /* try { // try from 009fc2cc to 00afc2e3 has its CatchHandler @ 009fcb10 */
    DAT_00ca5fc8 = 0;
    DAT_00ca5fc0 = &DAT_00ca5fc8;
    DAT_00ca5fe8 = 0;
    DAT_00ca5ff0 = 0;
                    /* try { // try from 009fc2e4 to 00afc3db has its CatchHandler @ 009fbe88 */
    DAT_00ca5fe0 = 0;
    DAT_00ca5fd0 = 0;
    DAT_00ca5fd8 = &DAT_00ca5fe0;
    __cxa_atexit(FUN_0047f114,&DAT_00ca5fc0,&PTR_LOOP_00c64030);
    __cxa_guard_release(&DAT_00ca5ff8);
  }
  local_14d = 0;
  local_158 = 0x14;
  local_14f = 0x676e;
                    /* catch() { ... } // from try @ 009fbc44 with catch @ 009fbd00 */
  local_188 = 0x1a;
  cStack_157 = (char)s_img029_png_002b3fb8._0_8_;
  uStack_156 = SUB86(s_img029_png_002b3fb8._0_8_,1);
  cStack_150 = SUB81(s_img029_png_002b3fb8._0_8_,7);
                    /* catch() { ... } // from try @ 009fbc68 with catch @ 009fbd10 */
  local_17a = 0;
  uStack_187 = _DAT_002b92eb;
  uStack_182 = (undefined2)s_9_imgcut_002b92f0._0_3_;
  cStack_180 = SUB31(s_9_imgcut_002b92f0._0_3_,2);
  acStack_17f[0] = s_9_imgcut_002b92f0[3];
  acStack_17f[1] = s_9_imgcut_002b92f0[4];
  acStack_17f[2] = s_9_imgcut_002b92f0[5];
  acStack_17f[3] = s_9_imgcut_002b92f0[6];
  acStack_17f[4] = s_9_imgcut_002b92f0[7];
  FUN_0047e96c(&local_170,&DAT_00ca5fc0,&local_158,&local_188,0x2601);
  plVar13 = plStack_168;
  plVar11 = local_170;
  plVar14 = *(long **)(lVar8 + 0xf0);
  local_170 = (long *)0x0;
  plStack_168 = (long *)0x0;
  *(long **)(lVar8 + 0xf0) = plVar13;
  *(long **)(lVar8 + 0xe8) = plVar11;
  plVar11 = plStack_168;
  if ((plVar14 != (long *)0x0) &&
     (lVar9 = FUN_00c54d90(0xffffffffffffffff,plVar14 + 1), plVar11 = plStack_168, lVar9 == 0)) {
    (**(code **)(*plVar14 + 0x10))(plVar14);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar14);
    plVar11 = plStack_168;
  }
  plStack_168 = plVar11;
  if ((plVar11 != (long *)0x0) && (lVar9 = FUN_00c54d90(0xffffffffffffffff,plVar11 + 1), lVar9 == 0)
     ) {
    (**(code **)(*plVar11 + 0x10))(plVar11);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar11);
  }
  if ((local_188 & 1) != 0) {
    _ZdlPv(local_178);
  }
  if ((local_158 & 1) != 0) {
    _ZdlPv(local_148);
  }
  FUN_009f8478();
  lVar9 = FUN_008524fc();
  local_90 = local_b0;
  local_158 = 0;
  cStack_157 = 0;
  local_b0[0] = &PTR_FUN_00c8bc40;
  uVar10 = FUN_008bb86c(lVar9 + 0x2f08,&local_158,0,0,4,local_b0);
  FUN_0046de54(&local_198,0,0xfffffff6,0x354,0x216);
  uVar10 = FUN_008ba504(uVar10,local_198,uStack_190);
  uVar10 = FUN_008ba85c(uVar10,0);
  if (local_90 == local_b0) {
    lVar9 = 0x20;
    pppuVar12 = local_b0;
LAB_009fbe34:
    (**(code **)((long)*pppuVar12 + lVar9))();
  }
  else if (local_90 != (undefined ***)0x0) {
    lVar9 = 0x28;
    pppuVar12 = local_90;
    goto LAB_009fbe34;
  }
  if ((local_158 & 1) != 0) {
    _ZdlPv(local_148);
  }
  lVar9 = FUN_008524fc();
  iVar6 = FUN_00a83a34(lVar9 + 0x3078,0x2a);
                    /* try { // try from 009fbe88 to 00afbf27 has its CatchHandler @ 009fbe88
                       catch() { ... } // from try @ 009fbe88 with catch @ 009fbe88
                       catch() { ... } // from try @ 009fbf48 with catch @ 009fbe88
                       catch() { ... } // from try @ 009fbfc8 with catch @ 009fbe88
                       catch() { ... } // from try @ 009fc09c with catch @ 009fbe88
                       catch() { ... } // from try @ 009fc1d0 with catch @ 009fbe88
                       catch() { ... } // from try @ 009fc2e4 with catch @ 009fbe88
                       catch() { ... } // from try @ 009fc3f4 with catch @ 009fbe88
                       catch() { ... } // from try @ 009fc504 with catch @ 009fbe88
                       catch() { ... } // from try @ 009fc584 with catch @ 009fbe88
                       catch() { ... } // from try @ 009fc660 with catch @ 009fbe88
                       catch() { ... } // from try @ 009fc790 with catch @ 009fbe88 */
  lVar9 = FUN_008524fc();
  iVar7 = FUN_00a83a34(lVar9 + 0x3078,0x2b);
  iVar15 = (int)((double)(iVar7 * 0x1a) * 1.2 + 75.0 +
                (double)((int)((double)(iVar6 * 0x1a) * 1.2 + 75.0 + 0.0) + 8));
  lVar9 = FUN_008524fc();
  plVar11 = (long *)FUN_009e3f94(lVar9 + 0x50,0xffffffff,0xffffffff);
  iVar6 = iVar15 + (int)((ulong)(plVar11[1] - *plVar11) >> 2) * 0x49249259 + 0x12;
  auVar17 = FUN_008ba29c(uVar10);
  iVar7 = auVar17._12_4_ + -0x42;
  if (iVar7 < iVar6) {
    lVar9 = FUN_008524fc();
    fVar16 = (float)iVar7;
                    /* try { // try from 009fbf28 to 00afbf47 has its CatchHandler @ 009fcb24 */
                    /* try { // try from 009fbf48 to 00afbfbb has its CatchHandler @ 009fbe88 */
    FUN_00ac9e74(fVar16,(float)iVar6,fVar16,(long)&fde_table_entry_00337d90.initial_loc + lVar9,1,
                 auVar17._8_4_ + auVar17._0_4_ + -0x2c,auVar17._4_4_ + 0x21,0x24);
    *(undefined4 *)(param_1 + 0x54) = 0;
    lVar9 = FUN_008524fc();
    *(undefined1 *)((long)&fde_table_entry_00337f60.data_loc + lVar9) = 1;
  }
  else {
    lVar9 = FUN_008524fc();
    FUN_00ac9eb8((long)&fde_table_entry_00337d90.initial_loc + lVar9);
  }
  local_c0 = (long *)_Znwm(0x28);
  *(undefined1 (*) [16])(local_c0 + 2) = auVar17;
  *local_c0 = (long)&PTR_FUN_00c8bcc0;
  local_c0[1] = param_1;
  *(int *)(local_c0 + 4) = iVar15 + 0x16;
  *(int *)((long)local_c0 + 0x24) = iVar6;
  FUN_008ba5d0(uVar10,local_e0);
  if (local_c0 == local_e0) {
    lVar9 = 0x20;
    plVar11 = local_e0;
LAB_009fbfc8:
                    /* try { // try from 009fbfc8 to 00afc083 has its CatchHandler @ 009fbe88 */
    (**(code **)(*plVar11 + lVar9))();
  }
  else if (local_c0 != (long *)0x0) {
    lVar9 = 0x28;
    plVar11 = local_c0;
                    /* try { // try from 009fbfbc to 00afbfc7 has its CatchHandler @ 009fcb1c */
    goto LAB_009fbfc8;
  }
  local_110 = &PTR_FUN_00c8bd40;
  lStack_108 = lVar8;
  local_100 = param_1;
  local_f0 = &local_110;
  FUN_008ba6a8(uVar10,&local_110);
  if (local_f0 == &local_110) {
    lVar9 = 0x20;
    pppuVar12 = &local_110;
LAB_009fc018:
    (**(code **)((long)*pppuVar12 + lVar9))();
  }
  else if (local_f0 != (undefined ***)0x0) {
    lVar9 = 0x28;
    pppuVar12 = local_f0;
    goto LAB_009fc018;
  }
  FUN_00a48594(&local_158,0x3f800000,lVar8 + 0x138,0xc9,0x267,0x91,0x26,0xa3,0xa4);
  plVar11 = (long *)CONCAT62(uStack_156,CONCAT11(cStack_157,local_158));
  (**(code **)(*plVar11 + 0x10))(plVar11,1);
  uVar2 = CONCAT62(uStack_156,CONCAT11(cStack_157,local_158));
  FUN_00a47944(&local_170,lVar8 + 0x138,0,0,0xa2);
  plVar11 = local_170;
  local_170 = (long *)0x0;
                    /* try { // try from 009fc084 to 00afc09b has its CatchHandler @ 009fcb18 */
  local_188 = (byte)plVar11;
  uStack_187 = (undefined5)((ulong)plVar11 >> 8);
  uStack_182 = (undefined2)((ulong)plVar11 >> 0x30);
  plVar11 = (long *)FUN_00a477cc(uVar2,&local_188);
                    /* try { // try from 009fc09c to 00afc1b7 has its CatchHandler @ 009fbe88 */
  (**(code **)(*plVar11 + 0x10))(plVar11,1);
  puVar3 = PTR_DAT_00c9c408;
  plVar11 = (long *)CONCAT26(uStack_182,CONCAT51(uStack_187,local_188));
  local_188 = 0;
  uStack_187 = 0;
  uStack_182 = 0;
  if (plVar11 != (long *)0x0) {
    *plVar11 = (long)(PTR_DAT_00c9c408 + 0x10);
    FUN_005d8fb8(plVar11 + 10);
    _ZdlPv(plVar11);
  }
  plVar11 = local_170;
  puVar4 = PTR_DAT_00c9c410;
  local_170 = (long *)0x0;
  if (plVar11 != (long *)0x0) {
    plVar13 = (long *)plVar11[0x16];
    *plVar11 = (long)(PTR_DAT_00c9c410 + 0x10);
    if ((plVar13 != (long *)0x0) &&
       (lVar8 = FUN_00c54d90(0xffffffffffffffff,plVar13 + 1), lVar8 == 0)) {
      (**(code **)(*plVar13 + 0x10))(plVar13);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar13);
    }
    *plVar11 = (long)(puVar3 + 0x10);
    FUN_005d8fb8(plVar11 + 10);
    _ZdlPv(plVar11);
  }
  lVar8 = FUN_008524fc();
  uVar5 = uStack_156;
  local_188 = local_158;
  uVar2 = CONCAT62(uStack_156,CONCAT11(cStack_157,local_158));
  local_158 = 0;
  cStack_157 = 0;
  uStack_156 = 0;
  uStack_187 = (undefined5)((ulong)uVar2 >> 8);
  uStack_182 = (undefined2)((uint6)uVar5 >> 0x20);
  local_140 = &PTR_FUN_00c8bdc0;
  uStack_138 = uVar10;
  local_120 = &local_140;
  FUN_008b7ff0(lVar8 + 0x2f38,0xd1,0x81,0x249,0x91,0x3c,&local_188,&local_140);
  if (local_120 == &local_140) {
    lVar8 = 0x20;
    pppuVar12 = &local_140;
  }
  else {
    if (local_120 == (undefined ***)0x0) goto LAB_009fc1ac;
    lVar8 = 0x28;
    pppuVar12 = local_120;
  }
  (**(code **)((long)*pppuVar12 + lVar8))();
LAB_009fc1ac:
  plVar11 = (long *)CONCAT26(uStack_182,CONCAT51(uStack_187,local_188));
  local_188 = 0;
  uStack_187 = 0;
  uStack_182 = 0;
  if (plVar11 != (long *)0x0) {
                    /* try { // try from 009fc1b8 to 00afc1cf has its CatchHandler @ 009fcb14 */
    *plVar11 = (long)(puVar3 + 0x10);
    FUN_005d8fb8(plVar11 + 10);
    _ZdlPv(plVar11);
  }
                    /* try { // try from 009fc1d0 to 00afc2cb has its CatchHandler @ 009fbe88 */
  plVar11 = (long *)CONCAT62(uStack_156,CONCAT11(cStack_157,local_158));
  local_158 = 0;
  cStack_157 = 0;
  uStack_156 = 0;
  if (plVar11 != (long *)0x0) {
    plVar13 = (long *)plVar11[0x16];
    *plVar11 = (long)(puVar4 + 0x10);
    if ((plVar13 != (long *)0x0) &&
       (lVar8 = FUN_00c54d90(0xffffffffffffffff,plVar13 + 1), lVar8 == 0)) {
      (**(code **)(*plVar13 + 0x10))(plVar13);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar13);
    }
    *plVar11 = (long)(puVar3 + 0x10);
    FUN_005d8fb8(plVar11 + 10);
    _ZdlPv(plVar11);
  }
  if (*(long *)(lVar1 + 0x28) != local_80) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009fbbcc"></a> `009fbbcc` | `ff 83 06 d1` | sub sp,sp,#0x1a0 | `FALL_THROUGH`
<a id="insn-009fbbd0"></a> `009fbbd0` | `e9 23 13 6d` | stp d9,d8,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-009fbbd4"></a> `009fbbd4` | `fd 7b 14 a9` | stp x29,x30,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-009fbbd8"></a> `009fbbd8` | `fc 6f 15 a9` | stp x28,x27,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-009fbbdc"></a> `009fbbdc` | `fa 67 16 a9` | stp x26,x25,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-009fbbe0"></a> `009fbbe0` | `f8 5f 17 a9` | stp x24,x23,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-009fbbe4"></a> `009fbbe4` | `f6 57 18 a9` | stp x22,x21,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-009fbbe8"></a> `009fbbe8` | `f4 4f 19 a9` | stp x20,x19,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-009fbbec"></a> `009fbbec` | `fd 03 05 91` | add x29,sp,#0x140 | `FALL_THROUGH`
<a id="insn-009fbbf0"></a> `009fbbf0` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-009fbbf4"></a> `009fbbf4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-009fbbf8"></a> `009fbbf8` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-009fbbfc"></a> `009fbbfc` | `a8 03 1e f8` | stur x8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-009fbc00"></a> `009fbc00` | `48 15 00 d0` | adrp x8,0xca5000 | `FALL_THROUGH`
<a id="insn-009fbc04"></a> `009fbc04` | `08 1d 45 f9` | ldr x8,[x8, #0xa38] | `FALL_THROUGH`
<a id="insn-009fbc08"></a> `009fbc08` | `48 01 00 b4` | cbz x8,0x009fbc30 | `CONDITIONAL_JUMP`
<a id="insn-009fbc0c"></a> `009fbc0c` | `41 13 00 f0` | adrp x1,0xc66000 | `FALL_THROUGH`
<a id="insn-009fbc10"></a> `009fbc10` | `21 e0 3b 91` | add x1,x1,#0xef8 | `FALL_THROUGH`
<a id="insn-009fbc14"></a> `009fbc14` | `a2 13 00 f0` | adrp x2,0xc72000 | `FALL_THROUGH`
<a id="insn-009fbc18"></a> `009fbc18` | `42 c0 28 91` | add x2,x2,#0xa30 | `FALL_THROUGH`
<a id="insn-009fbc1c"></a> `009fbc1c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-009fbc20"></a> `009fbc20` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-009fbc24"></a> `009fbc24` | `a3 76 09 94` | bl 0x00c596b0 | `UNCONDITIONAL_CALL`
<a id="insn-009fbc28"></a> `009fbc28` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-009fbc2c"></a> `009fbc2c` | `02 00 00 14` | b 0x009fbc34 | `UNCONDITIONAL_JUMP`
<a id="insn-009fbc30"></a> `009fbc30` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-009fbc34"></a> `009fbc34` | `32 5a f9 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-009fbc38"></a> `009fbc38` | `16 0f 86 52` | mov w22,#0x3078 | `FALL_THROUGH`
<a id="insn-009fbc3c"></a> `009fbc3c` | `41 05 80 52` | mov w1,#0x2a | `FALL_THROUGH`
<a id="insn-009fbc40"></a> `009fbc40` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-009fbc44"></a> `009fbc44` | `a0 21 02 94` | bl 0x00a842c4 | `UNCONDITIONAL_CALL`
<a id="insn-009fbc48"></a> `009fbc48` | `2d 5a f9 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-009fbc4c"></a> `009fbc4c` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-009fbc50"></a> `009fbc50` | `61 05 80 52` | mov w1,#0x2b | `FALL_THROUGH`
<a id="insn-009fbc54"></a> `009fbc54` | `9c 21 02 94` | bl 0x00a842c4 | `UNCONDITIONAL_CALL`
<a id="insn-009fbc58"></a> `009fbc58` | `29 5a f9 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-009fbc5c"></a> `009fbc5c` | `e8 23 01 91` | add x8,sp,#0x48 | `FALL_THROUGH`
<a id="insn-009fbc60"></a> `009fbc60` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-009fbc64"></a> `009fbc64` | `99 f9 ff 97` | bl 0x009fa2c8 | `UNCONDITIONAL_CALL`
<a id="insn-009fbc68"></a> `009fbc68` | `a0 02 16 8b` | add x0,x21,x22 | `FALL_THROUGH`
<a id="insn-009fbc6c"></a> `009fbc6c` | `e2 23 01 91` | add x2,sp,#0x48 | `FALL_THROUGH`
<a id="insn-009fbc70"></a> `009fbc70` | `41 05 80 52` | mov w1,#0x2a | `FALL_THROUGH`
<a id="insn-009fbc74"></a> `009fbc74` | `43 03 80 52` | mov w3,#0x1a | `FALL_THROUGH`
<a id="insn-009fbc78"></a> `009fbc78` | `04 59 80 52` | mov w4,#0x2c8 | `FALL_THROUGH`
<a id="insn-009fbc7c"></a> `009fbc7c` | `0d 22 02 94` | bl 0x00a844b0 | `UNCONDITIONAL_CALL`
<a id="insn-009fbc80"></a> `009fbc80` | `e8 23 41 39` | ldrb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009fbc84"></a> `009fbc84` | `68 00 00 36` | tbz w8,#0x0,0x009fbc90 | `CONDITIONAL_JUMP`
<a id="insn-009fbc88"></a> `009fbc88` | `e0 2f 40 f9` | ldr x0,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-009fbc8c"></a> `009fbc8c` | `b1 74 09 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-009fbc90"></a> `009fbc90` | `1b 5a f9 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-009fbc94"></a> `009fbc94` | `e8 23 01 91` | add x8,sp,#0x48 | `FALL_THROUGH`
<a id="insn-009fbc98"></a> `009fbc98` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-009fbc9c"></a> `009fbc9c` | `16 0f 86 52` | mov w22,#0x3078 | `FALL_THROUGH`
<a id="insn-009fbca0"></a> `009fbca0` | `df fa ff 97` | bl 0x009fa81c | `UNCONDITIONAL_CALL`
<a id="insn-009fbca4"></a> `009fbca4` | `a0 02 16 8b` | add x0,x21,x22 | `FALL_THROUGH`
<a id="insn-009fbca8"></a> `009fbca8` | `e2 23 01 91` | add x2,sp,#0x48 | `FALL_THROUGH`
<a id="insn-009fbcac"></a> `009fbcac` | `61 05 80 52` | mov w1,#0x2b | `FALL_THROUGH`
<a id="insn-009fbcb0"></a> `009fbcb0` | `43 03 80 52` | mov w3,#0x1a | `FALL_THROUGH`
<a id="insn-009fbcb4"></a> `009fbcb4` | `04 59 80 52` | mov w4,#0x2c8 | `FALL_THROUGH`
<a id="insn-009fbcb8"></a> `009fbcb8` | `fe 21 02 94` | bl 0x00a844b0 | `UNCONDITIONAL_CALL`
<a id="insn-009fbcbc"></a> `009fbcbc` | `e8 23 41 39` | ldrb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009fbcc0"></a> `009fbcc0` | `68 00 00 36` | tbz w8,#0x0,0x009fbccc | `CONDITIONAL_JUMP`
<a id="insn-009fbcc4"></a> `009fbcc4` | `e0 2f 40 f9` | ldr x0,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-009fbcc8"></a> `009fbcc8` | `a2 74 09 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-009fbccc"></a> `009fbccc` | `48 15 00 d0` | adrp x8,0xca5000 | `FALL_THROUGH`
<a id="insn-009fbcd0"></a> `009fbcd0` | `08 e1 3f 91` | add x8,x8,#0xff8 | `FALL_THROUGH`
<a id="insn-009fbcd4"></a> `009fbcd4` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-009fbcd8"></a> `009fbcd8` | `88 2e 00 36` | tbz w8,#0x0,0x009fc2a8 | `CONDITIONAL_JUMP`
<a id="insn-009fbcdc"></a> `009fbcdc` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-009fbce0"></a> `009fbce0` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-009fbce4"></a> `009fbce4` | `ff 4f 01 39` | strb wzr,[sp, #0x53] | `FALL_THROUGH`
<a id="insn-009fbce8"></a> `009fbce8` | `e8 23 01 39` | strb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009fbcec"></a> `009fbcec` | `c8 c5 ff 90` | adrp x8,0x2b3000 | `FALL_THROUGH`
<a id="insn-009fbcf0"></a> `009fbcf0` | `08 e1 3e 91` | add x8,x8,#0xfb8 | `FALL_THROUGH`
<a id="insn-009fbcf4"></a> `009fbcf4` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-009fbcf8"></a> `009fbcf8` | `e9 13 05 78` | sturh w9,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-009fbcfc"></a> `009fbcfc` | `49 03 80 52` | mov w9,#0x1a | `FALL_THROUGH`
<a id="insn-009fbd00"></a> `009fbd00` | `e9 63 00 39` | strb w9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009fbd04"></a> `009fbd04` | `e8 93 04 f8` | stur x8,[sp, #0x49] | `FALL_THROUGH`
<a id="insn-009fbd08"></a> `009fbd08` | `e8 c5 ff d0` | adrp x8,0x2b9000 | `FALL_THROUGH`
<a id="insn-009fbd0c"></a> `009fbd0c` | `08 ad 0b 91` | add x8,x8,#0x2eb | `FALL_THROUGH`
<a id="insn-009fbd10"></a> `009fbd10` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-009fbd14"></a> `009fbd14` | `08 51 40 f8` | ldur x8,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-009fbd18"></a> `009fbd18` | `ff 9b 00 39` | strb wzr,[sp, #0x26] | `FALL_THROUGH`
<a id="insn-009fbd1c"></a> `009fbd1c` | `e9 93 01 f8` | stur x9,[sp, #0x19] | `FALL_THROUGH`
<a id="insn-009fbd20"></a> `009fbd20` | `e8 e3 01 f8` | stur x8,[sp, #0x1e] | `FALL_THROUGH`
<a id="insn-009fbd24"></a> `009fbd24` | `40 15 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-009fbd28"></a> `009fbd28` | `00 00 3f 91` | add x0,x0,#0xfc0 | `FALL_THROUGH`
<a id="insn-009fbd2c"></a> `009fbd2c` | `e8 c3 00 91` | add x8,sp,#0x30 | `FALL_THROUGH`
<a id="insn-009fbd30"></a> `009fbd30` | `e1 23 01 91` | add x1,sp,#0x48 | `FALL_THROUGH`
<a id="insn-009fbd34"></a> `009fbd34` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-009fbd38"></a> `009fbd38` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-009fbd3c"></a> `009fbd3c` | `0c 0b ea 97` | bl 0x0047e96c | `UNCONDITIONAL_CALL`
<a id="insn-009fbd40"></a> `009fbd40` | `e0 0f c0 3d` | ldr q0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009fbd44"></a> `009fbd44` | `75 7a 40 f9` | ldr x21,[x19, #0xf0] | `FALL_THROUGH`
<a id="insn-009fbd48"></a> `009fbd48` | `ff 7f 03 a9` | stp xzr,xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009fbd4c"></a> `009fbd4c` | `60 82 8e 3c` | stur q0,[x19, #0xe8] | `FALL_THROUGH`
<a id="insn-009fbd50"></a> `009fbd50` | `b5 00 00 b4` | cbz x21,0x009fbd64 | `CONDITIONAL_JUMP`
<a id="insn-009fbd54"></a> `009fbd54` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-009fbd58"></a> `009fbd58` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009fbd5c"></a> `009fbd5c` | `0d 64 09 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-009fbd60"></a> `009fbd60` | `00 28 00 b4` | cbz x0,0x009fc260 | `CONDITIONAL_JUMP`
<a id="insn-009fbd64"></a> `009fbd64` | `f5 1f 40 f9` | ldr x21,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-009fbd68"></a> `009fbd68` | `b5 00 00 b4` | cbz x21,0x009fbd7c | `CONDITIONAL_JUMP`
<a id="insn-009fbd6c"></a> `009fbd6c` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-009fbd70"></a> `009fbd70` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009fbd74"></a> `009fbd74` | `07 64 09 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-009fbd78"></a> `009fbd78` | `60 28 00 b4` | cbz x0,0x009fc284 | `CONDITIONAL_JUMP`
<a id="insn-009fbd7c"></a> `009fbd7c` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009fbd80"></a> `009fbd80` | `68 00 00 36` | tbz w8,#0x0,0x009fbd8c | `CONDITIONAL_JUMP`
<a id="insn-009fbd84"></a> `009fbd84` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-009fbd88"></a> `009fbd88` | `72 74 09 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-009fbd8c"></a> `009fbd8c` | `e8 23 41 39` | ldrb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009fbd90"></a> `009fbd90` | `68 00 00 36` | tbz w8,#0x0,0x009fbd9c | `CONDITIONAL_JUMP`
<a id="insn-009fbd94"></a> `009fbd94` | `e0 2f 40 f9` | ldr x0,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-009fbd98"></a> `009fbd98` | `6e 74 09 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-009fbd9c"></a> `009fbd9c` | `b7 f1 ff 97` | bl 0x009f8478 | `UNCONDITIONAL_CALL`
<a id="insn-009fbda0"></a> `009fbda0` | `d7 59 f9 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-009fbda4"></a> `009fbda4` | `88 14 00 90` | adrp x8,0xc8b000 | `FALL_THROUGH`
<a id="insn-009fbda8"></a> `009fbda8` | `08 01 31 91` | add x8,x8,#0xc40 | `FALL_THROUGH`
<a id="insn-009fbdac"></a> `009fbdac` | `b6 43 01 d1` | sub x22,x29,#0x50 | `FALL_THROUGH`
<a id="insn-009fbdb0"></a> `009fbdb0` | `ff 93 00 79` | strh wzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009fbdb4"></a> `009fbdb4` | `a8 03 1b f8` | stur x8,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-009fbdb8"></a> `009fbdb8` | `08 e1 85 52` | mov w8,#0x2f08 | `FALL_THROUGH`
<a id="insn-009fbdbc"></a> `009fbdbc` | `b6 03 1d f8` | stur x22,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-009fbdc0"></a> `009fbdc0` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-009fbdc4"></a> `009fbdc4` | `e1 23 01 91` | add x1,sp,#0x48 | `FALL_THROUGH`
<a id="insn-009fbdc8"></a> `009fbdc8` | `a5 43 01 d1` | sub x5,x29,#0x50 | `FALL_THROUGH`
<a id="insn-009fbdcc"></a> `009fbdcc` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-009fbdd0"></a> `009fbdd0` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-009fbdd4"></a> `009fbdd4` | `84 00 80 52` | mov w4,#0x4 | `FALL_THROUGH`
<a id="insn-009fbdd8"></a> `009fbdd8` | `a5 fe fa 97` | bl 0x008bb86c | `UNCONDITIONAL_CALL`
<a id="insn-009fbddc"></a> `009fbddc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-009fbde0"></a> `009fbde0` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-009fbde4"></a> `009fbde4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-009fbde8"></a> `009fbde8` | `22 01 80 12` | mov w2,#0xfffffff6 | `FALL_THROUGH`
<a id="insn-009fbdec"></a> `009fbdec` | `83 6a 80 52` | mov w3,#0x354 | `FALL_THROUGH`
<a id="insn-009fbdf0"></a> `009fbdf0` | `c4 42 80 52` | mov w4,#0x216 | `FALL_THROUGH`
<a id="insn-009fbdf4"></a> `009fbdf4` | `18 c8 e9 97` | bl 0x0046de54 | `UNCONDITIONAL_CALL`
<a id="insn-009fbdf8"></a> `009fbdf8` | `e1 8b 40 a9` | ldp x1,x2,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009fbdfc"></a> `009fbdfc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009fbe00"></a> `009fbe00` | `c1 f9 fa 97` | bl 0x008ba504 | `UNCONDITIONAL_CALL`
<a id="insn-009fbe04"></a> `009fbe04` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-009fbe08"></a> `009fbe08` | `95 fa fa 97` | bl 0x008ba85c | `UNCONDITIONAL_CALL`
<a id="insn-009fbe0c"></a> `009fbe0c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-009fbe10"></a> `009fbe10` | `a0 03 5d f8` | ldur x0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-009fbe14"></a> `009fbe14` | `a8 43 01 d1` | sub x8,x29,#0x50 | `FALL_THROUGH`
<a id="insn-009fbe18"></a> `009fbe18` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-009fbe1c"></a> `009fbe1c` | `80 00 00 54` | b.eq 0x009fbe2c | `CONDITIONAL_JUMP`
<a id="insn-009fbe20"></a> `009fbe20` | `00 01 00 b4` | cbz x0,0x009fbe40 | `CONDITIONAL_JUMP`
<a id="insn-009fbe24"></a> `009fbe24` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-009fbe28"></a> `009fbe28` | `03 00 00 14` | b 0x009fbe34 | `UNCONDITIONAL_JUMP`
<a id="insn-009fbe2c"></a> `009fbe2c` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-009fbe30"></a> `009fbe30` | `a0 43 01 d1` | sub x0,x29,#0x50 | `FALL_THROUGH`
<a id="insn-009fbe34"></a> `009fbe34` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-009fbe38"></a> `009fbe38` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-009fbe3c"></a> `009fbe3c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009fbe40"></a> `009fbe40` | `e8 23 41 39` | ldrb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009fbe44"></a> `009fbe44` | `68 00 00 36` | tbz w8,#0x0,0x009fbe50 | `CONDITIONAL_JUMP`
<a id="insn-009fbe48"></a> `009fbe48` | `e0 2f 40 f9` | ldr x0,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-009fbe4c"></a> `009fbe4c` | `41 74 09 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-009fbe50"></a> `009fbe50` | `ab 59 f9 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-009fbe54"></a> `009fbe54` | `16 0f 86 52` | mov w22,#0x3078 | `FALL_THROUGH`
<a id="insn-009fbe58"></a> `009fbe58` | `41 05 80 52` | mov w1,#0x2a | `FALL_THROUGH`
<a id="insn-009fbe5c"></a> `009fbe5c` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-009fbe60"></a> `009fbe60` | `f5 1e 02 94` | bl 0x00a83a34 | `UNCONDITIONAL_CALL`
<a id="insn-009fbe64"></a> `009fbe64` | `57 03 80 52` | mov w23,#0x1a | `FALL_THROUGH`
<a id="insn-009fbe68"></a> `009fbe68` | `e9 e7 00 b2` | orr x9,xzr,#0x3333333333333333 | `FALL_THROUGH`
<a id="insn-009fbe6c"></a> `009fbe6c` | `01 e4 00 2f` | movi d1,#0x0 | `FALL_THROUGH`
<a id="insn-009fbe70"></a> `009fbe70` | `08 7c 17 1b` | mul w8,w0,w23 | `FALL_THROUGH`
<a id="insn-009fbe74"></a> `009fbe74` | `69 fe e7 f2` | movk x9,#0x3ff3, LSL #48 | `FALL_THROUGH`
<a id="insn-009fbe78"></a> `009fbe78` | `29 01 67 9e` | fmov d9,x9 | `FALL_THROUGH`
<a id="insn-009fbe7c"></a> `009fbe7c` | `00 01 62 1e` | scvtf d0,w8 | `FALL_THROUGH`
<a id="insn-009fbe80"></a> `009fbe80` | `08 00 d8 d2` | mov x8,#0xc00000000000 | `FALL_THROUGH`
<a id="insn-009fbe84"></a> `009fbe84` | `48 0a e8 f2` | movk x8,#0x4052, LSL #48 | `FALL_THROUGH`
<a id="insn-009fbe88"></a> `009fbe88` | `08 01 67 9e` | fmov d8,x8 | `FALL_THROUGH`
<a id="insn-009fbe8c"></a> `009fbe8c` | `00 20 49 1f` | fmadd d0,d0,d9,d8 | `FALL_THROUGH`
<a id="insn-009fbe90"></a> `009fbe90` | `00 28 61 1e` | fadd d0,d0,d1 | `FALL_THROUGH`
<a id="insn-009fbe94"></a> `009fbe94` | `08 00 78 1e` | fcvtzs w8,d0 | `FALL_THROUGH`
<a id="insn-009fbe98"></a> `009fbe98` | `19 21 00 11` | add w25,w8,#0x8 | `FALL_THROUGH`
<a id="insn-009fbe9c"></a> `009fbe9c` | `98 59 f9 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-009fbea0"></a> `009fbea0` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-009fbea4"></a> `009fbea4` | `61 05 80 52` | mov w1,#0x2b | `FALL_THROUGH`
<a id="insn-009fbea8"></a> `009fbea8` | `e3 1e 02 94` | bl 0x00a83a34 | `UNCONDITIONAL_CALL`
<a id="insn-009fbeac"></a> `009fbeac` | `08 7c 17 1b` | mul w8,w0,w23 | `FALL_THROUGH`
<a id="insn-009fbeb0"></a> `009fbeb0` | `20 03 62 1e` | scvtf d0,w25 | `FALL_THROUGH`
<a id="insn-009fbeb4"></a> `009fbeb4` | `01 01 62 1e` | scvtf d1,w8 | `FALL_THROUGH`
<a id="insn-009fbeb8"></a> `009fbeb8` | `21 20 49 1f` | fmadd d1,d1,d9,d8 | `FALL_THROUGH`
<a id="insn-009fbebc"></a> `009fbebc` | `20 28 60 1e` | fadd d0,d1,d0 | `FALL_THROUGH`
<a id="insn-009fbec0"></a> `009fbec0` | `16 00 78 1e` | fcvtzs w22,d0 | `FALL_THROUGH`
<a id="insn-009fbec4"></a> `009fbec4` | `d9 5a 00 11` | add w25,w22,#0x16 | `FALL_THROUGH`
<a id="insn-009fbec8"></a> `009fbec8` | `8d 59 f9 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-009fbecc"></a> `009fbecc` | `00 40 01 91` | add x0,x0,#0x50 | `FALL_THROUGH`
<a id="insn-009fbed0"></a> `009fbed0` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-009fbed4"></a> `009fbed4` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-009fbed8"></a> `009fbed8` | `2f a0 ff 97` | bl 0x009e3f94 | `UNCONDITIONAL_CALL`
<a id="insn-009fbedc"></a> `009fbedc` | `09 20 40 a9` | ldp x9,x8,[x0] | `FALL_THROUGH`
<a id="insn-009fbee0"></a> `009fbee0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009fbee4"></a> `009fbee4` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-009fbee8"></a> `009fbee8` | `29 4b 92 52` | mov w9,#0x9259 | `FALL_THROUGH`
<a id="insn-009fbeec"></a> `009fbeec` | `08 fd 42 d3` | lsr x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-009fbef0"></a> `009fbef0` | `89 24 a9 72` | movk w9,#0x4924, LSL #16 | `FALL_THROUGH`
<a id="insn-009fbef4"></a> `009fbef4` | `08 59 09 1b` | madd w8,w8,w9,w22 | `FALL_THROUGH`
<a id="insn-009fbef8"></a> `009fbef8` | `1a 49 00 11` | add w26,w8,#0x12 | `FALL_THROUGH`
<a id="insn-009fbefc"></a> `009fbefc` | `e8 f8 fa 97` | bl 0x008ba29c | `UNCONDITIONAL_CALL`
<a id="insn-009fbf00"></a> `009fbf00` | `28 fc 60 d3` | lsr x8,x1,#0x20 | `FALL_THROUGH`
<a id="insn-009fbf04"></a> `009fbf04` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-009fbf08"></a> `009fbf08` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-009fbf0c"></a> `009fbf0c` | `1b 09 01 51` | sub w27,w8,#0x42 | `FALL_THROUGH`
<a id="insn-009fbf10"></a> `009fbf10` | `5f 03 1b 6b` | cmp w26,w27 | `FALL_THROUGH`
<a id="insn-009fbf14"></a> `009fbf14` | `ad 02 00 54` | b.le 0x009fbf68 | `CONDITIONAL_JUMP`
<a id="insn-009fbf18"></a> `009fbf18` | `fc fe 60 d3` | lsr x28,x23,#0x20 | `FALL_THROUGH`
<a id="insn-009fbf1c"></a> `009fbf1c` | `78 59 f9 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-009fbf20"></a> `009fbf20` | `60 03 22 1e` | scvtf s0,w27 | `FALL_THROUGH`
<a id="insn-009fbf24"></a> `009fbf24` | `41 03 22 1e` | scvtf s1,w26 | `FALL_THROUGH`
<a id="insn-009fbf28"></a> `009fbf28` | `c8 02 17 0b` | add w8,w22,w23 | `FALL_THROUGH`
<a id="insn-009fbf2c"></a> `009fbf2c` | `02 b1 00 51` | sub w2,w8,#0x2c | `FALL_THROUGH`
<a id="insn-009fbf30"></a> `009fbf30` | `08 dc 4c 91` | add x8,x0,#0x337, LSL #12 | `FALL_THROUGH`
<a id="insn-009fbf34"></a> `009fbf34` | `83 87 00 11` | add w3,w28,#0x21 | `FALL_THROUGH`
<a id="insn-009fbf38"></a> `009fbf38` | `00 41 36 91` | add x0,x8,#0xd90 | `FALL_THROUGH`
<a id="insn-009fbf3c"></a> `009fbf3c` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-009fbf40"></a> `009fbf40` | `84 04 80 52` | mov w4,#0x24 | `FALL_THROUGH`
<a id="insn-009fbf44"></a> `009fbf44` | `3b 00 80 52` | mov w27,#0x1 | `FALL_THROUGH`
<a id="insn-009fbf48"></a> `009fbf48` | `02 40 20 1e` | fmov s2,s0 | `FALL_THROUGH`
<a id="insn-009fbf4c"></a> `009fbf4c` | `ca 37 03 94` | bl 0x00ac9e74 | `UNCONDITIONAL_CALL`
<a id="insn-009fbf50"></a> `009fbf50` | `9f 56 00 b9` | str wzr,[x20, #0x54] | `FALL_THROUGH`
<a id="insn-009fbf54"></a> `009fbf54` | `6a 59 f9 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-009fbf58"></a> `009fbf58` | `88 ec 8f 52` | mov w8,#0x7f64 | `FALL_THROUGH`
<a id="insn-009fbf5c"></a> `009fbf5c` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-009fbf60"></a> `009fbf60` | `1b 68 28 38` | strb w27,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-009fbf64"></a> `009fbf64` | `05 00 00 14` | b 0x009fbf78 | `UNCONDITIONAL_JUMP`
<a id="insn-009fbf68"></a> `009fbf68` | `65 59 f9 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-009fbf6c"></a> `009fbf6c` | `08 dc 4c 91` | add x8,x0,#0x337, LSL #12 | `FALL_THROUGH`
<a id="insn-009fbf70"></a> `009fbf70` | `00 41 36 91` | add x0,x8,#0xd90 | `FALL_THROUGH`
<a id="insn-009fbf74"></a> `009fbf74` | `d1 37 03 94` | bl 0x00ac9eb8 | `UNCONDITIONAL_CALL`
<a id="insn-009fbf78"></a> `009fbf78` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-009fbf7c"></a> `009fbf7c` | `ed 73 09 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-009fbf80"></a> `009fbf80` | `88 14 00 90` | adrp x8,0xc8b000 | `FALL_THROUGH`
<a id="insn-009fbf84"></a> `009fbf84` | `08 01 33 91` | add x8,x8,#0xcc0 | `FALL_THROUGH`
<a id="insn-009fbf88"></a> `009fbf88` | `17 58 01 a9` | stp x23,x22,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-009fbf8c"></a> `009fbf8c` | `08 50 00 a9` | stp x8,x20,[x0] | `FALL_THROUGH`
<a id="insn-009fbf90"></a> `009fbf90` | `19 68 04 29` | stp w25,w26,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-009fbf94"></a> `009fbf94` | `a0 03 1a f8` | stur x0,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-009fbf98"></a> `009fbf98` | `a1 03 02 d1` | sub x1,x29,#0x80 | `FALL_THROUGH`
<a id="insn-009fbf9c"></a> `009fbf9c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009fbfa0"></a> `009fbfa0` | `b6 03 02 d1` | sub x22,x29,#0x80 | `FALL_THROUGH`
<a id="insn-009fbfa4"></a> `009fbfa4` | `8b f9 fa 97` | bl 0x008ba5d0 | `UNCONDITIONAL_CALL`
<a id="insn-009fbfa8"></a> `009fbfa8` | `a0 03 5a f8` | ldur x0,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-009fbfac"></a> `009fbfac` | `1f 00 16 eb` | cmp x0,x22 | `FALL_THROUGH`
<a id="insn-009fbfb0"></a> `009fbfb0` | `80 00 00 54` | b.eq 0x009fbfc0 | `CONDITIONAL_JUMP`
<a id="insn-009fbfb4"></a> `009fbfb4` | `00 01 00 b4` | cbz x0,0x009fbfd4 | `CONDITIONAL_JUMP`
<a id="insn-009fbfb8"></a> `009fbfb8` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-009fbfbc"></a> `009fbfbc` | `03 00 00 14` | b 0x009fbfc8 | `UNCONDITIONAL_JUMP`
<a id="insn-009fbfc0"></a> `009fbfc0` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-009fbfc4"></a> `009fbfc4` | `a0 03 02 d1` | sub x0,x29,#0x80 | `FALL_THROUGH`
<a id="insn-009fbfc8"></a> `009fbfc8` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-009fbfcc"></a> `009fbfcc` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-009fbfd0"></a> `009fbfd0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009fbfd4"></a> `009fbfd4` | `88 14 00 90` | adrp x8,0xc8b000 | `FALL_THROUGH`
<a id="insn-009fbfd8"></a> `009fbfd8` | `08 01 35 91` | add x8,x8,#0xd40 | `FALL_THROUGH`
<a id="insn-009fbfdc"></a> `009fbfdc` | `f6 43 02 91` | add x22,sp,#0x90 | `FALL_THROUGH`
<a id="insn-009fbfe0"></a> `009fbfe0` | `e8 4f 09 a9` | stp x8,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-009fbfe4"></a> `009fbfe4` | `f4 53 00 f9` | str x20,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-009fbfe8"></a> `009fbfe8` | `f6 5b 00 f9` | str x22,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-009fbfec"></a> `009fbfec` | `e1 43 02 91` | add x1,sp,#0x90 | `FALL_THROUGH`
<a id="insn-009fbff0"></a> `009fbff0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009fbff4"></a> `009fbff4` | `ad f9 fa 97` | bl 0x008ba6a8 | `UNCONDITIONAL_CALL`
<a id="insn-009fbff8"></a> `009fbff8` | `e0 5b 40 f9` | ldr x0,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-009fbffc"></a> `009fbffc` | `1f 00 16 eb` | cmp x0,x22 | `FALL_THROUGH`
<a id="insn-009fc000"></a> `009fc000` | `80 00 00 54` | b.eq 0x009fc010 | `CONDITIONAL_JUMP`
<a id="insn-009fc004"></a> `009fc004` | `00 01 00 b4` | cbz x0,0x009fc024 | `CONDITIONAL_JUMP`
<a id="insn-009fc008"></a> `009fc008` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-009fc00c"></a> `009fc00c` | `03 00 00 14` | b 0x009fc018 | `UNCONDITIONAL_JUMP`
<a id="insn-009fc010"></a> `009fc010` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-009fc014"></a> `009fc014` | `e0 43 02 91` | add x0,sp,#0x90 | `FALL_THROUGH`
<a id="insn-009fc018"></a> `009fc018` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-009fc01c"></a> `009fc01c` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-009fc020"></a> `009fc020` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009fc024"></a> `009fc024` | `00 10 2e 1e` | fmov s0,0x3f800000 | `FALL_THROUGH`
<a id="insn-009fc028"></a> `009fc028` | `e8 23 01 91` | add x8,sp,#0x48 | `FALL_THROUGH`
<a id="insn-009fc02c"></a> `009fc02c` | `60 e2 04 91` | add x0,x19,#0x138 | `FALL_THROUGH`
<a id="insn-009fc030"></a> `009fc030` | `21 19 80 52` | mov w1,#0xc9 | `FALL_THROUGH`
<a id="insn-009fc034"></a> `009fc034` | `e2 4c 80 52` | mov w2,#0x267 | `FALL_THROUGH`
<a id="insn-009fc038"></a> `009fc038` | `23 12 80 52` | mov w3,#0x91 | `FALL_THROUGH`
<a id="insn-009fc03c"></a> `009fc03c` | `c4 04 80 52` | mov w4,#0x26 | `FALL_THROUGH`
<a id="insn-009fc040"></a> `009fc040` | `65 14 80 52` | mov w5,#0xa3 | `FALL_THROUGH`
<a id="insn-009fc044"></a> `009fc044` | `86 14 80 52` | mov w6,#0xa4 | `FALL_THROUGH`
<a id="insn-009fc048"></a> `009fc048` | `53 31 01 94` | bl 0x00a48594 | `UNCONDITIONAL_CALL`
<a id="insn-009fc04c"></a> `009fc04c` | `e0 27 40 f9` | ldr x0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009fc050"></a> `009fc050` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-009fc054"></a> `009fc054` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009fc058"></a> `009fc058` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-009fc05c"></a> `009fc05c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009fc060"></a> `009fc060` | `f4 27 40 f9` | ldr x20,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009fc064"></a> `009fc064` | `e8 c3 00 91` | add x8,sp,#0x30 | `FALL_THROUGH`
<a id="insn-009fc068"></a> `009fc068` | `60 e2 04 91` | add x0,x19,#0x138 | `FALL_THROUGH`
<a id="insn-009fc06c"></a> `009fc06c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-009fc070"></a> `009fc070` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-009fc074"></a> `009fc074` | `43 14 80 52` | mov w3,#0xa2 | `FALL_THROUGH`
<a id="insn-009fc078"></a> `009fc078` | `33 2e 01 94` | bl 0x00a47944 | `UNCONDITIONAL_CALL`
<a id="insn-009fc07c"></a> `009fc07c` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009fc080"></a> `009fc080` | `ff 1b 00 f9` | str xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009fc084"></a> `009fc084` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009fc088"></a> `009fc088` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-009fc08c"></a> `009fc08c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009fc090"></a> `009fc090` | `cf 2d 01 94` | bl 0x00a477cc | `UNCONDITIONAL_CALL`
<a id="insn-009fc094"></a> `009fc094` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-009fc098"></a> `009fc098` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009fc09c"></a> `009fc09c` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-009fc0a0"></a> `009fc0a0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009fc0a4"></a> `009fc0a4` | `16 15 00 90` | adrp x22,0xc9c000 | `FALL_THROUGH`
<a id="insn-009fc0a8"></a> `009fc0a8` | `f3 0f 40 f9` | ldr x19,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009fc0ac"></a> `009fc0ac` | `d6 06 42 f9` | ldr x22,[x22, #0x408] | `FALL_THROUGH`
<a id="insn-009fc0b0"></a> `009fc0b0` | `ff 0f 00 f9` | str xzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009fc0b4"></a> `009fc0b4` | `f3 00 00 b4` | cbz x19,0x009fc0d0 | `CONDITIONAL_JUMP`
<a id="insn-009fc0b8"></a> `009fc0b8` | `c8 42 00 91` | add x8,x22,#0x10 | `FALL_THROUGH`
<a id="insn-009fc0bc"></a> `009fc0bc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009fc0c0"></a> `009fc0c0` | `08 04 05 f8` | str x8,[x0], #0x50 | `FALL_THROUGH`
<a id="insn-009fc0c4"></a> `009fc0c4` | `bd 73 ef 97` | bl 0x005d8fb8 | `UNCONDITIONAL_CALL`
<a id="insn-009fc0c8"></a> `009fc0c8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009fc0cc"></a> `009fc0cc` | `a1 73 09 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-009fc0d0"></a> `009fc0d0` | `17 15 00 90` | adrp x23,0xc9c000 | `FALL_THROUGH`
<a id="insn-009fc0d4"></a> `009fc0d4` | `f3 1b 40 f9` | ldr x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009fc0d8"></a> `009fc0d8` | `f7 0a 42 f9` | ldr x23,[x23, #0x410] | `FALL_THROUGH`
<a id="insn-009fc0dc"></a> `009fc0dc` | `ff 1b 00 f9` | str xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009fc0e0"></a> `009fc0e0` | `b3 02 00 b4` | cbz x19,0x009fc134 | `CONDITIONAL_JUMP`
<a id="insn-009fc0e4"></a> `009fc0e4` | `74 5a 40 f9` | ldr x20,[x19, #0xb0] | `FALL_THROUGH`
<a id="insn-009fc0e8"></a> `009fc0e8` | `e8 42 00 91` | add x8,x23,#0x10 | `FALL_THROUGH`
<a id="insn-009fc0ec"></a> `009fc0ec` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-009fc0f0"></a> `009fc0f0` | `74 01 00 b4` | cbz x20,0x009fc11c | `CONDITIONAL_JUMP`
<a id="insn-009fc0f4"></a> `009fc0f4` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009fc0f8"></a> `009fc0f8` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009fc0fc"></a> `009fc0fc` | `25 63 09 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-009fc100"></a> `009fc100` | `e0 00 00 b5` | cbnz x0,0x009fc11c | `CONDITIONAL_JUMP`
<a id="insn-009fc104"></a> `009fc104` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-009fc108"></a> `009fc108` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009fc10c"></a> `009fc10c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009fc110"></a> `009fc110` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009fc114"></a> `009fc114` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009fc118"></a> `009fc118` | `82 73 09 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-009fc11c"></a> `009fc11c` | `c8 42 00 91` | add x8,x22,#0x10 | `FALL_THROUGH`
<a id="insn-009fc120"></a> `009fc120` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009fc124"></a> `009fc124` | `08 04 05 f8` | str x8,[x0], #0x50 | `FALL_THROUGH`
<a id="insn-009fc128"></a> `009fc128` | `a4 73 ef 97` | bl 0x005d8fb8 | `UNCONDITIONAL_CALL`
<a id="insn-009fc12c"></a> `009fc12c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009fc130"></a> `009fc130` | `88 73 09 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-009fc134"></a> `009fc134` | `f2 58 f9 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-009fc138"></a> `009fc138` | `e8 27 40 f9` | ldr x8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009fc13c"></a> `009fc13c` | `f3 83 01 91` | add x19,sp,#0x60 | `FALL_THROUGH`
<a id="insn-009fc140"></a> `009fc140` | `ff 27 00 f9` | str xzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009fc144"></a> `009fc144` | `f3 43 00 f9` | str x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-009fc148"></a> `009fc148` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009fc14c"></a> `009fc14c` | `68 14 00 f0` | adrp x8,0xc8b000 | `FALL_THROUGH`
<a id="insn-009fc150"></a> `009fc150` | `08 01 37 91` | add x8,x8,#0xdc0 | `FALL_THROUGH`
<a id="insn-009fc154"></a> `009fc154` | `e8 57 06 a9` | stp x8,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009fc158"></a> `009fc158` | `08 e7 85 52` | mov w8,#0x2f38 | `FALL_THROUGH`
<a id="insn-009fc15c"></a> `009fc15c` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-009fc160"></a> `009fc160` | `e6 63 00 91` | add x6,sp,#0x18 | `FALL_THROUGH`
<a id="insn-009fc164"></a> `009fc164` | `e7 83 01 91` | add x7,sp,#0x60 | `FALL_THROUGH`
<a id="insn-009fc168"></a> `009fc168` | `21 1a 80 52` | mov w1,#0xd1 | `FALL_THROUGH`
<a id="insn-009fc16c"></a> `009fc16c` | `22 10 80 52` | mov w2,#0x81 | `FALL_THROUGH`
<a id="insn-009fc170"></a> `009fc170` | `23 49 80 52` | mov w3,#0x249 | `FALL_THROUGH`
<a id="insn-009fc174"></a> `009fc174` | `24 12 80 52` | mov w4,#0x91 | `FALL_THROUGH`
<a id="insn-009fc178"></a> `009fc178` | `85 07 80 52` | mov w5,#0x3c | `FALL_THROUGH`
<a id="insn-009fc17c"></a> `009fc17c` | `9d ef fa 97` | bl 0x008b7ff0 | `UNCONDITIONAL_CALL`
<a id="insn-009fc180"></a> `009fc180` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-009fc184"></a> `009fc184` | `1f 00 13 eb` | cmp x0,x19 | `FALL_THROUGH`
<a id="insn-009fc188"></a> `009fc188` | `80 00 00 54` | b.eq 0x009fc198 | `CONDITIONAL_JUMP`
<a id="insn-009fc18c"></a> `009fc18c` | `00 01 00 b4` | cbz x0,0x009fc1ac | `CONDITIONAL_JUMP`
<a id="insn-009fc190"></a> `009fc190` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-009fc194"></a> `009fc194` | `03 00 00 14` | b 0x009fc1a0 | `UNCONDITIONAL_JUMP`
<a id="insn-009fc198"></a> `009fc198` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-009fc19c"></a> `009fc19c` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-009fc1a0"></a> `009fc1a0` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-009fc1a4"></a> `009fc1a4` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-009fc1a8"></a> `009fc1a8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009fc1ac"></a> `009fc1ac` | `f3 0f 40 f9` | ldr x19,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009fc1b0"></a> `009fc1b0` | `ff 0f 00 f9` | str xzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009fc1b4"></a> `009fc1b4` | `f3 00 00 b4` | cbz x19,0x009fc1d0 | `CONDITIONAL_JUMP`
<a id="insn-009fc1b8"></a> `009fc1b8` | `c8 42 00 91` | add x8,x22,#0x10 | `FALL_THROUGH`
<a id="insn-009fc1bc"></a> `009fc1bc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009fc1c0"></a> `009fc1c0` | `08 04 05 f8` | str x8,[x0], #0x50 | `FALL_THROUGH`
<a id="insn-009fc1c4"></a> `009fc1c4` | `7d 73 ef 97` | bl 0x005d8fb8 | `UNCONDITIONAL_CALL`
<a id="insn-009fc1c8"></a> `009fc1c8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009fc1cc"></a> `009fc1cc` | `61 73 09 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-009fc1d0"></a> `009fc1d0` | `f3 27 40 f9` | ldr x19,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009fc1d4"></a> `009fc1d4` | `ff 27 00 f9` | str xzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009fc1d8"></a> `009fc1d8` | `b3 02 00 b4` | cbz x19,0x009fc22c | `CONDITIONAL_JUMP`
<a id="insn-009fc1dc"></a> `009fc1dc` | `74 5a 40 f9` | ldr x20,[x19, #0xb0] | `FALL_THROUGH`
<a id="insn-009fc1e0"></a> `009fc1e0` | `e8 42 00 91` | add x8,x23,#0x10 | `FALL_THROUGH`
<a id="insn-009fc1e4"></a> `009fc1e4` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-009fc1e8"></a> `009fc1e8` | `74 01 00 b4` | cbz x20,0x009fc214 | `CONDITIONAL_JUMP`
<a id="insn-009fc1ec"></a> `009fc1ec` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009fc1f0"></a> `009fc1f0` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009fc1f4"></a> `009fc1f4` | `e7 62 09 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-009fc1f8"></a> `009fc1f8` | `e0 00 00 b5` | cbnz x0,0x009fc214 | `CONDITIONAL_JUMP`
<a id="insn-009fc1fc"></a> `009fc1fc` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-009fc200"></a> `009fc200` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009fc204"></a> `009fc204` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009fc208"></a> `009fc208` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009fc20c"></a> `009fc20c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009fc210"></a> `009fc210` | `44 73 09 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-009fc214"></a> `009fc214` | `c8 42 00 91` | add x8,x22,#0x10 | `FALL_THROUGH`
<a id="insn-009fc218"></a> `009fc218` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009fc21c"></a> `009fc21c` | `08 04 05 f8` | str x8,[x0], #0x50 | `FALL_THROUGH`
<a id="insn-009fc220"></a> `009fc220` | `66 73 ef 97` | bl 0x005d8fb8 | `UNCONDITIONAL_CALL`
<a id="insn-009fc224"></a> `009fc224` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009fc228"></a> `009fc228` | `4a 73 09 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-009fc22c"></a> `009fc22c` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-009fc230"></a> `009fc230` | `a9 03 5e f8` | ldur x9,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-009fc234"></a> `009fc234` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009fc238"></a> `009fc238` | `81 10 00 54` | b.ne 0x009fc448 | `CONDITIONAL_JUMP`
<a id="insn-009fc23c"></a> `009fc23c` | `f4 4f 59 a9` | ldp x20,x19,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-009fc240"></a> `009fc240` | `f6 57 58 a9` | ldp x22,x21,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-009fc244"></a> `009fc244` | `f8 5f 57 a9` | ldp x24,x23,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-009fc248"></a> `009fc248` | `fa 67 56 a9` | ldp x26,x25,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-009fc24c"></a> `009fc24c` | `fc 6f 55 a9` | ldp x28,x27,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-009fc250"></a> `009fc250` | `fd 7b 54 a9` | ldp x29,x30,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-009fc254"></a> `009fc254` | `e9 23 53 6d` | ldp d9,d8,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-009fc258"></a> `009fc258` | `ff 83 06 91` | add sp,sp,#0x1a0 | `FALL_THROUGH`
<a id="insn-009fc25c"></a> `009fc25c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-009fc260"></a> `009fc260` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-009fc264"></a> `009fc264` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009fc268"></a> `009fc268` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009fc26c"></a> `009fc26c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009fc270"></a> `009fc270` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009fc274"></a> `009fc274` | `2b 73 09 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-009fc278"></a> `009fc278` | `f5 1f 40 f9` | ldr x21,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-009fc27c"></a> `009fc27c` | `95 d7 ff b5` | cbnz x21,0x009fbd6c | `CONDITIONAL_JUMP`
<a id="insn-009fc280"></a> `009fc280` | `bf fe ff 17` | b 0x009fbd7c | `UNCONDITIONAL_JUMP`
<a id="insn-009fc284"></a> `009fc284` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-009fc288"></a> `009fc288` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009fc28c"></a> `009fc28c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009fc290"></a> `009fc290` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009fc294"></a> `009fc294` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009fc298"></a> `009fc298` | `22 73 09 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-009fc29c"></a> `009fc29c` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009fc2a0"></a> `009fc2a0` | `28 d7 07 37` | tbnz w8,#0x0,0x009fbd84 | `CONDITIONAL_JUMP`
<a id="insn-009fc2a4"></a> `009fc2a4` | `ba fe ff 17` | b 0x009fbd8c | `UNCONDITIONAL_JUMP`
<a id="insn-009fc2a8"></a> `009fc2a8` | `40 15 00 b0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-009fc2ac"></a> `009fc2ac` | `00 e0 3f 91` | add x0,x0,#0xff8 | `FALL_THROUGH`
<a id="insn-009fc2b0"></a> `009fc2b0` | `10 73 09 94` | bl 0x00c58ef0 | `UNCONDITIONAL_CALL`
<a id="insn-009fc2b4"></a> `009fc2b4` | `40 d1 ff 34` | cbz w0,0x009fbcdc | `CONDITIONAL_JUMP`
<a id="insn-009fc2b8"></a> `009fc2b8` | `41 15 00 b0` | adrp x1,0xca5000 | `FALL_THROUGH`
<a id="insn-009fc2bc"></a> `009fc2bc` | `21 00 3f 91` | add x1,x1,#0xfc0 | `FALL_THROUGH`
<a id="insn-009fc2c0"></a> `009fc2c0` | `00 d4 ff f0` | adrp x0,0x47f000 | `FALL_THROUGH`
<a id="insn-009fc2c4"></a> `009fc2c4` | `00 50 04 91` | add x0,x0,#0x114 | `FALL_THROUGH`
<a id="insn-009fc2c8"></a> `009fc2c8` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-009fc2cc"></a> `009fc2cc` | `42 13 00 90` | adrp x2,0xc64000 | `FALL_THROUGH`
<a id="insn-009fc2d0"></a> `009fc2d0` | `42 c0 00 91` | add x2,x2,#0x30 | `FALL_THROUGH`
<a id="insn-009fc2d4"></a> `009fc2d4` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-009fc2d8"></a> `009fc2d8` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-009fc2dc"></a> `009fc2dc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-009fc2e0"></a> `009fc2e0` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-009fc2e4"></a> `009fc2e4` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-009fc2e8"></a> `009fc2e8` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-009fc2ec"></a> `009fc2ec` | `f9 72 09 94` | bl 0x00c58ed0 | `UNCONDITIONAL_CALL`
<a id="insn-009fc2f0"></a> `009fc2f0` | `40 15 00 b0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-009fc2f4"></a> `009fc2f4` | `00 e0 3f 91` | add x0,x0,#0xff8 | `FALL_THROUGH`
<a id="insn-009fc2f8"></a> `009fc2f8` | `06 73 09 94` | bl 0x00c58f10 | `UNCONDITIONAL_CALL`
<a id="insn-009fc2fc"></a> `009fc2fc` | `78 fe ff 17` | b 0x009fbcdc | `UNCONDITIONAL_JUMP`
<a id="insn-009fc448"></a> `009fc448` | `ce 72 09 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009fbbcc`](#insn-009fbbcc) 範囲 `[['009fbbcc', '009fbc0b']]`
  - `CONDITIONAL_JUMP` [`009fbc08`](#insn-009fbc08) → [`009fbc30`](#insn-009fbc30)
  - `FALL_THROUGH` [`009fbc08`](#insn-009fbc08) → [`009fbc0c`](#insn-009fbc0c)
- ブロック [`009fbc0c`](#insn-009fbc0c) 範囲 `[['009fbc0c', '009fbc2f']]`
  - `UNCONDITIONAL_JUMP` [`009fbc2c`](#insn-009fbc2c) → [`009fbc34`](#insn-009fbc34)
- ブロック [`009fbc30`](#insn-009fbc30) 範囲 `[['009fbc30', '009fbc33']]`
  - `FALL_THROUGH` [`009fbc30`](#insn-009fbc30) → [`009fbc34`](#insn-009fbc34)
- ブロック [`009fbc34`](#insn-009fbc34) 範囲 `[['009fbc34', '009fbc43']]`
  - `FALL_THROUGH` [`009fbc40`](#insn-009fbc40) → [`009fbc44`](#insn-009fbc44)
- ブロック [`009fbc44`](#insn-009fbc44) 範囲 `[['009fbc44', '009fbc67']]`
  - `FALL_THROUGH` [`009fbc64`](#insn-009fbc64) → [`009fbc68`](#insn-009fbc68)
- ブロック [`009fbc68`](#insn-009fbc68) 範囲 `[['009fbc68', '009fbc87']]`
  - `CONDITIONAL_JUMP` [`009fbc84`](#insn-009fbc84) → [`009fbc90`](#insn-009fbc90)
  - `FALL_THROUGH` [`009fbc84`](#insn-009fbc84) → [`009fbc88`](#insn-009fbc88)
- ブロック [`009fbc88`](#insn-009fbc88) 範囲 `[['009fbc88', '009fbc8b']]`
  - `FALL_THROUGH` [`009fbc88`](#insn-009fbc88) → [`009fbc8c`](#insn-009fbc8c)
- ブロック [`009fbc8c`](#insn-009fbc8c) 範囲 `[['009fbc8c', '009fbc8f']]`
  - `FALL_THROUGH` [`009fbc8c`](#insn-009fbc8c) → [`009fbc90`](#insn-009fbc90)
- ブロック [`009fbc90`](#insn-009fbc90) 範囲 `[['009fbc90', '009fbcc3']]`
  - `CONDITIONAL_JUMP` [`009fbcc0`](#insn-009fbcc0) → [`009fbccc`](#insn-009fbccc)
  - `FALL_THROUGH` [`009fbcc0`](#insn-009fbcc0) → [`009fbcc4`](#insn-009fbcc4)
- ブロック [`009fbcc4`](#insn-009fbcc4) 範囲 `[['009fbcc4', '009fbccb']]`
  - `FALL_THROUGH` [`009fbcc8`](#insn-009fbcc8) → [`009fbccc`](#insn-009fbccc)
- ブロック [`009fbccc`](#insn-009fbccc) 範囲 `[['009fbccc', '009fbcdb']]`
  - `CONDITIONAL_JUMP` [`009fbcd8`](#insn-009fbcd8) → [`009fc2a8`](#insn-009fc2a8)
  - `FALL_THROUGH` [`009fbcd8`](#insn-009fbcd8) → [`009fbcdc`](#insn-009fbcdc)
- ブロック [`009fbcdc`](#insn-009fbcdc) 範囲 `[['009fbcdc', '009fbcff']]`
  - `FALL_THROUGH` [`009fbcfc`](#insn-009fbcfc) → [`009fbd00`](#insn-009fbd00)
- ブロック [`009fbd00`](#insn-009fbd00) 範囲 `[['009fbd00', '009fbd0f']]`
  - `FALL_THROUGH` [`009fbd0c`](#insn-009fbd0c) → [`009fbd10`](#insn-009fbd10)
- ブロック [`009fbd10`](#insn-009fbd10) 範囲 `[['009fbd10', '009fbd53']]`
  - `CONDITIONAL_JUMP` [`009fbd50`](#insn-009fbd50) → [`009fbd64`](#insn-009fbd64)
  - `FALL_THROUGH` [`009fbd50`](#insn-009fbd50) → [`009fbd54`](#insn-009fbd54)
- ブロック [`009fbd54`](#insn-009fbd54) 範囲 `[['009fbd54', '009fbd63']]`
  - `CONDITIONAL_JUMP` [`009fbd60`](#insn-009fbd60) → [`009fc260`](#insn-009fc260)
  - `FALL_THROUGH` [`009fbd60`](#insn-009fbd60) → [`009fbd64`](#insn-009fbd64)
- ブロック [`009fbd64`](#insn-009fbd64) 範囲 `[['009fbd64', '009fbd6b']]`
  - `CONDITIONAL_JUMP` [`009fbd68`](#insn-009fbd68) → [`009fbd7c`](#insn-009fbd7c)
  - `FALL_THROUGH` [`009fbd68`](#insn-009fbd68) → [`009fbd6c`](#insn-009fbd6c)
- ブロック [`009fbd6c`](#insn-009fbd6c) 範囲 `[['009fbd6c', '009fbd7b']]`
  - `CONDITIONAL_JUMP` [`009fbd78`](#insn-009fbd78) → [`009fc284`](#insn-009fc284)
  - `FALL_THROUGH` [`009fbd78`](#insn-009fbd78) → [`009fbd7c`](#insn-009fbd7c)
- ブロック [`009fbd7c`](#insn-009fbd7c) 範囲 `[['009fbd7c', '009fbd83']]`
  - `CONDITIONAL_JUMP` [`009fbd80`](#insn-009fbd80) → [`009fbd8c`](#insn-009fbd8c)
  - `FALL_THROUGH` [`009fbd80`](#insn-009fbd80) → [`009fbd84`](#insn-009fbd84)
- ブロック [`009fbd84`](#insn-009fbd84) 範囲 `[['009fbd84', '009fbd8b']]`
  - `FALL_THROUGH` [`009fbd88`](#insn-009fbd88) → [`009fbd8c`](#insn-009fbd8c)
- ブロック [`009fbd8c`](#insn-009fbd8c) 範囲 `[['009fbd8c', '009fbd93']]`
  - `CONDITIONAL_JUMP` [`009fbd90`](#insn-009fbd90) → [`009fbd9c`](#insn-009fbd9c)
  - `FALL_THROUGH` [`009fbd90`](#insn-009fbd90) → [`009fbd94`](#insn-009fbd94)
- ブロック [`009fbd94`](#insn-009fbd94) 範囲 `[['009fbd94', '009fbd9b']]`
  - `FALL_THROUGH` [`009fbd98`](#insn-009fbd98) → [`009fbd9c`](#insn-009fbd9c)
- ブロック [`009fbd9c`](#insn-009fbd9c) 範囲 `[['009fbd9c', '009fbe1f']]`
  - `CONDITIONAL_JUMP` [`009fbe1c`](#insn-009fbe1c) → [`009fbe2c`](#insn-009fbe2c)
  - `FALL_THROUGH` [`009fbe1c`](#insn-009fbe1c) → [`009fbe20`](#insn-009fbe20)
- ブロック [`009fbe20`](#insn-009fbe20) 範囲 `[['009fbe20', '009fbe23']]`
  - `CONDITIONAL_JUMP` [`009fbe20`](#insn-009fbe20) → [`009fbe40`](#insn-009fbe40)
  - `FALL_THROUGH` [`009fbe20`](#insn-009fbe20) → [`009fbe24`](#insn-009fbe24)
- ブロック [`009fbe24`](#insn-009fbe24) 範囲 `[['009fbe24', '009fbe2b']]`
  - `UNCONDITIONAL_JUMP` [`009fbe28`](#insn-009fbe28) → [`009fbe34`](#insn-009fbe34)
- ブロック [`009fbe2c`](#insn-009fbe2c) 範囲 `[['009fbe2c', '009fbe33']]`
  - `FALL_THROUGH` [`009fbe30`](#insn-009fbe30) → [`009fbe34`](#insn-009fbe34)
- ブロック [`009fbe34`](#insn-009fbe34) 範囲 `[['009fbe34', '009fbe3f']]`
  - `FALL_THROUGH` [`009fbe3c`](#insn-009fbe3c) → [`009fbe40`](#insn-009fbe40)
- ブロック [`009fbe40`](#insn-009fbe40) 範囲 `[['009fbe40', '009fbe47']]`
  - `CONDITIONAL_JUMP` [`009fbe44`](#insn-009fbe44) → [`009fbe50`](#insn-009fbe50)
  - `FALL_THROUGH` [`009fbe44`](#insn-009fbe44) → [`009fbe48`](#insn-009fbe48)
- ブロック [`009fbe48`](#insn-009fbe48) 範囲 `[['009fbe48', '009fbe4f']]`
  - `FALL_THROUGH` [`009fbe4c`](#insn-009fbe4c) → [`009fbe50`](#insn-009fbe50)
- ブロック [`009fbe50`](#insn-009fbe50) 範囲 `[['009fbe50', '009fbe87']]`
  - `FALL_THROUGH` [`009fbe84`](#insn-009fbe84) → [`009fbe88`](#insn-009fbe88)
- ブロック [`009fbe88`](#insn-009fbe88) 範囲 `[['009fbe88', '009fbf17']]`
  - `CONDITIONAL_JUMP` [`009fbf14`](#insn-009fbf14) → [`009fbf68`](#insn-009fbf68)
  - `FALL_THROUGH` [`009fbf14`](#insn-009fbf14) → [`009fbf18`](#insn-009fbf18)
- ブロック [`009fbf18`](#insn-009fbf18) 範囲 `[['009fbf18', '009fbf27']]`
  - `FALL_THROUGH` [`009fbf24`](#insn-009fbf24) → [`009fbf28`](#insn-009fbf28)
- ブロック [`009fbf28`](#insn-009fbf28) 範囲 `[['009fbf28', '009fbf47']]`
  - `FALL_THROUGH` [`009fbf44`](#insn-009fbf44) → [`009fbf48`](#insn-009fbf48)
- ブロック [`009fbf48`](#insn-009fbf48) 範囲 `[['009fbf48', '009fbf67']]`
  - `UNCONDITIONAL_JUMP` [`009fbf64`](#insn-009fbf64) → [`009fbf78`](#insn-009fbf78)
- ブロック [`009fbf68`](#insn-009fbf68) 範囲 `[['009fbf68', '009fbf77']]`
  - `FALL_THROUGH` [`009fbf74`](#insn-009fbf74) → [`009fbf78`](#insn-009fbf78)
- ブロック [`009fbf78`](#insn-009fbf78) 範囲 `[['009fbf78', '009fbfb3']]`
  - `CONDITIONAL_JUMP` [`009fbfb0`](#insn-009fbfb0) → [`009fbfc0`](#insn-009fbfc0)
  - `FALL_THROUGH` [`009fbfb0`](#insn-009fbfb0) → [`009fbfb4`](#insn-009fbfb4)
- ブロック [`009fbfb4`](#insn-009fbfb4) 範囲 `[['009fbfb4', '009fbfb7']]`
  - `CONDITIONAL_JUMP` [`009fbfb4`](#insn-009fbfb4) → [`009fbfd4`](#insn-009fbfd4)
  - `FALL_THROUGH` [`009fbfb4`](#insn-009fbfb4) → [`009fbfb8`](#insn-009fbfb8)
- ブロック [`009fbfb8`](#insn-009fbfb8) 範囲 `[['009fbfb8', '009fbfbb']]`
  - `FALL_THROUGH` [`009fbfb8`](#insn-009fbfb8) → [`009fbfbc`](#insn-009fbfbc)
- ブロック [`009fbfbc`](#insn-009fbfbc) 範囲 `[['009fbfbc', '009fbfbf']]`
  - `UNCONDITIONAL_JUMP` [`009fbfbc`](#insn-009fbfbc) → [`009fbfc8`](#insn-009fbfc8)
- ブロック [`009fbfc0`](#insn-009fbfc0) 範囲 `[['009fbfc0', '009fbfc7']]`
  - `FALL_THROUGH` [`009fbfc4`](#insn-009fbfc4) → [`009fbfc8`](#insn-009fbfc8)
- ブロック [`009fbfc8`](#insn-009fbfc8) 範囲 `[['009fbfc8', '009fbfd3']]`
  - `FALL_THROUGH` [`009fbfd0`](#insn-009fbfd0) → [`009fbfd4`](#insn-009fbfd4)
- ブロック [`009fbfd4`](#insn-009fbfd4) 範囲 `[['009fbfd4', '009fc003']]`
  - `CONDITIONAL_JUMP` [`009fc000`](#insn-009fc000) → [`009fc010`](#insn-009fc010)
  - `FALL_THROUGH` [`009fc000`](#insn-009fc000) → [`009fc004`](#insn-009fc004)
- ブロック [`009fc004`](#insn-009fc004) 範囲 `[['009fc004', '009fc007']]`
  - `CONDITIONAL_JUMP` [`009fc004`](#insn-009fc004) → [`009fc024`](#insn-009fc024)
  - `FALL_THROUGH` [`009fc004`](#insn-009fc004) → [`009fc008`](#insn-009fc008)
- ブロック [`009fc008`](#insn-009fc008) 範囲 `[['009fc008', '009fc00f']]`
  - `UNCONDITIONAL_JUMP` [`009fc00c`](#insn-009fc00c) → [`009fc018`](#insn-009fc018)
- ブロック [`009fc010`](#insn-009fc010) 範囲 `[['009fc010', '009fc017']]`
  - `FALL_THROUGH` [`009fc014`](#insn-009fc014) → [`009fc018`](#insn-009fc018)
- ブロック [`009fc018`](#insn-009fc018) 範囲 `[['009fc018', '009fc023']]`
  - `FALL_THROUGH` [`009fc020`](#insn-009fc020) → [`009fc024`](#insn-009fc024)
- ブロック [`009fc024`](#insn-009fc024) 範囲 `[['009fc024', '009fc083']]`
  - `FALL_THROUGH` [`009fc080`](#insn-009fc080) → [`009fc084`](#insn-009fc084)
- ブロック [`009fc084`](#insn-009fc084) 範囲 `[['009fc084', '009fc09b']]`
  - `FALL_THROUGH` [`009fc098`](#insn-009fc098) → [`009fc09c`](#insn-009fc09c)
- ブロック [`009fc09c`](#insn-009fc09c) 範囲 `[['009fc09c', '009fc0b7']]`
  - `CONDITIONAL_JUMP` [`009fc0b4`](#insn-009fc0b4) → [`009fc0d0`](#insn-009fc0d0)
  - `FALL_THROUGH` [`009fc0b4`](#insn-009fc0b4) → [`009fc0b8`](#insn-009fc0b8)
- ブロック [`009fc0b8`](#insn-009fc0b8) 範囲 `[['009fc0b8', '009fc0cf']]`
  - `FALL_THROUGH` [`009fc0cc`](#insn-009fc0cc) → [`009fc0d0`](#insn-009fc0d0)
- ブロック [`009fc0d0`](#insn-009fc0d0) 範囲 `[['009fc0d0', '009fc0e3']]`
  - `CONDITIONAL_JUMP` [`009fc0e0`](#insn-009fc0e0) → [`009fc134`](#insn-009fc134)
  - `FALL_THROUGH` [`009fc0e0`](#insn-009fc0e0) → [`009fc0e4`](#insn-009fc0e4)
- ブロック [`009fc0e4`](#insn-009fc0e4) 範囲 `[['009fc0e4', '009fc0f3']]`
  - `CONDITIONAL_JUMP` [`009fc0f0`](#insn-009fc0f0) → [`009fc11c`](#insn-009fc11c)
  - `FALL_THROUGH` [`009fc0f0`](#insn-009fc0f0) → [`009fc0f4`](#insn-009fc0f4)
- ブロック [`009fc0f4`](#insn-009fc0f4) 範囲 `[['009fc0f4', '009fc103']]`
  - `CONDITIONAL_JUMP` [`009fc100`](#insn-009fc100) → [`009fc11c`](#insn-009fc11c)
  - `FALL_THROUGH` [`009fc100`](#insn-009fc100) → [`009fc104`](#insn-009fc104)
- ブロック [`009fc104`](#insn-009fc104) 範囲 `[['009fc104', '009fc11b']]`
  - `FALL_THROUGH` [`009fc118`](#insn-009fc118) → [`009fc11c`](#insn-009fc11c)
- ブロック [`009fc11c`](#insn-009fc11c) 範囲 `[['009fc11c', '009fc133']]`
  - `FALL_THROUGH` [`009fc130`](#insn-009fc130) → [`009fc134`](#insn-009fc134)
- ブロック [`009fc134`](#insn-009fc134) 範囲 `[['009fc134', '009fc18b']]`
  - `CONDITIONAL_JUMP` [`009fc188`](#insn-009fc188) → [`009fc198`](#insn-009fc198)
  - `FALL_THROUGH` [`009fc188`](#insn-009fc188) → [`009fc18c`](#insn-009fc18c)
- ブロック [`009fc18c`](#insn-009fc18c) 範囲 `[['009fc18c', '009fc18f']]`
  - `CONDITIONAL_JUMP` [`009fc18c`](#insn-009fc18c) → [`009fc1ac`](#insn-009fc1ac)
  - `FALL_THROUGH` [`009fc18c`](#insn-009fc18c) → [`009fc190`](#insn-009fc190)
- ブロック [`009fc190`](#insn-009fc190) 範囲 `[['009fc190', '009fc197']]`
  - `UNCONDITIONAL_JUMP` [`009fc194`](#insn-009fc194) → [`009fc1a0`](#insn-009fc1a0)
- ブロック [`009fc198`](#insn-009fc198) 範囲 `[['009fc198', '009fc19f']]`
  - `FALL_THROUGH` [`009fc19c`](#insn-009fc19c) → [`009fc1a0`](#insn-009fc1a0)
- ブロック [`009fc1a0`](#insn-009fc1a0) 範囲 `[['009fc1a0', '009fc1ab']]`
  - `FALL_THROUGH` [`009fc1a8`](#insn-009fc1a8) → [`009fc1ac`](#insn-009fc1ac)
- ブロック [`009fc1ac`](#insn-009fc1ac) 範囲 `[['009fc1ac', '009fc1b7']]`
  - `CONDITIONAL_JUMP` [`009fc1b4`](#insn-009fc1b4) → [`009fc1d0`](#insn-009fc1d0)
  - `FALL_THROUGH` [`009fc1b4`](#insn-009fc1b4) → [`009fc1b8`](#insn-009fc1b8)
- ブロック [`009fc1b8`](#insn-009fc1b8) 範囲 `[['009fc1b8', '009fc1cf']]`
  - `FALL_THROUGH` [`009fc1cc`](#insn-009fc1cc) → [`009fc1d0`](#insn-009fc1d0)
- ブロック [`009fc1d0`](#insn-009fc1d0) 範囲 `[['009fc1d0', '009fc1db']]`
  - `CONDITIONAL_JUMP` [`009fc1d8`](#insn-009fc1d8) → [`009fc22c`](#insn-009fc22c)
  - `FALL_THROUGH` [`009fc1d8`](#insn-009fc1d8) → [`009fc1dc`](#insn-009fc1dc)
- ブロック [`009fc1dc`](#insn-009fc1dc) 範囲 `[['009fc1dc', '009fc1eb']]`
  - `CONDITIONAL_JUMP` [`009fc1e8`](#insn-009fc1e8) → [`009fc214`](#insn-009fc214)
  - `FALL_THROUGH` [`009fc1e8`](#insn-009fc1e8) → [`009fc1ec`](#insn-009fc1ec)
- ブロック [`009fc1ec`](#insn-009fc1ec) 範囲 `[['009fc1ec', '009fc1fb']]`
  - `CONDITIONAL_JUMP` [`009fc1f8`](#insn-009fc1f8) → [`009fc214`](#insn-009fc214)
  - `FALL_THROUGH` [`009fc1f8`](#insn-009fc1f8) → [`009fc1fc`](#insn-009fc1fc)
- ブロック [`009fc1fc`](#insn-009fc1fc) 範囲 `[['009fc1fc', '009fc213']]`
  - `FALL_THROUGH` [`009fc210`](#insn-009fc210) → [`009fc214`](#insn-009fc214)
- ブロック [`009fc214`](#insn-009fc214) 範囲 `[['009fc214', '009fc22b']]`
  - `FALL_THROUGH` [`009fc228`](#insn-009fc228) → [`009fc22c`](#insn-009fc22c)
- ブロック [`009fc22c`](#insn-009fc22c) 範囲 `[['009fc22c', '009fc23b']]`
  - `CONDITIONAL_JUMP` [`009fc238`](#insn-009fc238) → [`009fc448`](#insn-009fc448)
  - `FALL_THROUGH` [`009fc238`](#insn-009fc238) → [`009fc23c`](#insn-009fc23c)
- ブロック [`009fc23c`](#insn-009fc23c) 範囲 `[['009fc23c', '009fc25f']]`
- ブロック [`009fc260`](#insn-009fc260) 範囲 `[['009fc260', '009fc27f']]`
  - `CONDITIONAL_JUMP` [`009fc27c`](#insn-009fc27c) → [`009fbd6c`](#insn-009fbd6c)
  - `FALL_THROUGH` [`009fc27c`](#insn-009fc27c) → [`009fc280`](#insn-009fc280)
- ブロック [`009fc280`](#insn-009fc280) 範囲 `[['009fc280', '009fc283']]`
  - `UNCONDITIONAL_JUMP` [`009fc280`](#insn-009fc280) → [`009fbd7c`](#insn-009fbd7c)
- ブロック [`009fc284`](#insn-009fc284) 範囲 `[['009fc284', '009fc2a3']]`
  - `CONDITIONAL_JUMP` [`009fc2a0`](#insn-009fc2a0) → [`009fbd84`](#insn-009fbd84)
  - `FALL_THROUGH` [`009fc2a0`](#insn-009fc2a0) → [`009fc2a4`](#insn-009fc2a4)
- ブロック [`009fc2a4`](#insn-009fc2a4) 範囲 `[['009fc2a4', '009fc2a7']]`
  - `UNCONDITIONAL_JUMP` [`009fc2a4`](#insn-009fc2a4) → [`009fbd8c`](#insn-009fbd8c)
- ブロック [`009fc2a8`](#insn-009fc2a8) 範囲 `[['009fc2a8', '009fc2b7']]`
  - `CONDITIONAL_JUMP` [`009fc2b4`](#insn-009fc2b4) → [`009fbcdc`](#insn-009fbcdc)
  - `FALL_THROUGH` [`009fc2b4`](#insn-009fc2b4) → [`009fc2b8`](#insn-009fc2b8)
- ブロック [`009fc2b8`](#insn-009fc2b8) 範囲 `[['009fc2b8', '009fc2cb']]`
  - `FALL_THROUGH` [`009fc2c8`](#insn-009fc2c8) → [`009fc2cc`](#insn-009fc2cc)
- ブロック [`009fc2cc`](#insn-009fc2cc) 範囲 `[['009fc2cc', '009fc2e3']]`
  - `FALL_THROUGH` [`009fc2e0`](#insn-009fc2e0) → [`009fc2e4`](#insn-009fc2e4)
- ブロック [`009fc2e4`](#insn-009fc2e4) 範囲 `[['009fc2e4', '009fc2ff']]`
  - `UNCONDITIONAL_JUMP` [`009fc2fc`](#insn-009fc2fc) → [`009fbcdc`](#insn-009fbcdc)
- ブロック [`009fc448`](#insn-009fc448) 範囲 `[['009fc448', '009fc44b']]`

## 命令位置別の参照

- [`009fbbd0`](#insn-009fbbd0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbbd4`](#insn-009fbbd4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbbd8`](#insn-009fbbd8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbbdc`](#insn-009fbbdc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbbe0`](#insn-009fbbe0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbbe4`](#insn-009fbbe4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbbe8`](#insn-009fbbe8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbbfc`](#insn-009fbbfc) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbc04`](#insn-009fbc04) → `00ca5a38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009fbc08`](#insn-009fbc08) → [`009fbc30`](#insn-009fbc30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbc10`](#insn-009fbc10) → `00c66ef8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`009fbc18`](#insn-009fbc18) → `00c72a30`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`009fbc24`](#insn-009fbc24) → [`00c596b0`](../00c59/00c596b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c596b0` · 推定シンボル `None` · 推定型 `None`
- [`009fbc2c`](#insn-009fbc2c) → [`009fbc34`](#insn-009fbc34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbc34`](#insn-009fbc34) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`009fbc44`](#insn-009fbc44) → [`00a842c4`](../00a84/00a842c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a842c4` · 推定シンボル `None` · 推定型 `None`
- [`009fbc48`](#insn-009fbc48) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`009fbc54`](#insn-009fbc54) → [`00a842c4`](../00a84/00a842c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a842c4` · 推定シンボル `None` · 推定型 `None`
- [`009fbc58`](#insn-009fbc58) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`009fbc64`](#insn-009fbc64) → [`009fa2c8`](../009fa/009fa2c8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009fa2c8` · 推定シンボル `None` · 推定型 `None`
- [`009fbc7c`](#insn-009fbc7c) → [`00a844b0`](../00a84/00a844b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a844b0` · 推定シンボル `None` · 推定型 `None`
- [`009fbc80`](#insn-009fbc80) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbc84`](#insn-009fbc84) → [`009fbc90`](#insn-009fbc90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbc88`](#insn-009fbc88) → `Stack[-0x148]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbc8c`](#insn-009fbc8c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`009fbc90`](#insn-009fbc90) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`009fbca0`](#insn-009fbca0) → [`009fa81c`](../009fa/009fa81c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009fa81c` · 推定シンボル `None` · 推定型 `None`
- [`009fbcb8`](#insn-009fbcb8) → [`00a844b0`](../00a84/00a844b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a844b0` · 推定シンボル `None` · 推定型 `None`
- [`009fbcbc`](#insn-009fbcbc) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbcc0`](#insn-009fbcc0) → [`009fbccc`](#insn-009fbccc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbcc4`](#insn-009fbcc4) → `Stack[-0x148]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbcc8`](#insn-009fbcc8) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`009fbcd4`](#insn-009fbcd4) → `00ca5ff8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`009fbcd8`](#insn-009fbcd8) → [`009fc2a8`](#insn-009fc2a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbce4`](#insn-009fbce4) → `Stack[-0x14d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbce8`](#insn-009fbce8) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbcf4`](#insn-009fbcf4) → `002b3fb8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`009fbcf8`](#insn-009fbcf8) → `Stack[-0x14f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbd00`](#insn-009fbd00) → `Stack[-0x188]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbd04`](#insn-009fbd04) → `Stack[-0x157]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbd10`](#insn-009fbd10) → `002b92eb`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbd14`](#insn-009fbd14) → `002b92f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`009fbd18`](#insn-009fbd18) → `Stack[-0x17a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbd1c`](#insn-009fbd1c) → `Stack[-0x187]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbd20`](#insn-009fbd20) → `Stack[-0x182]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbd28`](#insn-009fbd28) → `00ca5fc0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009fbd3c`](#insn-009fbd3c) → [`0047e96c`](../0047e/0047e96c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047e96c` · 推定シンボル `None` · 推定型 `None`
- [`009fbd40`](#insn-009fbd40) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbd48`](#insn-009fbd48) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbd50`](#insn-009fbd50) → [`009fbd64`](#insn-009fbd64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbd5c`](#insn-009fbd5c) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`009fbd60`](#insn-009fbd60) → [`009fc260`](#insn-009fc260) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbd64`](#insn-009fbd64) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbd68`](#insn-009fbd68) → [`009fbd7c`](#insn-009fbd7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbd74`](#insn-009fbd74) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`009fbd78`](#insn-009fbd78) → [`009fc284`](#insn-009fc284) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbd7c`](#insn-009fbd7c) → `Stack[-0x188]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbd80`](#insn-009fbd80) → [`009fbd8c`](#insn-009fbd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbd84`](#insn-009fbd84) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbd88`](#insn-009fbd88) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`009fbd8c`](#insn-009fbd8c) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbd90`](#insn-009fbd90) → [`009fbd9c`](#insn-009fbd9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbd94`](#insn-009fbd94) → `Stack[-0x148]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbd98`](#insn-009fbd98) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`009fbd9c`](#insn-009fbd9c) → [`009f8478`](../009f8/009f8478.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009f8478` · 推定シンボル `None` · 推定型 `None`
- [`009fbda0`](#insn-009fbda0) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`009fbdb0`](#insn-009fbdb0) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbdb4`](#insn-009fbdb4) → `00c8bc40`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fbdb4`](#insn-009fbdb4) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbdbc`](#insn-009fbdbc) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbdd8`](#insn-009fbdd8) → [`008bb86c`](../008bb/008bb86c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008bb86c` · 推定シンボル `None` · 推定型 `None`
- [`009fbdf4`](#insn-009fbdf4) → [`0046de54`](../0046d/0046de54.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046de54` · 推定シンボル `None` · 推定型 `None`
- [`009fbdf8`](#insn-009fbdf8) → `Stack[-0x198]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbe00`](#insn-009fbe00) → [`008ba504`](../008ba/008ba504.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008ba504` · 推定シンボル `None` · 推定型 `None`
- [`009fbe08`](#insn-009fbe08) → [`008ba85c`](../008ba/008ba85c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008ba85c` · 推定シンボル `None` · 推定型 `None`
- [`009fbe10`](#insn-009fbe10) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbe1c`](#insn-009fbe1c) → [`009fbe2c`](#insn-009fbe2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbe20`](#insn-009fbe20) → [`009fbe40`](#insn-009fbe40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbe28`](#insn-009fbe28) → [`009fbe34`](#insn-009fbe34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbe34`](#insn-009fbe34) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbe38`](#insn-009fbe38) → `00c8bc60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`009fbe38`](#insn-009fbe38) → `00c8bc68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fbe3c`](#insn-009fbe3c) → [`00a023a8`](../00a02/00a023a8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00a023a8` · 推定シンボル `None` · 推定型 `None`
- [`009fbe3c`](#insn-009fbe3c) → [`00a023ac`](../00a02/00a023ac.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00a023ac` · 推定シンボル `None` · 推定型 `None`
- [`009fbe40`](#insn-009fbe40) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbe44`](#insn-009fbe44) → [`009fbe50`](#insn-009fbe50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbe48`](#insn-009fbe48) → `Stack[-0x148]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbe4c`](#insn-009fbe4c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`009fbe50`](#insn-009fbe50) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`009fbe60`](#insn-009fbe60) → [`00a83a34`](../00a83/00a83a34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a83a34` · 推定シンボル `None` · 推定型 `None`
- [`009fbe9c`](#insn-009fbe9c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`009fbea8`](#insn-009fbea8) → [`00a83a34`](../00a83/00a83a34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a83a34` · 推定シンボル `None` · 推定型 `None`
- [`009fbec8`](#insn-009fbec8) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`009fbed8`](#insn-009fbed8) → [`009e3f94`](../009e3/009e3f94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009e3f94` · 推定シンボル `None` · 推定型 `None`
- [`009fbefc`](#insn-009fbefc) → [`008ba29c`](../008ba/008ba29c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008ba29c` · 推定シンボル `None` · 推定型 `None`
- [`009fbf14`](#insn-009fbf14) → [`009fbf68`](#insn-009fbf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbf1c`](#insn-009fbf1c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`009fbf4c`](#insn-009fbf4c) → [`00ac9e74`](../00ac9/00ac9e74.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac9e74` · 推定シンボル `None` · 推定型 `None`
- [`009fbf54`](#insn-009fbf54) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`009fbf60`](#insn-009fbf60) → `00337f64`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009fbf64`](#insn-009fbf64) → [`009fbf78`](#insn-009fbf78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbf68`](#insn-009fbf68) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`009fbf74`](#insn-009fbf74) → [`00ac9eb8`](../00ac9/00ac9eb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac9eb8` · 推定シンボル `None` · 推定型 `None`
- [`009fbf7c`](#insn-009fbf7c) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`009fbf8c`](#insn-009fbf8c) → `00c8bcc0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fbf94`](#insn-009fbf94) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbfa4`](#insn-009fbfa4) → [`008ba5d0`](../008ba/008ba5d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008ba5d0` · 推定シンボル `None` · 推定型 `None`
- [`009fbfa8`](#insn-009fbfa8) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbfb0`](#insn-009fbfb0) → [`009fbfc0`](#insn-009fbfc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbfb4`](#insn-009fbfb4) → [`009fbfd4`](#insn-009fbfd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbfbc`](#insn-009fbfbc) → [`009fbfc8`](#insn-009fbfc8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbfc8`](#insn-009fbfc8) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbfcc`](#insn-009fbfcc) → `00c8bce8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fbfd0`](#insn-009fbfd0) → [`00a024ec`](../00a02/00a024ec.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00a024ec` · 推定シンボル `None` · 推定型 `None`
- [`009fbfe0`](#insn-009fbfe0) → `00c8bd40`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fbfe0`](#insn-009fbfe0) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbfe4`](#insn-009fbfe4) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbfe8`](#insn-009fbfe8) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fbff4`](#insn-009fbff4) → [`008ba6a8`](../008ba/008ba6a8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008ba6a8` · 推定シンボル `None` · 推定型 `None`
- [`009fbff8`](#insn-009fbff8) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc000`](#insn-009fc000) → [`009fc010`](#insn-009fc010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc004`](#insn-009fc004) → [`009fc024`](#insn-009fc024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc00c`](#insn-009fc00c) → [`009fc018`](#insn-009fc018) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc018`](#insn-009fc018) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc01c`](#insn-009fc01c) → `00c8bd60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`009fc01c`](#insn-009fc01c) → `00c8bd68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fc020`](#insn-009fc020) → [`00a032d0`](../00a03/00a032d0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00a032d0` · 推定シンボル `None` · 推定型 `None`
- [`009fc020`](#insn-009fc020) → [`00a032d4`](../00a03/00a032d4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00a032d4` · 推定シンボル `None` · 推定型 `None`
- [`009fc048`](#insn-009fc048) → [`00a48594`](../00a48/00a48594.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a48594` · 推定シンボル `None` · 推定型 `None`
- [`009fc04c`](#insn-009fc04c) → `2e393230676d0000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc04c`](#insn-009fc04c) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc050`](#insn-009fc050) → `2e393230676d0000`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc060`](#insn-009fc060) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc078`](#insn-009fc078) → [`00a47944`](../00a47/00a47944.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a47944` · 推定シンボル `None` · 推定型 `None`
- [`009fc07c`](#insn-009fc07c) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc080`](#insn-009fc080) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc084`](#insn-009fc084) → `Stack[-0x188]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc08c`](#insn-009fc08c) → `2e393230676d0000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc090`](#insn-009fc090) → [`00a477cc`](../00a47/00a477cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a477cc` · 推定シンボル `None` · 推定型 `None`
- [`009fc0a8`](#insn-009fc0a8) → `Stack[-0x188]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc0ac`](#insn-009fc0ac) → `00c9c408`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`009fc0b0`](#insn-009fc0b0) → `Stack[-0x188]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc0b4`](#insn-009fc0b4) → [`009fc0d0`](#insn-009fc0d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc0c0`](#insn-009fc0c0) → `00c8c7f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fc0c4`](#insn-009fc0c4) → [`005d8fb8`](../005d8/005d8fb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d8fb8` · 推定シンボル `None` · 推定型 `None`
- [`009fc0cc`](#insn-009fc0cc) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`009fc0d4`](#insn-009fc0d4) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc0d8`](#insn-009fc0d8) → `00c9c410`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`009fc0dc`](#insn-009fc0dc) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc0e0`](#insn-009fc0e0) → [`009fc134`](#insn-009fc134) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc0ec`](#insn-009fc0ec) → `00c8c850`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fc0f0`](#insn-009fc0f0) → [`009fc11c`](#insn-009fc11c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc0fc`](#insn-009fc0fc) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`009fc100`](#insn-009fc100) → [`009fc11c`](#insn-009fc11c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc118`](#insn-009fc118) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`009fc124`](#insn-009fc124) → `00c8c7f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fc128`](#insn-009fc128) → [`005d8fb8`](../005d8/005d8fb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d8fb8` · 推定シンボル `None` · 推定型 `None`
- [`009fc130`](#insn-009fc130) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`009fc134`](#insn-009fc134) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`009fc138`](#insn-009fc138) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc140`](#insn-009fc140) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc144`](#insn-009fc144) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc148`](#insn-009fc148) → `2e393230676d0000`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc148`](#insn-009fc148) → `Stack[-0x188]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc154`](#insn-009fc154) → `00c8bdc0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fc154`](#insn-009fc154) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc17c`](#insn-009fc17c) → [`008b7ff0`](../008b7/008b7ff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7ff0` · 推定シンボル `None` · 推定型 `None`
- [`009fc180`](#insn-009fc180) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc188`](#insn-009fc188) → [`009fc198`](#insn-009fc198) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc18c`](#insn-009fc18c) → [`009fc1ac`](#insn-009fc1ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc194`](#insn-009fc194) → [`009fc1a0`](#insn-009fc1a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc1a0`](#insn-009fc1a0) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc1a4`](#insn-009fc1a4) → `00c8bde0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`009fc1a4`](#insn-009fc1a4) → `00c8bde8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fc1a8`](#insn-009fc1a8) → [`00a036fc`](../00a03/00a036fc.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00a036fc` · 推定シンボル `None` · 推定型 `None`
- [`009fc1a8`](#insn-009fc1a8) → [`00a03700`](../00a03/00a03700.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00a03700` · 推定シンボル `None` · 推定型 `None`
- [`009fc1ac`](#insn-009fc1ac) → `Stack[-0x188]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc1b0`](#insn-009fc1b0) → `Stack[-0x188]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc1b4`](#insn-009fc1b4) → [`009fc1d0`](#insn-009fc1d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc1c0`](#insn-009fc1c0) → `2e393230676d0000`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc1c0`](#insn-009fc1c0) → `00c8c7f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fc1c4`](#insn-009fc1c4) → [`005d8fb8`](../005d8/005d8fb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d8fb8` · 推定シンボル `None` · 推定型 `None`
- [`009fc1c8`](#insn-009fc1c8) → `2e393230676d0000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc1cc`](#insn-009fc1cc) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`009fc1d0`](#insn-009fc1d0) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc1d4`](#insn-009fc1d4) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc1d8`](#insn-009fc1d8) → [`009fc22c`](#insn-009fc22c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc1e4`](#insn-009fc1e4) → `00c8c850`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fc1e8`](#insn-009fc1e8) → [`009fc214`](#insn-009fc214) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc1f4`](#insn-009fc1f4) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`009fc1f8`](#insn-009fc1f8) → [`009fc214`](#insn-009fc214) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc210`](#insn-009fc210) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`009fc21c`](#insn-009fc21c) → `00c8c7f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fc220`](#insn-009fc220) → [`005d8fb8`](../005d8/005d8fb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d8fb8` · 推定シンボル `None` · 推定型 `None`
- [`009fc228`](#insn-009fc228) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`009fc230`](#insn-009fc230) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc238`](#insn-009fc238) → [`009fc448`](#insn-009fc448) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc23c`](#insn-009fc23c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc240`](#insn-009fc240) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc244`](#insn-009fc244) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc248`](#insn-009fc248) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc24c`](#insn-009fc24c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc250`](#insn-009fc250) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc254`](#insn-009fc254) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc274`](#insn-009fc274) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`009fc278`](#insn-009fc278) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc27c`](#insn-009fc27c) → [`009fbd6c`](#insn-009fbd6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc280`](#insn-009fc280) → [`009fbd7c`](#insn-009fbd7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc298`](#insn-009fc298) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`009fc29c`](#insn-009fc29c) → `Stack[-0x188]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc2a0`](#insn-009fc2a0) → [`009fbd84`](#insn-009fbd84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc2a4`](#insn-009fc2a4) → [`009fbd8c`](#insn-009fbd8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc2ac`](#insn-009fc2ac) → `00ca5ff8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`009fc2b0`](#insn-009fc2b0) → [`00c58ef0`](../00c58/00c58ef0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58ef0` · 推定シンボル `None` · 推定型 `None`
- [`009fc2b4`](#insn-009fc2b4) → [`009fbcdc`](#insn-009fbcdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc2bc`](#insn-009fc2bc) → `00ca5fc0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009fc2c4`](#insn-009fc2c4) → [`0047f114`](../0047f/0047f114.md) · `PARAM` · `ANALYSIS` · 関数 `0047f114` · 推定シンボル `None` · 推定型 `None`
- [`009fc2d0`](#insn-009fc2d0) → `00c64030`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`009fc2d4`](#insn-009fc2d4) → `00ca5fc8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009fc2d8`](#insn-009fc2d8) → `00ca5fc0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009fc2d8`](#insn-009fc2d8) → `00ca5fc8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009fc2e0`](#insn-009fc2e0) → `00ca5fe8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009fc2e0`](#insn-009fc2e0) → `00ca5ff0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009fc2e4`](#insn-009fc2e4) → `00ca5fe0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009fc2e8`](#insn-009fc2e8) → `00ca5fd0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009fc2e8`](#insn-009fc2e8) → `00ca5fd8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009fc2e8`](#insn-009fc2e8) → `00ca5fe0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009fc2ec`](#insn-009fc2ec) → [`00c58ed0`](../00c58/00c58ed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58ed0` · 推定シンボル `None` · 推定型 `None`
- [`009fc2f4`](#insn-009fc2f4) → `00ca5ff8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`009fc2f8`](#insn-009fc2f8) → [`00c58f10`](../00c58/00c58f10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f10` · 推定シンボル `None` · 推定型 `None`
- [`009fc2fc`](#insn-009fc2fc) → [`009fbcdc`](#insn-009fbcdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fc448`](#insn-009fc448) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009fbbd0`](#insn-009fbbd0)

~~~json
{
  "source": "009fbbd0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbbd4`](#insn-009fbbd4)

~~~json
{
  "source": "009fbbd4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbbd8`](#insn-009fbbd8)

~~~json
{
  "source": "009fbbd8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbbdc`](#insn-009fbbdc)

~~~json
{
  "source": "009fbbdc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbbe0`](#insn-009fbbe0)

~~~json
{
  "source": "009fbbe0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbbe4`](#insn-009fbbe4)

~~~json
{
  "source": "009fbbe4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbbe8`](#insn-009fbbe8)

~~~json
{
  "source": "009fbbe8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbbfc`](#insn-009fbbfc)

~~~json
{
  "source": "009fbbfc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbc04`](#insn-009fbc04)

~~~json
{
  "source": "009fbc04",
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
- 参照命令 [`009fbc08`](#insn-009fbc08)

~~~json
{
  "source": "009fbc08",
  "target": "009fbc30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbc10`](#insn-009fbc10)

~~~json
{
  "source": "009fbc10",
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
- 参照命令 [`009fbc18`](#insn-009fbc18)

~~~json
{
  "source": "009fbc18",
  "target": "00c72a30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c72a30",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fbc24`](#insn-009fbc24)

~~~json
{
  "source": "009fbc24",
  "target": "00c596b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbc2c`](#insn-009fbc2c)

~~~json
{
  "source": "009fbc2c",
  "target": "009fbc34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbc34`](#insn-009fbc34)

~~~json
{
  "source": "009fbc34",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbc44`](#insn-009fbc44)

~~~json
{
  "source": "009fbc44",
  "target": "00a842c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbc48`](#insn-009fbc48)

~~~json
{
  "source": "009fbc48",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbc54`](#insn-009fbc54)

~~~json
{
  "source": "009fbc54",
  "target": "00a842c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbc58`](#insn-009fbc58)

~~~json
{
  "source": "009fbc58",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbc64`](#insn-009fbc64)

~~~json
{
  "source": "009fbc64",
  "target": "009fa2c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbc7c`](#insn-009fbc7c)

~~~json
{
  "source": "009fbc7c",
  "target": "00a844b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbc80`](#insn-009fbc80)

~~~json
{
  "source": "009fbc80",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbc84`](#insn-009fbc84)

~~~json
{
  "source": "009fbc84",
  "target": "009fbc90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbc88`](#insn-009fbc88)

~~~json
{
  "source": "009fbc88",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbc8c`](#insn-009fbc8c)

~~~json
{
  "source": "009fbc8c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbc90`](#insn-009fbc90)

~~~json
{
  "source": "009fbc90",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbca0`](#insn-009fbca0)

~~~json
{
  "source": "009fbca0",
  "target": "009fa81c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbcb8`](#insn-009fbcb8)

~~~json
{
  "source": "009fbcb8",
  "target": "00a844b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbcbc`](#insn-009fbcbc)

~~~json
{
  "source": "009fbcbc",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbcc0`](#insn-009fbcc0)

~~~json
{
  "source": "009fbcc0",
  "target": "009fbccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbcc4`](#insn-009fbcc4)

~~~json
{
  "source": "009fbcc4",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbcc8`](#insn-009fbcc8)

~~~json
{
  "source": "009fbcc8",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbcd4`](#insn-009fbcd4)

~~~json
{
  "source": "009fbcd4",
  "target": "00ca5ff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5ff8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fbcd8`](#insn-009fbcd8)

~~~json
{
  "source": "009fbcd8",
  "target": "009fc2a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbce4`](#insn-009fbce4)

~~~json
{
  "source": "009fbce4",
  "target": "Stack[-0x14d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbce8`](#insn-009fbce8)

~~~json
{
  "source": "009fbce8",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbcf4`](#insn-009fbcf4)

~~~json
{
  "source": "009fbcf4",
  "target": "002b3fb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b3fb8",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "696d673032392e706e6700",
  "capture_start": "002b3fb8",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009fbcf8`](#insn-009fbcf8)

~~~json
{
  "source": "009fbcf8",
  "target": "Stack[-0x14f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbd00`](#insn-009fbd00)

~~~json
{
  "source": "009fbd00",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbd04`](#insn-009fbd04)

~~~json
{
  "source": "009fbd04",
  "target": "Stack[-0x157]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbd10`](#insn-009fbd10)

~~~json
{
  "source": "009fbd10",
  "target": "002b92eb",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbd14`](#insn-009fbd14)

~~~json
{
  "source": "009fbd14",
  "target": "002b92f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b92f0",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "392e696d6763757400",
  "capture_start": "002b92f0",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009fbd18`](#insn-009fbd18)

~~~json
{
  "source": "009fbd18",
  "target": "Stack[-0x17a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbd1c`](#insn-009fbd1c)

~~~json
{
  "source": "009fbd1c",
  "target": "Stack[-0x187]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbd20`](#insn-009fbd20)

~~~json
{
  "source": "009fbd20",
  "target": "Stack[-0x182]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbd28`](#insn-009fbd28)

~~~json
{
  "source": "009fbd28",
  "target": "00ca5fc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5fc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fbd3c`](#insn-009fbd3c)

~~~json
{
  "source": "009fbd3c",
  "target": "0047e96c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbd40`](#insn-009fbd40)

~~~json
{
  "source": "009fbd40",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbd48`](#insn-009fbd48)

~~~json
{
  "source": "009fbd48",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbd50`](#insn-009fbd50)

~~~json
{
  "source": "009fbd50",
  "target": "009fbd64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbd5c`](#insn-009fbd5c)

~~~json
{
  "source": "009fbd5c",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbd60`](#insn-009fbd60)

~~~json
{
  "source": "009fbd60",
  "target": "009fc260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbd64`](#insn-009fbd64)

~~~json
{
  "source": "009fbd64",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbd68`](#insn-009fbd68)

~~~json
{
  "source": "009fbd68",
  "target": "009fbd7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbd74`](#insn-009fbd74)

~~~json
{
  "source": "009fbd74",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbd78`](#insn-009fbd78)

~~~json
{
  "source": "009fbd78",
  "target": "009fc284",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbd7c`](#insn-009fbd7c)

~~~json
{
  "source": "009fbd7c",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbd80`](#insn-009fbd80)

~~~json
{
  "source": "009fbd80",
  "target": "009fbd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbd84`](#insn-009fbd84)

~~~json
{
  "source": "009fbd84",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbd88`](#insn-009fbd88)

~~~json
{
  "source": "009fbd88",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbd8c`](#insn-009fbd8c)

~~~json
{
  "source": "009fbd8c",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbd90`](#insn-009fbd90)

~~~json
{
  "source": "009fbd90",
  "target": "009fbd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbd94`](#insn-009fbd94)

~~~json
{
  "source": "009fbd94",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbd98`](#insn-009fbd98)

~~~json
{
  "source": "009fbd98",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbd9c`](#insn-009fbd9c)

~~~json
{
  "source": "009fbd9c",
  "target": "009f8478",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbda0`](#insn-009fbda0)

~~~json
{
  "source": "009fbda0",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbdb0`](#insn-009fbdb0)

~~~json
{
  "source": "009fbdb0",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbdb4`](#insn-009fbdb4)

~~~json
{
  "source": "009fbdb4",
  "target": "00c8bc40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8bc40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fbdb4`](#insn-009fbdb4)

~~~json
{
  "source": "009fbdb4",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbdbc`](#insn-009fbdbc)

~~~json
{
  "source": "009fbdbc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbdd8`](#insn-009fbdd8)

~~~json
{
  "source": "009fbdd8",
  "target": "008bb86c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbdf4`](#insn-009fbdf4)

~~~json
{
  "source": "009fbdf4",
  "target": "0046de54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbdf8`](#insn-009fbdf8)

~~~json
{
  "source": "009fbdf8",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbe00`](#insn-009fbe00)

~~~json
{
  "source": "009fbe00",
  "target": "008ba504",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbe08`](#insn-009fbe08)

~~~json
{
  "source": "009fbe08",
  "target": "008ba85c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbe10`](#insn-009fbe10)

~~~json
{
  "source": "009fbe10",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbe1c`](#insn-009fbe1c)

~~~json
{
  "source": "009fbe1c",
  "target": "009fbe2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbe20`](#insn-009fbe20)

~~~json
{
  "source": "009fbe20",
  "target": "009fbe40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbe28`](#insn-009fbe28)

~~~json
{
  "source": "009fbe28",
  "target": "009fbe34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbe34`](#insn-009fbe34)

~~~json
{
  "source": "009fbe34",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbe38`](#insn-009fbe38)

~~~json
{
  "source": "009fbe38",
  "target": "00c8bc60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8bc60",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fbe38`](#insn-009fbe38)

~~~json
{
  "source": "009fbe38",
  "target": "00c8bc68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8bc68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fbe3c`](#insn-009fbe3c)

~~~json
{
  "source": "009fbe3c",
  "target": "00a023a8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbe3c`](#insn-009fbe3c)

~~~json
{
  "source": "009fbe3c",
  "target": "00a023ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbe40`](#insn-009fbe40)

~~~json
{
  "source": "009fbe40",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbe44`](#insn-009fbe44)

~~~json
{
  "source": "009fbe44",
  "target": "009fbe50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbe48`](#insn-009fbe48)

~~~json
{
  "source": "009fbe48",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbe4c`](#insn-009fbe4c)

~~~json
{
  "source": "009fbe4c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbe50`](#insn-009fbe50)

~~~json
{
  "source": "009fbe50",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbe60`](#insn-009fbe60)

~~~json
{
  "source": "009fbe60",
  "target": "00a83a34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbe9c`](#insn-009fbe9c)

~~~json
{
  "source": "009fbe9c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbea8`](#insn-009fbea8)

~~~json
{
  "source": "009fbea8",
  "target": "00a83a34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbec8`](#insn-009fbec8)

~~~json
{
  "source": "009fbec8",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbed8`](#insn-009fbed8)

~~~json
{
  "source": "009fbed8",
  "target": "009e3f94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbefc`](#insn-009fbefc)

~~~json
{
  "source": "009fbefc",
  "target": "008ba29c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbf14`](#insn-009fbf14)

~~~json
{
  "source": "009fbf14",
  "target": "009fbf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbf1c`](#insn-009fbf1c)

~~~json
{
  "source": "009fbf1c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbf4c`](#insn-009fbf4c)

~~~json
{
  "source": "009fbf4c",
  "target": "00ac9e74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbf54`](#insn-009fbf54)

~~~json
{
  "source": "009fbf54",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbf60`](#insn-009fbf60)

~~~json
{
  "source": "009fbf60",
  "target": "00337f64",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00337f60",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "94ba7d00e46a0a00",
  "capture_start": "00337f60",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009fbf64`](#insn-009fbf64)

~~~json
{
  "source": "009fbf64",
  "target": "009fbf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbf68`](#insn-009fbf68)

~~~json
{
  "source": "009fbf68",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbf74`](#insn-009fbf74)

~~~json
{
  "source": "009fbf74",
  "target": "00ac9eb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbf7c`](#insn-009fbf7c)

~~~json
{
  "source": "009fbf7c",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbf8c`](#insn-009fbf8c)

~~~json
{
  "source": "009fbf8c",
  "target": "00c8bcc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8bcc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fbf94`](#insn-009fbf94)

~~~json
{
  "source": "009fbf94",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbfa4`](#insn-009fbfa4)

~~~json
{
  "source": "009fbfa4",
  "target": "008ba5d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbfa8`](#insn-009fbfa8)

~~~json
{
  "source": "009fbfa8",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbfb0`](#insn-009fbfb0)

~~~json
{
  "source": "009fbfb0",
  "target": "009fbfc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbfb4`](#insn-009fbfb4)

~~~json
{
  "source": "009fbfb4",
  "target": "009fbfd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbfbc`](#insn-009fbfbc)

~~~json
{
  "source": "009fbfbc",
  "target": "009fbfc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbfc8`](#insn-009fbfc8)

~~~json
{
  "source": "009fbfc8",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbfcc`](#insn-009fbfcc)

~~~json
{
  "source": "009fbfcc",
  "target": "00c8bce8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8bce8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fbfd0`](#insn-009fbfd0)

~~~json
{
  "source": "009fbfd0",
  "target": "00a024ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbfe0`](#insn-009fbfe0)

~~~json
{
  "source": "009fbfe0",
  "target": "00c8bd40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8bd40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fbfe0`](#insn-009fbfe0)

~~~json
{
  "source": "009fbfe0",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbfe4`](#insn-009fbfe4)

~~~json
{
  "source": "009fbfe4",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbfe8`](#insn-009fbfe8)

~~~json
{
  "source": "009fbfe8",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fbff4`](#insn-009fbff4)

~~~json
{
  "source": "009fbff4",
  "target": "008ba6a8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fbff8`](#insn-009fbff8)

~~~json
{
  "source": "009fbff8",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc000`](#insn-009fc000)

~~~json
{
  "source": "009fc000",
  "target": "009fc010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc004`](#insn-009fc004)

~~~json
{
  "source": "009fc004",
  "target": "009fc024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc00c`](#insn-009fc00c)

~~~json
{
  "source": "009fc00c",
  "target": "009fc018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc018`](#insn-009fc018)

~~~json
{
  "source": "009fc018",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc01c`](#insn-009fc01c)

~~~json
{
  "source": "009fc01c",
  "target": "00c8bd60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8bd60",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fc01c`](#insn-009fc01c)

~~~json
{
  "source": "009fc01c",
  "target": "00c8bd68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8bd68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fc020`](#insn-009fc020)

~~~json
{
  "source": "009fc020",
  "target": "00a032d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc020`](#insn-009fc020)

~~~json
{
  "source": "009fc020",
  "target": "00a032d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc048`](#insn-009fc048)

~~~json
{
  "source": "009fc048",
  "target": "00a48594",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc04c`](#insn-009fc04c)

~~~json
{
  "source": "009fc04c",
  "target": "2e393230676d0000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc04c`](#insn-009fc04c)

~~~json
{
  "source": "009fc04c",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc050`](#insn-009fc050)

~~~json
{
  "source": "009fc050",
  "target": "2e393230676d0000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc060`](#insn-009fc060)

~~~json
{
  "source": "009fc060",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc078`](#insn-009fc078)

~~~json
{
  "source": "009fc078",
  "target": "00a47944",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc07c`](#insn-009fc07c)

~~~json
{
  "source": "009fc07c",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc080`](#insn-009fc080)

~~~json
{
  "source": "009fc080",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc084`](#insn-009fc084)

~~~json
{
  "source": "009fc084",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc08c`](#insn-009fc08c)

~~~json
{
  "source": "009fc08c",
  "target": "2e393230676d0000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc090`](#insn-009fc090)

~~~json
{
  "source": "009fc090",
  "target": "00a477cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc0a8`](#insn-009fc0a8)

~~~json
{
  "source": "009fc0a8",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc0ac`](#insn-009fc0ac)

~~~json
{
  "source": "009fc0ac",
  "target": "00c9c408",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c408",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fc0b0`](#insn-009fc0b0)

~~~json
{
  "source": "009fc0b0",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc0b4`](#insn-009fc0b4)

~~~json
{
  "source": "009fc0b4",
  "target": "009fc0d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc0c0`](#insn-009fc0c0)

~~~json
{
  "source": "009fc0c0",
  "target": "00c8c7f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8c7f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fc0c4`](#insn-009fc0c4)

~~~json
{
  "source": "009fc0c4",
  "target": "005d8fb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc0cc`](#insn-009fc0cc)

~~~json
{
  "source": "009fc0cc",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc0d4`](#insn-009fc0d4)

~~~json
{
  "source": "009fc0d4",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc0d8`](#insn-009fc0d8)

~~~json
{
  "source": "009fc0d8",
  "target": "00c9c410",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c410",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fc0dc`](#insn-009fc0dc)

~~~json
{
  "source": "009fc0dc",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc0e0`](#insn-009fc0e0)

~~~json
{
  "source": "009fc0e0",
  "target": "009fc134",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc0ec`](#insn-009fc0ec)

~~~json
{
  "source": "009fc0ec",
  "target": "00c8c850",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8c850",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fc0f0`](#insn-009fc0f0)

~~~json
{
  "source": "009fc0f0",
  "target": "009fc11c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc0fc`](#insn-009fc0fc)

~~~json
{
  "source": "009fc0fc",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc100`](#insn-009fc100)

~~~json
{
  "source": "009fc100",
  "target": "009fc11c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc118`](#insn-009fc118)

~~~json
{
  "source": "009fc118",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc124`](#insn-009fc124)

~~~json
{
  "source": "009fc124",
  "target": "00c8c7f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8c7f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fc128`](#insn-009fc128)

~~~json
{
  "source": "009fc128",
  "target": "005d8fb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc130`](#insn-009fc130)

~~~json
{
  "source": "009fc130",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc134`](#insn-009fc134)

~~~json
{
  "source": "009fc134",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc138`](#insn-009fc138)

~~~json
{
  "source": "009fc138",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc140`](#insn-009fc140)

~~~json
{
  "source": "009fc140",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc144`](#insn-009fc144)

~~~json
{
  "source": "009fc144",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc148`](#insn-009fc148)

~~~json
{
  "source": "009fc148",
  "target": "2e393230676d0000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc148`](#insn-009fc148)

~~~json
{
  "source": "009fc148",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc154`](#insn-009fc154)

~~~json
{
  "source": "009fc154",
  "target": "00c8bdc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8bdc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fc154`](#insn-009fc154)

~~~json
{
  "source": "009fc154",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc17c`](#insn-009fc17c)

~~~json
{
  "source": "009fc17c",
  "target": "008b7ff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc180`](#insn-009fc180)

~~~json
{
  "source": "009fc180",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc188`](#insn-009fc188)

~~~json
{
  "source": "009fc188",
  "target": "009fc198",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc18c`](#insn-009fc18c)

~~~json
{
  "source": "009fc18c",
  "target": "009fc1ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc194`](#insn-009fc194)

~~~json
{
  "source": "009fc194",
  "target": "009fc1a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc1a0`](#insn-009fc1a0)

~~~json
{
  "source": "009fc1a0",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc1a4`](#insn-009fc1a4)

~~~json
{
  "source": "009fc1a4",
  "target": "00c8bde0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8bde0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fc1a4`](#insn-009fc1a4)

~~~json
{
  "source": "009fc1a4",
  "target": "00c8bde8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8bde8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fc1a8`](#insn-009fc1a8)

~~~json
{
  "source": "009fc1a8",
  "target": "00a036fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc1a8`](#insn-009fc1a8)

~~~json
{
  "source": "009fc1a8",
  "target": "00a03700",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc1ac`](#insn-009fc1ac)

~~~json
{
  "source": "009fc1ac",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc1b0`](#insn-009fc1b0)

~~~json
{
  "source": "009fc1b0",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc1b4`](#insn-009fc1b4)

~~~json
{
  "source": "009fc1b4",
  "target": "009fc1d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc1c0`](#insn-009fc1c0)

~~~json
{
  "source": "009fc1c0",
  "target": "2e393230676d0000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc1c0`](#insn-009fc1c0)

~~~json
{
  "source": "009fc1c0",
  "target": "00c8c7f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8c7f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fc1c4`](#insn-009fc1c4)

~~~json
{
  "source": "009fc1c4",
  "target": "005d8fb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc1c8`](#insn-009fc1c8)

~~~json
{
  "source": "009fc1c8",
  "target": "2e393230676d0000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc1cc`](#insn-009fc1cc)

~~~json
{
  "source": "009fc1cc",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc1d0`](#insn-009fc1d0)

~~~json
{
  "source": "009fc1d0",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc1d4`](#insn-009fc1d4)

~~~json
{
  "source": "009fc1d4",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc1d8`](#insn-009fc1d8)

~~~json
{
  "source": "009fc1d8",
  "target": "009fc22c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc1e4`](#insn-009fc1e4)

~~~json
{
  "source": "009fc1e4",
  "target": "00c8c850",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8c850",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fc1e8`](#insn-009fc1e8)

~~~json
{
  "source": "009fc1e8",
  "target": "009fc214",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc1f4`](#insn-009fc1f4)

~~~json
{
  "source": "009fc1f4",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc1f8`](#insn-009fc1f8)

~~~json
{
  "source": "009fc1f8",
  "target": "009fc214",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc210`](#insn-009fc210)

~~~json
{
  "source": "009fc210",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc21c`](#insn-009fc21c)

~~~json
{
  "source": "009fc21c",
  "target": "00c8c7f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8c7f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fc220`](#insn-009fc220)

~~~json
{
  "source": "009fc220",
  "target": "005d8fb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc228`](#insn-009fc228)

~~~json
{
  "source": "009fc228",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc230`](#insn-009fc230)

~~~json
{
  "source": "009fc230",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc238`](#insn-009fc238)

~~~json
{
  "source": "009fc238",
  "target": "009fc448",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc23c`](#insn-009fc23c)

~~~json
{
  "source": "009fc23c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc240`](#insn-009fc240)

~~~json
{
  "source": "009fc240",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc244`](#insn-009fc244)

~~~json
{
  "source": "009fc244",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc248`](#insn-009fc248)

~~~json
{
  "source": "009fc248",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc24c`](#insn-009fc24c)

~~~json
{
  "source": "009fc24c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc250`](#insn-009fc250)

~~~json
{
  "source": "009fc250",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc254`](#insn-009fc254)

~~~json
{
  "source": "009fc254",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc274`](#insn-009fc274)

~~~json
{
  "source": "009fc274",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc278`](#insn-009fc278)

~~~json
{
  "source": "009fc278",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc27c`](#insn-009fc27c)

~~~json
{
  "source": "009fc27c",
  "target": "009fbd6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc280`](#insn-009fc280)

~~~json
{
  "source": "009fc280",
  "target": "009fbd7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc298`](#insn-009fc298)

~~~json
{
  "source": "009fc298",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc29c`](#insn-009fc29c)

~~~json
{
  "source": "009fc29c",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc2a0`](#insn-009fc2a0)

~~~json
{
  "source": "009fc2a0",
  "target": "009fbd84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc2a4`](#insn-009fc2a4)

~~~json
{
  "source": "009fc2a4",
  "target": "009fbd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc2ac`](#insn-009fc2ac)

~~~json
{
  "source": "009fc2ac",
  "target": "00ca5ff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5ff8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fc2b0`](#insn-009fc2b0)

~~~json
{
  "source": "009fc2b0",
  "target": "00c58ef0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc2b4`](#insn-009fc2b4)

~~~json
{
  "source": "009fc2b4",
  "target": "009fbcdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc2bc`](#insn-009fc2bc)

~~~json
{
  "source": "009fc2bc",
  "target": "00ca5fc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5fc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fc2c4`](#insn-009fc2c4)

~~~json
{
  "source": "009fc2c4",
  "target": "0047f114",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc2d0`](#insn-009fc2d0)

~~~json
{
  "source": "009fc2d0",
  "target": "00c64030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c64030",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fc2d4`](#insn-009fc2d4)

~~~json
{
  "source": "009fc2d4",
  "target": "00ca5fc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5fc8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fc2d8`](#insn-009fc2d8)

~~~json
{
  "source": "009fc2d8",
  "target": "00ca5fc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5fc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fc2d8`](#insn-009fc2d8)

~~~json
{
  "source": "009fc2d8",
  "target": "00ca5fc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5fc8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fc2e0`](#insn-009fc2e0)

~~~json
{
  "source": "009fc2e0",
  "target": "00ca5fe8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5fe8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fc2e0`](#insn-009fc2e0)

~~~json
{
  "source": "009fc2e0",
  "target": "00ca5ff0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5ff0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fc2e4`](#insn-009fc2e4)

~~~json
{
  "source": "009fc2e4",
  "target": "00ca5fe0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5fe0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fc2e8`](#insn-009fc2e8)

~~~json
{
  "source": "009fc2e8",
  "target": "00ca5fd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5fd0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fc2e8`](#insn-009fc2e8)

~~~json
{
  "source": "009fc2e8",
  "target": "00ca5fd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5fd8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fc2e8`](#insn-009fc2e8)

~~~json
{
  "source": "009fc2e8",
  "target": "00ca5fe0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5fe0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fc2ec`](#insn-009fc2ec)

~~~json
{
  "source": "009fc2ec",
  "target": "00c58ed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc2f4`](#insn-009fc2f4)

~~~json
{
  "source": "009fc2f4",
  "target": "00ca5ff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5ff8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fc2f8`](#insn-009fc2f8)

~~~json
{
  "source": "009fc2f8",
  "target": "00c58f10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fc2fc`](#insn-009fc2fc)

~~~json
{
  "source": "009fc2fc",
  "target": "009fbcdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fc448`](#insn-009fc448)

~~~json
{
  "source": "009fc448",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
