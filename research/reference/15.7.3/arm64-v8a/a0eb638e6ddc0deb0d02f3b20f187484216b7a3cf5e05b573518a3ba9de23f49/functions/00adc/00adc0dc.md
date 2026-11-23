# 00adc0dc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00adc014`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adc/00adc014.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-7a297b9ce059b3756b65f87233b5e25c)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00adc120`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc120.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/machine_only_observed-0042.md#compare-3d2de59e8b9a7462927e09d9b3e30c99)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adc0dc",
  "name": "FUN_00adc0dc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "475c0d95432c2d38b7ccc53a5e26b4fb8edef1c47afac613649f58b1e13873a7",
  "source_text_sha256": "475c0d95432c2d38b7ccc53a5e26b4fb8edef1c47afac613649f58b1e13873a7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adc0dc",
        "00adc127"
      ]
    ],
    "bytes_sha256": "b9cf32cf369b894914797956327037d6563764cb70ebb30d83cf9a22eedfb3ab",
    "instruction_count": 19,
    "instruction_bytes": 76,
    "body_bytes": 76,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005b726c](../005b7/005b726c.md)
- [00670de0](../00670/00670de0.md)
- [006f4518](../006f4/006f4518.md)
- [008b0960](../008b0/008b0960.md)
- [008b11a4](../008b1/008b11a4.md)

## 呼び出し先

- [005c3468](../005c3/005c3468.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 549 bytes

~~~c

void FUN_00adc0dc(byte *param_1,int param_2)

{
                    /* try { // try from 00adc0e4 to 00bdc203 has its CatchHandler @ 00adc0e4
                       catch() { ... } // from try @ 00adc0e4 with catch @ 00adc0e4
                       catch() { ... } // from try @ 00adc228 with catch @ 00adc0e4 */
  *(uint *)param_1 =
       (((uint)(param_1[5] ^ param_1[2]) << 0x10 | (uint)(param_1[4] ^ param_1[3]) << 0x18 |
        (uint)(param_1[6] ^ param_1[1]) << 8) - param_2) + (uint)(param_1[7] ^ *param_1);
  FUN_005c3468();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00adc0dc"></a> `00adc0dc` | `08 08 40 39` | ldrb w8,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00adc0e0"></a> `00adc0e0` | `09 14 40 39` | ldrb w9,[x0, #0x5] | `FALL_THROUGH`
<a id="insn-00adc0e4"></a> `00adc0e4` | `0a 10 40 39` | ldrb w10,[x0, #0x4] | `FALL_THROUGH`
<a id="insn-00adc0e8"></a> `00adc0e8` | `0b 04 40 39` | ldrb w11,[x0, #0x1] | `FALL_THROUGH`
<a id="insn-00adc0ec"></a> `00adc0ec` | `0c 18 40 39` | ldrb w12,[x0, #0x6] | `FALL_THROUGH`
<a id="insn-00adc0f0"></a> `00adc0f0` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00adc0f4"></a> `00adc0f4` | `09 0c 40 39` | ldrb w9,[x0, #0x3] | `FALL_THROUGH`
<a id="insn-00adc0f8"></a> `00adc0f8` | `08 3d 10 53` | lsl w8,w8,#0x10 | `FALL_THROUGH`
<a id="insn-00adc0fc"></a> `00adc0fc` | `49 01 09 4a` | eor w9,w10,w9 | `FALL_THROUGH`
<a id="insn-00adc100"></a> `00adc100` | `0a 00 40 39` | ldrb w10,[x0] | `FALL_THROUGH`
<a id="insn-00adc104"></a> `00adc104` | `08 61 09 2a` | orr w8,w8,w9, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00adc108"></a> `00adc108` | `89 01 0b 4a` | eor w9,w12,w11 | `FALL_THROUGH`
<a id="insn-00adc10c"></a> `00adc10c` | `0b 1c 40 39` | ldrb w11,[x0, #0x7] | `FALL_THROUGH`
<a id="insn-00adc110"></a> `00adc110` | `08 21 09 2a` | orr w8,w8,w9, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00adc114"></a> `00adc114` | `69 01 0a 4a` | eor w9,w11,w10 | `FALL_THROUGH`
<a id="insn-00adc118"></a> `00adc118` | `08 01 01 4b` | sub w8,w8,w1 | `FALL_THROUGH`
<a id="insn-00adc11c"></a> `00adc11c` | `08 01 09 0b` | add w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00adc120"></a> `00adc120` | `08 00 00 b9` | str w8,[x0] | `FALL_THROUGH`
<a id="insn-00adc124"></a> `00adc124` | `d1 9c eb 17` | b 0x005c3468 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adc0dc`](#insn-00adc0dc) 範囲 `[['00adc0dc', '00adc0e3']]`
  - `FALL_THROUGH` [`00adc0e0`](#insn-00adc0e0) → [`00adc0e4`](#insn-00adc0e4)
- ブロック [`00adc0e4`](#insn-00adc0e4) 範囲 `[['00adc0e4', '00adc127']]`

## 命令位置別の参照

- [`00adc124`](#insn-00adc124) → [`005c3468`](../005c3/005c3468.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c3468` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adc124`](#insn-00adc124)

~~~json
{
  "source": "00adc124",
  "target": "005c3468",
  "target_space": "ram",
  "resolution": "function"
}
~~~
