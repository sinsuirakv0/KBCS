# 00bddce8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdccf4`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdccf4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-9e16e8036cc711a97e581ac7d398f2b0)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddce8",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth10AuthResultEZNS2_35FederatedAuthProviderFutureCallbackIS3_EEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPvEUlSD_E_EEvRKNS_12FutureHandleEiSC_RKT0_",
  "size": 312,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "536d0a23aba0318ada7a7ed8392598ed1a6c1b4fd4ef233e4bca874545b204aa",
  "source_text_sha256": "536d0a23aba0318ada7a7ed8392598ed1a6c1b4fd4ef233e4bca874545b204aa",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddce8",
        "00bdde1f"
      ]
    ],
    "bytes_sha256": "5234468bbd635940c9d5180717e037c0bbe944f8c82bdd73c89e1191deeaf25c",
    "instruction_count": 78,
    "instruction_bytes": 312,
    "body_bytes": 312,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [00c5ee60](../00c5e/00c5ee60.md)

## 呼び出し先

- [00c5baa0](../00c5b/00c5baa0.md)
- [00c5bab0](../00c5b/00c5bab0.md)
- [00c5bed0](../00c5b/00c5bed0.md)
- [00c5bef0](../00c5b/00c5bef0.md)
- [00c5bf00](../00c5b/00c5bf00.md)
- [00c5bf10](../00c5b/00c5bf10.md)
- [00c5bf20](../00c5b/00c5bf20.md)
- [00c5bf30](../00c5b/00c5bf30.md)
- [00c5c0a0](../00c5c/00c5c0a0.md)
- [00c5c110](../00c5c/00c5c110.md)

## 関連文字列（未確認候補）

~~~text
"GetFutureStatus(handle) == kFutureStatusPending"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2368 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth10AuthResultEZNS2_35FederatedAuthProviderFutureCallbackIS3_EEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPvEUlSD_E_EEvRKNS_12FutureHandleEiSC_RKT0_
               (long *param_1,undefined8 *param_2,undefined4 param_3,undefined8 param_4,
               undefined8 *param_5)

