# 00abf8ac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a618f4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a61/00a618f4.md) · 移動量 `+0x5dfb8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0052.md#compare-b2a851c28333486cb9f80129c19463c7)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00abfaa8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abf/00abfaa8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-7744c44cf700522463631d96716c5a93)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abf8ac",
  "name": "FUN_00abf8ac",
  "size": 2064,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "956c8f8c6f3b377123e51ef5b84f643502a8f60e72c7c99d4b584f67043a1029",
  "source_text_sha256": "956c8f8c6f3b377123e51ef5b84f643502a8f60e72c7c99d4b584f67043a1029",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00abf8ac",
        "00ac0083"
      ],
      [
        "00ac00b0",
        "00ac00bf"
      ],
      [
        "00ac014c",
        "00ac0153"
      ],
      [
        "00ac0188",
        "00ac01a7"
      ]
    ],
    "bytes_sha256": "1605cf08ffb8a1a2a9f8515daee33929a630f955499f036bab8d57ddd801e73b",
    "instruction_count": 516,
    "instruction_bytes": 2064,
    "body_bytes": 2064,
    "indirect": 8,
    "unresolved": 8
  }
}
~~~

## 呼び出し元

- [00abf588](../00abf/00abf588.md)
- [00b3c6b0](../00b3c/00b3c6b0.md)

## 呼び出し先

- [0043bae0](../0043b/0043bae0.md)
- [00447eb4](../00447/00447eb4.md)
- [0046e930](../0046e/0046e930.md)
- [0047e5cc](../0047e/0047e5cc.md)
- [0047e89c](../0047e/0047e89c.md)
- [0048ce14](../0048c/0048ce14.md)
- [00492dc8](../00492/00492dc8.md)
- [0049f3b0](../0049f/0049f3b0.md)
- [00ac0de8](../00ac0/00ac0de8.md)
- [00c538e0](../00c53/00c538e0.md)
- [00c53b3c](../00c53/00c53b3c.md)
- [00c57a30](../00c57/00c57a30.md)
- [00c57a50](../00c57/00c57a50.md)
- [00c57a70](../00c57/00c57a70.md)
- [00c57a80](../00c57/00c57a80.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)

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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 18282 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void FUN_00abf8ac(long *param_1,long param_2)

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
    if (((DAT_00ca4b38 & 1) == 0) && (iVar3 = __cxa_guard_acquire(&DAT_00ca4b38), iVar3 != 0)) {
      DAT_00ca4b08 = 0;
                    /* try { // try from 00abff14 to 00bc0197 has its CatchHandler @ 00abf53c */
      DAT_00ca4b00 = &DAT_00ca4b08;
      DAT_00ca4b28 = 0;
      DAT_00ca4b30 = 0;
      DAT_00ca4b20 = 0;
      DAT_00ca4b10 = 0;
      DAT_00ca4b18 = &DAT_00ca4b20;
      __cxa_atexit(FUN_0047ed74,&DAT_00ca4b00,&PTR_LOOP_00c62b90);
      __cxa_guard_release(&DAT_00ca4b38);
    }
    local_70 = 0x20;
    local_88 = 0x26;
    uStack_67 = (undefined7)s_medal_get000_png_002ab964._8_8_;
    cStack_60 = SUB81(s_medal_get000_png_002ab964._8_8_,7);
    local_6f[0] = s_medal_get000_png_002ab964[0];
    local_6f[1] = s_medal_get000_png_002ab964[1];
    local_6f[2] = s_medal_get000_png_002ab964[2];
    local_6f[3] = s_medal_get000_png_002ab964[3];
    local_6f[4] = s_medal_get000_png_002ab964[4];
    local_6f[5] = s_medal_get000_png_002ab964[5];
    local_6f[6] = s_medal_get000_png_002ab964[6];
    local_6f[7] = s_medal_get000_png_002ab964[7];
    uStack_5f = 0;
    uStack_7f = (undefined6)s_medal_get000_imgcut_002adad5._8_8_;
    cStack_79 = SUB81(s_medal_get000_imgcut_002adad5._8_8_,6);
    uStack_78 = CONCAT31(0x747563,SUB81(s_medal_get000_imgcut_002adad5._8_8_,7));
    local_87 = (undefined6)s_medal_get000_imgcut_002adad5._0_8_;
    uStack_81 = SUB82(s_medal_get000_imgcut_002adad5._0_8_,6);
    uStack_74 = uStack_74 & 0xffffff00;
    FUN_0047e5cc(&local_c0,&DAT_00ca4b00,&local_70,&local_88,0x2601);
    uVar2 = CONCAT44(uStack_b4,CONCAT13(cStack_b5,CONCAT21(uStack_b7,cStack_b8)));
                    /* try { // try from 00abf95c to 00bbf963 has its CatchHandler @ 00ac0098 */
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
    if ((plVar8 == (long *)0x0) || (lVar4 = FUN_00c538e0(0xffffffffffffffff,plVar8 + 1), lVar4 != 0)
       ) {
      plVar8 = (long *)CONCAT44(uStack_b4,CONCAT13(cStack_b5,CONCAT21(uStack_b7,cStack_b8)));
    }
    else {
      (**(code **)(*plVar8 + 0x10))(plVar8);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
      plVar8 = (long *)CONCAT44(uStack_b4,CONCAT13(cStack_b5,CONCAT21(uStack_b7,cStack_b8)));
                    /* try { // try from 00abf9d0 to 00bbf9ef has its CatchHandler @ 00ac0164 */
    }
                    /* try { // try from 00abf98c to 00bbf997 has its CatchHandler @ 00ac0090 */
    if ((plVar8 != (long *)0x0) &&
       (lVar4 = FUN_00c538e0(0xffffffffffffffff,(long *)((long)plVar8 + 8)), lVar4 == 0)) {
      (**(code **)(*plVar8 + 0x10))(plVar8);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
    }
    if ((local_88 & 1) != 0) {
      _ZdlPv((void *)CONCAT44(uStack_74,uStack_78));
                    /* try { // try from 00abfa04 to 00bbfa0b has its CatchHandler @ 00ac00d0 */
    }
    if ((local_70 & 1) != 0) {
      _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT22(uStack_5e,CONCAT11(uStack_5f,cStack_60))));
    }
    if (((DAT_00ca4b38 & 1) == 0) && (iVar3 = __cxa_guard_acquire(&DAT_00ca4b38), iVar3 != 0)) {
      DAT_00ca4b08 = 0;
      DAT_00ca4b00 = &DAT_00ca4b08;
      DAT_00ca4b28 = 0;
      DAT_00ca4b30 = 0;
      DAT_00ca4b20 = 0;
      DAT_00ca4b10 = 0;
      DAT_00ca4b18 = &DAT_00ca4b20;
      __cxa_atexit(FUN_0047ed74,&DAT_00ca4b00,&PTR_LOOP_00c62b90);
                    /* catch() { ... } // from try @ 00abfe78 with catch @ 00abff80 */
                    /* catch() { ... } // from try @ 00abfdb8 with catch @ 00abff84 */
      __cxa_guard_release(&DAT_00ca4b38);
    }
    local_88 = 0x1c;
    plVar8 = param_1 + 0xf;
                    /* try { // try from 00abfa34 to 00bbfa3f has its CatchHandler @ 00ac00c8 */
    cStack_79 = 0;
                    /* try { // try from 00abfa40 to 00bbfa43 has its CatchHandler @ 00ac0100 */
    local_87._0_1_ = s_medal__03d_png_002bb807[0];
    local_87._1_1_ = s_medal__03d_png_002bb807[1];
    local_87._2_1_ = s_medal__03d_png_002bb807[2];
    local_87._3_1_ = s_medal__03d_png_002bb807[3];
    local_87._4_1_ = s_medal__03d_png_002bb807[4];
    local_87._5_1_ = s_medal__03d_png_002bb807[5];
    uStack_81._0_1_ = s_medal__03d_png_002bb807[6];
    uStack_81._1_1_ = s_medal__03d_png_002bb807[7];
    uStack_7f._0_1_ = s_medal__03d_png_002bb807[8];
    uStack_7f._1_1_ = s_medal__03d_png_002bb807[9];
    uStack_7f._2_1_ = s_medal__03d_png_002bb807[10];
    uStack_7f._3_1_ = s_medal__03d_png_002bb807[0xb];
    uStack_7f._4_1_ = s_medal__03d_png_002bb807[0xc];
    uStack_7f._5_1_ = s_medal__03d_png_002bb807[0xd];
    if ((undefined4 *)param_1[0x10] == (undefined4 *)*plVar8) {
                    /* catch() { ... } // from try @ 00abfdac with catch @ 00abff9c */
      if (*(long *)(lVar1 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
        FUN_0049f3b0(plVar8);
      }
      goto LAB_00ac01a4;
    }
    FUN_00447eb4(&local_70,&local_88,0,*(undefined4 *)*plVar8);
    local_c0 = 0x20;
    uStack_af = 0;
    uStack_b7 = (undefined2)s_medal_001_imgcut_002bcaae._8_8_;
    cStack_b5 = SUB81(s_medal_001_imgcut_002bcaae._8_8_,2);
    uStack_b4 = SUB84(s_medal_001_imgcut_002bcaae._8_8_,3);
    local_b0 = SUB81(s_medal_001_imgcut_002bcaae._8_8_,7);
    uStack_bf = (undefined7)s_medal_001_imgcut_002bcaae._0_8_;
    cStack_b8 = SUB81(s_medal_001_imgcut_002bcaae._0_8_,7);
                    /* try { // try from 00abfa80 to 00bbfaff has its CatchHandler @ 00ac0138 */
    FUN_0047e5cc(&local_a0,&DAT_00ca4b00,&local_70,&local_c0,0x2601);
    plVar7 = plStack_98;
    uVar5 = local_a0;
    plVar9 = *(long **)(param_2 + 0x60);
    local_a0 = 0;
    plStack_98 = (long *)0x0;
    *(long **)(param_2 + 0x60) = plVar7;
    *(undefined8 *)(param_2 + 0x58) = uVar5;
    plVar7 = plStack_98;
    if ((plVar9 != (long *)0x0) &&
       (lVar4 = FUN_00c538e0(0xffffffffffffffff,plVar9 + 1), plVar7 = plStack_98, lVar4 == 0)) {
      (**(code **)(*plVar9 + 0x10))(plVar9);
                    /* try { // try from 00abfdf4 to 00bbfe0f has its CatchHandler @ 00ac0108 */
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
      plVar7 = plStack_98;
    }
    plStack_98 = plVar7;
    if ((plVar7 != (long *)0x0) &&
       (lVar4 = FUN_00c538e0(0xffffffffffffffff,(long *)((long)plVar7 + 8)), lVar4 == 0)) {
                    /* try { // try from 00abfe14 to 00bbfe1f has its CatchHandler @ 00abffc0 */
      (**(code **)(*plVar7 + 0x10))(plVar7);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
                    /* try { // try from 00abfe20 to 00bbfe2f has its CatchHandler @ 00abffb8 */
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
                    /* catch() { ... } // from try @ 00abf678 with catch @ 00ac0008 */
      if (((DAT_00ca4b38 & 1) == 0) && (iVar3 = __cxa_guard_acquire(&DAT_00ca4b38), iVar3 != 0)) {
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
      local_c0 = 0x14;
      uStack_b7 = 0x3174;
      uStack_bf = (undefined7)s_medal_txt1_002a17d1._0_8_;
      cStack_b8 = SUB81(s_medal_txt1_002a17d1._0_8_,7);
      cStack_b5 = 0;
      FUN_0048ce14(&local_88,&local_c0);
                    /* try { // try from 00abfc74 to 00bbfc7f has its CatchHandler @ 00ac0108 */
      if ((int *)param_1[0x10] == (int *)param_1[0xf]) {
                    /* catch() { ... } // from try @ 00abfec0 with catch @ 00ac0050 */
                    /* catch() { ... } // from try @ 00abf844 with catch @ 00ac0054 */
                    /* catch() { ... } // from try @ 00abf820 with catch @ 00ac005c */
        if (*(long *)(lVar1 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00abfbb8 with catch @ 00ac0064 */
          FUN_0049f3b0(plVar8);
        }
        goto LAB_00ac01a4;
      }
      uVar6 = (ulong)*(int *)param_1[0xf];
                    /* try { // try from 00abfc80 to 00bbfc87 has its CatchHandler @ 00abffe4 */
      if ((ulong)(param_1[1] - *param_1 >> 3) <= uVar6) {
        if (*(long *)(lVar1 + 0x28) == local_58) {
                    /* catch() { ... } // from try @ 00abfb90 with catch @ 00ac007c */
          uVar5 = FUN_00ac0de8(param_1);
                    /* catch() { ... } // from try @ 00abfb10 with catch @ 00ac00b4 */
          if ((local_70 & 1) != 0) {
            _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT22(uStack_5e,CONCAT11(uStack_5f,cStack_60))));
          }
          if (*(long *)(lVar1 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
            FUN_00c53b3c(uVar5);
          }
        }
        goto LAB_00ac01a4;
      }
      lVar4 = *(long *)(*param_1 + uVar6 * 8);
      if ((*(byte *)(lVar4 + 0x80) & 1) == 0) {
        uStack_d8 = *(undefined8 *)(lVar4 + 0x88);
        local_e0 = *(ulong *)(lVar4 + 0x80);
        local_d0 = *(void **)(lVar4 + 0x90);
      }
      else {
                    /* try { // try from 00abfcb4 to 00bbfcbf has its CatchHandler @ 00abffdc */
        FUN_0043bae0(&local_e0,*(undefined8 *)(lVar4 + 0x90),*(undefined8 *)(lVar4 + 0x88));
      }
                    /* try { // try from 00abfcc0 to 00bbfcd3 has its CatchHandler @ 00abffd8 */
      FUN_00492dc8(&local_70,&local_88,&local_e0);
      FUN_0047e89c(&local_a0,&DAT_00ca4b00,&local_70,PTR_DAT_00c9a8a0,0x14,0,0,0);
      plVar8 = plStack_98;
      uVar5 = local_a0;
      plVar7 = *(long **)(param_2 + 0x70);
      local_a0 = 0;
      plStack_98 = (long *)0x0;
      *(long **)(param_2 + 0x70) = plVar8;
      *(undefined8 *)(param_2 + 0x68) = uVar5;
                    /* try { // try from 00abfd0c to 00bbfd13 has its CatchHandler @ 00abffc4 */
      if ((plVar7 != (long *)0x0) &&
         (lVar4 = FUN_00c538e0(0xffffffffffffffff,plVar7 + 1), lVar4 == 0)) {
        (**(code **)(*plVar7 + 0x10))(plVar7);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
      }
      plVar8 = plStack_98;
      if ((plStack_98 != (long *)0x0) &&
         (lVar4 = FUN_00c538e0(0xffffffffffffffff,plStack_98 + 1), lVar4 == 0)) {
        (**(code **)(*plVar8 + 0x10))(plVar8);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
      }
      if ((local_70 & 1) != 0) {
        _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT22(uStack_5e,CONCAT11(uStack_5f,cStack_60))));
      }
      if ((local_e0 & 1) != 0) {
                    /* try { // try from 00abfec0 to 00bbff13 has its CatchHandler @ 00ac0050 */
        _ZdlPv(local_d0);
      }
                    /* try { // try from 00abfd60 to 00bbfd73 has its CatchHandler @ 00ac0108 */
      if ((local_88 & 1) != 0) {
        _ZdlPv((void *)CONCAT44(uStack_74,uStack_78));
      }
      if ((local_c0 & 1) != 0) {
        _ZdlPv((void *)CONCAT62(uStack_ae,CONCAT11(uStack_af,local_b0)));
      }
                    /* try { // try from 00abfd74 to 00bbfd7f has its CatchHandler @ 00abffb4 */
      local_70 = 0x26;
      uStack_5f = 0x6e;
      uStack_5e = 0x6d69;
      uStack_67 = (undefined7)s_medal_get001_maanim_002b7b7d._8_8_;
      cStack_60 = SUB81(s_medal_get001_maanim_002b7b7d._8_8_,7);
      local_6f[0] = s_medal_get001_maanim_002b7b7d[0];
      local_6f[1] = s_medal_get001_maanim_002b7b7d[1];
      local_6f[2] = s_medal_get001_maanim_002b7b7d[2];
      local_6f[3] = s_medal_get001_maanim_002b7b7d[3];
      local_6f[4] = s_medal_get001_maanim_002b7b7d[4];
      local_6f[5] = s_medal_get001_maanim_002b7b7d[5];
      local_6f[6] = s_medal_get001_maanim_002b7b7d[6];
      local_6f[7] = s_medal_get001_maanim_002b7b7d[7];
      uStack_5c = uStack_5c & 0xffffff00;
      FUN_0046e930(param_1 + 0x2a,&local_70);
    }
    else {
                    /* try { // try from 00abfb08 to 00bbfb0f has its CatchHandler @ 00ac0100 */
                    /* catch() { ... } // from try @ 00abfd74 with catch @ 00abffb4 */
      if (((DAT_00ca4b38 & 1) == 0) && (iVar3 = __cxa_guard_acquire(&DAT_00ca4b38), iVar3 != 0)) {
                    /* catch() { ... } // from try @ 00abfe20 with catch @ 00abffb8 */
                    /* catch() { ... } // from try @ 00abfe14 with catch @ 00abffc0 */
                    /* catch() { ... } // from try @ 00abfd0c with catch @ 00abffc4 */
        DAT_00ca4b08 = 0;
        DAT_00ca4b00 = &DAT_00ca4b08;
                    /* catch() { ... } // from try @ 00abfcc0 with catch @ 00abffd8 */
                    /* catch() { ... } // from try @ 00abfcb4 with catch @ 00abffdc */
        DAT_00ca4b28 = 0;
        DAT_00ca4b30 = 0;
        DAT_00ca4b20 = 0;
                    /* catch() { ... } // from try @ 00abfc80 with catch @ 00abffe4 */
        DAT_00ca4b10 = 0;
        DAT_00ca4b18 = &DAT_00ca4b20;
                    /* catch() { ... } // from try @ 00abf65c with catch @ 00abffe8 */
        __cxa_atexit(FUN_0047ed74,&DAT_00ca4b00,&PTR_LOOP_00c62b90);
                    /* catch() { ... } // from try @ 00abf640 with catch @ 00abfff4 */
        __cxa_guard_release(&DAT_00ca4b38);
      }
                    /* try { // try from 00abfb10 to 00bbfb1f has its CatchHandler @ 00ac00b4 */
      local_c0 = 0x14;
      uStack_b7 = 0x3274;
      uStack_bf = (undefined7)s_medal_txt2_002a17c6._0_8_;
      cStack_b8 = SUB81(s_medal_txt2_002a17c6._0_8_,7);
      cStack_b5 = 0;
                    /* try { // try from 00abfb38 to 00bbfb3f has its CatchHandler @ 00ac009c */
      FUN_0048ce14(&local_88,&local_c0);
      FUN_00447eb4(&local_70,&local_88,0,(ulong)(param_1[0x10] - param_1[0xf]) >> 2);
      FUN_0047e89c(&local_a0,&DAT_00ca4b00,&local_70,PTR_DAT_00c9a8a0,0x14,0,0,0);
      plVar8 = plStack_98;
      uVar5 = local_a0;
                    /* try { // try from 00abfb88 to 00bbfb8f has its CatchHandler @ 00ac00fc */
      plVar7 = *(long **)(param_2 + 0x70);
                    /* try { // try from 00abfb90 to 00bbfb9f has its CatchHandler @ 00ac007c */
      local_a0 = 0;
      plStack_98 = (long *)0x0;
      *(long **)(param_2 + 0x70) = plVar8;
      *(undefined8 *)(param_2 + 0x68) = uVar5;
      if ((plVar7 != (long *)0x0) &&
         (lVar4 = FUN_00c538e0(0xffffffffffffffff,plVar7 + 1), lVar4 == 0)) {
                    /* try { // try from 00abfbb8 to 00bbfbbf has its CatchHandler @ 00ac0064 */
        (**(code **)(*plVar7 + 0x10))(plVar7);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
      }
      plVar8 = plStack_98;
      if ((plStack_98 != (long *)0x0) &&
         (lVar4 = FUN_00c538e0(0xffffffffffffffff,plStack_98 + 1), lVar4 == 0)) {
        (**(code **)(*plVar8 + 0x10))(plVar8);
                    /* try { // try from 00abfe5c to 00bbfe6f has its CatchHandler @ 00ac013c */
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
      }
      if ((local_70 & 1) != 0) {
        _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT22(uStack_5e,CONCAT11(uStack_5f,cStack_60))));
                    /* try { // try from 00abfe78 to 00bbfe83 has its CatchHandler @ 00abff80 */
      }
                    /* try { // try from 00abfbe8 to 00bbfc33 has its CatchHandler @ 00ac0164 */
      if ((local_88 & 1) != 0) {
        _ZdlPv((void *)CONCAT44(uStack_74,uStack_78));
                    /* try { // try from 00abfe84 to 00bbfebf has its CatchHandler @ 00abf53c */
      }
      if ((local_c0 & 1) != 0) {
        _ZdlPv((void *)CONCAT62(uStack_ae,CONCAT11(uStack_af,local_b0)));
      }
      local_70 = 0x26;
      uStack_5f = 0x6e;
      uStack_5e = 0x6d69;
      uStack_67 = (undefined7)s_medal_get002_maanim_002afebe._8_8_;
      cStack_60 = SUB81(s_medal_get002_maanim_002afebe._8_8_,7);
      local_6f[0] = s_medal_get002_maanim_002afebe[0];
      local_6f[1] = s_medal_get002_maanim_002afebe[1];
      local_6f[2] = s_medal_get002_maanim_002afebe[2];
      local_6f[3] = s_medal_get002_maanim_002afebe[3];
      local_6f[4] = s_medal_get002_maanim_002afebe[4];
      local_6f[5] = s_medal_get002_maanim_002afebe[5];
      local_6f[6] = s_medal_get002_maanim_002afebe[6];
      local_6f[7] = s_medal_get002_maanim_002afebe[7];
      uStack_5c = uStack_5c & 0xffffff00;
      FUN_0046e930(param_1 + 0x2a,&local_70);
    }
                    /* try { // try from 00abfdac to 00bbfdb7 has its CatchHandler @ 00abff9c */
    if ((local_70 & 1) != 0) {
      _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT22(uStack_5e,CONCAT11(uStack_5f,cStack_60))));
    }
  }
                    /* try { // try from 00abfdb8 to 00bbfdd3 has its CatchHandler @ 00abff84 */
  if (*(long *)(lVar1 + 0x28) == local_58) {
    return;
  }
