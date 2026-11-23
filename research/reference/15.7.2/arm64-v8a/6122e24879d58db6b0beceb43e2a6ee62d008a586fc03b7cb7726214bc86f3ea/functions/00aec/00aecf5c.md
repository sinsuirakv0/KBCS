# 00aecf5c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aed024`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed024.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-f7e51882f7ea6fcca2d3ea06959fed6a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aecf5c",
  "name": "_ZN8firebase4util3set11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "00192ea0942ea6a740fe855789d8a01bc509ea7fa31d1df2af701ac5c3c0b0ef",
  "source_text_sha256": "00192ea0942ea6a740fe855789d8a01bc509ea7fa31d1df2af701ac5c3c0b0ef",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aecf5c",
        "00aecf97"
      ]
    ],
    "bytes_sha256": "7f4ecb3b9cfc7fde57c8e4a60820cd52e02b933cbac303de0788ea86cce695f3",
    "instruction_count": 15,
    "instruction_bytes": 60,
    "body_bytes": 60,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bde580](../00bde/00bde580.md)

## 呼び出し先

- [00bde080](../00bde/00bde080.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 203 bytes

~~~c

undefined8 _ZN8firebase4util3set11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return (&DAT_010a08d8)[param_1];
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aecf5c"></a> `00aecf5c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aecf60"></a> `00aecf60` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecf64"></a> `00aecf64` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aecf68"></a> `00aecf68` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00aecf6c"></a> `00aecf6c` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aecf70"></a> `00aecf70` | `8b 00 00 54` | b.lt 0x00aecf80 | `CONDITIONAL_JUMP`
<a id="insn-00aecf74"></a> `00aecf74` | `60 bd ff 90` | adrp x0,0x298000 | `FALL_THROUGH`
<a id="insn-00aecf78"></a> `00aecf78` | `00 1c 15 91` | add x0,x0,#0x547 | `FALL_THROUGH`
<a id="insn-00aecf7c"></a> `00aecf7c` | `41 c4 03 94` | bl 0x00bde080 | `UNCONDITIONAL_CALL`
<a id="insn-00aecf80"></a> `00aecf80` | `a8 2d 00 90` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecf84"></a> `00aecf84` | `08 61 23 91` | add x8,x8,#0x8d8 | `FALL_THROUGH`
<a id="insn-00aecf88"></a> `00aecf88` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00aecf8c"></a> `00aecf8c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecf90"></a> `00aecf90` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aecf94"></a> `00aecf94` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aecf5c`](#insn-00aecf5c) 範囲 `[['00aecf5c', '00aecf73']]`
  - `CONDITIONAL_JUMP` [`00aecf70`](#insn-00aecf70) → [`00aecf80`](#insn-00aecf80)
  - `FALL_THROUGH` [`00aecf70`](#insn-00aecf70) → [`00aecf74`](#insn-00aecf74)
- ブロック [`00aecf74`](#insn-00aecf74) 範囲 `[['00aecf74', '00aecf7f']]`
  - `FALL_THROUGH` [`00aecf7c`](#insn-00aecf7c) → [`00aecf80`](#insn-00aecf80)
- ブロック [`00aecf80`](#insn-00aecf80) 範囲 `[['00aecf80', '00aecf97']]`

## 命令位置別の参照

- [`00aecf5c`](#insn-00aecf5c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecf60`](#insn-00aecf60) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecf70`](#insn-00aecf70) → [`00aecf80`](#insn-00aecf80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecf78`](#insn-00aecf78) → `00298547`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aecf7c`](#insn-00aecf7c) → [`00bde080`](../00bde/00bde080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde080` · 推定シンボル `None` · 推定型 `None`
- [`00aecf88`](#insn-00aecf88) → `010a08d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecf8c`](#insn-00aecf8c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aecf5c`](#insn-00aecf5c)

~~~json
{
  "source": "00aecf5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecf60`](#insn-00aecf60)

~~~json
{
  "source": "00aecf60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecf70`](#insn-00aecf70)

~~~json
{
  "source": "00aecf70",
  "target": "00aecf80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecf78`](#insn-00aecf78)

~~~json
{
  "source": "00aecf78",
  "target": "00298547",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00298547",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "6d6574686f64203c206b4d6574686f64436f756e7400",
  "capture_start": "00298547",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aecf7c`](#insn-00aecf7c)

~~~json
{
  "source": "00aecf7c",
  "target": "00bde080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aecf88`](#insn-00aecf88)

~~~json
{
  "source": "00aecf88",
  "target": "010a08d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecf8c`](#insn-00aecf8c)

~~~json
{
  "source": "00aecf8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
