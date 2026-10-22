# 00ace4cc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00ace4cc.md)

## 関数情報

~~~json
{
  "address": "00ace4cc",
  "name": "FUN_00ace4cc",
  "size": 3188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d5cd2b9aef8066174942fe89cff0149bb49033970a407b74e8fda70da4403d25",
  "source_text_sha256": "d5cd2b9aef8066174942fe89cff0149bb49033970a407b74e8fda70da4403d25"
}
~~~
## 呼び出し元

- [008d99b0](../008d9/008d99b0.md)
- [0092e43c](../0092e/0092e43c.md)
- [00932074](../00932/00932074.md)
- [0093249c](../00932/0093249c.md)
- [00934148](../00934/00934148.md)
- [00934fe8](../00934/00934fe8.md)
- [00935ba4](../00935/00935ba4.md)
- [00938cc0](../00938/00938cc0.md)
- [0093f290](../0093f/0093f290.md)
- [0093f2dc](../0093f/0093f2dc.md)
- [00a6731c](../00a67/00a6731c.md)
- [00a68ac0](../00a68/00a68ac0.md)
- [00a69030](../00a69/00a69030.md)

## 呼び出し先

- [0041b298](../0041b/0041b298.md)
- [004253b4](../00425/004253b4.md)
- [0044b660](../0044b/0044b660.md)
- [0045b734](../0045b/0045b734.md)
- [00467d20](../00467/00467d20.md)
- [00469f7c](../00469/00469f7c.md)
- [0046ff30](../0046f/0046ff30.md)
- [005bdd1c](../005bd/005bdd1c.md)
- [005bdd9c](../005bd/005bdd9c.md)
- [0064104c](../00641/0064104c.md)
- [006f18c4](../006f1/006f18c4.md)
- [006f3104](../006f3/006f3104.md)
- [0081f580](../0081f/0081f580.md)
- [00830c98](../00830/00830c98.md)
- [008d5d88](../008d5/008d5d88.md)
- [008eccc4](../008ec/008eccc4.md)
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
"2.imgcut"
"gatyaitemD_%02d_f.png"
"gatyaitem_%02d_f.png"
"gatyaitem_%02d_f_%@.png"
"img001.imgcut"
"img001.png"
"img050_01.imgcut"
"img050_01.png"
"img101.imgcut"
"img101.png"
"img101_nekoDojo.imgcut"
"img101_nekoDojo.png"
"img102.imgcut"
"img102.png"
"lang"
~~~
## 疑似コード 1/1 / UTF-8 20877 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */
/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00ace4cc(long param_1,uint param_2)

