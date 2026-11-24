# 00afabf8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afab5c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afab5c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0006.md#compare-cbaf6c512f918d5921c3a8701d21b481)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00afbbec`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00afb/00afbbec.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0013.md#compare-515f3eabea85c5ea5d208fc8a0c8c5d8)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afabf8",
  "name": "FUN_00afabf8",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aa148c940043701189718dee88172aca95e88d4c911a84a666867c3593926668",
  "source_text_sha256": "aa148c940043701189718dee88172aca95e88d4c911a84a666867c3593926668",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afabf8",
        "00afac3f"
      ]
    ],
    "bytes_sha256": "20fb0cbd68c7be4815199ef8d6eb4b139ac764463a959b532d290602e32057cb",
    "instruction_count": 18,
    "instruction_bytes": 72,
    "body_bytes": 72,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00710330](../00710/00710330.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 952 bytes

~~~c

bool FUN_00afabf8(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
                    /* try { // try from 00afac20 to 00bfacbb has its CatchHandler @ 00afac20
                       catch() { ... } // from try @ 00afac20 with catch @ 00afac20
                       catch() { ... } // from try @ 00afacd4 with catch @ 00afac20
                       catch() { ... } // from try @ 00afad94 with catch @ 00afac20
                       catch() { ... } // from try @ 00afae60 with catch @ 00afac20
                       catch() { ... } // from try @ 00afaffc with catch @ 00afac20
                       catch() { ... } // from try @ 00afb04c with catch @ 00afac20
                       catch() { ... } // from try @ 00afb0f8 with catch @ 00afac20
                       catch() { ... } // from try @ 00afb1d4 with catch @ 00afac20 */
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a28) != 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afabf8"></a> `00afabf8` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afabfc"></a> `00afabfc` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afac00"></a> `00afac00` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afac04"></a> `00afac04` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afac08"></a> `00afac08` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afac0c"></a> `00afac0c` | `51 5a f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00afac10"></a> `00afac10` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afac14"></a> `00afac14` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afac18"></a> `00afac18` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afac1c"></a> `00afac1c` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afac20"></a> `00afac20` | `09 45 89 52` | mov w9,#0x4a28 | `FALL_THROUGH`
<a id="insn-00afac24"></a> `00afac24` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afac28"></a> `00afac28` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afac2c"></a> `00afac2c` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00afac30"></a> `00afac30` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00afac34"></a> `00afac34` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afac38"></a> `00afac38` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afac3c"></a> `00afac3c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afabf8`](#insn-00afabf8) 範囲 `[['00afabf8', '00afac1f']]`
  - `FALL_THROUGH` [`00afac1c`](#insn-00afac1c) → [`00afac20`](#insn-00afac20)
- ブロック [`00afac20`](#insn-00afac20) 範囲 `[['00afac20', '00afac3f']]`

## 命令位置別の参照

- [`00afabf8`](#insn-00afabf8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afabfc`](#insn-00afabfc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac0c`](#insn-00afac0c) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00afac34`](#insn-00afac34) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac38`](#insn-00afac38) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afabf8`](#insn-00afabf8)

~~~json
{
  "source": "00afabf8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afabfc`](#insn-00afabfc)

~~~json
{
  "source": "00afabfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac0c`](#insn-00afac0c)

~~~json
{
  "source": "00afac0c",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afac34`](#insn-00afac34)

~~~json
{
  "source": "00afac34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac38`](#insn-00afac38)

~~~json
{
  "source": "00afac38",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
