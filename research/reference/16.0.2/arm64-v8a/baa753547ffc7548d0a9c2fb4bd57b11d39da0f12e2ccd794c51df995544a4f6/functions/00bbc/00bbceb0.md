# 00bbceb0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbce14`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbce14.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0079.md#compare-99ae576ef2523ab2cf55661e31ec796c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bbdea4`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbdea4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0079.md#compare-2c47f789ce52762215fe761cede82ed5)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbceb0",
  "name": "_ZN8firebase9messaging11DeleteTokenEv",
  "size": 468,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3e5450053770b82385cca4d81e7c3393c233488dccf84054f4585ca1a837998c",
  "source_text_sha256": "3e5450053770b82385cca4d81e7c3393c233488dccf84054f4585ca1a837998c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbceb0",
        "00bbd083"
      ]
    ],
    "bytes_sha256": "3b775c5d37c492eddafe164d28748ed8d01c31d81a84715bcd9fa3a61e6489d9",
    "instruction_count": 117,
    "instruction_bytes": 468,
    "body_bytes": 468,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497874](../00497/00497874.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5aad0](../00c5a/00c5aad0.md)
- [00c5aae0](../00c5a/00c5aae0.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5acb0](../00c5a/00c5acb0.md)
- [00c5ad40](../00c5a/00c5ad40.md)
- [00c5ad70](../00c5a/00c5ad70.md)
- [00c5ae70](../00c5a/00c5ae70.md)
- [00c5aea0](../00c5a/00c5aea0.md)
- [00c5aed0](../00c5a/00c5aed0.md)
- [00c5af10](../00c5a/00c5af10.md)
- [00c5b010](../00c5b/00c5b010.md)
- [00c5b030](../00c5b/00c5b030.md)
- [00c5b040](../00c5b/00c5b040.md)
- [00c5b0d0](../00c5b/00c5b0d0.md)
- [00c5b150](../00c5b/00c5b150.md)
- [00c5d340](../00c5d/00c5d340.md)

## 関連文字列（未確認候補）

~~~text
"Messaging"
"Messaging not initialized."
"internal::IsInitialized()"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3539 bytes

~~~c

void _ZN8firebase9messaging11DeleteTokenEv(long param_1)

