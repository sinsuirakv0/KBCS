# 00aec0bc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aec184`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec184.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-c7f731cf4dfb9f0b1097fe7615f15495)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aec0bc",
  "name": "_ZN8firebase4util4list11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1e8b2c3de0796be6c159616dda405a26eae34a9150fce61fad63093349e59fbe",
  "source_text_sha256": "1e8b2c3de0796be6c159616dda405a26eae34a9150fce61fad63093349e59fbe",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aec0bc",
        "00aec0f7"
      ]
    ],
    "bytes_sha256": "cb30d454ad8df29853cf8c9d98203575a371f41fcf459e7b211d488986d3548d",
    "instruction_count": 15,
    "instruction_bytes": 60,
    "body_bytes": 60,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bde5a0](../00bde/00bde5a0.md)

## 呼び出し先

- [00bde080](../00bde/00bde080.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 204 bytes

~~~c

undefined8 _ZN8firebase4util4list11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (2 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return (&DAT_010a0830)[param_1];
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aec0bc"></a> `00aec0bc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aec0c0"></a> `00aec0c0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aec0c4"></a> `00aec0c4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aec0c8"></a> `00aec0c8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00aec0cc"></a> `00aec0cc` | `1f 0c 00 71` | cmp w0,#0x3 | `FALL_THROUGH`
<a id="insn-00aec0d0"></a> `00aec0d0` | `8b 00 00 54` | b.lt 0x00aec0e0 | `CONDITIONAL_JUMP`
<a id="insn-00aec0d4"></a> `00aec0d4` | `60 bd ff 90` | adrp x0,0x298000 | `FALL_THROUGH`
<a id="insn-00aec0d8"></a> `00aec0d8` | `00 1c 15 91` | add x0,x0,#0x547 | `FALL_THROUGH`
<a id="insn-00aec0dc"></a> `00aec0dc` | `e9 c7 03 94` | bl 0x00bde080 | `UNCONDITIONAL_CALL`
<a id="insn-00aec0e0"></a> `00aec0e0` | `a8 2d 00 90` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aec0e4"></a> `00aec0e4` | `08 c1 20 91` | add x8,x8,#0x830 | `FALL_THROUGH`
<a id="insn-00aec0e8"></a> `00aec0e8` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00aec0ec"></a> `00aec0ec` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aec0f0"></a> `00aec0f0` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aec0f4"></a> `00aec0f4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aec0bc`](#insn-00aec0bc) 範囲 `[['00aec0bc', '00aec0d3']]`
  - `CONDITIONAL_JUMP` [`00aec0d0`](#insn-00aec0d0) → [`00aec0e0`](#insn-00aec0e0)
  - `FALL_THROUGH` [`00aec0d0`](#insn-00aec0d0) → [`00aec0d4`](#insn-00aec0d4)
- ブロック [`00aec0d4`](#insn-00aec0d4) 範囲 `[['00aec0d4', '00aec0df']]`
  - `FALL_THROUGH` [`00aec0dc`](#insn-00aec0dc) → [`00aec0e0`](#insn-00aec0e0)
- ブロック [`00aec0e0`](#insn-00aec0e0) 範囲 `[['00aec0e0', '00aec0f7']]`

## 命令位置別の参照

- [`00aec0bc`](#insn-00aec0bc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec0c0`](#insn-00aec0c0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec0d0`](#insn-00aec0d0) → [`00aec0e0`](#insn-00aec0e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec0d8`](#insn-00aec0d8) → `00298547`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aec0dc`](#insn-00aec0dc) → [`00bde080`](../00bde/00bde080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde080` · 推定シンボル `None` · 推定型 `None`
- [`00aec0e8`](#insn-00aec0e8) → `010a0830`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aec0ec`](#insn-00aec0ec) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aec0bc`](#insn-00aec0bc)

~~~json
{
  "source": "00aec0bc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec0c0`](#insn-00aec0c0)

~~~json
{
  "source": "00aec0c0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec0d0`](#insn-00aec0d0)

~~~json
{
  "source": "00aec0d0",
  "target": "00aec0e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec0d8`](#insn-00aec0d8)

~~~json
{
  "source": "00aec0d8",
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
- 参照命令 [`00aec0dc`](#insn-00aec0dc)

~~~json
{
  "source": "00aec0dc",
  "target": "00bde080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec0e8`](#insn-00aec0e8)

~~~json
{
  "source": "00aec0e8",
  "target": "010a0830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0830",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aec0ec`](#insn-00aec0ec)

~~~json
{
  "source": "00aec0ec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
