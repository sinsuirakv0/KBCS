# 00bcceb4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcbec0`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbec0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-a0c6fcadc2e92bff76dc054232e8d19d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcceb4",
  "name": "_ZNSt6__ndk16vectorIPN8firebase4auth17AuthStateListenerENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e4e40875b42fdb7b163912ba515653a1ff9d02f457ac9c7609489d3c41e2f230",
  "source_text_sha256": "e4e40875b42fdb7b163912ba515653a1ff9d02f457ac9c7609489d3c41e2f230",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcceb4",
        "00bccfab"
      ]
    ],
    "bytes_sha256": "e8fbbbd1894814bbed36ce6243c61cca7f7f09ccce4253a9f78a7f856e61a3fa",
    "instruction_count": 62,
    "instruction_bytes": 248,
    "body_bytes": 248,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5eb90](../00c5e/00c5eb90.md)

## 呼び出し先

- [00b41350](../00b41/00b41350.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c590a0](../00c59/00c590a0.md)
- [00c5bdb0](../00c5b/00c5bdb0.md)

## 関連文字列（未確認候補）

~~~text
"allocator<T>::allocate(size_t n) 'n' exceeds maximum supported size"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1755 bytes

~~~c

void _ZNSt6__ndk16vectorIPN8firebase4auth17AuthStateListenerENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_
               (undefined8 *param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  void *__src;
  void *__dest;
  ulong uVar2;
  size_t __n;
  ulong uVar3;
  
  __src = (void *)*param_1;
  __n = param_1[1] - (long)__src;
                    /* catch() { ... } // from try @ 00bccde8 with catch @ 00bccedc */
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
      goto LAB_00bccf34;
    }
    if (uVar3 >> 0x3d != 0) {
                    /* WARNING: Subroutine does not return */
      FUN_00b41350("allocator<T>::allocate(size_t n) \'n\' exceeds maximum supported size");
    }
  }
  else {
    uVar3 = 0x1fffffffffffffff;
  }
  __dest = (void *)_Znwm(uVar3 << 3);
