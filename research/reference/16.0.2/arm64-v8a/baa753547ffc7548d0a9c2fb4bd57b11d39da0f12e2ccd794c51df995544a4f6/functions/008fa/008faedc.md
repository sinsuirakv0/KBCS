# 008faedc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `008fae88`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fae88.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0053.md#compare-40b90009db86ce18806f6fec57c4d895)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `008fbe88`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008fb/008fbe88.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0055.md#compare-99d12bad5cd836baf4d54a961996f68f)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008faedc",
  "name": "FUN_008faedc",
  "size": 3188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3468ff61cc79121a8fac4c819c0af1fe33c9a80e600ad141feb284b0b12ab278",
  "source_text_sha256": "3468ff61cc79121a8fac4c819c0af1fe33c9a80e600ad141feb284b0b12ab278",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008faedc",
        "008fbb4b"
      ],
      [
        "008fbbbc",
        "008fbbbf"
      ]
    ],
    "bytes_sha256": "37607624e1c518be9fca8c61b74ab480587c07c7cbc4b8abd4c47ea33e286139",
    "instruction_count": 797,
    "instruction_bytes": 3188,
    "body_bytes": 3188,
    "indirect": 20,
    "unresolved": 20
  }
}
~~~

## 呼び出し元

- [008f67b8](../008f6/008f67b8.md)

## 呼び出し先

- [006333b4](../00633/006333b4.md)
- [00758228](../00758/00758228.md)
- [00862ca8](../00862/00862ca8.md)
- [00864590](../00864/00864590.md)
- [00c53da0](../00c53/00c53da0.md)
- [00c57f00](../00c57/00c57f00.md)
- [00c57f20](../00c57/00c57f20.md)
- [00c57f40](../00c57/00c57f40.md)
- [00c57f50](../00c57/00c57f50.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)

## 関連文字列（未確認候補）

