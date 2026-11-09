# 00b0dadc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00b0dadc",
  "name": "FUN_00b0dadc",
  "size": 1328,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1da61afc67157bfad2605538d3e0866a42b8916a889d2248bf7314a9e018b78d",
  "source_text_sha256": "1da61afc67157bfad2605538d3e0866a42b8916a889d2248bf7314a9e018b78d"
}
~~~

## 呼び出し元

- [00798e60](../00798/00798e60.md)
- [007a0744](../007a0/007a0744.md)
- [00b0dadc](../00b0d/00b0dadc.md)

## 呼び出し先

- [0043bae0](../0043b/0043bae0.md)
- [0048ce14](../0048c/0048ce14.md)
- [00492dc8](../00492/00492dc8.md)
- [005da544](../005da/005da544.md)
- [00684f70](../00684/00684f70.md)
- [006875e8](../00687/006875e8.md)
- [0071ecc0](../0071e/0071ecc0.md)
- [00737c34](../00737/00737c34.md)
- [008514b8](../00851/008514b8.md)
- [00b0dadc](../00b0d/00b0dadc.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57b70](../00c57/00c57b70.md)
- [00c57b80](../00c57/00c57b80.md)
- [00c57d90](../00c57/00c57d90.md)

## 関連文字列（未確認候補）

~~~text
"NSt6__ndk110__function6__funcIZN11aDownloader8downloadERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_2NS6_ISB_EEFvbEEE"
"receive_honor_popup"
"receive_item_popup"
"receive_item_popup_chara"
"receive_item_popup_chara_evolve"
"receive_item_popup_xp"
~~~

## 疑似コード / UTF-8 12237 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00b0dadc(undefined8 *param_1,long param_2,uint param_3,int param_4,undefined4 param_5,
                 ulong param_6)

