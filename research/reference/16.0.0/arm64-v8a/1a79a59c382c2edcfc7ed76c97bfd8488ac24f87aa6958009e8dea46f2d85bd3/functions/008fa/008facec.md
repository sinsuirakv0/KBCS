# 008facec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `008c6e18`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c6/008c6e18.md) · 移動量 `+0x33ed4`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0045.md#compare-d819b08d99c02c98e9059cb823a88912)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `008fae88`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fa/008fae88.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0052.md#compare-146833bf0435df084d3afabc45d6844e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008facec",
  "name": "FUN_008facec",
  "size": 3188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d4b3c95d9ae1cc12d887c621a254ce31fbf9b2a0560f70a849092eacaabbb2a4",
  "source_text_sha256": "d4b3c95d9ae1cc12d887c621a254ce31fbf9b2a0560f70a849092eacaabbb2a4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008facec",
        "008fb95b"
      ],
      [
        "008fb9cc",
        "008fb9cf"
      ]
    ],
    "bytes_sha256": "000d200b895af171cb3e326489961f30bc3ebf16eaf873d7d7ca375b6ade6b5d",
    "instruction_count": 797,
    "instruction_bytes": 3188,
    "body_bytes": 3188,
    "indirect": 20,
    "unresolved": 20
  }
}
~~~

## 呼び出し元

- [008f65c8](../008f6/008f65c8.md)

## 呼び出し先

- [00633334](../00633/00633334.md)
- [00758190](../00758/00758190.md)
- [00862c10](../00862/00862c10.md)
- [008644f8](../00864/008644f8.md)
- [00c538e0](../00c53/00c538e0.md)
- [00c57a30](../00c57/00c57a30.md)
- [00c57a50](../00c57/00c57a50.md)
- [00c57a70](../00c57/00c57a70.md)
- [00c57a80](../00c57/00c57a80.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)

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

