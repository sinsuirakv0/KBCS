# 00bd0dbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd0d20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0d20.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0082.md#compare-0e39edd4bec5bb93bd04e5d797db7bee)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bd1db0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd1/00bd1db0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0082.md#compare-9f011896c6b95aa3eb6a69254b8281ab)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd0dbc",
  "name": "_ZN8firebase4auth20additional_user_info10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "226858018ad0edb158a39eea0630294f444949ef8e58d1286a938f09bad5b0ff",
  "source_text_sha256": "226858018ad0edb158a39eea0630294f444949ef8e58d1286a938f09bad5b0ff",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd0dbc",
        "00bd0df7"
      ]
    ],
    "bytes_sha256": "981d492029ca10521bc6e0e77b22c8e7a7d27467f508634bd6afa09c2c71ae5e",
    "instruction_count": 15,
    "instruction_bytes": 60,
    "body_bytes": 60,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5b0d0](../00c5b/00c5b0d0.md)

## 関連文字列（未確認候補）

~~~text
"field < kFieldCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 244 bytes

~~~c

undefined8 _ZN8firebase4auth20additional_user_info10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_011269a0 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd0dbc"></a> `00bd0dbc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd0dc0"></a> `00bd0dc0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd0dc4"></a> `00bd0dc4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd0dc8"></a> `00bd0dc8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bd0dcc"></a> `00bd0dcc` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bd0dd0"></a> `00bd0dd0` | `8b 00 00 54` | b.lt 0x00bd0de0 | `CONDITIONAL_JUMP`
<a id="insn-00bd0dd4"></a> `00bd0dd4` | `c0 b6 ff b0` | adrp x0,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bd0dd8"></a> `00bd0dd8` | `00 34 15 91` | add x0,x0,#0x54d | `FALL_THROUGH`
<a id="insn-00bd0ddc"></a> `00bd0ddc` | `bd 28 02 94` | bl 0x00c5b0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd0de0"></a> `00bd0de0` | `a8 2a 00 d0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd0de4"></a> `00bd0de4` | `08 81 26 91` | add x8,x8,#0x9a0 | `FALL_THROUGH`
<a id="insn-00bd0de8"></a> `00bd0de8` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bd0dec"></a> `00bd0dec` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd0df0"></a> `00bd0df0` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd0df4"></a> `00bd0df4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd0dbc`](#insn-00bd0dbc) 範囲 `[['00bd0dbc', '00bd0dd3']]`
  - `CONDITIONAL_JUMP` [`00bd0dd0`](#insn-00bd0dd0) → [`00bd0de0`](#insn-00bd0de0)
  - `FALL_THROUGH` [`00bd0dd0`](#insn-00bd0dd0) → [`00bd0dd4`](#insn-00bd0dd4)
- ブロック [`00bd0dd4`](#insn-00bd0dd4) 範囲 `[['00bd0dd4', '00bd0ddf']]`
  - `FALL_THROUGH` [`00bd0ddc`](#insn-00bd0ddc) → [`00bd0de0`](#insn-00bd0de0)
- ブロック [`00bd0de0`](#insn-00bd0de0) 範囲 `[['00bd0de0', '00bd0df7']]`

## 命令位置別の参照

- [`00bd0dbc`](#insn-00bd0dbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0dc0`](#insn-00bd0dc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0dd0`](#insn-00bd0dd0) → [`00bd0de0`](#insn-00bd0de0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0dd8`](#insn-00bd0dd8) → `002a954d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd0ddc`](#insn-00bd0ddc) → [`00c5b0d0`](../00c5b/00c5b0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bd0de8`](#insn-00bd0de8) → `011269a0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0dec`](#insn-00bd0dec) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd0dbc`](#insn-00bd0dbc)

~~~json
{
  "source": "00bd0dbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0dc0`](#insn-00bd0dc0)

~~~json
{
  "source": "00bd0dc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0dd0`](#insn-00bd0dd0)

~~~json
{
  "source": "00bd0dd0",
  "target": "00bd0de0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0dd8`](#insn-00bd0dd8)

~~~json
{
  "source": "00bd0dd8",
  "target": "002a954d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a954d",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6669656c64203c206b4669656c64436f756e7400",
  "capture_start": "002a954d",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bd0ddc`](#insn-00bd0ddc)

~~~json
{
  "source": "00bd0ddc",
  "target": "00c5b0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd0de8`](#insn-00bd0de8)

~~~json
{
  "source": "00bd0de8",
  "target": "011269a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0dec`](#insn-00bd0dec)

~~~json
{
  "source": "00bd0dec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
