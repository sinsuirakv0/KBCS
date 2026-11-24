# 00b7ecac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b7ec68`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ec68.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0014.md#compare-c1f1ddb23840276139be4600992804e2)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0092.md#review-03c74b3728709e797aac26a5f00b7c00)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b7ecac",
  "name": "FUN_00b7ecac",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "934dd3d76189b3442804c12d5f04394a462b8e7dea6ab411f7c2aee5c923b20b",
  "source_text_sha256": "934dd3d76189b3442804c12d5f04394a462b8e7dea6ab411f7c2aee5c923b20b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b7ecac",
        "00b7ecd7"
      ]
    ],
    "bytes_sha256": "9dd4f01f03ec52755374674a4320f063ad71020672d3951db0f58f6054ae2ed4",
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
- [00be0ef0](../00be0/00be0ef0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 107 bytes

~~~c

void FUN_00b7ecac(void *param_1)

{
  _ZNSt6__ndk114error_categoryD2Ev();
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b7ecac"></a> `00b7ecac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00b7ecb0"></a> `00b7ecb0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b7ecb4"></a> `00b7ecb4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7ecb8"></a> `00b7ecb8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00b7ecbc"></a> `00b7ecbc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b7ecc0"></a> `00b7ecc0` | `8c 88 01 94` | bl 0x00be0ef0 | `UNCONDITIONAL_CALL`
<a id="insn-00b7ecc4"></a> `00b7ecc4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b7ecc8"></a> `00b7ecc8` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7eccc"></a> `00b7eccc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b7ecd0"></a> `00b7ecd0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00b7ecd4"></a> `00b7ecd4` | `e3 70 01 14` | b 0x00bdb060 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b7ecac`](#insn-00b7ecac) 範囲 `[['00b7ecac', '00b7ecd7']]`

## 命令位置別の参照

- [`00b7ecb0`](#insn-00b7ecb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7ecb4`](#insn-00b7ecb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7ecc0`](#insn-00b7ecc0) → [`00be0ef0`](../00be0/00be0ef0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0ef0` · 推定シンボル `None` · 推定型 `None`
- [`00b7ecc8`](#insn-00b7ecc8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7eccc`](#insn-00b7eccc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7ecd4`](#insn-00b7ecd4) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b7ecb0`](#insn-00b7ecb0)

~~~json
{
  "source": "00b7ecb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7ecb4`](#insn-00b7ecb4)

~~~json
{
  "source": "00b7ecb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7ecc0`](#insn-00b7ecc0)

~~~json
{
  "source": "00b7ecc0",
  "target": "00be0ef0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7ecc8`](#insn-00b7ecc8)

~~~json
{
  "source": "00b7ecc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7eccc`](#insn-00b7eccc)

~~~json
{
  "source": "00b7eccc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7ecd4`](#insn-00b7ecd4)

~~~json
{
  "source": "00b7ecd4",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