{
  ulong uVar1;
  void *pvVar2;
  long lVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  long *plVar6;
  undefined8 uVar7;
  undefined1 auStack_88 [16];
  byte local_78 [8];
  ulong local_70;
  void *local_68;
  undefined8 local_60 [2];
  undefined1 auStack_50 [8];
  long local_48;
  
                    /* catch() { ... } // from try @ 00bbcbf8 with catch @ 00bbceb0 */
  uVar4 = DAT_01126470;
  lVar3 = tpidr_el0;
                    /* catch() { ... } // from try @ 00bbc980 with catch @ 00bbcecc */
  local_48 = *(long *)(lVar3 + 0x28);
                    /* catch() { ... } // from try @ 00bbcd4c with catch @ 00bbcedc */
                    /* catch() { ... } // from try @ 00bbce4c with catch @ 00bbcee0 */
  if (DAT_01126460 == 0) {
    _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
    _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
                    /* catch() { ... } // from try @ 00bbce34 with catch @ 00bbcee4 */
                    /* catch() { ... } // from try @ 00bbcc40 with catch @ 00bbcee8 */
                    /* catch() { ... } // from try @ 00bbce18 with catch @ 00bbceec
                       catch() { ... } // from try @ 00bbce68 with catch @ 00bbceec */
    _ZN8firebase5Mutex7AcquireEv(DAT_01126470);
    uVar5 = _ZN8firebase9messaging10FutureData3GetEv();
    _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E(local_78,uVar5,4,0,0);
    _ZN8firebase12FutureHandleC1ERKS0_(local_60,local_78);
    _ZN8firebase12FutureHandleD2Ev(local_78);
    plVar6 = (long *)_ZNK8firebase3App9GetJNIEnvEv(DAT_01126460);
    uVar7 = FUN_00497874(plVar6,DAT_01126498,DAT_011263f8);
    _ZN8firebase4util27GetAndClearExceptionMessageEP7_JNIEnv(local_78,plVar6);
    uVar1 = (ulong)(local_78[0] >> 1);
    if ((local_78[0] & 1) != 0) {
      uVar1 = local_70;
    }
    if (uVar1 == 0) {
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (plVar6,uVar7,FUN_00bbc344,local_60[0],"Messaging");
    }
    else {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_88,local_60);
      pvVar2 = (void *)((ulong)local_78 | 1);
      if ((local_78[0] & 1) != 0) {
        pvVar2 = local_68;
      }
      _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
                (uVar5,auStack_88,0xffffffff,pvVar2,auStack_50);
      _ZN8firebase12FutureHandleD2Ev(auStack_88);
    }
    (**(code **)(*plVar6 + 0xb8))(plVar6,uVar7);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar6);
    _ZN8firebase6FutureIvEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,uVar5,local_60);
    if ((local_78[0] & 1) != 0) {
      _ZdlPv(local_68);
    }
    _ZN8firebase12FutureHandleD2Ev(local_60);
    _ZN8firebase5Mutex7ReleaseEv(uVar4);
  }
  if (*(long *)(lVar3 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00bbd080 to 00cbd2a7 has its CatchHandler @ 00bbd080
                       catch() { ... } // from try @ 00bbd080 with catch @ 00bbd080
                       catch() { ... } // from try @ 00bbd2cc with catch @ 00bbd080 */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbceb0"></a> `00bbceb0` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bbceb4"></a> `00bbceb4` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbceb8"></a> `00bbceb8` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbcebc"></a> `00bbcebc` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbcec0"></a> `00bbcec0` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bbcec4"></a> `00bbcec4` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bbcec8"></a> `00bbcec8` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bbcecc"></a> `00bbcecc` | `09 17 40 f9` | ldr x9,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bbced0"></a> `00bbced0` | `56 2b 00 d0` | adrp x22,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbced4"></a> `00bbced4` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00bbced8"></a> `00bbced8` | `a9 83 1c f8` | stur x9,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00bbcedc"></a> `00bbcedc` | `c9 32 42 f9` | ldr x9,[x22, #0x460] | `FALL_THROUGH`
<a id="insn-00bbcee0"></a> `00bbcee0` | `89 06 00 b4` | cbz x9,0x00bbcfb0 | `CONDITIONAL_JUMP`
<a id="insn-00bbcee4"></a> `00bbcee4` | `48 2b 00 d0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbcee8"></a> `00bbcee8` | `13 39 42 f9` | ldr x19,[x8, #0x470] | `FALL_THROUGH`
<a id="insn-00bbceec"></a> `00bbceec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbcef0"></a> `00bbcef0` | `f8 76 02 94` | bl 0x00c5aad0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcef4"></a> `00bbcef4` | `13 81 02 94` | bl 0x00c5d340 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcef8"></a> `00bbcef8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bbcefc"></a> `00bbcefc` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbcf00"></a> `00bbcf00` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00bbcf04"></a> `00bbcf04` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bbcf08"></a> `00bbcf08` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbcf0c"></a> `00bbcf0c` | `01 78 02 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcf10"></a> `00bbcf10` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bbcf14"></a> `00bbcf14` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbcf18"></a> `00bbcf18` | `ee 77 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcf1c"></a> `00bbcf1c` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbcf20"></a> `00bbcf20` | `10 77 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcf24"></a> `00bbcf24` | `c0 32 42 f9` | ldr x0,[x22, #0x460] | `FALL_THROUGH`
<a id="insn-00bbcf28"></a> `00bbcf28` | `8a 78 02 94` | bl 0x00c5b150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcf2c"></a> `00bbcf2c` | `48 2b 00 d0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbcf30"></a> `00bbcf30` | `49 2b 00 d0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbcf34"></a> `00bbcf34` | `01 4d 42 f9` | ldr x1,[x8, #0x498] | `FALL_THROUGH`
<a id="insn-00bbcf38"></a> `00bbcf38` | `22 fd 41 f9` | ldr x2,[x9, #0x3f8] | `FALL_THROUGH`
<a id="insn-00bbcf3c"></a> `00bbcf3c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbcf40"></a> `00bbcf40` | `4d 6a e3 97` | bl 0x00497874 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcf44"></a> `00bbcf44` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bbcf48"></a> `00bbcf48` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbcf4c"></a> `00bbcf4c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbcf50"></a> `00bbcf50` | `3c 78 02 94` | bl 0x00c5b040 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcf54"></a> `00bbcf54` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbcf58"></a> `00bbcf58` | `e9 13 40 f9` | ldr x9,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbcf5c"></a> `00bbcf5c` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcf60"></a> `00bbcf60` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcf64"></a> `00bbcf64` | `48 01 89 9a` | csel x8,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bbcf68"></a> `00bbcf68` | `28 04 00 b4` | cbz x8,0x00bbcfec | `CONDITIONAL_JUMP`
<a id="insn-00bbcf6c"></a> `00bbcf6c` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bbcf70"></a> `00bbcf70` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bbcf74"></a> `00bbcf74` | `d7 77 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcf78"></a> `00bbcf78` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbcf7c"></a> `00bbcf7c` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bbcf80"></a> `00bbcf80` | `ea 63 00 91` | add x10,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbcf84"></a> `00bbcf84` | `4a 01 40 b2` | orr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcf88"></a> `00bbcf88` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcf8c"></a> `00bbcf8c` | `43 01 89 9a` | csel x3,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bbcf90"></a> `00bbcf90` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bbcf94"></a> `00bbcf94` | `e4 03 01 91` | add x4,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bbcf98"></a> `00bbcf98` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-00bbcf9c"></a> `00bbcf9c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbcfa0"></a> `00bbcfa0` | `b4 77 02 94` | bl 0x00c5ae70 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcfa4"></a> `00bbcfa4` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bbcfa8"></a> `00bbcfa8` | `ee 76 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcfac"></a> `00bbcfac` | `18 00 00 14` | b 0x00bbd00c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbcfb0"></a> `00bbcfb0` | `20 b7 ff d0` | adrp x0,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bbcfb4"></a> `00bbcfb4` | `00 20 23 91` | add x0,x0,#0x8c8 | `FALL_THROUGH`
<a id="insn-00bbcfb8"></a> `00bbcfb8` | `6e 77 02 94` | bl 0x00c5ad70 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcfbc"></a> `00bbcfbc` | `a0 b7 ff 90` | adrp x0,0x2b0000 | `FALL_THROUGH`
<a id="insn-00bbcfc0"></a> `00bbcfc0` | `00 6c 1c 91` | add x0,x0,#0x71b | `FALL_THROUGH`
<a id="insn-00bbcfc4"></a> `00bbcfc4` | `43 78 02 94` | bl 0x00c5b0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcfc8"></a> `00bbcfc8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbcfcc"></a> `00bbcfcc` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbcfd0"></a> `00bbcfd0` | `5c 77 02 94` | bl 0x00c5ad40 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcfd4"></a> `00bbcfd4` | `80 c2 00 91` | add x0,x20,#0x30 | `FALL_THROUGH`
<a id="insn-00bbcfd8"></a> `00bbcfd8` | `9f 16 00 f9` | str xzr,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bbcfdc"></a> `00bbcfdc` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbcfe0"></a> `00bbcfe0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bbcfe4"></a> `00bbcfe4` | `33 77 02 94` | bl 0x00c5acb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcfe8"></a> `00bbcfe8` | `1c 00 00 14` | b 0x00bbd058 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbcfec"></a> `00bbcfec` | `e3 1b 40 f9` | ldr x3,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbcff0"></a> `00bbcff0` | `02 00 00 90` | adrp x2,0xbbc000 | `FALL_THROUGH`
<a id="insn-00bbcff4"></a> `00bbcff4` | `84 ba ff d0` | adrp x4,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbcff8"></a> `00bbcff8` | `42 10 0d 91` | add x2,x2,#0x344 | `FALL_THROUGH`
<a id="insn-00bbcffc"></a> `00bbcffc` | `84 04 20 91` | add x4,x4,#0x801 | `FALL_THROUGH`
<a id="insn-00bbd000"></a> `00bbd000` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbd004"></a> `00bbd004` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bbd008"></a> `00bbd008` | `02 78 02 94` | bl 0x00c5b010 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd00c"></a> `00bbd00c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bbd010"></a> `00bbd010` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bbd014"></a> `00bbd014` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbd018"></a> `00bbd018` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bbd01c"></a> `00bbd01c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbd020"></a> `00bbd020` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbd024"></a> `00bbd024` | `03 78 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd028"></a> `00bbd028` | `e2 c3 00 91` | add x2,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bbd02c"></a> `00bbd02c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbd030"></a> `00bbd030` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbd034"></a> `00bbd034` | `9b 77 02 94` | bl 0x00c5aea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd038"></a> `00bbd038` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbd03c"></a> `00bbd03c` | `68 00 00 36` | tbz w8,#0x0,0x00bbd048 | `CONDITIONAL_JUMP`
<a id="insn-00bbd040"></a> `00bbd040` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bbd044"></a> `00bbd044` | `cf 6b 02 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd048"></a> `00bbd048` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bbd04c"></a> `00bbd04c` | `c5 76 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd050"></a> `00bbd050` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd054"></a> `00bbd054` | `a3 76 02 94` | bl 0x00c5aae0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd058"></a> `00bbd058` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bbd05c"></a> `00bbd05c` | `a9 83 5c f8` | ldur x9,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00bbd060"></a> `00bbd060` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbd064"></a> `00bbd064` | `e1 00 00 54` | b.ne 0x00bbd080 | `CONDITIONAL_JUMP`
<a id="insn-00bbd068"></a> `00bbd068` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bbd06c"></a> `00bbd06c` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbd070"></a> `00bbd070` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbd074"></a> `00bbd074` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbd078"></a> `00bbd078` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bbd07c"></a> `00bbd07c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbd080"></a> `00bbd080` | `cc 6b 02 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbceb0`](#insn-00bbceb0) 範囲 `[['00bbceb0', '00bbcecb']]`
  - `FALL_THROUGH` [`00bbcec8`](#insn-00bbcec8) → [`00bbcecc`](#insn-00bbcecc)
- ブロック [`00bbcecc`](#insn-00bbcecc) 範囲 `[['00bbcecc', '00bbcedb']]`
  - `FALL_THROUGH` [`00bbced8`](#insn-00bbced8) → [`00bbcedc`](#insn-00bbcedc)
- ブロック [`00bbcedc`](#insn-00bbcedc) 範囲 `[['00bbcedc', '00bbcedf']]`
  - `FALL_THROUGH` [`00bbcedc`](#insn-00bbcedc) → [`00bbcee0`](#insn-00bbcee0)
- ブロック [`00bbcee0`](#insn-00bbcee0) 範囲 `[['00bbcee0', '00bbcee3']]`
  - `CONDITIONAL_JUMP` [`00bbcee0`](#insn-00bbcee0) → [`00bbcfb0`](#insn-00bbcfb0)
  - `FALL_THROUGH` [`00bbcee0`](#insn-00bbcee0) → [`00bbcee4`](#insn-00bbcee4)
- ブロック [`00bbcee4`](#insn-00bbcee4) 範囲 `[['00bbcee4', '00bbcee7']]`
  - `FALL_THROUGH` [`00bbcee4`](#insn-00bbcee4) → [`00bbcee8`](#insn-00bbcee8)
- ブロック [`00bbcee8`](#insn-00bbcee8) 範囲 `[['00bbcee8', '00bbceeb']]`
  - `FALL_THROUGH` [`00bbcee8`](#insn-00bbcee8) → [`00bbceec`](#insn-00bbceec)
- ブロック [`00bbceec`](#insn-00bbceec) 範囲 `[['00bbceec', '00bbcf6b']]`
  - `CONDITIONAL_JUMP` [`00bbcf68`](#insn-00bbcf68) → [`00bbcfec`](#insn-00bbcfec)
  - `FALL_THROUGH` [`00bbcf68`](#insn-00bbcf68) → [`00bbcf6c`](#insn-00bbcf6c)
- ブロック [`00bbcf6c`](#insn-00bbcf6c) 範囲 `[['00bbcf6c', '00bbcfaf']]`
  - `UNCONDITIONAL_JUMP` [`00bbcfac`](#insn-00bbcfac) → [`00bbd00c`](#insn-00bbd00c)
- ブロック [`00bbcfb0`](#insn-00bbcfb0) 範囲 `[['00bbcfb0', '00bbcfeb']]`
  - `UNCONDITIONAL_JUMP` [`00bbcfe8`](#insn-00bbcfe8) → [`00bbd058`](#insn-00bbd058)
- ブロック [`00bbcfec`](#insn-00bbcfec) 範囲 `[['00bbcfec', '00bbd00b']]`
  - `FALL_THROUGH` [`00bbd008`](#insn-00bbd008) → [`00bbd00c`](#insn-00bbd00c)
- ブロック [`00bbd00c`](#insn-00bbd00c) 範囲 `[['00bbd00c', '00bbd03f']]`
  - `CONDITIONAL_JUMP` [`00bbd03c`](#insn-00bbd03c) → [`00bbd048`](#insn-00bbd048)
  - `FALL_THROUGH` [`00bbd03c`](#insn-00bbd03c) → [`00bbd040`](#insn-00bbd040)
- ブロック [`00bbd040`](#insn-00bbd040) 範囲 `[['00bbd040', '00bbd047']]`
  - `FALL_THROUGH` [`00bbd044`](#insn-00bbd044) → [`00bbd048`](#insn-00bbd048)
- ブロック [`00bbd048`](#insn-00bbd048) 範囲 `[['00bbd048', '00bbd057']]`
  - `FALL_THROUGH` [`00bbd054`](#insn-00bbd054) → [`00bbd058`](#insn-00bbd058)
- ブロック [`00bbd058`](#insn-00bbd058) 範囲 `[['00bbd058', '00bbd067']]`
  - `CONDITIONAL_JUMP` [`00bbd064`](#insn-00bbd064) → [`00bbd080`](#insn-00bbd080)
  - `FALL_THROUGH` [`00bbd064`](#insn-00bbd064) → [`00bbd068`](#insn-00bbd068)
- ブロック [`00bbd068`](#insn-00bbd068) 範囲 `[['00bbd068', '00bbd07f']]`
- ブロック [`00bbd080`](#insn-00bbd080) 範囲 `[['00bbd080', '00bbd083']]`

## 命令位置別の参照

- [`00bbceb4`](#insn-00bbceb4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbceb8`](#insn-00bbceb8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcebc`](#insn-00bbcebc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcec0`](#insn-00bbcec0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbced8`](#insn-00bbced8) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcedc`](#insn-00bbcedc) → `01126460`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbcee0`](#insn-00bbcee0) → [`00bbcfb0`](#insn-00bbcfb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcee8`](#insn-00bbcee8) → `01126470`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbcef0`](#insn-00bbcef0) → [`00c5aad0`](../00c5a/00c5aad0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aad0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcef4`](#insn-00bbcef4) → [`00c5d340`](../00c5d/00c5d340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d340` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf0c`](#insn-00bbcf0c) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf18`](#insn-00bbcf18) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf20`](#insn-00bbcf20) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf24`](#insn-00bbcf24) → `01126460`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbcf28`](#insn-00bbcf28) → [`00c5b150`](../00c5b/00c5b150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b150` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf34`](#insn-00bbcf34) → `01126498`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbcf38`](#insn-00bbcf38) → `011263f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbcf40`](#insn-00bbcf40) → [`00497874`](../00497/00497874.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497874` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf50`](#insn-00bbcf50) → [`00c5b040`](../00c5b/00c5b040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b040` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf54`](#insn-00bbcf54) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf58`](#insn-00bbcf58) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf68`](#insn-00bbcf68) → [`00bbcfec`](#insn-00bbcfec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf74`](#insn-00bbcf74) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf78`](#insn-00bbcf78) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf7c`](#insn-00bbcf7c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcfa0`](#insn-00bbcfa0) → [`00c5ae70`](../00c5a/00c5ae70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae70` · 推定シンボル `None` · 推定型 `None`
- [`00bbcfa8`](#insn-00bbcfa8) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bbcfac`](#insn-00bbcfac) → [`00bbd00c`](#insn-00bbd00c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcfb4`](#insn-00bbcfb4) → `002a28c8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbcfb8`](#insn-00bbcfb8) → [`00c5ad70`](../00c5a/00c5ad70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad70` · 推定シンボル `None` · 推定型 `None`
- [`00bbcfc0`](#insn-00bbcfc0) → `002b071b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbcfc4`](#insn-00bbcfc4) → [`00c5b0d0`](../00c5b/00c5b0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcfd0`](#insn-00bbcfd0) → [`00c5ad40`](../00c5a/00c5ad40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad40` · 推定シンボル `None` · 推定型 `None`
- [`00bbcfe4`](#insn-00bbcfe4) → [`00c5acb0`](../00c5a/00c5acb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5acb0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcfe8`](#insn-00bbcfe8) → [`00bbd058`](#insn-00bbd058) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcfec`](#insn-00bbcfec) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcff8`](#insn-00bbcff8) → [`00bbc344`](00bbc344.md) · `PARAM` · `ANALYSIS` · 関数 `00bbc344` · 推定シンボル `None` · 推定型 `None`
- [`00bbcffc`](#insn-00bbcffc) → `0030e801`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbd008`](#insn-00bbd008) → [`00c5b010`](../00c5b/00c5b010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b010` · 推定シンボル `None` · 推定型 `None`
- [`00bbd024`](#insn-00bbd024) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bbd034`](#insn-00bbd034) → [`00c5aea0`](../00c5a/00c5aea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aea0` · 推定シンボル `None` · 推定型 `None`
- [`00bbd038`](#insn-00bbd038) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd03c`](#insn-00bbd03c) → [`00bbd048`](#insn-00bbd048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd040`](#insn-00bbd040) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd044`](#insn-00bbd044) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00bbd04c`](#insn-00bbd04c) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bbd054`](#insn-00bbd054) → [`00c5aae0`](../00c5a/00c5aae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aae0` · 推定シンボル `None` · 推定型 `None`
- [`00bbd05c`](#insn-00bbd05c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd064`](#insn-00bbd064) → [`00bbd080`](#insn-00bbd080) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd068`](#insn-00bbd068) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd06c`](#insn-00bbd06c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd070`](#insn-00bbd070) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd074`](#insn-00bbd074) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd080`](#insn-00bbd080) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbceb4`](#insn-00bbceb4)

~~~json
{
  "source": "00bbceb4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbceb8`](#insn-00bbceb8)

~~~json
{
  "source": "00bbceb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcebc`](#insn-00bbcebc)

~~~json
{
  "source": "00bbcebc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcec0`](#insn-00bbcec0)

~~~json
{
  "source": "00bbcec0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbced8`](#insn-00bbced8)

~~~json
{
  "source": "00bbced8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcedc`](#insn-00bbcedc)

~~~json
{
  "source": "00bbcedc",
  "target": "01126460",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126460",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbcee0`](#insn-00bbcee0)

~~~json
{
  "source": "00bbcee0",
  "target": "00bbcfb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcee8`](#insn-00bbcee8)

~~~json
{
  "source": "00bbcee8",
  "target": "01126470",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126470",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbcef0`](#insn-00bbcef0)

~~~json
{
  "source": "00bbcef0",
  "target": "00c5aad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcef4`](#insn-00bbcef4)

~~~json
{
  "source": "00bbcef4",
  "target": "00c5d340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcf0c`](#insn-00bbcf0c)

~~~json
{
  "source": "00bbcf0c",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcf18`](#insn-00bbcf18)

~~~json
{
  "source": "00bbcf18",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcf20`](#insn-00bbcf20)

~~~json
{
  "source": "00bbcf20",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcf24`](#insn-00bbcf24)

~~~json
{
  "source": "00bbcf24",
  "target": "01126460",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126460",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbcf28`](#insn-00bbcf28)

~~~json
{
  "source": "00bbcf28",
  "target": "00c5b150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcf34`](#insn-00bbcf34)

~~~json
{
  "source": "00bbcf34",
  "target": "01126498",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126498",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbcf38`](#insn-00bbcf38)

~~~json
{
  "source": "00bbcf38",
  "target": "011263f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011263f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbcf40`](#insn-00bbcf40)

~~~json
{
  "source": "00bbcf40",
  "target": "00497874",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcf50`](#insn-00bbcf50)

~~~json
{
  "source": "00bbcf50",
  "target": "00c5b040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcf54`](#insn-00bbcf54)

~~~json
{
  "source": "00bbcf54",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcf58`](#insn-00bbcf58)

~~~json
{
  "source": "00bbcf58",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcf68`](#insn-00bbcf68)

~~~json
{
  "source": "00bbcf68",
  "target": "00bbcfec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcf74`](#insn-00bbcf74)

~~~json
{
  "source": "00bbcf74",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcf78`](#insn-00bbcf78)

~~~json
{
  "source": "00bbcf78",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcf7c`](#insn-00bbcf7c)

~~~json
{
  "source": "00bbcf7c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcfa0`](#insn-00bbcfa0)

~~~json
{
  "source": "00bbcfa0",
  "target": "00c5ae70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcfa8`](#insn-00bbcfa8)

~~~json
{
  "source": "00bbcfa8",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcfac`](#insn-00bbcfac)

~~~json
{
  "source": "00bbcfac",
  "target": "00bbd00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcfb4`](#insn-00bbcfb4)

~~~json
{
  "source": "00bbcfb4",
  "target": "002a28c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a28c8",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "696e7465726e616c3a3a4973496e697469616c697a6564282900",
  "capture_start": "002a28c8",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbcfb8`](#insn-00bbcfb8)

~~~json
{
  "source": "00bbcfb8",
  "target": "00c5ad70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcfc0`](#insn-00bbcfc0)

~~~json
{
  "source": "00bbcfc0",
  "target": "002b071b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b071b",
  "offset": 0,
  "size": 27,
  "datatype": "string",
  "bytes": "4d6573736167696e67206e6f7420696e697469616c697a65642e00",
  "capture_start": "002b071b",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbcfc4`](#insn-00bbcfc4)

~~~json
{
  "source": "00bbcfc4",
  "target": "00c5b0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcfd0`](#insn-00bbcfd0)

~~~json
{
  "source": "00bbcfd0",
  "target": "00c5ad40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcfe4`](#insn-00bbcfe4)

~~~json
{
  "source": "00bbcfe4",
  "target": "00c5acb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcfe8`](#insn-00bbcfe8)

~~~json
{
  "source": "00bbcfe8",
  "target": "00bbd058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcfec`](#insn-00bbcfec)

~~~json
{
  "source": "00bbcfec",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcff8`](#insn-00bbcff8)

~~~json
{
  "source": "00bbcff8",
  "target": "00bbc344",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcffc`](#insn-00bbcffc)

~~~json
{
  "source": "00bbcffc",
  "target": "0030e801",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e801",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "4d6573736167696e6700",
  "capture_start": "0030e801",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbd008`](#insn-00bbd008)

~~~json
{
  "source": "00bbd008",
  "target": "00c5b010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd024`](#insn-00bbd024)

~~~json
{
  "source": "00bbd024",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd034`](#insn-00bbd034)

~~~json
{
  "source": "00bbd034",
  "target": "00c5aea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd038`](#insn-00bbd038)

~~~json
{
  "source": "00bbd038",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd03c`](#insn-00bbd03c)

~~~json
{
  "source": "00bbd03c",
  "target": "00bbd048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd040`](#insn-00bbd040)

~~~json
{
  "source": "00bbd040",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd044`](#insn-00bbd044)

~~~json
{
  "source": "00bbd044",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd04c`](#insn-00bbd04c)

~~~json
{
  "source": "00bbd04c",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd054`](#insn-00bbd054)

~~~json
{
  "source": "00bbd054",
  "target": "00c5aae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd05c`](#insn-00bbd05c)

~~~json
{
  "source": "00bbd05c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd064`](#insn-00bbd064)

~~~json
{
  "source": "00bbd064",
  "target": "00bbd080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd068`](#insn-00bbd068)

~~~json
{
  "source": "00bbd068",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd06c`](#insn-00bbd06c)

~~~json
{
  "source": "00bbd06c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd070`](#insn-00bbd070)

~~~json
{
  "source": "00bbd070",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd074`](#insn-00bbd074)

~~~json
{
  "source": "00bbd074",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd080`](#insn-00bbd080)

~~~json
{
  "source": "00bbd080",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