{
  undefined4 *puVar1;
  undefined *puVar2;
  undefined4 uVar3;
  int iVar4;
  undefined4 uVar5;
  long lVar6;
  undefined8 uVar7;
  undefined8 uVar8;
  undefined8 uVar9;
  undefined8 uVar10;
  undefined8 uVar11;
  void *__ptr;
  void *pvVar12;
  long lVar13;
  char *pcVar14;
  ulong uVar15;
  long lVar16;
  ulong uVar17;
  ulong local_150;
  ulong uStack_148;
  void *local_140;
  ulong local_130;
  ulong uStack_128;
  void *local_120;
  ulong local_110;
  ulong uStack_108;
  void *local_100;
  byte local_f8 [16];
  void *local_e8;
  byte local_e0 [16];
  void *local_d0;
  byte local_c8 [16];
  void *local_b8;
  ulong local_b0;
  ulong uStack_a8;
  void *local_a0;
  byte local_90;
  undefined7 uStack_8f;
  char cStack_88;
  undefined7 uStack_87;
  char local_80;
  undefined2 uStack_7f;
  undefined1 uStack_7d;
  uint uStack_7c;
  long local_78;
  
  lVar6 = tpidr_el0;
  local_78 = *(long *)(lVar6 + 0x28);
  if (param_4 < 3) {
    if (param_4 != 0) {
      if (param_4 != 1) {
        if (param_4 == 2) {
          FUN_00737c34(&local_90,param_3);
          pvVar12 = (void *)CONCAT71(uStack_8f,local_90);
          __ptr = (void *)CONCAT71(uStack_87,cStack_88);
          *param_1 = 0;
          param_1[1] = 0;
          param_1[2] = 0;
          if (__ptr != pvVar12) {
            lVar16 = 0;
            uVar17 = 0;
            puVar2 = &DAT_002bc77e;
            if ((param_6 & 1) == 0) {
              puVar2 = &DAT_002beb0e;
            }
            do {
              puVar1 = (undefined4 *)((long)pvVar12 + lVar16);
              uVar3 = *puVar1;
              iVar4 = puVar1[1];
              uVar5 = puVar1[2];
              lVar13 = FUN_008514b8();
              FUN_00b0dadc(&local_b0,(long)&DWORD_00396580 + lVar13 + (long)iVar4 * 0x40,iVar4,uVar3
                           ,uVar5,0);
              uVar15 = local_b0 >> 1 & 0x7f;
              pvVar12 = (void *)((ulong)&local_b0 | 1);
              if ((local_b0 & 1) != 0) {
                uVar15 = uStack_a8;
                pvVar12 = local_a0;
              }
              _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                        (param_1,pvVar12,uVar15);
              if ((local_b0 & 1) != 0) {
                _ZdlPv(local_a0);
              }
              __ptr = (void *)CONCAT71(uStack_8f,local_90);
              uVar15 = (CONCAT71(uStack_87,cStack_88) - (long)__ptr >> 2) * -0x5555555555555555;
              if (uVar17 < uVar15 - 1) {
                _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
                          (param_1,puVar2);
                __ptr = (void *)CONCAT71(uStack_8f,local_90);
                uVar15 = (CONCAT71(uStack_87,cStack_88) - (long)__ptr >> 2) * -0x5555555555555555;
              }
              uVar17 = uVar17 + 1;
              lVar16 = lVar16 + 0xc;
              pvVar12 = __ptr;
            } while (uVar17 < uVar15);
          }
          if (__ptr != (void *)0x0) {
            cStack_88 = (char)__ptr;
            uStack_87 = (undefined7)((ulong)__ptr >> 8);
            _ZdlPv(__ptr);
          }
          goto LAB_00b0dfa4;
        }
LAB_00b0dd9c:
        *(undefined2 *)param_1 = 0;
        goto LAB_00b0dfa4;
      }
      pcVar14 = (char *)_Znwm(0x20);
      uVar10 = _UNK_002c2268;
      uVar9 = _DAT_002c2260;
      uVar8 = s_receive_item_popup_chara_002b2009._16_8_;
      uVar7 = s_receive_item_popup_chara_002b2009._0_8_;
      local_80 = (char)pcVar14;
      uStack_7f = (undefined2)((ulong)pcVar14 >> 8);
      uStack_7d = (undefined1)((ulong)pcVar14 >> 0x18);
      uStack_7c = (uint)((ulong)pcVar14 >> 0x20);
      *(undefined8 *)(pcVar14 + 8) = s_receive_item_popup_chara_002b2009._8_8_;
      *(undefined8 *)pcVar14 = uVar7;
      *(undefined8 *)(pcVar14 + 0x10) = uVar8;
      cStack_88 = (char)uVar10;
      uStack_87 = (undefined7)((ulong)uVar10 >> 8);
      local_90 = (byte)uVar9;
      uStack_8f = (undefined7)((ulong)uVar9 >> 8);
      pcVar14[0x18] = '\0';
      lVar16 = FUN_008514b8();
      lVar16 = lVar16 + (long)(int)param_3 * 0x1e0;
      if ((*(ulong *)(
                     "NSt6__ndk110__function6__funcIZN11aDownloader8downloadERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_2NS6_ISB_EEFvbEEE"
                     + lVar16 + 0x60) & 1) == 0) {
        local_a0 = *(void **)(
                             "NSt6__ndk110__function6__funcIZN11aDownloader8downloadERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_2NS6_ISB_EEFvbEEE"
                             + lVar16 + 0x70);
        uStack_a8 = *(ulong *)(
                              "NSt6__ndk110__function6__funcIZN11aDownloader8downloadERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_2NS6_ISB_EEFvbEEE"
                              + lVar16 + 0x68);
        local_b0 = *(ulong *)(
                             "NSt6__ndk110__function6__funcIZN11aDownloader8downloadERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_2NS6_ISB_EEFvbEEE"
                             + lVar16 + 0x60);
      }
      else {
        FUN_0043bae0(&local_b0,
                     *(undefined8 *)
                      (
                      "NSt6__ndk110__function6__funcIZN11aDownloader8downloadERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_2NS6_ISB_EEFvbEEE"
                      + lVar16 + 0x70),
                     *(undefined8 *)
                      (
                      "NSt6__ndk110__function6__funcIZN11aDownloader8downloadERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_2NS6_ISB_EEFvbEEE"
                      + lVar16 + 0x68));
      }
      FUN_0048ce14(local_f8,&local_90);
      if ((local_b0 & 1) == 0) {
        uStack_108 = uStack_a8;
        local_110 = local_b0;
        local_100 = local_a0;
      }
      else {
        FUN_0043bae0(&local_110,local_a0,uStack_a8);
      }
      FUN_00492dc8(param_1,local_f8,&local_110);
      pvVar12 = local_100;
      uVar17 = local_110;
      goto joined_r0x00b0df0c;
    }
    local_90 = 0;
    uStack_8f = 0;
    cStack_88 = '\0';
    uStack_87 = 0;
    local_80 = '\0';
    uStack_7f = 0;
    uStack_7d = 0;
    uStack_7c = 0;
    if ((((*(uint *)(param_2 + 0x24) < 0xb) &&
         ((1 << (ulong)(*(uint *)(param_2 + 0x24) & 0x1f) & 0x502U) != 0)) ||
        ((param_3 < 0x1e && ((1 << (ulong)(param_3 & 0x1f) & 0x203040c0U) != 0)))) ||
       (param_3 == 0x91)) {
      pcVar14 = "receive_item_popup_xp";
    }
    else {
      pcVar14 = "receive_item_popup";
    }
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKc(&local_90,pcVar14)
    ;
    FUN_0048ce14(&local_b0,&local_90);
    FUN_0071ecc0(local_e0,param_3);
    FUN_005da544(param_1,&local_b0,local_e0,param_5);
  }
  else {
    if (param_4 == 3) {
      pcVar14 = (char *)_Znwm(0x20);
      uVar11 = _UNK_002c29c8;
      uVar10 = _DAT_002c29c0;
      uVar9 = s_receive_item_popup_chara_evolve_002a3614._23_8_;
      uVar8 = s_receive_item_popup_chara_evolve_002a3614._0_8_;
      uVar7 = CONCAT71(s_receive_item_popup_chara_evolve_002a3614._16_7_,
                       s_receive_item_popup_chara_evolve_002a3614[0xf]);
      local_80 = (char)pcVar14;
      uStack_7f = (undefined2)((ulong)pcVar14 >> 8);
      uStack_7d = (undefined1)((ulong)pcVar14 >> 0x18);
      uStack_7c = (uint)((ulong)pcVar14 >> 0x20);
      *(ulong *)(pcVar14 + 8) =
           CONCAT17(s_receive_item_popup_chara_evolve_002a3614[0xf],
                    s_receive_item_popup_chara_evolve_002a3614._8_7_);
      *(undefined8 *)pcVar14 = uVar8;
      *(undefined8 *)(pcVar14 + 0x17) = uVar9;
      *(undefined8 *)(pcVar14 + 0xf) = uVar7;
      cStack_88 = (char)uVar11;
      uStack_87 = (undefined7)((ulong)uVar11 >> 8);
      local_90 = (byte)uVar10;
      uStack_8f = (undefined7)((ulong)uVar10 >> 8);
      pcVar14[0x1f] = '\0';
      lVar16 = FUN_008514b8();
      lVar16 = lVar16 + (long)(int)param_3 * 0x1e0;
      if ((*(ulong *)(
                     "NSt6__ndk110__function6__funcIZN11aDownloader8downloadERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_2NS6_ISB_EEFvbEEE"
                     + lVar16 + 0x60) & 1) == 0) {
        local_a0 = *(void **)(
                             "NSt6__ndk110__function6__funcIZN11aDownloader8downloadERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_2NS6_ISB_EEFvbEEE"
                             + lVar16 + 0x70);
        uStack_a8 = *(ulong *)(
                              "NSt6__ndk110__function6__funcIZN11aDownloader8downloadERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_2NS6_ISB_EEFvbEEE"
                              + lVar16 + 0x68);
        local_b0 = *(ulong *)(
                             "NSt6__ndk110__function6__funcIZN11aDownloader8downloadERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_2NS6_ISB_EEFvbEEE"
                             + lVar16 + 0x60);
      }
      else {
        FUN_0043bae0(&local_b0,
                     *(undefined8 *)
                      (
                      "NSt6__ndk110__function6__funcIZN11aDownloader8downloadERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_2NS6_ISB_EEFvbEEE"
                      + lVar16 + 0x70),
                     *(undefined8 *)
                      (
                      "NSt6__ndk110__function6__funcIZN11aDownloader8downloadERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_2NS6_ISB_EEFvbEEE"
                      + lVar16 + 0x68));
      }
      FUN_0048ce14(local_f8,&local_90);
      if ((local_b0 & 1) == 0) {
        uStack_128 = uStack_a8;
        local_130 = local_b0;
        local_120 = local_a0;
      }
      else {
        FUN_0043bae0(&local_130,local_a0,uStack_a8);
      }
      FUN_00492dc8(param_1,local_f8,&local_130);
      pvVar12 = local_120;
      uVar17 = local_130;
    }
    else {
      if (param_4 != 4) {
        if (param_4 != 0xb) goto LAB_00b0dd9c;
        local_90 = 0x26;
        uStack_7f = 0x7570;
        uStack_7d = 0x70;
        uStack_87 = (undefined7)s_receive_honor_popup_002bdd52._8_8_;
        local_80 = SUB81(s_receive_honor_popup_002bdd52._8_8_,7);
        uStack_8f = (undefined7)s_receive_honor_popup_002bdd52._0_8_;
        cStack_88 = SUB81(s_receive_honor_popup_002bdd52._0_8_,7);
        uStack_7c = uStack_7c & 0xffffff00;
        FUN_0048ce14(&local_b0,&local_90);
        FUN_0071ecc0(local_c8,param_3);
        FUN_00492dc8(param_1,&local_b0,local_c8);
        local_d0 = local_b8;
        local_e0[0] = local_c8[0];
        goto joined_r0x00b0dcb8;
      }
      local_90 = 0x24;
      uStack_7f = 0x7075;
      uStack_87 = (undefined7)s_receive_item_popup_002b3f0e._8_8_;
      local_80 = SUB81(s_receive_item_popup_002b3f0e._8_8_,7);
      uStack_8f = (undefined7)s_receive_item_popup_002b3f0e._0_8_;
      cStack_88 = SUB81(s_receive_item_popup_002b3f0e._0_8_,7);
      uStack_7d = 0;
      lVar16 = FUN_008514b8();
      FUN_006875e8(lVar16 + 0x1648,param_3);
      FUN_00684f70(&local_b0);
      FUN_0048ce14(local_f8,&local_90);
      if ((local_b0 & 1) == 0) {
        uStack_148 = uStack_a8;
        local_150 = local_b0;
        local_140 = local_a0;
      }
      else {
        FUN_0043bae0(&local_150,local_a0,uStack_a8);
      }
      FUN_005da544(param_1,local_f8,&local_150,param_5);
      pvVar12 = local_140;
      uVar17 = local_150;
    }
joined_r0x00b0df0c:
    local_d0 = local_e8;
    local_e0[0] = local_f8[0];
    if ((uVar17 & 1) != 0) {
      _ZdlPv(pvVar12);
      local_d0 = local_e8;
      local_e0[0] = local_f8[0];
    }
  }
joined_r0x00b0dcb8:
  if ((local_e0[0] & 1) != 0) {
    _ZdlPv(local_d0);
  }
  if ((local_b0 & 1) != 0) {
    _ZdlPv(local_a0);
  }
  if ((local_90 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_7c,CONCAT13(uStack_7d,CONCAT21(uStack_7f,local_80))));
  }
LAB_00b0dfa4:
  if (*(long *)(lVar6 + 0x28) != local_78) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~
