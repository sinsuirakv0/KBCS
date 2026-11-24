# 00aed1bc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0162.md#review-206f17646048428555e763bbd819c8fd)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aed5e4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aed/00aed5e4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/machine_only_observed-0020.md#compare-7b04b4377f1542126799a895b8fdedee)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aed1bc",
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
        "00aed1bc",
        "00aed1bf"
      ]
    ],
    "bytes_sha256": "9a37121c9a3355abbe4dbd0a1618f3a07168ef874c187f03566a27a20d84c3c2",
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
<a id="insn-00aed1bc"></a> `00aed1bc` | `3d aa 05 14` | b 0x00c57ab0 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00aed1bc`](#insn-00aed1bc) 範囲 `[['00aed1bc', '00aed1bf']]`
  - `UNCONDITIONAL_JUMP` [`00aed1bc`](#insn-00aed1bc) → [`00c57ab0`](../00c57/00c57ab0.md)

## 命令位置別の参照

- [`00aed1bc`](#insn-00aed1bc) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aed1bc`](#insn-00aed1bc)

~~~json
{
  "source": "00aed1bc",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
