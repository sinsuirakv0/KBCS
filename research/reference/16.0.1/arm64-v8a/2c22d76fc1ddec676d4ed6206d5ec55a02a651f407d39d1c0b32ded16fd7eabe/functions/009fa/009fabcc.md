# 009fabcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

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
  "source_text_sha256": "13a63fce7aade6e531f3896dce4fdb12cd7b4ecce762bdf6eb9a97e5c01d0dc4"
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
