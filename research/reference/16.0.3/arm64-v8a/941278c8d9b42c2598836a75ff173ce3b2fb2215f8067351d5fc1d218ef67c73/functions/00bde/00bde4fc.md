# 00bde4fc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdd508`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd508.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-9e17a866b69558195ceb60f669d6bf29)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bde4fc",
  "name": "_ZN8firebase4auth4user10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "56d58e0d8715714418e8af134067219f6185da3cc886bff22e6320223af023e0",
  "source_text_sha256": "56d58e0d8715714418e8af134067219f6185da3cc886bff22e6320223af023e0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bde4fc",
        "00bde537"
      ]
    ],
    "bytes_sha256": "aecaee686f1bbe01944d63a4942493b63e74fcae1d75640b59686d62cbed17f2",
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

## 疑似コード / UTF-8 227 bytes

~~~c

undefined8 _ZN8firebase4auth4user10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_01127e68 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bde4fc"></a> `00bde4fc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bde500"></a> `00bde500` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bde504"></a> `00bde504` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bde508"></a> `00bde508` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bde50c"></a> `00bde50c` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bde510"></a> `00bde510` | `8b 00 00 54` | b.lt 0x00bde520 | `CONDITIONAL_JUMP`
<a id="insn-00bde514"></a> `00bde514` | `40 b6 ff f0` | adrp x0,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bde518"></a> `00bde518` | `00 68 18 91` | add x0,x0,#0x61a | `FALL_THROUGH`
<a id="insn-00bde51c"></a> `00bde51c` | `e1 f6 01 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bde520"></a> `00bde520` | `48 2a 00 b0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bde524"></a> `00bde524` | `08 a1 39 91` | add x8,x8,#0xe68 | `FALL_THROUGH`
<a id="insn-00bde528"></a> `00bde528` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bde52c"></a> `00bde52c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bde530"></a> `00bde530` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bde534"></a> `00bde534` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bde4fc`](#insn-00bde4fc) 範囲 `[['00bde4fc', '00bde513']]`
  - `CONDITIONAL_JUMP` [`00bde510`](#insn-00bde510) → [`00bde520`](#insn-00bde520)
  - `FALL_THROUGH` [`00bde510`](#insn-00bde510) → [`00bde514`](#insn-00bde514)
- ブロック [`00bde514`](#insn-00bde514) 範囲 `[['00bde514', '00bde51f']]`
  - `FALL_THROUGH` [`00bde51c`](#insn-00bde51c) → [`00bde520`](#insn-00bde520)
- ブロック [`00bde520`](#insn-00bde520) 範囲 `[['00bde520', '00bde537']]`

## 命令位置別の参照

- [`00bde4fc`](#insn-00bde4fc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde500`](#insn-00bde500) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde510`](#insn-00bde510) → [`00bde520`](#insn-00bde520) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde518`](#insn-00bde518) → `002a961a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bde51c`](#insn-00bde51c) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bde528`](#insn-00bde528) → `01127e68`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde52c`](#insn-00bde52c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bde4fc`](#insn-00bde4fc)

~~~json
{
  "source": "00bde4fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde500`](#insn-00bde500)

~~~json
{
  "source": "00bde500",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde510`](#insn-00bde510)

~~~json
{
  "source": "00bde510",
  "target": "00bde520",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde518`](#insn-00bde518)

~~~json
{
  "source": "00bde518",
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
- 参照命令 [`00bde51c`](#insn-00bde51c)

~~~json
{
  "source": "00bde51c",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bde528`](#insn-00bde528)

~~~json
{
  "source": "00bde528",
  "target": "01127e68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde52c`](#insn-00bde52c)

~~~json
{
  "source": "00bde52c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
