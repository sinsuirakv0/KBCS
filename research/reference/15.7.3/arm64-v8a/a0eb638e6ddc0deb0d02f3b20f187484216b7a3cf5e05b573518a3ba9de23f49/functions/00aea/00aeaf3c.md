# 00aeaf3c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aeae74`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeae74.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-9d16e55d411c5d0e266d2d66904c5373)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aeaf80`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaf80.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-7ead54c341c91ac8dba6545c3094b3f8)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeaf3c",
  "name": "_ZN8firebase4util8hash_map11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5bac7bb43a6c0af641eb42557a79c9cc8a07d69b96d5cbcbcd7c1d9924f1fc29",
  "source_text_sha256": "5bac7bb43a6c0af641eb42557a79c9cc8a07d69b96d5cbcbcd7c1d9924f1fc29",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeaf3c",
        "00aeaf77"
      ]
    ],
    "bytes_sha256": "74910af12102725adcdcc02d2fc8d18d45286a6f4be7ba98cdf018a23668fa17",
    "instruction_count": 15,
    "instruction_bytes": 60,
    "body_bytes": 60,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bde0e0](../00bde/00bde0e0.md)

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

undefined8 _ZN8firebase4util8hash_map11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return (&DAT_010a0820)[param_1];
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeaf3c"></a> `00aeaf3c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeaf40"></a> `00aeaf40` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeaf44"></a> `00aeaf44` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aeaf48"></a> `00aeaf48` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00aeaf4c"></a> `00aeaf4c` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aeaf50"></a> `00aeaf50` | `8b 00 00 54` | b.lt 0x00aeaf60 | `CONDITIONAL_JUMP`
<a id="insn-00aeaf54"></a> `00aeaf54` | `60 bd ff d0` | adrp x0,0x298000 | `FALL_THROUGH`
<a id="insn-00aeaf58"></a> `00aeaf58` | `00 50 17 91` | add x0,x0,#0x5d4 | `FALL_THROUGH`
<a id="insn-00aeaf5c"></a> `00aeaf5c` | `75 cc 03 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00aeaf60"></a> `00aeaf60` | `a8 2d 00 d0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeaf64"></a> `00aeaf64` | `08 81 20 91` | add x8,x8,#0x820 | `FALL_THROUGH`
<a id="insn-00aeaf68"></a> `00aeaf68` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00aeaf6c"></a> `00aeaf6c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeaf70"></a> `00aeaf70` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeaf74"></a> `00aeaf74` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeaf3c`](#insn-00aeaf3c) 範囲 `[['00aeaf3c', '00aeaf53']]`
  - `CONDITIONAL_JUMP` [`00aeaf50`](#insn-00aeaf50) → [`00aeaf60`](#insn-00aeaf60)
  - `FALL_THROUGH` [`00aeaf50`](#insn-00aeaf50) → [`00aeaf54`](#insn-00aeaf54)
- ブロック [`00aeaf54`](#insn-00aeaf54) 範囲 `[['00aeaf54', '00aeaf5f']]`
  - `FALL_THROUGH` [`00aeaf5c`](#insn-00aeaf5c) → [`00aeaf60`](#insn-00aeaf60)
- ブロック [`00aeaf60`](#insn-00aeaf60) 範囲 `[['00aeaf60', '00aeaf77']]`

## 命令位置別の参照

- [`00aeaf3c`](#insn-00aeaf3c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf40`](#insn-00aeaf40) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf50`](#insn-00aeaf50) → [`00aeaf60`](#insn-00aeaf60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf58`](#insn-00aeaf58) → `002985d4`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeaf5c`](#insn-00aeaf5c) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf68`](#insn-00aeaf68) → `010a0820`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeaf6c`](#insn-00aeaf6c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeaf3c`](#insn-00aeaf3c)

~~~json
{
  "source": "00aeaf3c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf40`](#insn-00aeaf40)

~~~json
{
  "source": "00aeaf40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf50`](#insn-00aeaf50)

~~~json
{
  "source": "00aeaf50",
  "target": "00aeaf60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf58`](#insn-00aeaf58)

~~~json
{
  "source": "00aeaf58",
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
- 参照命令 [`00aeaf5c`](#insn-00aeaf5c)

~~~json
{
  "source": "00aeaf5c",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeaf68`](#insn-00aeaf68)

~~~json
{
  "source": "00aeaf68",
  "target": "010a0820",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0820",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeaf6c`](#insn-00aeaf6c)

~~~json
{
  "source": "00aeaf6c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
