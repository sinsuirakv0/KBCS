# 00aea8dc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aea898`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea898.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0063.md#compare-5626a7c5946d36e6938e77327553c64c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4a660`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a660.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0058.md#compare-15b03090b3bfafe39dec0439f8d40b5e)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aea8dc",
  "name": "_ZN8firebase4util4file10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e50d27dc4085eb5516a15895a6aa1eb4f74197d0f341ba5eb1459b69e16b14c7",
  "source_text_sha256": "e50d27dc4085eb5516a15895a6aa1eb4f74197d0f341ba5eb1459b69e16b14c7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aea8dc",
        "00aea917"
      ]
    ],
    "bytes_sha256": "bc9a63d2f19f0189a08a0f25c1d10586228c6f9a6815ab0eb2113f0e98733127",
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

- [00bde180](../00bde/00bde180.md)

## 関連文字列（未確認候補）

~~~text
"field < kFieldCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 227 bytes

~~~c

undefined8 _ZN8firebase4util4file10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_010a0820 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aea8dc"></a> `00aea8dc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aea8e0"></a> `00aea8e0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aea8e4"></a> `00aea8e4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aea8e8"></a> `00aea8e8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00aea8ec"></a> `00aea8ec` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aea8f0"></a> `00aea8f0` | `8b 00 00 54` | b.lt 0x00aea900 | `CONDITIONAL_JUMP`
<a id="insn-00aea8f4"></a> `00aea8f4` | `60 bd ff f0` | adrp x0,0x299000 | `FALL_THROUGH`
<a id="insn-00aea8f8"></a> `00aea8f8` | `00 c8 17 91` | add x0,x0,#0x5f2 | `FALL_THROUGH`
<a id="insn-00aea8fc"></a> `00aea8fc` | `21 ce 03 94` | bl 0x00bde180 | `UNCONDITIONAL_CALL`
<a id="insn-00aea900"></a> `00aea900` | `a8 2d 00 d0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aea904"></a> `00aea904` | `08 81 20 91` | add x8,x8,#0x820 | `FALL_THROUGH`
<a id="insn-00aea908"></a> `00aea908` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00aea90c"></a> `00aea90c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aea910"></a> `00aea910` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aea914"></a> `00aea914` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aea8dc`](#insn-00aea8dc) 範囲 `[['00aea8dc', '00aea8f3']]`
  - `CONDITIONAL_JUMP` [`00aea8f0`](#insn-00aea8f0) → [`00aea900`](#insn-00aea900)
  - `FALL_THROUGH` [`00aea8f0`](#insn-00aea8f0) → [`00aea8f4`](#insn-00aea8f4)
- ブロック [`00aea8f4`](#insn-00aea8f4) 範囲 `[['00aea8f4', '00aea8ff']]`
  - `FALL_THROUGH` [`00aea8fc`](#insn-00aea8fc) → [`00aea900`](#insn-00aea900)
- ブロック [`00aea900`](#insn-00aea900) 範囲 `[['00aea900', '00aea917']]`

## 命令位置別の参照

- [`00aea8dc`](#insn-00aea8dc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea8e0`](#insn-00aea8e0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea8f0`](#insn-00aea8f0) → [`00aea900`](#insn-00aea900) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea8f8`](#insn-00aea8f8) → `002995f2`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aea8fc`](#insn-00aea8fc) → [`00bde180`](../00bde/00bde180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde180` · 推定シンボル `None` · 推定型 `None`
- [`00aea908`](#insn-00aea908) → `010a0820`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea90c`](#insn-00aea90c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aea8dc`](#insn-00aea8dc)

~~~json
{
  "source": "00aea8dc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea8e0`](#insn-00aea8e0)

~~~json
{
  "source": "00aea8e0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea8f0`](#insn-00aea8f0)

~~~json
{
  "source": "00aea8f0",
  "target": "00aea900",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea8f8`](#insn-00aea8f8)

~~~json
{
  "source": "00aea8f8",
  "target": "002995f2",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002995f2",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6669656c64203c206b4669656c64436f756e7400",
  "capture_start": "002995f2",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aea8fc`](#insn-00aea8fc)

~~~json
{
  "source": "00aea8fc",
  "target": "00bde180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aea908`](#insn-00aea908)

~~~json
{
  "source": "00aea908",
  "target": "010a0820",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea90c`](#insn-00aea90c)

~~~json
{
  "source": "00aea90c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
