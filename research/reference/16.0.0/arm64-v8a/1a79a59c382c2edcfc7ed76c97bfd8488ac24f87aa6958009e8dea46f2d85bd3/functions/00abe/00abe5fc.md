# 00abe5fc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00abe5fc",
  "name": "FUN_00abe5fc",
  "size": 3076,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3e40edee83c71ba6297c0e01fa03196828528eaabb177b3622e4211584cf348a",
  "source_text_sha256": "3e40edee83c71ba6297c0e01fa03196828528eaabb177b3622e4211584cf348a"
}
~~~

## 呼び出し元

- [00ac0258](../00ac0/00ac0258.md)
- [00ac30c4](../00ac3/00ac30c4.md)

## 呼び出し先

- [0043bb64](../0043b/0043bb64.md)
- [004428f0](../00442/004428f0.md)
- [00447eb4](../00447/00447eb4.md)
- [0046c984](../0046c/0046c984.md)
- [0047e5cc](../0047e/0047e5cc.md)
- [004945d0](../00494/004945d0.md)
- [005d8b88](../005d8/005d8b88.md)
- [008514b8](../00851/008514b8.md)
- [008b6fa8](../008b6/008b6fa8.md)
- [008b7904](../008b7/008b7904.md)
- [00a46704](../00a46/00a46704.md)
- [00abd0e0](../00abd/00abd0e0.md)
- [00ac0de8](../00ac0/00ac0de8.md)
- [00ac1ad4](../00ac1/00ac1ad4.md)
- [00ac1b3c](../00ac1/00ac1b3c.md)
- [00ac1b40](../00ac1/00ac1b40.md)
- [00c538e0](../00c53/00c538e0.md)
- [00c53b3c](../00c53/00c53b3c.md)
- [00c57a30](../00c57/00c57a30.md)
- [00c57a50](../00c57/00c57a50.md)
- [00c57a70](../00c57/00c57a70.md)
- [00c57a80](../00c57/00c57a80.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c58050](../00c58/00c58050.md)
- [00c58210](../00c58/00c58210.md)

## 関連文字列（未確認候補）

~~~text
"map::at:  key not found"
"medal_%03d.png"
"medal_001.imgcut"
"medal_lost_000.imgcut"
"medal_lost_000.png"
"medal_unknown_%03d.png"
"medal_unknown_000.imgcut"
~~~

## 疑似コード / UTF-8 18471 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00abe5fc(long *param_1,int param_2)

