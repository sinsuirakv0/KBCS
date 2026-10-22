# 00adcbcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00adcbcc.md)

## 関数情報

~~~json
{
  "address": "00adcbcc",
  "name": "FUN_00adcbcc",
  "size": 1448,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b77b608bc46b68014a4b0381900e22373e6b57a532ecccb0c5ef25b1f587bbbe",
  "source_text_sha256": "b77b608bc46b68014a4b0381900e22373e6b57a532ecccb0c5ef25b1f587bbbe"
}
~~~
## 呼び出し元

- [0064b18c](../0064b/0064b18c.md)
- [00654084](../00654/00654084.md)
- [00829478](../00829/00829478.md)
- [0089d9f4](../0089d/0089d9f4.md)
- [008f2388](../008f2/008f2388.md)
- [0098b984](../0098b/0098b984.md)
- [00a04be8](../00a04/00a04be8.md)
- [00acdcb0](../00acd/00acdcb0.md)

## 呼び出し先

- [0045b734](../0045b/0045b734.md)
- [0045ba04](../0045b/0045ba04.md)
- [00469f7c](../00469/00469f7c.md)
- [007f8ecc](../007f8/007f8ecc.md)
- [0081f580](../0081f/0081f580.md)
- [00821cb4](../00821/00821cb4.md)
- [008321a8](../00832/008321a8.md)
- [00a618b0](../00a61/00a618b0.md)
- [00bd6d90](../00bd6/00bd6d90.md)
- [00bdaee0](../00bda/00bdaee0.md)
- [00bdaf00](../00bda/00bdaf00.md)
- [00bdaf20](../00bda/00bdaf20.md)
- [00bdaf30](../00bda/00bdaf30.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

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
## 疑似コード 1/1 / UTF-8 9511 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */
/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00adcbcc(undefined8 *param_1,undefined8 param_2)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  int iVar4;
  long lVar5;
  __shared_weak_count *p_Var6;
  __shared_weak_count *p_Var7;
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
  __shared_weak_count *p_Stack_78;
  long local_68;
  
  lVar1 = tpidr_el0;
  local_68 = *(long *)(lVar1 + 0x28);
  *param_1 = &PTR_FUN_00bf7058;
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
                    /* try { // try from 00add07c to 00bdd083 has its CatchHandler @ 00add104 */
  if (((DAT_00c24f78 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00c24f78), iVar4 != 0)) {
                    /* try { // try from 00add084 to 00bdd12f has its CatchHandler @ 00adcee0 */
    DAT_00c24f48 = 0;
    DAT_00c24f40 = &DAT_00c24f48;
    DAT_00c24f68 = 0;
    DAT_00c24f70 = 0;
    DAT_00c24f60 = 0;
    DAT_00c24f50 = 0;
    DAT_00c24f58 = &DAT_00c24f60;
    __cxa_atexit(FUN_0045bedc,&DAT_00c24f40,&PTR_LOOP_00be5ed0);
    __cxa_guard_release(&DAT_00c24f78);
  }
  uStack_95 = 0;
  local_a0 = 0x14;
  uStack_97 = 0x676e;
  local_b8 = 0x1a;
  uStack_9f = (undefined7)s_img005_png_002a9f2e._0_8_;
  cStack_98 = SUB81(s_img005_png_002a9f2e._0_8_,7);
  cStack_aa = 0;
  local_b7 = _DAT_0029fe44;
  uStack_b2 = (undefined2)s_5_imgcut_0029fe49._0_3_;
  cStack_b0 = SUB31(s_5_imgcut_0029fe49._0_3_,2);
  uStack_af._0_1_ = s_5_imgcut_0029fe49[3];
  uStack_af._1_1_ = s_5_imgcut_0029fe49[4];
  uStack_af._2_1_ = s_5_imgcut_0029fe49[5];
  uStack_af._3_1_ = s_5_imgcut_0029fe49[6];
  uStack_af._4_1_ = s_5_imgcut_0029fe49[7];
  FUN_0045b734(&local_80,&DAT_00c24f40,&local_a0,&local_b8,0x2601);
  p_Var6 = p_Stack_78;
  uVar2 = local_80;
  p_Var7 = (__shared_weak_count *)param_1[2];
  local_80 = 0;
  p_Stack_78 = (__shared_weak_count *)0x0;
  param_1[2] = p_Var6;
  param_1[1] = uVar2;
  p_Var6 = p_Stack_78;
  if ((p_Var7 != (__shared_weak_count *)0x0) &&
     (lVar5 = FUN_00bd6d90(0xffffffffffffffff,p_Var7 + 8), p_Var6 = p_Stack_78, lVar5 == 0)) {
    (**(code **)(*(long *)p_Var7 + 0x10))(p_Var7);
    std::__ndk1::__shared_weak_count::__release_weak(p_Var7);
    p_Var6 = p_Stack_78;
  }
  p_Stack_78 = p_Var6;
  if ((p_Var6 != (__shared_weak_count *)0x0) &&
     (lVar5 = FUN_00bd6d90(0xffffffffffffffff,(__shared_weak_count *)((long)p_Var6 + 8)), lVar5 == 0
     )) {
    (**(code **)(*(long *)p_Var6 + 0x10))(p_Var6);
    std::__ndk1::__shared_weak_count::__release_weak(p_Var6);
  }
  if ((local_b8 & 1) != 0) {
    operator_delete((void *)CONCAT44(uStack_a4,uStack_a8));
  }
  if ((local_a0 & 1) != 0) {
    operator_delete(local_90);
  }
  if (((DAT_00c24f78 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00c24f78), iVar4 != 0)) {
    DAT_00c24f48 = 0;
    DAT_00c24f40 = &DAT_00c24f48;
    DAT_00c24f68 = 0;
    DAT_00c24f70 = 0;
    DAT_00c24f60 = 0;
                    /* catch() { ... } // from try @ 00add07c with catch @ 00add104 */
    DAT_00c24f50 = 0;
    DAT_00c24f58 = &DAT_00c24f60;
    __cxa_atexit(FUN_0045bedc,&DAT_00c24f40,&PTR_LOOP_00be5ed0);
    __cxa_guard_release(&DAT_00c24f78);
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
  local_b7 = (undefined5)_DAT_002ad239;
  uStack_b2 = (undefined2)((uint7)_DAT_002ad239 >> 0x28);
  cStack_b0 = s_1_imgcut_002ad240[0];
  uStack_af = (undefined5)s_1_imgcut_002ad240._1_7_;
  cStack_aa = SUB71(s_1_imgcut_002ad240._1_7_,5);
  cStack_a9 = SUB71(s_1_imgcut_002ad240._1_7_,6);
  FUN_0045b734(&local_80,&DAT_00c24f40,&local_a0,&local_b8,0x2601);
  p_Var6 = p_Stack_78;
  uVar2 = local_80;
  p_Var7 = (__shared_weak_count *)param_1[4];
  local_80 = 0;
  p_Stack_78 = (__shared_weak_count *)0x0;
  param_1[4] = p_Var6;
  param_1[3] = uVar2;
  p_Var6 = p_Stack_78;
  if ((p_Var7 != (__shared_weak_count *)0x0) &&
     (lVar5 = FUN_00bd6d90(0xffffffffffffffff,p_Var7 + 8), p_Var6 = p_Stack_78, lVar5 == 0)) {
    (**(code **)(*(long *)p_Var7 + 0x10))(p_Var7);
    std::__ndk1::__shared_weak_count::__release_weak(p_Var7);
    p_Var6 = p_Stack_78;
  }
  p_Stack_78 = p_Var6;
  if ((p_Var6 != (__shared_weak_count *)0x0) &&
     (lVar5 = FUN_00bd6d90(0xffffffffffffffff,p_Var6 + 8), lVar5 == 0)) {
    (**(code **)(*(long *)p_Var6 + 0x10))(p_Var6);
    std::__ndk1::__shared_weak_count::__release_weak(p_Var6);
  }
  if ((local_b8 & 1) != 0) {
    operator_delete((void *)CONCAT44(uStack_a4,uStack_a8));
  }
  if ((local_a0 & 1) != 0) {
    operator_delete(local_90);
  }
  iVar4 = FUN_00821cb4(param_2);
  if (iVar4 != 0x61) {
    FUN_008321a8(&local_a0,param_2);
    uVar3 = CONCAT26(uStack_92,
                     CONCAT15(uStack_93,
                              CONCAT14(uStack_94,CONCAT13(uStack_95,CONCAT21(uStack_97,cStack_98))))
                    );
    uVar2 = CONCAT71(uStack_9f,local_a0);
    p_Var6 = (__shared_weak_count *)param_1[6];
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
    if ((p_Var6 != (__shared_weak_count *)0x0) &&
       (lVar5 = FUN_00bd6d90(0xffffffffffffffff,p_Var6 + 8), lVar5 == 0)) {
      (**(code **)(*(long *)p_Var6 + 0x10))(p_Var6);
      std::__ndk1::__shared_weak_count::__release_weak(p_Var6);
    }
    p_Var6 = (__shared_weak_count *)
             CONCAT26(uStack_92,
                      CONCAT15(uStack_93,
                               CONCAT14(uStack_94,CONCAT13(uStack_95,CONCAT21(uStack_97,cStack_98)))
                              ));
    if ((p_Var6 != (__shared_weak_count *)0x0) &&
       (lVar5 = FUN_00bd6d90(0xffffffffffffffff,p_Var6 + 8), lVar5 == 0)) {
      (**(code **)(*(long *)p_Var6 + 0x10))(p_Var6);
      std::__ndk1::__shared_weak_count::__release_weak(p_Var6);
    }
  }
  if (((DAT_00c24f78 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00c24f78), iVar4 != 0)) {
    DAT_00c24f48 = 0;
    DAT_00c24f40 = &DAT_00c24f48;
    DAT_00c24f68 = 0;
    DAT_00c24f70 = 0;
    DAT_00c24f60 = 0;
    DAT_00c24f50 = 0;
    DAT_00c24f58 = &DAT_00c24f60;
    __cxa_atexit(FUN_0045bedc,&DAT_00c24f40,&PTR_LOOP_00be5ed0);
    __cxa_guard_release(&DAT_00c24f78);
  }
                    /* try { // try from 00adcee0 to 00bdd07b has its CatchHandler @ 00adcee0
                       catch() { ... } // from try @ 00adcee0 with catch @ 00adcee0
                       catch() { ... } // from try @ 00add084 with catch @ 00adcee0 */
  local_b8 = 0x26;
  uStack_af = (undefined5)s_unlockpopup_Guide_1_0029dc24._8_8_;
  cStack_aa = SUB81(s_unlockpopup_Guide_1_0029dc24._8_8_,5);
  cStack_a9 = SUB81(s_unlockpopup_Guide_1_0029dc24._8_8_,6);
  uStack_a8 = CONCAT31(0x315f65,SUB81(s_unlockpopup_Guide_1_0029dc24._8_8_,7));
  local_b7 = (undefined5)s_unlockpopup_Guide_1_0029dc24._0_8_;
  uStack_b2 = SUB82(s_unlockpopup_Guide_1_0029dc24._0_8_,5);
  cStack_b0 = SUB81(s_unlockpopup_Guide_1_0029dc24._0_8_,7);
  uStack_a4 = uStack_a4 & 0xffffff00;
  FUN_00469f7c(&local_a0,&local_b8);
  FUN_0045ba04(&local_80,&DAT_00c24f40,&local_a0,PTR_DAT_00c1adb0,0x14,0,0,0);
  p_Var6 = p_Stack_78;
  uVar2 = local_80;
  p_Var7 = (__shared_weak_count *)param_1[8];
  local_80 = 0;
  p_Stack_78 = (__shared_weak_count *)0x0;
  param_1[8] = p_Var6;
  param_1[7] = uVar2;
  p_Var6 = p_Stack_78;
  if ((p_Var7 != (__shared_weak_count *)0x0) &&
     (lVar5 = FUN_00bd6d90(0xffffffffffffffff,p_Var7 + 8), p_Var6 = p_Stack_78, lVar5 == 0)) {
    (**(code **)(*(long *)p_Var7 + 0x10))(p_Var7);
    std::__ndk1::__shared_weak_count::__release_weak(p_Var7);
    p_Var6 = p_Stack_78;
  }
  p_Stack_78 = p_Var6;
  if ((p_Var6 != (__shared_weak_count *)0x0) &&
     (lVar5 = FUN_00bd6d90(0xffffffffffffffff,p_Var6 + 8), lVar5 == 0)) {
    (**(code **)(*(long *)p_Var6 + 0x10))(p_Var6);
    std::__ndk1::__shared_weak_count::__release_weak(p_Var6);
  }
  if ((local_a0 & 1) != 0) {
    operator_delete(local_90);
  }
  if ((local_b8 & 1) != 0) {
    operator_delete((void *)CONCAT44(uStack_a4,uStack_a8));
  }
  lVar5 = FUN_0081f580();
  FUN_00a618b0(lVar5 + 0x1998,param_1);
  lVar5 = FUN_0081f580();
  FUN_007f8ecc(lVar5 + 0x3339a8,param_1);
  if (*(long *)(lVar1 + 0x28) == local_68) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
