# 00bcb4bc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5bfbc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5bfbc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0004.md#compare-73069c28549269589fbbd3088e62816d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcb8e4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb8e4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-4edee30ea13194311e8b0dc42351f077)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcb4bc",
  "name": "_ZNSt6__ndk16vectorIPN8firebase4auth15IdTokenListenerENS_9allocatorIS4_EEEC2ERKS7_",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7c03bd111398704ff81fd2bfd2c41600877c102be28b57c67687f464d43c3bb9",
  "source_text_sha256": "7c03bd111398704ff81fd2bfd2c41600877c102be28b57c67687f464d43c3bb9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcb4bc",
        "00bcb543"
      ]
    ],
    "bytes_sha256": "81d21f1dbe066671c172e1df6db507b58d3c4ebf260394c0c0166b8e6bb8aef2",
    "instruction_count": 34,
    "instruction_bytes": 136,
    "body_bytes": 136,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d6e0](../00c5d/00c5d6e0.md)

## 呼び出し先

- [00c57a90](../00c57/00c57a90.md)
- [00c57c00](../00c57/00c57c00.md)
- [00c5a910](../00c5a/00c5a910.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 911 bytes

~~~c

void _ZNSt6__ndk16vectorIPN8firebase4auth15IdTokenListenerENS_9allocatorIS4_EEEC2ERKS7_
               (undefined8 *param_1,long *param_2)

{
  void *__dest;
  size_t __n;
  ulong uVar1;
  
                    /* catch() { ... } // from try @ 00bcb6a8 with catch @ 00bcb4cc */
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
<a id="insn-00bcb4bc"></a> `00bcb4bc` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcb4c0"></a> `00bcb4c0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb4c4"></a> `00bcb4c4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcb4c8"></a> `00bcb4c8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcb4cc"></a> `00bcb4cc` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bcb4d0"></a> `00bcb4d0` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb4d4"></a> `00bcb4d4` | `28 24 40 a9` | ldp x8,x9,[x1] | `FALL_THROUGH`
<a id="insn-00bcb4d8"></a> `00bcb4d8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcb4dc"></a> `00bcb4dc` | `20 01 08 eb` | subs x0,x9,x8 | `FALL_THROUGH`
<a id="insn-00bcb4e0"></a> `00bcb4e0` | `60 02 00 54` | b.eq 0x00bcb52c | `CONDITIONAL_JUMP`
<a id="insn-00bcb4e4"></a> `00bcb4e4` | `16 fc 43 93` | asr x22,x0,#0x3 | `FALL_THROUGH`
<a id="insn-00bcb4e8"></a> `00bcb4e8` | `c8 fe 7d d3` | lsr x8,x22,#0x3d | `FALL_THROUGH`
<a id="insn-00bcb4ec"></a> `00bcb4ec` | `88 02 00 b5` | cbnz x8,0x00bcb53c | `CONDITIONAL_JUMP`
<a id="insn-00bcb4f0"></a> `00bcb4f0` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bcb4f4"></a> `00bcb4f4` | `67 31 02 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcb4f8"></a> `00bcb4f8` | `08 0c 16 8b` | add x8,x0,x22, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bcb4fc"></a> `00bcb4fc` | `60 02 00 a9` | stp x0,x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcb500"></a> `00bcb500` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb504"></a> `00bcb504` | `81 22 40 a9` | ldp x1,x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcb508"></a> `00bcb508` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bcb50c"></a> `00bcb50c` | `14 01 01 cb` | sub x20,x8,x1 | `FALL_THROUGH`
<a id="insn-00bcb510"></a> `00bcb510` | `9f 06 00 f1` | cmp x20,#0x1 | `FALL_THROUGH`
<a id="insn-00bcb514"></a> `00bcb514` | `ab 00 00 54` | b.lt 0x00bcb528 | `CONDITIONAL_JUMP`
<a id="insn-00bcb518"></a> `00bcb518` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcb51c"></a> `00bcb51c` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00bcb520"></a> `00bcb520` | `b8 31 02 94` | bl 0x00c57c00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcb524"></a> `00bcb524` | `b5 02 14 8b` | add x21,x21,x20 | `FALL_THROUGH`
<a id="insn-00bcb528"></a> `00bcb528` | `75 06 00 f9` | str x21,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcb52c"></a> `00bcb52c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcb530"></a> `00bcb530` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb534"></a> `00bcb534` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcb538"></a> `00bcb538` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcb53c"></a> `00bcb53c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcb540"></a> `00bcb540` | `f4 3c 02 94` | bl 0x00c5a910 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcb4bc`](#insn-00bcb4bc) 範囲 `[['00bcb4bc', '00bcb4cb']]`
  - `FALL_THROUGH` [`00bcb4c8`](#insn-00bcb4c8) → [`00bcb4cc`](#insn-00bcb4cc)
- ブロック [`00bcb4cc`](#insn-00bcb4cc) 範囲 `[['00bcb4cc', '00bcb4e3']]`
  - `CONDITIONAL_JUMP` [`00bcb4e0`](#insn-00bcb4e0) → [`00bcb52c`](#insn-00bcb52c)
  - `FALL_THROUGH` [`00bcb4e0`](#insn-00bcb4e0) → [`00bcb4e4`](#insn-00bcb4e4)
- ブロック [`00bcb4e4`](#insn-00bcb4e4) 範囲 `[['00bcb4e4', '00bcb4ef']]`
  - `CONDITIONAL_JUMP` [`00bcb4ec`](#insn-00bcb4ec) → [`00bcb53c`](#insn-00bcb53c)
  - `FALL_THROUGH` [`00bcb4ec`](#insn-00bcb4ec) → [`00bcb4f0`](#insn-00bcb4f0)
- ブロック [`00bcb4f0`](#insn-00bcb4f0) 範囲 `[['00bcb4f0', '00bcb517']]`
  - `CONDITIONAL_JUMP` [`00bcb514`](#insn-00bcb514) → [`00bcb528`](#insn-00bcb528)
  - `FALL_THROUGH` [`00bcb514`](#insn-00bcb514) → [`00bcb518`](#insn-00bcb518)
- ブロック [`00bcb518`](#insn-00bcb518) 範囲 `[['00bcb518', '00bcb527']]`
  - `FALL_THROUGH` [`00bcb524`](#insn-00bcb524) → [`00bcb528`](#insn-00bcb528)
- ブロック [`00bcb528`](#insn-00bcb528) 範囲 `[['00bcb528', '00bcb52b']]`
  - `FALL_THROUGH` [`00bcb528`](#insn-00bcb528) → [`00bcb52c`](#insn-00bcb52c)
- ブロック [`00bcb52c`](#insn-00bcb52c) 範囲 `[['00bcb52c', '00bcb53b']]`
- ブロック [`00bcb53c`](#insn-00bcb53c) 範囲 `[['00bcb53c', '00bcb543']]`

## 命令位置別の参照

- [`00bcb4bc`](#insn-00bcb4bc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb4c0`](#insn-00bcb4c0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb4c4`](#insn-00bcb4c4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb4e0`](#insn-00bcb4e0) → [`00bcb52c`](#insn-00bcb52c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb4ec`](#insn-00bcb4ec) → [`00bcb53c`](#insn-00bcb53c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb4f4`](#insn-00bcb4f4) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00bcb514`](#insn-00bcb514) → [`00bcb528`](#insn-00bcb528) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb520`](#insn-00bcb520) → [`00c57c00`](../00c57/00c57c00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c00` · 推定シンボル `None` · 推定型 `None`
- [`00bcb52c`](#insn-00bcb52c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb530`](#insn-00bcb530) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb540`](#insn-00bcb540) → [`00c5a910`](../00c5a/00c5a910.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a910` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcb4bc`](#insn-00bcb4bc)

~~~json
{
  "source": "00bcb4bc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb4c0`](#insn-00bcb4c0)

~~~json
{
  "source": "00bcb4c0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb4c4`](#insn-00bcb4c4)

~~~json
{
  "source": "00bcb4c4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb4e0`](#insn-00bcb4e0)

~~~json
{
  "source": "00bcb4e0",
  "target": "00bcb52c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb4ec`](#insn-00bcb4ec)

~~~json
{
  "source": "00bcb4ec",
  "target": "00bcb53c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb4f4`](#insn-00bcb4f4)

~~~json
{
  "source": "00bcb4f4",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb514`](#insn-00bcb514)

~~~json
{
  "source": "00bcb514",
  "target": "00bcb528",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb520`](#insn-00bcb520)

~~~json
{
  "source": "00bcb520",
  "target": "00c57c00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb52c`](#insn-00bcb52c)

~~~json
{
  "source": "00bcb52c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb530`](#insn-00bcb530)

~~~json
{
  "source": "00bcb530",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb540`](#insn-00bcb540)

~~~json
{
  "source": "00bcb540",
  "target": "00c5a910",
  "target_space": "ram",
  "resolution": "function"
}
~~~
