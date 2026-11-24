# 00bffaf4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bffa58`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffa58.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/high-0011.md#compare-d76ba899eef25646d09fa2fa7dc7b291)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00c00ae8`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00ae8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0011.md#compare-6b0440e83b7e5b282674a737b275ca3e)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffaf4",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEED2Ev",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4e6984b7db699be158f63f9cf296800e8603dfd76050b98eddca526e00fb2b8d",
  "source_text_sha256": "4e6984b7db699be158f63f9cf296800e8603dfd76050b98eddca526e00fb2b8d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bffaf4",
        "00bffb0b"
      ]
    ],
    "bytes_sha256": "c8d14fed27a2a1dd50c611e9e42f1b959546cc7a23009c1f244e390fc60f3736",
    "instruction_count": 6,
    "instruction_bytes": 24,
    "body_bytes": 24,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5e490](../00c5e/00c5e490.md)
- [00c5e4a0](../00c5e/00c5e4a0.md)

## 呼び出し先

- [00c58360](../00c58/00c58360.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 232 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEED2Ev(long *param_1)

{
  *param_1 = (long)(PTR__ZTVNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEE_00c9bc00 + 0x10);
  _ZNSt6__ndk16localeD1Ev(param_1 + 1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bffaf4"></a> `00bffaf4` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bffaf8"></a> `00bffaf8` | `e8 04 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bffafc"></a> `00bffafc` | `08 01 46 f9` | ldr x8,[x8, #0xc00] | `FALL_THROUGH`
<a id="insn-00bffb00"></a> `00bffb00` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bffb04"></a> `00bffb04` | `08 84 00 f8` | str x8,[x0], #0x8 | `FALL_THROUGH`
<a id="insn-00bffb08"></a> `00bffb08` | `16 62 01 14` | b 0x00c58360 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bffaf4`](#insn-00bffaf4) 範囲 `[['00bffaf4', '00bffb0b']]`

## 命令位置別の参照

- [`00bffafc`](#insn-00bffafc) → `00c9bc00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bffb04`](#insn-00bffb04) → `00c93048`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`00bffb08`](#insn-00bffb08) → [`00c58360`](../00c58/00c58360.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58360` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bffafc`](#insn-00bffafc)

~~~json
{
  "source": "00bffafc",
  "target": "00c9bc00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bc00",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bffb04`](#insn-00bffb04)

~~~json
{
  "source": "00bffb04",
  "target": "00c93048",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93038",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bffb08`](#insn-00bffb08)

~~~json
{
  "source": "00bffb08",
  "target": "00c58360",
  "target_space": "ram",
  "resolution": "function"
}
~~~
