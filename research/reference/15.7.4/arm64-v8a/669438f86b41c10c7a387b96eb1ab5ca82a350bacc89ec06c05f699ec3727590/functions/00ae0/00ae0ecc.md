# 00ae0ecc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ae0e88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0e88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0061.md#compare-56cb7817a796969402693b107c2b0997)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b408a4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b408a4.md) · 移動量 `+0x5f9d8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0014.md#compare-6b000ca114d999ca3e68b192ff5ca00f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae0ecc",
  "name": "_ZN8firebase9analytics24analytics_consent_status11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d3339030971994036c36cd4dc40476185eb78900369ea498b278cc0dea856600",
  "source_text_sha256": "d3339030971994036c36cd4dc40476185eb78900369ea498b278cc0dea856600",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae0ecc",
        "00ae0f07"
      ]
    ],
    "bytes_sha256": "0562240343b364796947b4bf1448e5b7bcf1fbfa4fe3469264a7823e0e5effc2",
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

## 疑似コード / UTF-8 257 bytes

~~~c

undefined8 _ZN8firebase9analytics24analytics_consent_status11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return *(undefined8 *)(&DAT_010a0128 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae0ecc"></a> `00ae0ecc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ae0ed0"></a> `00ae0ed0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae0ed4"></a> `00ae0ed4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ae0ed8"></a> `00ae0ed8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00ae0edc"></a> `00ae0edc` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00ae0ee0"></a> `00ae0ee0` | `8b 00 00 54` | b.lt 0x00ae0ef0 | `CONDITIONAL_JUMP`
<a id="insn-00ae0ee4"></a> `00ae0ee4` | `c0 bd ff 90` | adrp x0,0x298000 | `FALL_THROUGH`
<a id="insn-00ae0ee8"></a> `00ae0ee8` | `00 1c 15 91` | add x0,x0,#0x547 | `FALL_THROUGH`
<a id="insn-00ae0eec"></a> `00ae0eec` | `a5 f4 03 94` | bl 0x00bde180 | `UNCONDITIONAL_CALL`
<a id="insn-00ae0ef0"></a> `00ae0ef0` | `08 2e 00 90` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae0ef4"></a> `00ae0ef4` | `08 a1 04 91` | add x8,x8,#0x128 | `FALL_THROUGH`
<a id="insn-00ae0ef8"></a> `00ae0ef8` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00ae0efc"></a> `00ae0efc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae0f00"></a> `00ae0f00` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ae0f04"></a> `00ae0f04` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae0ecc`](#insn-00ae0ecc) 範囲 `[['00ae0ecc', '00ae0ee3']]`
  - `CONDITIONAL_JUMP` [`00ae0ee0`](#insn-00ae0ee0) → [`00ae0ef0`](#insn-00ae0ef0)
  - `FALL_THROUGH` [`00ae0ee0`](#insn-00ae0ee0) → [`00ae0ee4`](#insn-00ae0ee4)
- ブロック [`00ae0ee4`](#insn-00ae0ee4) 範囲 `[['00ae0ee4', '00ae0eef']]`
  - `FALL_THROUGH` [`00ae0eec`](#insn-00ae0eec) → [`00ae0ef0`](#insn-00ae0ef0)
- ブロック [`00ae0ef0`](#insn-00ae0ef0) 範囲 `[['00ae0ef0', '00ae0f07']]`

## 命令位置別の参照

- [`00ae0ecc`](#insn-00ae0ecc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0ed0`](#insn-00ae0ed0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0ee0`](#insn-00ae0ee0) → [`00ae0ef0`](#insn-00ae0ef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0ee8`](#insn-00ae0ee8) → `00298547`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae0eec`](#insn-00ae0eec) → [`00bde180`](../00bde/00bde180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde180` · 推定シンボル `None` · 推定型 `None`
- [`00ae0ef8`](#insn-00ae0ef8) → `010a0128`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0efc`](#insn-00ae0efc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae0ecc`](#insn-00ae0ecc)

~~~json
{
  "source": "00ae0ecc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0ed0`](#insn-00ae0ed0)

~~~json
{
  "source": "00ae0ed0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0ee0`](#insn-00ae0ee0)

~~~json
{
  "source": "00ae0ee0",
  "target": "00ae0ef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0ee8`](#insn-00ae0ee8)

~~~json
{
  "source": "00ae0ee8",
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
- 参照命令 [`00ae0eec`](#insn-00ae0eec)

~~~json
{
  "source": "00ae0eec",
  "target": "00bde180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae0ef8`](#insn-00ae0ef8)

~~~json
{
  "source": "00ae0ef8",
  "target": "010a0128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0efc`](#insn-00ae0efc)

~~~json
{
  "source": "00ae0efc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
