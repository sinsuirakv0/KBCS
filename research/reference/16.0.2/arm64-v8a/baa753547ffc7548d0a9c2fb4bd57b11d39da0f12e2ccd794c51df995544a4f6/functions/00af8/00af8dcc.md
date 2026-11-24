# 00af8dcc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00af8d30`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af8/00af8d30.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0006.md#compare-480eca74efcbeb19bb0d3d41f63b4426)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00af9dc0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af9/00af9dc0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0012.md#compare-4903b19651bb39da14046a89d737166e)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af8dcc",
  "name": "FUN_00af8dcc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7bebeffcaa2f4a72a75a48a85c0bcccc9f16152c6db36a92acb5e244b1db8256",
  "source_text_sha256": "7bebeffcaa2f4a72a75a48a85c0bcccc9f16152c6db36a92acb5e244b1db8256",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af8dcc",
        "00af8e17"
      ]
    ],
    "bytes_sha256": "afccb51c846f03b6a0fedce4d2952f474a39d2c41dde532094204c800d36dc33",
    "instruction_count": 19,
    "instruction_bytes": 76,
    "body_bytes": 76,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a4f424](../00a4f/00a4f424.md)
- [00af3590](../00af3/00af3590.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 411 bytes

~~~c

void FUN_00af8dcc(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
                    /* try { // try from 00af8e00 to 00bf8e03 has its CatchHandler @ 00af9224 */
                    /* try { // try from 00af8e04 to 00bf8e6b has its CatchHandler @ 00af8d00 */
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84990) = param_3;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af8dcc"></a> `00af8dcc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00af8dd0"></a> `00af8dd0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af8dd4"></a> `00af8dd4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af8dd8"></a> `00af8dd8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00af8ddc"></a> `00af8ddc` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00af8de0"></a> `00af8de0` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00af8de4"></a> `00af8de4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00af8de8"></a> `00af8de8` | `da 61 f5 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00af8dec"></a> `00af8dec` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af8df0"></a> `00af8df0` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af8df4"></a> `00af8df4` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00af8df8"></a> `00af8df8` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00af8dfc"></a> `00af8dfc` | `09 32 89 52` | mov w9,#0x4990 | `FALL_THROUGH`
<a id="insn-00af8e00"></a> `00af8e00` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af8e04"></a> `00af8e04` | `13 69 29 b8` | str w19,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af8e08"></a> `00af8e08` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af8e0c"></a> `00af8e0c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af8e10"></a> `00af8e10` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00af8e14"></a> `00af8e14` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af8dcc`](#insn-00af8dcc) 範囲 `[['00af8dcc', '00af8dff']]`
  - `FALL_THROUGH` [`00af8dfc`](#insn-00af8dfc) → [`00af8e00`](#insn-00af8e00)
- ブロック [`00af8e00`](#insn-00af8e00) 範囲 `[['00af8e00', '00af8e03']]`
  - `FALL_THROUGH` [`00af8e00`](#insn-00af8e00) → [`00af8e04`](#insn-00af8e04)
- ブロック [`00af8e04`](#insn-00af8e04) 範囲 `[['00af8e04', '00af8e17']]`

## 命令位置別の参照

- [`00af8dcc`](#insn-00af8dcc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af8dd0`](#insn-00af8dd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af8dd4`](#insn-00af8dd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af8de8`](#insn-00af8de8) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00af8e08`](#insn-00af8e08) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af8e0c`](#insn-00af8e0c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af8e10`](#insn-00af8e10) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af8dcc`](#insn-00af8dcc)

~~~json
{
  "source": "00af8dcc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af8dd0`](#insn-00af8dd0)

~~~json
{
  "source": "00af8dd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af8dd4`](#insn-00af8dd4)

~~~json
{
  "source": "00af8dd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af8de8`](#insn-00af8de8)

~~~json
{
  "source": "00af8de8",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af8e08`](#insn-00af8e08)

~~~json
{
  "source": "00af8e08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af8e0c`](#insn-00af8e0c)

~~~json
{
  "source": "00af8e0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af8e10`](#insn-00af8e10)

~~~json
{
  "source": "00af8e10",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
