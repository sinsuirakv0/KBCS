# 00ac8ddc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00ac8be0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8be0.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/no_difference_in_scope-0012.md#compare-c286b883f8f2717fe1580b002db60849)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00ac8e4c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac8e4c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/no_difference_in_scope-0013.md#compare-ed49fa90e3aea138dda74fe1d71a155a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ac8ddc",
  "name": "FUN_00ac8ddc",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f7894d32cef2af6f1be9914a6c8d425f920168e941e0f22b1ba300bd57a5ca49",
  "source_text_sha256": "f7894d32cef2af6f1be9914a6c8d425f920168e941e0f22b1ba300bd57a5ca49",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ac8ddc",
        "00ac8de3"
      ]
    ],
    "bytes_sha256": "0d15c1d9a7c781be0a3b517bc9e332ead28dc7efc7a19547c5fb172f81911707",
    "instruction_count": 2,
    "instruction_bytes": 8,
    "body_bytes": 8,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00789c50](../00789/00789c50.md)
- [00789de0](../00789/00789de0.md)
- [0078bd58](../0078b/0078bd58.md)
- [0078bfc4](../0078b/0078bfc4.md)
- [0078df38](../0078d/0078df38.md)
- [0078e91c](../0078e/0078e91c.md)
- [0078eb30](../0078e/0078eb30.md)
- [0082c864](../0082c/0082c864.md)
- [0082cd18](../0082c/0082cd18.md)
- [0082d7a8](../0082d/0082d7a8.md)
- [00a72594](../00a72/00a72594.md)
- [00a75dac](../00a75/00a75dac.md)
- [00a79c04](../00a79/00a79c04.md)
- [00ac0a9c](../00ac0/00ac0a9c.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 87 bytes

~~~c

undefined4 FUN_00ac8ddc(long param_1)

{
  return *(undefined4 *)(param_1 + 0x60);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ac8ddc"></a> `00ac8ddc` | `00 60 40 b9` | ldr w0,[x0, #0x60] | `FALL_THROUGH`
<a id="insn-00ac8de0"></a> `00ac8de0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ac8ddc`](#insn-00ac8ddc) 範囲 `[['00ac8ddc', '00ac8de3']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

