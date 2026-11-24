# 00bcb6bc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcb294`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb294.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0010.md#compare-392370851c95fc431b893c2b3073f705)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcb758`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcb758.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0011.md#compare-80ceb01c58959475974031d4670fb122)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcb6bc",
  "name": "_ZNSt6__ndk16vectorIPN8firebase4auth17AuthStateListenerENS_9allocatorIS4_EEEC2ERKS7_",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0779a2daaf54dd72b77dd944e32954c1af702e381aaa4afeb1c1c5ee97cdba97",
  "source_text_sha256": "0779a2daaf54dd72b77dd944e32954c1af702e381aaa4afeb1c1c5ee97cdba97",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcb6bc",
        "00bcb743"
      ]
    ],
    "bytes_sha256": "ed6fbdd730cd0e6c2773c2fad34982ec2b29b2fdaab20ceeeac8fdbc6226bf7c",
    "instruction_count": 34,
    "instruction_bytes": 136,
    "body_bytes": 136,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5db00](../00c5d/00c5db00.md)

## 呼び出し先

- [00c57e90](../00c57/00c57e90.md)
- [00c58000](../00c58/00c58000.md)
- [00c5ad10](../00c5a/00c5ad10.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 913 bytes

~~~c

void _ZNSt6__ndk16vectorIPN8firebase4auth17AuthStateListenerENS_9allocatorIS4_EEEC2ERKS7_
               (undefined8 *param_1,long *param_2)

{
  void *__dest;
  size_t __n;
  ulong uVar1;
  
                    /* catch() { ... } // from try @ 00bcb8a4 with catch @ 00bcb6c8 */
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  if (param_2[1] - *param_2 != 0) {
    uVar1 = param_2[1] - *param_2 >> 3;
    if (uVar1 >> 0x3d != 0) {
                    /* WARNING: Subroutine does not return */
      _ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv(param_1);
    }
    __dest = (void *)_Znwm();
    *param_1 = __dest;
    param_1[1] = __dest;
    param_1[2] = (void *)((long)__dest + uVar1 * 8);
    __n = param_2[1] - *param_2;
    if (0 < (long)__n) {
      memcpy(__dest,(void *)*param_2,__n);
      __dest = (void *)((long)__dest + __n);
    }
    param_1[1] = __dest;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcb6bc"></a> `00bcb6bc` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcb6c0"></a> `00bcb6c0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb6c4"></a> `00bcb6c4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcb6c8"></a> `00bcb6c8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcb6cc"></a> `00bcb6cc` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bcb6d0"></a> `00bcb6d0` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb6d4"></a> `00bcb6d4` | `28 24 40 a9` | ldp x8,x9,[x1] | `FALL_THROUGH`
<a id="insn-00bcb6d8"></a> `00bcb6d8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcb6dc"></a> `00bcb6dc` | `20 01 08 eb` | subs x0,x9,x8 | `FALL_THROUGH`
<a id="insn-00bcb6e0"></a> `00bcb6e0` | `60 02 00 54` | b.eq 0x00bcb72c | `CONDITIONAL_JUMP`
<a id="insn-00bcb6e4"></a> `00bcb6e4` | `16 fc 43 93` | asr x22,x0,#0x3 | `FALL_THROUGH`
<a id="insn-00bcb6e8"></a> `00bcb6e8` | `c8 fe 7d d3` | lsr x8,x22,#0x3d | `FALL_THROUGH`
<a id="insn-00bcb6ec"></a> `00bcb6ec` | `88 02 00 b5` | cbnz x8,0x00bcb73c | `CONDITIONAL_JUMP`
<a id="insn-00bcb6f0"></a> `00bcb6f0` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bcb6f4"></a> `00bcb6f4` | `e7 31 02 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcb6f8"></a> `00bcb6f8` | `08 0c 16 8b` | add x8,x0,x22, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bcb6fc"></a> `00bcb6fc` | `60 02 00 a9` | stp x0,x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcb700"></a> `00bcb700` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb704"></a> `00bcb704` | `81 22 40 a9` | ldp x1,x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcb708"></a> `00bcb708` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bcb70c"></a> `00bcb70c` | `14 01 01 cb` | sub x20,x8,x1 | `FALL_THROUGH`
<a id="insn-00bcb710"></a> `00bcb710` | `9f 06 00 f1` | cmp x20,#0x1 | `FALL_THROUGH`
<a id="insn-00bcb714"></a> `00bcb714` | `ab 00 00 54` | b.lt 0x00bcb728 | `CONDITIONAL_JUMP`
<a id="insn-00bcb718"></a> `00bcb718` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcb71c"></a> `00bcb71c` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00bcb720"></a> `00bcb720` | `38 32 02 94` | bl 0x00c58000 | `UNCONDITIONAL_CALL`
<a id="insn-00bcb724"></a> `00bcb724` | `b5 02 14 8b` | add x21,x21,x20 | `FALL_THROUGH`
<a id="insn-00bcb728"></a> `00bcb728` | `75 06 00 f9` | str x21,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcb72c"></a> `00bcb72c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcb730"></a> `00bcb730` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb734"></a> `00bcb734` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcb738"></a> `00bcb738` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcb73c"></a> `00bcb73c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcb740"></a> `00bcb740` | `74 3d 02 94` | bl 0x00c5ad10 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcb6bc`](#insn-00bcb6bc) 範囲 `[['00bcb6bc', '00bcb6c7']]`
  - `FALL_THROUGH` [`00bcb6c4`](#insn-00bcb6c4) → [`00bcb6c8`](#insn-00bcb6c8)
- ブロック [`00bcb6c8`](#insn-00bcb6c8) 範囲 `[['00bcb6c8', '00bcb6e3']]`
  - `CONDITIONAL_JUMP` [`00bcb6e0`](#insn-00bcb6e0) → [`00bcb72c`](#insn-00bcb72c)
  - `FALL_THROUGH` [`00bcb6e0`](#insn-00bcb6e0) → [`00bcb6e4`](#insn-00bcb6e4)
- ブロック [`00bcb6e4`](#insn-00bcb6e4) 範囲 `[['00bcb6e4', '00bcb6ef']]`
  - `CONDITIONAL_JUMP` [`00bcb6ec`](#insn-00bcb6ec) → [`00bcb73c`](#insn-00bcb73c)
  - `FALL_THROUGH` [`00bcb6ec`](#insn-00bcb6ec) → [`00bcb6f0`](#insn-00bcb6f0)
- ブロック [`00bcb6f0`](#insn-00bcb6f0) 範囲 `[['00bcb6f0', '00bcb717']]`
  - `CONDITIONAL_JUMP` [`00bcb714`](#insn-00bcb714) → [`00bcb728`](#insn-00bcb728)
  - `FALL_THROUGH` [`00bcb714`](#insn-00bcb714) → [`00bcb718`](#insn-00bcb718)
- ブロック [`00bcb718`](#insn-00bcb718) 範囲 `[['00bcb718', '00bcb727']]`
  - `FALL_THROUGH` [`00bcb724`](#insn-00bcb724) → [`00bcb728`](#insn-00bcb728)
- ブロック [`00bcb728`](#insn-00bcb728) 範囲 `[['00bcb728', '00bcb72b']]`
  - `FALL_THROUGH` [`00bcb728`](#insn-00bcb728) → [`00bcb72c`](#insn-00bcb72c)
- ブロック [`00bcb72c`](#insn-00bcb72c) 範囲 `[['00bcb72c', '00bcb73b']]`
- ブロック [`00bcb73c`](#insn-00bcb73c) 範囲 `[['00bcb73c', '00bcb743']]`

## 命令位置別の参照

- [`00bcb6bc`](#insn-00bcb6bc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb6c0`](#insn-00bcb6c0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb6c4`](#insn-00bcb6c4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb6e0`](#insn-00bcb6e0) → [`00bcb72c`](#insn-00bcb72c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb6ec`](#insn-00bcb6ec) → [`00bcb73c`](#insn-00bcb73c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb6f4`](#insn-00bcb6f4) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bcb714`](#insn-00bcb714) → [`00bcb728`](#insn-00bcb728) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb720`](#insn-00bcb720) → [`00c58000`](../00c58/00c58000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58000` · 推定シンボル `None` · 推定型 `None`
- [`00bcb72c`](#insn-00bcb72c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb730`](#insn-00bcb730) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb740`](#insn-00bcb740) → [`00c5ad10`](../00c5a/00c5ad10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad10` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcb6bc`](#insn-00bcb6bc)

~~~json
{
  "source": "00bcb6bc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb6c0`](#insn-00bcb6c0)

~~~json
{
  "source": "00bcb6c0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb6c4`](#insn-00bcb6c4)

~~~json
{
  "source": "00bcb6c4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb6e0`](#insn-00bcb6e0)

~~~json
{
  "source": "00bcb6e0",
  "target": "00bcb72c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb6ec`](#insn-00bcb6ec)

~~~json
{
  "source": "00bcb6ec",
  "target": "00bcb73c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb6f4`](#insn-00bcb6f4)

~~~json
{
  "source": "00bcb6f4",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb714`](#insn-00bcb714)

~~~json
{
  "source": "00bcb714",
  "target": "00bcb728",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb720`](#insn-00bcb720)

~~~json
{
  "source": "00bcb720",
  "target": "00c58000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb72c`](#insn-00bcb72c)

~~~json
{
  "source": "00bcb72c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb730`](#insn-00bcb730)

~~~json
{
  "source": "00bcb730",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb740`](#insn-00bcb740)

~~~json
{
  "source": "00bcb740",
  "target": "00c5ad10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
