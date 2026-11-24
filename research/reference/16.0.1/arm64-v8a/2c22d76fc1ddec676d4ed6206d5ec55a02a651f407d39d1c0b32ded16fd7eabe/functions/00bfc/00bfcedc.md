# 00bfcedc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfcab4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcab4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/detail_skipped-0006.md#compare-62c15a16d6f6fd9b1a9361db5592516a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfcf78`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfcf78.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/detail_skipped-0007.md#compare-6e4bc05dc17a06f46a2bdeed3132609a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfcedc",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsERx",
  "size": 8,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "684049e4046435a49b5f8c8482eab710e91f3fd67bbe25ea3c50f0d26348324b",
  "source_text_sha256": "684049e4046435a49b5f8c8482eab710e91f3fd67bbe25ea3c50f0d26348324b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfcedc",
        "00bfcee3"
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

- [00bfcee4](../00bfc/00bfcee4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 102 bytes

~~~c

void _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsERx(void)

{
  FUN_00bfcee4();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfcedc"></a> `00bfcedc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bfcee0"></a> `00bfcee0` | `01 00 00 14` | b 0x00bfcee4 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfcedc`](#insn-00bfcedc) 範囲 `[['00bfcedc', '00bfcee3']]`

## 命令位置別の参照

- [`00bfcee0`](#insn-00bfcee0) → [`00bfcee4`](00bfcee4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bfcee4` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfcee0`](#insn-00bfcee0)

~~~json
{
  "source": "00bfcee0",
  "target": "00bfcee4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
