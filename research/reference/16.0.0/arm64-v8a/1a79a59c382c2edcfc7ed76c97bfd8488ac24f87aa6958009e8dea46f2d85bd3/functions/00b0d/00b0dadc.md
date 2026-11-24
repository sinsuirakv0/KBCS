# 00b0dadc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aae04c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aae/00aae04c.md) · 移動量 `+0x5fa90`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0053.md#compare-50e00d03b82a7a0f525a24646d9ed312)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b0df04`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0df04.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0067.md#compare-174c3083da307ccce6cee610ec5fe8c3)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_text_sha256": "1da61afc67157bfad2605538d3e0866a42b8916a889d2248bf7314a9e018b78d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b0dadc",
        "00b0e007"
      ],
      [
        "00b0e178",
        "00b0e17b"
      ]
    ],
    "bytes_sha256": "ff25681c41f9fe173f3cb7f63d903e35f8982c5308e4bf6cb2ab40b56330e1e0",
    "instruction_count": 332,
    "instruction_bytes": 1328,
    "body_bytes": 1328,
    "indirect": 0,
    "unresolved": 0
  }
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b0dadc"></a> `00b0dadc` | `ff 83 05 d1` | sub sp,sp,#0x160 | `FALL_THROUGH`
<a id="insn-00b0dae0"></a> `00b0dae0` | `fd 7b 10 a9` | stp x29,x30,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00b0dae4"></a> `00b0dae4` | `fc 6f 11 a9` | stp x28,x27,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00b0dae8"></a> `00b0dae8` | `fa 67 12 a9` | stp x26,x25,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00b0daec"></a> `00b0daec` | `f8 5f 13 a9` | stp x24,x23,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00b0daf0"></a> `00b0daf0` | `f6 57 14 a9` | stp x22,x21,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00b0daf4"></a> `00b0daf4` | `f4 4f 15 a9` | stp x20,x19,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00b0daf8"></a> `00b0daf8` | `fd 03 04 91` | add x29,sp,#0x100 | `FALL_THROUGH`
<a id="insn-00b0dafc"></a> `00b0dafc` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b0db00"></a> `00b0db00` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00b0db04"></a> `00b0db04` | `f5 03 03 2a` | mov w21,w3 | `FALL_THROUGH`
<a id="insn-00b0db08"></a> `00b0db08` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00b0db0c"></a> `00b0db0c` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00b0db10"></a> `00b0db10` | `5f 08 00 71` | cmp w2,#0x2 | `FALL_THROUGH`
<a id="insn-00b0db14"></a> `00b0db14` | `a8 83 1e f8` | stur x8,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00b0db18"></a> `00b0db18` | `8c 09 00 54` | b.gt 0x00b0dc48 | `CONDITIONAL_JUMP`
<a id="insn-00b0db1c"></a> `00b0db1c` | `42 0d 00 34` | cbz w2,0x00b0dcc4 | `CONDITIONAL_JUMP`
<a id="insn-00b0db20"></a> `00b0db20` | `5f 04 00 71` | cmp w2,#0x1 | `FALL_THROUGH`
<a id="insn-00b0db24"></a> `00b0db24` | `00 14 00 54` | b.eq 0x00b0dda4 | `CONDITIONAL_JUMP`
<a id="insn-00b0db28"></a> `00b0db28` | `5f 08 00 71` | cmp w2,#0x2 | `FALL_THROUGH`
<a id="insn-00b0db2c"></a> `00b0db2c` | `81 13 00 54` | b.ne 0x00b0dd9c | `CONDITIONAL_JUMP`
<a id="insn-00b0db30"></a> `00b0db30` | `a8 c3 00 d1` | sub x8,x29,#0x30 | `FALL_THROUGH`
<a id="insn-00b0db34"></a> `00b0db34` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00b0db38"></a> `00b0db38` | `f6 07 00 f9` | str x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b0db3c"></a> `00b0db3c` | `f5 03 04 2a` | mov w21,w4 | `FALL_THROUGH`
<a id="insn-00b0db40"></a> `00b0db40` | `3d a8 f0 97` | bl 0x00737c34 | `UNCONDITIONAL_CALL`
<a id="insn-00b0db44"></a> `00b0db44` | `a8 03 7d a9` | ldp x8,x0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-00b0db48"></a> `00b0db48` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00b0db4c"></a> `00b0db4c` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b0db50"></a> `00b0db50` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00b0db54"></a> `00b0db54` | `e0 18 00 54` | b.eq 0x00b0de70 | `CONDITIONAL_JUMP`
<a id="insn-00b0db58"></a> `00b0db58` | `a9 43 01 d1` | sub x9,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00b0db5c"></a> `00b0db5c` | `8a bd ff b0` | adrp x10,0x2be000 | `FALL_THROUGH`
<a id="insn-00b0db60"></a> `00b0db60` | `4a 39 2c 91` | add x10,x10,#0xb0e | `FALL_THROUGH`
<a id="insn-00b0db64"></a> `00b0db64` | `3b 01 40 b2` | orr x27,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b0db68"></a> `00b0db68` | `bf 02 00 72` | tst w21,#0x1 | `FALL_THROUGH`
<a id="insn-00b0db6c"></a> `00b0db6c` | `69 bd ff f0` | adrp x9,0x2bc000 | `FALL_THROUGH`
<a id="insn-00b0db70"></a> `00b0db70` | `29 f9 1d 91` | add x9,x9,#0x77e | `FALL_THROUGH`
<a id="insn-00b0db74"></a> `00b0db74` | `1c b0 8c 52` | mov w28,#0x6580 | `FALL_THROUGH`
<a id="insn-00b0db78"></a> `00b0db78` | `f8 f3 01 b2` | orr x24,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00b0db7c"></a> `00b0db7c` | `f9 03 1f aa` | mov x25,xzr | `FALL_THROUGH`
<a id="insn-00b0db80"></a> `00b0db80` | `fa 03 1f aa` | mov x26,xzr | `FALL_THROUGH`
<a id="insn-00b0db84"></a> `00b0db84` | `34 11 8a 9a` | csel x20,x9,x10,ne | `FALL_THROUGH`
<a id="insn-00b0db88"></a> `00b0db88` | `3c 07 a0 72` | movk w28,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00b0db8c"></a> `00b0db8c` | `78 55 95 f2` | movk x24,#0xaaab | `FALL_THROUGH`
<a id="insn-00b0db90"></a> `00b0db90` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b0db94"></a> `00b0db94` | `09 00 00 14` | b 0x00b0dbb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0db98"></a> `00b0db98` | `a0 23 7d a9` | ldp x0,x8,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-00b0db9c"></a> `00b0db9c` | `08 01 00 cb` | sub x8,x8,x0 | `FALL_THROUGH`
<a id="insn-00b0dba0"></a> `00b0dba0` | `08 fd 42 93` | asr x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00b0dba4"></a> `00b0dba4` | `08 7d 18 9b` | mul x8,x8,x24 | `FALL_THROUGH`
<a id="insn-00b0dba8"></a> `00b0dba8` | `5a 07 00 91` | add x26,x26,#0x1 | `FALL_THROUGH`
<a id="insn-00b0dbac"></a> `00b0dbac` | `39 33 00 91` | add x25,x25,#0xc | `FALL_THROUGH`
<a id="insn-00b0dbb0"></a> `00b0dbb0` | `1f 01 1a eb` | cmp x8,x26 | `FALL_THROUGH`
<a id="insn-00b0dbb4"></a> `00b0dbb4` | `e9 15 00 54` | b.ls 0x00b0de70 | `CONDITIONAL_JUMP`
<a id="insn-00b0dbb8"></a> `00b0dbb8` | `08 00 19 8b` | add x8,x0,x25 | `FALL_THROUGH`
<a id="insn-00b0dbbc"></a> `00b0dbbc` | `15 5d 40 29` | ldp w21,w23,[x8] | `FALL_THROUGH`
<a id="insn-00b0dbc0"></a> `00b0dbc0` | `16 09 40 b9` | ldr w22,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b0dbc4"></a> `00b0dbc4` | `f7 7e 40 93` | sxtw x23,w23 | `FALL_THROUGH`
<a id="insn-00b0dbc8"></a> `00b0dbc8` | `3c 0e f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00b0dbcc"></a> `00b0dbcc` | `09 18 17 8b` | add x9,x0,x23, LSL #0x6 | `FALL_THROUGH`
<a id="insn-00b0dbd0"></a> `00b0dbd0` | `a8 43 01 d1` | sub x8,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00b0dbd4"></a> `00b0dbd4` | `20 01 1c 8b` | add x0,x9,x28 | `FALL_THROUGH`
<a id="insn-00b0dbd8"></a> `00b0dbd8` | `e1 03 17 2a` | mov w1,w23 | `FALL_THROUGH`
<a id="insn-00b0dbdc"></a> `00b0dbdc` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00b0dbe0"></a> `00b0dbe0` | `e3 03 16 2a` | mov w3,w22 | `FALL_THROUGH`
<a id="insn-00b0dbe4"></a> `00b0dbe4` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00b0dbe8"></a> `00b0dbe8` | `bd ff ff 97` | bl 0x00b0dadc | `UNCONDITIONAL_CALL`
<a id="insn-00b0dbec"></a> `00b0dbec` | `a8 03 5b 38` | ldurb w8,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00b0dbf0"></a> `00b0dbf0` | `aa a7 7b a9` | ldp x10,x9,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00b0dbf4"></a> `00b0dbf4` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b0dbf8"></a> `00b0dbf8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b0dbfc"></a> `00b0dbfc` | `61 03 89 9a` | csel x1,x27,x9,eq | `FALL_THROUGH`
<a id="insn-00b0dc00"></a> `00b0dc00` | `62 01 8a 9a` | csel x2,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00b0dc04"></a> `00b0dc04` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b0dc08"></a> `00b0dc08` | `de 27 05 94` | bl 0x00c57b80 | `UNCONDITIONAL_CALL`
<a id="insn-00b0dc0c"></a> `00b0dc0c` | `a8 03 5b 38` | ldurb w8,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00b0dc10"></a> `00b0dc10` | `68 00 00 36` | tbz w8,#0x0,0x00b0dc1c | `CONDITIONAL_JUMP`
<a id="insn-00b0dc14"></a> `00b0dc14` | `a0 03 5c f8` | ldur x0,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00b0dc18"></a> `00b0dc18` | `a6 27 05 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0dc1c"></a> `00b0dc1c` | `a0 23 7d a9` | ldp x0,x8,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-00b0dc20"></a> `00b0dc20` | `08 01 00 cb` | sub x8,x8,x0 | `FALL_THROUGH`
<a id="insn-00b0dc24"></a> `00b0dc24` | `08 fd 42 93` | asr x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00b0dc28"></a> `00b0dc28` | `08 7d 18 9b` | mul x8,x8,x24 | `FALL_THROUGH`
<a id="insn-00b0dc2c"></a> `00b0dc2c` | `09 05 00 d1` | sub x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b0dc30"></a> `00b0dc30` | `3f 01 1a eb` | cmp x9,x26 | `FALL_THROUGH`
<a id="insn-00b0dc34"></a> `00b0dc34` | `a9 fb ff 54` | b.ls 0x00b0dba8 | `CONDITIONAL_JUMP`
<a id="insn-00b0dc38"></a> `00b0dc38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b0dc3c"></a> `00b0dc3c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00b0dc40"></a> `00b0dc40` | `cc 27 05 94` | bl 0x00c57b70 | `UNCONDITIONAL_CALL`
<a id="insn-00b0dc44"></a> `00b0dc44` | `d5 ff ff 17` | b 0x00b0db98 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0dc48"></a> `00b0dc48` | `5f 0c 00 71` | cmp w2,#0x3 | `FALL_THROUGH`
<a id="insn-00b0dc4c"></a> `00b0dc4c` | `60 07 00 54` | b.eq 0x00b0dd38 | `CONDITIONAL_JUMP`
<a id="insn-00b0dc50"></a> `00b0dc50` | `5f 10 00 71` | cmp w2,#0x4 | `FALL_THROUGH`
<a id="insn-00b0dc54"></a> `00b0dc54` | `a8 c3 00 d1` | sub x8,x29,#0x30 | `FALL_THROUGH`
<a id="insn-00b0dc58"></a> `00b0dc58` | `80 0d 00 54` | b.eq 0x00b0de08 | `CONDITIONAL_JUMP`
<a id="insn-00b0dc5c"></a> `00b0dc5c` | `5f 2c 00 71` | cmp w2,#0xb | `FALL_THROUGH`
<a id="insn-00b0dc60"></a> `00b0dc60` | `e1 09 00 54` | b.ne 0x00b0dd9c | `CONDITIONAL_JUMP`
<a id="insn-00b0dc64"></a> `00b0dc64` | `8a bd ff 90` | adrp x10,0x2bd000 | `FALL_THROUGH`
<a id="insn-00b0dc68"></a> `00b0dc68` | `4a 49 35 91` | add x10,x10,#0xd52 | `FALL_THROUGH`
<a id="insn-00b0dc6c"></a> `00b0dc6c` | `eb 0d 8e 52` | mov w11,#0x706f | `FALL_THROUGH`
<a id="insn-00b0dc70"></a> `00b0dc70` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00b0dc74"></a> `00b0dc74` | `c9 04 80 52` | mov w9,#0x26 | `FALL_THROUGH`
<a id="insn-00b0dc78"></a> `00b0dc78` | `ab 0e ae 72` | movk w11,#0x7075, LSL #16 | `FALL_THROUGH`
<a id="insn-00b0dc7c"></a> `00b0dc7c` | `a9 03 1d 38` | sturb w9,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-00b0dc80"></a> `00b0dc80` | `ab 03 1e b8` | stur w11,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00b0dc84"></a> `00b0dc84` | `00 11 80 3c` | stur q0,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00b0dc88"></a> `00b0dc88` | `bf 43 1e 38` | sturb wzr,[x29, #-0x1c] | `FALL_THROUGH`
<a id="insn-00b0dc8c"></a> `00b0dc8c` | `a8 43 01 d1` | sub x8,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00b0dc90"></a> `00b0dc90` | `a0 c3 00 d1` | sub x0,x29,#0x30 | `FALL_THROUGH`
<a id="insn-00b0dc94"></a> `00b0dc94` | `60 fc e5 97` | bl 0x0048ce14 | `UNCONDITIONAL_CALL`
<a id="insn-00b0dc98"></a> `00b0dc98` | `a8 a3 01 d1` | sub x8,x29,#0x68 | `FALL_THROUGH`
<a id="insn-00b0dc9c"></a> `00b0dc9c` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00b0dca0"></a> `00b0dca0` | `08 44 f0 97` | bl 0x0071ecc0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0dca4"></a> `00b0dca4` | `a0 43 01 d1` | sub x0,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00b0dca8"></a> `00b0dca8` | `a1 a3 01 d1` | sub x1,x29,#0x68 | `FALL_THROUGH`
<a id="insn-00b0dcac"></a> `00b0dcac` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00b0dcb0"></a> `00b0dcb0` | `46 14 e6 97` | bl 0x00492dc8 | `UNCONDITIONAL_CALL`
<a id="insn-00b0dcb4"></a> `00b0dcb4` | `a8 83 59 38` | ldurb w8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00b0dcb8"></a> `00b0dcb8` | `68 16 00 36` | tbz w8,#0x0,0x00b0df84 | `CONDITIONAL_JUMP`
<a id="insn-00b0dcbc"></a> `00b0dcbc` | `a0 83 5a f8` | ldur x0,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-00b0dcc0"></a> `00b0dcc0` | `b0 00 00 14` | b 0x00b0df80 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0dcc4"></a> `00b0dcc4` | `08 24 40 b9` | ldr w8,[x0, #0x24] | `FALL_THROUGH`
<a id="insn-00b0dcc8"></a> `00b0dcc8` | `bf 7f 3d a9` | stp xzr,xzr,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-00b0dccc"></a> `00b0dccc` | `bf 03 1e f8` | stur xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00b0dcd0"></a> `00b0dcd0` | `1f 29 00 71` | cmp w8,#0xa | `FALL_THROUGH`
<a id="insn-00b0dcd4"></a> `00b0dcd4` | `08 18 00 54` | b.hi 0x00b0dfd4 | `CONDITIONAL_JUMP`
<a id="insn-00b0dcd8"></a> `00b0dcd8` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b0dcdc"></a> `00b0dcdc` | `28 21 c8 1a` | lsl w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00b0dce0"></a> `00b0dce0` | `49 a0 80 52` | mov w9,#0x502 | `FALL_THROUGH`
<a id="insn-00b0dce4"></a> `00b0dce4` | `1f 01 09 6a` | tst w8,w9 | `FALL_THROUGH`
<a id="insn-00b0dce8"></a> `00b0dce8` | `60 17 00 54` | b.eq 0x00b0dfd4 | `CONDITIONAL_JUMP`
<a id="insn-00b0dcec"></a> `00b0dcec` | `e1 bc ff f0` | adrp x1,0x2ac000 | `FALL_THROUGH`
<a id="insn-00b0dcf0"></a> `00b0dcf0` | `21 94 2b 91` | add x1,x1,#0xae5 | `FALL_THROUGH`
<a id="insn-00b0dcf4"></a> `00b0dcf4` | `a0 c3 00 d1` | sub x0,x29,#0x30 | `FALL_THROUGH`
<a id="insn-00b0dcf8"></a> `00b0dcf8` | `26 28 05 94` | bl 0x00c57d90 | `UNCONDITIONAL_CALL`
<a id="insn-00b0dcfc"></a> `00b0dcfc` | `a8 43 01 d1` | sub x8,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00b0dd00"></a> `00b0dd00` | `a0 c3 00 d1` | sub x0,x29,#0x30 | `FALL_THROUGH`
<a id="insn-00b0dd04"></a> `00b0dd04` | `44 fc e5 97` | bl 0x0048ce14 | `UNCONDITIONAL_CALL`
<a id="insn-00b0dd08"></a> `00b0dd08` | `e8 03 02 91` | add x8,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00b0dd0c"></a> `00b0dd0c` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00b0dd10"></a> `00b0dd10` | `ec 43 f0 97` | bl 0x0071ecc0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0dd14"></a> `00b0dd14` | `a0 43 01 d1` | sub x0,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00b0dd18"></a> `00b0dd18` | `e1 03 02 91` | add x1,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00b0dd1c"></a> `00b0dd1c` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00b0dd20"></a> `00b0dd20` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00b0dd24"></a> `00b0dd24` | `08 32 eb 97` | bl 0x005da544 | `UNCONDITIONAL_CALL`
<a id="insn-00b0dd28"></a> `00b0dd28` | `e8 03 42 39` | ldrb w8,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00b0dd2c"></a> `00b0dd2c` | `c8 12 00 36` | tbz w8,#0x0,0x00b0df84 | `CONDITIONAL_JUMP`
<a id="insn-00b0dd30"></a> `00b0dd30` | `e0 4b 40 f9` | ldr x0,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b0dd34"></a> `00b0dd34` | `93 00 00 14` | b 0x00b0df80 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0dd38"></a> `00b0dd38` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00b0dd3c"></a> `00b0dd3c` | `55 27 05 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00b0dd40"></a> `00b0dd40` | `a8 bc ff d0` | adrp x8,0x2a3000 | `FALL_THROUGH`
<a id="insn-00b0dd44"></a> `00b0dd44` | `08 51 18 91` | add x8,x8,#0x614 | `FALL_THROUGH`
<a id="insn-00b0dd48"></a> `00b0dd48` | `a9 bd ff b0` | adrp x9,0x2c2000 | `FALL_THROUGH`
<a id="insn-00b0dd4c"></a> `00b0dd4c` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00b0dd50"></a> `00b0dd50` | `01 f1 c0 3c` | ldur q1,[x8, #0xf] | `FALL_THROUGH`
<a id="insn-00b0dd54"></a> `00b0dd54` | `22 71 c2 3d` | ldr q2,[x9, #0x9c0] | `FALL_THROUGH`
<a id="insn-00b0dd58"></a> `00b0dd58` | `a0 03 1e f8` | stur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00b0dd5c"></a> `00b0dd5c` | `00 00 80 3d` | str q0,[x0] | `FALL_THROUGH`
<a id="insn-00b0dd60"></a> `00b0dd60` | `01 f0 80 3c` | stur q1,[x0, #0xf] | `FALL_THROUGH`
<a id="insn-00b0dd64"></a> `00b0dd64` | `a2 03 9d 3c` | stur q2,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-00b0dd68"></a> `00b0dd68` | `1f 7c 00 39` | strb wzr,[x0, #0x1f] | `FALL_THROUGH`
<a id="insn-00b0dd6c"></a> `00b0dd6c` | `d3 0d f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00b0dd70"></a> `00b0dd70` | `08 3c 80 52` | mov w8,#0x1e0 | `FALL_THROUGH`
<a id="insn-00b0dd74"></a> `00b0dd74` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00b0dd78"></a> `00b0dd78` | `08 11 4b 91` | add x8,x8,#0x2c4, LSL #12 | `FALL_THROUGH`
<a id="insn-00b0dd7c"></a> `00b0dd7c` | `08 61 1a 91` | add x8,x8,#0x698 | `FALL_THROUGH`
<a id="insn-00b0dd80"></a> `00b0dd80` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00b0dd84"></a> `00b0dd84` | `09 08 00 37` | tbnz w9,#0x0,0x00b0de84 | `CONDITIONAL_JUMP`
<a id="insn-00b0dd88"></a> `00b0dd88` | `09 09 40 f9` | ldr x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00b0dd8c"></a> `00b0dd8c` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00b0dd90"></a> `00b0dd90` | `a9 03 1c f8` | stur x9,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00b0dd94"></a> `00b0dd94` | `a0 03 9b 3c` | stur q0,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00b0dd98"></a> `00b0dd98` | `3e 00 00 14` | b 0x00b0de90 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0dd9c"></a> `00b0dd9c` | `7f 02 00 79` | strh wzr,[x19] | `FALL_THROUGH`
<a id="insn-00b0dda0"></a> `00b0dda0` | `81 00 00 14` | b 0x00b0dfa4 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0dda4"></a> `00b0dda4` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00b0dda8"></a> `00b0dda8` | `3a 27 05 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ddac"></a> `00b0ddac` | `28 bd ff b0` | adrp x8,0x2b2000 | `FALL_THROUGH`
<a id="insn-00b0ddb0"></a> `00b0ddb0` | `08 25 00 91` | add x8,x8,#0x9 | `FALL_THROUGH`
<a id="insn-00b0ddb4"></a> `00b0ddb4` | `a9 bd ff b0` | adrp x9,0x2c2000 | `FALL_THROUGH`
<a id="insn-00b0ddb8"></a> `00b0ddb8` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00b0ddbc"></a> `00b0ddbc` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00b0ddc0"></a> `00b0ddc0` | `21 99 c0 3d` | ldr q1,[x9, #0x260] | `FALL_THROUGH`
<a id="insn-00b0ddc4"></a> `00b0ddc4` | `a0 03 1e f8` | stur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00b0ddc8"></a> `00b0ddc8` | `00 00 80 3d` | str q0,[x0] | `FALL_THROUGH`
<a id="insn-00b0ddcc"></a> `00b0ddcc` | `08 08 00 f9` | str x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b0ddd0"></a> `00b0ddd0` | `a1 03 9d 3c` | stur q1,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-00b0ddd4"></a> `00b0ddd4` | `1f 60 00 39` | strb wzr,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00b0ddd8"></a> `00b0ddd8` | `b8 0d f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00b0dddc"></a> `00b0dddc` | `08 3c 80 52` | mov w8,#0x1e0 | `FALL_THROUGH`
<a id="insn-00b0dde0"></a> `00b0dde0` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00b0dde4"></a> `00b0dde4` | `08 11 4b 91` | add x8,x8,#0x2c4, LSL #12 | `FALL_THROUGH`
<a id="insn-00b0dde8"></a> `00b0dde8` | `08 61 1a 91` | add x8,x8,#0x698 | `FALL_THROUGH`
<a id="insn-00b0ddec"></a> `00b0ddec` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00b0ddf0"></a> `00b0ddf0` | `49 06 00 37` | tbnz w9,#0x0,0x00b0deb8 | `CONDITIONAL_JUMP`
<a id="insn-00b0ddf4"></a> `00b0ddf4` | `09 09 40 f9` | ldr x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00b0ddf8"></a> `00b0ddf8` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00b0ddfc"></a> `00b0ddfc` | `a9 03 1c f8` | stur x9,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00b0de00"></a> `00b0de00` | `a0 03 9b 3c` | stur q0,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00b0de04"></a> `00b0de04` | `30 00 00 14` | b 0x00b0dec4 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0de08"></a> `00b0de08` | `2a bd ff d0` | adrp x10,0x2b3000 | `FALL_THROUGH`
<a id="insn-00b0de0c"></a> `00b0de0c` | `4a 39 3c 91` | add x10,x10,#0xf0e | `FALL_THROUGH`
<a id="insn-00b0de10"></a> `00b0de10` | `89 04 80 52` | mov w9,#0x24 | `FALL_THROUGH`
<a id="insn-00b0de14"></a> `00b0de14` | `40 01 c0 3d` | ldr q0,[x10] | `FALL_THROUGH`
<a id="insn-00b0de18"></a> `00b0de18` | `ab 0e 8e 52` | mov w11,#0x7075 | `FALL_THROUGH`
<a id="insn-00b0de1c"></a> `00b0de1c` | `a9 03 1d 38` | sturb w9,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-00b0de20"></a> `00b0de20` | `0b 11 01 78` | sturh w11,[x8, #0x11] | `FALL_THROUGH`
<a id="insn-00b0de24"></a> `00b0de24` | `00 11 80 3c` | stur q0,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00b0de28"></a> `00b0de28` | `bf 33 1e 38` | sturb wzr,[x29, #-0x1d] | `FALL_THROUGH`
<a id="insn-00b0de2c"></a> `00b0de2c` | `a3 0d f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00b0de30"></a> `00b0de30` | `08 c9 82 52` | mov w8,#0x1648 | `FALL_THROUGH`
<a id="insn-00b0de34"></a> `00b0de34` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00b0de38"></a> `00b0de38` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00b0de3c"></a> `00b0de3c` | `eb e5 ed 97` | bl 0x006875e8 | `UNCONDITIONAL_CALL`
<a id="insn-00b0de40"></a> `00b0de40` | `a8 43 01 d1` | sub x8,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00b0de44"></a> `00b0de44` | `4b dc ed 97` | bl 0x00684f70 | `UNCONDITIONAL_CALL`
<a id="insn-00b0de48"></a> `00b0de48` | `e8 a3 01 91` | add x8,sp,#0x68 | `FALL_THROUGH`
<a id="insn-00b0de4c"></a> `00b0de4c` | `a0 c3 00 d1` | sub x0,x29,#0x30 | `FALL_THROUGH`
<a id="insn-00b0de50"></a> `00b0de50` | `f1 fb e5 97` | bl 0x0048ce14 | `UNCONDITIONAL_CALL`
<a id="insn-00b0de54"></a> `00b0de54` | `a8 03 5b 38` | ldurb w8,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00b0de58"></a> `00b0de58` | `68 07 00 37` | tbnz w8,#0x0,0x00b0df44 | `CONDITIONAL_JUMP`
<a id="insn-00b0de5c"></a> `00b0de5c` | `a0 03 db 3c` | ldur q0,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00b0de60"></a> `00b0de60` | `a8 03 5c f8` | ldur x8,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00b0de64"></a> `00b0de64` | `e0 07 80 3d` | str q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0de68"></a> `00b0de68` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b0de6c"></a> `00b0de6c` | `39 00 00 14` | b 0x00b0df50 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0de70"></a> `00b0de70` | `60 00 00 b4` | cbz x0,0x00b0de7c | `CONDITIONAL_JUMP`
<a id="insn-00b0de74"></a> `00b0de74` | `a0 83 1d f8` | stur x0,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00b0de78"></a> `00b0de78` | `0e 27 05 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0de7c"></a> `00b0de7c` | `f6 07 40 f9` | ldr x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b0de80"></a> `00b0de80` | `49 00 00 14` | b 0x00b0dfa4 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0de84"></a> `00b0de84` | `02 85 40 a9` | ldp x2,x1,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b0de88"></a> `00b0de88` | `a0 43 01 d1` | sub x0,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00b0de8c"></a> `00b0de8c` | `15 b7 e4 97` | bl 0x0043bae0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0de90"></a> `00b0de90` | `e8 a3 01 91` | add x8,sp,#0x68 | `FALL_THROUGH`
<a id="insn-00b0de94"></a> `00b0de94` | `a0 c3 00 d1` | sub x0,x29,#0x30 | `FALL_THROUGH`
<a id="insn-00b0de98"></a> `00b0de98` | `df fb e5 97` | bl 0x0048ce14 | `UNCONDITIONAL_CALL`
<a id="insn-00b0de9c"></a> `00b0de9c` | `a8 03 5b 38` | ldurb w8,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00b0dea0"></a> `00b0dea0` | `68 02 00 37` | tbnz w8,#0x0,0x00b0deec | `CONDITIONAL_JUMP`
<a id="insn-00b0dea4"></a> `00b0dea4` | `a0 03 db 3c` | ldur q0,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00b0dea8"></a> `00b0dea8` | `a8 03 5c f8` | ldur x8,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00b0deac"></a> `00b0deac` | `e0 0f 80 3d` | str q0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b0deb0"></a> `00b0deb0` | `e8 23 00 f9` | str x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b0deb4"></a> `00b0deb4` | `11 00 00 14` | b 0x00b0def8 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0deb8"></a> `00b0deb8` | `02 85 40 a9` | ldp x2,x1,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b0debc"></a> `00b0debc` | `a0 43 01 d1` | sub x0,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00b0dec0"></a> `00b0dec0` | `08 b7 e4 97` | bl 0x0043bae0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0dec4"></a> `00b0dec4` | `e8 a3 01 91` | add x8,sp,#0x68 | `FALL_THROUGH`
<a id="insn-00b0dec8"></a> `00b0dec8` | `a0 c3 00 d1` | sub x0,x29,#0x30 | `FALL_THROUGH`
<a id="insn-00b0decc"></a> `00b0decc` | `d2 fb e5 97` | bl 0x0048ce14 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ded0"></a> `00b0ded0` | `a8 03 5b 38` | ldurb w8,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00b0ded4"></a> `00b0ded4` | `28 02 00 37` | tbnz w8,#0x0,0x00b0df18 | `CONDITIONAL_JUMP`
<a id="insn-00b0ded8"></a> `00b0ded8` | `a0 03 db 3c` | ldur q0,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00b0dedc"></a> `00b0dedc` | `a8 03 5c f8` | ldur x8,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00b0dee0"></a> `00b0dee0` | `e0 17 80 3d` | str q0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b0dee4"></a> `00b0dee4` | `e8 33 00 f9` | str x8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b0dee8"></a> `00b0dee8` | `0f 00 00 14` | b 0x00b0df24 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0deec"></a> `00b0deec` | `a2 87 7b a9` | ldp x2,x1,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00b0def0"></a> `00b0def0` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b0def4"></a> `00b0def4` | `fb b6 e4 97` | bl 0x0043bae0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0def8"></a> `00b0def8` | `e0 a3 01 91` | add x0,sp,#0x68 | `FALL_THROUGH`
<a id="insn-00b0defc"></a> `00b0defc` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b0df00"></a> `00b0df00` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00b0df04"></a> `00b0df04` | `b1 13 e6 97` | bl 0x00492dc8 | `UNCONDITIONAL_CALL`
<a id="insn-00b0df08"></a> `00b0df08` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b0df0c"></a> `00b0df0c` | `48 03 00 36` | tbz w8,#0x0,0x00b0df74 | `CONDITIONAL_JUMP`
<a id="insn-00b0df10"></a> `00b0df10` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b0df14"></a> `00b0df14` | `17 00 00 14` | b 0x00b0df70 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0df18"></a> `00b0df18` | `a2 87 7b a9` | ldp x2,x1,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00b0df1c"></a> `00b0df1c` | `e0 43 01 91` | add x0,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b0df20"></a> `00b0df20` | `f0 b6 e4 97` | bl 0x0043bae0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0df24"></a> `00b0df24` | `e0 a3 01 91` | add x0,sp,#0x68 | `FALL_THROUGH`
<a id="insn-00b0df28"></a> `00b0df28` | `e1 43 01 91` | add x1,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b0df2c"></a> `00b0df2c` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00b0df30"></a> `00b0df30` | `a6 13 e6 97` | bl 0x00492dc8 | `UNCONDITIONAL_CALL`
<a id="insn-00b0df34"></a> `00b0df34` | `e8 43 41 39` | ldrb w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b0df38"></a> `00b0df38` | `e8 01 00 36` | tbz w8,#0x0,0x00b0df74 | `CONDITIONAL_JUMP`
<a id="insn-00b0df3c"></a> `00b0df3c` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b0df40"></a> `00b0df40` | `0c 00 00 14` | b 0x00b0df70 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0df44"></a> `00b0df44` | `a2 87 7b a9` | ldp x2,x1,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00b0df48"></a> `00b0df48` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b0df4c"></a> `00b0df4c` | `e5 b6 e4 97` | bl 0x0043bae0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0df50"></a> `00b0df50` | `e0 a3 01 91` | add x0,sp,#0x68 | `FALL_THROUGH`
<a id="insn-00b0df54"></a> `00b0df54` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b0df58"></a> `00b0df58` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00b0df5c"></a> `00b0df5c` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00b0df60"></a> `00b0df60` | `79 31 eb 97` | bl 0x005da544 | `UNCONDITIONAL_CALL`
<a id="insn-00b0df64"></a> `00b0df64` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0df68"></a> `00b0df68` | `68 00 00 36` | tbz w8,#0x0,0x00b0df74 | `CONDITIONAL_JUMP`
<a id="insn-00b0df6c"></a> `00b0df6c` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b0df70"></a> `00b0df70` | `d0 26 05 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0df74"></a> `00b0df74` | `e8 a3 41 39` | ldrb w8,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00b0df78"></a> `00b0df78` | `68 00 00 36` | tbz w8,#0x0,0x00b0df84 | `CONDITIONAL_JUMP`
<a id="insn-00b0df7c"></a> `00b0df7c` | `e0 3f 40 f9` | ldr x0,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00b0df80"></a> `00b0df80` | `cc 26 05 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0df84"></a> `00b0df84` | `a8 03 5b 38` | ldurb w8,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00b0df88"></a> `00b0df88` | `68 00 00 36` | tbz w8,#0x0,0x00b0df94 | `CONDITIONAL_JUMP`
<a id="insn-00b0df8c"></a> `00b0df8c` | `a0 03 5c f8` | ldur x0,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00b0df90"></a> `00b0df90` | `c8 26 05 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0df94"></a> `00b0df94` | `a8 03 5d 38` | ldurb w8,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-00b0df98"></a> `00b0df98` | `68 00 00 36` | tbz w8,#0x0,0x00b0dfa4 | `CONDITIONAL_JUMP`
<a id="insn-00b0df9c"></a> `00b0df9c` | `a0 03 5e f8` | ldur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00b0dfa0"></a> `00b0dfa0` | `c4 26 05 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0dfa4"></a> `00b0dfa4` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00b0dfa8"></a> `00b0dfa8` | `a9 83 5e f8` | ldur x9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00b0dfac"></a> `00b0dfac` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b0dfb0"></a> `00b0dfb0` | `41 0e 00 54` | b.ne 0x00b0e178 | `CONDITIONAL_JUMP`
<a id="insn-00b0dfb4"></a> `00b0dfb4` | `f4 4f 55 a9` | ldp x20,x19,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00b0dfb8"></a> `00b0dfb8` | `f6 57 54 a9` | ldp x22,x21,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00b0dfbc"></a> `00b0dfbc` | `f8 5f 53 a9` | ldp x24,x23,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00b0dfc0"></a> `00b0dfc0` | `fa 67 52 a9` | ldp x26,x25,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00b0dfc4"></a> `00b0dfc4` | `fc 6f 51 a9` | ldp x28,x27,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00b0dfc8"></a> `00b0dfc8` | `fd 7b 50 a9` | ldp x29,x30,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00b0dfcc"></a> `00b0dfcc` | `ff 83 05 91` | add sp,sp,#0x160 | `FALL_THROUGH`
<a id="insn-00b0dfd0"></a> `00b0dfd0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b0dfd4"></a> `00b0dfd4` | `9f 76 00 71` | cmp w20,#0x1d | `FALL_THROUGH`
<a id="insn-00b0dfd8"></a> `00b0dfd8` | `e8 00 00 54` | b.hi 0x00b0dff4 | `CONDITIONAL_JUMP`
<a id="insn-00b0dfdc"></a> `00b0dfdc` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b0dfe0"></a> `00b0dfe0` | `09 18 88 52` | mov w9,#0x40c0 | `FALL_THROUGH`
<a id="insn-00b0dfe4"></a> `00b0dfe4` | `08 21 d4 1a` | lsl w8,w8,w20 | `FALL_THROUGH`
<a id="insn-00b0dfe8"></a> `00b0dfe8` | `09 06 a4 72` | movk w9,#0x2030, LSL #16 | `FALL_THROUGH`
<a id="insn-00b0dfec"></a> `00b0dfec` | `1f 01 09 6a` | tst w8,w9 | `FALL_THROUGH`
<a id="insn-00b0dff0"></a> `00b0dff0` | `e1 e7 ff 54` | b.ne 0x00b0dcec | `CONDITIONAL_JUMP`
<a id="insn-00b0dff4"></a> `00b0dff4` | `9f 46 02 71` | cmp w20,#0x91 | `FALL_THROUGH`
<a id="insn-00b0dff8"></a> `00b0dff8` | `a0 e7 ff 54` | b.eq 0x00b0dcec | `CONDITIONAL_JUMP`
<a id="insn-00b0dffc"></a> `00b0dffc` | `21 bd ff d0` | adrp x1,0x2b3000 | `FALL_THROUGH`
<a id="insn-00b0e000"></a> `00b0e000` | `21 38 3c 91` | add x1,x1,#0xf0e | `FALL_THROUGH`
<a id="insn-00b0e004"></a> `00b0e004` | `3c ff ff 17` | b 0x00b0dcf4 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0e178"></a> `00b0e178` | `5a 26 05 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b0dadc`](#insn-00b0dadc) 範囲 `[['00b0dadc', '00b0db1b']]`
  - `CONDITIONAL_JUMP` [`00b0db18`](#insn-00b0db18) → [`00b0dc48`](#insn-00b0dc48)
  - `FALL_THROUGH` [`00b0db18`](#insn-00b0db18) → [`00b0db1c`](#insn-00b0db1c)
- ブロック [`00b0db1c`](#insn-00b0db1c) 範囲 `[['00b0db1c', '00b0db1f']]`
  - `CONDITIONAL_JUMP` [`00b0db1c`](#insn-00b0db1c) → [`00b0dcc4`](#insn-00b0dcc4)
  - `FALL_THROUGH` [`00b0db1c`](#insn-00b0db1c) → [`00b0db20`](#insn-00b0db20)
- ブロック [`00b0db20`](#insn-00b0db20) 範囲 `[['00b0db20', '00b0db27']]`
  - `CONDITIONAL_JUMP` [`00b0db24`](#insn-00b0db24) → [`00b0dda4`](#insn-00b0dda4)
  - `FALL_THROUGH` [`00b0db24`](#insn-00b0db24) → [`00b0db28`](#insn-00b0db28)
- ブロック [`00b0db28`](#insn-00b0db28) 範囲 `[['00b0db28', '00b0db2f']]`
  - `CONDITIONAL_JUMP` [`00b0db2c`](#insn-00b0db2c) → [`00b0dd9c`](#insn-00b0dd9c)
  - `FALL_THROUGH` [`00b0db2c`](#insn-00b0db2c) → [`00b0db30`](#insn-00b0db30)
- ブロック [`00b0db30`](#insn-00b0db30) 範囲 `[['00b0db30', '00b0db57']]`
  - `CONDITIONAL_JUMP` [`00b0db54`](#insn-00b0db54) → [`00b0de70`](#insn-00b0de70)
  - `FALL_THROUGH` [`00b0db54`](#insn-00b0db54) → [`00b0db58`](#insn-00b0db58)
- ブロック [`00b0db58`](#insn-00b0db58) 範囲 `[['00b0db58', '00b0db97']]`
  - `UNCONDITIONAL_JUMP` [`00b0db94`](#insn-00b0db94) → [`00b0dbb8`](#insn-00b0dbb8)
- ブロック [`00b0db98`](#insn-00b0db98) 範囲 `[['00b0db98', '00b0dba7']]`
  - `FALL_THROUGH` [`00b0dba4`](#insn-00b0dba4) → [`00b0dba8`](#insn-00b0dba8)
- ブロック [`00b0dba8`](#insn-00b0dba8) 範囲 `[['00b0dba8', '00b0dbb7']]`
  - `CONDITIONAL_JUMP` [`00b0dbb4`](#insn-00b0dbb4) → [`00b0de70`](#insn-00b0de70)
  - `FALL_THROUGH` [`00b0dbb4`](#insn-00b0dbb4) → [`00b0dbb8`](#insn-00b0dbb8)
- ブロック [`00b0dbb8`](#insn-00b0dbb8) 範囲 `[['00b0dbb8', '00b0dc13']]`
  - `CONDITIONAL_JUMP` [`00b0dc10`](#insn-00b0dc10) → [`00b0dc1c`](#insn-00b0dc1c)
  - `FALL_THROUGH` [`00b0dc10`](#insn-00b0dc10) → [`00b0dc14`](#insn-00b0dc14)
- ブロック [`00b0dc14`](#insn-00b0dc14) 範囲 `[['00b0dc14', '00b0dc1b']]`
  - `FALL_THROUGH` [`00b0dc18`](#insn-00b0dc18) → [`00b0dc1c`](#insn-00b0dc1c)
- ブロック [`00b0dc1c`](#insn-00b0dc1c) 範囲 `[['00b0dc1c', '00b0dc37']]`
  - `CONDITIONAL_JUMP` [`00b0dc34`](#insn-00b0dc34) → [`00b0dba8`](#insn-00b0dba8)
  - `FALL_THROUGH` [`00b0dc34`](#insn-00b0dc34) → [`00b0dc38`](#insn-00b0dc38)
- ブロック [`00b0dc38`](#insn-00b0dc38) 範囲 `[['00b0dc38', '00b0dc47']]`
  - `UNCONDITIONAL_JUMP` [`00b0dc44`](#insn-00b0dc44) → [`00b0db98`](#insn-00b0db98)
- ブロック [`00b0dc48`](#insn-00b0dc48) 範囲 `[['00b0dc48', '00b0dc4f']]`
  - `CONDITIONAL_JUMP` [`00b0dc4c`](#insn-00b0dc4c) → [`00b0dd38`](#insn-00b0dd38)
  - `FALL_THROUGH` [`00b0dc4c`](#insn-00b0dc4c) → [`00b0dc50`](#insn-00b0dc50)
- ブロック [`00b0dc50`](#insn-00b0dc50) 範囲 `[['00b0dc50', '00b0dc5b']]`
  - `CONDITIONAL_JUMP` [`00b0dc58`](#insn-00b0dc58) → [`00b0de08`](#insn-00b0de08)
  - `FALL_THROUGH` [`00b0dc58`](#insn-00b0dc58) → [`00b0dc5c`](#insn-00b0dc5c)
- ブロック [`00b0dc5c`](#insn-00b0dc5c) 範囲 `[['00b0dc5c', '00b0dc63']]`
  - `CONDITIONAL_JUMP` [`00b0dc60`](#insn-00b0dc60) → [`00b0dd9c`](#insn-00b0dd9c)
  - `FALL_THROUGH` [`00b0dc60`](#insn-00b0dc60) → [`00b0dc64`](#insn-00b0dc64)
- ブロック [`00b0dc64`](#insn-00b0dc64) 範囲 `[['00b0dc64', '00b0dcbb']]`
  - `CONDITIONAL_JUMP` [`00b0dcb8`](#insn-00b0dcb8) → [`00b0df84`](#insn-00b0df84)
  - `FALL_THROUGH` [`00b0dcb8`](#insn-00b0dcb8) → [`00b0dcbc`](#insn-00b0dcbc)
- ブロック [`00b0dcbc`](#insn-00b0dcbc) 範囲 `[['00b0dcbc', '00b0dcc3']]`
  - `UNCONDITIONAL_JUMP` [`00b0dcc0`](#insn-00b0dcc0) → [`00b0df80`](#insn-00b0df80)
- ブロック [`00b0dcc4`](#insn-00b0dcc4) 範囲 `[['00b0dcc4', '00b0dcd7']]`
  - `CONDITIONAL_JUMP` [`00b0dcd4`](#insn-00b0dcd4) → [`00b0dfd4`](#insn-00b0dfd4)
  - `FALL_THROUGH` [`00b0dcd4`](#insn-00b0dcd4) → [`00b0dcd8`](#insn-00b0dcd8)
- ブロック [`00b0dcd8`](#insn-00b0dcd8) 範囲 `[['00b0dcd8', '00b0dceb']]`
  - `CONDITIONAL_JUMP` [`00b0dce8`](#insn-00b0dce8) → [`00b0dfd4`](#insn-00b0dfd4)
  - `FALL_THROUGH` [`00b0dce8`](#insn-00b0dce8) → [`00b0dcec`](#insn-00b0dcec)
- ブロック [`00b0dcec`](#insn-00b0dcec) 範囲 `[['00b0dcec', '00b0dcf3']]`
  - `FALL_THROUGH` [`00b0dcf0`](#insn-00b0dcf0) → [`00b0dcf4`](#insn-00b0dcf4)
- ブロック [`00b0dcf4`](#insn-00b0dcf4) 範囲 `[['00b0dcf4', '00b0dd2f']]`
  - `CONDITIONAL_JUMP` [`00b0dd2c`](#insn-00b0dd2c) → [`00b0df84`](#insn-00b0df84)
  - `FALL_THROUGH` [`00b0dd2c`](#insn-00b0dd2c) → [`00b0dd30`](#insn-00b0dd30)
- ブロック [`00b0dd30`](#insn-00b0dd30) 範囲 `[['00b0dd30', '00b0dd37']]`
  - `UNCONDITIONAL_JUMP` [`00b0dd34`](#insn-00b0dd34) → [`00b0df80`](#insn-00b0df80)
- ブロック [`00b0dd38`](#insn-00b0dd38) 範囲 `[['00b0dd38', '00b0dd87']]`
  - `CONDITIONAL_JUMP` [`00b0dd84`](#insn-00b0dd84) → [`00b0de84`](#insn-00b0de84)
  - `FALL_THROUGH` [`00b0dd84`](#insn-00b0dd84) → [`00b0dd88`](#insn-00b0dd88)
- ブロック [`00b0dd88`](#insn-00b0dd88) 範囲 `[['00b0dd88', '00b0dd9b']]`
  - `UNCONDITIONAL_JUMP` [`00b0dd98`](#insn-00b0dd98) → [`00b0de90`](#insn-00b0de90)
- ブロック [`00b0dd9c`](#insn-00b0dd9c) 範囲 `[['00b0dd9c', '00b0dda3']]`
  - `UNCONDITIONAL_JUMP` [`00b0dda0`](#insn-00b0dda0) → [`00b0dfa4`](#insn-00b0dfa4)
- ブロック [`00b0dda4`](#insn-00b0dda4) 範囲 `[['00b0dda4', '00b0ddf3']]`
  - `CONDITIONAL_JUMP` [`00b0ddf0`](#insn-00b0ddf0) → [`00b0deb8`](#insn-00b0deb8)
  - `FALL_THROUGH` [`00b0ddf0`](#insn-00b0ddf0) → [`00b0ddf4`](#insn-00b0ddf4)
- ブロック [`00b0ddf4`](#insn-00b0ddf4) 範囲 `[['00b0ddf4', '00b0de07']]`
  - `UNCONDITIONAL_JUMP` [`00b0de04`](#insn-00b0de04) → [`00b0dec4`](#insn-00b0dec4)
- ブロック [`00b0de08`](#insn-00b0de08) 範囲 `[['00b0de08', '00b0de5b']]`
  - `CONDITIONAL_JUMP` [`00b0de58`](#insn-00b0de58) → [`00b0df44`](#insn-00b0df44)
  - `FALL_THROUGH` [`00b0de58`](#insn-00b0de58) → [`00b0de5c`](#insn-00b0de5c)
- ブロック [`00b0de5c`](#insn-00b0de5c) 範囲 `[['00b0de5c', '00b0de6f']]`
  - `UNCONDITIONAL_JUMP` [`00b0de6c`](#insn-00b0de6c) → [`00b0df50`](#insn-00b0df50)
- ブロック [`00b0de70`](#insn-00b0de70) 範囲 `[['00b0de70', '00b0de73']]`
  - `CONDITIONAL_JUMP` [`00b0de70`](#insn-00b0de70) → [`00b0de7c`](#insn-00b0de7c)
  - `FALL_THROUGH` [`00b0de70`](#insn-00b0de70) → [`00b0de74`](#insn-00b0de74)
- ブロック [`00b0de74`](#insn-00b0de74) 範囲 `[['00b0de74', '00b0de7b']]`
  - `FALL_THROUGH` [`00b0de78`](#insn-00b0de78) → [`00b0de7c`](#insn-00b0de7c)
- ブロック [`00b0de7c`](#insn-00b0de7c) 範囲 `[['00b0de7c', '00b0de83']]`
  - `UNCONDITIONAL_JUMP` [`00b0de80`](#insn-00b0de80) → [`00b0dfa4`](#insn-00b0dfa4)
- ブロック [`00b0de84`](#insn-00b0de84) 範囲 `[['00b0de84', '00b0de8f']]`
  - `FALL_THROUGH` [`00b0de8c`](#insn-00b0de8c) → [`00b0de90`](#insn-00b0de90)
- ブロック [`00b0de90`](#insn-00b0de90) 範囲 `[['00b0de90', '00b0dea3']]`
  - `CONDITIONAL_JUMP` [`00b0dea0`](#insn-00b0dea0) → [`00b0deec`](#insn-00b0deec)
  - `FALL_THROUGH` [`00b0dea0`](#insn-00b0dea0) → [`00b0dea4`](#insn-00b0dea4)
- ブロック [`00b0dea4`](#insn-00b0dea4) 範囲 `[['00b0dea4', '00b0deb7']]`
  - `UNCONDITIONAL_JUMP` [`00b0deb4`](#insn-00b0deb4) → [`00b0def8`](#insn-00b0def8)
- ブロック [`00b0deb8`](#insn-00b0deb8) 範囲 `[['00b0deb8', '00b0dec3']]`
  - `FALL_THROUGH` [`00b0dec0`](#insn-00b0dec0) → [`00b0dec4`](#insn-00b0dec4)
- ブロック [`00b0dec4`](#insn-00b0dec4) 範囲 `[['00b0dec4', '00b0ded7']]`
  - `CONDITIONAL_JUMP` [`00b0ded4`](#insn-00b0ded4) → [`00b0df18`](#insn-00b0df18)
  - `FALL_THROUGH` [`00b0ded4`](#insn-00b0ded4) → [`00b0ded8`](#insn-00b0ded8)
- ブロック [`00b0ded8`](#insn-00b0ded8) 範囲 `[['00b0ded8', '00b0deeb']]`
  - `UNCONDITIONAL_JUMP` [`00b0dee8`](#insn-00b0dee8) → [`00b0df24`](#insn-00b0df24)
- ブロック [`00b0deec`](#insn-00b0deec) 範囲 `[['00b0deec', '00b0def7']]`
  - `FALL_THROUGH` [`00b0def4`](#insn-00b0def4) → [`00b0def8`](#insn-00b0def8)
- ブロック [`00b0def8`](#insn-00b0def8) 範囲 `[['00b0def8', '00b0df0f']]`
  - `CONDITIONAL_JUMP` [`00b0df0c`](#insn-00b0df0c) → [`00b0df74`](#insn-00b0df74)
  - `FALL_THROUGH` [`00b0df0c`](#insn-00b0df0c) → [`00b0df10`](#insn-00b0df10)
- ブロック [`00b0df10`](#insn-00b0df10) 範囲 `[['00b0df10', '00b0df17']]`
  - `UNCONDITIONAL_JUMP` [`00b0df14`](#insn-00b0df14) → [`00b0df70`](#insn-00b0df70)
- ブロック [`00b0df18`](#insn-00b0df18) 範囲 `[['00b0df18', '00b0df23']]`
  - `FALL_THROUGH` [`00b0df20`](#insn-00b0df20) → [`00b0df24`](#insn-00b0df24)
- ブロック [`00b0df24`](#insn-00b0df24) 範囲 `[['00b0df24', '00b0df3b']]`
  - `CONDITIONAL_JUMP` [`00b0df38`](#insn-00b0df38) → [`00b0df74`](#insn-00b0df74)
  - `FALL_THROUGH` [`00b0df38`](#insn-00b0df38) → [`00b0df3c`](#insn-00b0df3c)
- ブロック [`00b0df3c`](#insn-00b0df3c) 範囲 `[['00b0df3c', '00b0df43']]`
  - `UNCONDITIONAL_JUMP` [`00b0df40`](#insn-00b0df40) → [`00b0df70`](#insn-00b0df70)
- ブロック [`00b0df44`](#insn-00b0df44) 範囲 `[['00b0df44', '00b0df4f']]`
  - `FALL_THROUGH` [`00b0df4c`](#insn-00b0df4c) → [`00b0df50`](#insn-00b0df50)
- ブロック [`00b0df50`](#insn-00b0df50) 範囲 `[['00b0df50', '00b0df6b']]`
  - `CONDITIONAL_JUMP` [`00b0df68`](#insn-00b0df68) → [`00b0df74`](#insn-00b0df74)
  - `FALL_THROUGH` [`00b0df68`](#insn-00b0df68) → [`00b0df6c`](#insn-00b0df6c)
- ブロック [`00b0df6c`](#insn-00b0df6c) 範囲 `[['00b0df6c', '00b0df6f']]`
  - `FALL_THROUGH` [`00b0df6c`](#insn-00b0df6c) → [`00b0df70`](#insn-00b0df70)
- ブロック [`00b0df70`](#insn-00b0df70) 範囲 `[['00b0df70', '00b0df73']]`
  - `FALL_THROUGH` [`00b0df70`](#insn-00b0df70) → [`00b0df74`](#insn-00b0df74)
- ブロック [`00b0df74`](#insn-00b0df74) 範囲 `[['00b0df74', '00b0df7b']]`
  - `CONDITIONAL_JUMP` [`00b0df78`](#insn-00b0df78) → [`00b0df84`](#insn-00b0df84)
  - `FALL_THROUGH` [`00b0df78`](#insn-00b0df78) → [`00b0df7c`](#insn-00b0df7c)
- ブロック [`00b0df7c`](#insn-00b0df7c) 範囲 `[['00b0df7c', '00b0df7f']]`
  - `FALL_THROUGH` [`00b0df7c`](#insn-00b0df7c) → [`00b0df80`](#insn-00b0df80)
- ブロック [`00b0df80`](#insn-00b0df80) 範囲 `[['00b0df80', '00b0df83']]`
  - `FALL_THROUGH` [`00b0df80`](#insn-00b0df80) → [`00b0df84`](#insn-00b0df84)
- ブロック [`00b0df84`](#insn-00b0df84) 範囲 `[['00b0df84', '00b0df8b']]`
  - `CONDITIONAL_JUMP` [`00b0df88`](#insn-00b0df88) → [`00b0df94`](#insn-00b0df94)
  - `FALL_THROUGH` [`00b0df88`](#insn-00b0df88) → [`00b0df8c`](#insn-00b0df8c)
- ブロック [`00b0df8c`](#insn-00b0df8c) 範囲 `[['00b0df8c', '00b0df93']]`
  - `FALL_THROUGH` [`00b0df90`](#insn-00b0df90) → [`00b0df94`](#insn-00b0df94)
- ブロック [`00b0df94`](#insn-00b0df94) 範囲 `[['00b0df94', '00b0df9b']]`
  - `CONDITIONAL_JUMP` [`00b0df98`](#insn-00b0df98) → [`00b0dfa4`](#insn-00b0dfa4)
  - `FALL_THROUGH` [`00b0df98`](#insn-00b0df98) → [`00b0df9c`](#insn-00b0df9c)
- ブロック [`00b0df9c`](#insn-00b0df9c) 範囲 `[['00b0df9c', '00b0dfa3']]`
  - `FALL_THROUGH` [`00b0dfa0`](#insn-00b0dfa0) → [`00b0dfa4`](#insn-00b0dfa4)
- ブロック [`00b0dfa4`](#insn-00b0dfa4) 範囲 `[['00b0dfa4', '00b0dfb3']]`
  - `CONDITIONAL_JUMP` [`00b0dfb0`](#insn-00b0dfb0) → [`00b0e178`](#insn-00b0e178)
  - `FALL_THROUGH` [`00b0dfb0`](#insn-00b0dfb0) → [`00b0dfb4`](#insn-00b0dfb4)
- ブロック [`00b0dfb4`](#insn-00b0dfb4) 範囲 `[['00b0dfb4', '00b0dfd3']]`
- ブロック [`00b0dfd4`](#insn-00b0dfd4) 範囲 `[['00b0dfd4', '00b0dfdb']]`
  - `CONDITIONAL_JUMP` [`00b0dfd8`](#insn-00b0dfd8) → [`00b0dff4`](#insn-00b0dff4)
  - `FALL_THROUGH` [`00b0dfd8`](#insn-00b0dfd8) → [`00b0dfdc`](#insn-00b0dfdc)
- ブロック [`00b0dfdc`](#insn-00b0dfdc) 範囲 `[['00b0dfdc', '00b0dff3']]`
  - `CONDITIONAL_JUMP` [`00b0dff0`](#insn-00b0dff0) → [`00b0dcec`](#insn-00b0dcec)
  - `FALL_THROUGH` [`00b0dff0`](#insn-00b0dff0) → [`00b0dff4`](#insn-00b0dff4)
- ブロック [`00b0dff4`](#insn-00b0dff4) 範囲 `[['00b0dff4', '00b0dffb']]`
  - `CONDITIONAL_JUMP` [`00b0dff8`](#insn-00b0dff8) → [`00b0dcec`](#insn-00b0dcec)
  - `FALL_THROUGH` [`00b0dff8`](#insn-00b0dff8) → [`00b0dffc`](#insn-00b0dffc)
- ブロック [`00b0dffc`](#insn-00b0dffc) 範囲 `[['00b0dffc', '00b0e007']]`
  - `UNCONDITIONAL_JUMP` [`00b0e004`](#insn-00b0e004) → [`00b0dcf4`](#insn-00b0dcf4)
- ブロック [`00b0e178`](#insn-00b0e178) 範囲 `[['00b0e178', '00b0e17b']]`

## 命令位置別の参照

- [`00b0dae0`](#insn-00b0dae0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dae4`](#insn-00b0dae4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dae8`](#insn-00b0dae8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0daec`](#insn-00b0daec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0daf0`](#insn-00b0daf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0daf4`](#insn-00b0daf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0db14`](#insn-00b0db14) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0db18`](#insn-00b0db18) → [`00b0dc48`](#insn-00b0dc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0db1c`](#insn-00b0db1c) → [`00b0dcc4`](#insn-00b0dcc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0db24`](#insn-00b0db24) → [`00b0dda4`](#insn-00b0dda4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0db2c`](#insn-00b0db2c) → [`00b0dd9c`](#insn-00b0dd9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0db38`](#insn-00b0db38) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0db40`](#insn-00b0db40) → [`00737c34`](../00737/00737c34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00737c34` · 推定シンボル `None` · 推定型 `None`
- [`00b0db44`](#insn-00b0db44) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0db54`](#insn-00b0db54) → [`00b0de70`](#insn-00b0de70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0db94`](#insn-00b0db94) → [`00b0dbb8`](#insn-00b0dbb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0db98`](#insn-00b0db98) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dbb4`](#insn-00b0dbb4) → [`00b0de70`](#insn-00b0de70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dbc8`](#insn-00b0dbc8) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00b0dbe8`](#insn-00b0dbe8) → [`00b0dadc`](#insn-00b0dadc) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b0dadc` · 推定シンボル `None` · 推定型 `None`
- [`00b0dbec`](#insn-00b0dbec) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dbf0`](#insn-00b0dbf0) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dc08`](#insn-00b0dc08) → [`00c57b80`](../00c57/00c57b80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57b80` · 推定シンボル `None` · 推定型 `None`
- [`00b0dc0c`](#insn-00b0dc0c) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dc10`](#insn-00b0dc10) → [`00b0dc1c`](#insn-00b0dc1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dc14`](#insn-00b0dc14) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dc18`](#insn-00b0dc18) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00b0dc1c`](#insn-00b0dc1c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dc34`](#insn-00b0dc34) → [`00b0dba8`](#insn-00b0dba8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dc3c`](#insn-00b0dc3c) → `002beb0e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dc40`](#insn-00b0dc40) → [`00c57b70`](../00c57/00c57b70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57b70` · 推定シンボル `None` · 推定型 `None`
- [`00b0dc44`](#insn-00b0dc44) → [`00b0db98`](#insn-00b0db98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dc4c`](#insn-00b0dc4c) → [`00b0dd38`](#insn-00b0dd38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dc58`](#insn-00b0dc58) → [`00b0de08`](#insn-00b0de08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dc60`](#insn-00b0dc60) → [`00b0dd9c`](#insn-00b0dd9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dc70`](#insn-00b0dc70) → `002bdd52`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b0dc7c`](#insn-00b0dc7c) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dc80`](#insn-00b0dc80) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dc84`](#insn-00b0dc84) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dc88`](#insn-00b0dc88) → `Stack[-0x7c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dc94`](#insn-00b0dc94) → [`0048ce14`](../0048c/0048ce14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce14` · 推定シンボル `None` · 推定型 `None`
- [`00b0dca0`](#insn-00b0dca0) → [`0071ecc0`](../0071e/0071ecc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0071ecc0` · 推定シンボル `None` · 推定型 `None`
- [`00b0dcb0`](#insn-00b0dcb0) → [`00492dc8`](../00492/00492dc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00492dc8` · 推定シンボル `None` · 推定型 `None`
- [`00b0dcb4`](#insn-00b0dcb4) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dcb8`](#insn-00b0dcb8) → [`00b0df84`](#insn-00b0df84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dcbc`](#insn-00b0dcbc) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dcc0`](#insn-00b0dcc0) → [`00b0df80`](#insn-00b0df80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dcc8`](#insn-00b0dcc8) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dccc`](#insn-00b0dccc) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dcd4`](#insn-00b0dcd4) → [`00b0dfd4`](#insn-00b0dfd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dce8`](#insn-00b0dce8) → [`00b0dfd4`](#insn-00b0dfd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dcf0`](#insn-00b0dcf0) → `002acae5`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b0dcf8`](#insn-00b0dcf8) → [`00c57d90`](../00c57/00c57d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57d90` · 推定シンボル `None` · 推定型 `None`
- [`00b0dd04`](#insn-00b0dd04) → [`0048ce14`](../0048c/0048ce14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce14` · 推定シンボル `None` · 推定型 `None`
- [`00b0dd10`](#insn-00b0dd10) → [`0071ecc0`](../0071e/0071ecc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0071ecc0` · 推定シンボル `None` · 推定型 `None`
- [`00b0dd24`](#insn-00b0dd24) → [`005da544`](../005da/005da544.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005da544` · 推定シンボル `None` · 推定型 `None`
- [`00b0dd28`](#insn-00b0dd28) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dd2c`](#insn-00b0dd2c) → [`00b0df84`](#insn-00b0df84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dd30`](#insn-00b0dd30) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dd34`](#insn-00b0dd34) → [`00b0df80`](#insn-00b0df80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dd3c`](#insn-00b0dd3c) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00b0dd4c`](#insn-00b0dd4c) → `002a3614`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b0dd50`](#insn-00b0dd50) → `002a3623`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b0dd54`](#insn-00b0dd54) → `002c29c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dd58`](#insn-00b0dd58) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dd64`](#insn-00b0dd64) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dd6c`](#insn-00b0dd6c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00b0dd80`](#insn-00b0dd80) → `002c4698`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b0dd84`](#insn-00b0dd84) → [`00b0de84`](#insn-00b0de84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dd88`](#insn-00b0dd88) → `002c46a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b0dd8c`](#insn-00b0dd8c) → `002c4698`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b0dd90`](#insn-00b0dd90) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dd94`](#insn-00b0dd94) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dd98`](#insn-00b0dd98) → [`00b0de90`](#insn-00b0de90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dda0`](#insn-00b0dda0) → [`00b0dfa4`](#insn-00b0dfa4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dda8`](#insn-00b0dda8) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00b0ddb8`](#insn-00b0ddb8) → `002b2009`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b0ddbc`](#insn-00b0ddbc) → `002b2019`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b0ddc0`](#insn-00b0ddc0) → `002c2260`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ddc4`](#insn-00b0ddc4) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ddd0`](#insn-00b0ddd0) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ddd8`](#insn-00b0ddd8) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00b0ddec`](#insn-00b0ddec) → `002c4698`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b0ddf0`](#insn-00b0ddf0) → [`00b0deb8`](#insn-00b0deb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ddf4`](#insn-00b0ddf4) → `002c46a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b0ddf8`](#insn-00b0ddf8) → `002c4698`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b0ddfc`](#insn-00b0ddfc) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de00`](#insn-00b0de00) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de04`](#insn-00b0de04) → [`00b0dec4`](#insn-00b0dec4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de14`](#insn-00b0de14) → `002b3f0e`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b0de1c`](#insn-00b0de1c) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de20`](#insn-00b0de20) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de24`](#insn-00b0de24) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de28`](#insn-00b0de28) → `Stack[-0x7d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de2c`](#insn-00b0de2c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00b0de3c`](#insn-00b0de3c) → [`006875e8`](../00687/006875e8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006875e8` · 推定シンボル `None` · 推定型 `None`
- [`00b0de44`](#insn-00b0de44) → [`00684f70`](../00684/00684f70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00684f70` · 推定シンボル `None` · 推定型 `None`
- [`00b0de50`](#insn-00b0de50) → [`0048ce14`](../0048c/0048ce14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce14` · 推定シンボル `None` · 推定型 `None`
- [`00b0de54`](#insn-00b0de54) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de58`](#insn-00b0de58) → [`00b0df44`](#insn-00b0df44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de5c`](#insn-00b0de5c) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de60`](#insn-00b0de60) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de64`](#insn-00b0de64) → `Stack[-0x150]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de68`](#insn-00b0de68) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de6c`](#insn-00b0de6c) → [`00b0df50`](#insn-00b0df50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de70`](#insn-00b0de70) → [`00b0de7c`](#insn-00b0de7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de74`](#insn-00b0de74) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de78`](#insn-00b0de78) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00b0de7c`](#insn-00b0de7c) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de80`](#insn-00b0de80) → [`00b0dfa4`](#insn-00b0dfa4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de84`](#insn-00b0de84) → `002c46a0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b0de84`](#insn-00b0de84) → `002c46a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b0de8c`](#insn-00b0de8c) → [`0043bae0`](../0043b/0043bae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bae0` · 推定シンボル `None` · 推定型 `None`
- [`00b0de98`](#insn-00b0de98) → [`0048ce14`](../0048c/0048ce14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce14` · 推定シンボル `None` · 推定型 `None`
- [`00b0de9c`](#insn-00b0de9c) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dea0`](#insn-00b0dea0) → [`00b0deec`](#insn-00b0deec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dea4`](#insn-00b0dea4) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dea8`](#insn-00b0dea8) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0deac`](#insn-00b0deac) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0deb0`](#insn-00b0deb0) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0deb4`](#insn-00b0deb4) → [`00b0def8`](#insn-00b0def8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0deb8`](#insn-00b0deb8) → `002c46a0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b0deb8`](#insn-00b0deb8) → `002c46a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b0dec0`](#insn-00b0dec0) → [`0043bae0`](../0043b/0043bae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bae0` · 推定シンボル `None` · 推定型 `None`
- [`00b0decc`](#insn-00b0decc) → [`0048ce14`](../0048c/0048ce14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce14` · 推定シンボル `None` · 推定型 `None`
- [`00b0ded0`](#insn-00b0ded0) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ded4`](#insn-00b0ded4) → [`00b0df18`](#insn-00b0df18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ded8`](#insn-00b0ded8) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dedc`](#insn-00b0dedc) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dee0`](#insn-00b0dee0) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dee4`](#insn-00b0dee4) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dee8`](#insn-00b0dee8) → [`00b0df24`](#insn-00b0df24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0deec`](#insn-00b0deec) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0def4`](#insn-00b0def4) → [`0043bae0`](../0043b/0043bae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bae0` · 推定シンボル `None` · 推定型 `None`
- [`00b0df04`](#insn-00b0df04) → [`00492dc8`](../00492/00492dc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00492dc8` · 推定シンボル `None` · 推定型 `None`
- [`00b0df08`](#insn-00b0df08) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0df0c`](#insn-00b0df0c) → [`00b0df74`](#insn-00b0df74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0df10`](#insn-00b0df10) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0df14`](#insn-00b0df14) → [`00b0df70`](#insn-00b0df70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0df18`](#insn-00b0df18) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0df20`](#insn-00b0df20) → [`0043bae0`](../0043b/0043bae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bae0` · 推定シンボル `None` · 推定型 `None`
- [`00b0df30`](#insn-00b0df30) → [`00492dc8`](../00492/00492dc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00492dc8` · 推定シンボル `None` · 推定型 `None`
- [`00b0df34`](#insn-00b0df34) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0df38`](#insn-00b0df38) → [`00b0df74`](#insn-00b0df74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0df3c`](#insn-00b0df3c) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0df40`](#insn-00b0df40) → [`00b0df70`](#insn-00b0df70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0df44`](#insn-00b0df44) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0df4c`](#insn-00b0df4c) → [`0043bae0`](../0043b/0043bae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bae0` · 推定シンボル `None` · 推定型 `None`
- [`00b0df60`](#insn-00b0df60) → [`005da544`](../005da/005da544.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005da544` · 推定シンボル `None` · 推定型 `None`
- [`00b0df64`](#insn-00b0df64) → `Stack[-0x150]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0df68`](#insn-00b0df68) → [`00b0df74`](#insn-00b0df74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0df6c`](#insn-00b0df6c) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0df70`](#insn-00b0df70) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00b0df74`](#insn-00b0df74) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0df78`](#insn-00b0df78) → [`00b0df84`](#insn-00b0df84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0df7c`](#insn-00b0df7c) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0df80`](#insn-00b0df80) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00b0df84`](#insn-00b0df84) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0df88`](#insn-00b0df88) → [`00b0df94`](#insn-00b0df94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0df8c`](#insn-00b0df8c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0df90`](#insn-00b0df90) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00b0df94`](#insn-00b0df94) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0df98`](#insn-00b0df98) → [`00b0dfa4`](#insn-00b0dfa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0df9c`](#insn-00b0df9c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dfa0`](#insn-00b0dfa0) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00b0dfa8`](#insn-00b0dfa8) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dfb0`](#insn-00b0dfb0) → [`00b0e178`](#insn-00b0e178) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dfb4`](#insn-00b0dfb4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dfb8`](#insn-00b0dfb8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dfbc`](#insn-00b0dfbc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dfc0`](#insn-00b0dfc0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dfc4`](#insn-00b0dfc4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dfc8`](#insn-00b0dfc8) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dfd8`](#insn-00b0dfd8) → [`00b0dff4`](#insn-00b0dff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dff0`](#insn-00b0dff0) → [`00b0dcec`](#insn-00b0dcec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dff8`](#insn-00b0dff8) → [`00b0dcec`](#insn-00b0dcec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0e000`](#insn-00b0e000) → `002b3f0e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b0e004`](#insn-00b0e004) → [`00b0dcf4`](#insn-00b0dcf4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0e178`](#insn-00b0e178) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b0dae0`](#insn-00b0dae0)

~~~json
{
  "source": "00b0dae0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dae4`](#insn-00b0dae4)

~~~json
{
  "source": "00b0dae4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dae8`](#insn-00b0dae8)

~~~json
{
  "source": "00b0dae8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0daec`](#insn-00b0daec)

~~~json
{
  "source": "00b0daec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0daf0`](#insn-00b0daf0)

~~~json
{
  "source": "00b0daf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0daf4`](#insn-00b0daf4)

~~~json
{
  "source": "00b0daf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0db14`](#insn-00b0db14)

~~~json
{
  "source": "00b0db14",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0db18`](#insn-00b0db18)

~~~json
{
  "source": "00b0db18",
  "target": "00b0dc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0db1c`](#insn-00b0db1c)

~~~json
{
  "source": "00b0db1c",
  "target": "00b0dcc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0db24`](#insn-00b0db24)

~~~json
{
  "source": "00b0db24",
  "target": "00b0dda4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0db2c`](#insn-00b0db2c)

~~~json
{
  "source": "00b0db2c",
  "target": "00b0dd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0db38`](#insn-00b0db38)

~~~json
{
  "source": "00b0db38",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0db40`](#insn-00b0db40)

~~~json
{
  "source": "00b0db40",
  "target": "00737c34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0db44`](#insn-00b0db44)

~~~json
{
  "source": "00b0db44",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0db54`](#insn-00b0db54)

~~~json
{
  "source": "00b0db54",
  "target": "00b0de70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0db94`](#insn-00b0db94)

~~~json
{
  "source": "00b0db94",
  "target": "00b0dbb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0db98`](#insn-00b0db98)

~~~json
{
  "source": "00b0db98",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dbb4`](#insn-00b0dbb4)

~~~json
{
  "source": "00b0dbb4",
  "target": "00b0de70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dbc8`](#insn-00b0dbc8)

~~~json
{
  "source": "00b0dbc8",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0dbe8`](#insn-00b0dbe8)

~~~json
{
  "source": "00b0dbe8",
  "target": "00b0dadc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0dbec`](#insn-00b0dbec)

~~~json
{
  "source": "00b0dbec",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dbf0`](#insn-00b0dbf0)

~~~json
{
  "source": "00b0dbf0",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dc08`](#insn-00b0dc08)

~~~json
{
  "source": "00b0dc08",
  "target": "00c57b80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0dc0c`](#insn-00b0dc0c)

~~~json
{
  "source": "00b0dc0c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dc10`](#insn-00b0dc10)

~~~json
{
  "source": "00b0dc10",
  "target": "00b0dc1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dc14`](#insn-00b0dc14)

~~~json
{
  "source": "00b0dc14",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dc18`](#insn-00b0dc18)

~~~json
{
  "source": "00b0dc18",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0dc1c`](#insn-00b0dc1c)

~~~json
{
  "source": "00b0dc1c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dc34`](#insn-00b0dc34)

~~~json
{
  "source": "00b0dc34",
  "target": "00b0dba8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dc3c`](#insn-00b0dc3c)

~~~json
{
  "source": "00b0dc3c",
  "target": "002beb0e",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dc40`](#insn-00b0dc40)

~~~json
{
  "source": "00b0dc40",
  "target": "00c57b70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0dc44`](#insn-00b0dc44)

~~~json
{
  "source": "00b0dc44",
  "target": "00b0db98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dc4c`](#insn-00b0dc4c)

~~~json
{
  "source": "00b0dc4c",
  "target": "00b0dd38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dc58`](#insn-00b0dc58)

~~~json
{
  "source": "00b0dc58",
  "target": "00b0de08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dc60`](#insn-00b0dc60)

~~~json
{
  "source": "00b0dc60",
  "target": "00b0dd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dc70`](#insn-00b0dc70)

~~~json
{
  "source": "00b0dc70",
  "target": "002bdd52",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bdd52",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "726563656976655f686f6e6f725f706f70757000",
  "capture_start": "002bdd52",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b0dc7c`](#insn-00b0dc7c)

~~~json
{
  "source": "00b0dc7c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dc80`](#insn-00b0dc80)

~~~json
{
  "source": "00b0dc80",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dc84`](#insn-00b0dc84)

~~~json
{
  "source": "00b0dc84",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dc88`](#insn-00b0dc88)

~~~json
{
  "source": "00b0dc88",
  "target": "Stack[-0x7c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dc94`](#insn-00b0dc94)

~~~json
{
  "source": "00b0dc94",
  "target": "0048ce14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0dca0`](#insn-00b0dca0)

~~~json
{
  "source": "00b0dca0",
  "target": "0071ecc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0dcb0`](#insn-00b0dcb0)

~~~json
{
  "source": "00b0dcb0",
  "target": "00492dc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0dcb4`](#insn-00b0dcb4)

~~~json
{
  "source": "00b0dcb4",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dcb8`](#insn-00b0dcb8)

~~~json
{
  "source": "00b0dcb8",
  "target": "00b0df84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dcbc`](#insn-00b0dcbc)

~~~json
{
  "source": "00b0dcbc",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dcc0`](#insn-00b0dcc0)

~~~json
{
  "source": "00b0dcc0",
  "target": "00b0df80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dcc8`](#insn-00b0dcc8)

~~~json
{
  "source": "00b0dcc8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dccc`](#insn-00b0dccc)

~~~json
{
  "source": "00b0dccc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dcd4`](#insn-00b0dcd4)

~~~json
{
  "source": "00b0dcd4",
  "target": "00b0dfd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dce8`](#insn-00b0dce8)

~~~json
{
  "source": "00b0dce8",
  "target": "00b0dfd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dcf0`](#insn-00b0dcf0)

~~~json
{
  "source": "00b0dcf0",
  "target": "002acae5",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002acae5",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "726563656976655f6974656d5f706f7075705f787000",
  "capture_start": "002acae5",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b0dcf8`](#insn-00b0dcf8)

~~~json
{
  "source": "00b0dcf8",
  "target": "00c57d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0dd04`](#insn-00b0dd04)

~~~json
{
  "source": "00b0dd04",
  "target": "0048ce14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0dd10`](#insn-00b0dd10)

~~~json
{
  "source": "00b0dd10",
  "target": "0071ecc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0dd24`](#insn-00b0dd24)

~~~json
{
  "source": "00b0dd24",
  "target": "005da544",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0dd28`](#insn-00b0dd28)

~~~json
{
  "source": "00b0dd28",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dd2c`](#insn-00b0dd2c)

~~~json
{
  "source": "00b0dd2c",
  "target": "00b0df84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dd30`](#insn-00b0dd30)

~~~json
{
  "source": "00b0dd30",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dd34`](#insn-00b0dd34)

~~~json
{
  "source": "00b0dd34",
  "target": "00b0df80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dd3c`](#insn-00b0dd3c)

~~~json
{
  "source": "00b0dd3c",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0dd4c`](#insn-00b0dd4c)

~~~json
{
  "source": "00b0dd4c",
  "target": "002a3614",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a3614",
  "offset": 0,
  "size": 32,
  "datatype": "string",
  "bytes": "726563656976655f6974656d5f706f7075705f63686172615f65766f6c766500",
  "capture_start": "002a3614",
  "capture_bytes": 32,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b0dd50`](#insn-00b0dd50)

~~~json
{
  "source": "00b0dd50",
  "target": "002a3623",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a3614",
  "offset": 15,
  "size": 32,
  "datatype": "string",
  "bytes": "726563656976655f6974656d5f706f7075705f63686172615f65766f6c766500",
  "capture_start": "002a3614",
  "capture_bytes": 32,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b0dd54`](#insn-00b0dd54)

~~~json
{
  "source": "00b0dd54",
  "target": "002c29c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dd58`](#insn-00b0dd58)

~~~json
{
  "source": "00b0dd58",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dd64`](#insn-00b0dd64)

~~~json
{
  "source": "00b0dd64",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dd6c`](#insn-00b0dd6c)

~~~json
{
  "source": "00b0dd6c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0dd80`](#insn-00b0dd80)

~~~json
{
  "source": "00b0dd80",
  "target": "002c4698",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c4638",
  "offset": 96,
  "size": 139,
  "datatype": "string",
  "bytes": "4e5374365f5f6e646b3131305f5f66756e6374696f6e365f5f66756e63495a4e",
  "capture_start": "002c4638",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b0dd84`](#insn-00b0dd84)

~~~json
{
  "source": "00b0dd84",
  "target": "00b0de84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dd88`](#insn-00b0dd88)

~~~json
{
  "source": "00b0dd88",
  "target": "002c46a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c4638",
  "offset": 112,
  "size": 139,
  "datatype": "string",
  "bytes": "4e5374365f5f6e646b3131305f5f66756e6374696f6e365f5f66756e63495a4e",
  "capture_start": "002c4638",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b0dd8c`](#insn-00b0dd8c)

~~~json
{
  "source": "00b0dd8c",
  "target": "002c4698",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c4638",
  "offset": 96,
  "size": 139,
  "datatype": "string",
  "bytes": "4e5374365f5f6e646b3131305f5f66756e6374696f6e365f5f66756e63495a4e",
  "capture_start": "002c4638",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b0dd90`](#insn-00b0dd90)

~~~json
{
  "source": "00b0dd90",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dd94`](#insn-00b0dd94)

~~~json
{
  "source": "00b0dd94",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dd98`](#insn-00b0dd98)

~~~json
{
  "source": "00b0dd98",
  "target": "00b0de90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dda0`](#insn-00b0dda0)

~~~json
{
  "source": "00b0dda0",
  "target": "00b0dfa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dda8`](#insn-00b0dda8)

~~~json
{
  "source": "00b0dda8",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ddb8`](#insn-00b0ddb8)

~~~json
{
  "source": "00b0ddb8",
  "target": "002b2009",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b2009",
  "offset": 0,
  "size": 25,
  "datatype": "string",
  "bytes": "726563656976655f6974656d5f706f7075705f636861726100",
  "capture_start": "002b2009",
  "capture_bytes": 25,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b0ddbc`](#insn-00b0ddbc)

~~~json
{
  "source": "00b0ddbc",
  "target": "002b2019",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b2009",
  "offset": 16,
  "size": 25,
  "datatype": "string",
  "bytes": "726563656976655f6974656d5f706f7075705f636861726100",
  "capture_start": "002b2009",
  "capture_bytes": 25,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b0ddc0`](#insn-00b0ddc0)

~~~json
{
  "source": "00b0ddc0",
  "target": "002c2260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ddc4`](#insn-00b0ddc4)

~~~json
{
  "source": "00b0ddc4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ddd0`](#insn-00b0ddd0)

~~~json
{
  "source": "00b0ddd0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ddd8`](#insn-00b0ddd8)

~~~json
{
  "source": "00b0ddd8",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ddec`](#insn-00b0ddec)

~~~json
{
  "source": "00b0ddec",
  "target": "002c4698",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c4638",
  "offset": 96,
  "size": 139,
  "datatype": "string",
  "bytes": "4e5374365f5f6e646b3131305f5f66756e6374696f6e365f5f66756e63495a4e",
  "capture_start": "002c4638",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b0ddf0`](#insn-00b0ddf0)

~~~json
{
  "source": "00b0ddf0",
  "target": "00b0deb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ddf4`](#insn-00b0ddf4)

~~~json
{
  "source": "00b0ddf4",
  "target": "002c46a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c4638",
  "offset": 112,
  "size": 139,
  "datatype": "string",
  "bytes": "4e5374365f5f6e646b3131305f5f66756e6374696f6e365f5f66756e63495a4e",
  "capture_start": "002c4638",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b0ddf8`](#insn-00b0ddf8)

~~~json
{
  "source": "00b0ddf8",
  "target": "002c4698",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c4638",
  "offset": 96,
  "size": 139,
  "datatype": "string",
  "bytes": "4e5374365f5f6e646b3131305f5f66756e6374696f6e365f5f66756e63495a4e",
  "capture_start": "002c4638",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b0ddfc`](#insn-00b0ddfc)

~~~json
{
  "source": "00b0ddfc",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de00`](#insn-00b0de00)

~~~json
{
  "source": "00b0de00",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de04`](#insn-00b0de04)

~~~json
{
  "source": "00b0de04",
  "target": "00b0dec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de14`](#insn-00b0de14)

~~~json
{
  "source": "00b0de14",
  "target": "002b3f0e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b3f0e",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "726563656976655f6974656d5f706f70757000",
  "capture_start": "002b3f0e",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b0de1c`](#insn-00b0de1c)

~~~json
{
  "source": "00b0de1c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de20`](#insn-00b0de20)

~~~json
{
  "source": "00b0de20",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de24`](#insn-00b0de24)

~~~json
{
  "source": "00b0de24",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de28`](#insn-00b0de28)

~~~json
{
  "source": "00b0de28",
  "target": "Stack[-0x7d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de2c`](#insn-00b0de2c)

~~~json
{
  "source": "00b0de2c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0de3c`](#insn-00b0de3c)

~~~json
{
  "source": "00b0de3c",
  "target": "006875e8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0de44`](#insn-00b0de44)

~~~json
{
  "source": "00b0de44",
  "target": "00684f70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0de50`](#insn-00b0de50)

~~~json
{
  "source": "00b0de50",
  "target": "0048ce14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0de54`](#insn-00b0de54)

~~~json
{
  "source": "00b0de54",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de58`](#insn-00b0de58)

~~~json
{
  "source": "00b0de58",
  "target": "00b0df44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de5c`](#insn-00b0de5c)

~~~json
{
  "source": "00b0de5c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de60`](#insn-00b0de60)

~~~json
{
  "source": "00b0de60",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de64`](#insn-00b0de64)

~~~json
{
  "source": "00b0de64",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de68`](#insn-00b0de68)

~~~json
{
  "source": "00b0de68",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de6c`](#insn-00b0de6c)

~~~json
{
  "source": "00b0de6c",
  "target": "00b0df50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de70`](#insn-00b0de70)

~~~json
{
  "source": "00b0de70",
  "target": "00b0de7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de74`](#insn-00b0de74)

~~~json
{
  "source": "00b0de74",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de78`](#insn-00b0de78)

~~~json
{
  "source": "00b0de78",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0de7c`](#insn-00b0de7c)

~~~json
{
  "source": "00b0de7c",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de80`](#insn-00b0de80)

~~~json
{
  "source": "00b0de80",
  "target": "00b0dfa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de84`](#insn-00b0de84)

~~~json
{
  "source": "00b0de84",
  "target": "002c46a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c4638",
  "offset": 104,
  "size": 139,
  "datatype": "string",
  "bytes": "4e5374365f5f6e646b3131305f5f66756e6374696f6e365f5f66756e63495a4e",
  "capture_start": "002c4638",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b0de84`](#insn-00b0de84)

~~~json
{
  "source": "00b0de84",
  "target": "002c46a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c4638",
  "offset": 112,
  "size": 139,
  "datatype": "string",
  "bytes": "4e5374365f5f6e646b3131305f5f66756e6374696f6e365f5f66756e63495a4e",
  "capture_start": "002c4638",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b0de8c`](#insn-00b0de8c)

~~~json
{
  "source": "00b0de8c",
  "target": "0043bae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0de98`](#insn-00b0de98)

~~~json
{
  "source": "00b0de98",
  "target": "0048ce14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0de9c`](#insn-00b0de9c)

~~~json
{
  "source": "00b0de9c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dea0`](#insn-00b0dea0)

~~~json
{
  "source": "00b0dea0",
  "target": "00b0deec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dea4`](#insn-00b0dea4)

~~~json
{
  "source": "00b0dea4",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dea8`](#insn-00b0dea8)

~~~json
{
  "source": "00b0dea8",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0deac`](#insn-00b0deac)

~~~json
{
  "source": "00b0deac",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0deb0`](#insn-00b0deb0)

~~~json
{
  "source": "00b0deb0",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0deb4`](#insn-00b0deb4)

~~~json
{
  "source": "00b0deb4",
  "target": "00b0def8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0deb8`](#insn-00b0deb8)

~~~json
{
  "source": "00b0deb8",
  "target": "002c46a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c4638",
  "offset": 104,
  "size": 139,
  "datatype": "string",
  "bytes": "4e5374365f5f6e646b3131305f5f66756e6374696f6e365f5f66756e63495a4e",
  "capture_start": "002c4638",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b0deb8`](#insn-00b0deb8)

~~~json
{
  "source": "00b0deb8",
  "target": "002c46a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c4638",
  "offset": 112,
  "size": 139,
  "datatype": "string",
  "bytes": "4e5374365f5f6e646b3131305f5f66756e6374696f6e365f5f66756e63495a4e",
  "capture_start": "002c4638",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b0dec0`](#insn-00b0dec0)

~~~json
{
  "source": "00b0dec0",
  "target": "0043bae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0decc`](#insn-00b0decc)

~~~json
{
  "source": "00b0decc",
  "target": "0048ce14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ded0`](#insn-00b0ded0)

~~~json
{
  "source": "00b0ded0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ded4`](#insn-00b0ded4)

~~~json
{
  "source": "00b0ded4",
  "target": "00b0df18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ded8`](#insn-00b0ded8)

~~~json
{
  "source": "00b0ded8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dedc`](#insn-00b0dedc)

~~~json
{
  "source": "00b0dedc",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dee0`](#insn-00b0dee0)

~~~json
{
  "source": "00b0dee0",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dee4`](#insn-00b0dee4)

~~~json
{
  "source": "00b0dee4",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dee8`](#insn-00b0dee8)

~~~json
{
  "source": "00b0dee8",
  "target": "00b0df24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0deec`](#insn-00b0deec)

~~~json
{
  "source": "00b0deec",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0def4`](#insn-00b0def4)

~~~json
{
  "source": "00b0def4",
  "target": "0043bae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0df04`](#insn-00b0df04)

~~~json
{
  "source": "00b0df04",
  "target": "00492dc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0df08`](#insn-00b0df08)

~~~json
{
  "source": "00b0df08",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0df0c`](#insn-00b0df0c)

~~~json
{
  "source": "00b0df0c",
  "target": "00b0df74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0df10`](#insn-00b0df10)

~~~json
{
  "source": "00b0df10",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0df14`](#insn-00b0df14)

~~~json
{
  "source": "00b0df14",
  "target": "00b0df70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0df18`](#insn-00b0df18)

~~~json
{
  "source": "00b0df18",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0df20`](#insn-00b0df20)

~~~json
{
  "source": "00b0df20",
  "target": "0043bae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0df30`](#insn-00b0df30)

~~~json
{
  "source": "00b0df30",
  "target": "00492dc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0df34`](#insn-00b0df34)

~~~json
{
  "source": "00b0df34",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0df38`](#insn-00b0df38)

~~~json
{
  "source": "00b0df38",
  "target": "00b0df74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0df3c`](#insn-00b0df3c)

~~~json
{
  "source": "00b0df3c",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0df40`](#insn-00b0df40)

~~~json
{
  "source": "00b0df40",
  "target": "00b0df70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0df44`](#insn-00b0df44)

~~~json
{
  "source": "00b0df44",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0df4c`](#insn-00b0df4c)

~~~json
{
  "source": "00b0df4c",
  "target": "0043bae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0df60`](#insn-00b0df60)

~~~json
{
  "source": "00b0df60",
  "target": "005da544",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0df64`](#insn-00b0df64)

~~~json
{
  "source": "00b0df64",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0df68`](#insn-00b0df68)

~~~json
{
  "source": "00b0df68",
  "target": "00b0df74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0df6c`](#insn-00b0df6c)

~~~json
{
  "source": "00b0df6c",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0df70`](#insn-00b0df70)

~~~json
{
  "source": "00b0df70",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0df74`](#insn-00b0df74)

~~~json
{
  "source": "00b0df74",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0df78`](#insn-00b0df78)

~~~json
{
  "source": "00b0df78",
  "target": "00b0df84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0df7c`](#insn-00b0df7c)

~~~json
{
  "source": "00b0df7c",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0df80`](#insn-00b0df80)

~~~json
{
  "source": "00b0df80",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0df84`](#insn-00b0df84)

~~~json
{
  "source": "00b0df84",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0df88`](#insn-00b0df88)

~~~json
{
  "source": "00b0df88",
  "target": "00b0df94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0df8c`](#insn-00b0df8c)

~~~json
{
  "source": "00b0df8c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0df90`](#insn-00b0df90)

~~~json
{
  "source": "00b0df90",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0df94`](#insn-00b0df94)

~~~json
{
  "source": "00b0df94",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0df98`](#insn-00b0df98)

~~~json
{
  "source": "00b0df98",
  "target": "00b0dfa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0df9c`](#insn-00b0df9c)

~~~json
{
  "source": "00b0df9c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dfa0`](#insn-00b0dfa0)

~~~json
{
  "source": "00b0dfa0",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0dfa8`](#insn-00b0dfa8)

~~~json
{
  "source": "00b0dfa8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dfb0`](#insn-00b0dfb0)

~~~json
{
  "source": "00b0dfb0",
  "target": "00b0e178",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dfb4`](#insn-00b0dfb4)

~~~json
{
  "source": "00b0dfb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dfb8`](#insn-00b0dfb8)

~~~json
{
  "source": "00b0dfb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dfbc`](#insn-00b0dfbc)

~~~json
{
  "source": "00b0dfbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dfc0`](#insn-00b0dfc0)

~~~json
{
  "source": "00b0dfc0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dfc4`](#insn-00b0dfc4)

~~~json
{
  "source": "00b0dfc4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dfc8`](#insn-00b0dfc8)

~~~json
{
  "source": "00b0dfc8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dfd8`](#insn-00b0dfd8)

~~~json
{
  "source": "00b0dfd8",
  "target": "00b0dff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dff0`](#insn-00b0dff0)

~~~json
{
  "source": "00b0dff0",
  "target": "00b0dcec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dff8`](#insn-00b0dff8)

~~~json
{
  "source": "00b0dff8",
  "target": "00b0dcec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0e000`](#insn-00b0e000)

~~~json
{
  "source": "00b0e000",
  "target": "002b3f0e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b3f0e",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "726563656976655f6974656d5f706f70757000",
  "capture_start": "002b3f0e",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b0e004`](#insn-00b0e004)

~~~json
{
  "source": "00b0e004",
  "target": "00b0dcf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0e178`](#insn-00b0e178)

~~~json
{
  "source": "00b0e178",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
