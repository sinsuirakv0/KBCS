# 00bed8bc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0007.md#review-acb08b6d96a8ebacb5ebc47016af3160)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 要確認
  - [v16.0.2 → v16.0.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/review-0004.md#review-acb08b6d96a8ebacb5ebc47016af3160)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bed8bc",
  "name": "FUN_00bed8bc",
  "size": 764,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "504bddb99ace1ca42837ff29eae25d2f3325c7a30dc7cdefe5e9b80c772091da",
  "source_text_sha256": "504bddb99ace1ca42837ff29eae25d2f3325c7a30dc7cdefe5e9b80c772091da",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bed8bc",
        "00bedbb7"
      ]
    ],
    "bytes_sha256": "6003e411dd7b319bad7c92da1a61e481722167449a2e003148513f09196596e2",
    "instruction_count": 191,
    "instruction_bytes": 764,
    "body_bytes": 764,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be6a94](../00be6/00be6a94.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 7008 bytes

~~~c

long * FUN_00bed8bc(long *param_1,long *param_2,long *param_3)

{
  bool bVar1;
  long *plVar2;
  ulong uVar3;
  long lVar4;
  long *plVar5;
  ulong uVar6;
  long lVar7;
  long *plVar8;
  ulong uVar9;
  long *plVar10;
  long *plVar11;
  ulong uVar12;
  long lVar13;
  long lVar14;
  long *plVar15;
  long lVar16;
  
  if (param_1 != param_2) {
    lVar7 = (long)param_2 - (long)param_1 >> 3;
    if (1 < lVar7) {
      uVar9 = lVar7 - 2U >> 1;
      uVar6 = uVar9;
      do {
        if ((long)uVar6 <= (long)uVar9) {
          uVar3 = (uVar6 & 0x1fffffffffffffff) << 1 | 1;
          uVar12 = (uVar6 & 0x1fffffffffffffff) * 2 + 2;
          plVar10 = param_1 + uVar3;
          if ((long)uVar12 < lVar7) {
            lVar16 = *plVar10;
            lVar4 = plVar10[1];
            lVar13 = lVar16;
            if (lVar16 <= lVar4) {
              lVar13 = lVar4;
            }
            plVar11 = plVar10 + 1;
            if (lVar4 <= lVar16) {
              plVar11 = plVar10;
              uVar12 = uVar3;
            }
          }
          else {
            lVar13 = *plVar10;
            plVar11 = plVar10;
            uVar12 = uVar3;
          }
          lVar4 = param_1[uVar6];
          plVar10 = param_1 + uVar6;
          if (lVar4 <= lVar13) {
            do {
              while( true ) {
                plVar8 = plVar11;
                *plVar10 = lVar13;
                if ((long)uVar9 < (long)uVar12) goto LAB_00bed8e4;
                uVar3 = uVar12 << 1 | 1;
                uVar12 = uVar12 * 2 + 2;
                plVar5 = param_1 + uVar3;
                plVar10 = plVar8;
                if ((long)uVar12 < lVar7) break;
                lVar13 = *plVar5;
                plVar11 = plVar5;
                uVar12 = uVar3;
                if (lVar13 < lVar4) goto LAB_00bed8e4;
              }
              lVar14 = *plVar5;
              lVar16 = plVar5[1];
              lVar13 = lVar14;
              if (lVar14 <= lVar16) {
                lVar13 = lVar16;
              }
              plVar11 = plVar5 + 1;
              if (lVar16 <= lVar14) {
                uVar12 = uVar3;
                plVar11 = plVar5;
              }
            } while (lVar4 <= lVar13);
LAB_00bed8e4:
            *plVar8 = lVar4;
          }
        }
        bVar1 = 0 < (long)uVar6;
        uVar6 = uVar6 - 1;
      } while (bVar1);
    }
    plVar10 = param_2;
    if (param_2 != param_3) {
      plVar11 = param_1 + 1;
      plVar8 = param_2;
      do {
        lVar13 = *plVar8;
                    /* try { // try from 00bed9ec to 00ceda8f has its CatchHandler @ 00bed9ec
                       catch() { ... } // from try @ 00bed9ec with catch @ 00bed9ec
                       catch() { ... } // from try @ 00bedafc with catch @ 00bed9ec
                       catch() { ... } // from try @ 00bedcbc with catch @ 00bed9ec */
        if (lVar13 < *param_1) {
          *plVar8 = *param_1;
          *param_1 = lVar13;
          if (1 < lVar7) {
            lVar16 = *plVar11;
            lVar4 = lVar16;
            if ((long)param_2 - (long)param_1 == 0x10) {
              uVar6 = 1;
              plVar10 = plVar11;
            }
            else {
              lVar14 = param_1[2];
              if (lVar16 <= lVar14) {
                lVar4 = lVar14;
              }
              plVar10 = param_1 + 2;
              if (lVar14 <= lVar16) {
                plVar10 = plVar11;
              }
              uVar6 = 1;
              if (lVar16 < lVar14) {
                uVar6 = 2;
              }
            }
            plVar5 = param_1;
            if (lVar13 <= lVar4) {
              do {
                while( true ) {
                  plVar15 = plVar10;
                  *plVar5 = lVar4;
                  if ((long)(lVar7 - 2U >> 1) < (long)uVar6) goto LAB_00bed9d8;
                  uVar9 = uVar6 << 1 | 1;
                  uVar6 = uVar6 * 2 + 2;
                    /* try { // try from 00beda90 to 00ceda9b has its CatchHandler @ 00bedd44 */
                  plVar2 = param_1 + uVar9;
                  plVar5 = plVar15;
                  if ((long)uVar6 < lVar7) break;
                    /* try { // try from 00beda9c to 00cedabf has its CatchHandler @ 00bedde0 */
                  lVar4 = *plVar2;
                  uVar6 = uVar9;
                  plVar10 = plVar2;
                  if (lVar4 < lVar13) goto LAB_00bed9d8;
                }
                lVar14 = *plVar2;
                lVar16 = plVar2[1];
                lVar4 = lVar14;
                if (lVar14 <= lVar16) {
                  lVar4 = lVar16;
                }
                plVar10 = plVar2 + 1;
                if (lVar16 <= lVar14) {
                  uVar6 = uVar9;
                  plVar10 = plVar2;
                }
              } while (lVar13 <= lVar4);
LAB_00bed9d8:
              *plVar15 = lVar13;
            }
          }
        }
        plVar8 = plVar8 + 1;
        plVar10 = param_3;
      } while (plVar8 != param_3);
    }
    param_3 = plVar10;
    if (1 < lVar7) {
      do {
                    /* try { // try from 00bedad8 to 00cedafb has its CatchHandler @ 00bedd54 */
        lVar13 = *param_1;
        uVar6 = 0;
        plVar10 = param_1;
        do {
          uVar12 = uVar6 << 1 | 1;
          uVar9 = uVar6 * 2 + 2;
          plVar11 = plVar10 + uVar6 + 1;
          if ((long)uVar9 < lVar7) {
            lVar16 = plVar10[uVar6 + 2];
            lVar14 = plVar10[uVar6 + 1];
                    /* try { // try from 00bedafc to 00cedcb3 has its CatchHandler @ 00bed9ec */
            lVar4 = lVar14;
            if (lVar14 <= lVar16) {
              lVar4 = lVar16;
            }
            plVar8 = plVar10 + uVar6 + 2;
            uVar6 = uVar9;
            if (lVar16 <= lVar14) {
              plVar8 = plVar11;
              uVar6 = uVar12;
            }
          }
          else {
            lVar4 = *plVar11;
            plVar8 = plVar11;
            uVar6 = uVar12;
          }
          *plVar10 = lVar4;
          plVar10 = plVar8;
        } while ((long)uVar6 <= (long)(lVar7 - 2U >> 1));
        param_2 = param_2 + -1;
        if (plVar8 == param_2) {
          *plVar8 = lVar13;
        }
        else {
          lVar4 = (long)plVar8 + (8 - (long)param_1) >> 3;
          *plVar8 = *param_2;
          *param_2 = lVar13;
          if (1 < lVar4) {
            uVar6 = lVar4 - 2U >> 1;
            lVar13 = *plVar8;
            lVar4 = param_1[uVar6];
            plVar10 = param_1 + uVar6;
            if (lVar4 < lVar13) {
              do {
                plVar11 = plVar10;
                *plVar8 = lVar4;
                if (uVar6 == 0) break;
                uVar6 = uVar6 - 1 >> 1;
                lVar4 = param_1[uVar6];
                plVar8 = plVar11;
                plVar10 = param_1 + uVar6;
              } while (lVar4 < lVar13);
              *plVar11 = lVar13;
            }
          }
        }
        bVar1 = 2 < lVar7;
        lVar7 = lVar7 + -1;
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
<a id="insn-00bed8bc"></a> `00bed8bc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bed8c0"></a> `00bed8c0` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-00bed8c4"></a> `00bed8c4` | `e0 0f 00 54` | b.eq 0x00bedac0 | `CONDITIONAL_JUMP`
<a id="insn-00bed8c8"></a> `00bed8c8` | `29 00 00 cb` | sub x9,x1,x0 | `FALL_THROUGH`
<a id="insn-00bed8cc"></a> `00bed8cc` | `28 fd 43 93` | asr x8,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00bed8d0"></a> `00bed8d0` | `0a 09 00 f1` | subs x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bed8d4"></a> `00bed8d4` | `0b 07 00 54` | b.lt 0x00bed9b4 | `CONDITIONAL_JUMP`
<a id="insn-00bed8d8"></a> `00bed8d8` | `4b fd 41 d3` | lsr x11,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bed8dc"></a> `00bed8dc` | `ec 03 0b aa` | mov x12,x11 | `FALL_THROUGH`
<a id="insn-00bed8e0"></a> `00bed8e0` | `05 00 00 14` | b 0x00bed8f4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bed8e4"></a> `00bed8e4` | `0f 02 00 f9` | str x15,[x16] | `FALL_THROUGH`
<a id="insn-00bed8e8"></a> `00bed8e8` | `9f 01 00 f1` | cmp x12,#0x0 | `FALL_THROUGH`
<a id="insn-00bed8ec"></a> `00bed8ec` | `8c 05 00 d1` | sub x12,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00bed8f0"></a> `00bed8f0` | `2d 06 00 54` | b.le 0x00bed9b4 | `CONDITIONAL_JUMP`
<a id="insn-00bed8f4"></a> `00bed8f4` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-00bed8f8"></a> `00bed8f8` | `8b ff ff 54` | b.lt 0x00bed8e8 | `CONDITIONAL_JUMP`
<a id="insn-00bed8fc"></a> `00bed8fc` | `2e 00 80 52` | mov w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bed900"></a> `00bed900` | `8d f1 7f d3` | ubfiz x13,x12,#0x1,#0x3d | `FALL_THROUGH`
<a id="insn-00bed904"></a> `00bed904` | `8e f1 7f b3` | bfm x14,x12,#0x3f,#0x3c | `FALL_THROUGH`
<a id="insn-00bed908"></a> `00bed908` | `af 09 00 91` | add x15,x13,#0x2 | `FALL_THROUGH`
<a id="insn-00bed90c"></a> `00bed90c` | `0d 0c 0e 8b` | add x13,x0,x14, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bed910"></a> `00bed910` | `ff 01 08 eb` | cmp x15,x8 | `FALL_THROUGH`
<a id="insn-00bed914"></a> `00bed914` | `2a 01 00 54` | b.ge 0x00bed938 | `CONDITIONAL_JUMP`
<a id="insn-00bed918"></a> `00bed918` | `f0 03 0d aa` | mov x16,x13 | `FALL_THROUGH`
<a id="insn-00bed91c"></a> `00bed91c` | `b1 01 40 f9` | ldr x17,[x13] | `FALL_THROUGH`
<a id="insn-00bed920"></a> `00bed920` | `03 8e 40 f8` | ldr x3,[x16, #0x8]! | `FALL_THROUGH`
<a id="insn-00bed924"></a> `00bed924` | `3f 02 03 eb` | cmp x17,x3 | `FALL_THROUGH`
<a id="insn-00bed928"></a> `00bed928` | `31 c2 83 9a` | csel x17,x17,x3,gt | `FALL_THROUGH`
<a id="insn-00bed92c"></a> `00bed92c` | `0d b2 8d 9a` | csel x13,x16,x13,lt | `FALL_THROUGH`
<a id="insn-00bed930"></a> `00bed930` | `ee b1 8e 9a` | csel x14,x15,x14,lt | `FALL_THROUGH`
<a id="insn-00bed934"></a> `00bed934` | `02 00 00 14` | b 0x00bed93c | `UNCONDITIONAL_JUMP`
<a id="insn-00bed938"></a> `00bed938` | `b1 01 40 f9` | ldr x17,[x13] | `FALL_THROUGH`
<a id="insn-00bed93c"></a> `00bed93c` | `10 0c 0c 8b` | add x16,x0,x12, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bed940"></a> `00bed940` | `0f 02 40 f9` | ldr x15,[x16] | `FALL_THROUGH`
<a id="insn-00bed944"></a> `00bed944` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bed948"></a> `00bed948` | `6a 01 00 54` | b.ge 0x00bed974 | `CONDITIONAL_JUMP`
<a id="insn-00bed94c"></a> `00bed94c` | `e7 ff ff 17` | b 0x00bed8e8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bed950"></a> `00bed950` | `e4 03 0d aa` | mov x4,x13 | `FALL_THROUGH`
<a id="insn-00bed954"></a> `00bed954` | `b1 01 40 f9` | ldr x17,[x13] | `FALL_THROUGH`
<a id="insn-00bed958"></a> `00bed958` | `85 8c 40 f8` | ldr x5,[x4, #0x8]! | `FALL_THROUGH`
<a id="insn-00bed95c"></a> `00bed95c` | `3f 02 05 eb` | cmp x17,x5 | `FALL_THROUGH`
<a id="insn-00bed960"></a> `00bed960` | `31 c2 85 9a` | csel x17,x17,x5,gt | `FALL_THROUGH`
<a id="insn-00bed964"></a> `00bed964` | `8d b0 8d 9a` | csel x13,x4,x13,lt | `FALL_THROUGH`
<a id="insn-00bed968"></a> `00bed968` | `ce b1 83 9a` | csel x14,x14,x3,lt | `FALL_THROUGH`
<a id="insn-00bed96c"></a> `00bed96c` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bed970"></a> `00bed970` | `ab fb ff 54` | b.lt 0x00bed8e4 | `CONDITIONAL_JUMP`
<a id="insn-00bed974"></a> `00bed974` | `7f 01 0e eb` | cmp x11,x14 | `FALL_THROUGH`
<a id="insn-00bed978"></a> `00bed978` | `11 02 00 f9` | str x17,[x16] | `FALL_THROUGH`
<a id="insn-00bed97c"></a> `00bed97c` | `f0 03 0d aa` | mov x16,x13 | `FALL_THROUGH`
<a id="insn-00bed980"></a> `00bed980` | `2b fb ff 54` | b.lt 0x00bed8e4 | `CONDITIONAL_JUMP`
<a id="insn-00bed984"></a> `00bed984` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bed988"></a> `00bed988` | `cd f9 7f d3` | lsl x13,x14,#0x1 | `FALL_THROUGH`
<a id="insn-00bed98c"></a> `00bed98c` | `c3 f9 7f b3` | bfm x3,x14,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bed990"></a> `00bed990` | `ae 09 00 91` | add x14,x13,#0x2 | `FALL_THROUGH`
<a id="insn-00bed994"></a> `00bed994` | `0d 0c 03 8b` | add x13,x0,x3, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bed998"></a> `00bed998` | `df 01 08 eb` | cmp x14,x8 | `FALL_THROUGH`
<a id="insn-00bed99c"></a> `00bed99c` | `ab fd ff 54` | b.lt 0x00bed950 | `CONDITIONAL_JUMP`
<a id="insn-00bed9a0"></a> `00bed9a0` | `b1 01 40 f9` | ldr x17,[x13] | `FALL_THROUGH`
<a id="insn-00bed9a4"></a> `00bed9a4` | `ee 03 03 aa` | mov x14,x3 | `FALL_THROUGH`
<a id="insn-00bed9a8"></a> `00bed9a8` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bed9ac"></a> `00bed9ac` | `4a fe ff 54` | b.ge 0x00bed974 | `CONDITIONAL_JUMP`
<a id="insn-00bed9b0"></a> `00bed9b0` | `cd ff ff 17` | b 0x00bed8e4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bed9b4"></a> `00bed9b4` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-00bed9b8"></a> `00bed9b8` | `e3 03 01 aa` | mov x3,x1 | `FALL_THROUGH`
<a id="insn-00bed9bc"></a> `00bed9bc` | `c0 07 00 54` | b.eq 0x00bedab4 | `CONDITIONAL_JUMP`
<a id="insn-00bed9c0"></a> `00bed9c0` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bed9c4"></a> `00bed9c4` | `0b 20 00 91` | add x11,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bed9c8"></a> `00bed9c8` | `0c 40 00 91` | add x12,x0,#0x10 | `FALL_THROUGH`
<a id="insn-00bed9cc"></a> `00bed9cc` | `2d 00 80 52` | mov w13,#0x1 | `FALL_THROUGH`
<a id="insn-00bed9d0"></a> `00bed9d0` | `ee 03 01 aa` | mov x14,x1 | `FALL_THROUGH`
<a id="insn-00bed9d4"></a> `00bed9d4` | `05 00 00 14` | b 0x00bed9e8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bed9d8"></a> `00bed9d8` | `6f 00 00 f9` | str x15,[x3] | `FALL_THROUGH`
<a id="insn-00bed9dc"></a> `00bed9dc` | `ce 21 00 91` | add x14,x14,#0x8 | `FALL_THROUGH`
<a id="insn-00bed9e0"></a> `00bed9e0` | `df 01 02 eb` | cmp x14,x2 | `FALL_THROUGH`
<a id="insn-00bed9e4"></a> `00bed9e4` | `60 06 00 54` | b.eq 0x00bedab0 | `CONDITIONAL_JUMP`
<a id="insn-00bed9e8"></a> `00bed9e8` | `cf 01 40 f9` | ldr x15,[x14] | `FALL_THROUGH`
<a id="insn-00bed9ec"></a> `00bed9ec` | `10 00 40 f9` | ldr x16,[x0] | `FALL_THROUGH`
<a id="insn-00bed9f0"></a> `00bed9f0` | `ff 01 10 eb` | cmp x15,x16 | `FALL_THROUGH`
<a id="insn-00bed9f4"></a> `00bed9f4` | `4a ff ff 54` | b.ge 0x00bed9dc | `CONDITIONAL_JUMP`
<a id="insn-00bed9f8"></a> `00bed9f8` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bed9fc"></a> `00bed9fc` | `d0 01 00 f9` | str x16,[x14] | `FALL_THROUGH`
<a id="insn-00beda00"></a> `00beda00` | `0f 00 00 f9` | str x15,[x0] | `FALL_THROUGH`
<a id="insn-00beda04"></a> `00beda04` | `cb fe ff 54` | b.lt 0x00bed9dc | `CONDITIONAL_JUMP`
<a id="insn-00beda08"></a> `00beda08` | `71 01 40 f9` | ldr x17,[x11] | `FALL_THROUGH`
<a id="insn-00beda0c"></a> `00beda0c` | `3f 41 00 f1` | cmp x9,#0x10 | `FALL_THROUGH`
<a id="insn-00beda10"></a> `00beda10` | `c1 00 00 54` | b.ne 0x00beda28 | `CONDITIONAL_JUMP`
<a id="insn-00beda14"></a> `00beda14` | `f0 03 0b aa` | mov x16,x11 | `FALL_THROUGH`
<a id="insn-00beda18"></a> `00beda18` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-00beda1c"></a> `00beda1c` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00beda20"></a> `00beda20` | `eb fd ff 54` | b.lt 0x00bed9dc | `CONDITIONAL_JUMP`
<a id="insn-00beda24"></a> `00beda24` | `08 00 00 14` | b 0x00beda44 | `UNCONDITIONAL_JUMP`
<a id="insn-00beda28"></a> `00beda28` | `90 01 40 f9` | ldr x16,[x12] | `FALL_THROUGH`
<a id="insn-00beda2c"></a> `00beda2c` | `3f 02 10 eb` | cmp x17,x16 | `FALL_THROUGH`
<a id="insn-00beda30"></a> `00beda30` | `31 c2 90 9a` | csel x17,x17,x16,gt | `FALL_THROUGH`
<a id="insn-00beda34"></a> `00beda34` | `90 b1 8b 9a` | csel x16,x12,x11,lt | `FALL_THROUGH`
<a id="insn-00beda38"></a> `00beda38` | `a4 a5 8d 9a` | cinc x4,x13,lt | `FALL_THROUGH`
<a id="insn-00beda3c"></a> `00beda3c` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00beda40"></a> `00beda40` | `eb fc ff 54` | b.lt 0x00bed9dc | `CONDITIONAL_JUMP`
<a id="insn-00beda44"></a> `00beda44` | `e3 03 00 aa` | mov x3,x0 | `FALL_THROUGH`
<a id="insn-00beda48"></a> `00beda48` | `0a 00 00 14` | b 0x00beda70 | `UNCONDITIONAL_JUMP`
<a id="insn-00beda4c"></a> `00beda4c` | `e6 03 10 aa` | mov x6,x16 | `FALL_THROUGH`
<a id="insn-00beda50"></a> `00beda50` | `11 02 40 f9` | ldr x17,[x16] | `FALL_THROUGH`
<a id="insn-00beda54"></a> `00beda54` | `c7 8c 40 f8` | ldr x7,[x6, #0x8]! | `FALL_THROUGH`
<a id="insn-00beda58"></a> `00beda58` | `3f 02 07 eb` | cmp x17,x7 | `FALL_THROUGH`
<a id="insn-00beda5c"></a> `00beda5c` | `31 c2 87 9a` | csel x17,x17,x7,gt | `FALL_THROUGH`
<a id="insn-00beda60"></a> `00beda60` | `d0 b0 90 9a` | csel x16,x6,x16,lt | `FALL_THROUGH`
<a id="insn-00beda64"></a> `00beda64` | `84 b0 85 9a` | csel x4,x4,x5,lt | `FALL_THROUGH`
<a id="insn-00beda68"></a> `00beda68` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00beda6c"></a> `00beda6c` | `6b fb ff 54` | b.lt 0x00bed9d8 | `CONDITIONAL_JUMP`
<a id="insn-00beda70"></a> `00beda70` | `5f 01 04 eb` | cmp x10,x4 | `FALL_THROUGH`
<a id="insn-00beda74"></a> `00beda74` | `71 00 00 f9` | str x17,[x3] | `FALL_THROUGH`
<a id="insn-00beda78"></a> `00beda78` | `e3 03 10 aa` | mov x3,x16 | `FALL_THROUGH`
<a id="insn-00beda7c"></a> `00beda7c` | `eb fa ff 54` | b.lt 0x00bed9d8 | `CONDITIONAL_JUMP`
<a id="insn-00beda80"></a> `00beda80` | `25 00 80 52` | mov w5,#0x1 | `FALL_THROUGH`
<a id="insn-00beda84"></a> `00beda84` | `90 f8 7f d3` | lsl x16,x4,#0x1 | `FALL_THROUGH`
<a id="insn-00beda88"></a> `00beda88` | `85 f8 7f b3` | bfm x5,x4,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00beda8c"></a> `00beda8c` | `04 0a 00 91` | add x4,x16,#0x2 | `FALL_THROUGH`
<a id="insn-00beda90"></a> `00beda90` | `10 0c 05 8b` | add x16,x0,x5, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00beda94"></a> `00beda94` | `9f 00 08 eb` | cmp x4,x8 | `FALL_THROUGH`
<a id="insn-00beda98"></a> `00beda98` | `ab fd ff 54` | b.lt 0x00beda4c | `CONDITIONAL_JUMP`
<a id="insn-00beda9c"></a> `00beda9c` | `11 02 40 f9` | ldr x17,[x16] | `FALL_THROUGH`
<a id="insn-00bedaa0"></a> `00bedaa0` | `e4 03 05 aa` | mov x4,x5 | `FALL_THROUGH`
<a id="insn-00bedaa4"></a> `00bedaa4` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bedaa8"></a> `00bedaa8` | `4a fe ff 54` | b.ge 0x00beda70 | `CONDITIONAL_JUMP`
<a id="insn-00bedaac"></a> `00bedaac` | `cb ff ff 17` | b 0x00bed9d8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedab0"></a> `00bedab0` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bedab4"></a> `00bedab4` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bedab8"></a> `00bedab8` | `0a 01 00 54` | b.ge 0x00bedad8 | `CONDITIONAL_JUMP`
<a id="insn-00bedabc"></a> `00bedabc` | `e2 03 03 aa` | mov x2,x3 | `FALL_THROUGH`
<a id="insn-00bedac0"></a> `00bedac0` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bedac4"></a> `00bedac4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bedac8"></a> `00bedac8` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bedacc"></a> `00bedacc` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bedad0"></a> `00bedad0` | `08 05 00 d1` | sub x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bedad4"></a> `00bedad4` | `4d ff ff 54` | b.le 0x00bedabc | `CONDITIONAL_JUMP`
<a id="insn-00bedad8"></a> `00bedad8` | `09 09 00 d1` | sub x9,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bedadc"></a> `00bedadc` | `0a 00 40 f9` | ldr x10,[x0] | `FALL_THROUGH`
<a id="insn-00bedae0"></a> `00bedae0` | `ed 03 1f aa` | mov x13,xzr | `FALL_THROUGH`
<a id="insn-00bedae4"></a> `00bedae4` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bedae8"></a> `00bedae8` | `ec 03 00 aa` | mov x12,x0 | `FALL_THROUGH`
<a id="insn-00bedaec"></a> `00bedaec` | `0b 00 00 14` | b 0x00bedb18 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedaf0"></a> `00bedaf0` | `0d 0e 41 f8` | ldr x13,[x16, #0x10]! | `FALL_THROUGH`
<a id="insn-00bedaf4"></a> `00bedaf4` | `0f 82 5f f8` | ldur x15,[x16, #-0x8] | `FALL_THROUGH`
<a id="insn-00bedaf8"></a> `00bedaf8` | `ff 01 0d eb` | cmp x15,x13 | `FALL_THROUGH`
<a id="insn-00bedafc"></a> `00bedafc` | `ef c1 8d 9a` | csel x15,x15,x13,gt | `FALL_THROUGH`
<a id="insn-00bedb00"></a> `00bedb00` | `09 b2 89 9a` | csel x9,x16,x9,lt | `FALL_THROUGH`
<a id="insn-00bedb04"></a> `00bedb04` | `2d b2 8e 9a` | csel x13,x17,x14,lt | `FALL_THROUGH`
<a id="insn-00bedb08"></a> `00bedb08` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00bedb0c"></a> `00bedb0c` | `8f 01 00 f9` | str x15,[x12] | `FALL_THROUGH`
<a id="insn-00bedb10"></a> `00bedb10` | `ec 03 09 aa` | mov x12,x9 | `FALL_THROUGH`
<a id="insn-00bedb14"></a> `00bedb14` | `8c 01 00 54` | b.gt 0x00bedb44 | `CONDITIONAL_JUMP`
<a id="insn-00bedb18"></a> `00bedb18` | `a9 f9 7f d3` | lsl x9,x13,#0x1 | `FALL_THROUGH`
<a id="insn-00bedb1c"></a> `00bedb1c` | `90 0d 0d 8b` | add x16,x12,x13, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bedb20"></a> `00bedb20` | `2e 00 80 52` | mov w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bedb24"></a> `00bedb24` | `ae f9 7f b3` | bfm x14,x13,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bedb28"></a> `00bedb28` | `31 09 00 91` | add x17,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bedb2c"></a> `00bedb2c` | `09 22 00 91` | add x9,x16,#0x8 | `FALL_THROUGH`
<a id="insn-00bedb30"></a> `00bedb30` | `3f 02 08 eb` | cmp x17,x8 | `FALL_THROUGH`
<a id="insn-00bedb34"></a> `00bedb34` | `eb fd ff 54` | b.lt 0x00bedaf0 | `CONDITIONAL_JUMP`
<a id="insn-00bedb38"></a> `00bedb38` | `2f 01 40 f9` | ldr x15,[x9] | `FALL_THROUGH`
<a id="insn-00bedb3c"></a> `00bedb3c` | `ed 03 0e aa` | mov x13,x14 | `FALL_THROUGH`
<a id="insn-00bedb40"></a> `00bedb40` | `f2 ff ff 17` | b 0x00bedb08 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedb44"></a> `00bedb44` | `21 20 00 d1` | sub x1,x1,#0x8 | `FALL_THROUGH`
<a id="insn-00bedb48"></a> `00bedb48` | `3f 01 01 eb` | cmp x9,x1 | `FALL_THROUGH`
<a id="insn-00bedb4c"></a> `00bedb4c` | `e0 fb ff 54` | b.eq 0x00bedac8 | `CONDITIONAL_JUMP`
<a id="insn-00bedb50"></a> `00bedb50` | `2b 01 00 cb` | sub x11,x9,x0 | `FALL_THROUGH`
<a id="insn-00bedb54"></a> `00bedb54` | `2c 00 40 f9` | ldr x12,[x1] | `FALL_THROUGH`
<a id="insn-00bedb58"></a> `00bedb58` | `6b 21 00 91` | add x11,x11,#0x8 | `FALL_THROUGH`
<a id="insn-00bedb5c"></a> `00bedb5c` | `6b fd 43 93` | asr x11,x11,#0x3 | `FALL_THROUGH`
<a id="insn-00bedb60"></a> `00bedb60` | `2c 01 00 f9` | str x12,[x9] | `FALL_THROUGH`
<a id="insn-00bedb64"></a> `00bedb64` | `2a 00 00 f9` | str x10,[x1] | `FALL_THROUGH`
<a id="insn-00bedb68"></a> `00bedb68` | `6b 09 00 f1` | subs x11,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00bedb6c"></a> `00bedb6c` | `0b fb ff 54` | b.lt 0x00bedacc | `CONDITIONAL_JUMP`
<a id="insn-00bedb70"></a> `00bedb70` | `6a fd 41 d3` | lsr x10,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00bedb74"></a> `00bedb74` | `2b 01 40 f9` | ldr x11,[x9] | `FALL_THROUGH`
<a id="insn-00bedb78"></a> `00bedb78` | `0c 0c 0a 8b` | add x12,x0,x10, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bedb7c"></a> `00bedb7c` | `8d 01 40 f9` | ldr x13,[x12] | `FALL_THROUGH`
<a id="insn-00bedb80"></a> `00bedb80` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00bedb84"></a> `00bedb84` | `4a fa ff 54` | b.ge 0x00bedacc | `CONDITIONAL_JUMP`
<a id="insn-00bedb88"></a> `00bedb88` | `ee 03 09 aa` | mov x14,x9 | `FALL_THROUGH`
<a id="insn-00bedb8c"></a> `00bedb8c` | `e9 03 0c aa` | mov x9,x12 | `FALL_THROUGH`
<a id="insn-00bedb90"></a> `00bedb90` | `cd 01 00 f9` | str x13,[x14] | `FALL_THROUGH`
<a id="insn-00bedb94"></a> `00bedb94` | `ea 00 00 b4` | cbz x10,0x00bedbb0 | `CONDITIONAL_JUMP`
<a id="insn-00bedb98"></a> `00bedb98` | `4a 05 00 d1` | sub x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bedb9c"></a> `00bedb9c` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bedba0"></a> `00bedba0` | `0c 0c 0a 8b` | add x12,x0,x10, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bedba4"></a> `00bedba4` | `8d 01 40 f9` | ldr x13,[x12] | `FALL_THROUGH`
<a id="insn-00bedba8"></a> `00bedba8` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00bedbac"></a> `00bedbac` | `eb fe ff 54` | b.lt 0x00bedb88 | `CONDITIONAL_JUMP`
<a id="insn-00bedbb0"></a> `00bedbb0` | `2b 01 00 f9` | str x11,[x9] | `FALL_THROUGH`
<a id="insn-00bedbb4"></a> `00bedbb4` | `c6 ff ff 17` | b 0x00bedacc | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bed8bc`](#insn-00bed8bc) 範囲 `[['00bed8bc', '00bed8c7']]`
  - `CONDITIONAL_JUMP` [`00bed8c4`](#insn-00bed8c4) → [`00bedac0`](#insn-00bedac0)
  - `FALL_THROUGH` [`00bed8c4`](#insn-00bed8c4) → [`00bed8c8`](#insn-00bed8c8)
- ブロック [`00bed8c8`](#insn-00bed8c8) 範囲 `[['00bed8c8', '00bed8d7']]`
  - `CONDITIONAL_JUMP` [`00bed8d4`](#insn-00bed8d4) → [`00bed9b4`](#insn-00bed9b4)
  - `FALL_THROUGH` [`00bed8d4`](#insn-00bed8d4) → [`00bed8d8`](#insn-00bed8d8)
- ブロック [`00bed8d8`](#insn-00bed8d8) 範囲 `[['00bed8d8', '00bed8e3']]`
  - `UNCONDITIONAL_JUMP` [`00bed8e0`](#insn-00bed8e0) → [`00bed8f4`](#insn-00bed8f4)
- ブロック [`00bed8e4`](#insn-00bed8e4) 範囲 `[['00bed8e4', '00bed8e7']]`
  - `FALL_THROUGH` [`00bed8e4`](#insn-00bed8e4) → [`00bed8e8`](#insn-00bed8e8)
- ブロック [`00bed8e8`](#insn-00bed8e8) 範囲 `[['00bed8e8', '00bed8f3']]`
  - `CONDITIONAL_JUMP` [`00bed8f0`](#insn-00bed8f0) → [`00bed9b4`](#insn-00bed9b4)
  - `FALL_THROUGH` [`00bed8f0`](#insn-00bed8f0) → [`00bed8f4`](#insn-00bed8f4)
- ブロック [`00bed8f4`](#insn-00bed8f4) 範囲 `[['00bed8f4', '00bed8fb']]`
  - `CONDITIONAL_JUMP` [`00bed8f8`](#insn-00bed8f8) → [`00bed8e8`](#insn-00bed8e8)
  - `FALL_THROUGH` [`00bed8f8`](#insn-00bed8f8) → [`00bed8fc`](#insn-00bed8fc)
- ブロック [`00bed8fc`](#insn-00bed8fc) 範囲 `[['00bed8fc', '00bed917']]`
  - `CONDITIONAL_JUMP` [`00bed914`](#insn-00bed914) → [`00bed938`](#insn-00bed938)
  - `FALL_THROUGH` [`00bed914`](#insn-00bed914) → [`00bed918`](#insn-00bed918)
- ブロック [`00bed918`](#insn-00bed918) 範囲 `[['00bed918', '00bed937']]`
  - `UNCONDITIONAL_JUMP` [`00bed934`](#insn-00bed934) → [`00bed93c`](#insn-00bed93c)
- ブロック [`00bed938`](#insn-00bed938) 範囲 `[['00bed938', '00bed93b']]`
  - `FALL_THROUGH` [`00bed938`](#insn-00bed938) → [`00bed93c`](#insn-00bed93c)
- ブロック [`00bed93c`](#insn-00bed93c) 範囲 `[['00bed93c', '00bed94b']]`
  - `CONDITIONAL_JUMP` [`00bed948`](#insn-00bed948) → [`00bed974`](#insn-00bed974)
  - `FALL_THROUGH` [`00bed948`](#insn-00bed948) → [`00bed94c`](#insn-00bed94c)
- ブロック [`00bed94c`](#insn-00bed94c) 範囲 `[['00bed94c', '00bed94f']]`
  - `UNCONDITIONAL_JUMP` [`00bed94c`](#insn-00bed94c) → [`00bed8e8`](#insn-00bed8e8)
- ブロック [`00bed950`](#insn-00bed950) 範囲 `[['00bed950', '00bed973']]`
  - `CONDITIONAL_JUMP` [`00bed970`](#insn-00bed970) → [`00bed8e4`](#insn-00bed8e4)
  - `FALL_THROUGH` [`00bed970`](#insn-00bed970) → [`00bed974`](#insn-00bed974)
- ブロック [`00bed974`](#insn-00bed974) 範囲 `[['00bed974', '00bed983']]`
  - `CONDITIONAL_JUMP` [`00bed980`](#insn-00bed980) → [`00bed8e4`](#insn-00bed8e4)
  - `FALL_THROUGH` [`00bed980`](#insn-00bed980) → [`00bed984`](#insn-00bed984)
- ブロック [`00bed984`](#insn-00bed984) 範囲 `[['00bed984', '00bed99f']]`
  - `CONDITIONAL_JUMP` [`00bed99c`](#insn-00bed99c) → [`00bed950`](#insn-00bed950)
  - `FALL_THROUGH` [`00bed99c`](#insn-00bed99c) → [`00bed9a0`](#insn-00bed9a0)
- ブロック [`00bed9a0`](#insn-00bed9a0) 範囲 `[['00bed9a0', '00bed9af']]`
  - `CONDITIONAL_JUMP` [`00bed9ac`](#insn-00bed9ac) → [`00bed974`](#insn-00bed974)
  - `FALL_THROUGH` [`00bed9ac`](#insn-00bed9ac) → [`00bed9b0`](#insn-00bed9b0)
- ブロック [`00bed9b0`](#insn-00bed9b0) 範囲 `[['00bed9b0', '00bed9b3']]`
  - `UNCONDITIONAL_JUMP` [`00bed9b0`](#insn-00bed9b0) → [`00bed8e4`](#insn-00bed8e4)
- ブロック [`00bed9b4`](#insn-00bed9b4) 範囲 `[['00bed9b4', '00bed9bf']]`
  - `CONDITIONAL_JUMP` [`00bed9bc`](#insn-00bed9bc) → [`00bedab4`](#insn-00bedab4)
  - `FALL_THROUGH` [`00bed9bc`](#insn-00bed9bc) → [`00bed9c0`](#insn-00bed9c0)
- ブロック [`00bed9c0`](#insn-00bed9c0) 範囲 `[['00bed9c0', '00bed9d7']]`
  - `UNCONDITIONAL_JUMP` [`00bed9d4`](#insn-00bed9d4) → [`00bed9e8`](#insn-00bed9e8)
- ブロック [`00bed9d8`](#insn-00bed9d8) 範囲 `[['00bed9d8', '00bed9db']]`
  - `FALL_THROUGH` [`00bed9d8`](#insn-00bed9d8) → [`00bed9dc`](#insn-00bed9dc)
- ブロック [`00bed9dc`](#insn-00bed9dc) 範囲 `[['00bed9dc', '00bed9e7']]`
  - `CONDITIONAL_JUMP` [`00bed9e4`](#insn-00bed9e4) → [`00bedab0`](#insn-00bedab0)
  - `FALL_THROUGH` [`00bed9e4`](#insn-00bed9e4) → [`00bed9e8`](#insn-00bed9e8)
- ブロック [`00bed9e8`](#insn-00bed9e8) 範囲 `[['00bed9e8', '00bed9eb']]`
  - `FALL_THROUGH` [`00bed9e8`](#insn-00bed9e8) → [`00bed9ec`](#insn-00bed9ec)
- ブロック [`00bed9ec`](#insn-00bed9ec) 範囲 `[['00bed9ec', '00bed9f7']]`
  - `CONDITIONAL_JUMP` [`00bed9f4`](#insn-00bed9f4) → [`00bed9dc`](#insn-00bed9dc)
  - `FALL_THROUGH` [`00bed9f4`](#insn-00bed9f4) → [`00bed9f8`](#insn-00bed9f8)
- ブロック [`00bed9f8`](#insn-00bed9f8) 範囲 `[['00bed9f8', '00beda07']]`
  - `CONDITIONAL_JUMP` [`00beda04`](#insn-00beda04) → [`00bed9dc`](#insn-00bed9dc)
  - `FALL_THROUGH` [`00beda04`](#insn-00beda04) → [`00beda08`](#insn-00beda08)
- ブロック [`00beda08`](#insn-00beda08) 範囲 `[['00beda08', '00beda13']]`
  - `CONDITIONAL_JUMP` [`00beda10`](#insn-00beda10) → [`00beda28`](#insn-00beda28)
  - `FALL_THROUGH` [`00beda10`](#insn-00beda10) → [`00beda14`](#insn-00beda14)
- ブロック [`00beda14`](#insn-00beda14) 範囲 `[['00beda14', '00beda23']]`
  - `CONDITIONAL_JUMP` [`00beda20`](#insn-00beda20) → [`00bed9dc`](#insn-00bed9dc)
  - `FALL_THROUGH` [`00beda20`](#insn-00beda20) → [`00beda24`](#insn-00beda24)
- ブロック [`00beda24`](#insn-00beda24) 範囲 `[['00beda24', '00beda27']]`
  - `UNCONDITIONAL_JUMP` [`00beda24`](#insn-00beda24) → [`00beda44`](#insn-00beda44)
- ブロック [`00beda28`](#insn-00beda28) 範囲 `[['00beda28', '00beda43']]`
  - `CONDITIONAL_JUMP` [`00beda40`](#insn-00beda40) → [`00bed9dc`](#insn-00bed9dc)
  - `FALL_THROUGH` [`00beda40`](#insn-00beda40) → [`00beda44`](#insn-00beda44)
- ブロック [`00beda44`](#insn-00beda44) 範囲 `[['00beda44', '00beda4b']]`
  - `UNCONDITIONAL_JUMP` [`00beda48`](#insn-00beda48) → [`00beda70`](#insn-00beda70)
- ブロック [`00beda4c`](#insn-00beda4c) 範囲 `[['00beda4c', '00beda6f']]`
  - `CONDITIONAL_JUMP` [`00beda6c`](#insn-00beda6c) → [`00bed9d8`](#insn-00bed9d8)
  - `FALL_THROUGH` [`00beda6c`](#insn-00beda6c) → [`00beda70`](#insn-00beda70)
- ブロック [`00beda70`](#insn-00beda70) 範囲 `[['00beda70', '00beda7f']]`
  - `CONDITIONAL_JUMP` [`00beda7c`](#insn-00beda7c) → [`00bed9d8`](#insn-00bed9d8)
  - `FALL_THROUGH` [`00beda7c`](#insn-00beda7c) → [`00beda80`](#insn-00beda80)
- ブロック [`00beda80`](#insn-00beda80) 範囲 `[['00beda80', '00beda8f']]`
  - `FALL_THROUGH` [`00beda8c`](#insn-00beda8c) → [`00beda90`](#insn-00beda90)
- ブロック [`00beda90`](#insn-00beda90) 範囲 `[['00beda90', '00beda9b']]`
  - `CONDITIONAL_JUMP` [`00beda98`](#insn-00beda98) → [`00beda4c`](#insn-00beda4c)
  - `FALL_THROUGH` [`00beda98`](#insn-00beda98) → [`00beda9c`](#insn-00beda9c)
- ブロック [`00beda9c`](#insn-00beda9c) 範囲 `[['00beda9c', '00bedaab']]`
  - `CONDITIONAL_JUMP` [`00bedaa8`](#insn-00bedaa8) → [`00beda70`](#insn-00beda70)
  - `FALL_THROUGH` [`00bedaa8`](#insn-00bedaa8) → [`00bedaac`](#insn-00bedaac)
- ブロック [`00bedaac`](#insn-00bedaac) 範囲 `[['00bedaac', '00bedaaf']]`
  - `UNCONDITIONAL_JUMP` [`00bedaac`](#insn-00bedaac) → [`00bed9d8`](#insn-00bed9d8)
- ブロック [`00bedab0`](#insn-00bedab0) 範囲 `[['00bedab0', '00bedab3']]`
  - `FALL_THROUGH` [`00bedab0`](#insn-00bedab0) → [`00bedab4`](#insn-00bedab4)
- ブロック [`00bedab4`](#insn-00bedab4) 範囲 `[['00bedab4', '00bedabb']]`
  - `CONDITIONAL_JUMP` [`00bedab8`](#insn-00bedab8) → [`00bedad8`](#insn-00bedad8)
  - `FALL_THROUGH` [`00bedab8`](#insn-00bedab8) → [`00bedabc`](#insn-00bedabc)
- ブロック [`00bedabc`](#insn-00bedabc) 範囲 `[['00bedabc', '00bedabf']]`
  - `FALL_THROUGH` [`00bedabc`](#insn-00bedabc) → [`00bedac0`](#insn-00bedac0)
- ブロック [`00bedac0`](#insn-00bedac0) 範囲 `[['00bedac0', '00bedac7']]`
- ブロック [`00bedac8`](#insn-00bedac8) 範囲 `[['00bedac8', '00bedacb']]`
  - `FALL_THROUGH` [`00bedac8`](#insn-00bedac8) → [`00bedacc`](#insn-00bedacc)
- ブロック [`00bedacc`](#insn-00bedacc) 範囲 `[['00bedacc', '00bedad7']]`
  - `CONDITIONAL_JUMP` [`00bedad4`](#insn-00bedad4) → [`00bedabc`](#insn-00bedabc)
  - `FALL_THROUGH` [`00bedad4`](#insn-00bedad4) → [`00bedad8`](#insn-00bedad8)
- ブロック [`00bedad8`](#insn-00bedad8) 範囲 `[['00bedad8', '00bedaef']]`
  - `UNCONDITIONAL_JUMP` [`00bedaec`](#insn-00bedaec) → [`00bedb18`](#insn-00bedb18)
- ブロック [`00bedaf0`](#insn-00bedaf0) 範囲 `[['00bedaf0', '00bedafb']]`
  - `FALL_THROUGH` [`00bedaf8`](#insn-00bedaf8) → [`00bedafc`](#insn-00bedafc)
- ブロック [`00bedafc`](#insn-00bedafc) 範囲 `[['00bedafc', '00bedb07']]`
  - `FALL_THROUGH` [`00bedb04`](#insn-00bedb04) → [`00bedb08`](#insn-00bedb08)
- ブロック [`00bedb08`](#insn-00bedb08) 範囲 `[['00bedb08', '00bedb17']]`
  - `CONDITIONAL_JUMP` [`00bedb14`](#insn-00bedb14) → [`00bedb44`](#insn-00bedb44)
  - `FALL_THROUGH` [`00bedb14`](#insn-00bedb14) → [`00bedb18`](#insn-00bedb18)
- ブロック [`00bedb18`](#insn-00bedb18) 範囲 `[['00bedb18', '00bedb37']]`
  - `CONDITIONAL_JUMP` [`00bedb34`](#insn-00bedb34) → [`00bedaf0`](#insn-00bedaf0)
  - `FALL_THROUGH` [`00bedb34`](#insn-00bedb34) → [`00bedb38`](#insn-00bedb38)
- ブロック [`00bedb38`](#insn-00bedb38) 範囲 `[['00bedb38', '00bedb43']]`
  - `UNCONDITIONAL_JUMP` [`00bedb40`](#insn-00bedb40) → [`00bedb08`](#insn-00bedb08)
- ブロック [`00bedb44`](#insn-00bedb44) 範囲 `[['00bedb44', '00bedb4f']]`
  - `CONDITIONAL_JUMP` [`00bedb4c`](#insn-00bedb4c) → [`00bedac8`](#insn-00bedac8)
  - `FALL_THROUGH` [`00bedb4c`](#insn-00bedb4c) → [`00bedb50`](#insn-00bedb50)
- ブロック [`00bedb50`](#insn-00bedb50) 範囲 `[['00bedb50', '00bedb6f']]`
  - `CONDITIONAL_JUMP` [`00bedb6c`](#insn-00bedb6c) → [`00bedacc`](#insn-00bedacc)
  - `FALL_THROUGH` [`00bedb6c`](#insn-00bedb6c) → [`00bedb70`](#insn-00bedb70)
- ブロック [`00bedb70`](#insn-00bedb70) 範囲 `[['00bedb70', '00bedb87']]`
  - `CONDITIONAL_JUMP` [`00bedb84`](#insn-00bedb84) → [`00bedacc`](#insn-00bedacc)
  - `FALL_THROUGH` [`00bedb84`](#insn-00bedb84) → [`00bedb88`](#insn-00bedb88)
- ブロック [`00bedb88`](#insn-00bedb88) 範囲 `[['00bedb88', '00bedb97']]`
  - `CONDITIONAL_JUMP` [`00bedb94`](#insn-00bedb94) → [`00bedbb0`](#insn-00bedbb0)
  - `FALL_THROUGH` [`00bedb94`](#insn-00bedb94) → [`00bedb98`](#insn-00bedb98)
- ブロック [`00bedb98`](#insn-00bedb98) 範囲 `[['00bedb98', '00bedbaf']]`
  - `CONDITIONAL_JUMP` [`00bedbac`](#insn-00bedbac) → [`00bedb88`](#insn-00bedb88)
  - `FALL_THROUGH` [`00bedbac`](#insn-00bedbac) → [`00bedbb0`](#insn-00bedbb0)
- ブロック [`00bedbb0`](#insn-00bedbb0) 範囲 `[['00bedbb0', '00bedbb7']]`
  - `UNCONDITIONAL_JUMP` [`00bedbb4`](#insn-00bedbb4) → [`00bedacc`](#insn-00bedacc)

## 命令位置別の参照

- [`00bed8c4`](#insn-00bed8c4) → [`00bedac0`](#insn-00bedac0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bed8d4`](#insn-00bed8d4) → [`00bed9b4`](#insn-00bed9b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bed8e0`](#insn-00bed8e0) → [`00bed8f4`](#insn-00bed8f4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bed8f0`](#insn-00bed8f0) → [`00bed9b4`](#insn-00bed9b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bed8f8`](#insn-00bed8f8) → [`00bed8e8`](#insn-00bed8e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bed914`](#insn-00bed914) → [`00bed938`](#insn-00bed938) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bed934`](#insn-00bed934) → [`00bed93c`](#insn-00bed93c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bed948`](#insn-00bed948) → [`00bed974`](#insn-00bed974) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bed94c`](#insn-00bed94c) → [`00bed8e8`](#insn-00bed8e8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bed970`](#insn-00bed970) → [`00bed8e4`](#insn-00bed8e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bed980`](#insn-00bed980) → [`00bed8e4`](#insn-00bed8e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bed99c`](#insn-00bed99c) → [`00bed950`](#insn-00bed950) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bed9ac`](#insn-00bed9ac) → [`00bed974`](#insn-00bed974) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bed9b0`](#insn-00bed9b0) → [`00bed8e4`](#insn-00bed8e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bed9bc`](#insn-00bed9bc) → [`00bedab4`](#insn-00bedab4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bed9d4`](#insn-00bed9d4) → [`00bed9e8`](#insn-00bed9e8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bed9e4`](#insn-00bed9e4) → [`00bedab0`](#insn-00bedab0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bed9f4`](#insn-00bed9f4) → [`00bed9dc`](#insn-00bed9dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beda04`](#insn-00beda04) → [`00bed9dc`](#insn-00bed9dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beda10`](#insn-00beda10) → [`00beda28`](#insn-00beda28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beda20`](#insn-00beda20) → [`00bed9dc`](#insn-00bed9dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beda24`](#insn-00beda24) → [`00beda44`](#insn-00beda44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beda40`](#insn-00beda40) → [`00bed9dc`](#insn-00bed9dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beda48`](#insn-00beda48) → [`00beda70`](#insn-00beda70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beda6c`](#insn-00beda6c) → [`00bed9d8`](#insn-00bed9d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beda7c`](#insn-00beda7c) → [`00bed9d8`](#insn-00bed9d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beda98`](#insn-00beda98) → [`00beda4c`](#insn-00beda4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedaa8`](#insn-00bedaa8) → [`00beda70`](#insn-00beda70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedaac`](#insn-00bedaac) → [`00bed9d8`](#insn-00bed9d8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedab8`](#insn-00bedab8) → [`00bedad8`](#insn-00bedad8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedad4`](#insn-00bedad4) → [`00bedabc`](#insn-00bedabc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedaec`](#insn-00bedaec) → [`00bedb18`](#insn-00bedb18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedb14`](#insn-00bedb14) → [`00bedb44`](#insn-00bedb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedb34`](#insn-00bedb34) → [`00bedaf0`](#insn-00bedaf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedb40`](#insn-00bedb40) → [`00bedb08`](#insn-00bedb08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedb4c`](#insn-00bedb4c) → [`00bedac8`](#insn-00bedac8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedb6c`](#insn-00bedb6c) → [`00bedacc`](#insn-00bedacc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedb84`](#insn-00bedb84) → [`00bedacc`](#insn-00bedacc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedb94`](#insn-00bedb94) → [`00bedbb0`](#insn-00bedbb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedbac`](#insn-00bedbac) → [`00bedb88`](#insn-00bedb88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedbb4`](#insn-00bedbb4) → [`00bedacc`](#insn-00bedacc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bed8c4`](#insn-00bed8c4)

~~~json
{
  "source": "00bed8c4",
  "target": "00bedac0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bed8d4`](#insn-00bed8d4)

~~~json
{
  "source": "00bed8d4",
  "target": "00bed9b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bed8e0`](#insn-00bed8e0)

~~~json
{
  "source": "00bed8e0",
  "target": "00bed8f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bed8f0`](#insn-00bed8f0)

~~~json
{
  "source": "00bed8f0",
  "target": "00bed9b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bed8f8`](#insn-00bed8f8)

~~~json
{
  "source": "00bed8f8",
  "target": "00bed8e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bed914`](#insn-00bed914)

~~~json
{
  "source": "00bed914",
  "target": "00bed938",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bed934`](#insn-00bed934)

~~~json
{
  "source": "00bed934",
  "target": "00bed93c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bed948`](#insn-00bed948)

~~~json
{
  "source": "00bed948",
  "target": "00bed974",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bed94c`](#insn-00bed94c)

~~~json
{
  "source": "00bed94c",
  "target": "00bed8e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bed970`](#insn-00bed970)

~~~json
{
  "source": "00bed970",
  "target": "00bed8e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bed980`](#insn-00bed980)

~~~json
{
  "source": "00bed980",
  "target": "00bed8e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bed99c`](#insn-00bed99c)

~~~json
{
  "source": "00bed99c",
  "target": "00bed950",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bed9ac`](#insn-00bed9ac)

~~~json
{
  "source": "00bed9ac",
  "target": "00bed974",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bed9b0`](#insn-00bed9b0)

~~~json
{
  "source": "00bed9b0",
  "target": "00bed8e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bed9bc`](#insn-00bed9bc)

~~~json
{
  "source": "00bed9bc",
  "target": "00bedab4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bed9d4`](#insn-00bed9d4)

~~~json
{
  "source": "00bed9d4",
  "target": "00bed9e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bed9e4`](#insn-00bed9e4)

~~~json
{
  "source": "00bed9e4",
  "target": "00bedab0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bed9f4`](#insn-00bed9f4)

~~~json
{
  "source": "00bed9f4",
  "target": "00bed9dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beda04`](#insn-00beda04)

~~~json
{
  "source": "00beda04",
  "target": "00bed9dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beda10`](#insn-00beda10)

~~~json
{
  "source": "00beda10",
  "target": "00beda28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beda20`](#insn-00beda20)

~~~json
{
  "source": "00beda20",
  "target": "00bed9dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beda24`](#insn-00beda24)

~~~json
{
  "source": "00beda24",
  "target": "00beda44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beda40`](#insn-00beda40)

~~~json
{
  "source": "00beda40",
  "target": "00bed9dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beda48`](#insn-00beda48)

~~~json
{
  "source": "00beda48",
  "target": "00beda70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beda6c`](#insn-00beda6c)

~~~json
{
  "source": "00beda6c",
  "target": "00bed9d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beda7c`](#insn-00beda7c)

~~~json
{
  "source": "00beda7c",
  "target": "00bed9d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beda98`](#insn-00beda98)

~~~json
{
  "source": "00beda98",
  "target": "00beda4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedaa8`](#insn-00bedaa8)

~~~json
{
  "source": "00bedaa8",
  "target": "00beda70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedaac`](#insn-00bedaac)

~~~json
{
  "source": "00bedaac",
  "target": "00bed9d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedab8`](#insn-00bedab8)

~~~json
{
  "source": "00bedab8",
  "target": "00bedad8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedad4`](#insn-00bedad4)

~~~json
{
  "source": "00bedad4",
  "target": "00bedabc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedaec`](#insn-00bedaec)

~~~json
{
  "source": "00bedaec",
  "target": "00bedb18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedb14`](#insn-00bedb14)

~~~json
{
  "source": "00bedb14",
  "target": "00bedb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedb34`](#insn-00bedb34)

~~~json
{
  "source": "00bedb34",
  "target": "00bedaf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedb40`](#insn-00bedb40)

~~~json
{
  "source": "00bedb40",
  "target": "00bedb08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedb4c`](#insn-00bedb4c)

~~~json
{
  "source": "00bedb4c",
  "target": "00bedac8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedb6c`](#insn-00bedb6c)

~~~json
{
  "source": "00bedb6c",
  "target": "00bedacc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedb84`](#insn-00bedb84)

~~~json
{
  "source": "00bedb84",
  "target": "00bedacc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedb94`](#insn-00bedb94)

~~~json
{
  "source": "00bedb94",
  "target": "00bedbb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedbac`](#insn-00bedbac)

~~~json
{
  "source": "00bedbac",
  "target": "00bedb88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedbb4`](#insn-00bedbb4)

~~~json
{
  "source": "00bedbb4",
  "target": "00bedacc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
