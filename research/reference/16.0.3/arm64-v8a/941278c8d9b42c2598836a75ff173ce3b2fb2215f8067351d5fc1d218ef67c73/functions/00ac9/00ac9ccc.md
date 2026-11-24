# 00ac9ccc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00ac8cd8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac8cd8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/no_difference_in_scope-0013.md#compare-a224b4e806d2f77d27ba620bde99f984)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ac9ccc",
  "name": "FUN_00ac9ccc",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "875824d4ce1f5feed979b4d4ff8cf6269d86e2a14cb3116ca7c9a47b86e88eb3",
  "source_text_sha256": "875824d4ce1f5feed979b4d4ff8cf6269d86e2a14cb3116ca7c9a47b86e88eb3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ac9ccc",
        "00ac9cd3"
      ]
    ],
    "bytes_sha256": "2a1a50aab93391344861220bfee6946af4220116057fea6ff48465a46ebeded3",
    "instruction_count": 2,
    "instruction_bytes": 8,
    "body_bytes": 8,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0068bed8](../0068b/0068bed8.md)
- [0078a084](../0078a/0078a084.md)
- [0082fe24](../0082f/0082fe24.md)
- [008c6da4](../008c6/008c6da4.md)
- [00a735f8](../00a73/00a735f8.md)
- [00ac14b8](../00ac1/00ac14b8.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 88 bytes

~~~c

void FUN_00ac9ccc(long param_1)

{
  *(undefined1 *)(param_1 + 0x3f) = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ac9ccc"></a> `00ac9ccc` | `1f fc 00 39` | strb wzr,[x0, #0x3f] | `FALL_THROUGH`
<a id="insn-00ac9cd0"></a> `00ac9cd0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ac9ccc`](#insn-00ac9ccc) 範囲 `[['00ac9ccc', '00ac9cd3']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

