# 00bd6bbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd6b20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd6b20.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0084.md#compare-1a2b5c81ae8509d59dfb074997f1b075)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bd7bb0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7bb0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0084.md#compare-f4b647904f88ee5e32c9451909434d37)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd6bbc",
  "name": "_ZN8firebase4auth8timeunit11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a55b0ae92dcdee3b6d7447d23a4ef9772c382ef655349cb88473c8064bbe2be9",
  "source_text_sha256": "a55b0ae92dcdee3b6d7447d23a4ef9772c382ef655349cb88473c8064bbe2be9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd6bbc",
        "00bd6bf7"
      ]
    ],
    "bytes_sha256": "1b274508497a40353f325534f536f6a3b53d1bd8ac307162cbc2fda908c9ab49",
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
"method < kMethodCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 235 bytes

~~~c

undefined8 _ZN8firebase4auth8timeunit11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return *(undefined8 *)(&DAT_01126c68 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd6bbc"></a> `00bd6bbc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd6bc0"></a> `00bd6bc0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd6bc4"></a> `00bd6bc4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd6bc8"></a> `00bd6bc8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bd6bcc"></a> `00bd6bcc` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bd6bd0"></a> `00bd6bd0` | `8b 00 00 54` | b.lt 0x00bd6be0 | `CONDITIONAL_JUMP`
<a id="insn-00bd6bd4"></a> `00bd6bd4` | `80 b6 ff d0` | adrp x0,0x2a8000 | `FALL_THROUGH`
<a id="insn-00bd6bd8"></a> `00bd6bd8` | `00 2c 0c 91` | add x0,x0,#0x30b | `FALL_THROUGH`
<a id="insn-00bd6bdc"></a> `00bd6bdc` | `3d 11 02 94` | bl 0x00c5b0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd6be0"></a> `00bd6be0` | `88 2a 00 90` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd6be4"></a> `00bd6be4` | `08 a1 31 91` | add x8,x8,#0xc68 | `FALL_THROUGH`
<a id="insn-00bd6be8"></a> `00bd6be8` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bd6bec"></a> `00bd6bec` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd6bf0"></a> `00bd6bf0` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd6bf4"></a> `00bd6bf4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd6bbc`](#insn-00bd6bbc) 範囲 `[['00bd6bbc', '00bd6bd3']]`
  - `CONDITIONAL_JUMP` [`00bd6bd0`](#insn-00bd6bd0) → [`00bd6be0`](#insn-00bd6be0)
  - `FALL_THROUGH` [`00bd6bd0`](#insn-00bd6bd0) → [`00bd6bd4`](#insn-00bd6bd4)
- ブロック [`00bd6bd4`](#insn-00bd6bd4) 範囲 `[['00bd6bd4', '00bd6bdf']]`
  - `FALL_THROUGH` [`00bd6bdc`](#insn-00bd6bdc) → [`00bd6be0`](#insn-00bd6be0)
- ブロック [`00bd6be0`](#insn-00bd6be0) 範囲 `[['00bd6be0', '00bd6bf7']]`

## 命令位置別の参照

- [`00bd6bbc`](#insn-00bd6bbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6bc0`](#insn-00bd6bc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6bd0`](#insn-00bd6bd0) → [`00bd6be0`](#insn-00bd6be0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6bd8`](#insn-00bd6bd8) → `002a830b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd6bdc`](#insn-00bd6bdc) → [`00c5b0d0`](../00c5b/00c5b0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bd6be8`](#insn-00bd6be8) → `01126c68`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6bec`](#insn-00bd6bec) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd6bbc`](#insn-00bd6bbc)

~~~json
{
  "source": "00bd6bbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6bc0`](#insn-00bd6bc0)

~~~json
{
  "source": "00bd6bc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6bd0`](#insn-00bd6bd0)

~~~json
{
  "source": "00bd6bd0",
  "target": "00bd6be0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6bd8`](#insn-00bd6bd8)

~~~json
{
  "source": "00bd6bd8",
  "target": "002a830b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a830b",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "6d6574686f64203c206b4d6574686f64436f756e7400",
  "capture_start": "002a830b",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bd6bdc`](#insn-00bd6bdc)

~~~json
{
  "source": "00bd6bdc",
  "target": "00c5b0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd6be8`](#insn-00bd6be8)

~~~json
{
  "source": "00bd6be8",
  "target": "01126c68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6bec`](#insn-00bd6bec)

~~~json
{
  "source": "00bd6bec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