{
  int iVar1;
  long lVar2;
  undefined8 uVar3;
  ulong uVar4;
  code *pcVar5;
  
                    /* try { // try from 00bddcf8 to 00cddd03 has its CatchHandler @ 00bdfc3c */
                    /* try { // try from 00bddd04 to 00cddd13 has its CatchHandler @ 00bdfc34 */
                    /* try { // try from 00bddd14 to 00cddd1f has its CatchHandler @ 00bdfc30 */
  _ZN8firebase5Mutex7AcquireEv(param_1 + 1);
                    /* try { // try from 00bddd20 to 00cddd37 has its CatchHandler @ 00bdfc2c */
  lVar2 = _ZN8firebase26ReferenceCountedFutureImpl17BackingFromHandleEm(param_1,*param_2);
  if (lVar2 == 0) {
    _ZN8firebase5Mutex7ReleaseEv(param_1 + 1);
    return;
  }
                    /* try { // try from 00bddd38 to 00cde753 has its CatchHandler @ 00bd7fb0 */
  iVar1 = (**(code **)(*param_1 + 0x20))(param_1,param_2);
  if (iVar1 != 1) {
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
  _ZN8firebase26ReferenceCountedFutureImpl27ReleaseMutexAndRunCallbacksERKNS_12FutureHandleE
            (param_1,param_2);
  uVar4 = _ZNK8firebase26ReferenceCountedFutureImpl11is_orphanedEv(param_1);
  if ((uVar4 & 1) != 0) {
                    /* WARNING: Could not recover jumptable at 0x00bddde8. Too many branches */
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
<a id="insn-00bddce8"></a> `00bddce8` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bddcec"></a> `00bddcec` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddcf0"></a> `00bddcf0` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bddcf4"></a> `00bddcf4` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bddcf8"></a> `00bddcf8` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bddcfc"></a> `00bddcfc` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bddd00"></a> `00bddd00` | `19 20 00 91` | add x25,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bddd04"></a> `00bddd04` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bddd08"></a> `00bddd08` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bddd0c"></a> `00bddd0c` | `f5 03 04 aa` | mov x21,x4 | `FALL_THROUGH`
<a id="insn-00bddd10"></a> `00bddd10` | `f7 03 03 aa` | mov x23,x3 | `FALL_THROUGH`
<a id="insn-00bddd14"></a> `00bddd14` | `f8 03 02 2a` | mov w24,w2 | `FALL_THROUGH`
<a id="insn-00bddd18"></a> `00bddd18` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bddd1c"></a> `00bddd1c` | `61 f7 01 94` | bl 0x00c5baa0 | `UNCONDITIONAL_CALL`
<a id="insn-00bddd20"></a> `00bddd20` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00bddd24"></a> `00bddd24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bddd28"></a> `00bddd28` | `7e f8 01 94` | bl 0x00c5bf20 | `UNCONDITIONAL_CALL`
<a id="insn-00bddd2c"></a> `00bddd2c` | `00 06 00 b4` | cbz x0,0x00bdddec | `CONDITIONAL_JUMP`
<a id="insn-00bddd30"></a> `00bddd30` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bddd34"></a> `00bddd34` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bddd38"></a> `00bddd38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bddd3c"></a> `00bddd3c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bddd40"></a> `00bddd40` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bddd44"></a> `00bddd44` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bddd48"></a> `00bddd48` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bddd4c"></a> `00bddd4c` | `80 00 00 54` | b.eq 0x00bddd5c | `CONDITIONAL_JUMP`
<a id="insn-00bddd50"></a> `00bddd50` | `40 b6 ff d0` | adrp x0,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bddd54"></a> `00bddd54` | `00 80 07 91` | add x0,x0,#0x1e0 | `FALL_THROUGH`
<a id="insn-00bddd58"></a> `00bddd58` | `d2 f8 01 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bddd5c"></a> `00bddd5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bddd60"></a> `00bddd60` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bddd64"></a> `00bddd64` | `e2 03 18 2a` | mov w2,w24 | `FALL_THROUGH`
<a id="insn-00bddd68"></a> `00bddd68` | `e3 03 17 aa` | mov x3,x23 | `FALL_THROUGH`
<a id="insn-00bddd6c"></a> `00bddd6c` | `69 f8 01 94` | bl 0x00c5bf10 | `UNCONDITIONAL_CALL`
<a id="insn-00bddd70"></a> `00bddd70` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bddd74"></a> `00bddd74` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bddd78"></a> `00bddd78` | `56 f8 01 94` | bl 0x00c5bed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bddd7c"></a> `00bddd7c` | `a1 0a 40 f9` | ldr x1,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bddd80"></a> `00bddd80` | `28 0c 40 f9` | ldr x8,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bddd84"></a> `00bddd84` | `a8 00 00 b4` | cbz x8,0x00bddd98 | `CONDITIONAL_JUMP`
<a id="insn-00bddd88"></a> `00bddd88` | `e3 03 00 aa` | mov x3,x0 | `FALL_THROUGH`
<a id="insn-00bddd8c"></a> `00bddd8c` | `a0 02 40 f9` | ldr x0,[x21] | `FALL_THROUGH`
<a id="insn-00bddd90"></a> `00bddd90` | `a2 22 40 39` | ldrb w2,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bddd94"></a> `00bddd94` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bddd98"></a> `00bddd98` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bddd9c"></a> `00bddd9c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bddda0"></a> `00bddda0` | `58 f8 01 94` | bl 0x00c5bf00 | `UNCONDITIONAL_CALL`
<a id="insn-00bddda4"></a> `00bddda4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bddda8"></a> `00bddda8` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdddac"></a> `00bdddac` | `51 f8 01 94` | bl 0x00c5bef0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdddb0"></a> `00bdddb0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdddb4"></a> `00bdddb4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdddb8"></a> `00bdddb8` | `5e f8 01 94` | bl 0x00c5bf30 | `UNCONDITIONAL_CALL`
<a id="insn-00bdddbc"></a> `00bdddbc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdddc0"></a> `00bdddc0` | `d4 f8 01 94` | bl 0x00c5c110 | `UNCONDITIONAL_CALL`
<a id="insn-00bdddc4"></a> `00bdddc4` | `20 02 00 36` | tbz w0,#0x0,0x00bdde08 | `CONDITIONAL_JUMP`
<a id="insn-00bdddc8"></a> `00bdddc8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdddcc"></a> `00bdddcc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdddd0"></a> `00bdddd0` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdddd4"></a> `00bdddd4` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdddd8"></a> `00bdddd8` | `01 05 40 f9` | ldr x1,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bddddc"></a> `00bddddc` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bddde0"></a> `00bddde0` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddde4"></a> `00bddde4` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bddde8"></a> `00bddde8` | `20 00 1f d6` | br x1 | `COMPUTED_JUMP`
<a id="insn-00bdddec"></a> `00bdddec` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdddf0"></a> `00bdddf0` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdddf4"></a> `00bdddf4` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdddf8"></a> `00bdddf8` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdddfc"></a> `00bdddfc` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdde00"></a> `00bdde00` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bdde04"></a> `00bdde04` | `2b f7 01 14` | b 0x00c5bab0 | `CALL_TERMINATOR`
<a id="insn-00bdde08"></a> `00bdde08` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdde0c"></a> `00bdde0c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdde10"></a> `00bdde10` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdde14"></a> `00bdde14` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdde18"></a> `00bdde18` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bdde1c"></a> `00bdde1c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddce8`](#insn-00bddce8) 範囲 `[['00bddce8', '00bddcf7']]`
  - `FALL_THROUGH` [`00bddcf4`](#insn-00bddcf4) → [`00bddcf8`](#insn-00bddcf8)
- ブロック [`00bddcf8`](#insn-00bddcf8) 範囲 `[['00bddcf8', '00bddd03']]`
  - `FALL_THROUGH` [`00bddd00`](#insn-00bddd00) → [`00bddd04`](#insn-00bddd04)
- ブロック [`00bddd04`](#insn-00bddd04) 範囲 `[['00bddd04', '00bddd13']]`
  - `FALL_THROUGH` [`00bddd10`](#insn-00bddd10) → [`00bddd14`](#insn-00bddd14)
- ブロック [`00bddd14`](#insn-00bddd14) 範囲 `[['00bddd14', '00bddd1f']]`
  - `FALL_THROUGH` [`00bddd1c`](#insn-00bddd1c) → [`00bddd20`](#insn-00bddd20)
- ブロック [`00bddd20`](#insn-00bddd20) 範囲 `[['00bddd20', '00bddd2f']]`
  - `CONDITIONAL_JUMP` [`00bddd2c`](#insn-00bddd2c) → [`00bdddec`](#insn-00bdddec)
  - `FALL_THROUGH` [`00bddd2c`](#insn-00bddd2c) → [`00bddd30`](#insn-00bddd30)
- ブロック [`00bddd30`](#insn-00bddd30) 範囲 `[['00bddd30', '00bddd37']]`
  - `FALL_THROUGH` [`00bddd34`](#insn-00bddd34) → [`00bddd38`](#insn-00bddd38)
- ブロック [`00bddd38`](#insn-00bddd38) 範囲 `[['00bddd38', '00bddd4f']]`
  - `CONDITIONAL_JUMP` [`00bddd4c`](#insn-00bddd4c) → [`00bddd5c`](#insn-00bddd5c)
  - `FALL_THROUGH` [`00bddd4c`](#insn-00bddd4c) → [`00bddd50`](#insn-00bddd50)
- ブロック [`00bddd50`](#insn-00bddd50) 範囲 `[['00bddd50', '00bddd5b']]`
  - `FALL_THROUGH` [`00bddd58`](#insn-00bddd58) → [`00bddd5c`](#insn-00bddd5c)
- ブロック [`00bddd5c`](#insn-00bddd5c) 範囲 `[['00bddd5c', '00bddd87']]`
  - `CONDITIONAL_JUMP` [`00bddd84`](#insn-00bddd84) → [`00bddd98`](#insn-00bddd98)
  - `FALL_THROUGH` [`00bddd84`](#insn-00bddd84) → [`00bddd88`](#insn-00bddd88)
- ブロック [`00bddd88`](#insn-00bddd88) 範囲 `[['00bddd88', '00bddd97']]`
  - `FALL_THROUGH` [`00bddd94`](#insn-00bddd94) → [`00bddd98`](#insn-00bddd98)
- ブロック [`00bddd98`](#insn-00bddd98) 範囲 `[['00bddd98', '00bdddc7']]`
  - `CONDITIONAL_JUMP` [`00bdddc4`](#insn-00bdddc4) → [`00bdde08`](#insn-00bdde08)
  - `FALL_THROUGH` [`00bdddc4`](#insn-00bdddc4) → [`00bdddc8`](#insn-00bdddc8)
- ブロック [`00bdddc8`](#insn-00bdddc8) 範囲 `[['00bdddc8', '00bdddeb']]`
- ブロック [`00bdddec`](#insn-00bdddec) 範囲 `[['00bdddec', '00bdde07']]`
- ブロック [`00bdde08`](#insn-00bdde08) 範囲 `[['00bdde08', '00bdde1f']]`

## 命令位置別の参照

- [`00bddce8`](#insn-00bddce8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddcec`](#insn-00bddcec) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddcf0`](#insn-00bddcf0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddcf4`](#insn-00bddcf4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddcf8`](#insn-00bddcf8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddd1c`](#insn-00bddd1c) → [`00c5baa0`](../00c5b/00c5baa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5baa0` · 推定シンボル `None` · 推定型 `None`
- [`00bddd28`](#insn-00bddd28) → [`00c5bf20`](../00c5b/00c5bf20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bf20` · 推定シンボル `None` · 推定型 `None`
- [`00bddd2c`](#insn-00bddd2c) → [`00bdddec`](#insn-00bdddec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddd4c`](#insn-00bddd4c) → [`00bddd5c`](#insn-00bddd5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddd54`](#insn-00bddd54) → `002a71e0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bddd58`](#insn-00bddd58) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bddd6c`](#insn-00bddd6c) → [`00c5bf10`](../00c5b/00c5bf10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bf10` · 推定シンボル `None` · 推定型 `None`
- [`00bddd78`](#insn-00bddd78) → [`00c5bed0`](../00c5b/00c5bed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bed0` · 推定シンボル `None` · 推定型 `None`
- [`00bddd84`](#insn-00bddd84) → [`00bddd98`](#insn-00bddd98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddda0`](#insn-00bddda0) → [`00c5bf00`](../00c5b/00c5bf00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bf00` · 推定シンボル `None` · 推定型 `None`
- [`00bdddac`](#insn-00bdddac) → [`00c5bef0`](../00c5b/00c5bef0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bef0` · 推定シンボル `None` · 推定型 `None`
- [`00bdddb8`](#insn-00bdddb8) → [`00c5bf30`](../00c5b/00c5bf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bf30` · 推定シンボル `None` · 推定型 `None`
- [`00bdddc0`](#insn-00bdddc0) → [`00c5c110`](../00c5c/00c5c110.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c110` · 推定シンボル `None` · 推定型 `None`
- [`00bdddc4`](#insn-00bdddc4) → [`00bdde08`](#insn-00bdde08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdddd0`](#insn-00bdddd0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdddd4`](#insn-00bdddd4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddddc`](#insn-00bddddc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddde0`](#insn-00bddde0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdddec`](#insn-00bdddec) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdddf0`](#insn-00bdddf0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdddf4`](#insn-00bdddf4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdddf8`](#insn-00bdddf8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdde04`](#insn-00bdde04) → [`00c5bab0`](../00c5b/00c5bab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bab0` · 推定シンボル `None` · 推定型 `None`
- [`00bdde08`](#insn-00bdde08) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdde0c`](#insn-00bdde0c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdde10`](#insn-00bdde10) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdde14`](#insn-00bdde14) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddce8`](#insn-00bddce8)

~~~json
{
  "source": "00bddce8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddcec`](#insn-00bddcec)

~~~json
{
  "source": "00bddcec",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddcf0`](#insn-00bddcf0)

~~~json
{
  "source": "00bddcf0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddcf4`](#insn-00bddcf4)

~~~json
{
  "source": "00bddcf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddcf8`](#insn-00bddcf8)

~~~json
{
  "source": "00bddcf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddd1c`](#insn-00bddd1c)

~~~json
{
  "source": "00bddd1c",
  "target": "00c5baa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddd28`](#insn-00bddd28)

~~~json
{
  "source": "00bddd28",
  "target": "00c5bf20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddd2c`](#insn-00bddd2c)

~~~json
{
  "source": "00bddd2c",
  "target": "00bdddec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddd4c`](#insn-00bddd4c)

~~~json
{
  "source": "00bddd4c",
  "target": "00bddd5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddd54`](#insn-00bddd54)

~~~json
{
  "source": "00bddd54",
  "target": "002a71e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a71e0",
  "offset": 0,
  "size": 48,
  "datatype": "string",
  "bytes": "4765744675747572655374617475732868616e646c6529203d3d206b46757475",
  "capture_start": "002a71e0",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bddd58`](#insn-00bddd58)

~~~json
{
  "source": "00bddd58",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddd6c`](#insn-00bddd6c)

~~~json
{
  "source": "00bddd6c",
  "target": "00c5bf10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddd78`](#insn-00bddd78)

~~~json
{
  "source": "00bddd78",
  "target": "00c5bed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddd84`](#insn-00bddd84)

~~~json
{
  "source": "00bddd84",
  "target": "00bddd98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddda0`](#insn-00bddda0)

~~~json
{
  "source": "00bddda0",
  "target": "00c5bf00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdddac`](#insn-00bdddac)

~~~json
{
  "source": "00bdddac",
  "target": "00c5bef0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdddb8`](#insn-00bdddb8)

~~~json
{
  "source": "00bdddb8",
  "target": "00c5bf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdddc0`](#insn-00bdddc0)

~~~json
{
  "source": "00bdddc0",
  "target": "00c5c110",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdddc4`](#insn-00bdddc4)

~~~json
{
  "source": "00bdddc4",
  "target": "00bdde08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdddd0`](#insn-00bdddd0)

~~~json
{
  "source": "00bdddd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdddd4`](#insn-00bdddd4)

~~~json
{
  "source": "00bdddd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddddc`](#insn-00bddddc)

~~~json
{
  "source": "00bddddc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddde0`](#insn-00bddde0)

~~~json
{
  "source": "00bddde0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdddec`](#insn-00bdddec)

~~~json
{
  "source": "00bdddec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdddf0`](#insn-00bdddf0)

~~~json
{
  "source": "00bdddf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdddf4`](#insn-00bdddf4)

~~~json
{
  "source": "00bdddf4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdddf8`](#insn-00bdddf8)

~~~json
{
  "source": "00bdddf8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdde04`](#insn-00bdde04)

~~~json
{
  "source": "00bdde04",
  "target": "00c5bab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdde08`](#insn-00bdde08)

~~~json
{
  "source": "00bdde08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdde0c`](#insn-00bdde0c)

~~~json
{
  "source": "00bdde0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdde10`](#insn-00bdde10)

~~~json
{
  "source": "00bdde10",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdde14`](#insn-00bdde14)

~~~json
{
  "source": "00bdde14",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
