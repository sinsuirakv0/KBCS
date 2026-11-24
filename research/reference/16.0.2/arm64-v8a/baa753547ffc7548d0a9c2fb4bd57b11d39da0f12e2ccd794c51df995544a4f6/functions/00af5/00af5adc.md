# 00af5adc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00af5a40`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5a40.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0006.md#compare-5dc792e1b91e3b42e4d62630d0c8cd5a)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00af6ad0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af6/00af6ad0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0012.md#compare-bb5ab9e06ca3b66045e236966d2111ae)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af5adc",
  "name": "FUN_00af5adc",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bf5c6f45d3f23b425cd13b0dff714383757b85c01177c35587f4fc9f9f95288b",
  "source_text_sha256": "bf5c6f45d3f23b425cd13b0dff714383757b85c01177c35587f4fc9f9f95288b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af5adc",
        "00af5b2f"
      ]
    ],
    "bytes_sha256": "bd523e74f47936594d18042bad1d96940825f3d27ddf0610d5948f7e9c1e4aad",
    "instruction_count": 21,
    "instruction_bytes": 84,
    "body_bytes": 84,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0070eab4](../0070e/0070eab4.md)
- [00710330](../00710/00710330.md)
- [00711a48](../00711/00711a48.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1020 bytes

~~~c

void FUN_00af5adc(int param_1,int param_2,int param_3)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00af596c with catch @ 00af5adc */
  lVar1 = FUN_00851550();
                    /* try { // try from 00af5b08 to 00bf5bc7 has its CatchHandler @ 00af5b08
                       catch() { ... } // from try @ 00af5b08 with catch @ 00af5b08
                       catch() { ... } // from try @ 00af5c28 with catch @ 00af5b08
                       catch() { ... } // from try @ 00af5cd8 with catch @ 00af5b08
                       catch() { ... } // from try @ 00af5d7c with catch @ 00af5b08
                       catch() { ... } // from try @ 00af5f18 with catch @ 00af5b08
                       catch() { ... } // from try @ 00af6048 with catch @ 00af5b08
                       catch() { ... } // from try @ 00af6124 with catch @ 00af5b08 */
  lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar1 + 0x84c68) = *(int *)(lVar1 + 0x84c68) + param_3;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af5adc"></a> `00af5adc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00af5ae0"></a> `00af5ae0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af5ae4"></a> `00af5ae4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af5ae8"></a> `00af5ae8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00af5aec"></a> `00af5aec` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00af5af0"></a> `00af5af0` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00af5af4"></a> `00af5af4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00af5af8"></a> `00af5af8` | `96 6e f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00af5afc"></a> `00af5afc` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af5b00"></a> `00af5b00` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af5b04"></a> `00af5b04` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00af5b08"></a> `00af5b08` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00af5b0c"></a> `00af5b0c` | `09 8d 89 52` | mov w9,#0x4c68 | `FALL_THROUGH`
<a id="insn-00af5b10"></a> `00af5b10` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af5b14"></a> `00af5b14` | `0a 69 69 b8` | ldr w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af5b18"></a> `00af5b18` | `4a 01 13 0b` | add w10,w10,w19 | `FALL_THROUGH`
<a id="insn-00af5b1c"></a> `00af5b1c` | `0a 69 29 b8` | str w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af5b20"></a> `00af5b20` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af5b24"></a> `00af5b24` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af5b28"></a> `00af5b28` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00af5b2c"></a> `00af5b2c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af5adc`](#insn-00af5adc) 範囲 `[['00af5adc', '00af5b07']]`
  - `FALL_THROUGH` [`00af5b04`](#insn-00af5b04) → [`00af5b08`](#insn-00af5b08)
- ブロック [`00af5b08`](#insn-00af5b08) 範囲 `[['00af5b08', '00af5b2f']]`

## 命令位置別の参照

- [`00af5adc`](#insn-00af5adc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5ae0`](#insn-00af5ae0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5ae4`](#insn-00af5ae4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5af8`](#insn-00af5af8) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00af5b20`](#insn-00af5b20) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5b24`](#insn-00af5b24) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5b28`](#insn-00af5b28) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af5adc`](#insn-00af5adc)

~~~json
{
  "source": "00af5adc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5ae0`](#insn-00af5ae0)

~~~json
{
  "source": "00af5ae0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5ae4`](#insn-00af5ae4)

~~~json
{
  "source": "00af5ae4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5af8`](#insn-00af5af8)

~~~json
{
  "source": "00af5af8",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af5b20`](#insn-00af5b20)

~~~json
{
  "source": "00af5b20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5b24`](#insn-00af5b24)

~~~json
{
  "source": "00af5b24",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5b28`](#insn-00af5b28)

~~~json
{
  "source": "00af5b28",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
