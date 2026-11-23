# 00ace4cc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 要確認
  - [v15.7.2 → v15.7.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/review-0021.md#review-e9da6e72e80d08f404463e5311ea59ee)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ace4cc",
  "name": "FUN_00ace4cc",
  "size": 3188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "199941e5079325a6c1b009b88db1ee40f3d70250cf16cad96c8e0a0156a8a962",
  "source_text_sha256": "199941e5079325a6c1b009b88db1ee40f3d70250cf16cad96c8e0a0156a8a962",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ace4cc",
        "00acf13b"
      ],
      [
        "00acf35c",
        "00acf35f"
      ]
    ],
    "bytes_sha256": "5129f2a73bfb0adbd816b32c73c0bfee64a1882f92a43e949dd5f817326be0ff",
    "instruction_count": 797,
    "instruction_bytes": 3188,
    "body_bytes": 3188,
    "indirect": 6,
    "unresolved": 6
  }
}
~~~

## 呼び出し元

- [008d99b0](../008d9/008d99b0.md)
- [0092e43c](../0092e/0092e43c.md)
- [00932074](../00932/00932074.md)
- [0093249c](../00932/0093249c.md)
- [00934148](../00934/00934148.md)
- [00934fe8](../00934/00934fe8.md)
- [00935ba4](../00935/00935ba4.md)
- [00938cc0](../00938/00938cc0.md)
- [0093f290](../0093f/0093f290.md)
- [0093f2dc](../0093f/0093f2dc.md)
- [00a6731c](../00a67/00a6731c.md)
- [00a68ac0](../00a68/00a68ac0.md)
- [00a69030](../00a69/00a69030.md)

## 呼び出し先

- [0041b298](../0041b/0041b298.md)
- [004253b4](../00425/004253b4.md)
- [0044b660](../0044b/0044b660.md)
- [0045b734](../0045b/0045b734.md)
- [00467d20](../00467/00467d20.md)
- [00469f7c](../00469/00469f7c.md)
- [0046ff30](../0046f/0046ff30.md)
- [005bdd1c](../005bd/005bdd1c.md)
- [005bdd9c](../005bd/005bdd9c.md)
- [0064104c](../00641/0064104c.md)
- [006f18c4](../006f1/006f18c4.md)
- [006f3104](../006f3/006f3104.md)
- [0081f580](../0081f/0081f580.md)
- [00830c98](../00830/00830c98.md)
- [008d5d88](../008d5/008d5d88.md)
- [008eccc4](../008ec/008eccc4.md)
- [00bd6d90](../00bd6/00bd6d90.md)
- [00bdaee0](../00bda/00bdaee0.md)
- [00bdaf00](../00bda/00bdaf00.md)
- [00bdaf20](../00bda/00bdaf20.md)
- [00bdaf30](../00bda/00bdaf30.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 関連文字列（未確認候補）

~~~text
"1.imgcut"
"2.imgcut"
"gatyaitemD_%02d_f.png"
"gatyaitem_%02d_f.png"
"gatyaitem_%02d_f_%@.png"
"img001.imgcut"
"img001.png"
"img050_01.imgcut"
"img050_01.png"
"img101.imgcut"
"img101.png"
"img101_nekoDojo.imgcut"
"img101_nekoDojo.png"
"img102.imgcut"
"img102.png"
"lang"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 19957 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */
/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00ace4cc(long param_1,uint param_2)

{
  ulong *puVar1;
  byte bVar2;
  byte bVar3;
  byte bVar4;
  byte bVar5;
  byte bVar6;
  byte bVar7;
  byte bVar8;
  byte bVar9;
  long lVar10;
  ulong uVar11;
  undefined4 uVar12;
  int iVar13;
  ulong uVar14;
  long lVar15;
  long lVar16;
  undefined8 uVar17;
  long *plVar18;
  long *plVar19;
  undefined8 uVar20;
  ulong local_100;
  long *plStack_f8;
  void *local_f0;
  byte local_e8 [16];
  void *local_d8;
  undefined1 auStack_d0 [16];
  ushort local_c0 [8];
  void *local_b0;
  byte local_a8 [16];
  void *local_98;
  ulong local_90;
  long *plStack_88;
  void *local_80;
  byte local_78;
  undefined5 local_77;
  char acStack_72 [3];
  char acStack_6f [5];
  char cStack_6a;
  char cStack_69;
  char cStack_68;
  char cStack_67;
  undefined5 uStack_66;
  undefined1 uStack_61;
  byte local_60;
  char acStack_5f [5];
  undefined2 uStack_5a;
  char cStack_58;
  undefined2 uStack_57;
  char cStack_55;
  undefined2 uStack_54;
  char cStack_52;
  char cStack_51;
  undefined4 uStack_50;
  uint uStack_4c;
  long local_48;
  
  lVar10 = tpidr_el0;
  local_48 = *(long *)(lVar10 + 0x28);
  puVar1 = (ulong *)(param_1 + 0x1a8 + (long)(int)param_2 * 0x10);
  if (((param_2 < 0x10) && (*puVar1 != 0)) && (uVar14 = FUN_00467d20(), (uVar14 & 1) != 0))
  goto LAB_00aceac0;
  if ((int)param_2 < 4) {
    if (param_2 == 0) {
      FUN_0081f580();
      FUN_00830c98(&local_60);
      uVar11 = CONCAT17(cStack_51,
                        CONCAT16(cStack_52,
                                 CONCAT24(uStack_54,
                                          CONCAT13(cStack_55,CONCAT21(uStack_57,cStack_58)))));
      uVar14 = CONCAT26(uStack_5a,CONCAT51(acStack_5f,local_60));
      plVar18 = (long *)puVar1[1];
      local_60 = 0;
      acStack_5f[0] = '\0';
      acStack_5f[1] = '\0';
      acStack_5f[2] = '\0';
      acStack_5f[3] = '\0';
      acStack_5f[4] = '\0';
      uStack_5a = 0;
      cStack_58 = '\0';
      uStack_57 = 0;
      cStack_55 = '\0';
      uStack_54 = 0;
      cStack_52 = '\0';
      cStack_51 = '\0';
      puVar1[1] = uVar11;
      *puVar1 = uVar14;
      if ((plVar18 != (long *)0x0) &&
         (lVar16 = FUN_00bd6d90(0xffffffffffffffff,plVar18 + 1), lVar16 == 0)) {
        (**(code **)(*plVar18 + 0x10))(plVar18);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar18);
      }
      plVar18 = (long *)CONCAT17(cStack_51,
                                 CONCAT16(cStack_52,
                                          CONCAT24(uStack_54,
                                                   CONCAT13(cStack_55,CONCAT21(uStack_57,cStack_58))
                                                  )));
      if ((plVar18 != (long *)0x0) &&
         (lVar16 = FUN_00bd6d90(0xffffffffffffffff,plVar18 + 1), lVar16 == 0)) {
        (**(code **)(*plVar18 + 0x10))(plVar18);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar18);
      }
      goto LAB_00aceac0;
    }
    if (param_2 == 2) {
      lVar16 = FUN_0081f580();
      iVar13 = *(int *)(BYTE_ARRAY_0032fef1 + lVar16 + 0x1b);
      FUN_0081f580();
      if ((iVar13 == 5) && (lVar16 = FUN_0081f580(), *(char *)(lVar16 + 0x32e9) != '\0')) {
        if (((DAT_00c24f78 & 1) == 0) && (iVar13 = __cxa_guard_acquire(&DAT_00c24f78), iVar13 != 0))
        {
          DAT_00c24f48 = 0;
          DAT_00c24f40 = &DAT_00c24f48;
          DAT_00c24f68 = 0;
          DAT_00c24f70 = 0;
          DAT_00c24f60 = 0;
          DAT_00c24f50 = 0;
          DAT_00c24f58 = &DAT_00c24f60;
          __cxa_atexit(FUN_0045bedc,&DAT_00c24f40,&PTR_LOOP_00be5ed0);
          __cxa_guard_release(&DAT_00c24f78);
        }
        local_60 = 0x26;
        uStack_4c = uStack_4c & 0xffffff00;
        local_78 = 0x2c;
        uStack_57 = (undefined2)s_img101_nekoDojo_png_002a4817._8_8_;
        cStack_55 = SUB81(s_img101_nekoDojo_png_002a4817._8_8_,2);
        uStack_54 = SUB82(s_img101_nekoDojo_png_002a4817._8_8_,3);
        cStack_52 = SUB81(s_img101_nekoDojo_png_002a4817._8_8_,5);
        cStack_51 = SUB81(s_img101_nekoDojo_png_002a4817._8_8_,6);
        uStack_50 = CONCAT31(0x676e70,SUB81(s_img101_nekoDojo_png_002a4817._8_8_,7));
        acStack_5f = SUB85(s_img101_nekoDojo_png_002a4817._0_8_,0);
        uStack_5a = SUB82(s_img101_nekoDojo_png_002a4817._0_8_,5);
        cStack_58 = SUB81(s_img101_nekoDojo_png_002a4817._0_8_,7);
        uStack_61 = 0;
        acStack_6f = SUB65(s_img101_nekoDojo_imgcut_002adceb._8_6_,0);
        cStack_6a = SUB61(s_img101_nekoDojo_imgcut_002adceb._8_6_,5);
        local_77 = (undefined5)s_img101_nekoDojo_imgcut_002adceb._0_8_;
        acStack_72 = SUB83(s_img101_nekoDojo_imgcut_002adceb._0_8_,5);
        cStack_69 = (char)s_img101_nekoDojo_imgcut_002adceb._14_2_;
        cStack_68 = SUB21(s_img101_nekoDojo_imgcut_002adceb._14_2_,1);
        cStack_67 = (char)s_img101_nekoDojo_imgcut_002adceb._16_6_;
        uStack_66 = SUB65(s_img101_nekoDojo_imgcut_002adceb._16_6_,1);
        FUN_0045b734(&local_90,&DAT_00c24f40,&local_60,&local_78,0x2601);
      }
      else {
        if (((DAT_00c24f78 & 1) == 0) && (iVar13 = __cxa_guard_acquire(&DAT_00c24f78), iVar13 != 0))
        {
          DAT_00c24f48 = 0;
          DAT_00c24f40 = &DAT_00c24f48;
          DAT_00c24f68 = 0;
          DAT_00c24f70 = 0;
          DAT_00c24f60 = 0;
          DAT_00c24f50 = 0;
          DAT_00c24f58 = &DAT_00c24f60;
          __cxa_atexit(FUN_0045bedc,&DAT_00c24f40,&PTR_LOOP_00be5ed0);
          __cxa_guard_release(&DAT_00c24f78);
        }
        cStack_55 = '\0';
        local_60 = 0x14;
        uStack_57 = 0x676e;
        local_78 = 0x1a;
        acStack_5f = SUB85(s_img101_png_002add02._0_8_,0);
        uStack_5a = SUB82(s_img101_png_002add02._0_8_,5);
        cStack_58 = SUB81(s_img101_png_002add02._0_8_,7);
        cStack_6a = '\0';
        local_77 = _DAT_002a84dd;
        acStack_72[0] = s_1_imgcut_002a84e2[0];
        acStack_72[1] = s_1_imgcut_002a84e2[1];
        acStack_72[2] = s_1_imgcut_002a84e2[2];
        acStack_6f[0] = s_1_imgcut_002a84e2[3];
        acStack_6f[1] = s_1_imgcut_002a84e2[4];
        acStack_6f[2] = s_1_imgcut_002a84e2[5];
        acStack_6f[3] = s_1_imgcut_002a84e2[6];
        acStack_6f[4] = s_1_imgcut_002a84e2[7];
        FUN_0045b734(&local_90,&DAT_00c24f40,&local_60,&local_78,0x2601);
      }
    }
    else {
      if (param_2 != 3) goto LAB_00aceac0;
      if (((DAT_00c24f78 & 1) == 0) && (iVar13 = __cxa_guard_acquire(&DAT_00c24f78), iVar13 != 0)) {
        DAT_00c24f48 = 0;
        DAT_00c24f40 = &DAT_00c24f48;
        DAT_00c24f68 = 0;
        DAT_00c24f70 = 0;
        DAT_00c24f60 = 0;
        DAT_00c24f50 = 0;
        DAT_00c24f58 = &DAT_00c24f60;
        __cxa_atexit(FUN_0045bedc,&DAT_00c24f40,&PTR_LOOP_00be5ed0);
        __cxa_guard_release(&DAT_00c24f78);
      }
      cStack_55 = '\0';
      local_60 = 0x14;
      uStack_57 = 0x676e;
      local_78 = 0x1a;
      acStack_5f = SUB85(s_img102_png_00294b68._0_8_,0);
      uStack_5a = SUB82(s_img102_png_00294b68._0_8_,5);
      cStack_58 = SUB81(s_img102_png_00294b68._0_8_,7);
      cStack_6a = '\0';
      local_77 = _DAT_002acb6e;
      acStack_72[0] = s_2_imgcut_002acb73[0];
      acStack_72[1] = s_2_imgcut_002acb73[1];
      acStack_72[2] = s_2_imgcut_002acb73[2];
      acStack_6f[0] = s_2_imgcut_002acb73[3];
      acStack_6f[1] = s_2_imgcut_002acb73[4];
      acStack_6f[2] = s_2_imgcut_002acb73[5];
      acStack_6f[3] = s_2_imgcut_002acb73[6];
      acStack_6f[4] = s_2_imgcut_002acb73[7];
      FUN_0045b734(&local_90,&DAT_00c24f40,&local_60,&local_78,0x2601);
    }
LAB_00acea34:
    plVar18 = plStack_88;
    uVar14 = local_90;
    plVar19 = (long *)puVar1[1];
    local_90 = 0;
    plStack_88 = (long *)0x0;
    puVar1[1] = (ulong)plVar18;
    *puVar1 = uVar14;
    if ((plVar19 != (long *)0x0) &&
       (lVar16 = FUN_00bd6d90(0xffffffffffffffff,plVar19 + 1), lVar16 == 0)) {
      (**(code **)(*plVar19 + 0x10))(plVar19);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar19);
    }
    plVar18 = plStack_88;
    if ((plStack_88 != (long *)0x0) &&
       (lVar16 = FUN_00bd6d90(0xffffffffffffffff,plStack_88 + 1), lVar16 == 0)) {
      (**(code **)(*plVar18 + 0x10))(plVar18);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar18);
    }
    if ((local_78 & 1) != 0) {
      _ZdlPv((void *)CONCAT17(uStack_61,CONCAT52(uStack_66,CONCAT11(cStack_67,cStack_68))));
    }
    if ((local_60 & 1) == 0) goto LAB_00aceac0;
    local_80 = (void *)CONCAT44(uStack_4c,uStack_50);
  }
  else {
    if (param_2 == 4) {
      if (((DAT_00c24f78 & 1) == 0) && (iVar13 = __cxa_guard_acquire(&DAT_00c24f78), iVar13 != 0)) {
        DAT_00c24f48 = 0;
        DAT_00c24f40 = &DAT_00c24f48;
        DAT_00c24f68 = 0;
        DAT_00c24f70 = 0;
        DAT_00c24f60 = 0;
        DAT_00c24f50 = 0;
        DAT_00c24f58 = &DAT_00c24f60;
        __cxa_atexit(FUN_0045bedc,&DAT_00c24f40,&PTR_LOOP_00be5ed0);
        __cxa_guard_release(&DAT_00c24f78);
      }
      cStack_55 = '\0';
      local_60 = 0x14;
      uStack_57 = 0x676e;
      local_78 = 0x1a;
      acStack_5f = SUB85(s_img001_png_002a081f._0_8_,0);
      uStack_5a = SUB82(s_img001_png_002a081f._0_8_,5);
      cStack_58 = SUB81(s_img001_png_002a081f._0_8_,7);
      cStack_6a = '\0';
      local_77 = (undefined5)DAT_0029b6af;
      acStack_72[0] = DAT_0029b6af._5_1_;
      acStack_72[1] = DAT_0029b6af._6_1_;
      acStack_72[2] = DAT_0029b6af._7_1_;
      acStack_6f[0] = UNK_0029b6b7;
      acStack_6f[1] = DAT_0029b6b8;
      acStack_6f[2] = UNK_0029b6b9;
      acStack_6f[3] = UNK_0029b6ba;
      acStack_6f[4] = UNK_0029b6bb;
      FUN_0045b734(&local_90,&DAT_00c24f40,&local_60,&local_78,0x2601);
      goto LAB_00acea34;
    }
    if (param_2 == 5) {
      if (((DAT_00c24f78 & 1) == 0) && (iVar13 = __cxa_guard_acquire(&DAT_00c24f78), iVar13 != 0)) {
        DAT_00c24f48 = 0;
        DAT_00c24f40 = &DAT_00c24f48;
        DAT_00c24f68 = 0;
        DAT_00c24f70 = 0;
        DAT_00c24f60 = 0;
        DAT_00c24f50 = 0;
        DAT_00c24f58 = &DAT_00c24f60;
        __cxa_atexit(FUN_0045bedc,&DAT_00c24f40,&PTR_LOOP_00be5ed0);
        __cxa_guard_release(&DAT_00c24f78);
      }
      local_60 = 0x1a;
      cStack_52 = '\0';
      acStack_5f[0] = s_img050_01_png_002aeec9[0];
      acStack_5f[1] = s_img050_01_png_002aeec9[1];
      acStack_5f[2] = s_img050_01_png_002aeec9[2];
      acStack_5f[3] = s_img050_01_png_002aeec9[3];
      acStack_5f[4] = s_img050_01_png_002aeec9[4];
      uStack_5a = (undefined2)s_img050_01_png_002aeec9._5_3_;
      cStack_58 = SUB31(s_img050_01_png_002aeec9._5_3_,2);
      uStack_57 = (undefined2)s_img050_01_png_002aeec9._8_5_;
      cStack_55 = SUB51(s_img050_01_png_002aeec9._8_5_,2);
      uStack_54 = SUB52(s_img050_01_png_002aeec9._8_5_,3);
      local_78 = 0x20;
      cStack_67 = '\0';
      acStack_6f = SUB85(s_img050_01_imgcut_002ade27._8_8_,0);
      cStack_6a = SUB81(s_img050_01_imgcut_002ade27._8_8_,5);
      cStack_69 = SUB81(s_img050_01_imgcut_002ade27._8_8_,6);
      cStack_68 = SUB81(s_img050_01_imgcut_002ade27._8_8_,7);
      local_77 = (undefined5)s_img050_01_imgcut_002ade27._0_8_;
      acStack_72 = SUB83(s_img050_01_imgcut_002ade27._0_8_,5);
      FUN_0045b734(&local_90,&DAT_00c24f40,&local_60,&local_78,0x2601);
      goto LAB_00acea34;
    }
    if ((param_2 != 6) || (lVar16 = FUN_0081f580(), BYTE_ARRAY_00331ea1[lVar16 + 9] == 0))
    goto LAB_00aceac0;
    lVar16 = FUN_0081f580();
    lVar15 = FUN_0081f580();
    lVar16 = lVar16 + (long)*(int *)((long)&DWORD_0033a22c + lVar15) * 8;
    if (((uint)(BYTE_ARRAY_00335e09[lVar16 + 0x1c] ^ BYTE_ARRAY_00335e09[lVar16 + 0x19]) << 0x10 |
         (uint)(BYTE_ARRAY_00335e09[lVar16 + 0x1b] ^ BYTE_ARRAY_00335e09[lVar16 + 0x1a]) << 0x18 |
         (uint)(BYTE_ARRAY_00335e09[lVar16 + 0x1d] ^ BYTE_ARRAY_00335e09[lVar16 + 0x18]) << 8 |
        (uint)(BYTE_ARRAY_00335e09[lVar16 + 0x1e] ^ BYTE_ARRAY_00335e09[lVar16 + 0x17])) == 1) {
      if (((DAT_00c24f78 & 1) == 0) && (iVar13 = __cxa_guard_acquire(&DAT_00c24f78), iVar13 != 0)) {
        DAT_00c24f48 = 0;
        DAT_00c24f40 = &DAT_00c24f48;
        DAT_00c24f68 = 0;
        DAT_00c24f70 = 0;
        DAT_00c24f60 = 0;
        DAT_00c24f50 = 0;
        DAT_00c24f58 = &DAT_00c24f60;
        __cxa_atexit(FUN_0045bedc,&DAT_00c24f40,&PTR_LOOP_00be5ed0);
        __cxa_guard_release(&DAT_00c24f78);
      }
      local_90 = 0x676e702e73250c;
      lVar16 = FUN_0081f580();
      lVar15 = FUN_0081f580();
      lVar16 = lVar16 + (long)*(int *)((long)&DWORD_0033a22c + lVar15) * 8;
      FUN_0064104c(local_a8,(uint)(BYTE_ARRAY_00335a05[lVar16 + 0x20] ^
                                  BYTE_ARRAY_00335a05[lVar16 + 0x1d]) << 0x10 |
                            (uint)(BYTE_ARRAY_00335a05[lVar16 + 0x1f] ^
                                  BYTE_ARRAY_00335a05[lVar16 + 0x1e]) << 0x18 |
                            (uint)(BYTE_ARRAY_00335a05[lVar16 + 0x21] ^
                                  BYTE_ARRAY_00335a05[lVar16 + 0x1c]) << 8 |
                            (uint)(BYTE_ARRAY_00335a05[lVar16 + 0x22] ^
                                  BYTE_ARRAY_00335a05[lVar16 + 0x1b]),0);
      FUN_0046ff30(&local_78,&local_90,local_a8);
      FUN_00469f7c(&local_60,&local_78);
      local_c0[0] = 0;
      FUN_0045b734(&local_100,&DAT_00c24f40,&local_60,local_c0,0x2601);
      plVar18 = plStack_f8;
      uVar14 = local_100;
      plVar19 = (long *)puVar1[1];
      local_100 = 0;
      plStack_f8 = (long *)0x0;
      puVar1[1] = (ulong)plVar18;
      *puVar1 = uVar14;
      if ((plVar19 != (long *)0x0) &&
         (lVar16 = FUN_00bd6d90(0xffffffffffffffff,plVar19 + 1), lVar16 == 0)) {
        (**(code **)(*plVar19 + 0x10))(plVar19);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar19);
      }
      plVar18 = plStack_f8;
      if ((plStack_f8 != (long *)0x0) &&
         (lVar16 = FUN_00bd6d90(0xffffffffffffffff,plStack_f8 + 1), lVar16 == 0)) {
        (**(code **)(*plVar18 + 0x10))(plVar18);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar18);
      }
      if ((local_c0[0] & 1) != 0) {
        _ZdlPv(local_b0);
      }
      if ((local_60 & 1) != 0) {
        _ZdlPv((void *)CONCAT44(uStack_4c,uStack_50));
      }
      local_b0 = local_98;
      if ((local_78 & 1) != 0) {
        _ZdlPv((void *)CONCAT17(uStack_61,CONCAT52(uStack_66,CONCAT11(cStack_67,cStack_68))));
        local_b0 = local_98;
      }
      if ((local_a8[0] & 1) != 0) goto LAB_00acee90;
    }
    else {
      lVar16 = FUN_0081f580();
      lVar15 = FUN_0081f580();
      lVar16 = lVar16 + (long)*(int *)((long)&DWORD_0033a22c + lVar15) * 8;
      bVar2 = BYTE_ARRAY_00335e09[lVar16 + 0x19];
      bVar3 = BYTE_ARRAY_00335e09[lVar16 + 0x1c];
      bVar4 = BYTE_ARRAY_00335e09[lVar16 + 0x1b];
      bVar5 = BYTE_ARRAY_00335e09[lVar16 + 0x18];
      bVar6 = BYTE_ARRAY_00335e09[lVar16 + 0x1a];
      bVar7 = BYTE_ARRAY_00335e09[lVar16 + 0x1d];
      bVar8 = BYTE_ARRAY_00335e09[lVar16 + 0x17];
      bVar9 = BYTE_ARRAY_00335e09[lVar16 + 0x1e];
      lVar16 = FUN_0081f580();
      lVar15 = FUN_0081f580();
      lVar16 = lVar16 + (long)*(int *)((long)&DWORD_0033a22c + lVar15) * 8;
      if (((uint)(bVar3 ^ bVar2) << 0x10 | (uint)(bVar4 ^ bVar6) << 0x18 |
           (uint)(bVar7 ^ bVar5) << 8 | (uint)(bVar9 ^ bVar8)) == 2) {
        iVar13 = FUN_006f18c4(lVar16 + 0x335a20);
        if (iVar13 != 0) {
          lVar16 = FUN_0081f580();
          lVar15 = FUN_0081f580();
          iVar13 = FUN_006f18c4(lVar16 + (long)*(int *)((long)&DWORD_0033a22c + lVar15) * 8 +
                                0x335a20);
          if (iVar13 != 2) {
            lVar16 = FUN_0081f580();
            lVar15 = FUN_0081f580();
            iVar13 = FUN_006f18c4(lVar16 + (long)*(int *)((long)&DWORD_0033a22c + lVar15) * 8 +
                                  0x335a20);
            if (iVar13 != 3) {
              lVar16 = FUN_0081f580();
              lVar15 = FUN_0081f580();
              iVar13 = FUN_006f18c4(lVar16 + (long)*(int *)((long)&DWORD_0033a22c + lVar15) * 8 +
                                    0x335a20);
              if (iVar13 != 4) {
                lVar16 = FUN_0081f580();
                lVar15 = FUN_0081f580();
                iVar13 = FUN_006f18c4(lVar16 + (long)*(int *)((long)&DWORD_0033a22c + lVar15) * 8 +
                                      0x335a20);
                if (iVar13 != 5) {
                  uVar17 = FUN_005bdd1c();
                  FUN_0041b298(&local_90,"gatyaitem_%02d_f.png");
                  lVar16 = FUN_0081f580();
                  lVar15 = FUN_0081f580();
                  FUN_008eccc4(&local_78,&local_90,0,
                               *(undefined8 *)
                                (BYTE_ARRAY_00335a05 +
                                lVar16 + (long)*(int *)((long)&DWORD_0033a22c + lVar15) * 8 + 0x1b))
                  ;
                  FUN_00469f7c(&local_60,&local_78);
                  FUN_0041b298(local_c0,&DAT_002967d9);
                  FUN_0045b734(&local_100,uVar17,&local_60,local_c0,0x2601);
                  goto LAB_00acedbc;
                }
              }
            }
          }
        }
        uVar17 = FUN_005bdd1c();
        FUN_0041b298(&local_90,"gatyaitem_%02d_f_%@.png");
        lVar16 = FUN_0081f580();
        lVar15 = FUN_0081f580();
        uVar20 = *(undefined8 *)
                  (BYTE_ARRAY_00335a05 +
                  lVar16 + (long)*(int *)((long)&DWORD_0033a22c + lVar15) * 8 + 0x1b);
        FUN_0041b298(local_c0,&DAT_00293a68);
        FUN_00469f7c(local_e8,local_c0);
        FUN_008d5d88(&local_78,&local_90,uVar20,local_e8);
        FUN_00469f7c(&local_60,&local_78);
        FUN_0041b298(&local_100,&DAT_002967d9);
        FUN_0045b734(auStack_d0,uVar17,&local_60,&local_100,0x2601);
        FUN_005bdd9c(puVar1,auStack_d0);
        FUN_0044b660(auStack_d0);
        if ((local_100 & 1) != 0) {
          _ZdlPv(local_f0);
        }
                    /* try { // try from 00acee30 to 00bcee3b has its CatchHandler @ 00ad0980 */
        if ((local_60 & 1) != 0) {
          _ZdlPv((void *)CONCAT44(uStack_4c,uStack_50));
                    /* try { // try from 00acee3c to 00bcfcf7 has its CatchHandler @ 00ace1d0 */
        }
        if ((local_78 & 1) != 0) {
          _ZdlPv((void *)CONCAT17(uStack_61,CONCAT52(uStack_66,CONCAT11(cStack_67,cStack_68))));
        }
        if ((local_e8[0] & 1) != 0) {
          _ZdlPv(local_d8);
        }
        if ((local_c0[0] & 1) != 0) {
LAB_00acee90:
          _ZdlPv(local_b0);
        }
      }
      else {
        iVar13 = FUN_006f18c4(lVar16 + 0x335e20);
        if (iVar13 != 3) goto LAB_00aceac0;
        uVar17 = FUN_005bdd1c();
        FUN_0041b298(&local_90,"gatyaitemD_%02d_f.png");
        lVar16 = FUN_0081f580();
        lVar15 = FUN_0081f580();
        FUN_006f18c4(lVar16 + (long)*(int *)((long)&DWORD_0033a22c + lVar15) * 8 + 0x335a20);
        uVar12 = FUN_006f3104();
        FUN_004253b4(&local_78,&local_90,0,uVar12);
        FUN_00469f7c(&local_60,&local_78);
        FUN_0041b298(local_c0,&DAT_002967d9);
        FUN_0045b734(&local_100,uVar17,&local_60,local_c0,0x2601);
LAB_00acedbc:
        FUN_005bdd9c(puVar1,&local_100);
        FUN_0044b660(&local_100);
        if ((local_c0[0] & 1) != 0) {
          _ZdlPv(local_b0);
        }
        if ((local_60 & 1) != 0) {
          _ZdlPv((void *)CONCAT44(uStack_4c,uStack_50));
        }
        if ((local_78 & 1) != 0) {
          local_b0 = (void *)CONCAT17(uStack_61,CONCAT52(uStack_66,CONCAT11(cStack_67,cStack_68)));
          goto LAB_00acee90;
        }
      }
    }
    if ((local_90 & 1) == 0) goto LAB_00aceac0;
  }
  _ZdlPv(local_80);
