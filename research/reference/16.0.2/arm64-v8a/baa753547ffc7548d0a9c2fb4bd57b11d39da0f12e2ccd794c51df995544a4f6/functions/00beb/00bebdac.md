# 00bebdac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bebd10`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00beb/00bebd10.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/no_difference_in_scope-0014.md#compare-0a6abce07dbc0a6c0bab16f4e9088172)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00becda0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00becda0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/no_difference_in_scope-0014.md#compare-4d7b538421d547e97928fbb5d7f62919)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bebdac",
  "name": "FUN_00bebdac",
  "size": 764,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "37d0f9605b8768fcb2fc0d6daacf94c8f7ccd62ee3cea89fd80b6ae3b106eed8",
  "source_text_sha256": "37d0f9605b8768fcb2fc0d6daacf94c8f7ccd62ee3cea89fd80b6ae3b106eed8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bebdac",
        "00bec0a7"
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

- [00be4e34](../00be4/00be4e34.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6640 bytes

~~~c

int * FUN_00bebdac(int *param_1,int *param_2,int *param_3)

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
                    /* try { // try from 00bebe08 to 00cebe23 has its CatchHandler @ 00bebfa4 */
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
                if ((long)uVar10 < (long)uVar14) goto LAB_00bebdd4;
                uVar3 = uVar14 << 1 | 1;
                uVar14 = uVar14 * 2 + 2;
                piVar6 = param_1 + uVar3;
                piVar12 = piVar9;
                if ((long)uVar14 < lVar8) break;
                iVar16 = *piVar6;
                piVar13 = piVar6;
                uVar14 = uVar3;
                if (iVar16 < iVar17) goto LAB_00bebdd4;
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
LAB_00bebdd4:
            *piVar9 = iVar17;
          }
        }
                    /* try { // try from 00bebdd8 to 00cebde3 has its CatchHandler @ 00bebf94 */
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
                  if ((long)(lVar8 - 2U >> 1) < (long)uVar7) goto LAB_00bebec8;
                  uVar10 = uVar7 << 1 | 1;
                  uVar7 = uVar7 * 2 + 2;
                  piVar2 = param_1 + uVar10;
                  piVar6 = piVar15;
                  if ((long)uVar7 < lVar8) break;
                  iVar17 = *piVar2;
                    /* catch() { ... } // from try @ 00bebdd8 with catch @ 00bebf94 */
                  uVar7 = uVar10;
                  piVar12 = piVar2;
                  if (iVar17 < iVar16) goto LAB_00bebec8;
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
LAB_00bebec8:
              *piVar15 = iVar16;
            }
          }
        }
        piVar9 = piVar9 + 1;
        piVar12 = param_3;
      } while (piVar9 != param_3);
    }
                    /* catch() { ... } // from try @ 00bebe08 with catch @ 00bebfa4 */
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
<a id="insn-00bebdac"></a> `00bebdac` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bebdb0"></a> `00bebdb0` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-00bebdb4"></a> `00bebdb4` | `e0 0f 00 54` | b.eq 0x00bebfb0 | `CONDITIONAL_JUMP`
<a id="insn-00bebdb8"></a> `00bebdb8` | `29 00 00 cb` | sub x9,x1,x0 | `FALL_THROUGH`
<a id="insn-00bebdbc"></a> `00bebdbc` | `28 fd 42 93` | asr x8,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bebdc0"></a> `00bebdc0` | `0a 09 00 f1` | subs x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bebdc4"></a> `00bebdc4` | `0b 07 00 54` | b.lt 0x00bebea4 | `CONDITIONAL_JUMP`
<a id="insn-00bebdc8"></a> `00bebdc8` | `4b fd 41 d3` | lsr x11,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bebdcc"></a> `00bebdcc` | `ec 03 0b aa` | mov x12,x11 | `FALL_THROUGH`
<a id="insn-00bebdd0"></a> `00bebdd0` | `05 00 00 14` | b 0x00bebde4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bebdd4"></a> `00bebdd4` | `0f 02 00 b9` | str w15,[x16] | `FALL_THROUGH`
<a id="insn-00bebdd8"></a> `00bebdd8` | `9f 01 00 f1` | cmp x12,#0x0 | `FALL_THROUGH`
<a id="insn-00bebddc"></a> `00bebddc` | `8c 05 00 d1` | sub x12,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00bebde0"></a> `00bebde0` | `2d 06 00 54` | b.le 0x00bebea4 | `CONDITIONAL_JUMP`
<a id="insn-00bebde4"></a> `00bebde4` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-00bebde8"></a> `00bebde8` | `8b ff ff 54` | b.lt 0x00bebdd8 | `CONDITIONAL_JUMP`
<a id="insn-00bebdec"></a> `00bebdec` | `2e 00 80 52` | mov w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bebdf0"></a> `00bebdf0` | `8d f5 7f d3` | ubfiz x13,x12,#0x1,#0x3e | `FALL_THROUGH`
<a id="insn-00bebdf4"></a> `00bebdf4` | `8e f5 7f b3` | bfm x14,x12,#0x3f,#0x3d | `FALL_THROUGH`
<a id="insn-00bebdf8"></a> `00bebdf8` | `af 09 00 91` | add x15,x13,#0x2 | `FALL_THROUGH`
<a id="insn-00bebdfc"></a> `00bebdfc` | `0d 08 0e 8b` | add x13,x0,x14, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bebe00"></a> `00bebe00` | `ff 01 08 eb` | cmp x15,x8 | `FALL_THROUGH`
<a id="insn-00bebe04"></a> `00bebe04` | `2a 01 00 54` | b.ge 0x00bebe28 | `CONDITIONAL_JUMP`
<a id="insn-00bebe08"></a> `00bebe08` | `f0 03 0d aa` | mov x16,x13 | `FALL_THROUGH`
<a id="insn-00bebe0c"></a> `00bebe0c` | `b1 01 40 b9` | ldr w17,[x13] | `FALL_THROUGH`
<a id="insn-00bebe10"></a> `00bebe10` | `03 4e 40 b8` | ldr w3,[x16, #0x4]! | `FALL_THROUGH`
<a id="insn-00bebe14"></a> `00bebe14` | `3f 02 03 6b` | cmp w17,w3 | `FALL_THROUGH`
<a id="insn-00bebe18"></a> `00bebe18` | `31 c2 83 1a` | csel w17,w17,w3,gt | `FALL_THROUGH`
<a id="insn-00bebe1c"></a> `00bebe1c` | `0d b2 8d 9a` | csel x13,x16,x13,lt | `FALL_THROUGH`
<a id="insn-00bebe20"></a> `00bebe20` | `ee b1 8e 9a` | csel x14,x15,x14,lt | `FALL_THROUGH`
<a id="insn-00bebe24"></a> `00bebe24` | `02 00 00 14` | b 0x00bebe2c | `UNCONDITIONAL_JUMP`
<a id="insn-00bebe28"></a> `00bebe28` | `b1 01 40 b9` | ldr w17,[x13] | `FALL_THROUGH`
<a id="insn-00bebe2c"></a> `00bebe2c` | `10 08 0c 8b` | add x16,x0,x12, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bebe30"></a> `00bebe30` | `0f 02 40 b9` | ldr w15,[x16] | `FALL_THROUGH`
<a id="insn-00bebe34"></a> `00bebe34` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bebe38"></a> `00bebe38` | `6a 01 00 54` | b.ge 0x00bebe64 | `CONDITIONAL_JUMP`
<a id="insn-00bebe3c"></a> `00bebe3c` | `e7 ff ff 17` | b 0x00bebdd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bebe40"></a> `00bebe40` | `e4 03 0d aa` | mov x4,x13 | `FALL_THROUGH`
<a id="insn-00bebe44"></a> `00bebe44` | `b1 01 40 b9` | ldr w17,[x13] | `FALL_THROUGH`
<a id="insn-00bebe48"></a> `00bebe48` | `85 4c 40 b8` | ldr w5,[x4, #0x4]! | `FALL_THROUGH`
<a id="insn-00bebe4c"></a> `00bebe4c` | `3f 02 05 6b` | cmp w17,w5 | `FALL_THROUGH`
<a id="insn-00bebe50"></a> `00bebe50` | `31 c2 85 1a` | csel w17,w17,w5,gt | `FALL_THROUGH`
<a id="insn-00bebe54"></a> `00bebe54` | `8d b0 8d 9a` | csel x13,x4,x13,lt | `FALL_THROUGH`
<a id="insn-00bebe58"></a> `00bebe58` | `ce b1 83 9a` | csel x14,x14,x3,lt | `FALL_THROUGH`
<a id="insn-00bebe5c"></a> `00bebe5c` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bebe60"></a> `00bebe60` | `ab fb ff 54` | b.lt 0x00bebdd4 | `CONDITIONAL_JUMP`
<a id="insn-00bebe64"></a> `00bebe64` | `7f 01 0e eb` | cmp x11,x14 | `FALL_THROUGH`
<a id="insn-00bebe68"></a> `00bebe68` | `11 02 00 b9` | str w17,[x16] | `FALL_THROUGH`
<a id="insn-00bebe6c"></a> `00bebe6c` | `f0 03 0d aa` | mov x16,x13 | `FALL_THROUGH`
<a id="insn-00bebe70"></a> `00bebe70` | `2b fb ff 54` | b.lt 0x00bebdd4 | `CONDITIONAL_JUMP`
<a id="insn-00bebe74"></a> `00bebe74` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bebe78"></a> `00bebe78` | `cd f9 7f d3` | lsl x13,x14,#0x1 | `FALL_THROUGH`
<a id="insn-00bebe7c"></a> `00bebe7c` | `c3 f9 7f b3` | bfm x3,x14,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bebe80"></a> `00bebe80` | `ae 09 00 91` | add x14,x13,#0x2 | `FALL_THROUGH`
<a id="insn-00bebe84"></a> `00bebe84` | `0d 08 03 8b` | add x13,x0,x3, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bebe88"></a> `00bebe88` | `df 01 08 eb` | cmp x14,x8 | `FALL_THROUGH`
<a id="insn-00bebe8c"></a> `00bebe8c` | `ab fd ff 54` | b.lt 0x00bebe40 | `CONDITIONAL_JUMP`
<a id="insn-00bebe90"></a> `00bebe90` | `b1 01 40 b9` | ldr w17,[x13] | `FALL_THROUGH`
<a id="insn-00bebe94"></a> `00bebe94` | `ee 03 03 aa` | mov x14,x3 | `FALL_THROUGH`
<a id="insn-00bebe98"></a> `00bebe98` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bebe9c"></a> `00bebe9c` | `4a fe ff 54` | b.ge 0x00bebe64 | `CONDITIONAL_JUMP`
<a id="insn-00bebea0"></a> `00bebea0` | `cd ff ff 17` | b 0x00bebdd4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bebea4"></a> `00bebea4` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-00bebea8"></a> `00bebea8` | `e3 03 01 aa` | mov x3,x1 | `FALL_THROUGH`
<a id="insn-00bebeac"></a> `00bebeac` | `c0 07 00 54` | b.eq 0x00bebfa4 | `CONDITIONAL_JUMP`
<a id="insn-00bebeb0"></a> `00bebeb0` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bebeb4"></a> `00bebeb4` | `0b 10 00 91` | add x11,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00bebeb8"></a> `00bebeb8` | `0c 20 00 91` | add x12,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bebebc"></a> `00bebebc` | `2d 00 80 52` | mov w13,#0x1 | `FALL_THROUGH`
<a id="insn-00bebec0"></a> `00bebec0` | `ee 03 01 aa` | mov x14,x1 | `FALL_THROUGH`
<a id="insn-00bebec4"></a> `00bebec4` | `05 00 00 14` | b 0x00bebed8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bebec8"></a> `00bebec8` | `6f 00 00 b9` | str w15,[x3] | `FALL_THROUGH`
<a id="insn-00bebecc"></a> `00bebecc` | `ce 11 00 91` | add x14,x14,#0x4 | `FALL_THROUGH`
<a id="insn-00bebed0"></a> `00bebed0` | `df 01 02 eb` | cmp x14,x2 | `FALL_THROUGH`
<a id="insn-00bebed4"></a> `00bebed4` | `60 06 00 54` | b.eq 0x00bebfa0 | `CONDITIONAL_JUMP`
<a id="insn-00bebed8"></a> `00bebed8` | `cf 01 40 b9` | ldr w15,[x14] | `FALL_THROUGH`
<a id="insn-00bebedc"></a> `00bebedc` | `10 00 40 b9` | ldr w16,[x0] | `FALL_THROUGH`
<a id="insn-00bebee0"></a> `00bebee0` | `ff 01 10 6b` | cmp w15,w16 | `FALL_THROUGH`
<a id="insn-00bebee4"></a> `00bebee4` | `4a ff ff 54` | b.ge 0x00bebecc | `CONDITIONAL_JUMP`
<a id="insn-00bebee8"></a> `00bebee8` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bebeec"></a> `00bebeec` | `d0 01 00 b9` | str w16,[x14] | `FALL_THROUGH`
<a id="insn-00bebef0"></a> `00bebef0` | `0f 00 00 b9` | str w15,[x0] | `FALL_THROUGH`
<a id="insn-00bebef4"></a> `00bebef4` | `cb fe ff 54` | b.lt 0x00bebecc | `CONDITIONAL_JUMP`
<a id="insn-00bebef8"></a> `00bebef8` | `71 01 40 b9` | ldr w17,[x11] | `FALL_THROUGH`
<a id="insn-00bebefc"></a> `00bebefc` | `3f 21 00 f1` | cmp x9,#0x8 | `FALL_THROUGH`
<a id="insn-00bebf00"></a> `00bebf00` | `c1 00 00 54` | b.ne 0x00bebf18 | `CONDITIONAL_JUMP`
<a id="insn-00bebf04"></a> `00bebf04` | `f0 03 0b aa` | mov x16,x11 | `FALL_THROUGH`
<a id="insn-00bebf08"></a> `00bebf08` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-00bebf0c"></a> `00bebf0c` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bebf10"></a> `00bebf10` | `eb fd ff 54` | b.lt 0x00bebecc | `CONDITIONAL_JUMP`
<a id="insn-00bebf14"></a> `00bebf14` | `08 00 00 14` | b 0x00bebf34 | `UNCONDITIONAL_JUMP`
<a id="insn-00bebf18"></a> `00bebf18` | `90 01 40 b9` | ldr w16,[x12] | `FALL_THROUGH`
<a id="insn-00bebf1c"></a> `00bebf1c` | `3f 02 10 6b` | cmp w17,w16 | `FALL_THROUGH`
<a id="insn-00bebf20"></a> `00bebf20` | `31 c2 90 1a` | csel w17,w17,w16,gt | `FALL_THROUGH`
<a id="insn-00bebf24"></a> `00bebf24` | `90 b1 8b 9a` | csel x16,x12,x11,lt | `FALL_THROUGH`
<a id="insn-00bebf28"></a> `00bebf28` | `a4 a5 8d 9a` | cinc x4,x13,lt | `FALL_THROUGH`
<a id="insn-00bebf2c"></a> `00bebf2c` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bebf30"></a> `00bebf30` | `eb fc ff 54` | b.lt 0x00bebecc | `CONDITIONAL_JUMP`
<a id="insn-00bebf34"></a> `00bebf34` | `e3 03 00 aa` | mov x3,x0 | `FALL_THROUGH`
<a id="insn-00bebf38"></a> `00bebf38` | `0a 00 00 14` | b 0x00bebf60 | `UNCONDITIONAL_JUMP`
<a id="insn-00bebf3c"></a> `00bebf3c` | `e6 03 10 aa` | mov x6,x16 | `FALL_THROUGH`
<a id="insn-00bebf40"></a> `00bebf40` | `11 02 40 b9` | ldr w17,[x16] | `FALL_THROUGH`
<a id="insn-00bebf44"></a> `00bebf44` | `c7 4c 40 b8` | ldr w7,[x6, #0x4]! | `FALL_THROUGH`
<a id="insn-00bebf48"></a> `00bebf48` | `3f 02 07 6b` | cmp w17,w7 | `FALL_THROUGH`
<a id="insn-00bebf4c"></a> `00bebf4c` | `31 c2 87 1a` | csel w17,w17,w7,gt | `FALL_THROUGH`
<a id="insn-00bebf50"></a> `00bebf50` | `d0 b0 90 9a` | csel x16,x6,x16,lt | `FALL_THROUGH`
<a id="insn-00bebf54"></a> `00bebf54` | `84 b0 85 9a` | csel x4,x4,x5,lt | `FALL_THROUGH`
<a id="insn-00bebf58"></a> `00bebf58` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bebf5c"></a> `00bebf5c` | `6b fb ff 54` | b.lt 0x00bebec8 | `CONDITIONAL_JUMP`
<a id="insn-00bebf60"></a> `00bebf60` | `5f 01 04 eb` | cmp x10,x4 | `FALL_THROUGH`
<a id="insn-00bebf64"></a> `00bebf64` | `71 00 00 b9` | str w17,[x3] | `FALL_THROUGH`
<a id="insn-00bebf68"></a> `00bebf68` | `e3 03 10 aa` | mov x3,x16 | `FALL_THROUGH`
<a id="insn-00bebf6c"></a> `00bebf6c` | `eb fa ff 54` | b.lt 0x00bebec8 | `CONDITIONAL_JUMP`
<a id="insn-00bebf70"></a> `00bebf70` | `25 00 80 52` | mov w5,#0x1 | `FALL_THROUGH`
<a id="insn-00bebf74"></a> `00bebf74` | `90 f8 7f d3` | lsl x16,x4,#0x1 | `FALL_THROUGH`
<a id="insn-00bebf78"></a> `00bebf78` | `85 f8 7f b3` | bfm x5,x4,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bebf7c"></a> `00bebf7c` | `04 0a 00 91` | add x4,x16,#0x2 | `FALL_THROUGH`
<a id="insn-00bebf80"></a> `00bebf80` | `10 08 05 8b` | add x16,x0,x5, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bebf84"></a> `00bebf84` | `9f 00 08 eb` | cmp x4,x8 | `FALL_THROUGH`
<a id="insn-00bebf88"></a> `00bebf88` | `ab fd ff 54` | b.lt 0x00bebf3c | `CONDITIONAL_JUMP`
<a id="insn-00bebf8c"></a> `00bebf8c` | `11 02 40 b9` | ldr w17,[x16] | `FALL_THROUGH`
<a id="insn-00bebf90"></a> `00bebf90` | `e4 03 05 aa` | mov x4,x5 | `FALL_THROUGH`
<a id="insn-00bebf94"></a> `00bebf94` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bebf98"></a> `00bebf98` | `4a fe ff 54` | b.ge 0x00bebf60 | `CONDITIONAL_JUMP`
<a id="insn-00bebf9c"></a> `00bebf9c` | `cb ff ff 17` | b 0x00bebec8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bebfa0"></a> `00bebfa0` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bebfa4"></a> `00bebfa4` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bebfa8"></a> `00bebfa8` | `0a 01 00 54` | b.ge 0x00bebfc8 | `CONDITIONAL_JUMP`
<a id="insn-00bebfac"></a> `00bebfac` | `e2 03 03 aa` | mov x2,x3 | `FALL_THROUGH`
<a id="insn-00bebfb0"></a> `00bebfb0` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bebfb4"></a> `00bebfb4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bebfb8"></a> `00bebfb8` | `2a 01 00 b9` | str w10,[x9] | `FALL_THROUGH`
<a id="insn-00bebfbc"></a> `00bebfbc` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bebfc0"></a> `00bebfc0` | `08 05 00 d1` | sub x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bebfc4"></a> `00bebfc4` | `4d ff ff 54` | b.le 0x00bebfac | `CONDITIONAL_JUMP`
<a id="insn-00bebfc8"></a> `00bebfc8` | `09 09 00 d1` | sub x9,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bebfcc"></a> `00bebfcc` | `0a 00 40 b9` | ldr w10,[x0] | `FALL_THROUGH`
<a id="insn-00bebfd0"></a> `00bebfd0` | `ed 03 1f aa` | mov x13,xzr | `FALL_THROUGH`
<a id="insn-00bebfd4"></a> `00bebfd4` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bebfd8"></a> `00bebfd8` | `ec 03 00 aa` | mov x12,x0 | `FALL_THROUGH`
<a id="insn-00bebfdc"></a> `00bebfdc` | `0b 00 00 14` | b 0x00bec008 | `UNCONDITIONAL_JUMP`
<a id="insn-00bebfe0"></a> `00bebfe0` | `0d 8e 40 b8` | ldr w13,[x16, #0x8]! | `FALL_THROUGH`
<a id="insn-00bebfe4"></a> `00bebfe4` | `0f c2 5f b8` | ldur w15,[x16, #-0x4] | `FALL_THROUGH`
<a id="insn-00bebfe8"></a> `00bebfe8` | `ff 01 0d 6b` | cmp w15,w13 | `FALL_THROUGH`
<a id="insn-00bebfec"></a> `00bebfec` | `ef c1 8d 1a` | csel w15,w15,w13,gt | `FALL_THROUGH`
<a id="insn-00bebff0"></a> `00bebff0` | `09 b2 89 9a` | csel x9,x16,x9,lt | `FALL_THROUGH`
<a id="insn-00bebff4"></a> `00bebff4` | `2d b2 8e 9a` | csel x13,x17,x14,lt | `FALL_THROUGH`
<a id="insn-00bebff8"></a> `00bebff8` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00bebffc"></a> `00bebffc` | `8f 01 00 b9` | str w15,[x12] | `FALL_THROUGH`
<a id="insn-00bec000"></a> `00bec000` | `ec 03 09 aa` | mov x12,x9 | `FALL_THROUGH`
<a id="insn-00bec004"></a> `00bec004` | `8c 01 00 54` | b.gt 0x00bec034 | `CONDITIONAL_JUMP`
<a id="insn-00bec008"></a> `00bec008` | `a9 f9 7f d3` | lsl x9,x13,#0x1 | `FALL_THROUGH`
<a id="insn-00bec00c"></a> `00bec00c` | `90 09 0d 8b` | add x16,x12,x13, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bec010"></a> `00bec010` | `2e 00 80 52` | mov w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bec014"></a> `00bec014` | `ae f9 7f b3` | bfm x14,x13,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bec018"></a> `00bec018` | `31 09 00 91` | add x17,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bec01c"></a> `00bec01c` | `09 12 00 91` | add x9,x16,#0x4 | `FALL_THROUGH`
<a id="insn-00bec020"></a> `00bec020` | `3f 02 08 eb` | cmp x17,x8 | `FALL_THROUGH`
<a id="insn-00bec024"></a> `00bec024` | `eb fd ff 54` | b.lt 0x00bebfe0 | `CONDITIONAL_JUMP`
<a id="insn-00bec028"></a> `00bec028` | `2f 01 40 b9` | ldr w15,[x9] | `FALL_THROUGH`
<a id="insn-00bec02c"></a> `00bec02c` | `ed 03 0e aa` | mov x13,x14 | `FALL_THROUGH`
<a id="insn-00bec030"></a> `00bec030` | `f2 ff ff 17` | b 0x00bebff8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec034"></a> `00bec034` | `21 10 00 d1` | sub x1,x1,#0x4 | `FALL_THROUGH`
<a id="insn-00bec038"></a> `00bec038` | `3f 01 01 eb` | cmp x9,x1 | `FALL_THROUGH`
<a id="insn-00bec03c"></a> `00bec03c` | `e0 fb ff 54` | b.eq 0x00bebfb8 | `CONDITIONAL_JUMP`
<a id="insn-00bec040"></a> `00bec040` | `2b 01 00 cb` | sub x11,x9,x0 | `FALL_THROUGH`
<a id="insn-00bec044"></a> `00bec044` | `2c 00 40 b9` | ldr w12,[x1] | `FALL_THROUGH`
<a id="insn-00bec048"></a> `00bec048` | `6b 11 00 91` | add x11,x11,#0x4 | `FALL_THROUGH`
<a id="insn-00bec04c"></a> `00bec04c` | `6b fd 42 93` | asr x11,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00bec050"></a> `00bec050` | `2c 01 00 b9` | str w12,[x9] | `FALL_THROUGH`
<a id="insn-00bec054"></a> `00bec054` | `2a 00 00 b9` | str w10,[x1] | `FALL_THROUGH`
<a id="insn-00bec058"></a> `00bec058` | `6b 09 00 f1` | subs x11,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00bec05c"></a> `00bec05c` | `0b fb ff 54` | b.lt 0x00bebfbc | `CONDITIONAL_JUMP`
<a id="insn-00bec060"></a> `00bec060` | `6a fd 41 d3` | lsr x10,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00bec064"></a> `00bec064` | `2b 01 40 b9` | ldr w11,[x9] | `FALL_THROUGH`
<a id="insn-00bec068"></a> `00bec068` | `0c 08 0a 8b` | add x12,x0,x10, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bec06c"></a> `00bec06c` | `8d 01 40 b9` | ldr w13,[x12] | `FALL_THROUGH`
<a id="insn-00bec070"></a> `00bec070` | `bf 01 0b 6b` | cmp w13,w11 | `FALL_THROUGH`
<a id="insn-00bec074"></a> `00bec074` | `4a fa ff 54` | b.ge 0x00bebfbc | `CONDITIONAL_JUMP`
<a id="insn-00bec078"></a> `00bec078` | `ee 03 09 aa` | mov x14,x9 | `FALL_THROUGH`
<a id="insn-00bec07c"></a> `00bec07c` | `e9 03 0c aa` | mov x9,x12 | `FALL_THROUGH`
<a id="insn-00bec080"></a> `00bec080` | `cd 01 00 b9` | str w13,[x14] | `FALL_THROUGH`
<a id="insn-00bec084"></a> `00bec084` | `ea 00 00 b4` | cbz x10,0x00bec0a0 | `CONDITIONAL_JUMP`
<a id="insn-00bec088"></a> `00bec088` | `4a 05 00 d1` | sub x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bec08c"></a> `00bec08c` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bec090"></a> `00bec090` | `0c 08 0a 8b` | add x12,x0,x10, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bec094"></a> `00bec094` | `8d 01 40 b9` | ldr w13,[x12] | `FALL_THROUGH`
<a id="insn-00bec098"></a> `00bec098` | `bf 01 0b 6b` | cmp w13,w11 | `FALL_THROUGH`
<a id="insn-00bec09c"></a> `00bec09c` | `eb fe ff 54` | b.lt 0x00bec078 | `CONDITIONAL_JUMP`
<a id="insn-00bec0a0"></a> `00bec0a0` | `2b 01 00 b9` | str w11,[x9] | `FALL_THROUGH`
<a id="insn-00bec0a4"></a> `00bec0a4` | `c6 ff ff 17` | b 0x00bebfbc | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bebdac`](#insn-00bebdac) 範囲 `[['00bebdac', '00bebdb7']]`
  - `CONDITIONAL_JUMP` [`00bebdb4`](#insn-00bebdb4) → [`00bebfb0`](#insn-00bebfb0)
  - `FALL_THROUGH` [`00bebdb4`](#insn-00bebdb4) → [`00bebdb8`](#insn-00bebdb8)
- ブロック [`00bebdb8`](#insn-00bebdb8) 範囲 `[['00bebdb8', '00bebdc7']]`
  - `CONDITIONAL_JUMP` [`00bebdc4`](#insn-00bebdc4) → [`00bebea4`](#insn-00bebea4)
  - `FALL_THROUGH` [`00bebdc4`](#insn-00bebdc4) → [`00bebdc8`](#insn-00bebdc8)
- ブロック [`00bebdc8`](#insn-00bebdc8) 範囲 `[['00bebdc8', '00bebdd3']]`
  - `UNCONDITIONAL_JUMP` [`00bebdd0`](#insn-00bebdd0) → [`00bebde4`](#insn-00bebde4)
- ブロック [`00bebdd4`](#insn-00bebdd4) 範囲 `[['00bebdd4', '00bebdd7']]`
  - `FALL_THROUGH` [`00bebdd4`](#insn-00bebdd4) → [`00bebdd8`](#insn-00bebdd8)
- ブロック [`00bebdd8`](#insn-00bebdd8) 範囲 `[['00bebdd8', '00bebde3']]`
  - `CONDITIONAL_JUMP` [`00bebde0`](#insn-00bebde0) → [`00bebea4`](#insn-00bebea4)
  - `FALL_THROUGH` [`00bebde0`](#insn-00bebde0) → [`00bebde4`](#insn-00bebde4)
- ブロック [`00bebde4`](#insn-00bebde4) 範囲 `[['00bebde4', '00bebdeb']]`
  - `CONDITIONAL_JUMP` [`00bebde8`](#insn-00bebde8) → [`00bebdd8`](#insn-00bebdd8)
  - `FALL_THROUGH` [`00bebde8`](#insn-00bebde8) → [`00bebdec`](#insn-00bebdec)
- ブロック [`00bebdec`](#insn-00bebdec) 範囲 `[['00bebdec', '00bebe07']]`
  - `CONDITIONAL_JUMP` [`00bebe04`](#insn-00bebe04) → [`00bebe28`](#insn-00bebe28)
  - `FALL_THROUGH` [`00bebe04`](#insn-00bebe04) → [`00bebe08`](#insn-00bebe08)
- ブロック [`00bebe08`](#insn-00bebe08) 範囲 `[['00bebe08', '00bebe23']]`
  - `FALL_THROUGH` [`00bebe20`](#insn-00bebe20) → [`00bebe24`](#insn-00bebe24)
- ブロック [`00bebe24`](#insn-00bebe24) 範囲 `[['00bebe24', '00bebe27']]`
  - `UNCONDITIONAL_JUMP` [`00bebe24`](#insn-00bebe24) → [`00bebe2c`](#insn-00bebe2c)
- ブロック [`00bebe28`](#insn-00bebe28) 範囲 `[['00bebe28', '00bebe2b']]`
  - `FALL_THROUGH` [`00bebe28`](#insn-00bebe28) → [`00bebe2c`](#insn-00bebe2c)
- ブロック [`00bebe2c`](#insn-00bebe2c) 範囲 `[['00bebe2c', '00bebe3b']]`
  - `CONDITIONAL_JUMP` [`00bebe38`](#insn-00bebe38) → [`00bebe64`](#insn-00bebe64)
  - `FALL_THROUGH` [`00bebe38`](#insn-00bebe38) → [`00bebe3c`](#insn-00bebe3c)
- ブロック [`00bebe3c`](#insn-00bebe3c) 範囲 `[['00bebe3c', '00bebe3f']]`
  - `UNCONDITIONAL_JUMP` [`00bebe3c`](#insn-00bebe3c) → [`00bebdd8`](#insn-00bebdd8)
- ブロック [`00bebe40`](#insn-00bebe40) 範囲 `[['00bebe40', '00bebe63']]`
  - `CONDITIONAL_JUMP` [`00bebe60`](#insn-00bebe60) → [`00bebdd4`](#insn-00bebdd4)
  - `FALL_THROUGH` [`00bebe60`](#insn-00bebe60) → [`00bebe64`](#insn-00bebe64)
- ブロック [`00bebe64`](#insn-00bebe64) 範囲 `[['00bebe64', '00bebe73']]`
  - `CONDITIONAL_JUMP` [`00bebe70`](#insn-00bebe70) → [`00bebdd4`](#insn-00bebdd4)
  - `FALL_THROUGH` [`00bebe70`](#insn-00bebe70) → [`00bebe74`](#insn-00bebe74)
- ブロック [`00bebe74`](#insn-00bebe74) 範囲 `[['00bebe74', '00bebe8f']]`
  - `CONDITIONAL_JUMP` [`00bebe8c`](#insn-00bebe8c) → [`00bebe40`](#insn-00bebe40)
  - `FALL_THROUGH` [`00bebe8c`](#insn-00bebe8c) → [`00bebe90`](#insn-00bebe90)
- ブロック [`00bebe90`](#insn-00bebe90) 範囲 `[['00bebe90', '00bebe9f']]`
  - `CONDITIONAL_JUMP` [`00bebe9c`](#insn-00bebe9c) → [`00bebe64`](#insn-00bebe64)
  - `FALL_THROUGH` [`00bebe9c`](#insn-00bebe9c) → [`00bebea0`](#insn-00bebea0)
- ブロック [`00bebea0`](#insn-00bebea0) 範囲 `[['00bebea0', '00bebea3']]`
  - `UNCONDITIONAL_JUMP` [`00bebea0`](#insn-00bebea0) → [`00bebdd4`](#insn-00bebdd4)
- ブロック [`00bebea4`](#insn-00bebea4) 範囲 `[['00bebea4', '00bebeaf']]`
  - `CONDITIONAL_JUMP` [`00bebeac`](#insn-00bebeac) → [`00bebfa4`](#insn-00bebfa4)
  - `FALL_THROUGH` [`00bebeac`](#insn-00bebeac) → [`00bebeb0`](#insn-00bebeb0)
- ブロック [`00bebeb0`](#insn-00bebeb0) 範囲 `[['00bebeb0', '00bebec7']]`
  - `UNCONDITIONAL_JUMP` [`00bebec4`](#insn-00bebec4) → [`00bebed8`](#insn-00bebed8)
- ブロック [`00bebec8`](#insn-00bebec8) 範囲 `[['00bebec8', '00bebecb']]`
  - `FALL_THROUGH` [`00bebec8`](#insn-00bebec8) → [`00bebecc`](#insn-00bebecc)
- ブロック [`00bebecc`](#insn-00bebecc) 範囲 `[['00bebecc', '00bebed7']]`
  - `CONDITIONAL_JUMP` [`00bebed4`](#insn-00bebed4) → [`00bebfa0`](#insn-00bebfa0)
  - `FALL_THROUGH` [`00bebed4`](#insn-00bebed4) → [`00bebed8`](#insn-00bebed8)
- ブロック [`00bebed8`](#insn-00bebed8) 範囲 `[['00bebed8', '00bebee7']]`
  - `CONDITIONAL_JUMP` [`00bebee4`](#insn-00bebee4) → [`00bebecc`](#insn-00bebecc)
  - `FALL_THROUGH` [`00bebee4`](#insn-00bebee4) → [`00bebee8`](#insn-00bebee8)
- ブロック [`00bebee8`](#insn-00bebee8) 範囲 `[['00bebee8', '00bebef7']]`
  - `CONDITIONAL_JUMP` [`00bebef4`](#insn-00bebef4) → [`00bebecc`](#insn-00bebecc)
  - `FALL_THROUGH` [`00bebef4`](#insn-00bebef4) → [`00bebef8`](#insn-00bebef8)
- ブロック [`00bebef8`](#insn-00bebef8) 範囲 `[['00bebef8', '00bebf03']]`
  - `CONDITIONAL_JUMP` [`00bebf00`](#insn-00bebf00) → [`00bebf18`](#insn-00bebf18)
  - `FALL_THROUGH` [`00bebf00`](#insn-00bebf00) → [`00bebf04`](#insn-00bebf04)
- ブロック [`00bebf04`](#insn-00bebf04) 範囲 `[['00bebf04', '00bebf13']]`
  - `CONDITIONAL_JUMP` [`00bebf10`](#insn-00bebf10) → [`00bebecc`](#insn-00bebecc)
  - `FALL_THROUGH` [`00bebf10`](#insn-00bebf10) → [`00bebf14`](#insn-00bebf14)
- ブロック [`00bebf14`](#insn-00bebf14) 範囲 `[['00bebf14', '00bebf17']]`
  - `UNCONDITIONAL_JUMP` [`00bebf14`](#insn-00bebf14) → [`00bebf34`](#insn-00bebf34)
- ブロック [`00bebf18`](#insn-00bebf18) 範囲 `[['00bebf18', '00bebf33']]`
  - `CONDITIONAL_JUMP` [`00bebf30`](#insn-00bebf30) → [`00bebecc`](#insn-00bebecc)
  - `FALL_THROUGH` [`00bebf30`](#insn-00bebf30) → [`00bebf34`](#insn-00bebf34)
- ブロック [`00bebf34`](#insn-00bebf34) 範囲 `[['00bebf34', '00bebf3b']]`
  - `UNCONDITIONAL_JUMP` [`00bebf38`](#insn-00bebf38) → [`00bebf60`](#insn-00bebf60)
- ブロック [`00bebf3c`](#insn-00bebf3c) 範囲 `[['00bebf3c', '00bebf5f']]`
  - `CONDITIONAL_JUMP` [`00bebf5c`](#insn-00bebf5c) → [`00bebec8`](#insn-00bebec8)
  - `FALL_THROUGH` [`00bebf5c`](#insn-00bebf5c) → [`00bebf60`](#insn-00bebf60)
- ブロック [`00bebf60`](#insn-00bebf60) 範囲 `[['00bebf60', '00bebf6f']]`
  - `CONDITIONAL_JUMP` [`00bebf6c`](#insn-00bebf6c) → [`00bebec8`](#insn-00bebec8)
  - `FALL_THROUGH` [`00bebf6c`](#insn-00bebf6c) → [`00bebf70`](#insn-00bebf70)
- ブロック [`00bebf70`](#insn-00bebf70) 範囲 `[['00bebf70', '00bebf8b']]`
  - `CONDITIONAL_JUMP` [`00bebf88`](#insn-00bebf88) → [`00bebf3c`](#insn-00bebf3c)
  - `FALL_THROUGH` [`00bebf88`](#insn-00bebf88) → [`00bebf8c`](#insn-00bebf8c)
- ブロック [`00bebf8c`](#insn-00bebf8c) 範囲 `[['00bebf8c', '00bebf93']]`
  - `FALL_THROUGH` [`00bebf90`](#insn-00bebf90) → [`00bebf94`](#insn-00bebf94)
- ブロック [`00bebf94`](#insn-00bebf94) 範囲 `[['00bebf94', '00bebf9b']]`
  - `CONDITIONAL_JUMP` [`00bebf98`](#insn-00bebf98) → [`00bebf60`](#insn-00bebf60)
  - `FALL_THROUGH` [`00bebf98`](#insn-00bebf98) → [`00bebf9c`](#insn-00bebf9c)
- ブロック [`00bebf9c`](#insn-00bebf9c) 範囲 `[['00bebf9c', '00bebf9f']]`
  - `UNCONDITIONAL_JUMP` [`00bebf9c`](#insn-00bebf9c) → [`00bebec8`](#insn-00bebec8)
- ブロック [`00bebfa0`](#insn-00bebfa0) 範囲 `[['00bebfa0', '00bebfa3']]`
  - `FALL_THROUGH` [`00bebfa0`](#insn-00bebfa0) → [`00bebfa4`](#insn-00bebfa4)
- ブロック [`00bebfa4`](#insn-00bebfa4) 範囲 `[['00bebfa4', '00bebfab']]`
  - `CONDITIONAL_JUMP` [`00bebfa8`](#insn-00bebfa8) → [`00bebfc8`](#insn-00bebfc8)
  - `FALL_THROUGH` [`00bebfa8`](#insn-00bebfa8) → [`00bebfac`](#insn-00bebfac)
- ブロック [`00bebfac`](#insn-00bebfac) 範囲 `[['00bebfac', '00bebfaf']]`
  - `FALL_THROUGH` [`00bebfac`](#insn-00bebfac) → [`00bebfb0`](#insn-00bebfb0)
- ブロック [`00bebfb0`](#insn-00bebfb0) 範囲 `[['00bebfb0', '00bebfb7']]`
- ブロック [`00bebfb8`](#insn-00bebfb8) 範囲 `[['00bebfb8', '00bebfbb']]`
  - `FALL_THROUGH` [`00bebfb8`](#insn-00bebfb8) → [`00bebfbc`](#insn-00bebfbc)
- ブロック [`00bebfbc`](#insn-00bebfbc) 範囲 `[['00bebfbc', '00bebfc7']]`
  - `CONDITIONAL_JUMP` [`00bebfc4`](#insn-00bebfc4) → [`00bebfac`](#insn-00bebfac)
  - `FALL_THROUGH` [`00bebfc4`](#insn-00bebfc4) → [`00bebfc8`](#insn-00bebfc8)
- ブロック [`00bebfc8`](#insn-00bebfc8) 範囲 `[['00bebfc8', '00bebfdf']]`
  - `UNCONDITIONAL_JUMP` [`00bebfdc`](#insn-00bebfdc) → [`00bec008`](#insn-00bec008)
- ブロック [`00bebfe0`](#insn-00bebfe0) 範囲 `[['00bebfe0', '00bebff7']]`
  - `FALL_THROUGH` [`00bebff4`](#insn-00bebff4) → [`00bebff8`](#insn-00bebff8)
- ブロック [`00bebff8`](#insn-00bebff8) 範囲 `[['00bebff8', '00bec007']]`
  - `CONDITIONAL_JUMP` [`00bec004`](#insn-00bec004) → [`00bec034`](#insn-00bec034)
  - `FALL_THROUGH` [`00bec004`](#insn-00bec004) → [`00bec008`](#insn-00bec008)
- ブロック [`00bec008`](#insn-00bec008) 範囲 `[['00bec008', '00bec027']]`
  - `CONDITIONAL_JUMP` [`00bec024`](#insn-00bec024) → [`00bebfe0`](#insn-00bebfe0)
  - `FALL_THROUGH` [`00bec024`](#insn-00bec024) → [`00bec028`](#insn-00bec028)
- ブロック [`00bec028`](#insn-00bec028) 範囲 `[['00bec028', '00bec033']]`
  - `UNCONDITIONAL_JUMP` [`00bec030`](#insn-00bec030) → [`00bebff8`](#insn-00bebff8)
- ブロック [`00bec034`](#insn-00bec034) 範囲 `[['00bec034', '00bec03f']]`
  - `CONDITIONAL_JUMP` [`00bec03c`](#insn-00bec03c) → [`00bebfb8`](#insn-00bebfb8)
  - `FALL_THROUGH` [`00bec03c`](#insn-00bec03c) → [`00bec040`](#insn-00bec040)
- ブロック [`00bec040`](#insn-00bec040) 範囲 `[['00bec040', '00bec05f']]`
  - `CONDITIONAL_JUMP` [`00bec05c`](#insn-00bec05c) → [`00bebfbc`](#insn-00bebfbc)
  - `FALL_THROUGH` [`00bec05c`](#insn-00bec05c) → [`00bec060`](#insn-00bec060)
- ブロック [`00bec060`](#insn-00bec060) 範囲 `[['00bec060', '00bec077']]`
  - `CONDITIONAL_JUMP` [`00bec074`](#insn-00bec074) → [`00bebfbc`](#insn-00bebfbc)
  - `FALL_THROUGH` [`00bec074`](#insn-00bec074) → [`00bec078`](#insn-00bec078)
- ブロック [`00bec078`](#insn-00bec078) 範囲 `[['00bec078', '00bec087']]`
  - `CONDITIONAL_JUMP` [`00bec084`](#insn-00bec084) → [`00bec0a0`](#insn-00bec0a0)
  - `FALL_THROUGH` [`00bec084`](#insn-00bec084) → [`00bec088`](#insn-00bec088)
- ブロック [`00bec088`](#insn-00bec088) 範囲 `[['00bec088', '00bec09f']]`
  - `CONDITIONAL_JUMP` [`00bec09c`](#insn-00bec09c) → [`00bec078`](#insn-00bec078)
  - `FALL_THROUGH` [`00bec09c`](#insn-00bec09c) → [`00bec0a0`](#insn-00bec0a0)
- ブロック [`00bec0a0`](#insn-00bec0a0) 範囲 `[['00bec0a0', '00bec0a7']]`
  - `UNCONDITIONAL_JUMP` [`00bec0a4`](#insn-00bec0a4) → [`00bebfbc`](#insn-00bebfbc)

## 命令位置別の参照

- [`00bebdb4`](#insn-00bebdb4) → [`00bebfb0`](#insn-00bebfb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebdc4`](#insn-00bebdc4) → [`00bebea4`](#insn-00bebea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebdd0`](#insn-00bebdd0) → [`00bebde4`](#insn-00bebde4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebde0`](#insn-00bebde0) → [`00bebea4`](#insn-00bebea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebde8`](#insn-00bebde8) → [`00bebdd8`](#insn-00bebdd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebe04`](#insn-00bebe04) → [`00bebe28`](#insn-00bebe28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebe24`](#insn-00bebe24) → [`00bebe2c`](#insn-00bebe2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebe38`](#insn-00bebe38) → [`00bebe64`](#insn-00bebe64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebe3c`](#insn-00bebe3c) → [`00bebdd8`](#insn-00bebdd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebe60`](#insn-00bebe60) → [`00bebdd4`](#insn-00bebdd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebe70`](#insn-00bebe70) → [`00bebdd4`](#insn-00bebdd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebe8c`](#insn-00bebe8c) → [`00bebe40`](#insn-00bebe40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebe9c`](#insn-00bebe9c) → [`00bebe64`](#insn-00bebe64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebea0`](#insn-00bebea0) → [`00bebdd4`](#insn-00bebdd4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebeac`](#insn-00bebeac) → [`00bebfa4`](#insn-00bebfa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebec4`](#insn-00bebec4) → [`00bebed8`](#insn-00bebed8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebed4`](#insn-00bebed4) → [`00bebfa0`](#insn-00bebfa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebee4`](#insn-00bebee4) → [`00bebecc`](#insn-00bebecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebef4`](#insn-00bebef4) → [`00bebecc`](#insn-00bebecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebf00`](#insn-00bebf00) → [`00bebf18`](#insn-00bebf18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebf10`](#insn-00bebf10) → [`00bebecc`](#insn-00bebecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebf14`](#insn-00bebf14) → [`00bebf34`](#insn-00bebf34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebf30`](#insn-00bebf30) → [`00bebecc`](#insn-00bebecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebf38`](#insn-00bebf38) → [`00bebf60`](#insn-00bebf60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebf5c`](#insn-00bebf5c) → [`00bebec8`](#insn-00bebec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebf6c`](#insn-00bebf6c) → [`00bebec8`](#insn-00bebec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebf88`](#insn-00bebf88) → [`00bebf3c`](#insn-00bebf3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebf98`](#insn-00bebf98) → [`00bebf60`](#insn-00bebf60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebf9c`](#insn-00bebf9c) → [`00bebec8`](#insn-00bebec8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebfa8`](#insn-00bebfa8) → [`00bebfc8`](#insn-00bebfc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebfc4`](#insn-00bebfc4) → [`00bebfac`](#insn-00bebfac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebfdc`](#insn-00bebfdc) → [`00bec008`](#insn-00bec008) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec004`](#insn-00bec004) → [`00bec034`](#insn-00bec034) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec024`](#insn-00bec024) → [`00bebfe0`](#insn-00bebfe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec030`](#insn-00bec030) → [`00bebff8`](#insn-00bebff8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec03c`](#insn-00bec03c) → [`00bebfb8`](#insn-00bebfb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec05c`](#insn-00bec05c) → [`00bebfbc`](#insn-00bebfbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec074`](#insn-00bec074) → [`00bebfbc`](#insn-00bebfbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec084`](#insn-00bec084) → [`00bec0a0`](#insn-00bec0a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec09c`](#insn-00bec09c) → [`00bec078`](#insn-00bec078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec0a4`](#insn-00bec0a4) → [`00bebfbc`](#insn-00bebfbc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bebdb4`](#insn-00bebdb4)

~~~json
{
  "source": "00bebdb4",
  "target": "00bebfb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebdc4`](#insn-00bebdc4)

~~~json
{
  "source": "00bebdc4",
  "target": "00bebea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebdd0`](#insn-00bebdd0)

~~~json
{
  "source": "00bebdd0",
  "target": "00bebde4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebde0`](#insn-00bebde0)

~~~json
{
  "source": "00bebde0",
  "target": "00bebea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebde8`](#insn-00bebde8)

~~~json
{
  "source": "00bebde8",
  "target": "00bebdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebe04`](#insn-00bebe04)

~~~json
{
  "source": "00bebe04",
  "target": "00bebe28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebe24`](#insn-00bebe24)

~~~json
{
  "source": "00bebe24",
  "target": "00bebe2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebe38`](#insn-00bebe38)

~~~json
{
  "source": "00bebe38",
  "target": "00bebe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebe3c`](#insn-00bebe3c)

~~~json
{
  "source": "00bebe3c",
  "target": "00bebdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebe60`](#insn-00bebe60)

~~~json
{
  "source": "00bebe60",
  "target": "00bebdd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebe70`](#insn-00bebe70)

~~~json
{
  "source": "00bebe70",
  "target": "00bebdd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebe8c`](#insn-00bebe8c)

~~~json
{
  "source": "00bebe8c",
  "target": "00bebe40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebe9c`](#insn-00bebe9c)

~~~json
{
  "source": "00bebe9c",
  "target": "00bebe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebea0`](#insn-00bebea0)

~~~json
{
  "source": "00bebea0",
  "target": "00bebdd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebeac`](#insn-00bebeac)

~~~json
{
  "source": "00bebeac",
  "target": "00bebfa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebec4`](#insn-00bebec4)

~~~json
{
  "source": "00bebec4",
  "target": "00bebed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebed4`](#insn-00bebed4)

~~~json
{
  "source": "00bebed4",
  "target": "00bebfa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebee4`](#insn-00bebee4)

~~~json
{
  "source": "00bebee4",
  "target": "00bebecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebef4`](#insn-00bebef4)

~~~json
{
  "source": "00bebef4",
  "target": "00bebecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebf00`](#insn-00bebf00)

~~~json
{
  "source": "00bebf00",
  "target": "00bebf18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebf10`](#insn-00bebf10)

~~~json
{
  "source": "00bebf10",
  "target": "00bebecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebf14`](#insn-00bebf14)

~~~json
{
  "source": "00bebf14",
  "target": "00bebf34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebf30`](#insn-00bebf30)

~~~json
{
  "source": "00bebf30",
  "target": "00bebecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebf38`](#insn-00bebf38)

~~~json
{
  "source": "00bebf38",
  "target": "00bebf60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebf5c`](#insn-00bebf5c)

~~~json
{
  "source": "00bebf5c",
  "target": "00bebec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebf6c`](#insn-00bebf6c)

~~~json
{
  "source": "00bebf6c",
  "target": "00bebec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebf88`](#insn-00bebf88)

~~~json
{
  "source": "00bebf88",
  "target": "00bebf3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebf98`](#insn-00bebf98)

~~~json
{
  "source": "00bebf98",
  "target": "00bebf60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebf9c`](#insn-00bebf9c)

~~~json
{
  "source": "00bebf9c",
  "target": "00bebec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebfa8`](#insn-00bebfa8)

~~~json
{
  "source": "00bebfa8",
  "target": "00bebfc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebfc4`](#insn-00bebfc4)

~~~json
{
  "source": "00bebfc4",
  "target": "00bebfac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebfdc`](#insn-00bebfdc)

~~~json
{
  "source": "00bebfdc",
  "target": "00bec008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec004`](#insn-00bec004)

~~~json
{
  "source": "00bec004",
  "target": "00bec034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec024`](#insn-00bec024)

~~~json
{
  "source": "00bec024",
  "target": "00bebfe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec030`](#insn-00bec030)

~~~json
{
  "source": "00bec030",
  "target": "00bebff8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec03c`](#insn-00bec03c)

~~~json
{
  "source": "00bec03c",
  "target": "00bebfb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec05c`](#insn-00bec05c)

~~~json
{
  "source": "00bec05c",
  "target": "00bebfbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec074`](#insn-00bec074)

~~~json
{
  "source": "00bec074",
  "target": "00bebfbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec084`](#insn-00bec084)

~~~json
{
  "source": "00bec084",
  "target": "00bec0a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec09c`](#insn-00bec09c)

~~~json
{
  "source": "00bec09c",
  "target": "00bec078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec0a4`](#insn-00bec0a4)

~~~json
{
  "source": "00bec0a4",
  "target": "00bebfbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
