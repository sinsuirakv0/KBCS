# 00bacd2c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bacce8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bacce8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0023.md#compare-ef782359a59c81f650a1cf80c6d95f89)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c29774`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29774.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0019.md#compare-a7e49494bdd3d20489479c48952f01d8)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bacd2c",
  "name": "FUN_00bacd2c",
  "size": 484,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f0ac4bbfd68c02383eab12320141fc0e3bb1096f398c26ed357e1bffe81be020",
  "source_text_sha256": "f0ac4bbfd68c02383eab12320141fc0e3bb1096f398c26ed357e1bffe81be020",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bacd2c",
        "00bacf0f"
      ]
    ],
    "bytes_sha256": "d7378fad7366733ca6da86eb8e588679bcef74e3898ed8ad6fcadaec1a990742",
    "instruction_count": 121,
    "instruction_bytes": 484,
    "body_bytes": 484,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bacd10](../00bac/00bacd10.md)
- [00bad100](../00bad/00bad100.md)
- [00bad230](../00bad/00bad230.md)
- [00bad7c0](../00bad/00bad7c0.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3197 bytes

~~~c

int FUN_00bacd2c(byte *param_1,byte *param_2,ulong param_3,ulong param_4,uint param_5)

{
  byte bVar1;
  bool bVar2;
  byte *pbVar3;
  ulong uVar4;
  uint uVar5;
  long lVar6;
  uint uVar7;
  uint uVar8;
  
  pbVar3 = param_1;
  if ((((2 < (long)param_2 - (long)param_1) && ((param_5 >> 2 & 1) != 0)) && (*param_1 == 0xef)) &&
     (param_1[1] == 0xbb)) {
    lVar6 = 3;
    if (param_1[2] != 0xbf) {
      lVar6 = 0;
    }
    pbVar3 = param_1 + lVar6;
  }
  if ((pbVar3 < param_2) && (param_3 != 0)) {
    uVar4 = 1;
    do {
      bVar1 = *pbVar3;
                    /* try { // try from 00bacd90 to 00cace8b has its CatchHandler @ 00bacd90
                       catch() { ... } // from try @ 00bacd90 with catch @ 00bacd90
                       catch() { ... } // from try @ 00bacef4 with catch @ 00bacd90
                       catch() { ... } // from try @ 00bacf84 with catch @ 00bacd90 */
      if ((char)bVar1 < '\0') {
        if (bVar1 < 0xc2) break;
        uVar5 = (uint)bVar1;
        if (bVar1 < 0xe0) {
          if ((((long)param_2 - (long)pbVar3 < 2) || ((pbVar3[1] & 0xc0) != 0x80)) ||
             (param_4 < (pbVar3[1] & 0x3f | (uVar5 & 0x1f) << 6))) break;
          lVar6 = 2;
        }
        else if (bVar1 < 0xf0) {
          if ((long)param_2 - (long)pbVar3 < 3) break;
          uVar7 = (uint)pbVar3[1];
          if (uVar5 == 0xed) {
            uVar8 = uVar7 & 0xe0;
LAB_00bace78:
            if (uVar8 != 0x80) break;
          }
          else {
            if (uVar5 != 0xe0) {
              uVar8 = uVar7 & 0xc0;
              goto LAB_00bace78;
            }
            if ((uVar7 & 0xe0) != 0xa0) break;
          }
                    /* try { // try from 00bace8c to 00cace97 has its CatchHandler @ 00bad074 */
                    /* try { // try from 00bace9c to 00caceaf has its CatchHandler @ 00bad054 */
          if (((pbVar3[2] & 0xc0) != 0x80) ||
             (param_4 < ((uVar5 & 0xf) << 0xc | (uVar7 & 0x3f) << 6 | pbVar3[2] & 0x3f))) break;
          lVar6 = 3;
        }
        else {
          if ((0xf4 < bVar1) || ((long)param_2 - (long)pbVar3 < 4)) break;
          uVar7 = (uint)pbVar3[1];
          if (uVar5 == 0xf4) {
            uVar8 = uVar7 & 0xf0;
LAB_00baceb4:
            if (uVar8 != 0x80) break;
          }
          else {
            if (uVar5 != 0xf0) {
              uVar8 = uVar7 & 0xc0;
              goto LAB_00baceb4;
            }
            if (0x2f < uVar7 - 0x90) break;
          }
                    /* try { // try from 00baced0 to 00cacef3 has its CatchHandler @ 00bad084 */
          if ((((pbVar3[2] & 0xc0) != 0x80) || ((pbVar3[3] & 0xc0) != 0x80)) ||
             (param_4 < ((uVar5 & 7) << 0x12 | (uVar7 & 0x3f) << 0xc | (pbVar3[2] & 0x3f) << 6 |
                        pbVar3[3] & 0x3f))) break;
          lVar6 = 4;
        }
      }
      else {
        if (param_4 < bVar1) break;
        lVar6 = 1;
      }
      pbVar3 = pbVar3 + lVar6;
                    /* try { // try from 00bacef4 to 00cacf33 has its CatchHandler @ 00bacd90 */
      if ((param_2 <= pbVar3) || (bVar2 = param_3 <= uVar4, uVar4 = uVar4 + 1, bVar2)) break;
    } while( true );
  }
  return (int)pbVar3 - (int)param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bacd2c"></a> `00bacd2c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bacd30"></a> `00bacd30` | `28 00 00 cb` | sub x8,x1,x0 | `FALL_THROUGH`
<a id="insn-00bacd34"></a> `00bacd34` | `1f 0d 00 f1` | cmp x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bacd38"></a> `00bacd38` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bacd3c"></a> `00bacd3c` | `0b 02 00 54` | b.lt 0x00bacd7c | `CONDITIONAL_JUMP`
<a id="insn-00bacd40"></a> `00bacd40` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bacd44"></a> `00bacd44` | `c4 01 10 36` | tbz w4,#0x2,0x00bacd7c | `CONDITIONAL_JUMP`
<a id="insn-00bacd48"></a> `00bacd48` | `08 00 40 39` | ldrb w8,[x0] | `FALL_THROUGH`
<a id="insn-00bacd4c"></a> `00bacd4c` | `1f bd 03 71` | cmp w8,#0xef | `FALL_THROUGH`
<a id="insn-00bacd50"></a> `00bacd50` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bacd54"></a> `00bacd54` | `41 01 00 54` | b.ne 0x00bacd7c | `CONDITIONAL_JUMP`
<a id="insn-00bacd58"></a> `00bacd58` | `08 04 40 39` | ldrb w8,[x0, #0x1] | `FALL_THROUGH`
<a id="insn-00bacd5c"></a> `00bacd5c` | `1f ed 02 71` | cmp w8,#0xbb | `FALL_THROUGH`
<a id="insn-00bacd60"></a> `00bacd60` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bacd64"></a> `00bacd64` | `c1 00 00 54` | b.ne 0x00bacd7c | `CONDITIONAL_JUMP`
<a id="insn-00bacd68"></a> `00bacd68` | `08 08 40 39` | ldrb w8,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00bacd6c"></a> `00bacd6c` | `1f fd 02 71` | cmp w8,#0xbf | `FALL_THROUGH`
<a id="insn-00bacd70"></a> `00bacd70` | `68 00 80 52` | mov w8,#0x3 | `FALL_THROUGH`
<a id="insn-00bacd74"></a> `00bacd74` | `08 01 9f 9a` | csel x8,x8,xzr,eq | `FALL_THROUGH`
<a id="insn-00bacd78"></a> `00bacd78` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bacd7c"></a> `00bacd7c` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00bacd80"></a> `00bacd80` | `42 0c 00 54` | b.cs 0x00bacf08 | `CONDITIONAL_JUMP`
<a id="insn-00bacd84"></a> `00bacd84` | `22 0c 00 b4` | cbz x2,0x00bacf08 | `CONDITIONAL_JUMP`
<a id="insn-00bacd88"></a> `00bacd88` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacd8c"></a> `00bacd8c` | `0a 01 c0 39` | ldrsb w10,[x8] | `FALL_THROUGH`
<a id="insn-00bacd90"></a> `00bacd90` | `ca 00 f8 37` | tbnz w10,#0x1f,0x00bacda8 | `CONDITIONAL_JUMP`
<a id="insn-00bacd94"></a> `00bacd94` | `4a 1d 40 92` | and x10,x10,#0xff | `FALL_THROUGH`
<a id="insn-00bacd98"></a> `00bacd98` | `5f 01 03 eb` | cmp x10,x3 | `FALL_THROUGH`
<a id="insn-00bacd9c"></a> `00bacd9c` | `68 0b 00 54` | b.hi 0x00bacf08 | `CONDITIONAL_JUMP`
<a id="insn-00bacda0"></a> `00bacda0` | `2a 00 80 52` | mov w10,#0x1 | `FALL_THROUGH`
<a id="insn-00bacda4"></a> `00bacda4` | `53 00 00 14` | b 0x00bacef0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacda8"></a> `00bacda8` | `4a 1d 00 12` | and w10,w10,#0xff | `FALL_THROUGH`
<a id="insn-00bacdac"></a> `00bacdac` | `5f 09 03 71` | cmp w10,#0xc2 | `FALL_THROUGH`
<a id="insn-00bacdb0"></a> `00bacdb0` | `c3 0a 00 54` | b.cc 0x00bacf08 | `CONDITIONAL_JUMP`
<a id="insn-00bacdb4"></a> `00bacdb4` | `5f 7d 03 71` | cmp w10,#0xdf | `FALL_THROUGH`
<a id="insn-00bacdb8"></a> `00bacdb8` | `c8 01 00 54` | b.hi 0x00bacdf0 | `CONDITIONAL_JUMP`
<a id="insn-00bacdbc"></a> `00bacdbc` | `2b 00 08 cb` | sub x11,x1,x8 | `FALL_THROUGH`
<a id="insn-00bacdc0"></a> `00bacdc0` | `7f 09 00 f1` | cmp x11,#0x2 | `FALL_THROUGH`
<a id="insn-00bacdc4"></a> `00bacdc4` | `2b 0a 00 54` | b.lt 0x00bacf08 | `CONDITIONAL_JUMP`
<a id="insn-00bacdc8"></a> `00bacdc8` | `0b 05 40 39` | ldrb w11,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bacdcc"></a> `00bacdcc` | `6c 05 1a 12` | and w12,w11,#0xc0 | `FALL_THROUGH`
<a id="insn-00bacdd0"></a> `00bacdd0` | `9f 01 02 71` | cmp w12,#0x80 | `FALL_THROUGH`
<a id="insn-00bacdd4"></a> `00bacdd4` | `a1 09 00 54` | b.ne 0x00bacf08 | `CONDITIONAL_JUMP`
<a id="insn-00bacdd8"></a> `00bacdd8` | `6b 15 00 12` | and w11,w11,#0x3f | `FALL_THROUGH`
<a id="insn-00bacddc"></a> `00bacddc` | `4b 11 1a 33` | bfm w11,w10,#0x1a,#0x4 | `FALL_THROUGH`
<a id="insn-00bacde0"></a> `00bacde0` | `7f 01 03 eb` | cmp x11,x3 | `FALL_THROUGH`
<a id="insn-00bacde4"></a> `00bacde4` | `28 09 00 54` | b.hi 0x00bacf08 | `CONDITIONAL_JUMP`
<a id="insn-00bacde8"></a> `00bacde8` | `4a 00 80 52` | mov w10,#0x2 | `FALL_THROUGH`
<a id="insn-00bacdec"></a> `00bacdec` | `41 00 00 14` | b 0x00bacef0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacdf0"></a> `00bacdf0` | `5f bd 03 71` | cmp w10,#0xef | `FALL_THROUGH`
<a id="insn-00bacdf4"></a> `00bacdf4` | `c8 01 00 54` | b.hi 0x00bace2c | `CONDITIONAL_JUMP`
<a id="insn-00bacdf8"></a> `00bacdf8` | `2b 00 08 cb` | sub x11,x1,x8 | `FALL_THROUGH`
<a id="insn-00bacdfc"></a> `00bacdfc` | `7f 0d 00 f1` | cmp x11,#0x3 | `FALL_THROUGH`
<a id="insn-00bace00"></a> `00bace00` | `4b 08 00 54` | b.lt 0x00bacf08 | `CONDITIONAL_JUMP`
<a id="insn-00bace04"></a> `00bace04` | `0c 05 40 39` | ldrb w12,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bace08"></a> `00bace08` | `0b 09 40 39` | ldrb w11,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00bace0c"></a> `00bace0c` | `5f b5 03 71` | cmp w10,#0xed | `FALL_THROUGH`
<a id="insn-00bace10"></a> `00bace10` | `e0 02 00 54` | b.eq 0x00bace6c | `CONDITIONAL_JUMP`
<a id="insn-00bace14"></a> `00bace14` | `5f 81 03 71` | cmp w10,#0xe0 | `FALL_THROUGH`
<a id="insn-00bace18"></a> `00bace18` | `e1 02 00 54` | b.ne 0x00bace74 | `CONDITIONAL_JUMP`
<a id="insn-00bace1c"></a> `00bace1c` | `8d 09 1b 12` | and w13,w12,#0xe0 | `FALL_THROUGH`
<a id="insn-00bace20"></a> `00bace20` | `bf 81 02 71` | cmp w13,#0xa0 | `FALL_THROUGH`
<a id="insn-00bace24"></a> `00bace24` | `e0 02 00 54` | b.eq 0x00bace80 | `CONDITIONAL_JUMP`
<a id="insn-00bace28"></a> `00bace28` | `38 00 00 14` | b 0x00bacf08 | `UNCONDITIONAL_JUMP`
<a id="insn-00bace2c"></a> `00bace2c` | `5f d1 03 71` | cmp w10,#0xf4 | `FALL_THROUGH`
<a id="insn-00bace30"></a> `00bace30` | `c8 06 00 54` | b.hi 0x00bacf08 | `CONDITIONAL_JUMP`
<a id="insn-00bace34"></a> `00bace34` | `2b 00 08 cb` | sub x11,x1,x8 | `FALL_THROUGH`
<a id="insn-00bace38"></a> `00bace38` | `7f 11 00 f1` | cmp x11,#0x4 | `FALL_THROUGH`
<a id="insn-00bace3c"></a> `00bace3c` | `6b 06 00 54` | b.lt 0x00bacf08 | `CONDITIONAL_JUMP`
<a id="insn-00bace40"></a> `00bace40` | `0c 05 40 39` | ldrb w12,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bace44"></a> `00bace44` | `0b 09 40 39` | ldrb w11,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00bace48"></a> `00bace48` | `5f d1 03 71` | cmp w10,#0xf4 | `FALL_THROUGH`
<a id="insn-00bace4c"></a> `00bace4c` | `0d 0d 40 39` | ldrb w13,[x8, #0x3] | `FALL_THROUGH`
<a id="insn-00bace50"></a> `00bace50` | `c0 02 00 54` | b.eq 0x00bacea8 | `CONDITIONAL_JUMP`
<a id="insn-00bace54"></a> `00bace54` | `5f c1 03 71` | cmp w10,#0xf0 | `FALL_THROUGH`
<a id="insn-00bace58"></a> `00bace58` | `c1 02 00 54` | b.ne 0x00baceb0 | `CONDITIONAL_JUMP`
<a id="insn-00bace5c"></a> `00bace5c` | `8e 41 02 51` | sub w14,w12,#0x90 | `FALL_THROUGH`
<a id="insn-00bace60"></a> `00bace60` | `df c1 00 71` | cmp w14,#0x30 | `FALL_THROUGH`
<a id="insn-00bace64"></a> `00bace64` | `c3 02 00 54` | b.cc 0x00bacebc | `CONDITIONAL_JUMP`
<a id="insn-00bace68"></a> `00bace68` | `28 00 00 14` | b 0x00bacf08 | `UNCONDITIONAL_JUMP`
<a id="insn-00bace6c"></a> `00bace6c` | `8d 09 1b 12` | and w13,w12,#0xe0 | `FALL_THROUGH`
<a id="insn-00bace70"></a> `00bace70` | `02 00 00 14` | b 0x00bace78 | `UNCONDITIONAL_JUMP`
<a id="insn-00bace74"></a> `00bace74` | `8d 05 1a 12` | and w13,w12,#0xc0 | `FALL_THROUGH`
<a id="insn-00bace78"></a> `00bace78` | `bf 01 02 71` | cmp w13,#0x80 | `FALL_THROUGH`
<a id="insn-00bace7c"></a> `00bace7c` | `61 04 00 54` | b.ne 0x00bacf08 | `CONDITIONAL_JUMP`
<a id="insn-00bace80"></a> `00bace80` | `6d 05 1a 12` | and w13,w11,#0xc0 | `FALL_THROUGH`
<a id="insn-00bace84"></a> `00bace84` | `bf 01 02 71` | cmp w13,#0x80 | `FALL_THROUGH`
<a id="insn-00bace88"></a> `00bace88` | `01 04 00 54` | b.ne 0x00bacf08 | `CONDITIONAL_JUMP`
<a id="insn-00bace8c"></a> `00bace8c` | `4a 0d 14 53` | ubfiz w10,w10,#0xc,#0x4 | `FALL_THROUGH`
<a id="insn-00bace90"></a> `00bace90` | `8a 15 1a 33` | bfm w10,w12,#0x1a,#0x5 | `FALL_THROUGH`
<a id="insn-00bace94"></a> `00bace94` | `6a 15 00 33` | bfxil w10,w11,#0x0,#0x6 | `FALL_THROUGH`
<a id="insn-00bace98"></a> `00bace98` | `5f 01 03 eb` | cmp x10,x3 | `FALL_THROUGH`
<a id="insn-00bace9c"></a> `00bace9c` | `68 03 00 54` | b.hi 0x00bacf08 | `CONDITIONAL_JUMP`
<a id="insn-00bacea0"></a> `00bacea0` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00bacea4"></a> `00bacea4` | `13 00 00 14` | b 0x00bacef0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacea8"></a> `00bacea8` | `8e 0d 1c 12` | and w14,w12,#0xf0 | `FALL_THROUGH`
<a id="insn-00baceac"></a> `00baceac` | `02 00 00 14` | b 0x00baceb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00baceb0"></a> `00baceb0` | `8e 05 1a 12` | and w14,w12,#0xc0 | `FALL_THROUGH`
<a id="insn-00baceb4"></a> `00baceb4` | `df 01 02 71` | cmp w14,#0x80 | `FALL_THROUGH`
<a id="insn-00baceb8"></a> `00baceb8` | `81 02 00 54` | b.ne 0x00bacf08 | `CONDITIONAL_JUMP`
<a id="insn-00bacebc"></a> `00bacebc` | `6e 05 1a 12` | and w14,w11,#0xc0 | `FALL_THROUGH`
<a id="insn-00bacec0"></a> `00bacec0` | `df 01 02 71` | cmp w14,#0x80 | `FALL_THROUGH`
<a id="insn-00bacec4"></a> `00bacec4` | `21 02 00 54` | b.ne 0x00bacf08 | `CONDITIONAL_JUMP`
<a id="insn-00bacec8"></a> `00bacec8` | `ae 05 1a 12` | and w14,w13,#0xc0 | `FALL_THROUGH`
<a id="insn-00bacecc"></a> `00bacecc` | `df 01 02 71` | cmp w14,#0x80 | `FALL_THROUGH`
<a id="insn-00baced0"></a> `00baced0` | `c1 01 00 54` | b.ne 0x00bacf08 | `CONDITIONAL_JUMP`
<a id="insn-00baced4"></a> `00baced4` | `4a 09 0e 53` | ubfiz w10,w10,#0x12,#0x3 | `FALL_THROUGH`
<a id="insn-00baced8"></a> `00baced8` | `8a 15 14 33` | bfm w10,w12,#0x14,#0x5 | `FALL_THROUGH`
<a id="insn-00bacedc"></a> `00bacedc` | `6a 15 1a 33` | bfm w10,w11,#0x1a,#0x5 | `FALL_THROUGH`
<a id="insn-00bacee0"></a> `00bacee0` | `aa 15 00 33` | bfxil w10,w13,#0x0,#0x6 | `FALL_THROUGH`
<a id="insn-00bacee4"></a> `00bacee4` | `5f 01 03 eb` | cmp x10,x3 | `FALL_THROUGH`
<a id="insn-00bacee8"></a> `00bacee8` | `08 01 00 54` | b.hi 0x00bacf08 | `CONDITIONAL_JUMP`
<a id="insn-00baceec"></a> `00baceec` | `8a 00 80 52` | mov w10,#0x4 | `FALL_THROUGH`
<a id="insn-00bacef0"></a> `00bacef0` | `08 01 0a 8b` | add x8,x8,x10 | `FALL_THROUGH`
<a id="insn-00bacef4"></a> `00bacef4` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00bacef8"></a> `00bacef8` | `82 00 00 54` | b.cs 0x00bacf08 | `CONDITIONAL_JUMP`
<a id="insn-00bacefc"></a> `00bacefc` | `3f 01 02 eb` | cmp x9,x2 | `FALL_THROUGH`
<a id="insn-00bacf00"></a> `00bacf00` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacf04"></a> `00bacf04` | `43 f4 ff 54` | b.cc 0x00bacd8c | `CONDITIONAL_JUMP`
<a id="insn-00bacf08"></a> `00bacf08` | `00 01 00 4b` | sub w0,w8,w0 | `FALL_THROUGH`
<a id="insn-00bacf0c"></a> `00bacf0c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bacd2c`](#insn-00bacd2c) 範囲 `[['00bacd2c', '00bacd3f']]`
  - `CONDITIONAL_JUMP` [`00bacd3c`](#insn-00bacd3c) → [`00bacd7c`](#insn-00bacd7c)
  - `FALL_THROUGH` [`00bacd3c`](#insn-00bacd3c) → [`00bacd40`](#insn-00bacd40)
- ブロック [`00bacd40`](#insn-00bacd40) 範囲 `[['00bacd40', '00bacd47']]`
  - `CONDITIONAL_JUMP` [`00bacd44`](#insn-00bacd44) → [`00bacd7c`](#insn-00bacd7c)
  - `FALL_THROUGH` [`00bacd44`](#insn-00bacd44) → [`00bacd48`](#insn-00bacd48)
- ブロック [`00bacd48`](#insn-00bacd48) 範囲 `[['00bacd48', '00bacd57']]`
  - `CONDITIONAL_JUMP` [`00bacd54`](#insn-00bacd54) → [`00bacd7c`](#insn-00bacd7c)
  - `FALL_THROUGH` [`00bacd54`](#insn-00bacd54) → [`00bacd58`](#insn-00bacd58)
- ブロック [`00bacd58`](#insn-00bacd58) 範囲 `[['00bacd58', '00bacd67']]`
  - `CONDITIONAL_JUMP` [`00bacd64`](#insn-00bacd64) → [`00bacd7c`](#insn-00bacd7c)
  - `FALL_THROUGH` [`00bacd64`](#insn-00bacd64) → [`00bacd68`](#insn-00bacd68)
- ブロック [`00bacd68`](#insn-00bacd68) 範囲 `[['00bacd68', '00bacd7b']]`
  - `FALL_THROUGH` [`00bacd78`](#insn-00bacd78) → [`00bacd7c`](#insn-00bacd7c)
- ブロック [`00bacd7c`](#insn-00bacd7c) 範囲 `[['00bacd7c', '00bacd83']]`
  - `CONDITIONAL_JUMP` [`00bacd80`](#insn-00bacd80) → [`00bacf08`](#insn-00bacf08)
  - `FALL_THROUGH` [`00bacd80`](#insn-00bacd80) → [`00bacd84`](#insn-00bacd84)
- ブロック [`00bacd84`](#insn-00bacd84) 範囲 `[['00bacd84', '00bacd87']]`
  - `CONDITIONAL_JUMP` [`00bacd84`](#insn-00bacd84) → [`00bacf08`](#insn-00bacf08)
  - `FALL_THROUGH` [`00bacd84`](#insn-00bacd84) → [`00bacd88`](#insn-00bacd88)
- ブロック [`00bacd88`](#insn-00bacd88) 範囲 `[['00bacd88', '00bacd8b']]`
  - `FALL_THROUGH` [`00bacd88`](#insn-00bacd88) → [`00bacd8c`](#insn-00bacd8c)
- ブロック [`00bacd8c`](#insn-00bacd8c) 範囲 `[['00bacd8c', '00bacd8f']]`
  - `FALL_THROUGH` [`00bacd8c`](#insn-00bacd8c) → [`00bacd90`](#insn-00bacd90)
- ブロック [`00bacd90`](#insn-00bacd90) 範囲 `[['00bacd90', '00bacd93']]`
  - `CONDITIONAL_JUMP` [`00bacd90`](#insn-00bacd90) → [`00bacda8`](#insn-00bacda8)
  - `FALL_THROUGH` [`00bacd90`](#insn-00bacd90) → [`00bacd94`](#insn-00bacd94)
- ブロック [`00bacd94`](#insn-00bacd94) 範囲 `[['00bacd94', '00bacd9f']]`
  - `CONDITIONAL_JUMP` [`00bacd9c`](#insn-00bacd9c) → [`00bacf08`](#insn-00bacf08)
  - `FALL_THROUGH` [`00bacd9c`](#insn-00bacd9c) → [`00bacda0`](#insn-00bacda0)
- ブロック [`00bacda0`](#insn-00bacda0) 範囲 `[['00bacda0', '00bacda7']]`
  - `UNCONDITIONAL_JUMP` [`00bacda4`](#insn-00bacda4) → [`00bacef0`](#insn-00bacef0)
- ブロック [`00bacda8`](#insn-00bacda8) 範囲 `[['00bacda8', '00bacdb3']]`
  - `CONDITIONAL_JUMP` [`00bacdb0`](#insn-00bacdb0) → [`00bacf08`](#insn-00bacf08)
  - `FALL_THROUGH` [`00bacdb0`](#insn-00bacdb0) → [`00bacdb4`](#insn-00bacdb4)
- ブロック [`00bacdb4`](#insn-00bacdb4) 範囲 `[['00bacdb4', '00bacdbb']]`
  - `CONDITIONAL_JUMP` [`00bacdb8`](#insn-00bacdb8) → [`00bacdf0`](#insn-00bacdf0)
  - `FALL_THROUGH` [`00bacdb8`](#insn-00bacdb8) → [`00bacdbc`](#insn-00bacdbc)
- ブロック [`00bacdbc`](#insn-00bacdbc) 範囲 `[['00bacdbc', '00bacdc7']]`
  - `CONDITIONAL_JUMP` [`00bacdc4`](#insn-00bacdc4) → [`00bacf08`](#insn-00bacf08)
  - `FALL_THROUGH` [`00bacdc4`](#insn-00bacdc4) → [`00bacdc8`](#insn-00bacdc8)
- ブロック [`00bacdc8`](#insn-00bacdc8) 範囲 `[['00bacdc8', '00bacdd7']]`
  - `CONDITIONAL_JUMP` [`00bacdd4`](#insn-00bacdd4) → [`00bacf08`](#insn-00bacf08)
  - `FALL_THROUGH` [`00bacdd4`](#insn-00bacdd4) → [`00bacdd8`](#insn-00bacdd8)
- ブロック [`00bacdd8`](#insn-00bacdd8) 範囲 `[['00bacdd8', '00bacde7']]`
  - `CONDITIONAL_JUMP` [`00bacde4`](#insn-00bacde4) → [`00bacf08`](#insn-00bacf08)
  - `FALL_THROUGH` [`00bacde4`](#insn-00bacde4) → [`00bacde8`](#insn-00bacde8)
- ブロック [`00bacde8`](#insn-00bacde8) 範囲 `[['00bacde8', '00bacdef']]`
  - `UNCONDITIONAL_JUMP` [`00bacdec`](#insn-00bacdec) → [`00bacef0`](#insn-00bacef0)
- ブロック [`00bacdf0`](#insn-00bacdf0) 範囲 `[['00bacdf0', '00bacdf7']]`
  - `CONDITIONAL_JUMP` [`00bacdf4`](#insn-00bacdf4) → [`00bace2c`](#insn-00bace2c)
  - `FALL_THROUGH` [`00bacdf4`](#insn-00bacdf4) → [`00bacdf8`](#insn-00bacdf8)
- ブロック [`00bacdf8`](#insn-00bacdf8) 範囲 `[['00bacdf8', '00bace03']]`
  - `CONDITIONAL_JUMP` [`00bace00`](#insn-00bace00) → [`00bacf08`](#insn-00bacf08)
  - `FALL_THROUGH` [`00bace00`](#insn-00bace00) → [`00bace04`](#insn-00bace04)
- ブロック [`00bace04`](#insn-00bace04) 範囲 `[['00bace04', '00bace13']]`
  - `CONDITIONAL_JUMP` [`00bace10`](#insn-00bace10) → [`00bace6c`](#insn-00bace6c)
  - `FALL_THROUGH` [`00bace10`](#insn-00bace10) → [`00bace14`](#insn-00bace14)
- ブロック [`00bace14`](#insn-00bace14) 範囲 `[['00bace14', '00bace1b']]`
  - `CONDITIONAL_JUMP` [`00bace18`](#insn-00bace18) → [`00bace74`](#insn-00bace74)
  - `FALL_THROUGH` [`00bace18`](#insn-00bace18) → [`00bace1c`](#insn-00bace1c)
- ブロック [`00bace1c`](#insn-00bace1c) 範囲 `[['00bace1c', '00bace27']]`
  - `CONDITIONAL_JUMP` [`00bace24`](#insn-00bace24) → [`00bace80`](#insn-00bace80)
  - `FALL_THROUGH` [`00bace24`](#insn-00bace24) → [`00bace28`](#insn-00bace28)
- ブロック [`00bace28`](#insn-00bace28) 範囲 `[['00bace28', '00bace2b']]`
  - `UNCONDITIONAL_JUMP` [`00bace28`](#insn-00bace28) → [`00bacf08`](#insn-00bacf08)
- ブロック [`00bace2c`](#insn-00bace2c) 範囲 `[['00bace2c', '00bace33']]`
  - `CONDITIONAL_JUMP` [`00bace30`](#insn-00bace30) → [`00bacf08`](#insn-00bacf08)
  - `FALL_THROUGH` [`00bace30`](#insn-00bace30) → [`00bace34`](#insn-00bace34)
- ブロック [`00bace34`](#insn-00bace34) 範囲 `[['00bace34', '00bace3f']]`
  - `CONDITIONAL_JUMP` [`00bace3c`](#insn-00bace3c) → [`00bacf08`](#insn-00bacf08)
  - `FALL_THROUGH` [`00bace3c`](#insn-00bace3c) → [`00bace40`](#insn-00bace40)
- ブロック [`00bace40`](#insn-00bace40) 範囲 `[['00bace40', '00bace53']]`
  - `CONDITIONAL_JUMP` [`00bace50`](#insn-00bace50) → [`00bacea8`](#insn-00bacea8)
  - `FALL_THROUGH` [`00bace50`](#insn-00bace50) → [`00bace54`](#insn-00bace54)
- ブロック [`00bace54`](#insn-00bace54) 範囲 `[['00bace54', '00bace5b']]`
  - `CONDITIONAL_JUMP` [`00bace58`](#insn-00bace58) → [`00baceb0`](#insn-00baceb0)
  - `FALL_THROUGH` [`00bace58`](#insn-00bace58) → [`00bace5c`](#insn-00bace5c)
- ブロック [`00bace5c`](#insn-00bace5c) 範囲 `[['00bace5c', '00bace67']]`
  - `CONDITIONAL_JUMP` [`00bace64`](#insn-00bace64) → [`00bacebc`](#insn-00bacebc)
  - `FALL_THROUGH` [`00bace64`](#insn-00bace64) → [`00bace68`](#insn-00bace68)
- ブロック [`00bace68`](#insn-00bace68) 範囲 `[['00bace68', '00bace6b']]`
  - `UNCONDITIONAL_JUMP` [`00bace68`](#insn-00bace68) → [`00bacf08`](#insn-00bacf08)
- ブロック [`00bace6c`](#insn-00bace6c) 範囲 `[['00bace6c', '00bace73']]`
  - `UNCONDITIONAL_JUMP` [`00bace70`](#insn-00bace70) → [`00bace78`](#insn-00bace78)
- ブロック [`00bace74`](#insn-00bace74) 範囲 `[['00bace74', '00bace77']]`
  - `FALL_THROUGH` [`00bace74`](#insn-00bace74) → [`00bace78`](#insn-00bace78)
- ブロック [`00bace78`](#insn-00bace78) 範囲 `[['00bace78', '00bace7f']]`
  - `CONDITIONAL_JUMP` [`00bace7c`](#insn-00bace7c) → [`00bacf08`](#insn-00bacf08)
  - `FALL_THROUGH` [`00bace7c`](#insn-00bace7c) → [`00bace80`](#insn-00bace80)
- ブロック [`00bace80`](#insn-00bace80) 範囲 `[['00bace80', '00bace8b']]`
  - `CONDITIONAL_JUMP` [`00bace88`](#insn-00bace88) → [`00bacf08`](#insn-00bacf08)
  - `FALL_THROUGH` [`00bace88`](#insn-00bace88) → [`00bace8c`](#insn-00bace8c)
- ブロック [`00bace8c`](#insn-00bace8c) 範囲 `[['00bace8c', '00bace9b']]`
  - `FALL_THROUGH` [`00bace98`](#insn-00bace98) → [`00bace9c`](#insn-00bace9c)
- ブロック [`00bace9c`](#insn-00bace9c) 範囲 `[['00bace9c', '00bace9f']]`
  - `CONDITIONAL_JUMP` [`00bace9c`](#insn-00bace9c) → [`00bacf08`](#insn-00bacf08)
  - `FALL_THROUGH` [`00bace9c`](#insn-00bace9c) → [`00bacea0`](#insn-00bacea0)
- ブロック [`00bacea0`](#insn-00bacea0) 範囲 `[['00bacea0', '00bacea7']]`
  - `UNCONDITIONAL_JUMP` [`00bacea4`](#insn-00bacea4) → [`00bacef0`](#insn-00bacef0)
- ブロック [`00bacea8`](#insn-00bacea8) 範囲 `[['00bacea8', '00baceaf']]`
  - `UNCONDITIONAL_JUMP` [`00baceac`](#insn-00baceac) → [`00baceb4`](#insn-00baceb4)
- ブロック [`00baceb0`](#insn-00baceb0) 範囲 `[['00baceb0', '00baceb3']]`
  - `FALL_THROUGH` [`00baceb0`](#insn-00baceb0) → [`00baceb4`](#insn-00baceb4)
- ブロック [`00baceb4`](#insn-00baceb4) 範囲 `[['00baceb4', '00bacebb']]`
  - `CONDITIONAL_JUMP` [`00baceb8`](#insn-00baceb8) → [`00bacf08`](#insn-00bacf08)
  - `FALL_THROUGH` [`00baceb8`](#insn-00baceb8) → [`00bacebc`](#insn-00bacebc)
- ブロック [`00bacebc`](#insn-00bacebc) 範囲 `[['00bacebc', '00bacec7']]`
  - `CONDITIONAL_JUMP` [`00bacec4`](#insn-00bacec4) → [`00bacf08`](#insn-00bacf08)
  - `FALL_THROUGH` [`00bacec4`](#insn-00bacec4) → [`00bacec8`](#insn-00bacec8)
- ブロック [`00bacec8`](#insn-00bacec8) 範囲 `[['00bacec8', '00bacecf']]`
  - `FALL_THROUGH` [`00bacecc`](#insn-00bacecc) → [`00baced0`](#insn-00baced0)
- ブロック [`00baced0`](#insn-00baced0) 範囲 `[['00baced0', '00baced3']]`
  - `CONDITIONAL_JUMP` [`00baced0`](#insn-00baced0) → [`00bacf08`](#insn-00bacf08)
  - `FALL_THROUGH` [`00baced0`](#insn-00baced0) → [`00baced4`](#insn-00baced4)
- ブロック [`00baced4`](#insn-00baced4) 範囲 `[['00baced4', '00baceeb']]`
  - `CONDITIONAL_JUMP` [`00bacee8`](#insn-00bacee8) → [`00bacf08`](#insn-00bacf08)
  - `FALL_THROUGH` [`00bacee8`](#insn-00bacee8) → [`00baceec`](#insn-00baceec)
- ブロック [`00baceec`](#insn-00baceec) 範囲 `[['00baceec', '00baceef']]`
  - `FALL_THROUGH` [`00baceec`](#insn-00baceec) → [`00bacef0`](#insn-00bacef0)
- ブロック [`00bacef0`](#insn-00bacef0) 範囲 `[['00bacef0', '00bacef3']]`
  - `FALL_THROUGH` [`00bacef0`](#insn-00bacef0) → [`00bacef4`](#insn-00bacef4)
- ブロック [`00bacef4`](#insn-00bacef4) 範囲 `[['00bacef4', '00bacefb']]`
  - `CONDITIONAL_JUMP` [`00bacef8`](#insn-00bacef8) → [`00bacf08`](#insn-00bacf08)
  - `FALL_THROUGH` [`00bacef8`](#insn-00bacef8) → [`00bacefc`](#insn-00bacefc)
- ブロック [`00bacefc`](#insn-00bacefc) 範囲 `[['00bacefc', '00bacf07']]`
  - `CONDITIONAL_JUMP` [`00bacf04`](#insn-00bacf04) → [`00bacd8c`](#insn-00bacd8c)
  - `FALL_THROUGH` [`00bacf04`](#insn-00bacf04) → [`00bacf08`](#insn-00bacf08)
- ブロック [`00bacf08`](#insn-00bacf08) 範囲 `[['00bacf08', '00bacf0f']]`

## 命令位置別の参照

- [`00bacd3c`](#insn-00bacd3c) → [`00bacd7c`](#insn-00bacd7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd44`](#insn-00bacd44) → [`00bacd7c`](#insn-00bacd7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd54`](#insn-00bacd54) → [`00bacd7c`](#insn-00bacd7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd64`](#insn-00bacd64) → [`00bacd7c`](#insn-00bacd7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd80`](#insn-00bacd80) → [`00bacf08`](#insn-00bacf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd84`](#insn-00bacd84) → [`00bacf08`](#insn-00bacf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd90`](#insn-00bacd90) → [`00bacda8`](#insn-00bacda8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd9c`](#insn-00bacd9c) → [`00bacf08`](#insn-00bacf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacda4`](#insn-00bacda4) → [`00bacef0`](#insn-00bacef0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacdb0`](#insn-00bacdb0) → [`00bacf08`](#insn-00bacf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacdb8`](#insn-00bacdb8) → [`00bacdf0`](#insn-00bacdf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacdc4`](#insn-00bacdc4) → [`00bacf08`](#insn-00bacf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacdd4`](#insn-00bacdd4) → [`00bacf08`](#insn-00bacf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacde4`](#insn-00bacde4) → [`00bacf08`](#insn-00bacf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacdec`](#insn-00bacdec) → [`00bacef0`](#insn-00bacef0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacdf4`](#insn-00bacdf4) → [`00bace2c`](#insn-00bace2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace00`](#insn-00bace00) → [`00bacf08`](#insn-00bacf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace10`](#insn-00bace10) → [`00bace6c`](#insn-00bace6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace18`](#insn-00bace18) → [`00bace74`](#insn-00bace74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace24`](#insn-00bace24) → [`00bace80`](#insn-00bace80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace28`](#insn-00bace28) → [`00bacf08`](#insn-00bacf08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace30`](#insn-00bace30) → [`00bacf08`](#insn-00bacf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace3c`](#insn-00bace3c) → [`00bacf08`](#insn-00bacf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace50`](#insn-00bace50) → [`00bacea8`](#insn-00bacea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace58`](#insn-00bace58) → [`00baceb0`](#insn-00baceb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace64`](#insn-00bace64) → [`00bacebc`](#insn-00bacebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace68`](#insn-00bace68) → [`00bacf08`](#insn-00bacf08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace70`](#insn-00bace70) → [`00bace78`](#insn-00bace78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace7c`](#insn-00bace7c) → [`00bacf08`](#insn-00bacf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace88`](#insn-00bace88) → [`00bacf08`](#insn-00bacf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace9c`](#insn-00bace9c) → [`00bacf08`](#insn-00bacf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacea4`](#insn-00bacea4) → [`00bacef0`](#insn-00bacef0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baceac`](#insn-00baceac) → [`00baceb4`](#insn-00baceb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baceb8`](#insn-00baceb8) → [`00bacf08`](#insn-00bacf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacec4`](#insn-00bacec4) → [`00bacf08`](#insn-00bacf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baced0`](#insn-00baced0) → [`00bacf08`](#insn-00bacf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacee8`](#insn-00bacee8) → [`00bacf08`](#insn-00bacf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacef8`](#insn-00bacef8) → [`00bacf08`](#insn-00bacf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf04`](#insn-00bacf04) → [`00bacd8c`](#insn-00bacd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bacd3c`](#insn-00bacd3c)

~~~json
{
  "source": "00bacd3c",
  "target": "00bacd7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd44`](#insn-00bacd44)

~~~json
{
  "source": "00bacd44",
  "target": "00bacd7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd54`](#insn-00bacd54)

~~~json
{
  "source": "00bacd54",
  "target": "00bacd7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd64`](#insn-00bacd64)

~~~json
{
  "source": "00bacd64",
  "target": "00bacd7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd80`](#insn-00bacd80)

~~~json
{
  "source": "00bacd80",
  "target": "00bacf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd84`](#insn-00bacd84)

~~~json
{
  "source": "00bacd84",
  "target": "00bacf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd90`](#insn-00bacd90)

~~~json
{
  "source": "00bacd90",
  "target": "00bacda8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd9c`](#insn-00bacd9c)

~~~json
{
  "source": "00bacd9c",
  "target": "00bacf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacda4`](#insn-00bacda4)

~~~json
{
  "source": "00bacda4",
  "target": "00bacef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacdb0`](#insn-00bacdb0)

~~~json
{
  "source": "00bacdb0",
  "target": "00bacf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacdb8`](#insn-00bacdb8)

~~~json
{
  "source": "00bacdb8",
  "target": "00bacdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacdc4`](#insn-00bacdc4)

~~~json
{
  "source": "00bacdc4",
  "target": "00bacf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacdd4`](#insn-00bacdd4)

~~~json
{
  "source": "00bacdd4",
  "target": "00bacf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacde4`](#insn-00bacde4)

~~~json
{
  "source": "00bacde4",
  "target": "00bacf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacdec`](#insn-00bacdec)

~~~json
{
  "source": "00bacdec",
  "target": "00bacef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacdf4`](#insn-00bacdf4)

~~~json
{
  "source": "00bacdf4",
  "target": "00bace2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace00`](#insn-00bace00)

~~~json
{
  "source": "00bace00",
  "target": "00bacf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace10`](#insn-00bace10)

~~~json
{
  "source": "00bace10",
  "target": "00bace6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace18`](#insn-00bace18)

~~~json
{
  "source": "00bace18",
  "target": "00bace74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace24`](#insn-00bace24)

~~~json
{
  "source": "00bace24",
  "target": "00bace80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace28`](#insn-00bace28)

~~~json
{
  "source": "00bace28",
  "target": "00bacf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace30`](#insn-00bace30)

~~~json
{
  "source": "00bace30",
  "target": "00bacf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace3c`](#insn-00bace3c)

~~~json
{
  "source": "00bace3c",
  "target": "00bacf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace50`](#insn-00bace50)

~~~json
{
  "source": "00bace50",
  "target": "00bacea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace58`](#insn-00bace58)

~~~json
{
  "source": "00bace58",
  "target": "00baceb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace64`](#insn-00bace64)

~~~json
{
  "source": "00bace64",
  "target": "00bacebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace68`](#insn-00bace68)

~~~json
{
  "source": "00bace68",
  "target": "00bacf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace70`](#insn-00bace70)

~~~json
{
  "source": "00bace70",
  "target": "00bace78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace7c`](#insn-00bace7c)

~~~json
{
  "source": "00bace7c",
  "target": "00bacf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace88`](#insn-00bace88)

~~~json
{
  "source": "00bace88",
  "target": "00bacf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace9c`](#insn-00bace9c)

~~~json
{
  "source": "00bace9c",
  "target": "00bacf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacea4`](#insn-00bacea4)

~~~json
{
  "source": "00bacea4",
  "target": "00bacef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baceac`](#insn-00baceac)

~~~json
{
  "source": "00baceac",
  "target": "00baceb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baceb8`](#insn-00baceb8)

~~~json
{
  "source": "00baceb8",
  "target": "00bacf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacec4`](#insn-00bacec4)

~~~json
{
  "source": "00bacec4",
  "target": "00bacf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baced0`](#insn-00baced0)

~~~json
{
  "source": "00baced0",
  "target": "00bacf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacee8`](#insn-00bacee8)

~~~json
{
  "source": "00bacee8",
  "target": "00bacf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacef8`](#insn-00bacef8)

~~~json
{
  "source": "00bacef8",
  "target": "00bacf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf04`](#insn-00bacf04)

~~~json
{
  "source": "00bacf04",
  "target": "00bacd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
