# 00becda0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bebdac`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00bebdac.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/no_difference_in_scope-0014.md#compare-4d7b538421d547e97928fbb5d7f62919)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00becda0",
  "name": "FUN_00becda0",
  "size": 764,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6eeb278815534cae5bc56ac05f5389c7eb00277d70b026778243be98758af271",
  "source_text_sha256": "6eeb278815534cae5bc56ac05f5389c7eb00277d70b026778243be98758af271",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00becda0",
        "00bed09b"
      ]
    ],
    "bytes_sha256": "6e6be1a71ded6f41dfce2c5dcf54974652c4c29e53b9f22edc859ce954b40ad0",
    "instruction_count": 191,
    "instruction_bytes": 764,
    "body_bytes": 764,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be5e28](../00be5/00be5e28.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6640 bytes

~~~c

int * FUN_00becda0(int *param_1,int *param_2,int *param_3)

{
  bool bVar1;
  int *piVar2;
  ulong uVar3;
  int iVar4;
  int iVar5;
  int *piVar6;
  ulong uVar7;
  long lVar8;
  int *piVar9;
  ulong uVar10;
  long lVar11;
  int *piVar12;
  int *piVar13;
  ulong uVar14;
  int *piVar15;
  int iVar16;
  int iVar17;
  
  if (param_1 != param_2) {
    lVar8 = (long)param_2 - (long)param_1 >> 2;
    if (1 < lVar8) {
      uVar10 = lVar8 - 2U >> 1;
      uVar7 = uVar10;
      do {
        if ((long)uVar7 <= (long)uVar10) {
          uVar3 = (uVar7 & 0x3fffffffffffffff) << 1 | 1;
          uVar14 = (uVar7 & 0x3fffffffffffffff) * 2 + 2;
          piVar12 = param_1 + uVar3;
          if ((long)uVar14 < lVar8) {
                    /* try { // try from 00becdfc to 00cece17 has its CatchHandler @ 00becf98 */
            iVar17 = *piVar12;
            iVar4 = piVar12[1];
            iVar16 = iVar17;
            if (iVar17 <= iVar4) {
              iVar16 = iVar4;
            }
            piVar13 = piVar12 + 1;
            if (iVar4 <= iVar17) {
              piVar13 = piVar12;
              uVar14 = uVar3;
            }
          }
          else {
            iVar16 = *piVar12;
            piVar13 = piVar12;
            uVar14 = uVar3;
          }
          iVar17 = param_1[uVar7];
          piVar12 = param_1 + uVar7;
          if (iVar17 <= iVar16) {
            do {
              while( true ) {
                piVar9 = piVar13;
                *piVar12 = iVar16;
                if ((long)uVar10 < (long)uVar14) goto LAB_00becdc8;
                uVar3 = uVar14 << 1 | 1;
                uVar14 = uVar14 * 2 + 2;
                piVar6 = param_1 + uVar3;
                piVar12 = piVar9;
                if ((long)uVar14 < lVar8) break;
                iVar16 = *piVar6;
                piVar13 = piVar6;
                uVar14 = uVar3;
                if (iVar16 < iVar17) goto LAB_00becdc8;
              }
              iVar4 = *piVar6;
              iVar5 = piVar6[1];
              iVar16 = iVar4;
              if (iVar4 <= iVar5) {
                iVar16 = iVar5;
              }
              piVar13 = piVar6 + 1;
              if (iVar5 <= iVar4) {
                uVar14 = uVar3;
                piVar13 = piVar6;
              }
            } while (iVar17 <= iVar16);
LAB_00becdc8:
            *piVar9 = iVar17;
          }
        }
                    /* try { // try from 00becdcc to 00cecdd7 has its CatchHandler @ 00becf88 */
        bVar1 = 0 < (long)uVar7;
        uVar7 = uVar7 - 1;
      } while (bVar1);
    }
    piVar12 = param_2;
    if (param_2 != param_3) {
      piVar13 = param_1 + 1;
      piVar9 = param_2;
      do {
        iVar16 = *piVar9;
        if (iVar16 < *param_1) {
          *piVar9 = *param_1;
          *param_1 = iVar16;
          if (1 < lVar8) {
            iVar4 = *piVar13;
            iVar17 = iVar4;
            if ((long)param_2 - (long)param_1 == 8) {
              uVar7 = 1;
              piVar12 = piVar13;
            }
            else {
              iVar5 = param_1[2];
              if (iVar4 <= iVar5) {
                iVar17 = iVar5;
              }
              piVar12 = param_1 + 2;
              if (iVar5 <= iVar4) {
                piVar12 = piVar13;
              }
              uVar7 = 1;
              if (iVar4 < iVar5) {
                uVar7 = 2;
              }
            }
            piVar6 = param_1;
            if (iVar16 <= iVar17) {
              do {
                while( true ) {
                  piVar15 = piVar12;
                  *piVar6 = iVar17;
                  if ((long)(lVar8 - 2U >> 1) < (long)uVar7) goto LAB_00becebc;
                  uVar10 = uVar7 << 1 | 1;
                  uVar7 = uVar7 * 2 + 2;
                  piVar2 = param_1 + uVar10;
                  piVar6 = piVar15;
                  if ((long)uVar7 < lVar8) break;
                  iVar17 = *piVar2;
                    /* catch() { ... } // from try @ 00becdcc with catch @ 00becf88 */
                  uVar7 = uVar10;
                  piVar12 = piVar2;
                  if (iVar17 < iVar16) goto LAB_00becebc;
                }
                iVar4 = *piVar2;
                iVar5 = piVar2[1];
                iVar17 = iVar4;
                if (iVar4 <= iVar5) {
                  iVar17 = iVar5;
                }
                piVar12 = piVar2 + 1;
                if (iVar5 <= iVar4) {
                  uVar7 = uVar10;
                  piVar12 = piVar2;
                }
              } while (iVar16 <= iVar17);
LAB_00becebc:
              *piVar15 = iVar16;
            }
          }
        }
        piVar9 = piVar9 + 1;
        piVar12 = param_3;
      } while (piVar9 != param_3);
    }
                    /* catch() { ... } // from try @ 00becdfc with catch @ 00becf98 */
    param_3 = piVar12;
    if (1 < lVar8) {
      do {
        iVar16 = *param_1;
        uVar7 = 0;
        piVar12 = param_1;
        do {
          uVar14 = uVar7 << 1 | 1;
          uVar10 = uVar7 * 2 + 2;
          piVar13 = piVar12 + uVar7 + 1;
          if ((long)uVar10 < lVar8) {
            iVar5 = piVar12[uVar7 + 2];
            iVar4 = piVar12[uVar7 + 1];
            iVar17 = iVar4;
            if (iVar4 <= iVar5) {
              iVar17 = iVar5;
            }
            piVar9 = piVar12 + uVar7 + 2;
            uVar7 = uVar10;
            if (iVar5 <= iVar4) {
              piVar9 = piVar13;
              uVar7 = uVar14;
            }
          }
          else {
            iVar17 = *piVar13;
            piVar9 = piVar13;
            uVar7 = uVar14;
          }
          *piVar12 = iVar17;
          piVar12 = piVar9;
        } while ((long)uVar7 <= (long)(lVar8 - 2U >> 1));
        param_2 = param_2 + -1;
        if (piVar9 == param_2) {
          *piVar9 = iVar16;
        }
        else {
          lVar11 = (long)piVar9 + (4 - (long)param_1) >> 2;
          *piVar9 = *param_2;
          *param_2 = iVar16;
          if (1 < lVar11) {
            uVar7 = lVar11 - 2U >> 1;
            iVar16 = *piVar9;
            iVar17 = param_1[uVar7];
            piVar12 = param_1 + uVar7;
            if (iVar17 < iVar16) {
              do {
                piVar13 = piVar12;
                *piVar9 = iVar17;
                if (uVar7 == 0) break;
                uVar7 = uVar7 - 1 >> 1;
                iVar17 = param_1[uVar7];
                piVar9 = piVar13;
                piVar12 = param_1 + uVar7;
              } while (iVar17 < iVar16);
              *piVar13 = iVar16;
            }
          }
        }
        bVar1 = 2 < lVar8;
        lVar8 = lVar8 + -1;
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
<a id="insn-00becda0"></a> `00becda0` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00becda4"></a> `00becda4` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-00becda8"></a> `00becda8` | `e0 0f 00 54` | b.eq 0x00becfa4 | `CONDITIONAL_JUMP`
<a id="insn-00becdac"></a> `00becdac` | `29 00 00 cb` | sub x9,x1,x0 | `FALL_THROUGH`
<a id="insn-00becdb0"></a> `00becdb0` | `28 fd 42 93` | asr x8,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00becdb4"></a> `00becdb4` | `0a 09 00 f1` | subs x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00becdb8"></a> `00becdb8` | `0b 07 00 54` | b.lt 0x00bece98 | `CONDITIONAL_JUMP`
<a id="insn-00becdbc"></a> `00becdbc` | `4b fd 41 d3` | lsr x11,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00becdc0"></a> `00becdc0` | `ec 03 0b aa` | mov x12,x11 | `FALL_THROUGH`
<a id="insn-00becdc4"></a> `00becdc4` | `05 00 00 14` | b 0x00becdd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00becdc8"></a> `00becdc8` | `0f 02 00 b9` | str w15,[x16] | `FALL_THROUGH`
<a id="insn-00becdcc"></a> `00becdcc` | `9f 01 00 f1` | cmp x12,#0x0 | `FALL_THROUGH`
<a id="insn-00becdd0"></a> `00becdd0` | `8c 05 00 d1` | sub x12,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00becdd4"></a> `00becdd4` | `2d 06 00 54` | b.le 0x00bece98 | `CONDITIONAL_JUMP`
<a id="insn-00becdd8"></a> `00becdd8` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-00becddc"></a> `00becddc` | `8b ff ff 54` | b.lt 0x00becdcc | `CONDITIONAL_JUMP`
<a id="insn-00becde0"></a> `00becde0` | `2e 00 80 52` | mov w14,#0x1 | `FALL_THROUGH`
<a id="insn-00becde4"></a> `00becde4` | `8d f5 7f d3` | ubfiz x13,x12,#0x1,#0x3e | `FALL_THROUGH`
<a id="insn-00becde8"></a> `00becde8` | `8e f5 7f b3` | bfm x14,x12,#0x3f,#0x3d | `FALL_THROUGH`
<a id="insn-00becdec"></a> `00becdec` | `af 09 00 91` | add x15,x13,#0x2 | `FALL_THROUGH`
<a id="insn-00becdf0"></a> `00becdf0` | `0d 08 0e 8b` | add x13,x0,x14, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00becdf4"></a> `00becdf4` | `ff 01 08 eb` | cmp x15,x8 | `FALL_THROUGH`
<a id="insn-00becdf8"></a> `00becdf8` | `2a 01 00 54` | b.ge 0x00bece1c | `CONDITIONAL_JUMP`
<a id="insn-00becdfc"></a> `00becdfc` | `f0 03 0d aa` | mov x16,x13 | `FALL_THROUGH`
<a id="insn-00bece00"></a> `00bece00` | `b1 01 40 b9` | ldr w17,[x13] | `FALL_THROUGH`
<a id="insn-00bece04"></a> `00bece04` | `03 4e 40 b8` | ldr w3,[x16, #0x4]! | `FALL_THROUGH`
<a id="insn-00bece08"></a> `00bece08` | `3f 02 03 6b` | cmp w17,w3 | `FALL_THROUGH`
<a id="insn-00bece0c"></a> `00bece0c` | `31 c2 83 1a` | csel w17,w17,w3,gt | `FALL_THROUGH`
<a id="insn-00bece10"></a> `00bece10` | `0d b2 8d 9a` | csel x13,x16,x13,lt | `FALL_THROUGH`
<a id="insn-00bece14"></a> `00bece14` | `ee b1 8e 9a` | csel x14,x15,x14,lt | `FALL_THROUGH`
<a id="insn-00bece18"></a> `00bece18` | `02 00 00 14` | b 0x00bece20 | `UNCONDITIONAL_JUMP`
<a id="insn-00bece1c"></a> `00bece1c` | `b1 01 40 b9` | ldr w17,[x13] | `FALL_THROUGH`
<a id="insn-00bece20"></a> `00bece20` | `10 08 0c 8b` | add x16,x0,x12, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bece24"></a> `00bece24` | `0f 02 40 b9` | ldr w15,[x16] | `FALL_THROUGH`
<a id="insn-00bece28"></a> `00bece28` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bece2c"></a> `00bece2c` | `6a 01 00 54` | b.ge 0x00bece58 | `CONDITIONAL_JUMP`
<a id="insn-00bece30"></a> `00bece30` | `e7 ff ff 17` | b 0x00becdcc | `UNCONDITIONAL_JUMP`
<a id="insn-00bece34"></a> `00bece34` | `e4 03 0d aa` | mov x4,x13 | `FALL_THROUGH`
<a id="insn-00bece38"></a> `00bece38` | `b1 01 40 b9` | ldr w17,[x13] | `FALL_THROUGH`
<a id="insn-00bece3c"></a> `00bece3c` | `85 4c 40 b8` | ldr w5,[x4, #0x4]! | `FALL_THROUGH`
<a id="insn-00bece40"></a> `00bece40` | `3f 02 05 6b` | cmp w17,w5 | `FALL_THROUGH`
<a id="insn-00bece44"></a> `00bece44` | `31 c2 85 1a` | csel w17,w17,w5,gt | `FALL_THROUGH`
<a id="insn-00bece48"></a> `00bece48` | `8d b0 8d 9a` | csel x13,x4,x13,lt | `FALL_THROUGH`
<a id="insn-00bece4c"></a> `00bece4c` | `ce b1 83 9a` | csel x14,x14,x3,lt | `FALL_THROUGH`
<a id="insn-00bece50"></a> `00bece50` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bece54"></a> `00bece54` | `ab fb ff 54` | b.lt 0x00becdc8 | `CONDITIONAL_JUMP`
<a id="insn-00bece58"></a> `00bece58` | `7f 01 0e eb` | cmp x11,x14 | `FALL_THROUGH`
<a id="insn-00bece5c"></a> `00bece5c` | `11 02 00 b9` | str w17,[x16] | `FALL_THROUGH`
<a id="insn-00bece60"></a> `00bece60` | `f0 03 0d aa` | mov x16,x13 | `FALL_THROUGH`
<a id="insn-00bece64"></a> `00bece64` | `2b fb ff 54` | b.lt 0x00becdc8 | `CONDITIONAL_JUMP`
<a id="insn-00bece68"></a> `00bece68` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bece6c"></a> `00bece6c` | `cd f9 7f d3` | lsl x13,x14,#0x1 | `FALL_THROUGH`
<a id="insn-00bece70"></a> `00bece70` | `c3 f9 7f b3` | bfm x3,x14,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bece74"></a> `00bece74` | `ae 09 00 91` | add x14,x13,#0x2 | `FALL_THROUGH`
<a id="insn-00bece78"></a> `00bece78` | `0d 08 03 8b` | add x13,x0,x3, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bece7c"></a> `00bece7c` | `df 01 08 eb` | cmp x14,x8 | `FALL_THROUGH`
<a id="insn-00bece80"></a> `00bece80` | `ab fd ff 54` | b.lt 0x00bece34 | `CONDITIONAL_JUMP`
<a id="insn-00bece84"></a> `00bece84` | `b1 01 40 b9` | ldr w17,[x13] | `FALL_THROUGH`
<a id="insn-00bece88"></a> `00bece88` | `ee 03 03 aa` | mov x14,x3 | `FALL_THROUGH`
<a id="insn-00bece8c"></a> `00bece8c` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bece90"></a> `00bece90` | `4a fe ff 54` | b.ge 0x00bece58 | `CONDITIONAL_JUMP`
<a id="insn-00bece94"></a> `00bece94` | `cd ff ff 17` | b 0x00becdc8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bece98"></a> `00bece98` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-00bece9c"></a> `00bece9c` | `e3 03 01 aa` | mov x3,x1 | `FALL_THROUGH`
<a id="insn-00becea0"></a> `00becea0` | `c0 07 00 54` | b.eq 0x00becf98 | `CONDITIONAL_JUMP`
<a id="insn-00becea4"></a> `00becea4` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00becea8"></a> `00becea8` | `0b 10 00 91` | add x11,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00beceac"></a> `00beceac` | `0c 20 00 91` | add x12,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00beceb0"></a> `00beceb0` | `2d 00 80 52` | mov w13,#0x1 | `FALL_THROUGH`
<a id="insn-00beceb4"></a> `00beceb4` | `ee 03 01 aa` | mov x14,x1 | `FALL_THROUGH`
<a id="insn-00beceb8"></a> `00beceb8` | `05 00 00 14` | b 0x00bececc | `UNCONDITIONAL_JUMP`
<a id="insn-00becebc"></a> `00becebc` | `6f 00 00 b9` | str w15,[x3] | `FALL_THROUGH`
<a id="insn-00becec0"></a> `00becec0` | `ce 11 00 91` | add x14,x14,#0x4 | `FALL_THROUGH`
<a id="insn-00becec4"></a> `00becec4` | `df 01 02 eb` | cmp x14,x2 | `FALL_THROUGH`
<a id="insn-00becec8"></a> `00becec8` | `60 06 00 54` | b.eq 0x00becf94 | `CONDITIONAL_JUMP`
<a id="insn-00bececc"></a> `00bececc` | `cf 01 40 b9` | ldr w15,[x14] | `FALL_THROUGH`
<a id="insn-00beced0"></a> `00beced0` | `10 00 40 b9` | ldr w16,[x0] | `FALL_THROUGH`
<a id="insn-00beced4"></a> `00beced4` | `ff 01 10 6b` | cmp w15,w16 | `FALL_THROUGH`
<a id="insn-00beced8"></a> `00beced8` | `4a ff ff 54` | b.ge 0x00becec0 | `CONDITIONAL_JUMP`
<a id="insn-00becedc"></a> `00becedc` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00becee0"></a> `00becee0` | `d0 01 00 b9` | str w16,[x14] | `FALL_THROUGH`
<a id="insn-00becee4"></a> `00becee4` | `0f 00 00 b9` | str w15,[x0] | `FALL_THROUGH`
<a id="insn-00becee8"></a> `00becee8` | `cb fe ff 54` | b.lt 0x00becec0 | `CONDITIONAL_JUMP`
<a id="insn-00beceec"></a> `00beceec` | `71 01 40 b9` | ldr w17,[x11] | `FALL_THROUGH`
<a id="insn-00becef0"></a> `00becef0` | `3f 21 00 f1` | cmp x9,#0x8 | `FALL_THROUGH`
<a id="insn-00becef4"></a> `00becef4` | `c1 00 00 54` | b.ne 0x00becf0c | `CONDITIONAL_JUMP`
<a id="insn-00becef8"></a> `00becef8` | `f0 03 0b aa` | mov x16,x11 | `FALL_THROUGH`
<a id="insn-00becefc"></a> `00becefc` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-00becf00"></a> `00becf00` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00becf04"></a> `00becf04` | `eb fd ff 54` | b.lt 0x00becec0 | `CONDITIONAL_JUMP`
<a id="insn-00becf08"></a> `00becf08` | `08 00 00 14` | b 0x00becf28 | `UNCONDITIONAL_JUMP`
<a id="insn-00becf0c"></a> `00becf0c` | `90 01 40 b9` | ldr w16,[x12] | `FALL_THROUGH`
<a id="insn-00becf10"></a> `00becf10` | `3f 02 10 6b` | cmp w17,w16 | `FALL_THROUGH`
<a id="insn-00becf14"></a> `00becf14` | `31 c2 90 1a` | csel w17,w17,w16,gt | `FALL_THROUGH`
<a id="insn-00becf18"></a> `00becf18` | `90 b1 8b 9a` | csel x16,x12,x11,lt | `FALL_THROUGH`
<a id="insn-00becf1c"></a> `00becf1c` | `a4 a5 8d 9a` | cinc x4,x13,lt | `FALL_THROUGH`
<a id="insn-00becf20"></a> `00becf20` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00becf24"></a> `00becf24` | `eb fc ff 54` | b.lt 0x00becec0 | `CONDITIONAL_JUMP`
<a id="insn-00becf28"></a> `00becf28` | `e3 03 00 aa` | mov x3,x0 | `FALL_THROUGH`
<a id="insn-00becf2c"></a> `00becf2c` | `0a 00 00 14` | b 0x00becf54 | `UNCONDITIONAL_JUMP`
<a id="insn-00becf30"></a> `00becf30` | `e6 03 10 aa` | mov x6,x16 | `FALL_THROUGH`
<a id="insn-00becf34"></a> `00becf34` | `11 02 40 b9` | ldr w17,[x16] | `FALL_THROUGH`
<a id="insn-00becf38"></a> `00becf38` | `c7 4c 40 b8` | ldr w7,[x6, #0x4]! | `FALL_THROUGH`
<a id="insn-00becf3c"></a> `00becf3c` | `3f 02 07 6b` | cmp w17,w7 | `FALL_THROUGH`
<a id="insn-00becf40"></a> `00becf40` | `31 c2 87 1a` | csel w17,w17,w7,gt | `FALL_THROUGH`
<a id="insn-00becf44"></a> `00becf44` | `d0 b0 90 9a` | csel x16,x6,x16,lt | `FALL_THROUGH`
<a id="insn-00becf48"></a> `00becf48` | `84 b0 85 9a` | csel x4,x4,x5,lt | `FALL_THROUGH`
<a id="insn-00becf4c"></a> `00becf4c` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00becf50"></a> `00becf50` | `6b fb ff 54` | b.lt 0x00becebc | `CONDITIONAL_JUMP`
<a id="insn-00becf54"></a> `00becf54` | `5f 01 04 eb` | cmp x10,x4 | `FALL_THROUGH`
<a id="insn-00becf58"></a> `00becf58` | `71 00 00 b9` | str w17,[x3] | `FALL_THROUGH`
<a id="insn-00becf5c"></a> `00becf5c` | `e3 03 10 aa` | mov x3,x16 | `FALL_THROUGH`
<a id="insn-00becf60"></a> `00becf60` | `eb fa ff 54` | b.lt 0x00becebc | `CONDITIONAL_JUMP`
<a id="insn-00becf64"></a> `00becf64` | `25 00 80 52` | mov w5,#0x1 | `FALL_THROUGH`
<a id="insn-00becf68"></a> `00becf68` | `90 f8 7f d3` | lsl x16,x4,#0x1 | `FALL_THROUGH`
<a id="insn-00becf6c"></a> `00becf6c` | `85 f8 7f b3` | bfm x5,x4,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00becf70"></a> `00becf70` | `04 0a 00 91` | add x4,x16,#0x2 | `FALL_THROUGH`
<a id="insn-00becf74"></a> `00becf74` | `10 08 05 8b` | add x16,x0,x5, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00becf78"></a> `00becf78` | `9f 00 08 eb` | cmp x4,x8 | `FALL_THROUGH`
<a id="insn-00becf7c"></a> `00becf7c` | `ab fd ff 54` | b.lt 0x00becf30 | `CONDITIONAL_JUMP`
<a id="insn-00becf80"></a> `00becf80` | `11 02 40 b9` | ldr w17,[x16] | `FALL_THROUGH`
<a id="insn-00becf84"></a> `00becf84` | `e4 03 05 aa` | mov x4,x5 | `FALL_THROUGH`
<a id="insn-00becf88"></a> `00becf88` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00becf8c"></a> `00becf8c` | `4a fe ff 54` | b.ge 0x00becf54 | `CONDITIONAL_JUMP`
<a id="insn-00becf90"></a> `00becf90` | `cb ff ff 17` | b 0x00becebc | `UNCONDITIONAL_JUMP`
<a id="insn-00becf94"></a> `00becf94` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00becf98"></a> `00becf98` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00becf9c"></a> `00becf9c` | `0a 01 00 54` | b.ge 0x00becfbc | `CONDITIONAL_JUMP`
<a id="insn-00becfa0"></a> `00becfa0` | `e2 03 03 aa` | mov x2,x3 | `FALL_THROUGH`
<a id="insn-00becfa4"></a> `00becfa4` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00becfa8"></a> `00becfa8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00becfac"></a> `00becfac` | `2a 01 00 b9` | str w10,[x9] | `FALL_THROUGH`
<a id="insn-00becfb0"></a> `00becfb0` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00becfb4"></a> `00becfb4` | `08 05 00 d1` | sub x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00becfb8"></a> `00becfb8` | `4d ff ff 54` | b.le 0x00becfa0 | `CONDITIONAL_JUMP`
<a id="insn-00becfbc"></a> `00becfbc` | `09 09 00 d1` | sub x9,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00becfc0"></a> `00becfc0` | `0a 00 40 b9` | ldr w10,[x0] | `FALL_THROUGH`
<a id="insn-00becfc4"></a> `00becfc4` | `ed 03 1f aa` | mov x13,xzr | `FALL_THROUGH`
<a id="insn-00becfc8"></a> `00becfc8` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00becfcc"></a> `00becfcc` | `ec 03 00 aa` | mov x12,x0 | `FALL_THROUGH`
<a id="insn-00becfd0"></a> `00becfd0` | `0b 00 00 14` | b 0x00becffc | `UNCONDITIONAL_JUMP`
<a id="insn-00becfd4"></a> `00becfd4` | `0d 8e 40 b8` | ldr w13,[x16, #0x8]! | `FALL_THROUGH`
<a id="insn-00becfd8"></a> `00becfd8` | `0f c2 5f b8` | ldur w15,[x16, #-0x4] | `FALL_THROUGH`
<a id="insn-00becfdc"></a> `00becfdc` | `ff 01 0d 6b` | cmp w15,w13 | `FALL_THROUGH`
<a id="insn-00becfe0"></a> `00becfe0` | `ef c1 8d 1a` | csel w15,w15,w13,gt | `FALL_THROUGH`
<a id="insn-00becfe4"></a> `00becfe4` | `09 b2 89 9a` | csel x9,x16,x9,lt | `FALL_THROUGH`
<a id="insn-00becfe8"></a> `00becfe8` | `2d b2 8e 9a` | csel x13,x17,x14,lt | `FALL_THROUGH`
<a id="insn-00becfec"></a> `00becfec` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00becff0"></a> `00becff0` | `8f 01 00 b9` | str w15,[x12] | `FALL_THROUGH`
<a id="insn-00becff4"></a> `00becff4` | `ec 03 09 aa` | mov x12,x9 | `FALL_THROUGH`
<a id="insn-00becff8"></a> `00becff8` | `8c 01 00 54` | b.gt 0x00bed028 | `CONDITIONAL_JUMP`
<a id="insn-00becffc"></a> `00becffc` | `a9 f9 7f d3` | lsl x9,x13,#0x1 | `FALL_THROUGH`
<a id="insn-00bed000"></a> `00bed000` | `90 09 0d 8b` | add x16,x12,x13, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bed004"></a> `00bed004` | `2e 00 80 52` | mov w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bed008"></a> `00bed008` | `ae f9 7f b3` | bfm x14,x13,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bed00c"></a> `00bed00c` | `31 09 00 91` | add x17,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bed010"></a> `00bed010` | `09 12 00 91` | add x9,x16,#0x4 | `FALL_THROUGH`
<a id="insn-00bed014"></a> `00bed014` | `3f 02 08 eb` | cmp x17,x8 | `FALL_THROUGH`
<a id="insn-00bed018"></a> `00bed018` | `eb fd ff 54` | b.lt 0x00becfd4 | `CONDITIONAL_JUMP`
<a id="insn-00bed01c"></a> `00bed01c` | `2f 01 40 b9` | ldr w15,[x9] | `FALL_THROUGH`
<a id="insn-00bed020"></a> `00bed020` | `ed 03 0e aa` | mov x13,x14 | `FALL_THROUGH`
<a id="insn-00bed024"></a> `00bed024` | `f2 ff ff 17` | b 0x00becfec | `UNCONDITIONAL_JUMP`
<a id="insn-00bed028"></a> `00bed028` | `21 10 00 d1` | sub x1,x1,#0x4 | `FALL_THROUGH`
<a id="insn-00bed02c"></a> `00bed02c` | `3f 01 01 eb` | cmp x9,x1 | `FALL_THROUGH`
<a id="insn-00bed030"></a> `00bed030` | `e0 fb ff 54` | b.eq 0x00becfac | `CONDITIONAL_JUMP`
<a id="insn-00bed034"></a> `00bed034` | `2b 01 00 cb` | sub x11,x9,x0 | `FALL_THROUGH`
<a id="insn-00bed038"></a> `00bed038` | `2c 00 40 b9` | ldr w12,[x1] | `FALL_THROUGH`
<a id="insn-00bed03c"></a> `00bed03c` | `6b 11 00 91` | add x11,x11,#0x4 | `FALL_THROUGH`
<a id="insn-00bed040"></a> `00bed040` | `6b fd 42 93` | asr x11,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00bed044"></a> `00bed044` | `2c 01 00 b9` | str w12,[x9] | `FALL_THROUGH`
<a id="insn-00bed048"></a> `00bed048` | `2a 00 00 b9` | str w10,[x1] | `FALL_THROUGH`
<a id="insn-00bed04c"></a> `00bed04c` | `6b 09 00 f1` | subs x11,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00bed050"></a> `00bed050` | `0b fb ff 54` | b.lt 0x00becfb0 | `CONDITIONAL_JUMP`
<a id="insn-00bed054"></a> `00bed054` | `6a fd 41 d3` | lsr x10,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00bed058"></a> `00bed058` | `2b 01 40 b9` | ldr w11,[x9] | `FALL_THROUGH`
<a id="insn-00bed05c"></a> `00bed05c` | `0c 08 0a 8b` | add x12,x0,x10, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bed060"></a> `00bed060` | `8d 01 40 b9` | ldr w13,[x12] | `FALL_THROUGH`
<a id="insn-00bed064"></a> `00bed064` | `bf 01 0b 6b` | cmp w13,w11 | `FALL_THROUGH`
<a id="insn-00bed068"></a> `00bed068` | `4a fa ff 54` | b.ge 0x00becfb0 | `CONDITIONAL_JUMP`
<a id="insn-00bed06c"></a> `00bed06c` | `ee 03 09 aa` | mov x14,x9 | `FALL_THROUGH`
<a id="insn-00bed070"></a> `00bed070` | `e9 03 0c aa` | mov x9,x12 | `FALL_THROUGH`
<a id="insn-00bed074"></a> `00bed074` | `cd 01 00 b9` | str w13,[x14] | `FALL_THROUGH`
<a id="insn-00bed078"></a> `00bed078` | `ea 00 00 b4` | cbz x10,0x00bed094 | `CONDITIONAL_JUMP`
<a id="insn-00bed07c"></a> `00bed07c` | `4a 05 00 d1` | sub x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bed080"></a> `00bed080` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bed084"></a> `00bed084` | `0c 08 0a 8b` | add x12,x0,x10, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bed088"></a> `00bed088` | `8d 01 40 b9` | ldr w13,[x12] | `FALL_THROUGH`
<a id="insn-00bed08c"></a> `00bed08c` | `bf 01 0b 6b` | cmp w13,w11 | `FALL_THROUGH`
<a id="insn-00bed090"></a> `00bed090` | `eb fe ff 54` | b.lt 0x00bed06c | `CONDITIONAL_JUMP`
<a id="insn-00bed094"></a> `00bed094` | `2b 01 00 b9` | str w11,[x9] | `FALL_THROUGH`
<a id="insn-00bed098"></a> `00bed098` | `c6 ff ff 17` | b 0x00becfb0 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00becda0`](#insn-00becda0) 範囲 `[['00becda0', '00becdab']]`
  - `CONDITIONAL_JUMP` [`00becda8`](#insn-00becda8) → [`00becfa4`](#insn-00becfa4)
  - `FALL_THROUGH` [`00becda8`](#insn-00becda8) → [`00becdac`](#insn-00becdac)
- ブロック [`00becdac`](#insn-00becdac) 範囲 `[['00becdac', '00becdbb']]`
  - `CONDITIONAL_JUMP` [`00becdb8`](#insn-00becdb8) → [`00bece98`](#insn-00bece98)
  - `FALL_THROUGH` [`00becdb8`](#insn-00becdb8) → [`00becdbc`](#insn-00becdbc)
- ブロック [`00becdbc`](#insn-00becdbc) 範囲 `[['00becdbc', '00becdc7']]`
  - `UNCONDITIONAL_JUMP` [`00becdc4`](#insn-00becdc4) → [`00becdd8`](#insn-00becdd8)
- ブロック [`00becdc8`](#insn-00becdc8) 範囲 `[['00becdc8', '00becdcb']]`
  - `FALL_THROUGH` [`00becdc8`](#insn-00becdc8) → [`00becdcc`](#insn-00becdcc)
- ブロック [`00becdcc`](#insn-00becdcc) 範囲 `[['00becdcc', '00becdd7']]`
  - `CONDITIONAL_JUMP` [`00becdd4`](#insn-00becdd4) → [`00bece98`](#insn-00bece98)
  - `FALL_THROUGH` [`00becdd4`](#insn-00becdd4) → [`00becdd8`](#insn-00becdd8)
- ブロック [`00becdd8`](#insn-00becdd8) 範囲 `[['00becdd8', '00becddf']]`
  - `CONDITIONAL_JUMP` [`00becddc`](#insn-00becddc) → [`00becdcc`](#insn-00becdcc)
  - `FALL_THROUGH` [`00becddc`](#insn-00becddc) → [`00becde0`](#insn-00becde0)
- ブロック [`00becde0`](#insn-00becde0) 範囲 `[['00becde0', '00becdfb']]`
  - `CONDITIONAL_JUMP` [`00becdf8`](#insn-00becdf8) → [`00bece1c`](#insn-00bece1c)
  - `FALL_THROUGH` [`00becdf8`](#insn-00becdf8) → [`00becdfc`](#insn-00becdfc)
- ブロック [`00becdfc`](#insn-00becdfc) 範囲 `[['00becdfc', '00bece17']]`
  - `FALL_THROUGH` [`00bece14`](#insn-00bece14) → [`00bece18`](#insn-00bece18)
- ブロック [`00bece18`](#insn-00bece18) 範囲 `[['00bece18', '00bece1b']]`
  - `UNCONDITIONAL_JUMP` [`00bece18`](#insn-00bece18) → [`00bece20`](#insn-00bece20)
- ブロック [`00bece1c`](#insn-00bece1c) 範囲 `[['00bece1c', '00bece1f']]`
  - `FALL_THROUGH` [`00bece1c`](#insn-00bece1c) → [`00bece20`](#insn-00bece20)
- ブロック [`00bece20`](#insn-00bece20) 範囲 `[['00bece20', '00bece2f']]`
  - `CONDITIONAL_JUMP` [`00bece2c`](#insn-00bece2c) → [`00bece58`](#insn-00bece58)
  - `FALL_THROUGH` [`00bece2c`](#insn-00bece2c) → [`00bece30`](#insn-00bece30)
- ブロック [`00bece30`](#insn-00bece30) 範囲 `[['00bece30', '00bece33']]`
  - `UNCONDITIONAL_JUMP` [`00bece30`](#insn-00bece30) → [`00becdcc`](#insn-00becdcc)
- ブロック [`00bece34`](#insn-00bece34) 範囲 `[['00bece34', '00bece57']]`
  - `CONDITIONAL_JUMP` [`00bece54`](#insn-00bece54) → [`00becdc8`](#insn-00becdc8)
  - `FALL_THROUGH` [`00bece54`](#insn-00bece54) → [`00bece58`](#insn-00bece58)
- ブロック [`00bece58`](#insn-00bece58) 範囲 `[['00bece58', '00bece67']]`
  - `CONDITIONAL_JUMP` [`00bece64`](#insn-00bece64) → [`00becdc8`](#insn-00becdc8)
  - `FALL_THROUGH` [`00bece64`](#insn-00bece64) → [`00bece68`](#insn-00bece68)
- ブロック [`00bece68`](#insn-00bece68) 範囲 `[['00bece68', '00bece83']]`
  - `CONDITIONAL_JUMP` [`00bece80`](#insn-00bece80) → [`00bece34`](#insn-00bece34)
  - `FALL_THROUGH` [`00bece80`](#insn-00bece80) → [`00bece84`](#insn-00bece84)
- ブロック [`00bece84`](#insn-00bece84) 範囲 `[['00bece84', '00bece93']]`
  - `CONDITIONAL_JUMP` [`00bece90`](#insn-00bece90) → [`00bece58`](#insn-00bece58)
  - `FALL_THROUGH` [`00bece90`](#insn-00bece90) → [`00bece94`](#insn-00bece94)
- ブロック [`00bece94`](#insn-00bece94) 範囲 `[['00bece94', '00bece97']]`
  - `UNCONDITIONAL_JUMP` [`00bece94`](#insn-00bece94) → [`00becdc8`](#insn-00becdc8)
- ブロック [`00bece98`](#insn-00bece98) 範囲 `[['00bece98', '00becea3']]`
  - `CONDITIONAL_JUMP` [`00becea0`](#insn-00becea0) → [`00becf98`](#insn-00becf98)
  - `FALL_THROUGH` [`00becea0`](#insn-00becea0) → [`00becea4`](#insn-00becea4)
- ブロック [`00becea4`](#insn-00becea4) 範囲 `[['00becea4', '00becebb']]`
  - `UNCONDITIONAL_JUMP` [`00beceb8`](#insn-00beceb8) → [`00bececc`](#insn-00bececc)
- ブロック [`00becebc`](#insn-00becebc) 範囲 `[['00becebc', '00becebf']]`
  - `FALL_THROUGH` [`00becebc`](#insn-00becebc) → [`00becec0`](#insn-00becec0)
- ブロック [`00becec0`](#insn-00becec0) 範囲 `[['00becec0', '00bececb']]`
  - `CONDITIONAL_JUMP` [`00becec8`](#insn-00becec8) → [`00becf94`](#insn-00becf94)
  - `FALL_THROUGH` [`00becec8`](#insn-00becec8) → [`00bececc`](#insn-00bececc)
- ブロック [`00bececc`](#insn-00bececc) 範囲 `[['00bececc', '00becedb']]`
  - `CONDITIONAL_JUMP` [`00beced8`](#insn-00beced8) → [`00becec0`](#insn-00becec0)
  - `FALL_THROUGH` [`00beced8`](#insn-00beced8) → [`00becedc`](#insn-00becedc)
- ブロック [`00becedc`](#insn-00becedc) 範囲 `[['00becedc', '00beceeb']]`
  - `CONDITIONAL_JUMP` [`00becee8`](#insn-00becee8) → [`00becec0`](#insn-00becec0)
  - `FALL_THROUGH` [`00becee8`](#insn-00becee8) → [`00beceec`](#insn-00beceec)
- ブロック [`00beceec`](#insn-00beceec) 範囲 `[['00beceec', '00becef7']]`
  - `CONDITIONAL_JUMP` [`00becef4`](#insn-00becef4) → [`00becf0c`](#insn-00becf0c)
  - `FALL_THROUGH` [`00becef4`](#insn-00becef4) → [`00becef8`](#insn-00becef8)
- ブロック [`00becef8`](#insn-00becef8) 範囲 `[['00becef8', '00becf07']]`
  - `CONDITIONAL_JUMP` [`00becf04`](#insn-00becf04) → [`00becec0`](#insn-00becec0)
  - `FALL_THROUGH` [`00becf04`](#insn-00becf04) → [`00becf08`](#insn-00becf08)
- ブロック [`00becf08`](#insn-00becf08) 範囲 `[['00becf08', '00becf0b']]`
  - `UNCONDITIONAL_JUMP` [`00becf08`](#insn-00becf08) → [`00becf28`](#insn-00becf28)
- ブロック [`00becf0c`](#insn-00becf0c) 範囲 `[['00becf0c', '00becf27']]`
  - `CONDITIONAL_JUMP` [`00becf24`](#insn-00becf24) → [`00becec0`](#insn-00becec0)
  - `FALL_THROUGH` [`00becf24`](#insn-00becf24) → [`00becf28`](#insn-00becf28)
- ブロック [`00becf28`](#insn-00becf28) 範囲 `[['00becf28', '00becf2f']]`
  - `UNCONDITIONAL_JUMP` [`00becf2c`](#insn-00becf2c) → [`00becf54`](#insn-00becf54)
- ブロック [`00becf30`](#insn-00becf30) 範囲 `[['00becf30', '00becf53']]`
  - `CONDITIONAL_JUMP` [`00becf50`](#insn-00becf50) → [`00becebc`](#insn-00becebc)
  - `FALL_THROUGH` [`00becf50`](#insn-00becf50) → [`00becf54`](#insn-00becf54)
- ブロック [`00becf54`](#insn-00becf54) 範囲 `[['00becf54', '00becf63']]`
  - `CONDITIONAL_JUMP` [`00becf60`](#insn-00becf60) → [`00becebc`](#insn-00becebc)
  - `FALL_THROUGH` [`00becf60`](#insn-00becf60) → [`00becf64`](#insn-00becf64)
- ブロック [`00becf64`](#insn-00becf64) 範囲 `[['00becf64', '00becf7f']]`
  - `CONDITIONAL_JUMP` [`00becf7c`](#insn-00becf7c) → [`00becf30`](#insn-00becf30)
  - `FALL_THROUGH` [`00becf7c`](#insn-00becf7c) → [`00becf80`](#insn-00becf80)
- ブロック [`00becf80`](#insn-00becf80) 範囲 `[['00becf80', '00becf87']]`
  - `FALL_THROUGH` [`00becf84`](#insn-00becf84) → [`00becf88`](#insn-00becf88)
- ブロック [`00becf88`](#insn-00becf88) 範囲 `[['00becf88', '00becf8f']]`
  - `CONDITIONAL_JUMP` [`00becf8c`](#insn-00becf8c) → [`00becf54`](#insn-00becf54)
  - `FALL_THROUGH` [`00becf8c`](#insn-00becf8c) → [`00becf90`](#insn-00becf90)
- ブロック [`00becf90`](#insn-00becf90) 範囲 `[['00becf90', '00becf93']]`
  - `UNCONDITIONAL_JUMP` [`00becf90`](#insn-00becf90) → [`00becebc`](#insn-00becebc)
- ブロック [`00becf94`](#insn-00becf94) 範囲 `[['00becf94', '00becf97']]`
  - `FALL_THROUGH` [`00becf94`](#insn-00becf94) → [`00becf98`](#insn-00becf98)
- ブロック [`00becf98`](#insn-00becf98) 範囲 `[['00becf98', '00becf9f']]`
  - `CONDITIONAL_JUMP` [`00becf9c`](#insn-00becf9c) → [`00becfbc`](#insn-00becfbc)
  - `FALL_THROUGH` [`00becf9c`](#insn-00becf9c) → [`00becfa0`](#insn-00becfa0)
- ブロック [`00becfa0`](#insn-00becfa0) 範囲 `[['00becfa0', '00becfa3']]`
  - `FALL_THROUGH` [`00becfa0`](#insn-00becfa0) → [`00becfa4`](#insn-00becfa4)
- ブロック [`00becfa4`](#insn-00becfa4) 範囲 `[['00becfa4', '00becfab']]`
- ブロック [`00becfac`](#insn-00becfac) 範囲 `[['00becfac', '00becfaf']]`
  - `FALL_THROUGH` [`00becfac`](#insn-00becfac) → [`00becfb0`](#insn-00becfb0)
- ブロック [`00becfb0`](#insn-00becfb0) 範囲 `[['00becfb0', '00becfbb']]`
  - `CONDITIONAL_JUMP` [`00becfb8`](#insn-00becfb8) → [`00becfa0`](#insn-00becfa0)
  - `FALL_THROUGH` [`00becfb8`](#insn-00becfb8) → [`00becfbc`](#insn-00becfbc)
- ブロック [`00becfbc`](#insn-00becfbc) 範囲 `[['00becfbc', '00becfd3']]`
  - `UNCONDITIONAL_JUMP` [`00becfd0`](#insn-00becfd0) → [`00becffc`](#insn-00becffc)
- ブロック [`00becfd4`](#insn-00becfd4) 範囲 `[['00becfd4', '00becfeb']]`
  - `FALL_THROUGH` [`00becfe8`](#insn-00becfe8) → [`00becfec`](#insn-00becfec)
- ブロック [`00becfec`](#insn-00becfec) 範囲 `[['00becfec', '00becffb']]`
  - `CONDITIONAL_JUMP` [`00becff8`](#insn-00becff8) → [`00bed028`](#insn-00bed028)
  - `FALL_THROUGH` [`00becff8`](#insn-00becff8) → [`00becffc`](#insn-00becffc)
- ブロック [`00becffc`](#insn-00becffc) 範囲 `[['00becffc', '00bed01b']]`
  - `CONDITIONAL_JUMP` [`00bed018`](#insn-00bed018) → [`00becfd4`](#insn-00becfd4)
  - `FALL_THROUGH` [`00bed018`](#insn-00bed018) → [`00bed01c`](#insn-00bed01c)
- ブロック [`00bed01c`](#insn-00bed01c) 範囲 `[['00bed01c', '00bed027']]`
  - `UNCONDITIONAL_JUMP` [`00bed024`](#insn-00bed024) → [`00becfec`](#insn-00becfec)
- ブロック [`00bed028`](#insn-00bed028) 範囲 `[['00bed028', '00bed033']]`
  - `CONDITIONAL_JUMP` [`00bed030`](#insn-00bed030) → [`00becfac`](#insn-00becfac)
  - `FALL_THROUGH` [`00bed030`](#insn-00bed030) → [`00bed034`](#insn-00bed034)
- ブロック [`00bed034`](#insn-00bed034) 範囲 `[['00bed034', '00bed053']]`
  - `CONDITIONAL_JUMP` [`00bed050`](#insn-00bed050) → [`00becfb0`](#insn-00becfb0)
  - `FALL_THROUGH` [`00bed050`](#insn-00bed050) → [`00bed054`](#insn-00bed054)
- ブロック [`00bed054`](#insn-00bed054) 範囲 `[['00bed054', '00bed06b']]`
  - `CONDITIONAL_JUMP` [`00bed068`](#insn-00bed068) → [`00becfb0`](#insn-00becfb0)
  - `FALL_THROUGH` [`00bed068`](#insn-00bed068) → [`00bed06c`](#insn-00bed06c)
- ブロック [`00bed06c`](#insn-00bed06c) 範囲 `[['00bed06c', '00bed07b']]`
  - `CONDITIONAL_JUMP` [`00bed078`](#insn-00bed078) → [`00bed094`](#insn-00bed094)
  - `FALL_THROUGH` [`00bed078`](#insn-00bed078) → [`00bed07c`](#insn-00bed07c)
- ブロック [`00bed07c`](#insn-00bed07c) 範囲 `[['00bed07c', '00bed093']]`
  - `CONDITIONAL_JUMP` [`00bed090`](#insn-00bed090) → [`00bed06c`](#insn-00bed06c)
  - `FALL_THROUGH` [`00bed090`](#insn-00bed090) → [`00bed094`](#insn-00bed094)
- ブロック [`00bed094`](#insn-00bed094) 範囲 `[['00bed094', '00bed09b']]`
  - `UNCONDITIONAL_JUMP` [`00bed098`](#insn-00bed098) → [`00becfb0`](#insn-00becfb0)

## 命令位置別の参照

- [`00becda8`](#insn-00becda8) → [`00becfa4`](#insn-00becfa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becdb8`](#insn-00becdb8) → [`00bece98`](#insn-00bece98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becdc4`](#insn-00becdc4) → [`00becdd8`](#insn-00becdd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becdd4`](#insn-00becdd4) → [`00bece98`](#insn-00bece98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becddc`](#insn-00becddc) → [`00becdcc`](#insn-00becdcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becdf8`](#insn-00becdf8) → [`00bece1c`](#insn-00bece1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bece18`](#insn-00bece18) → [`00bece20`](#insn-00bece20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bece2c`](#insn-00bece2c) → [`00bece58`](#insn-00bece58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bece30`](#insn-00bece30) → [`00becdcc`](#insn-00becdcc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bece54`](#insn-00bece54) → [`00becdc8`](#insn-00becdc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bece64`](#insn-00bece64) → [`00becdc8`](#insn-00becdc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bece80`](#insn-00bece80) → [`00bece34`](#insn-00bece34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bece90`](#insn-00bece90) → [`00bece58`](#insn-00bece58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bece94`](#insn-00bece94) → [`00becdc8`](#insn-00becdc8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becea0`](#insn-00becea0) → [`00becf98`](#insn-00becf98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beceb8`](#insn-00beceb8) → [`00bececc`](#insn-00bececc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becec8`](#insn-00becec8) → [`00becf94`](#insn-00becf94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beced8`](#insn-00beced8) → [`00becec0`](#insn-00becec0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becee8`](#insn-00becee8) → [`00becec0`](#insn-00becec0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becef4`](#insn-00becef4) → [`00becf0c`](#insn-00becf0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becf04`](#insn-00becf04) → [`00becec0`](#insn-00becec0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becf08`](#insn-00becf08) → [`00becf28`](#insn-00becf28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becf24`](#insn-00becf24) → [`00becec0`](#insn-00becec0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becf2c`](#insn-00becf2c) → [`00becf54`](#insn-00becf54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becf50`](#insn-00becf50) → [`00becebc`](#insn-00becebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becf60`](#insn-00becf60) → [`00becebc`](#insn-00becebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becf7c`](#insn-00becf7c) → [`00becf30`](#insn-00becf30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becf8c`](#insn-00becf8c) → [`00becf54`](#insn-00becf54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becf90`](#insn-00becf90) → [`00becebc`](#insn-00becebc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becf9c`](#insn-00becf9c) → [`00becfbc`](#insn-00becfbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becfb8`](#insn-00becfb8) → [`00becfa0`](#insn-00becfa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becfd0`](#insn-00becfd0) → [`00becffc`](#insn-00becffc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00becff8`](#insn-00becff8) → [`00bed028`](#insn-00bed028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bed018`](#insn-00bed018) → [`00becfd4`](#insn-00becfd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bed024`](#insn-00bed024) → [`00becfec`](#insn-00becfec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bed030`](#insn-00bed030) → [`00becfac`](#insn-00becfac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bed050`](#insn-00bed050) → [`00becfb0`](#insn-00becfb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bed068`](#insn-00bed068) → [`00becfb0`](#insn-00becfb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bed078`](#insn-00bed078) → [`00bed094`](#insn-00bed094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bed090`](#insn-00bed090) → [`00bed06c`](#insn-00bed06c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bed098`](#insn-00bed098) → [`00becfb0`](#insn-00becfb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00becda8`](#insn-00becda8)

~~~json
{
  "source": "00becda8",
  "target": "00becfa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becdb8`](#insn-00becdb8)

~~~json
{
  "source": "00becdb8",
  "target": "00bece98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becdc4`](#insn-00becdc4)

~~~json
{
  "source": "00becdc4",
  "target": "00becdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becdd4`](#insn-00becdd4)

~~~json
{
  "source": "00becdd4",
  "target": "00bece98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becddc`](#insn-00becddc)

~~~json
{
  "source": "00becddc",
  "target": "00becdcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becdf8`](#insn-00becdf8)

~~~json
{
  "source": "00becdf8",
  "target": "00bece1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bece18`](#insn-00bece18)

~~~json
{
  "source": "00bece18",
  "target": "00bece20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bece2c`](#insn-00bece2c)

~~~json
{
  "source": "00bece2c",
  "target": "00bece58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bece30`](#insn-00bece30)

~~~json
{
  "source": "00bece30",
  "target": "00becdcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bece54`](#insn-00bece54)

~~~json
{
  "source": "00bece54",
  "target": "00becdc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bece64`](#insn-00bece64)

~~~json
{
  "source": "00bece64",
  "target": "00becdc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bece80`](#insn-00bece80)

~~~json
{
  "source": "00bece80",
  "target": "00bece34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bece90`](#insn-00bece90)

~~~json
{
  "source": "00bece90",
  "target": "00bece58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bece94`](#insn-00bece94)

~~~json
{
  "source": "00bece94",
  "target": "00becdc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becea0`](#insn-00becea0)

~~~json
{
  "source": "00becea0",
  "target": "00becf98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beceb8`](#insn-00beceb8)

~~~json
{
  "source": "00beceb8",
  "target": "00bececc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becec8`](#insn-00becec8)

~~~json
{
  "source": "00becec8",
  "target": "00becf94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beced8`](#insn-00beced8)

~~~json
{
  "source": "00beced8",
  "target": "00becec0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becee8`](#insn-00becee8)

~~~json
{
  "source": "00becee8",
  "target": "00becec0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becef4`](#insn-00becef4)

~~~json
{
  "source": "00becef4",
  "target": "00becf0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becf04`](#insn-00becf04)

~~~json
{
  "source": "00becf04",
  "target": "00becec0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becf08`](#insn-00becf08)

~~~json
{
  "source": "00becf08",
  "target": "00becf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becf24`](#insn-00becf24)

~~~json
{
  "source": "00becf24",
  "target": "00becec0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becf2c`](#insn-00becf2c)

~~~json
{
  "source": "00becf2c",
  "target": "00becf54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becf50`](#insn-00becf50)

~~~json
{
  "source": "00becf50",
  "target": "00becebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becf60`](#insn-00becf60)

~~~json
{
  "source": "00becf60",
  "target": "00becebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becf7c`](#insn-00becf7c)

~~~json
{
  "source": "00becf7c",
  "target": "00becf30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becf8c`](#insn-00becf8c)

~~~json
{
  "source": "00becf8c",
  "target": "00becf54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becf90`](#insn-00becf90)

~~~json
{
  "source": "00becf90",
  "target": "00becebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becf9c`](#insn-00becf9c)

~~~json
{
  "source": "00becf9c",
  "target": "00becfbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becfb8`](#insn-00becfb8)

~~~json
{
  "source": "00becfb8",
  "target": "00becfa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becfd0`](#insn-00becfd0)

~~~json
{
  "source": "00becfd0",
  "target": "00becffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00becff8`](#insn-00becff8)

~~~json
{
  "source": "00becff8",
  "target": "00bed028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bed018`](#insn-00bed018)

~~~json
{
  "source": "00bed018",
  "target": "00becfd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bed024`](#insn-00bed024)

~~~json
{
  "source": "00bed024",
  "target": "00becfec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bed030`](#insn-00bed030)

~~~json
{
  "source": "00bed030",
  "target": "00becfac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bed050`](#insn-00bed050)

~~~json
{
  "source": "00bed050",
  "target": "00becfb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bed068`](#insn-00bed068)

~~~json
{
  "source": "00bed068",
  "target": "00becfb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bed078`](#insn-00bed078)

~~~json
{
  "source": "00bed078",
  "target": "00bed094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bed090`](#insn-00bed090)

~~~json
{
  "source": "00bed090",
  "target": "00bed06c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bed098`](#insn-00bed098)

~~~json
{
  "source": "00bed098",
  "target": "00becfb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
