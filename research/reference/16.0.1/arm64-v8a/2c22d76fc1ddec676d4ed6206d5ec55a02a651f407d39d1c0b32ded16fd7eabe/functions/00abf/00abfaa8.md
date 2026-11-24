# 00abfaa8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00abf8ac`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abf/00abf8ac.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-7744c44cf700522463631d96716c5a93)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00abfb18`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00abf/00abfb18.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0065.md#compare-1a8afd9c44c801999be7ae36c7ff3eba)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abfaa8",
  "name": "FUN_00abfaa8",
  "size": 2064,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f6f9f5ffafb5cc0f8c8edcc51c21bd31d81a6506685cac76ffcea283ce299dc8",
  "source_text_sha256": "f6f9f5ffafb5cc0f8c8edcc51c21bd31d81a6506685cac76ffcea283ce299dc8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00abfaa8",
        "00ac027f"
      ],
      [
        "00ac02ac",
        "00ac02bb"
      ],
      [
        "00ac0348",
        "00ac034f"
      ],
      [
        "00ac0384",
        "00ac03a3"
      ]
    ],
    "bytes_sha256": "baa0dca404d793d720d05ae8c8da8f2b09e22d886e486fde8e767b7056b4b9a3",
    "instruction_count": 516,
    "instruction_bytes": 2064,
    "body_bytes": 2064,
    "indirect": 8,
    "unresolved": 8
  }
}
~~~

## 呼び出し元

- [00abf784](../00abf/00abf784.md)
- [00b3cad8](../00b3c/00b3cad8.md)

## 呼び出し先

- [0043bb20](../0043b/0043bb20.md)
- [00447ef4](../00447/00447ef4.md)
- [0046e970](../0046e/0046e970.md)
- [0047e60c](../0047e/0047e60c.md)
- [0047e8dc](../0047e/0047e8dc.md)
- [0048ce54](../0048c/0048ce54.md)
- [00492e08](../00492/00492e08.md)
- [0049f3f0](../0049f/0049f3f0.md)
- [00ac0fe4](../00ac0/00ac0fe4.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c53f5c](../00c53/00c53f5c.md)
- [00c57e30](../00c57/00c57e30.md)
- [00c57e50](../00c57/00c57e50.md)
- [00c57e70](../00c57/00c57e70.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)

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

## 疑似コード / UTF-8 18610 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void FUN_00abfaa8(long *param_1,long param_2)

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
    if (((DAT_00ca4f38 & 1) == 0) && (iVar3 = __cxa_guard_acquire(&DAT_00ca4f38), iVar3 != 0)) {
      DAT_00ca4f08 = 0;
      DAT_00ca4f00 = &DAT_00ca4f08;
      DAT_00ca4f28 = 0;
      DAT_00ca4f30 = 0;
                    /* catch() { ... } // from try @ 00ac0014 with catch @ 00ac011c */
      DAT_00ca4f20 = 0;
                    /* catch() { ... } // from try @ 00abff54 with catch @ 00ac0120 */
      DAT_00ca4f10 = 0;
      DAT_00ca4f18 = &DAT_00ca4f20;
      __cxa_atexit(FUN_0047edb4,&DAT_00ca4f00,&PTR_LOOP_00c62f90);
      __cxa_guard_release(&DAT_00ca4f38);
    }
                    /* try { // try from 00abfaf8 to 00bbfaff has its CatchHandler @ 00ac0234 */
    local_70 = 0x20;
    local_88 = 0x26;
    uStack_67 = (undefined7)s_medal_get000_png_002ab9a4._8_8_;
    cStack_60 = SUB81(s_medal_get000_png_002ab9a4._8_8_,7);
    local_6f[0] = s_medal_get000_png_002ab9a4[0];
    local_6f[1] = s_medal_get000_png_002ab9a4[1];
    local_6f[2] = s_medal_get000_png_002ab9a4[2];
    local_6f[3] = s_medal_get000_png_002ab9a4[3];
    local_6f[4] = s_medal_get000_png_002ab9a4[4];
    local_6f[5] = s_medal_get000_png_002ab9a4[5];
    local_6f[6] = s_medal_get000_png_002ab9a4[6];
    local_6f[7] = s_medal_get000_png_002ab9a4[7];
                    /* try { // try from 00abfb28 to 00bbfb33 has its CatchHandler @ 00ac022c */
    uStack_5f = 0;
    uStack_7f = (undefined6)s_medal_get000_imgcut_002adb15._8_8_;
    cStack_79 = SUB81(s_medal_get000_imgcut_002adb15._8_8_,6);
    uStack_78 = CONCAT31(0x747563,SUB81(s_medal_get000_imgcut_002adb15._8_8_,7));
    local_87 = (undefined6)s_medal_get000_imgcut_002adb15._0_8_;
    uStack_81 = SUB82(s_medal_get000_imgcut_002adb15._0_8_,6);
                    /* try { // try from 00abfb34 to 00bbfb37 has its CatchHandler @ 00ac0298 */
    uStack_74 = uStack_74 & 0xffffff00;
    FUN_0047e60c(&local_c0,&DAT_00ca4f00,&local_70,&local_88,0x2601);
    uVar2 = CONCAT44(uStack_b4,CONCAT13(cStack_b5,CONCAT21(uStack_b7,cStack_b8)));
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
                    /* try { // try from 00abfb6c to 00bbfb8b has its CatchHandler @ 00ac0300 */
    if ((plVar8 == (long *)0x0) || (lVar4 = FUN_00c53d00(0xffffffffffffffff,plVar8 + 1), lVar4 != 0)
       ) {
      plVar8 = (long *)CONCAT44(uStack_b4,CONCAT13(cStack_b5,CONCAT21(uStack_b7,cStack_b8)));
    }
    else {
      (**(code **)(*plVar8 + 0x10))(plVar8);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
      plVar8 = (long *)CONCAT44(uStack_b4,CONCAT13(cStack_b5,CONCAT21(uStack_b7,cStack_b8)));
    }
    if ((plVar8 != (long *)0x0) &&
       (lVar4 = FUN_00c53d00(0xffffffffffffffff,(long *)((long)plVar8 + 8)), lVar4 == 0)) {
                    /* try { // try from 00abfbdc to 00bbfbdf has its CatchHandler @ 00ac029c */
      (**(code **)(*plVar8 + 0x10))(plVar8);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
    }
    if ((local_88 & 1) != 0) {
      _ZdlPv((void *)CONCAT44(uStack_74,uStack_78));
    }
                    /* try { // try from 00abfba0 to 00bbfba7 has its CatchHandler @ 00ac026c */
    if ((local_70 & 1) != 0) {
      _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT22(uStack_5e,CONCAT11(uStack_5f,cStack_60))));
    }
                    /* catch() { ... } // from try @ 00abff48 with catch @ 00ac0138 */
    if (((DAT_00ca4f38 & 1) == 0) && (iVar3 = __cxa_guard_acquire(&DAT_00ca4f38), iVar3 != 0)) {
                    /* catch() { ... } // from try @ 00abff10 with catch @ 00ac0150 */
                    /* catch() { ... } // from try @ 00abffbc with catch @ 00ac0154 */
      DAT_00ca4f08 = 0;
                    /* catch() { ... } // from try @ 00abffb0 with catch @ 00ac015c */
                    /* catch() { ... } // from try @ 00abfea8 with catch @ 00ac0160 */
      DAT_00ca4f00 = &DAT_00ca4f08;
      DAT_00ca4f28 = 0;
      DAT_00ca4f30 = 0;
      DAT_00ca4f20 = 0;
                    /* catch() { ... } // from try @ 00abfe5c with catch @ 00ac0174 */
      DAT_00ca4f10 = 0;
      DAT_00ca4f18 = &DAT_00ca4f20;
                    /* catch() { ... } // from try @ 00abfe50 with catch @ 00ac0178 */
      __cxa_atexit(FUN_0047edb4,&DAT_00ca4f00,&PTR_LOOP_00c62f90);
                    /* catch() { ... } // from try @ 00abfe1c with catch @ 00ac0180 */
                    /* catch() { ... } // from try @ 00abf7f8 with catch @ 00ac0184 */
      __cxa_guard_release(&DAT_00ca4f38);
    }
                    /* try { // try from 00abfc1c to 00bbfc9b has its CatchHandler @ 00ac02d4 */
    local_88 = 0x1c;
    plVar8 = param_1 + 0xf;
    cStack_79 = 0;
    local_87._0_1_ = s_medal__03d_png_002bb847[0];
    local_87._1_1_ = s_medal__03d_png_002bb847[1];
    local_87._2_1_ = s_medal__03d_png_002bb847[2];
    local_87._3_1_ = s_medal__03d_png_002bb847[3];
    local_87._4_1_ = s_medal__03d_png_002bb847[4];
    local_87._5_1_ = s_medal__03d_png_002bb847[5];
    uStack_81._0_1_ = s_medal__03d_png_002bb847[6];
    uStack_81._1_1_ = s_medal__03d_png_002bb847[7];
    uStack_7f._0_1_ = s_medal__03d_png_002bb847[8];
    uStack_7f._1_1_ = s_medal__03d_png_002bb847[9];
    uStack_7f._2_1_ = s_medal__03d_png_002bb847[10];
    uStack_7f._3_1_ = s_medal__03d_png_002bb847[0xb];
    uStack_7f._4_1_ = s_medal__03d_png_002bb847[0xc];
    uStack_7f._5_1_ = s_medal__03d_png_002bb847[0xd];
    if ((undefined4 *)param_1[0x10] == (undefined4 *)*plVar8) {
                    /* catch() { ... } // from try @ 00abf7dc with catch @ 00ac0190 */
      if (*(long *)(lVar1 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
        FUN_0049f3f0(plVar8);
      }
      goto LAB_00ac03a0;
    }
    FUN_00447ef4(&local_70,&local_88,0,*(undefined4 *)*plVar8);
    local_c0 = 0x20;
    uStack_af = 0;
    uStack_b7 = (undefined2)s_medal_001_imgcut_002bcaee._8_8_;
    cStack_b5 = SUB81(s_medal_001_imgcut_002bcaee._8_8_,2);
    uStack_b4 = SUB84(s_medal_001_imgcut_002bcaee._8_8_,3);
    local_b0 = SUB81(s_medal_001_imgcut_002bcaee._8_8_,7);
    uStack_bf = (undefined7)s_medal_001_imgcut_002bcaee._0_8_;
    cStack_b8 = SUB81(s_medal_001_imgcut_002bcaee._0_8_,7);
    FUN_0047e60c(&local_a0,&DAT_00ca4f00,&local_70,&local_c0,0x2601);
    plVar7 = plStack_98;
    uVar5 = local_a0;
    plVar9 = *(long **)(param_2 + 0x60);
    local_a0 = 0;
    plStack_98 = (long *)0x0;
                    /* try { // try from 00abfca4 to 00bbfcab has its CatchHandler @ 00ac029c */
    *(long **)(param_2 + 0x60) = plVar7;
    *(undefined8 *)(param_2 + 0x58) = uVar5;
    plVar7 = plStack_98;
                    /* try { // try from 00abfcac to 00bbfcbb has its CatchHandler @ 00ac0250 */
    if ((plVar9 != (long *)0x0) &&
       (lVar4 = FUN_00c53d00(0xffffffffffffffff,plVar9 + 1), plVar7 = plStack_98, lVar4 == 0)) {
      (**(code **)(*plVar9 + 0x10))(plVar9);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
                    /* try { // try from 00abfff8 to 00bc000b has its CatchHandler @ 00ac02d8 */
      plVar7 = plStack_98;
    }
    plStack_98 = plVar7;
    if ((plVar7 != (long *)0x0) &&
       (lVar4 = FUN_00c53d00(0xffffffffffffffff,(long *)((long)plVar7 + 8)), lVar4 == 0)) {
      (**(code **)(*plVar7 + 0x10))(plVar7);
                    /* try { // try from 00ac0014 to 00bc001f has its CatchHandler @ 00ac011c */
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
                    /* try { // try from 00ac0020 to 00bc005b has its CatchHandler @ 00abf6d8 */
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
                    /* catch() { ... } // from try @ 00abf9bc with catch @ 00ac01f8 */
                    /* catch() { ... } // from try @ 00abfd54 with catch @ 00ac0200 */
      if (((DAT_00ca4f38 & 1) == 0) && (iVar3 = __cxa_guard_acquire(&DAT_00ca4f38), iVar3 != 0)) {
        DAT_00ca4f08 = 0;
                    /* catch() { ... } // from try @ 00abfd2c with catch @ 00ac0218 */
        DAT_00ca4f00 = &DAT_00ca4f08;
                    /* catch() { ... } // from try @ 00abfb28 with catch @ 00ac022c */
        DAT_00ca4f28 = 0;
        DAT_00ca4f30 = 0;
        DAT_00ca4f20 = 0;
                    /* catch() { ... } // from try @ 00abfaf8 with catch @ 00ac0234 */
        DAT_00ca4f10 = 0;
        DAT_00ca4f18 = &DAT_00ca4f20;
                    /* catch() { ... } // from try @ 00abfcd4 with catch @ 00ac0238 */
        __cxa_atexit(FUN_0047edb4,&DAT_00ca4f00,&PTR_LOOP_00c62f90);
        __cxa_guard_release(&DAT_00ca4f38);
      }
      local_c0 = 0x14;
                    /* try { // try from 00abfe50 to 00bbfe5b has its CatchHandler @ 00ac0178 */
      uStack_b7 = 0x3174;
      uStack_bf = (undefined7)s_medal_txt1_002a189e._0_8_;
      cStack_b8 = SUB81(s_medal_txt1_002a189e._0_8_,7);
      cStack_b5 = 0;
                    /* try { // try from 00abfe5c to 00bbfe6f has its CatchHandler @ 00ac0174 */
      FUN_0048ce54(&local_88,&local_c0);
      if ((int *)param_1[0x10] == (int *)param_1[0xf]) {
                    /* catch() { ... } // from try @ 00abfcac with catch @ 00ac0250 */
        if (*(long *)(lVar1 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
          FUN_0049f3f0(plVar8);
        }
        goto LAB_00ac03a0;
      }
      uVar6 = (ulong)*(int *)param_1[0xf];
      if ((ulong)(param_1[1] - *param_1 >> 3) <= uVar6) {
                    /* catch() { ... } // from try @ 00abfbd0 with catch @ 00ac0264 */
                    /* catch() { ... } // from try @ 00abfba0 with catch @ 00ac026c */
                    /* catch() { ... } // from try @ 00abfa0c with catch @ 00ac0270 */
        if (*(long *)(lVar1 + 0x28) == local_58) {
          uVar5 = FUN_00ac0fe4(param_1);
          if ((local_70 & 1) != 0) {
            _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT22(uStack_5e,CONCAT11(uStack_5f,cStack_60))));
          }
          if (*(long *)(lVar1 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
            FUN_00c53f5c(uVar5);
          }
        }
        goto LAB_00ac03a0;
      }
      lVar4 = *(long *)(*param_1 + uVar6 * 8);
      if ((*(byte *)(lVar4 + 0x80) & 1) == 0) {
        uStack_d8 = *(undefined8 *)(lVar4 + 0x88);
        local_e0 = *(ulong *)(lVar4 + 0x80);
        local_d0 = *(void **)(lVar4 + 0x90);
                    /* try { // try from 00abfea8 to 00bbfeaf has its CatchHandler @ 00ac0160 */
      }
      else {
        FUN_0043bb20(&local_e0,*(undefined8 *)(lVar4 + 0x90),*(undefined8 *)(lVar4 + 0x88));
      }
      FUN_00492e08(&local_70,&local_88,&local_e0);
      FUN_0047e8dc(&local_a0,&DAT_00ca4f00,&local_70,PTR_DAT_00c9aca0,0x14,0,0,0);
      plVar8 = plStack_98;
      uVar5 = local_a0;
      plVar7 = *(long **)(param_2 + 0x70);
                    /* try { // try from 00abfefc to 00bbff0f has its CatchHandler @ 00ac02a4 */
      local_a0 = 0;
      plStack_98 = (long *)0x0;
      *(long **)(param_2 + 0x70) = plVar8;
      *(undefined8 *)(param_2 + 0x68) = uVar5;
                    /* try { // try from 00abff10 to 00bbff1b has its CatchHandler @ 00ac0150 */
      if ((plVar7 != (long *)0x0) &&
         (lVar4 = FUN_00c53d00(0xffffffffffffffff,plVar7 + 1), lVar4 == 0)) {
        (**(code **)(*plVar7 + 0x10))(plVar7);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
      }
      plVar8 = plStack_98;
      if ((plStack_98 != (long *)0x0) &&
         (lVar4 = FUN_00c53d00(0xffffffffffffffff,plStack_98 + 1), lVar4 == 0)) {
        (**(code **)(*plVar8 + 0x10))(plVar8);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
      }
      if ((local_70 & 1) != 0) {
                    /* try { // try from 00ac00b0 to 00bc0333 has its CatchHandler @ 00abf6d8 */
        _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT22(uStack_5e,CONCAT11(uStack_5f,cStack_60))));
      }
                    /* try { // try from 00abff54 to 00bbff6f has its CatchHandler @ 00ac0120 */
      if ((local_e0 & 1) != 0) {
        _ZdlPv(local_d0);
      }
      if ((local_88 & 1) != 0) {
        _ZdlPv((void *)CONCAT44(uStack_74,uStack_78));
      }
      if ((local_c0 & 1) != 0) {
        _ZdlPv((void *)CONCAT62(uStack_ae,CONCAT11(uStack_af,local_b0)));
      }
      local_70 = 0x26;
      uStack_5f = 0x6e;
      uStack_5e = 0x6d69;
                    /* try { // try from 00abff90 to 00bbffab has its CatchHandler @ 00ac02a4 */
      uStack_67 = (undefined7)s_medal_get001_maanim_002b7bbd._8_8_;
      cStack_60 = SUB81(s_medal_get001_maanim_002b7bbd._8_8_,7);
      local_6f[0] = s_medal_get001_maanim_002b7bbd[0];
      local_6f[1] = s_medal_get001_maanim_002b7bbd[1];
      local_6f[2] = s_medal_get001_maanim_002b7bbd[2];
      local_6f[3] = s_medal_get001_maanim_002b7bbd[3];
      local_6f[4] = s_medal_get001_maanim_002b7bbd[4];
      local_6f[5] = s_medal_get001_maanim_002b7bbd[5];
      local_6f[6] = s_medal_get001_maanim_002b7bbd[6];
      local_6f[7] = s_medal_get001_maanim_002b7bbd[7];
      uStack_5c = uStack_5c & 0xffffff00;
      FUN_0046e970(param_1 + 0x2a,&local_70);
    }
    else {
                    /* catch() { ... } // from try @ 00abf814 with catch @ 00ac01a4 */
      if (((DAT_00ca4f38 & 1) == 0) && (iVar3 = __cxa_guard_acquire(&DAT_00ca4f38), iVar3 != 0)) {
        DAT_00ca4f08 = 0;
        DAT_00ca4f00 = &DAT_00ca4f08;
        DAT_00ca4f28 = 0;
        DAT_00ca4f30 = 0;
        DAT_00ca4f20 = 0;
        DAT_00ca4f10 = 0;
        DAT_00ca4f18 = &DAT_00ca4f20;
        __cxa_atexit(FUN_0047edb4,&DAT_00ca4f00,&PTR_LOOP_00c62f90);
                    /* catch() { ... } // from try @ 00ac005c with catch @ 00ac01ec */
                    /* catch() { ... } // from try @ 00abf9e0 with catch @ 00ac01f0 */
        __cxa_guard_release(&DAT_00ca4f38);
      }
      local_c0 = 0x14;
                    /* try { // try from 00abfd24 to 00bbfd2b has its CatchHandler @ 00ac0298 */
      uStack_b7 = 0x3274;
      uStack_bf = (undefined7)s_medal_txt2_002a1893._0_8_;
      cStack_b8 = SUB81(s_medal_txt2_002a1893._0_8_,7);
                    /* try { // try from 00abfd2c to 00bbfd3b has its CatchHandler @ 00ac0218 */
      cStack_b5 = 0;
      FUN_0048ce54(&local_88,&local_c0);
                    /* try { // try from 00abfd54 to 00bbfd5b has its CatchHandler @ 00ac0200 */
      FUN_00447ef4(&local_70,&local_88,0,(ulong)(param_1[0x10] - param_1[0xf]) >> 2);
      FUN_0047e8dc(&local_a0,&DAT_00ca4f00,&local_70,PTR_DAT_00c9aca0,0x14,0,0,0);
      plVar8 = plStack_98;
      uVar5 = local_a0;
                    /* try { // try from 00abfd84 to 00bbfdcf has its CatchHandler @ 00ac0300 */
      plVar7 = *(long **)(param_2 + 0x70);
      local_a0 = 0;
      plStack_98 = (long *)0x0;
      *(long **)(param_2 + 0x70) = plVar8;
      *(undefined8 *)(param_2 + 0x68) = uVar5;
      if ((plVar7 != (long *)0x0) &&
         (lVar4 = FUN_00c53d00(0xffffffffffffffff,plVar7 + 1), lVar4 == 0)) {
        (**(code **)(*plVar7 + 0x10))(plVar7);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
      }
      plVar8 = plStack_98;
      if ((plStack_98 != (long *)0x0) &&
         (lVar4 = FUN_00c53d00(0xffffffffffffffff,plStack_98 + 1), lVar4 == 0)) {
        (**(code **)(*plVar8 + 0x10))(plVar8);
                    /* try { // try from 00ac005c to 00bc00af has its CatchHandler @ 00ac01ec */
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
      }
      if ((local_70 & 1) != 0) {
        _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT22(uStack_5e,CONCAT11(uStack_5f,cStack_60))));
      }
      if ((local_88 & 1) != 0) {
        _ZdlPv((void *)CONCAT44(uStack_74,uStack_78));
      }
      if ((local_c0 & 1) != 0) {
        _ZdlPv((void *)CONCAT62(uStack_ae,CONCAT11(uStack_af,local_b0)));
      }
                    /* try { // try from 00abfe10 to 00bbfe1b has its CatchHandler @ 00ac02a4 */
      local_70 = 0x26;
      uStack_5f = 0x6e;
      uStack_5e = 0x6d69;
      uStack_67 = (undefined7)s_medal_get002_maanim_002afefe._8_8_;
      cStack_60 = SUB81(s_medal_get002_maanim_002afefe._8_8_,7);
      local_6f[0] = s_medal_get002_maanim_002afefe[0];
      local_6f[1] = s_medal_get002_maanim_002afefe[1];
      local_6f[2] = s_medal_get002_maanim_002afefe[2];
      local_6f[3] = s_medal_get002_maanim_002afefe[3];
      local_6f[4] = s_medal_get002_maanim_002afefe[4];
      local_6f[5] = s_medal_get002_maanim_002afefe[5];
      local_6f[6] = s_medal_get002_maanim_002afefe[6];
      local_6f[7] = s_medal_get002_maanim_002afefe[7];
                    /* try { // try from 00abfe1c to 00bbfe23 has its CatchHandler @ 00ac0180 */
      uStack_5c = uStack_5c & 0xffffff00;
      FUN_0046e970(param_1 + 0x2a,&local_70);
    }
    if ((local_70 & 1) != 0) {
                    /* try { // try from 00abffb0 to 00bbffbb has its CatchHandler @ 00ac015c */
      _ZdlPv((void *)CONCAT44(uStack_5c,CONCAT22(uStack_5e,CONCAT11(uStack_5f,cStack_60))));
    }
  }
                    /* try { // try from 00abffbc to 00bbffcb has its CatchHandler @ 00ac0154 */
  if (*(long *)(lVar1 + 0x28) == local_58) {
    return;
  }