LAB_00aceac0:
  if (*(long *)(lVar10 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail(*puVar1);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ace4cc"></a> `00ace4cc` | `ff 03 04 d1` | sub sp,sp,#0x100 | `FALL_THROUGH`
<a id="insn-00ace4d0"></a> `00ace4d0` | `fd 7b 0c a9` | stp x29,x30,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00ace4d4"></a> `00ace4d4` | `f7 6b 00 f9` | str x23,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00ace4d8"></a> `00ace4d8` | `f6 57 0e a9` | stp x22,x21,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00ace4dc"></a> `00ace4dc` | `f4 4f 0f a9` | stp x20,x19,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00ace4e0"></a> `00ace4e0` | `fd 03 03 91` | add x29,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00ace4e4"></a> `00ace4e4` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00ace4e8"></a> `00ace4e8` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00ace4ec"></a> `00ace4ec` | `0a a0 06 91` | add x10,x0,#0x1a8 | `FALL_THROUGH`
<a id="insn-00ace4f0"></a> `00ace4f0` | `88 7e 40 93` | sxtw x8,w20 | `FALL_THROUGH`
<a id="insn-00ace4f4"></a> `00ace4f4` | `c9 16 40 f9` | ldr x9,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00ace4f8"></a> `00ace4f8` | `3f 3c 00 71` | cmp w1,#0xf | `FALL_THROUGH`
<a id="insn-00ace4fc"></a> `00ace4fc` | `53 11 08 8b` | add x19,x10,x8, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00ace500"></a> `00ace500` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ace504"></a> `00ace504` | `a8 00 00 54` | b.hi 0x00ace518 | `CONDITIONAL_JUMP`
<a id="insn-00ace508"></a> `00ace508` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00ace50c"></a> `00ace50c` | `60 00 00 b4` | cbz x0,0x00ace518 | `CONDITIONAL_JUMP`
<a id="insn-00ace510"></a> `00ace510` | `04 66 e6 97` | bl 0x00467d20 | `UNCONDITIONAL_CALL`
<a id="insn-00ace514"></a> `00ace514` | `60 2d 00 37` | tbnz w0,#0x0,0x00aceac0 | `CONDITIONAL_JUMP`
<a id="insn-00ace518"></a> `00ace518` | `9f 0e 00 71` | cmp w20,#0x3 | `FALL_THROUGH`
<a id="insn-00ace51c"></a> `00ace51c` | `b5 e3 00 d1` | sub x21,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00ace520"></a> `00ace520` | `8c 04 00 54` | b.gt 0x00ace5b0 | `CONDITIONAL_JUMP`
<a id="insn-00ace524"></a> `00ace524` | `94 14 00 34` | cbz w20,0x00ace7b4 | `CONDITIONAL_JUMP`
<a id="insn-00ace528"></a> `00ace528` | `9f 0a 00 71` | cmp w20,#0x2 | `FALL_THROUGH`
<a id="insn-00ace52c"></a> `00ace52c` | `e0 1b 00 54` | b.eq 0x00ace8a8 | `CONDITIONAL_JUMP`
<a id="insn-00ace530"></a> `00ace530` | `9f 0e 00 71` | cmp w20,#0x3 | `FALL_THROUGH`
<a id="insn-00ace534"></a> `00ace534` | `61 2c 00 54` | b.ne 0x00aceac0 | `CONDITIONAL_JUMP`
<a id="insn-00ace538"></a> `00ace538` | `a8 0a 00 d0` | adrp x8,0xc24000 | `FALL_THROUGH`
<a id="insn-00ace53c"></a> `00ace53c` | `08 e1 3d 91` | add x8,x8,#0xf78 | `FALL_THROUGH`
<a id="insn-00ace540"></a> `00ace540` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00ace544"></a> `00ace544` | `08 52 00 36` | tbz w8,#0x0,0x00acef84 | `CONDITIONAL_JUMP`
<a id="insn-00ace548"></a> `00ace548` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-00ace54c"></a> `00ace54c` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-00ace550"></a> `00ace550` | `bf b3 1e 38` | sturb wzr,[x29, #-0x15] | `FALL_THROUGH`
<a id="insn-00ace554"></a> `00ace554` | `a8 03 1e 38` | sturb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00ace558"></a> `00ace558` | `28 be ff d0` | adrp x8,0x294000 | `FALL_THROUGH`
<a id="insn-00ace55c"></a> `00ace55c` | `08 a1 2d 91` | add x8,x8,#0xb68 | `FALL_THROUGH`
<a id="insn-00ace560"></a> `00ace560` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ace564"></a> `00ace564` | `a9 12 02 78` | sturh w9,[x21, #0x21] | `FALL_THROUGH`
<a id="insn-00ace568"></a> `00ace568` | `49 03 80 52` | mov w9,#0x1a | `FALL_THROUGH`
<a id="insn-00ace56c"></a> `00ace56c` | `a9 83 1c 38` | sturb w9,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00ace570"></a> `00ace570` | `a8 92 01 f8` | stur x8,[x21, #0x19] | `FALL_THROUGH`
<a id="insn-00ace574"></a> `00ace574` | `e8 be ff d0` | adrp x8,0x2ac000 | `FALL_THROUGH`
<a id="insn-00ace578"></a> `00ace578` | `08 b9 2d 91` | add x8,x8,#0xb6e | `FALL_THROUGH`
<a id="insn-00ace57c"></a> `00ace57c` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00ace580"></a> `00ace580` | `08 51 40 f8` | ldur x8,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-00ace584"></a> `00ace584` | `bf 63 1d 38` | sturb wzr,[x29, #-0x2a] | `FALL_THROUGH`
<a id="insn-00ace588"></a> `00ace588` | `a9 12 00 f8` | stur x9,[x21, #0x1] | `FALL_THROUGH`
<a id="insn-00ace58c"></a> `00ace58c` | `a8 62 00 f8` | stur x8,[x21, #0x6] | `FALL_THROUGH`
<a id="insn-00ace590"></a> `00ace590` | `a0 0a 00 d0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00ace594"></a> `00ace594` | `00 00 3d 91` | add x0,x0,#0xf40 | `FALL_THROUGH`
<a id="insn-00ace598"></a> `00ace598` | `a8 43 01 d1` | sub x8,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00ace59c"></a> `00ace59c` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00ace5a0"></a> `00ace5a0` | `a2 e3 00 d1` | sub x2,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00ace5a4"></a> `00ace5a4` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-00ace5a8"></a> `00ace5a8` | `63 34 e6 97` | bl 0x0045b734 | `UNCONDITIONAL_CALL`
<a id="insn-00ace5ac"></a> `00ace5ac` | `22 01 00 14` | b 0x00acea34 | `UNCONDITIONAL_JUMP`
<a id="insn-00ace5b0"></a> `00ace5b0` | `9f 12 00 71` | cmp w20,#0x4 | `FALL_THROUGH`
<a id="insn-00ace5b4"></a> `00ace5b4` | `e0 13 00 54` | b.eq 0x00ace830 | `CONDITIONAL_JUMP`
<a id="insn-00ace5b8"></a> `00ace5b8` | `9f 16 00 71` | cmp w20,#0x5 | `FALL_THROUGH`
<a id="insn-00ace5bc"></a> `00ace5bc` | `a0 1c 00 54` | b.eq 0x00ace950 | `CONDITIONAL_JUMP`
<a id="insn-00ace5c0"></a> `00ace5c0` | `9f 1a 00 71` | cmp w20,#0x6 | `FALL_THROUGH`
<a id="insn-00ace5c4"></a> `00ace5c4` | `e1 27 00 54` | b.ne 0x00aceac0 | `CONDITIONAL_JUMP`
<a id="insn-00ace5c8"></a> `00ace5c8` | `ee 43 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ace5cc"></a> `00ace5cc` | `48 d5 83 52` | mov w8,#0x1eaa | `FALL_THROUGH`
<a id="insn-00ace5d0"></a> `00ace5d0` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ace5d4"></a> `00ace5d4` | `08 68 68 38` | ldrb w8,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00ace5d8"></a> `00ace5d8` | `48 27 00 34` | cbz w8,0x00aceac0 | `CONDITIONAL_JUMP`
<a id="insn-00ace5dc"></a> `00ace5dc` | `e9 43 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ace5e0"></a> `00ace5e0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00ace5e4"></a> `00ace5e4` | `e7 43 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ace5e8"></a> `00ace5e8` | `88 45 94 52` | mov w8,#0xa22c | `FALL_THROUGH`
<a id="insn-00ace5ec"></a> `00ace5ec` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ace5f0"></a> `00ace5f0` | `08 68 a8 b8` | ldrsw x8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ace5f4"></a> `00ace5f4` | `88 0e 08 8b` | add x8,x20,x8, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00ace5f8"></a> `00ace5f8` | `08 d5 4c 91` | add x8,x8,#0x335, LSL #12 | `FALL_THROUGH`
<a id="insn-00ace5fc"></a> `00ace5fc` | `08 81 38 91` | add x8,x8,#0xe20 | `FALL_THROUGH`
<a id="insn-00ace600"></a> `00ace600` | `09 09 40 39` | ldrb w9,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00ace604"></a> `00ace604` | `0a 15 40 39` | ldrb w10,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-00ace608"></a> `00ace608` | `0b 11 40 39` | ldrb w11,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00ace60c"></a> `00ace60c` | `0c 05 40 39` | ldrb w12,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00ace610"></a> `00ace610` | `49 01 09 4a` | eor w9,w10,w9 | `FALL_THROUGH`
<a id="insn-00ace614"></a> `00ace614` | `0a 0d 40 39` | ldrb w10,[x8, #0x3] | `FALL_THROUGH`
<a id="insn-00ace618"></a> `00ace618` | `29 3d 10 53` | lsl w9,w9,#0x10 | `FALL_THROUGH`
<a id="insn-00ace61c"></a> `00ace61c` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00ace620"></a> `00ace620` | `0b 19 40 39` | ldrb w11,[x8, #0x6] | `FALL_THROUGH`
<a id="insn-00ace624"></a> `00ace624` | `29 61 0a 2a` | orr w9,w9,w10, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00ace628"></a> `00ace628` | `0a 01 40 39` | ldrb w10,[x8] | `FALL_THROUGH`
<a id="insn-00ace62c"></a> `00ace62c` | `08 1d 40 39` | ldrb w8,[x8, #0x7] | `FALL_THROUGH`
<a id="insn-00ace630"></a> `00ace630` | `6b 01 0c 4a` | eor w11,w11,w12 | `FALL_THROUGH`
<a id="insn-00ace634"></a> `00ace634` | `29 21 0b 2a` | orr w9,w9,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00ace638"></a> `00ace638` | `08 01 0a 4a` | eor w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00ace63c"></a> `00ace63c` | `28 01 08 2a` | orr w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00ace640"></a> `00ace640` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ace644"></a> `00ace644` | `41 25 00 54` | b.ne 0x00aceaec | `CONDITIONAL_JUMP`
<a id="insn-00ace648"></a> `00ace648` | `a8 0a 00 d0` | adrp x8,0xc24000 | `FALL_THROUGH`
<a id="insn-00ace64c"></a> `00ace64c` | `08 e1 3d 91` | add x8,x8,#0xf78 | `FALL_THROUGH`
<a id="insn-00ace650"></a> `00ace650` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00ace654"></a> `00ace654` | `c8 51 00 36` | tbz w8,#0x0,0x00acf08c | `CONDITIONAL_JUMP`
<a id="insn-00ace658"></a> `00ace658` | `88 01 80 52` | mov w8,#0xc | `FALL_THROUGH`
<a id="insn-00ace65c"></a> `00ace65c` | `a9 64 8e 52` | mov w9,#0x7325 | `FALL_THROUGH`
<a id="insn-00ace660"></a> `00ace660` | `bf 73 1b 38` | sturb wzr,[x29, #-0x49] | `FALL_THROUGH`
<a id="insn-00ace664"></a> `00ace664` | `c9 05 ae 72` | movk w9,#0x702e, LSL #16 | `FALL_THROUGH`
<a id="insn-00ace668"></a> `00ace668` | `a8 03 1b 38` | sturb w8,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00ace66c"></a> `00ace66c` | `c8 ed 8c 52` | mov w8,#0x676e | `FALL_THROUGH`
<a id="insn-00ace670"></a> `00ace670` | `a9 13 1b b8` | stur w9,[x29, #-0x4f] | `FALL_THROUGH`
<a id="insn-00ace674"></a> `00ace674` | `a8 53 1b 78` | sturh w8,[x29, #-0x4b] | `FALL_THROUGH`
<a id="insn-00ace678"></a> `00ace678` | `c2 43 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ace67c"></a> `00ace67c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00ace680"></a> `00ace680` | `c0 43 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ace684"></a> `00ace684` | `88 45 94 52` | mov w8,#0xa22c | `FALL_THROUGH`
<a id="insn-00ace688"></a> `00ace688` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ace68c"></a> `00ace68c` | `08 68 a8 b8` | ldrsw x8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ace690"></a> `00ace690` | `88 0e 08 8b` | add x8,x20,x8, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00ace694"></a> `00ace694` | `08 d5 4c 91` | add x8,x8,#0x335, LSL #12 | `FALL_THROUGH`
<a id="insn-00ace698"></a> `00ace698` | `08 81 28 91` | add x8,x8,#0xa20 | `FALL_THROUGH`
<a id="insn-00ace69c"></a> `00ace69c` | `09 09 40 39` | ldrb w9,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00ace6a0"></a> `00ace6a0` | `0a 15 40 39` | ldrb w10,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-00ace6a4"></a> `00ace6a4` | `0b 11 40 39` | ldrb w11,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00ace6a8"></a> `00ace6a8` | `0c 05 40 39` | ldrb w12,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00ace6ac"></a> `00ace6ac` | `49 01 09 4a` | eor w9,w10,w9 | `FALL_THROUGH`
<a id="insn-00ace6b0"></a> `00ace6b0` | `0a 0d 40 39` | ldrb w10,[x8, #0x3] | `FALL_THROUGH`
<a id="insn-00ace6b4"></a> `00ace6b4` | `29 3d 10 53` | lsl w9,w9,#0x10 | `FALL_THROUGH`
<a id="insn-00ace6b8"></a> `00ace6b8` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00ace6bc"></a> `00ace6bc` | `0b 19 40 39` | ldrb w11,[x8, #0x6] | `FALL_THROUGH`
<a id="insn-00ace6c0"></a> `00ace6c0` | `29 61 0a 2a` | orr w9,w9,w10, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00ace6c4"></a> `00ace6c4` | `0a 01 40 39` | ldrb w10,[x8] | `FALL_THROUGH`
<a id="insn-00ace6c8"></a> `00ace6c8` | `08 1d 40 39` | ldrb w8,[x8, #0x7] | `FALL_THROUGH`
<a id="insn-00ace6cc"></a> `00ace6cc` | `6b 01 0c 4a` | eor w11,w11,w12 | `FALL_THROUGH`
<a id="insn-00ace6d0"></a> `00ace6d0` | `29 21 0b 2a` | orr w9,w9,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00ace6d4"></a> `00ace6d4` | `0a 01 0a 4a` | eor w10,w8,w10 | `FALL_THROUGH`
<a id="insn-00ace6d8"></a> `00ace6d8` | `e8 63 01 91` | add x8,sp,#0x58 | `FALL_THROUGH`
<a id="insn-00ace6dc"></a> `00ace6dc` | `20 01 0a 2a` | orr w0,w9,w10 | `FALL_THROUGH`
<a id="insn-00ace6e0"></a> `00ace6e0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00ace6e4"></a> `00ace6e4` | `5a ca ed 97` | bl 0x0064104c | `UNCONDITIONAL_CALL`
<a id="insn-00ace6e8"></a> `00ace6e8` | `a8 e3 00 d1` | sub x8,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00ace6ec"></a> `00ace6ec` | `a0 43 01 d1` | sub x0,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00ace6f0"></a> `00ace6f0` | `e1 63 01 91` | add x1,sp,#0x58 | `FALL_THROUGH`
<a id="insn-00ace6f4"></a> `00ace6f4` | `0f 86 e6 97` | bl 0x0046ff30 | `UNCONDITIONAL_CALL`
<a id="insn-00ace6f8"></a> `00ace6f8` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00ace6fc"></a> `00ace6fc` | `a0 e3 00 d1` | sub x0,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00ace700"></a> `00ace700` | `1f 6e e6 97` | bl 0x00469f7c | `UNCONDITIONAL_CALL`
<a id="insn-00ace704"></a> `00ace704` | `ff 83 00 79` | strh wzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ace708"></a> `00ace708` | `a0 0a 00 d0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00ace70c"></a> `00ace70c` | `00 00 3d 91` | add x0,x0,#0xf40 | `FALL_THROUGH`
<a id="insn-00ace710"></a> `00ace710` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00ace714"></a> `00ace714` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00ace718"></a> `00ace718` | `e2 03 01 91` | add x2,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00ace71c"></a> `00ace71c` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-00ace720"></a> `00ace720` | `05 34 e6 97` | bl 0x0045b734 | `UNCONDITIONAL_CALL`
<a id="insn-00ace724"></a> `00ace724` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00ace728"></a> `00ace728` | `74 06 40 f9` | ldr x20,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00ace72c"></a> `00ace72c` | `ff 7f 00 a9` | stp xzr,xzr,[sp] | `FALL_THROUGH`
<a id="insn-00ace730"></a> `00ace730` | `60 02 80 3d` | str q0,[x19] | `FALL_THROUGH`
<a id="insn-00ace734"></a> `00ace734` | `74 01 00 b4` | cbz x20,0x00ace760 | `CONDITIONAL_JUMP`
<a id="insn-00ace738"></a> `00ace738` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00ace73c"></a> `00ace73c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ace740"></a> `00ace740` | `94 21 04 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00ace744"></a> `00ace744` | `e0 00 00 b5` | cbnz x0,0x00ace760 | `CONDITIONAL_JUMP`
<a id="insn-00ace748"></a> `00ace748` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00ace74c"></a> `00ace74c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ace750"></a> `00ace750` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ace754"></a> `00ace754` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ace758"></a> `00ace758` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ace75c"></a> `00ace75c` | `f5 31 04 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00ace760"></a> `00ace760` | `f4 07 40 f9` | ldr x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ace764"></a> `00ace764` | `74 01 00 b4` | cbz x20,0x00ace790 | `CONDITIONAL_JUMP`
<a id="insn-00ace768"></a> `00ace768` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00ace76c"></a> `00ace76c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ace770"></a> `00ace770` | `88 21 04 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00ace774"></a> `00ace774` | `e0 00 00 b5` | cbnz x0,0x00ace790 | `CONDITIONAL_JUMP`
<a id="insn-00ace778"></a> `00ace778` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00ace77c"></a> `00ace77c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ace780"></a> `00ace780` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ace784"></a> `00ace784` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ace788"></a> `00ace788` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ace78c"></a> `00ace78c` | `e9 31 04 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00ace790"></a> `00ace790` | `e8 03 41 39` | ldrb w8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ace794"></a> `00ace794` | `c8 32 00 37` | tbnz w8,#0x0,0x00acedec | `CONDITIONAL_JUMP`
<a id="insn-00ace798"></a> `00ace798` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00ace79c"></a> `00ace79c` | `08 33 00 37` | tbnz w8,#0x0,0x00acedfc | `CONDITIONAL_JUMP`
<a id="insn-00ace7a0"></a> `00ace7a0` | `a8 83 5c 38` | ldurb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00ace7a4"></a> `00ace7a4` | `48 33 00 37` | tbnz w8,#0x0,0x00acee0c | `CONDITIONAL_JUMP`
<a id="insn-00ace7a8"></a> `00ace7a8` | `e8 63 41 39` | ldrb w8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00ace7ac"></a> `00ace7ac` | `88 33 00 37` | tbnz w8,#0x0,0x00acee1c | `CONDITIONAL_JUMP`
<a id="insn-00ace7b0"></a> `00ace7b0` | `b9 01 00 14` | b 0x00acee94 | `UNCONDITIONAL_JUMP`
<a id="insn-00ace7b4"></a> `00ace7b4` | `73 43 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ace7b8"></a> `00ace7b8` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00ace7bc"></a> `00ace7bc` | `37 89 f5 97` | bl 0x00830c98 | `UNCONDITIONAL_CALL`
<a id="insn-00ace7c0"></a> `00ace7c0` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00ace7c4"></a> `00ace7c4` | `74 06 40 f9` | ldr x20,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00ace7c8"></a> `00ace7c8` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00ace7cc"></a> `00ace7cc` | `60 02 80 3d` | str q0,[x19] | `FALL_THROUGH`
<a id="insn-00ace7d0"></a> `00ace7d0` | `74 01 00 b4` | cbz x20,0x00ace7fc | `CONDITIONAL_JUMP`
<a id="insn-00ace7d4"></a> `00ace7d4` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00ace7d8"></a> `00ace7d8` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ace7dc"></a> `00ace7dc` | `6d 21 04 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00ace7e0"></a> `00ace7e0` | `e0 00 00 b5` | cbnz x0,0x00ace7fc | `CONDITIONAL_JUMP`
<a id="insn-00ace7e4"></a> `00ace7e4` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00ace7e8"></a> `00ace7e8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ace7ec"></a> `00ace7ec` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ace7f0"></a> `00ace7f0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ace7f4"></a> `00ace7f4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ace7f8"></a> `00ace7f8` | `ce 31 04 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00ace7fc"></a> `00ace7fc` | `b4 83 5e f8` | ldur x20,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00ace800"></a> `00ace800` | `14 16 00 b4` | cbz x20,0x00aceac0 | `CONDITIONAL_JUMP`
<a id="insn-00ace804"></a> `00ace804` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00ace808"></a> `00ace808` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ace80c"></a> `00ace80c` | `61 21 04 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00ace810"></a> `00ace810` | `80 15 00 b5` | cbnz x0,0x00aceac0 | `CONDITIONAL_JUMP`
<a id="insn-00ace814"></a> `00ace814` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00ace818"></a> `00ace818` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ace81c"></a> `00ace81c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ace820"></a> `00ace820` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ace824"></a> `00ace824` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ace828"></a> `00ace828` | `c2 31 04 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00ace82c"></a> `00ace82c` | `a5 00 00 14` | b 0x00aceac0 | `UNCONDITIONAL_JUMP`
<a id="insn-00ace830"></a> `00ace830` | `a8 0a 00 d0` | adrp x8,0xc24000 | `FALL_THROUGH`
<a id="insn-00ace834"></a> `00ace834` | `08 e1 3d 91` | add x8,x8,#0xf78 | `FALL_THROUGH`
<a id="insn-00ace838"></a> `00ace838` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00ace83c"></a> `00ace83c` | `88 37 00 36` | tbz w8,#0x0,0x00acef2c | `CONDITIONAL_JUMP`
<a id="insn-00ace840"></a> `00ace840` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-00ace844"></a> `00ace844` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-00ace848"></a> `00ace848` | `bf b3 1e 38` | sturb wzr,[x29, #-0x15] | `FALL_THROUGH`
<a id="insn-00ace84c"></a> `00ace84c` | `a8 03 1e 38` | sturb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00ace850"></a> `00ace850` | `88 be ff d0` | adrp x8,0x2a0000 | `FALL_THROUGH`
<a id="insn-00ace854"></a> `00ace854` | `08 7d 20 91` | add x8,x8,#0x81f | `FALL_THROUGH`
<a id="insn-00ace858"></a> `00ace858` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ace85c"></a> `00ace85c` | `a9 12 02 78` | sturh w9,[x21, #0x21] | `FALL_THROUGH`
<a id="insn-00ace860"></a> `00ace860` | `49 03 80 52` | mov w9,#0x1a | `FALL_THROUGH`
<a id="insn-00ace864"></a> `00ace864` | `a9 83 1c 38` | sturb w9,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00ace868"></a> `00ace868` | `a8 92 01 f8` | stur x8,[x21, #0x19] | `FALL_THROUGH`
<a id="insn-00ace86c"></a> `00ace86c` | `68 be ff b0` | adrp x8,0x29b000 | `FALL_THROUGH`
<a id="insn-00ace870"></a> `00ace870` | `08 bd 1a 91` | add x8,x8,#0x6af | `FALL_THROUGH`
<a id="insn-00ace874"></a> `00ace874` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00ace878"></a> `00ace878` | `08 51 40 f8` | ldur x8,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-00ace87c"></a> `00ace87c` | `bf 63 1d 38` | sturb wzr,[x29, #-0x2a] | `FALL_THROUGH`
<a id="insn-00ace880"></a> `00ace880` | `a9 12 00 f8` | stur x9,[x21, #0x1] | `FALL_THROUGH`
<a id="insn-00ace884"></a> `00ace884` | `a8 62 00 f8` | stur x8,[x21, #0x6] | `FALL_THROUGH`
<a id="insn-00ace888"></a> `00ace888` | `a0 0a 00 d0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00ace88c"></a> `00ace88c` | `00 00 3d 91` | add x0,x0,#0xf40 | `FALL_THROUGH`
<a id="insn-00ace890"></a> `00ace890` | `a8 43 01 d1` | sub x8,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00ace894"></a> `00ace894` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00ace898"></a> `00ace898` | `a2 e3 00 d1` | sub x2,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00ace89c"></a> `00ace89c` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-00ace8a0"></a> `00ace8a0` | `a5 33 e6 97` | bl 0x0045b734 | `UNCONDITIONAL_CALL`
<a id="insn-00ace8a4"></a> `00ace8a4` | `64 00 00 14` | b 0x00acea34 | `UNCONDITIONAL_JUMP`
<a id="insn-00ace8a8"></a> `00ace8a8` | `36 43 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ace8ac"></a> `00ace8ac` | `88 e1 9f 52` | mov w8,#0xff0c | `FALL_THROUGH`
<a id="insn-00ace8b0"></a> `00ace8b0` | `48 06 a0 72` | movk w8,#0x32, LSL #16 | `FALL_THROUGH`
<a id="insn-00ace8b4"></a> `00ace8b4` | `14 68 68 b8` | ldr w20,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ace8b8"></a> `00ace8b8` | `32 43 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ace8bc"></a> `00ace8bc` | `9f 16 00 71` | cmp w20,#0x5 | `FALL_THROUGH`
<a id="insn-00ace8c0"></a> `00ace8c0` | `01 08 00 54` | b.ne 0x00ace9c0 | `CONDITIONAL_JUMP`
<a id="insn-00ace8c4"></a> `00ace8c4` | `2f 43 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ace8c8"></a> `00ace8c8` | `28 5d 86 52` | mov w8,#0x32e9 | `FALL_THROUGH`
<a id="insn-00ace8cc"></a> `00ace8cc` | `08 68 68 38` | ldrb w8,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00ace8d0"></a> `00ace8d0` | `88 07 00 34` | cbz w8,0x00ace9c0 | `CONDITIONAL_JUMP`
<a id="insn-00ace8d4"></a> `00ace8d4` | `a8 0a 00 d0` | adrp x8,0xc24000 | `FALL_THROUGH`
<a id="insn-00ace8d8"></a> `00ace8d8` | `08 e1 3d 91` | add x8,x8,#0xf78 | `FALL_THROUGH`
<a id="insn-00ace8dc"></a> `00ace8dc` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00ace8e0"></a> `00ace8e0` | `28 40 00 36` | tbz w8,#0x0,0x00acf0e4 | `CONDITIONAL_JUMP`
<a id="insn-00ace8e4"></a> `00ace8e4` | `c8 04 80 52` | mov w8,#0x26 | `FALL_THROUGH`
<a id="insn-00ace8e8"></a> `00ace8e8` | `a9 be ff d0` | adrp x9,0x2a4000 | `FALL_THROUGH`
<a id="insn-00ace8ec"></a> `00ace8ec` | `29 5d 20 91` | add x9,x9,#0x817 | `FALL_THROUGH`
<a id="insn-00ace8f0"></a> `00ace8f0` | `a8 03 1e 38` | sturb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00ace8f4"></a> `00ace8f4` | `c8 05 8e 52` | mov w8,#0x702e | `FALL_THROUGH`
<a id="insn-00ace8f8"></a> `00ace8f8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00ace8fc"></a> `00ace8fc` | `c8 ed ac 72` | movk w8,#0x676e, LSL #16 | `FALL_THROUGH`
<a id="insn-00ace900"></a> `00ace900` | `bf 43 1f 38` | sturb wzr,[x29, #-0xc] | `FALL_THROUGH`
<a id="insn-00ace904"></a> `00ace904` | `a8 03 1f b8` | stur w8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00ace908"></a> `00ace908` | `88 05 80 52` | mov w8,#0x2c | `FALL_THROUGH`
<a id="insn-00ace90c"></a> `00ace90c` | `a8 83 1c 38` | sturb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00ace910"></a> `00ace910` | `e8 be ff f0` | adrp x8,0x2ad000 | `FALL_THROUGH`
<a id="insn-00ace914"></a> `00ace914` | `08 ad 33 91` | add x8,x8,#0xceb | `FALL_THROUGH`
<a id="insn-00ace918"></a> `00ace918` | `a0 92 81 3c` | stur q0,[x21, #0x19] | `FALL_THROUGH`
<a id="insn-00ace91c"></a> `00ace91c` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00ace920"></a> `00ace920` | `08 e1 40 f8` | ldur x8,[x8, #0xe] | `FALL_THROUGH`
<a id="insn-00ace924"></a> `00ace924` | `bf f3 1d 38` | sturb wzr,[x29, #-0x21] | `FALL_THROUGH`
<a id="insn-00ace928"></a> `00ace928` | `a0 12 80 3c` | stur q0,[x21, #0x1] | `FALL_THROUGH`
<a id="insn-00ace92c"></a> `00ace92c` | `a8 f2 00 f8` | stur x8,[x21, #0xf] | `FALL_THROUGH`
<a id="insn-00ace930"></a> `00ace930` | `a0 0a 00 d0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00ace934"></a> `00ace934` | `00 00 3d 91` | add x0,x0,#0xf40 | `FALL_THROUGH`
<a id="insn-00ace938"></a> `00ace938` | `a8 43 01 d1` | sub x8,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00ace93c"></a> `00ace93c` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00ace940"></a> `00ace940` | `a2 e3 00 d1` | sub x2,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00ace944"></a> `00ace944` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-00ace948"></a> `00ace948` | `7b 33 e6 97` | bl 0x0045b734 | `UNCONDITIONAL_CALL`
<a id="insn-00ace94c"></a> `00ace94c` | `3a 00 00 14` | b 0x00acea34 | `UNCONDITIONAL_JUMP`
<a id="insn-00ace950"></a> `00ace950` | `a8 0a 00 d0` | adrp x8,0xc24000 | `FALL_THROUGH`
<a id="insn-00ace954"></a> `00ace954` | `08 e1 3d 91` | add x8,x8,#0xf78 | `FALL_THROUGH`
<a id="insn-00ace958"></a> `00ace958` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00ace95c"></a> `00ace95c` | `08 34 00 36` | tbz w8,#0x0,0x00acefdc | `CONDITIONAL_JUMP`
<a id="insn-00ace960"></a> `00ace960` | `09 bf ff 90` | adrp x9,0x2ae000 | `FALL_THROUGH`
<a id="insn-00ace964"></a> `00ace964` | `29 25 3b 91` | add x9,x9,#0xec9 | `FALL_THROUGH`
<a id="insn-00ace968"></a> `00ace968` | `48 03 80 52` | mov w8,#0x1a | `FALL_THROUGH`
<a id="insn-00ace96c"></a> `00ace96c` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00ace970"></a> `00ace970` | `29 51 40 f8` | ldur x9,[x9, #0x5] | `FALL_THROUGH`
<a id="insn-00ace974"></a> `00ace974` | `a8 03 1e 38` | sturb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00ace978"></a> `00ace978` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00ace97c"></a> `00ace97c` | `bf e3 1e 38` | sturb wzr,[x29, #-0x12] | `FALL_THROUGH`
<a id="insn-00ace980"></a> `00ace980` | `aa 92 01 f8` | stur x10,[x21, #0x19] | `FALL_THROUGH`
<a id="insn-00ace984"></a> `00ace984` | `a9 e2 01 f8` | stur x9,[x21, #0x1e] | `FALL_THROUGH`
<a id="insn-00ace988"></a> `00ace988` | `e9 be ff f0` | adrp x9,0x2ad000 | `FALL_THROUGH`
<a id="insn-00ace98c"></a> `00ace98c` | `29 9d 38 91` | add x9,x9,#0xe27 | `FALL_THROUGH`
<a id="insn-00ace990"></a> `00ace990` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00ace994"></a> `00ace994` | `a8 83 1c 38` | sturb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00ace998"></a> `00ace998` | `bf 93 1d 38` | sturb wzr,[x29, #-0x27] | `FALL_THROUGH`
<a id="insn-00ace99c"></a> `00ace99c` | `a0 12 80 3c` | stur q0,[x21, #0x1] | `FALL_THROUGH`
<a id="insn-00ace9a0"></a> `00ace9a0` | `a0 0a 00 d0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00ace9a4"></a> `00ace9a4` | `00 00 3d 91` | add x0,x0,#0xf40 | `FALL_THROUGH`
<a id="insn-00ace9a8"></a> `00ace9a8` | `a8 43 01 d1` | sub x8,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00ace9ac"></a> `00ace9ac` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00ace9b0"></a> `00ace9b0` | `a2 e3 00 d1` | sub x2,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00ace9b4"></a> `00ace9b4` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-00ace9b8"></a> `00ace9b8` | `5f 33 e6 97` | bl 0x0045b734 | `UNCONDITIONAL_CALL`
<a id="insn-00ace9bc"></a> `00ace9bc` | `1e 00 00 14` | b 0x00acea34 | `UNCONDITIONAL_JUMP`
<a id="insn-00ace9c0"></a> `00ace9c0` | `a8 0a 00 d0` | adrp x8,0xc24000 | `FALL_THROUGH`
<a id="insn-00ace9c4"></a> `00ace9c4` | `08 e1 3d 91` | add x8,x8,#0xf78 | `FALL_THROUGH`
<a id="insn-00ace9c8"></a> `00ace9c8` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00ace9cc"></a> `00ace9cc` | `48 33 00 36` | tbz w8,#0x0,0x00acf034 | `CONDITIONAL_JUMP`
<a id="insn-00ace9d0"></a> `00ace9d0` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-00ace9d4"></a> `00ace9d4` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-00ace9d8"></a> `00ace9d8` | `bf b3 1e 38` | sturb wzr,[x29, #-0x15] | `FALL_THROUGH`
<a id="insn-00ace9dc"></a> `00ace9dc` | `a8 03 1e 38` | sturb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00ace9e0"></a> `00ace9e0` | `e8 be ff f0` | adrp x8,0x2ad000 | `FALL_THROUGH`
<a id="insn-00ace9e4"></a> `00ace9e4` | `08 09 34 91` | add x8,x8,#0xd02 | `FALL_THROUGH`
<a id="insn-00ace9e8"></a> `00ace9e8` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ace9ec"></a> `00ace9ec` | `a9 12 02 78` | sturh w9,[x21, #0x21] | `FALL_THROUGH`
<a id="insn-00ace9f0"></a> `00ace9f0` | `49 03 80 52` | mov w9,#0x1a | `FALL_THROUGH`
<a id="insn-00ace9f4"></a> `00ace9f4` | `a9 83 1c 38` | sturb w9,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00ace9f8"></a> `00ace9f8` | `a8 92 01 f8` | stur x8,[x21, #0x19] | `FALL_THROUGH`
<a id="insn-00ace9fc"></a> `00ace9fc` | `c8 be ff d0` | adrp x8,0x2a8000 | `FALL_THROUGH`
<a id="insn-00acea00"></a> `00acea00` | `08 75 13 91` | add x8,x8,#0x4dd | `FALL_THROUGH`
<a id="insn-00acea04"></a> `00acea04` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00acea08"></a> `00acea08` | `08 51 40 f8` | ldur x8,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-00acea0c"></a> `00acea0c` | `bf 63 1d 38` | sturb wzr,[x29, #-0x2a] | `FALL_THROUGH`
<a id="insn-00acea10"></a> `00acea10` | `a9 12 00 f8` | stur x9,[x21, #0x1] | `FALL_THROUGH`
<a id="insn-00acea14"></a> `00acea14` | `a8 62 00 f8` | stur x8,[x21, #0x6] | `FALL_THROUGH`
<a id="insn-00acea18"></a> `00acea18` | `a0 0a 00 d0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00acea1c"></a> `00acea1c` | `00 00 3d 91` | add x0,x0,#0xf40 | `FALL_THROUGH`
<a id="insn-00acea20"></a> `00acea20` | `a8 43 01 d1` | sub x8,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00acea24"></a> `00acea24` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00acea28"></a> `00acea28` | `a2 e3 00 d1` | sub x2,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00acea2c"></a> `00acea2c` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-00acea30"></a> `00acea30` | `41 33 e6 97` | bl 0x0045b734 | `UNCONDITIONAL_CALL`
<a id="insn-00acea34"></a> `00acea34` | `a0 03 db 3c` | ldur q0,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00acea38"></a> `00acea38` | `74 06 40 f9` | ldr x20,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00acea3c"></a> `00acea3c` | `bf 7f 3b a9` | stp xzr,xzr,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00acea40"></a> `00acea40` | `60 02 80 3d` | str q0,[x19] | `FALL_THROUGH`
<a id="insn-00acea44"></a> `00acea44` | `74 01 00 b4` | cbz x20,0x00acea70 | `CONDITIONAL_JUMP`
<a id="insn-00acea48"></a> `00acea48` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00acea4c"></a> `00acea4c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acea50"></a> `00acea50` | `d0 20 04 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00acea54"></a> `00acea54` | `e0 00 00 b5` | cbnz x0,0x00acea70 | `CONDITIONAL_JUMP`
<a id="insn-00acea58"></a> `00acea58` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00acea5c"></a> `00acea5c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acea60"></a> `00acea60` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acea64"></a> `00acea64` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acea68"></a> `00acea68` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acea6c"></a> `00acea6c` | `31 31 04 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00acea70"></a> `00acea70` | `b4 83 5b f8` | ldur x20,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00acea74"></a> `00acea74` | `74 01 00 b4` | cbz x20,0x00aceaa0 | `CONDITIONAL_JUMP`
<a id="insn-00acea78"></a> `00acea78` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00acea7c"></a> `00acea7c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acea80"></a> `00acea80` | `c4 20 04 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00acea84"></a> `00acea84` | `e0 00 00 b5` | cbnz x0,0x00aceaa0 | `CONDITIONAL_JUMP`
<a id="insn-00acea88"></a> `00acea88` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00acea8c"></a> `00acea8c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acea90"></a> `00acea90` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acea94"></a> `00acea94` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acea98"></a> `00acea98` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acea9c"></a> `00acea9c` | `25 31 04 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00aceaa0"></a> `00aceaa0` | `a8 83 5c 38` | ldurb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00aceaa4"></a> `00aceaa4` | `68 00 00 36` | tbz w8,#0x0,0x00aceab0 | `CONDITIONAL_JUMP`
<a id="insn-00aceaa8"></a> `00aceaa8` | `a0 83 5d f8` | ldur x0,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00aceaac"></a> `00aceaac` | `2d 31 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aceab0"></a> `00aceab0` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aceab4"></a> `00aceab4` | `68 00 00 36` | tbz w8,#0x0,0x00aceac0 | `CONDITIONAL_JUMP`
<a id="insn-00aceab8"></a> `00aceab8` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00aceabc"></a> `00aceabc` | `29 31 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aceac0"></a> `00aceac0` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00aceac4"></a> `00aceac4` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00aceac8"></a> `00aceac8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aceacc"></a> `00aceacc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acead0"></a> `00acead0` | `61 44 00 54` | b.ne 0x00acf35c | `CONDITIONAL_JUMP`
<a id="insn-00acead4"></a> `00acead4` | `f4 4f 4f a9` | ldp x20,x19,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00acead8"></a> `00acead8` | `f7 6b 40 f9` | ldr x23,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00aceadc"></a> `00aceadc` | `f6 57 4e a9` | ldp x22,x21,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00aceae0"></a> `00aceae0` | `fd 7b 4c a9` | ldp x29,x30,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00aceae4"></a> `00aceae4` | `ff 03 04 91` | add sp,sp,#0x100 | `FALL_THROUGH`
<a id="insn-00aceae8"></a> `00aceae8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aceaec"></a> `00aceaec` | `a5 42 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aceaf0"></a> `00aceaf0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aceaf4"></a> `00aceaf4` | `a3 42 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aceaf8"></a> `00aceaf8` | `95 45 94 52` | mov w21,#0xa22c | `FALL_THROUGH`
<a id="insn-00aceafc"></a> `00aceafc` | `75 06 a0 72` | movk w21,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00aceb00"></a> `00aceb00` | `08 68 b5 b8` | ldrsw x8,[x0, x21, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aceb04"></a> `00aceb04` | `88 0e 08 8b` | add x8,x20,x8, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00aceb08"></a> `00aceb08` | `08 d5 4c 91` | add x8,x8,#0x335, LSL #12 | `FALL_THROUGH`
<a id="insn-00aceb0c"></a> `00aceb0c` | `08 81 38 91` | add x8,x8,#0xe20 | `FALL_THROUGH`
<a id="insn-00aceb10"></a> `00aceb10` | `09 09 40 39` | ldrb w9,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00aceb14"></a> `00aceb14` | `0a 15 40 39` | ldrb w10,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-00aceb18"></a> `00aceb18` | `0b 11 40 39` | ldrb w11,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00aceb1c"></a> `00aceb1c` | `0c 05 40 39` | ldrb w12,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00aceb20"></a> `00aceb20` | `49 01 09 4a` | eor w9,w10,w9 | `FALL_THROUGH`
<a id="insn-00aceb24"></a> `00aceb24` | `0a 0d 40 39` | ldrb w10,[x8, #0x3] | `FALL_THROUGH`
<a id="insn-00aceb28"></a> `00aceb28` | `29 3d 10 53` | lsl w9,w9,#0x10 | `FALL_THROUGH`
<a id="insn-00aceb2c"></a> `00aceb2c` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00aceb30"></a> `00aceb30` | `0b 19 40 39` | ldrb w11,[x8, #0x6] | `FALL_THROUGH`
<a id="insn-00aceb34"></a> `00aceb34` | `29 61 0a 2a` | orr w9,w9,w10, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00aceb38"></a> `00aceb38` | `0a 01 40 39` | ldrb w10,[x8] | `FALL_THROUGH`
<a id="insn-00aceb3c"></a> `00aceb3c` | `08 1d 40 39` | ldrb w8,[x8, #0x7] | `FALL_THROUGH`
<a id="insn-00aceb40"></a> `00aceb40` | `6b 01 0c 4a` | eor w11,w11,w12 | `FALL_THROUGH`
<a id="insn-00aceb44"></a> `00aceb44` | `29 21 0b 2a` | orr w9,w9,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00aceb48"></a> `00aceb48` | `08 01 0a 4a` | eor w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00aceb4c"></a> `00aceb4c` | `37 01 08 2a` | orr w23,w9,w8 | `FALL_THROUGH`
<a id="insn-00aceb50"></a> `00aceb50` | `8c 42 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aceb54"></a> `00aceb54` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aceb58"></a> `00aceb58` | `8a 42 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aceb5c"></a> `00aceb5c` | `08 68 b5 b8` | ldrsw x8,[x0, x21, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aceb60"></a> `00aceb60` | `ff 0a 00 71` | cmp w23,#0x2 | `FALL_THROUGH`
<a id="insn-00aceb64"></a> `00aceb64` | `88 0e 08 8b` | add x8,x20,x8, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00aceb68"></a> `00aceb68` | `08 d5 4c 91` | add x8,x8,#0x335, LSL #12 | `FALL_THROUGH`
<a id="insn-00aceb6c"></a> `00aceb6c` | `a1 0d 00 54` | b.ne 0x00aced20 | `CONDITIONAL_JUMP`
<a id="insn-00aceb70"></a> `00aceb70` | `00 81 28 91` | add x0,x8,#0xa20 | `FALL_THROUGH`
<a id="insn-00aceb74"></a> `00aceb74` | `54 8b f0 97` | bl 0x006f18c4 | `UNCONDITIONAL_CALL`
<a id="insn-00aceb78"></a> `00aceb78` | `20 06 00 34` | cbz w0,0x00acec3c | `CONDITIONAL_JUMP`
<a id="insn-00aceb7c"></a> `00aceb7c` | `81 42 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aceb80"></a> `00aceb80` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aceb84"></a> `00aceb84` | `7f 42 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aceb88"></a> `00aceb88` | `88 45 94 52` | mov w8,#0xa22c | `FALL_THROUGH`
<a id="insn-00aceb8c"></a> `00aceb8c` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00aceb90"></a> `00aceb90` | `08 68 a8 b8` | ldrsw x8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aceb94"></a> `00aceb94` | `88 0e 08 8b` | add x8,x20,x8, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00aceb98"></a> `00aceb98` | `08 d5 4c 91` | add x8,x8,#0x335, LSL #12 | `FALL_THROUGH`
<a id="insn-00aceb9c"></a> `00aceb9c` | `00 81 28 91` | add x0,x8,#0xa20 | `FALL_THROUGH`
<a id="insn-00aceba0"></a> `00aceba0` | `49 8b f0 97` | bl 0x006f18c4 | `UNCONDITIONAL_CALL`
<a id="insn-00aceba4"></a> `00aceba4` | `1f 08 00 71` | cmp w0,#0x2 | `FALL_THROUGH`
<a id="insn-00aceba8"></a> `00aceba8` | `a0 04 00 54` | b.eq 0x00acec3c | `CONDITIONAL_JUMP`
<a id="insn-00acebac"></a> `00acebac` | `75 42 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acebb0"></a> `00acebb0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00acebb4"></a> `00acebb4` | `73 42 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acebb8"></a> `00acebb8` | `88 45 94 52` | mov w8,#0xa22c | `FALL_THROUGH`
<a id="insn-00acebbc"></a> `00acebbc` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00acebc0"></a> `00acebc0` | `08 68 a8 b8` | ldrsw x8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acebc4"></a> `00acebc4` | `88 0e 08 8b` | add x8,x20,x8, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00acebc8"></a> `00acebc8` | `08 d5 4c 91` | add x8,x8,#0x335, LSL #12 | `FALL_THROUGH`
<a id="insn-00acebcc"></a> `00acebcc` | `00 81 28 91` | add x0,x8,#0xa20 | `FALL_THROUGH`
<a id="insn-00acebd0"></a> `00acebd0` | `3d 8b f0 97` | bl 0x006f18c4 | `UNCONDITIONAL_CALL`
<a id="insn-00acebd4"></a> `00acebd4` | `1f 0c 00 71` | cmp w0,#0x3 | `FALL_THROUGH`
<a id="insn-00acebd8"></a> `00acebd8` | `20 03 00 54` | b.eq 0x00acec3c | `CONDITIONAL_JUMP`
<a id="insn-00acebdc"></a> `00acebdc` | `69 42 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acebe0"></a> `00acebe0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00acebe4"></a> `00acebe4` | `67 42 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acebe8"></a> `00acebe8` | `88 45 94 52` | mov w8,#0xa22c | `FALL_THROUGH`
<a id="insn-00acebec"></a> `00acebec` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00acebf0"></a> `00acebf0` | `08 68 a8 b8` | ldrsw x8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acebf4"></a> `00acebf4` | `88 0e 08 8b` | add x8,x20,x8, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00acebf8"></a> `00acebf8` | `08 d5 4c 91` | add x8,x8,#0x335, LSL #12 | `FALL_THROUGH`
<a id="insn-00acebfc"></a> `00acebfc` | `00 81 28 91` | add x0,x8,#0xa20 | `FALL_THROUGH`
<a id="insn-00acec00"></a> `00acec00` | `31 8b f0 97` | bl 0x006f18c4 | `UNCONDITIONAL_CALL`
<a id="insn-00acec04"></a> `00acec04` | `1f 10 00 71` | cmp w0,#0x4 | `FALL_THROUGH`
<a id="insn-00acec08"></a> `00acec08` | `a0 01 00 54` | b.eq 0x00acec3c | `CONDITIONAL_JUMP`
<a id="insn-00acec0c"></a> `00acec0c` | `5d 42 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acec10"></a> `00acec10` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00acec14"></a> `00acec14` | `5b 42 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acec18"></a> `00acec18` | `88 45 94 52` | mov w8,#0xa22c | `FALL_THROUGH`
<a id="insn-00acec1c"></a> `00acec1c` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00acec20"></a> `00acec20` | `08 68 a8 b8` | ldrsw x8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acec24"></a> `00acec24` | `88 0e 08 8b` | add x8,x20,x8, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00acec28"></a> `00acec28` | `08 d5 4c 91` | add x8,x8,#0x335, LSL #12 | `FALL_THROUGH`
<a id="insn-00acec2c"></a> `00acec2c` | `00 81 28 91` | add x0,x8,#0xa20 | `FALL_THROUGH`
<a id="insn-00acec30"></a> `00acec30` | `25 8b f0 97` | bl 0x006f18c4 | `UNCONDITIONAL_CALL`
<a id="insn-00acec34"></a> `00acec34` | `1f 14 00 71` | cmp w0,#0x5 | `FALL_THROUGH`
<a id="insn-00acec38"></a> `00acec38` | `61 13 00 54` | b.ne 0x00aceea4 | `CONDITIONAL_JUMP`
<a id="insn-00acec3c"></a> `00acec3c` | `38 bc eb 97` | bl 0x005bdd1c | `UNCONDITIONAL_CALL`
<a id="insn-00acec40"></a> `00acec40` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00acec44"></a> `00acec44` | `41 be ff 90` | adrp x1,0x296000 | `FALL_THROUGH`
<a id="insn-00acec48"></a> `00acec48` | `21 f4 04 91` | add x1,x1,#0x13d | `FALL_THROUGH`
<a id="insn-00acec4c"></a> `00acec4c` | `a0 43 01 d1` | sub x0,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00acec50"></a> `00acec50` | `92 31 e5 97` | bl 0x0041b298 | `UNCONDITIONAL_CALL`
<a id="insn-00acec54"></a> `00acec54` | `4b 42 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acec58"></a> `00acec58` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00acec5c"></a> `00acec5c` | `49 42 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acec60"></a> `00acec60` | `88 45 94 52` | mov w8,#0xa22c | `FALL_THROUGH`
<a id="insn-00acec64"></a> `00acec64` | `09 44 8b 52` | mov w9,#0x5a20 | `FALL_THROUGH`
<a id="insn-00acec68"></a> `00acec68` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00acec6c"></a> `00acec6c` | `69 06 a0 72` | movk w9,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00acec70"></a> `00acec70` | `08 68 a8 b8` | ldrsw x8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acec74"></a> `00acec74` | `a8 0e 08 8b` | add x8,x21,x8, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00acec78"></a> `00acec78` | `15 69 69 f8` | ldr x21,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acec7c"></a> `00acec7c` | `21 be ff b0` | adrp x1,0x293000 | `FALL_THROUGH`
<a id="insn-00acec80"></a> `00acec80` | `21 a0 29 91` | add x1,x1,#0xa68 | `FALL_THROUGH`
<a id="insn-00acec84"></a> `00acec84` | `e0 03 01 91` | add x0,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00acec88"></a> `00acec88` | `84 31 e5 97` | bl 0x0041b298 | `UNCONDITIONAL_CALL`
<a id="insn-00acec8c"></a> `00acec8c` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00acec90"></a> `00acec90` | `e0 03 01 91` | add x0,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00acec94"></a> `00acec94` | `ba 6c e6 97` | bl 0x00469f7c | `UNCONDITIONAL_CALL`
<a id="insn-00acec98"></a> `00acec98` | `a8 e3 00 d1` | sub x8,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00acec9c"></a> `00acec9c` | `a0 43 01 d1` | sub x0,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00aceca0"></a> `00aceca0` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aceca4"></a> `00aceca4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00aceca8"></a> `00aceca8` | `38 1c f8 97` | bl 0x008d5d88 | `UNCONDITIONAL_CALL`
<a id="insn-00acecac"></a> `00acecac` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00acecb0"></a> `00acecb0` | `a0 e3 00 d1` | sub x0,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00acecb4"></a> `00acecb4` | `b2 6c e6 97` | bl 0x00469f7c | `UNCONDITIONAL_CALL`
<a id="insn-00acecb8"></a> `00acecb8` | `41 be ff 90` | adrp x1,0x296000 | `FALL_THROUGH`
<a id="insn-00acecbc"></a> `00acecbc` | `21 64 1f 91` | add x1,x1,#0x7d9 | `FALL_THROUGH`
<a id="insn-00acecc0"></a> `00acecc0` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00acecc4"></a> `00acecc4` | `75 31 e5 97` | bl 0x0041b298 | `UNCONDITIONAL_CALL`
<a id="insn-00acecc8"></a> `00acecc8` | `e8 c3 00 91` | add x8,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aceccc"></a> `00aceccc` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00acecd0"></a> `00acecd0` | `e2 03 00 91` | mov x2,sp | `FALL_THROUGH`
<a id="insn-00acecd4"></a> `00acecd4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acecd8"></a> `00acecd8` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-00acecdc"></a> `00acecdc` | `96 32 e6 97` | bl 0x0045b734 | `UNCONDITIONAL_CALL`
<a id="insn-00acece0"></a> `00acece0` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00acece4"></a> `00acece4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acece8"></a> `00acece8` | `2d bc eb 97` | bl 0x005bdd9c | `UNCONDITIONAL_CALL`
<a id="insn-00acecec"></a> `00acecec` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00acecf0"></a> `00acecf0` | `5c f2 e5 97` | bl 0x0044b660 | `UNCONDITIONAL_CALL`
<a id="insn-00acecf4"></a> `00acecf4` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00acecf8"></a> `00acecf8` | `68 09 00 37` | tbnz w8,#0x0,0x00acee24 | `CONDITIONAL_JUMP`
<a id="insn-00acecfc"></a> `00acecfc` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aced00"></a> `00aced00` | `a8 09 00 37` | tbnz w8,#0x0,0x00acee34 | `CONDITIONAL_JUMP`
<a id="insn-00aced04"></a> `00aced04` | `a8 83 5c 38` | ldurb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00aced08"></a> `00aced08` | `e8 09 00 37` | tbnz w8,#0x0,0x00acee44 | `CONDITIONAL_JUMP`
<a id="insn-00aced0c"></a> `00aced0c` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aced10"></a> `00aced10` | `28 0a 00 37` | tbnz w8,#0x0,0x00acee54 | `CONDITIONAL_JUMP`
<a id="insn-00aced14"></a> `00aced14` | `e8 03 41 39` | ldrb w8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aced18"></a> `00aced18` | `68 0a 00 37` | tbnz w8,#0x0,0x00acee64 | `CONDITIONAL_JUMP`
<a id="insn-00aced1c"></a> `00aced1c` | `5e 00 00 14` | b 0x00acee94 | `UNCONDITIONAL_JUMP`
<a id="insn-00aced20"></a> `00aced20` | `00 81 38 91` | add x0,x8,#0xe20 | `FALL_THROUGH`
<a id="insn-00aced24"></a> `00aced24` | `e8 8a f0 97` | bl 0x006f18c4 | `UNCONDITIONAL_CALL`
<a id="insn-00aced28"></a> `00aced28` | `1f 0c 00 71` | cmp w0,#0x3 | `FALL_THROUGH`
<a id="insn-00aced2c"></a> `00aced2c` | `a1 ec ff 54` | b.ne 0x00aceac0 | `CONDITIONAL_JUMP`
<a id="insn-00aced30"></a> `00aced30` | `fb bb eb 97` | bl 0x005bdd1c | `UNCONDITIONAL_CALL`
<a id="insn-00aced34"></a> `00aced34` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aced38"></a> `00aced38` | `81 be ff 90` | adrp x1,0x29e000 | `FALL_THROUGH`
<a id="insn-00aced3c"></a> `00aced3c` | `21 dc 18 91` | add x1,x1,#0x637 | `FALL_THROUGH`
<a id="insn-00aced40"></a> `00aced40` | `a0 43 01 d1` | sub x0,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00aced44"></a> `00aced44` | `55 31 e5 97` | bl 0x0041b298 | `UNCONDITIONAL_CALL`
<a id="insn-00aced48"></a> `00aced48` | `0e 42 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aced4c"></a> `00aced4c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00aced50"></a> `00aced50` | `0c 42 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aced54"></a> `00aced54` | `88 45 94 52` | mov w8,#0xa22c | `FALL_THROUGH`
<a id="insn-00aced58"></a> `00aced58` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00aced5c"></a> `00aced5c` | `08 68 a8 b8` | ldrsw x8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aced60"></a> `00aced60` | `a8 0e 08 8b` | add x8,x21,x8, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00aced64"></a> `00aced64` | `08 d5 4c 91` | add x8,x8,#0x335, LSL #12 | `FALL_THROUGH`
<a id="insn-00aced68"></a> `00aced68` | `00 81 28 91` | add x0,x8,#0xa20 | `FALL_THROUGH`
<a id="insn-00aced6c"></a> `00aced6c` | `d6 8a f0 97` | bl 0x006f18c4 | `UNCONDITIONAL_CALL`
<a id="insn-00aced70"></a> `00aced70` | `e5 90 f0 97` | bl 0x006f3104 | `UNCONDITIONAL_CALL`
<a id="insn-00aced74"></a> `00aced74` | `e2 03 00 2a` | mov w2,w0 | `FALL_THROUGH`
<a id="insn-00aced78"></a> `00aced78` | `a8 e3 00 d1` | sub x8,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00aced7c"></a> `00aced7c` | `a0 43 01 d1` | sub x0,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00aced80"></a> `00aced80` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00aced84"></a> `00aced84` | `8c 59 e5 97` | bl 0x004253b4 | `UNCONDITIONAL_CALL`
<a id="insn-00aced88"></a> `00aced88` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00aced8c"></a> `00aced8c` | `a0 e3 00 d1` | sub x0,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00aced90"></a> `00aced90` | `7b 6c e6 97` | bl 0x00469f7c | `UNCONDITIONAL_CALL`
<a id="insn-00aced94"></a> `00aced94` | `41 be ff 90` | adrp x1,0x296000 | `FALL_THROUGH`
<a id="insn-00aced98"></a> `00aced98` | `21 64 1f 91` | add x1,x1,#0x7d9 | `FALL_THROUGH`
<a id="insn-00aced9c"></a> `00aced9c` | `e0 03 01 91` | add x0,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00aceda0"></a> `00aceda0` | `3e 31 e5 97` | bl 0x0041b298 | `UNCONDITIONAL_CALL`
<a id="insn-00aceda4"></a> `00aceda4` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00aceda8"></a> `00aceda8` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00acedac"></a> `00acedac` | `e2 03 01 91` | add x2,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00acedb0"></a> `00acedb0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acedb4"></a> `00acedb4` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-00acedb8"></a> `00acedb8` | `5f 32 e6 97` | bl 0x0045b734 | `UNCONDITIONAL_CALL`
<a id="insn-00acedbc"></a> `00acedbc` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00acedc0"></a> `00acedc0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acedc4"></a> `00acedc4` | `f6 bb eb 97` | bl 0x005bdd9c | `UNCONDITIONAL_CALL`
<a id="insn-00acedc8"></a> `00acedc8` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00acedcc"></a> `00acedcc` | `25 f2 e5 97` | bl 0x0044b660 | `UNCONDITIONAL_CALL`
<a id="insn-00acedd0"></a> `00acedd0` | `e8 03 41 39` | ldrb w8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acedd4"></a> `00acedd4` | `c8 04 00 37` | tbnz w8,#0x0,0x00acee6c | `CONDITIONAL_JUMP`
<a id="insn-00acedd8"></a> `00acedd8` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aceddc"></a> `00aceddc` | `08 05 00 37` | tbnz w8,#0x0,0x00acee7c | `CONDITIONAL_JUMP`
<a id="insn-00acede0"></a> `00acede0` | `a8 83 5c 38` | ldurb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00acede4"></a> `00acede4` | `48 05 00 37` | tbnz w8,#0x0,0x00acee8c | `CONDITIONAL_JUMP`
<a id="insn-00acede8"></a> `00acede8` | `2b 00 00 14` | b 0x00acee94 | `UNCONDITIONAL_JUMP`
<a id="insn-00acedec"></a> `00acedec` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acedf0"></a> `00acedf0` | `5c 30 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00acedf4"></a> `00acedf4` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00acedf8"></a> `00acedf8` | `48 cd 07 36` | tbz w8,#0x0,0x00ace7a0 | `CONDITIONAL_JUMP`
<a id="insn-00acedfc"></a> `00acedfc` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00acee00"></a> `00acee00` | `58 30 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00acee04"></a> `00acee04` | `a8 83 5c 38` | ldurb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00acee08"></a> `00acee08` | `08 cd 07 36` | tbz w8,#0x0,0x00ace7a8 | `CONDITIONAL_JUMP`
<a id="insn-00acee0c"></a> `00acee0c` | `a0 83 5d f8` | ldur x0,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00acee10"></a> `00acee10` | `54 30 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00acee14"></a> `00acee14` | `e8 63 41 39` | ldrb w8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00acee18"></a> `00acee18` | `e8 03 00 36` | tbz w8,#0x0,0x00acee94 | `CONDITIONAL_JUMP`
<a id="insn-00acee1c"></a> `00acee1c` | `e0 37 40 f9` | ldr x0,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00acee20"></a> `00acee20` | `1c 00 00 14` | b 0x00acee90 | `UNCONDITIONAL_JUMP`
<a id="insn-00acee24"></a> `00acee24` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acee28"></a> `00acee28` | `4e 30 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00acee2c"></a> `00acee2c` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00acee30"></a> `00acee30` | `a8 f6 07 36` | tbz w8,#0x0,0x00aced04 | `CONDITIONAL_JUMP`
<a id="insn-00acee34"></a> `00acee34` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00acee38"></a> `00acee38` | `4a 30 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00acee3c"></a> `00acee3c` | `a8 83 5c 38` | ldurb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00acee40"></a> `00acee40` | `68 f6 07 36` | tbz w8,#0x0,0x00aced0c | `CONDITIONAL_JUMP`
<a id="insn-00acee44"></a> `00acee44` | `a0 83 5d f8` | ldur x0,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00acee48"></a> `00acee48` | `46 30 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00acee4c"></a> `00acee4c` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00acee50"></a> `00acee50` | `28 f6 07 36` | tbz w8,#0x0,0x00aced14 | `CONDITIONAL_JUMP`
<a id="insn-00acee54"></a> `00acee54` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00acee58"></a> `00acee58` | `42 30 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00acee5c"></a> `00acee5c` | `e8 03 41 39` | ldrb w8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acee60"></a> `00acee60` | `a8 01 00 36` | tbz w8,#0x0,0x00acee94 | `CONDITIONAL_JUMP`
<a id="insn-00acee64"></a> `00acee64` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acee68"></a> `00acee68` | `0a 00 00 14` | b 0x00acee90 | `UNCONDITIONAL_JUMP`
<a id="insn-00acee6c"></a> `00acee6c` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acee70"></a> `00acee70` | `3c 30 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00acee74"></a> `00acee74` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00acee78"></a> `00acee78` | `48 fb 07 36` | tbz w8,#0x0,0x00acede0 | `CONDITIONAL_JUMP`
<a id="insn-00acee7c"></a> `00acee7c` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00acee80"></a> `00acee80` | `38 30 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00acee84"></a> `00acee84` | `a8 83 5c 38` | ldurb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00acee88"></a> `00acee88` | `68 00 00 36` | tbz w8,#0x0,0x00acee94 | `CONDITIONAL_JUMP`
<a id="insn-00acee8c"></a> `00acee8c` | `a0 83 5d f8` | ldur x0,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00acee90"></a> `00acee90` | `34 30 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00acee94"></a> `00acee94` | `a8 03 5b 38` | ldurb w8,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00acee98"></a> `00acee98` | `48 e1 07 36` | tbz w8,#0x0,0x00aceac0 | `CONDITIONAL_JUMP`
<a id="insn-00acee9c"></a> `00acee9c` | `a0 03 5c f8` | ldur x0,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00aceea0"></a> `00aceea0` | `07 ff ff 17` | b 0x00aceabc | `UNCONDITIONAL_JUMP`
<a id="insn-00aceea4"></a> `00aceea4` | `9e bb eb 97` | bl 0x005bdd1c | `UNCONDITIONAL_CALL`
<a id="insn-00aceea8"></a> `00aceea8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aceeac"></a> `00aceeac` | `01 be ff f0` | adrp x1,0x291000 | `FALL_THROUGH`
<a id="insn-00aceeb0"></a> `00aceeb0` | `21 f0 04 91` | add x1,x1,#0x13c | `FALL_THROUGH`
<a id="insn-00aceeb4"></a> `00aceeb4` | `a0 43 01 d1` | sub x0,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00aceeb8"></a> `00aceeb8` | `f8 30 e5 97` | bl 0x0041b298 | `UNCONDITIONAL_CALL`
<a id="insn-00aceebc"></a> `00aceebc` | `b1 41 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aceec0"></a> `00aceec0` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00aceec4"></a> `00aceec4` | `af 41 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aceec8"></a> `00aceec8` | `88 45 94 52` | mov w8,#0xa22c | `FALL_THROUGH`
<a id="insn-00aceecc"></a> `00aceecc` | `09 44 8b 52` | mov w9,#0x5a20 | `FALL_THROUGH`
<a id="insn-00aceed0"></a> `00aceed0` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00aceed4"></a> `00aceed4` | `69 06 a0 72` | movk w9,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00aceed8"></a> `00aceed8` | `08 68 a8 b8` | ldrsw x8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aceedc"></a> `00aceedc` | `a8 0e 08 8b` | add x8,x21,x8, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00aceee0"></a> `00aceee0` | `02 69 69 f8` | ldr x2,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aceee4"></a> `00aceee4` | `a8 e3 00 d1` | sub x8,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00aceee8"></a> `00aceee8` | `a0 43 01 d1` | sub x0,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00aceeec"></a> `00aceeec` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00aceef0"></a> `00aceef0` | `75 77 f8 97` | bl 0x008eccc4 | `UNCONDITIONAL_CALL`
<a id="insn-00aceef4"></a> `00aceef4` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00aceef8"></a> `00aceef8` | `a0 e3 00 d1` | sub x0,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00aceefc"></a> `00aceefc` | `20 6c e6 97` | bl 0x00469f7c | `UNCONDITIONAL_CALL`
<a id="insn-00acef00"></a> `00acef00` | `41 be ff 90` | adrp x1,0x296000 | `FALL_THROUGH`
<a id="insn-00acef04"></a> `00acef04` | `21 64 1f 91` | add x1,x1,#0x7d9 | `FALL_THROUGH`
<a id="insn-00acef08"></a> `00acef08` | `e0 03 01 91` | add x0,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00acef0c"></a> `00acef0c` | `e3 30 e5 97` | bl 0x0041b298 | `UNCONDITIONAL_CALL`
<a id="insn-00acef10"></a> `00acef10` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00acef14"></a> `00acef14` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00acef18"></a> `00acef18` | `e2 03 01 91` | add x2,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00acef1c"></a> `00acef1c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acef20"></a> `00acef20` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-00acef24"></a> `00acef24` | `04 32 e6 97` | bl 0x0045b734 | `UNCONDITIONAL_CALL`
<a id="insn-00acef28"></a> `00acef28` | `a5 ff ff 17` | b 0x00acedbc | `UNCONDITIONAL_JUMP`
<a id="insn-00acef2c"></a> `00acef2c` | `a0 0a 00 d0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00acef30"></a> `00acef30` | `00 e0 3d 91` | add x0,x0,#0xf78 | `FALL_THROUGH`
<a id="insn-00acef34"></a> `00acef34` | `f3 2f 04 94` | bl 0x00bdaf00 | `UNCONDITIONAL_CALL`
<a id="insn-00acef38"></a> `00acef38` | `40 c8 ff 34` | cbz w0,0x00ace840 | `CONDITIONAL_JUMP`
<a id="insn-00acef3c"></a> `00acef3c` | `a1 0a 00 d0` | adrp x1,0xc24000 | `FALL_THROUGH`
<a id="insn-00acef40"></a> `00acef40` | `21 00 3d 91` | add x1,x1,#0xf40 | `FALL_THROUGH`
<a id="insn-00acef44"></a> `00acef44` | `60 cc ff b0` | adrp x0,0x45b000 | `FALL_THROUGH`
<a id="insn-00acef48"></a> `00acef48` | `00 70 3b 91` | add x0,x0,#0xedc | `FALL_THROUGH`
<a id="insn-00acef4c"></a> `00acef4c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00acef50"></a> `00acef50` | `a2 08 00 f0` | adrp x2,0xbe5000 | `FALL_THROUGH`
<a id="insn-00acef54"></a> `00acef54` | `42 40 3b 91` | add x2,x2,#0xed0 | `FALL_THROUGH`
<a id="insn-00acef58"></a> `00acef58` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00acef5c"></a> `00acef5c` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00acef60"></a> `00acef60` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00acef64"></a> `00acef64` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00acef68"></a> `00acef68` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00acef6c"></a> `00acef6c` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00acef70"></a> `00acef70` | `dc 2f 04 94` | bl 0x00bdaee0 | `UNCONDITIONAL_CALL`
<a id="insn-00acef74"></a> `00acef74` | `a0 0a 00 d0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00acef78"></a> `00acef78` | `00 e0 3d 91` | add x0,x0,#0xf78 | `FALL_THROUGH`
<a id="insn-00acef7c"></a> `00acef7c` | `e9 2f 04 94` | bl 0x00bdaf20 | `UNCONDITIONAL_CALL`
<a id="insn-00acef80"></a> `00acef80` | `30 fe ff 17` | b 0x00ace840 | `UNCONDITIONAL_JUMP`
<a id="insn-00acef84"></a> `00acef84` | `a0 0a 00 d0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00acef88"></a> `00acef88` | `00 e0 3d 91` | add x0,x0,#0xf78 | `FALL_THROUGH`
<a id="insn-00acef8c"></a> `00acef8c` | `dd 2f 04 94` | bl 0x00bdaf00 | `UNCONDITIONAL_CALL`
<a id="insn-00acef90"></a> `00acef90` | `c0 ad ff 34` | cbz w0,0x00ace548 | `CONDITIONAL_JUMP`
<a id="insn-00acef94"></a> `00acef94` | `a1 0a 00 d0` | adrp x1,0xc24000 | `FALL_THROUGH`
<a id="insn-00acef98"></a> `00acef98` | `21 00 3d 91` | add x1,x1,#0xf40 | `FALL_THROUGH`
<a id="insn-00acef9c"></a> `00acef9c` | `60 cc ff b0` | adrp x0,0x45b000 | `FALL_THROUGH`
<a id="insn-00acefa0"></a> `00acefa0` | `00 70 3b 91` | add x0,x0,#0xedc | `FALL_THROUGH`
<a id="insn-00acefa4"></a> `00acefa4` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00acefa8"></a> `00acefa8` | `a2 08 00 f0` | adrp x2,0xbe5000 | `FALL_THROUGH`
<a id="insn-00acefac"></a> `00acefac` | `42 40 3b 91` | add x2,x2,#0xed0 | `FALL_THROUGH`
<a id="insn-00acefb0"></a> `00acefb0` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00acefb4"></a> `00acefb4` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00acefb8"></a> `00acefb8` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00acefbc"></a> `00acefbc` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00acefc0"></a> `00acefc0` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00acefc4"></a> `00acefc4` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00acefc8"></a> `00acefc8` | `c6 2f 04 94` | bl 0x00bdaee0 | `UNCONDITIONAL_CALL`
<a id="insn-00acefcc"></a> `00acefcc` | `a0 0a 00 d0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00acefd0"></a> `00acefd0` | `00 e0 3d 91` | add x0,x0,#0xf78 | `FALL_THROUGH`
<a id="insn-00acefd4"></a> `00acefd4` | `d3 2f 04 94` | bl 0x00bdaf20 | `UNCONDITIONAL_CALL`
<a id="insn-00acefd8"></a> `00acefd8` | `5c fd ff 17` | b 0x00ace548 | `UNCONDITIONAL_JUMP`
<a id="insn-00acefdc"></a> `00acefdc` | `a0 0a 00 d0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00acefe0"></a> `00acefe0` | `00 e0 3d 91` | add x0,x0,#0xf78 | `FALL_THROUGH`
<a id="insn-00acefe4"></a> `00acefe4` | `c7 2f 04 94` | bl 0x00bdaf00 | `UNCONDITIONAL_CALL`
<a id="insn-00acefe8"></a> `00acefe8` | `c0 cb ff 34` | cbz w0,0x00ace960 | `CONDITIONAL_JUMP`
<a id="insn-00acefec"></a> `00acefec` | `a1 0a 00 d0` | adrp x1,0xc24000 | `FALL_THROUGH`
<a id="insn-00aceff0"></a> `00aceff0` | `21 00 3d 91` | add x1,x1,#0xf40 | `FALL_THROUGH`
<a id="insn-00aceff4"></a> `00aceff4` | `60 cc ff b0` | adrp x0,0x45b000 | `FALL_THROUGH`
<a id="insn-00aceff8"></a> `00aceff8` | `00 70 3b 91` | add x0,x0,#0xedc | `FALL_THROUGH`
<a id="insn-00aceffc"></a> `00aceffc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00acf000"></a> `00acf000` | `a2 08 00 d0` | adrp x2,0xbe5000 | `FALL_THROUGH`
<a id="insn-00acf004"></a> `00acf004` | `42 40 3b 91` | add x2,x2,#0xed0 | `FALL_THROUGH`
<a id="insn-00acf008"></a> `00acf008` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00acf00c"></a> `00acf00c` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00acf010"></a> `00acf010` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00acf014"></a> `00acf014` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00acf018"></a> `00acf018` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00acf01c"></a> `00acf01c` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00acf020"></a> `00acf020` | `b0 2f 04 94` | bl 0x00bdaee0 | `UNCONDITIONAL_CALL`
<a id="insn-00acf024"></a> `00acf024` | `a0 0a 00 b0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00acf028"></a> `00acf028` | `00 e0 3d 91` | add x0,x0,#0xf78 | `FALL_THROUGH`
<a id="insn-00acf02c"></a> `00acf02c` | `bd 2f 04 94` | bl 0x00bdaf20 | `UNCONDITIONAL_CALL`
<a id="insn-00acf030"></a> `00acf030` | `4c fe ff 17` | b 0x00ace960 | `UNCONDITIONAL_JUMP`
<a id="insn-00acf034"></a> `00acf034` | `a0 0a 00 b0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00acf038"></a> `00acf038` | `00 e0 3d 91` | add x0,x0,#0xf78 | `FALL_THROUGH`
<a id="insn-00acf03c"></a> `00acf03c` | `b1 2f 04 94` | bl 0x00bdaf00 | `UNCONDITIONAL_CALL`
<a id="insn-00acf040"></a> `00acf040` | `80 cc ff 34` | cbz w0,0x00ace9d0 | `CONDITIONAL_JUMP`
<a id="insn-00acf044"></a> `00acf044` | `a1 0a 00 b0` | adrp x1,0xc24000 | `FALL_THROUGH`
<a id="insn-00acf048"></a> `00acf048` | `21 00 3d 91` | add x1,x1,#0xf40 | `FALL_THROUGH`
<a id="insn-00acf04c"></a> `00acf04c` | `60 cc ff 90` | adrp x0,0x45b000 | `FALL_THROUGH`
<a id="insn-00acf050"></a> `00acf050` | `00 70 3b 91` | add x0,x0,#0xedc | `FALL_THROUGH`
<a id="insn-00acf054"></a> `00acf054` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00acf058"></a> `00acf058` | `a2 08 00 d0` | adrp x2,0xbe5000 | `FALL_THROUGH`
<a id="insn-00acf05c"></a> `00acf05c` | `42 40 3b 91` | add x2,x2,#0xed0 | `FALL_THROUGH`
<a id="insn-00acf060"></a> `00acf060` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00acf064"></a> `00acf064` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00acf068"></a> `00acf068` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00acf06c"></a> `00acf06c` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00acf070"></a> `00acf070` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00acf074"></a> `00acf074` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00acf078"></a> `00acf078` | `9a 2f 04 94` | bl 0x00bdaee0 | `UNCONDITIONAL_CALL`
<a id="insn-00acf07c"></a> `00acf07c` | `a0 0a 00 b0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00acf080"></a> `00acf080` | `00 e0 3d 91` | add x0,x0,#0xf78 | `FALL_THROUGH`
<a id="insn-00acf084"></a> `00acf084` | `a7 2f 04 94` | bl 0x00bdaf20 | `UNCONDITIONAL_CALL`
<a id="insn-00acf088"></a> `00acf088` | `52 fe ff 17` | b 0x00ace9d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00acf08c"></a> `00acf08c` | `a0 0a 00 b0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00acf090"></a> `00acf090` | `00 e0 3d 91` | add x0,x0,#0xf78 | `FALL_THROUGH`
<a id="insn-00acf094"></a> `00acf094` | `9b 2f 04 94` | bl 0x00bdaf00 | `UNCONDITIONAL_CALL`
<a id="insn-00acf098"></a> `00acf098` | `00 ae ff 34` | cbz w0,0x00ace658 | `CONDITIONAL_JUMP`
<a id="insn-00acf09c"></a> `00acf09c` | `a1 0a 00 b0` | adrp x1,0xc24000 | `FALL_THROUGH`
<a id="insn-00acf0a0"></a> `00acf0a0` | `21 00 3d 91` | add x1,x1,#0xf40 | `FALL_THROUGH`
<a id="insn-00acf0a4"></a> `00acf0a4` | `60 cc ff 90` | adrp x0,0x45b000 | `FALL_THROUGH`
<a id="insn-00acf0a8"></a> `00acf0a8` | `00 70 3b 91` | add x0,x0,#0xedc | `FALL_THROUGH`
<a id="insn-00acf0ac"></a> `00acf0ac` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00acf0b0"></a> `00acf0b0` | `a2 08 00 d0` | adrp x2,0xbe5000 | `FALL_THROUGH`
<a id="insn-00acf0b4"></a> `00acf0b4` | `42 40 3b 91` | add x2,x2,#0xed0 | `FALL_THROUGH`
<a id="insn-00acf0b8"></a> `00acf0b8` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00acf0bc"></a> `00acf0bc` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00acf0c0"></a> `00acf0c0` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00acf0c4"></a> `00acf0c4` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00acf0c8"></a> `00acf0c8` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00acf0cc"></a> `00acf0cc` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00acf0d0"></a> `00acf0d0` | `84 2f 04 94` | bl 0x00bdaee0 | `UNCONDITIONAL_CALL`
<a id="insn-00acf0d4"></a> `00acf0d4` | `a0 0a 00 b0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00acf0d8"></a> `00acf0d8` | `00 e0 3d 91` | add x0,x0,#0xf78 | `FALL_THROUGH`
<a id="insn-00acf0dc"></a> `00acf0dc` | `91 2f 04 94` | bl 0x00bdaf20 | `UNCONDITIONAL_CALL`
<a id="insn-00acf0e0"></a> `00acf0e0` | `5e fd ff 17` | b 0x00ace658 | `UNCONDITIONAL_JUMP`
<a id="insn-00acf0e4"></a> `00acf0e4` | `a0 0a 00 b0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00acf0e8"></a> `00acf0e8` | `00 e0 3d 91` | add x0,x0,#0xf78 | `FALL_THROUGH`
<a id="insn-00acf0ec"></a> `00acf0ec` | `85 2f 04 94` | bl 0x00bdaf00 | `UNCONDITIONAL_CALL`
<a id="insn-00acf0f0"></a> `00acf0f0` | `a0 bf ff 34` | cbz w0,0x00ace8e4 | `CONDITIONAL_JUMP`
<a id="insn-00acf0f4"></a> `00acf0f4` | `a1 0a 00 b0` | adrp x1,0xc24000 | `FALL_THROUGH`
<a id="insn-00acf0f8"></a> `00acf0f8` | `21 00 3d 91` | add x1,x1,#0xf40 | `FALL_THROUGH`
<a id="insn-00acf0fc"></a> `00acf0fc` | `60 cc ff 90` | adrp x0,0x45b000 | `FALL_THROUGH`
<a id="insn-00acf100"></a> `00acf100` | `00 70 3b 91` | add x0,x0,#0xedc | `FALL_THROUGH`
<a id="insn-00acf104"></a> `00acf104` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00acf108"></a> `00acf108` | `a2 08 00 d0` | adrp x2,0xbe5000 | `FALL_THROUGH`
<a id="insn-00acf10c"></a> `00acf10c` | `42 40 3b 91` | add x2,x2,#0xed0 | `FALL_THROUGH`
<a id="insn-00acf110"></a> `00acf110` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00acf114"></a> `00acf114` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00acf118"></a> `00acf118` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00acf11c"></a> `00acf11c` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00acf120"></a> `00acf120` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00acf124"></a> `00acf124` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00acf128"></a> `00acf128` | `6e 2f 04 94` | bl 0x00bdaee0 | `UNCONDITIONAL_CALL`
<a id="insn-00acf12c"></a> `00acf12c` | `a0 0a 00 b0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00acf130"></a> `00acf130` | `00 e0 3d 91` | add x0,x0,#0xf78 | `FALL_THROUGH`
<a id="insn-00acf134"></a> `00acf134` | `7b 2f 04 94` | bl 0x00bdaf20 | `UNCONDITIONAL_CALL`
<a id="insn-00acf138"></a> `00acf138` | `eb fd ff 17` | b 0x00ace8e4 | `UNCONDITIONAL_JUMP`
<a id="insn-00acf35c"></a> `00acf35c` | `0d 2f 04 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ace4cc`](#insn-00ace4cc) 範囲 `[['00ace4cc', '00ace507']]`
  - `CONDITIONAL_JUMP` [`00ace504`](#insn-00ace504) → [`00ace518`](#insn-00ace518)
  - `FALL_THROUGH` [`00ace504`](#insn-00ace504) → [`00ace508`](#insn-00ace508)
- ブロック [`00ace508`](#insn-00ace508) 範囲 `[['00ace508', '00ace50f']]`
  - `CONDITIONAL_JUMP` [`00ace50c`](#insn-00ace50c) → [`00ace518`](#insn-00ace518)
  - `FALL_THROUGH` [`00ace50c`](#insn-00ace50c) → [`00ace510`](#insn-00ace510)
- ブロック [`00ace510`](#insn-00ace510) 範囲 `[['00ace510', '00ace517']]`
  - `CONDITIONAL_JUMP` [`00ace514`](#insn-00ace514) → [`00aceac0`](#insn-00aceac0)
  - `FALL_THROUGH` [`00ace514`](#insn-00ace514) → [`00ace518`](#insn-00ace518)
- ブロック [`00ace518`](#insn-00ace518) 範囲 `[['00ace518', '00ace523']]`
  - `CONDITIONAL_JUMP` [`00ace520`](#insn-00ace520) → [`00ace5b0`](#insn-00ace5b0)
  - `FALL_THROUGH` [`00ace520`](#insn-00ace520) → [`00ace524`](#insn-00ace524)
- ブロック [`00ace524`](#insn-00ace524) 範囲 `[['00ace524', '00ace527']]`
  - `CONDITIONAL_JUMP` [`00ace524`](#insn-00ace524) → [`00ace7b4`](#insn-00ace7b4)
  - `FALL_THROUGH` [`00ace524`](#insn-00ace524) → [`00ace528`](#insn-00ace528)
- ブロック [`00ace528`](#insn-00ace528) 範囲 `[['00ace528', '00ace52f']]`
  - `CONDITIONAL_JUMP` [`00ace52c`](#insn-00ace52c) → [`00ace8a8`](#insn-00ace8a8)
  - `FALL_THROUGH` [`00ace52c`](#insn-00ace52c) → [`00ace530`](#insn-00ace530)
- ブロック [`00ace530`](#insn-00ace530) 範囲 `[['00ace530', '00ace537']]`
  - `CONDITIONAL_JUMP` [`00ace534`](#insn-00ace534) → [`00aceac0`](#insn-00aceac0)
  - `FALL_THROUGH` [`00ace534`](#insn-00ace534) → [`00ace538`](#insn-00ace538)
- ブロック [`00ace538`](#insn-00ace538) 範囲 `[['00ace538', '00ace547']]`
  - `CONDITIONAL_JUMP` [`00ace544`](#insn-00ace544) → [`00acef84`](#insn-00acef84)
  - `FALL_THROUGH` [`00ace544`](#insn-00ace544) → [`00ace548`](#insn-00ace548)
- ブロック [`00ace548`](#insn-00ace548) 範囲 `[['00ace548', '00ace5af']]`
  - `UNCONDITIONAL_JUMP` [`00ace5ac`](#insn-00ace5ac) → [`00acea34`](#insn-00acea34)
- ブロック [`00ace5b0`](#insn-00ace5b0) 範囲 `[['00ace5b0', '00ace5b7']]`
  - `CONDITIONAL_JUMP` [`00ace5b4`](#insn-00ace5b4) → [`00ace830`](#insn-00ace830)
  - `FALL_THROUGH` [`00ace5b4`](#insn-00ace5b4) → [`00ace5b8`](#insn-00ace5b8)
- ブロック [`00ace5b8`](#insn-00ace5b8) 範囲 `[['00ace5b8', '00ace5bf']]`
  - `CONDITIONAL_JUMP` [`00ace5bc`](#insn-00ace5bc) → [`00ace950`](#insn-00ace950)
  - `FALL_THROUGH` [`00ace5bc`](#insn-00ace5bc) → [`00ace5c0`](#insn-00ace5c0)
- ブロック [`00ace5c0`](#insn-00ace5c0) 範囲 `[['00ace5c0', '00ace5c7']]`
  - `CONDITIONAL_JUMP` [`00ace5c4`](#insn-00ace5c4) → [`00aceac0`](#insn-00aceac0)
  - `FALL_THROUGH` [`00ace5c4`](#insn-00ace5c4) → [`00ace5c8`](#insn-00ace5c8)
- ブロック [`00ace5c8`](#insn-00ace5c8) 範囲 `[['00ace5c8', '00ace5db']]`
  - `CONDITIONAL_JUMP` [`00ace5d8`](#insn-00ace5d8) → [`00aceac0`](#insn-00aceac0)
  - `FALL_THROUGH` [`00ace5d8`](#insn-00ace5d8) → [`00ace5dc`](#insn-00ace5dc)
- ブロック [`00ace5dc`](#insn-00ace5dc) 範囲 `[['00ace5dc', '00ace647']]`
  - `CONDITIONAL_JUMP` [`00ace644`](#insn-00ace644) → [`00aceaec`](#insn-00aceaec)
  - `FALL_THROUGH` [`00ace644`](#insn-00ace644) → [`00ace648`](#insn-00ace648)
- ブロック [`00ace648`](#insn-00ace648) 範囲 `[['00ace648', '00ace657']]`
  - `CONDITIONAL_JUMP` [`00ace654`](#insn-00ace654) → [`00acf08c`](#insn-00acf08c)
  - `FALL_THROUGH` [`00ace654`](#insn-00ace654) → [`00ace658`](#insn-00ace658)
- ブロック [`00ace658`](#insn-00ace658) 範囲 `[['00ace658', '00ace737']]`
  - `CONDITIONAL_JUMP` [`00ace734`](#insn-00ace734) → [`00ace760`](#insn-00ace760)
  - `FALL_THROUGH` [`00ace734`](#insn-00ace734) → [`00ace738`](#insn-00ace738)
- ブロック [`00ace738`](#insn-00ace738) 範囲 `[['00ace738', '00ace747']]`
  - `CONDITIONAL_JUMP` [`00ace744`](#insn-00ace744) → [`00ace760`](#insn-00ace760)
  - `FALL_THROUGH` [`00ace744`](#insn-00ace744) → [`00ace748`](#insn-00ace748)
- ブロック [`00ace748`](#insn-00ace748) 範囲 `[['00ace748', '00ace75f']]`
  - `FALL_THROUGH` [`00ace75c`](#insn-00ace75c) → [`00ace760`](#insn-00ace760)
- ブロック [`00ace760`](#insn-00ace760) 範囲 `[['00ace760', '00ace767']]`
  - `CONDITIONAL_JUMP` [`00ace764`](#insn-00ace764) → [`00ace790`](#insn-00ace790)
  - `FALL_THROUGH` [`00ace764`](#insn-00ace764) → [`00ace768`](#insn-00ace768)
- ブロック [`00ace768`](#insn-00ace768) 範囲 `[['00ace768', '00ace777']]`
  - `CONDITIONAL_JUMP` [`00ace774`](#insn-00ace774) → [`00ace790`](#insn-00ace790)
  - `FALL_THROUGH` [`00ace774`](#insn-00ace774) → [`00ace778`](#insn-00ace778)
- ブロック [`00ace778`](#insn-00ace778) 範囲 `[['00ace778', '00ace78f']]`
  - `FALL_THROUGH` [`00ace78c`](#insn-00ace78c) → [`00ace790`](#insn-00ace790)
- ブロック [`00ace790`](#insn-00ace790) 範囲 `[['00ace790', '00ace797']]`
  - `CONDITIONAL_JUMP` [`00ace794`](#insn-00ace794) → [`00acedec`](#insn-00acedec)
  - `FALL_THROUGH` [`00ace794`](#insn-00ace794) → [`00ace798`](#insn-00ace798)
- ブロック [`00ace798`](#insn-00ace798) 範囲 `[['00ace798', '00ace79f']]`
  - `CONDITIONAL_JUMP` [`00ace79c`](#insn-00ace79c) → [`00acedfc`](#insn-00acedfc)
  - `FALL_THROUGH` [`00ace79c`](#insn-00ace79c) → [`00ace7a0`](#insn-00ace7a0)
- ブロック [`00ace7a0`](#insn-00ace7a0) 範囲 `[['00ace7a0', '00ace7a7']]`
  - `CONDITIONAL_JUMP` [`00ace7a4`](#insn-00ace7a4) → [`00acee0c`](#insn-00acee0c)
  - `FALL_THROUGH` [`00ace7a4`](#insn-00ace7a4) → [`00ace7a8`](#insn-00ace7a8)
- ブロック [`00ace7a8`](#insn-00ace7a8) 範囲 `[['00ace7a8', '00ace7af']]`
  - `CONDITIONAL_JUMP` [`00ace7ac`](#insn-00ace7ac) → [`00acee1c`](#insn-00acee1c)
  - `FALL_THROUGH` [`00ace7ac`](#insn-00ace7ac) → [`00ace7b0`](#insn-00ace7b0)
- ブロック [`00ace7b0`](#insn-00ace7b0) 範囲 `[['00ace7b0', '00ace7b3']]`
  - `UNCONDITIONAL_JUMP` [`00ace7b0`](#insn-00ace7b0) → [`00acee94`](#insn-00acee94)
- ブロック [`00ace7b4`](#insn-00ace7b4) 範囲 `[['00ace7b4', '00ace7d3']]`
  - `CONDITIONAL_JUMP` [`00ace7d0`](#insn-00ace7d0) → [`00ace7fc`](#insn-00ace7fc)
  - `FALL_THROUGH` [`00ace7d0`](#insn-00ace7d0) → [`00ace7d4`](#insn-00ace7d4)
- ブロック [`00ace7d4`](#insn-00ace7d4) 範囲 `[['00ace7d4', '00ace7e3']]`
  - `CONDITIONAL_JUMP` [`00ace7e0`](#insn-00ace7e0) → [`00ace7fc`](#insn-00ace7fc)
  - `FALL_THROUGH` [`00ace7e0`](#insn-00ace7e0) → [`00ace7e4`](#insn-00ace7e4)
- ブロック [`00ace7e4`](#insn-00ace7e4) 範囲 `[['00ace7e4', '00ace7fb']]`
  - `FALL_THROUGH` [`00ace7f8`](#insn-00ace7f8) → [`00ace7fc`](#insn-00ace7fc)
- ブロック [`00ace7fc`](#insn-00ace7fc) 範囲 `[['00ace7fc', '00ace803']]`
  - `CONDITIONAL_JUMP` [`00ace800`](#insn-00ace800) → [`00aceac0`](#insn-00aceac0)
  - `FALL_THROUGH` [`00ace800`](#insn-00ace800) → [`00ace804`](#insn-00ace804)
- ブロック [`00ace804`](#insn-00ace804) 範囲 `[['00ace804', '00ace813']]`
  - `CONDITIONAL_JUMP` [`00ace810`](#insn-00ace810) → [`00aceac0`](#insn-00aceac0)
  - `FALL_THROUGH` [`00ace810`](#insn-00ace810) → [`00ace814`](#insn-00ace814)
- ブロック [`00ace814`](#insn-00ace814) 範囲 `[['00ace814', '00ace82f']]`
  - `UNCONDITIONAL_JUMP` [`00ace82c`](#insn-00ace82c) → [`00aceac0`](#insn-00aceac0)
- ブロック [`00ace830`](#insn-00ace830) 範囲 `[['00ace830', '00ace83f']]`
  - `CONDITIONAL_JUMP` [`00ace83c`](#insn-00ace83c) → [`00acef2c`](#insn-00acef2c)
  - `FALL_THROUGH` [`00ace83c`](#insn-00ace83c) → [`00ace840`](#insn-00ace840)
- ブロック [`00ace840`](#insn-00ace840) 範囲 `[['00ace840', '00ace8a7']]`
  - `UNCONDITIONAL_JUMP` [`00ace8a4`](#insn-00ace8a4) → [`00acea34`](#insn-00acea34)
- ブロック [`00ace8a8`](#insn-00ace8a8) 範囲 `[['00ace8a8', '00ace8c3']]`
  - `CONDITIONAL_JUMP` [`00ace8c0`](#insn-00ace8c0) → [`00ace9c0`](#insn-00ace9c0)
  - `FALL_THROUGH` [`00ace8c0`](#insn-00ace8c0) → [`00ace8c4`](#insn-00ace8c4)
- ブロック [`00ace8c4`](#insn-00ace8c4) 範囲 `[['00ace8c4', '00ace8d3']]`
  - `CONDITIONAL_JUMP` [`00ace8d0`](#insn-00ace8d0) → [`00ace9c0`](#insn-00ace9c0)
  - `FALL_THROUGH` [`00ace8d0`](#insn-00ace8d0) → [`00ace8d4`](#insn-00ace8d4)
- ブロック [`00ace8d4`](#insn-00ace8d4) 範囲 `[['00ace8d4', '00ace8e3']]`
  - `CONDITIONAL_JUMP` [`00ace8e0`](#insn-00ace8e0) → [`00acf0e4`](#insn-00acf0e4)
  - `FALL_THROUGH` [`00ace8e0`](#insn-00ace8e0) → [`00ace8e4`](#insn-00ace8e4)
- ブロック [`00ace8e4`](#insn-00ace8e4) 範囲 `[['00ace8e4', '00ace94f']]`
  - `UNCONDITIONAL_JUMP` [`00ace94c`](#insn-00ace94c) → [`00acea34`](#insn-00acea34)
- ブロック [`00ace950`](#insn-00ace950) 範囲 `[['00ace950', '00ace95f']]`
  - `CONDITIONAL_JUMP` [`00ace95c`](#insn-00ace95c) → [`00acefdc`](#insn-00acefdc)
  - `FALL_THROUGH` [`00ace95c`](#insn-00ace95c) → [`00ace960`](#insn-00ace960)
- ブロック [`00ace960`](#insn-00ace960) 範囲 `[['00ace960', '00ace9bf']]`
  - `UNCONDITIONAL_JUMP` [`00ace9bc`](#insn-00ace9bc) → [`00acea34`](#insn-00acea34)
- ブロック [`00ace9c0`](#insn-00ace9c0) 範囲 `[['00ace9c0', '00ace9cf']]`
  - `CONDITIONAL_JUMP` [`00ace9cc`](#insn-00ace9cc) → [`00acf034`](#insn-00acf034)
  - `FALL_THROUGH` [`00ace9cc`](#insn-00ace9cc) → [`00ace9d0`](#insn-00ace9d0)
- ブロック [`00ace9d0`](#insn-00ace9d0) 範囲 `[['00ace9d0', '00acea33']]`
  - `FALL_THROUGH` [`00acea30`](#insn-00acea30) → [`00acea34`](#insn-00acea34)
- ブロック [`00acea34`](#insn-00acea34) 範囲 `[['00acea34', '00acea47']]`
  - `CONDITIONAL_JUMP` [`00acea44`](#insn-00acea44) → [`00acea70`](#insn-00acea70)
  - `FALL_THROUGH` [`00acea44`](#insn-00acea44) → [`00acea48`](#insn-00acea48)
- ブロック [`00acea48`](#insn-00acea48) 範囲 `[['00acea48', '00acea57']]`
  - `CONDITIONAL_JUMP` [`00acea54`](#insn-00acea54) → [`00acea70`](#insn-00acea70)
  - `FALL_THROUGH` [`00acea54`](#insn-00acea54) → [`00acea58`](#insn-00acea58)
- ブロック [`00acea58`](#insn-00acea58) 範囲 `[['00acea58', '00acea6f']]`
  - `FALL_THROUGH` [`00acea6c`](#insn-00acea6c) → [`00acea70`](#insn-00acea70)
- ブロック [`00acea70`](#insn-00acea70) 範囲 `[['00acea70', '00acea77']]`
  - `CONDITIONAL_JUMP` [`00acea74`](#insn-00acea74) → [`00aceaa0`](#insn-00aceaa0)
  - `FALL_THROUGH` [`00acea74`](#insn-00acea74) → [`00acea78`](#insn-00acea78)
- ブロック [`00acea78`](#insn-00acea78) 範囲 `[['00acea78', '00acea87']]`
  - `CONDITIONAL_JUMP` [`00acea84`](#insn-00acea84) → [`00aceaa0`](#insn-00aceaa0)
  - `FALL_THROUGH` [`00acea84`](#insn-00acea84) → [`00acea88`](#insn-00acea88)
- ブロック [`00acea88`](#insn-00acea88) 範囲 `[['00acea88', '00acea9f']]`
  - `FALL_THROUGH` [`00acea9c`](#insn-00acea9c) → [`00aceaa0`](#insn-00aceaa0)
- ブロック [`00aceaa0`](#insn-00aceaa0) 範囲 `[['00aceaa0', '00aceaa7']]`
  - `CONDITIONAL_JUMP` [`00aceaa4`](#insn-00aceaa4) → [`00aceab0`](#insn-00aceab0)
  - `FALL_THROUGH` [`00aceaa4`](#insn-00aceaa4) → [`00aceaa8`](#insn-00aceaa8)
- ブロック [`00aceaa8`](#insn-00aceaa8) 範囲 `[['00aceaa8', '00aceaaf']]`
  - `FALL_THROUGH` [`00aceaac`](#insn-00aceaac) → [`00aceab0`](#insn-00aceab0)
- ブロック [`00aceab0`](#insn-00aceab0) 範囲 `[['00aceab0', '00aceab7']]`
  - `CONDITIONAL_JUMP` [`00aceab4`](#insn-00aceab4) → [`00aceac0`](#insn-00aceac0)
  - `FALL_THROUGH` [`00aceab4`](#insn-00aceab4) → [`00aceab8`](#insn-00aceab8)
- ブロック [`00aceab8`](#insn-00aceab8) 範囲 `[['00aceab8', '00aceabb']]`
  - `FALL_THROUGH` [`00aceab8`](#insn-00aceab8) → [`00aceabc`](#insn-00aceabc)
- ブロック [`00aceabc`](#insn-00aceabc) 範囲 `[['00aceabc', '00aceabf']]`
  - `FALL_THROUGH` [`00aceabc`](#insn-00aceabc) → [`00aceac0`](#insn-00aceac0)
- ブロック [`00aceac0`](#insn-00aceac0) 範囲 `[['00aceac0', '00acead3']]`
  - `CONDITIONAL_JUMP` [`00acead0`](#insn-00acead0) → [`00acf35c`](#insn-00acf35c)
  - `FALL_THROUGH` [`00acead0`](#insn-00acead0) → [`00acead4`](#insn-00acead4)
- ブロック [`00acead4`](#insn-00acead4) 範囲 `[['00acead4', '00aceaeb']]`
- ブロック [`00aceaec`](#insn-00aceaec) 範囲 `[['00aceaec', '00aceb6f']]`
  - `CONDITIONAL_JUMP` [`00aceb6c`](#insn-00aceb6c) → [`00aced20`](#insn-00aced20)
  - `FALL_THROUGH` [`00aceb6c`](#insn-00aceb6c) → [`00aceb70`](#insn-00aceb70)
- ブロック [`00aceb70`](#insn-00aceb70) 範囲 `[['00aceb70', '00aceb7b']]`
  - `CONDITIONAL_JUMP` [`00aceb78`](#insn-00aceb78) → [`00acec3c`](#insn-00acec3c)
  - `FALL_THROUGH` [`00aceb78`](#insn-00aceb78) → [`00aceb7c`](#insn-00aceb7c)
- ブロック [`00aceb7c`](#insn-00aceb7c) 範囲 `[['00aceb7c', '00acebab']]`
  - `CONDITIONAL_JUMP` [`00aceba8`](#insn-00aceba8) → [`00acec3c`](#insn-00acec3c)
  - `FALL_THROUGH` [`00aceba8`](#insn-00aceba8) → [`00acebac`](#insn-00acebac)
- ブロック [`00acebac`](#insn-00acebac) 範囲 `[['00acebac', '00acebdb']]`
  - `CONDITIONAL_JUMP` [`00acebd8`](#insn-00acebd8) → [`00acec3c`](#insn-00acec3c)
  - `FALL_THROUGH` [`00acebd8`](#insn-00acebd8) → [`00acebdc`](#insn-00acebdc)
- ブロック [`00acebdc`](#insn-00acebdc) 範囲 `[['00acebdc', '00acec0b']]`
  - `CONDITIONAL_JUMP` [`00acec08`](#insn-00acec08) → [`00acec3c`](#insn-00acec3c)
  - `FALL_THROUGH` [`00acec08`](#insn-00acec08) → [`00acec0c`](#insn-00acec0c)
- ブロック [`00acec0c`](#insn-00acec0c) 範囲 `[['00acec0c', '00acec3b']]`
  - `CONDITIONAL_JUMP` [`00acec38`](#insn-00acec38) → [`00aceea4`](#insn-00aceea4)
  - `FALL_THROUGH` [`00acec38`](#insn-00acec38) → [`00acec3c`](#insn-00acec3c)
- ブロック [`00acec3c`](#insn-00acec3c) 範囲 `[['00acec3c', '00acecfb']]`
  - `CONDITIONAL_JUMP` [`00acecf8`](#insn-00acecf8) → [`00acee24`](#insn-00acee24)
  - `FALL_THROUGH` [`00acecf8`](#insn-00acecf8) → [`00acecfc`](#insn-00acecfc)
- ブロック [`00acecfc`](#insn-00acecfc) 範囲 `[['00acecfc', '00aced03']]`
  - `CONDITIONAL_JUMP` [`00aced00`](#insn-00aced00) → [`00acee34`](#insn-00acee34)
  - `FALL_THROUGH` [`00aced00`](#insn-00aced00) → [`00aced04`](#insn-00aced04)
- ブロック [`00aced04`](#insn-00aced04) 範囲 `[['00aced04', '00aced0b']]`
  - `CONDITIONAL_JUMP` [`00aced08`](#insn-00aced08) → [`00acee44`](#insn-00acee44)
  - `FALL_THROUGH` [`00aced08`](#insn-00aced08) → [`00aced0c`](#insn-00aced0c)
- ブロック [`00aced0c`](#insn-00aced0c) 範囲 `[['00aced0c', '00aced13']]`
  - `CONDITIONAL_JUMP` [`00aced10`](#insn-00aced10) → [`00acee54`](#insn-00acee54)
  - `FALL_THROUGH` [`00aced10`](#insn-00aced10) → [`00aced14`](#insn-00aced14)
- ブロック [`00aced14`](#insn-00aced14) 範囲 `[['00aced14', '00aced1b']]`
  - `CONDITIONAL_JUMP` [`00aced18`](#insn-00aced18) → [`00acee64`](#insn-00acee64)
  - `FALL_THROUGH` [`00aced18`](#insn-00aced18) → [`00aced1c`](#insn-00aced1c)
- ブロック [`00aced1c`](#insn-00aced1c) 範囲 `[['00aced1c', '00aced1f']]`
  - `UNCONDITIONAL_JUMP` [`00aced1c`](#insn-00aced1c) → [`00acee94`](#insn-00acee94)
- ブロック [`00aced20`](#insn-00aced20) 範囲 `[['00aced20', '00aced2f']]`
  - `CONDITIONAL_JUMP` [`00aced2c`](#insn-00aced2c) → [`00aceac0`](#insn-00aceac0)
  - `FALL_THROUGH` [`00aced2c`](#insn-00aced2c) → [`00aced30`](#insn-00aced30)
- ブロック [`00aced30`](#insn-00aced30) 範囲 `[['00aced30', '00acedbb']]`
  - `FALL_THROUGH` [`00acedb8`](#insn-00acedb8) → [`00acedbc`](#insn-00acedbc)
- ブロック [`00acedbc`](#insn-00acedbc) 範囲 `[['00acedbc', '00acedd7']]`
  - `CONDITIONAL_JUMP` [`00acedd4`](#insn-00acedd4) → [`00acee6c`](#insn-00acee6c)
  - `FALL_THROUGH` [`00acedd4`](#insn-00acedd4) → [`00acedd8`](#insn-00acedd8)
- ブロック [`00acedd8`](#insn-00acedd8) 範囲 `[['00acedd8', '00aceddf']]`
  - `CONDITIONAL_JUMP` [`00aceddc`](#insn-00aceddc) → [`00acee7c`](#insn-00acee7c)
  - `FALL_THROUGH` [`00aceddc`](#insn-00aceddc) → [`00acede0`](#insn-00acede0)
- ブロック [`00acede0`](#insn-00acede0) 範囲 `[['00acede0', '00acede7']]`
  - `CONDITIONAL_JUMP` [`00acede4`](#insn-00acede4) → [`00acee8c`](#insn-00acee8c)
  - `FALL_THROUGH` [`00acede4`](#insn-00acede4) → [`00acede8`](#insn-00acede8)
- ブロック [`00acede8`](#insn-00acede8) 範囲 `[['00acede8', '00acedeb']]`
  - `UNCONDITIONAL_JUMP` [`00acede8`](#insn-00acede8) → [`00acee94`](#insn-00acee94)
- ブロック [`00acedec`](#insn-00acedec) 範囲 `[['00acedec', '00acedfb']]`
  - `CONDITIONAL_JUMP` [`00acedf8`](#insn-00acedf8) → [`00ace7a0`](#insn-00ace7a0)
  - `FALL_THROUGH` [`00acedf8`](#insn-00acedf8) → [`00acedfc`](#insn-00acedfc)
- ブロック [`00acedfc`](#insn-00acedfc) 範囲 `[['00acedfc', '00acee0b']]`
  - `CONDITIONAL_JUMP` [`00acee08`](#insn-00acee08) → [`00ace7a8`](#insn-00ace7a8)
  - `FALL_THROUGH` [`00acee08`](#insn-00acee08) → [`00acee0c`](#insn-00acee0c)
- ブロック [`00acee0c`](#insn-00acee0c) 範囲 `[['00acee0c', '00acee1b']]`
  - `CONDITIONAL_JUMP` [`00acee18`](#insn-00acee18) → [`00acee94`](#insn-00acee94)
  - `FALL_THROUGH` [`00acee18`](#insn-00acee18) → [`00acee1c`](#insn-00acee1c)
- ブロック [`00acee1c`](#insn-00acee1c) 範囲 `[['00acee1c', '00acee23']]`
  - `UNCONDITIONAL_JUMP` [`00acee20`](#insn-00acee20) → [`00acee90`](#insn-00acee90)
- ブロック [`00acee24`](#insn-00acee24) 範囲 `[['00acee24', '00acee2f']]`
  - `FALL_THROUGH` [`00acee2c`](#insn-00acee2c) → [`00acee30`](#insn-00acee30)
- ブロック [`00acee30`](#insn-00acee30) 範囲 `[['00acee30', '00acee33']]`
  - `CONDITIONAL_JUMP` [`00acee30`](#insn-00acee30) → [`00aced04`](#insn-00aced04)
  - `FALL_THROUGH` [`00acee30`](#insn-00acee30) → [`00acee34`](#insn-00acee34)
- ブロック [`00acee34`](#insn-00acee34) 範囲 `[['00acee34', '00acee3b']]`
  - `FALL_THROUGH` [`00acee38`](#insn-00acee38) → [`00acee3c`](#insn-00acee3c)
- ブロック [`00acee3c`](#insn-00acee3c) 範囲 `[['00acee3c', '00acee43']]`
  - `CONDITIONAL_JUMP` [`00acee40`](#insn-00acee40) → [`00aced0c`](#insn-00aced0c)
  - `FALL_THROUGH` [`00acee40`](#insn-00acee40) → [`00acee44`](#insn-00acee44)
- ブロック [`00acee44`](#insn-00acee44) 範囲 `[['00acee44', '00acee53']]`
  - `CONDITIONAL_JUMP` [`00acee50`](#insn-00acee50) → [`00aced14`](#insn-00aced14)
  - `FALL_THROUGH` [`00acee50`](#insn-00acee50) → [`00acee54`](#insn-00acee54)
- ブロック [`00acee54`](#insn-00acee54) 範囲 `[['00acee54', '00acee63']]`
  - `CONDITIONAL_JUMP` [`00acee60`](#insn-00acee60) → [`00acee94`](#insn-00acee94)
  - `FALL_THROUGH` [`00acee60`](#insn-00acee60) → [`00acee64`](#insn-00acee64)
- ブロック [`00acee64`](#insn-00acee64) 範囲 `[['00acee64', '00acee6b']]`
  - `UNCONDITIONAL_JUMP` [`00acee68`](#insn-00acee68) → [`00acee90`](#insn-00acee90)
- ブロック [`00acee6c`](#insn-00acee6c) 範囲 `[['00acee6c', '00acee7b']]`
  - `CONDITIONAL_JUMP` [`00acee78`](#insn-00acee78) → [`00acede0`](#insn-00acede0)
  - `FALL_THROUGH` [`00acee78`](#insn-00acee78) → [`00acee7c`](#insn-00acee7c)
- ブロック [`00acee7c`](#insn-00acee7c) 範囲 `[['00acee7c', '00acee8b']]`
  - `CONDITIONAL_JUMP` [`00acee88`](#insn-00acee88) → [`00acee94`](#insn-00acee94)
  - `FALL_THROUGH` [`00acee88`](#insn-00acee88) → [`00acee8c`](#insn-00acee8c)
- ブロック [`00acee8c`](#insn-00acee8c) 範囲 `[['00acee8c', '00acee8f']]`
  - `FALL_THROUGH` [`00acee8c`](#insn-00acee8c) → [`00acee90`](#insn-00acee90)
- ブロック [`00acee90`](#insn-00acee90) 範囲 `[['00acee90', '00acee93']]`
  - `FALL_THROUGH` [`00acee90`](#insn-00acee90) → [`00acee94`](#insn-00acee94)
- ブロック [`00acee94`](#insn-00acee94) 範囲 `[['00acee94', '00acee9b']]`
  - `CONDITIONAL_JUMP` [`00acee98`](#insn-00acee98) → [`00aceac0`](#insn-00aceac0)
  - `FALL_THROUGH` [`00acee98`](#insn-00acee98) → [`00acee9c`](#insn-00acee9c)
- ブロック [`00acee9c`](#insn-00acee9c) 範囲 `[['00acee9c', '00aceea3']]`
  - `UNCONDITIONAL_JUMP` [`00aceea0`](#insn-00aceea0) → [`00aceabc`](#insn-00aceabc)
- ブロック [`00aceea4`](#insn-00aceea4) 範囲 `[['00aceea4', '00acef2b']]`
  - `UNCONDITIONAL_JUMP` [`00acef28`](#insn-00acef28) → [`00acedbc`](#insn-00acedbc)
- ブロック [`00acef2c`](#insn-00acef2c) 範囲 `[['00acef2c', '00acef3b']]`
  - `CONDITIONAL_JUMP` [`00acef38`](#insn-00acef38) → [`00ace840`](#insn-00ace840)
  - `FALL_THROUGH` [`00acef38`](#insn-00acef38) → [`00acef3c`](#insn-00acef3c)
- ブロック [`00acef3c`](#insn-00acef3c) 範囲 `[['00acef3c', '00acef83']]`
  - `UNCONDITIONAL_JUMP` [`00acef80`](#insn-00acef80) → [`00ace840`](#insn-00ace840)
- ブロック [`00acef84`](#insn-00acef84) 範囲 `[['00acef84', '00acef93']]`
  - `CONDITIONAL_JUMP` [`00acef90`](#insn-00acef90) → [`00ace548`](#insn-00ace548)
  - `FALL_THROUGH` [`00acef90`](#insn-00acef90) → [`00acef94`](#insn-00acef94)
- ブロック [`00acef94`](#insn-00acef94) 範囲 `[['00acef94', '00acefdb']]`
  - `UNCONDITIONAL_JUMP` [`00acefd8`](#insn-00acefd8) → [`00ace548`](#insn-00ace548)
- ブロック [`00acefdc`](#insn-00acefdc) 範囲 `[['00acefdc', '00acefeb']]`
  - `CONDITIONAL_JUMP` [`00acefe8`](#insn-00acefe8) → [`00ace960`](#insn-00ace960)
  - `FALL_THROUGH` [`00acefe8`](#insn-00acefe8) → [`00acefec`](#insn-00acefec)
- ブロック [`00acefec`](#insn-00acefec) 範囲 `[['00acefec', '00acf033']]`
  - `UNCONDITIONAL_JUMP` [`00acf030`](#insn-00acf030) → [`00ace960`](#insn-00ace960)
- ブロック [`00acf034`](#insn-00acf034) 範囲 `[['00acf034', '00acf043']]`
  - `CONDITIONAL_JUMP` [`00acf040`](#insn-00acf040) → [`00ace9d0`](#insn-00ace9d0)
  - `FALL_THROUGH` [`00acf040`](#insn-00acf040) → [`00acf044`](#insn-00acf044)
- ブロック [`00acf044`](#insn-00acf044) 範囲 `[['00acf044', '00acf08b']]`
  - `UNCONDITIONAL_JUMP` [`00acf088`](#insn-00acf088) → [`00ace9d0`](#insn-00ace9d0)
- ブロック [`00acf08c`](#insn-00acf08c) 範囲 `[['00acf08c', '00acf09b']]`
  - `CONDITIONAL_JUMP` [`00acf098`](#insn-00acf098) → [`00ace658`](#insn-00ace658)
  - `FALL_THROUGH` [`00acf098`](#insn-00acf098) → [`00acf09c`](#insn-00acf09c)
- ブロック [`00acf09c`](#insn-00acf09c) 範囲 `[['00acf09c', '00acf0e3']]`
  - `UNCONDITIONAL_JUMP` [`00acf0e0`](#insn-00acf0e0) → [`00ace658`](#insn-00ace658)
- ブロック [`00acf0e4`](#insn-00acf0e4) 範囲 `[['00acf0e4', '00acf0f3']]`
  - `CONDITIONAL_JUMP` [`00acf0f0`](#insn-00acf0f0) → [`00ace8e4`](#insn-00ace8e4)
  - `FALL_THROUGH` [`00acf0f0`](#insn-00acf0f0) → [`00acf0f4`](#insn-00acf0f4)
- ブロック [`00acf0f4`](#insn-00acf0f4) 範囲 `[['00acf0f4', '00acf13b']]`
  - `UNCONDITIONAL_JUMP` [`00acf138`](#insn-00acf138) → [`00ace8e4`](#insn-00ace8e4)
- ブロック [`00acf35c`](#insn-00acf35c) 範囲 `[['00acf35c', '00acf35f']]`

## 命令位置別の参照

- [`00ace4d0`](#insn-00ace4d0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace4d4`](#insn-00ace4d4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace4d8`](#insn-00ace4d8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace4dc`](#insn-00ace4dc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace500`](#insn-00ace500) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace504`](#insn-00ace504) → [`00ace518`](#insn-00ace518) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace50c`](#insn-00ace50c) → [`00ace518`](#insn-00ace518) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace510`](#insn-00ace510) → [`00467d20`](../00467/00467d20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467d20` · 推定シンボル `None` · 推定型 `None`
- [`00ace514`](#insn-00ace514) → [`00aceac0`](#insn-00aceac0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace520`](#insn-00ace520) → [`00ace5b0`](#insn-00ace5b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace524`](#insn-00ace524) → [`00ace7b4`](#insn-00ace7b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace52c`](#insn-00ace52c) → [`00ace8a8`](#insn-00ace8a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace534`](#insn-00ace534) → [`00aceac0`](#insn-00aceac0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace540`](#insn-00ace540) → `00c24f78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ace544`](#insn-00ace544) → [`00acef84`](#insn-00acef84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace550`](#insn-00ace550) → `Stack[-0x55]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace554`](#insn-00ace554) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace560`](#insn-00ace560) → `00294b68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ace564`](#insn-00ace564) → `Stack[-0x57]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace56c`](#insn-00ace56c) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace570`](#insn-00ace570) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace57c`](#insn-00ace57c) → `002acb6e`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace580`](#insn-00ace580) → `002acb73`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ace584`](#insn-00ace584) → `Stack[-0x6a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace588`](#insn-00ace588) → `Stack[-0x77]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace58c`](#insn-00ace58c) → `Stack[-0x72]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace594`](#insn-00ace594) → `00c24f40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ace5a8`](#insn-00ace5a8) → [`0045b734`](../0045b/0045b734.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045b734` · 推定シンボル `None` · 推定型 `None`
- [`00ace5ac`](#insn-00ace5ac) → [`00acea34`](#insn-00acea34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace5b4`](#insn-00ace5b4) → [`00ace830`](#insn-00ace830) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace5bc`](#insn-00ace5bc) → [`00ace950`](#insn-00ace950) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace5c4`](#insn-00ace5c4) → [`00aceac0`](#insn-00aceac0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace5c8`](#insn-00ace5c8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ace5d4`](#insn-00ace5d4) → `00331eaa`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[43]`
- [`00ace5d8`](#insn-00ace5d8) → [`00aceac0`](#insn-00aceac0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace5dc`](#insn-00ace5dc) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ace5e4`](#insn-00ace5e4) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ace5f0`](#insn-00ace5f0) → `0033a22c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ace600`](#insn-00ace600) → `00335e22`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[63]`
- [`00ace604`](#insn-00ace604) → `00335e25`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[63]`
- [`00ace608`](#insn-00ace608) → `00335e24`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[63]`
- [`00ace60c`](#insn-00ace60c) → `00335e21`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[63]`
- [`00ace614`](#insn-00ace614) → `00335e23`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[63]`
- [`00ace620`](#insn-00ace620) → `00335e26`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[63]`
- [`00ace628`](#insn-00ace628) → `00335e20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[63]`
- [`00ace62c`](#insn-00ace62c) → `00335e27`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[63]`
- [`00ace644`](#insn-00ace644) → [`00aceaec`](#insn-00aceaec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace650`](#insn-00ace650) → `00c24f78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ace654`](#insn-00ace654) → [`00acf08c`](#insn-00acf08c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace660`](#insn-00ace660) → `Stack[-0x89]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace668`](#insn-00ace668) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace670`](#insn-00ace670) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace674`](#insn-00ace674) → `Stack[-0x8b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace678`](#insn-00ace678) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ace680`](#insn-00ace680) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ace68c`](#insn-00ace68c) → `0033a22c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ace69c`](#insn-00ace69c) → `00335a22`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`00ace6a0`](#insn-00ace6a0) → `00335a25`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`00ace6a4`](#insn-00ace6a4) → `00335a24`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`00ace6a8`](#insn-00ace6a8) → `00335a21`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`00ace6b0`](#insn-00ace6b0) → `00335a23`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`00ace6bc`](#insn-00ace6bc) → `00335a26`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`00ace6c4`](#insn-00ace6c4) → `00335a20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`00ace6c8`](#insn-00ace6c8) → `00335a27`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`00ace6e4`](#insn-00ace6e4) → [`0064104c`](../00641/0064104c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0064104c` · 推定シンボル `None` · 推定型 `None`
- [`00ace6f4`](#insn-00ace6f4) → [`0046ff30`](../0046f/0046ff30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ff30` · 推定シンボル `None` · 推定型 `None`
- [`00ace700`](#insn-00ace700) → [`00469f7c`](../00469/00469f7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469f7c` · 推定シンボル `None` · 推定型 `None`
- [`00ace704`](#insn-00ace704) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace70c`](#insn-00ace70c) → `00c24f40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ace720`](#insn-00ace720) → [`0045b734`](../0045b/0045b734.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045b734` · 推定シンボル `None` · 推定型 `None`
- [`00ace724`](#insn-00ace724) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace72c`](#insn-00ace72c) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace734`](#insn-00ace734) → [`00ace760`](#insn-00ace760) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace740`](#insn-00ace740) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00ace744`](#insn-00ace744) → [`00ace760`](#insn-00ace760) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace75c`](#insn-00ace75c) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00ace760`](#insn-00ace760) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace764`](#insn-00ace764) → [`00ace790`](#insn-00ace790) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace770`](#insn-00ace770) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00ace774`](#insn-00ace774) → [`00ace790`](#insn-00ace790) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace78c`](#insn-00ace78c) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00ace790`](#insn-00ace790) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace794`](#insn-00ace794) → [`00acedec`](#insn-00acedec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace798`](#insn-00ace798) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace79c`](#insn-00ace79c) → [`00acedfc`](#insn-00acedfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace7a0`](#insn-00ace7a0) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace7a4`](#insn-00ace7a4) → [`00acee0c`](#insn-00acee0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace7a8`](#insn-00ace7a8) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace7ac`](#insn-00ace7ac) → [`00acee1c`](#insn-00acee1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace7b0`](#insn-00ace7b0) → [`00acee94`](#insn-00acee94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace7b4`](#insn-00ace7b4) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ace7bc`](#insn-00ace7bc) → [`00830c98`](../00830/00830c98.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00830c98` · 推定シンボル `None` · 推定型 `None`
- [`00ace7c0`](#insn-00ace7c0) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace7c8`](#insn-00ace7c8) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace7d0`](#insn-00ace7d0) → [`00ace7fc`](#insn-00ace7fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace7dc`](#insn-00ace7dc) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00ace7e0`](#insn-00ace7e0) → [`00ace7fc`](#insn-00ace7fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace7f8`](#insn-00ace7f8) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00ace7fc`](#insn-00ace7fc) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace800`](#insn-00ace800) → [`00aceac0`](#insn-00aceac0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace80c`](#insn-00ace80c) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00ace810`](#insn-00ace810) → [`00aceac0`](#insn-00aceac0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace828`](#insn-00ace828) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00ace82c`](#insn-00ace82c) → [`00aceac0`](#insn-00aceac0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace838`](#insn-00ace838) → `00c24f78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ace83c`](#insn-00ace83c) → [`00acef2c`](#insn-00acef2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace848`](#insn-00ace848) → `Stack[-0x55]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace84c`](#insn-00ace84c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace858`](#insn-00ace858) → `002a081f`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ace85c`](#insn-00ace85c) → `Stack[-0x57]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace864`](#insn-00ace864) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace868`](#insn-00ace868) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace874`](#insn-00ace874) → `0029b6af`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ace878`](#insn-00ace878) → `0029b6b4`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ace87c`](#insn-00ace87c) → `Stack[-0x6a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace880`](#insn-00ace880) → `Stack[-0x77]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace884`](#insn-00ace884) → `Stack[-0x72]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace88c`](#insn-00ace88c) → `00c24f40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ace8a0`](#insn-00ace8a0) → [`0045b734`](../0045b/0045b734.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045b734` · 推定シンボル `None` · 推定型 `None`
- [`00ace8a4`](#insn-00ace8a4) → [`00acea34`](#insn-00acea34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace8a8`](#insn-00ace8a8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ace8b4`](#insn-00ace8b4) → `0032ff0c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[35]`
- [`00ace8b8`](#insn-00ace8b8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ace8c0`](#insn-00ace8c0) → [`00ace9c0`](#insn-00ace9c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace8c4`](#insn-00ace8c4) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ace8d0`](#insn-00ace8d0) → [`00ace9c0`](#insn-00ace9c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace8dc`](#insn-00ace8dc) → `00c24f78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ace8e0`](#insn-00ace8e0) → [`00acf0e4`](#insn-00acf0e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace8f0`](#insn-00ace8f0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace8f8`](#insn-00ace8f8) → `002a4817`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ace900`](#insn-00ace900) → `Stack[-0x4c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace904`](#insn-00ace904) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace90c`](#insn-00ace90c) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace918`](#insn-00ace918) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace91c`](#insn-00ace91c) → `002adceb`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ace920`](#insn-00ace920) → `002adcf9`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ace924`](#insn-00ace924) → `Stack[-0x61]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace928`](#insn-00ace928) → `Stack[-0x77]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace92c`](#insn-00ace92c) → `Stack[-0x69]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace934`](#insn-00ace934) → `00c24f40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ace948`](#insn-00ace948) → [`0045b734`](../0045b/0045b734.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045b734` · 推定シンボル `None` · 推定型 `None`
- [`00ace94c`](#insn-00ace94c) → [`00acea34`](#insn-00acea34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace958`](#insn-00ace958) → `00c24f78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ace95c`](#insn-00ace95c) → [`00acefdc`](#insn-00acefdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace96c`](#insn-00ace96c) → `002aeec9`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ace970`](#insn-00ace970) → `002aeece`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ace974`](#insn-00ace974) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace97c`](#insn-00ace97c) → `Stack[-0x52]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace980`](#insn-00ace980) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace984`](#insn-00ace984) → `Stack[-0x5a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace990`](#insn-00ace990) → `002ade27`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ace994`](#insn-00ace994) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace998`](#insn-00ace998) → `Stack[-0x67]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace99c`](#insn-00ace99c) → `Stack[-0x77]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace9a4`](#insn-00ace9a4) → `00c24f40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ace9b8`](#insn-00ace9b8) → [`0045b734`](../0045b/0045b734.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045b734` · 推定シンボル `None` · 推定型 `None`
- [`00ace9bc`](#insn-00ace9bc) → [`00acea34`](#insn-00acea34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace9c8`](#insn-00ace9c8) → `00c24f78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ace9cc`](#insn-00ace9cc) → [`00acf034`](#insn-00acf034) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace9d8`](#insn-00ace9d8) → `Stack[-0x55]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace9dc`](#insn-00ace9dc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace9e8`](#insn-00ace9e8) → `002add02`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ace9ec`](#insn-00ace9ec) → `Stack[-0x57]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace9f4`](#insn-00ace9f4) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ace9f8`](#insn-00ace9f8) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acea04`](#insn-00acea04) → `002a84dd`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acea08`](#insn-00acea08) → `002a84e2`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acea0c`](#insn-00acea0c) → `Stack[-0x6a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acea10`](#insn-00acea10) → `Stack[-0x77]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acea14`](#insn-00acea14) → `Stack[-0x72]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acea1c`](#insn-00acea1c) → `00c24f40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acea30`](#insn-00acea30) → [`0045b734`](../0045b/0045b734.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045b734` · 推定シンボル `None` · 推定型 `None`
- [`00acea34`](#insn-00acea34) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acea3c`](#insn-00acea3c) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acea44`](#insn-00acea44) → [`00acea70`](#insn-00acea70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acea50`](#insn-00acea50) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00acea54`](#insn-00acea54) → [`00acea70`](#insn-00acea70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acea6c`](#insn-00acea6c) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00acea70`](#insn-00acea70) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acea74`](#insn-00acea74) → [`00aceaa0`](#insn-00aceaa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acea80`](#insn-00acea80) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00acea84`](#insn-00acea84) → [`00aceaa0`](#insn-00aceaa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acea9c`](#insn-00acea9c) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00aceaa0`](#insn-00aceaa0) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aceaa4`](#insn-00aceaa4) → [`00aceab0`](#insn-00aceab0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aceaa8`](#insn-00aceaa8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aceaac`](#insn-00aceaac) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aceab0`](#insn-00aceab0) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aceab4`](#insn-00aceab4) → [`00aceac0`](#insn-00aceac0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aceab8`](#insn-00aceab8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aceabc`](#insn-00aceabc) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aceac8`](#insn-00aceac8) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acead0`](#insn-00acead0) → [`00acf35c`](#insn-00acf35c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acead4`](#insn-00acead4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acead8`](#insn-00acead8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aceadc`](#insn-00aceadc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aceae0`](#insn-00aceae0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aceaec`](#insn-00aceaec) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aceaf4`](#insn-00aceaf4) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aceb00`](#insn-00aceb00) → `0033a22c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aceb10`](#insn-00aceb10) → `00335e22`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[63]`
- [`00aceb14`](#insn-00aceb14) → `00335e25`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[63]`
- [`00aceb18`](#insn-00aceb18) → `00335e24`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[63]`
- [`00aceb1c`](#insn-00aceb1c) → `00335e21`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[63]`
- [`00aceb24`](#insn-00aceb24) → `00335e23`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[63]`
- [`00aceb30`](#insn-00aceb30) → `00335e26`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[63]`
- [`00aceb38`](#insn-00aceb38) → `00335e20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[63]`
- [`00aceb3c`](#insn-00aceb3c) → `00335e27`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[63]`
- [`00aceb50`](#insn-00aceb50) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aceb58`](#insn-00aceb58) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aceb5c`](#insn-00aceb5c) → `0033a22c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aceb6c`](#insn-00aceb6c) → [`00aced20`](#insn-00aced20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aceb74`](#insn-00aceb74) → [`006f18c4`](../006f1/006f18c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006f18c4` · 推定シンボル `None` · 推定型 `None`
- [`00aceb78`](#insn-00aceb78) → [`00acec3c`](#insn-00acec3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aceb7c`](#insn-00aceb7c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aceb84`](#insn-00aceb84) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aceb90`](#insn-00aceb90) → `0033a22c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aceba0`](#insn-00aceba0) → [`006f18c4`](../006f1/006f18c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006f18c4` · 推定シンボル `None` · 推定型 `None`
- [`00aceba8`](#insn-00aceba8) → [`00acec3c`](#insn-00acec3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acebac`](#insn-00acebac) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acebb4`](#insn-00acebb4) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acebc0`](#insn-00acebc0) → `0033a22c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00acebd0`](#insn-00acebd0) → [`006f18c4`](../006f1/006f18c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006f18c4` · 推定シンボル `None` · 推定型 `None`
- [`00acebd8`](#insn-00acebd8) → [`00acec3c`](#insn-00acec3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acebdc`](#insn-00acebdc) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acebe4`](#insn-00acebe4) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acebf0`](#insn-00acebf0) → `0033a22c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00acec00`](#insn-00acec00) → [`006f18c4`](../006f1/006f18c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006f18c4` · 推定シンボル `None` · 推定型 `None`
- [`00acec08`](#insn-00acec08) → [`00acec3c`](#insn-00acec3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acec0c`](#insn-00acec0c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acec14`](#insn-00acec14) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acec20`](#insn-00acec20) → `0033a22c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00acec30`](#insn-00acec30) → [`006f18c4`](../006f1/006f18c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006f18c4` · 推定シンボル `None` · 推定型 `None`
- [`00acec38`](#insn-00acec38) → [`00aceea4`](#insn-00aceea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acec3c`](#insn-00acec3c) → [`005bdd1c`](../005bd/005bdd1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005bdd1c` · 推定シンボル `None` · 推定型 `None`
- [`00acec48`](#insn-00acec48) → `0029613d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acec50`](#insn-00acec50) → [`0041b298`](../0041b/0041b298.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041b298` · 推定シンボル `None` · 推定型 `None`
- [`00acec54`](#insn-00acec54) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acec5c`](#insn-00acec5c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acec70`](#insn-00acec70) → `0033a22c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00acec78`](#insn-00acec78) → `00335a20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`00acec80`](#insn-00acec80) → `00293a68`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acec88`](#insn-00acec88) → [`0041b298`](../0041b/0041b298.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041b298` · 推定シンボル `None` · 推定型 `None`
- [`00acec94`](#insn-00acec94) → [`00469f7c`](../00469/00469f7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469f7c` · 推定シンボル `None` · 推定型 `None`
- [`00aceca8`](#insn-00aceca8) → [`008d5d88`](../008d5/008d5d88.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008d5d88` · 推定シンボル `None` · 推定型 `None`
- [`00acecb4`](#insn-00acecb4) → [`00469f7c`](../00469/00469f7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469f7c` · 推定シンボル `None` · 推定型 `None`
- [`00acecbc`](#insn-00acecbc) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acecc4`](#insn-00acecc4) → [`0041b298`](../0041b/0041b298.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041b298` · 推定シンボル `None` · 推定型 `None`
- [`00acecdc`](#insn-00acecdc) → [`0045b734`](../0045b/0045b734.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045b734` · 推定シンボル `None` · 推定型 `None`
- [`00acece8`](#insn-00acece8) → [`005bdd9c`](../005bd/005bdd9c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005bdd9c` · 推定シンボル `None` · 推定型 `None`
- [`00acecf0`](#insn-00acecf0) → [`0044b660`](../0044b/0044b660.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0044b660` · 推定シンボル `None` · 推定型 `None`
- [`00acecf4`](#insn-00acecf4) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acecf8`](#insn-00acecf8) → [`00acee24`](#insn-00acee24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acecfc`](#insn-00acecfc) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aced00`](#insn-00aced00) → [`00acee34`](#insn-00acee34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aced04`](#insn-00aced04) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aced08`](#insn-00aced08) → [`00acee44`](#insn-00acee44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aced0c`](#insn-00aced0c) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aced10`](#insn-00aced10) → [`00acee54`](#insn-00acee54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aced14`](#insn-00aced14) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aced18`](#insn-00aced18) → [`00acee64`](#insn-00acee64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aced1c`](#insn-00aced1c) → [`00acee94`](#insn-00acee94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aced24`](#insn-00aced24) → [`006f18c4`](../006f1/006f18c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006f18c4` · 推定シンボル `None` · 推定型 `None`
- [`00aced2c`](#insn-00aced2c) → [`00aceac0`](#insn-00aceac0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aced30`](#insn-00aced30) → [`005bdd1c`](../005bd/005bdd1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005bdd1c` · 推定シンボル `None` · 推定型 `None`
- [`00aced3c`](#insn-00aced3c) → `0029e637`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aced44`](#insn-00aced44) → [`0041b298`](../0041b/0041b298.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041b298` · 推定シンボル `None` · 推定型 `None`
- [`00aced48`](#insn-00aced48) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aced50`](#insn-00aced50) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aced5c`](#insn-00aced5c) → `0033a22c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aced6c`](#insn-00aced6c) → [`006f18c4`](../006f1/006f18c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006f18c4` · 推定シンボル `None` · 推定型 `None`
- [`00aced70`](#insn-00aced70) → [`006f3104`](../006f3/006f3104.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006f3104` · 推定シンボル `None` · 推定型 `None`
- [`00aced84`](#insn-00aced84) → [`004253b4`](../00425/004253b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004253b4` · 推定シンボル `None` · 推定型 `None`
- [`00aced90`](#insn-00aced90) → [`00469f7c`](../00469/00469f7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469f7c` · 推定シンボル `None` · 推定型 `None`
- [`00aced98`](#insn-00aced98) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aceda0`](#insn-00aceda0) → [`0041b298`](../0041b/0041b298.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041b298` · 推定シンボル `None` · 推定型 `None`
- [`00acedb8`](#insn-00acedb8) → [`0045b734`](../0045b/0045b734.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045b734` · 推定シンボル `None` · 推定型 `None`
- [`00acedc4`](#insn-00acedc4) → [`005bdd9c`](../005bd/005bdd9c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005bdd9c` · 推定シンボル `None` · 推定型 `None`
- [`00acedcc`](#insn-00acedcc) → [`0044b660`](../0044b/0044b660.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0044b660` · 推定シンボル `None` · 推定型 `None`
- [`00acedd0`](#insn-00acedd0) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acedd4`](#insn-00acedd4) → [`00acee6c`](#insn-00acee6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acedd8`](#insn-00acedd8) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aceddc`](#insn-00aceddc) → [`00acee7c`](#insn-00acee7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acede0`](#insn-00acede0) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acede4`](#insn-00acede4) → [`00acee8c`](#insn-00acee8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acede8`](#insn-00acede8) → [`00acee94`](#insn-00acee94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acedec`](#insn-00acedec) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acedf0`](#insn-00acedf0) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acedf4`](#insn-00acedf4) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acedf8`](#insn-00acedf8) → [`00ace7a0`](#insn-00ace7a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acedfc`](#insn-00acedfc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee00`](#insn-00acee00) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acee04`](#insn-00acee04) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee08`](#insn-00acee08) → [`00ace7a8`](#insn-00ace7a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee0c`](#insn-00acee0c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee10`](#insn-00acee10) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acee14`](#insn-00acee14) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee18`](#insn-00acee18) → [`00acee94`](#insn-00acee94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee1c`](#insn-00acee1c) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee20`](#insn-00acee20) → [`00acee90`](#insn-00acee90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee24`](#insn-00acee24) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee28`](#insn-00acee28) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acee2c`](#insn-00acee2c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee30`](#insn-00acee30) → [`00aced04`](#insn-00aced04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee34`](#insn-00acee34) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee38`](#insn-00acee38) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acee3c`](#insn-00acee3c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee40`](#insn-00acee40) → [`00aced0c`](#insn-00aced0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee44`](#insn-00acee44) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee48`](#insn-00acee48) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acee4c`](#insn-00acee4c) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee50`](#insn-00acee50) → [`00aced14`](#insn-00aced14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee54`](#insn-00acee54) → `Stack[-0xd8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee58`](#insn-00acee58) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acee5c`](#insn-00acee5c) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee60`](#insn-00acee60) → [`00acee94`](#insn-00acee94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee64`](#insn-00acee64) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee68`](#insn-00acee68) → [`00acee90`](#insn-00acee90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee6c`](#insn-00acee6c) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee70`](#insn-00acee70) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acee74`](#insn-00acee74) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee78`](#insn-00acee78) → [`00acede0`](#insn-00acede0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee7c`](#insn-00acee7c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee80`](#insn-00acee80) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acee84`](#insn-00acee84) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee88`](#insn-00acee88) → [`00acee94`](#insn-00acee94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee8c`](#insn-00acee8c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee90`](#insn-00acee90) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acee94`](#insn-00acee94) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee98`](#insn-00acee98) → [`00aceac0`](#insn-00aceac0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee9c`](#insn-00acee9c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aceea0`](#insn-00aceea0) → [`00aceabc`](#insn-00aceabc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aceea4`](#insn-00aceea4) → [`005bdd1c`](../005bd/005bdd1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005bdd1c` · 推定シンボル `None` · 推定型 `None`
- [`00aceeb0`](#insn-00aceeb0) → `0029113c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aceeb8`](#insn-00aceeb8) → [`0041b298`](../0041b/0041b298.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041b298` · 推定シンボル `None` · 推定型 `None`
- [`00aceebc`](#insn-00aceebc) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aceec4`](#insn-00aceec4) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aceed8`](#insn-00aceed8) → `0033a22c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aceee0`](#insn-00aceee0) → `00335a20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`00aceef0`](#insn-00aceef0) → [`008eccc4`](../008ec/008eccc4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008eccc4` · 推定シンボル `None` · 推定型 `None`
- [`00aceefc`](#insn-00aceefc) → [`00469f7c`](../00469/00469f7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469f7c` · 推定シンボル `None` · 推定型 `None`
- [`00acef04`](#insn-00acef04) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acef0c`](#insn-00acef0c) → [`0041b298`](../0041b/0041b298.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041b298` · 推定シンボル `None` · 推定型 `None`
- [`00acef24`](#insn-00acef24) → [`0045b734`](../0045b/0045b734.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045b734` · 推定シンボル `None` · 推定型 `None`
- [`00acef28`](#insn-00acef28) → [`00acedbc`](#insn-00acedbc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acef30`](#insn-00acef30) → `00c24f78`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acef34`](#insn-00acef34) → [`00bdaf00`](../00bda/00bdaf00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf00` · 推定シンボル `None` · 推定型 `None`
- [`00acef38`](#insn-00acef38) → [`00ace840`](#insn-00ace840) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acef40`](#insn-00acef40) → `00c24f40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acef48`](#insn-00acef48) → [`0045bedc`](../0045b/0045bedc.md) · `PARAM` · `ANALYSIS` · 関数 `0045bedc` · 推定シンボル `None` · 推定型 `None`
- [`00acef54`](#insn-00acef54) → `00be5ed0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acef58`](#insn-00acef58) → `00c24f48`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acef5c`](#insn-00acef5c) → `00c24f40`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acef5c`](#insn-00acef5c) → `00c24f48`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acef64`](#insn-00acef64) → `00c24f68`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acef64`](#insn-00acef64) → `00c24f70`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acef68`](#insn-00acef68) → `00c24f60`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acef6c`](#insn-00acef6c) → `00c24f50`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acef6c`](#insn-00acef6c) → `00c24f58`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acef6c`](#insn-00acef6c) → `00c24f60`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acef70`](#insn-00acef70) → [`00bdaee0`](../00bda/00bdaee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaee0` · 推定シンボル `None` · 推定型 `None`
- [`00acef78`](#insn-00acef78) → `00c24f78`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acef7c`](#insn-00acef7c) → [`00bdaf20`](../00bda/00bdaf20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf20` · 推定シンボル `None` · 推定型 `None`
- [`00acef80`](#insn-00acef80) → [`00ace840`](#insn-00ace840) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acef88`](#insn-00acef88) → `00c24f78`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acef8c`](#insn-00acef8c) → [`00bdaf00`](../00bda/00bdaf00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf00` · 推定シンボル `None` · 推定型 `None`
- [`00acef90`](#insn-00acef90) → [`00ace548`](#insn-00ace548) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acef98`](#insn-00acef98) → `00c24f40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acefa0`](#insn-00acefa0) → [`0045bedc`](../0045b/0045bedc.md) · `PARAM` · `ANALYSIS` · 関数 `0045bedc` · 推定シンボル `None` · 推定型 `None`
- [`00acefac`](#insn-00acefac) → `00be5ed0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acefb0`](#insn-00acefb0) → `00c24f48`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acefb4`](#insn-00acefb4) → `00c24f40`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acefb4`](#insn-00acefb4) → `00c24f48`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acefbc`](#insn-00acefbc) → `00c24f68`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acefbc`](#insn-00acefbc) → `00c24f70`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acefc0`](#insn-00acefc0) → `00c24f60`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acefc4`](#insn-00acefc4) → `00c24f50`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acefc4`](#insn-00acefc4) → `00c24f58`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acefc4`](#insn-00acefc4) → `00c24f60`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acefc8`](#insn-00acefc8) → [`00bdaee0`](../00bda/00bdaee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaee0` · 推定シンボル `None` · 推定型 `None`
- [`00acefd0`](#insn-00acefd0) → `00c24f78`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acefd4`](#insn-00acefd4) → [`00bdaf20`](../00bda/00bdaf20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf20` · 推定シンボル `None` · 推定型 `None`
- [`00acefd8`](#insn-00acefd8) → [`00ace548`](#insn-00ace548) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acefe0`](#insn-00acefe0) → `00c24f78`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acefe4`](#insn-00acefe4) → [`00bdaf00`](../00bda/00bdaf00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf00` · 推定シンボル `None` · 推定型 `None`
- [`00acefe8`](#insn-00acefe8) → [`00ace960`](#insn-00ace960) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aceff0`](#insn-00aceff0) → `00c24f40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aceff8`](#insn-00aceff8) → [`0045bedc`](../0045b/0045bedc.md) · `PARAM` · `ANALYSIS` · 関数 `0045bedc` · 推定シンボル `None` · 推定型 `None`
- [`00acf004`](#insn-00acf004) → `00be5ed0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acf008`](#insn-00acf008) → `00c24f48`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf00c`](#insn-00acf00c) → `00c24f40`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf00c`](#insn-00acf00c) → `00c24f48`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf014`](#insn-00acf014) → `00c24f68`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf014`](#insn-00acf014) → `00c24f70`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf018`](#insn-00acf018) → `00c24f60`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf01c`](#insn-00acf01c) → `00c24f50`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf01c`](#insn-00acf01c) → `00c24f58`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf01c`](#insn-00acf01c) → `00c24f60`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf020`](#insn-00acf020) → [`00bdaee0`](../00bda/00bdaee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaee0` · 推定シンボル `None` · 推定型 `None`
- [`00acf028`](#insn-00acf028) → `00c24f78`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acf02c`](#insn-00acf02c) → [`00bdaf20`](../00bda/00bdaf20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf20` · 推定シンボル `None` · 推定型 `None`
- [`00acf030`](#insn-00acf030) → [`00ace960`](#insn-00ace960) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf038`](#insn-00acf038) → `00c24f78`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acf03c`](#insn-00acf03c) → [`00bdaf00`](../00bda/00bdaf00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf00` · 推定シンボル `None` · 推定型 `None`
- [`00acf040`](#insn-00acf040) → [`00ace9d0`](#insn-00ace9d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf048`](#insn-00acf048) → `00c24f40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf050`](#insn-00acf050) → [`0045bedc`](../0045b/0045bedc.md) · `PARAM` · `ANALYSIS` · 関数 `0045bedc` · 推定シンボル `None` · 推定型 `None`
- [`00acf05c`](#insn-00acf05c) → `00be5ed0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acf060`](#insn-00acf060) → `00c24f48`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf064`](#insn-00acf064) → `00c24f40`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf064`](#insn-00acf064) → `00c24f48`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf06c`](#insn-00acf06c) → `00c24f68`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf06c`](#insn-00acf06c) → `00c24f70`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf070`](#insn-00acf070) → `00c24f60`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf074`](#insn-00acf074) → `00c24f50`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf074`](#insn-00acf074) → `00c24f58`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf074`](#insn-00acf074) → `00c24f60`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf078`](#insn-00acf078) → [`00bdaee0`](../00bda/00bdaee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaee0` · 推定シンボル `None` · 推定型 `None`
- [`00acf080`](#insn-00acf080) → `00c24f78`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acf084`](#insn-00acf084) → [`00bdaf20`](../00bda/00bdaf20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf20` · 推定シンボル `None` · 推定型 `None`
- [`00acf088`](#insn-00acf088) → [`00ace9d0`](#insn-00ace9d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf090`](#insn-00acf090) → `00c24f78`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acf094`](#insn-00acf094) → [`00bdaf00`](../00bda/00bdaf00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf00` · 推定シンボル `None` · 推定型 `None`
- [`00acf098`](#insn-00acf098) → [`00ace658`](#insn-00ace658) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf0a0`](#insn-00acf0a0) → `00c24f40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf0a8`](#insn-00acf0a8) → [`0045bedc`](../0045b/0045bedc.md) · `PARAM` · `ANALYSIS` · 関数 `0045bedc` · 推定シンボル `None` · 推定型 `None`
- [`00acf0b4`](#insn-00acf0b4) → `00be5ed0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acf0b8`](#insn-00acf0b8) → `00c24f48`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf0bc`](#insn-00acf0bc) → `00c24f40`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf0bc`](#insn-00acf0bc) → `00c24f48`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf0c4`](#insn-00acf0c4) → `00c24f68`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf0c4`](#insn-00acf0c4) → `00c24f70`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf0c8`](#insn-00acf0c8) → `00c24f60`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf0cc`](#insn-00acf0cc) → `00c24f50`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf0cc`](#insn-00acf0cc) → `00c24f58`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf0cc`](#insn-00acf0cc) → `00c24f60`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf0d0`](#insn-00acf0d0) → [`00bdaee0`](../00bda/00bdaee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaee0` · 推定シンボル `None` · 推定型 `None`
- [`00acf0d8`](#insn-00acf0d8) → `00c24f78`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acf0dc`](#insn-00acf0dc) → [`00bdaf20`](../00bda/00bdaf20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf20` · 推定シンボル `None` · 推定型 `None`
- [`00acf0e0`](#insn-00acf0e0) → [`00ace658`](#insn-00ace658) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf0e8`](#insn-00acf0e8) → `00c24f78`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acf0ec`](#insn-00acf0ec) → [`00bdaf00`](../00bda/00bdaf00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf00` · 推定シンボル `None` · 推定型 `None`
- [`00acf0f0`](#insn-00acf0f0) → [`00ace8e4`](#insn-00ace8e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf0f8`](#insn-00acf0f8) → `00c24f40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf100`](#insn-00acf100) → [`0045bedc`](../0045b/0045bedc.md) · `PARAM` · `ANALYSIS` · 関数 `0045bedc` · 推定シンボル `None` · 推定型 `None`
- [`00acf10c`](#insn-00acf10c) → `00be5ed0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acf110`](#insn-00acf110) → `00c24f48`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf114`](#insn-00acf114) → `00c24f40`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf114`](#insn-00acf114) → `00c24f48`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf11c`](#insn-00acf11c) → `00c24f68`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf11c`](#insn-00acf11c) → `00c24f70`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf120`](#insn-00acf120) → `00c24f60`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf124`](#insn-00acf124) → `00c24f50`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf124`](#insn-00acf124) → `00c24f58`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf124`](#insn-00acf124) → `00c24f60`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acf128`](#insn-00acf128) → [`00bdaee0`](../00bda/00bdaee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaee0` · 推定シンボル `None` · 推定型 `None`
- [`00acf130`](#insn-00acf130) → `00c24f78`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00acf134`](#insn-00acf134) → [`00bdaf20`](../00bda/00bdaf20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf20` · 推定シンボル `None` · 推定型 `None`
- [`00acf138`](#insn-00acf138) → [`00ace8e4`](#insn-00ace8e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf35c`](#insn-00acf35c) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ace4d0`](#insn-00ace4d0)

~~~json
{
  "source": "00ace4d0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace4d4`](#insn-00ace4d4)

~~~json
{
  "source": "00ace4d4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace4d8`](#insn-00ace4d8)

~~~json
{
  "source": "00ace4d8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace4dc`](#insn-00ace4dc)

~~~json
{
  "source": "00ace4dc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace500`](#insn-00ace500)

~~~json
{
  "source": "00ace500",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace504`](#insn-00ace504)

~~~json
{
  "source": "00ace504",
  "target": "00ace518",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace50c`](#insn-00ace50c)

~~~json
{
  "source": "00ace50c",
  "target": "00ace518",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace510`](#insn-00ace510)

~~~json
{
  "source": "00ace510",
  "target": "00467d20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace514`](#insn-00ace514)

~~~json
{
  "source": "00ace514",
  "target": "00aceac0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace520`](#insn-00ace520)

~~~json
{
  "source": "00ace520",
  "target": "00ace5b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace524`](#insn-00ace524)

~~~json
{
  "source": "00ace524",
  "target": "00ace7b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace52c`](#insn-00ace52c)

~~~json
{
  "source": "00ace52c",
  "target": "00ace8a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace534`](#insn-00ace534)

~~~json
{
  "source": "00ace534",
  "target": "00aceac0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace540`](#insn-00ace540)

~~~json
{
  "source": "00ace540",
  "target": "00c24f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ace544`](#insn-00ace544)

~~~json
{
  "source": "00ace544",
  "target": "00acef84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace550`](#insn-00ace550)

~~~json
{
  "source": "00ace550",
  "target": "Stack[-0x55]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace554`](#insn-00ace554)

~~~json
{
  "source": "00ace554",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace560`](#insn-00ace560)

~~~json
{
  "source": "00ace560",
  "target": "00294b68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00294b68",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "696d673130322e706e6700",
  "capture_start": "00294b68",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ace564`](#insn-00ace564)

~~~json
{
  "source": "00ace564",
  "target": "Stack[-0x57]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace56c`](#insn-00ace56c)

~~~json
{
  "source": "00ace56c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace570`](#insn-00ace570)

~~~json
{
  "source": "00ace570",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace57c`](#insn-00ace57c)

~~~json
{
  "source": "00ace57c",
  "target": "002acb6e",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace580`](#insn-00ace580)

~~~json
{
  "source": "00ace580",
  "target": "002acb73",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002acb73",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "322e696d6763757400",
  "capture_start": "002acb73",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ace584`](#insn-00ace584)

~~~json
{
  "source": "00ace584",
  "target": "Stack[-0x6a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace588`](#insn-00ace588)

~~~json
{
  "source": "00ace588",
  "target": "Stack[-0x77]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace58c`](#insn-00ace58c)

~~~json
{
  "source": "00ace58c",
  "target": "Stack[-0x72]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace594`](#insn-00ace594)

~~~json
{
  "source": "00ace594",
  "target": "00c24f40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ace5a8`](#insn-00ace5a8)

~~~json
{
  "source": "00ace5a8",
  "target": "0045b734",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace5ac`](#insn-00ace5ac)

~~~json
{
  "source": "00ace5ac",
  "target": "00acea34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace5b4`](#insn-00ace5b4)

~~~json
{
  "source": "00ace5b4",
  "target": "00ace830",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace5bc`](#insn-00ace5bc)

~~~json
{
  "source": "00ace5bc",
  "target": "00ace950",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace5c4`](#insn-00ace5c4)

~~~json
{
  "source": "00ace5c4",
  "target": "00aceac0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace5c8`](#insn-00ace5c8)

~~~json
{
  "source": "00ace5c8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace5d4`](#insn-00ace5d4)

~~~json
{
  "source": "00ace5d4",
  "target": "00331eaa",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00331ea1",
  "offset": 9,
  "size": 43,
  "datatype": "byte[43]",
  "bytes": "440e40500c1d409302940495069608970a980c9e0e9d100a0360010c1f40500e",
  "capture_start": "00331ea1",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ace5d8`](#insn-00ace5d8)

~~~json
{
  "source": "00ace5d8",
  "target": "00aceac0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace5dc`](#insn-00ace5dc)

~~~json
{
  "source": "00ace5dc",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace5e4`](#insn-00ace5e4)

~~~json
{
  "source": "00ace5e4",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace5f0`](#insn-00ace5f0)

~~~json
{
  "source": "00ace5f0",
  "target": "0033a22c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033a22c",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "34ed0000",
  "capture_start": "0033a22c",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ace600`](#insn-00ace600)

~~~json
{
  "source": "00ace600",
  "target": "00335e22",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335e09",
  "offset": 25,
  "size": 63,
  "datatype": "byte[63]",
  "bytes": "440e50540c1d509302940495069608970a980c99109e129d140a0354010c1f50",
  "capture_start": "00335e09",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ace604`](#insn-00ace604)

~~~json
{
  "source": "00ace604",
  "target": "00335e25",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335e09",
  "offset": 28,
  "size": 63,
  "datatype": "byte[63]",
  "bytes": "440e50540c1d509302940495069608970a980c99109e129d140a0354010c1f50",
  "capture_start": "00335e09",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ace608`](#insn-00ace608)

~~~json
{
  "source": "00ace608",
  "target": "00335e24",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335e09",
  "offset": 27,
  "size": 63,
  "datatype": "byte[63]",
  "bytes": "440e50540c1d509302940495069608970a980c99109e129d140a0354010c1f50",
  "capture_start": "00335e09",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ace60c`](#insn-00ace60c)

~~~json
{
  "source": "00ace60c",
  "target": "00335e21",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335e09",
  "offset": 24,
  "size": 63,
  "datatype": "byte[63]",
  "bytes": "440e50540c1d509302940495069608970a980c99109e129d140a0354010c1f50",
  "capture_start": "00335e09",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ace614`](#insn-00ace614)

~~~json
{
  "source": "00ace614",
  "target": "00335e23",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335e09",
  "offset": 26,
  "size": 63,
  "datatype": "byte[63]",
  "bytes": "440e50540c1d509302940495069608970a980c99109e129d140a0354010c1f50",
  "capture_start": "00335e09",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ace620`](#insn-00ace620)

~~~json
{
  "source": "00ace620",
  "target": "00335e26",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335e09",
  "offset": 29,
  "size": 63,
  "datatype": "byte[63]",
  "bytes": "440e50540c1d509302940495069608970a980c99109e129d140a0354010c1f50",
  "capture_start": "00335e09",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ace628`](#insn-00ace628)

~~~json
{
  "source": "00ace628",
  "target": "00335e20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335e09",
  "offset": 23,
  "size": 63,
  "datatype": "byte[63]",
  "bytes": "440e50540c1d509302940495069608970a980c99109e129d140a0354010c1f50",
  "capture_start": "00335e09",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ace62c`](#insn-00ace62c)

~~~json
{
  "source": "00ace62c",
  "target": "00335e27",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335e09",
  "offset": 30,
  "size": 63,
  "datatype": "byte[63]",
  "bytes": "440e50540c1d509302940495069608970a980c99109e129d140a0354010c1f50",
  "capture_start": "00335e09",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ace644`](#insn-00ace644)

~~~json
{
  "source": "00ace644",
  "target": "00aceaec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace650`](#insn-00ace650)

~~~json
{
  "source": "00ace650",
  "target": "00c24f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ace654`](#insn-00ace654)

~~~json
{
  "source": "00ace654",
  "target": "00acf08c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace660`](#insn-00ace660)

~~~json
{
  "source": "00ace660",
  "target": "Stack[-0x89]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace668`](#insn-00ace668)

~~~json
{
  "source": "00ace668",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace670`](#insn-00ace670)

~~~json
{
  "source": "00ace670",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace674`](#insn-00ace674)

~~~json
{
  "source": "00ace674",
  "target": "Stack[-0x8b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace678`](#insn-00ace678)

~~~json
{
  "source": "00ace678",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace680`](#insn-00ace680)

~~~json
{
  "source": "00ace680",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace68c`](#insn-00ace68c)

~~~json
{
  "source": "00ace68c",
  "target": "0033a22c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033a22c",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "34ed0000",
  "capture_start": "0033a22c",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ace69c`](#insn-00ace69c)

~~~json
{
  "source": "00ace69c",
  "target": "00335a22",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335a05",
  "offset": 29,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440e20480c1d2093049e069d080a640c1f20480e00d3dedd440b440c1f20480e",
  "capture_start": "00335a05",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ace6a0`](#insn-00ace6a0)

~~~json
{
  "source": "00ace6a0",
  "target": "00335a25",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335a05",
  "offset": 32,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440e20480c1d2093049e069d080a640c1f20480e00d3dedd440b440c1f20480e",
  "capture_start": "00335a05",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ace6a4`](#insn-00ace6a4)

~~~json
{
  "source": "00ace6a4",
  "target": "00335a24",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335a05",
  "offset": 31,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440e20480c1d2093049e069d080a640c1f20480e00d3dedd440b440c1f20480e",
  "capture_start": "00335a05",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ace6a8`](#insn-00ace6a8)

~~~json
{
  "source": "00ace6a8",
  "target": "00335a21",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335a05",
  "offset": 28,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440e20480c1d2093049e069d080a640c1f20480e00d3dedd440b440c1f20480e",
  "capture_start": "00335a05",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ace6b0`](#insn-00ace6b0)

~~~json
{
  "source": "00ace6b0",
  "target": "00335a23",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335a05",
  "offset": 30,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440e20480c1d2093049e069d080a640c1f20480e00d3dedd440b440c1f20480e",
  "capture_start": "00335a05",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ace6bc`](#insn-00ace6bc)

~~~json
{
  "source": "00ace6bc",
  "target": "00335a26",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335a05",
  "offset": 33,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440e20480c1d2093049e069d080a640c1f20480e00d3dedd440b440c1f20480e",
  "capture_start": "00335a05",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ace6c4`](#insn-00ace6c4)

~~~json
{
  "source": "00ace6c4",
  "target": "00335a20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335a05",
  "offset": 27,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440e20480c1d2093049e069d080a640c1f20480e00d3dedd440b440c1f20480e",
  "capture_start": "00335a05",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ace6c8`](#insn-00ace6c8)

~~~json
{
  "source": "00ace6c8",
  "target": "00335a27",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335a05",
  "offset": 34,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440e20480c1d2093049e069d080a640c1f20480e00d3dedd440b440c1f20480e",
  "capture_start": "00335a05",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ace6e4`](#insn-00ace6e4)

~~~json
{
  "source": "00ace6e4",
  "target": "0064104c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace6f4`](#insn-00ace6f4)

~~~json
{
  "source": "00ace6f4",
  "target": "0046ff30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace700`](#insn-00ace700)

~~~json
{
  "source": "00ace700",
  "target": "00469f7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace704`](#insn-00ace704)

~~~json
{
  "source": "00ace704",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace70c`](#insn-00ace70c)

~~~json
{
  "source": "00ace70c",
  "target": "00c24f40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ace720`](#insn-00ace720)

~~~json
{
  "source": "00ace720",
  "target": "0045b734",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace724`](#insn-00ace724)

~~~json
{
  "source": "00ace724",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace72c`](#insn-00ace72c)

~~~json
{
  "source": "00ace72c",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace734`](#insn-00ace734)

~~~json
{
  "source": "00ace734",
  "target": "00ace760",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace740`](#insn-00ace740)

~~~json
{
  "source": "00ace740",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace744`](#insn-00ace744)

~~~json
{
  "source": "00ace744",
  "target": "00ace760",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace75c`](#insn-00ace75c)

~~~json
{
  "source": "00ace75c",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace760`](#insn-00ace760)

~~~json
{
  "source": "00ace760",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace764`](#insn-00ace764)

~~~json
{
  "source": "00ace764",
  "target": "00ace790",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace770`](#insn-00ace770)

~~~json
{
  "source": "00ace770",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace774`](#insn-00ace774)

~~~json
{
  "source": "00ace774",
  "target": "00ace790",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace78c`](#insn-00ace78c)

~~~json
{
  "source": "00ace78c",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace790`](#insn-00ace790)

~~~json
{
  "source": "00ace790",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace794`](#insn-00ace794)

~~~json
{
  "source": "00ace794",
  "target": "00acedec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace798`](#insn-00ace798)

~~~json
{
  "source": "00ace798",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace79c`](#insn-00ace79c)

~~~json
{
  "source": "00ace79c",
  "target": "00acedfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace7a0`](#insn-00ace7a0)

~~~json
{
  "source": "00ace7a0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace7a4`](#insn-00ace7a4)

~~~json
{
  "source": "00ace7a4",
  "target": "00acee0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace7a8`](#insn-00ace7a8)

~~~json
{
  "source": "00ace7a8",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace7ac`](#insn-00ace7ac)

~~~json
{
  "source": "00ace7ac",
  "target": "00acee1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace7b0`](#insn-00ace7b0)

~~~json
{
  "source": "00ace7b0",
  "target": "00acee94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace7b4`](#insn-00ace7b4)

~~~json
{
  "source": "00ace7b4",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace7bc`](#insn-00ace7bc)

~~~json
{
  "source": "00ace7bc",
  "target": "00830c98",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace7c0`](#insn-00ace7c0)

~~~json
{
  "source": "00ace7c0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace7c8`](#insn-00ace7c8)

~~~json
{
  "source": "00ace7c8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace7d0`](#insn-00ace7d0)

~~~json
{
  "source": "00ace7d0",
  "target": "00ace7fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace7dc`](#insn-00ace7dc)

~~~json
{
  "source": "00ace7dc",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace7e0`](#insn-00ace7e0)

~~~json
{
  "source": "00ace7e0",
  "target": "00ace7fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace7f8`](#insn-00ace7f8)

~~~json
{
  "source": "00ace7f8",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace7fc`](#insn-00ace7fc)

~~~json
{
  "source": "00ace7fc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace800`](#insn-00ace800)

~~~json
{
  "source": "00ace800",
  "target": "00aceac0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace80c`](#insn-00ace80c)

~~~json
{
  "source": "00ace80c",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace810`](#insn-00ace810)

~~~json
{
  "source": "00ace810",
  "target": "00aceac0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace828`](#insn-00ace828)

~~~json
{
  "source": "00ace828",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace82c`](#insn-00ace82c)

~~~json
{
  "source": "00ace82c",
  "target": "00aceac0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace838`](#insn-00ace838)

~~~json
{
  "source": "00ace838",
  "target": "00c24f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ace83c`](#insn-00ace83c)

~~~json
{
  "source": "00ace83c",
  "target": "00acef2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace848`](#insn-00ace848)

~~~json
{
  "source": "00ace848",
  "target": "Stack[-0x55]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace84c`](#insn-00ace84c)

~~~json
{
  "source": "00ace84c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace858`](#insn-00ace858)

~~~json
{
  "source": "00ace858",
  "target": "002a081f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a081f",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "696d673030312e706e6700",
  "capture_start": "002a081f",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ace85c`](#insn-00ace85c)

~~~json
{
  "source": "00ace85c",
  "target": "Stack[-0x57]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace864`](#insn-00ace864)

~~~json
{
  "source": "00ace864",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace868`](#insn-00ace868)

~~~json
{
  "source": "00ace868",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace874`](#insn-00ace874)

~~~json
{
  "source": "00ace874",
  "target": "0029b6af",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029b6af",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "696d673030312e69",
  "capture_start": "0029b6af",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ace878`](#insn-00ace878)

~~~json
{
  "source": "00ace878",
  "target": "0029b6b4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029b6af",
  "offset": 5,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "696d673030312e69",
  "capture_start": "0029b6af",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ace87c`](#insn-00ace87c)

~~~json
{
  "source": "00ace87c",
  "target": "Stack[-0x6a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace880`](#insn-00ace880)

~~~json
{
  "source": "00ace880",
  "target": "Stack[-0x77]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace884`](#insn-00ace884)

~~~json
{
  "source": "00ace884",
  "target": "Stack[-0x72]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace88c`](#insn-00ace88c)

~~~json
{
  "source": "00ace88c",
  "target": "00c24f40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ace8a0`](#insn-00ace8a0)

~~~json
{
  "source": "00ace8a0",
  "target": "0045b734",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace8a4`](#insn-00ace8a4)

~~~json
{
  "source": "00ace8a4",
  "target": "00acea34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace8a8`](#insn-00ace8a8)

~~~json
{
  "source": "00ace8a8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace8b4`](#insn-00ace8b4)

~~~json
{
  "source": "00ace8b4",
  "target": "0032ff0c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032fef1",
  "offset": 27,
  "size": 35,
  "datatype": "byte[35]",
  "bytes": "440e304c0c1d2093049e069d0805480a05490c02500c1f304c0e00d3dedd0648",
  "capture_start": "0032fef1",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ace8b8`](#insn-00ace8b8)

~~~json
{
  "source": "00ace8b8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace8c0`](#insn-00ace8c0)

~~~json
{
  "source": "00ace8c0",
  "target": "00ace9c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace8c4`](#insn-00ace8c4)

~~~json
{
  "source": "00ace8c4",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace8d0`](#insn-00ace8d0)

~~~json
{
  "source": "00ace8d0",
  "target": "00ace9c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace8dc`](#insn-00ace8dc)

~~~json
{
  "source": "00ace8dc",
  "target": "00c24f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ace8e0`](#insn-00ace8e0)

~~~json
{
  "source": "00ace8e0",
  "target": "00acf0e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace8f0`](#insn-00ace8f0)

~~~json
{
  "source": "00ace8f0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace8f8`](#insn-00ace8f8)

~~~json
{
  "source": "00ace8f8",
  "target": "002a4817",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a4817",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "696d673130315f6e656b6f446f6a6f2e706e6700",
  "capture_start": "002a4817",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ace900`](#insn-00ace900)

~~~json
{
  "source": "00ace900",
  "target": "Stack[-0x4c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace904`](#insn-00ace904)

~~~json
{
  "source": "00ace904",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace90c`](#insn-00ace90c)

~~~json
{
  "source": "00ace90c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace918`](#insn-00ace918)

~~~json
{
  "source": "00ace918",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace91c`](#insn-00ace91c)

~~~json
{
  "source": "00ace91c",
  "target": "002adceb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002adceb",
  "offset": 0,
  "size": 23,
  "datatype": "string",
  "bytes": "696d673130315f6e656b6f446f6a6f2e696d6763757400",
  "capture_start": "002adceb",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ace920`](#insn-00ace920)

~~~json
{
  "source": "00ace920",
  "target": "002adcf9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002adceb",
  "offset": 14,
  "size": 23,
  "datatype": "string",
  "bytes": "696d673130315f6e656b6f446f6a6f2e696d6763757400",
  "capture_start": "002adceb",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ace924`](#insn-00ace924)

~~~json
{
  "source": "00ace924",
  "target": "Stack[-0x61]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace928`](#insn-00ace928)

~~~json
{
  "source": "00ace928",
  "target": "Stack[-0x77]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace92c`](#insn-00ace92c)

~~~json
{
  "source": "00ace92c",
  "target": "Stack[-0x69]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace934`](#insn-00ace934)

~~~json
{
  "source": "00ace934",
  "target": "00c24f40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ace948`](#insn-00ace948)

~~~json
{
  "source": "00ace948",
  "target": "0045b734",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace94c`](#insn-00ace94c)

~~~json
{
  "source": "00ace94c",
  "target": "00acea34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace958`](#insn-00ace958)

~~~json
{
  "source": "00ace958",
  "target": "00c24f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ace95c`](#insn-00ace95c)

~~~json
{
  "source": "00ace95c",
  "target": "00acefdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace96c`](#insn-00ace96c)

~~~json
{
  "source": "00ace96c",
  "target": "002aeec9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aeec9",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "696d673035305f30312e706e6700",
  "capture_start": "002aeec9",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ace970`](#insn-00ace970)

~~~json
{
  "source": "00ace970",
  "target": "002aeece",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aeec9",
  "offset": 5,
  "size": 14,
  "datatype": "string",
  "bytes": "696d673035305f30312e706e6700",
  "capture_start": "002aeec9",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ace974`](#insn-00ace974)

~~~json
{
  "source": "00ace974",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace97c`](#insn-00ace97c)

~~~json
{
  "source": "00ace97c",
  "target": "Stack[-0x52]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace980`](#insn-00ace980)

~~~json
{
  "source": "00ace980",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace984`](#insn-00ace984)

~~~json
{
  "source": "00ace984",
  "target": "Stack[-0x5a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace990`](#insn-00ace990)

~~~json
{
  "source": "00ace990",
  "target": "002ade27",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ade27",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "696d673035305f30312e696d6763757400",
  "capture_start": "002ade27",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ace994`](#insn-00ace994)

~~~json
{
  "source": "00ace994",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace998`](#insn-00ace998)

~~~json
{
  "source": "00ace998",
  "target": "Stack[-0x67]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace99c`](#insn-00ace99c)

~~~json
{
  "source": "00ace99c",
  "target": "Stack[-0x77]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace9a4`](#insn-00ace9a4)

~~~json
{
  "source": "00ace9a4",
  "target": "00c24f40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ace9b8`](#insn-00ace9b8)

~~~json
{
  "source": "00ace9b8",
  "target": "0045b734",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ace9bc`](#insn-00ace9bc)

~~~json
{
  "source": "00ace9bc",
  "target": "00acea34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace9c8`](#insn-00ace9c8)

~~~json
{
  "source": "00ace9c8",
  "target": "00c24f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ace9cc`](#insn-00ace9cc)

~~~json
{
  "source": "00ace9cc",
  "target": "00acf034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace9d8`](#insn-00ace9d8)

~~~json
{
  "source": "00ace9d8",
  "target": "Stack[-0x55]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace9dc`](#insn-00ace9dc)

~~~json
{
  "source": "00ace9dc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace9e8`](#insn-00ace9e8)

~~~json
{
  "source": "00ace9e8",
  "target": "002add02",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002add02",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "696d673130312e706e6700",
  "capture_start": "002add02",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ace9ec`](#insn-00ace9ec)

~~~json
{
  "source": "00ace9ec",
  "target": "Stack[-0x57]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace9f4`](#insn-00ace9f4)

~~~json
{
  "source": "00ace9f4",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ace9f8`](#insn-00ace9f8)

~~~json
{
  "source": "00ace9f8",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acea04`](#insn-00acea04)

~~~json
{
  "source": "00acea04",
  "target": "002a84dd",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acea08`](#insn-00acea08)

~~~json
{
  "source": "00acea08",
  "target": "002a84e2",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a84e2",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "312e696d6763757400",
  "capture_start": "002a84e2",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acea0c`](#insn-00acea0c)

~~~json
{
  "source": "00acea0c",
  "target": "Stack[-0x6a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acea10`](#insn-00acea10)

~~~json
{
  "source": "00acea10",
  "target": "Stack[-0x77]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acea14`](#insn-00acea14)

~~~json
{
  "source": "00acea14",
  "target": "Stack[-0x72]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acea1c`](#insn-00acea1c)

~~~json
{
  "source": "00acea1c",
  "target": "00c24f40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acea30`](#insn-00acea30)

~~~json
{
  "source": "00acea30",
  "target": "0045b734",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acea34`](#insn-00acea34)

~~~json
{
  "source": "00acea34",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acea3c`](#insn-00acea3c)

~~~json
{
  "source": "00acea3c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acea44`](#insn-00acea44)

~~~json
{
  "source": "00acea44",
  "target": "00acea70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acea50`](#insn-00acea50)

~~~json
{
  "source": "00acea50",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acea54`](#insn-00acea54)

~~~json
{
  "source": "00acea54",
  "target": "00acea70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acea6c`](#insn-00acea6c)

~~~json
{
  "source": "00acea6c",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acea70`](#insn-00acea70)

~~~json
{
  "source": "00acea70",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acea74`](#insn-00acea74)

~~~json
{
  "source": "00acea74",
  "target": "00aceaa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acea80`](#insn-00acea80)

~~~json
{
  "source": "00acea80",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acea84`](#insn-00acea84)

~~~json
{
  "source": "00acea84",
  "target": "00aceaa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acea9c`](#insn-00acea9c)

~~~json
{
  "source": "00acea9c",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aceaa0`](#insn-00aceaa0)

~~~json
{
  "source": "00aceaa0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aceaa4`](#insn-00aceaa4)

~~~json
{
  "source": "00aceaa4",
  "target": "00aceab0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aceaa8`](#insn-00aceaa8)

~~~json
{
  "source": "00aceaa8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aceaac`](#insn-00aceaac)

~~~json
{
  "source": "00aceaac",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aceab0`](#insn-00aceab0)

~~~json
{
  "source": "00aceab0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aceab4`](#insn-00aceab4)

~~~json
{
  "source": "00aceab4",
  "target": "00aceac0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aceab8`](#insn-00aceab8)

~~~json
{
  "source": "00aceab8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aceabc`](#insn-00aceabc)

~~~json
{
  "source": "00aceabc",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aceac8`](#insn-00aceac8)

~~~json
{
  "source": "00aceac8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acead0`](#insn-00acead0)

~~~json
{
  "source": "00acead0",
  "target": "00acf35c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acead4`](#insn-00acead4)

~~~json
{
  "source": "00acead4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acead8`](#insn-00acead8)

~~~json
{
  "source": "00acead8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aceadc`](#insn-00aceadc)

~~~json
{
  "source": "00aceadc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aceae0`](#insn-00aceae0)

~~~json
{
  "source": "00aceae0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aceaec`](#insn-00aceaec)

~~~json
{
  "source": "00aceaec",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aceaf4`](#insn-00aceaf4)

~~~json
{
  "source": "00aceaf4",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aceb00`](#insn-00aceb00)

~~~json
{
  "source": "00aceb00",
  "target": "0033a22c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033a22c",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "34ed0000",
  "capture_start": "0033a22c",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aceb10`](#insn-00aceb10)

~~~json
{
  "source": "00aceb10",
  "target": "00335e22",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335e09",
  "offset": 25,
  "size": 63,
  "datatype": "byte[63]",
  "bytes": "440e50540c1d509302940495069608970a980c99109e129d140a0354010c1f50",
  "capture_start": "00335e09",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aceb14`](#insn-00aceb14)

~~~json
{
  "source": "00aceb14",
  "target": "00335e25",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335e09",
  "offset": 28,
  "size": 63,
  "datatype": "byte[63]",
  "bytes": "440e50540c1d509302940495069608970a980c99109e129d140a0354010c1f50",
  "capture_start": "00335e09",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aceb18`](#insn-00aceb18)

~~~json
{
  "source": "00aceb18",
  "target": "00335e24",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335e09",
  "offset": 27,
  "size": 63,
  "datatype": "byte[63]",
  "bytes": "440e50540c1d509302940495069608970a980c99109e129d140a0354010c1f50",
  "capture_start": "00335e09",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aceb1c`](#insn-00aceb1c)

~~~json
{
  "source": "00aceb1c",
  "target": "00335e21",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335e09",
  "offset": 24,
  "size": 63,
  "datatype": "byte[63]",
  "bytes": "440e50540c1d509302940495069608970a980c99109e129d140a0354010c1f50",
  "capture_start": "00335e09",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aceb24`](#insn-00aceb24)

~~~json
{
  "source": "00aceb24",
  "target": "00335e23",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335e09",
  "offset": 26,
  "size": 63,
  "datatype": "byte[63]",
  "bytes": "440e50540c1d509302940495069608970a980c99109e129d140a0354010c1f50",
  "capture_start": "00335e09",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aceb30`](#insn-00aceb30)

~~~json
{
  "source": "00aceb30",
  "target": "00335e26",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335e09",
  "offset": 29,
  "size": 63,
  "datatype": "byte[63]",
  "bytes": "440e50540c1d509302940495069608970a980c99109e129d140a0354010c1f50",
  "capture_start": "00335e09",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aceb38`](#insn-00aceb38)

~~~json
{
  "source": "00aceb38",
  "target": "00335e20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335e09",
  "offset": 23,
  "size": 63,
  "datatype": "byte[63]",
  "bytes": "440e50540c1d509302940495069608970a980c99109e129d140a0354010c1f50",
  "capture_start": "00335e09",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aceb3c`](#insn-00aceb3c)

~~~json
{
  "source": "00aceb3c",
  "target": "00335e27",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335e09",
  "offset": 30,
  "size": 63,
  "datatype": "byte[63]",
  "bytes": "440e50540c1d509302940495069608970a980c99109e129d140a0354010c1f50",
  "capture_start": "00335e09",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aceb50`](#insn-00aceb50)

~~~json
{
  "source": "00aceb50",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aceb58`](#insn-00aceb58)

~~~json
{
  "source": "00aceb58",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aceb5c`](#insn-00aceb5c)

~~~json
{
  "source": "00aceb5c",
  "target": "0033a22c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033a22c",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "34ed0000",
  "capture_start": "0033a22c",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aceb6c`](#insn-00aceb6c)

~~~json
{
  "source": "00aceb6c",
  "target": "00aced20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aceb74`](#insn-00aceb74)

~~~json
{
  "source": "00aceb74",
  "target": "006f18c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aceb78`](#insn-00aceb78)

~~~json
{
  "source": "00aceb78",
  "target": "00acec3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aceb7c`](#insn-00aceb7c)

~~~json
{
  "source": "00aceb7c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aceb84`](#insn-00aceb84)

~~~json
{
  "source": "00aceb84",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aceb90`](#insn-00aceb90)

~~~json
{
  "source": "00aceb90",
  "target": "0033a22c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033a22c",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "34ed0000",
  "capture_start": "0033a22c",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aceba0`](#insn-00aceba0)

~~~json
{
  "source": "00aceba0",
  "target": "006f18c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aceba8`](#insn-00aceba8)

~~~json
{
  "source": "00aceba8",
  "target": "00acec3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acebac`](#insn-00acebac)

~~~json
{
  "source": "00acebac",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acebb4`](#insn-00acebb4)

~~~json
{
  "source": "00acebb4",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acebc0`](#insn-00acebc0)

~~~json
{
  "source": "00acebc0",
  "target": "0033a22c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033a22c",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "34ed0000",
  "capture_start": "0033a22c",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acebd0`](#insn-00acebd0)

~~~json
{
  "source": "00acebd0",
  "target": "006f18c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acebd8`](#insn-00acebd8)

~~~json
{
  "source": "00acebd8",
  "target": "00acec3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acebdc`](#insn-00acebdc)

~~~json
{
  "source": "00acebdc",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acebe4`](#insn-00acebe4)

~~~json
{
  "source": "00acebe4",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acebf0`](#insn-00acebf0)

~~~json
{
  "source": "00acebf0",
  "target": "0033a22c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033a22c",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "34ed0000",
  "capture_start": "0033a22c",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acec00`](#insn-00acec00)

~~~json
{
  "source": "00acec00",
  "target": "006f18c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acec08`](#insn-00acec08)

~~~json
{
  "source": "00acec08",
  "target": "00acec3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acec0c`](#insn-00acec0c)

~~~json
{
  "source": "00acec0c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acec14`](#insn-00acec14)

~~~json
{
  "source": "00acec14",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acec20`](#insn-00acec20)

~~~json
{
  "source": "00acec20",
  "target": "0033a22c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033a22c",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "34ed0000",
  "capture_start": "0033a22c",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acec30`](#insn-00acec30)

~~~json
{
  "source": "00acec30",
  "target": "006f18c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acec38`](#insn-00acec38)

~~~json
{
  "source": "00acec38",
  "target": "00aceea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acec3c`](#insn-00acec3c)

~~~json
{
  "source": "00acec3c",
  "target": "005bdd1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acec48`](#insn-00acec48)

~~~json
{
  "source": "00acec48",
  "target": "0029613d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029613d",
  "offset": 0,
  "size": 24,
  "datatype": "string",
  "bytes": "67617479616974656d5f253032645f665f25402e706e6700",
  "capture_start": "0029613d",
  "capture_bytes": 24,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acec50`](#insn-00acec50)

~~~json
{
  "source": "00acec50",
  "target": "0041b298",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acec54`](#insn-00acec54)

~~~json
{
  "source": "00acec54",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acec5c`](#insn-00acec5c)

~~~json
{
  "source": "00acec5c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acec70`](#insn-00acec70)

~~~json
{
  "source": "00acec70",
  "target": "0033a22c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033a22c",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "34ed0000",
  "capture_start": "0033a22c",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acec78`](#insn-00acec78)

~~~json
{
  "source": "00acec78",
  "target": "00335a20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335a05",
  "offset": 27,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440e20480c1d2093049e069d080a640c1f20480e00d3dedd440b440c1f20480e",
  "capture_start": "00335a05",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acec80`](#insn-00acec80)

~~~json
{
  "source": "00acec80",
  "target": "00293a68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acec88`](#insn-00acec88)

~~~json
{
  "source": "00acec88",
  "target": "0041b298",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acec94`](#insn-00acec94)

~~~json
{
  "source": "00acec94",
  "target": "00469f7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aceca8`](#insn-00aceca8)

~~~json
{
  "source": "00aceca8",
  "target": "008d5d88",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acecb4`](#insn-00acecb4)

~~~json
{
  "source": "00acecb4",
  "target": "00469f7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acecbc`](#insn-00acecbc)

~~~json
{
  "source": "00acecbc",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acecc4`](#insn-00acecc4)

~~~json
{
  "source": "00acecc4",
  "target": "0041b298",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acecdc`](#insn-00acecdc)

~~~json
{
  "source": "00acecdc",
  "target": "0045b734",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acece8`](#insn-00acece8)

~~~json
{
  "source": "00acece8",
  "target": "005bdd9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acecf0`](#insn-00acecf0)

~~~json
{
  "source": "00acecf0",
  "target": "0044b660",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acecf4`](#insn-00acecf4)

~~~json
{
  "source": "00acecf4",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acecf8`](#insn-00acecf8)

~~~json
{
  "source": "00acecf8",
  "target": "00acee24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acecfc`](#insn-00acecfc)

~~~json
{
  "source": "00acecfc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aced00`](#insn-00aced00)

~~~json
{
  "source": "00aced00",
  "target": "00acee34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aced04`](#insn-00aced04)

~~~json
{
  "source": "00aced04",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aced08`](#insn-00aced08)

~~~json
{
  "source": "00aced08",
  "target": "00acee44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aced0c`](#insn-00aced0c)

~~~json
{
  "source": "00aced0c",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aced10`](#insn-00aced10)

~~~json
{
  "source": "00aced10",
  "target": "00acee54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aced14`](#insn-00aced14)

~~~json
{
  "source": "00aced14",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aced18`](#insn-00aced18)

~~~json
{
  "source": "00aced18",
  "target": "00acee64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aced1c`](#insn-00aced1c)

~~~json
{
  "source": "00aced1c",
  "target": "00acee94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aced24`](#insn-00aced24)

~~~json
{
  "source": "00aced24",
  "target": "006f18c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aced2c`](#insn-00aced2c)

~~~json
{
  "source": "00aced2c",
  "target": "00aceac0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aced30`](#insn-00aced30)

~~~json
{
  "source": "00aced30",
  "target": "005bdd1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aced3c`](#insn-00aced3c)

~~~json
{
  "source": "00aced3c",
  "target": "0029e637",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029e637",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "67617479616974656d445f253032645f662e706e6700",
  "capture_start": "0029e637",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aced44`](#insn-00aced44)

~~~json
{
  "source": "00aced44",
  "target": "0041b298",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aced48`](#insn-00aced48)

~~~json
{
  "source": "00aced48",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aced50`](#insn-00aced50)

~~~json
{
  "source": "00aced50",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aced5c`](#insn-00aced5c)

~~~json
{
  "source": "00aced5c",
  "target": "0033a22c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033a22c",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "34ed0000",
  "capture_start": "0033a22c",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aced6c`](#insn-00aced6c)

~~~json
{
  "source": "00aced6c",
  "target": "006f18c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aced70`](#insn-00aced70)

~~~json
{
  "source": "00aced70",
  "target": "006f3104",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aced84`](#insn-00aced84)

~~~json
{
  "source": "00aced84",
  "target": "004253b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aced90`](#insn-00aced90)

~~~json
{
  "source": "00aced90",
  "target": "00469f7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aced98`](#insn-00aced98)

~~~json
{
  "source": "00aced98",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aceda0`](#insn-00aceda0)

~~~json
{
  "source": "00aceda0",
  "target": "0041b298",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acedb8`](#insn-00acedb8)

~~~json
{
  "source": "00acedb8",
  "target": "0045b734",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acedc4`](#insn-00acedc4)

~~~json
{
  "source": "00acedc4",
  "target": "005bdd9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acedcc`](#insn-00acedcc)

~~~json
{
  "source": "00acedcc",
  "target": "0044b660",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acedd0`](#insn-00acedd0)

~~~json
{
  "source": "00acedd0",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acedd4`](#insn-00acedd4)

~~~json
{
  "source": "00acedd4",
  "target": "00acee6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acedd8`](#insn-00acedd8)

~~~json
{
  "source": "00acedd8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aceddc`](#insn-00aceddc)

~~~json
{
  "source": "00aceddc",
  "target": "00acee7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acede0`](#insn-00acede0)

~~~json
{
  "source": "00acede0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acede4`](#insn-00acede4)

~~~json
{
  "source": "00acede4",
  "target": "00acee8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acede8`](#insn-00acede8)

~~~json
{
  "source": "00acede8",
  "target": "00acee94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acedec`](#insn-00acedec)

~~~json
{
  "source": "00acedec",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acedf0`](#insn-00acedf0)

~~~json
{
  "source": "00acedf0",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acedf4`](#insn-00acedf4)

~~~json
{
  "source": "00acedf4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acedf8`](#insn-00acedf8)

~~~json
{
  "source": "00acedf8",
  "target": "00ace7a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acedfc`](#insn-00acedfc)

~~~json
{
  "source": "00acedfc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee00`](#insn-00acee00)

~~~json
{
  "source": "00acee00",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acee04`](#insn-00acee04)

~~~json
{
  "source": "00acee04",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee08`](#insn-00acee08)

~~~json
{
  "source": "00acee08",
  "target": "00ace7a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee0c`](#insn-00acee0c)

~~~json
{
  "source": "00acee0c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee10`](#insn-00acee10)

~~~json
{
  "source": "00acee10",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acee14`](#insn-00acee14)

~~~json
{
  "source": "00acee14",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee18`](#insn-00acee18)

~~~json
{
  "source": "00acee18",
  "target": "00acee94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee1c`](#insn-00acee1c)

~~~json
{
  "source": "00acee1c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee20`](#insn-00acee20)

~~~json
{
  "source": "00acee20",
  "target": "00acee90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee24`](#insn-00acee24)

~~~json
{
  "source": "00acee24",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee28`](#insn-00acee28)

~~~json
{
  "source": "00acee28",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acee2c`](#insn-00acee2c)

~~~json
{
  "source": "00acee2c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee30`](#insn-00acee30)

~~~json
{
  "source": "00acee30",
  "target": "00aced04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee34`](#insn-00acee34)

~~~json
{
  "source": "00acee34",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee38`](#insn-00acee38)

~~~json
{
  "source": "00acee38",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acee3c`](#insn-00acee3c)

~~~json
{
  "source": "00acee3c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee40`](#insn-00acee40)

~~~json
{
  "source": "00acee40",
  "target": "00aced0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee44`](#insn-00acee44)

~~~json
{
  "source": "00acee44",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee48`](#insn-00acee48)

~~~json
{
  "source": "00acee48",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acee4c`](#insn-00acee4c)

~~~json
{
  "source": "00acee4c",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee50`](#insn-00acee50)

~~~json
{
  "source": "00acee50",
  "target": "00aced14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee54`](#insn-00acee54)

~~~json
{
  "source": "00acee54",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee58`](#insn-00acee58)

~~~json
{
  "source": "00acee58",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acee5c`](#insn-00acee5c)

~~~json
{
  "source": "00acee5c",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee60`](#insn-00acee60)

~~~json
{
  "source": "00acee60",
  "target": "00acee94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee64`](#insn-00acee64)

~~~json
{
  "source": "00acee64",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee68`](#insn-00acee68)

~~~json
{
  "source": "00acee68",
  "target": "00acee90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee6c`](#insn-00acee6c)

~~~json
{
  "source": "00acee6c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee70`](#insn-00acee70)

~~~json
{
  "source": "00acee70",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acee74`](#insn-00acee74)

~~~json
{
  "source": "00acee74",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee78`](#insn-00acee78)

~~~json
{
  "source": "00acee78",
  "target": "00acede0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee7c`](#insn-00acee7c)

~~~json
{
  "source": "00acee7c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee80`](#insn-00acee80)

~~~json
{
  "source": "00acee80",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acee84`](#insn-00acee84)

~~~json
{
  "source": "00acee84",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee88`](#insn-00acee88)

~~~json
{
  "source": "00acee88",
  "target": "00acee94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee8c`](#insn-00acee8c)

~~~json
{
  "source": "00acee8c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee90`](#insn-00acee90)

~~~json
{
  "source": "00acee90",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acee94`](#insn-00acee94)

~~~json
{
  "source": "00acee94",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee98`](#insn-00acee98)

~~~json
{
  "source": "00acee98",
  "target": "00aceac0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee9c`](#insn-00acee9c)

~~~json
{
  "source": "00acee9c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aceea0`](#insn-00aceea0)

~~~json
{
  "source": "00aceea0",
  "target": "00aceabc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aceea4`](#insn-00aceea4)

~~~json
{
  "source": "00aceea4",
  "target": "005bdd1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aceeb0`](#insn-00aceeb0)

~~~json
{
  "source": "00aceeb0",
  "target": "0029113c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029113c",
  "offset": 0,
  "size": 21,
  "datatype": "string",
  "bytes": "67617479616974656d5f253032645f662e706e6700",
  "capture_start": "0029113c",
  "capture_bytes": 21,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aceeb8`](#insn-00aceeb8)

~~~json
{
  "source": "00aceeb8",
  "target": "0041b298",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aceebc`](#insn-00aceebc)

~~~json
{
  "source": "00aceebc",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aceec4`](#insn-00aceec4)

~~~json
{
  "source": "00aceec4",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aceed8`](#insn-00aceed8)

~~~json
{
  "source": "00aceed8",
  "target": "0033a22c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033a22c",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "34ed0000",
  "capture_start": "0033a22c",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aceee0`](#insn-00aceee0)

~~~json
{
  "source": "00aceee0",
  "target": "00335a20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335a05",
  "offset": 27,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440e20480c1d2093049e069d080a640c1f20480e00d3dedd440b440c1f20480e",
  "capture_start": "00335a05",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aceef0`](#insn-00aceef0)

~~~json
{
  "source": "00aceef0",
  "target": "008eccc4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aceefc`](#insn-00aceefc)

~~~json
{
  "source": "00aceefc",
  "target": "00469f7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acef04`](#insn-00acef04)

~~~json
{
  "source": "00acef04",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acef0c`](#insn-00acef0c)

~~~json
{
  "source": "00acef0c",
  "target": "0041b298",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acef24`](#insn-00acef24)

~~~json
{
  "source": "00acef24",
  "target": "0045b734",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acef28`](#insn-00acef28)

~~~json
{
  "source": "00acef28",
  "target": "00acedbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acef30`](#insn-00acef30)

~~~json
{
  "source": "00acef30",
  "target": "00c24f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acef34`](#insn-00acef34)

~~~json
{
  "source": "00acef34",
  "target": "00bdaf00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acef38`](#insn-00acef38)

~~~json
{
  "source": "00acef38",
  "target": "00ace840",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acef40`](#insn-00acef40)

~~~json
{
  "source": "00acef40",
  "target": "00c24f40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acef48`](#insn-00acef48)

~~~json
{
  "source": "00acef48",
  "target": "0045bedc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acef54`](#insn-00acef54)

~~~json
{
  "source": "00acef54",
  "target": "00be5ed0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be5ed0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acef58`](#insn-00acef58)

~~~json
{
  "source": "00acef58",
  "target": "00c24f48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acef5c`](#insn-00acef5c)

~~~json
{
  "source": "00acef5c",
  "target": "00c24f40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acef5c`](#insn-00acef5c)

~~~json
{
  "source": "00acef5c",
  "target": "00c24f48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acef64`](#insn-00acef64)

~~~json
{
  "source": "00acef64",
  "target": "00c24f68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acef64`](#insn-00acef64)

~~~json
{
  "source": "00acef64",
  "target": "00c24f70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acef68`](#insn-00acef68)

~~~json
{
  "source": "00acef68",
  "target": "00c24f60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acef6c`](#insn-00acef6c)

~~~json
{
  "source": "00acef6c",
  "target": "00c24f50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f50",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acef6c`](#insn-00acef6c)

~~~json
{
  "source": "00acef6c",
  "target": "00c24f58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f58",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acef6c`](#insn-00acef6c)

~~~json
{
  "source": "00acef6c",
  "target": "00c24f60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acef70`](#insn-00acef70)

~~~json
{
  "source": "00acef70",
  "target": "00bdaee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acef78`](#insn-00acef78)

~~~json
{
  "source": "00acef78",
  "target": "00c24f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acef7c`](#insn-00acef7c)

~~~json
{
  "source": "00acef7c",
  "target": "00bdaf20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acef80`](#insn-00acef80)

~~~json
{
  "source": "00acef80",
  "target": "00ace840",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acef88`](#insn-00acef88)

~~~json
{
  "source": "00acef88",
  "target": "00c24f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acef8c`](#insn-00acef8c)

~~~json
{
  "source": "00acef8c",
  "target": "00bdaf00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acef90`](#insn-00acef90)

~~~json
{
  "source": "00acef90",
  "target": "00ace548",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acef98`](#insn-00acef98)

~~~json
{
  "source": "00acef98",
  "target": "00c24f40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acefa0`](#insn-00acefa0)

~~~json
{
  "source": "00acefa0",
  "target": "0045bedc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acefac`](#insn-00acefac)

~~~json
{
  "source": "00acefac",
  "target": "00be5ed0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be5ed0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acefb0`](#insn-00acefb0)

~~~json
{
  "source": "00acefb0",
  "target": "00c24f48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acefb4`](#insn-00acefb4)

~~~json
{
  "source": "00acefb4",
  "target": "00c24f40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acefb4`](#insn-00acefb4)

~~~json
{
  "source": "00acefb4",
  "target": "00c24f48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acefbc`](#insn-00acefbc)

~~~json
{
  "source": "00acefbc",
  "target": "00c24f68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acefbc`](#insn-00acefbc)

~~~json
{
  "source": "00acefbc",
  "target": "00c24f70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acefc0`](#insn-00acefc0)

~~~json
{
  "source": "00acefc0",
  "target": "00c24f60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acefc4`](#insn-00acefc4)

~~~json
{
  "source": "00acefc4",
  "target": "00c24f50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f50",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acefc4`](#insn-00acefc4)

~~~json
{
  "source": "00acefc4",
  "target": "00c24f58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f58",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acefc4`](#insn-00acefc4)

~~~json
{
  "source": "00acefc4",
  "target": "00c24f60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acefc8`](#insn-00acefc8)

~~~json
{
  "source": "00acefc8",
  "target": "00bdaee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acefd0`](#insn-00acefd0)

~~~json
{
  "source": "00acefd0",
  "target": "00c24f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acefd4`](#insn-00acefd4)

~~~json
{
  "source": "00acefd4",
  "target": "00bdaf20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acefd8`](#insn-00acefd8)

~~~json
{
  "source": "00acefd8",
  "target": "00ace548",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acefe0`](#insn-00acefe0)

~~~json
{
  "source": "00acefe0",
  "target": "00c24f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acefe4`](#insn-00acefe4)

~~~json
{
  "source": "00acefe4",
  "target": "00bdaf00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acefe8`](#insn-00acefe8)

~~~json
{
  "source": "00acefe8",
  "target": "00ace960",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aceff0`](#insn-00aceff0)

~~~json
{
  "source": "00aceff0",
  "target": "00c24f40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aceff8`](#insn-00aceff8)

~~~json
{
  "source": "00aceff8",
  "target": "0045bedc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf004`](#insn-00acf004)

~~~json
{
  "source": "00acf004",
  "target": "00be5ed0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be5ed0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acf008`](#insn-00acf008)

~~~json
{
  "source": "00acf008",
  "target": "00c24f48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf00c`](#insn-00acf00c)

~~~json
{
  "source": "00acf00c",
  "target": "00c24f40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf00c`](#insn-00acf00c)

~~~json
{
  "source": "00acf00c",
  "target": "00c24f48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf014`](#insn-00acf014)

~~~json
{
  "source": "00acf014",
  "target": "00c24f68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf014`](#insn-00acf014)

~~~json
{
  "source": "00acf014",
  "target": "00c24f70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf018`](#insn-00acf018)

~~~json
{
  "source": "00acf018",
  "target": "00c24f60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf01c`](#insn-00acf01c)

~~~json
{
  "source": "00acf01c",
  "target": "00c24f50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f50",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf01c`](#insn-00acf01c)

~~~json
{
  "source": "00acf01c",
  "target": "00c24f58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f58",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf01c`](#insn-00acf01c)

~~~json
{
  "source": "00acf01c",
  "target": "00c24f60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf020`](#insn-00acf020)

~~~json
{
  "source": "00acf020",
  "target": "00bdaee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf028`](#insn-00acf028)

~~~json
{
  "source": "00acf028",
  "target": "00c24f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf02c`](#insn-00acf02c)

~~~json
{
  "source": "00acf02c",
  "target": "00bdaf20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf030`](#insn-00acf030)

~~~json
{
  "source": "00acf030",
  "target": "00ace960",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf038`](#insn-00acf038)

~~~json
{
  "source": "00acf038",
  "target": "00c24f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf03c`](#insn-00acf03c)

~~~json
{
  "source": "00acf03c",
  "target": "00bdaf00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf040`](#insn-00acf040)

~~~json
{
  "source": "00acf040",
  "target": "00ace9d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf048`](#insn-00acf048)

~~~json
{
  "source": "00acf048",
  "target": "00c24f40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf050`](#insn-00acf050)

~~~json
{
  "source": "00acf050",
  "target": "0045bedc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf05c`](#insn-00acf05c)

~~~json
{
  "source": "00acf05c",
  "target": "00be5ed0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be5ed0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acf060`](#insn-00acf060)

~~~json
{
  "source": "00acf060",
  "target": "00c24f48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf064`](#insn-00acf064)

~~~json
{
  "source": "00acf064",
  "target": "00c24f40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf064`](#insn-00acf064)

~~~json
{
  "source": "00acf064",
  "target": "00c24f48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf06c`](#insn-00acf06c)

~~~json
{
  "source": "00acf06c",
  "target": "00c24f68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf06c`](#insn-00acf06c)

~~~json
{
  "source": "00acf06c",
  "target": "00c24f70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf070`](#insn-00acf070)

~~~json
{
  "source": "00acf070",
  "target": "00c24f60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf074`](#insn-00acf074)

~~~json
{
  "source": "00acf074",
  "target": "00c24f50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f50",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf074`](#insn-00acf074)

~~~json
{
  "source": "00acf074",
  "target": "00c24f58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f58",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf074`](#insn-00acf074)

~~~json
{
  "source": "00acf074",
  "target": "00c24f60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf078`](#insn-00acf078)

~~~json
{
  "source": "00acf078",
  "target": "00bdaee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf080`](#insn-00acf080)

~~~json
{
  "source": "00acf080",
  "target": "00c24f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf084`](#insn-00acf084)

~~~json
{
  "source": "00acf084",
  "target": "00bdaf20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf088`](#insn-00acf088)

~~~json
{
  "source": "00acf088",
  "target": "00ace9d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf090`](#insn-00acf090)

~~~json
{
  "source": "00acf090",
  "target": "00c24f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf094`](#insn-00acf094)

~~~json
{
  "source": "00acf094",
  "target": "00bdaf00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf098`](#insn-00acf098)

~~~json
{
  "source": "00acf098",
  "target": "00ace658",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf0a0`](#insn-00acf0a0)

~~~json
{
  "source": "00acf0a0",
  "target": "00c24f40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf0a8`](#insn-00acf0a8)

~~~json
{
  "source": "00acf0a8",
  "target": "0045bedc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf0b4`](#insn-00acf0b4)

~~~json
{
  "source": "00acf0b4",
  "target": "00be5ed0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be5ed0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acf0b8`](#insn-00acf0b8)

~~~json
{
  "source": "00acf0b8",
  "target": "00c24f48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf0bc`](#insn-00acf0bc)

~~~json
{
  "source": "00acf0bc",
  "target": "00c24f40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf0bc`](#insn-00acf0bc)

~~~json
{
  "source": "00acf0bc",
  "target": "00c24f48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf0c4`](#insn-00acf0c4)

~~~json
{
  "source": "00acf0c4",
  "target": "00c24f68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf0c4`](#insn-00acf0c4)

~~~json
{
  "source": "00acf0c4",
  "target": "00c24f70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf0c8`](#insn-00acf0c8)

~~~json
{
  "source": "00acf0c8",
  "target": "00c24f60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf0cc`](#insn-00acf0cc)

~~~json
{
  "source": "00acf0cc",
  "target": "00c24f50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f50",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf0cc`](#insn-00acf0cc)

~~~json
{
  "source": "00acf0cc",
  "target": "00c24f58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f58",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf0cc`](#insn-00acf0cc)

~~~json
{
  "source": "00acf0cc",
  "target": "00c24f60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf0d0`](#insn-00acf0d0)

~~~json
{
  "source": "00acf0d0",
  "target": "00bdaee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf0d8`](#insn-00acf0d8)

~~~json
{
  "source": "00acf0d8",
  "target": "00c24f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf0dc`](#insn-00acf0dc)

~~~json
{
  "source": "00acf0dc",
  "target": "00bdaf20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf0e0`](#insn-00acf0e0)

~~~json
{
  "source": "00acf0e0",
  "target": "00ace658",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf0e8`](#insn-00acf0e8)

~~~json
{
  "source": "00acf0e8",
  "target": "00c24f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf0ec`](#insn-00acf0ec)

~~~json
{
  "source": "00acf0ec",
  "target": "00bdaf00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf0f0`](#insn-00acf0f0)

~~~json
{
  "source": "00acf0f0",
  "target": "00ace8e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf0f8`](#insn-00acf0f8)

~~~json
{
  "source": "00acf0f8",
  "target": "00c24f40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf100`](#insn-00acf100)

~~~json
{
  "source": "00acf100",
  "target": "0045bedc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf10c`](#insn-00acf10c)

~~~json
{
  "source": "00acf10c",
  "target": "00be5ed0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be5ed0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acf110`](#insn-00acf110)

~~~json
{
  "source": "00acf110",
  "target": "00c24f48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf114`](#insn-00acf114)

~~~json
{
  "source": "00acf114",
  "target": "00c24f40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf114`](#insn-00acf114)

~~~json
{
  "source": "00acf114",
  "target": "00c24f48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf11c`](#insn-00acf11c)

~~~json
{
  "source": "00acf11c",
  "target": "00c24f68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf11c`](#insn-00acf11c)

~~~json
{
  "source": "00acf11c",
  "target": "00c24f70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf120`](#insn-00acf120)

~~~json
{
  "source": "00acf120",
  "target": "00c24f60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf124`](#insn-00acf124)

~~~json
{
  "source": "00acf124",
  "target": "00c24f50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f50",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf124`](#insn-00acf124)

~~~json
{
  "source": "00acf124",
  "target": "00c24f58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f58",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf124`](#insn-00acf124)

~~~json
{
  "source": "00acf124",
  "target": "00c24f60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf128`](#insn-00acf128)

~~~json
{
  "source": "00acf128",
  "target": "00bdaee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf130`](#insn-00acf130)

~~~json
{
  "source": "00acf130",
  "target": "00c24f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acf134`](#insn-00acf134)

~~~json
{
  "source": "00acf134",
  "target": "00bdaf20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf138`](#insn-00acf138)

~~~json
{
  "source": "00acf138",
  "target": "00ace8e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf35c`](#insn-00acf35c)

~~~json
{
  "source": "00acf35c",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
