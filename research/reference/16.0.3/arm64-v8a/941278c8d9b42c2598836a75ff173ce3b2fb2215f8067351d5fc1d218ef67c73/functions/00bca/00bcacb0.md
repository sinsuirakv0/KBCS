# 00bcacb0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bc9cbc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc9cbc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-54ed2e5f81ecc70fbd386c982e470294)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcacb0",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_13remote_config10ConfigInfoEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS7_iS9_RKT0_",
  "size": 264,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b127634a1f49b07d201175cc4fdbb8b3eb65924ae0be87f7c81e667bc4eebdce",
  "source_text_sha256": "b127634a1f49b07d201175cc4fdbb8b3eb65924ae0be87f7c81e667bc4eebdce",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcacb0",
        "00bcadb7"
      ]
    ],
    "bytes_sha256": "6c673f3054762b731a757f9b30a4eae4ac8fbfc082881fd7fef7e7fa32d4ba96",
    "instruction_count": 66,
    "instruction_bytes": 264,
    "body_bytes": 264,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00c5e990](../00c5e/00c5e990.md)

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

## 疑似コード / UTF-8 1873 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_13remote_config10ConfigInfoEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS7_iS9_RKT0_
               (long *param_1,undefined8 *param_2,undefined4 param_3,undefined8 param_4)