{
  long *plVar1;
  undefined *puVar2;
  undefined *puVar3;
  ulong *puVar4;
  wchar_t *pwVar5;
  long lVar6;
  wchar_t __c;
  int iVar7;
  long lVar8;
  undefined8 uVar9;
  ulong uVar10;
  long *plVar11;
  bool bVar12;
  int iVar13;
  int iVar14;
  long lVar15;
  long lVar16;
  wchar_t *pwVar17;
  long lVar18;
  ulong uVar19;
  undefined ***pppuVar20;
  undefined8 uVar21;
  int iVar22;
  char *pcVar23;
  ulong uVar24;
  long *plVar25;
  long *plVar26;
  long *plVar27;
  long *plVar28;
  int iVar29;
  long lVar30;
  long *plVar31;
  char *pcVar32;
  ulong local_100;
  long *plStack_f8;
  char *local_f0;
  long *local_e0;
  undefined1 local_d1;
  undefined6 local_d0;
  undefined1 uStack_ca;
  undefined1 uStack_c9;
  long *local_c8 [2];
  uint local_b8;
  undefined4 uStack_b4;
  ulong local_b0;
  long *plStack_a8;
  undefined **local_a0;
  long *plStack_98;
  ulong local_90;
  undefined ***local_80;
  long local_70;
  
                    /* catch() { ... } // from try @ 00abe57c with catch @ 00abe600 */
  lVar8 = tpidr_el0;
  local_70 = *(long *)(lVar8 + 0x28);
                    /* catch() { ... } // from try @ 00abe494 with catch @ 00abe638 */
  if (DAT_00ca4578 == 0) {
    lVar15 = 0;
  }
  else {
    lVar15 = __dynamic_cast(DAT_00ca4578,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65a58,
                            &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c8cef8,0);
  }
  lVar16 = FUN_008514b8();
  FUN_008b7904(lVar16 + 0x2f38,0x136);
  lVar16 = FUN_008514b8();
  FUN_008b7904(lVar16 + 0x2f38,0x137);
  lVar16 = FUN_008514b8();
  FUN_008b7904(lVar16 + 0x2f38,0x138);
  lVar16 = FUN_008514b8();
  FUN_008b7904(lVar16 + 0x2f38,0x139);
  lVar16 = FUN_008514b8();
  FUN_008b7904(lVar16 + 0x2f38,0x13a);
  lVar16 = FUN_008514b8();
  FUN_008b7904(lVar16 + 0x2f38,0x13b);
  lVar16 = FUN_008514b8();
  FUN_008b7904(lVar16 + 0x2f38,0x13c);
  lVar16 = FUN_008514b8();
  FUN_008b7904(lVar16 + 0x2f38,0x13d);
  lVar16 = FUN_008514b8();
  FUN_008b7904(lVar16 + 0x2f38,0x13e);
  lVar16 = FUN_008514b8();
  FUN_008b7904(lVar16 + 0x2f38,0x13f);
  lVar16 = FUN_008514b8();
  FUN_008b7904(lVar16 + 0x2f38,0x140);
  lVar16 = FUN_008514b8();
  FUN_008b7904(lVar16 + 0x2f38,0x141);
  lVar16 = FUN_008514b8();
  FUN_008b7904(lVar16 + 0x2f38,0x142);
  lVar16 = FUN_008514b8();
  FUN_008b7904(lVar16 + 0x2f38,0x143);
  lVar16 = FUN_008514b8();
  FUN_008b7904(lVar16 + 0x2f38,0x144);
  lVar16 = FUN_008514b8();
  FUN_008b7904(lVar16 + 0x2f38,0x145);
  lVar16 = FUN_008514b8();
  FUN_008b7904(lVar16 + 0x2f38,0x146);
  lVar16 = FUN_008514b8();
  FUN_008b7904(lVar16 + 0x2f38,0x147);
  lVar16 = FUN_008514b8();
  FUN_008b7904(lVar16 + 0x2f38,0x148);
  lVar16 = FUN_008514b8();
  FUN_008b7904(lVar16 + 0x2f38,0x149);
  plVar11 = _UNK_002c2268;
  uVar10 = _DAT_002c2260;
  pcVar32 = (char *)((ulong)&local_e0 | 1);
  plVar1 = param_1 + 10;
  lVar16 = 0;
  pcVar23 = (char *)((ulong)local_c8 | 1);
  puVar2 = PTR_DAT_00c9af70 + 0x10;
  puVar3 = PTR_DAT_00c9af68 + 0x10;
LAB_00abe828:
  lVar30 = 0;
  iVar22 = (int)lVar16 * 5;
  iVar7 = (int)lVar16 * 0x75;
LAB_00abe880:
  iVar29 = (int)lVar30;
  uVar24 = (ulong)(param_2 * 0x14 + iVar22 + iVar29);
  if (uVar24 < (ulong)(param_1[1] - *param_1 >> 3)) {
    if ((ulong)(param_1[4] - param_1[3] >> 3) <= uVar24) {
      if (*(long *)(lVar8 + 0x28) == local_70) {
        FUN_00ac1ad4(param_1 + 3);
LAB_00abf16c:
        if (*(long *)(lVar8 + 0x28) == local_70) {
          FUN_00ac0de8(param_1);
LAB_00abf188:
          if (*(long *)(lVar8 + 0x28) == local_70) {
            uVar21 = FUN_00ac0de8(param_1);
            if (((ulong)local_c8[0] & 1) != 0) {
              _ZdlPv((void *)CONCAT44(uStack_b4,local_b8));
            }
            if (((ulong)local_e0 & 1) != 0) {
              _ZdlPv((void *)CONCAT17(uStack_c9,CONCAT16(uStack_ca,local_d0)));
            }
            if (*(long *)(lVar8 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
              FUN_00c53b3c(uVar21);
            }
          }
        }
      }
      goto LAB_00abf2b0;
    }
    __c = *(wchar_t *)(param_1[3] + uVar24 * 8);
    if (__c != L'\xffffffff') {
      pwVar5 = (wchar_t *)param_1[7];
      pwVar17 = wmemchr((wchar_t *)param_1[6],__c,(long)pwVar5 - param_1[6] >> 2);
      if (pwVar17 != (wchar_t *)0x0) {
        pwVar5 = pwVar17;
      }
      puVar4 = (ulong *)(lVar15 + 0x2e0 + lVar16 * 0x50 + lVar30 * 0x10);
      if (pwVar5 != (wchar_t *)param_1[7]) {
        if (((DAT_00ca4b38 & 1) == 0) && (iVar14 = __cxa_guard_acquire(&DAT_00ca4b38), iVar14 != 0))
        {
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
        local_e0 = (long *)CONCAT71(local_e0._1_7_,0x1c);
        uVar21 = CONCAT62(s_medal__03d_png_002bb807._8_6_,s_medal__03d_png_002bb807._6_2_);
        local_d1 = 0;
        *(ulong *)pcVar32 =
             CONCAT26(s_medal__03d_png_002bb807._6_2_,s_medal__03d_png_002bb807._0_6_);
        *(undefined8 *)(pcVar32 + 6) = uVar21;
        FUN_00447eb4(local_c8,&local_e0,0,__c);
        uVar21 = s_medal_001_imgcut_002bcaae._0_8_;
        local_f0._0_2_ = (ushort)(byte)local_f0;
        local_100 = CONCAT71(local_100._1_7_,0x20);
        *(undefined8 *)((char *)((ulong)&local_100 | 1) + 8) = s_medal_001_imgcut_002bcaae._8_8_;
        *(undefined8 *)((ulong)&local_100 | 1) = uVar21;
        FUN_0047e5cc(&local_b0,&DAT_00ca4b00,local_c8,&local_100,0x2601);
        plVar25 = plStack_a8;
        uVar24 = local_b0;
        local_b0 = 0;
        plStack_a8 = (long *)0x0;
        plVar31 = (long *)puVar4[1];
        puVar4[1] = (ulong)plVar25;
        *puVar4 = uVar24;
        plVar25 = plStack_a8;
        if ((plVar31 != (long *)0x0) &&
           (lVar18 = FUN_00c538e0(0xffffffffffffffff,plVar31 + 1), plVar25 = plStack_a8, lVar18 == 0
           )) {
          (**(code **)(*plVar31 + 0x10))(plVar31);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar31);
          plVar25 = plStack_a8;
        }
        plStack_a8 = plVar25;
        if ((plVar25 != (long *)0x0) &&
           (lVar18 = FUN_00c538e0(0xffffffffffffffff,plVar25 + 1), lVar18 == 0)) {
          (**(code **)(*plVar25 + 0x10))(plVar25);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar25);
        }
        if ((local_100 & 1) != 0) {
          _ZdlPv(local_f0);
        }
        if (((ulong)local_c8[0] & 1) != 0) {
          _ZdlPv((void *)CONCAT44(uStack_b4,local_b8));
        }
        if (((ulong)local_e0 & 1) != 0) {
          _ZdlPv((void *)CONCAT17(uStack_c9,CONCAT16(uStack_ca,local_d0)));
        }
        plVar31 = (long *)*plVar1;
        plVar25 = plVar31;
        if (plVar31 == (long *)0x0) goto LAB_00abeeb4;
        do {
          plVar27 = plVar31;
          if (*(wchar_t *)((long)plVar25 + 0x1c) <= __c) {
            plVar26 = plVar31;
            if (__c <= *(wchar_t *)((long)plVar25 + 0x1c)) goto LAB_00abec5c;
            plVar25 = plVar25 + 1;
          }
          plVar25 = (long *)*plVar25;
        } while (plVar25 != (long *)0x0);
        goto LAB_00abec98;
      }
      uVar24 = (ulong)__c;
      if ((ulong)(param_1[1] - *param_1 >> 3) <= uVar24) goto LAB_00abf16c;
      uVar19 = FUN_00abd0e0(*(undefined8 *)(*param_1 + uVar24 * 8));
      if ((uVar19 & 1) == 0) {
        if (((DAT_00ca4b38 & 1) == 0) && (iVar14 = __cxa_guard_acquire(&DAT_00ca4b38), iVar14 != 0))
        {
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
        uVar9 = s_medal_lost_000_png_002af1d8._8_8_;
        uVar21 = s_medal_lost_000_png_002af1d8._0_8_;
        local_b8 = local_b8 & 0xffffff;
        local_c8[0] = (long *)CONCAT71(local_c8[0]._1_7_,0x24);
        uStack_ca = 0;
        pcVar23[0x10] = 'n';
        pcVar23[0x11] = 'g';
        *(undefined8 *)(pcVar23 + 8) = uVar9;
        *(undefined8 *)pcVar23 = uVar21;
        uVar9 = s_medal_lost_000_imgcut_002bf6af._0_8_;
        uVar21 = CONCAT53(s_medal_lost_000_imgcut_002bf6af._16_5_,
                          s_medal_lost_000_imgcut_002bf6af._13_3_);
        local_e0 = (long *)CONCAT71(local_e0._1_7_,0x2a);
        *(ulong *)(pcVar32 + 8) =
             CONCAT35(s_medal_lost_000_imgcut_002bf6af._13_3_,s_medal_lost_000_imgcut_002bf6af._8_5_
                     );
        *(undefined8 *)pcVar32 = uVar9;
        *(undefined8 *)(pcVar32 + 0xd) = uVar21;
        FUN_0047e5cc(&local_100,&DAT_00ca4b00,local_c8,&local_e0,0x2601);
        plVar25 = plStack_f8;
        uVar24 = local_100;
        local_100 = 0;
        plStack_f8 = (long *)0x0;
        plVar31 = (long *)puVar4[1];
        puVar4[1] = (ulong)plVar25;
        *puVar4 = uVar24;
        plVar25 = plStack_f8;
        if ((plVar31 != (long *)0x0) &&
           (lVar18 = FUN_00c538e0(0xffffffffffffffff,plVar31 + 1), plVar25 = plStack_f8, lVar18 == 0
           )) {
          (**(code **)(*plVar31 + 0x10))(plVar31);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar31);
          plVar25 = plStack_f8;
        }
        plStack_f8 = plVar25;
        if ((plVar25 != (long *)0x0) &&
           (lVar18 = FUN_00c538e0(0xffffffffffffffff,plVar25 + 1), lVar18 == 0)) {
          (**(code **)(*plVar25 + 0x10))(plVar25);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar25);
        }
        if (((ulong)local_e0 & 1) != 0) {
          _ZdlPv((void *)CONCAT17(uStack_c9,CONCAT16(uStack_ca,local_d0)));
        }
        if (((ulong)local_c8[0] & 1) != 0) {
          _ZdlPv((void *)CONCAT44(uStack_b4,local_b8));
        }
      }
      else {
        if (((DAT_00ca4b38 & 1) == 0) && (iVar14 = __cxa_guard_acquire(&DAT_00ca4b38), iVar14 != 0))
        {
                    /* try { // try from 00abf078 to 00bbf1d3 has its CatchHandler @ 00abf078
                       catch() { ... } // from try @ 00abf078 with catch @ 00abf078
                       catch() { ... } // from try @ 00abf1dc with catch @ 00abf078
                       catch() { ... } // from try @ 00abf348 with catch @ 00abf078 */
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
        uVar9 = s_medal_unknown__03d_png_002b0366._0_8_;
        lVar18 = *param_1;
        lVar6 = param_1[1];
        uStack_c9 = 0;
        local_e0 = (long *)CONCAT71(local_e0._1_7_,0x2c);
        uVar21 = CONCAT62(s_medal_unknown__03d_png_002b0366._16_6_,
                          s_medal_unknown__03d_png_002b0366._14_2_);
        *(ulong *)(pcVar32 + 8) =
             CONCAT26(s_medal_unknown__03d_png_002b0366._14_2_,
                      s_medal_unknown__03d_png_002b0366._8_6_);
        *(undefined8 *)pcVar32 = uVar9;
        *(undefined8 *)(pcVar32 + 0xe) = uVar21;
        if ((ulong)(lVar6 - lVar18 >> 3) <= uVar24) goto LAB_00abf188;
        FUN_00447eb4(local_c8,&local_e0,0,*(undefined4 *)(*(long *)(lVar18 + uVar24 * 8) + 0x48));
        local_f0 = (char *)_Znwm(0x20);
        uVar9 = s_medal_unknown_000_imgcut_002adfb5._16_8_;
        uVar21 = s_medal_unknown_000_imgcut_002adfb5._0_8_;
        plStack_f8 = plVar11;
        local_100 = uVar10;
        *(undefined8 *)(local_f0 + 8) = s_medal_unknown_000_imgcut_002adfb5._8_8_;
        *(undefined8 *)local_f0 = uVar21;
        *(undefined8 *)(local_f0 + 0x10) = uVar9;
        local_f0[0x18] = '\0';
        FUN_0047e5cc(&local_b0,&DAT_00ca4b00,local_c8,&local_100,0x2601);
        plVar25 = plStack_a8;
        uVar24 = local_b0;
        local_b0 = 0;
        plStack_a8 = (long *)0x0;
        plVar31 = (long *)puVar4[1];
        puVar4[1] = (ulong)plVar25;
        *puVar4 = uVar24;
        plVar25 = plStack_a8;
        if ((plVar31 != (long *)0x0) &&
           (lVar18 = FUN_00c538e0(0xffffffffffffffff,plVar31 + 1), plVar25 = plStack_a8, lVar18 == 0
           )) {
          (**(code **)(*plVar31 + 0x10))(plVar31);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar31);
          plVar25 = plStack_a8;
        }
        plStack_a8 = plVar25;
        if ((plVar25 != (long *)0x0) &&
           (lVar18 = FUN_00c538e0(0xffffffffffffffff,plVar25 + 1), lVar18 == 0)) {
          (**(code **)(*plVar25 + 0x10))(plVar25);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar25);
        }
        if ((local_100 & 1) != 0) {
          _ZdlPv(local_f0);
        }
        if (((ulong)local_c8[0] & 1) != 0) {
          _ZdlPv((void *)CONCAT44(uStack_b4,local_b8));
        }
        if (((ulong)local_e0 & 1) != 0) {
          _ZdlPv((void *)CONCAT17(uStack_c9,CONCAT16(uStack_ca,local_d0)));
        }
      }
      goto LAB_00abeeb4;
    }
  }
  goto LAB_00abe818;
