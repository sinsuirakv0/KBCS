# 00adcbcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00adcc94`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adcc94.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-949feb6b9635387224e499ec74bf138b)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adcbcc",
  "name": "FUN_00adcbcc",
  "size": 1448,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "44d77b850e0969577c761c45562addc861708ae1f0212ae97540f0fc55e7d80b",
  "source_text_sha256": "44d77b850e0969577c761c45562addc861708ae1f0212ae97540f0fc55e7d80b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adcbcc",
        "00add16f"
      ],
      [
        "00add218",
        "00add21b"
      ]
    ],
    "bytes_sha256": "eb109c1ea0bdc445a4c11383cd84e1605c128483efcd37c3256c38aa828b62c7",
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
- [00a04be8](../00a04/00a04be8.md)
- [00acdcb0](../00acd/00acdcb0.md)

## 呼び出し先

- [0045b734](../0045b/0045b734.md)
- [0045ba04](../0045b/0045ba04.md)
- [00469f7c](../00469/00469f7c.md)
- [007f8ecc](../007f8/007f8ecc.md)
- [0081f580](../0081f/0081f580.md)
- [00821cb4](../00821/00821cb4.md)
- [008321a8](../00832/008321a8.md)
- [00a618b0](../00a61/00a618b0.md)
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

void FUN_00adcbcc(undefined8 *param_1,undefined8 param_2)

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
  *param_1 = &PTR_FUN_00bf7058;
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
                    /* try { // try from 00add07c to 00bdd083 has its CatchHandler @ 00add104 */
  if (((DAT_00c24f78 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00c24f78), iVar4 != 0)) {
                    /* try { // try from 00add084 to 00bdd12f has its CatchHandler @ 00adcee0 */
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
  uStack_95 = 0;
  local_a0 = 0x14;
  uStack_97 = 0x676e;
  local_b8 = 0x1a;
  uStack_9f = (undefined7)s_img005_png_002a9f2e._0_8_;
  cStack_98 = SUB81(s_img005_png_002a9f2e._0_8_,7);
  cStack_aa = 0;
  local_b7 = _DAT_0029fe44;
  uStack_b2 = (undefined2)s_5_imgcut_0029fe49._0_3_;
  cStack_b0 = SUB31(s_5_imgcut_0029fe49._0_3_,2);
  uStack_af._0_1_ = s_5_imgcut_0029fe49[3];
  uStack_af._1_1_ = s_5_imgcut_0029fe49[4];
  uStack_af._2_1_ = s_5_imgcut_0029fe49[5];
  uStack_af._3_1_ = s_5_imgcut_0029fe49[6];
  uStack_af._4_1_ = s_5_imgcut_0029fe49[7];
  FUN_0045b734(&local_80,&DAT_00c24f40,&local_a0,&local_b8,0x2601);
  plVar6 = plStack_78;
  uVar2 = local_80;
  plVar7 = (long *)param_1[2];
  local_80 = 0;
  plStack_78 = (long *)0x0;
  param_1[2] = plVar6;
  param_1[1] = uVar2;
  plVar6 = plStack_78;
  if ((plVar7 != (long *)0x0) &&
     (lVar5 = FUN_00bd6d90(0xffffffffffffffff,plVar7 + 1), plVar6 = plStack_78, lVar5 == 0)) {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
    plVar6 = plStack_78;
  }
  plStack_78 = plVar6;
  if ((plVar6 != (long *)0x0) &&
     (lVar5 = FUN_00bd6d90(0xffffffffffffffff,(long *)((long)plVar6 + 8)), lVar5 == 0)) {
    (**(code **)(*plVar6 + 0x10))(plVar6);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
  }
  if ((local_b8 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_a4,uStack_a8));
  }
  if ((local_a0 & 1) != 0) {
    _ZdlPv(local_90);
  }
  if (((DAT_00c24f78 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00c24f78), iVar4 != 0)) {
    DAT_00c24f48 = 0;
    DAT_00c24f40 = &DAT_00c24f48;
    DAT_00c24f68 = 0;
    DAT_00c24f70 = 0;
    DAT_00c24f60 = 0;
                    /* catch() { ... } // from try @ 00add07c with catch @ 00add104 */
    DAT_00c24f50 = 0;
    DAT_00c24f58 = &DAT_00c24f60;
    __cxa_atexit(FUN_0045bedc,&DAT_00c24f40,&PTR_LOOP_00be5ed0);
    __cxa_guard_release(&DAT_00c24f78);
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
  local_b7 = (undefined5)_DAT_002ad239;
  uStack_b2 = (undefined2)((uint7)_DAT_002ad239 >> 0x28);
  cStack_b0 = s_1_imgcut_002ad240[0];
  uStack_af = (undefined5)s_1_imgcut_002ad240._1_7_;
  cStack_aa = SUB71(s_1_imgcut_002ad240._1_7_,5);
  cStack_a9 = SUB71(s_1_imgcut_002ad240._1_7_,6);
  FUN_0045b734(&local_80,&DAT_00c24f40,&local_a0,&local_b8,0x2601);
  plVar6 = plStack_78;
  uVar2 = local_80;
  plVar7 = (long *)param_1[4];
  local_80 = 0;
  plStack_78 = (long *)0x0;
  param_1[4] = plVar6;
  param_1[3] = uVar2;
  plVar6 = plStack_78;
  if ((plVar7 != (long *)0x0) &&
     (lVar5 = FUN_00bd6d90(0xffffffffffffffff,plVar7 + 1), plVar6 = plStack_78, lVar5 == 0)) {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
    plVar6 = plStack_78;
  }
  plStack_78 = plVar6;
  if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00bd6d90(0xffffffffffffffff,plVar6 + 1), lVar5 == 0))
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
    if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00bd6d90(0xffffffffffffffff,plVar6 + 1), lVar5 == 0)
       ) {
      (**(code **)(*plVar6 + 0x10))(plVar6);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
    }
    plVar6 = (long *)CONCAT26(uStack_92,
                              CONCAT15(uStack_93,
                                       CONCAT14(uStack_94,
                                                CONCAT13(uStack_95,CONCAT21(uStack_97,cStack_98)))))
    ;
    if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00bd6d90(0xffffffffffffffff,plVar6 + 1), lVar5 == 0)
       ) {
      (**(code **)(*plVar6 + 0x10))(plVar6);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
    }
  }
  if (((DAT_00c24f78 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00c24f78), iVar4 != 0)) {
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
                    /* try { // try from 00adcee0 to 00bdd07b has its CatchHandler @ 00adcee0
                       catch() { ... } // from try @ 00adcee0 with catch @ 00adcee0
                       catch() { ... } // from try @ 00add084 with catch @ 00adcee0 */
  local_b8 = 0x26;
  uStack_af = (undefined5)s_unlockpopup_Guide_1_0029dc24._8_8_;
  cStack_aa = SUB81(s_unlockpopup_Guide_1_0029dc24._8_8_,5);
  cStack_a9 = SUB81(s_unlockpopup_Guide_1_0029dc24._8_8_,6);
  uStack_a8 = CONCAT31(0x315f65,SUB81(s_unlockpopup_Guide_1_0029dc24._8_8_,7));
  local_b7 = (undefined5)s_unlockpopup_Guide_1_0029dc24._0_8_;
  uStack_b2 = SUB82(s_unlockpopup_Guide_1_0029dc24._0_8_,5);
  cStack_b0 = SUB81(s_unlockpopup_Guide_1_0029dc24._0_8_,7);
  uStack_a4 = uStack_a4 & 0xffffff00;
  FUN_00469f7c(&local_a0,&local_b8);
  FUN_0045ba04(&local_80,&DAT_00c24f40,&local_a0,PTR_DAT_00c1adb0,0x14,0,0,0);
  plVar6 = plStack_78;
  uVar2 = local_80;
  plVar7 = (long *)param_1[8];
  local_80 = 0;
  plStack_78 = (long *)0x0;
  param_1[8] = plVar6;
  param_1[7] = uVar2;
  plVar6 = plStack_78;
  if ((plVar7 != (long *)0x0) &&
     (lVar5 = FUN_00bd6d90(0xffffffffffffffff,plVar7 + 1), plVar6 = plStack_78, lVar5 == 0)) {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
    plVar6 = plStack_78;
  }
  plStack_78 = plVar6;
  if ((plVar6 != (long *)0x0) && (lVar5 = FUN_00bd6d90(0xffffffffffffffff,plVar6 + 1), lVar5 == 0))
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
  FUN_00a618b0(lVar5 + 0x1998,param_1);
  lVar5 = FUN_0081f580();
  FUN_007f8ecc(lVar5 + 0x3339a8,param_1);
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
<a id="insn-00adcbcc"></a> `00adcbcc` | `ff 03 03 d1` | sub sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00adcbd0"></a> `00adcbd0` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00adcbd4"></a> `00adcbd4` | `fc 6f 07 a9` | stp x28,x27,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00adcbd8"></a> `00adcbd8` | `fa 67 08 a9` | stp x26,x25,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00adcbdc"></a> `00adcbdc` | `f8 5f 09 a9` | stp x24,x23,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00adcbe0"></a> `00adcbe0` | `f6 57 0a a9` | stp x22,x21,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00adcbe4"></a> `00adcbe4` | `f4 4f 0b a9` | stp x20,x19,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00adcbe8"></a> `00adcbe8` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00adcbec"></a> `00adcbec` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00adcbf0"></a> `00adcbf0` | `5b d0 3b d5` | mrs x27,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00adcbf4"></a> `00adcbf4` | `c9 08 00 f0` | adrp x9,0xbf7000 | `FALL_THROUGH`
<a id="insn-00adcbf8"></a> `00adcbf8` | `29 61 01 91` | add x9,x9,#0x58 | `FALL_THROUGH`
<a id="insn-00adcbfc"></a> `00adcbfc` | `68 17 40 f9` | ldr x8,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-00adcc00"></a> `00adcc00` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00adcc04"></a> `00adcc04` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00adcc08"></a> `00adcc08` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00adcc0c"></a> `00adcc0c` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00adcc10"></a> `00adcc10` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adcc14"></a> `00adcc14` | `5c 0a 00 90` | adrp x28,0xc24000 | `FALL_THROUGH`
<a id="insn-00adcc18"></a> `00adcc18` | `9c e3 3d 91` | add x28,x28,#0xf78 | `FALL_THROUGH`
<a id="insn-00adcc1c"></a> `00adcc1c` | `09 00 00 f9` | str x9,[x0] | `FALL_THROUGH`
<a id="insn-00adcc20"></a> `00adcc20` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00adcc24"></a> `00adcc24` | `f8 03 01 aa` | mov x24,x1 | `FALL_THROUGH`
<a id="insn-00adcc28"></a> `00adcc28` | `60 8e 80 3c` | str q0,[x19, #0x8]! | `FALL_THROUGH`
<a id="insn-00adcc2c"></a> `00adcc2c` | `a0 8e 81 3c` | str q0,[x21, #0x18]! | `FALL_THROUGH`
<a id="insn-00adcc30"></a> `00adcc30` | `c0 8e 82 3c` | str q0,[x22, #0x28]! | `FALL_THROUGH`
<a id="insn-00adcc34"></a> `00adcc34` | `e0 8e 83 3c` | str q0,[x23, #0x38]! | `FALL_THROUGH`
<a id="insn-00adcc38"></a> `00adcc38` | `00 80 84 3c` | stur q0,[x0, #0x48] | `FALL_THROUGH`
<a id="insn-00adcc3c"></a> `00adcc3c` | `00 80 85 3c` | stur q0,[x0, #0x58] | `FALL_THROUGH`
<a id="insn-00adcc40"></a> `00adcc40` | `00 80 86 3c` | stur q0,[x0, #0x68] | `FALL_THROUGH`
<a id="insn-00adcc44"></a> `00adcc44` | `00 80 87 3c` | stur q0,[x0, #0x78] | `FALL_THROUGH`
<a id="insn-00adcc48"></a> `00adcc48` | `00 80 88 3c` | stur q0,[x0, #0x88] | `FALL_THROUGH`
<a id="insn-00adcc4c"></a> `00adcc4c` | `00 80 89 3c` | stur q0,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00adcc50"></a> `00adcc50` | `88 ff df 08` | ldarb w8,[x28] | `FALL_THROUGH`
<a id="insn-00adcc54"></a> `00adcc54` | `e8 20 00 36` | tbz w8,#0x0,0x00add070 | `CONDITIONAL_JUMP`
<a id="insn-00adcc58"></a> `00adcc58` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-00adcc5c"></a> `00adcc5c` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-00adcc60"></a> `00adcc60` | `ff af 00 39` | strb wzr,[sp, #0x2b] | `FALL_THROUGH`
<a id="insn-00adcc64"></a> `00adcc64` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adcc68"></a> `00adcc68` | `68 be ff b0` | adrp x8,0x2a9000 | `FALL_THROUGH`
<a id="insn-00adcc6c"></a> `00adcc6c` | `08 b9 3c 91` | add x8,x8,#0xf2e | `FALL_THROUGH`
<a id="insn-00adcc70"></a> `00adcc70` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00adcc74"></a> `00adcc74` | `e9 93 02 78` | sturh w9,[sp, #0x29] | `FALL_THROUGH`
<a id="insn-00adcc78"></a> `00adcc78` | `49 03 80 52` | mov w9,#0x1a | `FALL_THROUGH`
<a id="insn-00adcc7c"></a> `00adcc7c` | `e9 23 00 39` | strb w9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adcc80"></a> `00adcc80` | `e8 13 02 f8` | stur x8,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00adcc84"></a> `00adcc84` | `08 be ff f0` | adrp x8,0x29f000 | `FALL_THROUGH`
<a id="insn-00adcc88"></a> `00adcc88` | `08 11 39 91` | add x8,x8,#0xe44 | `FALL_THROUGH`
<a id="insn-00adcc8c"></a> `00adcc8c` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00adcc90"></a> `00adcc90` | `08 51 40 f8` | ldur x8,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-00adcc94"></a> `00adcc94` | `ff 5b 00 39` | strb wzr,[sp, #0x16] | `FALL_THROUGH`
<a id="insn-00adcc98"></a> `00adcc98` | `e9 93 00 f8` | stur x9,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-00adcc9c"></a> `00adcc9c` | `e8 e3 00 f8` | stur x8,[sp, #0xe] | `FALL_THROUGH`
<a id="insn-00adcca0"></a> `00adcca0` | `59 0a 00 90` | adrp x25,0xc24000 | `FALL_THROUGH`
<a id="insn-00adcca4"></a> `00adcca4` | `39 03 3d 91` | add x25,x25,#0xf40 | `FALL_THROUGH`
<a id="insn-00adcca8"></a> `00adcca8` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00adccac"></a> `00adccac` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00adccb0"></a> `00adccb0` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adccb4"></a> `00adccb4` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00adccb8"></a> `00adccb8` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-00adccbc"></a> `00adccbc` | `9e fa e5 97` | bl 0x0045b734 | `UNCONDITIONAL_CALL`
<a id="insn-00adccc0"></a> `00adccc0` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00adccc4"></a> `00adccc4` | `9a 0a 40 f9` | ldr x26,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00adccc8"></a> `00adccc8` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00adcccc"></a> `00adcccc` | `80 82 80 3c` | stur q0,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00adccd0"></a> `00adccd0` | `ba 00 00 b4` | cbz x26,0x00adcce4 | `CONDITIONAL_JUMP`
<a id="insn-00adccd4"></a> `00adccd4` | `41 23 00 91` | add x1,x26,#0x8 | `FALL_THROUGH`
<a id="insn-00adccd8"></a> `00adccd8` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00adccdc"></a> `00adccdc` | `2d e8 03 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00adcce0"></a> `00adcce0` | `c0 01 00 b4` | cbz x0,0x00adcd18 | `CONDITIONAL_JUMP`
<a id="insn-00adcce4"></a> `00adcce4` | `ba 83 5e f8` | ldur x26,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00adcce8"></a> `00adcce8` | `ba 00 00 b4` | cbz x26,0x00adccfc | `CONDITIONAL_JUMP`
<a id="insn-00adccec"></a> `00adccec` | `41 23 00 91` | add x1,x26,#0x8 | `FALL_THROUGH`
<a id="insn-00adccf0"></a> `00adccf0` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00adccf4"></a> `00adccf4` | `27 e8 03 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00adccf8"></a> `00adccf8` | `20 02 00 b4` | cbz x0,0x00adcd3c | `CONDITIONAL_JUMP`
<a id="insn-00adccfc"></a> `00adccfc` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adcd00"></a> `00adcd00` | `e8 02 00 37` | tbnz w8,#0x0,0x00adcd5c | `CONDITIONAL_JUMP`
<a id="insn-00adcd04"></a> `00adcd04` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adcd08"></a> `00adcd08` | `28 03 00 37` | tbnz w8,#0x0,0x00adcd6c | `CONDITIONAL_JUMP`
<a id="insn-00adcd0c"></a> `00adcd0c` | `88 ff df 08` | ldarb w8,[x28] | `FALL_THROUGH`
<a id="insn-00adcd10"></a> `00adcd10` | `68 03 00 37` | tbnz w8,#0x0,0x00adcd7c | `CONDITIONAL_JUMP`
<a id="insn-00adcd14"></a> `00adcd14` | `ed 00 00 14` | b 0x00add0c8 | `UNCONDITIONAL_JUMP`
<a id="insn-00adcd18"></a> `00adcd18` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-00adcd1c"></a> `00adcd1c` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00adcd20"></a> `00adcd20` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00adcd24"></a> `00adcd24` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adcd28"></a> `00adcd28` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00adcd2c"></a> `00adcd2c` | `81 f8 03 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00adcd30"></a> `00adcd30` | `ba 83 5e f8` | ldur x26,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00adcd34"></a> `00adcd34` | `da fd ff b5` | cbnz x26,0x00adccec | `CONDITIONAL_JUMP`
<a id="insn-00adcd38"></a> `00adcd38` | `f1 ff ff 17` | b 0x00adccfc | `UNCONDITIONAL_JUMP`
<a id="insn-00adcd3c"></a> `00adcd3c` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-00adcd40"></a> `00adcd40` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00adcd44"></a> `00adcd44` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00adcd48"></a> `00adcd48` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adcd4c"></a> `00adcd4c` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00adcd50"></a> `00adcd50` | `78 f8 03 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00adcd54"></a> `00adcd54` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adcd58"></a> `00adcd58` | `68 fd 07 36` | tbz w8,#0x0,0x00adcd04 | `CONDITIONAL_JUMP`
<a id="insn-00adcd5c"></a> `00adcd5c` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00adcd60"></a> `00adcd60` | `80 f8 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adcd64"></a> `00adcd64` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adcd68"></a> `00adcd68` | `28 fd 07 36` | tbz w8,#0x0,0x00adcd0c | `CONDITIONAL_JUMP`
<a id="insn-00adcd6c"></a> `00adcd6c` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adcd70"></a> `00adcd70` | `7c f8 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adcd74"></a> `00adcd74` | `88 ff df 08` | ldarb w8,[x28] | `FALL_THROUGH`
<a id="insn-00adcd78"></a> `00adcd78` | `88 1a 00 36` | tbz w8,#0x0,0x00add0c8 | `CONDITIONAL_JUMP`
<a id="insn-00adcd7c"></a> `00adcd7c` | `08 03 80 52` | mov w8,#0x18 | `FALL_THROUGH`
<a id="insn-00adcd80"></a> `00adcd80` | `c9 05 8e 52` | mov w9,#0x702e | `FALL_THROUGH`
<a id="insn-00adcd84"></a> `00adcd84` | `ff b7 00 39` | strb wzr,[sp, #0x2d] | `FALL_THROUGH`
<a id="insn-00adcd88"></a> `00adcd88` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adcd8c"></a> `00adcd8c` | `c8 bd ff f0` | adrp x8,0x297000 | `FALL_THROUGH`
<a id="insn-00adcd90"></a> `00adcd90` | `08 dd 0f 91` | add x8,x8,#0x3f7 | `FALL_THROUGH`
<a id="insn-00adcd94"></a> `00adcd94` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00adcd98"></a> `00adcd98` | `c9 ed ac 72` | movk w9,#0x676e, LSL #16 | `FALL_THROUGH`
<a id="insn-00adcd9c"></a> `00adcd9c` | `ff 63 00 39` | strb wzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00adcda0"></a> `00adcda0` | `e9 93 02 b8` | stur w9,[sp, #0x29] | `FALL_THROUGH`
<a id="insn-00adcda4"></a> `00adcda4` | `c9 03 80 52` | mov w9,#0x1e | `FALL_THROUGH`
<a id="insn-00adcda8"></a> `00adcda8` | `e8 13 02 f8` | stur x8,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00adcdac"></a> `00adcdac` | `88 be ff b0` | adrp x8,0x2ad000 | `FALL_THROUGH`
<a id="insn-00adcdb0"></a> `00adcdb0` | `08 e5 08 91` | add x8,x8,#0x239 | `FALL_THROUGH`
<a id="insn-00adcdb4"></a> `00adcdb4` | `e9 23 00 39` | strb w9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adcdb8"></a> `00adcdb8` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00adcdbc"></a> `00adcdbc` | `08 71 40 f8` | ldur x8,[x8, #0x7] | `FALL_THROUGH`
<a id="insn-00adcdc0"></a> `00adcdc0` | `e9 93 00 f8` | stur x9,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-00adcdc4"></a> `00adcdc4` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adcdc8"></a> `00adcdc8` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00adcdcc"></a> `00adcdcc` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00adcdd0"></a> `00adcdd0` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adcdd4"></a> `00adcdd4` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00adcdd8"></a> `00adcdd8` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-00adcddc"></a> `00adcddc` | `56 fa e5 97` | bl 0x0045b734 | `UNCONDITIONAL_CALL`
<a id="insn-00adcde0"></a> `00adcde0` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00adcde4"></a> `00adcde4` | `9a 12 40 f9` | ldr x26,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00adcde8"></a> `00adcde8` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00adcdec"></a> `00adcdec` | `80 82 81 3c` | stur q0,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00adcdf0"></a> `00adcdf0` | `ba 00 00 b4` | cbz x26,0x00adce04 | `CONDITIONAL_JUMP`
<a id="insn-00adcdf4"></a> `00adcdf4` | `41 23 00 91` | add x1,x26,#0x8 | `FALL_THROUGH`
<a id="insn-00adcdf8"></a> `00adcdf8` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00adcdfc"></a> `00adcdfc` | `e5 e7 03 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00adce00"></a> `00adce00` | `00 0f 00 b4` | cbz x0,0x00adcfe0 | `CONDITIONAL_JUMP`
<a id="insn-00adce04"></a> `00adce04` | `ba 83 5e f8` | ldur x26,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00adce08"></a> `00adce08` | `ba 00 00 b4` | cbz x26,0x00adce1c | `CONDITIONAL_JUMP`
<a id="insn-00adce0c"></a> `00adce0c` | `41 23 00 91` | add x1,x26,#0x8 | `FALL_THROUGH`
<a id="insn-00adce10"></a> `00adce10` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00adce14"></a> `00adce14` | `df e7 03 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00adce18"></a> `00adce18` | `60 0f 00 b4` | cbz x0,0x00add004 | `CONDITIONAL_JUMP`
<a id="insn-00adce1c"></a> `00adce1c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adce20"></a> `00adce20` | `68 00 00 36` | tbz w8,#0x0,0x00adce2c | `CONDITIONAL_JUMP`
<a id="insn-00adce24"></a> `00adce24` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00adce28"></a> `00adce28` | `4e f8 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adce2c"></a> `00adce2c` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adce30"></a> `00adce30` | `68 00 00 36` | tbz w8,#0x0,0x00adce3c | `CONDITIONAL_JUMP`
<a id="insn-00adce34"></a> `00adce34` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adce38"></a> `00adce38` | `4a f8 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adce3c"></a> `00adce3c` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00adce40"></a> `00adce40` | `9d 13 f5 97` | bl 0x00821cb4 | `UNCONDITIONAL_CALL`
<a id="insn-00adce44"></a> `00adce44` | `1f 84 01 71` | cmp w0,#0x61 | `FALL_THROUGH`
<a id="insn-00adce48"></a> `00adce48` | `e0 03 00 54` | b.eq 0x00adcec4 | `CONDITIONAL_JUMP`
<a id="insn-00adce4c"></a> `00adce4c` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00adce50"></a> `00adce50` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00adce54"></a> `00adce54` | `d5 54 f5 97` | bl 0x008321a8 | `UNCONDITIONAL_CALL`
<a id="insn-00adce58"></a> `00adce58` | `e0 0b c0 3d` | ldr q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adce5c"></a> `00adce5c` | `98 1a 40 f9` | ldr x24,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00adce60"></a> `00adce60` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adce64"></a> `00adce64` | `80 82 82 3c` | stur q0,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00adce68"></a> `00adce68` | `78 01 00 b4` | cbz x24,0x00adce94 | `CONDITIONAL_JUMP`
<a id="insn-00adce6c"></a> `00adce6c` | `01 23 00 91` | add x1,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00adce70"></a> `00adce70` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00adce74"></a> `00adce74` | `c7 e7 03 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00adce78"></a> `00adce78` | `e0 00 00 b5` | cbnz x0,0x00adce94 | `CONDITIONAL_JUMP`
<a id="insn-00adce7c"></a> `00adce7c` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00adce80"></a> `00adce80` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00adce84"></a> `00adce84` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00adce88"></a> `00adce88` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adce8c"></a> `00adce8c` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00adce90"></a> `00adce90` | `28 f8 03 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00adce94"></a> `00adce94` | `f8 17 40 f9` | ldr x24,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00adce98"></a> `00adce98` | `78 01 00 b4` | cbz x24,0x00adcec4 | `CONDITIONAL_JUMP`
<a id="insn-00adce9c"></a> `00adce9c` | `01 23 00 91` | add x1,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00adcea0"></a> `00adcea0` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00adcea4"></a> `00adcea4` | `bb e7 03 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00adcea8"></a> `00adcea8` | `e0 00 00 b5` | cbnz x0,0x00adcec4 | `CONDITIONAL_JUMP`
<a id="insn-00adceac"></a> `00adceac` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00adceb0"></a> `00adceb0` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00adceb4"></a> `00adceb4` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00adceb8"></a> `00adceb8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adcebc"></a> `00adcebc` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00adcec0"></a> `00adcec0` | `1c f8 03 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00adcec4"></a> `00adcec4` | `88 ff df 08` | ldarb w8,[x28] | `FALL_THROUGH`
<a id="insn-00adcec8"></a> `00adcec8` | `a8 12 00 36` | tbz w8,#0x0,0x00add11c | `CONDITIONAL_JUMP`
<a id="insn-00adcecc"></a> `00adcecc` | `09 be ff b0` | adrp x9,0x29d000 | `FALL_THROUGH`
<a id="insn-00adced0"></a> `00adced0` | `29 91 30 91` | add x9,x9,#0xc24 | `FALL_THROUGH`
<a id="insn-00adced4"></a> `00adced4` | `8a ac 8c 52` | mov w10,#0x6564 | `FALL_THROUGH`
<a id="insn-00adced8"></a> `00adced8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00adcedc"></a> `00adcedc` | `c8 04 80 52` | mov w8,#0x26 | `FALL_THROUGH`
<a id="insn-00adcee0"></a> `00adcee0` | `ea 2b a6 72` | movk w10,#0x315f, LSL #16 | `FALL_THROUGH`
<a id="insn-00adcee4"></a> `00adcee4` | `e8 23 00 39` | strb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adcee8"></a> `00adcee8` | `ea 1b 00 b9` | str w10,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00adceec"></a> `00adceec` | `e0 93 80 3c` | stur q0,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-00adcef0"></a> `00adcef0` | `ff 73 00 39` | strb wzr,[sp, #0x1c] | `FALL_THROUGH`
<a id="insn-00adcef4"></a> `00adcef4` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00adcef8"></a> `00adcef8` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adcefc"></a> `00adcefc` | `20 34 e6 97` | bl 0x00469f7c | `UNCONDITIONAL_CALL`
<a id="insn-00adcf00"></a> `00adcf00` | `e2 09 00 d0` | adrp x2,0xc1a000 | `FALL_THROUGH`
<a id="insn-00adcf04"></a> `00adcf04` | `40 0a 00 90` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00adcf08"></a> `00adcf08` | `00 00 3d 91` | add x0,x0,#0xf40 | `FALL_THROUGH`
<a id="insn-00adcf0c"></a> `00adcf0c` | `42 d8 46 f9` | ldr x2,[x2, #0xdb0] | `FALL_THROUGH`
<a id="insn-00adcf10"></a> `00adcf10` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00adcf14"></a> `00adcf14` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00adcf18"></a> `00adcf18` | `83 02 80 52` | mov w3,#0x14 | `FALL_THROUGH`
<a id="insn-00adcf1c"></a> `00adcf1c` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00adcf20"></a> `00adcf20` | `e5 03 1f 2a` | mov w5,wzr | `FALL_THROUGH`
<a id="insn-00adcf24"></a> `00adcf24` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-00adcf28"></a> `00adcf28` | `b7 fa e5 97` | bl 0x0045ba04 | `UNCONDITIONAL_CALL`
<a id="insn-00adcf2c"></a> `00adcf2c` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00adcf30"></a> `00adcf30` | `98 22 40 f9` | ldr x24,[x20, #0x40] | `FALL_THROUGH`
<a id="insn-00adcf34"></a> `00adcf34` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00adcf38"></a> `00adcf38` | `80 82 83 3c` | stur q0,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00adcf3c"></a> `00adcf3c` | `b8 00 00 b4` | cbz x24,0x00adcf50 | `CONDITIONAL_JUMP`
<a id="insn-00adcf40"></a> `00adcf40` | `01 23 00 91` | add x1,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00adcf44"></a> `00adcf44` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00adcf48"></a> `00adcf48` | `92 e7 03 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00adcf4c"></a> `00adcf4c` | `e0 06 00 b4` | cbz x0,0x00add028 | `CONDITIONAL_JUMP`
<a id="insn-00adcf50"></a> `00adcf50` | `b8 83 5e f8` | ldur x24,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00adcf54"></a> `00adcf54` | `b8 00 00 b4` | cbz x24,0x00adcf68 | `CONDITIONAL_JUMP`
<a id="insn-00adcf58"></a> `00adcf58` | `01 23 00 91` | add x1,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00adcf5c"></a> `00adcf5c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00adcf60"></a> `00adcf60` | `8c e7 03 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00adcf64"></a> `00adcf64` | `40 07 00 b4` | cbz x0,0x00add04c | `CONDITIONAL_JUMP`
<a id="insn-00adcf68"></a> `00adcf68` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adcf6c"></a> `00adcf6c` | `68 00 00 36` | tbz w8,#0x0,0x00adcf78 | `CONDITIONAL_JUMP`
<a id="insn-00adcf70"></a> `00adcf70` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adcf74"></a> `00adcf74` | `fb f7 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adcf78"></a> `00adcf78` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adcf7c"></a> `00adcf7c` | `68 00 00 36` | tbz w8,#0x0,0x00adcf88 | `CONDITIONAL_JUMP`
<a id="insn-00adcf80"></a> `00adcf80` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00adcf84"></a> `00adcf84` | `f7 f7 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00adcf88"></a> `00adcf88` | `7e 09 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00adcf8c"></a> `00adcf8c` | `08 33 83 52` | mov w8,#0x1998 | `FALL_THROUGH`
<a id="insn-00adcf90"></a> `00adcf90` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00adcf94"></a> `00adcf94` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00adcf98"></a> `00adcf98` | `46 12 fe 97` | bl 0x00a618b0 | `UNCONDITIONAL_CALL`
<a id="insn-00adcf9c"></a> `00adcf9c` | `79 09 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00adcfa0"></a> `00adcfa0` | `08 cc 4c 91` | add x8,x0,#0x333, LSL #12 | `FALL_THROUGH`
<a id="insn-00adcfa4"></a> `00adcfa4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00adcfa8"></a> `00adcfa8` | `00 a1 26 91` | add x0,x8,#0x9a8 | `FALL_THROUGH`
<a id="insn-00adcfac"></a> `00adcfac` | `c8 6f f4 97` | bl 0x007f8ecc | `UNCONDITIONAL_CALL`
<a id="insn-00adcfb0"></a> `00adcfb0` | `68 17 40 f9` | ldr x8,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-00adcfb4"></a> `00adcfb4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adcfb8"></a> `00adcfb8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00adcfbc"></a> `00adcfbc` | `e1 12 00 54` | b.ne 0x00add218 | `CONDITIONAL_JUMP`
<a id="insn-00adcfc0"></a> `00adcfc0` | `f4 4f 4b a9` | ldp x20,x19,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00adcfc4"></a> `00adcfc4` | `f6 57 4a a9` | ldp x22,x21,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00adcfc8"></a> `00adcfc8` | `f8 5f 49 a9` | ldp x24,x23,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00adcfcc"></a> `00adcfcc` | `fa 67 48 a9` | ldp x26,x25,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00adcfd0"></a> `00adcfd0` | `fc 6f 47 a9` | ldp x28,x27,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00adcfd4"></a> `00adcfd4` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00adcfd8"></a> `00adcfd8` | `ff 03 03 91` | add sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00adcfdc"></a> `00adcfdc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00adcfe0"></a> `00adcfe0` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-00adcfe4"></a> `00adcfe4` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00adcfe8"></a> `00adcfe8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00adcfec"></a> `00adcfec` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adcff0"></a> `00adcff0` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00adcff4"></a> `00adcff4` | `cf f7 03 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00adcff8"></a> `00adcff8` | `ba 83 5e f8` | ldur x26,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00adcffc"></a> `00adcffc` | `9a f0 ff b5` | cbnz x26,0x00adce0c | `CONDITIONAL_JUMP`
<a id="insn-00add000"></a> `00add000` | `87 ff ff 17` | b 0x00adce1c | `UNCONDITIONAL_JUMP`
<a id="insn-00add004"></a> `00add004` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-00add008"></a> `00add008` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00add00c"></a> `00add00c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00add010"></a> `00add010` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00add014"></a> `00add014` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00add018"></a> `00add018` | `c6 f7 03 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00add01c"></a> `00add01c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00add020"></a> `00add020` | `28 f0 07 37` | tbnz w8,#0x0,0x00adce24 | `CONDITIONAL_JUMP`
<a id="insn-00add024"></a> `00add024` | `82 ff ff 17` | b 0x00adce2c | `UNCONDITIONAL_JUMP`
<a id="insn-00add028"></a> `00add028` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00add02c"></a> `00add02c` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00add030"></a> `00add030` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00add034"></a> `00add034` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00add038"></a> `00add038` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00add03c"></a> `00add03c` | `bd f7 03 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00add040"></a> `00add040` | `b8 83 5e f8` | ldur x24,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00add044"></a> `00add044` | `b8 f8 ff b5` | cbnz x24,0x00adcf58 | `CONDITIONAL_JUMP`
<a id="insn-00add048"></a> `00add048` | `c8 ff ff 17` | b 0x00adcf68 | `UNCONDITIONAL_JUMP`
<a id="insn-00add04c"></a> `00add04c` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00add050"></a> `00add050` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00add054"></a> `00add054` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00add058"></a> `00add058` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00add05c"></a> `00add05c` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00add060"></a> `00add060` | `b4 f7 03 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00add064"></a> `00add064` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00add068"></a> `00add068` | `48 f8 07 37` | tbnz w8,#0x0,0x00adcf70 | `CONDITIONAL_JUMP`
<a id="insn-00add06c"></a> `00add06c` | `c3 ff ff 17` | b 0x00adcf78 | `UNCONDITIONAL_JUMP`
<a id="insn-00add070"></a> `00add070` | `20 0a 00 f0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00add074"></a> `00add074` | `00 e0 3d 91` | add x0,x0,#0xf78 | `FALL_THROUGH`
<a id="insn-00add078"></a> `00add078` | `a2 f7 03 94` | bl 0x00bdaf00 | `UNCONDITIONAL_CALL`
<a id="insn-00add07c"></a> `00add07c` | `e0 de ff 34` | cbz w0,0x00adcc58 | `CONDITIONAL_JUMP`
<a id="insn-00add080"></a> `00add080` | `21 0a 00 f0` | adrp x1,0xc24000 | `FALL_THROUGH`
<a id="insn-00add084"></a> `00add084` | `21 00 3d 91` | add x1,x1,#0xf40 | `FALL_THROUGH`
<a id="insn-00add088"></a> `00add088` | `e0 cb ff d0` | adrp x0,0x45b000 | `FALL_THROUGH`
<a id="insn-00add08c"></a> `00add08c` | `00 70 3b 91` | add x0,x0,#0xedc | `FALL_THROUGH`
<a id="insn-00add090"></a> `00add090` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00add094"></a> `00add094` | `42 08 00 90` | adrp x2,0xbe5000 | `FALL_THROUGH`
<a id="insn-00add098"></a> `00add098` | `42 40 3b 91` | add x2,x2,#0xed0 | `FALL_THROUGH`
<a id="insn-00add09c"></a> `00add09c` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00add0a0"></a> `00add0a0` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00add0a4"></a> `00add0a4` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00add0a8"></a> `00add0a8` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00add0ac"></a> `00add0ac` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00add0b0"></a> `00add0b0` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00add0b4"></a> `00add0b4` | `8b f7 03 94` | bl 0x00bdaee0 | `UNCONDITIONAL_CALL`
<a id="insn-00add0b8"></a> `00add0b8` | `20 0a 00 f0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00add0bc"></a> `00add0bc` | `00 e0 3d 91` | add x0,x0,#0xf78 | `FALL_THROUGH`
<a id="insn-00add0c0"></a> `00add0c0` | `98 f7 03 94` | bl 0x00bdaf20 | `UNCONDITIONAL_CALL`
<a id="insn-00add0c4"></a> `00add0c4` | `e5 fe ff 17` | b 0x00adcc58 | `UNCONDITIONAL_JUMP`
<a id="insn-00add0c8"></a> `00add0c8` | `20 0a 00 f0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00add0cc"></a> `00add0cc` | `00 e0 3d 91` | add x0,x0,#0xf78 | `FALL_THROUGH`
<a id="insn-00add0d0"></a> `00add0d0` | `8c f7 03 94` | bl 0x00bdaf00 | `UNCONDITIONAL_CALL`
<a id="insn-00add0d4"></a> `00add0d4` | `40 e5 ff 34` | cbz w0,0x00adcd7c | `CONDITIONAL_JUMP`
<a id="insn-00add0d8"></a> `00add0d8` | `e8 03 19 aa` | mov x8,x25 | `FALL_THROUGH`
<a id="insn-00add0dc"></a> `00add0dc` | `e0 cb ff d0` | adrp x0,0x45b000 | `FALL_THROUGH`
<a id="insn-00add0e0"></a> `00add0e0` | `00 70 3b 91` | add x0,x0,#0xedc | `FALL_THROUGH`
<a id="insn-00add0e4"></a> `00add0e4` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00add0e8"></a> `00add0e8` | `42 08 00 90` | adrp x2,0xbe5000 | `FALL_THROUGH`
<a id="insn-00add0ec"></a> `00add0ec` | `42 40 3b 91` | add x2,x2,#0xed0 | `FALL_THROUGH`
<a id="insn-00add0f0"></a> `00add0f0` | `28 03 00 f9` | str x8,[x25] | `FALL_THROUGH`
<a id="insn-00add0f4"></a> `00add0f4` | `e8 03 19 aa` | mov x8,x25 | `FALL_THROUGH`
<a id="insn-00add0f8"></a> `00add0f8` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00add0fc"></a> `00add0fc` | `3f ff 02 a9` | stp xzr,xzr,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00add100"></a> `00add100` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00add104"></a> `00add104` | `3f 23 01 a9` | stp xzr,x8,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00add108"></a> `00add108` | `76 f7 03 94` | bl 0x00bdaee0 | `UNCONDITIONAL_CALL`
<a id="insn-00add10c"></a> `00add10c` | `20 0a 00 f0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00add110"></a> `00add110` | `00 e0 3d 91` | add x0,x0,#0xf78 | `FALL_THROUGH`
<a id="insn-00add114"></a> `00add114` | `83 f7 03 94` | bl 0x00bdaf20 | `UNCONDITIONAL_CALL`
<a id="insn-00add118"></a> `00add118` | `19 ff ff 17` | b 0x00adcd7c | `UNCONDITIONAL_JUMP`
<a id="insn-00add11c"></a> `00add11c` | `20 0a 00 f0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00add120"></a> `00add120` | `00 e0 3d 91` | add x0,x0,#0xf78 | `FALL_THROUGH`
<a id="insn-00add124"></a> `00add124` | `77 f7 03 94` | bl 0x00bdaf00 | `UNCONDITIONAL_CALL`
<a id="insn-00add128"></a> `00add128` | `20 ed ff 34` | cbz w0,0x00adcecc | `CONDITIONAL_JUMP`
<a id="insn-00add12c"></a> `00add12c` | `e8 03 19 aa` | mov x8,x25 | `FALL_THROUGH`
<a id="insn-00add130"></a> `00add130` | `e0 cb ff d0` | adrp x0,0x45b000 | `FALL_THROUGH`
<a id="insn-00add134"></a> `00add134` | `00 70 3b 91` | add x0,x0,#0xedc | `FALL_THROUGH`
<a id="insn-00add138"></a> `00add138` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00add13c"></a> `00add13c` | `42 08 00 90` | adrp x2,0xbe5000 | `FALL_THROUGH`
<a id="insn-00add140"></a> `00add140` | `42 40 3b 91` | add x2,x2,#0xed0 | `FALL_THROUGH`
<a id="insn-00add144"></a> `00add144` | `28 03 00 f9` | str x8,[x25] | `FALL_THROUGH`
<a id="insn-00add148"></a> `00add148` | `e8 03 19 aa` | mov x8,x25 | `FALL_THROUGH`
<a id="insn-00add14c"></a> `00add14c` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00add150"></a> `00add150` | `3f ff 02 a9` | stp xzr,xzr,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00add154"></a> `00add154` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00add158"></a> `00add158` | `3f 23 01 a9` | stp xzr,x8,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00add15c"></a> `00add15c` | `61 f7 03 94` | bl 0x00bdaee0 | `UNCONDITIONAL_CALL`
<a id="insn-00add160"></a> `00add160` | `20 0a 00 f0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00add164"></a> `00add164` | `00 e0 3d 91` | add x0,x0,#0xf78 | `FALL_THROUGH`
<a id="insn-00add168"></a> `00add168` | `6e f7 03 94` | bl 0x00bdaf20 | `UNCONDITIONAL_CALL`
<a id="insn-00add16c"></a> `00add16c` | `58 ff ff 17` | b 0x00adcecc | `UNCONDITIONAL_JUMP`
<a id="insn-00add218"></a> `00add218` | `5e f7 03 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adcbcc`](#insn-00adcbcc) 範囲 `[['00adcbcc', '00adcc57']]`
  - `CONDITIONAL_JUMP` [`00adcc54`](#insn-00adcc54) → [`00add070`](#insn-00add070)
  - `FALL_THROUGH` [`00adcc54`](#insn-00adcc54) → [`00adcc58`](#insn-00adcc58)
- ブロック [`00adcc58`](#insn-00adcc58) 範囲 `[['00adcc58', '00adccd3']]`
  - `CONDITIONAL_JUMP` [`00adccd0`](#insn-00adccd0) → [`00adcce4`](#insn-00adcce4)
  - `FALL_THROUGH` [`00adccd0`](#insn-00adccd0) → [`00adccd4`](#insn-00adccd4)
- ブロック [`00adccd4`](#insn-00adccd4) 範囲 `[['00adccd4', '00adcce3']]`
  - `CONDITIONAL_JUMP` [`00adcce0`](#insn-00adcce0) → [`00adcd18`](#insn-00adcd18)
  - `FALL_THROUGH` [`00adcce0`](#insn-00adcce0) → [`00adcce4`](#insn-00adcce4)
- ブロック [`00adcce4`](#insn-00adcce4) 範囲 `[['00adcce4', '00adcceb']]`
  - `CONDITIONAL_JUMP` [`00adcce8`](#insn-00adcce8) → [`00adccfc`](#insn-00adccfc)
  - `FALL_THROUGH` [`00adcce8`](#insn-00adcce8) → [`00adccec`](#insn-00adccec)
- ブロック [`00adccec`](#insn-00adccec) 範囲 `[['00adccec', '00adccfb']]`
  - `CONDITIONAL_JUMP` [`00adccf8`](#insn-00adccf8) → [`00adcd3c`](#insn-00adcd3c)
  - `FALL_THROUGH` [`00adccf8`](#insn-00adccf8) → [`00adccfc`](#insn-00adccfc)
- ブロック [`00adccfc`](#insn-00adccfc) 範囲 `[['00adccfc', '00adcd03']]`
  - `CONDITIONAL_JUMP` [`00adcd00`](#insn-00adcd00) → [`00adcd5c`](#insn-00adcd5c)
  - `FALL_THROUGH` [`00adcd00`](#insn-00adcd00) → [`00adcd04`](#insn-00adcd04)
- ブロック [`00adcd04`](#insn-00adcd04) 範囲 `[['00adcd04', '00adcd0b']]`
  - `CONDITIONAL_JUMP` [`00adcd08`](#insn-00adcd08) → [`00adcd6c`](#insn-00adcd6c)
  - `FALL_THROUGH` [`00adcd08`](#insn-00adcd08) → [`00adcd0c`](#insn-00adcd0c)
- ブロック [`00adcd0c`](#insn-00adcd0c) 範囲 `[['00adcd0c', '00adcd13']]`
  - `CONDITIONAL_JUMP` [`00adcd10`](#insn-00adcd10) → [`00adcd7c`](#insn-00adcd7c)
  - `FALL_THROUGH` [`00adcd10`](#insn-00adcd10) → [`00adcd14`](#insn-00adcd14)
- ブロック [`00adcd14`](#insn-00adcd14) 範囲 `[['00adcd14', '00adcd17']]`
  - `UNCONDITIONAL_JUMP` [`00adcd14`](#insn-00adcd14) → [`00add0c8`](#insn-00add0c8)
- ブロック [`00adcd18`](#insn-00adcd18) 範囲 `[['00adcd18', '00adcd37']]`
  - `CONDITIONAL_JUMP` [`00adcd34`](#insn-00adcd34) → [`00adccec`](#insn-00adccec)
  - `FALL_THROUGH` [`00adcd34`](#insn-00adcd34) → [`00adcd38`](#insn-00adcd38)
- ブロック [`00adcd38`](#insn-00adcd38) 範囲 `[['00adcd38', '00adcd3b']]`
  - `UNCONDITIONAL_JUMP` [`00adcd38`](#insn-00adcd38) → [`00adccfc`](#insn-00adccfc)
- ブロック [`00adcd3c`](#insn-00adcd3c) 範囲 `[['00adcd3c', '00adcd5b']]`
  - `CONDITIONAL_JUMP` [`00adcd58`](#insn-00adcd58) → [`00adcd04`](#insn-00adcd04)
  - `FALL_THROUGH` [`00adcd58`](#insn-00adcd58) → [`00adcd5c`](#insn-00adcd5c)
- ブロック [`00adcd5c`](#insn-00adcd5c) 範囲 `[['00adcd5c', '00adcd6b']]`
  - `CONDITIONAL_JUMP` [`00adcd68`](#insn-00adcd68) → [`00adcd0c`](#insn-00adcd0c)
  - `FALL_THROUGH` [`00adcd68`](#insn-00adcd68) → [`00adcd6c`](#insn-00adcd6c)
- ブロック [`00adcd6c`](#insn-00adcd6c) 範囲 `[['00adcd6c', '00adcd7b']]`
  - `CONDITIONAL_JUMP` [`00adcd78`](#insn-00adcd78) → [`00add0c8`](#insn-00add0c8)
  - `FALL_THROUGH` [`00adcd78`](#insn-00adcd78) → [`00adcd7c`](#insn-00adcd7c)
- ブロック [`00adcd7c`](#insn-00adcd7c) 範囲 `[['00adcd7c', '00adcdf3']]`
  - `CONDITIONAL_JUMP` [`00adcdf0`](#insn-00adcdf0) → [`00adce04`](#insn-00adce04)
  - `FALL_THROUGH` [`00adcdf0`](#insn-00adcdf0) → [`00adcdf4`](#insn-00adcdf4)
- ブロック [`00adcdf4`](#insn-00adcdf4) 範囲 `[['00adcdf4', '00adce03']]`
  - `CONDITIONAL_JUMP` [`00adce00`](#insn-00adce00) → [`00adcfe0`](#insn-00adcfe0)
  - `FALL_THROUGH` [`00adce00`](#insn-00adce00) → [`00adce04`](#insn-00adce04)
- ブロック [`00adce04`](#insn-00adce04) 範囲 `[['00adce04', '00adce0b']]`
  - `CONDITIONAL_JUMP` [`00adce08`](#insn-00adce08) → [`00adce1c`](#insn-00adce1c)
  - `FALL_THROUGH` [`00adce08`](#insn-00adce08) → [`00adce0c`](#insn-00adce0c)
- ブロック [`00adce0c`](#insn-00adce0c) 範囲 `[['00adce0c', '00adce1b']]`
  - `CONDITIONAL_JUMP` [`00adce18`](#insn-00adce18) → [`00add004`](#insn-00add004)
  - `FALL_THROUGH` [`00adce18`](#insn-00adce18) → [`00adce1c`](#insn-00adce1c)
- ブロック [`00adce1c`](#insn-00adce1c) 範囲 `[['00adce1c', '00adce23']]`
  - `CONDITIONAL_JUMP` [`00adce20`](#insn-00adce20) → [`00adce2c`](#insn-00adce2c)
  - `FALL_THROUGH` [`00adce20`](#insn-00adce20) → [`00adce24`](#insn-00adce24)
- ブロック [`00adce24`](#insn-00adce24) 範囲 `[['00adce24', '00adce2b']]`
  - `FALL_THROUGH` [`00adce28`](#insn-00adce28) → [`00adce2c`](#insn-00adce2c)
- ブロック [`00adce2c`](#insn-00adce2c) 範囲 `[['00adce2c', '00adce33']]`
  - `CONDITIONAL_JUMP` [`00adce30`](#insn-00adce30) → [`00adce3c`](#insn-00adce3c)
  - `FALL_THROUGH` [`00adce30`](#insn-00adce30) → [`00adce34`](#insn-00adce34)
- ブロック [`00adce34`](#insn-00adce34) 範囲 `[['00adce34', '00adce3b']]`
  - `FALL_THROUGH` [`00adce38`](#insn-00adce38) → [`00adce3c`](#insn-00adce3c)
- ブロック [`00adce3c`](#insn-00adce3c) 範囲 `[['00adce3c', '00adce4b']]`
  - `CONDITIONAL_JUMP` [`00adce48`](#insn-00adce48) → [`00adcec4`](#insn-00adcec4)
  - `FALL_THROUGH` [`00adce48`](#insn-00adce48) → [`00adce4c`](#insn-00adce4c)
- ブロック [`00adce4c`](#insn-00adce4c) 範囲 `[['00adce4c', '00adce6b']]`
  - `CONDITIONAL_JUMP` [`00adce68`](#insn-00adce68) → [`00adce94`](#insn-00adce94)
  - `FALL_THROUGH` [`00adce68`](#insn-00adce68) → [`00adce6c`](#insn-00adce6c)
- ブロック [`00adce6c`](#insn-00adce6c) 範囲 `[['00adce6c', '00adce7b']]`
  - `CONDITIONAL_JUMP` [`00adce78`](#insn-00adce78) → [`00adce94`](#insn-00adce94)
  - `FALL_THROUGH` [`00adce78`](#insn-00adce78) → [`00adce7c`](#insn-00adce7c)
- ブロック [`00adce7c`](#insn-00adce7c) 範囲 `[['00adce7c', '00adce93']]`
  - `FALL_THROUGH` [`00adce90`](#insn-00adce90) → [`00adce94`](#insn-00adce94)
- ブロック [`00adce94`](#insn-00adce94) 範囲 `[['00adce94', '00adce9b']]`
  - `CONDITIONAL_JUMP` [`00adce98`](#insn-00adce98) → [`00adcec4`](#insn-00adcec4)
  - `FALL_THROUGH` [`00adce98`](#insn-00adce98) → [`00adce9c`](#insn-00adce9c)
- ブロック [`00adce9c`](#insn-00adce9c) 範囲 `[['00adce9c', '00adceab']]`
  - `CONDITIONAL_JUMP` [`00adcea8`](#insn-00adcea8) → [`00adcec4`](#insn-00adcec4)
  - `FALL_THROUGH` [`00adcea8`](#insn-00adcea8) → [`00adceac`](#insn-00adceac)
- ブロック [`00adceac`](#insn-00adceac) 範囲 `[['00adceac', '00adcec3']]`
  - `FALL_THROUGH` [`00adcec0`](#insn-00adcec0) → [`00adcec4`](#insn-00adcec4)
- ブロック [`00adcec4`](#insn-00adcec4) 範囲 `[['00adcec4', '00adcecb']]`
  - `CONDITIONAL_JUMP` [`00adcec8`](#insn-00adcec8) → [`00add11c`](#insn-00add11c)
  - `FALL_THROUGH` [`00adcec8`](#insn-00adcec8) → [`00adcecc`](#insn-00adcecc)
- ブロック [`00adcecc`](#insn-00adcecc) 範囲 `[['00adcecc', '00adcedf']]`
  - `FALL_THROUGH` [`00adcedc`](#insn-00adcedc) → [`00adcee0`](#insn-00adcee0)
- ブロック [`00adcee0`](#insn-00adcee0) 範囲 `[['00adcee0', '00adcf3f']]`
  - `CONDITIONAL_JUMP` [`00adcf3c`](#insn-00adcf3c) → [`00adcf50`](#insn-00adcf50)
  - `FALL_THROUGH` [`00adcf3c`](#insn-00adcf3c) → [`00adcf40`](#insn-00adcf40)
- ブロック [`00adcf40`](#insn-00adcf40) 範囲 `[['00adcf40', '00adcf4f']]`
  - `CONDITIONAL_JUMP` [`00adcf4c`](#insn-00adcf4c) → [`00add028`](#insn-00add028)
  - `FALL_THROUGH` [`00adcf4c`](#insn-00adcf4c) → [`00adcf50`](#insn-00adcf50)
- ブロック [`00adcf50`](#insn-00adcf50) 範囲 `[['00adcf50', '00adcf57']]`
  - `CONDITIONAL_JUMP` [`00adcf54`](#insn-00adcf54) → [`00adcf68`](#insn-00adcf68)
  - `FALL_THROUGH` [`00adcf54`](#insn-00adcf54) → [`00adcf58`](#insn-00adcf58)
- ブロック [`00adcf58`](#insn-00adcf58) 範囲 `[['00adcf58', '00adcf67']]`
  - `CONDITIONAL_JUMP` [`00adcf64`](#insn-00adcf64) → [`00add04c`](#insn-00add04c)
  - `FALL_THROUGH` [`00adcf64`](#insn-00adcf64) → [`00adcf68`](#insn-00adcf68)
- ブロック [`00adcf68`](#insn-00adcf68) 範囲 `[['00adcf68', '00adcf6f']]`
  - `CONDITIONAL_JUMP` [`00adcf6c`](#insn-00adcf6c) → [`00adcf78`](#insn-00adcf78)
  - `FALL_THROUGH` [`00adcf6c`](#insn-00adcf6c) → [`00adcf70`](#insn-00adcf70)
- ブロック [`00adcf70`](#insn-00adcf70) 範囲 `[['00adcf70', '00adcf77']]`
  - `FALL_THROUGH` [`00adcf74`](#insn-00adcf74) → [`00adcf78`](#insn-00adcf78)
- ブロック [`00adcf78`](#insn-00adcf78) 範囲 `[['00adcf78', '00adcf7f']]`
  - `CONDITIONAL_JUMP` [`00adcf7c`](#insn-00adcf7c) → [`00adcf88`](#insn-00adcf88)
  - `FALL_THROUGH` [`00adcf7c`](#insn-00adcf7c) → [`00adcf80`](#insn-00adcf80)
- ブロック [`00adcf80`](#insn-00adcf80) 範囲 `[['00adcf80', '00adcf87']]`
  - `FALL_THROUGH` [`00adcf84`](#insn-00adcf84) → [`00adcf88`](#insn-00adcf88)
- ブロック [`00adcf88`](#insn-00adcf88) 範囲 `[['00adcf88', '00adcfbf']]`
  - `CONDITIONAL_JUMP` [`00adcfbc`](#insn-00adcfbc) → [`00add218`](#insn-00add218)
  - `FALL_THROUGH` [`00adcfbc`](#insn-00adcfbc) → [`00adcfc0`](#insn-00adcfc0)
- ブロック [`00adcfc0`](#insn-00adcfc0) 範囲 `[['00adcfc0', '00adcfdf']]`
- ブロック [`00adcfe0`](#insn-00adcfe0) 範囲 `[['00adcfe0', '00adcfff']]`
  - `CONDITIONAL_JUMP` [`00adcffc`](#insn-00adcffc) → [`00adce0c`](#insn-00adce0c)
  - `FALL_THROUGH` [`00adcffc`](#insn-00adcffc) → [`00add000`](#insn-00add000)
- ブロック [`00add000`](#insn-00add000) 範囲 `[['00add000', '00add003']]`
  - `UNCONDITIONAL_JUMP` [`00add000`](#insn-00add000) → [`00adce1c`](#insn-00adce1c)
- ブロック [`00add004`](#insn-00add004) 範囲 `[['00add004', '00add023']]`
  - `CONDITIONAL_JUMP` [`00add020`](#insn-00add020) → [`00adce24`](#insn-00adce24)
  - `FALL_THROUGH` [`00add020`](#insn-00add020) → [`00add024`](#insn-00add024)
- ブロック [`00add024`](#insn-00add024) 範囲 `[['00add024', '00add027']]`
  - `UNCONDITIONAL_JUMP` [`00add024`](#insn-00add024) → [`00adce2c`](#insn-00adce2c)
- ブロック [`00add028`](#insn-00add028) 範囲 `[['00add028', '00add047']]`
  - `CONDITIONAL_JUMP` [`00add044`](#insn-00add044) → [`00adcf58`](#insn-00adcf58)
  - `FALL_THROUGH` [`00add044`](#insn-00add044) → [`00add048`](#insn-00add048)
- ブロック [`00add048`](#insn-00add048) 範囲 `[['00add048', '00add04b']]`
  - `UNCONDITIONAL_JUMP` [`00add048`](#insn-00add048) → [`00adcf68`](#insn-00adcf68)
- ブロック [`00add04c`](#insn-00add04c) 範囲 `[['00add04c', '00add06b']]`
  - `CONDITIONAL_JUMP` [`00add068`](#insn-00add068) → [`00adcf70`](#insn-00adcf70)
  - `FALL_THROUGH` [`00add068`](#insn-00add068) → [`00add06c`](#insn-00add06c)
- ブロック [`00add06c`](#insn-00add06c) 範囲 `[['00add06c', '00add06f']]`
  - `UNCONDITIONAL_JUMP` [`00add06c`](#insn-00add06c) → [`00adcf78`](#insn-00adcf78)
- ブロック [`00add070`](#insn-00add070) 範囲 `[['00add070', '00add07b']]`
  - `FALL_THROUGH` [`00add078`](#insn-00add078) → [`00add07c`](#insn-00add07c)
- ブロック [`00add07c`](#insn-00add07c) 範囲 `[['00add07c', '00add07f']]`
  - `CONDITIONAL_JUMP` [`00add07c`](#insn-00add07c) → [`00adcc58`](#insn-00adcc58)
  - `FALL_THROUGH` [`00add07c`](#insn-00add07c) → [`00add080`](#insn-00add080)
- ブロック [`00add080`](#insn-00add080) 範囲 `[['00add080', '00add083']]`
  - `FALL_THROUGH` [`00add080`](#insn-00add080) → [`00add084`](#insn-00add084)
- ブロック [`00add084`](#insn-00add084) 範囲 `[['00add084', '00add0c7']]`
  - `UNCONDITIONAL_JUMP` [`00add0c4`](#insn-00add0c4) → [`00adcc58`](#insn-00adcc58)
- ブロック [`00add0c8`](#insn-00add0c8) 範囲 `[['00add0c8', '00add0d7']]`
  - `CONDITIONAL_JUMP` [`00add0d4`](#insn-00add0d4) → [`00adcd7c`](#insn-00adcd7c)
  - `FALL_THROUGH` [`00add0d4`](#insn-00add0d4) → [`00add0d8`](#insn-00add0d8)
- ブロック [`00add0d8`](#insn-00add0d8) 範囲 `[['00add0d8', '00add103']]`
  - `FALL_THROUGH` [`00add100`](#insn-00add100) → [`00add104`](#insn-00add104)
- ブロック [`00add104`](#insn-00add104) 範囲 `[['00add104', '00add11b']]`
  - `UNCONDITIONAL_JUMP` [`00add118`](#insn-00add118) → [`00adcd7c`](#insn-00adcd7c)
- ブロック [`00add11c`](#insn-00add11c) 範囲 `[['00add11c', '00add12b']]`
  - `CONDITIONAL_JUMP` [`00add128`](#insn-00add128) → [`00adcecc`](#insn-00adcecc)
  - `FALL_THROUGH` [`00add128`](#insn-00add128) → [`00add12c`](#insn-00add12c)
- ブロック [`00add12c`](#insn-00add12c) 範囲 `[['00add12c', '00add16f']]`
  - `UNCONDITIONAL_JUMP` [`00add16c`](#insn-00add16c) → [`00adcecc`](#insn-00adcecc)
- ブロック [`00add218`](#insn-00add218) 範囲 `[['00add218', '00add21b']]`

## 命令位置別の参照

- [`00adcbd0`](#insn-00adcbd0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcbd4`](#insn-00adcbd4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcbd8`](#insn-00adcbd8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcbdc`](#insn-00adcbdc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcbe0`](#insn-00adcbe0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcbe4`](#insn-00adcbe4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcc10`](#insn-00adcc10) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcc1c`](#insn-00adcc1c) → `00bf7058`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00adcc50`](#insn-00adcc50) → `00c24f78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00adcc54`](#insn-00adcc54) → [`00add070`](#insn-00add070) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcc60`](#insn-00adcc60) → `Stack[-0x95]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcc64`](#insn-00adcc64) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcc70`](#insn-00adcc70) → `002a9f2e`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adcc74`](#insn-00adcc74) → `Stack[-0x97]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcc7c`](#insn-00adcc7c) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcc80`](#insn-00adcc80) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcc8c`](#insn-00adcc8c) → `0029fe44`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcc90`](#insn-00adcc90) → `0029fe49`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adcc94`](#insn-00adcc94) → `Stack[-0xaa]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcc98`](#insn-00adcc98) → `Stack[-0xb7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcc9c`](#insn-00adcc9c) → `Stack[-0xb2]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adccb4`](#insn-00adccb4) → `00c24f40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adccbc`](#insn-00adccbc) → [`0045b734`](../0045b/0045b734.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045b734` · 推定シンボル `None` · 推定型 `None`
- [`00adccc0`](#insn-00adccc0) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adccc8`](#insn-00adccc8) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adccd0`](#insn-00adccd0) → [`00adcce4`](#insn-00adcce4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adccdc`](#insn-00adccdc) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00adcce0`](#insn-00adcce0) → [`00adcd18`](#insn-00adcd18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcce4`](#insn-00adcce4) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcce8`](#insn-00adcce8) → [`00adccfc`](#insn-00adccfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adccf4`](#insn-00adccf4) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00adccf8`](#insn-00adccf8) → [`00adcd3c`](#insn-00adcd3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adccfc`](#insn-00adccfc) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd00`](#insn-00adcd00) → [`00adcd5c`](#insn-00adcd5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd04`](#insn-00adcd04) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd08`](#insn-00adcd08) → [`00adcd6c`](#insn-00adcd6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd0c`](#insn-00adcd0c) → `00c24f78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00adcd10`](#insn-00adcd10) → [`00adcd7c`](#insn-00adcd7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd14`](#insn-00adcd14) → [`00add0c8`](#insn-00add0c8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd2c`](#insn-00adcd2c) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00adcd30`](#insn-00adcd30) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd34`](#insn-00adcd34) → [`00adccec`](#insn-00adccec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd38`](#insn-00adcd38) → [`00adccfc`](#insn-00adccfc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd50`](#insn-00adcd50) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00adcd54`](#insn-00adcd54) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd58`](#insn-00adcd58) → [`00adcd04`](#insn-00adcd04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd5c`](#insn-00adcd5c) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd60`](#insn-00adcd60) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adcd64`](#insn-00adcd64) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd68`](#insn-00adcd68) → [`00adcd0c`](#insn-00adcd0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd6c`](#insn-00adcd6c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd70`](#insn-00adcd70) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adcd74`](#insn-00adcd74) → `00c24f78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00adcd78`](#insn-00adcd78) → [`00add0c8`](#insn-00add0c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd84`](#insn-00adcd84) → `Stack[-0x93]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd88`](#insn-00adcd88) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcd94`](#insn-00adcd94) → `002973f7`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adcd9c`](#insn-00adcd9c) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcda0`](#insn-00adcda0) → `Stack[-0x97]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcda8`](#insn-00adcda8) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcdb4`](#insn-00adcdb4) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcdb8`](#insn-00adcdb8) → `002ad239`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcdbc`](#insn-00adcdbc) → `002ad240`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adcdc0`](#insn-00adcdc0) → `Stack[-0xb7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcdc4`](#insn-00adcdc4) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcdd4`](#insn-00adcdd4) → `00c24f40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adcddc`](#insn-00adcddc) → [`0045b734`](../0045b/0045b734.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045b734` · 推定シンボル `None` · 推定型 `None`
- [`00adcde0`](#insn-00adcde0) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcde8`](#insn-00adcde8) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcdf0`](#insn-00adcdf0) → [`00adce04`](#insn-00adce04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcdfc`](#insn-00adcdfc) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00adce00`](#insn-00adce00) → [`00adcfe0`](#insn-00adcfe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce04`](#insn-00adce04) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce08`](#insn-00adce08) → [`00adce1c`](#insn-00adce1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce14`](#insn-00adce14) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00adce18`](#insn-00adce18) → [`00add004`](#insn-00add004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce1c`](#insn-00adce1c) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce20`](#insn-00adce20) → [`00adce2c`](#insn-00adce2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce24`](#insn-00adce24) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce28`](#insn-00adce28) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adce2c`](#insn-00adce2c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce30`](#insn-00adce30) → [`00adce3c`](#insn-00adce3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce34`](#insn-00adce34) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce38`](#insn-00adce38) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adce40`](#insn-00adce40) → [`00821cb4`](../00821/00821cb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00821cb4` · 推定シンボル `None` · 推定型 `None`
- [`00adce48`](#insn-00adce48) → [`00adcec4`](#insn-00adcec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce54`](#insn-00adce54) → [`008321a8`](../00832/008321a8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008321a8` · 推定シンボル `None` · 推定型 `None`
- [`00adce58`](#insn-00adce58) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce60`](#insn-00adce60) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce68`](#insn-00adce68) → [`00adce94`](#insn-00adce94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce74`](#insn-00adce74) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00adce78`](#insn-00adce78) → [`00adce94`](#insn-00adce94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce90`](#insn-00adce90) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00adce94`](#insn-00adce94) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adce98`](#insn-00adce98) → [`00adcec4`](#insn-00adcec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcea4`](#insn-00adcea4) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00adcea8`](#insn-00adcea8) → [`00adcec4`](#insn-00adcec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcec0`](#insn-00adcec0) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00adcec4`](#insn-00adcec4) → `00c24f78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00adcec8`](#insn-00adcec8) → [`00add11c`](#insn-00add11c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adced8`](#insn-00adced8) → `0029dc24`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00adcee4`](#insn-00adcee4) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcee8`](#insn-00adcee8) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adceec`](#insn-00adceec) → `Stack[-0xb7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcef0`](#insn-00adcef0) → `Stack[-0xa4]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcefc`](#insn-00adcefc) → [`00469f7c`](../00469/00469f7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469f7c` · 推定シンボル `None` · 推定型 `None`
- [`00adcf08`](#insn-00adcf08) → `00c24f40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adcf0c`](#insn-00adcf0c) → `00c1adb0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00adcf0c`](#insn-00adcf0c) → `00c25018`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00adcf28`](#insn-00adcf28) → [`0045ba04`](../0045b/0045ba04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045ba04` · 推定シンボル `None` · 推定型 `None`
- [`00adcf2c`](#insn-00adcf2c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf34`](#insn-00adcf34) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf3c`](#insn-00adcf3c) → [`00adcf50`](#insn-00adcf50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf48`](#insn-00adcf48) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00adcf4c`](#insn-00adcf4c) → [`00add028`](#insn-00add028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf50`](#insn-00adcf50) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf54`](#insn-00adcf54) → [`00adcf68`](#insn-00adcf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf60`](#insn-00adcf60) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00adcf64`](#insn-00adcf64) → [`00add04c`](#insn-00add04c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf68`](#insn-00adcf68) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf6c`](#insn-00adcf6c) → [`00adcf78`](#insn-00adcf78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf70`](#insn-00adcf70) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf74`](#insn-00adcf74) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adcf78`](#insn-00adcf78) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf7c`](#insn-00adcf7c) → [`00adcf88`](#insn-00adcf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf80`](#insn-00adcf80) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcf84`](#insn-00adcf84) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00adcf88`](#insn-00adcf88) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00adcf98`](#insn-00adcf98) → [`00a618b0`](../00a61/00a618b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a618b0` · 推定シンボル `None` · 推定型 `None`
- [`00adcf9c`](#insn-00adcf9c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00adcfac`](#insn-00adcfac) → [`007f8ecc`](../007f8/007f8ecc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007f8ecc` · 推定シンボル `None` · 推定型 `None`
- [`00adcfb4`](#insn-00adcfb4) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcfbc`](#insn-00adcfbc) → [`00add218`](#insn-00add218) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcfc0`](#insn-00adcfc0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcfc4`](#insn-00adcfc4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcfc8`](#insn-00adcfc8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcfcc`](#insn-00adcfcc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcfd0`](#insn-00adcfd0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcfd4`](#insn-00adcfd4) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcff4`](#insn-00adcff4) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00adcff8`](#insn-00adcff8) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adcffc`](#insn-00adcffc) → [`00adce0c`](#insn-00adce0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add000`](#insn-00add000) → [`00adce1c`](#insn-00adce1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add018`](#insn-00add018) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00add01c`](#insn-00add01c) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add020`](#insn-00add020) → [`00adce24`](#insn-00adce24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add024`](#insn-00add024) → [`00adce2c`](#insn-00adce2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add03c`](#insn-00add03c) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00add040`](#insn-00add040) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add044`](#insn-00add044) → [`00adcf58`](#insn-00adcf58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add048`](#insn-00add048) → [`00adcf68`](#insn-00adcf68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add060`](#insn-00add060) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00add064`](#insn-00add064) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add068`](#insn-00add068) → [`00adcf70`](#insn-00adcf70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add06c`](#insn-00add06c) → [`00adcf78`](#insn-00adcf78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add074`](#insn-00add074) → `00c24f78`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00add078`](#insn-00add078) → [`00bdaf00`](../00bda/00bdaf00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf00` · 推定シンボル `None` · 推定型 `None`
- [`00add07c`](#insn-00add07c) → [`00adcc58`](#insn-00adcc58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add084`](#insn-00add084) → `00c24f40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add08c`](#insn-00add08c) → [`0045bedc`](../0045b/0045bedc.md) · `PARAM` · `ANALYSIS` · 関数 `0045bedc` · 推定シンボル `None` · 推定型 `None`
- [`00add098`](#insn-00add098) → `00be5ed0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00add09c`](#insn-00add09c) → `00c24f48`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add0a0`](#insn-00add0a0) → `00c24f40`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add0a0`](#insn-00add0a0) → `00c24f48`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add0a8`](#insn-00add0a8) → `00c24f68`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add0a8`](#insn-00add0a8) → `00c24f70`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add0ac`](#insn-00add0ac) → `00c24f60`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add0b0`](#insn-00add0b0) → `00c24f50`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add0b0`](#insn-00add0b0) → `00c24f58`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add0b0`](#insn-00add0b0) → `00c24f60`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add0b4`](#insn-00add0b4) → [`00bdaee0`](../00bda/00bdaee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaee0` · 推定シンボル `None` · 推定型 `None`
- [`00add0bc`](#insn-00add0bc) → `00c24f78`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00add0c0`](#insn-00add0c0) → [`00bdaf20`](../00bda/00bdaf20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf20` · 推定シンボル `None` · 推定型 `None`
- [`00add0c4`](#insn-00add0c4) → [`00adcc58`](#insn-00adcc58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add0cc`](#insn-00add0cc) → `00c24f78`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00add0d0`](#insn-00add0d0) → [`00bdaf00`](../00bda/00bdaf00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf00` · 推定シンボル `None` · 推定型 `None`
- [`00add0d4`](#insn-00add0d4) → [`00adcd7c`](#insn-00adcd7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add0e0`](#insn-00add0e0) → [`0045bedc`](../0045b/0045bedc.md) · `PARAM` · `ANALYSIS` · 関数 `0045bedc` · 推定シンボル `None` · 推定型 `None`
- [`00add0e4`](#insn-00add0e4) → `00c24f48`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add0ec`](#insn-00add0ec) → `00be5ed0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00add0f0`](#insn-00add0f0) → `00c24f40`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add0f0`](#insn-00add0f0) → `00c24f48`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add0f8`](#insn-00add0f8) → `00c24f40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add0fc`](#insn-00add0fc) → `00c24f68`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add0fc`](#insn-00add0fc) → `00c24f70`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add100`](#insn-00add100) → `00c24f60`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add104`](#insn-00add104) → `00c24f50`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add104`](#insn-00add104) → `00c24f58`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add104`](#insn-00add104) → `00c24f60`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add108`](#insn-00add108) → [`00bdaee0`](../00bda/00bdaee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaee0` · 推定シンボル `None` · 推定型 `None`
- [`00add110`](#insn-00add110) → `00c24f78`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00add114`](#insn-00add114) → [`00bdaf20`](../00bda/00bdaf20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf20` · 推定シンボル `None` · 推定型 `None`
- [`00add118`](#insn-00add118) → [`00adcd7c`](#insn-00adcd7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add120`](#insn-00add120) → `00c24f78`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00add124`](#insn-00add124) → [`00bdaf00`](../00bda/00bdaf00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf00` · 推定シンボル `None` · 推定型 `None`
- [`00add128`](#insn-00add128) → [`00adcecc`](#insn-00adcecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add134`](#insn-00add134) → [`0045bedc`](../0045b/0045bedc.md) · `PARAM` · `ANALYSIS` · 関数 `0045bedc` · 推定シンボル `None` · 推定型 `None`
- [`00add138`](#insn-00add138) → `00c24f48`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add140`](#insn-00add140) → `00be5ed0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00add144`](#insn-00add144) → `00c24f40`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add144`](#insn-00add144) → `00c24f48`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add14c`](#insn-00add14c) → `00c24f40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add150`](#insn-00add150) → `00c24f68`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add150`](#insn-00add150) → `00c24f70`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add154`](#insn-00add154) → `00c24f60`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add158`](#insn-00add158) → `00c24f50`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add158`](#insn-00add158) → `00c24f58`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add158`](#insn-00add158) → `00c24f60`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00add15c`](#insn-00add15c) → [`00bdaee0`](../00bda/00bdaee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaee0` · 推定シンボル `None` · 推定型 `None`
- [`00add164`](#insn-00add164) → `00c24f78`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00add168`](#insn-00add168) → [`00bdaf20`](../00bda/00bdaf20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf20` · 推定シンボル `None` · 推定型 `None`
- [`00add16c`](#insn-00add16c) → [`00adcecc`](#insn-00adcecc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00add218`](#insn-00add218) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adcbd0`](#insn-00adcbd0)

~~~json
{
  "source": "00adcbd0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcbd4`](#insn-00adcbd4)

~~~json
{
  "source": "00adcbd4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcbd8`](#insn-00adcbd8)

~~~json
{
  "source": "00adcbd8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcbdc`](#insn-00adcbdc)

~~~json
{
  "source": "00adcbdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcbe0`](#insn-00adcbe0)

~~~json
{
  "source": "00adcbe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcbe4`](#insn-00adcbe4)

~~~json
{
  "source": "00adcbe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcc10`](#insn-00adcc10)

~~~json
{
  "source": "00adcc10",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcc1c`](#insn-00adcc1c)

~~~json
{
  "source": "00adcc1c",
  "target": "00bf7058",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00bf7058",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00adcc50`](#insn-00adcc50)

~~~json
{
  "source": "00adcc50",
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
- 参照命令 [`00adcc54`](#insn-00adcc54)

~~~json
{
  "source": "00adcc54",
  "target": "00add070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcc60`](#insn-00adcc60)

~~~json
{
  "source": "00adcc60",
  "target": "Stack[-0x95]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcc64`](#insn-00adcc64)

~~~json
{
  "source": "00adcc64",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcc70`](#insn-00adcc70)

~~~json
{
  "source": "00adcc70",
  "target": "002a9f2e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a9f2e",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "696d673030352e706e6700",
  "capture_start": "002a9f2e",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00adcc74`](#insn-00adcc74)

~~~json
{
  "source": "00adcc74",
  "target": "Stack[-0x97]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcc7c`](#insn-00adcc7c)

~~~json
{
  "source": "00adcc7c",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcc80`](#insn-00adcc80)

~~~json
{
  "source": "00adcc80",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcc8c`](#insn-00adcc8c)

~~~json
{
  "source": "00adcc8c",
  "target": "0029fe44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcc90`](#insn-00adcc90)

~~~json
{
  "source": "00adcc90",
  "target": "0029fe49",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029fe49",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "352e696d6763757400",
  "capture_start": "0029fe49",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00adcc94`](#insn-00adcc94)

~~~json
{
  "source": "00adcc94",
  "target": "Stack[-0xaa]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcc98`](#insn-00adcc98)

~~~json
{
  "source": "00adcc98",
  "target": "Stack[-0xb7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcc9c`](#insn-00adcc9c)

~~~json
{
  "source": "00adcc9c",
  "target": "Stack[-0xb2]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adccb4`](#insn-00adccb4)

~~~json
{
  "source": "00adccb4",
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
- 参照命令 [`00adccbc`](#insn-00adccbc)

~~~json
{
  "source": "00adccbc",
  "target": "0045b734",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adccc0`](#insn-00adccc0)

~~~json
{
  "source": "00adccc0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adccc8`](#insn-00adccc8)

~~~json
{
  "source": "00adccc8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adccd0`](#insn-00adccd0)

~~~json
{
  "source": "00adccd0",
  "target": "00adcce4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adccdc`](#insn-00adccdc)

~~~json
{
  "source": "00adccdc",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcce0`](#insn-00adcce0)

~~~json
{
  "source": "00adcce0",
  "target": "00adcd18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcce4`](#insn-00adcce4)

~~~json
{
  "source": "00adcce4",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcce8`](#insn-00adcce8)

~~~json
{
  "source": "00adcce8",
  "target": "00adccfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adccf4`](#insn-00adccf4)

~~~json
{
  "source": "00adccf4",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adccf8`](#insn-00adccf8)

~~~json
{
  "source": "00adccf8",
  "target": "00adcd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adccfc`](#insn-00adccfc)

~~~json
{
  "source": "00adccfc",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd00`](#insn-00adcd00)

~~~json
{
  "source": "00adcd00",
  "target": "00adcd5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd04`](#insn-00adcd04)

~~~json
{
  "source": "00adcd04",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd08`](#insn-00adcd08)

~~~json
{
  "source": "00adcd08",
  "target": "00adcd6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd0c`](#insn-00adcd0c)

~~~json
{
  "source": "00adcd0c",
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
- 参照命令 [`00adcd10`](#insn-00adcd10)

~~~json
{
  "source": "00adcd10",
  "target": "00adcd7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd14`](#insn-00adcd14)

~~~json
{
  "source": "00adcd14",
  "target": "00add0c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd2c`](#insn-00adcd2c)

~~~json
{
  "source": "00adcd2c",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcd30`](#insn-00adcd30)

~~~json
{
  "source": "00adcd30",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd34`](#insn-00adcd34)

~~~json
{
  "source": "00adcd34",
  "target": "00adccec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd38`](#insn-00adcd38)

~~~json
{
  "source": "00adcd38",
  "target": "00adccfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd50`](#insn-00adcd50)

~~~json
{
  "source": "00adcd50",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcd54`](#insn-00adcd54)

~~~json
{
  "source": "00adcd54",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd58`](#insn-00adcd58)

~~~json
{
  "source": "00adcd58",
  "target": "00adcd04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd5c`](#insn-00adcd5c)

~~~json
{
  "source": "00adcd5c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd60`](#insn-00adcd60)

~~~json
{
  "source": "00adcd60",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcd64`](#insn-00adcd64)

~~~json
{
  "source": "00adcd64",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd68`](#insn-00adcd68)

~~~json
{
  "source": "00adcd68",
  "target": "00adcd0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd6c`](#insn-00adcd6c)

~~~json
{
  "source": "00adcd6c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd70`](#insn-00adcd70)

~~~json
{
  "source": "00adcd70",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcd74`](#insn-00adcd74)

~~~json
{
  "source": "00adcd74",
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
- 参照命令 [`00adcd78`](#insn-00adcd78)

~~~json
{
  "source": "00adcd78",
  "target": "00add0c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd84`](#insn-00adcd84)

~~~json
{
  "source": "00adcd84",
  "target": "Stack[-0x93]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd88`](#insn-00adcd88)

~~~json
{
  "source": "00adcd88",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcd94`](#insn-00adcd94)

~~~json
{
  "source": "00adcd94",
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
- 参照命令 [`00adcd9c`](#insn-00adcd9c)

~~~json
{
  "source": "00adcd9c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcda0`](#insn-00adcda0)

~~~json
{
  "source": "00adcda0",
  "target": "Stack[-0x97]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcda8`](#insn-00adcda8)

~~~json
{
  "source": "00adcda8",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcdb4`](#insn-00adcdb4)

~~~json
{
  "source": "00adcdb4",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcdb8`](#insn-00adcdb8)

~~~json
{
  "source": "00adcdb8",
  "target": "002ad239",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcdbc`](#insn-00adcdbc)

~~~json
{
  "source": "00adcdbc",
  "target": "002ad240",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad240",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "312e696d6763757400",
  "capture_start": "002ad240",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00adcdc0`](#insn-00adcdc0)

~~~json
{
  "source": "00adcdc0",
  "target": "Stack[-0xb7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcdc4`](#insn-00adcdc4)

~~~json
{
  "source": "00adcdc4",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcdd4`](#insn-00adcdd4)

~~~json
{
  "source": "00adcdd4",
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
- 参照命令 [`00adcddc`](#insn-00adcddc)

~~~json
{
  "source": "00adcddc",
  "target": "0045b734",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcde0`](#insn-00adcde0)

~~~json
{
  "source": "00adcde0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcde8`](#insn-00adcde8)

~~~json
{
  "source": "00adcde8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcdf0`](#insn-00adcdf0)

~~~json
{
  "source": "00adcdf0",
  "target": "00adce04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcdfc`](#insn-00adcdfc)

~~~json
{
  "source": "00adcdfc",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adce00`](#insn-00adce00)

~~~json
{
  "source": "00adce00",
  "target": "00adcfe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce04`](#insn-00adce04)

~~~json
{
  "source": "00adce04",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce08`](#insn-00adce08)

~~~json
{
  "source": "00adce08",
  "target": "00adce1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce14`](#insn-00adce14)

~~~json
{
  "source": "00adce14",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adce18`](#insn-00adce18)

~~~json
{
  "source": "00adce18",
  "target": "00add004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce1c`](#insn-00adce1c)

~~~json
{
  "source": "00adce1c",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce20`](#insn-00adce20)

~~~json
{
  "source": "00adce20",
  "target": "00adce2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce24`](#insn-00adce24)

~~~json
{
  "source": "00adce24",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce28`](#insn-00adce28)

~~~json
{
  "source": "00adce28",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adce2c`](#insn-00adce2c)

~~~json
{
  "source": "00adce2c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce30`](#insn-00adce30)

~~~json
{
  "source": "00adce30",
  "target": "00adce3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce34`](#insn-00adce34)

~~~json
{
  "source": "00adce34",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce38`](#insn-00adce38)

~~~json
{
  "source": "00adce38",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adce40`](#insn-00adce40)

~~~json
{
  "source": "00adce40",
  "target": "00821cb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adce48`](#insn-00adce48)

~~~json
{
  "source": "00adce48",
  "target": "00adcec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce54`](#insn-00adce54)

~~~json
{
  "source": "00adce54",
  "target": "008321a8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adce58`](#insn-00adce58)

~~~json
{
  "source": "00adce58",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce60`](#insn-00adce60)

~~~json
{
  "source": "00adce60",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce68`](#insn-00adce68)

~~~json
{
  "source": "00adce68",
  "target": "00adce94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce74`](#insn-00adce74)

~~~json
{
  "source": "00adce74",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adce78`](#insn-00adce78)

~~~json
{
  "source": "00adce78",
  "target": "00adce94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce90`](#insn-00adce90)

~~~json
{
  "source": "00adce90",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adce94`](#insn-00adce94)

~~~json
{
  "source": "00adce94",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adce98`](#insn-00adce98)

~~~json
{
  "source": "00adce98",
  "target": "00adcec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcea4`](#insn-00adcea4)

~~~json
{
  "source": "00adcea4",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcea8`](#insn-00adcea8)

~~~json
{
  "source": "00adcea8",
  "target": "00adcec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcec0`](#insn-00adcec0)

~~~json
{
  "source": "00adcec0",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcec4`](#insn-00adcec4)

~~~json
{
  "source": "00adcec4",
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
- 参照命令 [`00adcec8`](#insn-00adcec8)

~~~json
{
  "source": "00adcec8",
  "target": "00add11c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adced8`](#insn-00adced8)

~~~json
{
  "source": "00adced8",
  "target": "0029dc24",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029dc24",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "756e6c6f636b706f7075705f47756964655f3100",
  "capture_start": "0029dc24",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00adcee4`](#insn-00adcee4)

~~~json
{
  "source": "00adcee4",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcee8`](#insn-00adcee8)

~~~json
{
  "source": "00adcee8",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adceec`](#insn-00adceec)

~~~json
{
  "source": "00adceec",
  "target": "Stack[-0xb7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcef0`](#insn-00adcef0)

~~~json
{
  "source": "00adcef0",
  "target": "Stack[-0xa4]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcefc`](#insn-00adcefc)

~~~json
{
  "source": "00adcefc",
  "target": "00469f7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcf08`](#insn-00adcf08)

~~~json
{
  "source": "00adcf08",
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
- 参照命令 [`00adcf0c`](#insn-00adcf0c)

~~~json
{
  "source": "00adcf0c",
  "target": "00c1adb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1adb0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00adcf0c`](#insn-00adcf0c)

~~~json
{
  "source": "00adcf0c",
  "target": "00c25018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c25018",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adcf28`](#insn-00adcf28)

~~~json
{
  "source": "00adcf28",
  "target": "0045ba04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcf2c`](#insn-00adcf2c)

~~~json
{
  "source": "00adcf2c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf34`](#insn-00adcf34)

~~~json
{
  "source": "00adcf34",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf3c`](#insn-00adcf3c)

~~~json
{
  "source": "00adcf3c",
  "target": "00adcf50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf48`](#insn-00adcf48)

~~~json
{
  "source": "00adcf48",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcf4c`](#insn-00adcf4c)

~~~json
{
  "source": "00adcf4c",
  "target": "00add028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf50`](#insn-00adcf50)

~~~json
{
  "source": "00adcf50",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf54`](#insn-00adcf54)

~~~json
{
  "source": "00adcf54",
  "target": "00adcf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf60`](#insn-00adcf60)

~~~json
{
  "source": "00adcf60",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcf64`](#insn-00adcf64)

~~~json
{
  "source": "00adcf64",
  "target": "00add04c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf68`](#insn-00adcf68)

~~~json
{
  "source": "00adcf68",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf6c`](#insn-00adcf6c)

~~~json
{
  "source": "00adcf6c",
  "target": "00adcf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf70`](#insn-00adcf70)

~~~json
{
  "source": "00adcf70",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf74`](#insn-00adcf74)

~~~json
{
  "source": "00adcf74",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcf78`](#insn-00adcf78)

~~~json
{
  "source": "00adcf78",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf7c`](#insn-00adcf7c)

~~~json
{
  "source": "00adcf7c",
  "target": "00adcf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf80`](#insn-00adcf80)

~~~json
{
  "source": "00adcf80",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcf84`](#insn-00adcf84)

~~~json
{
  "source": "00adcf84",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcf88`](#insn-00adcf88)

~~~json
{
  "source": "00adcf88",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcf98`](#insn-00adcf98)

~~~json
{
  "source": "00adcf98",
  "target": "00a618b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcf9c`](#insn-00adcf9c)

~~~json
{
  "source": "00adcf9c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcfac`](#insn-00adcfac)

~~~json
{
  "source": "00adcfac",
  "target": "007f8ecc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcfb4`](#insn-00adcfb4)

~~~json
{
  "source": "00adcfb4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcfbc`](#insn-00adcfbc)

~~~json
{
  "source": "00adcfbc",
  "target": "00add218",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcfc0`](#insn-00adcfc0)

~~~json
{
  "source": "00adcfc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcfc4`](#insn-00adcfc4)

~~~json
{
  "source": "00adcfc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcfc8`](#insn-00adcfc8)

~~~json
{
  "source": "00adcfc8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcfcc`](#insn-00adcfcc)

~~~json
{
  "source": "00adcfcc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcfd0`](#insn-00adcfd0)

~~~json
{
  "source": "00adcfd0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcfd4`](#insn-00adcfd4)

~~~json
{
  "source": "00adcfd4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcff4`](#insn-00adcff4)

~~~json
{
  "source": "00adcff4",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adcff8`](#insn-00adcff8)

~~~json
{
  "source": "00adcff8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adcffc`](#insn-00adcffc)

~~~json
{
  "source": "00adcffc",
  "target": "00adce0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add000`](#insn-00add000)

~~~json
{
  "source": "00add000",
  "target": "00adce1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add018`](#insn-00add018)

~~~json
{
  "source": "00add018",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add01c`](#insn-00add01c)

~~~json
{
  "source": "00add01c",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add020`](#insn-00add020)

~~~json
{
  "source": "00add020",
  "target": "00adce24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add024`](#insn-00add024)

~~~json
{
  "source": "00add024",
  "target": "00adce2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add03c`](#insn-00add03c)

~~~json
{
  "source": "00add03c",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add040`](#insn-00add040)

~~~json
{
  "source": "00add040",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add044`](#insn-00add044)

~~~json
{
  "source": "00add044",
  "target": "00adcf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add048`](#insn-00add048)

~~~json
{
  "source": "00add048",
  "target": "00adcf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add060`](#insn-00add060)

~~~json
{
  "source": "00add060",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add064`](#insn-00add064)

~~~json
{
  "source": "00add064",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add068`](#insn-00add068)

~~~json
{
  "source": "00add068",
  "target": "00adcf70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add06c`](#insn-00add06c)

~~~json
{
  "source": "00add06c",
  "target": "00adcf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add074`](#insn-00add074)

~~~json
{
  "source": "00add074",
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
- 参照命令 [`00add078`](#insn-00add078)

~~~json
{
  "source": "00add078",
  "target": "00bdaf00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add07c`](#insn-00add07c)

~~~json
{
  "source": "00add07c",
  "target": "00adcc58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add084`](#insn-00add084)

~~~json
{
  "source": "00add084",
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
- 参照命令 [`00add08c`](#insn-00add08c)

~~~json
{
  "source": "00add08c",
  "target": "0045bedc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add098`](#insn-00add098)

~~~json
{
  "source": "00add098",
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
- 参照命令 [`00add09c`](#insn-00add09c)

~~~json
{
  "source": "00add09c",
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
- 参照命令 [`00add0a0`](#insn-00add0a0)

~~~json
{
  "source": "00add0a0",
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
- 参照命令 [`00add0a0`](#insn-00add0a0)

~~~json
{
  "source": "00add0a0",
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
- 参照命令 [`00add0a8`](#insn-00add0a8)

~~~json
{
  "source": "00add0a8",
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
- 参照命令 [`00add0a8`](#insn-00add0a8)

~~~json
{
  "source": "00add0a8",
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
- 参照命令 [`00add0ac`](#insn-00add0ac)

~~~json
{
  "source": "00add0ac",
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
- 参照命令 [`00add0b0`](#insn-00add0b0)

~~~json
{
  "source": "00add0b0",
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
- 参照命令 [`00add0b0`](#insn-00add0b0)

~~~json
{
  "source": "00add0b0",
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
- 参照命令 [`00add0b0`](#insn-00add0b0)

~~~json
{
  "source": "00add0b0",
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
- 参照命令 [`00add0b4`](#insn-00add0b4)

~~~json
{
  "source": "00add0b4",
  "target": "00bdaee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add0bc`](#insn-00add0bc)

~~~json
{
  "source": "00add0bc",
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
- 参照命令 [`00add0c0`](#insn-00add0c0)

~~~json
{
  "source": "00add0c0",
  "target": "00bdaf20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add0c4`](#insn-00add0c4)

~~~json
{
  "source": "00add0c4",
  "target": "00adcc58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add0cc`](#insn-00add0cc)

~~~json
{
  "source": "00add0cc",
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
- 参照命令 [`00add0d0`](#insn-00add0d0)

~~~json
{
  "source": "00add0d0",
  "target": "00bdaf00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add0d4`](#insn-00add0d4)

~~~json
{
  "source": "00add0d4",
  "target": "00adcd7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add0e0`](#insn-00add0e0)

~~~json
{
  "source": "00add0e0",
  "target": "0045bedc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add0e4`](#insn-00add0e4)

~~~json
{
  "source": "00add0e4",
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
- 参照命令 [`00add0ec`](#insn-00add0ec)

~~~json
{
  "source": "00add0ec",
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
- 参照命令 [`00add0f0`](#insn-00add0f0)

~~~json
{
  "source": "00add0f0",
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
- 参照命令 [`00add0f0`](#insn-00add0f0)

~~~json
{
  "source": "00add0f0",
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
- 参照命令 [`00add0f8`](#insn-00add0f8)

~~~json
{
  "source": "00add0f8",
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
- 参照命令 [`00add0fc`](#insn-00add0fc)

~~~json
{
  "source": "00add0fc",
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
- 参照命令 [`00add0fc`](#insn-00add0fc)

~~~json
{
  "source": "00add0fc",
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
- 参照命令 [`00add100`](#insn-00add100)

~~~json
{
  "source": "00add100",
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
- 参照命令 [`00add104`](#insn-00add104)

~~~json
{
  "source": "00add104",
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
- 参照命令 [`00add104`](#insn-00add104)

~~~json
{
  "source": "00add104",
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
- 参照命令 [`00add104`](#insn-00add104)

~~~json
{
  "source": "00add104",
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
- 参照命令 [`00add108`](#insn-00add108)

~~~json
{
  "source": "00add108",
  "target": "00bdaee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add110`](#insn-00add110)

~~~json
{
  "source": "00add110",
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
- 参照命令 [`00add114`](#insn-00add114)

~~~json
{
  "source": "00add114",
  "target": "00bdaf20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add118`](#insn-00add118)

~~~json
{
  "source": "00add118",
  "target": "00adcd7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add120`](#insn-00add120)

~~~json
{
  "source": "00add120",
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
- 参照命令 [`00add124`](#insn-00add124)

~~~json
{
  "source": "00add124",
  "target": "00bdaf00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add128`](#insn-00add128)

~~~json
{
  "source": "00add128",
  "target": "00adcecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add134`](#insn-00add134)

~~~json
{
  "source": "00add134",
  "target": "0045bedc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add138`](#insn-00add138)

~~~json
{
  "source": "00add138",
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
- 参照命令 [`00add140`](#insn-00add140)

~~~json
{
  "source": "00add140",
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
- 参照命令 [`00add144`](#insn-00add144)

~~~json
{
  "source": "00add144",
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
- 参照命令 [`00add144`](#insn-00add144)

~~~json
{
  "source": "00add144",
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
- 参照命令 [`00add14c`](#insn-00add14c)

~~~json
{
  "source": "00add14c",
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
- 参照命令 [`00add150`](#insn-00add150)

~~~json
{
  "source": "00add150",
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
- 参照命令 [`00add150`](#insn-00add150)

~~~json
{
  "source": "00add150",
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
- 参照命令 [`00add154`](#insn-00add154)

~~~json
{
  "source": "00add154",
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
- 参照命令 [`00add158`](#insn-00add158)

~~~json
{
  "source": "00add158",
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
- 参照命令 [`00add158`](#insn-00add158)

~~~json
{
  "source": "00add158",
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
- 参照命令 [`00add158`](#insn-00add158)

~~~json
{
  "source": "00add158",
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
- 参照命令 [`00add15c`](#insn-00add15c)

~~~json
{
  "source": "00add15c",
  "target": "00bdaee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add164`](#insn-00add164)

~~~json
{
  "source": "00add164",
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
- 参照命令 [`00add168`](#insn-00add168)

~~~json
{
  "source": "00add168",
  "target": "00bdaf20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00add16c`](#insn-00add16c)

~~~json
{
  "source": "00add16c",
  "target": "00adcecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00add218`](#insn-00add218)

~~~json
{
  "source": "00add218",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
