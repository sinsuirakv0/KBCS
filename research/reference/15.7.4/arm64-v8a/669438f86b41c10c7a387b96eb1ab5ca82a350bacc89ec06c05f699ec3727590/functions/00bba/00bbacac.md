# 00bbacac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbac68`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbac68.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/machine_only_observed-0043.md#compare-6d766469e2fc00533bac6c56c0c27941)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c376f4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c376f4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0077.md#compare-ec5162b9c5b3372c6c0d3c235e6eb0c5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbacac",
  "name": "<EXTERNAL>::free",
  "size": 8,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b8fd70a8ac556fc9b873b3c2800c5037ab7af09085d945013b493eba6b8a34b9",
  "source_text_sha256": "b8fd70a8ac556fc9b873b3c2800c5037ab7af09085d945013b493eba6b8a34b9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbacac",
        "00bbacb3"
      ]
    ],
    "bytes_sha256": "34a20212ed521fc60bd9b11390b8fc640ca937a9bb8c398d8b8546eff2fddc02",
    "instruction_count": 2,
    "instruction_bytes": 8,
    "body_bytes": 8,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb810](../00bdb/00bdb810.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 220 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void free(void *__ptr)

{
                    /* catch() { ... } // from try @ 00bb610c with catch @ 00bbacb0 */
  free(__ptr);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbacac"></a> `00bbacac` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bbacb0"></a> `00bbacb0` | `d8 82 00 14` | b 0x00bdb810 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbacac`](#insn-00bbacac) 範囲 `[['00bbacac', '00bbacaf']]`
  - `FALL_THROUGH` [`00bbacac`](#insn-00bbacac) → [`00bbacb0`](#insn-00bbacb0)
- ブロック [`00bbacb0`](#insn-00bbacb0) 範囲 `[['00bbacb0', '00bbacb3']]`

## 命令位置別の参照

- [`00bbacb0`](#insn-00bbacb0) → [`00bdb810`](../00bdb/00bdb810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb810` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbacb0`](#insn-00bbacb0)

~~~json
{
  "source": "00bbacb0",
  "target": "00bdb810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
