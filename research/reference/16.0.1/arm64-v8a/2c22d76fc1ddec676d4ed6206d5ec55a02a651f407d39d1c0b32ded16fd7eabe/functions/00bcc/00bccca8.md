# 00bccca8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcc880`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc880.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-e6ac84776358b58f654a98d765ad5d30)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bccd44`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccd44.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0011.md#compare-64b20ff26122be8787c8abd8686c1f71)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bccca8",
  "name": "_ZN8firebase4auth11jnilistener10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b71032388e36192dfacb8bb46355a99eea17fe3177d6c1815deb8b68aa0b2bcd",
  "source_text_sha256": "b71032388e36192dfacb8bb46355a99eea17fe3177d6c1815deb8b68aa0b2bcd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bccca8",
        "00bccce3"
      ]
    ],
    "bytes_sha256": "fc69591c21cb54a69c91021e782eefc36154532b7366b75c8b25fc240412ee01",
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

## 疑似コード / UTF-8 235 bytes

~~~c

undefined8 _ZN8firebase4auth11jnilistener10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_01126810 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bccca8"></a> `00bccca8` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcccac"></a> `00bcccac` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcccb0"></a> `00bcccb0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcccb4"></a> `00bcccb4` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bcccb8"></a> `00bcccb8` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bcccbc"></a> `00bcccbc` | `8b 00 00 54` | b.lt 0x00bccccc | `CONDITIONAL_JUMP`
<a id="insn-00bcccc0"></a> `00bcccc0` | `e0 b6 ff b0` | adrp x0,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bcccc4"></a> `00bcccc4` | `00 78 14 91` | add x0,x0,#0x51e | `FALL_THROUGH`
<a id="insn-00bcccc8"></a> `00bcccc8` | `ce 38 02 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bccccc"></a> `00bccccc` | `c8 2a 00 d0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcccd0"></a> `00bcccd0` | `08 41 20 91` | add x8,x8,#0x810 | `FALL_THROUGH`
<a id="insn-00bcccd4"></a> `00bcccd4` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bcccd8"></a> `00bcccd8` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcccdc"></a> `00bcccdc` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bccce0"></a> `00bccce0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bccca8`](#insn-00bccca8) 範囲 `[['00bccca8', '00bcccbf']]`
  - `CONDITIONAL_JUMP` [`00bcccbc`](#insn-00bcccbc) → [`00bccccc`](#insn-00bccccc)
  - `FALL_THROUGH` [`00bcccbc`](#insn-00bcccbc) → [`00bcccc0`](#insn-00bcccc0)
- ブロック [`00bcccc0`](#insn-00bcccc0) 範囲 `[['00bcccc0', '00bccccb']]`
  - `FALL_THROUGH` [`00bcccc8`](#insn-00bcccc8) → [`00bccccc`](#insn-00bccccc)
- ブロック [`00bccccc`](#insn-00bccccc) 範囲 `[['00bccccc', '00bccce3']]`

## 命令位置別の参照

- [`00bccca8`](#insn-00bccca8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcccac`](#insn-00bcccac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcccbc`](#insn-00bcccbc) → [`00bccccc`](#insn-00bccccc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcccc4`](#insn-00bcccc4) → `002a951e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcccc8`](#insn-00bcccc8) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bcccd4`](#insn-00bcccd4) → `01126810`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcccd8`](#insn-00bcccd8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bccca8`](#insn-00bccca8)

~~~json
{
  "source": "00bccca8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcccac`](#insn-00bcccac)

~~~json
{
  "source": "00bcccac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcccbc`](#insn-00bcccbc)

~~~json
{
  "source": "00bcccbc",
  "target": "00bccccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcccc4`](#insn-00bcccc4)

~~~json
{
  "source": "00bcccc4",
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
- 参照命令 [`00bcccc8`](#insn-00bcccc8)

~~~json
{
  "source": "00bcccc8",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcccd4`](#insn-00bcccd4)

~~~json
{
  "source": "00bcccd4",
  "target": "01126810",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcccd8`](#insn-00bcccd8)

~~~json
{
  "source": "00bcccd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
