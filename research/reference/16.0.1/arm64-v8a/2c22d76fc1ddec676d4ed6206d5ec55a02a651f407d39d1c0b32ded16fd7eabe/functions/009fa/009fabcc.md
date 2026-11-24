# 009fabcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `009faa30`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fa/009faa30.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0058.md#compare-f677a4d3044c86df87fd7f09d336a42d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `009fac20`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fa/009fac20.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0060.md#compare-2efcbc91e9c1fecf53a974573c2705b6)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009fabcc",
  "name": "FUN_009fabcc",
  "size": 1848,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "13a63fce7aade6e531f3896dce4fdb12cd7b4ecce762bdf6eb9a97e5c01d0dc4",
  "source_text_sha256": "13a63fce7aade6e531f3896dce4fdb12cd7b4ecce762bdf6eb9a97e5c01d0dc4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009fabcc",
        "009fb2ff"
      ],
      [
        "009fb448",
        "009fb44b"
      ]
    ],
    "bytes_sha256": "cdbcae9947a5511fc7e2d68187858503b8a56e030ca88073f2a88619db29ecc1",
    "instruction_count": 462,
    "instruction_bytes": 1848,
    "body_bytes": 1848,
    "indirect": 10,
    "unresolved": 6
  }
}
~~~

## 呼び出し元

- [007f36a8](../007f3/007f36a8.md)
- [009fdc50](../009fd/009fdc50.md)
- [00a012f4](../00a01/00a012f4.md)
- [00a058bc](../00a05/00a058bc.md)

## 呼び出し先

- [0046daf4](../0046d/0046daf4.md)
- [0047e60c](../0047e/0047e60c.md)
- [005d8bc8](../005d8/005d8bc8.md)
- [008514f8](../00851/008514f8.md)
- [008b6fec](../008b6/008b6fec.md)
- [008b9298](../008b9/008b9298.md)
- [008b9500](../008b9/008b9500.md)
- [008b95cc](../008b9/008b95cc.md)
- [008b96a4](../008b9/008b96a4.md)
- [008b9858](../008b9/008b9858.md)
- [008ba868](../008ba/008ba868.md)
- [009e2f94](../009e2/009e2f94.md)
- [009f7478](../009f7/009f7478.md)
- [009f92c8](../009f9/009f92c8.md)
- [009f981c](../009f9/009f981c.md)
- [00a013a8](../00a01/00a013a8.md)
- [00a013ac](../00a01/00a013ac.md)
- [00a014ec](../00a01/00a014ec.md)
- [00a022d0](../00a02/00a022d0.md)
- [00a022d4](../00a02/00a022d4.md)
- [00a026fc](../00a02/00a026fc.md)
- [00a02700](../00a02/00a02700.md)
- [00a46784](../00a46/00a46784.md)
- [00a468fc](../00a46/00a468fc.md)
- [00a4754c](../00a47/00a4754c.md)
- [00a829d0](../00a82/00a829d0.md)
- [00a83260](../00a83/00a83260.md)
- [00a8344c](../00a83/00a8344c.md)
- [00ac8e10](../00ac8/00ac8e10.md)
- [00ac8e54](../00ac8/00ac8e54.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c57e30](../00c57/00c57e30.md)
- [00c57e50](../00c57/00c57e50.md)
- [00c57e70](../00c57/00c57e70.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c58610](../00c58/00c58610.md)

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

void FUN_009fabcc(long param_1)

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
  if (DAT_00ca4978 == 0) {
    lVar8 = 0;
  }
  else {
    lVar8 = __dynamic_cast(DAT_00ca4978,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65e58,
                           &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c71990,0);
  }
  lVar9 = FUN_008514f8();
                    /* try { // try from 009fac44 to 00afac4f has its CatchHandler @ 009fad00 */
  FUN_00a83260(lVar9 + 0x3078,0x2a);
  lVar9 = FUN_008514f8();
  FUN_00a83260(lVar9 + 0x3078,0x2b);
  lVar9 = FUN_008514f8();
  FUN_009f92c8(&local_158);
                    /* try { // try from 009fac68 to 00afac8b has its CatchHandler @ 009fad10 */
  FUN_00a8344c(lVar9 + 0x3078,0x2a,&local_158,0x1a,0x2c8);
  if ((local_158 & 1) != 0) {
                    /* try { // try from 009fac8c to 00afad93 has its CatchHandler @ 009fab90 */
    _ZdlPv(local_148);
  }
  lVar9 = FUN_008514f8();
  FUN_009f981c(&local_158);
  FUN_00a8344c(lVar9 + 0x3078,0x2b,&local_158,0x1a,0x2c8);
  if ((local_158 & 1) != 0) {
    _ZdlPv(local_148);
  }
  if (((DAT_00ca4f38 & 1) == 0) && (iVar6 = __cxa_guard_acquire(&DAT_00ca4f38), iVar6 != 0)) {
                    /* try { // try from 009fb2cc to 00afb2e3 has its CatchHandler @ 009fbb10 */
    DAT_00ca4f08 = 0;
    DAT_00ca4f00 = &DAT_00ca4f08;
    DAT_00ca4f28 = 0;
    DAT_00ca4f30 = 0;
                    /* try { // try from 009fb2e4 to 00afb3db has its CatchHandler @ 009fae88 */
    DAT_00ca4f20 = 0;
    DAT_00ca4f10 = 0;
    DAT_00ca4f18 = &DAT_00ca4f20;
    __cxa_atexit(FUN_0047edb4,&DAT_00ca4f00,&PTR_LOOP_00c62f90);
    __cxa_guard_release(&DAT_00ca4f38);
  }
  local_14d = 0;
  local_158 = 0x14;
  local_14f = 0x676e;
                    /* catch() { ... } // from try @ 009fac44 with catch @ 009fad00 */
  local_188 = 0x1a;
  cStack_157 = (char)s_img029_png_002b3ea9._0_8_;
  uStack_156 = SUB86(s_img029_png_002b3ea9._0_8_,1);
  cStack_150 = SUB81(s_img029_png_002b3ea9._0_8_,7);
                    /* catch() { ... } // from try @ 009fac68 with catch @ 009fad10 */
  local_17a = 0;
  uStack_187 = _DAT_002b9270;
  uStack_182 = (undefined2)s_9_imgcut_002b9275._0_3_;
  cStack_180 = SUB31(s_9_imgcut_002b9275._0_3_,2);
  acStack_17f[0] = s_9_imgcut_002b9275[3];
  acStack_17f[1] = s_9_imgcut_002b9275[4];
  acStack_17f[2] = s_9_imgcut_002b9275[5];
  acStack_17f[3] = s_9_imgcut_002b9275[6];
  acStack_17f[4] = s_9_imgcut_002b9275[7];
  FUN_0047e60c(&local_170,&DAT_00ca4f00,&local_158,&local_188,0x2601);
  plVar13 = plStack_168;
  plVar11 = local_170;
  plVar14 = *(long **)(lVar8 + 0xf0);
  local_170 = (long *)0x0;
  plStack_168 = (long *)0x0;
  *(long **)(lVar8 + 0xf0) = plVar13;
  *(long **)(lVar8 + 0xe8) = plVar11;
  plVar11 = plStack_168;
  if ((plVar14 != (long *)0x0) &&
     (lVar9 = FUN_00c53d00(0xffffffffffffffff,plVar14 + 1), plVar11 = plStack_168, lVar9 == 0)) {
    (**(code **)(*plVar14 + 0x10))(plVar14);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar14);
    plVar11 = plStack_168;
  }
  plStack_168 = plVar11;
  if ((plVar11 != (long *)0x0) && (lVar9 = FUN_00c53d00(0xffffffffffffffff,plVar11 + 1), lVar9 == 0)
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
  FUN_009f7478();
  lVar9 = FUN_008514f8();
  local_90 = local_b0;
  local_158 = 0;
  cStack_157 = 0;
  local_b0[0] = &PTR_FUN_00c8aba0;
  uVar10 = FUN_008ba868(lVar9 + 0x2f08,&local_158,0,0,4,local_b0);
  FUN_0046daf4(&local_198,0,0xfffffff6,0x354,0x216);
  uVar10 = FUN_008b9500(uVar10,local_198,uStack_190);
  uVar10 = FUN_008b9858(uVar10,0);
  if (local_90 == local_b0) {
    lVar9 = 0x20;
    pppuVar12 = local_b0;
LAB_009fae34:
    (**(code **)((long)*pppuVar12 + lVar9))();
  }
  else if (local_90 != (undefined ***)0x0) {
    lVar9 = 0x28;
    pppuVar12 = local_90;
    goto LAB_009fae34;
  }
  if ((local_158 & 1) != 0) {
    _ZdlPv(local_148);
  }
  lVar9 = FUN_008514f8();
  iVar6 = FUN_00a829d0(lVar9 + 0x3078,0x2a);
                    /* try { // try from 009fae88 to 00afaf27 has its CatchHandler @ 009fae88
                       catch() { ... } // from try @ 009fae88 with catch @ 009fae88
                       catch() { ... } // from try @ 009faf48 with catch @ 009fae88
                       catch() { ... } // from try @ 009fafc8 with catch @ 009fae88
                       catch() { ... } // from try @ 009fb09c with catch @ 009fae88
                       catch() { ... } // from try @ 009fb1d0 with catch @ 009fae88
                       catch() { ... } // from try @ 009fb2e4 with catch @ 009fae88
                       catch() { ... } // from try @ 009fb3f4 with catch @ 009fae88
                       catch() { ... } // from try @ 009fb504 with catch @ 009fae88
                       catch() { ... } // from try @ 009fb584 with catch @ 009fae88
                       catch() { ... } // from try @ 009fb660 with catch @ 009fae88
                       catch() { ... } // from try @ 009fb790 with catch @ 009fae88 */
  lVar9 = FUN_008514f8();
  iVar7 = FUN_00a829d0(lVar9 + 0x3078,0x2b);
  iVar15 = (int)((double)(iVar7 * 0x1a) * 1.2 + 75.0 +
                (double)((int)((double)(iVar6 * 0x1a) * 1.2 + 75.0 + 0.0) + 8));
  lVar9 = FUN_008514f8();
  plVar11 = (long *)FUN_009e2f94(lVar9 + 0x50,0xffffffff,0xffffffff);
  iVar6 = iVar15 + (int)((ulong)(plVar11[1] - *plVar11) >> 2) * 0x49249259 + 0x12;
  auVar17 = FUN_008b9298(uVar10);
  iVar7 = auVar17._12_4_ + -0x42;
  if (iVar7 < iVar6) {
    lVar9 = FUN_008514f8();
    fVar16 = (float)iVar7;
                    /* try { // try from 009faf28 to 00afaf47 has its CatchHandler @ 009fbb24 */
                    /* try { // try from 009faf48 to 00afafbb has its CatchHandler @ 009fae88 */
    FUN_00ac8e10(fVar16,(float)iVar6,fVar16,(long)&fde_table_entry_00337d90.initial_loc + lVar9,1,
                 auVar17._8_4_ + auVar17._0_4_ + -0x2c,auVar17._4_4_ + 0x21,0x24);
    *(undefined4 *)(param_1 + 0x54) = 0;
    lVar9 = FUN_008514f8();
    *(undefined1 *)((long)&fde_table_entry_00337f60.data_loc + lVar9) = 1;
  }
  else {
    lVar9 = FUN_008514f8();
    FUN_00ac8e54((long)&fde_table_entry_00337d90.initial_loc + lVar9);
  }
  local_c0 = (long *)_Znwm(0x28);
  *(undefined1 (*) [16])(local_c0 + 2) = auVar17;
  *local_c0 = (long)&PTR_FUN_00c8ac20;
  local_c0[1] = param_1;
  *(int *)(local_c0 + 4) = iVar15 + 0x16;
  *(int *)((long)local_c0 + 0x24) = iVar6;
  FUN_008b95cc(uVar10,local_e0);
  if (local_c0 == local_e0) {
    lVar9 = 0x20;
    plVar11 = local_e0;
LAB_009fafc8:
                    /* try { // try from 009fafc8 to 00afb083 has its CatchHandler @ 009fae88 */
    (**(code **)(*plVar11 + lVar9))();
  }
  else if (local_c0 != (long *)0x0) {
    lVar9 = 0x28;
    plVar11 = local_c0;
                    /* try { // try from 009fafbc to 00afafc7 has its CatchHandler @ 009fbb1c */
    goto LAB_009fafc8;
  }
  local_110 = &PTR_FUN_00c8aca0;
  lStack_108 = lVar8;
  local_100 = param_1;
  local_f0 = &local_110;
  FUN_008b96a4(uVar10,&local_110);
  if (local_f0 == &local_110) {
    lVar9 = 0x20;
    pppuVar12 = &local_110;
LAB_009fb018:
    (**(code **)((long)*pppuVar12 + lVar9))();
  }
  else if (local_f0 != (undefined ***)0x0) {
    lVar9 = 0x28;
    pppuVar12 = local_f0;
    goto LAB_009fb018;
  }
  FUN_00a4754c(&local_158,0x3f800000,lVar8 + 0x138,0xc9,0x267,0x91,0x26,0xa3,0xa4);
  plVar11 = (long *)CONCAT62(uStack_156,CONCAT11(cStack_157,local_158));
  (**(code **)(*plVar11 + 0x10))(plVar11,1);
  uVar2 = CONCAT62(uStack_156,CONCAT11(cStack_157,local_158));
  FUN_00a468fc(&local_170,lVar8 + 0x138,0,0,0xa2);
  plVar11 = local_170;
  local_170 = (long *)0x0;
                    /* try { // try from 009fb084 to 00afb09b has its CatchHandler @ 009fbb18 */
  local_188 = (byte)plVar11;
  uStack_187 = (undefined5)((ulong)plVar11 >> 8);
  uStack_182 = (undefined2)((ulong)plVar11 >> 0x30);
  plVar11 = (long *)FUN_00a46784(uVar2,&local_188);
                    /* try { // try from 009fb09c to 00afb1b7 has its CatchHandler @ 009fae88 */
  (**(code **)(*plVar11 + 0x10))(plVar11,1);
  puVar3 = PTR_DAT_00c9b368;
  plVar11 = (long *)CONCAT26(uStack_182,CONCAT51(uStack_187,local_188));
  local_188 = 0;
  uStack_187 = 0;
  uStack_182 = 0;
  if (plVar11 != (long *)0x0) {
    *plVar11 = (long)(PTR_DAT_00c9b368 + 0x10);
    FUN_005d8bc8(plVar11 + 10);
    _ZdlPv(plVar11);
  }
  plVar11 = local_170;
  puVar4 = PTR_DAT_00c9b370;
  local_170 = (long *)0x0;
  if (plVar11 != (long *)0x0) {
    plVar13 = (long *)plVar11[0x16];
    *plVar11 = (long)(PTR_DAT_00c9b370 + 0x10);
    if ((plVar13 != (long *)0x0) &&
       (lVar8 = FUN_00c53d00(0xffffffffffffffff,plVar13 + 1), lVar8 == 0)) {
      (**(code **)(*plVar13 + 0x10))(plVar13);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar13);
    }
    *plVar11 = (long)(puVar3 + 0x10);
    FUN_005d8bc8(plVar11 + 10);
    _ZdlPv(plVar11);
  }
  lVar8 = FUN_008514f8();
  uVar5 = uStack_156;
  local_188 = local_158;
  uVar2 = CONCAT62(uStack_156,CONCAT11(cStack_157,local_158));
  local_158 = 0;
  cStack_157 = 0;
  uStack_156 = 0;
  uStack_187 = (undefined5)((ulong)uVar2 >> 8);
  uStack_182 = (undefined2)((uint6)uVar5 >> 0x20);
  local_140 = &PTR_FUN_00c8ad20;
  uStack_138 = uVar10;
  local_120 = &local_140;
  FUN_008b6fec(lVar8 + 0x2f38,0xd1,0x81,0x249,0x91,0x3c,&local_188,&local_140);
  if (local_120 == &local_140) {
    lVar8 = 0x20;
    pppuVar12 = &local_140;
  }
  else {
    if (local_120 == (undefined ***)0x0) goto LAB_009fb1ac;
    lVar8 = 0x28;
    pppuVar12 = local_120;
  }
  (**(code **)((long)*pppuVar12 + lVar8))();
