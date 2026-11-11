# 00abfaa8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00abfaa8",
  "name": "FUN_00abfaa8",
  "size": 2064,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f6f9f5ffafb5cc0f8c8edcc51c21bd31d81a6506685cac76ffcea283ce299dc8",
  "source_text_sha256": "f6f9f5ffafb5cc0f8c8edcc51c21bd31d81a6506685cac76ffcea283ce299dc8"
}
~~~

## 呼び出し元

- [00abf784](../00abf/00abf784.md)
- [00b3cad8](../00b3c/00b3cad8.md)

## 呼び出し先

- [0043bb20](../0043b/0043bb20.md)
- [00447ef4](../00447/00447ef4.md)
- [0046e970](../0046e/0046e970.md)
- [0047e60c](../0047e/0047e60c.md)
- [0047e8dc](../0047e/0047e8dc.md)
- [0048ce54](../0048c/0048ce54.md)
- [00492e08](../00492/00492e08.md)
- [0049f3f0](../0049f/0049f3f0.md)
- [00ac0fe4](../00ac0/00ac0fe4.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c53f5c](../00c53/00c53f5c.md)
- [00c57e30](../00c57/00c57e30.md)
- [00c57e50](../00c57/00c57e50.md)
- [00c57e70](../00c57/00c57e70.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)

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

