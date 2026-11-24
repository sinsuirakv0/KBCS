# 00bfcbec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b801a4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b801a4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/no_difference_in_scope-0009.md#compare-314b9dbb86edf0ff60f81a3d58443efb)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfd014`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd014.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/detail_skipped-0007.md#compare-dd766ca664f8b2c5dca6b1ec48fe16c7)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfcbec",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsERy",
  "size": 8,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "96ed56e18600f2a33a243e69a7f688bd43e6b5141684b6ce07f4aa4d18e3c7d0",
  "source_text_sha256": "96ed56e18600f2a33a243e69a7f688bd43e6b5141684b6ce07f4aa4d18e3c7d0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfcbec",
        "00bfcbf3"
      ]
    ],
    "bytes_sha256": "224d4df0836ae187285a713f6eab38d506f106d5205135a58ab1548d5684fce9",
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

- [00bfcbf4](../00bfc/00bfcbf4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 102 bytes

~~~c

void _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsERy(void)

{
  FUN_00bfcbf4();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfcbec"></a> `00bfcbec` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bfcbf0"></a> `00bfcbf0` | `01 00 00 14` | b 0x00bfcbf4 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfcbec`](#insn-00bfcbec) 範囲 `[['00bfcbec', '00bfcbf3']]`

## 命令位置別の参照

- [`00bfcbf0`](#insn-00bfcbf0) → [`00bfcbf4`](00bfcbf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bfcbf4` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfcbf0`](#insn-00bfcbf0)

~~~json
{
  "source": "00bfcbf0",
  "target": "00bfcbf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
