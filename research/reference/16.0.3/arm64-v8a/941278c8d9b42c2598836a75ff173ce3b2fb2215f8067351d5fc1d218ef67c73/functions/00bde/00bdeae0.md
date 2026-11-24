# 00bdeae0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bddaec`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddaec.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-4f7d2190852b5db850f572e82b1bb594)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdeae0",
  "name": "_ZN8firebase4auth8metadata11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ff84f558aff1d2e66244502b064cada82f238d51e565dc460b64f1769ddee5bb",
  "source_text_sha256": "ff84f558aff1d2e66244502b064cada82f238d51e565dc460b64f1769ddee5bb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdeae0",
        "00bdeb1b"
      ]
    ],
    "bytes_sha256": "a03f8f66ed8c67ac85f541aeea4382a912342eec467c8b969b8021e00fc29dd3",
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
"method < kMethodCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 208 bytes

~~~c

undefined8 _ZN8firebase4auth8metadata11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (1 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return (&DAT_01127ed0)[param_1];
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdeae0"></a> `00bdeae0` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdeae4"></a> `00bdeae4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdeae8"></a> `00bdeae8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdeaec"></a> `00bdeaec` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bdeaf0"></a> `00bdeaf0` | `1f 08 00 71` | cmp w0,#0x2 | `FALL_THROUGH`
<a id="insn-00bdeaf4"></a> `00bdeaf4` | `8b 00 00 54` | b.lt 0x00bdeb04 | `CONDITIONAL_JUMP`
<a id="insn-00bdeaf8"></a> `00bdeaf8` | `40 b6 ff d0` | adrp x0,0x2a8000 | `FALL_THROUGH`
<a id="insn-00bdeafc"></a> `00bdeafc` | `00 8c 11 91` | add x0,x0,#0x463 | `FALL_THROUGH`
<a id="insn-00bdeb00"></a> `00bdeb00` | `68 f5 01 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdeb04"></a> `00bdeb04` | `48 2a 00 b0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdeb08"></a> `00bdeb08` | `08 41 3b 91` | add x8,x8,#0xed0 | `FALL_THROUGH`
<a id="insn-00bdeb0c"></a> `00bdeb0c` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bdeb10"></a> `00bdeb10` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdeb14"></a> `00bdeb14` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdeb18"></a> `00bdeb18` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdeae0`](#insn-00bdeae0) 範囲 `[['00bdeae0', '00bdeaf7']]`
  - `CONDITIONAL_JUMP` [`00bdeaf4`](#insn-00bdeaf4) → [`00bdeb04`](#insn-00bdeb04)
  - `FALL_THROUGH` [`00bdeaf4`](#insn-00bdeaf4) → [`00bdeaf8`](#insn-00bdeaf8)
- ブロック [`00bdeaf8`](#insn-00bdeaf8) 範囲 `[['00bdeaf8', '00bdeb03']]`
  - `FALL_THROUGH` [`00bdeb00`](#insn-00bdeb00) → [`00bdeb04`](#insn-00bdeb04)
- ブロック [`00bdeb04`](#insn-00bdeb04) 範囲 `[['00bdeb04', '00bdeb1b']]`

## 命令位置別の参照

- [`00bdeae0`](#insn-00bdeae0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeae4`](#insn-00bdeae4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeaf4`](#insn-00bdeaf4) → [`00bdeb04`](#insn-00bdeb04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeafc`](#insn-00bdeafc) → `002a8463`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdeb00`](#insn-00bdeb00) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bdeb0c`](#insn-00bdeb0c) → `01127ed0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdeb10`](#insn-00bdeb10) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdeae0`](#insn-00bdeae0)

~~~json
{
  "source": "00bdeae0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeae4`](#insn-00bdeae4)

~~~json
{
  "source": "00bdeae4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeaf4`](#insn-00bdeaf4)

~~~json
{
  "source": "00bdeaf4",
  "target": "00bdeb04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeafc`](#insn-00bdeafc)

~~~json
{
  "source": "00bdeafc",
  "target": "002a8463",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8463",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "6d6574686f64203c206b4d6574686f64436f756e7400",
  "capture_start": "002a8463",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bdeb00`](#insn-00bdeb00)

~~~json
{
  "source": "00bdeb00",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdeb0c`](#insn-00bdeb0c)

~~~json
{
  "source": "00bdeb0c",
  "target": "01127ed0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ed0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdeb10`](#insn-00bdeb10)

~~~json
{
  "source": "00bdeb10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