LAB_00ac01a4:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00abf8ac"></a> `00abf8ac` | `ff 83 03 d1` | sub sp,sp,#0xe0 | `FALL_THROUGH`
<a id="insn-00abf8b0"></a> `00abf8b0` | `fd 7b 09 a9` | stp x29,x30,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abf8b4"></a> `00abf8b4` | `f9 53 00 f9` | str x25,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00abf8b8"></a> `00abf8b8` | `f8 5f 0b a9` | stp x24,x23,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00abf8bc"></a> `00abf8bc` | `f6 57 0c a9` | stp x22,x21,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00abf8c0"></a> `00abf8c0` | `f4 4f 0d a9` | stp x20,x19,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00abf8c4"></a> `00abf8c4` | `fd 43 02 91` | add x29,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00abf8c8"></a> `00abf8c8` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00abf8cc"></a> `00abf8cc` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00abf8d0"></a> `00abf8d0` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abf8d4"></a> `00abf8d4` | `08 70 40 b9` | ldr w8,[x0, #0x70] | `FALL_THROUGH`
<a id="insn-00abf8d8"></a> `00abf8d8` | `1f 05 00 31` | cmn w8,#0x1 | `FALL_THROUGH`
<a id="insn-00abf8dc"></a> `00abf8dc` | `e0 26 00 54` | b.eq 0x00abfdb8 | `CONDITIONAL_JUMP`
<a id="insn-00abf8e0"></a> `00abf8e0` | `39 0f 00 b0` | adrp x25,0xca4000 | `FALL_THROUGH`
<a id="insn-00abf8e4"></a> `00abf8e4` | `39 e3 2c 91` | add x25,x25,#0xb38 | `FALL_THROUGH`
<a id="insn-00abf8e8"></a> `00abf8e8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00abf8ec"></a> `00abf8ec` | `28 ff df 08` | ldarb w8,[x25] | `FALL_THROUGH`
<a id="insn-00abf8f0"></a> `00abf8f0` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00abf8f4"></a> `00abf8f4` | `88 2f 00 36` | tbz w8,#0x0,0x00abfee4 | `CONDITIONAL_JUMP`
<a id="insn-00abf8f8"></a> `00abf8f8` | `68 bf ff 90` | adrp x8,0x2ab000 | `FALL_THROUGH`
<a id="insn-00abf8fc"></a> `00abf8fc` | `08 91 25 91` | add x8,x8,#0x964 | `FALL_THROUGH`
<a id="insn-00abf900"></a> `00abf900` | `09 04 80 52` | mov w9,#0x20 | `FALL_THROUGH`
<a id="insn-00abf904"></a> `00abf904` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00abf908"></a> `00abf908` | `a9 03 1e 38` | sturb w9,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abf90c"></a> `00abf90c` | `c8 04 80 52` | mov w8,#0x26 | `FALL_THROUGH`
<a id="insn-00abf910"></a> `00abf910` | `69 bf ff d0` | adrp x9,0x2ad000 | `FALL_THROUGH`
<a id="insn-00abf914"></a> `00abf914` | `29 55 2b 91` | add x9,x9,#0xad5 | `FALL_THROUGH`
<a id="insn-00abf918"></a> `00abf918` | `a8 83 1c 38` | sturb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00abf91c"></a> `00abf91c` | `a0 13 9e 3c` | stur q0,[x29, #-0x1f] | `FALL_THROUGH`
<a id="insn-00abf920"></a> `00abf920` | `e8 6c 8c 52` | mov w8,#0x6367 | `FALL_THROUGH`
<a id="insn-00abf924"></a> `00abf924` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00abf928"></a> `00abf928` | `a8 8e ae 72` | movk w8,#0x7475, LSL #16 | `FALL_THROUGH`
<a id="insn-00abf92c"></a> `00abf92c` | `bf 13 1f 38` | sturb wzr,[x29, #-0xf] | `FALL_THROUGH`
<a id="insn-00abf930"></a> `00abf930` | `a8 83 1d b8` | stur w8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00abf934"></a> `00abf934` | `a0 93 9c 3c` | stur q0,[x29, #-0x37] | `FALL_THROUGH`
<a id="insn-00abf938"></a> `00abf938` | `bf c3 1d 38` | sturb wzr,[x29, #-0x24] | `FALL_THROUGH`
<a id="insn-00abf93c"></a> `00abf93c` | `35 0f 00 b0` | adrp x21,0xca4000 | `FALL_THROUGH`
<a id="insn-00abf940"></a> `00abf940` | `b5 02 2c 91` | add x21,x21,#0xb00 | `FALL_THROUGH`
<a id="insn-00abf944"></a> `00abf944` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00abf948"></a> `00abf948` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00abf94c"></a> `00abf94c` | `a2 e3 00 d1` | sub x2,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00abf950"></a> `00abf950` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abf954"></a> `00abf954` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-00abf958"></a> `00abf958` | `1d fb e6 97` | bl 0x0047e5cc | `UNCONDITIONAL_CALL`
<a id="insn-00abf95c"></a> `00abf95c` | `e0 0b c0 3d` | ldr q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abf960"></a> `00abf960` | `96 2a 40 f9` | ldr x22,[x20, #0x50] | `FALL_THROUGH`
<a id="insn-00abf964"></a> `00abf964` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abf968"></a> `00abf968` | `80 82 84 3c` | stur q0,[x20, #0x48] | `FALL_THROUGH`
<a id="insn-00abf96c"></a> `00abf96c` | `b6 00 00 b4` | cbz x22,0x00abf980 | `CONDITIONAL_JUMP`
<a id="insn-00abf970"></a> `00abf970` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00abf974"></a> `00abf974` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abf978"></a> `00abf978` | `da 4f 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00abf97c"></a> `00abf97c` | `c0 01 00 b4` | cbz x0,0x00abf9b4 | `CONDITIONAL_JUMP`
<a id="insn-00abf980"></a> `00abf980` | `f6 17 40 f9` | ldr x22,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00abf984"></a> `00abf984` | `b6 00 00 b4` | cbz x22,0x00abf998 | `CONDITIONAL_JUMP`
<a id="insn-00abf988"></a> `00abf988` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00abf98c"></a> `00abf98c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abf990"></a> `00abf990` | `d4 4f 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00abf994"></a> `00abf994` | `20 02 00 b4` | cbz x0,0x00abf9d8 | `CONDITIONAL_JUMP`
<a id="insn-00abf998"></a> `00abf998` | `a8 83 5c 38` | ldurb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00abf99c"></a> `00abf99c` | `e8 02 00 37` | tbnz w8,#0x0,0x00abf9f8 | `CONDITIONAL_JUMP`
<a id="insn-00abf9a0"></a> `00abf9a0` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abf9a4"></a> `00abf9a4` | `28 03 00 37` | tbnz w8,#0x0,0x00abfa08 | `CONDITIONAL_JUMP`
<a id="insn-00abf9a8"></a> `00abf9a8` | `28 ff df 08` | ldarb w8,[x25] | `FALL_THROUGH`
<a id="insn-00abf9ac"></a> `00abf9ac` | `68 03 00 37` | tbnz w8,#0x0,0x00abfa18 | `CONDITIONAL_JUMP`
<a id="insn-00abf9b0"></a> `00abf9b0` | `63 01 00 14` | b 0x00abff3c | `UNCONDITIONAL_JUMP`
<a id="insn-00abf9b4"></a> `00abf9b4` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00abf9b8"></a> `00abf9b8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00abf9bc"></a> `00abf9bc` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abf9c0"></a> `00abf9c0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abf9c4"></a> `00abf9c4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00abf9c8"></a> `00abf9c8` | `2e 60 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00abf9cc"></a> `00abf9cc` | `f6 17 40 f9` | ldr x22,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00abf9d0"></a> `00abf9d0` | `d6 fd ff b5` | cbnz x22,0x00abf988 | `CONDITIONAL_JUMP`
<a id="insn-00abf9d4"></a> `00abf9d4` | `f1 ff ff 17` | b 0x00abf998 | `UNCONDITIONAL_JUMP`
<a id="insn-00abf9d8"></a> `00abf9d8` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00abf9dc"></a> `00abf9dc` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00abf9e0"></a> `00abf9e0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abf9e4"></a> `00abf9e4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abf9e8"></a> `00abf9e8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00abf9ec"></a> `00abf9ec` | `25 60 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00abf9f0"></a> `00abf9f0` | `a8 83 5c 38` | ldurb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00abf9f4"></a> `00abf9f4` | `68 fd 07 36` | tbz w8,#0x0,0x00abf9a0 | `CONDITIONAL_JUMP`
<a id="insn-00abf9f8"></a> `00abf9f8` | `a0 83 5d f8` | ldur x0,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00abf9fc"></a> `00abf9fc` | `2d 60 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abfa00"></a> `00abfa00` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abfa04"></a> `00abfa04` | `28 fd 07 36` | tbz w8,#0x0,0x00abf9a8 | `CONDITIONAL_JUMP`
<a id="insn-00abfa08"></a> `00abfa08` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abfa0c"></a> `00abfa0c` | `29 60 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abfa10"></a> `00abfa10` | `28 ff df 08` | ldarb w8,[x25] | `FALL_THROUGH`
<a id="insn-00abfa14"></a> `00abfa14` | `48 29 00 36` | tbz w8,#0x0,0x00abff3c | `CONDITIONAL_JUMP`
<a id="insn-00abfa18"></a> `00abfa18` | `88 03 80 52` | mov w8,#0x1c | `FALL_THROUGH`
<a id="insn-00abfa1c"></a> `00abfa1c` | `f5 03 13 aa` | mov x21,x19 | `FALL_THROUGH`
<a id="insn-00abfa20"></a> `00abfa20` | `e9 bf ff 90` | adrp x9,0x2bb000 | `FALL_THROUGH`
<a id="insn-00abfa24"></a> `00abfa24` | `29 1d 20 91` | add x9,x9,#0x807 | `FALL_THROUGH`
<a id="insn-00abfa28"></a> `00abfa28` | `a8 83 1c 38` | sturb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00abfa2c"></a> `00abfa2c` | `a8 ae c7 a9` | ldp x8,x11,[x21, #0x78]! | `FALL_THROUGH`
<a id="insn-00abfa30"></a> `00abfa30` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00abfa34"></a> `00abfa34` | `29 61 40 f8` | ldur x9,[x9, #0x6] | `FALL_THROUGH`
<a id="insn-00abfa38"></a> `00abfa38` | `bf 73 1d 38` | sturb wzr,[x29, #-0x29] | `FALL_THROUGH`
<a id="insn-00abfa3c"></a> `00abfa3c` | `7f 01 08 eb` | cmp x11,x8 | `FALL_THROUGH`
<a id="insn-00abfa40"></a> `00abfa40` | `aa 93 1c f8` | stur x10,[x29, #-0x37] | `FALL_THROUGH`
<a id="insn-00abfa44"></a> `00abfa44` | `a9 f3 1c f8` | stur x9,[x29, #-0x31] | `FALL_THROUGH`
<a id="insn-00abfa48"></a> `00abfa48` | `40 2a 00 54` | b.eq 0x00abff90 | `CONDITIONAL_JUMP`
<a id="insn-00abfa4c"></a> `00abfa4c` | `02 01 40 b9` | ldr w2,[x8] | `FALL_THROUGH`
<a id="insn-00abfa50"></a> `00abfa50` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00abfa54"></a> `00abfa54` | `a0 e3 00 d1` | sub x0,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00abfa58"></a> `00abfa58` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00abfa5c"></a> `00abfa5c` | `16 21 e6 97` | bl 0x00447eb4 | `UNCONDITIONAL_CALL`
<a id="insn-00abfa60"></a> `00abfa60` | `e9 bf ff b0` | adrp x9,0x2bc000 | `FALL_THROUGH`
<a id="insn-00abfa64"></a> `00abfa64` | `29 b9 2a 91` | add x9,x9,#0xaae | `FALL_THROUGH`
<a id="insn-00abfa68"></a> `00abfa68` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00abfa6c"></a> `00abfa6c` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00abfa70"></a> `00abfa70` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abfa74"></a> `00abfa74` | `ff c7 00 39` | strb wzr,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00abfa78"></a> `00abfa78` | `e0 13 82 3c` | stur q0,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00abfa7c"></a> `00abfa7c` | `36 0f 00 b0` | adrp x22,0xca4000 | `FALL_THROUGH`
<a id="insn-00abfa80"></a> `00abfa80` | `d6 02 2c 91` | add x22,x22,#0xb00 | `FALL_THROUGH`
<a id="insn-00abfa84"></a> `00abfa84` | `e8 03 01 91` | add x8,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00abfa88"></a> `00abfa88` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00abfa8c"></a> `00abfa8c` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00abfa90"></a> `00abfa90` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00abfa94"></a> `00abfa94` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-00abfa98"></a> `00abfa98` | `cd fa e6 97` | bl 0x0047e5cc | `UNCONDITIONAL_CALL`
<a id="insn-00abfa9c"></a> `00abfa9c` | `e0 13 c0 3d` | ldr q0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abfaa0"></a> `00abfaa0` | `97 32 40 f9` | ldr x23,[x20, #0x60] | `FALL_THROUGH`
<a id="insn-00abfaa4"></a> `00abfaa4` | `ff 7f 04 a9` | stp xzr,xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abfaa8"></a> `00abfaa8` | `80 82 85 3c` | stur q0,[x20, #0x58] | `FALL_THROUGH`
<a id="insn-00abfaac"></a> `00abfaac` | `b7 00 00 b4` | cbz x23,0x00abfac0 | `CONDITIONAL_JUMP`
<a id="insn-00abfab0"></a> `00abfab0` | `e1 22 00 91` | add x1,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00abfab4"></a> `00abfab4` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abfab8"></a> `00abfab8` | `8a 4f 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00abfabc"></a> `00abfabc` | `40 19 00 b4` | cbz x0,0x00abfde4 | `CONDITIONAL_JUMP`
<a id="insn-00abfac0"></a> `00abfac0` | `f7 27 40 f9` | ldr x23,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00abfac4"></a> `00abfac4` | `b7 00 00 b4` | cbz x23,0x00abfad8 | `CONDITIONAL_JUMP`
<a id="insn-00abfac8"></a> `00abfac8` | `e1 22 00 91` | add x1,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00abfacc"></a> `00abfacc` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abfad0"></a> `00abfad0` | `84 4f 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00abfad4"></a> `00abfad4` | `a0 19 00 b4` | cbz x0,0x00abfe08 | `CONDITIONAL_JUMP`
<a id="insn-00abfad8"></a> `00abfad8` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abfadc"></a> `00abfadc` | `68 1a 00 37` | tbnz w8,#0x0,0x00abfe28 | `CONDITIONAL_JUMP`
<a id="insn-00abfae0"></a> `00abfae0` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abfae4"></a> `00abfae4` | `a8 1a 00 37` | tbnz w8,#0x0,0x00abfe38 | `CONDITIONAL_JUMP`
<a id="insn-00abfae8"></a> `00abfae8` | `a8 83 5c 38` | ldurb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00abfaec"></a> `00abfaec` | `68 00 00 36` | tbz w8,#0x0,0x00abfaf8 | `CONDITIONAL_JUMP`
<a id="insn-00abfaf0"></a> `00abfaf0` | `a0 83 5d f8` | ldur x0,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00abfaf4"></a> `00abfaf4` | `ef 5f 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abfaf8"></a> `00abfaf8` | `69 a2 47 a9` | ldp x9,x8,[x19, #0x78] | `FALL_THROUGH`
<a id="insn-00abfafc"></a> `00abfafc` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00abfb00"></a> `00abfb00` | `1f 15 00 f1` | cmp x8,#0x5 | `FALL_THROUGH`
<a id="insn-00abfb04"></a> `00abfb04` | `83 09 00 54` | b.cc 0x00abfc34 | `CONDITIONAL_JUMP`
<a id="insn-00abfb08"></a> `00abfb08` | `28 ff df 08` | ldarb w8,[x25] | `FALL_THROUGH`
<a id="insn-00abfb0c"></a> `00abfb0c` | `e8 24 00 36` | tbz w8,#0x0,0x00abffa8 | `CONDITIONAL_JUMP`
<a id="insn-00abfb10"></a> `00abfb10` | `09 bf ff d0` | adrp x9,0x2a1000 | `FALL_THROUGH`
<a id="insn-00abfb14"></a> `00abfb14` | `29 19 1f 91` | add x9,x9,#0x7c6 | `FALL_THROUGH`
<a id="insn-00abfb18"></a> `00abfb18` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-00abfb1c"></a> `00abfb1c` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00abfb20"></a> `00abfb20` | `8a 4e 86 52` | mov w10,#0x3274 | `FALL_THROUGH`
<a id="insn-00abfb24"></a> `00abfb24` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abfb28"></a> `00abfb28` | `ea 93 02 78` | sturh w10,[sp, #0x29] | `FALL_THROUGH`
<a id="insn-00abfb2c"></a> `00abfb2c` | `e9 13 02 f8` | stur x9,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00abfb30"></a> `00abfb30` | `ff af 00 39` | strb wzr,[sp, #0x2b] | `FALL_THROUGH`
<a id="insn-00abfb34"></a> `00abfb34` | `a8 e3 00 d1` | sub x8,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00abfb38"></a> `00abfb38` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00abfb3c"></a> `00abfb3c` | `b6 34 e7 97` | bl 0x0048ce14 | `UNCONDITIONAL_CALL`
<a id="insn-00abfb40"></a> `00abfb40` | `69 a2 47 a9` | ldp x9,x8,[x19, #0x78] | `FALL_THROUGH`
<a id="insn-00abfb44"></a> `00abfb44` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00abfb48"></a> `00abfb48` | `02 fd 42 d3` | lsr x2,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00abfb4c"></a> `00abfb4c` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00abfb50"></a> `00abfb50` | `a0 e3 00 d1` | sub x0,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00abfb54"></a> `00abfb54` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00abfb58"></a> `00abfb58` | `d7 20 e6 97` | bl 0x00447eb4 | `UNCONDITIONAL_CALL`
<a id="insn-00abfb5c"></a> `00abfb5c` | `c2 0e 00 f0` | adrp x2,0xc9a000 | `FALL_THROUGH`
<a id="insn-00abfb60"></a> `00abfb60` | `20 0f 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00abfb64"></a> `00abfb64` | `00 00 2c 91` | add x0,x0,#0xb00 | `FALL_THROUGH`
<a id="insn-00abfb68"></a> `00abfb68` | `42 50 44 f9` | ldr x2,[x2, #0x8a0] | `FALL_THROUGH`
<a id="insn-00abfb6c"></a> `00abfb6c` | `e8 03 01 91` | add x8,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00abfb70"></a> `00abfb70` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00abfb74"></a> `00abfb74` | `83 02 80 52` | mov w3,#0x14 | `FALL_THROUGH`
<a id="insn-00abfb78"></a> `00abfb78` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00abfb7c"></a> `00abfb7c` | `e5 03 1f 2a` | mov w5,wzr | `FALL_THROUGH`
<a id="insn-00abfb80"></a> `00abfb80` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-00abfb84"></a> `00abfb84` | `46 fb e6 97` | bl 0x0047e89c | `UNCONDITIONAL_CALL`
<a id="insn-00abfb88"></a> `00abfb88` | `e0 13 c0 3d` | ldr q0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abfb8c"></a> `00abfb8c` | `95 3a 40 f9` | ldr x21,[x20, #0x70] | `FALL_THROUGH`
<a id="insn-00abfb90"></a> `00abfb90` | `ff 7f 04 a9` | stp xzr,xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abfb94"></a> `00abfb94` | `80 82 86 3c` | stur q0,[x20, #0x68] | `FALL_THROUGH`
<a id="insn-00abfb98"></a> `00abfb98` | `75 01 00 b4` | cbz x21,0x00abfbc4 | `CONDITIONAL_JUMP`
<a id="insn-00abfb9c"></a> `00abfb9c` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00abfba0"></a> `00abfba0` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abfba4"></a> `00abfba4` | `4f 4f 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00abfba8"></a> `00abfba8` | `e0 00 00 b5` | cbnz x0,0x00abfbc4 | `CONDITIONAL_JUMP`
<a id="insn-00abfbac"></a> `00abfbac` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00abfbb0"></a> `00abfbb0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abfbb4"></a> `00abfbb4` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abfbb8"></a> `00abfbb8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abfbbc"></a> `00abfbbc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abfbc0"></a> `00abfbc0` | `b0 5f 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00abfbc4"></a> `00abfbc4` | `f4 27 40 f9` | ldr x20,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00abfbc8"></a> `00abfbc8` | `b4 00 00 b4` | cbz x20,0x00abfbdc | `CONDITIONAL_JUMP`
<a id="insn-00abfbcc"></a> `00abfbcc` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00abfbd0"></a> `00abfbd0` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abfbd4"></a> `00abfbd4` | `43 4f 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00abfbd8"></a> `00abfbd8` | `a0 13 00 b4` | cbz x0,0x00abfe4c | `CONDITIONAL_JUMP`
<a id="insn-00abfbdc"></a> `00abfbdc` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abfbe0"></a> `00abfbe0` | `68 14 00 37` | tbnz w8,#0x0,0x00abfe6c | `CONDITIONAL_JUMP`
<a id="insn-00abfbe4"></a> `00abfbe4` | `a8 83 5c 38` | ldurb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00abfbe8"></a> `00abfbe8` | `a8 14 00 37` | tbnz w8,#0x0,0x00abfe7c | `CONDITIONAL_JUMP`
<a id="insn-00abfbec"></a> `00abfbec` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abfbf0"></a> `00abfbf0` | `68 00 00 36` | tbz w8,#0x0,0x00abfbfc | `CONDITIONAL_JUMP`
<a id="insn-00abfbf4"></a> `00abfbf4` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abfbf8"></a> `00abfbf8` | `ae 5f 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abfbfc"></a> `00abfbfc` | `89 bf ff 90` | adrp x9,0x2af000 | `FALL_THROUGH`
<a id="insn-00abfc00"></a> `00abfc00` | `29 f9 3a 91` | add x9,x9,#0xebe | `FALL_THROUGH`
<a id="insn-00abfc04"></a> `00abfc04` | `2a cc 8d 52` | mov w10,#0x6e61 | `FALL_THROUGH`
<a id="insn-00abfc08"></a> `00abfc08` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00abfc0c"></a> `00abfc0c` | `c8 04 80 52` | mov w8,#0x26 | `FALL_THROUGH`
<a id="insn-00abfc10"></a> `00abfc10` | `2a ad ad 72` | movk w10,#0x6d69, LSL #16 | `FALL_THROUGH`
<a id="insn-00abfc14"></a> `00abfc14` | `a8 03 1e 38` | sturb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abfc18"></a> `00abfc18` | `aa 03 1f b8` | stur w10,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abfc1c"></a> `00abfc1c` | `a0 13 9e 3c` | stur q0,[x29, #-0x1f] | `FALL_THROUGH`
<a id="insn-00abfc20"></a> `00abfc20` | `bf 43 1f 38` | sturb wzr,[x29, #-0xc] | `FALL_THROUGH`
<a id="insn-00abfc24"></a> `00abfc24` | `60 42 05 91` | add x0,x19,#0x150 | `FALL_THROUGH`
<a id="insn-00abfc28"></a> `00abfc28` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00abfc2c"></a> `00abfc2c` | `41 bb e6 97` | bl 0x0046e930 | `UNCONDITIONAL_CALL`
<a id="insn-00abfc30"></a> `00abfc30` | `5e 00 00 14` | b 0x00abfda8 | `UNCONDITIONAL_JUMP`
<a id="insn-00abfc34"></a> `00abfc34` | `28 ff df 08` | ldarb w8,[x25] | `FALL_THROUGH`
<a id="insn-00abfc38"></a> `00abfc38` | `28 1e 00 36` | tbz w8,#0x0,0x00abfffc | `CONDITIONAL_JUMP`
<a id="insn-00abfc3c"></a> `00abfc3c` | `09 bf ff d0` | adrp x9,0x2a1000 | `FALL_THROUGH`
<a id="insn-00abfc40"></a> `00abfc40` | `29 45 1f 91` | add x9,x9,#0x7d1 | `FALL_THROUGH`
<a id="insn-00abfc44"></a> `00abfc44` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-00abfc48"></a> `00abfc48` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00abfc4c"></a> `00abfc4c` | `8a 2e 86 52` | mov w10,#0x3174 | `FALL_THROUGH`
<a id="insn-00abfc50"></a> `00abfc50` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abfc54"></a> `00abfc54` | `ea 93 02 78` | sturh w10,[sp, #0x29] | `FALL_THROUGH`
<a id="insn-00abfc58"></a> `00abfc58` | `e9 13 02 f8` | stur x9,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00abfc5c"></a> `00abfc5c` | `ff af 00 39` | strb wzr,[sp, #0x2b] | `FALL_THROUGH`
<a id="insn-00abfc60"></a> `00abfc60` | `a8 e3 00 d1` | sub x8,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00abfc64"></a> `00abfc64` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00abfc68"></a> `00abfc68` | `6b 34 e7 97` | bl 0x0048ce14 | `UNCONDITIONAL_CALL`
<a id="insn-00abfc6c"></a> `00abfc6c` | `68 a6 47 a9` | ldp x8,x9,[x19, #0x78] | `FALL_THROUGH`
<a id="insn-00abfc70"></a> `00abfc70` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00abfc74"></a> `00abfc74` | `e0 1e 00 54` | b.eq 0x00ac0050 | `CONDITIONAL_JUMP`
<a id="insn-00abfc78"></a> `00abfc78` | `69 2a 40 a9` | ldp x9,x10,[x19] | `FALL_THROUGH`
<a id="insn-00abfc7c"></a> `00abfc7c` | `08 01 80 b9` | ldrsw x8,[x8] | `FALL_THROUGH`
<a id="insn-00abfc80"></a> `00abfc80` | `4a 01 09 cb` | sub x10,x10,x9 | `FALL_THROUGH`
<a id="insn-00abfc84"></a> `00abfc84` | `1f 0d 8a eb` | cmp x8,x10, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00abfc88"></a> `00abfc88` | `02 1f 00 54` | b.cs 0x00ac0068 | `CONDITIONAL_JUMP`
<a id="insn-00abfc8c"></a> `00abfc8c` | `28 79 68 f8` | ldr x8,[x9, x8, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00abfc90"></a> `00abfc90` | `e9 03 08 aa` | mov x9,x8 | `FALL_THROUGH`
<a id="insn-00abfc94"></a> `00abfc94` | `2a 0d 48 38` | ldrb w10,[x9, #0x80]! | `FALL_THROUGH`
<a id="insn-00abfc98"></a> `00abfc98` | `ca 00 00 37` | tbnz w10,#0x0,0x00abfcb0 | `CONDITIONAL_JUMP`
<a id="insn-00abfc9c"></a> `00abfc9c` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00abfca0"></a> `00abfca0` | `28 09 40 f9` | ldr x8,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00abfca4"></a> `00abfca4` | `e0 03 80 3d` | str q0,[sp] | `FALL_THROUGH`
<a id="insn-00abfca8"></a> `00abfca8` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abfcac"></a> `00abfcac` | `04 00 00 14` | b 0x00abfcbc | `UNCONDITIONAL_JUMP`
<a id="insn-00abfcb0"></a> `00abfcb0` | `02 85 48 a9` | ldp x2,x1,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00abfcb4"></a> `00abfcb4` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00abfcb8"></a> `00abfcb8` | `8a ef e5 97` | bl 0x0043bae0 | `UNCONDITIONAL_CALL`
<a id="insn-00abfcbc"></a> `00abfcbc` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00abfcc0"></a> `00abfcc0` | `a0 e3 00 d1` | sub x0,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00abfcc4"></a> `00abfcc4` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00abfcc8"></a> `00abfcc8` | `40 4c e7 97` | bl 0x00492dc8 | `UNCONDITIONAL_CALL`
<a id="insn-00abfccc"></a> `00abfccc` | `c2 0e 00 f0` | adrp x2,0xc9a000 | `FALL_THROUGH`
<a id="insn-00abfcd0"></a> `00abfcd0` | `20 0f 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00abfcd4"></a> `00abfcd4` | `00 00 2c 91` | add x0,x0,#0xb00 | `FALL_THROUGH`
<a id="insn-00abfcd8"></a> `00abfcd8` | `42 50 44 f9` | ldr x2,[x2, #0x8a0] | `FALL_THROUGH`
<a id="insn-00abfcdc"></a> `00abfcdc` | `e8 03 01 91` | add x8,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00abfce0"></a> `00abfce0` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00abfce4"></a> `00abfce4` | `83 02 80 52` | mov w3,#0x14 | `FALL_THROUGH`
<a id="insn-00abfce8"></a> `00abfce8` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00abfcec"></a> `00abfcec` | `e5 03 1f 2a` | mov w5,wzr | `FALL_THROUGH`
<a id="insn-00abfcf0"></a> `00abfcf0` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-00abfcf4"></a> `00abfcf4` | `ea fa e6 97` | bl 0x0047e89c | `UNCONDITIONAL_CALL`
<a id="insn-00abfcf8"></a> `00abfcf8` | `e0 13 c0 3d` | ldr q0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abfcfc"></a> `00abfcfc` | `95 3a 40 f9` | ldr x21,[x20, #0x70] | `FALL_THROUGH`
<a id="insn-00abfd00"></a> `00abfd00` | `ff 7f 04 a9` | stp xzr,xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abfd04"></a> `00abfd04` | `80 82 86 3c` | stur q0,[x20, #0x68] | `FALL_THROUGH`
<a id="insn-00abfd08"></a> `00abfd08` | `75 01 00 b4` | cbz x21,0x00abfd34 | `CONDITIONAL_JUMP`
<a id="insn-00abfd0c"></a> `00abfd0c` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00abfd10"></a> `00abfd10` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abfd14"></a> `00abfd14` | `f3 4e 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00abfd18"></a> `00abfd18` | `e0 00 00 b5` | cbnz x0,0x00abfd34 | `CONDITIONAL_JUMP`
<a id="insn-00abfd1c"></a> `00abfd1c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00abfd20"></a> `00abfd20` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abfd24"></a> `00abfd24` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abfd28"></a> `00abfd28` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abfd2c"></a> `00abfd2c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abfd30"></a> `00abfd30` | `54 5f 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00abfd34"></a> `00abfd34` | `f4 27 40 f9` | ldr x20,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00abfd38"></a> `00abfd38` | `b4 00 00 b4` | cbz x20,0x00abfd4c | `CONDITIONAL_JUMP`
<a id="insn-00abfd3c"></a> `00abfd3c` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00abfd40"></a> `00abfd40` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abfd44"></a> `00abfd44` | `e7 4e 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00abfd48"></a> `00abfd48` | `40 0a 00 b4` | cbz x0,0x00abfe90 | `CONDITIONAL_JUMP`
<a id="insn-00abfd4c"></a> `00abfd4c` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abfd50"></a> `00abfd50` | `08 0b 00 37` | tbnz w8,#0x0,0x00abfeb0 | `CONDITIONAL_JUMP`
<a id="insn-00abfd54"></a> `00abfd54` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00abfd58"></a> `00abfd58` | `48 0b 00 37` | tbnz w8,#0x0,0x00abfec0 | `CONDITIONAL_JUMP`
<a id="insn-00abfd5c"></a> `00abfd5c` | `a8 83 5c 38` | ldurb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00abfd60"></a> `00abfd60` | `88 0b 00 37` | tbnz w8,#0x0,0x00abfed0 | `CONDITIONAL_JUMP`
<a id="insn-00abfd64"></a> `00abfd64` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abfd68"></a> `00abfd68` | `68 00 00 36` | tbz w8,#0x0,0x00abfd74 | `CONDITIONAL_JUMP`
<a id="insn-00abfd6c"></a> `00abfd6c` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abfd70"></a> `00abfd70` | `50 5f 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abfd74"></a> `00abfd74` | `c9 bf ff 90` | adrp x9,0x2b7000 | `FALL_THROUGH`
<a id="insn-00abfd78"></a> `00abfd78` | `29 f5 2d 91` | add x9,x9,#0xb7d | `FALL_THROUGH`
<a id="insn-00abfd7c"></a> `00abfd7c` | `2a cc 8d 52` | mov w10,#0x6e61 | `FALL_THROUGH`
<a id="insn-00abfd80"></a> `00abfd80` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00abfd84"></a> `00abfd84` | `c8 04 80 52` | mov w8,#0x26 | `FALL_THROUGH`
<a id="insn-00abfd88"></a> `00abfd88` | `2a ad ad 72` | movk w10,#0x6d69, LSL #16 | `FALL_THROUGH`
<a id="insn-00abfd8c"></a> `00abfd8c` | `a8 03 1e 38` | sturb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abfd90"></a> `00abfd90` | `aa 03 1f b8` | stur w10,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abfd94"></a> `00abfd94` | `a0 13 9e 3c` | stur q0,[x29, #-0x1f] | `FALL_THROUGH`
<a id="insn-00abfd98"></a> `00abfd98` | `bf 43 1f 38` | sturb wzr,[x29, #-0xc] | `FALL_THROUGH`
<a id="insn-00abfd9c"></a> `00abfd9c` | `60 42 05 91` | add x0,x19,#0x150 | `FALL_THROUGH`
<a id="insn-00abfda0"></a> `00abfda0` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00abfda4"></a> `00abfda4` | `e3 ba e6 97` | bl 0x0046e930 | `UNCONDITIONAL_CALL`
<a id="insn-00abfda8"></a> `00abfda8` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abfdac"></a> `00abfdac` | `68 00 00 36` | tbz w8,#0x0,0x00abfdb8 | `CONDITIONAL_JUMP`
<a id="insn-00abfdb0"></a> `00abfdb0` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abfdb4"></a> `00abfdb4` | `3f 5f 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abfdb8"></a> `00abfdb8` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00abfdbc"></a> `00abfdbc` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abfdc0"></a> `00abfdc0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abfdc4"></a> `00abfdc4` | `01 1f 00 54` | b.ne 0x00ac01a4 | `CONDITIONAL_JUMP`
<a id="insn-00abfdc8"></a> `00abfdc8` | `f4 4f 4d a9` | ldp x20,x19,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00abfdcc"></a> `00abfdcc` | `f9 53 40 f9` | ldr x25,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00abfdd0"></a> `00abfdd0` | `f6 57 4c a9` | ldp x22,x21,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00abfdd4"></a> `00abfdd4` | `f8 5f 4b a9` | ldp x24,x23,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00abfdd8"></a> `00abfdd8` | `fd 7b 49 a9` | ldp x29,x30,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abfddc"></a> `00abfddc` | `ff 83 03 91` | add sp,sp,#0xe0 | `FALL_THROUGH`
<a id="insn-00abfde0"></a> `00abfde0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00abfde4"></a> `00abfde4` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00abfde8"></a> `00abfde8` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00abfdec"></a> `00abfdec` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abfdf0"></a> `00abfdf0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abfdf4"></a> `00abfdf4` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00abfdf8"></a> `00abfdf8` | `22 5f 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00abfdfc"></a> `00abfdfc` | `f7 27 40 f9` | ldr x23,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00abfe00"></a> `00abfe00` | `57 e6 ff b5` | cbnz x23,0x00abfac8 | `CONDITIONAL_JUMP`
<a id="insn-00abfe04"></a> `00abfe04` | `35 ff ff 17` | b 0x00abfad8 | `UNCONDITIONAL_JUMP`
<a id="insn-00abfe08"></a> `00abfe08` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00abfe0c"></a> `00abfe0c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00abfe10"></a> `00abfe10` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abfe14"></a> `00abfe14` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abfe18"></a> `00abfe18` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00abfe1c"></a> `00abfe1c` | `19 5f 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00abfe20"></a> `00abfe20` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abfe24"></a> `00abfe24` | `e8 e5 07 36` | tbz w8,#0x0,0x00abfae0 | `CONDITIONAL_JUMP`
<a id="insn-00abfe28"></a> `00abfe28` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abfe2c"></a> `00abfe2c` | `21 5f 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abfe30"></a> `00abfe30` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abfe34"></a> `00abfe34` | `a8 e5 07 36` | tbz w8,#0x0,0x00abfae8 | `CONDITIONAL_JUMP`
<a id="insn-00abfe38"></a> `00abfe38` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abfe3c"></a> `00abfe3c` | `1d 5f 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abfe40"></a> `00abfe40` | `a8 83 5c 38` | ldurb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00abfe44"></a> `00abfe44` | `68 e5 07 37` | tbnz w8,#0x0,0x00abfaf0 | `CONDITIONAL_JUMP`
<a id="insn-00abfe48"></a> `00abfe48` | `2c ff ff 17` | b 0x00abfaf8 | `UNCONDITIONAL_JUMP`
<a id="insn-00abfe4c"></a> `00abfe4c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00abfe50"></a> `00abfe50` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abfe54"></a> `00abfe54` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abfe58"></a> `00abfe58` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abfe5c"></a> `00abfe5c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abfe60"></a> `00abfe60` | `08 5f 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00abfe64"></a> `00abfe64` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abfe68"></a> `00abfe68` | `e8 eb 07 36` | tbz w8,#0x0,0x00abfbe4 | `CONDITIONAL_JUMP`
<a id="insn-00abfe6c"></a> `00abfe6c` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abfe70"></a> `00abfe70` | `10 5f 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abfe74"></a> `00abfe74` | `a8 83 5c 38` | ldurb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00abfe78"></a> `00abfe78` | `a8 eb 07 36` | tbz w8,#0x0,0x00abfbec | `CONDITIONAL_JUMP`
<a id="insn-00abfe7c"></a> `00abfe7c` | `a0 83 5d f8` | ldur x0,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00abfe80"></a> `00abfe80` | `0c 5f 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abfe84"></a> `00abfe84` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abfe88"></a> `00abfe88` | `68 eb 07 37` | tbnz w8,#0x0,0x00abfbf4 | `CONDITIONAL_JUMP`
<a id="insn-00abfe8c"></a> `00abfe8c` | `5c ff ff 17` | b 0x00abfbfc | `UNCONDITIONAL_JUMP`
<a id="insn-00abfe90"></a> `00abfe90` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00abfe94"></a> `00abfe94` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abfe98"></a> `00abfe98` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abfe9c"></a> `00abfe9c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abfea0"></a> `00abfea0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abfea4"></a> `00abfea4` | `f7 5e 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00abfea8"></a> `00abfea8` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abfeac"></a> `00abfeac` | `48 f5 07 36` | tbz w8,#0x0,0x00abfd54 | `CONDITIONAL_JUMP`
<a id="insn-00abfeb0"></a> `00abfeb0` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abfeb4"></a> `00abfeb4` | `ff 5e 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abfeb8"></a> `00abfeb8` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00abfebc"></a> `00abfebc` | `08 f5 07 36` | tbz w8,#0x0,0x00abfd5c | `CONDITIONAL_JUMP`
<a id="insn-00abfec0"></a> `00abfec0` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abfec4"></a> `00abfec4` | `fb 5e 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abfec8"></a> `00abfec8` | `a8 83 5c 38` | ldurb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00abfecc"></a> `00abfecc` | `c8 f4 07 36` | tbz w8,#0x0,0x00abfd64 | `CONDITIONAL_JUMP`
<a id="insn-00abfed0"></a> `00abfed0` | `a0 83 5d f8` | ldur x0,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00abfed4"></a> `00abfed4` | `f7 5e 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00abfed8"></a> `00abfed8` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abfedc"></a> `00abfedc` | `88 f4 07 37` | tbnz w8,#0x0,0x00abfd6c | `CONDITIONAL_JUMP`
<a id="insn-00abfee0"></a> `00abfee0` | `a5 ff ff 17` | b 0x00abfd74 | `UNCONDITIONAL_JUMP`
<a id="insn-00abfee4"></a> `00abfee4` | `20 0f 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00abfee8"></a> `00abfee8` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00abfeec"></a> `00abfeec` | `d9 5e 06 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-00abfef0"></a> `00abfef0` | `40 d0 ff 34` | cbz w0,0x00abf8f8 | `CONDITIONAL_JUMP`
<a id="insn-00abfef4"></a> `00abfef4` | `21 0f 00 b0` | adrp x1,0xca4000 | `FALL_THROUGH`
<a id="insn-00abfef8"></a> `00abfef8` | `21 00 2c 91` | add x1,x1,#0xb00 | `FALL_THROUGH`
<a id="insn-00abfefc"></a> `00abfefc` | `e0 cd ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-00abff00"></a> `00abff00` | `00 d0 35 91` | add x0,x0,#0xd74 | `FALL_THROUGH`
<a id="insn-00abff04"></a> `00abff04` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00abff08"></a> `00abff08` | `02 0d 00 f0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-00abff0c"></a> `00abff0c` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-00abff10"></a> `00abff10` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00abff14"></a> `00abff14` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00abff18"></a> `00abff18` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00abff1c"></a> `00abff1c` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00abff20"></a> `00abff20` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00abff24"></a> `00abff24` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00abff28"></a> `00abff28` | `c2 5e 06 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-00abff2c"></a> `00abff2c` | `20 0f 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00abff30"></a> `00abff30` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00abff34"></a> `00abff34` | `cf 5e 06 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-00abff38"></a> `00abff38` | `70 fe ff 17` | b 0x00abf8f8 | `UNCONDITIONAL_JUMP`
<a id="insn-00abff3c"></a> `00abff3c` | `20 0f 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00abff40"></a> `00abff40` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00abff44"></a> `00abff44` | `c3 5e 06 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-00abff48"></a> `00abff48` | `80 d6 ff 34` | cbz w0,0x00abfa18 | `CONDITIONAL_JUMP`
<a id="insn-00abff4c"></a> `00abff4c` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00abff50"></a> `00abff50` | `e0 cd ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-00abff54"></a> `00abff54` | `00 d0 35 91` | add x0,x0,#0xd74 | `FALL_THROUGH`
<a id="insn-00abff58"></a> `00abff58` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00abff5c"></a> `00abff5c` | `02 0d 00 f0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-00abff60"></a> `00abff60` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-00abff64"></a> `00abff64` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00abff68"></a> `00abff68` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00abff6c"></a> `00abff6c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00abff70"></a> `00abff70` | `bf fe 02 a9` | stp xzr,xzr,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00abff74"></a> `00abff74` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00abff78"></a> `00abff78` | `bf 22 01 a9` | stp xzr,x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00abff7c"></a> `00abff7c` | `ad 5e 06 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-00abff80"></a> `00abff80` | `20 0f 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00abff84"></a> `00abff84` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00abff88"></a> `00abff88` | `ba 5e 06 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-00abff8c"></a> `00abff8c` | `a3 fe ff 17` | b 0x00abfa18 | `UNCONDITIONAL_JUMP`
<a id="insn-00abff90"></a> `00abff90` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00abff94"></a> `00abff94` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abff98"></a> `00abff98` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abff9c"></a> `00abff9c` | `41 10 00 54` | b.ne 0x00ac01a4 | `CONDITIONAL_JUMP`
<a id="insn-00abffa0"></a> `00abffa0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abffa4"></a> `00abffa4` | `03 7d e7 97` | bl 0x0049f3b0 | `CALL_TERMINATOR`
<a id="insn-00abffa8"></a> `00abffa8` | `20 0f 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00abffac"></a> `00abffac` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00abffb0"></a> `00abffb0` | `a8 5e 06 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-00abffb4"></a> `00abffb4` | `e0 da ff 34` | cbz w0,0x00abfb10 | `CONDITIONAL_JUMP`
<a id="insn-00abffb8"></a> `00abffb8` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00abffbc"></a> `00abffbc` | `e0 cd ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-00abffc0"></a> `00abffc0` | `00 d0 35 91` | add x0,x0,#0xd74 | `FALL_THROUGH`
<a id="insn-00abffc4"></a> `00abffc4` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00abffc8"></a> `00abffc8` | `02 0d 00 f0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-00abffcc"></a> `00abffcc` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-00abffd0"></a> `00abffd0` | `c8 02 00 f9` | str x8,[x22] | `FALL_THROUGH`
<a id="insn-00abffd4"></a> `00abffd4` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00abffd8"></a> `00abffd8` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00abffdc"></a> `00abffdc` | `df fe 02 a9` | stp xzr,xzr,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00abffe0"></a> `00abffe0` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00abffe4"></a> `00abffe4` | `df 22 01 a9` | stp xzr,x8,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00abffe8"></a> `00abffe8` | `92 5e 06 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-00abffec"></a> `00abffec` | `20 0f 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00abfff0"></a> `00abfff0` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00abfff4"></a> `00abfff4` | `9f 5e 06 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-00abfff8"></a> `00abfff8` | `c6 fe ff 17` | b 0x00abfb10 | `UNCONDITIONAL_JUMP`
<a id="insn-00abfffc"></a> `00abfffc` | `20 0f 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00ac0000"></a> `00ac0000` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00ac0004"></a> `00ac0004` | `93 5e 06 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-00ac0008"></a> `00ac0008` | `a0 e1 ff 34` | cbz w0,0x00abfc3c | `CONDITIONAL_JUMP`
<a id="insn-00ac000c"></a> `00ac000c` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00ac0010"></a> `00ac0010` | `e0 cd ff d0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-00ac0014"></a> `00ac0014` | `00 d0 35 91` | add x0,x0,#0xd74 | `FALL_THROUGH`
<a id="insn-00ac0018"></a> `00ac0018` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00ac001c"></a> `00ac001c` | `02 0d 00 d0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-00ac0020"></a> `00ac0020` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-00ac0024"></a> `00ac0024` | `c8 02 00 f9` | str x8,[x22] | `FALL_THROUGH`
<a id="insn-00ac0028"></a> `00ac0028` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00ac002c"></a> `00ac002c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00ac0030"></a> `00ac0030` | `df fe 02 a9` | stp xzr,xzr,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00ac0034"></a> `00ac0034` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00ac0038"></a> `00ac0038` | `df 22 01 a9` | stp xzr,x8,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00ac003c"></a> `00ac003c` | `7d 5e 06 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-00ac0040"></a> `00ac0040` | `20 0f 00 90` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00ac0044"></a> `00ac0044` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-00ac0048"></a> `00ac0048` | `8a 5e 06 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-00ac004c"></a> `00ac004c` | `fc fe ff 17` | b 0x00abfc3c | `UNCONDITIONAL_JUMP`
<a id="insn-00ac0050"></a> `00ac0050` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00ac0054"></a> `00ac0054` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ac0058"></a> `00ac0058` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ac005c"></a> `00ac005c` | `41 0a 00 54` | b.ne 0x00ac01a4 | `CONDITIONAL_JUMP`
<a id="insn-00ac0060"></a> `00ac0060` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ac0064"></a> `00ac0064` | `d3 7c e7 97` | bl 0x0049f3b0 | `CALL_TERMINATOR`
<a id="insn-00ac0068"></a> `00ac0068` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00ac006c"></a> `00ac006c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ac0070"></a> `00ac0070` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ac0074"></a> `00ac0074` | `81 09 00 54` | b.ne 0x00ac01a4 | `CONDITIONAL_JUMP`
<a id="insn-00ac0078"></a> `00ac0078` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ac007c"></a> `00ac007c` | `5b 03 00 94` | bl 0x00ac0de8 | `UNCONDITIONAL_CALL`
<a id="insn-00ac0080"></a> `00ac0080` | `0c 00 00 14` | b 0x00ac00b0 | `UNCONDITIONAL_JUMP`
<a id="insn-00ac00b0"></a> `00ac00b0` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00ac00b4"></a> `00ac00b4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ac00b8"></a> `00ac00b8` | `a8 04 00 37` | tbnz w8,#0x0,0x00ac014c | `CONDITIONAL_JUMP`
<a id="insn-00ac00bc"></a> `00ac00bc` | `34 00 00 14` | b 0x00ac018c | `UNCONDITIONAL_JUMP`
<a id="insn-00ac014c"></a> `00ac014c` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00ac0150"></a> `00ac0150` | `0e 00 00 14` | b 0x00ac0188 | `UNCONDITIONAL_JUMP`
<a id="insn-00ac0188"></a> `00ac0188` | `4a 5e 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac018c"></a> `00ac018c` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00ac0190"></a> `00ac0190` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ac0194"></a> `00ac0194` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ac0198"></a> `00ac0198` | `61 00 00 54` | b.ne 0x00ac01a4 | `CONDITIONAL_JUMP`
<a id="insn-00ac019c"></a> `00ac019c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ac01a0"></a> `00ac01a0` | `67 4e 06 94` | bl 0x00c53b3c | `CALL_TERMINATOR`
<a id="insn-00ac01a4"></a> `00ac01a4` | `4f 5e 06 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00abf8ac`](#insn-00abf8ac) 範囲 `[['00abf8ac', '00abf8df']]`
  - `CONDITIONAL_JUMP` [`00abf8dc`](#insn-00abf8dc) → [`00abfdb8`](#insn-00abfdb8)
  - `FALL_THROUGH` [`00abf8dc`](#insn-00abf8dc) → [`00abf8e0`](#insn-00abf8e0)
- ブロック [`00abf8e0`](#insn-00abf8e0) 範囲 `[['00abf8e0', '00abf8f7']]`
  - `CONDITIONAL_JUMP` [`00abf8f4`](#insn-00abf8f4) → [`00abfee4`](#insn-00abfee4)
  - `FALL_THROUGH` [`00abf8f4`](#insn-00abf8f4) → [`00abf8f8`](#insn-00abf8f8)
- ブロック [`00abf8f8`](#insn-00abf8f8) 範囲 `[['00abf8f8', '00abf95b']]`
  - `FALL_THROUGH` [`00abf958`](#insn-00abf958) → [`00abf95c`](#insn-00abf95c)
- ブロック [`00abf95c`](#insn-00abf95c) 範囲 `[['00abf95c', '00abf96f']]`
  - `CONDITIONAL_JUMP` [`00abf96c`](#insn-00abf96c) → [`00abf980`](#insn-00abf980)
  - `FALL_THROUGH` [`00abf96c`](#insn-00abf96c) → [`00abf970`](#insn-00abf970)
- ブロック [`00abf970`](#insn-00abf970) 範囲 `[['00abf970', '00abf97f']]`
  - `CONDITIONAL_JUMP` [`00abf97c`](#insn-00abf97c) → [`00abf9b4`](#insn-00abf9b4)
  - `FALL_THROUGH` [`00abf97c`](#insn-00abf97c) → [`00abf980`](#insn-00abf980)
- ブロック [`00abf980`](#insn-00abf980) 範囲 `[['00abf980', '00abf987']]`
  - `CONDITIONAL_JUMP` [`00abf984`](#insn-00abf984) → [`00abf998`](#insn-00abf998)
  - `FALL_THROUGH` [`00abf984`](#insn-00abf984) → [`00abf988`](#insn-00abf988)
- ブロック [`00abf988`](#insn-00abf988) 範囲 `[['00abf988', '00abf98b']]`
  - `FALL_THROUGH` [`00abf988`](#insn-00abf988) → [`00abf98c`](#insn-00abf98c)
- ブロック [`00abf98c`](#insn-00abf98c) 範囲 `[['00abf98c', '00abf997']]`
  - `CONDITIONAL_JUMP` [`00abf994`](#insn-00abf994) → [`00abf9d8`](#insn-00abf9d8)
  - `FALL_THROUGH` [`00abf994`](#insn-00abf994) → [`00abf998`](#insn-00abf998)
- ブロック [`00abf998`](#insn-00abf998) 範囲 `[['00abf998', '00abf99f']]`
  - `CONDITIONAL_JUMP` [`00abf99c`](#insn-00abf99c) → [`00abf9f8`](#insn-00abf9f8)
  - `FALL_THROUGH` [`00abf99c`](#insn-00abf99c) → [`00abf9a0`](#insn-00abf9a0)
- ブロック [`00abf9a0`](#insn-00abf9a0) 範囲 `[['00abf9a0', '00abf9a7']]`
  - `CONDITIONAL_JUMP` [`00abf9a4`](#insn-00abf9a4) → [`00abfa08`](#insn-00abfa08)
  - `FALL_THROUGH` [`00abf9a4`](#insn-00abf9a4) → [`00abf9a8`](#insn-00abf9a8)
- ブロック [`00abf9a8`](#insn-00abf9a8) 範囲 `[['00abf9a8', '00abf9af']]`
  - `CONDITIONAL_JUMP` [`00abf9ac`](#insn-00abf9ac) → [`00abfa18`](#insn-00abfa18)
  - `FALL_THROUGH` [`00abf9ac`](#insn-00abf9ac) → [`00abf9b0`](#insn-00abf9b0)
- ブロック [`00abf9b0`](#insn-00abf9b0) 範囲 `[['00abf9b0', '00abf9b3']]`
  - `UNCONDITIONAL_JUMP` [`00abf9b0`](#insn-00abf9b0) → [`00abff3c`](#insn-00abff3c)
- ブロック [`00abf9b4`](#insn-00abf9b4) 範囲 `[['00abf9b4', '00abf9cf']]`
  - `FALL_THROUGH` [`00abf9cc`](#insn-00abf9cc) → [`00abf9d0`](#insn-00abf9d0)
- ブロック [`00abf9d0`](#insn-00abf9d0) 範囲 `[['00abf9d0', '00abf9d3']]`
  - `CONDITIONAL_JUMP` [`00abf9d0`](#insn-00abf9d0) → [`00abf988`](#insn-00abf988)
  - `FALL_THROUGH` [`00abf9d0`](#insn-00abf9d0) → [`00abf9d4`](#insn-00abf9d4)
- ブロック [`00abf9d4`](#insn-00abf9d4) 範囲 `[['00abf9d4', '00abf9d7']]`
  - `UNCONDITIONAL_JUMP` [`00abf9d4`](#insn-00abf9d4) → [`00abf998`](#insn-00abf998)
- ブロック [`00abf9d8`](#insn-00abf9d8) 範囲 `[['00abf9d8', '00abf9f7']]`
  - `CONDITIONAL_JUMP` [`00abf9f4`](#insn-00abf9f4) → [`00abf9a0`](#insn-00abf9a0)
  - `FALL_THROUGH` [`00abf9f4`](#insn-00abf9f4) → [`00abf9f8`](#insn-00abf9f8)
- ブロック [`00abf9f8`](#insn-00abf9f8) 範囲 `[['00abf9f8', '00abfa03']]`
  - `FALL_THROUGH` [`00abfa00`](#insn-00abfa00) → [`00abfa04`](#insn-00abfa04)
- ブロック [`00abfa04`](#insn-00abfa04) 範囲 `[['00abfa04', '00abfa07']]`
  - `CONDITIONAL_JUMP` [`00abfa04`](#insn-00abfa04) → [`00abf9a8`](#insn-00abf9a8)
  - `FALL_THROUGH` [`00abfa04`](#insn-00abfa04) → [`00abfa08`](#insn-00abfa08)
- ブロック [`00abfa08`](#insn-00abfa08) 範囲 `[['00abfa08', '00abfa17']]`
  - `CONDITIONAL_JUMP` [`00abfa14`](#insn-00abfa14) → [`00abff3c`](#insn-00abff3c)
  - `FALL_THROUGH` [`00abfa14`](#insn-00abfa14) → [`00abfa18`](#insn-00abfa18)
- ブロック [`00abfa18`](#insn-00abfa18) 範囲 `[['00abfa18', '00abfa33']]`
  - `FALL_THROUGH` [`00abfa30`](#insn-00abfa30) → [`00abfa34`](#insn-00abfa34)
- ブロック [`00abfa34`](#insn-00abfa34) 範囲 `[['00abfa34', '00abfa3f']]`
  - `FALL_THROUGH` [`00abfa3c`](#insn-00abfa3c) → [`00abfa40`](#insn-00abfa40)
- ブロック [`00abfa40`](#insn-00abfa40) 範囲 `[['00abfa40', '00abfa4b']]`
  - `CONDITIONAL_JUMP` [`00abfa48`](#insn-00abfa48) → [`00abff90`](#insn-00abff90)
  - `FALL_THROUGH` [`00abfa48`](#insn-00abfa48) → [`00abfa4c`](#insn-00abfa4c)
- ブロック [`00abfa4c`](#insn-00abfa4c) 範囲 `[['00abfa4c', '00abfa7f']]`
  - `FALL_THROUGH` [`00abfa7c`](#insn-00abfa7c) → [`00abfa80`](#insn-00abfa80)
- ブロック [`00abfa80`](#insn-00abfa80) 範囲 `[['00abfa80', '00abfaaf']]`
  - `CONDITIONAL_JUMP` [`00abfaac`](#insn-00abfaac) → [`00abfac0`](#insn-00abfac0)
  - `FALL_THROUGH` [`00abfaac`](#insn-00abfaac) → [`00abfab0`](#insn-00abfab0)
- ブロック [`00abfab0`](#insn-00abfab0) 範囲 `[['00abfab0', '00abfabf']]`
  - `CONDITIONAL_JUMP` [`00abfabc`](#insn-00abfabc) → [`00abfde4`](#insn-00abfde4)
  - `FALL_THROUGH` [`00abfabc`](#insn-00abfabc) → [`00abfac0`](#insn-00abfac0)
- ブロック [`00abfac0`](#insn-00abfac0) 範囲 `[['00abfac0', '00abfac7']]`
  - `CONDITIONAL_JUMP` [`00abfac4`](#insn-00abfac4) → [`00abfad8`](#insn-00abfad8)
  - `FALL_THROUGH` [`00abfac4`](#insn-00abfac4) → [`00abfac8`](#insn-00abfac8)
- ブロック [`00abfac8`](#insn-00abfac8) 範囲 `[['00abfac8', '00abfad7']]`
  - `CONDITIONAL_JUMP` [`00abfad4`](#insn-00abfad4) → [`00abfe08`](#insn-00abfe08)
  - `FALL_THROUGH` [`00abfad4`](#insn-00abfad4) → [`00abfad8`](#insn-00abfad8)
- ブロック [`00abfad8`](#insn-00abfad8) 範囲 `[['00abfad8', '00abfadf']]`
  - `CONDITIONAL_JUMP` [`00abfadc`](#insn-00abfadc) → [`00abfe28`](#insn-00abfe28)
  - `FALL_THROUGH` [`00abfadc`](#insn-00abfadc) → [`00abfae0`](#insn-00abfae0)
- ブロック [`00abfae0`](#insn-00abfae0) 範囲 `[['00abfae0', '00abfae7']]`
  - `CONDITIONAL_JUMP` [`00abfae4`](#insn-00abfae4) → [`00abfe38`](#insn-00abfe38)
  - `FALL_THROUGH` [`00abfae4`](#insn-00abfae4) → [`00abfae8`](#insn-00abfae8)
- ブロック [`00abfae8`](#insn-00abfae8) 範囲 `[['00abfae8', '00abfaef']]`
  - `CONDITIONAL_JUMP` [`00abfaec`](#insn-00abfaec) → [`00abfaf8`](#insn-00abfaf8)
  - `FALL_THROUGH` [`00abfaec`](#insn-00abfaec) → [`00abfaf0`](#insn-00abfaf0)
- ブロック [`00abfaf0`](#insn-00abfaf0) 範囲 `[['00abfaf0', '00abfaf7']]`
  - `FALL_THROUGH` [`00abfaf4`](#insn-00abfaf4) → [`00abfaf8`](#insn-00abfaf8)
- ブロック [`00abfaf8`](#insn-00abfaf8) 範囲 `[['00abfaf8', '00abfb07']]`
  - `CONDITIONAL_JUMP` [`00abfb04`](#insn-00abfb04) → [`00abfc34`](#insn-00abfc34)
  - `FALL_THROUGH` [`00abfb04`](#insn-00abfb04) → [`00abfb08`](#insn-00abfb08)
- ブロック [`00abfb08`](#insn-00abfb08) 範囲 `[['00abfb08', '00abfb0f']]`
  - `CONDITIONAL_JUMP` [`00abfb0c`](#insn-00abfb0c) → [`00abffa8`](#insn-00abffa8)
  - `FALL_THROUGH` [`00abfb0c`](#insn-00abfb0c) → [`00abfb10`](#insn-00abfb10)
- ブロック [`00abfb10`](#insn-00abfb10) 範囲 `[['00abfb10', '00abfb37']]`
  - `FALL_THROUGH` [`00abfb34`](#insn-00abfb34) → [`00abfb38`](#insn-00abfb38)
- ブロック [`00abfb38`](#insn-00abfb38) 範囲 `[['00abfb38', '00abfb87']]`
  - `FALL_THROUGH` [`00abfb84`](#insn-00abfb84) → [`00abfb88`](#insn-00abfb88)
- ブロック [`00abfb88`](#insn-00abfb88) 範囲 `[['00abfb88', '00abfb8f']]`
  - `FALL_THROUGH` [`00abfb8c`](#insn-00abfb8c) → [`00abfb90`](#insn-00abfb90)
- ブロック [`00abfb90`](#insn-00abfb90) 範囲 `[['00abfb90', '00abfb9b']]`
  - `CONDITIONAL_JUMP` [`00abfb98`](#insn-00abfb98) → [`00abfbc4`](#insn-00abfbc4)
  - `FALL_THROUGH` [`00abfb98`](#insn-00abfb98) → [`00abfb9c`](#insn-00abfb9c)
- ブロック [`00abfb9c`](#insn-00abfb9c) 範囲 `[['00abfb9c', '00abfbab']]`
  - `CONDITIONAL_JUMP` [`00abfba8`](#insn-00abfba8) → [`00abfbc4`](#insn-00abfbc4)
  - `FALL_THROUGH` [`00abfba8`](#insn-00abfba8) → [`00abfbac`](#insn-00abfbac)
- ブロック [`00abfbac`](#insn-00abfbac) 範囲 `[['00abfbac', '00abfbb7']]`
  - `FALL_THROUGH` [`00abfbb4`](#insn-00abfbb4) → [`00abfbb8`](#insn-00abfbb8)
- ブロック [`00abfbb8`](#insn-00abfbb8) 範囲 `[['00abfbb8', '00abfbc3']]`
  - `FALL_THROUGH` [`00abfbc0`](#insn-00abfbc0) → [`00abfbc4`](#insn-00abfbc4)
- ブロック [`00abfbc4`](#insn-00abfbc4) 範囲 `[['00abfbc4', '00abfbcb']]`
  - `CONDITIONAL_JUMP` [`00abfbc8`](#insn-00abfbc8) → [`00abfbdc`](#insn-00abfbdc)
  - `FALL_THROUGH` [`00abfbc8`](#insn-00abfbc8) → [`00abfbcc`](#insn-00abfbcc)
- ブロック [`00abfbcc`](#insn-00abfbcc) 範囲 `[['00abfbcc', '00abfbdb']]`
  - `CONDITIONAL_JUMP` [`00abfbd8`](#insn-00abfbd8) → [`00abfe4c`](#insn-00abfe4c)
  - `FALL_THROUGH` [`00abfbd8`](#insn-00abfbd8) → [`00abfbdc`](#insn-00abfbdc)
- ブロック [`00abfbdc`](#insn-00abfbdc) 範囲 `[['00abfbdc', '00abfbe3']]`
  - `CONDITIONAL_JUMP` [`00abfbe0`](#insn-00abfbe0) → [`00abfe6c`](#insn-00abfe6c)
  - `FALL_THROUGH` [`00abfbe0`](#insn-00abfbe0) → [`00abfbe4`](#insn-00abfbe4)
- ブロック [`00abfbe4`](#insn-00abfbe4) 範囲 `[['00abfbe4', '00abfbe7']]`
  - `FALL_THROUGH` [`00abfbe4`](#insn-00abfbe4) → [`00abfbe8`](#insn-00abfbe8)
- ブロック [`00abfbe8`](#insn-00abfbe8) 範囲 `[['00abfbe8', '00abfbeb']]`
  - `CONDITIONAL_JUMP` [`00abfbe8`](#insn-00abfbe8) → [`00abfe7c`](#insn-00abfe7c)
  - `FALL_THROUGH` [`00abfbe8`](#insn-00abfbe8) → [`00abfbec`](#insn-00abfbec)
- ブロック [`00abfbec`](#insn-00abfbec) 範囲 `[['00abfbec', '00abfbf3']]`
  - `CONDITIONAL_JUMP` [`00abfbf0`](#insn-00abfbf0) → [`00abfbfc`](#insn-00abfbfc)
  - `FALL_THROUGH` [`00abfbf0`](#insn-00abfbf0) → [`00abfbf4`](#insn-00abfbf4)
- ブロック [`00abfbf4`](#insn-00abfbf4) 範囲 `[['00abfbf4', '00abfbfb']]`
  - `FALL_THROUGH` [`00abfbf8`](#insn-00abfbf8) → [`00abfbfc`](#insn-00abfbfc)
- ブロック [`00abfbfc`](#insn-00abfbfc) 範囲 `[['00abfbfc', '00abfc33']]`
  - `UNCONDITIONAL_JUMP` [`00abfc30`](#insn-00abfc30) → [`00abfda8`](#insn-00abfda8)
- ブロック [`00abfc34`](#insn-00abfc34) 範囲 `[['00abfc34', '00abfc3b']]`
  - `CONDITIONAL_JUMP` [`00abfc38`](#insn-00abfc38) → [`00abfffc`](#insn-00abfffc)
  - `FALL_THROUGH` [`00abfc38`](#insn-00abfc38) → [`00abfc3c`](#insn-00abfc3c)
- ブロック [`00abfc3c`](#insn-00abfc3c) 範囲 `[['00abfc3c', '00abfc73']]`
  - `FALL_THROUGH` [`00abfc70`](#insn-00abfc70) → [`00abfc74`](#insn-00abfc74)
- ブロック [`00abfc74`](#insn-00abfc74) 範囲 `[['00abfc74', '00abfc77']]`
  - `CONDITIONAL_JUMP` [`00abfc74`](#insn-00abfc74) → [`00ac0050`](#insn-00ac0050)
  - `FALL_THROUGH` [`00abfc74`](#insn-00abfc74) → [`00abfc78`](#insn-00abfc78)
- ブロック [`00abfc78`](#insn-00abfc78) 範囲 `[['00abfc78', '00abfc7f']]`
  - `FALL_THROUGH` [`00abfc7c`](#insn-00abfc7c) → [`00abfc80`](#insn-00abfc80)
- ブロック [`00abfc80`](#insn-00abfc80) 範囲 `[['00abfc80', '00abfc8b']]`
  - `CONDITIONAL_JUMP` [`00abfc88`](#insn-00abfc88) → [`00ac0068`](#insn-00ac0068)
  - `FALL_THROUGH` [`00abfc88`](#insn-00abfc88) → [`00abfc8c`](#insn-00abfc8c)
- ブロック [`00abfc8c`](#insn-00abfc8c) 範囲 `[['00abfc8c', '00abfc9b']]`
  - `CONDITIONAL_JUMP` [`00abfc98`](#insn-00abfc98) → [`00abfcb0`](#insn-00abfcb0)
  - `FALL_THROUGH` [`00abfc98`](#insn-00abfc98) → [`00abfc9c`](#insn-00abfc9c)
- ブロック [`00abfc9c`](#insn-00abfc9c) 範囲 `[['00abfc9c', '00abfcaf']]`
  - `UNCONDITIONAL_JUMP` [`00abfcac`](#insn-00abfcac) → [`00abfcbc`](#insn-00abfcbc)
- ブロック [`00abfcb0`](#insn-00abfcb0) 範囲 `[['00abfcb0', '00abfcb3']]`
  - `FALL_THROUGH` [`00abfcb0`](#insn-00abfcb0) → [`00abfcb4`](#insn-00abfcb4)
- ブロック [`00abfcb4`](#insn-00abfcb4) 範囲 `[['00abfcb4', '00abfcbb']]`
  - `FALL_THROUGH` [`00abfcb8`](#insn-00abfcb8) → [`00abfcbc`](#insn-00abfcbc)
- ブロック [`00abfcbc`](#insn-00abfcbc) 範囲 `[['00abfcbc', '00abfcbf']]`
  - `FALL_THROUGH` [`00abfcbc`](#insn-00abfcbc) → [`00abfcc0`](#insn-00abfcc0)
- ブロック [`00abfcc0`](#insn-00abfcc0) 範囲 `[['00abfcc0', '00abfd0b']]`
  - `CONDITIONAL_JUMP` [`00abfd08`](#insn-00abfd08) → [`00abfd34`](#insn-00abfd34)
  - `FALL_THROUGH` [`00abfd08`](#insn-00abfd08) → [`00abfd0c`](#insn-00abfd0c)
- ブロック [`00abfd0c`](#insn-00abfd0c) 範囲 `[['00abfd0c', '00abfd1b']]`
  - `CONDITIONAL_JUMP` [`00abfd18`](#insn-00abfd18) → [`00abfd34`](#insn-00abfd34)
  - `FALL_THROUGH` [`00abfd18`](#insn-00abfd18) → [`00abfd1c`](#insn-00abfd1c)
- ブロック [`00abfd1c`](#insn-00abfd1c) 範囲 `[['00abfd1c', '00abfd33']]`
  - `FALL_THROUGH` [`00abfd30`](#insn-00abfd30) → [`00abfd34`](#insn-00abfd34)
- ブロック [`00abfd34`](#insn-00abfd34) 範囲 `[['00abfd34', '00abfd3b']]`
  - `CONDITIONAL_JUMP` [`00abfd38`](#insn-00abfd38) → [`00abfd4c`](#insn-00abfd4c)
  - `FALL_THROUGH` [`00abfd38`](#insn-00abfd38) → [`00abfd3c`](#insn-00abfd3c)
- ブロック [`00abfd3c`](#insn-00abfd3c) 範囲 `[['00abfd3c', '00abfd4b']]`
  - `CONDITIONAL_JUMP` [`00abfd48`](#insn-00abfd48) → [`00abfe90`](#insn-00abfe90)
  - `FALL_THROUGH` [`00abfd48`](#insn-00abfd48) → [`00abfd4c`](#insn-00abfd4c)
- ブロック [`00abfd4c`](#insn-00abfd4c) 範囲 `[['00abfd4c', '00abfd53']]`
  - `CONDITIONAL_JUMP` [`00abfd50`](#insn-00abfd50) → [`00abfeb0`](#insn-00abfeb0)
  - `FALL_THROUGH` [`00abfd50`](#insn-00abfd50) → [`00abfd54`](#insn-00abfd54)
- ブロック [`00abfd54`](#insn-00abfd54) 範囲 `[['00abfd54', '00abfd5b']]`
  - `CONDITIONAL_JUMP` [`00abfd58`](#insn-00abfd58) → [`00abfec0`](#insn-00abfec0)
  - `FALL_THROUGH` [`00abfd58`](#insn-00abfd58) → [`00abfd5c`](#insn-00abfd5c)
- ブロック [`00abfd5c`](#insn-00abfd5c) 範囲 `[['00abfd5c', '00abfd5f']]`
  - `FALL_THROUGH` [`00abfd5c`](#insn-00abfd5c) → [`00abfd60`](#insn-00abfd60)
- ブロック [`00abfd60`](#insn-00abfd60) 範囲 `[['00abfd60', '00abfd63']]`
  - `CONDITIONAL_JUMP` [`00abfd60`](#insn-00abfd60) → [`00abfed0`](#insn-00abfed0)
  - `FALL_THROUGH` [`00abfd60`](#insn-00abfd60) → [`00abfd64`](#insn-00abfd64)
- ブロック [`00abfd64`](#insn-00abfd64) 範囲 `[['00abfd64', '00abfd6b']]`
  - `CONDITIONAL_JUMP` [`00abfd68`](#insn-00abfd68) → [`00abfd74`](#insn-00abfd74)
  - `FALL_THROUGH` [`00abfd68`](#insn-00abfd68) → [`00abfd6c`](#insn-00abfd6c)
- ブロック [`00abfd6c`](#insn-00abfd6c) 範囲 `[['00abfd6c', '00abfd73']]`
  - `FALL_THROUGH` [`00abfd70`](#insn-00abfd70) → [`00abfd74`](#insn-00abfd74)
- ブロック [`00abfd74`](#insn-00abfd74) 範囲 `[['00abfd74', '00abfda7']]`
  - `FALL_THROUGH` [`00abfda4`](#insn-00abfda4) → [`00abfda8`](#insn-00abfda8)
- ブロック [`00abfda8`](#insn-00abfda8) 範囲 `[['00abfda8', '00abfdab']]`
  - `FALL_THROUGH` [`00abfda8`](#insn-00abfda8) → [`00abfdac`](#insn-00abfdac)
- ブロック [`00abfdac`](#insn-00abfdac) 範囲 `[['00abfdac', '00abfdaf']]`
  - `CONDITIONAL_JUMP` [`00abfdac`](#insn-00abfdac) → [`00abfdb8`](#insn-00abfdb8)
  - `FALL_THROUGH` [`00abfdac`](#insn-00abfdac) → [`00abfdb0`](#insn-00abfdb0)
- ブロック [`00abfdb0`](#insn-00abfdb0) 範囲 `[['00abfdb0', '00abfdb7']]`
  - `FALL_THROUGH` [`00abfdb4`](#insn-00abfdb4) → [`00abfdb8`](#insn-00abfdb8)
- ブロック [`00abfdb8`](#insn-00abfdb8) 範囲 `[['00abfdb8', '00abfdc7']]`
  - `CONDITIONAL_JUMP` [`00abfdc4`](#insn-00abfdc4) → [`00ac01a4`](#insn-00ac01a4)
  - `FALL_THROUGH` [`00abfdc4`](#insn-00abfdc4) → [`00abfdc8`](#insn-00abfdc8)
- ブロック [`00abfdc8`](#insn-00abfdc8) 範囲 `[['00abfdc8', '00abfde3']]`
- ブロック [`00abfde4`](#insn-00abfde4) 範囲 `[['00abfde4', '00abfdf3']]`
  - `FALL_THROUGH` [`00abfdf0`](#insn-00abfdf0) → [`00abfdf4`](#insn-00abfdf4)
- ブロック [`00abfdf4`](#insn-00abfdf4) 範囲 `[['00abfdf4', '00abfe03']]`
  - `CONDITIONAL_JUMP` [`00abfe00`](#insn-00abfe00) → [`00abfac8`](#insn-00abfac8)
  - `FALL_THROUGH` [`00abfe00`](#insn-00abfe00) → [`00abfe04`](#insn-00abfe04)
- ブロック [`00abfe04`](#insn-00abfe04) 範囲 `[['00abfe04', '00abfe07']]`
  - `UNCONDITIONAL_JUMP` [`00abfe04`](#insn-00abfe04) → [`00abfad8`](#insn-00abfad8)
- ブロック [`00abfe08`](#insn-00abfe08) 範囲 `[['00abfe08', '00abfe13']]`
  - `FALL_THROUGH` [`00abfe10`](#insn-00abfe10) → [`00abfe14`](#insn-00abfe14)
- ブロック [`00abfe14`](#insn-00abfe14) 範囲 `[['00abfe14', '00abfe1f']]`
  - `FALL_THROUGH` [`00abfe1c`](#insn-00abfe1c) → [`00abfe20`](#insn-00abfe20)
- ブロック [`00abfe20`](#insn-00abfe20) 範囲 `[['00abfe20', '00abfe27']]`
  - `CONDITIONAL_JUMP` [`00abfe24`](#insn-00abfe24) → [`00abfae0`](#insn-00abfae0)
  - `FALL_THROUGH` [`00abfe24`](#insn-00abfe24) → [`00abfe28`](#insn-00abfe28)
- ブロック [`00abfe28`](#insn-00abfe28) 範囲 `[['00abfe28', '00abfe37']]`
  - `CONDITIONAL_JUMP` [`00abfe34`](#insn-00abfe34) → [`00abfae8`](#insn-00abfae8)
  - `FALL_THROUGH` [`00abfe34`](#insn-00abfe34) → [`00abfe38`](#insn-00abfe38)
- ブロック [`00abfe38`](#insn-00abfe38) 範囲 `[['00abfe38', '00abfe47']]`
  - `CONDITIONAL_JUMP` [`00abfe44`](#insn-00abfe44) → [`00abfaf0`](#insn-00abfaf0)
  - `FALL_THROUGH` [`00abfe44`](#insn-00abfe44) → [`00abfe48`](#insn-00abfe48)
- ブロック [`00abfe48`](#insn-00abfe48) 範囲 `[['00abfe48', '00abfe4b']]`
  - `UNCONDITIONAL_JUMP` [`00abfe48`](#insn-00abfe48) → [`00abfaf8`](#insn-00abfaf8)
- ブロック [`00abfe4c`](#insn-00abfe4c) 範囲 `[['00abfe4c', '00abfe5b']]`
  - `FALL_THROUGH` [`00abfe58`](#insn-00abfe58) → [`00abfe5c`](#insn-00abfe5c)
- ブロック [`00abfe5c`](#insn-00abfe5c) 範囲 `[['00abfe5c', '00abfe6b']]`
  - `CONDITIONAL_JUMP` [`00abfe68`](#insn-00abfe68) → [`00abfbe4`](#insn-00abfbe4)
  - `FALL_THROUGH` [`00abfe68`](#insn-00abfe68) → [`00abfe6c`](#insn-00abfe6c)
- ブロック [`00abfe6c`](#insn-00abfe6c) 範囲 `[['00abfe6c', '00abfe77']]`
  - `FALL_THROUGH` [`00abfe74`](#insn-00abfe74) → [`00abfe78`](#insn-00abfe78)
- ブロック [`00abfe78`](#insn-00abfe78) 範囲 `[['00abfe78', '00abfe7b']]`
  - `CONDITIONAL_JUMP` [`00abfe78`](#insn-00abfe78) → [`00abfbec`](#insn-00abfbec)
  - `FALL_THROUGH` [`00abfe78`](#insn-00abfe78) → [`00abfe7c`](#insn-00abfe7c)
- ブロック [`00abfe7c`](#insn-00abfe7c) 範囲 `[['00abfe7c', '00abfe83']]`
  - `FALL_THROUGH` [`00abfe80`](#insn-00abfe80) → [`00abfe84`](#insn-00abfe84)
- ブロック [`00abfe84`](#insn-00abfe84) 範囲 `[['00abfe84', '00abfe8b']]`
  - `CONDITIONAL_JUMP` [`00abfe88`](#insn-00abfe88) → [`00abfbf4`](#insn-00abfbf4)
  - `FALL_THROUGH` [`00abfe88`](#insn-00abfe88) → [`00abfe8c`](#insn-00abfe8c)
- ブロック [`00abfe8c`](#insn-00abfe8c) 範囲 `[['00abfe8c', '00abfe8f']]`
  - `UNCONDITIONAL_JUMP` [`00abfe8c`](#insn-00abfe8c) → [`00abfbfc`](#insn-00abfbfc)
- ブロック [`00abfe90`](#insn-00abfe90) 範囲 `[['00abfe90', '00abfeaf']]`
  - `CONDITIONAL_JUMP` [`00abfeac`](#insn-00abfeac) → [`00abfd54`](#insn-00abfd54)
  - `FALL_THROUGH` [`00abfeac`](#insn-00abfeac) → [`00abfeb0`](#insn-00abfeb0)
- ブロック [`00abfeb0`](#insn-00abfeb0) 範囲 `[['00abfeb0', '00abfebf']]`
  - `CONDITIONAL_JUMP` [`00abfebc`](#insn-00abfebc) → [`00abfd5c`](#insn-00abfd5c)
  - `FALL_THROUGH` [`00abfebc`](#insn-00abfebc) → [`00abfec0`](#insn-00abfec0)
- ブロック [`00abfec0`](#insn-00abfec0) 範囲 `[['00abfec0', '00abfecf']]`
  - `CONDITIONAL_JUMP` [`00abfecc`](#insn-00abfecc) → [`00abfd64`](#insn-00abfd64)
  - `FALL_THROUGH` [`00abfecc`](#insn-00abfecc) → [`00abfed0`](#insn-00abfed0)
- ブロック [`00abfed0`](#insn-00abfed0) 範囲 `[['00abfed0', '00abfedf']]`
  - `CONDITIONAL_JUMP` [`00abfedc`](#insn-00abfedc) → [`00abfd6c`](#insn-00abfd6c)
  - `FALL_THROUGH` [`00abfedc`](#insn-00abfedc) → [`00abfee0`](#insn-00abfee0)
- ブロック [`00abfee0`](#insn-00abfee0) 範囲 `[['00abfee0', '00abfee3']]`
  - `UNCONDITIONAL_JUMP` [`00abfee0`](#insn-00abfee0) → [`00abfd74`](#insn-00abfd74)
- ブロック [`00abfee4`](#insn-00abfee4) 範囲 `[['00abfee4', '00abfef3']]`
  - `CONDITIONAL_JUMP` [`00abfef0`](#insn-00abfef0) → [`00abf8f8`](#insn-00abf8f8)
  - `FALL_THROUGH` [`00abfef0`](#insn-00abfef0) → [`00abfef4`](#insn-00abfef4)
- ブロック [`00abfef4`](#insn-00abfef4) 範囲 `[['00abfef4', '00abff13']]`
  - `FALL_THROUGH` [`00abff10`](#insn-00abff10) → [`00abff14`](#insn-00abff14)
- ブロック [`00abff14`](#insn-00abff14) 範囲 `[['00abff14', '00abff3b']]`
  - `UNCONDITIONAL_JUMP` [`00abff38`](#insn-00abff38) → [`00abf8f8`](#insn-00abf8f8)
- ブロック [`00abff3c`](#insn-00abff3c) 範囲 `[['00abff3c', '00abff4b']]`
  - `CONDITIONAL_JUMP` [`00abff48`](#insn-00abff48) → [`00abfa18`](#insn-00abfa18)
  - `FALL_THROUGH` [`00abff48`](#insn-00abff48) → [`00abff4c`](#insn-00abff4c)
- ブロック [`00abff4c`](#insn-00abff4c) 範囲 `[['00abff4c', '00abff7f']]`
  - `FALL_THROUGH` [`00abff7c`](#insn-00abff7c) → [`00abff80`](#insn-00abff80)
- ブロック [`00abff80`](#insn-00abff80) 範囲 `[['00abff80', '00abff83']]`
  - `FALL_THROUGH` [`00abff80`](#insn-00abff80) → [`00abff84`](#insn-00abff84)
- ブロック [`00abff84`](#insn-00abff84) 範囲 `[['00abff84', '00abff8f']]`
  - `UNCONDITIONAL_JUMP` [`00abff8c`](#insn-00abff8c) → [`00abfa18`](#insn-00abfa18)
- ブロック [`00abff90`](#insn-00abff90) 範囲 `[['00abff90', '00abff9b']]`
  - `FALL_THROUGH` [`00abff98`](#insn-00abff98) → [`00abff9c`](#insn-00abff9c)
- ブロック [`00abff9c`](#insn-00abff9c) 範囲 `[['00abff9c', '00abff9f']]`
  - `CONDITIONAL_JUMP` [`00abff9c`](#insn-00abff9c) → [`00ac01a4`](#insn-00ac01a4)
  - `FALL_THROUGH` [`00abff9c`](#insn-00abff9c) → [`00abffa0`](#insn-00abffa0)
- ブロック [`00abffa0`](#insn-00abffa0) 範囲 `[['00abffa0', '00abffa7']]`
- ブロック [`00abffa8`](#insn-00abffa8) 範囲 `[['00abffa8', '00abffb3']]`
  - `FALL_THROUGH` [`00abffb0`](#insn-00abffb0) → [`00abffb4`](#insn-00abffb4)
- ブロック [`00abffb4`](#insn-00abffb4) 範囲 `[['00abffb4', '00abffb7']]`
  - `CONDITIONAL_JUMP` [`00abffb4`](#insn-00abffb4) → [`00abfb10`](#insn-00abfb10)
  - `FALL_THROUGH` [`00abffb4`](#insn-00abffb4) → [`00abffb8`](#insn-00abffb8)
- ブロック [`00abffb8`](#insn-00abffb8) 範囲 `[['00abffb8', '00abffbf']]`
  - `FALL_THROUGH` [`00abffbc`](#insn-00abffbc) → [`00abffc0`](#insn-00abffc0)
- ブロック [`00abffc0`](#insn-00abffc0) 範囲 `[['00abffc0', '00abffc3']]`
  - `FALL_THROUGH` [`00abffc0`](#insn-00abffc0) → [`00abffc4`](#insn-00abffc4)
- ブロック [`00abffc4`](#insn-00abffc4) 範囲 `[['00abffc4', '00abffd7']]`
  - `FALL_THROUGH` [`00abffd4`](#insn-00abffd4) → [`00abffd8`](#insn-00abffd8)
- ブロック [`00abffd8`](#insn-00abffd8) 範囲 `[['00abffd8', '00abffdb']]`
  - `FALL_THROUGH` [`00abffd8`](#insn-00abffd8) → [`00abffdc`](#insn-00abffdc)
- ブロック [`00abffdc`](#insn-00abffdc) 範囲 `[['00abffdc', '00abffe3']]`
  - `FALL_THROUGH` [`00abffe0`](#insn-00abffe0) → [`00abffe4`](#insn-00abffe4)
- ブロック [`00abffe4`](#insn-00abffe4) 範囲 `[['00abffe4', '00abffe7']]`
  - `FALL_THROUGH` [`00abffe4`](#insn-00abffe4) → [`00abffe8`](#insn-00abffe8)
- ブロック [`00abffe8`](#insn-00abffe8) 範囲 `[['00abffe8', '00abfff3']]`
  - `FALL_THROUGH` [`00abfff0`](#insn-00abfff0) → [`00abfff4`](#insn-00abfff4)
- ブロック [`00abfff4`](#insn-00abfff4) 範囲 `[['00abfff4', '00abfffb']]`
  - `UNCONDITIONAL_JUMP` [`00abfff8`](#insn-00abfff8) → [`00abfb10`](#insn-00abfb10)
- ブロック [`00abfffc`](#insn-00abfffc) 範囲 `[['00abfffc', '00ac0007']]`
  - `FALL_THROUGH` [`00ac0004`](#insn-00ac0004) → [`00ac0008`](#insn-00ac0008)
- ブロック [`00ac0008`](#insn-00ac0008) 範囲 `[['00ac0008', '00ac000b']]`
  - `CONDITIONAL_JUMP` [`00ac0008`](#insn-00ac0008) → [`00abfc3c`](#insn-00abfc3c)
  - `FALL_THROUGH` [`00ac0008`](#insn-00ac0008) → [`00ac000c`](#insn-00ac000c)
- ブロック [`00ac000c`](#insn-00ac000c) 範囲 `[['00ac000c', '00ac004f']]`
  - `UNCONDITIONAL_JUMP` [`00ac004c`](#insn-00ac004c) → [`00abfc3c`](#insn-00abfc3c)
- ブロック [`00ac0050`](#insn-00ac0050) 範囲 `[['00ac0050', '00ac0053']]`
  - `FALL_THROUGH` [`00ac0050`](#insn-00ac0050) → [`00ac0054`](#insn-00ac0054)
- ブロック [`00ac0054`](#insn-00ac0054) 範囲 `[['00ac0054', '00ac005b']]`
  - `FALL_THROUGH` [`00ac0058`](#insn-00ac0058) → [`00ac005c`](#insn-00ac005c)
- ブロック [`00ac005c`](#insn-00ac005c) 範囲 `[['00ac005c', '00ac005f']]`
  - `CONDITIONAL_JUMP` [`00ac005c`](#insn-00ac005c) → [`00ac01a4`](#insn-00ac01a4)
  - `FALL_THROUGH` [`00ac005c`](#insn-00ac005c) → [`00ac0060`](#insn-00ac0060)
- ブロック [`00ac0060`](#insn-00ac0060) 範囲 `[['00ac0060', '00ac0063']]`
  - `FALL_THROUGH` [`00ac0060`](#insn-00ac0060) → [`00ac0064`](#insn-00ac0064)
- ブロック [`00ac0064`](#insn-00ac0064) 範囲 `[['00ac0064', '00ac0067']]`
- ブロック [`00ac0068`](#insn-00ac0068) 範囲 `[['00ac0068', '00ac0077']]`
  - `CONDITIONAL_JUMP` [`00ac0074`](#insn-00ac0074) → [`00ac01a4`](#insn-00ac01a4)
  - `FALL_THROUGH` [`00ac0074`](#insn-00ac0074) → [`00ac0078`](#insn-00ac0078)
- ブロック [`00ac0078`](#insn-00ac0078) 範囲 `[['00ac0078', '00ac007b']]`
  - `FALL_THROUGH` [`00ac0078`](#insn-00ac0078) → [`00ac007c`](#insn-00ac007c)
- ブロック [`00ac007c`](#insn-00ac007c) 範囲 `[['00ac007c', '00ac0083']]`
  - `UNCONDITIONAL_JUMP` [`00ac0080`](#insn-00ac0080) → [`00ac00b0`](#insn-00ac00b0)
- ブロック [`00ac00b0`](#insn-00ac00b0) 範囲 `[['00ac00b0', '00ac00b3']]`
  - `FALL_THROUGH` [`00ac00b0`](#insn-00ac00b0) → [`00ac00b4`](#insn-00ac00b4)
- ブロック [`00ac00b4`](#insn-00ac00b4) 範囲 `[['00ac00b4', '00ac00bb']]`
  - `CONDITIONAL_JUMP` [`00ac00b8`](#insn-00ac00b8) → [`00ac014c`](#insn-00ac014c)
  - `FALL_THROUGH` [`00ac00b8`](#insn-00ac00b8) → [`00ac00bc`](#insn-00ac00bc)
- ブロック [`00ac00bc`](#insn-00ac00bc) 範囲 `[['00ac00bc', '00ac00bf']]`
  - `UNCONDITIONAL_JUMP` [`00ac00bc`](#insn-00ac00bc) → [`00ac018c`](#insn-00ac018c)
- ブロック [`00ac014c`](#insn-00ac014c) 範囲 `[['00ac014c', '00ac0153']]`
  - `UNCONDITIONAL_JUMP` [`00ac0150`](#insn-00ac0150) → [`00ac0188`](#insn-00ac0188)
- ブロック [`00ac0188`](#insn-00ac0188) 範囲 `[['00ac0188', '00ac018b']]`
  - `FALL_THROUGH` [`00ac0188`](#insn-00ac0188) → [`00ac018c`](#insn-00ac018c)
- ブロック [`00ac018c`](#insn-00ac018c) 範囲 `[['00ac018c', '00ac019b']]`
  - `CONDITIONAL_JUMP` [`00ac0198`](#insn-00ac0198) → [`00ac01a4`](#insn-00ac01a4)
  - `FALL_THROUGH` [`00ac0198`](#insn-00ac0198) → [`00ac019c`](#insn-00ac019c)
- ブロック [`00ac019c`](#insn-00ac019c) 範囲 `[['00ac019c', '00ac01a3']]`
- ブロック [`00ac01a4`](#insn-00ac01a4) 範囲 `[['00ac01a4', '00ac01a7']]`

## 命令位置別の参照

- [`00abf8b0`](#insn-00abf8b0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf8b4`](#insn-00abf8b4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf8b8`](#insn-00abf8b8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf8bc`](#insn-00abf8bc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf8c0`](#insn-00abf8c0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf8d0`](#insn-00abf8d0) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf8dc`](#insn-00abf8dc) → [`00abfdb8`](#insn-00abfdb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf8ec`](#insn-00abf8ec) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abf8f4`](#insn-00abf8f4) → [`00abfee4`](#insn-00abfee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf904`](#insn-00abf904) → `002ab964`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abf908`](#insn-00abf908) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf918`](#insn-00abf918) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf91c`](#insn-00abf91c) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf924`](#insn-00abf924) → `002adad5`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abf92c`](#insn-00abf92c) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf930`](#insn-00abf930) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf934`](#insn-00abf934) → `Stack[-0x87]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf938`](#insn-00abf938) → `Stack[-0x74]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf950`](#insn-00abf950) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abf958`](#insn-00abf958) → [`0047e5cc`](../0047e/0047e5cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047e5cc` · 推定シンボル `None` · 推定型 `None`
- [`00abf95c`](#insn-00abf95c) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf964`](#insn-00abf964) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf96c`](#insn-00abf96c) → [`00abf980`](#insn-00abf980) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf978`](#insn-00abf978) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00abf97c`](#insn-00abf97c) → [`00abf9b4`](#insn-00abf9b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf980`](#insn-00abf980) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf984`](#insn-00abf984) → [`00abf998`](#insn-00abf998) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf990`](#insn-00abf990) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00abf994`](#insn-00abf994) → [`00abf9d8`](#insn-00abf9d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf998`](#insn-00abf998) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf99c`](#insn-00abf99c) → [`00abf9f8`](#insn-00abf9f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf9a0`](#insn-00abf9a0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf9a4`](#insn-00abf9a4) → [`00abfa08`](#insn-00abfa08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf9a8`](#insn-00abf9a8) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abf9ac`](#insn-00abf9ac) → [`00abfa18`](#insn-00abfa18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf9b0`](#insn-00abf9b0) → [`00abff3c`](#insn-00abff3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf9c8`](#insn-00abf9c8) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00abf9cc`](#insn-00abf9cc) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf9d0`](#insn-00abf9d0) → [`00abf988`](#insn-00abf988) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf9d4`](#insn-00abf9d4) → [`00abf998`](#insn-00abf998) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf9ec`](#insn-00abf9ec) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00abf9f0`](#insn-00abf9f0) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf9f4`](#insn-00abf9f4) → [`00abf9a0`](#insn-00abf9a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf9f8`](#insn-00abf9f8) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf9fc`](#insn-00abf9fc) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abfa00`](#insn-00abfa00) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfa04`](#insn-00abfa04) → [`00abf9a8`](#insn-00abf9a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfa08`](#insn-00abfa08) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfa0c`](#insn-00abfa0c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abfa10`](#insn-00abfa10) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abfa14`](#insn-00abfa14) → [`00abff3c`](#insn-00abff3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfa28`](#insn-00abfa28) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfa30`](#insn-00abfa30) → `002bb807`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abfa34`](#insn-00abfa34) → `002bb80d`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abfa38`](#insn-00abfa38) → `Stack[-0x79]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfa40`](#insn-00abfa40) → `Stack[-0x87]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfa44`](#insn-00abfa44) → `Stack[-0x81]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfa48`](#insn-00abfa48) → [`00abff90`](#insn-00abff90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfa5c`](#insn-00abfa5c) → [`00447eb4`](../00447/00447eb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00447eb4` · 推定シンボル `None` · 推定型 `None`
- [`00abfa6c`](#insn-00abfa6c) → `002bcaae`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abfa70`](#insn-00abfa70) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfa74`](#insn-00abfa74) → `Stack[-0xaf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfa78`](#insn-00abfa78) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfa90`](#insn-00abfa90) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abfa98`](#insn-00abfa98) → [`0047e5cc`](../0047e/0047e5cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047e5cc` · 推定シンボル `None` · 推定型 `None`
- [`00abfa9c`](#insn-00abfa9c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfaa4`](#insn-00abfaa4) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfaac`](#insn-00abfaac) → [`00abfac0`](#insn-00abfac0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfab8`](#insn-00abfab8) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00abfabc`](#insn-00abfabc) → [`00abfde4`](#insn-00abfde4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfac0`](#insn-00abfac0) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfac4`](#insn-00abfac4) → [`00abfad8`](#insn-00abfad8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfad0`](#insn-00abfad0) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00abfad4`](#insn-00abfad4) → [`00abfe08`](#insn-00abfe08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfad8`](#insn-00abfad8) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfadc`](#insn-00abfadc) → [`00abfe28`](#insn-00abfe28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfae0`](#insn-00abfae0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfae4`](#insn-00abfae4) → [`00abfe38`](#insn-00abfe38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfae8`](#insn-00abfae8) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfaec`](#insn-00abfaec) → [`00abfaf8`](#insn-00abfaf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfaf0`](#insn-00abfaf0) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfaf4`](#insn-00abfaf4) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abfb04`](#insn-00abfb04) → [`00abfc34`](#insn-00abfc34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfb08`](#insn-00abfb08) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abfb0c`](#insn-00abfb0c) → [`00abffa8`](#insn-00abffa8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfb1c`](#insn-00abfb1c) → `002a17c6`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abfb24`](#insn-00abfb24) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfb28`](#insn-00abfb28) → `Stack[-0xb7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfb2c`](#insn-00abfb2c) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfb30`](#insn-00abfb30) → `Stack[-0xb5]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfb3c`](#insn-00abfb3c) → [`0048ce14`](../0048c/0048ce14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce14` · 推定シンボル `None` · 推定型 `None`
- [`00abfb58`](#insn-00abfb58) → [`00447eb4`](../00447/00447eb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00447eb4` · 推定シンボル `None` · 推定型 `None`
- [`00abfb64`](#insn-00abfb64) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abfb68`](#insn-00abfb68) → `00c9a8a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abfb68`](#insn-00abfb68) → `00ca4bd8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abfb84`](#insn-00abfb84) → [`0047e89c`](../0047e/0047e89c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047e89c` · 推定シンボル `None` · 推定型 `None`
- [`00abfb88`](#insn-00abfb88) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfb90`](#insn-00abfb90) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfb98`](#insn-00abfb98) → [`00abfbc4`](#insn-00abfbc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfba4`](#insn-00abfba4) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00abfba8`](#insn-00abfba8) → [`00abfbc4`](#insn-00abfbc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfbc0`](#insn-00abfbc0) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00abfbc4`](#insn-00abfbc4) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfbc8`](#insn-00abfbc8) → [`00abfbdc`](#insn-00abfbdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfbd4`](#insn-00abfbd4) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00abfbd8`](#insn-00abfbd8) → [`00abfe4c`](#insn-00abfe4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfbdc`](#insn-00abfbdc) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfbe0`](#insn-00abfbe0) → [`00abfe6c`](#insn-00abfe6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfbe4`](#insn-00abfbe4) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfbe8`](#insn-00abfbe8) → [`00abfe7c`](#insn-00abfe7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfbec`](#insn-00abfbec) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfbf0`](#insn-00abfbf0) → [`00abfbfc`](#insn-00abfbfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfbf4`](#insn-00abfbf4) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfbf8`](#insn-00abfbf8) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abfc08`](#insn-00abfc08) → `002afebe`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abfc14`](#insn-00abfc14) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfc18`](#insn-00abfc18) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfc1c`](#insn-00abfc1c) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfc20`](#insn-00abfc20) → `Stack[-0x5c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfc2c`](#insn-00abfc2c) → [`0046e930`](../0046e/0046e930.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046e930` · 推定シンボル `None` · 推定型 `None`
- [`00abfc30`](#insn-00abfc30) → [`00abfda8`](#insn-00abfda8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfc34`](#insn-00abfc34) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abfc38`](#insn-00abfc38) → [`00abfffc`](#insn-00abfffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfc48`](#insn-00abfc48) → `002a17d1`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abfc50`](#insn-00abfc50) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfc54`](#insn-00abfc54) → `Stack[-0xb7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfc58`](#insn-00abfc58) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfc5c`](#insn-00abfc5c) → `Stack[-0xb5]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfc68`](#insn-00abfc68) → [`0048ce14`](../0048c/0048ce14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce14` · 推定シンボル `None` · 推定型 `None`
- [`00abfc74`](#insn-00abfc74) → [`00ac0050`](#insn-00ac0050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfc88`](#insn-00abfc88) → [`00ac0068`](#insn-00ac0068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfc98`](#insn-00abfc98) → [`00abfcb0`](#insn-00abfcb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfca4`](#insn-00abfca4) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfca8`](#insn-00abfca8) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfcac`](#insn-00abfcac) → [`00abfcbc`](#insn-00abfcbc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfcb8`](#insn-00abfcb8) → [`0043bae0`](../0043b/0043bae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bae0` · 推定シンボル `None` · 推定型 `None`
- [`00abfcc8`](#insn-00abfcc8) → [`00492dc8`](../00492/00492dc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00492dc8` · 推定シンボル `None` · 推定型 `None`
- [`00abfcd4`](#insn-00abfcd4) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abfcd8`](#insn-00abfcd8) → `00c9a8a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abfcd8`](#insn-00abfcd8) → `00ca4bd8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abfcf4`](#insn-00abfcf4) → [`0047e89c`](../0047e/0047e89c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047e89c` · 推定シンボル `None` · 推定型 `None`
- [`00abfcf8`](#insn-00abfcf8) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd00`](#insn-00abfd00) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd08`](#insn-00abfd08) → [`00abfd34`](#insn-00abfd34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd14`](#insn-00abfd14) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00abfd18`](#insn-00abfd18) → [`00abfd34`](#insn-00abfd34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd30`](#insn-00abfd30) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00abfd34`](#insn-00abfd34) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd38`](#insn-00abfd38) → [`00abfd4c`](#insn-00abfd4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd44`](#insn-00abfd44) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00abfd48`](#insn-00abfd48) → [`00abfe90`](#insn-00abfe90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd4c`](#insn-00abfd4c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd50`](#insn-00abfd50) → [`00abfeb0`](#insn-00abfeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd54`](#insn-00abfd54) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd58`](#insn-00abfd58) → [`00abfec0`](#insn-00abfec0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd5c`](#insn-00abfd5c) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd60`](#insn-00abfd60) → [`00abfed0`](#insn-00abfed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd64`](#insn-00abfd64) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd68`](#insn-00abfd68) → [`00abfd74`](#insn-00abfd74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd6c`](#insn-00abfd6c) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd70`](#insn-00abfd70) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abfd80`](#insn-00abfd80) → `002b7b7d`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abfd8c`](#insn-00abfd8c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd90`](#insn-00abfd90) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd94`](#insn-00abfd94) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd98`](#insn-00abfd98) → `Stack[-0x5c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfda4`](#insn-00abfda4) → [`0046e930`](../0046e/0046e930.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046e930` · 推定シンボル `None` · 推定型 `None`
- [`00abfda8`](#insn-00abfda8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfdac`](#insn-00abfdac) → [`00abfdb8`](#insn-00abfdb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfdb0`](#insn-00abfdb0) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfdb4`](#insn-00abfdb4) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abfdbc`](#insn-00abfdbc) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfdc4`](#insn-00abfdc4) → [`00ac01a4`](#insn-00ac01a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfdc8`](#insn-00abfdc8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfdcc`](#insn-00abfdcc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfdd0`](#insn-00abfdd0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfdd4`](#insn-00abfdd4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfdd8`](#insn-00abfdd8) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfdf8`](#insn-00abfdf8) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00abfdfc`](#insn-00abfdfc) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe00`](#insn-00abfe00) → [`00abfac8`](#insn-00abfac8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe04`](#insn-00abfe04) → [`00abfad8`](#insn-00abfad8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe1c`](#insn-00abfe1c) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00abfe20`](#insn-00abfe20) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe24`](#insn-00abfe24) → [`00abfae0`](#insn-00abfae0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe28`](#insn-00abfe28) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe2c`](#insn-00abfe2c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abfe30`](#insn-00abfe30) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe34`](#insn-00abfe34) → [`00abfae8`](#insn-00abfae8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe38`](#insn-00abfe38) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe3c`](#insn-00abfe3c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abfe40`](#insn-00abfe40) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe44`](#insn-00abfe44) → [`00abfaf0`](#insn-00abfaf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe48`](#insn-00abfe48) → [`00abfaf8`](#insn-00abfaf8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe60`](#insn-00abfe60) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00abfe64`](#insn-00abfe64) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe68`](#insn-00abfe68) → [`00abfbe4`](#insn-00abfbe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe6c`](#insn-00abfe6c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe70`](#insn-00abfe70) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abfe74`](#insn-00abfe74) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe78`](#insn-00abfe78) → [`00abfbec`](#insn-00abfbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe7c`](#insn-00abfe7c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe80`](#insn-00abfe80) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abfe84`](#insn-00abfe84) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe88`](#insn-00abfe88) → [`00abfbf4`](#insn-00abfbf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe8c`](#insn-00abfe8c) → [`00abfbfc`](#insn-00abfbfc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfea4`](#insn-00abfea4) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00abfea8`](#insn-00abfea8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfeac`](#insn-00abfeac) → [`00abfd54`](#insn-00abfd54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfeb0`](#insn-00abfeb0) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfeb4`](#insn-00abfeb4) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abfeb8`](#insn-00abfeb8) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfebc`](#insn-00abfebc) → [`00abfd5c`](#insn-00abfd5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfec0`](#insn-00abfec0) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfec4`](#insn-00abfec4) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abfec8`](#insn-00abfec8) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfecc`](#insn-00abfecc) → [`00abfd64`](#insn-00abfd64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfed0`](#insn-00abfed0) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfed4`](#insn-00abfed4) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00abfed8`](#insn-00abfed8) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfedc`](#insn-00abfedc) → [`00abfd6c`](#insn-00abfd6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfee0`](#insn-00abfee0) → [`00abfd74`](#insn-00abfd74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfee8`](#insn-00abfee8) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abfeec`](#insn-00abfeec) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`00abfef0`](#insn-00abfef0) → [`00abf8f8`](#insn-00abf8f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfef8`](#insn-00abfef8) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abff00`](#insn-00abff00) → [`0047ed74`](../0047e/0047ed74.md) · `PARAM` · `ANALYSIS` · 関数 `0047ed74` · 推定シンボル `None` · 推定型 `None`
- [`00abff0c`](#insn-00abff0c) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abff10`](#insn-00abff10) → `00ca4b08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abff14`](#insn-00abff14) → `00ca4b00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abff14`](#insn-00abff14) → `00ca4b08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abff1c`](#insn-00abff1c) → `00ca4b28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abff1c`](#insn-00abff1c) → `00ca4b30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abff20`](#insn-00abff20) → `00ca4b20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abff24`](#insn-00abff24) → `00ca4b10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abff24`](#insn-00abff24) → `00ca4b18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abff24`](#insn-00abff24) → `00ca4b20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abff28`](#insn-00abff28) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`00abff30`](#insn-00abff30) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abff34`](#insn-00abff34) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`00abff38`](#insn-00abff38) → [`00abf8f8`](#insn-00abf8f8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abff40`](#insn-00abff40) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abff44`](#insn-00abff44) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`00abff48`](#insn-00abff48) → [`00abfa18`](#insn-00abfa18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abff54`](#insn-00abff54) → [`0047ed74`](../0047e/0047ed74.md) · `PARAM` · `ANALYSIS` · 関数 `0047ed74` · 推定シンボル `None` · 推定型 `None`
- [`00abff58`](#insn-00abff58) → `00ca4b08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abff60`](#insn-00abff60) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abff64`](#insn-00abff64) → `00ca4b00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abff64`](#insn-00abff64) → `00ca4b08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abff6c`](#insn-00abff6c) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abff70`](#insn-00abff70) → `00ca4b28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abff70`](#insn-00abff70) → `00ca4b30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abff74`](#insn-00abff74) → `00ca4b20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abff78`](#insn-00abff78) → `00ca4b10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abff78`](#insn-00abff78) → `00ca4b18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abff78`](#insn-00abff78) → `00ca4b20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abff7c`](#insn-00abff7c) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`00abff84`](#insn-00abff84) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abff88`](#insn-00abff88) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`00abff8c`](#insn-00abff8c) → [`00abfa18`](#insn-00abfa18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abff94`](#insn-00abff94) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abff9c`](#insn-00abff9c) → [`00ac01a4`](#insn-00ac01a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abffa4`](#insn-00abffa4) → [`0049f3b0`](../0049f/0049f3b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0049f3b0` · 推定シンボル `None` · 推定型 `None`
- [`00abffac`](#insn-00abffac) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abffb0`](#insn-00abffb0) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`00abffb4`](#insn-00abffb4) → [`00abfb10`](#insn-00abfb10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abffc0`](#insn-00abffc0) → [`0047ed74`](../0047e/0047ed74.md) · `PARAM` · `ANALYSIS` · 関数 `0047ed74` · 推定シンボル `None` · 推定型 `None`
- [`00abffc4`](#insn-00abffc4) → `00ca4b08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abffcc`](#insn-00abffcc) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abffd0`](#insn-00abffd0) → `00ca4b00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abffd0`](#insn-00abffd0) → `00ca4b08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abffd8`](#insn-00abffd8) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abffdc`](#insn-00abffdc) → `00ca4b28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abffdc`](#insn-00abffdc) → `00ca4b30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abffe0`](#insn-00abffe0) → `00ca4b20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abffe4`](#insn-00abffe4) → `00ca4b10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abffe4`](#insn-00abffe4) → `00ca4b18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abffe4`](#insn-00abffe4) → `00ca4b20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abffe8`](#insn-00abffe8) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`00abfff0`](#insn-00abfff0) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abfff4`](#insn-00abfff4) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`00abfff8`](#insn-00abfff8) → [`00abfb10`](#insn-00abfb10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0000`](#insn-00ac0000) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ac0004`](#insn-00ac0004) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`00ac0008`](#insn-00ac0008) → [`00abfc3c`](#insn-00abfc3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0014`](#insn-00ac0014) → [`0047ed74`](../0047e/0047ed74.md) · `PARAM` · `ANALYSIS` · 関数 `0047ed74` · 推定シンボル `None` · 推定型 `None`
- [`00ac0018`](#insn-00ac0018) → `00ca4b08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0020`](#insn-00ac0020) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ac0024`](#insn-00ac0024) → `00ca4b00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0024`](#insn-00ac0024) → `00ca4b08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac002c`](#insn-00ac002c) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0030`](#insn-00ac0030) → `00ca4b28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0030`](#insn-00ac0030) → `00ca4b30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0034`](#insn-00ac0034) → `00ca4b20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0038`](#insn-00ac0038) → `00ca4b10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0038`](#insn-00ac0038) → `00ca4b18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0038`](#insn-00ac0038) → `00ca4b20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac003c`](#insn-00ac003c) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`00ac0044`](#insn-00ac0044) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ac0048`](#insn-00ac0048) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`00ac004c`](#insn-00ac004c) → [`00abfc3c`](#insn-00abfc3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0054`](#insn-00ac0054) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac005c`](#insn-00ac005c) → [`00ac01a4`](#insn-00ac01a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0064`](#insn-00ac0064) → [`0049f3b0`](../0049f/0049f3b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0049f3b0` · 推定シンボル `None` · 推定型 `None`
- [`00ac006c`](#insn-00ac006c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0074`](#insn-00ac0074) → [`00ac01a4`](#insn-00ac01a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac007c`](#insn-00ac007c) → [`00ac0de8`](../00ac0/00ac0de8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac0de8` · 推定シンボル `None` · 推定型 `None`
- [`00ac0080`](#insn-00ac0080) → [`00ac00b0`](#insn-00ac00b0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac00b0`](#insn-00ac00b0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac00b8`](#insn-00ac00b8) → [`00ac014c`](#insn-00ac014c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac00bc`](#insn-00ac00bc) → [`00ac018c`](#insn-00ac018c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac014c`](#insn-00ac014c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0150`](#insn-00ac0150) → [`00ac0188`](#insn-00ac0188) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0188`](#insn-00ac0188) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00ac0190`](#insn-00ac0190) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0198`](#insn-00ac0198) → [`00ac01a4`](#insn-00ac01a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac01a0`](#insn-00ac01a0) → [`00c53b3c`](../00c53/00c53b3c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53b3c` · 推定シンボル `None` · 推定型 `None`
- [`00ac01a4`](#insn-00ac01a4) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00abf8b0`](#insn-00abf8b0)

~~~json
{
  "source": "00abf8b0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf8b4`](#insn-00abf8b4)

~~~json
{
  "source": "00abf8b4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf8b8`](#insn-00abf8b8)

~~~json
{
  "source": "00abf8b8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf8bc`](#insn-00abf8bc)

~~~json
{
  "source": "00abf8bc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf8c0`](#insn-00abf8c0)

~~~json
{
  "source": "00abf8c0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf8d0`](#insn-00abf8d0)

~~~json
{
  "source": "00abf8d0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf8dc`](#insn-00abf8dc)

~~~json
{
  "source": "00abf8dc",
  "target": "00abfdb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf8ec`](#insn-00abf8ec)

~~~json
{
  "source": "00abf8ec",
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
- 参照命令 [`00abf8f4`](#insn-00abf8f4)

~~~json
{
  "source": "00abf8f4",
  "target": "00abfee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf904`](#insn-00abf904)

~~~json
{
  "source": "00abf904",
  "target": "002ab964",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ab964",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "6d6564616c5f6765743030302e706e6700",
  "capture_start": "002ab964",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abf908`](#insn-00abf908)

~~~json
{
  "source": "00abf908",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf918`](#insn-00abf918)

~~~json
{
  "source": "00abf918",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf91c`](#insn-00abf91c)

~~~json
{
  "source": "00abf91c",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf924`](#insn-00abf924)

~~~json
{
  "source": "00abf924",
  "target": "002adad5",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002adad5",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6d6564616c5f6765743030302e696d6763757400",
  "capture_start": "002adad5",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abf92c`](#insn-00abf92c)

~~~json
{
  "source": "00abf92c",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf930`](#insn-00abf930)

~~~json
{
  "source": "00abf930",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf934`](#insn-00abf934)

~~~json
{
  "source": "00abf934",
  "target": "Stack[-0x87]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf938`](#insn-00abf938)

~~~json
{
  "source": "00abf938",
  "target": "Stack[-0x74]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf950`](#insn-00abf950)

~~~json
{
  "source": "00abf950",
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
- 参照命令 [`00abf958`](#insn-00abf958)

~~~json
{
  "source": "00abf958",
  "target": "0047e5cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf95c`](#insn-00abf95c)

~~~json
{
  "source": "00abf95c",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf964`](#insn-00abf964)

~~~json
{
  "source": "00abf964",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf96c`](#insn-00abf96c)

~~~json
{
  "source": "00abf96c",
  "target": "00abf980",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf978`](#insn-00abf978)

~~~json
{
  "source": "00abf978",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf97c`](#insn-00abf97c)

~~~json
{
  "source": "00abf97c",
  "target": "00abf9b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf980`](#insn-00abf980)

~~~json
{
  "source": "00abf980",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf984`](#insn-00abf984)

~~~json
{
  "source": "00abf984",
  "target": "00abf998",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf990`](#insn-00abf990)

~~~json
{
  "source": "00abf990",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf994`](#insn-00abf994)

~~~json
{
  "source": "00abf994",
  "target": "00abf9d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf998`](#insn-00abf998)

~~~json
{
  "source": "00abf998",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf99c`](#insn-00abf99c)

~~~json
{
  "source": "00abf99c",
  "target": "00abf9f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf9a0`](#insn-00abf9a0)

~~~json
{
  "source": "00abf9a0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf9a4`](#insn-00abf9a4)

~~~json
{
  "source": "00abf9a4",
  "target": "00abfa08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf9a8`](#insn-00abf9a8)

~~~json
{
  "source": "00abf9a8",
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
- 参照命令 [`00abf9ac`](#insn-00abf9ac)

~~~json
{
  "source": "00abf9ac",
  "target": "00abfa18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf9b0`](#insn-00abf9b0)

~~~json
{
  "source": "00abf9b0",
  "target": "00abff3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf9c8`](#insn-00abf9c8)

~~~json
{
  "source": "00abf9c8",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf9cc`](#insn-00abf9cc)

~~~json
{
  "source": "00abf9cc",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf9d0`](#insn-00abf9d0)

~~~json
{
  "source": "00abf9d0",
  "target": "00abf988",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf9d4`](#insn-00abf9d4)

~~~json
{
  "source": "00abf9d4",
  "target": "00abf998",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf9ec`](#insn-00abf9ec)

~~~json
{
  "source": "00abf9ec",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf9f0`](#insn-00abf9f0)

~~~json
{
  "source": "00abf9f0",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf9f4`](#insn-00abf9f4)

~~~json
{
  "source": "00abf9f4",
  "target": "00abf9a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf9f8`](#insn-00abf9f8)

~~~json
{
  "source": "00abf9f8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf9fc`](#insn-00abf9fc)

~~~json
{
  "source": "00abf9fc",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfa00`](#insn-00abfa00)

~~~json
{
  "source": "00abfa00",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfa04`](#insn-00abfa04)

~~~json
{
  "source": "00abfa04",
  "target": "00abf9a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfa08`](#insn-00abfa08)

~~~json
{
  "source": "00abfa08",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfa0c`](#insn-00abfa0c)

~~~json
{
  "source": "00abfa0c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfa10`](#insn-00abfa10)

~~~json
{
  "source": "00abfa10",
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
- 参照命令 [`00abfa14`](#insn-00abfa14)

~~~json
{
  "source": "00abfa14",
  "target": "00abff3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfa28`](#insn-00abfa28)

~~~json
{
  "source": "00abfa28",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfa30`](#insn-00abfa30)

~~~json
{
  "source": "00abfa30",
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
- 参照命令 [`00abfa34`](#insn-00abfa34)

~~~json
{
  "source": "00abfa34",
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
- 参照命令 [`00abfa38`](#insn-00abfa38)

~~~json
{
  "source": "00abfa38",
  "target": "Stack[-0x79]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfa40`](#insn-00abfa40)

~~~json
{
  "source": "00abfa40",
  "target": "Stack[-0x87]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfa44`](#insn-00abfa44)

~~~json
{
  "source": "00abfa44",
  "target": "Stack[-0x81]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfa48`](#insn-00abfa48)

~~~json
{
  "source": "00abfa48",
  "target": "00abff90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfa5c`](#insn-00abfa5c)

~~~json
{
  "source": "00abfa5c",
  "target": "00447eb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfa6c`](#insn-00abfa6c)

~~~json
{
  "source": "00abfa6c",
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
- 参照命令 [`00abfa70`](#insn-00abfa70)

~~~json
{
  "source": "00abfa70",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfa74`](#insn-00abfa74)

~~~json
{
  "source": "00abfa74",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfa78`](#insn-00abfa78)

~~~json
{
  "source": "00abfa78",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfa90`](#insn-00abfa90)

~~~json
{
  "source": "00abfa90",
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
- 参照命令 [`00abfa98`](#insn-00abfa98)

~~~json
{
  "source": "00abfa98",
  "target": "0047e5cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfa9c`](#insn-00abfa9c)

~~~json
{
  "source": "00abfa9c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfaa4`](#insn-00abfaa4)

~~~json
{
  "source": "00abfaa4",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfaac`](#insn-00abfaac)

~~~json
{
  "source": "00abfaac",
  "target": "00abfac0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfab8`](#insn-00abfab8)

~~~json
{
  "source": "00abfab8",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfabc`](#insn-00abfabc)

~~~json
{
  "source": "00abfabc",
  "target": "00abfde4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfac0`](#insn-00abfac0)

~~~json
{
  "source": "00abfac0",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfac4`](#insn-00abfac4)

~~~json
{
  "source": "00abfac4",
  "target": "00abfad8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfad0`](#insn-00abfad0)

~~~json
{
  "source": "00abfad0",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfad4`](#insn-00abfad4)

~~~json
{
  "source": "00abfad4",
  "target": "00abfe08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfad8`](#insn-00abfad8)

~~~json
{
  "source": "00abfad8",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfadc`](#insn-00abfadc)

~~~json
{
  "source": "00abfadc",
  "target": "00abfe28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfae0`](#insn-00abfae0)

~~~json
{
  "source": "00abfae0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfae4`](#insn-00abfae4)

~~~json
{
  "source": "00abfae4",
  "target": "00abfe38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfae8`](#insn-00abfae8)

~~~json
{
  "source": "00abfae8",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfaec`](#insn-00abfaec)

~~~json
{
  "source": "00abfaec",
  "target": "00abfaf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfaf0`](#insn-00abfaf0)

~~~json
{
  "source": "00abfaf0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfaf4`](#insn-00abfaf4)

~~~json
{
  "source": "00abfaf4",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfb04`](#insn-00abfb04)

~~~json
{
  "source": "00abfb04",
  "target": "00abfc34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfb08`](#insn-00abfb08)

~~~json
{
  "source": "00abfb08",
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
- 参照命令 [`00abfb0c`](#insn-00abfb0c)

~~~json
{
  "source": "00abfb0c",
  "target": "00abffa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfb1c`](#insn-00abfb1c)

~~~json
{
  "source": "00abfb1c",
  "target": "002a17c6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a17c6",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "6d6564616c5f7478743200",
  "capture_start": "002a17c6",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abfb24`](#insn-00abfb24)

~~~json
{
  "source": "00abfb24",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfb28`](#insn-00abfb28)

~~~json
{
  "source": "00abfb28",
  "target": "Stack[-0xb7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfb2c`](#insn-00abfb2c)

~~~json
{
  "source": "00abfb2c",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfb30`](#insn-00abfb30)

~~~json
{
  "source": "00abfb30",
  "target": "Stack[-0xb5]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfb3c`](#insn-00abfb3c)

~~~json
{
  "source": "00abfb3c",
  "target": "0048ce14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfb58`](#insn-00abfb58)

~~~json
{
  "source": "00abfb58",
  "target": "00447eb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfb64`](#insn-00abfb64)

~~~json
{
  "source": "00abfb64",
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
- 参照命令 [`00abfb68`](#insn-00abfb68)

~~~json
{
  "source": "00abfb68",
  "target": "00c9a8a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9a8a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abfb68`](#insn-00abfb68)

~~~json
{
  "source": "00abfb68",
  "target": "00ca4bd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4bd8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abfb84`](#insn-00abfb84)

~~~json
{
  "source": "00abfb84",
  "target": "0047e89c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfb88`](#insn-00abfb88)

~~~json
{
  "source": "00abfb88",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfb90`](#insn-00abfb90)

~~~json
{
  "source": "00abfb90",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfb98`](#insn-00abfb98)

~~~json
{
  "source": "00abfb98",
  "target": "00abfbc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfba4`](#insn-00abfba4)

~~~json
{
  "source": "00abfba4",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfba8`](#insn-00abfba8)

~~~json
{
  "source": "00abfba8",
  "target": "00abfbc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfbc0`](#insn-00abfbc0)

~~~json
{
  "source": "00abfbc0",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfbc4`](#insn-00abfbc4)

~~~json
{
  "source": "00abfbc4",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfbc8`](#insn-00abfbc8)

~~~json
{
  "source": "00abfbc8",
  "target": "00abfbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfbd4`](#insn-00abfbd4)

~~~json
{
  "source": "00abfbd4",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfbd8`](#insn-00abfbd8)

~~~json
{
  "source": "00abfbd8",
  "target": "00abfe4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfbdc`](#insn-00abfbdc)

~~~json
{
  "source": "00abfbdc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfbe0`](#insn-00abfbe0)

~~~json
{
  "source": "00abfbe0",
  "target": "00abfe6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfbe4`](#insn-00abfbe4)

~~~json
{
  "source": "00abfbe4",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfbe8`](#insn-00abfbe8)

~~~json
{
  "source": "00abfbe8",
  "target": "00abfe7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfbec`](#insn-00abfbec)

~~~json
{
  "source": "00abfbec",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfbf0`](#insn-00abfbf0)

~~~json
{
  "source": "00abfbf0",
  "target": "00abfbfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfbf4`](#insn-00abfbf4)

~~~json
{
  "source": "00abfbf4",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfbf8`](#insn-00abfbf8)

~~~json
{
  "source": "00abfbf8",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfc08`](#insn-00abfc08)

~~~json
{
  "source": "00abfc08",
  "target": "002afebe",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002afebe",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6d6564616c5f6765743030322e6d61616e696d00",
  "capture_start": "002afebe",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abfc14`](#insn-00abfc14)

~~~json
{
  "source": "00abfc14",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfc18`](#insn-00abfc18)

~~~json
{
  "source": "00abfc18",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfc1c`](#insn-00abfc1c)

~~~json
{
  "source": "00abfc1c",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfc20`](#insn-00abfc20)

~~~json
{
  "source": "00abfc20",
  "target": "Stack[-0x5c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfc2c`](#insn-00abfc2c)

~~~json
{
  "source": "00abfc2c",
  "target": "0046e930",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfc30`](#insn-00abfc30)

~~~json
{
  "source": "00abfc30",
  "target": "00abfda8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfc34`](#insn-00abfc34)

~~~json
{
  "source": "00abfc34",
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
- 参照命令 [`00abfc38`](#insn-00abfc38)

~~~json
{
  "source": "00abfc38",
  "target": "00abfffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfc48`](#insn-00abfc48)

~~~json
{
  "source": "00abfc48",
  "target": "002a17d1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a17d1",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "6d6564616c5f7478743100",
  "capture_start": "002a17d1",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abfc50`](#insn-00abfc50)

~~~json
{
  "source": "00abfc50",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfc54`](#insn-00abfc54)

~~~json
{
  "source": "00abfc54",
  "target": "Stack[-0xb7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfc58`](#insn-00abfc58)

~~~json
{
  "source": "00abfc58",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfc5c`](#insn-00abfc5c)

~~~json
{
  "source": "00abfc5c",
  "target": "Stack[-0xb5]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfc68`](#insn-00abfc68)

~~~json
{
  "source": "00abfc68",
  "target": "0048ce14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfc74`](#insn-00abfc74)

~~~json
{
  "source": "00abfc74",
  "target": "00ac0050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfc88`](#insn-00abfc88)

~~~json
{
  "source": "00abfc88",
  "target": "00ac0068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfc98`](#insn-00abfc98)

~~~json
{
  "source": "00abfc98",
  "target": "00abfcb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfca4`](#insn-00abfca4)

~~~json
{
  "source": "00abfca4",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfca8`](#insn-00abfca8)

~~~json
{
  "source": "00abfca8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfcac`](#insn-00abfcac)

~~~json
{
  "source": "00abfcac",
  "target": "00abfcbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfcb8`](#insn-00abfcb8)

~~~json
{
  "source": "00abfcb8",
  "target": "0043bae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfcc8`](#insn-00abfcc8)

~~~json
{
  "source": "00abfcc8",
  "target": "00492dc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfcd4`](#insn-00abfcd4)

~~~json
{
  "source": "00abfcd4",
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
- 参照命令 [`00abfcd8`](#insn-00abfcd8)

~~~json
{
  "source": "00abfcd8",
  "target": "00c9a8a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9a8a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abfcd8`](#insn-00abfcd8)

~~~json
{
  "source": "00abfcd8",
  "target": "00ca4bd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4bd8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abfcf4`](#insn-00abfcf4)

~~~json
{
  "source": "00abfcf4",
  "target": "0047e89c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfcf8`](#insn-00abfcf8)

~~~json
{
  "source": "00abfcf8",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd00`](#insn-00abfd00)

~~~json
{
  "source": "00abfd00",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd08`](#insn-00abfd08)

~~~json
{
  "source": "00abfd08",
  "target": "00abfd34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd14`](#insn-00abfd14)

~~~json
{
  "source": "00abfd14",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfd18`](#insn-00abfd18)

~~~json
{
  "source": "00abfd18",
  "target": "00abfd34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd30`](#insn-00abfd30)

~~~json
{
  "source": "00abfd30",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfd34`](#insn-00abfd34)

~~~json
{
  "source": "00abfd34",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd38`](#insn-00abfd38)

~~~json
{
  "source": "00abfd38",
  "target": "00abfd4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd44`](#insn-00abfd44)

~~~json
{
  "source": "00abfd44",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfd48`](#insn-00abfd48)

~~~json
{
  "source": "00abfd48",
  "target": "00abfe90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd4c`](#insn-00abfd4c)

~~~json
{
  "source": "00abfd4c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd50`](#insn-00abfd50)

~~~json
{
  "source": "00abfd50",
  "target": "00abfeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd54`](#insn-00abfd54)

~~~json
{
  "source": "00abfd54",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd58`](#insn-00abfd58)

~~~json
{
  "source": "00abfd58",
  "target": "00abfec0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd5c`](#insn-00abfd5c)

~~~json
{
  "source": "00abfd5c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd60`](#insn-00abfd60)

~~~json
{
  "source": "00abfd60",
  "target": "00abfed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd64`](#insn-00abfd64)

~~~json
{
  "source": "00abfd64",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd68`](#insn-00abfd68)

~~~json
{
  "source": "00abfd68",
  "target": "00abfd74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd6c`](#insn-00abfd6c)

~~~json
{
  "source": "00abfd6c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd70`](#insn-00abfd70)

~~~json
{
  "source": "00abfd70",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfd80`](#insn-00abfd80)

~~~json
{
  "source": "00abfd80",
  "target": "002b7b7d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b7b7d",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6d6564616c5f6765743030312e6d61616e696d00",
  "capture_start": "002b7b7d",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abfd8c`](#insn-00abfd8c)

~~~json
{
  "source": "00abfd8c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd90`](#insn-00abfd90)

~~~json
{
  "source": "00abfd90",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd94`](#insn-00abfd94)

~~~json
{
  "source": "00abfd94",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd98`](#insn-00abfd98)

~~~json
{
  "source": "00abfd98",
  "target": "Stack[-0x5c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfda4`](#insn-00abfda4)

~~~json
{
  "source": "00abfda4",
  "target": "0046e930",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfda8`](#insn-00abfda8)

~~~json
{
  "source": "00abfda8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfdac`](#insn-00abfdac)

~~~json
{
  "source": "00abfdac",
  "target": "00abfdb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfdb0`](#insn-00abfdb0)

~~~json
{
  "source": "00abfdb0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfdb4`](#insn-00abfdb4)

~~~json
{
  "source": "00abfdb4",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfdbc`](#insn-00abfdbc)

~~~json
{
  "source": "00abfdbc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfdc4`](#insn-00abfdc4)

~~~json
{
  "source": "00abfdc4",
  "target": "00ac01a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfdc8`](#insn-00abfdc8)

~~~json
{
  "source": "00abfdc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfdcc`](#insn-00abfdcc)

~~~json
{
  "source": "00abfdcc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfdd0`](#insn-00abfdd0)

~~~json
{
  "source": "00abfdd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfdd4`](#insn-00abfdd4)

~~~json
{
  "source": "00abfdd4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfdd8`](#insn-00abfdd8)

~~~json
{
  "source": "00abfdd8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfdf8`](#insn-00abfdf8)

~~~json
{
  "source": "00abfdf8",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfdfc`](#insn-00abfdfc)

~~~json
{
  "source": "00abfdfc",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe00`](#insn-00abfe00)

~~~json
{
  "source": "00abfe00",
  "target": "00abfac8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe04`](#insn-00abfe04)

~~~json
{
  "source": "00abfe04",
  "target": "00abfad8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe1c`](#insn-00abfe1c)

~~~json
{
  "source": "00abfe1c",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfe20`](#insn-00abfe20)

~~~json
{
  "source": "00abfe20",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe24`](#insn-00abfe24)

~~~json
{
  "source": "00abfe24",
  "target": "00abfae0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe28`](#insn-00abfe28)

~~~json
{
  "source": "00abfe28",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe2c`](#insn-00abfe2c)

~~~json
{
  "source": "00abfe2c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfe30`](#insn-00abfe30)

~~~json
{
  "source": "00abfe30",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe34`](#insn-00abfe34)

~~~json
{
  "source": "00abfe34",
  "target": "00abfae8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe38`](#insn-00abfe38)

~~~json
{
  "source": "00abfe38",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe3c`](#insn-00abfe3c)

~~~json
{
  "source": "00abfe3c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfe40`](#insn-00abfe40)

~~~json
{
  "source": "00abfe40",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe44`](#insn-00abfe44)

~~~json
{
  "source": "00abfe44",
  "target": "00abfaf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe48`](#insn-00abfe48)

~~~json
{
  "source": "00abfe48",
  "target": "00abfaf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe60`](#insn-00abfe60)

~~~json
{
  "source": "00abfe60",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfe64`](#insn-00abfe64)

~~~json
{
  "source": "00abfe64",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe68`](#insn-00abfe68)

~~~json
{
  "source": "00abfe68",
  "target": "00abfbe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe6c`](#insn-00abfe6c)

~~~json
{
  "source": "00abfe6c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe70`](#insn-00abfe70)

~~~json
{
  "source": "00abfe70",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfe74`](#insn-00abfe74)

~~~json
{
  "source": "00abfe74",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe78`](#insn-00abfe78)

~~~json
{
  "source": "00abfe78",
  "target": "00abfbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe7c`](#insn-00abfe7c)

~~~json
{
  "source": "00abfe7c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe80`](#insn-00abfe80)

~~~json
{
  "source": "00abfe80",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfe84`](#insn-00abfe84)

~~~json
{
  "source": "00abfe84",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe88`](#insn-00abfe88)

~~~json
{
  "source": "00abfe88",
  "target": "00abfbf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe8c`](#insn-00abfe8c)

~~~json
{
  "source": "00abfe8c",
  "target": "00abfbfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfea4`](#insn-00abfea4)

~~~json
{
  "source": "00abfea4",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfea8`](#insn-00abfea8)

~~~json
{
  "source": "00abfea8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfeac`](#insn-00abfeac)

~~~json
{
  "source": "00abfeac",
  "target": "00abfd54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfeb0`](#insn-00abfeb0)

~~~json
{
  "source": "00abfeb0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfeb4`](#insn-00abfeb4)

~~~json
{
  "source": "00abfeb4",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfeb8`](#insn-00abfeb8)

~~~json
{
  "source": "00abfeb8",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfebc`](#insn-00abfebc)

~~~json
{
  "source": "00abfebc",
  "target": "00abfd5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfec0`](#insn-00abfec0)

~~~json
{
  "source": "00abfec0",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfec4`](#insn-00abfec4)

~~~json
{
  "source": "00abfec4",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfec8`](#insn-00abfec8)

~~~json
{
  "source": "00abfec8",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfecc`](#insn-00abfecc)

~~~json
{
  "source": "00abfecc",
  "target": "00abfd64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfed0`](#insn-00abfed0)

~~~json
{
  "source": "00abfed0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfed4`](#insn-00abfed4)

~~~json
{
  "source": "00abfed4",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfed8`](#insn-00abfed8)

~~~json
{
  "source": "00abfed8",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfedc`](#insn-00abfedc)

~~~json
{
  "source": "00abfedc",
  "target": "00abfd6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfee0`](#insn-00abfee0)

~~~json
{
  "source": "00abfee0",
  "target": "00abfd74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfee8`](#insn-00abfee8)

~~~json
{
  "source": "00abfee8",
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
- 参照命令 [`00abfeec`](#insn-00abfeec)

~~~json
{
  "source": "00abfeec",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfef0`](#insn-00abfef0)

~~~json
{
  "source": "00abfef0",
  "target": "00abf8f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfef8`](#insn-00abfef8)

~~~json
{
  "source": "00abfef8",
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
- 参照命令 [`00abff00`](#insn-00abff00)

~~~json
{
  "source": "00abff00",
  "target": "0047ed74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abff0c`](#insn-00abff0c)

~~~json
{
  "source": "00abff0c",
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
- 参照命令 [`00abff10`](#insn-00abff10)

~~~json
{
  "source": "00abff10",
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
- 参照命令 [`00abff14`](#insn-00abff14)

~~~json
{
  "source": "00abff14",
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
- 参照命令 [`00abff14`](#insn-00abff14)

~~~json
{
  "source": "00abff14",
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
- 参照命令 [`00abff1c`](#insn-00abff1c)

~~~json
{
  "source": "00abff1c",
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
- 参照命令 [`00abff1c`](#insn-00abff1c)

~~~json
{
  "source": "00abff1c",
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
- 参照命令 [`00abff20`](#insn-00abff20)

~~~json
{
  "source": "00abff20",
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
- 参照命令 [`00abff24`](#insn-00abff24)

~~~json
{
  "source": "00abff24",
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
- 参照命令 [`00abff24`](#insn-00abff24)

~~~json
{
  "source": "00abff24",
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
- 参照命令 [`00abff24`](#insn-00abff24)

~~~json
{
  "source": "00abff24",
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
- 参照命令 [`00abff28`](#insn-00abff28)

~~~json
{
  "source": "00abff28",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abff30`](#insn-00abff30)

~~~json
{
  "source": "00abff30",
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
- 参照命令 [`00abff34`](#insn-00abff34)

~~~json
{
  "source": "00abff34",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abff38`](#insn-00abff38)

~~~json
{
  "source": "00abff38",
  "target": "00abf8f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abff40`](#insn-00abff40)

~~~json
{
  "source": "00abff40",
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
- 参照命令 [`00abff44`](#insn-00abff44)

~~~json
{
  "source": "00abff44",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abff48`](#insn-00abff48)

~~~json
{
  "source": "00abff48",
  "target": "00abfa18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abff54`](#insn-00abff54)

~~~json
{
  "source": "00abff54",
  "target": "0047ed74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abff58`](#insn-00abff58)

~~~json
{
  "source": "00abff58",
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
- 参照命令 [`00abff60`](#insn-00abff60)

~~~json
{
  "source": "00abff60",
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
- 参照命令 [`00abff64`](#insn-00abff64)

~~~json
{
  "source": "00abff64",
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
- 参照命令 [`00abff64`](#insn-00abff64)

~~~json
{
  "source": "00abff64",
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
- 参照命令 [`00abff6c`](#insn-00abff6c)

~~~json
{
  "source": "00abff6c",
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
- 参照命令 [`00abff70`](#insn-00abff70)

~~~json
{
  "source": "00abff70",
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
- 参照命令 [`00abff70`](#insn-00abff70)

~~~json
{
  "source": "00abff70",
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
- 参照命令 [`00abff74`](#insn-00abff74)

~~~json
{
  "source": "00abff74",
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
- 参照命令 [`00abff78`](#insn-00abff78)

~~~json
{
  "source": "00abff78",
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
- 参照命令 [`00abff78`](#insn-00abff78)

~~~json
{
  "source": "00abff78",
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
- 参照命令 [`00abff78`](#insn-00abff78)

~~~json
{
  "source": "00abff78",
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
- 参照命令 [`00abff7c`](#insn-00abff7c)

~~~json
{
  "source": "00abff7c",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abff84`](#insn-00abff84)

~~~json
{
  "source": "00abff84",
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
- 参照命令 [`00abff88`](#insn-00abff88)

~~~json
{
  "source": "00abff88",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abff8c`](#insn-00abff8c)

~~~json
{
  "source": "00abff8c",
  "target": "00abfa18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abff94`](#insn-00abff94)

~~~json
{
  "source": "00abff94",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abff9c`](#insn-00abff9c)

~~~json
{
  "source": "00abff9c",
  "target": "00ac01a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abffa4`](#insn-00abffa4)

~~~json
{
  "source": "00abffa4",
  "target": "0049f3b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abffac`](#insn-00abffac)

~~~json
{
  "source": "00abffac",
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
- 参照命令 [`00abffb0`](#insn-00abffb0)

~~~json
{
  "source": "00abffb0",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abffb4`](#insn-00abffb4)

~~~json
{
  "source": "00abffb4",
  "target": "00abfb10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abffc0`](#insn-00abffc0)

~~~json
{
  "source": "00abffc0",
  "target": "0047ed74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abffc4`](#insn-00abffc4)

~~~json
{
  "source": "00abffc4",
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
- 参照命令 [`00abffcc`](#insn-00abffcc)

~~~json
{
  "source": "00abffcc",
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
- 参照命令 [`00abffd0`](#insn-00abffd0)

~~~json
{
  "source": "00abffd0",
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
- 参照命令 [`00abffd0`](#insn-00abffd0)

~~~json
{
  "source": "00abffd0",
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
- 参照命令 [`00abffd8`](#insn-00abffd8)

~~~json
{
  "source": "00abffd8",
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
- 参照命令 [`00abffdc`](#insn-00abffdc)

~~~json
{
  "source": "00abffdc",
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
- 参照命令 [`00abffdc`](#insn-00abffdc)

~~~json
{
  "source": "00abffdc",
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
- 参照命令 [`00abffe0`](#insn-00abffe0)

~~~json
{
  "source": "00abffe0",
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
- 参照命令 [`00abffe4`](#insn-00abffe4)

~~~json
{
  "source": "00abffe4",
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
- 参照命令 [`00abffe4`](#insn-00abffe4)

~~~json
{
  "source": "00abffe4",
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
- 参照命令 [`00abffe4`](#insn-00abffe4)

~~~json
{
  "source": "00abffe4",
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
- 参照命令 [`00abffe8`](#insn-00abffe8)

~~~json
{
  "source": "00abffe8",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfff0`](#insn-00abfff0)

~~~json
{
  "source": "00abfff0",
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
- 参照命令 [`00abfff4`](#insn-00abfff4)

~~~json
{
  "source": "00abfff4",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfff8`](#insn-00abfff8)

~~~json
{
  "source": "00abfff8",
  "target": "00abfb10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0000`](#insn-00ac0000)

~~~json
{
  "source": "00ac0000",
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
- 参照命令 [`00ac0004`](#insn-00ac0004)

~~~json
{
  "source": "00ac0004",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac0008`](#insn-00ac0008)

~~~json
{
  "source": "00ac0008",
  "target": "00abfc3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0014`](#insn-00ac0014)

~~~json
{
  "source": "00ac0014",
  "target": "0047ed74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac0018`](#insn-00ac0018)

~~~json
{
  "source": "00ac0018",
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
- 参照命令 [`00ac0020`](#insn-00ac0020)

~~~json
{
  "source": "00ac0020",
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
- 参照命令 [`00ac0024`](#insn-00ac0024)

~~~json
{
  "source": "00ac0024",
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
- 参照命令 [`00ac0024`](#insn-00ac0024)

~~~json
{
  "source": "00ac0024",
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
- 参照命令 [`00ac002c`](#insn-00ac002c)

~~~json
{
  "source": "00ac002c",
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
- 参照命令 [`00ac0030`](#insn-00ac0030)

~~~json
{
  "source": "00ac0030",
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
- 参照命令 [`00ac0030`](#insn-00ac0030)

~~~json
{
  "source": "00ac0030",
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
- 参照命令 [`00ac0034`](#insn-00ac0034)

~~~json
{
  "source": "00ac0034",
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
- 参照命令 [`00ac0038`](#insn-00ac0038)

~~~json
{
  "source": "00ac0038",
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
- 参照命令 [`00ac0038`](#insn-00ac0038)

~~~json
{
  "source": "00ac0038",
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
- 参照命令 [`00ac0038`](#insn-00ac0038)

~~~json
{
  "source": "00ac0038",
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
- 参照命令 [`00ac003c`](#insn-00ac003c)

~~~json
{
  "source": "00ac003c",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac0044`](#insn-00ac0044)

~~~json
{
  "source": "00ac0044",
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
- 参照命令 [`00ac0048`](#insn-00ac0048)

~~~json
{
  "source": "00ac0048",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac004c`](#insn-00ac004c)

~~~json
{
  "source": "00ac004c",
  "target": "00abfc3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0054`](#insn-00ac0054)

~~~json
{
  "source": "00ac0054",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac005c`](#insn-00ac005c)

~~~json
{
  "source": "00ac005c",
  "target": "00ac01a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0064`](#insn-00ac0064)

~~~json
{
  "source": "00ac0064",
  "target": "0049f3b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac006c`](#insn-00ac006c)

~~~json
{
  "source": "00ac006c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0074`](#insn-00ac0074)

~~~json
{
  "source": "00ac0074",
  "target": "00ac01a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac007c`](#insn-00ac007c)

~~~json
{
  "source": "00ac007c",
  "target": "00ac0de8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac0080`](#insn-00ac0080)

~~~json
{
  "source": "00ac0080",
  "target": "00ac00b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac00b0`](#insn-00ac00b0)

~~~json
{
  "source": "00ac00b0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac00b8`](#insn-00ac00b8)

~~~json
{
  "source": "00ac00b8",
  "target": "00ac014c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac00bc`](#insn-00ac00bc)

~~~json
{
  "source": "00ac00bc",
  "target": "00ac018c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac014c`](#insn-00ac014c)

~~~json
{
  "source": "00ac014c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0150`](#insn-00ac0150)

~~~json
{
  "source": "00ac0150",
  "target": "00ac0188",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0188`](#insn-00ac0188)

~~~json
{
  "source": "00ac0188",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac0190`](#insn-00ac0190)

~~~json
{
  "source": "00ac0190",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0198`](#insn-00ac0198)

~~~json
{
  "source": "00ac0198",
  "target": "00ac01a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac01a0`](#insn-00ac01a0)

~~~json
{
  "source": "00ac01a0",
  "target": "00c53b3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac01a4`](#insn-00ac01a4)

~~~json
{
  "source": "00ac01a4",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
