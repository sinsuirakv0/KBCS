# 00bccfac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcbfb8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbfb8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-f555eacc3f3fa939ec604e07b5ff5cfc)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bccfac",
  "name": "_ZNSt6__ndk16vectorIPN8firebase4auth4AuthENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5cb2969490938d6531d05e92d364eeb10000ab02afe3702566f54ef965b2e771",
  "source_text_sha256": "5cb2969490938d6531d05e92d364eeb10000ab02afe3702566f54ef965b2e771",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bccfac",
        "00bcd0a3"
      ]
    ],
    "bytes_sha256": "b25aae652c1bc87e3e417f71304d1386c927247fc5ae9a86a893c6e621c7c149",
    "instruction_count": 62,
    "instruction_bytes": 248,
    "body_bytes": 248,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5ebb0](../00c5e/00c5ebb0.md)

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
                    /* try { // try from 00bccff0 to 00cccffb has its CatchHandler @ 00bcd054 */
  if ((ulong)(param_1[2] - (long)__src >> 3) < 0xfffffffffffffff) {
    uVar2 = param_1[2] - (long)__src >> 2;
                    /* try { // try from 00bccffc to 00ccd07b has its CatchHandler @ 00bccf90 */
    if (uVar3 <= uVar2) {
      uVar3 = uVar2;
    }
    if (uVar3 == 0) {
      __dest = (void *)0x0;
      goto LAB_00bcd02c;
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
LAB_00bcd02c:
  puVar1 = (undefined8 *)((long)__dest + ((long)__n >> 3) * 8);
  *puVar1 = *param_2;
  if (0 < (long)__n) {
    memcpy(__dest,__src,__n);
  }
                    /* catch() { ... } // from try @ 00bccff0 with catch @ 00bcd054 */
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
<a id="insn-00bccfac"></a> `00bccfac` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bccfb0"></a> `00bccfb0` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccfb4"></a> `00bccfb4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bccfb8"></a> `00bccfb8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bccfbc"></a> `00bccfbc` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bccfc0"></a> `00bccfc0` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bccfc4"></a> `00bccfc4` | `14 20 40 a9` | ldp x20,x8,[x0] | `FALL_THROUGH`
<a id="insn-00bccfc8"></a> `00bccfc8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bccfcc"></a> `00bccfcc` | `15 01 14 cb` | sub x21,x8,x20 | `FALL_THROUGH`
<a id="insn-00bccfd0"></a> `00bccfd0` | `b8 fe 43 93` | asr x24,x21,#0x3 | `FALL_THROUGH`
<a id="insn-00bccfd4"></a> `00bccfd4` | `08 07 00 91` | add x8,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00bccfd8"></a> `00bccfd8` | `09 fd 7d d3` | lsr x9,x8,#0x3d | `FALL_THROUGH`
<a id="insn-00bccfdc"></a> `00bccfdc` | `09 06 00 b5` | cbnz x9,0x00bcd09c | `CONDITIONAL_JUMP`
<a id="insn-00bccfe0"></a> `00bccfe0` | `69 0a 40 f9` | ldr x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bccfe4"></a> `00bccfe4` | `ea eb 7f b2` | orr x10,xzr,#0xffffffffffffffe | `FALL_THROUGH`
<a id="insn-00bccfe8"></a> `00bccfe8` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00bccfec"></a> `00bccfec` | `29 01 14 cb` | sub x9,x9,x20 | `FALL_THROUGH`
<a id="insn-00bccff0"></a> `00bccff0` | `5f 0d 89 eb` | cmp x10,x9, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00bccff4"></a> `00bccff4` | `43 01 00 54` | b.cc 0x00bcd01c | `CONDITIONAL_JUMP`
<a id="insn-00bccff8"></a> `00bccff8` | `29 fd 42 93` | asr x9,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bccffc"></a> `00bccffc` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcd000"></a> `00bcd000` | `19 31 89 9a` | csel x25,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00bcd004"></a> `00bcd004` | `99 04 00 b4` | cbz x25,0x00bcd094 | `CONDITIONAL_JUMP`
<a id="insn-00bcd008"></a> `00bcd008` | `28 ff 7d d3` | lsr x8,x25,#0x3d | `FALL_THROUGH`
<a id="insn-00bcd00c"></a> `00bcd00c` | `a8 00 00 b4` | cbz x8,0x00bcd020 | `CONDITIONAL_JUMP`
<a id="insn-00bcd010"></a> `00bcd010` | `c0 b6 ff f0` | adrp x0,0x2a8000 | `FALL_THROUGH`
<a id="insn-00bcd014"></a> `00bcd014` | `00 dc 1d 91` | add x0,x0,#0x777 | `FALL_THROUGH`
<a id="insn-00bcd018"></a> `00bcd018` | `ce d0 fd 97` | bl 0x00b41350 | `CALL_TERMINATOR`
<a id="insn-00bcd01c"></a> `00bcd01c` | `19 00 fc 92` | mov x25,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bcd020"></a> `00bcd020` | `20 f3 7d d3` | lsl x0,x25,#0x3 | `FALL_THROUGH`
<a id="insn-00bcd024"></a> `00bcd024` | `c3 2f 02 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00bcd028"></a> `00bcd028` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bcd02c"></a> `00bcd02c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bcd030"></a> `00bcd030` | `f8 0e 18 8b` | add x24,x23,x24, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bcd034"></a> `00bcd034` | `f6 0e 19 8b` | add x22,x23,x25, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bcd038"></a> `00bcd038` | `bf 06 00 f1` | cmp x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bcd03c"></a> `00bcd03c` | `08 87 00 f8` | str x8,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-00bcd040"></a> `00bcd040` | `ab 00 00 54` | b.lt 0x00bcd054 | `CONDITIONAL_JUMP`
<a id="insn-00bcd044"></a> `00bcd044` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bcd048"></a> `00bcd048` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcd04c"></a> `00bcd04c` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bcd050"></a> `00bcd050` | `14 30 02 94` | bl 0x00c590a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcd054"></a> `00bcd054` | `77 62 00 a9` | stp x23,x24,[x19] | `FALL_THROUGH`
<a id="insn-00bcd058"></a> `00bcd058` | `76 0a 00 f9` | str x22,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcd05c"></a> `00bcd05c` | `14 01 00 b4` | cbz x20,0x00bcd07c | `CONDITIONAL_JUMP`
<a id="insn-00bcd060"></a> `00bcd060` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcd064"></a> `00bcd064` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcd068"></a> `00bcd068` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcd06c"></a> `00bcd06c` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcd070"></a> `00bcd070` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcd074"></a> `00bcd074` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcd078"></a> `00bcd078` | `b6 2f 02 14` | b 0x00c58f50 | `CALL_TERMINATOR`
<a id="insn-00bcd07c"></a> `00bcd07c` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcd080"></a> `00bcd080` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcd084"></a> `00bcd084` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcd088"></a> `00bcd088` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcd08c"></a> `00bcd08c` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcd090"></a> `00bcd090` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcd094"></a> `00bcd094` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00bcd098"></a> `00bcd098` | `e5 ff ff 17` | b 0x00bcd02c | `UNCONDITIONAL_JUMP`
<a id="insn-00bcd09c"></a> `00bcd09c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcd0a0"></a> `00bcd0a0` | `44 3b 02 94` | bl 0x00c5bdb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bccfac`](#insn-00bccfac) 範囲 `[['00bccfac', '00bccfdf']]`
  - `CONDITIONAL_JUMP` [`00bccfdc`](#insn-00bccfdc) → [`00bcd09c`](#insn-00bcd09c)
  - `FALL_THROUGH` [`00bccfdc`](#insn-00bccfdc) → [`00bccfe0`](#insn-00bccfe0)
- ブロック [`00bccfe0`](#insn-00bccfe0) 範囲 `[['00bccfe0', '00bccfef']]`
  - `FALL_THROUGH` [`00bccfec`](#insn-00bccfec) → [`00bccff0`](#insn-00bccff0)
- ブロック [`00bccff0`](#insn-00bccff0) 範囲 `[['00bccff0', '00bccff7']]`
  - `CONDITIONAL_JUMP` [`00bccff4`](#insn-00bccff4) → [`00bcd01c`](#insn-00bcd01c)
  - `FALL_THROUGH` [`00bccff4`](#insn-00bccff4) → [`00bccff8`](#insn-00bccff8)
- ブロック [`00bccff8`](#insn-00bccff8) 範囲 `[['00bccff8', '00bccffb']]`
  - `FALL_THROUGH` [`00bccff8`](#insn-00bccff8) → [`00bccffc`](#insn-00bccffc)
- ブロック [`00bccffc`](#insn-00bccffc) 範囲 `[['00bccffc', '00bcd007']]`
  - `CONDITIONAL_JUMP` [`00bcd004`](#insn-00bcd004) → [`00bcd094`](#insn-00bcd094)
  - `FALL_THROUGH` [`00bcd004`](#insn-00bcd004) → [`00bcd008`](#insn-00bcd008)
- ブロック [`00bcd008`](#insn-00bcd008) 範囲 `[['00bcd008', '00bcd00f']]`
  - `CONDITIONAL_JUMP` [`00bcd00c`](#insn-00bcd00c) → [`00bcd020`](#insn-00bcd020)
  - `FALL_THROUGH` [`00bcd00c`](#insn-00bcd00c) → [`00bcd010`](#insn-00bcd010)
- ブロック [`00bcd010`](#insn-00bcd010) 範囲 `[['00bcd010', '00bcd01b']]`
- ブロック [`00bcd01c`](#insn-00bcd01c) 範囲 `[['00bcd01c', '00bcd01f']]`
  - `FALL_THROUGH` [`00bcd01c`](#insn-00bcd01c) → [`00bcd020`](#insn-00bcd020)
- ブロック [`00bcd020`](#insn-00bcd020) 範囲 `[['00bcd020', '00bcd02b']]`
  - `FALL_THROUGH` [`00bcd028`](#insn-00bcd028) → [`00bcd02c`](#insn-00bcd02c)
- ブロック [`00bcd02c`](#insn-00bcd02c) 範囲 `[['00bcd02c', '00bcd043']]`
  - `CONDITIONAL_JUMP` [`00bcd040`](#insn-00bcd040) → [`00bcd054`](#insn-00bcd054)
  - `FALL_THROUGH` [`00bcd040`](#insn-00bcd040) → [`00bcd044`](#insn-00bcd044)
- ブロック [`00bcd044`](#insn-00bcd044) 範囲 `[['00bcd044', '00bcd053']]`
  - `FALL_THROUGH` [`00bcd050`](#insn-00bcd050) → [`00bcd054`](#insn-00bcd054)
- ブロック [`00bcd054`](#insn-00bcd054) 範囲 `[['00bcd054', '00bcd05f']]`
  - `CONDITIONAL_JUMP` [`00bcd05c`](#insn-00bcd05c) → [`00bcd07c`](#insn-00bcd07c)
  - `FALL_THROUGH` [`00bcd05c`](#insn-00bcd05c) → [`00bcd060`](#insn-00bcd060)
- ブロック [`00bcd060`](#insn-00bcd060) 範囲 `[['00bcd060', '00bcd07b']]`
- ブロック [`00bcd07c`](#insn-00bcd07c) 範囲 `[['00bcd07c', '00bcd093']]`
- ブロック [`00bcd094`](#insn-00bcd094) 範囲 `[['00bcd094', '00bcd09b']]`
  - `UNCONDITIONAL_JUMP` [`00bcd098`](#insn-00bcd098) → [`00bcd02c`](#insn-00bcd02c)
- ブロック [`00bcd09c`](#insn-00bcd09c) 範囲 `[['00bcd09c', '00bcd0a3']]`

## 命令位置別の参照

- [`00bccfac`](#insn-00bccfac) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccfb0`](#insn-00bccfb0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccfb4`](#insn-00bccfb4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccfb8`](#insn-00bccfb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccfbc`](#insn-00bccfbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccfdc`](#insn-00bccfdc) → [`00bcd09c`](#insn-00bcd09c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccff4`](#insn-00bccff4) → [`00bcd01c`](#insn-00bcd01c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd004`](#insn-00bcd004) → [`00bcd094`](#insn-00bcd094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd00c`](#insn-00bcd00c) → [`00bcd020`](#insn-00bcd020) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd014`](#insn-00bcd014) → `002a8777`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcd018`](#insn-00bcd018) → [`00b41350`](../00b41/00b41350.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b41350` · 推定シンボル `None` · 推定型 `None`
- [`00bcd024`](#insn-00bcd024) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00bcd040`](#insn-00bcd040) → [`00bcd054`](#insn-00bcd054) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd050`](#insn-00bcd050) → [`00c590a0`](../00c59/00c590a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590a0` · 推定シンボル `None` · 推定型 `None`
- [`00bcd05c`](#insn-00bcd05c) → [`00bcd07c`](#insn-00bcd07c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd064`](#insn-00bcd064) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd068`](#insn-00bcd068) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd06c`](#insn-00bcd06c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd070`](#insn-00bcd070) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd078`](#insn-00bcd078) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bcd07c`](#insn-00bcd07c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd080`](#insn-00bcd080) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd084`](#insn-00bcd084) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd088`](#insn-00bcd088) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd098`](#insn-00bcd098) → [`00bcd02c`](#insn-00bcd02c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd0a0`](#insn-00bcd0a0) → [`00c5bdb0`](../00c5b/00c5bdb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bdb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bccfac`](#insn-00bccfac)

~~~json
{
  "source": "00bccfac",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccfb0`](#insn-00bccfb0)

~~~json
{
  "source": "00bccfb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccfb4`](#insn-00bccfb4)

~~~json
{
  "source": "00bccfb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccfb8`](#insn-00bccfb8)

~~~json
{
  "source": "00bccfb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccfbc`](#insn-00bccfbc)

~~~json
{
  "source": "00bccfbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccfdc`](#insn-00bccfdc)

~~~json
{
  "source": "00bccfdc",
  "target": "00bcd09c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccff4`](#insn-00bccff4)

~~~json
{
  "source": "00bccff4",
  "target": "00bcd01c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd004`](#insn-00bcd004)

~~~json
{
  "source": "00bcd004",
  "target": "00bcd094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd00c`](#insn-00bcd00c)

~~~json
{
  "source": "00bcd00c",
  "target": "00bcd020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd014`](#insn-00bcd014)

~~~json
{
  "source": "00bcd014",
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
- 参照命令 [`00bcd018`](#insn-00bcd018)

~~~json
{
  "source": "00bcd018",
  "target": "00b41350",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd024`](#insn-00bcd024)

~~~json
{
  "source": "00bcd024",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd040`](#insn-00bcd040)

~~~json
{
  "source": "00bcd040",
  "target": "00bcd054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd050`](#insn-00bcd050)

~~~json
{
  "source": "00bcd050",
  "target": "00c590a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd05c`](#insn-00bcd05c)

~~~json
{
  "source": "00bcd05c",
  "target": "00bcd07c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd064`](#insn-00bcd064)

~~~json
{
  "source": "00bcd064",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd068`](#insn-00bcd068)

~~~json
{
  "source": "00bcd068",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd06c`](#insn-00bcd06c)

~~~json
{
  "source": "00bcd06c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd070`](#insn-00bcd070)

~~~json
{
  "source": "00bcd070",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd078`](#insn-00bcd078)

~~~json
{
  "source": "00bcd078",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd07c`](#insn-00bcd07c)

~~~json
{
  "source": "00bcd07c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd080`](#insn-00bcd080)

~~~json
{
  "source": "00bcd080",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd084`](#insn-00bcd084)

~~~json
{
  "source": "00bcd084",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd088`](#insn-00bcd088)

~~~json
{
  "source": "00bcd088",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd098`](#insn-00bcd098)

~~~json
{
  "source": "00bcd098",
  "target": "00bcd02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd0a0`](#insn-00bcd0a0)

~~~json
{
  "source": "00bcd0a0",
  "target": "00c5bdb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
