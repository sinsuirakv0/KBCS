# 00adccd8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00adcbcc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adc/00adcbcc.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00adccd8",
  "name": "FUN_00adccd8",
  "size": 1448,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7a39cc9fd27b0d34aa56a95f69ad5a7106290940f2ac5fad8234b464ef6198d9",
  "source_text_sha256": "7a39cc9fd27b0d34aa56a95f69ad5a7106290940f2ac5fad8234b464ef6198d9"
}
~~~

## 呼び出し元

- [0064b18c](../0064b/0064b18c.md)
- [00654084](../00654/00654084.md)
- [00829478](../00829/00829478.md)
- [0089d9f4](../0089d/0089d9f4.md)
- [008f2388](../008f2/008f2388.md)
- [0098b984](../0098b/0098b984.md)
- [00a04c2c](../00a04/00a04c2c.md)
- [00acddbc](../00acd/00acddbc.md)

## 呼び出し先

- [0045b734](../0045b/0045b734.md)
- [0045ba04](../0045b/0045ba04.md)
- [00469f7c](../00469/00469f7c.md)
- [007f8ecc](../007f8/007f8ecc.md)
- [0081f580](../0081f/0081f580.md)
- [00821cb4](../00821/00821cb4.md)
- [008321a8](../00832/008321a8.md)
- [00a618f4](../00a61/00a618f4.md)
- [00bd6e90](../00bd6/00bd6e90.md)
- [00bdafe0](../00bda/00bdafe0.md)
- [00bdb000](../00bdb/00bdb000.md)
- [00bdb020](../00bdb/00bdb020.md)
- [00bdb030](../00bdb/00bdb030.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)

## 関連文字列（未確認候補）

~~~text
"1.imgcut"
"5.imgcut"
"img005.imgcut"
"img005.png"
"img005_1.imgcut"
"img005_1.png"
"unlockpopup_Guide_1"
~~~

