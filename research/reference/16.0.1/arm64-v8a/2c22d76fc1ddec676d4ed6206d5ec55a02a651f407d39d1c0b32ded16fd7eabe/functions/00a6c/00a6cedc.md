# 00a6cedc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00a6cedc",
  "name": "FUN_00a6cedc",
  "size": 3244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "60f1b3f398676e2f30f80903383942df14bb1eafbd195a1ed38d23f7cdbfe05c",
  "source_text_sha256": "60f1b3f398676e2f30f80903383942df14bb1eafbd195a1ed38d23f7cdbfe05c"
}
~~~

## 呼び出し元

- [00a6dcd4](../00a6d/00a6dcd4.md)

## 呼び出し先

- [00447ef4](../00447/00447ef4.md)
- [0047e60c](../0047e/0047e60c.md)
- [0048ce54](../0048c/0048ce54.md)
- [0067e19c](../0067e/0067e19c.md)
- [00864160](../00864/00864160.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c57e30](../00c57/00c57e30.md)
- [00c57e50](../00c57/00c57e50.md)
- [00c57e70](../00c57/00c57e70.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 関連文字列（未確認候補）

~~~text
"%03d_stamp_f.imgcut"
"%03d_stamp_f.png"
"001_img044.imgcut"
"001_img044.png"
"1.imgcut"
"4.imgcut"
"5.imgcut"
"6.imgcut"
"7.imgcut"
"g044.png"
"img006.imgcut"
"img006.png"
"img007.imgcut"
"img007.png"
"img024.imgcut"
"img024.png"
"img025.imgcut"
"img025.png"
"img101.imgcut"
"img101.png"
"img101_nekoDojo.imgcut"
"img101_nekoDojo.png"
~~~

## 疑似コード / UTF-8 21076 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */
/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00a6cedc(undefined8 *param_1,long param_2)

{
  ulong uVar1;
  byte bVar2;
  long lVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  int iVar6;
  long lVar7;
  byte *pbVar8;
  byte *pbVar9;
  long *plVar10;
  long *plVar11;
  byte local_108;
  char local_107 [8];
  undefined7 uStack_ff;
  undefined4 uStack_f8;
  uint uStack_f4;
  byte local_f0 [16];
  void *local_e0;
  byte local_d8 [16];
  void *local_c8;
  byte local_c0;
  undefined7 uStack_bf;
  char cStack_b8;
  undefined7 uStack_b7;
  char local_b0;
  undefined1 uStack_af;
  undefined6 uStack_ae;
  undefined8 local_a0;
  long *plStack_98;
  byte local_88;
  undefined5 local_87;
  undefined3 uStack_82;
  undefined5 uStack_7f;
  char cStack_7a;
  char cStack_79;
  char cStack_78;
  undefined2 uStack_77;
  undefined4 uStack_75;
  undefined1 uStack_71;
  byte local_70;
  undefined6 uStack_6f;
  char cStack_69;
  char cStack_68;
  undefined2 uStack_67;
  uint uStack_65;
  char cStack_61;
  undefined4 local_60;
  uint uStack_5c;
  long local_58;
  
  lVar3 = tpidr_el0;
  local_58 = *(long *)(lVar3 + 0x28);
  FUN_0067e19c();
  *param_1 = &PTR_FUN_00c8b9e0;
                    /* try { // try from 00a6cf2c to 00b6cf37 has its CatchHandler @ 00a77fd8 */
  param_1[0x5d] = 0;
  param_1[0x5c] = 0;
  param_1[0x5f] = 0;
  param_1[0x5e] = 0;
  param_1[0x61] = 0;
  param_1[0x60] = 0;
  param_1[99] = 0;
  param_1[0x62] = 0;
  param_1[0x65] = 0;
  param_1[100] = 0;
  param_1[0x67] = 0;
  param_1[0x66] = 0;
                    /* try { // try from 00a6cf38 to 00b6d02f has its CatchHandler @ 00a63fd8 */
  param_1[0x69] = 0;
  param_1[0x68] = 0;
  param_1[0x6b] = 0;
  param_1[0x6a] = 0;
  param_1[0x6d] = 0;
  param_1[0x6c] = 0;
  param_1[0x6f] = 0;
  param_1[0x6e] = 0;
  param_1[0x71] = 0;
  param_1[0x70] = 0;
  param_1[0x73] = 0;
  param_1[0x72] = 0;
  param_1[0x75] = 0;
  param_1[0x74] = 0;
  param_1[0x77] = 0;
  param_1[0x76] = 0;
  param_1[0x79] = 0;
  param_1[0x78] = 0;
  param_1[0x7b] = 0;
  param_1[0x7a] = 0;
  param_1[0x7d] = 0;
  param_1[0x7c] = 0;
  param_1[0x7f] = 0;
  param_1[0x7e] = 0;
  param_1[0x81] = 0;
  param_1[0x80] = 0;
  param_1[0x83] = 0;
  param_1[0x82] = 0;
  param_1[0x85] = 0;
  param_1[0x84] = 0;
  if (((DAT_00ca4f38 & 1) == 0) && (iVar6 = __cxa_guard_acquire(&DAT_00ca4f38), iVar6 != 0)) {
    DAT_00ca4f08 = 0;
    DAT_00ca4f00 = &DAT_00ca4f08;
    DAT_00ca4f28 = 0;
    DAT_00ca4f30 = 0;
    DAT_00ca4f20 = 0;
    DAT_00ca4f10 = 0;
    DAT_00ca4f18 = &DAT_00ca4f20;
    __cxa_atexit(FUN_0047edb4,&DAT_00ca4f00,&PTR_LOOP_00c62f90);
    __cxa_guard_release(&DAT_00ca4f38);
  }
  uStack_65 = uStack_65 & 0xffffff00;
  local_70 = 0x14;
  uStack_67 = 0x676e;
  local_88 = 0x1a;
  uStack_6f = (undefined6)s_img006_png_002b638e._0_8_;
  cStack_69 = SUB81(s_img006_png_002b638e._0_8_,6);
  cStack_68 = SUB81(s_img006_png_002b638e._0_8_,7);
  cStack_7a = 0;
  local_87 = _DAT_002b1f16;
  uStack_82._0_1_ = s_6_imgcut_002b1f1b[0];
  uStack_82._1_1_ = s_6_imgcut_002b1f1b[1];
  uStack_82._2_1_ = s_6_imgcut_002b1f1b[2];
  uStack_7f._0_1_ = s_6_imgcut_002b1f1b[3];
  uStack_7f._1_1_ = s_6_imgcut_002b1f1b[4];
  uStack_7f._2_1_ = s_6_imgcut_002b1f1b[5];
  uStack_7f._3_1_ = s_6_imgcut_002b1f1b[6];
  uStack_7f._4_1_ = s_6_imgcut_002b1f1b[7];
  FUN_0047e60c(&local_c0,&DAT_00ca4f00,&local_70,&local_88,0x2601);
  uVar5 = CONCAT71(uStack_b7,cStack_b8);
  uVar4 = CONCAT71(uStack_bf,local_c0);
  plVar11 = (long *)param_1[0x5d];
  local_c0 = 0;
  uStack_bf = 0;
  cStack_b8 = 0;
  uStack_b7 = 0;
  param_1[0x5d] = uVar5;
  param_1[0x5c] = uVar4;
  if ((plVar11 != (long *)0x0) && (lVar7 = FUN_00c53d00(0xffffffffffffffff,plVar11 + 1), lVar7 == 0)
     ) {
    (**(code **)(*plVar11 + 0x10))(plVar11);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar11);
  }
  plVar11 = (long *)CONCAT71(uStack_b7,cStack_b8);
  if ((plVar11 != (long *)0x0) && (lVar7 = FUN_00c53d00(0xffffffffffffffff,plVar11 + 1), lVar7 == 0)
     ) {
    (**(code **)(*plVar11 + 0x10))(plVar11);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar11);
  }
  if ((local_88 & 1) != 0) {
    _ZdlPv((void *)CONCAT17(uStack_71,CONCAT43(uStack_75,CONCAT21(uStack_77,cStack_78))));
                    /* try { // try from 00a6d064 to 00b6d073 has its CatchHandler @ 00a78078 */
  }
  if ((local_70 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_5c,local_60));
                    /* try { // try from 00a6d074 to 00b6daab has its CatchHandler @ 00a63fd8 */
  }
  if (((DAT_00ca4f38 & 1) == 0) && (iVar6 = __cxa_guard_acquire(&DAT_00ca4f38), iVar6 != 0)) {
    DAT_00ca4f08 = 0;
    DAT_00ca4f00 = &DAT_00ca4f08;
    DAT_00ca4f28 = 0;
    DAT_00ca4f30 = 0;
    DAT_00ca4f20 = 0;
    DAT_00ca4f10 = 0;
    DAT_00ca4f18 = &DAT_00ca4f20;
    __cxa_atexit(FUN_0047edb4,&DAT_00ca4f00,&PTR_LOOP_00c62f90);
    __cxa_guard_release(&DAT_00ca4f38);
  }
  uStack_65 = uStack_65 & 0xffffff00;
  local_70 = 0x14;
  uStack_67 = 0x676e;
  local_88 = 0x1a;
  uStack_6f = (undefined6)s_img007_png_002a2318._0_8_;
  cStack_69 = SUB81(s_img007_png_002a2318._0_8_,6);
  cStack_68 = SUB81(s_img007_png_002a2318._0_8_,7);
  cStack_7a = 0;
  local_87 = _DAT_002bc8aa;
  uStack_82._0_1_ = s_7_imgcut_002bc8af[0];
  uStack_82._1_1_ = s_7_imgcut_002bc8af[1];
  uStack_82._2_1_ = s_7_imgcut_002bc8af[2];
  uStack_7f._0_1_ = s_7_imgcut_002bc8af[3];
  uStack_7f._1_1_ = s_7_imgcut_002bc8af[4];
  uStack_7f._2_1_ = s_7_imgcut_002bc8af[5];
  uStack_7f._3_1_ = s_7_imgcut_002bc8af[6];
  uStack_7f._4_1_ = s_7_imgcut_002bc8af[7];
  FUN_0047e60c(&local_c0,&DAT_00ca4f00,&local_70,&local_88,0x2601);
  uVar5 = CONCAT71(uStack_b7,cStack_b8);
  uVar4 = CONCAT71(uStack_bf,local_c0);
  plVar11 = (long *)param_1[0x5f];
  local_c0 = 0;
  uStack_bf = 0;
  cStack_b8 = 0;
  uStack_b7 = 0;
  param_1[0x5f] = uVar5;
  param_1[0x5e] = uVar4;
  if ((plVar11 != (long *)0x0) && (lVar7 = FUN_00c53d00(0xffffffffffffffff,plVar11 + 1), lVar7 == 0)
     ) {
    (**(code **)(*plVar11 + 0x10))(plVar11);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar11);
  }
  plVar11 = (long *)CONCAT71(uStack_b7,cStack_b8);
  if ((plVar11 != (long *)0x0) && (lVar7 = FUN_00c53d00(0xffffffffffffffff,plVar11 + 1), lVar7 == 0)
     ) {
    (**(code **)(*plVar11 + 0x10))(plVar11);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar11);
  }
  if ((local_88 & 1) != 0) {
    _ZdlPv((void *)CONCAT17(uStack_71,CONCAT43(uStack_75,CONCAT21(uStack_77,cStack_78))));
  }
  if ((local_70 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_5c,local_60));
  }
  FUN_00864160(&local_70,param_2);
  uVar5 = CONCAT17(cStack_61,CONCAT43(uStack_65,CONCAT21(uStack_67,cStack_68)));
  uVar4 = CONCAT17(cStack_69,CONCAT61(uStack_6f,local_70));
  plVar11 = (long *)param_1[0x61];
  local_70 = 0;
  uStack_6f = 0;
  cStack_69 = 0;
  cStack_68 = 0;
  uStack_67 = 0;
  uStack_65 = 0;
  cStack_61 = '\0';
  param_1[0x61] = uVar5;
  param_1[0x60] = uVar4;
  if ((plVar11 != (long *)0x0) && (lVar7 = FUN_00c53d00(0xffffffffffffffff,plVar11 + 1), lVar7 == 0)
     ) {
    (**(code **)(*plVar11 + 0x10))(plVar11);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar11);
  }
  plVar11 = (long *)CONCAT17(cStack_61,CONCAT43(uStack_65,CONCAT21(uStack_67,cStack_68)));
  if ((plVar11 != (long *)0x0) && (lVar7 = FUN_00c53d00(0xffffffffffffffff,plVar11 + 1), lVar7 == 0)
     ) {
    (**(code **)(*plVar11 + 0x10))(plVar11);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar11);
  }
  if (((DAT_00ca4f38 & 1) == 0) && (iVar6 = __cxa_guard_acquire(&DAT_00ca4f38), iVar6 != 0)) {
    DAT_00ca4f08 = 0;
    DAT_00ca4f00 = &DAT_00ca4f08;
    DAT_00ca4f28 = 0;
    DAT_00ca4f30 = 0;
    DAT_00ca4f20 = 0;
    DAT_00ca4f10 = 0;
    DAT_00ca4f18 = &DAT_00ca4f20;
    __cxa_atexit(FUN_0047edb4,&DAT_00ca4f00,&PTR_LOOP_00c62f90);
    __cxa_guard_release(&DAT_00ca4f38);
  }
  uStack_65 = uStack_65 & 0xffffff00;
  local_70 = 0x14;
  uStack_67 = 0x676e;
  local_88 = 0x1a;
  uStack_6f = (undefined6)s_img024_png_002befbe._0_8_;
  cStack_69 = SUB81(s_img024_png_002befbe._0_8_,6);
  cStack_68 = SUB81(s_img024_png_002befbe._0_8_,7);
  cStack_7a = 0;
  local_87 = _DAT_002a9fa3;
  uStack_82._0_1_ = s_4_imgcut_002a9fa8[0];
  uStack_82._1_1_ = s_4_imgcut_002a9fa8[1];
  uStack_82._2_1_ = s_4_imgcut_002a9fa8[2];
  uStack_7f._0_1_ = s_4_imgcut_002a9fa8[3];
  uStack_7f._1_1_ = s_4_imgcut_002a9fa8[4];
  uStack_7f._2_1_ = s_4_imgcut_002a9fa8[5];
  uStack_7f._3_1_ = s_4_imgcut_002a9fa8[6];
  uStack_7f._4_1_ = s_4_imgcut_002a9fa8[7];
  FUN_0047e60c(&local_c0,&DAT_00ca4f00,&local_70,&local_88,0x2601);
  uVar5 = CONCAT71(uStack_b7,cStack_b8);
  uVar4 = CONCAT71(uStack_bf,local_c0);
  plVar11 = (long *)param_1[0x67];
  local_c0 = 0;
  uStack_bf = 0;
  cStack_b8 = 0;
  uStack_b7 = 0;
  param_1[0x67] = uVar5;
  param_1[0x66] = uVar4;
  if ((plVar11 != (long *)0x0) && (lVar7 = FUN_00c53d00(0xffffffffffffffff,plVar11 + 1), lVar7 == 0)
     ) {
    (**(code **)(*plVar11 + 0x10))(plVar11);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar11);
  }
  plVar11 = (long *)CONCAT71(uStack_b7,cStack_b8);
  if ((plVar11 != (long *)0x0) && (lVar7 = FUN_00c53d00(0xffffffffffffffff,plVar11 + 1), lVar7 == 0)
     ) {
    (**(code **)(*plVar11 + 0x10))(plVar11);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar11);
  }
  if ((local_88 & 1) != 0) {
    _ZdlPv((void *)CONCAT17(uStack_71,CONCAT43(uStack_75,CONCAT21(uStack_77,cStack_78))));
  }
  if ((local_70 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_5c,local_60));
  }
  if (((DAT_00ca4f38 & 1) == 0) && (iVar6 = __cxa_guard_acquire(&DAT_00ca4f38), iVar6 != 0)) {
    DAT_00ca4f08 = 0;
    DAT_00ca4f00 = &DAT_00ca4f08;
    DAT_00ca4f28 = 0;
    DAT_00ca4f30 = 0;
    DAT_00ca4f20 = 0;
    DAT_00ca4f10 = 0;
    DAT_00ca4f18 = &DAT_00ca4f20;
    __cxa_atexit(FUN_0047edb4,&DAT_00ca4f00,&PTR_LOOP_00c62f90);
    __cxa_guard_release(&DAT_00ca4f38);
  }
  uStack_65 = uStack_65 & 0xffffff00;
  local_70 = 0x14;
  uStack_67 = 0x676e;
  local_88 = 0x1a;
  uStack_6f = (undefined6)s_img025_png_002b7632._0_8_;
  cStack_69 = SUB81(s_img025_png_002b7632._0_8_,6);
  cStack_68 = SUB81(s_img025_png_002b7632._0_8_,7);
  cStack_7a = '\0';
  local_87 = _DAT_002ab79f;
  uStack_82._0_1_ = s_5_imgcut_002ab7a4[0];
  uStack_82._1_1_ = s_5_imgcut_002ab7a4[1];
  uStack_82._2_1_ = s_5_imgcut_002ab7a4[2];
  uStack_7f._0_1_ = s_5_imgcut_002ab7a4[3];
  uStack_7f._1_1_ = s_5_imgcut_002ab7a4[4];
  uStack_7f._2_1_ = s_5_imgcut_002ab7a4[5];
  uStack_7f._3_1_ = s_5_imgcut_002ab7a4[6];
  uStack_7f._4_1_ = s_5_imgcut_002ab7a4[7];
  FUN_0047e60c(&local_c0,&DAT_00ca4f00,&local_70,&local_88,0x2601);
  uVar5 = CONCAT71(uStack_b7,cStack_b8);
  uVar4 = CONCAT71(uStack_bf,local_c0);
  plVar11 = (long *)param_1[0x71];
  local_c0 = 0;
  uStack_bf = 0;
  cStack_b8 = 0;
  uStack_b7 = 0;
  param_1[0x71] = uVar5;
  param_1[0x70] = uVar4;
  if ((plVar11 != (long *)0x0) && (lVar7 = FUN_00c53d00(0xffffffffffffffff,plVar11 + 1), lVar7 == 0)
     ) {
    (**(code **)(*plVar11 + 0x10))(plVar11);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar11);
  }
  plVar11 = (long *)CONCAT71(uStack_b7,cStack_b8);
  if ((plVar11 != (long *)0x0) && (lVar7 = FUN_00c53d00(0xffffffffffffffff,plVar11 + 1), lVar7 == 0)
     ) {
    (**(code **)(*plVar11 + 0x10))(plVar11);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar11);
  }
  if ((local_88 & 1) != 0) {
    _ZdlPv((void *)CONCAT17(uStack_71,CONCAT43(uStack_75,CONCAT21(uStack_77,cStack_78))));
  }
  if ((local_70 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_5c,local_60));
  }
  if ((*(int *)((long)&fde_table_entry_00333f48.data_loc + param_2) == 5) &&
     (*(char *)(param_2 + 0x33d9) != '\0')) {
    if (((DAT_00ca4f38 & 1) == 0) && (iVar6 = __cxa_guard_acquire(&DAT_00ca4f38), iVar6 != 0)) {
      DAT_00ca4f08 = 0;
      DAT_00ca4f00 = &DAT_00ca4f08;
      DAT_00ca4f28 = 0;
      DAT_00ca4f30 = 0;
      DAT_00ca4f20 = 0;
      DAT_00ca4f10 = 0;
      DAT_00ca4f18 = &DAT_00ca4f20;
      __cxa_atexit(FUN_0047edb4,&DAT_00ca4f00,&PTR_LOOP_00c62f90);
      __cxa_guard_release(&DAT_00ca4f38);
    }
    local_70 = 0x26;
    uStack_5c = uStack_5c & 0xffffff00;
    local_88 = 0x2c;
    uStack_67 = (undefined2)s_img101_nekoDojo_png_002b515f._8_8_;
    uStack_65 = SUB84(s_img101_nekoDojo_png_002b515f._8_8_,2);
    cStack_61 = SUB81(s_img101_nekoDojo_png_002b515f._8_8_,6);
    local_60 = CONCAT31(0x676e70,SUB81(s_img101_nekoDojo_png_002b515f._8_8_,7));
    uStack_6f = (undefined6)s_img101_nekoDojo_png_002b515f._0_8_;
    cStack_69 = SUB81(s_img101_nekoDojo_png_002b515f._0_8_,6);
    cStack_68 = SUB81(s_img101_nekoDojo_png_002b515f._0_8_,7);
    uStack_71 = 0;
    uStack_7f = (undefined5)s_img101_nekoDojo_imgcut_002befc9._8_6_;
    cStack_7a = SUB61(s_img101_nekoDojo_imgcut_002befc9._8_6_,5);
    local_87 = (undefined5)s_img101_nekoDojo_imgcut_002befc9._0_8_;
    uStack_82 = SUB83(s_img101_nekoDojo_imgcut_002befc9._0_8_,5);
    cStack_79 = (char)s_img101_nekoDojo_imgcut_002befc9._14_2_;
    cStack_78 = SUB21(s_img101_nekoDojo_imgcut_002befc9._14_2_,1);
    uStack_77 = (undefined2)s_img101_nekoDojo_imgcut_002befc9._16_6_;
    uStack_75 = SUB64(s_img101_nekoDojo_imgcut_002befc9._16_6_,2);
    FUN_0047e60c(&local_c0,&DAT_00ca4f00,&local_70,&local_88,0x2601);
  }
  else {
    pbVar8 = (byte *)param_1[0x7a];
    if (pbVar8 != (byte *)0x0) {
      bVar2 = *pbVar8;
      uVar1 = (ulong)(bVar2 >> 1);
      if ((bVar2 & 1) != 0) {
        uVar1 = *(ulong *)(pbVar8 + 8);
      }
      if (uVar1 != 0x13) goto LAB_00a6d5dc;
      pbVar9 = *(byte **)(pbVar8 + 0x10);
      if ((bVar2 & 1) == 0) {
        pbVar9 = pbVar8 + 1;
      }
      if ((*(long *)pbVar9 != 0x6e5f313031676d69 || *(long *)(pbVar9 + 8) != 0x2e6f6a6f446f6b65) ||
          *(long *)(pbVar9 + 0xb) != 0x676e702e6f6a6f44) goto LAB_00a6d5dc;
    }
    if (((DAT_00ca4f38 & 1) == 0) && (iVar6 = __cxa_guard_acquire(&DAT_00ca4f38), iVar6 != 0)) {
      DAT_00ca4f08 = 0;
      DAT_00ca4f00 = &DAT_00ca4f08;
      DAT_00ca4f28 = 0;
      DAT_00ca4f30 = 0;
      DAT_00ca4f20 = 0;
      DAT_00ca4f10 = 0;
      DAT_00ca4f18 = &DAT_00ca4f20;
      __cxa_atexit(FUN_0047edb4,&DAT_00ca4f00,&PTR_LOOP_00c62f90);
      __cxa_guard_release(&DAT_00ca4f38);
    }
    uStack_65 = uStack_65 & 0xffffff00;
    local_70 = 0x14;
    uStack_67 = 0x676e;
    local_88 = 0x1a;
    uStack_6f = (undefined6)s_img101_png_002befe0._0_8_;
    cStack_69 = SUB81(s_img101_png_002befe0._0_8_,6);
    cStack_68 = SUB81(s_img101_png_002befe0._0_8_,7);
    cStack_7a = '\0';
    local_87 = _DAT_002b91c5;
    uStack_82._0_1_ = s_1_imgcut_002b91ca[0];
    uStack_82._1_1_ = s_1_imgcut_002b91ca[1];
    uStack_82._2_1_ = s_1_imgcut_002b91ca[2];
    uStack_7f._0_1_ = s_1_imgcut_002b91ca[3];
    uStack_7f._1_1_ = s_1_imgcut_002b91ca[4];
    uStack_7f._2_1_ = s_1_imgcut_002b91ca[5];
    uStack_7f._3_1_ = s_1_imgcut_002b91ca[6];
    uStack_7f._4_1_ = s_1_imgcut_002b91ca[7];
    FUN_0047e60c(&local_c0,&DAT_00ca4f00,&local_70,&local_88,0x2601);
  }
  uVar5 = CONCAT71(uStack_b7,cStack_b8);
  uVar4 = CONCAT71(uStack_bf,local_c0);
  plVar11 = (long *)param_1[0x7b];
  local_c0 = 0;
  uStack_bf = 0;
  cStack_b8 = 0;
  uStack_b7 = 0;
  param_1[0x7b] = uVar5;
  param_1[0x7a] = uVar4;
  if ((plVar11 != (long *)0x0) && (lVar7 = FUN_00c53d00(0xffffffffffffffff,plVar11 + 1), lVar7 == 0)
     ) {
    (**(code **)(*plVar11 + 0x10))(plVar11);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar11);
  }
  plVar11 = (long *)CONCAT71(uStack_b7,cStack_b8);
  if ((plVar11 != (long *)0x0) && (lVar7 = FUN_00c53d00(0xffffffffffffffff,plVar11 + 1), lVar7 == 0)
     ) {
    (**(code **)(*plVar11 + 0x10))(plVar11);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar11);
  }
  if ((local_88 & 1) != 0) {
    _ZdlPv((void *)CONCAT17(uStack_71,CONCAT43(uStack_75,CONCAT21(uStack_77,cStack_78))));
  }
  if ((local_70 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_5c,local_60));
  }
