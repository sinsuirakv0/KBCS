# 00bffae0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b83098`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83098.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/detail_skipped-0004.md#compare-8e02acdc8ce58f6dfc5418a1c9658dda)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfff08`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bfff08.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/detail_skipped-0007.md#compare-8c0ab40e66ee48a5ad5e2ca8441d8333)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffae0",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE7seekoffExNS_8ios_base7seekdirEj",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ac9f176aa87a1c76192e26cab2926ae45a6cdb3e3b281590dcfd3e90a4621053",
  "source_text_sha256": "ac9f176aa87a1c76192e26cab2926ae45a6cdb3e3b281590dcfd3e90a4621053",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bffae0",
        "00bffaef"
      ]
    ],
    "bytes_sha256": "36af1bc5d17ab8c0b4b1a90d94ec77f84a57fc569935732e4f339ab867202fe3",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
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

## 疑似コード / UTF-8 161 bytes

~~~c

undefined1  [16]
_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE7seekoffExNS_8ios_base7seekdirEj(void)

{
  return ZEXT816(0xffffffffffffffff) << 0x40;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bffae0"></a> `00bffae0` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bffae4"></a> `00bffae4` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bffae8"></a> `00bffae8` | `01 00 80 92` | mov x1,#-0x1 | `FALL_THROUGH`
<a id="insn-00bffaec"></a> `00bffaec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bffae0`](#insn-00bffae0) 範囲 `[['00bffae0', '00bffaef']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

