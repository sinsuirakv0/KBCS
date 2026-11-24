# 00bd5dcc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b668cc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b668cc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0069.md#compare-76b472fcc6d42694e12344f4955ff3bf)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd61f4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd61f4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0083.md#compare-bcce85906216e4fe6613a7ed5017c47d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd5dcc",
  "name": "_ZN8firebase4auth13playgamescred10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "40f20edca8c878a371edbc24827fc404631a03bc38e1911489ff0bd7ee80557f",
  "source_text_sha256": "40f20edca8c878a371edbc24827fc404631a03bc38e1911489ff0bd7ee80557f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd5dcc",
        "00bd5e07"
      ]
    ],
    "bytes_sha256": "a2776ed3c3c93f07a81d07c96e37776fce51dd3e59898412fd5ad6481d571f70",
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
"field < kFieldCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 237 bytes

~~~c

undefined8 _ZN8firebase4auth13playgamescred10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_01126700 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd5dcc"></a> `00bd5dcc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd5dd0"></a> `00bd5dd0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd5dd4"></a> `00bd5dd4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd5dd8"></a> `00bd5dd8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bd5ddc"></a> `00bd5ddc` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bd5de0"></a> `00bd5de0` | `8b 00 00 54` | b.lt 0x00bd5df0 | `CONDITIONAL_JUMP`
<a id="insn-00bd5de4"></a> `00bd5de4` | `a0 b6 ff 90` | adrp x0,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bd5de8"></a> `00bd5de8` | `00 44 11 91` | add x0,x0,#0x451 | `FALL_THROUGH`
<a id="insn-00bd5dec"></a> `00bd5dec` | `85 13 02 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00bd5df0"></a> `00bd5df0` | `88 2a 00 b0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd5df4"></a> `00bd5df4` | `08 01 1c 91` | add x8,x8,#0x700 | `FALL_THROUGH`
<a id="insn-00bd5df8"></a> `00bd5df8` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bd5dfc"></a> `00bd5dfc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd5e00"></a> `00bd5e00` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd5e04"></a> `00bd5e04` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd5dcc`](#insn-00bd5dcc) 範囲 `[['00bd5dcc', '00bd5de3']]`
  - `CONDITIONAL_JUMP` [`00bd5de0`](#insn-00bd5de0) → [`00bd5df0`](#insn-00bd5df0)
  - `FALL_THROUGH` [`00bd5de0`](#insn-00bd5de0) → [`00bd5de4`](#insn-00bd5de4)
- ブロック [`00bd5de4`](#insn-00bd5de4) 範囲 `[['00bd5de4', '00bd5def']]`
  - `FALL_THROUGH` [`00bd5dec`](#insn-00bd5dec) → [`00bd5df0`](#insn-00bd5df0)
- ブロック [`00bd5df0`](#insn-00bd5df0) 範囲 `[['00bd5df0', '00bd5e07']]`

## 命令位置別の参照

- [`00bd5dcc`](#insn-00bd5dcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5dd0`](#insn-00bd5dd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5de0`](#insn-00bd5de0) → [`00bd5df0`](#insn-00bd5df0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5de8`](#insn-00bd5de8) → `002a9451`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd5dec`](#insn-00bd5dec) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00bd5df8`](#insn-00bd5df8) → `01126700`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5dfc`](#insn-00bd5dfc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd5dcc`](#insn-00bd5dcc)

~~~json
{
  "source": "00bd5dcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5dd0`](#insn-00bd5dd0)

~~~json
{
  "source": "00bd5dd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5de0`](#insn-00bd5de0)

~~~json
{
  "source": "00bd5de0",
  "target": "00bd5df0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5de8`](#insn-00bd5de8)

~~~json
{
  "source": "00bd5de8",
  "target": "002a9451",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a9451",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6669656c64203c206b4669656c64436f756e7400",
  "capture_start": "002a9451",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bd5dec`](#insn-00bd5dec)

~~~json
{
  "source": "00bd5dec",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd5df8`](#insn-00bd5df8)

~~~json
{
  "source": "00bd5df8",
  "target": "01126700",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5dfc`](#insn-00bd5dfc)

~~~json
{
  "source": "00bd5dfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
