# 00bcbec0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcbe24`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbe24.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-40690e2c0ae136ec2a903a23c9adb07c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bcceb4`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bcceb4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-a0c6fcadc2e92bff76dc054232e8d19d)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbec0",
  "name": "_ZNSt6__ndk16vectorIPN8firebase4auth17AuthStateListenerENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "56f87ac2e002769108b440ef395d19893bf75ac9141ab963220723eb4a4e24ab",
  "source_text_sha256": "56f87ac2e002769108b440ef395d19893bf75ac9141ab963220723eb4a4e24ab",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbec0",
        "00bcbfb7"
      ]
    ],
    "bytes_sha256": "d762dd86dda968f5c92bf7db11d5ed664fe375753459b89303695313850e3dcf",
    "instruction_count": 62,
    "instruction_bytes": 248,
    "body_bytes": 248,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5dbc0](../00c5d/00c5dbc0.md)

## 呼び出し先

- [00b4035c](../00b40/00b4035c.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c580d0](../00c58/00c580d0.md)
- [00c5ade0](../00c5a/00c5ade0.md)

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
                    /* catch() { ... } // from try @ 00bcbdf4 with catch @ 00bcbee8 */
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
      goto LAB_00bcbf40;
    }
    if (uVar3 >> 0x3d != 0) {
                    /* WARNING: Subroutine does not return */
      FUN_00b4035c("allocator<T>::allocate(size_t n) \'n\' exceeds maximum supported size");
    }
  }
  else {
    uVar3 = 0x1fffffffffffffff;
  }
  __dest = (void *)_Znwm(uVar3 << 3);
