# 00bcfeb4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcfe18`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfe18.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0082.md#compare-839d045baf102f8e0824d55e5ea49299)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bd0ea8`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0ea8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-4e8c4b689c74f26cd1fc59d065f984d5)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcfeb4",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth10AuthResultEZNS2_14FutureCallbackIS3_EEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPvEUlSD_E_EEvRKNS_12FutureHandleEiSC_RKT0_",
  "size": 312,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2ecd746e30504d468b921b8c209009b5ef98a572891d21cfc735db997492c5c5",
  "source_text_sha256": "2ecd746e30504d468b921b8c209009b5ef98a572891d21cfc735db997492c5c5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcfeb4",
        "00bcffeb"
      ]
    ],
    "bytes_sha256": "071f09646c4f534de5bcdc264a068d961ada1d22574635ecdb6a9d0f936fe049",
    "instruction_count": 78,
    "instruction_bytes": 312,
    "body_bytes": 312,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [00c5dc60](../00c5d/00c5dc60.md)

## 呼び出し先

- [00c5aad0](../00c5a/00c5aad0.md)
- [00c5aae0](../00c5a/00c5aae0.md)
- [00c5af00](../00c5a/00c5af00.md)
- [00c5af20](../00c5a/00c5af20.md)
- [00c5af30](../00c5a/00c5af30.md)
- [00c5af40](../00c5a/00c5af40.md)
- [00c5af50](../00c5a/00c5af50.md)
- [00c5af60](../00c5a/00c5af60.md)
- [00c5b0d0](../00c5b/00c5b0d0.md)
- [00c5b140](../00c5b/00c5b140.md)

## 関連文字列（未確認候補）

~~~text
"GetFutureStatus(handle) == kFutureStatusPending"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2250 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth10AuthResultEZNS2_14FutureCallbackIS3_EEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPvEUlSD_E_EEvRKNS_12FutureHandleEiSC_RKT0_
               (long *param_1,undefined8 *param_2,undefined4 param_3,undefined8 param_4,
               undefined8 *param_5)