~~~text
"1.imgcut"
"2.imgcut"
"4.imgcut"
"5.imgcut"
"6.imgcut"
"9.imgcut"
"img006.imgcut"
"img006.png"
"img015.imgcut"
"img015.png"
"img016.imgcut"
"img016.png"
"img021.imgcut"
"img021.png"
"img024.imgcut"
"img024.png"
"img029.imgcut"
"img029.png"
"img050_02.imgcut"
"img050_02.png"
"img102.imgcut"
"img102.png"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 19328 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */
/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_008faedc(undefined8 *param_1,undefined8 param_2)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  int iVar4;
  long lVar5;
  long *plVar6;
  long *plVar7;
  byte local_a8;
  undefined5 local_a7;
  undefined3 uStack_a2;
  undefined5 uStack_9f;
  char cStack_9a;
  char cStack_99;
  char cStack_98;
  undefined1 uStack_97;
  undefined6 uStack_96;
  byte local_90;
  undefined5 uStack_8f;
  undefined2 uStack_8a;
  char cStack_88;
  undefined2 uStack_87;
  char cStack_85;
  undefined2 uStack_84;
  undefined1 uStack_82;
  undefined1 uStack_81;
  void *local_80;
  undefined8 local_70;
  long *plStack_68;
  long local_58;
  
                    /* catch() { ... } // from try @ 008fae5c with catch @ 008faee4 */
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  FUN_00758228();
  *param_1 = &PTR_FUN_00c85bc8;
  *(undefined1 *)(param_1 + 0x5e) = 1;
  if (((DAT_00ca5038 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca5038), iVar4 != 0)) {
    DAT_00ca5008 = 0;
    DAT_00ca5000 = &DAT_00ca5008;
    DAT_00ca5028 = 0;
    DAT_00ca5030 = 0;
    DAT_00ca5020 = 0;
    DAT_00ca5010 = 0;
    DAT_00ca5018 = &DAT_00ca5020;
    __cxa_atexit(FUN_0047edf4,&DAT_00ca5000,&PTR_LOOP_00c63060);
    __cxa_guard_release(&DAT_00ca5038);
  }
  cStack_85 = 0;
  local_90 = 0x14;
  uStack_87 = 0x676e;
  local_a8 = 0x1a;
  uStack_8f = (undefined5)s_img006_png_002b63ce._0_8_;
  uStack_8a = SUB82(s_img006_png_002b63ce._0_8_,5);
  cStack_88 = SUB81(s_img006_png_002b63ce._0_8_,7);
  cStack_9a = 0;
  local_a7 = _DAT_002b1f47;
  uStack_a2._0_1_ = s_6_imgcut_002b1f4c[0];
  uStack_a2._1_1_ = s_6_imgcut_002b1f4c[1];
  uStack_a2._2_1_ = s_6_imgcut_002b1f4c[2];
  uStack_9f._0_1_ = s_6_imgcut_002b1f4c[3];
  uStack_9f._1_1_ = s_6_imgcut_002b1f4c[4];
  uStack_9f._2_1_ = s_6_imgcut_002b1f4c[5];
  uStack_9f._3_1_ = s_6_imgcut_002b1f4c[6];
  uStack_9f._4_1_ = s_6_imgcut_002b1f4c[7];
                    /* try { // try from 008faf94 to 009fafef has its CatchHandler @ 008faf94
                       catch() { ... } // from try @ 008faf94 with catch @ 008faf94
                       catch() { ... } // from try @ 008fb01c with catch @ 008faf94 */
  FUN_006333b4(&local_70,&DAT_00ca5000,&local_90,&local_a8,0x2601);
  plVar7 = plStack_68;
  uVar2 = local_70;
  plVar6 = (long *)param_1[0x16];
  local_70 = 0;
  plStack_68 = (long *)0x0;
  param_1[0x16] = plVar7;
  param_1[0x15] = uVar2;
  if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00c53da0(0xffffffffffffffff,plVar6 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar6 + 0x10))(plVar6);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
  }
  plVar7 = plStack_68;
  if ((plStack_68 != (long *)0x0) &&
     (lVar5 = FUN_00c53da0(0xffffffffffffffff,plStack_68 + 1), lVar5 == 0)) {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
  }
  if ((local_a8 & 1) != 0) {
    _ZdlPv((void *)CONCAT62(uStack_96,CONCAT11(uStack_97,cStack_98)));
  }
  if ((local_90 & 1) != 0) {
    _ZdlPv(local_80);
  }
  FUN_00864590(&local_90,param_2);
  uVar3 = CONCAT17(uStack_81,
                   CONCAT16(uStack_82,
                            CONCAT24(uStack_84,CONCAT13(cStack_85,CONCAT21(uStack_87,cStack_88)))));
                    /* try { // try from 008fb01c to 009fb16b has its CatchHandler @ 008faf94 */
  uVar2 = CONCAT26(uStack_8a,CONCAT51(uStack_8f,local_90));
  plVar7 = (long *)param_1[0x1a];
  local_90 = 0;
  uStack_8f = 0;
  uStack_8a = 0;
  cStack_88 = 0;
  uStack_87 = 0;
  cStack_85 = 0;
  uStack_84 = 0;
  uStack_82 = 0;
  uStack_81 = 0;
  param_1[0x1a] = uVar3;
  param_1[0x19] = uVar2;
  if ((plVar7 != (long *)0x0) && (lVar5 = FUN_00c53da0(0xffffffffffffffff,plVar7 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
  }
  plVar7 = (long *)CONCAT17(uStack_81,
                            CONCAT16(uStack_82,
                                     CONCAT24(uStack_84,
                                              CONCAT13(cStack_85,CONCAT21(uStack_87,cStack_88)))));
  if ((plVar7 != (long *)0x0) && (lVar5 = FUN_00c53da0(0xffffffffffffffff,plVar7 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
  }
  if (((DAT_00ca5038 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca5038), iVar4 != 0)) {
    DAT_00ca5008 = 0;
    DAT_00ca5000 = &DAT_00ca5008;
    DAT_00ca5028 = 0;
    DAT_00ca5030 = 0;
    DAT_00ca5020 = 0;
    DAT_00ca5010 = 0;
    DAT_00ca5018 = &DAT_00ca5020;
    __cxa_atexit(FUN_0047edf4,&DAT_00ca5000,&PTR_LOOP_00c63060);
    __cxa_guard_release(&DAT_00ca5038);
  }
  cStack_85 = 0;
  local_90 = 0x14;
  uStack_87 = 0x676e;
  local_a8 = 0x1a;
  uStack_8f = (undefined5)s_img024_png_002bef6a._0_8_;
  uStack_8a = SUB82(s_img024_png_002bef6a._0_8_,5);
  cStack_88 = SUB81(s_img024_png_002bef6a._0_8_,7);
  cStack_9a = 0;
  local_a7 = _DAT_002a9f47;
  uStack_a2._0_1_ = s_4_imgcut_002a9f4c[0];
  uStack_a2._1_1_ = s_4_imgcut_002a9f4c[1];
  uStack_a2._2_1_ = s_4_imgcut_002a9f4c[2];
  uStack_9f._0_1_ = s_4_imgcut_002a9f4c[3];
  uStack_9f._1_1_ = s_4_imgcut_002a9f4c[4];
  uStack_9f._2_1_ = s_4_imgcut_002a9f4c[5];
  uStack_9f._3_1_ = s_4_imgcut_002a9f4c[6];
  uStack_9f._4_1_ = s_4_imgcut_002a9f4c[7];
  FUN_006333b4(&local_70,&DAT_00ca5000,&local_90,&local_a8,0x2601);
  plVar7 = plStack_68;
  uVar2 = local_70;
  plVar6 = (long *)param_1[0x20];
  local_70 = 0;
  plStack_68 = (long *)0x0;
  param_1[0x20] = plVar7;
  param_1[0x1f] = uVar2;
  if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00c53da0(0xffffffffffffffff,plVar6 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar6 + 0x10))(plVar6);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
  }
  plVar7 = plStack_68;
                    /* catch() { ... } // from try @ 008faff0 with catch @ 008fb13c */
  if ((plStack_68 != (long *)0x0) &&
     (lVar5 = FUN_00c53da0(0xffffffffffffffff,plStack_68 + 1), lVar5 == 0)) {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
  }
  if ((local_a8 & 1) != 0) {
    _ZdlPv((void *)CONCAT62(uStack_96,CONCAT11(uStack_97,cStack_98)));
  }
  if ((local_90 & 1) != 0) {
    _ZdlPv(local_80);
  }
  if (((DAT_00ca5038 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca5038), iVar4 != 0)) {
    DAT_00ca5008 = 0;
    DAT_00ca5000 = &DAT_00ca5008;
    DAT_00ca5028 = 0;
    DAT_00ca5030 = 0;
    DAT_00ca5020 = 0;
    DAT_00ca5010 = 0;
    DAT_00ca5018 = &DAT_00ca5020;
    __cxa_atexit(FUN_0047edf4,&DAT_00ca5000,&PTR_LOOP_00c63060);
    __cxa_guard_release(&DAT_00ca5038);
  }
  cStack_85 = 0;
  local_90 = 0x14;
  uStack_87 = 0x676e;
  local_a8 = 0x1a;
  uStack_8f = (undefined5)s_img016_png_002c0076._0_8_;
  uStack_8a = SUB82(s_img016_png_002c0076._0_8_,5);
  cStack_88 = SUB81(s_img016_png_002c0076._0_8_,7);
  cStack_9a = 0;
  local_a7 = _DAT_002a9e9a;
  uStack_a2._0_1_ = s_6_imgcut_002a9e9f[0];
  uStack_a2._1_1_ = s_6_imgcut_002a9e9f[1];
  uStack_a2._2_1_ = s_6_imgcut_002a9e9f[2];
  uStack_9f._0_1_ = s_6_imgcut_002a9e9f[3];
  uStack_9f._1_1_ = s_6_imgcut_002a9e9f[4];
  uStack_9f._2_1_ = s_6_imgcut_002a9e9f[5];
  uStack_9f._3_1_ = s_6_imgcut_002a9e9f[6];
  uStack_9f._4_1_ = s_6_imgcut_002a9e9f[7];
  FUN_006333b4(&local_70,&DAT_00ca5000,&local_90,&local_a8,0x2601);
  plVar7 = plStack_68;
  uVar2 = local_70;
  plVar6 = (long *)param_1[0x24];
  local_70 = 0;
  plStack_68 = (long *)0x0;
  param_1[0x24] = plVar7;
  param_1[0x23] = uVar2;
  if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00c53da0(0xffffffffffffffff,plVar6 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar6 + 0x10))(plVar6);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
  }
  plVar7 = plStack_68;
  if ((plStack_68 != (long *)0x0) &&
     (lVar5 = FUN_00c53da0(0xffffffffffffffff,plStack_68 + 1), lVar5 == 0)) {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
  }
  if ((local_a8 & 1) != 0) {
    _ZdlPv((void *)CONCAT62(uStack_96,CONCAT11(uStack_97,cStack_98)));
  }
  if ((local_90 & 1) != 0) {
    _ZdlPv(local_80);
  }
  if (((DAT_00ca5038 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca5038), iVar4 != 0)) {
    DAT_00ca5008 = 0;
    DAT_00ca5000 = &DAT_00ca5008;
    DAT_00ca5028 = 0;
    DAT_00ca5030 = 0;
    DAT_00ca5020 = 0;
    DAT_00ca5010 = 0;
    DAT_00ca5018 = &DAT_00ca5020;
    __cxa_atexit(FUN_0047edf4,&DAT_00ca5000,&PTR_LOOP_00c63060);
    __cxa_guard_release(&DAT_00ca5038);
  }
  cStack_85 = 0;
  local_90 = 0x14;
  uStack_87 = 0x676e;
  local_a8 = 0x1a;
  uStack_8f = (undefined5)s_img015_png_002b91bb._0_8_;
  uStack_8a = SUB82(s_img015_png_002b91bb._0_8_,5);
  cStack_88 = SUB81(s_img015_png_002b91bb._0_8_,7);
  cStack_9a = 0;
  local_a7 = _DAT_002bdbbb;
  uStack_a2._0_1_ = s_5_imgcut_002bdbc0[0];
  uStack_a2._1_1_ = s_5_imgcut_002bdbc0[1];
  uStack_a2._2_1_ = s_5_imgcut_002bdbc0[2];
  uStack_9f._0_1_ = s_5_imgcut_002bdbc0[3];
  uStack_9f._1_1_ = s_5_imgcut_002bdbc0[4];
  uStack_9f._2_1_ = s_5_imgcut_002bdbc0[5];
  uStack_9f._3_1_ = s_5_imgcut_002bdbc0[6];
  uStack_9f._4_1_ = s_5_imgcut_002bdbc0[7];
  FUN_006333b4(&local_70,&DAT_00ca5000,&local_90,&local_a8,0x2601);
  plVar7 = plStack_68;
  uVar2 = local_70;
  plVar6 = (long *)param_1[0x26];
  local_70 = 0;
  plStack_68 = (long *)0x0;
  param_1[0x26] = plVar7;
  param_1[0x25] = uVar2;
  if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00c53da0(0xffffffffffffffff,plVar6 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar6 + 0x10))(plVar6);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
  }
  plVar7 = plStack_68;
  if ((plStack_68 != (long *)0x0) &&
     (lVar5 = FUN_00c53da0(0xffffffffffffffff,plStack_68 + 1), lVar5 == 0)) {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
  }
  if ((local_a8 & 1) != 0) {
    _ZdlPv((void *)CONCAT62(uStack_96,CONCAT11(uStack_97,cStack_98)));
  }
  if ((local_90 & 1) != 0) {
    _ZdlPv(local_80);
  }
  if (((DAT_00ca5038 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca5038), iVar4 != 0)) {
    DAT_00ca5008 = 0;
    DAT_00ca5000 = &DAT_00ca5008;
    DAT_00ca5028 = 0;
    DAT_00ca5030 = 0;
    DAT_00ca5020 = 0;
    DAT_00ca5010 = 0;
    DAT_00ca5018 = &DAT_00ca5020;
    __cxa_atexit(FUN_0047edf4,&DAT_00ca5000,&PTR_LOOP_00c63060);
    __cxa_guard_release(&DAT_00ca5038);
  }
  cStack_85 = 0;
  local_90 = 0x14;
  uStack_87 = 0x676e;
  local_a8 = 0x1a;
  uStack_8f = (undefined5)s_img021_png_0029f1f3._0_8_;
  uStack_8a = SUB82(s_img021_png_0029f1f3._0_8_,5);
  cStack_88 = SUB81(s_img021_png_0029f1f3._0_8_,7);
  cStack_9a = 0;
  local_a7 = _DAT_002c13b3;
  uStack_a2._0_1_ = s_1_imgcut_002c13b8[0];
  uStack_a2._1_1_ = s_1_imgcut_002c13b8[1];
  uStack_a2._2_1_ = s_1_imgcut_002c13b8[2];
  uStack_9f._0_1_ = s_1_imgcut_002c13b8[3];
  uStack_9f._1_1_ = s_1_imgcut_002c13b8[4];
  uStack_9f._2_1_ = s_1_imgcut_002c13b8[5];
  uStack_9f._3_1_ = s_1_imgcut_002c13b8[6];
  uStack_9f._4_1_ = s_1_imgcut_002c13b8[7];
  FUN_006333b4(&local_70,&DAT_00ca5000,&local_90,&local_a8,0x2601);
  plVar7 = plStack_68;
  uVar2 = local_70;
  plVar6 = (long *)param_1[0x28];
  local_70 = 0;
  plStack_68 = (long *)0x0;
  param_1[0x28] = plVar7;
  param_1[0x27] = uVar2;
  if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00c53da0(0xffffffffffffffff,plVar6 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar6 + 0x10))(plVar6);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
  }
  plVar7 = plStack_68;
  if ((plStack_68 != (long *)0x0) &&
     (lVar5 = FUN_00c53da0(0xffffffffffffffff,plStack_68 + 1), lVar5 == 0)) {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
  }
  if ((local_a8 & 1) != 0) {
    _ZdlPv((void *)CONCAT62(uStack_96,CONCAT11(uStack_97,cStack_98)));
  }
  if ((local_90 & 1) != 0) {
    _ZdlPv(local_80);
  }
  if (((DAT_00ca5038 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca5038), iVar4 != 0)) {
    DAT_00ca5008 = 0;
    DAT_00ca5000 = &DAT_00ca5008;
    DAT_00ca5028 = 0;
    DAT_00ca5030 = 0;
    DAT_00ca5020 = 0;
    DAT_00ca5010 = 0;
    DAT_00ca5018 = &DAT_00ca5020;
    __cxa_atexit(FUN_0047edf4,&DAT_00ca5000,&PTR_LOOP_00c63060);
    __cxa_guard_release(&DAT_00ca5038);
  }
  cStack_85 = 0;
  local_90 = 0x14;
  uStack_87 = 0x676e;
  local_a8 = 0x1a;
  uStack_8f = (undefined5)s_img029_png_002b3eda._0_8_;
  uStack_8a = SUB82(s_img029_png_002b3eda._0_8_,5);
  cStack_88 = SUB81(s_img029_png_002b3eda._0_8_,7);
  cStack_9a = 0;
  local_a7 = _DAT_002b921c;
  uStack_a2._0_1_ = s_9_imgcut_002b9221[0];
  uStack_a2._1_1_ = s_9_imgcut_002b9221[1];
  uStack_a2._2_1_ = s_9_imgcut_002b9221[2];
  uStack_9f._0_1_ = s_9_imgcut_002b9221[3];
  uStack_9f._1_1_ = s_9_imgcut_002b9221[4];
  uStack_9f._2_1_ = s_9_imgcut_002b9221[5];
  uStack_9f._3_1_ = s_9_imgcut_002b9221[6];
  uStack_9f._4_1_ = s_9_imgcut_002b9221[7];
  FUN_006333b4(&local_70,&DAT_00ca5000,&local_90,&local_a8,0x2601);
  plVar7 = plStack_68;
  uVar2 = local_70;
  plVar6 = (long *)param_1[0x2a];
  local_70 = 0;
  plStack_68 = (long *)0x0;
  param_1[0x2a] = plVar7;
  param_1[0x29] = uVar2;
  if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00c53da0(0xffffffffffffffff,plVar6 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar6 + 0x10))(plVar6);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
  }
  plVar7 = plStack_68;
  if ((plStack_68 != (long *)0x0) &&
     (lVar5 = FUN_00c53da0(0xffffffffffffffff,plStack_68 + 1), lVar5 == 0)) {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
  }
  if ((local_a8 & 1) != 0) {
    _ZdlPv((void *)CONCAT62(uStack_96,CONCAT11(uStack_97,cStack_98)));
  }
  if ((local_90 & 1) != 0) {
    _ZdlPv(local_80);
  }
  FUN_00862ca8(&local_90,param_2);
  uVar3 = CONCAT17(uStack_81,
                   CONCAT16(uStack_82,
                            CONCAT24(uStack_84,CONCAT13(cStack_85,CONCAT21(uStack_87,cStack_88)))));
  uVar2 = CONCAT26(uStack_8a,CONCAT51(uStack_8f,local_90));
  plVar7 = (long *)param_1[0x36];
  local_90 = 0;
  uStack_8f = 0;
  uStack_8a = 0;
  cStack_88 = 0;
  uStack_87 = 0;
  cStack_85 = 0;
  uStack_84 = 0;
  uStack_82 = 0;
  uStack_81 = 0;
  param_1[0x36] = uVar3;
  param_1[0x35] = uVar2;
  if ((plVar7 != (long *)0x0) && (lVar5 = FUN_00c53da0(0xffffffffffffffff,plVar7 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
  }
  plVar7 = (long *)CONCAT17(uStack_81,
                            CONCAT16(uStack_82,
                                     CONCAT24(uStack_84,
                                              CONCAT13(cStack_85,CONCAT21(uStack_87,cStack_88)))));
  if ((plVar7 != (long *)0x0) && (lVar5 = FUN_00c53da0(0xffffffffffffffff,plVar7 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
  }
  if (((DAT_00ca5038 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca5038), iVar4 != 0)) {
    DAT_00ca5008 = 0;
    DAT_00ca5000 = &DAT_00ca5008;
    DAT_00ca5028 = 0;
    DAT_00ca5030 = 0;
    DAT_00ca5020 = 0;
    DAT_00ca5010 = 0;
    DAT_00ca5018 = &DAT_00ca5020;
    __cxa_atexit(FUN_0047edf4,&DAT_00ca5000,&PTR_LOOP_00c63060);
    __cxa_guard_release(&DAT_00ca5038);
  }
  cStack_85 = 0;
  local_90 = 0x14;
  uStack_87 = 0x676e;
  local_a8 = 0x1a;
  uStack_8f = (undefined5)s_img102_png_002a450a._0_8_;
  uStack_8a = SUB82(s_img102_png_002a450a._0_8_,5);
  cStack_88 = SUB81(s_img102_png_002a450a._0_8_,7);
  cStack_9a = 0;
  local_a7 = _DAT_002bdbc9;
  uStack_a2._0_1_ = s_2_imgcut_002bdbce[0];
  uStack_a2._1_1_ = s_2_imgcut_002bdbce[1];
  uStack_a2._2_1_ = s_2_imgcut_002bdbce[2];
  uStack_9f._0_1_ = s_2_imgcut_002bdbce[3];
  uStack_9f._1_1_ = s_2_imgcut_002bdbce[4];
  uStack_9f._2_1_ = s_2_imgcut_002bdbce[5];
  uStack_9f._3_1_ = s_2_imgcut_002bdbce[6];
  uStack_9f._4_1_ = s_2_imgcut_002bdbce[7];
  FUN_006333b4(&local_70,&DAT_00ca5000,&local_90,&local_a8,0x2601);
  plVar7 = plStack_68;
  uVar2 = local_70;
  plVar6 = (long *)param_1[0x3c];
  local_70 = 0;
  plStack_68 = (long *)0x0;
  param_1[0x3c] = plVar7;
  param_1[0x3b] = uVar2;
  if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00c53da0(0xffffffffffffffff,plVar6 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar6 + 0x10))(plVar6);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
  }
  plVar7 = plStack_68;
  if ((plStack_68 != (long *)0x0) &&
     (lVar5 = FUN_00c53da0(0xffffffffffffffff,plStack_68 + 1), lVar5 == 0)) {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
  }
  if ((local_a8 & 1) != 0) {
    _ZdlPv((void *)CONCAT62(uStack_96,CONCAT11(uStack_97,cStack_98)));
  }
  if ((local_90 & 1) != 0) {
    _ZdlPv(local_80);
  }
  if (((DAT_00ca5038 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca5038), iVar4 != 0)) {
    DAT_00ca5008 = 0;
    DAT_00ca5000 = &DAT_00ca5008;
    DAT_00ca5028 = 0;
    DAT_00ca5030 = 0;
    DAT_00ca5020 = 0;
    DAT_00ca5010 = 0;
    DAT_00ca5018 = &DAT_00ca5020;
    __cxa_atexit(FUN_0047edf4,&DAT_00ca5000,&PTR_LOOP_00c63060);
    __cxa_guard_release(&DAT_00ca5038);
  }
  local_90 = 0x1a;
  uStack_82 = 0;
  uStack_8f._0_1_ = s_img050_02_png_002a3471[0];
  uStack_8f._1_1_ = s_img050_02_png_002a3471[1];
  uStack_8f._2_1_ = s_img050_02_png_002a3471[2];
  uStack_8f._3_1_ = s_img050_02_png_002a3471[3];
  uStack_8f._4_1_ = s_img050_02_png_002a3471[4];
  uStack_8a = (undefined2)s_img050_02_png_002a3471._5_3_;
  cStack_88 = SUB31(s_img050_02_png_002a3471._5_3_,2);
  uStack_87 = (undefined2)s_img050_02_png_002a3471._8_5_;
  cStack_85 = SUB51(s_img050_02_png_002a3471._8_5_,2);
  uStack_84 = SUB52(s_img050_02_png_002a3471._8_5_,3);
  local_a8 = 0x20;
  uStack_97 = 0;
  uStack_9f = (undefined5)s_img050_02_imgcut_002c034b._8_8_;
  cStack_9a = SUB81(s_img050_02_imgcut_002c034b._8_8_,5);
  cStack_99 = SUB81(s_img050_02_imgcut_002c034b._8_8_,6);
  cStack_98 = SUB81(s_img050_02_imgcut_002c034b._8_8_,7);
  local_a7 = (undefined5)s_img050_02_imgcut_002c034b._0_8_;
  uStack_a2 = SUB83(s_img050_02_imgcut_002c034b._0_8_,5);
  FUN_006333b4(&local_70,&DAT_00ca5000,&local_90,&local_a8,0x2601);
  plVar7 = plStack_68;
  uVar2 = local_70;
  plVar6 = (long *)param_1[0x40];
  local_70 = 0;
  plStack_68 = (long *)0x0;
  param_1[0x40] = plVar7;
  param_1[0x3f] = uVar2;
  if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00c53da0(0xffffffffffffffff,plVar6 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar6 + 0x10))(plVar6);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
  }
  plVar7 = plStack_68;
  if ((plStack_68 != (long *)0x0) &&
     (lVar5 = FUN_00c53da0(0xffffffffffffffff,plStack_68 + 1), lVar5 == 0)) {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
  }
  if ((local_a8 & 1) != 0) {
    _ZdlPv((void *)CONCAT62(uStack_96,CONCAT11(uStack_97,cStack_98)));
  }
  if ((local_90 & 1) != 0) {
    _ZdlPv(local_80);
  }
  if (*(long *)(lVar1 + 0x28) != local_58) {
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
<a id="insn-008faedc"></a> `008faedc` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-008faee0"></a> `008faee0` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-008faee4"></a> `008faee4` | `f9 3b 00 f9` | str x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-008faee8"></a> `008faee8` | `f8 5f 08 a9` | stp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-008faeec"></a> `008faeec` | `f6 57 09 a9` | stp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-008faef0"></a> `008faef0` | `f4 4f 0a a9` | stp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-008faef4"></a> `008faef4` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-008faef8"></a> `008faef8` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-008faefc"></a> `008faefc` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-008faf00"></a> `008faf00` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-008faf04"></a> `008faf04` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-008faf08"></a> `008faf08` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-008faf0c"></a> `008faf0c` | `c7 74 f9 97` | bl 0x00758228 | `UNCONDITIONAL_CALL`
<a id="insn-008faf10"></a> `008faf10` | `48 1c 00 f0` | adrp x8,0xc85000 | `FALL_THROUGH`
<a id="insn-008faf14"></a> `008faf14` | `08 21 2f 91` | add x8,x8,#0xbc8 | `FALL_THROUGH`
<a id="insn-008faf18"></a> `008faf18` | `58 1d 00 f0` | adrp x24,0xca5000 | `FALL_THROUGH`
<a id="insn-008faf1c"></a> `008faf1c` | `18 e3 00 91` | add x24,x24,#0x38 | `FALL_THROUGH`
<a id="insn-008faf20"></a> `008faf20` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-008faf24"></a> `008faf24` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-008faf28"></a> `008faf28` | `68 c2 0b 39` | strb w8,[x19, #0x2f0] | `FALL_THROUGH`
<a id="insn-008faf2c"></a> `008faf2c` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008faf30"></a> `008faf30` | `c8 4b 00 36` | tbz w8,#0x0,0x008fb8a8 | `CONDITIONAL_JUMP`
<a id="insn-008faf34"></a> `008faf34` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-008faf38"></a> `008faf38` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-008faf3c"></a> `008faf3c` | `ff af 00 39` | strb wzr,[sp, #0x2b] | `FALL_THROUGH`
<a id="insn-008faf40"></a> `008faf40` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008faf44"></a> `008faf44` | `e8 cd ff 90` | adrp x8,0x2b6000 | `FALL_THROUGH`
<a id="insn-008faf48"></a> `008faf48` | `08 39 0f 91` | add x8,x8,#0x3ce | `FALL_THROUGH`
<a id="insn-008faf4c"></a> `008faf4c` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-008faf50"></a> `008faf50` | `e9 93 02 78` | sturh w9,[sp, #0x29] | `FALL_THROUGH`
<a id="insn-008faf54"></a> `008faf54` | `49 03 80 52` | mov w9,#0x1a | `FALL_THROUGH`
<a id="insn-008faf58"></a> `008faf58` | `e9 23 00 39` | strb w9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008faf5c"></a> `008faf5c` | `e8 13 02 f8` | stur x8,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-008faf60"></a> `008faf60` | `a8 cd ff f0` | adrp x8,0x2b1000 | `FALL_THROUGH`
<a id="insn-008faf64"></a> `008faf64` | `08 1d 3d 91` | add x8,x8,#0xf47 | `FALL_THROUGH`
<a id="insn-008faf68"></a> `008faf68` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-008faf6c"></a> `008faf6c` | `08 51 40 f8` | ldur x8,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-008faf70"></a> `008faf70` | `ff 5b 00 39` | strb wzr,[sp, #0x16] | `FALL_THROUGH`
<a id="insn-008faf74"></a> `008faf74` | `e9 93 00 f8` | stur x9,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-008faf78"></a> `008faf78` | `e8 e3 00 f8` | stur x8,[sp, #0xe] | `FALL_THROUGH`
<a id="insn-008faf7c"></a> `008faf7c` | `55 1d 00 f0` | adrp x21,0xca5000 | `FALL_THROUGH`
<a id="insn-008faf80"></a> `008faf80` | `b5 02 00 91` | add x21,x21,#0x0 | `FALL_THROUGH`
<a id="insn-008faf84"></a> `008faf84` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-008faf88"></a> `008faf88` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-008faf8c"></a> `008faf8c` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-008faf90"></a> `008faf90` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008faf94"></a> `008faf94` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-008faf98"></a> `008faf98` | `07 e1 f4 97` | bl 0x006333b4 | `UNCONDITIONAL_CALL`
<a id="insn-008faf9c"></a> `008faf9c` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fafa0"></a> `008fafa0` | `76 5a 40 f9` | ldr x22,[x19, #0xb0] | `FALL_THROUGH`
<a id="insn-008fafa4"></a> `008fafa4` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fafa8"></a> `008fafa8` | `60 82 8a 3c` | stur q0,[x19, #0xa8] | `FALL_THROUGH`
<a id="insn-008fafac"></a> `008fafac` | `76 01 00 b4` | cbz x22,0x008fafd8 | `CONDITIONAL_JUMP`
<a id="insn-008fafb0"></a> `008fafb0` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fafb4"></a> `008fafb4` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fafb8"></a> `008fafb8` | `7a 63 0d 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-008fafbc"></a> `008fafbc` | `e0 00 00 b5` | cbnz x0,0x008fafd8 | `CONDITIONAL_JUMP`
<a id="insn-008fafc0"></a> `008fafc0` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008fafc4"></a> `008fafc4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fafc8"></a> `008fafc8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fafcc"></a> `008fafcc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fafd0"></a> `008fafd0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fafd4"></a> `008fafd4` | `df 73 0d 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-008fafd8"></a> `008fafd8` | `b6 83 5e f8` | ldur x22,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-008fafdc"></a> `008fafdc` | `b6 00 00 b4` | cbz x22,0x008faff0 | `CONDITIONAL_JUMP`
<a id="insn-008fafe0"></a> `008fafe0` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fafe4"></a> `008fafe4` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fafe8"></a> `008fafe8` | `6e 63 0d 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-008fafec"></a> `008fafec` | `a0 0b 00 b4` | cbz x0,0x008fb160 | `CONDITIONAL_JUMP`
<a id="insn-008faff0"></a> `008faff0` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008faff4"></a> `008faff4` | `68 00 00 36` | tbz w8,#0x0,0x008fb000 | `CONDITIONAL_JUMP`
<a id="insn-008faff8"></a> `008faff8` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-008faffc"></a> `008faffc` | `e1 73 0d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb000"></a> `008fb000` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb004"></a> `008fb004` | `68 00 00 36` | tbz w8,#0x0,0x008fb010 | `CONDITIONAL_JUMP`
<a id="insn-008fb008"></a> `008fb008` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008fb00c"></a> `008fb00c` | `dd 73 0d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb010"></a> `008fb010` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-008fb014"></a> `008fb014` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-008fb018"></a> `008fb018` | `5e a5 fd 97` | bl 0x00864590 | `UNCONDITIONAL_CALL`
<a id="insn-008fb01c"></a> `008fb01c` | `e0 0b c0 3d` | ldr q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb020"></a> `008fb020` | `76 6a 40 f9` | ldr x22,[x19, #0xd0] | `FALL_THROUGH`
<a id="insn-008fb024"></a> `008fb024` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb028"></a> `008fb028` | `60 82 8c 3c` | stur q0,[x19, #0xc8] | `FALL_THROUGH`
<a id="insn-008fb02c"></a> `008fb02c` | `76 01 00 b4` | cbz x22,0x008fb058 | `CONDITIONAL_JUMP`
<a id="insn-008fb030"></a> `008fb030` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fb034"></a> `008fb034` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb038"></a> `008fb038` | `5a 63 0d 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb03c"></a> `008fb03c` | `e0 00 00 b5` | cbnz x0,0x008fb058 | `CONDITIONAL_JUMP`
<a id="insn-008fb040"></a> `008fb040` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008fb044"></a> `008fb044` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb048"></a> `008fb048` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb04c"></a> `008fb04c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb050"></a> `008fb050` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb054"></a> `008fb054` | `bf 73 0d 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb058"></a> `008fb058` | `f6 17 40 f9` | ldr x22,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-008fb05c"></a> `008fb05c` | `76 01 00 b4` | cbz x22,0x008fb088 | `CONDITIONAL_JUMP`
<a id="insn-008fb060"></a> `008fb060` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fb064"></a> `008fb064` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb068"></a> `008fb068` | `4e 63 0d 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb06c"></a> `008fb06c` | `e0 00 00 b5` | cbnz x0,0x008fb088 | `CONDITIONAL_JUMP`
<a id="insn-008fb070"></a> `008fb070` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008fb074"></a> `008fb074` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb078"></a> `008fb078` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb07c"></a> `008fb07c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb080"></a> `008fb080` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb084"></a> `008fb084` | `b3 73 0d 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb088"></a> `008fb088` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008fb08c"></a> `008fb08c` | `a8 43 00 36` | tbz w8,#0x0,0x008fb900 | `CONDITIONAL_JUMP`
<a id="insn-008fb090"></a> `008fb090` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-008fb094"></a> `008fb094` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-008fb098"></a> `008fb098` | `ff af 00 39` | strb wzr,[sp, #0x2b] | `FALL_THROUGH`
<a id="insn-008fb09c"></a> `008fb09c` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb0a0"></a> `008fb0a0` | `08 ce ff f0` | adrp x8,0x2be000 | `FALL_THROUGH`
<a id="insn-008fb0a4"></a> `008fb0a4` | `08 a9 3d 91` | add x8,x8,#0xf6a | `FALL_THROUGH`
<a id="insn-008fb0a8"></a> `008fb0a8` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-008fb0ac"></a> `008fb0ac` | `e9 93 02 78` | sturh w9,[sp, #0x29] | `FALL_THROUGH`
<a id="insn-008fb0b0"></a> `008fb0b0` | `49 03 80 52` | mov w9,#0x1a | `FALL_THROUGH`
<a id="insn-008fb0b4"></a> `008fb0b4` | `e9 23 00 39` | strb w9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb0b8"></a> `008fb0b8` | `e8 13 02 f8` | stur x8,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-008fb0bc"></a> `008fb0bc` | `68 cd ff d0` | adrp x8,0x2a9000 | `FALL_THROUGH`
<a id="insn-008fb0c0"></a> `008fb0c0` | `08 1d 3d 91` | add x8,x8,#0xf47 | `FALL_THROUGH`
<a id="insn-008fb0c4"></a> `008fb0c4` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-008fb0c8"></a> `008fb0c8` | `08 51 40 f8` | ldur x8,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-008fb0cc"></a> `008fb0cc` | `ff 5b 00 39` | strb wzr,[sp, #0x16] | `FALL_THROUGH`
<a id="insn-008fb0d0"></a> `008fb0d0` | `e9 93 00 f8` | stur x9,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-008fb0d4"></a> `008fb0d4` | `e8 e3 00 f8` | stur x8,[sp, #0xe] | `FALL_THROUGH`
<a id="insn-008fb0d8"></a> `008fb0d8` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-008fb0dc"></a> `008fb0dc` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-008fb0e0"></a> `008fb0e0` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-008fb0e4"></a> `008fb0e4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008fb0e8"></a> `008fb0e8` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-008fb0ec"></a> `008fb0ec` | `b2 e0 f4 97` | bl 0x006333b4 | `UNCONDITIONAL_CALL`
<a id="insn-008fb0f0"></a> `008fb0f0` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb0f4"></a> `008fb0f4` | `76 82 40 f9` | ldr x22,[x19, #0x100] | `FALL_THROUGH`
<a id="insn-008fb0f8"></a> `008fb0f8` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb0fc"></a> `008fb0fc` | `60 82 8f 3c` | stur q0,[x19, #0xf8] | `FALL_THROUGH`
<a id="insn-008fb100"></a> `008fb100` | `76 01 00 b4` | cbz x22,0x008fb12c | `CONDITIONAL_JUMP`
<a id="insn-008fb104"></a> `008fb104` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fb108"></a> `008fb108` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb10c"></a> `008fb10c` | `25 63 0d 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb110"></a> `008fb110` | `e0 00 00 b5` | cbnz x0,0x008fb12c | `CONDITIONAL_JUMP`
<a id="insn-008fb114"></a> `008fb114` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008fb118"></a> `008fb118` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb11c"></a> `008fb11c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb120"></a> `008fb120` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb124"></a> `008fb124` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb128"></a> `008fb128` | `8a 73 0d 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb12c"></a> `008fb12c` | `b6 83 5e f8` | ldur x22,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-008fb130"></a> `008fb130` | `b6 00 00 b4` | cbz x22,0x008fb144 | `CONDITIONAL_JUMP`
<a id="insn-008fb134"></a> `008fb134` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fb138"></a> `008fb138` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb13c"></a> `008fb13c` | `19 63 0d 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb140"></a> `008fb140` | `20 02 00 b4` | cbz x0,0x008fb184 | `CONDITIONAL_JUMP`
<a id="insn-008fb144"></a> `008fb144` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb148"></a> `008fb148` | `e8 02 00 37` | tbnz w8,#0x0,0x008fb1a4 | `CONDITIONAL_JUMP`
<a id="insn-008fb14c"></a> `008fb14c` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb150"></a> `008fb150` | `28 03 00 37` | tbnz w8,#0x0,0x008fb1b4 | `CONDITIONAL_JUMP`
<a id="insn-008fb154"></a> `008fb154` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008fb158"></a> `008fb158` | `68 03 00 37` | tbnz w8,#0x0,0x008fb1c4 | `CONDITIONAL_JUMP`
<a id="insn-008fb15c"></a> `008fb15c` | `fe 01 00 14` | b 0x008fb954 | `UNCONDITIONAL_JUMP`
<a id="insn-008fb160"></a> `008fb160` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008fb164"></a> `008fb164` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb168"></a> `008fb168` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb16c"></a> `008fb16c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb170"></a> `008fb170` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb174"></a> `008fb174` | `77 73 0d 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb178"></a> `008fb178` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb17c"></a> `008fb17c` | `e8 f3 07 37` | tbnz w8,#0x0,0x008faff8 | `CONDITIONAL_JUMP`
<a id="insn-008fb180"></a> `008fb180` | `a0 ff ff 17` | b 0x008fb000 | `UNCONDITIONAL_JUMP`
<a id="insn-008fb184"></a> `008fb184` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008fb188"></a> `008fb188` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb18c"></a> `008fb18c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb190"></a> `008fb190` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb194"></a> `008fb194` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb198"></a> `008fb198` | `6e 73 0d 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb19c"></a> `008fb19c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb1a0"></a> `008fb1a0` | `68 fd 07 36` | tbz w8,#0x0,0x008fb14c | `CONDITIONAL_JUMP`
<a id="insn-008fb1a4"></a> `008fb1a4` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-008fb1a8"></a> `008fb1a8` | `76 73 0d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb1ac"></a> `008fb1ac` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb1b0"></a> `008fb1b0` | `28 fd 07 36` | tbz w8,#0x0,0x008fb154 | `CONDITIONAL_JUMP`
<a id="insn-008fb1b4"></a> `008fb1b4` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008fb1b8"></a> `008fb1b8` | `72 73 0d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb1bc"></a> `008fb1bc` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008fb1c0"></a> `008fb1c0` | `a8 3c 00 36` | tbz w8,#0x0,0x008fb954 | `CONDITIONAL_JUMP`
<a id="insn-008fb1c4"></a> `008fb1c4` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-008fb1c8"></a> `008fb1c8` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-008fb1cc"></a> `008fb1cc` | `ff af 00 39` | strb wzr,[sp, #0x2b] | `FALL_THROUGH`
<a id="insn-008fb1d0"></a> `008fb1d0` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb1d4"></a> `008fb1d4` | `28 ce ff b0` | adrp x8,0x2c0000 | `FALL_THROUGH`
<a id="insn-008fb1d8"></a> `008fb1d8` | `08 d9 01 91` | add x8,x8,#0x76 | `FALL_THROUGH`
<a id="insn-008fb1dc"></a> `008fb1dc` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-008fb1e0"></a> `008fb1e0` | `e9 93 02 78` | sturh w9,[sp, #0x29] | `FALL_THROUGH`
<a id="insn-008fb1e4"></a> `008fb1e4` | `49 03 80 52` | mov w9,#0x1a | `FALL_THROUGH`
<a id="insn-008fb1e8"></a> `008fb1e8` | `e9 23 00 39` | strb w9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb1ec"></a> `008fb1ec` | `e8 13 02 f8` | stur x8,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-008fb1f0"></a> `008fb1f0` | `68 cd ff d0` | adrp x8,0x2a9000 | `FALL_THROUGH`
<a id="insn-008fb1f4"></a> `008fb1f4` | `08 69 3a 91` | add x8,x8,#0xe9a | `FALL_THROUGH`
<a id="insn-008fb1f8"></a> `008fb1f8` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-008fb1fc"></a> `008fb1fc` | `08 51 40 f8` | ldur x8,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-008fb200"></a> `008fb200` | `ff 5b 00 39` | strb wzr,[sp, #0x16] | `FALL_THROUGH`
<a id="insn-008fb204"></a> `008fb204` | `e9 93 00 f8` | stur x9,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-008fb208"></a> `008fb208` | `e8 e3 00 f8` | stur x8,[sp, #0xe] | `FALL_THROUGH`
<a id="insn-008fb20c"></a> `008fb20c` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-008fb210"></a> `008fb210` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-008fb214"></a> `008fb214` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-008fb218"></a> `008fb218` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008fb21c"></a> `008fb21c` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-008fb220"></a> `008fb220` | `65 e0 f4 97` | bl 0x006333b4 | `UNCONDITIONAL_CALL`
<a id="insn-008fb224"></a> `008fb224` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb228"></a> `008fb228` | `76 92 40 f9` | ldr x22,[x19, #0x120] | `FALL_THROUGH`
<a id="insn-008fb22c"></a> `008fb22c` | `79 62 04 91` | add x25,x19,#0x118 | `FALL_THROUGH`
<a id="insn-008fb230"></a> `008fb230` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb234"></a> `008fb234` | `20 03 80 3d` | str q0,[x25] | `FALL_THROUGH`
<a id="insn-008fb238"></a> `008fb238` | `76 01 00 b4` | cbz x22,0x008fb264 | `CONDITIONAL_JUMP`
<a id="insn-008fb23c"></a> `008fb23c` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fb240"></a> `008fb240` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb244"></a> `008fb244` | `d7 62 0d 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb248"></a> `008fb248` | `e0 00 00 b5` | cbnz x0,0x008fb264 | `CONDITIONAL_JUMP`
<a id="insn-008fb24c"></a> `008fb24c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008fb250"></a> `008fb250` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb254"></a> `008fb254` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb258"></a> `008fb258` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb25c"></a> `008fb25c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb260"></a> `008fb260` | `3c 73 0d 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb264"></a> `008fb264` | `b6 83 5e f8` | ldur x22,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-008fb268"></a> `008fb268` | `b6 00 00 b4` | cbz x22,0x008fb27c | `CONDITIONAL_JUMP`
<a id="insn-008fb26c"></a> `008fb26c` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fb270"></a> `008fb270` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb274"></a> `008fb274` | `cb 62 0d 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb278"></a> `008fb278` | `00 01 00 b4` | cbz x0,0x008fb298 | `CONDITIONAL_JUMP`
<a id="insn-008fb27c"></a> `008fb27c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb280"></a> `008fb280` | `c8 01 00 37` | tbnz w8,#0x0,0x008fb2b8 | `CONDITIONAL_JUMP`
<a id="insn-008fb284"></a> `008fb284` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb288"></a> `008fb288` | `08 02 00 37` | tbnz w8,#0x0,0x008fb2c8 | `CONDITIONAL_JUMP`
<a id="insn-008fb28c"></a> `008fb28c` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008fb290"></a> `008fb290` | `48 02 00 37` | tbnz w8,#0x0,0x008fb2d8 | `CONDITIONAL_JUMP`
<a id="insn-008fb294"></a> `008fb294` | `c5 01 00 14` | b 0x008fb9a8 | `UNCONDITIONAL_JUMP`
<a id="insn-008fb298"></a> `008fb298` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008fb29c"></a> `008fb29c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb2a0"></a> `008fb2a0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb2a4"></a> `008fb2a4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb2a8"></a> `008fb2a8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb2ac"></a> `008fb2ac` | `29 73 0d 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb2b0"></a> `008fb2b0` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb2b4"></a> `008fb2b4` | `88 fe 07 36` | tbz w8,#0x0,0x008fb284 | `CONDITIONAL_JUMP`
<a id="insn-008fb2b8"></a> `008fb2b8` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-008fb2bc"></a> `008fb2bc` | `31 73 0d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb2c0"></a> `008fb2c0` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb2c4"></a> `008fb2c4` | `48 fe 07 36` | tbz w8,#0x0,0x008fb28c | `CONDITIONAL_JUMP`
<a id="insn-008fb2c8"></a> `008fb2c8` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008fb2cc"></a> `008fb2cc` | `2d 73 0d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb2d0"></a> `008fb2d0` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008fb2d4"></a> `008fb2d4` | `a8 36 00 36` | tbz w8,#0x0,0x008fb9a8 | `CONDITIONAL_JUMP`
<a id="insn-008fb2d8"></a> `008fb2d8` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-008fb2dc"></a> `008fb2dc` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-008fb2e0"></a> `008fb2e0` | `ff af 00 39` | strb wzr,[sp, #0x2b] | `FALL_THROUGH`
<a id="insn-008fb2e4"></a> `008fb2e4` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb2e8"></a> `008fb2e8` | `e8 cd ff d0` | adrp x8,0x2b9000 | `FALL_THROUGH`
<a id="insn-008fb2ec"></a> `008fb2ec` | `08 ed 06 91` | add x8,x8,#0x1bb | `FALL_THROUGH`
<a id="insn-008fb2f0"></a> `008fb2f0` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-008fb2f4"></a> `008fb2f4` | `e9 93 02 78` | sturh w9,[sp, #0x29] | `FALL_THROUGH`
<a id="insn-008fb2f8"></a> `008fb2f8` | `49 03 80 52` | mov w9,#0x1a | `FALL_THROUGH`
<a id="insn-008fb2fc"></a> `008fb2fc` | `e9 23 00 39` | strb w9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb300"></a> `008fb300` | `e8 13 02 f8` | stur x8,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-008fb304"></a> `008fb304` | `08 ce ff d0` | adrp x8,0x2bd000 | `FALL_THROUGH`
<a id="insn-008fb308"></a> `008fb308` | `08 ed 2e 91` | add x8,x8,#0xbbb | `FALL_THROUGH`
<a id="insn-008fb30c"></a> `008fb30c` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-008fb310"></a> `008fb310` | `08 51 40 f8` | ldur x8,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-008fb314"></a> `008fb314` | `ff 5b 00 39` | strb wzr,[sp, #0x16] | `FALL_THROUGH`
<a id="insn-008fb318"></a> `008fb318` | `e9 93 00 f8` | stur x9,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-008fb31c"></a> `008fb31c` | `e8 e3 00 f8` | stur x8,[sp, #0xe] | `FALL_THROUGH`
<a id="insn-008fb320"></a> `008fb320` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-008fb324"></a> `008fb324` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-008fb328"></a> `008fb328` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-008fb32c"></a> `008fb32c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008fb330"></a> `008fb330` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-008fb334"></a> `008fb334` | `20 e0 f4 97` | bl 0x006333b4 | `UNCONDITIONAL_CALL`
<a id="insn-008fb338"></a> `008fb338` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb33c"></a> `008fb33c` | `76 9a 40 f9` | ldr x22,[x19, #0x130] | `FALL_THROUGH`
<a id="insn-008fb340"></a> `008fb340` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb344"></a> `008fb344` | `20 07 80 3d` | str q0,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-008fb348"></a> `008fb348` | `76 01 00 b4` | cbz x22,0x008fb374 | `CONDITIONAL_JUMP`
<a id="insn-008fb34c"></a> `008fb34c` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fb350"></a> `008fb350` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb354"></a> `008fb354` | `93 62 0d 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb358"></a> `008fb358` | `e0 00 00 b5` | cbnz x0,0x008fb374 | `CONDITIONAL_JUMP`
<a id="insn-008fb35c"></a> `008fb35c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008fb360"></a> `008fb360` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb364"></a> `008fb364` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb368"></a> `008fb368` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb36c"></a> `008fb36c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb370"></a> `008fb370` | `f8 72 0d 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb374"></a> `008fb374` | `b6 83 5e f8` | ldur x22,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-008fb378"></a> `008fb378` | `b6 00 00 b4` | cbz x22,0x008fb38c | `CONDITIONAL_JUMP`
<a id="insn-008fb37c"></a> `008fb37c` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fb380"></a> `008fb380` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb384"></a> `008fb384` | `87 62 0d 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb388"></a> `008fb388` | `00 01 00 b4` | cbz x0,0x008fb3a8 | `CONDITIONAL_JUMP`
<a id="insn-008fb38c"></a> `008fb38c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb390"></a> `008fb390` | `c8 01 00 37` | tbnz w8,#0x0,0x008fb3c8 | `CONDITIONAL_JUMP`
<a id="insn-008fb394"></a> `008fb394` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb398"></a> `008fb398` | `08 02 00 37` | tbnz w8,#0x0,0x008fb3d8 | `CONDITIONAL_JUMP`
<a id="insn-008fb39c"></a> `008fb39c` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008fb3a0"></a> `008fb3a0` | `48 02 00 37` | tbnz w8,#0x0,0x008fb3e8 | `CONDITIONAL_JUMP`
<a id="insn-008fb3a4"></a> `008fb3a4` | `96 01 00 14` | b 0x008fb9fc | `UNCONDITIONAL_JUMP`
<a id="insn-008fb3a8"></a> `008fb3a8` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008fb3ac"></a> `008fb3ac` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb3b0"></a> `008fb3b0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb3b4"></a> `008fb3b4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb3b8"></a> `008fb3b8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb3bc"></a> `008fb3bc` | `e5 72 0d 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb3c0"></a> `008fb3c0` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb3c4"></a> `008fb3c4` | `88 fe 07 36` | tbz w8,#0x0,0x008fb394 | `CONDITIONAL_JUMP`
<a id="insn-008fb3c8"></a> `008fb3c8` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-008fb3cc"></a> `008fb3cc` | `ed 72 0d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb3d0"></a> `008fb3d0` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb3d4"></a> `008fb3d4` | `48 fe 07 36` | tbz w8,#0x0,0x008fb39c | `CONDITIONAL_JUMP`
<a id="insn-008fb3d8"></a> `008fb3d8` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008fb3dc"></a> `008fb3dc` | `e9 72 0d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb3e0"></a> `008fb3e0` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008fb3e4"></a> `008fb3e4` | `c8 30 00 36` | tbz w8,#0x0,0x008fb9fc | `CONDITIONAL_JUMP`
<a id="insn-008fb3e8"></a> `008fb3e8` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-008fb3ec"></a> `008fb3ec` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-008fb3f0"></a> `008fb3f0` | `ff af 00 39` | strb wzr,[sp, #0x2b] | `FALL_THROUGH`
<a id="insn-008fb3f4"></a> `008fb3f4` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb3f8"></a> `008fb3f8` | `28 cd ff 90` | adrp x8,0x29f000 | `FALL_THROUGH`
<a id="insn-008fb3fc"></a> `008fb3fc` | `08 cd 07 91` | add x8,x8,#0x1f3 | `FALL_THROUGH`
<a id="insn-008fb400"></a> `008fb400` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-008fb404"></a> `008fb404` | `e9 93 02 78` | sturh w9,[sp, #0x29] | `FALL_THROUGH`
<a id="insn-008fb408"></a> `008fb408` | `49 03 80 52` | mov w9,#0x1a | `FALL_THROUGH`
<a id="insn-008fb40c"></a> `008fb40c` | `e9 23 00 39` | strb w9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb410"></a> `008fb410` | `e8 13 02 f8` | stur x8,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-008fb414"></a> `008fb414` | `28 ce ff d0` | adrp x8,0x2c1000 | `FALL_THROUGH`
<a id="insn-008fb418"></a> `008fb418` | `08 cd 0e 91` | add x8,x8,#0x3b3 | `FALL_THROUGH`
<a id="insn-008fb41c"></a> `008fb41c` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-008fb420"></a> `008fb420` | `08 51 40 f8` | ldur x8,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-008fb424"></a> `008fb424` | `ff 5b 00 39` | strb wzr,[sp, #0x16] | `FALL_THROUGH`
<a id="insn-008fb428"></a> `008fb428` | `e9 93 00 f8` | stur x9,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-008fb42c"></a> `008fb42c` | `e8 e3 00 f8` | stur x8,[sp, #0xe] | `FALL_THROUGH`
<a id="insn-008fb430"></a> `008fb430` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-008fb434"></a> `008fb434` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-008fb438"></a> `008fb438` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-008fb43c"></a> `008fb43c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008fb440"></a> `008fb440` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-008fb444"></a> `008fb444` | `dc df f4 97` | bl 0x006333b4 | `UNCONDITIONAL_CALL`
<a id="insn-008fb448"></a> `008fb448` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb44c"></a> `008fb44c` | `76 a2 40 f9` | ldr x22,[x19, #0x140] | `FALL_THROUGH`
<a id="insn-008fb450"></a> `008fb450` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb454"></a> `008fb454` | `20 0b 80 3d` | str q0,[x25, #0x20] | `FALL_THROUGH`
<a id="insn-008fb458"></a> `008fb458` | `76 01 00 b4` | cbz x22,0x008fb484 | `CONDITIONAL_JUMP`
<a id="insn-008fb45c"></a> `008fb45c` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fb460"></a> `008fb460` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb464"></a> `008fb464` | `4f 62 0d 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb468"></a> `008fb468` | `e0 00 00 b5` | cbnz x0,0x008fb484 | `CONDITIONAL_JUMP`
<a id="insn-008fb46c"></a> `008fb46c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008fb470"></a> `008fb470` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb474"></a> `008fb474` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb478"></a> `008fb478` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb47c"></a> `008fb47c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb480"></a> `008fb480` | `b4 72 0d 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb484"></a> `008fb484` | `b6 83 5e f8` | ldur x22,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-008fb488"></a> `008fb488` | `b6 00 00 b4` | cbz x22,0x008fb49c | `CONDITIONAL_JUMP`
<a id="insn-008fb48c"></a> `008fb48c` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fb490"></a> `008fb490` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb494"></a> `008fb494` | `43 62 0d 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb498"></a> `008fb498` | `00 01 00 b4` | cbz x0,0x008fb4b8 | `CONDITIONAL_JUMP`
<a id="insn-008fb49c"></a> `008fb49c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb4a0"></a> `008fb4a0` | `c8 01 00 37` | tbnz w8,#0x0,0x008fb4d8 | `CONDITIONAL_JUMP`
<a id="insn-008fb4a4"></a> `008fb4a4` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb4a8"></a> `008fb4a8` | `08 02 00 37` | tbnz w8,#0x0,0x008fb4e8 | `CONDITIONAL_JUMP`
<a id="insn-008fb4ac"></a> `008fb4ac` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008fb4b0"></a> `008fb4b0` | `48 02 00 37` | tbnz w8,#0x0,0x008fb4f8 | `CONDITIONAL_JUMP`
<a id="insn-008fb4b4"></a> `008fb4b4` | `67 01 00 14` | b 0x008fba50 | `UNCONDITIONAL_JUMP`
<a id="insn-008fb4b8"></a> `008fb4b8` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008fb4bc"></a> `008fb4bc` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb4c0"></a> `008fb4c0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb4c4"></a> `008fb4c4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb4c8"></a> `008fb4c8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb4cc"></a> `008fb4cc` | `a1 72 0d 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb4d0"></a> `008fb4d0` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb4d4"></a> `008fb4d4` | `88 fe 07 36` | tbz w8,#0x0,0x008fb4a4 | `CONDITIONAL_JUMP`
<a id="insn-008fb4d8"></a> `008fb4d8` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-008fb4dc"></a> `008fb4dc` | `a9 72 0d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb4e0"></a> `008fb4e0` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb4e4"></a> `008fb4e4` | `48 fe 07 36` | tbz w8,#0x0,0x008fb4ac | `CONDITIONAL_JUMP`
<a id="insn-008fb4e8"></a> `008fb4e8` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008fb4ec"></a> `008fb4ec` | `a5 72 0d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb4f0"></a> `008fb4f0` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008fb4f4"></a> `008fb4f4` | `e8 2a 00 36` | tbz w8,#0x0,0x008fba50 | `CONDITIONAL_JUMP`
<a id="insn-008fb4f8"></a> `008fb4f8` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-008fb4fc"></a> `008fb4fc` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-008fb500"></a> `008fb500` | `ff af 00 39` | strb wzr,[sp, #0x2b] | `FALL_THROUGH`
<a id="insn-008fb504"></a> `008fb504` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb508"></a> `008fb508` | `c8 cd ff 90` | adrp x8,0x2b3000 | `FALL_THROUGH`
<a id="insn-008fb50c"></a> `008fb50c` | `08 69 3b 91` | add x8,x8,#0xeda | `FALL_THROUGH`
<a id="insn-008fb510"></a> `008fb510` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-008fb514"></a> `008fb514` | `e9 93 02 78` | sturh w9,[sp, #0x29] | `FALL_THROUGH`
<a id="insn-008fb518"></a> `008fb518` | `49 03 80 52` | mov w9,#0x1a | `FALL_THROUGH`
<a id="insn-008fb51c"></a> `008fb51c` | `e9 23 00 39` | strb w9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb520"></a> `008fb520` | `e8 13 02 f8` | stur x8,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-008fb524"></a> `008fb524` | `e8 cd ff d0` | adrp x8,0x2b9000 | `FALL_THROUGH`
<a id="insn-008fb528"></a> `008fb528` | `08 71 08 91` | add x8,x8,#0x21c | `FALL_THROUGH`
<a id="insn-008fb52c"></a> `008fb52c` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-008fb530"></a> `008fb530` | `08 51 40 f8` | ldur x8,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-008fb534"></a> `008fb534` | `ff 5b 00 39` | strb wzr,[sp, #0x16] | `FALL_THROUGH`
<a id="insn-008fb538"></a> `008fb538` | `e9 93 00 f8` | stur x9,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-008fb53c"></a> `008fb53c` | `e8 e3 00 f8` | stur x8,[sp, #0xe] | `FALL_THROUGH`
<a id="insn-008fb540"></a> `008fb540` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-008fb544"></a> `008fb544` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-008fb548"></a> `008fb548` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-008fb54c"></a> `008fb54c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008fb550"></a> `008fb550` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-008fb554"></a> `008fb554` | `98 df f4 97` | bl 0x006333b4 | `UNCONDITIONAL_CALL`
<a id="insn-008fb558"></a> `008fb558` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb55c"></a> `008fb55c` | `76 aa 40 f9` | ldr x22,[x19, #0x150] | `FALL_THROUGH`
<a id="insn-008fb560"></a> `008fb560` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb564"></a> `008fb564` | `20 0f 80 3d` | str q0,[x25, #0x30] | `FALL_THROUGH`
<a id="insn-008fb568"></a> `008fb568` | `76 01 00 b4` | cbz x22,0x008fb594 | `CONDITIONAL_JUMP`
<a id="insn-008fb56c"></a> `008fb56c` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fb570"></a> `008fb570` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb574"></a> `008fb574` | `0b 62 0d 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb578"></a> `008fb578` | `e0 00 00 b5` | cbnz x0,0x008fb594 | `CONDITIONAL_JUMP`
<a id="insn-008fb57c"></a> `008fb57c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008fb580"></a> `008fb580` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb584"></a> `008fb584` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb588"></a> `008fb588` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb58c"></a> `008fb58c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb590"></a> `008fb590` | `70 72 0d 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb594"></a> `008fb594` | `b6 83 5e f8` | ldur x22,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-008fb598"></a> `008fb598` | `b6 00 00 b4` | cbz x22,0x008fb5ac | `CONDITIONAL_JUMP`
<a id="insn-008fb59c"></a> `008fb59c` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fb5a0"></a> `008fb5a0` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb5a4"></a> `008fb5a4` | `ff 61 0d 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb5a8"></a> `008fb5a8` | `e0 0b 00 b4` | cbz x0,0x008fb724 | `CONDITIONAL_JUMP`
<a id="insn-008fb5ac"></a> `008fb5ac` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb5b0"></a> `008fb5b0` | `68 00 00 36` | tbz w8,#0x0,0x008fb5bc | `CONDITIONAL_JUMP`
<a id="insn-008fb5b4"></a> `008fb5b4` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-008fb5b8"></a> `008fb5b8` | `72 72 0d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb5bc"></a> `008fb5bc` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb5c0"></a> `008fb5c0` | `68 00 00 36` | tbz w8,#0x0,0x008fb5cc | `CONDITIONAL_JUMP`
<a id="insn-008fb5c4"></a> `008fb5c4` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008fb5c8"></a> `008fb5c8` | `6e 72 0d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb5cc"></a> `008fb5cc` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-008fb5d0"></a> `008fb5d0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-008fb5d4"></a> `008fb5d4` | `b5 9d fd 97` | bl 0x00862ca8 | `UNCONDITIONAL_CALL`
<a id="insn-008fb5d8"></a> `008fb5d8` | `e0 0b c0 3d` | ldr q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb5dc"></a> `008fb5dc` | `74 da 40 f9` | ldr x20,[x19, #0x1b0] | `FALL_THROUGH`
<a id="insn-008fb5e0"></a> `008fb5e0` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb5e4"></a> `008fb5e4` | `20 27 80 3d` | str q0,[x25, #0x90] | `FALL_THROUGH`
<a id="insn-008fb5e8"></a> `008fb5e8` | `74 01 00 b4` | cbz x20,0x008fb614 | `CONDITIONAL_JUMP`
<a id="insn-008fb5ec"></a> `008fb5ec` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-008fb5f0"></a> `008fb5f0` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb5f4"></a> `008fb5f4` | `eb 61 0d 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb5f8"></a> `008fb5f8` | `e0 00 00 b5` | cbnz x0,0x008fb614 | `CONDITIONAL_JUMP`
<a id="insn-008fb5fc"></a> `008fb5fc` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-008fb600"></a> `008fb600` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-008fb604"></a> `008fb604` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb608"></a> `008fb608` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb60c"></a> `008fb60c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-008fb610"></a> `008fb610` | `50 72 0d 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb614"></a> `008fb614` | `f4 17 40 f9` | ldr x20,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-008fb618"></a> `008fb618` | `74 01 00 b4` | cbz x20,0x008fb644 | `CONDITIONAL_JUMP`
<a id="insn-008fb61c"></a> `008fb61c` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-008fb620"></a> `008fb620` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb624"></a> `008fb624` | `df 61 0d 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb628"></a> `008fb628` | `e0 00 00 b5` | cbnz x0,0x008fb644 | `CONDITIONAL_JUMP`
<a id="insn-008fb62c"></a> `008fb62c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-008fb630"></a> `008fb630` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-008fb634"></a> `008fb634` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb638"></a> `008fb638` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb63c"></a> `008fb63c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-008fb640"></a> `008fb640` | `44 72 0d 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb644"></a> `008fb644` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008fb648"></a> `008fb648` | `e8 22 00 36` | tbz w8,#0x0,0x008fbaa4 | `CONDITIONAL_JUMP`
<a id="insn-008fb64c"></a> `008fb64c` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-008fb650"></a> `008fb650` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-008fb654"></a> `008fb654` | `ff af 00 39` | strb wzr,[sp, #0x2b] | `FALL_THROUGH`
<a id="insn-008fb658"></a> `008fb658` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb65c"></a> `008fb65c` | `48 cd ff b0` | adrp x8,0x2a4000 | `FALL_THROUGH`
<a id="insn-008fb660"></a> `008fb660` | `08 29 14 91` | add x8,x8,#0x50a | `FALL_THROUGH`
<a id="insn-008fb664"></a> `008fb664` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-008fb668"></a> `008fb668` | `e9 93 02 78` | sturh w9,[sp, #0x29] | `FALL_THROUGH`
<a id="insn-008fb66c"></a> `008fb66c` | `49 03 80 52` | mov w9,#0x1a | `FALL_THROUGH`
<a id="insn-008fb670"></a> `008fb670` | `e9 23 00 39` | strb w9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb674"></a> `008fb674` | `e8 13 02 f8` | stur x8,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-008fb678"></a> `008fb678` | `08 ce ff d0` | adrp x8,0x2bd000 | `FALL_THROUGH`
<a id="insn-008fb67c"></a> `008fb67c` | `08 25 2f 91` | add x8,x8,#0xbc9 | `FALL_THROUGH`
<a id="insn-008fb680"></a> `008fb680` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-008fb684"></a> `008fb684` | `08 51 40 f8` | ldur x8,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-008fb688"></a> `008fb688` | `ff 5b 00 39` | strb wzr,[sp, #0x16] | `FALL_THROUGH`
<a id="insn-008fb68c"></a> `008fb68c` | `e9 93 00 f8` | stur x9,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-008fb690"></a> `008fb690` | `e8 e3 00 f8` | stur x8,[sp, #0xe] | `FALL_THROUGH`
<a id="insn-008fb694"></a> `008fb694` | `54 1d 00 d0` | adrp x20,0xca5000 | `FALL_THROUGH`
<a id="insn-008fb698"></a> `008fb698` | `94 02 00 91` | add x20,x20,#0x0 | `FALL_THROUGH`
<a id="insn-008fb69c"></a> `008fb69c` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-008fb6a0"></a> `008fb6a0` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-008fb6a4"></a> `008fb6a4` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-008fb6a8"></a> `008fb6a8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-008fb6ac"></a> `008fb6ac` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-008fb6b0"></a> `008fb6b0` | `41 df f4 97` | bl 0x006333b4 | `UNCONDITIONAL_CALL`
<a id="insn-008fb6b4"></a> `008fb6b4` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb6b8"></a> `008fb6b8` | `75 f2 40 f9` | ldr x21,[x19, #0x1e0] | `FALL_THROUGH`
<a id="insn-008fb6bc"></a> `008fb6bc` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb6c0"></a> `008fb6c0` | `20 33 80 3d` | str q0,[x25, #0xc0] | `FALL_THROUGH`
<a id="insn-008fb6c4"></a> `008fb6c4` | `75 01 00 b4` | cbz x21,0x008fb6f0 | `CONDITIONAL_JUMP`
<a id="insn-008fb6c8"></a> `008fb6c8` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-008fb6cc"></a> `008fb6cc` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb6d0"></a> `008fb6d0` | `b4 61 0d 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb6d4"></a> `008fb6d4` | `e0 00 00 b5` | cbnz x0,0x008fb6f0 | `CONDITIONAL_JUMP`
<a id="insn-008fb6d8"></a> `008fb6d8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-008fb6dc"></a> `008fb6dc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008fb6e0"></a> `008fb6e0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb6e4"></a> `008fb6e4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb6e8"></a> `008fb6e8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008fb6ec"></a> `008fb6ec` | `19 72 0d 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb6f0"></a> `008fb6f0` | `b5 83 5e f8` | ldur x21,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-008fb6f4"></a> `008fb6f4` | `b5 00 00 b4` | cbz x21,0x008fb708 | `CONDITIONAL_JUMP`
<a id="insn-008fb6f8"></a> `008fb6f8` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-008fb6fc"></a> `008fb6fc` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb700"></a> `008fb700` | `a8 61 0d 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb704"></a> `008fb704` | `20 02 00 b4` | cbz x0,0x008fb748 | `CONDITIONAL_JUMP`
<a id="insn-008fb708"></a> `008fb708` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb70c"></a> `008fb70c` | `e8 02 00 37` | tbnz w8,#0x0,0x008fb768 | `CONDITIONAL_JUMP`
<a id="insn-008fb710"></a> `008fb710` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb714"></a> `008fb714` | `28 03 00 37` | tbnz w8,#0x0,0x008fb778 | `CONDITIONAL_JUMP`
<a id="insn-008fb718"></a> `008fb718` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008fb71c"></a> `008fb71c` | `68 03 00 37` | tbnz w8,#0x0,0x008fb788 | `CONDITIONAL_JUMP`
<a id="insn-008fb720"></a> `008fb720` | `f6 00 00 14` | b 0x008fbaf8 | `UNCONDITIONAL_JUMP`
<a id="insn-008fb724"></a> `008fb724` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008fb728"></a> `008fb728` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb72c"></a> `008fb72c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb730"></a> `008fb730` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb734"></a> `008fb734` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb738"></a> `008fb738` | `06 72 0d 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb73c"></a> `008fb73c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb740"></a> `008fb740` | `a8 f3 07 37` | tbnz w8,#0x0,0x008fb5b4 | `CONDITIONAL_JUMP`
<a id="insn-008fb744"></a> `008fb744` | `9e ff ff 17` | b 0x008fb5bc | `UNCONDITIONAL_JUMP`
<a id="insn-008fb748"></a> `008fb748` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-008fb74c"></a> `008fb74c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008fb750"></a> `008fb750` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb754"></a> `008fb754` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb758"></a> `008fb758` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008fb75c"></a> `008fb75c` | `fd 71 0d 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb760"></a> `008fb760` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb764"></a> `008fb764` | `68 fd 07 36` | tbz w8,#0x0,0x008fb710 | `CONDITIONAL_JUMP`
<a id="insn-008fb768"></a> `008fb768` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-008fb76c"></a> `008fb76c` | `05 72 0d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb770"></a> `008fb770` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb774"></a> `008fb774` | `28 fd 07 36` | tbz w8,#0x0,0x008fb718 | `CONDITIONAL_JUMP`
<a id="insn-008fb778"></a> `008fb778` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008fb77c"></a> `008fb77c` | `01 72 0d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb780"></a> `008fb780` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008fb784"></a> `008fb784` | `a8 1b 00 36` | tbz w8,#0x0,0x008fbaf8 | `CONDITIONAL_JUMP`
<a id="insn-008fb788"></a> `008fb788` | `49 cd ff 90` | adrp x9,0x2a3000 | `FALL_THROUGH`
<a id="insn-008fb78c"></a> `008fb78c` | `29 c5 11 91` | add x9,x9,#0x471 | `FALL_THROUGH`
<a id="insn-008fb790"></a> `008fb790` | `48 03 80 52` | mov w8,#0x1a | `FALL_THROUGH`
<a id="insn-008fb794"></a> `008fb794` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-008fb798"></a> `008fb798` | `29 51 40 f8` | ldur x9,[x9, #0x5] | `FALL_THROUGH`
<a id="insn-008fb79c"></a> `008fb79c` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb7a0"></a> `008fb7a0` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-008fb7a4"></a> `008fb7a4` | `ff bb 00 39` | strb wzr,[sp, #0x2e] | `FALL_THROUGH`
<a id="insn-008fb7a8"></a> `008fb7a8` | `ea 13 02 f8` | stur x10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-008fb7ac"></a> `008fb7ac` | `e9 63 02 f8` | stur x9,[sp, #0x26] | `FALL_THROUGH`
<a id="insn-008fb7b0"></a> `008fb7b0` | `29 ce ff b0` | adrp x9,0x2c0000 | `FALL_THROUGH`
<a id="insn-008fb7b4"></a> `008fb7b4` | `29 2d 0d 91` | add x9,x9,#0x34b | `FALL_THROUGH`
<a id="insn-008fb7b8"></a> `008fb7b8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-008fb7bc"></a> `008fb7bc` | `e8 23 00 39` | strb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb7c0"></a> `008fb7c0` | `ff 67 00 39` | strb wzr,[sp, #0x19] | `FALL_THROUGH`
<a id="insn-008fb7c4"></a> `008fb7c4` | `e0 93 80 3c` | stur q0,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-008fb7c8"></a> `008fb7c8` | `40 1d 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-008fb7cc"></a> `008fb7cc` | `00 00 00 91` | add x0,x0,#0x0 | `FALL_THROUGH`
<a id="insn-008fb7d0"></a> `008fb7d0` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-008fb7d4"></a> `008fb7d4` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-008fb7d8"></a> `008fb7d8` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-008fb7dc"></a> `008fb7dc` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-008fb7e0"></a> `008fb7e0` | `f5 de f4 97` | bl 0x006333b4 | `UNCONDITIONAL_CALL`
<a id="insn-008fb7e4"></a> `008fb7e4` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb7e8"></a> `008fb7e8` | `73 02 41 f9` | ldr x19,[x19, #0x200] | `FALL_THROUGH`
<a id="insn-008fb7ec"></a> `008fb7ec` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb7f0"></a> `008fb7f0` | `20 3b 80 3d` | str q0,[x25, #0xe0] | `FALL_THROUGH`
<a id="insn-008fb7f4"></a> `008fb7f4` | `73 01 00 b4` | cbz x19,0x008fb820 | `CONDITIONAL_JUMP`
<a id="insn-008fb7f8"></a> `008fb7f8` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-008fb7fc"></a> `008fb7fc` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb800"></a> `008fb800` | `68 61 0d 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb804"></a> `008fb804` | `e0 00 00 b5` | cbnz x0,0x008fb820 | `CONDITIONAL_JUMP`
<a id="insn-008fb808"></a> `008fb808` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-008fb80c"></a> `008fb80c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008fb810"></a> `008fb810` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb814"></a> `008fb814` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb818"></a> `008fb818` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008fb81c"></a> `008fb81c` | `cd 71 0d 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb820"></a> `008fb820` | `b3 83 5e f8` | ldur x19,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-008fb824"></a> `008fb824` | `b3 00 00 b4` | cbz x19,0x008fb838 | `CONDITIONAL_JUMP`
<a id="insn-008fb828"></a> `008fb828` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-008fb82c"></a> `008fb82c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb830"></a> `008fb830` | `5c 61 0d 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb834"></a> `008fb834` | `80 02 00 b4` | cbz x0,0x008fb884 | `CONDITIONAL_JUMP`
<a id="insn-008fb838"></a> `008fb838` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb83c"></a> `008fb83c` | `68 00 00 36` | tbz w8,#0x0,0x008fb848 | `CONDITIONAL_JUMP`
<a id="insn-008fb840"></a> `008fb840` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-008fb844"></a> `008fb844` | `cf 71 0d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb848"></a> `008fb848` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb84c"></a> `008fb84c` | `68 00 00 36` | tbz w8,#0x0,0x008fb858 | `CONDITIONAL_JUMP`
<a id="insn-008fb850"></a> `008fb850` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008fb854"></a> `008fb854` | `cb 71 0d 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb858"></a> `008fb858` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-008fb85c"></a> `008fb85c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-008fb860"></a> `008fb860` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-008fb864"></a> `008fb864` | `c1 1a 00 54` | b.ne 0x008fbbbc | `CONDITIONAL_JUMP`
<a id="insn-008fb868"></a> `008fb868` | `f4 4f 4a a9` | ldp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-008fb86c"></a> `008fb86c` | `f9 3b 40 f9` | ldr x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-008fb870"></a> `008fb870` | `f6 57 49 a9` | ldp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-008fb874"></a> `008fb874` | `f8 5f 48 a9` | ldp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-008fb878"></a> `008fb878` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-008fb87c"></a> `008fb87c` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-008fb880"></a> `008fb880` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-008fb884"></a> `008fb884` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-008fb888"></a> `008fb888` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008fb88c"></a> `008fb88c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb890"></a> `008fb890` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb894"></a> `008fb894` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008fb898"></a> `008fb898` | `ae 71 0d 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb89c"></a> `008fb89c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb8a0"></a> `008fb8a0` | `08 fd 07 37` | tbnz w8,#0x0,0x008fb840 | `CONDITIONAL_JUMP`
<a id="insn-008fb8a4"></a> `008fb8a4` | `e9 ff ff 17` | b 0x008fb848 | `UNCONDITIONAL_JUMP`
<a id="insn-008fb8a8"></a> `008fb8a8` | `40 1d 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-008fb8ac"></a> `008fb8ac` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-008fb8b0"></a> `008fb8b0` | `9c 71 0d 94` | bl 0x00c57f20 | `UNCONDITIONAL_CALL`
<a id="insn-008fb8b4"></a> `008fb8b4` | `00 b4 ff 34` | cbz w0,0x008faf34 | `CONDITIONAL_JUMP`
<a id="insn-008fb8b8"></a> `008fb8b8` | `41 1d 00 d0` | adrp x1,0xca5000 | `FALL_THROUGH`
<a id="insn-008fb8bc"></a> `008fb8bc` | `21 00 00 91` | add x1,x1,#0x0 | `FALL_THROUGH`
<a id="insn-008fb8c0"></a> `008fb8c0` | `00 dc ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-008fb8c4"></a> `008fb8c4` | `00 d0 37 91` | add x0,x0,#0xdf4 | `FALL_THROUGH`
<a id="insn-008fb8c8"></a> `008fb8c8` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-008fb8cc"></a> `008fb8cc` | `42 1b 00 90` | adrp x2,0xc63000 | `FALL_THROUGH`
<a id="insn-008fb8d0"></a> `008fb8d0` | `42 80 01 91` | add x2,x2,#0x60 | `FALL_THROUGH`
<a id="insn-008fb8d4"></a> `008fb8d4` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-008fb8d8"></a> `008fb8d8` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-008fb8dc"></a> `008fb8dc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-008fb8e0"></a> `008fb8e0` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-008fb8e4"></a> `008fb8e4` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-008fb8e8"></a> `008fb8e8` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-008fb8ec"></a> `008fb8ec` | `85 71 0d 94` | bl 0x00c57f00 | `UNCONDITIONAL_CALL`
<a id="insn-008fb8f0"></a> `008fb8f0` | `40 1d 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-008fb8f4"></a> `008fb8f4` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-008fb8f8"></a> `008fb8f8` | `92 71 0d 94` | bl 0x00c57f40 | `UNCONDITIONAL_CALL`
<a id="insn-008fb8fc"></a> `008fb8fc` | `8e fd ff 17` | b 0x008faf34 | `UNCONDITIONAL_JUMP`
<a id="insn-008fb900"></a> `008fb900` | `40 1d 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-008fb904"></a> `008fb904` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-008fb908"></a> `008fb908` | `86 71 0d 94` | bl 0x00c57f20 | `UNCONDITIONAL_CALL`
<a id="insn-008fb90c"></a> `008fb90c` | `20 bc ff 34` | cbz w0,0x008fb090 | `CONDITIONAL_JUMP`
<a id="insn-008fb910"></a> `008fb910` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-008fb914"></a> `008fb914` | `00 dc ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-008fb918"></a> `008fb918` | `00 d0 37 91` | add x0,x0,#0xdf4 | `FALL_THROUGH`
<a id="insn-008fb91c"></a> `008fb91c` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-008fb920"></a> `008fb920` | `42 1b 00 90` | adrp x2,0xc63000 | `FALL_THROUGH`
<a id="insn-008fb924"></a> `008fb924` | `42 80 01 91` | add x2,x2,#0x60 | `FALL_THROUGH`
<a id="insn-008fb928"></a> `008fb928` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-008fb92c"></a> `008fb92c` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-008fb930"></a> `008fb930` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-008fb934"></a> `008fb934` | `bf fe 02 a9` | stp xzr,xzr,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-008fb938"></a> `008fb938` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-008fb93c"></a> `008fb93c` | `bf 22 01 a9` | stp xzr,x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-008fb940"></a> `008fb940` | `70 71 0d 94` | bl 0x00c57f00 | `UNCONDITIONAL_CALL`
<a id="insn-008fb944"></a> `008fb944` | `40 1d 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-008fb948"></a> `008fb948` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-008fb94c"></a> `008fb94c` | `7d 71 0d 94` | bl 0x00c57f40 | `UNCONDITIONAL_CALL`
<a id="insn-008fb950"></a> `008fb950` | `d0 fd ff 17` | b 0x008fb090 | `UNCONDITIONAL_JUMP`
<a id="insn-008fb954"></a> `008fb954` | `40 1d 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-008fb958"></a> `008fb958` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-008fb95c"></a> `008fb95c` | `71 71 0d 94` | bl 0x00c57f20 | `UNCONDITIONAL_CALL`
<a id="insn-008fb960"></a> `008fb960` | `20 c3 ff 34` | cbz w0,0x008fb1c4 | `CONDITIONAL_JUMP`
<a id="insn-008fb964"></a> `008fb964` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-008fb968"></a> `008fb968` | `00 dc ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-008fb96c"></a> `008fb96c` | `00 d0 37 91` | add x0,x0,#0xdf4 | `FALL_THROUGH`
<a id="insn-008fb970"></a> `008fb970` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-008fb974"></a> `008fb974` | `42 1b 00 90` | adrp x2,0xc63000 | `FALL_THROUGH`
<a id="insn-008fb978"></a> `008fb978` | `42 80 01 91` | add x2,x2,#0x60 | `FALL_THROUGH`
<a id="insn-008fb97c"></a> `008fb97c` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-008fb980"></a> `008fb980` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-008fb984"></a> `008fb984` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-008fb988"></a> `008fb988` | `bf fe 02 a9` | stp xzr,xzr,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-008fb98c"></a> `008fb98c` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-008fb990"></a> `008fb990` | `bf 22 01 a9` | stp xzr,x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-008fb994"></a> `008fb994` | `5b 71 0d 94` | bl 0x00c57f00 | `UNCONDITIONAL_CALL`
<a id="insn-008fb998"></a> `008fb998` | `40 1d 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-008fb99c"></a> `008fb99c` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-008fb9a0"></a> `008fb9a0` | `68 71 0d 94` | bl 0x00c57f40 | `UNCONDITIONAL_CALL`
<a id="insn-008fb9a4"></a> `008fb9a4` | `08 fe ff 17` | b 0x008fb1c4 | `UNCONDITIONAL_JUMP`
<a id="insn-008fb9a8"></a> `008fb9a8` | `40 1d 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-008fb9ac"></a> `008fb9ac` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-008fb9b0"></a> `008fb9b0` | `5c 71 0d 94` | bl 0x00c57f20 | `UNCONDITIONAL_CALL`
<a id="insn-008fb9b4"></a> `008fb9b4` | `20 c9 ff 34` | cbz w0,0x008fb2d8 | `CONDITIONAL_JUMP`
<a id="insn-008fb9b8"></a> `008fb9b8` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-008fb9bc"></a> `008fb9bc` | `00 dc ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-008fb9c0"></a> `008fb9c0` | `00 d0 37 91` | add x0,x0,#0xdf4 | `FALL_THROUGH`
<a id="insn-008fb9c4"></a> `008fb9c4` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-008fb9c8"></a> `008fb9c8` | `42 1b 00 90` | adrp x2,0xc63000 | `FALL_THROUGH`
<a id="insn-008fb9cc"></a> `008fb9cc` | `42 80 01 91` | add x2,x2,#0x60 | `FALL_THROUGH`
<a id="insn-008fb9d0"></a> `008fb9d0` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-008fb9d4"></a> `008fb9d4` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-008fb9d8"></a> `008fb9d8` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-008fb9dc"></a> `008fb9dc` | `bf fe 02 a9` | stp xzr,xzr,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-008fb9e0"></a> `008fb9e0` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-008fb9e4"></a> `008fb9e4` | `bf 22 01 a9` | stp xzr,x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-008fb9e8"></a> `008fb9e8` | `46 71 0d 94` | bl 0x00c57f00 | `UNCONDITIONAL_CALL`
<a id="insn-008fb9ec"></a> `008fb9ec` | `40 1d 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-008fb9f0"></a> `008fb9f0` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-008fb9f4"></a> `008fb9f4` | `53 71 0d 94` | bl 0x00c57f40 | `UNCONDITIONAL_CALL`
<a id="insn-008fb9f8"></a> `008fb9f8` | `38 fe ff 17` | b 0x008fb2d8 | `UNCONDITIONAL_JUMP`
<a id="insn-008fb9fc"></a> `008fb9fc` | `40 1d 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-008fba00"></a> `008fba00` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-008fba04"></a> `008fba04` | `47 71 0d 94` | bl 0x00c57f20 | `UNCONDITIONAL_CALL`
<a id="insn-008fba08"></a> `008fba08` | `00 cf ff 34` | cbz w0,0x008fb3e8 | `CONDITIONAL_JUMP`
<a id="insn-008fba0c"></a> `008fba0c` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-008fba10"></a> `008fba10` | `00 dc ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-008fba14"></a> `008fba14` | `00 d0 37 91` | add x0,x0,#0xdf4 | `FALL_THROUGH`
<a id="insn-008fba18"></a> `008fba18` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-008fba1c"></a> `008fba1c` | `42 1b 00 90` | adrp x2,0xc63000 | `FALL_THROUGH`
<a id="insn-008fba20"></a> `008fba20` | `42 80 01 91` | add x2,x2,#0x60 | `FALL_THROUGH`
<a id="insn-008fba24"></a> `008fba24` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-008fba28"></a> `008fba28` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-008fba2c"></a> `008fba2c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-008fba30"></a> `008fba30` | `bf fe 02 a9` | stp xzr,xzr,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-008fba34"></a> `008fba34` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-008fba38"></a> `008fba38` | `bf 22 01 a9` | stp xzr,x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-008fba3c"></a> `008fba3c` | `31 71 0d 94` | bl 0x00c57f00 | `UNCONDITIONAL_CALL`
<a id="insn-008fba40"></a> `008fba40` | `40 1d 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-008fba44"></a> `008fba44` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-008fba48"></a> `008fba48` | `3e 71 0d 94` | bl 0x00c57f40 | `UNCONDITIONAL_CALL`
<a id="insn-008fba4c"></a> `008fba4c` | `67 fe ff 17` | b 0x008fb3e8 | `UNCONDITIONAL_JUMP`
<a id="insn-008fba50"></a> `008fba50` | `40 1d 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-008fba54"></a> `008fba54` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-008fba58"></a> `008fba58` | `32 71 0d 94` | bl 0x00c57f20 | `UNCONDITIONAL_CALL`
<a id="insn-008fba5c"></a> `008fba5c` | `e0 d4 ff 34` | cbz w0,0x008fb4f8 | `CONDITIONAL_JUMP`
<a id="insn-008fba60"></a> `008fba60` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-008fba64"></a> `008fba64` | `00 dc ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-008fba68"></a> `008fba68` | `00 d0 37 91` | add x0,x0,#0xdf4 | `FALL_THROUGH`
<a id="insn-008fba6c"></a> `008fba6c` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-008fba70"></a> `008fba70` | `42 1b 00 90` | adrp x2,0xc63000 | `FALL_THROUGH`
<a id="insn-008fba74"></a> `008fba74` | `42 80 01 91` | add x2,x2,#0x60 | `FALL_THROUGH`
<a id="insn-008fba78"></a> `008fba78` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-008fba7c"></a> `008fba7c` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-008fba80"></a> `008fba80` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-008fba84"></a> `008fba84` | `bf fe 02 a9` | stp xzr,xzr,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-008fba88"></a> `008fba88` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-008fba8c"></a> `008fba8c` | `bf 22 01 a9` | stp xzr,x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-008fba90"></a> `008fba90` | `1c 71 0d 94` | bl 0x00c57f00 | `UNCONDITIONAL_CALL`
<a id="insn-008fba94"></a> `008fba94` | `40 1d 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-008fba98"></a> `008fba98` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-008fba9c"></a> `008fba9c` | `29 71 0d 94` | bl 0x00c57f40 | `UNCONDITIONAL_CALL`
<a id="insn-008fbaa0"></a> `008fbaa0` | `96 fe ff 17` | b 0x008fb4f8 | `UNCONDITIONAL_JUMP`
<a id="insn-008fbaa4"></a> `008fbaa4` | `40 1d 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-008fbaa8"></a> `008fbaa8` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-008fbaac"></a> `008fbaac` | `1d 71 0d 94` | bl 0x00c57f20 | `UNCONDITIONAL_CALL`
<a id="insn-008fbab0"></a> `008fbab0` | `e0 dc ff 34` | cbz w0,0x008fb64c | `CONDITIONAL_JUMP`
<a id="insn-008fbab4"></a> `008fbab4` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-008fbab8"></a> `008fbab8` | `00 dc ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-008fbabc"></a> `008fbabc` | `00 d0 37 91` | add x0,x0,#0xdf4 | `FALL_THROUGH`
<a id="insn-008fbac0"></a> `008fbac0` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-008fbac4"></a> `008fbac4` | `42 1b 00 90` | adrp x2,0xc63000 | `FALL_THROUGH`
<a id="insn-008fbac8"></a> `008fbac8` | `42 80 01 91` | add x2,x2,#0x60 | `FALL_THROUGH`
<a id="insn-008fbacc"></a> `008fbacc` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-008fbad0"></a> `008fbad0` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-008fbad4"></a> `008fbad4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-008fbad8"></a> `008fbad8` | `bf fe 02 a9` | stp xzr,xzr,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-008fbadc"></a> `008fbadc` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-008fbae0"></a> `008fbae0` | `bf 22 01 a9` | stp xzr,x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-008fbae4"></a> `008fbae4` | `07 71 0d 94` | bl 0x00c57f00 | `UNCONDITIONAL_CALL`
<a id="insn-008fbae8"></a> `008fbae8` | `40 1d 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-008fbaec"></a> `008fbaec` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-008fbaf0"></a> `008fbaf0` | `14 71 0d 94` | bl 0x00c57f40 | `UNCONDITIONAL_CALL`
<a id="insn-008fbaf4"></a> `008fbaf4` | `d6 fe ff 17` | b 0x008fb64c | `UNCONDITIONAL_JUMP`
<a id="insn-008fbaf8"></a> `008fbaf8` | `40 1d 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-008fbafc"></a> `008fbafc` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-008fbb00"></a> `008fbb00` | `08 71 0d 94` | bl 0x00c57f20 | `UNCONDITIONAL_CALL`
<a id="insn-008fbb04"></a> `008fbb04` | `20 e4 ff 34` | cbz w0,0x008fb788 | `CONDITIONAL_JUMP`
<a id="insn-008fbb08"></a> `008fbb08` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-008fbb0c"></a> `008fbb0c` | `00 dc ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-008fbb10"></a> `008fbb10` | `00 d0 37 91` | add x0,x0,#0xdf4 | `FALL_THROUGH`
<a id="insn-008fbb14"></a> `008fbb14` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-008fbb18"></a> `008fbb18` | `42 1b 00 90` | adrp x2,0xc63000 | `FALL_THROUGH`
<a id="insn-008fbb1c"></a> `008fbb1c` | `42 80 01 91` | add x2,x2,#0x60 | `FALL_THROUGH`
<a id="insn-008fbb20"></a> `008fbb20` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-008fbb24"></a> `008fbb24` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-008fbb28"></a> `008fbb28` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-008fbb2c"></a> `008fbb2c` | `9f fe 02 a9` | stp xzr,xzr,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-008fbb30"></a> `008fbb30` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-008fbb34"></a> `008fbb34` | `9f 22 01 a9` | stp xzr,x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-008fbb38"></a> `008fbb38` | `f2 70 0d 94` | bl 0x00c57f00 | `UNCONDITIONAL_CALL`
<a id="insn-008fbb3c"></a> `008fbb3c` | `40 1d 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-008fbb40"></a> `008fbb40` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-008fbb44"></a> `008fbb44` | `ff 70 0d 94` | bl 0x00c57f40 | `UNCONDITIONAL_CALL`
<a id="insn-008fbb48"></a> `008fbb48` | `10 ff ff 17` | b 0x008fb788 | `UNCONDITIONAL_JUMP`
<a id="insn-008fbbbc"></a> `008fbbbc` | `fd 70 0d 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008faedc`](#insn-008faedc) 範囲 `[['008faedc', '008faee3']]`
  - `FALL_THROUGH` [`008faee0`](#insn-008faee0) → [`008faee4`](#insn-008faee4)
- ブロック [`008faee4`](#insn-008faee4) 範囲 `[['008faee4', '008faf33']]`
  - `CONDITIONAL_JUMP` [`008faf30`](#insn-008faf30) → [`008fb8a8`](#insn-008fb8a8)
  - `FALL_THROUGH` [`008faf30`](#insn-008faf30) → [`008faf34`](#insn-008faf34)
- ブロック [`008faf34`](#insn-008faf34) 範囲 `[['008faf34', '008faf93']]`
  - `FALL_THROUGH` [`008faf90`](#insn-008faf90) → [`008faf94`](#insn-008faf94)
- ブロック [`008faf94`](#insn-008faf94) 範囲 `[['008faf94', '008fafaf']]`
  - `CONDITIONAL_JUMP` [`008fafac`](#insn-008fafac) → [`008fafd8`](#insn-008fafd8)
  - `FALL_THROUGH` [`008fafac`](#insn-008fafac) → [`008fafb0`](#insn-008fafb0)
- ブロック [`008fafb0`](#insn-008fafb0) 範囲 `[['008fafb0', '008fafbf']]`
  - `CONDITIONAL_JUMP` [`008fafbc`](#insn-008fafbc) → [`008fafd8`](#insn-008fafd8)
  - `FALL_THROUGH` [`008fafbc`](#insn-008fafbc) → [`008fafc0`](#insn-008fafc0)
- ブロック [`008fafc0`](#insn-008fafc0) 範囲 `[['008fafc0', '008fafd7']]`
  - `FALL_THROUGH` [`008fafd4`](#insn-008fafd4) → [`008fafd8`](#insn-008fafd8)
- ブロック [`008fafd8`](#insn-008fafd8) 範囲 `[['008fafd8', '008fafdf']]`
  - `CONDITIONAL_JUMP` [`008fafdc`](#insn-008fafdc) → [`008faff0`](#insn-008faff0)
  - `FALL_THROUGH` [`008fafdc`](#insn-008fafdc) → [`008fafe0`](#insn-008fafe0)
- ブロック [`008fafe0`](#insn-008fafe0) 範囲 `[['008fafe0', '008fafef']]`
  - `CONDITIONAL_JUMP` [`008fafec`](#insn-008fafec) → [`008fb160`](#insn-008fb160)
  - `FALL_THROUGH` [`008fafec`](#insn-008fafec) → [`008faff0`](#insn-008faff0)
- ブロック [`008faff0`](#insn-008faff0) 範囲 `[['008faff0', '008faff7']]`
  - `CONDITIONAL_JUMP` [`008faff4`](#insn-008faff4) → [`008fb000`](#insn-008fb000)
  - `FALL_THROUGH` [`008faff4`](#insn-008faff4) → [`008faff8`](#insn-008faff8)
- ブロック [`008faff8`](#insn-008faff8) 範囲 `[['008faff8', '008fafff']]`
  - `FALL_THROUGH` [`008faffc`](#insn-008faffc) → [`008fb000`](#insn-008fb000)
- ブロック [`008fb000`](#insn-008fb000) 範囲 `[['008fb000', '008fb007']]`
  - `CONDITIONAL_JUMP` [`008fb004`](#insn-008fb004) → [`008fb010`](#insn-008fb010)
  - `FALL_THROUGH` [`008fb004`](#insn-008fb004) → [`008fb008`](#insn-008fb008)
- ブロック [`008fb008`](#insn-008fb008) 範囲 `[['008fb008', '008fb00f']]`
  - `FALL_THROUGH` [`008fb00c`](#insn-008fb00c) → [`008fb010`](#insn-008fb010)
- ブロック [`008fb010`](#insn-008fb010) 範囲 `[['008fb010', '008fb01b']]`
  - `FALL_THROUGH` [`008fb018`](#insn-008fb018) → [`008fb01c`](#insn-008fb01c)
- ブロック [`008fb01c`](#insn-008fb01c) 範囲 `[['008fb01c', '008fb02f']]`
  - `CONDITIONAL_JUMP` [`008fb02c`](#insn-008fb02c) → [`008fb058`](#insn-008fb058)
  - `FALL_THROUGH` [`008fb02c`](#insn-008fb02c) → [`008fb030`](#insn-008fb030)
- ブロック [`008fb030`](#insn-008fb030) 範囲 `[['008fb030', '008fb03f']]`
  - `CONDITIONAL_JUMP` [`008fb03c`](#insn-008fb03c) → [`008fb058`](#insn-008fb058)
  - `FALL_THROUGH` [`008fb03c`](#insn-008fb03c) → [`008fb040`](#insn-008fb040)
- ブロック [`008fb040`](#insn-008fb040) 範囲 `[['008fb040', '008fb057']]`
  - `FALL_THROUGH` [`008fb054`](#insn-008fb054) → [`008fb058`](#insn-008fb058)
- ブロック [`008fb058`](#insn-008fb058) 範囲 `[['008fb058', '008fb05f']]`
  - `CONDITIONAL_JUMP` [`008fb05c`](#insn-008fb05c) → [`008fb088`](#insn-008fb088)
  - `FALL_THROUGH` [`008fb05c`](#insn-008fb05c) → [`008fb060`](#insn-008fb060)
- ブロック [`008fb060`](#insn-008fb060) 範囲 `[['008fb060', '008fb06f']]`
  - `CONDITIONAL_JUMP` [`008fb06c`](#insn-008fb06c) → [`008fb088`](#insn-008fb088)
  - `FALL_THROUGH` [`008fb06c`](#insn-008fb06c) → [`008fb070`](#insn-008fb070)
- ブロック [`008fb070`](#insn-008fb070) 範囲 `[['008fb070', '008fb087']]`
  - `FALL_THROUGH` [`008fb084`](#insn-008fb084) → [`008fb088`](#insn-008fb088)
- ブロック [`008fb088`](#insn-008fb088) 範囲 `[['008fb088', '008fb08f']]`
  - `CONDITIONAL_JUMP` [`008fb08c`](#insn-008fb08c) → [`008fb900`](#insn-008fb900)
  - `FALL_THROUGH` [`008fb08c`](#insn-008fb08c) → [`008fb090`](#insn-008fb090)
- ブロック [`008fb090`](#insn-008fb090) 範囲 `[['008fb090', '008fb103']]`
  - `CONDITIONAL_JUMP` [`008fb100`](#insn-008fb100) → [`008fb12c`](#insn-008fb12c)
  - `FALL_THROUGH` [`008fb100`](#insn-008fb100) → [`008fb104`](#insn-008fb104)
- ブロック [`008fb104`](#insn-008fb104) 範囲 `[['008fb104', '008fb113']]`
  - `CONDITIONAL_JUMP` [`008fb110`](#insn-008fb110) → [`008fb12c`](#insn-008fb12c)
  - `FALL_THROUGH` [`008fb110`](#insn-008fb110) → [`008fb114`](#insn-008fb114)
- ブロック [`008fb114`](#insn-008fb114) 範囲 `[['008fb114', '008fb12b']]`
  - `FALL_THROUGH` [`008fb128`](#insn-008fb128) → [`008fb12c`](#insn-008fb12c)
- ブロック [`008fb12c`](#insn-008fb12c) 範囲 `[['008fb12c', '008fb133']]`
  - `CONDITIONAL_JUMP` [`008fb130`](#insn-008fb130) → [`008fb144`](#insn-008fb144)
  - `FALL_THROUGH` [`008fb130`](#insn-008fb130) → [`008fb134`](#insn-008fb134)
- ブロック [`008fb134`](#insn-008fb134) 範囲 `[['008fb134', '008fb13b']]`
  - `FALL_THROUGH` [`008fb138`](#insn-008fb138) → [`008fb13c`](#insn-008fb13c)
- ブロック [`008fb13c`](#insn-008fb13c) 範囲 `[['008fb13c', '008fb143']]`
  - `CONDITIONAL_JUMP` [`008fb140`](#insn-008fb140) → [`008fb184`](#insn-008fb184)
  - `FALL_THROUGH` [`008fb140`](#insn-008fb140) → [`008fb144`](#insn-008fb144)
- ブロック [`008fb144`](#insn-008fb144) 範囲 `[['008fb144', '008fb14b']]`
  - `CONDITIONAL_JUMP` [`008fb148`](#insn-008fb148) → [`008fb1a4`](#insn-008fb1a4)
  - `FALL_THROUGH` [`008fb148`](#insn-008fb148) → [`008fb14c`](#insn-008fb14c)
- ブロック [`008fb14c`](#insn-008fb14c) 範囲 `[['008fb14c', '008fb153']]`
  - `CONDITIONAL_JUMP` [`008fb150`](#insn-008fb150) → [`008fb1b4`](#insn-008fb1b4)
  - `FALL_THROUGH` [`008fb150`](#insn-008fb150) → [`008fb154`](#insn-008fb154)
- ブロック [`008fb154`](#insn-008fb154) 範囲 `[['008fb154', '008fb15b']]`
  - `CONDITIONAL_JUMP` [`008fb158`](#insn-008fb158) → [`008fb1c4`](#insn-008fb1c4)
  - `FALL_THROUGH` [`008fb158`](#insn-008fb158) → [`008fb15c`](#insn-008fb15c)
- ブロック [`008fb15c`](#insn-008fb15c) 範囲 `[['008fb15c', '008fb15f']]`
  - `UNCONDITIONAL_JUMP` [`008fb15c`](#insn-008fb15c) → [`008fb954`](#insn-008fb954)
- ブロック [`008fb160`](#insn-008fb160) 範囲 `[['008fb160', '008fb17f']]`
  - `CONDITIONAL_JUMP` [`008fb17c`](#insn-008fb17c) → [`008faff8`](#insn-008faff8)
  - `FALL_THROUGH` [`008fb17c`](#insn-008fb17c) → [`008fb180`](#insn-008fb180)
- ブロック [`008fb180`](#insn-008fb180) 範囲 `[['008fb180', '008fb183']]`
  - `UNCONDITIONAL_JUMP` [`008fb180`](#insn-008fb180) → [`008fb000`](#insn-008fb000)
- ブロック [`008fb184`](#insn-008fb184) 範囲 `[['008fb184', '008fb1a3']]`
  - `CONDITIONAL_JUMP` [`008fb1a0`](#insn-008fb1a0) → [`008fb14c`](#insn-008fb14c)
  - `FALL_THROUGH` [`008fb1a0`](#insn-008fb1a0) → [`008fb1a4`](#insn-008fb1a4)
- ブロック [`008fb1a4`](#insn-008fb1a4) 範囲 `[['008fb1a4', '008fb1b3']]`
  - `CONDITIONAL_JUMP` [`008fb1b0`](#insn-008fb1b0) → [`008fb154`](#insn-008fb154)
  - `FALL_THROUGH` [`008fb1b0`](#insn-008fb1b0) → [`008fb1b4`](#insn-008fb1b4)
- ブロック [`008fb1b4`](#insn-008fb1b4) 範囲 `[['008fb1b4', '008fb1c3']]`
  - `CONDITIONAL_JUMP` [`008fb1c0`](#insn-008fb1c0) → [`008fb954`](#insn-008fb954)
  - `FALL_THROUGH` [`008fb1c0`](#insn-008fb1c0) → [`008fb1c4`](#insn-008fb1c4)
- ブロック [`008fb1c4`](#insn-008fb1c4) 範囲 `[['008fb1c4', '008fb23b']]`
  - `CONDITIONAL_JUMP` [`008fb238`](#insn-008fb238) → [`008fb264`](#insn-008fb264)
  - `FALL_THROUGH` [`008fb238`](#insn-008fb238) → [`008fb23c`](#insn-008fb23c)
- ブロック [`008fb23c`](#insn-008fb23c) 範囲 `[['008fb23c', '008fb24b']]`
  - `CONDITIONAL_JUMP` [`008fb248`](#insn-008fb248) → [`008fb264`](#insn-008fb264)
  - `FALL_THROUGH` [`008fb248`](#insn-008fb248) → [`008fb24c`](#insn-008fb24c)
- ブロック [`008fb24c`](#insn-008fb24c) 範囲 `[['008fb24c', '008fb263']]`
  - `FALL_THROUGH` [`008fb260`](#insn-008fb260) → [`008fb264`](#insn-008fb264)
- ブロック [`008fb264`](#insn-008fb264) 範囲 `[['008fb264', '008fb26b']]`
  - `CONDITIONAL_JUMP` [`008fb268`](#insn-008fb268) → [`008fb27c`](#insn-008fb27c)
  - `FALL_THROUGH` [`008fb268`](#insn-008fb268) → [`008fb26c`](#insn-008fb26c)
- ブロック [`008fb26c`](#insn-008fb26c) 範囲 `[['008fb26c', '008fb27b']]`
  - `CONDITIONAL_JUMP` [`008fb278`](#insn-008fb278) → [`008fb298`](#insn-008fb298)
  - `FALL_THROUGH` [`008fb278`](#insn-008fb278) → [`008fb27c`](#insn-008fb27c)
- ブロック [`008fb27c`](#insn-008fb27c) 範囲 `[['008fb27c', '008fb283']]`
  - `CONDITIONAL_JUMP` [`008fb280`](#insn-008fb280) → [`008fb2b8`](#insn-008fb2b8)
  - `FALL_THROUGH` [`008fb280`](#insn-008fb280) → [`008fb284`](#insn-008fb284)
- ブロック [`008fb284`](#insn-008fb284) 範囲 `[['008fb284', '008fb28b']]`
  - `CONDITIONAL_JUMP` [`008fb288`](#insn-008fb288) → [`008fb2c8`](#insn-008fb2c8)
  - `FALL_THROUGH` [`008fb288`](#insn-008fb288) → [`008fb28c`](#insn-008fb28c)
- ブロック [`008fb28c`](#insn-008fb28c) 範囲 `[['008fb28c', '008fb293']]`
  - `CONDITIONAL_JUMP` [`008fb290`](#insn-008fb290) → [`008fb2d8`](#insn-008fb2d8)
  - `FALL_THROUGH` [`008fb290`](#insn-008fb290) → [`008fb294`](#insn-008fb294)
- ブロック [`008fb294`](#insn-008fb294) 範囲 `[['008fb294', '008fb297']]`
  - `UNCONDITIONAL_JUMP` [`008fb294`](#insn-008fb294) → [`008fb9a8`](#insn-008fb9a8)
- ブロック [`008fb298`](#insn-008fb298) 範囲 `[['008fb298', '008fb2b7']]`
  - `CONDITIONAL_JUMP` [`008fb2b4`](#insn-008fb2b4) → [`008fb284`](#insn-008fb284)
  - `FALL_THROUGH` [`008fb2b4`](#insn-008fb2b4) → [`008fb2b8`](#insn-008fb2b8)
- ブロック [`008fb2b8`](#insn-008fb2b8) 範囲 `[['008fb2b8', '008fb2c7']]`
  - `CONDITIONAL_JUMP` [`008fb2c4`](#insn-008fb2c4) → [`008fb28c`](#insn-008fb28c)
  - `FALL_THROUGH` [`008fb2c4`](#insn-008fb2c4) → [`008fb2c8`](#insn-008fb2c8)
- ブロック [`008fb2c8`](#insn-008fb2c8) 範囲 `[['008fb2c8', '008fb2d7']]`
  - `CONDITIONAL_JUMP` [`008fb2d4`](#insn-008fb2d4) → [`008fb9a8`](#insn-008fb9a8)
  - `FALL_THROUGH` [`008fb2d4`](#insn-008fb2d4) → [`008fb2d8`](#insn-008fb2d8)
- ブロック [`008fb2d8`](#insn-008fb2d8) 範囲 `[['008fb2d8', '008fb34b']]`
  - `CONDITIONAL_JUMP` [`008fb348`](#insn-008fb348) → [`008fb374`](#insn-008fb374)
  - `FALL_THROUGH` [`008fb348`](#insn-008fb348) → [`008fb34c`](#insn-008fb34c)
- ブロック [`008fb34c`](#insn-008fb34c) 範囲 `[['008fb34c', '008fb35b']]`
  - `CONDITIONAL_JUMP` [`008fb358`](#insn-008fb358) → [`008fb374`](#insn-008fb374)
  - `FALL_THROUGH` [`008fb358`](#insn-008fb358) → [`008fb35c`](#insn-008fb35c)
- ブロック [`008fb35c`](#insn-008fb35c) 範囲 `[['008fb35c', '008fb373']]`
  - `FALL_THROUGH` [`008fb370`](#insn-008fb370) → [`008fb374`](#insn-008fb374)
- ブロック [`008fb374`](#insn-008fb374) 範囲 `[['008fb374', '008fb37b']]`
  - `CONDITIONAL_JUMP` [`008fb378`](#insn-008fb378) → [`008fb38c`](#insn-008fb38c)
  - `FALL_THROUGH` [`008fb378`](#insn-008fb378) → [`008fb37c`](#insn-008fb37c)
- ブロック [`008fb37c`](#insn-008fb37c) 範囲 `[['008fb37c', '008fb38b']]`
  - `CONDITIONAL_JUMP` [`008fb388`](#insn-008fb388) → [`008fb3a8`](#insn-008fb3a8)
  - `FALL_THROUGH` [`008fb388`](#insn-008fb388) → [`008fb38c`](#insn-008fb38c)
- ブロック [`008fb38c`](#insn-008fb38c) 範囲 `[['008fb38c', '008fb393']]`
  - `CONDITIONAL_JUMP` [`008fb390`](#insn-008fb390) → [`008fb3c8`](#insn-008fb3c8)
  - `FALL_THROUGH` [`008fb390`](#insn-008fb390) → [`008fb394`](#insn-008fb394)
- ブロック [`008fb394`](#insn-008fb394) 範囲 `[['008fb394', '008fb39b']]`
  - `CONDITIONAL_JUMP` [`008fb398`](#insn-008fb398) → [`008fb3d8`](#insn-008fb3d8)
  - `FALL_THROUGH` [`008fb398`](#insn-008fb398) → [`008fb39c`](#insn-008fb39c)
- ブロック [`008fb39c`](#insn-008fb39c) 範囲 `[['008fb39c', '008fb3a3']]`
  - `CONDITIONAL_JUMP` [`008fb3a0`](#insn-008fb3a0) → [`008fb3e8`](#insn-008fb3e8)
  - `FALL_THROUGH` [`008fb3a0`](#insn-008fb3a0) → [`008fb3a4`](#insn-008fb3a4)
- ブロック [`008fb3a4`](#insn-008fb3a4) 範囲 `[['008fb3a4', '008fb3a7']]`
  - `UNCONDITIONAL_JUMP` [`008fb3a4`](#insn-008fb3a4) → [`008fb9fc`](#insn-008fb9fc)
- ブロック [`008fb3a8`](#insn-008fb3a8) 範囲 `[['008fb3a8', '008fb3c7']]`
  - `CONDITIONAL_JUMP` [`008fb3c4`](#insn-008fb3c4) → [`008fb394`](#insn-008fb394)
  - `FALL_THROUGH` [`008fb3c4`](#insn-008fb3c4) → [`008fb3c8`](#insn-008fb3c8)
- ブロック [`008fb3c8`](#insn-008fb3c8) 範囲 `[['008fb3c8', '008fb3d7']]`
  - `CONDITIONAL_JUMP` [`008fb3d4`](#insn-008fb3d4) → [`008fb39c`](#insn-008fb39c)
  - `FALL_THROUGH` [`008fb3d4`](#insn-008fb3d4) → [`008fb3d8`](#insn-008fb3d8)
- ブロック [`008fb3d8`](#insn-008fb3d8) 範囲 `[['008fb3d8', '008fb3e7']]`
  - `CONDITIONAL_JUMP` [`008fb3e4`](#insn-008fb3e4) → [`008fb9fc`](#insn-008fb9fc)
  - `FALL_THROUGH` [`008fb3e4`](#insn-008fb3e4) → [`008fb3e8`](#insn-008fb3e8)
- ブロック [`008fb3e8`](#insn-008fb3e8) 範囲 `[['008fb3e8', '008fb45b']]`
  - `CONDITIONAL_JUMP` [`008fb458`](#insn-008fb458) → [`008fb484`](#insn-008fb484)
  - `FALL_THROUGH` [`008fb458`](#insn-008fb458) → [`008fb45c`](#insn-008fb45c)
- ブロック [`008fb45c`](#insn-008fb45c) 範囲 `[['008fb45c', '008fb46b']]`
  - `CONDITIONAL_JUMP` [`008fb468`](#insn-008fb468) → [`008fb484`](#insn-008fb484)
  - `FALL_THROUGH` [`008fb468`](#insn-008fb468) → [`008fb46c`](#insn-008fb46c)
- ブロック [`008fb46c`](#insn-008fb46c) 範囲 `[['008fb46c', '008fb483']]`
  - `FALL_THROUGH` [`008fb480`](#insn-008fb480) → [`008fb484`](#insn-008fb484)
- ブロック [`008fb484`](#insn-008fb484) 範囲 `[['008fb484', '008fb48b']]`
  - `CONDITIONAL_JUMP` [`008fb488`](#insn-008fb488) → [`008fb49c`](#insn-008fb49c)
  - `FALL_THROUGH` [`008fb488`](#insn-008fb488) → [`008fb48c`](#insn-008fb48c)
- ブロック [`008fb48c`](#insn-008fb48c) 範囲 `[['008fb48c', '008fb49b']]`
  - `CONDITIONAL_JUMP` [`008fb498`](#insn-008fb498) → [`008fb4b8`](#insn-008fb4b8)
  - `FALL_THROUGH` [`008fb498`](#insn-008fb498) → [`008fb49c`](#insn-008fb49c)
- ブロック [`008fb49c`](#insn-008fb49c) 範囲 `[['008fb49c', '008fb4a3']]`
  - `CONDITIONAL_JUMP` [`008fb4a0`](#insn-008fb4a0) → [`008fb4d8`](#insn-008fb4d8)
  - `FALL_THROUGH` [`008fb4a0`](#insn-008fb4a0) → [`008fb4a4`](#insn-008fb4a4)
- ブロック [`008fb4a4`](#insn-008fb4a4) 範囲 `[['008fb4a4', '008fb4ab']]`
  - `CONDITIONAL_JUMP` [`008fb4a8`](#insn-008fb4a8) → [`008fb4e8`](#insn-008fb4e8)
  - `FALL_THROUGH` [`008fb4a8`](#insn-008fb4a8) → [`008fb4ac`](#insn-008fb4ac)
- ブロック [`008fb4ac`](#insn-008fb4ac) 範囲 `[['008fb4ac', '008fb4b3']]`
  - `CONDITIONAL_JUMP` [`008fb4b0`](#insn-008fb4b0) → [`008fb4f8`](#insn-008fb4f8)
  - `FALL_THROUGH` [`008fb4b0`](#insn-008fb4b0) → [`008fb4b4`](#insn-008fb4b4)
- ブロック [`008fb4b4`](#insn-008fb4b4) 範囲 `[['008fb4b4', '008fb4b7']]`
  - `UNCONDITIONAL_JUMP` [`008fb4b4`](#insn-008fb4b4) → [`008fba50`](#insn-008fba50)
- ブロック [`008fb4b8`](#insn-008fb4b8) 範囲 `[['008fb4b8', '008fb4d7']]`
  - `CONDITIONAL_JUMP` [`008fb4d4`](#insn-008fb4d4) → [`008fb4a4`](#insn-008fb4a4)
  - `FALL_THROUGH` [`008fb4d4`](#insn-008fb4d4) → [`008fb4d8`](#insn-008fb4d8)
- ブロック [`008fb4d8`](#insn-008fb4d8) 範囲 `[['008fb4d8', '008fb4e7']]`
  - `CONDITIONAL_JUMP` [`008fb4e4`](#insn-008fb4e4) → [`008fb4ac`](#insn-008fb4ac)
  - `FALL_THROUGH` [`008fb4e4`](#insn-008fb4e4) → [`008fb4e8`](#insn-008fb4e8)
- ブロック [`008fb4e8`](#insn-008fb4e8) 範囲 `[['008fb4e8', '008fb4f7']]`
  - `CONDITIONAL_JUMP` [`008fb4f4`](#insn-008fb4f4) → [`008fba50`](#insn-008fba50)
  - `FALL_THROUGH` [`008fb4f4`](#insn-008fb4f4) → [`008fb4f8`](#insn-008fb4f8)
- ブロック [`008fb4f8`](#insn-008fb4f8) 範囲 `[['008fb4f8', '008fb56b']]`
  - `CONDITIONAL_JUMP` [`008fb568`](#insn-008fb568) → [`008fb594`](#insn-008fb594)
  - `FALL_THROUGH` [`008fb568`](#insn-008fb568) → [`008fb56c`](#insn-008fb56c)
- ブロック [`008fb56c`](#insn-008fb56c) 範囲 `[['008fb56c', '008fb57b']]`
  - `CONDITIONAL_JUMP` [`008fb578`](#insn-008fb578) → [`008fb594`](#insn-008fb594)
  - `FALL_THROUGH` [`008fb578`](#insn-008fb578) → [`008fb57c`](#insn-008fb57c)
- ブロック [`008fb57c`](#insn-008fb57c) 範囲 `[['008fb57c', '008fb593']]`
  - `FALL_THROUGH` [`008fb590`](#insn-008fb590) → [`008fb594`](#insn-008fb594)
- ブロック [`008fb594`](#insn-008fb594) 範囲 `[['008fb594', '008fb59b']]`
  - `CONDITIONAL_JUMP` [`008fb598`](#insn-008fb598) → [`008fb5ac`](#insn-008fb5ac)
  - `FALL_THROUGH` [`008fb598`](#insn-008fb598) → [`008fb59c`](#insn-008fb59c)
- ブロック [`008fb59c`](#insn-008fb59c) 範囲 `[['008fb59c', '008fb5ab']]`
  - `CONDITIONAL_JUMP` [`008fb5a8`](#insn-008fb5a8) → [`008fb724`](#insn-008fb724)
  - `FALL_THROUGH` [`008fb5a8`](#insn-008fb5a8) → [`008fb5ac`](#insn-008fb5ac)
- ブロック [`008fb5ac`](#insn-008fb5ac) 範囲 `[['008fb5ac', '008fb5b3']]`
  - `CONDITIONAL_JUMP` [`008fb5b0`](#insn-008fb5b0) → [`008fb5bc`](#insn-008fb5bc)
  - `FALL_THROUGH` [`008fb5b0`](#insn-008fb5b0) → [`008fb5b4`](#insn-008fb5b4)
- ブロック [`008fb5b4`](#insn-008fb5b4) 範囲 `[['008fb5b4', '008fb5bb']]`
  - `FALL_THROUGH` [`008fb5b8`](#insn-008fb5b8) → [`008fb5bc`](#insn-008fb5bc)
- ブロック [`008fb5bc`](#insn-008fb5bc) 範囲 `[['008fb5bc', '008fb5c3']]`
  - `CONDITIONAL_JUMP` [`008fb5c0`](#insn-008fb5c0) → [`008fb5cc`](#insn-008fb5cc)
  - `FALL_THROUGH` [`008fb5c0`](#insn-008fb5c0) → [`008fb5c4`](#insn-008fb5c4)
- ブロック [`008fb5c4`](#insn-008fb5c4) 範囲 `[['008fb5c4', '008fb5cb']]`
  - `FALL_THROUGH` [`008fb5c8`](#insn-008fb5c8) → [`008fb5cc`](#insn-008fb5cc)
- ブロック [`008fb5cc`](#insn-008fb5cc) 範囲 `[['008fb5cc', '008fb5eb']]`
  - `CONDITIONAL_JUMP` [`008fb5e8`](#insn-008fb5e8) → [`008fb614`](#insn-008fb614)
  - `FALL_THROUGH` [`008fb5e8`](#insn-008fb5e8) → [`008fb5ec`](#insn-008fb5ec)
- ブロック [`008fb5ec`](#insn-008fb5ec) 範囲 `[['008fb5ec', '008fb5fb']]`
  - `CONDITIONAL_JUMP` [`008fb5f8`](#insn-008fb5f8) → [`008fb614`](#insn-008fb614)
  - `FALL_THROUGH` [`008fb5f8`](#insn-008fb5f8) → [`008fb5fc`](#insn-008fb5fc)
- ブロック [`008fb5fc`](#insn-008fb5fc) 範囲 `[['008fb5fc', '008fb613']]`
  - `FALL_THROUGH` [`008fb610`](#insn-008fb610) → [`008fb614`](#insn-008fb614)
- ブロック [`008fb614`](#insn-008fb614) 範囲 `[['008fb614', '008fb61b']]`
  - `CONDITIONAL_JUMP` [`008fb618`](#insn-008fb618) → [`008fb644`](#insn-008fb644)
  - `FALL_THROUGH` [`008fb618`](#insn-008fb618) → [`008fb61c`](#insn-008fb61c)
- ブロック [`008fb61c`](#insn-008fb61c) 範囲 `[['008fb61c', '008fb62b']]`
  - `CONDITIONAL_JUMP` [`008fb628`](#insn-008fb628) → [`008fb644`](#insn-008fb644)
  - `FALL_THROUGH` [`008fb628`](#insn-008fb628) → [`008fb62c`](#insn-008fb62c)
- ブロック [`008fb62c`](#insn-008fb62c) 範囲 `[['008fb62c', '008fb643']]`
  - `FALL_THROUGH` [`008fb640`](#insn-008fb640) → [`008fb644`](#insn-008fb644)
- ブロック [`008fb644`](#insn-008fb644) 範囲 `[['008fb644', '008fb64b']]`
  - `CONDITIONAL_JUMP` [`008fb648`](#insn-008fb648) → [`008fbaa4`](#insn-008fbaa4)
  - `FALL_THROUGH` [`008fb648`](#insn-008fb648) → [`008fb64c`](#insn-008fb64c)
- ブロック [`008fb64c`](#insn-008fb64c) 範囲 `[['008fb64c', '008fb6c7']]`
  - `CONDITIONAL_JUMP` [`008fb6c4`](#insn-008fb6c4) → [`008fb6f0`](#insn-008fb6f0)
  - `FALL_THROUGH` [`008fb6c4`](#insn-008fb6c4) → [`008fb6c8`](#insn-008fb6c8)
- ブロック [`008fb6c8`](#insn-008fb6c8) 範囲 `[['008fb6c8', '008fb6d7']]`
  - `CONDITIONAL_JUMP` [`008fb6d4`](#insn-008fb6d4) → [`008fb6f0`](#insn-008fb6f0)
  - `FALL_THROUGH` [`008fb6d4`](#insn-008fb6d4) → [`008fb6d8`](#insn-008fb6d8)
- ブロック [`008fb6d8`](#insn-008fb6d8) 範囲 `[['008fb6d8', '008fb6ef']]`
  - `FALL_THROUGH` [`008fb6ec`](#insn-008fb6ec) → [`008fb6f0`](#insn-008fb6f0)
- ブロック [`008fb6f0`](#insn-008fb6f0) 範囲 `[['008fb6f0', '008fb6f7']]`
  - `CONDITIONAL_JUMP` [`008fb6f4`](#insn-008fb6f4) → [`008fb708`](#insn-008fb708)
  - `FALL_THROUGH` [`008fb6f4`](#insn-008fb6f4) → [`008fb6f8`](#insn-008fb6f8)
- ブロック [`008fb6f8`](#insn-008fb6f8) 範囲 `[['008fb6f8', '008fb707']]`
  - `CONDITIONAL_JUMP` [`008fb704`](#insn-008fb704) → [`008fb748`](#insn-008fb748)
  - `FALL_THROUGH` [`008fb704`](#insn-008fb704) → [`008fb708`](#insn-008fb708)
- ブロック [`008fb708`](#insn-008fb708) 範囲 `[['008fb708', '008fb70f']]`
  - `CONDITIONAL_JUMP` [`008fb70c`](#insn-008fb70c) → [`008fb768`](#insn-008fb768)
  - `FALL_THROUGH` [`008fb70c`](#insn-008fb70c) → [`008fb710`](#insn-008fb710)
- ブロック [`008fb710`](#insn-008fb710) 範囲 `[['008fb710', '008fb717']]`
  - `CONDITIONAL_JUMP` [`008fb714`](#insn-008fb714) → [`008fb778`](#insn-008fb778)
  - `FALL_THROUGH` [`008fb714`](#insn-008fb714) → [`008fb718`](#insn-008fb718)
- ブロック [`008fb718`](#insn-008fb718) 範囲 `[['008fb718', '008fb71f']]`
  - `CONDITIONAL_JUMP` [`008fb71c`](#insn-008fb71c) → [`008fb788`](#insn-008fb788)
  - `FALL_THROUGH` [`008fb71c`](#insn-008fb71c) → [`008fb720`](#insn-008fb720)
- ブロック [`008fb720`](#insn-008fb720) 範囲 `[['008fb720', '008fb723']]`
  - `UNCONDITIONAL_JUMP` [`008fb720`](#insn-008fb720) → [`008fbaf8`](#insn-008fbaf8)
- ブロック [`008fb724`](#insn-008fb724) 範囲 `[['008fb724', '008fb743']]`
  - `CONDITIONAL_JUMP` [`008fb740`](#insn-008fb740) → [`008fb5b4`](#insn-008fb5b4)
  - `FALL_THROUGH` [`008fb740`](#insn-008fb740) → [`008fb744`](#insn-008fb744)
- ブロック [`008fb744`](#insn-008fb744) 範囲 `[['008fb744', '008fb747']]`
  - `UNCONDITIONAL_JUMP` [`008fb744`](#insn-008fb744) → [`008fb5bc`](#insn-008fb5bc)
- ブロック [`008fb748`](#insn-008fb748) 範囲 `[['008fb748', '008fb767']]`
  - `CONDITIONAL_JUMP` [`008fb764`](#insn-008fb764) → [`008fb710`](#insn-008fb710)
  - `FALL_THROUGH` [`008fb764`](#insn-008fb764) → [`008fb768`](#insn-008fb768)
- ブロック [`008fb768`](#insn-008fb768) 範囲 `[['008fb768', '008fb777']]`
  - `CONDITIONAL_JUMP` [`008fb774`](#insn-008fb774) → [`008fb718`](#insn-008fb718)
  - `FALL_THROUGH` [`008fb774`](#insn-008fb774) → [`008fb778`](#insn-008fb778)
- ブロック [`008fb778`](#insn-008fb778) 範囲 `[['008fb778', '008fb787']]`
  - `CONDITIONAL_JUMP` [`008fb784`](#insn-008fb784) → [`008fbaf8`](#insn-008fbaf8)
  - `FALL_THROUGH` [`008fb784`](#insn-008fb784) → [`008fb788`](#insn-008fb788)
- ブロック [`008fb788`](#insn-008fb788) 範囲 `[['008fb788', '008fb7f7']]`
  - `CONDITIONAL_JUMP` [`008fb7f4`](#insn-008fb7f4) → [`008fb820`](#insn-008fb820)
  - `FALL_THROUGH` [`008fb7f4`](#insn-008fb7f4) → [`008fb7f8`](#insn-008fb7f8)
- ブロック [`008fb7f8`](#insn-008fb7f8) 範囲 `[['008fb7f8', '008fb807']]`
  - `CONDITIONAL_JUMP` [`008fb804`](#insn-008fb804) → [`008fb820`](#insn-008fb820)
  - `FALL_THROUGH` [`008fb804`](#insn-008fb804) → [`008fb808`](#insn-008fb808)
- ブロック [`008fb808`](#insn-008fb808) 範囲 `[['008fb808', '008fb81f']]`
  - `FALL_THROUGH` [`008fb81c`](#insn-008fb81c) → [`008fb820`](#insn-008fb820)
- ブロック [`008fb820`](#insn-008fb820) 範囲 `[['008fb820', '008fb827']]`
  - `CONDITIONAL_JUMP` [`008fb824`](#insn-008fb824) → [`008fb838`](#insn-008fb838)
  - `FALL_THROUGH` [`008fb824`](#insn-008fb824) → [`008fb828`](#insn-008fb828)
- ブロック [`008fb828`](#insn-008fb828) 範囲 `[['008fb828', '008fb837']]`
  - `CONDITIONAL_JUMP` [`008fb834`](#insn-008fb834) → [`008fb884`](#insn-008fb884)
  - `FALL_THROUGH` [`008fb834`](#insn-008fb834) → [`008fb838`](#insn-008fb838)
- ブロック [`008fb838`](#insn-008fb838) 範囲 `[['008fb838', '008fb83f']]`
  - `CONDITIONAL_JUMP` [`008fb83c`](#insn-008fb83c) → [`008fb848`](#insn-008fb848)
  - `FALL_THROUGH` [`008fb83c`](#insn-008fb83c) → [`008fb840`](#insn-008fb840)
- ブロック [`008fb840`](#insn-008fb840) 範囲 `[['008fb840', '008fb847']]`
  - `FALL_THROUGH` [`008fb844`](#insn-008fb844) → [`008fb848`](#insn-008fb848)
- ブロック [`008fb848`](#insn-008fb848) 範囲 `[['008fb848', '008fb84f']]`
  - `CONDITIONAL_JUMP` [`008fb84c`](#insn-008fb84c) → [`008fb858`](#insn-008fb858)
  - `FALL_THROUGH` [`008fb84c`](#insn-008fb84c) → [`008fb850`](#insn-008fb850)
- ブロック [`008fb850`](#insn-008fb850) 範囲 `[['008fb850', '008fb857']]`
  - `FALL_THROUGH` [`008fb854`](#insn-008fb854) → [`008fb858`](#insn-008fb858)
- ブロック [`008fb858`](#insn-008fb858) 範囲 `[['008fb858', '008fb867']]`
  - `CONDITIONAL_JUMP` [`008fb864`](#insn-008fb864) → [`008fbbbc`](#insn-008fbbbc)
  - `FALL_THROUGH` [`008fb864`](#insn-008fb864) → [`008fb868`](#insn-008fb868)
- ブロック [`008fb868`](#insn-008fb868) 範囲 `[['008fb868', '008fb883']]`
- ブロック [`008fb884`](#insn-008fb884) 範囲 `[['008fb884', '008fb8a3']]`
  - `CONDITIONAL_JUMP` [`008fb8a0`](#insn-008fb8a0) → [`008fb840`](#insn-008fb840)
  - `FALL_THROUGH` [`008fb8a0`](#insn-008fb8a0) → [`008fb8a4`](#insn-008fb8a4)
- ブロック [`008fb8a4`](#insn-008fb8a4) 範囲 `[['008fb8a4', '008fb8a7']]`
  - `UNCONDITIONAL_JUMP` [`008fb8a4`](#insn-008fb8a4) → [`008fb848`](#insn-008fb848)
- ブロック [`008fb8a8`](#insn-008fb8a8) 範囲 `[['008fb8a8', '008fb8b7']]`
  - `CONDITIONAL_JUMP` [`008fb8b4`](#insn-008fb8b4) → [`008faf34`](#insn-008faf34)
  - `FALL_THROUGH` [`008fb8b4`](#insn-008fb8b4) → [`008fb8b8`](#insn-008fb8b8)
- ブロック [`008fb8b8`](#insn-008fb8b8) 範囲 `[['008fb8b8', '008fb8ff']]`
  - `UNCONDITIONAL_JUMP` [`008fb8fc`](#insn-008fb8fc) → [`008faf34`](#insn-008faf34)
- ブロック [`008fb900`](#insn-008fb900) 範囲 `[['008fb900', '008fb90f']]`
  - `CONDITIONAL_JUMP` [`008fb90c`](#insn-008fb90c) → [`008fb090`](#insn-008fb090)
  - `FALL_THROUGH` [`008fb90c`](#insn-008fb90c) → [`008fb910`](#insn-008fb910)
- ブロック [`008fb910`](#insn-008fb910) 範囲 `[['008fb910', '008fb953']]`
  - `UNCONDITIONAL_JUMP` [`008fb950`](#insn-008fb950) → [`008fb090`](#insn-008fb090)
- ブロック [`008fb954`](#insn-008fb954) 範囲 `[['008fb954', '008fb963']]`
  - `CONDITIONAL_JUMP` [`008fb960`](#insn-008fb960) → [`008fb1c4`](#insn-008fb1c4)
  - `FALL_THROUGH` [`008fb960`](#insn-008fb960) → [`008fb964`](#insn-008fb964)
- ブロック [`008fb964`](#insn-008fb964) 範囲 `[['008fb964', '008fb9a7']]`
  - `UNCONDITIONAL_JUMP` [`008fb9a4`](#insn-008fb9a4) → [`008fb1c4`](#insn-008fb1c4)
- ブロック [`008fb9a8`](#insn-008fb9a8) 範囲 `[['008fb9a8', '008fb9b7']]`
  - `CONDITIONAL_JUMP` [`008fb9b4`](#insn-008fb9b4) → [`008fb2d8`](#insn-008fb2d8)
  - `FALL_THROUGH` [`008fb9b4`](#insn-008fb9b4) → [`008fb9b8`](#insn-008fb9b8)
- ブロック [`008fb9b8`](#insn-008fb9b8) 範囲 `[['008fb9b8', '008fb9fb']]`
  - `UNCONDITIONAL_JUMP` [`008fb9f8`](#insn-008fb9f8) → [`008fb2d8`](#insn-008fb2d8)
- ブロック [`008fb9fc`](#insn-008fb9fc) 範囲 `[['008fb9fc', '008fba0b']]`
  - `CONDITIONAL_JUMP` [`008fba08`](#insn-008fba08) → [`008fb3e8`](#insn-008fb3e8)
  - `FALL_THROUGH` [`008fba08`](#insn-008fba08) → [`008fba0c`](#insn-008fba0c)
- ブロック [`008fba0c`](#insn-008fba0c) 範囲 `[['008fba0c', '008fba4f']]`
  - `UNCONDITIONAL_JUMP` [`008fba4c`](#insn-008fba4c) → [`008fb3e8`](#insn-008fb3e8)
- ブロック [`008fba50`](#insn-008fba50) 範囲 `[['008fba50', '008fba5f']]`
  - `CONDITIONAL_JUMP` [`008fba5c`](#insn-008fba5c) → [`008fb4f8`](#insn-008fb4f8)
  - `FALL_THROUGH` [`008fba5c`](#insn-008fba5c) → [`008fba60`](#insn-008fba60)
- ブロック [`008fba60`](#insn-008fba60) 範囲 `[['008fba60', '008fbaa3']]`
  - `UNCONDITIONAL_JUMP` [`008fbaa0`](#insn-008fbaa0) → [`008fb4f8`](#insn-008fb4f8)
- ブロック [`008fbaa4`](#insn-008fbaa4) 範囲 `[['008fbaa4', '008fbab3']]`
  - `CONDITIONAL_JUMP` [`008fbab0`](#insn-008fbab0) → [`008fb64c`](#insn-008fb64c)
  - `FALL_THROUGH` [`008fbab0`](#insn-008fbab0) → [`008fbab4`](#insn-008fbab4)
- ブロック [`008fbab4`](#insn-008fbab4) 範囲 `[['008fbab4', '008fbaf7']]`
  - `UNCONDITIONAL_JUMP` [`008fbaf4`](#insn-008fbaf4) → [`008fb64c`](#insn-008fb64c)
- ブロック [`008fbaf8`](#insn-008fbaf8) 範囲 `[['008fbaf8', '008fbb07']]`
  - `CONDITIONAL_JUMP` [`008fbb04`](#insn-008fbb04) → [`008fb788`](#insn-008fb788)
  - `FALL_THROUGH` [`008fbb04`](#insn-008fbb04) → [`008fbb08`](#insn-008fbb08)
- ブロック [`008fbb08`](#insn-008fbb08) 範囲 `[['008fbb08', '008fbb4b']]`
  - `UNCONDITIONAL_JUMP` [`008fbb48`](#insn-008fbb48) → [`008fb788`](#insn-008fb788)
- ブロック [`008fbbbc`](#insn-008fbbbc) 範囲 `[['008fbbbc', '008fbbbf']]`

## 命令位置別の参照

- [`008faee0`](#insn-008faee0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faee4`](#insn-008faee4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faee8`](#insn-008faee8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faeec`](#insn-008faeec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faef0`](#insn-008faef0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf08`](#insn-008faf08) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf0c`](#insn-008faf0c) → [`00758228`](../00758/00758228.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00758228` · 推定シンボル `None` · 推定型 `None`
- [`008faf20`](#insn-008faf20) → `00c85bc8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008faf2c`](#insn-008faf2c) → `00ca5038`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008faf30`](#insn-008faf30) → [`008fb8a8`](#insn-008fb8a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf3c`](#insn-008faf3c) → `Stack[-0x85]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf40`](#insn-008faf40) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf4c`](#insn-008faf4c) → `002b63ce`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008faf50`](#insn-008faf50) → `Stack[-0x87]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf58`](#insn-008faf58) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf5c`](#insn-008faf5c) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf68`](#insn-008faf68) → `002b1f47`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf6c`](#insn-008faf6c) → `002b1f4c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008faf70`](#insn-008faf70) → `Stack[-0x9a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf74`](#insn-008faf74) → `Stack[-0xa7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf78`](#insn-008faf78) → `Stack[-0xa2]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf90`](#insn-008faf90) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008faf98`](#insn-008faf98) → [`006333b4`](../00633/006333b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006333b4` · 推定シンボル `None` · 推定型 `None`
- [`008faf9c`](#insn-008faf9c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fafa4`](#insn-008fafa4) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fafac`](#insn-008fafac) → [`008fafd8`](#insn-008fafd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fafb8`](#insn-008fafb8) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`008fafbc`](#insn-008fafbc) → [`008fafd8`](#insn-008fafd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fafd4`](#insn-008fafd4) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`008fafd8`](#insn-008fafd8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fafdc`](#insn-008fafdc) → [`008faff0`](#insn-008faff0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fafe8`](#insn-008fafe8) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`008fafec`](#insn-008fafec) → [`008fb160`](#insn-008fb160) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faff0`](#insn-008faff0) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faff4`](#insn-008faff4) → [`008fb000`](#insn-008fb000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faff8`](#insn-008faff8) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faffc`](#insn-008faffc) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`008fb000`](#insn-008fb000) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb004`](#insn-008fb004) → [`008fb010`](#insn-008fb010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb008`](#insn-008fb008) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb00c`](#insn-008fb00c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`008fb018`](#insn-008fb018) → [`00864590`](../00864/00864590.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00864590` · 推定シンボル `None` · 推定型 `None`
- [`008fb01c`](#insn-008fb01c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb024`](#insn-008fb024) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb02c`](#insn-008fb02c) → [`008fb058`](#insn-008fb058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb038`](#insn-008fb038) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`008fb03c`](#insn-008fb03c) → [`008fb058`](#insn-008fb058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb054`](#insn-008fb054) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`008fb058`](#insn-008fb058) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb05c`](#insn-008fb05c) → [`008fb088`](#insn-008fb088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb068`](#insn-008fb068) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`008fb06c`](#insn-008fb06c) → [`008fb088`](#insn-008fb088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb084`](#insn-008fb084) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`008fb088`](#insn-008fb088) → `00ca5038`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb08c`](#insn-008fb08c) → [`008fb900`](#insn-008fb900) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb098`](#insn-008fb098) → `Stack[-0x85]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb09c`](#insn-008fb09c) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb0a8`](#insn-008fb0a8) → `002bef6a`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb0ac`](#insn-008fb0ac) → `Stack[-0x87]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb0b4`](#insn-008fb0b4) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb0b8`](#insn-008fb0b8) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb0c4`](#insn-008fb0c4) → `002a9f47`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb0c8`](#insn-008fb0c8) → `002a9f4c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb0cc`](#insn-008fb0cc) → `Stack[-0x9a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb0d0`](#insn-008fb0d0) → `Stack[-0xa7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb0d4`](#insn-008fb0d4) → `Stack[-0xa2]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb0e4`](#insn-008fb0e4) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb0ec`](#insn-008fb0ec) → [`006333b4`](../00633/006333b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006333b4` · 推定シンボル `None` · 推定型 `None`
- [`008fb0f0`](#insn-008fb0f0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb0f8`](#insn-008fb0f8) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb100`](#insn-008fb100) → [`008fb12c`](#insn-008fb12c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb10c`](#insn-008fb10c) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`008fb110`](#insn-008fb110) → [`008fb12c`](#insn-008fb12c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb128`](#insn-008fb128) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`008fb12c`](#insn-008fb12c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb130`](#insn-008fb130) → [`008fb144`](#insn-008fb144) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb13c`](#insn-008fb13c) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`008fb140`](#insn-008fb140) → [`008fb184`](#insn-008fb184) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb144`](#insn-008fb144) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb148`](#insn-008fb148) → [`008fb1a4`](#insn-008fb1a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb14c`](#insn-008fb14c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb150`](#insn-008fb150) → [`008fb1b4`](#insn-008fb1b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb154`](#insn-008fb154) → `00ca5038`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb158`](#insn-008fb158) → [`008fb1c4`](#insn-008fb1c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb15c`](#insn-008fb15c) → [`008fb954`](#insn-008fb954) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb174`](#insn-008fb174) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`008fb178`](#insn-008fb178) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb17c`](#insn-008fb17c) → [`008faff8`](#insn-008faff8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb180`](#insn-008fb180) → [`008fb000`](#insn-008fb000) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb198`](#insn-008fb198) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`008fb19c`](#insn-008fb19c) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb1a0`](#insn-008fb1a0) → [`008fb14c`](#insn-008fb14c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb1a4`](#insn-008fb1a4) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb1a8`](#insn-008fb1a8) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`008fb1ac`](#insn-008fb1ac) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb1b0`](#insn-008fb1b0) → [`008fb154`](#insn-008fb154) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb1b4`](#insn-008fb1b4) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb1b8`](#insn-008fb1b8) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`008fb1bc`](#insn-008fb1bc) → `00ca5038`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb1c0`](#insn-008fb1c0) → [`008fb954`](#insn-008fb954) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb1cc`](#insn-008fb1cc) → `Stack[-0x85]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb1d0`](#insn-008fb1d0) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb1dc`](#insn-008fb1dc) → `002c0076`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb1e0`](#insn-008fb1e0) → `Stack[-0x87]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb1e8`](#insn-008fb1e8) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb1ec`](#insn-008fb1ec) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb1f8`](#insn-008fb1f8) → `002a9e9a`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb1fc`](#insn-008fb1fc) → `002a9e9f`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb200`](#insn-008fb200) → `Stack[-0x9a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb204`](#insn-008fb204) → `Stack[-0xa7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb208`](#insn-008fb208) → `Stack[-0xa2]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb218`](#insn-008fb218) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb220`](#insn-008fb220) → [`006333b4`](../00633/006333b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006333b4` · 推定シンボル `None` · 推定型 `None`
- [`008fb224`](#insn-008fb224) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb230`](#insn-008fb230) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb238`](#insn-008fb238) → [`008fb264`](#insn-008fb264) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb244`](#insn-008fb244) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`008fb248`](#insn-008fb248) → [`008fb264`](#insn-008fb264) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb260`](#insn-008fb260) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`008fb264`](#insn-008fb264) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb268`](#insn-008fb268) → [`008fb27c`](#insn-008fb27c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb274`](#insn-008fb274) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`008fb278`](#insn-008fb278) → [`008fb298`](#insn-008fb298) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb27c`](#insn-008fb27c) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb280`](#insn-008fb280) → [`008fb2b8`](#insn-008fb2b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb284`](#insn-008fb284) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb288`](#insn-008fb288) → [`008fb2c8`](#insn-008fb2c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb28c`](#insn-008fb28c) → `00ca5038`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb290`](#insn-008fb290) → [`008fb2d8`](#insn-008fb2d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb294`](#insn-008fb294) → [`008fb9a8`](#insn-008fb9a8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb2ac`](#insn-008fb2ac) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`008fb2b0`](#insn-008fb2b0) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb2b4`](#insn-008fb2b4) → [`008fb284`](#insn-008fb284) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb2b8`](#insn-008fb2b8) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb2bc`](#insn-008fb2bc) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`008fb2c0`](#insn-008fb2c0) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb2c4`](#insn-008fb2c4) → [`008fb28c`](#insn-008fb28c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb2c8`](#insn-008fb2c8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb2cc`](#insn-008fb2cc) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`008fb2d0`](#insn-008fb2d0) → `00ca5038`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb2d4`](#insn-008fb2d4) → [`008fb9a8`](#insn-008fb9a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb2e0`](#insn-008fb2e0) → `Stack[-0x85]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb2e4`](#insn-008fb2e4) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb2f0`](#insn-008fb2f0) → `002b91bb`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb2f4`](#insn-008fb2f4) → `Stack[-0x87]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb2fc`](#insn-008fb2fc) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb300`](#insn-008fb300) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb30c`](#insn-008fb30c) → `002bdbbb`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb310`](#insn-008fb310) → `002bdbc0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb314`](#insn-008fb314) → `Stack[-0x9a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb318`](#insn-008fb318) → `Stack[-0xa7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb31c`](#insn-008fb31c) → `Stack[-0xa2]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb32c`](#insn-008fb32c) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb334`](#insn-008fb334) → [`006333b4`](../00633/006333b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006333b4` · 推定シンボル `None` · 推定型 `None`
- [`008fb338`](#insn-008fb338) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb340`](#insn-008fb340) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb348`](#insn-008fb348) → [`008fb374`](#insn-008fb374) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb354`](#insn-008fb354) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`008fb358`](#insn-008fb358) → [`008fb374`](#insn-008fb374) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb370`](#insn-008fb370) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`008fb374`](#insn-008fb374) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb378`](#insn-008fb378) → [`008fb38c`](#insn-008fb38c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb384`](#insn-008fb384) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`008fb388`](#insn-008fb388) → [`008fb3a8`](#insn-008fb3a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb38c`](#insn-008fb38c) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb390`](#insn-008fb390) → [`008fb3c8`](#insn-008fb3c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb394`](#insn-008fb394) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb398`](#insn-008fb398) → [`008fb3d8`](#insn-008fb3d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb39c`](#insn-008fb39c) → `00ca5038`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb3a0`](#insn-008fb3a0) → [`008fb3e8`](#insn-008fb3e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb3a4`](#insn-008fb3a4) → [`008fb9fc`](#insn-008fb9fc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb3bc`](#insn-008fb3bc) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`008fb3c0`](#insn-008fb3c0) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb3c4`](#insn-008fb3c4) → [`008fb394`](#insn-008fb394) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb3c8`](#insn-008fb3c8) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb3cc`](#insn-008fb3cc) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`008fb3d0`](#insn-008fb3d0) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb3d4`](#insn-008fb3d4) → [`008fb39c`](#insn-008fb39c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb3d8`](#insn-008fb3d8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb3dc`](#insn-008fb3dc) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`008fb3e0`](#insn-008fb3e0) → `00ca5038`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb3e4`](#insn-008fb3e4) → [`008fb9fc`](#insn-008fb9fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb3f0`](#insn-008fb3f0) → `Stack[-0x85]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb3f4`](#insn-008fb3f4) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb400`](#insn-008fb400) → `0029f1f3`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb404`](#insn-008fb404) → `Stack[-0x87]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb40c`](#insn-008fb40c) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb410`](#insn-008fb410) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb41c`](#insn-008fb41c) → `002c13b3`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb420`](#insn-008fb420) → `002c13b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb424`](#insn-008fb424) → `Stack[-0x9a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb428`](#insn-008fb428) → `Stack[-0xa7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb42c`](#insn-008fb42c) → `Stack[-0xa2]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb43c`](#insn-008fb43c) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb444`](#insn-008fb444) → [`006333b4`](../00633/006333b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006333b4` · 推定シンボル `None` · 推定型 `None`
- [`008fb448`](#insn-008fb448) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb450`](#insn-008fb450) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb458`](#insn-008fb458) → [`008fb484`](#insn-008fb484) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb464`](#insn-008fb464) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`008fb468`](#insn-008fb468) → [`008fb484`](#insn-008fb484) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb480`](#insn-008fb480) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`008fb484`](#insn-008fb484) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb488`](#insn-008fb488) → [`008fb49c`](#insn-008fb49c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb494`](#insn-008fb494) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`008fb498`](#insn-008fb498) → [`008fb4b8`](#insn-008fb4b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb49c`](#insn-008fb49c) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb4a0`](#insn-008fb4a0) → [`008fb4d8`](#insn-008fb4d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb4a4`](#insn-008fb4a4) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb4a8`](#insn-008fb4a8) → [`008fb4e8`](#insn-008fb4e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb4ac`](#insn-008fb4ac) → `00ca5038`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb4b0`](#insn-008fb4b0) → [`008fb4f8`](#insn-008fb4f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb4b4`](#insn-008fb4b4) → [`008fba50`](#insn-008fba50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb4cc`](#insn-008fb4cc) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`008fb4d0`](#insn-008fb4d0) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb4d4`](#insn-008fb4d4) → [`008fb4a4`](#insn-008fb4a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb4d8`](#insn-008fb4d8) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb4dc`](#insn-008fb4dc) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`008fb4e0`](#insn-008fb4e0) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb4e4`](#insn-008fb4e4) → [`008fb4ac`](#insn-008fb4ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb4e8`](#insn-008fb4e8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb4ec`](#insn-008fb4ec) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`008fb4f0`](#insn-008fb4f0) → `00ca5038`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb4f4`](#insn-008fb4f4) → [`008fba50`](#insn-008fba50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb500`](#insn-008fb500) → `Stack[-0x85]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb504`](#insn-008fb504) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb510`](#insn-008fb510) → `002b3eda`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb514`](#insn-008fb514) → `Stack[-0x87]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb51c`](#insn-008fb51c) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb520`](#insn-008fb520) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb52c`](#insn-008fb52c) → `002b921c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb530`](#insn-008fb530) → `002b9221`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb534`](#insn-008fb534) → `Stack[-0x9a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb538`](#insn-008fb538) → `Stack[-0xa7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb53c`](#insn-008fb53c) → `Stack[-0xa2]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb54c`](#insn-008fb54c) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb554`](#insn-008fb554) → [`006333b4`](../00633/006333b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006333b4` · 推定シンボル `None` · 推定型 `None`
- [`008fb558`](#insn-008fb558) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb560`](#insn-008fb560) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb568`](#insn-008fb568) → [`008fb594`](#insn-008fb594) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb574`](#insn-008fb574) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`008fb578`](#insn-008fb578) → [`008fb594`](#insn-008fb594) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb590`](#insn-008fb590) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`008fb594`](#insn-008fb594) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb598`](#insn-008fb598) → [`008fb5ac`](#insn-008fb5ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb5a4`](#insn-008fb5a4) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`008fb5a8`](#insn-008fb5a8) → [`008fb724`](#insn-008fb724) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb5ac`](#insn-008fb5ac) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb5b0`](#insn-008fb5b0) → [`008fb5bc`](#insn-008fb5bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb5b4`](#insn-008fb5b4) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb5b8`](#insn-008fb5b8) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`008fb5bc`](#insn-008fb5bc) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb5c0`](#insn-008fb5c0) → [`008fb5cc`](#insn-008fb5cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb5c4`](#insn-008fb5c4) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb5c8`](#insn-008fb5c8) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`008fb5d4`](#insn-008fb5d4) → [`00862ca8`](../00862/00862ca8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00862ca8` · 推定シンボル `None` · 推定型 `None`
- [`008fb5d8`](#insn-008fb5d8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb5e0`](#insn-008fb5e0) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb5e8`](#insn-008fb5e8) → [`008fb614`](#insn-008fb614) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb5f4`](#insn-008fb5f4) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`008fb5f8`](#insn-008fb5f8) → [`008fb614`](#insn-008fb614) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb610`](#insn-008fb610) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`008fb614`](#insn-008fb614) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb618`](#insn-008fb618) → [`008fb644`](#insn-008fb644) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb624`](#insn-008fb624) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`008fb628`](#insn-008fb628) → [`008fb644`](#insn-008fb644) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb640`](#insn-008fb640) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`008fb644`](#insn-008fb644) → `00ca5038`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb648`](#insn-008fb648) → [`008fbaa4`](#insn-008fbaa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb654`](#insn-008fb654) → `Stack[-0x85]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb658`](#insn-008fb658) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb664`](#insn-008fb664) → `002a450a`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb668`](#insn-008fb668) → `Stack[-0x87]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb670`](#insn-008fb670) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb674`](#insn-008fb674) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb680`](#insn-008fb680) → `002bdbc9`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb684`](#insn-008fb684) → `002bdbce`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb688`](#insn-008fb688) → `Stack[-0x9a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb68c`](#insn-008fb68c) → `Stack[-0xa7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb690`](#insn-008fb690) → `Stack[-0xa2]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb6a8`](#insn-008fb6a8) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb6b0`](#insn-008fb6b0) → [`006333b4`](../00633/006333b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006333b4` · 推定シンボル `None` · 推定型 `None`
- [`008fb6b4`](#insn-008fb6b4) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb6bc`](#insn-008fb6bc) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb6c4`](#insn-008fb6c4) → [`008fb6f0`](#insn-008fb6f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb6d0`](#insn-008fb6d0) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`008fb6d4`](#insn-008fb6d4) → [`008fb6f0`](#insn-008fb6f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb6ec`](#insn-008fb6ec) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`008fb6f0`](#insn-008fb6f0) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb6f4`](#insn-008fb6f4) → [`008fb708`](#insn-008fb708) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb700`](#insn-008fb700) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`008fb704`](#insn-008fb704) → [`008fb748`](#insn-008fb748) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb708`](#insn-008fb708) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb70c`](#insn-008fb70c) → [`008fb768`](#insn-008fb768) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb710`](#insn-008fb710) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb714`](#insn-008fb714) → [`008fb778`](#insn-008fb778) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb718`](#insn-008fb718) → `00ca5038`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb71c`](#insn-008fb71c) → [`008fb788`](#insn-008fb788) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb720`](#insn-008fb720) → [`008fbaf8`](#insn-008fbaf8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb738`](#insn-008fb738) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`008fb73c`](#insn-008fb73c) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb740`](#insn-008fb740) → [`008fb5b4`](#insn-008fb5b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb744`](#insn-008fb744) → [`008fb5bc`](#insn-008fb5bc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb75c`](#insn-008fb75c) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`008fb760`](#insn-008fb760) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb764`](#insn-008fb764) → [`008fb710`](#insn-008fb710) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb768`](#insn-008fb768) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb76c`](#insn-008fb76c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`008fb770`](#insn-008fb770) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb774`](#insn-008fb774) → [`008fb718`](#insn-008fb718) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb778`](#insn-008fb778) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb77c`](#insn-008fb77c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`008fb780`](#insn-008fb780) → `00ca5038`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb784`](#insn-008fb784) → [`008fbaf8`](#insn-008fbaf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb794`](#insn-008fb794) → `002a3471`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb798`](#insn-008fb798) → `002a3476`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb79c`](#insn-008fb79c) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb7a4`](#insn-008fb7a4) → `Stack[-0x82]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb7a8`](#insn-008fb7a8) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb7ac`](#insn-008fb7ac) → `Stack[-0x8a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb7b8`](#insn-008fb7b8) → `002c034b`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb7bc`](#insn-008fb7bc) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb7c0`](#insn-008fb7c0) → `Stack[-0x97]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb7c4`](#insn-008fb7c4) → `Stack[-0xa7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb7cc`](#insn-008fb7cc) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb7e0`](#insn-008fb7e0) → [`006333b4`](../00633/006333b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006333b4` · 推定シンボル `None` · 推定型 `None`
- [`008fb7e4`](#insn-008fb7e4) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb7ec`](#insn-008fb7ec) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb7f4`](#insn-008fb7f4) → [`008fb820`](#insn-008fb820) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb800`](#insn-008fb800) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`008fb804`](#insn-008fb804) → [`008fb820`](#insn-008fb820) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb81c`](#insn-008fb81c) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`008fb820`](#insn-008fb820) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb824`](#insn-008fb824) → [`008fb838`](#insn-008fb838) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb830`](#insn-008fb830) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`008fb834`](#insn-008fb834) → [`008fb884`](#insn-008fb884) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb838`](#insn-008fb838) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb83c`](#insn-008fb83c) → [`008fb848`](#insn-008fb848) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb840`](#insn-008fb840) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb844`](#insn-008fb844) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`008fb848`](#insn-008fb848) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb84c`](#insn-008fb84c) → [`008fb858`](#insn-008fb858) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb850`](#insn-008fb850) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb854`](#insn-008fb854) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`008fb85c`](#insn-008fb85c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb864`](#insn-008fb864) → [`008fbbbc`](#insn-008fbbbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb868`](#insn-008fb868) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb86c`](#insn-008fb86c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb870`](#insn-008fb870) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb874`](#insn-008fb874) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb878`](#insn-008fb878) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb898`](#insn-008fb898) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`008fb89c`](#insn-008fb89c) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb8a0`](#insn-008fb8a0) → [`008fb840`](#insn-008fb840) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb8a4`](#insn-008fb8a4) → [`008fb848`](#insn-008fb848) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb8ac`](#insn-008fb8ac) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb8b0`](#insn-008fb8b0) → [`00c57f20`](../00c57/00c57f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f20` · 推定シンボル `None` · 推定型 `None`
- [`008fb8b4`](#insn-008fb8b4) → [`008faf34`](#insn-008faf34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb8bc`](#insn-008fb8bc) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb8c4`](#insn-008fb8c4) → [`0047edf4`](../0047e/0047edf4.md) · `PARAM` · `ANALYSIS` · 関数 `0047edf4` · 推定シンボル `None` · 推定型 `None`
- [`008fb8d0`](#insn-008fb8d0) → `00c63060`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008fb8d4`](#insn-008fb8d4) → `00ca5008`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb8d8`](#insn-008fb8d8) → `00ca5000`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb8d8`](#insn-008fb8d8) → `00ca5008`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb8e0`](#insn-008fb8e0) → `00ca5028`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb8e0`](#insn-008fb8e0) → `00ca5030`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb8e4`](#insn-008fb8e4) → `00ca5020`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb8e8`](#insn-008fb8e8) → `00ca5010`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb8e8`](#insn-008fb8e8) → `00ca5018`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb8e8`](#insn-008fb8e8) → `00ca5020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb8ec`](#insn-008fb8ec) → [`00c57f00`](../00c57/00c57f00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f00` · 推定シンボル `None` · 推定型 `None`
- [`008fb8f4`](#insn-008fb8f4) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb8f8`](#insn-008fb8f8) → [`00c57f40`](../00c57/00c57f40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f40` · 推定シンボル `None` · 推定型 `None`
- [`008fb8fc`](#insn-008fb8fc) → [`008faf34`](#insn-008faf34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb904`](#insn-008fb904) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb908`](#insn-008fb908) → [`00c57f20`](../00c57/00c57f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f20` · 推定シンボル `None` · 推定型 `None`
- [`008fb90c`](#insn-008fb90c) → [`008fb090`](#insn-008fb090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb918`](#insn-008fb918) → [`0047edf4`](../0047e/0047edf4.md) · `PARAM` · `ANALYSIS` · 関数 `0047edf4` · 推定シンボル `None` · 推定型 `None`
- [`008fb91c`](#insn-008fb91c) → `00ca5008`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb924`](#insn-008fb924) → `00c63060`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008fb928`](#insn-008fb928) → `00ca5000`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb928`](#insn-008fb928) → `00ca5008`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb930`](#insn-008fb930) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb934`](#insn-008fb934) → `00ca5028`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb934`](#insn-008fb934) → `00ca5030`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb938`](#insn-008fb938) → `00ca5020`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb93c`](#insn-008fb93c) → `00ca5010`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb93c`](#insn-008fb93c) → `00ca5018`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb93c`](#insn-008fb93c) → `00ca5020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb940`](#insn-008fb940) → [`00c57f00`](../00c57/00c57f00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f00` · 推定シンボル `None` · 推定型 `None`
- [`008fb948`](#insn-008fb948) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb94c`](#insn-008fb94c) → [`00c57f40`](../00c57/00c57f40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f40` · 推定シンボル `None` · 推定型 `None`
- [`008fb950`](#insn-008fb950) → [`008fb090`](#insn-008fb090) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb958`](#insn-008fb958) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb95c`](#insn-008fb95c) → [`00c57f20`](../00c57/00c57f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f20` · 推定シンボル `None` · 推定型 `None`
- [`008fb960`](#insn-008fb960) → [`008fb1c4`](#insn-008fb1c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb96c`](#insn-008fb96c) → [`0047edf4`](../0047e/0047edf4.md) · `PARAM` · `ANALYSIS` · 関数 `0047edf4` · 推定シンボル `None` · 推定型 `None`
- [`008fb970`](#insn-008fb970) → `00ca5008`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb978`](#insn-008fb978) → `00c63060`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008fb97c`](#insn-008fb97c) → `00ca5000`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb97c`](#insn-008fb97c) → `00ca5008`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb984`](#insn-008fb984) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb988`](#insn-008fb988) → `00ca5028`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb988`](#insn-008fb988) → `00ca5030`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb98c`](#insn-008fb98c) → `00ca5020`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb990`](#insn-008fb990) → `00ca5010`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb990`](#insn-008fb990) → `00ca5018`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb990`](#insn-008fb990) → `00ca5020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb994`](#insn-008fb994) → [`00c57f00`](../00c57/00c57f00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f00` · 推定シンボル `None` · 推定型 `None`
- [`008fb99c`](#insn-008fb99c) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb9a0`](#insn-008fb9a0) → [`00c57f40`](../00c57/00c57f40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f40` · 推定シンボル `None` · 推定型 `None`
- [`008fb9a4`](#insn-008fb9a4) → [`008fb1c4`](#insn-008fb1c4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb9ac`](#insn-008fb9ac) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb9b0`](#insn-008fb9b0) → [`00c57f20`](../00c57/00c57f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f20` · 推定シンボル `None` · 推定型 `None`
- [`008fb9b4`](#insn-008fb9b4) → [`008fb2d8`](#insn-008fb2d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb9c0`](#insn-008fb9c0) → [`0047edf4`](../0047e/0047edf4.md) · `PARAM` · `ANALYSIS` · 関数 `0047edf4` · 推定シンボル `None` · 推定型 `None`
- [`008fb9c4`](#insn-008fb9c4) → `00ca5008`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb9cc`](#insn-008fb9cc) → `00c63060`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008fb9d0`](#insn-008fb9d0) → `00ca5000`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb9d0`](#insn-008fb9d0) → `00ca5008`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb9d8`](#insn-008fb9d8) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb9dc`](#insn-008fb9dc) → `00ca5028`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb9dc`](#insn-008fb9dc) → `00ca5030`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb9e0`](#insn-008fb9e0) → `00ca5020`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb9e4`](#insn-008fb9e4) → `00ca5010`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb9e4`](#insn-008fb9e4) → `00ca5018`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb9e4`](#insn-008fb9e4) → `00ca5020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb9e8`](#insn-008fb9e8) → [`00c57f00`](../00c57/00c57f00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f00` · 推定シンボル `None` · 推定型 `None`
- [`008fb9f0`](#insn-008fb9f0) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb9f4`](#insn-008fb9f4) → [`00c57f40`](../00c57/00c57f40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f40` · 推定シンボル `None` · 推定型 `None`
- [`008fb9f8`](#insn-008fb9f8) → [`008fb2d8`](#insn-008fb2d8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fba00`](#insn-008fba00) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fba04`](#insn-008fba04) → [`00c57f20`](../00c57/00c57f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f20` · 推定シンボル `None` · 推定型 `None`
- [`008fba08`](#insn-008fba08) → [`008fb3e8`](#insn-008fb3e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fba14`](#insn-008fba14) → [`0047edf4`](../0047e/0047edf4.md) · `PARAM` · `ANALYSIS` · 関数 `0047edf4` · 推定シンボル `None` · 推定型 `None`
- [`008fba18`](#insn-008fba18) → `00ca5008`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fba20`](#insn-008fba20) → `00c63060`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008fba24`](#insn-008fba24) → `00ca5000`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fba24`](#insn-008fba24) → `00ca5008`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fba2c`](#insn-008fba2c) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fba30`](#insn-008fba30) → `00ca5028`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fba30`](#insn-008fba30) → `00ca5030`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fba34`](#insn-008fba34) → `00ca5020`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fba38`](#insn-008fba38) → `00ca5010`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fba38`](#insn-008fba38) → `00ca5018`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fba38`](#insn-008fba38) → `00ca5020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fba3c`](#insn-008fba3c) → [`00c57f00`](../00c57/00c57f00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f00` · 推定シンボル `None` · 推定型 `None`
- [`008fba44`](#insn-008fba44) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fba48`](#insn-008fba48) → [`00c57f40`](../00c57/00c57f40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f40` · 推定シンボル `None` · 推定型 `None`
- [`008fba4c`](#insn-008fba4c) → [`008fb3e8`](#insn-008fb3e8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fba54`](#insn-008fba54) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fba58`](#insn-008fba58) → [`00c57f20`](../00c57/00c57f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f20` · 推定シンボル `None` · 推定型 `None`
- [`008fba5c`](#insn-008fba5c) → [`008fb4f8`](#insn-008fb4f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fba68`](#insn-008fba68) → [`0047edf4`](../0047e/0047edf4.md) · `PARAM` · `ANALYSIS` · 関数 `0047edf4` · 推定シンボル `None` · 推定型 `None`
- [`008fba6c`](#insn-008fba6c) → `00ca5008`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fba74`](#insn-008fba74) → `00c63060`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008fba78`](#insn-008fba78) → `00ca5000`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fba78`](#insn-008fba78) → `00ca5008`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fba80`](#insn-008fba80) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fba84`](#insn-008fba84) → `00ca5028`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fba84`](#insn-008fba84) → `00ca5030`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fba88`](#insn-008fba88) → `00ca5020`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fba8c`](#insn-008fba8c) → `00ca5010`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fba8c`](#insn-008fba8c) → `00ca5018`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fba8c`](#insn-008fba8c) → `00ca5020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fba90`](#insn-008fba90) → [`00c57f00`](../00c57/00c57f00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f00` · 推定シンボル `None` · 推定型 `None`
- [`008fba98`](#insn-008fba98) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fba9c`](#insn-008fba9c) → [`00c57f40`](../00c57/00c57f40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f40` · 推定シンボル `None` · 推定型 `None`
- [`008fbaa0`](#insn-008fbaa0) → [`008fb4f8`](#insn-008fb4f8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fbaa8`](#insn-008fbaa8) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fbaac`](#insn-008fbaac) → [`00c57f20`](../00c57/00c57f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f20` · 推定シンボル `None` · 推定型 `None`
- [`008fbab0`](#insn-008fbab0) → [`008fb64c`](#insn-008fb64c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fbabc`](#insn-008fbabc) → [`0047edf4`](../0047e/0047edf4.md) · `PARAM` · `ANALYSIS` · 関数 `0047edf4` · 推定シンボル `None` · 推定型 `None`
- [`008fbac0`](#insn-008fbac0) → `00ca5008`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fbac8`](#insn-008fbac8) → `00c63060`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008fbacc`](#insn-008fbacc) → `00ca5000`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fbacc`](#insn-008fbacc) → `00ca5008`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fbad4`](#insn-008fbad4) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fbad8`](#insn-008fbad8) → `00ca5028`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fbad8`](#insn-008fbad8) → `00ca5030`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fbadc`](#insn-008fbadc) → `00ca5020`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fbae0`](#insn-008fbae0) → `00ca5010`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fbae0`](#insn-008fbae0) → `00ca5018`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fbae0`](#insn-008fbae0) → `00ca5020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fbae4`](#insn-008fbae4) → [`00c57f00`](../00c57/00c57f00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f00` · 推定シンボル `None` · 推定型 `None`
- [`008fbaec`](#insn-008fbaec) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fbaf0`](#insn-008fbaf0) → [`00c57f40`](../00c57/00c57f40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f40` · 推定シンボル `None` · 推定型 `None`
- [`008fbaf4`](#insn-008fbaf4) → [`008fb64c`](#insn-008fb64c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fbafc`](#insn-008fbafc) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fbb00`](#insn-008fbb00) → [`00c57f20`](../00c57/00c57f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f20` · 推定シンボル `None` · 推定型 `None`
- [`008fbb04`](#insn-008fbb04) → [`008fb788`](#insn-008fb788) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fbb10`](#insn-008fbb10) → [`0047edf4`](../0047e/0047edf4.md) · `PARAM` · `ANALYSIS` · 関数 `0047edf4` · 推定シンボル `None` · 推定型 `None`
- [`008fbb14`](#insn-008fbb14) → `00ca5008`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fbb1c`](#insn-008fbb1c) → `00c63060`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008fbb20`](#insn-008fbb20) → `00ca5000`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fbb20`](#insn-008fbb20) → `00ca5008`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fbb28`](#insn-008fbb28) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fbb2c`](#insn-008fbb2c) → `00ca5028`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fbb2c`](#insn-008fbb2c) → `00ca5030`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fbb30`](#insn-008fbb30) → `00ca5020`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fbb34`](#insn-008fbb34) → `00ca5010`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fbb34`](#insn-008fbb34) → `00ca5018`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fbb34`](#insn-008fbb34) → `00ca5020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fbb38`](#insn-008fbb38) → [`00c57f00`](../00c57/00c57f00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f00` · 推定シンボル `None` · 推定型 `None`
- [`008fbb40`](#insn-008fbb40) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fbb44`](#insn-008fbb44) → [`00c57f40`](../00c57/00c57f40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f40` · 推定シンボル `None` · 推定型 `None`
- [`008fbb48`](#insn-008fbb48) → [`008fb788`](#insn-008fb788) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fbbbc`](#insn-008fbbbc) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008faee0`](#insn-008faee0)

~~~json
{
  "source": "008faee0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faee4`](#insn-008faee4)

~~~json
{
  "source": "008faee4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faee8`](#insn-008faee8)

~~~json
{
  "source": "008faee8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faeec`](#insn-008faeec)

~~~json
{
  "source": "008faeec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faef0`](#insn-008faef0)

~~~json
{
  "source": "008faef0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf08`](#insn-008faf08)

~~~json
{
  "source": "008faf08",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf0c`](#insn-008faf0c)

~~~json
{
  "source": "008faf0c",
  "target": "00758228",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008faf20`](#insn-008faf20)

~~~json
{
  "source": "008faf20",
  "target": "00c85bc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c85bc8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008faf2c`](#insn-008faf2c)

~~~json
{
  "source": "008faf2c",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008faf30`](#insn-008faf30)

~~~json
{
  "source": "008faf30",
  "target": "008fb8a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf3c`](#insn-008faf3c)

~~~json
{
  "source": "008faf3c",
  "target": "Stack[-0x85]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf40`](#insn-008faf40)

~~~json
{
  "source": "008faf40",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf4c`](#insn-008faf4c)

~~~json
{
  "source": "008faf4c",
  "target": "002b63ce",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b63ce",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "696d673030362e706e6700",
  "capture_start": "002b63ce",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008faf50`](#insn-008faf50)

~~~json
{
  "source": "008faf50",
  "target": "Stack[-0x87]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf58`](#insn-008faf58)

~~~json
{
  "source": "008faf58",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf5c`](#insn-008faf5c)

~~~json
{
  "source": "008faf5c",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf68`](#insn-008faf68)

~~~json
{
  "source": "008faf68",
  "target": "002b1f47",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf6c`](#insn-008faf6c)

~~~json
{
  "source": "008faf6c",
  "target": "002b1f4c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b1f4c",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "362e696d6763757400",
  "capture_start": "002b1f4c",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008faf70`](#insn-008faf70)

~~~json
{
  "source": "008faf70",
  "target": "Stack[-0x9a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf74`](#insn-008faf74)

~~~json
{
  "source": "008faf74",
  "target": "Stack[-0xa7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf78`](#insn-008faf78)

~~~json
{
  "source": "008faf78",
  "target": "Stack[-0xa2]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf90`](#insn-008faf90)

~~~json
{
  "source": "008faf90",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008faf98`](#insn-008faf98)

~~~json
{
  "source": "008faf98",
  "target": "006333b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008faf9c`](#insn-008faf9c)

~~~json
{
  "source": "008faf9c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fafa4`](#insn-008fafa4)

~~~json
{
  "source": "008fafa4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fafac`](#insn-008fafac)

~~~json
{
  "source": "008fafac",
  "target": "008fafd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fafb8`](#insn-008fafb8)

~~~json
{
  "source": "008fafb8",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fafbc`](#insn-008fafbc)

~~~json
{
  "source": "008fafbc",
  "target": "008fafd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fafd4`](#insn-008fafd4)

~~~json
{
  "source": "008fafd4",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fafd8`](#insn-008fafd8)

~~~json
{
  "source": "008fafd8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fafdc`](#insn-008fafdc)

~~~json
{
  "source": "008fafdc",
  "target": "008faff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fafe8`](#insn-008fafe8)

~~~json
{
  "source": "008fafe8",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fafec`](#insn-008fafec)

~~~json
{
  "source": "008fafec",
  "target": "008fb160",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faff0`](#insn-008faff0)

~~~json
{
  "source": "008faff0",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faff4`](#insn-008faff4)

~~~json
{
  "source": "008faff4",
  "target": "008fb000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faff8`](#insn-008faff8)

~~~json
{
  "source": "008faff8",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faffc`](#insn-008faffc)

~~~json
{
  "source": "008faffc",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb000`](#insn-008fb000)

~~~json
{
  "source": "008fb000",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb004`](#insn-008fb004)

~~~json
{
  "source": "008fb004",
  "target": "008fb010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb008`](#insn-008fb008)

~~~json
{
  "source": "008fb008",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb00c`](#insn-008fb00c)

~~~json
{
  "source": "008fb00c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb018`](#insn-008fb018)

~~~json
{
  "source": "008fb018",
  "target": "00864590",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb01c`](#insn-008fb01c)

~~~json
{
  "source": "008fb01c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb024`](#insn-008fb024)

~~~json
{
  "source": "008fb024",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb02c`](#insn-008fb02c)

~~~json
{
  "source": "008fb02c",
  "target": "008fb058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb038`](#insn-008fb038)

~~~json
{
  "source": "008fb038",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb03c`](#insn-008fb03c)

~~~json
{
  "source": "008fb03c",
  "target": "008fb058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb054`](#insn-008fb054)

~~~json
{
  "source": "008fb054",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb058`](#insn-008fb058)

~~~json
{
  "source": "008fb058",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb05c`](#insn-008fb05c)

~~~json
{
  "source": "008fb05c",
  "target": "008fb088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb068`](#insn-008fb068)

~~~json
{
  "source": "008fb068",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb06c`](#insn-008fb06c)

~~~json
{
  "source": "008fb06c",
  "target": "008fb088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb084`](#insn-008fb084)

~~~json
{
  "source": "008fb084",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb088`](#insn-008fb088)

~~~json
{
  "source": "008fb088",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb08c`](#insn-008fb08c)

~~~json
{
  "source": "008fb08c",
  "target": "008fb900",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb098`](#insn-008fb098)

~~~json
{
  "source": "008fb098",
  "target": "Stack[-0x85]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb09c`](#insn-008fb09c)

~~~json
{
  "source": "008fb09c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb0a8`](#insn-008fb0a8)

~~~json
{
  "source": "008fb0a8",
  "target": "002bef6a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bef6a",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "696d673032342e706e6700",
  "capture_start": "002bef6a",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb0ac`](#insn-008fb0ac)

~~~json
{
  "source": "008fb0ac",
  "target": "Stack[-0x87]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb0b4`](#insn-008fb0b4)

~~~json
{
  "source": "008fb0b4",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb0b8`](#insn-008fb0b8)

~~~json
{
  "source": "008fb0b8",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb0c4`](#insn-008fb0c4)

~~~json
{
  "source": "008fb0c4",
  "target": "002a9f47",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb0c8`](#insn-008fb0c8)

~~~json
{
  "source": "008fb0c8",
  "target": "002a9f4c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a9f4c",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "342e696d6763757400",
  "capture_start": "002a9f4c",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb0cc`](#insn-008fb0cc)

~~~json
{
  "source": "008fb0cc",
  "target": "Stack[-0x9a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb0d0`](#insn-008fb0d0)

~~~json
{
  "source": "008fb0d0",
  "target": "Stack[-0xa7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb0d4`](#insn-008fb0d4)

~~~json
{
  "source": "008fb0d4",
  "target": "Stack[-0xa2]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb0e4`](#insn-008fb0e4)

~~~json
{
  "source": "008fb0e4",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb0ec`](#insn-008fb0ec)

~~~json
{
  "source": "008fb0ec",
  "target": "006333b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb0f0`](#insn-008fb0f0)

~~~json
{
  "source": "008fb0f0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb0f8`](#insn-008fb0f8)

~~~json
{
  "source": "008fb0f8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb100`](#insn-008fb100)

~~~json
{
  "source": "008fb100",
  "target": "008fb12c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb10c`](#insn-008fb10c)

~~~json
{
  "source": "008fb10c",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb110`](#insn-008fb110)

~~~json
{
  "source": "008fb110",
  "target": "008fb12c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb128`](#insn-008fb128)

~~~json
{
  "source": "008fb128",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb12c`](#insn-008fb12c)

~~~json
{
  "source": "008fb12c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb130`](#insn-008fb130)

~~~json
{
  "source": "008fb130",
  "target": "008fb144",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb13c`](#insn-008fb13c)

~~~json
{
  "source": "008fb13c",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb140`](#insn-008fb140)

~~~json
{
  "source": "008fb140",
  "target": "008fb184",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb144`](#insn-008fb144)

~~~json
{
  "source": "008fb144",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb148`](#insn-008fb148)

~~~json
{
  "source": "008fb148",
  "target": "008fb1a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb14c`](#insn-008fb14c)

~~~json
{
  "source": "008fb14c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb150`](#insn-008fb150)

~~~json
{
  "source": "008fb150",
  "target": "008fb1b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb154`](#insn-008fb154)

~~~json
{
  "source": "008fb154",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb158`](#insn-008fb158)

~~~json
{
  "source": "008fb158",
  "target": "008fb1c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb15c`](#insn-008fb15c)

~~~json
{
  "source": "008fb15c",
  "target": "008fb954",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb174`](#insn-008fb174)

~~~json
{
  "source": "008fb174",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb178`](#insn-008fb178)

~~~json
{
  "source": "008fb178",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb17c`](#insn-008fb17c)

~~~json
{
  "source": "008fb17c",
  "target": "008faff8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb180`](#insn-008fb180)

~~~json
{
  "source": "008fb180",
  "target": "008fb000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb198`](#insn-008fb198)

~~~json
{
  "source": "008fb198",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb19c`](#insn-008fb19c)

~~~json
{
  "source": "008fb19c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb1a0`](#insn-008fb1a0)

~~~json
{
  "source": "008fb1a0",
  "target": "008fb14c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb1a4`](#insn-008fb1a4)

~~~json
{
  "source": "008fb1a4",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb1a8`](#insn-008fb1a8)

~~~json
{
  "source": "008fb1a8",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb1ac`](#insn-008fb1ac)

~~~json
{
  "source": "008fb1ac",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb1b0`](#insn-008fb1b0)

~~~json
{
  "source": "008fb1b0",
  "target": "008fb154",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb1b4`](#insn-008fb1b4)

~~~json
{
  "source": "008fb1b4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb1b8`](#insn-008fb1b8)

~~~json
{
  "source": "008fb1b8",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb1bc`](#insn-008fb1bc)

~~~json
{
  "source": "008fb1bc",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb1c0`](#insn-008fb1c0)

~~~json
{
  "source": "008fb1c0",
  "target": "008fb954",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb1cc`](#insn-008fb1cc)

~~~json
{
  "source": "008fb1cc",
  "target": "Stack[-0x85]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb1d0`](#insn-008fb1d0)

~~~json
{
  "source": "008fb1d0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb1dc`](#insn-008fb1dc)

~~~json
{
  "source": "008fb1dc",
  "target": "002c0076",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c0076",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "696d673031362e706e6700",
  "capture_start": "002c0076",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb1e0`](#insn-008fb1e0)

~~~json
{
  "source": "008fb1e0",
  "target": "Stack[-0x87]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb1e8`](#insn-008fb1e8)

~~~json
{
  "source": "008fb1e8",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb1ec`](#insn-008fb1ec)

~~~json
{
  "source": "008fb1ec",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb1f8`](#insn-008fb1f8)

~~~json
{
  "source": "008fb1f8",
  "target": "002a9e9a",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb1fc`](#insn-008fb1fc)

~~~json
{
  "source": "008fb1fc",
  "target": "002a9e9f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a9e9f",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "362e696d6763757400",
  "capture_start": "002a9e9f",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb200`](#insn-008fb200)

~~~json
{
  "source": "008fb200",
  "target": "Stack[-0x9a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb204`](#insn-008fb204)

~~~json
{
  "source": "008fb204",
  "target": "Stack[-0xa7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb208`](#insn-008fb208)

~~~json
{
  "source": "008fb208",
  "target": "Stack[-0xa2]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb218`](#insn-008fb218)

~~~json
{
  "source": "008fb218",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb220`](#insn-008fb220)

~~~json
{
  "source": "008fb220",
  "target": "006333b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb224`](#insn-008fb224)

~~~json
{
  "source": "008fb224",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb230`](#insn-008fb230)

~~~json
{
  "source": "008fb230",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb238`](#insn-008fb238)

~~~json
{
  "source": "008fb238",
  "target": "008fb264",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb244`](#insn-008fb244)

~~~json
{
  "source": "008fb244",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb248`](#insn-008fb248)

~~~json
{
  "source": "008fb248",
  "target": "008fb264",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb260`](#insn-008fb260)

~~~json
{
  "source": "008fb260",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb264`](#insn-008fb264)

~~~json
{
  "source": "008fb264",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb268`](#insn-008fb268)

~~~json
{
  "source": "008fb268",
  "target": "008fb27c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb274`](#insn-008fb274)

~~~json
{
  "source": "008fb274",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb278`](#insn-008fb278)

~~~json
{
  "source": "008fb278",
  "target": "008fb298",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb27c`](#insn-008fb27c)

~~~json
{
  "source": "008fb27c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb280`](#insn-008fb280)

~~~json
{
  "source": "008fb280",
  "target": "008fb2b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb284`](#insn-008fb284)

~~~json
{
  "source": "008fb284",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb288`](#insn-008fb288)

~~~json
{
  "source": "008fb288",
  "target": "008fb2c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb28c`](#insn-008fb28c)

~~~json
{
  "source": "008fb28c",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb290`](#insn-008fb290)

~~~json
{
  "source": "008fb290",
  "target": "008fb2d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb294`](#insn-008fb294)

~~~json
{
  "source": "008fb294",
  "target": "008fb9a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb2ac`](#insn-008fb2ac)

~~~json
{
  "source": "008fb2ac",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb2b0`](#insn-008fb2b0)

~~~json
{
  "source": "008fb2b0",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb2b4`](#insn-008fb2b4)

~~~json
{
  "source": "008fb2b4",
  "target": "008fb284",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb2b8`](#insn-008fb2b8)

~~~json
{
  "source": "008fb2b8",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb2bc`](#insn-008fb2bc)

~~~json
{
  "source": "008fb2bc",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb2c0`](#insn-008fb2c0)

~~~json
{
  "source": "008fb2c0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb2c4`](#insn-008fb2c4)

~~~json
{
  "source": "008fb2c4",
  "target": "008fb28c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb2c8`](#insn-008fb2c8)

~~~json
{
  "source": "008fb2c8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb2cc`](#insn-008fb2cc)

~~~json
{
  "source": "008fb2cc",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb2d0`](#insn-008fb2d0)

~~~json
{
  "source": "008fb2d0",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb2d4`](#insn-008fb2d4)

~~~json
{
  "source": "008fb2d4",
  "target": "008fb9a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb2e0`](#insn-008fb2e0)

~~~json
{
  "source": "008fb2e0",
  "target": "Stack[-0x85]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb2e4`](#insn-008fb2e4)

~~~json
{
  "source": "008fb2e4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb2f0`](#insn-008fb2f0)

~~~json
{
  "source": "008fb2f0",
  "target": "002b91bb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b91bb",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "696d673031352e706e6700",
  "capture_start": "002b91bb",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb2f4`](#insn-008fb2f4)

~~~json
{
  "source": "008fb2f4",
  "target": "Stack[-0x87]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb2fc`](#insn-008fb2fc)

~~~json
{
  "source": "008fb2fc",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb300`](#insn-008fb300)

~~~json
{
  "source": "008fb300",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb30c`](#insn-008fb30c)

~~~json
{
  "source": "008fb30c",
  "target": "002bdbbb",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb310`](#insn-008fb310)

~~~json
{
  "source": "008fb310",
  "target": "002bdbc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bdbc0",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "352e696d6763757400",
  "capture_start": "002bdbc0",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb314`](#insn-008fb314)

~~~json
{
  "source": "008fb314",
  "target": "Stack[-0x9a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb318`](#insn-008fb318)

~~~json
{
  "source": "008fb318",
  "target": "Stack[-0xa7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb31c`](#insn-008fb31c)

~~~json
{
  "source": "008fb31c",
  "target": "Stack[-0xa2]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb32c`](#insn-008fb32c)

~~~json
{
  "source": "008fb32c",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb334`](#insn-008fb334)

~~~json
{
  "source": "008fb334",
  "target": "006333b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb338`](#insn-008fb338)

~~~json
{
  "source": "008fb338",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb340`](#insn-008fb340)

~~~json
{
  "source": "008fb340",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb348`](#insn-008fb348)

~~~json
{
  "source": "008fb348",
  "target": "008fb374",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb354`](#insn-008fb354)

~~~json
{
  "source": "008fb354",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb358`](#insn-008fb358)

~~~json
{
  "source": "008fb358",
  "target": "008fb374",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb370`](#insn-008fb370)

~~~json
{
  "source": "008fb370",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb374`](#insn-008fb374)

~~~json
{
  "source": "008fb374",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb378`](#insn-008fb378)

~~~json
{
  "source": "008fb378",
  "target": "008fb38c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb384`](#insn-008fb384)

~~~json
{
  "source": "008fb384",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb388`](#insn-008fb388)

~~~json
{
  "source": "008fb388",
  "target": "008fb3a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb38c`](#insn-008fb38c)

~~~json
{
  "source": "008fb38c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb390`](#insn-008fb390)

~~~json
{
  "source": "008fb390",
  "target": "008fb3c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb394`](#insn-008fb394)

~~~json
{
  "source": "008fb394",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb398`](#insn-008fb398)

~~~json
{
  "source": "008fb398",
  "target": "008fb3d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb39c`](#insn-008fb39c)

~~~json
{
  "source": "008fb39c",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb3a0`](#insn-008fb3a0)

~~~json
{
  "source": "008fb3a0",
  "target": "008fb3e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb3a4`](#insn-008fb3a4)

~~~json
{
  "source": "008fb3a4",
  "target": "008fb9fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb3bc`](#insn-008fb3bc)

~~~json
{
  "source": "008fb3bc",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb3c0`](#insn-008fb3c0)

~~~json
{
  "source": "008fb3c0",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb3c4`](#insn-008fb3c4)

~~~json
{
  "source": "008fb3c4",
  "target": "008fb394",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb3c8`](#insn-008fb3c8)

~~~json
{
  "source": "008fb3c8",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb3cc`](#insn-008fb3cc)

~~~json
{
  "source": "008fb3cc",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb3d0`](#insn-008fb3d0)

~~~json
{
  "source": "008fb3d0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb3d4`](#insn-008fb3d4)

~~~json
{
  "source": "008fb3d4",
  "target": "008fb39c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb3d8`](#insn-008fb3d8)

~~~json
{
  "source": "008fb3d8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb3dc`](#insn-008fb3dc)

~~~json
{
  "source": "008fb3dc",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb3e0`](#insn-008fb3e0)

~~~json
{
  "source": "008fb3e0",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb3e4`](#insn-008fb3e4)

~~~json
{
  "source": "008fb3e4",
  "target": "008fb9fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb3f0`](#insn-008fb3f0)

~~~json
{
  "source": "008fb3f0",
  "target": "Stack[-0x85]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb3f4`](#insn-008fb3f4)

~~~json
{
  "source": "008fb3f4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb400`](#insn-008fb400)

~~~json
{
  "source": "008fb400",
  "target": "0029f1f3",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029f1f3",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "696d673032312e706e6700",
  "capture_start": "0029f1f3",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb404`](#insn-008fb404)

~~~json
{
  "source": "008fb404",
  "target": "Stack[-0x87]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb40c`](#insn-008fb40c)

~~~json
{
  "source": "008fb40c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb410`](#insn-008fb410)

~~~json
{
  "source": "008fb410",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb41c`](#insn-008fb41c)

~~~json
{
  "source": "008fb41c",
  "target": "002c13b3",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb420`](#insn-008fb420)

~~~json
{
  "source": "008fb420",
  "target": "002c13b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c13b8",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "312e696d6763757400",
  "capture_start": "002c13b8",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb424`](#insn-008fb424)

~~~json
{
  "source": "008fb424",
  "target": "Stack[-0x9a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb428`](#insn-008fb428)

~~~json
{
  "source": "008fb428",
  "target": "Stack[-0xa7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb42c`](#insn-008fb42c)

~~~json
{
  "source": "008fb42c",
  "target": "Stack[-0xa2]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb43c`](#insn-008fb43c)

~~~json
{
  "source": "008fb43c",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb444`](#insn-008fb444)

~~~json
{
  "source": "008fb444",
  "target": "006333b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb448`](#insn-008fb448)

~~~json
{
  "source": "008fb448",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb450`](#insn-008fb450)

~~~json
{
  "source": "008fb450",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb458`](#insn-008fb458)

~~~json
{
  "source": "008fb458",
  "target": "008fb484",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb464`](#insn-008fb464)

~~~json
{
  "source": "008fb464",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb468`](#insn-008fb468)

~~~json
{
  "source": "008fb468",
  "target": "008fb484",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb480`](#insn-008fb480)

~~~json
{
  "source": "008fb480",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb484`](#insn-008fb484)

~~~json
{
  "source": "008fb484",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb488`](#insn-008fb488)

~~~json
{
  "source": "008fb488",
  "target": "008fb49c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb494`](#insn-008fb494)

~~~json
{
  "source": "008fb494",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb498`](#insn-008fb498)

~~~json
{
  "source": "008fb498",
  "target": "008fb4b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb49c`](#insn-008fb49c)

~~~json
{
  "source": "008fb49c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb4a0`](#insn-008fb4a0)

~~~json
{
  "source": "008fb4a0",
  "target": "008fb4d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb4a4`](#insn-008fb4a4)

~~~json
{
  "source": "008fb4a4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb4a8`](#insn-008fb4a8)

~~~json
{
  "source": "008fb4a8",
  "target": "008fb4e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb4ac`](#insn-008fb4ac)

~~~json
{
  "source": "008fb4ac",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb4b0`](#insn-008fb4b0)

~~~json
{
  "source": "008fb4b0",
  "target": "008fb4f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb4b4`](#insn-008fb4b4)

~~~json
{
  "source": "008fb4b4",
  "target": "008fba50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb4cc`](#insn-008fb4cc)

~~~json
{
  "source": "008fb4cc",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb4d0`](#insn-008fb4d0)

~~~json
{
  "source": "008fb4d0",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb4d4`](#insn-008fb4d4)

~~~json
{
  "source": "008fb4d4",
  "target": "008fb4a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb4d8`](#insn-008fb4d8)

~~~json
{
  "source": "008fb4d8",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb4dc`](#insn-008fb4dc)

~~~json
{
  "source": "008fb4dc",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb4e0`](#insn-008fb4e0)

~~~json
{
  "source": "008fb4e0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb4e4`](#insn-008fb4e4)

~~~json
{
  "source": "008fb4e4",
  "target": "008fb4ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb4e8`](#insn-008fb4e8)

~~~json
{
  "source": "008fb4e8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb4ec`](#insn-008fb4ec)

~~~json
{
  "source": "008fb4ec",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb4f0`](#insn-008fb4f0)

~~~json
{
  "source": "008fb4f0",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb4f4`](#insn-008fb4f4)

~~~json
{
  "source": "008fb4f4",
  "target": "008fba50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb500`](#insn-008fb500)

~~~json
{
  "source": "008fb500",
  "target": "Stack[-0x85]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb504`](#insn-008fb504)

~~~json
{
  "source": "008fb504",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb510`](#insn-008fb510)

~~~json
{
  "source": "008fb510",
  "target": "002b3eda",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b3eda",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "696d673032392e706e6700",
  "capture_start": "002b3eda",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb514`](#insn-008fb514)

~~~json
{
  "source": "008fb514",
  "target": "Stack[-0x87]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb51c`](#insn-008fb51c)

~~~json
{
  "source": "008fb51c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb520`](#insn-008fb520)

~~~json
{
  "source": "008fb520",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb52c`](#insn-008fb52c)

~~~json
{
  "source": "008fb52c",
  "target": "002b921c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb530`](#insn-008fb530)

~~~json
{
  "source": "008fb530",
  "target": "002b9221",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b9221",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "392e696d6763757400",
  "capture_start": "002b9221",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb534`](#insn-008fb534)

~~~json
{
  "source": "008fb534",
  "target": "Stack[-0x9a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb538`](#insn-008fb538)

~~~json
{
  "source": "008fb538",
  "target": "Stack[-0xa7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb53c`](#insn-008fb53c)

~~~json
{
  "source": "008fb53c",
  "target": "Stack[-0xa2]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb54c`](#insn-008fb54c)

~~~json
{
  "source": "008fb54c",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb554`](#insn-008fb554)

~~~json
{
  "source": "008fb554",
  "target": "006333b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb558`](#insn-008fb558)

~~~json
{
  "source": "008fb558",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb560`](#insn-008fb560)

~~~json
{
  "source": "008fb560",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb568`](#insn-008fb568)

~~~json
{
  "source": "008fb568",
  "target": "008fb594",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb574`](#insn-008fb574)

~~~json
{
  "source": "008fb574",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb578`](#insn-008fb578)

~~~json
{
  "source": "008fb578",
  "target": "008fb594",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb590`](#insn-008fb590)

~~~json
{
  "source": "008fb590",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb594`](#insn-008fb594)

~~~json
{
  "source": "008fb594",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb598`](#insn-008fb598)

~~~json
{
  "source": "008fb598",
  "target": "008fb5ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb5a4`](#insn-008fb5a4)

~~~json
{
  "source": "008fb5a4",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb5a8`](#insn-008fb5a8)

~~~json
{
  "source": "008fb5a8",
  "target": "008fb724",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb5ac`](#insn-008fb5ac)

~~~json
{
  "source": "008fb5ac",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb5b0`](#insn-008fb5b0)

~~~json
{
  "source": "008fb5b0",
  "target": "008fb5bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb5b4`](#insn-008fb5b4)

~~~json
{
  "source": "008fb5b4",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb5b8`](#insn-008fb5b8)

~~~json
{
  "source": "008fb5b8",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb5bc`](#insn-008fb5bc)

~~~json
{
  "source": "008fb5bc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb5c0`](#insn-008fb5c0)

~~~json
{
  "source": "008fb5c0",
  "target": "008fb5cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb5c4`](#insn-008fb5c4)

~~~json
{
  "source": "008fb5c4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb5c8`](#insn-008fb5c8)

~~~json
{
  "source": "008fb5c8",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb5d4`](#insn-008fb5d4)

~~~json
{
  "source": "008fb5d4",
  "target": "00862ca8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb5d8`](#insn-008fb5d8)

~~~json
{
  "source": "008fb5d8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb5e0`](#insn-008fb5e0)

~~~json
{
  "source": "008fb5e0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb5e8`](#insn-008fb5e8)

~~~json
{
  "source": "008fb5e8",
  "target": "008fb614",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb5f4`](#insn-008fb5f4)

~~~json
{
  "source": "008fb5f4",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb5f8`](#insn-008fb5f8)

~~~json
{
  "source": "008fb5f8",
  "target": "008fb614",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb610`](#insn-008fb610)

~~~json
{
  "source": "008fb610",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb614`](#insn-008fb614)

~~~json
{
  "source": "008fb614",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb618`](#insn-008fb618)

~~~json
{
  "source": "008fb618",
  "target": "008fb644",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb624`](#insn-008fb624)

~~~json
{
  "source": "008fb624",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb628`](#insn-008fb628)

~~~json
{
  "source": "008fb628",
  "target": "008fb644",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb640`](#insn-008fb640)

~~~json
{
  "source": "008fb640",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb644`](#insn-008fb644)

~~~json
{
  "source": "008fb644",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb648`](#insn-008fb648)

~~~json
{
  "source": "008fb648",
  "target": "008fbaa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb654`](#insn-008fb654)

~~~json
{
  "source": "008fb654",
  "target": "Stack[-0x85]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb658`](#insn-008fb658)

~~~json
{
  "source": "008fb658",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb664`](#insn-008fb664)

~~~json
{
  "source": "008fb664",
  "target": "002a450a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a450a",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "696d673130322e706e6700",
  "capture_start": "002a450a",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb668`](#insn-008fb668)

~~~json
{
  "source": "008fb668",
  "target": "Stack[-0x87]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb670`](#insn-008fb670)

~~~json
{
  "source": "008fb670",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb674`](#insn-008fb674)

~~~json
{
  "source": "008fb674",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb680`](#insn-008fb680)

~~~json
{
  "source": "008fb680",
  "target": "002bdbc9",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb684`](#insn-008fb684)

~~~json
{
  "source": "008fb684",
  "target": "002bdbce",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bdbce",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "322e696d6763757400",
  "capture_start": "002bdbce",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb688`](#insn-008fb688)

~~~json
{
  "source": "008fb688",
  "target": "Stack[-0x9a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb68c`](#insn-008fb68c)

~~~json
{
  "source": "008fb68c",
  "target": "Stack[-0xa7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb690`](#insn-008fb690)

~~~json
{
  "source": "008fb690",
  "target": "Stack[-0xa2]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb6a8`](#insn-008fb6a8)

~~~json
{
  "source": "008fb6a8",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb6b0`](#insn-008fb6b0)

~~~json
{
  "source": "008fb6b0",
  "target": "006333b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb6b4`](#insn-008fb6b4)

~~~json
{
  "source": "008fb6b4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb6bc`](#insn-008fb6bc)

~~~json
{
  "source": "008fb6bc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb6c4`](#insn-008fb6c4)

~~~json
{
  "source": "008fb6c4",
  "target": "008fb6f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb6d0`](#insn-008fb6d0)

~~~json
{
  "source": "008fb6d0",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb6d4`](#insn-008fb6d4)

~~~json
{
  "source": "008fb6d4",
  "target": "008fb6f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb6ec`](#insn-008fb6ec)

~~~json
{
  "source": "008fb6ec",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb6f0`](#insn-008fb6f0)

~~~json
{
  "source": "008fb6f0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb6f4`](#insn-008fb6f4)

~~~json
{
  "source": "008fb6f4",
  "target": "008fb708",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb700`](#insn-008fb700)

~~~json
{
  "source": "008fb700",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb704`](#insn-008fb704)

~~~json
{
  "source": "008fb704",
  "target": "008fb748",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb708`](#insn-008fb708)

~~~json
{
  "source": "008fb708",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb70c`](#insn-008fb70c)

~~~json
{
  "source": "008fb70c",
  "target": "008fb768",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb710`](#insn-008fb710)

~~~json
{
  "source": "008fb710",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb714`](#insn-008fb714)

~~~json
{
  "source": "008fb714",
  "target": "008fb778",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb718`](#insn-008fb718)

~~~json
{
  "source": "008fb718",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb71c`](#insn-008fb71c)

~~~json
{
  "source": "008fb71c",
  "target": "008fb788",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb720`](#insn-008fb720)

~~~json
{
  "source": "008fb720",
  "target": "008fbaf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb738`](#insn-008fb738)

~~~json
{
  "source": "008fb738",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb73c`](#insn-008fb73c)

~~~json
{
  "source": "008fb73c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb740`](#insn-008fb740)

~~~json
{
  "source": "008fb740",
  "target": "008fb5b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb744`](#insn-008fb744)

~~~json
{
  "source": "008fb744",
  "target": "008fb5bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb75c`](#insn-008fb75c)

~~~json
{
  "source": "008fb75c",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb760`](#insn-008fb760)

~~~json
{
  "source": "008fb760",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb764`](#insn-008fb764)

~~~json
{
  "source": "008fb764",
  "target": "008fb710",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb768`](#insn-008fb768)

~~~json
{
  "source": "008fb768",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb76c`](#insn-008fb76c)

~~~json
{
  "source": "008fb76c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb770`](#insn-008fb770)

~~~json
{
  "source": "008fb770",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb774`](#insn-008fb774)

~~~json
{
  "source": "008fb774",
  "target": "008fb718",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb778`](#insn-008fb778)

~~~json
{
  "source": "008fb778",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb77c`](#insn-008fb77c)

~~~json
{
  "source": "008fb77c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb780`](#insn-008fb780)

~~~json
{
  "source": "008fb780",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb784`](#insn-008fb784)

~~~json
{
  "source": "008fb784",
  "target": "008fbaf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb794`](#insn-008fb794)

~~~json
{
  "source": "008fb794",
  "target": "002a3471",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a3471",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "696d673035305f30322e706e6700",
  "capture_start": "002a3471",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb798`](#insn-008fb798)

~~~json
{
  "source": "008fb798",
  "target": "002a3476",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a3471",
  "offset": 5,
  "size": 14,
  "datatype": "string",
  "bytes": "696d673035305f30322e706e6700",
  "capture_start": "002a3471",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb79c`](#insn-008fb79c)

~~~json
{
  "source": "008fb79c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb7a4`](#insn-008fb7a4)

~~~json
{
  "source": "008fb7a4",
  "target": "Stack[-0x82]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb7a8`](#insn-008fb7a8)

~~~json
{
  "source": "008fb7a8",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb7ac`](#insn-008fb7ac)

~~~json
{
  "source": "008fb7ac",
  "target": "Stack[-0x8a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb7b8`](#insn-008fb7b8)

~~~json
{
  "source": "008fb7b8",
  "target": "002c034b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c034b",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "696d673035305f30322e696d6763757400",
  "capture_start": "002c034b",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb7bc`](#insn-008fb7bc)

~~~json
{
  "source": "008fb7bc",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb7c0`](#insn-008fb7c0)

~~~json
{
  "source": "008fb7c0",
  "target": "Stack[-0x97]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb7c4`](#insn-008fb7c4)

~~~json
{
  "source": "008fb7c4",
  "target": "Stack[-0xa7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb7cc`](#insn-008fb7cc)

~~~json
{
  "source": "008fb7cc",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb7e0`](#insn-008fb7e0)

~~~json
{
  "source": "008fb7e0",
  "target": "006333b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb7e4`](#insn-008fb7e4)

~~~json
{
  "source": "008fb7e4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb7ec`](#insn-008fb7ec)

~~~json
{
  "source": "008fb7ec",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb7f4`](#insn-008fb7f4)

~~~json
{
  "source": "008fb7f4",
  "target": "008fb820",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb800`](#insn-008fb800)

~~~json
{
  "source": "008fb800",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb804`](#insn-008fb804)

~~~json
{
  "source": "008fb804",
  "target": "008fb820",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb81c`](#insn-008fb81c)

~~~json
{
  "source": "008fb81c",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb820`](#insn-008fb820)

~~~json
{
  "source": "008fb820",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb824`](#insn-008fb824)

~~~json
{
  "source": "008fb824",
  "target": "008fb838",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb830`](#insn-008fb830)

~~~json
{
  "source": "008fb830",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb834`](#insn-008fb834)

~~~json
{
  "source": "008fb834",
  "target": "008fb884",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb838`](#insn-008fb838)

~~~json
{
  "source": "008fb838",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb83c`](#insn-008fb83c)

~~~json
{
  "source": "008fb83c",
  "target": "008fb848",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb840`](#insn-008fb840)

~~~json
{
  "source": "008fb840",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb844`](#insn-008fb844)

~~~json
{
  "source": "008fb844",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb848`](#insn-008fb848)

~~~json
{
  "source": "008fb848",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb84c`](#insn-008fb84c)

~~~json
{
  "source": "008fb84c",
  "target": "008fb858",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb850`](#insn-008fb850)

~~~json
{
  "source": "008fb850",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb854`](#insn-008fb854)

~~~json
{
  "source": "008fb854",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb85c`](#insn-008fb85c)

~~~json
{
  "source": "008fb85c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb864`](#insn-008fb864)

~~~json
{
  "source": "008fb864",
  "target": "008fbbbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb868`](#insn-008fb868)

~~~json
{
  "source": "008fb868",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb86c`](#insn-008fb86c)

~~~json
{
  "source": "008fb86c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb870`](#insn-008fb870)

~~~json
{
  "source": "008fb870",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb874`](#insn-008fb874)

~~~json
{
  "source": "008fb874",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb878`](#insn-008fb878)

~~~json
{
  "source": "008fb878",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb898`](#insn-008fb898)

~~~json
{
  "source": "008fb898",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb89c`](#insn-008fb89c)

~~~json
{
  "source": "008fb89c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb8a0`](#insn-008fb8a0)

~~~json
{
  "source": "008fb8a0",
  "target": "008fb840",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb8a4`](#insn-008fb8a4)

~~~json
{
  "source": "008fb8a4",
  "target": "008fb848",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb8ac`](#insn-008fb8ac)

~~~json
{
  "source": "008fb8ac",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb8b0`](#insn-008fb8b0)

~~~json
{
  "source": "008fb8b0",
  "target": "00c57f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb8b4`](#insn-008fb8b4)

~~~json
{
  "source": "008fb8b4",
  "target": "008faf34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb8bc`](#insn-008fb8bc)

~~~json
{
  "source": "008fb8bc",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb8c4`](#insn-008fb8c4)

~~~json
{
  "source": "008fb8c4",
  "target": "0047edf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb8d0`](#insn-008fb8d0)

~~~json
{
  "source": "008fb8d0",
  "target": "00c63060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c63060",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008fb8d4`](#insn-008fb8d4)

~~~json
{
  "source": "008fb8d4",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb8d8`](#insn-008fb8d8)

~~~json
{
  "source": "008fb8d8",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb8d8`](#insn-008fb8d8)

~~~json
{
  "source": "008fb8d8",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb8e0`](#insn-008fb8e0)

~~~json
{
  "source": "008fb8e0",
  "target": "00ca5028",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5028",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb8e0`](#insn-008fb8e0)

~~~json
{
  "source": "008fb8e0",
  "target": "00ca5030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb8e4`](#insn-008fb8e4)

~~~json
{
  "source": "008fb8e4",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb8e8`](#insn-008fb8e8)

~~~json
{
  "source": "008fb8e8",
  "target": "00ca5010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5010",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb8e8`](#insn-008fb8e8)

~~~json
{
  "source": "008fb8e8",
  "target": "00ca5018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5018",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb8e8`](#insn-008fb8e8)

~~~json
{
  "source": "008fb8e8",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb8ec`](#insn-008fb8ec)

~~~json
{
  "source": "008fb8ec",
  "target": "00c57f00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb8f4`](#insn-008fb8f4)

~~~json
{
  "source": "008fb8f4",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb8f8`](#insn-008fb8f8)

~~~json
{
  "source": "008fb8f8",
  "target": "00c57f40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb8fc`](#insn-008fb8fc)

~~~json
{
  "source": "008fb8fc",
  "target": "008faf34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb904`](#insn-008fb904)

~~~json
{
  "source": "008fb904",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb908`](#insn-008fb908)

~~~json
{
  "source": "008fb908",
  "target": "00c57f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb90c`](#insn-008fb90c)

~~~json
{
  "source": "008fb90c",
  "target": "008fb090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb918`](#insn-008fb918)

~~~json
{
  "source": "008fb918",
  "target": "0047edf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb91c`](#insn-008fb91c)

~~~json
{
  "source": "008fb91c",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb924`](#insn-008fb924)

~~~json
{
  "source": "008fb924",
  "target": "00c63060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c63060",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008fb928`](#insn-008fb928)

~~~json
{
  "source": "008fb928",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb928`](#insn-008fb928)

~~~json
{
  "source": "008fb928",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb930`](#insn-008fb930)

~~~json
{
  "source": "008fb930",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb934`](#insn-008fb934)

~~~json
{
  "source": "008fb934",
  "target": "00ca5028",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5028",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb934`](#insn-008fb934)

~~~json
{
  "source": "008fb934",
  "target": "00ca5030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb938`](#insn-008fb938)

~~~json
{
  "source": "008fb938",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb93c`](#insn-008fb93c)

~~~json
{
  "source": "008fb93c",
  "target": "00ca5010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5010",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb93c`](#insn-008fb93c)

~~~json
{
  "source": "008fb93c",
  "target": "00ca5018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5018",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb93c`](#insn-008fb93c)

~~~json
{
  "source": "008fb93c",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb940`](#insn-008fb940)

~~~json
{
  "source": "008fb940",
  "target": "00c57f00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb948`](#insn-008fb948)

~~~json
{
  "source": "008fb948",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb94c`](#insn-008fb94c)

~~~json
{
  "source": "008fb94c",
  "target": "00c57f40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb950`](#insn-008fb950)

~~~json
{
  "source": "008fb950",
  "target": "008fb090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb958`](#insn-008fb958)

~~~json
{
  "source": "008fb958",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb95c`](#insn-008fb95c)

~~~json
{
  "source": "008fb95c",
  "target": "00c57f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb960`](#insn-008fb960)

~~~json
{
  "source": "008fb960",
  "target": "008fb1c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb96c`](#insn-008fb96c)

~~~json
{
  "source": "008fb96c",
  "target": "0047edf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb970`](#insn-008fb970)

~~~json
{
  "source": "008fb970",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb978`](#insn-008fb978)

~~~json
{
  "source": "008fb978",
  "target": "00c63060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c63060",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008fb97c`](#insn-008fb97c)

~~~json
{
  "source": "008fb97c",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb97c`](#insn-008fb97c)

~~~json
{
  "source": "008fb97c",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb984`](#insn-008fb984)

~~~json
{
  "source": "008fb984",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb988`](#insn-008fb988)

~~~json
{
  "source": "008fb988",
  "target": "00ca5028",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5028",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb988`](#insn-008fb988)

~~~json
{
  "source": "008fb988",
  "target": "00ca5030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb98c`](#insn-008fb98c)

~~~json
{
  "source": "008fb98c",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb990`](#insn-008fb990)

~~~json
{
  "source": "008fb990",
  "target": "00ca5010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5010",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb990`](#insn-008fb990)

~~~json
{
  "source": "008fb990",
  "target": "00ca5018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5018",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb990`](#insn-008fb990)

~~~json
{
  "source": "008fb990",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb994`](#insn-008fb994)

~~~json
{
  "source": "008fb994",
  "target": "00c57f00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb99c`](#insn-008fb99c)

~~~json
{
  "source": "008fb99c",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb9a0`](#insn-008fb9a0)

~~~json
{
  "source": "008fb9a0",
  "target": "00c57f40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb9a4`](#insn-008fb9a4)

~~~json
{
  "source": "008fb9a4",
  "target": "008fb1c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb9ac`](#insn-008fb9ac)

~~~json
{
  "source": "008fb9ac",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb9b0`](#insn-008fb9b0)

~~~json
{
  "source": "008fb9b0",
  "target": "00c57f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb9b4`](#insn-008fb9b4)

~~~json
{
  "source": "008fb9b4",
  "target": "008fb2d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb9c0`](#insn-008fb9c0)

~~~json
{
  "source": "008fb9c0",
  "target": "0047edf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb9c4`](#insn-008fb9c4)

~~~json
{
  "source": "008fb9c4",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb9cc`](#insn-008fb9cc)

~~~json
{
  "source": "008fb9cc",
  "target": "00c63060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c63060",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008fb9d0`](#insn-008fb9d0)

~~~json
{
  "source": "008fb9d0",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb9d0`](#insn-008fb9d0)

~~~json
{
  "source": "008fb9d0",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb9d8`](#insn-008fb9d8)

~~~json
{
  "source": "008fb9d8",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb9dc`](#insn-008fb9dc)

~~~json
{
  "source": "008fb9dc",
  "target": "00ca5028",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5028",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb9dc`](#insn-008fb9dc)

~~~json
{
  "source": "008fb9dc",
  "target": "00ca5030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb9e0`](#insn-008fb9e0)

~~~json
{
  "source": "008fb9e0",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb9e4`](#insn-008fb9e4)

~~~json
{
  "source": "008fb9e4",
  "target": "00ca5010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5010",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb9e4`](#insn-008fb9e4)

~~~json
{
  "source": "008fb9e4",
  "target": "00ca5018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5018",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb9e4`](#insn-008fb9e4)

~~~json
{
  "source": "008fb9e4",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb9e8`](#insn-008fb9e8)

~~~json
{
  "source": "008fb9e8",
  "target": "00c57f00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb9f0`](#insn-008fb9f0)

~~~json
{
  "source": "008fb9f0",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fb9f4`](#insn-008fb9f4)

~~~json
{
  "source": "008fb9f4",
  "target": "00c57f40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb9f8`](#insn-008fb9f8)

~~~json
{
  "source": "008fb9f8",
  "target": "008fb2d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fba00`](#insn-008fba00)

~~~json
{
  "source": "008fba00",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fba04`](#insn-008fba04)

~~~json
{
  "source": "008fba04",
  "target": "00c57f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fba08`](#insn-008fba08)

~~~json
{
  "source": "008fba08",
  "target": "008fb3e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fba14`](#insn-008fba14)

~~~json
{
  "source": "008fba14",
  "target": "0047edf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fba18`](#insn-008fba18)

~~~json
{
  "source": "008fba18",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fba20`](#insn-008fba20)

~~~json
{
  "source": "008fba20",
  "target": "00c63060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c63060",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008fba24`](#insn-008fba24)

~~~json
{
  "source": "008fba24",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fba24`](#insn-008fba24)

~~~json
{
  "source": "008fba24",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fba2c`](#insn-008fba2c)

~~~json
{
  "source": "008fba2c",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fba30`](#insn-008fba30)

~~~json
{
  "source": "008fba30",
  "target": "00ca5028",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5028",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fba30`](#insn-008fba30)

~~~json
{
  "source": "008fba30",
  "target": "00ca5030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fba34`](#insn-008fba34)

~~~json
{
  "source": "008fba34",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fba38`](#insn-008fba38)

~~~json
{
  "source": "008fba38",
  "target": "00ca5010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5010",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fba38`](#insn-008fba38)

~~~json
{
  "source": "008fba38",
  "target": "00ca5018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5018",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fba38`](#insn-008fba38)

~~~json
{
  "source": "008fba38",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fba3c`](#insn-008fba3c)

~~~json
{
  "source": "008fba3c",
  "target": "00c57f00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fba44`](#insn-008fba44)

~~~json
{
  "source": "008fba44",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fba48`](#insn-008fba48)

~~~json
{
  "source": "008fba48",
  "target": "00c57f40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fba4c`](#insn-008fba4c)

~~~json
{
  "source": "008fba4c",
  "target": "008fb3e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fba54`](#insn-008fba54)

~~~json
{
  "source": "008fba54",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fba58`](#insn-008fba58)

~~~json
{
  "source": "008fba58",
  "target": "00c57f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fba5c`](#insn-008fba5c)

~~~json
{
  "source": "008fba5c",
  "target": "008fb4f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fba68`](#insn-008fba68)

~~~json
{
  "source": "008fba68",
  "target": "0047edf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fba6c`](#insn-008fba6c)

~~~json
{
  "source": "008fba6c",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fba74`](#insn-008fba74)

~~~json
{
  "source": "008fba74",
  "target": "00c63060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c63060",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008fba78`](#insn-008fba78)

~~~json
{
  "source": "008fba78",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fba78`](#insn-008fba78)

~~~json
{
  "source": "008fba78",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fba80`](#insn-008fba80)

~~~json
{
  "source": "008fba80",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fba84`](#insn-008fba84)

~~~json
{
  "source": "008fba84",
  "target": "00ca5028",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5028",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fba84`](#insn-008fba84)

~~~json
{
  "source": "008fba84",
  "target": "00ca5030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fba88`](#insn-008fba88)

~~~json
{
  "source": "008fba88",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fba8c`](#insn-008fba8c)

~~~json
{
  "source": "008fba8c",
  "target": "00ca5010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5010",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fba8c`](#insn-008fba8c)

~~~json
{
  "source": "008fba8c",
  "target": "00ca5018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5018",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fba8c`](#insn-008fba8c)

~~~json
{
  "source": "008fba8c",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fba90`](#insn-008fba90)

~~~json
{
  "source": "008fba90",
  "target": "00c57f00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fba98`](#insn-008fba98)

~~~json
{
  "source": "008fba98",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fba9c`](#insn-008fba9c)

~~~json
{
  "source": "008fba9c",
  "target": "00c57f40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fbaa0`](#insn-008fbaa0)

~~~json
{
  "source": "008fbaa0",
  "target": "008fb4f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fbaa8`](#insn-008fbaa8)

~~~json
{
  "source": "008fbaa8",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fbaac`](#insn-008fbaac)

~~~json
{
  "source": "008fbaac",
  "target": "00c57f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fbab0`](#insn-008fbab0)

~~~json
{
  "source": "008fbab0",
  "target": "008fb64c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fbabc`](#insn-008fbabc)

~~~json
{
  "source": "008fbabc",
  "target": "0047edf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fbac0`](#insn-008fbac0)

~~~json
{
  "source": "008fbac0",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fbac8`](#insn-008fbac8)

~~~json
{
  "source": "008fbac8",
  "target": "00c63060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c63060",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008fbacc`](#insn-008fbacc)

~~~json
{
  "source": "008fbacc",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fbacc`](#insn-008fbacc)

~~~json
{
  "source": "008fbacc",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fbad4`](#insn-008fbad4)

~~~json
{
  "source": "008fbad4",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fbad8`](#insn-008fbad8)

~~~json
{
  "source": "008fbad8",
  "target": "00ca5028",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5028",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fbad8`](#insn-008fbad8)

~~~json
{
  "source": "008fbad8",
  "target": "00ca5030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fbadc`](#insn-008fbadc)

~~~json
{
  "source": "008fbadc",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fbae0`](#insn-008fbae0)

~~~json
{
  "source": "008fbae0",
  "target": "00ca5010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5010",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fbae0`](#insn-008fbae0)

~~~json
{
  "source": "008fbae0",
  "target": "00ca5018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5018",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fbae0`](#insn-008fbae0)

~~~json
{
  "source": "008fbae0",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fbae4`](#insn-008fbae4)

~~~json
{
  "source": "008fbae4",
  "target": "00c57f00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fbaec`](#insn-008fbaec)

~~~json
{
  "source": "008fbaec",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fbaf0`](#insn-008fbaf0)

~~~json
{
  "source": "008fbaf0",
  "target": "00c57f40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fbaf4`](#insn-008fbaf4)

~~~json
{
  "source": "008fbaf4",
  "target": "008fb64c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fbafc`](#insn-008fbafc)

~~~json
{
  "source": "008fbafc",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fbb00`](#insn-008fbb00)

~~~json
{
  "source": "008fbb00",
  "target": "00c57f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fbb04`](#insn-008fbb04)

~~~json
{
  "source": "008fbb04",
  "target": "008fb788",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fbb10`](#insn-008fbb10)

~~~json
{
  "source": "008fbb10",
  "target": "0047edf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fbb14`](#insn-008fbb14)

~~~json
{
  "source": "008fbb14",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fbb1c`](#insn-008fbb1c)

~~~json
{
  "source": "008fbb1c",
  "target": "00c63060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c63060",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008fbb20`](#insn-008fbb20)

~~~json
{
  "source": "008fbb20",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fbb20`](#insn-008fbb20)

~~~json
{
  "source": "008fbb20",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fbb28`](#insn-008fbb28)

~~~json
{
  "source": "008fbb28",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fbb2c`](#insn-008fbb2c)

~~~json
{
  "source": "008fbb2c",
  "target": "00ca5028",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5028",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fbb2c`](#insn-008fbb2c)

~~~json
{
  "source": "008fbb2c",
  "target": "00ca5030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fbb30`](#insn-008fbb30)

~~~json
{
  "source": "008fbb30",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fbb34`](#insn-008fbb34)

~~~json
{
  "source": "008fbb34",
  "target": "00ca5010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5010",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fbb34`](#insn-008fbb34)

~~~json
{
  "source": "008fbb34",
  "target": "00ca5018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5018",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fbb34`](#insn-008fbb34)

~~~json
{
  "source": "008fbb34",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fbb38`](#insn-008fbb38)

~~~json
{
  "source": "008fbb38",
  "target": "00c57f00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fbb40`](#insn-008fbb40)

~~~json
{
  "source": "008fbb40",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008fbb44`](#insn-008fbb44)

~~~json
{
  "source": "008fbb44",
  "target": "00c57f40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fbb48`](#insn-008fbb48)

~~~json
{
  "source": "008fbb48",
  "target": "008fb788",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fbbbc`](#insn-008fbbbc)

~~~json
{
  "source": "008fbbbc",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
