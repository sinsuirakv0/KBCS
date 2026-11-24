# 00bdeb8c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bddb98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddb98.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-25e437d0dfe9f5309be016611a1d5c8d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdeb8c",
  "name": "_ZN8firebase4auth8metadata10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c770a7e330ad91c7d17d86166e77163a972d05928862cedbed38492980a6faa0",
  "source_text_sha256": "c770a7e330ad91c7d17d86166e77163a972d05928862cedbed38492980a6faa0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdeb8c",
        "00bdebc7"
      ]
    ],
    "bytes_sha256": "4920152461449c04cd73825c3f0a543a5d7e2795268a53cb7d9f9f54201f5660",
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

## 疑似コード / UTF-8 231 bytes

~~~c

undefined8 _ZN8firebase4auth8metadata10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_01127ee0 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdeb8c"></a> `00bdeb8c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdeb90"></a> `00bdeb90` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdeb94"></a> `00bdeb94` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdeb98"></a> `00bdeb98` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bdeb9c"></a> `00bdeb9c` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bdeba0"></a> `00bdeba0` | `8b 00 00 54` | b.lt 0x00bdebb0 | `CONDITIONAL_JUMP`
<a id="insn-00bdeba4"></a> `00bdeba4` | `40 b6 ff f0` | adrp x0,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bdeba8"></a> `00bdeba8` | `00 68 18 91` | add x0,x0,#0x61a | `FALL_THROUGH`
<a id="insn-00bdebac"></a> `00bdebac` | `3d f5 01 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdebb0"></a> `00bdebb0` | `48 2a 00 b0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdebb4"></a> `00bdebb4` | `08 81 3b 91` | add x8,x8,#0xee0 | `FALL_THROUGH`
<a id="insn-00bdebb8"></a> `00bdebb8` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bdebbc"></a> `00bdebbc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdebc0"></a> `00bdebc0` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdebc4"></a> `00bdebc4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdeb8c`](#insn-00bdeb8c) 範囲 `[['00bdeb8c', '00bdeba3']]`
  - `CONDITIONAL_JUMP` [`00bdeba0`](#insn-00bdeba0) → [`00bdebb0`](#insn-00bdebb0)
  - `FALL_THROUGH` [`00bdeba0`](#insn-00bdeba0) → [`00bdeba4`](#insn-00bdeba4)
- ブロック [`00bdeba4`](#insn-00bdeba4) 範囲 `[['00bdeba4', '00bdebaf']]`
  - `FALL_THROUGH` [`00bdebac`](#insn-00bdebac) → [`00bdebb0`](#insn-00bdebb0)
- ブロック [`00bdebb0`](#insn-00bdebb0) 範囲 `[['00bdebb0', '00bdebc7']]`

## 命令位置別の参照

- [`00bdeb8c`](#insn-00bdeb8c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeb90`](#insn-00bdeb90) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeba0`](#insn-00bdeba0) → [`00bdebb0`](#insn-00bdebb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeba8`](#insn-00bdeba8) → `002a961a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdebac`](#insn-00bdebac) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bdebb8`](#insn-00bdebb8) → `01127ee0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdebbc`](#insn-00bdebbc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdeb8c`](#insn-00bdeb8c)

~~~json
{
  "source": "00bdeb8c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeb90`](#insn-00bdeb90)

~~~json
{
  "source": "00bdeb90",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeba0`](#insn-00bdeba0)

~~~json
{
  "source": "00bdeba0",
  "target": "00bdebb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeba8`](#insn-00bdeba8)

~~~json
{
  "source": "00bdeba8",
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
- 参照命令 [`00bdebac`](#insn-00bdebac)

~~~json
{
  "source": "00bdebac",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdebb8`](#insn-00bdebb8)

~~~json
{
  "source": "00bdebb8",
  "target": "01127ee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdebbc`](#insn-00bdebbc)

~~~json
{
  "source": "00bdebbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