{
  int iVar1;
  long lVar2;
  ulong uVar3;
  
  _ZN8firebase5Mutex7AcquireEv(param_1 + 1);
  lVar2 = _ZN8firebase26ReferenceCountedFutureImpl17BackingFromHandleEm(param_1,*param_2);
  if (lVar2 == 0) {
    _ZN8firebase5Mutex7ReleaseEv(param_1 + 1);
    return;
  }
  iVar1 = (**(code **)(*param_1 + 0x20))(param_1,param_2);
  if (iVar1 != 1) {
    _ZN8firebase9LogAssertEPKcz("GetFutureStatus(handle) == kFutureStatusPending");
  }
                    /* try { // try from 00bcad2c to 00ccad43 has its CatchHandler @ 00bcaf30 */
  _ZN8firebase26ReferenceCountedFutureImpl15SetBackingErrorEPNS_17FutureBackingDataEiPKc
            (param_1,lVar2,param_3,param_4);
  _ZN8firebase26ReferenceCountedFutureImpl11BackingDataEPNS_17FutureBackingDataE(param_1,lVar2);
  _ZN8firebase26ReferenceCountedFutureImpl14CompleteHandleERKNS_12FutureHandleE(param_1,param_2);
                    /* try { // try from 00bcad4c to 00ccad7b has its CatchHandler @ 00bcaf8c */
  _ZN8firebase26ReferenceCountedFutureImpl13CompleteProxyEPNS_17FutureBackingDataE(param_1,lVar2);
  _ZN8firebase26ReferenceCountedFutureImpl27ReleaseMutexAndRunCallbacksERKNS_12FutureHandleE
            (param_1,param_2);
  uVar3 = _ZNK8firebase26ReferenceCountedFutureImpl11is_orphanedEv(param_1);
  if ((uVar3 & 1) != 0) {
                    /* try { // try from 00bcad7c to 00ccadfb has its CatchHandler @ 00bcab50 */
                    /* WARNING: Could not recover jumptable at 0x00bcad88. Too many branches */
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
<a id="insn-00bcacb0"></a> `00bcacb0` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bcacb4"></a> `00bcacb4` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcacb8"></a> `00bcacb8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcacbc"></a> `00bcacbc` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcacc0"></a> `00bcacc0` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bcacc4"></a> `00bcacc4` | `18 20 00 91` | add x24,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bcacc8"></a> `00bcacc8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcaccc"></a> `00bcaccc` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bcacd0"></a> `00bcacd0` | `f5 03 03 aa` | mov x21,x3 | `FALL_THROUGH`
<a id="insn-00bcacd4"></a> `00bcacd4` | `f7 03 02 2a` | mov w23,w2 | `FALL_THROUGH`
<a id="insn-00bcacd8"></a> `00bcacd8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bcacdc"></a> `00bcacdc` | `71 43 02 94` | bl 0x00c5baa0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcace0"></a> `00bcace0` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00bcace4"></a> `00bcace4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcace8"></a> `00bcace8` | `8e 44 02 94` | bl 0x00c5bf20 | `UNCONDITIONAL_CALL`
<a id="insn-00bcacec"></a> `00bcacec` | `00 05 00 b4` | cbz x0,0x00bcad8c | `CONDITIONAL_JUMP`
<a id="insn-00bcacf0"></a> `00bcacf0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcacf4"></a> `00bcacf4` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bcacf8"></a> `00bcacf8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcacfc"></a> `00bcacfc` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcad00"></a> `00bcad00` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bcad04"></a> `00bcad04` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcad08"></a> `00bcad08` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bcad0c"></a> `00bcad0c` | `80 00 00 54` | b.eq 0x00bcad1c | `CONDITIONAL_JUMP`
<a id="insn-00bcad10"></a> `00bcad10` | `e0 b6 ff b0` | adrp x0,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bcad14"></a> `00bcad14` | `00 80 07 91` | add x0,x0,#0x1e0 | `FALL_THROUGH`
<a id="insn-00bcad18"></a> `00bcad18` | `e2 44 02 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcad1c"></a> `00bcad1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcad20"></a> `00bcad20` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcad24"></a> `00bcad24` | `e2 03 17 2a` | mov w2,w23 | `FALL_THROUGH`
<a id="insn-00bcad28"></a> `00bcad28` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-00bcad2c"></a> `00bcad2c` | `79 44 02 94` | bl 0x00c5bf10 | `UNCONDITIONAL_CALL`
<a id="insn-00bcad30"></a> `00bcad30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcad34"></a> `00bcad34` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcad38"></a> `00bcad38` | `66 44 02 94` | bl 0x00c5bed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcad3c"></a> `00bcad3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcad40"></a> `00bcad40` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcad44"></a> `00bcad44` | `6f 44 02 94` | bl 0x00c5bf00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcad48"></a> `00bcad48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcad4c"></a> `00bcad4c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcad50"></a> `00bcad50` | `68 44 02 94` | bl 0x00c5bef0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcad54"></a> `00bcad54` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcad58"></a> `00bcad58` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcad5c"></a> `00bcad5c` | `75 44 02 94` | bl 0x00c5bf30 | `UNCONDITIONAL_CALL`
<a id="insn-00bcad60"></a> `00bcad60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcad64"></a> `00bcad64` | `eb 44 02 94` | bl 0x00c5c110 | `UNCONDITIONAL_CALL`
<a id="insn-00bcad68"></a> `00bcad68` | `e0 01 00 36` | tbz w0,#0x0,0x00bcada4 | `CONDITIONAL_JUMP`
<a id="insn-00bcad6c"></a> `00bcad6c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcad70"></a> `00bcad70` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcad74"></a> `00bcad74` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcad78"></a> `00bcad78` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcad7c"></a> `00bcad7c` | `01 05 40 f9` | ldr x1,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bcad80"></a> `00bcad80` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcad84"></a> `00bcad84` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bcad88"></a> `00bcad88` | `20 00 1f d6` | br x1 | `COMPUTED_JUMP`
<a id="insn-00bcad8c"></a> `00bcad8c` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcad90"></a> `00bcad90` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcad94"></a> `00bcad94` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcad98"></a> `00bcad98` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bcad9c"></a> `00bcad9c` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bcada0"></a> `00bcada0` | `44 43 02 14` | b 0x00c5bab0 | `CALL_TERMINATOR`
<a id="insn-00bcada4"></a> `00bcada4` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcada8"></a> `00bcada8` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcadac"></a> `00bcadac` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcadb0"></a> `00bcadb0` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bcadb4"></a> `00bcadb4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcacb0`](#insn-00bcacb0) 範囲 `[['00bcacb0', '00bcacef']]`
  - `CONDITIONAL_JUMP` [`00bcacec`](#insn-00bcacec) → [`00bcad8c`](#insn-00bcad8c)
  - `FALL_THROUGH` [`00bcacec`](#insn-00bcacec) → [`00bcacf0`](#insn-00bcacf0)
- ブロック [`00bcacf0`](#insn-00bcacf0) 範囲 `[['00bcacf0', '00bcad0f']]`
  - `CONDITIONAL_JUMP` [`00bcad0c`](#insn-00bcad0c) → [`00bcad1c`](#insn-00bcad1c)
  - `FALL_THROUGH` [`00bcad0c`](#insn-00bcad0c) → [`00bcad10`](#insn-00bcad10)
- ブロック [`00bcad10`](#insn-00bcad10) 範囲 `[['00bcad10', '00bcad1b']]`
  - `FALL_THROUGH` [`00bcad18`](#insn-00bcad18) → [`00bcad1c`](#insn-00bcad1c)
- ブロック [`00bcad1c`](#insn-00bcad1c) 範囲 `[['00bcad1c', '00bcad2b']]`
  - `FALL_THROUGH` [`00bcad28`](#insn-00bcad28) → [`00bcad2c`](#insn-00bcad2c)
- ブロック [`00bcad2c`](#insn-00bcad2c) 範囲 `[['00bcad2c', '00bcad4b']]`
  - `FALL_THROUGH` [`00bcad48`](#insn-00bcad48) → [`00bcad4c`](#insn-00bcad4c)
- ブロック [`00bcad4c`](#insn-00bcad4c) 範囲 `[['00bcad4c', '00bcad6b']]`
  - `CONDITIONAL_JUMP` [`00bcad68`](#insn-00bcad68) → [`00bcada4`](#insn-00bcada4)
  - `FALL_THROUGH` [`00bcad68`](#insn-00bcad68) → [`00bcad6c`](#insn-00bcad6c)
- ブロック [`00bcad6c`](#insn-00bcad6c) 範囲 `[['00bcad6c', '00bcad7b']]`
  - `FALL_THROUGH` [`00bcad78`](#insn-00bcad78) → [`00bcad7c`](#insn-00bcad7c)
- ブロック [`00bcad7c`](#insn-00bcad7c) 範囲 `[['00bcad7c', '00bcad8b']]`
- ブロック [`00bcad8c`](#insn-00bcad8c) 範囲 `[['00bcad8c', '00bcada3']]`
- ブロック [`00bcada4`](#insn-00bcada4) 範囲 `[['00bcada4', '00bcadb7']]`

## 命令位置別の参照

- [`00bcacb0`](#insn-00bcacb0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcacb4`](#insn-00bcacb4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcacb8`](#insn-00bcacb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcacbc`](#insn-00bcacbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcacdc`](#insn-00bcacdc) → [`00c5baa0`](../00c5b/00c5baa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5baa0` · 推定シンボル `None` · 推定型 `None`
- [`00bcace8`](#insn-00bcace8) → [`00c5bf20`](../00c5b/00c5bf20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bf20` · 推定シンボル `None` · 推定型 `None`
- [`00bcacec`](#insn-00bcacec) → [`00bcad8c`](#insn-00bcad8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcad0c`](#insn-00bcad0c) → [`00bcad1c`](#insn-00bcad1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcad14`](#insn-00bcad14) → `002a71e0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcad18`](#insn-00bcad18) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bcad2c`](#insn-00bcad2c) → [`00c5bf10`](../00c5b/00c5bf10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bf10` · 推定シンボル `None` · 推定型 `None`
- [`00bcad38`](#insn-00bcad38) → [`00c5bed0`](../00c5b/00c5bed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bed0` · 推定シンボル `None` · 推定型 `None`
- [`00bcad44`](#insn-00bcad44) → [`00c5bf00`](../00c5b/00c5bf00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bf00` · 推定シンボル `None` · 推定型 `None`
- [`00bcad50`](#insn-00bcad50) → [`00c5bef0`](../00c5b/00c5bef0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bef0` · 推定シンボル `None` · 推定型 `None`
- [`00bcad5c`](#insn-00bcad5c) → [`00c5bf30`](../00c5b/00c5bf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bf30` · 推定シンボル `None` · 推定型 `None`
- [`00bcad64`](#insn-00bcad64) → [`00c5c110`](../00c5c/00c5c110.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c110` · 推定シンボル `None` · 推定型 `None`
- [`00bcad68`](#insn-00bcad68) → [`00bcada4`](#insn-00bcada4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcad74`](#insn-00bcad74) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcad78`](#insn-00bcad78) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcad80`](#insn-00bcad80) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcad8c`](#insn-00bcad8c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcad90`](#insn-00bcad90) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcad94`](#insn-00bcad94) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcada0`](#insn-00bcada0) → [`00c5bab0`](../00c5b/00c5bab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bab0` · 推定シンボル `None` · 推定型 `None`
- [`00bcada4`](#insn-00bcada4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcada8`](#insn-00bcada8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcadac`](#insn-00bcadac) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcacb0`](#insn-00bcacb0)

~~~json
{
  "source": "00bcacb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcacb4`](#insn-00bcacb4)

~~~json
{
  "source": "00bcacb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcacb8`](#insn-00bcacb8)

~~~json
{
  "source": "00bcacb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcacbc`](#insn-00bcacbc)

~~~json
{
  "source": "00bcacbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcacdc`](#insn-00bcacdc)

~~~json
{
  "source": "00bcacdc",
  "target": "00c5baa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcace8`](#insn-00bcace8)

~~~json
{
  "source": "00bcace8",
  "target": "00c5bf20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcacec`](#insn-00bcacec)

~~~json
{
  "source": "00bcacec",
  "target": "00bcad8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcad0c`](#insn-00bcad0c)

~~~json
{
  "source": "00bcad0c",
  "target": "00bcad1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcad14`](#insn-00bcad14)

~~~json
{
  "source": "00bcad14",
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
- 参照命令 [`00bcad18`](#insn-00bcad18)

~~~json
{
  "source": "00bcad18",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcad2c`](#insn-00bcad2c)

~~~json
{
  "source": "00bcad2c",
  "target": "00c5bf10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcad38`](#insn-00bcad38)

~~~json
{
  "source": "00bcad38",
  "target": "00c5bed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcad44`](#insn-00bcad44)

~~~json
{
  "source": "00bcad44",
  "target": "00c5bf00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcad50`](#insn-00bcad50)

~~~json
{
  "source": "00bcad50",
  "target": "00c5bef0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcad5c`](#insn-00bcad5c)

~~~json
{
  "source": "00bcad5c",
  "target": "00c5bf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcad64`](#insn-00bcad64)

~~~json
{
  "source": "00bcad64",
  "target": "00c5c110",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcad68`](#insn-00bcad68)

~~~json
{
  "source": "00bcad68",
  "target": "00bcada4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcad74`](#insn-00bcad74)

~~~json
{
  "source": "00bcad74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcad78`](#insn-00bcad78)

~~~json
{
  "source": "00bcad78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcad80`](#insn-00bcad80)

~~~json
{
  "source": "00bcad80",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcad8c`](#insn-00bcad8c)

~~~json
{
  "source": "00bcad8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcad90`](#insn-00bcad90)

~~~json
{
  "source": "00bcad90",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcad94`](#insn-00bcad94)

~~~json
{
  "source": "00bcad94",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcada0`](#insn-00bcada0)

~~~json
{
  "source": "00bcada0",
  "target": "00c5bab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcada4`](#insn-00bcada4)

~~~json
{
  "source": "00bcada4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcada8`](#insn-00bcada8)

~~~json
{
  "source": "00bcada8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcadac`](#insn-00bcadac)

~~~json
{
  "source": "00bcadac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
