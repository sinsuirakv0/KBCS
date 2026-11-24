# 00aeccc0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aecc7c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecc7c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-44b2fa4e078aba0e2970ee8054cb4908)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4ca44`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ca44.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0058.md#compare-64564501ac75ad13d75d496127138458)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeccc0",
  "name": "_ZN8firebase4util22parcel_file_descriptor11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8f05a78122fc88dddf0fedb55d6b6627ae8466efd5819f573a6236f5cc13f25f",
  "source_text_sha256": "8f05a78122fc88dddf0fedb55d6b6627ae8466efd5819f573a6236f5cc13f25f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeccc0",
        "00aeccfb"
      ]
    ],
    "bytes_sha256": "0946bbcf937bdeb8ba491c49b145d567887e7f7e23cb98a4b794b181c98b1a0e",
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

- [00bde180](../00bde/00bde180.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 250 bytes

~~~c

undefined8 _ZN8firebase4util22parcel_file_descriptor11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return *(undefined8 *)(&DAT_010a09b8 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeccc0"></a> `00aeccc0` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeccc4"></a> `00aeccc4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeccc8"></a> `00aeccc8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aecccc"></a> `00aecccc` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00aeccd0"></a> `00aeccd0` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aeccd4"></a> `00aeccd4` | `8b 00 00 54` | b.lt 0x00aecce4 | `CONDITIONAL_JUMP`
<a id="insn-00aeccd8"></a> `00aeccd8` | `60 bd ff 90` | adrp x0,0x298000 | `FALL_THROUGH`
<a id="insn-00aeccdc"></a> `00aeccdc` | `00 1c 15 91` | add x0,x0,#0x547 | `FALL_THROUGH`
<a id="insn-00aecce0"></a> `00aecce0` | `28 c5 03 94` | bl 0x00bde180 | `UNCONDITIONAL_CALL`
<a id="insn-00aecce4"></a> `00aecce4` | `a8 2d 00 90` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecce8"></a> `00aecce8` | `08 e1 26 91` | add x8,x8,#0x9b8 | `FALL_THROUGH`
<a id="insn-00aeccec"></a> `00aeccec` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00aeccf0"></a> `00aeccf0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeccf4"></a> `00aeccf4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeccf8"></a> `00aeccf8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeccc0`](#insn-00aeccc0) 範囲 `[['00aeccc0', '00aeccd7']]`
  - `CONDITIONAL_JUMP` [`00aeccd4`](#insn-00aeccd4) → [`00aecce4`](#insn-00aecce4)
  - `FALL_THROUGH` [`00aeccd4`](#insn-00aeccd4) → [`00aeccd8`](#insn-00aeccd8)
- ブロック [`00aeccd8`](#insn-00aeccd8) 範囲 `[['00aeccd8', '00aecce3']]`
  - `FALL_THROUGH` [`00aecce0`](#insn-00aecce0) → [`00aecce4`](#insn-00aecce4)
- ブロック [`00aecce4`](#insn-00aecce4) 範囲 `[['00aecce4', '00aeccfb']]`

## 命令位置別の参照

- [`00aeccc0`](#insn-00aeccc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeccc4`](#insn-00aeccc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeccd4`](#insn-00aeccd4) → [`00aecce4`](#insn-00aecce4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeccdc`](#insn-00aeccdc) → `00298547`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aecce0`](#insn-00aecce0) → [`00bde180`](../00bde/00bde180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde180` · 推定シンボル `None` · 推定型 `None`
- [`00aeccec`](#insn-00aeccec) → `010a09b8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeccf0`](#insn-00aeccf0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeccc0`](#insn-00aeccc0)

~~~json
{
  "source": "00aeccc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeccc4`](#insn-00aeccc4)

~~~json
{
  "source": "00aeccc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeccd4`](#insn-00aeccd4)

~~~json
{
  "source": "00aeccd4",
  "target": "00aecce4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeccdc`](#insn-00aeccdc)

~~~json
{
  "source": "00aeccdc",
  "target": "00298547",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00298547",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "6d6574686f64203c206b4d6574686f64436f756e7400",
  "capture_start": "00298547",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aecce0`](#insn-00aecce0)

~~~json
{
  "source": "00aecce0",
  "target": "00bde180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeccec`](#insn-00aeccec)

~~~json
{
  "source": "00aeccec",
  "target": "010a09b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeccf0`](#insn-00aeccf0)

~~~json
{
  "source": "00aeccf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
