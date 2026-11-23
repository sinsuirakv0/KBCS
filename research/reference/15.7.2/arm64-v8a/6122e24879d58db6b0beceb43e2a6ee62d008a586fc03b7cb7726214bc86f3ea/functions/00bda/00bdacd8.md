# 00bdacd8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdad98`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdad98.md) · 移動量 `+0xc0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/no_difference_in_scope-0026.md#compare-ce27467cbfbf7bd02ce7bf1004ca6934)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdacd8",
  "name": "FUN_00bdacd8",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2d765373cb8bad7dfcab7fe83e02c6c2e6940492df7210d9c7c6961285bad54c",
  "source_text_sha256": "2d765373cb8bad7dfcab7fe83e02c6c2e6940492df7210d9c7c6961285bad54c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdacd8",
        "00bdad73"
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

- [00bd6dc0](../00bd6/00bd6dc0.md)
- [00bd6fec](../00bd6/00bd6fec.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4775 bytes

~~~c

undefined8
FUN_00bdacd8(undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
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
                    /* try { // try from 00bdacf4 to 00cdad03 has its CatchHandler @ 00bdad84 */
  *(undefined8 *)(param_10 + 0x60) = in_x12;
  *(undefined8 *)(param_10 + 0x68) = in_x13;
  *(undefined8 *)(param_10 + 0x70) = in_x14;
  *(undefined8 *)(param_10 + 0x78) = in_x15;
  *(undefined8 *)(param_10 + 0x80) = in_x16;
  *(undefined8 *)(param_10 + 0x88) = in_x17;
  *(undefined8 *)(param_10 + 0x90) = in_x18;
  *(undefined8 *)(param_10 + 0x98) = unaff_x19;
                    /* try { // try from 00bdad04 to 00cdad3f has its CatchHandler @ 00bdad8c */
  *(undefined8 *)(param_10 + 0xa0) = unaff_x20;
  *(undefined8 *)(param_10 + 0xa8) = unaff_x21;
  *(undefined8 *)(param_10 + 0xb0) = unaff_x22;
  *(undefined8 *)(param_10 + 0xb8) = unaff_x23;
  *(undefined8 *)(param_10 + 0xc0) = unaff_x24;
  *(undefined8 *)(param_10 + 200) = unaff_x25;
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
                    /* try { // try from 00bdad40 to 00cdadcb has its CatchHandler @ 00bdacc0 */
  *(undefined8 *)(param_10 + 0x170) = unaff_d12;
  *(undefined8 *)(param_10 + 0x178) = unaff_d13;
  *(undefined8 *)(param_10 + 0x180) = unaff_d14;
  *(undefined8 *)(param_10 + 0x188) = unaff_d15;
  *(undefined8 *)(param_10 + 400) = in_d16;
  *(undefined8 *)(param_10 + 0x198) = in_d17;
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
<a id="insn-00bdacd8"></a> `00bdacd8` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bdacdc"></a> `00bdacdc` | `00 04 00 a9` | stp x0,x1,[x0] | `FALL_THROUGH`
<a id="insn-00bdace0"></a> `00bdace0` | `02 0c 01 a9` | stp x2,x3,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bdace4"></a> `00bdace4` | `04 14 02 a9` | stp x4,x5,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bdace8"></a> `00bdace8` | `06 1c 03 a9` | stp x6,x7,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00bdacec"></a> `00bdacec` | `08 24 04 a9` | stp x8,x9,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00bdacf0"></a> `00bdacf0` | `0a 2c 05 a9` | stp x10,x11,[x0, #0x50] | `FALL_THROUGH`
<a id="insn-00bdacf4"></a> `00bdacf4` | `0c 34 06 a9` | stp x12,x13,[x0, #0x60] | `FALL_THROUGH`
<a id="insn-00bdacf8"></a> `00bdacf8` | `0e 3c 07 a9` | stp x14,x15,[x0, #0x70] | `FALL_THROUGH`
<a id="insn-00bdacfc"></a> `00bdacfc` | `10 44 08 a9` | stp x16,x17,[x0, #0x80] | `FALL_THROUGH`
<a id="insn-00bdad00"></a> `00bdad00` | `12 4c 09 a9` | stp x18,x19,[x0, #0x90] | `FALL_THROUGH`
<a id="insn-00bdad04"></a> `00bdad04` | `14 54 0a a9` | stp x20,x21,[x0, #0xa0] | `FALL_THROUGH`
<a id="insn-00bdad08"></a> `00bdad08` | `16 5c 0b a9` | stp x22,x23,[x0, #0xb0] | `FALL_THROUGH`
<a id="insn-00bdad0c"></a> `00bdad0c` | `18 64 0c a9` | stp x24,x25,[x0, #0xc0] | `FALL_THROUGH`
<a id="insn-00bdad10"></a> `00bdad10` | `1a 6c 0d a9` | stp x26,x27,[x0, #0xd0] | `FALL_THROUGH`
<a id="insn-00bdad14"></a> `00bdad14` | `1c 74 0e a9` | stp x28,x29,[x0, #0xe0] | `FALL_THROUGH`
<a id="insn-00bdad18"></a> `00bdad18` | `1e 78 00 f9` | str x30,[x0, #0xf0] | `FALL_THROUGH`
<a id="insn-00bdad1c"></a> `00bdad1c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bdad20"></a> `00bdad20` | `01 7c 00 f9` | str x1,[x0, #0xf8] | `FALL_THROUGH`
<a id="insn-00bdad24"></a> `00bdad24` | `1e 80 00 f9` | str x30,[x0, #0x100] | `FALL_THROUGH`
<a id="insn-00bdad28"></a> `00bdad28` | `00 04 11 6d` | stp d0,d1,[x0, #0x110] | `FALL_THROUGH`
<a id="insn-00bdad2c"></a> `00bdad2c` | `02 0c 12 6d` | stp d2,d3,[x0, #0x120] | `FALL_THROUGH`
<a id="insn-00bdad30"></a> `00bdad30` | `04 14 13 6d` | stp d4,d5,[x0, #0x130] | `FALL_THROUGH`
<a id="insn-00bdad34"></a> `00bdad34` | `06 1c 14 6d` | stp d6,d7,[x0, #0x140] | `FALL_THROUGH`
<a id="insn-00bdad38"></a> `00bdad38` | `08 24 15 6d` | stp d8,d9,[x0, #0x150] | `FALL_THROUGH`
<a id="insn-00bdad3c"></a> `00bdad3c` | `0a 2c 16 6d` | stp d10,d11,[x0, #0x160] | `FALL_THROUGH`
<a id="insn-00bdad40"></a> `00bdad40` | `0c 34 17 6d` | stp d12,d13,[x0, #0x170] | `FALL_THROUGH`
<a id="insn-00bdad44"></a> `00bdad44` | `0e 3c 18 6d` | stp d14,d15,[x0, #0x180] | `FALL_THROUGH`
<a id="insn-00bdad48"></a> `00bdad48` | `10 44 19 6d` | stp d16,d17,[x0, #0x190] | `FALL_THROUGH`
<a id="insn-00bdad4c"></a> `00bdad4c` | `12 4c 1a 6d` | stp d18,d19,[x0, #0x1a0] | `FALL_THROUGH`
<a id="insn-00bdad50"></a> `00bdad50` | `14 54 1b 6d` | stp d20,d21,[x0, #0x1b0] | `FALL_THROUGH`
<a id="insn-00bdad54"></a> `00bdad54` | `16 5c 1c 6d` | stp d22,d23,[x0, #0x1c0] | `FALL_THROUGH`
<a id="insn-00bdad58"></a> `00bdad58` | `18 64 1d 6d` | stp d24,d25,[x0, #0x1d0] | `FALL_THROUGH`
<a id="insn-00bdad5c"></a> `00bdad5c` | `1a 6c 1e 6d` | stp d26,d27,[x0, #0x1e0] | `FALL_THROUGH`
<a id="insn-00bdad60"></a> `00bdad60` | `1c 74 1f 6d` | stp d28,d29,[x0, #0x1f0] | `FALL_THROUGH`
<a id="insn-00bdad64"></a> `00bdad64` | `1e 00 01 fd` | str d30,[x0, #0x200] | `FALL_THROUGH`
<a id="insn-00bdad68"></a> `00bdad68` | `1f 04 01 fd` | str d31,[x0, #0x208] | `FALL_THROUGH`
<a id="insn-00bdad6c"></a> `00bdad6c` | `00 00 80 d2` | mov x0,#0x0 | `FALL_THROUGH`
<a id="insn-00bdad70"></a> `00bdad70` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdacd8`](#insn-00bdacd8) 範囲 `[['00bdacd8', '00bdacf3']]`
  - `FALL_THROUGH` [`00bdacf0`](#insn-00bdacf0) → [`00bdacf4`](#insn-00bdacf4)
- ブロック [`00bdacf4`](#insn-00bdacf4) 範囲 `[['00bdacf4', '00bdad03']]`
  - `FALL_THROUGH` [`00bdad00`](#insn-00bdad00) → [`00bdad04`](#insn-00bdad04)
- ブロック [`00bdad04`](#insn-00bdad04) 範囲 `[['00bdad04', '00bdad3f']]`
  - `FALL_THROUGH` [`00bdad3c`](#insn-00bdad3c) → [`00bdad40`](#insn-00bdad40)
- ブロック [`00bdad40`](#insn-00bdad40) 範囲 `[['00bdad40', '00bdad73']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