LAB_00abec5c:
  if (__c < *(wchar_t *)((long)plVar26 + 0x1c)) {
    plVar26 = (long *)*plVar26;
  }
  else {
    if (__c <= *(wchar_t *)((long)plVar26 + 0x1c)) goto LAB_00abec78;
    plVar26 = (long *)plVar26[1];
  }
  if (plVar26 == (long *)0x0) goto LAB_00abf130;
  goto LAB_00abec5c;
LAB_00abec78:
  if ((int)plVar26[4] == 1) {
    do {
      while (plVar25 = plVar31, *(wchar_t *)((long)plVar25 + 0x1c) <= __c) {
        if (__c <= *(wchar_t *)((long)plVar25 + 0x1c)) goto LAB_00abeeac;
        plVar31 = (long *)plVar25[1];
        if ((long *)plVar25[1] == (long *)0x0) {
          plVar27 = plVar25 + 1;
          goto LAB_00abee58;
        }
      }
      plVar31 = (long *)*plVar25;
      plVar27 = plVar25;
    } while ((long *)*plVar25 != (long *)0x0);
LAB_00abee58:
    plVar31 = (long *)_Znwm(0x28);
    *(wchar_t *)((long)plVar31 + 0x1c) = __c;
    *(undefined4 *)(plVar31 + 4) = 0;
    *plVar31 = 0;
    plVar31[1] = 0;
    plVar31[2] = (long)plVar25;
    *plVar27 = (long)plVar31;
    plVar25 = plVar31;
    if (*(long *)param_1[9] != 0) {
      param_1[9] = *(long *)param_1[9];
      plVar25 = (long *)*plVar27;
    }
    FUN_0043bb64(param_1[10],plVar25);
    param_1[0xb] = param_1[0xb] + 1;
    plVar25 = plVar31;
LAB_00abeeac:
    *(undefined4 *)(plVar25 + 4) = 2;
  }
  else {
LAB_00abec98:
    do {
      if (*(wchar_t *)((long)plVar27 + 0x1c) <= __c) {
        plVar25 = plVar31;
        if (__c <= *(wchar_t *)((long)plVar27 + 0x1c)) goto LAB_00abecb8;
        plVar27 = plVar27 + 1;
      }
      plVar27 = (long *)*plVar27;
    } while (plVar27 != (long *)0x0);
  }
