# 00aea7ec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aea724`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aea724.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-45769e8821ba3bc9446c5f6e51e95744)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aea830`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea830.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0063.md#compare-2fe1b17b888440380cce8301e002c96b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aea7ec",
  "name": "_ZN8firebase4util4file11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2417ebbd3b90ab5e11daa1d3bc8270dec7dbd47d9e3d0ae212a522abfb9945c6",
  "source_text_sha256": "2417ebbd3b90ab5e11daa1d3bc8270dec7dbd47d9e3d0ae212a522abfb9945c6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aea7ec",
        "00aea827"
      ]
    ],
    "bytes_sha256": "9a40a449d59779b0c65d3f3b0d766098d086c8c7d4fe038b9949bcce45385472",
    "instruction_count": 15,
    "instruction_bytes": 60,
    "body_bytes": 60,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bde640](../00bde/00bde640.md)

## 呼び出し先

- [00bde130](../00bde/00bde130.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 204 bytes

~~~c

undefined8 _ZN8firebase4util4file11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (7 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return (&DAT_010a07a0)[param_1];
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aea7ec"></a> `00aea7ec` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aea7f0"></a> `00aea7f0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aea7f4"></a> `00aea7f4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aea7f8"></a> `00aea7f8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00aea7fc"></a> `00aea7fc` | `1f 20 00 71` | cmp w0,#0x8 | `FALL_THROUGH`
<a id="insn-00aea800"></a> `00aea800` | `8b 00 00 54` | b.lt 0x00aea810 | `CONDITIONAL_JUMP`
<a id="insn-00aea804"></a> `00aea804` | `60 bd ff d0` | adrp x0,0x298000 | `FALL_THROUGH`
<a id="insn-00aea808"></a> `00aea808` | `00 50 17 91` | add x0,x0,#0x5d4 | `FALL_THROUGH`
<a id="insn-00aea80c"></a> `00aea80c` | `49 ce 03 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00aea810"></a> `00aea810` | `a8 2d 00 d0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aea814"></a> `00aea814` | `08 81 1e 91` | add x8,x8,#0x7a0 | `FALL_THROUGH`
<a id="insn-00aea818"></a> `00aea818` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00aea81c"></a> `00aea81c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aea820"></a> `00aea820` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aea824"></a> `00aea824` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aea7ec`](#insn-00aea7ec) 範囲 `[['00aea7ec', '00aea803']]`
  - `CONDITIONAL_JUMP` [`00aea800`](#insn-00aea800) → [`00aea810`](#insn-00aea810)
  - `FALL_THROUGH` [`00aea800`](#insn-00aea800) → [`00aea804`](#insn-00aea804)
- ブロック [`00aea804`](#insn-00aea804) 範囲 `[['00aea804', '00aea80f']]`
  - `FALL_THROUGH` [`00aea80c`](#insn-00aea80c) → [`00aea810`](#insn-00aea810)
- ブロック [`00aea810`](#insn-00aea810) 範囲 `[['00aea810', '00aea827']]`

## 命令位置別の参照

- [`00aea7ec`](#insn-00aea7ec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea7f0`](#insn-00aea7f0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea800`](#insn-00aea800) → [`00aea810`](#insn-00aea810) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea808`](#insn-00aea808) → `002985d4`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aea80c`](#insn-00aea80c) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00aea818`](#insn-00aea818) → `010a07a0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aea81c`](#insn-00aea81c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aea7ec`](#insn-00aea7ec)

~~~json
{
  "source": "00aea7ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea7f0`](#insn-00aea7f0)

~~~json
{
  "source": "00aea7f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea800`](#insn-00aea800)

~~~json
{
  "source": "00aea800",
  "target": "00aea810",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea808`](#insn-00aea808)

~~~json
{
  "source": "00aea808",
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
- 参照命令 [`00aea80c`](#insn-00aea80c)

~~~json
{
  "source": "00aea80c",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea818`](#insn-00aea818)

~~~json
{
  "source": "00aea818",
  "target": "010a07a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a07a0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aea81c`](#insn-00aea81c)

~~~json
{
  "source": "00aea81c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
