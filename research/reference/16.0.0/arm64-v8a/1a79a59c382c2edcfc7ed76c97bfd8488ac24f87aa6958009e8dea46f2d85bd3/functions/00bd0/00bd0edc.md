# 00bd0edc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b619dc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b619dc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0017.md#compare-82962b5fa36bac17239dff70586aea2e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd1304`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd1/00bd1304.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0010.md#compare-7ea2a88f48e9b3e574ce5da8b573e949)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd0edc",
  "name": "_ZN8firebase4auth21action_code_exception11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "adb32034c646a00fa3042de0d8c1c00403c42f98c8198c1edd011e5b23c571ab",
  "source_text_sha256": "adb32034c646a00fa3042de0d8c1c00403c42f98c8198c1edd011e5b23c571ab",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd0edc",
        "00bd0f17"
      ]
    ],
    "bytes_sha256": "7dc194f7b15821ae04a22ec91bc610a8c53711c53081e274fd7b4acc590a9b6d",
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

## 疑似コード / UTF-8 443 bytes

~~~c

undefined8 _ZN8firebase4auth21action_code_exception11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
                    /* try { // try from 00bd0f08 to 00cd0f0f has its CatchHandler @ 00bd6544 */
                    /* try { // try from 00bd0f14 to 00cd0f2b has its CatchHandler @ 00bd653c */
  return *(undefined8 *)(&DAT_011264d8 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd0edc"></a> `00bd0edc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd0ee0"></a> `00bd0ee0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd0ee4"></a> `00bd0ee4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd0ee8"></a> `00bd0ee8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bd0eec"></a> `00bd0eec` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bd0ef0"></a> `00bd0ef0` | `8b 00 00 54` | b.lt 0x00bd0f00 | `CONDITIONAL_JUMP`
<a id="insn-00bd0ef4"></a> `00bd0ef4` | `c0 b6 ff 90` | adrp x0,0x2a8000 | `FALL_THROUGH`
<a id="insn-00bd0ef8"></a> `00bd0ef8` | `00 68 0a 91` | add x0,x0,#0x29a | `FALL_THROUGH`
<a id="insn-00bd0efc"></a> `00bd0efc` | `41 27 02 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00bd0f00"></a> `00bd0f00` | `a8 2a 00 d0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd0f04"></a> `00bd0f04` | `08 61 13 91` | add x8,x8,#0x4d8 | `FALL_THROUGH`
<a id="insn-00bd0f08"></a> `00bd0f08` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bd0f0c"></a> `00bd0f0c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd0f10"></a> `00bd0f10` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd0f14"></a> `00bd0f14` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd0edc`](#insn-00bd0edc) 範囲 `[['00bd0edc', '00bd0ef3']]`
  - `CONDITIONAL_JUMP` [`00bd0ef0`](#insn-00bd0ef0) → [`00bd0f00`](#insn-00bd0f00)
  - `FALL_THROUGH` [`00bd0ef0`](#insn-00bd0ef0) → [`00bd0ef4`](#insn-00bd0ef4)
- ブロック [`00bd0ef4`](#insn-00bd0ef4) 範囲 `[['00bd0ef4', '00bd0eff']]`
  - `FALL_THROUGH` [`00bd0efc`](#insn-00bd0efc) → [`00bd0f00`](#insn-00bd0f00)
- ブロック [`00bd0f00`](#insn-00bd0f00) 範囲 `[['00bd0f00', '00bd0f07']]`
  - `FALL_THROUGH` [`00bd0f04`](#insn-00bd0f04) → [`00bd0f08`](#insn-00bd0f08)
- ブロック [`00bd0f08`](#insn-00bd0f08) 範囲 `[['00bd0f08', '00bd0f13']]`
  - `FALL_THROUGH` [`00bd0f10`](#insn-00bd0f10) → [`00bd0f14`](#insn-00bd0f14)
- ブロック [`00bd0f14`](#insn-00bd0f14) 範囲 `[['00bd0f14', '00bd0f17']]`

## 命令位置別の参照

- [`00bd0edc`](#insn-00bd0edc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0ee0`](#insn-00bd0ee0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0ef0`](#insn-00bd0ef0) → [`00bd0f00`](#insn-00bd0f00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0ef8`](#insn-00bd0ef8) → `002a829a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd0efc`](#insn-00bd0efc) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00bd0f08`](#insn-00bd0f08) → `011264d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0f0c`](#insn-00bd0f0c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd0edc`](#insn-00bd0edc)

~~~json
{
  "source": "00bd0edc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0ee0`](#insn-00bd0ee0)

~~~json
{
  "source": "00bd0ee0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0ef0`](#insn-00bd0ef0)

~~~json
{
  "source": "00bd0ef0",
  "target": "00bd0f00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0ef8`](#insn-00bd0ef8)

~~~json
{
  "source": "00bd0ef8",
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
- 参照命令 [`00bd0efc`](#insn-00bd0efc)

~~~json
{
  "source": "00bd0efc",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd0f08`](#insn-00bd0f08)

~~~json
{
  "source": "00bd0f08",
  "target": "011264d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0f0c`](#insn-00bd0f0c)

~~~json
{
  "source": "00bd0f0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
