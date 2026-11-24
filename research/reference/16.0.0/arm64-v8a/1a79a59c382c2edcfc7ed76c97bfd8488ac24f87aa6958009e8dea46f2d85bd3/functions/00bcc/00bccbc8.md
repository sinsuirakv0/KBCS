# 00bccbc8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5d6c8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d6c8.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0017.md#compare-ba7028c820292d1e2bcfcc62104f81d5)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bccff0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccff0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0010.md#compare-faebaaeef1ac854c3b332d3051b23ee6)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bccbc8",
  "name": "_ZN8firebase4auth21jni_id_token_listener10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "723bf1fea30754317b85b8a8aedb735ac758fa4b0ea2fe55798da423161fec60",
  "source_text_sha256": "723bf1fea30754317b85b8a8aedb735ac758fa4b0ea2fe55798da423161fec60",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bccbc8",
        "00bccc03"
      ]
    ],
    "bytes_sha256": "7e913c074ff45427acc801d5bc08841e7155fc771c84670e5419efda46f78a6b",
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

## 疑似コード / UTF-8 439 bytes

~~~c

undefined8 _ZN8firebase4auth21jni_id_token_listener10GetFieldIdENS1_5FieldE(uint param_1)

{
                    /* try { // try from 00bccbd0 to 00cccbe7 has its CatchHandler @ 00bce6fc */
  if (0 < (int)param_1) {
                    /* try { // try from 00bccbe8 to 00cccc93 has its CatchHandler @ 00bcc3d4 */
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_01126438 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bccbc8"></a> `00bccbc8` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bccbcc"></a> `00bccbcc` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccbd0"></a> `00bccbd0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bccbd4"></a> `00bccbd4` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bccbd8"></a> `00bccbd8` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bccbdc"></a> `00bccbdc` | `8b 00 00 54` | b.lt 0x00bccbec | `CONDITIONAL_JUMP`
<a id="insn-00bccbe0"></a> `00bccbe0` | `e0 b6 ff b0` | adrp x0,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bccbe4"></a> `00bccbe4` | `00 44 11 91` | add x0,x0,#0x451 | `FALL_THROUGH`
<a id="insn-00bccbe8"></a> `00bccbe8` | `06 38 02 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00bccbec"></a> `00bccbec` | `c8 2a 00 d0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bccbf0"></a> `00bccbf0` | `08 e1 10 91` | add x8,x8,#0x438 | `FALL_THROUGH`
<a id="insn-00bccbf4"></a> `00bccbf4` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bccbf8"></a> `00bccbf8` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccbfc"></a> `00bccbfc` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bccc00"></a> `00bccc00` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bccbc8`](#insn-00bccbc8) 範囲 `[['00bccbc8', '00bccbcf']]`
  - `FALL_THROUGH` [`00bccbcc`](#insn-00bccbcc) → [`00bccbd0`](#insn-00bccbd0)
- ブロック [`00bccbd0`](#insn-00bccbd0) 範囲 `[['00bccbd0', '00bccbdf']]`
  - `CONDITIONAL_JUMP` [`00bccbdc`](#insn-00bccbdc) → [`00bccbec`](#insn-00bccbec)
  - `FALL_THROUGH` [`00bccbdc`](#insn-00bccbdc) → [`00bccbe0`](#insn-00bccbe0)
- ブロック [`00bccbe0`](#insn-00bccbe0) 範囲 `[['00bccbe0', '00bccbe7']]`
  - `FALL_THROUGH` [`00bccbe4`](#insn-00bccbe4) → [`00bccbe8`](#insn-00bccbe8)
- ブロック [`00bccbe8`](#insn-00bccbe8) 範囲 `[['00bccbe8', '00bccbeb']]`
  - `FALL_THROUGH` [`00bccbe8`](#insn-00bccbe8) → [`00bccbec`](#insn-00bccbec)
- ブロック [`00bccbec`](#insn-00bccbec) 範囲 `[['00bccbec', '00bccc03']]`

## 命令位置別の参照

- [`00bccbc8`](#insn-00bccbc8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccbcc`](#insn-00bccbcc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccbdc`](#insn-00bccbdc) → [`00bccbec`](#insn-00bccbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccbe4`](#insn-00bccbe4) → `002a9451`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bccbe8`](#insn-00bccbe8) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00bccbf4`](#insn-00bccbf4) → `01126438`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccbf8`](#insn-00bccbf8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bccbc8`](#insn-00bccbc8)

~~~json
{
  "source": "00bccbc8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccbcc`](#insn-00bccbcc)

~~~json
{
  "source": "00bccbcc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccbdc`](#insn-00bccbdc)

~~~json
{
  "source": "00bccbdc",
  "target": "00bccbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccbe4`](#insn-00bccbe4)

~~~json
{
  "source": "00bccbe4",
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
- 参照命令 [`00bccbe8`](#insn-00bccbe8)

~~~json
{
  "source": "00bccbe8",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bccbf4`](#insn-00bccbf4)

~~~json
{
  "source": "00bccbf4",
  "target": "01126438",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccbf8`](#insn-00bccbf8)

~~~json
{
  "source": "00bccbf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