LAB_00abeeb4:
  FUN_008514b8();
  iVar13 = FUN_0046c984();
  iVar14 = iVar13 + -0x3bf;
  if (0x3bf < iVar13) {
    iVar14 = iVar13 + -0x3c0;
  }
  iVar14 = iVar29 * 0x87 + (iVar14 >> 1);
  FUN_00a46704(local_c8,puVar4,iVar14 + 0xd2,iVar7 + 0x93,0);
  (**(code **)(*local_c8[0] + 0x10))(local_c8[0],1);
  lVar18 = FUN_008514b8();
  local_e0 = local_c8[0];
  local_c8[0] = (long *)0x0;
  local_a0 = &PTR_FUN_00c8cf20;
  local_80 = &local_a0;
  plStack_98 = param_1;
  local_90 = (ulong)(uint)__c;
  FUN_008b6fa8(lVar18 + 0x2f38,iVar22 + 0x136 + iVar29,iVar14 + 0x9b,iVar7 + 0x5c,0x6e,0x6e,
               &local_e0,&local_a0);
  if (local_80 == &local_a0) {
    pppuVar20 = &local_a0;
    lVar18 = 0x20;
  }
  else {
    if (local_80 == (undefined ***)0x0) goto LAB_00abef80;
    lVar18 = 0x28;
    pppuVar20 = local_80;
  }
  (**(code **)((long)*pppuVar20 + lVar18))();
