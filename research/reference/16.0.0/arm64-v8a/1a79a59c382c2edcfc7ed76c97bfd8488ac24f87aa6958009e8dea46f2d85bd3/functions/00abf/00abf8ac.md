# 00abf8ac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00abf8ac",
  "name": "FUN_00abf8ac",
  "size": 2064,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "956c8f8c6f3b377123e51ef5b84f643502a8f60e72c7c99d4b584f67043a1029",
  "source_text_sha256": "956c8f8c6f3b377123e51ef5b84f643502a8f60e72c7c99d4b584f67043a1029"
}
~~~

## 呼び出し元

- [00abf588](../00abf/00abf588.md)
- [00b3c6b0](../00b3c/00b3c6b0.md)

## 呼び出し先

- [0043bae0](../0043b/0043bae0.md)
- [00447eb4](../00447/00447eb4.md)
- [0046e930](../0046e/0046e930.md)
- [0047e5cc](../0047e/0047e5cc.md)
- [0047e89c](../0047e/0047e89c.md)
- [0048ce14](../0048c/0048ce14.md)
- [00492dc8](../00492/00492dc8.md)
- [0049f3b0](../0049f/0049f3b0.md)
- [00ac0de8](../00ac0/00ac0de8.md)
- [00c538e0](../00c53/00c538e0.md)
- [00c53b3c](../00c53/00c53b3c.md)
- [00c57a30](../00c57/00c57a30.md)
- [00c57a50](../00c57/00c57a50.md)
- [00c57a70](../00c57/00c57a70.md)
- [00c57a80](../00c57/00c57a80.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)

## 関連文字列（未確認候補）

~~~text
"medal_%03d.png"
"medal_001.imgcut"
"medal_get000.imgcut"
"medal_get000.png"
"medal_get001.maanim"
"medal_get002.maanim"
"medal_txt1"
"medal_txt2"
~~~

## 疑似コード / UTF-8 18282 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void FUN_00abf8ac(long *param_1,long param_2)