LAB_00bcbf40:
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
                    /* try { // try from 00bcbf9c to 00ccbffb has its CatchHandler @ 00bcbf9c
                       catch() { ... } // from try @ 00bcbf9c with catch @ 00bcbf9c
                       catch() { ... } // from try @ 00bcc008 with catch @ 00bcbf9c */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbec0"></a> `00bcbec0` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bcbec4"></a> `00bcbec4` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbec8"></a> `00bcbec8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbecc"></a> `00bcbecc` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcbed0"></a> `00bcbed0` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcbed4"></a> `00bcbed4` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bcbed8"></a> `00bcbed8` | `14 20 40 a9` | ldp x20,x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcbedc"></a> `00bcbedc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcbee0"></a> `00bcbee0` | `15 01 14 cb` | sub x21,x8,x20 | `FALL_THROUGH`
<a id="insn-00bcbee4"></a> `00bcbee4` | `b8 fe 43 93` | asr x24,x21,#0x3 | `FALL_THROUGH`
<a id="insn-00bcbee8"></a> `00bcbee8` | `08 07 00 91` | add x8,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbeec"></a> `00bcbeec` | `09 fd 7d d3` | lsr x9,x8,#0x3d | `FALL_THROUGH`
<a id="insn-00bcbef0"></a> `00bcbef0` | `09 06 00 b5` | cbnz x9,0x00bcbfb0 | `CONDITIONAL_JUMP`
<a id="insn-00bcbef4"></a> `00bcbef4` | `69 0a 40 f9` | ldr x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbef8"></a> `00bcbef8` | `ea eb 7f b2` | orr x10,xzr,#0xffffffffffffffe | `FALL_THROUGH`
<a id="insn-00bcbefc"></a> `00bcbefc` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00bcbf00"></a> `00bcbf00` | `29 01 14 cb` | sub x9,x9,x20 | `FALL_THROUGH`
<a id="insn-00bcbf04"></a> `00bcbf04` | `5f 0d 89 eb` | cmp x10,x9, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00bcbf08"></a> `00bcbf08` | `43 01 00 54` | b.cc 0x00bcbf30 | `CONDITIONAL_JUMP`
<a id="insn-00bcbf0c"></a> `00bcbf0c` | `29 fd 42 93` | asr x9,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bcbf10"></a> `00bcbf10` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcbf14"></a> `00bcbf14` | `19 31 89 9a` | csel x25,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00bcbf18"></a> `00bcbf18` | `99 04 00 b4` | cbz x25,0x00bcbfa8 | `CONDITIONAL_JUMP`
<a id="insn-00bcbf1c"></a> `00bcbf1c` | `28 ff 7d d3` | lsr x8,x25,#0x3d | `FALL_THROUGH`
<a id="insn-00bcbf20"></a> `00bcbf20` | `a8 00 00 b4` | cbz x8,0x00bcbf34 | `CONDITIONAL_JUMP`
<a id="insn-00bcbf24"></a> `00bcbf24` | `e0 b6 ff b0` | adrp x0,0x2a8000 | `FALL_THROUGH`
<a id="insn-00bcbf28"></a> `00bcbf28` | `00 7c 18 91` | add x0,x0,#0x61f | `FALL_THROUGH`
<a id="insn-00bcbf2c"></a> `00bcbf2c` | `0c d1 fd 97` | bl 0x00b4035c | `CALL_TERMINATOR`
<a id="insn-00bcbf30"></a> `00bcbf30` | `19 00 fc 92` | mov x25,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bcbf34"></a> `00bcbf34` | `20 f3 7d d3` | lsl x0,x25,#0x3 | `FALL_THROUGH`
<a id="insn-00bcbf38"></a> `00bcbf38` | `0a 30 02 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbf3c"></a> `00bcbf3c` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bcbf40"></a> `00bcbf40` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bcbf44"></a> `00bcbf44` | `f8 0e 18 8b` | add x24,x23,x24, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bcbf48"></a> `00bcbf48` | `f6 0e 19 8b` | add x22,x23,x25, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bcbf4c"></a> `00bcbf4c` | `bf 06 00 f1` | cmp x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbf50"></a> `00bcbf50` | `08 87 00 f8` | str x8,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-00bcbf54"></a> `00bcbf54` | `ab 00 00 54` | b.lt 0x00bcbf68 | `CONDITIONAL_JUMP`
<a id="insn-00bcbf58"></a> `00bcbf58` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bcbf5c"></a> `00bcbf5c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcbf60"></a> `00bcbf60` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bcbf64"></a> `00bcbf64` | `5b 30 02 94` | bl 0x00c580d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbf68"></a> `00bcbf68` | `77 62 00 a9` | stp x23,x24,[x19] | `FALL_THROUGH`
<a id="insn-00bcbf6c"></a> `00bcbf6c` | `76 0a 00 f9` | str x22,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbf70"></a> `00bcbf70` | `14 01 00 b4` | cbz x20,0x00bcbf90 | `CONDITIONAL_JUMP`
<a id="insn-00bcbf74"></a> `00bcbf74` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcbf78"></a> `00bcbf78` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcbf7c"></a> `00bcbf7c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcbf80"></a> `00bcbf80` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbf84"></a> `00bcbf84` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbf88"></a> `00bcbf88` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcbf8c"></a> `00bcbf8c` | `fd 2f 02 14` | b 0x00c57f80 | `CALL_TERMINATOR`
<a id="insn-00bcbf90"></a> `00bcbf90` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcbf94"></a> `00bcbf94` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcbf98"></a> `00bcbf98` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbf9c"></a> `00bcbf9c` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbfa0"></a> `00bcbfa0` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcbfa4"></a> `00bcbfa4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcbfa8"></a> `00bcbfa8` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00bcbfac"></a> `00bcbfac` | `e5 ff ff 17` | b 0x00bcbf40 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcbfb0"></a> `00bcbfb0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcbfb4"></a> `00bcbfb4` | `8b 3b 02 94` | bl 0x00c5ade0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbec0`](#insn-00bcbec0) 範囲 `[['00bcbec0', '00bcbee7']]`
  - `FALL_THROUGH` [`00bcbee4`](#insn-00bcbee4) → [`00bcbee8`](#insn-00bcbee8)
- ブロック [`00bcbee8`](#insn-00bcbee8) 範囲 `[['00bcbee8', '00bcbef3']]`
  - `CONDITIONAL_JUMP` [`00bcbef0`](#insn-00bcbef0) → [`00bcbfb0`](#insn-00bcbfb0)
  - `FALL_THROUGH` [`00bcbef0`](#insn-00bcbef0) → [`00bcbef4`](#insn-00bcbef4)
- ブロック [`00bcbef4`](#insn-00bcbef4) 範囲 `[['00bcbef4', '00bcbf0b']]`
  - `CONDITIONAL_JUMP` [`00bcbf08`](#insn-00bcbf08) → [`00bcbf30`](#insn-00bcbf30)
  - `FALL_THROUGH` [`00bcbf08`](#insn-00bcbf08) → [`00bcbf0c`](#insn-00bcbf0c)
- ブロック [`00bcbf0c`](#insn-00bcbf0c) 範囲 `[['00bcbf0c', '00bcbf1b']]`
  - `CONDITIONAL_JUMP` [`00bcbf18`](#insn-00bcbf18) → [`00bcbfa8`](#insn-00bcbfa8)
  - `FALL_THROUGH` [`00bcbf18`](#insn-00bcbf18) → [`00bcbf1c`](#insn-00bcbf1c)
- ブロック [`00bcbf1c`](#insn-00bcbf1c) 範囲 `[['00bcbf1c', '00bcbf23']]`
  - `CONDITIONAL_JUMP` [`00bcbf20`](#insn-00bcbf20) → [`00bcbf34`](#insn-00bcbf34)
  - `FALL_THROUGH` [`00bcbf20`](#insn-00bcbf20) → [`00bcbf24`](#insn-00bcbf24)
- ブロック [`00bcbf24`](#insn-00bcbf24) 範囲 `[['00bcbf24', '00bcbf2f']]`
- ブロック [`00bcbf30`](#insn-00bcbf30) 範囲 `[['00bcbf30', '00bcbf33']]`
  - `FALL_THROUGH` [`00bcbf30`](#insn-00bcbf30) → [`00bcbf34`](#insn-00bcbf34)
- ブロック [`00bcbf34`](#insn-00bcbf34) 範囲 `[['00bcbf34', '00bcbf3f']]`
  - `FALL_THROUGH` [`00bcbf3c`](#insn-00bcbf3c) → [`00bcbf40`](#insn-00bcbf40)
- ブロック [`00bcbf40`](#insn-00bcbf40) 範囲 `[['00bcbf40', '00bcbf57']]`
  - `CONDITIONAL_JUMP` [`00bcbf54`](#insn-00bcbf54) → [`00bcbf68`](#insn-00bcbf68)
  - `FALL_THROUGH` [`00bcbf54`](#insn-00bcbf54) → [`00bcbf58`](#insn-00bcbf58)
- ブロック [`00bcbf58`](#insn-00bcbf58) 範囲 `[['00bcbf58', '00bcbf67']]`
  - `FALL_THROUGH` [`00bcbf64`](#insn-00bcbf64) → [`00bcbf68`](#insn-00bcbf68)
- ブロック [`00bcbf68`](#insn-00bcbf68) 範囲 `[['00bcbf68', '00bcbf73']]`
  - `CONDITIONAL_JUMP` [`00bcbf70`](#insn-00bcbf70) → [`00bcbf90`](#insn-00bcbf90)
  - `FALL_THROUGH` [`00bcbf70`](#insn-00bcbf70) → [`00bcbf74`](#insn-00bcbf74)
- ブロック [`00bcbf74`](#insn-00bcbf74) 範囲 `[['00bcbf74', '00bcbf8f']]`
- ブロック [`00bcbf90`](#insn-00bcbf90) 範囲 `[['00bcbf90', '00bcbf9b']]`
  - `FALL_THROUGH` [`00bcbf98`](#insn-00bcbf98) → [`00bcbf9c`](#insn-00bcbf9c)
- ブロック [`00bcbf9c`](#insn-00bcbf9c) 範囲 `[['00bcbf9c', '00bcbfa7']]`
- ブロック [`00bcbfa8`](#insn-00bcbfa8) 範囲 `[['00bcbfa8', '00bcbfaf']]`
  - `UNCONDITIONAL_JUMP` [`00bcbfac`](#insn-00bcbfac) → [`00bcbf40`](#insn-00bcbf40)
- ブロック [`00bcbfb0`](#insn-00bcbfb0) 範囲 `[['00bcbfb0', '00bcbfb7']]`

## 命令位置別の参照

- [`00bcbec0`](#insn-00bcbec0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbec4`](#insn-00bcbec4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbec8`](#insn-00bcbec8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbecc`](#insn-00bcbecc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbed0`](#insn-00bcbed0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbef0`](#insn-00bcbef0) → [`00bcbfb0`](#insn-00bcbfb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf08`](#insn-00bcbf08) → [`00bcbf30`](#insn-00bcbf30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf18`](#insn-00bcbf18) → [`00bcbfa8`](#insn-00bcbfa8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf20`](#insn-00bcbf20) → [`00bcbf34`](#insn-00bcbf34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf28`](#insn-00bcbf28) → `002a861f`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcbf2c`](#insn-00bcbf2c) → [`00b4035c`](../00b40/00b4035c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b4035c` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf38`](#insn-00bcbf38) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf54`](#insn-00bcbf54) → [`00bcbf68`](#insn-00bcbf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf64`](#insn-00bcbf64) → [`00c580d0`](../00c58/00c580d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580d0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf70`](#insn-00bcbf70) → [`00bcbf90`](#insn-00bcbf90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf78`](#insn-00bcbf78) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf7c`](#insn-00bcbf7c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf80`](#insn-00bcbf80) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf84`](#insn-00bcbf84) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf8c`](#insn-00bcbf8c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf90`](#insn-00bcbf90) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf94`](#insn-00bcbf94) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf98`](#insn-00bcbf98) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf9c`](#insn-00bcbf9c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfac`](#insn-00bcbfac) → [`00bcbf40`](#insn-00bcbf40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfb4`](#insn-00bcbfb4) → [`00c5ade0`](../00c5a/00c5ade0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ade0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbec0`](#insn-00bcbec0)

~~~json
{
  "source": "00bcbec0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbec4`](#insn-00bcbec4)

~~~json
{
  "source": "00bcbec4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbec8`](#insn-00bcbec8)

~~~json
{
  "source": "00bcbec8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbecc`](#insn-00bcbecc)

~~~json
{
  "source": "00bcbecc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbed0`](#insn-00bcbed0)

~~~json
{
  "source": "00bcbed0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbef0`](#insn-00bcbef0)

~~~json
{
  "source": "00bcbef0",
  "target": "00bcbfb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf08`](#insn-00bcbf08)

~~~json
{
  "source": "00bcbf08",
  "target": "00bcbf30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf18`](#insn-00bcbf18)

~~~json
{
  "source": "00bcbf18",
  "target": "00bcbfa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf20`](#insn-00bcbf20)

~~~json
{
  "source": "00bcbf20",
  "target": "00bcbf34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf28`](#insn-00bcbf28)

~~~json
{
  "source": "00bcbf28",
  "target": "002a861f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a861f",
  "offset": 0,
  "size": 68,
  "datatype": "string",
  "bytes": "616c6c6f6361746f723c543e3a3a616c6c6f636174652873697a655f74206e29",
  "capture_start": "002a861f",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcbf2c`](#insn-00bcbf2c)

~~~json
{
  "source": "00bcbf2c",
  "target": "00b4035c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbf38`](#insn-00bcbf38)

~~~json
{
  "source": "00bcbf38",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbf54`](#insn-00bcbf54)

~~~json
{
  "source": "00bcbf54",
  "target": "00bcbf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf64`](#insn-00bcbf64)

~~~json
{
  "source": "00bcbf64",
  "target": "00c580d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbf70`](#insn-00bcbf70)

~~~json
{
  "source": "00bcbf70",
  "target": "00bcbf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf78`](#insn-00bcbf78)

~~~json
{
  "source": "00bcbf78",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf7c`](#insn-00bcbf7c)

~~~json
{
  "source": "00bcbf7c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf80`](#insn-00bcbf80)

~~~json
{
  "source": "00bcbf80",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf84`](#insn-00bcbf84)

~~~json
{
  "source": "00bcbf84",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf8c`](#insn-00bcbf8c)

~~~json
{
  "source": "00bcbf8c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbf90`](#insn-00bcbf90)

~~~json
{
  "source": "00bcbf90",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf94`](#insn-00bcbf94)

~~~json
{
  "source": "00bcbf94",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf98`](#insn-00bcbf98)

~~~json
{
  "source": "00bcbf98",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf9c`](#insn-00bcbf9c)

~~~json
{
  "source": "00bcbf9c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfac`](#insn-00bcbfac)

~~~json
{
  "source": "00bcbfac",
  "target": "00bcbf40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfb4`](#insn-00bcbfb4)

~~~json
{
  "source": "00bcbfb4",
  "target": "00c5ade0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
