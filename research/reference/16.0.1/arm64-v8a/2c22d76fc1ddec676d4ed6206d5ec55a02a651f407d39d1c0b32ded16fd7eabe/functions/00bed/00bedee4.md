# 00bedee4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0005.md#review-d8ec67e04a6ee275ccc155848c3af0f7)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0004.md#review-d8ec67e04a6ee275ccc155848c3af0f7)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bedee4",
  "name": "FUN_00bedee4",
  "size": 764,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "77c445730ef6cd745f4b0c98e722e6f23b74f933477fe05b959fabb3e29dd76f",
  "source_text_sha256": "77c445730ef6cd745f4b0c98e722e6f23b74f933477fe05b959fabb3e29dd76f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bedee4",
        "00bee1df"
      ]
    ],
    "bytes_sha256": "8afdd3b2f6c538bfa452884526a87c1c55c347e8f3ecf14f12a3a8b348358cd4",
    "instruction_count": 191,
    "instruction_bytes": 764,
    "body_bytes": 764,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be7110](../00be7/00be7110.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 7468 bytes

~~~c

ulong * FUN_00bedee4(ulong *param_1,ulong *param_2,ulong *param_3)

{
  ulong *puVar1;
  bool bVar2;
  ulong uVar3;
  ulong *puVar4;
  ulong uVar5;
  long lVar6;
  ulong *puVar7;
  ulong uVar8;
  long lVar9;
  ulong *puVar10;
  ulong *puVar11;
  ulong uVar12;
  ulong uVar13;
  ulong uVar14;
  ulong *puVar15;
  ulong uVar16;
  ulong uVar17;
  
  if (param_1 != param_2) {
    lVar6 = (long)param_2 - (long)param_1 >> 3;
    if (1 < lVar6) {
      uVar8 = lVar6 - 2U >> 1;
      uVar13 = uVar8;
      do {
        if ((long)uVar13 <= (long)uVar8) {
          uVar12 = (uVar13 & 0x1fffffffffffffff) << 1 | 1;
          uVar5 = (uVar13 & 0x1fffffffffffffff) * 2 + 2;
          puVar10 = param_1 + uVar12;
                    /* try { // try from 00bedf3c to 00cedf43 has its CatchHandler @ 00bee74c */
          if ((long)uVar5 < lVar6) {
            uVar16 = *puVar10;
                    /* try { // try from 00bedf48 to 00cedf5f has its CatchHandler @ 00bee744 */
            uVar3 = puVar10[1];
            uVar14 = uVar16;
            if (uVar16 <= uVar3) {
              uVar14 = uVar3;
            }
            puVar11 = puVar10 + 1;
            if (uVar3 <= uVar16) {
              puVar11 = puVar10;
              uVar5 = uVar12;
            }
          }
          else {
            uVar14 = *puVar10;
            puVar11 = puVar10;
            uVar5 = uVar12;
          }
          uVar12 = param_1[uVar13];
                    /* try { // try from 00bedf6c to 00cedf87 has its CatchHandler @ 00bee7b4 */
          puVar10 = param_1 + uVar13;
          if (uVar12 <= uVar14) {
            do {
              while( true ) {
                puVar7 = puVar11;
                *puVar10 = uVar14;
                if ((long)uVar8 < (long)uVar5) goto LAB_00bedf0c;
                uVar3 = uVar5 << 1 | 1;
                uVar5 = uVar5 * 2 + 2;
                puVar4 = param_1 + uVar3;
                puVar10 = puVar7;
                if ((long)uVar5 < lVar6) break;
                uVar14 = *puVar4;
                puVar11 = puVar4;
                uVar5 = uVar3;
                if (uVar14 < uVar12) goto LAB_00bedf0c;
              }
              uVar17 = *puVar4;
              uVar16 = puVar4[1];
                    /* try { // try from 00bedf88 to 00cee03f has its CatchHandler @ 00bedde0 */
              uVar14 = uVar17;
              if (uVar17 <= uVar16) {
                uVar14 = uVar16;
              }
              puVar11 = puVar4 + 1;
              if (uVar16 <= uVar17) {
                uVar5 = uVar3;
                puVar11 = puVar4;
              }
            } while (uVar12 <= uVar14);
LAB_00bedf0c:
            *puVar7 = uVar12;
          }
        }
        bVar2 = 0 < (long)uVar13;
        uVar13 = uVar13 - 1;
      } while (bVar2);
    }
    puVar10 = param_2;
    if (param_2 != param_3) {
      puVar11 = param_1 + 1;
      puVar7 = param_2;
      do {
        uVar13 = *puVar7;
        if (uVar13 < *param_1) {
          *puVar7 = *param_1;
          *param_1 = uVar13;
          if (1 < lVar6) {
            uVar8 = *puVar11;
            if ((long)param_2 - (long)param_1 == 0x10) {
                    /* try { // try from 00bee040 to 00cee063 has its CatchHandler @ 00bee704 */
              uVar5 = 1;
              puVar10 = puVar11;
            }
            else {
              uVar5 = param_1[2];
              bVar2 = uVar5 <= uVar8;
              if (uVar8 <= uVar5) {
                uVar8 = uVar5;
              }
              puVar10 = param_1 + 2;
              if (bVar2) {
                puVar10 = puVar11;
              }
              uVar5 = 1;
              if (!bVar2) {
                uVar5 = 2;
              }
            }
                    /* try { // try from 00bee064 to 00cee0b3 has its CatchHandler @ 00bedde0 */
            puVar4 = param_1;
            if (uVar13 <= uVar8) {
              do {
                while( true ) {
                  puVar15 = puVar10;
                  *puVar4 = uVar8;
                  if ((long)(lVar6 - 2U >> 1) < (long)uVar5) goto LAB_00bee000;
                  uVar12 = uVar5 << 1 | 1;
                    /* try { // try from 00bee0b4 to 00cee0db has its CatchHandler @ 00bee6fc */
                  uVar5 = uVar5 * 2 + 2;
                  puVar1 = param_1 + uVar12;
                  puVar4 = puVar15;
                  if ((long)uVar5 < lVar6) break;
                  uVar8 = *puVar1;
                  uVar5 = uVar12;
                  puVar10 = puVar1;
                  if (uVar8 < uVar13) goto LAB_00bee000;
                }
                uVar3 = *puVar1;
                uVar14 = puVar1[1];
                uVar8 = uVar3;
                if (uVar3 <= uVar14) {
                  uVar8 = uVar14;
                }
                puVar10 = puVar1 + 1;
                if (uVar14 <= uVar3) {
                  uVar5 = uVar12;
                  puVar10 = puVar1;
                }
              } while (uVar13 <= uVar8);
LAB_00bee000:
              *puVar15 = uVar13;
            }
          }
        }
        puVar7 = puVar7 + 1;
        puVar10 = param_3;
      } while (puVar7 != param_3);
    }
    param_3 = puVar10;
    if (1 < lVar6) {
      do {
        uVar8 = *param_1;
        uVar13 = 0;
        puVar10 = param_1;
                    /* try { // try from 00bee114 to 00cee12f has its CatchHandler @ 00bee794 */
        do {
          uVar12 = uVar13 << 1 | 1;
          uVar5 = uVar13 * 2 + 2;
          puVar11 = puVar10 + uVar13 + 1;
          if ((long)uVar5 < lVar6) {
            uVar3 = puVar10[uVar13 + 2];
            uVar16 = puVar10[uVar13 + 1];
            uVar14 = uVar16;
            if (uVar16 <= uVar3) {
              uVar14 = uVar3;
            }
            puVar7 = puVar10 + uVar13 + 2;
            uVar13 = uVar5;
            if (uVar3 <= uVar16) {
              puVar7 = puVar11;
              uVar13 = uVar12;
            }
          }
          else {
            uVar14 = *puVar11;
            puVar7 = puVar11;
            uVar13 = uVar12;
          }
                    /* try { // try from 00bee130 to 00cee1db has its CatchHandler @ 00bedde0 */
          *puVar10 = uVar14;
          puVar10 = puVar7;
        } while ((long)uVar13 <= (long)(lVar6 - 2U >> 1));
        param_2 = param_2 + -1;
        if (puVar7 == param_2) {
          *puVar7 = uVar8;
        }
        else {
          lVar9 = (long)puVar7 + (8 - (long)param_1) >> 3;
          *puVar7 = *param_2;
          *param_2 = uVar8;
          if (1 < lVar9) {
            uVar13 = lVar9 - 2U >> 1;
            uVar8 = *puVar7;
            uVar5 = param_1[uVar13];
            puVar10 = param_1 + uVar13;
            if (uVar5 < uVar8) {
              do {
                puVar11 = puVar10;
                *puVar7 = uVar5;
                if (uVar13 == 0) break;
                uVar13 = uVar13 - 1 >> 1;
                uVar5 = param_1[uVar13];
                puVar7 = puVar11;
                puVar10 = param_1 + uVar13;
              } while (uVar5 < uVar8);
              *puVar11 = uVar8;
                    /* try { // try from 00bee1dc to 00cee257 has its CatchHandler @ 00bee754 */
            }
          }
        }
                    /* try { // try from 00bee0f4 to 00cee10b has its CatchHandler @ 00bee6ec */
        bVar2 = 2 < lVar6;
        lVar6 = lVar6 + -1;
      } while (bVar2);
    }
  }
                    /* try { // try from 00bee0e8 to 00cee0ef has its CatchHandler @ 00bee6f4 */
  return param_3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bedee4"></a> `00bedee4` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bedee8"></a> `00bedee8` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-00bedeec"></a> `00bedeec` | `e0 0f 00 54` | b.eq 0x00bee0e8 | `CONDITIONAL_JUMP`
<a id="insn-00bedef0"></a> `00bedef0` | `29 00 00 cb` | sub x9,x1,x0 | `FALL_THROUGH`
<a id="insn-00bedef4"></a> `00bedef4` | `28 fd 43 93` | asr x8,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00bedef8"></a> `00bedef8` | `0a 09 00 f1` | subs x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bedefc"></a> `00bedefc` | `0b 07 00 54` | b.lt 0x00bedfdc | `CONDITIONAL_JUMP`
<a id="insn-00bedf00"></a> `00bedf00` | `4b fd 41 d3` | lsr x11,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bedf04"></a> `00bedf04` | `ec 03 0b aa` | mov x12,x11 | `FALL_THROUGH`
<a id="insn-00bedf08"></a> `00bedf08` | `05 00 00 14` | b 0x00bedf1c | `UNCONDITIONAL_JUMP`
<a id="insn-00bedf0c"></a> `00bedf0c` | `0f 02 00 f9` | str x15,[x16] | `FALL_THROUGH`
<a id="insn-00bedf10"></a> `00bedf10` | `9f 01 00 f1` | cmp x12,#0x0 | `FALL_THROUGH`
<a id="insn-00bedf14"></a> `00bedf14` | `8c 05 00 d1` | sub x12,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00bedf18"></a> `00bedf18` | `2d 06 00 54` | b.le 0x00bedfdc | `CONDITIONAL_JUMP`
<a id="insn-00bedf1c"></a> `00bedf1c` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-00bedf20"></a> `00bedf20` | `8b ff ff 54` | b.lt 0x00bedf10 | `CONDITIONAL_JUMP`
<a id="insn-00bedf24"></a> `00bedf24` | `2e 00 80 52` | mov w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bedf28"></a> `00bedf28` | `8d f1 7f d3` | ubfiz x13,x12,#0x1,#0x3d | `FALL_THROUGH`
<a id="insn-00bedf2c"></a> `00bedf2c` | `8e f1 7f b3` | bfm x14,x12,#0x3f,#0x3c | `FALL_THROUGH`
<a id="insn-00bedf30"></a> `00bedf30` | `af 09 00 91` | add x15,x13,#0x2 | `FALL_THROUGH`
<a id="insn-00bedf34"></a> `00bedf34` | `0d 0c 0e 8b` | add x13,x0,x14, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bedf38"></a> `00bedf38` | `ff 01 08 eb` | cmp x15,x8 | `FALL_THROUGH`
<a id="insn-00bedf3c"></a> `00bedf3c` | `2a 01 00 54` | b.ge 0x00bedf60 | `CONDITIONAL_JUMP`
<a id="insn-00bedf40"></a> `00bedf40` | `f0 03 0d aa` | mov x16,x13 | `FALL_THROUGH`
<a id="insn-00bedf44"></a> `00bedf44` | `b1 01 40 f9` | ldr x17,[x13] | `FALL_THROUGH`
<a id="insn-00bedf48"></a> `00bedf48` | `03 8e 40 f8` | ldr x3,[x16, #0x8]! | `FALL_THROUGH`
<a id="insn-00bedf4c"></a> `00bedf4c` | `3f 02 03 eb` | cmp x17,x3 | `FALL_THROUGH`
<a id="insn-00bedf50"></a> `00bedf50` | `31 82 83 9a` | csel x17,x17,x3,hi | `FALL_THROUGH`
<a id="insn-00bedf54"></a> `00bedf54` | `0d 32 8d 9a` | csel x13,x16,x13,cc | `FALL_THROUGH`
<a id="insn-00bedf58"></a> `00bedf58` | `ee 31 8e 9a` | csel x14,x15,x14,cc | `FALL_THROUGH`
<a id="insn-00bedf5c"></a> `00bedf5c` | `02 00 00 14` | b 0x00bedf64 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedf60"></a> `00bedf60` | `b1 01 40 f9` | ldr x17,[x13] | `FALL_THROUGH`
<a id="insn-00bedf64"></a> `00bedf64` | `10 0c 0c 8b` | add x16,x0,x12, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bedf68"></a> `00bedf68` | `0f 02 40 f9` | ldr x15,[x16] | `FALL_THROUGH`
<a id="insn-00bedf6c"></a> `00bedf6c` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bedf70"></a> `00bedf70` | `62 01 00 54` | b.cs 0x00bedf9c | `CONDITIONAL_JUMP`
<a id="insn-00bedf74"></a> `00bedf74` | `e7 ff ff 17` | b 0x00bedf10 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedf78"></a> `00bedf78` | `e4 03 0d aa` | mov x4,x13 | `FALL_THROUGH`
<a id="insn-00bedf7c"></a> `00bedf7c` | `b1 01 40 f9` | ldr x17,[x13] | `FALL_THROUGH`
<a id="insn-00bedf80"></a> `00bedf80` | `85 8c 40 f8` | ldr x5,[x4, #0x8]! | `FALL_THROUGH`
<a id="insn-00bedf84"></a> `00bedf84` | `3f 02 05 eb` | cmp x17,x5 | `FALL_THROUGH`
<a id="insn-00bedf88"></a> `00bedf88` | `31 82 85 9a` | csel x17,x17,x5,hi | `FALL_THROUGH`
<a id="insn-00bedf8c"></a> `00bedf8c` | `8d 30 8d 9a` | csel x13,x4,x13,cc | `FALL_THROUGH`
<a id="insn-00bedf90"></a> `00bedf90` | `ce 31 83 9a` | csel x14,x14,x3,cc | `FALL_THROUGH`
<a id="insn-00bedf94"></a> `00bedf94` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bedf98"></a> `00bedf98` | `a3 fb ff 54` | b.cc 0x00bedf0c | `CONDITIONAL_JUMP`
<a id="insn-00bedf9c"></a> `00bedf9c` | `7f 01 0e eb` | cmp x11,x14 | `FALL_THROUGH`
<a id="insn-00bedfa0"></a> `00bedfa0` | `11 02 00 f9` | str x17,[x16] | `FALL_THROUGH`
<a id="insn-00bedfa4"></a> `00bedfa4` | `f0 03 0d aa` | mov x16,x13 | `FALL_THROUGH`
<a id="insn-00bedfa8"></a> `00bedfa8` | `2b fb ff 54` | b.lt 0x00bedf0c | `CONDITIONAL_JUMP`
<a id="insn-00bedfac"></a> `00bedfac` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bedfb0"></a> `00bedfb0` | `cd f9 7f d3` | lsl x13,x14,#0x1 | `FALL_THROUGH`
<a id="insn-00bedfb4"></a> `00bedfb4` | `c3 f9 7f b3` | bfm x3,x14,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bedfb8"></a> `00bedfb8` | `ae 09 00 91` | add x14,x13,#0x2 | `FALL_THROUGH`
<a id="insn-00bedfbc"></a> `00bedfbc` | `0d 0c 03 8b` | add x13,x0,x3, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bedfc0"></a> `00bedfc0` | `df 01 08 eb` | cmp x14,x8 | `FALL_THROUGH`
<a id="insn-00bedfc4"></a> `00bedfc4` | `ab fd ff 54` | b.lt 0x00bedf78 | `CONDITIONAL_JUMP`
<a id="insn-00bedfc8"></a> `00bedfc8` | `b1 01 40 f9` | ldr x17,[x13] | `FALL_THROUGH`
<a id="insn-00bedfcc"></a> `00bedfcc` | `ee 03 03 aa` | mov x14,x3 | `FALL_THROUGH`
<a id="insn-00bedfd0"></a> `00bedfd0` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bedfd4"></a> `00bedfd4` | `42 fe ff 54` | b.cs 0x00bedf9c | `CONDITIONAL_JUMP`
<a id="insn-00bedfd8"></a> `00bedfd8` | `cd ff ff 17` | b 0x00bedf0c | `UNCONDITIONAL_JUMP`
<a id="insn-00bedfdc"></a> `00bedfdc` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-00bedfe0"></a> `00bedfe0` | `e3 03 01 aa` | mov x3,x1 | `FALL_THROUGH`
<a id="insn-00bedfe4"></a> `00bedfe4` | `c0 07 00 54` | b.eq 0x00bee0dc | `CONDITIONAL_JUMP`
<a id="insn-00bedfe8"></a> `00bedfe8` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bedfec"></a> `00bedfec` | `0b 20 00 91` | add x11,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bedff0"></a> `00bedff0` | `0c 40 00 91` | add x12,x0,#0x10 | `FALL_THROUGH`
<a id="insn-00bedff4"></a> `00bedff4` | `2d 00 80 52` | mov w13,#0x1 | `FALL_THROUGH`
<a id="insn-00bedff8"></a> `00bedff8` | `ee 03 01 aa` | mov x14,x1 | `FALL_THROUGH`
<a id="insn-00bedffc"></a> `00bedffc` | `05 00 00 14` | b 0x00bee010 | `UNCONDITIONAL_JUMP`
<a id="insn-00bee000"></a> `00bee000` | `6f 00 00 f9` | str x15,[x3] | `FALL_THROUGH`
<a id="insn-00bee004"></a> `00bee004` | `ce 21 00 91` | add x14,x14,#0x8 | `FALL_THROUGH`
<a id="insn-00bee008"></a> `00bee008` | `df 01 02 eb` | cmp x14,x2 | `FALL_THROUGH`
<a id="insn-00bee00c"></a> `00bee00c` | `60 06 00 54` | b.eq 0x00bee0d8 | `CONDITIONAL_JUMP`
<a id="insn-00bee010"></a> `00bee010` | `cf 01 40 f9` | ldr x15,[x14] | `FALL_THROUGH`
<a id="insn-00bee014"></a> `00bee014` | `10 00 40 f9` | ldr x16,[x0] | `FALL_THROUGH`
<a id="insn-00bee018"></a> `00bee018` | `ff 01 10 eb` | cmp x15,x16 | `FALL_THROUGH`
<a id="insn-00bee01c"></a> `00bee01c` | `42 ff ff 54` | b.cs 0x00bee004 | `CONDITIONAL_JUMP`
<a id="insn-00bee020"></a> `00bee020` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bee024"></a> `00bee024` | `d0 01 00 f9` | str x16,[x14] | `FALL_THROUGH`
<a id="insn-00bee028"></a> `00bee028` | `0f 00 00 f9` | str x15,[x0] | `FALL_THROUGH`
<a id="insn-00bee02c"></a> `00bee02c` | `cb fe ff 54` | b.lt 0x00bee004 | `CONDITIONAL_JUMP`
<a id="insn-00bee030"></a> `00bee030` | `71 01 40 f9` | ldr x17,[x11] | `FALL_THROUGH`
<a id="insn-00bee034"></a> `00bee034` | `3f 41 00 f1` | cmp x9,#0x10 | `FALL_THROUGH`
<a id="insn-00bee038"></a> `00bee038` | `c1 00 00 54` | b.ne 0x00bee050 | `CONDITIONAL_JUMP`
<a id="insn-00bee03c"></a> `00bee03c` | `f0 03 0b aa` | mov x16,x11 | `FALL_THROUGH`
<a id="insn-00bee040"></a> `00bee040` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-00bee044"></a> `00bee044` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bee048"></a> `00bee048` | `e3 fd ff 54` | b.cc 0x00bee004 | `CONDITIONAL_JUMP`
<a id="insn-00bee04c"></a> `00bee04c` | `08 00 00 14` | b 0x00bee06c | `UNCONDITIONAL_JUMP`
<a id="insn-00bee050"></a> `00bee050` | `90 01 40 f9` | ldr x16,[x12] | `FALL_THROUGH`
<a id="insn-00bee054"></a> `00bee054` | `3f 02 10 eb` | cmp x17,x16 | `FALL_THROUGH`
<a id="insn-00bee058"></a> `00bee058` | `31 82 90 9a` | csel x17,x17,x16,hi | `FALL_THROUGH`
<a id="insn-00bee05c"></a> `00bee05c` | `90 31 8b 9a` | csel x16,x12,x11,cc | `FALL_THROUGH`
<a id="insn-00bee060"></a> `00bee060` | `a4 25 8d 9a` | cinc x4,x13,cc | `FALL_THROUGH`
<a id="insn-00bee064"></a> `00bee064` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bee068"></a> `00bee068` | `e3 fc ff 54` | b.cc 0x00bee004 | `CONDITIONAL_JUMP`
<a id="insn-00bee06c"></a> `00bee06c` | `e3 03 00 aa` | mov x3,x0 | `FALL_THROUGH`
<a id="insn-00bee070"></a> `00bee070` | `0a 00 00 14` | b 0x00bee098 | `UNCONDITIONAL_JUMP`
<a id="insn-00bee074"></a> `00bee074` | `e6 03 10 aa` | mov x6,x16 | `FALL_THROUGH`
<a id="insn-00bee078"></a> `00bee078` | `11 02 40 f9` | ldr x17,[x16] | `FALL_THROUGH`
<a id="insn-00bee07c"></a> `00bee07c` | `c7 8c 40 f8` | ldr x7,[x6, #0x8]! | `FALL_THROUGH`
<a id="insn-00bee080"></a> `00bee080` | `3f 02 07 eb` | cmp x17,x7 | `FALL_THROUGH`
<a id="insn-00bee084"></a> `00bee084` | `31 82 87 9a` | csel x17,x17,x7,hi | `FALL_THROUGH`
<a id="insn-00bee088"></a> `00bee088` | `d0 30 90 9a` | csel x16,x6,x16,cc | `FALL_THROUGH`
<a id="insn-00bee08c"></a> `00bee08c` | `84 30 85 9a` | csel x4,x4,x5,cc | `FALL_THROUGH`
<a id="insn-00bee090"></a> `00bee090` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bee094"></a> `00bee094` | `63 fb ff 54` | b.cc 0x00bee000 | `CONDITIONAL_JUMP`
<a id="insn-00bee098"></a> `00bee098` | `5f 01 04 eb` | cmp x10,x4 | `FALL_THROUGH`
<a id="insn-00bee09c"></a> `00bee09c` | `71 00 00 f9` | str x17,[x3] | `FALL_THROUGH`
<a id="insn-00bee0a0"></a> `00bee0a0` | `e3 03 10 aa` | mov x3,x16 | `FALL_THROUGH`
<a id="insn-00bee0a4"></a> `00bee0a4` | `eb fa ff 54` | b.lt 0x00bee000 | `CONDITIONAL_JUMP`
<a id="insn-00bee0a8"></a> `00bee0a8` | `25 00 80 52` | mov w5,#0x1 | `FALL_THROUGH`
<a id="insn-00bee0ac"></a> `00bee0ac` | `90 f8 7f d3` | lsl x16,x4,#0x1 | `FALL_THROUGH`
<a id="insn-00bee0b0"></a> `00bee0b0` | `85 f8 7f b3` | bfm x5,x4,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bee0b4"></a> `00bee0b4` | `04 0a 00 91` | add x4,x16,#0x2 | `FALL_THROUGH`
<a id="insn-00bee0b8"></a> `00bee0b8` | `10 0c 05 8b` | add x16,x0,x5, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bee0bc"></a> `00bee0bc` | `9f 00 08 eb` | cmp x4,x8 | `FALL_THROUGH`
<a id="insn-00bee0c0"></a> `00bee0c0` | `ab fd ff 54` | b.lt 0x00bee074 | `CONDITIONAL_JUMP`
<a id="insn-00bee0c4"></a> `00bee0c4` | `11 02 40 f9` | ldr x17,[x16] | `FALL_THROUGH`
<a id="insn-00bee0c8"></a> `00bee0c8` | `e4 03 05 aa` | mov x4,x5 | `FALL_THROUGH`
<a id="insn-00bee0cc"></a> `00bee0cc` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bee0d0"></a> `00bee0d0` | `42 fe ff 54` | b.cs 0x00bee098 | `CONDITIONAL_JUMP`
<a id="insn-00bee0d4"></a> `00bee0d4` | `cb ff ff 17` | b 0x00bee000 | `UNCONDITIONAL_JUMP`
<a id="insn-00bee0d8"></a> `00bee0d8` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bee0dc"></a> `00bee0dc` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bee0e0"></a> `00bee0e0` | `0a 01 00 54` | b.ge 0x00bee100 | `CONDITIONAL_JUMP`
<a id="insn-00bee0e4"></a> `00bee0e4` | `e2 03 03 aa` | mov x2,x3 | `FALL_THROUGH`
<a id="insn-00bee0e8"></a> `00bee0e8` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bee0ec"></a> `00bee0ec` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bee0f0"></a> `00bee0f0` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bee0f4"></a> `00bee0f4` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bee0f8"></a> `00bee0f8` | `08 05 00 d1` | sub x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bee0fc"></a> `00bee0fc` | `4d ff ff 54` | b.le 0x00bee0e4 | `CONDITIONAL_JUMP`
<a id="insn-00bee100"></a> `00bee100` | `09 09 00 d1` | sub x9,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bee104"></a> `00bee104` | `0a 00 40 f9` | ldr x10,[x0] | `FALL_THROUGH`
<a id="insn-00bee108"></a> `00bee108` | `ed 03 1f aa` | mov x13,xzr | `FALL_THROUGH`
<a id="insn-00bee10c"></a> `00bee10c` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bee110"></a> `00bee110` | `ec 03 00 aa` | mov x12,x0 | `FALL_THROUGH`
<a id="insn-00bee114"></a> `00bee114` | `0b 00 00 14` | b 0x00bee140 | `UNCONDITIONAL_JUMP`
<a id="insn-00bee118"></a> `00bee118` | `0d 0e 41 f8` | ldr x13,[x16, #0x10]! | `FALL_THROUGH`
<a id="insn-00bee11c"></a> `00bee11c` | `0f 82 5f f8` | ldur x15,[x16, #-0x8] | `FALL_THROUGH`
<a id="insn-00bee120"></a> `00bee120` | `ff 01 0d eb` | cmp x15,x13 | `FALL_THROUGH`
<a id="insn-00bee124"></a> `00bee124` | `ef 81 8d 9a` | csel x15,x15,x13,hi | `FALL_THROUGH`
<a id="insn-00bee128"></a> `00bee128` | `09 32 89 9a` | csel x9,x16,x9,cc | `FALL_THROUGH`
<a id="insn-00bee12c"></a> `00bee12c` | `2d 32 8e 9a` | csel x13,x17,x14,cc | `FALL_THROUGH`
<a id="insn-00bee130"></a> `00bee130` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00bee134"></a> `00bee134` | `8f 01 00 f9` | str x15,[x12] | `FALL_THROUGH`
<a id="insn-00bee138"></a> `00bee138` | `ec 03 09 aa` | mov x12,x9 | `FALL_THROUGH`
<a id="insn-00bee13c"></a> `00bee13c` | `8c 01 00 54` | b.gt 0x00bee16c | `CONDITIONAL_JUMP`
<a id="insn-00bee140"></a> `00bee140` | `a9 f9 7f d3` | lsl x9,x13,#0x1 | `FALL_THROUGH`
<a id="insn-00bee144"></a> `00bee144` | `90 0d 0d 8b` | add x16,x12,x13, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bee148"></a> `00bee148` | `2e 00 80 52` | mov w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bee14c"></a> `00bee14c` | `ae f9 7f b3` | bfm x14,x13,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bee150"></a> `00bee150` | `31 09 00 91` | add x17,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bee154"></a> `00bee154` | `09 22 00 91` | add x9,x16,#0x8 | `FALL_THROUGH`
<a id="insn-00bee158"></a> `00bee158` | `3f 02 08 eb` | cmp x17,x8 | `FALL_THROUGH`
<a id="insn-00bee15c"></a> `00bee15c` | `eb fd ff 54` | b.lt 0x00bee118 | `CONDITIONAL_JUMP`
<a id="insn-00bee160"></a> `00bee160` | `2f 01 40 f9` | ldr x15,[x9] | `FALL_THROUGH`
<a id="insn-00bee164"></a> `00bee164` | `ed 03 0e aa` | mov x13,x14 | `FALL_THROUGH`
<a id="insn-00bee168"></a> `00bee168` | `f2 ff ff 17` | b 0x00bee130 | `UNCONDITIONAL_JUMP`
<a id="insn-00bee16c"></a> `00bee16c` | `21 20 00 d1` | sub x1,x1,#0x8 | `FALL_THROUGH`
<a id="insn-00bee170"></a> `00bee170` | `3f 01 01 eb` | cmp x9,x1 | `FALL_THROUGH`
<a id="insn-00bee174"></a> `00bee174` | `e0 fb ff 54` | b.eq 0x00bee0f0 | `CONDITIONAL_JUMP`
<a id="insn-00bee178"></a> `00bee178` | `2b 01 00 cb` | sub x11,x9,x0 | `FALL_THROUGH`
<a id="insn-00bee17c"></a> `00bee17c` | `2c 00 40 f9` | ldr x12,[x1] | `FALL_THROUGH`
<a id="insn-00bee180"></a> `00bee180` | `6b 21 00 91` | add x11,x11,#0x8 | `FALL_THROUGH`
<a id="insn-00bee184"></a> `00bee184` | `6b fd 43 93` | asr x11,x11,#0x3 | `FALL_THROUGH`
<a id="insn-00bee188"></a> `00bee188` | `2c 01 00 f9` | str x12,[x9] | `FALL_THROUGH`
<a id="insn-00bee18c"></a> `00bee18c` | `2a 00 00 f9` | str x10,[x1] | `FALL_THROUGH`
<a id="insn-00bee190"></a> `00bee190` | `6b 09 00 f1` | subs x11,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00bee194"></a> `00bee194` | `0b fb ff 54` | b.lt 0x00bee0f4 | `CONDITIONAL_JUMP`
<a id="insn-00bee198"></a> `00bee198` | `6a fd 41 d3` | lsr x10,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00bee19c"></a> `00bee19c` | `2b 01 40 f9` | ldr x11,[x9] | `FALL_THROUGH`
<a id="insn-00bee1a0"></a> `00bee1a0` | `0c 0c 0a 8b` | add x12,x0,x10, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bee1a4"></a> `00bee1a4` | `8d 01 40 f9` | ldr x13,[x12] | `FALL_THROUGH`
<a id="insn-00bee1a8"></a> `00bee1a8` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00bee1ac"></a> `00bee1ac` | `42 fa ff 54` | b.cs 0x00bee0f4 | `CONDITIONAL_JUMP`
<a id="insn-00bee1b0"></a> `00bee1b0` | `ee 03 09 aa` | mov x14,x9 | `FALL_THROUGH`
<a id="insn-00bee1b4"></a> `00bee1b4` | `e9 03 0c aa` | mov x9,x12 | `FALL_THROUGH`
<a id="insn-00bee1b8"></a> `00bee1b8` | `cd 01 00 f9` | str x13,[x14] | `FALL_THROUGH`
<a id="insn-00bee1bc"></a> `00bee1bc` | `ea 00 00 b4` | cbz x10,0x00bee1d8 | `CONDITIONAL_JUMP`
<a id="insn-00bee1c0"></a> `00bee1c0` | `4a 05 00 d1` | sub x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bee1c4"></a> `00bee1c4` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bee1c8"></a> `00bee1c8` | `0c 0c 0a 8b` | add x12,x0,x10, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bee1cc"></a> `00bee1cc` | `8d 01 40 f9` | ldr x13,[x12] | `FALL_THROUGH`
<a id="insn-00bee1d0"></a> `00bee1d0` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00bee1d4"></a> `00bee1d4` | `e3 fe ff 54` | b.cc 0x00bee1b0 | `CONDITIONAL_JUMP`
<a id="insn-00bee1d8"></a> `00bee1d8` | `2b 01 00 f9` | str x11,[x9] | `FALL_THROUGH`
<a id="insn-00bee1dc"></a> `00bee1dc` | `c6 ff ff 17` | b 0x00bee0f4 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bedee4`](#insn-00bedee4) 範囲 `[['00bedee4', '00bedeef']]`
  - `CONDITIONAL_JUMP` [`00bedeec`](#insn-00bedeec) → [`00bee0e8`](#insn-00bee0e8)
  - `FALL_THROUGH` [`00bedeec`](#insn-00bedeec) → [`00bedef0`](#insn-00bedef0)
- ブロック [`00bedef0`](#insn-00bedef0) 範囲 `[['00bedef0', '00bedeff']]`
  - `CONDITIONAL_JUMP` [`00bedefc`](#insn-00bedefc) → [`00bedfdc`](#insn-00bedfdc)
  - `FALL_THROUGH` [`00bedefc`](#insn-00bedefc) → [`00bedf00`](#insn-00bedf00)
- ブロック [`00bedf00`](#insn-00bedf00) 範囲 `[['00bedf00', '00bedf0b']]`
  - `UNCONDITIONAL_JUMP` [`00bedf08`](#insn-00bedf08) → [`00bedf1c`](#insn-00bedf1c)
- ブロック [`00bedf0c`](#insn-00bedf0c) 範囲 `[['00bedf0c', '00bedf0f']]`
  - `FALL_THROUGH` [`00bedf0c`](#insn-00bedf0c) → [`00bedf10`](#insn-00bedf10)
- ブロック [`00bedf10`](#insn-00bedf10) 範囲 `[['00bedf10', '00bedf1b']]`
  - `CONDITIONAL_JUMP` [`00bedf18`](#insn-00bedf18) → [`00bedfdc`](#insn-00bedfdc)
  - `FALL_THROUGH` [`00bedf18`](#insn-00bedf18) → [`00bedf1c`](#insn-00bedf1c)
- ブロック [`00bedf1c`](#insn-00bedf1c) 範囲 `[['00bedf1c', '00bedf23']]`
  - `CONDITIONAL_JUMP` [`00bedf20`](#insn-00bedf20) → [`00bedf10`](#insn-00bedf10)
  - `FALL_THROUGH` [`00bedf20`](#insn-00bedf20) → [`00bedf24`](#insn-00bedf24)
- ブロック [`00bedf24`](#insn-00bedf24) 範囲 `[['00bedf24', '00bedf3b']]`
  - `FALL_THROUGH` [`00bedf38`](#insn-00bedf38) → [`00bedf3c`](#insn-00bedf3c)
- ブロック [`00bedf3c`](#insn-00bedf3c) 範囲 `[['00bedf3c', '00bedf3f']]`
  - `CONDITIONAL_JUMP` [`00bedf3c`](#insn-00bedf3c) → [`00bedf60`](#insn-00bedf60)
  - `FALL_THROUGH` [`00bedf3c`](#insn-00bedf3c) → [`00bedf40`](#insn-00bedf40)
- ブロック [`00bedf40`](#insn-00bedf40) 範囲 `[['00bedf40', '00bedf47']]`
  - `FALL_THROUGH` [`00bedf44`](#insn-00bedf44) → [`00bedf48`](#insn-00bedf48)
- ブロック [`00bedf48`](#insn-00bedf48) 範囲 `[['00bedf48', '00bedf5f']]`
  - `UNCONDITIONAL_JUMP` [`00bedf5c`](#insn-00bedf5c) → [`00bedf64`](#insn-00bedf64)
- ブロック [`00bedf60`](#insn-00bedf60) 範囲 `[['00bedf60', '00bedf63']]`
  - `FALL_THROUGH` [`00bedf60`](#insn-00bedf60) → [`00bedf64`](#insn-00bedf64)
- ブロック [`00bedf64`](#insn-00bedf64) 範囲 `[['00bedf64', '00bedf6b']]`
  - `FALL_THROUGH` [`00bedf68`](#insn-00bedf68) → [`00bedf6c`](#insn-00bedf6c)
- ブロック [`00bedf6c`](#insn-00bedf6c) 範囲 `[['00bedf6c', '00bedf73']]`
  - `CONDITIONAL_JUMP` [`00bedf70`](#insn-00bedf70) → [`00bedf9c`](#insn-00bedf9c)
  - `FALL_THROUGH` [`00bedf70`](#insn-00bedf70) → [`00bedf74`](#insn-00bedf74)
- ブロック [`00bedf74`](#insn-00bedf74) 範囲 `[['00bedf74', '00bedf77']]`
  - `UNCONDITIONAL_JUMP` [`00bedf74`](#insn-00bedf74) → [`00bedf10`](#insn-00bedf10)
- ブロック [`00bedf78`](#insn-00bedf78) 範囲 `[['00bedf78', '00bedf87']]`
  - `FALL_THROUGH` [`00bedf84`](#insn-00bedf84) → [`00bedf88`](#insn-00bedf88)
- ブロック [`00bedf88`](#insn-00bedf88) 範囲 `[['00bedf88', '00bedf9b']]`
  - `CONDITIONAL_JUMP` [`00bedf98`](#insn-00bedf98) → [`00bedf0c`](#insn-00bedf0c)
  - `FALL_THROUGH` [`00bedf98`](#insn-00bedf98) → [`00bedf9c`](#insn-00bedf9c)
- ブロック [`00bedf9c`](#insn-00bedf9c) 範囲 `[['00bedf9c', '00bedfab']]`
  - `CONDITIONAL_JUMP` [`00bedfa8`](#insn-00bedfa8) → [`00bedf0c`](#insn-00bedf0c)
  - `FALL_THROUGH` [`00bedfa8`](#insn-00bedfa8) → [`00bedfac`](#insn-00bedfac)
- ブロック [`00bedfac`](#insn-00bedfac) 範囲 `[['00bedfac', '00bedfc7']]`
  - `CONDITIONAL_JUMP` [`00bedfc4`](#insn-00bedfc4) → [`00bedf78`](#insn-00bedf78)
  - `FALL_THROUGH` [`00bedfc4`](#insn-00bedfc4) → [`00bedfc8`](#insn-00bedfc8)
- ブロック [`00bedfc8`](#insn-00bedfc8) 範囲 `[['00bedfc8', '00bedfd7']]`
  - `CONDITIONAL_JUMP` [`00bedfd4`](#insn-00bedfd4) → [`00bedf9c`](#insn-00bedf9c)
  - `FALL_THROUGH` [`00bedfd4`](#insn-00bedfd4) → [`00bedfd8`](#insn-00bedfd8)
- ブロック [`00bedfd8`](#insn-00bedfd8) 範囲 `[['00bedfd8', '00bedfdb']]`
  - `UNCONDITIONAL_JUMP` [`00bedfd8`](#insn-00bedfd8) → [`00bedf0c`](#insn-00bedf0c)
- ブロック [`00bedfdc`](#insn-00bedfdc) 範囲 `[['00bedfdc', '00bedfe7']]`
  - `CONDITIONAL_JUMP` [`00bedfe4`](#insn-00bedfe4) → [`00bee0dc`](#insn-00bee0dc)
  - `FALL_THROUGH` [`00bedfe4`](#insn-00bedfe4) → [`00bedfe8`](#insn-00bedfe8)
- ブロック [`00bedfe8`](#insn-00bedfe8) 範囲 `[['00bedfe8', '00bedfff']]`
  - `UNCONDITIONAL_JUMP` [`00bedffc`](#insn-00bedffc) → [`00bee010`](#insn-00bee010)
- ブロック [`00bee000`](#insn-00bee000) 範囲 `[['00bee000', '00bee003']]`
  - `FALL_THROUGH` [`00bee000`](#insn-00bee000) → [`00bee004`](#insn-00bee004)
- ブロック [`00bee004`](#insn-00bee004) 範囲 `[['00bee004', '00bee00f']]`
  - `CONDITIONAL_JUMP` [`00bee00c`](#insn-00bee00c) → [`00bee0d8`](#insn-00bee0d8)
  - `FALL_THROUGH` [`00bee00c`](#insn-00bee00c) → [`00bee010`](#insn-00bee010)
- ブロック [`00bee010`](#insn-00bee010) 範囲 `[['00bee010', '00bee01f']]`
  - `CONDITIONAL_JUMP` [`00bee01c`](#insn-00bee01c) → [`00bee004`](#insn-00bee004)
  - `FALL_THROUGH` [`00bee01c`](#insn-00bee01c) → [`00bee020`](#insn-00bee020)
- ブロック [`00bee020`](#insn-00bee020) 範囲 `[['00bee020', '00bee02f']]`
  - `CONDITIONAL_JUMP` [`00bee02c`](#insn-00bee02c) → [`00bee004`](#insn-00bee004)
  - `FALL_THROUGH` [`00bee02c`](#insn-00bee02c) → [`00bee030`](#insn-00bee030)
- ブロック [`00bee030`](#insn-00bee030) 範囲 `[['00bee030', '00bee03b']]`
  - `CONDITIONAL_JUMP` [`00bee038`](#insn-00bee038) → [`00bee050`](#insn-00bee050)
  - `FALL_THROUGH` [`00bee038`](#insn-00bee038) → [`00bee03c`](#insn-00bee03c)
- ブロック [`00bee03c`](#insn-00bee03c) 範囲 `[['00bee03c', '00bee03f']]`
  - `FALL_THROUGH` [`00bee03c`](#insn-00bee03c) → [`00bee040`](#insn-00bee040)
- ブロック [`00bee040`](#insn-00bee040) 範囲 `[['00bee040', '00bee04b']]`
  - `CONDITIONAL_JUMP` [`00bee048`](#insn-00bee048) → [`00bee004`](#insn-00bee004)
  - `FALL_THROUGH` [`00bee048`](#insn-00bee048) → [`00bee04c`](#insn-00bee04c)
- ブロック [`00bee04c`](#insn-00bee04c) 範囲 `[['00bee04c', '00bee04f']]`
  - `UNCONDITIONAL_JUMP` [`00bee04c`](#insn-00bee04c) → [`00bee06c`](#insn-00bee06c)
- ブロック [`00bee050`](#insn-00bee050) 範囲 `[['00bee050', '00bee063']]`
  - `FALL_THROUGH` [`00bee060`](#insn-00bee060) → [`00bee064`](#insn-00bee064)
- ブロック [`00bee064`](#insn-00bee064) 範囲 `[['00bee064', '00bee06b']]`
  - `CONDITIONAL_JUMP` [`00bee068`](#insn-00bee068) → [`00bee004`](#insn-00bee004)
  - `FALL_THROUGH` [`00bee068`](#insn-00bee068) → [`00bee06c`](#insn-00bee06c)
- ブロック [`00bee06c`](#insn-00bee06c) 範囲 `[['00bee06c', '00bee073']]`
  - `UNCONDITIONAL_JUMP` [`00bee070`](#insn-00bee070) → [`00bee098`](#insn-00bee098)
- ブロック [`00bee074`](#insn-00bee074) 範囲 `[['00bee074', '00bee097']]`
  - `CONDITIONAL_JUMP` [`00bee094`](#insn-00bee094) → [`00bee000`](#insn-00bee000)
  - `FALL_THROUGH` [`00bee094`](#insn-00bee094) → [`00bee098`](#insn-00bee098)
- ブロック [`00bee098`](#insn-00bee098) 範囲 `[['00bee098', '00bee0a7']]`
  - `CONDITIONAL_JUMP` [`00bee0a4`](#insn-00bee0a4) → [`00bee000`](#insn-00bee000)
  - `FALL_THROUGH` [`00bee0a4`](#insn-00bee0a4) → [`00bee0a8`](#insn-00bee0a8)
- ブロック [`00bee0a8`](#insn-00bee0a8) 範囲 `[['00bee0a8', '00bee0b3']]`
  - `FALL_THROUGH` [`00bee0b0`](#insn-00bee0b0) → [`00bee0b4`](#insn-00bee0b4)
- ブロック [`00bee0b4`](#insn-00bee0b4) 範囲 `[['00bee0b4', '00bee0c3']]`
  - `CONDITIONAL_JUMP` [`00bee0c0`](#insn-00bee0c0) → [`00bee074`](#insn-00bee074)
  - `FALL_THROUGH` [`00bee0c0`](#insn-00bee0c0) → [`00bee0c4`](#insn-00bee0c4)
- ブロック [`00bee0c4`](#insn-00bee0c4) 範囲 `[['00bee0c4', '00bee0d3']]`
  - `CONDITIONAL_JUMP` [`00bee0d0`](#insn-00bee0d0) → [`00bee098`](#insn-00bee098)
  - `FALL_THROUGH` [`00bee0d0`](#insn-00bee0d0) → [`00bee0d4`](#insn-00bee0d4)
- ブロック [`00bee0d4`](#insn-00bee0d4) 範囲 `[['00bee0d4', '00bee0d7']]`
  - `UNCONDITIONAL_JUMP` [`00bee0d4`](#insn-00bee0d4) → [`00bee000`](#insn-00bee000)
- ブロック [`00bee0d8`](#insn-00bee0d8) 範囲 `[['00bee0d8', '00bee0db']]`
  - `FALL_THROUGH` [`00bee0d8`](#insn-00bee0d8) → [`00bee0dc`](#insn-00bee0dc)
- ブロック [`00bee0dc`](#insn-00bee0dc) 範囲 `[['00bee0dc', '00bee0e3']]`
  - `CONDITIONAL_JUMP` [`00bee0e0`](#insn-00bee0e0) → [`00bee100`](#insn-00bee100)
  - `FALL_THROUGH` [`00bee0e0`](#insn-00bee0e0) → [`00bee0e4`](#insn-00bee0e4)
- ブロック [`00bee0e4`](#insn-00bee0e4) 範囲 `[['00bee0e4', '00bee0e7']]`
  - `FALL_THROUGH` [`00bee0e4`](#insn-00bee0e4) → [`00bee0e8`](#insn-00bee0e8)
- ブロック [`00bee0e8`](#insn-00bee0e8) 範囲 `[['00bee0e8', '00bee0ef']]`
- ブロック [`00bee0f0`](#insn-00bee0f0) 範囲 `[['00bee0f0', '00bee0f3']]`
  - `FALL_THROUGH` [`00bee0f0`](#insn-00bee0f0) → [`00bee0f4`](#insn-00bee0f4)
- ブロック [`00bee0f4`](#insn-00bee0f4) 範囲 `[['00bee0f4', '00bee0ff']]`
  - `CONDITIONAL_JUMP` [`00bee0fc`](#insn-00bee0fc) → [`00bee0e4`](#insn-00bee0e4)
  - `FALL_THROUGH` [`00bee0fc`](#insn-00bee0fc) → [`00bee100`](#insn-00bee100)
- ブロック [`00bee100`](#insn-00bee100) 範囲 `[['00bee100', '00bee113']]`
  - `FALL_THROUGH` [`00bee110`](#insn-00bee110) → [`00bee114`](#insn-00bee114)
- ブロック [`00bee114`](#insn-00bee114) 範囲 `[['00bee114', '00bee117']]`
  - `UNCONDITIONAL_JUMP` [`00bee114`](#insn-00bee114) → [`00bee140`](#insn-00bee140)
- ブロック [`00bee118`](#insn-00bee118) 範囲 `[['00bee118', '00bee12f']]`
  - `FALL_THROUGH` [`00bee12c`](#insn-00bee12c) → [`00bee130`](#insn-00bee130)
- ブロック [`00bee130`](#insn-00bee130) 範囲 `[['00bee130', '00bee13f']]`
  - `CONDITIONAL_JUMP` [`00bee13c`](#insn-00bee13c) → [`00bee16c`](#insn-00bee16c)
  - `FALL_THROUGH` [`00bee13c`](#insn-00bee13c) → [`00bee140`](#insn-00bee140)
- ブロック [`00bee140`](#insn-00bee140) 範囲 `[['00bee140', '00bee15f']]`
  - `CONDITIONAL_JUMP` [`00bee15c`](#insn-00bee15c) → [`00bee118`](#insn-00bee118)
  - `FALL_THROUGH` [`00bee15c`](#insn-00bee15c) → [`00bee160`](#insn-00bee160)
- ブロック [`00bee160`](#insn-00bee160) 範囲 `[['00bee160', '00bee16b']]`
  - `UNCONDITIONAL_JUMP` [`00bee168`](#insn-00bee168) → [`00bee130`](#insn-00bee130)
- ブロック [`00bee16c`](#insn-00bee16c) 範囲 `[['00bee16c', '00bee177']]`
  - `CONDITIONAL_JUMP` [`00bee174`](#insn-00bee174) → [`00bee0f0`](#insn-00bee0f0)
  - `FALL_THROUGH` [`00bee174`](#insn-00bee174) → [`00bee178`](#insn-00bee178)
- ブロック [`00bee178`](#insn-00bee178) 範囲 `[['00bee178', '00bee197']]`
  - `CONDITIONAL_JUMP` [`00bee194`](#insn-00bee194) → [`00bee0f4`](#insn-00bee0f4)
  - `FALL_THROUGH` [`00bee194`](#insn-00bee194) → [`00bee198`](#insn-00bee198)
- ブロック [`00bee198`](#insn-00bee198) 範囲 `[['00bee198', '00bee1af']]`
  - `CONDITIONAL_JUMP` [`00bee1ac`](#insn-00bee1ac) → [`00bee0f4`](#insn-00bee0f4)
  - `FALL_THROUGH` [`00bee1ac`](#insn-00bee1ac) → [`00bee1b0`](#insn-00bee1b0)
- ブロック [`00bee1b0`](#insn-00bee1b0) 範囲 `[['00bee1b0', '00bee1bf']]`
  - `CONDITIONAL_JUMP` [`00bee1bc`](#insn-00bee1bc) → [`00bee1d8`](#insn-00bee1d8)
  - `FALL_THROUGH` [`00bee1bc`](#insn-00bee1bc) → [`00bee1c0`](#insn-00bee1c0)
- ブロック [`00bee1c0`](#insn-00bee1c0) 範囲 `[['00bee1c0', '00bee1d7']]`
  - `CONDITIONAL_JUMP` [`00bee1d4`](#insn-00bee1d4) → [`00bee1b0`](#insn-00bee1b0)
  - `FALL_THROUGH` [`00bee1d4`](#insn-00bee1d4) → [`00bee1d8`](#insn-00bee1d8)
- ブロック [`00bee1d8`](#insn-00bee1d8) 範囲 `[['00bee1d8', '00bee1db']]`
  - `FALL_THROUGH` [`00bee1d8`](#insn-00bee1d8) → [`00bee1dc`](#insn-00bee1dc)
- ブロック [`00bee1dc`](#insn-00bee1dc) 範囲 `[['00bee1dc', '00bee1df']]`
  - `UNCONDITIONAL_JUMP` [`00bee1dc`](#insn-00bee1dc) → [`00bee0f4`](#insn-00bee0f4)

## 命令位置別の参照

- [`00bedeec`](#insn-00bedeec) → [`00bee0e8`](#insn-00bee0e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedefc`](#insn-00bedefc) → [`00bedfdc`](#insn-00bedfdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedf08`](#insn-00bedf08) → [`00bedf1c`](#insn-00bedf1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedf18`](#insn-00bedf18) → [`00bedfdc`](#insn-00bedfdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedf20`](#insn-00bedf20) → [`00bedf10`](#insn-00bedf10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedf3c`](#insn-00bedf3c) → [`00bedf60`](#insn-00bedf60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedf5c`](#insn-00bedf5c) → [`00bedf64`](#insn-00bedf64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedf70`](#insn-00bedf70) → [`00bedf9c`](#insn-00bedf9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedf74`](#insn-00bedf74) → [`00bedf10`](#insn-00bedf10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedf98`](#insn-00bedf98) → [`00bedf0c`](#insn-00bedf0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedfa8`](#insn-00bedfa8) → [`00bedf0c`](#insn-00bedf0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedfc4`](#insn-00bedfc4) → [`00bedf78`](#insn-00bedf78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedfd4`](#insn-00bedfd4) → [`00bedf9c`](#insn-00bedf9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedfd8`](#insn-00bedfd8) → [`00bedf0c`](#insn-00bedf0c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedfe4`](#insn-00bedfe4) → [`00bee0dc`](#insn-00bee0dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedffc`](#insn-00bedffc) → [`00bee010`](#insn-00bee010) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee00c`](#insn-00bee00c) → [`00bee0d8`](#insn-00bee0d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee01c`](#insn-00bee01c) → [`00bee004`](#insn-00bee004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee02c`](#insn-00bee02c) → [`00bee004`](#insn-00bee004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee038`](#insn-00bee038) → [`00bee050`](#insn-00bee050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee048`](#insn-00bee048) → [`00bee004`](#insn-00bee004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee04c`](#insn-00bee04c) → [`00bee06c`](#insn-00bee06c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee068`](#insn-00bee068) → [`00bee004`](#insn-00bee004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee070`](#insn-00bee070) → [`00bee098`](#insn-00bee098) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee094`](#insn-00bee094) → [`00bee000`](#insn-00bee000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee0a4`](#insn-00bee0a4) → [`00bee000`](#insn-00bee000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee0c0`](#insn-00bee0c0) → [`00bee074`](#insn-00bee074) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee0d0`](#insn-00bee0d0) → [`00bee098`](#insn-00bee098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee0d4`](#insn-00bee0d4) → [`00bee000`](#insn-00bee000) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee0e0`](#insn-00bee0e0) → [`00bee100`](#insn-00bee100) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee0fc`](#insn-00bee0fc) → [`00bee0e4`](#insn-00bee0e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee114`](#insn-00bee114) → [`00bee140`](#insn-00bee140) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee13c`](#insn-00bee13c) → [`00bee16c`](#insn-00bee16c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee15c`](#insn-00bee15c) → [`00bee118`](#insn-00bee118) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee168`](#insn-00bee168) → [`00bee130`](#insn-00bee130) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee174`](#insn-00bee174) → [`00bee0f0`](#insn-00bee0f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee194`](#insn-00bee194) → [`00bee0f4`](#insn-00bee0f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee1ac`](#insn-00bee1ac) → [`00bee0f4`](#insn-00bee0f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee1bc`](#insn-00bee1bc) → [`00bee1d8`](#insn-00bee1d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee1d4`](#insn-00bee1d4) → [`00bee1b0`](#insn-00bee1b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee1dc`](#insn-00bee1dc) → [`00bee0f4`](#insn-00bee0f4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bedeec`](#insn-00bedeec)

~~~json
{
  "source": "00bedeec",
  "target": "00bee0e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedefc`](#insn-00bedefc)

~~~json
{
  "source": "00bedefc",
  "target": "00bedfdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedf08`](#insn-00bedf08)

~~~json
{
  "source": "00bedf08",
  "target": "00bedf1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedf18`](#insn-00bedf18)

~~~json
{
  "source": "00bedf18",
  "target": "00bedfdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedf20`](#insn-00bedf20)

~~~json
{
  "source": "00bedf20",
  "target": "00bedf10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedf3c`](#insn-00bedf3c)

~~~json
{
  "source": "00bedf3c",
  "target": "00bedf60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedf5c`](#insn-00bedf5c)

~~~json
{
  "source": "00bedf5c",
  "target": "00bedf64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedf70`](#insn-00bedf70)

~~~json
{
  "source": "00bedf70",
  "target": "00bedf9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedf74`](#insn-00bedf74)

~~~json
{
  "source": "00bedf74",
  "target": "00bedf10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedf98`](#insn-00bedf98)

~~~json
{
  "source": "00bedf98",
  "target": "00bedf0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedfa8`](#insn-00bedfa8)

~~~json
{
  "source": "00bedfa8",
  "target": "00bedf0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedfc4`](#insn-00bedfc4)

~~~json
{
  "source": "00bedfc4",
  "target": "00bedf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedfd4`](#insn-00bedfd4)

~~~json
{
  "source": "00bedfd4",
  "target": "00bedf9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedfd8`](#insn-00bedfd8)

~~~json
{
  "source": "00bedfd8",
  "target": "00bedf0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedfe4`](#insn-00bedfe4)

~~~json
{
  "source": "00bedfe4",
  "target": "00bee0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedffc`](#insn-00bedffc)

~~~json
{
  "source": "00bedffc",
  "target": "00bee010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee00c`](#insn-00bee00c)

~~~json
{
  "source": "00bee00c",
  "target": "00bee0d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee01c`](#insn-00bee01c)

~~~json
{
  "source": "00bee01c",
  "target": "00bee004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee02c`](#insn-00bee02c)

~~~json
{
  "source": "00bee02c",
  "target": "00bee004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee038`](#insn-00bee038)

~~~json
{
  "source": "00bee038",
  "target": "00bee050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee048`](#insn-00bee048)

~~~json
{
  "source": "00bee048",
  "target": "00bee004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee04c`](#insn-00bee04c)

~~~json
{
  "source": "00bee04c",
  "target": "00bee06c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee068`](#insn-00bee068)

~~~json
{
  "source": "00bee068",
  "target": "00bee004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee070`](#insn-00bee070)

~~~json
{
  "source": "00bee070",
  "target": "00bee098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee094`](#insn-00bee094)

~~~json
{
  "source": "00bee094",
  "target": "00bee000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee0a4`](#insn-00bee0a4)

~~~json
{
  "source": "00bee0a4",
  "target": "00bee000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee0c0`](#insn-00bee0c0)

~~~json
{
  "source": "00bee0c0",
  "target": "00bee074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee0d0`](#insn-00bee0d0)

~~~json
{
  "source": "00bee0d0",
  "target": "00bee098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee0d4`](#insn-00bee0d4)

~~~json
{
  "source": "00bee0d4",
  "target": "00bee000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee0e0`](#insn-00bee0e0)

~~~json
{
  "source": "00bee0e0",
  "target": "00bee100",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee0fc`](#insn-00bee0fc)

~~~json
{
  "source": "00bee0fc",
  "target": "00bee0e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee114`](#insn-00bee114)

~~~json
{
  "source": "00bee114",
  "target": "00bee140",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee13c`](#insn-00bee13c)

~~~json
{
  "source": "00bee13c",
  "target": "00bee16c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee15c`](#insn-00bee15c)

~~~json
{
  "source": "00bee15c",
  "target": "00bee118",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee168`](#insn-00bee168)

~~~json
{
  "source": "00bee168",
  "target": "00bee130",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee174`](#insn-00bee174)

~~~json
{
  "source": "00bee174",
  "target": "00bee0f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee194`](#insn-00bee194)

~~~json
{
  "source": "00bee194",
  "target": "00bee0f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee1ac`](#insn-00bee1ac)

~~~json
{
  "source": "00bee1ac",
  "target": "00bee0f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee1bc`](#insn-00bee1bc)

~~~json
{
  "source": "00bee1bc",
  "target": "00bee1d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee1d4`](#insn-00bee1d4)

~~~json
{
  "source": "00bee1d4",
  "target": "00bee1b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee1dc`](#insn-00bee1dc)

~~~json
{
  "source": "00bee1dc",
  "target": "00bee0f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
