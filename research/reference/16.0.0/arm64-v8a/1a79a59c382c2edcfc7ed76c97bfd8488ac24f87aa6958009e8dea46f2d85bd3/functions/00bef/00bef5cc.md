# 00bef5cc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b729c4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b729c4.md) · 移動量 `+0x7cc08`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/detail_skipped-0004.md#compare-f35bf88f4a946344a13fc23dd4d05d14)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bef9f4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef9f4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/detail_skipped-0006.md#compare-688c02e9b406853c4cc1139e901549ea)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bef5cc",
  "name": "_ZNSt6__ndk16chrono12system_clock11from_time_tEl",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "17102783bbf409c14dd0b0ae30c6c86da41e6894896b01ce67ab80a856e72733",
  "source_text_sha256": "17102783bbf409c14dd0b0ae30c6c86da41e6894896b01ce67ab80a856e72733",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bef5cc",
        "00bef5df"
      ]
    ],
    "bytes_sha256": "9d48a81bce5598181a63c56c1fb5a18c978e5d3cd264ef5f3466eee854cee73a",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c58610](../00c58/00c58610.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 103 bytes

~~~c

long _ZNSt6__ndk16chrono12system_clock11from_time_tEl(long param_1)

{
  return param_1 * 1000000;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bef5cc"></a> `00bef5cc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bef5d0"></a> `00bef5d0` | `08 48 88 52` | mov w8,#0x4240 | `FALL_THROUGH`
<a id="insn-00bef5d4"></a> `00bef5d4` | `e8 01 a0 72` | movk w8,#0xf, LSL #16 | `FALL_THROUGH`
<a id="insn-00bef5d8"></a> `00bef5d8` | `00 7c 08 9b` | mul x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00bef5dc"></a> `00bef5dc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bef5cc`](#insn-00bef5cc) 範囲 `[['00bef5cc', '00bef5df']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

