# 00bec6dc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00beb6e8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00beb6e8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/no_difference_in_scope-0014.md#compare-cc66b14db24f05255fc0f867115f18e6)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bec6dc",
  "name": "FUN_00bec6dc",
  "size": 764,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "788d69b12ea34b9ef40418d28e65e9bf8736a0f4b22584429c9f9154f5dbbc03",
  "source_text_sha256": "788d69b12ea34b9ef40418d28e65e9bf8736a0f4b22584429c9f9154f5dbbc03",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bec6dc",
        "00bec9d7"
      ]
    ],
    "bytes_sha256": "f3ed589a62affcf95a473490afaab2962430f138d02dd521fe97f1e75e046171",
    "instruction_count": 191,
    "instruction_bytes": 764,
    "body_bytes": 764,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be56ec](../00be5/00be56ec.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6265 bytes

~~~c

ushort * FUN_00bec6dc(ushort *param_1,ushort *param_2,ushort *param_3)

{
  ushort *puVar1;
  ulong uVar2;
  ushort uVar3;
  ushort uVar4;
  bool bVar5;
  ushort *puVar6;
  ulong uVar7;
  long lVar8;
  ushort *puVar9;
  ulong uVar10;
  long lVar11;
  ushort *puVar12;
  ushort *puVar13;
  ulong uVar14;
  ushort uVar15;
  ushort *puVar16;
  ushort uVar17;
  
  if (param_1 != param_2) {
    lVar8 = (long)param_2 - (long)param_1 >> 1;
    if (1 < lVar8) {
      uVar10 = lVar8 - 2U >> 1;
      uVar7 = uVar10;
      do {
        if ((long)uVar7 <= (long)uVar10) {
          uVar2 = uVar7 << 1 | 1;
          uVar14 = uVar7 * 2 + 2;
          puVar12 = param_1 + uVar2;
          if ((long)uVar14 < lVar8) {
            uVar15 = *puVar12;
            uVar3 = puVar12[1];
            uVar17 = uVar15;
            if (uVar15 <= uVar3) {
              uVar17 = uVar3;
            }
            puVar13 = puVar12 + 1;
            if (uVar3 <= uVar15) {
              puVar13 = puVar12;
              uVar14 = uVar2;
            }
          }
          else {
            uVar17 = *puVar12;
            puVar13 = puVar12;
            uVar14 = uVar2;
          }
          uVar15 = param_1[uVar7];
          puVar12 = param_1 + uVar7;
          if (uVar15 <= uVar17) {
            do {
              while( true ) {
                puVar9 = puVar13;
                *puVar12 = uVar17;
                if ((long)uVar10 < (long)uVar14) goto LAB_00bec704;
                uVar2 = uVar14 << 1 | 1;
                uVar14 = uVar14 * 2 + 2;
                puVar6 = param_1 + uVar2;
                puVar12 = puVar9;
                if ((long)uVar14 < lVar8) break;
                uVar17 = *puVar6;
                puVar13 = puVar6;
                uVar14 = uVar2;
                if (uVar17 < uVar15) goto LAB_00bec704;
              }
              uVar3 = *puVar6;
              uVar4 = puVar6[1];
              uVar17 = uVar3;
              if (uVar3 <= uVar4) {
                uVar17 = uVar4;
              }
              puVar13 = puVar6 + 1;
              if (uVar4 <= uVar3) {
                uVar14 = uVar2;
                puVar13 = puVar6;
              }
            } while (uVar15 <= uVar17);
LAB_00bec704:
            *puVar9 = uVar15;
          }
        }
        bVar5 = 0 < (long)uVar7;
        uVar7 = uVar7 - 1;
      } while (bVar5);
    }
    puVar12 = param_2;
    if (param_2 != param_3) {
      puVar13 = param_1 + 1;
      puVar9 = param_2;
      do {
        uVar17 = *puVar9;
        if (uVar17 < *param_1) {
          *puVar9 = *param_1;
          *param_1 = uVar17;
          if (1 < lVar8) {
            uVar15 = *puVar13;
            if ((long)param_2 - (long)param_1 == 4) {
              uVar7 = 1;
              puVar12 = puVar13;
            }
            else {
              uVar3 = param_1[2];
              bVar5 = uVar3 <= uVar15;
              if (uVar15 <= uVar3) {
                uVar15 = uVar3;
              }
              puVar12 = param_1 + 2;
              if (bVar5) {
                puVar12 = puVar13;
              }
              uVar7 = 1;
              if (!bVar5) {
                uVar7 = 2;
              }
            }
            puVar6 = param_1;
            if (uVar17 <= uVar15) {
              do {
                while( true ) {
                  puVar16 = puVar12;
                  *puVar6 = uVar15;
                  if ((long)(lVar8 - 2U >> 1) < (long)uVar7) goto LAB_00bec7f8;
                  uVar10 = uVar7 << 1 | 1;
                  uVar7 = uVar7 * 2 + 2;
                  puVar1 = param_1 + uVar10;
                  puVar6 = puVar16;
                  if ((long)uVar7 < lVar8) break;
                  uVar15 = *puVar1;
                  uVar7 = uVar10;
                  puVar12 = puVar1;
                  if (uVar15 < uVar17) goto LAB_00bec7f8;
                }
                uVar3 = *puVar1;
                uVar4 = puVar1[1];
                uVar15 = uVar3;
                if (uVar3 <= uVar4) {
                  uVar15 = uVar4;
                }
                puVar12 = puVar1 + 1;
                if (uVar4 <= uVar3) {
                  uVar7 = uVar10;
                  puVar12 = puVar1;
                }
              } while (uVar17 <= uVar15);
LAB_00bec7f8:
              *puVar16 = uVar17;
            }
          }
        }
        puVar9 = puVar9 + 1;
        puVar12 = param_3;
      } while (puVar9 != param_3);
    }
    param_3 = puVar12;
    if (1 < lVar8) {
      do {
        uVar17 = *param_1;
        uVar7 = 0;
        puVar12 = param_1;
        do {
          uVar14 = uVar7 << 1 | 1;
          uVar10 = uVar7 * 2 + 2;
          puVar13 = puVar12 + uVar7 + 1;
          if ((long)uVar10 < lVar8) {
            uVar3 = puVar12[uVar7 + 2];
            uVar4 = puVar12[uVar7 + 1];
            uVar15 = uVar4;
            if (uVar4 <= uVar3) {
              uVar15 = uVar3;
            }
            puVar9 = puVar12 + uVar7 + 2;
            uVar7 = uVar10;
            if (uVar3 <= uVar4) {
              puVar9 = puVar13;
              uVar7 = uVar14;
            }
          }
          else {
            uVar15 = *puVar13;
            puVar9 = puVar13;
            uVar7 = uVar14;
          }
          *puVar12 = uVar15;
          puVar12 = puVar9;
        } while ((long)uVar7 <= (long)(lVar8 - 2U >> 1));
        param_2 = param_2 + -1;
        if (puVar9 == param_2) {
          *puVar9 = uVar17;
        }
        else {
          lVar11 = (long)puVar9 + (2 - (long)param_1) >> 1;
          *puVar9 = *param_2;
          *param_2 = uVar17;
          if (1 < lVar11) {
            uVar7 = lVar11 - 2U >> 1;
            uVar17 = *puVar9;
            uVar15 = param_1[uVar7];
            puVar12 = param_1 + uVar7;
            if (uVar15 < uVar17) {
              do {
                puVar13 = puVar12;
                *puVar9 = uVar15;
                if (uVar7 == 0) break;
                uVar7 = uVar7 - 1 >> 1;
                uVar15 = param_1[uVar7];
                puVar9 = puVar13;
                puVar12 = param_1 + uVar7;
              } while (uVar15 < uVar17);
              *puVar13 = uVar17;
            }
          }
        }
        bVar5 = 2 < lVar8;
        lVar8 = lVar8 + -1;
      } while (bVar5);
    }
  }
  return param_3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bec6dc"></a> `00bec6dc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bec6e0"></a> `00bec6e0` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-00bec6e4"></a> `00bec6e4` | `e0 0f 00 54` | b.eq 0x00bec8e0 | `CONDITIONAL_JUMP`
<a id="insn-00bec6e8"></a> `00bec6e8` | `29 00 00 cb` | sub x9,x1,x0 | `FALL_THROUGH`
<a id="insn-00bec6ec"></a> `00bec6ec` | `28 fd 41 93` | asr x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bec6f0"></a> `00bec6f0` | `0a 09 00 f1` | subs x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bec6f4"></a> `00bec6f4` | `0b 07 00 54` | b.lt 0x00bec7d4 | `CONDITIONAL_JUMP`
<a id="insn-00bec6f8"></a> `00bec6f8` | `4b fd 41 d3` | lsr x11,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bec6fc"></a> `00bec6fc` | `ec 03 0b aa` | mov x12,x11 | `FALL_THROUGH`
<a id="insn-00bec700"></a> `00bec700` | `05 00 00 14` | b 0x00bec714 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec704"></a> `00bec704` | `0f 02 00 79` | strh w15,[x16] | `FALL_THROUGH`
<a id="insn-00bec708"></a> `00bec708` | `9f 01 00 f1` | cmp x12,#0x0 | `FALL_THROUGH`
<a id="insn-00bec70c"></a> `00bec70c` | `8c 05 00 d1` | sub x12,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00bec710"></a> `00bec710` | `2d 06 00 54` | b.le 0x00bec7d4 | `CONDITIONAL_JUMP`
<a id="insn-00bec714"></a> `00bec714` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-00bec718"></a> `00bec718` | `8b ff ff 54` | b.lt 0x00bec708 | `CONDITIONAL_JUMP`
<a id="insn-00bec71c"></a> `00bec71c` | `2e 00 80 52` | mov w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bec720"></a> `00bec720` | `8d f9 7f d3` | lsl x13,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00bec724"></a> `00bec724` | `8e f9 7f b3` | bfm x14,x12,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bec728"></a> `00bec728` | `af 09 00 91` | add x15,x13,#0x2 | `FALL_THROUGH`
<a id="insn-00bec72c"></a> `00bec72c` | `0d 04 0e 8b` | add x13,x0,x14, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00bec730"></a> `00bec730` | `ff 01 08 eb` | cmp x15,x8 | `FALL_THROUGH`
<a id="insn-00bec734"></a> `00bec734` | `2a 01 00 54` | b.ge 0x00bec758 | `CONDITIONAL_JUMP`
<a id="insn-00bec738"></a> `00bec738` | `f0 03 0d aa` | mov x16,x13 | `FALL_THROUGH`
<a id="insn-00bec73c"></a> `00bec73c` | `b1 01 40 79` | ldrh w17,[x13] | `FALL_THROUGH`
<a id="insn-00bec740"></a> `00bec740` | `03 2e 40 78` | ldrh w3,[x16, #0x2]! | `FALL_THROUGH`
<a id="insn-00bec744"></a> `00bec744` | `3f 02 03 6b` | cmp w17,w3 | `FALL_THROUGH`
<a id="insn-00bec748"></a> `00bec748` | `31 82 83 1a` | csel w17,w17,w3,hi | `FALL_THROUGH`
<a id="insn-00bec74c"></a> `00bec74c` | `0d 32 8d 9a` | csel x13,x16,x13,cc | `FALL_THROUGH`
<a id="insn-00bec750"></a> `00bec750` | `ee 31 8e 9a` | csel x14,x15,x14,cc | `FALL_THROUGH`
<a id="insn-00bec754"></a> `00bec754` | `02 00 00 14` | b 0x00bec75c | `UNCONDITIONAL_JUMP`
<a id="insn-00bec758"></a> `00bec758` | `b1 01 40 79` | ldrh w17,[x13] | `FALL_THROUGH`
<a id="insn-00bec75c"></a> `00bec75c` | `10 04 0c 8b` | add x16,x0,x12, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00bec760"></a> `00bec760` | `0f 02 40 79` | ldrh w15,[x16] | `FALL_THROUGH`
<a id="insn-00bec764"></a> `00bec764` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bec768"></a> `00bec768` | `62 01 00 54` | b.cs 0x00bec794 | `CONDITIONAL_JUMP`
<a id="insn-00bec76c"></a> `00bec76c` | `e7 ff ff 17` | b 0x00bec708 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec770"></a> `00bec770` | `e4 03 0d aa` | mov x4,x13 | `FALL_THROUGH`
<a id="insn-00bec774"></a> `00bec774` | `b1 01 40 79` | ldrh w17,[x13] | `FALL_THROUGH`
<a id="insn-00bec778"></a> `00bec778` | `85 2c 40 78` | ldrh w5,[x4, #0x2]! | `FALL_THROUGH`
<a id="insn-00bec77c"></a> `00bec77c` | `3f 02 05 6b` | cmp w17,w5 | `FALL_THROUGH`
<a id="insn-00bec780"></a> `00bec780` | `31 82 85 1a` | csel w17,w17,w5,hi | `FALL_THROUGH`
<a id="insn-00bec784"></a> `00bec784` | `8d 30 8d 9a` | csel x13,x4,x13,cc | `FALL_THROUGH`
<a id="insn-00bec788"></a> `00bec788` | `ce 31 83 9a` | csel x14,x14,x3,cc | `FALL_THROUGH`
<a id="insn-00bec78c"></a> `00bec78c` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bec790"></a> `00bec790` | `a3 fb ff 54` | b.cc 0x00bec704 | `CONDITIONAL_JUMP`
<a id="insn-00bec794"></a> `00bec794` | `7f 01 0e eb` | cmp x11,x14 | `FALL_THROUGH`
<a id="insn-00bec798"></a> `00bec798` | `11 02 00 79` | strh w17,[x16] | `FALL_THROUGH`
<a id="insn-00bec79c"></a> `00bec79c` | `f0 03 0d aa` | mov x16,x13 | `FALL_THROUGH`
<a id="insn-00bec7a0"></a> `00bec7a0` | `2b fb ff 54` | b.lt 0x00bec704 | `CONDITIONAL_JUMP`
<a id="insn-00bec7a4"></a> `00bec7a4` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bec7a8"></a> `00bec7a8` | `cd f9 7f d3` | lsl x13,x14,#0x1 | `FALL_THROUGH`
<a id="insn-00bec7ac"></a> `00bec7ac` | `c3 f9 7f b3` | bfm x3,x14,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bec7b0"></a> `00bec7b0` | `ae 09 00 91` | add x14,x13,#0x2 | `FALL_THROUGH`
<a id="insn-00bec7b4"></a> `00bec7b4` | `0d 04 03 8b` | add x13,x0,x3, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00bec7b8"></a> `00bec7b8` | `df 01 08 eb` | cmp x14,x8 | `FALL_THROUGH`
<a id="insn-00bec7bc"></a> `00bec7bc` | `ab fd ff 54` | b.lt 0x00bec770 | `CONDITIONAL_JUMP`
<a id="insn-00bec7c0"></a> `00bec7c0` | `b1 01 40 79` | ldrh w17,[x13] | `FALL_THROUGH`
<a id="insn-00bec7c4"></a> `00bec7c4` | `ee 03 03 aa` | mov x14,x3 | `FALL_THROUGH`
<a id="insn-00bec7c8"></a> `00bec7c8` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bec7cc"></a> `00bec7cc` | `42 fe ff 54` | b.cs 0x00bec794 | `CONDITIONAL_JUMP`
<a id="insn-00bec7d0"></a> `00bec7d0` | `cd ff ff 17` | b 0x00bec704 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec7d4"></a> `00bec7d4` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-00bec7d8"></a> `00bec7d8` | `e3 03 01 aa` | mov x3,x1 | `FALL_THROUGH`
<a id="insn-00bec7dc"></a> `00bec7dc` | `c0 07 00 54` | b.eq 0x00bec8d4 | `CONDITIONAL_JUMP`
<a id="insn-00bec7e0"></a> `00bec7e0` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bec7e4"></a> `00bec7e4` | `0b 08 00 91` | add x11,x0,#0x2 | `FALL_THROUGH`
<a id="insn-00bec7e8"></a> `00bec7e8` | `0c 10 00 91` | add x12,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00bec7ec"></a> `00bec7ec` | `2d 00 80 52` | mov w13,#0x1 | `FALL_THROUGH`
<a id="insn-00bec7f0"></a> `00bec7f0` | `ee 03 01 aa` | mov x14,x1 | `FALL_THROUGH`
<a id="insn-00bec7f4"></a> `00bec7f4` | `05 00 00 14` | b 0x00bec808 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec7f8"></a> `00bec7f8` | `6f 00 00 79` | strh w15,[x3] | `FALL_THROUGH`
<a id="insn-00bec7fc"></a> `00bec7fc` | `ce 09 00 91` | add x14,x14,#0x2 | `FALL_THROUGH`
<a id="insn-00bec800"></a> `00bec800` | `df 01 02 eb` | cmp x14,x2 | `FALL_THROUGH`
<a id="insn-00bec804"></a> `00bec804` | `60 06 00 54` | b.eq 0x00bec8d0 | `CONDITIONAL_JUMP`
<a id="insn-00bec808"></a> `00bec808` | `cf 01 40 79` | ldrh w15,[x14] | `FALL_THROUGH`
<a id="insn-00bec80c"></a> `00bec80c` | `10 00 40 79` | ldrh w16,[x0] | `FALL_THROUGH`
<a id="insn-00bec810"></a> `00bec810` | `ff 01 10 6b` | cmp w15,w16 | `FALL_THROUGH`
<a id="insn-00bec814"></a> `00bec814` | `42 ff ff 54` | b.cs 0x00bec7fc | `CONDITIONAL_JUMP`
<a id="insn-00bec818"></a> `00bec818` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bec81c"></a> `00bec81c` | `d0 01 00 79` | strh w16,[x14] | `FALL_THROUGH`
<a id="insn-00bec820"></a> `00bec820` | `0f 00 00 79` | strh w15,[x0] | `FALL_THROUGH`
<a id="insn-00bec824"></a> `00bec824` | `cb fe ff 54` | b.lt 0x00bec7fc | `CONDITIONAL_JUMP`
<a id="insn-00bec828"></a> `00bec828` | `71 01 40 79` | ldrh w17,[x11] | `FALL_THROUGH`
<a id="insn-00bec82c"></a> `00bec82c` | `3f 11 00 f1` | cmp x9,#0x4 | `FALL_THROUGH`
<a id="insn-00bec830"></a> `00bec830` | `c1 00 00 54` | b.ne 0x00bec848 | `CONDITIONAL_JUMP`
<a id="insn-00bec834"></a> `00bec834` | `f0 03 0b aa` | mov x16,x11 | `FALL_THROUGH`
<a id="insn-00bec838"></a> `00bec838` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-00bec83c"></a> `00bec83c` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bec840"></a> `00bec840` | `e3 fd ff 54` | b.cc 0x00bec7fc | `CONDITIONAL_JUMP`
<a id="insn-00bec844"></a> `00bec844` | `08 00 00 14` | b 0x00bec864 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec848"></a> `00bec848` | `90 01 40 79` | ldrh w16,[x12] | `FALL_THROUGH`
<a id="insn-00bec84c"></a> `00bec84c` | `3f 02 10 6b` | cmp w17,w16 | `FALL_THROUGH`
<a id="insn-00bec850"></a> `00bec850` | `31 82 90 1a` | csel w17,w17,w16,hi | `FALL_THROUGH`
<a id="insn-00bec854"></a> `00bec854` | `90 31 8b 9a` | csel x16,x12,x11,cc | `FALL_THROUGH`
<a id="insn-00bec858"></a> `00bec858` | `a4 25 8d 9a` | cinc x4,x13,cc | `FALL_THROUGH`
<a id="insn-00bec85c"></a> `00bec85c` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bec860"></a> `00bec860` | `e3 fc ff 54` | b.cc 0x00bec7fc | `CONDITIONAL_JUMP`
<a id="insn-00bec864"></a> `00bec864` | `e3 03 00 aa` | mov x3,x0 | `FALL_THROUGH`
<a id="insn-00bec868"></a> `00bec868` | `0a 00 00 14` | b 0x00bec890 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec86c"></a> `00bec86c` | `e6 03 10 aa` | mov x6,x16 | `FALL_THROUGH`
<a id="insn-00bec870"></a> `00bec870` | `11 02 40 79` | ldrh w17,[x16] | `FALL_THROUGH`
<a id="insn-00bec874"></a> `00bec874` | `c7 2c 40 78` | ldrh w7,[x6, #0x2]! | `FALL_THROUGH`
<a id="insn-00bec878"></a> `00bec878` | `3f 02 07 6b` | cmp w17,w7 | `FALL_THROUGH`
<a id="insn-00bec87c"></a> `00bec87c` | `31 82 87 1a` | csel w17,w17,w7,hi | `FALL_THROUGH`
<a id="insn-00bec880"></a> `00bec880` | `d0 30 90 9a` | csel x16,x6,x16,cc | `FALL_THROUGH`
<a id="insn-00bec884"></a> `00bec884` | `84 30 85 9a` | csel x4,x4,x5,cc | `FALL_THROUGH`
<a id="insn-00bec888"></a> `00bec888` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bec88c"></a> `00bec88c` | `63 fb ff 54` | b.cc 0x00bec7f8 | `CONDITIONAL_JUMP`
<a id="insn-00bec890"></a> `00bec890` | `5f 01 04 eb` | cmp x10,x4 | `FALL_THROUGH`
<a id="insn-00bec894"></a> `00bec894` | `71 00 00 79` | strh w17,[x3] | `FALL_THROUGH`
<a id="insn-00bec898"></a> `00bec898` | `e3 03 10 aa` | mov x3,x16 | `FALL_THROUGH`
<a id="insn-00bec89c"></a> `00bec89c` | `eb fa ff 54` | b.lt 0x00bec7f8 | `CONDITIONAL_JUMP`
<a id="insn-00bec8a0"></a> `00bec8a0` | `25 00 80 52` | mov w5,#0x1 | `FALL_THROUGH`
<a id="insn-00bec8a4"></a> `00bec8a4` | `90 f8 7f d3` | lsl x16,x4,#0x1 | `FALL_THROUGH`
<a id="insn-00bec8a8"></a> `00bec8a8` | `85 f8 7f b3` | bfm x5,x4,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bec8ac"></a> `00bec8ac` | `04 0a 00 91` | add x4,x16,#0x2 | `FALL_THROUGH`
<a id="insn-00bec8b0"></a> `00bec8b0` | `10 04 05 8b` | add x16,x0,x5, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00bec8b4"></a> `00bec8b4` | `9f 00 08 eb` | cmp x4,x8 | `FALL_THROUGH`
<a id="insn-00bec8b8"></a> `00bec8b8` | `ab fd ff 54` | b.lt 0x00bec86c | `CONDITIONAL_JUMP`
<a id="insn-00bec8bc"></a> `00bec8bc` | `11 02 40 79` | ldrh w17,[x16] | `FALL_THROUGH`
<a id="insn-00bec8c0"></a> `00bec8c0` | `e4 03 05 aa` | mov x4,x5 | `FALL_THROUGH`
<a id="insn-00bec8c4"></a> `00bec8c4` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bec8c8"></a> `00bec8c8` | `42 fe ff 54` | b.cs 0x00bec890 | `CONDITIONAL_JUMP`
<a id="insn-00bec8cc"></a> `00bec8cc` | `cb ff ff 17` | b 0x00bec7f8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec8d0"></a> `00bec8d0` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bec8d4"></a> `00bec8d4` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bec8d8"></a> `00bec8d8` | `0a 01 00 54` | b.ge 0x00bec8f8 | `CONDITIONAL_JUMP`
<a id="insn-00bec8dc"></a> `00bec8dc` | `e2 03 03 aa` | mov x2,x3 | `FALL_THROUGH`
<a id="insn-00bec8e0"></a> `00bec8e0` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bec8e4"></a> `00bec8e4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bec8e8"></a> `00bec8e8` | `2a 01 00 79` | strh w10,[x9] | `FALL_THROUGH`
<a id="insn-00bec8ec"></a> `00bec8ec` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bec8f0"></a> `00bec8f0` | `08 05 00 d1` | sub x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bec8f4"></a> `00bec8f4` | `4d ff ff 54` | b.le 0x00bec8dc | `CONDITIONAL_JUMP`
<a id="insn-00bec8f8"></a> `00bec8f8` | `09 09 00 d1` | sub x9,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bec8fc"></a> `00bec8fc` | `0a 00 40 79` | ldrh w10,[x0] | `FALL_THROUGH`
<a id="insn-00bec900"></a> `00bec900` | `ed 03 1f aa` | mov x13,xzr | `FALL_THROUGH`
<a id="insn-00bec904"></a> `00bec904` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bec908"></a> `00bec908` | `ec 03 00 aa` | mov x12,x0 | `FALL_THROUGH`
<a id="insn-00bec90c"></a> `00bec90c` | `0b 00 00 14` | b 0x00bec938 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec910"></a> `00bec910` | `2d 4e 40 78` | ldrh w13,[x17, #0x4]! | `FALL_THROUGH`
<a id="insn-00bec914"></a> `00bec914` | `2f e2 5f 78` | ldurh w15,[x17, #-0x2] | `FALL_THROUGH`
<a id="insn-00bec918"></a> `00bec918` | `ff 01 0d 6b` | cmp w15,w13 | `FALL_THROUGH`
<a id="insn-00bec91c"></a> `00bec91c` | `ef 81 8d 1a` | csel w15,w15,w13,hi | `FALL_THROUGH`
<a id="insn-00bec920"></a> `00bec920` | `29 32 89 9a` | csel x9,x17,x9,cc | `FALL_THROUGH`
<a id="insn-00bec924"></a> `00bec924` | `0d 32 8e 9a` | csel x13,x16,x14,cc | `FALL_THROUGH`
<a id="insn-00bec928"></a> `00bec928` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00bec92c"></a> `00bec92c` | `8f 01 00 79` | strh w15,[x12] | `FALL_THROUGH`
<a id="insn-00bec930"></a> `00bec930` | `ec 03 09 aa` | mov x12,x9 | `FALL_THROUGH`
<a id="insn-00bec934"></a> `00bec934` | `8c 01 00 54` | b.gt 0x00bec964 | `CONDITIONAL_JUMP`
<a id="insn-00bec938"></a> `00bec938` | `a9 f9 7f d3` | lsl x9,x13,#0x1 | `FALL_THROUGH`
<a id="insn-00bec93c"></a> `00bec93c` | `2e 00 80 52` | mov w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bec940"></a> `00bec940` | `ae f9 7f b3` | bfm x14,x13,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bec944"></a> `00bec944` | `30 09 00 91` | add x16,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bec948"></a> `00bec948` | `91 01 09 8b` | add x17,x12,x9 | `FALL_THROUGH`
<a id="insn-00bec94c"></a> `00bec94c` | `1f 02 08 eb` | cmp x16,x8 | `FALL_THROUGH`
<a id="insn-00bec950"></a> `00bec950` | `29 0a 00 91` | add x9,x17,#0x2 | `FALL_THROUGH`
<a id="insn-00bec954"></a> `00bec954` | `eb fd ff 54` | b.lt 0x00bec910 | `CONDITIONAL_JUMP`
<a id="insn-00bec958"></a> `00bec958` | `2f 01 40 79` | ldrh w15,[x9] | `FALL_THROUGH`
<a id="insn-00bec95c"></a> `00bec95c` | `ed 03 0e aa` | mov x13,x14 | `FALL_THROUGH`
<a id="insn-00bec960"></a> `00bec960` | `f2 ff ff 17` | b 0x00bec928 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec964"></a> `00bec964` | `21 08 00 d1` | sub x1,x1,#0x2 | `FALL_THROUGH`
<a id="insn-00bec968"></a> `00bec968` | `3f 01 01 eb` | cmp x9,x1 | `FALL_THROUGH`
<a id="insn-00bec96c"></a> `00bec96c` | `e0 fb ff 54` | b.eq 0x00bec8e8 | `CONDITIONAL_JUMP`
<a id="insn-00bec970"></a> `00bec970` | `2b 01 00 cb` | sub x11,x9,x0 | `FALL_THROUGH`
<a id="insn-00bec974"></a> `00bec974` | `2c 00 40 79` | ldrh w12,[x1] | `FALL_THROUGH`
<a id="insn-00bec978"></a> `00bec978` | `6b 09 00 91` | add x11,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00bec97c"></a> `00bec97c` | `6b fd 41 93` | asr x11,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00bec980"></a> `00bec980` | `2c 01 00 79` | strh w12,[x9] | `FALL_THROUGH`
<a id="insn-00bec984"></a> `00bec984` | `2a 00 00 79` | strh w10,[x1] | `FALL_THROUGH`
<a id="insn-00bec988"></a> `00bec988` | `6b 09 00 f1` | subs x11,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00bec98c"></a> `00bec98c` | `0b fb ff 54` | b.lt 0x00bec8ec | `CONDITIONAL_JUMP`
<a id="insn-00bec990"></a> `00bec990` | `6a fd 41 d3` | lsr x10,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00bec994"></a> `00bec994` | `2b 01 40 79` | ldrh w11,[x9] | `FALL_THROUGH`
<a id="insn-00bec998"></a> `00bec998` | `0c 04 0a 8b` | add x12,x0,x10, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00bec99c"></a> `00bec99c` | `8d 01 40 79` | ldrh w13,[x12] | `FALL_THROUGH`
<a id="insn-00bec9a0"></a> `00bec9a0` | `bf 01 0b 6b` | cmp w13,w11 | `FALL_THROUGH`
<a id="insn-00bec9a4"></a> `00bec9a4` | `42 fa ff 54` | b.cs 0x00bec8ec | `CONDITIONAL_JUMP`
<a id="insn-00bec9a8"></a> `00bec9a8` | `ee 03 09 aa` | mov x14,x9 | `FALL_THROUGH`
<a id="insn-00bec9ac"></a> `00bec9ac` | `e9 03 0c aa` | mov x9,x12 | `FALL_THROUGH`
<a id="insn-00bec9b0"></a> `00bec9b0` | `cd 01 00 79` | strh w13,[x14] | `FALL_THROUGH`
<a id="insn-00bec9b4"></a> `00bec9b4` | `ea 00 00 b4` | cbz x10,0x00bec9d0 | `CONDITIONAL_JUMP`
<a id="insn-00bec9b8"></a> `00bec9b8` | `4a 05 00 d1` | sub x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bec9bc"></a> `00bec9bc` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bec9c0"></a> `00bec9c0` | `0c 04 0a 8b` | add x12,x0,x10, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00bec9c4"></a> `00bec9c4` | `8d 01 40 79` | ldrh w13,[x12] | `FALL_THROUGH`
<a id="insn-00bec9c8"></a> `00bec9c8` | `bf 01 0b 6b` | cmp w13,w11 | `FALL_THROUGH`
<a id="insn-00bec9cc"></a> `00bec9cc` | `e3 fe ff 54` | b.cc 0x00bec9a8 | `CONDITIONAL_JUMP`
<a id="insn-00bec9d0"></a> `00bec9d0` | `2b 01 00 79` | strh w11,[x9] | `FALL_THROUGH`
<a id="insn-00bec9d4"></a> `00bec9d4` | `c6 ff ff 17` | b 0x00bec8ec | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bec6dc`](#insn-00bec6dc) 範囲 `[['00bec6dc', '00bec6e7']]`
  - `CONDITIONAL_JUMP` [`00bec6e4`](#insn-00bec6e4) → [`00bec8e0`](#insn-00bec8e0)
  - `FALL_THROUGH` [`00bec6e4`](#insn-00bec6e4) → [`00bec6e8`](#insn-00bec6e8)
- ブロック [`00bec6e8`](#insn-00bec6e8) 範囲 `[['00bec6e8', '00bec6f7']]`
  - `CONDITIONAL_JUMP` [`00bec6f4`](#insn-00bec6f4) → [`00bec7d4`](#insn-00bec7d4)
  - `FALL_THROUGH` [`00bec6f4`](#insn-00bec6f4) → [`00bec6f8`](#insn-00bec6f8)
- ブロック [`00bec6f8`](#insn-00bec6f8) 範囲 `[['00bec6f8', '00bec703']]`
  - `UNCONDITIONAL_JUMP` [`00bec700`](#insn-00bec700) → [`00bec714`](#insn-00bec714)
- ブロック [`00bec704`](#insn-00bec704) 範囲 `[['00bec704', '00bec707']]`
  - `FALL_THROUGH` [`00bec704`](#insn-00bec704) → [`00bec708`](#insn-00bec708)
- ブロック [`00bec708`](#insn-00bec708) 範囲 `[['00bec708', '00bec713']]`
  - `CONDITIONAL_JUMP` [`00bec710`](#insn-00bec710) → [`00bec7d4`](#insn-00bec7d4)
  - `FALL_THROUGH` [`00bec710`](#insn-00bec710) → [`00bec714`](#insn-00bec714)
- ブロック [`00bec714`](#insn-00bec714) 範囲 `[['00bec714', '00bec71b']]`
  - `CONDITIONAL_JUMP` [`00bec718`](#insn-00bec718) → [`00bec708`](#insn-00bec708)
  - `FALL_THROUGH` [`00bec718`](#insn-00bec718) → [`00bec71c`](#insn-00bec71c)
- ブロック [`00bec71c`](#insn-00bec71c) 範囲 `[['00bec71c', '00bec737']]`
  - `CONDITIONAL_JUMP` [`00bec734`](#insn-00bec734) → [`00bec758`](#insn-00bec758)
  - `FALL_THROUGH` [`00bec734`](#insn-00bec734) → [`00bec738`](#insn-00bec738)
- ブロック [`00bec738`](#insn-00bec738) 範囲 `[['00bec738', '00bec757']]`
  - `UNCONDITIONAL_JUMP` [`00bec754`](#insn-00bec754) → [`00bec75c`](#insn-00bec75c)
- ブロック [`00bec758`](#insn-00bec758) 範囲 `[['00bec758', '00bec75b']]`
  - `FALL_THROUGH` [`00bec758`](#insn-00bec758) → [`00bec75c`](#insn-00bec75c)
- ブロック [`00bec75c`](#insn-00bec75c) 範囲 `[['00bec75c', '00bec76b']]`
  - `CONDITIONAL_JUMP` [`00bec768`](#insn-00bec768) → [`00bec794`](#insn-00bec794)
  - `FALL_THROUGH` [`00bec768`](#insn-00bec768) → [`00bec76c`](#insn-00bec76c)
- ブロック [`00bec76c`](#insn-00bec76c) 範囲 `[['00bec76c', '00bec76f']]`
  - `UNCONDITIONAL_JUMP` [`00bec76c`](#insn-00bec76c) → [`00bec708`](#insn-00bec708)
- ブロック [`00bec770`](#insn-00bec770) 範囲 `[['00bec770', '00bec793']]`
  - `CONDITIONAL_JUMP` [`00bec790`](#insn-00bec790) → [`00bec704`](#insn-00bec704)
  - `FALL_THROUGH` [`00bec790`](#insn-00bec790) → [`00bec794`](#insn-00bec794)
- ブロック [`00bec794`](#insn-00bec794) 範囲 `[['00bec794', '00bec7a3']]`
  - `CONDITIONAL_JUMP` [`00bec7a0`](#insn-00bec7a0) → [`00bec704`](#insn-00bec704)
  - `FALL_THROUGH` [`00bec7a0`](#insn-00bec7a0) → [`00bec7a4`](#insn-00bec7a4)
- ブロック [`00bec7a4`](#insn-00bec7a4) 範囲 `[['00bec7a4', '00bec7bf']]`
  - `CONDITIONAL_JUMP` [`00bec7bc`](#insn-00bec7bc) → [`00bec770`](#insn-00bec770)
  - `FALL_THROUGH` [`00bec7bc`](#insn-00bec7bc) → [`00bec7c0`](#insn-00bec7c0)
- ブロック [`00bec7c0`](#insn-00bec7c0) 範囲 `[['00bec7c0', '00bec7cf']]`
  - `CONDITIONAL_JUMP` [`00bec7cc`](#insn-00bec7cc) → [`00bec794`](#insn-00bec794)
  - `FALL_THROUGH` [`00bec7cc`](#insn-00bec7cc) → [`00bec7d0`](#insn-00bec7d0)
- ブロック [`00bec7d0`](#insn-00bec7d0) 範囲 `[['00bec7d0', '00bec7d3']]`
  - `UNCONDITIONAL_JUMP` [`00bec7d0`](#insn-00bec7d0) → [`00bec704`](#insn-00bec704)
- ブロック [`00bec7d4`](#insn-00bec7d4) 範囲 `[['00bec7d4', '00bec7df']]`
  - `CONDITIONAL_JUMP` [`00bec7dc`](#insn-00bec7dc) → [`00bec8d4`](#insn-00bec8d4)
  - `FALL_THROUGH` [`00bec7dc`](#insn-00bec7dc) → [`00bec7e0`](#insn-00bec7e0)
- ブロック [`00bec7e0`](#insn-00bec7e0) 範囲 `[['00bec7e0', '00bec7f7']]`
  - `UNCONDITIONAL_JUMP` [`00bec7f4`](#insn-00bec7f4) → [`00bec808`](#insn-00bec808)
- ブロック [`00bec7f8`](#insn-00bec7f8) 範囲 `[['00bec7f8', '00bec7fb']]`
  - `FALL_THROUGH` [`00bec7f8`](#insn-00bec7f8) → [`00bec7fc`](#insn-00bec7fc)
- ブロック [`00bec7fc`](#insn-00bec7fc) 範囲 `[['00bec7fc', '00bec807']]`
  - `CONDITIONAL_JUMP` [`00bec804`](#insn-00bec804) → [`00bec8d0`](#insn-00bec8d0)
  - `FALL_THROUGH` [`00bec804`](#insn-00bec804) → [`00bec808`](#insn-00bec808)
- ブロック [`00bec808`](#insn-00bec808) 範囲 `[['00bec808', '00bec817']]`
  - `CONDITIONAL_JUMP` [`00bec814`](#insn-00bec814) → [`00bec7fc`](#insn-00bec7fc)
  - `FALL_THROUGH` [`00bec814`](#insn-00bec814) → [`00bec818`](#insn-00bec818)
- ブロック [`00bec818`](#insn-00bec818) 範囲 `[['00bec818', '00bec827']]`
  - `CONDITIONAL_JUMP` [`00bec824`](#insn-00bec824) → [`00bec7fc`](#insn-00bec7fc)
  - `FALL_THROUGH` [`00bec824`](#insn-00bec824) → [`00bec828`](#insn-00bec828)
- ブロック [`00bec828`](#insn-00bec828) 範囲 `[['00bec828', '00bec833']]`
  - `CONDITIONAL_JUMP` [`00bec830`](#insn-00bec830) → [`00bec848`](#insn-00bec848)
  - `FALL_THROUGH` [`00bec830`](#insn-00bec830) → [`00bec834`](#insn-00bec834)
- ブロック [`00bec834`](#insn-00bec834) 範囲 `[['00bec834', '00bec843']]`
  - `CONDITIONAL_JUMP` [`00bec840`](#insn-00bec840) → [`00bec7fc`](#insn-00bec7fc)
  - `FALL_THROUGH` [`00bec840`](#insn-00bec840) → [`00bec844`](#insn-00bec844)
- ブロック [`00bec844`](#insn-00bec844) 範囲 `[['00bec844', '00bec847']]`
  - `UNCONDITIONAL_JUMP` [`00bec844`](#insn-00bec844) → [`00bec864`](#insn-00bec864)
- ブロック [`00bec848`](#insn-00bec848) 範囲 `[['00bec848', '00bec863']]`
  - `CONDITIONAL_JUMP` [`00bec860`](#insn-00bec860) → [`00bec7fc`](#insn-00bec7fc)
  - `FALL_THROUGH` [`00bec860`](#insn-00bec860) → [`00bec864`](#insn-00bec864)
- ブロック [`00bec864`](#insn-00bec864) 範囲 `[['00bec864', '00bec86b']]`
  - `UNCONDITIONAL_JUMP` [`00bec868`](#insn-00bec868) → [`00bec890`](#insn-00bec890)
- ブロック [`00bec86c`](#insn-00bec86c) 範囲 `[['00bec86c', '00bec88f']]`
  - `CONDITIONAL_JUMP` [`00bec88c`](#insn-00bec88c) → [`00bec7f8`](#insn-00bec7f8)
  - `FALL_THROUGH` [`00bec88c`](#insn-00bec88c) → [`00bec890`](#insn-00bec890)
- ブロック [`00bec890`](#insn-00bec890) 範囲 `[['00bec890', '00bec89f']]`
  - `CONDITIONAL_JUMP` [`00bec89c`](#insn-00bec89c) → [`00bec7f8`](#insn-00bec7f8)
  - `FALL_THROUGH` [`00bec89c`](#insn-00bec89c) → [`00bec8a0`](#insn-00bec8a0)
- ブロック [`00bec8a0`](#insn-00bec8a0) 範囲 `[['00bec8a0', '00bec8bb']]`
  - `CONDITIONAL_JUMP` [`00bec8b8`](#insn-00bec8b8) → [`00bec86c`](#insn-00bec86c)
  - `FALL_THROUGH` [`00bec8b8`](#insn-00bec8b8) → [`00bec8bc`](#insn-00bec8bc)
- ブロック [`00bec8bc`](#insn-00bec8bc) 範囲 `[['00bec8bc', '00bec8cb']]`
  - `CONDITIONAL_JUMP` [`00bec8c8`](#insn-00bec8c8) → [`00bec890`](#insn-00bec890)
  - `FALL_THROUGH` [`00bec8c8`](#insn-00bec8c8) → [`00bec8cc`](#insn-00bec8cc)
- ブロック [`00bec8cc`](#insn-00bec8cc) 範囲 `[['00bec8cc', '00bec8cf']]`
  - `UNCONDITIONAL_JUMP` [`00bec8cc`](#insn-00bec8cc) → [`00bec7f8`](#insn-00bec7f8)
- ブロック [`00bec8d0`](#insn-00bec8d0) 範囲 `[['00bec8d0', '00bec8d3']]`
  - `FALL_THROUGH` [`00bec8d0`](#insn-00bec8d0) → [`00bec8d4`](#insn-00bec8d4)
- ブロック [`00bec8d4`](#insn-00bec8d4) 範囲 `[['00bec8d4', '00bec8db']]`
  - `CONDITIONAL_JUMP` [`00bec8d8`](#insn-00bec8d8) → [`00bec8f8`](#insn-00bec8f8)
  - `FALL_THROUGH` [`00bec8d8`](#insn-00bec8d8) → [`00bec8dc`](#insn-00bec8dc)
- ブロック [`00bec8dc`](#insn-00bec8dc) 範囲 `[['00bec8dc', '00bec8df']]`
  - `FALL_THROUGH` [`00bec8dc`](#insn-00bec8dc) → [`00bec8e0`](#insn-00bec8e0)
- ブロック [`00bec8e0`](#insn-00bec8e0) 範囲 `[['00bec8e0', '00bec8e7']]`
- ブロック [`00bec8e8`](#insn-00bec8e8) 範囲 `[['00bec8e8', '00bec8eb']]`
  - `FALL_THROUGH` [`00bec8e8`](#insn-00bec8e8) → [`00bec8ec`](#insn-00bec8ec)
- ブロック [`00bec8ec`](#insn-00bec8ec) 範囲 `[['00bec8ec', '00bec8f7']]`
  - `CONDITIONAL_JUMP` [`00bec8f4`](#insn-00bec8f4) → [`00bec8dc`](#insn-00bec8dc)
  - `FALL_THROUGH` [`00bec8f4`](#insn-00bec8f4) → [`00bec8f8`](#insn-00bec8f8)
- ブロック [`00bec8f8`](#insn-00bec8f8) 範囲 `[['00bec8f8', '00bec90f']]`
  - `UNCONDITIONAL_JUMP` [`00bec90c`](#insn-00bec90c) → [`00bec938`](#insn-00bec938)
- ブロック [`00bec910`](#insn-00bec910) 範囲 `[['00bec910', '00bec927']]`
  - `FALL_THROUGH` [`00bec924`](#insn-00bec924) → [`00bec928`](#insn-00bec928)
- ブロック [`00bec928`](#insn-00bec928) 範囲 `[['00bec928', '00bec937']]`
  - `CONDITIONAL_JUMP` [`00bec934`](#insn-00bec934) → [`00bec964`](#insn-00bec964)
  - `FALL_THROUGH` [`00bec934`](#insn-00bec934) → [`00bec938`](#insn-00bec938)
- ブロック [`00bec938`](#insn-00bec938) 範囲 `[['00bec938', '00bec957']]`
  - `CONDITIONAL_JUMP` [`00bec954`](#insn-00bec954) → [`00bec910`](#insn-00bec910)
  - `FALL_THROUGH` [`00bec954`](#insn-00bec954) → [`00bec958`](#insn-00bec958)
- ブロック [`00bec958`](#insn-00bec958) 範囲 `[['00bec958', '00bec963']]`
  - `UNCONDITIONAL_JUMP` [`00bec960`](#insn-00bec960) → [`00bec928`](#insn-00bec928)
- ブロック [`00bec964`](#insn-00bec964) 範囲 `[['00bec964', '00bec96f']]`
  - `CONDITIONAL_JUMP` [`00bec96c`](#insn-00bec96c) → [`00bec8e8`](#insn-00bec8e8)
  - `FALL_THROUGH` [`00bec96c`](#insn-00bec96c) → [`00bec970`](#insn-00bec970)
- ブロック [`00bec970`](#insn-00bec970) 範囲 `[['00bec970', '00bec98f']]`
  - `CONDITIONAL_JUMP` [`00bec98c`](#insn-00bec98c) → [`00bec8ec`](#insn-00bec8ec)
  - `FALL_THROUGH` [`00bec98c`](#insn-00bec98c) → [`00bec990`](#insn-00bec990)
- ブロック [`00bec990`](#insn-00bec990) 範囲 `[['00bec990', '00bec9a7']]`
  - `CONDITIONAL_JUMP` [`00bec9a4`](#insn-00bec9a4) → [`00bec8ec`](#insn-00bec8ec)
  - `FALL_THROUGH` [`00bec9a4`](#insn-00bec9a4) → [`00bec9a8`](#insn-00bec9a8)
- ブロック [`00bec9a8`](#insn-00bec9a8) 範囲 `[['00bec9a8', '00bec9b7']]`
  - `CONDITIONAL_JUMP` [`00bec9b4`](#insn-00bec9b4) → [`00bec9d0`](#insn-00bec9d0)
  - `FALL_THROUGH` [`00bec9b4`](#insn-00bec9b4) → [`00bec9b8`](#insn-00bec9b8)
- ブロック [`00bec9b8`](#insn-00bec9b8) 範囲 `[['00bec9b8', '00bec9cf']]`
  - `CONDITIONAL_JUMP` [`00bec9cc`](#insn-00bec9cc) → [`00bec9a8`](#insn-00bec9a8)
  - `FALL_THROUGH` [`00bec9cc`](#insn-00bec9cc) → [`00bec9d0`](#insn-00bec9d0)
- ブロック [`00bec9d0`](#insn-00bec9d0) 範囲 `[['00bec9d0', '00bec9d7']]`
  - `UNCONDITIONAL_JUMP` [`00bec9d4`](#insn-00bec9d4) → [`00bec8ec`](#insn-00bec8ec)

## 命令位置別の参照

- [`00bec6e4`](#insn-00bec6e4) → [`00bec8e0`](#insn-00bec8e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec6f4`](#insn-00bec6f4) → [`00bec7d4`](#insn-00bec7d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec700`](#insn-00bec700) → [`00bec714`](#insn-00bec714) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec710`](#insn-00bec710) → [`00bec7d4`](#insn-00bec7d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec718`](#insn-00bec718) → [`00bec708`](#insn-00bec708) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec734`](#insn-00bec734) → [`00bec758`](#insn-00bec758) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec754`](#insn-00bec754) → [`00bec75c`](#insn-00bec75c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec768`](#insn-00bec768) → [`00bec794`](#insn-00bec794) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec76c`](#insn-00bec76c) → [`00bec708`](#insn-00bec708) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec790`](#insn-00bec790) → [`00bec704`](#insn-00bec704) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec7a0`](#insn-00bec7a0) → [`00bec704`](#insn-00bec704) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec7bc`](#insn-00bec7bc) → [`00bec770`](#insn-00bec770) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec7cc`](#insn-00bec7cc) → [`00bec794`](#insn-00bec794) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec7d0`](#insn-00bec7d0) → [`00bec704`](#insn-00bec704) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec7dc`](#insn-00bec7dc) → [`00bec8d4`](#insn-00bec8d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec7f4`](#insn-00bec7f4) → [`00bec808`](#insn-00bec808) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec804`](#insn-00bec804) → [`00bec8d0`](#insn-00bec8d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec814`](#insn-00bec814) → [`00bec7fc`](#insn-00bec7fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec824`](#insn-00bec824) → [`00bec7fc`](#insn-00bec7fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec830`](#insn-00bec830) → [`00bec848`](#insn-00bec848) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec840`](#insn-00bec840) → [`00bec7fc`](#insn-00bec7fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec844`](#insn-00bec844) → [`00bec864`](#insn-00bec864) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec860`](#insn-00bec860) → [`00bec7fc`](#insn-00bec7fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec868`](#insn-00bec868) → [`00bec890`](#insn-00bec890) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec88c`](#insn-00bec88c) → [`00bec7f8`](#insn-00bec7f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec89c`](#insn-00bec89c) → [`00bec7f8`](#insn-00bec7f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec8b8`](#insn-00bec8b8) → [`00bec86c`](#insn-00bec86c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec8c8`](#insn-00bec8c8) → [`00bec890`](#insn-00bec890) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec8cc`](#insn-00bec8cc) → [`00bec7f8`](#insn-00bec7f8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec8d8`](#insn-00bec8d8) → [`00bec8f8`](#insn-00bec8f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec8f4`](#insn-00bec8f4) → [`00bec8dc`](#insn-00bec8dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec90c`](#insn-00bec90c) → [`00bec938`](#insn-00bec938) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec934`](#insn-00bec934) → [`00bec964`](#insn-00bec964) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec954`](#insn-00bec954) → [`00bec910`](#insn-00bec910) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec960`](#insn-00bec960) → [`00bec928`](#insn-00bec928) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec96c`](#insn-00bec96c) → [`00bec8e8`](#insn-00bec8e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec98c`](#insn-00bec98c) → [`00bec8ec`](#insn-00bec8ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec9a4`](#insn-00bec9a4) → [`00bec8ec`](#insn-00bec8ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec9b4`](#insn-00bec9b4) → [`00bec9d0`](#insn-00bec9d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec9cc`](#insn-00bec9cc) → [`00bec9a8`](#insn-00bec9a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec9d4`](#insn-00bec9d4) → [`00bec8ec`](#insn-00bec8ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bec6e4`](#insn-00bec6e4)

~~~json
{
  "source": "00bec6e4",
  "target": "00bec8e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec6f4`](#insn-00bec6f4)

~~~json
{
  "source": "00bec6f4",
  "target": "00bec7d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec700`](#insn-00bec700)

~~~json
{
  "source": "00bec700",
  "target": "00bec714",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec710`](#insn-00bec710)

~~~json
{
  "source": "00bec710",
  "target": "00bec7d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec718`](#insn-00bec718)

~~~json
{
  "source": "00bec718",
  "target": "00bec708",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec734`](#insn-00bec734)

~~~json
{
  "source": "00bec734",
  "target": "00bec758",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec754`](#insn-00bec754)

~~~json
{
  "source": "00bec754",
  "target": "00bec75c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec768`](#insn-00bec768)

~~~json
{
  "source": "00bec768",
  "target": "00bec794",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec76c`](#insn-00bec76c)

~~~json
{
  "source": "00bec76c",
  "target": "00bec708",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec790`](#insn-00bec790)

~~~json
{
  "source": "00bec790",
  "target": "00bec704",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec7a0`](#insn-00bec7a0)

~~~json
{
  "source": "00bec7a0",
  "target": "00bec704",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec7bc`](#insn-00bec7bc)

~~~json
{
  "source": "00bec7bc",
  "target": "00bec770",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec7cc`](#insn-00bec7cc)

~~~json
{
  "source": "00bec7cc",
  "target": "00bec794",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec7d0`](#insn-00bec7d0)

~~~json
{
  "source": "00bec7d0",
  "target": "00bec704",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec7dc`](#insn-00bec7dc)

~~~json
{
  "source": "00bec7dc",
  "target": "00bec8d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec7f4`](#insn-00bec7f4)

~~~json
{
  "source": "00bec7f4",
  "target": "00bec808",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec804`](#insn-00bec804)

~~~json
{
  "source": "00bec804",
  "target": "00bec8d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec814`](#insn-00bec814)

~~~json
{
  "source": "00bec814",
  "target": "00bec7fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec824`](#insn-00bec824)

~~~json
{
  "source": "00bec824",
  "target": "00bec7fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec830`](#insn-00bec830)

~~~json
{
  "source": "00bec830",
  "target": "00bec848",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec840`](#insn-00bec840)

~~~json
{
  "source": "00bec840",
  "target": "00bec7fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec844`](#insn-00bec844)

~~~json
{
  "source": "00bec844",
  "target": "00bec864",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec860`](#insn-00bec860)

~~~json
{
  "source": "00bec860",
  "target": "00bec7fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec868`](#insn-00bec868)

~~~json
{
  "source": "00bec868",
  "target": "00bec890",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec88c`](#insn-00bec88c)

~~~json
{
  "source": "00bec88c",
  "target": "00bec7f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec89c`](#insn-00bec89c)

~~~json
{
  "source": "00bec89c",
  "target": "00bec7f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec8b8`](#insn-00bec8b8)

~~~json
{
  "source": "00bec8b8",
  "target": "00bec86c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec8c8`](#insn-00bec8c8)

~~~json
{
  "source": "00bec8c8",
  "target": "00bec890",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec8cc`](#insn-00bec8cc)

~~~json
{
  "source": "00bec8cc",
  "target": "00bec7f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec8d8`](#insn-00bec8d8)

~~~json
{
  "source": "00bec8d8",
  "target": "00bec8f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec8f4`](#insn-00bec8f4)

~~~json
{
  "source": "00bec8f4",
  "target": "00bec8dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec90c`](#insn-00bec90c)

~~~json
{
  "source": "00bec90c",
  "target": "00bec938",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec934`](#insn-00bec934)

~~~json
{
  "source": "00bec934",
  "target": "00bec964",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec954`](#insn-00bec954)

~~~json
{
  "source": "00bec954",
  "target": "00bec910",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec960`](#insn-00bec960)

~~~json
{
  "source": "00bec960",
  "target": "00bec928",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec96c`](#insn-00bec96c)

~~~json
{
  "source": "00bec96c",
  "target": "00bec8e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec98c`](#insn-00bec98c)

~~~json
{
  "source": "00bec98c",
  "target": "00bec8ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec9a4`](#insn-00bec9a4)

~~~json
{
  "source": "00bec9a4",
  "target": "00bec8ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec9b4`](#insn-00bec9b4)

~~~json
{
  "source": "00bec9b4",
  "target": "00bec9d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec9cc`](#insn-00bec9cc)

~~~json
{
  "source": "00bec9cc",
  "target": "00bec9a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec9d4`](#insn-00bec9d4)

~~~json
{
  "source": "00bec9d4",
  "target": "00bec8ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