LAB_00ac03a0:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00abfaa8"></a> `00abfaa8` | `ff 83 03 d1` | sub sp,sp,#0xe0 | `FALL_THROUGH`
<a id="insn-00abfaac"></a> `00abfaac` | `fd 7b 09 a9` | stp x29,x30,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abfab0"></a> `00abfab0` | `f9 53 00 f9` | str x25,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00abfab4"></a> `00abfab4` | `f8 5f 0b a9` | stp x24,x23,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00abfab8"></a> `00abfab8` | `f6 57 0c a9` | stp x22,x21,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00abfabc"></a> `00abfabc` | `f4 4f 0d a9` | stp x20,x19,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00abfac0"></a> `00abfac0` | `fd 43 02 91` | add x29,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00abfac4"></a> `00abfac4` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00abfac8"></a> `00abfac8` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00abfacc"></a> `00abfacc` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abfad0"></a> `00abfad0` | `08 70 40 b9` | ldr w8,[x0, #0x70] | `FALL_THROUGH`
<a id="insn-00abfad4"></a> `00abfad4` | `1f 05 00 31` | cmn w8,#0x1 | `FALL_THROUGH`
<a id="insn-00abfad8"></a> `00abfad8` | `e0 26 00 54` | b.eq 0x00abffb4 | `CONDITIONAL_JUMP`
<a id="insn-00abfadc"></a> `00abfadc` | `39 0f 00 b0` | adrp x25,0xca4000 | `FALL_THROUGH`
<a id="insn-00abfae0"></a> `00abfae0` | `39 e3 3c 91` | add x25,x25,#0xf38 | `FALL_THROUGH`
<a id="insn-00abfae4"></a> `00abfae4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00abfae8"></a> `00abfae8` | `28 ff df 08` | ldarb w8,[x25] | `FALL_THROUGH`
<a id="insn-00abfaec"></a> `00abfaec` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00abfaf0"></a> `00abfaf0` | `88 2f 00 36` | tbz w8,#0x0,0x00ac00e0 | `CONDITIONAL_JUMP`
<a id="insn-00abfaf4"></a> `00abfaf4` | `68 bf ff 90` | adrp x8,0x2ab000 | `FALL_THROUGH`
<a id="insn-00abfaf8"></a> `00abfaf8` | `08 91 26 91` | add x8,x8,#0x9a4 | `FALL_THROUGH`
<a id="insn-00abfafc"></a> `00abfafc` | `09 04 80 52` | mov w9,#0x20 | `FALL_THROUGH`
<a id="insn-00abfb00"></a> `00abfb00` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00abfb04"></a> `00abfb04` | `a9 03 1e 38` | sturb w9,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abfb08"></a> `00abfb08` | `c8 04 80 52` | mov w8,#0x26 | `FALL_THROUGH`
<a id="insn-00abfb0c"></a> `00abfb0c` | `69 bf ff d0` | adrp x9,0x2ad000 | `FALL_THROUGH`
<a id="insn-00abfb10"></a> `00abfb10` | `29 55 2c 91` | add x9,x9,#0xb15 | `FALL_THROUGH`
<a id="insn-00abfb14"></a> `00abfb14` | `a8 83 1c 38` | sturb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00abfb18"></a> `00abfb18` | `a0 13 9e 3c` | stur q0,[x29, #-0x1f] | `FALL_THROUGH`
<a id="insn-00abfb1c"></a> `00abfb1c` | `e8 6c 8c 52` | mov w8,#0x6367 | `FALL_THROUGH`
<a id="insn-00abfb20"></a> `00abfb20` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00abfb24"></a> `00abfb24` | `a8 8e ae 72` | movk w8,#0x7475, LSL #16 | `FALL_THROUGH`
<a id="insn-00abfb28"></a> `00abfb28` | `bf 13 1f 38` | sturb wzr,[x29, #-0xf] | `FALL_THROUGH`
<a id="insn-00abfb2c"></a> `00abfb2c` | `a8 83 1d b8` | stur w8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00abfb30"></a> `00abfb30` | `a0 93 9c 3c` | stur q0,[x29, #-0x37] | `FALL_THROUGH`
<a id="insn-00abfb34"></a> `00abfb34` | `bf c3 1d 38` | sturb wzr,[x29, #-0x24] | `FALL_THROUGH`
<a id="insn-00abfb38"></a> `00abfb38` | `35 0f 00 b0` | adrp x21,0xca4000 | `FALL_THROUGH`
<a id="insn-00abfb3c"></a> `00abfb3c` | `b5 02 3c 91` | add x21,x21,#0xf00 | `FALL_THROUGH`
<a id="insn-00abfb40"></a> `00abfb40` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00abfb44"></a> `00abfb44` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00abfb48"></a> `00abfb48` | `a2 e3 00 d1` | sub x2,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00abfb4c"></a> `00abfb4c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abfb50"></a> `00abfb50` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-00abfb54"></a> `00abfb54` | `ae fa e6 97` | bl 0x0047e60c | `UNCONDITIONAL_CALL`
<a id="insn-00abfb58"></a> `00abfb58` | `e0 0b c0 3d` | ldr q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abfb5c"></a> `00abfb5c` | `96 2a 40 f9` | ldr x22,[x20, #0x50] | `FALL_THROUGH`
<a id="insn-00abfb60"></a> `00abfb60` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abfb64"></a> `00abfb64` | `80 82 84 3c` | stur q0,[x20, #0x48] | `FALL_THROUGH`
<a id="insn-00abfb68"></a> `00abfb68` | `b6 00 00 b4` | cbz x22,0x00abfb7c | `CONDITIONAL_JUMP`
<a id="insn-00abfb6c"></a> `00abfb6c` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00abfb70"></a> `00abfb70` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abfb74"></a> `00abfb74` | `63 50 06 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00abfb78"></a> `00abfb78` | `c0 01 00 b4` | cbz x0,0x00abfbb0 | `CONDITIONAL_JUMP`
<a id="insn-00abfb7c"></a> `00abfb7c` | `f6 17 40 f9` | ldr x22,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00abfb80"></a> `00abfb80` | `b6 00 00 b4` | cbz x22,0x00abfb94 | `CONDITIONAL_JUMP`
<a id="insn-00abfb84"></a> `00abfb84` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00abfb88"></a> `00abfb88` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abfb8c"></a> `00abfb8c` | `5d 50 06 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00abfb90"></a> `00abfb90` | `20 02 00 b4` | cbz x0,0x00abfbd4 | `CONDITIONAL_JUMP`
<a id="insn-00abfb94"></a> `00abfb94` | `a8 83 5c 38` | ldurb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00abfb98"></a> `00abfb98` | `e8 02 00 37` | tbnz w8,#0x0,0x00abfbf4 | `CONDITIONAL_JUMP`
<a id="insn-00abfb9c"></a> `00abfb9c` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abfba0"></a> `00abfba0` | `28 03 00 37` | tbnz w8,#0x0,0x00abfc04 | `CONDITIONAL_JUMP`
<a id="insn-00abfba4"></a> `00abfba4` | `28 ff df 08` | ldarb w8,[x25] | `FALL_THROUGH`
<a id="insn-00abfba8"></a> `00abfba8` | `68 03 00 37` | tbnz w8,#0x0,0x00abfc14 | `CONDITIONAL_JUMP`
<a id="insn-00abfbac"></a> `00abfbac` | `63 01 00 14` | b 0x00ac0138 | `UNCONDITIONAL_JUMP`
<a id="insn-00abfbb0"></a> `00abfbb0` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00abfbb4"></a> `00abfbb4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00abfbb8"></a> `00abfbb8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abfbbc"></a> `00abfbbc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abfbc0"></a> `00abfbc0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00abfbc4"></a> `00abfbc4` | `af 60 06 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00abfbc8"></a> `00abfbc8` | `f6 17 40 f9` | ldr x22,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00abfbcc"></a> `00abfbcc` | `d6 fd ff b5` | cbnz x22,0x00abfb84 | `CONDITIONAL_JUMP`
<a id="insn-00abfbd0"></a> `00abfbd0` | `f1 ff ff 17` | b 0x00abfb94 | `UNCONDITIONAL_JUMP`
<a id="insn-00abfbd4"></a> `00abfbd4` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00abfbd8"></a> `00abfbd8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00abfbdc"></a> `00abfbdc` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abfbe0"></a> `00abfbe0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abfbe4"></a> `00abfbe4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00abfbe8"></a> `00abfbe8` | `a6 60 06 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00abfbec"></a> `00abfbec` | `a8 83 5c 38` | ldurb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00abfbf0"></a> `00abfbf0` | `68 fd 07 36` | tbz w8,#0x0,0x00abfb9c | `CONDITIONAL_JUMP`
<a id="insn-00abfbf4"></a> `00abfbf4` | `a0 83 5d f8` | ldur x0,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00abfbf8"></a> `00abfbf8` | `ae 60 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00abfbfc"></a> `00abfbfc` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abfc00"></a> `00abfc00` | `28 fd 07 36` | tbz w8,#0x0,0x00abfba4 | `CONDITIONAL_JUMP`
<a id="insn-00abfc04"></a> `00abfc04` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abfc08"></a> `00abfc08` | `aa 60 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00abfc0c"></a> `00abfc0c` | `28 ff df 08` | ldarb w8,[x25] | `FALL_THROUGH`
<a id="insn-00abfc10"></a> `00abfc10` | `48 29 00 36` | tbz w8,#0x0,0x00ac0138 | `CONDITIONAL_JUMP`
<a id="insn-00abfc14"></a> `00abfc14` | `88 03 80 52` | mov w8,#0x1c | `FALL_THROUGH`
<a id="insn-00abfc18"></a> `00abfc18` | `f5 03 13 aa` | mov x21,x19 | `FALL_THROUGH`
<a id="insn-00abfc1c"></a> `00abfc1c` | `e9 bf ff 90` | adrp x9,0x2bb000 | `FALL_THROUGH`
<a id="insn-00abfc20"></a> `00abfc20` | `29 1d 21 91` | add x9,x9,#0x847 | `FALL_THROUGH`
<a id="insn-00abfc24"></a> `00abfc24` | `a8 83 1c 38` | sturb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00abfc28"></a> `00abfc28` | `a8 ae c7 a9` | ldp x8,x11,[x21, #0x78]! | `FALL_THROUGH`
<a id="insn-00abfc2c"></a> `00abfc2c` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00abfc30"></a> `00abfc30` | `29 61 40 f8` | ldur x9,[x9, #0x6] | `FALL_THROUGH`
<a id="insn-00abfc34"></a> `00abfc34` | `bf 73 1d 38` | sturb wzr,[x29, #-0x29] | `FALL_THROUGH`
<a id="insn-00abfc38"></a> `00abfc38` | `7f 01 08 eb` | cmp x11,x8 | `FALL_THROUGH`
<a id="insn-00abfc3c"></a> `00abfc3c` | `aa 93 1c f8` | stur x10,[x29, #-0x37] | `FALL_THROUGH`
<a id="insn-00abfc40"></a> `00abfc40` | `a9 f3 1c f8` | stur x9,[x29, #-0x31] | `FALL_THROUGH`
<a id="insn-00abfc44"></a> `00abfc44` | `40 2a 00 54` | b.eq 0x00ac018c | `CONDITIONAL_JUMP`
<a id="insn-00abfc48"></a> `00abfc48` | `02 01 40 b9` | ldr w2,[x8] | `FALL_THROUGH`
<a id="insn-00abfc4c"></a> `00abfc4c` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00abfc50"></a> `00abfc50` | `a0 e3 00 d1` | sub x0,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00abfc54"></a> `00abfc54` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00abfc58"></a> `00abfc58` | `a7 20 e6 97` | bl 0x00447ef4 | `UNCONDITIONAL_CALL`
<a id="insn-00abfc5c"></a> `00abfc5c` | `e9 bf ff b0` | adrp x9,0x2bc000 | `FALL_THROUGH`
<a id="insn-00abfc60"></a> `00abfc60` | `29 b9 2b 91` | add x9,x9,#0xaee | `FALL_THROUGH`
<a id="insn-00abfc64"></a> `00abfc64` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00abfc68"></a> `00abfc68` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00abfc6c"></a> `00abfc6c` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abfc70"></a> `00abfc70` | `ff c7 00 39` | strb wzr,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00abfc74"></a> `00abfc74` | `e0 13 82 3c` | stur q0,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00abfc78"></a> `00abfc78` | `36 0f 00 b0` | adrp x22,0xca4000 | `FALL_THROUGH`
<a id="insn-00abfc7c"></a> `00abfc7c` | `d6 02 3c 91` | add x22,x22,#0xf00 | `FALL_THROUGH`
<a id="insn-00abfc80"></a> `00abfc80` | `e8 03 01 91` | add x8,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00abfc84"></a> `00abfc84` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00abfc88"></a> `00abfc88` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00abfc8c"></a> `00abfc8c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00abfc90"></a> `00abfc90` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-00abfc94"></a> `00abfc94` | `5e fa e6 97` | bl 0x0047e60c | `UNCONDITIONAL_CALL`
<a id="insn-00abfc98"></a> `00abfc98` | `e0 13 c0 3d` | ldr q0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abfc9c"></a> `00abfc9c` | `97 32 40 f9` | ldr x23,[x20, #0x60] | `FALL_THROUGH`
<a id="insn-00abfca0"></a> `00abfca0` | `ff 7f 04 a9` | stp xzr,xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abfca4"></a> `00abfca4` | `80 82 85 3c` | stur q0,[x20, #0x58] | `FALL_THROUGH`
<a id="insn-00abfca8"></a> `00abfca8` | `b7 00 00 b4` | cbz x23,0x00abfcbc | `CONDITIONAL_JUMP`
<a id="insn-00abfcac"></a> `00abfcac` | `e1 22 00 91` | add x1,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00abfcb0"></a> `00abfcb0` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abfcb4"></a> `00abfcb4` | `13 50 06 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00abfcb8"></a> `00abfcb8` | `40 19 00 b4` | cbz x0,0x00abffe0 | `CONDITIONAL_JUMP`
<a id="insn-00abfcbc"></a> `00abfcbc` | `f7 27 40 f9` | ldr x23,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00abfcc0"></a> `00abfcc0` | `b7 00 00 b4` | cbz x23,0x00abfcd4 | `CONDITIONAL_JUMP`
<a id="insn-00abfcc4"></a> `00abfcc4` | `e1 22 00 91` | add x1,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00abfcc8"></a> `00abfcc8` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abfccc"></a> `00abfccc` | `0d 50 06 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00abfcd0"></a> `00abfcd0` | `a0 19 00 b4` | cbz x0,0x00ac0004 | `CONDITIONAL_JUMP`
<a id="insn-00abfcd4"></a> `00abfcd4` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abfcd8"></a> `00abfcd8` | `68 1a 00 37` | tbnz w8,#0x0,0x00ac0024 | `CONDITIONAL_JUMP`
<a id="insn-00abfcdc"></a> `00abfcdc` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abfce0"></a> `00abfce0` | `a8 1a 00 37` | tbnz w8,#0x0,0x00ac0034 | `CONDITIONAL_JUMP`
<a id="insn-00abfce4"></a> `00abfce4` | `a8 83 5c 38` | ldurb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00abfce8"></a> `00abfce8` | `68 00 00 36` | tbz w8,#0x0,0x00abfcf4 | `CONDITIONAL_JUMP`
<a id="insn-00abfcec"></a> `00abfcec` | `a0 83 5d f8` | ldur x0,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00abfcf0"></a> `00abfcf0` | `70 60 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00abfcf4"></a> `00abfcf4` | `69 a2 47 a9` | ldp x9,x8,[x19, #0x78] | `FALL_THROUGH`
<a id="insn-00abfcf8"></a> `00abfcf8` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00abfcfc"></a> `00abfcfc` | `1f 15 00 f1` | cmp x8,#0x5 | `FALL_THROUGH`
<a id="insn-00abfd00"></a> `00abfd00` | `83 09 00 54` | b.cc 0x00abfe30 | `CONDITIONAL_JUMP`
<a id="insn-00abfd04"></a> `00abfd04` | `28 ff df 08` | ldarb w8,[x25] | `FALL_THROUGH`
<a id="insn-00abfd08"></a> `00abfd08` | `e8 24 00 36` | tbz w8,#0x0,0x00ac01a4 | `CONDITIONAL_JUMP`
<a id="insn-00abfd0c"></a> `00abfd0c` | `09 bf ff d0` | adrp x9,0x2a1000 | `FALL_THROUGH`
<a id="insn-00abfd10"></a> `00abfd10` | `29 4d 22 91` | add x9,x9,#0x893 | `FALL_THROUGH`
<a id="insn-00abfd14"></a> `00abfd14` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-00abfd18"></a> `00abfd18` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00abfd1c"></a> `00abfd1c` | `8a 4e 86 52` | mov w10,#0x3274 | `FALL_THROUGH`
<a id="insn-00abfd20"></a> `00abfd20` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abfd24"></a> `00abfd24` | `ea 93 02 78` | sturh w10,[sp, #0x29] | `FALL_THROUGH`
<a id="insn-00abfd28"></a> `00abfd28` | `e9 13 02 f8` | stur x9,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00abfd2c"></a> `00abfd2c` | `ff af 00 39` | strb wzr,[sp, #0x2b] | `FALL_THROUGH`
<a id="insn-00abfd30"></a> `00abfd30` | `a8 e3 00 d1` | sub x8,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00abfd34"></a> `00abfd34` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00abfd38"></a> `00abfd38` | `47 34 e7 97` | bl 0x0048ce54 | `UNCONDITIONAL_CALL`
<a id="insn-00abfd3c"></a> `00abfd3c` | `69 a2 47 a9` | ldp x9,x8,[x19, #0x78] | `FALL_THROUGH`
<a id="insn-00abfd40"></a> `00abfd40` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00abfd44"></a> `00abfd44` | `02 fd 42 d3` | lsr x2,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00abfd48"></a> `00abfd48` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00abfd4c"></a> `00abfd4c` | `a0 e3 00 d1` | sub x0,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00abfd50"></a> `00abfd50` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00abfd54"></a> `00abfd54` | `68 20 e6 97` | bl 0x00447ef4 | `UNCONDITIONAL_CALL`
<a id="insn-00abfd58"></a> `00abfd58` | `c2 0e 00 f0` | adrp x2,0xc9a000 | `FALL_THROUGH`
<a id="insn-00abfd5c"></a> `00abfd5c` | `20 0f 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00abfd60"></a> `00abfd60` | `00 00 3c 91` | add x0,x0,#0xf00 | `FALL_THROUGH`
<a id="insn-00abfd64"></a> `00abfd64` | `42 50 46 f9` | ldr x2,[x2, #0xca0] | `FALL_THROUGH`
<a id="insn-00abfd68"></a> `00abfd68` | `e8 03 01 91` | add x8,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00abfd6c"></a> `00abfd6c` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00abfd70"></a> `00abfd70` | `83 02 80 52` | mov w3,#0x14 | `FALL_THROUGH`
<a id="insn-00abfd74"></a> `00abfd74` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00abfd78"></a> `00abfd78` | `e5 03 1f 2a` | mov w5,wzr | `FALL_THROUGH`
<a id="insn-00abfd7c"></a> `00abfd7c` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-00abfd80"></a> `00abfd80` | `d7 fa e6 97` | bl 0x0047e8dc | `UNCONDITIONAL_CALL`
<a id="insn-00abfd84"></a> `00abfd84` | `e0 13 c0 3d` | ldr q0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abfd88"></a> `00abfd88` | `95 3a 40 f9` | ldr x21,[x20, #0x70] | `FALL_THROUGH`
<a id="insn-00abfd8c"></a> `00abfd8c` | `ff 7f 04 a9` | stp xzr,xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abfd90"></a> `00abfd90` | `80 82 86 3c` | stur q0,[x20, #0x68] | `FALL_THROUGH`
<a id="insn-00abfd94"></a> `00abfd94` | `75 01 00 b4` | cbz x21,0x00abfdc0 | `CONDITIONAL_JUMP`
<a id="insn-00abfd98"></a> `00abfd98` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00abfd9c"></a> `00abfd9c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abfda0"></a> `00abfda0` | `d8 4f 06 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00abfda4"></a> `00abfda4` | `e0 00 00 b5` | cbnz x0,0x00abfdc0 | `CONDITIONAL_JUMP`
<a id="insn-00abfda8"></a> `00abfda8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00abfdac"></a> `00abfdac` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abfdb0"></a> `00abfdb0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abfdb4"></a> `00abfdb4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abfdb8"></a> `00abfdb8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abfdbc"></a> `00abfdbc` | `31 60 06 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00abfdc0"></a> `00abfdc0` | `f4 27 40 f9` | ldr x20,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00abfdc4"></a> `00abfdc4` | `b4 00 00 b4` | cbz x20,0x00abfdd8 | `CONDITIONAL_JUMP`
<a id="insn-00abfdc8"></a> `00abfdc8` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00abfdcc"></a> `00abfdcc` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abfdd0"></a> `00abfdd0` | `cc 4f 06 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00abfdd4"></a> `00abfdd4` | `a0 13 00 b4` | cbz x0,0x00ac0048 | `CONDITIONAL_JUMP`
<a id="insn-00abfdd8"></a> `00abfdd8` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abfddc"></a> `00abfddc` | `68 14 00 37` | tbnz w8,#0x0,0x00ac0068 | `CONDITIONAL_JUMP`
<a id="insn-00abfde0"></a> `00abfde0` | `a8 83 5c 38` | ldurb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00abfde4"></a> `00abfde4` | `a8 14 00 37` | tbnz w8,#0x0,0x00ac0078 | `CONDITIONAL_JUMP`
<a id="insn-00abfde8"></a> `00abfde8` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abfdec"></a> `00abfdec` | `68 00 00 36` | tbz w8,#0x0,0x00abfdf8 | `CONDITIONAL_JUMP`
<a id="insn-00abfdf0"></a> `00abfdf0` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abfdf4"></a> `00abfdf4` | `2f 60 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00abfdf8"></a> `00abfdf8` | `89 bf ff 90` | adrp x9,0x2af000 | `FALL_THROUGH`
<a id="insn-00abfdfc"></a> `00abfdfc` | `29 f9 3b 91` | add x9,x9,#0xefe | `FALL_THROUGH`
<a id="insn-00abfe00"></a> `00abfe00` | `2a cc 8d 52` | mov w10,#0x6e61 | `FALL_THROUGH`
<a id="insn-00abfe04"></a> `00abfe04` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00abfe08"></a> `00abfe08` | `c8 04 80 52` | mov w8,#0x26 | `FALL_THROUGH`
<a id="insn-00abfe0c"></a> `00abfe0c` | `2a ad ad 72` | movk w10,#0x6d69, LSL #16 | `FALL_THROUGH`
<a id="insn-00abfe10"></a> `00abfe10` | `a8 03 1e 38` | sturb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abfe14"></a> `00abfe14` | `aa 03 1f b8` | stur w10,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abfe18"></a> `00abfe18` | `a0 13 9e 3c` | stur q0,[x29, #-0x1f] | `FALL_THROUGH`
<a id="insn-00abfe1c"></a> `00abfe1c` | `bf 43 1f 38` | sturb wzr,[x29, #-0xc] | `FALL_THROUGH`
<a id="insn-00abfe20"></a> `00abfe20` | `60 42 05 91` | add x0,x19,#0x150 | `FALL_THROUGH`
<a id="insn-00abfe24"></a> `00abfe24` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00abfe28"></a> `00abfe28` | `d2 ba e6 97` | bl 0x0046e970 | `UNCONDITIONAL_CALL`
<a id="insn-00abfe2c"></a> `00abfe2c` | `5e 00 00 14` | b 0x00abffa4 | `UNCONDITIONAL_JUMP`
<a id="insn-00abfe30"></a> `00abfe30` | `28 ff df 08` | ldarb w8,[x25] | `FALL_THROUGH`
<a id="insn-00abfe34"></a> `00abfe34` | `28 1e 00 36` | tbz w8,#0x0,0x00ac01f8 | `CONDITIONAL_JUMP`
<a id="insn-00abfe38"></a> `00abfe38` | `09 bf ff d0` | adrp x9,0x2a1000 | `FALL_THROUGH`
<a id="insn-00abfe3c"></a> `00abfe3c` | `29 79 22 91` | add x9,x9,#0x89e | `FALL_THROUGH`
<a id="insn-00abfe40"></a> `00abfe40` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-00abfe44"></a> `00abfe44` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00abfe48"></a> `00abfe48` | `8a 2e 86 52` | mov w10,#0x3174 | `FALL_THROUGH`
<a id="insn-00abfe4c"></a> `00abfe4c` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abfe50"></a> `00abfe50` | `ea 93 02 78` | sturh w10,[sp, #0x29] | `FALL_THROUGH`
<a id="insn-00abfe54"></a> `00abfe54` | `e9 13 02 f8` | stur x9,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00abfe58"></a> `00abfe58` | `ff af 00 39` | strb wzr,[sp, #0x2b] | `FALL_THROUGH`
<a id="insn-00abfe5c"></a> `00abfe5c` | `a8 e3 00 d1` | sub x8,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00abfe60"></a> `00abfe60` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00abfe64"></a> `00abfe64` | `fc 33 e7 97` | bl 0x0048ce54 | `UNCONDITIONAL_CALL`
<a id="insn-00abfe68"></a> `00abfe68` | `68 a6 47 a9` | ldp x8,x9,[x19, #0x78] | `FALL_THROUGH`
<a id="insn-00abfe6c"></a> `00abfe6c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00abfe70"></a> `00abfe70` | `e0 1e 00 54` | b.eq 0x00ac024c | `CONDITIONAL_JUMP`
<a id="insn-00abfe74"></a> `00abfe74` | `69 2a 40 a9` | ldp x9,x10,[x19] | `FALL_THROUGH`
<a id="insn-00abfe78"></a> `00abfe78` | `08 01 80 b9` | ldrsw x8,[x8] | `FALL_THROUGH`
<a id="insn-00abfe7c"></a> `00abfe7c` | `4a 01 09 cb` | sub x10,x10,x9 | `FALL_THROUGH`
<a id="insn-00abfe80"></a> `00abfe80` | `1f 0d 8a eb` | cmp x8,x10, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00abfe84"></a> `00abfe84` | `02 1f 00 54` | b.cs 0x00ac0264 | `CONDITIONAL_JUMP`
<a id="insn-00abfe88"></a> `00abfe88` | `28 79 68 f8` | ldr x8,[x9, x8, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00abfe8c"></a> `00abfe8c` | `e9 03 08 aa` | mov x9,x8 | `FALL_THROUGH`
<a id="insn-00abfe90"></a> `00abfe90` | `2a 0d 48 38` | ldrb w10,[x9, #0x80]! | `FALL_THROUGH`
<a id="insn-00abfe94"></a> `00abfe94` | `ca 00 00 37` | tbnz w10,#0x0,0x00abfeac | `CONDITIONAL_JUMP`
<a id="insn-00abfe98"></a> `00abfe98` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00abfe9c"></a> `00abfe9c` | `28 09 40 f9` | ldr x8,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00abfea0"></a> `00abfea0` | `e0 03 80 3d` | str q0,[sp] | `FALL_THROUGH`
<a id="insn-00abfea4"></a> `00abfea4` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abfea8"></a> `00abfea8` | `04 00 00 14` | b 0x00abfeb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00abfeac"></a> `00abfeac` | `02 85 48 a9` | ldp x2,x1,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00abfeb0"></a> `00abfeb0` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00abfeb4"></a> `00abfeb4` | `1b ef e5 97` | bl 0x0043bb20 | `UNCONDITIONAL_CALL`
<a id="insn-00abfeb8"></a> `00abfeb8` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00abfebc"></a> `00abfebc` | `a0 e3 00 d1` | sub x0,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00abfec0"></a> `00abfec0` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00abfec4"></a> `00abfec4` | `d1 4b e7 97` | bl 0x00492e08 | `UNCONDITIONAL_CALL`
<a id="insn-00abfec8"></a> `00abfec8` | `c2 0e 00 f0` | adrp x2,0xc9a000 | `FALL_THROUGH`
<a id="insn-00abfecc"></a> `00abfecc` | `20 0f 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00abfed0"></a> `00abfed0` | `00 00 3c 91` | add x0,x0,#0xf00 | `FALL_THROUGH`
<a id="insn-00abfed4"></a> `00abfed4` | `42 50 46 f9` | ldr x2,[x2, #0xca0] | `FALL_THROUGH`
<a id="insn-00abfed8"></a> `00abfed8` | `e8 03 01 91` | add x8,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00abfedc"></a> `00abfedc` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00abfee0"></a> `00abfee0` | `83 02 80 52` | mov w3,#0x14 | `FALL_THROUGH`
<a id="insn-00abfee4"></a> `00abfee4` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00abfee8"></a> `00abfee8` | `e5 03 1f 2a` | mov w5,wzr | `FALL_THROUGH`
<a id="insn-00abfeec"></a> `00abfeec` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-00abfef0"></a> `00abfef0` | `7b fa e6 97` | bl 0x0047e8dc | `UNCONDITIONAL_CALL`
<a id="insn-00abfef4"></a> `00abfef4` | `e0 13 c0 3d` | ldr q0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abfef8"></a> `00abfef8` | `95 3a 40 f9` | ldr x21,[x20, #0x70] | `FALL_THROUGH`
<a id="insn-00abfefc"></a> `00abfefc` | `ff 7f 04 a9` | stp xzr,xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abff00"></a> `00abff00` | `80 82 86 3c` | stur q0,[x20, #0x68] | `FALL_THROUGH`
<a id="insn-00abff04"></a> `00abff04` | `75 01 00 b4` | cbz x21,0x00abff30 | `CONDITIONAL_JUMP`
<a id="insn-00abff08"></a> `00abff08` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00abff0c"></a> `00abff0c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abff10"></a> `00abff10` | `7c 4f 06 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00abff14"></a> `00abff14` | `e0 00 00 b5` | cbnz x0,0x00abff30 | `CONDITIONAL_JUMP`
<a id="insn-00abff18"></a> `00abff18` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00abff1c"></a> `00abff1c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abff20"></a> `00abff20` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abff24"></a> `00abff24` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abff28"></a> `00abff28` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abff2c"></a> `00abff2c` | `d5 5f 06 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00abff30"></a> `00abff30` | `f4 27 40 f9` | ldr x20,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00abff34"></a> `00abff34` | `b4 00 00 b4` | cbz x20,0x00abff48 | `CONDITIONAL_JUMP`
<a id="insn-00abff38"></a> `00abff38` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00abff3c"></a> `00abff3c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00abff40"></a> `00abff40` | `70 4f 06 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00abff44"></a> `00abff44` | `40 0a 00 b4` | cbz x0,0x00ac008c | `CONDITIONAL_JUMP`
<a id="insn-00abff48"></a> `00abff48` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abff4c"></a> `00abff4c` | `08 0b 00 37` | tbnz w8,#0x0,0x00ac00ac | `CONDITIONAL_JUMP`
<a id="insn-00abff50"></a> `00abff50` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00abff54"></a> `00abff54` | `48 0b 00 37` | tbnz w8,#0x0,0x00ac00bc | `CONDITIONAL_JUMP`
<a id="insn-00abff58"></a> `00abff58` | `a8 83 5c 38` | ldurb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00abff5c"></a> `00abff5c` | `88 0b 00 37` | tbnz w8,#0x0,0x00ac00cc | `CONDITIONAL_JUMP`
<a id="insn-00abff60"></a> `00abff60` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abff64"></a> `00abff64` | `68 00 00 36` | tbz w8,#0x0,0x00abff70 | `CONDITIONAL_JUMP`
<a id="insn-00abff68"></a> `00abff68` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abff6c"></a> `00abff6c` | `d1 5f 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00abff70"></a> `00abff70` | `c9 bf ff 90` | adrp x9,0x2b7000 | `FALL_THROUGH`
<a id="insn-00abff74"></a> `00abff74` | `29 f5 2e 91` | add x9,x9,#0xbbd | `FALL_THROUGH`
<a id="insn-00abff78"></a> `00abff78` | `2a cc 8d 52` | mov w10,#0x6e61 | `FALL_THROUGH`
<a id="insn-00abff7c"></a> `00abff7c` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00abff80"></a> `00abff80` | `c8 04 80 52` | mov w8,#0x26 | `FALL_THROUGH`
<a id="insn-00abff84"></a> `00abff84` | `2a ad ad 72` | movk w10,#0x6d69, LSL #16 | `FALL_THROUGH`
<a id="insn-00abff88"></a> `00abff88` | `a8 03 1e 38` | sturb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abff8c"></a> `00abff8c` | `aa 03 1f b8` | stur w10,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abff90"></a> `00abff90` | `a0 13 9e 3c` | stur q0,[x29, #-0x1f] | `FALL_THROUGH`
<a id="insn-00abff94"></a> `00abff94` | `bf 43 1f 38` | sturb wzr,[x29, #-0xc] | `FALL_THROUGH`
<a id="insn-00abff98"></a> `00abff98` | `60 42 05 91` | add x0,x19,#0x150 | `FALL_THROUGH`
<a id="insn-00abff9c"></a> `00abff9c` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00abffa0"></a> `00abffa0` | `74 ba e6 97` | bl 0x0046e970 | `UNCONDITIONAL_CALL`
<a id="insn-00abffa4"></a> `00abffa4` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abffa8"></a> `00abffa8` | `68 00 00 36` | tbz w8,#0x0,0x00abffb4 | `CONDITIONAL_JUMP`
<a id="insn-00abffac"></a> `00abffac` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abffb0"></a> `00abffb0` | `c0 5f 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00abffb4"></a> `00abffb4` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00abffb8"></a> `00abffb8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abffbc"></a> `00abffbc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abffc0"></a> `00abffc0` | `01 1f 00 54` | b.ne 0x00ac03a0 | `CONDITIONAL_JUMP`
<a id="insn-00abffc4"></a> `00abffc4` | `f4 4f 4d a9` | ldp x20,x19,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00abffc8"></a> `00abffc8` | `f9 53 40 f9` | ldr x25,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00abffcc"></a> `00abffcc` | `f6 57 4c a9` | ldp x22,x21,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00abffd0"></a> `00abffd0` | `f8 5f 4b a9` | ldp x24,x23,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00abffd4"></a> `00abffd4` | `fd 7b 49 a9` | ldp x29,x30,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abffd8"></a> `00abffd8` | `ff 83 03 91` | add sp,sp,#0xe0 | `FALL_THROUGH`
<a id="insn-00abffdc"></a> `00abffdc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00abffe0"></a> `00abffe0` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00abffe4"></a> `00abffe4` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00abffe8"></a> `00abffe8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abffec"></a> `00abffec` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00abfff0"></a> `00abfff0` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00abfff4"></a> `00abfff4` | `a3 5f 06 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00abfff8"></a> `00abfff8` | `f7 27 40 f9` | ldr x23,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00abfffc"></a> `00abfffc` | `57 e6 ff b5` | cbnz x23,0x00abfcc4 | `CONDITIONAL_JUMP`
<a id="insn-00ac0000"></a> `00ac0000` | `35 ff ff 17` | b 0x00abfcd4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ac0004"></a> `00ac0004` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00ac0008"></a> `00ac0008` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00ac000c"></a> `00ac000c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ac0010"></a> `00ac0010` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac0014"></a> `00ac0014` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00ac0018"></a> `00ac0018` | `9a 5f 06 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00ac001c"></a> `00ac001c` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ac0020"></a> `00ac0020` | `e8 e5 07 36` | tbz w8,#0x0,0x00abfcdc | `CONDITIONAL_JUMP`
<a id="insn-00ac0024"></a> `00ac0024` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ac0028"></a> `00ac0028` | `a2 5f 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac002c"></a> `00ac002c` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00ac0030"></a> `00ac0030` | `a8 e5 07 36` | tbz w8,#0x0,0x00abfce4 | `CONDITIONAL_JUMP`
<a id="insn-00ac0034"></a> `00ac0034` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00ac0038"></a> `00ac0038` | `9e 5f 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac003c"></a> `00ac003c` | `a8 83 5c 38` | ldurb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00ac0040"></a> `00ac0040` | `68 e5 07 37` | tbnz w8,#0x0,0x00abfcec | `CONDITIONAL_JUMP`
<a id="insn-00ac0044"></a> `00ac0044` | `2c ff ff 17` | b 0x00abfcf4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ac0048"></a> `00ac0048` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00ac004c"></a> `00ac004c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac0050"></a> `00ac0050` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ac0054"></a> `00ac0054` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac0058"></a> `00ac0058` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac005c"></a> `00ac005c` | `89 5f 06 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00ac0060"></a> `00ac0060` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00ac0064"></a> `00ac0064` | `e8 eb 07 36` | tbz w8,#0x0,0x00abfde0 | `CONDITIONAL_JUMP`
<a id="insn-00ac0068"></a> `00ac0068` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00ac006c"></a> `00ac006c` | `91 5f 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac0070"></a> `00ac0070` | `a8 83 5c 38` | ldurb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00ac0074"></a> `00ac0074` | `a8 eb 07 36` | tbz w8,#0x0,0x00abfde8 | `CONDITIONAL_JUMP`
<a id="insn-00ac0078"></a> `00ac0078` | `a0 83 5d f8` | ldur x0,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00ac007c"></a> `00ac007c` | `8d 5f 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac0080"></a> `00ac0080` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ac0084"></a> `00ac0084` | `68 eb 07 37` | tbnz w8,#0x0,0x00abfdf0 | `CONDITIONAL_JUMP`
<a id="insn-00ac0088"></a> `00ac0088` | `5c ff ff 17` | b 0x00abfdf8 | `UNCONDITIONAL_JUMP`
<a id="insn-00ac008c"></a> `00ac008c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00ac0090"></a> `00ac0090` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac0094"></a> `00ac0094` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ac0098"></a> `00ac0098` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac009c"></a> `00ac009c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac00a0"></a> `00ac00a0` | `78 5f 06 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00ac00a4"></a> `00ac00a4` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00ac00a8"></a> `00ac00a8` | `48 f5 07 36` | tbz w8,#0x0,0x00abff50 | `CONDITIONAL_JUMP`
<a id="insn-00ac00ac"></a> `00ac00ac` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00ac00b0"></a> `00ac00b0` | `80 5f 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac00b4"></a> `00ac00b4` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00ac00b8"></a> `00ac00b8` | `08 f5 07 36` | tbz w8,#0x0,0x00abff58 | `CONDITIONAL_JUMP`
<a id="insn-00ac00bc"></a> `00ac00bc` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ac00c0"></a> `00ac00c0` | `7c 5f 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac00c4"></a> `00ac00c4` | `a8 83 5c 38` | ldurb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00ac00c8"></a> `00ac00c8` | `c8 f4 07 36` | tbz w8,#0x0,0x00abff60 | `CONDITIONAL_JUMP`
<a id="insn-00ac00cc"></a> `00ac00cc` | `a0 83 5d f8` | ldur x0,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00ac00d0"></a> `00ac00d0` | `78 5f 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac00d4"></a> `00ac00d4` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ac00d8"></a> `00ac00d8` | `88 f4 07 37` | tbnz w8,#0x0,0x00abff68 | `CONDITIONAL_JUMP`
<a id="insn-00ac00dc"></a> `00ac00dc` | `a5 ff ff 17` | b 0x00abff70 | `UNCONDITIONAL_JUMP`
<a id="insn-00ac00e0"></a> `00ac00e0` | `20 0f 00 90` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00ac00e4"></a> `00ac00e4` | `00 e0 3c 91` | add x0,x0,#0xf38 | `FALL_THROUGH`
<a id="insn-00ac00e8"></a> `00ac00e8` | `5a 5f 06 94` | bl 0x00c57e50 | `UNCONDITIONAL_CALL`
<a id="insn-00ac00ec"></a> `00ac00ec` | `40 d0 ff 34` | cbz w0,0x00abfaf4 | `CONDITIONAL_JUMP`
<a id="insn-00ac00f0"></a> `00ac00f0` | `21 0f 00 90` | adrp x1,0xca4000 | `FALL_THROUGH`
<a id="insn-00ac00f4"></a> `00ac00f4` | `21 00 3c 91` | add x1,x1,#0xf00 | `FALL_THROUGH`
<a id="insn-00ac00f8"></a> `00ac00f8` | `e0 cd ff d0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-00ac00fc"></a> `00ac00fc` | `00 d0 36 91` | add x0,x0,#0xdb4 | `FALL_THROUGH`
<a id="insn-00ac0100"></a> `00ac0100` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00ac0104"></a> `00ac0104` | `02 0d 00 d0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-00ac0108"></a> `00ac0108` | `42 40 3e 91` | add x2,x2,#0xf90 | `FALL_THROUGH`
<a id="insn-00ac010c"></a> `00ac010c` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00ac0110"></a> `00ac0110` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00ac0114"></a> `00ac0114` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00ac0118"></a> `00ac0118` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00ac011c"></a> `00ac011c` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00ac0120"></a> `00ac0120` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00ac0124"></a> `00ac0124` | `43 5f 06 94` | bl 0x00c57e30 | `UNCONDITIONAL_CALL`
<a id="insn-00ac0128"></a> `00ac0128` | `20 0f 00 90` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00ac012c"></a> `00ac012c` | `00 e0 3c 91` | add x0,x0,#0xf38 | `FALL_THROUGH`
<a id="insn-00ac0130"></a> `00ac0130` | `50 5f 06 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00ac0134"></a> `00ac0134` | `70 fe ff 17` | b 0x00abfaf4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ac0138"></a> `00ac0138` | `20 0f 00 90` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00ac013c"></a> `00ac013c` | `00 e0 3c 91` | add x0,x0,#0xf38 | `FALL_THROUGH`
<a id="insn-00ac0140"></a> `00ac0140` | `44 5f 06 94` | bl 0x00c57e50 | `UNCONDITIONAL_CALL`
<a id="insn-00ac0144"></a> `00ac0144` | `80 d6 ff 34` | cbz w0,0x00abfc14 | `CONDITIONAL_JUMP`
<a id="insn-00ac0148"></a> `00ac0148` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00ac014c"></a> `00ac014c` | `e0 cd ff d0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-00ac0150"></a> `00ac0150` | `00 d0 36 91` | add x0,x0,#0xdb4 | `FALL_THROUGH`
<a id="insn-00ac0154"></a> `00ac0154` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00ac0158"></a> `00ac0158` | `02 0d 00 d0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-00ac015c"></a> `00ac015c` | `42 40 3e 91` | add x2,x2,#0xf90 | `FALL_THROUGH`
<a id="insn-00ac0160"></a> `00ac0160` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00ac0164"></a> `00ac0164` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00ac0168"></a> `00ac0168` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ac016c"></a> `00ac016c` | `bf fe 02 a9` | stp xzr,xzr,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00ac0170"></a> `00ac0170` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00ac0174"></a> `00ac0174` | `bf 22 01 a9` | stp xzr,x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00ac0178"></a> `00ac0178` | `2e 5f 06 94` | bl 0x00c57e30 | `UNCONDITIONAL_CALL`
<a id="insn-00ac017c"></a> `00ac017c` | `20 0f 00 90` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00ac0180"></a> `00ac0180` | `00 e0 3c 91` | add x0,x0,#0xf38 | `FALL_THROUGH`
<a id="insn-00ac0184"></a> `00ac0184` | `3b 5f 06 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00ac0188"></a> `00ac0188` | `a3 fe ff 17` | b 0x00abfc14 | `UNCONDITIONAL_JUMP`
<a id="insn-00ac018c"></a> `00ac018c` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00ac0190"></a> `00ac0190` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ac0194"></a> `00ac0194` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ac0198"></a> `00ac0198` | `41 10 00 54` | b.ne 0x00ac03a0 | `CONDITIONAL_JUMP`
<a id="insn-00ac019c"></a> `00ac019c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ac01a0"></a> `00ac01a0` | `94 7c e7 97` | bl 0x0049f3f0 | `CALL_TERMINATOR`
<a id="insn-00ac01a4"></a> `00ac01a4` | `20 0f 00 90` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00ac01a8"></a> `00ac01a8` | `00 e0 3c 91` | add x0,x0,#0xf38 | `FALL_THROUGH`
<a id="insn-00ac01ac"></a> `00ac01ac` | `29 5f 06 94` | bl 0x00c57e50 | `UNCONDITIONAL_CALL`
<a id="insn-00ac01b0"></a> `00ac01b0` | `e0 da ff 34` | cbz w0,0x00abfd0c | `CONDITIONAL_JUMP`
<a id="insn-00ac01b4"></a> `00ac01b4` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00ac01b8"></a> `00ac01b8` | `e0 cd ff d0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-00ac01bc"></a> `00ac01bc` | `00 d0 36 91` | add x0,x0,#0xdb4 | `FALL_THROUGH`
<a id="insn-00ac01c0"></a> `00ac01c0` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00ac01c4"></a> `00ac01c4` | `02 0d 00 d0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-00ac01c8"></a> `00ac01c8` | `42 40 3e 91` | add x2,x2,#0xf90 | `FALL_THROUGH`
<a id="insn-00ac01cc"></a> `00ac01cc` | `c8 02 00 f9` | str x8,[x22] | `FALL_THROUGH`
<a id="insn-00ac01d0"></a> `00ac01d0` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00ac01d4"></a> `00ac01d4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00ac01d8"></a> `00ac01d8` | `df fe 02 a9` | stp xzr,xzr,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00ac01dc"></a> `00ac01dc` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00ac01e0"></a> `00ac01e0` | `df 22 01 a9` | stp xzr,x8,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00ac01e4"></a> `00ac01e4` | `13 5f 06 94` | bl 0x00c57e30 | `UNCONDITIONAL_CALL`
<a id="insn-00ac01e8"></a> `00ac01e8` | `20 0f 00 90` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00ac01ec"></a> `00ac01ec` | `00 e0 3c 91` | add x0,x0,#0xf38 | `FALL_THROUGH`
<a id="insn-00ac01f0"></a> `00ac01f0` | `20 5f 06 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00ac01f4"></a> `00ac01f4` | `c6 fe ff 17` | b 0x00abfd0c | `UNCONDITIONAL_JUMP`
<a id="insn-00ac01f8"></a> `00ac01f8` | `20 0f 00 90` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00ac01fc"></a> `00ac01fc` | `00 e0 3c 91` | add x0,x0,#0xf38 | `FALL_THROUGH`
<a id="insn-00ac0200"></a> `00ac0200` | `14 5f 06 94` | bl 0x00c57e50 | `UNCONDITIONAL_CALL`
<a id="insn-00ac0204"></a> `00ac0204` | `a0 e1 ff 34` | cbz w0,0x00abfe38 | `CONDITIONAL_JUMP`
<a id="insn-00ac0208"></a> `00ac0208` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00ac020c"></a> `00ac020c` | `e0 cd ff d0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-00ac0210"></a> `00ac0210` | `00 d0 36 91` | add x0,x0,#0xdb4 | `FALL_THROUGH`
<a id="insn-00ac0214"></a> `00ac0214` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00ac0218"></a> `00ac0218` | `02 0d 00 d0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-00ac021c"></a> `00ac021c` | `42 40 3e 91` | add x2,x2,#0xf90 | `FALL_THROUGH`
<a id="insn-00ac0220"></a> `00ac0220` | `c8 02 00 f9` | str x8,[x22] | `FALL_THROUGH`
<a id="insn-00ac0224"></a> `00ac0224` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00ac0228"></a> `00ac0228` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00ac022c"></a> `00ac022c` | `df fe 02 a9` | stp xzr,xzr,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00ac0230"></a> `00ac0230` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00ac0234"></a> `00ac0234` | `df 22 01 a9` | stp xzr,x8,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00ac0238"></a> `00ac0238` | `fe 5e 06 94` | bl 0x00c57e30 | `UNCONDITIONAL_CALL`
<a id="insn-00ac023c"></a> `00ac023c` | `20 0f 00 90` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00ac0240"></a> `00ac0240` | `00 e0 3c 91` | add x0,x0,#0xf38 | `FALL_THROUGH`
<a id="insn-00ac0244"></a> `00ac0244` | `0b 5f 06 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00ac0248"></a> `00ac0248` | `fc fe ff 17` | b 0x00abfe38 | `UNCONDITIONAL_JUMP`
<a id="insn-00ac024c"></a> `00ac024c` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00ac0250"></a> `00ac0250` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ac0254"></a> `00ac0254` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ac0258"></a> `00ac0258` | `41 0a 00 54` | b.ne 0x00ac03a0 | `CONDITIONAL_JUMP`
<a id="insn-00ac025c"></a> `00ac025c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ac0260"></a> `00ac0260` | `64 7c e7 97` | bl 0x0049f3f0 | `CALL_TERMINATOR`
<a id="insn-00ac0264"></a> `00ac0264` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00ac0268"></a> `00ac0268` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ac026c"></a> `00ac026c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ac0270"></a> `00ac0270` | `81 09 00 54` | b.ne 0x00ac03a0 | `CONDITIONAL_JUMP`
<a id="insn-00ac0274"></a> `00ac0274` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ac0278"></a> `00ac0278` | `5b 03 00 94` | bl 0x00ac0fe4 | `UNCONDITIONAL_CALL`
<a id="insn-00ac027c"></a> `00ac027c` | `0c 00 00 14` | b 0x00ac02ac | `UNCONDITIONAL_JUMP`
<a id="insn-00ac02ac"></a> `00ac02ac` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00ac02b0"></a> `00ac02b0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ac02b4"></a> `00ac02b4` | `a8 04 00 37` | tbnz w8,#0x0,0x00ac0348 | `CONDITIONAL_JUMP`
<a id="insn-00ac02b8"></a> `00ac02b8` | `34 00 00 14` | b 0x00ac0388 | `UNCONDITIONAL_JUMP`
<a id="insn-00ac0348"></a> `00ac0348` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00ac034c"></a> `00ac034c` | `0e 00 00 14` | b 0x00ac0384 | `UNCONDITIONAL_JUMP`
<a id="insn-00ac0384"></a> `00ac0384` | `cb 5e 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac0388"></a> `00ac0388` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00ac038c"></a> `00ac038c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ac0390"></a> `00ac0390` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ac0394"></a> `00ac0394` | `61 00 00 54` | b.ne 0x00ac03a0 | `CONDITIONAL_JUMP`
<a id="insn-00ac0398"></a> `00ac0398` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ac039c"></a> `00ac039c` | `f0 4e 06 94` | bl 0x00c53f5c | `CALL_TERMINATOR`
<a id="insn-00ac03a0"></a> `00ac03a0` | `d0 5e 06 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00abfaa8`](#insn-00abfaa8) 範囲 `[['00abfaa8', '00abfadb']]`
  - `CONDITIONAL_JUMP` [`00abfad8`](#insn-00abfad8) → [`00abffb4`](#insn-00abffb4)
  - `FALL_THROUGH` [`00abfad8`](#insn-00abfad8) → [`00abfadc`](#insn-00abfadc)
- ブロック [`00abfadc`](#insn-00abfadc) 範囲 `[['00abfadc', '00abfaf3']]`
  - `CONDITIONAL_JUMP` [`00abfaf0`](#insn-00abfaf0) → [`00ac00e0`](#insn-00ac00e0)
  - `FALL_THROUGH` [`00abfaf0`](#insn-00abfaf0) → [`00abfaf4`](#insn-00abfaf4)
- ブロック [`00abfaf4`](#insn-00abfaf4) 範囲 `[['00abfaf4', '00abfaf7']]`
  - `FALL_THROUGH` [`00abfaf4`](#insn-00abfaf4) → [`00abfaf8`](#insn-00abfaf8)
- ブロック [`00abfaf8`](#insn-00abfaf8) 範囲 `[['00abfaf8', '00abfb27']]`
  - `FALL_THROUGH` [`00abfb24`](#insn-00abfb24) → [`00abfb28`](#insn-00abfb28)
- ブロック [`00abfb28`](#insn-00abfb28) 範囲 `[['00abfb28', '00abfb33']]`
  - `FALL_THROUGH` [`00abfb30`](#insn-00abfb30) → [`00abfb34`](#insn-00abfb34)
- ブロック [`00abfb34`](#insn-00abfb34) 範囲 `[['00abfb34', '00abfb6b']]`
  - `CONDITIONAL_JUMP` [`00abfb68`](#insn-00abfb68) → [`00abfb7c`](#insn-00abfb7c)
  - `FALL_THROUGH` [`00abfb68`](#insn-00abfb68) → [`00abfb6c`](#insn-00abfb6c)
- ブロック [`00abfb6c`](#insn-00abfb6c) 範囲 `[['00abfb6c', '00abfb7b']]`
  - `CONDITIONAL_JUMP` [`00abfb78`](#insn-00abfb78) → [`00abfbb0`](#insn-00abfbb0)
  - `FALL_THROUGH` [`00abfb78`](#insn-00abfb78) → [`00abfb7c`](#insn-00abfb7c)
- ブロック [`00abfb7c`](#insn-00abfb7c) 範囲 `[['00abfb7c', '00abfb83']]`
  - `CONDITIONAL_JUMP` [`00abfb80`](#insn-00abfb80) → [`00abfb94`](#insn-00abfb94)
  - `FALL_THROUGH` [`00abfb80`](#insn-00abfb80) → [`00abfb84`](#insn-00abfb84)
- ブロック [`00abfb84`](#insn-00abfb84) 範囲 `[['00abfb84', '00abfb93']]`
  - `CONDITIONAL_JUMP` [`00abfb90`](#insn-00abfb90) → [`00abfbd4`](#insn-00abfbd4)
  - `FALL_THROUGH` [`00abfb90`](#insn-00abfb90) → [`00abfb94`](#insn-00abfb94)
- ブロック [`00abfb94`](#insn-00abfb94) 範囲 `[['00abfb94', '00abfb9b']]`
  - `CONDITIONAL_JUMP` [`00abfb98`](#insn-00abfb98) → [`00abfbf4`](#insn-00abfbf4)
  - `FALL_THROUGH` [`00abfb98`](#insn-00abfb98) → [`00abfb9c`](#insn-00abfb9c)
- ブロック [`00abfb9c`](#insn-00abfb9c) 範囲 `[['00abfb9c', '00abfb9f']]`
  - `FALL_THROUGH` [`00abfb9c`](#insn-00abfb9c) → [`00abfba0`](#insn-00abfba0)
- ブロック [`00abfba0`](#insn-00abfba0) 範囲 `[['00abfba0', '00abfba3']]`
  - `CONDITIONAL_JUMP` [`00abfba0`](#insn-00abfba0) → [`00abfc04`](#insn-00abfc04)
  - `FALL_THROUGH` [`00abfba0`](#insn-00abfba0) → [`00abfba4`](#insn-00abfba4)
- ブロック [`00abfba4`](#insn-00abfba4) 範囲 `[['00abfba4', '00abfbab']]`
  - `CONDITIONAL_JUMP` [`00abfba8`](#insn-00abfba8) → [`00abfc14`](#insn-00abfc14)
  - `FALL_THROUGH` [`00abfba8`](#insn-00abfba8) → [`00abfbac`](#insn-00abfbac)
- ブロック [`00abfbac`](#insn-00abfbac) 範囲 `[['00abfbac', '00abfbaf']]`
  - `UNCONDITIONAL_JUMP` [`00abfbac`](#insn-00abfbac) → [`00ac0138`](#insn-00ac0138)
- ブロック [`00abfbb0`](#insn-00abfbb0) 範囲 `[['00abfbb0', '00abfbcf']]`
  - `CONDITIONAL_JUMP` [`00abfbcc`](#insn-00abfbcc) → [`00abfb84`](#insn-00abfb84)
  - `FALL_THROUGH` [`00abfbcc`](#insn-00abfbcc) → [`00abfbd0`](#insn-00abfbd0)
- ブロック [`00abfbd0`](#insn-00abfbd0) 範囲 `[['00abfbd0', '00abfbd3']]`
  - `UNCONDITIONAL_JUMP` [`00abfbd0`](#insn-00abfbd0) → [`00abfb94`](#insn-00abfb94)
- ブロック [`00abfbd4`](#insn-00abfbd4) 範囲 `[['00abfbd4', '00abfbdb']]`
  - `FALL_THROUGH` [`00abfbd8`](#insn-00abfbd8) → [`00abfbdc`](#insn-00abfbdc)
- ブロック [`00abfbdc`](#insn-00abfbdc) 範囲 `[['00abfbdc', '00abfbf3']]`
  - `CONDITIONAL_JUMP` [`00abfbf0`](#insn-00abfbf0) → [`00abfb9c`](#insn-00abfb9c)
  - `FALL_THROUGH` [`00abfbf0`](#insn-00abfbf0) → [`00abfbf4`](#insn-00abfbf4)
- ブロック [`00abfbf4`](#insn-00abfbf4) 範囲 `[['00abfbf4', '00abfc03']]`
  - `CONDITIONAL_JUMP` [`00abfc00`](#insn-00abfc00) → [`00abfba4`](#insn-00abfba4)
  - `FALL_THROUGH` [`00abfc00`](#insn-00abfc00) → [`00abfc04`](#insn-00abfc04)
- ブロック [`00abfc04`](#insn-00abfc04) 範囲 `[['00abfc04', '00abfc13']]`
  - `CONDITIONAL_JUMP` [`00abfc10`](#insn-00abfc10) → [`00ac0138`](#insn-00ac0138)
  - `FALL_THROUGH` [`00abfc10`](#insn-00abfc10) → [`00abfc14`](#insn-00abfc14)
- ブロック [`00abfc14`](#insn-00abfc14) 範囲 `[['00abfc14', '00abfc1b']]`
  - `FALL_THROUGH` [`00abfc18`](#insn-00abfc18) → [`00abfc1c`](#insn-00abfc1c)
- ブロック [`00abfc1c`](#insn-00abfc1c) 範囲 `[['00abfc1c', '00abfc47']]`
  - `CONDITIONAL_JUMP` [`00abfc44`](#insn-00abfc44) → [`00ac018c`](#insn-00ac018c)
  - `FALL_THROUGH` [`00abfc44`](#insn-00abfc44) → [`00abfc48`](#insn-00abfc48)
- ブロック [`00abfc48`](#insn-00abfc48) 範囲 `[['00abfc48', '00abfca3']]`
  - `FALL_THROUGH` [`00abfca0`](#insn-00abfca0) → [`00abfca4`](#insn-00abfca4)
- ブロック [`00abfca4`](#insn-00abfca4) 範囲 `[['00abfca4', '00abfcab']]`
  - `CONDITIONAL_JUMP` [`00abfca8`](#insn-00abfca8) → [`00abfcbc`](#insn-00abfcbc)
  - `FALL_THROUGH` [`00abfca8`](#insn-00abfca8) → [`00abfcac`](#insn-00abfcac)
- ブロック [`00abfcac`](#insn-00abfcac) 範囲 `[['00abfcac', '00abfcbb']]`
  - `CONDITIONAL_JUMP` [`00abfcb8`](#insn-00abfcb8) → [`00abffe0`](#insn-00abffe0)
  - `FALL_THROUGH` [`00abfcb8`](#insn-00abfcb8) → [`00abfcbc`](#insn-00abfcbc)
- ブロック [`00abfcbc`](#insn-00abfcbc) 範囲 `[['00abfcbc', '00abfcc3']]`
  - `CONDITIONAL_JUMP` [`00abfcc0`](#insn-00abfcc0) → [`00abfcd4`](#insn-00abfcd4)
  - `FALL_THROUGH` [`00abfcc0`](#insn-00abfcc0) → [`00abfcc4`](#insn-00abfcc4)
- ブロック [`00abfcc4`](#insn-00abfcc4) 範囲 `[['00abfcc4', '00abfcd3']]`
  - `CONDITIONAL_JUMP` [`00abfcd0`](#insn-00abfcd0) → [`00ac0004`](#insn-00ac0004)
  - `FALL_THROUGH` [`00abfcd0`](#insn-00abfcd0) → [`00abfcd4`](#insn-00abfcd4)
- ブロック [`00abfcd4`](#insn-00abfcd4) 範囲 `[['00abfcd4', '00abfcdb']]`
  - `CONDITIONAL_JUMP` [`00abfcd8`](#insn-00abfcd8) → [`00ac0024`](#insn-00ac0024)
  - `FALL_THROUGH` [`00abfcd8`](#insn-00abfcd8) → [`00abfcdc`](#insn-00abfcdc)
- ブロック [`00abfcdc`](#insn-00abfcdc) 範囲 `[['00abfcdc', '00abfce3']]`
  - `CONDITIONAL_JUMP` [`00abfce0`](#insn-00abfce0) → [`00ac0034`](#insn-00ac0034)
  - `FALL_THROUGH` [`00abfce0`](#insn-00abfce0) → [`00abfce4`](#insn-00abfce4)
- ブロック [`00abfce4`](#insn-00abfce4) 範囲 `[['00abfce4', '00abfceb']]`
  - `CONDITIONAL_JUMP` [`00abfce8`](#insn-00abfce8) → [`00abfcf4`](#insn-00abfcf4)
  - `FALL_THROUGH` [`00abfce8`](#insn-00abfce8) → [`00abfcec`](#insn-00abfcec)
- ブロック [`00abfcec`](#insn-00abfcec) 範囲 `[['00abfcec', '00abfcf3']]`
  - `FALL_THROUGH` [`00abfcf0`](#insn-00abfcf0) → [`00abfcf4`](#insn-00abfcf4)
- ブロック [`00abfcf4`](#insn-00abfcf4) 範囲 `[['00abfcf4', '00abfd03']]`
  - `CONDITIONAL_JUMP` [`00abfd00`](#insn-00abfd00) → [`00abfe30`](#insn-00abfe30)
  - `FALL_THROUGH` [`00abfd00`](#insn-00abfd00) → [`00abfd04`](#insn-00abfd04)
- ブロック [`00abfd04`](#insn-00abfd04) 範囲 `[['00abfd04', '00abfd0b']]`
  - `CONDITIONAL_JUMP` [`00abfd08`](#insn-00abfd08) → [`00ac01a4`](#insn-00ac01a4)
  - `FALL_THROUGH` [`00abfd08`](#insn-00abfd08) → [`00abfd0c`](#insn-00abfd0c)
- ブロック [`00abfd0c`](#insn-00abfd0c) 範囲 `[['00abfd0c', '00abfd23']]`
  - `FALL_THROUGH` [`00abfd20`](#insn-00abfd20) → [`00abfd24`](#insn-00abfd24)
- ブロック [`00abfd24`](#insn-00abfd24) 範囲 `[['00abfd24', '00abfd2b']]`
  - `FALL_THROUGH` [`00abfd28`](#insn-00abfd28) → [`00abfd2c`](#insn-00abfd2c)
- ブロック [`00abfd2c`](#insn-00abfd2c) 範囲 `[['00abfd2c', '00abfd53']]`
  - `FALL_THROUGH` [`00abfd50`](#insn-00abfd50) → [`00abfd54`](#insn-00abfd54)
- ブロック [`00abfd54`](#insn-00abfd54) 範囲 `[['00abfd54', '00abfd83']]`
  - `FALL_THROUGH` [`00abfd80`](#insn-00abfd80) → [`00abfd84`](#insn-00abfd84)
- ブロック [`00abfd84`](#insn-00abfd84) 範囲 `[['00abfd84', '00abfd97']]`
  - `CONDITIONAL_JUMP` [`00abfd94`](#insn-00abfd94) → [`00abfdc0`](#insn-00abfdc0)
  - `FALL_THROUGH` [`00abfd94`](#insn-00abfd94) → [`00abfd98`](#insn-00abfd98)
- ブロック [`00abfd98`](#insn-00abfd98) 範囲 `[['00abfd98', '00abfda7']]`
  - `CONDITIONAL_JUMP` [`00abfda4`](#insn-00abfda4) → [`00abfdc0`](#insn-00abfdc0)
  - `FALL_THROUGH` [`00abfda4`](#insn-00abfda4) → [`00abfda8`](#insn-00abfda8)
- ブロック [`00abfda8`](#insn-00abfda8) 範囲 `[['00abfda8', '00abfdbf']]`
  - `FALL_THROUGH` [`00abfdbc`](#insn-00abfdbc) → [`00abfdc0`](#insn-00abfdc0)
- ブロック [`00abfdc0`](#insn-00abfdc0) 範囲 `[['00abfdc0', '00abfdc7']]`
  - `CONDITIONAL_JUMP` [`00abfdc4`](#insn-00abfdc4) → [`00abfdd8`](#insn-00abfdd8)
  - `FALL_THROUGH` [`00abfdc4`](#insn-00abfdc4) → [`00abfdc8`](#insn-00abfdc8)
- ブロック [`00abfdc8`](#insn-00abfdc8) 範囲 `[['00abfdc8', '00abfdd7']]`
  - `CONDITIONAL_JUMP` [`00abfdd4`](#insn-00abfdd4) → [`00ac0048`](#insn-00ac0048)
  - `FALL_THROUGH` [`00abfdd4`](#insn-00abfdd4) → [`00abfdd8`](#insn-00abfdd8)
- ブロック [`00abfdd8`](#insn-00abfdd8) 範囲 `[['00abfdd8', '00abfddf']]`
  - `CONDITIONAL_JUMP` [`00abfddc`](#insn-00abfddc) → [`00ac0068`](#insn-00ac0068)
  - `FALL_THROUGH` [`00abfddc`](#insn-00abfddc) → [`00abfde0`](#insn-00abfde0)
- ブロック [`00abfde0`](#insn-00abfde0) 範囲 `[['00abfde0', '00abfde7']]`
  - `CONDITIONAL_JUMP` [`00abfde4`](#insn-00abfde4) → [`00ac0078`](#insn-00ac0078)
  - `FALL_THROUGH` [`00abfde4`](#insn-00abfde4) → [`00abfde8`](#insn-00abfde8)
- ブロック [`00abfde8`](#insn-00abfde8) 範囲 `[['00abfde8', '00abfdef']]`
  - `CONDITIONAL_JUMP` [`00abfdec`](#insn-00abfdec) → [`00abfdf8`](#insn-00abfdf8)
  - `FALL_THROUGH` [`00abfdec`](#insn-00abfdec) → [`00abfdf0`](#insn-00abfdf0)
- ブロック [`00abfdf0`](#insn-00abfdf0) 範囲 `[['00abfdf0', '00abfdf7']]`
  - `FALL_THROUGH` [`00abfdf4`](#insn-00abfdf4) → [`00abfdf8`](#insn-00abfdf8)
- ブロック [`00abfdf8`](#insn-00abfdf8) 範囲 `[['00abfdf8', '00abfe0f']]`
  - `FALL_THROUGH` [`00abfe0c`](#insn-00abfe0c) → [`00abfe10`](#insn-00abfe10)
- ブロック [`00abfe10`](#insn-00abfe10) 範囲 `[['00abfe10', '00abfe1b']]`
  - `FALL_THROUGH` [`00abfe18`](#insn-00abfe18) → [`00abfe1c`](#insn-00abfe1c)
- ブロック [`00abfe1c`](#insn-00abfe1c) 範囲 `[['00abfe1c', '00abfe2f']]`
  - `UNCONDITIONAL_JUMP` [`00abfe2c`](#insn-00abfe2c) → [`00abffa4`](#insn-00abffa4)
- ブロック [`00abfe30`](#insn-00abfe30) 範囲 `[['00abfe30', '00abfe37']]`
  - `CONDITIONAL_JUMP` [`00abfe34`](#insn-00abfe34) → [`00ac01f8`](#insn-00ac01f8)
  - `FALL_THROUGH` [`00abfe34`](#insn-00abfe34) → [`00abfe38`](#insn-00abfe38)
- ブロック [`00abfe38`](#insn-00abfe38) 範囲 `[['00abfe38', '00abfe4f']]`
  - `FALL_THROUGH` [`00abfe4c`](#insn-00abfe4c) → [`00abfe50`](#insn-00abfe50)
- ブロック [`00abfe50`](#insn-00abfe50) 範囲 `[['00abfe50', '00abfe5b']]`
  - `FALL_THROUGH` [`00abfe58`](#insn-00abfe58) → [`00abfe5c`](#insn-00abfe5c)
- ブロック [`00abfe5c`](#insn-00abfe5c) 範囲 `[['00abfe5c', '00abfe73']]`
  - `CONDITIONAL_JUMP` [`00abfe70`](#insn-00abfe70) → [`00ac024c`](#insn-00ac024c)
  - `FALL_THROUGH` [`00abfe70`](#insn-00abfe70) → [`00abfe74`](#insn-00abfe74)
- ブロック [`00abfe74`](#insn-00abfe74) 範囲 `[['00abfe74', '00abfe87']]`
  - `CONDITIONAL_JUMP` [`00abfe84`](#insn-00abfe84) → [`00ac0264`](#insn-00ac0264)
  - `FALL_THROUGH` [`00abfe84`](#insn-00abfe84) → [`00abfe88`](#insn-00abfe88)
- ブロック [`00abfe88`](#insn-00abfe88) 範囲 `[['00abfe88', '00abfe97']]`
  - `CONDITIONAL_JUMP` [`00abfe94`](#insn-00abfe94) → [`00abfeac`](#insn-00abfeac)
  - `FALL_THROUGH` [`00abfe94`](#insn-00abfe94) → [`00abfe98`](#insn-00abfe98)
- ブロック [`00abfe98`](#insn-00abfe98) 範囲 `[['00abfe98', '00abfea7']]`
  - `FALL_THROUGH` [`00abfea4`](#insn-00abfea4) → [`00abfea8`](#insn-00abfea8)
- ブロック [`00abfea8`](#insn-00abfea8) 範囲 `[['00abfea8', '00abfeab']]`
  - `UNCONDITIONAL_JUMP` [`00abfea8`](#insn-00abfea8) → [`00abfeb8`](#insn-00abfeb8)
- ブロック [`00abfeac`](#insn-00abfeac) 範囲 `[['00abfeac', '00abfeb7']]`
  - `FALL_THROUGH` [`00abfeb4`](#insn-00abfeb4) → [`00abfeb8`](#insn-00abfeb8)
- ブロック [`00abfeb8`](#insn-00abfeb8) 範囲 `[['00abfeb8', '00abfefb']]`
  - `FALL_THROUGH` [`00abfef8`](#insn-00abfef8) → [`00abfefc`](#insn-00abfefc)
- ブロック [`00abfefc`](#insn-00abfefc) 範囲 `[['00abfefc', '00abff07']]`
  - `CONDITIONAL_JUMP` [`00abff04`](#insn-00abff04) → [`00abff30`](#insn-00abff30)
  - `FALL_THROUGH` [`00abff04`](#insn-00abff04) → [`00abff08`](#insn-00abff08)
- ブロック [`00abff08`](#insn-00abff08) 範囲 `[['00abff08', '00abff0f']]`
  - `FALL_THROUGH` [`00abff0c`](#insn-00abff0c) → [`00abff10`](#insn-00abff10)
- ブロック [`00abff10`](#insn-00abff10) 範囲 `[['00abff10', '00abff17']]`
  - `CONDITIONAL_JUMP` [`00abff14`](#insn-00abff14) → [`00abff30`](#insn-00abff30)
  - `FALL_THROUGH` [`00abff14`](#insn-00abff14) → [`00abff18`](#insn-00abff18)
- ブロック [`00abff18`](#insn-00abff18) 範囲 `[['00abff18', '00abff2f']]`
  - `FALL_THROUGH` [`00abff2c`](#insn-00abff2c) → [`00abff30`](#insn-00abff30)
- ブロック [`00abff30`](#insn-00abff30) 範囲 `[['00abff30', '00abff37']]`
  - `CONDITIONAL_JUMP` [`00abff34`](#insn-00abff34) → [`00abff48`](#insn-00abff48)
  - `FALL_THROUGH` [`00abff34`](#insn-00abff34) → [`00abff38`](#insn-00abff38)
- ブロック [`00abff38`](#insn-00abff38) 範囲 `[['00abff38', '00abff47']]`
  - `CONDITIONAL_JUMP` [`00abff44`](#insn-00abff44) → [`00ac008c`](#insn-00ac008c)
  - `FALL_THROUGH` [`00abff44`](#insn-00abff44) → [`00abff48`](#insn-00abff48)
- ブロック [`00abff48`](#insn-00abff48) 範囲 `[['00abff48', '00abff4f']]`
  - `CONDITIONAL_JUMP` [`00abff4c`](#insn-00abff4c) → [`00ac00ac`](#insn-00ac00ac)
  - `FALL_THROUGH` [`00abff4c`](#insn-00abff4c) → [`00abff50`](#insn-00abff50)
- ブロック [`00abff50`](#insn-00abff50) 範囲 `[['00abff50', '00abff53']]`
  - `FALL_THROUGH` [`00abff50`](#insn-00abff50) → [`00abff54`](#insn-00abff54)
- ブロック [`00abff54`](#insn-00abff54) 範囲 `[['00abff54', '00abff57']]`
  - `CONDITIONAL_JUMP` [`00abff54`](#insn-00abff54) → [`00ac00bc`](#insn-00ac00bc)
  - `FALL_THROUGH` [`00abff54`](#insn-00abff54) → [`00abff58`](#insn-00abff58)
- ブロック [`00abff58`](#insn-00abff58) 範囲 `[['00abff58', '00abff5f']]`
  - `CONDITIONAL_JUMP` [`00abff5c`](#insn-00abff5c) → [`00ac00cc`](#insn-00ac00cc)
  - `FALL_THROUGH` [`00abff5c`](#insn-00abff5c) → [`00abff60`](#insn-00abff60)
- ブロック [`00abff60`](#insn-00abff60) 範囲 `[['00abff60', '00abff67']]`
  - `CONDITIONAL_JUMP` [`00abff64`](#insn-00abff64) → [`00abff70`](#insn-00abff70)
  - `FALL_THROUGH` [`00abff64`](#insn-00abff64) → [`00abff68`](#insn-00abff68)
- ブロック [`00abff68`](#insn-00abff68) 範囲 `[['00abff68', '00abff6f']]`
  - `FALL_THROUGH` [`00abff6c`](#insn-00abff6c) → [`00abff70`](#insn-00abff70)
- ブロック [`00abff70`](#insn-00abff70) 範囲 `[['00abff70', '00abff8f']]`
  - `FALL_THROUGH` [`00abff8c`](#insn-00abff8c) → [`00abff90`](#insn-00abff90)
- ブロック [`00abff90`](#insn-00abff90) 範囲 `[['00abff90', '00abffa3']]`
  - `FALL_THROUGH` [`00abffa0`](#insn-00abffa0) → [`00abffa4`](#insn-00abffa4)
- ブロック [`00abffa4`](#insn-00abffa4) 範囲 `[['00abffa4', '00abffab']]`
  - `CONDITIONAL_JUMP` [`00abffa8`](#insn-00abffa8) → [`00abffb4`](#insn-00abffb4)
  - `FALL_THROUGH` [`00abffa8`](#insn-00abffa8) → [`00abffac`](#insn-00abffac)
- ブロック [`00abffac`](#insn-00abffac) 範囲 `[['00abffac', '00abffaf']]`
  - `FALL_THROUGH` [`00abffac`](#insn-00abffac) → [`00abffb0`](#insn-00abffb0)
- ブロック [`00abffb0`](#insn-00abffb0) 範囲 `[['00abffb0', '00abffb3']]`
  - `FALL_THROUGH` [`00abffb0`](#insn-00abffb0) → [`00abffb4`](#insn-00abffb4)
- ブロック [`00abffb4`](#insn-00abffb4) 範囲 `[['00abffb4', '00abffbb']]`
  - `FALL_THROUGH` [`00abffb8`](#insn-00abffb8) → [`00abffbc`](#insn-00abffbc)
- ブロック [`00abffbc`](#insn-00abffbc) 範囲 `[['00abffbc', '00abffc3']]`
  - `CONDITIONAL_JUMP` [`00abffc0`](#insn-00abffc0) → [`00ac03a0`](#insn-00ac03a0)
  - `FALL_THROUGH` [`00abffc0`](#insn-00abffc0) → [`00abffc4`](#insn-00abffc4)
- ブロック [`00abffc4`](#insn-00abffc4) 範囲 `[['00abffc4', '00abffdf']]`
- ブロック [`00abffe0`](#insn-00abffe0) 範囲 `[['00abffe0', '00abfff7']]`
  - `FALL_THROUGH` [`00abfff4`](#insn-00abfff4) → [`00abfff8`](#insn-00abfff8)
- ブロック [`00abfff8`](#insn-00abfff8) 範囲 `[['00abfff8', '00abffff']]`
  - `CONDITIONAL_JUMP` [`00abfffc`](#insn-00abfffc) → [`00abfcc4`](#insn-00abfcc4)
  - `FALL_THROUGH` [`00abfffc`](#insn-00abfffc) → [`00ac0000`](#insn-00ac0000)
- ブロック [`00ac0000`](#insn-00ac0000) 範囲 `[['00ac0000', '00ac0003']]`
  - `UNCONDITIONAL_JUMP` [`00ac0000`](#insn-00ac0000) → [`00abfcd4`](#insn-00abfcd4)
- ブロック [`00ac0004`](#insn-00ac0004) 範囲 `[['00ac0004', '00ac0013']]`
  - `FALL_THROUGH` [`00ac0010`](#insn-00ac0010) → [`00ac0014`](#insn-00ac0014)
- ブロック [`00ac0014`](#insn-00ac0014) 範囲 `[['00ac0014', '00ac001f']]`
  - `FALL_THROUGH` [`00ac001c`](#insn-00ac001c) → [`00ac0020`](#insn-00ac0020)
- ブロック [`00ac0020`](#insn-00ac0020) 範囲 `[['00ac0020', '00ac0023']]`
  - `CONDITIONAL_JUMP` [`00ac0020`](#insn-00ac0020) → [`00abfcdc`](#insn-00abfcdc)
  - `FALL_THROUGH` [`00ac0020`](#insn-00ac0020) → [`00ac0024`](#insn-00ac0024)
- ブロック [`00ac0024`](#insn-00ac0024) 範囲 `[['00ac0024', '00ac0033']]`
  - `CONDITIONAL_JUMP` [`00ac0030`](#insn-00ac0030) → [`00abfce4`](#insn-00abfce4)
  - `FALL_THROUGH` [`00ac0030`](#insn-00ac0030) → [`00ac0034`](#insn-00ac0034)
- ブロック [`00ac0034`](#insn-00ac0034) 範囲 `[['00ac0034', '00ac0043']]`
  - `CONDITIONAL_JUMP` [`00ac0040`](#insn-00ac0040) → [`00abfcec`](#insn-00abfcec)
  - `FALL_THROUGH` [`00ac0040`](#insn-00ac0040) → [`00ac0044`](#insn-00ac0044)
- ブロック [`00ac0044`](#insn-00ac0044) 範囲 `[['00ac0044', '00ac0047']]`
  - `UNCONDITIONAL_JUMP` [`00ac0044`](#insn-00ac0044) → [`00abfcf4`](#insn-00abfcf4)
- ブロック [`00ac0048`](#insn-00ac0048) 範囲 `[['00ac0048', '00ac005b']]`
  - `FALL_THROUGH` [`00ac0058`](#insn-00ac0058) → [`00ac005c`](#insn-00ac005c)
- ブロック [`00ac005c`](#insn-00ac005c) 範囲 `[['00ac005c', '00ac0067']]`
  - `CONDITIONAL_JUMP` [`00ac0064`](#insn-00ac0064) → [`00abfde0`](#insn-00abfde0)
  - `FALL_THROUGH` [`00ac0064`](#insn-00ac0064) → [`00ac0068`](#insn-00ac0068)
- ブロック [`00ac0068`](#insn-00ac0068) 範囲 `[['00ac0068', '00ac0077']]`
  - `CONDITIONAL_JUMP` [`00ac0074`](#insn-00ac0074) → [`00abfde8`](#insn-00abfde8)
  - `FALL_THROUGH` [`00ac0074`](#insn-00ac0074) → [`00ac0078`](#insn-00ac0078)
- ブロック [`00ac0078`](#insn-00ac0078) 範囲 `[['00ac0078', '00ac0087']]`
  - `CONDITIONAL_JUMP` [`00ac0084`](#insn-00ac0084) → [`00abfdf0`](#insn-00abfdf0)
  - `FALL_THROUGH` [`00ac0084`](#insn-00ac0084) → [`00ac0088`](#insn-00ac0088)
- ブロック [`00ac0088`](#insn-00ac0088) 範囲 `[['00ac0088', '00ac008b']]`
  - `UNCONDITIONAL_JUMP` [`00ac0088`](#insn-00ac0088) → [`00abfdf8`](#insn-00abfdf8)
- ブロック [`00ac008c`](#insn-00ac008c) 範囲 `[['00ac008c', '00ac00ab']]`
  - `CONDITIONAL_JUMP` [`00ac00a8`](#insn-00ac00a8) → [`00abff50`](#insn-00abff50)
  - `FALL_THROUGH` [`00ac00a8`](#insn-00ac00a8) → [`00ac00ac`](#insn-00ac00ac)
- ブロック [`00ac00ac`](#insn-00ac00ac) 範囲 `[['00ac00ac', '00ac00af']]`
  - `FALL_THROUGH` [`00ac00ac`](#insn-00ac00ac) → [`00ac00b0`](#insn-00ac00b0)
- ブロック [`00ac00b0`](#insn-00ac00b0) 範囲 `[['00ac00b0', '00ac00bb']]`
  - `CONDITIONAL_JUMP` [`00ac00b8`](#insn-00ac00b8) → [`00abff58`](#insn-00abff58)
  - `FALL_THROUGH` [`00ac00b8`](#insn-00ac00b8) → [`00ac00bc`](#insn-00ac00bc)
- ブロック [`00ac00bc`](#insn-00ac00bc) 範囲 `[['00ac00bc', '00ac00cb']]`
  - `CONDITIONAL_JUMP` [`00ac00c8`](#insn-00ac00c8) → [`00abff60`](#insn-00abff60)
  - `FALL_THROUGH` [`00ac00c8`](#insn-00ac00c8) → [`00ac00cc`](#insn-00ac00cc)
- ブロック [`00ac00cc`](#insn-00ac00cc) 範囲 `[['00ac00cc', '00ac00db']]`
  - `CONDITIONAL_JUMP` [`00ac00d8`](#insn-00ac00d8) → [`00abff68`](#insn-00abff68)
  - `FALL_THROUGH` [`00ac00d8`](#insn-00ac00d8) → [`00ac00dc`](#insn-00ac00dc)
- ブロック [`00ac00dc`](#insn-00ac00dc) 範囲 `[['00ac00dc', '00ac00df']]`
  - `UNCONDITIONAL_JUMP` [`00ac00dc`](#insn-00ac00dc) → [`00abff70`](#insn-00abff70)
- ブロック [`00ac00e0`](#insn-00ac00e0) 範囲 `[['00ac00e0', '00ac00ef']]`
  - `CONDITIONAL_JUMP` [`00ac00ec`](#insn-00ac00ec) → [`00abfaf4`](#insn-00abfaf4)
  - `FALL_THROUGH` [`00ac00ec`](#insn-00ac00ec) → [`00ac00f0`](#insn-00ac00f0)
- ブロック [`00ac00f0`](#insn-00ac00f0) 範囲 `[['00ac00f0', '00ac011b']]`
  - `FALL_THROUGH` [`00ac0118`](#insn-00ac0118) → [`00ac011c`](#insn-00ac011c)
- ブロック [`00ac011c`](#insn-00ac011c) 範囲 `[['00ac011c', '00ac011f']]`
  - `FALL_THROUGH` [`00ac011c`](#insn-00ac011c) → [`00ac0120`](#insn-00ac0120)
- ブロック [`00ac0120`](#insn-00ac0120) 範囲 `[['00ac0120', '00ac0137']]`
  - `UNCONDITIONAL_JUMP` [`00ac0134`](#insn-00ac0134) → [`00abfaf4`](#insn-00abfaf4)
- ブロック [`00ac0138`](#insn-00ac0138) 範囲 `[['00ac0138', '00ac0147']]`
  - `CONDITIONAL_JUMP` [`00ac0144`](#insn-00ac0144) → [`00abfc14`](#insn-00abfc14)
  - `FALL_THROUGH` [`00ac0144`](#insn-00ac0144) → [`00ac0148`](#insn-00ac0148)
- ブロック [`00ac0148`](#insn-00ac0148) 範囲 `[['00ac0148', '00ac014f']]`
  - `FALL_THROUGH` [`00ac014c`](#insn-00ac014c) → [`00ac0150`](#insn-00ac0150)
- ブロック [`00ac0150`](#insn-00ac0150) 範囲 `[['00ac0150', '00ac0153']]`
  - `FALL_THROUGH` [`00ac0150`](#insn-00ac0150) → [`00ac0154`](#insn-00ac0154)
- ブロック [`00ac0154`](#insn-00ac0154) 範囲 `[['00ac0154', '00ac015b']]`
  - `FALL_THROUGH` [`00ac0158`](#insn-00ac0158) → [`00ac015c`](#insn-00ac015c)
- ブロック [`00ac015c`](#insn-00ac015c) 範囲 `[['00ac015c', '00ac015f']]`
  - `FALL_THROUGH` [`00ac015c`](#insn-00ac015c) → [`00ac0160`](#insn-00ac0160)
- ブロック [`00ac0160`](#insn-00ac0160) 範囲 `[['00ac0160', '00ac0173']]`
  - `FALL_THROUGH` [`00ac0170`](#insn-00ac0170) → [`00ac0174`](#insn-00ac0174)
- ブロック [`00ac0174`](#insn-00ac0174) 範囲 `[['00ac0174', '00ac0177']]`
  - `FALL_THROUGH` [`00ac0174`](#insn-00ac0174) → [`00ac0178`](#insn-00ac0178)
- ブロック [`00ac0178`](#insn-00ac0178) 範囲 `[['00ac0178', '00ac017f']]`
  - `FALL_THROUGH` [`00ac017c`](#insn-00ac017c) → [`00ac0180`](#insn-00ac0180)
- ブロック [`00ac0180`](#insn-00ac0180) 範囲 `[['00ac0180', '00ac0183']]`
  - `FALL_THROUGH` [`00ac0180`](#insn-00ac0180) → [`00ac0184`](#insn-00ac0184)
- ブロック [`00ac0184`](#insn-00ac0184) 範囲 `[['00ac0184', '00ac018b']]`
  - `UNCONDITIONAL_JUMP` [`00ac0188`](#insn-00ac0188) → [`00abfc14`](#insn-00abfc14)
- ブロック [`00ac018c`](#insn-00ac018c) 範囲 `[['00ac018c', '00ac018f']]`
  - `FALL_THROUGH` [`00ac018c`](#insn-00ac018c) → [`00ac0190`](#insn-00ac0190)
- ブロック [`00ac0190`](#insn-00ac0190) 範囲 `[['00ac0190', '00ac019b']]`
  - `CONDITIONAL_JUMP` [`00ac0198`](#insn-00ac0198) → [`00ac03a0`](#insn-00ac03a0)
  - `FALL_THROUGH` [`00ac0198`](#insn-00ac0198) → [`00ac019c`](#insn-00ac019c)
- ブロック [`00ac019c`](#insn-00ac019c) 範囲 `[['00ac019c', '00ac01a3']]`
- ブロック [`00ac01a4`](#insn-00ac01a4) 範囲 `[['00ac01a4', '00ac01b3']]`
  - `CONDITIONAL_JUMP` [`00ac01b0`](#insn-00ac01b0) → [`00abfd0c`](#insn-00abfd0c)
  - `FALL_THROUGH` [`00ac01b0`](#insn-00ac01b0) → [`00ac01b4`](#insn-00ac01b4)
- ブロック [`00ac01b4`](#insn-00ac01b4) 範囲 `[['00ac01b4', '00ac01eb']]`
  - `FALL_THROUGH` [`00ac01e8`](#insn-00ac01e8) → [`00ac01ec`](#insn-00ac01ec)
- ブロック [`00ac01ec`](#insn-00ac01ec) 範囲 `[['00ac01ec', '00ac01ef']]`
  - `FALL_THROUGH` [`00ac01ec`](#insn-00ac01ec) → [`00ac01f0`](#insn-00ac01f0)
- ブロック [`00ac01f0`](#insn-00ac01f0) 範囲 `[['00ac01f0', '00ac01f7']]`
  - `UNCONDITIONAL_JUMP` [`00ac01f4`](#insn-00ac01f4) → [`00abfd0c`](#insn-00abfd0c)
- ブロック [`00ac01f8`](#insn-00ac01f8) 範囲 `[['00ac01f8', '00ac01ff']]`
  - `FALL_THROUGH` [`00ac01fc`](#insn-00ac01fc) → [`00ac0200`](#insn-00ac0200)
- ブロック [`00ac0200`](#insn-00ac0200) 範囲 `[['00ac0200', '00ac0207']]`
  - `CONDITIONAL_JUMP` [`00ac0204`](#insn-00ac0204) → [`00abfe38`](#insn-00abfe38)
  - `FALL_THROUGH` [`00ac0204`](#insn-00ac0204) → [`00ac0208`](#insn-00ac0208)
- ブロック [`00ac0208`](#insn-00ac0208) 範囲 `[['00ac0208', '00ac0217']]`
  - `FALL_THROUGH` [`00ac0214`](#insn-00ac0214) → [`00ac0218`](#insn-00ac0218)
- ブロック [`00ac0218`](#insn-00ac0218) 範囲 `[['00ac0218', '00ac022b']]`
  - `FALL_THROUGH` [`00ac0228`](#insn-00ac0228) → [`00ac022c`](#insn-00ac022c)
- ブロック [`00ac022c`](#insn-00ac022c) 範囲 `[['00ac022c', '00ac0233']]`
  - `FALL_THROUGH` [`00ac0230`](#insn-00ac0230) → [`00ac0234`](#insn-00ac0234)
- ブロック [`00ac0234`](#insn-00ac0234) 範囲 `[['00ac0234', '00ac0237']]`
  - `FALL_THROUGH` [`00ac0234`](#insn-00ac0234) → [`00ac0238`](#insn-00ac0238)
- ブロック [`00ac0238`](#insn-00ac0238) 範囲 `[['00ac0238', '00ac024b']]`
  - `UNCONDITIONAL_JUMP` [`00ac0248`](#insn-00ac0248) → [`00abfe38`](#insn-00abfe38)
- ブロック [`00ac024c`](#insn-00ac024c) 範囲 `[['00ac024c', '00ac024f']]`
  - `FALL_THROUGH` [`00ac024c`](#insn-00ac024c) → [`00ac0250`](#insn-00ac0250)
- ブロック [`00ac0250`](#insn-00ac0250) 範囲 `[['00ac0250', '00ac025b']]`
  - `CONDITIONAL_JUMP` [`00ac0258`](#insn-00ac0258) → [`00ac03a0`](#insn-00ac03a0)
  - `FALL_THROUGH` [`00ac0258`](#insn-00ac0258) → [`00ac025c`](#insn-00ac025c)
- ブロック [`00ac025c`](#insn-00ac025c) 範囲 `[['00ac025c', '00ac0263']]`
- ブロック [`00ac0264`](#insn-00ac0264) 範囲 `[['00ac0264', '00ac026b']]`
  - `FALL_THROUGH` [`00ac0268`](#insn-00ac0268) → [`00ac026c`](#insn-00ac026c)
- ブロック [`00ac026c`](#insn-00ac026c) 範囲 `[['00ac026c', '00ac026f']]`
  - `FALL_THROUGH` [`00ac026c`](#insn-00ac026c) → [`00ac0270`](#insn-00ac0270)
- ブロック [`00ac0270`](#insn-00ac0270) 範囲 `[['00ac0270', '00ac0273']]`
  - `CONDITIONAL_JUMP` [`00ac0270`](#insn-00ac0270) → [`00ac03a0`](#insn-00ac03a0)
  - `FALL_THROUGH` [`00ac0270`](#insn-00ac0270) → [`00ac0274`](#insn-00ac0274)
- ブロック [`00ac0274`](#insn-00ac0274) 範囲 `[['00ac0274', '00ac027f']]`
  - `UNCONDITIONAL_JUMP` [`00ac027c`](#insn-00ac027c) → [`00ac02ac`](#insn-00ac02ac)
- ブロック [`00ac02ac`](#insn-00ac02ac) 範囲 `[['00ac02ac', '00ac02b7']]`
  - `CONDITIONAL_JUMP` [`00ac02b4`](#insn-00ac02b4) → [`00ac0348`](#insn-00ac0348)
  - `FALL_THROUGH` [`00ac02b4`](#insn-00ac02b4) → [`00ac02b8`](#insn-00ac02b8)
- ブロック [`00ac02b8`](#insn-00ac02b8) 範囲 `[['00ac02b8', '00ac02bb']]`
  - `UNCONDITIONAL_JUMP` [`00ac02b8`](#insn-00ac02b8) → [`00ac0388`](#insn-00ac0388)
- ブロック [`00ac0348`](#insn-00ac0348) 範囲 `[['00ac0348', '00ac034f']]`
  - `UNCONDITIONAL_JUMP` [`00ac034c`](#insn-00ac034c) → [`00ac0384`](#insn-00ac0384)
- ブロック [`00ac0384`](#insn-00ac0384) 範囲 `[['00ac0384', '00ac0387']]`
  - `FALL_THROUGH` [`00ac0384`](#insn-00ac0384) → [`00ac0388`](#insn-00ac0388)
- ブロック [`00ac0388`](#insn-00ac0388) 範囲 `[['00ac0388', '00ac0397']]`
  - `CONDITIONAL_JUMP` [`00ac0394`](#insn-00ac0394) → [`00ac03a0`](#insn-00ac03a0)
  - `FALL_THROUGH` [`00ac0394`](#insn-00ac0394) → [`00ac0398`](#insn-00ac0398)
- ブロック [`00ac0398`](#insn-00ac0398) 範囲 `[['00ac0398', '00ac039f']]`
- ブロック [`00ac03a0`](#insn-00ac03a0) 範囲 `[['00ac03a0', '00ac03a3']]`

## 命令位置別の参照

- [`00abfaac`](#insn-00abfaac) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfab0`](#insn-00abfab0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfab4`](#insn-00abfab4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfab8`](#insn-00abfab8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfabc`](#insn-00abfabc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfacc`](#insn-00abfacc) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfad8`](#insn-00abfad8) → [`00abffb4`](#insn-00abffb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfae8`](#insn-00abfae8) → `00ca4f38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abfaf0`](#insn-00abfaf0) → [`00ac00e0`](#insn-00ac00e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfb00`](#insn-00abfb00) → `002ab9a4`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abfb04`](#insn-00abfb04) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfb14`](#insn-00abfb14) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfb18`](#insn-00abfb18) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfb20`](#insn-00abfb20) → `002adb15`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abfb28`](#insn-00abfb28) → `Stack[-0x5f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfb2c`](#insn-00abfb2c) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfb30`](#insn-00abfb30) → `Stack[-0x87]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfb34`](#insn-00abfb34) → `Stack[-0x74]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfb4c`](#insn-00abfb4c) → `00ca4f00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abfb54`](#insn-00abfb54) → [`0047e60c`](../0047e/0047e60c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047e60c` · 推定シンボル `None` · 推定型 `None`
- [`00abfb58`](#insn-00abfb58) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfb60`](#insn-00abfb60) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfb68`](#insn-00abfb68) → [`00abfb7c`](#insn-00abfb7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfb74`](#insn-00abfb74) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00abfb78`](#insn-00abfb78) → [`00abfbb0`](#insn-00abfbb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfb7c`](#insn-00abfb7c) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfb80`](#insn-00abfb80) → [`00abfb94`](#insn-00abfb94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfb8c`](#insn-00abfb8c) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00abfb90`](#insn-00abfb90) → [`00abfbd4`](#insn-00abfbd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfb94`](#insn-00abfb94) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfb98`](#insn-00abfb98) → [`00abfbf4`](#insn-00abfbf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfb9c`](#insn-00abfb9c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfba0`](#insn-00abfba0) → [`00abfc04`](#insn-00abfc04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfba4`](#insn-00abfba4) → `00ca4f38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abfba8`](#insn-00abfba8) → [`00abfc14`](#insn-00abfc14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfbac`](#insn-00abfbac) → [`00ac0138`](#insn-00ac0138) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfbc4`](#insn-00abfbc4) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00abfbc8`](#insn-00abfbc8) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfbcc`](#insn-00abfbcc) → [`00abfb84`](#insn-00abfb84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfbd0`](#insn-00abfbd0) → [`00abfb94`](#insn-00abfb94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfbe8`](#insn-00abfbe8) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00abfbec`](#insn-00abfbec) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfbf0`](#insn-00abfbf0) → [`00abfb9c`](#insn-00abfb9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfbf4`](#insn-00abfbf4) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfbf8`](#insn-00abfbf8) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00abfbfc`](#insn-00abfbfc) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfc00`](#insn-00abfc00) → [`00abfba4`](#insn-00abfba4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfc04`](#insn-00abfc04) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfc08`](#insn-00abfc08) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00abfc0c`](#insn-00abfc0c) → `00ca4f38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abfc10`](#insn-00abfc10) → [`00ac0138`](#insn-00ac0138) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfc24`](#insn-00abfc24) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfc2c`](#insn-00abfc2c) → `002bb847`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abfc30`](#insn-00abfc30) → `002bb84d`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abfc34`](#insn-00abfc34) → `Stack[-0x79]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfc3c`](#insn-00abfc3c) → `Stack[-0x87]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfc40`](#insn-00abfc40) → `Stack[-0x81]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfc44`](#insn-00abfc44) → [`00ac018c`](#insn-00ac018c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfc58`](#insn-00abfc58) → [`00447ef4`](../00447/00447ef4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00447ef4` · 推定シンボル `None` · 推定型 `None`
- [`00abfc68`](#insn-00abfc68) → `002bcaee`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abfc6c`](#insn-00abfc6c) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfc70`](#insn-00abfc70) → `Stack[-0xaf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfc74`](#insn-00abfc74) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfc8c`](#insn-00abfc8c) → `00ca4f00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abfc94`](#insn-00abfc94) → [`0047e60c`](../0047e/0047e60c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047e60c` · 推定シンボル `None` · 推定型 `None`
- [`00abfc98`](#insn-00abfc98) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfca0`](#insn-00abfca0) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfca8`](#insn-00abfca8) → [`00abfcbc`](#insn-00abfcbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfcb4`](#insn-00abfcb4) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00abfcb8`](#insn-00abfcb8) → [`00abffe0`](#insn-00abffe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfcbc`](#insn-00abfcbc) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfcc0`](#insn-00abfcc0) → [`00abfcd4`](#insn-00abfcd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfccc`](#insn-00abfccc) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00abfcd0`](#insn-00abfcd0) → [`00ac0004`](#insn-00ac0004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfcd4`](#insn-00abfcd4) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfcd8`](#insn-00abfcd8) → [`00ac0024`](#insn-00ac0024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfcdc`](#insn-00abfcdc) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfce0`](#insn-00abfce0) → [`00ac0034`](#insn-00ac0034) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfce4`](#insn-00abfce4) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfce8`](#insn-00abfce8) → [`00abfcf4`](#insn-00abfcf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfcec`](#insn-00abfcec) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfcf0`](#insn-00abfcf0) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00abfd00`](#insn-00abfd00) → [`00abfe30`](#insn-00abfe30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd04`](#insn-00abfd04) → `00ca4f38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abfd08`](#insn-00abfd08) → [`00ac01a4`](#insn-00ac01a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd18`](#insn-00abfd18) → `002a1893`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abfd20`](#insn-00abfd20) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd24`](#insn-00abfd24) → `Stack[-0xb7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd28`](#insn-00abfd28) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd2c`](#insn-00abfd2c) → `Stack[-0xb5]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd38`](#insn-00abfd38) → [`0048ce54`](../0048c/0048ce54.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce54` · 推定シンボル `None` · 推定型 `None`
- [`00abfd54`](#insn-00abfd54) → [`00447ef4`](../00447/00447ef4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00447ef4` · 推定シンボル `None` · 推定型 `None`
- [`00abfd60`](#insn-00abfd60) → `00ca4f00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abfd64`](#insn-00abfd64) → `00c9aca0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abfd64`](#insn-00abfd64) → `00ca4fd8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abfd80`](#insn-00abfd80) → [`0047e8dc`](../0047e/0047e8dc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047e8dc` · 推定シンボル `None` · 推定型 `None`
- [`00abfd84`](#insn-00abfd84) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd8c`](#insn-00abfd8c) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfd94`](#insn-00abfd94) → [`00abfdc0`](#insn-00abfdc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfda0`](#insn-00abfda0) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00abfda4`](#insn-00abfda4) → [`00abfdc0`](#insn-00abfdc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfdbc`](#insn-00abfdbc) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00abfdc0`](#insn-00abfdc0) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfdc4`](#insn-00abfdc4) → [`00abfdd8`](#insn-00abfdd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfdd0`](#insn-00abfdd0) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00abfdd4`](#insn-00abfdd4) → [`00ac0048`](#insn-00ac0048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfdd8`](#insn-00abfdd8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfddc`](#insn-00abfddc) → [`00ac0068`](#insn-00ac0068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfde0`](#insn-00abfde0) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfde4`](#insn-00abfde4) → [`00ac0078`](#insn-00ac0078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfde8`](#insn-00abfde8) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfdec`](#insn-00abfdec) → [`00abfdf8`](#insn-00abfdf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfdf0`](#insn-00abfdf0) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfdf4`](#insn-00abfdf4) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00abfe04`](#insn-00abfe04) → `002afefe`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abfe10`](#insn-00abfe10) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe14`](#insn-00abfe14) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe18`](#insn-00abfe18) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe1c`](#insn-00abfe1c) → `Stack[-0x5c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe28`](#insn-00abfe28) → [`0046e970`](../0046e/0046e970.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046e970` · 推定シンボル `None` · 推定型 `None`
- [`00abfe2c`](#insn-00abfe2c) → [`00abffa4`](#insn-00abffa4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe30`](#insn-00abfe30) → `00ca4f38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abfe34`](#insn-00abfe34) → [`00ac01f8`](#insn-00ac01f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe44`](#insn-00abfe44) → `002a189e`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abfe4c`](#insn-00abfe4c) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe50`](#insn-00abfe50) → `Stack[-0xb7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe54`](#insn-00abfe54) → `Stack[-0xbf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe58`](#insn-00abfe58) → `Stack[-0xb5]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe64`](#insn-00abfe64) → [`0048ce54`](../0048c/0048ce54.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048ce54` · 推定シンボル `None` · 推定型 `None`
- [`00abfe70`](#insn-00abfe70) → [`00ac024c`](#insn-00ac024c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe84`](#insn-00abfe84) → [`00ac0264`](#insn-00ac0264) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfe94`](#insn-00abfe94) → [`00abfeac`](#insn-00abfeac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfea0`](#insn-00abfea0) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfea4`](#insn-00abfea4) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfea8`](#insn-00abfea8) → [`00abfeb8`](#insn-00abfeb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfeb4`](#insn-00abfeb4) → [`0043bb20`](../0043b/0043bb20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb20` · 推定シンボル `None` · 推定型 `None`
- [`00abfec4`](#insn-00abfec4) → [`00492e08`](../00492/00492e08.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00492e08` · 推定シンボル `None` · 推定型 `None`
- [`00abfed0`](#insn-00abfed0) → `00ca4f00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00abfed4`](#insn-00abfed4) → `00c9aca0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00abfed4`](#insn-00abfed4) → `00ca4fd8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00abfef0`](#insn-00abfef0) → [`0047e8dc`](../0047e/0047e8dc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047e8dc` · 推定シンボル `None` · 推定型 `None`
- [`00abfef4`](#insn-00abfef4) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfefc`](#insn-00abfefc) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abff04`](#insn-00abff04) → [`00abff30`](#insn-00abff30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abff10`](#insn-00abff10) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00abff14`](#insn-00abff14) → [`00abff30`](#insn-00abff30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abff2c`](#insn-00abff2c) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00abff30`](#insn-00abff30) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abff34`](#insn-00abff34) → [`00abff48`](#insn-00abff48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abff40`](#insn-00abff40) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00abff44`](#insn-00abff44) → [`00ac008c`](#insn-00ac008c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abff48`](#insn-00abff48) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abff4c`](#insn-00abff4c) → [`00ac00ac`](#insn-00ac00ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abff50`](#insn-00abff50) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abff54`](#insn-00abff54) → [`00ac00bc`](#insn-00ac00bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abff58`](#insn-00abff58) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abff5c`](#insn-00abff5c) → [`00ac00cc`](#insn-00ac00cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abff60`](#insn-00abff60) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abff64`](#insn-00abff64) → [`00abff70`](#insn-00abff70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abff68`](#insn-00abff68) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abff6c`](#insn-00abff6c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00abff7c`](#insn-00abff7c) → `002b7bbd`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00abff88`](#insn-00abff88) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abff8c`](#insn-00abff8c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abff90`](#insn-00abff90) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abff94`](#insn-00abff94) → `Stack[-0x5c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abffa0`](#insn-00abffa0) → [`0046e970`](../0046e/0046e970.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046e970` · 推定シンボル `None` · 推定型 `None`
- [`00abffa4`](#insn-00abffa4) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abffa8`](#insn-00abffa8) → [`00abffb4`](#insn-00abffb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abffac`](#insn-00abffac) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abffb0`](#insn-00abffb0) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00abffb8`](#insn-00abffb8) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abffc0`](#insn-00abffc0) → [`00ac03a0`](#insn-00ac03a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abffc4`](#insn-00abffc4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abffc8`](#insn-00abffc8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abffcc`](#insn-00abffcc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abffd0`](#insn-00abffd0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abffd4`](#insn-00abffd4) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfff4`](#insn-00abfff4) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00abfff8`](#insn-00abfff8) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abfffc`](#insn-00abfffc) → [`00abfcc4`](#insn-00abfcc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0000`](#insn-00ac0000) → [`00abfcd4`](#insn-00abfcd4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0018`](#insn-00ac0018) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00ac001c`](#insn-00ac001c) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0020`](#insn-00ac0020) → [`00abfcdc`](#insn-00abfcdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0024`](#insn-00ac0024) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0028`](#insn-00ac0028) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00ac002c`](#insn-00ac002c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0030`](#insn-00ac0030) → [`00abfce4`](#insn-00abfce4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0034`](#insn-00ac0034) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0038`](#insn-00ac0038) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00ac003c`](#insn-00ac003c) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0040`](#insn-00ac0040) → [`00abfcec`](#insn-00abfcec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0044`](#insn-00ac0044) → [`00abfcf4`](#insn-00abfcf4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac005c`](#insn-00ac005c) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00ac0060`](#insn-00ac0060) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0064`](#insn-00ac0064) → [`00abfde0`](#insn-00abfde0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0068`](#insn-00ac0068) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac006c`](#insn-00ac006c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00ac0070`](#insn-00ac0070) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0074`](#insn-00ac0074) → [`00abfde8`](#insn-00abfde8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0078`](#insn-00ac0078) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac007c`](#insn-00ac007c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00ac0080`](#insn-00ac0080) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0084`](#insn-00ac0084) → [`00abfdf0`](#insn-00abfdf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0088`](#insn-00ac0088) → [`00abfdf8`](#insn-00abfdf8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac00a0`](#insn-00ac00a0) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00ac00a4`](#insn-00ac00a4) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac00a8`](#insn-00ac00a8) → [`00abff50`](#insn-00abff50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac00ac`](#insn-00ac00ac) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac00b0`](#insn-00ac00b0) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00ac00b4`](#insn-00ac00b4) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac00b8`](#insn-00ac00b8) → [`00abff58`](#insn-00abff58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac00bc`](#insn-00ac00bc) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac00c0`](#insn-00ac00c0) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00ac00c4`](#insn-00ac00c4) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac00c8`](#insn-00ac00c8) → [`00abff60`](#insn-00abff60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac00cc`](#insn-00ac00cc) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac00d0`](#insn-00ac00d0) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00ac00d4`](#insn-00ac00d4) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac00d8`](#insn-00ac00d8) → [`00abff68`](#insn-00abff68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac00dc`](#insn-00ac00dc) → [`00abff70`](#insn-00abff70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac00e4`](#insn-00ac00e4) → `00ca4f38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ac00e8`](#insn-00ac00e8) → [`00c57e50`](../00c57/00c57e50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e50` · 推定シンボル `None` · 推定型 `None`
- [`00ac00ec`](#insn-00ac00ec) → [`00abfaf4`](#insn-00abfaf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac00f4`](#insn-00ac00f4) → `00ca4f00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac00fc`](#insn-00ac00fc) → [`0047edb4`](../0047e/0047edb4.md) · `PARAM` · `ANALYSIS` · 関数 `0047edb4` · 推定シンボル `None` · 推定型 `None`
- [`00ac0108`](#insn-00ac0108) → `00c62f90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ac010c`](#insn-00ac010c) → `00ca4f08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0110`](#insn-00ac0110) → `00ca4f00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0110`](#insn-00ac0110) → `00ca4f08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0118`](#insn-00ac0118) → `00ca4f28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0118`](#insn-00ac0118) → `00ca4f30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac011c`](#insn-00ac011c) → `00ca4f20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0120`](#insn-00ac0120) → `00ca4f10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0120`](#insn-00ac0120) → `00ca4f18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0120`](#insn-00ac0120) → `00ca4f20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0124`](#insn-00ac0124) → [`00c57e30`](../00c57/00c57e30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e30` · 推定シンボル `None` · 推定型 `None`
- [`00ac012c`](#insn-00ac012c) → `00ca4f38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ac0130`](#insn-00ac0130) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00ac0134`](#insn-00ac0134) → [`00abfaf4`](#insn-00abfaf4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac013c`](#insn-00ac013c) → `00ca4f38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ac0140`](#insn-00ac0140) → [`00c57e50`](../00c57/00c57e50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e50` · 推定シンボル `None` · 推定型 `None`
- [`00ac0144`](#insn-00ac0144) → [`00abfc14`](#insn-00abfc14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0150`](#insn-00ac0150) → [`0047edb4`](../0047e/0047edb4.md) · `PARAM` · `ANALYSIS` · 関数 `0047edb4` · 推定シンボル `None` · 推定型 `None`
- [`00ac0154`](#insn-00ac0154) → `00ca4f08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac015c`](#insn-00ac015c) → `00c62f90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ac0160`](#insn-00ac0160) → `00ca4f00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0160`](#insn-00ac0160) → `00ca4f08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0168`](#insn-00ac0168) → `00ca4f00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac016c`](#insn-00ac016c) → `00ca4f28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac016c`](#insn-00ac016c) → `00ca4f30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0170`](#insn-00ac0170) → `00ca4f20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0174`](#insn-00ac0174) → `00ca4f10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0174`](#insn-00ac0174) → `00ca4f18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0174`](#insn-00ac0174) → `00ca4f20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0178`](#insn-00ac0178) → [`00c57e30`](../00c57/00c57e30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e30` · 推定シンボル `None` · 推定型 `None`
- [`00ac0180`](#insn-00ac0180) → `00ca4f38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ac0184`](#insn-00ac0184) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00ac0188`](#insn-00ac0188) → [`00abfc14`](#insn-00abfc14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0190`](#insn-00ac0190) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0198`](#insn-00ac0198) → [`00ac03a0`](#insn-00ac03a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac01a0`](#insn-00ac01a0) → [`0049f3f0`](../0049f/0049f3f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0049f3f0` · 推定シンボル `None` · 推定型 `None`
- [`00ac01a8`](#insn-00ac01a8) → `00ca4f38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ac01ac`](#insn-00ac01ac) → [`00c57e50`](../00c57/00c57e50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e50` · 推定シンボル `None` · 推定型 `None`
- [`00ac01b0`](#insn-00ac01b0) → [`00abfd0c`](#insn-00abfd0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac01bc`](#insn-00ac01bc) → [`0047edb4`](../0047e/0047edb4.md) · `PARAM` · `ANALYSIS` · 関数 `0047edb4` · 推定シンボル `None` · 推定型 `None`
- [`00ac01c0`](#insn-00ac01c0) → `00ca4f08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac01c8`](#insn-00ac01c8) → `00c62f90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ac01cc`](#insn-00ac01cc) → `00ca4f00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac01cc`](#insn-00ac01cc) → `00ca4f08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac01d4`](#insn-00ac01d4) → `00ca4f00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac01d8`](#insn-00ac01d8) → `00ca4f28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac01d8`](#insn-00ac01d8) → `00ca4f30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac01dc`](#insn-00ac01dc) → `00ca4f20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac01e0`](#insn-00ac01e0) → `00ca4f10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac01e0`](#insn-00ac01e0) → `00ca4f18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac01e0`](#insn-00ac01e0) → `00ca4f20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac01e4`](#insn-00ac01e4) → [`00c57e30`](../00c57/00c57e30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e30` · 推定シンボル `None` · 推定型 `None`
- [`00ac01ec`](#insn-00ac01ec) → `00ca4f38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ac01f0`](#insn-00ac01f0) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00ac01f4`](#insn-00ac01f4) → [`00abfd0c`](#insn-00abfd0c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac01fc`](#insn-00ac01fc) → `00ca4f38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ac0200`](#insn-00ac0200) → [`00c57e50`](../00c57/00c57e50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e50` · 推定シンボル `None` · 推定型 `None`
- [`00ac0204`](#insn-00ac0204) → [`00abfe38`](#insn-00abfe38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0210`](#insn-00ac0210) → [`0047edb4`](../0047e/0047edb4.md) · `PARAM` · `ANALYSIS` · 関数 `0047edb4` · 推定シンボル `None` · 推定型 `None`
- [`00ac0214`](#insn-00ac0214) → `00ca4f08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac021c`](#insn-00ac021c) → `00c62f90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ac0220`](#insn-00ac0220) → `00ca4f00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0220`](#insn-00ac0220) → `00ca4f08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0228`](#insn-00ac0228) → `00ca4f00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac022c`](#insn-00ac022c) → `00ca4f28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac022c`](#insn-00ac022c) → `00ca4f30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0230`](#insn-00ac0230) → `00ca4f20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0234`](#insn-00ac0234) → `00ca4f10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0234`](#insn-00ac0234) → `00ca4f18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0234`](#insn-00ac0234) → `00ca4f20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ac0238`](#insn-00ac0238) → [`00c57e30`](../00c57/00c57e30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e30` · 推定シンボル `None` · 推定型 `None`
- [`00ac0240`](#insn-00ac0240) → `00ca4f38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ac0244`](#insn-00ac0244) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00ac0248`](#insn-00ac0248) → [`00abfe38`](#insn-00abfe38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0250`](#insn-00ac0250) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0258`](#insn-00ac0258) → [`00ac03a0`](#insn-00ac03a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0260`](#insn-00ac0260) → [`0049f3f0`](../0049f/0049f3f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0049f3f0` · 推定シンボル `None` · 推定型 `None`
- [`00ac0268`](#insn-00ac0268) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0270`](#insn-00ac0270) → [`00ac03a0`](#insn-00ac03a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0278`](#insn-00ac0278) → [`00ac0fe4`](../00ac0/00ac0fe4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac0fe4` · 推定シンボル `None` · 推定型 `None`
- [`00ac027c`](#insn-00ac027c) → [`00ac02ac`](#insn-00ac02ac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac02ac`](#insn-00ac02ac) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac02b4`](#insn-00ac02b4) → [`00ac0348`](#insn-00ac0348) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac02b8`](#insn-00ac02b8) → [`00ac0388`](#insn-00ac0388) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0348`](#insn-00ac0348) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac034c`](#insn-00ac034c) → [`00ac0384`](#insn-00ac0384) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0384`](#insn-00ac0384) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00ac038c`](#insn-00ac038c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac0394`](#insn-00ac0394) → [`00ac03a0`](#insn-00ac03a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac039c`](#insn-00ac039c) → [`00c53f5c`](../00c53/00c53f5c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53f5c` · 推定シンボル `None` · 推定型 `None`
- [`00ac03a0`](#insn-00ac03a0) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00abfaac`](#insn-00abfaac)

~~~json
{
  "source": "00abfaac",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfab0`](#insn-00abfab0)

~~~json
{
  "source": "00abfab0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfab4`](#insn-00abfab4)

~~~json
{
  "source": "00abfab4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfab8`](#insn-00abfab8)

~~~json
{
  "source": "00abfab8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfabc`](#insn-00abfabc)

~~~json
{
  "source": "00abfabc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfacc`](#insn-00abfacc)

~~~json
{
  "source": "00abfacc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfad8`](#insn-00abfad8)

~~~json
{
  "source": "00abfad8",
  "target": "00abffb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfae8`](#insn-00abfae8)

~~~json
{
  "source": "00abfae8",
  "target": "00ca4f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abfaf0`](#insn-00abfaf0)

~~~json
{
  "source": "00abfaf0",
  "target": "00ac00e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfb00`](#insn-00abfb00)

~~~json
{
  "source": "00abfb00",
  "target": "002ab9a4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ab9a4",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "6d6564616c5f6765743030302e706e6700",
  "capture_start": "002ab9a4",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abfb04`](#insn-00abfb04)

~~~json
{
  "source": "00abfb04",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfb14`](#insn-00abfb14)

~~~json
{
  "source": "00abfb14",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfb18`](#insn-00abfb18)

~~~json
{
  "source": "00abfb18",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfb20`](#insn-00abfb20)

~~~json
{
  "source": "00abfb20",
  "target": "002adb15",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002adb15",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6d6564616c5f6765743030302e696d6763757400",
  "capture_start": "002adb15",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abfb28`](#insn-00abfb28)

~~~json
{
  "source": "00abfb28",
  "target": "Stack[-0x5f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfb2c`](#insn-00abfb2c)

~~~json
{
  "source": "00abfb2c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfb30`](#insn-00abfb30)

~~~json
{
  "source": "00abfb30",
  "target": "Stack[-0x87]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfb34`](#insn-00abfb34)

~~~json
{
  "source": "00abfb34",
  "target": "Stack[-0x74]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfb4c`](#insn-00abfb4c)

~~~json
{
  "source": "00abfb4c",
  "target": "00ca4f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abfb54`](#insn-00abfb54)

~~~json
{
  "source": "00abfb54",
  "target": "0047e60c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfb58`](#insn-00abfb58)

~~~json
{
  "source": "00abfb58",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfb60`](#insn-00abfb60)

~~~json
{
  "source": "00abfb60",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfb68`](#insn-00abfb68)

~~~json
{
  "source": "00abfb68",
  "target": "00abfb7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfb74`](#insn-00abfb74)

~~~json
{
  "source": "00abfb74",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfb78`](#insn-00abfb78)

~~~json
{
  "source": "00abfb78",
  "target": "00abfbb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfb7c`](#insn-00abfb7c)

~~~json
{
  "source": "00abfb7c",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfb80`](#insn-00abfb80)

~~~json
{
  "source": "00abfb80",
  "target": "00abfb94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfb8c`](#insn-00abfb8c)

~~~json
{
  "source": "00abfb8c",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfb90`](#insn-00abfb90)

~~~json
{
  "source": "00abfb90",
  "target": "00abfbd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfb94`](#insn-00abfb94)

~~~json
{
  "source": "00abfb94",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfb98`](#insn-00abfb98)

~~~json
{
  "source": "00abfb98",
  "target": "00abfbf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfb9c`](#insn-00abfb9c)

~~~json
{
  "source": "00abfb9c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfba0`](#insn-00abfba0)

~~~json
{
  "source": "00abfba0",
  "target": "00abfc04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfba4`](#insn-00abfba4)

~~~json
{
  "source": "00abfba4",
  "target": "00ca4f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abfba8`](#insn-00abfba8)

~~~json
{
  "source": "00abfba8",
  "target": "00abfc14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfbac`](#insn-00abfbac)

~~~json
{
  "source": "00abfbac",
  "target": "00ac0138",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfbc4`](#insn-00abfbc4)

~~~json
{
  "source": "00abfbc4",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfbc8`](#insn-00abfbc8)

~~~json
{
  "source": "00abfbc8",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfbcc`](#insn-00abfbcc)

~~~json
{
  "source": "00abfbcc",
  "target": "00abfb84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfbd0`](#insn-00abfbd0)

~~~json
{
  "source": "00abfbd0",
  "target": "00abfb94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfbe8`](#insn-00abfbe8)

~~~json
{
  "source": "00abfbe8",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfbec`](#insn-00abfbec)

~~~json
{
  "source": "00abfbec",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfbf0`](#insn-00abfbf0)

~~~json
{
  "source": "00abfbf0",
  "target": "00abfb9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfbf4`](#insn-00abfbf4)

~~~json
{
  "source": "00abfbf4",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfbf8`](#insn-00abfbf8)

~~~json
{
  "source": "00abfbf8",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfbfc`](#insn-00abfbfc)

~~~json
{
  "source": "00abfbfc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfc00`](#insn-00abfc00)

~~~json
{
  "source": "00abfc00",
  "target": "00abfba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfc04`](#insn-00abfc04)

~~~json
{
  "source": "00abfc04",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfc08`](#insn-00abfc08)

~~~json
{
  "source": "00abfc08",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfc0c`](#insn-00abfc0c)

~~~json
{
  "source": "00abfc0c",
  "target": "00ca4f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abfc10`](#insn-00abfc10)

~~~json
{
  "source": "00abfc10",
  "target": "00ac0138",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfc24`](#insn-00abfc24)

~~~json
{
  "source": "00abfc24",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfc2c`](#insn-00abfc2c)

~~~json
{
  "source": "00abfc2c",
  "target": "002bb847",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bb847",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "6d6564616c5f253033642e706e6700",
  "capture_start": "002bb847",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abfc30`](#insn-00abfc30)

~~~json
{
  "source": "00abfc30",
  "target": "002bb84d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bb847",
  "offset": 6,
  "size": 15,
  "datatype": "string",
  "bytes": "6d6564616c5f253033642e706e6700",
  "capture_start": "002bb847",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abfc34`](#insn-00abfc34)

~~~json
{
  "source": "00abfc34",
  "target": "Stack[-0x79]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfc3c`](#insn-00abfc3c)

~~~json
{
  "source": "00abfc3c",
  "target": "Stack[-0x87]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfc40`](#insn-00abfc40)

~~~json
{
  "source": "00abfc40",
  "target": "Stack[-0x81]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfc44`](#insn-00abfc44)

~~~json
{
  "source": "00abfc44",
  "target": "00ac018c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfc58`](#insn-00abfc58)

~~~json
{
  "source": "00abfc58",
  "target": "00447ef4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfc68`](#insn-00abfc68)

~~~json
{
  "source": "00abfc68",
  "target": "002bcaee",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bcaee",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "6d6564616c5f3030312e696d6763757400",
  "capture_start": "002bcaee",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abfc6c`](#insn-00abfc6c)

~~~json
{
  "source": "00abfc6c",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfc70`](#insn-00abfc70)

~~~json
{
  "source": "00abfc70",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfc74`](#insn-00abfc74)

~~~json
{
  "source": "00abfc74",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfc8c`](#insn-00abfc8c)

~~~json
{
  "source": "00abfc8c",
  "target": "00ca4f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abfc94`](#insn-00abfc94)

~~~json
{
  "source": "00abfc94",
  "target": "0047e60c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfc98`](#insn-00abfc98)

~~~json
{
  "source": "00abfc98",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfca0`](#insn-00abfca0)

~~~json
{
  "source": "00abfca0",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfca8`](#insn-00abfca8)

~~~json
{
  "source": "00abfca8",
  "target": "00abfcbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfcb4`](#insn-00abfcb4)

~~~json
{
  "source": "00abfcb4",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfcb8`](#insn-00abfcb8)

~~~json
{
  "source": "00abfcb8",
  "target": "00abffe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfcbc`](#insn-00abfcbc)

~~~json
{
  "source": "00abfcbc",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfcc0`](#insn-00abfcc0)

~~~json
{
  "source": "00abfcc0",
  "target": "00abfcd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfccc`](#insn-00abfccc)

~~~json
{
  "source": "00abfccc",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfcd0`](#insn-00abfcd0)

~~~json
{
  "source": "00abfcd0",
  "target": "00ac0004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfcd4`](#insn-00abfcd4)

~~~json
{
  "source": "00abfcd4",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfcd8`](#insn-00abfcd8)

~~~json
{
  "source": "00abfcd8",
  "target": "00ac0024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfcdc`](#insn-00abfcdc)

~~~json
{
  "source": "00abfcdc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfce0`](#insn-00abfce0)

~~~json
{
  "source": "00abfce0",
  "target": "00ac0034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfce4`](#insn-00abfce4)

~~~json
{
  "source": "00abfce4",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfce8`](#insn-00abfce8)

~~~json
{
  "source": "00abfce8",
  "target": "00abfcf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfcec`](#insn-00abfcec)

~~~json
{
  "source": "00abfcec",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfcf0`](#insn-00abfcf0)

~~~json
{
  "source": "00abfcf0",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfd00`](#insn-00abfd00)

~~~json
{
  "source": "00abfd00",
  "target": "00abfe30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd04`](#insn-00abfd04)

~~~json
{
  "source": "00abfd04",
  "target": "00ca4f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abfd08`](#insn-00abfd08)

~~~json
{
  "source": "00abfd08",
  "target": "00ac01a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd18`](#insn-00abfd18)

~~~json
{
  "source": "00abfd18",
  "target": "002a1893",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a1893",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "6d6564616c5f7478743200",
  "capture_start": "002a1893",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abfd20`](#insn-00abfd20)

~~~json
{
  "source": "00abfd20",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd24`](#insn-00abfd24)

~~~json
{
  "source": "00abfd24",
  "target": "Stack[-0xb7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd28`](#insn-00abfd28)

~~~json
{
  "source": "00abfd28",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd2c`](#insn-00abfd2c)

~~~json
{
  "source": "00abfd2c",
  "target": "Stack[-0xb5]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd38`](#insn-00abfd38)

~~~json
{
  "source": "00abfd38",
  "target": "0048ce54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfd54`](#insn-00abfd54)

~~~json
{
  "source": "00abfd54",
  "target": "00447ef4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfd60`](#insn-00abfd60)

~~~json
{
  "source": "00abfd60",
  "target": "00ca4f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abfd64`](#insn-00abfd64)

~~~json
{
  "source": "00abfd64",
  "target": "00c9aca0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9aca0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abfd64`](#insn-00abfd64)

~~~json
{
  "source": "00abfd64",
  "target": "00ca4fd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4fd8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abfd80`](#insn-00abfd80)

~~~json
{
  "source": "00abfd80",
  "target": "0047e8dc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfd84`](#insn-00abfd84)

~~~json
{
  "source": "00abfd84",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd8c`](#insn-00abfd8c)

~~~json
{
  "source": "00abfd8c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfd94`](#insn-00abfd94)

~~~json
{
  "source": "00abfd94",
  "target": "00abfdc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfda0`](#insn-00abfda0)

~~~json
{
  "source": "00abfda0",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfda4`](#insn-00abfda4)

~~~json
{
  "source": "00abfda4",
  "target": "00abfdc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfdbc`](#insn-00abfdbc)

~~~json
{
  "source": "00abfdbc",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfdc0`](#insn-00abfdc0)

~~~json
{
  "source": "00abfdc0",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfdc4`](#insn-00abfdc4)

~~~json
{
  "source": "00abfdc4",
  "target": "00abfdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfdd0`](#insn-00abfdd0)

~~~json
{
  "source": "00abfdd0",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfdd4`](#insn-00abfdd4)

~~~json
{
  "source": "00abfdd4",
  "target": "00ac0048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfdd8`](#insn-00abfdd8)

~~~json
{
  "source": "00abfdd8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfddc`](#insn-00abfddc)

~~~json
{
  "source": "00abfddc",
  "target": "00ac0068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfde0`](#insn-00abfde0)

~~~json
{
  "source": "00abfde0",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfde4`](#insn-00abfde4)

~~~json
{
  "source": "00abfde4",
  "target": "00ac0078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfde8`](#insn-00abfde8)

~~~json
{
  "source": "00abfde8",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfdec`](#insn-00abfdec)

~~~json
{
  "source": "00abfdec",
  "target": "00abfdf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfdf0`](#insn-00abfdf0)

~~~json
{
  "source": "00abfdf0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfdf4`](#insn-00abfdf4)

~~~json
{
  "source": "00abfdf4",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfe04`](#insn-00abfe04)

~~~json
{
  "source": "00abfe04",
  "target": "002afefe",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002afefe",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6d6564616c5f6765743030322e6d61616e696d00",
  "capture_start": "002afefe",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abfe10`](#insn-00abfe10)

~~~json
{
  "source": "00abfe10",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe14`](#insn-00abfe14)

~~~json
{
  "source": "00abfe14",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe18`](#insn-00abfe18)

~~~json
{
  "source": "00abfe18",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe1c`](#insn-00abfe1c)

~~~json
{
  "source": "00abfe1c",
  "target": "Stack[-0x5c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe28`](#insn-00abfe28)

~~~json
{
  "source": "00abfe28",
  "target": "0046e970",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfe2c`](#insn-00abfe2c)

~~~json
{
  "source": "00abfe2c",
  "target": "00abffa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe30`](#insn-00abfe30)

~~~json
{
  "source": "00abfe30",
  "target": "00ca4f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abfe34`](#insn-00abfe34)

~~~json
{
  "source": "00abfe34",
  "target": "00ac01f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe44`](#insn-00abfe44)

~~~json
{
  "source": "00abfe44",
  "target": "002a189e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a189e",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "6d6564616c5f7478743100",
  "capture_start": "002a189e",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abfe4c`](#insn-00abfe4c)

~~~json
{
  "source": "00abfe4c",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe50`](#insn-00abfe50)

~~~json
{
  "source": "00abfe50",
  "target": "Stack[-0xb7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe54`](#insn-00abfe54)

~~~json
{
  "source": "00abfe54",
  "target": "Stack[-0xbf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe58`](#insn-00abfe58)

~~~json
{
  "source": "00abfe58",
  "target": "Stack[-0xb5]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe64`](#insn-00abfe64)

~~~json
{
  "source": "00abfe64",
  "target": "0048ce54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfe70`](#insn-00abfe70)

~~~json
{
  "source": "00abfe70",
  "target": "00ac024c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe84`](#insn-00abfe84)

~~~json
{
  "source": "00abfe84",
  "target": "00ac0264",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfe94`](#insn-00abfe94)

~~~json
{
  "source": "00abfe94",
  "target": "00abfeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfea0`](#insn-00abfea0)

~~~json
{
  "source": "00abfea0",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfea4`](#insn-00abfea4)

~~~json
{
  "source": "00abfea4",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfea8`](#insn-00abfea8)

~~~json
{
  "source": "00abfea8",
  "target": "00abfeb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfeb4`](#insn-00abfeb4)

~~~json
{
  "source": "00abfeb4",
  "target": "0043bb20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfec4`](#insn-00abfec4)

~~~json
{
  "source": "00abfec4",
  "target": "00492e08",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfed0`](#insn-00abfed0)

~~~json
{
  "source": "00abfed0",
  "target": "00ca4f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abfed4`](#insn-00abfed4)

~~~json
{
  "source": "00abfed4",
  "target": "00c9aca0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9aca0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00abfed4`](#insn-00abfed4)

~~~json
{
  "source": "00abfed4",
  "target": "00ca4fd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4fd8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00abfef0`](#insn-00abfef0)

~~~json
{
  "source": "00abfef0",
  "target": "0047e8dc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfef4`](#insn-00abfef4)

~~~json
{
  "source": "00abfef4",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfefc`](#insn-00abfefc)

~~~json
{
  "source": "00abfefc",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abff04`](#insn-00abff04)

~~~json
{
  "source": "00abff04",
  "target": "00abff30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abff10`](#insn-00abff10)

~~~json
{
  "source": "00abff10",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abff14`](#insn-00abff14)

~~~json
{
  "source": "00abff14",
  "target": "00abff30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abff2c`](#insn-00abff2c)

~~~json
{
  "source": "00abff2c",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abff30`](#insn-00abff30)

~~~json
{
  "source": "00abff30",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abff34`](#insn-00abff34)

~~~json
{
  "source": "00abff34",
  "target": "00abff48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abff40`](#insn-00abff40)

~~~json
{
  "source": "00abff40",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abff44`](#insn-00abff44)

~~~json
{
  "source": "00abff44",
  "target": "00ac008c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abff48`](#insn-00abff48)

~~~json
{
  "source": "00abff48",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abff4c`](#insn-00abff4c)

~~~json
{
  "source": "00abff4c",
  "target": "00ac00ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abff50`](#insn-00abff50)

~~~json
{
  "source": "00abff50",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abff54`](#insn-00abff54)

~~~json
{
  "source": "00abff54",
  "target": "00ac00bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abff58`](#insn-00abff58)

~~~json
{
  "source": "00abff58",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abff5c`](#insn-00abff5c)

~~~json
{
  "source": "00abff5c",
  "target": "00ac00cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abff60`](#insn-00abff60)

~~~json
{
  "source": "00abff60",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abff64`](#insn-00abff64)

~~~json
{
  "source": "00abff64",
  "target": "00abff70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abff68`](#insn-00abff68)

~~~json
{
  "source": "00abff68",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abff6c`](#insn-00abff6c)

~~~json
{
  "source": "00abff6c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abff7c`](#insn-00abff7c)

~~~json
{
  "source": "00abff7c",
  "target": "002b7bbd",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b7bbd",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6d6564616c5f6765743030312e6d61616e696d00",
  "capture_start": "002b7bbd",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abff88`](#insn-00abff88)

~~~json
{
  "source": "00abff88",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abff8c`](#insn-00abff8c)

~~~json
{
  "source": "00abff8c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abff90`](#insn-00abff90)

~~~json
{
  "source": "00abff90",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abff94`](#insn-00abff94)

~~~json
{
  "source": "00abff94",
  "target": "Stack[-0x5c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abffa0`](#insn-00abffa0)

~~~json
{
  "source": "00abffa0",
  "target": "0046e970",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abffa4`](#insn-00abffa4)

~~~json
{
  "source": "00abffa4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abffa8`](#insn-00abffa8)

~~~json
{
  "source": "00abffa8",
  "target": "00abffb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abffac`](#insn-00abffac)

~~~json
{
  "source": "00abffac",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abffb0`](#insn-00abffb0)

~~~json
{
  "source": "00abffb0",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abffb8`](#insn-00abffb8)

~~~json
{
  "source": "00abffb8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abffc0`](#insn-00abffc0)

~~~json
{
  "source": "00abffc0",
  "target": "00ac03a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abffc4`](#insn-00abffc4)

~~~json
{
  "source": "00abffc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abffc8`](#insn-00abffc8)

~~~json
{
  "source": "00abffc8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abffcc`](#insn-00abffcc)

~~~json
{
  "source": "00abffcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abffd0`](#insn-00abffd0)

~~~json
{
  "source": "00abffd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abffd4`](#insn-00abffd4)

~~~json
{
  "source": "00abffd4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfff4`](#insn-00abfff4)

~~~json
{
  "source": "00abfff4",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abfff8`](#insn-00abfff8)

~~~json
{
  "source": "00abfff8",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abfffc`](#insn-00abfffc)

~~~json
{
  "source": "00abfffc",
  "target": "00abfcc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0000`](#insn-00ac0000)

~~~json
{
  "source": "00ac0000",
  "target": "00abfcd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0018`](#insn-00ac0018)

~~~json
{
  "source": "00ac0018",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac001c`](#insn-00ac001c)

~~~json
{
  "source": "00ac001c",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0020`](#insn-00ac0020)

~~~json
{
  "source": "00ac0020",
  "target": "00abfcdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0024`](#insn-00ac0024)

~~~json
{
  "source": "00ac0024",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0028`](#insn-00ac0028)

~~~json
{
  "source": "00ac0028",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac002c`](#insn-00ac002c)

~~~json
{
  "source": "00ac002c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0030`](#insn-00ac0030)

~~~json
{
  "source": "00ac0030",
  "target": "00abfce4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0034`](#insn-00ac0034)

~~~json
{
  "source": "00ac0034",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0038`](#insn-00ac0038)

~~~json
{
  "source": "00ac0038",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac003c`](#insn-00ac003c)

~~~json
{
  "source": "00ac003c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0040`](#insn-00ac0040)

~~~json
{
  "source": "00ac0040",
  "target": "00abfcec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0044`](#insn-00ac0044)

~~~json
{
  "source": "00ac0044",
  "target": "00abfcf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac005c`](#insn-00ac005c)

~~~json
{
  "source": "00ac005c",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac0060`](#insn-00ac0060)

~~~json
{
  "source": "00ac0060",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0064`](#insn-00ac0064)

~~~json
{
  "source": "00ac0064",
  "target": "00abfde0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0068`](#insn-00ac0068)

~~~json
{
  "source": "00ac0068",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac006c`](#insn-00ac006c)

~~~json
{
  "source": "00ac006c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac0070`](#insn-00ac0070)

~~~json
{
  "source": "00ac0070",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0074`](#insn-00ac0074)

~~~json
{
  "source": "00ac0074",
  "target": "00abfde8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0078`](#insn-00ac0078)

~~~json
{
  "source": "00ac0078",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac007c`](#insn-00ac007c)

~~~json
{
  "source": "00ac007c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac0080`](#insn-00ac0080)

~~~json
{
  "source": "00ac0080",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0084`](#insn-00ac0084)

~~~json
{
  "source": "00ac0084",
  "target": "00abfdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0088`](#insn-00ac0088)

~~~json
{
  "source": "00ac0088",
  "target": "00abfdf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac00a0`](#insn-00ac00a0)

~~~json
{
  "source": "00ac00a0",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac00a4`](#insn-00ac00a4)

~~~json
{
  "source": "00ac00a4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac00a8`](#insn-00ac00a8)

~~~json
{
  "source": "00ac00a8",
  "target": "00abff50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac00ac`](#insn-00ac00ac)

~~~json
{
  "source": "00ac00ac",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac00b0`](#insn-00ac00b0)

~~~json
{
  "source": "00ac00b0",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac00b4`](#insn-00ac00b4)

~~~json
{
  "source": "00ac00b4",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac00b8`](#insn-00ac00b8)

~~~json
{
  "source": "00ac00b8",
  "target": "00abff58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac00bc`](#insn-00ac00bc)

~~~json
{
  "source": "00ac00bc",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac00c0`](#insn-00ac00c0)

~~~json
{
  "source": "00ac00c0",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac00c4`](#insn-00ac00c4)

~~~json
{
  "source": "00ac00c4",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac00c8`](#insn-00ac00c8)

~~~json
{
  "source": "00ac00c8",
  "target": "00abff60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac00cc`](#insn-00ac00cc)

~~~json
{
  "source": "00ac00cc",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac00d0`](#insn-00ac00d0)

~~~json
{
  "source": "00ac00d0",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac00d4`](#insn-00ac00d4)

~~~json
{
  "source": "00ac00d4",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac00d8`](#insn-00ac00d8)

~~~json
{
  "source": "00ac00d8",
  "target": "00abff68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac00dc`](#insn-00ac00dc)

~~~json
{
  "source": "00ac00dc",
  "target": "00abff70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac00e4`](#insn-00ac00e4)

~~~json
{
  "source": "00ac00e4",
  "target": "00ca4f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac00e8`](#insn-00ac00e8)

~~~json
{
  "source": "00ac00e8",
  "target": "00c57e50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac00ec`](#insn-00ac00ec)

~~~json
{
  "source": "00ac00ec",
  "target": "00abfaf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac00f4`](#insn-00ac00f4)

~~~json
{
  "source": "00ac00f4",
  "target": "00ca4f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac00fc`](#insn-00ac00fc)

~~~json
{
  "source": "00ac00fc",
  "target": "0047edb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac0108`](#insn-00ac0108)

~~~json
{
  "source": "00ac0108",
  "target": "00c62f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c62f90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ac010c`](#insn-00ac010c)

~~~json
{
  "source": "00ac010c",
  "target": "00ca4f08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0110`](#insn-00ac0110)

~~~json
{
  "source": "00ac0110",
  "target": "00ca4f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0110`](#insn-00ac0110)

~~~json
{
  "source": "00ac0110",
  "target": "00ca4f08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0118`](#insn-00ac0118)

~~~json
{
  "source": "00ac0118",
  "target": "00ca4f28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0118`](#insn-00ac0118)

~~~json
{
  "source": "00ac0118",
  "target": "00ca4f30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac011c`](#insn-00ac011c)

~~~json
{
  "source": "00ac011c",
  "target": "00ca4f20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0120`](#insn-00ac0120)

~~~json
{
  "source": "00ac0120",
  "target": "00ca4f10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0120`](#insn-00ac0120)

~~~json
{
  "source": "00ac0120",
  "target": "00ca4f18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0120`](#insn-00ac0120)

~~~json
{
  "source": "00ac0120",
  "target": "00ca4f20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0124`](#insn-00ac0124)

~~~json
{
  "source": "00ac0124",
  "target": "00c57e30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac012c`](#insn-00ac012c)

~~~json
{
  "source": "00ac012c",
  "target": "00ca4f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0130`](#insn-00ac0130)

~~~json
{
  "source": "00ac0130",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac0134`](#insn-00ac0134)

~~~json
{
  "source": "00ac0134",
  "target": "00abfaf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac013c`](#insn-00ac013c)

~~~json
{
  "source": "00ac013c",
  "target": "00ca4f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0140`](#insn-00ac0140)

~~~json
{
  "source": "00ac0140",
  "target": "00c57e50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac0144`](#insn-00ac0144)

~~~json
{
  "source": "00ac0144",
  "target": "00abfc14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0150`](#insn-00ac0150)

~~~json
{
  "source": "00ac0150",
  "target": "0047edb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac0154`](#insn-00ac0154)

~~~json
{
  "source": "00ac0154",
  "target": "00ca4f08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac015c`](#insn-00ac015c)

~~~json
{
  "source": "00ac015c",
  "target": "00c62f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c62f90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ac0160`](#insn-00ac0160)

~~~json
{
  "source": "00ac0160",
  "target": "00ca4f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0160`](#insn-00ac0160)

~~~json
{
  "source": "00ac0160",
  "target": "00ca4f08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0168`](#insn-00ac0168)

~~~json
{
  "source": "00ac0168",
  "target": "00ca4f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac016c`](#insn-00ac016c)

~~~json
{
  "source": "00ac016c",
  "target": "00ca4f28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac016c`](#insn-00ac016c)

~~~json
{
  "source": "00ac016c",
  "target": "00ca4f30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0170`](#insn-00ac0170)

~~~json
{
  "source": "00ac0170",
  "target": "00ca4f20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0174`](#insn-00ac0174)

~~~json
{
  "source": "00ac0174",
  "target": "00ca4f10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0174`](#insn-00ac0174)

~~~json
{
  "source": "00ac0174",
  "target": "00ca4f18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0174`](#insn-00ac0174)

~~~json
{
  "source": "00ac0174",
  "target": "00ca4f20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0178`](#insn-00ac0178)

~~~json
{
  "source": "00ac0178",
  "target": "00c57e30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac0180`](#insn-00ac0180)

~~~json
{
  "source": "00ac0180",
  "target": "00ca4f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0184`](#insn-00ac0184)

~~~json
{
  "source": "00ac0184",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac0188`](#insn-00ac0188)

~~~json
{
  "source": "00ac0188",
  "target": "00abfc14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
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
  "target": "00ac03a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac01a0`](#insn-00ac01a0)

~~~json
{
  "source": "00ac01a0",
  "target": "0049f3f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac01a8`](#insn-00ac01a8)

~~~json
{
  "source": "00ac01a8",
  "target": "00ca4f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac01ac`](#insn-00ac01ac)

~~~json
{
  "source": "00ac01ac",
  "target": "00c57e50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac01b0`](#insn-00ac01b0)

~~~json
{
  "source": "00ac01b0",
  "target": "00abfd0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac01bc`](#insn-00ac01bc)

~~~json
{
  "source": "00ac01bc",
  "target": "0047edb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac01c0`](#insn-00ac01c0)

~~~json
{
  "source": "00ac01c0",
  "target": "00ca4f08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac01c8`](#insn-00ac01c8)

~~~json
{
  "source": "00ac01c8",
  "target": "00c62f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c62f90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ac01cc`](#insn-00ac01cc)

~~~json
{
  "source": "00ac01cc",
  "target": "00ca4f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac01cc`](#insn-00ac01cc)

~~~json
{
  "source": "00ac01cc",
  "target": "00ca4f08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac01d4`](#insn-00ac01d4)

~~~json
{
  "source": "00ac01d4",
  "target": "00ca4f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac01d8`](#insn-00ac01d8)

~~~json
{
  "source": "00ac01d8",
  "target": "00ca4f28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac01d8`](#insn-00ac01d8)

~~~json
{
  "source": "00ac01d8",
  "target": "00ca4f30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac01dc`](#insn-00ac01dc)

~~~json
{
  "source": "00ac01dc",
  "target": "00ca4f20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac01e0`](#insn-00ac01e0)

~~~json
{
  "source": "00ac01e0",
  "target": "00ca4f10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac01e0`](#insn-00ac01e0)

~~~json
{
  "source": "00ac01e0",
  "target": "00ca4f18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac01e0`](#insn-00ac01e0)

~~~json
{
  "source": "00ac01e0",
  "target": "00ca4f20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac01e4`](#insn-00ac01e4)

~~~json
{
  "source": "00ac01e4",
  "target": "00c57e30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac01ec`](#insn-00ac01ec)

~~~json
{
  "source": "00ac01ec",
  "target": "00ca4f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac01f0`](#insn-00ac01f0)

~~~json
{
  "source": "00ac01f0",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac01f4`](#insn-00ac01f4)

~~~json
{
  "source": "00ac01f4",
  "target": "00abfd0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac01fc`](#insn-00ac01fc)

~~~json
{
  "source": "00ac01fc",
  "target": "00ca4f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0200`](#insn-00ac0200)

~~~json
{
  "source": "00ac0200",
  "target": "00c57e50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac0204`](#insn-00ac0204)

~~~json
{
  "source": "00ac0204",
  "target": "00abfe38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0210`](#insn-00ac0210)

~~~json
{
  "source": "00ac0210",
  "target": "0047edb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac0214`](#insn-00ac0214)

~~~json
{
  "source": "00ac0214",
  "target": "00ca4f08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac021c`](#insn-00ac021c)

~~~json
{
  "source": "00ac021c",
  "target": "00c62f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c62f90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ac0220`](#insn-00ac0220)

~~~json
{
  "source": "00ac0220",
  "target": "00ca4f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0220`](#insn-00ac0220)

~~~json
{
  "source": "00ac0220",
  "target": "00ca4f08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0228`](#insn-00ac0228)

~~~json
{
  "source": "00ac0228",
  "target": "00ca4f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac022c`](#insn-00ac022c)

~~~json
{
  "source": "00ac022c",
  "target": "00ca4f28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac022c`](#insn-00ac022c)

~~~json
{
  "source": "00ac022c",
  "target": "00ca4f30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0230`](#insn-00ac0230)

~~~json
{
  "source": "00ac0230",
  "target": "00ca4f20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0234`](#insn-00ac0234)

~~~json
{
  "source": "00ac0234",
  "target": "00ca4f10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0234`](#insn-00ac0234)

~~~json
{
  "source": "00ac0234",
  "target": "00ca4f18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0234`](#insn-00ac0234)

~~~json
{
  "source": "00ac0234",
  "target": "00ca4f20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0238`](#insn-00ac0238)

~~~json
{
  "source": "00ac0238",
  "target": "00c57e30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac0240`](#insn-00ac0240)

~~~json
{
  "source": "00ac0240",
  "target": "00ca4f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ac0244`](#insn-00ac0244)

~~~json
{
  "source": "00ac0244",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac0248`](#insn-00ac0248)

~~~json
{
  "source": "00ac0248",
  "target": "00abfe38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0250`](#insn-00ac0250)

~~~json
{
  "source": "00ac0250",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0258`](#insn-00ac0258)

~~~json
{
  "source": "00ac0258",
  "target": "00ac03a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0260`](#insn-00ac0260)

~~~json
{
  "source": "00ac0260",
  "target": "0049f3f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac0268`](#insn-00ac0268)

~~~json
{
  "source": "00ac0268",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0270`](#insn-00ac0270)

~~~json
{
  "source": "00ac0270",
  "target": "00ac03a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0278`](#insn-00ac0278)

~~~json
{
  "source": "00ac0278",
  "target": "00ac0fe4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac027c`](#insn-00ac027c)

~~~json
{
  "source": "00ac027c",
  "target": "00ac02ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac02ac`](#insn-00ac02ac)

~~~json
{
  "source": "00ac02ac",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac02b4`](#insn-00ac02b4)

~~~json
{
  "source": "00ac02b4",
  "target": "00ac0348",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac02b8`](#insn-00ac02b8)

~~~json
{
  "source": "00ac02b8",
  "target": "00ac0388",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0348`](#insn-00ac0348)

~~~json
{
  "source": "00ac0348",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac034c`](#insn-00ac034c)

~~~json
{
  "source": "00ac034c",
  "target": "00ac0384",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0384`](#insn-00ac0384)

~~~json
{
  "source": "00ac0384",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac038c`](#insn-00ac038c)

~~~json
{
  "source": "00ac038c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac0394`](#insn-00ac0394)

~~~json
{
  "source": "00ac0394",
  "target": "00ac03a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac039c`](#insn-00ac039c)

~~~json
{
  "source": "00ac039c",
  "target": "00c53f5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac03a0`](#insn-00ac03a0)

~~~json
{
  "source": "00ac03a0",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
