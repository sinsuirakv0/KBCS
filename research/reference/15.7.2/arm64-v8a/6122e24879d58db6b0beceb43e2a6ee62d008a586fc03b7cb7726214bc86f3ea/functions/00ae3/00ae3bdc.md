# 00ae3bdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ae3ca4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3ca4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0058.md#compare-45ef8a6252b468ed3efb720dad21f392)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae3bdc",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIiZNS0_26CompleteWithResultInternalIiEEvRKNS_12FutureHandleEiPKcRKT_EUlPiE_EEvS5_iS7_RKT0_",
  "size": 292,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d4e8e9555b05303c6de4c2983767d552b2662f3af24881834f3c06accce1974d",
  "source_text_sha256": "d4e8e9555b05303c6de4c2983767d552b2662f3af24881834f3c06accce1974d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae3bdc",
        "00ae3cff"
      ]
    ],
    "bytes_sha256": "134a700620543d04245f94f9e56351b3dfca422f5f773be1e46d792b23f192f2",
    "instruction_count": 73,
    "instruction_bytes": 292,
    "body_bytes": 292,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00bdde10](../00bdd/00bdde10.md)

## 呼び出し先

- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)
- [00bddeb0](../00bdd/00bddeb0.md)
- [00bdded0](../00bdd/00bdded0.md)
- [00bddee0](../00bdd/00bddee0.md)
- [00bddef0](../00bdd/00bddef0.md)
- [00bddf00](../00bdd/00bddf00.md)
- [00bddf10](../00bdd/00bddf10.md)
- [00bde080](../00bde/00bde080.md)
- [00bde0f0](../00bde/00bde0f0.md)

## 関連文字列（未確認候補）

~~~text
"GetFutureStatus(handle) == kFutureStatusPending"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2249 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIiZNS0_26CompleteWithResultInternalIiEEvRKNS_12FutureHandleEiPKcRKT_EUlPiE_EEvS5_iS7_RKT0_
               (long *param_1,undefined8 *param_2,undefined4 param_3,undefined8 param_4,
               undefined4 *param_5)

