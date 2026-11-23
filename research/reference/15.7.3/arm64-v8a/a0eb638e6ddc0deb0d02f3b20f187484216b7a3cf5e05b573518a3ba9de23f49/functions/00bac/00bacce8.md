# 00bacce8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bacc20`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bacc20.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0023.md#compare-e84ffddb1860b48dfb0cd6f71d2b6139)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bacd2c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bacd2c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0023.md#compare-ef782359a59c81f650a1cf80c6d95f89)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bacce8",
  "name": "FUN_00bacce8",
  "size": 484,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "00384c0eaf2ff263f49e87a7b7e91a7610b3ba9e6988300c75e1faa53a7755e0",
  "source_text_sha256": "00384c0eaf2ff263f49e87a7b7e91a7610b3ba9e6988300c75e1faa53a7755e0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bacce8",
        "00bacecb"
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

- [00bacccc](../00bac/00bacccc.md)
- [00bad0bc](../00bad/00bad0bc.md)
- [00bad1ec](../00bad/00bad1ec.md)
- [00bad77c](../00bad/00bad77c.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3197 bytes

~~~c

int FUN_00bacce8(byte *param_1,byte *param_2,ulong param_3,ulong param_4,uint param_5)

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
                    /* try { // try from 00bacd4c to 00cace47 has its CatchHandler @ 00bacd4c
                       catch() { ... } // from try @ 00bacd4c with catch @ 00bacd4c
                       catch() { ... } // from try @ 00baceb0 with catch @ 00bacd4c
                       catch() { ... } // from try @ 00bacf40 with catch @ 00bacd4c */
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
LAB_00bace34:
            if (uVar8 != 0x80) break;
          }
          else {
            if (uVar5 != 0xe0) {
              uVar8 = uVar7 & 0xc0;
              goto LAB_00bace34;
            }
            if ((uVar7 & 0xe0) != 0xa0) break;
          }
                    /* try { // try from 00bace48 to 00cace53 has its CatchHandler @ 00bad030 */
                    /* try { // try from 00bace58 to 00cace6b has its CatchHandler @ 00bad010 */
          if (((pbVar3[2] & 0xc0) != 0x80) ||
             (param_4 < ((uVar5 & 0xf) << 0xc | (uVar7 & 0x3f) << 6 | pbVar3[2] & 0x3f))) break;
          lVar6 = 3;
        }
        else {
          if ((0xf4 < bVar1) || ((long)param_2 - (long)pbVar3 < 4)) break;
          uVar7 = (uint)pbVar3[1];
          if (uVar5 == 0xf4) {
            uVar8 = uVar7 & 0xf0;
LAB_00bace70:
            if (uVar8 != 0x80) break;
          }
          else {
            if (uVar5 != 0xf0) {
              uVar8 = uVar7 & 0xc0;
              goto LAB_00bace70;
            }
            if (0x2f < uVar7 - 0x90) break;
          }
                    /* try { // try from 00bace8c to 00caceaf has its CatchHandler @ 00bad040 */
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
                    /* try { // try from 00baceb0 to 00caceef has its CatchHandler @ 00bacd4c */
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
<a id="insn-00bacce8"></a> `00bacce8` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00baccec"></a> `00baccec` | `28 00 00 cb` | sub x8,x1,x0 | `FALL_THROUGH`
<a id="insn-00baccf0"></a> `00baccf0` | `1f 0d 00 f1` | cmp x8,#0x3 | `FALL_THROUGH`
<a id="insn-00baccf4"></a> `00baccf4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00baccf8"></a> `00baccf8` | `0b 02 00 54` | b.lt 0x00bacd38 | `CONDITIONAL_JUMP`
<a id="insn-00baccfc"></a> `00baccfc` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bacd00"></a> `00bacd00` | `c4 01 10 36` | tbz w4,#0x2,0x00bacd38 | `CONDITIONAL_JUMP`
<a id="insn-00bacd04"></a> `00bacd04` | `08 00 40 39` | ldrb w8,[x0] | `FALL_THROUGH`
<a id="insn-00bacd08"></a> `00bacd08` | `1f bd 03 71` | cmp w8,#0xef | `FALL_THROUGH`
<a id="insn-00bacd0c"></a> `00bacd0c` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bacd10"></a> `00bacd10` | `41 01 00 54` | b.ne 0x00bacd38 | `CONDITIONAL_JUMP`
<a id="insn-00bacd14"></a> `00bacd14` | `08 04 40 39` | ldrb w8,[x0, #0x1] | `FALL_THROUGH`
<a id="insn-00bacd18"></a> `00bacd18` | `1f ed 02 71` | cmp w8,#0xbb | `FALL_THROUGH`
<a id="insn-00bacd1c"></a> `00bacd1c` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bacd20"></a> `00bacd20` | `c1 00 00 54` | b.ne 0x00bacd38 | `CONDITIONAL_JUMP`
<a id="insn-00bacd24"></a> `00bacd24` | `08 08 40 39` | ldrb w8,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00bacd28"></a> `00bacd28` | `1f fd 02 71` | cmp w8,#0xbf | `FALL_THROUGH`
<a id="insn-00bacd2c"></a> `00bacd2c` | `68 00 80 52` | mov w8,#0x3 | `FALL_THROUGH`
<a id="insn-00bacd30"></a> `00bacd30` | `08 01 9f 9a` | csel x8,x8,xzr,eq | `FALL_THROUGH`
<a id="insn-00bacd34"></a> `00bacd34` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bacd38"></a> `00bacd38` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00bacd3c"></a> `00bacd3c` | `42 0c 00 54` | b.cs 0x00bacec4 | `CONDITIONAL_JUMP`
<a id="insn-00bacd40"></a> `00bacd40` | `22 0c 00 b4` | cbz x2,0x00bacec4 | `CONDITIONAL_JUMP`
<a id="insn-00bacd44"></a> `00bacd44` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacd48"></a> `00bacd48` | `0a 01 c0 39` | ldrsb w10,[x8] | `FALL_THROUGH`
<a id="insn-00bacd4c"></a> `00bacd4c` | `ca 00 f8 37` | tbnz w10,#0x1f,0x00bacd64 | `CONDITIONAL_JUMP`
<a id="insn-00bacd50"></a> `00bacd50` | `4a 1d 40 92` | and x10,x10,#0xff | `FALL_THROUGH`
<a id="insn-00bacd54"></a> `00bacd54` | `5f 01 03 eb` | cmp x10,x3 | `FALL_THROUGH`
<a id="insn-00bacd58"></a> `00bacd58` | `68 0b 00 54` | b.hi 0x00bacec4 | `CONDITIONAL_JUMP`
<a id="insn-00bacd5c"></a> `00bacd5c` | `2a 00 80 52` | mov w10,#0x1 | `FALL_THROUGH`
<a id="insn-00bacd60"></a> `00bacd60` | `53 00 00 14` | b 0x00baceac | `UNCONDITIONAL_JUMP`
<a id="insn-00bacd64"></a> `00bacd64` | `4a 1d 00 12` | and w10,w10,#0xff | `FALL_THROUGH`
<a id="insn-00bacd68"></a> `00bacd68` | `5f 09 03 71` | cmp w10,#0xc2 | `FALL_THROUGH`
<a id="insn-00bacd6c"></a> `00bacd6c` | `c3 0a 00 54` | b.cc 0x00bacec4 | `CONDITIONAL_JUMP`
<a id="insn-00bacd70"></a> `00bacd70` | `5f 7d 03 71` | cmp w10,#0xdf | `FALL_THROUGH`
<a id="insn-00bacd74"></a> `00bacd74` | `c8 01 00 54` | b.hi 0x00bacdac | `CONDITIONAL_JUMP`
<a id="insn-00bacd78"></a> `00bacd78` | `2b 00 08 cb` | sub x11,x1,x8 | `FALL_THROUGH`
<a id="insn-00bacd7c"></a> `00bacd7c` | `7f 09 00 f1` | cmp x11,#0x2 | `FALL_THROUGH`
<a id="insn-00bacd80"></a> `00bacd80` | `2b 0a 00 54` | b.lt 0x00bacec4 | `CONDITIONAL_JUMP`
<a id="insn-00bacd84"></a> `00bacd84` | `0b 05 40 39` | ldrb w11,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bacd88"></a> `00bacd88` | `6c 05 1a 12` | and w12,w11,#0xc0 | `FALL_THROUGH`
<a id="insn-00bacd8c"></a> `00bacd8c` | `9f 01 02 71` | cmp w12,#0x80 | `FALL_THROUGH`
<a id="insn-00bacd90"></a> `00bacd90` | `a1 09 00 54` | b.ne 0x00bacec4 | `CONDITIONAL_JUMP`
<a id="insn-00bacd94"></a> `00bacd94` | `6b 15 00 12` | and w11,w11,#0x3f | `FALL_THROUGH`
<a id="insn-00bacd98"></a> `00bacd98` | `4b 11 1a 33` | bfm w11,w10,#0x1a,#0x4 | `FALL_THROUGH`
<a id="insn-00bacd9c"></a> `00bacd9c` | `7f 01 03 eb` | cmp x11,x3 | `FALL_THROUGH`
<a id="insn-00bacda0"></a> `00bacda0` | `28 09 00 54` | b.hi 0x00bacec4 | `CONDITIONAL_JUMP`
<a id="insn-00bacda4"></a> `00bacda4` | `4a 00 80 52` | mov w10,#0x2 | `FALL_THROUGH`
<a id="insn-00bacda8"></a> `00bacda8` | `41 00 00 14` | b 0x00baceac | `UNCONDITIONAL_JUMP`
<a id="insn-00bacdac"></a> `00bacdac` | `5f bd 03 71` | cmp w10,#0xef | `FALL_THROUGH`
<a id="insn-00bacdb0"></a> `00bacdb0` | `c8 01 00 54` | b.hi 0x00bacde8 | `CONDITIONAL_JUMP`
<a id="insn-00bacdb4"></a> `00bacdb4` | `2b 00 08 cb` | sub x11,x1,x8 | `FALL_THROUGH`
<a id="insn-00bacdb8"></a> `00bacdb8` | `7f 0d 00 f1` | cmp x11,#0x3 | `FALL_THROUGH`
<a id="insn-00bacdbc"></a> `00bacdbc` | `4b 08 00 54` | b.lt 0x00bacec4 | `CONDITIONAL_JUMP`
<a id="insn-00bacdc0"></a> `00bacdc0` | `0c 05 40 39` | ldrb w12,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bacdc4"></a> `00bacdc4` | `0b 09 40 39` | ldrb w11,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00bacdc8"></a> `00bacdc8` | `5f b5 03 71` | cmp w10,#0xed | `FALL_THROUGH`
<a id="insn-00bacdcc"></a> `00bacdcc` | `e0 02 00 54` | b.eq 0x00bace28 | `CONDITIONAL_JUMP`
<a id="insn-00bacdd0"></a> `00bacdd0` | `5f 81 03 71` | cmp w10,#0xe0 | `FALL_THROUGH`
<a id="insn-00bacdd4"></a> `00bacdd4` | `e1 02 00 54` | b.ne 0x00bace30 | `CONDITIONAL_JUMP`
<a id="insn-00bacdd8"></a> `00bacdd8` | `8d 09 1b 12` | and w13,w12,#0xe0 | `FALL_THROUGH`
<a id="insn-00bacddc"></a> `00bacddc` | `bf 81 02 71` | cmp w13,#0xa0 | `FALL_THROUGH`
<a id="insn-00bacde0"></a> `00bacde0` | `e0 02 00 54` | b.eq 0x00bace3c | `CONDITIONAL_JUMP`
<a id="insn-00bacde4"></a> `00bacde4` | `38 00 00 14` | b 0x00bacec4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacde8"></a> `00bacde8` | `5f d1 03 71` | cmp w10,#0xf4 | `FALL_THROUGH`
<a id="insn-00bacdec"></a> `00bacdec` | `c8 06 00 54` | b.hi 0x00bacec4 | `CONDITIONAL_JUMP`
<a id="insn-00bacdf0"></a> `00bacdf0` | `2b 00 08 cb` | sub x11,x1,x8 | `FALL_THROUGH`
<a id="insn-00bacdf4"></a> `00bacdf4` | `7f 11 00 f1` | cmp x11,#0x4 | `FALL_THROUGH`
<a id="insn-00bacdf8"></a> `00bacdf8` | `6b 06 00 54` | b.lt 0x00bacec4 | `CONDITIONAL_JUMP`
<a id="insn-00bacdfc"></a> `00bacdfc` | `0c 05 40 39` | ldrb w12,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bace00"></a> `00bace00` | `0b 09 40 39` | ldrb w11,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00bace04"></a> `00bace04` | `5f d1 03 71` | cmp w10,#0xf4 | `FALL_THROUGH`
<a id="insn-00bace08"></a> `00bace08` | `0d 0d 40 39` | ldrb w13,[x8, #0x3] | `FALL_THROUGH`
<a id="insn-00bace0c"></a> `00bace0c` | `c0 02 00 54` | b.eq 0x00bace64 | `CONDITIONAL_JUMP`
<a id="insn-00bace10"></a> `00bace10` | `5f c1 03 71` | cmp w10,#0xf0 | `FALL_THROUGH`
<a id="insn-00bace14"></a> `00bace14` | `c1 02 00 54` | b.ne 0x00bace6c | `CONDITIONAL_JUMP`
<a id="insn-00bace18"></a> `00bace18` | `8e 41 02 51` | sub w14,w12,#0x90 | `FALL_THROUGH`
<a id="insn-00bace1c"></a> `00bace1c` | `df c1 00 71` | cmp w14,#0x30 | `FALL_THROUGH`
<a id="insn-00bace20"></a> `00bace20` | `c3 02 00 54` | b.cc 0x00bace78 | `CONDITIONAL_JUMP`
<a id="insn-00bace24"></a> `00bace24` | `28 00 00 14` | b 0x00bacec4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bace28"></a> `00bace28` | `8d 09 1b 12` | and w13,w12,#0xe0 | `FALL_THROUGH`
<a id="insn-00bace2c"></a> `00bace2c` | `02 00 00 14` | b 0x00bace34 | `UNCONDITIONAL_JUMP`
<a id="insn-00bace30"></a> `00bace30` | `8d 05 1a 12` | and w13,w12,#0xc0 | `FALL_THROUGH`
<a id="insn-00bace34"></a> `00bace34` | `bf 01 02 71` | cmp w13,#0x80 | `FALL_THROUGH`
<a id="insn-00bace38"></a> `00bace38` | `61 04 00 54` | b.ne 0x00bacec4 | `CONDITIONAL_JUMP`
<a id="insn-00bace3c"></a> `00bace3c` | `6d 05 1a 12` | and w13,w11,#0xc0 | `FALL_THROUGH`
<a id="insn-00bace40"></a> `00bace40` | `bf 01 02 71` | cmp w13,#0x80 | `FALL_THROUGH`
<a id="insn-00bace44"></a> `00bace44` | `01 04 00 54` | b.ne 0x00bacec4 | `CONDITIONAL_JUMP`
<a id="insn-00bace48"></a> `00bace48` | `4a 0d 14 53` | ubfiz w10,w10,#0xc,#0x4 | `FALL_THROUGH`
<a id="insn-00bace4c"></a> `00bace4c` | `8a 15 1a 33` | bfm w10,w12,#0x1a,#0x5 | `FALL_THROUGH`
<a id="insn-00bace50"></a> `00bace50` | `6a 15 00 33` | bfxil w10,w11,#0x0,#0x6 | `FALL_THROUGH`
<a id="insn-00bace54"></a> `00bace54` | `5f 01 03 eb` | cmp x10,x3 | `FALL_THROUGH`
<a id="insn-00bace58"></a> `00bace58` | `68 03 00 54` | b.hi 0x00bacec4 | `CONDITIONAL_JUMP`
<a id="insn-00bace5c"></a> `00bace5c` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00bace60"></a> `00bace60` | `13 00 00 14` | b 0x00baceac | `UNCONDITIONAL_JUMP`
<a id="insn-00bace64"></a> `00bace64` | `8e 0d 1c 12` | and w14,w12,#0xf0 | `FALL_THROUGH`
<a id="insn-00bace68"></a> `00bace68` | `02 00 00 14` | b 0x00bace70 | `UNCONDITIONAL_JUMP`
<a id="insn-00bace6c"></a> `00bace6c` | `8e 05 1a 12` | and w14,w12,#0xc0 | `FALL_THROUGH`
<a id="insn-00bace70"></a> `00bace70` | `df 01 02 71` | cmp w14,#0x80 | `FALL_THROUGH`
<a id="insn-00bace74"></a> `00bace74` | `81 02 00 54` | b.ne 0x00bacec4 | `CONDITIONAL_JUMP`
<a id="insn-00bace78"></a> `00bace78` | `6e 05 1a 12` | and w14,w11,#0xc0 | `FALL_THROUGH`
<a id="insn-00bace7c"></a> `00bace7c` | `df 01 02 71` | cmp w14,#0x80 | `FALL_THROUGH`
<a id="insn-00bace80"></a> `00bace80` | `21 02 00 54` | b.ne 0x00bacec4 | `CONDITIONAL_JUMP`
<a id="insn-00bace84"></a> `00bace84` | `ae 05 1a 12` | and w14,w13,#0xc0 | `FALL_THROUGH`
<a id="insn-00bace88"></a> `00bace88` | `df 01 02 71` | cmp w14,#0x80 | `FALL_THROUGH`
<a id="insn-00bace8c"></a> `00bace8c` | `c1 01 00 54` | b.ne 0x00bacec4 | `CONDITIONAL_JUMP`
<a id="insn-00bace90"></a> `00bace90` | `4a 09 0e 53` | ubfiz w10,w10,#0x12,#0x3 | `FALL_THROUGH`
<a id="insn-00bace94"></a> `00bace94` | `8a 15 14 33` | bfm w10,w12,#0x14,#0x5 | `FALL_THROUGH`
<a id="insn-00bace98"></a> `00bace98` | `6a 15 1a 33` | bfm w10,w11,#0x1a,#0x5 | `FALL_THROUGH`
<a id="insn-00bace9c"></a> `00bace9c` | `aa 15 00 33` | bfxil w10,w13,#0x0,#0x6 | `FALL_THROUGH`
<a id="insn-00bacea0"></a> `00bacea0` | `5f 01 03 eb` | cmp x10,x3 | `FALL_THROUGH`
<a id="insn-00bacea4"></a> `00bacea4` | `08 01 00 54` | b.hi 0x00bacec4 | `CONDITIONAL_JUMP`
<a id="insn-00bacea8"></a> `00bacea8` | `8a 00 80 52` | mov w10,#0x4 | `FALL_THROUGH`
<a id="insn-00baceac"></a> `00baceac` | `08 01 0a 8b` | add x8,x8,x10 | `FALL_THROUGH`
<a id="insn-00baceb0"></a> `00baceb0` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00baceb4"></a> `00baceb4` | `82 00 00 54` | b.cs 0x00bacec4 | `CONDITIONAL_JUMP`
<a id="insn-00baceb8"></a> `00baceb8` | `3f 01 02 eb` | cmp x9,x2 | `FALL_THROUGH`
<a id="insn-00bacebc"></a> `00bacebc` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacec0"></a> `00bacec0` | `43 f4 ff 54` | b.cc 0x00bacd48 | `CONDITIONAL_JUMP`
<a id="insn-00bacec4"></a> `00bacec4` | `00 01 00 4b` | sub w0,w8,w0 | `FALL_THROUGH`
<a id="insn-00bacec8"></a> `00bacec8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bacce8`](#insn-00bacce8) 範囲 `[['00bacce8', '00baccfb']]`
  - `CONDITIONAL_JUMP` [`00baccf8`](#insn-00baccf8) → [`00bacd38`](#insn-00bacd38)
  - `FALL_THROUGH` [`00baccf8`](#insn-00baccf8) → [`00baccfc`](#insn-00baccfc)
- ブロック [`00baccfc`](#insn-00baccfc) 範囲 `[['00baccfc', '00bacd03']]`
  - `CONDITIONAL_JUMP` [`00bacd00`](#insn-00bacd00) → [`00bacd38`](#insn-00bacd38)
  - `FALL_THROUGH` [`00bacd00`](#insn-00bacd00) → [`00bacd04`](#insn-00bacd04)
- ブロック [`00bacd04`](#insn-00bacd04) 範囲 `[['00bacd04', '00bacd13']]`
  - `CONDITIONAL_JUMP` [`00bacd10`](#insn-00bacd10) → [`00bacd38`](#insn-00bacd38)
  - `FALL_THROUGH` [`00bacd10`](#insn-00bacd10) → [`00bacd14`](#insn-00bacd14)
- ブロック [`00bacd14`](#insn-00bacd14) 範囲 `[['00bacd14', '00bacd23']]`
  - `CONDITIONAL_JUMP` [`00bacd20`](#insn-00bacd20) → [`00bacd38`](#insn-00bacd38)
  - `FALL_THROUGH` [`00bacd20`](#insn-00bacd20) → [`00bacd24`](#insn-00bacd24)
- ブロック [`00bacd24`](#insn-00bacd24) 範囲 `[['00bacd24', '00bacd37']]`
  - `FALL_THROUGH` [`00bacd34`](#insn-00bacd34) → [`00bacd38`](#insn-00bacd38)
- ブロック [`00bacd38`](#insn-00bacd38) 範囲 `[['00bacd38', '00bacd3f']]`
  - `CONDITIONAL_JUMP` [`00bacd3c`](#insn-00bacd3c) → [`00bacec4`](#insn-00bacec4)
  - `FALL_THROUGH` [`00bacd3c`](#insn-00bacd3c) → [`00bacd40`](#insn-00bacd40)
- ブロック [`00bacd40`](#insn-00bacd40) 範囲 `[['00bacd40', '00bacd43']]`
  - `CONDITIONAL_JUMP` [`00bacd40`](#insn-00bacd40) → [`00bacec4`](#insn-00bacec4)
  - `FALL_THROUGH` [`00bacd40`](#insn-00bacd40) → [`00bacd44`](#insn-00bacd44)
- ブロック [`00bacd44`](#insn-00bacd44) 範囲 `[['00bacd44', '00bacd47']]`
  - `FALL_THROUGH` [`00bacd44`](#insn-00bacd44) → [`00bacd48`](#insn-00bacd48)
- ブロック [`00bacd48`](#insn-00bacd48) 範囲 `[['00bacd48', '00bacd4b']]`
  - `FALL_THROUGH` [`00bacd48`](#insn-00bacd48) → [`00bacd4c`](#insn-00bacd4c)
- ブロック [`00bacd4c`](#insn-00bacd4c) 範囲 `[['00bacd4c', '00bacd4f']]`
  - `CONDITIONAL_JUMP` [`00bacd4c`](#insn-00bacd4c) → [`00bacd64`](#insn-00bacd64)
  - `FALL_THROUGH` [`00bacd4c`](#insn-00bacd4c) → [`00bacd50`](#insn-00bacd50)
- ブロック [`00bacd50`](#insn-00bacd50) 範囲 `[['00bacd50', '00bacd5b']]`
  - `CONDITIONAL_JUMP` [`00bacd58`](#insn-00bacd58) → [`00bacec4`](#insn-00bacec4)
  - `FALL_THROUGH` [`00bacd58`](#insn-00bacd58) → [`00bacd5c`](#insn-00bacd5c)
- ブロック [`00bacd5c`](#insn-00bacd5c) 範囲 `[['00bacd5c', '00bacd63']]`
  - `UNCONDITIONAL_JUMP` [`00bacd60`](#insn-00bacd60) → [`00baceac`](#insn-00baceac)
- ブロック [`00bacd64`](#insn-00bacd64) 範囲 `[['00bacd64', '00bacd6f']]`
  - `CONDITIONAL_JUMP` [`00bacd6c`](#insn-00bacd6c) → [`00bacec4`](#insn-00bacec4)
  - `FALL_THROUGH` [`00bacd6c`](#insn-00bacd6c) → [`00bacd70`](#insn-00bacd70)
- ブロック [`00bacd70`](#insn-00bacd70) 範囲 `[['00bacd70', '00bacd77']]`
  - `CONDITIONAL_JUMP` [`00bacd74`](#insn-00bacd74) → [`00bacdac`](#insn-00bacdac)
  - `FALL_THROUGH` [`00bacd74`](#insn-00bacd74) → [`00bacd78`](#insn-00bacd78)
- ブロック [`00bacd78`](#insn-00bacd78) 範囲 `[['00bacd78', '00bacd83']]`
  - `CONDITIONAL_JUMP` [`00bacd80`](#insn-00bacd80) → [`00bacec4`](#insn-00bacec4)
  - `FALL_THROUGH` [`00bacd80`](#insn-00bacd80) → [`00bacd84`](#insn-00bacd84)
- ブロック [`00bacd84`](#insn-00bacd84) 範囲 `[['00bacd84', '00bacd93']]`
  - `CONDITIONAL_JUMP` [`00bacd90`](#insn-00bacd90) → [`00bacec4`](#insn-00bacec4)
  - `FALL_THROUGH` [`00bacd90`](#insn-00bacd90) → [`00bacd94`](#insn-00bacd94)
- ブロック [`00bacd94`](#insn-00bacd94) 範囲 `[['00bacd94', '00bacda3']]`
  - `CONDITIONAL_JUMP` [`00bacda0`](#insn-00bacda0) → [`00bacec4`](#insn-00bacec4)
  - `FALL_THROUGH` [`00bacda0`](#insn-00bacda0) → [`00bacda4`](#insn-00bacda4)
- ブロック [`00bacda4`](#insn-00bacda4) 範囲 `[['00bacda4', '00bacdab']]`
  - `UNCONDITIONAL_JUMP` [`00bacda8`](#insn-00bacda8) → [`00baceac`](#insn-00baceac)
- ブロック [`00bacdac`](#insn-00bacdac) 範囲 `[['00bacdac', '00bacdb3']]`
  - `CONDITIONAL_JUMP` [`00bacdb0`](#insn-00bacdb0) → [`00bacde8`](#insn-00bacde8)
  - `FALL_THROUGH` [`00bacdb0`](#insn-00bacdb0) → [`00bacdb4`](#insn-00bacdb4)
- ブロック [`00bacdb4`](#insn-00bacdb4) 範囲 `[['00bacdb4', '00bacdbf']]`
  - `CONDITIONAL_JUMP` [`00bacdbc`](#insn-00bacdbc) → [`00bacec4`](#insn-00bacec4)
  - `FALL_THROUGH` [`00bacdbc`](#insn-00bacdbc) → [`00bacdc0`](#insn-00bacdc0)
- ブロック [`00bacdc0`](#insn-00bacdc0) 範囲 `[['00bacdc0', '00bacdcf']]`
  - `CONDITIONAL_JUMP` [`00bacdcc`](#insn-00bacdcc) → [`00bace28`](#insn-00bace28)
  - `FALL_THROUGH` [`00bacdcc`](#insn-00bacdcc) → [`00bacdd0`](#insn-00bacdd0)
- ブロック [`00bacdd0`](#insn-00bacdd0) 範囲 `[['00bacdd0', '00bacdd7']]`
  - `CONDITIONAL_JUMP` [`00bacdd4`](#insn-00bacdd4) → [`00bace30`](#insn-00bace30)
  - `FALL_THROUGH` [`00bacdd4`](#insn-00bacdd4) → [`00bacdd8`](#insn-00bacdd8)
- ブロック [`00bacdd8`](#insn-00bacdd8) 範囲 `[['00bacdd8', '00bacde3']]`
  - `CONDITIONAL_JUMP` [`00bacde0`](#insn-00bacde0) → [`00bace3c`](#insn-00bace3c)
  - `FALL_THROUGH` [`00bacde0`](#insn-00bacde0) → [`00bacde4`](#insn-00bacde4)
- ブロック [`00bacde4`](#insn-00bacde4) 範囲 `[['00bacde4', '00bacde7']]`
  - `UNCONDITIONAL_JUMP` [`00bacde4`](#insn-00bacde4) → [`00bacec4`](#insn-00bacec4)
- ブロック [`00bacde8`](#insn-00bacde8) 範囲 `[['00bacde8', '00bacdef']]`
  - `CONDITIONAL_JUMP` [`00bacdec`](#insn-00bacdec) → [`00bacec4`](#insn-00bacec4)
  - `FALL_THROUGH` [`00bacdec`](#insn-00bacdec) → [`00bacdf0`](#insn-00bacdf0)
- ブロック [`00bacdf0`](#insn-00bacdf0) 範囲 `[['00bacdf0', '00bacdfb']]`
  - `CONDITIONAL_JUMP` [`00bacdf8`](#insn-00bacdf8) → [`00bacec4`](#insn-00bacec4)
  - `FALL_THROUGH` [`00bacdf8`](#insn-00bacdf8) → [`00bacdfc`](#insn-00bacdfc)
- ブロック [`00bacdfc`](#insn-00bacdfc) 範囲 `[['00bacdfc', '00bace0f']]`
  - `CONDITIONAL_JUMP` [`00bace0c`](#insn-00bace0c) → [`00bace64`](#insn-00bace64)
  - `FALL_THROUGH` [`00bace0c`](#insn-00bace0c) → [`00bace10`](#insn-00bace10)
- ブロック [`00bace10`](#insn-00bace10) 範囲 `[['00bace10', '00bace17']]`
  - `CONDITIONAL_JUMP` [`00bace14`](#insn-00bace14) → [`00bace6c`](#insn-00bace6c)
  - `FALL_THROUGH` [`00bace14`](#insn-00bace14) → [`00bace18`](#insn-00bace18)
- ブロック [`00bace18`](#insn-00bace18) 範囲 `[['00bace18', '00bace23']]`
  - `CONDITIONAL_JUMP` [`00bace20`](#insn-00bace20) → [`00bace78`](#insn-00bace78)
  - `FALL_THROUGH` [`00bace20`](#insn-00bace20) → [`00bace24`](#insn-00bace24)
- ブロック [`00bace24`](#insn-00bace24) 範囲 `[['00bace24', '00bace27']]`
  - `UNCONDITIONAL_JUMP` [`00bace24`](#insn-00bace24) → [`00bacec4`](#insn-00bacec4)
- ブロック [`00bace28`](#insn-00bace28) 範囲 `[['00bace28', '00bace2f']]`
  - `UNCONDITIONAL_JUMP` [`00bace2c`](#insn-00bace2c) → [`00bace34`](#insn-00bace34)
- ブロック [`00bace30`](#insn-00bace30) 範囲 `[['00bace30', '00bace33']]`
  - `FALL_THROUGH` [`00bace30`](#insn-00bace30) → [`00bace34`](#insn-00bace34)
- ブロック [`00bace34`](#insn-00bace34) 範囲 `[['00bace34', '00bace3b']]`
  - `CONDITIONAL_JUMP` [`00bace38`](#insn-00bace38) → [`00bacec4`](#insn-00bacec4)
  - `FALL_THROUGH` [`00bace38`](#insn-00bace38) → [`00bace3c`](#insn-00bace3c)
- ブロック [`00bace3c`](#insn-00bace3c) 範囲 `[['00bace3c', '00bace47']]`
  - `CONDITIONAL_JUMP` [`00bace44`](#insn-00bace44) → [`00bacec4`](#insn-00bacec4)
  - `FALL_THROUGH` [`00bace44`](#insn-00bace44) → [`00bace48`](#insn-00bace48)
- ブロック [`00bace48`](#insn-00bace48) 範囲 `[['00bace48', '00bace57']]`
  - `FALL_THROUGH` [`00bace54`](#insn-00bace54) → [`00bace58`](#insn-00bace58)
- ブロック [`00bace58`](#insn-00bace58) 範囲 `[['00bace58', '00bace5b']]`
  - `CONDITIONAL_JUMP` [`00bace58`](#insn-00bace58) → [`00bacec4`](#insn-00bacec4)
  - `FALL_THROUGH` [`00bace58`](#insn-00bace58) → [`00bace5c`](#insn-00bace5c)
- ブロック [`00bace5c`](#insn-00bace5c) 範囲 `[['00bace5c', '00bace63']]`
  - `UNCONDITIONAL_JUMP` [`00bace60`](#insn-00bace60) → [`00baceac`](#insn-00baceac)
- ブロック [`00bace64`](#insn-00bace64) 範囲 `[['00bace64', '00bace6b']]`
  - `UNCONDITIONAL_JUMP` [`00bace68`](#insn-00bace68) → [`00bace70`](#insn-00bace70)
- ブロック [`00bace6c`](#insn-00bace6c) 範囲 `[['00bace6c', '00bace6f']]`
  - `FALL_THROUGH` [`00bace6c`](#insn-00bace6c) → [`00bace70`](#insn-00bace70)
- ブロック [`00bace70`](#insn-00bace70) 範囲 `[['00bace70', '00bace77']]`
  - `CONDITIONAL_JUMP` [`00bace74`](#insn-00bace74) → [`00bacec4`](#insn-00bacec4)
  - `FALL_THROUGH` [`00bace74`](#insn-00bace74) → [`00bace78`](#insn-00bace78)
- ブロック [`00bace78`](#insn-00bace78) 範囲 `[['00bace78', '00bace83']]`
  - `CONDITIONAL_JUMP` [`00bace80`](#insn-00bace80) → [`00bacec4`](#insn-00bacec4)
  - `FALL_THROUGH` [`00bace80`](#insn-00bace80) → [`00bace84`](#insn-00bace84)
- ブロック [`00bace84`](#insn-00bace84) 範囲 `[['00bace84', '00bace8b']]`
  - `FALL_THROUGH` [`00bace88`](#insn-00bace88) → [`00bace8c`](#insn-00bace8c)
- ブロック [`00bace8c`](#insn-00bace8c) 範囲 `[['00bace8c', '00bace8f']]`
  - `CONDITIONAL_JUMP` [`00bace8c`](#insn-00bace8c) → [`00bacec4`](#insn-00bacec4)
  - `FALL_THROUGH` [`00bace8c`](#insn-00bace8c) → [`00bace90`](#insn-00bace90)
- ブロック [`00bace90`](#insn-00bace90) 範囲 `[['00bace90', '00bacea7']]`
  - `CONDITIONAL_JUMP` [`00bacea4`](#insn-00bacea4) → [`00bacec4`](#insn-00bacec4)
  - `FALL_THROUGH` [`00bacea4`](#insn-00bacea4) → [`00bacea8`](#insn-00bacea8)
- ブロック [`00bacea8`](#insn-00bacea8) 範囲 `[['00bacea8', '00baceab']]`
  - `FALL_THROUGH` [`00bacea8`](#insn-00bacea8) → [`00baceac`](#insn-00baceac)
- ブロック [`00baceac`](#insn-00baceac) 範囲 `[['00baceac', '00baceaf']]`
  - `FALL_THROUGH` [`00baceac`](#insn-00baceac) → [`00baceb0`](#insn-00baceb0)
- ブロック [`00baceb0`](#insn-00baceb0) 範囲 `[['00baceb0', '00baceb7']]`
  - `CONDITIONAL_JUMP` [`00baceb4`](#insn-00baceb4) → [`00bacec4`](#insn-00bacec4)
  - `FALL_THROUGH` [`00baceb4`](#insn-00baceb4) → [`00baceb8`](#insn-00baceb8)
- ブロック [`00baceb8`](#insn-00baceb8) 範囲 `[['00baceb8', '00bacec3']]`
  - `CONDITIONAL_JUMP` [`00bacec0`](#insn-00bacec0) → [`00bacd48`](#insn-00bacd48)
  - `FALL_THROUGH` [`00bacec0`](#insn-00bacec0) → [`00bacec4`](#insn-00bacec4)
- ブロック [`00bacec4`](#insn-00bacec4) 範囲 `[['00bacec4', '00bacecb']]`

## 命令位置別の参照

- [`00baccf8`](#insn-00baccf8) → [`00bacd38`](#insn-00bacd38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd00`](#insn-00bacd00) → [`00bacd38`](#insn-00bacd38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd10`](#insn-00bacd10) → [`00bacd38`](#insn-00bacd38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd20`](#insn-00bacd20) → [`00bacd38`](#insn-00bacd38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd3c`](#insn-00bacd3c) → [`00bacec4`](#insn-00bacec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd40`](#insn-00bacd40) → [`00bacec4`](#insn-00bacec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd4c`](#insn-00bacd4c) → [`00bacd64`](#insn-00bacd64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd58`](#insn-00bacd58) → [`00bacec4`](#insn-00bacec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd60`](#insn-00bacd60) → [`00baceac`](#insn-00baceac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd6c`](#insn-00bacd6c) → [`00bacec4`](#insn-00bacec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd74`](#insn-00bacd74) → [`00bacdac`](#insn-00bacdac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd80`](#insn-00bacd80) → [`00bacec4`](#insn-00bacec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd90`](#insn-00bacd90) → [`00bacec4`](#insn-00bacec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacda0`](#insn-00bacda0) → [`00bacec4`](#insn-00bacec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacda8`](#insn-00bacda8) → [`00baceac`](#insn-00baceac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacdb0`](#insn-00bacdb0) → [`00bacde8`](#insn-00bacde8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacdbc`](#insn-00bacdbc) → [`00bacec4`](#insn-00bacec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacdcc`](#insn-00bacdcc) → [`00bace28`](#insn-00bace28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacdd4`](#insn-00bacdd4) → [`00bace30`](#insn-00bace30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacde0`](#insn-00bacde0) → [`00bace3c`](#insn-00bace3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacde4`](#insn-00bacde4) → [`00bacec4`](#insn-00bacec4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacdec`](#insn-00bacdec) → [`00bacec4`](#insn-00bacec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacdf8`](#insn-00bacdf8) → [`00bacec4`](#insn-00bacec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace0c`](#insn-00bace0c) → [`00bace64`](#insn-00bace64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace14`](#insn-00bace14) → [`00bace6c`](#insn-00bace6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace20`](#insn-00bace20) → [`00bace78`](#insn-00bace78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace24`](#insn-00bace24) → [`00bacec4`](#insn-00bacec4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace2c`](#insn-00bace2c) → [`00bace34`](#insn-00bace34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace38`](#insn-00bace38) → [`00bacec4`](#insn-00bacec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace44`](#insn-00bace44) → [`00bacec4`](#insn-00bacec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace58`](#insn-00bace58) → [`00bacec4`](#insn-00bacec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace60`](#insn-00bace60) → [`00baceac`](#insn-00baceac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace68`](#insn-00bace68) → [`00bace70`](#insn-00bace70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace74`](#insn-00bace74) → [`00bacec4`](#insn-00bacec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace80`](#insn-00bace80) → [`00bacec4`](#insn-00bacec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace8c`](#insn-00bace8c) → [`00bacec4`](#insn-00bacec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacea4`](#insn-00bacea4) → [`00bacec4`](#insn-00bacec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baceb4`](#insn-00baceb4) → [`00bacec4`](#insn-00bacec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacec0`](#insn-00bacec0) → [`00bacd48`](#insn-00bacd48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baccf8`](#insn-00baccf8)

~~~json
{
  "source": "00baccf8",
  "target": "00bacd38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd00`](#insn-00bacd00)

~~~json
{
  "source": "00bacd00",
  "target": "00bacd38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd10`](#insn-00bacd10)

~~~json
{
  "source": "00bacd10",
  "target": "00bacd38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd20`](#insn-00bacd20)

~~~json
{
  "source": "00bacd20",
  "target": "00bacd38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd3c`](#insn-00bacd3c)

~~~json
{
  "source": "00bacd3c",
  "target": "00bacec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd40`](#insn-00bacd40)

~~~json
{
  "source": "00bacd40",
  "target": "00bacec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd4c`](#insn-00bacd4c)

~~~json
{
  "source": "00bacd4c",
  "target": "00bacd64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd58`](#insn-00bacd58)

~~~json
{
  "source": "00bacd58",
  "target": "00bacec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd60`](#insn-00bacd60)

~~~json
{
  "source": "00bacd60",
  "target": "00baceac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd6c`](#insn-00bacd6c)

~~~json
{
  "source": "00bacd6c",
  "target": "00bacec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd74`](#insn-00bacd74)

~~~json
{
  "source": "00bacd74",
  "target": "00bacdac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd80`](#insn-00bacd80)

~~~json
{
  "source": "00bacd80",
  "target": "00bacec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd90`](#insn-00bacd90)

~~~json
{
  "source": "00bacd90",
  "target": "00bacec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacda0`](#insn-00bacda0)

~~~json
{
  "source": "00bacda0",
  "target": "00bacec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacda8`](#insn-00bacda8)

~~~json
{
  "source": "00bacda8",
  "target": "00baceac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacdb0`](#insn-00bacdb0)

~~~json
{
  "source": "00bacdb0",
  "target": "00bacde8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacdbc`](#insn-00bacdbc)

~~~json
{
  "source": "00bacdbc",
  "target": "00bacec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacdcc`](#insn-00bacdcc)

~~~json
{
  "source": "00bacdcc",
  "target": "00bace28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacdd4`](#insn-00bacdd4)

~~~json
{
  "source": "00bacdd4",
  "target": "00bace30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacde0`](#insn-00bacde0)

~~~json
{
  "source": "00bacde0",
  "target": "00bace3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacde4`](#insn-00bacde4)

~~~json
{
  "source": "00bacde4",
  "target": "00bacec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacdec`](#insn-00bacdec)

~~~json
{
  "source": "00bacdec",
  "target": "00bacec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacdf8`](#insn-00bacdf8)

~~~json
{
  "source": "00bacdf8",
  "target": "00bacec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace0c`](#insn-00bace0c)

~~~json
{
  "source": "00bace0c",
  "target": "00bace64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace14`](#insn-00bace14)

~~~json
{
  "source": "00bace14",
  "target": "00bace6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace20`](#insn-00bace20)

~~~json
{
  "source": "00bace20",
  "target": "00bace78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace24`](#insn-00bace24)

~~~json
{
  "source": "00bace24",
  "target": "00bacec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace2c`](#insn-00bace2c)

~~~json
{
  "source": "00bace2c",
  "target": "00bace34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace38`](#insn-00bace38)

~~~json
{
  "source": "00bace38",
  "target": "00bacec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace44`](#insn-00bace44)

~~~json
{
  "source": "00bace44",
  "target": "00bacec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace58`](#insn-00bace58)

~~~json
{
  "source": "00bace58",
  "target": "00bacec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace60`](#insn-00bace60)

~~~json
{
  "source": "00bace60",
  "target": "00baceac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace68`](#insn-00bace68)

~~~json
{
  "source": "00bace68",
  "target": "00bace70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace74`](#insn-00bace74)

~~~json
{
  "source": "00bace74",
  "target": "00bacec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace80`](#insn-00bace80)

~~~json
{
  "source": "00bace80",
  "target": "00bacec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace8c`](#insn-00bace8c)

~~~json
{
  "source": "00bace8c",
  "target": "00bacec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacea4`](#insn-00bacea4)

~~~json
{
  "source": "00bacea4",
  "target": "00bacec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baceb4`](#insn-00baceb4)

~~~json
{
  "source": "00baceb4",
  "target": "00bacec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacec0`](#insn-00bacec0)

~~~json
{
  "source": "00bacec0",
  "target": "00bacd48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
