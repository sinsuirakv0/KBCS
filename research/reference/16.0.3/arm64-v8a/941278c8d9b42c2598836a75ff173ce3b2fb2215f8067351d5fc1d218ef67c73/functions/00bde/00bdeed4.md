# 00bdeed4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bddee0`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddee0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0086.md#compare-aec6d6ec59a2512a4fb01e8989307c17)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdeed4",
  "name": "_ZN8firebase4auth18userprofilebuilder10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "42d1251ee998e21585e5087fb4c0f5ad5785f48143bbd658bae422f610b2b4d6",
  "source_text_sha256": "42d1251ee998e21585e5087fb4c0f5ad5785f48143bbd658bae422f610b2b4d6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdeed4",
        "00bdef0f"
      ]
    ],
    "bytes_sha256": "4b15fc18c606e2add888217c62947039be627d4a95300689fd9075b6484632d3",
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

- [00c5c0a0](../00c5c/00c5c0a0.md)

## 関連文字列（未確認候補）

~~~text
"field < kFieldCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 242 bytes

~~~c

undefined8 _ZN8firebase4auth18userprofilebuilder10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_01127f18 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdeed4"></a> `00bdeed4` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdeed8"></a> `00bdeed8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdeedc"></a> `00bdeedc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdeee0"></a> `00bdeee0` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bdeee4"></a> `00bdeee4` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bdeee8"></a> `00bdeee8` | `8b 00 00 54` | b.lt 0x00bdeef8 | `CONDITIONAL_JUMP`
<a id="insn-00bdeeec"></a> `00bdeeec` | `40 b6 ff f0` | adrp x0,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bdeef0"></a> `00bdeef0` | `00 68 18 91` | add x0,x0,#0x61a | `FALL_THROUGH`
<a id="insn-00bdeef4"></a> `00bdeef4` | `6b f4 01 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdeef8"></a> `00bdeef8` | `48 2a 00 b0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdeefc"></a> `00bdeefc` | `08 61 3c 91` | add x8,x8,#0xf18 | `FALL_THROUGH`
<a id="insn-00bdef00"></a> `00bdef00` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bdef04"></a> `00bdef04` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdef08"></a> `00bdef08` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdef0c"></a> `00bdef0c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdeed4`](#insn-00bdeed4) 範囲 `[['00bdeed4', '00bdeeeb']]`
  - `CONDITIONAL_JUMP` [`00bdeee8`](#insn-00bdeee8) → [`00bdeef8`](#insn-00bdeef8)
  - `FALL_THROUGH` [`00bdeee8`](#insn-00bdeee8) → [`00bdeeec`](#insn-00bdeeec)
- ブロック [`00bdeeec`](#insn-00bdeeec) 範囲 `[['00bdeeec', '00bdeef7']]`
  - `FALL_THROUGH` [`00bdeef4`](#insn-00bdeef4) → [`00bdeef8`](#insn-00bdeef8)
- ブロック [`00bdeef8`](#insn-00bdeef8) 範囲 `[['00bdeef8', '00bdef0f']]`

## 命令位置別の参照

- [`00bdeed4`](#insn-00bdeed4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeed8`](#insn-00bdeed8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeee8`](#insn-00bdeee8) → [`00bdeef8`](#insn-00bdeef8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeef0`](#insn-00bdeef0) → `002a961a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdeef4`](#insn-00bdeef4) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bdef00`](#insn-00bdef00) → `01127f18`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdef04`](#insn-00bdef04) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdeed4`](#insn-00bdeed4)

~~~json
{
  "source": "00bdeed4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeed8`](#insn-00bdeed8)

~~~json
{
  "source": "00bdeed8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeee8`](#insn-00bdeee8)

~~~json
{
  "source": "00bdeee8",
  "target": "00bdeef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeef0`](#insn-00bdeef0)

~~~json
{
  "source": "00bdeef0",
  "target": "002a961a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a961a",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6669656c64203c206b4669656c64436f756e7400",
  "capture_start": "002a961a",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bdeef4`](#insn-00bdeef4)

~~~json
{
  "source": "00bdeef4",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdef00`](#insn-00bdef00)

~~~json
{
  "source": "00bdef00",
  "target": "01127f18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdef04`](#insn-00bdef04)

~~~json
{
  "source": "00bdef04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
