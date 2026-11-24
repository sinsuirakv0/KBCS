# 00bef9cc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bef5a4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef5a4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/detail_skipped-0006.md#compare-876dba7c263df79565ebedff27030140)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00befa68`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befa68.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/detail_skipped-0007.md#compare-05434a5843587eb9c7d6bf74bdf8f168)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bef9cc",
  "name": "_ZNSt6__ndk16chrono12system_clock9to_time_tERKNS0_10time_pointIS1_NS0_8durationIxNS_5ratioILl1ELl1000000EEEEEEE",
  "size": 40,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "52977bd100fe8d4c83044b13210764ff197a9588662d3fb95e5eac04529addde",
  "source_text_sha256": "52977bd100fe8d4c83044b13210764ff197a9588662d3fb95e5eac04529addde",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bef9cc",
        "00bef9f3"
      ]
    ],
    "bytes_sha256": "bf24b810813986ed4c72f4103c4cf7edd4f1bf74729d17def9877b0c6de88a77",
    "instruction_count": 10,
    "instruction_bytes": 40,
    "body_bytes": 40,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c589a0](../00c58/00c589a0.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 184 bytes

~~~c

long _ZNSt6__ndk16chrono12system_clock9to_time_tERKNS0_10time_pointIS1_NS0_8durationIxNS_5ratioILl1ELl1000000EEEEEEE
               (long *param_1)

{
  return *param_1 / 1000000;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bef9cc"></a> `00bef9cc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bef9d0"></a> `00bef9d0` | `69 9b 86 d2` | mov x9,#0x34db | `FALL_THROUGH`
<a id="insn-00bef9d4"></a> `00bef9d4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bef9d8"></a> `00bef9d8` | `c9 f6 ba f2` | movk x9,#0xd7b6, LSL #16 | `FALL_THROUGH`
<a id="insn-00bef9dc"></a> `00bef9dc` | `49 d0 db f2` | movk x9,#0xde82, LSL #32 | `FALL_THROUGH`
<a id="insn-00bef9e0"></a> `00bef9e0` | `69 63 e8 f2` | movk x9,#0x431b, LSL #48 | `FALL_THROUGH`
<a id="insn-00bef9e4"></a> `00bef9e4` | `08 7d 49 9b` | smulh x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bef9e8"></a> `00bef9e8` | `09 fd 52 93` | asr x9,x8,#0x12 | `FALL_THROUGH`
<a id="insn-00bef9ec"></a> `00bef9ec` | `20 fd 48 8b` | add x0,x9,x8, LSR #0x3f | `FALL_THROUGH`
<a id="insn-00bef9f0"></a> `00bef9f0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bef9cc`](#insn-00bef9cc) 範囲 `[['00bef9cc', '00bef9f3']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

