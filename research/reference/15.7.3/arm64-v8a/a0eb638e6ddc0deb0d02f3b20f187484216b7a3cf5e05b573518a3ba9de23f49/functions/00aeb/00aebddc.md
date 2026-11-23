# 00aebddc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aebd14`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aebd14.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-bb0e01143c329e584402fe5f8f5f82d6)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aebe20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebe20.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-d805e4aecc6831e495590eac3a50327a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebddc",
  "name": "_ZN8firebase4util8iterator11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0075e307bd3b35f20292fd9e43fe5488bb2cc4710cd464fc362b5c849a86a73d",
  "source_text_sha256": "0075e307bd3b35f20292fd9e43fe5488bb2cc4710cd464fc362b5c849a86a73d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aebddc",
        "00aebe17"
      ]
    ],
    "bytes_sha256": "d95743663b15804b9ab3530c477c7a85e97789101c63908ce8c1b3f4a3dc4ab5",
    "instruction_count": 15,
    "instruction_bytes": 60,
    "body_bytes": 60,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bde690](../00bde/00bde690.md)

## 呼び出し先

- [00bde130](../00bde/00bde130.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 208 bytes

~~~c

undefined8 _ZN8firebase4util8iterator11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (1 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return (&DAT_010a08c8)[param_1];
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aebddc"></a> `00aebddc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aebde0"></a> `00aebde0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebde4"></a> `00aebde4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aebde8"></a> `00aebde8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00aebdec"></a> `00aebdec` | `1f 08 00 71` | cmp w0,#0x2 | `FALL_THROUGH`
<a id="insn-00aebdf0"></a> `00aebdf0` | `8b 00 00 54` | b.lt 0x00aebe00 | `CONDITIONAL_JUMP`
<a id="insn-00aebdf4"></a> `00aebdf4` | `60 bd ff b0` | adrp x0,0x298000 | `FALL_THROUGH`
<a id="insn-00aebdf8"></a> `00aebdf8` | `00 50 17 91` | add x0,x0,#0x5d4 | `FALL_THROUGH`
<a id="insn-00aebdfc"></a> `00aebdfc` | `cd c8 03 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00aebe00"></a> `00aebe00` | `a8 2d 00 b0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebe04"></a> `00aebe04` | `08 21 23 91` | add x8,x8,#0x8c8 | `FALL_THROUGH`
<a id="insn-00aebe08"></a> `00aebe08` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00aebe0c"></a> `00aebe0c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebe10"></a> `00aebe10` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aebe14"></a> `00aebe14` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aebddc`](#insn-00aebddc) 範囲 `[['00aebddc', '00aebdf3']]`
  - `CONDITIONAL_JUMP` [`00aebdf0`](#insn-00aebdf0) → [`00aebe00`](#insn-00aebe00)
  - `FALL_THROUGH` [`00aebdf0`](#insn-00aebdf0) → [`00aebdf4`](#insn-00aebdf4)
- ブロック [`00aebdf4`](#insn-00aebdf4) 範囲 `[['00aebdf4', '00aebdff']]`
  - `FALL_THROUGH` [`00aebdfc`](#insn-00aebdfc) → [`00aebe00`](#insn-00aebe00)
- ブロック [`00aebe00`](#insn-00aebe00) 範囲 `[['00aebe00', '00aebe17']]`

## 命令位置別の参照

- [`00aebddc`](#insn-00aebddc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebde0`](#insn-00aebde0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebdf0`](#insn-00aebdf0) → [`00aebe00`](#insn-00aebe00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebdf8`](#insn-00aebdf8) → `002985d4`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aebdfc`](#insn-00aebdfc) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00aebe08`](#insn-00aebe08) → `010a08c8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebe0c`](#insn-00aebe0c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aebddc`](#insn-00aebddc)

~~~json
{
  "source": "00aebddc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebde0`](#insn-00aebde0)

~~~json
{
  "source": "00aebde0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebdf0`](#insn-00aebdf0)

~~~json
{
  "source": "00aebdf0",
  "target": "00aebe00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebdf8`](#insn-00aebdf8)

~~~json
{
  "source": "00aebdf8",
  "target": "002985d4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002985d4",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "6d6574686f64203c206b4d6574686f64436f756e7400",
  "capture_start": "002985d4",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aebdfc`](#insn-00aebdfc)

~~~json
{
  "source": "00aebdfc",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebe08`](#insn-00aebe08)

~~~json
{
  "source": "00aebe08",
  "target": "010a08c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebe0c`](#insn-00aebe0c)

~~~json
{
  "source": "00aebe0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