LAB_00abef80:
  plVar25 = local_e0;
  local_e0 = (long *)0x0;
  if (plVar25 != (long *)0x0) {
    *plVar25 = (long)(PTR_DAT_00c9af68 + 0x10);
    FUN_005d8b88(plVar25 + 10);
    _ZdlPv(plVar25);
  }
  plVar25 = local_c8[0];
  local_c8[0] = (long *)0x0;
  if (plVar25 != (long *)0x0) {
    plVar31 = (long *)plVar25[0x16];
    *plVar25 = (long)puVar2;
    if ((plVar31 != (long *)0x0) &&
       (lVar18 = FUN_00c538e0(0xffffffffffffffff,plVar31 + 1), lVar18 == 0)) {
      (**(code **)(*plVar31 + 0x10))(plVar31);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar31);
    }
    *plVar25 = (long)puVar3;
    FUN_005d8b88(plVar25 + 10);
    _ZdlPv(plVar25);
  }
  lVar30 = lVar30 + 1;
  if (lVar30 == 5) goto LAB_00abe818;
  goto LAB_00abe880;
LAB_00abecb8:
  if (__c < *(wchar_t *)((long)plVar25 + 0x1c)) {
    plVar25 = (long *)*plVar25;
  }
  else {
    if (__c <= *(wchar_t *)((long)plVar25 + 0x1c)) goto LAB_00abed00;
    plVar25 = (long *)plVar25[1];
  }
  if (plVar25 == (long *)0x0) goto LAB_00abf130;
  goto LAB_00abecb8;
