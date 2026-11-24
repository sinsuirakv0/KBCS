# 00bcbaf4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5c5f4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c5f4.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-4415be2b7432586b80c0e6511044c3c3)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcbf1c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbf1c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-c141c6bcdaeecfd9ce6be8b2429f3873)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbaf4",
  "name": "_ZNSt6__ndk16vectorIPN8firebase4auth4AuthENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7a41c869b94de4fd9d492e9e0ce556bfce6ded56f3d9126a8e33e993b107cb3d",
  "source_text_sha256": "7a41c869b94de4fd9d492e9e0ce556bfce6ded56f3d9126a8e33e993b107cb3d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbaf4",
        "00bcbbeb"
      ]
    ],
    "bytes_sha256": "7b93fae188eac2ac2ff6424caaaa4f9fef84d87d3fc48ea88c82680d9c6ed47c",
    "instruction_count": 62,
    "instruction_bytes": 248,
    "body_bytes": 248,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d710](../00c5d/00c5d710.md)

## 呼び出し先

- [00b3fe98](../00b3f/00b3fe98.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57c00](../00c57/00c57c00.md)
- [00c5a910](../00c5a/00c5a910.md)

## 関連文字列（未確認候補）

~~~text
"allocator<T>::allocate(size_t n) 'n' exceeds maximum supported size"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1757 bytes

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
                    /* catch() { ... } // from try @ 00bcbac4 with catch @ 00bcbb28 */
  if ((ulong)(param_1[2] - (long)__src >> 3) < 0xfffffffffffffff) {
    uVar2 = param_1[2] - (long)__src >> 2;
    if (uVar3 <= uVar2) {
      uVar3 = uVar2;
    }
    if (uVar3 == 0) {
      __dest = (void *)0x0;
      goto LAB_00bcbb74;
    }
                    /* catch() { ... } // from try @ 00bcbb90 with catch @ 00bcbb50 */
    if (uVar3 >> 0x3d != 0) {
                    /* WARNING: Subroutine does not return */
      FUN_00b3fe98("allocator<T>::allocate(size_t n) \'n\' exceeds maximum supported size");
    }
  }
  else {
    uVar3 = 0x1fffffffffffffff;
  }
  __dest = (void *)_Znwm(uVar3 << 3);
