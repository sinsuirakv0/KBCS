# 006afbdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00689894`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/00689894.md) · 移動量 `+0x26348`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/machine_only_observed-0006.md#compare-5637c8de2291d90190915c2370e779b4)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `006afc1c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006af/006afc1c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/machine_only_observed-0007.md#compare-a0a3ad919ca4c7d594183c01673e28fb)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006afbdc",
  "name": "_ZdlPv",
  "size": 4,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "15f5b122ce4d9a978d45a3bf4f5674ef19abf4f20177e224f8d1a5744d9f4b29",
  "source_text_sha256": "15f5b122ce4d9a978d45a3bf4f5674ef19abf4f20177e224f8d1a5744d9f4b29",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006afbdc",
        "006afbdf"
      ]
    ],
    "bytes_sha256": "1d90b1090417a478000447aa15c33aa42be10b3d25471bc77ca415f17e3d55cd",
    "instruction_count": 1,
    "instruction_bytes": 4,
    "body_bytes": 4,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006a7480](../006a7/006a7480.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 156 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void _ZdlPv(void *__ptr)

{
  (*(code *)PTR__ZdlPv_00c9bb18)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006afbdc"></a> `006afbdc` | `b5 9f 16 14` | b 0x00c57ab0 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`006afbdc`](#insn-006afbdc) 範囲 `[['006afbdc', '006afbdf']]`
  - `UNCONDITIONAL_JUMP` [`006afbdc`](#insn-006afbdc) → [`00c57ab0`](../00c57/00c57ab0.md)

## 命令位置別の参照

- [`006afbdc`](#insn-006afbdc) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006afbdc`](#insn-006afbdc)

~~~json
{
  "source": "006afbdc",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