{
  int iVar1;
  long lVar2;
  undefined8 uVar3;
  ulong uVar4;
  code *pcVar5;
  
  _ZN8firebase5Mutex7AcquireEv(param_1 + 1);
  lVar2 = _ZN8firebase26ReferenceCountedFutureImpl17BackingFromHandleEm(param_1,*param_2);
  if (lVar2 == 0) {
    _ZN8firebase5Mutex7ReleaseEv(param_1 + 1);
    return;
  }
                    /* try { // try from 00bcff10 to 00ccff1b has its CatchHandler @ 00bd03e0 */
  iVar1 = (**(code **)(*param_1 + 0x20))(param_1,param_2);
  if (iVar1 != 1) {
                    /* try { // try from 00bcff1c to 00ccff7b has its CatchHandler @ 00bcfd30 */
    _ZN8firebase9LogAssertEPKcz("GetFutureStatus(handle) == kFutureStatusPending");
  }
  _ZN8firebase26ReferenceCountedFutureImpl15SetBackingErrorEPNS_17FutureBackingDataEiPKc
            (param_1,lVar2,param_3,param_4);
  uVar3 = _ZN8firebase26ReferenceCountedFutureImpl11BackingDataEPNS_17FutureBackingDataE
                    (param_1,lVar2);
  pcVar5 = *(code **)(param_5[2] + 0x18);
  if (pcVar5 != (code *)0x0) {
    (*pcVar5)(*param_5,param_5[2],*(undefined1 *)(param_5 + 1),uVar3);
  }
  _ZN8firebase26ReferenceCountedFutureImpl14CompleteHandleERKNS_12FutureHandleE(param_1,param_2);
  _ZN8firebase26ReferenceCountedFutureImpl13CompleteProxyEPNS_17FutureBackingDataE(param_1,lVar2);
                    /* try { // try from 00bcff7c to 00ccff97 has its CatchHandler @ 00bd03e4 */
  _ZN8firebase26ReferenceCountedFutureImpl27ReleaseMutexAndRunCallbacksERKNS_12FutureHandleE
            (param_1,param_2);
  uVar4 = _ZNK8firebase26ReferenceCountedFutureImpl11is_orphanedEv(param_1);
  if ((uVar4 & 1) != 0) {
                    /* try { // try from 00bcff98 to 00ccffeb has its CatchHandler @ 00bcfd30 */
                    /* WARNING: Could not recover jumptable at 0x00bcffb4. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*param_1 + 8))(param_1);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcfeb4"></a> `00bcfeb4` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bcfeb8"></a> `00bcfeb8` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfebc"></a> `00bcfebc` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfec0"></a> `00bcfec0` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcfec4"></a> `00bcfec4` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcfec8"></a> `00bcfec8` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bcfecc"></a> `00bcfecc` | `19 20 00 91` | add x25,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bcfed0"></a> `00bcfed0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcfed4"></a> `00bcfed4` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bcfed8"></a> `00bcfed8` | `f5 03 04 aa` | mov x21,x4 | `FALL_THROUGH`
<a id="insn-00bcfedc"></a> `00bcfedc` | `f7 03 03 aa` | mov x23,x3 | `FALL_THROUGH`
<a id="insn-00bcfee0"></a> `00bcfee0` | `f8 03 02 2a` | mov w24,w2 | `FALL_THROUGH`
<a id="insn-00bcfee4"></a> `00bcfee4` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bcfee8"></a> `00bcfee8` | `fa 2a 02 94` | bl 0x00c5aad0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfeec"></a> `00bcfeec` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00bcfef0"></a> `00bcfef0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfef4"></a> `00bcfef4` | `17 2c 02 94` | bl 0x00c5af50 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfef8"></a> `00bcfef8` | `00 06 00 b4` | cbz x0,0x00bcffb8 | `CONDITIONAL_JUMP`
<a id="insn-00bcfefc"></a> `00bcfefc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcff00"></a> `00bcff00` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bcff04"></a> `00bcff04` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcff08"></a> `00bcff08` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcff0c"></a> `00bcff0c` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bcff10"></a> `00bcff10` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcff14"></a> `00bcff14` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bcff18"></a> `00bcff18` | `80 00 00 54` | b.eq 0x00bcff28 | `CONDITIONAL_JUMP`
<a id="insn-00bcff1c"></a> `00bcff1c` | `c0 b6 ff 90` | adrp x0,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bcff20"></a> `00bcff20` | `00 20 02 91` | add x0,x0,#0x88 | `FALL_THROUGH`
<a id="insn-00bcff24"></a> `00bcff24` | `6b 2c 02 94` | bl 0x00c5b0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcff28"></a> `00bcff28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcff2c"></a> `00bcff2c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcff30"></a> `00bcff30` | `e2 03 18 2a` | mov w2,w24 | `FALL_THROUGH`
<a id="insn-00bcff34"></a> `00bcff34` | `e3 03 17 aa` | mov x3,x23 | `FALL_THROUGH`
<a id="insn-00bcff38"></a> `00bcff38` | `02 2c 02 94` | bl 0x00c5af40 | `UNCONDITIONAL_CALL`
<a id="insn-00bcff3c"></a> `00bcff3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcff40"></a> `00bcff40` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcff44"></a> `00bcff44` | `ef 2b 02 94` | bl 0x00c5af00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcff48"></a> `00bcff48` | `a1 0a 40 f9` | ldr x1,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bcff4c"></a> `00bcff4c` | `28 0c 40 f9` | ldr x8,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bcff50"></a> `00bcff50` | `a8 00 00 b4` | cbz x8,0x00bcff64 | `CONDITIONAL_JUMP`
<a id="insn-00bcff54"></a> `00bcff54` | `e3 03 00 aa` | mov x3,x0 | `FALL_THROUGH`
<a id="insn-00bcff58"></a> `00bcff58` | `a0 02 40 f9` | ldr x0,[x21] | `FALL_THROUGH`
<a id="insn-00bcff5c"></a> `00bcff5c` | `a2 22 40 39` | ldrb w2,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcff60"></a> `00bcff60` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcff64"></a> `00bcff64` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcff68"></a> `00bcff68` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcff6c"></a> `00bcff6c` | `f1 2b 02 94` | bl 0x00c5af30 | `UNCONDITIONAL_CALL`
<a id="insn-00bcff70"></a> `00bcff70` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcff74"></a> `00bcff74` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcff78"></a> `00bcff78` | `ea 2b 02 94` | bl 0x00c5af20 | `UNCONDITIONAL_CALL`
<a id="insn-00bcff7c"></a> `00bcff7c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcff80"></a> `00bcff80` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcff84"></a> `00bcff84` | `f7 2b 02 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcff88"></a> `00bcff88` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcff8c"></a> `00bcff8c` | `6d 2c 02 94` | bl 0x00c5b140 | `UNCONDITIONAL_CALL`
<a id="insn-00bcff90"></a> `00bcff90` | `20 02 00 36` | tbz w0,#0x0,0x00bcffd4 | `CONDITIONAL_JUMP`
<a id="insn-00bcff94"></a> `00bcff94` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcff98"></a> `00bcff98` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcff9c"></a> `00bcff9c` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcffa0"></a> `00bcffa0` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcffa4"></a> `00bcffa4` | `01 05 40 f9` | ldr x1,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bcffa8"></a> `00bcffa8` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcffac"></a> `00bcffac` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcffb0"></a> `00bcffb0` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcffb4"></a> `00bcffb4` | `20 00 1f d6` | br x1 | `COMPUTED_JUMP`
<a id="insn-00bcffb8"></a> `00bcffb8` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcffbc"></a> `00bcffbc` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcffc0"></a> `00bcffc0` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcffc4"></a> `00bcffc4` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcffc8"></a> `00bcffc8` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bcffcc"></a> `00bcffcc` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcffd0"></a> `00bcffd0` | `c4 2a 02 14` | b 0x00c5aae0 | `CALL_TERMINATOR`
<a id="insn-00bcffd4"></a> `00bcffd4` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcffd8"></a> `00bcffd8` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcffdc"></a> `00bcffdc` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcffe0"></a> `00bcffe0` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcffe4"></a> `00bcffe4` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcffe8"></a> `00bcffe8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcfeb4`](#insn-00bcfeb4) 範囲 `[['00bcfeb4', '00bcfefb']]`
  - `CONDITIONAL_JUMP` [`00bcfef8`](#insn-00bcfef8) → [`00bcffb8`](#insn-00bcffb8)
  - `FALL_THROUGH` [`00bcfef8`](#insn-00bcfef8) → [`00bcfefc`](#insn-00bcfefc)
- ブロック [`00bcfefc`](#insn-00bcfefc) 範囲 `[['00bcfefc', '00bcff0f']]`
  - `FALL_THROUGH` [`00bcff0c`](#insn-00bcff0c) → [`00bcff10`](#insn-00bcff10)
- ブロック [`00bcff10`](#insn-00bcff10) 範囲 `[['00bcff10', '00bcff1b']]`
  - `CONDITIONAL_JUMP` [`00bcff18`](#insn-00bcff18) → [`00bcff28`](#insn-00bcff28)
  - `FALL_THROUGH` [`00bcff18`](#insn-00bcff18) → [`00bcff1c`](#insn-00bcff1c)
- ブロック [`00bcff1c`](#insn-00bcff1c) 範囲 `[['00bcff1c', '00bcff27']]`
  - `FALL_THROUGH` [`00bcff24`](#insn-00bcff24) → [`00bcff28`](#insn-00bcff28)
- ブロック [`00bcff28`](#insn-00bcff28) 範囲 `[['00bcff28', '00bcff53']]`
  - `CONDITIONAL_JUMP` [`00bcff50`](#insn-00bcff50) → [`00bcff64`](#insn-00bcff64)
  - `FALL_THROUGH` [`00bcff50`](#insn-00bcff50) → [`00bcff54`](#insn-00bcff54)
- ブロック [`00bcff54`](#insn-00bcff54) 範囲 `[['00bcff54', '00bcff63']]`
  - `FALL_THROUGH` [`00bcff60`](#insn-00bcff60) → [`00bcff64`](#insn-00bcff64)
- ブロック [`00bcff64`](#insn-00bcff64) 範囲 `[['00bcff64', '00bcff7b']]`
  - `FALL_THROUGH` [`00bcff78`](#insn-00bcff78) → [`00bcff7c`](#insn-00bcff7c)
- ブロック [`00bcff7c`](#insn-00bcff7c) 範囲 `[['00bcff7c', '00bcff93']]`
  - `CONDITIONAL_JUMP` [`00bcff90`](#insn-00bcff90) → [`00bcffd4`](#insn-00bcffd4)
  - `FALL_THROUGH` [`00bcff90`](#insn-00bcff90) → [`00bcff94`](#insn-00bcff94)
- ブロック [`00bcff94`](#insn-00bcff94) 範囲 `[['00bcff94', '00bcff97']]`
  - `FALL_THROUGH` [`00bcff94`](#insn-00bcff94) → [`00bcff98`](#insn-00bcff98)
- ブロック [`00bcff98`](#insn-00bcff98) 範囲 `[['00bcff98', '00bcffb7']]`
- ブロック [`00bcffb8`](#insn-00bcffb8) 範囲 `[['00bcffb8', '00bcffd3']]`
- ブロック [`00bcffd4`](#insn-00bcffd4) 範囲 `[['00bcffd4', '00bcffeb']]`

## 命令位置別の参照

- [`00bcfeb4`](#insn-00bcfeb4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfeb8`](#insn-00bcfeb8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfebc`](#insn-00bcfebc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfec0`](#insn-00bcfec0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfec4`](#insn-00bcfec4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfee8`](#insn-00bcfee8) → [`00c5aad0`](../00c5a/00c5aad0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aad0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfef4`](#insn-00bcfef4) → [`00c5af50`](../00c5a/00c5af50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af50` · 推定シンボル `None` · 推定型 `None`
- [`00bcfef8`](#insn-00bcfef8) → [`00bcffb8`](#insn-00bcffb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcff18`](#insn-00bcff18) → [`00bcff28`](#insn-00bcff28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcff20`](#insn-00bcff20) → `002a7088`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcff24`](#insn-00bcff24) → [`00c5b0d0`](../00c5b/00c5b0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bcff38`](#insn-00bcff38) → [`00c5af40`](../00c5a/00c5af40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af40` · 推定シンボル `None` · 推定型 `None`
- [`00bcff44`](#insn-00bcff44) → [`00c5af00`](../00c5a/00c5af00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af00` · 推定シンボル `None` · 推定型 `None`
- [`00bcff50`](#insn-00bcff50) → [`00bcff64`](#insn-00bcff64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcff6c`](#insn-00bcff6c) → [`00c5af30`](../00c5a/00c5af30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af30` · 推定シンボル `None` · 推定型 `None`
- [`00bcff78`](#insn-00bcff78) → [`00c5af20`](../00c5a/00c5af20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af20` · 推定シンボル `None` · 推定型 `None`
- [`00bcff84`](#insn-00bcff84) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bcff8c`](#insn-00bcff8c) → [`00c5b140`](../00c5b/00c5b140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b140` · 推定シンボル `None` · 推定型 `None`
- [`00bcff90`](#insn-00bcff90) → [`00bcffd4`](#insn-00bcffd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcff9c`](#insn-00bcff9c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcffa0`](#insn-00bcffa0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcffa8`](#insn-00bcffa8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcffac`](#insn-00bcffac) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcffb8`](#insn-00bcffb8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcffbc`](#insn-00bcffbc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcffc0`](#insn-00bcffc0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcffc4`](#insn-00bcffc4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcffd0`](#insn-00bcffd0) → [`00c5aae0`](../00c5a/00c5aae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aae0` · 推定シンボル `None` · 推定型 `None`
- [`00bcffd4`](#insn-00bcffd4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcffd8`](#insn-00bcffd8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcffdc`](#insn-00bcffdc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcffe0`](#insn-00bcffe0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcfeb4`](#insn-00bcfeb4)

~~~json
{
  "source": "00bcfeb4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfeb8`](#insn-00bcfeb8)

~~~json
{
  "source": "00bcfeb8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfebc`](#insn-00bcfebc)

~~~json
{
  "source": "00bcfebc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfec0`](#insn-00bcfec0)

~~~json
{
  "source": "00bcfec0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfec4`](#insn-00bcfec4)

~~~json
{
  "source": "00bcfec4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfee8`](#insn-00bcfee8)

~~~json
{
  "source": "00bcfee8",
  "target": "00c5aad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfef4`](#insn-00bcfef4)

~~~json
{
  "source": "00bcfef4",
  "target": "00c5af50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfef8`](#insn-00bcfef8)

~~~json
{
  "source": "00bcfef8",
  "target": "00bcffb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcff18`](#insn-00bcff18)

~~~json
{
  "source": "00bcff18",
  "target": "00bcff28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcff20`](#insn-00bcff20)

~~~json
{
  "source": "00bcff20",
  "target": "002a7088",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7088",
  "offset": 0,
  "size": 48,
  "datatype": "string",
  "bytes": "4765744675747572655374617475732868616e646c6529203d3d206b46757475",
  "capture_start": "002a7088",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcff24`](#insn-00bcff24)

~~~json
{
  "source": "00bcff24",
  "target": "00c5b0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcff38`](#insn-00bcff38)

~~~json
{
  "source": "00bcff38",
  "target": "00c5af40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcff44`](#insn-00bcff44)

~~~json
{
  "source": "00bcff44",
  "target": "00c5af00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcff50`](#insn-00bcff50)

~~~json
{
  "source": "00bcff50",
  "target": "00bcff64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcff6c`](#insn-00bcff6c)

~~~json
{
  "source": "00bcff6c",
  "target": "00c5af30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcff78`](#insn-00bcff78)

~~~json
{
  "source": "00bcff78",
  "target": "00c5af20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcff84`](#insn-00bcff84)

~~~json
{
  "source": "00bcff84",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcff8c`](#insn-00bcff8c)

~~~json
{
  "source": "00bcff8c",
  "target": "00c5b140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcff90`](#insn-00bcff90)

~~~json
{
  "source": "00bcff90",
  "target": "00bcffd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcff9c`](#insn-00bcff9c)

~~~json
{
  "source": "00bcff9c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcffa0`](#insn-00bcffa0)

~~~json
{
  "source": "00bcffa0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcffa8`](#insn-00bcffa8)

~~~json
{
  "source": "00bcffa8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcffac`](#insn-00bcffac)

~~~json
{
  "source": "00bcffac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcffb8`](#insn-00bcffb8)

~~~json
{
  "source": "00bcffb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcffbc`](#insn-00bcffbc)

~~~json
{
  "source": "00bcffbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcffc0`](#insn-00bcffc0)

~~~json
{
  "source": "00bcffc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcffc4`](#insn-00bcffc4)

~~~json
{
  "source": "00bcffc4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcffd0`](#insn-00bcffd0)

~~~json
{
  "source": "00bcffd0",
  "target": "00c5aae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcffd4`](#insn-00bcffd4)

~~~json
{
  "source": "00bcffd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcffd8`](#insn-00bcffd8)

~~~json
{
  "source": "00bcffd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcffdc`](#insn-00bcffdc)

~~~json
{
  "source": "00bcffdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcffe0`](#insn-00bcffe0)

~~~json
{
  "source": "00bcffe0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
