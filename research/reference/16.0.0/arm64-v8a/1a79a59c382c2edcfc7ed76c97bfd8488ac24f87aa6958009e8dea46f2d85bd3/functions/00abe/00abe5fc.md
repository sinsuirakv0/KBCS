# 00abe5fc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a60644`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60644.md) · 移動量 `+0x5dfb8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0052.md#compare-ebe88b7a19c91bb9471d2eb28826ccfd)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00abe7f8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abe/00abe7f8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-d4a4f3501fc201ecb9d02fa171863326)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_text_sha256": "3e40edee83c71ba6297c0e01fa03196828528eaabb177b3622e4211584cf348a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00abe5fc",
        "00abf1b3"
      ],
      [
        "00abf1fc",
        "00abf207"
      ],
      [
        "00abf218",
        "00abf22b"
      ],
      [
        "00abf238",
        "00abf243"
      ],
      [
        "00abf294",
        "00abf2b3"
      ]
    ],
    "bytes_sha256": "cbeeeaefb88f5c6c32b4f76b349d10ddb006aeb1a5f70e554ce46a682db29f48",
    "instruction_count": 769,
    "instruction_bytes": 3076,
    "body_bytes": 3076,
    "indirect": 9,
    "unresolved": 8
  }
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00abe5fc"></a> `00abe5fc` | `ff c3 05 d1` | sub sp,sp,#0x170 | `FALL_THROUGH`
<a id="insn-00abe600"></a> `00abe600` | `fd 7b 11 a9` | stp x29,x30,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00abe604"></a> `00abe604` | `fc 6f 12 a9` | stp x28,x27,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00abe608"></a> `00abe608` | `fa 67 13 a9` | stp x26,x25,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00abe60c"></a> `00abe60c` | `f8 5f 14 a9` | stp x24,x23,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00abe610"></a> `00abe610` | `f6 57 15 a9` | stp x22,x21,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00abe614"></a> `00abe614` | `f4 4f 16 a9` | stp x20,x19,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-00abe618"></a> `00abe618` | `fd 43 04 91` | add x29,sp,#0x110 | `FALL_THROUGH`
<a id="insn-00abe61c"></a> `00abe61c` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00abe620"></a> `00abe620` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00abe624"></a> `00abe624` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00abe628"></a> `00abe628` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abe62c"></a> `00abe62c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00abe630"></a> `00abe630` | `a8 03 1f f8` | stur x8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abe634"></a> `00abe634` | `28 0f 00 d0` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-00abe638"></a> `00abe638` | `08 bd 42 f9` | ldr x8,[x8, #0x578] | `FALL_THROUGH`
<a id="insn-00abe63c"></a> `00abe63c` | `48 01 00 b4` | cbz x8,0x00abe664 | `CONDITIONAL_JUMP`
<a id="insn-00abe640"></a> `00abe640` | `21 0d 00 f0` | adrp x1,0xc65000 | `FALL_THROUGH`
<a id="insn-00abe644"></a> `00abe644` | `21 60 29 91` | add x1,x1,#0xa58 | `FALL_THROUGH`
<a id="insn-00abe648"></a> `00abe648` | `62 0e 00 d0` | adrp x2,0xc8c000 | `FALL_THROUGH`
<a id="insn-00abe64c"></a> `00abe64c` | `42 e0 3b 91` | add x2,x2,#0xef8 | `FALL_THROUGH`
<a id="insn-00abe650"></a> `00abe650` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00abe654"></a> `00abe654` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00abe658"></a> `00abe658` | `ee 66 06 94` | bl 0x00c58210 | `UNCONDITIONAL_CALL`
<a id="insn-00abe65c"></a> `00abe65c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00abe660"></a> `00abe660` | `02 00 00 14` | b 0x00abe668 | `UNCONDITIONAL_JUMP`
<a id="insn-00abe664"></a> `00abe664` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00abe668"></a> `00abe668` | `94 4b f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abe66c"></a> `00abe66c` | `16 e7 85 52` | mov w22,#0x2f38 | `FALL_THROUGH`
<a id="insn-00abe670"></a> `00abe670` | `c1 26 80 52` | mov w1,#0x136 | `FALL_THROUGH`
<a id="insn-00abe674"></a> `00abe674` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-00abe678"></a> `00abe678` | `a3 e4 f7 97` | bl 0x008b7904 | `UNCONDITIONAL_CALL`
<a id="insn-00abe67c"></a> `00abe67c` | `8f 4b f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abe680"></a> `00abe680` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-00abe684"></a> `00abe684` | `e1 26 80 52` | mov w1,#0x137 | `FALL_THROUGH`
<a id="insn-00abe688"></a> `00abe688` | `9f e4 f7 97` | bl 0x008b7904 | `UNCONDITIONAL_CALL`
<a id="insn-00abe68c"></a> `00abe68c` | `8b 4b f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abe690"></a> `00abe690` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-00abe694"></a> `00abe694` | `01 27 80 52` | mov w1,#0x138 | `FALL_THROUGH`
<a id="insn-00abe698"></a> `00abe698` | `9b e4 f7 97` | bl 0x008b7904 | `UNCONDITIONAL_CALL`
<a id="insn-00abe69c"></a> `00abe69c` | `87 4b f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abe6a0"></a> `00abe6a0` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-00abe6a4"></a> `00abe6a4` | `21 27 80 52` | mov w1,#0x139 | `FALL_THROUGH`
<a id="insn-00abe6a8"></a> `00abe6a8` | `97 e4 f7 97` | bl 0x008b7904 | `UNCONDITIONAL_CALL`
<a id="insn-00abe6ac"></a> `00abe6ac` | `83 4b f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abe6b0"></a> `00abe6b0` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-00abe6b4"></a> `00abe6b4` | `41 27 80 52` | mov w1,#0x13a | `FALL_THROUGH`
<a id="insn-00abe6b8"></a> `00abe6b8` | `93 e4 f7 97` | bl 0x008b7904 | `UNCONDITIONAL_CALL`
<a id="insn-00abe6bc"></a> `00abe6bc` | `7f 4b f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abe6c0"></a> `00abe6c0` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-00abe6c4"></a> `00abe6c4` | `61 27 80 52` | mov w1,#0x13b | `FALL_THROUGH`
<a id="insn-00abe6c8"></a> `00abe6c8` | `8f e4 f7 97` | bl 0x008b7904 | `UNCONDITIONAL_CALL`
<a id="insn-00abe6cc"></a> `00abe6cc` | `7b 4b f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abe6d0"></a> `00abe6d0` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-00abe6d4"></a> `00abe6d4` | `81 27 80 52` | mov w1,#0x13c | `FALL_THROUGH`
<a id="insn-00abe6d8"></a> `00abe6d8` | `8b e4 f7 97` | bl 0x008b7904 | `UNCONDITIONAL_CALL`
<a id="insn-00abe6dc"></a> `00abe6dc` | `77 4b f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abe6e0"></a> `00abe6e0` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-00abe6e4"></a> `00abe6e4` | `a1 27 80 52` | mov w1,#0x13d | `FALL_THROUGH`
<a id="insn-00abe6e8"></a> `00abe6e8` | `87 e4 f7 97` | bl 0x008b7904 | `UNCONDITIONAL_CALL`
<a id="insn-00abe6ec"></a> `00abe6ec` | `73 4b f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abe6f0"></a> `00abe6f0` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-00abe6f4"></a> `00abe6f4` | `c1 27 80 52` | mov w1,#0x13e | `FALL_THROUGH`
<a id="insn-00abe6f8"></a> `00abe6f8` | `83 e4 f7 97` | bl 0x008b7904 | `UNCONDITIONAL_CALL`
<a id="insn-00abe6fc"></a> `00abe6fc` | `6f 4b f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abe700"></a> `00abe700` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-00abe704"></a> `00abe704` | `e1 27 80 52` | mov w1,#0x13f | `FALL_THROUGH`
<a id="insn-00abe708"></a> `00abe708` | `7f e4 f7 97` | bl 0x008b7904 | `UNCONDITIONAL_CALL`
<a id="insn-00abe70c"></a> `00abe70c` | `6b 4b f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abe710"></a> `00abe710` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-00abe714"></a> `00abe714` | `01 28 80 52` | mov w1,#0x140 | `FALL_THROUGH`
<a id="insn-00abe718"></a> `00abe718` | `7b e4 f7 97` | bl 0x008b7904 | `UNCONDITIONAL_CALL`
<a id="insn-00abe71c"></a> `00abe71c` | `67 4b f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abe720"></a> `00abe720` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-00abe724"></a> `00abe724` | `21 28 80 52` | mov w1,#0x141 | `FALL_THROUGH`
<a id="insn-00abe728"></a> `00abe728` | `77 e4 f7 97` | bl 0x008b7904 | `UNCONDITIONAL_CALL`
<a id="insn-00abe72c"></a> `00abe72c` | `63 4b f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abe730"></a> `00abe730` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-00abe734"></a> `00abe734` | `41 28 80 52` | mov w1,#0x142 | `FALL_THROUGH`
<a id="insn-00abe738"></a> `00abe738` | `73 e4 f7 97` | bl 0x008b7904 | `UNCONDITIONAL_CALL`
<a id="insn-00abe73c"></a> `00abe73c` | `5f 4b f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abe740"></a> `00abe740` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-00abe744"></a> `00abe744` | `61 28 80 52` | mov w1,#0x143 | `FALL_THROUGH`
<a id="insn-00abe748"></a> `00abe748` | `6f e4 f7 97` | bl 0x008b7904 | `UNCONDITIONAL_CALL`
<a id="insn-00abe74c"></a> `00abe74c` | `5b 4b f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abe750"></a> `00abe750` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-00abe754"></a> `00abe754` | `81 28 80 52` | mov w1,#0x144 | `FALL_THROUGH`
<a id="insn-00abe758"></a> `00abe758` | `6b e4 f7 97` | bl 0x008b7904 | `UNCONDITIONAL_CALL`
<a id="insn-00abe75c"></a> `00abe75c` | `57 4b f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abe760"></a> `00abe760` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-00abe764"></a> `00abe764` | `a1 28 80 52` | mov w1,#0x145 | `FALL_THROUGH`
<a id="insn-00abe768"></a> `00abe768` | `67 e4 f7 97` | bl 0x008b7904 | `UNCONDITIONAL_CALL`
<a id="insn-00abe76c"></a> `00abe76c` | `53 4b f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abe770"></a> `00abe770` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-00abe774"></a> `00abe774` | `c1 28 80 52` | mov w1,#0x146 | `FALL_THROUGH`
<a id="insn-00abe778"></a> `00abe778` | `63 e4 f7 97` | bl 0x008b7904 | `UNCONDITIONAL_CALL`
<a id="insn-00abe77c"></a> `00abe77c` | `4f 4b f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abe780"></a> `00abe780` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-00abe784"></a> `00abe784` | `e1 28 80 52` | mov w1,#0x147 | `FALL_THROUGH`
<a id="insn-00abe788"></a> `00abe788` | `5f e4 f7 97` | bl 0x008b7904 | `UNCONDITIONAL_CALL`
<a id="insn-00abe78c"></a> `00abe78c` | `4b 4b f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abe790"></a> `00abe790` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-00abe794"></a> `00abe794` | `01 29 80 52` | mov w1,#0x148 | `FALL_THROUGH`
<a id="insn-00abe798"></a> `00abe798` | `5b e4 f7 97` | bl 0x008b7904 | `UNCONDITIONAL_CALL`
<a id="insn-00abe79c"></a> `00abe79c` | `47 4b f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abe7a0"></a> `00abe7a0` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-00abe7a4"></a> `00abe7a4` | `21 29 80 52` | mov w1,#0x149 | `FALL_THROUGH`
<a id="insn-00abe7a8"></a> `00abe7a8` | `57 e4 f7 97` | bl 0x008b7904 | `UNCONDITIONAL_CALL`
<a id="insn-00abe7ac"></a> `00abe7ac` | `88 0a 14 0b` | add w8,w20,w20, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00abe7b0"></a> `00abe7b0` | `a9 03 02 d1` | sub x9,x29,#0x80 | `FALL_THROUGH`
<a id="insn-00abe7b4"></a> `00abe7b4` | `ea c3 01 91` | add x10,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00abe7b8"></a> `00abe7b8` | `3b 01 40 b2` | orr x27,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00abe7bc"></a> `00abe7bc` | `69 42 01 91` | add x9,x19,#0x50 | `FALL_THROUGH`
<a id="insn-00abe7c0"></a> `00abe7c0` | `ac 82 0b 91` | add x12,x21,#0x2e0 | `FALL_THROUGH`
<a id="insn-00abe7c4"></a> `00abe7c4` | `08 75 1e 53` | lsl w8,w8,#0x2 | `FALL_THROUGH`
<a id="insn-00abe7c8"></a> `00abe7c8` | `e9 2f 00 f9` | str x9,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00abe7cc"></a> `00abe7cc` | `49 01 40 b2` | orr x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00abe7d0"></a> `00abe7d0` | `ec 0f 00 f9` | str x12,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00abe7d4"></a> `00abe7d4` | `eb 03 1f aa` | mov x11,xzr | `FALL_THROUGH`
<a id="insn-00abe7d8"></a> `00abe7d8` | `e8 17 00 b9` | str w8,[sp, #0x14] | `FALL_THROUGH`
<a id="insn-00abe7dc"></a> `00abe7dc` | `a8 a3 01 d1` | sub x8,x29,#0x68 | `FALL_THROUGH`
<a id="insn-00abe7e0"></a> `00abe7e0` | `08 01 40 b2` | orr x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00abe7e4"></a> `00abe7e4` | `e9 2b 00 f9` | str x9,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abe7e8"></a> `00abe7e8` | `e9 0e 00 90` | adrp x9,0xc9a000 | `FALL_THROUGH`
<a id="insn-00abe7ec"></a> `00abe7ec` | `e8 1b 00 f9` | str x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abe7f0"></a> `00abe7f0` | `28 c0 ff 90` | adrp x8,0x2c2000 | `FALL_THROUGH`
<a id="insn-00abe7f4"></a> `00abe7f4` | `00 99 c0 3d` | ldr q0,[x8, #0x260] | `FALL_THROUGH`
<a id="insn-00abe7f8"></a> `00abe7f8` | `e8 0e 00 90` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-00abe7fc"></a> `00abe7fc` | `e0 0b 80 3d` | str q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abe800"></a> `00abe800` | `08 b9 47 f9` | ldr x8,[x8, #0xf70] | `FALL_THROUGH`
<a id="insn-00abe804"></a> `00abe804` | `29 b5 47 f9` | ldr x9,[x9, #0xf68] | `FALL_THROUGH`
<a id="insn-00abe808"></a> `00abe808` | `0a 41 00 91` | add x10,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00abe80c"></a> `00abe80c` | `28 41 00 91` | add x8,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00abe810"></a> `00abe810` | `e8 2b 04 a9` | stp x8,x10,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abe814"></a> `00abe814` | `05 00 00 14` | b 0x00abe828 | `UNCONDITIONAL_JUMP`
<a id="insn-00abe818"></a> `00abe818` | `eb 1f 40 f9` | ldr x11,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00abe81c"></a> `00abe81c` | `6b 05 00 91` | add x11,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00abe820"></a> `00abe820` | `7f 11 00 f1` | cmp x11,#0x4 | `FALL_THROUGH`
<a id="insn-00abe824"></a> `00abe824` | `c0 46 00 54` | b.eq 0x00abf0fc | `CONDITIONAL_JUMP`
<a id="insn-00abe828"></a> `00abe828` | `09 0a 80 52` | mov w9,#0x50 | `FALL_THROUGH`
<a id="insn-00abe82c"></a> `00abe82c` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00abe830"></a> `00abe830` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00abe834"></a> `00abe834` | `6a 21 09 9b` | madd x10,x11,x9,x8 | `FALL_THROUGH`
<a id="insn-00abe838"></a> `00abe838` | `a9 0e 80 52` | mov w9,#0x75 | `FALL_THROUGH`
<a id="insn-00abe83c"></a> `00abe83c` | `68 09 0b 8b` | add x8,x11,x11, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00abe840"></a> `00abe840` | `eb 1f 00 f9` | str x11,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00abe844"></a> `00abe844` | `7c 7d 09 1b` | mul w28,w11,w9 | `FALL_THROUGH`
<a id="insn-00abe848"></a> `00abe848` | `e9 17 40 b9` | ldr w9,[sp, #0x14] | `FALL_THROUGH`
<a id="insn-00abe84c"></a> `00abe84c` | `37 01 08 0b` | add w23,w9,w8 | `FALL_THROUGH`
<a id="insn-00abe850"></a> `00abe850` | `08 d9 04 91` | add x8,x8,#0x136 | `FALL_THROUGH`
<a id="insn-00abe854"></a> `00abe854` | `e8 2b 06 a9` | stp x8,x10,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abe858"></a> `00abe858` | `0a 00 00 14` | b 0x00abe880 | `UNCONDITIONAL_JUMP`
<a id="insn-00abe85c"></a> `00abe85c` | `e8 23 40 f9` | ldr x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abe860"></a> `00abe860` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00abe864"></a> `00abe864` | `08 04 05 f8` | str x8,[x0], #0x50 | `FALL_THROUGH`
<a id="insn-00abe868"></a> `00abe868` | `c8 68 ec 97` | bl 0x005d8b88 | `UNCONDITIONAL_CALL`
<a id="insn-00abe86c"></a> `00abe86c` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00abe870"></a> `00abe870` | `90 64 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abe874"></a> `00abe874` | `b5 06 00 91` | add x21,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00abe878"></a> `00abe878` | `bf 16 00 f1` | cmp x21,#0x5 | `FALL_THROUGH`
<a id="insn-00abe87c"></a> `00abe87c` | `e0 fc ff 54` | b.eq 0x00abe818 | `CONDITIONAL_JUMP`
<a id="insn-00abe880"></a> `00abe880` | `6a 26 40 a9` | ldp x10,x9,[x19] | `FALL_THROUGH`
<a id="insn-00abe884"></a> `00abe884` | `e8 02 15 0b` | add w8,w23,w21 | `FALL_THROUGH`
<a id="insn-00abe888"></a> `00abe888` | `08 7d 40 93` | sxtw x8,w8 | `FALL_THROUGH`
<a id="insn-00abe88c"></a> `00abe88c` | `29 01 0a cb` | sub x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00abe890"></a> `00abe890` | `1f 0d 89 eb` | cmp x8,x9, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00abe894"></a> `00abe894` | `22 fc ff 54` | b.cs 0x00abe818 | `CONDITIONAL_JUMP`
<a id="insn-00abe898"></a> `00abe898` | `69 aa 41 a9` | ldp x9,x10,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00abe89c"></a> `00abe89c` | `4a 01 09 cb` | sub x10,x10,x9 | `FALL_THROUGH`
<a id="insn-00abe8a0"></a> `00abe8a0` | `1f 0d 8a eb` | cmp x8,x10, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00abe8a4"></a> `00abe8a4` | `62 45 00 54` | b.cs 0x00abf150 | `CONDITIONAL_JUMP`
<a id="insn-00abe8a8"></a> `00abe8a8` | `08 f1 7d d3` | lsl x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00abe8ac"></a> `00abe8ac` | `38 69 68 b8` | ldr w24,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00abe8b0"></a> `00abe8b0` | `1f 07 00 31` | cmn w24,#0x1 | `FALL_THROUGH`
<a id="insn-00abe8b4"></a> `00abe8b4` | `20 fb ff 54` | b.eq 0x00abe818 | `CONDITIONAL_JUMP`
<a id="insn-00abe8b8"></a> `00abe8b8` | `60 52 43 a9` | ldp x0,x20,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00abe8bc"></a> `00abe8bc` | `e1 03 18 2a` | mov w1,w24 | `FALL_THROUGH`
<a id="insn-00abe8c0"></a> `00abe8c0` | `88 02 00 cb` | sub x8,x20,x0 | `FALL_THROUGH`
<a id="insn-00abe8c4"></a> `00abe8c4` | `02 fd 42 93` | asr x2,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00abe8c8"></a> `00abe8c8` | `e2 65 06 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00abe8cc"></a> `00abe8cc` | `68 1e 40 f9` | ldr x8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00abe8d0"></a> `00abe8d0` | `1f 00 00 f1` | cmp x0,#0x0 | `FALL_THROUGH`
<a id="insn-00abe8d4"></a> `00abe8d4` | `89 02 80 9a` | csel x9,x20,x0,eq | `FALL_THROUGH`
<a id="insn-00abe8d8"></a> `00abe8d8` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00abe8dc"></a> `00abe8dc` | `e8 37 40 f9` | ldr x8,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00abe8e0"></a> `00abe8e0` | `19 11 15 8b` | add x25,x8,x21, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00abe8e4"></a> `00abe8e4` | `00 07 00 54` | b.eq 0x00abe9c4 | `CONDITIONAL_JUMP`
<a id="insn-00abe8e8"></a> `00abe8e8` | `28 0f 00 d0` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-00abe8ec"></a> `00abe8ec` | `08 e1 2c 91` | add x8,x8,#0xb38 | `FALL_THROUGH`
<a id="insn-00abe8f0"></a> `00abe8f0` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00abe8f4"></a> `00abe8f4` | `08 38 00 36` | tbz w8,#0x0,0x00abeff4 | `CONDITIONAL_JUMP`
<a id="insn-00abe8f8"></a> `00abe8f8` | `ea bf ff b0` | adrp x10,0x2bb000 | `FALL_THROUGH`
<a id="insn-00abe8fc"></a> `00abe8fc` | `4a 1d 20 91` | add x10,x10,#0x807 | `FALL_THROUGH`
<a id="insn-00abe900"></a> `00abe900` | `89 03 80 52` | mov w9,#0x1c | `FALL_THROUGH`
<a id="insn-00abe904"></a> `00abe904` | `48 01 40 f9` | ldr x8,[x10] | `FALL_THROUGH`
<a id="insn-00abe908"></a> `00abe908` | `a9 03 18 38` | sturb w9,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00abe90c"></a> `00abe90c` | `49 61 40 f8` | ldur x9,[x10, #0x6] | `FALL_THROUGH`
<a id="insn-00abe910"></a> `00abe910` | `bf f3 18 38` | sturb wzr,[x29, #-0x71] | `FALL_THROUGH`
<a id="insn-00abe914"></a> `00abe914` | `68 03 00 f9` | str x8,[x27] | `FALL_THROUGH`
<a id="insn-00abe918"></a> `00abe918` | `69 63 00 f8` | stur x9,[x27, #0x6] | `FALL_THROUGH`
<a id="insn-00abe91c"></a> `00abe91c` | `a8 a3 01 d1` | sub x8,x29,#0x68 | `FALL_THROUGH`
<a id="insn-00abe920"></a> `00abe920` | `a0 03 02 d1` | sub x0,x29,#0x80 | `FALL_THROUGH`
<a id="insn-00abe924"></a> `00abe924` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00abe928"></a> `00abe928` | `e2 03 18 2a` | mov w2,w24 | `FALL_THROUGH`
<a id="insn-00abe92c"></a> `00abe92c` | `62 25 e6 97` | bl 0x00447eb4 | `UNCONDITIONAL_CALL`
<a id="insn-00abe930"></a> `00abe930` | `e8 bf ff d0` | adrp x8,0x2bc000 | `FALL_THROUGH`
<a id="insn-00abe934"></a> `00abe934` | `08 b9 2a 91` | add x8,x8,#0xaae | `FALL_THROUGH`
<a id="insn-00abe938"></a> `00abe938` | `ff 07 02 39` | strb wzr,[sp, #0x81] | `FALL_THROUGH`
<a id="insn-00abe93c"></a> `00abe93c` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00abe940"></a> `00abe940` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00abe944"></a> `00abe944` | `e8 c3 01 39` | strb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abe948"></a> `00abe948` | `e8 2b 40 f9` | ldr x8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abe94c"></a> `00abe94c` | `00 01 80 3d` | str q0,[x8] | `FALL_THROUGH`
<a id="insn-00abe950"></a> `00abe950` | `a8 43 01 d1` | sub x8,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00abe954"></a> `00abe954` | `a1 a3 01 d1` | sub x1,x29,#0x68 | `FALL_THROUGH`
<a id="insn-00abe958"></a> `00abe958` | `e2 c3 01 91` | add x2,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00abe95c"></a> `00abe95c` | `20 0f 00 d0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00abe960"></a> `00abe960` | `00 00 2c 91` | add x0,x0,#0xb00 | `FALL_THROUGH`
<a id="insn-00abe964"></a> `00abe964` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-00abe968"></a> `00abe968` | `19 ff e6 97` | bl 0x0047e5cc | `UNCONDITIONAL_CALL`
<a id="insn-00abe96c"></a> `00abe96c` | `a0 03 db 3c` | ldur q0,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00abe970"></a> `00abe970` | `bf 7f 3b a9` | stp xzr,xzr,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00abe974"></a> `00abe974` | `3a 07 40 f9` | ldr x26,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00abe978"></a> `00abe978` | `20 03 80 3d` | str q0,[x25] | `FALL_THROUGH`
<a id="insn-00abe97c"></a> `00abe97c` | `ba 00 00 b4` | cbz x26,0x00abe990 | `CONDITIONAL_JUMP`
<a id="insn-00abe980"></a> `00abe980` | `41 23 00 91` | add x1,x26,#0x8 | `FALL_THROUGH`
<a id="insn-00abe984"></a> `00abe984` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abe988"></a> `00abe988` | `d6 53 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00abe98c"></a> `00abe98c` | `00 11 00 b4` | cbz x0,0x00abebac | `CONDITIONAL_JUMP`
<a id="insn-00abe990"></a> `00abe990` | `ba 83 5b f8` | ldur x26,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00abe994"></a> `00abe994` | `da 11 00 b4` | cbz x26,0x00abebcc | `CONDITIONAL_JUMP`
<a id="insn-00abe998"></a> `00abe998` | `41 23 00 91` | add x1,x26,#0x8 | `FALL_THROUGH`
<a id="insn-00abe99c"></a> `00abe99c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abe9a0"></a> `00abe9a0` | `d0 53 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00abe9a4"></a> `00abe9a4` | `40 11 00 b5` | cbnz x0,0x00abebcc | `CONDITIONAL_JUMP`
<a id="insn-00abe9a8"></a> `00abe9a8` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-00abe9ac"></a> `00abe9ac` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00abe9b0"></a> `00abe9b0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abe9b4"></a> `00abe9b4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abe9b8"></a> `00abe9b8` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00abe9bc"></a> `00abe9bc` | `31 64 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00abe9c0"></a> `00abe9c0` | `83 00 00 14` | b 0x00abebcc | `UNCONDITIONAL_JUMP`
<a id="insn-00abe9c4"></a> `00abe9c4` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-00abe9c8"></a> `00abe9c8` | `1a 7f 40 93` | sxtw x26,w24 | `FALL_THROUGH`
<a id="insn-00abe9cc"></a> `00abe9cc` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-00abe9d0"></a> `00abe9d0` | `5f 0f 89 eb` | cmp x26,x9, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00abe9d4"></a> `00abe9d4` | `c2 3c 00 54` | b.cs 0x00abf16c | `CONDITIONAL_JUMP`
<a id="insn-00abe9d8"></a> `00abe9d8` | `00 79 7a f8` | ldr x0,[x8, x26, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00abe9dc"></a> `00abe9dc` | `c1 f9 ff 97` | bl 0x00abd0e0 | `UNCONDITIONAL_CALL`
<a id="insn-00abe9e0"></a> `00abe9e0` | `28 0f 00 d0` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-00abe9e4"></a> `00abe9e4` | `08 e1 2c 91` | add x8,x8,#0xb38 | `FALL_THROUGH`
<a id="insn-00abe9e8"></a> `00abe9e8` | `e0 07 00 36` | tbz w0,#0x0,0x00abeae4 | `CONDITIONAL_JUMP`
<a id="insn-00abe9ec"></a> `00abe9ec` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00abe9f0"></a> `00abe9f0` | `e8 32 00 36` | tbz w8,#0x0,0x00abf04c | `CONDITIONAL_JUMP`
<a id="insn-00abe9f4"></a> `00abe9f4` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-00abe9f8"></a> `00abe9f8` | `8b bf ff d0` | adrp x11,0x2b0000 | `FALL_THROUGH`
<a id="insn-00abe9fc"></a> `00abe9fc` | `6b 99 0d 91` | add x11,x11,#0x366 | `FALL_THROUGH`
<a id="insn-00abea00"></a> `00abea00` | `8a 05 80 52` | mov w10,#0x2c | `FALL_THROUGH`
<a id="insn-00abea04"></a> `00abea04` | `bf 73 19 38` | sturb wzr,[x29, #-0x69] | `FALL_THROUGH`
<a id="insn-00abea08"></a> `00abea08` | `60 01 c0 3d` | ldr q0,[x11] | `FALL_THROUGH`
<a id="insn-00abea0c"></a> `00abea0c` | `aa 03 18 38` | sturb w10,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00abea10"></a> `00abea10` | `6a e1 40 f8` | ldur x10,[x11, #0xe] | `FALL_THROUGH`
<a id="insn-00abea14"></a> `00abea14` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-00abea18"></a> `00abea18` | `5f 0f 89 eb` | cmp x26,x9, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00abea1c"></a> `00abea1c` | `60 03 80 3d` | str q0,[x27] | `FALL_THROUGH`
<a id="insn-00abea20"></a> `00abea20` | `6a e3 00 f8` | stur x10,[x27, #0xe] | `FALL_THROUGH`
<a id="insn-00abea24"></a> `00abea24` | `22 3b 00 54` | b.cs 0x00abf188 | `CONDITIONAL_JUMP`
<a id="insn-00abea28"></a> `00abea28` | `08 79 7a f8` | ldr x8,[x8, x26, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00abea2c"></a> `00abea2c` | `02 49 40 b9` | ldr w2,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00abea30"></a> `00abea30` | `a8 a3 01 d1` | sub x8,x29,#0x68 | `FALL_THROUGH`
<a id="insn-00abea34"></a> `00abea34` | `a0 03 02 d1` | sub x0,x29,#0x80 | `FALL_THROUGH`
<a id="insn-00abea38"></a> `00abea38` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00abea3c"></a> `00abea3c` | `1e 25 e6 97` | bl 0x00447eb4 | `UNCONDITIONAL_CALL`
<a id="insn-00abea40"></a> `00abea40` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00abea44"></a> `00abea44` | `13 64 06 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00abea48"></a> `00abea48` | `68 bf ff f0` | adrp x8,0x2ad000 | `FALL_THROUGH`
<a id="insn-00abea4c"></a> `00abea4c` | `08 d5 3e 91` | add x8,x8,#0xfb5 | `FALL_THROUGH`
<a id="insn-00abea50"></a> `00abea50` | `e1 0b c0 3d` | ldr q1,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abea54"></a> `00abea54` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00abea58"></a> `00abea58` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abea5c"></a> `00abea5c` | `e0 43 00 f9` | str x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00abea60"></a> `00abea60` | `e1 1f 80 3d` | str q1,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abea64"></a> `00abea64` | `00 00 80 3d` | str q0,[x0] | `FALL_THROUGH`
<a id="insn-00abea68"></a> `00abea68` | `08 08 00 f9` | str x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00abea6c"></a> `00abea6c` | `1f 60 00 39` | strb wzr,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00abea70"></a> `00abea70` | `a8 43 01 d1` | sub x8,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00abea74"></a> `00abea74` | `a1 a3 01 d1` | sub x1,x29,#0x68 | `FALL_THROUGH`
<a id="insn-00abea78"></a> `00abea78` | `e2 c3 01 91` | add x2,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00abea7c"></a> `00abea7c` | `20 0f 00 d0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00abea80"></a> `00abea80` | `00 00 2c 91` | add x0,x0,#0xb00 | `FALL_THROUGH`
<a id="insn-00abea84"></a> `00abea84` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-00abea88"></a> `00abea88` | `d1 fe e6 97` | bl 0x0047e5cc | `UNCONDITIONAL_CALL`
<a id="insn-00abea8c"></a> `00abea8c` | `a0 03 db 3c` | ldur q0,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00abea90"></a> `00abea90` | `bf 7f 3b a9` | stp xzr,xzr,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00abea94"></a> `00abea94` | `3a 07 40 f9` | ldr x26,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00abea98"></a> `00abea98` | `20 03 80 3d` | str q0,[x25] | `FALL_THROUGH`
<a id="insn-00abea9c"></a> `00abea9c` | `ba 00 00 b4` | cbz x26,0x00abeab0 | `CONDITIONAL_JUMP`
<a id="insn-00abeaa0"></a> `00abeaa0` | `41 23 00 91` | add x1,x26,#0x8 | `FALL_THROUGH`
<a id="insn-00abeaa4"></a> `00abeaa4` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abeaa8"></a> `00abeaa8` | `8e 53 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00abeaac"></a> `00abeaac` | `00 1a 00 b4` | cbz x0,0x00abedec | `CONDITIONAL_JUMP`
<a id="insn-00abeab0"></a> `00abeab0` | `ba 83 5b f8` | ldur x26,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00abeab4"></a> `00abeab4` | `da 1a 00 b4` | cbz x26,0x00abee0c | `CONDITIONAL_JUMP`
<a id="insn-00abeab8"></a> `00abeab8` | `41 23 00 91` | add x1,x26,#0x8 | `FALL_THROUGH`
<a id="insn-00abeabc"></a> `00abeabc` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abeac0"></a> `00abeac0` | `88 53 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00abeac4"></a> `00abeac4` | `40 1a 00 b5` | cbnz x0,0x00abee0c | `CONDITIONAL_JUMP`
<a id="insn-00abeac8"></a> `00abeac8` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-00abeacc"></a> `00abeacc` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00abead0"></a> `00abead0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abead4"></a> `00abead4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abead8"></a> `00abead8` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00abeadc"></a> `00abeadc` | `e9 63 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00abeae0"></a> `00abeae0` | `cb 00 00 14` | b 0x00abee0c | `UNCONDITIONAL_JUMP`
<a id="insn-00abeae4"></a> `00abeae4` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00abeae8"></a> `00abeae8` | `e8 2d 00 36` | tbz w8,#0x0,0x00abf0a4 | `CONDITIONAL_JUMP`
<a id="insn-00abeaec"></a> `00abeaec` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-00abeaf0"></a> `00abeaf0` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-00abeaf4"></a> `00abeaf4` | `bf b3 1a 38` | sturb wzr,[x29, #-0x55] | `FALL_THROUGH`
<a id="insn-00abeaf8"></a> `00abeaf8` | `a8 83 19 38` | sturb w8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00abeafc"></a> `00abeafc` | `88 bf ff b0` | adrp x8,0x2af000 | `FALL_THROUGH`
<a id="insn-00abeb00"></a> `00abeb00` | `08 61 07 91` | add x8,x8,#0x1d8 | `FALL_THROUGH`
<a id="insn-00abeb04"></a> `00abeb04` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00abeb08"></a> `00abeb08` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abeb0c"></a> `00abeb0c` | `bf 63 19 38` | sturb wzr,[x29, #-0x6a] | `FALL_THROUGH`
<a id="insn-00abeb10"></a> `00abeb10` | `09 21 00 79` | strh w9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abeb14"></a> `00abeb14` | `49 05 80 52` | mov w9,#0x2a | `FALL_THROUGH`
<a id="insn-00abeb18"></a> `00abeb18` | `00 01 80 3d` | str q0,[x8] | `FALL_THROUGH`
<a id="insn-00abeb1c"></a> `00abeb1c` | `08 c0 ff b0` | adrp x8,0x2bf000 | `FALL_THROUGH`
<a id="insn-00abeb20"></a> `00abeb20` | `08 bd 1a 91` | add x8,x8,#0x6af | `FALL_THROUGH`
<a id="insn-00abeb24"></a> `00abeb24` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00abeb28"></a> `00abeb28` | `08 d1 40 f8` | ldur x8,[x8, #0xd] | `FALL_THROUGH`
<a id="insn-00abeb2c"></a> `00abeb2c` | `a9 03 18 38` | sturb w9,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00abeb30"></a> `00abeb30` | `60 03 80 3d` | str q0,[x27] | `FALL_THROUGH`
<a id="insn-00abeb34"></a> `00abeb34` | `68 d3 00 f8` | stur x8,[x27, #0xd] | `FALL_THROUGH`
<a id="insn-00abeb38"></a> `00abeb38` | `e8 c3 01 91` | add x8,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00abeb3c"></a> `00abeb3c` | `a1 a3 01 d1` | sub x1,x29,#0x68 | `FALL_THROUGH`
<a id="insn-00abeb40"></a> `00abeb40` | `a2 03 02 d1` | sub x2,x29,#0x80 | `FALL_THROUGH`
<a id="insn-00abeb44"></a> `00abeb44` | `20 0f 00 d0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00abeb48"></a> `00abeb48` | `00 00 2c 91` | add x0,x0,#0xb00 | `FALL_THROUGH`
<a id="insn-00abeb4c"></a> `00abeb4c` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-00abeb50"></a> `00abeb50` | `9f fe e6 97` | bl 0x0047e5cc | `UNCONDITIONAL_CALL`
<a id="insn-00abeb54"></a> `00abeb54` | `e0 1f c0 3d` | ldr q0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abeb58"></a> `00abeb58` | `ff 7f 07 a9` | stp xzr,xzr,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abeb5c"></a> `00abeb5c` | `3a 07 40 f9` | ldr x26,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00abeb60"></a> `00abeb60` | `20 03 80 3d` | str q0,[x25] | `FALL_THROUGH`
<a id="insn-00abeb64"></a> `00abeb64` | `ba 00 00 b4` | cbz x26,0x00abeb78 | `CONDITIONAL_JUMP`
<a id="insn-00abeb68"></a> `00abeb68` | `41 23 00 91` | add x1,x26,#0x8 | `FALL_THROUGH`
<a id="insn-00abeb6c"></a> `00abeb6c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abeb70"></a> `00abeb70` | `5c 53 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00abeb74"></a> `00abeb74` | `a0 11 00 b4` | cbz x0,0x00abeda8 | `CONDITIONAL_JUMP`
<a id="insn-00abeb78"></a> `00abeb78` | `fa 3f 40 f9` | ldr x26,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00abeb7c"></a> `00abeb7c` | `7a 12 00 b4` | cbz x26,0x00abedc8 | `CONDITIONAL_JUMP`
<a id="insn-00abeb80"></a> `00abeb80` | `41 23 00 91` | add x1,x26,#0x8 | `FALL_THROUGH`
<a id="insn-00abeb84"></a> `00abeb84` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abeb88"></a> `00abeb88` | `56 53 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00abeb8c"></a> `00abeb8c` | `e0 11 00 b5` | cbnz x0,0x00abedc8 | `CONDITIONAL_JUMP`
<a id="insn-00abeb90"></a> `00abeb90` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-00abeb94"></a> `00abeb94` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00abeb98"></a> `00abeb98` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abeb9c"></a> `00abeb9c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abeba0"></a> `00abeba0` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00abeba4"></a> `00abeba4` | `b7 63 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00abeba8"></a> `00abeba8` | `88 00 00 14` | b 0x00abedc8 | `UNCONDITIONAL_JUMP`
<a id="insn-00abebac"></a> `00abebac` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-00abebb0"></a> `00abebb0` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00abebb4"></a> `00abebb4` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abebb8"></a> `00abebb8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abebbc"></a> `00abebbc` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00abebc0"></a> `00abebc0` | `b0 63 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00abebc4"></a> `00abebc4` | `ba 83 5b f8` | ldur x26,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00abebc8"></a> `00abebc8` | `9a ee ff b5` | cbnz x26,0x00abe998 | `CONDITIONAL_JUMP`
<a id="insn-00abebcc"></a> `00abebcc` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abebd0"></a> `00abebd0` | `88 02 00 37` | tbnz w8,#0x0,0x00abec20 | `CONDITIONAL_JUMP`
<a id="insn-00abebd4"></a> `00abebd4` | `a8 83 59 38` | ldurb w8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00abebd8"></a> `00abebd8` | `c8 02 00 37` | tbnz w8,#0x0,0x00abec30 | `CONDITIONAL_JUMP`
<a id="insn-00abebdc"></a> `00abebdc` | `a8 03 58 38` | ldurb w8,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00abebe0"></a> `00abebe0` | `68 00 00 36` | tbz w8,#0x0,0x00abebec | `CONDITIONAL_JUMP`
<a id="insn-00abebe4"></a> `00abebe4` | `a0 03 59 f8` | ldur x0,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00abebe8"></a> `00abebe8` | `b2 63 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abebec"></a> `00abebec` | `e8 2f 40 f9` | ldr x8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00abebf0"></a> `00abebf0` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00abebf4"></a> `00abebf4` | `00 16 00 b4` | cbz x0,0x00abeeb4 | `CONDITIONAL_JUMP`
<a id="insn-00abebf8"></a> `00abebf8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00abebfc"></a> `00abebfc` | `03 00 00 14` | b 0x00abec08 | `UNCONDITIONAL_JUMP`
<a id="insn-00abec00"></a> `00abec00` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00abec04"></a> `00abec04` | `08 02 00 b4` | cbz x8,0x00abec44 | `CONDITIONAL_JUMP`
<a id="insn-00abec08"></a> `00abec08` | `09 1d 40 b9` | ldr w9,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00abec0c"></a> `00abec0c` | `3f 01 18 6b` | cmp w9,w24 | `FALL_THROUGH`
<a id="insn-00abec10"></a> `00abec10` | `8c ff ff 54` | b.gt 0x00abec00 | `CONDITIONAL_JUMP`
<a id="insn-00abec14"></a> `00abec14` | `ca 01 00 54` | b.ge 0x00abec4c | `CONDITIONAL_JUMP`
<a id="insn-00abec18"></a> `00abec18` | `08 21 00 91` | add x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00abec1c"></a> `00abec1c` | `f9 ff ff 17` | b 0x00abec00 | `UNCONDITIONAL_JUMP`
<a id="insn-00abec20"></a> `00abec20` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00abec24"></a> `00abec24` | `a3 63 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abec28"></a> `00abec28` | `a8 83 59 38` | ldurb w8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00abec2c"></a> `00abec2c` | `88 fd 07 36` | tbz w8,#0x0,0x00abebdc | `CONDITIONAL_JUMP`
<a id="insn-00abec30"></a> `00abec30` | `a0 83 5a f8` | ldur x0,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-00abec34"></a> `00abec34` | `9f 63 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abec38"></a> `00abec38` | `a8 03 58 38` | ldurb w8,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00abec3c"></a> `00abec3c` | `48 fd 07 37` | tbnz w8,#0x0,0x00abebe4 | `CONDITIONAL_JUMP`
<a id="insn-00abec40"></a> `00abec40` | `eb ff ff 17` | b 0x00abebec | `UNCONDITIONAL_JUMP`
<a id="insn-00abec44"></a> `00abec44` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00abec48"></a> `00abec48` | `14 00 00 14` | b 0x00abec98 | `UNCONDITIONAL_JUMP`
<a id="insn-00abec4c"></a> `00abec4c` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00abec50"></a> `00abec50` | `03 00 00 14` | b 0x00abec5c | `UNCONDITIONAL_JUMP`
<a id="insn-00abec54"></a> `00abec54` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00abec58"></a> `00abec58` | `c8 26 00 b4` | cbz x8,0x00abf130 | `CONDITIONAL_JUMP`
<a id="insn-00abec5c"></a> `00abec5c` | `09 1d 40 b9` | ldr w9,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00abec60"></a> `00abec60` | `3f 01 18 6b` | cmp w9,w24 | `FALL_THROUGH`
<a id="insn-00abec64"></a> `00abec64` | `8c ff ff 54` | b.gt 0x00abec54 | `CONDITIONAL_JUMP`
<a id="insn-00abec68"></a> `00abec68` | `8a 00 00 54` | b.ge 0x00abec78 | `CONDITIONAL_JUMP`
<a id="insn-00abec6c"></a> `00abec6c` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00abec70"></a> `00abec70` | `68 ff ff b5` | cbnz x8,0x00abec5c | `CONDITIONAL_JUMP`
<a id="insn-00abec74"></a> `00abec74` | `2f 01 00 14` | b 0x00abf130 | `UNCONDITIONAL_JUMP`
<a id="insn-00abec78"></a> `00abec78` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00abec7c"></a> `00abec7c` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00abec80"></a> `00abec80` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00abec84"></a> `00abec84` | `a1 00 00 54` | b.ne 0x00abec98 | `CONDITIONAL_JUMP`
<a id="insn-00abec88"></a> `00abec88` | `15 00 00 14` | b 0x00abecdc | `UNCONDITIONAL_JUMP`
<a id="insn-00abec8c"></a> `00abec8c` | `08 21 00 91` | add x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00abec90"></a> `00abec90` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00abec94"></a> `00abec94` | `08 11 00 b4` | cbz x8,0x00abeeb4 | `CONDITIONAL_JUMP`
<a id="insn-00abec98"></a> `00abec98` | `09 1d 40 b9` | ldr w9,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00abec9c"></a> `00abec9c` | `3f 01 18 6b` | cmp w9,w24 | `FALL_THROUGH`
<a id="insn-00abeca0"></a> `00abeca0` | `8c ff ff 54` | b.gt 0x00abec90 | `CONDITIONAL_JUMP`
<a id="insn-00abeca4"></a> `00abeca4` | `4b ff ff 54` | b.lt 0x00abec8c | `CONDITIONAL_JUMP`
<a id="insn-00abeca8"></a> `00abeca8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00abecac"></a> `00abecac` | `03 00 00 14` | b 0x00abecb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00abecb0"></a> `00abecb0` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00abecb4"></a> `00abecb4` | `e8 23 00 b4` | cbz x8,0x00abf130 | `CONDITIONAL_JUMP`
<a id="insn-00abecb8"></a> `00abecb8` | `09 1d 40 b9` | ldr w9,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00abecbc"></a> `00abecbc` | `3f 01 18 6b` | cmp w9,w24 | `FALL_THROUGH`
<a id="insn-00abecc0"></a> `00abecc0` | `8c ff ff 54` | b.gt 0x00abecb0 | `CONDITIONAL_JUMP`
<a id="insn-00abecc4"></a> `00abecc4` | `ea 01 00 54` | b.ge 0x00abed00 | `CONDITIONAL_JUMP`
<a id="insn-00abecc8"></a> `00abecc8` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00abeccc"></a> `00abeccc` | `68 ff ff b5` | cbnz x8,0x00abecb8 | `CONDITIONAL_JUMP`
<a id="insn-00abecd0"></a> `00abecd0` | `18 01 00 14` | b 0x00abf130 | `UNCONDITIONAL_JUMP`
<a id="insn-00abecd4"></a> `00abecd4` | `40 03 40 f9` | ldr x0,[x26] | `FALL_THROUGH`
<a id="insn-00abecd8"></a> `00abecd8` | `e0 0b 00 b4` | cbz x0,0x00abee54 | `CONDITIONAL_JUMP`
<a id="insn-00abecdc"></a> `00abecdc` | `08 1c 40 b9` | ldr w8,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00abece0"></a> `00abece0` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00abece4"></a> `00abece4` | `1f 01 18 6b` | cmp w8,w24 | `FALL_THROUGH`
<a id="insn-00abece8"></a> `00abece8` | `6c ff ff 54` | b.gt 0x00abecd4 | `CONDITIONAL_JUMP`
<a id="insn-00abecec"></a> `00abecec` | `ea 0d 00 54` | b.ge 0x00abeea8 | `CONDITIONAL_JUMP`
<a id="insn-00abecf0"></a> `00abecf0` | `40 07 40 f9` | ldr x0,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00abecf4"></a> `00abecf4` | `40 ff ff b5` | cbnz x0,0x00abecdc | `CONDITIONAL_JUMP`
<a id="insn-00abecf8"></a> `00abecf8` | `56 23 00 91` | add x22,x26,#0x8 | `FALL_THROUGH`
<a id="insn-00abecfc"></a> `00abecfc` | `57 00 00 14` | b 0x00abee58 | `UNCONDITIONAL_JUMP`
<a id="insn-00abed00"></a> `00abed00` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00abed04"></a> `00abed04` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00abed08"></a> `00abed08` | `61 0d 00 54` | b.ne 0x00abeeb4 | `CONDITIONAL_JUMP`
<a id="insn-00abed0c"></a> `00abed0c` | `e8 2f 40 f9` | ldr x8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00abed10"></a> `00abed10` | `e9 03 00 aa` | mov x9,x0 | `FALL_THROUGH`
<a id="insn-00abed14"></a> `00abed14` | `2a 1d 40 b9` | ldr w10,[x9, #0x1c] | `FALL_THROUGH`
<a id="insn-00abed18"></a> `00abed18` | `5f 01 18 6b` | cmp w10,w24 | `FALL_THROUGH`
<a id="insn-00abed1c"></a> `00abed1c` | `ea a7 9f 1a` | cset w10,lt | `FALL_THROUGH`
<a id="insn-00abed20"></a> `00abed20` | `08 b1 89 9a` | csel x8,x8,x9,lt | `FALL_THROUGH`
<a id="insn-00abed24"></a> `00abed24` | `29 59 6a f8` | ldr x9,[x9, w10, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00abed28"></a> `00abed28` | `69 ff ff b5` | cbnz x9,0x00abed14 | `CONDITIONAL_JUMP`
<a id="insn-00abed2c"></a> `00abed2c` | `e9 2f 40 f9` | ldr x9,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00abed30"></a> `00abed30` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abed34"></a> `00abed34` | `00 0c 00 54` | b.eq 0x00abeeb4 | `CONDITIONAL_JUMP`
<a id="insn-00abed38"></a> `00abed38` | `09 1d 40 b9` | ldr w9,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00abed3c"></a> `00abed3c` | `3f 01 18 6b` | cmp w9,w24 | `FALL_THROUGH`
<a id="insn-00abed40"></a> `00abed40` | `e9 2f 40 f9` | ldr x9,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00abed44"></a> `00abed44` | `3a c1 88 9a` | csel x26,x9,x8,gt | `FALL_THROUGH`
<a id="insn-00abed48"></a> `00abed48` | `6c 0b 00 54` | b.gt 0x00abeeb4 | `CONDITIONAL_JUMP`
<a id="insn-00abed4c"></a> `00abed4c` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00abed50"></a> `00abed50` | `aa 00 00 b4` | cbz x10,0x00abed64 | `CONDITIONAL_JUMP`
<a id="insn-00abed54"></a> `00abed54` | `e9 03 0a aa` | mov x9,x10 | `FALL_THROUGH`
<a id="insn-00abed58"></a> `00abed58` | `4a 01 40 f9` | ldr x10,[x10] | `FALL_THROUGH`
<a id="insn-00abed5c"></a> `00abed5c` | `ca ff ff b5` | cbnz x10,0x00abed54 | `CONDITIONAL_JUMP`
<a id="insn-00abed60"></a> `00abed60` | `06 00 00 14` | b 0x00abed78 | `UNCONDITIONAL_JUMP`
<a id="insn-00abed64"></a> `00abed64` | `09 09 40 f9` | ldr x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abed68"></a> `00abed68` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00abed6c"></a> `00abed6c` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00abed70"></a> `00abed70` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00abed74"></a> `00abed74` | `81 ff ff 54` | b.ne 0x00abed64 | `CONDITIONAL_JUMP`
<a id="insn-00abed78"></a> `00abed78` | `68 26 40 f9` | ldr x8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00abed7c"></a> `00abed7c` | `1f 01 1a eb` | cmp x8,x26 | `FALL_THROUGH`
<a id="insn-00abed80"></a> `00abed80` | `41 00 00 54` | b.ne 0x00abed88 | `CONDITIONAL_JUMP`
<a id="insn-00abed84"></a> `00abed84` | `69 26 00 f9` | str x9,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00abed88"></a> `00abed88` | `68 2e 40 f9` | ldr x8,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00abed8c"></a> `00abed8c` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00abed90"></a> `00abed90` | `08 05 00 d1` | sub x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00abed94"></a> `00abed94` | `68 2e 00 f9` | str x8,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00abed98"></a> `00abed98` | `0e 56 e7 97` | bl 0x004945d0 | `UNCONDITIONAL_CALL`
<a id="insn-00abed9c"></a> `00abed9c` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00abeda0"></a> `00abeda0` | `44 63 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abeda4"></a> `00abeda4` | `44 00 00 14` | b 0x00abeeb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00abeda8"></a> `00abeda8` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-00abedac"></a> `00abedac` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00abedb0"></a> `00abedb0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abedb4"></a> `00abedb4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abedb8"></a> `00abedb8` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00abedbc"></a> `00abedbc` | `31 63 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00abedc0"></a> `00abedc0` | `fa 3f 40 f9` | ldr x26,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00abedc4"></a> `00abedc4` | `fa ed ff b5` | cbnz x26,0x00abeb80 | `CONDITIONAL_JUMP`
<a id="insn-00abedc8"></a> `00abedc8` | `a8 03 58 38` | ldurb w8,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00abedcc"></a> `00abedcc` | `68 00 00 36` | tbz w8,#0x0,0x00abedd8 | `CONDITIONAL_JUMP`
<a id="insn-00abedd0"></a> `00abedd0` | `a0 03 59 f8` | ldur x0,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00abedd4"></a> `00abedd4` | `37 63 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abedd8"></a> `00abedd8` | `a8 83 59 38` | ldurb w8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00abeddc"></a> `00abeddc` | `c8 06 00 36` | tbz w8,#0x0,0x00abeeb4 | `CONDITIONAL_JUMP`
<a id="insn-00abede0"></a> `00abede0` | `a0 83 5a f8` | ldur x0,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-00abede4"></a> `00abede4` | `33 63 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abede8"></a> `00abede8` | `33 00 00 14` | b 0x00abeeb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00abedec"></a> `00abedec` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-00abedf0"></a> `00abedf0` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00abedf4"></a> `00abedf4` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abedf8"></a> `00abedf8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abedfc"></a> `00abedfc` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00abee00"></a> `00abee00` | `20 63 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00abee04"></a> `00abee04` | `ba 83 5b f8` | ldur x26,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00abee08"></a> `00abee08` | `9a e5 ff b5` | cbnz x26,0x00abeab8 | `CONDITIONAL_JUMP`
<a id="insn-00abee0c"></a> `00abee0c` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abee10"></a> `00abee10` | `c8 00 00 37` | tbnz w8,#0x0,0x00abee28 | `CONDITIONAL_JUMP`
<a id="insn-00abee14"></a> `00abee14` | `a8 83 59 38` | ldurb w8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00abee18"></a> `00abee18` | `08 01 00 37` | tbnz w8,#0x0,0x00abee38 | `CONDITIONAL_JUMP`
<a id="insn-00abee1c"></a> `00abee1c` | `a8 03 58 38` | ldurb w8,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00abee20"></a> `00abee20` | `48 01 00 37` | tbnz w8,#0x0,0x00abee48 | `CONDITIONAL_JUMP`
<a id="insn-00abee24"></a> `00abee24` | `24 00 00 14` | b 0x00abeeb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00abee28"></a> `00abee28` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00abee2c"></a> `00abee2c` | `21 63 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abee30"></a> `00abee30` | `a8 83 59 38` | ldurb w8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00abee34"></a> `00abee34` | `48 ff 07 36` | tbz w8,#0x0,0x00abee1c | `CONDITIONAL_JUMP`
<a id="insn-00abee38"></a> `00abee38` | `a0 83 5a f8` | ldur x0,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-00abee3c"></a> `00abee3c` | `1d 63 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abee40"></a> `00abee40` | `a8 03 58 38` | ldurb w8,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00abee44"></a> `00abee44` | `88 03 00 36` | tbz w8,#0x0,0x00abeeb4 | `CONDITIONAL_JUMP`
<a id="insn-00abee48"></a> `00abee48` | `a0 03 59 f8` | ldur x0,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00abee4c"></a> `00abee4c` | `19 63 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abee50"></a> `00abee50` | `19 00 00 14` | b 0x00abeeb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00abee54"></a> `00abee54` | `f6 03 1a aa` | mov x22,x26 | `FALL_THROUGH`
<a id="insn-00abee58"></a> `00abee58` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00abee5c"></a> `00abee5c` | `0d 63 06 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00abee60"></a> `00abee60` | `18 fc 03 29` | stp w24,wzr,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00abee64"></a> `00abee64` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00abee68"></a> `00abee68` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00abee6c"></a> `00abee6c` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00abee70"></a> `00abee70` | `1a 08 00 f9` | str x26,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00abee74"></a> `00abee74` | `c0 02 00 f9` | str x0,[x22] | `FALL_THROUGH`
<a id="insn-00abee78"></a> `00abee78` | `68 26 40 f9` | ldr x8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00abee7c"></a> `00abee7c` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00abee80"></a> `00abee80` | `68 00 00 b4` | cbz x8,0x00abee8c | `CONDITIONAL_JUMP`
<a id="insn-00abee84"></a> `00abee84` | `68 26 00 f9` | str x8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00abee88"></a> `00abee88` | `c1 02 40 f9` | ldr x1,[x22] | `FALL_THROUGH`
<a id="insn-00abee8c"></a> `00abee8c` | `60 2a 40 f9` | ldr x0,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-00abee90"></a> `00abee90` | `35 f3 e5 97` | bl 0x0043bb64 | `UNCONDITIONAL_CALL`
<a id="insn-00abee94"></a> `00abee94` | `68 2e 40 f9` | ldr x8,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00abee98"></a> `00abee98` | `16 e7 85 52` | mov w22,#0x2f38 | `FALL_THROUGH`
<a id="insn-00abee9c"></a> `00abee9c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00abeea0"></a> `00abeea0` | `68 2e 00 f9` | str x8,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00abeea4"></a> `00abeea4` | `02 00 00 14` | b 0x00abeeac | `UNCONDITIONAL_JUMP`
<a id="insn-00abeea8"></a> `00abeea8` | `f4 03 1a aa` | mov x20,x26 | `FALL_THROUGH`
<a id="insn-00abeeac"></a> `00abeeac` | `48 00 80 52` | mov w8,#0x2 | `FALL_THROUGH`
<a id="insn-00abeeb0"></a> `00abeeb0` | `88 22 00 b9` | str w8,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00abeeb4"></a> `00abeeb4` | `81 49 f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abeeb8"></a> `00abeeb8` | `b3 b6 e6 97` | bl 0x0046c984 | `UNCONDITIONAL_CALL`
<a id="insn-00abeebc"></a> `00abeebc` | `e8 10 80 52` | mov w8,#0x87 | `FALL_THROUGH`
<a id="insn-00abeec0"></a> `00abeec0` | `09 00 0f 71` | subs w9,w0,#0x3c0 | `FALL_THROUGH`
<a id="insn-00abeec4"></a> `00abeec4` | `0a fc 0e 51` | sub w10,w0,#0x3bf | `FALL_THROUGH`
<a id="insn-00abeec8"></a> `00abeec8` | `a8 7e 08 1b` | mul w8,w21,w8 | `FALL_THROUGH`
<a id="insn-00abeecc"></a> `00abeecc` | `49 b1 89 1a` | csel w9,w10,w9,lt | `FALL_THROUGH`
<a id="insn-00abeed0"></a> `00abeed0` | `82 4f 02 11` | add w2,w28,#0x93 | `FALL_THROUGH`
<a id="insn-00abeed4"></a> `00abeed4` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00abeed8"></a> `00abeed8` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00abeedc"></a> `00abeedc` | `1a 05 89 0b` | add w26,w8,w9, ASR #0x1 | `FALL_THROUGH`
<a id="insn-00abeee0"></a> `00abeee0` | `a8 a3 01 d1` | sub x8,x29,#0x68 | `FALL_THROUGH`
<a id="insn-00abeee4"></a> `00abeee4` | `41 4b 03 11` | add w1,w26,#0xd2 | `FALL_THROUGH`
<a id="insn-00abeee8"></a> `00abeee8` | `07 1e fe 97` | bl 0x00a46704 | `UNCONDITIONAL_CALL`
<a id="insn-00abeeec"></a> `00abeeec` | `a0 83 59 f8` | ldur x0,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00abeef0"></a> `00abeef0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00abeef4"></a> `00abeef4` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abeef8"></a> `00abeef8` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00abeefc"></a> `00abeefc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abef00"></a> `00abef00` | `6e 49 f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abef04"></a> `00abef04` | `a8 83 59 f8` | ldur x8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00abef08"></a> `00abef08` | `bf 83 19 f8` | stur xzr,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00abef0c"></a> `00abef0c` | `b8 03 1d f8` | stur x24,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-00abef10"></a> `00abef10` | `a8 03 18 f8` | stur x8,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00abef14"></a> `00abef14` | `68 0e 00 d0` | adrp x8,0xc8c000 | `FALL_THROUGH`
<a id="insn-00abef18"></a> `00abef18` | `08 81 3c 91` | add x8,x8,#0xf20 | `FALL_THROUGH`
<a id="insn-00abef1c"></a> `00abef1c` | `a8 4f 3c a9` | stp x8,x19,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00abef20"></a> `00abef20` | `a8 03 01 d1` | sub x8,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00abef24"></a> `00abef24` | `a8 03 1e f8` | stur x8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abef28"></a> `00abef28` | `e8 33 40 f9` | ldr x8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abef2c"></a> `00abef2c` | `00 00 16 8b` | add x0,x0,x22 | `FALL_THROUGH`
<a id="insn-00abef30"></a> `00abef30` | `42 6f 02 11` | add w2,w26,#0x9b | `FALL_THROUGH`
<a id="insn-00abef34"></a> `00abef34` | `83 73 01 11` | add w3,w28,#0x5c | `FALL_THROUGH`
<a id="insn-00abef38"></a> `00abef38` | `a6 03 02 d1` | sub x6,x29,#0x80 | `FALL_THROUGH`
<a id="insn-00abef3c"></a> `00abef3c` | `a7 03 01 d1` | sub x7,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00abef40"></a> `00abef40` | `01 01 15 0b` | add w1,w8,w21 | `FALL_THROUGH`
<a id="insn-00abef44"></a> `00abef44` | `c4 0d 80 52` | mov w4,#0x6e | `FALL_THROUGH`
<a id="insn-00abef48"></a> `00abef48` | `c5 0d 80 52` | mov w5,#0x6e | `FALL_THROUGH`
<a id="insn-00abef4c"></a> `00abef4c` | `17 e0 f7 97` | bl 0x008b6fa8 | `UNCONDITIONAL_CALL`
<a id="insn-00abef50"></a> `00abef50` | `a0 03 5e f8` | ldur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abef54"></a> `00abef54` | `a8 03 01 d1` | sub x8,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00abef58"></a> `00abef58` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00abef5c"></a> `00abef5c` | `80 00 00 54` | b.eq 0x00abef6c | `CONDITIONAL_JUMP`
<a id="insn-00abef60"></a> `00abef60` | `00 01 00 b4` | cbz x0,0x00abef80 | `CONDITIONAL_JUMP`
<a id="insn-00abef64"></a> `00abef64` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00abef68"></a> `00abef68` | `03 00 00 14` | b 0x00abef74 | `UNCONDITIONAL_JUMP`
<a id="insn-00abef6c"></a> `00abef6c` | `a0 03 01 d1` | sub x0,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00abef70"></a> `00abef70` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00abef74"></a> `00abef74` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00abef78"></a> `00abef78` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00abef7c"></a> `00abef7c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abef80"></a> `00abef80` | `b8 03 58 f8` | ldur x24,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00abef84"></a> `00abef84` | `bf 03 18 f8` | stur xzr,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00abef88"></a> `00abef88` | `38 01 00 b4` | cbz x24,0x00abefac | `CONDITIONAL_JUMP`
<a id="insn-00abef8c"></a> `00abef8c` | `e8 0e 00 90` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-00abef90"></a> `00abef90` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00abef94"></a> `00abef94` | `08 b5 47 f9` | ldr x8,[x8, #0xf68] | `FALL_THROUGH`
<a id="insn-00abef98"></a> `00abef98` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00abef9c"></a> `00abef9c` | `08 04 05 f8` | str x8,[x0], #0x50 | `FALL_THROUGH`
<a id="insn-00abefa0"></a> `00abefa0` | `fa 66 ec 97` | bl 0x005d8b88 | `UNCONDITIONAL_CALL`
<a id="insn-00abefa4"></a> `00abefa4` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00abefa8"></a> `00abefa8` | `c2 62 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abefac"></a> `00abefac` | `b8 83 59 f8` | ldur x24,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00abefb0"></a> `00abefb0` | `bf 83 19 f8` | stur xzr,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00abefb4"></a> `00abefb4` | `18 c6 ff b4` | cbz x24,0x00abe874 | `CONDITIONAL_JUMP`
<a id="insn-00abefb8"></a> `00abefb8` | `19 5b 40 f9` | ldr x25,[x24, #0xb0] | `FALL_THROUGH`
<a id="insn-00abefbc"></a> `00abefbc` | `e8 27 40 f9` | ldr x8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00abefc0"></a> `00abefc0` | `08 03 00 f9` | str x8,[x24] | `FALL_THROUGH`
<a id="insn-00abefc4"></a> `00abefc4` | `d9 c4 ff b4` | cbz x25,0x00abe85c | `CONDITIONAL_JUMP`
<a id="insn-00abefc8"></a> `00abefc8` | `21 23 00 91` | add x1,x25,#0x8 | `FALL_THROUGH`
<a id="insn-00abefcc"></a> `00abefcc` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abefd0"></a> `00abefd0` | `44 52 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00abefd4"></a> `00abefd4` | `40 c4 ff b5` | cbnz x0,0x00abe85c | `CONDITIONAL_JUMP`
<a id="insn-00abefd8"></a> `00abefd8` | `28 03 40 f9` | ldr x8,[x25] | `FALL_THROUGH`
<a id="insn-00abefdc"></a> `00abefdc` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00abefe0"></a> `00abefe0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abefe4"></a> `00abefe4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abefe8"></a> `00abefe8` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00abefec"></a> `00abefec` | `a5 62 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00abeff0"></a> `00abeff0` | `1b fe ff 17` | b 0x00abe85c | `UNCONDITIONAL_JUMP`
<a id="insn-00abeff4"></a> `00abeff4` | `20 0f 00 d0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00abeff8"></a> `00abeff8` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00abeffc"></a> `00abeffc` | `95 62 06 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-00abf000"></a> `00abf000` | `c0 c7 ff 34` | cbz w0,0x00abe8f8 | `CONDITIONAL_JUMP`
<a id="insn-00abf004"></a> `00abf004` | `21 0f 00 b0` | adrp x1,0xca4000 | `FALL_THROUGH`
<a id="insn-00abf008"></a> `00abf008` | `21 00 2c 91` | add x1,x1,#0xb00 | `FALL_THROUGH`
<a id="insn-00abf00c"></a> `00abf00c` | `e0 cd ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-00abf010"></a> `00abf010` | `00 d0 35 91` | add x0,x0,#0xd74 | `FALL_THROUGH`
<a id="insn-00abf014"></a> `00abf014` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00abf018"></a> `00abf018` | `02 0d 00 f0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-00abf01c"></a> `00abf01c` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-00abf020"></a> `00abf020` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00abf024"></a> `00abf024` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00abf028"></a> `00abf028` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00abf02c"></a> `00abf02c` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00abf030"></a> `00abf030` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00abf034"></a> `00abf034` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00abf038"></a> `00abf038` | `7e 62 06 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-00abf03c"></a> `00abf03c` | `20 0f 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00abf040"></a> `00abf040` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00abf044"></a> `00abf044` | `8b 62 06 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-00abf048"></a> `00abf048` | `2c fe ff 17` | b 0x00abe8f8 | `UNCONDITIONAL_JUMP`
<a id="insn-00abf04c"></a> `00abf04c` | `20 0f 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00abf050"></a> `00abf050` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00abf054"></a> `00abf054` | `7f 62 06 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-00abf058"></a> `00abf058` | `e0 cc ff 34` | cbz w0,0x00abe9f4 | `CONDITIONAL_JUMP`
<a id="insn-00abf05c"></a> `00abf05c` | `21 0f 00 b0` | adrp x1,0xca4000 | `FALL_THROUGH`
<a id="insn-00abf060"></a> `00abf060` | `21 00 2c 91` | add x1,x1,#0xb00 | `FALL_THROUGH`
<a id="insn-00abf064"></a> `00abf064` | `e0 cd ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-00abf068"></a> `00abf068` | `00 d0 35 91` | add x0,x0,#0xd74 | `FALL_THROUGH`
<a id="insn-00abf06c"></a> `00abf06c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00abf070"></a> `00abf070` | `02 0d 00 f0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-00abf074"></a> `00abf074` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-00abf078"></a> `00abf078` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00abf07c"></a> `00abf07c` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00abf080"></a> `00abf080` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00abf084"></a> `00abf084` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00abf088"></a> `00abf088` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00abf08c"></a> `00abf08c` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00abf090"></a> `00abf090` | `68 62 06 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-00abf094"></a> `00abf094` | `20 0f 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00abf098"></a> `00abf098` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00abf09c"></a> `00abf09c` | `75 62 06 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-00abf0a0"></a> `00abf0a0` | `55 fe ff 17` | b 0x00abe9f4 | `UNCONDITIONAL_JUMP`
<a id="insn-00abf0a4"></a> `00abf0a4` | `20 0f 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00abf0a8"></a> `00abf0a8` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00abf0ac"></a> `00abf0ac` | `69 62 06 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-00abf0b0"></a> `00abf0b0` | `e0 d1 ff 34` | cbz w0,0x00abeaec | `CONDITIONAL_JUMP`
<a id="insn-00abf0b4"></a> `00abf0b4` | `21 0f 00 b0` | adrp x1,0xca4000 | `FALL_THROUGH`
<a id="insn-00abf0b8"></a> `00abf0b8` | `21 00 2c 91` | add x1,x1,#0xb00 | `FALL_THROUGH`
<a id="insn-00abf0bc"></a> `00abf0bc` | `e0 cd ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-00abf0c0"></a> `00abf0c0` | `00 d0 35 91` | add x0,x0,#0xd74 | `FALL_THROUGH`
<a id="insn-00abf0c4"></a> `00abf0c4` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00abf0c8"></a> `00abf0c8` | `02 0d 00 f0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-00abf0cc"></a> `00abf0cc` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-00abf0d0"></a> `00abf0d0` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00abf0d4"></a> `00abf0d4` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00abf0d8"></a> `00abf0d8` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00abf0dc"></a> `00abf0dc` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00abf0e0"></a> `00abf0e0` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00abf0e4"></a> `00abf0e4` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00abf0e8"></a> `00abf0e8` | `52 62 06 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-00abf0ec"></a> `00abf0ec` | `20 0f 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00abf0f0"></a> `00abf0f0` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00abf0f4"></a> `00abf0f4` | `5f 62 06 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-00abf0f8"></a> `00abf0f8` | `7d fe ff 17` | b 0x00abeaec | `UNCONDITIONAL_JUMP`
<a id="insn-00abf0fc"></a> `00abf0fc` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abf100"></a> `00abf100` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00abf104"></a> `00abf104` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abf108"></a> `00abf108` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abf10c"></a> `00abf10c` | `21 0d 00 54` | b.ne 0x00abf2b0 | `CONDITIONAL_JUMP`
<a id="insn-00abf110"></a> `00abf110` | `f4 4f 56 a9` | ldp x20,x19,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-00abf114"></a> `00abf114` | `f6 57 55 a9` | ldp x22,x21,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00abf118"></a> `00abf118` | `f8 5f 54 a9` | ldp x24,x23,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00abf11c"></a> `00abf11c` | `fa 67 53 a9` | ldp x26,x25,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00abf120"></a> `00abf120` | `fc 6f 52 a9` | ldp x28,x27,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00abf124"></a> `00abf124` | `fd 7b 51 a9` | ldp x29,x30,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00abf128"></a> `00abf128` | `ff c3 05 91` | add sp,sp,#0x170 | `FALL_THROUGH`
<a id="insn-00abf12c"></a> `00abf12c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00abf130"></a> `00abf130` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abf134"></a> `00abf134` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00abf138"></a> `00abf138` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abf13c"></a> `00abf13c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abf140"></a> `00abf140` | `81 0b 00 54` | b.ne 0x00abf2b0 | `CONDITIONAL_JUMP`
<a id="insn-00abf144"></a> `00abf144` | `00 bf ff b0` | adrp x0,0x2a0000 | `FALL_THROUGH`
<a id="insn-00abf148"></a> `00abf148` | `00 c0 03 91` | add x0,x0,#0xf0 | `FALL_THROUGH`
<a id="insn-00abf14c"></a> `00abf14c` | `e9 0d e6 97` | bl 0x004428f0 | `CALL_TERMINATOR`
<a id="insn-00abf150"></a> `00abf150` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abf154"></a> `00abf154` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00abf158"></a> `00abf158` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abf15c"></a> `00abf15c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abf160"></a> `00abf160` | `81 0a 00 54` | b.ne 0x00abf2b0 | `CONDITIONAL_JUMP`
<a id="insn-00abf164"></a> `00abf164` | `60 62 00 91` | add x0,x19,#0x18 | `FALL_THROUGH`
<a id="insn-00abf168"></a> `00abf168` | `5b 0a 00 94` | bl 0x00ac1ad4 | `UNCONDITIONAL_CALL`
<a id="insn-00abf16c"></a> `00abf16c` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abf170"></a> `00abf170` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00abf174"></a> `00abf174` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abf178"></a> `00abf178` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abf17c"></a> `00abf17c` | `a1 09 00 54` | b.ne 0x00abf2b0 | `CONDITIONAL_JUMP`
<a id="insn-00abf180"></a> `00abf180` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00abf184"></a> `00abf184` | `19 07 00 94` | bl 0x00ac0de8 | `UNCONDITIONAL_CALL`
<a id="insn-00abf188"></a> `00abf188` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abf18c"></a> `00abf18c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00abf190"></a> `00abf190` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abf194"></a> `00abf194` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abf198"></a> `00abf198` | `c1 08 00 54` | b.ne 0x00abf2b0 | `CONDITIONAL_JUMP`
<a id="insn-00abf19c"></a> `00abf19c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00abf1a0"></a> `00abf1a0` | `12 07 00 94` | bl 0x00ac0de8 | `UNCONDITIONAL_CALL`
<a id="insn-00abf1a4"></a> `00abf1a4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00abf1a8"></a> `00abf1a8` | `a8 83 59 38` | ldurb w8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00abf1ac"></a> `00abf1ac` | `88 02 00 36` | tbz w8,#0x0,0x00abf1fc | `CONDITIONAL_JUMP`
<a id="insn-00abf1b0"></a> `00abf1b0` | `1a 00 00 14` | b 0x00abf218 | `UNCONDITIONAL_JUMP`
<a id="insn-00abf1fc"></a> `00abf1fc` | `a8 03 58 38` | ldurb w8,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00abf200"></a> `00abf200` | `c8 01 00 37` | tbnz w8,#0x0,0x00abf238 | `CONDITIONAL_JUMP`
<a id="insn-00abf204"></a> `00abf204` | `24 00 00 14` | b 0x00abf294 | `UNCONDITIONAL_JUMP`
<a id="insn-00abf218"></a> `00abf218` | `a0 83 5a f8` | ldur x0,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-00abf21c"></a> `00abf21c` | `25 62 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abf220"></a> `00abf220` | `a8 03 58 38` | ldurb w8,[x29, #-0x80] | `FALL_THROUGH`
<a id="insn-00abf224"></a> `00abf224` | `a8 00 00 37` | tbnz w8,#0x0,0x00abf238 | `CONDITIONAL_JUMP`
<a id="insn-00abf228"></a> `00abf228` | `1b 00 00 14` | b 0x00abf294 | `UNCONDITIONAL_JUMP`
<a id="insn-00abf238"></a> `00abf238` | `a0 03 59 f8` | ldur x0,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00abf23c"></a> `00abf23c` | `1d 62 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abf240"></a> `00abf240` | `15 00 00 14` | b 0x00abf294 | `UNCONDITIONAL_JUMP`
<a id="insn-00abf294"></a> `00abf294` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abf298"></a> `00abf298` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00abf29c"></a> `00abf29c` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abf2a0"></a> `00abf2a0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abf2a4"></a> `00abf2a4` | `61 00 00 54` | b.ne 0x00abf2b0 | `CONDITIONAL_JUMP`
<a id="insn-00abf2a8"></a> `00abf2a8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00abf2ac"></a> `00abf2ac` | `24 52 06 94` | bl 0x00c53b3c | `CALL_TERMINATOR`
<a id="insn-00abf2b0"></a> `00abf2b0` | `0c 62 06 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00abe5fc`](#insn-00abe5fc) 範囲 `[['00abe5fc', '00abe5ff']]`
  - `FALL_THROUGH` [`00abe5fc`](#insn-00abe5fc) → [`00abe600`](#insn-00abe600)
- ブロック [`00abe600`](#insn-00abe600) 範囲 `[['00abe600', '00abe637']]`
  - `FALL_THROUGH` [`00abe634`](#insn-00abe634) → [`00abe638`](#insn-00abe638)
- ブロック [`00abe638`](#insn-00abe638) 範囲 `[['00abe638', '00abe63f']]`
  - `CONDITIONAL_JUMP` [`00abe63c`](#insn-00abe63c) → [`00abe664`](#insn-00abe664)
  - `FALL_THROUGH` [`00abe63c`](#insn-00abe63c) → [`00abe640`](#insn-00abe640)
- ブロック [`00abe640`](#insn-00abe640) 範囲 `[['00abe640', '00abe663']]`
  - `UNCONDITIONAL_JUMP` [`00abe660`](#insn-00abe660) → [`00abe668`](#insn-00abe668)
- ブロック [`00abe664`](#insn-00abe664) 範囲 `[['00abe664', '00abe667']]`
  - `FALL_THROUGH` [`00abe664`](#insn-00abe664) → [`00abe668`](#insn-00abe668)
- ブロック [`00abe668`](#insn-00abe668) 範囲 `[['00abe668', '00abe817']]`
  - `UNCONDITIONAL_JUMP` [`00abe814`](#insn-00abe814) → [`00abe828`](#insn-00abe828)
- ブロック [`00abe818`](#insn-00abe818) 範囲 `[['00abe818', '00abe827']]`
  - `CONDITIONAL_JUMP` [`00abe824`](#insn-00abe824) → [`00abf0fc`](#insn-00abf0fc)
  - `FALL_THROUGH` [`00abe824`](#insn-00abe824) → [`00abe828`](#insn-00abe828)
- ブロック [`00abe828`](#insn-00abe828) 範囲 `[['00abe828', '00abe85b']]`
  - `UNCONDITIONAL_JUMP` [`00abe858`](#insn-00abe858) → [`00abe880`](#insn-00abe880)
- ブロック [`00abe85c`](#insn-00abe85c) 範囲 `[['00abe85c', '00abe873']]`
  - `FALL_THROUGH` [`00abe870`](#insn-00abe870) → [`00abe874`](#insn-00abe874)
- ブロック [`00abe874`](#insn-00abe874) 範囲 `[['00abe874', '00abe87f']]`
  - `CONDITIONAL_JUMP` [`00abe87c`](#insn-00abe87c) → [`00abe818`](#insn-00abe818)
  - `FALL_THROUGH` [`00abe87c`](#insn-00abe87c) → [`00abe880`](#insn-00abe880)
- ブロック [`00abe880`](#insn-00abe880) 範囲 `[['00abe880', '00abe897']]`
  - `CONDITIONAL_JUMP` [`00abe894`](#insn-00abe894) → [`00abe818`](#insn-00abe818)
  - `FALL_THROUGH` [`00abe894`](#insn-00abe894) → [`00abe898`](#insn-00abe898)
- ブロック [`00abe898`](#insn-00abe898) 範囲 `[['00abe898', '00abe8a7']]`
  - `CONDITIONAL_JUMP` [`00abe8a4`](#insn-00abe8a4) → [`00abf150`](#insn-00abf150)
  - `FALL_THROUGH` [`00abe8a4`](#insn-00abe8a4) → [`00abe8a8`](#insn-00abe8a8)
- ブロック [`00abe8a8`](#insn-00abe8a8) 範囲 `[['00abe8a8', '00abe8b7']]`
  - `CONDITIONAL_JUMP` [`00abe8b4`](#insn-00abe8b4) → [`00abe818`](#insn-00abe818)
  - `FALL_THROUGH` [`00abe8b4`](#insn-00abe8b4) → [`00abe8b8`](#insn-00abe8b8)
- ブロック [`00abe8b8`](#insn-00abe8b8) 範囲 `[['00abe8b8', '00abe8e7']]`
  - `CONDITIONAL_JUMP` [`00abe8e4`](#insn-00abe8e4) → [`00abe9c4`](#insn-00abe9c4)
  - `FALL_THROUGH` [`00abe8e4`](#insn-00abe8e4) → [`00abe8e8`](#insn-00abe8e8)
- ブロック [`00abe8e8`](#insn-00abe8e8) 範囲 `[['00abe8e8', '00abe8f7']]`
  - `CONDITIONAL_JUMP` [`00abe8f4`](#insn-00abe8f4) → [`00abeff4`](#insn-00abeff4)
  - `FALL_THROUGH` [`00abe8f4`](#insn-00abe8f4) → [`00abe8f8`](#insn-00abe8f8)
- ブロック [`00abe8f8`](#insn-00abe8f8) 範囲 `[['00abe8f8', '00abe97f']]`
  - `CONDITIONAL_JUMP` [`00abe97c`](#insn-00abe97c) → [`00abe990`](#insn-00abe990)
  - `FALL_THROUGH` [`00abe97c`](#insn-00abe97c) → [`00abe980`](#insn-00abe980)
- ブロック [`00abe980`](#insn-00abe980) 範囲 `[['00abe980', '00abe98f']]`
  - `CONDITIONAL_JUMP` [`00abe98c`](#insn-00abe98c) → [`00abebac`](#insn-00abebac)
  - `FALL_THROUGH` [`00abe98c`](#insn-00abe98c) → [`00abe990`](#insn-00abe990)
- ブロック [`00abe990`](#insn-00abe990) 範囲 `[['00abe990', '00abe997']]`
  - `CONDITIONAL_JUMP` [`00abe994`](#insn-00abe994) → [`00abebcc`](#insn-00abebcc)
  - `FALL_THROUGH` [`00abe994`](#insn-00abe994) → [`00abe998`](#insn-00abe998)
- ブロック [`00abe998`](#insn-00abe998) 範囲 `[['00abe998', '00abe9a7']]`
  - `CONDITIONAL_JUMP` [`00abe9a4`](#insn-00abe9a4) → [`00abebcc`](#insn-00abebcc)
  - `FALL_THROUGH` [`00abe9a4`](#insn-00abe9a4) → [`00abe9a8`](#insn-00abe9a8)
- ブロック [`00abe9a8`](#insn-00abe9a8) 範囲 `[['00abe9a8', '00abe9c3']]`
  - `UNCONDITIONAL_JUMP` [`00abe9c0`](#insn-00abe9c0) → [`00abebcc`](#insn-00abebcc)
- ブロック [`00abe9c4`](#insn-00abe9c4) 範囲 `[['00abe9c4', '00abe9d7']]`
  - `CONDITIONAL_JUMP` [`00abe9d4`](#insn-00abe9d4) → [`00abf16c`](#insn-00abf16c)
  - `FALL_THROUGH` [`00abe9d4`](#insn-00abe9d4) → [`00abe9d8`](#insn-00abe9d8)
- ブロック [`00abe9d8`](#insn-00abe9d8) 範囲 `[['00abe9d8', '00abe9eb']]`
  - `CONDITIONAL_JUMP` [`00abe9e8`](#insn-00abe9e8) → [`00abeae4`](#insn-00abeae4)
  - `FALL_THROUGH` [`00abe9e8`](#insn-00abe9e8) → [`00abe9ec`](#insn-00abe9ec)
- ブロック [`00abe9ec`](#insn-00abe9ec) 範囲 `[['00abe9ec', '00abe9f3']]`
  - `CONDITIONAL_JUMP` [`00abe9f0`](#insn-00abe9f0) → [`00abf04c`](#insn-00abf04c)
  - `FALL_THROUGH` [`00abe9f0`](#insn-00abe9f0) → [`00abe9f4`](#insn-00abe9f4)
- ブロック [`00abe9f4`](#insn-00abe9f4) 範囲 `[['00abe9f4', '00abea27']]`
  - `CONDITIONAL_JUMP` [`00abea24`](#insn-00abea24) → [`00abf188`](#insn-00abf188)
  - `FALL_THROUGH` [`00abea24`](#insn-00abea24) → [`00abea28`](#insn-00abea28)
- ブロック [`00abea28`](#insn-00abea28) 範囲 `[['00abea28', '00abea9f']]`
  - `CONDITIONAL_JUMP` [`00abea9c`](#insn-00abea9c) → [`00abeab0`](#insn-00abeab0)
  - `FALL_THROUGH` [`00abea9c`](#insn-00abea9c) → [`00abeaa0`](#insn-00abeaa0)
- ブロック [`00abeaa0`](#insn-00abeaa0) 範囲 `[['00abeaa0', '00abeaaf']]`
  - `CONDITIONAL_JUMP` [`00abeaac`](#insn-00abeaac) → [`00abedec`](#insn-00abedec)
  - `FALL_THROUGH` [`00abeaac`](#insn-00abeaac) → [`00abeab0`](#insn-00abeab0)
- ブロック [`00abeab0`](#insn-00abeab0) 範囲 `[['00abeab0', '00abeab7']]`
  - `CONDITIONAL_JUMP` [`00abeab4`](#insn-00abeab4) → [`00abee0c`](#insn-00abee0c)
  - `FALL_THROUGH` [`00abeab4`](#insn-00abeab4) → [`00abeab8`](#insn-00abeab8)
- ブロック [`00abeab8`](#insn-00abeab8) 範囲 `[['00abeab8', '00abeac7']]`
  - `CONDITIONAL_JUMP` [`00abeac4`](#insn-00abeac4) → [`00abee0c`](#insn-00abee0c)
  - `FALL_THROUGH` [`00abeac4`](#insn-00abeac4) → [`00abeac8`](#insn-00abeac8)
- ブロック [`00abeac8`](#insn-00abeac8) 範囲 `[['00abeac8', '00abeae3']]`
  - `UNCONDITIONAL_JUMP` [`00abeae0`](#insn-00abeae0) → [`00abee0c`](#insn-00abee0c)
- ブロック [`00abeae4`](#insn-00abeae4) 範囲 `[['00abeae4', '00abeaeb']]`
  - `CONDITIONAL_JUMP` [`00abeae8`](#insn-00abeae8) → [`00abf0a4`](#insn-00abf0a4)
  - `FALL_THROUGH` [`00abeae8`](#insn-00abeae8) → [`00abeaec`](#insn-00abeaec)
- ブロック [`00abeaec`](#insn-00abeaec) 範囲 `[['00abeaec', '00abeb67']]`
  - `CONDITIONAL_JUMP` [`00abeb64`](#insn-00abeb64) → [`00abeb78`](#insn-00abeb78)
  - `FALL_THROUGH` [`00abeb64`](#insn-00abeb64) → [`00abeb68`](#insn-00abeb68)
- ブロック [`00abeb68`](#insn-00abeb68) 範囲 `[['00abeb68', '00abeb77']]`
  - `CONDITIONAL_JUMP` [`00abeb74`](#insn-00abeb74) → [`00abeda8`](#insn-00abeda8)
  - `FALL_THROUGH` [`00abeb74`](#insn-00abeb74) → [`00abeb78`](#insn-00abeb78)
- ブロック [`00abeb78`](#insn-00abeb78) 範囲 `[['00abeb78', '00abeb7f']]`
  - `CONDITIONAL_JUMP` [`00abeb7c`](#insn-00abeb7c) → [`00abedc8`](#insn-00abedc8)
  - `FALL_THROUGH` [`00abeb7c`](#insn-00abeb7c) → [`00abeb80`](#insn-00abeb80)
- ブロック [`00abeb80`](#insn-00abeb80) 範囲 `[['00abeb80', '00abeb8f']]`
  - `CONDITIONAL_JUMP` [`00abeb8c`](#insn-00abeb8c) → [`00abedc8`](#insn-00abedc8)
  - `FALL_THROUGH` [`00abeb8c`](#insn-00abeb8c) → [`00abeb90`](#insn-00abeb90)
- ブロック [`00abeb90`](#insn-00abeb90) 範囲 `[['00abeb90', '00abebab']]`
  - `UNCONDITIONAL_JUMP` [`00abeba8`](#insn-00abeba8) → [`00abedc8`](#insn-00abedc8)
- ブロック [`00abebac`](#insn-00abebac) 範囲 `[['00abebac', '00abebcb']]`
  - `CONDITIONAL_JUMP` [`00abebc8`](#insn-00abebc8) → [`00abe998`](#insn-00abe998)
  - `FALL_THROUGH` [`00abebc8`](#insn-00abebc8) → [`00abebcc`](#insn-00abebcc)
- ブロック [`00abebcc`](#insn-00abebcc) 範囲 `[['00abebcc', '00abebd3']]`
  - `CONDITIONAL_JUMP` [`00abebd0`](#insn-00abebd0) → [`00abec20`](#insn-00abec20)
  - `FALL_THROUGH` [`00abebd0`](#insn-00abebd0) → [`00abebd4`](#insn-00abebd4)
- ブロック [`00abebd4`](#insn-00abebd4) 範囲 `[['00abebd4', '00abebdb']]`
  - `CONDITIONAL_JUMP` [`00abebd8`](#insn-00abebd8) → [`00abec30`](#insn-00abec30)
  - `FALL_THROUGH` [`00abebd8`](#insn-00abebd8) → [`00abebdc`](#insn-00abebdc)
- ブロック [`00abebdc`](#insn-00abebdc) 範囲 `[['00abebdc', '00abebe3']]`
  - `CONDITIONAL_JUMP` [`00abebe0`](#insn-00abebe0) → [`00abebec`](#insn-00abebec)
  - `FALL_THROUGH` [`00abebe0`](#insn-00abebe0) → [`00abebe4`](#insn-00abebe4)
- ブロック [`00abebe4`](#insn-00abebe4) 範囲 `[['00abebe4', '00abebeb']]`
  - `FALL_THROUGH` [`00abebe8`](#insn-00abebe8) → [`00abebec`](#insn-00abebec)
- ブロック [`00abebec`](#insn-00abebec) 範囲 `[['00abebec', '00abebf7']]`
  - `CONDITIONAL_JUMP` [`00abebf4`](#insn-00abebf4) → [`00abeeb4`](#insn-00abeeb4)
  - `FALL_THROUGH` [`00abebf4`](#insn-00abebf4) → [`00abebf8`](#insn-00abebf8)
- ブロック [`00abebf8`](#insn-00abebf8) 範囲 `[['00abebf8', '00abebff']]`
  - `UNCONDITIONAL_JUMP` [`00abebfc`](#insn-00abebfc) → [`00abec08`](#insn-00abec08)
- ブロック [`00abec00`](#insn-00abec00) 範囲 `[['00abec00', '00abec07']]`
  - `CONDITIONAL_JUMP` [`00abec04`](#insn-00abec04) → [`00abec44`](#insn-00abec44)
  - `FALL_THROUGH` [`00abec04`](#insn-00abec04) → [`00abec08`](#insn-00abec08)
- ブロック [`00abec08`](#insn-00abec08) 範囲 `[['00abec08', '00abec13']]`
  - `CONDITIONAL_JUMP` [`00abec10`](#insn-00abec10) → [`00abec00`](#insn-00abec00)
  - `FALL_THROUGH` [`00abec10`](#insn-00abec10) → [`00abec14`](#insn-00abec14)
- ブロック [`00abec14`](#insn-00abec14) 範囲 `[['00abec14', '00abec17']]`
  - `CONDITIONAL_JUMP` [`00abec14`](#insn-00abec14) → [`00abec4c`](#insn-00abec4c)
  - `FALL_THROUGH` [`00abec14`](#insn-00abec14) → [`00abec18`](#insn-00abec18)
- ブロック [`00abec18`](#insn-00abec18) 範囲 `[['00abec18', '00abec1f']]`
  - `UNCONDITIONAL_JUMP` [`00abec1c`](#insn-00abec1c) → [`00abec00`](#insn-00abec00)
- ブロック [`00abec20`](#insn-00abec20) 範囲 `[['00abec20', '00abec2f']]`
  - `CONDITIONAL_JUMP` [`00abec2c`](#insn-00abec2c) → [`00abebdc`](#insn-00abebdc)
  - `FALL_THROUGH` [`00abec2c`](#insn-00abec2c) → [`00abec30`](#insn-00abec30)
- ブロック [`00abec30`](#insn-00abec30) 範囲 `[['00abec30', '00abec3f']]`
  - `CONDITIONAL_JUMP` [`00abec3c`](#insn-00abec3c) → [`00abebe4`](#insn-00abebe4)
  - `FALL_THROUGH` [`00abec3c`](#insn-00abec3c) → [`00abec40`](#insn-00abec40)
- ブロック [`00abec40`](#insn-00abec40) 範囲 `[['00abec40', '00abec43']]`
  - `UNCONDITIONAL_JUMP` [`00abec40`](#insn-00abec40) → [`00abebec`](#insn-00abebec)
- ブロック [`00abec44`](#insn-00abec44) 範囲 `[['00abec44', '00abec4b']]`
  - `UNCONDITIONAL_JUMP` [`00abec48`](#insn-00abec48) → [`00abec98`](#insn-00abec98)
- ブロック [`00abec4c`](#insn-00abec4c) 範囲 `[['00abec4c', '00abec53']]`
  - `UNCONDITIONAL_JUMP` [`00abec50`](#insn-00abec50) → [`00abec5c`](#insn-00abec5c)
- ブロック [`00abec54`](#insn-00abec54) 範囲 `[['00abec54', '00abec5b']]`
  - `CONDITIONAL_JUMP` [`00abec58`](#insn-00abec58) → [`00abf130`](#insn-00abf130)
  - `FALL_THROUGH` [`00abec58`](#insn-00abec58) → [`00abec5c`](#insn-00abec5c)
- ブロック [`00abec5c`](#insn-00abec5c) 範囲 `[['00abec5c', '00abec67']]`
  - `CONDITIONAL_JUMP` [`00abec64`](#insn-00abec64) → [`00abec54`](#insn-00abec54)
  - `FALL_THROUGH` [`00abec64`](#insn-00abec64) → [`00abec68`](#insn-00abec68)
- ブロック [`00abec68`](#insn-00abec68) 範囲 `[['00abec68', '00abec6b']]`
  - `CONDITIONAL_JUMP` [`00abec68`](#insn-00abec68) → [`00abec78`](#insn-00abec78)
  - `FALL_THROUGH` [`00abec68`](#insn-00abec68) → [`00abec6c`](#insn-00abec6c)
- ブロック [`00abec6c`](#insn-00abec6c) 範囲 `[['00abec6c', '00abec73']]`
  - `CONDITIONAL_JUMP` [`00abec70`](#insn-00abec70) → [`00abec5c`](#insn-00abec5c)
  - `FALL_THROUGH` [`00abec70`](#insn-00abec70) → [`00abec74`](#insn-00abec74)
- ブロック [`00abec74`](#insn-00abec74) 範囲 `[['00abec74', '00abec77']]`
  - `UNCONDITIONAL_JUMP` [`00abec74`](#insn-00abec74) → [`00abf130`](#insn-00abf130)
- ブロック [`00abec78`](#insn-00abec78) 範囲 `[['00abec78', '00abec87']]`
  - `CONDITIONAL_JUMP` [`00abec84`](#insn-00abec84) → [`00abec98`](#insn-00abec98)
  - `FALL_THROUGH` [`00abec84`](#insn-00abec84) → [`00abec88`](#insn-00abec88)
- ブロック [`00abec88`](#insn-00abec88) 範囲 `[['00abec88', '00abec8b']]`
  - `UNCONDITIONAL_JUMP` [`00abec88`](#insn-00abec88) → [`00abecdc`](#insn-00abecdc)
- ブロック [`00abec8c`](#insn-00abec8c) 範囲 `[['00abec8c', '00abec8f']]`
  - `FALL_THROUGH` [`00abec8c`](#insn-00abec8c) → [`00abec90`](#insn-00abec90)
- ブロック [`00abec90`](#insn-00abec90) 範囲 `[['00abec90', '00abec97']]`
  - `CONDITIONAL_JUMP` [`00abec94`](#insn-00abec94) → [`00abeeb4`](#insn-00abeeb4)
  - `FALL_THROUGH` [`00abec94`](#insn-00abec94) → [`00abec98`](#insn-00abec98)
- ブロック [`00abec98`](#insn-00abec98) 範囲 `[['00abec98', '00abeca3']]`
  - `CONDITIONAL_JUMP` [`00abeca0`](#insn-00abeca0) → [`00abec90`](#insn-00abec90)
  - `FALL_THROUGH` [`00abeca0`](#insn-00abeca0) → [`00abeca4`](#insn-00abeca4)
- ブロック [`00abeca4`](#insn-00abeca4) 範囲 `[['00abeca4', '00abeca7']]`
  - `CONDITIONAL_JUMP` [`00abeca4`](#insn-00abeca4) → [`00abec8c`](#insn-00abec8c)
  - `FALL_THROUGH` [`00abeca4`](#insn-00abeca4) → [`00abeca8`](#insn-00abeca8)
- ブロック [`00abeca8`](#insn-00abeca8) 範囲 `[['00abeca8', '00abecaf']]`
  - `UNCONDITIONAL_JUMP` [`00abecac`](#insn-00abecac) → [`00abecb8`](#insn-00abecb8)
- ブロック [`00abecb0`](#insn-00abecb0) 範囲 `[['00abecb0', '00abecb7']]`
  - `CONDITIONAL_JUMP` [`00abecb4`](#insn-00abecb4) → [`00abf130`](#insn-00abf130)
  - `FALL_THROUGH` [`00abecb4`](#insn-00abecb4) → [`00abecb8`](#insn-00abecb8)
- ブロック [`00abecb8`](#insn-00abecb8) 範囲 `[['00abecb8', '00abecc3']]`
  - `CONDITIONAL_JUMP` [`00abecc0`](#insn-00abecc0) → [`00abecb0`](#insn-00abecb0)
  - `FALL_THROUGH` [`00abecc0`](#insn-00abecc0) → [`00abecc4`](#insn-00abecc4)
- ブロック [`00abecc4`](#insn-00abecc4) 範囲 `[['00abecc4', '00abecc7']]`
  - `CONDITIONAL_JUMP` [`00abecc4`](#insn-00abecc4) → [`00abed00`](#insn-00abed00)
  - `FALL_THROUGH` [`00abecc4`](#insn-00abecc4) → [`00abecc8`](#insn-00abecc8)
- ブロック [`00abecc8`](#insn-00abecc8) 範囲 `[['00abecc8', '00abeccf']]`
  - `CONDITIONAL_JUMP` [`00abeccc`](#insn-00abeccc) → [`00abecb8`](#insn-00abecb8)
  - `FALL_THROUGH` [`00abeccc`](#insn-00abeccc) → [`00abecd0`](#insn-00abecd0)
- ブロック [`00abecd0`](#insn-00abecd0) 範囲 `[['00abecd0', '00abecd3']]`
  - `UNCONDITIONAL_JUMP` [`00abecd0`](#insn-00abecd0) → [`00abf130`](#insn-00abf130)
- ブロック [`00abecd4`](#insn-00abecd4) 範囲 `[['00abecd4', '00abecdb']]`
  - `CONDITIONAL_JUMP` [`00abecd8`](#insn-00abecd8) → [`00abee54`](#insn-00abee54)
  - `FALL_THROUGH` [`00abecd8`](#insn-00abecd8) → [`00abecdc`](#insn-00abecdc)
- ブロック [`00abecdc`](#insn-00abecdc) 範囲 `[['00abecdc', '00abeceb']]`
  - `CONDITIONAL_JUMP` [`00abece8`](#insn-00abece8) → [`00abecd4`](#insn-00abecd4)
  - `FALL_THROUGH` [`00abece8`](#insn-00abece8) → [`00abecec`](#insn-00abecec)
- ブロック [`00abecec`](#insn-00abecec) 範囲 `[['00abecec', '00abecef']]`
  - `CONDITIONAL_JUMP` [`00abecec`](#insn-00abecec) → [`00abeea8`](#insn-00abeea8)
  - `FALL_THROUGH` [`00abecec`](#insn-00abecec) → [`00abecf0`](#insn-00abecf0)
- ブロック [`00abecf0`](#insn-00abecf0) 範囲 `[['00abecf0', '00abecf7']]`
  - `CONDITIONAL_JUMP` [`00abecf4`](#insn-00abecf4) → [`00abecdc`](#insn-00abecdc)
  - `FALL_THROUGH` [`00abecf4`](#insn-00abecf4) → [`00abecf8`](#insn-00abecf8)
- ブロック [`00abecf8`](#insn-00abecf8) 範囲 `[['00abecf8', '00abecff']]`
  - `UNCONDITIONAL_JUMP` [`00abecfc`](#insn-00abecfc) → [`00abee58`](#insn-00abee58)
- ブロック [`00abed00`](#insn-00abed00) 範囲 `[['00abed00', '00abed0b']]`
  - `CONDITIONAL_JUMP` [`00abed08`](#insn-00abed08) → [`00abeeb4`](#insn-00abeeb4)
  - `FALL_THROUGH` [`00abed08`](#insn-00abed08) → [`00abed0c`](#insn-00abed0c)
- ブロック [`00abed0c`](#insn-00abed0c) 範囲 `[['00abed0c', '00abed13']]`
  - `FALL_THROUGH` [`00abed10`](#insn-00abed10) → [`00abed14`](#insn-00abed14)
- ブロック [`00abed14`](#insn-00abed14) 範囲 `[['00abed14', '00abed2b']]`
  - `CONDITIONAL_JUMP` [`00abed28`](#insn-00abed28) → [`00abed14`](#insn-00abed14)
  - `FALL_THROUGH` [`00abed28`](#insn-00abed28) → [`00abed2c`](#insn-00abed2c)
- ブロック [`00abed2c`](#insn-00abed2c) 範囲 `[['00abed2c', '00abed37']]`
  - `CONDITIONAL_JUMP` [`00abed34`](#insn-00abed34) → [`00abeeb4`](#insn-00abeeb4)
  - `FALL_THROUGH` [`00abed34`](#insn-00abed34) → [`00abed38`](#insn-00abed38)
- ブロック [`00abed38`](#insn-00abed38) 範囲 `[['00abed38', '00abed4b']]`
  - `CONDITIONAL_JUMP` [`00abed48`](#insn-00abed48) → [`00abeeb4`](#insn-00abeeb4)
  - `FALL_THROUGH` [`00abed48`](#insn-00abed48) → [`00abed4c`](#insn-00abed4c)
- ブロック [`00abed4c`](#insn-00abed4c) 範囲 `[['00abed4c', '00abed53']]`
  - `CONDITIONAL_JUMP` [`00abed50`](#insn-00abed50) → [`00abed64`](#insn-00abed64)
  - `FALL_THROUGH` [`00abed50`](#insn-00abed50) → [`00abed54`](#insn-00abed54)
- ブロック [`00abed54`](#insn-00abed54) 範囲 `[['00abed54', '00abed5f']]`
  - `CONDITIONAL_JUMP` [`00abed5c`](#insn-00abed5c) → [`00abed54`](#insn-00abed54)
  - `FALL_THROUGH` [`00abed5c`](#insn-00abed5c) → [`00abed60`](#insn-00abed60)
- ブロック [`00abed60`](#insn-00abed60) 範囲 `[['00abed60', '00abed63']]`
  - `UNCONDITIONAL_JUMP` [`00abed60`](#insn-00abed60) → [`00abed78`](#insn-00abed78)
- ブロック [`00abed64`](#insn-00abed64) 範囲 `[['00abed64', '00abed77']]`
  - `CONDITIONAL_JUMP` [`00abed74`](#insn-00abed74) → [`00abed64`](#insn-00abed64)
  - `FALL_THROUGH` [`00abed74`](#insn-00abed74) → [`00abed78`](#insn-00abed78)
- ブロック [`00abed78`](#insn-00abed78) 範囲 `[['00abed78', '00abed83']]`
  - `CONDITIONAL_JUMP` [`00abed80`](#insn-00abed80) → [`00abed88`](#insn-00abed88)
  - `FALL_THROUGH` [`00abed80`](#insn-00abed80) → [`00abed84`](#insn-00abed84)
- ブロック [`00abed84`](#insn-00abed84) 範囲 `[['00abed84', '00abed87']]`
  - `FALL_THROUGH` [`00abed84`](#insn-00abed84) → [`00abed88`](#insn-00abed88)
- ブロック [`00abed88`](#insn-00abed88) 範囲 `[['00abed88', '00abeda7']]`
  - `UNCONDITIONAL_JUMP` [`00abeda4`](#insn-00abeda4) → [`00abeeb4`](#insn-00abeeb4)
- ブロック [`00abeda8`](#insn-00abeda8) 範囲 `[['00abeda8', '00abedc7']]`
  - `CONDITIONAL_JUMP` [`00abedc4`](#insn-00abedc4) → [`00abeb80`](#insn-00abeb80)
  - `FALL_THROUGH` [`00abedc4`](#insn-00abedc4) → [`00abedc8`](#insn-00abedc8)
- ブロック [`00abedc8`](#insn-00abedc8) 範囲 `[['00abedc8', '00abedcf']]`
  - `CONDITIONAL_JUMP` [`00abedcc`](#insn-00abedcc) → [`00abedd8`](#insn-00abedd8)
  - `FALL_THROUGH` [`00abedcc`](#insn-00abedcc) → [`00abedd0`](#insn-00abedd0)
- ブロック [`00abedd0`](#insn-00abedd0) 範囲 `[['00abedd0', '00abedd7']]`
  - `FALL_THROUGH` [`00abedd4`](#insn-00abedd4) → [`00abedd8`](#insn-00abedd8)
- ブロック [`00abedd8`](#insn-00abedd8) 範囲 `[['00abedd8', '00abeddf']]`
  - `CONDITIONAL_JUMP` [`00abeddc`](#insn-00abeddc) → [`00abeeb4`](#insn-00abeeb4)
  - `FALL_THROUGH` [`00abeddc`](#insn-00abeddc) → [`00abede0`](#insn-00abede0)
- ブロック [`00abede0`](#insn-00abede0) 範囲 `[['00abede0', '00abedeb']]`
  - `UNCONDITIONAL_JUMP` [`00abede8`](#insn-00abede8) → [`00abeeb4`](#insn-00abeeb4)
- ブロック [`00abedec`](#insn-00abedec) 範囲 `[['00abedec', '00abee0b']]`
  - `CONDITIONAL_JUMP` [`00abee08`](#insn-00abee08) → [`00abeab8`](#insn-00abeab8)
  - `FALL_THROUGH` [`00abee08`](#insn-00abee08) → [`00abee0c`](#insn-00abee0c)
- ブロック [`00abee0c`](#insn-00abee0c) 範囲 `[['00abee0c', '00abee13']]`
  - `CONDITIONAL_JUMP` [`00abee10`](#insn-00abee10) → [`00abee28`](#insn-00abee28)
  - `FALL_THROUGH` [`00abee10`](#insn-00abee10) → [`00abee14`](#insn-00abee14)
- ブロック [`00abee14`](#insn-00abee14) 範囲 `[['00abee14', '00abee1b']]`
  - `CONDITIONAL_JUMP` [`00abee18`](#insn-00abee18) → [`00abee38`](#insn-00abee38)
  - `FALL_THROUGH` [`00abee18`](#insn-00abee18) → [`00abee1c`](#insn-00abee1c)
- ブロック [`00abee1c`](#insn-00abee1c) 範囲 `[['00abee1c', '00abee23']]`
  - `CONDITIONAL_JUMP` [`00abee20`](#insn-00abee20) → [`00abee48`](#insn-00abee48)
  - `FALL_THROUGH` [`00abee20`](#insn-00abee20) → [`00abee24`](#insn-00abee24)
- ブロック [`00abee24`](#insn-00abee24) 範囲 `[['00abee24', '00abee27']]`
  - `UNCONDITIONAL_JUMP` [`00abee24`](#insn-00abee24) → [`00abeeb4`](#insn-00abeeb4)
- ブロック [`00abee28`](#insn-00abee28) 範囲 `[['00abee28', '00abee37']]`
  - `CONDITIONAL_JUMP` [`00abee34`](#insn-00abee34) → [`00abee1c`](#insn-00abee1c)
  - `FALL_THROUGH` [`00abee34`](#insn-00abee34) → [`00abee38`](#insn-00abee38)
- ブロック [`00abee38`](#insn-00abee38) 範囲 `[['00abee38', '00abee47']]`
  - `CONDITIONAL_JUMP` [`00abee44`](#insn-00abee44) → [`00abeeb4`](#insn-00abeeb4)
  - `FALL_THROUGH` [`00abee44`](#insn-00abee44) → [`00abee48`](#insn-00abee48)
- ブロック [`00abee48`](#insn-00abee48) 範囲 `[['00abee48', '00abee53']]`
  - `UNCONDITIONAL_JUMP` [`00abee50`](#insn-00abee50) → [`00abeeb4`](#insn-00abeeb4)
- ブロック [`00abee54`](#insn-00abee54) 範囲 `[['00abee54', '00abee57']]`
  - `FALL_THROUGH` [`00abee54`](#insn-00abee54) → [`00abee58`](#insn-00abee58)
- ブロック [`00abee58`](#insn-00abee58) 範囲 `[['00abee58', '00abee83']]`
  - `CONDITIONAL_JUMP` [`00abee80`](#insn-00abee80) → [`00abee8c`](#insn-00abee8c)
  - `FALL_THROUGH` [`00abee80`](#insn-00abee80) → [`00abee84`](#insn-00abee84)
- ブロック [`00abee84`](#insn-00abee84) 範囲 `[['00abee84', '00abee8b']]`
  - `FALL_THROUGH` [`00abee88`](#insn-00abee88) → [`00abee8c`](#insn-00abee8c)
- ブロック [`00abee8c`](#insn-00abee8c) 範囲 `[['00abee8c', '00abeea7']]`
  - `UNCONDITIONAL_JUMP` [`00abeea4`](#insn-00abeea4) → [`00abeeac`](#insn-00abeeac)
- ブロック [`00abeea8`](#insn-00abeea8) 範囲 `[['00abeea8', '00abeeab']]`
  - `FALL_THROUGH` [`00abeea8`](#insn-00abeea8) → [`00abeeac`](#insn-00abeeac)
- ブロック [`00abeeac`](#insn-00abeeac) 範囲 `[['00abeeac', '00abeeb3']]`
  - `FALL_THROUGH` [`00abeeb0`](#insn-00abeeb0) → [`00abeeb4`](#insn-00abeeb4)
- ブロック [`00abeeb4`](#insn-00abeeb4) 範囲 `[['00abeeb4', '00abef5f']]`
  - `CONDITIONAL_JUMP` [`00abef5c`](#insn-00abef5c) → [`00abef6c`](#insn-00abef6c)
  - `FALL_THROUGH` [`00abef5c`](#insn-00abef5c) → [`00abef60`](#insn-00abef60)
- ブロック [`00abef60`](#insn-00abef60) 範囲 `[['00abef60', '00abef63']]`
  - `CONDITIONAL_JUMP` [`00abef60`](#insn-00abef60) → [`00abef80`](#insn-00abef80)
  - `FALL_THROUGH` [`00abef60`](#insn-00abef60) → [`00abef64`](#insn-00abef64)
- ブロック [`00abef64`](#insn-00abef64) 範囲 `[['00abef64', '00abef6b']]`
  - `UNCONDITIONAL_JUMP` [`00abef68`](#insn-00abef68) → [`00abef74`](#insn-00abef74)
- ブロック [`00abef6c`](#insn-00abef6c) 範囲 `[['00abef6c', '00abef73']]`
  - `FALL_THROUGH` [`00abef70`](#insn-00abef70) → [`00abef74`](#insn-00abef74)
- ブロック [`00abef74`](#insn-00abef74) 範囲 `[['00abef74', '00abef7f']]`
  - `FALL_THROUGH` [`00abef7c`](#insn-00abef7c) → [`00abef80`](#insn-00abef80)
- ブロック [`00abef80`](#insn-00abef80) 範囲 `[['00abef80', '00abef8b']]`
  - `CONDITIONAL_JUMP` [`00abef88`](#insn-00abef88) → [`00abefac`](#insn-00abefac)
  - `FALL_THROUGH` [`00abef88`](#insn-00abef88) → [`00abef8c`](#insn-00abef8c)
- ブロック [`00abef8c`](#insn-00abef8c) 範囲 `[['00abef8c', '00abefab']]`
  - `FALL_THROUGH` [`00abefa8`](#insn-00abefa8) → [`00abefac`](#insn-00abefac)
- ブロック [`00abefac`](#insn-00abefac) 範囲 `[['00abefac', '00abefb7']]`
  - `CONDITIONAL_JUMP` [`00abefb4`](#insn-00abefb4) → [`00abe874`](#insn-00abe874)
  - `FALL_THROUGH` [`00abefb4`](#insn-00abefb4) → [`00abefb8`](#insn-00abefb8)
- ブロック [`00abefb8`](#insn-00abefb8) 範囲 `[['00abefb8', '00abefc7']]`
  - `CONDITIONAL_JUMP` [`00abefc4`](#insn-00abefc4) → [`00abe85c`](#insn-00abe85c)
  - `FALL_THROUGH` [`00abefc4`](#insn-00abefc4) → [`00abefc8`](#insn-00abefc8)
- ブロック [`00abefc8`](#insn-00abefc8) 範囲 `[['00abefc8', '00abefd7']]`
  - `CONDITIONAL_JUMP` [`00abefd4`](#insn-00abefd4) → [`00abe85c`](#insn-00abe85c)
  - `FALL_THROUGH` [`00abefd4`](#insn-00abefd4) → [`00abefd8`](#insn-00abefd8)
- ブロック [`00abefd8`](#insn-00abefd8) 範囲 `[['00abefd8', '00abeff3']]`
  - `UNCONDITIONAL_JUMP` [`00abeff0`](#insn-00abeff0) → [`00abe85c`](#insn-00abe85c)
- ブロック [`00abeff4`](#insn-00abeff4) 範囲 `[['00abeff4', '00abf003']]`
  - `CONDITIONAL_JUMP` [`00abf000`](#insn-00abf000) → [`00abe8f8`](#insn-00abe8f8)
  - `FALL_THROUGH` [`00abf000`](#insn-00abf000) → [`00abf004`](#insn-00abf004)
- ブロック [`00abf004`](#insn-00abf004) 範囲 `[['00abf004', '00abf04b']]`
  - `UNCONDITIONAL_JUMP` [`00abf048`](#insn-00abf048) → [`00abe8f8`](#insn-00abe8f8)
- ブロック [`00abf04c`](#insn-00abf04c) 範囲 `[['00abf04c', '00abf05b']]`
  - `CONDITIONAL_JUMP` [`00abf058`](#insn-00abf058) → [`00abe9f4`](#insn-00abe9f4)
  - `FALL_THROUGH` [`00abf058`](#insn-00abf058) → [`00abf05c`](#insn-00abf05c)
- ブロック [`00abf05c`](#insn-00abf05c) 範囲 `[['00abf05c', '00abf077']]`
  - `FALL_THROUGH` [`00abf074`](#insn-00abf074) → [`00abf078`](#insn-00abf078)
- ブロック [`00abf078`](#insn-00abf078) 範囲 `[['00abf078', '00abf0a3']]`
  - `UNCONDITIONAL_JUMP` [`00abf0a0`](#insn-00abf0a0) → [`00abe9f4`](#insn-00abe9f4)
- ブロック [`00abf0a4`](#insn-00abf0a4) 範囲 `[['00abf0a4', '00abf0b3']]`
  - `CONDITIONAL_JUMP` [`00abf0b0`](#insn-00abf0b0) → [`00abeaec`](#insn-00abeaec)
  - `FALL_THROUGH` [`00abf0b0`](#insn-00abf0b0) → [`00abf0b4`](#insn-00abf0b4)
- ブロック [`00abf0b4`](#insn-00abf0b4) 範囲 `[['00abf0b4', '00abf0fb']]`
  - `UNCONDITIONAL_JUMP` [`00abf0f8`](#insn-00abf0f8) → [`00abeaec`](#insn-00abeaec)
- ブロック [`00abf0fc`](#insn-00abf0fc) 範囲 `[['00abf0fc', '00abf10f']]`
  - `CONDITIONAL_JUMP` [`00abf10c`](#insn-00abf10c) → [`00abf2b0`](#insn-00abf2b0)
  - `FALL_THROUGH` [`00abf10c`](#insn-00abf10c) → [`00abf110`](#insn-00abf110)
- ブロック [`00abf110`](#insn-00abf110) 範囲 `[['00abf110', '00abf12f']]`
- ブロック [`00abf130`](#insn-00abf130) 範囲 `[['00abf130', '00abf143']]`
  - `CONDITIONAL_JUMP` [`00abf140`](#insn-00abf140) → [`00abf2b0`](#insn-00abf2b0)
  - `FALL_THROUGH` [`00abf140`](#insn-00abf140) → [`00abf144`](#insn-00abf144)
- ブロック [`00abf144`](#insn-00abf144) 範囲 `[['00abf144', '00abf14f']]`
- ブロック [`00abf150`](#insn-00abf150) 範囲 `[['00abf150', '00abf163']]`
  - `CONDITIONAL_JUMP` [`00abf160`](#insn-00abf160) → [`00abf2b0`](#insn-00abf2b0)
  - `FALL_THROUGH` [`00abf160`](#insn-00abf160) → [`00abf164`](#insn-00abf164)
- ブロック [`00abf164`](#insn-00abf164) 範囲 `[['00abf164', '00abf16b']]`
  - `FALL_THROUGH` [`00abf168`](#insn-00abf168) → [`00abf16c`](#insn-00abf16c)
- ブロック [`00abf16c`](#insn-00abf16c) 範囲 `[['00abf16c', '00abf17f']]`
  - `CONDITIONAL_JUMP` [`00abf17c`](#insn-00abf17c) → [`00abf2b0`](#insn-00abf2b0)
  - `FALL_THROUGH` [`00abf17c`](#insn-00abf17c) → [`00abf180`](#insn-00abf180)
- ブロック [`00abf180`](#insn-00abf180) 範囲 `[['00abf180', '00abf187']]`
  - `FALL_THROUGH` [`00abf184`](#insn-00abf184) → [`00abf188`](#insn-00abf188)
- ブロック [`00abf188`](#insn-00abf188) 範囲 `[['00abf188', '00abf19b']]`
  - `CONDITIONAL_JUMP` [`00abf198`](#insn-00abf198) → [`00abf2b0`](#insn-00abf2b0)
  - `FALL_THROUGH` [`00abf198`](#insn-00abf198) → [`00abf19c`](#insn-00abf19c)
- ブロック [`00abf19c`](#insn-00abf19c) 範囲 `[['00abf19c', '00abf1af']]`
  - `CONDITIONAL_JUMP` [`00abf1ac`](#insn-00abf1ac) → [`00abf1fc`](#insn-00abf1fc)
  - `FALL_THROUGH` [`00abf1ac`](#insn-00abf1ac) → [`00abf1b0`](#insn-00abf1b0)
- ブロック [`00abf1b0`](#insn-00abf1b0) 範囲 `[['00abf1b0', '00abf1b3']]`
  - `UNCONDITIONAL_JUMP` [`00abf1b0`](#insn-00abf1b0) → [`00abf218`](#insn-00abf218)
- ブロック [`00abf1fc`](#insn-00abf1fc) 範囲 `[['00abf1fc', '00abf203']]`
  - `CONDITIONAL_JUMP` [`00abf200`](#insn-00abf200) → [`00abf238`](#insn-00abf238)
  - `FALL_THROUGH` [`00abf200`](#insn-00abf200) → [`00abf204`](#insn-00abf204)
- ブロック [`00abf204`](#insn-00abf204) 範囲 `[['00abf204', '00abf207']]`
  - `UNCONDITIONAL_JUMP` [`00abf204`](#insn-00abf204) → [`00abf294`](#insn-00abf294)
- ブロック [`00abf218`](#insn-00abf218) 範囲 `[['00abf218', '00abf227']]`
  - `CONDITIONAL_JUMP` [`00abf224`](#insn-00abf224) → [`00abf238`](#insn-00abf238)
  - `FALL_THROUGH` [`00abf224`](#insn-00abf224) → [`00abf228`](#insn-00abf228)
- ブロック [`00abf228`](#insn-00abf228) 範囲 `[['00abf228', '00abf22b']]`
  - `UNCONDITIONAL_JUMP` [`00abf228`](#insn-00abf228) → [`00abf294`](#insn-00abf294)
- ブロック [`00abf238`](#insn-00abf238) 範囲 `[['00abf238', '00abf243']]`
  - `UNCONDITIONAL_JUMP` [`00abf240`](#insn-00abf240) → [`00abf294`](#insn-00abf294)
- ブロック [`00abf294`](#insn-00abf294) 範囲 `[['00abf294', '00abf2a7']]`
  - `CONDITIONAL_JUMP` [`00abf2a4`](#insn-00abf2a4) → [`00abf2b0`](#insn-00abf2b0)
  - `FALL_THROUGH` [`00abf2a4`](#insn-00abf2a4) → [`00abf2a8`](#insn-00abf2a8)
- ブロック [`00abf2a8`](#insn-00abf2a8) 範囲 `[['00abf2a8', '00abf2af']]`
- ブロック [`00abf2b0`](#insn-00abf2b0) 範囲 `[['00abf2b0', '00abf2b3']]`

## 命令位置別の参照

- [`00abe600`](#insn-00abe600) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe604`](#insn-00abe604) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe608`](#insn-00abe608) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe60c`](#insn-00abe60c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe610`](#insn-00abe610) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe614`](#insn-00abe614) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe628`](#insn-00abe628) → `Stack[-0x168]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe630`](#insn-00abe630) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe638`](#insn-00abe638) → `00ca4578`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abe63c`](#insn-00abe63c) → [`00abe664`](#insn-00abe664) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe644`](#insn-00abe644) → `00c65a58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00abe64c`](#insn-00abe64c) → `00c8cef8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00abe658`](#insn-00abe658) → [`00c58210`](../00c58/00c58210.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58210` · 推定シンボル `None` · 推定型 `None`
- [`00abe660`](#insn-00abe660) → [`00abe668`](#insn-00abe668) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe668`](#insn-00abe668) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abe678`](#insn-00abe678) → [`008b7904`](../008b7/008b7904.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7904` · 推定シンボル `None` · 推定型 `None`
- [`00abe67c`](#insn-00abe67c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abe688`](#insn-00abe688) → [`008b7904`](../008b7/008b7904.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7904` · 推定シンボル `None` · 推定型 `None`
- [`00abe68c`](#insn-00abe68c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abe698`](#insn-00abe698) → [`008b7904`](../008b7/008b7904.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7904` · 推定シンボル `None` · 推定型 `None`
- [`00abe69c`](#insn-00abe69c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abe6a8`](#insn-00abe6a8) → [`008b7904`](../008b7/008b7904.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7904` · 推定シンボル `None` · 推定型 `None`
- [`00abe6ac`](#insn-00abe6ac) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abe6b8`](#insn-00abe6b8) → [`008b7904`](../008b7/008b7904.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7904` · 推定シンボル `None` · 推定型 `None`
- [`00abe6bc`](#insn-00abe6bc) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abe6c8`](#insn-00abe6c8) → [`008b7904`](../008b7/008b7904.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7904` · 推定シンボル `None` · 推定型 `None`
- [`00abe6cc`](#insn-00abe6cc) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abe6d8`](#insn-00abe6d8) → [`008b7904`](../008b7/008b7904.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7904` · 推定シンボル `None` · 推定型 `None`
- [`00abe6dc`](#insn-00abe6dc) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abe6e8`](#insn-00abe6e8) → [`008b7904`](../008b7/008b7904.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7904` · 推定シンボル `None` · 推定型 `None`
- [`00abe6ec`](#insn-00abe6ec) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abe6f8`](#insn-00abe6f8) → [`008b7904`](../008b7/008b7904.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7904` · 推定シンボル `None` · 推定型 `None`
- [`00abe6fc`](#insn-00abe6fc) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abe708`](#insn-00abe708) → [`008b7904`](../008b7/008b7904.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7904` · 推定シンボル `None` · 推定型 `None`
- [`00abe70c`](#insn-00abe70c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abe718`](#insn-00abe718) → [`008b7904`](../008b7/008b7904.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7904` · 推定シンボル `None` · 推定型 `None`
- [`00abe71c`](#insn-00abe71c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abe728`](#insn-00abe728) → [`008b7904`](../008b7/008b7904.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7904` · 推定シンボル `None` · 推定型 `None`
- [`00abe72c`](#insn-00abe72c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abe738`](#insn-00abe738) → [`008b7904`](../008b7/008b7904.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7904` · 推定シンボル `None` · 推定型 `None`
- [`00abe73c`](#insn-00abe73c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abe748`](#insn-00abe748) → [`008b7904`](../008b7/008b7904.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7904` · 推定シンボル `None` · 推定型 `None`
- [`00abe74c`](#insn-00abe74c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abe758`](#insn-00abe758) → [`008b7904`](../008b7/008b7904.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7904` · 推定シンボル `None` · 推定型 `None`
- [`00abe75c`](#insn-00abe75c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abe768`](#insn-00abe768) → [`008b7904`](../008b7/008b7904.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7904` · 推定シンボル `None` · 推定型 `None`
- [`00abe76c`](#insn-00abe76c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abe778`](#insn-00abe778) → [`008b7904`](../008b7/008b7904.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7904` · 推定シンボル `None` · 推定型 `None`
- [`00abe77c`](#insn-00abe77c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abe788`](#insn-00abe788) → [`008b7904`](../008b7/008b7904.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7904` · 推定シンボル `None` · 推定型 `None`
- [`00abe78c`](#insn-00abe78c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abe798`](#insn-00abe798) → [`008b7904`](../008b7/008b7904.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7904` · 推定シンボル `None` · 推定型 `None`
- [`00abe79c`](#insn-00abe79c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abe7a8`](#insn-00abe7a8) → [`008b7904`](../008b7/008b7904.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7904` · 推定シンボル `None` · 推定型 `None`
- [`00abe7c8`](#insn-00abe7c8) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe7d0`](#insn-00abe7d0) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe7d8`](#insn-00abe7d8) → `Stack[-0x15c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe7e4`](#insn-00abe7e4) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe7ec`](#insn-00abe7ec) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe7f4`](#insn-00abe7f4) → `002c2260`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe7fc`](#insn-00abe7fc) → `Stack[-0x150]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe800`](#insn-00abe800) → `00c9af70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abe804`](#insn-00abe804) → `00c9af68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abe810`](#insn-00abe810) → `00c8b358`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00abe810`](#insn-00abe810) → `00c8b3b0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00abe810`](#insn-00abe810) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe814`](#insn-00abe814) → [`00abe828`](#insn-00abe828) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe818`](#insn-00abe818) → `Stack[-0x138]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe824`](#insn-00abe824) → [`00abf0fc`](#insn-00abf0fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe82c`](#insn-00abe82c) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe840`](#insn-00abe840) → `Stack[-0x138]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe848`](#insn-00abe848) → `Stack[-0x15c]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe854`](#insn-00abe854) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe858`](#insn-00abe858) → [`00abe880`](#insn-00abe880) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe85c`](#insn-00abe85c) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe864`](#insn-00abe864) → `00c8b358`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00abe868`](#insn-00abe868) → [`005d8b88`](../005d8/005d8b88.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d8b88` · 推定シンボル `None` · 推定型 `None`
- [`00abe870`](#insn-00abe870) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abe87c`](#insn-00abe87c) → [`00abe818`](#insn-00abe818) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe894`](#insn-00abe894) → [`00abe818`](#insn-00abe818) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe8a4`](#insn-00abe8a4) → [`00abf150`](#insn-00abf150) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe8b4`](#insn-00abe8b4) → [`00abe818`](#insn-00abe818) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe8c8`](#insn-00abe8c8) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00abe8dc`](#insn-00abe8dc) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe8e4`](#insn-00abe8e4) → [`00abe9c4`](#insn-00abe9c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe8f0`](#insn-00abe8f0) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abe8f4`](#insn-00abe8f4) → [`00abeff4`](#insn-00abeff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe904`](#insn-00abe904) → `002bb807`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abe908`](#insn-00abe908) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe90c`](#insn-00abe90c) → `002bb80d`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abe910`](#insn-00abe910) → `Stack[-0xd1]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe92c`](#insn-00abe92c) → [`00447eb4`](../00447/00447eb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00447eb4` · 推定シンボル `None` · 推定型 `None`
- [`00abe938`](#insn-00abe938) → `Stack[-0xef]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe93c`](#insn-00abe93c) → `002bcaae`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abe944`](#insn-00abe944) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe948`](#insn-00abe948) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe960`](#insn-00abe960) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abe968`](#insn-00abe968) → [`0047e5cc`](../0047e/0047e5cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047e5cc` · 推定シンボル `None` · 推定型 `None`
- [`00abe96c`](#insn-00abe96c) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe970`](#insn-00abe970) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe97c`](#insn-00abe97c) → [`00abe990`](#insn-00abe990) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe988`](#insn-00abe988) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00abe98c`](#insn-00abe98c) → [`00abebac`](#insn-00abebac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe990`](#insn-00abe990) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe994`](#insn-00abe994) → [`00abebcc`](#insn-00abebcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe9a0`](#insn-00abe9a0) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00abe9a4`](#insn-00abe9a4) → [`00abebcc`](#insn-00abebcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe9bc`](#insn-00abe9bc) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00abe9c0`](#insn-00abe9c0) → [`00abebcc`](#insn-00abebcc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe9d4`](#insn-00abe9d4) → [`00abf16c`](#insn-00abf16c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe9dc`](#insn-00abe9dc) → [`00abd0e0`](../00abd/00abd0e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00abd0e0` · 推定シンボル `None` · 推定型 `None`
- [`00abe9e8`](#insn-00abe9e8) → [`00abeae4`](#insn-00abeae4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abe9ec`](#insn-00abe9ec) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abe9f0`](#insn-00abe9f0) → [`00abf04c`](#insn-00abf04c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abea04`](#insn-00abea04) → `Stack[-0xc9]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abea08`](#insn-00abea08) → `002b0366`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abea0c`](#insn-00abea0c) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abea10`](#insn-00abea10) → `002b0374`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abea24`](#insn-00abea24) → [`00abf188`](#insn-00abf188) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abea3c`](#insn-00abea3c) → [`00447eb4`](../00447/00447eb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00447eb4` · 推定シンボル `None` · 推定型 `None`
- [`00abea44`](#insn-00abea44) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00abea50`](#insn-00abea50) → `Stack[-0x150]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abea54`](#insn-00abea54) → `002adfb5`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abea58`](#insn-00abea58) → `002adfc5`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abea5c`](#insn-00abea5c) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abea60`](#insn-00abea60) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abea80`](#insn-00abea80) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abea88`](#insn-00abea88) → [`0047e5cc`](../0047e/0047e5cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047e5cc` · 推定シンボル `None` · 推定型 `None`
- [`00abea8c`](#insn-00abea8c) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abea90`](#insn-00abea90) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abea9c`](#insn-00abea9c) → [`00abeab0`](#insn-00abeab0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeaa8`](#insn-00abeaa8) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00abeaac`](#insn-00abeaac) → [`00abedec`](#insn-00abedec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeab0`](#insn-00abeab0) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeab4`](#insn-00abeab4) → [`00abee0c`](#insn-00abee0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeac0`](#insn-00abeac0) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00abeac4`](#insn-00abeac4) → [`00abee0c`](#insn-00abee0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeadc`](#insn-00abeadc) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00abeae0`](#insn-00abeae0) → [`00abee0c`](#insn-00abee0c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeae4`](#insn-00abeae4) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abeae8`](#insn-00abeae8) → [`00abf0a4`](#insn-00abf0a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeaf4`](#insn-00abeaf4) → `Stack[-0xb5]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeaf8`](#insn-00abeaf8) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeb04`](#insn-00abeb04) → `002af1d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abeb08`](#insn-00abeb08) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeb0c`](#insn-00abeb0c) → `Stack[-0xca]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeb24`](#insn-00abeb24) → `002bf6af`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abeb28`](#insn-00abeb28) → `002bf6bc`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abeb2c`](#insn-00abeb2c) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeb48`](#insn-00abeb48) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abeb50`](#insn-00abeb50) → [`0047e5cc`](../0047e/0047e5cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047e5cc` · 推定シンボル `None` · 推定型 `None`
- [`00abeb54`](#insn-00abeb54) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeb58`](#insn-00abeb58) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeb64`](#insn-00abeb64) → [`00abeb78`](#insn-00abeb78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeb70`](#insn-00abeb70) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00abeb74`](#insn-00abeb74) → [`00abeda8`](#insn-00abeda8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeb78`](#insn-00abeb78) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeb7c`](#insn-00abeb7c) → [`00abedc8`](#insn-00abedc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeb88`](#insn-00abeb88) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00abeb8c`](#insn-00abeb8c) → [`00abedc8`](#insn-00abedc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeba4`](#insn-00abeba4) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00abeba8`](#insn-00abeba8) → [`00abedc8`](#insn-00abedc8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abebc0`](#insn-00abebc0) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00abebc4`](#insn-00abebc4) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abebc8`](#insn-00abebc8) → [`00abe998`](#insn-00abe998) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abebcc`](#insn-00abebcc) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abebd0`](#insn-00abebd0) → [`00abec20`](#insn-00abec20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abebd4`](#insn-00abebd4) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abebd8`](#insn-00abebd8) → [`00abec30`](#insn-00abec30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abebdc`](#insn-00abebdc) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abebe0`](#insn-00abebe0) → [`00abebec`](#insn-00abebec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abebe4`](#insn-00abebe4) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abebe8`](#insn-00abebe8) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abebec`](#insn-00abebec) → `Stack[-0x118]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abebf4`](#insn-00abebf4) → [`00abeeb4`](#insn-00abeeb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abebfc`](#insn-00abebfc) → [`00abec08`](#insn-00abec08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abec04`](#insn-00abec04) → [`00abec44`](#insn-00abec44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abec10`](#insn-00abec10) → [`00abec00`](#insn-00abec00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abec14`](#insn-00abec14) → [`00abec4c`](#insn-00abec4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abec1c`](#insn-00abec1c) → [`00abec00`](#insn-00abec00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abec20`](#insn-00abec20) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abec24`](#insn-00abec24) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abec28`](#insn-00abec28) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abec2c`](#insn-00abec2c) → [`00abebdc`](#insn-00abebdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abec30`](#insn-00abec30) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abec34`](#insn-00abec34) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abec38`](#insn-00abec38) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abec3c`](#insn-00abec3c) → [`00abebe4`](#insn-00abebe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abec40`](#insn-00abec40) → [`00abebec`](#insn-00abebec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abec48`](#insn-00abec48) → [`00abec98`](#insn-00abec98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abec50`](#insn-00abec50) → [`00abec5c`](#insn-00abec5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abec58`](#insn-00abec58) → [`00abf130`](#insn-00abf130) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abec64`](#insn-00abec64) → [`00abec54`](#insn-00abec54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abec68`](#insn-00abec68) → [`00abec78`](#insn-00abec78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abec70`](#insn-00abec70) → [`00abec5c`](#insn-00abec5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abec74`](#insn-00abec74) → [`00abf130`](#insn-00abf130) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abec84`](#insn-00abec84) → [`00abec98`](#insn-00abec98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abec88`](#insn-00abec88) → [`00abecdc`](#insn-00abecdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abec94`](#insn-00abec94) → [`00abeeb4`](#insn-00abeeb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeca0`](#insn-00abeca0) → [`00abec90`](#insn-00abec90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeca4`](#insn-00abeca4) → [`00abec8c`](#insn-00abec8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abecac`](#insn-00abecac) → [`00abecb8`](#insn-00abecb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abecb4`](#insn-00abecb4) → [`00abf130`](#insn-00abf130) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abecc0`](#insn-00abecc0) → [`00abecb0`](#insn-00abecb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abecc4`](#insn-00abecc4) → [`00abed00`](#insn-00abed00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeccc`](#insn-00abeccc) → [`00abecb8`](#insn-00abecb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abecd0`](#insn-00abecd0) → [`00abf130`](#insn-00abf130) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abecd8`](#insn-00abecd8) → [`00abee54`](#insn-00abee54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abece8`](#insn-00abece8) → [`00abecd4`](#insn-00abecd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abecec`](#insn-00abecec) → [`00abeea8`](#insn-00abeea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abecf4`](#insn-00abecf4) → [`00abecdc`](#insn-00abecdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abecfc`](#insn-00abecfc) → [`00abee58`](#insn-00abee58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abed08`](#insn-00abed08) → [`00abeeb4`](#insn-00abeeb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abed0c`](#insn-00abed0c) → `Stack[-0x118]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abed28`](#insn-00abed28) → [`00abed14`](#insn-00abed14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abed2c`](#insn-00abed2c) → `Stack[-0x118]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abed34`](#insn-00abed34) → [`00abeeb4`](#insn-00abeeb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abed40`](#insn-00abed40) → `Stack[-0x118]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abed48`](#insn-00abed48) → [`00abeeb4`](#insn-00abeeb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abed50`](#insn-00abed50) → [`00abed64`](#insn-00abed64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abed5c`](#insn-00abed5c) → [`00abed54`](#insn-00abed54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abed60`](#insn-00abed60) → [`00abed78`](#insn-00abed78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abed74`](#insn-00abed74) → [`00abed64`](#insn-00abed64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abed80`](#insn-00abed80) → [`00abed88`](#insn-00abed88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abed98`](#insn-00abed98) → [`004945d0`](../00494/004945d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004945d0` · 推定シンボル `None` · 推定型 `None`
- [`00abeda0`](#insn-00abeda0) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abeda4`](#insn-00abeda4) → [`00abeeb4`](#insn-00abeeb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abedbc`](#insn-00abedbc) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00abedc0`](#insn-00abedc0) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abedc4`](#insn-00abedc4) → [`00abeb80`](#insn-00abeb80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abedc8`](#insn-00abedc8) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abedcc`](#insn-00abedcc) → [`00abedd8`](#insn-00abedd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abedd0`](#insn-00abedd0) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abedd4`](#insn-00abedd4) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abedd8`](#insn-00abedd8) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeddc`](#insn-00abeddc) → [`00abeeb4`](#insn-00abeeb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abede0`](#insn-00abede0) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abede4`](#insn-00abede4) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abede8`](#insn-00abede8) → [`00abeeb4`](#insn-00abeeb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abee00`](#insn-00abee00) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00abee04`](#insn-00abee04) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abee08`](#insn-00abee08) → [`00abeab8`](#insn-00abeab8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abee0c`](#insn-00abee0c) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abee10`](#insn-00abee10) → [`00abee28`](#insn-00abee28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abee14`](#insn-00abee14) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abee18`](#insn-00abee18) → [`00abee38`](#insn-00abee38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abee1c`](#insn-00abee1c) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abee20`](#insn-00abee20) → [`00abee48`](#insn-00abee48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abee24`](#insn-00abee24) → [`00abeeb4`](#insn-00abeeb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abee28`](#insn-00abee28) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abee2c`](#insn-00abee2c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abee30`](#insn-00abee30) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abee34`](#insn-00abee34) → [`00abee1c`](#insn-00abee1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abee38`](#insn-00abee38) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abee3c`](#insn-00abee3c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abee40`](#insn-00abee40) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abee44`](#insn-00abee44) → [`00abeeb4`](#insn-00abeeb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abee48`](#insn-00abee48) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abee4c`](#insn-00abee4c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abee50`](#insn-00abee50) → [`00abeeb4`](#insn-00abeeb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abee5c`](#insn-00abee5c) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00abee80`](#insn-00abee80) → [`00abee8c`](#insn-00abee8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abee90`](#insn-00abee90) → [`0043bb64`](../0043b/0043bb64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb64` · 推定シンボル `None` · 推定型 `None`
- [`00abeea4`](#insn-00abeea4) → [`00abeeac`](#insn-00abeeac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeeb4`](#insn-00abeeb4) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abeeb8`](#insn-00abeeb8) → [`0046c984`](../0046c/0046c984.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c984` · 推定シンボル `None` · 推定型 `None`
- [`00abeee8`](#insn-00abeee8) → [`00a46704`](../00a46/00a46704.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a46704` · 推定シンボル `None` · 推定型 `None`
- [`00abeeec`](#insn-00abeeec) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abef00`](#insn-00abef00) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abef04`](#insn-00abef04) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abef08`](#insn-00abef08) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abef0c`](#insn-00abef0c) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abef10`](#insn-00abef10) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abef1c`](#insn-00abef1c) → `00c8cf20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00abef1c`](#insn-00abef1c) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abef24`](#insn-00abef24) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abef28`](#insn-00abef28) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abef4c`](#insn-00abef4c) → [`008b6fa8`](../008b6/008b6fa8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6fa8` · 推定シンボル `None` · 推定型 `None`
- [`00abef50`](#insn-00abef50) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abef5c`](#insn-00abef5c) → [`00abef6c`](#insn-00abef6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abef60`](#insn-00abef60) → [`00abef80`](#insn-00abef80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abef68`](#insn-00abef68) → [`00abef74`](#insn-00abef74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abef74`](#insn-00abef74) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abef78`](#insn-00abef78) → `00c8cf40`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abef78`](#insn-00abef78) → `00c8cf48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00abef7c`](#insn-00abef7c) → [`00ac1b3c`](../00ac1/00ac1b3c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00ac1b3c` · 推定シンボル `None` · 推定型 `None`
- [`00abef7c`](#insn-00abef7c) → [`00ac1b40`](../00ac1/00ac1b40.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00ac1b40` · 推定シンボル `None` · 推定型 `None`
- [`00abef80`](#insn-00abef80) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abef84`](#insn-00abef84) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abef88`](#insn-00abef88) → [`00abefac`](#insn-00abefac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abef94`](#insn-00abef94) → `00c9af68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abef9c`](#insn-00abef9c) → `00c8b358`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00abefa0`](#insn-00abefa0) → [`005d8b88`](../005d8/005d8b88.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d8b88` · 推定シンボル `None` · 推定型 `None`
- [`00abefa8`](#insn-00abefa8) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abefac`](#insn-00abefac) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abefb0`](#insn-00abefb0) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abefb4`](#insn-00abefb4) → [`00abe874`](#insn-00abe874) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abefbc`](#insn-00abefbc) → `Stack[-0x128]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abefc0`](#insn-00abefc0) → `00c8b3b0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00abefc4`](#insn-00abefc4) → [`00abe85c`](#insn-00abe85c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abefd0`](#insn-00abefd0) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00abefd4`](#insn-00abefd4) → [`00abe85c`](#insn-00abe85c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abefec`](#insn-00abefec) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00abeff0`](#insn-00abeff0) → [`00abe85c`](#insn-00abe85c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeff8`](#insn-00abeff8) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abeffc`](#insn-00abeffc) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`00abf000`](#insn-00abf000) → [`00abe8f8`](#insn-00abe8f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf008`](#insn-00abf008) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf010`](#insn-00abf010) → [`0047ed74`](../0047e/0047ed74.md) · `PARAM` · `ANALYSIS` · 関数 `0047ed74` · 推定シンボル `None` · 推定型 `None`
- [`00abf01c`](#insn-00abf01c) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abf020`](#insn-00abf020) → `00ca4b08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf024`](#insn-00abf024) → `00ca4b00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf024`](#insn-00abf024) → `00ca4b08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf02c`](#insn-00abf02c) → `00ca4b28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf02c`](#insn-00abf02c) → `00ca4b30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf030`](#insn-00abf030) → `00ca4b20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf034`](#insn-00abf034) → `00ca4b10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf034`](#insn-00abf034) → `00ca4b18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf034`](#insn-00abf034) → `00ca4b20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf038`](#insn-00abf038) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`00abf040`](#insn-00abf040) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abf044`](#insn-00abf044) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`00abf048`](#insn-00abf048) → [`00abe8f8`](#insn-00abe8f8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf050`](#insn-00abf050) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abf054`](#insn-00abf054) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`00abf058`](#insn-00abf058) → [`00abe9f4`](#insn-00abe9f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf060`](#insn-00abf060) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf068`](#insn-00abf068) → [`0047ed74`](../0047e/0047ed74.md) · `PARAM` · `ANALYSIS` · 関数 `0047ed74` · 推定シンボル `None` · 推定型 `None`
- [`00abf074`](#insn-00abf074) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abf078`](#insn-00abf078) → `00ca4b08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf07c`](#insn-00abf07c) → `00ca4b00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf07c`](#insn-00abf07c) → `00ca4b08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf084`](#insn-00abf084) → `00ca4b28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf084`](#insn-00abf084) → `00ca4b30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf088`](#insn-00abf088) → `00ca4b20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf08c`](#insn-00abf08c) → `00ca4b10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf08c`](#insn-00abf08c) → `00ca4b18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf08c`](#insn-00abf08c) → `00ca4b20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf090`](#insn-00abf090) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`00abf098`](#insn-00abf098) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abf09c`](#insn-00abf09c) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`00abf0a0`](#insn-00abf0a0) → [`00abe9f4`](#insn-00abe9f4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0a8`](#insn-00abf0a8) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abf0ac`](#insn-00abf0ac) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`00abf0b0`](#insn-00abf0b0) → [`00abeaec`](#insn-00abeaec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0b8`](#insn-00abf0b8) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf0c0`](#insn-00abf0c0) → [`0047ed74`](../0047e/0047ed74.md) · `PARAM` · `ANALYSIS` · 関数 `0047ed74` · 推定シンボル `None` · 推定型 `None`
- [`00abf0cc`](#insn-00abf0cc) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abf0d0`](#insn-00abf0d0) → `00ca4b08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf0d4`](#insn-00abf0d4) → `00ca4b00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf0d4`](#insn-00abf0d4) → `00ca4b08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf0dc`](#insn-00abf0dc) → `00ca4b28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf0dc`](#insn-00abf0dc) → `00ca4b30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf0e0`](#insn-00abf0e0) → `00ca4b20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf0e4`](#insn-00abf0e4) → `00ca4b10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf0e4`](#insn-00abf0e4) → `00ca4b18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf0e4`](#insn-00abf0e4) → `00ca4b20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf0e8`](#insn-00abf0e8) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`00abf0f0`](#insn-00abf0f0) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abf0f4`](#insn-00abf0f4) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`00abf0f8`](#insn-00abf0f8) → [`00abeaec`](#insn-00abeaec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0fc`](#insn-00abf0fc) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf104`](#insn-00abf104) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf10c`](#insn-00abf10c) → [`00abf2b0`](#insn-00abf2b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf110`](#insn-00abf110) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf114`](#insn-00abf114) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf118`](#insn-00abf118) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf11c`](#insn-00abf11c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf120`](#insn-00abf120) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf124`](#insn-00abf124) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf130`](#insn-00abf130) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf138`](#insn-00abf138) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf140`](#insn-00abf140) → [`00abf2b0`](#insn-00abf2b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf148`](#insn-00abf148) → `002a00f0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abf14c`](#insn-00abf14c) → [`004428f0`](../00442/004428f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004428f0` · 推定シンボル `None` · 推定型 `None`
- [`00abf150`](#insn-00abf150) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf158`](#insn-00abf158) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf160`](#insn-00abf160) → [`00abf2b0`](#insn-00abf2b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf168`](#insn-00abf168) → [`00ac1ad4`](../00ac1/00ac1ad4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac1ad4` · 推定シンボル `None` · 推定型 `None`
- [`00abf16c`](#insn-00abf16c) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf174`](#insn-00abf174) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf17c`](#insn-00abf17c) → [`00abf2b0`](#insn-00abf2b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf184`](#insn-00abf184) → [`00ac0de8`](../00ac0/00ac0de8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac0de8` · 推定シンボル `None` · 推定型 `None`
- [`00abf188`](#insn-00abf188) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf190`](#insn-00abf190) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf198`](#insn-00abf198) → [`00abf2b0`](#insn-00abf2b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf1a0`](#insn-00abf1a0) → [`00ac0de8`](../00ac0/00ac0de8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac0de8` · 推定シンボル `None` · 推定型 `None`
- [`00abf1a8`](#insn-00abf1a8) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf1ac`](#insn-00abf1ac) → [`00abf1fc`](#insn-00abf1fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf1b0`](#insn-00abf1b0) → [`00abf218`](#insn-00abf218) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf1fc`](#insn-00abf1fc) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf200`](#insn-00abf200) → [`00abf238`](#insn-00abf238) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf204`](#insn-00abf204) → [`00abf294`](#insn-00abf294) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf218`](#insn-00abf218) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf21c`](#insn-00abf21c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abf220`](#insn-00abf220) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf224`](#insn-00abf224) → [`00abf238`](#insn-00abf238) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf228`](#insn-00abf228) → [`00abf294`](#insn-00abf294) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf238`](#insn-00abf238) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf23c`](#insn-00abf23c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abf240`](#insn-00abf240) → [`00abf294`](#insn-00abf294) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf294`](#insn-00abf294) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf29c`](#insn-00abf29c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf2a4`](#insn-00abf2a4) → [`00abf2b0`](#insn-00abf2b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf2ac`](#insn-00abf2ac) → [`00c53b3c`](../00c53/00c53b3c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53b3c` · 推定シンボル `None` · 推定型 `None`
- [`00abf2b0`](#insn-00abf2b0) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00abe600`](#insn-00abe600)

~~~json
{
  "source": "00abe600",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe604`](#insn-00abe604)

~~~json
{
  "source": "00abe604",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe608`](#insn-00abe608)

~~~json
{
  "source": "00abe608",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe60c`](#insn-00abe60c)

~~~json
{
  "source": "00abe60c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe610`](#insn-00abe610)

~~~json
{
  "source": "00abe610",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe614`](#insn-00abe614)

~~~json
{
  "source": "00abe614",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe628`](#insn-00abe628)

~~~json
{
  "source": "00abe628",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe630`](#insn-00abe630)

~~~json
{
  "source": "00abe630",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe638`](#insn-00abe638)

~~~json
{
  "source": "00abe638",
  "target": "00ca4578",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4578",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abe63c`](#insn-00abe63c)

~~~json
{
  "source": "00abe63c",
  "target": "00abe664",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe644`](#insn-00abe644)

~~~json
{
  "source": "00abe644",
  "target": "00c65a58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c65a58",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abe64c`](#insn-00abe64c)

~~~json
{
  "source": "00abe64c",
  "target": "00c8cef8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8cef8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abe658`](#insn-00abe658)

~~~json
{
  "source": "00abe658",
  "target": "00c58210",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe660`](#insn-00abe660)

~~~json
{
  "source": "00abe660",
  "target": "00abe668",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe668`](#insn-00abe668)

~~~json
{
  "source": "00abe668",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe678`](#insn-00abe678)

~~~json
{
  "source": "00abe678",
  "target": "008b7904",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe67c`](#insn-00abe67c)

~~~json
{
  "source": "00abe67c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe688`](#insn-00abe688)

~~~json
{
  "source": "00abe688",
  "target": "008b7904",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe68c`](#insn-00abe68c)

~~~json
{
  "source": "00abe68c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe698`](#insn-00abe698)

~~~json
{
  "source": "00abe698",
  "target": "008b7904",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe69c`](#insn-00abe69c)

~~~json
{
  "source": "00abe69c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe6a8`](#insn-00abe6a8)

~~~json
{
  "source": "00abe6a8",
  "target": "008b7904",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe6ac`](#insn-00abe6ac)

~~~json
{
  "source": "00abe6ac",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe6b8`](#insn-00abe6b8)

~~~json
{
  "source": "00abe6b8",
  "target": "008b7904",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe6bc`](#insn-00abe6bc)

~~~json
{
  "source": "00abe6bc",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe6c8`](#insn-00abe6c8)

~~~json
{
  "source": "00abe6c8",
  "target": "008b7904",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe6cc`](#insn-00abe6cc)

~~~json
{
  "source": "00abe6cc",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe6d8`](#insn-00abe6d8)

~~~json
{
  "source": "00abe6d8",
  "target": "008b7904",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe6dc`](#insn-00abe6dc)

~~~json
{
  "source": "00abe6dc",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe6e8`](#insn-00abe6e8)

~~~json
{
  "source": "00abe6e8",
  "target": "008b7904",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe6ec`](#insn-00abe6ec)

~~~json
{
  "source": "00abe6ec",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe6f8`](#insn-00abe6f8)

~~~json
{
  "source": "00abe6f8",
  "target": "008b7904",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe6fc`](#insn-00abe6fc)

~~~json
{
  "source": "00abe6fc",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe708`](#insn-00abe708)

~~~json
{
  "source": "00abe708",
  "target": "008b7904",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe70c`](#insn-00abe70c)

~~~json
{
  "source": "00abe70c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe718`](#insn-00abe718)

~~~json
{
  "source": "00abe718",
  "target": "008b7904",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe71c`](#insn-00abe71c)

~~~json
{
  "source": "00abe71c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe728`](#insn-00abe728)

~~~json
{
  "source": "00abe728",
  "target": "008b7904",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe72c`](#insn-00abe72c)

~~~json
{
  "source": "00abe72c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe738`](#insn-00abe738)

~~~json
{
  "source": "00abe738",
  "target": "008b7904",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe73c`](#insn-00abe73c)

~~~json
{
  "source": "00abe73c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe748`](#insn-00abe748)

~~~json
{
  "source": "00abe748",
  "target": "008b7904",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe74c`](#insn-00abe74c)

~~~json
{
  "source": "00abe74c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe758`](#insn-00abe758)

~~~json
{
  "source": "00abe758",
  "target": "008b7904",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe75c`](#insn-00abe75c)

~~~json
{
  "source": "00abe75c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe768`](#insn-00abe768)

~~~json
{
  "source": "00abe768",
  "target": "008b7904",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe76c`](#insn-00abe76c)

~~~json
{
  "source": "00abe76c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe778`](#insn-00abe778)

~~~json
{
  "source": "00abe778",
  "target": "008b7904",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe77c`](#insn-00abe77c)

~~~json
{
  "source": "00abe77c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe788`](#insn-00abe788)

~~~json
{
  "source": "00abe788",
  "target": "008b7904",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe78c`](#insn-00abe78c)

~~~json
{
  "source": "00abe78c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe798`](#insn-00abe798)

~~~json
{
  "source": "00abe798",
  "target": "008b7904",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe79c`](#insn-00abe79c)

~~~json
{
  "source": "00abe79c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe7a8`](#insn-00abe7a8)

~~~json
{
  "source": "00abe7a8",
  "target": "008b7904",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe7c8`](#insn-00abe7c8)

~~~json
{
  "source": "00abe7c8",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe7d0`](#insn-00abe7d0)

~~~json
{
  "source": "00abe7d0",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe7d8`](#insn-00abe7d8)

~~~json
{
  "source": "00abe7d8",
  "target": "Stack[-0x15c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe7e4`](#insn-00abe7e4)

~~~json
{
  "source": "00abe7e4",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe7ec`](#insn-00abe7ec)

~~~json
{
  "source": "00abe7ec",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe7f4`](#insn-00abe7f4)

~~~json
{
  "source": "00abe7f4",
  "target": "002c2260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe7fc`](#insn-00abe7fc)

~~~json
{
  "source": "00abe7fc",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe800`](#insn-00abe800)

~~~json
{
  "source": "00abe800",
  "target": "00c9af70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9af70",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abe804`](#insn-00abe804)

~~~json
{
  "source": "00abe804",
  "target": "00c9af68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9af68",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abe810`](#insn-00abe810)

~~~json
{
  "source": "00abe810",
  "target": "00c8b358",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b358",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abe810`](#insn-00abe810)

~~~json
{
  "source": "00abe810",
  "target": "00c8b3b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b3b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abe810`](#insn-00abe810)

~~~json
{
  "source": "00abe810",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe814`](#insn-00abe814)

~~~json
{
  "source": "00abe814",
  "target": "00abe828",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe818`](#insn-00abe818)

~~~json
{
  "source": "00abe818",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe824`](#insn-00abe824)

~~~json
{
  "source": "00abe824",
  "target": "00abf0fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe82c`](#insn-00abe82c)

~~~json
{
  "source": "00abe82c",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe840`](#insn-00abe840)

~~~json
{
  "source": "00abe840",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe848`](#insn-00abe848)

~~~json
{
  "source": "00abe848",
  "target": "Stack[-0x15c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe854`](#insn-00abe854)

~~~json
{
  "source": "00abe854",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe858`](#insn-00abe858)

~~~json
{
  "source": "00abe858",
  "target": "00abe880",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe85c`](#insn-00abe85c)

~~~json
{
  "source": "00abe85c",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe864`](#insn-00abe864)

~~~json
{
  "source": "00abe864",
  "target": "00c8b358",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b358",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abe868`](#insn-00abe868)

~~~json
{
  "source": "00abe868",
  "target": "005d8b88",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe870`](#insn-00abe870)

~~~json
{
  "source": "00abe870",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe87c`](#insn-00abe87c)

~~~json
{
  "source": "00abe87c",
  "target": "00abe818",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe894`](#insn-00abe894)

~~~json
{
  "source": "00abe894",
  "target": "00abe818",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe8a4`](#insn-00abe8a4)

~~~json
{
  "source": "00abe8a4",
  "target": "00abf150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe8b4`](#insn-00abe8b4)

~~~json
{
  "source": "00abe8b4",
  "target": "00abe818",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe8c8`](#insn-00abe8c8)

~~~json
{
  "source": "00abe8c8",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe8dc`](#insn-00abe8dc)

~~~json
{
  "source": "00abe8dc",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe8e4`](#insn-00abe8e4)

~~~json
{
  "source": "00abe8e4",
  "target": "00abe9c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe8f0`](#insn-00abe8f0)

~~~json
{
  "source": "00abe8f0",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abe8f4`](#insn-00abe8f4)

~~~json
{
  "source": "00abe8f4",
  "target": "00abeff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe904`](#insn-00abe904)

~~~json
{
  "source": "00abe904",
  "target": "002bb807",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bb807",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "6d6564616c5f253033642e706e6700",
  "capture_start": "002bb807",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abe908`](#insn-00abe908)

~~~json
{
  "source": "00abe908",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe90c`](#insn-00abe90c)

~~~json
{
  "source": "00abe90c",
  "target": "002bb80d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bb807",
  "offset": 6,
  "size": 15,
  "datatype": "string",
  "bytes": "6d6564616c5f253033642e706e6700",
  "capture_start": "002bb807",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abe910`](#insn-00abe910)

~~~json
{
  "source": "00abe910",
  "target": "Stack[-0xd1]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe92c`](#insn-00abe92c)

~~~json
{
  "source": "00abe92c",
  "target": "00447eb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe938`](#insn-00abe938)

~~~json
{
  "source": "00abe938",
  "target": "Stack[-0xef]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe93c`](#insn-00abe93c)

~~~json
{
  "source": "00abe93c",
  "target": "002bcaae",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bcaae",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "6d6564616c5f3030312e696d6763757400",
  "capture_start": "002bcaae",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abe944`](#insn-00abe944)

~~~json
{
  "source": "00abe944",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe948`](#insn-00abe948)

~~~json
{
  "source": "00abe948",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe960`](#insn-00abe960)

~~~json
{
  "source": "00abe960",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abe968`](#insn-00abe968)

~~~json
{
  "source": "00abe968",
  "target": "0047e5cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe96c`](#insn-00abe96c)

~~~json
{
  "source": "00abe96c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe970`](#insn-00abe970)

~~~json
{
  "source": "00abe970",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe97c`](#insn-00abe97c)

~~~json
{
  "source": "00abe97c",
  "target": "00abe990",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe988`](#insn-00abe988)

~~~json
{
  "source": "00abe988",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe98c`](#insn-00abe98c)

~~~json
{
  "source": "00abe98c",
  "target": "00abebac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe990`](#insn-00abe990)

~~~json
{
  "source": "00abe990",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe994`](#insn-00abe994)

~~~json
{
  "source": "00abe994",
  "target": "00abebcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe9a0`](#insn-00abe9a0)

~~~json
{
  "source": "00abe9a0",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe9a4`](#insn-00abe9a4)

~~~json
{
  "source": "00abe9a4",
  "target": "00abebcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe9bc`](#insn-00abe9bc)

~~~json
{
  "source": "00abe9bc",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe9c0`](#insn-00abe9c0)

~~~json
{
  "source": "00abe9c0",
  "target": "00abebcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe9d4`](#insn-00abe9d4)

~~~json
{
  "source": "00abe9d4",
  "target": "00abf16c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe9dc`](#insn-00abe9dc)

~~~json
{
  "source": "00abe9dc",
  "target": "00abd0e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abe9e8`](#insn-00abe9e8)

~~~json
{
  "source": "00abe9e8",
  "target": "00abeae4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abe9ec`](#insn-00abe9ec)

~~~json
{
  "source": "00abe9ec",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abe9f0`](#insn-00abe9f0)

~~~json
{
  "source": "00abe9f0",
  "target": "00abf04c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abea04`](#insn-00abea04)

~~~json
{
  "source": "00abea04",
  "target": "Stack[-0xc9]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abea08`](#insn-00abea08)

~~~json
{
  "source": "00abea08",
  "target": "002b0366",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b0366",
  "offset": 0,
  "size": 23,
  "datatype": "string",
  "bytes": "6d6564616c5f756e6b6e6f776e5f253033642e706e6700",
  "capture_start": "002b0366",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abea0c`](#insn-00abea0c)

~~~json
{
  "source": "00abea0c",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abea10`](#insn-00abea10)

~~~json
{
  "source": "00abea10",
  "target": "002b0374",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b0366",
  "offset": 14,
  "size": 23,
  "datatype": "string",
  "bytes": "6d6564616c5f756e6b6e6f776e5f253033642e706e6700",
  "capture_start": "002b0366",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abea24`](#insn-00abea24)

~~~json
{
  "source": "00abea24",
  "target": "00abf188",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abea3c`](#insn-00abea3c)

~~~json
{
  "source": "00abea3c",
  "target": "00447eb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abea44`](#insn-00abea44)

~~~json
{
  "source": "00abea44",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abea50`](#insn-00abea50)

~~~json
{
  "source": "00abea50",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abea54`](#insn-00abea54)

~~~json
{
  "source": "00abea54",
  "target": "002adfb5",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002adfb5",
  "offset": 0,
  "size": 25,
  "datatype": "string",
  "bytes": "6d6564616c5f756e6b6e6f776e5f3030302e696d6763757400",
  "capture_start": "002adfb5",
  "capture_bytes": 25,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abea58`](#insn-00abea58)

~~~json
{
  "source": "00abea58",
  "target": "002adfc5",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002adfb5",
  "offset": 16,
  "size": 25,
  "datatype": "string",
  "bytes": "6d6564616c5f756e6b6e6f776e5f3030302e696d6763757400",
  "capture_start": "002adfb5",
  "capture_bytes": 25,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abea5c`](#insn-00abea5c)

~~~json
{
  "source": "00abea5c",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abea60`](#insn-00abea60)

~~~json
{
  "source": "00abea60",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abea80`](#insn-00abea80)

~~~json
{
  "source": "00abea80",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abea88`](#insn-00abea88)

~~~json
{
  "source": "00abea88",
  "target": "0047e5cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abea8c`](#insn-00abea8c)

~~~json
{
  "source": "00abea8c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abea90`](#insn-00abea90)

~~~json
{
  "source": "00abea90",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abea9c`](#insn-00abea9c)

~~~json
{
  "source": "00abea9c",
  "target": "00abeab0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeaa8`](#insn-00abeaa8)

~~~json
{
  "source": "00abeaa8",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abeaac`](#insn-00abeaac)

~~~json
{
  "source": "00abeaac",
  "target": "00abedec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeab0`](#insn-00abeab0)

~~~json
{
  "source": "00abeab0",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeab4`](#insn-00abeab4)

~~~json
{
  "source": "00abeab4",
  "target": "00abee0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeac0`](#insn-00abeac0)

~~~json
{
  "source": "00abeac0",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abeac4`](#insn-00abeac4)

~~~json
{
  "source": "00abeac4",
  "target": "00abee0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeadc`](#insn-00abeadc)

~~~json
{
  "source": "00abeadc",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abeae0`](#insn-00abeae0)

~~~json
{
  "source": "00abeae0",
  "target": "00abee0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeae4`](#insn-00abeae4)

~~~json
{
  "source": "00abeae4",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abeae8`](#insn-00abeae8)

~~~json
{
  "source": "00abeae8",
  "target": "00abf0a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeaf4`](#insn-00abeaf4)

~~~json
{
  "source": "00abeaf4",
  "target": "Stack[-0xb5]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeaf8`](#insn-00abeaf8)

~~~json
{
  "source": "00abeaf8",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeb04`](#insn-00abeb04)

~~~json
{
  "source": "00abeb04",
  "target": "002af1d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002af1d8",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "6d6564616c5f6c6f73745f3030302e706e6700",
  "capture_start": "002af1d8",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abeb08`](#insn-00abeb08)

~~~json
{
  "source": "00abeb08",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeb0c`](#insn-00abeb0c)

~~~json
{
  "source": "00abeb0c",
  "target": "Stack[-0xca]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeb24`](#insn-00abeb24)

~~~json
{
  "source": "00abeb24",
  "target": "002bf6af",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bf6af",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "6d6564616c5f6c6f73745f3030302e696d6763757400",
  "capture_start": "002bf6af",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abeb28`](#insn-00abeb28)

~~~json
{
  "source": "00abeb28",
  "target": "002bf6bc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bf6af",
  "offset": 13,
  "size": 22,
  "datatype": "string",
  "bytes": "6d6564616c5f6c6f73745f3030302e696d6763757400",
  "capture_start": "002bf6af",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abeb2c`](#insn-00abeb2c)

~~~json
{
  "source": "00abeb2c",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeb48`](#insn-00abeb48)

~~~json
{
  "source": "00abeb48",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abeb50`](#insn-00abeb50)

~~~json
{
  "source": "00abeb50",
  "target": "0047e5cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abeb54`](#insn-00abeb54)

~~~json
{
  "source": "00abeb54",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeb58`](#insn-00abeb58)

~~~json
{
  "source": "00abeb58",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeb64`](#insn-00abeb64)

~~~json
{
  "source": "00abeb64",
  "target": "00abeb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeb70`](#insn-00abeb70)

~~~json
{
  "source": "00abeb70",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abeb74`](#insn-00abeb74)

~~~json
{
  "source": "00abeb74",
  "target": "00abeda8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeb78`](#insn-00abeb78)

~~~json
{
  "source": "00abeb78",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeb7c`](#insn-00abeb7c)

~~~json
{
  "source": "00abeb7c",
  "target": "00abedc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeb88`](#insn-00abeb88)

~~~json
{
  "source": "00abeb88",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abeb8c`](#insn-00abeb8c)

~~~json
{
  "source": "00abeb8c",
  "target": "00abedc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeba4`](#insn-00abeba4)

~~~json
{
  "source": "00abeba4",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abeba8`](#insn-00abeba8)

~~~json
{
  "source": "00abeba8",
  "target": "00abedc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abebc0`](#insn-00abebc0)

~~~json
{
  "source": "00abebc0",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abebc4`](#insn-00abebc4)

~~~json
{
  "source": "00abebc4",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abebc8`](#insn-00abebc8)

~~~json
{
  "source": "00abebc8",
  "target": "00abe998",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abebcc`](#insn-00abebcc)

~~~json
{
  "source": "00abebcc",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abebd0`](#insn-00abebd0)

~~~json
{
  "source": "00abebd0",
  "target": "00abec20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abebd4`](#insn-00abebd4)

~~~json
{
  "source": "00abebd4",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abebd8`](#insn-00abebd8)

~~~json
{
  "source": "00abebd8",
  "target": "00abec30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abebdc`](#insn-00abebdc)

~~~json
{
  "source": "00abebdc",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abebe0`](#insn-00abebe0)

~~~json
{
  "source": "00abebe0",
  "target": "00abebec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abebe4`](#insn-00abebe4)

~~~json
{
  "source": "00abebe4",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abebe8`](#insn-00abebe8)

~~~json
{
  "source": "00abebe8",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abebec`](#insn-00abebec)

~~~json
{
  "source": "00abebec",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abebf4`](#insn-00abebf4)

~~~json
{
  "source": "00abebf4",
  "target": "00abeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abebfc`](#insn-00abebfc)

~~~json
{
  "source": "00abebfc",
  "target": "00abec08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abec04`](#insn-00abec04)

~~~json
{
  "source": "00abec04",
  "target": "00abec44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abec10`](#insn-00abec10)

~~~json
{
  "source": "00abec10",
  "target": "00abec00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abec14`](#insn-00abec14)

~~~json
{
  "source": "00abec14",
  "target": "00abec4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abec1c`](#insn-00abec1c)

~~~json
{
  "source": "00abec1c",
  "target": "00abec00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abec20`](#insn-00abec20)

~~~json
{
  "source": "00abec20",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abec24`](#insn-00abec24)

~~~json
{
  "source": "00abec24",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abec28`](#insn-00abec28)

~~~json
{
  "source": "00abec28",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abec2c`](#insn-00abec2c)

~~~json
{
  "source": "00abec2c",
  "target": "00abebdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abec30`](#insn-00abec30)

~~~json
{
  "source": "00abec30",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abec34`](#insn-00abec34)

~~~json
{
  "source": "00abec34",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abec38`](#insn-00abec38)

~~~json
{
  "source": "00abec38",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abec3c`](#insn-00abec3c)

~~~json
{
  "source": "00abec3c",
  "target": "00abebe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abec40`](#insn-00abec40)

~~~json
{
  "source": "00abec40",
  "target": "00abebec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abec48`](#insn-00abec48)

~~~json
{
  "source": "00abec48",
  "target": "00abec98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abec50`](#insn-00abec50)

~~~json
{
  "source": "00abec50",
  "target": "00abec5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abec58`](#insn-00abec58)

~~~json
{
  "source": "00abec58",
  "target": "00abf130",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abec64`](#insn-00abec64)

~~~json
{
  "source": "00abec64",
  "target": "00abec54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abec68`](#insn-00abec68)

~~~json
{
  "source": "00abec68",
  "target": "00abec78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abec70`](#insn-00abec70)

~~~json
{
  "source": "00abec70",
  "target": "00abec5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abec74`](#insn-00abec74)

~~~json
{
  "source": "00abec74",
  "target": "00abf130",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abec84`](#insn-00abec84)

~~~json
{
  "source": "00abec84",
  "target": "00abec98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abec88`](#insn-00abec88)

~~~json
{
  "source": "00abec88",
  "target": "00abecdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abec94`](#insn-00abec94)

~~~json
{
  "source": "00abec94",
  "target": "00abeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeca0`](#insn-00abeca0)

~~~json
{
  "source": "00abeca0",
  "target": "00abec90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeca4`](#insn-00abeca4)

~~~json
{
  "source": "00abeca4",
  "target": "00abec8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abecac`](#insn-00abecac)

~~~json
{
  "source": "00abecac",
  "target": "00abecb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abecb4`](#insn-00abecb4)

~~~json
{
  "source": "00abecb4",
  "target": "00abf130",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abecc0`](#insn-00abecc0)

~~~json
{
  "source": "00abecc0",
  "target": "00abecb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abecc4`](#insn-00abecc4)

~~~json
{
  "source": "00abecc4",
  "target": "00abed00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeccc`](#insn-00abeccc)

~~~json
{
  "source": "00abeccc",
  "target": "00abecb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abecd0`](#insn-00abecd0)

~~~json
{
  "source": "00abecd0",
  "target": "00abf130",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abecd8`](#insn-00abecd8)

~~~json
{
  "source": "00abecd8",
  "target": "00abee54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abece8`](#insn-00abece8)

~~~json
{
  "source": "00abece8",
  "target": "00abecd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abecec`](#insn-00abecec)

~~~json
{
  "source": "00abecec",
  "target": "00abeea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abecf4`](#insn-00abecf4)

~~~json
{
  "source": "00abecf4",
  "target": "00abecdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abecfc`](#insn-00abecfc)

~~~json
{
  "source": "00abecfc",
  "target": "00abee58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abed08`](#insn-00abed08)

~~~json
{
  "source": "00abed08",
  "target": "00abeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abed0c`](#insn-00abed0c)

~~~json
{
  "source": "00abed0c",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abed28`](#insn-00abed28)

~~~json
{
  "source": "00abed28",
  "target": "00abed14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abed2c`](#insn-00abed2c)

~~~json
{
  "source": "00abed2c",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abed34`](#insn-00abed34)

~~~json
{
  "source": "00abed34",
  "target": "00abeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abed40`](#insn-00abed40)

~~~json
{
  "source": "00abed40",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abed48`](#insn-00abed48)

~~~json
{
  "source": "00abed48",
  "target": "00abeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abed50`](#insn-00abed50)

~~~json
{
  "source": "00abed50",
  "target": "00abed64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abed5c`](#insn-00abed5c)

~~~json
{
  "source": "00abed5c",
  "target": "00abed54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abed60`](#insn-00abed60)

~~~json
{
  "source": "00abed60",
  "target": "00abed78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abed74`](#insn-00abed74)

~~~json
{
  "source": "00abed74",
  "target": "00abed64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abed80`](#insn-00abed80)

~~~json
{
  "source": "00abed80",
  "target": "00abed88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abed98`](#insn-00abed98)

~~~json
{
  "source": "00abed98",
  "target": "004945d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abeda0`](#insn-00abeda0)

~~~json
{
  "source": "00abeda0",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abeda4`](#insn-00abeda4)

~~~json
{
  "source": "00abeda4",
  "target": "00abeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abedbc`](#insn-00abedbc)

~~~json
{
  "source": "00abedbc",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abedc0`](#insn-00abedc0)

~~~json
{
  "source": "00abedc0",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abedc4`](#insn-00abedc4)

~~~json
{
  "source": "00abedc4",
  "target": "00abeb80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abedc8`](#insn-00abedc8)

~~~json
{
  "source": "00abedc8",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abedcc`](#insn-00abedcc)

~~~json
{
  "source": "00abedcc",
  "target": "00abedd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abedd0`](#insn-00abedd0)

~~~json
{
  "source": "00abedd0",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abedd4`](#insn-00abedd4)

~~~json
{
  "source": "00abedd4",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abedd8`](#insn-00abedd8)

~~~json
{
  "source": "00abedd8",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeddc`](#insn-00abeddc)

~~~json
{
  "source": "00abeddc",
  "target": "00abeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abede0`](#insn-00abede0)

~~~json
{
  "source": "00abede0",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abede4`](#insn-00abede4)

~~~json
{
  "source": "00abede4",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abede8`](#insn-00abede8)

~~~json
{
  "source": "00abede8",
  "target": "00abeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abee00`](#insn-00abee00)

~~~json
{
  "source": "00abee00",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abee04`](#insn-00abee04)

~~~json
{
  "source": "00abee04",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abee08`](#insn-00abee08)

~~~json
{
  "source": "00abee08",
  "target": "00abeab8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abee0c`](#insn-00abee0c)

~~~json
{
  "source": "00abee0c",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abee10`](#insn-00abee10)

~~~json
{
  "source": "00abee10",
  "target": "00abee28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abee14`](#insn-00abee14)

~~~json
{
  "source": "00abee14",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abee18`](#insn-00abee18)

~~~json
{
  "source": "00abee18",
  "target": "00abee38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abee1c`](#insn-00abee1c)

~~~json
{
  "source": "00abee1c",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abee20`](#insn-00abee20)

~~~json
{
  "source": "00abee20",
  "target": "00abee48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abee24`](#insn-00abee24)

~~~json
{
  "source": "00abee24",
  "target": "00abeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abee28`](#insn-00abee28)

~~~json
{
  "source": "00abee28",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abee2c`](#insn-00abee2c)

~~~json
{
  "source": "00abee2c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abee30`](#insn-00abee30)

~~~json
{
  "source": "00abee30",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abee34`](#insn-00abee34)

~~~json
{
  "source": "00abee34",
  "target": "00abee1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abee38`](#insn-00abee38)

~~~json
{
  "source": "00abee38",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abee3c`](#insn-00abee3c)

~~~json
{
  "source": "00abee3c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abee40`](#insn-00abee40)

~~~json
{
  "source": "00abee40",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abee44`](#insn-00abee44)

~~~json
{
  "source": "00abee44",
  "target": "00abeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abee48`](#insn-00abee48)

~~~json
{
  "source": "00abee48",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abee4c`](#insn-00abee4c)

~~~json
{
  "source": "00abee4c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abee50`](#insn-00abee50)

~~~json
{
  "source": "00abee50",
  "target": "00abeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abee5c`](#insn-00abee5c)

~~~json
{
  "source": "00abee5c",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abee80`](#insn-00abee80)

~~~json
{
  "source": "00abee80",
  "target": "00abee8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abee90`](#insn-00abee90)

~~~json
{
  "source": "00abee90",
  "target": "0043bb64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abeea4`](#insn-00abeea4)

~~~json
{
  "source": "00abeea4",
  "target": "00abeeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeeb4`](#insn-00abeeb4)

~~~json
{
  "source": "00abeeb4",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abeeb8`](#insn-00abeeb8)

~~~json
{
  "source": "00abeeb8",
  "target": "0046c984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abeee8`](#insn-00abeee8)

~~~json
{
  "source": "00abeee8",
  "target": "00a46704",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abeeec`](#insn-00abeeec)

~~~json
{
  "source": "00abeeec",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abef00`](#insn-00abef00)

~~~json
{
  "source": "00abef00",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abef04`](#insn-00abef04)

~~~json
{
  "source": "00abef04",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abef08`](#insn-00abef08)

~~~json
{
  "source": "00abef08",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abef0c`](#insn-00abef0c)

~~~json
{
  "source": "00abef0c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abef10`](#insn-00abef10)

~~~json
{
  "source": "00abef10",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abef1c`](#insn-00abef1c)

~~~json
{
  "source": "00abef1c",
  "target": "00c8cf20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8cf20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abef1c`](#insn-00abef1c)

~~~json
{
  "source": "00abef1c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abef24`](#insn-00abef24)

~~~json
{
  "source": "00abef24",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abef28`](#insn-00abef28)

~~~json
{
  "source": "00abef28",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abef4c`](#insn-00abef4c)

~~~json
{
  "source": "00abef4c",
  "target": "008b6fa8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abef50`](#insn-00abef50)

~~~json
{
  "source": "00abef50",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abef5c`](#insn-00abef5c)

~~~json
{
  "source": "00abef5c",
  "target": "00abef6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abef60`](#insn-00abef60)

~~~json
{
  "source": "00abef60",
  "target": "00abef80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abef68`](#insn-00abef68)

~~~json
{
  "source": "00abef68",
  "target": "00abef74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abef74`](#insn-00abef74)

~~~json
{
  "source": "00abef74",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abef78`](#insn-00abef78)

~~~json
{
  "source": "00abef78",
  "target": "00c8cf40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8cf40",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abef78`](#insn-00abef78)

~~~json
{
  "source": "00abef78",
  "target": "00c8cf48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8cf48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abef7c`](#insn-00abef7c)

~~~json
{
  "source": "00abef7c",
  "target": "00ac1b3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abef7c`](#insn-00abef7c)

~~~json
{
  "source": "00abef7c",
  "target": "00ac1b40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abef80`](#insn-00abef80)

~~~json
{
  "source": "00abef80",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abef84`](#insn-00abef84)

~~~json
{
  "source": "00abef84",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abef88`](#insn-00abef88)

~~~json
{
  "source": "00abef88",
  "target": "00abefac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abef94`](#insn-00abef94)

~~~json
{
  "source": "00abef94",
  "target": "00c9af68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9af68",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abef9c`](#insn-00abef9c)

~~~json
{
  "source": "00abef9c",
  "target": "00c8b358",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b358",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abefa0`](#insn-00abefa0)

~~~json
{
  "source": "00abefa0",
  "target": "005d8b88",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abefa8`](#insn-00abefa8)

~~~json
{
  "source": "00abefa8",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abefac`](#insn-00abefac)

~~~json
{
  "source": "00abefac",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abefb0`](#insn-00abefb0)

~~~json
{
  "source": "00abefb0",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abefb4`](#insn-00abefb4)

~~~json
{
  "source": "00abefb4",
  "target": "00abe874",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abefbc`](#insn-00abefbc)

~~~json
{
  "source": "00abefbc",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abefc0`](#insn-00abefc0)

~~~json
{
  "source": "00abefc0",
  "target": "00c8b3b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b3b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abefc4`](#insn-00abefc4)

~~~json
{
  "source": "00abefc4",
  "target": "00abe85c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abefd0`](#insn-00abefd0)

~~~json
{
  "source": "00abefd0",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abefd4`](#insn-00abefd4)

~~~json
{
  "source": "00abefd4",
  "target": "00abe85c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abefec`](#insn-00abefec)

~~~json
{
  "source": "00abefec",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abeff0`](#insn-00abeff0)

~~~json
{
  "source": "00abeff0",
  "target": "00abe85c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeff8`](#insn-00abeff8)

~~~json
{
  "source": "00abeff8",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abeffc`](#insn-00abeffc)

~~~json
{
  "source": "00abeffc",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf000`](#insn-00abf000)

~~~json
{
  "source": "00abf000",
  "target": "00abe8f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf008`](#insn-00abf008)

~~~json
{
  "source": "00abf008",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf010`](#insn-00abf010)

~~~json
{
  "source": "00abf010",
  "target": "0047ed74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf01c`](#insn-00abf01c)

~~~json
{
  "source": "00abf01c",
  "target": "00c62b90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c62b90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abf020`](#insn-00abf020)

~~~json
{
  "source": "00abf020",
  "target": "00ca4b08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf024`](#insn-00abf024)

~~~json
{
  "source": "00abf024",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf024`](#insn-00abf024)

~~~json
{
  "source": "00abf024",
  "target": "00ca4b08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf02c`](#insn-00abf02c)

~~~json
{
  "source": "00abf02c",
  "target": "00ca4b28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf02c`](#insn-00abf02c)

~~~json
{
  "source": "00abf02c",
  "target": "00ca4b30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf030`](#insn-00abf030)

~~~json
{
  "source": "00abf030",
  "target": "00ca4b20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf034`](#insn-00abf034)

~~~json
{
  "source": "00abf034",
  "target": "00ca4b10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf034`](#insn-00abf034)

~~~json
{
  "source": "00abf034",
  "target": "00ca4b18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf034`](#insn-00abf034)

~~~json
{
  "source": "00abf034",
  "target": "00ca4b20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf038`](#insn-00abf038)

~~~json
{
  "source": "00abf038",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf040`](#insn-00abf040)

~~~json
{
  "source": "00abf040",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf044`](#insn-00abf044)

~~~json
{
  "source": "00abf044",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf048`](#insn-00abf048)

~~~json
{
  "source": "00abf048",
  "target": "00abe8f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf050`](#insn-00abf050)

~~~json
{
  "source": "00abf050",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf054`](#insn-00abf054)

~~~json
{
  "source": "00abf054",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf058`](#insn-00abf058)

~~~json
{
  "source": "00abf058",
  "target": "00abe9f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf060`](#insn-00abf060)

~~~json
{
  "source": "00abf060",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf068`](#insn-00abf068)

~~~json
{
  "source": "00abf068",
  "target": "0047ed74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf074`](#insn-00abf074)

~~~json
{
  "source": "00abf074",
  "target": "00c62b90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c62b90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abf078`](#insn-00abf078)

~~~json
{
  "source": "00abf078",
  "target": "00ca4b08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf07c`](#insn-00abf07c)

~~~json
{
  "source": "00abf07c",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf07c`](#insn-00abf07c)

~~~json
{
  "source": "00abf07c",
  "target": "00ca4b08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf084`](#insn-00abf084)

~~~json
{
  "source": "00abf084",
  "target": "00ca4b28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf084`](#insn-00abf084)

~~~json
{
  "source": "00abf084",
  "target": "00ca4b30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf088`](#insn-00abf088)

~~~json
{
  "source": "00abf088",
  "target": "00ca4b20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf08c`](#insn-00abf08c)

~~~json
{
  "source": "00abf08c",
  "target": "00ca4b10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf08c`](#insn-00abf08c)

~~~json
{
  "source": "00abf08c",
  "target": "00ca4b18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf08c`](#insn-00abf08c)

~~~json
{
  "source": "00abf08c",
  "target": "00ca4b20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf090`](#insn-00abf090)

~~~json
{
  "source": "00abf090",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf098`](#insn-00abf098)

~~~json
{
  "source": "00abf098",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf09c`](#insn-00abf09c)

~~~json
{
  "source": "00abf09c",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf0a0`](#insn-00abf0a0)

~~~json
{
  "source": "00abf0a0",
  "target": "00abe9f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0a8`](#insn-00abf0a8)

~~~json
{
  "source": "00abf0a8",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf0ac`](#insn-00abf0ac)

~~~json
{
  "source": "00abf0ac",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf0b0`](#insn-00abf0b0)

~~~json
{
  "source": "00abf0b0",
  "target": "00abeaec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0b8`](#insn-00abf0b8)

~~~json
{
  "source": "00abf0b8",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf0c0`](#insn-00abf0c0)

~~~json
{
  "source": "00abf0c0",
  "target": "0047ed74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf0cc`](#insn-00abf0cc)

~~~json
{
  "source": "00abf0cc",
  "target": "00c62b90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c62b90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abf0d0`](#insn-00abf0d0)

~~~json
{
  "source": "00abf0d0",
  "target": "00ca4b08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf0d4`](#insn-00abf0d4)

~~~json
{
  "source": "00abf0d4",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf0d4`](#insn-00abf0d4)

~~~json
{
  "source": "00abf0d4",
  "target": "00ca4b08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf0dc`](#insn-00abf0dc)

~~~json
{
  "source": "00abf0dc",
  "target": "00ca4b28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf0dc`](#insn-00abf0dc)

~~~json
{
  "source": "00abf0dc",
  "target": "00ca4b30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf0e0`](#insn-00abf0e0)

~~~json
{
  "source": "00abf0e0",
  "target": "00ca4b20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf0e4`](#insn-00abf0e4)

~~~json
{
  "source": "00abf0e4",
  "target": "00ca4b10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf0e4`](#insn-00abf0e4)

~~~json
{
  "source": "00abf0e4",
  "target": "00ca4b18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf0e4`](#insn-00abf0e4)

~~~json
{
  "source": "00abf0e4",
  "target": "00ca4b20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf0e8`](#insn-00abf0e8)

~~~json
{
  "source": "00abf0e8",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf0f0`](#insn-00abf0f0)

~~~json
{
  "source": "00abf0f0",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abf0f4`](#insn-00abf0f4)

~~~json
{
  "source": "00abf0f4",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf0f8`](#insn-00abf0f8)

~~~json
{
  "source": "00abf0f8",
  "target": "00abeaec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0fc`](#insn-00abf0fc)

~~~json
{
  "source": "00abf0fc",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf104`](#insn-00abf104)

~~~json
{
  "source": "00abf104",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf10c`](#insn-00abf10c)

~~~json
{
  "source": "00abf10c",
  "target": "00abf2b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf110`](#insn-00abf110)

~~~json
{
  "source": "00abf110",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf114`](#insn-00abf114)

~~~json
{
  "source": "00abf114",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf118`](#insn-00abf118)

~~~json
{
  "source": "00abf118",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf11c`](#insn-00abf11c)

~~~json
{
  "source": "00abf11c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf120`](#insn-00abf120)

~~~json
{
  "source": "00abf120",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf124`](#insn-00abf124)

~~~json
{
  "source": "00abf124",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf130`](#insn-00abf130)

~~~json
{
  "source": "00abf130",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf138`](#insn-00abf138)

~~~json
{
  "source": "00abf138",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf140`](#insn-00abf140)

~~~json
{
  "source": "00abf140",
  "target": "00abf2b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf148`](#insn-00abf148)

~~~json
{
  "source": "00abf148",
  "target": "002a00f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a00f0",
  "offset": 0,
  "size": 24,
  "datatype": "string",
  "bytes": "6d61703a3a61743a20206b6579206e6f7420666f756e6400",
  "capture_start": "002a00f0",
  "capture_bytes": 24,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abf14c`](#insn-00abf14c)

~~~json
{
  "source": "00abf14c",
  "target": "004428f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf150`](#insn-00abf150)

~~~json
{
  "source": "00abf150",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf158`](#insn-00abf158)

~~~json
{
  "source": "00abf158",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf160`](#insn-00abf160)

~~~json
{
  "source": "00abf160",
  "target": "00abf2b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf168`](#insn-00abf168)

~~~json
{
  "source": "00abf168",
  "target": "00ac1ad4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf16c`](#insn-00abf16c)

~~~json
{
  "source": "00abf16c",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf174`](#insn-00abf174)

~~~json
{
  "source": "00abf174",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf17c`](#insn-00abf17c)

~~~json
{
  "source": "00abf17c",
  "target": "00abf2b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf184`](#insn-00abf184)

~~~json
{
  "source": "00abf184",
  "target": "00ac0de8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf188`](#insn-00abf188)

~~~json
{
  "source": "00abf188",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf190`](#insn-00abf190)

~~~json
{
  "source": "00abf190",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf198`](#insn-00abf198)

~~~json
{
  "source": "00abf198",
  "target": "00abf2b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf1a0`](#insn-00abf1a0)

~~~json
{
  "source": "00abf1a0",
  "target": "00ac0de8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf1a8`](#insn-00abf1a8)

~~~json
{
  "source": "00abf1a8",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf1ac`](#insn-00abf1ac)

~~~json
{
  "source": "00abf1ac",
  "target": "00abf1fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf1b0`](#insn-00abf1b0)

~~~json
{
  "source": "00abf1b0",
  "target": "00abf218",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf1fc`](#insn-00abf1fc)

~~~json
{
  "source": "00abf1fc",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf200`](#insn-00abf200)

~~~json
{
  "source": "00abf200",
  "target": "00abf238",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf204`](#insn-00abf204)

~~~json
{
  "source": "00abf204",
  "target": "00abf294",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf218`](#insn-00abf218)

~~~json
{
  "source": "00abf218",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf21c`](#insn-00abf21c)

~~~json
{
  "source": "00abf21c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf220`](#insn-00abf220)

~~~json
{
  "source": "00abf220",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf224`](#insn-00abf224)

~~~json
{
  "source": "00abf224",
  "target": "00abf238",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf228`](#insn-00abf228)

~~~json
{
  "source": "00abf228",
  "target": "00abf294",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf238`](#insn-00abf238)

~~~json
{
  "source": "00abf238",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf23c`](#insn-00abf23c)

~~~json
{
  "source": "00abf23c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf240`](#insn-00abf240)

~~~json
{
  "source": "00abf240",
  "target": "00abf294",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf294`](#insn-00abf294)

~~~json
{
  "source": "00abf294",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf29c`](#insn-00abf29c)

~~~json
{
  "source": "00abf29c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf2a4`](#insn-00abf2a4)

~~~json
{
  "source": "00abf2a4",
  "target": "00abf2b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf2ac`](#insn-00abf2ac)

~~~json
{
  "source": "00abf2ac",
  "target": "00c53b3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf2b0`](#insn-00abf2b0)

~~~json
{
  "source": "00abf2b0",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
