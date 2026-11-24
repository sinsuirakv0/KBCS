# 00bb7dec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bb7da8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7da8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0017.md#compare-c0e04f1e7b76cf322019ba1b152fb133)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0092.md#review-2aec6e90d67173945edb29397c0bf649)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb7dec",
  "name": "FUN_00bb7dec",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "447bcb96279a9f36963ac56a3ac4843395e41d423b74a9ea123ddb6b4c05c857",
  "source_text_sha256": "447bcb96279a9f36963ac56a3ac4843395e41d423b74a9ea123ddb6b4c05c857",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bb7dec",
        "00bb7e17"
      ]
    ],
    "bytes_sha256": "5c0a51cf43d294109deaeab9123fc8265e6930b37cf322472484f34427d285c5",
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
- [00be1770](../00be1/00be1770.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 116 bytes

~~~c

void FUN_00bb7dec(void *param_1)

{
  _ZNSt6__ndk116__narrow_to_utf8ILm32EED1Ev();
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bb7dec"></a> `00bb7dec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bb7df0"></a> `00bb7df0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bb7df4"></a> `00bb7df4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb7df8"></a> `00bb7df8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bb7dfc"></a> `00bb7dfc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bb7e00"></a> `00bb7e00` | `5c a6 00 94` | bl 0x00be1770 | `UNCONDITIONAL_CALL`
<a id="insn-00bb7e04"></a> `00bb7e04` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb7e08"></a> `00bb7e08` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb7e0c"></a> `00bb7e0c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bb7e10"></a> `00bb7e10` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bb7e14"></a> `00bb7e14` | `93 8c 00 14` | b 0x00bdb060 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bb7dec`](#insn-00bb7dec) 範囲 `[['00bb7dec', '00bb7e17']]`

## 命令位置別の参照

- [`00bb7df0`](#insn-00bb7df0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb7df4`](#insn-00bb7df4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb7e00`](#insn-00bb7e00) → [`00be1770`](../00be1/00be1770.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1770` · 推定シンボル `None` · 推定型 `None`
- [`00bb7e08`](#insn-00bb7e08) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb7e0c`](#insn-00bb7e0c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb7e14`](#insn-00bb7e14) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bb7df0`](#insn-00bb7df0)

~~~json
{
  "source": "00bb7df0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb7df4`](#insn-00bb7df4)

~~~json
{
  "source": "00bb7df4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb7e00`](#insn-00bb7e00)

~~~json
{
  "source": "00bb7e00",
  "target": "00be1770",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb7e08`](#insn-00bb7e08)

~~~json
{
  "source": "00bb7e08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb7e0c`](#insn-00bb7e0c)

~~~json
{
  "source": "00bb7e0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb7e14`](#insn-00bb7e14)

~~~json
{
  "source": "00bb7e14",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
