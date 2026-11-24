# 00b4bfcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4bba4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bba4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0072.md#compare-4bb02b43c3993e08638e54d91f21a541)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b4c068`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c068.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0073.md#compare-56cc42c836b41529ac775dc6adfab5ae)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4bfcc",
  "name": "_ZN8firebase4util8iterator11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "37e63ac54e774efd27292c01a7d24b8253cce8f19519b327f67e652f876da48b",
  "source_text_sha256": "37e63ac54e774efd27292c01a7d24b8253cce8f19519b327f67e652f876da48b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4bfcc",
        "00b4c007"
      ]
    ],
    "bytes_sha256": "6d367921381c1b75259fb0e45c3ec199764b960297cfbb6cec1702c3faf1f5e7",
    "instruction_count": 15,
    "instruction_bytes": 60,
    "body_bytes": 60,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5b560](../00c5b/00c5b560.md)

## 呼び出し先

- [00c5b000](../00c5b/00c5b000.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 208 bytes

~~~c

undefined8 _ZN8firebase4util8iterator11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (1 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return (&DAT_01125bc8)[param_1];
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4bfcc"></a> `00b4bfcc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b4bfd0"></a> `00b4bfd0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4bfd4"></a> `00b4bfd4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b4bfd8"></a> `00b4bfd8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00b4bfdc"></a> `00b4bfdc` | `1f 08 00 71` | cmp w0,#0x2 | `FALL_THROUGH`
<a id="insn-00b4bfe0"></a> `00b4bfe0` | `8b 00 00 54` | b.lt 0x00b4bff0 | `CONDITIONAL_JUMP`
<a id="insn-00b4bfe4"></a> `00b4bfe4` | `e0 ba ff b0` | adrp x0,0x2a8000 | `FALL_THROUGH`
<a id="insn-00b4bfe8"></a> `00b4bfe8` | `00 9c 0d 91` | add x0,x0,#0x367 | `FALL_THROUGH`
<a id="insn-00b4bfec"></a> `00b4bfec` | `05 3c 04 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00b4bff0"></a> `00b4bff0` | `c8 2e 00 d0` | adrp x8,0x1125000 | `FALL_THROUGH`
<a id="insn-00b4bff4"></a> `00b4bff4` | `08 21 2f 91` | add x8,x8,#0xbc8 | `FALL_THROUGH`
<a id="insn-00b4bff8"></a> `00b4bff8` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00b4bffc"></a> `00b4bffc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4c000"></a> `00b4c000` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b4c004"></a> `00b4c004` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4bfcc`](#insn-00b4bfcc) 範囲 `[['00b4bfcc', '00b4bfe3']]`
  - `CONDITIONAL_JUMP` [`00b4bfe0`](#insn-00b4bfe0) → [`00b4bff0`](#insn-00b4bff0)
  - `FALL_THROUGH` [`00b4bfe0`](#insn-00b4bfe0) → [`00b4bfe4`](#insn-00b4bfe4)
- ブロック [`00b4bfe4`](#insn-00b4bfe4) 範囲 `[['00b4bfe4', '00b4bfef']]`
  - `FALL_THROUGH` [`00b4bfec`](#insn-00b4bfec) → [`00b4bff0`](#insn-00b4bff0)
- ブロック [`00b4bff0`](#insn-00b4bff0) 範囲 `[['00b4bff0', '00b4c007']]`

## 命令位置別の参照

- [`00b4bfcc`](#insn-00b4bfcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bfd0`](#insn-00b4bfd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bfe0`](#insn-00b4bfe0) → [`00b4bff0`](#insn-00b4bff0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bfe8`](#insn-00b4bfe8) → `002a8367`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4bfec`](#insn-00b4bfec) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00b4bff8`](#insn-00b4bff8) → `01125bc8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4bffc`](#insn-00b4bffc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4bfcc`](#insn-00b4bfcc)

~~~json
{
  "source": "00b4bfcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bfd0`](#insn-00b4bfd0)

~~~json
{
  "source": "00b4bfd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bfe0`](#insn-00b4bfe0)

~~~json
{
  "source": "00b4bfe0",
  "target": "00b4bff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bfe8`](#insn-00b4bfe8)

~~~json
{
  "source": "00b4bfe8",
  "target": "002a8367",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8367",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "6d6574686f64203c206b4d6574686f64436f756e7400",
  "capture_start": "002a8367",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4bfec`](#insn-00b4bfec)

~~~json
{
  "source": "00b4bfec",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4bff8`](#insn-00b4bff8)

~~~json
{
  "source": "00b4bff8",
  "target": "01125bc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125bc8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4bffc`](#insn-00b4bffc)

~~~json
{
  "source": "00b4bffc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
