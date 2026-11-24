# 00bcf6fc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcf2d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf2d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0082.md#compare-656f8980a51e1eb79104060c6cd666d4)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcf798`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcf/00bcf798.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-7ebcba543615fb448df590bf8bffcf5b)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcf6fc",
  "name": "_ZN8firebase4auth29CheckAndCompleteFutureOnErrorIvEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2cb774b8b29fceab434bea459de44f0db3f80fe56a6b880b8211052d7d829a7b",
  "source_text_sha256": "2cb774b8b29fceab434bea459de44f0db3f80fe56a6b880b8211052d7d829a7b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcf6fc",
        "00bcf7cb"
      ]
    ],
    "bytes_sha256": "40484009c8d4f840c05339fdd2244320f4129188d925a9510db1a23f1b2fe9d5",
    "instruction_count": 52,
    "instruction_bytes": 208,
    "body_bytes": 208,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5dd00](../00c5d/00c5dd00.md)

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c5aa90](../00c5a/00c5aa90.md)
- [00c5ada0](../00c5a/00c5ada0.md)
- [00c5ae00](../00c5a/00c5ae00.md)
- [00c5dd10](../00c5d/00c5dd10.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2444 bytes

~~~c

undefined8
_ZN8firebase4auth29CheckAndCompleteFutureOnErrorIvEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
          (undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  void *pvVar1;
  long lVar2;
  int iVar3;
  undefined8 uVar4;
  undefined1 auStack_68 [16];
  ulong local_58;
  undefined8 local_50;
  void *local_48;
  undefined1 auStack_40 [8];
  long local_38;
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  local_50 = 0;
  local_48 = (void *)0x0;
  local_58 = 0;
  iVar3 = _ZN8firebase4auth30CheckAndClearJniAuthExceptionsEP7_JNIEnvPNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE
                    (param_1,&local_58);
  if (iVar3 == 0) {
    uVar4 = 0;
  }
  else {
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_68,param_3);
    pvVar1 = (void *)((ulong)&local_58 | 1);
    if ((local_58 & 1) != 0) {
      pvVar1 = local_48;
    }
                    /* try { // try from 00bcf770 to 00ccf77b has its CatchHandler @ 00bcf7c8 */
    _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
              (param_2,auStack_68,iVar3,pvVar1,auStack_40);
    _ZN8firebase12FutureHandleD2Ev(auStack_68);
                    /* catch() { ... } // from try @ 00bcf5e8 with catch @ 00bcf77c
                       try { // try from 00bcf77c to 00ccf7f7 has its CatchHandler @ 00bcf4f4 */
    uVar4 = 1;
                    /* catch() { ... } // from try @ 00bcf5a4 with catch @ 00bcf780 */
                    /* catch() { ... } // from try @ 00bcf558 with catch @ 00bcf784 */
  }
  if ((local_58 & 1) != 0) {
    _ZdlPv(local_48);
  }
                    /* catch() { ... } // from try @ 00bcf690 with catch @ 00bcf798 */
  if (*(long *)(lVar2 + 0x28) == local_38) {
                    /* catch() { ... } // from try @ 00bcf6c8 with catch @ 00bcf7a0 */
    return uVar4;
  }
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00bcf524 with catch @ 00bcf7c8
                       catch() { ... } // from try @ 00bcf568 with catch @ 00bcf7c8
                       catch() { ... } // from try @ 00bcf5b4 with catch @ 00bcf7c8
                       catch() { ... } // from try @ 00bcf64c with catch @ 00bcf7c8
                       catch() { ... } // from try @ 00bcf770 with catch @ 00bcf7c8 */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcf6fc"></a> `00bcf6fc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bcf700"></a> `00bcf700` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcf704"></a> `00bcf704` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcf708"></a> `00bcf708` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcf70c"></a> `00bcf70c` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bcf710"></a> `00bcf710` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bcf714"></a> `00bcf714` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00bcf718"></a> `00bcf718` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-00bcf71c"></a> `00bcf71c` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcf720"></a> `00bcf720` | `a8 83 1d f8` | stur x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00bcf724"></a> `00bcf724` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcf728"></a> `00bcf728` | `ff 0f 00 f9` | str xzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcf72c"></a> `00bcf72c` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcf730"></a> `00bcf730` | `78 39 02 94` | bl 0x00c5dd10 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf734"></a> `00bcf734` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bcf738"></a> `00bcf738` | `00 04 00 34` | cbz w0,0x00bcf7b8 | `CONDITIONAL_JUMP`
<a id="insn-00bcf73c"></a> `00bcf73c` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcf740"></a> `00bcf740` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bcf744"></a> `00bcf744` | `af 2d 02 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf748"></a> `00bcf748` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcf74c"></a> `00bcf74c` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bcf750"></a> `00bcf750` | `ea 63 00 91` | add x10,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcf754"></a> `00bcf754` | `4a 01 40 b2` | orr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcf758"></a> `00bcf758` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcf75c"></a> `00bcf75c` | `43 01 89 9a` | csel x3,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bcf760"></a> `00bcf760` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcf764"></a> `00bcf764` | `e4 c3 00 91` | add x4,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bcf768"></a> `00bcf768` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcf76c"></a> `00bcf76c` | `e2 03 14 2a` | mov w2,w20 | `FALL_THROUGH`
<a id="insn-00bcf770"></a> `00bcf770` | `8c 2d 02 94` | bl 0x00c5ada0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf774"></a> `00bcf774` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcf778"></a> `00bcf778` | `c6 2c 02 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf77c"></a> `00bcf77c` | `33 00 80 52` | mov w19,#0x1 | `FALL_THROUGH`
<a id="insn-00bcf780"></a> `00bcf780` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcf784"></a> `00bcf784` | `68 00 00 36` | tbz w8,#0x0,0x00bcf790 | `CONDITIONAL_JUMP`
<a id="insn-00bcf788"></a> `00bcf788` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bcf78c"></a> `00bcf78c` | `c9 21 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf790"></a> `00bcf790` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00bcf794"></a> `00bcf794` | `a9 83 5d f8` | ldur x9,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00bcf798"></a> `00bcf798` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcf79c"></a> `00bcf79c` | `61 01 00 54` | b.ne 0x00bcf7c8 | `CONDITIONAL_JUMP`
<a id="insn-00bcf7a0"></a> `00bcf7a0` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00bcf7a4"></a> `00bcf7a4` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcf7a8"></a> `00bcf7a8` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcf7ac"></a> `00bcf7ac` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcf7b0"></a> `00bcf7b0` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bcf7b4"></a> `00bcf7b4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcf7b8"></a> `00bcf7b8` | `f3 03 1f 2a` | mov w19,wzr | `FALL_THROUGH`
<a id="insn-00bcf7bc"></a> `00bcf7bc` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcf7c0"></a> `00bcf7c0` | `48 fe 07 37` | tbnz w8,#0x0,0x00bcf788 | `CONDITIONAL_JUMP`
<a id="insn-00bcf7c4"></a> `00bcf7c4` | `f3 ff ff 17` | b 0x00bcf790 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcf7c8"></a> `00bcf7c8` | `c6 21 02 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcf6fc`](#insn-00bcf6fc) 範囲 `[['00bcf6fc', '00bcf73b']]`
  - `CONDITIONAL_JUMP` [`00bcf738`](#insn-00bcf738) → [`00bcf7b8`](#insn-00bcf7b8)
  - `FALL_THROUGH` [`00bcf738`](#insn-00bcf738) → [`00bcf73c`](#insn-00bcf73c)
- ブロック [`00bcf73c`](#insn-00bcf73c) 範囲 `[['00bcf73c', '00bcf76f']]`
  - `FALL_THROUGH` [`00bcf76c`](#insn-00bcf76c) → [`00bcf770`](#insn-00bcf770)
- ブロック [`00bcf770`](#insn-00bcf770) 範囲 `[['00bcf770', '00bcf77b']]`
  - `FALL_THROUGH` [`00bcf778`](#insn-00bcf778) → [`00bcf77c`](#insn-00bcf77c)
- ブロック [`00bcf77c`](#insn-00bcf77c) 範囲 `[['00bcf77c', '00bcf77f']]`
  - `FALL_THROUGH` [`00bcf77c`](#insn-00bcf77c) → [`00bcf780`](#insn-00bcf780)
- ブロック [`00bcf780`](#insn-00bcf780) 範囲 `[['00bcf780', '00bcf783']]`
  - `FALL_THROUGH` [`00bcf780`](#insn-00bcf780) → [`00bcf784`](#insn-00bcf784)
- ブロック [`00bcf784`](#insn-00bcf784) 範囲 `[['00bcf784', '00bcf787']]`
  - `CONDITIONAL_JUMP` [`00bcf784`](#insn-00bcf784) → [`00bcf790`](#insn-00bcf790)
  - `FALL_THROUGH` [`00bcf784`](#insn-00bcf784) → [`00bcf788`](#insn-00bcf788)
- ブロック [`00bcf788`](#insn-00bcf788) 範囲 `[['00bcf788', '00bcf78f']]`
  - `FALL_THROUGH` [`00bcf78c`](#insn-00bcf78c) → [`00bcf790`](#insn-00bcf790)
- ブロック [`00bcf790`](#insn-00bcf790) 範囲 `[['00bcf790', '00bcf797']]`
  - `FALL_THROUGH` [`00bcf794`](#insn-00bcf794) → [`00bcf798`](#insn-00bcf798)
- ブロック [`00bcf798`](#insn-00bcf798) 範囲 `[['00bcf798', '00bcf79f']]`
  - `CONDITIONAL_JUMP` [`00bcf79c`](#insn-00bcf79c) → [`00bcf7c8`](#insn-00bcf7c8)
  - `FALL_THROUGH` [`00bcf79c`](#insn-00bcf79c) → [`00bcf7a0`](#insn-00bcf7a0)
- ブロック [`00bcf7a0`](#insn-00bcf7a0) 範囲 `[['00bcf7a0', '00bcf7b7']]`
- ブロック [`00bcf7b8`](#insn-00bcf7b8) 範囲 `[['00bcf7b8', '00bcf7c3']]`
  - `CONDITIONAL_JUMP` [`00bcf7c0`](#insn-00bcf7c0) → [`00bcf788`](#insn-00bcf788)
  - `FALL_THROUGH` [`00bcf7c0`](#insn-00bcf7c0) → [`00bcf7c4`](#insn-00bcf7c4)
- ブロック [`00bcf7c4`](#insn-00bcf7c4) 範囲 `[['00bcf7c4', '00bcf7c7']]`
  - `UNCONDITIONAL_JUMP` [`00bcf7c4`](#insn-00bcf7c4) → [`00bcf790`](#insn-00bcf790)
- ブロック [`00bcf7c8`](#insn-00bcf7c8) 範囲 `[['00bcf7c8', '00bcf7cb']]`

## 命令位置別の参照

- [`00bcf700`](#insn-00bcf700) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf704`](#insn-00bcf704) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf708`](#insn-00bcf708) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf720`](#insn-00bcf720) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf724`](#insn-00bcf724) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf728`](#insn-00bcf728) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf730`](#insn-00bcf730) → [`00c5dd10`](../00c5d/00c5dd10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dd10` · 推定シンボル `None` · 推定型 `None`
- [`00bcf738`](#insn-00bcf738) → [`00bcf7b8`](#insn-00bcf7b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf744`](#insn-00bcf744) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00bcf748`](#insn-00bcf748) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf74c`](#insn-00bcf74c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf770`](#insn-00bcf770) → [`00c5ada0`](../00c5a/00c5ada0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ada0` · 推定シンボル `None` · 推定型 `None`
- [`00bcf778`](#insn-00bcf778) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bcf780`](#insn-00bcf780) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf784`](#insn-00bcf784) → [`00bcf790`](#insn-00bcf790) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf788`](#insn-00bcf788) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf78c`](#insn-00bcf78c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bcf794`](#insn-00bcf794) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf79c`](#insn-00bcf79c) → [`00bcf7c8`](#insn-00bcf7c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf7a4`](#insn-00bcf7a4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf7a8`](#insn-00bcf7a8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf7ac`](#insn-00bcf7ac) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf7bc`](#insn-00bcf7bc) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf7c0`](#insn-00bcf7c0) → [`00bcf788`](#insn-00bcf788) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf7c4`](#insn-00bcf7c4) → [`00bcf790`](#insn-00bcf790) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf7c8`](#insn-00bcf7c8) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcf700`](#insn-00bcf700)

~~~json
{
  "source": "00bcf700",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf704`](#insn-00bcf704)

~~~json
{
  "source": "00bcf704",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf708`](#insn-00bcf708)

~~~json
{
  "source": "00bcf708",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf720`](#insn-00bcf720)

~~~json
{
  "source": "00bcf720",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf724`](#insn-00bcf724)

~~~json
{
  "source": "00bcf724",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf728`](#insn-00bcf728)

~~~json
{
  "source": "00bcf728",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf730`](#insn-00bcf730)

~~~json
{
  "source": "00bcf730",
  "target": "00c5dd10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf738`](#insn-00bcf738)

~~~json
{
  "source": "00bcf738",
  "target": "00bcf7b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf744`](#insn-00bcf744)

~~~json
{
  "source": "00bcf744",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf748`](#insn-00bcf748)

~~~json
{
  "source": "00bcf748",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf74c`](#insn-00bcf74c)

~~~json
{
  "source": "00bcf74c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf770`](#insn-00bcf770)

~~~json
{
  "source": "00bcf770",
  "target": "00c5ada0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf778`](#insn-00bcf778)

~~~json
{
  "source": "00bcf778",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf780`](#insn-00bcf780)

~~~json
{
  "source": "00bcf780",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf784`](#insn-00bcf784)

~~~json
{
  "source": "00bcf784",
  "target": "00bcf790",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf788`](#insn-00bcf788)

~~~json
{
  "source": "00bcf788",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf78c`](#insn-00bcf78c)

~~~json
{
  "source": "00bcf78c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf794`](#insn-00bcf794)

~~~json
{
  "source": "00bcf794",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf79c`](#insn-00bcf79c)

~~~json
{
  "source": "00bcf79c",
  "target": "00bcf7c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf7a4`](#insn-00bcf7a4)

~~~json
{
  "source": "00bcf7a4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf7a8`](#insn-00bcf7a8)

~~~json
{
  "source": "00bcf7a8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf7ac`](#insn-00bcf7ac)

~~~json
{
  "source": "00bcf7ac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf7bc`](#insn-00bcf7bc)

~~~json
{
  "source": "00bcf7bc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf7c0`](#insn-00bcf7c0)

~~~json
{
  "source": "00bcf7c0",
  "target": "00bcf788",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf7c4`](#insn-00bcf7c4)

~~~json
{
  "source": "00bcf7c4",
  "target": "00bcf790",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf7c8`](#insn-00bcf7c8)

~~~json
{
  "source": "00bcf7c8",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