LAB_009fb1ac:
  plVar11 = (long *)CONCAT26(uStack_182,CONCAT51(uStack_187,local_188));
  local_188 = 0;
  uStack_187 = 0;
  uStack_182 = 0;
  if (plVar11 != (long *)0x0) {
                    /* try { // try from 009fb1b8 to 00afb1cf has its CatchHandler @ 009fbb14 */
    *plVar11 = (long)(puVar3 + 0x10);
    FUN_005d8bc8(plVar11 + 10);
    _ZdlPv(plVar11);
  }
                    /* try { // try from 009fb1d0 to 00afb2cb has its CatchHandler @ 009fae88 */
  plVar11 = (long *)CONCAT62(uStack_156,CONCAT11(cStack_157,local_158));
  local_158 = 0;
  cStack_157 = 0;
  uStack_156 = 0;
  if (plVar11 != (long *)0x0) {
    plVar13 = (long *)plVar11[0x16];
    *plVar11 = (long)(puVar4 + 0x10);
    if ((plVar13 != (long *)0x0) &&
       (lVar8 = FUN_00c53d00(0xffffffffffffffff,plVar13 + 1), lVar8 == 0)) {
      (**(code **)(*plVar13 + 0x10))(plVar13);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar13);
    }
    *plVar11 = (long)(puVar3 + 0x10);
    FUN_005d8bc8(plVar11 + 10);
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
<a id="insn-009fabcc"></a> `009fabcc` | `ff 83 06 d1` | sub sp,sp,#0x1a0 | `FALL_THROUGH`
<a id="insn-009fabd0"></a> `009fabd0` | `e9 23 13 6d` | stp d9,d8,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-009fabd4"></a> `009fabd4` | `fd 7b 14 a9` | stp x29,x30,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-009fabd8"></a> `009fabd8` | `fc 6f 15 a9` | stp x28,x27,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-009fabdc"></a> `009fabdc` | `fa 67 16 a9` | stp x26,x25,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-009fabe0"></a> `009fabe0` | `f8 5f 17 a9` | stp x24,x23,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-009fabe4"></a> `009fabe4` | `f6 57 18 a9` | stp x22,x21,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-009fabe8"></a> `009fabe8` | `f4 4f 19 a9` | stp x20,x19,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-009fabec"></a> `009fabec` | `fd 03 05 91` | add x29,sp,#0x140 | `FALL_THROUGH`
<a id="insn-009fabf0"></a> `009fabf0` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-009fabf4"></a> `009fabf4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-009fabf8"></a> `009fabf8` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-009fabfc"></a> `009fabfc` | `a8 03 1e f8` | stur x8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-009fac00"></a> `009fac00` | `48 15 00 d0` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-009fac04"></a> `009fac04` | `08 bd 44 f9` | ldr x8,[x8, #0x978] | `FALL_THROUGH`
<a id="insn-009fac08"></a> `009fac08` | `48 01 00 b4` | cbz x8,0x009fac30 | `CONDITIONAL_JUMP`
<a id="insn-009fac0c"></a> `009fac0c` | `41 13 00 f0` | adrp x1,0xc65000 | `FALL_THROUGH`
<a id="insn-009fac10"></a> `009fac10` | `21 60 39 91` | add x1,x1,#0xe58 | `FALL_THROUGH`
<a id="insn-009fac14"></a> `009fac14` | `a2 13 00 f0` | adrp x2,0xc71000 | `FALL_THROUGH`
<a id="insn-009fac18"></a> `009fac18` | `42 40 26 91` | add x2,x2,#0x990 | `FALL_THROUGH`
<a id="insn-009fac1c"></a> `009fac1c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-009fac20"></a> `009fac20` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-009fac24"></a> `009fac24` | `7b 76 09 94` | bl 0x00c58610 | `UNCONDITIONAL_CALL`
<a id="insn-009fac28"></a> `009fac28` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-009fac2c"></a> `009fac2c` | `02 00 00 14` | b 0x009fac34 | `UNCONDITIONAL_JUMP`
<a id="insn-009fac30"></a> `009fac30` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-009fac34"></a> `009fac34` | `31 5a f9 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-009fac38"></a> `009fac38` | `16 0f 86 52` | mov w22,#0x3078 | `FALL_THROUGH`
<a id="insn-009fac3c"></a> `009fac3c` | `41 05 80 52` | mov w1,#0x2a | `FALL_THROUGH`
<a id="insn-009fac40"></a> `009fac40` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-009fac44"></a> `009fac44` | `87 21 02 94` | bl 0x00a83260 | `UNCONDITIONAL_CALL`
<a id="insn-009fac48"></a> `009fac48` | `2c 5a f9 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-009fac4c"></a> `009fac4c` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-009fac50"></a> `009fac50` | `61 05 80 52` | mov w1,#0x2b | `FALL_THROUGH`
<a id="insn-009fac54"></a> `009fac54` | `83 21 02 94` | bl 0x00a83260 | `UNCONDITIONAL_CALL`
<a id="insn-009fac58"></a> `009fac58` | `28 5a f9 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-009fac5c"></a> `009fac5c` | `e8 23 01 91` | add x8,sp,#0x48 | `FALL_THROUGH`
<a id="insn-009fac60"></a> `009fac60` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-009fac64"></a> `009fac64` | `99 f9 ff 97` | bl 0x009f92c8 | `UNCONDITIONAL_CALL`
<a id="insn-009fac68"></a> `009fac68` | `a0 02 16 8b` | add x0,x21,x22 | `FALL_THROUGH`
<a id="insn-009fac6c"></a> `009fac6c` | `e2 23 01 91` | add x2,sp,#0x48 | `FALL_THROUGH`
<a id="insn-009fac70"></a> `009fac70` | `41 05 80 52` | mov w1,#0x2a | `FALL_THROUGH`
<a id="insn-009fac74"></a> `009fac74` | `43 03 80 52` | mov w3,#0x1a | `FALL_THROUGH`
<a id="insn-009fac78"></a> `009fac78` | `04 59 80 52` | mov w4,#0x2c8 | `FALL_THROUGH`
<a id="insn-009fac7c"></a> `009fac7c` | `f4 21 02 94` | bl 0x00a8344c | `UNCONDITIONAL_CALL`
<a id="insn-009fac80"></a> `009fac80` | `e8 23 41 39` | ldrb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009fac84"></a> `009fac84` | `68 00 00 36` | tbz w8,#0x0,0x009fac90 | `CONDITIONAL_JUMP`
<a id="insn-009fac88"></a> `009fac88` | `e0 2f 40 f9` | ldr x0,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-009fac8c"></a> `009fac8c` | `89 74 09 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-009fac90"></a> `009fac90` | `1a 5a f9 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-009fac94"></a> `009fac94` | `e8 23 01 91` | add x8,sp,#0x48 | `FALL_THROUGH`
<a id="insn-009fac98"></a> `009fac98` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-009fac9c"></a> `009fac9c` | `16 0f 86 52` | mov w22,#0x3078 | `FALL_THROUGH`
<a id="insn-009faca0"></a> `009faca0` | `df fa ff 97` | bl 0x009f981c | `UNCONDITIONAL_CALL`
<a id="insn-009faca4"></a> `009faca4` | `a0 02 16 8b` | add x0,x21,x22 | `FALL_THROUGH`
<a id="insn-009faca8"></a> `009faca8` | `e2 23 01 91` | add x2,sp,#0x48 | `FALL_THROUGH`
<a id="insn-009facac"></a> `009facac` | `61 05 80 52` | mov w1,#0x2b | `FALL_THROUGH`
<a id="insn-009facb0"></a> `009facb0` | `43 03 80 52` | mov w3,#0x1a | `FALL_THROUGH`
<a id="insn-009facb4"></a> `009facb4` | `04 59 80 52` | mov w4,#0x2c8 | `FALL_THROUGH`
<a id="insn-009facb8"></a> `009facb8` | `e5 21 02 94` | bl 0x00a8344c | `UNCONDITIONAL_CALL`
<a id="insn-009facbc"></a> `009facbc` | `e8 23 41 39` | ldrb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009facc0"></a> `009facc0` | `68 00 00 36` | tbz w8,#0x0,0x009faccc | `CONDITIONAL_JUMP`
<a id="insn-009facc4"></a> `009facc4` | `e0 2f 40 f9` | ldr x0,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-009facc8"></a> `009facc8` | `7a 74 09 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-009faccc"></a> `009faccc` | `48 15 00 d0` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-009facd0"></a> `009facd0` | `08 e1 3c 91` | add x8,x8,#0xf38 | `FALL_THROUGH`
<a id="insn-009facd4"></a> `009facd4` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-009facd8"></a> `009facd8` | `88 2e 00 36` | tbz w8,#0x0,0x009fb2a8 | `CONDITIONAL_JUMP`
<a id="insn-009facdc"></a> `009facdc` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-009face0"></a> `009face0` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-009face4"></a> `009face4` | `ff 4f 01 39` | strb wzr,[sp, #0x53] | `FALL_THROUGH`
<a id="insn-009face8"></a> `009face8` | `e8 23 01 39` | strb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009facec"></a> `009facec` | `c8 c5 ff b0` | adrp x8,0x2b3000 | `FALL_THROUGH`
<a id="insn-009facf0"></a> `009facf0` | `08 a5 3a 91` | add x8,x8,#0xea9 | `FALL_THROUGH`
<a id="insn-009facf4"></a> `009facf4` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-009facf8"></a> `009facf8` | `e9 13 05 78` | sturh w9,[sp, #0x51] | `FALL_THROUGH`
<a id="insn-009facfc"></a> `009facfc` | `49 03 80 52` | mov w9,#0x1a | `FALL_THROUGH`
<a id="insn-009fad00"></a> `009fad00` | `e9 63 00 39` | strb w9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009fad04"></a> `009fad04` | `e8 93 04 f8` | stur x8,[sp, #0x49] | `FALL_THROUGH`
<a id="insn-009fad08"></a> `009fad08` | `e8 c5 ff f0` | adrp x8,0x2b9000 | `FALL_THROUGH`
<a id="insn-009fad0c"></a> `009fad0c` | `08 c1 09 91` | add x8,x8,#0x270 | `FALL_THROUGH`
<a id="insn-009fad10"></a> `009fad10` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-009fad14"></a> `009fad14` | `08 51 40 f8` | ldur x8,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-009fad18"></a> `009fad18` | `ff 9b 00 39` | strb wzr,[sp, #0x26] | `FALL_THROUGH`
<a id="insn-009fad1c"></a> `009fad1c` | `e9 93 01 f8` | stur x9,[sp, #0x19] | `FALL_THROUGH`
<a id="insn-009fad20"></a> `009fad20` | `e8 e3 01 f8` | stur x8,[sp, #0x1e] | `FALL_THROUGH`
<a id="insn-009fad24"></a> `009fad24` | `40 15 00 d0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-009fad28"></a> `009fad28` | `00 00 3c 91` | add x0,x0,#0xf00 | `FALL_THROUGH`
<a id="insn-009fad2c"></a> `009fad2c` | `e8 c3 00 91` | add x8,sp,#0x30 | `FALL_THROUGH`
<a id="insn-009fad30"></a> `009fad30` | `e1 23 01 91` | add x1,sp,#0x48 | `FALL_THROUGH`
<a id="insn-009fad34"></a> `009fad34` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-009fad38"></a> `009fad38` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-009fad3c"></a> `009fad3c` | `34 0e ea 97` | bl 0x0047e60c | `UNCONDITIONAL_CALL`
<a id="insn-009fad40"></a> `009fad40` | `e0 0f c0 3d` | ldr q0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009fad44"></a> `009fad44` | `75 7a 40 f9` | ldr x21,[x19, #0xf0] | `FALL_THROUGH`
<a id="insn-009fad48"></a> `009fad48` | `ff 7f 03 a9` | stp xzr,xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009fad4c"></a> `009fad4c` | `60 82 8e 3c` | stur q0,[x19, #0xe8] | `FALL_THROUGH`
<a id="insn-009fad50"></a> `009fad50` | `b5 00 00 b4` | cbz x21,0x009fad64 | `CONDITIONAL_JUMP`
<a id="insn-009fad54"></a> `009fad54` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-009fad58"></a> `009fad58` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009fad5c"></a> `009fad5c` | `e9 63 09 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-009fad60"></a> `009fad60` | `00 28 00 b4` | cbz x0,0x009fb260 | `CONDITIONAL_JUMP`
<a id="insn-009fad64"></a> `009fad64` | `f5 1f 40 f9` | ldr x21,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-009fad68"></a> `009fad68` | `b5 00 00 b4` | cbz x21,0x009fad7c | `CONDITIONAL_JUMP`
<a id="insn-009fad6c"></a> `009fad6c` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-009fad70"></a> `009fad70` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009fad74"></a> `009fad74` | `e3 63 09 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-009fad78"></a> `009fad78` | `60 28 00 b4` | cbz x0,0x009fb284 | `CONDITIONAL_JUMP`
<a id="insn-009fad7c"></a> `009fad7c` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009fad80"></a> `009fad80` | `68 00 00 36` | tbz w8,#0x0,0x009fad8c | `CONDITIONAL_JUMP`
<a id="insn-009fad84"></a> `009fad84` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-009fad88"></a> `009fad88` | `4a 74 09 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-009fad8c"></a> `009fad8c` | `e8 23 41 39` | ldrb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009fad90"></a> `009fad90` | `68 00 00 36` | tbz w8,#0x0,0x009fad9c | `CONDITIONAL_JUMP`
<a id="insn-009fad94"></a> `009fad94` | `e0 2f 40 f9` | ldr x0,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-009fad98"></a> `009fad98` | `46 74 09 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-009fad9c"></a> `009fad9c` | `b7 f1 ff 97` | bl 0x009f7478 | `UNCONDITIONAL_CALL`
<a id="insn-009fada0"></a> `009fada0` | `d6 59 f9 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-009fada4"></a> `009fada4` | `88 14 00 90` | adrp x8,0xc8a000 | `FALL_THROUGH`
<a id="insn-009fada8"></a> `009fada8` | `08 81 2e 91` | add x8,x8,#0xba0 | `FALL_THROUGH`
<a id="insn-009fadac"></a> `009fadac` | `b6 43 01 d1` | sub x22,x29,#0x50 | `FALL_THROUGH`
<a id="insn-009fadb0"></a> `009fadb0` | `ff 93 00 79` | strh wzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009fadb4"></a> `009fadb4` | `a8 03 1b f8` | stur x8,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-009fadb8"></a> `009fadb8` | `08 e1 85 52` | mov w8,#0x2f08 | `FALL_THROUGH`
<a id="insn-009fadbc"></a> `009fadbc` | `b6 03 1d f8` | stur x22,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-009fadc0"></a> `009fadc0` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-009fadc4"></a> `009fadc4` | `e1 23 01 91` | add x1,sp,#0x48 | `FALL_THROUGH`
<a id="insn-009fadc8"></a> `009fadc8` | `a5 43 01 d1` | sub x5,x29,#0x50 | `FALL_THROUGH`
<a id="insn-009fadcc"></a> `009fadcc` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-009fadd0"></a> `009fadd0` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-009fadd4"></a> `009fadd4` | `84 00 80 52` | mov w4,#0x4 | `FALL_THROUGH`
<a id="insn-009fadd8"></a> `009fadd8` | `a4 fe fa 97` | bl 0x008ba868 | `UNCONDITIONAL_CALL`
<a id="insn-009faddc"></a> `009faddc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-009fade0"></a> `009fade0` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-009fade4"></a> `009fade4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-009fade8"></a> `009fade8` | `22 01 80 12` | mov w2,#0xfffffff6 | `FALL_THROUGH`
<a id="insn-009fadec"></a> `009fadec` | `83 6a 80 52` | mov w3,#0x354 | `FALL_THROUGH`
<a id="insn-009fadf0"></a> `009fadf0` | `c4 42 80 52` | mov w4,#0x216 | `FALL_THROUGH`
<a id="insn-009fadf4"></a> `009fadf4` | `40 cb e9 97` | bl 0x0046daf4 | `UNCONDITIONAL_CALL`
<a id="insn-009fadf8"></a> `009fadf8` | `e1 8b 40 a9` | ldp x1,x2,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009fadfc"></a> `009fadfc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009fae00"></a> `009fae00` | `c0 f9 fa 97` | bl 0x008b9500 | `UNCONDITIONAL_CALL`
<a id="insn-009fae04"></a> `009fae04` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-009fae08"></a> `009fae08` | `94 fa fa 97` | bl 0x008b9858 | `UNCONDITIONAL_CALL`
<a id="insn-009fae0c"></a> `009fae0c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-009fae10"></a> `009fae10` | `a0 03 5d f8` | ldur x0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-009fae14"></a> `009fae14` | `a8 43 01 d1` | sub x8,x29,#0x50 | `FALL_THROUGH`
<a id="insn-009fae18"></a> `009fae18` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-009fae1c"></a> `009fae1c` | `80 00 00 54` | b.eq 0x009fae2c | `CONDITIONAL_JUMP`
<a id="insn-009fae20"></a> `009fae20` | `00 01 00 b4` | cbz x0,0x009fae40 | `CONDITIONAL_JUMP`
<a id="insn-009fae24"></a> `009fae24` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-009fae28"></a> `009fae28` | `03 00 00 14` | b 0x009fae34 | `UNCONDITIONAL_JUMP`
<a id="insn-009fae2c"></a> `009fae2c` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-009fae30"></a> `009fae30` | `a0 43 01 d1` | sub x0,x29,#0x50 | `FALL_THROUGH`
<a id="insn-009fae34"></a> `009fae34` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-009fae38"></a> `009fae38` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-009fae3c"></a> `009fae3c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009fae40"></a> `009fae40` | `e8 23 41 39` | ldrb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009fae44"></a> `009fae44` | `68 00 00 36` | tbz w8,#0x0,0x009fae50 | `CONDITIONAL_JUMP`
<a id="insn-009fae48"></a> `009fae48` | `e0 2f 40 f9` | ldr x0,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-009fae4c"></a> `009fae4c` | `19 74 09 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-009fae50"></a> `009fae50` | `aa 59 f9 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-009fae54"></a> `009fae54` | `16 0f 86 52` | mov w22,#0x3078 | `FALL_THROUGH`
<a id="insn-009fae58"></a> `009fae58` | `41 05 80 52` | mov w1,#0x2a | `FALL_THROUGH`
<a id="insn-009fae5c"></a> `009fae5c` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-009fae60"></a> `009fae60` | `dc 1e 02 94` | bl 0x00a829d0 | `UNCONDITIONAL_CALL`
<a id="insn-009fae64"></a> `009fae64` | `57 03 80 52` | mov w23,#0x1a | `FALL_THROUGH`
<a id="insn-009fae68"></a> `009fae68` | `e9 e7 00 b2` | orr x9,xzr,#0x3333333333333333 | `FALL_THROUGH`
<a id="insn-009fae6c"></a> `009fae6c` | `01 e4 00 2f` | movi d1,#0x0 | `FALL_THROUGH`
<a id="insn-009fae70"></a> `009fae70` | `08 7c 17 1b` | mul w8,w0,w23 | `FALL_THROUGH`
<a id="insn-009fae74"></a> `009fae74` | `69 fe e7 f2` | movk x9,#0x3ff3, LSL #48 | `FALL_THROUGH`
<a id="insn-009fae78"></a> `009fae78` | `29 01 67 9e` | fmov d9,x9 | `FALL_THROUGH`
<a id="insn-009fae7c"></a> `009fae7c` | `00 01 62 1e` | scvtf d0,w8 | `FALL_THROUGH`
<a id="insn-009fae80"></a> `009fae80` | `08 00 d8 d2` | mov x8,#0xc00000000000 | `FALL_THROUGH`
<a id="insn-009fae84"></a> `009fae84` | `48 0a e8 f2` | movk x8,#0x4052, LSL #48 | `FALL_THROUGH`
<a id="insn-009fae88"></a> `009fae88` | `08 01 67 9e` | fmov d8,x8 | `FALL_THROUGH`
<a id="insn-009fae8c"></a> `009fae8c` | `00 20 49 1f` | fmadd d0,d0,d9,d8 | `FALL_THROUGH`
<a id="insn-009fae90"></a> `009fae90` | `00 28 61 1e` | fadd d0,d0,d1 | `FALL_THROUGH`
<a id="insn-009fae94"></a> `009fae94` | `08 00 78 1e` | fcvtzs w8,d0 | `FALL_THROUGH`
<a id="insn-009fae98"></a> `009fae98` | `19 21 00 11` | add w25,w8,#0x8 | `FALL_THROUGH`
<a id="insn-009fae9c"></a> `009fae9c` | `97 59 f9 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-009faea0"></a> `009faea0` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-009faea4"></a> `009faea4` | `61 05 80 52` | mov w1,#0x2b | `FALL_THROUGH`
<a id="insn-009faea8"></a> `009faea8` | `ca 1e 02 94` | bl 0x00a829d0 | `UNCONDITIONAL_CALL`
<a id="insn-009faeac"></a> `009faeac` | `08 7c 17 1b` | mul w8,w0,w23 | `FALL_THROUGH`
<a id="insn-009faeb0"></a> `009faeb0` | `20 03 62 1e` | scvtf d0,w25 | `FALL_THROUGH`
<a id="insn-009faeb4"></a> `009faeb4` | `01 01 62 1e` | scvtf d1,w8 | `FALL_THROUGH`
<a id="insn-009faeb8"></a> `009faeb8` | `21 20 49 1f` | fmadd d1,d1,d9,d8 | `FALL_THROUGH`
<a id="insn-009faebc"></a> `009faebc` | `20 28 60 1e` | fadd d0,d1,d0 | `FALL_THROUGH`
<a id="insn-009faec0"></a> `009faec0` | `16 00 78 1e` | fcvtzs w22,d0 | `FALL_THROUGH`
<a id="insn-009faec4"></a> `009faec4` | `d9 5a 00 11` | add w25,w22,#0x16 | `FALL_THROUGH`
<a id="insn-009faec8"></a> `009faec8` | `8c 59 f9 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-009faecc"></a> `009faecc` | `00 40 01 91` | add x0,x0,#0x50 | `FALL_THROUGH`
<a id="insn-009faed0"></a> `009faed0` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-009faed4"></a> `009faed4` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-009faed8"></a> `009faed8` | `2f a0 ff 97` | bl 0x009e2f94 | `UNCONDITIONAL_CALL`
<a id="insn-009faedc"></a> `009faedc` | `09 20 40 a9` | ldp x9,x8,[x0] | `FALL_THROUGH`
<a id="insn-009faee0"></a> `009faee0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009faee4"></a> `009faee4` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-009faee8"></a> `009faee8` | `29 4b 92 52` | mov w9,#0x9259 | `FALL_THROUGH`
<a id="insn-009faeec"></a> `009faeec` | `08 fd 42 d3` | lsr x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-009faef0"></a> `009faef0` | `89 24 a9 72` | movk w9,#0x4924, LSL #16 | `FALL_THROUGH`
<a id="insn-009faef4"></a> `009faef4` | `08 59 09 1b` | madd w8,w8,w9,w22 | `FALL_THROUGH`
<a id="insn-009faef8"></a> `009faef8` | `1a 49 00 11` | add w26,w8,#0x12 | `FALL_THROUGH`
<a id="insn-009faefc"></a> `009faefc` | `e7 f8 fa 97` | bl 0x008b9298 | `UNCONDITIONAL_CALL`
<a id="insn-009faf00"></a> `009faf00` | `28 fc 60 d3` | lsr x8,x1,#0x20 | `FALL_THROUGH`
<a id="insn-009faf04"></a> `009faf04` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-009faf08"></a> `009faf08` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-009faf0c"></a> `009faf0c` | `1b 09 01 51` | sub w27,w8,#0x42 | `FALL_THROUGH`
<a id="insn-009faf10"></a> `009faf10` | `5f 03 1b 6b` | cmp w26,w27 | `FALL_THROUGH`
<a id="insn-009faf14"></a> `009faf14` | `ad 02 00 54` | b.le 0x009faf68 | `CONDITIONAL_JUMP`
<a id="insn-009faf18"></a> `009faf18` | `fc fe 60 d3` | lsr x28,x23,#0x20 | `FALL_THROUGH`
<a id="insn-009faf1c"></a> `009faf1c` | `77 59 f9 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-009faf20"></a> `009faf20` | `60 03 22 1e` | scvtf s0,w27 | `FALL_THROUGH`
<a id="insn-009faf24"></a> `009faf24` | `41 03 22 1e` | scvtf s1,w26 | `FALL_THROUGH`
<a id="insn-009faf28"></a> `009faf28` | `c8 02 17 0b` | add w8,w22,w23 | `FALL_THROUGH`
<a id="insn-009faf2c"></a> `009faf2c` | `02 b1 00 51` | sub w2,w8,#0x2c | `FALL_THROUGH`
<a id="insn-009faf30"></a> `009faf30` | `08 dc 4c 91` | add x8,x0,#0x337, LSL #12 | `FALL_THROUGH`
<a id="insn-009faf34"></a> `009faf34` | `83 87 00 11` | add w3,w28,#0x21 | `FALL_THROUGH`
<a id="insn-009faf38"></a> `009faf38` | `00 41 36 91` | add x0,x8,#0xd90 | `FALL_THROUGH`
<a id="insn-009faf3c"></a> `009faf3c` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-009faf40"></a> `009faf40` | `84 04 80 52` | mov w4,#0x24 | `FALL_THROUGH`
<a id="insn-009faf44"></a> `009faf44` | `3b 00 80 52` | mov w27,#0x1 | `FALL_THROUGH`
<a id="insn-009faf48"></a> `009faf48` | `02 40 20 1e` | fmov s2,s0 | `FALL_THROUGH`
<a id="insn-009faf4c"></a> `009faf4c` | `b1 37 03 94` | bl 0x00ac8e10 | `UNCONDITIONAL_CALL`
<a id="insn-009faf50"></a> `009faf50` | `9f 56 00 b9` | str wzr,[x20, #0x54] | `FALL_THROUGH`
<a id="insn-009faf54"></a> `009faf54` | `69 59 f9 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-009faf58"></a> `009faf58` | `88 ec 8f 52` | mov w8,#0x7f64 | `FALL_THROUGH`
<a id="insn-009faf5c"></a> `009faf5c` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-009faf60"></a> `009faf60` | `1b 68 28 38` | strb w27,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-009faf64"></a> `009faf64` | `05 00 00 14` | b 0x009faf78 | `UNCONDITIONAL_JUMP`
<a id="insn-009faf68"></a> `009faf68` | `64 59 f9 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-009faf6c"></a> `009faf6c` | `08 dc 4c 91` | add x8,x0,#0x337, LSL #12 | `FALL_THROUGH`
<a id="insn-009faf70"></a> `009faf70` | `00 41 36 91` | add x0,x8,#0xd90 | `FALL_THROUGH`
<a id="insn-009faf74"></a> `009faf74` | `b8 37 03 94` | bl 0x00ac8e54 | `UNCONDITIONAL_CALL`
<a id="insn-009faf78"></a> `009faf78` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-009faf7c"></a> `009faf7c` | `c5 73 09 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-009faf80"></a> `009faf80` | `88 14 00 90` | adrp x8,0xc8a000 | `FALL_THROUGH`
<a id="insn-009faf84"></a> `009faf84` | `08 81 30 91` | add x8,x8,#0xc20 | `FALL_THROUGH`
<a id="insn-009faf88"></a> `009faf88` | `17 58 01 a9` | stp x23,x22,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-009faf8c"></a> `009faf8c` | `08 50 00 a9` | stp x8,x20,[x0] | `FALL_THROUGH`
<a id="insn-009faf90"></a> `009faf90` | `19 68 04 29` | stp w25,w26,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-009faf94"></a> `009faf94` | `a0 03 1a f8` | stur x0,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-009faf98"></a> `009faf98` | `a1 03 02 d1` | sub x1,x29,#0x80 | `FALL_THROUGH`
<a id="insn-009faf9c"></a> `009faf9c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009fafa0"></a> `009fafa0` | `b6 03 02 d1` | sub x22,x29,#0x80 | `FALL_THROUGH`
<a id="insn-009fafa4"></a> `009fafa4` | `8a f9 fa 97` | bl 0x008b95cc | `UNCONDITIONAL_CALL`
<a id="insn-009fafa8"></a> `009fafa8` | `a0 03 5a f8` | ldur x0,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-009fafac"></a> `009fafac` | `1f 00 16 eb` | cmp x0,x22 | `FALL_THROUGH`
<a id="insn-009fafb0"></a> `009fafb0` | `80 00 00 54` | b.eq 0x009fafc0 | `CONDITIONAL_JUMP`
<a id="insn-009fafb4"></a> `009fafb4` | `00 01 00 b4` | cbz x0,0x009fafd4 | `CONDITIONAL_JUMP`
<a id="insn-009fafb8"></a> `009fafb8` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-009fafbc"></a> `009fafbc` | `03 00 00 14` | b 0x009fafc8 | `UNCONDITIONAL_JUMP`
<a id="insn-009fafc0"></a> `009fafc0` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-009fafc4"></a> `009fafc4` | `a0 03 02 d1` | sub x0,x29,#0x80 | `FALL_THROUGH`
<a id="insn-009fafc8"></a> `009fafc8` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-009fafcc"></a> `009fafcc` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-009fafd0"></a> `009fafd0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009fafd4"></a> `009fafd4` | `88 14 00 90` | adrp x8,0xc8a000 | `FALL_THROUGH`
<a id="insn-009fafd8"></a> `009fafd8` | `08 81 32 91` | add x8,x8,#0xca0 | `FALL_THROUGH`
<a id="insn-009fafdc"></a> `009fafdc` | `f6 43 02 91` | add x22,sp,#0x90 | `FALL_THROUGH`
<a id="insn-009fafe0"></a> `009fafe0` | `e8 4f 09 a9` | stp x8,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-009fafe4"></a> `009fafe4` | `f4 53 00 f9` | str x20,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-009fafe8"></a> `009fafe8` | `f6 5b 00 f9` | str x22,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-009fafec"></a> `009fafec` | `e1 43 02 91` | add x1,sp,#0x90 | `FALL_THROUGH`
<a id="insn-009faff0"></a> `009faff0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009faff4"></a> `009faff4` | `ac f9 fa 97` | bl 0x008b96a4 | `UNCONDITIONAL_CALL`
<a id="insn-009faff8"></a> `009faff8` | `e0 5b 40 f9` | ldr x0,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-009faffc"></a> `009faffc` | `1f 00 16 eb` | cmp x0,x22 | `FALL_THROUGH`
<a id="insn-009fb000"></a> `009fb000` | `80 00 00 54` | b.eq 0x009fb010 | `CONDITIONAL_JUMP`
<a id="insn-009fb004"></a> `009fb004` | `00 01 00 b4` | cbz x0,0x009fb024 | `CONDITIONAL_JUMP`
<a id="insn-009fb008"></a> `009fb008` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-009fb00c"></a> `009fb00c` | `03 00 00 14` | b 0x009fb018 | `UNCONDITIONAL_JUMP`
<a id="insn-009fb010"></a> `009fb010` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-009fb014"></a> `009fb014` | `e0 43 02 91` | add x0,sp,#0x90 | `FALL_THROUGH`
<a id="insn-009fb018"></a> `009fb018` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-009fb01c"></a> `009fb01c` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-009fb020"></a> `009fb020` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009fb024"></a> `009fb024` | `00 10 2e 1e` | fmov s0,0x3f800000 | `FALL_THROUGH`
<a id="insn-009fb028"></a> `009fb028` | `e8 23 01 91` | add x8,sp,#0x48 | `FALL_THROUGH`
<a id="insn-009fb02c"></a> `009fb02c` | `60 e2 04 91` | add x0,x19,#0x138 | `FALL_THROUGH`
<a id="insn-009fb030"></a> `009fb030` | `21 19 80 52` | mov w1,#0xc9 | `FALL_THROUGH`
<a id="insn-009fb034"></a> `009fb034` | `e2 4c 80 52` | mov w2,#0x267 | `FALL_THROUGH`
<a id="insn-009fb038"></a> `009fb038` | `23 12 80 52` | mov w3,#0x91 | `FALL_THROUGH`
<a id="insn-009fb03c"></a> `009fb03c` | `c4 04 80 52` | mov w4,#0x26 | `FALL_THROUGH`
<a id="insn-009fb040"></a> `009fb040` | `65 14 80 52` | mov w5,#0xa3 | `FALL_THROUGH`
<a id="insn-009fb044"></a> `009fb044` | `86 14 80 52` | mov w6,#0xa4 | `FALL_THROUGH`
<a id="insn-009fb048"></a> `009fb048` | `41 31 01 94` | bl 0x00a4754c | `UNCONDITIONAL_CALL`
<a id="insn-009fb04c"></a> `009fb04c` | `e0 27 40 f9` | ldr x0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009fb050"></a> `009fb050` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-009fb054"></a> `009fb054` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009fb058"></a> `009fb058` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-009fb05c"></a> `009fb05c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009fb060"></a> `009fb060` | `f4 27 40 f9` | ldr x20,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009fb064"></a> `009fb064` | `e8 c3 00 91` | add x8,sp,#0x30 | `FALL_THROUGH`
<a id="insn-009fb068"></a> `009fb068` | `60 e2 04 91` | add x0,x19,#0x138 | `FALL_THROUGH`
<a id="insn-009fb06c"></a> `009fb06c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-009fb070"></a> `009fb070` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-009fb074"></a> `009fb074` | `43 14 80 52` | mov w3,#0xa2 | `FALL_THROUGH`
<a id="insn-009fb078"></a> `009fb078` | `21 2e 01 94` | bl 0x00a468fc | `UNCONDITIONAL_CALL`
<a id="insn-009fb07c"></a> `009fb07c` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009fb080"></a> `009fb080` | `ff 1b 00 f9` | str xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009fb084"></a> `009fb084` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009fb088"></a> `009fb088` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-009fb08c"></a> `009fb08c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009fb090"></a> `009fb090` | `bd 2d 01 94` | bl 0x00a46784 | `UNCONDITIONAL_CALL`
<a id="insn-009fb094"></a> `009fb094` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-009fb098"></a> `009fb098` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009fb09c"></a> `009fb09c` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-009fb0a0"></a> `009fb0a0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009fb0a4"></a> `009fb0a4` | `16 15 00 90` | adrp x22,0xc9b000 | `FALL_THROUGH`
<a id="insn-009fb0a8"></a> `009fb0a8` | `f3 0f 40 f9` | ldr x19,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009fb0ac"></a> `009fb0ac` | `d6 b6 41 f9` | ldr x22,[x22, #0x368] | `FALL_THROUGH`
<a id="insn-009fb0b0"></a> `009fb0b0` | `ff 0f 00 f9` | str xzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009fb0b4"></a> `009fb0b4` | `f3 00 00 b4` | cbz x19,0x009fb0d0 | `CONDITIONAL_JUMP`
<a id="insn-009fb0b8"></a> `009fb0b8` | `c8 42 00 91` | add x8,x22,#0x10 | `FALL_THROUGH`
<a id="insn-009fb0bc"></a> `009fb0bc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009fb0c0"></a> `009fb0c0` | `08 04 05 f8` | str x8,[x0], #0x50 | `FALL_THROUGH`
<a id="insn-009fb0c4"></a> `009fb0c4` | `c1 76 ef 97` | bl 0x005d8bc8 | `UNCONDITIONAL_CALL`
<a id="insn-009fb0c8"></a> `009fb0c8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009fb0cc"></a> `009fb0cc` | `79 73 09 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-009fb0d0"></a> `009fb0d0` | `17 15 00 90` | adrp x23,0xc9b000 | `FALL_THROUGH`
<a id="insn-009fb0d4"></a> `009fb0d4` | `f3 1b 40 f9` | ldr x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009fb0d8"></a> `009fb0d8` | `f7 ba 41 f9` | ldr x23,[x23, #0x370] | `FALL_THROUGH`
<a id="insn-009fb0dc"></a> `009fb0dc` | `ff 1b 00 f9` | str xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009fb0e0"></a> `009fb0e0` | `b3 02 00 b4` | cbz x19,0x009fb134 | `CONDITIONAL_JUMP`
<a id="insn-009fb0e4"></a> `009fb0e4` | `74 5a 40 f9` | ldr x20,[x19, #0xb0] | `FALL_THROUGH`
<a id="insn-009fb0e8"></a> `009fb0e8` | `e8 42 00 91` | add x8,x23,#0x10 | `FALL_THROUGH`
<a id="insn-009fb0ec"></a> `009fb0ec` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-009fb0f0"></a> `009fb0f0` | `74 01 00 b4` | cbz x20,0x009fb11c | `CONDITIONAL_JUMP`
<a id="insn-009fb0f4"></a> `009fb0f4` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009fb0f8"></a> `009fb0f8` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009fb0fc"></a> `009fb0fc` | `01 63 09 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-009fb100"></a> `009fb100` | `e0 00 00 b5` | cbnz x0,0x009fb11c | `CONDITIONAL_JUMP`
<a id="insn-009fb104"></a> `009fb104` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-009fb108"></a> `009fb108` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009fb10c"></a> `009fb10c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009fb110"></a> `009fb110` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009fb114"></a> `009fb114` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009fb118"></a> `009fb118` | `5a 73 09 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-009fb11c"></a> `009fb11c` | `c8 42 00 91` | add x8,x22,#0x10 | `FALL_THROUGH`
<a id="insn-009fb120"></a> `009fb120` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009fb124"></a> `009fb124` | `08 04 05 f8` | str x8,[x0], #0x50 | `FALL_THROUGH`
<a id="insn-009fb128"></a> `009fb128` | `a8 76 ef 97` | bl 0x005d8bc8 | `UNCONDITIONAL_CALL`
<a id="insn-009fb12c"></a> `009fb12c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009fb130"></a> `009fb130` | `60 73 09 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-009fb134"></a> `009fb134` | `f1 58 f9 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-009fb138"></a> `009fb138` | `e8 27 40 f9` | ldr x8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009fb13c"></a> `009fb13c` | `f3 83 01 91` | add x19,sp,#0x60 | `FALL_THROUGH`
<a id="insn-009fb140"></a> `009fb140` | `ff 27 00 f9` | str xzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009fb144"></a> `009fb144` | `f3 43 00 f9` | str x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-009fb148"></a> `009fb148` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009fb14c"></a> `009fb14c` | `68 14 00 f0` | adrp x8,0xc8a000 | `FALL_THROUGH`
<a id="insn-009fb150"></a> `009fb150` | `08 81 34 91` | add x8,x8,#0xd20 | `FALL_THROUGH`
<a id="insn-009fb154"></a> `009fb154` | `e8 57 06 a9` | stp x8,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009fb158"></a> `009fb158` | `08 e7 85 52` | mov w8,#0x2f38 | `FALL_THROUGH`
<a id="insn-009fb15c"></a> `009fb15c` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-009fb160"></a> `009fb160` | `e6 63 00 91` | add x6,sp,#0x18 | `FALL_THROUGH`
<a id="insn-009fb164"></a> `009fb164` | `e7 83 01 91` | add x7,sp,#0x60 | `FALL_THROUGH`
<a id="insn-009fb168"></a> `009fb168` | `21 1a 80 52` | mov w1,#0xd1 | `FALL_THROUGH`
<a id="insn-009fb16c"></a> `009fb16c` | `22 10 80 52` | mov w2,#0x81 | `FALL_THROUGH`
<a id="insn-009fb170"></a> `009fb170` | `23 49 80 52` | mov w3,#0x249 | `FALL_THROUGH`
<a id="insn-009fb174"></a> `009fb174` | `24 12 80 52` | mov w4,#0x91 | `FALL_THROUGH`
<a id="insn-009fb178"></a> `009fb178` | `85 07 80 52` | mov w5,#0x3c | `FALL_THROUGH`
<a id="insn-009fb17c"></a> `009fb17c` | `9c ef fa 97` | bl 0x008b6fec | `UNCONDITIONAL_CALL`
<a id="insn-009fb180"></a> `009fb180` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-009fb184"></a> `009fb184` | `1f 00 13 eb` | cmp x0,x19 | `FALL_THROUGH`
<a id="insn-009fb188"></a> `009fb188` | `80 00 00 54` | b.eq 0x009fb198 | `CONDITIONAL_JUMP`
<a id="insn-009fb18c"></a> `009fb18c` | `00 01 00 b4` | cbz x0,0x009fb1ac | `CONDITIONAL_JUMP`
<a id="insn-009fb190"></a> `009fb190` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-009fb194"></a> `009fb194` | `03 00 00 14` | b 0x009fb1a0 | `UNCONDITIONAL_JUMP`
<a id="insn-009fb198"></a> `009fb198` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-009fb19c"></a> `009fb19c` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-009fb1a0"></a> `009fb1a0` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-009fb1a4"></a> `009fb1a4` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-009fb1a8"></a> `009fb1a8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009fb1ac"></a> `009fb1ac` | `f3 0f 40 f9` | ldr x19,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009fb1b0"></a> `009fb1b0` | `ff 0f 00 f9` | str xzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009fb1b4"></a> `009fb1b4` | `f3 00 00 b4` | cbz x19,0x009fb1d0 | `CONDITIONAL_JUMP`
<a id="insn-009fb1b8"></a> `009fb1b8` | `c8 42 00 91` | add x8,x22,#0x10 | `FALL_THROUGH`
<a id="insn-009fb1bc"></a> `009fb1bc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009fb1c0"></a> `009fb1c0` | `08 04 05 f8` | str x8,[x0], #0x50 | `FALL_THROUGH`
<a id="insn-009fb1c4"></a> `009fb1c4` | `81 76 ef 97` | bl 0x005d8bc8 | `UNCONDITIONAL_CALL`
<a id="insn-009fb1c8"></a> `009fb1c8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009fb1cc"></a> `009fb1cc` | `39 73 09 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-009fb1d0"></a> `009fb1d0` | `f3 27 40 f9` | ldr x19,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009fb1d4"></a> `009fb1d4` | `ff 27 00 f9` | str xzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-009fb1d8"></a> `009fb1d8` | `b3 02 00 b4` | cbz x19,0x009fb22c | `CONDITIONAL_JUMP`
<a id="insn-009fb1dc"></a> `009fb1dc` | `74 5a 40 f9` | ldr x20,[x19, #0xb0] | `FALL_THROUGH`
<a id="insn-009fb1e0"></a> `009fb1e0` | `e8 42 00 91` | add x8,x23,#0x10 | `FALL_THROUGH`
<a id="insn-009fb1e4"></a> `009fb1e4` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-009fb1e8"></a> `009fb1e8` | `74 01 00 b4` | cbz x20,0x009fb214 | `CONDITIONAL_JUMP`
<a id="insn-009fb1ec"></a> `009fb1ec` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009fb1f0"></a> `009fb1f0` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009fb1f4"></a> `009fb1f4` | `c3 62 09 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-009fb1f8"></a> `009fb1f8` | `e0 00 00 b5` | cbnz x0,0x009fb214 | `CONDITIONAL_JUMP`
<a id="insn-009fb1fc"></a> `009fb1fc` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-009fb200"></a> `009fb200` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009fb204"></a> `009fb204` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009fb208"></a> `009fb208` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009fb20c"></a> `009fb20c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009fb210"></a> `009fb210` | `1c 73 09 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-009fb214"></a> `009fb214` | `c8 42 00 91` | add x8,x22,#0x10 | `FALL_THROUGH`
<a id="insn-009fb218"></a> `009fb218` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009fb21c"></a> `009fb21c` | `08 04 05 f8` | str x8,[x0], #0x50 | `FALL_THROUGH`
<a id="insn-009fb220"></a> `009fb220` | `6a 76 ef 97` | bl 0x005d8bc8 | `UNCONDITIONAL_CALL`
<a id="insn-009fb224"></a> `009fb224` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009fb228"></a> `009fb228` | `22 73 09 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-009fb22c"></a> `009fb22c` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-009fb230"></a> `009fb230` | `a9 03 5e f8` | ldur x9,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-009fb234"></a> `009fb234` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009fb238"></a> `009fb238` | `81 10 00 54` | b.ne 0x009fb448 | `CONDITIONAL_JUMP`
<a id="insn-009fb23c"></a> `009fb23c` | `f4 4f 59 a9` | ldp x20,x19,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-009fb240"></a> `009fb240` | `f6 57 58 a9` | ldp x22,x21,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-009fb244"></a> `009fb244` | `f8 5f 57 a9` | ldp x24,x23,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-009fb248"></a> `009fb248` | `fa 67 56 a9` | ldp x26,x25,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-009fb24c"></a> `009fb24c` | `fc 6f 55 a9` | ldp x28,x27,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-009fb250"></a> `009fb250` | `fd 7b 54 a9` | ldp x29,x30,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-009fb254"></a> `009fb254` | `e9 23 53 6d` | ldp d9,d8,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-009fb258"></a> `009fb258` | `ff 83 06 91` | add sp,sp,#0x1a0 | `FALL_THROUGH`
<a id="insn-009fb25c"></a> `009fb25c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-009fb260"></a> `009fb260` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-009fb264"></a> `009fb264` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009fb268"></a> `009fb268` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009fb26c"></a> `009fb26c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009fb270"></a> `009fb270` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009fb274"></a> `009fb274` | `03 73 09 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-009fb278"></a> `009fb278` | `f5 1f 40 f9` | ldr x21,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-009fb27c"></a> `009fb27c` | `95 d7 ff b5` | cbnz x21,0x009fad6c | `CONDITIONAL_JUMP`
<a id="insn-009fb280"></a> `009fb280` | `bf fe ff 17` | b 0x009fad7c | `UNCONDITIONAL_JUMP`
<a id="insn-009fb284"></a> `009fb284` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-009fb288"></a> `009fb288` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009fb28c"></a> `009fb28c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009fb290"></a> `009fb290` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009fb294"></a> `009fb294` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009fb298"></a> `009fb298` | `fa 72 09 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-009fb29c"></a> `009fb29c` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009fb2a0"></a> `009fb2a0` | `28 d7 07 37` | tbnz w8,#0x0,0x009fad84 | `CONDITIONAL_JUMP`
<a id="insn-009fb2a4"></a> `009fb2a4` | `ba fe ff 17` | b 0x009fad8c | `UNCONDITIONAL_JUMP`
<a id="insn-009fb2a8"></a> `009fb2a8` | `40 15 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-009fb2ac"></a> `009fb2ac` | `00 e0 3c 91` | add x0,x0,#0xf38 | `FALL_THROUGH`
<a id="insn-009fb2b0"></a> `009fb2b0` | `e8 72 09 94` | bl 0x00c57e50 | `UNCONDITIONAL_CALL`
<a id="insn-009fb2b4"></a> `009fb2b4` | `40 d1 ff 34` | cbz w0,0x009facdc | `CONDITIONAL_JUMP`
<a id="insn-009fb2b8"></a> `009fb2b8` | `41 15 00 b0` | adrp x1,0xca4000 | `FALL_THROUGH`
<a id="insn-009fb2bc"></a> `009fb2bc` | `21 00 3c 91` | add x1,x1,#0xf00 | `FALL_THROUGH`
<a id="insn-009fb2c0"></a> `009fb2c0` | `00 d4 ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-009fb2c4"></a> `009fb2c4` | `00 d0 36 91` | add x0,x0,#0xdb4 | `FALL_THROUGH`
<a id="insn-009fb2c8"></a> `009fb2c8` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-009fb2cc"></a> `009fb2cc` | `22 13 00 f0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-009fb2d0"></a> `009fb2d0` | `42 40 3e 91` | add x2,x2,#0xf90 | `FALL_THROUGH`
<a id="insn-009fb2d4"></a> `009fb2d4` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-009fb2d8"></a> `009fb2d8` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-009fb2dc"></a> `009fb2dc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-009fb2e0"></a> `009fb2e0` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-009fb2e4"></a> `009fb2e4` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-009fb2e8"></a> `009fb2e8` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-009fb2ec"></a> `009fb2ec` | `d1 72 09 94` | bl 0x00c57e30 | `UNCONDITIONAL_CALL`
<a id="insn-009fb2f0"></a> `009fb2f0` | `40 15 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-009fb2f4"></a> `009fb2f4` | `00 e0 3c 91` | add x0,x0,#0xf38 | `FALL_THROUGH`
<a id="insn-009fb2f8"></a> `009fb2f8` | `de 72 09 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-009fb2fc"></a> `009fb2fc` | `78 fe ff 17` | b 0x009facdc | `UNCONDITIONAL_JUMP`
<a id="insn-009fb448"></a> `009fb448` | `a6 72 09 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009fabcc`](#insn-009fabcc) 範囲 `[['009fabcc', '009fac0b']]`
  - `CONDITIONAL_JUMP` [`009fac08`](#insn-009fac08) → [`009fac30`](#insn-009fac30)
  - `FALL_THROUGH` [`009fac08`](#insn-009fac08) → [`009fac0c`](#insn-009fac0c)
- ブロック [`009fac0c`](#insn-009fac0c) 範囲 `[['009fac0c', '009fac2f']]`
  - `UNCONDITIONAL_JUMP` [`009fac2c`](#insn-009fac2c) → [`009fac34`](#insn-009fac34)
- ブロック [`009fac30`](#insn-009fac30) 範囲 `[['009fac30', '009fac33']]`
  - `FALL_THROUGH` [`009fac30`](#insn-009fac30) → [`009fac34`](#insn-009fac34)
- ブロック [`009fac34`](#insn-009fac34) 範囲 `[['009fac34', '009fac43']]`
  - `FALL_THROUGH` [`009fac40`](#insn-009fac40) → [`009fac44`](#insn-009fac44)
- ブロック [`009fac44`](#insn-009fac44) 範囲 `[['009fac44', '009fac67']]`
  - `FALL_THROUGH` [`009fac64`](#insn-009fac64) → [`009fac68`](#insn-009fac68)
- ブロック [`009fac68`](#insn-009fac68) 範囲 `[['009fac68', '009fac87']]`
  - `CONDITIONAL_JUMP` [`009fac84`](#insn-009fac84) → [`009fac90`](#insn-009fac90)
  - `FALL_THROUGH` [`009fac84`](#insn-009fac84) → [`009fac88`](#insn-009fac88)
- ブロック [`009fac88`](#insn-009fac88) 範囲 `[['009fac88', '009fac8b']]`
  - `FALL_THROUGH` [`009fac88`](#insn-009fac88) → [`009fac8c`](#insn-009fac8c)
- ブロック [`009fac8c`](#insn-009fac8c) 範囲 `[['009fac8c', '009fac8f']]`
  - `FALL_THROUGH` [`009fac8c`](#insn-009fac8c) → [`009fac90`](#insn-009fac90)
- ブロック [`009fac90`](#insn-009fac90) 範囲 `[['009fac90', '009facc3']]`
  - `CONDITIONAL_JUMP` [`009facc0`](#insn-009facc0) → [`009faccc`](#insn-009faccc)
  - `FALL_THROUGH` [`009facc0`](#insn-009facc0) → [`009facc4`](#insn-009facc4)
- ブロック [`009facc4`](#insn-009facc4) 範囲 `[['009facc4', '009faccb']]`
  - `FALL_THROUGH` [`009facc8`](#insn-009facc8) → [`009faccc`](#insn-009faccc)
- ブロック [`009faccc`](#insn-009faccc) 範囲 `[['009faccc', '009facdb']]`
  - `CONDITIONAL_JUMP` [`009facd8`](#insn-009facd8) → [`009fb2a8`](#insn-009fb2a8)
  - `FALL_THROUGH` [`009facd8`](#insn-009facd8) → [`009facdc`](#insn-009facdc)
- ブロック [`009facdc`](#insn-009facdc) 範囲 `[['009facdc', '009facff']]`
  - `FALL_THROUGH` [`009facfc`](#insn-009facfc) → [`009fad00`](#insn-009fad00)
- ブロック [`009fad00`](#insn-009fad00) 範囲 `[['009fad00', '009fad0f']]`
  - `FALL_THROUGH` [`009fad0c`](#insn-009fad0c) → [`009fad10`](#insn-009fad10)
- ブロック [`009fad10`](#insn-009fad10) 範囲 `[['009fad10', '009fad53']]`
  - `CONDITIONAL_JUMP` [`009fad50`](#insn-009fad50) → [`009fad64`](#insn-009fad64)
  - `FALL_THROUGH` [`009fad50`](#insn-009fad50) → [`009fad54`](#insn-009fad54)
- ブロック [`009fad54`](#insn-009fad54) 範囲 `[['009fad54', '009fad63']]`
  - `CONDITIONAL_JUMP` [`009fad60`](#insn-009fad60) → [`009fb260`](#insn-009fb260)
  - `FALL_THROUGH` [`009fad60`](#insn-009fad60) → [`009fad64`](#insn-009fad64)
- ブロック [`009fad64`](#insn-009fad64) 範囲 `[['009fad64', '009fad6b']]`
  - `CONDITIONAL_JUMP` [`009fad68`](#insn-009fad68) → [`009fad7c`](#insn-009fad7c)
  - `FALL_THROUGH` [`009fad68`](#insn-009fad68) → [`009fad6c`](#insn-009fad6c)
- ブロック [`009fad6c`](#insn-009fad6c) 範囲 `[['009fad6c', '009fad7b']]`
  - `CONDITIONAL_JUMP` [`009fad78`](#insn-009fad78) → [`009fb284`](#insn-009fb284)
  - `FALL_THROUGH` [`009fad78`](#insn-009fad78) → [`009fad7c`](#insn-009fad7c)
- ブロック [`009fad7c`](#insn-009fad7c) 範囲 `[['009fad7c', '009fad83']]`
  - `CONDITIONAL_JUMP` [`009fad80`](#insn-009fad80) → [`009fad8c`](#insn-009fad8c)
  - `FALL_THROUGH` [`009fad80`](#insn-009fad80) → [`009fad84`](#insn-009fad84)
- ブロック [`009fad84`](#insn-009fad84) 範囲 `[['009fad84', '009fad8b']]`
  - `FALL_THROUGH` [`009fad88`](#insn-009fad88) → [`009fad8c`](#insn-009fad8c)
- ブロック [`009fad8c`](#insn-009fad8c) 範囲 `[['009fad8c', '009fad93']]`
  - `CONDITIONAL_JUMP` [`009fad90`](#insn-009fad90) → [`009fad9c`](#insn-009fad9c)
  - `FALL_THROUGH` [`009fad90`](#insn-009fad90) → [`009fad94`](#insn-009fad94)
- ブロック [`009fad94`](#insn-009fad94) 範囲 `[['009fad94', '009fad9b']]`
  - `FALL_THROUGH` [`009fad98`](#insn-009fad98) → [`009fad9c`](#insn-009fad9c)
- ブロック [`009fad9c`](#insn-009fad9c) 範囲 `[['009fad9c', '009fae1f']]`
  - `CONDITIONAL_JUMP` [`009fae1c`](#insn-009fae1c) → [`009fae2c`](#insn-009fae2c)
  - `FALL_THROUGH` [`009fae1c`](#insn-009fae1c) → [`009fae20`](#insn-009fae20)
- ブロック [`009fae20`](#insn-009fae20) 範囲 `[['009fae20', '009fae23']]`
  - `CONDITIONAL_JUMP` [`009fae20`](#insn-009fae20) → [`009fae40`](#insn-009fae40)
  - `FALL_THROUGH` [`009fae20`](#insn-009fae20) → [`009fae24`](#insn-009fae24)
- ブロック [`009fae24`](#insn-009fae24) 範囲 `[['009fae24', '009fae2b']]`
  - `UNCONDITIONAL_JUMP` [`009fae28`](#insn-009fae28) → [`009fae34`](#insn-009fae34)
- ブロック [`009fae2c`](#insn-009fae2c) 範囲 `[['009fae2c', '009fae33']]`
  - `FALL_THROUGH` [`009fae30`](#insn-009fae30) → [`009fae34`](#insn-009fae34)
- ブロック [`009fae34`](#insn-009fae34) 範囲 `[['009fae34', '009fae3f']]`
  - `FALL_THROUGH` [`009fae3c`](#insn-009fae3c) → [`009fae40`](#insn-009fae40)
- ブロック [`009fae40`](#insn-009fae40) 範囲 `[['009fae40', '009fae47']]`
  - `CONDITIONAL_JUMP` [`009fae44`](#insn-009fae44) → [`009fae50`](#insn-009fae50)
  - `FALL_THROUGH` [`009fae44`](#insn-009fae44) → [`009fae48`](#insn-009fae48)
- ブロック [`009fae48`](#insn-009fae48) 範囲 `[['009fae48', '009fae4f']]`
  - `FALL_THROUGH` [`009fae4c`](#insn-009fae4c) → [`009fae50`](#insn-009fae50)
- ブロック [`009fae50`](#insn-009fae50) 範囲 `[['009fae50', '009fae87']]`
  - `FALL_THROUGH` [`009fae84`](#insn-009fae84) → [`009fae88`](#insn-009fae88)
- ブロック [`009fae88`](#insn-009fae88) 範囲 `[['009fae88', '009faf17']]`
  - `CONDITIONAL_JUMP` [`009faf14`](#insn-009faf14) → [`009faf68`](#insn-009faf68)
  - `FALL_THROUGH` [`009faf14`](#insn-009faf14) → [`009faf18`](#insn-009faf18)
- ブロック [`009faf18`](#insn-009faf18) 範囲 `[['009faf18', '009faf27']]`
  - `FALL_THROUGH` [`009faf24`](#insn-009faf24) → [`009faf28`](#insn-009faf28)
- ブロック [`009faf28`](#insn-009faf28) 範囲 `[['009faf28', '009faf47']]`
  - `FALL_THROUGH` [`009faf44`](#insn-009faf44) → [`009faf48`](#insn-009faf48)
- ブロック [`009faf48`](#insn-009faf48) 範囲 `[['009faf48', '009faf67']]`
  - `UNCONDITIONAL_JUMP` [`009faf64`](#insn-009faf64) → [`009faf78`](#insn-009faf78)
- ブロック [`009faf68`](#insn-009faf68) 範囲 `[['009faf68', '009faf77']]`
  - `FALL_THROUGH` [`009faf74`](#insn-009faf74) → [`009faf78`](#insn-009faf78)
- ブロック [`009faf78`](#insn-009faf78) 範囲 `[['009faf78', '009fafb3']]`
  - `CONDITIONAL_JUMP` [`009fafb0`](#insn-009fafb0) → [`009fafc0`](#insn-009fafc0)
  - `FALL_THROUGH` [`009fafb0`](#insn-009fafb0) → [`009fafb4`](#insn-009fafb4)
- ブロック [`009fafb4`](#insn-009fafb4) 範囲 `[['009fafb4', '009fafb7']]`
  - `CONDITIONAL_JUMP` [`009fafb4`](#insn-009fafb4) → [`009fafd4`](#insn-009fafd4)
  - `FALL_THROUGH` [`009fafb4`](#insn-009fafb4) → [`009fafb8`](#insn-009fafb8)
- ブロック [`009fafb8`](#insn-009fafb8) 範囲 `[['009fafb8', '009fafbb']]`
  - `FALL_THROUGH` [`009fafb8`](#insn-009fafb8) → [`009fafbc`](#insn-009fafbc)
- ブロック [`009fafbc`](#insn-009fafbc) 範囲 `[['009fafbc', '009fafbf']]`
  - `UNCONDITIONAL_JUMP` [`009fafbc`](#insn-009fafbc) → [`009fafc8`](#insn-009fafc8)
- ブロック [`009fafc0`](#insn-009fafc0) 範囲 `[['009fafc0', '009fafc7']]`
  - `FALL_THROUGH` [`009fafc4`](#insn-009fafc4) → [`009fafc8`](#insn-009fafc8)
- ブロック [`009fafc8`](#insn-009fafc8) 範囲 `[['009fafc8', '009fafd3']]`
  - `FALL_THROUGH` [`009fafd0`](#insn-009fafd0) → [`009fafd4`](#insn-009fafd4)
- ブロック [`009fafd4`](#insn-009fafd4) 範囲 `[['009fafd4', '009fb003']]`
  - `CONDITIONAL_JUMP` [`009fb000`](#insn-009fb000) → [`009fb010`](#insn-009fb010)
  - `FALL_THROUGH` [`009fb000`](#insn-009fb000) → [`009fb004`](#insn-009fb004)
- ブロック [`009fb004`](#insn-009fb004) 範囲 `[['009fb004', '009fb007']]`
  - `CONDITIONAL_JUMP` [`009fb004`](#insn-009fb004) → [`009fb024`](#insn-009fb024)
  - `FALL_THROUGH` [`009fb004`](#insn-009fb004) → [`009fb008`](#insn-009fb008)
- ブロック [`009fb008`](#insn-009fb008) 範囲 `[['009fb008', '009fb00f']]`
  - `UNCONDITIONAL_JUMP` [`009fb00c`](#insn-009fb00c) → [`009fb018`](#insn-009fb018)
- ブロック [`009fb010`](#insn-009fb010) 範囲 `[['009fb010', '009fb017']]`
  - `FALL_THROUGH` [`009fb014`](#insn-009fb014) → [`009fb018`](#insn-009fb018)
- ブロック [`009fb018`](#insn-009fb018) 範囲 `[['009fb018', '009fb023']]`
  - `FALL_THROUGH` [`009fb020`](#insn-009fb020) → [`009fb024`](#insn-009fb024)
- ブロック [`009fb024`](#insn-009fb024) 範囲 `[['009fb024', '009fb083']]`
  - `FALL_THROUGH` [`009fb080`](#insn-009fb080) → [`009fb084`](#insn-009fb084)
- ブロック [`009fb084`](#insn-009fb084) 範囲 `[['009fb084', '009fb09b']]`
  - `FALL_THROUGH` [`009fb098`](#insn-009fb098) → [`009fb09c`](#insn-009fb09c)
- ブロック [`009fb09c`](#insn-009fb09c) 範囲 `[['009fb09c', '009fb0b7']]`
  - `CONDITIONAL_JUMP` [`009fb0b4`](#insn-009fb0b4) → [`009fb0d0`](#insn-009fb0d0)
  - `FALL_THROUGH` [`009fb0b4`](#insn-009fb0b4) → [`009fb0b8`](#insn-009fb0b8)
- ブロック [`009fb0b8`](#insn-009fb0b8) 範囲 `[['009fb0b8', '009fb0cf']]`
  - `FALL_THROUGH` [`009fb0cc`](#insn-009fb0cc) → [`009fb0d0`](#insn-009fb0d0)
- ブロック [`009fb0d0`](#insn-009fb0d0) 範囲 `[['009fb0d0', '009fb0e3']]`
  - `CONDITIONAL_JUMP` [`009fb0e0`](#insn-009fb0e0) → [`009fb134`](#insn-009fb134)
  - `FALL_THROUGH` [`009fb0e0`](#insn-009fb0e0) → [`009fb0e4`](#insn-009fb0e4)
- ブロック [`009fb0e4`](#insn-009fb0e4) 範囲 `[['009fb0e4', '009fb0f3']]`
  - `CONDITIONAL_JUMP` [`009fb0f0`](#insn-009fb0f0) → [`009fb11c`](#insn-009fb11c)
  - `FALL_THROUGH` [`009fb0f0`](#insn-009fb0f0) → [`009fb0f4`](#insn-009fb0f4)
- ブロック [`009fb0f4`](#insn-009fb0f4) 範囲 `[['009fb0f4', '009fb103']]`
  - `CONDITIONAL_JUMP` [`009fb100`](#insn-009fb100) → [`009fb11c`](#insn-009fb11c)
  - `FALL_THROUGH` [`009fb100`](#insn-009fb100) → [`009fb104`](#insn-009fb104)
- ブロック [`009fb104`](#insn-009fb104) 範囲 `[['009fb104', '009fb11b']]`
  - `FALL_THROUGH` [`009fb118`](#insn-009fb118) → [`009fb11c`](#insn-009fb11c)
- ブロック [`009fb11c`](#insn-009fb11c) 範囲 `[['009fb11c', '009fb133']]`
  - `FALL_THROUGH` [`009fb130`](#insn-009fb130) → [`009fb134`](#insn-009fb134)
- ブロック [`009fb134`](#insn-009fb134) 範囲 `[['009fb134', '009fb18b']]`
  - `CONDITIONAL_JUMP` [`009fb188`](#insn-009fb188) → [`009fb198`](#insn-009fb198)
  - `FALL_THROUGH` [`009fb188`](#insn-009fb188) → [`009fb18c`](#insn-009fb18c)
- ブロック [`009fb18c`](#insn-009fb18c) 範囲 `[['009fb18c', '009fb18f']]`
  - `CONDITIONAL_JUMP` [`009fb18c`](#insn-009fb18c) → [`009fb1ac`](#insn-009fb1ac)
  - `FALL_THROUGH` [`009fb18c`](#insn-009fb18c) → [`009fb190`](#insn-009fb190)
- ブロック [`009fb190`](#insn-009fb190) 範囲 `[['009fb190', '009fb197']]`
  - `UNCONDITIONAL_JUMP` [`009fb194`](#insn-009fb194) → [`009fb1a0`](#insn-009fb1a0)
- ブロック [`009fb198`](#insn-009fb198) 範囲 `[['009fb198', '009fb19f']]`
  - `FALL_THROUGH` [`009fb19c`](#insn-009fb19c) → [`009fb1a0`](#insn-009fb1a0)
- ブロック [`009fb1a0`](#insn-009fb1a0) 範囲 `[['009fb1a0', '009fb1ab']]`
  - `FALL_THROUGH` [`009fb1a8`](#insn-009fb1a8) → [`009fb1ac`](#insn-009fb1ac)
- ブロック [`009fb1ac`](#insn-009fb1ac) 範囲 `[['009fb1ac', '009fb1b7']]`
  - `CONDITIONAL_JUMP` [`009fb1b4`](#insn-009fb1b4) → [`009fb1d0`](#insn-009fb1d0)
  - `FALL_THROUGH` [`009fb1b4`](#insn-009fb1b4) → [`009fb1b8`](#insn-009fb1b8)
- ブロック [`009fb1b8`](#insn-009fb1b8) 範囲 `[['009fb1b8', '009fb1cf']]`
  - `FALL_THROUGH` [`009fb1cc`](#insn-009fb1cc) → [`009fb1d0`](#insn-009fb1d0)
- ブロック [`009fb1d0`](#insn-009fb1d0) 範囲 `[['009fb1d0', '009fb1db']]`
  - `CONDITIONAL_JUMP` [`009fb1d8`](#insn-009fb1d8) → [`009fb22c`](#insn-009fb22c)
  - `FALL_THROUGH` [`009fb1d8`](#insn-009fb1d8) → [`009fb1dc`](#insn-009fb1dc)
- ブロック [`009fb1dc`](#insn-009fb1dc) 範囲 `[['009fb1dc', '009fb1eb']]`
  - `CONDITIONAL_JUMP` [`009fb1e8`](#insn-009fb1e8) → [`009fb214`](#insn-009fb214)
  - `FALL_THROUGH` [`009fb1e8`](#insn-009fb1e8) → [`009fb1ec`](#insn-009fb1ec)
- ブロック [`009fb1ec`](#insn-009fb1ec) 範囲 `[['009fb1ec', '009fb1fb']]`
  - `CONDITIONAL_JUMP` [`009fb1f8`](#insn-009fb1f8) → [`009fb214`](#insn-009fb214)
  - `FALL_THROUGH` [`009fb1f8`](#insn-009fb1f8) → [`009fb1fc`](#insn-009fb1fc)
- ブロック [`009fb1fc`](#insn-009fb1fc) 範囲 `[['009fb1fc', '009fb213']]`
  - `FALL_THROUGH` [`009fb210`](#insn-009fb210) → [`009fb214`](#insn-009fb214)
- ブロック [`009fb214`](#insn-009fb214) 範囲 `[['009fb214', '009fb22b']]`
  - `FALL_THROUGH` [`009fb228`](#insn-009fb228) → [`009fb22c`](#insn-009fb22c)
- ブロック [`009fb22c`](#insn-009fb22c) 範囲 `[['009fb22c', '009fb23b']]`
  - `CONDITIONAL_JUMP` [`009fb238`](#insn-009fb238) → [`009fb448`](#insn-009fb448)
  - `FALL_THROUGH` [`009fb238`](#insn-009fb238) → [`009fb23c`](#insn-009fb23c)
- ブロック [`009fb23c`](#insn-009fb23c) 範囲 `[['009fb23c', '009fb25f']]`
- ブロック [`009fb260`](#insn-009fb260) 範囲 `[['009fb260', '009fb27f']]`
  - `CONDITIONAL_JUMP` [`009fb27c`](#insn-009fb27c) → [`009fad6c`](#insn-009fad6c)
  - `FALL_THROUGH` [`009fb27c`](#insn-009fb27c) → [`009fb280`](#insn-009fb280)
- ブロック [`009fb280`](#insn-009fb280) 範囲 `[['009fb280', '009fb283']]`
  - `UNCONDITIONAL_JUMP` [`009fb280`](#insn-009fb280) → [`009fad7c`](#insn-009fad7c)
- ブロック [`009fb284`](#insn-009fb284) 範囲 `[['009fb284', '009fb2a3']]`
  - `CONDITIONAL_JUMP` [`009fb2a0`](#insn-009fb2a0) → [`009fad84`](#insn-009fad84)
  - `FALL_THROUGH` [`009fb2a0`](#insn-009fb2a0) → [`009fb2a4`](#insn-009fb2a4)
- ブロック [`009fb2a4`](#insn-009fb2a4) 範囲 `[['009fb2a4', '009fb2a7']]`
  - `UNCONDITIONAL_JUMP` [`009fb2a4`](#insn-009fb2a4) → [`009fad8c`](#insn-009fad8c)
- ブロック [`009fb2a8`](#insn-009fb2a8) 範囲 `[['009fb2a8', '009fb2b7']]`
  - `CONDITIONAL_JUMP` [`009fb2b4`](#insn-009fb2b4) → [`009facdc`](#insn-009facdc)
  - `FALL_THROUGH` [`009fb2b4`](#insn-009fb2b4) → [`009fb2b8`](#insn-009fb2b8)
- ブロック [`009fb2b8`](#insn-009fb2b8) 範囲 `[['009fb2b8', '009fb2cb']]`
  - `FALL_THROUGH` [`009fb2c8`](#insn-009fb2c8) → [`009fb2cc`](#insn-009fb2cc)
- ブロック [`009fb2cc`](#insn-009fb2cc) 範囲 `[['009fb2cc', '009fb2e3']]`
  - `FALL_THROUGH` [`009fb2e0`](#insn-009fb2e0) → [`009fb2e4`](#insn-009fb2e4)
- ブロック [`009fb2e4`](#insn-009fb2e4) 範囲 `[['009fb2e4', '009fb2ff']]`
  - `UNCONDITIONAL_JUMP` [`009fb2fc`](#insn-009fb2fc) → [`009facdc`](#insn-009facdc)
- ブロック [`009fb448`](#insn-009fb448) 範囲 `[['009fb448', '009fb44b']]`

## 命令位置別の参照

- [`009fabd0`](#insn-009fabd0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fabd4`](#insn-009fabd4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fabd8`](#insn-009fabd8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fabdc`](#insn-009fabdc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fabe0`](#insn-009fabe0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fabe4`](#insn-009fabe4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fabe8`](#insn-009fabe8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fabfc`](#insn-009fabfc) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fac04`](#insn-009fac04) → `00ca4978`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009fac08`](#insn-009fac08) → [`009fac30`](#insn-009fac30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fac10`](#insn-009fac10) → `00c65e58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`009fac18`](#insn-009fac18) → `00c71990`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`009fac24`](#insn-009fac24) → [`00c58610`](../00c58/00c58610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58610` · 推定シンボル `None` · 推定型 `None`
- [`009fac2c`](#insn-009fac2c) → [`009fac34`](#insn-009fac34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fac34`](#insn-009fac34) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`009fac44`](#insn-009fac44) → [`00a83260`](../00a83/00a83260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a83260` · 推定シンボル `None` · 推定型 `None`
- [`009fac48`](#insn-009fac48) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`009fac54`](#insn-009fac54) → [`00a83260`](../00a83/00a83260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a83260` · 推定シンボル `None` · 推定型 `None`
- [`009fac58`](#insn-009fac58) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`009fac64`](#insn-009fac64) → [`009f92c8`](../009f9/009f92c8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009f92c8` · 推定シンボル `None` · 推定型 `None`
- [`009fac7c`](#insn-009fac7c) → [`00a8344c`](../00a83/00a8344c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a8344c` · 推定シンボル `None` · 推定型 `None`
- [`009fac80`](#insn-009fac80) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fac84`](#insn-009fac84) → [`009fac90`](#insn-009fac90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fac88`](#insn-009fac88) → `Stack[-0x148]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fac8c`](#insn-009fac8c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`009fac90`](#insn-009fac90) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`009faca0`](#insn-009faca0) → [`009f981c`](../009f9/009f981c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009f981c` · 推定シンボル `None` · 推定型 `None`
- [`009facb8`](#insn-009facb8) → [`00a8344c`](../00a83/00a8344c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a8344c` · 推定シンボル `None` · 推定型 `None`
- [`009facbc`](#insn-009facbc) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009facc0`](#insn-009facc0) → [`009faccc`](#insn-009faccc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009facc4`](#insn-009facc4) → `Stack[-0x148]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009facc8`](#insn-009facc8) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`009facd4`](#insn-009facd4) → `00ca4f38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`009facd8`](#insn-009facd8) → [`009fb2a8`](#insn-009fb2a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009face4`](#insn-009face4) → `Stack[-0x14d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009face8`](#insn-009face8) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009facf4`](#insn-009facf4) → `002b3ea9`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`009facf8`](#insn-009facf8) → `Stack[-0x14f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fad00`](#insn-009fad00) → `Stack[-0x188]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fad04`](#insn-009fad04) → `Stack[-0x157]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fad10`](#insn-009fad10) → `002b9270`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fad14`](#insn-009fad14) → `002b9275`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`009fad18`](#insn-009fad18) → `Stack[-0x17a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fad1c`](#insn-009fad1c) → `Stack[-0x187]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fad20`](#insn-009fad20) → `Stack[-0x182]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fad28`](#insn-009fad28) → `00ca4f00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009fad3c`](#insn-009fad3c) → [`0047e60c`](../0047e/0047e60c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047e60c` · 推定シンボル `None` · 推定型 `None`
- [`009fad40`](#insn-009fad40) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fad48`](#insn-009fad48) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fad50`](#insn-009fad50) → [`009fad64`](#insn-009fad64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fad5c`](#insn-009fad5c) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`009fad60`](#insn-009fad60) → [`009fb260`](#insn-009fb260) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fad64`](#insn-009fad64) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fad68`](#insn-009fad68) → [`009fad7c`](#insn-009fad7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fad74`](#insn-009fad74) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`009fad78`](#insn-009fad78) → [`009fb284`](#insn-009fb284) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fad7c`](#insn-009fad7c) → `Stack[-0x188]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fad80`](#insn-009fad80) → [`009fad8c`](#insn-009fad8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fad84`](#insn-009fad84) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fad88`](#insn-009fad88) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`009fad8c`](#insn-009fad8c) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fad90`](#insn-009fad90) → [`009fad9c`](#insn-009fad9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fad94`](#insn-009fad94) → `Stack[-0x148]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fad98`](#insn-009fad98) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`009fad9c`](#insn-009fad9c) → [`009f7478`](../009f7/009f7478.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009f7478` · 推定シンボル `None` · 推定型 `None`
- [`009fada0`](#insn-009fada0) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`009fadb0`](#insn-009fadb0) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fadb4`](#insn-009fadb4) → `00c8aba0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fadb4`](#insn-009fadb4) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fadbc`](#insn-009fadbc) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fadd8`](#insn-009fadd8) → [`008ba868`](../008ba/008ba868.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008ba868` · 推定シンボル `None` · 推定型 `None`
- [`009fadf4`](#insn-009fadf4) → [`0046daf4`](../0046d/0046daf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046daf4` · 推定シンボル `None` · 推定型 `None`
- [`009fadf8`](#insn-009fadf8) → `Stack[-0x198]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fae00`](#insn-009fae00) → [`008b9500`](../008b9/008b9500.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9500` · 推定シンボル `None` · 推定型 `None`
- [`009fae08`](#insn-009fae08) → [`008b9858`](../008b9/008b9858.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9858` · 推定シンボル `None` · 推定型 `None`
- [`009fae10`](#insn-009fae10) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fae1c`](#insn-009fae1c) → [`009fae2c`](#insn-009fae2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fae20`](#insn-009fae20) → [`009fae40`](#insn-009fae40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fae28`](#insn-009fae28) → [`009fae34`](#insn-009fae34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fae34`](#insn-009fae34) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fae38`](#insn-009fae38) → `00c8abc0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`009fae38`](#insn-009fae38) → `00c8abc8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fae3c`](#insn-009fae3c) → [`00a013a8`](../00a01/00a013a8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00a013a8` · 推定シンボル `None` · 推定型 `None`
- [`009fae3c`](#insn-009fae3c) → [`00a013ac`](../00a01/00a013ac.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00a013ac` · 推定シンボル `None` · 推定型 `None`
- [`009fae40`](#insn-009fae40) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fae44`](#insn-009fae44) → [`009fae50`](#insn-009fae50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fae48`](#insn-009fae48) → `Stack[-0x148]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fae4c`](#insn-009fae4c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`009fae50`](#insn-009fae50) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`009fae60`](#insn-009fae60) → [`00a829d0`](../00a82/00a829d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a829d0` · 推定シンボル `None` · 推定型 `None`
- [`009fae9c`](#insn-009fae9c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`009faea8`](#insn-009faea8) → [`00a829d0`](../00a82/00a829d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a829d0` · 推定シンボル `None` · 推定型 `None`
- [`009faec8`](#insn-009faec8) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`009faed8`](#insn-009faed8) → [`009e2f94`](../009e2/009e2f94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009e2f94` · 推定シンボル `None` · 推定型 `None`
- [`009faefc`](#insn-009faefc) → [`008b9298`](../008b9/008b9298.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9298` · 推定シンボル `None` · 推定型 `None`
- [`009faf14`](#insn-009faf14) → [`009faf68`](#insn-009faf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009faf1c`](#insn-009faf1c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`009faf4c`](#insn-009faf4c) → [`00ac8e10`](../00ac8/00ac8e10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac8e10` · 推定シンボル `None` · 推定型 `None`
- [`009faf54`](#insn-009faf54) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`009faf60`](#insn-009faf60) → `00337f64`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009faf64`](#insn-009faf64) → [`009faf78`](#insn-009faf78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009faf68`](#insn-009faf68) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`009faf74`](#insn-009faf74) → [`00ac8e54`](../00ac8/00ac8e54.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac8e54` · 推定シンボル `None` · 推定型 `None`
- [`009faf7c`](#insn-009faf7c) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`009faf8c`](#insn-009faf8c) → `00c8ac20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009faf94`](#insn-009faf94) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fafa4`](#insn-009fafa4) → [`008b95cc`](../008b9/008b95cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b95cc` · 推定シンボル `None` · 推定型 `None`
- [`009fafa8`](#insn-009fafa8) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fafb0`](#insn-009fafb0) → [`009fafc0`](#insn-009fafc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fafb4`](#insn-009fafb4) → [`009fafd4`](#insn-009fafd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fafbc`](#insn-009fafbc) → [`009fafc8`](#insn-009fafc8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fafc8`](#insn-009fafc8) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fafcc`](#insn-009fafcc) → `00c8ac48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fafd0`](#insn-009fafd0) → [`00a014ec`](../00a01/00a014ec.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00a014ec` · 推定シンボル `None` · 推定型 `None`
- [`009fafe0`](#insn-009fafe0) → `00c8aca0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fafe0`](#insn-009fafe0) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fafe4`](#insn-009fafe4) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fafe8`](#insn-009fafe8) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009faff4`](#insn-009faff4) → [`008b96a4`](../008b9/008b96a4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b96a4` · 推定シンボル `None` · 推定型 `None`
- [`009faff8`](#insn-009faff8) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb000`](#insn-009fb000) → [`009fb010`](#insn-009fb010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb004`](#insn-009fb004) → [`009fb024`](#insn-009fb024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb00c`](#insn-009fb00c) → [`009fb018`](#insn-009fb018) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb018`](#insn-009fb018) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb01c`](#insn-009fb01c) → `00c8acc0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`009fb01c`](#insn-009fb01c) → `00c8acc8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fb020`](#insn-009fb020) → [`00a022d0`](../00a02/00a022d0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00a022d0` · 推定シンボル `None` · 推定型 `None`
- [`009fb020`](#insn-009fb020) → [`00a022d4`](../00a02/00a022d4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00a022d4` · 推定シンボル `None` · 推定型 `None`
- [`009fb048`](#insn-009fb048) → [`00a4754c`](../00a47/00a4754c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a4754c` · 推定シンボル `None` · 推定型 `None`
- [`009fb04c`](#insn-009fb04c) → `2e393230676d0000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb04c`](#insn-009fb04c) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb050`](#insn-009fb050) → `2e393230676d0000`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb060`](#insn-009fb060) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb078`](#insn-009fb078) → [`00a468fc`](../00a46/00a468fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a468fc` · 推定シンボル `None` · 推定型 `None`
- [`009fb07c`](#insn-009fb07c) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb080`](#insn-009fb080) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb084`](#insn-009fb084) → `Stack[-0x188]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb08c`](#insn-009fb08c) → `2e393230676d0000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb090`](#insn-009fb090) → [`00a46784`](../00a46/00a46784.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a46784` · 推定シンボル `None` · 推定型 `None`
- [`009fb0a8`](#insn-009fb0a8) → `Stack[-0x188]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb0ac`](#insn-009fb0ac) → `00c9b368`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`009fb0b0`](#insn-009fb0b0) → `Stack[-0x188]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb0b4`](#insn-009fb0b4) → [`009fb0d0`](#insn-009fb0d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb0c0`](#insn-009fb0c0) → `00c8b758`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fb0c4`](#insn-009fb0c4) → [`005d8bc8`](../005d8/005d8bc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d8bc8` · 推定シンボル `None` · 推定型 `None`
- [`009fb0cc`](#insn-009fb0cc) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`009fb0d4`](#insn-009fb0d4) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb0d8`](#insn-009fb0d8) → `00c9b370`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`009fb0dc`](#insn-009fb0dc) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb0e0`](#insn-009fb0e0) → [`009fb134`](#insn-009fb134) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb0ec`](#insn-009fb0ec) → `00c8b7b0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fb0f0`](#insn-009fb0f0) → [`009fb11c`](#insn-009fb11c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb0fc`](#insn-009fb0fc) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`009fb100`](#insn-009fb100) → [`009fb11c`](#insn-009fb11c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb118`](#insn-009fb118) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`009fb124`](#insn-009fb124) → `00c8b758`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fb128`](#insn-009fb128) → [`005d8bc8`](../005d8/005d8bc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d8bc8` · 推定シンボル `None` · 推定型 `None`
- [`009fb130`](#insn-009fb130) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`009fb134`](#insn-009fb134) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`009fb138`](#insn-009fb138) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb140`](#insn-009fb140) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb144`](#insn-009fb144) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb148`](#insn-009fb148) → `2e393230676d0000`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb148`](#insn-009fb148) → `Stack[-0x188]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb154`](#insn-009fb154) → `00c8ad20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fb154`](#insn-009fb154) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb17c`](#insn-009fb17c) → [`008b6fec`](../008b6/008b6fec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6fec` · 推定シンボル `None` · 推定型 `None`
- [`009fb180`](#insn-009fb180) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb188`](#insn-009fb188) → [`009fb198`](#insn-009fb198) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb18c`](#insn-009fb18c) → [`009fb1ac`](#insn-009fb1ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb194`](#insn-009fb194) → [`009fb1a0`](#insn-009fb1a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb1a0`](#insn-009fb1a0) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb1a4`](#insn-009fb1a4) → `00c8ad40`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`009fb1a4`](#insn-009fb1a4) → `00c8ad48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fb1a8`](#insn-009fb1a8) → [`00a026fc`](../00a02/00a026fc.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00a026fc` · 推定シンボル `None` · 推定型 `None`
- [`009fb1a8`](#insn-009fb1a8) → [`00a02700`](../00a02/00a02700.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00a02700` · 推定シンボル `None` · 推定型 `None`
- [`009fb1ac`](#insn-009fb1ac) → `Stack[-0x188]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb1b0`](#insn-009fb1b0) → `Stack[-0x188]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb1b4`](#insn-009fb1b4) → [`009fb1d0`](#insn-009fb1d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb1c0`](#insn-009fb1c0) → `2e393230676d0000`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb1c0`](#insn-009fb1c0) → `00c8b758`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fb1c4`](#insn-009fb1c4) → [`005d8bc8`](../005d8/005d8bc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d8bc8` · 推定シンボル `None` · 推定型 `None`
- [`009fb1c8`](#insn-009fb1c8) → `2e393230676d0000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb1cc`](#insn-009fb1cc) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`009fb1d0`](#insn-009fb1d0) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb1d4`](#insn-009fb1d4) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb1d8`](#insn-009fb1d8) → [`009fb22c`](#insn-009fb22c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb1e4`](#insn-009fb1e4) → `00c8b7b0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fb1e8`](#insn-009fb1e8) → [`009fb214`](#insn-009fb214) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb1f4`](#insn-009fb1f4) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`009fb1f8`](#insn-009fb1f8) → [`009fb214`](#insn-009fb214) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb210`](#insn-009fb210) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`009fb21c`](#insn-009fb21c) → `00c8b758`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fb220`](#insn-009fb220) → [`005d8bc8`](../005d8/005d8bc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d8bc8` · 推定シンボル `None` · 推定型 `None`
- [`009fb228`](#insn-009fb228) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`009fb230`](#insn-009fb230) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb238`](#insn-009fb238) → [`009fb448`](#insn-009fb448) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb23c`](#insn-009fb23c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb240`](#insn-009fb240) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb244`](#insn-009fb244) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb248`](#insn-009fb248) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb24c`](#insn-009fb24c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb250`](#insn-009fb250) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb254`](#insn-009fb254) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb274`](#insn-009fb274) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`009fb278`](#insn-009fb278) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb27c`](#insn-009fb27c) → [`009fad6c`](#insn-009fad6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb280`](#insn-009fb280) → [`009fad7c`](#insn-009fad7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb298`](#insn-009fb298) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`009fb29c`](#insn-009fb29c) → `Stack[-0x188]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb2a0`](#insn-009fb2a0) → [`009fad84`](#insn-009fad84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb2a4`](#insn-009fb2a4) → [`009fad8c`](#insn-009fad8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb2ac`](#insn-009fb2ac) → `00ca4f38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`009fb2b0`](#insn-009fb2b0) → [`00c57e50`](../00c57/00c57e50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e50` · 推定シンボル `None` · 推定型 `None`
- [`009fb2b4`](#insn-009fb2b4) → [`009facdc`](#insn-009facdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb2bc`](#insn-009fb2bc) → `00ca4f00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009fb2c4`](#insn-009fb2c4) → [`0047edb4`](../0047e/0047edb4.md) · `PARAM` · `ANALYSIS` · 関数 `0047edb4` · 推定シンボル `None` · 推定型 `None`
- [`009fb2d0`](#insn-009fb2d0) → `00c62f90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`009fb2d4`](#insn-009fb2d4) → `00ca4f08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009fb2d8`](#insn-009fb2d8) → `00ca4f00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009fb2d8`](#insn-009fb2d8) → `00ca4f08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009fb2e0`](#insn-009fb2e0) → `00ca4f28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009fb2e0`](#insn-009fb2e0) → `00ca4f30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009fb2e4`](#insn-009fb2e4) → `00ca4f20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009fb2e8`](#insn-009fb2e8) → `00ca4f10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009fb2e8`](#insn-009fb2e8) → `00ca4f18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009fb2e8`](#insn-009fb2e8) → `00ca4f20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009fb2ec`](#insn-009fb2ec) → [`00c57e30`](../00c57/00c57e30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e30` · 推定シンボル `None` · 推定型 `None`
- [`009fb2f4`](#insn-009fb2f4) → `00ca4f38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`009fb2f8`](#insn-009fb2f8) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`009fb2fc`](#insn-009fb2fc) → [`009facdc`](#insn-009facdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fb448`](#insn-009fb448) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009fabd0`](#insn-009fabd0)

~~~json
{
  "source": "009fabd0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fabd4`](#insn-009fabd4)

~~~json
{
  "source": "009fabd4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fabd8`](#insn-009fabd8)

~~~json
{
  "source": "009fabd8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fabdc`](#insn-009fabdc)

~~~json
{
  "source": "009fabdc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fabe0`](#insn-009fabe0)

~~~json
{
  "source": "009fabe0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fabe4`](#insn-009fabe4)

~~~json
{
  "source": "009fabe4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fabe8`](#insn-009fabe8)

~~~json
{
  "source": "009fabe8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fabfc`](#insn-009fabfc)

~~~json
{
  "source": "009fabfc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fac04`](#insn-009fac04)

~~~json
{
  "source": "009fac04",
  "target": "00ca4978",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4978",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fac08`](#insn-009fac08)

~~~json
{
  "source": "009fac08",
  "target": "009fac30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fac10`](#insn-009fac10)

~~~json
{
  "source": "009fac10",
  "target": "00c65e58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c65e58",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fac18`](#insn-009fac18)

~~~json
{
  "source": "009fac18",
  "target": "00c71990",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c71990",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fac24`](#insn-009fac24)

~~~json
{
  "source": "009fac24",
  "target": "00c58610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fac2c`](#insn-009fac2c)

~~~json
{
  "source": "009fac2c",
  "target": "009fac34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fac34`](#insn-009fac34)

~~~json
{
  "source": "009fac34",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fac44`](#insn-009fac44)

~~~json
{
  "source": "009fac44",
  "target": "00a83260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fac48`](#insn-009fac48)

~~~json
{
  "source": "009fac48",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fac54`](#insn-009fac54)

~~~json
{
  "source": "009fac54",
  "target": "00a83260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fac58`](#insn-009fac58)

~~~json
{
  "source": "009fac58",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fac64`](#insn-009fac64)

~~~json
{
  "source": "009fac64",
  "target": "009f92c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fac7c`](#insn-009fac7c)

~~~json
{
  "source": "009fac7c",
  "target": "00a8344c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fac80`](#insn-009fac80)

~~~json
{
  "source": "009fac80",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fac84`](#insn-009fac84)

~~~json
{
  "source": "009fac84",
  "target": "009fac90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fac88`](#insn-009fac88)

~~~json
{
  "source": "009fac88",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fac8c`](#insn-009fac8c)

~~~json
{
  "source": "009fac8c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fac90`](#insn-009fac90)

~~~json
{
  "source": "009fac90",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009faca0`](#insn-009faca0)

~~~json
{
  "source": "009faca0",
  "target": "009f981c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009facb8`](#insn-009facb8)

~~~json
{
  "source": "009facb8",
  "target": "00a8344c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009facbc`](#insn-009facbc)

~~~json
{
  "source": "009facbc",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009facc0`](#insn-009facc0)

~~~json
{
  "source": "009facc0",
  "target": "009faccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009facc4`](#insn-009facc4)

~~~json
{
  "source": "009facc4",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009facc8`](#insn-009facc8)

~~~json
{
  "source": "009facc8",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009facd4`](#insn-009facd4)

~~~json
{
  "source": "009facd4",
  "target": "00ca4f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009facd8`](#insn-009facd8)

~~~json
{
  "source": "009facd8",
  "target": "009fb2a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009face4`](#insn-009face4)

~~~json
{
  "source": "009face4",
  "target": "Stack[-0x14d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009face8`](#insn-009face8)

~~~json
{
  "source": "009face8",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009facf4`](#insn-009facf4)

~~~json
{
  "source": "009facf4",
  "target": "002b3ea9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b3ea9",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "696d673032392e706e6700",
  "capture_start": "002b3ea9",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009facf8`](#insn-009facf8)

~~~json
{
  "source": "009facf8",
  "target": "Stack[-0x14f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fad00`](#insn-009fad00)

~~~json
{
  "source": "009fad00",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fad04`](#insn-009fad04)

~~~json
{
  "source": "009fad04",
  "target": "Stack[-0x157]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fad10`](#insn-009fad10)

~~~json
{
  "source": "009fad10",
  "target": "002b9270",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fad14`](#insn-009fad14)

~~~json
{
  "source": "009fad14",
  "target": "002b9275",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b9275",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "392e696d6763757400",
  "capture_start": "002b9275",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009fad18`](#insn-009fad18)

~~~json
{
  "source": "009fad18",
  "target": "Stack[-0x17a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fad1c`](#insn-009fad1c)

~~~json
{
  "source": "009fad1c",
  "target": "Stack[-0x187]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fad20`](#insn-009fad20)

~~~json
{
  "source": "009fad20",
  "target": "Stack[-0x182]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fad28`](#insn-009fad28)

~~~json
{
  "source": "009fad28",
  "target": "00ca4f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fad3c`](#insn-009fad3c)

~~~json
{
  "source": "009fad3c",
  "target": "0047e60c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fad40`](#insn-009fad40)

~~~json
{
  "source": "009fad40",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fad48`](#insn-009fad48)

~~~json
{
  "source": "009fad48",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fad50`](#insn-009fad50)

~~~json
{
  "source": "009fad50",
  "target": "009fad64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fad5c`](#insn-009fad5c)

~~~json
{
  "source": "009fad5c",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fad60`](#insn-009fad60)

~~~json
{
  "source": "009fad60",
  "target": "009fb260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fad64`](#insn-009fad64)

~~~json
{
  "source": "009fad64",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fad68`](#insn-009fad68)

~~~json
{
  "source": "009fad68",
  "target": "009fad7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fad74`](#insn-009fad74)

~~~json
{
  "source": "009fad74",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fad78`](#insn-009fad78)

~~~json
{
  "source": "009fad78",
  "target": "009fb284",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fad7c`](#insn-009fad7c)

~~~json
{
  "source": "009fad7c",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fad80`](#insn-009fad80)

~~~json
{
  "source": "009fad80",
  "target": "009fad8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fad84`](#insn-009fad84)

~~~json
{
  "source": "009fad84",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fad88`](#insn-009fad88)

~~~json
{
  "source": "009fad88",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fad8c`](#insn-009fad8c)

~~~json
{
  "source": "009fad8c",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fad90`](#insn-009fad90)

~~~json
{
  "source": "009fad90",
  "target": "009fad9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fad94`](#insn-009fad94)

~~~json
{
  "source": "009fad94",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fad98`](#insn-009fad98)

~~~json
{
  "source": "009fad98",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fad9c`](#insn-009fad9c)

~~~json
{
  "source": "009fad9c",
  "target": "009f7478",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fada0`](#insn-009fada0)

~~~json
{
  "source": "009fada0",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fadb0`](#insn-009fadb0)

~~~json
{
  "source": "009fadb0",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fadb4`](#insn-009fadb4)

~~~json
{
  "source": "009fadb4",
  "target": "00c8aba0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8aba0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fadb4`](#insn-009fadb4)

~~~json
{
  "source": "009fadb4",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fadbc`](#insn-009fadbc)

~~~json
{
  "source": "009fadbc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fadd8`](#insn-009fadd8)

~~~json
{
  "source": "009fadd8",
  "target": "008ba868",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fadf4`](#insn-009fadf4)

~~~json
{
  "source": "009fadf4",
  "target": "0046daf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fadf8`](#insn-009fadf8)

~~~json
{
  "source": "009fadf8",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fae00`](#insn-009fae00)

~~~json
{
  "source": "009fae00",
  "target": "008b9500",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fae08`](#insn-009fae08)

~~~json
{
  "source": "009fae08",
  "target": "008b9858",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fae10`](#insn-009fae10)

~~~json
{
  "source": "009fae10",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fae1c`](#insn-009fae1c)

~~~json
{
  "source": "009fae1c",
  "target": "009fae2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fae20`](#insn-009fae20)

~~~json
{
  "source": "009fae20",
  "target": "009fae40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fae28`](#insn-009fae28)

~~~json
{
  "source": "009fae28",
  "target": "009fae34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fae34`](#insn-009fae34)

~~~json
{
  "source": "009fae34",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fae38`](#insn-009fae38)

~~~json
{
  "source": "009fae38",
  "target": "00c8abc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8abc0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fae38`](#insn-009fae38)

~~~json
{
  "source": "009fae38",
  "target": "00c8abc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8abc8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fae3c`](#insn-009fae3c)

~~~json
{
  "source": "009fae3c",
  "target": "00a013a8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fae3c`](#insn-009fae3c)

~~~json
{
  "source": "009fae3c",
  "target": "00a013ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fae40`](#insn-009fae40)

~~~json
{
  "source": "009fae40",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fae44`](#insn-009fae44)

~~~json
{
  "source": "009fae44",
  "target": "009fae50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fae48`](#insn-009fae48)

~~~json
{
  "source": "009fae48",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fae4c`](#insn-009fae4c)

~~~json
{
  "source": "009fae4c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fae50`](#insn-009fae50)

~~~json
{
  "source": "009fae50",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fae60`](#insn-009fae60)

~~~json
{
  "source": "009fae60",
  "target": "00a829d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fae9c`](#insn-009fae9c)

~~~json
{
  "source": "009fae9c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009faea8`](#insn-009faea8)

~~~json
{
  "source": "009faea8",
  "target": "00a829d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009faec8`](#insn-009faec8)

~~~json
{
  "source": "009faec8",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009faed8`](#insn-009faed8)

~~~json
{
  "source": "009faed8",
  "target": "009e2f94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009faefc`](#insn-009faefc)

~~~json
{
  "source": "009faefc",
  "target": "008b9298",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009faf14`](#insn-009faf14)

~~~json
{
  "source": "009faf14",
  "target": "009faf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009faf1c`](#insn-009faf1c)

~~~json
{
  "source": "009faf1c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009faf4c`](#insn-009faf4c)

~~~json
{
  "source": "009faf4c",
  "target": "00ac8e10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009faf54`](#insn-009faf54)

~~~json
{
  "source": "009faf54",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009faf60`](#insn-009faf60)

~~~json
{
  "source": "009faf60",
  "target": "00337f64",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00337f60",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "34b77d00546b0a00",
  "capture_start": "00337f60",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009faf64`](#insn-009faf64)

~~~json
{
  "source": "009faf64",
  "target": "009faf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009faf68`](#insn-009faf68)

~~~json
{
  "source": "009faf68",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009faf74`](#insn-009faf74)

~~~json
{
  "source": "009faf74",
  "target": "00ac8e54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009faf7c`](#insn-009faf7c)

~~~json
{
  "source": "009faf7c",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009faf8c`](#insn-009faf8c)

~~~json
{
  "source": "009faf8c",
  "target": "00c8ac20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8ac20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009faf94`](#insn-009faf94)

~~~json
{
  "source": "009faf94",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fafa4`](#insn-009fafa4)

~~~json
{
  "source": "009fafa4",
  "target": "008b95cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fafa8`](#insn-009fafa8)

~~~json
{
  "source": "009fafa8",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fafb0`](#insn-009fafb0)

~~~json
{
  "source": "009fafb0",
  "target": "009fafc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fafb4`](#insn-009fafb4)

~~~json
{
  "source": "009fafb4",
  "target": "009fafd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fafbc`](#insn-009fafbc)

~~~json
{
  "source": "009fafbc",
  "target": "009fafc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fafc8`](#insn-009fafc8)

~~~json
{
  "source": "009fafc8",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fafcc`](#insn-009fafcc)

~~~json
{
  "source": "009fafcc",
  "target": "00c8ac48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8ac48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fafd0`](#insn-009fafd0)

~~~json
{
  "source": "009fafd0",
  "target": "00a014ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fafe0`](#insn-009fafe0)

~~~json
{
  "source": "009fafe0",
  "target": "00c8aca0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8aca0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fafe0`](#insn-009fafe0)

~~~json
{
  "source": "009fafe0",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fafe4`](#insn-009fafe4)

~~~json
{
  "source": "009fafe4",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fafe8`](#insn-009fafe8)

~~~json
{
  "source": "009fafe8",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009faff4`](#insn-009faff4)

~~~json
{
  "source": "009faff4",
  "target": "008b96a4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009faff8`](#insn-009faff8)

~~~json
{
  "source": "009faff8",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb000`](#insn-009fb000)

~~~json
{
  "source": "009fb000",
  "target": "009fb010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb004`](#insn-009fb004)

~~~json
{
  "source": "009fb004",
  "target": "009fb024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb00c`](#insn-009fb00c)

~~~json
{
  "source": "009fb00c",
  "target": "009fb018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb018`](#insn-009fb018)

~~~json
{
  "source": "009fb018",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb01c`](#insn-009fb01c)

~~~json
{
  "source": "009fb01c",
  "target": "00c8acc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8acc0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fb01c`](#insn-009fb01c)

~~~json
{
  "source": "009fb01c",
  "target": "00c8acc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8acc8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fb020`](#insn-009fb020)

~~~json
{
  "source": "009fb020",
  "target": "00a022d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb020`](#insn-009fb020)

~~~json
{
  "source": "009fb020",
  "target": "00a022d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb048`](#insn-009fb048)

~~~json
{
  "source": "009fb048",
  "target": "00a4754c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb04c`](#insn-009fb04c)

~~~json
{
  "source": "009fb04c",
  "target": "2e393230676d0000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb04c`](#insn-009fb04c)

~~~json
{
  "source": "009fb04c",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb050`](#insn-009fb050)

~~~json
{
  "source": "009fb050",
  "target": "2e393230676d0000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb060`](#insn-009fb060)

~~~json
{
  "source": "009fb060",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb078`](#insn-009fb078)

~~~json
{
  "source": "009fb078",
  "target": "00a468fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb07c`](#insn-009fb07c)

~~~json
{
  "source": "009fb07c",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb080`](#insn-009fb080)

~~~json
{
  "source": "009fb080",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb084`](#insn-009fb084)

~~~json
{
  "source": "009fb084",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb08c`](#insn-009fb08c)

~~~json
{
  "source": "009fb08c",
  "target": "2e393230676d0000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb090`](#insn-009fb090)

~~~json
{
  "source": "009fb090",
  "target": "00a46784",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb0a8`](#insn-009fb0a8)

~~~json
{
  "source": "009fb0a8",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb0ac`](#insn-009fb0ac)

~~~json
{
  "source": "009fb0ac",
  "target": "00c9b368",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b368",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fb0b0`](#insn-009fb0b0)

~~~json
{
  "source": "009fb0b0",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb0b4`](#insn-009fb0b4)

~~~json
{
  "source": "009fb0b4",
  "target": "009fb0d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb0c0`](#insn-009fb0c0)

~~~json
{
  "source": "009fb0c0",
  "target": "00c8b758",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b758",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fb0c4`](#insn-009fb0c4)

~~~json
{
  "source": "009fb0c4",
  "target": "005d8bc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb0cc`](#insn-009fb0cc)

~~~json
{
  "source": "009fb0cc",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb0d4`](#insn-009fb0d4)

~~~json
{
  "source": "009fb0d4",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb0d8`](#insn-009fb0d8)

~~~json
{
  "source": "009fb0d8",
  "target": "00c9b370",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b370",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fb0dc`](#insn-009fb0dc)

~~~json
{
  "source": "009fb0dc",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb0e0`](#insn-009fb0e0)

~~~json
{
  "source": "009fb0e0",
  "target": "009fb134",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb0ec`](#insn-009fb0ec)

~~~json
{
  "source": "009fb0ec",
  "target": "00c8b7b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b7b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fb0f0`](#insn-009fb0f0)

~~~json
{
  "source": "009fb0f0",
  "target": "009fb11c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb0fc`](#insn-009fb0fc)

~~~json
{
  "source": "009fb0fc",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb100`](#insn-009fb100)

~~~json
{
  "source": "009fb100",
  "target": "009fb11c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb118`](#insn-009fb118)

~~~json
{
  "source": "009fb118",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb124`](#insn-009fb124)

~~~json
{
  "source": "009fb124",
  "target": "00c8b758",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b758",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fb128`](#insn-009fb128)

~~~json
{
  "source": "009fb128",
  "target": "005d8bc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb130`](#insn-009fb130)

~~~json
{
  "source": "009fb130",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb134`](#insn-009fb134)

~~~json
{
  "source": "009fb134",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb138`](#insn-009fb138)

~~~json
{
  "source": "009fb138",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb140`](#insn-009fb140)

~~~json
{
  "source": "009fb140",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb144`](#insn-009fb144)

~~~json
{
  "source": "009fb144",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb148`](#insn-009fb148)

~~~json
{
  "source": "009fb148",
  "target": "2e393230676d0000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb148`](#insn-009fb148)

~~~json
{
  "source": "009fb148",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb154`](#insn-009fb154)

~~~json
{
  "source": "009fb154",
  "target": "00c8ad20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8ad20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fb154`](#insn-009fb154)

~~~json
{
  "source": "009fb154",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb17c`](#insn-009fb17c)

~~~json
{
  "source": "009fb17c",
  "target": "008b6fec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb180`](#insn-009fb180)

~~~json
{
  "source": "009fb180",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb188`](#insn-009fb188)

~~~json
{
  "source": "009fb188",
  "target": "009fb198",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb18c`](#insn-009fb18c)

~~~json
{
  "source": "009fb18c",
  "target": "009fb1ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb194`](#insn-009fb194)

~~~json
{
  "source": "009fb194",
  "target": "009fb1a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb1a0`](#insn-009fb1a0)

~~~json
{
  "source": "009fb1a0",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb1a4`](#insn-009fb1a4)

~~~json
{
  "source": "009fb1a4",
  "target": "00c8ad40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8ad40",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fb1a4`](#insn-009fb1a4)

~~~json
{
  "source": "009fb1a4",
  "target": "00c8ad48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8ad48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fb1a8`](#insn-009fb1a8)

~~~json
{
  "source": "009fb1a8",
  "target": "00a026fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb1a8`](#insn-009fb1a8)

~~~json
{
  "source": "009fb1a8",
  "target": "00a02700",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb1ac`](#insn-009fb1ac)

~~~json
{
  "source": "009fb1ac",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb1b0`](#insn-009fb1b0)

~~~json
{
  "source": "009fb1b0",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb1b4`](#insn-009fb1b4)

~~~json
{
  "source": "009fb1b4",
  "target": "009fb1d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb1c0`](#insn-009fb1c0)

~~~json
{
  "source": "009fb1c0",
  "target": "2e393230676d0000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb1c0`](#insn-009fb1c0)

~~~json
{
  "source": "009fb1c0",
  "target": "00c8b758",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b758",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fb1c4`](#insn-009fb1c4)

~~~json
{
  "source": "009fb1c4",
  "target": "005d8bc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb1c8`](#insn-009fb1c8)

~~~json
{
  "source": "009fb1c8",
  "target": "2e393230676d0000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb1cc`](#insn-009fb1cc)

~~~json
{
  "source": "009fb1cc",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb1d0`](#insn-009fb1d0)

~~~json
{
  "source": "009fb1d0",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb1d4`](#insn-009fb1d4)

~~~json
{
  "source": "009fb1d4",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb1d8`](#insn-009fb1d8)

~~~json
{
  "source": "009fb1d8",
  "target": "009fb22c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb1e4`](#insn-009fb1e4)

~~~json
{
  "source": "009fb1e4",
  "target": "00c8b7b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b7b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fb1e8`](#insn-009fb1e8)

~~~json
{
  "source": "009fb1e8",
  "target": "009fb214",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb1f4`](#insn-009fb1f4)

~~~json
{
  "source": "009fb1f4",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb1f8`](#insn-009fb1f8)

~~~json
{
  "source": "009fb1f8",
  "target": "009fb214",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb210`](#insn-009fb210)

~~~json
{
  "source": "009fb210",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb21c`](#insn-009fb21c)

~~~json
{
  "source": "009fb21c",
  "target": "00c8b758",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b758",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fb220`](#insn-009fb220)

~~~json
{
  "source": "009fb220",
  "target": "005d8bc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb228`](#insn-009fb228)

~~~json
{
  "source": "009fb228",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb230`](#insn-009fb230)

~~~json
{
  "source": "009fb230",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb238`](#insn-009fb238)

~~~json
{
  "source": "009fb238",
  "target": "009fb448",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb23c`](#insn-009fb23c)

~~~json
{
  "source": "009fb23c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb240`](#insn-009fb240)

~~~json
{
  "source": "009fb240",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb244`](#insn-009fb244)

~~~json
{
  "source": "009fb244",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb248`](#insn-009fb248)

~~~json
{
  "source": "009fb248",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb24c`](#insn-009fb24c)

~~~json
{
  "source": "009fb24c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb250`](#insn-009fb250)

~~~json
{
  "source": "009fb250",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb254`](#insn-009fb254)

~~~json
{
  "source": "009fb254",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb274`](#insn-009fb274)

~~~json
{
  "source": "009fb274",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb278`](#insn-009fb278)

~~~json
{
  "source": "009fb278",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb27c`](#insn-009fb27c)

~~~json
{
  "source": "009fb27c",
  "target": "009fad6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb280`](#insn-009fb280)

~~~json
{
  "source": "009fb280",
  "target": "009fad7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb298`](#insn-009fb298)

~~~json
{
  "source": "009fb298",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb29c`](#insn-009fb29c)

~~~json
{
  "source": "009fb29c",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb2a0`](#insn-009fb2a0)

~~~json
{
  "source": "009fb2a0",
  "target": "009fad84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb2a4`](#insn-009fb2a4)

~~~json
{
  "source": "009fb2a4",
  "target": "009fad8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb2ac`](#insn-009fb2ac)

~~~json
{
  "source": "009fb2ac",
  "target": "00ca4f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fb2b0`](#insn-009fb2b0)

~~~json
{
  "source": "009fb2b0",
  "target": "00c57e50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb2b4`](#insn-009fb2b4)

~~~json
{
  "source": "009fb2b4",
  "target": "009facdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb2bc`](#insn-009fb2bc)

~~~json
{
  "source": "009fb2bc",
  "target": "00ca4f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fb2c4`](#insn-009fb2c4)

~~~json
{
  "source": "009fb2c4",
  "target": "0047edb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb2d0`](#insn-009fb2d0)

~~~json
{
  "source": "009fb2d0",
  "target": "00c62f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c62f90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fb2d4`](#insn-009fb2d4)

~~~json
{
  "source": "009fb2d4",
  "target": "00ca4f08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fb2d8`](#insn-009fb2d8)

~~~json
{
  "source": "009fb2d8",
  "target": "00ca4f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fb2d8`](#insn-009fb2d8)

~~~json
{
  "source": "009fb2d8",
  "target": "00ca4f08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fb2e0`](#insn-009fb2e0)

~~~json
{
  "source": "009fb2e0",
  "target": "00ca4f28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fb2e0`](#insn-009fb2e0)

~~~json
{
  "source": "009fb2e0",
  "target": "00ca4f30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fb2e4`](#insn-009fb2e4)

~~~json
{
  "source": "009fb2e4",
  "target": "00ca4f20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fb2e8`](#insn-009fb2e8)

~~~json
{
  "source": "009fb2e8",
  "target": "00ca4f10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fb2e8`](#insn-009fb2e8)

~~~json
{
  "source": "009fb2e8",
  "target": "00ca4f18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fb2e8`](#insn-009fb2e8)

~~~json
{
  "source": "009fb2e8",
  "target": "00ca4f20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fb2ec`](#insn-009fb2ec)

~~~json
{
  "source": "009fb2ec",
  "target": "00c57e30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb2f4`](#insn-009fb2f4)

~~~json
{
  "source": "009fb2f4",
  "target": "00ca4f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`009fb2f8`](#insn-009fb2f8)

~~~json
{
  "source": "009fb2f8",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fb2fc`](#insn-009fb2fc)

~~~json
{
  "source": "009fb2fc",
  "target": "009facdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fb448`](#insn-009fb448)

~~~json
{
  "source": "009fb448",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
