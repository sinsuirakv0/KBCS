# 00bcd5fc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcc608`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcc608.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-6424a08b0381b9ce8cdc5b58008cf1ad)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcd5fc",
  "name": "_ZN8firebase4auth4auth11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a5983696bb4e8680ac2b075f1a03802ad7733ff143fef46bc64d4c9b42f41657",
  "source_text_sha256": "a5983696bb4e8680ac2b075f1a03802ad7733ff143fef46bc64d4c9b42f41657",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcd5fc",
        "00bcd637"
      ]
    ],
    "bytes_sha256": "6cb05530ec7d93f34c8665160887369c60698ef4dbf660fc93af4b275ed5ec77",
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

## 疑似コード / UTF-8 2404 bytes

~~~c

undefined8 _ZN8firebase4auth4auth11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (0x11 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
                    /* try { // try from 00bcd634 to 00ccd79b has its CatchHandler @ 00bcd634
                       catch() { ... } // from try @ 00bcd634 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcd7c0 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcd828 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcd904 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcd9d0 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcdaa0 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcdb6c with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcdc38 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcdca0 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcdd7c with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcde48 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcdf0c with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcdfdc with catch @ 00bcd634
                       catch() { ... } // from try @ 00bce0f8 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bce1d0 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bce3a0 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bce468 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bce5c8 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bce97c with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcec20 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcef18 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcf024 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcf124 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcf234 with catch @ 00bcd634
                       catch() { ... } // from try @ 00bcf2a0 with catch @ 00bcd634 */
  return (&DAT_011277f8)[param_1];
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcd5fc"></a> `00bcd5fc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcd600"></a> `00bcd600` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcd604"></a> `00bcd604` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcd608"></a> `00bcd608` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bcd60c"></a> `00bcd60c` | `1f 48 00 71` | cmp w0,#0x12 | `FALL_THROUGH`
<a id="insn-00bcd610"></a> `00bcd610` | `8b 00 00 54` | b.lt 0x00bcd620 | `CONDITIONAL_JUMP`
<a id="insn-00bcd614"></a> `00bcd614` | `c0 b6 ff f0` | adrp x0,0x2a8000 | `FALL_THROUGH`
<a id="insn-00bcd618"></a> `00bcd618` | `00 8c 11 91` | add x0,x0,#0x463 | `FALL_THROUGH`
<a id="insn-00bcd61c"></a> `00bcd61c` | `a1 3a 02 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcd620"></a> `00bcd620` | `c8 2a 00 d0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bcd624"></a> `00bcd624` | `08 e1 1f 91` | add x8,x8,#0x7f8 | `FALL_THROUGH`
<a id="insn-00bcd628"></a> `00bcd628` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bcd62c"></a> `00bcd62c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcd630"></a> `00bcd630` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcd634"></a> `00bcd634` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcd5fc`](#insn-00bcd5fc) 範囲 `[['00bcd5fc', '00bcd613']]`
  - `CONDITIONAL_JUMP` [`00bcd610`](#insn-00bcd610) → [`00bcd620`](#insn-00bcd620)
  - `FALL_THROUGH` [`00bcd610`](#insn-00bcd610) → [`00bcd614`](#insn-00bcd614)
- ブロック [`00bcd614`](#insn-00bcd614) 範囲 `[['00bcd614', '00bcd61f']]`
  - `FALL_THROUGH` [`00bcd61c`](#insn-00bcd61c) → [`00bcd620`](#insn-00bcd620)
- ブロック [`00bcd620`](#insn-00bcd620) 範囲 `[['00bcd620', '00bcd633']]`
  - `FALL_THROUGH` [`00bcd630`](#insn-00bcd630) → [`00bcd634`](#insn-00bcd634)
- ブロック [`00bcd634`](#insn-00bcd634) 範囲 `[['00bcd634', '00bcd637']]`

## 命令位置別の参照

- [`00bcd5fc`](#insn-00bcd5fc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd600`](#insn-00bcd600) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd610`](#insn-00bcd610) → [`00bcd620`](#insn-00bcd620) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd618`](#insn-00bcd618) → `002a8463`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcd61c`](#insn-00bcd61c) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bcd628`](#insn-00bcd628) → `011277f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcd62c`](#insn-00bcd62c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcd5fc`](#insn-00bcd5fc)

~~~json
{
  "source": "00bcd5fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd600`](#insn-00bcd600)

~~~json
{
  "source": "00bcd600",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd610`](#insn-00bcd610)

~~~json
{
  "source": "00bcd610",
  "target": "00bcd620",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd618`](#insn-00bcd618)

~~~json
{
  "source": "00bcd618",
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
- 参照命令 [`00bcd61c`](#insn-00bcd61c)

~~~json
{
  "source": "00bcd61c",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd628`](#insn-00bcd628)

~~~json
{
  "source": "00bcd628",
  "target": "011277f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011277f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcd62c`](#insn-00bcd62c)

~~~json
{
  "source": "00bcd62c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