LAB_00a6d5dc:
  if (((DAT_00ca4f38 & 1) == 0) && (iVar6 = __cxa_guard_acquire(&DAT_00ca4f38), iVar6 != 0)) {
    DAT_00ca4f08 = 0;
    DAT_00ca4f00 = &DAT_00ca4f08;
    DAT_00ca4f28 = 0;
    DAT_00ca4f30 = 0;
    DAT_00ca4f20 = 0;
    DAT_00ca4f10 = 0;
    DAT_00ca4f18 = &DAT_00ca4f20;
    __cxa_atexit(FUN_0047edb4,&DAT_00ca4f00,&PTR_LOOP_00c62f90);
    __cxa_guard_release(&DAT_00ca4f38);
  }
  local_c0 = 0x20;
  uStack_af = 0;
  uStack_b7 = (undefined7)s__03d_stamp_f_png_002b239e._8_8_;
  local_b0 = SUB81(s__03d_stamp_f_png_002b239e._8_8_,7);
  uStack_bf = (undefined7)s__03d_stamp_f_png_002b239e._0_8_;
  cStack_b8 = SUB81(s__03d_stamp_f_png_002b239e._0_8_,7);
  FUN_00447ef4(&local_88,&local_c0,0,0);
  FUN_0048ce54(&local_70,&local_88);
  local_108 = 0x26;
  uStack_ff = (undefined7)s__03d_stamp_f_imgcut_002addc4._8_8_;
  uStack_f8 = CONCAT31(0x747563,SUB81(s__03d_stamp_f_imgcut_002addc4._8_8_,7));
  local_107[0] = s__03d_stamp_f_imgcut_002addc4[0];
  local_107[1] = s__03d_stamp_f_imgcut_002addc4[1];
  local_107[2] = s__03d_stamp_f_imgcut_002addc4[2];
  local_107[3] = s__03d_stamp_f_imgcut_002addc4[3];
  local_107[4] = s__03d_stamp_f_imgcut_002addc4[4];
  local_107[5] = s__03d_stamp_f_imgcut_002addc4[5];
  local_107[6] = s__03d_stamp_f_imgcut_002addc4[6];
  local_107[7] = s__03d_stamp_f_imgcut_002addc4[7];
  uStack_f4 = uStack_f4 & 0xffffff00;
  FUN_00447ef4(local_f0,&local_108,0,0);
  FUN_0048ce54(local_d8,local_f0);
  FUN_0047e60c(&local_a0,&DAT_00ca4f00,&local_70,local_d8,0x2601);
  plVar11 = plStack_98;
  uVar4 = local_a0;
  plVar10 = (long *)param_1[0x83];
  local_a0 = 0;
  plStack_98 = (long *)0x0;
  param_1[0x83] = plVar11;
  param_1[0x82] = uVar4;
  if ((plVar10 != (long *)0x0) && (lVar7 = FUN_00c53d00(0xffffffffffffffff,plVar10 + 1), lVar7 == 0)
     ) {
    (**(code **)(*plVar10 + 0x10))(plVar10);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar10);
  }
  plVar11 = plStack_98;
  if ((plStack_98 != (long *)0x0) &&
     (lVar7 = FUN_00c53d00(0xffffffffffffffff,plStack_98 + 1), lVar7 == 0)) {
    (**(code **)(*plVar11 + 0x10))(plVar11);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar11);
  }
  if ((local_d8[0] & 1) != 0) {
    _ZdlPv(local_c8);
  }
  if ((local_f0[0] & 1) != 0) {
    _ZdlPv(local_e0);
  }
  if ((local_108 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_f4,uStack_f8));
  }
  if ((local_70 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_5c,local_60));
  }
  if ((local_88 & 1) != 0) {
    _ZdlPv((void *)CONCAT17(uStack_71,CONCAT43(uStack_75,CONCAT21(uStack_77,cStack_78))));
  }
  if ((local_c0 & 1) != 0) {
    _ZdlPv((void *)CONCAT62(uStack_ae,CONCAT11(uStack_af,local_b0)));
  }
  if (((DAT_00ca4f38 & 1) == 0) && (iVar6 = __cxa_guard_acquire(&DAT_00ca4f38), iVar6 != 0)) {
    DAT_00ca4f08 = 0;
                    /* try { // try from 00a6daac to 00b6dabb has its CatchHandler @ 00a77d78 */
    DAT_00ca4f00 = &DAT_00ca4f08;
                    /* try { // try from 00a6dabc to 00b6de1b has its CatchHandler @ 00a63fd8 */
    DAT_00ca4f28 = 0;
    DAT_00ca4f30 = 0;
    DAT_00ca4f20 = 0;
    DAT_00ca4f10 = 0;
    DAT_00ca4f18 = &DAT_00ca4f20;
    __cxa_atexit(FUN_0047edb4,&DAT_00ca4f00,&PTR_LOOP_00c62f90);
    __cxa_guard_release(&DAT_00ca4f38);
  }
  local_70 = 0x1c;
  cStack_61 = 0;
  uStack_6f = _DAT_002aeb52;
  cStack_69 = (char)s_g044_png_002aeb58._0_2_;
  cStack_68 = SUB21(s_g044_png_002aeb58._0_2_,1);
  uStack_67 = (undefined2)s_g044_png_002aeb58._2_6_;
  uStack_65 = SUB64(s_g044_png_002aeb58._2_6_,2);
  local_88 = 0x22;
  uStack_7f = (undefined5)s_001_img044_imgcut_002b8434._8_8_;
  cStack_7a = SUB81(s_001_img044_imgcut_002b8434._8_8_,5);
  cStack_79 = SUB81(s_001_img044_imgcut_002b8434._8_8_,6);
  cStack_78 = SUB81(s_001_img044_imgcut_002b8434._8_8_,7);
  local_87 = (undefined5)s_001_img044_imgcut_002b8434._0_8_;
  uStack_82 = SUB83(s_001_img044_imgcut_002b8434._0_8_,5);
  uStack_77 = 0x74;
  FUN_0047e60c(&local_c0,&DAT_00ca4f00,&local_70,&local_88,0x2601);
  uVar5 = CONCAT71(uStack_b7,cStack_b8);
  uVar4 = CONCAT71(uStack_bf,local_c0);
  plVar11 = (long *)param_1[0x85];
  local_c0 = 0;
  uStack_bf = 0;
  cStack_b8 = 0;
  uStack_b7 = 0;
  param_1[0x85] = uVar5;
  param_1[0x84] = uVar4;
  if ((plVar11 != (long *)0x0) && (lVar7 = FUN_00c53d00(0xffffffffffffffff,plVar11 + 1), lVar7 == 0)
     ) {
    (**(code **)(*plVar11 + 0x10))(plVar11);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar11);
  }
  plVar11 = (long *)CONCAT71(uStack_b7,cStack_b8);
  if ((plVar11 != (long *)0x0) && (lVar7 = FUN_00c53d00(0xffffffffffffffff,plVar11 + 1), lVar7 == 0)
     ) {
    (**(code **)(*plVar11 + 0x10))(plVar11);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar11);
  }
  if ((local_88 & 1) != 0) {
    _ZdlPv((void *)CONCAT17(uStack_71,CONCAT43(uStack_75,CONCAT21(uStack_77,cStack_78))));
  }
  if ((local_70 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_5c,local_60));
  }
  if (*(long *)(lVar3 + 0x28) != local_58) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~