## 疑似コード / UTF-8 18610 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void FUN_00abfaa8(long *param_1,long param_2)

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
    if (((DAT_00ca4f38 & 1) == 0) && (iVar3 = __cxa_guard_acquire(&DAT_00ca4f38), iVar3 != 0)) {
      DAT_00ca4f08 = 0;
      DAT_00ca4f00 = &DAT_00ca4f08;
      DAT_00ca4f28 = 0;
      DAT_00ca4f30 = 0;
                    /* catch() { ... } // from try @ 00ac0014 with catch @ 00ac011c */
      DAT_00ca4f20 = 0;
                    /* catch() { ... } // from try @ 00abff54 with catch @ 00ac0120 */
      DAT_00ca4f10 = 0;
      DAT_00ca4f18 = &DAT_00ca4f20;
      __cxa_atexit(FUN_0047edb4,&DAT_00ca4f00,&PTR_LOOP_00c62f90);
      __cxa_guard_release(&DAT_00ca4f38);
    }
                    /* try { // try from 00abfaf8 to 00bbfaff has its CatchHandler @ 00ac0234 */
    local_70 = 0x20;
    local_88 = 0x26;
    uStack_67 = (undefined7)s_medal_get000_png_002ab9a4._8_8_;
    cStack_60 = SUB81(s_medal_get000_png_002ab9a4._8_8_,7);
    local_6f[0] = s_medal_get000_png_002ab9a4[0];
    local_6f[1] = s_medal_get000_png_002ab9a4[1];
    local_6f[2] = s_medal_get000_png_002ab9a4[2];
    local_6f[3] = s_medal_get000_png_002ab9a4[3];
    local_6f[4] = s_medal_get000_png_002ab9a4[4];
    local_6f[5] = s_medal_get000_png_002ab9a4[5];
    local_6f[6] = s_medal_get000_png_002ab9a4[6];
    local_6f[7] = s_medal_get000_png_002ab9a4[7];
                    /* try { // try from 00abfb28 to 00bbfb33 has its CatchHandler @ 00ac022c */
    uStack_5f = 0;
    uStack_7f = (undefined6)s_medal_get000_imgcut_002adb15._8_8_;
    cStack_79 = SUB81(s_medal_get000_imgcut_002adb15._8_8_,6);
    uStack_78 = CONCAT31(0x747563,SUB81(s_medal_get000_imgcut_002adb15._8_8_,7));
    local_87 = (undefined6)s_medal_get000_imgcut_002adb15._0_8_;
    uStack_81 = SUB82(s_medal_get000_imgcut_002adb15._0_8_,6);
                    /* try { // try from 00abfb34 to 00bbfb37 has its CatchHandler @ 00ac0298 */
    uStack_74 = uStack_74 & 0xffffff00;
    FUN_0047e60c(&local_c0,&DAT_00ca4f00,&local_70,&local_88,0x2601);
    uVar2 = CONCAT44(uStack_b4,CONCAT13(cStack_b5,CONCAT21(uStack_b7,cStack_b8)));
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
                    /* try { // try from 00abfb6c to 00bbfb8b has its CatchHandler @ 00ac0300 */
    if ((plVar8 == (long *)0x0) || (lVar4 = FUN_00c53d00(0xffffffffffffffff,plVar8 + 1), lVar4 != 0)
       ) {
      plVar8 = (long *)CONCAT44(uStack_b4,CONCAT13(cStack_b5,CONCAT21(uStack_b7,cStack_b8)));
    }
    else {
      (**(code **)(*plVar8 + 0x10))(plVar8);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
      plVar8 = (long *)CONCAT44(uStack_b4,CONCAT13(cStack_b5,CONCAT21(uStack_b7,cStack_b8)));
    }
    if ((plVar8 != (long *)0x0) &&
       (lVar4 = FUN_00c53d00(0xffffffffffffffff,(long *)((long)plVar8 + 8)), lVar4 == 0)) {
                    /* try { // try from 00abfbdc to 00bbfbdf has its CatchHandler @ 00ac029c */
      (**(code **)(*plVar8 + 0x10))(plVar8);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
    }
    if ((local_88 & 1) != 0) {
      _ZdlPv((void *)CONCAT44(uStack_74,uStack_78));
    }
                    /* try { // try from 00abfba0 to 00bbfba7 has its CatchHandler @ 00ac026c */
    if ((local_70 & 1) != 0) {
      _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT22(uStack_5e,CONCAT11(uStack_5f,cStack_60))));
    }
                    /* catch() { ... } // from try @ 00abff48 with catch @ 00ac0138 */
    if (((DAT_00ca4f38 & 1) == 0) && (iVar3 = __cxa_guard_acquire(&DAT_00ca4f38), iVar3 != 0)) {
                    /* catch() { ... } // from try @ 00abff10 with catch @ 00ac0150 */
                    /* catch() { ... } // from try @ 00abffbc with catch @ 00ac0154 */
      DAT_00ca4f08 = 0;
                    /* catch() { ... } // from try @ 00abffb0 with catch @ 00ac015c */
                    /* catch() { ... } // from try @ 00abfea8 with catch @ 00ac0160 */
      DAT_00ca4f00 = &DAT_00ca4f08;
      DAT_00ca4f28 = 0;
      DAT_00ca4f30 = 0;
      DAT_00ca4f20 = 0;
                    /* catch() { ... } // from try @ 00abfe5c with catch @ 00ac0174 */
      DAT_00ca4f10 = 0;
      DAT_00ca4f18 = &DAT_00ca4f20;
                    /* catch() { ... } // from try @ 00abfe50 with catch @ 00ac0178 */
      __cxa_atexit(FUN_0047edb4,&DAT_00ca4f00,&PTR_LOOP_00c62f90);
                    /* catch() { ... } // from try @ 00abfe1c with catch @ 00ac0180 */
                    /* catch() { ... } // from try @ 00abf7f8 with catch @ 00ac0184 */
      __cxa_guard_release(&DAT_00ca4f38);
    }
                    /* try { // try from 00abfc1c to 00bbfc9b has its CatchHandler @ 00ac02d4 */
    local_88 = 0x1c;
    plVar8 = param_1 + 0xf;
    cStack_79 = 0;
    local_87._0_1_ = s_medal__03d_png_002bb847[0];
    local_87._1_1_ = s_medal__03d_png_002bb847[1];
    local_87._2_1_ = s_medal__03d_png_002bb847[2];
    local_87._3_1_ = s_medal__03d_png_002bb847[3];
    local_87._4_1_ = s_medal__03d_png_002bb847[4];
    local_87._5_1_ = s_medal__03d_png_002bb847[5];
    uStack_81._0_1_ = s_medal__03d_png_002bb847[6];
    uStack_81._1_1_ = s_medal__03d_png_002bb847[7];
    uStack_7f._0_1_ = s_medal__03d_png_002bb847[8];
    uStack_7f._1_1_ = s_medal__03d_png_002bb847[9];
    uStack_7f._2_1_ = s_medal__03d_png_002bb847[10];
    uStack_7f._3_1_ = s_medal__03d_png_002bb847[0xb];
    uStack_7f._4_1_ = s_medal__03d_png_002bb847[0xc];
    uStack_7f._5_1_ = s_medal__03d_png_002bb847[0xd];
    if ((undefined4 *)param_1[0x10] == (undefined4 *)*plVar8) {
                    /* catch() { ... } // from try @ 00abf7dc with catch @ 00ac0190 */
      if (*(long *)(lVar1 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
        FUN_0049f3f0(plVar8);
      }
      goto LAB_00ac03a0;
    }
    FUN_00447ef4(&local_70,&local_88,0,*(undefined4 *)*plVar8);
    local_c0 = 0x20;
    uStack_af = 0;
    uStack_b7 = (undefined2)s_medal_001_imgcut_002bcaee._8_8_;
    cStack_b5 = SUB81(s_medal_001_imgcut_002bcaee._8_8_,2);
    uStack_b4 = SUB84(s_medal_001_imgcut_002bcaee._8_8_,3);
    local_b0 = SUB81(s_medal_001_imgcut_002bcaee._8_8_,7);
    uStack_bf = (undefined7)s_medal_001_imgcut_002bcaee._0_8_;
    cStack_b8 = SUB81(s_medal_001_imgcut_002bcaee._0_8_,7);
    FUN_0047e60c(&local_a0,&DAT_00ca4f00,&local_70,&local_c0,0x2601);
    plVar7 = plStack_98;
    uVar5 = local_a0;
    plVar9 = *(long **)(param_2 + 0x60);
    local_a0 = 0;
    plStack_98 = (long *)0x0;
                    /* try { // try from 00abfca4 to 00bbfcab has its CatchHandler @ 00ac029c */
    *(long **)(param_2 + 0x60) = plVar7;
    *(undefined8 *)(param_2 + 0x58) = uVar5;
    plVar7 = plStack_98;
                    /* try { // try from 00abfcac to 00bbfcbb has its CatchHandler @ 00ac0250 */
    if ((plVar9 != (long *)0x0) &&
       (lVar4 = FUN_00c53d00(0xffffffffffffffff,plVar9 + 1), plVar7 = plStack_98, lVar4 == 0)) {
      (**(code **)(*plVar9 + 0x10))(plVar9);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
                    /* try { // try from 00abfff8 to 00bc000b has its CatchHandler @ 00ac02d8 */
      plVar7 = plStack_98;
    }
    plStack_98 = plVar7;
    if ((plVar7 != (long *)0x0) &&
       (lVar4 = FUN_00c53d00(0xffffffffffffffff,(long *)((long)plVar7 + 8)), lVar4 == 0)) {
      (**(code **)(*plVar7 + 0x10))(plVar7);
                    /* try { // try from 00ac0014 to 00bc001f has its CatchHandler @ 00ac011c */
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
                    /* try { // try from 00ac0020 to 00bc005b has its CatchHandler @ 00abf6d8 */
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
                    /* catch() { ... } // from try @ 00abf9bc with catch @ 00ac01f8 */
                    /* catch() { ... } // from try @ 00abfd54 with catch @ 00ac0200 */
      if (((DAT_00ca4f38 & 1) == 0) && (iVar3 = __cxa_guard_acquire(&DAT_00ca4f38), iVar3 != 0)) {
        DAT_00ca4f08 = 0;
                    /* catch() { ... } // from try @ 00abfd2c with catch @ 00ac0218 */
        DAT_00ca4f00 = &DAT_00ca4f08;
                    /* catch() { ... } // from try @ 00abfb28 with catch @ 00ac022c */
        DAT_00ca4f28 = 0;
        DAT_00ca4f30 = 0;
        DAT_00ca4f20 = 0;
                    /* catch() { ... } // from try @ 00abfaf8 with catch @ 00ac0234 */
        DAT_00ca4f10 = 0;
        DAT_00ca4f18 = &DAT_00ca4f20;
                    /* catch() { ... } // from try @ 00abfcd4 with catch @ 00ac0238 */
        __cxa_atexit(FUN_0047edb4,&DAT_00ca4f00,&PTR_LOOP_00c62f90);
        __cxa_guard_release(&DAT_00ca4f38);
      }
      local_c0 = 0x14;
                    /* try { // try from 00abfe50 to 00bbfe5b has its CatchHandler @ 00ac0178 */
      uStack_b7 = 0x3174;
      uStack_bf = (undefined7)s_medal_txt1_002a189e._0_8_;
      cStack_b8 = SUB81(s_medal_txt1_002a189e._0_8_,7);
      cStack_b5 = 0;
                    /* try { // try from 00abfe5c to 00bbfe6f has its CatchHandler @ 00ac0174 */
      FUN_0048ce54(&local_88,&local_c0);
      if ((int *)param_1[0x10] == (int *)param_1[0xf]) {
                    /* catch() { ... } // from try @ 00abfcac with catch @ 00ac0250 */
        if (*(long *)(lVar1 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
          FUN_0049f3f0(plVar8);
        }
        goto LAB_00ac03a0;
      }
      uVar6 = (ulong)*(int *)param_1[0xf];
      if ((ulong)(param_1[1] - *param_1 >> 3) <= uVar6) {
                    /* catch() { ... } // from try @ 00abfbd0 with catch @ 00ac0264 */
                    /* catch() { ... } // from try @ 00abfba0 with catch @ 00ac026c */
                    /* catch() { ... } // from try @ 00abfa0c with catch @ 00ac0270 */
        if (*(long *)(lVar1 + 0x28) == local_58) {
          uVar5 = FUN_00ac0fe4(param_1);
          if ((local_70 & 1) != 0) {
            _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT22(uStack_5e,CONCAT11(uStack_5f,cStack_60))));
          }
          if (*(long *)(lVar1 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
            FUN_00c53f5c(uVar5);
          }
        }
        goto LAB_00ac03a0;
      }
      lVar4 = *(long *)(*param_1 + uVar6 * 8);
      if ((*(byte *)(lVar4 + 0x80) & 1) == 0) {
        uStack_d8 = *(undefined8 *)(lVar4 + 0x88);
        local_e0 = *(ulong *)(lVar4 + 0x80);
        local_d0 = *(void **)(lVar4 + 0x90);
                    /* try { // try from 00abfea8 to 00bbfeaf has its CatchHandler @ 00ac0160 */
      }
      else {
        FUN_0043bb20(&local_e0,*(undefined8 *)(lVar4 + 0x90),*(undefined8 *)(lVar4 + 0x88));
      }
      FUN_00492e08(&local_70,&local_88,&local_e0);
      FUN_0047e8dc(&local_a0,&DAT_00ca4f00,&local_70,PTR_DAT_00c9aca0,0x14,0,0,0);
      plVar8 = plStack_98;
      uVar5 = local_a0;
      plVar7 = *(long **)(param_2 + 0x70);
                    /* try { // try from 00abfefc to 00bbff0f has its CatchHandler @ 00ac02a4 */
      local_a0 = 0;
      plStack_98 = (long *)0x0;
      *(long **)(param_2 + 0x70) = plVar8;
      *(undefined8 *)(param_2 + 0x68) = uVar5;
                    /* try { // try from 00abff10 to 00bbff1b has its CatchHandler @ 00ac0150 */
      if ((plVar7 != (long *)0x0) &&
         (lVar4 = FUN_00c53d00(0xffffffffffffffff,plVar7 + 1), lVar4 == 0)) {
        (**(code **)(*plVar7 + 0x10))(plVar7);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
      }
      plVar8 = plStack_98;
      if ((plStack_98 != (long *)0x0) &&
         (lVar4 = FUN_00c53d00(0xffffffffffffffff,plStack_98 + 1), lVar4 == 0)) {
        (**(code **)(*plVar8 + 0x10))(plVar8);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
      }
      if ((local_70 & 1) != 0) {
                    /* try { // try from 00ac00b0 to 00bc0333 has its CatchHandler @ 00abf6d8 */
        _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT22(uStack_5e,CONCAT11(uStack_5f,cStack_60))));
      }
                    /* try { // try from 00abff54 to 00bbff6f has its CatchHandler @ 00ac0120 */
      if ((local_e0 & 1) != 0) {
        _ZdlPv(local_d0);
      }
      if ((local_88 & 1) != 0) {
        _ZdlPv((void *)CONCAT44(uStack_74,uStack_78));
      }
      if ((local_c0 & 1) != 0) {
        _ZdlPv((void *)CONCAT62(uStack_ae,CONCAT11(uStack_af,local_b0)));
      }
      local_70 = 0x26;
      uStack_5f = 0x6e;
      uStack_5e = 0x6d69;
                    /* try { // try from 00abff90 to 00bbffab has its CatchHandler @ 00ac02a4 */
      uStack_67 = (undefined7)s_medal_get001_maanim_002b7bbd._8_8_;
      cStack_60 = SUB81(s_medal_get001_maanim_002b7bbd._8_8_,7);
      local_6f[0] = s_medal_get001_maanim_002b7bbd[0];
      local_6f[1] = s_medal_get001_maanim_002b7bbd[1];
      local_6f[2] = s_medal_get001_maanim_002b7bbd[2];
      local_6f[3] = s_medal_get001_maanim_002b7bbd[3];
      local_6f[4] = s_medal_get001_maanim_002b7bbd[4];
      local_6f[5] = s_medal_get001_maanim_002b7bbd[5];
      local_6f[6] = s_medal_get001_maanim_002b7bbd[6];
      local_6f[7] = s_medal_get001_maanim_002b7bbd[7];
      uStack_5c = uStack_5c & 0xffffff00;
      FUN_0046e970(param_1 + 0x2a,&local_70);
    }
    else {
                    /* catch() { ... } // from try @ 00abf814 with catch @ 00ac01a4 */
      if (((DAT_00ca4f38 & 1) == 0) && (iVar3 = __cxa_guard_acquire(&DAT_00ca4f38), iVar3 != 0)) {
        DAT_00ca4f08 = 0;
        DAT_00ca4f00 = &DAT_00ca4f08;
        DAT_00ca4f28 = 0;
        DAT_00ca4f30 = 0;
        DAT_00ca4f20 = 0;
        DAT_00ca4f10 = 0;
        DAT_00ca4f18 = &DAT_00ca4f20;
        __cxa_atexit(FUN_0047edb4,&DAT_00ca4f00,&PTR_LOOP_00c62f90);
                    /* catch() { ... } // from try @ 00ac005c with catch @ 00ac01ec */
                    /* catch() { ... } // from try @ 00abf9e0 with catch @ 00ac01f0 */
        __cxa_guard_release(&DAT_00ca4f38);
      }
      local_c0 = 0x14;
                    /* try { // try from 00abfd24 to 00bbfd2b has its CatchHandler @ 00ac0298 */
      uStack_b7 = 0x3274;
      uStack_bf = (undefined7)s_medal_txt2_002a1893._0_8_;
      cStack_b8 = SUB81(s_medal_txt2_002a1893._0_8_,7);
                    /* try { // try from 00abfd2c to 00bbfd3b has its CatchHandler @ 00ac0218 */
      cStack_b5 = 0;
      FUN_0048ce54(&local_88,&local_c0);
                    /* try { // try from 00abfd54 to 00bbfd5b has its CatchHandler @ 00ac0200 */
      FUN_00447ef4(&local_70,&local_88,0,(ulong)(param_1[0x10] - param_1[0xf]) >> 2);
      FUN_0047e8dc(&local_a0,&DAT_00ca4f00,&local_70,PTR_DAT_00c9aca0,0x14,0,0,0);
      plVar8 = plStack_98;
      uVar5 = local_a0;
                    /* try { // try from 00abfd84 to 00bbfdcf has its CatchHandler @ 00ac0300 */
      plVar7 = *(long **)(param_2 + 0x70);
      local_a0 = 0;
      plStack_98 = (long *)0x0;
      *(long **)(param_2 + 0x70) = plVar8;
      *(undefined8 *)(param_2 + 0x68) = uVar5;
      if ((plVar7 != (long *)0x0) &&
         (lVar4 = FUN_00c53d00(0xffffffffffffffff,plVar7 + 1), lVar4 == 0)) {
        (**(code **)(*plVar7 + 0x10))(plVar7);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
      }
      plVar8 = plStack_98;
      if ((plStack_98 != (long *)0x0) &&
         (lVar4 = FUN_00c53d00(0xffffffffffffffff,plStack_98 + 1), lVar4 == 0)) {
        (**(code **)(*plVar8 + 0x10))(plVar8);
                    /* try { // try from 00ac005c to 00bc00af has its CatchHandler @ 00ac01ec */
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
      }
      if ((local_70 & 1) != 0) {
        _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT22(uStack_5e,CONCAT11(uStack_5f,cStack_60))));
      }
      if ((local_88 & 1) != 0) {
        _ZdlPv((void *)CONCAT44(uStack_74,uStack_78));
      }
      if ((local_c0 & 1) != 0) {
        _ZdlPv((void *)CONCAT62(uStack_ae,CONCAT11(uStack_af,local_b0)));
      }
                    /* try { // try from 00abfe10 to 00bbfe1b has its CatchHandler @ 00ac02a4 */
      local_70 = 0x26;
      uStack_5f = 0x6e;
      uStack_5e = 0x6d69;
      uStack_67 = (undefined7)s_medal_get002_maanim_002afefe._8_8_;
      cStack_60 = SUB81(s_medal_get002_maanim_002afefe._8_8_,7);
      local_6f[0] = s_medal_get002_maanim_002afefe[0];
      local_6f[1] = s_medal_get002_maanim_002afefe[1];
      local_6f[2] = s_medal_get002_maanim_002afefe[2];
      local_6f[3] = s_medal_get002_maanim_002afefe[3];
      local_6f[4] = s_medal_get002_maanim_002afefe[4];
      local_6f[5] = s_medal_get002_maanim_002afefe[5];
      local_6f[6] = s_medal_get002_maanim_002afefe[6];
      local_6f[7] = s_medal_get002_maanim_002afefe[7];
                    /* try { // try from 00abfe1c to 00bbfe23 has its CatchHandler @ 00ac0180 */
      uStack_5c = uStack_5c & 0xffffff00;
      FUN_0046e970(param_1 + 0x2a,&local_70);
    }
    if ((local_70 & 1) != 0) {
                    /* try { // try from 00abffb0 to 00bbffbb has its CatchHandler @ 00ac015c */
      _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT22(uStack_5e,CONCAT11(uStack_5f,cStack_60))));
    }
  }
                    /* try { // try from 00abffbc to 00bbffcb has its CatchHandler @ 00ac0154 */
  if (*(long *)(lVar1 + 0x28) == local_58) {
    return;
  }
LAB_00ac03a0:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