LAB_00bccf34:
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
                    /* try { // try from 00bccf90 to 00cccfef has its CatchHandler @ 00bccf90
                       catch() { ... } // from try @ 00bccf90 with catch @ 00bccf90
                       catch() { ... } // from try @ 00bccffc with catch @ 00bccf90 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcceb4"></a> `00bcceb4` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bcceb8"></a> `00bcceb8` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccebc"></a> `00bccebc` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bccec0"></a> `00bccec0` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bccec4"></a> `00bccec4` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bccec8"></a> `00bccec8` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bccecc"></a> `00bccecc` | `14 20 40 a9` | ldp x20,x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcced0"></a> `00bcced0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcced4"></a> `00bcced4` | `15 01 14 cb` | sub x21,x8,x20 | `FALL_THROUGH`
<a id="insn-00bcced8"></a> `00bcced8` | `b8 fe 43 93` | asr x24,x21,#0x3 | `FALL_THROUGH`
<a id="insn-00bccedc"></a> `00bccedc` | `08 07 00 91` | add x8,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00bccee0"></a> `00bccee0` | `09 fd 7d d3` | lsr x9,x8,#0x3d | `FALL_THROUGH`
<a id="insn-00bccee4"></a> `00bccee4` | `09 06 00 b5` | cbnz x9,0x00bccfa4 | `CONDITIONAL_JUMP`
<a id="insn-00bccee8"></a> `00bccee8` | `69 0a 40 f9` | ldr x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcceec"></a> `00bcceec` | `ea eb 7f b2` | orr x10,xzr,#0xffffffffffffffe | `FALL_THROUGH`
<a id="insn-00bccef0"></a> `00bccef0` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00bccef4"></a> `00bccef4` | `29 01 14 cb` | sub x9,x9,x20 | `FALL_THROUGH`
<a id="insn-00bccef8"></a> `00bccef8` | `5f 0d 89 eb` | cmp x10,x9, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00bccefc"></a> `00bccefc` | `43 01 00 54` | b.cc 0x00bccf24 | `CONDITIONAL_JUMP`
<a id="insn-00bccf00"></a> `00bccf00` | `29 fd 42 93` | asr x9,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bccf04"></a> `00bccf04` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bccf08"></a> `00bccf08` | `19 31 89 9a` | csel x25,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00bccf0c"></a> `00bccf0c` | `99 04 00 b4` | cbz x25,0x00bccf9c | `CONDITIONAL_JUMP`
<a id="insn-00bccf10"></a> `00bccf10` | `28 ff 7d d3` | lsr x8,x25,#0x3d | `FALL_THROUGH`
<a id="insn-00bccf14"></a> `00bccf14` | `a8 00 00 b4` | cbz x8,0x00bccf28 | `CONDITIONAL_JUMP`
<a id="insn-00bccf18"></a> `00bccf18` | `e0 b6 ff 90` | adrp x0,0x2a8000 | `FALL_THROUGH`
<a id="insn-00bccf1c"></a> `00bccf1c` | `00 dc 1d 91` | add x0,x0,#0x777 | `FALL_THROUGH`
<a id="insn-00bccf20"></a> `00bccf20` | `0c d1 fd 97` | bl 0x00b41350 | `CALL_TERMINATOR`
<a id="insn-00bccf24"></a> `00bccf24` | `19 00 fc 92` | mov x25,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bccf28"></a> `00bccf28` | `20 f3 7d d3` | lsl x0,x25,#0x3 | `FALL_THROUGH`
<a id="insn-00bccf2c"></a> `00bccf2c` | `01 30 02 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00bccf30"></a> `00bccf30` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bccf34"></a> `00bccf34` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bccf38"></a> `00bccf38` | `f8 0e 18 8b` | add x24,x23,x24, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bccf3c"></a> `00bccf3c` | `f6 0e 19 8b` | add x22,x23,x25, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bccf40"></a> `00bccf40` | `bf 06 00 f1` | cmp x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bccf44"></a> `00bccf44` | `08 87 00 f8` | str x8,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-00bccf48"></a> `00bccf48` | `ab 00 00 54` | b.lt 0x00bccf5c | `CONDITIONAL_JUMP`
<a id="insn-00bccf4c"></a> `00bccf4c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bccf50"></a> `00bccf50` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bccf54"></a> `00bccf54` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bccf58"></a> `00bccf58` | `52 30 02 94` | bl 0x00c590a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bccf5c"></a> `00bccf5c` | `77 62 00 a9` | stp x23,x24,[x19] | `FALL_THROUGH`
<a id="insn-00bccf60"></a> `00bccf60` | `76 0a 00 f9` | str x22,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bccf64"></a> `00bccf64` | `14 01 00 b4` | cbz x20,0x00bccf84 | `CONDITIONAL_JUMP`
<a id="insn-00bccf68"></a> `00bccf68` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bccf6c"></a> `00bccf6c` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bccf70"></a> `00bccf70` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bccf74"></a> `00bccf74` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bccf78"></a> `00bccf78` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccf7c"></a> `00bccf7c` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bccf80"></a> `00bccf80` | `f4 2f 02 14` | b 0x00c58f50 | `CALL_TERMINATOR`
<a id="insn-00bccf84"></a> `00bccf84` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bccf88"></a> `00bccf88` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bccf8c"></a> `00bccf8c` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bccf90"></a> `00bccf90` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccf94"></a> `00bccf94` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bccf98"></a> `00bccf98` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bccf9c"></a> `00bccf9c` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00bccfa0"></a> `00bccfa0` | `e5 ff ff 17` | b 0x00bccf34 | `UNCONDITIONAL_JUMP`
<a id="insn-00bccfa4"></a> `00bccfa4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bccfa8"></a> `00bccfa8` | `82 3b 02 94` | bl 0x00c5bdb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcceb4`](#insn-00bcceb4) 範囲 `[['00bcceb4', '00bccedb']]`
  - `FALL_THROUGH` [`00bcced8`](#insn-00bcced8) → [`00bccedc`](#insn-00bccedc)
- ブロック [`00bccedc`](#insn-00bccedc) 範囲 `[['00bccedc', '00bccee7']]`
  - `CONDITIONAL_JUMP` [`00bccee4`](#insn-00bccee4) → [`00bccfa4`](#insn-00bccfa4)
  - `FALL_THROUGH` [`00bccee4`](#insn-00bccee4) → [`00bccee8`](#insn-00bccee8)
- ブロック [`00bccee8`](#insn-00bccee8) 範囲 `[['00bccee8', '00bcceff']]`
  - `CONDITIONAL_JUMP` [`00bccefc`](#insn-00bccefc) → [`00bccf24`](#insn-00bccf24)
  - `FALL_THROUGH` [`00bccefc`](#insn-00bccefc) → [`00bccf00`](#insn-00bccf00)
- ブロック [`00bccf00`](#insn-00bccf00) 範囲 `[['00bccf00', '00bccf0f']]`
  - `CONDITIONAL_JUMP` [`00bccf0c`](#insn-00bccf0c) → [`00bccf9c`](#insn-00bccf9c)
  - `FALL_THROUGH` [`00bccf0c`](#insn-00bccf0c) → [`00bccf10`](#insn-00bccf10)
- ブロック [`00bccf10`](#insn-00bccf10) 範囲 `[['00bccf10', '00bccf17']]`
  - `CONDITIONAL_JUMP` [`00bccf14`](#insn-00bccf14) → [`00bccf28`](#insn-00bccf28)
  - `FALL_THROUGH` [`00bccf14`](#insn-00bccf14) → [`00bccf18`](#insn-00bccf18)
- ブロック [`00bccf18`](#insn-00bccf18) 範囲 `[['00bccf18', '00bccf23']]`
- ブロック [`00bccf24`](#insn-00bccf24) 範囲 `[['00bccf24', '00bccf27']]`
  - `FALL_THROUGH` [`00bccf24`](#insn-00bccf24) → [`00bccf28`](#insn-00bccf28)
- ブロック [`00bccf28`](#insn-00bccf28) 範囲 `[['00bccf28', '00bccf33']]`
  - `FALL_THROUGH` [`00bccf30`](#insn-00bccf30) → [`00bccf34`](#insn-00bccf34)
- ブロック [`00bccf34`](#insn-00bccf34) 範囲 `[['00bccf34', '00bccf4b']]`
  - `CONDITIONAL_JUMP` [`00bccf48`](#insn-00bccf48) → [`00bccf5c`](#insn-00bccf5c)
  - `FALL_THROUGH` [`00bccf48`](#insn-00bccf48) → [`00bccf4c`](#insn-00bccf4c)
- ブロック [`00bccf4c`](#insn-00bccf4c) 範囲 `[['00bccf4c', '00bccf5b']]`
  - `FALL_THROUGH` [`00bccf58`](#insn-00bccf58) → [`00bccf5c`](#insn-00bccf5c)
- ブロック [`00bccf5c`](#insn-00bccf5c) 範囲 `[['00bccf5c', '00bccf67']]`
  - `CONDITIONAL_JUMP` [`00bccf64`](#insn-00bccf64) → [`00bccf84`](#insn-00bccf84)
  - `FALL_THROUGH` [`00bccf64`](#insn-00bccf64) → [`00bccf68`](#insn-00bccf68)
- ブロック [`00bccf68`](#insn-00bccf68) 範囲 `[['00bccf68', '00bccf83']]`
- ブロック [`00bccf84`](#insn-00bccf84) 範囲 `[['00bccf84', '00bccf8f']]`
  - `FALL_THROUGH` [`00bccf8c`](#insn-00bccf8c) → [`00bccf90`](#insn-00bccf90)
- ブロック [`00bccf90`](#insn-00bccf90) 範囲 `[['00bccf90', '00bccf9b']]`
- ブロック [`00bccf9c`](#insn-00bccf9c) 範囲 `[['00bccf9c', '00bccfa3']]`
  - `UNCONDITIONAL_JUMP` [`00bccfa0`](#insn-00bccfa0) → [`00bccf34`](#insn-00bccf34)
- ブロック [`00bccfa4`](#insn-00bccfa4) 範囲 `[['00bccfa4', '00bccfab']]`

## 命令位置別の参照

- [`00bcceb4`](#insn-00bcceb4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcceb8`](#insn-00bcceb8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccebc`](#insn-00bccebc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccec0`](#insn-00bccec0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccec4`](#insn-00bccec4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccee4`](#insn-00bccee4) → [`00bccfa4`](#insn-00bccfa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccefc`](#insn-00bccefc) → [`00bccf24`](#insn-00bccf24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccf0c`](#insn-00bccf0c) → [`00bccf9c`](#insn-00bccf9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccf14`](#insn-00bccf14) → [`00bccf28`](#insn-00bccf28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccf1c`](#insn-00bccf1c) → `002a8777`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bccf20`](#insn-00bccf20) → [`00b41350`](../00b41/00b41350.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b41350` · 推定シンボル `None` · 推定型 `None`
- [`00bccf2c`](#insn-00bccf2c) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00bccf48`](#insn-00bccf48) → [`00bccf5c`](#insn-00bccf5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccf58`](#insn-00bccf58) → [`00c590a0`](../00c59/00c590a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590a0` · 推定シンボル `None` · 推定型 `None`
- [`00bccf64`](#insn-00bccf64) → [`00bccf84`](#insn-00bccf84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccf6c`](#insn-00bccf6c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccf70`](#insn-00bccf70) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccf74`](#insn-00bccf74) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccf78`](#insn-00bccf78) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccf80`](#insn-00bccf80) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bccf84`](#insn-00bccf84) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccf88`](#insn-00bccf88) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccf8c`](#insn-00bccf8c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccf90`](#insn-00bccf90) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccfa0`](#insn-00bccfa0) → [`00bccf34`](#insn-00bccf34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccfa8`](#insn-00bccfa8) → [`00c5bdb0`](../00c5b/00c5bdb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bdb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcceb4`](#insn-00bcceb4)

~~~json
{
  "source": "00bcceb4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcceb8`](#insn-00bcceb8)

~~~json
{
  "source": "00bcceb8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccebc`](#insn-00bccebc)

~~~json
{
  "source": "00bccebc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccec0`](#insn-00bccec0)

~~~json
{
  "source": "00bccec0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccec4`](#insn-00bccec4)

~~~json
{
  "source": "00bccec4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccee4`](#insn-00bccee4)

~~~json
{
  "source": "00bccee4",
  "target": "00bccfa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccefc`](#insn-00bccefc)

~~~json
{
  "source": "00bccefc",
  "target": "00bccf24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccf0c`](#insn-00bccf0c)

~~~json
{
  "source": "00bccf0c",
  "target": "00bccf9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccf14`](#insn-00bccf14)

~~~json
{
  "source": "00bccf14",
  "target": "00bccf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccf1c`](#insn-00bccf1c)

~~~json
{
  "source": "00bccf1c",
  "target": "002a8777",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8777",
  "offset": 0,
  "size": 68,
  "datatype": "string",
  "bytes": "616c6c6f6361746f723c543e3a3a616c6c6f636174652873697a655f74206e29",
  "capture_start": "002a8777",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bccf20`](#insn-00bccf20)

~~~json
{
  "source": "00bccf20",
  "target": "00b41350",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bccf2c`](#insn-00bccf2c)

~~~json
{
  "source": "00bccf2c",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bccf48`](#insn-00bccf48)

~~~json
{
  "source": "00bccf48",
  "target": "00bccf5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccf58`](#insn-00bccf58)

~~~json
{
  "source": "00bccf58",
  "target": "00c590a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bccf64`](#insn-00bccf64)

~~~json
{
  "source": "00bccf64",
  "target": "00bccf84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccf6c`](#insn-00bccf6c)

~~~json
{
  "source": "00bccf6c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccf70`](#insn-00bccf70)

~~~json
{
  "source": "00bccf70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccf74`](#insn-00bccf74)

~~~json
{
  "source": "00bccf74",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccf78`](#insn-00bccf78)

~~~json
{
  "source": "00bccf78",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccf80`](#insn-00bccf80)

~~~json
{
  "source": "00bccf80",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bccf84`](#insn-00bccf84)

~~~json
{
  "source": "00bccf84",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccf88`](#insn-00bccf88)

~~~json
{
  "source": "00bccf88",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccf8c`](#insn-00bccf8c)

~~~json
{
  "source": "00bccf8c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccf90`](#insn-00bccf90)

~~~json
{
  "source": "00bccf90",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccfa0`](#insn-00bccfa0)

~~~json
{
  "source": "00bccfa0",
  "target": "00bccf34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccfa8`](#insn-00bccfa8)

~~~json
{
  "source": "00bccfa8",
  "target": "00c5bdb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
