# 00bdadd8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdad98`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdad98.md) · 移動量 `+0x40`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/no_difference_in_scope-0019.md#compare-8dfe11c777b5faba28470149fa964b33)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c57828`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57828.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0079.md#compare-0607eded5b72e4101f2d7dabda4afbc8)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdadd8",
  "name": "FUN_00bdadd8",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "148f13534a3730cf12f77055bed7b8e1bf52ce63da325844204b2cf5b68044c1",
  "source_text_sha256": "148f13534a3730cf12f77055bed7b8e1bf52ce63da325844204b2cf5b68044c1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdadd8",
        "00bdae73"
      ]
    ],
    "bytes_sha256": "cf33b8b617a8c4c15b8d23f27384e6bcd78a5e31687a299b4d2c3e26914e22f6",
    "instruction_count": 39,
    "instruction_bytes": 156,
    "body_bytes": 156,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bd6ec0](../00bd6/00bd6ec0.md)
- [00bd70ec](../00bd7/00bd70ec.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4775 bytes

~~~c

undefined8
FUN_00bdadd8(undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
            undefined8 param_5,undefined8 param_6,undefined8 param_7,undefined8 param_8,
            undefined8 param_9,long param_10,undefined8 param_11,undefined8 param_12,
            undefined8 param_13,undefined8 param_14,undefined8 param_15,undefined8 param_16,
            undefined8 param_17)

{
  undefined8 in_x9;
  undefined8 in_x10;
  undefined8 in_x11;
  undefined8 in_x12;
  undefined8 in_x13;
  undefined8 in_x14;
  undefined8 in_x15;
  undefined8 in_x16;
  undefined8 in_x17;
  undefined8 in_x18;
  undefined8 unaff_x19;
  undefined8 unaff_x20;
  undefined8 unaff_x21;
  undefined8 unaff_x22;
  undefined8 unaff_x23;
  undefined8 unaff_x24;
  undefined8 unaff_x25;
  undefined8 unaff_x26;
  undefined8 unaff_x27;
  undefined8 unaff_x28;
  undefined8 unaff_x29;
  undefined8 unaff_x30;
  undefined8 unaff_d8;
  undefined8 unaff_d9;
  undefined8 unaff_d10;
  undefined8 unaff_d11;
  undefined8 unaff_d12;
  undefined8 unaff_d13;
  undefined8 unaff_d14;
  undefined8 unaff_d15;
  undefined8 in_d16;
  undefined8 in_d17;
  undefined8 in_d18;
  undefined8 in_d19;
  undefined8 in_d20;
  undefined8 in_d21;
  undefined8 in_d22;
  undefined8 in_d23;
  undefined8 in_d24;
  undefined8 in_d25;
  undefined8 in_d26;
  undefined8 in_d27;
  undefined8 in_d28;
  undefined8 in_d29;
  undefined8 in_d30;
  undefined8 in_d31;
  
  *(long *)param_10 = param_10;
  *(undefined8 *)(param_10 + 8) = param_11;
  *(undefined8 *)(param_10 + 0x10) = param_12;
  *(undefined8 *)(param_10 + 0x18) = param_13;
  *(undefined8 *)(param_10 + 0x20) = param_14;
  *(undefined8 *)(param_10 + 0x28) = param_15;
  *(undefined8 *)(param_10 + 0x30) = param_16;
  *(undefined8 *)(param_10 + 0x38) = param_17;
  *(undefined8 *)(param_10 + 0x40) = param_1;
  *(undefined8 *)(param_10 + 0x48) = in_x9;
  *(undefined8 *)(param_10 + 0x50) = in_x10;
  *(undefined8 *)(param_10 + 0x58) = in_x11;
  *(undefined8 *)(param_10 + 0x60) = in_x12;
  *(undefined8 *)(param_10 + 0x68) = in_x13;
  *(undefined8 *)(param_10 + 0x70) = in_x14;
  *(undefined8 *)(param_10 + 0x78) = in_x15;
  *(undefined8 *)(param_10 + 0x80) = in_x16;
  *(undefined8 *)(param_10 + 0x88) = in_x17;
                    /* try { // try from 00bdae00 to 00cdae0f has its CatchHandler @ 00bdae90 */
  *(undefined8 *)(param_10 + 0x90) = in_x18;
  *(undefined8 *)(param_10 + 0x98) = unaff_x19;
  *(undefined8 *)(param_10 + 0xa0) = unaff_x20;
  *(undefined8 *)(param_10 + 0xa8) = unaff_x21;
  *(undefined8 *)(param_10 + 0xb0) = unaff_x22;
  *(undefined8 *)(param_10 + 0xb8) = unaff_x23;
  *(undefined8 *)(param_10 + 0xc0) = unaff_x24;
  *(undefined8 *)(param_10 + 200) = unaff_x25;
                    /* try { // try from 00bdae10 to 00cdae4b has its CatchHandler @ 00bdae98 */
  *(undefined8 *)(param_10 + 0xd0) = unaff_x26;
  *(undefined8 *)(param_10 + 0xd8) = unaff_x27;
  *(undefined8 *)(param_10 + 0xe0) = unaff_x28;
  *(undefined8 *)(param_10 + 0xe8) = unaff_x29;
  *(undefined8 *)(param_10 + 0xf0) = unaff_x30;
  *(BADSPACEBASE **)(param_10 + 0xf8) = register0x00000008;
  *(undefined8 *)(param_10 + 0x100) = unaff_x30;
  *(undefined8 *)(param_10 + 0x110) = param_2;
  *(undefined8 *)(param_10 + 0x118) = param_3;
  *(undefined8 *)(param_10 + 0x120) = param_4;
  *(undefined8 *)(param_10 + 0x128) = param_5;
  *(undefined8 *)(param_10 + 0x130) = param_6;
  *(undefined8 *)(param_10 + 0x138) = param_7;
  *(undefined8 *)(param_10 + 0x140) = param_8;
  *(undefined8 *)(param_10 + 0x148) = param_9;
  *(undefined8 *)(param_10 + 0x150) = unaff_d8;
  *(undefined8 *)(param_10 + 0x158) = unaff_d9;
  *(undefined8 *)(param_10 + 0x160) = unaff_d10;
  *(undefined8 *)(param_10 + 0x168) = unaff_d11;
  *(undefined8 *)(param_10 + 0x170) = unaff_d12;
  *(undefined8 *)(param_10 + 0x178) = unaff_d13;
  *(undefined8 *)(param_10 + 0x180) = unaff_d14;
  *(undefined8 *)(param_10 + 0x188) = unaff_d15;
  *(undefined8 *)(param_10 + 400) = in_d16;
  *(undefined8 *)(param_10 + 0x198) = in_d17;
                    /* try { // try from 00bdae4c to 00cdaed7 has its CatchHandler @ 00bdadcc */
  *(undefined8 *)(param_10 + 0x1a0) = in_d18;
  *(undefined8 *)(param_10 + 0x1a8) = in_d19;
  *(undefined8 *)(param_10 + 0x1b0) = in_d20;
  *(undefined8 *)(param_10 + 0x1b8) = in_d21;
  *(undefined8 *)(param_10 + 0x1c0) = in_d22;
  *(undefined8 *)(param_10 + 0x1c8) = in_d23;
  *(undefined8 *)(param_10 + 0x1d0) = in_d24;
  *(undefined8 *)(param_10 + 0x1d8) = in_d25;
  *(undefined8 *)(param_10 + 0x1e0) = in_d26;
  *(undefined8 *)(param_10 + 0x1e8) = in_d27;
  *(undefined8 *)(param_10 + 0x1f0) = in_d28;
  *(undefined8 *)(param_10 + 0x1f8) = in_d29;
  *(undefined8 *)(param_10 + 0x200) = in_d30;
  *(undefined8 *)(param_10 + 0x208) = in_d31;
  return 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdadd8"></a> `00bdadd8` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bdaddc"></a> `00bdaddc` | `00 04 00 a9` | stp x0,x1,[x0] | `FALL_THROUGH`
<a id="insn-00bdade0"></a> `00bdade0` | `02 0c 01 a9` | stp x2,x3,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bdade4"></a> `00bdade4` | `04 14 02 a9` | stp x4,x5,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bdade8"></a> `00bdade8` | `06 1c 03 a9` | stp x6,x7,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00bdadec"></a> `00bdadec` | `08 24 04 a9` | stp x8,x9,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00bdadf0"></a> `00bdadf0` | `0a 2c 05 a9` | stp x10,x11,[x0, #0x50] | `FALL_THROUGH`
<a id="insn-00bdadf4"></a> `00bdadf4` | `0c 34 06 a9` | stp x12,x13,[x0, #0x60] | `FALL_THROUGH`
<a id="insn-00bdadf8"></a> `00bdadf8` | `0e 3c 07 a9` | stp x14,x15,[x0, #0x70] | `FALL_THROUGH`
<a id="insn-00bdadfc"></a> `00bdadfc` | `10 44 08 a9` | stp x16,x17,[x0, #0x80] | `FALL_THROUGH`
<a id="insn-00bdae00"></a> `00bdae00` | `12 4c 09 a9` | stp x18,x19,[x0, #0x90] | `FALL_THROUGH`
<a id="insn-00bdae04"></a> `00bdae04` | `14 54 0a a9` | stp x20,x21,[x0, #0xa0] | `FALL_THROUGH`
<a id="insn-00bdae08"></a> `00bdae08` | `16 5c 0b a9` | stp x22,x23,[x0, #0xb0] | `FALL_THROUGH`
<a id="insn-00bdae0c"></a> `00bdae0c` | `18 64 0c a9` | stp x24,x25,[x0, #0xc0] | `FALL_THROUGH`
<a id="insn-00bdae10"></a> `00bdae10` | `1a 6c 0d a9` | stp x26,x27,[x0, #0xd0] | `FALL_THROUGH`
<a id="insn-00bdae14"></a> `00bdae14` | `1c 74 0e a9` | stp x28,x29,[x0, #0xe0] | `FALL_THROUGH`
<a id="insn-00bdae18"></a> `00bdae18` | `1e 78 00 f9` | str x30,[x0, #0xf0] | `FALL_THROUGH`
<a id="insn-00bdae1c"></a> `00bdae1c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bdae20"></a> `00bdae20` | `01 7c 00 f9` | str x1,[x0, #0xf8] | `FALL_THROUGH`
<a id="insn-00bdae24"></a> `00bdae24` | `1e 80 00 f9` | str x30,[x0, #0x100] | `FALL_THROUGH`
<a id="insn-00bdae28"></a> `00bdae28` | `00 04 11 6d` | stp d0,d1,[x0, #0x110] | `FALL_THROUGH`
<a id="insn-00bdae2c"></a> `00bdae2c` | `02 0c 12 6d` | stp d2,d3,[x0, #0x120] | `FALL_THROUGH`
<a id="insn-00bdae30"></a> `00bdae30` | `04 14 13 6d` | stp d4,d5,[x0, #0x130] | `FALL_THROUGH`
<a id="insn-00bdae34"></a> `00bdae34` | `06 1c 14 6d` | stp d6,d7,[x0, #0x140] | `FALL_THROUGH`
<a id="insn-00bdae38"></a> `00bdae38` | `08 24 15 6d` | stp d8,d9,[x0, #0x150] | `FALL_THROUGH`
<a id="insn-00bdae3c"></a> `00bdae3c` | `0a 2c 16 6d` | stp d10,d11,[x0, #0x160] | `FALL_THROUGH`
<a id="insn-00bdae40"></a> `00bdae40` | `0c 34 17 6d` | stp d12,d13,[x0, #0x170] | `FALL_THROUGH`
<a id="insn-00bdae44"></a> `00bdae44` | `0e 3c 18 6d` | stp d14,d15,[x0, #0x180] | `FALL_THROUGH`
<a id="insn-00bdae48"></a> `00bdae48` | `10 44 19 6d` | stp d16,d17,[x0, #0x190] | `FALL_THROUGH`
<a id="insn-00bdae4c"></a> `00bdae4c` | `12 4c 1a 6d` | stp d18,d19,[x0, #0x1a0] | `FALL_THROUGH`
<a id="insn-00bdae50"></a> `00bdae50` | `14 54 1b 6d` | stp d20,d21,[x0, #0x1b0] | `FALL_THROUGH`
<a id="insn-00bdae54"></a> `00bdae54` | `16 5c 1c 6d` | stp d22,d23,[x0, #0x1c0] | `FALL_THROUGH`
<a id="insn-00bdae58"></a> `00bdae58` | `18 64 1d 6d` | stp d24,d25,[x0, #0x1d0] | `FALL_THROUGH`
<a id="insn-00bdae5c"></a> `00bdae5c` | `1a 6c 1e 6d` | stp d26,d27,[x0, #0x1e0] | `FALL_THROUGH`
<a id="insn-00bdae60"></a> `00bdae60` | `1c 74 1f 6d` | stp d28,d29,[x0, #0x1f0] | `FALL_THROUGH`
<a id="insn-00bdae64"></a> `00bdae64` | `1e 00 01 fd` | str d30,[x0, #0x200] | `FALL_THROUGH`
<a id="insn-00bdae68"></a> `00bdae68` | `1f 04 01 fd` | str d31,[x0, #0x208] | `FALL_THROUGH`
<a id="insn-00bdae6c"></a> `00bdae6c` | `00 00 80 d2` | mov x0,#0x0 | `FALL_THROUGH`
<a id="insn-00bdae70"></a> `00bdae70` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdadd8`](#insn-00bdadd8) 範囲 `[['00bdadd8', '00bdadff']]`
  - `FALL_THROUGH` [`00bdadfc`](#insn-00bdadfc) → [`00bdae00`](#insn-00bdae00)
- ブロック [`00bdae00`](#insn-00bdae00) 範囲 `[['00bdae00', '00bdae0f']]`
  - `FALL_THROUGH` [`00bdae0c`](#insn-00bdae0c) → [`00bdae10`](#insn-00bdae10)
- ブロック [`00bdae10`](#insn-00bdae10) 範囲 `[['00bdae10', '00bdae4b']]`
  - `FALL_THROUGH` [`00bdae48`](#insn-00bdae48) → [`00bdae4c`](#insn-00bdae4c)
- ブロック [`00bdae4c`](#insn-00bdae4c) 範囲 `[['00bdae4c', '00bdae73']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

