# 00c2bbbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00baf174`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf174.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/detail_skipped-0006.md#compare-ab74b49e8e83171081cc96607bb2b2b1)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00c2bfe4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2bfe4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/detail_skipped-0009.md#compare-d2f4c524bac4437c336f01576ae700b7)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c2bbbc",
  "name": "_ZNKSt6__ndk18numpunctIwE16do_thousands_sepEv",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7716d0e64ec658ddb530cc4486e4754574e14b3b90d0d0f265f27d6fd07ec30c",
  "source_text_sha256": "7716d0e64ec658ddb530cc4486e4754574e14b3b90d0d0f265f27d6fd07ec30c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c2bbbc",
        "00c2bbc7"
      ]
    ],
    "bytes_sha256": "3b0d7006c59aef9e12cfa2b25bdcff70ae712cabcb26940d7687dac028541fa4",
    "instruction_count": 3,
    "instruction_bytes": 12,
    "body_bytes": 12,
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

## 疑似コード / UTF-8 120 bytes

~~~c

undefined4 _ZNKSt6__ndk18numpunctIwE16do_thousands_sepEv(long param_1)

{
  return *(undefined4 *)(param_1 + 0x14);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c2bbbc"></a> `00c2bbbc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00c2bbc0"></a> `00c2bbc0` | `00 14 40 b9` | ldr w0,[x0, #0x14] | `FALL_THROUGH`
<a id="insn-00c2bbc4"></a> `00c2bbc4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c2bbbc`](#insn-00c2bbbc) 範囲 `[['00c2bbbc', '00c2bbc7']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

