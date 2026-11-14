# 009fbbcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

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
  "source_text_sha256": "3beb7bc2f1b253d5e0384a49f1d83f6f35d15744e1a77c2c588c4a9f66a9cec1"
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
