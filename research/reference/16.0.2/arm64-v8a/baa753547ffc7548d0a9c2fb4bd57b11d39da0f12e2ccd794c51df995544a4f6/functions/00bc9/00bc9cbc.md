# 00bc9cbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bc9c20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc9c20.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-bc17866a54a5053340f67ae4197652b5)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bcacb0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bca/00bcacb0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-54ed2e5f81ecc70fbd386c982e470294)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc9cbc",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_13remote_config10ConfigInfoEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS7_iS9_RKT0_",
  "size": 264,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1c577f6794ae523662fa5a756c9a2110699df70c7a864ff7e5966410a343150c",
  "source_text_sha256": "1c577f6794ae523662fa5a756c9a2110699df70c7a864ff7e5966410a343150c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc9cbc",
        "00bc9dc3"
      ]
    ],
    "bytes_sha256": "ed879e18d03a9dad946aeb813d986097a3f8b64815af55690d5b35cee8e15211",
    "instruction_count": 66,
    "instruction_bytes": 264,
    "body_bytes": 264,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00c5d9c0](../00c5d/00c5d9c0.md)

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
                    /* try { // try from 00bc9d38 to 00cc9d4f has its CatchHandler @ 00bc9f3c */
  _ZN8firebase26ReferenceCountedFutureImpl15SetBackingErrorEPNS_17FutureBackingDataEiPKc
            (param_1,lVar2,param_3,param_4);
  _ZN8firebase26ReferenceCountedFutureImpl11BackingDataEPNS_17FutureBackingDataE(param_1,lVar2);
  _ZN8firebase26ReferenceCountedFutureImpl14CompleteHandleERKNS_12FutureHandleE(param_1,param_2);
                    /* try { // try from 00bc9d58 to 00cc9d87 has its CatchHandler @ 00bc9f98 */
  _ZN8firebase26ReferenceCountedFutureImpl13CompleteProxyEPNS_17FutureBackingDataE(param_1,lVar2);
  _ZN8firebase26ReferenceCountedFutureImpl27ReleaseMutexAndRunCallbacksERKNS_12FutureHandleE
            (param_1,param_2);
  uVar3 = _ZNK8firebase26ReferenceCountedFutureImpl11is_orphanedEv(param_1);
  if ((uVar3 & 1) != 0) {
                    /* try { // try from 00bc9d88 to 00cc9e07 has its CatchHandler @ 00bc9b5c */
                    /* WARNING: Could not recover jumptable at 0x00bc9d94. Too many branches */
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
<a id="insn-00bc9cbc"></a> `00bc9cbc` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bc9cc0"></a> `00bc9cc0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc9cc4"></a> `00bc9cc4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc9cc8"></a> `00bc9cc8` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bc9ccc"></a> `00bc9ccc` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bc9cd0"></a> `00bc9cd0` | `18 20 00 91` | add x24,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bc9cd4"></a> `00bc9cd4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bc9cd8"></a> `00bc9cd8` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bc9cdc"></a> `00bc9cdc` | `f5 03 03 aa` | mov x21,x3 | `FALL_THROUGH`
<a id="insn-00bc9ce0"></a> `00bc9ce0` | `f7 03 02 2a` | mov w23,w2 | `FALL_THROUGH`
<a id="insn-00bc9ce4"></a> `00bc9ce4` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bc9ce8"></a> `00bc9ce8` | `7a 43 02 94` | bl 0x00c5aad0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc9cec"></a> `00bc9cec` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00bc9cf0"></a> `00bc9cf0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc9cf4"></a> `00bc9cf4` | `97 44 02 94` | bl 0x00c5af50 | `UNCONDITIONAL_CALL`
<a id="insn-00bc9cf8"></a> `00bc9cf8` | `00 05 00 b4` | cbz x0,0x00bc9d98 | `CONDITIONAL_JUMP`
<a id="insn-00bc9cfc"></a> `00bc9cfc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc9d00"></a> `00bc9d00` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bc9d04"></a> `00bc9d04` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc9d08"></a> `00bc9d08` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bc9d0c"></a> `00bc9d0c` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bc9d10"></a> `00bc9d10` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc9d14"></a> `00bc9d14` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bc9d18"></a> `00bc9d18` | `80 00 00 54` | b.eq 0x00bc9d28 | `CONDITIONAL_JUMP`
<a id="insn-00bc9d1c"></a> `00bc9d1c` | `e0 b6 ff d0` | adrp x0,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bc9d20"></a> `00bc9d20` | `00 20 02 91` | add x0,x0,#0x88 | `FALL_THROUGH`
<a id="insn-00bc9d24"></a> `00bc9d24` | `eb 44 02 94` | bl 0x00c5b0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc9d28"></a> `00bc9d28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc9d2c"></a> `00bc9d2c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bc9d30"></a> `00bc9d30` | `e2 03 17 2a` | mov w2,w23 | `FALL_THROUGH`
<a id="insn-00bc9d34"></a> `00bc9d34` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-00bc9d38"></a> `00bc9d38` | `82 44 02 94` | bl 0x00c5af40 | `UNCONDITIONAL_CALL`
<a id="insn-00bc9d3c"></a> `00bc9d3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc9d40"></a> `00bc9d40` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bc9d44"></a> `00bc9d44` | `6f 44 02 94` | bl 0x00c5af00 | `UNCONDITIONAL_CALL`
<a id="insn-00bc9d48"></a> `00bc9d48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc9d4c"></a> `00bc9d4c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bc9d50"></a> `00bc9d50` | `78 44 02 94` | bl 0x00c5af30 | `UNCONDITIONAL_CALL`
<a id="insn-00bc9d54"></a> `00bc9d54` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc9d58"></a> `00bc9d58` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bc9d5c"></a> `00bc9d5c` | `71 44 02 94` | bl 0x00c5af20 | `UNCONDITIONAL_CALL`
<a id="insn-00bc9d60"></a> `00bc9d60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc9d64"></a> `00bc9d64` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bc9d68"></a> `00bc9d68` | `7e 44 02 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bc9d6c"></a> `00bc9d6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc9d70"></a> `00bc9d70` | `f4 44 02 94` | bl 0x00c5b140 | `UNCONDITIONAL_CALL`
<a id="insn-00bc9d74"></a> `00bc9d74` | `e0 01 00 36` | tbz w0,#0x0,0x00bc9db0 | `CONDITIONAL_JUMP`
<a id="insn-00bc9d78"></a> `00bc9d78` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc9d7c"></a> `00bc9d7c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc9d80"></a> `00bc9d80` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bc9d84"></a> `00bc9d84` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc9d88"></a> `00bc9d88` | `01 05 40 f9` | ldr x1,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bc9d8c"></a> `00bc9d8c` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc9d90"></a> `00bc9d90` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bc9d94"></a> `00bc9d94` | `20 00 1f d6` | br x1 | `COMPUTED_JUMP`
<a id="insn-00bc9d98"></a> `00bc9d98` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bc9d9c"></a> `00bc9d9c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc9da0"></a> `00bc9da0` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc9da4"></a> `00bc9da4` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bc9da8"></a> `00bc9da8` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bc9dac"></a> `00bc9dac` | `4d 43 02 14` | b 0x00c5aae0 | `CALL_TERMINATOR`
<a id="insn-00bc9db0"></a> `00bc9db0` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bc9db4"></a> `00bc9db4` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc9db8"></a> `00bc9db8` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc9dbc"></a> `00bc9dbc` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bc9dc0"></a> `00bc9dc0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc9cbc`](#insn-00bc9cbc) 範囲 `[['00bc9cbc', '00bc9cfb']]`
  - `CONDITIONAL_JUMP` [`00bc9cf8`](#insn-00bc9cf8) → [`00bc9d98`](#insn-00bc9d98)
  - `FALL_THROUGH` [`00bc9cf8`](#insn-00bc9cf8) → [`00bc9cfc`](#insn-00bc9cfc)
- ブロック [`00bc9cfc`](#insn-00bc9cfc) 範囲 `[['00bc9cfc', '00bc9d1b']]`
  - `CONDITIONAL_JUMP` [`00bc9d18`](#insn-00bc9d18) → [`00bc9d28`](#insn-00bc9d28)
  - `FALL_THROUGH` [`00bc9d18`](#insn-00bc9d18) → [`00bc9d1c`](#insn-00bc9d1c)
- ブロック [`00bc9d1c`](#insn-00bc9d1c) 範囲 `[['00bc9d1c', '00bc9d27']]`
  - `FALL_THROUGH` [`00bc9d24`](#insn-00bc9d24) → [`00bc9d28`](#insn-00bc9d28)
- ブロック [`00bc9d28`](#insn-00bc9d28) 範囲 `[['00bc9d28', '00bc9d37']]`
  - `FALL_THROUGH` [`00bc9d34`](#insn-00bc9d34) → [`00bc9d38`](#insn-00bc9d38)
- ブロック [`00bc9d38`](#insn-00bc9d38) 範囲 `[['00bc9d38', '00bc9d57']]`
  - `FALL_THROUGH` [`00bc9d54`](#insn-00bc9d54) → [`00bc9d58`](#insn-00bc9d58)
- ブロック [`00bc9d58`](#insn-00bc9d58) 範囲 `[['00bc9d58', '00bc9d77']]`
  - `CONDITIONAL_JUMP` [`00bc9d74`](#insn-00bc9d74) → [`00bc9db0`](#insn-00bc9db0)
  - `FALL_THROUGH` [`00bc9d74`](#insn-00bc9d74) → [`00bc9d78`](#insn-00bc9d78)
- ブロック [`00bc9d78`](#insn-00bc9d78) 範囲 `[['00bc9d78', '00bc9d87']]`
  - `FALL_THROUGH` [`00bc9d84`](#insn-00bc9d84) → [`00bc9d88`](#insn-00bc9d88)
- ブロック [`00bc9d88`](#insn-00bc9d88) 範囲 `[['00bc9d88', '00bc9d97']]`
- ブロック [`00bc9d98`](#insn-00bc9d98) 範囲 `[['00bc9d98', '00bc9daf']]`
- ブロック [`00bc9db0`](#insn-00bc9db0) 範囲 `[['00bc9db0', '00bc9dc3']]`

## 命令位置別の参照

- [`00bc9cbc`](#insn-00bc9cbc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9cc0`](#insn-00bc9cc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9cc4`](#insn-00bc9cc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9cc8`](#insn-00bc9cc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9ce8`](#insn-00bc9ce8) → [`00c5aad0`](../00c5a/00c5aad0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aad0` · 推定シンボル `None` · 推定型 `None`
- [`00bc9cf4`](#insn-00bc9cf4) → [`00c5af50`](../00c5a/00c5af50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af50` · 推定シンボル `None` · 推定型 `None`
- [`00bc9cf8`](#insn-00bc9cf8) → [`00bc9d98`](#insn-00bc9d98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9d18`](#insn-00bc9d18) → [`00bc9d28`](#insn-00bc9d28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9d20`](#insn-00bc9d20) → `002a7088`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bc9d24`](#insn-00bc9d24) → [`00c5b0d0`](../00c5b/00c5b0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bc9d38`](#insn-00bc9d38) → [`00c5af40`](../00c5a/00c5af40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af40` · 推定シンボル `None` · 推定型 `None`
- [`00bc9d44`](#insn-00bc9d44) → [`00c5af00`](../00c5a/00c5af00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af00` · 推定シンボル `None` · 推定型 `None`
- [`00bc9d50`](#insn-00bc9d50) → [`00c5af30`](../00c5a/00c5af30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af30` · 推定シンボル `None` · 推定型 `None`
- [`00bc9d5c`](#insn-00bc9d5c) → [`00c5af20`](../00c5a/00c5af20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af20` · 推定シンボル `None` · 推定型 `None`
- [`00bc9d68`](#insn-00bc9d68) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bc9d70`](#insn-00bc9d70) → [`00c5b140`](../00c5b/00c5b140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b140` · 推定シンボル `None` · 推定型 `None`
- [`00bc9d74`](#insn-00bc9d74) → [`00bc9db0`](#insn-00bc9db0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9d80`](#insn-00bc9d80) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9d84`](#insn-00bc9d84) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9d8c`](#insn-00bc9d8c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9d98`](#insn-00bc9d98) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9d9c`](#insn-00bc9d9c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9da0`](#insn-00bc9da0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9dac`](#insn-00bc9dac) → [`00c5aae0`](../00c5a/00c5aae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aae0` · 推定シンボル `None` · 推定型 `None`
- [`00bc9db0`](#insn-00bc9db0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9db4`](#insn-00bc9db4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9db8`](#insn-00bc9db8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc9cbc`](#insn-00bc9cbc)

~~~json
{
  "source": "00bc9cbc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9cc0`](#insn-00bc9cc0)

~~~json
{
  "source": "00bc9cc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9cc4`](#insn-00bc9cc4)

~~~json
{
  "source": "00bc9cc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9cc8`](#insn-00bc9cc8)

~~~json
{
  "source": "00bc9cc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9ce8`](#insn-00bc9ce8)

~~~json
{
  "source": "00bc9ce8",
  "target": "00c5aad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc9cf4`](#insn-00bc9cf4)

~~~json
{
  "source": "00bc9cf4",
  "target": "00c5af50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc9cf8`](#insn-00bc9cf8)

~~~json
{
  "source": "00bc9cf8",
  "target": "00bc9d98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9d18`](#insn-00bc9d18)

~~~json
{
  "source": "00bc9d18",
  "target": "00bc9d28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9d20`](#insn-00bc9d20)

~~~json
{
  "source": "00bc9d20",
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
- 参照命令 [`00bc9d24`](#insn-00bc9d24)

~~~json
{
  "source": "00bc9d24",
  "target": "00c5b0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc9d38`](#insn-00bc9d38)

~~~json
{
  "source": "00bc9d38",
  "target": "00c5af40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc9d44`](#insn-00bc9d44)

~~~json
{
  "source": "00bc9d44",
  "target": "00c5af00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc9d50`](#insn-00bc9d50)

~~~json
{
  "source": "00bc9d50",
  "target": "00c5af30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc9d5c`](#insn-00bc9d5c)

~~~json
{
  "source": "00bc9d5c",
  "target": "00c5af20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc9d68`](#insn-00bc9d68)

~~~json
{
  "source": "00bc9d68",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc9d70`](#insn-00bc9d70)

~~~json
{
  "source": "00bc9d70",
  "target": "00c5b140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc9d74`](#insn-00bc9d74)

~~~json
{
  "source": "00bc9d74",
  "target": "00bc9db0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9d80`](#insn-00bc9d80)

~~~json
{
  "source": "00bc9d80",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9d84`](#insn-00bc9d84)

~~~json
{
  "source": "00bc9d84",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9d8c`](#insn-00bc9d8c)

~~~json
{
  "source": "00bc9d8c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9d98`](#insn-00bc9d98)

~~~json
{
  "source": "00bc9d98",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9d9c`](#insn-00bc9d9c)

~~~json
{
  "source": "00bc9d9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9da0`](#insn-00bc9da0)

~~~json
{
  "source": "00bc9da0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9dac`](#insn-00bc9dac)

~~~json
{
  "source": "00bc9dac",
  "target": "00c5aae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc9db0`](#insn-00bc9db0)

~~~json
{
  "source": "00bc9db0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9db4`](#insn-00bc9db4)

~~~json
{
  "source": "00bc9db4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9db8`](#insn-00bc9db8)

~~~json
{
  "source": "00bc9db8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
