# 00bd1cdc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bd18b4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd18b4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0082.md#compare-b697c0565d6a83fb429a2858f5207e0b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bd1d78`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd1/00bd1d78.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0082.md#compare-a2e6a212c189dfb4d93b764c2f48b3b9)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd1cdc",
  "name": "_ZN8firebase4auth29invalid_credentials_exception11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5f183bb95931fc156a08bb94461db2c0e83c49e2b9c7f7b0e56d13b7f2083590",
  "source_text_sha256": "5f183bb95931fc156a08bb94461db2c0e83c49e2b9c7f7b0e56d13b7f2083590",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd1cdc",
        "00bd1d17"
      ]
    ],
    "bytes_sha256": "4dd29aef5253f3405f755d68fd9139879015ffc85c6524692d82e7a2d446222a",
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

- [00c5b000](../00c5b/00c5b000.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 257 bytes

~~~c

undefined8 _ZN8firebase4auth29invalid_credentials_exception11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return *(undefined8 *)(&DAT_01126938 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd1cdc"></a> `00bd1cdc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd1ce0"></a> `00bd1ce0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd1ce4"></a> `00bd1ce4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd1ce8"></a> `00bd1ce8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bd1cec"></a> `00bd1cec` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bd1cf0"></a> `00bd1cf0` | `8b 00 00 54` | b.lt 0x00bd1d00 | `CONDITIONAL_JUMP`
<a id="insn-00bd1cf4"></a> `00bd1cf4` | `a0 b6 ff f0` | adrp x0,0x2a8000 | `FALL_THROUGH`
<a id="insn-00bd1cf8"></a> `00bd1cf8` | `00 9c 0d 91` | add x0,x0,#0x367 | `FALL_THROUGH`
<a id="insn-00bd1cfc"></a> `00bd1cfc` | `c1 24 02 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bd1d00"></a> `00bd1d00` | `a8 2a 00 b0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd1d04"></a> `00bd1d04` | `08 e1 24 91` | add x8,x8,#0x938 | `FALL_THROUGH`
<a id="insn-00bd1d08"></a> `00bd1d08` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bd1d0c"></a> `00bd1d0c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd1d10"></a> `00bd1d10` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd1d14"></a> `00bd1d14` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd1cdc`](#insn-00bd1cdc) 範囲 `[['00bd1cdc', '00bd1cf3']]`
  - `CONDITIONAL_JUMP` [`00bd1cf0`](#insn-00bd1cf0) → [`00bd1d00`](#insn-00bd1d00)
  - `FALL_THROUGH` [`00bd1cf0`](#insn-00bd1cf0) → [`00bd1cf4`](#insn-00bd1cf4)
- ブロック [`00bd1cf4`](#insn-00bd1cf4) 範囲 `[['00bd1cf4', '00bd1cff']]`
  - `FALL_THROUGH` [`00bd1cfc`](#insn-00bd1cfc) → [`00bd1d00`](#insn-00bd1d00)
- ブロック [`00bd1d00`](#insn-00bd1d00) 範囲 `[['00bd1d00', '00bd1d17']]`

## 命令位置別の参照

- [`00bd1cdc`](#insn-00bd1cdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1ce0`](#insn-00bd1ce0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1cf0`](#insn-00bd1cf0) → [`00bd1d00`](#insn-00bd1d00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1cf8`](#insn-00bd1cf8) → `002a8367`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd1cfc`](#insn-00bd1cfc) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bd1d08`](#insn-00bd1d08) → `01126938`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1d0c`](#insn-00bd1d0c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd1cdc`](#insn-00bd1cdc)

~~~json
{
  "source": "00bd1cdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1ce0`](#insn-00bd1ce0)

~~~json
{
  "source": "00bd1ce0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1cf0`](#insn-00bd1cf0)

~~~json
{
  "source": "00bd1cf0",
  "target": "00bd1d00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1cf8`](#insn-00bd1cf8)

~~~json
{
  "source": "00bd1cf8",
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
- 参照命令 [`00bd1cfc`](#insn-00bd1cfc)

~~~json
{
  "source": "00bd1cfc",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd1d08`](#insn-00bd1d08)

~~~json
{
  "source": "00bd1d08",
  "target": "01126938",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1d0c`](#insn-00bd1d0c)

~~~json
{
  "source": "00bd1d0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
