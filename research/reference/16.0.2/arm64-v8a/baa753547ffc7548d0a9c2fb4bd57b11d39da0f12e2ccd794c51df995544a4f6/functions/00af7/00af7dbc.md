# 00af7dbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00af7d20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7d20.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0066.md#compare-ddbedaef24d9c5c335944b08efd9a82c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00af8db0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af8/00af8db0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0012.md#compare-a9f68434ade9d17ea418988cc35b94b3)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af7dbc",
  "name": "FUN_00af7dbc",
  "size": 96,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "31571def2ecc362beedbf796c7cea50489db9c560fad7041b5f134bf7d51ff89",
  "source_text_sha256": "31571def2ecc362beedbf796c7cea50489db9c560fad7041b5f134bf7d51ff89",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af7dbc",
        "00af7e1b"
      ]
    ],
    "bytes_sha256": "004ad2b9bcaa731110dda6ed2d5457a6719fd4ffabe1eb6b780a9c06fcd3bf28",
    "instruction_count": 24,
    "instruction_bytes": 96,
    "body_bytes": 96,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a4f424](../00a4f/00a4f424.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 278 bytes

~~~c

void FUN_00af7dbc(int param_1,int param_2,int param_3,undefined4 param_4)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
  *(undefined4 *)
   (lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + (long)(int)(&DAT_0030a3e4)[param_3] * 4
   + 0x848c8) = param_4;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af7dbc"></a> `00af7dbc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00af7dc0"></a> `00af7dc0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af7dc4"></a> `00af7dc4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af7dc8"></a> `00af7dc8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00af7dcc"></a> `00af7dcc` | `f3 03 03 2a` | mov w19,w3 | `FALL_THROUGH`
<a id="insn-00af7dd0"></a> `00af7dd0` | `f4 03 02 2a` | mov w20,w2 | `FALL_THROUGH`
<a id="insn-00af7dd4"></a> `00af7dd4` | `f5 03 01 2a` | mov w21,w1 | `FALL_THROUGH`
<a id="insn-00af7dd8"></a> `00af7dd8` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00af7ddc"></a> `00af7ddc` | `dd 65 f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00af7de0"></a> `00af7de0` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af7de4"></a> `00af7de4` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af7de8"></a> `00af7de8` | `c8 02 28 9b` | smaddl x8,w22,w8,x0 | `FALL_THROUGH`
<a id="insn-00af7dec"></a> `00af7dec` | `a8 22 29 9b` | smaddl x8,w21,w9,x8 | `FALL_THROUGH`
<a id="insn-00af7df0"></a> `00af7df0` | `89 c0 ff f0` | adrp x9,0x30a000 | `FALL_THROUGH`
<a id="insn-00af7df4"></a> `00af7df4` | `29 91 0f 91` | add x9,x9,#0x3e4 | `FALL_THROUGH`
<a id="insn-00af7df8"></a> `00af7df8` | `29 d9 b4 b8` | ldrsw x9,[x9, w20, SXTW #0x2] | `FALL_THROUGH`
<a id="insn-00af7dfc"></a> `00af7dfc` | `08 09 09 8b` | add x8,x8,x9, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00af7e00"></a> `00af7e00` | `09 19 89 52` | mov w9,#0x48c8 | `FALL_THROUGH`
<a id="insn-00af7e04"></a> `00af7e04` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af7e08"></a> `00af7e08` | `13 69 29 b8` | str w19,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af7e0c"></a> `00af7e0c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af7e10"></a> `00af7e10` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af7e14"></a> `00af7e14` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00af7e18"></a> `00af7e18` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af7dbc`](#insn-00af7dbc) 範囲 `[['00af7dbc', '00af7e1b']]`

## 命令位置別の参照

- [`00af7dbc`](#insn-00af7dbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7dc0`](#insn-00af7dc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7dc4`](#insn-00af7dc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7ddc`](#insn-00af7ddc) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00af7df8`](#insn-00af7df8) → `0030a3e4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00af7e0c`](#insn-00af7e0c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7e10`](#insn-00af7e10) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7e14`](#insn-00af7e14) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af7dbc`](#insn-00af7dbc)

~~~json
{
  "source": "00af7dbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7dc0`](#insn-00af7dc0)

~~~json
{
  "source": "00af7dc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7dc4`](#insn-00af7dc4)

~~~json
{
  "source": "00af7dc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7ddc`](#insn-00af7ddc)

~~~json
{
  "source": "00af7ddc",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af7df8`](#insn-00af7df8)

~~~json
{
  "source": "00af7df8",
  "target": "0030a3e4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030a3e4",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "bytes": "55000000",
  "capture_start": "0030a3e4",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00af7e0c`](#insn-00af7e0c)

~~~json
{
  "source": "00af7e0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7e10`](#insn-00af7e10)

~~~json
{
  "source": "00af7e10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7e14`](#insn-00af7e14)

~~~json
{
  "source": "00af7e14",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
