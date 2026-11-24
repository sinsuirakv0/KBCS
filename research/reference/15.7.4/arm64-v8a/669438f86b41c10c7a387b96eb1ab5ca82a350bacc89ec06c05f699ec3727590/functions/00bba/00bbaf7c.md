# 00bbaf7c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbaf38`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaf38.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-b97cf3b0a9ab48f74f4cd30895ff2092)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c379c4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c379c4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0077.md#compare-0f912a14040894b38db8e38f49bfeb2f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbaf7c",
  "name": "_ZNSt12domain_errorD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d1d98d512c30376917141bf6b8a9822a88916f2e591a68a8926dbc279596f323",
  "source_text_sha256": "d1d98d512c30376917141bf6b8a9822a88916f2e591a68a8926dbc279596f323",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbaf7c",
        "00bbafa7"
      ]
    ],
    "bytes_sha256": "e00cde9a363e53de15c31cb4a43dd8d90ec44d645f4c0a75fb19e3854acb8b7d",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00be1e70](../00be1/00be1e70.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 108 bytes

~~~c

void _ZNSt12domain_errorD0Ev(void *param_1)

{
  _ZNSt11logic_errorD1Ev();
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbaf7c"></a> `00bbaf7c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbaf80"></a> `00bbaf80` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbaf84"></a> `00bbaf84` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbaf88"></a> `00bbaf88` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbaf8c"></a> `00bbaf8c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbaf90"></a> `00bbaf90` | `b8 9b 00 94` | bl 0x00be1e70 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaf94"></a> `00bbaf94` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbaf98"></a> `00bbaf98` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbaf9c"></a> `00bbaf9c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbafa0"></a> `00bbafa0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbafa4"></a> `00bbafa4` | `2f 80 00 14` | b 0x00bdb060 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbaf7c`](#insn-00bbaf7c) 範囲 `[['00bbaf7c', '00bbafa7']]`

## 命令位置別の参照

- [`00bbaf80`](#insn-00bbaf80) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf84`](#insn-00bbaf84) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf90`](#insn-00bbaf90) → [`00be1e70`](../00be1/00be1e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1e70` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf98`](#insn-00bbaf98) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaf9c`](#insn-00bbaf9c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbafa4`](#insn-00bbafa4) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbaf80`](#insn-00bbaf80)

~~~json
{
  "source": "00bbaf80",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf84`](#insn-00bbaf84)

~~~json
{
  "source": "00bbaf84",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf90`](#insn-00bbaf90)

~~~json
{
  "source": "00bbaf90",
  "target": "00be1e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaf98`](#insn-00bbaf98)

~~~json
{
  "source": "00bbaf98",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaf9c`](#insn-00bbaf9c)

~~~json
{
  "source": "00bbaf9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbafa4`](#insn-00bbafa4)

~~~json
{
  "source": "00bbafa4",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