{
  int iVar1;
  long lVar2;
  undefined4 *puVar3;
  ulong uVar4;
  
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
                    /* try { // try from 00ae3c58 to 00be3c9f has its CatchHandler @ 00ae3c58
                       catch() { ... } // from try @ 00ae3c58 with catch @ 00ae3c58
                       catch() { ... } // from try @ 00ae3cac with catch @ 00ae3c58 */
  _ZN8firebase26ReferenceCountedFutureImpl15SetBackingErrorEPNS_17FutureBackingDataEiPKc
            (param_1,lVar2,param_3,param_4);
  puVar3 = (undefined4 *)
           _ZN8firebase26ReferenceCountedFutureImpl11BackingDataEPNS_17FutureBackingDataE
                     (param_1,lVar2);
  *puVar3 = *param_5;
  _ZN8firebase26ReferenceCountedFutureImpl14CompleteHandleERKNS_12FutureHandleE(param_1,param_2);
  _ZN8firebase26ReferenceCountedFutureImpl13CompleteProxyEPNS_17FutureBackingDataE(param_1,lVar2);
  _ZN8firebase26ReferenceCountedFutureImpl27ReleaseMutexAndRunCallbacksERKNS_12FutureHandleE
            (param_1,param_2);
                    /* try { // try from 00ae3ca0 to 00be3cab has its CatchHandler @ 00ae3cfc */
  uVar4 = _ZNK8firebase26ReferenceCountedFutureImpl11is_orphanedEv(param_1);
  if ((uVar4 & 1) != 0) {
                    /* try { // try from 00ae3cac to 00be3d4b has its CatchHandler @ 00ae3c58 */
                    /* WARNING: Could not recover jumptable at 0x00ae3cc8. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*param_1 + 8))(param_1);
    return;
  }
                    /* catch() { ... } // from try @ 00ae3ca0 with catch @ 00ae3cfc */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae3bdc"></a> `00ae3bdc` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00ae3be0"></a> `00ae3be0` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae3be4"></a> `00ae3be4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ae3be8"></a> `00ae3be8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ae3bec"></a> `00ae3bec` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ae3bf0"></a> `00ae3bf0` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00ae3bf4"></a> `00ae3bf4` | `19 20 00 91` | add x25,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00ae3bf8"></a> `00ae3bf8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ae3bfc"></a> `00ae3bfc` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00ae3c00"></a> `00ae3c00` | `f5 03 04 aa` | mov x21,x4 | `FALL_THROUGH`
<a id="insn-00ae3c04"></a> `00ae3c04` | `f7 03 03 aa` | mov x23,x3 | `FALL_THROUGH`
<a id="insn-00ae3c08"></a> `00ae3c08` | `f8 03 02 2a` | mov w24,w2 | `FALL_THROUGH`
<a id="insn-00ae3c0c"></a> `00ae3c0c` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00ae3c10"></a> `00ae3c10` | `c4 e7 03 94` | bl 0x00bddb20 | `UNCONDITIONAL_CALL`
<a id="insn-00ae3c14"></a> `00ae3c14` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00ae3c18"></a> `00ae3c18` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae3c1c"></a> `00ae3c1c` | `b9 e8 03 94` | bl 0x00bddf00 | `UNCONDITIONAL_CALL`
<a id="insn-00ae3c20"></a> `00ae3c20` | `60 05 00 b4` | cbz x0,0x00ae3ccc | `CONDITIONAL_JUMP`
<a id="insn-00ae3c24"></a> `00ae3c24` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae3c28"></a> `00ae3c28` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00ae3c2c"></a> `00ae3c2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae3c30"></a> `00ae3c30` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00ae3c34"></a> `00ae3c34` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00ae3c38"></a> `00ae3c38` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae3c3c"></a> `00ae3c3c` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00ae3c40"></a> `00ae3c40` | `80 00 00 54` | b.eq 0x00ae3c50 | `CONDITIONAL_JUMP`
<a id="insn-00ae3c44"></a> `00ae3c44` | `a0 bd ff 90` | adrp x0,0x297000 | `FALL_THROUGH`
<a id="insn-00ae3c48"></a> `00ae3c48` | `00 9c 11 91` | add x0,x0,#0x467 | `FALL_THROUGH`
<a id="insn-00ae3c4c"></a> `00ae3c4c` | `0d e9 03 94` | bl 0x00bde080 | `UNCONDITIONAL_CALL`
<a id="insn-00ae3c50"></a> `00ae3c50` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae3c54"></a> `00ae3c54` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00ae3c58"></a> `00ae3c58` | `e2 03 18 2a` | mov w2,w24 | `FALL_THROUGH`
<a id="insn-00ae3c5c"></a> `00ae3c5c` | `e3 03 17 aa` | mov x3,x23 | `FALL_THROUGH`
<a id="insn-00ae3c60"></a> `00ae3c60` | `a4 e8 03 94` | bl 0x00bddef0 | `UNCONDITIONAL_CALL`
<a id="insn-00ae3c64"></a> `00ae3c64` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae3c68"></a> `00ae3c68` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00ae3c6c"></a> `00ae3c6c` | `91 e8 03 94` | bl 0x00bddeb0 | `UNCONDITIONAL_CALL`
<a id="insn-00ae3c70"></a> `00ae3c70` | `a8 02 40 b9` | ldr w8,[x21] | `FALL_THROUGH`
<a id="insn-00ae3c74"></a> `00ae3c74` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00ae3c78"></a> `00ae3c78` | `08 00 00 b9` | str w8,[x0] | `FALL_THROUGH`
<a id="insn-00ae3c7c"></a> `00ae3c7c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae3c80"></a> `00ae3c80` | `98 e8 03 94` | bl 0x00bddee0 | `UNCONDITIONAL_CALL`
<a id="insn-00ae3c84"></a> `00ae3c84` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae3c88"></a> `00ae3c88` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00ae3c8c"></a> `00ae3c8c` | `91 e8 03 94` | bl 0x00bdded0 | `UNCONDITIONAL_CALL`
<a id="insn-00ae3c90"></a> `00ae3c90` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae3c94"></a> `00ae3c94` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00ae3c98"></a> `00ae3c98` | `9e e8 03 94` | bl 0x00bddf10 | `UNCONDITIONAL_CALL`
<a id="insn-00ae3c9c"></a> `00ae3c9c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae3ca0"></a> `00ae3ca0` | `14 e9 03 94` | bl 0x00bde0f0 | `UNCONDITIONAL_CALL`
<a id="insn-00ae3ca4"></a> `00ae3ca4` | `20 02 00 36` | tbz w0,#0x0,0x00ae3ce8 | `CONDITIONAL_JUMP`
<a id="insn-00ae3ca8"></a> `00ae3ca8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae3cac"></a> `00ae3cac` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae3cb0"></a> `00ae3cb0` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ae3cb4"></a> `00ae3cb4` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ae3cb8"></a> `00ae3cb8` | `01 05 40 f9` | ldr x1,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00ae3cbc"></a> `00ae3cbc` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ae3cc0"></a> `00ae3cc0` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae3cc4"></a> `00ae3cc4` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00ae3cc8"></a> `00ae3cc8` | `20 00 1f d6` | br x1 | `COMPUTED_JUMP`
<a id="insn-00ae3ccc"></a> `00ae3ccc` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ae3cd0"></a> `00ae3cd0` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ae3cd4"></a> `00ae3cd4` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ae3cd8"></a> `00ae3cd8` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae3cdc"></a> `00ae3cdc` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00ae3ce0"></a> `00ae3ce0` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00ae3ce4"></a> `00ae3ce4` | `93 e7 03 14` | b 0x00bddb30 | `CALL_TERMINATOR`
<a id="insn-00ae3ce8"></a> `00ae3ce8` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ae3cec"></a> `00ae3cec` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ae3cf0"></a> `00ae3cf0` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ae3cf4"></a> `00ae3cf4` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae3cf8"></a> `00ae3cf8` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00ae3cfc"></a> `00ae3cfc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae3bdc`](#insn-00ae3bdc) 範囲 `[['00ae3bdc', '00ae3c23']]`
  - `CONDITIONAL_JUMP` [`00ae3c20`](#insn-00ae3c20) → [`00ae3ccc`](#insn-00ae3ccc)
  - `FALL_THROUGH` [`00ae3c20`](#insn-00ae3c20) → [`00ae3c24`](#insn-00ae3c24)
- ブロック [`00ae3c24`](#insn-00ae3c24) 範囲 `[['00ae3c24', '00ae3c43']]`
  - `CONDITIONAL_JUMP` [`00ae3c40`](#insn-00ae3c40) → [`00ae3c50`](#insn-00ae3c50)
  - `FALL_THROUGH` [`00ae3c40`](#insn-00ae3c40) → [`00ae3c44`](#insn-00ae3c44)
- ブロック [`00ae3c44`](#insn-00ae3c44) 範囲 `[['00ae3c44', '00ae3c4f']]`
  - `FALL_THROUGH` [`00ae3c4c`](#insn-00ae3c4c) → [`00ae3c50`](#insn-00ae3c50)
- ブロック [`00ae3c50`](#insn-00ae3c50) 範囲 `[['00ae3c50', '00ae3c57']]`
  - `FALL_THROUGH` [`00ae3c54`](#insn-00ae3c54) → [`00ae3c58`](#insn-00ae3c58)
- ブロック [`00ae3c58`](#insn-00ae3c58) 範囲 `[['00ae3c58', '00ae3c9f']]`
  - `FALL_THROUGH` [`00ae3c9c`](#insn-00ae3c9c) → [`00ae3ca0`](#insn-00ae3ca0)
- ブロック [`00ae3ca0`](#insn-00ae3ca0) 範囲 `[['00ae3ca0', '00ae3ca7']]`
  - `CONDITIONAL_JUMP` [`00ae3ca4`](#insn-00ae3ca4) → [`00ae3ce8`](#insn-00ae3ce8)
  - `FALL_THROUGH` [`00ae3ca4`](#insn-00ae3ca4) → [`00ae3ca8`](#insn-00ae3ca8)
- ブロック [`00ae3ca8`](#insn-00ae3ca8) 範囲 `[['00ae3ca8', '00ae3cab']]`
  - `FALL_THROUGH` [`00ae3ca8`](#insn-00ae3ca8) → [`00ae3cac`](#insn-00ae3cac)
- ブロック [`00ae3cac`](#insn-00ae3cac) 範囲 `[['00ae3cac', '00ae3ccb']]`
- ブロック [`00ae3ccc`](#insn-00ae3ccc) 範囲 `[['00ae3ccc', '00ae3ce7']]`
- ブロック [`00ae3ce8`](#insn-00ae3ce8) 範囲 `[['00ae3ce8', '00ae3cfb']]`
  - `FALL_THROUGH` [`00ae3cf8`](#insn-00ae3cf8) → [`00ae3cfc`](#insn-00ae3cfc)
- ブロック [`00ae3cfc`](#insn-00ae3cfc) 範囲 `[['00ae3cfc', '00ae3cff']]`

## 命令位置別の参照

- [`00ae3bdc`](#insn-00ae3bdc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3be0`](#insn-00ae3be0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3be4`](#insn-00ae3be4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3be8`](#insn-00ae3be8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3bec`](#insn-00ae3bec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3c10`](#insn-00ae3c10) → [`00bddb20`](../00bdd/00bddb20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb20` · 推定シンボル `None` · 推定型 `None`
- [`00ae3c1c`](#insn-00ae3c1c) → [`00bddf00`](../00bdd/00bddf00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf00` · 推定シンボル `None` · 推定型 `None`
- [`00ae3c20`](#insn-00ae3c20) → [`00ae3ccc`](#insn-00ae3ccc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3c40`](#insn-00ae3c40) → [`00ae3c50`](#insn-00ae3c50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3c48`](#insn-00ae3c48) → `00297467`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae3c4c`](#insn-00ae3c4c) → [`00bde080`](../00bde/00bde080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde080` · 推定シンボル `None` · 推定型 `None`
- [`00ae3c60`](#insn-00ae3c60) → [`00bddef0`](../00bdd/00bddef0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddef0` · 推定シンボル `None` · 推定型 `None`
- [`00ae3c6c`](#insn-00ae3c6c) → [`00bddeb0`](../00bdd/00bddeb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddeb0` · 推定シンボル `None` · 推定型 `None`
- [`00ae3c80`](#insn-00ae3c80) → [`00bddee0`](../00bdd/00bddee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddee0` · 推定シンボル `None` · 推定型 `None`
- [`00ae3c8c`](#insn-00ae3c8c) → [`00bdded0`](../00bdd/00bdded0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdded0` · 推定シンボル `None` · 推定型 `None`
- [`00ae3c98`](#insn-00ae3c98) → [`00bddf10`](../00bdd/00bddf10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf10` · 推定シンボル `None` · 推定型 `None`
- [`00ae3ca0`](#insn-00ae3ca0) → [`00bde0f0`](../00bde/00bde0f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde0f0` · 推定シンボル `None` · 推定型 `None`
- [`00ae3ca4`](#insn-00ae3ca4) → [`00ae3ce8`](#insn-00ae3ce8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3cb0`](#insn-00ae3cb0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3cb4`](#insn-00ae3cb4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3cbc`](#insn-00ae3cbc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3cc0`](#insn-00ae3cc0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3ccc`](#insn-00ae3ccc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3cd0`](#insn-00ae3cd0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3cd4`](#insn-00ae3cd4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3cd8`](#insn-00ae3cd8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3ce4`](#insn-00ae3ce4) → [`00bddb30`](../00bdd/00bddb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb30` · 推定シンボル `None` · 推定型 `None`
- [`00ae3ce8`](#insn-00ae3ce8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3cec`](#insn-00ae3cec) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3cf0`](#insn-00ae3cf0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3cf4`](#insn-00ae3cf4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae3bdc`](#insn-00ae3bdc)

~~~json
{
  "source": "00ae3bdc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3be0`](#insn-00ae3be0)

~~~json
{
  "source": "00ae3be0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3be4`](#insn-00ae3be4)

~~~json
{
  "source": "00ae3be4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3be8`](#insn-00ae3be8)

~~~json
{
  "source": "00ae3be8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3bec`](#insn-00ae3bec)

~~~json
{
  "source": "00ae3bec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3c10`](#insn-00ae3c10)

~~~json
{
  "source": "00ae3c10",
  "target": "00bddb20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae3c1c`](#insn-00ae3c1c)

~~~json
{
  "source": "00ae3c1c",
  "target": "00bddf00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae3c20`](#insn-00ae3c20)

~~~json
{
  "source": "00ae3c20",
  "target": "00ae3ccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3c40`](#insn-00ae3c40)

~~~json
{
  "source": "00ae3c40",
  "target": "00ae3c50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3c48`](#insn-00ae3c48)

~~~json
{
  "source": "00ae3c48",
  "target": "00297467",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00297467",
  "offset": 0,
  "size": 48,
  "datatype": "string",
  "bytes": "4765744675747572655374617475732868616e646c6529203d3d206b46757475",
  "capture_start": "00297467",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ae3c4c`](#insn-00ae3c4c)

~~~json
{
  "source": "00ae3c4c",
  "target": "00bde080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae3c60`](#insn-00ae3c60)

~~~json
{
  "source": "00ae3c60",
  "target": "00bddef0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae3c6c`](#insn-00ae3c6c)

~~~json
{
  "source": "00ae3c6c",
  "target": "00bddeb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae3c80`](#insn-00ae3c80)

~~~json
{
  "source": "00ae3c80",
  "target": "00bddee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae3c8c`](#insn-00ae3c8c)

~~~json
{
  "source": "00ae3c8c",
  "target": "00bdded0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae3c98`](#insn-00ae3c98)

~~~json
{
  "source": "00ae3c98",
  "target": "00bddf10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae3ca0`](#insn-00ae3ca0)

~~~json
{
  "source": "00ae3ca0",
  "target": "00bde0f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae3ca4`](#insn-00ae3ca4)

~~~json
{
  "source": "00ae3ca4",
  "target": "00ae3ce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3cb0`](#insn-00ae3cb0)

~~~json
{
  "source": "00ae3cb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3cb4`](#insn-00ae3cb4)

~~~json
{
  "source": "00ae3cb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3cbc`](#insn-00ae3cbc)

~~~json
{
  "source": "00ae3cbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3cc0`](#insn-00ae3cc0)

~~~json
{
  "source": "00ae3cc0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3ccc`](#insn-00ae3ccc)

~~~json
{
  "source": "00ae3ccc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3cd0`](#insn-00ae3cd0)

~~~json
{
  "source": "00ae3cd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3cd4`](#insn-00ae3cd4)

~~~json
{
  "source": "00ae3cd4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3cd8`](#insn-00ae3cd8)

~~~json
{
  "source": "00ae3cd8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3ce4`](#insn-00ae3ce4)

~~~json
{
  "source": "00ae3ce4",
  "target": "00bddb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae3ce8`](#insn-00ae3ce8)

~~~json
{
  "source": "00ae3ce8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3cec`](#insn-00ae3cec)

~~~json
{
  "source": "00ae3cec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3cf0`](#insn-00ae3cf0)

~~~json
{
  "source": "00ae3cf0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3cf4`](#insn-00ae3cf4)

~~~json
{
  "source": "00ae3cf4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
