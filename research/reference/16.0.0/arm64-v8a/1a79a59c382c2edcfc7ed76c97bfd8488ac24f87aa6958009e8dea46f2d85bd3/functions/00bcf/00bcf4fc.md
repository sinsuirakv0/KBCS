# 00bcf4fc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5fffc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5fffc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0067.md#compare-ab1da60d8e74a3c5dec76e9d0fc43a86)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcf924`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf924.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0082.md#compare-bdb0998f150a3f0d0193e87122685a39)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcf4fc",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth4Auth20FetchProvidersResultEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS8_iSA_RKT0_",
  "size": 264,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ed06c0b2f0fc7bce82e0fbde729c09e596e53e09e61a19830dd36d3463386268",
  "source_text_sha256": "ed06c0b2f0fc7bce82e0fbde729c09e596e53e09e61a19830dd36d3463386268",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcf4fc",
        "00bcf603"
      ]
    ],
    "bytes_sha256": "a34edfcb1894ab7e6648d7f079e3328446af4a9c58a5541861d8eadd36faac1a",
    "instruction_count": 66,
    "instruction_bytes": 264,
    "body_bytes": 264,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00c5d7d0](../00c5d/00c5d7d0.md)

## 呼び出し先

- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)
- [00c5aa30](../00c5a/00c5aa30.md)
- [00c5aa50](../00c5a/00c5aa50.md)
- [00c5aa60](../00c5a/00c5aa60.md)
- [00c5aa70](../00c5a/00c5aa70.md)
- [00c5aa80](../00c5a/00c5aa80.md)
- [00c5aa90](../00c5a/00c5aa90.md)
- [00c5ac00](../00c5a/00c5ac00.md)
- [00c5ac70](../00c5a/00c5ac70.md)

## 関連文字列（未確認候補）

