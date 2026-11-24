# 00ac9dfc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00ac8e08`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac8e08.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/no_difference_in_scope-0013.md#compare-37edbfcfe27bd187cdd125c876707695)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ac9dfc",
  "name": "FUN_00ac9dfc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "114f472a925b6d36bcf6bd3a3417f44e1c3657ff227bcb593272ab0ebfa193b8",
  "source_text_sha256": "114f472a925b6d36bcf6bd3a3417f44e1c3657ff227bcb593272ab0ebfa193b8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ac9dfc",
        "00ac9e0f"
      ]
    ],
    "bytes_sha256": "f8a32f5a9c8006a273a3eaec944e9143b7d4ff599ec81b9e6c638f8ddb15aff3",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a735f8](../00a73/00a735f8.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 169 bytes

~~~c

void FUN_00ac9dfc(long param_1,int param_2,int param_3)

{
  *(float *)(param_1 + 0x208) = (float)param_2;
  *(float *)(param_1 + 0x20c) = (float)param_3;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ac9dfc"></a> `00ac9dfc` | `20 00 22 1e` | scvtf s0,w1 | `FALL_THROUGH`
<a id="insn-00ac9e00"></a> `00ac9e00` | `41 00 22 1e` | scvtf s1,w2 | `FALL_THROUGH`
<a id="insn-00ac9e04"></a> `00ac9e04` | `00 08 02 bd` | str s0,[x0, #0x208] | `FALL_THROUGH`
<a id="insn-00ac9e08"></a> `00ac9e08` | `01 0c 02 bd` | str s1,[x0, #0x20c] | `FALL_THROUGH`
<a id="insn-00ac9e0c"></a> `00ac9e0c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ac9dfc`](#insn-00ac9dfc) 範囲 `[['00ac9dfc', '00ac9e0f']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

