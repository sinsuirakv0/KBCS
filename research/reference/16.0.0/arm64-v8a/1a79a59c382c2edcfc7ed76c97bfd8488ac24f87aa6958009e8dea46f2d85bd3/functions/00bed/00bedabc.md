# 00bedabc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 対応未確定
  - [v15.7.4 → v16.0.0 版の比較一覧](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/README.md)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0003.md#review-b664e2b4c95a2009d5d75e4d7a641c44)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bedabc",
  "name": "FUN_00bedabc",
  "size": 764,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0ebec2708709255b30528effb365f8e1f8ee86d76e43ea35fd9c01d8b7fb00c5",
  "source_text_sha256": "0ebec2708709255b30528effb365f8e1f8ee86d76e43ea35fd9c01d8b7fb00c5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bedabc",
        "00beddb7"
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

- [00be6ce8](../00be6/00be6ce8.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 7468 bytes

~~~c

ulong * FUN_00bedabc(ulong *param_1,ulong *param_2,ulong *param_3)

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
                    /* try { // try from 00bedb14 to 00cedb1b has its CatchHandler @ 00bee324 */
          if ((long)uVar5 < lVar6) {
            uVar16 = *puVar10;
                    /* try { // try from 00bedb20 to 00cedb37 has its CatchHandler @ 00bee31c */
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
                    /* try { // try from 00bedb44 to 00cedb5f has its CatchHandler @ 00bee38c */
          puVar10 = param_1 + uVar13;
          if (uVar12 <= uVar14) {
            do {
              while( true ) {
                puVar7 = puVar11;
                *puVar10 = uVar14;
                if ((long)uVar8 < (long)uVar5) goto LAB_00bedae4;
                uVar3 = uVar5 << 1 | 1;
                uVar5 = uVar5 * 2 + 2;
                puVar4 = param_1 + uVar3;
                puVar10 = puVar7;
                if ((long)uVar5 < lVar6) break;
                uVar14 = *puVar4;
                puVar11 = puVar4;
                uVar5 = uVar3;
                if (uVar14 < uVar12) goto LAB_00bedae4;
              }
              uVar17 = *puVar4;
              uVar16 = puVar4[1];
                    /* try { // try from 00bedb60 to 00cedc17 has its CatchHandler @ 00bed9b8 */
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
LAB_00bedae4:
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
                    /* try { // try from 00bedc18 to 00cedc3b has its CatchHandler @ 00bee2dc */
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
                    /* try { // try from 00bedc3c to 00cedc8b has its CatchHandler @ 00bed9b8 */
            puVar4 = param_1;
            if (uVar13 <= uVar8) {
              do {
                while( true ) {
                  puVar15 = puVar10;
                  *puVar4 = uVar8;
                  if ((long)(lVar6 - 2U >> 1) < (long)uVar5) goto LAB_00bedbd8;
                  uVar12 = uVar5 << 1 | 1;
                    /* try { // try from 00bedc8c to 00cedcb3 has its CatchHandler @ 00bee2d4 */
                  uVar5 = uVar5 * 2 + 2;
                  puVar1 = param_1 + uVar12;
                  puVar4 = puVar15;
                  if ((long)uVar5 < lVar6) break;
                  uVar8 = *puVar1;
                  uVar5 = uVar12;
                  puVar10 = puVar1;
                  if (uVar8 < uVar13) goto LAB_00bedbd8;
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
LAB_00bedbd8:
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
                    /* try { // try from 00bedcec to 00cedd07 has its CatchHandler @ 00bee36c */
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
                    /* try { // try from 00bedd08 to 00ceddb3 has its CatchHandler @ 00bed9b8 */
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
                    /* try { // try from 00beddb4 to 00cede2f has its CatchHandler @ 00bee32c */
            }
          }
        }
                    /* try { // try from 00bedccc to 00cedce3 has its CatchHandler @ 00bee2c4 */
        bVar2 = 2 < lVar6;
        lVar6 = lVar6 + -1;
      } while (bVar2);
    }
  }
                    /* try { // try from 00bedcc0 to 00cedcc7 has its CatchHandler @ 00bee2cc */
  return param_3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bedabc"></a> `00bedabc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bedac0"></a> `00bedac0` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-00bedac4"></a> `00bedac4` | `e0 0f 00 54` | b.eq 0x00bedcc0 | `CONDITIONAL_JUMP`
<a id="insn-00bedac8"></a> `00bedac8` | `29 00 00 cb` | sub x9,x1,x0 | `FALL_THROUGH`
<a id="insn-00bedacc"></a> `00bedacc` | `28 fd 43 93` | asr x8,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00bedad0"></a> `00bedad0` | `0a 09 00 f1` | subs x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bedad4"></a> `00bedad4` | `0b 07 00 54` | b.lt 0x00bedbb4 | `CONDITIONAL_JUMP`
<a id="insn-00bedad8"></a> `00bedad8` | `4b fd 41 d3` | lsr x11,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bedadc"></a> `00bedadc` | `ec 03 0b aa` | mov x12,x11 | `FALL_THROUGH`
<a id="insn-00bedae0"></a> `00bedae0` | `05 00 00 14` | b 0x00bedaf4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedae4"></a> `00bedae4` | `0f 02 00 f9` | str x15,[x16] | `FALL_THROUGH`
<a id="insn-00bedae8"></a> `00bedae8` | `9f 01 00 f1` | cmp x12,#0x0 | `FALL_THROUGH`
<a id="insn-00bedaec"></a> `00bedaec` | `8c 05 00 d1` | sub x12,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00bedaf0"></a> `00bedaf0` | `2d 06 00 54` | b.le 0x00bedbb4 | `CONDITIONAL_JUMP`
<a id="insn-00bedaf4"></a> `00bedaf4` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-00bedaf8"></a> `00bedaf8` | `8b ff ff 54` | b.lt 0x00bedae8 | `CONDITIONAL_JUMP`
<a id="insn-00bedafc"></a> `00bedafc` | `2e 00 80 52` | mov w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bedb00"></a> `00bedb00` | `8d f1 7f d3` | ubfiz x13,x12,#0x1,#0x3d | `FALL_THROUGH`
<a id="insn-00bedb04"></a> `00bedb04` | `8e f1 7f b3` | bfm x14,x12,#0x3f,#0x3c | `FALL_THROUGH`
<a id="insn-00bedb08"></a> `00bedb08` | `af 09 00 91` | add x15,x13,#0x2 | `FALL_THROUGH`
<a id="insn-00bedb0c"></a> `00bedb0c` | `0d 0c 0e 8b` | add x13,x0,x14, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bedb10"></a> `00bedb10` | `ff 01 08 eb` | cmp x15,x8 | `FALL_THROUGH`
<a id="insn-00bedb14"></a> `00bedb14` | `2a 01 00 54` | b.ge 0x00bedb38 | `CONDITIONAL_JUMP`
<a id="insn-00bedb18"></a> `00bedb18` | `f0 03 0d aa` | mov x16,x13 | `FALL_THROUGH`
<a id="insn-00bedb1c"></a> `00bedb1c` | `b1 01 40 f9` | ldr x17,[x13] | `FALL_THROUGH`
<a id="insn-00bedb20"></a> `00bedb20` | `03 8e 40 f8` | ldr x3,[x16, #0x8]! | `FALL_THROUGH`
<a id="insn-00bedb24"></a> `00bedb24` | `3f 02 03 eb` | cmp x17,x3 | `FALL_THROUGH`
<a id="insn-00bedb28"></a> `00bedb28` | `31 82 83 9a` | csel x17,x17,x3,hi | `FALL_THROUGH`
<a id="insn-00bedb2c"></a> `00bedb2c` | `0d 32 8d 9a` | csel x13,x16,x13,cc | `FALL_THROUGH`
<a id="insn-00bedb30"></a> `00bedb30` | `ee 31 8e 9a` | csel x14,x15,x14,cc | `FALL_THROUGH`
<a id="insn-00bedb34"></a> `00bedb34` | `02 00 00 14` | b 0x00bedb3c | `UNCONDITIONAL_JUMP`
<a id="insn-00bedb38"></a> `00bedb38` | `b1 01 40 f9` | ldr x17,[x13] | `FALL_THROUGH`
<a id="insn-00bedb3c"></a> `00bedb3c` | `10 0c 0c 8b` | add x16,x0,x12, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bedb40"></a> `00bedb40` | `0f 02 40 f9` | ldr x15,[x16] | `FALL_THROUGH`
<a id="insn-00bedb44"></a> `00bedb44` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bedb48"></a> `00bedb48` | `62 01 00 54` | b.cs 0x00bedb74 | `CONDITIONAL_JUMP`
<a id="insn-00bedb4c"></a> `00bedb4c` | `e7 ff ff 17` | b 0x00bedae8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedb50"></a> `00bedb50` | `e4 03 0d aa` | mov x4,x13 | `FALL_THROUGH`
<a id="insn-00bedb54"></a> `00bedb54` | `b1 01 40 f9` | ldr x17,[x13] | `FALL_THROUGH`
<a id="insn-00bedb58"></a> `00bedb58` | `85 8c 40 f8` | ldr x5,[x4, #0x8]! | `FALL_THROUGH`
<a id="insn-00bedb5c"></a> `00bedb5c` | `3f 02 05 eb` | cmp x17,x5 | `FALL_THROUGH`
<a id="insn-00bedb60"></a> `00bedb60` | `31 82 85 9a` | csel x17,x17,x5,hi | `FALL_THROUGH`
<a id="insn-00bedb64"></a> `00bedb64` | `8d 30 8d 9a` | csel x13,x4,x13,cc | `FALL_THROUGH`
<a id="insn-00bedb68"></a> `00bedb68` | `ce 31 83 9a` | csel x14,x14,x3,cc | `FALL_THROUGH`
<a id="insn-00bedb6c"></a> `00bedb6c` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bedb70"></a> `00bedb70` | `a3 fb ff 54` | b.cc 0x00bedae4 | `CONDITIONAL_JUMP`
<a id="insn-00bedb74"></a> `00bedb74` | `7f 01 0e eb` | cmp x11,x14 | `FALL_THROUGH`
<a id="insn-00bedb78"></a> `00bedb78` | `11 02 00 f9` | str x17,[x16] | `FALL_THROUGH`
<a id="insn-00bedb7c"></a> `00bedb7c` | `f0 03 0d aa` | mov x16,x13 | `FALL_THROUGH`
<a id="insn-00bedb80"></a> `00bedb80` | `2b fb ff 54` | b.lt 0x00bedae4 | `CONDITIONAL_JUMP`
<a id="insn-00bedb84"></a> `00bedb84` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bedb88"></a> `00bedb88` | `cd f9 7f d3` | lsl x13,x14,#0x1 | `FALL_THROUGH`
<a id="insn-00bedb8c"></a> `00bedb8c` | `c3 f9 7f b3` | bfm x3,x14,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bedb90"></a> `00bedb90` | `ae 09 00 91` | add x14,x13,#0x2 | `FALL_THROUGH`
<a id="insn-00bedb94"></a> `00bedb94` | `0d 0c 03 8b` | add x13,x0,x3, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bedb98"></a> `00bedb98` | `df 01 08 eb` | cmp x14,x8 | `FALL_THROUGH`
<a id="insn-00bedb9c"></a> `00bedb9c` | `ab fd ff 54` | b.lt 0x00bedb50 | `CONDITIONAL_JUMP`
<a id="insn-00bedba0"></a> `00bedba0` | `b1 01 40 f9` | ldr x17,[x13] | `FALL_THROUGH`
<a id="insn-00bedba4"></a> `00bedba4` | `ee 03 03 aa` | mov x14,x3 | `FALL_THROUGH`
<a id="insn-00bedba8"></a> `00bedba8` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bedbac"></a> `00bedbac` | `42 fe ff 54` | b.cs 0x00bedb74 | `CONDITIONAL_JUMP`
<a id="insn-00bedbb0"></a> `00bedbb0` | `cd ff ff 17` | b 0x00bedae4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedbb4"></a> `00bedbb4` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-00bedbb8"></a> `00bedbb8` | `e3 03 01 aa` | mov x3,x1 | `FALL_THROUGH`
<a id="insn-00bedbbc"></a> `00bedbbc` | `c0 07 00 54` | b.eq 0x00bedcb4 | `CONDITIONAL_JUMP`
<a id="insn-00bedbc0"></a> `00bedbc0` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bedbc4"></a> `00bedbc4` | `0b 20 00 91` | add x11,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bedbc8"></a> `00bedbc8` | `0c 40 00 91` | add x12,x0,#0x10 | `FALL_THROUGH`
<a id="insn-00bedbcc"></a> `00bedbcc` | `2d 00 80 52` | mov w13,#0x1 | `FALL_THROUGH`
<a id="insn-00bedbd0"></a> `00bedbd0` | `ee 03 01 aa` | mov x14,x1 | `FALL_THROUGH`
<a id="insn-00bedbd4"></a> `00bedbd4` | `05 00 00 14` | b 0x00bedbe8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedbd8"></a> `00bedbd8` | `6f 00 00 f9` | str x15,[x3] | `FALL_THROUGH`
<a id="insn-00bedbdc"></a> `00bedbdc` | `ce 21 00 91` | add x14,x14,#0x8 | `FALL_THROUGH`
<a id="insn-00bedbe0"></a> `00bedbe0` | `df 01 02 eb` | cmp x14,x2 | `FALL_THROUGH`
<a id="insn-00bedbe4"></a> `00bedbe4` | `60 06 00 54` | b.eq 0x00bedcb0 | `CONDITIONAL_JUMP`
<a id="insn-00bedbe8"></a> `00bedbe8` | `cf 01 40 f9` | ldr x15,[x14] | `FALL_THROUGH`
<a id="insn-00bedbec"></a> `00bedbec` | `10 00 40 f9` | ldr x16,[x0] | `FALL_THROUGH`
<a id="insn-00bedbf0"></a> `00bedbf0` | `ff 01 10 eb` | cmp x15,x16 | `FALL_THROUGH`
<a id="insn-00bedbf4"></a> `00bedbf4` | `42 ff ff 54` | b.cs 0x00bedbdc | `CONDITIONAL_JUMP`
<a id="insn-00bedbf8"></a> `00bedbf8` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bedbfc"></a> `00bedbfc` | `d0 01 00 f9` | str x16,[x14] | `FALL_THROUGH`
<a id="insn-00bedc00"></a> `00bedc00` | `0f 00 00 f9` | str x15,[x0] | `FALL_THROUGH`
<a id="insn-00bedc04"></a> `00bedc04` | `cb fe ff 54` | b.lt 0x00bedbdc | `CONDITIONAL_JUMP`
<a id="insn-00bedc08"></a> `00bedc08` | `71 01 40 f9` | ldr x17,[x11] | `FALL_THROUGH`
<a id="insn-00bedc0c"></a> `00bedc0c` | `3f 41 00 f1` | cmp x9,#0x10 | `FALL_THROUGH`
<a id="insn-00bedc10"></a> `00bedc10` | `c1 00 00 54` | b.ne 0x00bedc28 | `CONDITIONAL_JUMP`
<a id="insn-00bedc14"></a> `00bedc14` | `f0 03 0b aa` | mov x16,x11 | `FALL_THROUGH`
<a id="insn-00bedc18"></a> `00bedc18` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-00bedc1c"></a> `00bedc1c` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bedc20"></a> `00bedc20` | `e3 fd ff 54` | b.cc 0x00bedbdc | `CONDITIONAL_JUMP`
<a id="insn-00bedc24"></a> `00bedc24` | `08 00 00 14` | b 0x00bedc44 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedc28"></a> `00bedc28` | `90 01 40 f9` | ldr x16,[x12] | `FALL_THROUGH`
<a id="insn-00bedc2c"></a> `00bedc2c` | `3f 02 10 eb` | cmp x17,x16 | `FALL_THROUGH`
<a id="insn-00bedc30"></a> `00bedc30` | `31 82 90 9a` | csel x17,x17,x16,hi | `FALL_THROUGH`
<a id="insn-00bedc34"></a> `00bedc34` | `90 31 8b 9a` | csel x16,x12,x11,cc | `FALL_THROUGH`
<a id="insn-00bedc38"></a> `00bedc38` | `a4 25 8d 9a` | cinc x4,x13,cc | `FALL_THROUGH`
<a id="insn-00bedc3c"></a> `00bedc3c` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bedc40"></a> `00bedc40` | `e3 fc ff 54` | b.cc 0x00bedbdc | `CONDITIONAL_JUMP`
<a id="insn-00bedc44"></a> `00bedc44` | `e3 03 00 aa` | mov x3,x0 | `FALL_THROUGH`
<a id="insn-00bedc48"></a> `00bedc48` | `0a 00 00 14` | b 0x00bedc70 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedc4c"></a> `00bedc4c` | `e6 03 10 aa` | mov x6,x16 | `FALL_THROUGH`
<a id="insn-00bedc50"></a> `00bedc50` | `11 02 40 f9` | ldr x17,[x16] | `FALL_THROUGH`
<a id="insn-00bedc54"></a> `00bedc54` | `c7 8c 40 f8` | ldr x7,[x6, #0x8]! | `FALL_THROUGH`
<a id="insn-00bedc58"></a> `00bedc58` | `3f 02 07 eb` | cmp x17,x7 | `FALL_THROUGH`
<a id="insn-00bedc5c"></a> `00bedc5c` | `31 82 87 9a` | csel x17,x17,x7,hi | `FALL_THROUGH`
<a id="insn-00bedc60"></a> `00bedc60` | `d0 30 90 9a` | csel x16,x6,x16,cc | `FALL_THROUGH`
<a id="insn-00bedc64"></a> `00bedc64` | `84 30 85 9a` | csel x4,x4,x5,cc | `FALL_THROUGH`
<a id="insn-00bedc68"></a> `00bedc68` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bedc6c"></a> `00bedc6c` | `63 fb ff 54` | b.cc 0x00bedbd8 | `CONDITIONAL_JUMP`
<a id="insn-00bedc70"></a> `00bedc70` | `5f 01 04 eb` | cmp x10,x4 | `FALL_THROUGH`
<a id="insn-00bedc74"></a> `00bedc74` | `71 00 00 f9` | str x17,[x3] | `FALL_THROUGH`
<a id="insn-00bedc78"></a> `00bedc78` | `e3 03 10 aa` | mov x3,x16 | `FALL_THROUGH`
<a id="insn-00bedc7c"></a> `00bedc7c` | `eb fa ff 54` | b.lt 0x00bedbd8 | `CONDITIONAL_JUMP`
<a id="insn-00bedc80"></a> `00bedc80` | `25 00 80 52` | mov w5,#0x1 | `FALL_THROUGH`
<a id="insn-00bedc84"></a> `00bedc84` | `90 f8 7f d3` | lsl x16,x4,#0x1 | `FALL_THROUGH`
<a id="insn-00bedc88"></a> `00bedc88` | `85 f8 7f b3` | bfm x5,x4,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bedc8c"></a> `00bedc8c` | `04 0a 00 91` | add x4,x16,#0x2 | `FALL_THROUGH`
<a id="insn-00bedc90"></a> `00bedc90` | `10 0c 05 8b` | add x16,x0,x5, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bedc94"></a> `00bedc94` | `9f 00 08 eb` | cmp x4,x8 | `FALL_THROUGH`
<a id="insn-00bedc98"></a> `00bedc98` | `ab fd ff 54` | b.lt 0x00bedc4c | `CONDITIONAL_JUMP`
<a id="insn-00bedc9c"></a> `00bedc9c` | `11 02 40 f9` | ldr x17,[x16] | `FALL_THROUGH`
<a id="insn-00bedca0"></a> `00bedca0` | `e4 03 05 aa` | mov x4,x5 | `FALL_THROUGH`
<a id="insn-00bedca4"></a> `00bedca4` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bedca8"></a> `00bedca8` | `42 fe ff 54` | b.cs 0x00bedc70 | `CONDITIONAL_JUMP`
<a id="insn-00bedcac"></a> `00bedcac` | `cb ff ff 17` | b 0x00bedbd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedcb0"></a> `00bedcb0` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bedcb4"></a> `00bedcb4` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bedcb8"></a> `00bedcb8` | `0a 01 00 54` | b.ge 0x00bedcd8 | `CONDITIONAL_JUMP`
<a id="insn-00bedcbc"></a> `00bedcbc` | `e2 03 03 aa` | mov x2,x3 | `FALL_THROUGH`
<a id="insn-00bedcc0"></a> `00bedcc0` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bedcc4"></a> `00bedcc4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bedcc8"></a> `00bedcc8` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bedccc"></a> `00bedccc` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bedcd0"></a> `00bedcd0` | `08 05 00 d1` | sub x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bedcd4"></a> `00bedcd4` | `4d ff ff 54` | b.le 0x00bedcbc | `CONDITIONAL_JUMP`
<a id="insn-00bedcd8"></a> `00bedcd8` | `09 09 00 d1` | sub x9,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bedcdc"></a> `00bedcdc` | `0a 00 40 f9` | ldr x10,[x0] | `FALL_THROUGH`
<a id="insn-00bedce0"></a> `00bedce0` | `ed 03 1f aa` | mov x13,xzr | `FALL_THROUGH`
<a id="insn-00bedce4"></a> `00bedce4` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bedce8"></a> `00bedce8` | `ec 03 00 aa` | mov x12,x0 | `FALL_THROUGH`
<a id="insn-00bedcec"></a> `00bedcec` | `0b 00 00 14` | b 0x00bedd18 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedcf0"></a> `00bedcf0` | `0d 0e 41 f8` | ldr x13,[x16, #0x10]! | `FALL_THROUGH`
<a id="insn-00bedcf4"></a> `00bedcf4` | `0f 82 5f f8` | ldur x15,[x16, #-0x8] | `FALL_THROUGH`
<a id="insn-00bedcf8"></a> `00bedcf8` | `ff 01 0d eb` | cmp x15,x13 | `FALL_THROUGH`
<a id="insn-00bedcfc"></a> `00bedcfc` | `ef 81 8d 9a` | csel x15,x15,x13,hi | `FALL_THROUGH`
<a id="insn-00bedd00"></a> `00bedd00` | `09 32 89 9a` | csel x9,x16,x9,cc | `FALL_THROUGH`
<a id="insn-00bedd04"></a> `00bedd04` | `2d 32 8e 9a` | csel x13,x17,x14,cc | `FALL_THROUGH`
<a id="insn-00bedd08"></a> `00bedd08` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00bedd0c"></a> `00bedd0c` | `8f 01 00 f9` | str x15,[x12] | `FALL_THROUGH`
<a id="insn-00bedd10"></a> `00bedd10` | `ec 03 09 aa` | mov x12,x9 | `FALL_THROUGH`
<a id="insn-00bedd14"></a> `00bedd14` | `8c 01 00 54` | b.gt 0x00bedd44 | `CONDITIONAL_JUMP`
<a id="insn-00bedd18"></a> `00bedd18` | `a9 f9 7f d3` | lsl x9,x13,#0x1 | `FALL_THROUGH`
<a id="insn-00bedd1c"></a> `00bedd1c` | `90 0d 0d 8b` | add x16,x12,x13, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bedd20"></a> `00bedd20` | `2e 00 80 52` | mov w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bedd24"></a> `00bedd24` | `ae f9 7f b3` | bfm x14,x13,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bedd28"></a> `00bedd28` | `31 09 00 91` | add x17,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bedd2c"></a> `00bedd2c` | `09 22 00 91` | add x9,x16,#0x8 | `FALL_THROUGH`
<a id="insn-00bedd30"></a> `00bedd30` | `3f 02 08 eb` | cmp x17,x8 | `FALL_THROUGH`
<a id="insn-00bedd34"></a> `00bedd34` | `eb fd ff 54` | b.lt 0x00bedcf0 | `CONDITIONAL_JUMP`
<a id="insn-00bedd38"></a> `00bedd38` | `2f 01 40 f9` | ldr x15,[x9] | `FALL_THROUGH`
<a id="insn-00bedd3c"></a> `00bedd3c` | `ed 03 0e aa` | mov x13,x14 | `FALL_THROUGH`
<a id="insn-00bedd40"></a> `00bedd40` | `f2 ff ff 17` | b 0x00bedd08 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedd44"></a> `00bedd44` | `21 20 00 d1` | sub x1,x1,#0x8 | `FALL_THROUGH`
<a id="insn-00bedd48"></a> `00bedd48` | `3f 01 01 eb` | cmp x9,x1 | `FALL_THROUGH`
<a id="insn-00bedd4c"></a> `00bedd4c` | `e0 fb ff 54` | b.eq 0x00bedcc8 | `CONDITIONAL_JUMP`
<a id="insn-00bedd50"></a> `00bedd50` | `2b 01 00 cb` | sub x11,x9,x0 | `FALL_THROUGH`
<a id="insn-00bedd54"></a> `00bedd54` | `2c 00 40 f9` | ldr x12,[x1] | `FALL_THROUGH`
<a id="insn-00bedd58"></a> `00bedd58` | `6b 21 00 91` | add x11,x11,#0x8 | `FALL_THROUGH`
<a id="insn-00bedd5c"></a> `00bedd5c` | `6b fd 43 93` | asr x11,x11,#0x3 | `FALL_THROUGH`
<a id="insn-00bedd60"></a> `00bedd60` | `2c 01 00 f9` | str x12,[x9] | `FALL_THROUGH`
<a id="insn-00bedd64"></a> `00bedd64` | `2a 00 00 f9` | str x10,[x1] | `FALL_THROUGH`
<a id="insn-00bedd68"></a> `00bedd68` | `6b 09 00 f1` | subs x11,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00bedd6c"></a> `00bedd6c` | `0b fb ff 54` | b.lt 0x00bedccc | `CONDITIONAL_JUMP`
<a id="insn-00bedd70"></a> `00bedd70` | `6a fd 41 d3` | lsr x10,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00bedd74"></a> `00bedd74` | `2b 01 40 f9` | ldr x11,[x9] | `FALL_THROUGH`
<a id="insn-00bedd78"></a> `00bedd78` | `0c 0c 0a 8b` | add x12,x0,x10, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bedd7c"></a> `00bedd7c` | `8d 01 40 f9` | ldr x13,[x12] | `FALL_THROUGH`
<a id="insn-00bedd80"></a> `00bedd80` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00bedd84"></a> `00bedd84` | `42 fa ff 54` | b.cs 0x00bedccc | `CONDITIONAL_JUMP`
<a id="insn-00bedd88"></a> `00bedd88` | `ee 03 09 aa` | mov x14,x9 | `FALL_THROUGH`
<a id="insn-00bedd8c"></a> `00bedd8c` | `e9 03 0c aa` | mov x9,x12 | `FALL_THROUGH`
<a id="insn-00bedd90"></a> `00bedd90` | `cd 01 00 f9` | str x13,[x14] | `FALL_THROUGH`
<a id="insn-00bedd94"></a> `00bedd94` | `ea 00 00 b4` | cbz x10,0x00beddb0 | `CONDITIONAL_JUMP`
<a id="insn-00bedd98"></a> `00bedd98` | `4a 05 00 d1` | sub x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bedd9c"></a> `00bedd9c` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bedda0"></a> `00bedda0` | `0c 0c 0a 8b` | add x12,x0,x10, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bedda4"></a> `00bedda4` | `8d 01 40 f9` | ldr x13,[x12] | `FALL_THROUGH`
<a id="insn-00bedda8"></a> `00bedda8` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00beddac"></a> `00beddac` | `e3 fe ff 54` | b.cc 0x00bedd88 | `CONDITIONAL_JUMP`
<a id="insn-00beddb0"></a> `00beddb0` | `2b 01 00 f9` | str x11,[x9] | `FALL_THROUGH`
<a id="insn-00beddb4"></a> `00beddb4` | `c6 ff ff 17` | b 0x00bedccc | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bedabc`](#insn-00bedabc) 範囲 `[['00bedabc', '00bedac7']]`
  - `CONDITIONAL_JUMP` [`00bedac4`](#insn-00bedac4) → [`00bedcc0`](#insn-00bedcc0)
  - `FALL_THROUGH` [`00bedac4`](#insn-00bedac4) → [`00bedac8`](#insn-00bedac8)
- ブロック [`00bedac8`](#insn-00bedac8) 範囲 `[['00bedac8', '00bedad7']]`
  - `CONDITIONAL_JUMP` [`00bedad4`](#insn-00bedad4) → [`00bedbb4`](#insn-00bedbb4)
  - `FALL_THROUGH` [`00bedad4`](#insn-00bedad4) → [`00bedad8`](#insn-00bedad8)
- ブロック [`00bedad8`](#insn-00bedad8) 範囲 `[['00bedad8', '00bedae3']]`
  - `UNCONDITIONAL_JUMP` [`00bedae0`](#insn-00bedae0) → [`00bedaf4`](#insn-00bedaf4)
- ブロック [`00bedae4`](#insn-00bedae4) 範囲 `[['00bedae4', '00bedae7']]`
  - `FALL_THROUGH` [`00bedae4`](#insn-00bedae4) → [`00bedae8`](#insn-00bedae8)
- ブロック [`00bedae8`](#insn-00bedae8) 範囲 `[['00bedae8', '00bedaf3']]`
  - `CONDITIONAL_JUMP` [`00bedaf0`](#insn-00bedaf0) → [`00bedbb4`](#insn-00bedbb4)
  - `FALL_THROUGH` [`00bedaf0`](#insn-00bedaf0) → [`00bedaf4`](#insn-00bedaf4)
- ブロック [`00bedaf4`](#insn-00bedaf4) 範囲 `[['00bedaf4', '00bedafb']]`
  - `CONDITIONAL_JUMP` [`00bedaf8`](#insn-00bedaf8) → [`00bedae8`](#insn-00bedae8)
  - `FALL_THROUGH` [`00bedaf8`](#insn-00bedaf8) → [`00bedafc`](#insn-00bedafc)
- ブロック [`00bedafc`](#insn-00bedafc) 範囲 `[['00bedafc', '00bedb13']]`
  - `FALL_THROUGH` [`00bedb10`](#insn-00bedb10) → [`00bedb14`](#insn-00bedb14)
- ブロック [`00bedb14`](#insn-00bedb14) 範囲 `[['00bedb14', '00bedb17']]`
  - `CONDITIONAL_JUMP` [`00bedb14`](#insn-00bedb14) → [`00bedb38`](#insn-00bedb38)
  - `FALL_THROUGH` [`00bedb14`](#insn-00bedb14) → [`00bedb18`](#insn-00bedb18)
- ブロック [`00bedb18`](#insn-00bedb18) 範囲 `[['00bedb18', '00bedb1f']]`
  - `FALL_THROUGH` [`00bedb1c`](#insn-00bedb1c) → [`00bedb20`](#insn-00bedb20)
- ブロック [`00bedb20`](#insn-00bedb20) 範囲 `[['00bedb20', '00bedb37']]`
  - `UNCONDITIONAL_JUMP` [`00bedb34`](#insn-00bedb34) → [`00bedb3c`](#insn-00bedb3c)
- ブロック [`00bedb38`](#insn-00bedb38) 範囲 `[['00bedb38', '00bedb3b']]`
  - `FALL_THROUGH` [`00bedb38`](#insn-00bedb38) → [`00bedb3c`](#insn-00bedb3c)
- ブロック [`00bedb3c`](#insn-00bedb3c) 範囲 `[['00bedb3c', '00bedb43']]`
  - `FALL_THROUGH` [`00bedb40`](#insn-00bedb40) → [`00bedb44`](#insn-00bedb44)
- ブロック [`00bedb44`](#insn-00bedb44) 範囲 `[['00bedb44', '00bedb4b']]`
  - `CONDITIONAL_JUMP` [`00bedb48`](#insn-00bedb48) → [`00bedb74`](#insn-00bedb74)
  - `FALL_THROUGH` [`00bedb48`](#insn-00bedb48) → [`00bedb4c`](#insn-00bedb4c)
- ブロック [`00bedb4c`](#insn-00bedb4c) 範囲 `[['00bedb4c', '00bedb4f']]`
  - `UNCONDITIONAL_JUMP` [`00bedb4c`](#insn-00bedb4c) → [`00bedae8`](#insn-00bedae8)
- ブロック [`00bedb50`](#insn-00bedb50) 範囲 `[['00bedb50', '00bedb5f']]`
  - `FALL_THROUGH` [`00bedb5c`](#insn-00bedb5c) → [`00bedb60`](#insn-00bedb60)
- ブロック [`00bedb60`](#insn-00bedb60) 範囲 `[['00bedb60', '00bedb73']]`
  - `CONDITIONAL_JUMP` [`00bedb70`](#insn-00bedb70) → [`00bedae4`](#insn-00bedae4)
  - `FALL_THROUGH` [`00bedb70`](#insn-00bedb70) → [`00bedb74`](#insn-00bedb74)
- ブロック [`00bedb74`](#insn-00bedb74) 範囲 `[['00bedb74', '00bedb83']]`
  - `CONDITIONAL_JUMP` [`00bedb80`](#insn-00bedb80) → [`00bedae4`](#insn-00bedae4)
  - `FALL_THROUGH` [`00bedb80`](#insn-00bedb80) → [`00bedb84`](#insn-00bedb84)
- ブロック [`00bedb84`](#insn-00bedb84) 範囲 `[['00bedb84', '00bedb9f']]`
  - `CONDITIONAL_JUMP` [`00bedb9c`](#insn-00bedb9c) → [`00bedb50`](#insn-00bedb50)
  - `FALL_THROUGH` [`00bedb9c`](#insn-00bedb9c) → [`00bedba0`](#insn-00bedba0)
- ブロック [`00bedba0`](#insn-00bedba0) 範囲 `[['00bedba0', '00bedbaf']]`
  - `CONDITIONAL_JUMP` [`00bedbac`](#insn-00bedbac) → [`00bedb74`](#insn-00bedb74)
  - `FALL_THROUGH` [`00bedbac`](#insn-00bedbac) → [`00bedbb0`](#insn-00bedbb0)
- ブロック [`00bedbb0`](#insn-00bedbb0) 範囲 `[['00bedbb0', '00bedbb3']]`
  - `UNCONDITIONAL_JUMP` [`00bedbb0`](#insn-00bedbb0) → [`00bedae4`](#insn-00bedae4)
- ブロック [`00bedbb4`](#insn-00bedbb4) 範囲 `[['00bedbb4', '00bedbbf']]`
  - `CONDITIONAL_JUMP` [`00bedbbc`](#insn-00bedbbc) → [`00bedcb4`](#insn-00bedcb4)
  - `FALL_THROUGH` [`00bedbbc`](#insn-00bedbbc) → [`00bedbc0`](#insn-00bedbc0)
- ブロック [`00bedbc0`](#insn-00bedbc0) 範囲 `[['00bedbc0', '00bedbd7']]`
  - `UNCONDITIONAL_JUMP` [`00bedbd4`](#insn-00bedbd4) → [`00bedbe8`](#insn-00bedbe8)
- ブロック [`00bedbd8`](#insn-00bedbd8) 範囲 `[['00bedbd8', '00bedbdb']]`
  - `FALL_THROUGH` [`00bedbd8`](#insn-00bedbd8) → [`00bedbdc`](#insn-00bedbdc)
- ブロック [`00bedbdc`](#insn-00bedbdc) 範囲 `[['00bedbdc', '00bedbe7']]`
  - `CONDITIONAL_JUMP` [`00bedbe4`](#insn-00bedbe4) → [`00bedcb0`](#insn-00bedcb0)
  - `FALL_THROUGH` [`00bedbe4`](#insn-00bedbe4) → [`00bedbe8`](#insn-00bedbe8)
- ブロック [`00bedbe8`](#insn-00bedbe8) 範囲 `[['00bedbe8', '00bedbf7']]`
  - `CONDITIONAL_JUMP` [`00bedbf4`](#insn-00bedbf4) → [`00bedbdc`](#insn-00bedbdc)
  - `FALL_THROUGH` [`00bedbf4`](#insn-00bedbf4) → [`00bedbf8`](#insn-00bedbf8)
- ブロック [`00bedbf8`](#insn-00bedbf8) 範囲 `[['00bedbf8', '00bedc07']]`
  - `CONDITIONAL_JUMP` [`00bedc04`](#insn-00bedc04) → [`00bedbdc`](#insn-00bedbdc)
  - `FALL_THROUGH` [`00bedc04`](#insn-00bedc04) → [`00bedc08`](#insn-00bedc08)
- ブロック [`00bedc08`](#insn-00bedc08) 範囲 `[['00bedc08', '00bedc13']]`
  - `CONDITIONAL_JUMP` [`00bedc10`](#insn-00bedc10) → [`00bedc28`](#insn-00bedc28)
  - `FALL_THROUGH` [`00bedc10`](#insn-00bedc10) → [`00bedc14`](#insn-00bedc14)
- ブロック [`00bedc14`](#insn-00bedc14) 範囲 `[['00bedc14', '00bedc17']]`
  - `FALL_THROUGH` [`00bedc14`](#insn-00bedc14) → [`00bedc18`](#insn-00bedc18)
- ブロック [`00bedc18`](#insn-00bedc18) 範囲 `[['00bedc18', '00bedc23']]`
  - `CONDITIONAL_JUMP` [`00bedc20`](#insn-00bedc20) → [`00bedbdc`](#insn-00bedbdc)
  - `FALL_THROUGH` [`00bedc20`](#insn-00bedc20) → [`00bedc24`](#insn-00bedc24)
- ブロック [`00bedc24`](#insn-00bedc24) 範囲 `[['00bedc24', '00bedc27']]`
  - `UNCONDITIONAL_JUMP` [`00bedc24`](#insn-00bedc24) → [`00bedc44`](#insn-00bedc44)
- ブロック [`00bedc28`](#insn-00bedc28) 範囲 `[['00bedc28', '00bedc3b']]`
  - `FALL_THROUGH` [`00bedc38`](#insn-00bedc38) → [`00bedc3c`](#insn-00bedc3c)
- ブロック [`00bedc3c`](#insn-00bedc3c) 範囲 `[['00bedc3c', '00bedc43']]`
  - `CONDITIONAL_JUMP` [`00bedc40`](#insn-00bedc40) → [`00bedbdc`](#insn-00bedbdc)
  - `FALL_THROUGH` [`00bedc40`](#insn-00bedc40) → [`00bedc44`](#insn-00bedc44)
- ブロック [`00bedc44`](#insn-00bedc44) 範囲 `[['00bedc44', '00bedc4b']]`
  - `UNCONDITIONAL_JUMP` [`00bedc48`](#insn-00bedc48) → [`00bedc70`](#insn-00bedc70)
- ブロック [`00bedc4c`](#insn-00bedc4c) 範囲 `[['00bedc4c', '00bedc6f']]`
  - `CONDITIONAL_JUMP` [`00bedc6c`](#insn-00bedc6c) → [`00bedbd8`](#insn-00bedbd8)
  - `FALL_THROUGH` [`00bedc6c`](#insn-00bedc6c) → [`00bedc70`](#insn-00bedc70)
- ブロック [`00bedc70`](#insn-00bedc70) 範囲 `[['00bedc70', '00bedc7f']]`
  - `CONDITIONAL_JUMP` [`00bedc7c`](#insn-00bedc7c) → [`00bedbd8`](#insn-00bedbd8)
  - `FALL_THROUGH` [`00bedc7c`](#insn-00bedc7c) → [`00bedc80`](#insn-00bedc80)
- ブロック [`00bedc80`](#insn-00bedc80) 範囲 `[['00bedc80', '00bedc8b']]`
  - `FALL_THROUGH` [`00bedc88`](#insn-00bedc88) → [`00bedc8c`](#insn-00bedc8c)
- ブロック [`00bedc8c`](#insn-00bedc8c) 範囲 `[['00bedc8c', '00bedc9b']]`
  - `CONDITIONAL_JUMP` [`00bedc98`](#insn-00bedc98) → [`00bedc4c`](#insn-00bedc4c)
  - `FALL_THROUGH` [`00bedc98`](#insn-00bedc98) → [`00bedc9c`](#insn-00bedc9c)
- ブロック [`00bedc9c`](#insn-00bedc9c) 範囲 `[['00bedc9c', '00bedcab']]`
  - `CONDITIONAL_JUMP` [`00bedca8`](#insn-00bedca8) → [`00bedc70`](#insn-00bedc70)
  - `FALL_THROUGH` [`00bedca8`](#insn-00bedca8) → [`00bedcac`](#insn-00bedcac)
- ブロック [`00bedcac`](#insn-00bedcac) 範囲 `[['00bedcac', '00bedcaf']]`
  - `UNCONDITIONAL_JUMP` [`00bedcac`](#insn-00bedcac) → [`00bedbd8`](#insn-00bedbd8)
- ブロック [`00bedcb0`](#insn-00bedcb0) 範囲 `[['00bedcb0', '00bedcb3']]`
  - `FALL_THROUGH` [`00bedcb0`](#insn-00bedcb0) → [`00bedcb4`](#insn-00bedcb4)
- ブロック [`00bedcb4`](#insn-00bedcb4) 範囲 `[['00bedcb4', '00bedcbb']]`
  - `CONDITIONAL_JUMP` [`00bedcb8`](#insn-00bedcb8) → [`00bedcd8`](#insn-00bedcd8)
  - `FALL_THROUGH` [`00bedcb8`](#insn-00bedcb8) → [`00bedcbc`](#insn-00bedcbc)
- ブロック [`00bedcbc`](#insn-00bedcbc) 範囲 `[['00bedcbc', '00bedcbf']]`
  - `FALL_THROUGH` [`00bedcbc`](#insn-00bedcbc) → [`00bedcc0`](#insn-00bedcc0)
- ブロック [`00bedcc0`](#insn-00bedcc0) 範囲 `[['00bedcc0', '00bedcc7']]`
- ブロック [`00bedcc8`](#insn-00bedcc8) 範囲 `[['00bedcc8', '00bedccb']]`
  - `FALL_THROUGH` [`00bedcc8`](#insn-00bedcc8) → [`00bedccc`](#insn-00bedccc)
- ブロック [`00bedccc`](#insn-00bedccc) 範囲 `[['00bedccc', '00bedcd7']]`
  - `CONDITIONAL_JUMP` [`00bedcd4`](#insn-00bedcd4) → [`00bedcbc`](#insn-00bedcbc)
  - `FALL_THROUGH` [`00bedcd4`](#insn-00bedcd4) → [`00bedcd8`](#insn-00bedcd8)
- ブロック [`00bedcd8`](#insn-00bedcd8) 範囲 `[['00bedcd8', '00bedceb']]`
  - `FALL_THROUGH` [`00bedce8`](#insn-00bedce8) → [`00bedcec`](#insn-00bedcec)
- ブロック [`00bedcec`](#insn-00bedcec) 範囲 `[['00bedcec', '00bedcef']]`
  - `UNCONDITIONAL_JUMP` [`00bedcec`](#insn-00bedcec) → [`00bedd18`](#insn-00bedd18)
- ブロック [`00bedcf0`](#insn-00bedcf0) 範囲 `[['00bedcf0', '00bedd07']]`
  - `FALL_THROUGH` [`00bedd04`](#insn-00bedd04) → [`00bedd08`](#insn-00bedd08)
- ブロック [`00bedd08`](#insn-00bedd08) 範囲 `[['00bedd08', '00bedd17']]`
  - `CONDITIONAL_JUMP` [`00bedd14`](#insn-00bedd14) → [`00bedd44`](#insn-00bedd44)
  - `FALL_THROUGH` [`00bedd14`](#insn-00bedd14) → [`00bedd18`](#insn-00bedd18)
- ブロック [`00bedd18`](#insn-00bedd18) 範囲 `[['00bedd18', '00bedd37']]`
  - `CONDITIONAL_JUMP` [`00bedd34`](#insn-00bedd34) → [`00bedcf0`](#insn-00bedcf0)
  - `FALL_THROUGH` [`00bedd34`](#insn-00bedd34) → [`00bedd38`](#insn-00bedd38)
- ブロック [`00bedd38`](#insn-00bedd38) 範囲 `[['00bedd38', '00bedd43']]`
  - `UNCONDITIONAL_JUMP` [`00bedd40`](#insn-00bedd40) → [`00bedd08`](#insn-00bedd08)
- ブロック [`00bedd44`](#insn-00bedd44) 範囲 `[['00bedd44', '00bedd4f']]`
  - `CONDITIONAL_JUMP` [`00bedd4c`](#insn-00bedd4c) → [`00bedcc8`](#insn-00bedcc8)
  - `FALL_THROUGH` [`00bedd4c`](#insn-00bedd4c) → [`00bedd50`](#insn-00bedd50)
- ブロック [`00bedd50`](#insn-00bedd50) 範囲 `[['00bedd50', '00bedd6f']]`
  - `CONDITIONAL_JUMP` [`00bedd6c`](#insn-00bedd6c) → [`00bedccc`](#insn-00bedccc)
  - `FALL_THROUGH` [`00bedd6c`](#insn-00bedd6c) → [`00bedd70`](#insn-00bedd70)
- ブロック [`00bedd70`](#insn-00bedd70) 範囲 `[['00bedd70', '00bedd87']]`
  - `CONDITIONAL_JUMP` [`00bedd84`](#insn-00bedd84) → [`00bedccc`](#insn-00bedccc)
  - `FALL_THROUGH` [`00bedd84`](#insn-00bedd84) → [`00bedd88`](#insn-00bedd88)
- ブロック [`00bedd88`](#insn-00bedd88) 範囲 `[['00bedd88', '00bedd97']]`
  - `CONDITIONAL_JUMP` [`00bedd94`](#insn-00bedd94) → [`00beddb0`](#insn-00beddb0)
  - `FALL_THROUGH` [`00bedd94`](#insn-00bedd94) → [`00bedd98`](#insn-00bedd98)
- ブロック [`00bedd98`](#insn-00bedd98) 範囲 `[['00bedd98', '00beddaf']]`
  - `CONDITIONAL_JUMP` [`00beddac`](#insn-00beddac) → [`00bedd88`](#insn-00bedd88)
  - `FALL_THROUGH` [`00beddac`](#insn-00beddac) → [`00beddb0`](#insn-00beddb0)
- ブロック [`00beddb0`](#insn-00beddb0) 範囲 `[['00beddb0', '00beddb3']]`
  - `FALL_THROUGH` [`00beddb0`](#insn-00beddb0) → [`00beddb4`](#insn-00beddb4)
- ブロック [`00beddb4`](#insn-00beddb4) 範囲 `[['00beddb4', '00beddb7']]`
  - `UNCONDITIONAL_JUMP` [`00beddb4`](#insn-00beddb4) → [`00bedccc`](#insn-00bedccc)

## 命令位置別の参照

- [`00bedac4`](#insn-00bedac4) → [`00bedcc0`](#insn-00bedcc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedad4`](#insn-00bedad4) → [`00bedbb4`](#insn-00bedbb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedae0`](#insn-00bedae0) → [`00bedaf4`](#insn-00bedaf4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedaf0`](#insn-00bedaf0) → [`00bedbb4`](#insn-00bedbb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedaf8`](#insn-00bedaf8) → [`00bedae8`](#insn-00bedae8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedb14`](#insn-00bedb14) → [`00bedb38`](#insn-00bedb38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedb34`](#insn-00bedb34) → [`00bedb3c`](#insn-00bedb3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedb48`](#insn-00bedb48) → [`00bedb74`](#insn-00bedb74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedb4c`](#insn-00bedb4c) → [`00bedae8`](#insn-00bedae8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedb70`](#insn-00bedb70) → [`00bedae4`](#insn-00bedae4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedb80`](#insn-00bedb80) → [`00bedae4`](#insn-00bedae4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedb9c`](#insn-00bedb9c) → [`00bedb50`](#insn-00bedb50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedbac`](#insn-00bedbac) → [`00bedb74`](#insn-00bedb74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedbb0`](#insn-00bedbb0) → [`00bedae4`](#insn-00bedae4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedbbc`](#insn-00bedbbc) → [`00bedcb4`](#insn-00bedcb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedbd4`](#insn-00bedbd4) → [`00bedbe8`](#insn-00bedbe8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedbe4`](#insn-00bedbe4) → [`00bedcb0`](#insn-00bedcb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedbf4`](#insn-00bedbf4) → [`00bedbdc`](#insn-00bedbdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc04`](#insn-00bedc04) → [`00bedbdc`](#insn-00bedbdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc10`](#insn-00bedc10) → [`00bedc28`](#insn-00bedc28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc20`](#insn-00bedc20) → [`00bedbdc`](#insn-00bedbdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc24`](#insn-00bedc24) → [`00bedc44`](#insn-00bedc44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc40`](#insn-00bedc40) → [`00bedbdc`](#insn-00bedbdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc48`](#insn-00bedc48) → [`00bedc70`](#insn-00bedc70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc6c`](#insn-00bedc6c) → [`00bedbd8`](#insn-00bedbd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc7c`](#insn-00bedc7c) → [`00bedbd8`](#insn-00bedbd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc98`](#insn-00bedc98) → [`00bedc4c`](#insn-00bedc4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedca8`](#insn-00bedca8) → [`00bedc70`](#insn-00bedc70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedcac`](#insn-00bedcac) → [`00bedbd8`](#insn-00bedbd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedcb8`](#insn-00bedcb8) → [`00bedcd8`](#insn-00bedcd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedcd4`](#insn-00bedcd4) → [`00bedcbc`](#insn-00bedcbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedcec`](#insn-00bedcec) → [`00bedd18`](#insn-00bedd18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd14`](#insn-00bedd14) → [`00bedd44`](#insn-00bedd44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd34`](#insn-00bedd34) → [`00bedcf0`](#insn-00bedcf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd40`](#insn-00bedd40) → [`00bedd08`](#insn-00bedd08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd4c`](#insn-00bedd4c) → [`00bedcc8`](#insn-00bedcc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd6c`](#insn-00bedd6c) → [`00bedccc`](#insn-00bedccc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd84`](#insn-00bedd84) → [`00bedccc`](#insn-00bedccc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd94`](#insn-00bedd94) → [`00beddb0`](#insn-00beddb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beddac`](#insn-00beddac) → [`00bedd88`](#insn-00bedd88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beddb4`](#insn-00beddb4) → [`00bedccc`](#insn-00bedccc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bedac4`](#insn-00bedac4)

~~~json
{
  "source": "00bedac4",
  "target": "00bedcc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedad4`](#insn-00bedad4)

~~~json
{
  "source": "00bedad4",
  "target": "00bedbb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedae0`](#insn-00bedae0)

~~~json
{
  "source": "00bedae0",
  "target": "00bedaf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedaf0`](#insn-00bedaf0)

~~~json
{
  "source": "00bedaf0",
  "target": "00bedbb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedaf8`](#insn-00bedaf8)

~~~json
{
  "source": "00bedaf8",
  "target": "00bedae8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedb14`](#insn-00bedb14)

~~~json
{
  "source": "00bedb14",
  "target": "00bedb38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedb34`](#insn-00bedb34)

~~~json
{
  "source": "00bedb34",
  "target": "00bedb3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedb48`](#insn-00bedb48)

~~~json
{
  "source": "00bedb48",
  "target": "00bedb74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedb4c`](#insn-00bedb4c)

~~~json
{
  "source": "00bedb4c",
  "target": "00bedae8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedb70`](#insn-00bedb70)

~~~json
{
  "source": "00bedb70",
  "target": "00bedae4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedb80`](#insn-00bedb80)

~~~json
{
  "source": "00bedb80",
  "target": "00bedae4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedb9c`](#insn-00bedb9c)

~~~json
{
  "source": "00bedb9c",
  "target": "00bedb50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedbac`](#insn-00bedbac)

~~~json
{
  "source": "00bedbac",
  "target": "00bedb74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedbb0`](#insn-00bedbb0)

~~~json
{
  "source": "00bedbb0",
  "target": "00bedae4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedbbc`](#insn-00bedbbc)

~~~json
{
  "source": "00bedbbc",
  "target": "00bedcb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedbd4`](#insn-00bedbd4)

~~~json
{
  "source": "00bedbd4",
  "target": "00bedbe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedbe4`](#insn-00bedbe4)

~~~json
{
  "source": "00bedbe4",
  "target": "00bedcb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedbf4`](#insn-00bedbf4)

~~~json
{
  "source": "00bedbf4",
  "target": "00bedbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc04`](#insn-00bedc04)

~~~json
{
  "source": "00bedc04",
  "target": "00bedbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc10`](#insn-00bedc10)

~~~json
{
  "source": "00bedc10",
  "target": "00bedc28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc20`](#insn-00bedc20)

~~~json
{
  "source": "00bedc20",
  "target": "00bedbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc24`](#insn-00bedc24)

~~~json
{
  "source": "00bedc24",
  "target": "00bedc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc40`](#insn-00bedc40)

~~~json
{
  "source": "00bedc40",
  "target": "00bedbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc48`](#insn-00bedc48)

~~~json
{
  "source": "00bedc48",
  "target": "00bedc70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc6c`](#insn-00bedc6c)

~~~json
{
  "source": "00bedc6c",
  "target": "00bedbd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc7c`](#insn-00bedc7c)

~~~json
{
  "source": "00bedc7c",
  "target": "00bedbd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc98`](#insn-00bedc98)

~~~json
{
  "source": "00bedc98",
  "target": "00bedc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedca8`](#insn-00bedca8)

~~~json
{
  "source": "00bedca8",
  "target": "00bedc70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedcac`](#insn-00bedcac)

~~~json
{
  "source": "00bedcac",
  "target": "00bedbd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedcb8`](#insn-00bedcb8)

~~~json
{
  "source": "00bedcb8",
  "target": "00bedcd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedcd4`](#insn-00bedcd4)

~~~json
{
  "source": "00bedcd4",
  "target": "00bedcbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedcec`](#insn-00bedcec)

~~~json
{
  "source": "00bedcec",
  "target": "00bedd18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd14`](#insn-00bedd14)

~~~json
{
  "source": "00bedd14",
  "target": "00bedd44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd34`](#insn-00bedd34)

~~~json
{
  "source": "00bedd34",
  "target": "00bedcf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd40`](#insn-00bedd40)

~~~json
{
  "source": "00bedd40",
  "target": "00bedd08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd4c`](#insn-00bedd4c)

~~~json
{
  "source": "00bedd4c",
  "target": "00bedcc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd6c`](#insn-00bedd6c)

~~~json
{
  "source": "00bedd6c",
  "target": "00bedccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd84`](#insn-00bedd84)

~~~json
{
  "source": "00bedd84",
  "target": "00bedccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd94`](#insn-00bedd94)

~~~json
{
  "source": "00bedd94",
  "target": "00beddb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beddac`](#insn-00beddac)

~~~json
{
  "source": "00beddac",
  "target": "00bedd88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beddb4`](#insn-00beddb4)

~~~json
{
  "source": "00beddb4",
  "target": "00bedccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
