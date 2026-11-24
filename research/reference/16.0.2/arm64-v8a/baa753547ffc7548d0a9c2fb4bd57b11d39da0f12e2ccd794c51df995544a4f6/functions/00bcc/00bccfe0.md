# 00bccfe0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bccf44`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccf44.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0011.md#compare-60b8190d917505ee5b7839b22ccf99fa)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bcdfd4`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcd/00bcdfd4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-eae934b5d8d87332273a2e507365a9c8)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bccfe0",
  "name": "_ZN8firebase4auth21jni_id_token_listener11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "818b964c6a1886c4258a06297e6642b1623a1855665db2ccab2e217b4673c033",
  "source_text_sha256": "818b964c6a1886c4258a06297e6642b1623a1855665db2ccab2e217b4673c033",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bccfe0",
        "00bcd01b"
      ]
    ],
    "bytes_sha256": "fa28002561c2ec091b48d143a5c7ce349848f073d837a317b19a6fef902374fa",
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

- [00c5b0d0](../00c5b/00c5b0d0.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 319 bytes

~~~c

undefined8 _ZN8firebase4auth21jni_id_token_listener11GetMethodIdENS1_6MethodE(uint param_1)

{
                    /* try { // try from 00bccfe8 to 00ccd0f7 has its CatchHandler @ 00bcc640 */
  if (1 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return (&DAT_01126928)[param_1];
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bccfe0"></a> `00bccfe0` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bccfe4"></a> `00bccfe4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccfe8"></a> `00bccfe8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bccfec"></a> `00bccfec` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bccff0"></a> `00bccff0` | `1f 08 00 71` | cmp w0,#0x2 | `FALL_THROUGH`
<a id="insn-00bccff4"></a> `00bccff4` | `8b 00 00 54` | b.lt 0x00bcd004 | `CONDITIONAL_JUMP`
<a id="insn-00bccff8"></a> `00bccff8` | `e0 b6 ff 90` | adrp x0,0x2a8000 | `FALL_THROUGH`
<a id="insn-00bccffc"></a> `00bccffc` | `00 2c 0c 91` | add x0,x0,#0x30b | `FALL_THROUGH`
<a id="insn-00bcd000"></a> `00bcd000` | `34 38 02 94` | bl 0x00c5b0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcd004"></a> `00bcd004` | `c8 2a 00 b0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcd008"></a> `00bcd008` | `08 a1 24 91` | add x8,x8,#0x928 | `FALL_THROUGH`
<a id="insn-00bcd00c"></a> `00bcd00c` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bcd010"></a> `00bcd010` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcd014"></a> `00bcd014` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcd018"></a> `00bcd018` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bccfe0`](#insn-00bccfe0) 範囲 `[['00bccfe0', '00bccfe7']]`
  - `FALL_THROUGH` [`00bccfe4`](#insn-00bccfe4) → [`00bccfe8`](#insn-00bccfe8)
- ブロック [`00bccfe8`](#insn-00bccfe8) 範囲 `[['00bccfe8', '00bccff7']]`
  - `CONDITIONAL_JUMP` [`00bccff4`](#insn-00bccff4) → [`00bcd004`](#insn-00bcd004)
  - `FALL_THROUGH` [`00bccff4`](#insn-00bccff4) → [`00bccff8`](#insn-00bccff8)
- ブロック [`00bccff8`](#insn-00bccff8) 範囲 `[['00bccff8', '00bcd003']]`
  - `FALL_THROUGH` [`00bcd000`](#insn-00bcd000) → [`00bcd004`](#insn-00bcd004)
- ブロック [`00bcd004`](#insn-00bcd004) 範囲 `[['00bcd004', '00bcd01b']]`

## 命令位置別の参照

- [`00bccfe0`](#insn-00bccfe0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccfe4`](#insn-00bccfe4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccff4`](#insn-00bccff4) → [`00bcd004`](#insn-00bcd004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccffc`](#insn-00bccffc) → `002a830b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcd000`](#insn-00bcd000) → [`00c5b0d0`](../00c5b/00c5b0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bcd00c`](#insn-00bcd00c) → `01126928`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcd010`](#insn-00bcd010) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bccfe0`](#insn-00bccfe0)

~~~json
{
  "source": "00bccfe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccfe4`](#insn-00bccfe4)

~~~json
{
  "source": "00bccfe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccff4`](#insn-00bccff4)

~~~json
{
  "source": "00bccff4",
  "target": "00bcd004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccffc`](#insn-00bccffc)

~~~json
{
  "source": "00bccffc",
  "target": "002a830b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a830b",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "6d6574686f64203c206b4d6574686f64436f756e7400",
  "capture_start": "002a830b",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcd000`](#insn-00bcd000)

~~~json
{
  "source": "00bcd000",
  "target": "00c5b0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd00c`](#insn-00bcd00c)

~~~json
{
  "source": "00bcd00c",
  "target": "01126928",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126928",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcd010`](#insn-00bcd010)

~~~json
{
  "source": "00bcd010",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
