# 00befcd8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00beece4`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00beece4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/no_difference_in_scope-0014.md#compare-b67d7f89b3002693c0e2793085cbed1f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00befcd8",
  "name": "FUN_00befcd8",
  "size": 728,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4066c7fca1553ea07b4ebdc6ed7d2cd74bac00463506fce16f7b38ddc8142d69",
  "source_text_sha256": "4066c7fca1553ea07b4ebdc6ed7d2cd74bac00463506fce16f7b38ddc8142d69",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00befcd8",
        "00beffaf"
      ]
    ],
    "bytes_sha256": "6f795c93e7d7a4fc5aedae5bd8a4f38974442a7c2fe67b53a7a890bf03ccece4",
    "instruction_count": 182,
    "instruction_bytes": 728,
    "body_bytes": 728,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be8fd0](../00be8/00be8fd0.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4728 bytes

~~~c

double * FUN_00befcd8(double *param_1,double *param_2,double *param_3)

{
  bool bVar1;
  ulong uVar2;
  long lVar3;
  double *pdVar4;
  double *pdVar5;
  long lVar6;
  ulong uVar7;
  ulong uVar8;
  ulong uVar9;
  ulong uVar10;
  double *pdVar11;
  double *pdVar12;
  double dVar13;
  double dVar14;
  
  if (param_1 != param_2) {
    lVar3 = (long)param_2 - (long)param_1 >> 3;
    if (1 < lVar3) {
      uVar7 = lVar3 - 2U >> 1;
      uVar10 = uVar7;
      do {
        if ((long)uVar10 <= (long)uVar7) {
          uVar9 = (uVar10 & 0x1fffffffffffffff) << 1 | 1;
          uVar8 = (uVar10 & 0x1fffffffffffffff) * 2 + 2;
          pdVar5 = param_1 + uVar9;
          if (((long)uVar8 < lVar3) && (*pdVar5 < pdVar5[1])) {
            uVar9 = uVar8;
            pdVar5 = pdVar5 + 1;
          }
          dVar14 = *pdVar5;
          dVar13 = param_1[uVar10];
          pdVar4 = param_1 + uVar10;
          if (dVar13 <= dVar14) {
            do {
              pdVar12 = pdVar5;
              *pdVar4 = dVar14;
              if ((long)uVar7 < (long)uVar9) break;
              uVar2 = uVar9 << 1 | 1;
              uVar8 = uVar9 * 2 + 2;
              pdVar5 = param_1 + uVar2;
              uVar9 = uVar2;
              if (((long)uVar8 < lVar3) && (*pdVar5 < pdVar5[1])) {
                uVar9 = uVar8;
                pdVar5 = pdVar5 + 1;
              }
              dVar14 = *pdVar5;
              pdVar4 = pdVar12;
            } while (dVar13 <= dVar14);
            *pdVar12 = dVar13;
          }
        }
        bVar1 = 0 < (long)uVar10;
        uVar10 = uVar10 - 1;
      } while (bVar1);
    }
    pdVar5 = param_2;
    if (param_2 != param_3) {
      pdVar4 = param_2;
      do {
        dVar13 = *pdVar4;
        if (dVar13 < *param_1) {
          *pdVar4 = *param_1;
          *param_1 = dVar13;
          if (1 < lVar3) {
            if (((long)param_2 - (long)param_1 == 0x10) || (param_1[2] <= param_1[1])) {
              uVar10 = 1;
              pdVar5 = param_1 + 1;
            }
            else {
              uVar10 = 2;
              pdVar5 = param_1 + 2;
            }
            dVar14 = *pdVar5;
            pdVar12 = param_1;
            if (dVar13 <= dVar14) {
              do {
                pdVar11 = pdVar5;
                *pdVar12 = dVar14;
                if ((long)(lVar3 - 2U >> 1) < (long)uVar10) break;
                uVar8 = uVar10 << 1 | 1;
                uVar7 = uVar10 * 2 + 2;
                pdVar5 = param_1 + uVar8;
                uVar10 = uVar8;
                if (((long)uVar7 < lVar3) && (*pdVar5 < pdVar5[1])) {
                  uVar10 = uVar7;
                  pdVar5 = pdVar5 + 1;
                }
                dVar14 = *pdVar5;
                pdVar12 = pdVar11;
              } while (dVar13 <= dVar14);
              *pdVar11 = dVar13;
            }
          }
        }
        pdVar4 = pdVar4 + 1;
        pdVar5 = param_3;
      } while (pdVar4 != param_3);
    }
    param_3 = pdVar5;
    if (1 < lVar3) {
      do {
        dVar13 = *param_1;
        pdVar5 = param_1;
        uVar10 = 0;
        do {
          uVar8 = uVar10 << 1 | 1;
          uVar7 = uVar10 * 2 + 2;
          pdVar4 = pdVar5 + uVar10 + 1;
          if (((long)uVar7 < lVar3) && (pdVar5[uVar10 + 1] < pdVar5[uVar10 + 2])) {
            pdVar4 = pdVar5 + uVar10 + 2;
            uVar8 = uVar7;
          }
          *pdVar5 = *pdVar4;
          pdVar5 = pdVar4;
          uVar10 = uVar8;
        } while ((long)uVar8 <= (long)(lVar3 - 2U >> 1));
        param_2 = param_2 + -1;
        if (pdVar4 == param_2) {
LAB_00befec8:
          *pdVar4 = dVar13;
        }
        else {
          lVar6 = (long)pdVar4 + (8 - (long)param_1) >> 3;
          *pdVar4 = *param_2;
          *param_2 = dVar13;
          if (1 < lVar6) {
            uVar10 = lVar6 - 2U >> 1;
            dVar13 = *pdVar4;
            dVar14 = param_1[uVar10];
            pdVar12 = param_1 + uVar10;
            if (dVar14 < dVar13) {
              do {
                pdVar4 = pdVar12;
                    /* try { // try from 00beff88 to 00cf0023 has its CatchHandler @ 00beff88
                       catch() { ... } // from try @ 00beff88 with catch @ 00beff88
                       catch() { ... } // from try @ 00bf0030 with catch @ 00beff88 */
                *pdVar5 = dVar14;
                if (uVar10 == 0) break;
                uVar10 = uVar10 - 1 >> 1;
                dVar14 = param_1[uVar10];
                pdVar5 = pdVar4;
                pdVar12 = param_1 + uVar10;
              } while (dVar14 < dVar13);
              goto LAB_00befec8;
            }
          }
        }
        bVar1 = 2 < lVar3;
        lVar3 = lVar3 + -1;
      } while (bVar1);
    }
  }
  return param_3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00befcd8"></a> `00befcd8` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00befcdc"></a> `00befcdc` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-00befce0"></a> `00befce0` | `00 0f 00 54` | b.eq 0x00befec0 | `CONDITIONAL_JUMP`
<a id="insn-00befce4"></a> `00befce4` | `29 00 00 cb` | sub x9,x1,x0 | `FALL_THROUGH`
<a id="insn-00befce8"></a> `00befce8` | `28 fd 43 93` | asr x8,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00befcec"></a> `00befcec` | `0a 09 00 f1` | subs x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00befcf0"></a> `00befcf0` | `ab 06 00 54` | b.lt 0x00befdc4 | `CONDITIONAL_JUMP`
<a id="insn-00befcf4"></a> `00befcf4` | `4b fd 41 d3` | lsr x11,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00befcf8"></a> `00befcf8` | `ec 03 0b aa` | mov x12,x11 | `FALL_THROUGH`
<a id="insn-00befcfc"></a> `00befcfc` | `05 00 00 14` | b 0x00befd10 | `UNCONDITIONAL_JUMP`
<a id="insn-00befd00"></a> `00befd00` | `e0 01 00 fd` | str d0,[x15] | `FALL_THROUGH`
<a id="insn-00befd04"></a> `00befd04` | `9f 01 00 f1` | cmp x12,#0x0 | `FALL_THROUGH`
<a id="insn-00befd08"></a> `00befd08` | `8c 05 00 d1` | sub x12,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00befd0c"></a> `00befd0c` | `cd 05 00 54` | b.le 0x00befdc4 | `CONDITIONAL_JUMP`
<a id="insn-00befd10"></a> `00befd10` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-00befd14"></a> `00befd14` | `8b ff ff 54` | b.lt 0x00befd04 | `CONDITIONAL_JUMP`
<a id="insn-00befd18"></a> `00befd18` | `2d 00 80 52` | mov w13,#0x1 | `FALL_THROUGH`
<a id="insn-00befd1c"></a> `00befd1c` | `8e f1 7f d3` | ubfiz x14,x12,#0x1,#0x3d | `FALL_THROUGH`
<a id="insn-00befd20"></a> `00befd20` | `8d f1 7f b3` | bfm x13,x12,#0x3f,#0x3c | `FALL_THROUGH`
<a id="insn-00befd24"></a> `00befd24` | `cf 09 00 91` | add x15,x14,#0x2 | `FALL_THROUGH`
<a id="insn-00befd28"></a> `00befd28` | `0e 0c 0d 8b` | add x14,x0,x13, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00befd2c"></a> `00befd2c` | `ff 01 08 eb` | cmp x15,x8 | `FALL_THROUGH`
<a id="insn-00befd30"></a> `00befd30` | `0a 01 00 54` | b.ge 0x00befd50 | `CONDITIONAL_JUMP`
<a id="insn-00befd34"></a> `00befd34` | `f0 03 0e aa` | mov x16,x14 | `FALL_THROUGH`
<a id="insn-00befd38"></a> `00befd38` | `c1 01 40 fd` | ldr d1,[x14] | `FALL_THROUGH`
<a id="insn-00befd3c"></a> `00befd3c` | `00 8e 40 fc` | ldr d0,[x16, #0x8]! | `FALL_THROUGH`
<a id="insn-00befd40"></a> `00befd40` | `20 20 60 1e` | fcmp d1,d0 | `FALL_THROUGH`
<a id="insn-00befd44"></a> `00befd44` | `65 00 00 54` | b.pl 0x00befd50 | `CONDITIONAL_JUMP`
<a id="insn-00befd48"></a> `00befd48` | `ee 03 10 aa` | mov x14,x16 | `FALL_THROUGH`
<a id="insn-00befd4c"></a> `00befd4c` | `ed 03 0f aa` | mov x13,x15 | `FALL_THROUGH`
<a id="insn-00befd50"></a> `00befd50` | `0f 0c 0c 8b` | add x15,x0,x12, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00befd54"></a> `00befd54` | `c1 01 40 fd` | ldr d1,[x14] | `FALL_THROUGH`
<a id="insn-00befd58"></a> `00befd58` | `e0 01 40 fd` | ldr d0,[x15] | `FALL_THROUGH`
<a id="insn-00befd5c"></a> `00befd5c` | `20 20 60 1e` | fcmp d1,d0 | `FALL_THROUGH`
<a id="insn-00befd60"></a> `00befd60` | `a5 00 00 54` | b.pl 0x00befd74 | `CONDITIONAL_JUMP`
<a id="insn-00befd64"></a> `00befd64` | `e8 ff ff 17` | b 0x00befd04 | `UNCONDITIONAL_JUMP`
<a id="insn-00befd68"></a> `00befd68` | `c1 01 40 fd` | ldr d1,[x14] | `FALL_THROUGH`
<a id="insn-00befd6c"></a> `00befd6c` | `20 20 60 1e` | fcmp d1,d0 | `FALL_THROUGH`
<a id="insn-00befd70"></a> `00befd70` | `84 fc ff 54` | b.mi 0x00befd00 | `CONDITIONAL_JUMP`
<a id="insn-00befd74"></a> `00befd74` | `7f 01 0d eb` | cmp x11,x13 | `FALL_THROUGH`
<a id="insn-00befd78"></a> `00befd78` | `e1 01 00 fd` | str d1,[x15] | `FALL_THROUGH`
<a id="insn-00befd7c"></a> `00befd7c` | `ef 03 0e aa` | mov x15,x14 | `FALL_THROUGH`
<a id="insn-00befd80"></a> `00befd80` | `0b fc ff 54` | b.lt 0x00befd00 | `CONDITIONAL_JUMP`
<a id="insn-00befd84"></a> `00befd84` | `31 00 80 52` | mov w17,#0x1 | `FALL_THROUGH`
<a id="insn-00befd88"></a> `00befd88` | `ae f9 7f d3` | lsl x14,x13,#0x1 | `FALL_THROUGH`
<a id="insn-00befd8c"></a> `00befd8c` | `b1 f9 7f b3` | bfm x17,x13,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00befd90"></a> `00befd90` | `d0 09 00 91` | add x16,x14,#0x2 | `FALL_THROUGH`
<a id="insn-00befd94"></a> `00befd94` | `0e 0c 11 8b` | add x14,x0,x17, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00befd98"></a> `00befd98` | `1f 02 08 eb` | cmp x16,x8 | `FALL_THROUGH`
<a id="insn-00befd9c"></a> `00befd9c` | `ed 03 11 aa` | mov x13,x17 | `FALL_THROUGH`
<a id="insn-00befda0"></a> `00befda0` | `4a fe ff 54` | b.ge 0x00befd68 | `CONDITIONAL_JUMP`
<a id="insn-00befda4"></a> `00befda4` | `f1 03 0e aa` | mov x17,x14 | `FALL_THROUGH`
<a id="insn-00befda8"></a> `00befda8` | `c2 01 40 fd` | ldr d2,[x14] | `FALL_THROUGH`
<a id="insn-00befdac"></a> `00befdac` | `21 8e 40 fc` | ldr d1,[x17, #0x8]! | `FALL_THROUGH`
<a id="insn-00befdb0"></a> `00befdb0` | `40 20 61 1e` | fcmp d2,d1 | `FALL_THROUGH`
<a id="insn-00befdb4"></a> `00befdb4` | `a5 fd ff 54` | b.pl 0x00befd68 | `CONDITIONAL_JUMP`
<a id="insn-00befdb8"></a> `00befdb8` | `ee 03 11 aa` | mov x14,x17 | `FALL_THROUGH`
<a id="insn-00befdbc"></a> `00befdbc` | `ed 03 10 aa` | mov x13,x16 | `FALL_THROUGH`
<a id="insn-00befdc0"></a> `00befdc0` | `ea ff ff 17` | b 0x00befd68 | `UNCONDITIONAL_JUMP`
<a id="insn-00befdc4"></a> `00befdc4` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-00befdc8"></a> `00befdc8` | `e3 03 01 aa` | mov x3,x1 | `FALL_THROUGH`
<a id="insn-00befdcc"></a> `00befdcc` | `40 07 00 54` | b.eq 0x00befeb4 | `CONDITIONAL_JUMP`
<a id="insn-00befdd0"></a> `00befdd0` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00befdd4"></a> `00befdd4` | `0b 20 00 91` | add x11,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00befdd8"></a> `00befdd8` | `0c 40 00 91` | add x12,x0,#0x10 | `FALL_THROUGH`
<a id="insn-00befddc"></a> `00befddc` | `ed 03 01 aa` | mov x13,x1 | `FALL_THROUGH`
<a id="insn-00befde0"></a> `00befde0` | `05 00 00 14` | b 0x00befdf4 | `UNCONDITIONAL_JUMP`
<a id="insn-00befde4"></a> `00befde4` | `00 02 00 fd` | str d0,[x16] | `FALL_THROUGH`
<a id="insn-00befde8"></a> `00befde8` | `ad 21 00 91` | add x13,x13,#0x8 | `FALL_THROUGH`
<a id="insn-00befdec"></a> `00befdec` | `bf 01 02 eb` | cmp x13,x2 | `FALL_THROUGH`
<a id="insn-00befdf0"></a> `00befdf0` | `00 06 00 54` | b.eq 0x00befeb0 | `CONDITIONAL_JUMP`
<a id="insn-00befdf4"></a> `00befdf4` | `a0 01 40 fd` | ldr d0,[x13] | `FALL_THROUGH`
<a id="insn-00befdf8"></a> `00befdf8` | `01 00 40 fd` | ldr d1,[x0] | `FALL_THROUGH`
<a id="insn-00befdfc"></a> `00befdfc` | `00 20 61 1e` | fcmp d0,d1 | `FALL_THROUGH`
<a id="insn-00befe00"></a> `00befe00` | `45 ff ff 54` | b.pl 0x00befde8 | `CONDITIONAL_JUMP`
<a id="insn-00befe04"></a> `00befe04` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00befe08"></a> `00befe08` | `a1 01 00 fd` | str d1,[x13] | `FALL_THROUGH`
<a id="insn-00befe0c"></a> `00befe0c` | `00 00 00 fd` | str d0,[x0] | `FALL_THROUGH`
<a id="insn-00befe10"></a> `00befe10` | `cb fe ff 54` | b.lt 0x00befde8 | `CONDITIONAL_JUMP`
<a id="insn-00befe14"></a> `00befe14` | `3f 41 00 f1` | cmp x9,#0x10 | `FALL_THROUGH`
<a id="insn-00befe18"></a> `00befe18` | `00 01 00 54` | b.eq 0x00befe38 | `CONDITIONAL_JUMP`
<a id="insn-00befe1c"></a> `00befe1c` | `61 01 40 fd` | ldr d1,[x11] | `FALL_THROUGH`
<a id="insn-00befe20"></a> `00befe20` | `82 01 40 fd` | ldr d2,[x12] | `FALL_THROUGH`
<a id="insn-00befe24"></a> `00befe24` | `20 20 62 1e` | fcmp d1,d2 | `FALL_THROUGH`
<a id="insn-00befe28"></a> `00befe28` | `85 00 00 54` | b.pl 0x00befe38 | `CONDITIONAL_JUMP`
<a id="insn-00befe2c"></a> `00befe2c` | `ef 03 0c aa` | mov x15,x12 | `FALL_THROUGH`
<a id="insn-00befe30"></a> `00befe30` | `4e 00 80 52` | mov w14,#0x2 | `FALL_THROUGH`
<a id="insn-00befe34"></a> `00befe34` | `03 00 00 14` | b 0x00befe40 | `UNCONDITIONAL_JUMP`
<a id="insn-00befe38"></a> `00befe38` | `ef 03 0b aa` | mov x15,x11 | `FALL_THROUGH`
<a id="insn-00befe3c"></a> `00befe3c` | `2e 00 80 52` | mov w14,#0x1 | `FALL_THROUGH`
<a id="insn-00befe40"></a> `00befe40` | `e1 01 40 fd` | ldr d1,[x15] | `FALL_THROUGH`
<a id="insn-00befe44"></a> `00befe44` | `20 20 60 1e` | fcmp d1,d0 | `FALL_THROUGH`
<a id="insn-00befe48"></a> `00befe48` | `04 fd ff 54` | b.mi 0x00befde8 | `CONDITIONAL_JUMP`
<a id="insn-00befe4c"></a> `00befe4c` | `f0 03 00 aa` | mov x16,x0 | `FALL_THROUGH`
<a id="insn-00befe50"></a> `00befe50` | `04 00 00 14` | b 0x00befe60 | `UNCONDITIONAL_JUMP`
<a id="insn-00befe54"></a> `00befe54` | `e1 01 40 fd` | ldr d1,[x15] | `FALL_THROUGH`
<a id="insn-00befe58"></a> `00befe58` | `20 20 60 1e` | fcmp d1,d0 | `FALL_THROUGH`
<a id="insn-00befe5c"></a> `00befe5c` | `44 fc ff 54` | b.mi 0x00befde4 | `CONDITIONAL_JUMP`
<a id="insn-00befe60"></a> `00befe60` | `5f 01 0e eb` | cmp x10,x14 | `FALL_THROUGH`
<a id="insn-00befe64"></a> `00befe64` | `01 02 00 fd` | str d1,[x16] | `FALL_THROUGH`
<a id="insn-00befe68"></a> `00befe68` | `f0 03 0f aa` | mov x16,x15 | `FALL_THROUGH`
<a id="insn-00befe6c"></a> `00befe6c` | `cb fb ff 54` | b.lt 0x00befde4 | `CONDITIONAL_JUMP`
<a id="insn-00befe70"></a> `00befe70` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00befe74"></a> `00befe74` | `cf f9 7f d3` | lsl x15,x14,#0x1 | `FALL_THROUGH`
<a id="insn-00befe78"></a> `00befe78` | `c3 f9 7f b3` | bfm x3,x14,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00befe7c"></a> `00befe7c` | `f1 09 00 91` | add x17,x15,#0x2 | `FALL_THROUGH`
<a id="insn-00befe80"></a> `00befe80` | `0f 0c 03 8b` | add x15,x0,x3, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00befe84"></a> `00befe84` | `3f 02 08 eb` | cmp x17,x8 | `FALL_THROUGH`
<a id="insn-00befe88"></a> `00befe88` | `ee 03 03 aa` | mov x14,x3 | `FALL_THROUGH`
<a id="insn-00befe8c"></a> `00befe8c` | `4a fe ff 54` | b.ge 0x00befe54 | `CONDITIONAL_JUMP`
<a id="insn-00befe90"></a> `00befe90` | `e3 03 0f aa` | mov x3,x15 | `FALL_THROUGH`
<a id="insn-00befe94"></a> `00befe94` | `e2 01 40 fd` | ldr d2,[x15] | `FALL_THROUGH`
<a id="insn-00befe98"></a> `00befe98` | `61 8c 40 fc` | ldr d1,[x3, #0x8]! | `FALL_THROUGH`
<a id="insn-00befe9c"></a> `00befe9c` | `40 20 61 1e` | fcmp d2,d1 | `FALL_THROUGH`
<a id="insn-00befea0"></a> `00befea0` | `a5 fd ff 54` | b.pl 0x00befe54 | `CONDITIONAL_JUMP`
<a id="insn-00befea4"></a> `00befea4` | `ef 03 03 aa` | mov x15,x3 | `FALL_THROUGH`
<a id="insn-00befea8"></a> `00befea8` | `ee 03 11 aa` | mov x14,x17 | `FALL_THROUGH`
<a id="insn-00befeac"></a> `00befeac` | `ea ff ff 17` | b 0x00befe54 | `UNCONDITIONAL_JUMP`
<a id="insn-00befeb0"></a> `00befeb0` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00befeb4"></a> `00befeb4` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00befeb8"></a> `00befeb8` | `0a 01 00 54` | b.ge 0x00befed8 | `CONDITIONAL_JUMP`
<a id="insn-00befebc"></a> `00befebc` | `e2 03 03 aa` | mov x2,x3 | `FALL_THROUGH`
<a id="insn-00befec0"></a> `00befec0` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00befec4"></a> `00befec4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00befec8"></a> `00befec8` | `20 01 00 fd` | str d0,[x9] | `FALL_THROUGH`
<a id="insn-00befecc"></a> `00befecc` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00befed0"></a> `00befed0` | `08 05 00 d1` | sub x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00befed4"></a> `00befed4` | `4d ff ff 54` | b.le 0x00befebc | `CONDITIONAL_JUMP`
<a id="insn-00befed8"></a> `00befed8` | `09 09 00 d1` | sub x9,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00befedc"></a> `00befedc` | `00 00 40 fd` | ldr d0,[x0] | `FALL_THROUGH`
<a id="insn-00befee0"></a> `00befee0` | `ec 03 1f aa` | mov x12,xzr | `FALL_THROUGH`
<a id="insn-00befee4"></a> `00befee4` | `2a fd 41 d3` | lsr x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00befee8"></a> `00befee8` | `eb 03 00 aa` | mov x11,x0 | `FALL_THROUGH`
<a id="insn-00befeec"></a> `00befeec` | `0b 00 00 14` | b 0x00beff18 | `UNCONDITIONAL_JUMP`
<a id="insn-00befef0"></a> `00befef0` | `c1 0d 41 fc` | ldr d1,[x14, #0x10]! | `FALL_THROUGH`
<a id="insn-00befef4"></a> `00befef4` | `c2 81 5f fc` | ldur d2,[x14, #-0x8] | `FALL_THROUGH`
<a id="insn-00befef8"></a> `00befef8` | `40 20 61 1e` | fcmp d2,d1 | `FALL_THROUGH`
<a id="insn-00befefc"></a> `00befefc` | `29 51 8e 9a` | csel x9,x9,x14,pl | `FALL_THROUGH`
<a id="insn-00beff00"></a> `00beff00` | `ac 51 8f 9a` | csel x12,x13,x15,pl | `FALL_THROUGH`
<a id="insn-00beff04"></a> `00beff04` | `21 01 40 fd` | ldr d1,[x9] | `FALL_THROUGH`
<a id="insn-00beff08"></a> `00beff08` | `9f 01 0a eb` | cmp x12,x10 | `FALL_THROUGH`
<a id="insn-00beff0c"></a> `00beff0c` | `61 01 00 fd` | str d1,[x11] | `FALL_THROUGH`
<a id="insn-00beff10"></a> `00beff10` | `eb 03 09 aa` | mov x11,x9 | `FALL_THROUGH`
<a id="insn-00beff14"></a> `00beff14` | `6c 01 00 54` | b.gt 0x00beff40 | `CONDITIONAL_JUMP`
<a id="insn-00beff18"></a> `00beff18` | `89 f9 7f d3` | lsl x9,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00beff1c"></a> `00beff1c` | `6e 0d 0c 8b` | add x14,x11,x12, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00beff20"></a> `00beff20` | `2d 00 80 52` | mov w13,#0x1 | `FALL_THROUGH`
<a id="insn-00beff24"></a> `00beff24` | `8d f9 7f b3` | bfm x13,x12,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00beff28"></a> `00beff28` | `2f 09 00 91` | add x15,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00beff2c"></a> `00beff2c` | `c9 21 00 91` | add x9,x14,#0x8 | `FALL_THROUGH`
<a id="insn-00beff30"></a> `00beff30` | `ff 01 08 eb` | cmp x15,x8 | `FALL_THROUGH`
<a id="insn-00beff34"></a> `00beff34` | `eb fd ff 54` | b.lt 0x00befef0 | `CONDITIONAL_JUMP`
<a id="insn-00beff38"></a> `00beff38` | `ec 03 0d aa` | mov x12,x13 | `FALL_THROUGH`
<a id="insn-00beff3c"></a> `00beff3c` | `f2 ff ff 17` | b 0x00beff04 | `UNCONDITIONAL_JUMP`
<a id="insn-00beff40"></a> `00beff40` | `21 20 00 d1` | sub x1,x1,#0x8 | `FALL_THROUGH`
<a id="insn-00beff44"></a> `00beff44` | `3f 01 01 eb` | cmp x9,x1 | `FALL_THROUGH`
<a id="insn-00beff48"></a> `00beff48` | `00 fc ff 54` | b.eq 0x00befec8 | `CONDITIONAL_JUMP`
<a id="insn-00beff4c"></a> `00beff4c` | `2a 01 00 cb` | sub x10,x9,x0 | `FALL_THROUGH`
<a id="insn-00beff50"></a> `00beff50` | `21 00 40 fd` | ldr d1,[x1] | `FALL_THROUGH`
<a id="insn-00beff54"></a> `00beff54` | `4a 21 00 91` | add x10,x10,#0x8 | `FALL_THROUGH`
<a id="insn-00beff58"></a> `00beff58` | `4a fd 43 93` | asr x10,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00beff5c"></a> `00beff5c` | `21 01 00 fd` | str d1,[x9] | `FALL_THROUGH`
<a id="insn-00beff60"></a> `00beff60` | `20 00 00 fd` | str d0,[x1] | `FALL_THROUGH`
<a id="insn-00beff64"></a> `00beff64` | `4a 09 00 f1` | subs x10,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00beff68"></a> `00beff68` | `2b fb ff 54` | b.lt 0x00befecc | `CONDITIONAL_JUMP`
<a id="insn-00beff6c"></a> `00beff6c` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00beff70"></a> `00beff70` | `20 01 40 fd` | ldr d0,[x9] | `FALL_THROUGH`
<a id="insn-00beff74"></a> `00beff74` | `0b 0c 0a 8b` | add x11,x0,x10, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00beff78"></a> `00beff78` | `61 01 40 fd` | ldr d1,[x11] | `FALL_THROUGH`
<a id="insn-00beff7c"></a> `00beff7c` | `20 20 60 1e` | fcmp d1,d0 | `FALL_THROUGH`
<a id="insn-00beff80"></a> `00beff80` | `65 fa ff 54` | b.pl 0x00befecc | `CONDITIONAL_JUMP`
<a id="insn-00beff84"></a> `00beff84` | `ec 03 09 aa` | mov x12,x9 | `FALL_THROUGH`
<a id="insn-00beff88"></a> `00beff88` | `e9 03 0b aa` | mov x9,x11 | `FALL_THROUGH`
<a id="insn-00beff8c"></a> `00beff8c` | `81 01 00 fd` | str d1,[x12] | `FALL_THROUGH`
<a id="insn-00beff90"></a> `00beff90` | `ca f9 ff b4` | cbz x10,0x00befec8 | `CONDITIONAL_JUMP`
<a id="insn-00beff94"></a> `00beff94` | `4a 05 00 d1` | sub x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00beff98"></a> `00beff98` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00beff9c"></a> `00beff9c` | `0b 0c 0a 8b` | add x11,x0,x10, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00beffa0"></a> `00beffa0` | `61 01 40 fd` | ldr d1,[x11] | `FALL_THROUGH`
<a id="insn-00beffa4"></a> `00beffa4` | `20 20 60 1e` | fcmp d1,d0 | `FALL_THROUGH`
<a id="insn-00beffa8"></a> `00beffa8` | `e4 fe ff 54` | b.mi 0x00beff84 | `CONDITIONAL_JUMP`
<a id="insn-00beffac"></a> `00beffac` | `c7 ff ff 17` | b 0x00befec8 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00befcd8`](#insn-00befcd8) 範囲 `[['00befcd8', '00befce3']]`
  - `CONDITIONAL_JUMP` [`00befce0`](#insn-00befce0) → [`00befec0`](#insn-00befec0)
  - `FALL_THROUGH` [`00befce0`](#insn-00befce0) → [`00befce4`](#insn-00befce4)
- ブロック [`00befce4`](#insn-00befce4) 範囲 `[['00befce4', '00befcf3']]`
  - `CONDITIONAL_JUMP` [`00befcf0`](#insn-00befcf0) → [`00befdc4`](#insn-00befdc4)
  - `FALL_THROUGH` [`00befcf0`](#insn-00befcf0) → [`00befcf4`](#insn-00befcf4)
- ブロック [`00befcf4`](#insn-00befcf4) 範囲 `[['00befcf4', '00befcff']]`
  - `UNCONDITIONAL_JUMP` [`00befcfc`](#insn-00befcfc) → [`00befd10`](#insn-00befd10)
- ブロック [`00befd00`](#insn-00befd00) 範囲 `[['00befd00', '00befd03']]`
  - `FALL_THROUGH` [`00befd00`](#insn-00befd00) → [`00befd04`](#insn-00befd04)
- ブロック [`00befd04`](#insn-00befd04) 範囲 `[['00befd04', '00befd0f']]`
  - `CONDITIONAL_JUMP` [`00befd0c`](#insn-00befd0c) → [`00befdc4`](#insn-00befdc4)
  - `FALL_THROUGH` [`00befd0c`](#insn-00befd0c) → [`00befd10`](#insn-00befd10)
- ブロック [`00befd10`](#insn-00befd10) 範囲 `[['00befd10', '00befd17']]`
  - `CONDITIONAL_JUMP` [`00befd14`](#insn-00befd14) → [`00befd04`](#insn-00befd04)
  - `FALL_THROUGH` [`00befd14`](#insn-00befd14) → [`00befd18`](#insn-00befd18)
- ブロック [`00befd18`](#insn-00befd18) 範囲 `[['00befd18', '00befd33']]`
  - `CONDITIONAL_JUMP` [`00befd30`](#insn-00befd30) → [`00befd50`](#insn-00befd50)
  - `FALL_THROUGH` [`00befd30`](#insn-00befd30) → [`00befd34`](#insn-00befd34)
- ブロック [`00befd34`](#insn-00befd34) 範囲 `[['00befd34', '00befd47']]`
  - `CONDITIONAL_JUMP` [`00befd44`](#insn-00befd44) → [`00befd50`](#insn-00befd50)
  - `FALL_THROUGH` [`00befd44`](#insn-00befd44) → [`00befd48`](#insn-00befd48)
- ブロック [`00befd48`](#insn-00befd48) 範囲 `[['00befd48', '00befd4f']]`
  - `FALL_THROUGH` [`00befd4c`](#insn-00befd4c) → [`00befd50`](#insn-00befd50)
- ブロック [`00befd50`](#insn-00befd50) 範囲 `[['00befd50', '00befd63']]`
  - `CONDITIONAL_JUMP` [`00befd60`](#insn-00befd60) → [`00befd74`](#insn-00befd74)
  - `FALL_THROUGH` [`00befd60`](#insn-00befd60) → [`00befd64`](#insn-00befd64)
- ブロック [`00befd64`](#insn-00befd64) 範囲 `[['00befd64', '00befd67']]`
  - `UNCONDITIONAL_JUMP` [`00befd64`](#insn-00befd64) → [`00befd04`](#insn-00befd04)
- ブロック [`00befd68`](#insn-00befd68) 範囲 `[['00befd68', '00befd73']]`
  - `CONDITIONAL_JUMP` [`00befd70`](#insn-00befd70) → [`00befd00`](#insn-00befd00)
  - `FALL_THROUGH` [`00befd70`](#insn-00befd70) → [`00befd74`](#insn-00befd74)
- ブロック [`00befd74`](#insn-00befd74) 範囲 `[['00befd74', '00befd83']]`
  - `CONDITIONAL_JUMP` [`00befd80`](#insn-00befd80) → [`00befd00`](#insn-00befd00)
  - `FALL_THROUGH` [`00befd80`](#insn-00befd80) → [`00befd84`](#insn-00befd84)
- ブロック [`00befd84`](#insn-00befd84) 範囲 `[['00befd84', '00befda3']]`
  - `CONDITIONAL_JUMP` [`00befda0`](#insn-00befda0) → [`00befd68`](#insn-00befd68)
  - `FALL_THROUGH` [`00befda0`](#insn-00befda0) → [`00befda4`](#insn-00befda4)
- ブロック [`00befda4`](#insn-00befda4) 範囲 `[['00befda4', '00befdb7']]`
  - `CONDITIONAL_JUMP` [`00befdb4`](#insn-00befdb4) → [`00befd68`](#insn-00befd68)
  - `FALL_THROUGH` [`00befdb4`](#insn-00befdb4) → [`00befdb8`](#insn-00befdb8)
- ブロック [`00befdb8`](#insn-00befdb8) 範囲 `[['00befdb8', '00befdc3']]`
  - `UNCONDITIONAL_JUMP` [`00befdc0`](#insn-00befdc0) → [`00befd68`](#insn-00befd68)
- ブロック [`00befdc4`](#insn-00befdc4) 範囲 `[['00befdc4', '00befdcf']]`
  - `CONDITIONAL_JUMP` [`00befdcc`](#insn-00befdcc) → [`00befeb4`](#insn-00befeb4)
  - `FALL_THROUGH` [`00befdcc`](#insn-00befdcc) → [`00befdd0`](#insn-00befdd0)
- ブロック [`00befdd0`](#insn-00befdd0) 範囲 `[['00befdd0', '00befde3']]`
  - `UNCONDITIONAL_JUMP` [`00befde0`](#insn-00befde0) → [`00befdf4`](#insn-00befdf4)
- ブロック [`00befde4`](#insn-00befde4) 範囲 `[['00befde4', '00befde7']]`
  - `FALL_THROUGH` [`00befde4`](#insn-00befde4) → [`00befde8`](#insn-00befde8)
- ブロック [`00befde8`](#insn-00befde8) 範囲 `[['00befde8', '00befdf3']]`
  - `CONDITIONAL_JUMP` [`00befdf0`](#insn-00befdf0) → [`00befeb0`](#insn-00befeb0)
  - `FALL_THROUGH` [`00befdf0`](#insn-00befdf0) → [`00befdf4`](#insn-00befdf4)
- ブロック [`00befdf4`](#insn-00befdf4) 範囲 `[['00befdf4', '00befe03']]`
  - `CONDITIONAL_JUMP` [`00befe00`](#insn-00befe00) → [`00befde8`](#insn-00befde8)
  - `FALL_THROUGH` [`00befe00`](#insn-00befe00) → [`00befe04`](#insn-00befe04)
- ブロック [`00befe04`](#insn-00befe04) 範囲 `[['00befe04', '00befe13']]`
  - `CONDITIONAL_JUMP` [`00befe10`](#insn-00befe10) → [`00befde8`](#insn-00befde8)
  - `FALL_THROUGH` [`00befe10`](#insn-00befe10) → [`00befe14`](#insn-00befe14)
- ブロック [`00befe14`](#insn-00befe14) 範囲 `[['00befe14', '00befe1b']]`
  - `CONDITIONAL_JUMP` [`00befe18`](#insn-00befe18) → [`00befe38`](#insn-00befe38)
  - `FALL_THROUGH` [`00befe18`](#insn-00befe18) → [`00befe1c`](#insn-00befe1c)
- ブロック [`00befe1c`](#insn-00befe1c) 範囲 `[['00befe1c', '00befe2b']]`
  - `CONDITIONAL_JUMP` [`00befe28`](#insn-00befe28) → [`00befe38`](#insn-00befe38)
  - `FALL_THROUGH` [`00befe28`](#insn-00befe28) → [`00befe2c`](#insn-00befe2c)
- ブロック [`00befe2c`](#insn-00befe2c) 範囲 `[['00befe2c', '00befe37']]`
  - `UNCONDITIONAL_JUMP` [`00befe34`](#insn-00befe34) → [`00befe40`](#insn-00befe40)
- ブロック [`00befe38`](#insn-00befe38) 範囲 `[['00befe38', '00befe3f']]`
  - `FALL_THROUGH` [`00befe3c`](#insn-00befe3c) → [`00befe40`](#insn-00befe40)
- ブロック [`00befe40`](#insn-00befe40) 範囲 `[['00befe40', '00befe4b']]`
  - `CONDITIONAL_JUMP` [`00befe48`](#insn-00befe48) → [`00befde8`](#insn-00befde8)
  - `FALL_THROUGH` [`00befe48`](#insn-00befe48) → [`00befe4c`](#insn-00befe4c)
- ブロック [`00befe4c`](#insn-00befe4c) 範囲 `[['00befe4c', '00befe53']]`
  - `UNCONDITIONAL_JUMP` [`00befe50`](#insn-00befe50) → [`00befe60`](#insn-00befe60)
- ブロック [`00befe54`](#insn-00befe54) 範囲 `[['00befe54', '00befe5f']]`
  - `CONDITIONAL_JUMP` [`00befe5c`](#insn-00befe5c) → [`00befde4`](#insn-00befde4)
  - `FALL_THROUGH` [`00befe5c`](#insn-00befe5c) → [`00befe60`](#insn-00befe60)
- ブロック [`00befe60`](#insn-00befe60) 範囲 `[['00befe60', '00befe6f']]`
  - `CONDITIONAL_JUMP` [`00befe6c`](#insn-00befe6c) → [`00befde4`](#insn-00befde4)
  - `FALL_THROUGH` [`00befe6c`](#insn-00befe6c) → [`00befe70`](#insn-00befe70)
- ブロック [`00befe70`](#insn-00befe70) 範囲 `[['00befe70', '00befe8f']]`
  - `CONDITIONAL_JUMP` [`00befe8c`](#insn-00befe8c) → [`00befe54`](#insn-00befe54)
  - `FALL_THROUGH` [`00befe8c`](#insn-00befe8c) → [`00befe90`](#insn-00befe90)
- ブロック [`00befe90`](#insn-00befe90) 範囲 `[['00befe90', '00befea3']]`
  - `CONDITIONAL_JUMP` [`00befea0`](#insn-00befea0) → [`00befe54`](#insn-00befe54)
  - `FALL_THROUGH` [`00befea0`](#insn-00befea0) → [`00befea4`](#insn-00befea4)
- ブロック [`00befea4`](#insn-00befea4) 範囲 `[['00befea4', '00befeaf']]`
  - `UNCONDITIONAL_JUMP` [`00befeac`](#insn-00befeac) → [`00befe54`](#insn-00befe54)
- ブロック [`00befeb0`](#insn-00befeb0) 範囲 `[['00befeb0', '00befeb3']]`
  - `FALL_THROUGH` [`00befeb0`](#insn-00befeb0) → [`00befeb4`](#insn-00befeb4)
- ブロック [`00befeb4`](#insn-00befeb4) 範囲 `[['00befeb4', '00befebb']]`
  - `CONDITIONAL_JUMP` [`00befeb8`](#insn-00befeb8) → [`00befed8`](#insn-00befed8)
  - `FALL_THROUGH` [`00befeb8`](#insn-00befeb8) → [`00befebc`](#insn-00befebc)
- ブロック [`00befebc`](#insn-00befebc) 範囲 `[['00befebc', '00befebf']]`
  - `FALL_THROUGH` [`00befebc`](#insn-00befebc) → [`00befec0`](#insn-00befec0)
- ブロック [`00befec0`](#insn-00befec0) 範囲 `[['00befec0', '00befec7']]`
- ブロック [`00befec8`](#insn-00befec8) 範囲 `[['00befec8', '00befecb']]`
  - `FALL_THROUGH` [`00befec8`](#insn-00befec8) → [`00befecc`](#insn-00befecc)
- ブロック [`00befecc`](#insn-00befecc) 範囲 `[['00befecc', '00befed7']]`
  - `CONDITIONAL_JUMP` [`00befed4`](#insn-00befed4) → [`00befebc`](#insn-00befebc)
  - `FALL_THROUGH` [`00befed4`](#insn-00befed4) → [`00befed8`](#insn-00befed8)
- ブロック [`00befed8`](#insn-00befed8) 範囲 `[['00befed8', '00befeef']]`
  - `UNCONDITIONAL_JUMP` [`00befeec`](#insn-00befeec) → [`00beff18`](#insn-00beff18)
- ブロック [`00befef0`](#insn-00befef0) 範囲 `[['00befef0', '00beff03']]`
  - `FALL_THROUGH` [`00beff00`](#insn-00beff00) → [`00beff04`](#insn-00beff04)
- ブロック [`00beff04`](#insn-00beff04) 範囲 `[['00beff04', '00beff17']]`
  - `CONDITIONAL_JUMP` [`00beff14`](#insn-00beff14) → [`00beff40`](#insn-00beff40)
  - `FALL_THROUGH` [`00beff14`](#insn-00beff14) → [`00beff18`](#insn-00beff18)
- ブロック [`00beff18`](#insn-00beff18) 範囲 `[['00beff18', '00beff37']]`
  - `CONDITIONAL_JUMP` [`00beff34`](#insn-00beff34) → [`00befef0`](#insn-00befef0)
  - `FALL_THROUGH` [`00beff34`](#insn-00beff34) → [`00beff38`](#insn-00beff38)
- ブロック [`00beff38`](#insn-00beff38) 範囲 `[['00beff38', '00beff3f']]`
  - `UNCONDITIONAL_JUMP` [`00beff3c`](#insn-00beff3c) → [`00beff04`](#insn-00beff04)
- ブロック [`00beff40`](#insn-00beff40) 範囲 `[['00beff40', '00beff4b']]`
  - `CONDITIONAL_JUMP` [`00beff48`](#insn-00beff48) → [`00befec8`](#insn-00befec8)
  - `FALL_THROUGH` [`00beff48`](#insn-00beff48) → [`00beff4c`](#insn-00beff4c)
- ブロック [`00beff4c`](#insn-00beff4c) 範囲 `[['00beff4c', '00beff6b']]`
  - `CONDITIONAL_JUMP` [`00beff68`](#insn-00beff68) → [`00befecc`](#insn-00befecc)
  - `FALL_THROUGH` [`00beff68`](#insn-00beff68) → [`00beff6c`](#insn-00beff6c)
- ブロック [`00beff6c`](#insn-00beff6c) 範囲 `[['00beff6c', '00beff83']]`
  - `CONDITIONAL_JUMP` [`00beff80`](#insn-00beff80) → [`00befecc`](#insn-00befecc)
  - `FALL_THROUGH` [`00beff80`](#insn-00beff80) → [`00beff84`](#insn-00beff84)
- ブロック [`00beff84`](#insn-00beff84) 範囲 `[['00beff84', '00beff87']]`
  - `FALL_THROUGH` [`00beff84`](#insn-00beff84) → [`00beff88`](#insn-00beff88)
- ブロック [`00beff88`](#insn-00beff88) 範囲 `[['00beff88', '00beff93']]`
  - `CONDITIONAL_JUMP` [`00beff90`](#insn-00beff90) → [`00befec8`](#insn-00befec8)
  - `FALL_THROUGH` [`00beff90`](#insn-00beff90) → [`00beff94`](#insn-00beff94)
- ブロック [`00beff94`](#insn-00beff94) 範囲 `[['00beff94', '00beffab']]`
  - `CONDITIONAL_JUMP` [`00beffa8`](#insn-00beffa8) → [`00beff84`](#insn-00beff84)
  - `FALL_THROUGH` [`00beffa8`](#insn-00beffa8) → [`00beffac`](#insn-00beffac)
- ブロック [`00beffac`](#insn-00beffac) 範囲 `[['00beffac', '00beffaf']]`
  - `UNCONDITIONAL_JUMP` [`00beffac`](#insn-00beffac) → [`00befec8`](#insn-00befec8)

## 命令位置別の参照

- [`00befce0`](#insn-00befce0) → [`00befec0`](#insn-00befec0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befcf0`](#insn-00befcf0) → [`00befdc4`](#insn-00befdc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befcfc`](#insn-00befcfc) → [`00befd10`](#insn-00befd10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befd0c`](#insn-00befd0c) → [`00befdc4`](#insn-00befdc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befd14`](#insn-00befd14) → [`00befd04`](#insn-00befd04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befd30`](#insn-00befd30) → [`00befd50`](#insn-00befd50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befd44`](#insn-00befd44) → [`00befd50`](#insn-00befd50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befd60`](#insn-00befd60) → [`00befd74`](#insn-00befd74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befd64`](#insn-00befd64) → [`00befd04`](#insn-00befd04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befd70`](#insn-00befd70) → [`00befd00`](#insn-00befd00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befd80`](#insn-00befd80) → [`00befd00`](#insn-00befd00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befda0`](#insn-00befda0) → [`00befd68`](#insn-00befd68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befdb4`](#insn-00befdb4) → [`00befd68`](#insn-00befd68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befdc0`](#insn-00befdc0) → [`00befd68`](#insn-00befd68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befdcc`](#insn-00befdcc) → [`00befeb4`](#insn-00befeb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befde0`](#insn-00befde0) → [`00befdf4`](#insn-00befdf4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befdf0`](#insn-00befdf0) → [`00befeb0`](#insn-00befeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befe00`](#insn-00befe00) → [`00befde8`](#insn-00befde8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befe10`](#insn-00befe10) → [`00befde8`](#insn-00befde8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befe18`](#insn-00befe18) → [`00befe38`](#insn-00befe38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befe28`](#insn-00befe28) → [`00befe38`](#insn-00befe38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befe34`](#insn-00befe34) → [`00befe40`](#insn-00befe40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befe48`](#insn-00befe48) → [`00befde8`](#insn-00befde8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befe50`](#insn-00befe50) → [`00befe60`](#insn-00befe60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befe5c`](#insn-00befe5c) → [`00befde4`](#insn-00befde4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befe6c`](#insn-00befe6c) → [`00befde4`](#insn-00befde4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befe8c`](#insn-00befe8c) → [`00befe54`](#insn-00befe54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befea0`](#insn-00befea0) → [`00befe54`](#insn-00befe54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befeac`](#insn-00befeac) → [`00befe54`](#insn-00befe54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befeb8`](#insn-00befeb8) → [`00befed8`](#insn-00befed8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befed4`](#insn-00befed4) → [`00befebc`](#insn-00befebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befeec`](#insn-00befeec) → [`00beff18`](#insn-00beff18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beff14`](#insn-00beff14) → [`00beff40`](#insn-00beff40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beff34`](#insn-00beff34) → [`00befef0`](#insn-00befef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beff3c`](#insn-00beff3c) → [`00beff04`](#insn-00beff04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beff48`](#insn-00beff48) → [`00befec8`](#insn-00befec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beff68`](#insn-00beff68) → [`00befecc`](#insn-00befecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beff80`](#insn-00beff80) → [`00befecc`](#insn-00befecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beff90`](#insn-00beff90) → [`00befec8`](#insn-00befec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beffa8`](#insn-00beffa8) → [`00beff84`](#insn-00beff84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beffac`](#insn-00beffac) → [`00befec8`](#insn-00befec8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00befce0`](#insn-00befce0)

~~~json
{
  "source": "00befce0",
  "target": "00befec0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befcf0`](#insn-00befcf0)

~~~json
{
  "source": "00befcf0",
  "target": "00befdc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befcfc`](#insn-00befcfc)

~~~json
{
  "source": "00befcfc",
  "target": "00befd10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befd0c`](#insn-00befd0c)

~~~json
{
  "source": "00befd0c",
  "target": "00befdc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befd14`](#insn-00befd14)

~~~json
{
  "source": "00befd14",
  "target": "00befd04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befd30`](#insn-00befd30)

~~~json
{
  "source": "00befd30",
  "target": "00befd50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befd44`](#insn-00befd44)

~~~json
{
  "source": "00befd44",
  "target": "00befd50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befd60`](#insn-00befd60)

~~~json
{
  "source": "00befd60",
  "target": "00befd74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befd64`](#insn-00befd64)

~~~json
{
  "source": "00befd64",
  "target": "00befd04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befd70`](#insn-00befd70)

~~~json
{
  "source": "00befd70",
  "target": "00befd00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befd80`](#insn-00befd80)

~~~json
{
  "source": "00befd80",
  "target": "00befd00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befda0`](#insn-00befda0)

~~~json
{
  "source": "00befda0",
  "target": "00befd68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befdb4`](#insn-00befdb4)

~~~json
{
  "source": "00befdb4",
  "target": "00befd68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befdc0`](#insn-00befdc0)

~~~json
{
  "source": "00befdc0",
  "target": "00befd68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befdcc`](#insn-00befdcc)

~~~json
{
  "source": "00befdcc",
  "target": "00befeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befde0`](#insn-00befde0)

~~~json
{
  "source": "00befde0",
  "target": "00befdf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befdf0`](#insn-00befdf0)

~~~json
{
  "source": "00befdf0",
  "target": "00befeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befe00`](#insn-00befe00)

~~~json
{
  "source": "00befe00",
  "target": "00befde8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befe10`](#insn-00befe10)

~~~json
{
  "source": "00befe10",
  "target": "00befde8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befe18`](#insn-00befe18)

~~~json
{
  "source": "00befe18",
  "target": "00befe38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befe28`](#insn-00befe28)

~~~json
{
  "source": "00befe28",
  "target": "00befe38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befe34`](#insn-00befe34)

~~~json
{
  "source": "00befe34",
  "target": "00befe40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befe48`](#insn-00befe48)

~~~json
{
  "source": "00befe48",
  "target": "00befde8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befe50`](#insn-00befe50)

~~~json
{
  "source": "00befe50",
  "target": "00befe60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befe5c`](#insn-00befe5c)

~~~json
{
  "source": "00befe5c",
  "target": "00befde4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befe6c`](#insn-00befe6c)

~~~json
{
  "source": "00befe6c",
  "target": "00befde4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befe8c`](#insn-00befe8c)

~~~json
{
  "source": "00befe8c",
  "target": "00befe54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befea0`](#insn-00befea0)

~~~json
{
  "source": "00befea0",
  "target": "00befe54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befeac`](#insn-00befeac)

~~~json
{
  "source": "00befeac",
  "target": "00befe54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befeb8`](#insn-00befeb8)

~~~json
{
  "source": "00befeb8",
  "target": "00befed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befed4`](#insn-00befed4)

~~~json
{
  "source": "00befed4",
  "target": "00befebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befeec`](#insn-00befeec)

~~~json
{
  "source": "00befeec",
  "target": "00beff18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beff14`](#insn-00beff14)

~~~json
{
  "source": "00beff14",
  "target": "00beff40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beff34`](#insn-00beff34)

~~~json
{
  "source": "00beff34",
  "target": "00befef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beff3c`](#insn-00beff3c)

~~~json
{
  "source": "00beff3c",
  "target": "00beff04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beff48`](#insn-00beff48)

~~~json
{
  "source": "00beff48",
  "target": "00befec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beff68`](#insn-00beff68)

~~~json
{
  "source": "00beff68",
  "target": "00befecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beff80`](#insn-00beff80)

~~~json
{
  "source": "00beff80",
  "target": "00befecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beff90`](#insn-00beff90)

~~~json
{
  "source": "00beff90",
  "target": "00befec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beffa8`](#insn-00beffa8)

~~~json
{
  "source": "00beffa8",
  "target": "00beff84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beffac`](#insn-00beffac)

~~~json
{
  "source": "00beffac",
  "target": "00befec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
