# 00bd2fac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b63aac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63aac.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0068.md#compare-6146ab326c3a54a8c9b34a0f8213a804)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd33d4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd33d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0083.md#compare-88634a4930789add3185d6a631ad999d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd2fac",
  "name": "_ZN8firebase4auth27too_many_requests_exception11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1aa4cde4cfd1bf82cb289435c48d473f10fedf5cbce1641ae6241b74d5fa150f",
  "source_text_sha256": "1aa4cde4cfd1bf82cb289435c48d473f10fedf5cbce1641ae6241b74d5fa150f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd2fac",
        "00bd2fe7"
      ]
    ],
    "bytes_sha256": "e022388f966136f89e7cc59372ee35e9d35cedaf6a1ca938080bef24900288c3",
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

- [00c5ac00](../00c5a/00c5ac00.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 255 bytes

~~~c

undefined8 _ZN8firebase4auth27too_many_requests_exception11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return *(undefined8 *)(&DAT_01126618 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd2fac"></a> `00bd2fac` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd2fb0"></a> `00bd2fb0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2fb4"></a> `00bd2fb4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd2fb8"></a> `00bd2fb8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bd2fbc"></a> `00bd2fbc` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2fc0"></a> `00bd2fc0` | `8b 00 00 54` | b.lt 0x00bd2fd0 | `CONDITIONAL_JUMP`
<a id="insn-00bd2fc4"></a> `00bd2fc4` | `a0 b6 ff d0` | adrp x0,0x2a8000 | `FALL_THROUGH`
<a id="insn-00bd2fc8"></a> `00bd2fc8` | `00 68 0a 91` | add x0,x0,#0x29a | `FALL_THROUGH`
<a id="insn-00bd2fcc"></a> `00bd2fcc` | `0d 1f 02 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00bd2fd0"></a> `00bd2fd0` | `a8 2a 00 90` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd2fd4"></a> `00bd2fd4` | `08 61 18 91` | add x8,x8,#0x618 | `FALL_THROUGH`
<a id="insn-00bd2fd8"></a> `00bd2fd8` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bd2fdc"></a> `00bd2fdc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2fe0"></a> `00bd2fe0` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd2fe4"></a> `00bd2fe4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd2fac`](#insn-00bd2fac) 範囲 `[['00bd2fac', '00bd2fc3']]`
  - `CONDITIONAL_JUMP` [`00bd2fc0`](#insn-00bd2fc0) → [`00bd2fd0`](#insn-00bd2fd0)
  - `FALL_THROUGH` [`00bd2fc0`](#insn-00bd2fc0) → [`00bd2fc4`](#insn-00bd2fc4)
- ブロック [`00bd2fc4`](#insn-00bd2fc4) 範囲 `[['00bd2fc4', '00bd2fcf']]`
  - `FALL_THROUGH` [`00bd2fcc`](#insn-00bd2fcc) → [`00bd2fd0`](#insn-00bd2fd0)
- ブロック [`00bd2fd0`](#insn-00bd2fd0) 範囲 `[['00bd2fd0', '00bd2fe7']]`

## 命令位置別の参照

- [`00bd2fac`](#insn-00bd2fac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2fb0`](#insn-00bd2fb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2fc0`](#insn-00bd2fc0) → [`00bd2fd0`](#insn-00bd2fd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2fc8`](#insn-00bd2fc8) → `002a829a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd2fcc`](#insn-00bd2fcc) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00bd2fd8`](#insn-00bd2fd8) → `01126618`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2fdc`](#insn-00bd2fdc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd2fac`](#insn-00bd2fac)

~~~json
{
  "source": "00bd2fac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2fb0`](#insn-00bd2fb0)

~~~json
{
  "source": "00bd2fb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2fc0`](#insn-00bd2fc0)

~~~json
{
  "source": "00bd2fc0",
  "target": "00bd2fd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2fc8`](#insn-00bd2fc8)

~~~json
{
  "source": "00bd2fc8",
  "target": "002a829a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a829a",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "6d6574686f64203c206b4d6574686f64436f756e7400",
  "capture_start": "002a829a",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bd2fcc`](#insn-00bd2fcc)

~~~json
{
  "source": "00bd2fcc",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2fd8`](#insn-00bd2fd8)

~~~json
{
  "source": "00bd2fd8",
  "target": "01126618",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2fdc`](#insn-00bd2fdc)

~~~json
{
  "source": "00bd2fdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
