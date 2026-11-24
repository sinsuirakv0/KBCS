# 00babe6c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00babe28`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00babe28.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0022.md#compare-29259068f0c5b0fc5495d92c7dfe9a43)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c288b4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c288b4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0075.md#compare-5d65d431beb542268c0be9009eed4c47)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00babe6c",
  "name": "FUN_00babe6c",
  "size": 604,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dee472cc8c24a181099fe882dffa869bb9e1962557bf517244acbfdfb6138c43",
  "source_text_sha256": "dee472cc8c24a181099fe882dffa869bb9e1962557bf517244acbfdfb6138c43",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00babe6c",
        "00bac0c7"
      ]
    ],
    "bytes_sha256": "a5aa80fd44a449484988c55bdb561cc95553188a3b281244f1e67947a4da17ad",
    "instruction_count": 151,
    "instruction_bytes": 604,
    "body_bytes": 604,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00babe04](../00bab/00babe04.md)
- [00bac640](../00bac/00bac640.md)
- [00baecc4](../00bae/00baecc4.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3700 bytes

~~~c

undefined8
FUN_00babe6c(long param_1,ushort *param_2,long *param_3,undefined1 *param_4,long param_5,
            long *param_6,ulong param_7,uint param_8)

{
  uint uVar1;
  ushort uVar2;
  ushort uVar3;
  undefined1 *puVar4;
  uint uVar5;
  ushort *puVar6;
  byte *pbVar7;
  byte bVar8;
  
  *param_3 = param_1;
  *param_6 = (long)param_4;
  if ((param_8 >> 1 & 1) != 0) {
    if (param_5 - (long)param_4 < 3) {
      return 1;
    }
    *param_6 = (long)(param_4 + 1);
    *param_4 = 0xef;
    puVar4 = (undefined1 *)*param_6;
    *param_6 = (long)(puVar4 + 1);
    *puVar4 = 0xbb;
    puVar4 = (undefined1 *)*param_6;
    *param_6 = (long)(puVar4 + 1);
    *puVar4 = 0xbf;
  }
  puVar6 = (ushort *)*param_3;
  do {
    if (param_2 <= puVar6) {
      return 0;
    }
    uVar2 = *puVar6;
    if (param_7 < uVar2) {
      return 2;
    }
    uVar5 = (uint)uVar2;
    if (uVar2 < 0x80) {
      pbVar7 = (byte *)*param_6;
      if (param_5 - (long)pbVar7 < 1) {
        return 1;
      }
      *param_6 = (long)(pbVar7 + 1);
      *pbVar7 = (byte)uVar2;
    }
    else {
      if (uVar2 < 0x800) {
        pbVar7 = (byte *)*param_6;
        if (param_5 - (long)pbVar7 < 2) {
          return 1;
        }
        *param_6 = (long)(pbVar7 + 1);
        bVar8 = (byte)(uVar2 >> 6) | 0xc0;
      }
      else {
        bVar8 = (byte)(uVar2 >> 8);
        if (uVar2 >> 0xb < 0x1b) {
          pbVar7 = (byte *)*param_6;
          if (param_5 - (long)pbVar7 < 3) {
            return 1;
          }
          *param_6 = (long)(pbVar7 + 1);
          *pbVar7 = bVar8 >> 4 | 0xe0;
          pbVar7 = (byte *)*param_6;
          bVar8 = (byte)(uVar2 >> 6) & 0x3f | 0x80;
        }
        else {
          if (uVar2 >> 10 < 0x37) {
            if ((long)param_2 - (long)puVar6 < 4) {
              return 1;
            }
            uVar3 = puVar6[1];
            if ((uVar3 & 0xfc00) != 0xdc00) {
              return 2;
            }
            if (param_5 - *param_6 < 4) {
              return 1;
            }
                    /* try { // try from 00bac018 to 00cac033 has its CatchHandler @ 00bac348 */
            if (param_7 < ((ulong)uVar3 & 0x3ff | ((ulong)uVar5 & 0x3ff) << 10) + 0x10000) {
              return 2;
            }
            *param_3 = (long)(puVar6 + 1);
            pbVar7 = (byte *)*param_6;
            uVar1 = (uVar2 >> 6 & 0xf) + 1;
                    /* try { // try from 00bac034 to 00cac1df has its CatchHandler @ 00babe48 */
            *param_6 = (long)(pbVar7 + 1);
            *pbVar7 = (byte)(uVar1 >> 2) | 0xf0;
            pbVar7 = (byte *)*param_6;
            *param_6 = (long)(pbVar7 + 1);
            *pbVar7 = (byte)((uVar1 & 3) << 4) | (byte)(uVar2 >> 2) & 0xf | 0x80;
            pbVar7 = (byte *)*param_6;
            *param_6 = (long)(pbVar7 + 1);
            *pbVar7 = (byte)((uVar5 & 3) << 4) | (byte)(uVar3 >> 6) & 0xf | 0x80;
            pbVar7 = (byte *)*param_6;
            *param_6 = (long)(pbVar7 + 1);
            *pbVar7 = (byte)uVar3 & 0x3f | 0x80;
            goto LAB_00babf20;
          }
          if (uVar5 < 0xe000) {
            return 2;
          }
          pbVar7 = (byte *)*param_6;
          if (param_5 - (long)pbVar7 < 3) {
            return 1;
          }
          *param_6 = (long)(pbVar7 + 1);
          *pbVar7 = bVar8 >> 4 | 0xe0;
          pbVar7 = (byte *)*param_6;
          bVar8 = (byte)(uVar2 >> 6) & 0xbf;
        }
        *param_6 = (long)(pbVar7 + 1);
      }
      *pbVar7 = bVar8;
      pbVar7 = (byte *)*param_6;
      *param_6 = (long)(pbVar7 + 1);
      *pbVar7 = (byte)uVar2 & 0x3f | 0x80;
    }
LAB_00babf20:
    puVar6 = (ushort *)(*param_3 + 2);
    *param_3 = (long)puVar6;
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00babe6c"></a> `00babe6c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00babe70"></a> `00babe70` | `40 00 00 f9` | str x0,[x2] | `FALL_THROUGH`
<a id="insn-00babe74"></a> `00babe74` | `a3 00 00 f9` | str x3,[x5] | `FALL_THROUGH`
<a id="insn-00babe78"></a> `00babe78` | `87 02 08 36` | tbz w7,#0x1,0x00babec8 | `CONDITIONAL_JUMP`
<a id="insn-00babe7c"></a> `00babe7c` | `88 00 03 cb` | sub x8,x4,x3 | `FALL_THROUGH`
<a id="insn-00babe80"></a> `00babe80` | `1f 0d 00 f1` | cmp x8,#0x3 | `FALL_THROUGH`
<a id="insn-00babe84"></a> `00babe84` | `6a 00 00 54` | b.ge 0x00babe90 | `CONDITIONAL_JUMP`
<a id="insn-00babe88"></a> `00babe88` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00babe8c"></a> `00babe8c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00babe90"></a> `00babe90` | `68 04 00 91` | add x8,x3,#0x1 | `FALL_THROUGH`
<a id="insn-00babe94"></a> `00babe94` | `e9 1d 80 52` | mov w9,#0xef | `FALL_THROUGH`
<a id="insn-00babe98"></a> `00babe98` | `6a 17 80 52` | mov w10,#0xbb | `FALL_THROUGH`
<a id="insn-00babe9c"></a> `00babe9c` | `a8 00 00 f9` | str x8,[x5] | `FALL_THROUGH`
<a id="insn-00babea0"></a> `00babea0` | `69 00 00 39` | strb w9,[x3] | `FALL_THROUGH`
<a id="insn-00babea4"></a> `00babea4` | `a8 00 40 f9` | ldr x8,[x5] | `FALL_THROUGH`
<a id="insn-00babea8"></a> `00babea8` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00babeac"></a> `00babeac` | `a9 00 00 f9` | str x9,[x5] | `FALL_THROUGH`
<a id="insn-00babeb0"></a> `00babeb0` | `0a 01 00 39` | strb w10,[x8] | `FALL_THROUGH`
<a id="insn-00babeb4"></a> `00babeb4` | `ea 17 80 52` | mov w10,#0xbf | `FALL_THROUGH`
<a id="insn-00babeb8"></a> `00babeb8` | `a8 00 40 f9` | ldr x8,[x5] | `FALL_THROUGH`
<a id="insn-00babebc"></a> `00babebc` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00babec0"></a> `00babec0` | `a9 00 00 f9` | str x9,[x5] | `FALL_THROUGH`
<a id="insn-00babec4"></a> `00babec4` | `0a 01 00 39` | strb w10,[x8] | `FALL_THROUGH`
<a id="insn-00babec8"></a> `00babec8` | `4a 00 40 f9` | ldr x10,[x2] | `FALL_THROUGH`
<a id="insn-00babecc"></a> `00babecc` | `5f 01 01 eb` | cmp x10,x1 | `FALL_THROUGH`
<a id="insn-00babed0"></a> `00babed0` | `42 0f 00 54` | b.cs 0x00bac0b8 | `CONDITIONAL_JUMP`
<a id="insn-00babed4"></a> `00babed4` | `08 80 9b 52` | mov w8,#0xdc00 | `FALL_THROUGH`
<a id="insn-00babed8"></a> `00babed8` | `17 00 00 14` | b 0x00babf34 | `UNCONDITIONAL_JUMP`
<a id="insn-00babedc"></a> `00babedc` | `2b 7d 4c d3` | ubfx x11,x9,#0xc,#0x14 | `FALL_THROUGH`
<a id="insn-00babee0"></a> `00babee0` | `4c 05 00 91` | add x12,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00babee4"></a> `00babee4` | `ac 00 00 f9` | str x12,[x5] | `FALL_THROUGH`
<a id="insn-00babee8"></a> `00babee8` | `6b 09 1b 32` | orr w11,w11,#0xe0 | `FALL_THROUGH`
<a id="insn-00babeec"></a> `00babeec` | `4b 01 00 39` | strb w11,[x10] | `FALL_THROUGH`
<a id="insn-00babef0"></a> `00babef0` | `2b 7d 46 d3` | ubfx x11,x9,#0x6,#0x1a | `FALL_THROUGH`
<a id="insn-00babef4"></a> `00babef4` | `aa 00 40 f9` | ldr x10,[x5] | `FALL_THROUGH`
<a id="insn-00babef8"></a> `00babef8` | `6b 79 19 12` | and w11,w11,#0xffffffbf | `FALL_THROUGH`
<a id="insn-00babefc"></a> `00babefc` | `4c 05 00 91` | add x12,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00babf00"></a> `00babf00` | `ac 00 00 f9` | str x12,[x5] | `FALL_THROUGH`
<a id="insn-00babf04"></a> `00babf04` | `4b 01 00 39` | strb w11,[x10] | `FALL_THROUGH`
<a id="insn-00babf08"></a> `00babf08` | `0b 10 80 52` | mov w11,#0x80 | `FALL_THROUGH`
<a id="insn-00babf0c"></a> `00babf0c` | `aa 00 40 f9` | ldr x10,[x5] | `FALL_THROUGH`
<a id="insn-00babf10"></a> `00babf10` | `2b 15 00 33` | bfxil w11,w9,#0x0,#0x6 | `FALL_THROUGH`
<a id="insn-00babf14"></a> `00babf14` | `49 05 00 91` | add x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00babf18"></a> `00babf18` | `a9 00 00 f9` | str x9,[x5] | `FALL_THROUGH`
<a id="insn-00babf1c"></a> `00babf1c` | `4b 01 00 39` | strb w11,[x10] | `FALL_THROUGH`
<a id="insn-00babf20"></a> `00babf20` | `49 00 40 f9` | ldr x9,[x2] | `FALL_THROUGH`
<a id="insn-00babf24"></a> `00babf24` | `2a 09 00 91` | add x10,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00babf28"></a> `00babf28` | `5f 01 01 eb` | cmp x10,x1 | `FALL_THROUGH`
<a id="insn-00babf2c"></a> `00babf2c` | `4a 00 00 f9` | str x10,[x2] | `FALL_THROUGH`
<a id="insn-00babf30"></a> `00babf30` | `42 0c 00 54` | b.cs 0x00bac0b8 | `CONDITIONAL_JUMP`
<a id="insn-00babf34"></a> `00babf34` | `49 01 40 79` | ldrh w9,[x10] | `FALL_THROUGH`
<a id="insn-00babf38"></a> `00babf38` | `3f 01 06 eb` | cmp x9,x6 | `FALL_THROUGH`
<a id="insn-00babf3c"></a> `00babf3c` | `28 0c 00 54` | b.hi 0x00bac0c0 | `CONDITIONAL_JUMP`
<a id="insn-00babf40"></a> `00babf40` | `3f fd 01 71` | cmp w9,#0x7f | `FALL_THROUGH`
<a id="insn-00babf44"></a> `00babf44` | `28 01 00 54` | b.hi 0x00babf68 | `CONDITIONAL_JUMP`
<a id="insn-00babf48"></a> `00babf48` | `aa 00 40 f9` | ldr x10,[x5] | `FALL_THROUGH`
<a id="insn-00babf4c"></a> `00babf4c` | `8b 00 0a cb` | sub x11,x4,x10 | `FALL_THROUGH`
<a id="insn-00babf50"></a> `00babf50` | `7f 05 00 f1` | cmp x11,#0x1 | `FALL_THROUGH`
<a id="insn-00babf54"></a> `00babf54` | `ab f9 ff 54` | b.lt 0x00babe88 | `CONDITIONAL_JUMP`
<a id="insn-00babf58"></a> `00babf58` | `4b 05 00 91` | add x11,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00babf5c"></a> `00babf5c` | `ab 00 00 f9` | str x11,[x5] | `FALL_THROUGH`
<a id="insn-00babf60"></a> `00babf60` | `49 01 00 39` | strb w9,[x10] | `FALL_THROUGH`
<a id="insn-00babf64"></a> `00babf64` | `ef ff ff 17` | b 0x00babf20 | `UNCONDITIONAL_JUMP`
<a id="insn-00babf68"></a> `00babf68` | `3f fd 1f 71` | cmp w9,#0x7ff | `FALL_THROUGH`
<a id="insn-00babf6c"></a> `00babf6c` | `48 01 00 54` | b.hi 0x00babf94 | `CONDITIONAL_JUMP`
<a id="insn-00babf70"></a> `00babf70` | `aa 00 40 f9` | ldr x10,[x5] | `FALL_THROUGH`
<a id="insn-00babf74"></a> `00babf74` | `8b 00 0a cb` | sub x11,x4,x10 | `FALL_THROUGH`
<a id="insn-00babf78"></a> `00babf78` | `7f 09 00 f1` | cmp x11,#0x2 | `FALL_THROUGH`
<a id="insn-00babf7c"></a> `00babf7c` | `6b f8 ff 54` | b.lt 0x00babe88 | `CONDITIONAL_JUMP`
<a id="insn-00babf80"></a> `00babf80` | `2b 7d 46 d3` | ubfx x11,x9,#0x6,#0x1a | `FALL_THROUGH`
<a id="insn-00babf84"></a> `00babf84` | `4c 05 00 91` | add x12,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00babf88"></a> `00babf88` | `ac 00 00 f9` | str x12,[x5] | `FALL_THROUGH`
<a id="insn-00babf8c"></a> `00babf8c` | `6b 05 1a 32` | orr w11,w11,#0xc0 | `FALL_THROUGH`
<a id="insn-00babf90"></a> `00babf90` | `dd ff ff 17` | b 0x00babf04 | `UNCONDITIONAL_JUMP`
<a id="insn-00babf94"></a> `00babf94` | `2b 7d 4b d3` | ubfx x11,x9,#0xb,#0x15 | `FALL_THROUGH`
<a id="insn-00babf98"></a> `00babf98` | `7f 69 00 71` | cmp w11,#0x1a | `FALL_THROUGH`
<a id="insn-00babf9c"></a> `00babf9c` | `c8 01 00 54` | b.hi 0x00babfd4 | `CONDITIONAL_JUMP`
<a id="insn-00babfa0"></a> `00babfa0` | `aa 00 40 f9` | ldr x10,[x5] | `FALL_THROUGH`
<a id="insn-00babfa4"></a> `00babfa4` | `8b 00 0a cb` | sub x11,x4,x10 | `FALL_THROUGH`
<a id="insn-00babfa8"></a> `00babfa8` | `7f 0d 00 f1` | cmp x11,#0x3 | `FALL_THROUGH`
<a id="insn-00babfac"></a> `00babfac` | `eb f6 ff 54` | b.lt 0x00babe88 | `CONDITIONAL_JUMP`
<a id="insn-00babfb0"></a> `00babfb0` | `2b 7d 4c d3` | ubfx x11,x9,#0xc,#0x14 | `FALL_THROUGH`
<a id="insn-00babfb4"></a> `00babfb4` | `4c 05 00 91` | add x12,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00babfb8"></a> `00babfb8` | `ac 00 00 f9` | str x12,[x5] | `FALL_THROUGH`
<a id="insn-00babfbc"></a> `00babfbc` | `6b 09 1b 32` | orr w11,w11,#0xe0 | `FALL_THROUGH`
<a id="insn-00babfc0"></a> `00babfc0` | `4b 01 00 39` | strb w11,[x10] | `FALL_THROUGH`
<a id="insn-00babfc4"></a> `00babfc4` | `0b 10 80 52` | mov w11,#0x80 | `FALL_THROUGH`
<a id="insn-00babfc8"></a> `00babfc8` | `aa 00 40 f9` | ldr x10,[x5] | `FALL_THROUGH`
<a id="insn-00babfcc"></a> `00babfcc` | `2b 2d 06 33` | bfxil w11,w9,#0x6,#0x6 | `FALL_THROUGH`
<a id="insn-00babfd0"></a> `00babfd0` | `cb ff ff 17` | b 0x00babefc | `UNCONDITIONAL_JUMP`
<a id="insn-00babfd4"></a> `00babfd4` | `2b 7d 4a d3` | ubfx x11,x9,#0xa,#0x16 | `FALL_THROUGH`
<a id="insn-00babfd8"></a> `00babfd8` | `7f d9 00 71` | cmp w11,#0x36 | `FALL_THROUGH`
<a id="insn-00babfdc"></a> `00babfdc` | `08 06 00 54` | b.hi 0x00bac09c | `CONDITIONAL_JUMP`
<a id="insn-00babfe0"></a> `00babfe0` | `2b 00 0a cb` | sub x11,x1,x10 | `FALL_THROUGH`
<a id="insn-00babfe4"></a> `00babfe4` | `7f 11 00 f1` | cmp x11,#0x4 | `FALL_THROUGH`
<a id="insn-00babfe8"></a> `00babfe8` | `0b f5 ff 54` | b.lt 0x00babe88 | `CONDITIONAL_JUMP`
<a id="insn-00babfec"></a> `00babfec` | `4b 2d 40 78` | ldrh w11,[x10, #0x2]! | `FALL_THROUGH`
<a id="insn-00babff0"></a> `00babff0` | `6c 15 16 12` | and w12,w11,#0xfc00 | `FALL_THROUGH`
<a id="insn-00babff4"></a> `00babff4` | `9f 01 08 6b` | cmp w12,w8 | `FALL_THROUGH`
<a id="insn-00babff8"></a> `00babff8` | `41 06 00 54` | b.ne 0x00bac0c0 | `CONDITIONAL_JUMP`
<a id="insn-00babffc"></a> `00babffc` | `ac 00 40 f9` | ldr x12,[x5] | `FALL_THROUGH`
<a id="insn-00bac000"></a> `00bac000` | `8c 00 0c cb` | sub x12,x4,x12 | `FALL_THROUGH`
<a id="insn-00bac004"></a> `00bac004` | `9f 11 00 f1` | cmp x12,#0x4 | `FALL_THROUGH`
<a id="insn-00bac008"></a> `00bac008` | `0b f4 ff 54` | b.lt 0x00babe88 | `CONDITIONAL_JUMP`
<a id="insn-00bac00c"></a> `00bac00c` | `ec 03 09 2a` | mov w12,w9 | `FALL_THROUGH`
<a id="insn-00bac010"></a> `00bac010` | `6d 25 40 92` | and x13,x11,#0x3ff | `FALL_THROUGH`
<a id="insn-00bac014"></a> `00bac014` | `8d 25 76 b3` | bfm x13,x12,#0x36,#0x9 | `FALL_THROUGH`
<a id="insn-00bac018"></a> `00bac018` | `ac 41 40 91` | add x12,x13,#0x10, LSL #12 | `FALL_THROUGH`
<a id="insn-00bac01c"></a> `00bac01c` | `9f 01 06 eb` | cmp x12,x6 | `FALL_THROUGH`
<a id="insn-00bac020"></a> `00bac020` | `08 05 00 54` | b.hi 0x00bac0c0 | `CONDITIONAL_JUMP`
<a id="insn-00bac024"></a> `00bac024` | `2c 25 06 53` | ubfx w12,w9,#0x6,#0x4 | `FALL_THROUGH`
<a id="insn-00bac028"></a> `00bac028` | `4a 00 00 f9` | str x10,[x2] | `FALL_THROUGH`
<a id="insn-00bac02c"></a> `00bac02c` | `aa 00 40 f9` | ldr x10,[x5] | `FALL_THROUGH`
<a id="insn-00bac030"></a> `00bac030` | `8c 05 00 11` | add w12,w12,#0x1 | `FALL_THROUGH`
<a id="insn-00bac034"></a> `00bac034` | `8d 7d 02 53` | lsr w13,w12,#0x2 | `FALL_THROUGH`
<a id="insn-00bac038"></a> `00bac038` | `4e 05 00 91` | add x14,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bac03c"></a> `00bac03c` | `8c 05 1c 53` | ubfiz w12,w12,#0x4,#0x2 | `FALL_THROUGH`
<a id="insn-00bac040"></a> `00bac040` | `ae 00 00 f9` | str x14,[x5] | `FALL_THROUGH`
<a id="insn-00bac044"></a> `00bac044` | `ad 0d 1c 32` | orr w13,w13,#0xf0 | `FALL_THROUGH`
<a id="insn-00bac048"></a> `00bac048` | `2c 15 02 33` | bfxil w12,w9,#0x2,#0x4 | `FALL_THROUGH`
<a id="insn-00bac04c"></a> `00bac04c` | `29 05 1c 53` | ubfiz w9,w9,#0x4,#0x2 | `FALL_THROUGH`
<a id="insn-00bac050"></a> `00bac050` | `4d 01 00 39` | strb w13,[x10] | `FALL_THROUGH`
<a id="insn-00bac054"></a> `00bac054` | `aa 00 40 f9` | ldr x10,[x5] | `FALL_THROUGH`
<a id="insn-00bac058"></a> `00bac058` | `8c 01 19 32` | orr w12,w12,#0x80 | `FALL_THROUGH`
<a id="insn-00bac05c"></a> `00bac05c` | `69 25 06 33` | bfxil w9,w11,#0x6,#0x4 | `FALL_THROUGH`
<a id="insn-00bac060"></a> `00bac060` | `4d 05 00 91` | add x13,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bac064"></a> `00bac064` | `29 01 19 32` | orr w9,w9,#0x80 | `FALL_THROUGH`
<a id="insn-00bac068"></a> `00bac068` | `ad 00 00 f9` | str x13,[x5] | `FALL_THROUGH`
<a id="insn-00bac06c"></a> `00bac06c` | `4c 01 00 39` | strb w12,[x10] | `FALL_THROUGH`
<a id="insn-00bac070"></a> `00bac070` | `aa 00 40 f9` | ldr x10,[x5] | `FALL_THROUGH`
<a id="insn-00bac074"></a> `00bac074` | `4c 05 00 91` | add x12,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bac078"></a> `00bac078` | `ac 00 00 f9` | str x12,[x5] | `FALL_THROUGH`
<a id="insn-00bac07c"></a> `00bac07c` | `49 01 00 39` | strb w9,[x10] | `FALL_THROUGH`
<a id="insn-00bac080"></a> `00bac080` | `0a 10 80 52` | mov w10,#0x80 | `FALL_THROUGH`
<a id="insn-00bac084"></a> `00bac084` | `a9 00 40 f9` | ldr x9,[x5] | `FALL_THROUGH`
<a id="insn-00bac088"></a> `00bac088` | `6a 15 00 33` | bfxil w10,w11,#0x0,#0x6 | `FALL_THROUGH`
<a id="insn-00bac08c"></a> `00bac08c` | `2b 05 00 91` | add x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac090"></a> `00bac090` | `ab 00 00 f9` | str x11,[x5] | `FALL_THROUGH`
<a id="insn-00bac094"></a> `00bac094` | `2a 01 00 39` | strb w10,[x9] | `FALL_THROUGH`
<a id="insn-00bac098"></a> `00bac098` | `a2 ff ff 17` | b 0x00babf20 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac09c"></a> `00bac09c` | `3f 39 40 71` | cmp w9,#0xe, LSL #12 | `FALL_THROUGH`
<a id="insn-00bac0a0"></a> `00bac0a0` | `03 01 00 54` | b.cc 0x00bac0c0 | `CONDITIONAL_JUMP`
<a id="insn-00bac0a4"></a> `00bac0a4` | `aa 00 40 f9` | ldr x10,[x5] | `FALL_THROUGH`
<a id="insn-00bac0a8"></a> `00bac0a8` | `8b 00 0a cb` | sub x11,x4,x10 | `FALL_THROUGH`
<a id="insn-00bac0ac"></a> `00bac0ac` | `7f 0d 00 f1` | cmp x11,#0x3 | `FALL_THROUGH`
<a id="insn-00bac0b0"></a> `00bac0b0` | `6a f1 ff 54` | b.ge 0x00babedc | `CONDITIONAL_JUMP`
<a id="insn-00bac0b4"></a> `00bac0b4` | `75 ff ff 17` | b 0x00babe88 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac0b8"></a> `00bac0b8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bac0bc"></a> `00bac0bc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bac0c0"></a> `00bac0c0` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00bac0c4"></a> `00bac0c4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00babe6c`](#insn-00babe6c) 範囲 `[['00babe6c', '00babe7b']]`
  - `CONDITIONAL_JUMP` [`00babe78`](#insn-00babe78) → [`00babec8`](#insn-00babec8)
  - `FALL_THROUGH` [`00babe78`](#insn-00babe78) → [`00babe7c`](#insn-00babe7c)
- ブロック [`00babe7c`](#insn-00babe7c) 範囲 `[['00babe7c', '00babe87']]`
  - `CONDITIONAL_JUMP` [`00babe84`](#insn-00babe84) → [`00babe90`](#insn-00babe90)
  - `FALL_THROUGH` [`00babe84`](#insn-00babe84) → [`00babe88`](#insn-00babe88)
- ブロック [`00babe88`](#insn-00babe88) 範囲 `[['00babe88', '00babe8f']]`
- ブロック [`00babe90`](#insn-00babe90) 範囲 `[['00babe90', '00babec7']]`
  - `FALL_THROUGH` [`00babec4`](#insn-00babec4) → [`00babec8`](#insn-00babec8)
- ブロック [`00babec8`](#insn-00babec8) 範囲 `[['00babec8', '00babed3']]`
  - `CONDITIONAL_JUMP` [`00babed0`](#insn-00babed0) → [`00bac0b8`](#insn-00bac0b8)
  - `FALL_THROUGH` [`00babed0`](#insn-00babed0) → [`00babed4`](#insn-00babed4)
- ブロック [`00babed4`](#insn-00babed4) 範囲 `[['00babed4', '00babedb']]`
  - `UNCONDITIONAL_JUMP` [`00babed8`](#insn-00babed8) → [`00babf34`](#insn-00babf34)
- ブロック [`00babedc`](#insn-00babedc) 範囲 `[['00babedc', '00babefb']]`
  - `FALL_THROUGH` [`00babef8`](#insn-00babef8) → [`00babefc`](#insn-00babefc)
- ブロック [`00babefc`](#insn-00babefc) 範囲 `[['00babefc', '00babf03']]`
  - `FALL_THROUGH` [`00babf00`](#insn-00babf00) → [`00babf04`](#insn-00babf04)
- ブロック [`00babf04`](#insn-00babf04) 範囲 `[['00babf04', '00babf1f']]`
  - `FALL_THROUGH` [`00babf1c`](#insn-00babf1c) → [`00babf20`](#insn-00babf20)
- ブロック [`00babf20`](#insn-00babf20) 範囲 `[['00babf20', '00babf33']]`
  - `CONDITIONAL_JUMP` [`00babf30`](#insn-00babf30) → [`00bac0b8`](#insn-00bac0b8)
  - `FALL_THROUGH` [`00babf30`](#insn-00babf30) → [`00babf34`](#insn-00babf34)
- ブロック [`00babf34`](#insn-00babf34) 範囲 `[['00babf34', '00babf3f']]`
  - `CONDITIONAL_JUMP` [`00babf3c`](#insn-00babf3c) → [`00bac0c0`](#insn-00bac0c0)
  - `FALL_THROUGH` [`00babf3c`](#insn-00babf3c) → [`00babf40`](#insn-00babf40)
- ブロック [`00babf40`](#insn-00babf40) 範囲 `[['00babf40', '00babf47']]`
  - `CONDITIONAL_JUMP` [`00babf44`](#insn-00babf44) → [`00babf68`](#insn-00babf68)
  - `FALL_THROUGH` [`00babf44`](#insn-00babf44) → [`00babf48`](#insn-00babf48)
- ブロック [`00babf48`](#insn-00babf48) 範囲 `[['00babf48', '00babf57']]`
  - `CONDITIONAL_JUMP` [`00babf54`](#insn-00babf54) → [`00babe88`](#insn-00babe88)
  - `FALL_THROUGH` [`00babf54`](#insn-00babf54) → [`00babf58`](#insn-00babf58)
- ブロック [`00babf58`](#insn-00babf58) 範囲 `[['00babf58', '00babf67']]`
  - `UNCONDITIONAL_JUMP` [`00babf64`](#insn-00babf64) → [`00babf20`](#insn-00babf20)
- ブロック [`00babf68`](#insn-00babf68) 範囲 `[['00babf68', '00babf6f']]`
  - `CONDITIONAL_JUMP` [`00babf6c`](#insn-00babf6c) → [`00babf94`](#insn-00babf94)
  - `FALL_THROUGH` [`00babf6c`](#insn-00babf6c) → [`00babf70`](#insn-00babf70)
- ブロック [`00babf70`](#insn-00babf70) 範囲 `[['00babf70', '00babf7f']]`
  - `CONDITIONAL_JUMP` [`00babf7c`](#insn-00babf7c) → [`00babe88`](#insn-00babe88)
  - `FALL_THROUGH` [`00babf7c`](#insn-00babf7c) → [`00babf80`](#insn-00babf80)
- ブロック [`00babf80`](#insn-00babf80) 範囲 `[['00babf80', '00babf93']]`
  - `UNCONDITIONAL_JUMP` [`00babf90`](#insn-00babf90) → [`00babf04`](#insn-00babf04)
- ブロック [`00babf94`](#insn-00babf94) 範囲 `[['00babf94', '00babf9f']]`
  - `CONDITIONAL_JUMP` [`00babf9c`](#insn-00babf9c) → [`00babfd4`](#insn-00babfd4)
  - `FALL_THROUGH` [`00babf9c`](#insn-00babf9c) → [`00babfa0`](#insn-00babfa0)
- ブロック [`00babfa0`](#insn-00babfa0) 範囲 `[['00babfa0', '00babfaf']]`
  - `CONDITIONAL_JUMP` [`00babfac`](#insn-00babfac) → [`00babe88`](#insn-00babe88)
  - `FALL_THROUGH` [`00babfac`](#insn-00babfac) → [`00babfb0`](#insn-00babfb0)
- ブロック [`00babfb0`](#insn-00babfb0) 範囲 `[['00babfb0', '00babfd3']]`
  - `UNCONDITIONAL_JUMP` [`00babfd0`](#insn-00babfd0) → [`00babefc`](#insn-00babefc)
- ブロック [`00babfd4`](#insn-00babfd4) 範囲 `[['00babfd4', '00babfdf']]`
  - `CONDITIONAL_JUMP` [`00babfdc`](#insn-00babfdc) → [`00bac09c`](#insn-00bac09c)
  - `FALL_THROUGH` [`00babfdc`](#insn-00babfdc) → [`00babfe0`](#insn-00babfe0)
- ブロック [`00babfe0`](#insn-00babfe0) 範囲 `[['00babfe0', '00babfeb']]`
  - `CONDITIONAL_JUMP` [`00babfe8`](#insn-00babfe8) → [`00babe88`](#insn-00babe88)
  - `FALL_THROUGH` [`00babfe8`](#insn-00babfe8) → [`00babfec`](#insn-00babfec)
- ブロック [`00babfec`](#insn-00babfec) 範囲 `[['00babfec', '00babffb']]`
  - `CONDITIONAL_JUMP` [`00babff8`](#insn-00babff8) → [`00bac0c0`](#insn-00bac0c0)
  - `FALL_THROUGH` [`00babff8`](#insn-00babff8) → [`00babffc`](#insn-00babffc)
- ブロック [`00babffc`](#insn-00babffc) 範囲 `[['00babffc', '00bac00b']]`
  - `CONDITIONAL_JUMP` [`00bac008`](#insn-00bac008) → [`00babe88`](#insn-00babe88)
  - `FALL_THROUGH` [`00bac008`](#insn-00bac008) → [`00bac00c`](#insn-00bac00c)
- ブロック [`00bac00c`](#insn-00bac00c) 範囲 `[['00bac00c', '00bac017']]`
  - `FALL_THROUGH` [`00bac014`](#insn-00bac014) → [`00bac018`](#insn-00bac018)
- ブロック [`00bac018`](#insn-00bac018) 範囲 `[['00bac018', '00bac023']]`
  - `CONDITIONAL_JUMP` [`00bac020`](#insn-00bac020) → [`00bac0c0`](#insn-00bac0c0)
  - `FALL_THROUGH` [`00bac020`](#insn-00bac020) → [`00bac024`](#insn-00bac024)
- ブロック [`00bac024`](#insn-00bac024) 範囲 `[['00bac024', '00bac033']]`
  - `FALL_THROUGH` [`00bac030`](#insn-00bac030) → [`00bac034`](#insn-00bac034)
- ブロック [`00bac034`](#insn-00bac034) 範囲 `[['00bac034', '00bac09b']]`
  - `UNCONDITIONAL_JUMP` [`00bac098`](#insn-00bac098) → [`00babf20`](#insn-00babf20)
- ブロック [`00bac09c`](#insn-00bac09c) 範囲 `[['00bac09c', '00bac0a3']]`
  - `CONDITIONAL_JUMP` [`00bac0a0`](#insn-00bac0a0) → [`00bac0c0`](#insn-00bac0c0)
  - `FALL_THROUGH` [`00bac0a0`](#insn-00bac0a0) → [`00bac0a4`](#insn-00bac0a4)
- ブロック [`00bac0a4`](#insn-00bac0a4) 範囲 `[['00bac0a4', '00bac0b3']]`
  - `CONDITIONAL_JUMP` [`00bac0b0`](#insn-00bac0b0) → [`00babedc`](#insn-00babedc)
  - `FALL_THROUGH` [`00bac0b0`](#insn-00bac0b0) → [`00bac0b4`](#insn-00bac0b4)
- ブロック [`00bac0b4`](#insn-00bac0b4) 範囲 `[['00bac0b4', '00bac0b7']]`
  - `UNCONDITIONAL_JUMP` [`00bac0b4`](#insn-00bac0b4) → [`00babe88`](#insn-00babe88)
- ブロック [`00bac0b8`](#insn-00bac0b8) 範囲 `[['00bac0b8', '00bac0bf']]`
- ブロック [`00bac0c0`](#insn-00bac0c0) 範囲 `[['00bac0c0', '00bac0c7']]`

## 命令位置別の参照

- [`00babe78`](#insn-00babe78) → [`00babec8`](#insn-00babec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babe84`](#insn-00babe84) → [`00babe90`](#insn-00babe90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babed0`](#insn-00babed0) → [`00bac0b8`](#insn-00bac0b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babed8`](#insn-00babed8) → [`00babf34`](#insn-00babf34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf30`](#insn-00babf30) → [`00bac0b8`](#insn-00bac0b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf3c`](#insn-00babf3c) → [`00bac0c0`](#insn-00bac0c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf44`](#insn-00babf44) → [`00babf68`](#insn-00babf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf54`](#insn-00babf54) → [`00babe88`](#insn-00babe88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf64`](#insn-00babf64) → [`00babf20`](#insn-00babf20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf6c`](#insn-00babf6c) → [`00babf94`](#insn-00babf94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf7c`](#insn-00babf7c) → [`00babe88`](#insn-00babe88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf90`](#insn-00babf90) → [`00babf04`](#insn-00babf04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf9c`](#insn-00babf9c) → [`00babfd4`](#insn-00babfd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babfac`](#insn-00babfac) → [`00babe88`](#insn-00babe88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babfd0`](#insn-00babfd0) → [`00babefc`](#insn-00babefc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babfdc`](#insn-00babfdc) → [`00bac09c`](#insn-00bac09c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babfe8`](#insn-00babfe8) → [`00babe88`](#insn-00babe88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babff8`](#insn-00babff8) → [`00bac0c0`](#insn-00bac0c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac008`](#insn-00bac008) → [`00babe88`](#insn-00babe88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac020`](#insn-00bac020) → [`00bac0c0`](#insn-00bac0c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac098`](#insn-00bac098) → [`00babf20`](#insn-00babf20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac0a0`](#insn-00bac0a0) → [`00bac0c0`](#insn-00bac0c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac0b0`](#insn-00bac0b0) → [`00babedc`](#insn-00babedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac0b4`](#insn-00bac0b4) → [`00babe88`](#insn-00babe88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00babe78`](#insn-00babe78)

~~~json
{
  "source": "00babe78",
  "target": "00babec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babe84`](#insn-00babe84)

~~~json
{
  "source": "00babe84",
  "target": "00babe90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babed0`](#insn-00babed0)

~~~json
{
  "source": "00babed0",
  "target": "00bac0b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babed8`](#insn-00babed8)

~~~json
{
  "source": "00babed8",
  "target": "00babf34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf30`](#insn-00babf30)

~~~json
{
  "source": "00babf30",
  "target": "00bac0b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf3c`](#insn-00babf3c)

~~~json
{
  "source": "00babf3c",
  "target": "00bac0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf44`](#insn-00babf44)

~~~json
{
  "source": "00babf44",
  "target": "00babf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf54`](#insn-00babf54)

~~~json
{
  "source": "00babf54",
  "target": "00babe88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf64`](#insn-00babf64)

~~~json
{
  "source": "00babf64",
  "target": "00babf20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf6c`](#insn-00babf6c)

~~~json
{
  "source": "00babf6c",
  "target": "00babf94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf7c`](#insn-00babf7c)

~~~json
{
  "source": "00babf7c",
  "target": "00babe88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf90`](#insn-00babf90)

~~~json
{
  "source": "00babf90",
  "target": "00babf04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf9c`](#insn-00babf9c)

~~~json
{
  "source": "00babf9c",
  "target": "00babfd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfac`](#insn-00babfac)

~~~json
{
  "source": "00babfac",
  "target": "00babe88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfd0`](#insn-00babfd0)

~~~json
{
  "source": "00babfd0",
  "target": "00babefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfdc`](#insn-00babfdc)

~~~json
{
  "source": "00babfdc",
  "target": "00bac09c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfe8`](#insn-00babfe8)

~~~json
{
  "source": "00babfe8",
  "target": "00babe88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babff8`](#insn-00babff8)

~~~json
{
  "source": "00babff8",
  "target": "00bac0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac008`](#insn-00bac008)

~~~json
{
  "source": "00bac008",
  "target": "00babe88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac020`](#insn-00bac020)

~~~json
{
  "source": "00bac020",
  "target": "00bac0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac098`](#insn-00bac098)

~~~json
{
  "source": "00bac098",
  "target": "00babf20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac0a0`](#insn-00bac0a0)

~~~json
{
  "source": "00bac0a0",
  "target": "00bac0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac0b0`](#insn-00bac0b0)

~~~json
{
  "source": "00bac0b0",
  "target": "00babedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac0b4`](#insn-00bac0b4)

~~~json
{
  "source": "00bac0b4",
  "target": "00babe88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
