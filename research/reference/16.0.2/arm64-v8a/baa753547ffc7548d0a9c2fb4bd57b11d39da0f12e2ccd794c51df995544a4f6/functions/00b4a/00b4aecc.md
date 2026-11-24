# 00b4aecc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b4ae30`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ae30.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0008.md#compare-d32818e64c5d89faeb2ad0411c9e724e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00b4bec0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bec0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0075.md#compare-6e0357b7b1adbcb79863d79d710db2e9)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4aecc",
  "name": "_ZN8firebase4util11float_class10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e9f05782b85b43b43539b2527dde738621e5fcbc174082c9d88978f29f6b8326",
  "source_text_sha256": "e9f05782b85b43b43539b2527dde738621e5fcbc174082c9d88978f29f6b8326",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4aecc",
        "00b4af07"
      ]
    ],
    "bytes_sha256": "2ef912b82e8cffb9b8e910fda27ed3ea4edddf7f1d33ed2af118ef8cb7d32964",
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

## 疑似コード / UTF-8 332 bytes

~~~c

undefined8 _ZN8firebase4util11float_class10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
                    /* try { // try from 00b4aee8 to 00c4af23 has its CatchHandler @ 00b4f098 */
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_01125c08 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4aecc"></a> `00b4aecc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b4aed0"></a> `00b4aed0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4aed4"></a> `00b4aed4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b4aed8"></a> `00b4aed8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00b4aedc"></a> `00b4aedc` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00b4aee0"></a> `00b4aee0` | `8b 00 00 54` | b.lt 0x00b4aef0 | `CONDITIONAL_JUMP`
<a id="insn-00b4aee4"></a> `00b4aee4` | `e0 ba ff f0` | adrp x0,0x2a9000 | `FALL_THROUGH`
<a id="insn-00b4aee8"></a> `00b4aee8` | `00 34 15 91` | add x0,x0,#0x54d | `FALL_THROUGH`
<a id="insn-00b4aeec"></a> `00b4aeec` | `79 40 04 94` | bl 0x00c5b0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00b4aef0"></a> `00b4aef0` | `c8 2e 00 f0` | adrp x8,0x1125000 | `FALL_THROUGH`
<a id="insn-00b4aef4"></a> `00b4aef4` | `08 21 30 91` | add x8,x8,#0xc08 | `FALL_THROUGH`
<a id="insn-00b4aef8"></a> `00b4aef8` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00b4aefc"></a> `00b4aefc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4af00"></a> `00b4af00` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b4af04"></a> `00b4af04` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4aecc`](#insn-00b4aecc) 範囲 `[['00b4aecc', '00b4aee3']]`
  - `CONDITIONAL_JUMP` [`00b4aee0`](#insn-00b4aee0) → [`00b4aef0`](#insn-00b4aef0)
  - `FALL_THROUGH` [`00b4aee0`](#insn-00b4aee0) → [`00b4aee4`](#insn-00b4aee4)
- ブロック [`00b4aee4`](#insn-00b4aee4) 範囲 `[['00b4aee4', '00b4aee7']]`
  - `FALL_THROUGH` [`00b4aee4`](#insn-00b4aee4) → [`00b4aee8`](#insn-00b4aee8)
- ブロック [`00b4aee8`](#insn-00b4aee8) 範囲 `[['00b4aee8', '00b4aeef']]`
  - `FALL_THROUGH` [`00b4aeec`](#insn-00b4aeec) → [`00b4aef0`](#insn-00b4aef0)
- ブロック [`00b4aef0`](#insn-00b4aef0) 範囲 `[['00b4aef0', '00b4af07']]`

## 命令位置別の参照

- [`00b4aecc`](#insn-00b4aecc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4aed0`](#insn-00b4aed0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4aee0`](#insn-00b4aee0) → [`00b4aef0`](#insn-00b4aef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4aee8`](#insn-00b4aee8) → `002a954d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4aeec`](#insn-00b4aeec) → [`00c5b0d0`](../00c5b/00c5b0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0d0` · 推定シンボル `None` · 推定型 `None`
- [`00b4aef8`](#insn-00b4aef8) → `01125c08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4aefc`](#insn-00b4aefc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4aecc`](#insn-00b4aecc)

~~~json
{
  "source": "00b4aecc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4aed0`](#insn-00b4aed0)

~~~json
{
  "source": "00b4aed0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4aee0`](#insn-00b4aee0)

~~~json
{
  "source": "00b4aee0",
  "target": "00b4aef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4aee8`](#insn-00b4aee8)

~~~json
{
  "source": "00b4aee8",
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
- 参照命令 [`00b4aeec`](#insn-00b4aeec)

~~~json
{
  "source": "00b4aeec",
  "target": "00c5b0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4aef8`](#insn-00b4aef8)

~~~json
{
  "source": "00b4aef8",
  "target": "01125c08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4aefc`](#insn-00b4aefc)

~~~json
{
  "source": "00b4aefc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