LAB_00bcbb74:
  puVar1 = (undefined8 *)((long)__dest + ((long)__n >> 3) * 8);
  *puVar1 = *param_2;
                    /* try { // try from 00bcbb88 to 00ccbb8f has its CatchHandler @ 00bcbc7c */
  if (0 < (long)__n) {
                    /* try { // try from 00bcbb90 to 00ccbca3 has its CatchHandler @ 00bcbb50 */
    memcpy(__dest,__src,__n);
  }
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
<a id="insn-00bcbaf4"></a> `00bcbaf4` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bcbaf8"></a> `00bcbaf8` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbafc"></a> `00bcbafc` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbb00"></a> `00bcbb00` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcbb04"></a> `00bcbb04` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcbb08"></a> `00bcbb08` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bcbb0c"></a> `00bcbb0c` | `14 20 40 a9` | ldp x20,x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcbb10"></a> `00bcbb10` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcbb14"></a> `00bcbb14` | `15 01 14 cb` | sub x21,x8,x20 | `FALL_THROUGH`
<a id="insn-00bcbb18"></a> `00bcbb18` | `b8 fe 43 93` | asr x24,x21,#0x3 | `FALL_THROUGH`
<a id="insn-00bcbb1c"></a> `00bcbb1c` | `08 07 00 91` | add x8,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbb20"></a> `00bcbb20` | `09 fd 7d d3` | lsr x9,x8,#0x3d | `FALL_THROUGH`
<a id="insn-00bcbb24"></a> `00bcbb24` | `09 06 00 b5` | cbnz x9,0x00bcbbe4 | `CONDITIONAL_JUMP`
<a id="insn-00bcbb28"></a> `00bcbb28` | `69 0a 40 f9` | ldr x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbb2c"></a> `00bcbb2c` | `ea eb 7f b2` | orr x10,xzr,#0xffffffffffffffe | `FALL_THROUGH`
<a id="insn-00bcbb30"></a> `00bcbb30` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00bcbb34"></a> `00bcbb34` | `29 01 14 cb` | sub x9,x9,x20 | `FALL_THROUGH`
<a id="insn-00bcbb38"></a> `00bcbb38` | `5f 0d 89 eb` | cmp x10,x9, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00bcbb3c"></a> `00bcbb3c` | `43 01 00 54` | b.cc 0x00bcbb64 | `CONDITIONAL_JUMP`
<a id="insn-00bcbb40"></a> `00bcbb40` | `29 fd 42 93` | asr x9,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bcbb44"></a> `00bcbb44` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcbb48"></a> `00bcbb48` | `19 31 89 9a` | csel x25,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00bcbb4c"></a> `00bcbb4c` | `99 04 00 b4` | cbz x25,0x00bcbbdc | `CONDITIONAL_JUMP`
<a id="insn-00bcbb50"></a> `00bcbb50` | `28 ff 7d d3` | lsr x8,x25,#0x3d | `FALL_THROUGH`
<a id="insn-00bcbb54"></a> `00bcbb54` | `a8 00 00 b4` | cbz x8,0x00bcbb68 | `CONDITIONAL_JUMP`
<a id="insn-00bcbb58"></a> `00bcbb58` | `e0 b6 ff b0` | adrp x0,0x2a8000 | `FALL_THROUGH`
<a id="insn-00bcbb5c"></a> `00bcbb5c` | `00 b8 16 91` | add x0,x0,#0x5ae | `FALL_THROUGH`
<a id="insn-00bcbb60"></a> `00bcbb60` | `ce d0 fd 97` | bl 0x00b3fe98 | `CALL_TERMINATOR`
<a id="insn-00bcbb64"></a> `00bcbb64` | `19 00 fc 92` | mov x25,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bcbb68"></a> `00bcbb68` | `20 f3 7d d3` | lsl x0,x25,#0x3 | `FALL_THROUGH`
<a id="insn-00bcbb6c"></a> `00bcbb6c` | `c9 2f 02 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbb70"></a> `00bcbb70` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bcbb74"></a> `00bcbb74` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bcbb78"></a> `00bcbb78` | `f8 0e 18 8b` | add x24,x23,x24, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bcbb7c"></a> `00bcbb7c` | `f6 0e 19 8b` | add x22,x23,x25, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bcbb80"></a> `00bcbb80` | `bf 06 00 f1` | cmp x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbb84"></a> `00bcbb84` | `08 87 00 f8` | str x8,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-00bcbb88"></a> `00bcbb88` | `ab 00 00 54` | b.lt 0x00bcbb9c | `CONDITIONAL_JUMP`
<a id="insn-00bcbb8c"></a> `00bcbb8c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bcbb90"></a> `00bcbb90` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcbb94"></a> `00bcbb94` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bcbb98"></a> `00bcbb98` | `1a 30 02 94` | bl 0x00c57c00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbb9c"></a> `00bcbb9c` | `77 62 00 a9` | stp x23,x24,[x19] | `FALL_THROUGH`
<a id="insn-00bcbba0"></a> `00bcbba0` | `76 0a 00 f9` | str x22,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbba4"></a> `00bcbba4` | `14 01 00 b4` | cbz x20,0x00bcbbc4 | `CONDITIONAL_JUMP`
<a id="insn-00bcbba8"></a> `00bcbba8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcbbac"></a> `00bcbbac` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcbbb0"></a> `00bcbbb0` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcbbb4"></a> `00bcbbb4` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbbb8"></a> `00bcbbb8` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbbbc"></a> `00bcbbbc` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcbbc0"></a> `00bcbbc0` | `bc 2f 02 14` | b 0x00c57ab0 | `CALL_TERMINATOR`
<a id="insn-00bcbbc4"></a> `00bcbbc4` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcbbc8"></a> `00bcbbc8` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcbbcc"></a> `00bcbbcc` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbbd0"></a> `00bcbbd0` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbbd4"></a> `00bcbbd4` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcbbd8"></a> `00bcbbd8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcbbdc"></a> `00bcbbdc` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00bcbbe0"></a> `00bcbbe0` | `e5 ff ff 17` | b 0x00bcbb74 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcbbe4"></a> `00bcbbe4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcbbe8"></a> `00bcbbe8` | `4a 3b 02 94` | bl 0x00c5a910 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbaf4`](#insn-00bcbaf4) 範囲 `[['00bcbaf4', '00bcbb27']]`
  - `CONDITIONAL_JUMP` [`00bcbb24`](#insn-00bcbb24) → [`00bcbbe4`](#insn-00bcbbe4)
  - `FALL_THROUGH` [`00bcbb24`](#insn-00bcbb24) → [`00bcbb28`](#insn-00bcbb28)
- ブロック [`00bcbb28`](#insn-00bcbb28) 範囲 `[['00bcbb28', '00bcbb3f']]`
  - `CONDITIONAL_JUMP` [`00bcbb3c`](#insn-00bcbb3c) → [`00bcbb64`](#insn-00bcbb64)
  - `FALL_THROUGH` [`00bcbb3c`](#insn-00bcbb3c) → [`00bcbb40`](#insn-00bcbb40)
- ブロック [`00bcbb40`](#insn-00bcbb40) 範囲 `[['00bcbb40', '00bcbb4f']]`
  - `CONDITIONAL_JUMP` [`00bcbb4c`](#insn-00bcbb4c) → [`00bcbbdc`](#insn-00bcbbdc)
  - `FALL_THROUGH` [`00bcbb4c`](#insn-00bcbb4c) → [`00bcbb50`](#insn-00bcbb50)
- ブロック [`00bcbb50`](#insn-00bcbb50) 範囲 `[['00bcbb50', '00bcbb57']]`
  - `CONDITIONAL_JUMP` [`00bcbb54`](#insn-00bcbb54) → [`00bcbb68`](#insn-00bcbb68)
  - `FALL_THROUGH` [`00bcbb54`](#insn-00bcbb54) → [`00bcbb58`](#insn-00bcbb58)
- ブロック [`00bcbb58`](#insn-00bcbb58) 範囲 `[['00bcbb58', '00bcbb63']]`
- ブロック [`00bcbb64`](#insn-00bcbb64) 範囲 `[['00bcbb64', '00bcbb67']]`
  - `FALL_THROUGH` [`00bcbb64`](#insn-00bcbb64) → [`00bcbb68`](#insn-00bcbb68)
- ブロック [`00bcbb68`](#insn-00bcbb68) 範囲 `[['00bcbb68', '00bcbb73']]`
  - `FALL_THROUGH` [`00bcbb70`](#insn-00bcbb70) → [`00bcbb74`](#insn-00bcbb74)
- ブロック [`00bcbb74`](#insn-00bcbb74) 範囲 `[['00bcbb74', '00bcbb87']]`
  - `FALL_THROUGH` [`00bcbb84`](#insn-00bcbb84) → [`00bcbb88`](#insn-00bcbb88)
- ブロック [`00bcbb88`](#insn-00bcbb88) 範囲 `[['00bcbb88', '00bcbb8b']]`
  - `CONDITIONAL_JUMP` [`00bcbb88`](#insn-00bcbb88) → [`00bcbb9c`](#insn-00bcbb9c)
  - `FALL_THROUGH` [`00bcbb88`](#insn-00bcbb88) → [`00bcbb8c`](#insn-00bcbb8c)
- ブロック [`00bcbb8c`](#insn-00bcbb8c) 範囲 `[['00bcbb8c', '00bcbb8f']]`
  - `FALL_THROUGH` [`00bcbb8c`](#insn-00bcbb8c) → [`00bcbb90`](#insn-00bcbb90)
- ブロック [`00bcbb90`](#insn-00bcbb90) 範囲 `[['00bcbb90', '00bcbb9b']]`
  - `FALL_THROUGH` [`00bcbb98`](#insn-00bcbb98) → [`00bcbb9c`](#insn-00bcbb9c)
- ブロック [`00bcbb9c`](#insn-00bcbb9c) 範囲 `[['00bcbb9c', '00bcbba7']]`
  - `CONDITIONAL_JUMP` [`00bcbba4`](#insn-00bcbba4) → [`00bcbbc4`](#insn-00bcbbc4)
  - `FALL_THROUGH` [`00bcbba4`](#insn-00bcbba4) → [`00bcbba8`](#insn-00bcbba8)
- ブロック [`00bcbba8`](#insn-00bcbba8) 範囲 `[['00bcbba8', '00bcbbc3']]`
- ブロック [`00bcbbc4`](#insn-00bcbbc4) 範囲 `[['00bcbbc4', '00bcbbdb']]`
- ブロック [`00bcbbdc`](#insn-00bcbbdc) 範囲 `[['00bcbbdc', '00bcbbe3']]`
  - `UNCONDITIONAL_JUMP` [`00bcbbe0`](#insn-00bcbbe0) → [`00bcbb74`](#insn-00bcbb74)
- ブロック [`00bcbbe4`](#insn-00bcbbe4) 範囲 `[['00bcbbe4', '00bcbbeb']]`

## 命令位置別の参照

- [`00bcbaf4`](#insn-00bcbaf4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbaf8`](#insn-00bcbaf8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbafc`](#insn-00bcbafc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb00`](#insn-00bcbb00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb04`](#insn-00bcbb04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb24`](#insn-00bcbb24) → [`00bcbbe4`](#insn-00bcbbe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb3c`](#insn-00bcbb3c) → [`00bcbb64`](#insn-00bcbb64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb4c`](#insn-00bcbb4c) → [`00bcbbdc`](#insn-00bcbbdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb54`](#insn-00bcbb54) → [`00bcbb68`](#insn-00bcbb68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb5c`](#insn-00bcbb5c) → `002a85ae`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcbb60`](#insn-00bcbb60) → [`00b3fe98`](../00b3f/00b3fe98.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b3fe98` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb6c`](#insn-00bcbb6c) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb88`](#insn-00bcbb88) → [`00bcbb9c`](#insn-00bcbb9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbb98`](#insn-00bcbb98) → [`00c57c00`](../00c57/00c57c00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c00` · 推定シンボル `None` · 推定型 `None`
- [`00bcbba4`](#insn-00bcbba4) → [`00bcbbc4`](#insn-00bcbbc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbac`](#insn-00bcbbac) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbb0`](#insn-00bcbbb0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbb4`](#insn-00bcbbb4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbb8`](#insn-00bcbbb8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbc0`](#insn-00bcbbc0) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbc4`](#insn-00bcbbc4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbc8`](#insn-00bcbbc8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbcc`](#insn-00bcbbcc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbd0`](#insn-00bcbbd0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbe0`](#insn-00bcbbe0) → [`00bcbb74`](#insn-00bcbb74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbe8`](#insn-00bcbbe8) → [`00c5a910`](../00c5a/00c5a910.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a910` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbaf4`](#insn-00bcbaf4)

~~~json
{
  "source": "00bcbaf4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbaf8`](#insn-00bcbaf8)

~~~json
{
  "source": "00bcbaf8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbafc`](#insn-00bcbafc)

~~~json
{
  "source": "00bcbafc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb00`](#insn-00bcbb00)

~~~json
{
  "source": "00bcbb00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb04`](#insn-00bcbb04)

~~~json
{
  "source": "00bcbb04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb24`](#insn-00bcbb24)

~~~json
{
  "source": "00bcbb24",
  "target": "00bcbbe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb3c`](#insn-00bcbb3c)

~~~json
{
  "source": "00bcbb3c",
  "target": "00bcbb64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb4c`](#insn-00bcbb4c)

~~~json
{
  "source": "00bcbb4c",
  "target": "00bcbbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb54`](#insn-00bcbb54)

~~~json
{
  "source": "00bcbb54",
  "target": "00bcbb68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb5c`](#insn-00bcbb5c)

~~~json
{
  "source": "00bcbb5c",
  "target": "002a85ae",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a85ae",
  "offset": 0,
  "size": 68,
  "datatype": "string",
  "bytes": "616c6c6f6361746f723c543e3a3a616c6c6f636174652873697a655f74206e29",
  "capture_start": "002a85ae",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcbb60`](#insn-00bcbb60)

~~~json
{
  "source": "00bcbb60",
  "target": "00b3fe98",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbb6c`](#insn-00bcbb6c)

~~~json
{
  "source": "00bcbb6c",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbb88`](#insn-00bcbb88)

~~~json
{
  "source": "00bcbb88",
  "target": "00bcbb9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbb98`](#insn-00bcbb98)

~~~json
{
  "source": "00bcbb98",
  "target": "00c57c00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbba4`](#insn-00bcbba4)

~~~json
{
  "source": "00bcbba4",
  "target": "00bcbbc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbac`](#insn-00bcbbac)

~~~json
{
  "source": "00bcbbac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbb0`](#insn-00bcbbb0)

~~~json
{
  "source": "00bcbbb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbb4`](#insn-00bcbbb4)

~~~json
{
  "source": "00bcbbb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbb8`](#insn-00bcbbb8)

~~~json
{
  "source": "00bcbbb8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbc0`](#insn-00bcbbc0)

~~~json
{
  "source": "00bcbbc0",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbbc4`](#insn-00bcbbc4)

~~~json
{
  "source": "00bcbbc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbc8`](#insn-00bcbbc8)

~~~json
{
  "source": "00bcbbc8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbcc`](#insn-00bcbbcc)

~~~json
{
  "source": "00bcbbcc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbd0`](#insn-00bcbbd0)

~~~json
{
  "source": "00bcbbd0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbe0`](#insn-00bcbbe0)

~~~json
{
  "source": "00bcbbe0",
  "target": "00bcbb74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbe8`](#insn-00bcbbe8)

~~~json
{
  "source": "00bcbbe8",
  "target": "00c5a910",
  "target_space": "ram",
  "resolution": "function"
}
~~~
