# 00aeaacc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aeab94`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeab94.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-55102232df1a3d2b04a03ca5c0279d7c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeaacc",
  "name": "_ZN8firebase4util11float_class11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "178bcda26c310356327703ffac743be4b9551884759b3b3926091d02e02e447b",
  "source_text_sha256": "178bcda26c310356327703ffac743be4b9551884759b3b3926091d02e02e447b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeaacc",
        "00aeab07"
      ]
    ],
    "bytes_sha256": "261ecc4b13a75514053d80f17aac4c749f1d7e836c1fa695c38a8f380f78f191",
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

- [00bde080](../00bde/00bde080.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 239 bytes

~~~c

undefined8 _ZN8firebase4util11float_class11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (1 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return *(undefined8 *)(&DAT_010a0738 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeaacc"></a> `00aeaacc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeaad0"></a> `00aeaad0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeaad4"></a> `00aeaad4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aeaad8"></a> `00aeaad8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00aeaadc"></a> `00aeaadc` | `1f 08 00 71` | cmp w0,#0x2 | `FALL_THROUGH`
<a id="insn-00aeaae0"></a> `00aeaae0` | `8b 00 00 54` | b.lt 0x00aeaaf0 | `CONDITIONAL_JUMP`
<a id="insn-00aeaae4"></a> `00aeaae4` | `60 bd ff d0` | adrp x0,0x298000 | `FALL_THROUGH`
<a id="insn-00aeaae8"></a> `00aeaae8` | `00 1c 15 91` | add x0,x0,#0x547 | `FALL_THROUGH`
<a id="insn-00aeaaec"></a> `00aeaaec` | `65 cd 03 94` | bl 0x00bde080 | `UNCONDITIONAL_CALL`
<a id="insn-00aeaaf0"></a> `00aeaaf0` | `a8 2d 00 d0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeaaf4"></a> `00aeaaf4` | `08 e1 1c 91` | add x8,x8,#0x738 | `FALL_THROUGH`
<a id="insn-00aeaaf8"></a> `00aeaaf8` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00aeaafc"></a> `00aeaafc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeab00"></a> `00aeab00` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeab04"></a> `00aeab04` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeaacc`](#insn-00aeaacc) 範囲 `[['00aeaacc', '00aeaae3']]`
  - `CONDITIONAL_JUMP` [`00aeaae0`](#insn-00aeaae0) → [`00aeaaf0`](#insn-00aeaaf0)
  - `FALL_THROUGH` [`00aeaae0`](#insn-00aeaae0) → [`00aeaae4`](#insn-00aeaae4)
- ブロック [`00aeaae4`](#insn-00aeaae4) 範囲 `[['00aeaae4', '00aeaaef']]`
  - `FALL_THROUGH` [`00aeaaec`](#insn-00aeaaec) → [`00aeaaf0`](#insn-00aeaaf0)
- ブロック [`00aeaaf0`](#insn-00aeaaf0) 範囲 `[['00aeaaf0', '00aeab07']]`

## 命令位置別の参照

- [`00aeaacc`](#insn-00aeaacc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaad0`](#insn-00aeaad0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaae0`](#insn-00aeaae0) → [`00aeaaf0`](#insn-00aeaaf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaae8`](#insn-00aeaae8) → `00298547`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeaaec`](#insn-00aeaaec) → [`00bde080`](../00bde/00bde080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde080` · 推定シンボル `None` · 推定型 `None`
- [`00aeaaf8`](#insn-00aeaaf8) → `010a0738`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaafc`](#insn-00aeaafc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeaacc`](#insn-00aeaacc)

~~~json
{
  "source": "00aeaacc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaad0`](#insn-00aeaad0)

~~~json
{
  "source": "00aeaad0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaae0`](#insn-00aeaae0)

~~~json
{
  "source": "00aeaae0",
  "target": "00aeaaf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaae8`](#insn-00aeaae8)

~~~json
{
  "source": "00aeaae8",
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
- 参照命令 [`00aeaaec`](#insn-00aeaaec)

~~~json
{
  "source": "00aeaaec",
  "target": "00bde080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeaaf8`](#insn-00aeaaf8)

~~~json
{
  "source": "00aeaaf8",
  "target": "010a0738",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaafc`](#insn-00aeaafc)

~~~json
{
  "source": "00aeaafc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
