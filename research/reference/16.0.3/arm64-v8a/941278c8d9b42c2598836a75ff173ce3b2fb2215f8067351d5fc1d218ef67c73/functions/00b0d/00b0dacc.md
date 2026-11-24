# 00b0dacc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b0cad8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0cad8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0070.md#compare-34d2b15601b37544e0a4903cceb978bf)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b0dacc",
  "name": "FUN_00b0dacc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0b85f4f780b7b736025ef6e7358df0edfec5197959f0ebda762e0ee49e03f742",
  "source_text_sha256": "0b85f4f780b7b736025ef6e7358df0edfec5197959f0ebda762e0ee49e03f742",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b0dacc",
        "00b0dadf"
      ]
    ],
    "bytes_sha256": "21759aceb54dc3f5fa96f1b8faa2bf4e8ab5306cc6d667f813d9f6a498ea2b23",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b0a798](../00b0a/00b0a798.md)
- [00b0bf30](../00b0b/00b0bf30.md)

## 呼び出し先

- [0043bad8](../0043b/0043bad8.md)

## 関連文字列（未確認候補）

~~~text
"vector"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 119 bytes

~~~c

void FUN_00b0dacc(void)

{
                    /* WARNING: Subroutine does not return */
  FUN_0043bad8("vector");
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b0dacc"></a> `00b0dacc` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00b0dad0"></a> `00b0dad0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00b0dad4"></a> `00b0dad4` | `40 bd ff f0` | adrp x0,0x2b8000 | `FALL_THROUGH`
<a id="insn-00b0dad8"></a> `00b0dad8` | `00 6c 01 91` | add x0,x0,#0x5b | `FALL_THROUGH`
<a id="insn-00b0dadc"></a> `00b0dadc` | `ff b7 e4 97` | bl 0x0043bad8 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b0dacc`](#insn-00b0dacc) 範囲 `[['00b0dacc', '00b0dadf']]`

## 命令位置別の参照

- [`00b0dacc`](#insn-00b0dacc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dad8`](#insn-00b0dad8) → `002b805b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b0dadc`](#insn-00b0dadc) → [`0043bad8`](../0043b/0043bad8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bad8` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b0dacc`](#insn-00b0dacc)

~~~json
{
  "source": "00b0dacc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dad8`](#insn-00b0dad8)

~~~json
{
  "source": "00b0dad8",
  "target": "002b805b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b805b",
  "offset": 0,
  "size": 7,
  "datatype": "string",
  "bytes": "766563746f7200",
  "capture_start": "002b805b",
  "capture_bytes": 7,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b0dadc`](#insn-00b0dadc)

~~~json
{
  "source": "00b0dadc",
  "target": "0043bad8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
