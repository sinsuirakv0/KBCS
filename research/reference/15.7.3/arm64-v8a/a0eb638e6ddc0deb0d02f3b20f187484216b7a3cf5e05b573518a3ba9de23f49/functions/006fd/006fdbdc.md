# 006fdbdc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `006fdbdc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006fd/006fdbdc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/no_difference_in_scope-0009.md#compare-f64d8279eaf9757ef8a560b885da7abd)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `006fdbdc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fdbdc.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/no_difference_in_scope-0008.md#compare-70150f0262c825d058666dcc36dc0699)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006fdbdc",
  "name": "FUN_006fdbdc",
  "size": 332,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "390ecbe89248ae30db7cf0fe5bb46739e32d929c960c7b9974dfd21af2a98f47",
  "source_text_sha256": "390ecbe89248ae30db7cf0fe5bb46739e32d929c960c7b9974dfd21af2a98f47",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006fdbdc",
        "006fdd27"
      ]
    ],
    "bytes_sha256": "a0eab60f5f6fb47629931bc06e2ffb121f751fba1daefe4a4a0526668fcc4113",
    "instruction_count": 83,
    "instruction_bytes": 332,
    "body_bytes": 332,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0067417c](../00674/0067417c.md)
- [00695904](../00695/00695904.md)
- [0070f364](../0070f/0070f364.md)
- [0070fd04](../0070f/0070fd04.md)
- [007317b0](../00731/007317b0.md)
- [00734374](../00734/00734374.md)
- [0073496c](../00734/0073496c.md)
- [00739a10](../00739/00739a10.md)
- [0073fa38](../0073f/0073fa38.md)
- [00749514](../00749/00749514.md)
- [0075e798](../0075e/0075e798.md)
- [0075f8cc](../0075f/0075f8cc.md)
- [00761d08](../00761/00761d08.md)
- [007999cc](../00799/007999cc.md)
- [0081fa64](../0081f/0081fa64.md)
- [008336f0](../00833/008336f0.md)
- [00844bd8](../00844/00844bd8.md)
- [008673f0](../00867/008673f0.md)
- [0086b704](../0086b/0086b704.md)
- [009903e4](../00990/009903e4.md)
- [009d85c0](../009d8/009d85c0.md)
- [009d9f2c](../009d9/009d9f2c.md)
- [00a30514](../00a30/00a30514.md)
- [00a3d6c8](../00a3d/00a3d6c8.md)
- [00a42124](../00a42/00a42124.md)
- [00ade2f4](../00ade/00ade2f4.md)
- [00ade990](../00ade/00ade990.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2109 bytes

~~~c

int FUN_006fdbdc(void)

{
  char *pcVar1;
  byte *pbVar2;
  long lVar3;
  int iVar4;
  int iVar5;
  long lVar6;
  long lVar7;
  
                    /* catch() { ... } // from try @ 006fd8c0 with catch @ 006fdbdc
                       catch() { ... } // from try @ 006fdb44 with catch @ 006fdbdc */
                    /* catch() { ... } // from try @ 006fd908 with catch @ 006fdbe4 */
  iVar5 = 0;
  iVar4 = 0;
  lVar6 = -300;
  lVar7 = 0xca3f;
  do {
    lVar3 = FUN_0081f580();
    pcVar1 = (char *)(lVar3 + lVar7);
    if (((*(char *)(lVar3 + 0xca66) == pcVar1[-1] && *(char *)(lVar3 + 0xca67) == *pcVar1) &&
        *(char *)(lVar3 + 0xca65) == pcVar1[-2]) && *(char *)(lVar3 + 0xca64) == pcVar1[-3]) {
      return iVar4;
    }
    lVar3 = FUN_0081f580();
    pbVar2 = (byte *)(lVar3 + lVar7);
    if (((uint)(*(byte *)(lVar3 + 0xca66) ^ pbVar2[-1]) << 0x10 |
         (uint)(*(byte *)(lVar3 + 0xca67) ^ *pbVar2) << 0x18 |
         (uint)(*(byte *)(lVar3 + 0xca65) ^ pbVar2[-2]) << 8 |
        (uint)(*(byte *)(lVar3 + 0xca64) ^ pbVar2[-3])) == 0x30) {
      iVar4 = (int)lVar6 + 400;
    }
    else {
      lVar3 = FUN_0081f580();
      pbVar2 = (byte *)(lVar3 + lVar7);
                    /* try { // try from 006fdc34 to 007fdf1f has its CatchHandler @ 006fdc34
                       catch() { ... } // from try @ 006fdc34 with catch @ 006fdc34
                       catch() { ... } // from try @ 006fe068 with catch @ 006fdc34
                       catch() { ... } // from try @ 006fe114 with catch @ 006fdc34
                       catch() { ... } // from try @ 006fe3a8 with catch @ 006fdc34
                       catch() { ... } // from try @ 006fe444 with catch @ 006fdc34 */
      iVar4 = (uint)(*(byte *)(lVar3 + 0xca64) ^ pbVar2[-3]) + iVar5 * 100 +
              (uint)(*(byte *)(lVar3 + 0xca65) ^ pbVar2[-2]) * 0x100 +
              (uint)(*(byte *)(lVar3 + 0xca66) ^ pbVar2[-1]) * 0x10000 +
              (uint)(*(byte *)(lVar3 + 0xca67) ^ *pbVar2) * 0x1000000;
    }
    lVar6 = lVar6 + 100;
    iVar5 = iVar5 + 1;
    lVar7 = lVar7 + 4;
  } while (lVar6 != 0);
  return iVar4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006fdbdc"></a> `006fdbdc` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-006fdbe0"></a> `006fdbe0` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006fdbe4"></a> `006fdbe4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006fdbe8"></a> `006fdbe8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006fdbec"></a> `006fdbec` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-006fdbf0"></a> `006fdbf0` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-006fdbf4"></a> `006fdbf4` | `f3 03 1f 2a` | mov w19,wzr | `FALL_THROUGH`
<a id="insn-006fdbf8"></a> `006fdbf8` | `75 25 80 92` | mov x21,#-0x12c | `FALL_THROUGH`
<a id="insn-006fdbfc"></a> `006fdbfc` | `f6 47 99 52` | mov w22,#0xca3f | `FALL_THROUGH`
<a id="insn-006fdc00"></a> `006fdc00` | `97 0c 80 52` | mov w23,#0x64 | `FALL_THROUGH`
<a id="insn-006fdc04"></a> `006fdc04` | `18 00 00 14` | b 0x006fdc64 | `UNCONDITIONAL_JUMP`
<a id="insn-006fdc08"></a> `006fdc08` | `5e 86 04 94` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-006fdc0c"></a> `006fdc0c` | `08 30 40 91` | add x8,x0,#0xc, LSL #12 | `FALL_THROUGH`
<a id="insn-006fdc10"></a> `006fdc10` | `09 00 16 8b` | add x9,x0,x22 | `FALL_THROUGH`
<a id="insn-006fdc14"></a> `006fdc14` | `2a d1 5f 38` | ldurb w10,[x9, #-0x3] | `FALL_THROUGH`
<a id="insn-006fdc18"></a> `006fdc18` | `0b 91 69 39` | ldrb w11,[x8, #0xa64] | `FALL_THROUGH`
<a id="insn-006fdc1c"></a> `006fdc1c` | `0c 95 69 39` | ldrb w12,[x8, #0xa65] | `FALL_THROUGH`
<a id="insn-006fdc20"></a> `006fdc20` | `0d 99 69 39` | ldrb w13,[x8, #0xa66] | `FALL_THROUGH`
<a id="insn-006fdc24"></a> `006fdc24` | `08 9d 69 39` | ldrb w8,[x8, #0xa67] | `FALL_THROUGH`
<a id="insn-006fdc28"></a> `006fdc28` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-006fdc2c"></a> `006fdc2c` | `2b e1 5f 38` | ldurb w11,[x9, #-0x2] | `FALL_THROUGH`
<a id="insn-006fdc30"></a> `006fdc30` | `8a 2a 17 1b` | madd w10,w20,w23,w10 | `FALL_THROUGH`
<a id="insn-006fdc34"></a> `006fdc34` | `8b 01 0b 4a` | eor w11,w12,w11 | `FALL_THROUGH`
<a id="insn-006fdc38"></a> `006fdc38` | `2c f1 5f 38` | ldurb w12,[x9, #-0x1] | `FALL_THROUGH`
<a id="insn-006fdc3c"></a> `006fdc3c` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-006fdc40"></a> `006fdc40` | `4a 21 0b 0b` | add w10,w10,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-006fdc44"></a> `006fdc44` | `ab 01 0c 4a` | eor w11,w13,w12 | `FALL_THROUGH`
<a id="insn-006fdc48"></a> `006fdc48` | `08 01 09 4a` | eor w8,w8,w9 | `FALL_THROUGH`
<a id="insn-006fdc4c"></a> `006fdc4c` | `4a 41 0b 0b` | add w10,w10,w11, LSL #0x10 | `FALL_THROUGH`
<a id="insn-006fdc50"></a> `006fdc50` | `53 61 08 0b` | add w19,w10,w8, LSL #0x18 | `FALL_THROUGH`
<a id="insn-006fdc54"></a> `006fdc54` | `b5 92 01 b1` | adds x21,x21,#0x64 | `FALL_THROUGH`
<a id="insn-006fdc58"></a> `006fdc58` | `94 06 00 91` | add x20,x20,#0x1 | `FALL_THROUGH`
<a id="insn-006fdc5c"></a> `006fdc5c` | `d6 12 00 91` | add x22,x22,#0x4 | `FALL_THROUGH`
<a id="insn-006fdc60"></a> `006fdc60` | `80 05 00 54` | b.eq 0x006fdd10 | `CONDITIONAL_JUMP`
<a id="insn-006fdc64"></a> `006fdc64` | `47 86 04 94` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-006fdc68"></a> `006fdc68` | `08 30 40 91` | add x8,x0,#0xc, LSL #12 | `FALL_THROUGH`
<a id="insn-006fdc6c"></a> `006fdc6c` | `09 00 16 8b` | add x9,x0,x22 | `FALL_THROUGH`
<a id="insn-006fdc70"></a> `006fdc70` | `2a f1 5f 38` | ldurb w10,[x9, #-0x1] | `FALL_THROUGH`
<a id="insn-006fdc74"></a> `006fdc74` | `0b 99 69 39` | ldrb w11,[x8, #0xa66] | `FALL_THROUGH`
<a id="insn-006fdc78"></a> `006fdc78` | `0c 9d 69 39` | ldrb w12,[x8, #0xa67] | `FALL_THROUGH`
<a id="insn-006fdc7c"></a> `006fdc7c` | `2d e1 5f 38` | ldurb w13,[x9, #-0x2] | `FALL_THROUGH`
<a id="insn-006fdc80"></a> `006fdc80` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-006fdc84"></a> `006fdc84` | `2b 01 40 39` | ldrb w11,[x9] | `FALL_THROUGH`
<a id="insn-006fdc88"></a> `006fdc88` | `29 d1 5f 38` | ldurb w9,[x9, #-0x3] | `FALL_THROUGH`
<a id="insn-006fdc8c"></a> `006fdc8c` | `4a 3d 10 53` | lsl w10,w10,#0x10 | `FALL_THROUGH`
<a id="insn-006fdc90"></a> `006fdc90` | `8b 01 0b 4a` | eor w11,w12,w11 | `FALL_THROUGH`
<a id="insn-006fdc94"></a> `006fdc94` | `0c 95 69 39` | ldrb w12,[x8, #0xa65] | `FALL_THROUGH`
<a id="insn-006fdc98"></a> `006fdc98` | `08 91 69 39` | ldrb w8,[x8, #0xa64] | `FALL_THROUGH`
<a id="insn-006fdc9c"></a> `006fdc9c` | `4a 61 0b 2a` | orr w10,w10,w11, LSL #0x18 | `FALL_THROUGH`
<a id="insn-006fdca0"></a> `006fdca0` | `8b 01 0d 4a` | eor w11,w12,w13 | `FALL_THROUGH`
<a id="insn-006fdca4"></a> `006fdca4` | `08 01 09 4a` | eor w8,w8,w9 | `FALL_THROUGH`
<a id="insn-006fdca8"></a> `006fdca8` | `4a 21 0b 2a` | orr w10,w10,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-006fdcac"></a> `006fdcac` | `48 01 08 2a` | orr w8,w10,w8 | `FALL_THROUGH`
<a id="insn-006fdcb0"></a> `006fdcb0` | `08 03 00 34` | cbz w8,0x006fdd10 | `CONDITIONAL_JUMP`
<a id="insn-006fdcb4"></a> `006fdcb4` | `33 86 04 94` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-006fdcb8"></a> `006fdcb8` | `08 30 40 91` | add x8,x0,#0xc, LSL #12 | `FALL_THROUGH`
<a id="insn-006fdcbc"></a> `006fdcbc` | `09 00 16 8b` | add x9,x0,x22 | `FALL_THROUGH`
<a id="insn-006fdcc0"></a> `006fdcc0` | `2a f1 5f 38` | ldurb w10,[x9, #-0x1] | `FALL_THROUGH`
<a id="insn-006fdcc4"></a> `006fdcc4` | `0b 99 69 39` | ldrb w11,[x8, #0xa66] | `FALL_THROUGH`
<a id="insn-006fdcc8"></a> `006fdcc8` | `0c 9d 69 39` | ldrb w12,[x8, #0xa67] | `FALL_THROUGH`
<a id="insn-006fdccc"></a> `006fdccc` | `2d e1 5f 38` | ldurb w13,[x9, #-0x2] | `FALL_THROUGH`
<a id="insn-006fdcd0"></a> `006fdcd0` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-006fdcd4"></a> `006fdcd4` | `2b 01 40 39` | ldrb w11,[x9] | `FALL_THROUGH`
<a id="insn-006fdcd8"></a> `006fdcd8` | `29 d1 5f 38` | ldurb w9,[x9, #-0x3] | `FALL_THROUGH`
<a id="insn-006fdcdc"></a> `006fdcdc` | `4a 3d 10 53` | lsl w10,w10,#0x10 | `FALL_THROUGH`
<a id="insn-006fdce0"></a> `006fdce0` | `8b 01 0b 4a` | eor w11,w12,w11 | `FALL_THROUGH`
<a id="insn-006fdce4"></a> `006fdce4` | `0c 95 69 39` | ldrb w12,[x8, #0xa65] | `FALL_THROUGH`
<a id="insn-006fdce8"></a> `006fdce8` | `08 91 69 39` | ldrb w8,[x8, #0xa64] | `FALL_THROUGH`
<a id="insn-006fdcec"></a> `006fdcec` | `4a 61 0b 2a` | orr w10,w10,w11, LSL #0x18 | `FALL_THROUGH`
<a id="insn-006fdcf0"></a> `006fdcf0` | `8b 01 0d 4a` | eor w11,w12,w13 | `FALL_THROUGH`
<a id="insn-006fdcf4"></a> `006fdcf4` | `08 01 09 4a` | eor w8,w8,w9 | `FALL_THROUGH`
<a id="insn-006fdcf8"></a> `006fdcf8` | `4a 21 0b 2a` | orr w10,w10,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-006fdcfc"></a> `006fdcfc` | `48 01 08 2a` | orr w8,w10,w8 | `FALL_THROUGH`
<a id="insn-006fdd00"></a> `006fdd00` | `1f c1 00 71` | cmp w8,#0x30 | `FALL_THROUGH`
<a id="insn-006fdd04"></a> `006fdd04` | `21 f8 ff 54` | b.ne 0x006fdc08 | `CONDITIONAL_JUMP`
<a id="insn-006fdd08"></a> `006fdd08` | `b3 42 06 11` | add w19,w21,#0x190 | `FALL_THROUGH`
<a id="insn-006fdd0c"></a> `006fdd0c` | `d2 ff ff 17` | b 0x006fdc54 | `UNCONDITIONAL_JUMP`
<a id="insn-006fdd10"></a> `006fdd10` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-006fdd14"></a> `006fdd14` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006fdd18"></a> `006fdd18` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006fdd1c"></a> `006fdd1c` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006fdd20"></a> `006fdd20` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-006fdd24"></a> `006fdd24` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006fdbdc`](#insn-006fdbdc) 範囲 `[['006fdbdc', '006fdbe3']]`
  - `FALL_THROUGH` [`006fdbe0`](#insn-006fdbe0) → [`006fdbe4`](#insn-006fdbe4)
- ブロック [`006fdbe4`](#insn-006fdbe4) 範囲 `[['006fdbe4', '006fdc07']]`
  - `UNCONDITIONAL_JUMP` [`006fdc04`](#insn-006fdc04) → [`006fdc64`](#insn-006fdc64)
- ブロック [`006fdc08`](#insn-006fdc08) 範囲 `[['006fdc08', '006fdc33']]`
  - `FALL_THROUGH` [`006fdc30`](#insn-006fdc30) → [`006fdc34`](#insn-006fdc34)
- ブロック [`006fdc34`](#insn-006fdc34) 範囲 `[['006fdc34', '006fdc53']]`
  - `FALL_THROUGH` [`006fdc50`](#insn-006fdc50) → [`006fdc54`](#insn-006fdc54)
- ブロック [`006fdc54`](#insn-006fdc54) 範囲 `[['006fdc54', '006fdc63']]`
  - `CONDITIONAL_JUMP` [`006fdc60`](#insn-006fdc60) → [`006fdd10`](#insn-006fdd10)
  - `FALL_THROUGH` [`006fdc60`](#insn-006fdc60) → [`006fdc64`](#insn-006fdc64)
- ブロック [`006fdc64`](#insn-006fdc64) 範囲 `[['006fdc64', '006fdcb3']]`
  - `CONDITIONAL_JUMP` [`006fdcb0`](#insn-006fdcb0) → [`006fdd10`](#insn-006fdd10)
  - `FALL_THROUGH` [`006fdcb0`](#insn-006fdcb0) → [`006fdcb4`](#insn-006fdcb4)
- ブロック [`006fdcb4`](#insn-006fdcb4) 範囲 `[['006fdcb4', '006fdd07']]`
  - `CONDITIONAL_JUMP` [`006fdd04`](#insn-006fdd04) → [`006fdc08`](#insn-006fdc08)
  - `FALL_THROUGH` [`006fdd04`](#insn-006fdd04) → [`006fdd08`](#insn-006fdd08)
- ブロック [`006fdd08`](#insn-006fdd08) 範囲 `[['006fdd08', '006fdd0f']]`
  - `UNCONDITIONAL_JUMP` [`006fdd0c`](#insn-006fdd0c) → [`006fdc54`](#insn-006fdc54)
- ブロック [`006fdd10`](#insn-006fdd10) 範囲 `[['006fdd10', '006fdd27']]`

## 命令位置別の参照

- [`006fdbdc`](#insn-006fdbdc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fdbe0`](#insn-006fdbe0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fdbe4`](#insn-006fdbe4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fdbe8`](#insn-006fdbe8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fdc04`](#insn-006fdc04) → [`006fdc64`](#insn-006fdc64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fdc08`](#insn-006fdc08) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`006fdc60`](#insn-006fdc60) → [`006fdd10`](#insn-006fdd10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fdc64`](#insn-006fdc64) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`006fdcb0`](#insn-006fdcb0) → [`006fdd10`](#insn-006fdd10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fdcb4`](#insn-006fdcb4) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`006fdd04`](#insn-006fdd04) → [`006fdc08`](#insn-006fdc08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fdd0c`](#insn-006fdd0c) → [`006fdc54`](#insn-006fdc54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fdd14`](#insn-006fdd14) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fdd18`](#insn-006fdd18) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fdd1c`](#insn-006fdd1c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fdd20`](#insn-006fdd20) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006fdbdc`](#insn-006fdbdc)

~~~json
{
  "source": "006fdbdc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fdbe0`](#insn-006fdbe0)

~~~json
{
  "source": "006fdbe0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fdbe4`](#insn-006fdbe4)

~~~json
{
  "source": "006fdbe4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fdbe8`](#insn-006fdbe8)

~~~json
{
  "source": "006fdbe8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fdc04`](#insn-006fdc04)

~~~json
{
  "source": "006fdc04",
  "target": "006fdc64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fdc08`](#insn-006fdc08)

~~~json
{
  "source": "006fdc08",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fdc60`](#insn-006fdc60)

~~~json
{
  "source": "006fdc60",
  "target": "006fdd10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fdc64`](#insn-006fdc64)

~~~json
{
  "source": "006fdc64",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fdcb0`](#insn-006fdcb0)

~~~json
{
  "source": "006fdcb0",
  "target": "006fdd10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fdcb4`](#insn-006fdcb4)

~~~json
{
  "source": "006fdcb4",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fdd04`](#insn-006fdd04)

~~~json
{
  "source": "006fdd04",
  "target": "006fdc08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fdd0c`](#insn-006fdd0c)

~~~json
{
  "source": "006fdd0c",
  "target": "006fdc54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fdd14`](#insn-006fdd14)

~~~json
{
  "source": "006fdd14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fdd18`](#insn-006fdd18)

~~~json
{
  "source": "006fdd18",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fdd1c`](#insn-006fdd1c)

~~~json
{
  "source": "006fdd1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fdd20`](#insn-006fdd20)

~~~json
{
  "source": "006fdd20",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
