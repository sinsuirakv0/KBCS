# 00beece4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00beec48`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00beec48.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/no_difference_in_scope-0014.md#compare-0fe5a58bf400c1c9c02af3f1859e3be8)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00befcd8`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00befcd8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/no_difference_in_scope-0014.md#compare-b67d7f89b3002693c0e2793085cbed1f)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00beece4",
  "name": "FUN_00beece4",
  "size": 728,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e2cd922bf47ef825287cf13be987b6dbc1e1bc25c76015453b75c9e6b38fdb28",
  "source_text_sha256": "e2cd922bf47ef825287cf13be987b6dbc1e1bc25c76015453b75c9e6b38fdb28",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00beece4",
        "00beefbb"
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

- [00be7fdc](../00be7/00be7fdc.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4728 bytes

~~~c

double * FUN_00beece4(double *param_1,double *param_2,double *param_3)

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
LAB_00beeed4:
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
                    /* try { // try from 00beef94 to 00cef02f has its CatchHandler @ 00beef94
                       catch() { ... } // from try @ 00beef94 with catch @ 00beef94
                       catch() { ... } // from try @ 00bef03c with catch @ 00beef94 */
                *pdVar5 = dVar14;
                if (uVar10 == 0) break;
                uVar10 = uVar10 - 1 >> 1;
                dVar14 = param_1[uVar10];
                pdVar5 = pdVar4;
                pdVar12 = param_1 + uVar10;
              } while (dVar14 < dVar13);
              goto LAB_00beeed4;
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
<a id="insn-00beece4"></a> `00beece4` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00beece8"></a> `00beece8` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-00beecec"></a> `00beecec` | `00 0f 00 54` | b.eq 0x00beeecc | `CONDITIONAL_JUMP`
<a id="insn-00beecf0"></a> `00beecf0` | `29 00 00 cb` | sub x9,x1,x0 | `FALL_THROUGH`
<a id="insn-00beecf4"></a> `00beecf4` | `28 fd 43 93` | asr x8,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00beecf8"></a> `00beecf8` | `0a 09 00 f1` | subs x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00beecfc"></a> `00beecfc` | `ab 06 00 54` | b.lt 0x00beedd0 | `CONDITIONAL_JUMP`
<a id="insn-00beed00"></a> `00beed00` | `4b fd 41 d3` | lsr x11,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00beed04"></a> `00beed04` | `ec 03 0b aa` | mov x12,x11 | `FALL_THROUGH`
<a id="insn-00beed08"></a> `00beed08` | `05 00 00 14` | b 0x00beed1c | `UNCONDITIONAL_JUMP`
<a id="insn-00beed0c"></a> `00beed0c` | `e0 01 00 fd` | str d0,[x15] | `FALL_THROUGH`
<a id="insn-00beed10"></a> `00beed10` | `9f 01 00 f1` | cmp x12,#0x0 | `FALL_THROUGH`
<a id="insn-00beed14"></a> `00beed14` | `8c 05 00 d1` | sub x12,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00beed18"></a> `00beed18` | `cd 05 00 54` | b.le 0x00beedd0 | `CONDITIONAL_JUMP`
<a id="insn-00beed1c"></a> `00beed1c` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-00beed20"></a> `00beed20` | `8b ff ff 54` | b.lt 0x00beed10 | `CONDITIONAL_JUMP`
<a id="insn-00beed24"></a> `00beed24` | `2d 00 80 52` | mov w13,#0x1 | `FALL_THROUGH`
<a id="insn-00beed28"></a> `00beed28` | `8e f1 7f d3` | ubfiz x14,x12,#0x1,#0x3d | `FALL_THROUGH`
<a id="insn-00beed2c"></a> `00beed2c` | `8d f1 7f b3` | bfm x13,x12,#0x3f,#0x3c | `FALL_THROUGH`
<a id="insn-00beed30"></a> `00beed30` | `cf 09 00 91` | add x15,x14,#0x2 | `FALL_THROUGH`
<a id="insn-00beed34"></a> `00beed34` | `0e 0c 0d 8b` | add x14,x0,x13, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00beed38"></a> `00beed38` | `ff 01 08 eb` | cmp x15,x8 | `FALL_THROUGH`
<a id="insn-00beed3c"></a> `00beed3c` | `0a 01 00 54` | b.ge 0x00beed5c | `CONDITIONAL_JUMP`
<a id="insn-00beed40"></a> `00beed40` | `f0 03 0e aa` | mov x16,x14 | `FALL_THROUGH`
<a id="insn-00beed44"></a> `00beed44` | `c1 01 40 fd` | ldr d1,[x14] | `FALL_THROUGH`
<a id="insn-00beed48"></a> `00beed48` | `00 8e 40 fc` | ldr d0,[x16, #0x8]! | `FALL_THROUGH`
<a id="insn-00beed4c"></a> `00beed4c` | `20 20 60 1e` | fcmp d1,d0 | `FALL_THROUGH`
<a id="insn-00beed50"></a> `00beed50` | `65 00 00 54` | b.pl 0x00beed5c | `CONDITIONAL_JUMP`
<a id="insn-00beed54"></a> `00beed54` | `ee 03 10 aa` | mov x14,x16 | `FALL_THROUGH`
<a id="insn-00beed58"></a> `00beed58` | `ed 03 0f aa` | mov x13,x15 | `FALL_THROUGH`
<a id="insn-00beed5c"></a> `00beed5c` | `0f 0c 0c 8b` | add x15,x0,x12, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00beed60"></a> `00beed60` | `c1 01 40 fd` | ldr d1,[x14] | `FALL_THROUGH`
<a id="insn-00beed64"></a> `00beed64` | `e0 01 40 fd` | ldr d0,[x15] | `FALL_THROUGH`
<a id="insn-00beed68"></a> `00beed68` | `20 20 60 1e` | fcmp d1,d0 | `FALL_THROUGH`
<a id="insn-00beed6c"></a> `00beed6c` | `a5 00 00 54` | b.pl 0x00beed80 | `CONDITIONAL_JUMP`
<a id="insn-00beed70"></a> `00beed70` | `e8 ff ff 17` | b 0x00beed10 | `UNCONDITIONAL_JUMP`
<a id="insn-00beed74"></a> `00beed74` | `c1 01 40 fd` | ldr d1,[x14] | `FALL_THROUGH`
<a id="insn-00beed78"></a> `00beed78` | `20 20 60 1e` | fcmp d1,d0 | `FALL_THROUGH`
<a id="insn-00beed7c"></a> `00beed7c` | `84 fc ff 54` | b.mi 0x00beed0c | `CONDITIONAL_JUMP`
<a id="insn-00beed80"></a> `00beed80` | `7f 01 0d eb` | cmp x11,x13 | `FALL_THROUGH`
<a id="insn-00beed84"></a> `00beed84` | `e1 01 00 fd` | str d1,[x15] | `FALL_THROUGH`
<a id="insn-00beed88"></a> `00beed88` | `ef 03 0e aa` | mov x15,x14 | `FALL_THROUGH`
<a id="insn-00beed8c"></a> `00beed8c` | `0b fc ff 54` | b.lt 0x00beed0c | `CONDITIONAL_JUMP`
<a id="insn-00beed90"></a> `00beed90` | `31 00 80 52` | mov w17,#0x1 | `FALL_THROUGH`
<a id="insn-00beed94"></a> `00beed94` | `ae f9 7f d3` | lsl x14,x13,#0x1 | `FALL_THROUGH`
<a id="insn-00beed98"></a> `00beed98` | `b1 f9 7f b3` | bfm x17,x13,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00beed9c"></a> `00beed9c` | `d0 09 00 91` | add x16,x14,#0x2 | `FALL_THROUGH`
<a id="insn-00beeda0"></a> `00beeda0` | `0e 0c 11 8b` | add x14,x0,x17, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00beeda4"></a> `00beeda4` | `1f 02 08 eb` | cmp x16,x8 | `FALL_THROUGH`
<a id="insn-00beeda8"></a> `00beeda8` | `ed 03 11 aa` | mov x13,x17 | `FALL_THROUGH`
<a id="insn-00beedac"></a> `00beedac` | `4a fe ff 54` | b.ge 0x00beed74 | `CONDITIONAL_JUMP`
<a id="insn-00beedb0"></a> `00beedb0` | `f1 03 0e aa` | mov x17,x14 | `FALL_THROUGH`
<a id="insn-00beedb4"></a> `00beedb4` | `c2 01 40 fd` | ldr d2,[x14] | `FALL_THROUGH`
<a id="insn-00beedb8"></a> `00beedb8` | `21 8e 40 fc` | ldr d1,[x17, #0x8]! | `FALL_THROUGH`
<a id="insn-00beedbc"></a> `00beedbc` | `40 20 61 1e` | fcmp d2,d1 | `FALL_THROUGH`
<a id="insn-00beedc0"></a> `00beedc0` | `a5 fd ff 54` | b.pl 0x00beed74 | `CONDITIONAL_JUMP`
<a id="insn-00beedc4"></a> `00beedc4` | `ee 03 11 aa` | mov x14,x17 | `FALL_THROUGH`
<a id="insn-00beedc8"></a> `00beedc8` | `ed 03 10 aa` | mov x13,x16 | `FALL_THROUGH`
<a id="insn-00beedcc"></a> `00beedcc` | `ea ff ff 17` | b 0x00beed74 | `UNCONDITIONAL_JUMP`
<a id="insn-00beedd0"></a> `00beedd0` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-00beedd4"></a> `00beedd4` | `e3 03 01 aa` | mov x3,x1 | `FALL_THROUGH`
<a id="insn-00beedd8"></a> `00beedd8` | `40 07 00 54` | b.eq 0x00beeec0 | `CONDITIONAL_JUMP`
<a id="insn-00beeddc"></a> `00beeddc` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00beede0"></a> `00beede0` | `0b 20 00 91` | add x11,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00beede4"></a> `00beede4` | `0c 40 00 91` | add x12,x0,#0x10 | `FALL_THROUGH`
<a id="insn-00beede8"></a> `00beede8` | `ed 03 01 aa` | mov x13,x1 | `FALL_THROUGH`
<a id="insn-00beedec"></a> `00beedec` | `05 00 00 14` | b 0x00beee00 | `UNCONDITIONAL_JUMP`
<a id="insn-00beedf0"></a> `00beedf0` | `00 02 00 fd` | str d0,[x16] | `FALL_THROUGH`
<a id="insn-00beedf4"></a> `00beedf4` | `ad 21 00 91` | add x13,x13,#0x8 | `FALL_THROUGH`
<a id="insn-00beedf8"></a> `00beedf8` | `bf 01 02 eb` | cmp x13,x2 | `FALL_THROUGH`
<a id="insn-00beedfc"></a> `00beedfc` | `00 06 00 54` | b.eq 0x00beeebc | `CONDITIONAL_JUMP`
<a id="insn-00beee00"></a> `00beee00` | `a0 01 40 fd` | ldr d0,[x13] | `FALL_THROUGH`
<a id="insn-00beee04"></a> `00beee04` | `01 00 40 fd` | ldr d1,[x0] | `FALL_THROUGH`
<a id="insn-00beee08"></a> `00beee08` | `00 20 61 1e` | fcmp d0,d1 | `FALL_THROUGH`
<a id="insn-00beee0c"></a> `00beee0c` | `45 ff ff 54` | b.pl 0x00beedf4 | `CONDITIONAL_JUMP`
<a id="insn-00beee10"></a> `00beee10` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00beee14"></a> `00beee14` | `a1 01 00 fd` | str d1,[x13] | `FALL_THROUGH`
<a id="insn-00beee18"></a> `00beee18` | `00 00 00 fd` | str d0,[x0] | `FALL_THROUGH`
<a id="insn-00beee1c"></a> `00beee1c` | `cb fe ff 54` | b.lt 0x00beedf4 | `CONDITIONAL_JUMP`
<a id="insn-00beee20"></a> `00beee20` | `3f 41 00 f1` | cmp x9,#0x10 | `FALL_THROUGH`
<a id="insn-00beee24"></a> `00beee24` | `00 01 00 54` | b.eq 0x00beee44 | `CONDITIONAL_JUMP`
<a id="insn-00beee28"></a> `00beee28` | `61 01 40 fd` | ldr d1,[x11] | `FALL_THROUGH`
<a id="insn-00beee2c"></a> `00beee2c` | `82 01 40 fd` | ldr d2,[x12] | `FALL_THROUGH`
<a id="insn-00beee30"></a> `00beee30` | `20 20 62 1e` | fcmp d1,d2 | `FALL_THROUGH`
<a id="insn-00beee34"></a> `00beee34` | `85 00 00 54` | b.pl 0x00beee44 | `CONDITIONAL_JUMP`
<a id="insn-00beee38"></a> `00beee38` | `ef 03 0c aa` | mov x15,x12 | `FALL_THROUGH`
<a id="insn-00beee3c"></a> `00beee3c` | `4e 00 80 52` | mov w14,#0x2 | `FALL_THROUGH`
<a id="insn-00beee40"></a> `00beee40` | `03 00 00 14` | b 0x00beee4c | `UNCONDITIONAL_JUMP`
<a id="insn-00beee44"></a> `00beee44` | `ef 03 0b aa` | mov x15,x11 | `FALL_THROUGH`
<a id="insn-00beee48"></a> `00beee48` | `2e 00 80 52` | mov w14,#0x1 | `FALL_THROUGH`
<a id="insn-00beee4c"></a> `00beee4c` | `e1 01 40 fd` | ldr d1,[x15] | `FALL_THROUGH`
<a id="insn-00beee50"></a> `00beee50` | `20 20 60 1e` | fcmp d1,d0 | `FALL_THROUGH`
<a id="insn-00beee54"></a> `00beee54` | `04 fd ff 54` | b.mi 0x00beedf4 | `CONDITIONAL_JUMP`
<a id="insn-00beee58"></a> `00beee58` | `f0 03 00 aa` | mov x16,x0 | `FALL_THROUGH`
<a id="insn-00beee5c"></a> `00beee5c` | `04 00 00 14` | b 0x00beee6c | `UNCONDITIONAL_JUMP`
<a id="insn-00beee60"></a> `00beee60` | `e1 01 40 fd` | ldr d1,[x15] | `FALL_THROUGH`
<a id="insn-00beee64"></a> `00beee64` | `20 20 60 1e` | fcmp d1,d0 | `FALL_THROUGH`
<a id="insn-00beee68"></a> `00beee68` | `44 fc ff 54` | b.mi 0x00beedf0 | `CONDITIONAL_JUMP`
<a id="insn-00beee6c"></a> `00beee6c` | `5f 01 0e eb` | cmp x10,x14 | `FALL_THROUGH`
<a id="insn-00beee70"></a> `00beee70` | `01 02 00 fd` | str d1,[x16] | `FALL_THROUGH`
<a id="insn-00beee74"></a> `00beee74` | `f0 03 0f aa` | mov x16,x15 | `FALL_THROUGH`
<a id="insn-00beee78"></a> `00beee78` | `cb fb ff 54` | b.lt 0x00beedf0 | `CONDITIONAL_JUMP`
<a id="insn-00beee7c"></a> `00beee7c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00beee80"></a> `00beee80` | `cf f9 7f d3` | lsl x15,x14,#0x1 | `FALL_THROUGH`
<a id="insn-00beee84"></a> `00beee84` | `c3 f9 7f b3` | bfm x3,x14,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00beee88"></a> `00beee88` | `f1 09 00 91` | add x17,x15,#0x2 | `FALL_THROUGH`
<a id="insn-00beee8c"></a> `00beee8c` | `0f 0c 03 8b` | add x15,x0,x3, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00beee90"></a> `00beee90` | `3f 02 08 eb` | cmp x17,x8 | `FALL_THROUGH`
<a id="insn-00beee94"></a> `00beee94` | `ee 03 03 aa` | mov x14,x3 | `FALL_THROUGH`
<a id="insn-00beee98"></a> `00beee98` | `4a fe ff 54` | b.ge 0x00beee60 | `CONDITIONAL_JUMP`
<a id="insn-00beee9c"></a> `00beee9c` | `e3 03 0f aa` | mov x3,x15 | `FALL_THROUGH`
<a id="insn-00beeea0"></a> `00beeea0` | `e2 01 40 fd` | ldr d2,[x15] | `FALL_THROUGH`
<a id="insn-00beeea4"></a> `00beeea4` | `61 8c 40 fc` | ldr d1,[x3, #0x8]! | `FALL_THROUGH`
<a id="insn-00beeea8"></a> `00beeea8` | `40 20 61 1e` | fcmp d2,d1 | `FALL_THROUGH`
<a id="insn-00beeeac"></a> `00beeeac` | `a5 fd ff 54` | b.pl 0x00beee60 | `CONDITIONAL_JUMP`
<a id="insn-00beeeb0"></a> `00beeeb0` | `ef 03 03 aa` | mov x15,x3 | `FALL_THROUGH`
<a id="insn-00beeeb4"></a> `00beeeb4` | `ee 03 11 aa` | mov x14,x17 | `FALL_THROUGH`
<a id="insn-00beeeb8"></a> `00beeeb8` | `ea ff ff 17` | b 0x00beee60 | `UNCONDITIONAL_JUMP`
<a id="insn-00beeebc"></a> `00beeebc` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00beeec0"></a> `00beeec0` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00beeec4"></a> `00beeec4` | `0a 01 00 54` | b.ge 0x00beeee4 | `CONDITIONAL_JUMP`
<a id="insn-00beeec8"></a> `00beeec8` | `e2 03 03 aa` | mov x2,x3 | `FALL_THROUGH`
<a id="insn-00beeecc"></a> `00beeecc` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00beeed0"></a> `00beeed0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00beeed4"></a> `00beeed4` | `20 01 00 fd` | str d0,[x9] | `FALL_THROUGH`
<a id="insn-00beeed8"></a> `00beeed8` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00beeedc"></a> `00beeedc` | `08 05 00 d1` | sub x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00beeee0"></a> `00beeee0` | `4d ff ff 54` | b.le 0x00beeec8 | `CONDITIONAL_JUMP`
<a id="insn-00beeee4"></a> `00beeee4` | `09 09 00 d1` | sub x9,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00beeee8"></a> `00beeee8` | `00 00 40 fd` | ldr d0,[x0] | `FALL_THROUGH`
<a id="insn-00beeeec"></a> `00beeeec` | `ec 03 1f aa` | mov x12,xzr | `FALL_THROUGH`
<a id="insn-00beeef0"></a> `00beeef0` | `2a fd 41 d3` | lsr x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00beeef4"></a> `00beeef4` | `eb 03 00 aa` | mov x11,x0 | `FALL_THROUGH`
<a id="insn-00beeef8"></a> `00beeef8` | `0b 00 00 14` | b 0x00beef24 | `UNCONDITIONAL_JUMP`
<a id="insn-00beeefc"></a> `00beeefc` | `c1 0d 41 fc` | ldr d1,[x14, #0x10]! | `FALL_THROUGH`
<a id="insn-00beef00"></a> `00beef00` | `c2 81 5f fc` | ldur d2,[x14, #-0x8] | `FALL_THROUGH`
<a id="insn-00beef04"></a> `00beef04` | `40 20 61 1e` | fcmp d2,d1 | `FALL_THROUGH`
<a id="insn-00beef08"></a> `00beef08` | `29 51 8e 9a` | csel x9,x9,x14,pl | `FALL_THROUGH`
<a id="insn-00beef0c"></a> `00beef0c` | `ac 51 8f 9a` | csel x12,x13,x15,pl | `FALL_THROUGH`
<a id="insn-00beef10"></a> `00beef10` | `21 01 40 fd` | ldr d1,[x9] | `FALL_THROUGH`
<a id="insn-00beef14"></a> `00beef14` | `9f 01 0a eb` | cmp x12,x10 | `FALL_THROUGH`
<a id="insn-00beef18"></a> `00beef18` | `61 01 00 fd` | str d1,[x11] | `FALL_THROUGH`
<a id="insn-00beef1c"></a> `00beef1c` | `eb 03 09 aa` | mov x11,x9 | `FALL_THROUGH`
<a id="insn-00beef20"></a> `00beef20` | `6c 01 00 54` | b.gt 0x00beef4c | `CONDITIONAL_JUMP`
<a id="insn-00beef24"></a> `00beef24` | `89 f9 7f d3` | lsl x9,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00beef28"></a> `00beef28` | `6e 0d 0c 8b` | add x14,x11,x12, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00beef2c"></a> `00beef2c` | `2d 00 80 52` | mov w13,#0x1 | `FALL_THROUGH`
<a id="insn-00beef30"></a> `00beef30` | `8d f9 7f b3` | bfm x13,x12,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00beef34"></a> `00beef34` | `2f 09 00 91` | add x15,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00beef38"></a> `00beef38` | `c9 21 00 91` | add x9,x14,#0x8 | `FALL_THROUGH`
<a id="insn-00beef3c"></a> `00beef3c` | `ff 01 08 eb` | cmp x15,x8 | `FALL_THROUGH`
<a id="insn-00beef40"></a> `00beef40` | `eb fd ff 54` | b.lt 0x00beeefc | `CONDITIONAL_JUMP`
<a id="insn-00beef44"></a> `00beef44` | `ec 03 0d aa` | mov x12,x13 | `FALL_THROUGH`
<a id="insn-00beef48"></a> `00beef48` | `f2 ff ff 17` | b 0x00beef10 | `UNCONDITIONAL_JUMP`
<a id="insn-00beef4c"></a> `00beef4c` | `21 20 00 d1` | sub x1,x1,#0x8 | `FALL_THROUGH`
<a id="insn-00beef50"></a> `00beef50` | `3f 01 01 eb` | cmp x9,x1 | `FALL_THROUGH`
<a id="insn-00beef54"></a> `00beef54` | `00 fc ff 54` | b.eq 0x00beeed4 | `CONDITIONAL_JUMP`
<a id="insn-00beef58"></a> `00beef58` | `2a 01 00 cb` | sub x10,x9,x0 | `FALL_THROUGH`
<a id="insn-00beef5c"></a> `00beef5c` | `21 00 40 fd` | ldr d1,[x1] | `FALL_THROUGH`
<a id="insn-00beef60"></a> `00beef60` | `4a 21 00 91` | add x10,x10,#0x8 | `FALL_THROUGH`
<a id="insn-00beef64"></a> `00beef64` | `4a fd 43 93` | asr x10,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00beef68"></a> `00beef68` | `21 01 00 fd` | str d1,[x9] | `FALL_THROUGH`
<a id="insn-00beef6c"></a> `00beef6c` | `20 00 00 fd` | str d0,[x1] | `FALL_THROUGH`
<a id="insn-00beef70"></a> `00beef70` | `4a 09 00 f1` | subs x10,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00beef74"></a> `00beef74` | `2b fb ff 54` | b.lt 0x00beeed8 | `CONDITIONAL_JUMP`
<a id="insn-00beef78"></a> `00beef78` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00beef7c"></a> `00beef7c` | `20 01 40 fd` | ldr d0,[x9] | `FALL_THROUGH`
<a id="insn-00beef80"></a> `00beef80` | `0b 0c 0a 8b` | add x11,x0,x10, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00beef84"></a> `00beef84` | `61 01 40 fd` | ldr d1,[x11] | `FALL_THROUGH`
<a id="insn-00beef88"></a> `00beef88` | `20 20 60 1e` | fcmp d1,d0 | `FALL_THROUGH`
<a id="insn-00beef8c"></a> `00beef8c` | `65 fa ff 54` | b.pl 0x00beeed8 | `CONDITIONAL_JUMP`
<a id="insn-00beef90"></a> `00beef90` | `ec 03 09 aa` | mov x12,x9 | `FALL_THROUGH`
<a id="insn-00beef94"></a> `00beef94` | `e9 03 0b aa` | mov x9,x11 | `FALL_THROUGH`
<a id="insn-00beef98"></a> `00beef98` | `81 01 00 fd` | str d1,[x12] | `FALL_THROUGH`
<a id="insn-00beef9c"></a> `00beef9c` | `ca f9 ff b4` | cbz x10,0x00beeed4 | `CONDITIONAL_JUMP`
<a id="insn-00beefa0"></a> `00beefa0` | `4a 05 00 d1` | sub x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00beefa4"></a> `00beefa4` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00beefa8"></a> `00beefa8` | `0b 0c 0a 8b` | add x11,x0,x10, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00beefac"></a> `00beefac` | `61 01 40 fd` | ldr d1,[x11] | `FALL_THROUGH`
<a id="insn-00beefb0"></a> `00beefb0` | `20 20 60 1e` | fcmp d1,d0 | `FALL_THROUGH`
<a id="insn-00beefb4"></a> `00beefb4` | `e4 fe ff 54` | b.mi 0x00beef90 | `CONDITIONAL_JUMP`
<a id="insn-00beefb8"></a> `00beefb8` | `c7 ff ff 17` | b 0x00beeed4 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00beece4`](#insn-00beece4) 範囲 `[['00beece4', '00beecef']]`
  - `CONDITIONAL_JUMP` [`00beecec`](#insn-00beecec) → [`00beeecc`](#insn-00beeecc)
  - `FALL_THROUGH` [`00beecec`](#insn-00beecec) → [`00beecf0`](#insn-00beecf0)
- ブロック [`00beecf0`](#insn-00beecf0) 範囲 `[['00beecf0', '00beecff']]`
  - `CONDITIONAL_JUMP` [`00beecfc`](#insn-00beecfc) → [`00beedd0`](#insn-00beedd0)
  - `FALL_THROUGH` [`00beecfc`](#insn-00beecfc) → [`00beed00`](#insn-00beed00)
- ブロック [`00beed00`](#insn-00beed00) 範囲 `[['00beed00', '00beed0b']]`
  - `UNCONDITIONAL_JUMP` [`00beed08`](#insn-00beed08) → [`00beed1c`](#insn-00beed1c)
- ブロック [`00beed0c`](#insn-00beed0c) 範囲 `[['00beed0c', '00beed0f']]`
  - `FALL_THROUGH` [`00beed0c`](#insn-00beed0c) → [`00beed10`](#insn-00beed10)
- ブロック [`00beed10`](#insn-00beed10) 範囲 `[['00beed10', '00beed1b']]`
  - `CONDITIONAL_JUMP` [`00beed18`](#insn-00beed18) → [`00beedd0`](#insn-00beedd0)
  - `FALL_THROUGH` [`00beed18`](#insn-00beed18) → [`00beed1c`](#insn-00beed1c)
- ブロック [`00beed1c`](#insn-00beed1c) 範囲 `[['00beed1c', '00beed23']]`
  - `CONDITIONAL_JUMP` [`00beed20`](#insn-00beed20) → [`00beed10`](#insn-00beed10)
  - `FALL_THROUGH` [`00beed20`](#insn-00beed20) → [`00beed24`](#insn-00beed24)
- ブロック [`00beed24`](#insn-00beed24) 範囲 `[['00beed24', '00beed3f']]`
  - `CONDITIONAL_JUMP` [`00beed3c`](#insn-00beed3c) → [`00beed5c`](#insn-00beed5c)
  - `FALL_THROUGH` [`00beed3c`](#insn-00beed3c) → [`00beed40`](#insn-00beed40)
- ブロック [`00beed40`](#insn-00beed40) 範囲 `[['00beed40', '00beed53']]`
  - `CONDITIONAL_JUMP` [`00beed50`](#insn-00beed50) → [`00beed5c`](#insn-00beed5c)
  - `FALL_THROUGH` [`00beed50`](#insn-00beed50) → [`00beed54`](#insn-00beed54)
- ブロック [`00beed54`](#insn-00beed54) 範囲 `[['00beed54', '00beed5b']]`
  - `FALL_THROUGH` [`00beed58`](#insn-00beed58) → [`00beed5c`](#insn-00beed5c)
- ブロック [`00beed5c`](#insn-00beed5c) 範囲 `[['00beed5c', '00beed6f']]`
  - `CONDITIONAL_JUMP` [`00beed6c`](#insn-00beed6c) → [`00beed80`](#insn-00beed80)
  - `FALL_THROUGH` [`00beed6c`](#insn-00beed6c) → [`00beed70`](#insn-00beed70)
- ブロック [`00beed70`](#insn-00beed70) 範囲 `[['00beed70', '00beed73']]`
  - `UNCONDITIONAL_JUMP` [`00beed70`](#insn-00beed70) → [`00beed10`](#insn-00beed10)
- ブロック [`00beed74`](#insn-00beed74) 範囲 `[['00beed74', '00beed7f']]`
  - `CONDITIONAL_JUMP` [`00beed7c`](#insn-00beed7c) → [`00beed0c`](#insn-00beed0c)
  - `FALL_THROUGH` [`00beed7c`](#insn-00beed7c) → [`00beed80`](#insn-00beed80)
- ブロック [`00beed80`](#insn-00beed80) 範囲 `[['00beed80', '00beed8f']]`
  - `CONDITIONAL_JUMP` [`00beed8c`](#insn-00beed8c) → [`00beed0c`](#insn-00beed0c)
  - `FALL_THROUGH` [`00beed8c`](#insn-00beed8c) → [`00beed90`](#insn-00beed90)
- ブロック [`00beed90`](#insn-00beed90) 範囲 `[['00beed90', '00beedaf']]`
  - `CONDITIONAL_JUMP` [`00beedac`](#insn-00beedac) → [`00beed74`](#insn-00beed74)
  - `FALL_THROUGH` [`00beedac`](#insn-00beedac) → [`00beedb0`](#insn-00beedb0)
- ブロック [`00beedb0`](#insn-00beedb0) 範囲 `[['00beedb0', '00beedc3']]`
  - `CONDITIONAL_JUMP` [`00beedc0`](#insn-00beedc0) → [`00beed74`](#insn-00beed74)
  - `FALL_THROUGH` [`00beedc0`](#insn-00beedc0) → [`00beedc4`](#insn-00beedc4)
- ブロック [`00beedc4`](#insn-00beedc4) 範囲 `[['00beedc4', '00beedcf']]`
  - `UNCONDITIONAL_JUMP` [`00beedcc`](#insn-00beedcc) → [`00beed74`](#insn-00beed74)
- ブロック [`00beedd0`](#insn-00beedd0) 範囲 `[['00beedd0', '00beeddb']]`
  - `CONDITIONAL_JUMP` [`00beedd8`](#insn-00beedd8) → [`00beeec0`](#insn-00beeec0)
  - `FALL_THROUGH` [`00beedd8`](#insn-00beedd8) → [`00beeddc`](#insn-00beeddc)
- ブロック [`00beeddc`](#insn-00beeddc) 範囲 `[['00beeddc', '00beedef']]`
  - `UNCONDITIONAL_JUMP` [`00beedec`](#insn-00beedec) → [`00beee00`](#insn-00beee00)
- ブロック [`00beedf0`](#insn-00beedf0) 範囲 `[['00beedf0', '00beedf3']]`
  - `FALL_THROUGH` [`00beedf0`](#insn-00beedf0) → [`00beedf4`](#insn-00beedf4)
- ブロック [`00beedf4`](#insn-00beedf4) 範囲 `[['00beedf4', '00beedff']]`
  - `CONDITIONAL_JUMP` [`00beedfc`](#insn-00beedfc) → [`00beeebc`](#insn-00beeebc)
  - `FALL_THROUGH` [`00beedfc`](#insn-00beedfc) → [`00beee00`](#insn-00beee00)
- ブロック [`00beee00`](#insn-00beee00) 範囲 `[['00beee00', '00beee0f']]`
  - `CONDITIONAL_JUMP` [`00beee0c`](#insn-00beee0c) → [`00beedf4`](#insn-00beedf4)
  - `FALL_THROUGH` [`00beee0c`](#insn-00beee0c) → [`00beee10`](#insn-00beee10)
- ブロック [`00beee10`](#insn-00beee10) 範囲 `[['00beee10', '00beee1f']]`
  - `CONDITIONAL_JUMP` [`00beee1c`](#insn-00beee1c) → [`00beedf4`](#insn-00beedf4)
  - `FALL_THROUGH` [`00beee1c`](#insn-00beee1c) → [`00beee20`](#insn-00beee20)
- ブロック [`00beee20`](#insn-00beee20) 範囲 `[['00beee20', '00beee27']]`
  - `CONDITIONAL_JUMP` [`00beee24`](#insn-00beee24) → [`00beee44`](#insn-00beee44)
  - `FALL_THROUGH` [`00beee24`](#insn-00beee24) → [`00beee28`](#insn-00beee28)
- ブロック [`00beee28`](#insn-00beee28) 範囲 `[['00beee28', '00beee37']]`
  - `CONDITIONAL_JUMP` [`00beee34`](#insn-00beee34) → [`00beee44`](#insn-00beee44)
  - `FALL_THROUGH` [`00beee34`](#insn-00beee34) → [`00beee38`](#insn-00beee38)
- ブロック [`00beee38`](#insn-00beee38) 範囲 `[['00beee38', '00beee43']]`
  - `UNCONDITIONAL_JUMP` [`00beee40`](#insn-00beee40) → [`00beee4c`](#insn-00beee4c)
- ブロック [`00beee44`](#insn-00beee44) 範囲 `[['00beee44', '00beee4b']]`
  - `FALL_THROUGH` [`00beee48`](#insn-00beee48) → [`00beee4c`](#insn-00beee4c)
- ブロック [`00beee4c`](#insn-00beee4c) 範囲 `[['00beee4c', '00beee57']]`
  - `CONDITIONAL_JUMP` [`00beee54`](#insn-00beee54) → [`00beedf4`](#insn-00beedf4)
  - `FALL_THROUGH` [`00beee54`](#insn-00beee54) → [`00beee58`](#insn-00beee58)
- ブロック [`00beee58`](#insn-00beee58) 範囲 `[['00beee58', '00beee5f']]`
  - `UNCONDITIONAL_JUMP` [`00beee5c`](#insn-00beee5c) → [`00beee6c`](#insn-00beee6c)
- ブロック [`00beee60`](#insn-00beee60) 範囲 `[['00beee60', '00beee6b']]`
  - `CONDITIONAL_JUMP` [`00beee68`](#insn-00beee68) → [`00beedf0`](#insn-00beedf0)
  - `FALL_THROUGH` [`00beee68`](#insn-00beee68) → [`00beee6c`](#insn-00beee6c)
- ブロック [`00beee6c`](#insn-00beee6c) 範囲 `[['00beee6c', '00beee7b']]`
  - `CONDITIONAL_JUMP` [`00beee78`](#insn-00beee78) → [`00beedf0`](#insn-00beedf0)
  - `FALL_THROUGH` [`00beee78`](#insn-00beee78) → [`00beee7c`](#insn-00beee7c)
- ブロック [`00beee7c`](#insn-00beee7c) 範囲 `[['00beee7c', '00beee9b']]`
  - `CONDITIONAL_JUMP` [`00beee98`](#insn-00beee98) → [`00beee60`](#insn-00beee60)
  - `FALL_THROUGH` [`00beee98`](#insn-00beee98) → [`00beee9c`](#insn-00beee9c)
- ブロック [`00beee9c`](#insn-00beee9c) 範囲 `[['00beee9c', '00beeeaf']]`
  - `CONDITIONAL_JUMP` [`00beeeac`](#insn-00beeeac) → [`00beee60`](#insn-00beee60)
  - `FALL_THROUGH` [`00beeeac`](#insn-00beeeac) → [`00beeeb0`](#insn-00beeeb0)
- ブロック [`00beeeb0`](#insn-00beeeb0) 範囲 `[['00beeeb0', '00beeebb']]`
  - `UNCONDITIONAL_JUMP` [`00beeeb8`](#insn-00beeeb8) → [`00beee60`](#insn-00beee60)
- ブロック [`00beeebc`](#insn-00beeebc) 範囲 `[['00beeebc', '00beeebf']]`
  - `FALL_THROUGH` [`00beeebc`](#insn-00beeebc) → [`00beeec0`](#insn-00beeec0)
- ブロック [`00beeec0`](#insn-00beeec0) 範囲 `[['00beeec0', '00beeec7']]`
  - `CONDITIONAL_JUMP` [`00beeec4`](#insn-00beeec4) → [`00beeee4`](#insn-00beeee4)
  - `FALL_THROUGH` [`00beeec4`](#insn-00beeec4) → [`00beeec8`](#insn-00beeec8)
- ブロック [`00beeec8`](#insn-00beeec8) 範囲 `[['00beeec8', '00beeecb']]`
  - `FALL_THROUGH` [`00beeec8`](#insn-00beeec8) → [`00beeecc`](#insn-00beeecc)
- ブロック [`00beeecc`](#insn-00beeecc) 範囲 `[['00beeecc', '00beeed3']]`
- ブロック [`00beeed4`](#insn-00beeed4) 範囲 `[['00beeed4', '00beeed7']]`
  - `FALL_THROUGH` [`00beeed4`](#insn-00beeed4) → [`00beeed8`](#insn-00beeed8)
- ブロック [`00beeed8`](#insn-00beeed8) 範囲 `[['00beeed8', '00beeee3']]`
  - `CONDITIONAL_JUMP` [`00beeee0`](#insn-00beeee0) → [`00beeec8`](#insn-00beeec8)
  - `FALL_THROUGH` [`00beeee0`](#insn-00beeee0) → [`00beeee4`](#insn-00beeee4)
- ブロック [`00beeee4`](#insn-00beeee4) 範囲 `[['00beeee4', '00beeefb']]`
  - `UNCONDITIONAL_JUMP` [`00beeef8`](#insn-00beeef8) → [`00beef24`](#insn-00beef24)
- ブロック [`00beeefc`](#insn-00beeefc) 範囲 `[['00beeefc', '00beef0f']]`
  - `FALL_THROUGH` [`00beef0c`](#insn-00beef0c) → [`00beef10`](#insn-00beef10)
- ブロック [`00beef10`](#insn-00beef10) 範囲 `[['00beef10', '00beef23']]`
  - `CONDITIONAL_JUMP` [`00beef20`](#insn-00beef20) → [`00beef4c`](#insn-00beef4c)
  - `FALL_THROUGH` [`00beef20`](#insn-00beef20) → [`00beef24`](#insn-00beef24)
- ブロック [`00beef24`](#insn-00beef24) 範囲 `[['00beef24', '00beef43']]`
  - `CONDITIONAL_JUMP` [`00beef40`](#insn-00beef40) → [`00beeefc`](#insn-00beeefc)
  - `FALL_THROUGH` [`00beef40`](#insn-00beef40) → [`00beef44`](#insn-00beef44)
- ブロック [`00beef44`](#insn-00beef44) 範囲 `[['00beef44', '00beef4b']]`
  - `UNCONDITIONAL_JUMP` [`00beef48`](#insn-00beef48) → [`00beef10`](#insn-00beef10)
- ブロック [`00beef4c`](#insn-00beef4c) 範囲 `[['00beef4c', '00beef57']]`
  - `CONDITIONAL_JUMP` [`00beef54`](#insn-00beef54) → [`00beeed4`](#insn-00beeed4)
  - `FALL_THROUGH` [`00beef54`](#insn-00beef54) → [`00beef58`](#insn-00beef58)
- ブロック [`00beef58`](#insn-00beef58) 範囲 `[['00beef58', '00beef77']]`
  - `CONDITIONAL_JUMP` [`00beef74`](#insn-00beef74) → [`00beeed8`](#insn-00beeed8)
  - `FALL_THROUGH` [`00beef74`](#insn-00beef74) → [`00beef78`](#insn-00beef78)
- ブロック [`00beef78`](#insn-00beef78) 範囲 `[['00beef78', '00beef8f']]`
  - `CONDITIONAL_JUMP` [`00beef8c`](#insn-00beef8c) → [`00beeed8`](#insn-00beeed8)
  - `FALL_THROUGH` [`00beef8c`](#insn-00beef8c) → [`00beef90`](#insn-00beef90)
- ブロック [`00beef90`](#insn-00beef90) 範囲 `[['00beef90', '00beef93']]`
  - `FALL_THROUGH` [`00beef90`](#insn-00beef90) → [`00beef94`](#insn-00beef94)
- ブロック [`00beef94`](#insn-00beef94) 範囲 `[['00beef94', '00beef9f']]`
  - `CONDITIONAL_JUMP` [`00beef9c`](#insn-00beef9c) → [`00beeed4`](#insn-00beeed4)
  - `FALL_THROUGH` [`00beef9c`](#insn-00beef9c) → [`00beefa0`](#insn-00beefa0)
- ブロック [`00beefa0`](#insn-00beefa0) 範囲 `[['00beefa0', '00beefb7']]`
  - `CONDITIONAL_JUMP` [`00beefb4`](#insn-00beefb4) → [`00beef90`](#insn-00beef90)
  - `FALL_THROUGH` [`00beefb4`](#insn-00beefb4) → [`00beefb8`](#insn-00beefb8)
- ブロック [`00beefb8`](#insn-00beefb8) 範囲 `[['00beefb8', '00beefbb']]`
  - `UNCONDITIONAL_JUMP` [`00beefb8`](#insn-00beefb8) → [`00beeed4`](#insn-00beeed4)

## 命令位置別の参照

- [`00beecec`](#insn-00beecec) → [`00beeecc`](#insn-00beeecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beecfc`](#insn-00beecfc) → [`00beedd0`](#insn-00beedd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed08`](#insn-00beed08) → [`00beed1c`](#insn-00beed1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed18`](#insn-00beed18) → [`00beedd0`](#insn-00beedd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed20`](#insn-00beed20) → [`00beed10`](#insn-00beed10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed3c`](#insn-00beed3c) → [`00beed5c`](#insn-00beed5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed50`](#insn-00beed50) → [`00beed5c`](#insn-00beed5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed6c`](#insn-00beed6c) → [`00beed80`](#insn-00beed80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed70`](#insn-00beed70) → [`00beed10`](#insn-00beed10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed7c`](#insn-00beed7c) → [`00beed0c`](#insn-00beed0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed8c`](#insn-00beed8c) → [`00beed0c`](#insn-00beed0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beedac`](#insn-00beedac) → [`00beed74`](#insn-00beed74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beedc0`](#insn-00beedc0) → [`00beed74`](#insn-00beed74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beedcc`](#insn-00beedcc) → [`00beed74`](#insn-00beed74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beedd8`](#insn-00beedd8) → [`00beeec0`](#insn-00beeec0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beedec`](#insn-00beedec) → [`00beee00`](#insn-00beee00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beedfc`](#insn-00beedfc) → [`00beeebc`](#insn-00beeebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee0c`](#insn-00beee0c) → [`00beedf4`](#insn-00beedf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee1c`](#insn-00beee1c) → [`00beedf4`](#insn-00beedf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee24`](#insn-00beee24) → [`00beee44`](#insn-00beee44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee34`](#insn-00beee34) → [`00beee44`](#insn-00beee44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee40`](#insn-00beee40) → [`00beee4c`](#insn-00beee4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee54`](#insn-00beee54) → [`00beedf4`](#insn-00beedf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee5c`](#insn-00beee5c) → [`00beee6c`](#insn-00beee6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee68`](#insn-00beee68) → [`00beedf0`](#insn-00beedf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee78`](#insn-00beee78) → [`00beedf0`](#insn-00beedf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee98`](#insn-00beee98) → [`00beee60`](#insn-00beee60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeeac`](#insn-00beeeac) → [`00beee60`](#insn-00beee60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeeb8`](#insn-00beeeb8) → [`00beee60`](#insn-00beee60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeec4`](#insn-00beeec4) → [`00beeee4`](#insn-00beeee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeee0`](#insn-00beeee0) → [`00beeec8`](#insn-00beeec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeef8`](#insn-00beeef8) → [`00beef24`](#insn-00beef24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beef20`](#insn-00beef20) → [`00beef4c`](#insn-00beef4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beef40`](#insn-00beef40) → [`00beeefc`](#insn-00beeefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beef48`](#insn-00beef48) → [`00beef10`](#insn-00beef10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beef54`](#insn-00beef54) → [`00beeed4`](#insn-00beeed4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beef74`](#insn-00beef74) → [`00beeed8`](#insn-00beeed8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beef8c`](#insn-00beef8c) → [`00beeed8`](#insn-00beeed8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beef9c`](#insn-00beef9c) → [`00beeed4`](#insn-00beeed4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beefb4`](#insn-00beefb4) → [`00beef90`](#insn-00beef90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beefb8`](#insn-00beefb8) → [`00beeed4`](#insn-00beeed4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00beecec`](#insn-00beecec)

~~~json
{
  "source": "00beecec",
  "target": "00beeecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beecfc`](#insn-00beecfc)

~~~json
{
  "source": "00beecfc",
  "target": "00beedd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed08`](#insn-00beed08)

~~~json
{
  "source": "00beed08",
  "target": "00beed1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed18`](#insn-00beed18)

~~~json
{
  "source": "00beed18",
  "target": "00beedd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed20`](#insn-00beed20)

~~~json
{
  "source": "00beed20",
  "target": "00beed10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed3c`](#insn-00beed3c)

~~~json
{
  "source": "00beed3c",
  "target": "00beed5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed50`](#insn-00beed50)

~~~json
{
  "source": "00beed50",
  "target": "00beed5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed6c`](#insn-00beed6c)

~~~json
{
  "source": "00beed6c",
  "target": "00beed80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed70`](#insn-00beed70)

~~~json
{
  "source": "00beed70",
  "target": "00beed10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed7c`](#insn-00beed7c)

~~~json
{
  "source": "00beed7c",
  "target": "00beed0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed8c`](#insn-00beed8c)

~~~json
{
  "source": "00beed8c",
  "target": "00beed0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beedac`](#insn-00beedac)

~~~json
{
  "source": "00beedac",
  "target": "00beed74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beedc0`](#insn-00beedc0)

~~~json
{
  "source": "00beedc0",
  "target": "00beed74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beedcc`](#insn-00beedcc)

~~~json
{
  "source": "00beedcc",
  "target": "00beed74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beedd8`](#insn-00beedd8)

~~~json
{
  "source": "00beedd8",
  "target": "00beeec0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beedec`](#insn-00beedec)

~~~json
{
  "source": "00beedec",
  "target": "00beee00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beedfc`](#insn-00beedfc)

~~~json
{
  "source": "00beedfc",
  "target": "00beeebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee0c`](#insn-00beee0c)

~~~json
{
  "source": "00beee0c",
  "target": "00beedf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee1c`](#insn-00beee1c)

~~~json
{
  "source": "00beee1c",
  "target": "00beedf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee24`](#insn-00beee24)

~~~json
{
  "source": "00beee24",
  "target": "00beee44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee34`](#insn-00beee34)

~~~json
{
  "source": "00beee34",
  "target": "00beee44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee40`](#insn-00beee40)

~~~json
{
  "source": "00beee40",
  "target": "00beee4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee54`](#insn-00beee54)

~~~json
{
  "source": "00beee54",
  "target": "00beedf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee5c`](#insn-00beee5c)

~~~json
{
  "source": "00beee5c",
  "target": "00beee6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee68`](#insn-00beee68)

~~~json
{
  "source": "00beee68",
  "target": "00beedf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee78`](#insn-00beee78)

~~~json
{
  "source": "00beee78",
  "target": "00beedf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee98`](#insn-00beee98)

~~~json
{
  "source": "00beee98",
  "target": "00beee60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeeac`](#insn-00beeeac)

~~~json
{
  "source": "00beeeac",
  "target": "00beee60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeeb8`](#insn-00beeeb8)

~~~json
{
  "source": "00beeeb8",
  "target": "00beee60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeec4`](#insn-00beeec4)

~~~json
{
  "source": "00beeec4",
  "target": "00beeee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeee0`](#insn-00beeee0)

~~~json
{
  "source": "00beeee0",
  "target": "00beeec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeef8`](#insn-00beeef8)

~~~json
{
  "source": "00beeef8",
  "target": "00beef24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beef20`](#insn-00beef20)

~~~json
{
  "source": "00beef20",
  "target": "00beef4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beef40`](#insn-00beef40)

~~~json
{
  "source": "00beef40",
  "target": "00beeefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beef48`](#insn-00beef48)

~~~json
{
  "source": "00beef48",
  "target": "00beef10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beef54`](#insn-00beef54)

~~~json
{
  "source": "00beef54",
  "target": "00beeed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beef74`](#insn-00beef74)

~~~json
{
  "source": "00beef74",
  "target": "00beeed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beef8c`](#insn-00beef8c)

~~~json
{
  "source": "00beef8c",
  "target": "00beeed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beef9c`](#insn-00beef9c)

~~~json
{
  "source": "00beef9c",
  "target": "00beeed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beefb4`](#insn-00beefb4)

~~~json
{
  "source": "00beefb4",
  "target": "00beef90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beefb8`](#insn-00beefb8)

~~~json
{
  "source": "00beefb8",
  "target": "00beeed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
