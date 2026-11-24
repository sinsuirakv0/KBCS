# 006bedac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `006be9fc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006be/006be9fc.md) · 移動量 `+0x3b0`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/no_difference_in_scope-0005.md#compare-3899c76761d7d07bcda69cc93621a8dc)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006bedac",
  "name": "FUN_006bedac",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fbe62027b3bc584fc48eacaeb8d3eab9fa7c8c2ee5ffddf8217885e551cd14ee",
  "source_text_sha256": "fbe62027b3bc584fc48eacaeb8d3eab9fa7c8c2ee5ffddf8217885e551cd14ee",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006bedac",
        "006bedf3"
      ]
    ],
    "bytes_sha256": "1f3c3d03f4a786536d03bed0de117e5e5b362eea285e9ca5e05e70f2189fb066",
    "instruction_count": 18,
    "instruction_bytes": 72,
    "body_bytes": 72,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006bc0a0](../006bc/006bc0a0.md)
- [00720498](../00720/00720498.md)
- [0076a1b8](../0076a/0076a1b8.md)
- [007bea00](../007be/007bea00.md)
- [007cdea8](../007cd/007cdea8.md)
- [007e00a4](../007e0/007e00a4.md)
- [008080c0](../00808/008080c0.md)
- [0089e4cc](../0089e/0089e4cc.md)
- [009258c8](../00925/009258c8.md)
- [00986418](../00986/00986418.md)
- [0098df8c](../0098d/0098df8c.md)
- [0098ec08](../0098e/0098ec08.md)
- [0099803c](../00998/0099803c.md)
- [00a8f618](../00a8f/00a8f618.md)
- [00ad7fb0](../00ad7/00ad7fb0.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 361 bytes

~~~c

uint FUN_006bedac(long param_1,long param_2)

{
  byte *pbVar1;
  
  pbVar1 = (byte *)(param_1 + param_2 * 4);
  return (uint)(*(byte *)(param_1 + 0x2a) ^ pbVar1[2]) << 0x10 |
         (uint)(*(byte *)(param_1 + 0x2b) ^ pbVar1[3]) << 0x18 |
         (uint)(*(byte *)(param_1 + 0x29) ^ pbVar1[1]) << 8 |
         (uint)(*(byte *)(param_1 + 0x28) ^ *pbVar1);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006bedac"></a> `006bedac` | `08 08 01 8b` | add x8,x0,x1, LSL #0x2 | `FALL_THROUGH`
<a id="insn-006bedb0"></a> `006bedb0` | `0a a8 40 39` | ldrb w10,[x0, #0x2a] | `FALL_THROUGH`
<a id="insn-006bedb4"></a> `006bedb4` | `0b ac 40 39` | ldrb w11,[x0, #0x2b] | `FALL_THROUGH`
<a id="insn-006bedb8"></a> `006bedb8` | `09 09 40 39` | ldrb w9,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-006bedbc"></a> `006bedbc` | `0c 05 40 39` | ldrb w12,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-006bedc0"></a> `006bedc0` | `49 01 09 4a` | eor w9,w10,w9 | `FALL_THROUGH`
<a id="insn-006bedc4"></a> `006bedc4` | `0a 0d 40 39` | ldrb w10,[x8, #0x3] | `FALL_THROUGH`
<a id="insn-006bedc8"></a> `006bedc8` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-006bedcc"></a> `006bedcc` | `29 3d 10 53` | lsl w9,w9,#0x10 | `FALL_THROUGH`
<a id="insn-006bedd0"></a> `006bedd0` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-006bedd4"></a> `006bedd4` | `0b a4 40 39` | ldrb w11,[x0, #0x29] | `FALL_THROUGH`
<a id="insn-006bedd8"></a> `006bedd8` | `29 61 0a 2a` | orr w9,w9,w10, LSL #0x18 | `FALL_THROUGH`
<a id="insn-006beddc"></a> `006beddc` | `0a a0 40 39` | ldrb w10,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-006bede0"></a> `006bede0` | `6b 01 0c 4a` | eor w11,w11,w12 | `FALL_THROUGH`
<a id="insn-006bede4"></a> `006bede4` | `29 21 0b 2a` | orr w9,w9,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-006bede8"></a> `006bede8` | `48 01 08 4a` | eor w8,w10,w8 | `FALL_THROUGH`
<a id="insn-006bedec"></a> `006bedec` | `20 01 08 2a` | orr w0,w9,w8 | `FALL_THROUGH`
<a id="insn-006bedf0"></a> `006bedf0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006bedac`](#insn-006bedac) 範囲 `[['006bedac', '006bedf3']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

