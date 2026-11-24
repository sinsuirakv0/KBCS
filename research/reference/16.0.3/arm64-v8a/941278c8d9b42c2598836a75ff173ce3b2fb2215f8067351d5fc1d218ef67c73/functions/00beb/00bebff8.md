# 00bebff8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00beb004`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00beb004.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/no_difference_in_scope-0014.md#compare-43574a4cbbeab505e9476a69a2f7f8a5)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bebff8",
  "name": "FUN_00bebff8",
  "size": 764,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "90969e8b9b2db3481f9794a1a575897680c61e28acfb2d415d4218542e072c74",
  "source_text_sha256": "90969e8b9b2db3481f9794a1a575897680c61e28acfb2d415d4218542e072c74",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bebff8",
        "00bec2f3"
      ]
    ],
    "bytes_sha256": "615ada46179eb8a98c4b2d8c5c4b463cd23bc68b351badc3322d5405367cbdd3",
    "instruction_count": 191,
    "instruction_bytes": 764,
    "body_bytes": 764,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be4fb0](../00be4/00be4fb0.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6806 bytes

~~~c

ushort * FUN_00bebff8(ushort *param_1,ushort *param_2,ushort *param_3)

{
  bool bVar1;
  ushort *puVar2;
  ulong uVar3;
  ushort uVar4;
  ushort uVar5;
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
  int iVar16;
  uint uVar17;
  ushort *puVar18;
  ushort uVar19;
  uint uVar20;
  
  if (param_1 != param_2) {
    lVar8 = (long)param_2 - (long)param_1 >> 1;
    if (1 < lVar8) {
      uVar10 = lVar8 - 2U >> 1;
      uVar7 = uVar10;
      do {
        if ((long)uVar7 <= (long)uVar10) {
          uVar3 = uVar7 << 1 | 1;
          uVar14 = uVar7 * 2 + 2;
          puVar12 = param_1 + uVar3;
          if ((long)uVar14 < lVar8) {
            uVar15 = *puVar12;
            uVar4 = puVar12[1];
            uVar19 = uVar15;
            if ((short)uVar15 <= (short)uVar4) {
              uVar19 = uVar4;
            }
            puVar13 = puVar12 + 1;
            if ((short)uVar4 <= (short)uVar15) {
              puVar13 = puVar12;
              uVar14 = uVar3;
            }
          }
          else {
            uVar19 = *puVar12;
            puVar13 = puVar12;
            uVar14 = uVar3;
          }
          uVar15 = param_1[uVar7];
          puVar12 = param_1 + uVar7;
          if ((short)uVar15 <= (short)uVar19) {
            do {
              while( true ) {
                puVar9 = puVar13;
                *puVar12 = uVar19;
                if ((long)uVar10 < (long)uVar14) goto LAB_00bec020;
                uVar3 = uVar14 << 1 | 1;
                uVar14 = uVar14 * 2 + 2;
                puVar6 = param_1 + uVar3;
                puVar12 = puVar9;
                if ((long)uVar14 < lVar8) break;
                uVar19 = *puVar6;
                puVar13 = puVar6;
                uVar14 = uVar3;
                if ((short)uVar19 < (short)uVar15) goto LAB_00bec020;
              }
              uVar4 = *puVar6;
              uVar5 = puVar6[1];
              uVar19 = uVar4;
              if ((short)uVar4 <= (short)uVar5) {
                uVar19 = uVar5;
              }
              puVar13 = puVar6 + 1;
              if ((short)uVar5 <= (short)uVar4) {
                uVar14 = uVar3;
                puVar13 = puVar6;
              }
            } while ((short)uVar15 <= (short)uVar19);
LAB_00bec020:
            *puVar9 = uVar15;
          }
        }
        bVar1 = 0 < (long)uVar7;
        uVar7 = uVar7 - 1;
      } while (bVar1);
    }
    puVar12 = param_2;
    if (param_2 != param_3) {
      puVar13 = param_1 + 1;
      puVar9 = param_2;
      do {
        uVar19 = *puVar9;
        if ((short)uVar19 < (short)*param_1) {
          *puVar9 = *param_1;
          *param_1 = uVar19;
          if (1 < lVar8) {
            uVar15 = *puVar13;
            uVar20 = (uint)(short)uVar15;
            if ((long)param_2 - (long)param_1 == 4) {
              uVar7 = 1;
              puVar12 = puVar13;
            }
            else {
              uVar15 = param_1[2];
              iVar16 = (int)(short)uVar15;
              uVar17 = uVar20;
              if ((int)uVar20 <= iVar16) {
                uVar17 = (uint)(short)uVar15;
              }
              puVar12 = param_1 + 2;
              if (iVar16 <= (int)uVar20) {
                puVar12 = puVar13;
              }
              uVar7 = 1;
              if ((int)uVar20 < iVar16) {
                uVar7 = 2;
              }
              uVar15 = (ushort)uVar17;
              uVar20 = uVar17;
            }
            puVar6 = param_1;
            if ((short)uVar19 <= (short)uVar15) {
              do {
                while( true ) {
                  puVar18 = puVar12;
                  *puVar6 = (ushort)uVar20;
                  if ((long)(lVar8 - 2U >> 1) < (long)uVar7) goto LAB_00bec114;
                  uVar10 = uVar7 << 1 | 1;
                  uVar7 = uVar7 * 2 + 2;
                  puVar2 = param_1 + uVar10;
                  puVar6 = puVar18;
                  if ((long)uVar7 < lVar8) break;
                  uVar20 = (uint)*puVar2;
                  uVar7 = uVar10;
                  puVar12 = puVar2;
                  if ((short)*puVar2 < (short)uVar19) goto LAB_00bec114;
                }
                uVar15 = *puVar2;
                uVar4 = puVar2[1];
                uVar5 = uVar15;
                if ((short)uVar15 <= (short)uVar4) {
                  uVar5 = uVar4;
                }
                uVar20 = (uint)(short)uVar5;
                puVar12 = puVar2 + 1;
                if ((short)uVar4 <= (short)uVar15) {
                  uVar7 = uVar10;
                  puVar12 = puVar2;
                }
              } while ((short)uVar19 <= (short)uVar5);
LAB_00bec114:
              *puVar18 = uVar19;
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
        uVar19 = *param_1;
        uVar7 = 0;
        puVar12 = param_1;
        do {
          uVar14 = uVar7 << 1 | 1;
          uVar10 = uVar7 * 2 + 2;
          puVar13 = puVar12 + uVar7 + 1;
          if ((long)uVar10 < lVar8) {
            uVar5 = puVar12[uVar7 + 2];
            uVar4 = puVar12[uVar7 + 1];
            uVar15 = uVar4;
            if ((short)uVar4 <= (short)uVar5) {
              uVar15 = uVar5;
            }
            puVar9 = puVar12 + uVar7 + 2;
            uVar7 = uVar10;
            if ((short)uVar5 <= (short)uVar4) {
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
          *puVar9 = uVar19;
        }
        else {
          lVar11 = (long)puVar9 + (2 - (long)param_1) >> 1;
          *puVar9 = *param_2;
          *param_2 = uVar19;
          if (1 < lVar11) {
            uVar7 = lVar11 - 2U >> 1;
            uVar19 = *puVar9;
            uVar15 = param_1[uVar7];
            puVar12 = param_1 + uVar7;
            if ((short)uVar15 < (short)uVar19) {
              do {
                puVar13 = puVar12;
                *puVar9 = uVar15;
                if (uVar7 == 0) break;
                uVar7 = uVar7 - 1 >> 1;
                uVar15 = param_1[uVar7];
                puVar9 = puVar13;
                puVar12 = param_1 + uVar7;
              } while ((short)uVar15 < (short)uVar19);
              *puVar13 = uVar19;
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
<a id="insn-00bebff8"></a> `00bebff8` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bebffc"></a> `00bebffc` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-00bec000"></a> `00bec000` | `e0 0f 00 54` | b.eq 0x00bec1fc | `CONDITIONAL_JUMP`
<a id="insn-00bec004"></a> `00bec004` | `29 00 00 cb` | sub x9,x1,x0 | `FALL_THROUGH`
<a id="insn-00bec008"></a> `00bec008` | `28 fd 41 93` | asr x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bec00c"></a> `00bec00c` | `0a 09 00 f1` | subs x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bec010"></a> `00bec010` | `0b 07 00 54` | b.lt 0x00bec0f0 | `CONDITIONAL_JUMP`
<a id="insn-00bec014"></a> `00bec014` | `4b fd 41 d3` | lsr x11,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bec018"></a> `00bec018` | `ec 03 0b aa` | mov x12,x11 | `FALL_THROUGH`
<a id="insn-00bec01c"></a> `00bec01c` | `05 00 00 14` | b 0x00bec030 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec020"></a> `00bec020` | `0f 02 00 79` | strh w15,[x16] | `FALL_THROUGH`
<a id="insn-00bec024"></a> `00bec024` | `9f 01 00 f1` | cmp x12,#0x0 | `FALL_THROUGH`
<a id="insn-00bec028"></a> `00bec028` | `8c 05 00 d1` | sub x12,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00bec02c"></a> `00bec02c` | `2d 06 00 54` | b.le 0x00bec0f0 | `CONDITIONAL_JUMP`
<a id="insn-00bec030"></a> `00bec030` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-00bec034"></a> `00bec034` | `8b ff ff 54` | b.lt 0x00bec024 | `CONDITIONAL_JUMP`
<a id="insn-00bec038"></a> `00bec038` | `2e 00 80 52` | mov w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bec03c"></a> `00bec03c` | `8d f9 7f d3` | lsl x13,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00bec040"></a> `00bec040` | `8e f9 7f b3` | bfm x14,x12,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bec044"></a> `00bec044` | `af 09 00 91` | add x15,x13,#0x2 | `FALL_THROUGH`
<a id="insn-00bec048"></a> `00bec048` | `0d 04 0e 8b` | add x13,x0,x14, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00bec04c"></a> `00bec04c` | `ff 01 08 eb` | cmp x15,x8 | `FALL_THROUGH`
<a id="insn-00bec050"></a> `00bec050` | `2a 01 00 54` | b.ge 0x00bec074 | `CONDITIONAL_JUMP`
<a id="insn-00bec054"></a> `00bec054` | `f0 03 0d aa` | mov x16,x13 | `FALL_THROUGH`
<a id="insn-00bec058"></a> `00bec058` | `b1 01 c0 79` | ldrsh w17,[x13] | `FALL_THROUGH`
<a id="insn-00bec05c"></a> `00bec05c` | `03 2e c0 78` | ldrsh w3,[x16, #0x2]! | `FALL_THROUGH`
<a id="insn-00bec060"></a> `00bec060` | `3f 02 03 6b` | cmp w17,w3 | `FALL_THROUGH`
<a id="insn-00bec064"></a> `00bec064` | `31 c2 83 1a` | csel w17,w17,w3,gt | `FALL_THROUGH`
<a id="insn-00bec068"></a> `00bec068` | `0d b2 8d 9a` | csel x13,x16,x13,lt | `FALL_THROUGH`
<a id="insn-00bec06c"></a> `00bec06c` | `ee b1 8e 9a` | csel x14,x15,x14,lt | `FALL_THROUGH`
<a id="insn-00bec070"></a> `00bec070` | `02 00 00 14` | b 0x00bec078 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec074"></a> `00bec074` | `b1 01 40 79` | ldrh w17,[x13] | `FALL_THROUGH`
<a id="insn-00bec078"></a> `00bec078` | `10 04 0c 8b` | add x16,x0,x12, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00bec07c"></a> `00bec07c` | `0f 02 c0 79` | ldrsh w15,[x16] | `FALL_THROUGH`
<a id="insn-00bec080"></a> `00bec080` | `ff a1 31 6b` | cmp w15,w17, SXTH  | `FALL_THROUGH`
<a id="insn-00bec084"></a> `00bec084` | `6d 01 00 54` | b.le 0x00bec0b0 | `CONDITIONAL_JUMP`
<a id="insn-00bec088"></a> `00bec088` | `e7 ff ff 17` | b 0x00bec024 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec08c"></a> `00bec08c` | `e4 03 0d aa` | mov x4,x13 | `FALL_THROUGH`
<a id="insn-00bec090"></a> `00bec090` | `b1 01 c0 79` | ldrsh w17,[x13] | `FALL_THROUGH`
<a id="insn-00bec094"></a> `00bec094` | `85 2c c0 78` | ldrsh w5,[x4, #0x2]! | `FALL_THROUGH`
<a id="insn-00bec098"></a> `00bec098` | `3f 02 05 6b` | cmp w17,w5 | `FALL_THROUGH`
<a id="insn-00bec09c"></a> `00bec09c` | `31 c2 85 1a` | csel w17,w17,w5,gt | `FALL_THROUGH`
<a id="insn-00bec0a0"></a> `00bec0a0` | `8d b0 8d 9a` | csel x13,x4,x13,lt | `FALL_THROUGH`
<a id="insn-00bec0a4"></a> `00bec0a4` | `ce b1 83 9a` | csel x14,x14,x3,lt | `FALL_THROUGH`
<a id="insn-00bec0a8"></a> `00bec0a8` | `ff a1 31 6b` | cmp w15,w17, SXTH  | `FALL_THROUGH`
<a id="insn-00bec0ac"></a> `00bec0ac` | `ac fb ff 54` | b.gt 0x00bec020 | `CONDITIONAL_JUMP`
<a id="insn-00bec0b0"></a> `00bec0b0` | `7f 01 0e eb` | cmp x11,x14 | `FALL_THROUGH`
<a id="insn-00bec0b4"></a> `00bec0b4` | `11 02 00 79` | strh w17,[x16] | `FALL_THROUGH`
<a id="insn-00bec0b8"></a> `00bec0b8` | `f0 03 0d aa` | mov x16,x13 | `FALL_THROUGH`
<a id="insn-00bec0bc"></a> `00bec0bc` | `2b fb ff 54` | b.lt 0x00bec020 | `CONDITIONAL_JUMP`
<a id="insn-00bec0c0"></a> `00bec0c0` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bec0c4"></a> `00bec0c4` | `cd f9 7f d3` | lsl x13,x14,#0x1 | `FALL_THROUGH`
<a id="insn-00bec0c8"></a> `00bec0c8` | `c3 f9 7f b3` | bfm x3,x14,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bec0cc"></a> `00bec0cc` | `ae 09 00 91` | add x14,x13,#0x2 | `FALL_THROUGH`
<a id="insn-00bec0d0"></a> `00bec0d0` | `0d 04 03 8b` | add x13,x0,x3, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00bec0d4"></a> `00bec0d4` | `df 01 08 eb` | cmp x14,x8 | `FALL_THROUGH`
<a id="insn-00bec0d8"></a> `00bec0d8` | `ab fd ff 54` | b.lt 0x00bec08c | `CONDITIONAL_JUMP`
<a id="insn-00bec0dc"></a> `00bec0dc` | `b1 01 40 79` | ldrh w17,[x13] | `FALL_THROUGH`
<a id="insn-00bec0e0"></a> `00bec0e0` | `ee 03 03 aa` | mov x14,x3 | `FALL_THROUGH`
<a id="insn-00bec0e4"></a> `00bec0e4` | `ff a1 31 6b` | cmp w15,w17, SXTH  | `FALL_THROUGH`
<a id="insn-00bec0e8"></a> `00bec0e8` | `4d fe ff 54` | b.le 0x00bec0b0 | `CONDITIONAL_JUMP`
<a id="insn-00bec0ec"></a> `00bec0ec` | `cd ff ff 17` | b 0x00bec020 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec0f0"></a> `00bec0f0` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-00bec0f4"></a> `00bec0f4` | `e3 03 01 aa` | mov x3,x1 | `FALL_THROUGH`
<a id="insn-00bec0f8"></a> `00bec0f8` | `c0 07 00 54` | b.eq 0x00bec1f0 | `CONDITIONAL_JUMP`
<a id="insn-00bec0fc"></a> `00bec0fc` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bec100"></a> `00bec100` | `0b 08 00 91` | add x11,x0,#0x2 | `FALL_THROUGH`
<a id="insn-00bec104"></a> `00bec104` | `0c 10 00 91` | add x12,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00bec108"></a> `00bec108` | `2d 00 80 52` | mov w13,#0x1 | `FALL_THROUGH`
<a id="insn-00bec10c"></a> `00bec10c` | `ee 03 01 aa` | mov x14,x1 | `FALL_THROUGH`
<a id="insn-00bec110"></a> `00bec110` | `05 00 00 14` | b 0x00bec124 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec114"></a> `00bec114` | `6f 00 00 79` | strh w15,[x3] | `FALL_THROUGH`
<a id="insn-00bec118"></a> `00bec118` | `ce 09 00 91` | add x14,x14,#0x2 | `FALL_THROUGH`
<a id="insn-00bec11c"></a> `00bec11c` | `df 01 02 eb` | cmp x14,x2 | `FALL_THROUGH`
<a id="insn-00bec120"></a> `00bec120` | `60 06 00 54` | b.eq 0x00bec1ec | `CONDITIONAL_JUMP`
<a id="insn-00bec124"></a> `00bec124` | `cf 01 c0 79` | ldrsh w15,[x14] | `FALL_THROUGH`
<a id="insn-00bec128"></a> `00bec128` | `10 00 c0 79` | ldrsh w16,[x0] | `FALL_THROUGH`
<a id="insn-00bec12c"></a> `00bec12c` | `ff 01 10 6b` | cmp w15,w16 | `FALL_THROUGH`
<a id="insn-00bec130"></a> `00bec130` | `4a ff ff 54` | b.ge 0x00bec118 | `CONDITIONAL_JUMP`
<a id="insn-00bec134"></a> `00bec134` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bec138"></a> `00bec138` | `d0 01 00 79` | strh w16,[x14] | `FALL_THROUGH`
<a id="insn-00bec13c"></a> `00bec13c` | `0f 00 00 79` | strh w15,[x0] | `FALL_THROUGH`
<a id="insn-00bec140"></a> `00bec140` | `cb fe ff 54` | b.lt 0x00bec118 | `CONDITIONAL_JUMP`
<a id="insn-00bec144"></a> `00bec144` | `71 01 c0 79` | ldrsh w17,[x11] | `FALL_THROUGH`
<a id="insn-00bec148"></a> `00bec148` | `3f 11 00 f1` | cmp x9,#0x4 | `FALL_THROUGH`
<a id="insn-00bec14c"></a> `00bec14c` | `c1 00 00 54` | b.ne 0x00bec164 | `CONDITIONAL_JUMP`
<a id="insn-00bec150"></a> `00bec150` | `f0 03 0b aa` | mov x16,x11 | `FALL_THROUGH`
<a id="insn-00bec154"></a> `00bec154` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-00bec158"></a> `00bec158` | `ff a1 31 6b` | cmp w15,w17, SXTH  | `FALL_THROUGH`
<a id="insn-00bec15c"></a> `00bec15c` | `ec fd ff 54` | b.gt 0x00bec118 | `CONDITIONAL_JUMP`
<a id="insn-00bec160"></a> `00bec160` | `08 00 00 14` | b 0x00bec180 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec164"></a> `00bec164` | `90 01 c0 79` | ldrsh w16,[x12] | `FALL_THROUGH`
<a id="insn-00bec168"></a> `00bec168` | `3f 02 10 6b` | cmp w17,w16 | `FALL_THROUGH`
<a id="insn-00bec16c"></a> `00bec16c` | `31 c2 90 1a` | csel w17,w17,w16,gt | `FALL_THROUGH`
<a id="insn-00bec170"></a> `00bec170` | `90 b1 8b 9a` | csel x16,x12,x11,lt | `FALL_THROUGH`
<a id="insn-00bec174"></a> `00bec174` | `a4 a5 8d 9a` | cinc x4,x13,lt | `FALL_THROUGH`
<a id="insn-00bec178"></a> `00bec178` | `ff a1 31 6b` | cmp w15,w17, SXTH  | `FALL_THROUGH`
<a id="insn-00bec17c"></a> `00bec17c` | `ec fc ff 54` | b.gt 0x00bec118 | `CONDITIONAL_JUMP`
<a id="insn-00bec180"></a> `00bec180` | `e3 03 00 aa` | mov x3,x0 | `FALL_THROUGH`
<a id="insn-00bec184"></a> `00bec184` | `0a 00 00 14` | b 0x00bec1ac | `UNCONDITIONAL_JUMP`
<a id="insn-00bec188"></a> `00bec188` | `e6 03 10 aa` | mov x6,x16 | `FALL_THROUGH`
<a id="insn-00bec18c"></a> `00bec18c` | `11 02 c0 79` | ldrsh w17,[x16] | `FALL_THROUGH`
<a id="insn-00bec190"></a> `00bec190` | `c7 2c c0 78` | ldrsh w7,[x6, #0x2]! | `FALL_THROUGH`
<a id="insn-00bec194"></a> `00bec194` | `3f 02 07 6b` | cmp w17,w7 | `FALL_THROUGH`
<a id="insn-00bec198"></a> `00bec198` | `31 c2 87 1a` | csel w17,w17,w7,gt | `FALL_THROUGH`
<a id="insn-00bec19c"></a> `00bec19c` | `d0 b0 90 9a` | csel x16,x6,x16,lt | `FALL_THROUGH`
<a id="insn-00bec1a0"></a> `00bec1a0` | `84 b0 85 9a` | csel x4,x4,x5,lt | `FALL_THROUGH`
<a id="insn-00bec1a4"></a> `00bec1a4` | `ff a1 31 6b` | cmp w15,w17, SXTH  | `FALL_THROUGH`
<a id="insn-00bec1a8"></a> `00bec1a8` | `6c fb ff 54` | b.gt 0x00bec114 | `CONDITIONAL_JUMP`
<a id="insn-00bec1ac"></a> `00bec1ac` | `5f 01 04 eb` | cmp x10,x4 | `FALL_THROUGH`
<a id="insn-00bec1b0"></a> `00bec1b0` | `71 00 00 79` | strh w17,[x3] | `FALL_THROUGH`
<a id="insn-00bec1b4"></a> `00bec1b4` | `e3 03 10 aa` | mov x3,x16 | `FALL_THROUGH`
<a id="insn-00bec1b8"></a> `00bec1b8` | `eb fa ff 54` | b.lt 0x00bec114 | `CONDITIONAL_JUMP`
<a id="insn-00bec1bc"></a> `00bec1bc` | `25 00 80 52` | mov w5,#0x1 | `FALL_THROUGH`
<a id="insn-00bec1c0"></a> `00bec1c0` | `90 f8 7f d3` | lsl x16,x4,#0x1 | `FALL_THROUGH`
<a id="insn-00bec1c4"></a> `00bec1c4` | `85 f8 7f b3` | bfm x5,x4,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bec1c8"></a> `00bec1c8` | `04 0a 00 91` | add x4,x16,#0x2 | `FALL_THROUGH`
<a id="insn-00bec1cc"></a> `00bec1cc` | `10 04 05 8b` | add x16,x0,x5, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00bec1d0"></a> `00bec1d0` | `9f 00 08 eb` | cmp x4,x8 | `FALL_THROUGH`
<a id="insn-00bec1d4"></a> `00bec1d4` | `ab fd ff 54` | b.lt 0x00bec188 | `CONDITIONAL_JUMP`
<a id="insn-00bec1d8"></a> `00bec1d8` | `11 02 40 79` | ldrh w17,[x16] | `FALL_THROUGH`
<a id="insn-00bec1dc"></a> `00bec1dc` | `e4 03 05 aa` | mov x4,x5 | `FALL_THROUGH`
<a id="insn-00bec1e0"></a> `00bec1e0` | `ff a1 31 6b` | cmp w15,w17, SXTH  | `FALL_THROUGH`
<a id="insn-00bec1e4"></a> `00bec1e4` | `4d fe ff 54` | b.le 0x00bec1ac | `CONDITIONAL_JUMP`
<a id="insn-00bec1e8"></a> `00bec1e8` | `cb ff ff 17` | b 0x00bec114 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec1ec"></a> `00bec1ec` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bec1f0"></a> `00bec1f0` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bec1f4"></a> `00bec1f4` | `0a 01 00 54` | b.ge 0x00bec214 | `CONDITIONAL_JUMP`
<a id="insn-00bec1f8"></a> `00bec1f8` | `e2 03 03 aa` | mov x2,x3 | `FALL_THROUGH`
<a id="insn-00bec1fc"></a> `00bec1fc` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bec200"></a> `00bec200` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bec204"></a> `00bec204` | `2a 01 00 79` | strh w10,[x9] | `FALL_THROUGH`
<a id="insn-00bec208"></a> `00bec208` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bec20c"></a> `00bec20c` | `08 05 00 d1` | sub x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bec210"></a> `00bec210` | `4d ff ff 54` | b.le 0x00bec1f8 | `CONDITIONAL_JUMP`
<a id="insn-00bec214"></a> `00bec214` | `09 09 00 d1` | sub x9,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bec218"></a> `00bec218` | `0a 00 40 79` | ldrh w10,[x0] | `FALL_THROUGH`
<a id="insn-00bec21c"></a> `00bec21c` | `ed 03 1f aa` | mov x13,xzr | `FALL_THROUGH`
<a id="insn-00bec220"></a> `00bec220` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bec224"></a> `00bec224` | `ec 03 00 aa` | mov x12,x0 | `FALL_THROUGH`
<a id="insn-00bec228"></a> `00bec228` | `0b 00 00 14` | b 0x00bec254 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec22c"></a> `00bec22c` | `2d 4e c0 78` | ldrsh w13,[x17, #0x4]! | `FALL_THROUGH`
<a id="insn-00bec230"></a> `00bec230` | `2f e2 df 78` | ldursh w15,[x17, #-0x2] | `FALL_THROUGH`
<a id="insn-00bec234"></a> `00bec234` | `ff 01 0d 6b` | cmp w15,w13 | `FALL_THROUGH`
<a id="insn-00bec238"></a> `00bec238` | `ef c1 8d 1a` | csel w15,w15,w13,gt | `FALL_THROUGH`
<a id="insn-00bec23c"></a> `00bec23c` | `29 b2 89 9a` | csel x9,x17,x9,lt | `FALL_THROUGH`
<a id="insn-00bec240"></a> `00bec240` | `0d b2 8e 9a` | csel x13,x16,x14,lt | `FALL_THROUGH`
<a id="insn-00bec244"></a> `00bec244` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00bec248"></a> `00bec248` | `8f 01 00 79` | strh w15,[x12] | `FALL_THROUGH`
<a id="insn-00bec24c"></a> `00bec24c` | `ec 03 09 aa` | mov x12,x9 | `FALL_THROUGH`
<a id="insn-00bec250"></a> `00bec250` | `8c 01 00 54` | b.gt 0x00bec280 | `CONDITIONAL_JUMP`
<a id="insn-00bec254"></a> `00bec254` | `a9 f9 7f d3` | lsl x9,x13,#0x1 | `FALL_THROUGH`
<a id="insn-00bec258"></a> `00bec258` | `2e 00 80 52` | mov w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bec25c"></a> `00bec25c` | `ae f9 7f b3` | bfm x14,x13,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bec260"></a> `00bec260` | `30 09 00 91` | add x16,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bec264"></a> `00bec264` | `91 01 09 8b` | add x17,x12,x9 | `FALL_THROUGH`
<a id="insn-00bec268"></a> `00bec268` | `1f 02 08 eb` | cmp x16,x8 | `FALL_THROUGH`
<a id="insn-00bec26c"></a> `00bec26c` | `29 0a 00 91` | add x9,x17,#0x2 | `FALL_THROUGH`
<a id="insn-00bec270"></a> `00bec270` | `eb fd ff 54` | b.lt 0x00bec22c | `CONDITIONAL_JUMP`
<a id="insn-00bec274"></a> `00bec274` | `2f 01 40 79` | ldrh w15,[x9] | `FALL_THROUGH`
<a id="insn-00bec278"></a> `00bec278` | `ed 03 0e aa` | mov x13,x14 | `FALL_THROUGH`
<a id="insn-00bec27c"></a> `00bec27c` | `f2 ff ff 17` | b 0x00bec244 | `UNCONDITIONAL_JUMP`
<a id="insn-00bec280"></a> `00bec280` | `21 08 00 d1` | sub x1,x1,#0x2 | `FALL_THROUGH`
<a id="insn-00bec284"></a> `00bec284` | `3f 01 01 eb` | cmp x9,x1 | `FALL_THROUGH`
<a id="insn-00bec288"></a> `00bec288` | `e0 fb ff 54` | b.eq 0x00bec204 | `CONDITIONAL_JUMP`
<a id="insn-00bec28c"></a> `00bec28c` | `2b 01 00 cb` | sub x11,x9,x0 | `FALL_THROUGH`
<a id="insn-00bec290"></a> `00bec290` | `2c 00 40 79` | ldrh w12,[x1] | `FALL_THROUGH`
<a id="insn-00bec294"></a> `00bec294` | `6b 09 00 91` | add x11,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00bec298"></a> `00bec298` | `6b fd 41 93` | asr x11,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00bec29c"></a> `00bec29c` | `2c 01 00 79` | strh w12,[x9] | `FALL_THROUGH`
<a id="insn-00bec2a0"></a> `00bec2a0` | `2a 00 00 79` | strh w10,[x1] | `FALL_THROUGH`
<a id="insn-00bec2a4"></a> `00bec2a4` | `6b 09 00 f1` | subs x11,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00bec2a8"></a> `00bec2a8` | `0b fb ff 54` | b.lt 0x00bec208 | `CONDITIONAL_JUMP`
<a id="insn-00bec2ac"></a> `00bec2ac` | `6a fd 41 d3` | lsr x10,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00bec2b0"></a> `00bec2b0` | `2b 01 c0 79` | ldrsh w11,[x9] | `FALL_THROUGH`
<a id="insn-00bec2b4"></a> `00bec2b4` | `0c 04 0a 8b` | add x12,x0,x10, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00bec2b8"></a> `00bec2b8` | `8d 01 c0 79` | ldrsh w13,[x12] | `FALL_THROUGH`
<a id="insn-00bec2bc"></a> `00bec2bc` | `bf 01 0b 6b` | cmp w13,w11 | `FALL_THROUGH`
<a id="insn-00bec2c0"></a> `00bec2c0` | `4a fa ff 54` | b.ge 0x00bec208 | `CONDITIONAL_JUMP`
<a id="insn-00bec2c4"></a> `00bec2c4` | `ee 03 09 aa` | mov x14,x9 | `FALL_THROUGH`
<a id="insn-00bec2c8"></a> `00bec2c8` | `e9 03 0c aa` | mov x9,x12 | `FALL_THROUGH`
<a id="insn-00bec2cc"></a> `00bec2cc` | `cd 01 00 79` | strh w13,[x14] | `FALL_THROUGH`
<a id="insn-00bec2d0"></a> `00bec2d0` | `ea 00 00 b4` | cbz x10,0x00bec2ec | `CONDITIONAL_JUMP`
<a id="insn-00bec2d4"></a> `00bec2d4` | `4a 05 00 d1` | sub x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bec2d8"></a> `00bec2d8` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bec2dc"></a> `00bec2dc` | `0c 04 0a 8b` | add x12,x0,x10, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00bec2e0"></a> `00bec2e0` | `8d 01 c0 79` | ldrsh w13,[x12] | `FALL_THROUGH`
<a id="insn-00bec2e4"></a> `00bec2e4` | `bf 01 0b 6b` | cmp w13,w11 | `FALL_THROUGH`
<a id="insn-00bec2e8"></a> `00bec2e8` | `eb fe ff 54` | b.lt 0x00bec2c4 | `CONDITIONAL_JUMP`
<a id="insn-00bec2ec"></a> `00bec2ec` | `2b 01 00 79` | strh w11,[x9] | `FALL_THROUGH`
<a id="insn-00bec2f0"></a> `00bec2f0` | `c6 ff ff 17` | b 0x00bec208 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bebff8`](#insn-00bebff8) 範囲 `[['00bebff8', '00bec003']]`
  - `CONDITIONAL_JUMP` [`00bec000`](#insn-00bec000) → [`00bec1fc`](#insn-00bec1fc)
  - `FALL_THROUGH` [`00bec000`](#insn-00bec000) → [`00bec004`](#insn-00bec004)
- ブロック [`00bec004`](#insn-00bec004) 範囲 `[['00bec004', '00bec013']]`
  - `CONDITIONAL_JUMP` [`00bec010`](#insn-00bec010) → [`00bec0f0`](#insn-00bec0f0)
  - `FALL_THROUGH` [`00bec010`](#insn-00bec010) → [`00bec014`](#insn-00bec014)
- ブロック [`00bec014`](#insn-00bec014) 範囲 `[['00bec014', '00bec01f']]`
  - `UNCONDITIONAL_JUMP` [`00bec01c`](#insn-00bec01c) → [`00bec030`](#insn-00bec030)
- ブロック [`00bec020`](#insn-00bec020) 範囲 `[['00bec020', '00bec023']]`
  - `FALL_THROUGH` [`00bec020`](#insn-00bec020) → [`00bec024`](#insn-00bec024)
- ブロック [`00bec024`](#insn-00bec024) 範囲 `[['00bec024', '00bec02f']]`
  - `CONDITIONAL_JUMP` [`00bec02c`](#insn-00bec02c) → [`00bec0f0`](#insn-00bec0f0)
  - `FALL_THROUGH` [`00bec02c`](#insn-00bec02c) → [`00bec030`](#insn-00bec030)
- ブロック [`00bec030`](#insn-00bec030) 範囲 `[['00bec030', '00bec037']]`
  - `CONDITIONAL_JUMP` [`00bec034`](#insn-00bec034) → [`00bec024`](#insn-00bec024)
  - `FALL_THROUGH` [`00bec034`](#insn-00bec034) → [`00bec038`](#insn-00bec038)
- ブロック [`00bec038`](#insn-00bec038) 範囲 `[['00bec038', '00bec053']]`
  - `CONDITIONAL_JUMP` [`00bec050`](#insn-00bec050) → [`00bec074`](#insn-00bec074)
  - `FALL_THROUGH` [`00bec050`](#insn-00bec050) → [`00bec054`](#insn-00bec054)
- ブロック [`00bec054`](#insn-00bec054) 範囲 `[['00bec054', '00bec073']]`
  - `UNCONDITIONAL_JUMP` [`00bec070`](#insn-00bec070) → [`00bec078`](#insn-00bec078)
- ブロック [`00bec074`](#insn-00bec074) 範囲 `[['00bec074', '00bec077']]`
  - `FALL_THROUGH` [`00bec074`](#insn-00bec074) → [`00bec078`](#insn-00bec078)
- ブロック [`00bec078`](#insn-00bec078) 範囲 `[['00bec078', '00bec087']]`
  - `CONDITIONAL_JUMP` [`00bec084`](#insn-00bec084) → [`00bec0b0`](#insn-00bec0b0)
  - `FALL_THROUGH` [`00bec084`](#insn-00bec084) → [`00bec088`](#insn-00bec088)
- ブロック [`00bec088`](#insn-00bec088) 範囲 `[['00bec088', '00bec08b']]`
  - `UNCONDITIONAL_JUMP` [`00bec088`](#insn-00bec088) → [`00bec024`](#insn-00bec024)
- ブロック [`00bec08c`](#insn-00bec08c) 範囲 `[['00bec08c', '00bec0af']]`
  - `CONDITIONAL_JUMP` [`00bec0ac`](#insn-00bec0ac) → [`00bec020`](#insn-00bec020)
  - `FALL_THROUGH` [`00bec0ac`](#insn-00bec0ac) → [`00bec0b0`](#insn-00bec0b0)
- ブロック [`00bec0b0`](#insn-00bec0b0) 範囲 `[['00bec0b0', '00bec0bf']]`
  - `CONDITIONAL_JUMP` [`00bec0bc`](#insn-00bec0bc) → [`00bec020`](#insn-00bec020)
  - `FALL_THROUGH` [`00bec0bc`](#insn-00bec0bc) → [`00bec0c0`](#insn-00bec0c0)
- ブロック [`00bec0c0`](#insn-00bec0c0) 範囲 `[['00bec0c0', '00bec0db']]`
  - `CONDITIONAL_JUMP` [`00bec0d8`](#insn-00bec0d8) → [`00bec08c`](#insn-00bec08c)
  - `FALL_THROUGH` [`00bec0d8`](#insn-00bec0d8) → [`00bec0dc`](#insn-00bec0dc)
- ブロック [`00bec0dc`](#insn-00bec0dc) 範囲 `[['00bec0dc', '00bec0eb']]`
  - `CONDITIONAL_JUMP` [`00bec0e8`](#insn-00bec0e8) → [`00bec0b0`](#insn-00bec0b0)
  - `FALL_THROUGH` [`00bec0e8`](#insn-00bec0e8) → [`00bec0ec`](#insn-00bec0ec)
- ブロック [`00bec0ec`](#insn-00bec0ec) 範囲 `[['00bec0ec', '00bec0ef']]`
  - `UNCONDITIONAL_JUMP` [`00bec0ec`](#insn-00bec0ec) → [`00bec020`](#insn-00bec020)
- ブロック [`00bec0f0`](#insn-00bec0f0) 範囲 `[['00bec0f0', '00bec0fb']]`
  - `CONDITIONAL_JUMP` [`00bec0f8`](#insn-00bec0f8) → [`00bec1f0`](#insn-00bec1f0)
  - `FALL_THROUGH` [`00bec0f8`](#insn-00bec0f8) → [`00bec0fc`](#insn-00bec0fc)
- ブロック [`00bec0fc`](#insn-00bec0fc) 範囲 `[['00bec0fc', '00bec113']]`
  - `UNCONDITIONAL_JUMP` [`00bec110`](#insn-00bec110) → [`00bec124`](#insn-00bec124)
- ブロック [`00bec114`](#insn-00bec114) 範囲 `[['00bec114', '00bec117']]`
  - `FALL_THROUGH` [`00bec114`](#insn-00bec114) → [`00bec118`](#insn-00bec118)
- ブロック [`00bec118`](#insn-00bec118) 範囲 `[['00bec118', '00bec123']]`
  - `CONDITIONAL_JUMP` [`00bec120`](#insn-00bec120) → [`00bec1ec`](#insn-00bec1ec)
  - `FALL_THROUGH` [`00bec120`](#insn-00bec120) → [`00bec124`](#insn-00bec124)
- ブロック [`00bec124`](#insn-00bec124) 範囲 `[['00bec124', '00bec133']]`
  - `CONDITIONAL_JUMP` [`00bec130`](#insn-00bec130) → [`00bec118`](#insn-00bec118)
  - `FALL_THROUGH` [`00bec130`](#insn-00bec130) → [`00bec134`](#insn-00bec134)
- ブロック [`00bec134`](#insn-00bec134) 範囲 `[['00bec134', '00bec143']]`
  - `CONDITIONAL_JUMP` [`00bec140`](#insn-00bec140) → [`00bec118`](#insn-00bec118)
  - `FALL_THROUGH` [`00bec140`](#insn-00bec140) → [`00bec144`](#insn-00bec144)
- ブロック [`00bec144`](#insn-00bec144) 範囲 `[['00bec144', '00bec14f']]`
  - `CONDITIONAL_JUMP` [`00bec14c`](#insn-00bec14c) → [`00bec164`](#insn-00bec164)
  - `FALL_THROUGH` [`00bec14c`](#insn-00bec14c) → [`00bec150`](#insn-00bec150)
- ブロック [`00bec150`](#insn-00bec150) 範囲 `[['00bec150', '00bec15f']]`
  - `CONDITIONAL_JUMP` [`00bec15c`](#insn-00bec15c) → [`00bec118`](#insn-00bec118)
  - `FALL_THROUGH` [`00bec15c`](#insn-00bec15c) → [`00bec160`](#insn-00bec160)
- ブロック [`00bec160`](#insn-00bec160) 範囲 `[['00bec160', '00bec163']]`
  - `UNCONDITIONAL_JUMP` [`00bec160`](#insn-00bec160) → [`00bec180`](#insn-00bec180)
- ブロック [`00bec164`](#insn-00bec164) 範囲 `[['00bec164', '00bec17f']]`
  - `CONDITIONAL_JUMP` [`00bec17c`](#insn-00bec17c) → [`00bec118`](#insn-00bec118)
  - `FALL_THROUGH` [`00bec17c`](#insn-00bec17c) → [`00bec180`](#insn-00bec180)
- ブロック [`00bec180`](#insn-00bec180) 範囲 `[['00bec180', '00bec187']]`
  - `UNCONDITIONAL_JUMP` [`00bec184`](#insn-00bec184) → [`00bec1ac`](#insn-00bec1ac)
- ブロック [`00bec188`](#insn-00bec188) 範囲 `[['00bec188', '00bec1ab']]`
  - `CONDITIONAL_JUMP` [`00bec1a8`](#insn-00bec1a8) → [`00bec114`](#insn-00bec114)
  - `FALL_THROUGH` [`00bec1a8`](#insn-00bec1a8) → [`00bec1ac`](#insn-00bec1ac)
- ブロック [`00bec1ac`](#insn-00bec1ac) 範囲 `[['00bec1ac', '00bec1bb']]`
  - `CONDITIONAL_JUMP` [`00bec1b8`](#insn-00bec1b8) → [`00bec114`](#insn-00bec114)
  - `FALL_THROUGH` [`00bec1b8`](#insn-00bec1b8) → [`00bec1bc`](#insn-00bec1bc)
- ブロック [`00bec1bc`](#insn-00bec1bc) 範囲 `[['00bec1bc', '00bec1d7']]`
  - `CONDITIONAL_JUMP` [`00bec1d4`](#insn-00bec1d4) → [`00bec188`](#insn-00bec188)
  - `FALL_THROUGH` [`00bec1d4`](#insn-00bec1d4) → [`00bec1d8`](#insn-00bec1d8)
- ブロック [`00bec1d8`](#insn-00bec1d8) 範囲 `[['00bec1d8', '00bec1e7']]`
  - `CONDITIONAL_JUMP` [`00bec1e4`](#insn-00bec1e4) → [`00bec1ac`](#insn-00bec1ac)
  - `FALL_THROUGH` [`00bec1e4`](#insn-00bec1e4) → [`00bec1e8`](#insn-00bec1e8)
- ブロック [`00bec1e8`](#insn-00bec1e8) 範囲 `[['00bec1e8', '00bec1eb']]`
  - `UNCONDITIONAL_JUMP` [`00bec1e8`](#insn-00bec1e8) → [`00bec114`](#insn-00bec114)
- ブロック [`00bec1ec`](#insn-00bec1ec) 範囲 `[['00bec1ec', '00bec1ef']]`
  - `FALL_THROUGH` [`00bec1ec`](#insn-00bec1ec) → [`00bec1f0`](#insn-00bec1f0)
- ブロック [`00bec1f0`](#insn-00bec1f0) 範囲 `[['00bec1f0', '00bec1f7']]`
  - `CONDITIONAL_JUMP` [`00bec1f4`](#insn-00bec1f4) → [`00bec214`](#insn-00bec214)
  - `FALL_THROUGH` [`00bec1f4`](#insn-00bec1f4) → [`00bec1f8`](#insn-00bec1f8)
- ブロック [`00bec1f8`](#insn-00bec1f8) 範囲 `[['00bec1f8', '00bec1fb']]`
  - `FALL_THROUGH` [`00bec1f8`](#insn-00bec1f8) → [`00bec1fc`](#insn-00bec1fc)
- ブロック [`00bec1fc`](#insn-00bec1fc) 範囲 `[['00bec1fc', '00bec203']]`
- ブロック [`00bec204`](#insn-00bec204) 範囲 `[['00bec204', '00bec207']]`
  - `FALL_THROUGH` [`00bec204`](#insn-00bec204) → [`00bec208`](#insn-00bec208)
- ブロック [`00bec208`](#insn-00bec208) 範囲 `[['00bec208', '00bec213']]`
  - `CONDITIONAL_JUMP` [`00bec210`](#insn-00bec210) → [`00bec1f8`](#insn-00bec1f8)
  - `FALL_THROUGH` [`00bec210`](#insn-00bec210) → [`00bec214`](#insn-00bec214)
- ブロック [`00bec214`](#insn-00bec214) 範囲 `[['00bec214', '00bec22b']]`
  - `UNCONDITIONAL_JUMP` [`00bec228`](#insn-00bec228) → [`00bec254`](#insn-00bec254)
- ブロック [`00bec22c`](#insn-00bec22c) 範囲 `[['00bec22c', '00bec243']]`
  - `FALL_THROUGH` [`00bec240`](#insn-00bec240) → [`00bec244`](#insn-00bec244)
- ブロック [`00bec244`](#insn-00bec244) 範囲 `[['00bec244', '00bec253']]`
  - `CONDITIONAL_JUMP` [`00bec250`](#insn-00bec250) → [`00bec280`](#insn-00bec280)
  - `FALL_THROUGH` [`00bec250`](#insn-00bec250) → [`00bec254`](#insn-00bec254)
- ブロック [`00bec254`](#insn-00bec254) 範囲 `[['00bec254', '00bec273']]`
  - `CONDITIONAL_JUMP` [`00bec270`](#insn-00bec270) → [`00bec22c`](#insn-00bec22c)
  - `FALL_THROUGH` [`00bec270`](#insn-00bec270) → [`00bec274`](#insn-00bec274)
- ブロック [`00bec274`](#insn-00bec274) 範囲 `[['00bec274', '00bec27f']]`
  - `UNCONDITIONAL_JUMP` [`00bec27c`](#insn-00bec27c) → [`00bec244`](#insn-00bec244)
- ブロック [`00bec280`](#insn-00bec280) 範囲 `[['00bec280', '00bec28b']]`
  - `CONDITIONAL_JUMP` [`00bec288`](#insn-00bec288) → [`00bec204`](#insn-00bec204)
  - `FALL_THROUGH` [`00bec288`](#insn-00bec288) → [`00bec28c`](#insn-00bec28c)
- ブロック [`00bec28c`](#insn-00bec28c) 範囲 `[['00bec28c', '00bec2ab']]`
  - `CONDITIONAL_JUMP` [`00bec2a8`](#insn-00bec2a8) → [`00bec208`](#insn-00bec208)
  - `FALL_THROUGH` [`00bec2a8`](#insn-00bec2a8) → [`00bec2ac`](#insn-00bec2ac)
- ブロック [`00bec2ac`](#insn-00bec2ac) 範囲 `[['00bec2ac', '00bec2c3']]`
  - `CONDITIONAL_JUMP` [`00bec2c0`](#insn-00bec2c0) → [`00bec208`](#insn-00bec208)
  - `FALL_THROUGH` [`00bec2c0`](#insn-00bec2c0) → [`00bec2c4`](#insn-00bec2c4)
- ブロック [`00bec2c4`](#insn-00bec2c4) 範囲 `[['00bec2c4', '00bec2d3']]`
  - `CONDITIONAL_JUMP` [`00bec2d0`](#insn-00bec2d0) → [`00bec2ec`](#insn-00bec2ec)
  - `FALL_THROUGH` [`00bec2d0`](#insn-00bec2d0) → [`00bec2d4`](#insn-00bec2d4)
- ブロック [`00bec2d4`](#insn-00bec2d4) 範囲 `[['00bec2d4', '00bec2eb']]`
  - `CONDITIONAL_JUMP` [`00bec2e8`](#insn-00bec2e8) → [`00bec2c4`](#insn-00bec2c4)
  - `FALL_THROUGH` [`00bec2e8`](#insn-00bec2e8) → [`00bec2ec`](#insn-00bec2ec)
- ブロック [`00bec2ec`](#insn-00bec2ec) 範囲 `[['00bec2ec', '00bec2f3']]`
  - `UNCONDITIONAL_JUMP` [`00bec2f0`](#insn-00bec2f0) → [`00bec208`](#insn-00bec208)

## 命令位置別の参照

- [`00bec000`](#insn-00bec000) → [`00bec1fc`](#insn-00bec1fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec010`](#insn-00bec010) → [`00bec0f0`](#insn-00bec0f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec01c`](#insn-00bec01c) → [`00bec030`](#insn-00bec030) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec02c`](#insn-00bec02c) → [`00bec0f0`](#insn-00bec0f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec034`](#insn-00bec034) → [`00bec024`](#insn-00bec024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec050`](#insn-00bec050) → [`00bec074`](#insn-00bec074) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec070`](#insn-00bec070) → [`00bec078`](#insn-00bec078) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec084`](#insn-00bec084) → [`00bec0b0`](#insn-00bec0b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec088`](#insn-00bec088) → [`00bec024`](#insn-00bec024) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec0ac`](#insn-00bec0ac) → [`00bec020`](#insn-00bec020) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec0bc`](#insn-00bec0bc) → [`00bec020`](#insn-00bec020) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec0d8`](#insn-00bec0d8) → [`00bec08c`](#insn-00bec08c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec0e8`](#insn-00bec0e8) → [`00bec0b0`](#insn-00bec0b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec0ec`](#insn-00bec0ec) → [`00bec020`](#insn-00bec020) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec0f8`](#insn-00bec0f8) → [`00bec1f0`](#insn-00bec1f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec110`](#insn-00bec110) → [`00bec124`](#insn-00bec124) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec120`](#insn-00bec120) → [`00bec1ec`](#insn-00bec1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec130`](#insn-00bec130) → [`00bec118`](#insn-00bec118) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec140`](#insn-00bec140) → [`00bec118`](#insn-00bec118) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec14c`](#insn-00bec14c) → [`00bec164`](#insn-00bec164) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec15c`](#insn-00bec15c) → [`00bec118`](#insn-00bec118) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec160`](#insn-00bec160) → [`00bec180`](#insn-00bec180) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec17c`](#insn-00bec17c) → [`00bec118`](#insn-00bec118) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec184`](#insn-00bec184) → [`00bec1ac`](#insn-00bec1ac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec1a8`](#insn-00bec1a8) → [`00bec114`](#insn-00bec114) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec1b8`](#insn-00bec1b8) → [`00bec114`](#insn-00bec114) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec1d4`](#insn-00bec1d4) → [`00bec188`](#insn-00bec188) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec1e4`](#insn-00bec1e4) → [`00bec1ac`](#insn-00bec1ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec1e8`](#insn-00bec1e8) → [`00bec114`](#insn-00bec114) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec1f4`](#insn-00bec1f4) → [`00bec214`](#insn-00bec214) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec210`](#insn-00bec210) → [`00bec1f8`](#insn-00bec1f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec228`](#insn-00bec228) → [`00bec254`](#insn-00bec254) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec250`](#insn-00bec250) → [`00bec280`](#insn-00bec280) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec270`](#insn-00bec270) → [`00bec22c`](#insn-00bec22c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec27c`](#insn-00bec27c) → [`00bec244`](#insn-00bec244) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec288`](#insn-00bec288) → [`00bec204`](#insn-00bec204) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec2a8`](#insn-00bec2a8) → [`00bec208`](#insn-00bec208) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec2c0`](#insn-00bec2c0) → [`00bec208`](#insn-00bec208) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec2d0`](#insn-00bec2d0) → [`00bec2ec`](#insn-00bec2ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec2e8`](#insn-00bec2e8) → [`00bec2c4`](#insn-00bec2c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec2f0`](#insn-00bec2f0) → [`00bec208`](#insn-00bec208) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bec000`](#insn-00bec000)

~~~json
{
  "source": "00bec000",
  "target": "00bec1fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec010`](#insn-00bec010)

~~~json
{
  "source": "00bec010",
  "target": "00bec0f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec01c`](#insn-00bec01c)

~~~json
{
  "source": "00bec01c",
  "target": "00bec030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec02c`](#insn-00bec02c)

~~~json
{
  "source": "00bec02c",
  "target": "00bec0f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec034`](#insn-00bec034)

~~~json
{
  "source": "00bec034",
  "target": "00bec024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec050`](#insn-00bec050)

~~~json
{
  "source": "00bec050",
  "target": "00bec074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec070`](#insn-00bec070)

~~~json
{
  "source": "00bec070",
  "target": "00bec078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec084`](#insn-00bec084)

~~~json
{
  "source": "00bec084",
  "target": "00bec0b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec088`](#insn-00bec088)

~~~json
{
  "source": "00bec088",
  "target": "00bec024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec0ac`](#insn-00bec0ac)

~~~json
{
  "source": "00bec0ac",
  "target": "00bec020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec0bc`](#insn-00bec0bc)

~~~json
{
  "source": "00bec0bc",
  "target": "00bec020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec0d8`](#insn-00bec0d8)

~~~json
{
  "source": "00bec0d8",
  "target": "00bec08c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec0e8`](#insn-00bec0e8)

~~~json
{
  "source": "00bec0e8",
  "target": "00bec0b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec0ec`](#insn-00bec0ec)

~~~json
{
  "source": "00bec0ec",
  "target": "00bec020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec0f8`](#insn-00bec0f8)

~~~json
{
  "source": "00bec0f8",
  "target": "00bec1f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec110`](#insn-00bec110)

~~~json
{
  "source": "00bec110",
  "target": "00bec124",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec120`](#insn-00bec120)

~~~json
{
  "source": "00bec120",
  "target": "00bec1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec130`](#insn-00bec130)

~~~json
{
  "source": "00bec130",
  "target": "00bec118",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec140`](#insn-00bec140)

~~~json
{
  "source": "00bec140",
  "target": "00bec118",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec14c`](#insn-00bec14c)

~~~json
{
  "source": "00bec14c",
  "target": "00bec164",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec15c`](#insn-00bec15c)

~~~json
{
  "source": "00bec15c",
  "target": "00bec118",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec160`](#insn-00bec160)

~~~json
{
  "source": "00bec160",
  "target": "00bec180",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec17c`](#insn-00bec17c)

~~~json
{
  "source": "00bec17c",
  "target": "00bec118",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec184`](#insn-00bec184)

~~~json
{
  "source": "00bec184",
  "target": "00bec1ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec1a8`](#insn-00bec1a8)

~~~json
{
  "source": "00bec1a8",
  "target": "00bec114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec1b8`](#insn-00bec1b8)

~~~json
{
  "source": "00bec1b8",
  "target": "00bec114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec1d4`](#insn-00bec1d4)

~~~json
{
  "source": "00bec1d4",
  "target": "00bec188",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec1e4`](#insn-00bec1e4)

~~~json
{
  "source": "00bec1e4",
  "target": "00bec1ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec1e8`](#insn-00bec1e8)

~~~json
{
  "source": "00bec1e8",
  "target": "00bec114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec1f4`](#insn-00bec1f4)

~~~json
{
  "source": "00bec1f4",
  "target": "00bec214",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec210`](#insn-00bec210)

~~~json
{
  "source": "00bec210",
  "target": "00bec1f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec228`](#insn-00bec228)

~~~json
{
  "source": "00bec228",
  "target": "00bec254",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec250`](#insn-00bec250)

~~~json
{
  "source": "00bec250",
  "target": "00bec280",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec270`](#insn-00bec270)

~~~json
{
  "source": "00bec270",
  "target": "00bec22c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec27c`](#insn-00bec27c)

~~~json
{
  "source": "00bec27c",
  "target": "00bec244",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec288`](#insn-00bec288)

~~~json
{
  "source": "00bec288",
  "target": "00bec204",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec2a8`](#insn-00bec2a8)

~~~json
{
  "source": "00bec2a8",
  "target": "00bec208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec2c0`](#insn-00bec2c0)

~~~json
{
  "source": "00bec2c0",
  "target": "00bec208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec2d0`](#insn-00bec2d0)

~~~json
{
  "source": "00bec2d0",
  "target": "00bec2ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec2e8`](#insn-00bec2e8)

~~~json
{
  "source": "00bec2e8",
  "target": "00bec2c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec2f0`](#insn-00bec2f0)

~~~json
{
  "source": "00bec2f0",
  "target": "00bec208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
