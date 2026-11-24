# 00bfbbe4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfbb48`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbb48.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/machine_only_observed-0022.md#compare-92a62699c03451d31314ea089479dfe0)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bfcbd8`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcbd8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/machine_only_observed-0022.md#compare-a43224e68374f181d96466aa8e1d4897)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbbe4",
  "name": "_ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev",
  "size": 8,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7aad78d5ee02cd9a543a3b578a4fbc03a1974e4f9f0c76a3d883e486885d4b06",
  "source_text_sha256": "7aad78d5ee02cd9a543a3b578a4fbc03a1974e4f9f0c76a3d883e486885d4b06",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfbbe4",
        "00bfbbeb"
      ]
    ],
    "bytes_sha256": "e9e330fa94f4f77147789dd2e7cb555ec6443707b65aedb69396e3411cca2869",
    "instruction_count": 2,
    "instruction_bytes": 8,
    "body_bytes": 8,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c58090](../00c58/00c58090.md)
- [00c5e410](../00c5e/00c5e410.md)

## 呼び出し先

- [00c5d1b0](../00c5d/00c5d1b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 109 bytes

~~~c

void _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev(void)

{
  _ZNSt6__ndk18ios_baseD1Ev();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfbbe4"></a> `00bfbbe4` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bfbbe8"></a> `00bfbbe8` | `72 85 01 14` | b 0x00c5d1b0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfbbe4`](#insn-00bfbbe4) 範囲 `[['00bfbbe4', '00bfbbeb']]`

## 命令位置別の参照

- [`00bfbbe8`](#insn-00bfbbe8) → [`00c5d1b0`](../00c5d/00c5d1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d1b0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfbbe8`](#insn-00bfbbe8)

~~~json
{
  "source": "00bfbbe8",
  "target": "00c5d1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
