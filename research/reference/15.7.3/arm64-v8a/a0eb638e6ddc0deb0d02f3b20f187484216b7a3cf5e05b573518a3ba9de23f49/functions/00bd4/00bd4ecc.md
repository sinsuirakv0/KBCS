# 00bd4ecc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bd4e04`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4e04.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/machine_only_observed-0045.md#compare-a133a461c45ca92731458c2ea3ca0bfc)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bd4f10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4f10.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/machine_only_observed-0044.md#compare-5b09d255517bfe508a51ef7cc47c851a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd4ecc",
  "name": "_ZdlPv",
  "size": 8,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bcd67d1a60fc94360f12ccc2efea0f8e2d22398f91874eedfb07b95c3036d690",
  "source_text_sha256": "bcd67d1a60fc94360f12ccc2efea0f8e2d22398f91874eedfb07b95c3036d690",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd4ecc",
        "00bd4ed3"
      ]
    ],
    "bytes_sha256": "63447c7d4c1b47574b4fa4c38d2d9b1d8b19708e3199bfd0ef1ebbc190e576e1",
    "instruction_count": 2,
    "instruction_bytes": 8,
    "body_bytes": 8,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdb010](../00bdb/00bdb010.md)

## 呼び出し先

- [00bdb7c0](../00bdb/00bdb7c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 135 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void _ZdlPv(void *__ptr)

{
  free(__ptr);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd4ecc"></a> `00bd4ecc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bd4ed0"></a> `00bd4ed0` | `3c 1a 00 14` | b 0x00bdb7c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd4ecc`](#insn-00bd4ecc) 範囲 `[['00bd4ecc', '00bd4ed3']]`

## 命令位置別の参照

- [`00bd4ed0`](#insn-00bd4ed0) → [`00bdb7c0`](../00bdb/00bdb7c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb7c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd4ed0`](#insn-00bd4ed0)

~~~json
{
  "source": "00bd4ed0",
  "target": "00bdb7c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
