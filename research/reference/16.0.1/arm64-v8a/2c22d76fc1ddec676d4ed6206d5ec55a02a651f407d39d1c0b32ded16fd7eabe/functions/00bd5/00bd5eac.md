# 00bd5eac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bd5a84`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5a84.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0083.md#compare-b8475bd8ee0c03e34449151ba6ef13d5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bd5f48`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd5/00bd5f48.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0083.md#compare-8a3b52e982cd636903e92b4808a06e6f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd5eac",
  "name": "_ZN8firebase4auth10googlecred10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4972f1e203207e732de161e323b39a8a82530940ac258a7a2a300e13823b5b35",
  "source_text_sha256": "4972f1e203207e732de161e323b39a8a82530940ac258a7a2a300e13823b5b35",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd5eac",
        "00bd5ee7"
      ]
    ],
    "bytes_sha256": "9f48ccccc5ef73bdc8d81f0e64931652808fa3e2b43c90ca0aa62fe6063b10e4",
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

## 疑似コード / UTF-8 234 bytes

~~~c

undefined8 _ZN8firebase4auth10googlecred10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_01126ae0 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd5eac"></a> `00bd5eac` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd5eb0"></a> `00bd5eb0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd5eb4"></a> `00bd5eb4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd5eb8"></a> `00bd5eb8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bd5ebc"></a> `00bd5ebc` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bd5ec0"></a> `00bd5ec0` | `8b 00 00 54` | b.lt 0x00bd5ed0 | `CONDITIONAL_JUMP`
<a id="insn-00bd5ec4"></a> `00bd5ec4` | `a0 b6 ff 90` | adrp x0,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bd5ec8"></a> `00bd5ec8` | `00 78 14 91` | add x0,x0,#0x51e | `FALL_THROUGH`
<a id="insn-00bd5ecc"></a> `00bd5ecc` | `4d 14 02 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bd5ed0"></a> `00bd5ed0` | `88 2a 00 b0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd5ed4"></a> `00bd5ed4` | `08 81 2b 91` | add x8,x8,#0xae0 | `FALL_THROUGH`
<a id="insn-00bd5ed8"></a> `00bd5ed8` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bd5edc"></a> `00bd5edc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd5ee0"></a> `00bd5ee0` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd5ee4"></a> `00bd5ee4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd5eac`](#insn-00bd5eac) 範囲 `[['00bd5eac', '00bd5ec3']]`
  - `CONDITIONAL_JUMP` [`00bd5ec0`](#insn-00bd5ec0) → [`00bd5ed0`](#insn-00bd5ed0)
  - `FALL_THROUGH` [`00bd5ec0`](#insn-00bd5ec0) → [`00bd5ec4`](#insn-00bd5ec4)
- ブロック [`00bd5ec4`](#insn-00bd5ec4) 範囲 `[['00bd5ec4', '00bd5ecf']]`
  - `FALL_THROUGH` [`00bd5ecc`](#insn-00bd5ecc) → [`00bd5ed0`](#insn-00bd5ed0)
- ブロック [`00bd5ed0`](#insn-00bd5ed0) 範囲 `[['00bd5ed0', '00bd5ee7']]`

## 命令位置別の参照

- [`00bd5eac`](#insn-00bd5eac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5eb0`](#insn-00bd5eb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5ec0`](#insn-00bd5ec0) → [`00bd5ed0`](#insn-00bd5ed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5ec8`](#insn-00bd5ec8) → `002a951e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd5ecc`](#insn-00bd5ecc) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bd5ed8`](#insn-00bd5ed8) → `01126ae0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5edc`](#insn-00bd5edc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd5eac`](#insn-00bd5eac)

~~~json
{
  "source": "00bd5eac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5eb0`](#insn-00bd5eb0)

~~~json
{
  "source": "00bd5eb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5ec0`](#insn-00bd5ec0)

~~~json
{
  "source": "00bd5ec0",
  "target": "00bd5ed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5ec8`](#insn-00bd5ec8)

~~~json
{
  "source": "00bd5ec8",
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
- 参照命令 [`00bd5ecc`](#insn-00bd5ecc)

~~~json
{
  "source": "00bd5ecc",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd5ed8`](#insn-00bd5ed8)

~~~json
{
  "source": "00bd5ed8",
  "target": "01126ae0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5edc`](#insn-00bd5edc)

~~~json
{
  "source": "00bd5edc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