## 疑似コード / UTF-8 8866 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */
/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00adccd8(undefined8 *param_1,undefined8 param_2)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  int iVar4;
  long lVar5;
  long *plVar6;
  long *plVar7;
  byte local_b8;
  undefined5 local_b7;
  undefined2 uStack_b2;
  char cStack_b0;
  undefined5 uStack_af;
  char cStack_aa;
  char cStack_a9;
  uint uStack_a8;
  uint uStack_a4;
  byte local_a0;
  undefined7 uStack_9f;
  char cStack_98;
  undefined2 uStack_97;
  undefined1 uStack_95;
  undefined1 uStack_94;
  undefined1 uStack_93;
  undefined2 uStack_92;
  void *local_90;
  undefined8 local_80;
  long *plStack_78;
  long local_68;
  
  lVar1 = tpidr_el0;
  local_68 = *(long *)(lVar1 + 0x28);
  *param_1 = &PTR_FUN_00bf7158;
  param_1[2] = 0;
  param_1[1] = 0;
  param_1[4] = 0;
  param_1[3] = 0;
  param_1[6] = 0;
  param_1[5] = 0;
  param_1[8] = 0;
  param_1[7] = 0;
  param_1[10] = 0;
  param_1[9] = 0;
  param_1[0xc] = 0;
  param_1[0xb] = 0;
  param_1[0xe] = 0;
  param_1[0xd] = 0;
  param_1[0x10] = 0;
  param_1[0xf] = 0;
  param_1[0x12] = 0;
  param_1[0x11] = 0;
  param_1[0x14] = 0;
  param_1[0x13] = 0;
  if (((DAT_00c25078 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00c25078), iVar4 != 0)) {
    DAT_00c25048 = 0;
    DAT_00c25040 = &DAT_00c25048;
    DAT_00c25068 = 0;
    DAT_00c25070 = 0;
    DAT_00c25060 = 0;
    DAT_00c25050 = 0;
    DAT_00c25058 = &DAT_00c25060;
    __cxa_atexit(FUN_0045bedc,&DAT_00c25040,&PTR_LOOP_00be5fd0);
    __cxa_guard_release(&DAT_00c25078);
  }
  uStack_95 = 0;
  local_a0 = 0x14;
  uStack_97 = 0x676e;
  local_b8 = 0x1a;
  uStack_9f = (undefined7)s_img005_png_002a9f34._0_8_;
  cStack_98 = SUB81(s_img005_png_002a9f34._0_8_,7);
  cStack_aa = 0;
  local_b7 = _DAT_0029ff5c;
  uStack_b2 = (undefined2)s_5_imgcut_0029ff61._0_3_;
  cStack_b0 = SUB31(s_5_imgcut_0029ff61._0_3_,2);
  uStack_af._0_1_ = s_5_imgcut_0029ff61[3];
  uStack_af._1_1_ = s_5_imgcut_0029ff61[4];
  uStack_af._2_1_ = s_5_imgcut_0029ff61[5];
  uStack_af._3_1_ = s_5_imgcut_0029ff61[6];
  uStack_af._4_1_ = s_5_imgcut_0029ff61[7];
  FUN_0045b734(&local_80,&DAT_00c25040,&local_a0,&local_b8,0x2601);
  plVar6 = plStack_78;
  uVar2 = local_80;
  plVar7 = (long *)param_1[2];
  local_80 = 0;
  plStack_78 = (long *)0x0;
  param_1[2] = plVar6;
  param_1[1] = uVar2;
  plVar6 = plStack_78;
  if ((plVar7 != (long *)0x0) &&
     (lVar5 = FUN_00bd6e90(0xffffffffffffffff,plVar7 + 1), plVar6 = plStack_78, lVar5 == 0)) {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
    plVar6 = plStack_78;
  }
  plStack_78 = plVar6;
  if ((plVar6 != (long *)0x0) &&
     (lVar5 = FUN_00bd6e90(0xffffffffffffffff,(long *)((long)plVar6 + 8)), lVar5 == 0)) {
    (**(code **)(*plVar6 + 0x10))(plVar6);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
  }
  if ((local_b8 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_a4,uStack_a8));
  }
  if ((local_a0 & 1) != 0) {
    _ZdlPv(local_90);
  }
  if (((DAT_00c25078 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00c25078), iVar4 != 0)) {
    DAT_00c25048 = 0;
    DAT_00c25040 = &DAT_00c25048;
    DAT_00c25068 = 0;
    DAT_00c25070 = 0;
    DAT_00c25060 = 0;
    DAT_00c25050 = 0;
    DAT_00c25058 = &DAT_00c25060;
    __cxa_atexit(FUN_0045bedc,&DAT_00c25040,&PTR_LOOP_00be5fd0);
    __cxa_guard_release(&DAT_00c25078);
  }
  uStack_93 = 0;
  local_a0 = 0x18;
  uStack_a8 = uStack_a8 & 0xffffff00;
  uStack_97 = 0x702e;
  uStack_95 = 0x6e;
  uStack_94 = 0x67;
  uStack_9f = (undefined7)s_img005_1_png_002973f7._0_8_;
  cStack_98 = SUB81(s_img005_1_png_002973f7._0_8_,7);
  local_b8 = 0x1e;
  local_b7 = (undefined5)_DAT_002ad230;
  uStack_b2 = (undefined2)((uint7)_DAT_002ad230 >> 0x28);
  cStack_b0 = s_1_imgcut_002ad237[0];
  uStack_af = (undefined5)s_1_imgcut_002ad237._1_7_;
  cStack_aa = SUB71(s_1_imgcut_002ad237._1_7_,5);
  cStack_a9 = SUB71(s_1_imgcut_002ad237._1_7_,6);
  FUN_0045b734(&local_80,&DAT_00c25040,&local_a0,&local_b8,0x2601);
  plVar6 = plStack_78;
  uVar2 = local_80;
  plVar7 = (long *)param_1[4];
  local_80 = 0;
  plStack_78 = (long *)0x0;
  param_1[4] = plVar6;
  param_1[3] = uVar2;
  plVar6 = plStack_78;
  if ((plVar7 != (long *)0x0) &&
     (lVar5 = FUN_00bd6e90(0xffffffffffffffff,plVar7 + 1), plVar6 = plStack_78, lVar5 == 0)) {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
    plVar6 = plStack_78;
  }
  plStack_78 = plVar6;
                    /* try { // try from 00adcf24 to 00bdd0bf has its CatchHandler @ 00adcf24
                       catch() { ... } // from try @ 00adcf24 with catch @ 00adcf24
                       catch() { ... } // from try @ 00add0c8 with catch @ 00adcf24 */
  if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00bd6e90(0xffffffffffffffff,plVar6 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar6 + 0x10))(plVar6);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
  }
  if ((local_b8 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_a4,uStack_a8));
  }
  if ((local_a0 & 1) != 0) {
    _ZdlPv(local_90);
  }
  iVar4 = FUN_00821cb4(param_2);
  if (iVar4 != 0x61) {
    FUN_008321a8(&local_a0,param_2);
    uVar3 = CONCAT26(uStack_92,
                     CONCAT15(uStack_93,
                              CONCAT14(uStack_94,CONCAT13(uStack_95,CONCAT21(uStack_97,cStack_98))))
                    );
    uVar2 = CONCAT71(uStack_9f,local_a0);
    plVar6 = (long *)param_1[6];
    local_a0 = 0;
    uStack_9f = 0;
    cStack_98 = '\0';
    uStack_97 = 0;
    uStack_95 = 0;
    uStack_94 = 0;
    uStack_93 = 0;
    uStack_92 = 0;
    param_1[6] = uVar3;
    param_1[5] = uVar2;
    if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00bd6e90(0xffffffffffffffff,plVar6 + 1), lVar5 == 0)
       ) {
      (**(code **)(*plVar6 + 0x10))(plVar6);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
    }
    plVar6 = (long *)CONCAT26(uStack_92,
                              CONCAT15(uStack_93,
                                       CONCAT14(uStack_94,
                                                CONCAT13(uStack_95,CONCAT21(uStack_97,cStack_98)))))
    ;
    if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00bd6e90(0xffffffffffffffff,plVar6 + 1), lVar5 == 0)
       ) {
      (**(code **)(*plVar6 + 0x10))(plVar6);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
    }
  }
  if (((DAT_00c25078 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00c25078), iVar4 != 0)) {
    DAT_00c25048 = 0;
    DAT_00c25040 = &DAT_00c25048;
    DAT_00c25068 = 0;
    DAT_00c25070 = 0;
    DAT_00c25060 = 0;
    DAT_00c25050 = 0;
    DAT_00c25058 = &DAT_00c25060;
    __cxa_atexit(FUN_0045bedc,&DAT_00c25040,&PTR_LOOP_00be5fd0);
    __cxa_guard_release(&DAT_00c25078);
  }
  local_b8 = 0x26;
  uStack_af = (undefined5)s_unlockpopup_Guide_1_0029dd3c._8_8_;
  cStack_aa = SUB81(s_unlockpopup_Guide_1_0029dd3c._8_8_,5);
  cStack_a9 = SUB81(s_unlockpopup_Guide_1_0029dd3c._8_8_,6);
  uStack_a8 = CONCAT31(0x315f65,SUB81(s_unlockpopup_Guide_1_0029dd3c._8_8_,7));
  local_b7 = (undefined5)s_unlockpopup_Guide_1_0029dd3c._0_8_;
  uStack_b2 = SUB82(s_unlockpopup_Guide_1_0029dd3c._0_8_,5);
  cStack_b0 = SUB81(s_unlockpopup_Guide_1_0029dd3c._0_8_,7);
  uStack_a4 = uStack_a4 & 0xffffff00;
  FUN_00469f7c(&local_a0,&local_b8);
  FUN_0045ba04(&local_80,&DAT_00c25040,&local_a0,PTR_DAT_00c1aeb0,0x14,0,0,0);
  plVar6 = plStack_78;
  uVar2 = local_80;
  plVar7 = (long *)param_1[8];
  local_80 = 0;
  plStack_78 = (long *)0x0;
  param_1[8] = plVar6;
  param_1[7] = uVar2;
  plVar6 = plStack_78;
  if ((plVar7 != (long *)0x0) &&
     (lVar5 = FUN_00bd6e90(0xffffffffffffffff,plVar7 + 1), plVar6 = plStack_78, lVar5 == 0)) {
    (**(code **)(*plVar7 + 0x10))(plVar7);
                    /* catch() { ... } // from try @ 00add0c0 with catch @ 00add148 */
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
    plVar6 = plStack_78;
  }
  plStack_78 = plVar6;
  if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00bd6e90(0xffffffffffffffff,plVar6 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar6 + 0x10))(plVar6);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
  }
  if ((local_a0 & 1) != 0) {
    _ZdlPv(local_90);
  }
  if ((local_b8 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_a4,uStack_a8));
  }
  lVar5 = FUN_0081f580();
  FUN_00a618f4(lVar5 + 0x1998,param_1);
  lVar5 = FUN_0081f580();
  FUN_007f8ecc(lVar5 + 0x3339a8,param_1);
                    /* try { // try from 00add0c0 to 00bdd0c7 has its CatchHandler @ 00add148 */
                    /* try { // try from 00add0c8 to 00bdd173 has its CatchHandler @ 00adcf24 */
  if (*(long *)(lVar1 + 0x28) == local_68) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
