# 00aefbac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a90780`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a90780.md) · 移動量 `+0x5f42c`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/machine_only_observed-0017.md#compare-93cff693b49f440bf064854761daca39)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aeffd4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aeffd4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/machine_only_observed-0020.md#compare-5f8f126c2cc4294ebee9111bfc932ec0)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aefbac",
  "name": "_ZdlPv",
  "size": 4,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b60df0e95a43003ef4aafa80a5b038a13ec43078cfefc2ffb11476109da5983b",
  "source_text_sha256": "b60df0e95a43003ef4aafa80a5b038a13ec43078cfefc2ffb11476109da5983b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aefbac",
        "00aefbaf"
      ]
    ],
    "bytes_sha256": "d99beafdab5bf90995a6755b328ec1355d42b5909170cbea264916146451713f",
    "instruction_count": 1,
    "instruction_bytes": 4,
    "body_bytes": 4,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ad075c](../00ad0/00ad075c.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 253 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void _ZdlPv(void *__ptr)

{
                    /* try { // try from 00aefbac to 00befbaf has its CatchHandler @ 00aefc10 */
  (*(code *)PTR__ZdlPv_00c9bb18)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aefbac"></a> `00aefbac` | `c1 9f 05 14` | b 0x00c57ab0 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00aefbac`](#insn-00aefbac) 範囲 `[['00aefbac', '00aefbaf']]`
  - `UNCONDITIONAL_JUMP` [`00aefbac`](#insn-00aefbac) → [`00c57ab0`](../00c57/00c57ab0.md)

## 命令位置別の参照

- [`00aefbac`](#insn-00aefbac) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aefbac`](#insn-00aefbac)

~~~json
{
  "source": "00aefbac",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
