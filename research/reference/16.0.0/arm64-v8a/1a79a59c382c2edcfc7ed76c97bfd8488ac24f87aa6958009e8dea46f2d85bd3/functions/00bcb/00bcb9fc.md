# 00bcb9fc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5c4fc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c4fc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0017.md#compare-c5188e6527cdf756f60e964f27e6cfde)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcbe24`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcbe24.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-cf481b0f2940fa11b79ad596c81950a9)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcb9fc",
  "name": "_ZNSt6__ndk16vectorIPN8firebase4auth17AuthStateListenerENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "06de6ac1902b25c066493372b9f37d084eb308a6c80f0323521ccb4d698ba5da",
  "source_text_sha256": "06de6ac1902b25c066493372b9f37d084eb308a6c80f0323521ccb4d698ba5da",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcb9fc",
        "00bcbaf3"
      ]
    ],
    "bytes_sha256": "d4919dfa56e033d1dd3c8da79d708da8b49c93356f6b69e7e0e9f0c453632ceb",
    "instruction_count": 62,
    "instruction_bytes": 248,
    "body_bytes": 248,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d6f0](../00c5d/00c5d6f0.md)

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

## 疑似コード / UTF-8 1949 bytes

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
  uVar3 = ((long)__n >> 3) + 1;
  if (uVar3 >> 0x3d != 0) {
                    /* WARNING: Subroutine does not return */
    _ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv(param_1);
  }
                    /* catch() { ... } // from try @ 00bcb9cc with catch @ 00bcba30 */
  if ((ulong)(param_1[2] - (long)__src >> 3) < 0xfffffffffffffff) {
    uVar2 = param_1[2] - (long)__src >> 2;
    if (uVar3 <= uVar2) {
      uVar3 = uVar2;
    }
    if (uVar3 == 0) {
      __dest = (void *)0x0;
      goto LAB_00bcba7c;
    }
                    /* try { // try from 00bcba58 to 00ccbac3 has its CatchHandler @ 00bcba58
                       catch() { ... } // from try @ 00bcba58 with catch @ 00bcba58
                       catch() { ... } // from try @ 00bcbad0 with catch @ 00bcba58 */
    if (uVar3 >> 0x3d != 0) {
                    /* WARNING: Subroutine does not return */
      FUN_00b3fe98("allocator<T>::allocate(size_t n) \'n\' exceeds maximum supported size");
    }
  }
  else {
    uVar3 = 0x1fffffffffffffff;
  }
  __dest = (void *)_Znwm(uVar3 << 3);
