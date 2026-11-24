# 00bcbf1c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcbaf4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcbaf4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-c141c6bcdaeecfd9ce6be8b2429f3873)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcbfb8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbfb8.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-0fcdcdad20e8d5a7e94bb2b851b78e21)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbf1c",
  "name": "_ZNSt6__ndk16vectorIPN8firebase4auth4AuthENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "39950dce15118708e420e0078208e3175d11eb2f52a8be1261591039a8e98e83",
  "source_text_sha256": "39950dce15118708e420e0078208e3175d11eb2f52a8be1261591039a8e98e83",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbf1c",
        "00bcc013"
      ]
    ],
    "bytes_sha256": "8d9a80ddc4ca40ef0dbc34e1eeb2fc81aa2d59cae02dd95f666be0462e851d7e",
    "instruction_count": 62,
    "instruction_bytes": 248,
    "body_bytes": 248,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5db10](../00c5d/00c5db10.md)

## 呼び出し先

- [00b402c0](../00b40/00b402c0.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c58000](../00c58/00c58000.md)
- [00c5ad10](../00c5a/00c5ad10.md)

## 関連文字列（未確認候補）

~~~text
"allocator<T>::allocate(size_t n) 'n' exceeds maximum supported size"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1935 bytes

~~~c

void _ZNSt6__ndk16vectorIPN8firebase4auth4AuthENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_
               (undefined8 *param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  void *__src;
  void *__dest;
  ulong uVar2;
  size_t __n;
  ulong uVar3;
  
                    /* try { // try from 00bcbf2c to 00ccbf8b has its CatchHandler @ 00bcbf2c
                       catch() { ... } // from try @ 00bcbf2c with catch @ 00bcbf2c
                       catch() { ... } // from try @ 00bcbf98 with catch @ 00bcbf2c */
  __src = (void *)*param_1;
  __n = param_1[1] - (long)__src;
  uVar3 = ((long)__n >> 3) + 1;
  if (uVar3 >> 0x3d != 0) {
                    /* WARNING: Subroutine does not return */
    _ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv(param_1);
  }
  if ((ulong)(param_1[2] - (long)__src >> 3) < 0xfffffffffffffff) {
    uVar2 = param_1[2] - (long)__src >> 2;
    if (uVar3 <= uVar2) {
      uVar3 = uVar2;
    }
    if (uVar3 == 0) {
      __dest = (void *)0x0;
      goto LAB_00bcbf9c;
    }
    if (uVar3 >> 0x3d != 0) {
                    /* WARNING: Subroutine does not return */
      FUN_00b402c0("allocator<T>::allocate(size_t n) \'n\' exceeds maximum supported size");
    }
  }
  else {
                    /* try { // try from 00bcbf8c to 00ccbf97 has its CatchHandler @ 00bcbff0 */
    uVar3 = 0x1fffffffffffffff;
  }
  __dest = (void *)_Znwm(uVar3 << 3);
                    /* try { // try from 00bcbf98 to 00ccc017 has its CatchHandler @ 00bcbf2c */
LAB_00bcbf9c:
  puVar1 = (undefined8 *)((long)__dest + ((long)__n >> 3) * 8);
  *puVar1 = *param_2;
  if (0 < (long)__n) {
    memcpy(__dest,__src,__n);
  }
  *param_1 = __dest;
  param_1[1] = puVar1 + 1;
  param_1[2] = (void *)((long)__dest + uVar3 * 8);
  if (__src != (void *)0x0) {
    _ZdlPv(__src);
    return;
  }
                    /* catch() { ... } // from try @ 00bcbf8c with catch @ 00bcbff0 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbf1c"></a> `00bcbf1c` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bcbf20"></a> `00bcbf20` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbf24"></a> `00bcbf24` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbf28"></a> `00bcbf28` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcbf2c"></a> `00bcbf2c` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcbf30"></a> `00bcbf30` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bcbf34"></a> `00bcbf34` | `14 20 40 a9` | ldp x20,x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcbf38"></a> `00bcbf38` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcbf3c"></a> `00bcbf3c` | `15 01 14 cb` | sub x21,x8,x20 | `FALL_THROUGH`
<a id="insn-00bcbf40"></a> `00bcbf40` | `b8 fe 43 93` | asr x24,x21,#0x3 | `FALL_THROUGH`
<a id="insn-00bcbf44"></a> `00bcbf44` | `08 07 00 91` | add x8,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbf48"></a> `00bcbf48` | `09 fd 7d d3` | lsr x9,x8,#0x3d | `FALL_THROUGH`
<a id="insn-00bcbf4c"></a> `00bcbf4c` | `09 06 00 b5` | cbnz x9,0x00bcc00c | `CONDITIONAL_JUMP`
<a id="insn-00bcbf50"></a> `00bcbf50` | `69 0a 40 f9` | ldr x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbf54"></a> `00bcbf54` | `ea eb 7f b2` | orr x10,xzr,#0xffffffffffffffe | `FALL_THROUGH`
<a id="insn-00bcbf58"></a> `00bcbf58` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00bcbf5c"></a> `00bcbf5c` | `29 01 14 cb` | sub x9,x9,x20 | `FALL_THROUGH`
<a id="insn-00bcbf60"></a> `00bcbf60` | `5f 0d 89 eb` | cmp x10,x9, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00bcbf64"></a> `00bcbf64` | `43 01 00 54` | b.cc 0x00bcbf8c | `CONDITIONAL_JUMP`
<a id="insn-00bcbf68"></a> `00bcbf68` | `29 fd 42 93` | asr x9,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bcbf6c"></a> `00bcbf6c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcbf70"></a> `00bcbf70` | `19 31 89 9a` | csel x25,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00bcbf74"></a> `00bcbf74` | `99 04 00 b4` | cbz x25,0x00bcc004 | `CONDITIONAL_JUMP`
<a id="insn-00bcbf78"></a> `00bcbf78` | `28 ff 7d d3` | lsr x8,x25,#0x3d | `FALL_THROUGH`
<a id="insn-00bcbf7c"></a> `00bcbf7c` | `a8 00 00 b4` | cbz x8,0x00bcbf90 | `CONDITIONAL_JUMP`
<a id="insn-00bcbf80"></a> `00bcbf80` | `e0 b6 ff b0` | adrp x0,0x2a8000 | `FALL_THROUGH`
<a id="insn-00bcbf84"></a> `00bcbf84` | `00 ec 19 91` | add x0,x0,#0x67b | `FALL_THROUGH`
<a id="insn-00bcbf88"></a> `00bcbf88` | `ce d0 fd 97` | bl 0x00b402c0 | `CALL_TERMINATOR`
<a id="insn-00bcbf8c"></a> `00bcbf8c` | `19 00 fc 92` | mov x25,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bcbf90"></a> `00bcbf90` | `20 f3 7d d3` | lsl x0,x25,#0x3 | `FALL_THROUGH`
<a id="insn-00bcbf94"></a> `00bcbf94` | `bf 2f 02 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbf98"></a> `00bcbf98` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bcbf9c"></a> `00bcbf9c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bcbfa0"></a> `00bcbfa0` | `f8 0e 18 8b` | add x24,x23,x24, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bcbfa4"></a> `00bcbfa4` | `f6 0e 19 8b` | add x22,x23,x25, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bcbfa8"></a> `00bcbfa8` | `bf 06 00 f1` | cmp x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbfac"></a> `00bcbfac` | `08 87 00 f8` | str x8,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-00bcbfb0"></a> `00bcbfb0` | `ab 00 00 54` | b.lt 0x00bcbfc4 | `CONDITIONAL_JUMP`
<a id="insn-00bcbfb4"></a> `00bcbfb4` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bcbfb8"></a> `00bcbfb8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcbfbc"></a> `00bcbfbc` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bcbfc0"></a> `00bcbfc0` | `10 30 02 94` | bl 0x00c58000 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbfc4"></a> `00bcbfc4` | `77 62 00 a9` | stp x23,x24,[x19] | `FALL_THROUGH`
<a id="insn-00bcbfc8"></a> `00bcbfc8` | `76 0a 00 f9` | str x22,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbfcc"></a> `00bcbfcc` | `14 01 00 b4` | cbz x20,0x00bcbfec | `CONDITIONAL_JUMP`
<a id="insn-00bcbfd0"></a> `00bcbfd0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcbfd4"></a> `00bcbfd4` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcbfd8"></a> `00bcbfd8` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcbfdc"></a> `00bcbfdc` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbfe0"></a> `00bcbfe0` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbfe4"></a> `00bcbfe4` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcbfe8"></a> `00bcbfe8` | `b2 2f 02 14` | b 0x00c57eb0 | `CALL_TERMINATOR`
<a id="insn-00bcbfec"></a> `00bcbfec` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcbff0"></a> `00bcbff0` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcbff4"></a> `00bcbff4` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbff8"></a> `00bcbff8` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbffc"></a> `00bcbffc` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcc000"></a> `00bcc000` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcc004"></a> `00bcc004` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00bcc008"></a> `00bcc008` | `e5 ff ff 17` | b 0x00bcbf9c | `UNCONDITIONAL_JUMP`
<a id="insn-00bcc00c"></a> `00bcc00c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcc010"></a> `00bcc010` | `40 3b 02 94` | bl 0x00c5ad10 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbf1c`](#insn-00bcbf1c) 範囲 `[['00bcbf1c', '00bcbf2b']]`
  - `FALL_THROUGH` [`00bcbf28`](#insn-00bcbf28) → [`00bcbf2c`](#insn-00bcbf2c)
- ブロック [`00bcbf2c`](#insn-00bcbf2c) 範囲 `[['00bcbf2c', '00bcbf4f']]`
  - `CONDITIONAL_JUMP` [`00bcbf4c`](#insn-00bcbf4c) → [`00bcc00c`](#insn-00bcc00c)
  - `FALL_THROUGH` [`00bcbf4c`](#insn-00bcbf4c) → [`00bcbf50`](#insn-00bcbf50)
- ブロック [`00bcbf50`](#insn-00bcbf50) 範囲 `[['00bcbf50', '00bcbf67']]`
  - `CONDITIONAL_JUMP` [`00bcbf64`](#insn-00bcbf64) → [`00bcbf8c`](#insn-00bcbf8c)
  - `FALL_THROUGH` [`00bcbf64`](#insn-00bcbf64) → [`00bcbf68`](#insn-00bcbf68)
- ブロック [`00bcbf68`](#insn-00bcbf68) 範囲 `[['00bcbf68', '00bcbf77']]`
  - `CONDITIONAL_JUMP` [`00bcbf74`](#insn-00bcbf74) → [`00bcc004`](#insn-00bcc004)
  - `FALL_THROUGH` [`00bcbf74`](#insn-00bcbf74) → [`00bcbf78`](#insn-00bcbf78)
- ブロック [`00bcbf78`](#insn-00bcbf78) 範囲 `[['00bcbf78', '00bcbf7f']]`
  - `CONDITIONAL_JUMP` [`00bcbf7c`](#insn-00bcbf7c) → [`00bcbf90`](#insn-00bcbf90)
  - `FALL_THROUGH` [`00bcbf7c`](#insn-00bcbf7c) → [`00bcbf80`](#insn-00bcbf80)
- ブロック [`00bcbf80`](#insn-00bcbf80) 範囲 `[['00bcbf80', '00bcbf8b']]`
- ブロック [`00bcbf8c`](#insn-00bcbf8c) 範囲 `[['00bcbf8c', '00bcbf8f']]`
  - `FALL_THROUGH` [`00bcbf8c`](#insn-00bcbf8c) → [`00bcbf90`](#insn-00bcbf90)
- ブロック [`00bcbf90`](#insn-00bcbf90) 範囲 `[['00bcbf90', '00bcbf97']]`
  - `FALL_THROUGH` [`00bcbf94`](#insn-00bcbf94) → [`00bcbf98`](#insn-00bcbf98)
- ブロック [`00bcbf98`](#insn-00bcbf98) 範囲 `[['00bcbf98', '00bcbf9b']]`
  - `FALL_THROUGH` [`00bcbf98`](#insn-00bcbf98) → [`00bcbf9c`](#insn-00bcbf9c)
- ブロック [`00bcbf9c`](#insn-00bcbf9c) 範囲 `[['00bcbf9c', '00bcbfb3']]`
  - `CONDITIONAL_JUMP` [`00bcbfb0`](#insn-00bcbfb0) → [`00bcbfc4`](#insn-00bcbfc4)
  - `FALL_THROUGH` [`00bcbfb0`](#insn-00bcbfb0) → [`00bcbfb4`](#insn-00bcbfb4)
- ブロック [`00bcbfb4`](#insn-00bcbfb4) 範囲 `[['00bcbfb4', '00bcbfc3']]`
  - `FALL_THROUGH` [`00bcbfc0`](#insn-00bcbfc0) → [`00bcbfc4`](#insn-00bcbfc4)
- ブロック [`00bcbfc4`](#insn-00bcbfc4) 範囲 `[['00bcbfc4', '00bcbfcf']]`
  - `CONDITIONAL_JUMP` [`00bcbfcc`](#insn-00bcbfcc) → [`00bcbfec`](#insn-00bcbfec)
  - `FALL_THROUGH` [`00bcbfcc`](#insn-00bcbfcc) → [`00bcbfd0`](#insn-00bcbfd0)
- ブロック [`00bcbfd0`](#insn-00bcbfd0) 範囲 `[['00bcbfd0', '00bcbfeb']]`
- ブロック [`00bcbfec`](#insn-00bcbfec) 範囲 `[['00bcbfec', '00bcbfef']]`
  - `FALL_THROUGH` [`00bcbfec`](#insn-00bcbfec) → [`00bcbff0`](#insn-00bcbff0)
- ブロック [`00bcbff0`](#insn-00bcbff0) 範囲 `[['00bcbff0', '00bcc003']]`
- ブロック [`00bcc004`](#insn-00bcc004) 範囲 `[['00bcc004', '00bcc00b']]`
  - `UNCONDITIONAL_JUMP` [`00bcc008`](#insn-00bcc008) → [`00bcbf9c`](#insn-00bcbf9c)
- ブロック [`00bcc00c`](#insn-00bcc00c) 範囲 `[['00bcc00c', '00bcc013']]`

## 命令位置別の参照

- [`00bcbf1c`](#insn-00bcbf1c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf20`](#insn-00bcbf20) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf24`](#insn-00bcbf24) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf28`](#insn-00bcbf28) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf2c`](#insn-00bcbf2c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf4c`](#insn-00bcbf4c) → [`00bcc00c`](#insn-00bcc00c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf64`](#insn-00bcbf64) → [`00bcbf8c`](#insn-00bcbf8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf74`](#insn-00bcbf74) → [`00bcc004`](#insn-00bcc004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf7c`](#insn-00bcbf7c) → [`00bcbf90`](#insn-00bcbf90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf84`](#insn-00bcbf84) → `002a867b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcbf88`](#insn-00bcbf88) → [`00b402c0`](../00b40/00b402c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b402c0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf94`](#insn-00bcbf94) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfb0`](#insn-00bcbfb0) → [`00bcbfc4`](#insn-00bcbfc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfc0`](#insn-00bcbfc0) → [`00c58000`](../00c58/00c58000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58000` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfcc`](#insn-00bcbfcc) → [`00bcbfec`](#insn-00bcbfec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfd4`](#insn-00bcbfd4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfd8`](#insn-00bcbfd8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfdc`](#insn-00bcbfdc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfe0`](#insn-00bcbfe0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfe8`](#insn-00bcbfe8) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfec`](#insn-00bcbfec) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbff0`](#insn-00bcbff0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbff4`](#insn-00bcbff4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbff8`](#insn-00bcbff8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc008`](#insn-00bcc008) → [`00bcbf9c`](#insn-00bcbf9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc010`](#insn-00bcc010) → [`00c5ad10`](../00c5a/00c5ad10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad10` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbf1c`](#insn-00bcbf1c)

~~~json
{
  "source": "00bcbf1c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf20`](#insn-00bcbf20)

~~~json
{
  "source": "00bcbf20",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf24`](#insn-00bcbf24)

~~~json
{
  "source": "00bcbf24",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf28`](#insn-00bcbf28)

~~~json
{
  "source": "00bcbf28",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf2c`](#insn-00bcbf2c)

~~~json
{
  "source": "00bcbf2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf4c`](#insn-00bcbf4c)

~~~json
{
  "source": "00bcbf4c",
  "target": "00bcc00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf64`](#insn-00bcbf64)

~~~json
{
  "source": "00bcbf64",
  "target": "00bcbf8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf74`](#insn-00bcbf74)

~~~json
{
  "source": "00bcbf74",
  "target": "00bcc004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf7c`](#insn-00bcbf7c)

~~~json
{
  "source": "00bcbf7c",
  "target": "00bcbf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf84`](#insn-00bcbf84)

~~~json
{
  "source": "00bcbf84",
  "target": "002a867b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a867b",
  "offset": 0,
  "size": 68,
  "datatype": "string",
  "bytes": "616c6c6f6361746f723c543e3a3a616c6c6f636174652873697a655f74206e29",
  "capture_start": "002a867b",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcbf88`](#insn-00bcbf88)

~~~json
{
  "source": "00bcbf88",
  "target": "00b402c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbf94`](#insn-00bcbf94)

~~~json
{
  "source": "00bcbf94",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbfb0`](#insn-00bcbfb0)

~~~json
{
  "source": "00bcbfb0",
  "target": "00bcbfc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfc0`](#insn-00bcbfc0)

~~~json
{
  "source": "00bcbfc0",
  "target": "00c58000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbfcc`](#insn-00bcbfcc)

~~~json
{
  "source": "00bcbfcc",
  "target": "00bcbfec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfd4`](#insn-00bcbfd4)

~~~json
{
  "source": "00bcbfd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfd8`](#insn-00bcbfd8)

~~~json
{
  "source": "00bcbfd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfdc`](#insn-00bcbfdc)

~~~json
{
  "source": "00bcbfdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfe0`](#insn-00bcbfe0)

~~~json
{
  "source": "00bcbfe0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfe8`](#insn-00bcbfe8)

~~~json
{
  "source": "00bcbfe8",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbfec`](#insn-00bcbfec)

~~~json
{
  "source": "00bcbfec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbff0`](#insn-00bcbff0)

~~~json
{
  "source": "00bcbff0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbff4`](#insn-00bcbff4)

~~~json
{
  "source": "00bcbff4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbff8`](#insn-00bcbff8)

~~~json
{
  "source": "00bcbff8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc008`](#insn-00bcc008)

~~~json
{
  "source": "00bcc008",
  "target": "00bcbf9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc010`](#insn-00bcc010)

~~~json
{
  "source": "00bcc010",
  "target": "00c5ad10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
