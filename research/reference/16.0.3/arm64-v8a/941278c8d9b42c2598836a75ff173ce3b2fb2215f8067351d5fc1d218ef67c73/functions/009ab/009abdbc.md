# 009abdbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `009aae10`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aae10.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/no_difference_in_scope-0010.md#compare-58e21caebc7f50e23ed1fa71b9a03bb9)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009abdbc",
  "name": "FUN_009abdbc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "98a73b8c94db259919c9b08deaea28b4af061aa994b4f40e71bf7f20268b09d7",
  "source_text_sha256": "98a73b8c94db259919c9b08deaea28b4af061aa994b4f40e71bf7f20268b09d7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009abdbc",
        "009abdcf"
      ]
    ],
    "bytes_sha256": "90a6819cc261eae52fb1349202315430547c2cf2e719b67ddf4f522b691b8542",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00764918](../00764/00764918.md)
- [009b0ea8](../009b0/009b0ea8.md)
- [009b6d74](../009b6/009b6d74.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 306 bytes

~~~c

void FUN_009abdbc(undefined8 *param_1,long param_2)

{
  undefined4 uVar1;
  undefined8 uVar2;
  
  uVar2 = *(undefined8 *)(param_2 + 0x4c);
  uVar1 = *(undefined4 *)(param_2 + 0x5c);
  param_1[1] = *(undefined8 *)(param_2 + 0x54);
  *param_1 = uVar2;
  *(undefined4 *)(param_1 + 2) = uVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009abdbc"></a> `009abdbc` | `00 c0 c4 3c` | ldur q0,[x0, #0x4c] | `FALL_THROUGH`
<a id="insn-009abdc0"></a> `009abdc0` | `09 5c 40 b9` | ldr w9,[x0, #0x5c] | `FALL_THROUGH`
<a id="insn-009abdc4"></a> `009abdc4` | `00 01 80 3d` | str q0,[x8] | `FALL_THROUGH`
<a id="insn-009abdc8"></a> `009abdc8` | `09 11 00 b9` | str w9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009abdcc"></a> `009abdcc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009abdbc`](#insn-009abdbc) 範囲 `[['009abdbc', '009abdcf']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

