# 006dccec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `006dc93c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc93c.md) · 移動量 `+0x3b0`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/no_difference_in_scope-0005.md#compare-266caa1a7341112581b8d16d908891bb)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006dccec",
  "name": "FUN_006dccec",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "63aa05c0f53c7bb1c41c5cd74935ee64c9886c82795447049f2cdd519475d8b5",
  "source_text_sha256": "63aa05c0f53c7bb1c41c5cd74935ee64c9886c82795447049f2cdd519475d8b5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006dccec",
        "006dcd0b"
      ]
    ],
    "bytes_sha256": "38c5ca779a9110814aa02b5a5d98d41df3440559a95920b30d9a56fccbe72fad",
    "instruction_count": 8,
    "instruction_bytes": 32,
    "body_bytes": 32,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0063b0a4](../0063b/0063b0a4.md)
- [0063b7a4](../0063b/0063b7a4.md)
- [0064f0a8](../0064f/0064f0a8.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 76 bytes

~~~c

int FUN_006dccec(long param_1)

{
  return *(int *)(param_1 + 4) / 100;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006dccec"></a> `006dccec` | `e8 a3 90 52` | mov w8,#0x851f | `FALL_THROUGH`
<a id="insn-006dccf0"></a> `006dccf0` | `09 04 80 b9` | ldrsw x9,[x0, #0x4] | `FALL_THROUGH`
<a id="insn-006dccf4"></a> `006dccf4` | `68 3d aa 72` | movk w8,#0x51eb, LSL #16 | `FALL_THROUGH`
<a id="insn-006dccf8"></a> `006dccf8` | `28 7d 28 9b` | smull x8,w9,w8 | `FALL_THROUGH`
<a id="insn-006dccfc"></a> `006dccfc` | `09 fd 7f d3` | lsr x9,x8,#0x3f | `FALL_THROUGH`
<a id="insn-006dcd00"></a> `006dcd00` | `08 fd 65 93` | asr x8,x8,#0x25 | `FALL_THROUGH`
<a id="insn-006dcd04"></a> `006dcd04` | `00 01 09 0b` | add w0,w8,w9 | `FALL_THROUGH`
<a id="insn-006dcd08"></a> `006dcd08` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006dccec`](#insn-006dccec) 範囲 `[['006dccec', '006dcd0b']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

