# 00afb6ec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afb6a8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb6a8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/machine_only_observed-0042.md#compare-5fd098ccfed895467d1e205fec47c331)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b5b470`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b470.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/machine_only_observed-0017.md#compare-0ae1656fe8e076133fb967e1df4975ed)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afb6ec",
  "name": "_ZN8firebase6LoggerD0Ev",
  "size": 4,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "897aa8a80b398314ac0658372894a0b3242473700975b07465f6b6911d750d50",
  "source_text_sha256": "897aa8a80b398314ac0658372894a0b3242473700975b07465f6b6911d750d50",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afb6ec",
        "00afb6ef"
      ]
    ],
    "bytes_sha256": "7fd60a97e3d3e0c2886463d747e0b046ee56ba09a542318a0718ca02bea373d9",
    "instruction_count": 1,
    "instruction_bytes": 4,
    "body_bytes": 4,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 173 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void _ZN8firebase6LoggerD0Ev(void *__ptr)

{
  (*(code *)PTR__ZdlPv_00c1c0e8)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afb6ec"></a> `00afb6ec` | `5d 7e 03 14` | b 0x00bdb060 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00afb6ec`](#insn-00afb6ec) 範囲 `[['00afb6ec', '00afb6ef']]`
  - `UNCONDITIONAL_JUMP` [`00afb6ec`](#insn-00afb6ec) → [`00bdb060`](../00bdb/00bdb060.md)

## 命令位置別の参照

- [`00afb6ec`](#insn-00afb6ec) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afb6ec`](#insn-00afb6ec)

~~~json
{
  "source": "00afb6ec",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
