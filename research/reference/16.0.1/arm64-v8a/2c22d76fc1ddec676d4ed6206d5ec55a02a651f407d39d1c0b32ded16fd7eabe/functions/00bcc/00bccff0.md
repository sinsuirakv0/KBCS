# 00bccff0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bccbc8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bccbc8.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0010.md#compare-faebaaeef1ac854c3b332d3051b23ee6)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcd08c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd08c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-3e96dda121e4e61a1da5ecccddbc492e)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bccff0",
  "name": "_ZN8firebase4auth21jni_id_token_listener10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fa3e8fb86a4011e06621c179b139f8fa867bdf77148118018c91a1a59268d57f",
  "source_text_sha256": "fa3e8fb86a4011e06621c179b139f8fa867bdf77148118018c91a1a59268d57f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bccff0",
        "00bcd02b"
      ]
    ],
    "bytes_sha256": "996f3fe7e739408cff86382a627b7c7b7cf795f175a734c3ee48e987ecf6cf05",
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
"field < kFieldCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 245 bytes

~~~c

undefined8 _ZN8firebase4auth21jni_id_token_listener10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_01126838 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bccff0"></a> `00bccff0` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bccff4"></a> `00bccff4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccff8"></a> `00bccff8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bccffc"></a> `00bccffc` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bcd000"></a> `00bcd000` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bcd004"></a> `00bcd004` | `8b 00 00 54` | b.lt 0x00bcd014 | `CONDITIONAL_JUMP`
<a id="insn-00bcd008"></a> `00bcd008` | `e0 b6 ff 90` | adrp x0,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bcd00c"></a> `00bcd00c` | `00 78 14 91` | add x0,x0,#0x51e | `FALL_THROUGH`
<a id="insn-00bcd010"></a> `00bcd010` | `fc 37 02 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bcd014"></a> `00bcd014` | `c8 2a 00 b0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcd018"></a> `00bcd018` | `08 e1 20 91` | add x8,x8,#0x838 | `FALL_THROUGH`
<a id="insn-00bcd01c"></a> `00bcd01c` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bcd020"></a> `00bcd020` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcd024"></a> `00bcd024` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcd028"></a> `00bcd028` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bccff0`](#insn-00bccff0) 範囲 `[['00bccff0', '00bcd007']]`
  - `CONDITIONAL_JUMP` [`00bcd004`](#insn-00bcd004) → [`00bcd014`](#insn-00bcd014)
  - `FALL_THROUGH` [`00bcd004`](#insn-00bcd004) → [`00bcd008`](#insn-00bcd008)
- ブロック [`00bcd008`](#insn-00bcd008) 範囲 `[['00bcd008', '00bcd013']]`
  - `FALL_THROUGH` [`00bcd010`](#insn-00bcd010) → [`00bcd014`](#insn-00bcd014)
- ブロック [`00bcd014`](#insn-00bcd014) 範囲 `[['00bcd014', '00bcd02b']]`

## 命令位置別の参照

- [`00bccff0`](#insn-00bccff0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccff4`](#insn-00bccff4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd004`](#insn-00bcd004) → [`00bcd014`](#insn-00bcd014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd00c`](#insn-00bcd00c) → `002a951e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcd010`](#insn-00bcd010) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bcd01c`](#insn-00bcd01c) → `01126838`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd020`](#insn-00bcd020) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bccff0`](#insn-00bccff0)

~~~json
{
  "source": "00bccff0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccff4`](#insn-00bccff4)

~~~json
{
  "source": "00bccff4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd004`](#insn-00bcd004)

~~~json
{
  "source": "00bcd004",
  "target": "00bcd014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd00c`](#insn-00bcd00c)

~~~json
{
  "source": "00bcd00c",
  "target": "002a951e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a951e",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6669656c64203c206b4669656c64436f756e7400",
  "capture_start": "002a951e",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcd010`](#insn-00bcd010)

~~~json
{
  "source": "00bcd010",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd01c`](#insn-00bcd01c)

~~~json
{
  "source": "00bcd01c",
  "target": "01126838",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd020`](#insn-00bcd020)

~~~json
{
  "source": "00bcd020",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
