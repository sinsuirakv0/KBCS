# 00bd4fbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bd4f78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4f78.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/machine_only_observed-0044.md#compare-0f572697596a003353432e12fbdfa088)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c51a04`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51a04.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/machine_only_observed-0019.md#compare-d52570cbcd2853ca66573c31b60d1aad)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd4fbc",
  "name": "_ZdaPvSt11align_val_t",
  "size": 8,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cb1d7e0ec5098b7df0ab981a2e64ed4cdae378704644dd6f7f59f498049ac8c5",
  "source_text_sha256": "cb1d7e0ec5098b7df0ab981a2e64ed4cdae378704644dd6f7f59f498049ac8c5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd4fbc",
        "00bd4fc3"
      ]
    ],
    "bytes_sha256": "30fd76aaca56c65b66f02e1cc6bef3b6ecb4e542797f7569a542cab8496dfd7b",
    "instruction_count": 2,
    "instruction_bytes": 8,
    "body_bytes": 8,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be1f40](../00be1/00be1f40.md)

## 呼び出し先

- [00be1f30](../00be1/00be1f30.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 167 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void _ZdaPvSt11align_val_t(void *__ptr)

{
  _ZdlPvSt11align_val_t(__ptr);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd4fbc"></a> `00bd4fbc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bd4fc0"></a> `00bd4fc0` | `dc 33 00 14` | b 0x00be1f30 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd4fbc`](#insn-00bd4fbc) 範囲 `[['00bd4fbc', '00bd4fc3']]`

## 命令位置別の参照

- [`00bd4fc0`](#insn-00bd4fc0) → [`00be1f30`](../00be1/00be1f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1f30` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd4fc0`](#insn-00bd4fc0)

~~~json
{
  "source": "00bd4fc0",
  "target": "00be1f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
