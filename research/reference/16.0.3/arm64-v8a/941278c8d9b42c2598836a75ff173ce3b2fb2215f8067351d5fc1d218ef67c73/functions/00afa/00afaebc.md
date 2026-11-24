# 00afaebc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00af9ec8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9ec8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0012.md#compare-5719abef2ac7c56a952e2c3416c30c3f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afaebc",
  "name": "FUN_00afaebc",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "320c2ea425f59d224fc88c94bd1286f5fdf336962d7774b1b4ad3351ab356a1a",
  "source_text_sha256": "320c2ea425f59d224fc88c94bd1286f5fdf336962d7774b1b4ad3351ab356a1a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afaebc",
        "00afaf2b"
      ]
    ],
    "bytes_sha256": "dd9862e3ce168d18d24e897859fb34c0c27ab27d69d53d9553a5343d14620ed8",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a50418](../00a50/00a50418.md)

## 呼び出し先

- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1537 bytes

~~~c

void FUN_00afaebc(int param_1,int param_2,uint param_3)

{
  long lVar1;
  ulong uVar2;
  
  lVar1 = FUN_008524fc();
                    /* try { // try from 00afaee0 to 00bfafd3 has its CatchHandler @ 00afaee0
                       catch() { ... } // from try @ 00afaee0 with catch @ 00afaee0
                       catch() { ... } // from try @ 00afaffc with catch @ 00afaee0
                       catch() { ... } // from try @ 00afb080 with catch @ 00afaee0
                       catch() { ... } // from try @ 00afb0d0 with catch @ 00afaee0
                       catch() { ... } // from try @ 00afb244 with catch @ 00afaee0
                       catch() { ... } // from try @ 00afb2ec with catch @ 00afaee0
                       catch() { ... } // from try @ 00afb33c with catch @ 00afaee0
                       catch() { ... } // from try @ 00afb404 with catch @ 00afaee0
                       catch() { ... } // from try @ 00afb4e0 with catch @ 00afaee0
                       catch() { ... } // from try @ 00afb610 with catch @ 00afaee0
                       catch() { ... } // from try @ 00afb6dc with catch @ 00afaee0
                       catch() { ... } // from try @ 00afb820 with catch @ 00afaee0
                       catch() { ... } // from try @ 00afb8ec with catch @ 00afaee0 */
  uVar2 = FUN_005e7810(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) != 0) {
    lVar1 = FUN_008524fc();
    *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b0c) = param_3 & 1;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afaebc"></a> `00afaebc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afaec0"></a> `00afaec0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afaec4"></a> `00afaec4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afaec8"></a> `00afaec8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afaecc"></a> `00afaecc` | `f4 03 02 2a` | mov w20,w2 | `FALL_THROUGH`
<a id="insn-00afaed0"></a> `00afaed0` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afaed4"></a> `00afaed4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00afaed8"></a> `00afaed8` | `89 5d f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afaedc"></a> `00afaedc` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afaee0"></a> `00afaee0` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afaee4"></a> `00afaee4` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afaee8"></a> `00afaee8` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afaeec"></a> `00afaeec` | `49 b2 eb 97` | bl 0x005e7810 | `UNCONDITIONAL_CALL`
<a id="insn-00afaef0"></a> `00afaef0` | `60 01 00 36` | tbz w0,#0x0,0x00afaf1c | `CONDITIONAL_JUMP`
<a id="insn-00afaef4"></a> `00afaef4` | `b5 7e 40 93` | sxtw x21,w21 | `FALL_THROUGH`
<a id="insn-00afaef8"></a> `00afaef8` | `94 02 00 12` | and w20,w20,#0x1 | `FALL_THROUGH`
<a id="insn-00afaefc"></a> `00afaefc` | `80 5d f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afaf00"></a> `00afaf00` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afaf04"></a> `00afaf04` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afaf08"></a> `00afaf08` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afaf0c"></a> `00afaf0c` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afaf10"></a> `00afaf10` | `89 61 89 52` | mov w9,#0x4b0c | `FALL_THROUGH`
<a id="insn-00afaf14"></a> `00afaf14` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afaf18"></a> `00afaf18` | `14 69 29 b8` | str w20,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afaf1c"></a> `00afaf1c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afaf20"></a> `00afaf20` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afaf24"></a> `00afaf24` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afaf28"></a> `00afaf28` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afaebc`](#insn-00afaebc) 範囲 `[['00afaebc', '00afaedf']]`
  - `FALL_THROUGH` [`00afaedc`](#insn-00afaedc) → [`00afaee0`](#insn-00afaee0)
- ブロック [`00afaee0`](#insn-00afaee0) 範囲 `[['00afaee0', '00afaef3']]`
  - `CONDITIONAL_JUMP` [`00afaef0`](#insn-00afaef0) → [`00afaf1c`](#insn-00afaf1c)
  - `FALL_THROUGH` [`00afaef0`](#insn-00afaef0) → [`00afaef4`](#insn-00afaef4)
- ブロック [`00afaef4`](#insn-00afaef4) 範囲 `[['00afaef4', '00afaf1b']]`
  - `FALL_THROUGH` [`00afaf18`](#insn-00afaf18) → [`00afaf1c`](#insn-00afaf1c)
- ブロック [`00afaf1c`](#insn-00afaf1c) 範囲 `[['00afaf1c', '00afaf2b']]`

## 命令位置別の参照

- [`00afaebc`](#insn-00afaebc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaec0`](#insn-00afaec0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaec4`](#insn-00afaec4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaed8`](#insn-00afaed8) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afaeec`](#insn-00afaeec) → [`005e7810`](../005e7/005e7810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7810` · 推定シンボル `None` · 推定型 `None`
- [`00afaef0`](#insn-00afaef0) → [`00afaf1c`](#insn-00afaf1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaefc`](#insn-00afaefc) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afaf1c`](#insn-00afaf1c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf20`](#insn-00afaf20) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf24`](#insn-00afaf24) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afaebc`](#insn-00afaebc)

~~~json
{
  "source": "00afaebc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaec0`](#insn-00afaec0)

~~~json
{
  "source": "00afaec0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaec4`](#insn-00afaec4)

~~~json
{
  "source": "00afaec4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaed8`](#insn-00afaed8)

~~~json
{
  "source": "00afaed8",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaeec`](#insn-00afaeec)

~~~json
{
  "source": "00afaeec",
  "target": "005e7810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaef0`](#insn-00afaef0)

~~~json
{
  "source": "00afaef0",
  "target": "00afaf1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaefc`](#insn-00afaefc)

~~~json
{
  "source": "00afaefc",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaf1c`](#insn-00afaf1c)

~~~json
{
  "source": "00afaf1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf20`](#insn-00afaf20)

~~~json
{
  "source": "00afaf20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf24`](#insn-00afaf24)

~~~json
{
  "source": "00afaf24",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
