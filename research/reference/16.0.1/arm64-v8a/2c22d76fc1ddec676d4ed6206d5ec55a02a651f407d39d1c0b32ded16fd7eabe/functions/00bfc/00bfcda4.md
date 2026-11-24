# 00bfcda4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfc97c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc97c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/detail_skipped-0006.md#compare-bce294a68d3ee0ac570d4b6a7eaa8527)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfce40`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfce40.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/detail_skipped-0007.md#compare-a7f405d9b6aacc3bc09f40283d7a8ca0)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfcda4",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsERm",
  "size": 8,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9bc057a0eed34ea994908c37e4063354aa8a6792cd7adc7b4181d27be8f4b7a4",
  "source_text_sha256": "9bc057a0eed34ea994908c37e4063354aa8a6792cd7adc7b4181d27be8f4b7a4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfcda4",
        "00bfcdab"
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

- [00c59ff0](../00c59/00c59ff0.md)

## 呼び出し先

- [00bfcdac](../00bfc/00bfcdac.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 102 bytes

~~~c

void _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsERm(void)

{
  FUN_00bfcdac();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfcda4"></a> `00bfcda4` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bfcda8"></a> `00bfcda8` | `01 00 00 14` | b 0x00bfcdac | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfcda4`](#insn-00bfcda4) 範囲 `[['00bfcda4', '00bfcdab']]`

## 命令位置別の参照

- [`00bfcda8`](#insn-00bfcda8) → [`00bfcdac`](00bfcdac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bfcdac` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfcda8`](#insn-00bfcda8)

~~~json
{
  "source": "00bfcda8",
  "target": "00bfcdac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