## 疑似コード / UTF-8 19716 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */
/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_008facec(undefined8 *param_1,undefined8 param_2)

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
  
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  FUN_00758190();
  *param_1 = &PTR_FUN_00c856f8;
  *(undefined1 *)(param_1 + 0x5e) = 1;
  if (((DAT_00ca4b38 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca4b38), iVar4 != 0)) {
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
  cStack_85 = 0;
  local_90 = 0x14;
  uStack_87 = 0x676e;
  local_a8 = 0x1a;
  uStack_8f = (undefined5)s_img006_png_002b634e._0_8_;
  uStack_8a = SUB82(s_img006_png_002b634e._0_8_,5);
  cStack_88 = SUB81(s_img006_png_002b634e._0_8_,7);
  cStack_9a = 0;
  local_a7 = _DAT_002b1ed6;
  uStack_a2._0_1_ = s_6_imgcut_002b1edb[0];
  uStack_a2._1_1_ = s_6_imgcut_002b1edb[1];
  uStack_a2._2_1_ = s_6_imgcut_002b1edb[2];
  uStack_9f._0_1_ = s_6_imgcut_002b1edb[3];
  uStack_9f._1_1_ = s_6_imgcut_002b1edb[4];
  uStack_9f._2_1_ = s_6_imgcut_002b1edb[5];
  uStack_9f._3_1_ = s_6_imgcut_002b1edb[6];
  uStack_9f._4_1_ = s_6_imgcut_002b1edb[7];
                    /* try { // try from 008fada0 to 009fadab has its CatchHandler @ 008fae3c */
  FUN_00633334(&local_70,&DAT_00ca4b00,&local_90,&local_a8,0x2601);
  plVar7 = plStack_68;
  uVar2 = local_70;
  plVar6 = (long *)param_1[0x16];
  local_70 = 0;
  plStack_68 = (long *)0x0;
  param_1[0x16] = plVar7;
  param_1[0x15] = uVar2;
                    /* try { // try from 008fadc4 to 009fade7 has its CatchHandler @ 008fae4c */
  if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00c538e0(0xffffffffffffffff,plVar6 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar6 + 0x10))(plVar6);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
  }
                    /* try { // try from 008fade8 to 009faed3 has its CatchHandler @ 008fa950 */
  plVar7 = plStack_68;
  if ((plStack_68 != (long *)0x0) &&
     (lVar5 = FUN_00c538e0(0xffffffffffffffff,plStack_68 + 1), lVar5 == 0)) {
    (**(code **)(*plVar7 + 0x10))(plVar7);
                    /* try { // try from 008faf84 to 009fb0d3 has its CatchHandler @ 008faefc */
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
  }
  if ((local_a8 & 1) != 0) {
    _ZdlPv((void *)CONCAT62(uStack_96,CONCAT11(uStack_97,cStack_98)));
  }
  if ((local_90 & 1) != 0) {
    _ZdlPv(local_80);
  }
  FUN_008644f8(&local_90,param_2);
  uVar3 = CONCAT17(uStack_81,
                   CONCAT16(uStack_82,
                            CONCAT24(uStack_84,CONCAT13(cStack_85,CONCAT21(uStack_87,cStack_88)))));
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
                    /* catch() { ... } // from try @ 008fada0 with catch @ 008fae3c */
                    /* catch() { ... } // from try @ 008fadc4 with catch @ 008fae4c */
  if ((plVar7 != (long *)0x0) && (lVar5 = FUN_00c538e0(0xffffffffffffffff,plVar7 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
  }
  plVar7 = (long *)CONCAT17(uStack_81,
                            CONCAT16(uStack_82,
                                     CONCAT24(uStack_84,
                                              CONCAT13(cStack_85,CONCAT21(uStack_87,cStack_88)))));
  if ((plVar7 != (long *)0x0) && (lVar5 = FUN_00c538e0(0xffffffffffffffff,plVar7 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
  }
  if (((DAT_00ca4b38 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca4b38), iVar4 != 0)) {
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
  cStack_85 = 0;
  local_90 = 0x14;
  uStack_87 = 0x676e;
  local_a8 = 0x1a;
  uStack_8f = (undefined5)s_img024_png_002bef7e._0_8_;
  uStack_8a = SUB82(s_img024_png_002bef7e._0_8_,5);
  cStack_88 = SUB81(s_img024_png_002bef7e._0_8_,7);
  cStack_9a = 0;
  local_a7 = _DAT_002a9ed6;
  uStack_a2._0_1_ = s_4_imgcut_002a9edb[0];
  uStack_a2._1_1_ = s_4_imgcut_002a9edb[1];
  uStack_a2._2_1_ = s_4_imgcut_002a9edb[2];
  uStack_9f._0_1_ = s_4_imgcut_002a9edb[3];
  uStack_9f._1_1_ = s_4_imgcut_002a9edb[4];
  uStack_9f._2_1_ = s_4_imgcut_002a9edb[5];
  uStack_9f._3_1_ = s_4_imgcut_002a9edb[6];
  uStack_9f._4_1_ = s_4_imgcut_002a9edb[7];
                    /* try { // try from 008faefc to 009faf57 has its CatchHandler @ 008faefc
                       catch() { ... } // from try @ 008faefc with catch @ 008faefc
                       catch() { ... } // from try @ 008faf84 with catch @ 008faefc */
  FUN_00633334(&local_70,&DAT_00ca4b00,&local_90,&local_a8,0x2601);
  plVar7 = plStack_68;
  uVar2 = local_70;
  plVar6 = (long *)param_1[0x20];
  local_70 = 0;
  plStack_68 = (long *)0x0;
  param_1[0x20] = plVar7;
  param_1[0x1f] = uVar2;
  if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00c538e0(0xffffffffffffffff,plVar6 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar6 + 0x10))(plVar6);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
  }
  plVar7 = plStack_68;
  if ((plStack_68 != (long *)0x0) &&
     (lVar5 = FUN_00c538e0(0xffffffffffffffff,plStack_68 + 1), lVar5 == 0)) {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
  }
                    /* try { // try from 008faf58 to 009faf83 has its CatchHandler @ 008fb0a4 */
  if ((local_a8 & 1) != 0) {
    _ZdlPv((void *)CONCAT62(uStack_96,CONCAT11(uStack_97,cStack_98)));
  }
  if ((local_90 & 1) != 0) {
    _ZdlPv(local_80);
  }
  if (((DAT_00ca4b38 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca4b38), iVar4 != 0)) {
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
  cStack_85 = 0;
  local_90 = 0x14;
  uStack_87 = 0x676e;
  local_a8 = 0x1a;
  uStack_8f = (undefined5)s_img016_png_002bfff6._0_8_;
  uStack_8a = SUB82(s_img016_png_002bfff6._0_8_,5);
  cStack_88 = SUB81(s_img016_png_002bfff6._0_8_,7);
  cStack_9a = 0;
  local_a7 = _DAT_002a9e29;
  uStack_a2._0_1_ = s_6_imgcut_002a9e2e[0];
  uStack_a2._1_1_ = s_6_imgcut_002a9e2e[1];
  uStack_a2._2_1_ = s_6_imgcut_002a9e2e[2];
  uStack_9f._0_1_ = s_6_imgcut_002a9e2e[3];
  uStack_9f._1_1_ = s_6_imgcut_002a9e2e[4];
  uStack_9f._2_1_ = s_6_imgcut_002a9e2e[5];
  uStack_9f._3_1_ = s_6_imgcut_002a9e2e[6];
  uStack_9f._4_1_ = s_6_imgcut_002a9e2e[7];
  FUN_00633334(&local_70,&DAT_00ca4b00,&local_90,&local_a8,0x2601);
  plVar7 = plStack_68;
  uVar2 = local_70;
  plVar6 = (long *)param_1[0x24];
  local_70 = 0;
  plStack_68 = (long *)0x0;
  param_1[0x24] = plVar7;
  param_1[0x23] = uVar2;
  if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00c538e0(0xffffffffffffffff,plVar6 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar6 + 0x10))(plVar6);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
  }
  plVar7 = plStack_68;
  if ((plStack_68 != (long *)0x0) &&
     (lVar5 = FUN_00c538e0(0xffffffffffffffff,plStack_68 + 1), lVar5 == 0)) {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
  }
  if ((local_a8 & 1) != 0) {
    _ZdlPv((void *)CONCAT62(uStack_96,CONCAT11(uStack_97,cStack_98)));
  }
  if ((local_90 & 1) != 0) {
    _ZdlPv(local_80);
  }
  if (((DAT_00ca4b38 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca4b38), iVar4 != 0)) {
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
  cStack_85 = 0;
  local_90 = 0x14;
  uStack_87 = 0x676e;
  local_a8 = 0x1a;
  uStack_8f = (undefined5)s_img015_png_002b91cf._0_8_;
  uStack_8a = SUB82(s_img015_png_002b91cf._0_8_,5);
  cStack_88 = SUB81(s_img015_png_002b91cf._0_8_,7);
  cStack_9a = 0;
  local_a7 = _DAT_002bdbcf;
  uStack_a2._0_1_ = s_5_imgcut_002bdbd4[0];
  uStack_a2._1_1_ = s_5_imgcut_002bdbd4[1];
  uStack_a2._2_1_ = s_5_imgcut_002bdbd4[2];
  uStack_9f._0_1_ = s_5_imgcut_002bdbd4[3];
  uStack_9f._1_1_ = s_5_imgcut_002bdbd4[4];
  uStack_9f._2_1_ = s_5_imgcut_002bdbd4[5];
  uStack_9f._3_1_ = s_5_imgcut_002bdbd4[6];
  uStack_9f._4_1_ = s_5_imgcut_002bdbd4[7];
  FUN_00633334(&local_70,&DAT_00ca4b00,&local_90,&local_a8,0x2601);
  plVar7 = plStack_68;
  uVar2 = local_70;
  plVar6 = (long *)param_1[0x26];
  local_70 = 0;
  plStack_68 = (long *)0x0;
  param_1[0x26] = plVar7;
  param_1[0x25] = uVar2;
  if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00c538e0(0xffffffffffffffff,plVar6 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar6 + 0x10))(plVar6);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
  }
  plVar7 = plStack_68;
  if ((plStack_68 != (long *)0x0) &&
     (lVar5 = FUN_00c538e0(0xffffffffffffffff,plStack_68 + 1), lVar5 == 0)) {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
  }
  if ((local_a8 & 1) != 0) {
    _ZdlPv((void *)CONCAT62(uStack_96,CONCAT11(uStack_97,cStack_98)));
  }
  if ((local_90 & 1) != 0) {
    _ZdlPv(local_80);
  }
  if (((DAT_00ca4b38 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca4b38), iVar4 != 0)) {
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
  cStack_85 = 0;
  local_90 = 0x14;
  uStack_87 = 0x676e;
  local_a8 = 0x1a;
  uStack_8f = (undefined5)s_img021_png_0029f173._0_8_;
  uStack_8a = SUB82(s_img021_png_0029f173._0_8_,5);
  cStack_88 = SUB81(s_img021_png_0029f173._0_8_,7);
  cStack_9a = 0;
  local_a7 = _DAT_002c1333;
  uStack_a2._0_1_ = s_1_imgcut_002c1338[0];
  uStack_a2._1_1_ = s_1_imgcut_002c1338[1];
  uStack_a2._2_1_ = s_1_imgcut_002c1338[2];
  uStack_9f._0_1_ = s_1_imgcut_002c1338[3];
  uStack_9f._1_1_ = s_1_imgcut_002c1338[4];
  uStack_9f._2_1_ = s_1_imgcut_002c1338[5];
  uStack_9f._3_1_ = s_1_imgcut_002c1338[6];
  uStack_9f._4_1_ = s_1_imgcut_002c1338[7];
  FUN_00633334(&local_70,&DAT_00ca4b00,&local_90,&local_a8,0x2601);
  plVar7 = plStack_68;
  uVar2 = local_70;
  plVar6 = (long *)param_1[0x28];
  local_70 = 0;
  plStack_68 = (long *)0x0;
  param_1[0x28] = plVar7;
  param_1[0x27] = uVar2;
  if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00c538e0(0xffffffffffffffff,plVar6 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar6 + 0x10))(plVar6);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
  }
  plVar7 = plStack_68;
  if ((plStack_68 != (long *)0x0) &&
     (lVar5 = FUN_00c538e0(0xffffffffffffffff,plStack_68 + 1), lVar5 == 0)) {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
  }
  if ((local_a8 & 1) != 0) {
    _ZdlPv((void *)CONCAT62(uStack_96,CONCAT11(uStack_97,cStack_98)));
  }
  if ((local_90 & 1) != 0) {
    _ZdlPv(local_80);
  }
  if (((DAT_00ca4b38 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca4b38), iVar4 != 0)) {
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
  cStack_85 = 0;
  local_90 = 0x14;
  uStack_87 = 0x676e;
  local_a8 = 0x1a;
  uStack_8f = (undefined5)s_img029_png_002b3e69._0_8_;
  uStack_8a = SUB82(s_img029_png_002b3e69._0_8_,5);
  cStack_88 = SUB81(s_img029_png_002b3e69._0_8_,7);
  cStack_9a = 0;
  local_a7 = _DAT_002b9230;
  uStack_a2._0_1_ = s_9_imgcut_002b9235[0];
  uStack_a2._1_1_ = s_9_imgcut_002b9235[1];
  uStack_a2._2_1_ = s_9_imgcut_002b9235[2];
  uStack_9f._0_1_ = s_9_imgcut_002b9235[3];
  uStack_9f._1_1_ = s_9_imgcut_002b9235[4];
  uStack_9f._2_1_ = s_9_imgcut_002b9235[5];
  uStack_9f._3_1_ = s_9_imgcut_002b9235[6];
  uStack_9f._4_1_ = s_9_imgcut_002b9235[7];
  FUN_00633334(&local_70,&DAT_00ca4b00,&local_90,&local_a8,0x2601);
  plVar7 = plStack_68;
  uVar2 = local_70;
  plVar6 = (long *)param_1[0x2a];
  local_70 = 0;
  plStack_68 = (long *)0x0;
  param_1[0x2a] = plVar7;
  param_1[0x29] = uVar2;
  if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00c538e0(0xffffffffffffffff,plVar6 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar6 + 0x10))(plVar6);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
  }
  plVar7 = plStack_68;
  if ((plStack_68 != (long *)0x0) &&
     (lVar5 = FUN_00c538e0(0xffffffffffffffff,plStack_68 + 1), lVar5 == 0)) {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
  }
  if ((local_a8 & 1) != 0) {
    _ZdlPv((void *)CONCAT62(uStack_96,CONCAT11(uStack_97,cStack_98)));
  }
  if ((local_90 & 1) != 0) {
    _ZdlPv(local_80);
  }
  FUN_00862c10(&local_90,param_2);
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
  if ((plVar7 != (long *)0x0) && (lVar5 = FUN_00c538e0(0xffffffffffffffff,plVar7 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
  }
  plVar7 = (long *)CONCAT17(uStack_81,
                            CONCAT16(uStack_82,
                                     CONCAT24(uStack_84,
                                              CONCAT13(cStack_85,CONCAT21(uStack_87,cStack_88)))));
  if ((plVar7 != (long *)0x0) && (lVar5 = FUN_00c538e0(0xffffffffffffffff,plVar7 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
  }
  if (((DAT_00ca4b38 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca4b38), iVar4 != 0)) {
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
  cStack_85 = 0;
  local_90 = 0x14;
  uStack_87 = 0x676e;
  local_a8 = 0x1a;
  uStack_8f = (undefined5)s_img102_png_002a448a._0_8_;
  uStack_8a = SUB82(s_img102_png_002a448a._0_8_,5);
  cStack_88 = SUB81(s_img102_png_002a448a._0_8_,7);
  cStack_9a = 0;
  local_a7 = _DAT_002bdbdd;
  uStack_a2._0_1_ = s_2_imgcut_002bdbe2[0];
  uStack_a2._1_1_ = s_2_imgcut_002bdbe2[1];
  uStack_a2._2_1_ = s_2_imgcut_002bdbe2[2];
  uStack_9f._0_1_ = s_2_imgcut_002bdbe2[3];
  uStack_9f._1_1_ = s_2_imgcut_002bdbe2[4];
  uStack_9f._2_1_ = s_2_imgcut_002bdbe2[5];
  uStack_9f._3_1_ = s_2_imgcut_002bdbe2[6];
  uStack_9f._4_1_ = s_2_imgcut_002bdbe2[7];
  FUN_00633334(&local_70,&DAT_00ca4b00,&local_90,&local_a8,0x2601);
  plVar7 = plStack_68;
  uVar2 = local_70;
  plVar6 = (long *)param_1[0x3c];
  local_70 = 0;
  plStack_68 = (long *)0x0;
  param_1[0x3c] = plVar7;
  param_1[0x3b] = uVar2;
  if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00c538e0(0xffffffffffffffff,plVar6 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar6 + 0x10))(plVar6);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
  }
  plVar7 = plStack_68;
  if ((plStack_68 != (long *)0x0) &&
     (lVar5 = FUN_00c538e0(0xffffffffffffffff,plStack_68 + 1), lVar5 == 0)) {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
  }
  if ((local_a8 & 1) != 0) {
    _ZdlPv((void *)CONCAT62(uStack_96,CONCAT11(uStack_97,cStack_98)));
  }
  if ((local_90 & 1) != 0) {
    _ZdlPv(local_80);
  }
  if (((DAT_00ca4b38 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca4b38), iVar4 != 0)) {
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
  local_90 = 0x1a;
  uStack_82 = 0;
  uStack_8f._0_1_ = s_img050_02_png_002a33f1[0];
  uStack_8f._1_1_ = s_img050_02_png_002a33f1[1];
  uStack_8f._2_1_ = s_img050_02_png_002a33f1[2];
  uStack_8f._3_1_ = s_img050_02_png_002a33f1[3];
  uStack_8f._4_1_ = s_img050_02_png_002a33f1[4];
  uStack_8a = (undefined2)s_img050_02_png_002a33f1._5_3_;
  cStack_88 = SUB31(s_img050_02_png_002a33f1._5_3_,2);
  uStack_87 = (undefined2)s_img050_02_png_002a33f1._8_5_;
  cStack_85 = SUB51(s_img050_02_png_002a33f1._8_5_,2);
  uStack_84 = SUB52(s_img050_02_png_002a33f1._8_5_,3);
  local_a8 = 0x20;
  uStack_97 = 0;
  uStack_9f = (undefined5)s_img050_02_imgcut_002c02cb._8_8_;
  cStack_9a = SUB81(s_img050_02_imgcut_002c02cb._8_8_,5);
  cStack_99 = SUB81(s_img050_02_imgcut_002c02cb._8_8_,6);
  cStack_98 = SUB81(s_img050_02_imgcut_002c02cb._8_8_,7);
  local_a7 = (undefined5)s_img050_02_imgcut_002c02cb._0_8_;
  uStack_a2 = SUB83(s_img050_02_imgcut_002c02cb._0_8_,5);
  FUN_00633334(&local_70,&DAT_00ca4b00,&local_90,&local_a8,0x2601);
  plVar7 = plStack_68;
  uVar2 = local_70;
  plVar6 = (long *)param_1[0x40];
  local_70 = 0;
  plStack_68 = (long *)0x0;
  param_1[0x40] = plVar7;
  param_1[0x3f] = uVar2;
  if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00c538e0(0xffffffffffffffff,plVar6 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar6 + 0x10))(plVar6);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
  }
  plVar7 = plStack_68;
  if ((plStack_68 != (long *)0x0) &&
     (lVar5 = FUN_00c538e0(0xffffffffffffffff,plStack_68 + 1), lVar5 == 0)) {
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
<a id="insn-008facec"></a> `008facec` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-008facf0"></a> `008facf0` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-008facf4"></a> `008facf4` | `f9 3b 00 f9` | str x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-008facf8"></a> `008facf8` | `f8 5f 08 a9` | stp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-008facfc"></a> `008facfc` | `f6 57 09 a9` | stp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-008fad00"></a> `008fad00` | `f4 4f 0a a9` | stp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-008fad04"></a> `008fad04` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-008fad08"></a> `008fad08` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-008fad0c"></a> `008fad0c` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-008fad10"></a> `008fad10` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-008fad14"></a> `008fad14` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-008fad18"></a> `008fad18` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-008fad1c"></a> `008fad1c` | `1d 75 f9 97` | bl 0x00758190 | `UNCONDITIONAL_CALL`
<a id="insn-008fad20"></a> `008fad20` | `48 1c 00 f0` | adrp x8,0xc85000 | `FALL_THROUGH`
<a id="insn-008fad24"></a> `008fad24` | `08 e1 1b 91` | add x8,x8,#0x6f8 | `FALL_THROUGH`
<a id="insn-008fad28"></a> `008fad28` | `58 1d 00 d0` | adrp x24,0xca4000 | `FALL_THROUGH`
<a id="insn-008fad2c"></a> `008fad2c` | `18 e3 2c 91` | add x24,x24,#0xb38 | `FALL_THROUGH`
<a id="insn-008fad30"></a> `008fad30` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-008fad34"></a> `008fad34` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-008fad38"></a> `008fad38` | `68 c2 0b 39` | strb w8,[x19, #0x2f0] | `FALL_THROUGH`
<a id="insn-008fad3c"></a> `008fad3c` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008fad40"></a> `008fad40` | `c8 4b 00 36` | tbz w8,#0x0,0x008fb6b8 | `CONDITIONAL_JUMP`
<a id="insn-008fad44"></a> `008fad44` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-008fad48"></a> `008fad48` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-008fad4c"></a> `008fad4c` | `ff af 00 39` | strb wzr,[sp, #0x2b] | `FALL_THROUGH`
<a id="insn-008fad50"></a> `008fad50` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fad54"></a> `008fad54` | `e8 cd ff 90` | adrp x8,0x2b6000 | `FALL_THROUGH`
<a id="insn-008fad58"></a> `008fad58` | `08 39 0d 91` | add x8,x8,#0x34e | `FALL_THROUGH`
<a id="insn-008fad5c"></a> `008fad5c` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-008fad60"></a> `008fad60` | `e9 93 02 78` | sturh w9,[sp, #0x29] | `FALL_THROUGH`
<a id="insn-008fad64"></a> `008fad64` | `49 03 80 52` | mov w9,#0x1a | `FALL_THROUGH`
<a id="insn-008fad68"></a> `008fad68` | `e9 23 00 39` | strb w9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fad6c"></a> `008fad6c` | `e8 13 02 f8` | stur x8,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-008fad70"></a> `008fad70` | `a8 cd ff f0` | adrp x8,0x2b1000 | `FALL_THROUGH`
<a id="insn-008fad74"></a> `008fad74` | `08 59 3b 91` | add x8,x8,#0xed6 | `FALL_THROUGH`
<a id="insn-008fad78"></a> `008fad78` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-008fad7c"></a> `008fad7c` | `08 51 40 f8` | ldur x8,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-008fad80"></a> `008fad80` | `ff 5b 00 39` | strb wzr,[sp, #0x16] | `FALL_THROUGH`
<a id="insn-008fad84"></a> `008fad84` | `e9 93 00 f8` | stur x9,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-008fad88"></a> `008fad88` | `e8 e3 00 f8` | stur x8,[sp, #0xe] | `FALL_THROUGH`
<a id="insn-008fad8c"></a> `008fad8c` | `55 1d 00 d0` | adrp x21,0xca4000 | `FALL_THROUGH`
<a id="insn-008fad90"></a> `008fad90` | `b5 02 2c 91` | add x21,x21,#0xb00 | `FALL_THROUGH`
<a id="insn-008fad94"></a> `008fad94` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-008fad98"></a> `008fad98` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-008fad9c"></a> `008fad9c` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-008fada0"></a> `008fada0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008fada4"></a> `008fada4` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-008fada8"></a> `008fada8` | `63 e1 f4 97` | bl 0x00633334 | `UNCONDITIONAL_CALL`
<a id="insn-008fadac"></a> `008fadac` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fadb0"></a> `008fadb0` | `76 5a 40 f9` | ldr x22,[x19, #0xb0] | `FALL_THROUGH`
<a id="insn-008fadb4"></a> `008fadb4` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fadb8"></a> `008fadb8` | `60 82 8a 3c` | stur q0,[x19, #0xa8] | `FALL_THROUGH`
<a id="insn-008fadbc"></a> `008fadbc` | `76 01 00 b4` | cbz x22,0x008fade8 | `CONDITIONAL_JUMP`
<a id="insn-008fadc0"></a> `008fadc0` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fadc4"></a> `008fadc4` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fadc8"></a> `008fadc8` | `c6 62 0d 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-008fadcc"></a> `008fadcc` | `e0 00 00 b5` | cbnz x0,0x008fade8 | `CONDITIONAL_JUMP`
<a id="insn-008fadd0"></a> `008fadd0` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008fadd4"></a> `008fadd4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fadd8"></a> `008fadd8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008faddc"></a> `008faddc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fade0"></a> `008fade0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fade4"></a> `008fade4` | `27 73 0d 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-008fade8"></a> `008fade8` | `b6 83 5e f8` | ldur x22,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-008fadec"></a> `008fadec` | `b6 00 00 b4` | cbz x22,0x008fae00 | `CONDITIONAL_JUMP`
<a id="insn-008fadf0"></a> `008fadf0` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fadf4"></a> `008fadf4` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fadf8"></a> `008fadf8` | `ba 62 0d 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-008fadfc"></a> `008fadfc` | `a0 0b 00 b4` | cbz x0,0x008faf70 | `CONDITIONAL_JUMP`
<a id="insn-008fae00"></a> `008fae00` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fae04"></a> `008fae04` | `68 00 00 36` | tbz w8,#0x0,0x008fae10 | `CONDITIONAL_JUMP`
<a id="insn-008fae08"></a> `008fae08` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-008fae0c"></a> `008fae0c` | `29 73 0d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008fae10"></a> `008fae10` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fae14"></a> `008fae14` | `68 00 00 36` | tbz w8,#0x0,0x008fae20 | `CONDITIONAL_JUMP`
<a id="insn-008fae18"></a> `008fae18` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008fae1c"></a> `008fae1c` | `25 73 0d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008fae20"></a> `008fae20` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-008fae24"></a> `008fae24` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-008fae28"></a> `008fae28` | `b4 a5 fd 97` | bl 0x008644f8 | `UNCONDITIONAL_CALL`
<a id="insn-008fae2c"></a> `008fae2c` | `e0 0b c0 3d` | ldr q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fae30"></a> `008fae30` | `76 6a 40 f9` | ldr x22,[x19, #0xd0] | `FALL_THROUGH`
<a id="insn-008fae34"></a> `008fae34` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fae38"></a> `008fae38` | `60 82 8c 3c` | stur q0,[x19, #0xc8] | `FALL_THROUGH`
<a id="insn-008fae3c"></a> `008fae3c` | `76 01 00 b4` | cbz x22,0x008fae68 | `CONDITIONAL_JUMP`
<a id="insn-008fae40"></a> `008fae40` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fae44"></a> `008fae44` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fae48"></a> `008fae48` | `a6 62 0d 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-008fae4c"></a> `008fae4c` | `e0 00 00 b5` | cbnz x0,0x008fae68 | `CONDITIONAL_JUMP`
<a id="insn-008fae50"></a> `008fae50` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008fae54"></a> `008fae54` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fae58"></a> `008fae58` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fae5c"></a> `008fae5c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fae60"></a> `008fae60` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fae64"></a> `008fae64` | `07 73 0d 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-008fae68"></a> `008fae68` | `f6 17 40 f9` | ldr x22,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-008fae6c"></a> `008fae6c` | `76 01 00 b4` | cbz x22,0x008fae98 | `CONDITIONAL_JUMP`
<a id="insn-008fae70"></a> `008fae70` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fae74"></a> `008fae74` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fae78"></a> `008fae78` | `9a 62 0d 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-008fae7c"></a> `008fae7c` | `e0 00 00 b5` | cbnz x0,0x008fae98 | `CONDITIONAL_JUMP`
<a id="insn-008fae80"></a> `008fae80` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008fae84"></a> `008fae84` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fae88"></a> `008fae88` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fae8c"></a> `008fae8c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fae90"></a> `008fae90` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fae94"></a> `008fae94` | `fb 72 0d 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-008fae98"></a> `008fae98` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008fae9c"></a> `008fae9c` | `a8 43 00 36` | tbz w8,#0x0,0x008fb710 | `CONDITIONAL_JUMP`
<a id="insn-008faea0"></a> `008faea0` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-008faea4"></a> `008faea4` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-008faea8"></a> `008faea8` | `ff af 00 39` | strb wzr,[sp, #0x2b] | `FALL_THROUGH`
<a id="insn-008faeac"></a> `008faeac` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008faeb0"></a> `008faeb0` | `28 ce ff 90` | adrp x8,0x2be000 | `FALL_THROUGH`
<a id="insn-008faeb4"></a> `008faeb4` | `08 f9 3d 91` | add x8,x8,#0xf7e | `FALL_THROUGH`
<a id="insn-008faeb8"></a> `008faeb8` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-008faebc"></a> `008faebc` | `e9 93 02 78` | sturh w9,[sp, #0x29] | `FALL_THROUGH`
<a id="insn-008faec0"></a> `008faec0` | `49 03 80 52` | mov w9,#0x1a | `FALL_THROUGH`
<a id="insn-008faec4"></a> `008faec4` | `e9 23 00 39` | strb w9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008faec8"></a> `008faec8` | `e8 13 02 f8` | stur x8,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-008faecc"></a> `008faecc` | `68 cd ff f0` | adrp x8,0x2a9000 | `FALL_THROUGH`
<a id="insn-008faed0"></a> `008faed0` | `08 59 3b 91` | add x8,x8,#0xed6 | `FALL_THROUGH`
<a id="insn-008faed4"></a> `008faed4` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-008faed8"></a> `008faed8` | `08 51 40 f8` | ldur x8,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-008faedc"></a> `008faedc` | `ff 5b 00 39` | strb wzr,[sp, #0x16] | `FALL_THROUGH`
<a id="insn-008faee0"></a> `008faee0` | `e9 93 00 f8` | stur x9,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-008faee4"></a> `008faee4` | `e8 e3 00 f8` | stur x8,[sp, #0xe] | `FALL_THROUGH`
<a id="insn-008faee8"></a> `008faee8` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-008faeec"></a> `008faeec` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-008faef0"></a> `008faef0` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-008faef4"></a> `008faef4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008faef8"></a> `008faef8` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-008faefc"></a> `008faefc` | `0e e1 f4 97` | bl 0x00633334 | `UNCONDITIONAL_CALL`
<a id="insn-008faf00"></a> `008faf00` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008faf04"></a> `008faf04` | `76 82 40 f9` | ldr x22,[x19, #0x100] | `FALL_THROUGH`
<a id="insn-008faf08"></a> `008faf08` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008faf0c"></a> `008faf0c` | `60 82 8f 3c` | stur q0,[x19, #0xf8] | `FALL_THROUGH`
<a id="insn-008faf10"></a> `008faf10` | `76 01 00 b4` | cbz x22,0x008faf3c | `CONDITIONAL_JUMP`
<a id="insn-008faf14"></a> `008faf14` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008faf18"></a> `008faf18` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008faf1c"></a> `008faf1c` | `71 62 0d 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-008faf20"></a> `008faf20` | `e0 00 00 b5` | cbnz x0,0x008faf3c | `CONDITIONAL_JUMP`
<a id="insn-008faf24"></a> `008faf24` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008faf28"></a> `008faf28` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008faf2c"></a> `008faf2c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008faf30"></a> `008faf30` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008faf34"></a> `008faf34` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008faf38"></a> `008faf38` | `d2 72 0d 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-008faf3c"></a> `008faf3c` | `b6 83 5e f8` | ldur x22,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-008faf40"></a> `008faf40` | `b6 00 00 b4` | cbz x22,0x008faf54 | `CONDITIONAL_JUMP`
<a id="insn-008faf44"></a> `008faf44` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008faf48"></a> `008faf48` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008faf4c"></a> `008faf4c` | `65 62 0d 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-008faf50"></a> `008faf50` | `20 02 00 b4` | cbz x0,0x008faf94 | `CONDITIONAL_JUMP`
<a id="insn-008faf54"></a> `008faf54` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008faf58"></a> `008faf58` | `e8 02 00 37` | tbnz w8,#0x0,0x008fafb4 | `CONDITIONAL_JUMP`
<a id="insn-008faf5c"></a> `008faf5c` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008faf60"></a> `008faf60` | `28 03 00 37` | tbnz w8,#0x0,0x008fafc4 | `CONDITIONAL_JUMP`
<a id="insn-008faf64"></a> `008faf64` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008faf68"></a> `008faf68` | `68 03 00 37` | tbnz w8,#0x0,0x008fafd4 | `CONDITIONAL_JUMP`
<a id="insn-008faf6c"></a> `008faf6c` | `fe 01 00 14` | b 0x008fb764 | `UNCONDITIONAL_JUMP`
<a id="insn-008faf70"></a> `008faf70` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008faf74"></a> `008faf74` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008faf78"></a> `008faf78` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008faf7c"></a> `008faf7c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008faf80"></a> `008faf80` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008faf84"></a> `008faf84` | `bf 72 0d 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-008faf88"></a> `008faf88` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008faf8c"></a> `008faf8c` | `e8 f3 07 37` | tbnz w8,#0x0,0x008fae08 | `CONDITIONAL_JUMP`
<a id="insn-008faf90"></a> `008faf90` | `a0 ff ff 17` | b 0x008fae10 | `UNCONDITIONAL_JUMP`
<a id="insn-008faf94"></a> `008faf94` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008faf98"></a> `008faf98` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008faf9c"></a> `008faf9c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fafa0"></a> `008fafa0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fafa4"></a> `008fafa4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fafa8"></a> `008fafa8` | `b6 72 0d 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-008fafac"></a> `008fafac` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fafb0"></a> `008fafb0` | `68 fd 07 36` | tbz w8,#0x0,0x008faf5c | `CONDITIONAL_JUMP`
<a id="insn-008fafb4"></a> `008fafb4` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-008fafb8"></a> `008fafb8` | `be 72 0d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008fafbc"></a> `008fafbc` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fafc0"></a> `008fafc0` | `28 fd 07 36` | tbz w8,#0x0,0x008faf64 | `CONDITIONAL_JUMP`
<a id="insn-008fafc4"></a> `008fafc4` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008fafc8"></a> `008fafc8` | `ba 72 0d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008fafcc"></a> `008fafcc` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008fafd0"></a> `008fafd0` | `a8 3c 00 36` | tbz w8,#0x0,0x008fb764 | `CONDITIONAL_JUMP`
<a id="insn-008fafd4"></a> `008fafd4` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-008fafd8"></a> `008fafd8` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-008fafdc"></a> `008fafdc` | `ff af 00 39` | strb wzr,[sp, #0x2b] | `FALL_THROUGH`
<a id="insn-008fafe0"></a> `008fafe0` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fafe4"></a> `008fafe4` | `28 ce ff b0` | adrp x8,0x2bf000 | `FALL_THROUGH`
<a id="insn-008fafe8"></a> `008fafe8` | `08 d9 3f 91` | add x8,x8,#0xff6 | `FALL_THROUGH`
<a id="insn-008fafec"></a> `008fafec` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-008faff0"></a> `008faff0` | `e9 93 02 78` | sturh w9,[sp, #0x29] | `FALL_THROUGH`
<a id="insn-008faff4"></a> `008faff4` | `49 03 80 52` | mov w9,#0x1a | `FALL_THROUGH`
<a id="insn-008faff8"></a> `008faff8` | `e9 23 00 39` | strb w9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008faffc"></a> `008faffc` | `e8 13 02 f8` | stur x8,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-008fb000"></a> `008fb000` | `68 cd ff d0` | adrp x8,0x2a9000 | `FALL_THROUGH`
<a id="insn-008fb004"></a> `008fb004` | `08 a5 38 91` | add x8,x8,#0xe29 | `FALL_THROUGH`
<a id="insn-008fb008"></a> `008fb008` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-008fb00c"></a> `008fb00c` | `08 51 40 f8` | ldur x8,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-008fb010"></a> `008fb010` | `ff 5b 00 39` | strb wzr,[sp, #0x16] | `FALL_THROUGH`
<a id="insn-008fb014"></a> `008fb014` | `e9 93 00 f8` | stur x9,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-008fb018"></a> `008fb018` | `e8 e3 00 f8` | stur x8,[sp, #0xe] | `FALL_THROUGH`
<a id="insn-008fb01c"></a> `008fb01c` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-008fb020"></a> `008fb020` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-008fb024"></a> `008fb024` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-008fb028"></a> `008fb028` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008fb02c"></a> `008fb02c` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-008fb030"></a> `008fb030` | `c1 e0 f4 97` | bl 0x00633334 | `UNCONDITIONAL_CALL`
<a id="insn-008fb034"></a> `008fb034` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb038"></a> `008fb038` | `76 92 40 f9` | ldr x22,[x19, #0x120] | `FALL_THROUGH`
<a id="insn-008fb03c"></a> `008fb03c` | `79 62 04 91` | add x25,x19,#0x118 | `FALL_THROUGH`
<a id="insn-008fb040"></a> `008fb040` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb044"></a> `008fb044` | `20 03 80 3d` | str q0,[x25] | `FALL_THROUGH`
<a id="insn-008fb048"></a> `008fb048` | `76 01 00 b4` | cbz x22,0x008fb074 | `CONDITIONAL_JUMP`
<a id="insn-008fb04c"></a> `008fb04c` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fb050"></a> `008fb050` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb054"></a> `008fb054` | `23 62 0d 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb058"></a> `008fb058` | `e0 00 00 b5` | cbnz x0,0x008fb074 | `CONDITIONAL_JUMP`
<a id="insn-008fb05c"></a> `008fb05c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008fb060"></a> `008fb060` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb064"></a> `008fb064` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb068"></a> `008fb068` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb06c"></a> `008fb06c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb070"></a> `008fb070` | `84 72 0d 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb074"></a> `008fb074` | `b6 83 5e f8` | ldur x22,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-008fb078"></a> `008fb078` | `b6 00 00 b4` | cbz x22,0x008fb08c | `CONDITIONAL_JUMP`
<a id="insn-008fb07c"></a> `008fb07c` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fb080"></a> `008fb080` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb084"></a> `008fb084` | `17 62 0d 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb088"></a> `008fb088` | `00 01 00 b4` | cbz x0,0x008fb0a8 | `CONDITIONAL_JUMP`
<a id="insn-008fb08c"></a> `008fb08c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb090"></a> `008fb090` | `c8 01 00 37` | tbnz w8,#0x0,0x008fb0c8 | `CONDITIONAL_JUMP`
<a id="insn-008fb094"></a> `008fb094` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb098"></a> `008fb098` | `08 02 00 37` | tbnz w8,#0x0,0x008fb0d8 | `CONDITIONAL_JUMP`
<a id="insn-008fb09c"></a> `008fb09c` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008fb0a0"></a> `008fb0a0` | `48 02 00 37` | tbnz w8,#0x0,0x008fb0e8 | `CONDITIONAL_JUMP`
<a id="insn-008fb0a4"></a> `008fb0a4` | `c5 01 00 14` | b 0x008fb7b8 | `UNCONDITIONAL_JUMP`
<a id="insn-008fb0a8"></a> `008fb0a8` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008fb0ac"></a> `008fb0ac` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb0b0"></a> `008fb0b0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb0b4"></a> `008fb0b4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb0b8"></a> `008fb0b8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb0bc"></a> `008fb0bc` | `71 72 0d 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb0c0"></a> `008fb0c0` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb0c4"></a> `008fb0c4` | `88 fe 07 36` | tbz w8,#0x0,0x008fb094 | `CONDITIONAL_JUMP`
<a id="insn-008fb0c8"></a> `008fb0c8` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-008fb0cc"></a> `008fb0cc` | `79 72 0d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb0d0"></a> `008fb0d0` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb0d4"></a> `008fb0d4` | `48 fe 07 36` | tbz w8,#0x0,0x008fb09c | `CONDITIONAL_JUMP`
<a id="insn-008fb0d8"></a> `008fb0d8` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008fb0dc"></a> `008fb0dc` | `75 72 0d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb0e0"></a> `008fb0e0` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008fb0e4"></a> `008fb0e4` | `a8 36 00 36` | tbz w8,#0x0,0x008fb7b8 | `CONDITIONAL_JUMP`
<a id="insn-008fb0e8"></a> `008fb0e8` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-008fb0ec"></a> `008fb0ec` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-008fb0f0"></a> `008fb0f0` | `ff af 00 39` | strb wzr,[sp, #0x2b] | `FALL_THROUGH`
<a id="insn-008fb0f4"></a> `008fb0f4` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb0f8"></a> `008fb0f8` | `e8 cd ff d0` | adrp x8,0x2b9000 | `FALL_THROUGH`
<a id="insn-008fb0fc"></a> `008fb0fc` | `08 3d 07 91` | add x8,x8,#0x1cf | `FALL_THROUGH`
<a id="insn-008fb100"></a> `008fb100` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-008fb104"></a> `008fb104` | `e9 93 02 78` | sturh w9,[sp, #0x29] | `FALL_THROUGH`
<a id="insn-008fb108"></a> `008fb108` | `49 03 80 52` | mov w9,#0x1a | `FALL_THROUGH`
<a id="insn-008fb10c"></a> `008fb10c` | `e9 23 00 39` | strb w9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb110"></a> `008fb110` | `e8 13 02 f8` | stur x8,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-008fb114"></a> `008fb114` | `08 ce ff d0` | adrp x8,0x2bd000 | `FALL_THROUGH`
<a id="insn-008fb118"></a> `008fb118` | `08 3d 2f 91` | add x8,x8,#0xbcf | `FALL_THROUGH`
<a id="insn-008fb11c"></a> `008fb11c` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-008fb120"></a> `008fb120` | `08 51 40 f8` | ldur x8,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-008fb124"></a> `008fb124` | `ff 5b 00 39` | strb wzr,[sp, #0x16] | `FALL_THROUGH`
<a id="insn-008fb128"></a> `008fb128` | `e9 93 00 f8` | stur x9,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-008fb12c"></a> `008fb12c` | `e8 e3 00 f8` | stur x8,[sp, #0xe] | `FALL_THROUGH`
<a id="insn-008fb130"></a> `008fb130` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-008fb134"></a> `008fb134` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-008fb138"></a> `008fb138` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-008fb13c"></a> `008fb13c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008fb140"></a> `008fb140` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-008fb144"></a> `008fb144` | `7c e0 f4 97` | bl 0x00633334 | `UNCONDITIONAL_CALL`
<a id="insn-008fb148"></a> `008fb148` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb14c"></a> `008fb14c` | `76 9a 40 f9` | ldr x22,[x19, #0x130] | `FALL_THROUGH`
<a id="insn-008fb150"></a> `008fb150` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb154"></a> `008fb154` | `20 07 80 3d` | str q0,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-008fb158"></a> `008fb158` | `76 01 00 b4` | cbz x22,0x008fb184 | `CONDITIONAL_JUMP`
<a id="insn-008fb15c"></a> `008fb15c` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fb160"></a> `008fb160` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb164"></a> `008fb164` | `df 61 0d 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb168"></a> `008fb168` | `e0 00 00 b5` | cbnz x0,0x008fb184 | `CONDITIONAL_JUMP`
<a id="insn-008fb16c"></a> `008fb16c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008fb170"></a> `008fb170` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb174"></a> `008fb174` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb178"></a> `008fb178` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb17c"></a> `008fb17c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb180"></a> `008fb180` | `40 72 0d 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb184"></a> `008fb184` | `b6 83 5e f8` | ldur x22,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-008fb188"></a> `008fb188` | `b6 00 00 b4` | cbz x22,0x008fb19c | `CONDITIONAL_JUMP`
<a id="insn-008fb18c"></a> `008fb18c` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fb190"></a> `008fb190` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb194"></a> `008fb194` | `d3 61 0d 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb198"></a> `008fb198` | `00 01 00 b4` | cbz x0,0x008fb1b8 | `CONDITIONAL_JUMP`
<a id="insn-008fb19c"></a> `008fb19c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb1a0"></a> `008fb1a0` | `c8 01 00 37` | tbnz w8,#0x0,0x008fb1d8 | `CONDITIONAL_JUMP`
<a id="insn-008fb1a4"></a> `008fb1a4` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb1a8"></a> `008fb1a8` | `08 02 00 37` | tbnz w8,#0x0,0x008fb1e8 | `CONDITIONAL_JUMP`
<a id="insn-008fb1ac"></a> `008fb1ac` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008fb1b0"></a> `008fb1b0` | `48 02 00 37` | tbnz w8,#0x0,0x008fb1f8 | `CONDITIONAL_JUMP`
<a id="insn-008fb1b4"></a> `008fb1b4` | `96 01 00 14` | b 0x008fb80c | `UNCONDITIONAL_JUMP`
<a id="insn-008fb1b8"></a> `008fb1b8` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008fb1bc"></a> `008fb1bc` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb1c0"></a> `008fb1c0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb1c4"></a> `008fb1c4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb1c8"></a> `008fb1c8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb1cc"></a> `008fb1cc` | `2d 72 0d 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb1d0"></a> `008fb1d0` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb1d4"></a> `008fb1d4` | `88 fe 07 36` | tbz w8,#0x0,0x008fb1a4 | `CONDITIONAL_JUMP`
<a id="insn-008fb1d8"></a> `008fb1d8` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-008fb1dc"></a> `008fb1dc` | `35 72 0d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb1e0"></a> `008fb1e0` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb1e4"></a> `008fb1e4` | `48 fe 07 36` | tbz w8,#0x0,0x008fb1ac | `CONDITIONAL_JUMP`
<a id="insn-008fb1e8"></a> `008fb1e8` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008fb1ec"></a> `008fb1ec` | `31 72 0d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb1f0"></a> `008fb1f0` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008fb1f4"></a> `008fb1f4` | `c8 30 00 36` | tbz w8,#0x0,0x008fb80c | `CONDITIONAL_JUMP`
<a id="insn-008fb1f8"></a> `008fb1f8` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-008fb1fc"></a> `008fb1fc` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-008fb200"></a> `008fb200` | `ff af 00 39` | strb wzr,[sp, #0x2b] | `FALL_THROUGH`
<a id="insn-008fb204"></a> `008fb204` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb208"></a> `008fb208` | `28 cd ff 90` | adrp x8,0x29f000 | `FALL_THROUGH`
<a id="insn-008fb20c"></a> `008fb20c` | `08 cd 05 91` | add x8,x8,#0x173 | `FALL_THROUGH`
<a id="insn-008fb210"></a> `008fb210` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-008fb214"></a> `008fb214` | `e9 93 02 78` | sturh w9,[sp, #0x29] | `FALL_THROUGH`
<a id="insn-008fb218"></a> `008fb218` | `49 03 80 52` | mov w9,#0x1a | `FALL_THROUGH`
<a id="insn-008fb21c"></a> `008fb21c` | `e9 23 00 39` | strb w9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb220"></a> `008fb220` | `e8 13 02 f8` | stur x8,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-008fb224"></a> `008fb224` | `28 ce ff d0` | adrp x8,0x2c1000 | `FALL_THROUGH`
<a id="insn-008fb228"></a> `008fb228` | `08 cd 0c 91` | add x8,x8,#0x333 | `FALL_THROUGH`
<a id="insn-008fb22c"></a> `008fb22c` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-008fb230"></a> `008fb230` | `08 51 40 f8` | ldur x8,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-008fb234"></a> `008fb234` | `ff 5b 00 39` | strb wzr,[sp, #0x16] | `FALL_THROUGH`
<a id="insn-008fb238"></a> `008fb238` | `e9 93 00 f8` | stur x9,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-008fb23c"></a> `008fb23c` | `e8 e3 00 f8` | stur x8,[sp, #0xe] | `FALL_THROUGH`
<a id="insn-008fb240"></a> `008fb240` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-008fb244"></a> `008fb244` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-008fb248"></a> `008fb248` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-008fb24c"></a> `008fb24c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008fb250"></a> `008fb250` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-008fb254"></a> `008fb254` | `38 e0 f4 97` | bl 0x00633334 | `UNCONDITIONAL_CALL`
<a id="insn-008fb258"></a> `008fb258` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb25c"></a> `008fb25c` | `76 a2 40 f9` | ldr x22,[x19, #0x140] | `FALL_THROUGH`
<a id="insn-008fb260"></a> `008fb260` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb264"></a> `008fb264` | `20 0b 80 3d` | str q0,[x25, #0x20] | `FALL_THROUGH`
<a id="insn-008fb268"></a> `008fb268` | `76 01 00 b4` | cbz x22,0x008fb294 | `CONDITIONAL_JUMP`
<a id="insn-008fb26c"></a> `008fb26c` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fb270"></a> `008fb270` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb274"></a> `008fb274` | `9b 61 0d 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb278"></a> `008fb278` | `e0 00 00 b5` | cbnz x0,0x008fb294 | `CONDITIONAL_JUMP`
<a id="insn-008fb27c"></a> `008fb27c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008fb280"></a> `008fb280` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb284"></a> `008fb284` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb288"></a> `008fb288` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb28c"></a> `008fb28c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb290"></a> `008fb290` | `fc 71 0d 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb294"></a> `008fb294` | `b6 83 5e f8` | ldur x22,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-008fb298"></a> `008fb298` | `b6 00 00 b4` | cbz x22,0x008fb2ac | `CONDITIONAL_JUMP`
<a id="insn-008fb29c"></a> `008fb29c` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fb2a0"></a> `008fb2a0` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb2a4"></a> `008fb2a4` | `8f 61 0d 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb2a8"></a> `008fb2a8` | `00 01 00 b4` | cbz x0,0x008fb2c8 | `CONDITIONAL_JUMP`
<a id="insn-008fb2ac"></a> `008fb2ac` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb2b0"></a> `008fb2b0` | `c8 01 00 37` | tbnz w8,#0x0,0x008fb2e8 | `CONDITIONAL_JUMP`
<a id="insn-008fb2b4"></a> `008fb2b4` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb2b8"></a> `008fb2b8` | `08 02 00 37` | tbnz w8,#0x0,0x008fb2f8 | `CONDITIONAL_JUMP`
<a id="insn-008fb2bc"></a> `008fb2bc` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008fb2c0"></a> `008fb2c0` | `48 02 00 37` | tbnz w8,#0x0,0x008fb308 | `CONDITIONAL_JUMP`
<a id="insn-008fb2c4"></a> `008fb2c4` | `67 01 00 14` | b 0x008fb860 | `UNCONDITIONAL_JUMP`
<a id="insn-008fb2c8"></a> `008fb2c8` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008fb2cc"></a> `008fb2cc` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb2d0"></a> `008fb2d0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb2d4"></a> `008fb2d4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb2d8"></a> `008fb2d8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb2dc"></a> `008fb2dc` | `e9 71 0d 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb2e0"></a> `008fb2e0` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb2e4"></a> `008fb2e4` | `88 fe 07 36` | tbz w8,#0x0,0x008fb2b4 | `CONDITIONAL_JUMP`
<a id="insn-008fb2e8"></a> `008fb2e8` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-008fb2ec"></a> `008fb2ec` | `f1 71 0d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb2f0"></a> `008fb2f0` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb2f4"></a> `008fb2f4` | `48 fe 07 36` | tbz w8,#0x0,0x008fb2bc | `CONDITIONAL_JUMP`
<a id="insn-008fb2f8"></a> `008fb2f8` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008fb2fc"></a> `008fb2fc` | `ed 71 0d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb300"></a> `008fb300` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008fb304"></a> `008fb304` | `e8 2a 00 36` | tbz w8,#0x0,0x008fb860 | `CONDITIONAL_JUMP`
<a id="insn-008fb308"></a> `008fb308` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-008fb30c"></a> `008fb30c` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-008fb310"></a> `008fb310` | `ff af 00 39` | strb wzr,[sp, #0x2b] | `FALL_THROUGH`
<a id="insn-008fb314"></a> `008fb314` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb318"></a> `008fb318` | `c8 cd ff 90` | adrp x8,0x2b3000 | `FALL_THROUGH`
<a id="insn-008fb31c"></a> `008fb31c` | `08 a5 39 91` | add x8,x8,#0xe69 | `FALL_THROUGH`
<a id="insn-008fb320"></a> `008fb320` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-008fb324"></a> `008fb324` | `e9 93 02 78` | sturh w9,[sp, #0x29] | `FALL_THROUGH`
<a id="insn-008fb328"></a> `008fb328` | `49 03 80 52` | mov w9,#0x1a | `FALL_THROUGH`
<a id="insn-008fb32c"></a> `008fb32c` | `e9 23 00 39` | strb w9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb330"></a> `008fb330` | `e8 13 02 f8` | stur x8,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-008fb334"></a> `008fb334` | `e8 cd ff d0` | adrp x8,0x2b9000 | `FALL_THROUGH`
<a id="insn-008fb338"></a> `008fb338` | `08 c1 08 91` | add x8,x8,#0x230 | `FALL_THROUGH`
<a id="insn-008fb33c"></a> `008fb33c` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-008fb340"></a> `008fb340` | `08 51 40 f8` | ldur x8,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-008fb344"></a> `008fb344` | `ff 5b 00 39` | strb wzr,[sp, #0x16] | `FALL_THROUGH`
<a id="insn-008fb348"></a> `008fb348` | `e9 93 00 f8` | stur x9,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-008fb34c"></a> `008fb34c` | `e8 e3 00 f8` | stur x8,[sp, #0xe] | `FALL_THROUGH`
<a id="insn-008fb350"></a> `008fb350` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-008fb354"></a> `008fb354` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-008fb358"></a> `008fb358` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-008fb35c"></a> `008fb35c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008fb360"></a> `008fb360` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-008fb364"></a> `008fb364` | `f4 df f4 97` | bl 0x00633334 | `UNCONDITIONAL_CALL`
<a id="insn-008fb368"></a> `008fb368` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb36c"></a> `008fb36c` | `76 aa 40 f9` | ldr x22,[x19, #0x150] | `FALL_THROUGH`
<a id="insn-008fb370"></a> `008fb370` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb374"></a> `008fb374` | `20 0f 80 3d` | str q0,[x25, #0x30] | `FALL_THROUGH`
<a id="insn-008fb378"></a> `008fb378` | `76 01 00 b4` | cbz x22,0x008fb3a4 | `CONDITIONAL_JUMP`
<a id="insn-008fb37c"></a> `008fb37c` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fb380"></a> `008fb380` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb384"></a> `008fb384` | `57 61 0d 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb388"></a> `008fb388` | `e0 00 00 b5` | cbnz x0,0x008fb3a4 | `CONDITIONAL_JUMP`
<a id="insn-008fb38c"></a> `008fb38c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008fb390"></a> `008fb390` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb394"></a> `008fb394` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb398"></a> `008fb398` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb39c"></a> `008fb39c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb3a0"></a> `008fb3a0` | `b8 71 0d 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb3a4"></a> `008fb3a4` | `b6 83 5e f8` | ldur x22,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-008fb3a8"></a> `008fb3a8` | `b6 00 00 b4` | cbz x22,0x008fb3bc | `CONDITIONAL_JUMP`
<a id="insn-008fb3ac"></a> `008fb3ac` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-008fb3b0"></a> `008fb3b0` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb3b4"></a> `008fb3b4` | `4b 61 0d 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb3b8"></a> `008fb3b8` | `e0 0b 00 b4` | cbz x0,0x008fb534 | `CONDITIONAL_JUMP`
<a id="insn-008fb3bc"></a> `008fb3bc` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb3c0"></a> `008fb3c0` | `68 00 00 36` | tbz w8,#0x0,0x008fb3cc | `CONDITIONAL_JUMP`
<a id="insn-008fb3c4"></a> `008fb3c4` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-008fb3c8"></a> `008fb3c8` | `ba 71 0d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb3cc"></a> `008fb3cc` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb3d0"></a> `008fb3d0` | `68 00 00 36` | tbz w8,#0x0,0x008fb3dc | `CONDITIONAL_JUMP`
<a id="insn-008fb3d4"></a> `008fb3d4` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008fb3d8"></a> `008fb3d8` | `b6 71 0d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb3dc"></a> `008fb3dc` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-008fb3e0"></a> `008fb3e0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-008fb3e4"></a> `008fb3e4` | `0b 9e fd 97` | bl 0x00862c10 | `UNCONDITIONAL_CALL`
<a id="insn-008fb3e8"></a> `008fb3e8` | `e0 0b c0 3d` | ldr q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb3ec"></a> `008fb3ec` | `74 da 40 f9` | ldr x20,[x19, #0x1b0] | `FALL_THROUGH`
<a id="insn-008fb3f0"></a> `008fb3f0` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb3f4"></a> `008fb3f4` | `20 27 80 3d` | str q0,[x25, #0x90] | `FALL_THROUGH`
<a id="insn-008fb3f8"></a> `008fb3f8` | `74 01 00 b4` | cbz x20,0x008fb424 | `CONDITIONAL_JUMP`
<a id="insn-008fb3fc"></a> `008fb3fc` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-008fb400"></a> `008fb400` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb404"></a> `008fb404` | `37 61 0d 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb408"></a> `008fb408` | `e0 00 00 b5` | cbnz x0,0x008fb424 | `CONDITIONAL_JUMP`
<a id="insn-008fb40c"></a> `008fb40c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-008fb410"></a> `008fb410` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-008fb414"></a> `008fb414` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb418"></a> `008fb418` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb41c"></a> `008fb41c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-008fb420"></a> `008fb420` | `98 71 0d 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb424"></a> `008fb424` | `f4 17 40 f9` | ldr x20,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-008fb428"></a> `008fb428` | `74 01 00 b4` | cbz x20,0x008fb454 | `CONDITIONAL_JUMP`
<a id="insn-008fb42c"></a> `008fb42c` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-008fb430"></a> `008fb430` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb434"></a> `008fb434` | `2b 61 0d 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb438"></a> `008fb438` | `e0 00 00 b5` | cbnz x0,0x008fb454 | `CONDITIONAL_JUMP`
<a id="insn-008fb43c"></a> `008fb43c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-008fb440"></a> `008fb440` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-008fb444"></a> `008fb444` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb448"></a> `008fb448` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb44c"></a> `008fb44c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-008fb450"></a> `008fb450` | `8c 71 0d 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb454"></a> `008fb454` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008fb458"></a> `008fb458` | `e8 22 00 36` | tbz w8,#0x0,0x008fb8b4 | `CONDITIONAL_JUMP`
<a id="insn-008fb45c"></a> `008fb45c` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-008fb460"></a> `008fb460` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-008fb464"></a> `008fb464` | `ff af 00 39` | strb wzr,[sp, #0x2b] | `FALL_THROUGH`
<a id="insn-008fb468"></a> `008fb468` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb46c"></a> `008fb46c` | `48 cd ff b0` | adrp x8,0x2a4000 | `FALL_THROUGH`
<a id="insn-008fb470"></a> `008fb470` | `08 29 12 91` | add x8,x8,#0x48a | `FALL_THROUGH`
<a id="insn-008fb474"></a> `008fb474` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-008fb478"></a> `008fb478` | `e9 93 02 78` | sturh w9,[sp, #0x29] | `FALL_THROUGH`
<a id="insn-008fb47c"></a> `008fb47c` | `49 03 80 52` | mov w9,#0x1a | `FALL_THROUGH`
<a id="insn-008fb480"></a> `008fb480` | `e9 23 00 39` | strb w9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb484"></a> `008fb484` | `e8 13 02 f8` | stur x8,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-008fb488"></a> `008fb488` | `08 ce ff d0` | adrp x8,0x2bd000 | `FALL_THROUGH`
<a id="insn-008fb48c"></a> `008fb48c` | `08 75 2f 91` | add x8,x8,#0xbdd | `FALL_THROUGH`
<a id="insn-008fb490"></a> `008fb490` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-008fb494"></a> `008fb494` | `08 51 40 f8` | ldur x8,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-008fb498"></a> `008fb498` | `ff 5b 00 39` | strb wzr,[sp, #0x16] | `FALL_THROUGH`
<a id="insn-008fb49c"></a> `008fb49c` | `e9 93 00 f8` | stur x9,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-008fb4a0"></a> `008fb4a0` | `e8 e3 00 f8` | stur x8,[sp, #0xe] | `FALL_THROUGH`
<a id="insn-008fb4a4"></a> `008fb4a4` | `54 1d 00 b0` | adrp x20,0xca4000 | `FALL_THROUGH`
<a id="insn-008fb4a8"></a> `008fb4a8` | `94 02 2c 91` | add x20,x20,#0xb00 | `FALL_THROUGH`
<a id="insn-008fb4ac"></a> `008fb4ac` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-008fb4b0"></a> `008fb4b0` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-008fb4b4"></a> `008fb4b4` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-008fb4b8"></a> `008fb4b8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-008fb4bc"></a> `008fb4bc` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-008fb4c0"></a> `008fb4c0` | `9d df f4 97` | bl 0x00633334 | `UNCONDITIONAL_CALL`
<a id="insn-008fb4c4"></a> `008fb4c4` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb4c8"></a> `008fb4c8` | `75 f2 40 f9` | ldr x21,[x19, #0x1e0] | `FALL_THROUGH`
<a id="insn-008fb4cc"></a> `008fb4cc` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb4d0"></a> `008fb4d0` | `20 33 80 3d` | str q0,[x25, #0xc0] | `FALL_THROUGH`
<a id="insn-008fb4d4"></a> `008fb4d4` | `75 01 00 b4` | cbz x21,0x008fb500 | `CONDITIONAL_JUMP`
<a id="insn-008fb4d8"></a> `008fb4d8` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-008fb4dc"></a> `008fb4dc` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb4e0"></a> `008fb4e0` | `00 61 0d 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb4e4"></a> `008fb4e4` | `e0 00 00 b5` | cbnz x0,0x008fb500 | `CONDITIONAL_JUMP`
<a id="insn-008fb4e8"></a> `008fb4e8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-008fb4ec"></a> `008fb4ec` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008fb4f0"></a> `008fb4f0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb4f4"></a> `008fb4f4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb4f8"></a> `008fb4f8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008fb4fc"></a> `008fb4fc` | `61 71 0d 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb500"></a> `008fb500` | `b5 83 5e f8` | ldur x21,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-008fb504"></a> `008fb504` | `b5 00 00 b4` | cbz x21,0x008fb518 | `CONDITIONAL_JUMP`
<a id="insn-008fb508"></a> `008fb508` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-008fb50c"></a> `008fb50c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb510"></a> `008fb510` | `f4 60 0d 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb514"></a> `008fb514` | `20 02 00 b4` | cbz x0,0x008fb558 | `CONDITIONAL_JUMP`
<a id="insn-008fb518"></a> `008fb518` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb51c"></a> `008fb51c` | `e8 02 00 37` | tbnz w8,#0x0,0x008fb578 | `CONDITIONAL_JUMP`
<a id="insn-008fb520"></a> `008fb520` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb524"></a> `008fb524` | `28 03 00 37` | tbnz w8,#0x0,0x008fb588 | `CONDITIONAL_JUMP`
<a id="insn-008fb528"></a> `008fb528` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008fb52c"></a> `008fb52c` | `68 03 00 37` | tbnz w8,#0x0,0x008fb598 | `CONDITIONAL_JUMP`
<a id="insn-008fb530"></a> `008fb530` | `f6 00 00 14` | b 0x008fb908 | `UNCONDITIONAL_JUMP`
<a id="insn-008fb534"></a> `008fb534` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-008fb538"></a> `008fb538` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb53c"></a> `008fb53c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb540"></a> `008fb540` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb544"></a> `008fb544` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008fb548"></a> `008fb548` | `4e 71 0d 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb54c"></a> `008fb54c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb550"></a> `008fb550` | `a8 f3 07 37` | tbnz w8,#0x0,0x008fb3c4 | `CONDITIONAL_JUMP`
<a id="insn-008fb554"></a> `008fb554` | `9e ff ff 17` | b 0x008fb3cc | `UNCONDITIONAL_JUMP`
<a id="insn-008fb558"></a> `008fb558` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-008fb55c"></a> `008fb55c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008fb560"></a> `008fb560` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb564"></a> `008fb564` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb568"></a> `008fb568` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008fb56c"></a> `008fb56c` | `45 71 0d 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb570"></a> `008fb570` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb574"></a> `008fb574` | `68 fd 07 36` | tbz w8,#0x0,0x008fb520 | `CONDITIONAL_JUMP`
<a id="insn-008fb578"></a> `008fb578` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-008fb57c"></a> `008fb57c` | `4d 71 0d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb580"></a> `008fb580` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb584"></a> `008fb584` | `28 fd 07 36` | tbz w8,#0x0,0x008fb528 | `CONDITIONAL_JUMP`
<a id="insn-008fb588"></a> `008fb588` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008fb58c"></a> `008fb58c` | `49 71 0d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb590"></a> `008fb590` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-008fb594"></a> `008fb594` | `a8 1b 00 36` | tbz w8,#0x0,0x008fb908 | `CONDITIONAL_JUMP`
<a id="insn-008fb598"></a> `008fb598` | `49 cd ff 90` | adrp x9,0x2a3000 | `FALL_THROUGH`
<a id="insn-008fb59c"></a> `008fb59c` | `29 c5 0f 91` | add x9,x9,#0x3f1 | `FALL_THROUGH`
<a id="insn-008fb5a0"></a> `008fb5a0` | `48 03 80 52` | mov w8,#0x1a | `FALL_THROUGH`
<a id="insn-008fb5a4"></a> `008fb5a4` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-008fb5a8"></a> `008fb5a8` | `29 51 40 f8` | ldur x9,[x9, #0x5] | `FALL_THROUGH`
<a id="insn-008fb5ac"></a> `008fb5ac` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb5b0"></a> `008fb5b0` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-008fb5b4"></a> `008fb5b4` | `ff bb 00 39` | strb wzr,[sp, #0x2e] | `FALL_THROUGH`
<a id="insn-008fb5b8"></a> `008fb5b8` | `ea 13 02 f8` | stur x10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-008fb5bc"></a> `008fb5bc` | `e9 63 02 f8` | stur x9,[sp, #0x26] | `FALL_THROUGH`
<a id="insn-008fb5c0"></a> `008fb5c0` | `29 ce ff b0` | adrp x9,0x2c0000 | `FALL_THROUGH`
<a id="insn-008fb5c4"></a> `008fb5c4` | `29 2d 0b 91` | add x9,x9,#0x2cb | `FALL_THROUGH`
<a id="insn-008fb5c8"></a> `008fb5c8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-008fb5cc"></a> `008fb5cc` | `e8 23 00 39` | strb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb5d0"></a> `008fb5d0` | `ff 67 00 39` | strb wzr,[sp, #0x19] | `FALL_THROUGH`
<a id="insn-008fb5d4"></a> `008fb5d4` | `e0 93 80 3c` | stur q0,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-008fb5d8"></a> `008fb5d8` | `40 1d 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-008fb5dc"></a> `008fb5dc` | `00 00 2c 91` | add x0,x0,#0xb00 | `FALL_THROUGH`
<a id="insn-008fb5e0"></a> `008fb5e0` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-008fb5e4"></a> `008fb5e4` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-008fb5e8"></a> `008fb5e8` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-008fb5ec"></a> `008fb5ec` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-008fb5f0"></a> `008fb5f0` | `51 df f4 97` | bl 0x00633334 | `UNCONDITIONAL_CALL`
<a id="insn-008fb5f4"></a> `008fb5f4` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb5f8"></a> `008fb5f8` | `73 02 41 f9` | ldr x19,[x19, #0x200] | `FALL_THROUGH`
<a id="insn-008fb5fc"></a> `008fb5fc` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-008fb600"></a> `008fb600` | `20 3b 80 3d` | str q0,[x25, #0xe0] | `FALL_THROUGH`
<a id="insn-008fb604"></a> `008fb604` | `73 01 00 b4` | cbz x19,0x008fb630 | `CONDITIONAL_JUMP`
<a id="insn-008fb608"></a> `008fb608` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-008fb60c"></a> `008fb60c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb610"></a> `008fb610` | `b4 60 0d 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb614"></a> `008fb614` | `e0 00 00 b5` | cbnz x0,0x008fb630 | `CONDITIONAL_JUMP`
<a id="insn-008fb618"></a> `008fb618` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-008fb61c"></a> `008fb61c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008fb620"></a> `008fb620` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb624"></a> `008fb624` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb628"></a> `008fb628` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008fb62c"></a> `008fb62c` | `15 71 0d 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb630"></a> `008fb630` | `b3 83 5e f8` | ldur x19,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-008fb634"></a> `008fb634` | `b3 00 00 b4` | cbz x19,0x008fb648 | `CONDITIONAL_JUMP`
<a id="insn-008fb638"></a> `008fb638` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-008fb63c"></a> `008fb63c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-008fb640"></a> `008fb640` | `a8 60 0d 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb644"></a> `008fb644` | `80 02 00 b4` | cbz x0,0x008fb694 | `CONDITIONAL_JUMP`
<a id="insn-008fb648"></a> `008fb648` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb64c"></a> `008fb64c` | `68 00 00 36` | tbz w8,#0x0,0x008fb658 | `CONDITIONAL_JUMP`
<a id="insn-008fb650"></a> `008fb650` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-008fb654"></a> `008fb654` | `17 71 0d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb658"></a> `008fb658` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008fb65c"></a> `008fb65c` | `68 00 00 36` | tbz w8,#0x0,0x008fb668 | `CONDITIONAL_JUMP`
<a id="insn-008fb660"></a> `008fb660` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008fb664"></a> `008fb664` | `13 71 0d 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008fb668"></a> `008fb668` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-008fb66c"></a> `008fb66c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-008fb670"></a> `008fb670` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-008fb674"></a> `008fb674` | `c1 1a 00 54` | b.ne 0x008fb9cc | `CONDITIONAL_JUMP`
<a id="insn-008fb678"></a> `008fb678` | `f4 4f 4a a9` | ldp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-008fb67c"></a> `008fb67c` | `f9 3b 40 f9` | ldr x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-008fb680"></a> `008fb680` | `f6 57 49 a9` | ldp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-008fb684"></a> `008fb684` | `f8 5f 48 a9` | ldp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-008fb688"></a> `008fb688` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-008fb68c"></a> `008fb68c` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-008fb690"></a> `008fb690` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-008fb694"></a> `008fb694` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-008fb698"></a> `008fb698` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008fb69c"></a> `008fb69c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008fb6a0"></a> `008fb6a0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008fb6a4"></a> `008fb6a4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008fb6a8"></a> `008fb6a8` | `f6 70 0d 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-008fb6ac"></a> `008fb6ac` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008fb6b0"></a> `008fb6b0` | `08 fd 07 37` | tbnz w8,#0x0,0x008fb650 | `CONDITIONAL_JUMP`
<a id="insn-008fb6b4"></a> `008fb6b4` | `e9 ff ff 17` | b 0x008fb658 | `UNCONDITIONAL_JUMP`
<a id="insn-008fb6b8"></a> `008fb6b8` | `40 1d 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-008fb6bc"></a> `008fb6bc` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-008fb6c0"></a> `008fb6c0` | `e4 70 0d 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb6c4"></a> `008fb6c4` | `00 b4 ff 34` | cbz w0,0x008fad44 | `CONDITIONAL_JUMP`
<a id="insn-008fb6c8"></a> `008fb6c8` | `41 1d 00 b0` | adrp x1,0xca4000 | `FALL_THROUGH`
<a id="insn-008fb6cc"></a> `008fb6cc` | `21 00 2c 91` | add x1,x1,#0xb00 | `FALL_THROUGH`
<a id="insn-008fb6d0"></a> `008fb6d0` | `00 dc ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-008fb6d4"></a> `008fb6d4` | `00 d0 35 91` | add x0,x0,#0xd74 | `FALL_THROUGH`
<a id="insn-008fb6d8"></a> `008fb6d8` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-008fb6dc"></a> `008fb6dc` | `22 1b 00 f0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-008fb6e0"></a> `008fb6e0` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-008fb6e4"></a> `008fb6e4` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-008fb6e8"></a> `008fb6e8` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-008fb6ec"></a> `008fb6ec` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-008fb6f0"></a> `008fb6f0` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-008fb6f4"></a> `008fb6f4` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-008fb6f8"></a> `008fb6f8` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-008fb6fc"></a> `008fb6fc` | `cd 70 0d 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-008fb700"></a> `008fb700` | `40 1d 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-008fb704"></a> `008fb704` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-008fb708"></a> `008fb708` | `da 70 0d 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-008fb70c"></a> `008fb70c` | `8e fd ff 17` | b 0x008fad44 | `UNCONDITIONAL_JUMP`
<a id="insn-008fb710"></a> `008fb710` | `40 1d 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-008fb714"></a> `008fb714` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-008fb718"></a> `008fb718` | `ce 70 0d 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb71c"></a> `008fb71c` | `20 bc ff 34` | cbz w0,0x008faea0 | `CONDITIONAL_JUMP`
<a id="insn-008fb720"></a> `008fb720` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-008fb724"></a> `008fb724` | `00 dc ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-008fb728"></a> `008fb728` | `00 d0 35 91` | add x0,x0,#0xd74 | `FALL_THROUGH`
<a id="insn-008fb72c"></a> `008fb72c` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-008fb730"></a> `008fb730` | `22 1b 00 f0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-008fb734"></a> `008fb734` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-008fb738"></a> `008fb738` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-008fb73c"></a> `008fb73c` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-008fb740"></a> `008fb740` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-008fb744"></a> `008fb744` | `bf fe 02 a9` | stp xzr,xzr,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-008fb748"></a> `008fb748` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-008fb74c"></a> `008fb74c` | `bf 22 01 a9` | stp xzr,x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-008fb750"></a> `008fb750` | `b8 70 0d 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-008fb754"></a> `008fb754` | `40 1d 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-008fb758"></a> `008fb758` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-008fb75c"></a> `008fb75c` | `c5 70 0d 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-008fb760"></a> `008fb760` | `d0 fd ff 17` | b 0x008faea0 | `UNCONDITIONAL_JUMP`
<a id="insn-008fb764"></a> `008fb764` | `40 1d 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-008fb768"></a> `008fb768` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-008fb76c"></a> `008fb76c` | `b9 70 0d 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb770"></a> `008fb770` | `20 c3 ff 34` | cbz w0,0x008fafd4 | `CONDITIONAL_JUMP`
<a id="insn-008fb774"></a> `008fb774` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-008fb778"></a> `008fb778` | `00 dc ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-008fb77c"></a> `008fb77c` | `00 d0 35 91` | add x0,x0,#0xd74 | `FALL_THROUGH`
<a id="insn-008fb780"></a> `008fb780` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-008fb784"></a> `008fb784` | `22 1b 00 f0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-008fb788"></a> `008fb788` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-008fb78c"></a> `008fb78c` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-008fb790"></a> `008fb790` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-008fb794"></a> `008fb794` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-008fb798"></a> `008fb798` | `bf fe 02 a9` | stp xzr,xzr,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-008fb79c"></a> `008fb79c` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-008fb7a0"></a> `008fb7a0` | `bf 22 01 a9` | stp xzr,x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-008fb7a4"></a> `008fb7a4` | `a3 70 0d 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-008fb7a8"></a> `008fb7a8` | `40 1d 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-008fb7ac"></a> `008fb7ac` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-008fb7b0"></a> `008fb7b0` | `b0 70 0d 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-008fb7b4"></a> `008fb7b4` | `08 fe ff 17` | b 0x008fafd4 | `UNCONDITIONAL_JUMP`
<a id="insn-008fb7b8"></a> `008fb7b8` | `40 1d 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-008fb7bc"></a> `008fb7bc` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-008fb7c0"></a> `008fb7c0` | `a4 70 0d 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb7c4"></a> `008fb7c4` | `20 c9 ff 34` | cbz w0,0x008fb0e8 | `CONDITIONAL_JUMP`
<a id="insn-008fb7c8"></a> `008fb7c8` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-008fb7cc"></a> `008fb7cc` | `00 dc ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-008fb7d0"></a> `008fb7d0` | `00 d0 35 91` | add x0,x0,#0xd74 | `FALL_THROUGH`
<a id="insn-008fb7d4"></a> `008fb7d4` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-008fb7d8"></a> `008fb7d8` | `22 1b 00 f0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-008fb7dc"></a> `008fb7dc` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-008fb7e0"></a> `008fb7e0` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-008fb7e4"></a> `008fb7e4` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-008fb7e8"></a> `008fb7e8` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-008fb7ec"></a> `008fb7ec` | `bf fe 02 a9` | stp xzr,xzr,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-008fb7f0"></a> `008fb7f0` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-008fb7f4"></a> `008fb7f4` | `bf 22 01 a9` | stp xzr,x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-008fb7f8"></a> `008fb7f8` | `8e 70 0d 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-008fb7fc"></a> `008fb7fc` | `40 1d 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-008fb800"></a> `008fb800` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-008fb804"></a> `008fb804` | `9b 70 0d 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-008fb808"></a> `008fb808` | `38 fe ff 17` | b 0x008fb0e8 | `UNCONDITIONAL_JUMP`
<a id="insn-008fb80c"></a> `008fb80c` | `40 1d 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-008fb810"></a> `008fb810` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-008fb814"></a> `008fb814` | `8f 70 0d 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb818"></a> `008fb818` | `00 cf ff 34` | cbz w0,0x008fb1f8 | `CONDITIONAL_JUMP`
<a id="insn-008fb81c"></a> `008fb81c` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-008fb820"></a> `008fb820` | `00 dc ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-008fb824"></a> `008fb824` | `00 d0 35 91` | add x0,x0,#0xd74 | `FALL_THROUGH`
<a id="insn-008fb828"></a> `008fb828` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-008fb82c"></a> `008fb82c` | `22 1b 00 f0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-008fb830"></a> `008fb830` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-008fb834"></a> `008fb834` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-008fb838"></a> `008fb838` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-008fb83c"></a> `008fb83c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-008fb840"></a> `008fb840` | `bf fe 02 a9` | stp xzr,xzr,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-008fb844"></a> `008fb844` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-008fb848"></a> `008fb848` | `bf 22 01 a9` | stp xzr,x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-008fb84c"></a> `008fb84c` | `79 70 0d 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-008fb850"></a> `008fb850` | `40 1d 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-008fb854"></a> `008fb854` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-008fb858"></a> `008fb858` | `86 70 0d 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-008fb85c"></a> `008fb85c` | `67 fe ff 17` | b 0x008fb1f8 | `UNCONDITIONAL_JUMP`
<a id="insn-008fb860"></a> `008fb860` | `40 1d 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-008fb864"></a> `008fb864` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-008fb868"></a> `008fb868` | `7a 70 0d 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb86c"></a> `008fb86c` | `e0 d4 ff 34` | cbz w0,0x008fb308 | `CONDITIONAL_JUMP`
<a id="insn-008fb870"></a> `008fb870` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-008fb874"></a> `008fb874` | `00 dc ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-008fb878"></a> `008fb878` | `00 d0 35 91` | add x0,x0,#0xd74 | `FALL_THROUGH`
<a id="insn-008fb87c"></a> `008fb87c` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-008fb880"></a> `008fb880` | `22 1b 00 f0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-008fb884"></a> `008fb884` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-008fb888"></a> `008fb888` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-008fb88c"></a> `008fb88c` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-008fb890"></a> `008fb890` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-008fb894"></a> `008fb894` | `bf fe 02 a9` | stp xzr,xzr,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-008fb898"></a> `008fb898` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-008fb89c"></a> `008fb89c` | `bf 22 01 a9` | stp xzr,x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-008fb8a0"></a> `008fb8a0` | `64 70 0d 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-008fb8a4"></a> `008fb8a4` | `40 1d 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-008fb8a8"></a> `008fb8a8` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-008fb8ac"></a> `008fb8ac` | `71 70 0d 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-008fb8b0"></a> `008fb8b0` | `96 fe ff 17` | b 0x008fb308 | `UNCONDITIONAL_JUMP`
<a id="insn-008fb8b4"></a> `008fb8b4` | `40 1d 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-008fb8b8"></a> `008fb8b8` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-008fb8bc"></a> `008fb8bc` | `65 70 0d 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb8c0"></a> `008fb8c0` | `e0 dc ff 34` | cbz w0,0x008fb45c | `CONDITIONAL_JUMP`
<a id="insn-008fb8c4"></a> `008fb8c4` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-008fb8c8"></a> `008fb8c8` | `00 dc ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-008fb8cc"></a> `008fb8cc` | `00 d0 35 91` | add x0,x0,#0xd74 | `FALL_THROUGH`
<a id="insn-008fb8d0"></a> `008fb8d0` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-008fb8d4"></a> `008fb8d4` | `22 1b 00 f0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-008fb8d8"></a> `008fb8d8` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-008fb8dc"></a> `008fb8dc` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-008fb8e0"></a> `008fb8e0` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-008fb8e4"></a> `008fb8e4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-008fb8e8"></a> `008fb8e8` | `bf fe 02 a9` | stp xzr,xzr,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-008fb8ec"></a> `008fb8ec` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-008fb8f0"></a> `008fb8f0` | `bf 22 01 a9` | stp xzr,x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-008fb8f4"></a> `008fb8f4` | `4f 70 0d 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-008fb8f8"></a> `008fb8f8` | `40 1d 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-008fb8fc"></a> `008fb8fc` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-008fb900"></a> `008fb900` | `5c 70 0d 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-008fb904"></a> `008fb904` | `d6 fe ff 17` | b 0x008fb45c | `UNCONDITIONAL_JUMP`
<a id="insn-008fb908"></a> `008fb908` | `40 1d 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-008fb90c"></a> `008fb90c` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-008fb910"></a> `008fb910` | `50 70 0d 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-008fb914"></a> `008fb914` | `20 e4 ff 34` | cbz w0,0x008fb598 | `CONDITIONAL_JUMP`
<a id="insn-008fb918"></a> `008fb918` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-008fb91c"></a> `008fb91c` | `00 dc ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-008fb920"></a> `008fb920` | `00 d0 35 91` | add x0,x0,#0xd74 | `FALL_THROUGH`
<a id="insn-008fb924"></a> `008fb924` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-008fb928"></a> `008fb928` | `22 1b 00 f0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-008fb92c"></a> `008fb92c` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-008fb930"></a> `008fb930` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-008fb934"></a> `008fb934` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-008fb938"></a> `008fb938` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-008fb93c"></a> `008fb93c` | `9f fe 02 a9` | stp xzr,xzr,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-008fb940"></a> `008fb940` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-008fb944"></a> `008fb944` | `9f 22 01 a9` | stp xzr,x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-008fb948"></a> `008fb948` | `3a 70 0d 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-008fb94c"></a> `008fb94c` | `40 1d 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-008fb950"></a> `008fb950` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-008fb954"></a> `008fb954` | `47 70 0d 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-008fb958"></a> `008fb958` | `10 ff ff 17` | b 0x008fb598 | `UNCONDITIONAL_JUMP`
<a id="insn-008fb9cc"></a> `008fb9cc` | `45 70 0d 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008facec`](#insn-008facec) 範囲 `[['008facec', '008fad43']]`
  - `CONDITIONAL_JUMP` [`008fad40`](#insn-008fad40) → [`008fb6b8`](#insn-008fb6b8)
  - `FALL_THROUGH` [`008fad40`](#insn-008fad40) → [`008fad44`](#insn-008fad44)
- ブロック [`008fad44`](#insn-008fad44) 範囲 `[['008fad44', '008fad9f']]`
  - `FALL_THROUGH` [`008fad9c`](#insn-008fad9c) → [`008fada0`](#insn-008fada0)
- ブロック [`008fada0`](#insn-008fada0) 範囲 `[['008fada0', '008fadbf']]`
  - `CONDITIONAL_JUMP` [`008fadbc`](#insn-008fadbc) → [`008fade8`](#insn-008fade8)
  - `FALL_THROUGH` [`008fadbc`](#insn-008fadbc) → [`008fadc0`](#insn-008fadc0)
- ブロック [`008fadc0`](#insn-008fadc0) 範囲 `[['008fadc0', '008fadc3']]`
  - `FALL_THROUGH` [`008fadc0`](#insn-008fadc0) → [`008fadc4`](#insn-008fadc4)
- ブロック [`008fadc4`](#insn-008fadc4) 範囲 `[['008fadc4', '008fadcf']]`
  - `CONDITIONAL_JUMP` [`008fadcc`](#insn-008fadcc) → [`008fade8`](#insn-008fade8)
  - `FALL_THROUGH` [`008fadcc`](#insn-008fadcc) → [`008fadd0`](#insn-008fadd0)
- ブロック [`008fadd0`](#insn-008fadd0) 範囲 `[['008fadd0', '008fade7']]`
  - `FALL_THROUGH` [`008fade4`](#insn-008fade4) → [`008fade8`](#insn-008fade8)
- ブロック [`008fade8`](#insn-008fade8) 範囲 `[['008fade8', '008fadef']]`
  - `CONDITIONAL_JUMP` [`008fadec`](#insn-008fadec) → [`008fae00`](#insn-008fae00)
  - `FALL_THROUGH` [`008fadec`](#insn-008fadec) → [`008fadf0`](#insn-008fadf0)
- ブロック [`008fadf0`](#insn-008fadf0) 範囲 `[['008fadf0', '008fadff']]`
  - `CONDITIONAL_JUMP` [`008fadfc`](#insn-008fadfc) → [`008faf70`](#insn-008faf70)
  - `FALL_THROUGH` [`008fadfc`](#insn-008fadfc) → [`008fae00`](#insn-008fae00)
- ブロック [`008fae00`](#insn-008fae00) 範囲 `[['008fae00', '008fae07']]`
  - `CONDITIONAL_JUMP` [`008fae04`](#insn-008fae04) → [`008fae10`](#insn-008fae10)
  - `FALL_THROUGH` [`008fae04`](#insn-008fae04) → [`008fae08`](#insn-008fae08)
- ブロック [`008fae08`](#insn-008fae08) 範囲 `[['008fae08', '008fae0f']]`
  - `FALL_THROUGH` [`008fae0c`](#insn-008fae0c) → [`008fae10`](#insn-008fae10)
- ブロック [`008fae10`](#insn-008fae10) 範囲 `[['008fae10', '008fae17']]`
  - `CONDITIONAL_JUMP` [`008fae14`](#insn-008fae14) → [`008fae20`](#insn-008fae20)
  - `FALL_THROUGH` [`008fae14`](#insn-008fae14) → [`008fae18`](#insn-008fae18)
- ブロック [`008fae18`](#insn-008fae18) 範囲 `[['008fae18', '008fae1f']]`
  - `FALL_THROUGH` [`008fae1c`](#insn-008fae1c) → [`008fae20`](#insn-008fae20)
- ブロック [`008fae20`](#insn-008fae20) 範囲 `[['008fae20', '008fae3b']]`
  - `FALL_THROUGH` [`008fae38`](#insn-008fae38) → [`008fae3c`](#insn-008fae3c)
- ブロック [`008fae3c`](#insn-008fae3c) 範囲 `[['008fae3c', '008fae3f']]`
  - `CONDITIONAL_JUMP` [`008fae3c`](#insn-008fae3c) → [`008fae68`](#insn-008fae68)
  - `FALL_THROUGH` [`008fae3c`](#insn-008fae3c) → [`008fae40`](#insn-008fae40)
- ブロック [`008fae40`](#insn-008fae40) 範囲 `[['008fae40', '008fae4b']]`
  - `FALL_THROUGH` [`008fae48`](#insn-008fae48) → [`008fae4c`](#insn-008fae4c)
- ブロック [`008fae4c`](#insn-008fae4c) 範囲 `[['008fae4c', '008fae4f']]`
  - `CONDITIONAL_JUMP` [`008fae4c`](#insn-008fae4c) → [`008fae68`](#insn-008fae68)
  - `FALL_THROUGH` [`008fae4c`](#insn-008fae4c) → [`008fae50`](#insn-008fae50)
- ブロック [`008fae50`](#insn-008fae50) 範囲 `[['008fae50', '008fae67']]`
  - `FALL_THROUGH` [`008fae64`](#insn-008fae64) → [`008fae68`](#insn-008fae68)
- ブロック [`008fae68`](#insn-008fae68) 範囲 `[['008fae68', '008fae6f']]`
  - `CONDITIONAL_JUMP` [`008fae6c`](#insn-008fae6c) → [`008fae98`](#insn-008fae98)
  - `FALL_THROUGH` [`008fae6c`](#insn-008fae6c) → [`008fae70`](#insn-008fae70)
- ブロック [`008fae70`](#insn-008fae70) 範囲 `[['008fae70', '008fae7f']]`
  - `CONDITIONAL_JUMP` [`008fae7c`](#insn-008fae7c) → [`008fae98`](#insn-008fae98)
  - `FALL_THROUGH` [`008fae7c`](#insn-008fae7c) → [`008fae80`](#insn-008fae80)
- ブロック [`008fae80`](#insn-008fae80) 範囲 `[['008fae80', '008fae97']]`
  - `FALL_THROUGH` [`008fae94`](#insn-008fae94) → [`008fae98`](#insn-008fae98)
- ブロック [`008fae98`](#insn-008fae98) 範囲 `[['008fae98', '008fae9f']]`
  - `CONDITIONAL_JUMP` [`008fae9c`](#insn-008fae9c) → [`008fb710`](#insn-008fb710)
  - `FALL_THROUGH` [`008fae9c`](#insn-008fae9c) → [`008faea0`](#insn-008faea0)
- ブロック [`008faea0`](#insn-008faea0) 範囲 `[['008faea0', '008faefb']]`
  - `FALL_THROUGH` [`008faef8`](#insn-008faef8) → [`008faefc`](#insn-008faefc)
- ブロック [`008faefc`](#insn-008faefc) 範囲 `[['008faefc', '008faf13']]`
  - `CONDITIONAL_JUMP` [`008faf10`](#insn-008faf10) → [`008faf3c`](#insn-008faf3c)
  - `FALL_THROUGH` [`008faf10`](#insn-008faf10) → [`008faf14`](#insn-008faf14)
- ブロック [`008faf14`](#insn-008faf14) 範囲 `[['008faf14', '008faf23']]`
  - `CONDITIONAL_JUMP` [`008faf20`](#insn-008faf20) → [`008faf3c`](#insn-008faf3c)
  - `FALL_THROUGH` [`008faf20`](#insn-008faf20) → [`008faf24`](#insn-008faf24)
- ブロック [`008faf24`](#insn-008faf24) 範囲 `[['008faf24', '008faf3b']]`
  - `FALL_THROUGH` [`008faf38`](#insn-008faf38) → [`008faf3c`](#insn-008faf3c)
- ブロック [`008faf3c`](#insn-008faf3c) 範囲 `[['008faf3c', '008faf43']]`
  - `CONDITIONAL_JUMP` [`008faf40`](#insn-008faf40) → [`008faf54`](#insn-008faf54)
  - `FALL_THROUGH` [`008faf40`](#insn-008faf40) → [`008faf44`](#insn-008faf44)
- ブロック [`008faf44`](#insn-008faf44) 範囲 `[['008faf44', '008faf53']]`
  - `CONDITIONAL_JUMP` [`008faf50`](#insn-008faf50) → [`008faf94`](#insn-008faf94)
  - `FALL_THROUGH` [`008faf50`](#insn-008faf50) → [`008faf54`](#insn-008faf54)
- ブロック [`008faf54`](#insn-008faf54) 範囲 `[['008faf54', '008faf57']]`
  - `FALL_THROUGH` [`008faf54`](#insn-008faf54) → [`008faf58`](#insn-008faf58)
- ブロック [`008faf58`](#insn-008faf58) 範囲 `[['008faf58', '008faf5b']]`
  - `CONDITIONAL_JUMP` [`008faf58`](#insn-008faf58) → [`008fafb4`](#insn-008fafb4)
  - `FALL_THROUGH` [`008faf58`](#insn-008faf58) → [`008faf5c`](#insn-008faf5c)
- ブロック [`008faf5c`](#insn-008faf5c) 範囲 `[['008faf5c', '008faf63']]`
  - `CONDITIONAL_JUMP` [`008faf60`](#insn-008faf60) → [`008fafc4`](#insn-008fafc4)
  - `FALL_THROUGH` [`008faf60`](#insn-008faf60) → [`008faf64`](#insn-008faf64)
- ブロック [`008faf64`](#insn-008faf64) 範囲 `[['008faf64', '008faf6b']]`
  - `CONDITIONAL_JUMP` [`008faf68`](#insn-008faf68) → [`008fafd4`](#insn-008fafd4)
  - `FALL_THROUGH` [`008faf68`](#insn-008faf68) → [`008faf6c`](#insn-008faf6c)
- ブロック [`008faf6c`](#insn-008faf6c) 範囲 `[['008faf6c', '008faf6f']]`
  - `UNCONDITIONAL_JUMP` [`008faf6c`](#insn-008faf6c) → [`008fb764`](#insn-008fb764)
- ブロック [`008faf70`](#insn-008faf70) 範囲 `[['008faf70', '008faf83']]`
  - `FALL_THROUGH` [`008faf80`](#insn-008faf80) → [`008faf84`](#insn-008faf84)
- ブロック [`008faf84`](#insn-008faf84) 範囲 `[['008faf84', '008faf8f']]`
  - `CONDITIONAL_JUMP` [`008faf8c`](#insn-008faf8c) → [`008fae08`](#insn-008fae08)
  - `FALL_THROUGH` [`008faf8c`](#insn-008faf8c) → [`008faf90`](#insn-008faf90)
- ブロック [`008faf90`](#insn-008faf90) 範囲 `[['008faf90', '008faf93']]`
  - `UNCONDITIONAL_JUMP` [`008faf90`](#insn-008faf90) → [`008fae10`](#insn-008fae10)
- ブロック [`008faf94`](#insn-008faf94) 範囲 `[['008faf94', '008fafb3']]`
  - `CONDITIONAL_JUMP` [`008fafb0`](#insn-008fafb0) → [`008faf5c`](#insn-008faf5c)
  - `FALL_THROUGH` [`008fafb0`](#insn-008fafb0) → [`008fafb4`](#insn-008fafb4)
- ブロック [`008fafb4`](#insn-008fafb4) 範囲 `[['008fafb4', '008fafc3']]`
  - `CONDITIONAL_JUMP` [`008fafc0`](#insn-008fafc0) → [`008faf64`](#insn-008faf64)
  - `FALL_THROUGH` [`008fafc0`](#insn-008fafc0) → [`008fafc4`](#insn-008fafc4)
- ブロック [`008fafc4`](#insn-008fafc4) 範囲 `[['008fafc4', '008fafd3']]`
  - `CONDITIONAL_JUMP` [`008fafd0`](#insn-008fafd0) → [`008fb764`](#insn-008fb764)
  - `FALL_THROUGH` [`008fafd0`](#insn-008fafd0) → [`008fafd4`](#insn-008fafd4)
- ブロック [`008fafd4`](#insn-008fafd4) 範囲 `[['008fafd4', '008fb04b']]`
  - `CONDITIONAL_JUMP` [`008fb048`](#insn-008fb048) → [`008fb074`](#insn-008fb074)
  - `FALL_THROUGH` [`008fb048`](#insn-008fb048) → [`008fb04c`](#insn-008fb04c)
- ブロック [`008fb04c`](#insn-008fb04c) 範囲 `[['008fb04c', '008fb05b']]`
  - `CONDITIONAL_JUMP` [`008fb058`](#insn-008fb058) → [`008fb074`](#insn-008fb074)
  - `FALL_THROUGH` [`008fb058`](#insn-008fb058) → [`008fb05c`](#insn-008fb05c)
- ブロック [`008fb05c`](#insn-008fb05c) 範囲 `[['008fb05c', '008fb073']]`
  - `FALL_THROUGH` [`008fb070`](#insn-008fb070) → [`008fb074`](#insn-008fb074)
- ブロック [`008fb074`](#insn-008fb074) 範囲 `[['008fb074', '008fb07b']]`
  - `CONDITIONAL_JUMP` [`008fb078`](#insn-008fb078) → [`008fb08c`](#insn-008fb08c)
  - `FALL_THROUGH` [`008fb078`](#insn-008fb078) → [`008fb07c`](#insn-008fb07c)
- ブロック [`008fb07c`](#insn-008fb07c) 範囲 `[['008fb07c', '008fb08b']]`
  - `CONDITIONAL_JUMP` [`008fb088`](#insn-008fb088) → [`008fb0a8`](#insn-008fb0a8)
  - `FALL_THROUGH` [`008fb088`](#insn-008fb088) → [`008fb08c`](#insn-008fb08c)
- ブロック [`008fb08c`](#insn-008fb08c) 範囲 `[['008fb08c', '008fb093']]`
  - `CONDITIONAL_JUMP` [`008fb090`](#insn-008fb090) → [`008fb0c8`](#insn-008fb0c8)
  - `FALL_THROUGH` [`008fb090`](#insn-008fb090) → [`008fb094`](#insn-008fb094)
- ブロック [`008fb094`](#insn-008fb094) 範囲 `[['008fb094', '008fb09b']]`
  - `CONDITIONAL_JUMP` [`008fb098`](#insn-008fb098) → [`008fb0d8`](#insn-008fb0d8)
  - `FALL_THROUGH` [`008fb098`](#insn-008fb098) → [`008fb09c`](#insn-008fb09c)
- ブロック [`008fb09c`](#insn-008fb09c) 範囲 `[['008fb09c', '008fb0a3']]`
  - `CONDITIONAL_JUMP` [`008fb0a0`](#insn-008fb0a0) → [`008fb0e8`](#insn-008fb0e8)
  - `FALL_THROUGH` [`008fb0a0`](#insn-008fb0a0) → [`008fb0a4`](#insn-008fb0a4)
- ブロック [`008fb0a4`](#insn-008fb0a4) 範囲 `[['008fb0a4', '008fb0a7']]`
  - `UNCONDITIONAL_JUMP` [`008fb0a4`](#insn-008fb0a4) → [`008fb7b8`](#insn-008fb7b8)
- ブロック [`008fb0a8`](#insn-008fb0a8) 範囲 `[['008fb0a8', '008fb0c7']]`
  - `CONDITIONAL_JUMP` [`008fb0c4`](#insn-008fb0c4) → [`008fb094`](#insn-008fb094)
  - `FALL_THROUGH` [`008fb0c4`](#insn-008fb0c4) → [`008fb0c8`](#insn-008fb0c8)
- ブロック [`008fb0c8`](#insn-008fb0c8) 範囲 `[['008fb0c8', '008fb0d7']]`
  - `CONDITIONAL_JUMP` [`008fb0d4`](#insn-008fb0d4) → [`008fb09c`](#insn-008fb09c)
  - `FALL_THROUGH` [`008fb0d4`](#insn-008fb0d4) → [`008fb0d8`](#insn-008fb0d8)
- ブロック [`008fb0d8`](#insn-008fb0d8) 範囲 `[['008fb0d8', '008fb0e7']]`
  - `CONDITIONAL_JUMP` [`008fb0e4`](#insn-008fb0e4) → [`008fb7b8`](#insn-008fb7b8)
  - `FALL_THROUGH` [`008fb0e4`](#insn-008fb0e4) → [`008fb0e8`](#insn-008fb0e8)
- ブロック [`008fb0e8`](#insn-008fb0e8) 範囲 `[['008fb0e8', '008fb15b']]`
  - `CONDITIONAL_JUMP` [`008fb158`](#insn-008fb158) → [`008fb184`](#insn-008fb184)
  - `FALL_THROUGH` [`008fb158`](#insn-008fb158) → [`008fb15c`](#insn-008fb15c)
- ブロック [`008fb15c`](#insn-008fb15c) 範囲 `[['008fb15c', '008fb16b']]`
  - `CONDITIONAL_JUMP` [`008fb168`](#insn-008fb168) → [`008fb184`](#insn-008fb184)
  - `FALL_THROUGH` [`008fb168`](#insn-008fb168) → [`008fb16c`](#insn-008fb16c)
- ブロック [`008fb16c`](#insn-008fb16c) 範囲 `[['008fb16c', '008fb183']]`
  - `FALL_THROUGH` [`008fb180`](#insn-008fb180) → [`008fb184`](#insn-008fb184)
- ブロック [`008fb184`](#insn-008fb184) 範囲 `[['008fb184', '008fb18b']]`
  - `CONDITIONAL_JUMP` [`008fb188`](#insn-008fb188) → [`008fb19c`](#insn-008fb19c)
  - `FALL_THROUGH` [`008fb188`](#insn-008fb188) → [`008fb18c`](#insn-008fb18c)
- ブロック [`008fb18c`](#insn-008fb18c) 範囲 `[['008fb18c', '008fb19b']]`
  - `CONDITIONAL_JUMP` [`008fb198`](#insn-008fb198) → [`008fb1b8`](#insn-008fb1b8)
  - `FALL_THROUGH` [`008fb198`](#insn-008fb198) → [`008fb19c`](#insn-008fb19c)
- ブロック [`008fb19c`](#insn-008fb19c) 範囲 `[['008fb19c', '008fb1a3']]`
  - `CONDITIONAL_JUMP` [`008fb1a0`](#insn-008fb1a0) → [`008fb1d8`](#insn-008fb1d8)
  - `FALL_THROUGH` [`008fb1a0`](#insn-008fb1a0) → [`008fb1a4`](#insn-008fb1a4)
- ブロック [`008fb1a4`](#insn-008fb1a4) 範囲 `[['008fb1a4', '008fb1ab']]`
  - `CONDITIONAL_JUMP` [`008fb1a8`](#insn-008fb1a8) → [`008fb1e8`](#insn-008fb1e8)
  - `FALL_THROUGH` [`008fb1a8`](#insn-008fb1a8) → [`008fb1ac`](#insn-008fb1ac)
- ブロック [`008fb1ac`](#insn-008fb1ac) 範囲 `[['008fb1ac', '008fb1b3']]`
  - `CONDITIONAL_JUMP` [`008fb1b0`](#insn-008fb1b0) → [`008fb1f8`](#insn-008fb1f8)
  - `FALL_THROUGH` [`008fb1b0`](#insn-008fb1b0) → [`008fb1b4`](#insn-008fb1b4)
- ブロック [`008fb1b4`](#insn-008fb1b4) 範囲 `[['008fb1b4', '008fb1b7']]`
  - `UNCONDITIONAL_JUMP` [`008fb1b4`](#insn-008fb1b4) → [`008fb80c`](#insn-008fb80c)
- ブロック [`008fb1b8`](#insn-008fb1b8) 範囲 `[['008fb1b8', '008fb1d7']]`
  - `CONDITIONAL_JUMP` [`008fb1d4`](#insn-008fb1d4) → [`008fb1a4`](#insn-008fb1a4)
  - `FALL_THROUGH` [`008fb1d4`](#insn-008fb1d4) → [`008fb1d8`](#insn-008fb1d8)
- ブロック [`008fb1d8`](#insn-008fb1d8) 範囲 `[['008fb1d8', '008fb1e7']]`
  - `CONDITIONAL_JUMP` [`008fb1e4`](#insn-008fb1e4) → [`008fb1ac`](#insn-008fb1ac)
  - `FALL_THROUGH` [`008fb1e4`](#insn-008fb1e4) → [`008fb1e8`](#insn-008fb1e8)
- ブロック [`008fb1e8`](#insn-008fb1e8) 範囲 `[['008fb1e8', '008fb1f7']]`
  - `CONDITIONAL_JUMP` [`008fb1f4`](#insn-008fb1f4) → [`008fb80c`](#insn-008fb80c)
  - `FALL_THROUGH` [`008fb1f4`](#insn-008fb1f4) → [`008fb1f8`](#insn-008fb1f8)
- ブロック [`008fb1f8`](#insn-008fb1f8) 範囲 `[['008fb1f8', '008fb26b']]`
  - `CONDITIONAL_JUMP` [`008fb268`](#insn-008fb268) → [`008fb294`](#insn-008fb294)
  - `FALL_THROUGH` [`008fb268`](#insn-008fb268) → [`008fb26c`](#insn-008fb26c)
- ブロック [`008fb26c`](#insn-008fb26c) 範囲 `[['008fb26c', '008fb27b']]`
  - `CONDITIONAL_JUMP` [`008fb278`](#insn-008fb278) → [`008fb294`](#insn-008fb294)
  - `FALL_THROUGH` [`008fb278`](#insn-008fb278) → [`008fb27c`](#insn-008fb27c)
- ブロック [`008fb27c`](#insn-008fb27c) 範囲 `[['008fb27c', '008fb293']]`
  - `FALL_THROUGH` [`008fb290`](#insn-008fb290) → [`008fb294`](#insn-008fb294)
- ブロック [`008fb294`](#insn-008fb294) 範囲 `[['008fb294', '008fb29b']]`
  - `CONDITIONAL_JUMP` [`008fb298`](#insn-008fb298) → [`008fb2ac`](#insn-008fb2ac)
  - `FALL_THROUGH` [`008fb298`](#insn-008fb298) → [`008fb29c`](#insn-008fb29c)
- ブロック [`008fb29c`](#insn-008fb29c) 範囲 `[['008fb29c', '008fb2ab']]`
  - `CONDITIONAL_JUMP` [`008fb2a8`](#insn-008fb2a8) → [`008fb2c8`](#insn-008fb2c8)
  - `FALL_THROUGH` [`008fb2a8`](#insn-008fb2a8) → [`008fb2ac`](#insn-008fb2ac)
- ブロック [`008fb2ac`](#insn-008fb2ac) 範囲 `[['008fb2ac', '008fb2b3']]`
  - `CONDITIONAL_JUMP` [`008fb2b0`](#insn-008fb2b0) → [`008fb2e8`](#insn-008fb2e8)
  - `FALL_THROUGH` [`008fb2b0`](#insn-008fb2b0) → [`008fb2b4`](#insn-008fb2b4)
- ブロック [`008fb2b4`](#insn-008fb2b4) 範囲 `[['008fb2b4', '008fb2bb']]`
  - `CONDITIONAL_JUMP` [`008fb2b8`](#insn-008fb2b8) → [`008fb2f8`](#insn-008fb2f8)
  - `FALL_THROUGH` [`008fb2b8`](#insn-008fb2b8) → [`008fb2bc`](#insn-008fb2bc)
- ブロック [`008fb2bc`](#insn-008fb2bc) 範囲 `[['008fb2bc', '008fb2c3']]`
  - `CONDITIONAL_JUMP` [`008fb2c0`](#insn-008fb2c0) → [`008fb308`](#insn-008fb308)
  - `FALL_THROUGH` [`008fb2c0`](#insn-008fb2c0) → [`008fb2c4`](#insn-008fb2c4)
- ブロック [`008fb2c4`](#insn-008fb2c4) 範囲 `[['008fb2c4', '008fb2c7']]`
  - `UNCONDITIONAL_JUMP` [`008fb2c4`](#insn-008fb2c4) → [`008fb860`](#insn-008fb860)
- ブロック [`008fb2c8`](#insn-008fb2c8) 範囲 `[['008fb2c8', '008fb2e7']]`
  - `CONDITIONAL_JUMP` [`008fb2e4`](#insn-008fb2e4) → [`008fb2b4`](#insn-008fb2b4)
  - `FALL_THROUGH` [`008fb2e4`](#insn-008fb2e4) → [`008fb2e8`](#insn-008fb2e8)
- ブロック [`008fb2e8`](#insn-008fb2e8) 範囲 `[['008fb2e8', '008fb2f7']]`
  - `CONDITIONAL_JUMP` [`008fb2f4`](#insn-008fb2f4) → [`008fb2bc`](#insn-008fb2bc)
  - `FALL_THROUGH` [`008fb2f4`](#insn-008fb2f4) → [`008fb2f8`](#insn-008fb2f8)
- ブロック [`008fb2f8`](#insn-008fb2f8) 範囲 `[['008fb2f8', '008fb307']]`
  - `CONDITIONAL_JUMP` [`008fb304`](#insn-008fb304) → [`008fb860`](#insn-008fb860)
  - `FALL_THROUGH` [`008fb304`](#insn-008fb304) → [`008fb308`](#insn-008fb308)
- ブロック [`008fb308`](#insn-008fb308) 範囲 `[['008fb308', '008fb37b']]`
  - `CONDITIONAL_JUMP` [`008fb378`](#insn-008fb378) → [`008fb3a4`](#insn-008fb3a4)
  - `FALL_THROUGH` [`008fb378`](#insn-008fb378) → [`008fb37c`](#insn-008fb37c)
- ブロック [`008fb37c`](#insn-008fb37c) 範囲 `[['008fb37c', '008fb38b']]`
  - `CONDITIONAL_JUMP` [`008fb388`](#insn-008fb388) → [`008fb3a4`](#insn-008fb3a4)
  - `FALL_THROUGH` [`008fb388`](#insn-008fb388) → [`008fb38c`](#insn-008fb38c)
- ブロック [`008fb38c`](#insn-008fb38c) 範囲 `[['008fb38c', '008fb3a3']]`
  - `FALL_THROUGH` [`008fb3a0`](#insn-008fb3a0) → [`008fb3a4`](#insn-008fb3a4)
- ブロック [`008fb3a4`](#insn-008fb3a4) 範囲 `[['008fb3a4', '008fb3ab']]`
  - `CONDITIONAL_JUMP` [`008fb3a8`](#insn-008fb3a8) → [`008fb3bc`](#insn-008fb3bc)
  - `FALL_THROUGH` [`008fb3a8`](#insn-008fb3a8) → [`008fb3ac`](#insn-008fb3ac)
- ブロック [`008fb3ac`](#insn-008fb3ac) 範囲 `[['008fb3ac', '008fb3bb']]`
  - `CONDITIONAL_JUMP` [`008fb3b8`](#insn-008fb3b8) → [`008fb534`](#insn-008fb534)
  - `FALL_THROUGH` [`008fb3b8`](#insn-008fb3b8) → [`008fb3bc`](#insn-008fb3bc)
- ブロック [`008fb3bc`](#insn-008fb3bc) 範囲 `[['008fb3bc', '008fb3c3']]`
  - `CONDITIONAL_JUMP` [`008fb3c0`](#insn-008fb3c0) → [`008fb3cc`](#insn-008fb3cc)
  - `FALL_THROUGH` [`008fb3c0`](#insn-008fb3c0) → [`008fb3c4`](#insn-008fb3c4)
- ブロック [`008fb3c4`](#insn-008fb3c4) 範囲 `[['008fb3c4', '008fb3cb']]`
  - `FALL_THROUGH` [`008fb3c8`](#insn-008fb3c8) → [`008fb3cc`](#insn-008fb3cc)
- ブロック [`008fb3cc`](#insn-008fb3cc) 範囲 `[['008fb3cc', '008fb3d3']]`
  - `CONDITIONAL_JUMP` [`008fb3d0`](#insn-008fb3d0) → [`008fb3dc`](#insn-008fb3dc)
  - `FALL_THROUGH` [`008fb3d0`](#insn-008fb3d0) → [`008fb3d4`](#insn-008fb3d4)
- ブロック [`008fb3d4`](#insn-008fb3d4) 範囲 `[['008fb3d4', '008fb3db']]`
  - `FALL_THROUGH` [`008fb3d8`](#insn-008fb3d8) → [`008fb3dc`](#insn-008fb3dc)
- ブロック [`008fb3dc`](#insn-008fb3dc) 範囲 `[['008fb3dc', '008fb3fb']]`
  - `CONDITIONAL_JUMP` [`008fb3f8`](#insn-008fb3f8) → [`008fb424`](#insn-008fb424)
  - `FALL_THROUGH` [`008fb3f8`](#insn-008fb3f8) → [`008fb3fc`](#insn-008fb3fc)
- ブロック [`008fb3fc`](#insn-008fb3fc) 範囲 `[['008fb3fc', '008fb40b']]`
  - `CONDITIONAL_JUMP` [`008fb408`](#insn-008fb408) → [`008fb424`](#insn-008fb424)
  - `FALL_THROUGH` [`008fb408`](#insn-008fb408) → [`008fb40c`](#insn-008fb40c)
- ブロック [`008fb40c`](#insn-008fb40c) 範囲 `[['008fb40c', '008fb423']]`
  - `FALL_THROUGH` [`008fb420`](#insn-008fb420) → [`008fb424`](#insn-008fb424)
- ブロック [`008fb424`](#insn-008fb424) 範囲 `[['008fb424', '008fb42b']]`
  - `CONDITIONAL_JUMP` [`008fb428`](#insn-008fb428) → [`008fb454`](#insn-008fb454)
  - `FALL_THROUGH` [`008fb428`](#insn-008fb428) → [`008fb42c`](#insn-008fb42c)
- ブロック [`008fb42c`](#insn-008fb42c) 範囲 `[['008fb42c', '008fb43b']]`
  - `CONDITIONAL_JUMP` [`008fb438`](#insn-008fb438) → [`008fb454`](#insn-008fb454)
  - `FALL_THROUGH` [`008fb438`](#insn-008fb438) → [`008fb43c`](#insn-008fb43c)
- ブロック [`008fb43c`](#insn-008fb43c) 範囲 `[['008fb43c', '008fb453']]`
  - `FALL_THROUGH` [`008fb450`](#insn-008fb450) → [`008fb454`](#insn-008fb454)
- ブロック [`008fb454`](#insn-008fb454) 範囲 `[['008fb454', '008fb45b']]`
  - `CONDITIONAL_JUMP` [`008fb458`](#insn-008fb458) → [`008fb8b4`](#insn-008fb8b4)
  - `FALL_THROUGH` [`008fb458`](#insn-008fb458) → [`008fb45c`](#insn-008fb45c)
- ブロック [`008fb45c`](#insn-008fb45c) 範囲 `[['008fb45c', '008fb4d7']]`
  - `CONDITIONAL_JUMP` [`008fb4d4`](#insn-008fb4d4) → [`008fb500`](#insn-008fb500)
  - `FALL_THROUGH` [`008fb4d4`](#insn-008fb4d4) → [`008fb4d8`](#insn-008fb4d8)
- ブロック [`008fb4d8`](#insn-008fb4d8) 範囲 `[['008fb4d8', '008fb4e7']]`
  - `CONDITIONAL_JUMP` [`008fb4e4`](#insn-008fb4e4) → [`008fb500`](#insn-008fb500)
  - `FALL_THROUGH` [`008fb4e4`](#insn-008fb4e4) → [`008fb4e8`](#insn-008fb4e8)
- ブロック [`008fb4e8`](#insn-008fb4e8) 範囲 `[['008fb4e8', '008fb4ff']]`
  - `FALL_THROUGH` [`008fb4fc`](#insn-008fb4fc) → [`008fb500`](#insn-008fb500)
- ブロック [`008fb500`](#insn-008fb500) 範囲 `[['008fb500', '008fb507']]`
  - `CONDITIONAL_JUMP` [`008fb504`](#insn-008fb504) → [`008fb518`](#insn-008fb518)
  - `FALL_THROUGH` [`008fb504`](#insn-008fb504) → [`008fb508`](#insn-008fb508)
- ブロック [`008fb508`](#insn-008fb508) 範囲 `[['008fb508', '008fb517']]`
  - `CONDITIONAL_JUMP` [`008fb514`](#insn-008fb514) → [`008fb558`](#insn-008fb558)
  - `FALL_THROUGH` [`008fb514`](#insn-008fb514) → [`008fb518`](#insn-008fb518)
- ブロック [`008fb518`](#insn-008fb518) 範囲 `[['008fb518', '008fb51f']]`
  - `CONDITIONAL_JUMP` [`008fb51c`](#insn-008fb51c) → [`008fb578`](#insn-008fb578)
  - `FALL_THROUGH` [`008fb51c`](#insn-008fb51c) → [`008fb520`](#insn-008fb520)
- ブロック [`008fb520`](#insn-008fb520) 範囲 `[['008fb520', '008fb527']]`
  - `CONDITIONAL_JUMP` [`008fb524`](#insn-008fb524) → [`008fb588`](#insn-008fb588)
  - `FALL_THROUGH` [`008fb524`](#insn-008fb524) → [`008fb528`](#insn-008fb528)
- ブロック [`008fb528`](#insn-008fb528) 範囲 `[['008fb528', '008fb52f']]`
  - `CONDITIONAL_JUMP` [`008fb52c`](#insn-008fb52c) → [`008fb598`](#insn-008fb598)
  - `FALL_THROUGH` [`008fb52c`](#insn-008fb52c) → [`008fb530`](#insn-008fb530)
- ブロック [`008fb530`](#insn-008fb530) 範囲 `[['008fb530', '008fb533']]`
  - `UNCONDITIONAL_JUMP` [`008fb530`](#insn-008fb530) → [`008fb908`](#insn-008fb908)
- ブロック [`008fb534`](#insn-008fb534) 範囲 `[['008fb534', '008fb553']]`
  - `CONDITIONAL_JUMP` [`008fb550`](#insn-008fb550) → [`008fb3c4`](#insn-008fb3c4)
  - `FALL_THROUGH` [`008fb550`](#insn-008fb550) → [`008fb554`](#insn-008fb554)
- ブロック [`008fb554`](#insn-008fb554) 範囲 `[['008fb554', '008fb557']]`
  - `UNCONDITIONAL_JUMP` [`008fb554`](#insn-008fb554) → [`008fb3cc`](#insn-008fb3cc)
- ブロック [`008fb558`](#insn-008fb558) 範囲 `[['008fb558', '008fb577']]`
  - `CONDITIONAL_JUMP` [`008fb574`](#insn-008fb574) → [`008fb520`](#insn-008fb520)
  - `FALL_THROUGH` [`008fb574`](#insn-008fb574) → [`008fb578`](#insn-008fb578)
- ブロック [`008fb578`](#insn-008fb578) 範囲 `[['008fb578', '008fb587']]`
  - `CONDITIONAL_JUMP` [`008fb584`](#insn-008fb584) → [`008fb528`](#insn-008fb528)
  - `FALL_THROUGH` [`008fb584`](#insn-008fb584) → [`008fb588`](#insn-008fb588)
- ブロック [`008fb588`](#insn-008fb588) 範囲 `[['008fb588', '008fb597']]`
  - `CONDITIONAL_JUMP` [`008fb594`](#insn-008fb594) → [`008fb908`](#insn-008fb908)
  - `FALL_THROUGH` [`008fb594`](#insn-008fb594) → [`008fb598`](#insn-008fb598)
- ブロック [`008fb598`](#insn-008fb598) 範囲 `[['008fb598', '008fb607']]`
  - `CONDITIONAL_JUMP` [`008fb604`](#insn-008fb604) → [`008fb630`](#insn-008fb630)
  - `FALL_THROUGH` [`008fb604`](#insn-008fb604) → [`008fb608`](#insn-008fb608)
- ブロック [`008fb608`](#insn-008fb608) 範囲 `[['008fb608', '008fb617']]`
  - `CONDITIONAL_JUMP` [`008fb614`](#insn-008fb614) → [`008fb630`](#insn-008fb630)
  - `FALL_THROUGH` [`008fb614`](#insn-008fb614) → [`008fb618`](#insn-008fb618)
- ブロック [`008fb618`](#insn-008fb618) 範囲 `[['008fb618', '008fb62f']]`
  - `FALL_THROUGH` [`008fb62c`](#insn-008fb62c) → [`008fb630`](#insn-008fb630)
- ブロック [`008fb630`](#insn-008fb630) 範囲 `[['008fb630', '008fb637']]`
  - `CONDITIONAL_JUMP` [`008fb634`](#insn-008fb634) → [`008fb648`](#insn-008fb648)
  - `FALL_THROUGH` [`008fb634`](#insn-008fb634) → [`008fb638`](#insn-008fb638)
- ブロック [`008fb638`](#insn-008fb638) 範囲 `[['008fb638', '008fb647']]`
  - `CONDITIONAL_JUMP` [`008fb644`](#insn-008fb644) → [`008fb694`](#insn-008fb694)
  - `FALL_THROUGH` [`008fb644`](#insn-008fb644) → [`008fb648`](#insn-008fb648)
- ブロック [`008fb648`](#insn-008fb648) 範囲 `[['008fb648', '008fb64f']]`
  - `CONDITIONAL_JUMP` [`008fb64c`](#insn-008fb64c) → [`008fb658`](#insn-008fb658)
  - `FALL_THROUGH` [`008fb64c`](#insn-008fb64c) → [`008fb650`](#insn-008fb650)
- ブロック [`008fb650`](#insn-008fb650) 範囲 `[['008fb650', '008fb657']]`
  - `FALL_THROUGH` [`008fb654`](#insn-008fb654) → [`008fb658`](#insn-008fb658)
- ブロック [`008fb658`](#insn-008fb658) 範囲 `[['008fb658', '008fb65f']]`
  - `CONDITIONAL_JUMP` [`008fb65c`](#insn-008fb65c) → [`008fb668`](#insn-008fb668)
  - `FALL_THROUGH` [`008fb65c`](#insn-008fb65c) → [`008fb660`](#insn-008fb660)
- ブロック [`008fb660`](#insn-008fb660) 範囲 `[['008fb660', '008fb667']]`
  - `FALL_THROUGH` [`008fb664`](#insn-008fb664) → [`008fb668`](#insn-008fb668)
- ブロック [`008fb668`](#insn-008fb668) 範囲 `[['008fb668', '008fb677']]`
  - `CONDITIONAL_JUMP` [`008fb674`](#insn-008fb674) → [`008fb9cc`](#insn-008fb9cc)
  - `FALL_THROUGH` [`008fb674`](#insn-008fb674) → [`008fb678`](#insn-008fb678)
- ブロック [`008fb678`](#insn-008fb678) 範囲 `[['008fb678', '008fb693']]`
- ブロック [`008fb694`](#insn-008fb694) 範囲 `[['008fb694', '008fb6b3']]`
  - `CONDITIONAL_JUMP` [`008fb6b0`](#insn-008fb6b0) → [`008fb650`](#insn-008fb650)
  - `FALL_THROUGH` [`008fb6b0`](#insn-008fb6b0) → [`008fb6b4`](#insn-008fb6b4)
- ブロック [`008fb6b4`](#insn-008fb6b4) 範囲 `[['008fb6b4', '008fb6b7']]`
  - `UNCONDITIONAL_JUMP` [`008fb6b4`](#insn-008fb6b4) → [`008fb658`](#insn-008fb658)
- ブロック [`008fb6b8`](#insn-008fb6b8) 範囲 `[['008fb6b8', '008fb6c7']]`
  - `CONDITIONAL_JUMP` [`008fb6c4`](#insn-008fb6c4) → [`008fad44`](#insn-008fad44)
  - `FALL_THROUGH` [`008fb6c4`](#insn-008fb6c4) → [`008fb6c8`](#insn-008fb6c8)
- ブロック [`008fb6c8`](#insn-008fb6c8) 範囲 `[['008fb6c8', '008fb70f']]`
  - `UNCONDITIONAL_JUMP` [`008fb70c`](#insn-008fb70c) → [`008fad44`](#insn-008fad44)
- ブロック [`008fb710`](#insn-008fb710) 範囲 `[['008fb710', '008fb71f']]`
  - `CONDITIONAL_JUMP` [`008fb71c`](#insn-008fb71c) → [`008faea0`](#insn-008faea0)
  - `FALL_THROUGH` [`008fb71c`](#insn-008fb71c) → [`008fb720`](#insn-008fb720)
- ブロック [`008fb720`](#insn-008fb720) 範囲 `[['008fb720', '008fb763']]`
  - `UNCONDITIONAL_JUMP` [`008fb760`](#insn-008fb760) → [`008faea0`](#insn-008faea0)
- ブロック [`008fb764`](#insn-008fb764) 範囲 `[['008fb764', '008fb773']]`
  - `CONDITIONAL_JUMP` [`008fb770`](#insn-008fb770) → [`008fafd4`](#insn-008fafd4)
  - `FALL_THROUGH` [`008fb770`](#insn-008fb770) → [`008fb774`](#insn-008fb774)
- ブロック [`008fb774`](#insn-008fb774) 範囲 `[['008fb774', '008fb7b7']]`
  - `UNCONDITIONAL_JUMP` [`008fb7b4`](#insn-008fb7b4) → [`008fafd4`](#insn-008fafd4)
- ブロック [`008fb7b8`](#insn-008fb7b8) 範囲 `[['008fb7b8', '008fb7c7']]`
  - `CONDITIONAL_JUMP` [`008fb7c4`](#insn-008fb7c4) → [`008fb0e8`](#insn-008fb0e8)
  - `FALL_THROUGH` [`008fb7c4`](#insn-008fb7c4) → [`008fb7c8`](#insn-008fb7c8)
- ブロック [`008fb7c8`](#insn-008fb7c8) 範囲 `[['008fb7c8', '008fb80b']]`
  - `UNCONDITIONAL_JUMP` [`008fb808`](#insn-008fb808) → [`008fb0e8`](#insn-008fb0e8)
- ブロック [`008fb80c`](#insn-008fb80c) 範囲 `[['008fb80c', '008fb81b']]`
  - `CONDITIONAL_JUMP` [`008fb818`](#insn-008fb818) → [`008fb1f8`](#insn-008fb1f8)
  - `FALL_THROUGH` [`008fb818`](#insn-008fb818) → [`008fb81c`](#insn-008fb81c)
- ブロック [`008fb81c`](#insn-008fb81c) 範囲 `[['008fb81c', '008fb85f']]`
  - `UNCONDITIONAL_JUMP` [`008fb85c`](#insn-008fb85c) → [`008fb1f8`](#insn-008fb1f8)
- ブロック [`008fb860`](#insn-008fb860) 範囲 `[['008fb860', '008fb86f']]`
  - `CONDITIONAL_JUMP` [`008fb86c`](#insn-008fb86c) → [`008fb308`](#insn-008fb308)
  - `FALL_THROUGH` [`008fb86c`](#insn-008fb86c) → [`008fb870`](#insn-008fb870)
- ブロック [`008fb870`](#insn-008fb870) 範囲 `[['008fb870', '008fb8b3']]`
  - `UNCONDITIONAL_JUMP` [`008fb8b0`](#insn-008fb8b0) → [`008fb308`](#insn-008fb308)
- ブロック [`008fb8b4`](#insn-008fb8b4) 範囲 `[['008fb8b4', '008fb8c3']]`
  - `CONDITIONAL_JUMP` [`008fb8c0`](#insn-008fb8c0) → [`008fb45c`](#insn-008fb45c)
  - `FALL_THROUGH` [`008fb8c0`](#insn-008fb8c0) → [`008fb8c4`](#insn-008fb8c4)
- ブロック [`008fb8c4`](#insn-008fb8c4) 範囲 `[['008fb8c4', '008fb907']]`
  - `UNCONDITIONAL_JUMP` [`008fb904`](#insn-008fb904) → [`008fb45c`](#insn-008fb45c)
- ブロック [`008fb908`](#insn-008fb908) 範囲 `[['008fb908', '008fb917']]`
  - `CONDITIONAL_JUMP` [`008fb914`](#insn-008fb914) → [`008fb598`](#insn-008fb598)
  - `FALL_THROUGH` [`008fb914`](#insn-008fb914) → [`008fb918`](#insn-008fb918)
- ブロック [`008fb918`](#insn-008fb918) 範囲 `[['008fb918', '008fb95b']]`
  - `UNCONDITIONAL_JUMP` [`008fb958`](#insn-008fb958) → [`008fb598`](#insn-008fb598)
- ブロック [`008fb9cc`](#insn-008fb9cc) 範囲 `[['008fb9cc', '008fb9cf']]`

## 命令位置別の参照

- [`008facf0`](#insn-008facf0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008facf4`](#insn-008facf4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008facf8`](#insn-008facf8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008facfc`](#insn-008facfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fad00`](#insn-008fad00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fad18`](#insn-008fad18) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fad1c`](#insn-008fad1c) → [`00758190`](../00758/00758190.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00758190` · 推定シンボル `None` · 推定型 `None`
- [`008fad30`](#insn-008fad30) → `00c856f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008fad3c`](#insn-008fad3c) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fad40`](#insn-008fad40) → [`008fb6b8`](#insn-008fb6b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fad4c`](#insn-008fad4c) → `Stack[-0x85]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fad50`](#insn-008fad50) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fad5c`](#insn-008fad5c) → `002b634e`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fad60`](#insn-008fad60) → `Stack[-0x87]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fad68`](#insn-008fad68) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fad6c`](#insn-008fad6c) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fad78`](#insn-008fad78) → `002b1ed6`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fad7c`](#insn-008fad7c) → `002b1edb`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fad80`](#insn-008fad80) → `Stack[-0x9a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fad84`](#insn-008fad84) → `Stack[-0xa7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fad88`](#insn-008fad88) → `Stack[-0xa2]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fada0`](#insn-008fada0) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fada8`](#insn-008fada8) → [`00633334`](../00633/00633334.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00633334` · 推定シンボル `None` · 推定型 `None`
- [`008fadac`](#insn-008fadac) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fadb4`](#insn-008fadb4) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fadbc`](#insn-008fadbc) → [`008fade8`](#insn-008fade8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fadc8`](#insn-008fadc8) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`008fadcc`](#insn-008fadcc) → [`008fade8`](#insn-008fade8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fade4`](#insn-008fade4) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`008fade8`](#insn-008fade8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fadec`](#insn-008fadec) → [`008fae00`](#insn-008fae00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fadf8`](#insn-008fadf8) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`008fadfc`](#insn-008fadfc) → [`008faf70`](#insn-008faf70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fae00`](#insn-008fae00) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fae04`](#insn-008fae04) → [`008fae10`](#insn-008fae10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fae08`](#insn-008fae08) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fae0c`](#insn-008fae0c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008fae10`](#insn-008fae10) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fae14`](#insn-008fae14) → [`008fae20`](#insn-008fae20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fae18`](#insn-008fae18) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fae1c`](#insn-008fae1c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008fae28`](#insn-008fae28) → [`008644f8`](../00864/008644f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008644f8` · 推定シンボル `None` · 推定型 `None`
- [`008fae2c`](#insn-008fae2c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fae34`](#insn-008fae34) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fae3c`](#insn-008fae3c) → [`008fae68`](#insn-008fae68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fae48`](#insn-008fae48) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`008fae4c`](#insn-008fae4c) → [`008fae68`](#insn-008fae68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fae64`](#insn-008fae64) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`008fae68`](#insn-008fae68) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fae6c`](#insn-008fae6c) → [`008fae98`](#insn-008fae98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fae78`](#insn-008fae78) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`008fae7c`](#insn-008fae7c) → [`008fae98`](#insn-008fae98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fae94`](#insn-008fae94) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`008fae98`](#insn-008fae98) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fae9c`](#insn-008fae9c) → [`008fb710`](#insn-008fb710) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faea8`](#insn-008faea8) → `Stack[-0x85]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faeac`](#insn-008faeac) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faeb8`](#insn-008faeb8) → `002bef7e`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008faebc`](#insn-008faebc) → `Stack[-0x87]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faec4`](#insn-008faec4) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faec8`](#insn-008faec8) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faed4`](#insn-008faed4) → `002a9ed6`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faed8`](#insn-008faed8) → `002a9edb`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008faedc`](#insn-008faedc) → `Stack[-0x9a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faee0`](#insn-008faee0) → `Stack[-0xa7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faee4`](#insn-008faee4) → `Stack[-0xa2]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faef4`](#insn-008faef4) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008faefc`](#insn-008faefc) → [`00633334`](../00633/00633334.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00633334` · 推定シンボル `None` · 推定型 `None`
- [`008faf00`](#insn-008faf00) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf08`](#insn-008faf08) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf10`](#insn-008faf10) → [`008faf3c`](#insn-008faf3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf1c`](#insn-008faf1c) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`008faf20`](#insn-008faf20) → [`008faf3c`](#insn-008faf3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf38`](#insn-008faf38) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`008faf3c`](#insn-008faf3c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf40`](#insn-008faf40) → [`008faf54`](#insn-008faf54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf4c`](#insn-008faf4c) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`008faf50`](#insn-008faf50) → [`008faf94`](#insn-008faf94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf54`](#insn-008faf54) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf58`](#insn-008faf58) → [`008fafb4`](#insn-008fafb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf5c`](#insn-008faf5c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf60`](#insn-008faf60) → [`008fafc4`](#insn-008fafc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf64`](#insn-008faf64) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008faf68`](#insn-008faf68) → [`008fafd4`](#insn-008fafd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf6c`](#insn-008faf6c) → [`008fb764`](#insn-008fb764) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf84`](#insn-008faf84) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`008faf88`](#insn-008faf88) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf8c`](#insn-008faf8c) → [`008fae08`](#insn-008fae08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faf90`](#insn-008faf90) → [`008fae10`](#insn-008fae10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fafa8`](#insn-008fafa8) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`008fafac`](#insn-008fafac) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fafb0`](#insn-008fafb0) → [`008faf5c`](#insn-008faf5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fafb4`](#insn-008fafb4) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fafb8`](#insn-008fafb8) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008fafbc`](#insn-008fafbc) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fafc0`](#insn-008fafc0) → [`008faf64`](#insn-008faf64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fafc4`](#insn-008fafc4) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fafc8`](#insn-008fafc8) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008fafcc`](#insn-008fafcc) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fafd0`](#insn-008fafd0) → [`008fb764`](#insn-008fb764) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fafdc`](#insn-008fafdc) → `Stack[-0x85]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fafe0`](#insn-008fafe0) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fafec`](#insn-008fafec) → `002bfff6`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008faff0`](#insn-008faff0) → `Stack[-0x87]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faff8`](#insn-008faff8) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008faffc`](#insn-008faffc) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb008`](#insn-008fb008) → `002a9e29`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb00c`](#insn-008fb00c) → `002a9e2e`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb010`](#insn-008fb010) → `Stack[-0x9a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb014`](#insn-008fb014) → `Stack[-0xa7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb018`](#insn-008fb018) → `Stack[-0xa2]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb028`](#insn-008fb028) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb030`](#insn-008fb030) → [`00633334`](../00633/00633334.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00633334` · 推定シンボル `None` · 推定型 `None`
- [`008fb034`](#insn-008fb034) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb040`](#insn-008fb040) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb048`](#insn-008fb048) → [`008fb074`](#insn-008fb074) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb054`](#insn-008fb054) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`008fb058`](#insn-008fb058) → [`008fb074`](#insn-008fb074) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb070`](#insn-008fb070) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`008fb074`](#insn-008fb074) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb078`](#insn-008fb078) → [`008fb08c`](#insn-008fb08c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb084`](#insn-008fb084) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`008fb088`](#insn-008fb088) → [`008fb0a8`](#insn-008fb0a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb08c`](#insn-008fb08c) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb090`](#insn-008fb090) → [`008fb0c8`](#insn-008fb0c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb094`](#insn-008fb094) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb098`](#insn-008fb098) → [`008fb0d8`](#insn-008fb0d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb09c`](#insn-008fb09c) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb0a0`](#insn-008fb0a0) → [`008fb0e8`](#insn-008fb0e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb0a4`](#insn-008fb0a4) → [`008fb7b8`](#insn-008fb7b8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb0bc`](#insn-008fb0bc) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`008fb0c0`](#insn-008fb0c0) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb0c4`](#insn-008fb0c4) → [`008fb094`](#insn-008fb094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb0c8`](#insn-008fb0c8) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb0cc`](#insn-008fb0cc) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008fb0d0`](#insn-008fb0d0) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb0d4`](#insn-008fb0d4) → [`008fb09c`](#insn-008fb09c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb0d8`](#insn-008fb0d8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb0dc`](#insn-008fb0dc) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008fb0e0`](#insn-008fb0e0) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb0e4`](#insn-008fb0e4) → [`008fb7b8`](#insn-008fb7b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb0f0`](#insn-008fb0f0) → `Stack[-0x85]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb0f4`](#insn-008fb0f4) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb100`](#insn-008fb100) → `002b91cf`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb104`](#insn-008fb104) → `Stack[-0x87]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb10c`](#insn-008fb10c) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb110`](#insn-008fb110) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb11c`](#insn-008fb11c) → `002bdbcf`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb120`](#insn-008fb120) → `002bdbd4`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb124`](#insn-008fb124) → `Stack[-0x9a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb128`](#insn-008fb128) → `Stack[-0xa7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb12c`](#insn-008fb12c) → `Stack[-0xa2]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb13c`](#insn-008fb13c) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb144`](#insn-008fb144) → [`00633334`](../00633/00633334.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00633334` · 推定シンボル `None` · 推定型 `None`
- [`008fb148`](#insn-008fb148) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb150`](#insn-008fb150) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb158`](#insn-008fb158) → [`008fb184`](#insn-008fb184) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb164`](#insn-008fb164) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`008fb168`](#insn-008fb168) → [`008fb184`](#insn-008fb184) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb180`](#insn-008fb180) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`008fb184`](#insn-008fb184) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb188`](#insn-008fb188) → [`008fb19c`](#insn-008fb19c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb194`](#insn-008fb194) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`008fb198`](#insn-008fb198) → [`008fb1b8`](#insn-008fb1b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb19c`](#insn-008fb19c) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb1a0`](#insn-008fb1a0) → [`008fb1d8`](#insn-008fb1d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb1a4`](#insn-008fb1a4) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb1a8`](#insn-008fb1a8) → [`008fb1e8`](#insn-008fb1e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb1ac`](#insn-008fb1ac) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb1b0`](#insn-008fb1b0) → [`008fb1f8`](#insn-008fb1f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb1b4`](#insn-008fb1b4) → [`008fb80c`](#insn-008fb80c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb1cc`](#insn-008fb1cc) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`008fb1d0`](#insn-008fb1d0) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb1d4`](#insn-008fb1d4) → [`008fb1a4`](#insn-008fb1a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb1d8`](#insn-008fb1d8) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb1dc`](#insn-008fb1dc) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008fb1e0`](#insn-008fb1e0) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb1e4`](#insn-008fb1e4) → [`008fb1ac`](#insn-008fb1ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb1e8`](#insn-008fb1e8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb1ec`](#insn-008fb1ec) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008fb1f0`](#insn-008fb1f0) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb1f4`](#insn-008fb1f4) → [`008fb80c`](#insn-008fb80c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb200`](#insn-008fb200) → `Stack[-0x85]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb204`](#insn-008fb204) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb210`](#insn-008fb210) → `0029f173`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb214`](#insn-008fb214) → `Stack[-0x87]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb21c`](#insn-008fb21c) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb220`](#insn-008fb220) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb22c`](#insn-008fb22c) → `002c1333`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb230`](#insn-008fb230) → `002c1338`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb234`](#insn-008fb234) → `Stack[-0x9a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb238`](#insn-008fb238) → `Stack[-0xa7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb23c`](#insn-008fb23c) → `Stack[-0xa2]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb24c`](#insn-008fb24c) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb254`](#insn-008fb254) → [`00633334`](../00633/00633334.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00633334` · 推定シンボル `None` · 推定型 `None`
- [`008fb258`](#insn-008fb258) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb260`](#insn-008fb260) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb268`](#insn-008fb268) → [`008fb294`](#insn-008fb294) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb274`](#insn-008fb274) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`008fb278`](#insn-008fb278) → [`008fb294`](#insn-008fb294) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb290`](#insn-008fb290) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`008fb294`](#insn-008fb294) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb298`](#insn-008fb298) → [`008fb2ac`](#insn-008fb2ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb2a4`](#insn-008fb2a4) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`008fb2a8`](#insn-008fb2a8) → [`008fb2c8`](#insn-008fb2c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb2ac`](#insn-008fb2ac) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb2b0`](#insn-008fb2b0) → [`008fb2e8`](#insn-008fb2e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb2b4`](#insn-008fb2b4) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb2b8`](#insn-008fb2b8) → [`008fb2f8`](#insn-008fb2f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb2bc`](#insn-008fb2bc) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb2c0`](#insn-008fb2c0) → [`008fb308`](#insn-008fb308) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb2c4`](#insn-008fb2c4) → [`008fb860`](#insn-008fb860) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb2dc`](#insn-008fb2dc) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`008fb2e0`](#insn-008fb2e0) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb2e4`](#insn-008fb2e4) → [`008fb2b4`](#insn-008fb2b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb2e8`](#insn-008fb2e8) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb2ec`](#insn-008fb2ec) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008fb2f0`](#insn-008fb2f0) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb2f4`](#insn-008fb2f4) → [`008fb2bc`](#insn-008fb2bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb2f8`](#insn-008fb2f8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb2fc`](#insn-008fb2fc) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008fb300`](#insn-008fb300) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb304`](#insn-008fb304) → [`008fb860`](#insn-008fb860) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb310`](#insn-008fb310) → `Stack[-0x85]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb314`](#insn-008fb314) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb320`](#insn-008fb320) → `002b3e69`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb324`](#insn-008fb324) → `Stack[-0x87]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb32c`](#insn-008fb32c) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb330`](#insn-008fb330) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb33c`](#insn-008fb33c) → `002b9230`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb340`](#insn-008fb340) → `002b9235`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb344`](#insn-008fb344) → `Stack[-0x9a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb348`](#insn-008fb348) → `Stack[-0xa7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb34c`](#insn-008fb34c) → `Stack[-0xa2]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb35c`](#insn-008fb35c) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb364`](#insn-008fb364) → [`00633334`](../00633/00633334.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00633334` · 推定シンボル `None` · 推定型 `None`
- [`008fb368`](#insn-008fb368) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb370`](#insn-008fb370) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb378`](#insn-008fb378) → [`008fb3a4`](#insn-008fb3a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb384`](#insn-008fb384) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`008fb388`](#insn-008fb388) → [`008fb3a4`](#insn-008fb3a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb3a0`](#insn-008fb3a0) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`008fb3a4`](#insn-008fb3a4) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb3a8`](#insn-008fb3a8) → [`008fb3bc`](#insn-008fb3bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb3b4`](#insn-008fb3b4) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`008fb3b8`](#insn-008fb3b8) → [`008fb534`](#insn-008fb534) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb3bc`](#insn-008fb3bc) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb3c0`](#insn-008fb3c0) → [`008fb3cc`](#insn-008fb3cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb3c4`](#insn-008fb3c4) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb3c8`](#insn-008fb3c8) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008fb3cc`](#insn-008fb3cc) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb3d0`](#insn-008fb3d0) → [`008fb3dc`](#insn-008fb3dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb3d4`](#insn-008fb3d4) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb3d8`](#insn-008fb3d8) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008fb3e4`](#insn-008fb3e4) → [`00862c10`](../00862/00862c10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00862c10` · 推定シンボル `None` · 推定型 `None`
- [`008fb3e8`](#insn-008fb3e8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb3f0`](#insn-008fb3f0) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb3f8`](#insn-008fb3f8) → [`008fb424`](#insn-008fb424) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb404`](#insn-008fb404) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`008fb408`](#insn-008fb408) → [`008fb424`](#insn-008fb424) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb420`](#insn-008fb420) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`008fb424`](#insn-008fb424) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb428`](#insn-008fb428) → [`008fb454`](#insn-008fb454) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb434`](#insn-008fb434) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`008fb438`](#insn-008fb438) → [`008fb454`](#insn-008fb454) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb450`](#insn-008fb450) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`008fb454`](#insn-008fb454) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb458`](#insn-008fb458) → [`008fb8b4`](#insn-008fb8b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb464`](#insn-008fb464) → `Stack[-0x85]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb468`](#insn-008fb468) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb474`](#insn-008fb474) → `002a448a`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb478`](#insn-008fb478) → `Stack[-0x87]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb480`](#insn-008fb480) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb484`](#insn-008fb484) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb490`](#insn-008fb490) → `002bdbdd`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb494`](#insn-008fb494) → `002bdbe2`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb498`](#insn-008fb498) → `Stack[-0x9a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb49c`](#insn-008fb49c) → `Stack[-0xa7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb4a0`](#insn-008fb4a0) → `Stack[-0xa2]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb4b8`](#insn-008fb4b8) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb4c0`](#insn-008fb4c0) → [`00633334`](../00633/00633334.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00633334` · 推定シンボル `None` · 推定型 `None`
- [`008fb4c4`](#insn-008fb4c4) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb4cc`](#insn-008fb4cc) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb4d4`](#insn-008fb4d4) → [`008fb500`](#insn-008fb500) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb4e0`](#insn-008fb4e0) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`008fb4e4`](#insn-008fb4e4) → [`008fb500`](#insn-008fb500) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb4fc`](#insn-008fb4fc) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`008fb500`](#insn-008fb500) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb504`](#insn-008fb504) → [`008fb518`](#insn-008fb518) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb510`](#insn-008fb510) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`008fb514`](#insn-008fb514) → [`008fb558`](#insn-008fb558) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb518`](#insn-008fb518) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb51c`](#insn-008fb51c) → [`008fb578`](#insn-008fb578) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb520`](#insn-008fb520) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb524`](#insn-008fb524) → [`008fb588`](#insn-008fb588) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb528`](#insn-008fb528) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb52c`](#insn-008fb52c) → [`008fb598`](#insn-008fb598) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb530`](#insn-008fb530) → [`008fb908`](#insn-008fb908) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb548`](#insn-008fb548) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`008fb54c`](#insn-008fb54c) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb550`](#insn-008fb550) → [`008fb3c4`](#insn-008fb3c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb554`](#insn-008fb554) → [`008fb3cc`](#insn-008fb3cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb56c`](#insn-008fb56c) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`008fb570`](#insn-008fb570) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb574`](#insn-008fb574) → [`008fb520`](#insn-008fb520) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb578`](#insn-008fb578) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb57c`](#insn-008fb57c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008fb580`](#insn-008fb580) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb584`](#insn-008fb584) → [`008fb528`](#insn-008fb528) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb588`](#insn-008fb588) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb58c`](#insn-008fb58c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008fb590`](#insn-008fb590) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb594`](#insn-008fb594) → [`008fb908`](#insn-008fb908) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb5a4`](#insn-008fb5a4) → `002a33f1`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb5a8`](#insn-008fb5a8) → `002a33f6`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb5ac`](#insn-008fb5ac) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb5b4`](#insn-008fb5b4) → `Stack[-0x82]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb5b8`](#insn-008fb5b8) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb5bc`](#insn-008fb5bc) → `Stack[-0x8a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb5c8`](#insn-008fb5c8) → `002c02cb`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`008fb5cc`](#insn-008fb5cc) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb5d0`](#insn-008fb5d0) → `Stack[-0x97]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb5d4`](#insn-008fb5d4) → `Stack[-0xa7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb5dc`](#insn-008fb5dc) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb5f0`](#insn-008fb5f0) → [`00633334`](../00633/00633334.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00633334` · 推定シンボル `None` · 推定型 `None`
- [`008fb5f4`](#insn-008fb5f4) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb5fc`](#insn-008fb5fc) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb604`](#insn-008fb604) → [`008fb630`](#insn-008fb630) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb610`](#insn-008fb610) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`008fb614`](#insn-008fb614) → [`008fb630`](#insn-008fb630) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb62c`](#insn-008fb62c) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`008fb630`](#insn-008fb630) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb634`](#insn-008fb634) → [`008fb648`](#insn-008fb648) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb640`](#insn-008fb640) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`008fb644`](#insn-008fb644) → [`008fb694`](#insn-008fb694) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb648`](#insn-008fb648) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb64c`](#insn-008fb64c) → [`008fb658`](#insn-008fb658) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb650`](#insn-008fb650) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb654`](#insn-008fb654) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008fb658`](#insn-008fb658) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb65c`](#insn-008fb65c) → [`008fb668`](#insn-008fb668) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb660`](#insn-008fb660) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb664`](#insn-008fb664) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008fb66c`](#insn-008fb66c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb674`](#insn-008fb674) → [`008fb9cc`](#insn-008fb9cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb678`](#insn-008fb678) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb67c`](#insn-008fb67c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb680`](#insn-008fb680) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb684`](#insn-008fb684) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb688`](#insn-008fb688) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb6a8`](#insn-008fb6a8) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`008fb6ac`](#insn-008fb6ac) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb6b0`](#insn-008fb6b0) → [`008fb650`](#insn-008fb650) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb6b4`](#insn-008fb6b4) → [`008fb658`](#insn-008fb658) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb6bc`](#insn-008fb6bc) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb6c0`](#insn-008fb6c0) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`008fb6c4`](#insn-008fb6c4) → [`008fad44`](#insn-008fad44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb6cc`](#insn-008fb6cc) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb6d4`](#insn-008fb6d4) → [`0047ed74`](../0047e/0047ed74.md) · `PARAM` · `ANALYSIS` · 関数 `0047ed74` · 推定シンボル `None` · 推定型 `None`
- [`008fb6e0`](#insn-008fb6e0) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008fb6e4`](#insn-008fb6e4) → `00ca4b08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb6e8`](#insn-008fb6e8) → `00ca4b00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb6e8`](#insn-008fb6e8) → `00ca4b08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb6f0`](#insn-008fb6f0) → `00ca4b28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb6f0`](#insn-008fb6f0) → `00ca4b30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb6f4`](#insn-008fb6f4) → `00ca4b20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb6f8`](#insn-008fb6f8) → `00ca4b10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb6f8`](#insn-008fb6f8) → `00ca4b18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb6f8`](#insn-008fb6f8) → `00ca4b20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb6fc`](#insn-008fb6fc) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`008fb704`](#insn-008fb704) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb708`](#insn-008fb708) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`008fb70c`](#insn-008fb70c) → [`008fad44`](#insn-008fad44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb714`](#insn-008fb714) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb718`](#insn-008fb718) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`008fb71c`](#insn-008fb71c) → [`008faea0`](#insn-008faea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb728`](#insn-008fb728) → [`0047ed74`](../0047e/0047ed74.md) · `PARAM` · `ANALYSIS` · 関数 `0047ed74` · 推定シンボル `None` · 推定型 `None`
- [`008fb72c`](#insn-008fb72c) → `00ca4b08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb734`](#insn-008fb734) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008fb738`](#insn-008fb738) → `00ca4b00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb738`](#insn-008fb738) → `00ca4b08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb740`](#insn-008fb740) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb744`](#insn-008fb744) → `00ca4b28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb744`](#insn-008fb744) → `00ca4b30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb748`](#insn-008fb748) → `00ca4b20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb74c`](#insn-008fb74c) → `00ca4b10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb74c`](#insn-008fb74c) → `00ca4b18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb74c`](#insn-008fb74c) → `00ca4b20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb750`](#insn-008fb750) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`008fb758`](#insn-008fb758) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb75c`](#insn-008fb75c) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`008fb760`](#insn-008fb760) → [`008faea0`](#insn-008faea0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb768`](#insn-008fb768) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb76c`](#insn-008fb76c) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`008fb770`](#insn-008fb770) → [`008fafd4`](#insn-008fafd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb77c`](#insn-008fb77c) → [`0047ed74`](../0047e/0047ed74.md) · `PARAM` · `ANALYSIS` · 関数 `0047ed74` · 推定シンボル `None` · 推定型 `None`
- [`008fb780`](#insn-008fb780) → `00ca4b08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb788`](#insn-008fb788) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008fb78c`](#insn-008fb78c) → `00ca4b00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb78c`](#insn-008fb78c) → `00ca4b08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb794`](#insn-008fb794) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb798`](#insn-008fb798) → `00ca4b28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb798`](#insn-008fb798) → `00ca4b30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb79c`](#insn-008fb79c) → `00ca4b20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb7a0`](#insn-008fb7a0) → `00ca4b10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb7a0`](#insn-008fb7a0) → `00ca4b18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb7a0`](#insn-008fb7a0) → `00ca4b20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb7a4`](#insn-008fb7a4) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`008fb7ac`](#insn-008fb7ac) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb7b0`](#insn-008fb7b0) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`008fb7b4`](#insn-008fb7b4) → [`008fafd4`](#insn-008fafd4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb7bc`](#insn-008fb7bc) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb7c0`](#insn-008fb7c0) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`008fb7c4`](#insn-008fb7c4) → [`008fb0e8`](#insn-008fb0e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb7d0`](#insn-008fb7d0) → [`0047ed74`](../0047e/0047ed74.md) · `PARAM` · `ANALYSIS` · 関数 `0047ed74` · 推定シンボル `None` · 推定型 `None`
- [`008fb7d4`](#insn-008fb7d4) → `00ca4b08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb7dc`](#insn-008fb7dc) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008fb7e0`](#insn-008fb7e0) → `00ca4b00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb7e0`](#insn-008fb7e0) → `00ca4b08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb7e8`](#insn-008fb7e8) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb7ec`](#insn-008fb7ec) → `00ca4b28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb7ec`](#insn-008fb7ec) → `00ca4b30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb7f0`](#insn-008fb7f0) → `00ca4b20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb7f4`](#insn-008fb7f4) → `00ca4b10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb7f4`](#insn-008fb7f4) → `00ca4b18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb7f4`](#insn-008fb7f4) → `00ca4b20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb7f8`](#insn-008fb7f8) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`008fb800`](#insn-008fb800) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb804`](#insn-008fb804) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`008fb808`](#insn-008fb808) → [`008fb0e8`](#insn-008fb0e8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb810`](#insn-008fb810) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb814`](#insn-008fb814) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`008fb818`](#insn-008fb818) → [`008fb1f8`](#insn-008fb1f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb824`](#insn-008fb824) → [`0047ed74`](../0047e/0047ed74.md) · `PARAM` · `ANALYSIS` · 関数 `0047ed74` · 推定シンボル `None` · 推定型 `None`
- [`008fb828`](#insn-008fb828) → `00ca4b08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb830`](#insn-008fb830) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008fb834`](#insn-008fb834) → `00ca4b00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb834`](#insn-008fb834) → `00ca4b08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb83c`](#insn-008fb83c) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb840`](#insn-008fb840) → `00ca4b28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb840`](#insn-008fb840) → `00ca4b30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb844`](#insn-008fb844) → `00ca4b20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb848`](#insn-008fb848) → `00ca4b10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb848`](#insn-008fb848) → `00ca4b18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb848`](#insn-008fb848) → `00ca4b20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb84c`](#insn-008fb84c) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`008fb854`](#insn-008fb854) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb858`](#insn-008fb858) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`008fb85c`](#insn-008fb85c) → [`008fb1f8`](#insn-008fb1f8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb864`](#insn-008fb864) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb868`](#insn-008fb868) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`008fb86c`](#insn-008fb86c) → [`008fb308`](#insn-008fb308) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb878`](#insn-008fb878) → [`0047ed74`](../0047e/0047ed74.md) · `PARAM` · `ANALYSIS` · 関数 `0047ed74` · 推定シンボル `None` · 推定型 `None`
- [`008fb87c`](#insn-008fb87c) → `00ca4b08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb884`](#insn-008fb884) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008fb888`](#insn-008fb888) → `00ca4b00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb888`](#insn-008fb888) → `00ca4b08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb890`](#insn-008fb890) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb894`](#insn-008fb894) → `00ca4b28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb894`](#insn-008fb894) → `00ca4b30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb898`](#insn-008fb898) → `00ca4b20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb89c`](#insn-008fb89c) → `00ca4b10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb89c`](#insn-008fb89c) → `00ca4b18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb89c`](#insn-008fb89c) → `00ca4b20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb8a0`](#insn-008fb8a0) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`008fb8a8`](#insn-008fb8a8) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb8ac`](#insn-008fb8ac) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`008fb8b0`](#insn-008fb8b0) → [`008fb308`](#insn-008fb308) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb8b8`](#insn-008fb8b8) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb8bc`](#insn-008fb8bc) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`008fb8c0`](#insn-008fb8c0) → [`008fb45c`](#insn-008fb45c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb8cc`](#insn-008fb8cc) → [`0047ed74`](../0047e/0047ed74.md) · `PARAM` · `ANALYSIS` · 関数 `0047ed74` · 推定シンボル `None` · 推定型 `None`
- [`008fb8d0`](#insn-008fb8d0) → `00ca4b08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb8d8`](#insn-008fb8d8) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008fb8dc`](#insn-008fb8dc) → `00ca4b00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb8dc`](#insn-008fb8dc) → `00ca4b08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb8e4`](#insn-008fb8e4) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb8e8`](#insn-008fb8e8) → `00ca4b28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb8e8`](#insn-008fb8e8) → `00ca4b30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb8ec`](#insn-008fb8ec) → `00ca4b20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb8f0`](#insn-008fb8f0) → `00ca4b10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb8f0`](#insn-008fb8f0) → `00ca4b18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb8f0`](#insn-008fb8f0) → `00ca4b20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb8f4`](#insn-008fb8f4) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`008fb8fc`](#insn-008fb8fc) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb900`](#insn-008fb900) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`008fb904`](#insn-008fb904) → [`008fb45c`](#insn-008fb45c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb90c`](#insn-008fb90c) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb910`](#insn-008fb910) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`008fb914`](#insn-008fb914) → [`008fb598`](#insn-008fb598) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb920`](#insn-008fb920) → [`0047ed74`](../0047e/0047ed74.md) · `PARAM` · `ANALYSIS` · 関数 `0047ed74` · 推定シンボル `None` · 推定型 `None`
- [`008fb924`](#insn-008fb924) → `00ca4b08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb92c`](#insn-008fb92c) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008fb930`](#insn-008fb930) → `00ca4b00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb930`](#insn-008fb930) → `00ca4b08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb938`](#insn-008fb938) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb93c`](#insn-008fb93c) → `00ca4b28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb93c`](#insn-008fb93c) → `00ca4b30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb940`](#insn-008fb940) → `00ca4b20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb944`](#insn-008fb944) → `00ca4b10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb944`](#insn-008fb944) → `00ca4b18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb944`](#insn-008fb944) → `00ca4b20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008fb948`](#insn-008fb948) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`008fb950`](#insn-008fb950) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008fb954`](#insn-008fb954) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`008fb958`](#insn-008fb958) → [`008fb598`](#insn-008fb598) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008fb9cc`](#insn-008fb9cc) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008facf0`](#insn-008facf0)

~~~json
{
  "source": "008facf0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008facf4`](#insn-008facf4)

~~~json
{
  "source": "008facf4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008facf8`](#insn-008facf8)

~~~json
{
  "source": "008facf8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008facfc`](#insn-008facfc)

~~~json
{
  "source": "008facfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fad00`](#insn-008fad00)

~~~json
{
  "source": "008fad00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fad18`](#insn-008fad18)

~~~json
{
  "source": "008fad18",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fad1c`](#insn-008fad1c)

~~~json
{
  "source": "008fad1c",
  "target": "00758190",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fad30`](#insn-008fad30)

~~~json
{
  "source": "008fad30",
  "target": "00c856f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c856f8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008fad3c`](#insn-008fad3c)

~~~json
{
  "source": "008fad3c",
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
- 参照命令 [`008fad40`](#insn-008fad40)

~~~json
{
  "source": "008fad40",
  "target": "008fb6b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fad4c`](#insn-008fad4c)

~~~json
{
  "source": "008fad4c",
  "target": "Stack[-0x85]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fad50`](#insn-008fad50)

~~~json
{
  "source": "008fad50",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fad5c`](#insn-008fad5c)

~~~json
{
  "source": "008fad5c",
  "target": "002b634e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b634e",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "696d673030362e706e6700",
  "capture_start": "002b634e",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fad60`](#insn-008fad60)

~~~json
{
  "source": "008fad60",
  "target": "Stack[-0x87]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fad68`](#insn-008fad68)

~~~json
{
  "source": "008fad68",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fad6c`](#insn-008fad6c)

~~~json
{
  "source": "008fad6c",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fad78`](#insn-008fad78)

~~~json
{
  "source": "008fad78",
  "target": "002b1ed6",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fad7c`](#insn-008fad7c)

~~~json
{
  "source": "008fad7c",
  "target": "002b1edb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b1edb",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "362e696d6763757400",
  "capture_start": "002b1edb",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fad80`](#insn-008fad80)

~~~json
{
  "source": "008fad80",
  "target": "Stack[-0x9a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fad84`](#insn-008fad84)

~~~json
{
  "source": "008fad84",
  "target": "Stack[-0xa7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fad88`](#insn-008fad88)

~~~json
{
  "source": "008fad88",
  "target": "Stack[-0xa2]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fada0`](#insn-008fada0)

~~~json
{
  "source": "008fada0",
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
- 参照命令 [`008fada8`](#insn-008fada8)

~~~json
{
  "source": "008fada8",
  "target": "00633334",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fadac`](#insn-008fadac)

~~~json
{
  "source": "008fadac",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fadb4`](#insn-008fadb4)

~~~json
{
  "source": "008fadb4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fadbc`](#insn-008fadbc)

~~~json
{
  "source": "008fadbc",
  "target": "008fade8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fadc8`](#insn-008fadc8)

~~~json
{
  "source": "008fadc8",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fadcc`](#insn-008fadcc)

~~~json
{
  "source": "008fadcc",
  "target": "008fade8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fade4`](#insn-008fade4)

~~~json
{
  "source": "008fade4",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fade8`](#insn-008fade8)

~~~json
{
  "source": "008fade8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fadec`](#insn-008fadec)

~~~json
{
  "source": "008fadec",
  "target": "008fae00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fadf8`](#insn-008fadf8)

~~~json
{
  "source": "008fadf8",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fadfc`](#insn-008fadfc)

~~~json
{
  "source": "008fadfc",
  "target": "008faf70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fae00`](#insn-008fae00)

~~~json
{
  "source": "008fae00",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fae04`](#insn-008fae04)

~~~json
{
  "source": "008fae04",
  "target": "008fae10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fae08`](#insn-008fae08)

~~~json
{
  "source": "008fae08",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fae0c`](#insn-008fae0c)

~~~json
{
  "source": "008fae0c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fae10`](#insn-008fae10)

~~~json
{
  "source": "008fae10",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fae14`](#insn-008fae14)

~~~json
{
  "source": "008fae14",
  "target": "008fae20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fae18`](#insn-008fae18)

~~~json
{
  "source": "008fae18",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fae1c`](#insn-008fae1c)

~~~json
{
  "source": "008fae1c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fae28`](#insn-008fae28)

~~~json
{
  "source": "008fae28",
  "target": "008644f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fae2c`](#insn-008fae2c)

~~~json
{
  "source": "008fae2c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fae34`](#insn-008fae34)

~~~json
{
  "source": "008fae34",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fae3c`](#insn-008fae3c)

~~~json
{
  "source": "008fae3c",
  "target": "008fae68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fae48`](#insn-008fae48)

~~~json
{
  "source": "008fae48",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fae4c`](#insn-008fae4c)

~~~json
{
  "source": "008fae4c",
  "target": "008fae68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fae64`](#insn-008fae64)

~~~json
{
  "source": "008fae64",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fae68`](#insn-008fae68)

~~~json
{
  "source": "008fae68",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fae6c`](#insn-008fae6c)

~~~json
{
  "source": "008fae6c",
  "target": "008fae98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fae78`](#insn-008fae78)

~~~json
{
  "source": "008fae78",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fae7c`](#insn-008fae7c)

~~~json
{
  "source": "008fae7c",
  "target": "008fae98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fae94`](#insn-008fae94)

~~~json
{
  "source": "008fae94",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fae98`](#insn-008fae98)

~~~json
{
  "source": "008fae98",
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
- 参照命令 [`008fae9c`](#insn-008fae9c)

~~~json
{
  "source": "008fae9c",
  "target": "008fb710",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faea8`](#insn-008faea8)

~~~json
{
  "source": "008faea8",
  "target": "Stack[-0x85]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faeac`](#insn-008faeac)

~~~json
{
  "source": "008faeac",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faeb8`](#insn-008faeb8)

~~~json
{
  "source": "008faeb8",
  "target": "002bef7e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bef7e",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "696d673032342e706e6700",
  "capture_start": "002bef7e",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008faebc`](#insn-008faebc)

~~~json
{
  "source": "008faebc",
  "target": "Stack[-0x87]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faec4`](#insn-008faec4)

~~~json
{
  "source": "008faec4",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faec8`](#insn-008faec8)

~~~json
{
  "source": "008faec8",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faed4`](#insn-008faed4)

~~~json
{
  "source": "008faed4",
  "target": "002a9ed6",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faed8`](#insn-008faed8)

~~~json
{
  "source": "008faed8",
  "target": "002a9edb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a9edb",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "342e696d6763757400",
  "capture_start": "002a9edb",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008faedc`](#insn-008faedc)

~~~json
{
  "source": "008faedc",
  "target": "Stack[-0x9a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faee0`](#insn-008faee0)

~~~json
{
  "source": "008faee0",
  "target": "Stack[-0xa7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faee4`](#insn-008faee4)

~~~json
{
  "source": "008faee4",
  "target": "Stack[-0xa2]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faef4`](#insn-008faef4)

~~~json
{
  "source": "008faef4",
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
- 参照命令 [`008faefc`](#insn-008faefc)

~~~json
{
  "source": "008faefc",
  "target": "00633334",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008faf00`](#insn-008faf00)

~~~json
{
  "source": "008faf00",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf08`](#insn-008faf08)

~~~json
{
  "source": "008faf08",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf10`](#insn-008faf10)

~~~json
{
  "source": "008faf10",
  "target": "008faf3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf1c`](#insn-008faf1c)

~~~json
{
  "source": "008faf1c",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008faf20`](#insn-008faf20)

~~~json
{
  "source": "008faf20",
  "target": "008faf3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf38`](#insn-008faf38)

~~~json
{
  "source": "008faf38",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008faf3c`](#insn-008faf3c)

~~~json
{
  "source": "008faf3c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf40`](#insn-008faf40)

~~~json
{
  "source": "008faf40",
  "target": "008faf54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf4c`](#insn-008faf4c)

~~~json
{
  "source": "008faf4c",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008faf50`](#insn-008faf50)

~~~json
{
  "source": "008faf50",
  "target": "008faf94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf54`](#insn-008faf54)

~~~json
{
  "source": "008faf54",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf58`](#insn-008faf58)

~~~json
{
  "source": "008faf58",
  "target": "008fafb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf5c`](#insn-008faf5c)

~~~json
{
  "source": "008faf5c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf60`](#insn-008faf60)

~~~json
{
  "source": "008faf60",
  "target": "008fafc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf64`](#insn-008faf64)

~~~json
{
  "source": "008faf64",
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
- 参照命令 [`008faf68`](#insn-008faf68)

~~~json
{
  "source": "008faf68",
  "target": "008fafd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf6c`](#insn-008faf6c)

~~~json
{
  "source": "008faf6c",
  "target": "008fb764",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf84`](#insn-008faf84)

~~~json
{
  "source": "008faf84",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008faf88`](#insn-008faf88)

~~~json
{
  "source": "008faf88",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf8c`](#insn-008faf8c)

~~~json
{
  "source": "008faf8c",
  "target": "008fae08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faf90`](#insn-008faf90)

~~~json
{
  "source": "008faf90",
  "target": "008fae10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fafa8`](#insn-008fafa8)

~~~json
{
  "source": "008fafa8",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fafac`](#insn-008fafac)

~~~json
{
  "source": "008fafac",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fafb0`](#insn-008fafb0)

~~~json
{
  "source": "008fafb0",
  "target": "008faf5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fafb4`](#insn-008fafb4)

~~~json
{
  "source": "008fafb4",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fafb8`](#insn-008fafb8)

~~~json
{
  "source": "008fafb8",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fafbc`](#insn-008fafbc)

~~~json
{
  "source": "008fafbc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fafc0`](#insn-008fafc0)

~~~json
{
  "source": "008fafc0",
  "target": "008faf64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fafc4`](#insn-008fafc4)

~~~json
{
  "source": "008fafc4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fafc8`](#insn-008fafc8)

~~~json
{
  "source": "008fafc8",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fafcc`](#insn-008fafcc)

~~~json
{
  "source": "008fafcc",
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
- 参照命令 [`008fafd0`](#insn-008fafd0)

~~~json
{
  "source": "008fafd0",
  "target": "008fb764",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fafdc`](#insn-008fafdc)

~~~json
{
  "source": "008fafdc",
  "target": "Stack[-0x85]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fafe0`](#insn-008fafe0)

~~~json
{
  "source": "008fafe0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fafec`](#insn-008fafec)

~~~json
{
  "source": "008fafec",
  "target": "002bfff6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bfff6",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "696d673031362e706e6700",
  "capture_start": "002bfff6",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008faff0`](#insn-008faff0)

~~~json
{
  "source": "008faff0",
  "target": "Stack[-0x87]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faff8`](#insn-008faff8)

~~~json
{
  "source": "008faff8",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008faffc`](#insn-008faffc)

~~~json
{
  "source": "008faffc",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb008`](#insn-008fb008)

~~~json
{
  "source": "008fb008",
  "target": "002a9e29",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb00c`](#insn-008fb00c)

~~~json
{
  "source": "008fb00c",
  "target": "002a9e2e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a9e2e",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "362e696d6763757400",
  "capture_start": "002a9e2e",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb010`](#insn-008fb010)

~~~json
{
  "source": "008fb010",
  "target": "Stack[-0x9a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb014`](#insn-008fb014)

~~~json
{
  "source": "008fb014",
  "target": "Stack[-0xa7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb018`](#insn-008fb018)

~~~json
{
  "source": "008fb018",
  "target": "Stack[-0xa2]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb028`](#insn-008fb028)

~~~json
{
  "source": "008fb028",
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
- 参照命令 [`008fb030`](#insn-008fb030)

~~~json
{
  "source": "008fb030",
  "target": "00633334",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb034`](#insn-008fb034)

~~~json
{
  "source": "008fb034",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb040`](#insn-008fb040)

~~~json
{
  "source": "008fb040",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb048`](#insn-008fb048)

~~~json
{
  "source": "008fb048",
  "target": "008fb074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb054`](#insn-008fb054)

~~~json
{
  "source": "008fb054",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb058`](#insn-008fb058)

~~~json
{
  "source": "008fb058",
  "target": "008fb074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb070`](#insn-008fb070)

~~~json
{
  "source": "008fb070",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb074`](#insn-008fb074)

~~~json
{
  "source": "008fb074",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb078`](#insn-008fb078)

~~~json
{
  "source": "008fb078",
  "target": "008fb08c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb084`](#insn-008fb084)

~~~json
{
  "source": "008fb084",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb088`](#insn-008fb088)

~~~json
{
  "source": "008fb088",
  "target": "008fb0a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb08c`](#insn-008fb08c)

~~~json
{
  "source": "008fb08c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb090`](#insn-008fb090)

~~~json
{
  "source": "008fb090",
  "target": "008fb0c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb094`](#insn-008fb094)

~~~json
{
  "source": "008fb094",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb098`](#insn-008fb098)

~~~json
{
  "source": "008fb098",
  "target": "008fb0d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb09c`](#insn-008fb09c)

~~~json
{
  "source": "008fb09c",
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
- 参照命令 [`008fb0a0`](#insn-008fb0a0)

~~~json
{
  "source": "008fb0a0",
  "target": "008fb0e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb0a4`](#insn-008fb0a4)

~~~json
{
  "source": "008fb0a4",
  "target": "008fb7b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb0bc`](#insn-008fb0bc)

~~~json
{
  "source": "008fb0bc",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb0c0`](#insn-008fb0c0)

~~~json
{
  "source": "008fb0c0",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb0c4`](#insn-008fb0c4)

~~~json
{
  "source": "008fb0c4",
  "target": "008fb094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb0c8`](#insn-008fb0c8)

~~~json
{
  "source": "008fb0c8",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb0cc`](#insn-008fb0cc)

~~~json
{
  "source": "008fb0cc",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb0d0`](#insn-008fb0d0)

~~~json
{
  "source": "008fb0d0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb0d4`](#insn-008fb0d4)

~~~json
{
  "source": "008fb0d4",
  "target": "008fb09c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb0d8`](#insn-008fb0d8)

~~~json
{
  "source": "008fb0d8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb0dc`](#insn-008fb0dc)

~~~json
{
  "source": "008fb0dc",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb0e0`](#insn-008fb0e0)

~~~json
{
  "source": "008fb0e0",
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
- 参照命令 [`008fb0e4`](#insn-008fb0e4)

~~~json
{
  "source": "008fb0e4",
  "target": "008fb7b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb0f0`](#insn-008fb0f0)

~~~json
{
  "source": "008fb0f0",
  "target": "Stack[-0x85]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb0f4`](#insn-008fb0f4)

~~~json
{
  "source": "008fb0f4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb100`](#insn-008fb100)

~~~json
{
  "source": "008fb100",
  "target": "002b91cf",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b91cf",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "696d673031352e706e6700",
  "capture_start": "002b91cf",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb104`](#insn-008fb104)

~~~json
{
  "source": "008fb104",
  "target": "Stack[-0x87]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb10c`](#insn-008fb10c)

~~~json
{
  "source": "008fb10c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb110`](#insn-008fb110)

~~~json
{
  "source": "008fb110",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb11c`](#insn-008fb11c)

~~~json
{
  "source": "008fb11c",
  "target": "002bdbcf",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb120`](#insn-008fb120)

~~~json
{
  "source": "008fb120",
  "target": "002bdbd4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bdbd4",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "352e696d6763757400",
  "capture_start": "002bdbd4",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb124`](#insn-008fb124)

~~~json
{
  "source": "008fb124",
  "target": "Stack[-0x9a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb128`](#insn-008fb128)

~~~json
{
  "source": "008fb128",
  "target": "Stack[-0xa7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb12c`](#insn-008fb12c)

~~~json
{
  "source": "008fb12c",
  "target": "Stack[-0xa2]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb13c`](#insn-008fb13c)

~~~json
{
  "source": "008fb13c",
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
- 参照命令 [`008fb144`](#insn-008fb144)

~~~json
{
  "source": "008fb144",
  "target": "00633334",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb148`](#insn-008fb148)

~~~json
{
  "source": "008fb148",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb150`](#insn-008fb150)

~~~json
{
  "source": "008fb150",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb158`](#insn-008fb158)

~~~json
{
  "source": "008fb158",
  "target": "008fb184",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb164`](#insn-008fb164)

~~~json
{
  "source": "008fb164",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb168`](#insn-008fb168)

~~~json
{
  "source": "008fb168",
  "target": "008fb184",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb180`](#insn-008fb180)

~~~json
{
  "source": "008fb180",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb184`](#insn-008fb184)

~~~json
{
  "source": "008fb184",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb188`](#insn-008fb188)

~~~json
{
  "source": "008fb188",
  "target": "008fb19c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb194`](#insn-008fb194)

~~~json
{
  "source": "008fb194",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb198`](#insn-008fb198)

~~~json
{
  "source": "008fb198",
  "target": "008fb1b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
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
  "target": "008fb1d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb1a4`](#insn-008fb1a4)

~~~json
{
  "source": "008fb1a4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb1a8`](#insn-008fb1a8)

~~~json
{
  "source": "008fb1a8",
  "target": "008fb1e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb1ac`](#insn-008fb1ac)

~~~json
{
  "source": "008fb1ac",
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
- 参照命令 [`008fb1b0`](#insn-008fb1b0)

~~~json
{
  "source": "008fb1b0",
  "target": "008fb1f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb1b4`](#insn-008fb1b4)

~~~json
{
  "source": "008fb1b4",
  "target": "008fb80c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb1cc`](#insn-008fb1cc)

~~~json
{
  "source": "008fb1cc",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb1d0`](#insn-008fb1d0)

~~~json
{
  "source": "008fb1d0",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb1d4`](#insn-008fb1d4)

~~~json
{
  "source": "008fb1d4",
  "target": "008fb1a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb1d8`](#insn-008fb1d8)

~~~json
{
  "source": "008fb1d8",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb1dc`](#insn-008fb1dc)

~~~json
{
  "source": "008fb1dc",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb1e0`](#insn-008fb1e0)

~~~json
{
  "source": "008fb1e0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb1e4`](#insn-008fb1e4)

~~~json
{
  "source": "008fb1e4",
  "target": "008fb1ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb1e8`](#insn-008fb1e8)

~~~json
{
  "source": "008fb1e8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb1ec`](#insn-008fb1ec)

~~~json
{
  "source": "008fb1ec",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb1f0`](#insn-008fb1f0)

~~~json
{
  "source": "008fb1f0",
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
- 参照命令 [`008fb1f4`](#insn-008fb1f4)

~~~json
{
  "source": "008fb1f4",
  "target": "008fb80c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb200`](#insn-008fb200)

~~~json
{
  "source": "008fb200",
  "target": "Stack[-0x85]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb204`](#insn-008fb204)

~~~json
{
  "source": "008fb204",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb210`](#insn-008fb210)

~~~json
{
  "source": "008fb210",
  "target": "0029f173",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029f173",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "696d673032312e706e6700",
  "capture_start": "0029f173",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb214`](#insn-008fb214)

~~~json
{
  "source": "008fb214",
  "target": "Stack[-0x87]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb21c`](#insn-008fb21c)

~~~json
{
  "source": "008fb21c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb220`](#insn-008fb220)

~~~json
{
  "source": "008fb220",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb22c`](#insn-008fb22c)

~~~json
{
  "source": "008fb22c",
  "target": "002c1333",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb230`](#insn-008fb230)

~~~json
{
  "source": "008fb230",
  "target": "002c1338",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c1338",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "312e696d6763757400",
  "capture_start": "002c1338",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb234`](#insn-008fb234)

~~~json
{
  "source": "008fb234",
  "target": "Stack[-0x9a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb238`](#insn-008fb238)

~~~json
{
  "source": "008fb238",
  "target": "Stack[-0xa7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb23c`](#insn-008fb23c)

~~~json
{
  "source": "008fb23c",
  "target": "Stack[-0xa2]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb24c`](#insn-008fb24c)

~~~json
{
  "source": "008fb24c",
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
- 参照命令 [`008fb254`](#insn-008fb254)

~~~json
{
  "source": "008fb254",
  "target": "00633334",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb258`](#insn-008fb258)

~~~json
{
  "source": "008fb258",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb260`](#insn-008fb260)

~~~json
{
  "source": "008fb260",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb268`](#insn-008fb268)

~~~json
{
  "source": "008fb268",
  "target": "008fb294",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb274`](#insn-008fb274)

~~~json
{
  "source": "008fb274",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb278`](#insn-008fb278)

~~~json
{
  "source": "008fb278",
  "target": "008fb294",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb290`](#insn-008fb290)

~~~json
{
  "source": "008fb290",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb294`](#insn-008fb294)

~~~json
{
  "source": "008fb294",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb298`](#insn-008fb298)

~~~json
{
  "source": "008fb298",
  "target": "008fb2ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb2a4`](#insn-008fb2a4)

~~~json
{
  "source": "008fb2a4",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb2a8`](#insn-008fb2a8)

~~~json
{
  "source": "008fb2a8",
  "target": "008fb2c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb2ac`](#insn-008fb2ac)

~~~json
{
  "source": "008fb2ac",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb2b0`](#insn-008fb2b0)

~~~json
{
  "source": "008fb2b0",
  "target": "008fb2e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb2b4`](#insn-008fb2b4)

~~~json
{
  "source": "008fb2b4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb2b8`](#insn-008fb2b8)

~~~json
{
  "source": "008fb2b8",
  "target": "008fb2f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb2bc`](#insn-008fb2bc)

~~~json
{
  "source": "008fb2bc",
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
- 参照命令 [`008fb2c0`](#insn-008fb2c0)

~~~json
{
  "source": "008fb2c0",
  "target": "008fb308",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb2c4`](#insn-008fb2c4)

~~~json
{
  "source": "008fb2c4",
  "target": "008fb860",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb2dc`](#insn-008fb2dc)

~~~json
{
  "source": "008fb2dc",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb2e0`](#insn-008fb2e0)

~~~json
{
  "source": "008fb2e0",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb2e4`](#insn-008fb2e4)

~~~json
{
  "source": "008fb2e4",
  "target": "008fb2b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb2e8`](#insn-008fb2e8)

~~~json
{
  "source": "008fb2e8",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb2ec`](#insn-008fb2ec)

~~~json
{
  "source": "008fb2ec",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb2f0`](#insn-008fb2f0)

~~~json
{
  "source": "008fb2f0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb2f4`](#insn-008fb2f4)

~~~json
{
  "source": "008fb2f4",
  "target": "008fb2bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb2f8`](#insn-008fb2f8)

~~~json
{
  "source": "008fb2f8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb2fc`](#insn-008fb2fc)

~~~json
{
  "source": "008fb2fc",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb300`](#insn-008fb300)

~~~json
{
  "source": "008fb300",
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
- 参照命令 [`008fb304`](#insn-008fb304)

~~~json
{
  "source": "008fb304",
  "target": "008fb860",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb310`](#insn-008fb310)

~~~json
{
  "source": "008fb310",
  "target": "Stack[-0x85]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb314`](#insn-008fb314)

~~~json
{
  "source": "008fb314",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb320`](#insn-008fb320)

~~~json
{
  "source": "008fb320",
  "target": "002b3e69",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b3e69",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "696d673032392e706e6700",
  "capture_start": "002b3e69",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb324`](#insn-008fb324)

~~~json
{
  "source": "008fb324",
  "target": "Stack[-0x87]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb32c`](#insn-008fb32c)

~~~json
{
  "source": "008fb32c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb330`](#insn-008fb330)

~~~json
{
  "source": "008fb330",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb33c`](#insn-008fb33c)

~~~json
{
  "source": "008fb33c",
  "target": "002b9230",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb340`](#insn-008fb340)

~~~json
{
  "source": "008fb340",
  "target": "002b9235",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b9235",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "392e696d6763757400",
  "capture_start": "002b9235",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb344`](#insn-008fb344)

~~~json
{
  "source": "008fb344",
  "target": "Stack[-0x9a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb348`](#insn-008fb348)

~~~json
{
  "source": "008fb348",
  "target": "Stack[-0xa7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb34c`](#insn-008fb34c)

~~~json
{
  "source": "008fb34c",
  "target": "Stack[-0xa2]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb35c`](#insn-008fb35c)

~~~json
{
  "source": "008fb35c",
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
- 参照命令 [`008fb364`](#insn-008fb364)

~~~json
{
  "source": "008fb364",
  "target": "00633334",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb368`](#insn-008fb368)

~~~json
{
  "source": "008fb368",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb370`](#insn-008fb370)

~~~json
{
  "source": "008fb370",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb378`](#insn-008fb378)

~~~json
{
  "source": "008fb378",
  "target": "008fb3a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb384`](#insn-008fb384)

~~~json
{
  "source": "008fb384",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb388`](#insn-008fb388)

~~~json
{
  "source": "008fb388",
  "target": "008fb3a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb3a0`](#insn-008fb3a0)

~~~json
{
  "source": "008fb3a0",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb3a4`](#insn-008fb3a4)

~~~json
{
  "source": "008fb3a4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb3a8`](#insn-008fb3a8)

~~~json
{
  "source": "008fb3a8",
  "target": "008fb3bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb3b4`](#insn-008fb3b4)

~~~json
{
  "source": "008fb3b4",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb3b8`](#insn-008fb3b8)

~~~json
{
  "source": "008fb3b8",
  "target": "008fb534",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb3bc`](#insn-008fb3bc)

~~~json
{
  "source": "008fb3bc",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb3c0`](#insn-008fb3c0)

~~~json
{
  "source": "008fb3c0",
  "target": "008fb3cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb3c4`](#insn-008fb3c4)

~~~json
{
  "source": "008fb3c4",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb3c8`](#insn-008fb3c8)

~~~json
{
  "source": "008fb3c8",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb3cc`](#insn-008fb3cc)

~~~json
{
  "source": "008fb3cc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb3d0`](#insn-008fb3d0)

~~~json
{
  "source": "008fb3d0",
  "target": "008fb3dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb3d4`](#insn-008fb3d4)

~~~json
{
  "source": "008fb3d4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb3d8`](#insn-008fb3d8)

~~~json
{
  "source": "008fb3d8",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb3e4`](#insn-008fb3e4)

~~~json
{
  "source": "008fb3e4",
  "target": "00862c10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb3e8`](#insn-008fb3e8)

~~~json
{
  "source": "008fb3e8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb3f0`](#insn-008fb3f0)

~~~json
{
  "source": "008fb3f0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb3f8`](#insn-008fb3f8)

~~~json
{
  "source": "008fb3f8",
  "target": "008fb424",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb404`](#insn-008fb404)

~~~json
{
  "source": "008fb404",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb408`](#insn-008fb408)

~~~json
{
  "source": "008fb408",
  "target": "008fb424",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb420`](#insn-008fb420)

~~~json
{
  "source": "008fb420",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb424`](#insn-008fb424)

~~~json
{
  "source": "008fb424",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb428`](#insn-008fb428)

~~~json
{
  "source": "008fb428",
  "target": "008fb454",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb434`](#insn-008fb434)

~~~json
{
  "source": "008fb434",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb438`](#insn-008fb438)

~~~json
{
  "source": "008fb438",
  "target": "008fb454",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb450`](#insn-008fb450)

~~~json
{
  "source": "008fb450",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb454`](#insn-008fb454)

~~~json
{
  "source": "008fb454",
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
- 参照命令 [`008fb458`](#insn-008fb458)

~~~json
{
  "source": "008fb458",
  "target": "008fb8b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb464`](#insn-008fb464)

~~~json
{
  "source": "008fb464",
  "target": "Stack[-0x85]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb468`](#insn-008fb468)

~~~json
{
  "source": "008fb468",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb474`](#insn-008fb474)

~~~json
{
  "source": "008fb474",
  "target": "002a448a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a448a",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "696d673130322e706e6700",
  "capture_start": "002a448a",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb478`](#insn-008fb478)

~~~json
{
  "source": "008fb478",
  "target": "Stack[-0x87]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb480`](#insn-008fb480)

~~~json
{
  "source": "008fb480",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb484`](#insn-008fb484)

~~~json
{
  "source": "008fb484",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb490`](#insn-008fb490)

~~~json
{
  "source": "008fb490",
  "target": "002bdbdd",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb494`](#insn-008fb494)

~~~json
{
  "source": "008fb494",
  "target": "002bdbe2",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bdbe2",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "322e696d6763757400",
  "capture_start": "002bdbe2",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb498`](#insn-008fb498)

~~~json
{
  "source": "008fb498",
  "target": "Stack[-0x9a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb49c`](#insn-008fb49c)

~~~json
{
  "source": "008fb49c",
  "target": "Stack[-0xa7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb4a0`](#insn-008fb4a0)

~~~json
{
  "source": "008fb4a0",
  "target": "Stack[-0xa2]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb4b8`](#insn-008fb4b8)

~~~json
{
  "source": "008fb4b8",
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
- 参照命令 [`008fb4c0`](#insn-008fb4c0)

~~~json
{
  "source": "008fb4c0",
  "target": "00633334",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb4c4`](#insn-008fb4c4)

~~~json
{
  "source": "008fb4c4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb4cc`](#insn-008fb4cc)

~~~json
{
  "source": "008fb4cc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb4d4`](#insn-008fb4d4)

~~~json
{
  "source": "008fb4d4",
  "target": "008fb500",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb4e0`](#insn-008fb4e0)

~~~json
{
  "source": "008fb4e0",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb4e4`](#insn-008fb4e4)

~~~json
{
  "source": "008fb4e4",
  "target": "008fb500",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb4fc`](#insn-008fb4fc)

~~~json
{
  "source": "008fb4fc",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb500`](#insn-008fb500)

~~~json
{
  "source": "008fb500",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb504`](#insn-008fb504)

~~~json
{
  "source": "008fb504",
  "target": "008fb518",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb510`](#insn-008fb510)

~~~json
{
  "source": "008fb510",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb514`](#insn-008fb514)

~~~json
{
  "source": "008fb514",
  "target": "008fb558",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb518`](#insn-008fb518)

~~~json
{
  "source": "008fb518",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb51c`](#insn-008fb51c)

~~~json
{
  "source": "008fb51c",
  "target": "008fb578",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb520`](#insn-008fb520)

~~~json
{
  "source": "008fb520",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb524`](#insn-008fb524)

~~~json
{
  "source": "008fb524",
  "target": "008fb588",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb528`](#insn-008fb528)

~~~json
{
  "source": "008fb528",
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
- 参照命令 [`008fb52c`](#insn-008fb52c)

~~~json
{
  "source": "008fb52c",
  "target": "008fb598",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb530`](#insn-008fb530)

~~~json
{
  "source": "008fb530",
  "target": "008fb908",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb548`](#insn-008fb548)

~~~json
{
  "source": "008fb548",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb54c`](#insn-008fb54c)

~~~json
{
  "source": "008fb54c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb550`](#insn-008fb550)

~~~json
{
  "source": "008fb550",
  "target": "008fb3c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb554`](#insn-008fb554)

~~~json
{
  "source": "008fb554",
  "target": "008fb3cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb56c`](#insn-008fb56c)

~~~json
{
  "source": "008fb56c",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb570`](#insn-008fb570)

~~~json
{
  "source": "008fb570",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb574`](#insn-008fb574)

~~~json
{
  "source": "008fb574",
  "target": "008fb520",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb578`](#insn-008fb578)

~~~json
{
  "source": "008fb578",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb57c`](#insn-008fb57c)

~~~json
{
  "source": "008fb57c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb580`](#insn-008fb580)

~~~json
{
  "source": "008fb580",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb584`](#insn-008fb584)

~~~json
{
  "source": "008fb584",
  "target": "008fb528",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb588`](#insn-008fb588)

~~~json
{
  "source": "008fb588",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb58c`](#insn-008fb58c)

~~~json
{
  "source": "008fb58c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb590`](#insn-008fb590)

~~~json
{
  "source": "008fb590",
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
- 参照命令 [`008fb594`](#insn-008fb594)

~~~json
{
  "source": "008fb594",
  "target": "008fb908",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb5a4`](#insn-008fb5a4)

~~~json
{
  "source": "008fb5a4",
  "target": "002a33f1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a33f1",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "696d673035305f30322e706e6700",
  "capture_start": "002a33f1",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb5a8`](#insn-008fb5a8)

~~~json
{
  "source": "008fb5a8",
  "target": "002a33f6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a33f1",
  "offset": 5,
  "size": 14,
  "datatype": "string",
  "bytes": "696d673035305f30322e706e6700",
  "capture_start": "002a33f1",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb5ac`](#insn-008fb5ac)

~~~json
{
  "source": "008fb5ac",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb5b4`](#insn-008fb5b4)

~~~json
{
  "source": "008fb5b4",
  "target": "Stack[-0x82]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb5b8`](#insn-008fb5b8)

~~~json
{
  "source": "008fb5b8",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb5bc`](#insn-008fb5bc)

~~~json
{
  "source": "008fb5bc",
  "target": "Stack[-0x8a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb5c8`](#insn-008fb5c8)

~~~json
{
  "source": "008fb5c8",
  "target": "002c02cb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c02cb",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "696d673035305f30322e696d6763757400",
  "capture_start": "002c02cb",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008fb5cc`](#insn-008fb5cc)

~~~json
{
  "source": "008fb5cc",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb5d0`](#insn-008fb5d0)

~~~json
{
  "source": "008fb5d0",
  "target": "Stack[-0x97]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb5d4`](#insn-008fb5d4)

~~~json
{
  "source": "008fb5d4",
  "target": "Stack[-0xa7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb5dc`](#insn-008fb5dc)

~~~json
{
  "source": "008fb5dc",
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
- 参照命令 [`008fb5f0`](#insn-008fb5f0)

~~~json
{
  "source": "008fb5f0",
  "target": "00633334",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb5f4`](#insn-008fb5f4)

~~~json
{
  "source": "008fb5f4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb5fc`](#insn-008fb5fc)

~~~json
{
  "source": "008fb5fc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb604`](#insn-008fb604)

~~~json
{
  "source": "008fb604",
  "target": "008fb630",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb610`](#insn-008fb610)

~~~json
{
  "source": "008fb610",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb614`](#insn-008fb614)

~~~json
{
  "source": "008fb614",
  "target": "008fb630",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb62c`](#insn-008fb62c)

~~~json
{
  "source": "008fb62c",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb630`](#insn-008fb630)

~~~json
{
  "source": "008fb630",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb634`](#insn-008fb634)

~~~json
{
  "source": "008fb634",
  "target": "008fb648",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb640`](#insn-008fb640)

~~~json
{
  "source": "008fb640",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb644`](#insn-008fb644)

~~~json
{
  "source": "008fb644",
  "target": "008fb694",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb648`](#insn-008fb648)

~~~json
{
  "source": "008fb648",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb64c`](#insn-008fb64c)

~~~json
{
  "source": "008fb64c",
  "target": "008fb658",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb650`](#insn-008fb650)

~~~json
{
  "source": "008fb650",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb654`](#insn-008fb654)

~~~json
{
  "source": "008fb654",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
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
- 参照命令 [`008fb65c`](#insn-008fb65c)

~~~json
{
  "source": "008fb65c",
  "target": "008fb668",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb660`](#insn-008fb660)

~~~json
{
  "source": "008fb660",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb664`](#insn-008fb664)

~~~json
{
  "source": "008fb664",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb66c`](#insn-008fb66c)

~~~json
{
  "source": "008fb66c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb674`](#insn-008fb674)

~~~json
{
  "source": "008fb674",
  "target": "008fb9cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb678`](#insn-008fb678)

~~~json
{
  "source": "008fb678",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb67c`](#insn-008fb67c)

~~~json
{
  "source": "008fb67c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb680`](#insn-008fb680)

~~~json
{
  "source": "008fb680",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb684`](#insn-008fb684)

~~~json
{
  "source": "008fb684",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb688`](#insn-008fb688)

~~~json
{
  "source": "008fb688",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb6a8`](#insn-008fb6a8)

~~~json
{
  "source": "008fb6a8",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb6ac`](#insn-008fb6ac)

~~~json
{
  "source": "008fb6ac",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb6b0`](#insn-008fb6b0)

~~~json
{
  "source": "008fb6b0",
  "target": "008fb650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb6b4`](#insn-008fb6b4)

~~~json
{
  "source": "008fb6b4",
  "target": "008fb658",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb6bc`](#insn-008fb6bc)

~~~json
{
  "source": "008fb6bc",
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
- 参照命令 [`008fb6c0`](#insn-008fb6c0)

~~~json
{
  "source": "008fb6c0",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb6c4`](#insn-008fb6c4)

~~~json
{
  "source": "008fb6c4",
  "target": "008fad44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb6cc`](#insn-008fb6cc)

~~~json
{
  "source": "008fb6cc",
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
- 参照命令 [`008fb6d4`](#insn-008fb6d4)

~~~json
{
  "source": "008fb6d4",
  "target": "0047ed74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb6e0`](#insn-008fb6e0)

~~~json
{
  "source": "008fb6e0",
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
- 参照命令 [`008fb6e4`](#insn-008fb6e4)

~~~json
{
  "source": "008fb6e4",
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
- 参照命令 [`008fb6e8`](#insn-008fb6e8)

~~~json
{
  "source": "008fb6e8",
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
- 参照命令 [`008fb6e8`](#insn-008fb6e8)

~~~json
{
  "source": "008fb6e8",
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
- 参照命令 [`008fb6f0`](#insn-008fb6f0)

~~~json
{
  "source": "008fb6f0",
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
- 参照命令 [`008fb6f0`](#insn-008fb6f0)

~~~json
{
  "source": "008fb6f0",
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
- 参照命令 [`008fb6f4`](#insn-008fb6f4)

~~~json
{
  "source": "008fb6f4",
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
- 参照命令 [`008fb6f8`](#insn-008fb6f8)

~~~json
{
  "source": "008fb6f8",
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
- 参照命令 [`008fb6f8`](#insn-008fb6f8)

~~~json
{
  "source": "008fb6f8",
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
- 参照命令 [`008fb6f8`](#insn-008fb6f8)

~~~json
{
  "source": "008fb6f8",
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
- 参照命令 [`008fb6fc`](#insn-008fb6fc)

~~~json
{
  "source": "008fb6fc",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb704`](#insn-008fb704)

~~~json
{
  "source": "008fb704",
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
- 参照命令 [`008fb708`](#insn-008fb708)

~~~json
{
  "source": "008fb708",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb70c`](#insn-008fb70c)

~~~json
{
  "source": "008fb70c",
  "target": "008fad44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb714`](#insn-008fb714)

~~~json
{
  "source": "008fb714",
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
- 参照命令 [`008fb718`](#insn-008fb718)

~~~json
{
  "source": "008fb718",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb71c`](#insn-008fb71c)

~~~json
{
  "source": "008fb71c",
  "target": "008faea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb728`](#insn-008fb728)

~~~json
{
  "source": "008fb728",
  "target": "0047ed74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb72c`](#insn-008fb72c)

~~~json
{
  "source": "008fb72c",
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
- 参照命令 [`008fb734`](#insn-008fb734)

~~~json
{
  "source": "008fb734",
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
- 参照命令 [`008fb738`](#insn-008fb738)

~~~json
{
  "source": "008fb738",
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
- 参照命令 [`008fb738`](#insn-008fb738)

~~~json
{
  "source": "008fb738",
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
- 参照命令 [`008fb740`](#insn-008fb740)

~~~json
{
  "source": "008fb740",
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
- 参照命令 [`008fb744`](#insn-008fb744)

~~~json
{
  "source": "008fb744",
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
- 参照命令 [`008fb744`](#insn-008fb744)

~~~json
{
  "source": "008fb744",
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
- 参照命令 [`008fb748`](#insn-008fb748)

~~~json
{
  "source": "008fb748",
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
- 参照命令 [`008fb74c`](#insn-008fb74c)

~~~json
{
  "source": "008fb74c",
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
- 参照命令 [`008fb74c`](#insn-008fb74c)

~~~json
{
  "source": "008fb74c",
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
- 参照命令 [`008fb74c`](#insn-008fb74c)

~~~json
{
  "source": "008fb74c",
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
- 参照命令 [`008fb750`](#insn-008fb750)

~~~json
{
  "source": "008fb750",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb758`](#insn-008fb758)

~~~json
{
  "source": "008fb758",
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
- 参照命令 [`008fb75c`](#insn-008fb75c)

~~~json
{
  "source": "008fb75c",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb760`](#insn-008fb760)

~~~json
{
  "source": "008fb760",
  "target": "008faea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb768`](#insn-008fb768)

~~~json
{
  "source": "008fb768",
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
- 参照命令 [`008fb76c`](#insn-008fb76c)

~~~json
{
  "source": "008fb76c",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb770`](#insn-008fb770)

~~~json
{
  "source": "008fb770",
  "target": "008fafd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb77c`](#insn-008fb77c)

~~~json
{
  "source": "008fb77c",
  "target": "0047ed74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb780`](#insn-008fb780)

~~~json
{
  "source": "008fb780",
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
- 参照命令 [`008fb788`](#insn-008fb788)

~~~json
{
  "source": "008fb788",
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
- 参照命令 [`008fb78c`](#insn-008fb78c)

~~~json
{
  "source": "008fb78c",
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
- 参照命令 [`008fb78c`](#insn-008fb78c)

~~~json
{
  "source": "008fb78c",
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
- 参照命令 [`008fb794`](#insn-008fb794)

~~~json
{
  "source": "008fb794",
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
- 参照命令 [`008fb798`](#insn-008fb798)

~~~json
{
  "source": "008fb798",
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
- 参照命令 [`008fb798`](#insn-008fb798)

~~~json
{
  "source": "008fb798",
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
- 参照命令 [`008fb79c`](#insn-008fb79c)

~~~json
{
  "source": "008fb79c",
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
- 参照命令 [`008fb7a0`](#insn-008fb7a0)

~~~json
{
  "source": "008fb7a0",
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
- 参照命令 [`008fb7a0`](#insn-008fb7a0)

~~~json
{
  "source": "008fb7a0",
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
- 参照命令 [`008fb7a0`](#insn-008fb7a0)

~~~json
{
  "source": "008fb7a0",
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
- 参照命令 [`008fb7a4`](#insn-008fb7a4)

~~~json
{
  "source": "008fb7a4",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb7ac`](#insn-008fb7ac)

~~~json
{
  "source": "008fb7ac",
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
- 参照命令 [`008fb7b0`](#insn-008fb7b0)

~~~json
{
  "source": "008fb7b0",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb7b4`](#insn-008fb7b4)

~~~json
{
  "source": "008fb7b4",
  "target": "008fafd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb7bc`](#insn-008fb7bc)

~~~json
{
  "source": "008fb7bc",
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
- 参照命令 [`008fb7c0`](#insn-008fb7c0)

~~~json
{
  "source": "008fb7c0",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb7c4`](#insn-008fb7c4)

~~~json
{
  "source": "008fb7c4",
  "target": "008fb0e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb7d0`](#insn-008fb7d0)

~~~json
{
  "source": "008fb7d0",
  "target": "0047ed74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb7d4`](#insn-008fb7d4)

~~~json
{
  "source": "008fb7d4",
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
- 参照命令 [`008fb7dc`](#insn-008fb7dc)

~~~json
{
  "source": "008fb7dc",
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
- 参照命令 [`008fb7e0`](#insn-008fb7e0)

~~~json
{
  "source": "008fb7e0",
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
- 参照命令 [`008fb7e0`](#insn-008fb7e0)

~~~json
{
  "source": "008fb7e0",
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
- 参照命令 [`008fb7e8`](#insn-008fb7e8)

~~~json
{
  "source": "008fb7e8",
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
- 参照命令 [`008fb7ec`](#insn-008fb7ec)

~~~json
{
  "source": "008fb7ec",
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
- 参照命令 [`008fb7ec`](#insn-008fb7ec)

~~~json
{
  "source": "008fb7ec",
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
- 参照命令 [`008fb7f0`](#insn-008fb7f0)

~~~json
{
  "source": "008fb7f0",
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
- 参照命令 [`008fb7f4`](#insn-008fb7f4)

~~~json
{
  "source": "008fb7f4",
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
- 参照命令 [`008fb7f4`](#insn-008fb7f4)

~~~json
{
  "source": "008fb7f4",
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
- 参照命令 [`008fb7f4`](#insn-008fb7f4)

~~~json
{
  "source": "008fb7f4",
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
- 参照命令 [`008fb7f8`](#insn-008fb7f8)

~~~json
{
  "source": "008fb7f8",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb800`](#insn-008fb800)

~~~json
{
  "source": "008fb800",
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
- 参照命令 [`008fb804`](#insn-008fb804)

~~~json
{
  "source": "008fb804",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb808`](#insn-008fb808)

~~~json
{
  "source": "008fb808",
  "target": "008fb0e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb810`](#insn-008fb810)

~~~json
{
  "source": "008fb810",
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
- 参照命令 [`008fb814`](#insn-008fb814)

~~~json
{
  "source": "008fb814",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb818`](#insn-008fb818)

~~~json
{
  "source": "008fb818",
  "target": "008fb1f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb824`](#insn-008fb824)

~~~json
{
  "source": "008fb824",
  "target": "0047ed74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb828`](#insn-008fb828)

~~~json
{
  "source": "008fb828",
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
- 参照命令 [`008fb830`](#insn-008fb830)

~~~json
{
  "source": "008fb830",
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
- 参照命令 [`008fb834`](#insn-008fb834)

~~~json
{
  "source": "008fb834",
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
- 参照命令 [`008fb834`](#insn-008fb834)

~~~json
{
  "source": "008fb834",
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
- 参照命令 [`008fb83c`](#insn-008fb83c)

~~~json
{
  "source": "008fb83c",
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
- 参照命令 [`008fb840`](#insn-008fb840)

~~~json
{
  "source": "008fb840",
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
- 参照命令 [`008fb840`](#insn-008fb840)

~~~json
{
  "source": "008fb840",
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
- 参照命令 [`008fb844`](#insn-008fb844)

~~~json
{
  "source": "008fb844",
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
- 参照命令 [`008fb848`](#insn-008fb848)

~~~json
{
  "source": "008fb848",
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
- 参照命令 [`008fb848`](#insn-008fb848)

~~~json
{
  "source": "008fb848",
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
- 参照命令 [`008fb848`](#insn-008fb848)

~~~json
{
  "source": "008fb848",
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
- 参照命令 [`008fb84c`](#insn-008fb84c)

~~~json
{
  "source": "008fb84c",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb854`](#insn-008fb854)

~~~json
{
  "source": "008fb854",
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
- 参照命令 [`008fb858`](#insn-008fb858)

~~~json
{
  "source": "008fb858",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb85c`](#insn-008fb85c)

~~~json
{
  "source": "008fb85c",
  "target": "008fb1f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb864`](#insn-008fb864)

~~~json
{
  "source": "008fb864",
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
- 参照命令 [`008fb868`](#insn-008fb868)

~~~json
{
  "source": "008fb868",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb86c`](#insn-008fb86c)

~~~json
{
  "source": "008fb86c",
  "target": "008fb308",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb878`](#insn-008fb878)

~~~json
{
  "source": "008fb878",
  "target": "0047ed74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb87c`](#insn-008fb87c)

~~~json
{
  "source": "008fb87c",
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
- 参照命令 [`008fb884`](#insn-008fb884)

~~~json
{
  "source": "008fb884",
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
- 参照命令 [`008fb888`](#insn-008fb888)

~~~json
{
  "source": "008fb888",
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
- 参照命令 [`008fb888`](#insn-008fb888)

~~~json
{
  "source": "008fb888",
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
- 参照命令 [`008fb890`](#insn-008fb890)

~~~json
{
  "source": "008fb890",
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
- 参照命令 [`008fb894`](#insn-008fb894)

~~~json
{
  "source": "008fb894",
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
- 参照命令 [`008fb894`](#insn-008fb894)

~~~json
{
  "source": "008fb894",
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
- 参照命令 [`008fb898`](#insn-008fb898)

~~~json
{
  "source": "008fb898",
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
- 参照命令 [`008fb89c`](#insn-008fb89c)

~~~json
{
  "source": "008fb89c",
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
- 参照命令 [`008fb89c`](#insn-008fb89c)

~~~json
{
  "source": "008fb89c",
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
- 参照命令 [`008fb89c`](#insn-008fb89c)

~~~json
{
  "source": "008fb89c",
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
- 参照命令 [`008fb8a0`](#insn-008fb8a0)

~~~json
{
  "source": "008fb8a0",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb8a8`](#insn-008fb8a8)

~~~json
{
  "source": "008fb8a8",
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
- 参照命令 [`008fb8ac`](#insn-008fb8ac)

~~~json
{
  "source": "008fb8ac",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb8b0`](#insn-008fb8b0)

~~~json
{
  "source": "008fb8b0",
  "target": "008fb308",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb8b8`](#insn-008fb8b8)

~~~json
{
  "source": "008fb8b8",
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
- 参照命令 [`008fb8bc`](#insn-008fb8bc)

~~~json
{
  "source": "008fb8bc",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb8c0`](#insn-008fb8c0)

~~~json
{
  "source": "008fb8c0",
  "target": "008fb45c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb8cc`](#insn-008fb8cc)

~~~json
{
  "source": "008fb8cc",
  "target": "0047ed74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb8d0`](#insn-008fb8d0)

~~~json
{
  "source": "008fb8d0",
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
- 参照命令 [`008fb8d8`](#insn-008fb8d8)

~~~json
{
  "source": "008fb8d8",
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
- 参照命令 [`008fb8dc`](#insn-008fb8dc)

~~~json
{
  "source": "008fb8dc",
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
- 参照命令 [`008fb8dc`](#insn-008fb8dc)

~~~json
{
  "source": "008fb8dc",
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
- 参照命令 [`008fb8e4`](#insn-008fb8e4)

~~~json
{
  "source": "008fb8e4",
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
- 参照命令 [`008fb8e8`](#insn-008fb8e8)

~~~json
{
  "source": "008fb8e8",
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
- 参照命令 [`008fb8e8`](#insn-008fb8e8)

~~~json
{
  "source": "008fb8e8",
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
- 参照命令 [`008fb8ec`](#insn-008fb8ec)

~~~json
{
  "source": "008fb8ec",
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
- 参照命令 [`008fb8f0`](#insn-008fb8f0)

~~~json
{
  "source": "008fb8f0",
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
- 参照命令 [`008fb8f0`](#insn-008fb8f0)

~~~json
{
  "source": "008fb8f0",
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
- 参照命令 [`008fb8f0`](#insn-008fb8f0)

~~~json
{
  "source": "008fb8f0",
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
- 参照命令 [`008fb8f4`](#insn-008fb8f4)

~~~json
{
  "source": "008fb8f4",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb8fc`](#insn-008fb8fc)

~~~json
{
  "source": "008fb8fc",
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
- 参照命令 [`008fb900`](#insn-008fb900)

~~~json
{
  "source": "008fb900",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb904`](#insn-008fb904)

~~~json
{
  "source": "008fb904",
  "target": "008fb45c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb90c`](#insn-008fb90c)

~~~json
{
  "source": "008fb90c",
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
- 参照命令 [`008fb910`](#insn-008fb910)

~~~json
{
  "source": "008fb910",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb914`](#insn-008fb914)

~~~json
{
  "source": "008fb914",
  "target": "008fb598",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb920`](#insn-008fb920)

~~~json
{
  "source": "008fb920",
  "target": "0047ed74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb924`](#insn-008fb924)

~~~json
{
  "source": "008fb924",
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
- 参照命令 [`008fb92c`](#insn-008fb92c)

~~~json
{
  "source": "008fb92c",
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
- 参照命令 [`008fb930`](#insn-008fb930)

~~~json
{
  "source": "008fb930",
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
- 参照命令 [`008fb930`](#insn-008fb930)

~~~json
{
  "source": "008fb930",
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
- 参照命令 [`008fb938`](#insn-008fb938)

~~~json
{
  "source": "008fb938",
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
- 参照命令 [`008fb93c`](#insn-008fb93c)

~~~json
{
  "source": "008fb93c",
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
- 参照命令 [`008fb93c`](#insn-008fb93c)

~~~json
{
  "source": "008fb93c",
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
- 参照命令 [`008fb940`](#insn-008fb940)

~~~json
{
  "source": "008fb940",
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
- 参照命令 [`008fb944`](#insn-008fb944)

~~~json
{
  "source": "008fb944",
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
- 参照命令 [`008fb944`](#insn-008fb944)

~~~json
{
  "source": "008fb944",
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
- 参照命令 [`008fb944`](#insn-008fb944)

~~~json
{
  "source": "008fb944",
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
- 参照命令 [`008fb948`](#insn-008fb948)

~~~json
{
  "source": "008fb948",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb950`](#insn-008fb950)

~~~json
{
  "source": "008fb950",
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
- 参照命令 [`008fb954`](#insn-008fb954)

~~~json
{
  "source": "008fb954",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008fb958`](#insn-008fb958)

~~~json
{
  "source": "008fb958",
  "target": "008fb598",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008fb9cc`](#insn-008fb9cc)

~~~json
{
  "source": "008fb9cc",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