{
  long lVar1;
  undefined8 uVar2;
  int iVar3;
  long lVar4;
  undefined8 uVar5;
  ulong uVar6;
  long *plVar7;
  long *plVar8;
  long *plVar9;
  ulong local_e0;
  undefined8 uStack_d8;
  void *local_d0;
  byte local_c0;
  undefined7 uStack_bf;
  char cStack_b8;
  undefined2 uStack_b7;
  char cStack_b5;
  undefined4 uStack_b4;
  char local_b0;
  undefined1 uStack_af;
  undefined6 uStack_ae;
  undefined8 local_a0;
  long *plStack_98;
  byte local_88;
  undefined6 local_87;
  undefined2 uStack_81;
  undefined6 uStack_7f;
  char cStack_79;
  undefined4 uStack_78;
  uint uStack_74;
  byte local_70;
  char local_6f [8];
  undefined7 uStack_67;
  char cStack_60;
  undefined1 uStack_5f;
  undefined2 uStack_5e;
  uint uStack_5c;
  long local_58;
  
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  if ((int)param_1[0xe] != -1) {
    if (((DAT_00ca4b38 & 1) == 0) && (iVar3 = __cxa_guard_acquire(&DAT_00ca4b38), iVar3 != 0)) {
      DAT_00ca4b08 = 0;
                    /* try { // try from 00abff14 to 00bc0197 has its CatchHandler @ 00abf53c */
      DAT_00ca4b00 = &DAT_00ca4b08;
      DAT_00ca4b28 = 0;
      DAT_00ca4b30 = 0;
      DAT_00ca4b20 = 0;
      DAT_00ca4b10 = 0;
      DAT_00ca4b18 = &DAT_00ca4b20;
      __cxa_atexit(FUN_0047ed74,&DAT_00ca4b00,&PTR_LOOP_00c62b90);
      __cxa_guard_release(&DAT_00ca4b38);
    }
    local_70 = 0x20;
    local_88 = 0x26;
    uStack_67 = (undefined7)s_medal_get000_png_002ab964._8_8_;
    cStack_60 = SUB81(s_medal_get000_png_002ab964._8_8_,7);
    local_6f[0] = s_medal_get000_png_002ab964[0];
    local_6f[1] = s_medal_get000_png_002ab964[1];
    local_6f[2] = s_medal_get000_png_002ab964[2];
    local_6f[3] = s_medal_get000_png_002ab964[3];
    local_6f[4] = s_medal_get000_png_002ab964[4];
    local_6f[5] = s_medal_get000_png_002ab964[5];
    local_6f[6] = s_medal_get000_png_002ab964[6];
    local_6f[7] = s_medal_get000_png_002ab964[7];
    uStack_5f = 0;
    uStack_7f = (undefined6)s_medal_get000_imgcut_002adad5._8_8_;
    cStack_79 = SUB81(s_medal_get000_imgcut_002adad5._8_8_,6);
    uStack_78 = CONCAT31(0x747563,SUB81(s_medal_get000_imgcut_002adad5._8_8_,7));
    local_87 = (undefined6)s_medal_get000_imgcut_002adad5._0_8_;
    uStack_81 = SUB82(s_medal_get000_imgcut_002adad5._0_8_,6);
    uStack_74 = uStack_74 & 0xffffff00;
    FUN_0047e5cc(&local_c0,&DAT_00ca4b00,&local_70,&local_88,0x2601);
    uVar2 = CONCAT44(uStack_b4,CONCAT13(cStack_b5,CONCAT21(uStack_b7,cStack_b8)));
                    /* try { // try from 00abf95c to 00bbf963 has its CatchHandler @ 00ac0098 */
    uVar5 = CONCAT71(uStack_bf,local_c0);
    plVar8 = *(long **)(param_2 + 0x50);
    local_c0 = 0;
    uStack_bf = 0;
    cStack_b8 = '\0';
    uStack_b7 = 0;
    cStack_b5 = 0;
    uStack_b4 = 0;
    *(undefined8 *)(param_2 + 0x50) = uVar2;
    *(undefined8 *)(param_2 + 0x48) = uVar5;
    if ((plVar8 == (long *)0x0) || (lVar4 = FUN_00c538e0(0xffffffffffffffff,plVar8 + 1), lVar4 != 0)
       ) {
      plVar8 = (long *)CONCAT44(uStack_b4,CONCAT13(cStack_b5,CONCAT21(uStack_b7,cStack_b8)));
    }
    else {
      (**(code **)(*plVar8 + 0x10))(plVar8);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
      plVar8 = (long *)CONCAT44(uStack_b4,CONCAT13(cStack_b5,CONCAT21(uStack_b7,cStack_b8)));
                    /* try { // try from 00abf9d0 to 00bbf9ef has its CatchHandler @ 00ac0164 */
    }
                    /* try { // try from 00abf98c to 00bbf997 has its CatchHandler @ 00ac0090 */
    if ((plVar8 != (long *)0x0) &&
       (lVar4 = FUN_00c538e0(0xffffffffffffffff,(long *)((long)plVar8 + 8)), lVar4 == 0)) {
      (**(code **)(*plVar8 + 0x10))(plVar8);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
    }
    if ((local_88 & 1) != 0) {
      _ZdlPv((void *)CONCAT44(uStack_74,uStack_78));
                    /* try { // try from 00abfa04 to 00bbfa0b has its CatchHandler @ 00ac00d0 */
    }
    if ((local_70 & 1) != 0) {
      _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT22(uStack_5e,CONCAT11(uStack_5f,cStack_60))));
    }
    if (((DAT_00ca4b38 & 1) == 0) && (iVar3 = __cxa_guard_acquire(&DAT_00ca4b38), iVar3 != 0)) {
      DAT_00ca4b08 = 0;
      DAT_00ca4b00 = &DAT_00ca4b08;
      DAT_00ca4b28 = 0;
      DAT_00ca4b30 = 0;
      DAT_00ca4b20 = 0;
      DAT_00ca4b10 = 0;
      DAT_00ca4b18 = &DAT_00ca4b20;
      __cxa_atexit(FUN_0047ed74,&DAT_00ca4b00,&PTR_LOOP_00c62b90);
                    /* catch() { ... } // from try @ 00abfe78 with catch @ 00abff80 */
                    /* catch() { ... } // from try @ 00abfdb8 with catch @ 00abff84 */
      __cxa_guard_release(&DAT_00ca4b38);
    }
    local_88 = 0x1c;
    plVar8 = param_1 + 0xf;
                    /* try { // try from 00abfa34 to 00bbfa3f has its CatchHandler @ 00ac00c8 */
    cStack_79 = 0;
                    /* try { // try from 00abfa40 to 00bbfa43 has its CatchHandler @ 00ac0100 */
    local_87._0_1_ = s_medal__03d_png_002bb807[0];
    local_87._1_1_ = s_medal__03d_png_002bb807[1];
    local_87._2_1_ = s_medal__03d_png_002bb807[2];
    local_87._3_1_ = s_medal__03d_png_002bb807[3];
    local_87._4_1_ = s_medal__03d_png_002bb807[4];
    local_87._5_1_ = s_medal__03d_png_002bb807[5];
    uStack_81._0_1_ = s_medal__03d_png_002bb807[6];
    uStack_81._1_1_ = s_medal__03d_png_002bb807[7];
    uStack_7f._0_1_ = s_medal__03d_png_002bb807[8];
    uStack_7f._1_1_ = s_medal__03d_png_002bb807[9];
    uStack_7f._2_1_ = s_medal__03d_png_002bb807[10];
    uStack_7f._3_1_ = s_medal__03d_png_002bb807[0xb];
    uStack_7f._4_1_ = s_medal__03d_png_002bb807[0xc];
    uStack_7f._5_1_ = s_medal__03d_png_002bb807[0xd];
    if ((undefined4 *)param_1[0x10] == (undefined4 *)*plVar8) {
                    /* catch() { ... } // from try @ 00abfdac with catch @ 00abff9c */
      if (*(long *)(lVar1 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
        FUN_0049f3b0(plVar8);
      }
      goto LAB_00ac01a4;
    }
    FUN_00447eb4(&local_70,&local_88,0,*(undefined4 *)*plVar8);
    local_c0 = 0x20;
    uStack_af = 0;
    uStack_b7 = (undefined2)s_medal_001_imgcut_002bcaae._8_8_;
    cStack_b5 = SUB81(s_medal_001_imgcut_002bcaae._8_8_,2);
    uStack_b4 = SUB84(s_medal_001_imgcut_002bcaae._8_8_,3);
    local_b0 = SUB81(s_medal_001_imgcut_002bcaae._8_8_,7);
    uStack_bf = (undefined7)s_medal_001_imgcut_002bcaae._0_8_;
    cStack_b8 = SUB81(s_medal_001_imgcut_002bcaae._0_8_,7);
                    /* try { // try from 00abfa80 to 00bbfaff has its CatchHandler @ 00ac0138 */
    FUN_0047e5cc(&local_a0,&DAT_00ca4b00,&local_70,&local_c0,0x2601);
    plVar7 = plStack_98;
    uVar5 = local_a0;
    plVar9 = *(long **)(param_2 + 0x60);
    local_a0 = 0;
    plStack_98 = (long *)0x0;
    *(long **)(param_2 + 0x60) = plVar7;
    *(undefined8 *)(param_2 + 0x58) = uVar5;
    plVar7 = plStack_98;
    if ((plVar9 != (long *)0x0) &&
       (lVar4 = FUN_00c538e0(0xffffffffffffffff,plVar9 + 1), plVar7 = plStack_98, lVar4 == 0)) {
      (**(code **)(*plVar9 + 0x10))(plVar9);
                    /* try { // try from 00abfdf4 to 00bbfe0f has its CatchHandler @ 00ac0108 */
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
      plVar7 = plStack_98;
    }
    plStack_98 = plVar7;
    if ((plVar7 != (long *)0x0) &&
       (lVar4 = FUN_00c538e0(0xffffffffffffffff,(long *)((long)plVar7 + 8)), lVar4 == 0)) {
                    /* try { // try from 00abfe14 to 00bbfe1f has its CatchHandler @ 00abffc0 */
      (**(code **)(*plVar7 + 0x10))(plVar7);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
                    /* try { // try from 00abfe20 to 00bbfe2f has its CatchHandler @ 00abffb8 */
    }
    if ((local_c0 & 1) != 0) {
      _ZdlPv((void *)CONCAT62(uStack_ae,CONCAT11(uStack_af,local_b0)));
    }
    if ((local_70 & 1) != 0) {
      _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT22(uStack_5e,CONCAT11(uStack_5f,cStack_60))));
    }
    if ((local_88 & 1) != 0) {
      _ZdlPv((void *)CONCAT44(uStack_74,uStack_78));
    }
    if ((ulong)(param_1[0x10] - param_1[0xf]) < 5) {
                    /* catch() { ... } // from try @ 00abf678 with catch @ 00ac0008 */
      if (((DAT_00ca4b38 & 1) == 0) && (iVar3 = __cxa_guard_acquire(&DAT_00ca4b38), iVar3 != 0)) {
        DAT_00ca4b08 = 0;
        DAT_00ca4b00 = &DAT_00ca4b08;
        DAT_00ca4b28 = 0;
        DAT_00ca4b30 = 0;
        DAT_00ca4b20 = 0;
        DAT_00ca4b10 = 0;
        DAT_00ca4b18 = &DAT_00ca4b20;
        __cxa_atexit(FUN_0047ed74,&DAT_00ca4b00,&PTR_LOOP_00c62b90);
        __cxa_guard_release(&DAT_00ca4b38);
      }
      local_c0 = 0x14;
      uStack_b7 = 0x3174;
      uStack_bf = (undefined7)s_medal_txt1_002a17d1._0_8_;
      cStack_b8 = SUB81(s_medal_txt1_002a17d1._0_8_,7);
      cStack_b5 = 0;
      FUN_0048ce14(&local_88,&local_c0);
                    /* try { // try from 00abfc74 to 00bbfc7f has its CatchHandler @ 00ac0108 */
      if ((int *)param_1[0x10] == (int *)param_1[0xf]) {
                    /* catch() { ... } // from try @ 00abfec0 with catch @ 00ac0050 */
                    /* catch() { ... } // from try @ 00abf844 with catch @ 00ac0054 */
                    /* catch() { ... } // from try @ 00abf820 with catch @ 00ac005c */
        if (*(long *)(lVar1 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00abfbb8 with catch @ 00ac0064 */
          FUN_0049f3b0(plVar8);
        }
        goto LAB_00ac01a4;
      }
      uVar6 = (ulong)*(int *)param_1[0xf];
                    /* try { // try from 00abfc80 to 00bbfc87 has its CatchHandler @ 00abffe4 */
      if ((ulong)(param_1[1] - *param_1 >> 3) <= uVar6) {
        if (*(long *)(lVar1 + 0x28) == local_58) {
                    /* catch() { ... } // from try @ 00abfb90 with catch @ 00ac007c */
          uVar5 = FUN_00ac0de8(param_1);
                    /* catch() { ... } // from try @ 00abfb10 with catch @ 00ac00b4 */
          if ((local_70 & 1) != 0) {
            _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT22(uStack_5e,CONCAT11(uStack_5f,cStack_60))));
          }
          if (*(long *)(lVar1 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
            FUN_00c53b3c(uVar5);
          }
        }
        goto LAB_00ac01a4;
      }
      lVar4 = *(long *)(*param_1 + uVar6 * 8);
      if ((*(byte *)(lVar4 + 0x80) & 1) == 0) {
        uStack_d8 = *(undefined8 *)(lVar4 + 0x88);
        local_e0 = *(ulong *)(lVar4 + 0x80);
        local_d0 = *(void **)(lVar4 + 0x90);
      }
      else {
                    /* try { // try from 00abfcb4 to 00bbfcbf has its CatchHandler @ 00abffdc */
        FUN_0043bae0(&local_e0,*(undefined8 *)(lVar4 + 0x90),*(undefined8 *)(lVar4 + 0x88));
      }
                    /* try { // try from 00abfcc0 to 00bbfcd3 has its CatchHandler @ 00abffd8 */
      FUN_00492dc8(&local_70,&local_88,&local_e0);
      FUN_0047e89c(&local_a0,&DAT_00ca4b00,&local_70,PTR_DAT_00c9a8a0,0x14,0,0,0);
      plVar8 = plStack_98;
      uVar5 = local_a0;
      plVar7 = *(long **)(param_2 + 0x70);
      local_a0 = 0;
      plStack_98 = (long *)0x0;
      *(long **)(param_2 + 0x70) = plVar8;
      *(undefined8 *)(param_2 + 0x68) = uVar5;
                    /* try { // try from 00abfd0c to 00bbfd13 has its CatchHandler @ 00abffc4 */
      if ((plVar7 != (long *)0x0) &&
         (lVar4 = FUN_00c538e0(0xffffffffffffffff,plVar7 + 1), lVar4 == 0)) {
        (**(code **)(*plVar7 + 0x10))(plVar7);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
      }
      plVar8 = plStack_98;
      if ((plStack_98 != (long *)0x0) &&
         (lVar4 = FUN_00c538e0(0xffffffffffffffff,plStack_98 + 1), lVar4 == 0)) {
        (**(code **)(*plVar8 + 0x10))(plVar8);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
      }
      if ((local_70 & 1) != 0) {
        _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT22(uStack_5e,CONCAT11(uStack_5f,cStack_60))));
      }
      if ((local_e0 & 1) != 0) {
                    /* try { // try from 00abfec0 to 00bbff13 has its CatchHandler @ 00ac0050 */
        _ZdlPv(local_d0);
      }
                    /* try { // try from 00abfd60 to 00bbfd73 has its CatchHandler @ 00ac0108 */
      if ((local_88 & 1) != 0) {
        _ZdlPv((void *)CONCAT44(uStack_74,uStack_78));
      }
      if ((local_c0 & 1) != 0) {
        _ZdlPv((void *)CONCAT62(uStack_ae,CONCAT11(uStack_af,local_b0)));
      }
                    /* try { // try from 00abfd74 to 00bbfd7f has its CatchHandler @ 00abffb4 */
      local_70 = 0x26;
      uStack_5f = 0x6e;
      uStack_5e = 0x6d69;
      uStack_67 = (undefined7)s_medal_get001_maanim_002b7b7d._8_8_;
      cStack_60 = SUB81(s_medal_get001_maanim_002b7b7d._8_8_,7);
      local_6f[0] = s_medal_get001_maanim_002b7b7d[0];
      local_6f[1] = s_medal_get001_maanim_002b7b7d[1];
      local_6f[2] = s_medal_get001_maanim_002b7b7d[2];
      local_6f[3] = s_medal_get001_maanim_002b7b7d[3];
      local_6f[4] = s_medal_get001_maanim_002b7b7d[4];
      local_6f[5] = s_medal_get001_maanim_002b7b7d[5];
      local_6f[6] = s_medal_get001_maanim_002b7b7d[6];
      local_6f[7] = s_medal_get001_maanim_002b7b7d[7];
      uStack_5c = uStack_5c & 0xffffff00;
      FUN_0046e930(param_1 + 0x2a,&local_70);
    }
    else {
                    /* try { // try from 00abfb08 to 00bbfb0f has its CatchHandler @ 00ac0100 */
                    /* catch() { ... } // from try @ 00abfd74 with catch @ 00abffb4 */
      if (((DAT_00ca4b38 & 1) == 0) && (iVar3 = __cxa_guard_acquire(&DAT_00ca4b38), iVar3 != 0)) {
                    /* catch() { ... } // from try @ 00abfe20 with catch @ 00abffb8 */
                    /* catch() { ... } // from try @ 00abfe14 with catch @ 00abffc0 */
                    /* catch() { ... } // from try @ 00abfd0c with catch @ 00abffc4 */
        DAT_00ca4b08 = 0;
        DAT_00ca4b00 = &DAT_00ca4b08;
                    /* catch() { ... } // from try @ 00abfcc0 with catch @ 00abffd8 */
                    /* catch() { ... } // from try @ 00abfcb4 with catch @ 00abffdc */
        DAT_00ca4b28 = 0;
        DAT_00ca4b30 = 0;
        DAT_00ca4b20 = 0;
                    /* catch() { ... } // from try @ 00abfc80 with catch @ 00abffe4 */
        DAT_00ca4b10 = 0;
        DAT_00ca4b18 = &DAT_00ca4b20;
                    /* catch() { ... } // from try @ 00abf65c with catch @ 00abffe8 */
        __cxa_atexit(FUN_0047ed74,&DAT_00ca4b00,&PTR_LOOP_00c62b90);
                    /* catch() { ... } // from try @ 00abf640 with catch @ 00abfff4 */
        __cxa_guard_release(&DAT_00ca4b38);
      }
                    /* try { // try from 00abfb10 to 00bbfb1f has its CatchHandler @ 00ac00b4 */
      local_c0 = 0x14;
      uStack_b7 = 0x3274;
      uStack_bf = (undefined7)s_medal_txt2_002a17c6._0_8_;
      cStack_b8 = SUB81(s_medal_txt2_002a17c6._0_8_,7);
      cStack_b5 = 0;
                    /* try { // try from 00abfb38 to 00bbfb3f has its CatchHandler @ 00ac009c */
      FUN_0048ce14(&local_88,&local_c0);
      FUN_00447eb4(&local_70,&local_88,0,(ulong)(param_1[0x10] - param_1[0xf]) >> 2);
      FUN_0047e89c(&local_a0,&DAT_00ca4b00,&local_70,PTR_DAT_00c9a8a0,0x14,0,0,0);
      plVar8 = plStack_98;
      uVar5 = local_a0;
                    /* try { // try from 00abfb88 to 00bbfb8f has its CatchHandler @ 00ac00fc */
      plVar7 = *(long **)(param_2 + 0x70);
                    /* try { // try from 00abfb90 to 00bbfb9f has its CatchHandler @ 00ac007c */
      local_a0 = 0;
      plStack_98 = (long *)0x0;
      *(long **)(param_2 + 0x70) = plVar8;
      *(undefined8 *)(param_2 + 0x68) = uVar5;
      if ((plVar7 != (long *)0x0) &&
         (lVar4 = FUN_00c538e0(0xffffffffffffffff,plVar7 + 1), lVar4 == 0)) {
                    /* try { // try from 00abfbb8 to 00bbfbbf has its CatchHandler @ 00ac0064 */
        (**(code **)(*plVar7 + 0x10))(plVar7);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
      }
      plVar8 = plStack_98;
      if ((plStack_98 != (long *)0x0) &&
         (lVar4 = FUN_00c538e0(0xffffffffffffffff,plStack_98 + 1), lVar4 == 0)) {
        (**(code **)(*plVar8 + 0x10))(plVar8);
                    /* try { // try from 00abfe5c to 00bbfe6f has its CatchHandler @ 00ac013c */
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
      }
      if ((local_70 & 1) != 0) {
        _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT22(uStack_5e,CONCAT11(uStack_5f,cStack_60))));
                    /* try { // try from 00abfe78 to 00bbfe83 has its CatchHandler @ 00abff80 */
      }
                    /* try { // try from 00abfbe8 to 00bbfc33 has its CatchHandler @ 00ac0164 */
      if ((local_88 & 1) != 0) {
        _ZdlPv((void *)CONCAT44(uStack_74,uStack_78));
                    /* try { // try from 00abfe84 to 00bbfebf has its CatchHandler @ 00abf53c */
      }
      if ((local_c0 & 1) != 0) {
        _ZdlPv((void *)CONCAT62(uStack_ae,CONCAT11(uStack_af,local_b0)));
      }
      local_70 = 0x26;
      uStack_5f = 0x6e;
      uStack_5e = 0x6d69;
      uStack_67 = (undefined7)s_medal_get002_maanim_002afebe._8_8_;
      cStack_60 = SUB81(s_medal_get002_maanim_002afebe._8_8_,7);
      local_6f[0] = s_medal_get002_maanim_002afebe[0];
      local_6f[1] = s_medal_get002_maanim_002afebe[1];
      local_6f[2] = s_medal_get002_maanim_002afebe[2];
      local_6f[3] = s_medal_get002_maanim_002afebe[3];
      local_6f[4] = s_medal_get002_maanim_002afebe[4];
      local_6f[5] = s_medal_get002_maanim_002afebe[5];
      local_6f[6] = s_medal_get002_maanim_002afebe[6];
      local_6f[7] = s_medal_get002_maanim_002afebe[7];
      uStack_5c = uStack_5c & 0xffffff00;
      FUN_0046e930(param_1 + 0x2a,&local_70);
    }
                    /* try { // try from 00abfdac to 00bbfdb7 has its CatchHandler @ 00abff9c */
    if ((local_70 & 1) != 0) {
      _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT22(uStack_5e,CONCAT11(uStack_5f,cStack_60))));
    }
  }
                    /* try { // try from 00abfdb8 to 00bbfdd3 has its CatchHandler @ 00abff84 */
  if (*(long *)(lVar1 + 0x28) == local_58) {
    return;
  }
LAB_00ac01a4:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