{
  ulong *puVar1;
  byte bVar2;
  byte bVar3;
  byte bVar4;
  byte bVar5;
  byte bVar6;
  byte bVar7;
  byte bVar8;
  byte bVar9;
  long lVar10;
  ulong uVar11;
  undefined4 uVar12;
  int iVar13;
  ulong uVar14;
  long lVar15;
  long lVar16;
  undefined8 uVar17;
  __shared_weak_count *p_Var18;
  __shared_weak_count *p_Var19;
  undefined8 uVar20;
  ulong local_100;
  __shared_weak_count *p_Stack_f8;
  void *local_f0;
  byte local_e8 [16];
  void *local_d8;
  undefined1 auStack_d0 [16];
  ushort local_c0 [8];
  void *local_b0;
  byte local_a8 [16];
  void *local_98;
  ulong local_90;
  __shared_weak_count *p_Stack_88;
  void *local_80;
  byte local_78;
  undefined5 local_77;
  char acStack_72 [3];
  char acStack_6f [5];
  char cStack_6a;
  char cStack_69;
  char cStack_68;
  char cStack_67;
  undefined5 uStack_66;
  undefined1 uStack_61;
  byte local_60;
  char acStack_5f [5];
  undefined2 uStack_5a;
  char cStack_58;
  undefined2 uStack_57;
  char cStack_55;
  undefined2 uStack_54;
  char cStack_52;
  char cStack_51;
  undefined4 uStack_50;
  uint uStack_4c;
  long local_48;
  
  lVar10 = tpidr_el0;
  local_48 = *(long *)(lVar10 + 0x28);
  puVar1 = (ulong *)(param_1 + 0x1a8 + (long)(int)param_2 * 0x10);
  if (((param_2 < 0x10) && (*puVar1 != 0)) && (uVar14 = FUN_00467d20(), (uVar14 & 1) != 0))
  goto LAB_00aceac0;
  if ((int)param_2 < 4) {
    if (param_2 == 0) {
      FUN_0081f580();
      FUN_00830c98(&local_60);
      uVar11 = CONCAT17(cStack_51,
                        CONCAT16(cStack_52,
                                 CONCAT24(uStack_54,
                                          CONCAT13(cStack_55,CONCAT21(uStack_57,cStack_58)))));
      uVar14 = CONCAT26(uStack_5a,CONCAT51(acStack_5f,local_60));
      p_Var18 = (__shared_weak_count *)puVar1[1];
      local_60 = 0;
      acStack_5f[0] = '\0';
      acStack_5f[1] = '\0';
      acStack_5f[2] = '\0';
      acStack_5f[3] = '\0';
      acStack_5f[4] = '\0';
      uStack_5a = 0;
      cStack_58 = '\0';
      uStack_57 = 0;
      cStack_55 = '\0';
      uStack_54 = 0;
      cStack_52 = '\0';
      cStack_51 = '\0';
      puVar1[1] = uVar11;
      *puVar1 = uVar14;
      if ((p_Var18 != (__shared_weak_count *)0x0) &&
         (lVar16 = FUN_00bd6d90(0xffffffffffffffff,p_Var18 + 8), lVar16 == 0)) {
        (**(code **)(*(long *)p_Var18 + 0x10))(p_Var18);
        std::__ndk1::__shared_weak_count::__release_weak(p_Var18);
      }
      p_Var18 = (__shared_weak_count *)
                CONCAT17(cStack_51,
                         CONCAT16(cStack_52,
                                  CONCAT24(uStack_54,
                                           CONCAT13(cStack_55,CONCAT21(uStack_57,cStack_58)))));
      if ((p_Var18 != (__shared_weak_count *)0x0) &&
         (lVar16 = FUN_00bd6d90(0xffffffffffffffff,p_Var18 + 8), lVar16 == 0)) {
        (**(code **)(*(long *)p_Var18 + 0x10))(p_Var18);
        std::__ndk1::__shared_weak_count::__release_weak(p_Var18);
      }
      goto LAB_00aceac0;
    }
    if (param_2 == 2) {
      lVar16 = FUN_0081f580();
      iVar13 = *(int *)(BYTE_ARRAY_0032fef1 + lVar16 + 0x1b);
      FUN_0081f580();
      if ((iVar13 == 5) && (lVar16 = FUN_0081f580(), *(char *)(lVar16 + 0x32e9) != '\0')) {
        if (((DAT_00c24f78 & 1) == 0) && (iVar13 = __cxa_guard_acquire(&DAT_00c24f78), iVar13 != 0))
        {
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
        local_60 = 0x26;
        uStack_4c = uStack_4c & 0xffffff00;
        local_78 = 0x2c;
        uStack_57 = (undefined2)s_img101_nekoDojo_png_002a4817._8_8_;
        cStack_55 = SUB81(s_img101_nekoDojo_png_002a4817._8_8_,2);
        uStack_54 = SUB82(s_img101_nekoDojo_png_002a4817._8_8_,3);
        cStack_52 = SUB81(s_img101_nekoDojo_png_002a4817._8_8_,5);
        cStack_51 = SUB81(s_img101_nekoDojo_png_002a4817._8_8_,6);
        uStack_50 = CONCAT31(0x676e70,SUB81(s_img101_nekoDojo_png_002a4817._8_8_,7));
        acStack_5f = SUB85(s_img101_nekoDojo_png_002a4817._0_8_,0);
        uStack_5a = SUB82(s_img101_nekoDojo_png_002a4817._0_8_,5);
        cStack_58 = SUB81(s_img101_nekoDojo_png_002a4817._0_8_,7);
        uStack_61 = 0;
        acStack_6f = SUB65(s_img101_nekoDojo_imgcut_002adceb._8_6_,0);
        cStack_6a = SUB61(s_img101_nekoDojo_imgcut_002adceb._8_6_,5);
        local_77 = (undefined5)s_img101_nekoDojo_imgcut_002adceb._0_8_;
        acStack_72 = SUB83(s_img101_nekoDojo_imgcut_002adceb._0_8_,5);
        cStack_69 = (char)s_img101_nekoDojo_imgcut_002adceb._14_2_;
        cStack_68 = SUB21(s_img101_nekoDojo_imgcut_002adceb._14_2_,1);
        cStack_67 = (char)s_img101_nekoDojo_imgcut_002adceb._16_6_;
        uStack_66 = SUB65(s_img101_nekoDojo_imgcut_002adceb._16_6_,1);
        FUN_0045b734(&local_90,&DAT_00c24f40,&local_60,&local_78,0x2601);
      }
      else {
        if (((DAT_00c24f78 & 1) == 0) && (iVar13 = __cxa_guard_acquire(&DAT_00c24f78), iVar13 != 0))
        {
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
        cStack_55 = '\0';
        local_60 = 0x14;
        uStack_57 = 0x676e;
        local_78 = 0x1a;
        acStack_5f = SUB85(s_img101_png_002add02._0_8_,0);
        uStack_5a = SUB82(s_img101_png_002add02._0_8_,5);
        cStack_58 = SUB81(s_img101_png_002add02._0_8_,7);
        cStack_6a = '\0';
        local_77 = _DAT_002a84dd;
        acStack_72[0] = s_1_imgcut_002a84e2[0];
        acStack_72[1] = s_1_imgcut_002a84e2[1];
        acStack_72[2] = s_1_imgcut_002a84e2[2];
        acStack_6f[0] = s_1_imgcut_002a84e2[3];
        acStack_6f[1] = s_1_imgcut_002a84e2[4];
        acStack_6f[2] = s_1_imgcut_002a84e2[5];
        acStack_6f[3] = s_1_imgcut_002a84e2[6];
        acStack_6f[4] = s_1_imgcut_002a84e2[7];
        FUN_0045b734(&local_90,&DAT_00c24f40,&local_60,&local_78,0x2601);
      }
    }
    else {
      if (param_2 != 3) goto LAB_00aceac0;
      if (((DAT_00c24f78 & 1) == 0) && (iVar13 = __cxa_guard_acquire(&DAT_00c24f78), iVar13 != 0)) {
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
      cStack_55 = '\0';
      local_60 = 0x14;
      uStack_57 = 0x676e;
      local_78 = 0x1a;
      acStack_5f = SUB85(s_img102_png_00294b68._0_8_,0);
      uStack_5a = SUB82(s_img102_png_00294b68._0_8_,5);
      cStack_58 = SUB81(s_img102_png_00294b68._0_8_,7);
      cStack_6a = '\0';
      local_77 = _DAT_002acb6e;
      acStack_72[0] = s_2_imgcut_002acb73[0];
      acStack_72[1] = s_2_imgcut_002acb73[1];
      acStack_72[2] = s_2_imgcut_002acb73[2];
      acStack_6f[0] = s_2_imgcut_002acb73[3];
      acStack_6f[1] = s_2_imgcut_002acb73[4];
      acStack_6f[2] = s_2_imgcut_002acb73[5];
      acStack_6f[3] = s_2_imgcut_002acb73[6];
      acStack_6f[4] = s_2_imgcut_002acb73[7];
      FUN_0045b734(&local_90,&DAT_00c24f40,&local_60,&local_78,0x2601);
    }
LAB_00acea34:
    p_Var18 = p_Stack_88;
    uVar14 = local_90;
    p_Var19 = (__shared_weak_count *)puVar1[1];
    local_90 = 0;
    p_Stack_88 = (__shared_weak_count *)0x0;
    puVar1[1] = (ulong)p_Var18;
    *puVar1 = uVar14;
    if ((p_Var19 != (__shared_weak_count *)0x0) &&
       (lVar16 = FUN_00bd6d90(0xffffffffffffffff,p_Var19 + 8), lVar16 == 0)) {
      (**(code **)(*(long *)p_Var19 + 0x10))(p_Var19);
      std::__ndk1::__shared_weak_count::__release_weak(p_Var19);
    }
    p_Var18 = p_Stack_88;
    if ((p_Stack_88 != (__shared_weak_count *)0x0) &&
       (lVar16 = FUN_00bd6d90(0xffffffffffffffff,p_Stack_88 + 8), lVar16 == 0)) {
      (**(code **)(*(long *)p_Var18 + 0x10))(p_Var18);
      std::__ndk1::__shared_weak_count::__release_weak(p_Var18);
    }
    if ((local_78 & 1) != 0) {
      operator_delete((void *)CONCAT17(uStack_61,CONCAT52(uStack_66,CONCAT11(cStack_67,cStack_68))))
      ;
    }
    if ((local_60 & 1) == 0) goto LAB_00aceac0;
    local_80 = (void *)CONCAT44(uStack_4c,uStack_50);
  }
  else {
    if (param_2 == 4) {
      if (((DAT_00c24f78 & 1) == 0) && (iVar13 = __cxa_guard_acquire(&DAT_00c24f78), iVar13 != 0)) {
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
      cStack_55 = '\0';
      local_60 = 0x14;
      uStack_57 = 0x676e;
      local_78 = 0x1a;
      acStack_5f = SUB85(s_img001_png_002a081f._0_8_,0);
      uStack_5a = SUB82(s_img001_png_002a081f._0_8_,5);
      cStack_58 = SUB81(s_img001_png_002a081f._0_8_,7);
      cStack_6a = '\0';
      local_77 = (undefined5)DAT_0029b6af;
      acStack_72[0] = DAT_0029b6af._5_1_;
      acStack_72[1] = DAT_0029b6af._6_1_;
      acStack_72[2] = DAT_0029b6af._7_1_;
      acStack_6f[0] = UNK_0029b6b7;
      acStack_6f[1] = DAT_0029b6b8;
      acStack_6f[2] = UNK_0029b6b9;
      acStack_6f[3] = UNK_0029b6ba;
      acStack_6f[4] = UNK_0029b6bb;
      FUN_0045b734(&local_90,&DAT_00c24f40,&local_60,&local_78,0x2601);
      goto LAB_00acea34;
    }
    if (param_2 == 5) {
      if (((DAT_00c24f78 & 1) == 0) && (iVar13 = __cxa_guard_acquire(&DAT_00c24f78), iVar13 != 0)) {
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
      local_60 = 0x1a;
      cStack_52 = '\0';
      acStack_5f[0] = s_img050_01_png_002aeec9[0];
      acStack_5f[1] = s_img050_01_png_002aeec9[1];
      acStack_5f[2] = s_img050_01_png_002aeec9[2];
      acStack_5f[3] = s_img050_01_png_002aeec9[3];
      acStack_5f[4] = s_img050_01_png_002aeec9[4];
      uStack_5a = (undefined2)s_img050_01_png_002aeec9._5_3_;
      cStack_58 = SUB31(s_img050_01_png_002aeec9._5_3_,2);
      uStack_57 = (undefined2)s_img050_01_png_002aeec9._8_5_;
      cStack_55 = SUB51(s_img050_01_png_002aeec9._8_5_,2);
      uStack_54 = SUB52(s_img050_01_png_002aeec9._8_5_,3);
      local_78 = 0x20;
      cStack_67 = '\0';
      acStack_6f = SUB85(s_img050_01_imgcut_002ade27._8_8_,0);
      cStack_6a = SUB81(s_img050_01_imgcut_002ade27._8_8_,5);
      cStack_69 = SUB81(s_img050_01_imgcut_002ade27._8_8_,6);
      cStack_68 = SUB81(s_img050_01_imgcut_002ade27._8_8_,7);
      local_77 = (undefined5)s_img050_01_imgcut_002ade27._0_8_;
      acStack_72 = SUB83(s_img050_01_imgcut_002ade27._0_8_,5);
      FUN_0045b734(&local_90,&DAT_00c24f40,&local_60,&local_78,0x2601);
      goto LAB_00acea34;
    }
    if ((param_2 != 6) || (lVar16 = FUN_0081f580(), BYTE_ARRAY_00331ea1[lVar16 + 9] == 0))
    goto LAB_00aceac0;
    lVar16 = FUN_0081f580();
    lVar15 = FUN_0081f580();
    lVar16 = lVar16 + (long)*(int *)((long)&DWORD_0033a22c + lVar15) * 8;
    if (((uint)(BYTE_ARRAY_00335e09[lVar16 + 0x1c] ^ BYTE_ARRAY_00335e09[lVar16 + 0x19]) << 0x10 |
         (uint)(BYTE_ARRAY_00335e09[lVar16 + 0x1b] ^ BYTE_ARRAY_00335e09[lVar16 + 0x1a]) << 0x18 |
         (uint)(BYTE_ARRAY_00335e09[lVar16 + 0x1d] ^ BYTE_ARRAY_00335e09[lVar16 + 0x18]) << 8 |
        (uint)(BYTE_ARRAY_00335e09[lVar16 + 0x1e] ^ BYTE_ARRAY_00335e09[lVar16 + 0x17])) == 1) {
      if (((DAT_00c24f78 & 1) == 0) && (iVar13 = __cxa_guard_acquire(&DAT_00c24f78), iVar13 != 0)) {
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
      local_90 = 0x676e702e73250c;
      lVar16 = FUN_0081f580();
      lVar15 = FUN_0081f580();
      lVar16 = lVar16 + (long)*(int *)((long)&DWORD_0033a22c + lVar15) * 8;
      FUN_0064104c(local_a8,(uint)(BYTE_ARRAY_00335a05[lVar16 + 0x20] ^
                                  BYTE_ARRAY_00335a05[lVar16 + 0x1d]) << 0x10 |
                            (uint)(BYTE_ARRAY_00335a05[lVar16 + 0x1f] ^
                                  BYTE_ARRAY_00335a05[lVar16 + 0x1e]) << 0x18 |
                            (uint)(BYTE_ARRAY_00335a05[lVar16 + 0x21] ^
                                  BYTE_ARRAY_00335a05[lVar16 + 0x1c]) << 8 |
                            (uint)(BYTE_ARRAY_00335a05[lVar16 + 0x22] ^
                                  BYTE_ARRAY_00335a05[lVar16 + 0x1b]),0);
      FUN_0046ff30(&local_78,&local_90,local_a8);
      FUN_00469f7c(&local_60,&local_78);
      local_c0[0] = 0;
      FUN_0045b734(&local_100,&DAT_00c24f40,&local_60,local_c0,0x2601);
      p_Var18 = p_Stack_f8;
      uVar14 = local_100;
      p_Var19 = (__shared_weak_count *)puVar1[1];
      local_100 = 0;
      p_Stack_f8 = (__shared_weak_count *)0x0;
      puVar1[1] = (ulong)p_Var18;
      *puVar1 = uVar14;
      if ((p_Var19 != (__shared_weak_count *)0x0) &&
         (lVar16 = FUN_00bd6d90(0xffffffffffffffff,p_Var19 + 8), lVar16 == 0)) {
        (**(code **)(*(long *)p_Var19 + 0x10))(p_Var19);
        std::__ndk1::__shared_weak_count::__release_weak(p_Var19);
      }
      p_Var18 = p_Stack_f8;
      if ((p_Stack_f8 != (__shared_weak_count *)0x0) &&
         (lVar16 = FUN_00bd6d90(0xffffffffffffffff,p_Stack_f8 + 8), lVar16 == 0)) {
        (**(code **)(*(long *)p_Var18 + 0x10))(p_Var18);
        std::__ndk1::__shared_weak_count::__release_weak(p_Var18);
      }
      if ((local_c0[0] & 1) != 0) {
        operator_delete(local_b0);
      }
      if ((local_60 & 1) != 0) {
        operator_delete((void *)CONCAT44(uStack_4c,uStack_50));
      }
      local_b0 = local_98;
      if ((local_78 & 1) != 0) {
        operator_delete((void *)CONCAT17(uStack_61,CONCAT52(uStack_66,CONCAT11(cStack_67,cStack_68))
                                        ));
        local_b0 = local_98;
      }
      if ((local_a8[0] & 1) != 0) goto LAB_00acee90;
    }
    else {
      lVar16 = FUN_0081f580();
      lVar15 = FUN_0081f580();
      lVar16 = lVar16 + (long)*(int *)((long)&DWORD_0033a22c + lVar15) * 8;
      bVar2 = BYTE_ARRAY_00335e09[lVar16 + 0x19];
      bVar3 = BYTE_ARRAY_00335e09[lVar16 + 0x1c];
      bVar4 = BYTE_ARRAY_00335e09[lVar16 + 0x1b];
      bVar5 = BYTE_ARRAY_00335e09[lVar16 + 0x18];
      bVar6 = BYTE_ARRAY_00335e09[lVar16 + 0x1a];
      bVar7 = BYTE_ARRAY_00335e09[lVar16 + 0x1d];
      bVar8 = BYTE_ARRAY_00335e09[lVar16 + 0x17];
      bVar9 = BYTE_ARRAY_00335e09[lVar16 + 0x1e];
      lVar16 = FUN_0081f580();
      lVar15 = FUN_0081f580();
      lVar16 = lVar16 + (long)*(int *)((long)&DWORD_0033a22c + lVar15) * 8;
      if (((uint)(bVar3 ^ bVar2) << 0x10 | (uint)(bVar4 ^ bVar6) << 0x18 |
           (uint)(bVar7 ^ bVar5) << 8 | (uint)(bVar9 ^ bVar8)) == 2) {
        iVar13 = FUN_006f18c4(lVar16 + 0x335a20);
        if (iVar13 != 0) {
          lVar16 = FUN_0081f580();
          lVar15 = FUN_0081f580();
          iVar13 = FUN_006f18c4(lVar16 + (long)*(int *)((long)&DWORD_0033a22c + lVar15) * 8 +
                                0x335a20);
          if (iVar13 != 2) {
            lVar16 = FUN_0081f580();
            lVar15 = FUN_0081f580();
            iVar13 = FUN_006f18c4(lVar16 + (long)*(int *)((long)&DWORD_0033a22c + lVar15) * 8 +
                                  0x335a20);
            if (iVar13 != 3) {
              lVar16 = FUN_0081f580();
              lVar15 = FUN_0081f580();
              iVar13 = FUN_006f18c4(lVar16 + (long)*(int *)((long)&DWORD_0033a22c + lVar15) * 8 +
                                    0x335a20);
              if (iVar13 != 4) {
                lVar16 = FUN_0081f580();
                lVar15 = FUN_0081f580();
                iVar13 = FUN_006f18c4(lVar16 + (long)*(int *)((long)&DWORD_0033a22c + lVar15) * 8 +
                                      0x335a20);
                if (iVar13 != 5) {
                  uVar17 = FUN_005bdd1c();
                  FUN_0041b298(&local_90,"gatyaitem_%02d_f.png");
                  lVar16 = FUN_0081f580();
                  lVar15 = FUN_0081f580();
                  FUN_008eccc4(&local_78,&local_90,0,
                               *(undefined8 *)
                                (BYTE_ARRAY_00335a05 +
                                lVar16 + (long)*(int *)((long)&DWORD_0033a22c + lVar15) * 8 + 0x1b))
                  ;
                  FUN_00469f7c(&local_60,&local_78);
                  FUN_0041b298(local_c0,&DAT_002967d9);
                  FUN_0045b734(&local_100,uVar17,&local_60,local_c0,0x2601);
                  goto LAB_00acedbc;
                }
              }
            }
          }
        }
        uVar17 = FUN_005bdd1c();
        FUN_0041b298(&local_90,"gatyaitem_%02d_f_%@.png");
        lVar16 = FUN_0081f580();
        lVar15 = FUN_0081f580();
        uVar20 = *(undefined8 *)
                  (BYTE_ARRAY_00335a05 +
                  lVar16 + (long)*(int *)((long)&DWORD_0033a22c + lVar15) * 8 + 0x1b);
        FUN_0041b298(local_c0,&DAT_00293a68);
        FUN_00469f7c(local_e8,local_c0);
        FUN_008d5d88(&local_78,&local_90,uVar20,local_e8);
        FUN_00469f7c(&local_60,&local_78);
        FUN_0041b298(&local_100,&DAT_002967d9);
        FUN_0045b734(auStack_d0,uVar17,&local_60,&local_100,0x2601);
        FUN_005bdd9c(puVar1,auStack_d0);
        FUN_0044b660(auStack_d0);
        if ((local_100 & 1) != 0) {
          operator_delete(local_f0);
        }
                    /* try { // try from 00acee30 to 00bcee3b has its CatchHandler @ 00ad0980 */
        if ((local_60 & 1) != 0) {
          operator_delete((void *)CONCAT44(uStack_4c,uStack_50));
                    /* try { // try from 00acee3c to 00bcfcf7 has its CatchHandler @ 00ace1d0 */
        }
        if ((local_78 & 1) != 0) {
          operator_delete((void *)CONCAT17(uStack_61,
                                           CONCAT52(uStack_66,CONCAT11(cStack_67,cStack_68))));
        }
        if ((local_e8[0] & 1) != 0) {
          operator_delete(local_d8);
        }
        if ((local_c0[0] & 1) != 0) {
LAB_00acee90:
          operator_delete(local_b0);
        }
      }
      else {
        iVar13 = FUN_006f18c4(lVar16 + 0x335e20);
        if (iVar13 != 3) goto LAB_00aceac0;
        uVar17 = FUN_005bdd1c();
        FUN_0041b298(&local_90,"gatyaitemD_%02d_f.png");
        lVar16 = FUN_0081f580();
        lVar15 = FUN_0081f580();
        FUN_006f18c4(lVar16 + (long)*(int *)((long)&DWORD_0033a22c + lVar15) * 8 + 0x335a20);
        uVar12 = FUN_006f3104();
        FUN_004253b4(&local_78,&local_90,0,uVar12);
        FUN_00469f7c(&local_60,&local_78);
        FUN_0041b298(local_c0,&DAT_002967d9);
        FUN_0045b734(&local_100,uVar17,&local_60,local_c0,0x2601);
LAB_00acedbc:
        FUN_005bdd9c(puVar1,&local_100);
        FUN_0044b660(&local_100);
        if ((local_c0[0] & 1) != 0) {
          operator_delete(local_b0);
        }
        if ((local_60 & 1) != 0) {
          operator_delete((void *)CONCAT44(uStack_4c,uStack_50));
        }
        if ((local_78 & 1) != 0) {
          local_b0 = (void *)CONCAT17(uStack_61,CONCAT52(uStack_66,CONCAT11(cStack_67,cStack_68)));
          goto LAB_00acee90;
        }
      }
    }
    if ((local_90 & 1) == 0) goto LAB_00aceac0;
  }
  operator_delete(local_80);
LAB_00aceac0:
  if (*(long *)(lVar10 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail(*puVar1);
  }
  return;
}

~~~
