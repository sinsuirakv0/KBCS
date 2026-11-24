# 00b3bfbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b3bf20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3bf20.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0069.md#compare-588d953a29088c0c98e2449a9fe3960a)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00b3cfb0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3cfb0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/machine_only_observed-0021.md#compare-da907d6875993cd9c8da02e1426f5512)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b3bfbc",
  "name": "FUN_00b3bfbc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cf81e6170c340491d223c1b0774faca564fa7c34f01db0b4601f01472fbcbb6b",
  "source_text_sha256": "cf81e6170c340491d223c1b0774faca564fa7c34f01db0b4601f01472fbcbb6b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b3bfbc",
        "00b3c007"
      ]
    ],
    "bytes_sha256": "2e7d188338a2c63d8d7b5c6d53ce5cc4b572c75742de3c70aafe87fe6a4a7132",
    "instruction_count": 19,
    "instruction_bytes": 76,
    "body_bytes": 76,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005dbfbc](../005db/005dbfbc.md)
- [006971c0](../00697/006971c0.md)
- [0071e618](../0071e/0071e618.md)
- [008e49f4](../008e4/008e49f4.md)
- [008e5238](../008e5/008e5238.md)

## 呼び出し先

- [005e81d8](../005e8/005e81d8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 284 bytes

~~~c

void FUN_00b3bfbc(byte *param_1,int param_2)

{
  *(uint *)param_1 =
       (((uint)(param_1[5] ^ param_1[2]) << 0x10 | (uint)(param_1[4] ^ param_1[3]) << 0x18 |
        (uint)(param_1[6] ^ param_1[1]) << 8) - param_2) + (uint)(param_1[7] ^ *param_1);
  FUN_005e81d8();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b3bfbc"></a> `00b3bfbc` | `08 08 40 39` | ldrb w8,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00b3bfc0"></a> `00b3bfc0` | `09 14 40 39` | ldrb w9,[x0, #0x5] | `FALL_THROUGH`
<a id="insn-00b3bfc4"></a> `00b3bfc4` | `0a 10 40 39` | ldrb w10,[x0, #0x4] | `FALL_THROUGH`
<a id="insn-00b3bfc8"></a> `00b3bfc8` | `0b 04 40 39` | ldrb w11,[x0, #0x1] | `FALL_THROUGH`
<a id="insn-00b3bfcc"></a> `00b3bfcc` | `0c 18 40 39` | ldrb w12,[x0, #0x6] | `FALL_THROUGH`
<a id="insn-00b3bfd0"></a> `00b3bfd0` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00b3bfd4"></a> `00b3bfd4` | `09 0c 40 39` | ldrb w9,[x0, #0x3] | `FALL_THROUGH`
<a id="insn-00b3bfd8"></a> `00b3bfd8` | `08 3d 10 53` | lsl w8,w8,#0x10 | `FALL_THROUGH`
<a id="insn-00b3bfdc"></a> `00b3bfdc` | `49 01 09 4a` | eor w9,w10,w9 | `FALL_THROUGH`
<a id="insn-00b3bfe0"></a> `00b3bfe0` | `0a 00 40 39` | ldrb w10,[x0] | `FALL_THROUGH`
<a id="insn-00b3bfe4"></a> `00b3bfe4` | `08 61 09 2a` | orr w8,w8,w9, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00b3bfe8"></a> `00b3bfe8` | `89 01 0b 4a` | eor w9,w12,w11 | `FALL_THROUGH`
<a id="insn-00b3bfec"></a> `00b3bfec` | `0b 1c 40 39` | ldrb w11,[x0, #0x7] | `FALL_THROUGH`
<a id="insn-00b3bff0"></a> `00b3bff0` | `08 21 09 2a` | orr w8,w8,w9, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00b3bff4"></a> `00b3bff4` | `69 01 0a 4a` | eor w9,w11,w10 | `FALL_THROUGH`
<a id="insn-00b3bff8"></a> `00b3bff8` | `08 01 01 4b` | sub w8,w8,w1 | `FALL_THROUGH`
<a id="insn-00b3bffc"></a> `00b3bffc` | `08 01 09 0b` | add w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00b3c000"></a> `00b3c000` | `08 00 00 b9` | str w8,[x0] | `FALL_THROUGH`
<a id="insn-00b3c004"></a> `00b3c004` | `75 b0 ea 17` | b 0x005e81d8 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b3bfbc`](#insn-00b3bfbc) 範囲 `[['00b3bfbc', '00b3c007']]`

## 命令位置別の参照

- [`00b3c004`](#insn-00b3c004) → [`005e81d8`](../005e8/005e81d8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e81d8` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b3c004`](#insn-00b3c004)

~~~json
{
  "source": "00b3c004",
  "target": "005e81d8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
