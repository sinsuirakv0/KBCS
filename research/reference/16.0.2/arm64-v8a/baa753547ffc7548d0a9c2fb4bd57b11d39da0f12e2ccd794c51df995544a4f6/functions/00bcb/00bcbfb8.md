# 00bcbfb8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcbf1c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbf1c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-0fcdcdad20e8d5a7e94bb2b851b78e21)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bccfac`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcc/00bccfac.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-f555eacc3f3fa939ec604e07b5ff5cfc)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbfb8",
  "name": "_ZNSt6__ndk16vectorIPN8firebase4auth4AuthENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3dcdcb5dd3e4271a962e8e3a1d8db6529d8d157cecef43328f9e545a1a3f327d",
  "source_text_sha256": "3dcdcb5dd3e4271a962e8e3a1d8db6529d8d157cecef43328f9e545a1a3f327d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbfb8",
        "00bcc0af"
      ]
    ],
    "bytes_sha256": "4aeebf9c68c828889729ae006f3b0942f31b397cbc007e817e7125f66a48ab5c",
    "instruction_count": 62,
    "instruction_bytes": 248,
    "body_bytes": 248,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5dbe0](../00c5d/00c5dbe0.md)

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

## 疑似コード / UTF-8 1670 bytes

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
  
  __src = (void *)*param_1;
  __n = param_1[1] - (long)__src;
  uVar3 = ((long)__n >> 3) + 1;
  if (uVar3 >> 0x3d != 0) {
                    /* WARNING: Subroutine does not return */
    _ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv(param_1);
  }
                    /* try { // try from 00bcbffc to 00ccc007 has its CatchHandler @ 00bcc060 */
  if ((ulong)(param_1[2] - (long)__src >> 3) < 0xfffffffffffffff) {
    uVar2 = param_1[2] - (long)__src >> 2;
                    /* try { // try from 00bcc008 to 00ccc087 has its CatchHandler @ 00bcbf9c */
    if (uVar3 <= uVar2) {
      uVar3 = uVar2;
    }
    if (uVar3 == 0) {
      __dest = (void *)0x0;
      goto LAB_00bcc038;
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
LAB_00bcc038:
  puVar1 = (undefined8 *)((long)__dest + ((long)__n >> 3) * 8);
  *puVar1 = *param_2;
  if (0 < (long)__n) {
    memcpy(__dest,__src,__n);
  }
                    /* catch() { ... } // from try @ 00bcbffc with catch @ 00bcc060 */
  *param_1 = __dest;
  param_1[1] = puVar1 + 1;
  param_1[2] = (void *)((long)__dest + uVar3 * 8);
  if (__src != (void *)0x0) {
    _ZdlPv(__src);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbfb8"></a> `00bcbfb8` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bcbfbc"></a> `00bcbfbc` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbfc0"></a> `00bcbfc0` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbfc4"></a> `00bcbfc4` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcbfc8"></a> `00bcbfc8` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcbfcc"></a> `00bcbfcc` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bcbfd0"></a> `00bcbfd0` | `14 20 40 a9` | ldp x20,x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcbfd4"></a> `00bcbfd4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcbfd8"></a> `00bcbfd8` | `15 01 14 cb` | sub x21,x8,x20 | `FALL_THROUGH`
<a id="insn-00bcbfdc"></a> `00bcbfdc` | `b8 fe 43 93` | asr x24,x21,#0x3 | `FALL_THROUGH`
<a id="insn-00bcbfe0"></a> `00bcbfe0` | `08 07 00 91` | add x8,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbfe4"></a> `00bcbfe4` | `09 fd 7d d3` | lsr x9,x8,#0x3d | `FALL_THROUGH`
<a id="insn-00bcbfe8"></a> `00bcbfe8` | `09 06 00 b5` | cbnz x9,0x00bcc0a8 | `CONDITIONAL_JUMP`
<a id="insn-00bcbfec"></a> `00bcbfec` | `69 0a 40 f9` | ldr x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbff0"></a> `00bcbff0` | `ea eb 7f b2` | orr x10,xzr,#0xffffffffffffffe | `FALL_THROUGH`
<a id="insn-00bcbff4"></a> `00bcbff4` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00bcbff8"></a> `00bcbff8` | `29 01 14 cb` | sub x9,x9,x20 | `FALL_THROUGH`
<a id="insn-00bcbffc"></a> `00bcbffc` | `5f 0d 89 eb` | cmp x10,x9, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00bcc000"></a> `00bcc000` | `43 01 00 54` | b.cc 0x00bcc028 | `CONDITIONAL_JUMP`
<a id="insn-00bcc004"></a> `00bcc004` | `29 fd 42 93` | asr x9,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bcc008"></a> `00bcc008` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcc00c"></a> `00bcc00c` | `19 31 89 9a` | csel x25,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00bcc010"></a> `00bcc010` | `99 04 00 b4` | cbz x25,0x00bcc0a0 | `CONDITIONAL_JUMP`
<a id="insn-00bcc014"></a> `00bcc014` | `28 ff 7d d3` | lsr x8,x25,#0x3d | `FALL_THROUGH`
<a id="insn-00bcc018"></a> `00bcc018` | `a8 00 00 b4` | cbz x8,0x00bcc02c | `CONDITIONAL_JUMP`
<a id="insn-00bcc01c"></a> `00bcc01c` | `e0 b6 ff 90` | adrp x0,0x2a8000 | `FALL_THROUGH`
<a id="insn-00bcc020"></a> `00bcc020` | `00 7c 18 91` | add x0,x0,#0x61f | `FALL_THROUGH`
<a id="insn-00bcc024"></a> `00bcc024` | `ce d0 fd 97` | bl 0x00b4035c | `CALL_TERMINATOR`
<a id="insn-00bcc028"></a> `00bcc028` | `19 00 fc 92` | mov x25,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bcc02c"></a> `00bcc02c` | `20 f3 7d d3` | lsl x0,x25,#0x3 | `FALL_THROUGH`
<a id="insn-00bcc030"></a> `00bcc030` | `cc 2f 02 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcc034"></a> `00bcc034` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bcc038"></a> `00bcc038` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bcc03c"></a> `00bcc03c` | `f8 0e 18 8b` | add x24,x23,x24, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bcc040"></a> `00bcc040` | `f6 0e 19 8b` | add x22,x23,x25, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bcc044"></a> `00bcc044` | `bf 06 00 f1` | cmp x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bcc048"></a> `00bcc048` | `08 87 00 f8` | str x8,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-00bcc04c"></a> `00bcc04c` | `ab 00 00 54` | b.lt 0x00bcc060 | `CONDITIONAL_JUMP`
<a id="insn-00bcc050"></a> `00bcc050` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bcc054"></a> `00bcc054` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcc058"></a> `00bcc058` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bcc05c"></a> `00bcc05c` | `1d 30 02 94` | bl 0x00c580d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcc060"></a> `00bcc060` | `77 62 00 a9` | stp x23,x24,[x19] | `FALL_THROUGH`
<a id="insn-00bcc064"></a> `00bcc064` | `76 0a 00 f9` | str x22,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc068"></a> `00bcc068` | `14 01 00 b4` | cbz x20,0x00bcc088 | `CONDITIONAL_JUMP`
<a id="insn-00bcc06c"></a> `00bcc06c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcc070"></a> `00bcc070` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcc074"></a> `00bcc074` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcc078"></a> `00bcc078` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcc07c"></a> `00bcc07c` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc080"></a> `00bcc080` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcc084"></a> `00bcc084` | `bf 2f 02 14` | b 0x00c57f80 | `CALL_TERMINATOR`
<a id="insn-00bcc088"></a> `00bcc088` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcc08c"></a> `00bcc08c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcc090"></a> `00bcc090` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcc094"></a> `00bcc094` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc098"></a> `00bcc098` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcc09c"></a> `00bcc09c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcc0a0"></a> `00bcc0a0` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00bcc0a4"></a> `00bcc0a4` | `e5 ff ff 17` | b 0x00bcc038 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcc0a8"></a> `00bcc0a8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcc0ac"></a> `00bcc0ac` | `4d 3b 02 94` | bl 0x00c5ade0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbfb8`](#insn-00bcbfb8) 範囲 `[['00bcbfb8', '00bcbfeb']]`
  - `CONDITIONAL_JUMP` [`00bcbfe8`](#insn-00bcbfe8) → [`00bcc0a8`](#insn-00bcc0a8)
  - `FALL_THROUGH` [`00bcbfe8`](#insn-00bcbfe8) → [`00bcbfec`](#insn-00bcbfec)
- ブロック [`00bcbfec`](#insn-00bcbfec) 範囲 `[['00bcbfec', '00bcbffb']]`
  - `FALL_THROUGH` [`00bcbff8`](#insn-00bcbff8) → [`00bcbffc`](#insn-00bcbffc)
- ブロック [`00bcbffc`](#insn-00bcbffc) 範囲 `[['00bcbffc', '00bcc003']]`
  - `CONDITIONAL_JUMP` [`00bcc000`](#insn-00bcc000) → [`00bcc028`](#insn-00bcc028)
  - `FALL_THROUGH` [`00bcc000`](#insn-00bcc000) → [`00bcc004`](#insn-00bcc004)
- ブロック [`00bcc004`](#insn-00bcc004) 範囲 `[['00bcc004', '00bcc007']]`
  - `FALL_THROUGH` [`00bcc004`](#insn-00bcc004) → [`00bcc008`](#insn-00bcc008)
- ブロック [`00bcc008`](#insn-00bcc008) 範囲 `[['00bcc008', '00bcc013']]`
  - `CONDITIONAL_JUMP` [`00bcc010`](#insn-00bcc010) → [`00bcc0a0`](#insn-00bcc0a0)
  - `FALL_THROUGH` [`00bcc010`](#insn-00bcc010) → [`00bcc014`](#insn-00bcc014)
- ブロック [`00bcc014`](#insn-00bcc014) 範囲 `[['00bcc014', '00bcc01b']]`
  - `CONDITIONAL_JUMP` [`00bcc018`](#insn-00bcc018) → [`00bcc02c`](#insn-00bcc02c)
  - `FALL_THROUGH` [`00bcc018`](#insn-00bcc018) → [`00bcc01c`](#insn-00bcc01c)
- ブロック [`00bcc01c`](#insn-00bcc01c) 範囲 `[['00bcc01c', '00bcc027']]`
- ブロック [`00bcc028`](#insn-00bcc028) 範囲 `[['00bcc028', '00bcc02b']]`
  - `FALL_THROUGH` [`00bcc028`](#insn-00bcc028) → [`00bcc02c`](#insn-00bcc02c)
- ブロック [`00bcc02c`](#insn-00bcc02c) 範囲 `[['00bcc02c', '00bcc037']]`
  - `FALL_THROUGH` [`00bcc034`](#insn-00bcc034) → [`00bcc038`](#insn-00bcc038)
- ブロック [`00bcc038`](#insn-00bcc038) 範囲 `[['00bcc038', '00bcc04f']]`
  - `CONDITIONAL_JUMP` [`00bcc04c`](#insn-00bcc04c) → [`00bcc060`](#insn-00bcc060)
  - `FALL_THROUGH` [`00bcc04c`](#insn-00bcc04c) → [`00bcc050`](#insn-00bcc050)
- ブロック [`00bcc050`](#insn-00bcc050) 範囲 `[['00bcc050', '00bcc05f']]`
  - `FALL_THROUGH` [`00bcc05c`](#insn-00bcc05c) → [`00bcc060`](#insn-00bcc060)
- ブロック [`00bcc060`](#insn-00bcc060) 範囲 `[['00bcc060', '00bcc06b']]`
  - `CONDITIONAL_JUMP` [`00bcc068`](#insn-00bcc068) → [`00bcc088`](#insn-00bcc088)
  - `FALL_THROUGH` [`00bcc068`](#insn-00bcc068) → [`00bcc06c`](#insn-00bcc06c)
- ブロック [`00bcc06c`](#insn-00bcc06c) 範囲 `[['00bcc06c', '00bcc087']]`
- ブロック [`00bcc088`](#insn-00bcc088) 範囲 `[['00bcc088', '00bcc09f']]`
- ブロック [`00bcc0a0`](#insn-00bcc0a0) 範囲 `[['00bcc0a0', '00bcc0a7']]`
  - `UNCONDITIONAL_JUMP` [`00bcc0a4`](#insn-00bcc0a4) → [`00bcc038`](#insn-00bcc038)
- ブロック [`00bcc0a8`](#insn-00bcc0a8) 範囲 `[['00bcc0a8', '00bcc0af']]`

## 命令位置別の参照

- [`00bcbfb8`](#insn-00bcbfb8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfbc`](#insn-00bcbfbc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfc0`](#insn-00bcbfc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfc4`](#insn-00bcbfc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfc8`](#insn-00bcbfc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfe8`](#insn-00bcbfe8) → [`00bcc0a8`](#insn-00bcc0a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc000`](#insn-00bcc000) → [`00bcc028`](#insn-00bcc028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc010`](#insn-00bcc010) → [`00bcc0a0`](#insn-00bcc0a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc018`](#insn-00bcc018) → [`00bcc02c`](#insn-00bcc02c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc020`](#insn-00bcc020) → `002a861f`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcc024`](#insn-00bcc024) → [`00b4035c`](../00b40/00b4035c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b4035c` · 推定シンボル `None` · 推定型 `None`
- [`00bcc030`](#insn-00bcc030) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00bcc04c`](#insn-00bcc04c) → [`00bcc060`](#insn-00bcc060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc05c`](#insn-00bcc05c) → [`00c580d0`](../00c58/00c580d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580d0` · 推定シンボル `None` · 推定型 `None`
- [`00bcc068`](#insn-00bcc068) → [`00bcc088`](#insn-00bcc088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc070`](#insn-00bcc070) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc074`](#insn-00bcc074) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc078`](#insn-00bcc078) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc07c`](#insn-00bcc07c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc084`](#insn-00bcc084) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00bcc088`](#insn-00bcc088) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc08c`](#insn-00bcc08c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc090`](#insn-00bcc090) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc094`](#insn-00bcc094) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc0a4`](#insn-00bcc0a4) → [`00bcc038`](#insn-00bcc038) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc0ac`](#insn-00bcc0ac) → [`00c5ade0`](../00c5a/00c5ade0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ade0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbfb8`](#insn-00bcbfb8)

~~~json
{
  "source": "00bcbfb8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfbc`](#insn-00bcbfbc)

~~~json
{
  "source": "00bcbfbc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfc0`](#insn-00bcbfc0)

~~~json
{
  "source": "00bcbfc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfc4`](#insn-00bcbfc4)

~~~json
{
  "source": "00bcbfc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfc8`](#insn-00bcbfc8)

~~~json
{
  "source": "00bcbfc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfe8`](#insn-00bcbfe8)

~~~json
{
  "source": "00bcbfe8",
  "target": "00bcc0a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc000`](#insn-00bcc000)

~~~json
{
  "source": "00bcc000",
  "target": "00bcc028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc010`](#insn-00bcc010)

~~~json
{
  "source": "00bcc010",
  "target": "00bcc0a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc018`](#insn-00bcc018)

~~~json
{
  "source": "00bcc018",
  "target": "00bcc02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc020`](#insn-00bcc020)

~~~json
{
  "source": "00bcc020",
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
- 参照命令 [`00bcc024`](#insn-00bcc024)

~~~json
{
  "source": "00bcc024",
  "target": "00b4035c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcc030`](#insn-00bcc030)

~~~json
{
  "source": "00bcc030",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcc04c`](#insn-00bcc04c)

~~~json
{
  "source": "00bcc04c",
  "target": "00bcc060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc05c`](#insn-00bcc05c)

~~~json
{
  "source": "00bcc05c",
  "target": "00c580d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcc068`](#insn-00bcc068)

~~~json
{
  "source": "00bcc068",
  "target": "00bcc088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc070`](#insn-00bcc070)

~~~json
{
  "source": "00bcc070",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc074`](#insn-00bcc074)

~~~json
{
  "source": "00bcc074",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc078`](#insn-00bcc078)

~~~json
{
  "source": "00bcc078",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc07c`](#insn-00bcc07c)

~~~json
{
  "source": "00bcc07c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc084`](#insn-00bcc084)

~~~json
{
  "source": "00bcc084",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcc088`](#insn-00bcc088)

~~~json
{
  "source": "00bcc088",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc08c`](#insn-00bcc08c)

~~~json
{
  "source": "00bcc08c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc090`](#insn-00bcc090)

~~~json
{
  "source": "00bcc090",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc094`](#insn-00bcc094)

~~~json
{
  "source": "00bcc094",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc0a4`](#insn-00bcc0a4)

~~~json
{
  "source": "00bcc0a4",
  "target": "00bcc038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc0ac`](#insn-00bcc0ac)

~~~json
{
  "source": "00bcc0ac",
  "target": "00c5ade0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
