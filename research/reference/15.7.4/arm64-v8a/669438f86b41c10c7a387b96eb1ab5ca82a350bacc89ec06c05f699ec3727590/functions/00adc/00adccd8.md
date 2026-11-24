# 00adccd8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00adcc94`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adcc94.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0060.md#compare-5b2203330672dc0ebbfa476677c18973)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b3c6b0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c6b0.md) · 移動量 `+0x5f9d8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0055.md#compare-c27853d6780126c5a85f31d0eac11aa9)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adccd8",
  "name": "FUN_00adccd8",
  "size": 1448,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7a39cc9fd27b0d34aa56a95f69ad5a7106290940f2ac5fad8234b464ef6198d9",
  "source_text_sha256": "7a39cc9fd27b0d34aa56a95f69ad5a7106290940f2ac5fad8234b464ef6198d9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adccd8",
        "00add27b"
      ],
      [
        "00add324",
        "00add327"
      ]
    ],
    "bytes_sha256": "eee214f3e8e7ae2463419f7bc419a17c4ef1b35e97ebc13bfe9c5ad1eee8fa04",
    "instruction_count": 362,
    "instruction_bytes": 1448,
    "body_bytes": 1448,
    "indirect": 8,
    "unresolved": 8
  }
}
~~~

## 呼び出し元

- [0064b18c](../0064b/0064b18c.md)
- [00654084](../00654/00654084.md)
- [00829478](../00829/00829478.md)
- [0089d9f4](../0089d/0089d9f4.md)
- [008f2388](../008f2/008f2388.md)
- [0098b984](../0098b/0098b984.md)
- [00a04c2c](../00a04/00a04c2c.md)
- [00acddbc](../00acd/00acddbc.md)

## 呼び出し先

- [0045b734](../0045b/0045b734.md)
- [0045ba04](../0045b/0045ba04.md)
- [00469f7c](../00469/00469f7c.md)
- [007f8ecc](../007f8/007f8ecc.md)
- [0081f580](../0081f/0081f580.md)
- [00821cb4](../00821/00821cb4.md)
- [008321a8](../00832/008321a8.md)
- [00a618f4](../00a61/00a618f4.md)
- [00bd6e90](../00bd6/00bd6e90.md)
- [00bdafe0](../00bda/00bdafe0.md)
- [00bdb000](../00bdb/00bdb000.md)
- [00bdb020](../00bdb/00bdb020.md)
- [00bdb030](../00bdb/00bdb030.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)

## 関連文字列（未確認候補）

~~~text
"1.imgcut"
"5.imgcut"
"img005.imgcut"
"img005.png"
"img005_1.imgcut"
"img005_1.png"
"unlockpopup_Guide_1"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 8866 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */
/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00adccd8(undefined8 *param_1,undefined8 param_2)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  int iVar4;
  long lVar5;
  long *plVar6;
  long *plVar7;
  byte local_b8;
  undefined5 local_b7;
  undefined2 uStack_b2;
  char cStack_b0;
  undefined5 uStack_af;
  char cStack_aa;
  char cStack_a9;
  uint uStack_a8;
  uint uStack_a4;
  byte local_a0;
  undefined7 uStack_9f;
  char cStack_98;
  undefined2 uStack_97;
  undefined1 uStack_95;
  undefined1 uStack_94;
  undefined1 uStack_93;
  undefined2 uStack_92;
  void *local_90;
  undefined8 local_80;
  long *plStack_78;
  long local_68;
  
  lVar1 = tpidr_el0;
  local_68 = *(long *)(lVar1 + 0x28);
  *param_1 = &PTR_FUN_00bf7158;
  param_1[2] = 0;
  param_1[1] = 0;
  param_1[4] = 0;
  param_1[3] = 0;
  param_1[6] = 0;
  param_1[5] = 0;
  param_1[8] = 0;
  param_1[7] = 0;
  param_1[10] = 0;
  param_1[9] = 0;
  param_1[0xc] = 0;
  param_1[0xb] = 0;
  param_1[0xe] = 0;
  param_1[0xd] = 0;
  param_1[0x10] = 0;
  param_1[0xf] = 0;
  param_1[0x12] = 0;
  param_1[0x11] = 0;
  param_1[0x14] = 0;
  param_1[0x13] = 0;
  if (((DAT_00c25078 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00c25078), iVar4 != 0)) {
    DAT_00c25048 = 0;
    DAT_00c25040 = &DAT_00c25048;
    DAT_00c25068 = 0;
    DAT_00c25070 = 0;
    DAT_00c25060 = 0;
    DAT_00c25050 = 0;
    DAT_00c25058 = &DAT_00c25060;
    __cxa_atexit(FUN_0045bedc,&DAT_00c25040,&PTR_LOOP_00be5fd0);
    __cxa_guard_release(&DAT_00c25078);
  }
  uStack_95 = 0;
  local_a0 = 0x14;
  uStack_97 = 0x676e;
  local_b8 = 0x1a;
  uStack_9f = (undefined7)s_img005_png_002a9f34._0_8_;
  cStack_98 = SUB81(s_img005_png_002a9f34._0_8_,7);
  cStack_aa = 0;
  local_b7 = _DAT_0029ff5c;
  uStack_b2 = (undefined2)s_5_imgcut_0029ff61._0_3_;
  cStack_b0 = SUB31(s_5_imgcut_0029ff61._0_3_,2);
  uStack_af._0_1_ = s_5_imgcut_0029ff61[3];
  uStack_af._1_1_ = s_5_imgcut_0029ff61[4];
  uStack_af._2_1_ = s_5_imgcut_0029ff61[5];
  uStack_af._3_1_ = s_5_imgcut_0029ff61[6];
  uStack_af._4_1_ = s_5_imgcut_0029ff61[7];
  FUN_0045b734(&local_80,&DAT_00c25040,&local_a0,&local_b8,0x2601);
  plVar6 = plStack_78;
  uVar2 = local_80;
  plVar7 = (long *)param_1[2];
  local_80 = 0;
  plStack_78 = (long *)0x0;
  param_1[2] = plVar6;
  param_1[1] = uVar2;
  plVar6 = plStack_78;
  if ((plVar7 != (long *)0x0) &&
     (lVar5 = FUN_00bd6e90(0xffffffffffffffff,plVar7 + 1), plVar6 = plStack_78, lVar5 == 0)) {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
    plVar6 = plStack_78;
  }
  plStack_78 = plVar6;
  if ((plVar6 != (long *)0x0) &&
     (lVar5 = FUN_00bd6e90(0xffffffffffffffff,(long *)((long)plVar6 + 8)), lVar5 == 0)) {
    (**(code **)(*plVar6 + 0x10))(plVar6);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
  }
  if ((local_b8 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_a4,uStack_a8));
  }
  if ((local_a0 & 1) != 0) {
    _ZdlPv(local_90);
  }
  if (((DAT_00c25078 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00c25078), iVar4 != 0)) {
    DAT_00c25048 = 0;
    DAT_00c25040 = &DAT_00c25048;
    DAT_00c25068 = 0;
    DAT_00c25070 = 0;
    DAT_00c25060 = 0;
    DAT_00c25050 = 0;
    DAT_00c25058 = &DAT_00c25060;
    __cxa_atexit(FUN_0045bedc,&DAT_00c25040,&PTR_LOOP_00be5fd0);
    __cxa_guard_release(&DAT_00c25078);
  }
  uStack_93 = 0;
  local_a0 = 0x18;
  uStack_a8 = uStack_a8 & 0xffffff00;
  uStack_97 = 0x702e;
  uStack_95 = 0x6e;
  uStack_94 = 0x67;
  uStack_9f = (undefined7)s_img005_1_png_002973f7._0_8_;
  cStack_98 = SUB81(s_img005_1_png_002973f7._0_8_,7);
  local_b8 = 0x1e;
  local_b7 = (undefined5)_DAT_002ad230;
  uStack_b2 = (undefined2)((uint7)_DAT_002ad230 >> 0x28);
  cStack_b0 = s_1_imgcut_002ad237[0];
  uStack_af = (undefined5)s_1_imgcut_002ad237._1_7_;
  cStack_aa = SUB71(s_1_imgcut_002ad237._1_7_,5);
  cStack_a9 = SUB71(s_1_imgcut_002ad237._1_7_,6);
  FUN_0045b734(&local_80,&DAT_00c25040,&local_a0,&local_b8,0x2601);
  plVar6 = plStack_78;
  uVar2 = local_80;
  plVar7 = (long *)param_1[4];
  local_80 = 0;
  plStack_78 = (long *)0x0;
  param_1[4] = plVar6;
  param_1[3] = uVar2;
  plVar6 = plStack_78;
  if ((plVar7 != (long *)0x0) &&
     (lVar5 = FUN_00bd6e90(0xffffffffffffffff,plVar7 + 1), plVar6 = plStack_78, lVar5 == 0)) {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
    plVar6 = plStack_78;
  }
  plStack_78 = plVar6;
                    /* try { // try from 00adcf24 to 00bdd0bf has its CatchHandler @ 00adcf24
                       catch() { ... } // from try @ 00adcf24 with catch @ 00adcf24
                       catch() { ... } // from try @ 00add0c8 with catch @ 00adcf24 */
  if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00bd6e90(0xffffffffffffffff,plVar6 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar6 + 0x10))(plVar6);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
  }
  if ((local_b8 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_a4,uStack_a8));
  }
  if ((local_a0 & 1) != 0) {
    _ZdlPv(local_90);
  }
  iVar4 = FUN_00821cb4(param_2);
  if (iVar4 != 0x61) {
    FUN_008321a8(&local_a0,param_2);
    uVar3 = CONCAT26(uStack_92,
                     CONCAT15(uStack_93,
                              CONCAT14(uStack_94,CONCAT13(uStack_95,CONCAT21(uStack_97,cStack_98))))
                    );
    uVar2 = CONCAT71(uStack_9f,local_a0);
    plVar6 = (long *)param_1[6];
    local_a0 = 0;
    uStack_9f = 0;
    cStack_98 = '\0';
    uStack_97 = 0;
    uStack_95 = 0;
    uStack_94 = 0;
    uStack_93 = 0;
    uStack_92 = 0;
    param_1[6] = uVar3;
    param_1[5] = uVar2;
    if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00bd6e90(0xffffffffffffffff,plVar6 + 1), lVar5 == 0)
       ) {
      (**(code **)(*plVar6 + 0x10))(plVar6);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
    }
    plVar6 = (long *)CONCAT26(uStack_92,
                              CONCAT15(uStack_93,
                                       CONCAT14(uStack_94,
                                                CONCAT13(uStack_95,CONCAT21(uStack_97,cStack_98)))))
    ;
    if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00bd6e90(0xffffffffffffffff,plVar6 + 1), lVar5 == 0)
       ) {
      (**(code **)(*plVar6 + 0x10))(plVar6);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
    }
  }
  if (((DAT_00c25078 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00c25078), iVar4 != 0)) {
    DAT_00c25048 = 0;
    DAT_00c25040 = &DAT_00c25048;
    DAT_00c25068 = 0;
    DAT_00c25070 = 0;
    DAT_00c25060 = 0;
    DAT_00c25050 = 0;
    DAT_00c25058 = &DAT_00c25060;
    __cxa_atexit(FUN_0045bedc,&DAT_00c25040,&PTR_LOOP_00be5fd0);
    __cxa_guard_release(&DAT_00c25078);
  }
  local_b8 = 0x26;
  uStack_af = (undefined5)s_unlockpopup_Guide_1_0029dd3c._8_8_;
  cStack_aa = SUB81(s_unlockpopup_Guide_1_0029dd3c._8_8_,5);
  cStack_a9 = SUB81(s_unlockpopup_Guide_1_0029dd3c._8_8_,6);
  uStack_a8 = CONCAT31(0x315f65,SUB81(s_unlockpopup_Guide_1_0029dd3c._8_8_,7));
  local_b7 = (undefined5)s_unlockpopup_Guide_1_0029dd3c._0_8_;
  uStack_b2 = SUB82(s_unlockpopup_Guide_1_0029dd3c._0_8_,5);
  cStack_b0 = SUB81(s_unlockpopup_Guide_1_0029dd3c._0_8_,7);
  uStack_a4 = uStack_a4 & 0xffffff00;
  FUN_00469f7c(&local_a0,&local_b8);
  FUN_0045ba04(&local_80,&DAT_00c25040,&local_a0,PTR_DAT_00c1aeb0,0x14,0,0,0);
  plVar6 = plStack_78;
  uVar2 = local_80;
  plVar7 = (long *)param_1[8];
  local_80 = 0;
  plStack_78 = (long *)0x0;
  param_1[8] = plVar6;
  param_1[7] = uVar2;
  plVar6 = plStack_78;
  if ((plVar7 != (long *)0x0) &&
     (lVar5 = FUN_00bd6e90(0xffffffffffffffff,plVar7 + 1), plVar6 = plStack_78, lVar5 == 0)) {
    (**(code **)(*plVar7 + 0x10))(plVar7);
                    /* catch() { ... } // from try @ 00add0c0 with catch @ 00add148 */
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
    plVar6 = plStack_78;
  }
  plStack_78 = plVar6;
  if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00bd6e90(0xffffffffffffffff,plVar6 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar6 + 0x10))(plVar6);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
  }
  if ((local_a0 & 1) != 0) {
    _ZdlPv(local_90);
  }
  if ((local_b8 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_a4,uStack_a8));
  }
  lVar5 = FUN_0081f580();
  FUN_00a618f4(lVar5 + 0x1998,param_1);
  lVar5 = FUN_0081f580();
  FUN_007f8ecc(lVar5 + 0x3339a8,param_1);
                    /* try { // try from 00add0c0 to 00bdd0c7 has its CatchHandler @ 00add148 */
                    /* try { // try from 00add0c8 to 00bdd173 has its CatchHandler @ 00adcf24 */
  if (*(long *)(lVar1 + 0x28) == local_68) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00adccd8"></a> `00adccd8` | `ff 03 03 d1` | sub sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00adccdc"></a> `00adccdc` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00adcce0"></a> `00adcce0` | `fc 6f 07 a9` | stp x28,x27,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00adcce4"></a> `00adcce4` | `fa 67 08 a9` | stp x26,x25,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00adcce8"></a> `00adcce8` | `f8 5f 09 a9` | stp x24,x23,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00adccec"></a> `00adccec` | `f6 57 0a a9` | stp x22,x21,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00adccf0"></a> `00adccf0` | `f4 4f 0b a9` | stp x20,x19,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00adccf4"></a> `00adccf4` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00adccf8"></a> `00adccf8` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00adccfc"></a> `00adccfc` | `5b d0 3b d5` | mrs x27,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00adcd00"></a> `00adcd00` | `c9 08 00 f0` | adrp x9,0xbf7000 | `FALL_THROUGH`
