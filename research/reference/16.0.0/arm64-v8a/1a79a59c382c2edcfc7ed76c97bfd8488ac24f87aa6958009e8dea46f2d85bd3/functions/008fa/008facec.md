# 008facec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

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
  "source_text_sha256": "d4b3c95d9ae1cc12d887c621a254ce31fbf9b2a0560f70a849092eacaabbb2a4"
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