LAB_00bcba7c:
  puVar1 = (undefined8 *)((long)__dest + ((long)__n >> 3) * 8);
  *puVar1 = *param_2;
  if (0 < (long)__n) {
    memcpy(__dest,__src,__n);
  }
  *param_1 = __dest;
  param_1[1] = puVar1 + 1;
  param_1[2] = (void *)((long)__dest + uVar3 * 8);
  if (__src != (void *)0x0) {
                    /* try { // try from 00bcbac4 to 00ccbacf has its CatchHandler @ 00bcbb28 */
    _ZdlPv(__src);
    return;
  }
                    /* try { // try from 00bcbad0 to 00ccbb4f has its CatchHandler @ 00bcba58 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcb9fc"></a> `00bcb9fc` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bcba00"></a> `00bcba00` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcba04"></a> `00bcba04` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcba08"></a> `00bcba08` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcba0c"></a> `00bcba0c` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcba10"></a> `00bcba10` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bcba14"></a> `00bcba14` | `14 20 40 a9` | ldp x20,x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcba18"></a> `00bcba18` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcba1c"></a> `00bcba1c` | `15 01 14 cb` | sub x21,x8,x20 | `FALL_THROUGH`
<a id="insn-00bcba20"></a> `00bcba20` | `b8 fe 43 93` | asr x24,x21,#0x3 | `FALL_THROUGH`
<a id="insn-00bcba24"></a> `00bcba24` | `08 07 00 91` | add x8,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00bcba28"></a> `00bcba28` | `09 fd 7d d3` | lsr x9,x8,#0x3d | `FALL_THROUGH`
<a id="insn-00bcba2c"></a> `00bcba2c` | `09 06 00 b5` | cbnz x9,0x00bcbaec | `CONDITIONAL_JUMP`
<a id="insn-00bcba30"></a> `00bcba30` | `69 0a 40 f9` | ldr x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcba34"></a> `00bcba34` | `ea eb 7f b2` | orr x10,xzr,#0xffffffffffffffe | `FALL_THROUGH`
<a id="insn-00bcba38"></a> `00bcba38` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00bcba3c"></a> `00bcba3c` | `29 01 14 cb` | sub x9,x9,x20 | `FALL_THROUGH`
<a id="insn-00bcba40"></a> `00bcba40` | `5f 0d 89 eb` | cmp x10,x9, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00bcba44"></a> `00bcba44` | `43 01 00 54` | b.cc 0x00bcba6c | `CONDITIONAL_JUMP`
<a id="insn-00bcba48"></a> `00bcba48` | `29 fd 42 93` | asr x9,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bcba4c"></a> `00bcba4c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcba50"></a> `00bcba50` | `19 31 89 9a` | csel x25,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00bcba54"></a> `00bcba54` | `99 04 00 b4` | cbz x25,0x00bcbae4 | `CONDITIONAL_JUMP`
<a id="insn-00bcba58"></a> `00bcba58` | `28 ff 7d d3` | lsr x8,x25,#0x3d | `FALL_THROUGH`
<a id="insn-00bcba5c"></a> `00bcba5c` | `a8 00 00 b4` | cbz x8,0x00bcba70 | `CONDITIONAL_JUMP`
<a id="insn-00bcba60"></a> `00bcba60` | `e0 b6 ff b0` | adrp x0,0x2a8000 | `FALL_THROUGH`
<a id="insn-00bcba64"></a> `00bcba64` | `00 b8 16 91` | add x0,x0,#0x5ae | `FALL_THROUGH`
<a id="insn-00bcba68"></a> `00bcba68` | `0c d1 fd 97` | bl 0x00b3fe98 | `CALL_TERMINATOR`
<a id="insn-00bcba6c"></a> `00bcba6c` | `19 00 fc 92` | mov x25,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bcba70"></a> `00bcba70` | `20 f3 7d d3` | lsl x0,x25,#0x3 | `FALL_THROUGH`
<a id="insn-00bcba74"></a> `00bcba74` | `07 30 02 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcba78"></a> `00bcba78` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bcba7c"></a> `00bcba7c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bcba80"></a> `00bcba80` | `f8 0e 18 8b` | add x24,x23,x24, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bcba84"></a> `00bcba84` | `f6 0e 19 8b` | add x22,x23,x25, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bcba88"></a> `00bcba88` | `bf 06 00 f1` | cmp x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bcba8c"></a> `00bcba8c` | `08 87 00 f8` | str x8,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-00bcba90"></a> `00bcba90` | `ab 00 00 54` | b.lt 0x00bcbaa4 | `CONDITIONAL_JUMP`
<a id="insn-00bcba94"></a> `00bcba94` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bcba98"></a> `00bcba98` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcba9c"></a> `00bcba9c` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bcbaa0"></a> `00bcbaa0` | `58 30 02 94` | bl 0x00c57c00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbaa4"></a> `00bcbaa4` | `77 62 00 a9` | stp x23,x24,[x19] | `FALL_THROUGH`
<a id="insn-00bcbaa8"></a> `00bcbaa8` | `76 0a 00 f9` | str x22,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbaac"></a> `00bcbaac` | `14 01 00 b4` | cbz x20,0x00bcbacc | `CONDITIONAL_JUMP`
<a id="insn-00bcbab0"></a> `00bcbab0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcbab4"></a> `00bcbab4` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcbab8"></a> `00bcbab8` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcbabc"></a> `00bcbabc` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbac0"></a> `00bcbac0` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbac4"></a> `00bcbac4` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcbac8"></a> `00bcbac8` | `fa 2f 02 14` | b 0x00c57ab0 | `CALL_TERMINATOR`
<a id="insn-00bcbacc"></a> `00bcbacc` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcbad0"></a> `00bcbad0` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcbad4"></a> `00bcbad4` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbad8"></a> `00bcbad8` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbadc"></a> `00bcbadc` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcbae0"></a> `00bcbae0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcbae4"></a> `00bcbae4` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00bcbae8"></a> `00bcbae8` | `e5 ff ff 17` | b 0x00bcba7c | `UNCONDITIONAL_JUMP`
<a id="insn-00bcbaec"></a> `00bcbaec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcbaf0"></a> `00bcbaf0` | `88 3b 02 94` | bl 0x00c5a910 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcb9fc`](#insn-00bcb9fc) 範囲 `[['00bcb9fc', '00bcba2f']]`
  - `CONDITIONAL_JUMP` [`00bcba2c`](#insn-00bcba2c) → [`00bcbaec`](#insn-00bcbaec)
  - `FALL_THROUGH` [`00bcba2c`](#insn-00bcba2c) → [`00bcba30`](#insn-00bcba30)
- ブロック [`00bcba30`](#insn-00bcba30) 範囲 `[['00bcba30', '00bcba47']]`
  - `CONDITIONAL_JUMP` [`00bcba44`](#insn-00bcba44) → [`00bcba6c`](#insn-00bcba6c)
  - `FALL_THROUGH` [`00bcba44`](#insn-00bcba44) → [`00bcba48`](#insn-00bcba48)
- ブロック [`00bcba48`](#insn-00bcba48) 範囲 `[['00bcba48', '00bcba57']]`
  - `CONDITIONAL_JUMP` [`00bcba54`](#insn-00bcba54) → [`00bcbae4`](#insn-00bcbae4)
  - `FALL_THROUGH` [`00bcba54`](#insn-00bcba54) → [`00bcba58`](#insn-00bcba58)
- ブロック [`00bcba58`](#insn-00bcba58) 範囲 `[['00bcba58', '00bcba5f']]`
  - `CONDITIONAL_JUMP` [`00bcba5c`](#insn-00bcba5c) → [`00bcba70`](#insn-00bcba70)
  - `FALL_THROUGH` [`00bcba5c`](#insn-00bcba5c) → [`00bcba60`](#insn-00bcba60)
- ブロック [`00bcba60`](#insn-00bcba60) 範囲 `[['00bcba60', '00bcba6b']]`
- ブロック [`00bcba6c`](#insn-00bcba6c) 範囲 `[['00bcba6c', '00bcba6f']]`
  - `FALL_THROUGH` [`00bcba6c`](#insn-00bcba6c) → [`00bcba70`](#insn-00bcba70)
- ブロック [`00bcba70`](#insn-00bcba70) 範囲 `[['00bcba70', '00bcba7b']]`
  - `FALL_THROUGH` [`00bcba78`](#insn-00bcba78) → [`00bcba7c`](#insn-00bcba7c)
- ブロック [`00bcba7c`](#insn-00bcba7c) 範囲 `[['00bcba7c', '00bcba93']]`
  - `CONDITIONAL_JUMP` [`00bcba90`](#insn-00bcba90) → [`00bcbaa4`](#insn-00bcbaa4)
  - `FALL_THROUGH` [`00bcba90`](#insn-00bcba90) → [`00bcba94`](#insn-00bcba94)
- ブロック [`00bcba94`](#insn-00bcba94) 範囲 `[['00bcba94', '00bcbaa3']]`
  - `FALL_THROUGH` [`00bcbaa0`](#insn-00bcbaa0) → [`00bcbaa4`](#insn-00bcbaa4)
- ブロック [`00bcbaa4`](#insn-00bcbaa4) 範囲 `[['00bcbaa4', '00bcbaaf']]`
  - `CONDITIONAL_JUMP` [`00bcbaac`](#insn-00bcbaac) → [`00bcbacc`](#insn-00bcbacc)
  - `FALL_THROUGH` [`00bcbaac`](#insn-00bcbaac) → [`00bcbab0`](#insn-00bcbab0)
- ブロック [`00bcbab0`](#insn-00bcbab0) 範囲 `[['00bcbab0', '00bcbac3']]`
  - `FALL_THROUGH` [`00bcbac0`](#insn-00bcbac0) → [`00bcbac4`](#insn-00bcbac4)
- ブロック [`00bcbac4`](#insn-00bcbac4) 範囲 `[['00bcbac4', '00bcbacb']]`
- ブロック [`00bcbacc`](#insn-00bcbacc) 範囲 `[['00bcbacc', '00bcbacf']]`
  - `FALL_THROUGH` [`00bcbacc`](#insn-00bcbacc) → [`00bcbad0`](#insn-00bcbad0)
- ブロック [`00bcbad0`](#insn-00bcbad0) 範囲 `[['00bcbad0', '00bcbae3']]`
- ブロック [`00bcbae4`](#insn-00bcbae4) 範囲 `[['00bcbae4', '00bcbaeb']]`
  - `UNCONDITIONAL_JUMP` [`00bcbae8`](#insn-00bcbae8) → [`00bcba7c`](#insn-00bcba7c)
- ブロック [`00bcbaec`](#insn-00bcbaec) 範囲 `[['00bcbaec', '00bcbaf3']]`

## 命令位置別の参照

- [`00bcb9fc`](#insn-00bcb9fc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcba00`](#insn-00bcba00) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcba04`](#insn-00bcba04) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcba08`](#insn-00bcba08) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcba0c`](#insn-00bcba0c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcba2c`](#insn-00bcba2c) → [`00bcbaec`](#insn-00bcbaec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcba44`](#insn-00bcba44) → [`00bcba6c`](#insn-00bcba6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcba54`](#insn-00bcba54) → [`00bcbae4`](#insn-00bcbae4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcba5c`](#insn-00bcba5c) → [`00bcba70`](#insn-00bcba70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcba64`](#insn-00bcba64) → `002a85ae`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcba68`](#insn-00bcba68) → [`00b3fe98`](../00b3f/00b3fe98.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b3fe98` · 推定シンボル `None` · 推定型 `None`
- [`00bcba74`](#insn-00bcba74) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00bcba90`](#insn-00bcba90) → [`00bcbaa4`](#insn-00bcbaa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbaa0`](#insn-00bcbaa0) → [`00c57c00`](../00c57/00c57c00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c00` · 推定シンボル `None` · 推定型 `None`
- [`00bcbaac`](#insn-00bcbaac) → [`00bcbacc`](#insn-00bcbacc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbab4`](#insn-00bcbab4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbab8`](#insn-00bcbab8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbabc`](#insn-00bcbabc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbac0`](#insn-00bcbac0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbac8`](#insn-00bcbac8) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbacc`](#insn-00bcbacc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbad0`](#insn-00bcbad0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbad4`](#insn-00bcbad4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbad8`](#insn-00bcbad8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbae8`](#insn-00bcbae8) → [`00bcba7c`](#insn-00bcba7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbaf0`](#insn-00bcbaf0) → [`00c5a910`](../00c5a/00c5a910.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a910` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcb9fc`](#insn-00bcb9fc)

~~~json
{
  "source": "00bcb9fc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcba00`](#insn-00bcba00)

~~~json
{
  "source": "00bcba00",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcba04`](#insn-00bcba04)

~~~json
{
  "source": "00bcba04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcba08`](#insn-00bcba08)

~~~json
{
  "source": "00bcba08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcba0c`](#insn-00bcba0c)

~~~json
{
  "source": "00bcba0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcba2c`](#insn-00bcba2c)

~~~json
{
  "source": "00bcba2c",
  "target": "00bcbaec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcba44`](#insn-00bcba44)

~~~json
{
  "source": "00bcba44",
  "target": "00bcba6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcba54`](#insn-00bcba54)

~~~json
{
  "source": "00bcba54",
  "target": "00bcbae4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcba5c`](#insn-00bcba5c)

~~~json
{
  "source": "00bcba5c",
  "target": "00bcba70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcba64`](#insn-00bcba64)

~~~json
{
  "source": "00bcba64",
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
- 参照命令 [`00bcba68`](#insn-00bcba68)

~~~json
{
  "source": "00bcba68",
  "target": "00b3fe98",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcba74`](#insn-00bcba74)

~~~json
{
  "source": "00bcba74",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcba90`](#insn-00bcba90)

~~~json
{
  "source": "00bcba90",
  "target": "00bcbaa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbaa0`](#insn-00bcbaa0)

~~~json
{
  "source": "00bcbaa0",
  "target": "00c57c00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbaac`](#insn-00bcbaac)

~~~json
{
  "source": "00bcbaac",
  "target": "00bcbacc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbab4`](#insn-00bcbab4)

~~~json
{
  "source": "00bcbab4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbab8`](#insn-00bcbab8)

~~~json
{
  "source": "00bcbab8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbabc`](#insn-00bcbabc)

~~~json
{
  "source": "00bcbabc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbac0`](#insn-00bcbac0)

~~~json
{
  "source": "00bcbac0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbac8`](#insn-00bcbac8)

~~~json
{
  "source": "00bcbac8",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbacc`](#insn-00bcbacc)

~~~json
{
  "source": "00bcbacc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbad0`](#insn-00bcbad0)

~~~json
{
  "source": "00bcbad0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbad4`](#insn-00bcbad4)

~~~json
{
  "source": "00bcbad4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbad8`](#insn-00bcbad8)

~~~json
{
  "source": "00bcbad8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbae8`](#insn-00bcbae8)

~~~json
{
  "source": "00bcbae8",
  "target": "00bcba7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbaf0`](#insn-00bcbaf0)

~~~json
{
  "source": "00bcbaf0",
  "target": "00c5a910",
  "target_space": "ram",
  "resolution": "function"
}
~~~