<a id="insn-00adcd04"></a> `00adcd04` | `29 61 05 91` | add x9,x9,#0x158 | `FALL_THROUGH`
<a id="insn-00adcd08"></a> `00adcd08` | `68 17 40 f9` | ldr x8,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-00adcd0c"></a> `00adcd0c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00adcd10"></a> `00adcd10` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00adcd14"></a> `00adcd14` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00adcd18"></a> `00adcd18` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00adcd1c"></a> `00adcd1c` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adcd20"></a> `00adcd20` | `5c 0a 00 b0` | adrp x28,0xc25000 | `FALL_THROUGH`
<a id="insn-00adcd24"></a> `00adcd24` | `9c e3 01 91` | add x28,x28,#0x78 | `FALL_THROUGH`
<a id="insn-00adcd28"></a> `00adcd28` | `09 00 00 f9` | str x9,[x0] | `FALL_THROUGH`
<a id="insn-00adcd2c"></a> `00adcd2c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00adcd30"></a> `00adcd30` | `f8 03 01 aa` | mov x24,x1 | `FALL_THROUGH`
<a id="insn-00adcd34"></a> `00adcd34` | `60 8e 80 3c` | str q0,[x19, #0x8]! | `FALL_THROUGH`
<a id="insn-00adcd38"></a> `00adcd38` | `a0 8e 81 3c` | str q0,[x21, #0x18]! | `FALL_THROUGH`
<a id="insn-00adcd3c"></a> `00adcd3c` | `c0 8e 82 3c` | str q0,[x22, #0x28]! | `FALL_THROUGH`
<a id="insn-00adcd40"></a> `00adcd40` | `e0 8e 83 3c` | str q0,[x23, #0x38]! | `FALL_THROUGH`
<a id="insn-00adcd44"></a> `00adcd44` | `00 80 84 3c` | stur q0,[x0, #0x48] | `FALL_THROUGH`
<a id="insn-00adcd48"></a> `00adcd48` | `00 80 85 3c` | stur q0,[x0, #0x58] | `FALL_THROUGH`
<a id="insn-00adcd4c"></a> `00adcd4c` | `00 80 86 3c` | stur q0,[x0, #0x68] | `FALL_THROUGH`
<a id="insn-00adcd50"></a> `00adcd50` | `00 80 87 3c` | stur q0,[x0, #0x78] | `FALL_THROUGH`
<a id="insn-00adcd54"></a> `00adcd54` | `00 80 88 3c` | stur q0,[x0, #0x88] | `FALL_THROUGH`
<a id="insn-00adcd58"></a> `00adcd58` | `00 80 89 3c` | stur q0,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00adcd5c"></a> `00adcd5c` | `88 ff df 08` | ldarb w8,[x28] | `FALL_THROUGH`
<a id="insn-00adcd60"></a> `00adcd60` | `e8 20 00 36` | tbz w8,#0x0,0x00add17c | `CONDITIONAL_JUMP`
<a id="insn-00adcd64"></a> `00adcd64` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-00adcd68"></a> `00adcd68` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-00adcd6c"></a> `00adcd6c` | `ff af 00 39` | strb wzr,[sp, #0x2b] | `FALL_THROUGH`
<a id="insn-00adcd70"></a> `00adcd70` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adcd74"></a> `00adcd74` | `68 be ff b0` | adrp x8,0x2a9000 | `FALL_THROUGH`
<a id="insn-00adcd78"></a> `00adcd78` | `08 d1 3c 91` | add x8,x8,#0xf34 | `FALL_THROUGH`
<a id="insn-00adcd7c"></a> `00adcd7c` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00adcd80"></a> `00adcd80` | `e9 93 02 78` | sturh w9,[sp, #0x29] | `FALL_THROUGH`
<a id="insn-00adcd84"></a> `00adcd84` | `49 03 80 52` | mov w9,#0x1a | `FALL_THROUGH`
<a id="insn-00adcd88"></a> `00adcd88` | `e9 23 00 39` | strb w9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adcd8c"></a> `00adcd8c` | `e8 13 02 f8` | stur x8,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00adcd90"></a> `00adcd90` | `08 be ff f0` | adrp x8,0x29f000 | `FALL_THROUGH`
<a id="insn-00adcd94"></a> `00adcd94` | `08 71 3d 91` | add x8,x8,#0xf5c | `FALL_THROUGH`
<a id="insn-00adcd98"></a> `00adcd98` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00adcd9c"></a> `00adcd9c` | `08 51 40 f8` | ldur x8,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-00adcda0"></a> `00adcda0` | `ff 5b 00 39` | strb wzr,[sp, #0x16] | `FALL_THROUGH`
<a id="insn-00adcda4"></a> `00adcda4` | `e9 93 00 f8` | stur x9,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-00adcda8"></a> `00adcda8` | `e8 e3 00 f8` | stur x8,[sp, #0xe] | `FALL_THROUGH`
<a id="insn-00adcdac"></a> `00adcdac` | `59 0a 00 b0` | adrp x25,0xc25000 | `FALL_THROUGH`
<a id="insn-00adcdb0"></a> `00adcdb0` | `39 03 01 91` | add x25,x25,#0x40 | `FALL_THROUGH`
<a id="insn-00adcdb4"></a> `00adcdb4` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00adcdb8"></a> `00adcdb8` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00adcdbc"></a> `00adcdbc` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adcdc0"></a> `00adcdc0` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00adcdc4"></a> `00adcdc4` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-00adcdc8"></a> `00adcdc8` | `5b fa e5 97` | bl 0x0045b734 | `UNCONDITIONAL_CALL`
<a id="insn-00adcdcc"></a> `00adcdcc` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00adcdd0"></a> `00adcdd0` | `9a 0a 40 f9` | ldr x26,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00adcdd4"></a> `00adcdd4` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00adcdd8"></a> `00adcdd8` | `80 82 80 3c` | stur q0,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00adcddc"></a> `00adcddc` | `ba 00 00 b4` | cbz x26,0x00adcdf0 | `CONDITIONAL_JUMP`
<a id="insn-00adcde0"></a> `00adcde0` | `41 23 00 91` | add x1,x26,#0x8 | `FALL_THROUGH`
<a id="insn-00adcde4"></a> `00adcde4` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00adcde8"></a> `00adcde8` | `2a e8 03 94` | bl 0x00bd6e90 | `UNCONDITIONAL_CALL`
<a id="insn-00adcdec"></a> `00adcdec` | `c0 01 00 b4` | cbz x0,0x00adce24 | `CONDITIONAL_JUMP`
<a id="insn-00adcdf0"></a> `00adcdf0` | `ba 83 5e f8` | ldur x26,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00adcdf4"></a> `00adcdf4` | `ba 00 00 b4` | cbz x26,0x00adce08 | `CONDITIONAL_JUMP`
<a id="insn-00adcdf8"></a> `00adcdf8` | `41 23 00 91` | add x1,x26,#0x8 | `FALL_THROUGH`
<a id="insn-00adcdfc"></a> `00adcdfc` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00adce00"></a> `00adce00` | `24 e8 03 94` | bl 0x00bd6e90 | `UNCONDITIONAL_CALL`
<a id="insn-00adce04"></a> `00adce04` | `20 02 00 b4` | cbz x0,0x00adce48 | `CONDITIONAL_JUMP`
<a id="insn-00adce08"></a> `00adce08` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adce0c"></a> `00adce0c` | `e8 02 00 37` | tbnz w8,#0x0,0x00adce68 | `CONDITIONAL_JUMP`
<a id="insn-00adce10"></a> `00adce10` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adce14"></a> `00adce14` | `28 03 00 37` | tbnz w8,#0x0,0x00adce78 | `CONDITIONAL_JUMP`
<a id="insn-00adce18"></a> `00adce18` | `88 ff df 08` | ldarb w8,[x28] | `FALL_THROUGH`
<a id="insn-00adce1c"></a> `00adce1c` | `68 03 00 37` | tbnz w8,#0x0,0x00adce88 | `CONDITIONAL_JUMP`
<a id="insn-00adce20"></a> `00adce20` | `ed 00 00 14` | b 0x00add1d4 | `UNCONDITIONAL_JUMP`
<a id="insn-00adce24"></a> `00adce24` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-00adce28"></a> `00adce28` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00adce2c"></a> `00adce2c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00adce30"></a> `00adce30` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adce34"></a> `00adce34` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00adce38"></a> `00adce38` | `7e f8 03 94` | bl 0x00bdb030 | `UNCONDITIONAL_CALL`
<a id="insn-00adce3c"></a> `00adce3c` | `ba 83 5e f8` | ldur x26,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00adce40"></a> `00adce40` | `da fd ff b5` | cbnz x26,0x00adcdf8 | `CONDITIONAL_JUMP`
<a id="insn-00adce44"></a> `00adce44` | `f1 ff ff 17` | b 0x00adce08 | `UNCONDITIONAL_JUMP`
<a id="insn-00adce48"></a> `00adce48` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-00adce4c"></a> `00adce4c` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00adce50"></a> `00adce50` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00adce54"></a> `00adce54` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adce58"></a> `00adce58` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00adce5c"></a> `00adce5c` | `75 f8 03 94` | bl 0x00bdb030 | `UNCONDITIONAL_CALL`
<a id="insn-00adce60"></a> `00adce60` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adce64"></a> `00adce64` | `68 fd 07 36` | tbz w8,#0x0,0x00adce10 | `CONDITIONAL_JUMP`
<a id="insn-00adce68"></a> `00adce68` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00adce6c"></a> `00adce6c` | `7d f8 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00adce70"></a> `00adce70` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adce74"></a> `00adce74` | `28 fd 07 36` | tbz w8,#0x0,0x00adce18 | `CONDITIONAL_JUMP`
<a id="insn-00adce78"></a> `00adce78` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adce7c"></a> `00adce7c` | `79 f8 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00adce80"></a> `00adce80` | `88 ff df 08` | ldarb w8,[x28] | `FALL_THROUGH`
<a id="insn-00adce84"></a> `00adce84` | `88 1a 00 36` | tbz w8,#0x0,0x00add1d4 | `CONDITIONAL_JUMP`
<a id="insn-00adce88"></a> `00adce88` | `08 03 80 52` | mov w8,#0x18 | `FALL_THROUGH`
<a id="insn-00adce8c"></a> `00adce8c` | `c9 05 8e 52` | mov w9,#0x702e | `FALL_THROUGH`
<a id="insn-00adce90"></a> `00adce90` | `ff b7 00 39` | strb wzr,[sp, #0x2d] | `FALL_THROUGH`
<a id="insn-00adce94"></a> `00adce94` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adce98"></a> `00adce98` | `c8 bd ff f0` | adrp x8,0x297000 | `FALL_THROUGH`
<a id="insn-00adce9c"></a> `00adce9c` | `08 dd 0f 91` | add x8,x8,#0x3f7 | `FALL_THROUGH`
<a id="insn-00adcea0"></a> `00adcea0` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00adcea4"></a> `00adcea4` | `c9 ed ac 72` | movk w9,#0x676e, LSL #16 | `FALL_THROUGH`
<a id="insn-00adcea8"></a> `00adcea8` | `ff 63 00 39` | strb wzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00adceac"></a> `00adceac` | `e9 93 02 b8` | stur w9,[sp, #0x29] | `FALL_THROUGH`
<a id="insn-00adceb0"></a> `00adceb0` | `c9 03 80 52` | mov w9,#0x1e | `FALL_THROUGH`
<a id="insn-00adceb4"></a> `00adceb4` | `e8 13 02 f8` | stur x8,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00adceb8"></a> `00adceb8` | `88 be ff b0` | adrp x8,0x2ad000 | `FALL_THROUGH`
<a id="insn-00adcebc"></a> `00adcebc` | `08 c1 08 91` | add x8,x8,#0x230 | `FALL_THROUGH`
<a id="insn-00adcec0"></a> `00adcec0` | `e9 23 00 39` | strb w9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adcec4"></a> `00adcec4` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00adcec8"></a> `00adcec8` | `08 71 40 f8` | ldur x8,[x8, #0x7] | `FALL_THROUGH`
<a id="insn-00adcecc"></a> `00adcecc` | `e9 93 00 f8` | stur x9,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-00adced0"></a> `00adced0` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adced4"></a> `00adced4` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00adced8"></a> `00adced8` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00adcedc"></a> `00adcedc` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adcee0"></a> `00adcee0` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00adcee4"></a> `00adcee4` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-00adcee8"></a> `00adcee8` | `13 fa e5 97` | bl 0x0045b734 | `UNCONDITIONAL_CALL`
<a id="insn-00adceec"></a> `00adceec` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00adcef0"></a> `00adcef0` | `9a 12 40 f9` | ldr x26,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00adcef4"></a> `00adcef4` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00adcef8"></a> `00adcef8` | `80 82 81 3c` | stur q0,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00adcefc"></a> `00adcefc` | `ba 00 00 b4` | cbz x26,0x00adcf10 | `CONDITIONAL_JUMP`
<a id="insn-00adcf00"></a> `00adcf00` | `41 23 00 91` | add x1,x26,#0x8 | `FALL_THROUGH`
<a id="insn-00adcf04"></a> `00adcf04` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00adcf08"></a> `00adcf08` | `e2 e7 03 94` | bl 0x00bd6e90 | `UNCONDITIONAL_CALL`
<a id="insn-00adcf0c"></a> `00adcf0c` | `00 0f 00 b4` | cbz x0,0x00add0ec | `CONDITIONAL_JUMP`
<a id="insn-00adcf10"></a> `00adcf10` | `ba 83 5e f8` | ldur x26,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00adcf14"></a> `00adcf14` | `ba 00 00 b4` | cbz x26,0x00adcf28 | `CONDITIONAL_JUMP`
<a id="insn-00adcf18"></a> `00adcf18` | `41 23 00 91` | add x1,x26,#0x8 | `FALL_THROUGH`
<a id="insn-00adcf1c"></a> `00adcf1c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00adcf20"></a> `00adcf20` | `dc e7 03 94` | bl 0x00bd6e90 | `UNCONDITIONAL_CALL`
<a id="insn-00adcf24"></a> `00adcf24` | `60 0f 00 b4` | cbz x0,0x00add110 | `CONDITIONAL_JUMP`
<a id="insn-00adcf28"></a> `00adcf28` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adcf2c"></a> `00adcf2c` | `68 00 00 36` | tbz w8,#0x0,0x00adcf38 | `CONDITIONAL_JUMP`
<a id="insn-00adcf30"></a> `00adcf30` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00adcf34"></a> `00adcf34` | `4b f8 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00adcf38"></a> `00adcf38` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adcf3c"></a> `00adcf3c` | `68 00 00 36` | tbz w8,#0x0,0x00adcf48 | `CONDITIONAL_JUMP`
<a id="insn-00adcf40"></a> `00adcf40` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adcf44"></a> `00adcf44` | `47 f8 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00adcf48"></a> `00adcf48` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00adcf4c"></a> `00adcf4c` | `5a 13 f5 97` | bl 0x00821cb4 | `UNCONDITIONAL_CALL`
<a id="insn-00adcf50"></a> `00adcf50` | `1f 84 01 71` | cmp w0,#0x61 | `FALL_THROUGH`
<a id="insn-00adcf54"></a> `00adcf54` | `e0 03 00 54` | b.eq 0x00adcfd0 | `CONDITIONAL_JUMP`
<a id="insn-00adcf58"></a> `00adcf58` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00adcf5c"></a> `00adcf5c` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00adcf60"></a> `00adcf60` | `92 54 f5 97` | bl 0x008321a8 | `UNCONDITIONAL_CALL`
<a id="insn-00adcf64"></a> `00adcf64` | `e0 0b c0 3d` | ldr q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adcf68"></a> `00adcf68` | `98 1a 40 f9` | ldr x24,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00adcf6c"></a> `00adcf6c` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adcf70"></a> `00adcf70` | `80 82 82 3c` | stur q0,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00adcf74"></a> `00adcf74` | `78 01 00 b4` | cbz x24,0x00adcfa0 | `CONDITIONAL_JUMP`
<a id="insn-00adcf78"></a> `00adcf78` | `01 23 00 91` | add x1,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00adcf7c"></a> `00adcf7c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00adcf80"></a> `00adcf80` | `c4 e7 03 94` | bl 0x00bd6e90 | `UNCONDITIONAL_CALL`
<a id="insn-00adcf84"></a> `00adcf84` | `e0 00 00 b5` | cbnz x0,0x00adcfa0 | `CONDITIONAL_JUMP`
<a id="insn-00adcf88"></a> `00adcf88` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00adcf8c"></a> `00adcf8c` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00adcf90"></a> `00adcf90` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00adcf94"></a> `00adcf94` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adcf98"></a> `00adcf98` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00adcf9c"></a> `00adcf9c` | `25 f8 03 94` | bl 0x00bdb030 | `UNCONDITIONAL_CALL`
<a id="insn-00adcfa0"></a> `00adcfa0` | `f8 17 40 f9` | ldr x24,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00adcfa4"></a> `00adcfa4` | `78 01 00 b4` | cbz x24,0x00adcfd0 | `CONDITIONAL_JUMP`
<a id="insn-00adcfa8"></a> `00adcfa8` | `01 23 00 91` | add x1,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00adcfac"></a> `00adcfac` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00adcfb0"></a> `00adcfb0` | `b8 e7 03 94` | bl 0x00bd6e90 | `UNCONDITIONAL_CALL`
<a id="insn-00adcfb4"></a> `00adcfb4` | `e0 00 00 b5` | cbnz x0,0x00adcfd0 | `CONDITIONAL_JUMP`
<a id="insn-00adcfb8"></a> `00adcfb8` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00adcfbc"></a> `00adcfbc` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00adcfc0"></a> `00adcfc0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00adcfc4"></a> `00adcfc4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adcfc8"></a> `00adcfc8` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00adcfcc"></a> `00adcfcc` | `19 f8 03 94` | bl 0x00bdb030 | `UNCONDITIONAL_CALL`
<a id="insn-00adcfd0"></a> `00adcfd0` | `88 ff df 08` | ldarb w8,[x28] | `FALL_THROUGH`
<a id="insn-00adcfd4"></a> `00adcfd4` | `a8 12 00 36` | tbz w8,#0x0,0x00add228 | `CONDITIONAL_JUMP`
<a id="insn-00adcfd8"></a> `00adcfd8` | `09 be ff b0` | adrp x9,0x29d000 | `FALL_THROUGH`
<a id="insn-00adcfdc"></a> `00adcfdc` | `29 f1 34 91` | add x9,x9,#0xd3c | `FALL_THROUGH`
<a id="insn-00adcfe0"></a> `00adcfe0` | `8a ac 8c 52` | mov w10,#0x6564 | `FALL_THROUGH`
<a id="insn-00adcfe4"></a> `00adcfe4` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00adcfe8"></a> `00adcfe8` | `c8 04 80 52` | mov w8,#0x26 | `FALL_THROUGH`
<a id="insn-00adcfec"></a> `00adcfec` | `ea 2b a6 72` | movk w10,#0x315f, LSL #16 | `FALL_THROUGH`
<a id="insn-00adcff0"></a> `00adcff0` | `e8 23 00 39` | strb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adcff4"></a> `00adcff4` | `ea 1b 00 b9` | str w10,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00adcff8"></a> `00adcff8` | `e0 93 80 3c` | stur q0,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-00adcffc"></a> `00adcffc` | `ff 73 00 39` | strb wzr,[sp, #0x1c] | `FALL_THROUGH`
<a id="insn-00add000"></a> `00add000` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00add004"></a> `00add004` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00add008"></a> `00add008` | `dd 33 e6 97` | bl 0x00469f7c | `UNCONDITIONAL_CALL`
<a id="insn-00add00c"></a> `00add00c` | `e2 09 00 b0` | adrp x2,0xc1a000 | `FALL_THROUGH`
<a id="insn-00add010"></a> `00add010` | `40 0a 00 90` | adrp x0,0xc25000 | `FALL_THROUGH`
<a id="insn-00add014"></a> `00add014` | `00 00 01 91` | add x0,x0,#0x40 | `FALL_THROUGH`
<a id="insn-00add018"></a> `00add018` | `42 58 47 f9` | ldr x2,[x2, #0xeb0] | `FALL_THROUGH`
<a id="insn-00add01c"></a> `00add01c` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00add020"></a> `00add020` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00add024"></a> `00add024` | `83 02 80 52` | mov w3,#0x14 | `FALL_THROUGH`
<a id="insn-00add028"></a> `00add028` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00add02c"></a> `00add02c` | `e5 03 1f 2a` | mov w5,wzr | `FALL_THROUGH`
<a id="insn-00add030"></a> `00add030` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-00add034"></a> `00add034` | `74 fa e5 97` | bl 0x0045ba04 | `UNCONDITIONAL_CALL`
<a id="insn-00add038"></a> `00add038` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00add03c"></a> `00add03c` | `98 22 40 f9` | ldr x24,[x20, #0x40] | `FALL_THROUGH`
<a id="insn-00add040"></a> `00add040` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00add044"></a> `00add044` | `80 82 83 3c` | stur q0,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00add048"></a> `00add048` | `b8 00 00 b4` | cbz x24,0x00add05c | `CONDITIONAL_JUMP`
<a id="insn-00add04c"></a> `00add04c` | `01 23 00 91` | add x1,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00add050"></a> `00add050` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00add054"></a> `00add054` | `8f e7 03 94` | bl 0x00bd6e90 | `UNCONDITIONAL_CALL`
<a id="insn-00add058"></a> `00add058` | `e0 06 00 b4` | cbz x0,0x00add134 | `CONDITIONAL_JUMP`
<a id="insn-00add05c"></a> `00add05c` | `b8 83 5e f8` | ldur x24,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00add060"></a> `00add060` | `b8 00 00 b4` | cbz x24,0x00add074 | `CONDITIONAL_JUMP`
<a id="insn-00add064"></a> `00add064` | `01 23 00 91` | add x1,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00add068"></a> `00add068` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00add06c"></a> `00add06c` | `89 e7 03 94` | bl 0x00bd6e90 | `UNCONDITIONAL_CALL`
<a id="insn-00add070"></a> `00add070` | `40 07 00 b4` | cbz x0,0x00add158 | `CONDITIONAL_JUMP`
<a id="insn-00add074"></a> `00add074` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00add078"></a> `00add078` | `68 00 00 36` | tbz w8,#0x0,0x00add084 | `CONDITIONAL_JUMP`
<a id="insn-00add07c"></a> `00add07c` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00add080"></a> `00add080` | `f8 f7 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00add084"></a> `00add084` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00add088"></a> `00add088` | `68 00 00 36` | tbz w8,#0x0,0x00add094 | `CONDITIONAL_JUMP`
<a id="insn-00add08c"></a> `00add08c` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00add090"></a> `00add090` | `f4 f7 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00add094"></a> `00add094` | `3b 09 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00add098"></a> `00add098` | `08 33 83 52` | mov w8,#0x1998 | `FALL_THROUGH`
<a id="insn-00add09c"></a> `00add09c` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00add0a0"></a> `00add0a0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00add0a4"></a> `00add0a4` | `14 12 fe 97` | bl 0x00a618f4 | `UNCONDITIONAL_CALL`
<a id="insn-00add0a8"></a> `00add0a8` | `36 09 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00add0ac"></a> `00add0ac` | `08 cc 4c 91` | add x8,x0,#0x333, LSL #12 | `FALL_THROUGH`
<a id="insn-00add0b0"></a> `00add0b0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00add0b4"></a> `00add0b4` | `00 a1 26 91` | add x0,x8,#0x9a8 | `FALL_THROUGH`
<a id="insn-00add0b8"></a> `00add0b8` | `85 6f f4 97` | bl 0x007f8ecc | `UNCONDITIONAL_CALL`
<a id="insn-00add0bc"></a> `00add0bc` | `68 17 40 f9` | ldr x8,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-00add0c0"></a> `00add0c0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00add0c4"></a> `00add0c4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00add0c8"></a> `00add0c8` | `e1 12 00 54` | b.ne 0x00add324 | `CONDITIONAL_JUMP`
<a id="insn-00add0cc"></a> `00add0cc` | `f4 4f 4b a9` | ldp x20,x19,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00add0d0"></a> `00add0d0` | `f6 57 4a a9` | ldp x22,x21,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00add0d4"></a> `00add0d4` | `f8 5f 49 a9` | ldp x24,x23,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00add0d8"></a> `00add0d8` | `fa 67 48 a9` | ldp x26,x25,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00add0dc"></a> `00add0dc` | `fc 6f 47 a9` | ldp x28,x27,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00add0e0"></a> `00add0e0` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00add0e4"></a> `00add0e4` | `ff 03 03 91` | add sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00add0e8"></a> `00add0e8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00add0ec"></a> `00add0ec` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-00add0f0"></a> `00add0f0` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00add0f4"></a> `00add0f4` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00add0f8"></a> `00add0f8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00add0fc"></a> `00add0fc` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00add100"></a> `00add100` | `cc f7 03 94` | bl 0x00bdb030 | `UNCONDITIONAL_CALL`
<a id="insn-00add104"></a> `00add104` | `ba 83 5e f8` | ldur x26,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00add108"></a> `00add108` | `9a f0 ff b5` | cbnz x26,0x00adcf18 | `CONDITIONAL_JUMP`
<a id="insn-00add10c"></a> `00add10c` | `87 ff ff 17` | b 0x00adcf28 | `UNCONDITIONAL_JUMP`
<a id="insn-00add110"></a> `00add110` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-00add114"></a> `00add114` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00add118"></a> `00add118` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00add11c"></a> `00add11c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00add120"></a> `00add120` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00add124"></a> `00add124` | `c3 f7 03 94` | bl 0x00bdb030 | `UNCONDITIONAL_CALL`
<a id="insn-00add128"></a> `00add128` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00add12c"></a> `00add12c` | `28 f0 07 37` | tbnz w8,#0x0,0x00adcf30 | `CONDITIONAL_JUMP`
<a id="insn-00add130"></a> `00add130` | `82 ff ff 17` | b 0x00adcf38 | `UNCONDITIONAL_JUMP`
<a id="insn-00add134"></a> `00add134` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00add138"></a> `00add138` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00add13c"></a> `00add13c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00add140"></a> `00add140` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00add144"></a> `00add144` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00add148"></a> `00add148` | `ba f7 03 94` | bl 0x00bdb030 | `UNCONDITIONAL_CALL`
<a id="insn-00add14c"></a> `00add14c` | `b8 83 5e f8` | ldur x24,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00add150"></a> `00add150` | `b8 f8 ff b5` | cbnz x24,0x00add064 | `CONDITIONAL_JUMP`
<a id="insn-00add154"></a> `00add154` | `c8 ff ff 17` | b 0x00add074 | `UNCONDITIONAL_JUMP`
<a id="insn-00add158"></a> `00add158` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00add15c"></a> `00add15c` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00add160"></a> `00add160` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00add164"></a> `00add164` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00add168"></a> `00add168` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00add16c"></a> `00add16c` | `b1 f7 03 94` | bl 0x00bdb030 | `UNCONDITIONAL_CALL`
<a id="insn-00add170"></a> `00add170` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00add174"></a> `00add174` | `48 f8 07 37` | tbnz w8,#0x0,0x00add07c | `CONDITIONAL_JUMP`
<a id="insn-00add178"></a> `00add178` | `c3 ff ff 17` | b 0x00add084 | `UNCONDITIONAL_JUMP`
<a id="insn-00add17c"></a> `00add17c` | `40 0a 00 90` | adrp x0,0xc25000 | `FALL_THROUGH`
<a id="insn-00add180"></a> `00add180` | `00 e0 01 91` | add x0,x0,#0x78 | `FALL_THROUGH`
<a id="insn-00add184"></a> `00add184` | `9f f7 03 94` | bl 0x00bdb000 | `UNCONDITIONAL_CALL`
<a id="insn-00add188"></a> `00add188` | `e0 de ff 34` | cbz w0,0x00adcd64 | `CONDITIONAL_JUMP`
<a id="insn-00add18c"></a> `00add18c` | `41 0a 00 90` | adrp x1,0xc25000 | `FALL_THROUGH`
<a id="insn-00add190"></a> `00add190` | `21 00 01 91` | add x1,x1,#0x40 | `FALL_THROUGH`
<a id="insn-00add194"></a> `00add194` | `e0 cb ff d0` | adrp x0,0x45b000 | `FALL_THROUGH`
<a id="insn-00add198"></a> `00add198` | `00 70 3b 91` | add x0,x0,#0xedc | `FALL_THROUGH`
<a id="insn-00add19c"></a> `00add19c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00add1a0"></a> `00add1a0` | `42 08 00 90` | adrp x2,0xbe5000 | `FALL_THROUGH`
<a id="insn-00add1a4"></a> `00add1a4` | `42 40 3f 91` | add x2,x2,#0xfd0 | `FALL_THROUGH`
<a id="insn-00add1a8"></a> `00add1a8` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00add1ac"></a> `00add1ac` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00add1b0"></a> `00add1b0` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00add1b4"></a> `00add1b4` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00add1b8"></a> `00add1b8` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00add1bc"></a> `00add1bc` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00add1c0"></a> `00add1c0` | `88 f7 03 94` | bl 0x00bdafe0 | `UNCONDITIONAL_CALL`
<a id="insn-00add1c4"></a> `00add1c4` | `40 0a 00 90` | adrp x0,0xc25000 | `FALL_THROUGH`
<a id="insn-00add1c8"></a> `00add1c8` | `00 e0 01 91` | add x0,x0,#0x78 | `FALL_THROUGH`
<a id="insn-00add1cc"></a> `00add1cc` | `95 f7 03 94` | bl 0x00bdb020 | `UNCONDITIONAL_CALL`
<a id="insn-00add1d0"></a> `00add1d0` | `e5 fe ff 17` | b 0x00adcd64 | `UNCONDITIONAL_JUMP`
<a id="insn-00add1d4"></a> `00add1d4` | `40 0a 00 90` | adrp x0,0xc25000 | `FALL_THROUGH`
<a id="insn-00add1d8"></a> `00add1d8` | `00 e0 01 91` | add x0,x0,#0x78 | `FALL_THROUGH`
<a id="insn-00add1dc"></a> `00add1dc` | `89 f7 03 94` | bl 0x00bdb000 | `UNCONDITIONAL_CALL`
<a id="insn-00add1e0"></a> `00add1e0` | `40 e5 ff 34` | cbz w0,0x00adce88 | `CONDITIONAL_JUMP`
<a id="insn-00add1e4"></a> `00add1e4` | `e8 03 19 aa` | mov x8,x25 | `FALL_THROUGH`
<a id="insn-00add1e8"></a> `00add1e8` | `e0 cb ff d0` | adrp x0,0x45b000 | `FALL_THROUGH`
<a id="insn-00add1ec"></a> `00add1ec` | `00 70 3b 91` | add x0,x0,#0xedc | `FALL_THROUGH`
<a id="insn-00add1f0"></a> `00add1f0` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00add1f4"></a> `00add1f4` | `42 08 00 90` | adrp x2,0xbe5000 | `FALL_THROUGH`
<a id="insn-00add1f8"></a> `00add1f8` | `42 40 3f 91` | add x2,x2,#0xfd0 | `FALL_THROUGH`
<a id="insn-00add1fc"></a> `00add1fc` | `28 03 00 f9` | str x8,[x25] | `FALL_THROUGH`
<a id="insn-00add200"></a> `00add200` | `e8 03 19 aa` | mov x8,x25 | `FALL_THROUGH`
<a id="insn-00add204"></a> `00add204` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00add208"></a> `00add208` | `3f ff 02 a9` | stp xzr,xzr,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00add20c"></a> `00add20c` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00add210"></a> `00add210` | `3f 23 01 a9` | stp xzr,x8,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00add214"></a> `00add214` | `73 f7 03 94` | bl 0x00bdafe0 | `UNCONDITIONAL_CALL`
<a id="insn-00add218"></a> `00add218` | `40 0a 00 90` | adrp x0,0xc25000 | `FALL_THROUGH`
<a id="insn-00add21c"></a> `00add21c` | `00 e0 01 91` | add x0,x0,#0x78 | `FALL_THROUGH`
<a id="insn-00add220"></a> `00add220` | `80 f7 03 94` | bl 0x00bdb020 | `UNCONDITIONAL_CALL`
<a id="insn-00add224"></a> `00add224` | `19 ff ff 17` | b 0x00adce88 | `UNCONDITIONAL_JUMP`
<a id="insn-00add228"></a> `00add228` | `40 0a 00 90` | adrp x0,0xc25000 | `FALL_THROUGH`
<a id="insn-00add22c"></a> `00add22c` | `00 e0 01 91` | add x0,x0,#0x78 | `FALL_THROUGH`
<a id="insn-00add230"></a> `00add230` | `74 f7 03 94` | bl 0x00bdb000 | `UNCONDITIONAL_CALL`
<a id="insn-00add234"></a> `00add234` | `20 ed ff 34` | cbz w0,0x00adcfd8 | `CONDITIONAL_JUMP`
<a id="insn-00add238"></a> `00add238` | `e8 03 19 aa` | mov x8,x25 | `FALL_THROUGH`
<a id="insn-00add23c"></a> `00add23c` | `e0 cb ff d0` | adrp x0,0x45b000 | `FALL_THROUGH`
<a id="insn-00add240"></a> `00add240` | `00 70 3b 91` | add x0,x0,#0xedc | `FALL_THROUGH`
<a id="insn-00add244"></a> `00add244` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00add248"></a> `00add248` | `42 08 00 90` | adrp x2,0xbe5000 | `FALL_THROUGH`
<a id="insn-00add24c"></a> `00add24c` | `42 40 3f 91` | add x2,x2,#0xfd0 | `FALL_THROUGH`
<a id="insn-00add250"></a> `00add250` | `28 03 00 f9` | str x8,[x25] | `FALL_THROUGH`
<a id="insn-00add254"></a> `00add254` | `e8 03 19 aa` | mov x8,x25 | `FALL_THROUGH`
<a id="insn-00add258"></a> `00add258` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00add25c"></a> `00add25c` | `3f ff 02 a9` | stp xzr,xzr,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00add260"></a> `00add260` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00add264"></a> `00add264` | `3f 23 01 a9` | stp xzr,x8,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00add268"></a> `00add268` | `5e f7 03 94` | bl 0x00bdafe0 | `UNCONDITIONAL_CALL`
<a id="insn-00add26c"></a> `00add26c` | `40 0a 00 90` | adrp x0,0xc25000 | `FALL_THROUGH`
<a id="insn-00add270"></a> `00add270` | `00 e0 01 91` | add x0,x0,#0x78 | `FALL_THROUGH`
<a id="insn-00add274"></a> `00add274` | `6b f7 03 94` | bl 0x00bdb020 | `UNCONDITIONAL_CALL`
<a id="insn-00add278"></a> `00add278` | `58 ff ff 17` | b 0x00adcfd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00add324"></a> `00add324` | `5b f7 03 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adccd8`](#insn-00adccd8) 範囲 `[['00adccd8', '00adcd63']]`
  - `CONDITIONAL_JUMP` [`00adcd60`](#insn-00adcd60) → [`00add17c`](#insn-00add17c)
  - `FALL_THROUGH` [`00adcd60`](#insn-00adcd60) → [`00adcd64`](#insn-00adcd64)
- ブロック [`00adcd64`](#insn-00adcd64) 範囲 `[['00adcd64', '00adcddf']]`
  - `CONDITIONAL_JUMP` [`00adcddc`](#insn-00adcddc) → [`00adcdf0`](#insn-00adcdf0)
  - `FALL_THROUGH` [`00adcddc`](#insn-00adcddc) → [`00adcde0`](#insn-00adcde0)
- ブロック [`00adcde0`](#insn-00adcde0) 範囲 `[['00adcde0', '00adcdef']]`
  - `CONDITIONAL_JUMP` [`00adcdec`](#insn-00adcdec) → [`00adce24`](#insn-00adce24)
  - `FALL_THROUGH` [`00adcdec`](#insn-00adcdec) → [`00adcdf0`](#insn-00adcdf0)
- ブロック [`00adcdf0`](#insn-00adcdf0) 範囲 `[['00adcdf0', '00adcdf7']]`
  - `CONDITIONAL_JUMP` [`00adcdf4`](#insn-00adcdf4) → [`00adce08`](#insn-00adce08)
  - `FALL_THROUGH` [`00adcdf4`](#insn-00adcdf4) → [`00adcdf8`](#insn-00adcdf8)
- ブロック [`00adcdf8`](#insn-00adcdf8) 範囲 `[['00adcdf8', '00adce07']]`
  - `CONDITIONAL_JUMP` [`00adce04`](#insn-00adce04) → [`00adce48`](#insn-00adce48)
  - `FALL_THROUGH` [`00adce04`](#insn-00adce04) → [`00adce08`](#insn-00adce08)
- ブロック [`00adce08`](#insn-00adce08) 範囲 `[['00adce08', '00adce0f']]`
  - `CONDITIONAL_JUMP` [`00adce0c`](#insn-00adce0c) → [`00adce68`](#insn-00adce68)
  - `FALL_THROUGH` [`00adce0c`](#insn-00adce0c) → [`00adce10`](#insn-00adce10)
- ブロック [`00adce10`](#insn-00adce10) 範囲 `[['00adce10', '00adce17']]`
  - `CONDITIONAL_JUMP` [`00adce14`](#insn-00adce14) → [`00adce78`](#insn-00adce78)
  - `FALL_THROUGH` [`00adce14`](#insn-00adce14) → [`00adce18`](#insn-00adce18)
- ブロック [`00adce18`](#insn-00adce18) 範囲 `[['00adce18', '00adce1f']]`
  - `CONDITIONAL_JUMP` [`00adce1c`](#insn-00adce1c) → [`00adce88`](#insn-00adce88)
  - `FALL_THROUGH` [`00adce1c`](#insn-00adce1c) → [`00adce20`](#insn-00adce20)
- ブロック [`00adce20`](#insn-00adce20) 範囲 `[['00adce20', '00adce23']]`
  - `UNCONDITIONAL_JUMP` [`00adce20`](#insn-00adce20) → [`00add1d4`](#insn-00add1d4)
- ブロック [`00adce24`](#insn-00adce24) 範囲 `[['00adce24', '00adce43']]`
  - `CONDITIONAL_JUMP` [`00adce40`](#insn-00adce40) → [`00adcdf8`](#insn-00adcdf8)
  - `FALL_THROUGH` [`00adce40`](#insn-00adce40) → [`00adce44`](#insn-00adce44)
- ブロック [`00adce44`](#insn-00adce44) 範囲 `[['00adce44', '00adce47']]`
  - `UNCONDITIONAL_JUMP` [`00adce44`](#insn-00adce44) → [`00adce08`](#insn-00adce08)
- ブロック [`00adce48`](#insn-00adce48) 範囲 `[['00adce48', '00adce67']]`
  - `CONDITIONAL_JUMP` [`00adce64`](#insn-00adce64) → [`00adce10`](#insn-00adce10)
  - `FALL_THROUGH` [`00adce64`](#insn-00adce64) → [`00adce68`](#insn-00adce68)
- ブロック [`00adce68`](#insn-00adce68) 範囲 `[['00adce68', '00adce77']]`
  - `CONDITIONAL_JUMP` [`00adce74`](#insn-00adce74) → [`00adce18`](#insn-00adce18)
  - `FALL_THROUGH` [`00adce74`](#insn-00adce74) → [`00adce78`](#insn-00adce78)
- ブロック [`00adce78`](#insn-00adce78) 範囲 `[['00adce78', '00adce87']]`
  - `CONDITIONAL_JUMP` [`00adce84`](#insn-00adce84) → [`00add1d4`](#insn-00add1d4)
  - `FALL_THROUGH` [`00adce84`](#insn-00adce84) → [`00adce88`](#insn-00adce88)
- ブロック [`00adce88`](#insn-00adce88) 範囲 `[['00adce88', '00adceff']]`
  - `CONDITIONAL_JUMP` [`00adcefc`](#insn-00adcefc) → [`00adcf10`](#insn-00adcf10)
  - `FALL_THROUGH` [`00adcefc`](#insn-00adcefc) → [`00adcf00`](#insn-00adcf00)
- ブロック [`00adcf00`](#insn-00adcf00) 範囲 `[['00adcf00', '00adcf0f']]`
  - `CONDITIONAL_JUMP` [`00adcf0c`](#insn-00adcf0c) → [`00add0ec`](#insn-00add0ec)
  - `FALL_THROUGH` [`00adcf0c`](#insn-00adcf0c) → [`00adcf10`](#insn-00adcf10)
- ブロック [`00adcf10`](#insn-00adcf10) 範囲 `[['00adcf10', '00adcf17']]`
  - `CONDITIONAL_JUMP` [`00adcf14`](#insn-00adcf14) → [`00adcf28`](#insn-00adcf28)
  - `FALL_THROUGH` [`00adcf14`](#insn-00adcf14) → [`00adcf18`](#insn-00adcf18)
- ブロック [`00adcf18`](#insn-00adcf18) 範囲 `[['00adcf18', '00adcf23']]`
  - `FALL_THROUGH` [`00adcf20`](#insn-00adcf20) → [`00adcf24`](#insn-00adcf24)
- ブロック [`00adcf24`](#insn-00adcf24) 範囲 `[['00adcf24', '00adcf27']]`
  - `CONDITIONAL_JUMP` [`00adcf24`](#insn-00adcf24) → [`00add110`](#insn-00add110)
  - `FALL_THROUGH` [`00adcf24`](#insn-00adcf24) → [`00adcf28`](#insn-00adcf28)
- ブロック [`00adcf28`](#insn-00adcf28) 範囲 `[['00adcf28', '00adcf2f']]`
  - `CONDITIONAL_JUMP` [`00adcf2c`](#insn-00adcf2c) → [`00adcf38`](#insn-00adcf38)
  - `FALL_THROUGH` [`00adcf2c`](#insn-00adcf2c) → [`00adcf30`](#insn-00adcf30)
- ブロック [`00adcf30`](#insn-00adcf30) 範囲 `[['00adcf30', '00adcf37']]`
  - `FALL_THROUGH` [`00adcf34`](#insn-00adcf34) → [`00adcf38`](#insn-00adcf38)
- ブロック [`00adcf38`](#insn-00adcf38) 範囲 `[['00adcf38', '00adcf3f']]`
  - `CONDITIONAL_JUMP` [`00adcf3c`](#insn-00adcf3c) → [`00adcf48`](#insn-00adcf48)
  - `FALL_THROUGH` [`00adcf3c`](#insn-00adcf3c) → [`00adcf40`](#insn-00adcf40)
- ブロック [`00adcf40`](#insn-00adcf40) 範囲 `[['00adcf40', '00adcf47']]`
  - `FALL_THROUGH` [`00adcf44`](#insn-00adcf44) → [`00adcf48`](#insn-00adcf48)
- ブロック [`00adcf48`](#insn-00adcf48) 範囲 `[['00adcf48', '00adcf57']]`
  - `CONDITIONAL_JUMP` [`00adcf54`](#insn-00adcf54) → [`00adcfd0`](#insn-00adcfd0)
  - `FALL_THROUGH` [`00adcf54`](#insn-00adcf54) → [`00adcf58`](#insn-00adcf58)
- ブロック [`00adcf58`](#insn-00adcf58) 範囲 `[['00adcf58', '00adcf77']]`
  - `CONDITIONAL_JUMP` [`00adcf74`](#insn-00adcf74) → [`00adcfa0`](#insn-00adcfa0)
  - `FALL_THROUGH` [`00adcf74`](#insn-00adcf74) → [`00adcf78`](#insn-00adcf78)
- ブロック [`00adcf78`](#insn-00adcf78) 範囲 `[['00adcf78', '00adcf87']]`
  - `CONDITIONAL_JUMP` [`00adcf84`](#insn-00adcf84) → [`00adcfa0`](#insn-00adcfa0)
  - `FALL_THROUGH` [`00adcf84`](#insn-00adcf84) → [`00adcf88`](#insn-00adcf88)
- ブロック [`00adcf88`](#insn-00adcf88) 範囲 `[['00adcf88', '00adcf9f']]`
  - `FALL_THROUGH` [`00adcf9c`](#insn-00adcf9c) → [`00adcfa0`](#insn-00adcfa0)
- ブロック [`00adcfa0`](#insn-00adcfa0) 範囲 `[['00adcfa0', '00adcfa7']]`
  - `CONDITIONAL_JUMP` [`00adcfa4`](#insn-00adcfa4) → [`00adcfd0`](#insn-00adcfd0)
  - `FALL_THROUGH` [`00adcfa4`](#insn-00adcfa4) → [`00adcfa8`](#insn-00adcfa8)
- ブロック [`00adcfa8`](#insn-00adcfa8) 範囲 `[['00adcfa8', '00adcfb7']]`
  - `CONDITIONAL_JUMP` [`00adcfb4`](#insn-00adcfb4) → [`00adcfd0`](#insn-00adcfd0)
  - `FALL_THROUGH` [`00adcfb4`](#insn-00adcfb4) → [`00adcfb8`](#insn-00adcfb8)
- ブロック [`00adcfb8`](#insn-00adcfb8) 範囲 `[['00adcfb8', '00adcfcf']]`
  - `FALL_THROUGH` [`00adcfcc`](#insn-00adcfcc) → [`00adcfd0`](#insn-00adcfd0)
- ブロック [`00adcfd0`](#insn-00adcfd0) 範囲 `[['00adcfd0', '00adcfd7']]`
  - `CONDITIONAL_JUMP` [`00adcfd4`](#insn-00adcfd4) → [`00add228`](#insn-00add228)
  - `FALL_THROUGH` [`00adcfd4`](#insn-00adcfd4) → [`00adcfd8`](#insn-00adcfd8)
- ブロック [`00adcfd8`](#insn-00adcfd8) 範囲 `[['00adcfd8', '00add04b']]`
  - `CONDITIONAL_JUMP` [`00add048`](#insn-00add048) → [`00add05c`](#insn-00add05c)
  - `FALL_THROUGH` [`00add048`](#insn-00add048) → [`00add04c`](#insn-00add04c)
- ブロック [`00add04c`](#insn-00add04c) 範囲 `[['00add04c', '00add05b']]`
  - `CONDITIONAL_JUMP` [`00add058`](#insn-00add058) → [`00add134`](#insn-00add134)
  - `FALL_THROUGH` [`00add058`](#insn-00add058) → [`00add05c`](#insn-00add05c)
- ブロック [`00add05c`](#insn-00add05c) 範囲 `[['00add05c', '00add063']]`
  - `CONDITIONAL_JUMP` [`00add060`](#insn-00add060) → [`00add074`](#insn-00add074)
  - `FALL_THROUGH` [`00add060`](#insn-00add060) → [`00add064`](#insn-00add064)
- ブロック [`00add064`](#insn-00add064) 範囲 `[['00add064', '00add073']]`
  - `CONDITIONAL_JUMP` [`00add070`](#insn-00add070) → [`00add158`](#insn-00add158)
  - `FALL_THROUGH` [`00add070`](#insn-00add070) → [`00add074`](#insn-00add074)
- ブロック [`00add074`](#insn-00add074) 範囲 `[['00add074', '00add07b']]`
  - `CONDITIONAL_JUMP` [`00add078`](#insn-00add078) → [`00add084`](#insn-00add084)
  - `FALL_THROUGH` [`00add078`](#insn-00add078) → [`00add07c`](#insn-00add07c)
- ブロック [`00add07c`](#insn-00add07c) 範囲 `[['00add07c', '00add083']]`
  - `FALL_THROUGH` [`00add080`](#insn-00add080) → [`00add084`](#insn-00add084)
- ブロック [`00add084`](#insn-00add084) 範囲 `[['00add084', '00add08b']]`
  - `CONDITIONAL_JUMP` [`00add088`](#insn-00add088) → [`00add094`](#insn-00add094)
  - `FALL_THROUGH` [`00add088`](#insn-00add088) → [`00add08c`](#insn-00add08c)
- ブロック [`00add08c`](#insn-00add08c) 範囲 `[['00add08c', '00add093']]`
  - `FALL_THROUGH` [`00add090`](#insn-00add090) → [`00add094`](#insn-00add094)
- ブロック [`00add094`](#insn-00add094) 範囲 `[['00add094', '00add0bf']]`
  - `FALL_THROUGH` [`00add0bc`](#insn-00add0bc) → [`00add0c0`](#insn-00add0c0)
- ブロック [`00add0c0`](#insn-00add0c0) 範囲 `[['00add0c0', '00add0c7']]`
  - `FALL_THROUGH` [`00add0c4`](#insn-00add0c4) → [`00add0c8`](#insn-00add0c8)
- ブロック [`00add0c8`](#insn-00add0c8) 範囲 `[['00add0c8', '00add0cb']]`
  - `CONDITIONAL_JUMP` [`00add0c8`](#insn-00add0c8) → [`00add324`](#insn-00add324)
  - `FALL_THROUGH` [`00add0c8`](#insn-00add0c8) → [`00add0cc`](#insn-00add0cc)
- ブロック [`00add0cc`](#insn-00add0cc) 範囲 `[['00add0cc', '00add0eb']]`
- ブロック [`00add0ec`](#insn-00add0ec) 範囲 `[['00add0ec', '00add10b']]`
  - `CONDITIONAL_JUMP` [`00add108`](#insn-00add108) → [`00adcf18`](#insn-00adcf18)
  - `FALL_THROUGH` [`00add108`](#insn-00add108) → [`00add10c`](#insn-00add10c)
- ブロック [`00add10c`](#insn-00add10c) 範囲 `[['00add10c', '00add10f']]`
  - `UNCONDITIONAL_JUMP` [`00add10c`](#insn-00add10c) → [`00adcf28`](#insn-00adcf28)
- ブロック [`00add110`](#insn-00add110) 範囲 `[['00add110', '00add12f']]`
  - `CONDITIONAL_JUMP` [`00add12c`](#insn-00add12c) → [`00adcf30`](#insn-00adcf30)
  - `FALL_THROUGH` [`00add12c`](#insn-00add12c) → [`00add130`](#insn-00add130)
- ブロック [`00add130`](#insn-00add130) 範囲 `[['00add130', '00add133']]`
  - `UNCONDITIONAL_JUMP` [`00add130`](#insn-00add130) → [`00adcf38`](#insn-00adcf38)
- ブロック [`00add134`](#insn-00add134) 範囲 `[['00add134', '00add147']]`
  - `FALL_THROUGH` [`00add144`](#insn-00add144) → [`00add148`](#insn-00add148)
- ブロック [`00add148`](#insn-00add148) 範囲 `[['00add148', '00add153']]`
  - `CONDITIONAL_JUMP` [`00add150`](#insn-00add150) → [`00add064`](#insn-00add064)
  - `FALL_THROUGH` [`00add150`](#insn-00add150) → [`00add154`](#insn-00add154)
- ブロック [`00add154`](#insn-00add154) 範囲 `[['00add154', '00add157']]`
  - `UNCONDITIONAL_JUMP` [`00add154`](#insn-00add154) → [`00add074`](#insn-00add074)
- ブロック [`00add158`](#insn-00add158) 範囲 `[['00add158', '00add177']]`
  - `CONDITIONAL_JUMP` [`00add174`](#insn-00add174) → [`00add07c`](#insn-00add07c)
  - `FALL_THROUGH` [`00add174`](#insn-00add174) → [`00add178`](#insn-00add178)
- ブロック [`00add178`](#insn-00add178) 範囲 `[['00add178', '00add17b']]`
  - `UNCONDITIONAL_JUMP` [`00add178`](#insn-00add178) → [`00add084`](#insn-00add084)
- ブロック [`00add17c`](#insn-00add17c) 範囲 `[['00add17c', '00add18b']]`
  - `CONDITIONAL_JUMP` [`00add188`](#insn-00add188) → [`00adcd64`](#insn-00adcd64)
  - `FALL_THROUGH` [`00add188`](#insn-00add188) → [`00add18c`](#insn-00add18c)
- ブロック [`00add18c`](#insn-00add18c) 範囲 `[['00add18c', '00add1d3']]`
  - `UNCONDITIONAL_JUMP` [`00add1d0`](#insn-00add1d0) → [`00adcd64`](#insn-00adcd64)
- ブロック [`00add1d4`](#insn-00add1d4) 範囲 `[['00add1d4', '00add1e3']]`
  - `CONDITIONAL_JUMP` [`00add1e0`](#insn-00add1e0) → [`00adce88`](#insn-00adce88)
  - `FALL_THROUGH` [`00add1e0`](#insn-00add1e0) → [`00add1e4`](#insn-00add1e4)
- ブロック [`00add1e4`](#insn-00add1e4) 範囲 `[['00add1e4', '00add227']]`
  - `UNCONDITIONAL_JUMP` [`00add224`](#insn-00add224) → [`00adce88`](#insn-00adce88)
- ブロック [`00add228`](#insn-00add228) 範囲 `[['00add228', '00add237']]`
  - `CONDITIONAL_JUMP` [`00add234`](#insn-00add234) → [`00adcfd8`](#insn-00adcfd8)
  - `FALL_THROUGH` [`00add234`](#insn-00add234) → [`00add238`](#insn-00add238)
- ブロック [`00add238`](#insn-00add238) 範囲 `[['00add238', '00add27b']]`
  - `UNCONDITIONAL_JUMP` [`00add278`](#insn-00add278) → [`00adcfd8`](#insn-00adcfd8)
- ブロック [`00add324`](#insn-00add324) 範囲 `[['00add324', '00add327']]`

## 命令位置別の参照

- [`00adccdc`](#insn-00adccdc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcce0`](#insn-00adcce0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcce4`](#insn-00adcce4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcce8`](#insn-00adcce8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adccec`](#insn-00adccec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adccf0`](#insn-00adccf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd1c`](#insn-00adcd1c) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd28`](#insn-00adcd28) → `00bf7158`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00adcd5c`](#insn-00adcd5c) → `00c25078`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00adcd60`](#insn-00adcd60) → [`00add17c`](#insn-00add17c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd6c`](#insn-00adcd6c) → `Stack[-0x95]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd70`](#insn-00adcd70) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd7c`](#insn-00adcd7c) → `002a9f34`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adcd80`](#insn-00adcd80) → `Stack[-0x97]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd88`](#insn-00adcd88) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd8c`](#insn-00adcd8c) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd98`](#insn-00adcd98) → `0029ff5c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd9c`](#insn-00adcd9c) → `0029ff61`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adcda0`](#insn-00adcda0) → `Stack[-0xaa]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcda4`](#insn-00adcda4) → `Stack[-0xb7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcda8`](#insn-00adcda8) → `Stack[-0xb2]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcdc0`](#insn-00adcdc0) → `00c25040`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adcdc8`](#insn-00adcdc8) → [`0045b734`](../0045b/0045b734.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045b734` · 推定シンボル `None` · 推定型 `None`
- [`00adcdcc`](#insn-00adcdcc) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcdd4`](#insn-00adcdd4) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcddc`](#insn-00adcddc) → [`00adcdf0`](#insn-00adcdf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcde8`](#insn-00adcde8) → [`00bd6e90`](../00bd6/00bd6e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e90` · 推定シンボル `None` · 推定型 `None`
- [`00adcdec`](#insn-00adcdec) → [`00adce24`](#insn-00adce24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcdf0`](#insn-00adcdf0) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcdf4`](#insn-00adcdf4) → [`00adce08`](#insn-00adce08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce00`](#insn-00adce00) → [`00bd6e90`](../00bd6/00bd6e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e90` · 推定シンボル `None` · 推定型 `None`
- [`00adce04`](#insn-00adce04) → [`00adce48`](#insn-00adce48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce08`](#insn-00adce08) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce0c`](#insn-00adce0c) → [`00adce68`](#insn-00adce68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce10`](#insn-00adce10) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce14`](#insn-00adce14) → [`00adce78`](#insn-00adce78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce18`](#insn-00adce18) → `00c25078`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00adce1c`](#insn-00adce1c) → [`00adce88`](#insn-00adce88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce20`](#insn-00adce20) → [`00add1d4`](#insn-00add1d4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce38`](#insn-00adce38) → [`00bdb030`](../00bdb/00bdb030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb030` · 推定シンボル `None` · 推定型 `None`
- [`00adce3c`](#insn-00adce3c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce40`](#insn-00adce40) → [`00adcdf8`](#insn-00adcdf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce44`](#insn-00adce44) → [`00adce08`](#insn-00adce08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce5c`](#insn-00adce5c) → [`00bdb030`](../00bdb/00bdb030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb030` · 推定シンボル `None` · 推定型 `None`
- [`00adce60`](#insn-00adce60) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce64`](#insn-00adce64) → [`00adce10`](#insn-00adce10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce68`](#insn-00adce68) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce6c`](#insn-00adce6c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00adce70`](#insn-00adce70) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce74`](#insn-00adce74) → [`00adce18`](#insn-00adce18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce78`](#insn-00adce78) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce7c`](#insn-00adce7c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00adce80`](#insn-00adce80) → `00c25078`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00adce84`](#insn-00adce84) → [`00add1d4`](#insn-00add1d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce90`](#insn-00adce90) → `Stack[-0x93]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce94`](#insn-00adce94) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcea0`](#insn-00adcea0) → `002973f7`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adcea8`](#insn-00adcea8) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adceac`](#insn-00adceac) → `Stack[-0x97]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adceb4`](#insn-00adceb4) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcec0`](#insn-00adcec0) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcec4`](#insn-00adcec4) → `002ad230`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcec8`](#insn-00adcec8) → `002ad237`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adcecc`](#insn-00adcecc) → `Stack[-0xb7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adced0`](#insn-00adced0) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcee0`](#insn-00adcee0) → `00c25040`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adcee8`](#insn-00adcee8) → [`0045b734`](../0045b/0045b734.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045b734` · 推定シンボル `None` · 推定型 `None`
- [`00adceec`](#insn-00adceec) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcef4`](#insn-00adcef4) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcefc`](#insn-00adcefc) → [`00adcf10`](#insn-00adcf10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf08`](#insn-00adcf08) → [`00bd6e90`](../00bd6/00bd6e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e90` · 推定シンボル `None` · 推定型 `None`
- [`00adcf0c`](#insn-00adcf0c) → [`00add0ec`](#insn-00add0ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf10`](#insn-00adcf10) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf14`](#insn-00adcf14) → [`00adcf28`](#insn-00adcf28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf20`](#insn-00adcf20) → [`00bd6e90`](../00bd6/00bd6e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e90` · 推定シンボル `None` · 推定型 `None`
- [`00adcf24`](#insn-00adcf24) → [`00add110`](#insn-00add110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf28`](#insn-00adcf28) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf2c`](#insn-00adcf2c) → [`00adcf38`](#insn-00adcf38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf30`](#insn-00adcf30) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf34`](#insn-00adcf34) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00adcf38`](#insn-00adcf38) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf3c`](#insn-00adcf3c) → [`00adcf48`](#insn-00adcf48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf40`](#insn-00adcf40) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf44`](#insn-00adcf44) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00adcf4c`](#insn-00adcf4c) → [`00821cb4`](../00821/00821cb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00821cb4` · 推定シンボル `None` · 推定型 `None`
- [`00adcf54`](#insn-00adcf54) → [`00adcfd0`](#insn-00adcfd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf60`](#insn-00adcf60) → [`008321a8`](../00832/008321a8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008321a8` · 推定シンボル `None` · 推定型 `None`
- [`00adcf64`](#insn-00adcf64) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf6c`](#insn-00adcf6c) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf74`](#insn-00adcf74) → [`00adcfa0`](#insn-00adcfa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf80`](#insn-00adcf80) → [`00bd6e90`](../00bd6/00bd6e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e90` · 推定シンボル `None` · 推定型 `None`
- [`00adcf84`](#insn-00adcf84) → [`00adcfa0`](#insn-00adcfa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf9c`](#insn-00adcf9c) → [`00bdb030`](../00bdb/00bdb030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb030` · 推定シンボル `None` · 推定型 `None`
- [`00adcfa0`](#insn-00adcfa0) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcfa4`](#insn-00adcfa4) → [`00adcfd0`](#insn-00adcfd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcfb0`](#insn-00adcfb0) → [`00bd6e90`](../00bd6/00bd6e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e90` · 推定シンボル `None` · 推定型 `None`
- [`00adcfb4`](#insn-00adcfb4) → [`00adcfd0`](#insn-00adcfd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcfcc`](#insn-00adcfcc) → [`00bdb030`](../00bdb/00bdb030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb030` · 推定シンボル `None` · 推定型 `None`
- [`00adcfd0`](#insn-00adcfd0) → `00c25078`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00adcfd4`](#insn-00adcfd4) → [`00add228`](#insn-00add228) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcfe4`](#insn-00adcfe4) → `0029dd3c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adcff0`](#insn-00adcff0) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcff4`](#insn-00adcff4) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcff8`](#insn-00adcff8) → `Stack[-0xb7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcffc`](#insn-00adcffc) → `Stack[-0xa4]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add008`](#insn-00add008) → [`00469f7c`](../00469/00469f7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469f7c` · 推定シンボル `None` · 推定型 `None`
- [`00add014`](#insn-00add014) → `00c25040`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add018`](#insn-00add018) → `00c1aeb0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00add018`](#insn-00add018) → `00c25118`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00add034`](#insn-00add034) → [`0045ba04`](../0045b/0045ba04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045ba04` · 推定シンボル `None` · 推定型 `None`
- [`00add038`](#insn-00add038) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add040`](#insn-00add040) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add048`](#insn-00add048) → [`00add05c`](#insn-00add05c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add054`](#insn-00add054) → [`00bd6e90`](../00bd6/00bd6e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e90` · 推定シンボル `None` · 推定型 `None`
- [`00add058`](#insn-00add058) → [`00add134`](#insn-00add134) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add05c`](#insn-00add05c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add060`](#insn-00add060) → [`00add074`](#insn-00add074) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add06c`](#insn-00add06c) → [`00bd6e90`](../00bd6/00bd6e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e90` · 推定シンボル `None` · 推定型 `None`
- [`00add070`](#insn-00add070) → [`00add158`](#insn-00add158) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add074`](#insn-00add074) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add078`](#insn-00add078) → [`00add084`](#insn-00add084) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add07c`](#insn-00add07c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add080`](#insn-00add080) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00add084`](#insn-00add084) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add088`](#insn-00add088) → [`00add094`](#insn-00add094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add08c`](#insn-00add08c) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add090`](#insn-00add090) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00add094`](#insn-00add094) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00add0a4`](#insn-00add0a4) → [`00a618f4`](../00a61/00a618f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a618f4` · 推定シンボル `None` · 推定型 `None`
- [`00add0a8`](#insn-00add0a8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00add0b8`](#insn-00add0b8) → [`007f8ecc`](../007f8/007f8ecc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007f8ecc` · 推定シンボル `None` · 推定型 `None`
- [`00add0c0`](#insn-00add0c0) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add0c8`](#insn-00add0c8) → [`00add324`](#insn-00add324) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add0cc`](#insn-00add0cc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add0d0`](#insn-00add0d0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add0d4`](#insn-00add0d4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add0d8`](#insn-00add0d8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add0dc`](#insn-00add0dc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add0e0`](#insn-00add0e0) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add100`](#insn-00add100) → [`00bdb030`](../00bdb/00bdb030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb030` · 推定シンボル `None` · 推定型 `None`
- [`00add104`](#insn-00add104) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add108`](#insn-00add108) → [`00adcf18`](#insn-00adcf18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add10c`](#insn-00add10c) → [`00adcf28`](#insn-00adcf28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add124`](#insn-00add124) → [`00bdb030`](../00bdb/00bdb030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb030` · 推定シンボル `None` · 推定型 `None`
- [`00add128`](#insn-00add128) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add12c`](#insn-00add12c) → [`00adcf30`](#insn-00adcf30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add130`](#insn-00add130) → [`00adcf38`](#insn-00adcf38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add148`](#insn-00add148) → [`00bdb030`](../00bdb/00bdb030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb030` · 推定シンボル `None` · 推定型 `None`
- [`00add14c`](#insn-00add14c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add150`](#insn-00add150) → [`00add064`](#insn-00add064) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add154`](#insn-00add154) → [`00add074`](#insn-00add074) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add16c`](#insn-00add16c) → [`00bdb030`](../00bdb/00bdb030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb030` · 推定シンボル `None` · 推定型 `None`
- [`00add170`](#insn-00add170) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add174`](#insn-00add174) → [`00add07c`](#insn-00add07c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add178`](#insn-00add178) → [`00add084`](#insn-00add084) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add180`](#insn-00add180) → `00c25078`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00add184`](#insn-00add184) → [`00bdb000`](../00bdb/00bdb000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb000` · 推定シンボル `None` · 推定型 `None`
- [`00add188`](#insn-00add188) → [`00adcd64`](#insn-00adcd64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add190`](#insn-00add190) → `00c25040`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add198`](#insn-00add198) → [`0045bedc`](../0045b/0045bedc.md) · `PARAM` · `ANALYSIS` · 関数 `0045bedc` · 推定シンボル `None` · 推定型 `None`
- [`00add1a4`](#insn-00add1a4) → `00be5fd0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00add1a8`](#insn-00add1a8) → `00c25048`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add1ac`](#insn-00add1ac) → `00c25040`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add1ac`](#insn-00add1ac) → `00c25048`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add1b4`](#insn-00add1b4) → `00c25068`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add1b4`](#insn-00add1b4) → `00c25070`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add1b8`](#insn-00add1b8) → `00c25060`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add1bc`](#insn-00add1bc) → `00c25050`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add1bc`](#insn-00add1bc) → `00c25058`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add1bc`](#insn-00add1bc) → `00c25060`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add1c0`](#insn-00add1c0) → [`00bdafe0`](../00bda/00bdafe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdafe0` · 推定シンボル `None` · 推定型 `None`
- [`00add1c8`](#insn-00add1c8) → `00c25078`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00add1cc`](#insn-00add1cc) → [`00bdb020`](../00bdb/00bdb020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb020` · 推定シンボル `None` · 推定型 `None`
- [`00add1d0`](#insn-00add1d0) → [`00adcd64`](#insn-00adcd64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add1d8`](#insn-00add1d8) → `00c25078`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00add1dc`](#insn-00add1dc) → [`00bdb000`](../00bdb/00bdb000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb000` · 推定シンボル `None` · 推定型 `None`
- [`00add1e0`](#insn-00add1e0) → [`00adce88`](#insn-00adce88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add1ec`](#insn-00add1ec) → [`0045bedc`](../0045b/0045bedc.md) · `PARAM` · `ANALYSIS` · 関数 `0045bedc` · 推定シンボル `None` · 推定型 `None`
- [`00add1f0`](#insn-00add1f0) → `00c25048`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add1f8`](#insn-00add1f8) → `00be5fd0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00add1fc`](#insn-00add1fc) → `00c25040`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add1fc`](#insn-00add1fc) → `00c25048`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add204`](#insn-00add204) → `00c25040`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add208`](#insn-00add208) → `00c25068`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add208`](#insn-00add208) → `00c25070`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add20c`](#insn-00add20c) → `00c25060`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add210`](#insn-00add210) → `00c25050`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add210`](#insn-00add210) → `00c25058`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add210`](#insn-00add210) → `00c25060`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add214`](#insn-00add214) → [`00bdafe0`](../00bda/00bdafe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdafe0` · 推定シンボル `None` · 推定型 `None`
- [`00add21c`](#insn-00add21c) → `00c25078`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00add220`](#insn-00add220) → [`00bdb020`](../00bdb/00bdb020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb020` · 推定シンボル `None` · 推定型 `None`
- [`00add224`](#insn-00add224) → [`00adce88`](#insn-00adce88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add22c`](#insn-00add22c) → `00c25078`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00add230`](#insn-00add230) → [`00bdb000`](../00bdb/00bdb000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb000` · 推定シンボル `None` · 推定型 `None`
- [`00add234`](#insn-00add234) → [`00adcfd8`](#insn-00adcfd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add240`](#insn-00add240) → [`0045bedc`](../0045b/0045bedc.md) · `PARAM` · `ANALYSIS` · 関数 `0045bedc` · 推定シンボル `None` · 推定型 `None`
- [`00add244`](#insn-00add244) → `00c25048`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add24c`](#insn-00add24c) → `00be5fd0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00add250`](#insn-00add250) → `00c25040`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add250`](#insn-00add250) → `00c25048`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add258`](#insn-00add258) → `00c25040`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add25c`](#insn-00add25c) → `00c25068`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add25c`](#insn-00add25c) → `00c25070`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add260`](#insn-00add260) → `00c25060`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add264`](#insn-00add264) → `00c25050`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add264`](#insn-00add264) → `00c25058`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add264`](#insn-00add264) → `00c25060`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add268`](#insn-00add268) → [`00bdafe0`](../00bda/00bdafe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdafe0` · 推定シンボル `None` · 推定型 `None`
- [`00add270`](#insn-00add270) → `00c25078`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00add274`](#insn-00add274) → [`00bdb020`](../00bdb/00bdb020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb020` · 推定シンボル `None` · 推定型 `None`
- [`00add278`](#insn-00add278) → [`00adcfd8`](#insn-00adcfd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add324`](#insn-00add324) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adccdc`](#insn-00adccdc)

~~~json
{
  "source": "00adccdc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcce0`](#insn-00adcce0)

~~~json
{
  "source": "00adcce0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcce4`](#insn-00adcce4)

~~~json
{
  "source": "00adcce4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcce8`](#insn-00adcce8)

~~~json
{
  "source": "00adcce8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adccec`](#insn-00adccec)

~~~json
{
  "source": "00adccec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adccf0`](#insn-00adccf0)

~~~json
{
  "source": "00adccf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd1c`](#insn-00adcd1c)

~~~json
{
  "source": "00adcd1c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd28`](#insn-00adcd28)

~~~json
{
  "source": "00adcd28",
  "target": "00bf7158",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00bf7158",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00adcd5c`](#insn-00adcd5c)

~~~json
{
  "source": "00adcd5c",
  "target": "00c25078",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25078",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adcd60`](#insn-00adcd60)

~~~json
{
  "source": "00adcd60",
  "target": "00add17c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd6c`](#insn-00adcd6c)

~~~json
{
  "source": "00adcd6c",
  "target": "Stack[-0x95]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd70`](#insn-00adcd70)

~~~json
{
  "source": "00adcd70",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd7c`](#insn-00adcd7c)

~~~json
{
  "source": "00adcd7c",
  "target": "002a9f34",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a9f34",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "696d673030352e706e6700",
  "capture_start": "002a9f34",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00adcd80`](#insn-00adcd80)

~~~json
{
  "source": "00adcd80",
  "target": "Stack[-0x97]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd88`](#insn-00adcd88)

~~~json
{
  "source": "00adcd88",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd8c`](#insn-00adcd8c)

~~~json
{
  "source": "00adcd8c",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd98`](#insn-00adcd98)

~~~json
{
  "source": "00adcd98",
  "target": "0029ff5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd9c`](#insn-00adcd9c)

~~~json
{
  "source": "00adcd9c",
  "target": "0029ff61",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029ff61",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "352e696d6763757400",
  "capture_start": "0029ff61",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00adcda0`](#insn-00adcda0)

~~~json
{
  "source": "00adcda0",
  "target": "Stack[-0xaa]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcda4`](#insn-00adcda4)

~~~json
{
  "source": "00adcda4",
  "target": "Stack[-0xb7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcda8`](#insn-00adcda8)

~~~json
{
  "source": "00adcda8",
  "target": "Stack[-0xb2]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcdc0`](#insn-00adcdc0)

~~~json
{
  "source": "00adcdc0",
  "target": "00c25040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25040",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adcdc8`](#insn-00adcdc8)

~~~json
{
  "source": "00adcdc8",
  "target": "0045b734",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcdcc`](#insn-00adcdcc)

~~~json
{
  "source": "00adcdcc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcdd4`](#insn-00adcdd4)

~~~json
{
  "source": "00adcdd4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcddc`](#insn-00adcddc)

~~~json
{
  "source": "00adcddc",
  "target": "00adcdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcde8`](#insn-00adcde8)

~~~json
{
  "source": "00adcde8",
  "target": "00bd6e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcdec`](#insn-00adcdec)

~~~json
{
  "source": "00adcdec",
  "target": "00adce24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcdf0`](#insn-00adcdf0)

~~~json
{
  "source": "00adcdf0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcdf4`](#insn-00adcdf4)

~~~json
{
  "source": "00adcdf4",
  "target": "00adce08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce00`](#insn-00adce00)

~~~json
{
  "source": "00adce00",
  "target": "00bd6e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adce04`](#insn-00adce04)

~~~json
{
  "source": "00adce04",
  "target": "00adce48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce08`](#insn-00adce08)

~~~json
{
  "source": "00adce08",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce0c`](#insn-00adce0c)

~~~json
{
  "source": "00adce0c",
  "target": "00adce68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce10`](#insn-00adce10)

~~~json
{
  "source": "00adce10",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce14`](#insn-00adce14)

~~~json
{
  "source": "00adce14",
  "target": "00adce78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce18`](#insn-00adce18)

~~~json
{
  "source": "00adce18",
  "target": "00c25078",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25078",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adce1c`](#insn-00adce1c)

~~~json
{
  "source": "00adce1c",
  "target": "00adce88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce20`](#insn-00adce20)

~~~json
{
  "source": "00adce20",
  "target": "00add1d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce38`](#insn-00adce38)

~~~json
{
  "source": "00adce38",
  "target": "00bdb030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adce3c`](#insn-00adce3c)

~~~json
{
  "source": "00adce3c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce40`](#insn-00adce40)

~~~json
{
  "source": "00adce40",
  "target": "00adcdf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce44`](#insn-00adce44)

~~~json
{
  "source": "00adce44",
  "target": "00adce08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce5c`](#insn-00adce5c)

~~~json
{
  "source": "00adce5c",
  "target": "00bdb030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adce60`](#insn-00adce60)

~~~json
{
  "source": "00adce60",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce64`](#insn-00adce64)

~~~json
{
  "source": "00adce64",
  "target": "00adce10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce68`](#insn-00adce68)

~~~json
{
  "source": "00adce68",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce6c`](#insn-00adce6c)

~~~json
{
  "source": "00adce6c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adce70`](#insn-00adce70)

~~~json
{
  "source": "00adce70",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce74`](#insn-00adce74)

~~~json
{
  "source": "00adce74",
  "target": "00adce18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce78`](#insn-00adce78)

~~~json
{
  "source": "00adce78",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce7c`](#insn-00adce7c)

~~~json
{
  "source": "00adce7c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adce80`](#insn-00adce80)

~~~json
{
  "source": "00adce80",
  "target": "00c25078",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25078",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adce84`](#insn-00adce84)

~~~json
{
  "source": "00adce84",
  "target": "00add1d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce90`](#insn-00adce90)

~~~json
{
  "source": "00adce90",
  "target": "Stack[-0x93]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce94`](#insn-00adce94)

~~~json
{
  "source": "00adce94",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcea0`](#insn-00adcea0)

~~~json
{
  "source": "00adcea0",
  "target": "002973f7",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002973f7",
  "offset": 0,
  "size": 13,
  "datatype": "string",
  "bytes": "696d673030355f312e706e6700",
  "capture_start": "002973f7",
  "capture_bytes": 13,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00adcea8`](#insn-00adcea8)

~~~json
{
  "source": "00adcea8",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adceac`](#insn-00adceac)

~~~json
{
  "source": "00adceac",
  "target": "Stack[-0x97]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adceb4`](#insn-00adceb4)

~~~json
{
  "source": "00adceb4",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcec0`](#insn-00adcec0)

~~~json
{
  "source": "00adcec0",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcec4`](#insn-00adcec4)

~~~json
{
  "source": "00adcec4",
  "target": "002ad230",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcec8`](#insn-00adcec8)

~~~json
{
  "source": "00adcec8",
  "target": "002ad237",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad237",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "312e696d6763757400",
  "capture_start": "002ad237",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00adcecc`](#insn-00adcecc)

~~~json
{
  "source": "00adcecc",
  "target": "Stack[-0xb7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adced0`](#insn-00adced0)

~~~json
{
  "source": "00adced0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcee0`](#insn-00adcee0)

~~~json
{
  "source": "00adcee0",
  "target": "00c25040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25040",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adcee8`](#insn-00adcee8)

~~~json
{
  "source": "00adcee8",
  "target": "0045b734",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adceec`](#insn-00adceec)

~~~json
{
  "source": "00adceec",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcef4`](#insn-00adcef4)

~~~json
{
  "source": "00adcef4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcefc`](#insn-00adcefc)

~~~json
{
  "source": "00adcefc",
  "target": "00adcf10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf08`](#insn-00adcf08)

~~~json
{
  "source": "00adcf08",
  "target": "00bd6e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcf0c`](#insn-00adcf0c)

~~~json
{
  "source": "00adcf0c",
  "target": "00add0ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf10`](#insn-00adcf10)

~~~json
{
  "source": "00adcf10",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf14`](#insn-00adcf14)

~~~json
{
  "source": "00adcf14",
  "target": "00adcf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf20`](#insn-00adcf20)

~~~json
{
  "source": "00adcf20",
  "target": "00bd6e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcf24`](#insn-00adcf24)

~~~json
{
  "source": "00adcf24",
  "target": "00add110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf28`](#insn-00adcf28)

~~~json
{
  "source": "00adcf28",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf2c`](#insn-00adcf2c)

~~~json
{
  "source": "00adcf2c",
  "target": "00adcf38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf30`](#insn-00adcf30)

~~~json
{
  "source": "00adcf30",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf34`](#insn-00adcf34)

~~~json
{
  "source": "00adcf34",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcf38`](#insn-00adcf38)

~~~json
{
  "source": "00adcf38",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf3c`](#insn-00adcf3c)

~~~json
{
  "source": "00adcf3c",
  "target": "00adcf48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf40`](#insn-00adcf40)

~~~json
{
  "source": "00adcf40",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf44`](#insn-00adcf44)

~~~json
{
  "source": "00adcf44",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcf4c`](#insn-00adcf4c)

~~~json
{
  "source": "00adcf4c",
  "target": "00821cb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcf54`](#insn-00adcf54)

~~~json
{
  "source": "00adcf54",
  "target": "00adcfd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf60`](#insn-00adcf60)

~~~json
{
  "source": "00adcf60",
  "target": "008321a8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcf64`](#insn-00adcf64)

~~~json
{
  "source": "00adcf64",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf6c`](#insn-00adcf6c)

~~~json
{
  "source": "00adcf6c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf74`](#insn-00adcf74)

~~~json
{
  "source": "00adcf74",
  "target": "00adcfa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf80`](#insn-00adcf80)

~~~json
{
  "source": "00adcf80",
  "target": "00bd6e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcf84`](#insn-00adcf84)

~~~json
{
  "source": "00adcf84",
  "target": "00adcfa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf9c`](#insn-00adcf9c)

~~~json
{
  "source": "00adcf9c",
  "target": "00bdb030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcfa0`](#insn-00adcfa0)

~~~json
{
  "source": "00adcfa0",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcfa4`](#insn-00adcfa4)

~~~json
{
  "source": "00adcfa4",
  "target": "00adcfd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcfb0`](#insn-00adcfb0)

~~~json
{
  "source": "00adcfb0",
  "target": "00bd6e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcfb4`](#insn-00adcfb4)

~~~json
{
  "source": "00adcfb4",
  "target": "00adcfd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcfcc`](#insn-00adcfcc)

~~~json
{
  "source": "00adcfcc",
  "target": "00bdb030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcfd0`](#insn-00adcfd0)

~~~json
{
  "source": "00adcfd0",
  "target": "00c25078",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25078",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adcfd4`](#insn-00adcfd4)

~~~json
{
  "source": "00adcfd4",
  "target": "00add228",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcfe4`](#insn-00adcfe4)

~~~json
{
  "source": "00adcfe4",
  "target": "0029dd3c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029dd3c",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "756e6c6f636b706f7075705f47756964655f3100",
  "capture_start": "0029dd3c",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00adcff0`](#insn-00adcff0)

~~~json
{
  "source": "00adcff0",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcff4`](#insn-00adcff4)

~~~json
{
  "source": "00adcff4",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcff8`](#insn-00adcff8)

~~~json
{
  "source": "00adcff8",
  "target": "Stack[-0xb7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcffc`](#insn-00adcffc)

~~~json
{
  "source": "00adcffc",
  "target": "Stack[-0xa4]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add008`](#insn-00add008)

~~~json
{
  "source": "00add008",
  "target": "00469f7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add014`](#insn-00add014)

~~~json
{
  "source": "00add014",
  "target": "00c25040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25040",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add018`](#insn-00add018)

~~~json
{
  "source": "00add018",
  "target": "00c1aeb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1aeb0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00add018`](#insn-00add018)

~~~json
{
  "source": "00add018",
  "target": "00c25118",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25118",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add034`](#insn-00add034)

~~~json
{
  "source": "00add034",
  "target": "0045ba04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add038`](#insn-00add038)

~~~json
{
  "source": "00add038",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add040`](#insn-00add040)

~~~json
{
  "source": "00add040",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add048`](#insn-00add048)

~~~json
{
  "source": "00add048",
  "target": "00add05c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add054`](#insn-00add054)

~~~json
{
  "source": "00add054",
  "target": "00bd6e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add058`](#insn-00add058)

~~~json
{
  "source": "00add058",
  "target": "00add134",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add05c`](#insn-00add05c)

~~~json
{
  "source": "00add05c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add060`](#insn-00add060)

~~~json
{
  "source": "00add060",
  "target": "00add074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add06c`](#insn-00add06c)

~~~json
{
  "source": "00add06c",
  "target": "00bd6e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add070`](#insn-00add070)

~~~json
{
  "source": "00add070",
  "target": "00add158",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add074`](#insn-00add074)

~~~json
{
  "source": "00add074",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add078`](#insn-00add078)

~~~json
{
  "source": "00add078",
  "target": "00add084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add07c`](#insn-00add07c)

~~~json
{
  "source": "00add07c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add080`](#insn-00add080)

~~~json
{
  "source": "00add080",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add084`](#insn-00add084)

~~~json
{
  "source": "00add084",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add088`](#insn-00add088)

~~~json
{
  "source": "00add088",
  "target": "00add094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add08c`](#insn-00add08c)

~~~json
{
  "source": "00add08c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add090`](#insn-00add090)

~~~json
{
  "source": "00add090",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add094`](#insn-00add094)

~~~json
{
  "source": "00add094",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add0a4`](#insn-00add0a4)

~~~json
{
  "source": "00add0a4",
  "target": "00a618f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add0a8`](#insn-00add0a8)

~~~json
{
  "source": "00add0a8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add0b8`](#insn-00add0b8)

~~~json
{
  "source": "00add0b8",
  "target": "007f8ecc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add0c0`](#insn-00add0c0)

~~~json
{
  "source": "00add0c0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add0c8`](#insn-00add0c8)

~~~json
{
  "source": "00add0c8",
  "target": "00add324",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add0cc`](#insn-00add0cc)

~~~json
{
  "source": "00add0cc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add0d0`](#insn-00add0d0)

~~~json
{
  "source": "00add0d0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add0d4`](#insn-00add0d4)

~~~json
{
  "source": "00add0d4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add0d8`](#insn-00add0d8)

~~~json
{
  "source": "00add0d8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add0dc`](#insn-00add0dc)

~~~json
{
  "source": "00add0dc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add0e0`](#insn-00add0e0)

~~~json
{
  "source": "00add0e0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add100`](#insn-00add100)

~~~json
{
  "source": "00add100",
  "target": "00bdb030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add104`](#insn-00add104)

~~~json
{
  "source": "00add104",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add108`](#insn-00add108)

~~~json
{
  "source": "00add108",
  "target": "00adcf18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add10c`](#insn-00add10c)

~~~json
{
  "source": "00add10c",
  "target": "00adcf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add124`](#insn-00add124)

~~~json
{
  "source": "00add124",
  "target": "00bdb030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add128`](#insn-00add128)

~~~json
{
  "source": "00add128",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add12c`](#insn-00add12c)

~~~json
{
  "source": "00add12c",
  "target": "00adcf30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add130`](#insn-00add130)

~~~json
{
  "source": "00add130",
  "target": "00adcf38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add148`](#insn-00add148)

~~~json
{
  "source": "00add148",
  "target": "00bdb030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add14c`](#insn-00add14c)

~~~json
{
  "source": "00add14c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add150`](#insn-00add150)

~~~json
{
  "source": "00add150",
  "target": "00add064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add154`](#insn-00add154)

~~~json
{
  "source": "00add154",
  "target": "00add074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add16c`](#insn-00add16c)

~~~json
{
  "source": "00add16c",
  "target": "00bdb030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add170`](#insn-00add170)

~~~json
{
  "source": "00add170",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add174`](#insn-00add174)

~~~json
{
  "source": "00add174",
  "target": "00add07c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add178`](#insn-00add178)

~~~json
{
  "source": "00add178",
  "target": "00add084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add180`](#insn-00add180)

~~~json
{
  "source": "00add180",
  "target": "00c25078",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25078",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add184`](#insn-00add184)

~~~json
{
  "source": "00add184",
  "target": "00bdb000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add188`](#insn-00add188)

~~~json
{
  "source": "00add188",
  "target": "00adcd64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add190`](#insn-00add190)

~~~json
{
  "source": "00add190",
  "target": "00c25040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25040",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add198`](#insn-00add198)

~~~json
{
  "source": "00add198",
  "target": "0045bedc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add1a4`](#insn-00add1a4)

~~~json
{
  "source": "00add1a4",
  "target": "00be5fd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be5fd0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00add1a8`](#insn-00add1a8)

~~~json
{
  "source": "00add1a8",
  "target": "00c25048",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25048",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add1ac`](#insn-00add1ac)

~~~json
{
  "source": "00add1ac",
  "target": "00c25040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25040",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add1ac`](#insn-00add1ac)

~~~json
{
  "source": "00add1ac",
  "target": "00c25048",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25048",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add1b4`](#insn-00add1b4)

~~~json
{
  "source": "00add1b4",
  "target": "00c25068",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25068",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add1b4`](#insn-00add1b4)

~~~json
{
  "source": "00add1b4",
  "target": "00c25070",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25070",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add1b8`](#insn-00add1b8)

~~~json
{
  "source": "00add1b8",
  "target": "00c25060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25060",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add1bc`](#insn-00add1bc)

~~~json
{
  "source": "00add1bc",
  "target": "00c25050",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25050",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add1bc`](#insn-00add1bc)

~~~json
{
  "source": "00add1bc",
  "target": "00c25058",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25058",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add1bc`](#insn-00add1bc)

~~~json
{
  "source": "00add1bc",
  "target": "00c25060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25060",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add1c0`](#insn-00add1c0)

~~~json
{
  "source": "00add1c0",
  "target": "00bdafe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add1c8`](#insn-00add1c8)

~~~json
{
  "source": "00add1c8",
  "target": "00c25078",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25078",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add1cc`](#insn-00add1cc)

~~~json
{
  "source": "00add1cc",
  "target": "00bdb020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add1d0`](#insn-00add1d0)

~~~json
{
  "source": "00add1d0",
  "target": "00adcd64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add1d8`](#insn-00add1d8)

~~~json
{
  "source": "00add1d8",
  "target": "00c25078",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25078",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add1dc`](#insn-00add1dc)

~~~json
{
  "source": "00add1dc",
  "target": "00bdb000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add1e0`](#insn-00add1e0)

~~~json
{
  "source": "00add1e0",
  "target": "00adce88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add1ec`](#insn-00add1ec)

~~~json
{
  "source": "00add1ec",
  "target": "0045bedc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add1f0`](#insn-00add1f0)

~~~json
{
  "source": "00add1f0",
  "target": "00c25048",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25048",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add1f8`](#insn-00add1f8)

~~~json
{
  "source": "00add1f8",
  "target": "00be5fd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be5fd0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00add1fc`](#insn-00add1fc)

~~~json
{
  "source": "00add1fc",
  "target": "00c25040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25040",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add1fc`](#insn-00add1fc)

~~~json
{
  "source": "00add1fc",
  "target": "00c25048",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25048",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add204`](#insn-00add204)

~~~json
{
  "source": "00add204",
  "target": "00c25040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25040",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add208`](#insn-00add208)

~~~json
{
  "source": "00add208",
  "target": "00c25068",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25068",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add208`](#insn-00add208)

~~~json
{
  "source": "00add208",
  "target": "00c25070",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25070",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add20c`](#insn-00add20c)

~~~json
{
  "source": "00add20c",
  "target": "00c25060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25060",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add210`](#insn-00add210)

~~~json
{
  "source": "00add210",
  "target": "00c25050",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25050",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add210`](#insn-00add210)

~~~json
{
  "source": "00add210",
  "target": "00c25058",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25058",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add210`](#insn-00add210)

~~~json
{
  "source": "00add210",
  "target": "00c25060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25060",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add214`](#insn-00add214)

~~~json
{
  "source": "00add214",
  "target": "00bdafe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add21c`](#insn-00add21c)

~~~json
{
  "source": "00add21c",
  "target": "00c25078",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25078",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add220`](#insn-00add220)

~~~json
{
  "source": "00add220",
  "target": "00bdb020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add224`](#insn-00add224)

~~~json
{
  "source": "00add224",
  "target": "00adce88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add22c`](#insn-00add22c)

~~~json
{
  "source": "00add22c",
  "target": "00c25078",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25078",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add230`](#insn-00add230)

~~~json
{
  "source": "00add230",
  "target": "00bdb000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add234`](#insn-00add234)

~~~json
{
  "source": "00add234",
  "target": "00adcfd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add240`](#insn-00add240)

~~~json
{
  "source": "00add240",
  "target": "0045bedc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add244`](#insn-00add244)

~~~json
{
  "source": "00add244",
  "target": "00c25048",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25048",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add24c`](#insn-00add24c)

~~~json
{
  "source": "00add24c",
  "target": "00be5fd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be5fd0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00add250`](#insn-00add250)

~~~json
{
  "source": "00add250",
  "target": "00c25040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25040",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add250`](#insn-00add250)

~~~json
{
  "source": "00add250",
  "target": "00c25048",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25048",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add258`](#insn-00add258)

~~~json
{
  "source": "00add258",
  "target": "00c25040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25040",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add25c`](#insn-00add25c)

~~~json
{
  "source": "00add25c",
  "target": "00c25068",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25068",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add25c`](#insn-00add25c)

~~~json
{
  "source": "00add25c",
  "target": "00c25070",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25070",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add260`](#insn-00add260)

~~~json
{
  "source": "00add260",
  "target": "00c25060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25060",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add264`](#insn-00add264)

~~~json
{
  "source": "00add264",
  "target": "00c25050",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25050",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add264`](#insn-00add264)

~~~json
{
  "source": "00add264",
  "target": "00c25058",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25058",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add264`](#insn-00add264)

~~~json
{
  "source": "00add264",
  "target": "00c25060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25060",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add268`](#insn-00add268)

~~~json
{
  "source": "00add268",
  "target": "00bdafe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add270`](#insn-00add270)

~~~json
{
  "source": "00add270",
  "target": "00c25078",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25078",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00add274`](#insn-00add274)

~~~json
{
  "source": "00add274",
  "target": "00bdb020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add278`](#insn-00add278)

~~~json
{
  "source": "00add278",
  "target": "00adcfd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add324`](#insn-00add324)

~~~json
{
  "source": "00add324",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