~~~text
"GetFutureStatus(handle) == kFutureStatusPending"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2636 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth4Auth20FetchProvidersResultEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS8_iSA_RKT0_
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
                    /* try { // try from 00bcf574 to 00ccf57f has its CatchHandler @ 00bcf5cc */
  _ZN8firebase26ReferenceCountedFutureImpl15SetBackingErrorEPNS_17FutureBackingDataEiPKc
            (param_1,lVar2,param_3,param_4);
                    /* catch() { ... } // from try @ 00bcf3ec with catch @ 00bcf580
                       try { // try from 00bcf580 to 00ccf5fb has its CatchHandler @ 00bcf2f8 */
                    /* catch() { ... } // from try @ 00bcf3a8 with catch @ 00bcf584 */
  _ZN8firebase26ReferenceCountedFutureImpl11BackingDataEPNS_17FutureBackingDataE(param_1,lVar2);
                    /* catch() { ... } // from try @ 00bcf35c with catch @ 00bcf588 */
  _ZN8firebase26ReferenceCountedFutureImpl14CompleteHandleERKNS_12FutureHandleE(param_1,param_2);
                    /* catch() { ... } // from try @ 00bcf494 with catch @ 00bcf59c */
  _ZN8firebase26ReferenceCountedFutureImpl13CompleteProxyEPNS_17FutureBackingDataE(param_1,lVar2);
                    /* catch() { ... } // from try @ 00bcf4cc with catch @ 00bcf5a4 */
  _ZN8firebase26ReferenceCountedFutureImpl27ReleaseMutexAndRunCallbacksERKNS_12FutureHandleE
            (param_1,param_2);
  uVar3 = _ZNK8firebase26ReferenceCountedFutureImpl11is_orphanedEv(param_1);
  if ((uVar3 & 1) != 0) {
                    /* catch() { ... } // from try @ 00bcf328 with catch @ 00bcf5cc
                       catch() { ... } // from try @ 00bcf36c with catch @ 00bcf5cc
                       catch() { ... } // from try @ 00bcf3b8 with catch @ 00bcf5cc
                       catch() { ... } // from try @ 00bcf450 with catch @ 00bcf5cc
                       catch() { ... } // from try @ 00bcf574 with catch @ 00bcf5cc */
                    /* WARNING: Could not recover jumptable at 0x00bcf5d4. Too many branches */
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
<a id="insn-00bcf4fc"></a> `00bcf4fc` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bcf500"></a> `00bcf500` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcf504"></a> `00bcf504` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcf508"></a> `00bcf508` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcf50c"></a> `00bcf50c` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bcf510"></a> `00bcf510` | `18 20 00 91` | add x24,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bcf514"></a> `00bcf514` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcf518"></a> `00bcf518` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bcf51c"></a> `00bcf51c` | `f5 03 03 aa` | mov x21,x3 | `FALL_THROUGH`
<a id="insn-00bcf520"></a> `00bcf520` | `f7 03 02 2a` | mov w23,w2 | `FALL_THROUGH`
<a id="insn-00bcf524"></a> `00bcf524` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bcf528"></a> `00bcf528` | `36 2c 02 94` | bl 0x00c5a600 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf52c"></a> `00bcf52c` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00bcf530"></a> `00bcf530` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcf534"></a> `00bcf534` | `53 2d 02 94` | bl 0x00c5aa80 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf538"></a> `00bcf538` | `00 05 00 b4` | cbz x0,0x00bcf5d8 | `CONDITIONAL_JUMP`
<a id="insn-00bcf53c"></a> `00bcf53c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcf540"></a> `00bcf540` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bcf544"></a> `00bcf544` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcf548"></a> `00bcf548` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcf54c"></a> `00bcf54c` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bcf550"></a> `00bcf550` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcf554"></a> `00bcf554` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bcf558"></a> `00bcf558` | `80 00 00 54` | b.eq 0x00bcf568 | `CONDITIONAL_JUMP`
<a id="insn-00bcf55c"></a> `00bcf55c` | `c0 b6 ff 90` | adrp x0,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bcf560"></a> `00bcf560` | `00 20 00 91` | add x0,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bcf564"></a> `00bcf564` | `a7 2d 02 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf568"></a> `00bcf568` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcf56c"></a> `00bcf56c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcf570"></a> `00bcf570` | `e2 03 17 2a` | mov w2,w23 | `FALL_THROUGH`
<a id="insn-00bcf574"></a> `00bcf574` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-00bcf578"></a> `00bcf578` | `3e 2d 02 94` | bl 0x00c5aa70 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf57c"></a> `00bcf57c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcf580"></a> `00bcf580` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcf584"></a> `00bcf584` | `2b 2d 02 94` | bl 0x00c5aa30 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf588"></a> `00bcf588` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcf58c"></a> `00bcf58c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcf590"></a> `00bcf590` | `34 2d 02 94` | bl 0x00c5aa60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf594"></a> `00bcf594` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcf598"></a> `00bcf598` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcf59c"></a> `00bcf59c` | `2d 2d 02 94` | bl 0x00c5aa50 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf5a0"></a> `00bcf5a0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcf5a4"></a> `00bcf5a4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcf5a8"></a> `00bcf5a8` | `3a 2d 02 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf5ac"></a> `00bcf5ac` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcf5b0"></a> `00bcf5b0` | `b0 2d 02 94` | bl 0x00c5ac70 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf5b4"></a> `00bcf5b4` | `e0 01 00 36` | tbz w0,#0x0,0x00bcf5f0 | `CONDITIONAL_JUMP`
<a id="insn-00bcf5b8"></a> `00bcf5b8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcf5bc"></a> `00bcf5bc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcf5c0"></a> `00bcf5c0` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcf5c4"></a> `00bcf5c4` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcf5c8"></a> `00bcf5c8` | `01 05 40 f9` | ldr x1,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bcf5cc"></a> `00bcf5cc` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcf5d0"></a> `00bcf5d0` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bcf5d4"></a> `00bcf5d4` | `20 00 1f d6` | br x1 | `COMPUTED_JUMP`
<a id="insn-00bcf5d8"></a> `00bcf5d8` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcf5dc"></a> `00bcf5dc` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcf5e0"></a> `00bcf5e0` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcf5e4"></a> `00bcf5e4` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bcf5e8"></a> `00bcf5e8` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bcf5ec"></a> `00bcf5ec` | `09 2c 02 14` | b 0x00c5a610 | `CALL_TERMINATOR`
<a id="insn-00bcf5f0"></a> `00bcf5f0` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcf5f4"></a> `00bcf5f4` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcf5f8"></a> `00bcf5f8` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcf5fc"></a> `00bcf5fc` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bcf600"></a> `00bcf600` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcf4fc`](#insn-00bcf4fc) 範囲 `[['00bcf4fc', '00bcf53b']]`
  - `CONDITIONAL_JUMP` [`00bcf538`](#insn-00bcf538) → [`00bcf5d8`](#insn-00bcf5d8)
  - `FALL_THROUGH` [`00bcf538`](#insn-00bcf538) → [`00bcf53c`](#insn-00bcf53c)
- ブロック [`00bcf53c`](#insn-00bcf53c) 範囲 `[['00bcf53c', '00bcf55b']]`
  - `CONDITIONAL_JUMP` [`00bcf558`](#insn-00bcf558) → [`00bcf568`](#insn-00bcf568)
  - `FALL_THROUGH` [`00bcf558`](#insn-00bcf558) → [`00bcf55c`](#insn-00bcf55c)
- ブロック [`00bcf55c`](#insn-00bcf55c) 範囲 `[['00bcf55c', '00bcf567']]`
  - `FALL_THROUGH` [`00bcf564`](#insn-00bcf564) → [`00bcf568`](#insn-00bcf568)
- ブロック [`00bcf568`](#insn-00bcf568) 範囲 `[['00bcf568', '00bcf573']]`
  - `FALL_THROUGH` [`00bcf570`](#insn-00bcf570) → [`00bcf574`](#insn-00bcf574)
- ブロック [`00bcf574`](#insn-00bcf574) 範囲 `[['00bcf574', '00bcf57f']]`
  - `FALL_THROUGH` [`00bcf57c`](#insn-00bcf57c) → [`00bcf580`](#insn-00bcf580)
- ブロック [`00bcf580`](#insn-00bcf580) 範囲 `[['00bcf580', '00bcf583']]`
  - `FALL_THROUGH` [`00bcf580`](#insn-00bcf580) → [`00bcf584`](#insn-00bcf584)
- ブロック [`00bcf584`](#insn-00bcf584) 範囲 `[['00bcf584', '00bcf587']]`
  - `FALL_THROUGH` [`00bcf584`](#insn-00bcf584) → [`00bcf588`](#insn-00bcf588)
- ブロック [`00bcf588`](#insn-00bcf588) 範囲 `[['00bcf588', '00bcf59b']]`
  - `FALL_THROUGH` [`00bcf598`](#insn-00bcf598) → [`00bcf59c`](#insn-00bcf59c)
- ブロック [`00bcf59c`](#insn-00bcf59c) 範囲 `[['00bcf59c', '00bcf5a3']]`
  - `FALL_THROUGH` [`00bcf5a0`](#insn-00bcf5a0) → [`00bcf5a4`](#insn-00bcf5a4)
- ブロック [`00bcf5a4`](#insn-00bcf5a4) 範囲 `[['00bcf5a4', '00bcf5b7']]`
  - `CONDITIONAL_JUMP` [`00bcf5b4`](#insn-00bcf5b4) → [`00bcf5f0`](#insn-00bcf5f0)
  - `FALL_THROUGH` [`00bcf5b4`](#insn-00bcf5b4) → [`00bcf5b8`](#insn-00bcf5b8)
- ブロック [`00bcf5b8`](#insn-00bcf5b8) 範囲 `[['00bcf5b8', '00bcf5cb']]`
  - `FALL_THROUGH` [`00bcf5c8`](#insn-00bcf5c8) → [`00bcf5cc`](#insn-00bcf5cc)
- ブロック [`00bcf5cc`](#insn-00bcf5cc) 範囲 `[['00bcf5cc', '00bcf5d7']]`
- ブロック [`00bcf5d8`](#insn-00bcf5d8) 範囲 `[['00bcf5d8', '00bcf5ef']]`
- ブロック [`00bcf5f0`](#insn-00bcf5f0) 範囲 `[['00bcf5f0', '00bcf603']]`

## 命令位置別の参照

- [`00bcf4fc`](#insn-00bcf4fc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf500`](#insn-00bcf500) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf504`](#insn-00bcf504) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf508`](#insn-00bcf508) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf528`](#insn-00bcf528) → [`00c5a600`](../00c5a/00c5a600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a600` · 推定シンボル `None` · 推定型 `None`
- [`00bcf534`](#insn-00bcf534) → [`00c5aa80`](../00c5a/00c5aa80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa80` · 推定シンボル `None` · 推定型 `None`
- [`00bcf538`](#insn-00bcf538) → [`00bcf5d8`](#insn-00bcf5d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf558`](#insn-00bcf558) → [`00bcf568`](#insn-00bcf568) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf560`](#insn-00bcf560) → `002a7008`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcf564`](#insn-00bcf564) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00bcf578`](#insn-00bcf578) → [`00c5aa70`](../00c5a/00c5aa70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa70` · 推定シンボル `None` · 推定型 `None`
- [`00bcf584`](#insn-00bcf584) → [`00c5aa30`](../00c5a/00c5aa30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa30` · 推定シンボル `None` · 推定型 `None`
- [`00bcf590`](#insn-00bcf590) → [`00c5aa60`](../00c5a/00c5aa60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa60` · 推定シンボル `None` · 推定型 `None`
- [`00bcf59c`](#insn-00bcf59c) → [`00c5aa50`](../00c5a/00c5aa50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa50` · 推定シンボル `None` · 推定型 `None`
- [`00bcf5a8`](#insn-00bcf5a8) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bcf5b0`](#insn-00bcf5b0) → [`00c5ac70`](../00c5a/00c5ac70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac70` · 推定シンボル `None` · 推定型 `None`
- [`00bcf5b4`](#insn-00bcf5b4) → [`00bcf5f0`](#insn-00bcf5f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf5c0`](#insn-00bcf5c0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf5c4`](#insn-00bcf5c4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf5cc`](#insn-00bcf5cc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf5d8`](#insn-00bcf5d8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf5dc`](#insn-00bcf5dc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf5e0`](#insn-00bcf5e0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf5ec`](#insn-00bcf5ec) → [`00c5a610`](../00c5a/00c5a610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a610` · 推定シンボル `None` · 推定型 `None`
- [`00bcf5f0`](#insn-00bcf5f0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf5f4`](#insn-00bcf5f4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf5f8`](#insn-00bcf5f8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcf4fc`](#insn-00bcf4fc)

~~~json
{
  "source": "00bcf4fc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf500`](#insn-00bcf500)

~~~json
{
  "source": "00bcf500",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf504`](#insn-00bcf504)

~~~json
{
  "source": "00bcf504",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf508`](#insn-00bcf508)

~~~json
{
  "source": "00bcf508",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf528`](#insn-00bcf528)

~~~json
{
  "source": "00bcf528",
  "target": "00c5a600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf534`](#insn-00bcf534)

~~~json
{
  "source": "00bcf534",
  "target": "00c5aa80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf538`](#insn-00bcf538)

~~~json
{
  "source": "00bcf538",
  "target": "00bcf5d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf558`](#insn-00bcf558)

~~~json
{
  "source": "00bcf558",
  "target": "00bcf568",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf560`](#insn-00bcf560)

~~~json
{
  "source": "00bcf560",
  "target": "002a7008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7008",
  "offset": 0,
  "size": 48,
  "datatype": "string",
  "bytes": "4765744675747572655374617475732868616e646c6529203d3d206b46757475",
  "capture_start": "002a7008",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcf564`](#insn-00bcf564)

~~~json
{
  "source": "00bcf564",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf578`](#insn-00bcf578)

~~~json
{
  "source": "00bcf578",
  "target": "00c5aa70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf584`](#insn-00bcf584)

~~~json
{
  "source": "00bcf584",
  "target": "00c5aa30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf590`](#insn-00bcf590)

~~~json
{
  "source": "00bcf590",
  "target": "00c5aa60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf59c`](#insn-00bcf59c)

~~~json
{
  "source": "00bcf59c",
  "target": "00c5aa50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf5a8`](#insn-00bcf5a8)

~~~json
{
  "source": "00bcf5a8",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf5b0`](#insn-00bcf5b0)

~~~json
{
  "source": "00bcf5b0",
  "target": "00c5ac70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf5b4`](#insn-00bcf5b4)

~~~json
{
  "source": "00bcf5b4",
  "target": "00bcf5f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf5c0`](#insn-00bcf5c0)

~~~json
{
  "source": "00bcf5c0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf5c4`](#insn-00bcf5c4)

~~~json
{
  "source": "00bcf5c4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf5cc`](#insn-00bcf5cc)

~~~json
{
  "source": "00bcf5cc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf5d8`](#insn-00bcf5d8)

~~~json
{
  "source": "00bcf5d8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf5dc`](#insn-00bcf5dc)

~~~json
{
  "source": "00bcf5dc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf5e0`](#insn-00bcf5e0)

~~~json
{
  "source": "00bcf5e0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf5ec`](#insn-00bcf5ec)

~~~json
{
  "source": "00bcf5ec",
  "target": "00c5a610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf5f0`](#insn-00bcf5f0)

~~~json
{
  "source": "00bcf5f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf5f4`](#insn-00bcf5f4)

~~~json
{
  "source": "00bcf5f4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf5f8`](#insn-00bcf5f8)

~~~json
{
  "source": "00bcf5f8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