LAB_00abed00:
  plVar27 = plVar1;
  plVar26 = plVar31;
  if ((int)plVar25[4] == 2) {
    do {
      if (__c <= *(wchar_t *)((long)plVar26 + 0x1c)) {
        plVar27 = plVar26;
      }
      plVar25 = plVar26 + (*(wchar_t *)((long)plVar26 + 0x1c) < __c);
      plVar26 = (long *)*plVar25;
    } while ((long *)*plVar25 != (long *)0x0);
    if ((plVar27 != plVar1) && (*(wchar_t *)((long)plVar27 + 0x1c) <= __c)) {
      plVar25 = plVar27;
      plVar26 = (long *)plVar27[1];
      if ((long *)plVar27[1] == (long *)0x0) {
        do {
          plVar28 = (long *)plVar25[2];
          bVar12 = (long *)*plVar28 != plVar25;
          plVar25 = plVar28;
        } while (bVar12);
      }
      else {
        do {
          plVar28 = plVar26;
          plVar26 = (long *)*plVar28;
        } while ((long *)*plVar28 != (long *)0x0);
      }
      if ((long *)param_1[9] == plVar27) {
        param_1[9] = (long)plVar28;
      }
      param_1[0xb] = param_1[0xb] + -1;
      FUN_004945d0(plVar31,plVar27);
      _ZdlPv(plVar27);
    }
  }
  goto LAB_00abeeb4;
LAB_00abf130:
  if (*(long *)(lVar8 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
    FUN_004428f0("map::at:  key not found");
  }
  goto LAB_00abf2b0;
LAB_00abe818:
  lVar16 = lVar16 + 1;
  if (lVar16 == 4) {
    if (*(long *)(lVar8 + 0x28) == local_70) {
      return;
    }
LAB_00abf2b0:
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  goto LAB_00abe828;
}

~~~
