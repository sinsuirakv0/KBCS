# 00adbfcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00adc094`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc094.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/machine_only_observed-0042.md#compare-30d429efb71e185730803a47cd11bc73)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adbfcc",
  "name": "FUN_00adbfcc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fcab2c2bd2fb3508186b472a804cc0c3a17e575f2d604f020fb94d8f87df6a9d",
  "source_text_sha256": "fcab2c2bd2fb3508186b472a804cc0c3a17e575f2d604f020fb94d8f87df6a9d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adbfcc",
        "00adc013"
      ]
    ],
    "bytes_sha256": "cd241573627be405bc3d5a4c984b22798378a4249e8dc9e064941f0101037813",
    "instruction_count": 18,
    "instruction_bytes": 72,
    "body_bytes": 72,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005d996c](../005d9/005d996c.md)
- [006f424c](../006f4/006f424c.md)
- [006f42ec](../006f4/006f42ec.md)
- [006f4724](../006f4/006f4724.md)
- [006f478c](../006f4/006f478c.md)
- [009121c4](../00912/009121c4.md)
- [00957f9c](../00957/00957f9c.md)

## 呼び出し先

- [005c3468](../005c3/005c3468.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 288 bytes

~~~c

void FUN_00adbfcc(byte *param_1,int param_2)

{
  *(uint *)param_1 =
       (uint)(param_1[7] ^ *param_1) + param_2 + (uint)(param_1[6] ^ param_1[1]) * 0x100 +
       (uint)(param_1[5] ^ param_1[2]) * 0x10000 + (uint)(param_1[4] ^ param_1[3]) * 0x1000000;
  FUN_005c3468();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00adbfcc"></a> `00adbfcc` | `08 00 40 39` | ldrb w8,[x0] | `FALL_THROUGH`
<a id="insn-00adbfd0"></a> `00adbfd0` | `09 1c 40 39` | ldrb w9,[x0, #0x7] | `FALL_THROUGH`
<a id="insn-00adbfd4"></a> `00adbfd4` | `0a 04 40 39` | ldrb w10,[x0, #0x1] | `FALL_THROUGH`
<a id="insn-00adbfd8"></a> `00adbfd8` | `0b 18 40 39` | ldrb w11,[x0, #0x6] | `FALL_THROUGH`
<a id="insn-00adbfdc"></a> `00adbfdc` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00adbfe0"></a> `00adbfe0` | `69 01 0a 4a` | eor w9,w11,w10 | `FALL_THROUGH`
<a id="insn-00adbfe4"></a> `00adbfe4` | `0a 08 40 39` | ldrb w10,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00adbfe8"></a> `00adbfe8` | `0b 14 40 39` | ldrb w11,[x0, #0x5] | `FALL_THROUGH`
<a id="insn-00adbfec"></a> `00adbfec` | `08 01 01 0b` | add w8,w8,w1 | `FALL_THROUGH`
<a id="insn-00adbff0"></a> `00adbff0` | `08 21 09 0b` | add w8,w8,w9, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00adbff4"></a> `00adbff4` | `69 01 0a 4a` | eor w9,w11,w10 | `FALL_THROUGH`
<a id="insn-00adbff8"></a> `00adbff8` | `0a 0c 40 39` | ldrb w10,[x0, #0x3] | `FALL_THROUGH`
<a id="insn-00adbffc"></a> `00adbffc` | `0b 10 40 39` | ldrb w11,[x0, #0x4] | `FALL_THROUGH`
<a id="insn-00adc000"></a> `00adc000` | `08 41 09 0b` | add w8,w8,w9, LSL #0x10 | `FALL_THROUGH`
<a id="insn-00adc004"></a> `00adc004` | `69 01 0a 4a` | eor w9,w11,w10 | `FALL_THROUGH`
<a id="insn-00adc008"></a> `00adc008` | `08 61 09 0b` | add w8,w8,w9, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00adc00c"></a> `00adc00c` | `08 00 00 b9` | str w8,[x0] | `FALL_THROUGH`
<a id="insn-00adc010"></a> `00adc010` | `16 9d eb 17` | b 0x005c3468 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adbfcc`](#insn-00adbfcc) 範囲 `[['00adbfcc', '00adc013']]`

## 命令位置別の参照

- [`00adc010`](#insn-00adc010) → [`005c3468`](../005c3/005c3468.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c3468` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adc010`](#insn-00adc010)

~~~json
{
  "source": "00adc010",
  "target": "005c3468",
  "target_space": "ram",
  "resolution": "function"
}
~~~
