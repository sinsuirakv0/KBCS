# 00bee1ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 要確認
  - [v16.0.2 → v16.0.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/review-0006.md#review-1c047e47f18eca78413ea55c2269f470)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bee1ec",
  "name": "FUN_00bee1ec",
  "size": 764,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "14114138c4b0830956b1c148ba7f7e21b0f76a8495053972f9f7af57fd669b08",
  "source_text_sha256": "14114138c4b0830956b1c148ba7f7e21b0f76a8495053972f9f7af57fd669b08",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bee1ec",
        "00bee4e7"
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

- [00be7370](../00be7/00be7370.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6830 bytes

~~~c

ulong * FUN_00bee1ec(ulong *param_1,ulong *param_2,ulong *param_3)

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
          if ((long)uVar5 < lVar6) {
            uVar16 = *puVar10;
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
          puVar10 = param_1 + uVar13;
          if (uVar12 <= uVar14) {
            do {
              while( true ) {
                puVar7 = puVar11;
                *puVar10 = uVar14;
                if ((long)uVar8 < (long)uVar5) goto LAB_00bee214;
                uVar3 = uVar5 << 1 | 1;
                uVar5 = uVar5 * 2 + 2;
                puVar4 = param_1 + uVar3;
                puVar10 = puVar7;
                if ((long)uVar5 < lVar6) break;
                uVar14 = *puVar4;
                puVar11 = puVar4;
                uVar5 = uVar3;
                if (uVar14 < uVar12) goto LAB_00bee214;
              }
              uVar17 = *puVar4;
              uVar16 = puVar4[1];
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
LAB_00bee214:
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
                    /* catch() { ... } // from try @ 00bee16c with catch @ 00bee330 */
          *param_1 = uVar13;
          if (1 < lVar6) {
            uVar8 = *puVar11;
                    /* catch() { ... } // from try @ 00bee138 with catch @ 00bee340 */
            if ((long)param_2 - (long)param_1 == 0x10) {
              uVar5 = 1;
                    /* catch() { ... } // from try @ 00bee178 with catch @ 00bee350 */
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
            puVar4 = param_1;
            if (uVar13 <= uVar8) {
              do {
                while( true ) {
                  puVar15 = puVar10;
                  *puVar4 = uVar8;
                  if ((long)(lVar6 - 2U >> 1) < (long)uVar5) goto LAB_00bee308;
                  uVar12 = uVar5 << 1 | 1;
                  uVar5 = uVar5 * 2 + 2;
                  puVar1 = param_1 + uVar12;
                  puVar4 = puVar15;
                  if ((long)uVar5 < lVar6) break;
                  uVar8 = *puVar1;
                  uVar5 = uVar12;
                  puVar10 = puVar1;
                  if (uVar8 < uVar13) goto LAB_00bee308;
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
LAB_00bee308:
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
        do {
                    /* try { // try from 00bee44c to 00cee597 has its CatchHandler @ 00bee44c
                       catch() { ... } // from try @ 00bee44c with catch @ 00bee44c
                       catch() { ... } // from try @ 00bee5a4 with catch @ 00bee44c */
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
            }
          }
        }
        bVar2 = 2 < lVar6;
        lVar6 = lVar6 + -1;
      } while (bVar2);
    }
  }
  return param_3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bee1ec"></a> `00bee1ec` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bee1f0"></a> `00bee1f0` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-00bee1f4"></a> `00bee1f4` | `e0 0f 00 54` | b.eq 0x00bee3f0 | `CONDITIONAL_JUMP`
<a id="insn-00bee1f8"></a> `00bee1f8` | `29 00 00 cb` | sub x9,x1,x0 | `FALL_THROUGH`
<a id="insn-00bee1fc"></a> `00bee1fc` | `28 fd 43 93` | asr x8,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00bee200"></a> `00bee200` | `0a 09 00 f1` | subs x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bee204"></a> `00bee204` | `0b 07 00 54` | b.lt 0x00bee2e4 | `CONDITIONAL_JUMP`
<a id="insn-00bee208"></a> `00bee208` | `4b fd 41 d3` | lsr x11,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bee20c"></a> `00bee20c` | `ec 03 0b aa` | mov x12,x11 | `FALL_THROUGH`
<a id="insn-00bee210"></a> `00bee210` | `05 00 00 14` | b 0x00bee224 | `UNCONDITIONAL_JUMP`
<a id="insn-00bee214"></a> `00bee214` | `0f 02 00 f9` | str x15,[x16] | `FALL_THROUGH`
<a id="insn-00bee218"></a> `00bee218` | `9f 01 00 f1` | cmp x12,#0x0 | `FALL_THROUGH`
<a id="insn-00bee21c"></a> `00bee21c` | `8c 05 00 d1` | sub x12,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00bee220"></a> `00bee220` | `2d 06 00 54` | b.le 0x00bee2e4 | `CONDITIONAL_JUMP`
<a id="insn-00bee224"></a> `00bee224` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-00bee228"></a> `00bee228` | `8b ff ff 54` | b.lt 0x00bee218 | `CONDITIONAL_JUMP`
<a id="insn-00bee22c"></a> `00bee22c` | `2e 00 80 52` | mov w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bee230"></a> `00bee230` | `8d f1 7f d3` | ubfiz x13,x12,#0x1,#0x3d | `FALL_THROUGH`
<a id="insn-00bee234"></a> `00bee234` | `8e f1 7f b3` | bfm x14,x12,#0x3f,#0x3c | `FALL_THROUGH`
<a id="insn-00bee238"></a> `00bee238` | `af 09 00 91` | add x15,x13,#0x2 | `FALL_THROUGH`
<a id="insn-00bee23c"></a> `00bee23c` | `0d 0c 0e 8b` | add x13,x0,x14, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bee240"></a> `00bee240` | `ff 01 08 eb` | cmp x15,x8 | `FALL_THROUGH`
<a id="insn-00bee244"></a> `00bee244` | `2a 01 00 54` | b.ge 0x00bee268 | `CONDITIONAL_JUMP`
<a id="insn-00bee248"></a> `00bee248` | `f0 03 0d aa` | mov x16,x13 | `FALL_THROUGH`
<a id="insn-00bee24c"></a> `00bee24c` | `b1 01 40 f9` | ldr x17,[x13] | `FALL_THROUGH`
<a id="insn-00bee250"></a> `00bee250` | `03 8e 40 f8` | ldr x3,[x16, #0x8]! | `FALL_THROUGH`
<a id="insn-00bee254"></a> `00bee254` | `3f 02 03 eb` | cmp x17,x3 | `FALL_THROUGH`
<a id="insn-00bee258"></a> `00bee258` | `31 82 83 9a` | csel x17,x17,x3,hi | `FALL_THROUGH`
<a id="insn-00bee25c"></a> `00bee25c` | `0d 32 8d 9a` | csel x13,x16,x13,cc | `FALL_THROUGH`
<a id="insn-00bee260"></a> `00bee260` | `ee 31 8e 9a` | csel x14,x15,x14,cc | `FALL_THROUGH`
<a id="insn-00bee264"></a> `00bee264` | `02 00 00 14` | b 0x00bee26c | `UNCONDITIONAL_JUMP`
<a id="insn-00bee268"></a> `00bee268` | `b1 01 40 f9` | ldr x17,[x13] | `FALL_THROUGH`
<a id="insn-00bee26c"></a> `00bee26c` | `10 0c 0c 8b` | add x16,x0,x12, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bee270"></a> `00bee270` | `0f 02 40 f9` | ldr x15,[x16] | `FALL_THROUGH`
<a id="insn-00bee274"></a> `00bee274` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bee278"></a> `00bee278` | `62 01 00 54` | b.cs 0x00bee2a4 | `CONDITIONAL_JUMP`
<a id="insn-00bee27c"></a> `00bee27c` | `e7 ff ff 17` | b 0x00bee218 | `UNCONDITIONAL_JUMP`
<a id="insn-00bee280"></a> `00bee280` | `e4 03 0d aa` | mov x4,x13 | `FALL_THROUGH`
<a id="insn-00bee284"></a> `00bee284` | `b1 01 40 f9` | ldr x17,[x13] | `FALL_THROUGH`
<a id="insn-00bee288"></a> `00bee288` | `85 8c 40 f8` | ldr x5,[x4, #0x8]! | `FALL_THROUGH`
<a id="insn-00bee28c"></a> `00bee28c` | `3f 02 05 eb` | cmp x17,x5 | `FALL_THROUGH`
<a id="insn-00bee290"></a> `00bee290` | `31 82 85 9a` | csel x17,x17,x5,hi | `FALL_THROUGH`
<a id="insn-00bee294"></a> `00bee294` | `8d 30 8d 9a` | csel x13,x4,x13,cc | `FALL_THROUGH`
<a id="insn-00bee298"></a> `00bee298` | `ce 31 83 9a` | csel x14,x14,x3,cc | `FALL_THROUGH`
<a id="insn-00bee29c"></a> `00bee29c` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bee2a0"></a> `00bee2a0` | `a3 fb ff 54` | b.cc 0x00bee214 | `CONDITIONAL_JUMP`
<a id="insn-00bee2a4"></a> `00bee2a4` | `7f 01 0e eb` | cmp x11,x14 | `FALL_THROUGH`
<a id="insn-00bee2a8"></a> `00bee2a8` | `11 02 00 f9` | str x17,[x16] | `FALL_THROUGH`
<a id="insn-00bee2ac"></a> `00bee2ac` | `f0 03 0d aa` | mov x16,x13 | `FALL_THROUGH`
<a id="insn-00bee2b0"></a> `00bee2b0` | `2b fb ff 54` | b.lt 0x00bee214 | `CONDITIONAL_JUMP`
<a id="insn-00bee2b4"></a> `00bee2b4` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bee2b8"></a> `00bee2b8` | `cd f9 7f d3` | lsl x13,x14,#0x1 | `FALL_THROUGH`
<a id="insn-00bee2bc"></a> `00bee2bc` | `c3 f9 7f b3` | bfm x3,x14,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bee2c0"></a> `00bee2c0` | `ae 09 00 91` | add x14,x13,#0x2 | `FALL_THROUGH`
<a id="insn-00bee2c4"></a> `00bee2c4` | `0d 0c 03 8b` | add x13,x0,x3, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bee2c8"></a> `00bee2c8` | `df 01 08 eb` | cmp x14,x8 | `FALL_THROUGH`
<a id="insn-00bee2cc"></a> `00bee2cc` | `ab fd ff 54` | b.lt 0x00bee280 | `CONDITIONAL_JUMP`
<a id="insn-00bee2d0"></a> `00bee2d0` | `b1 01 40 f9` | ldr x17,[x13] | `FALL_THROUGH`
<a id="insn-00bee2d4"></a> `00bee2d4` | `ee 03 03 aa` | mov x14,x3 | `FALL_THROUGH`
<a id="insn-00bee2d8"></a> `00bee2d8` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bee2dc"></a> `00bee2dc` | `42 fe ff 54` | b.cs 0x00bee2a4 | `CONDITIONAL_JUMP`
<a id="insn-00bee2e0"></a> `00bee2e0` | `cd ff ff 17` | b 0x00bee214 | `UNCONDITIONAL_JUMP`
<a id="insn-00bee2e4"></a> `00bee2e4` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-00bee2e8"></a> `00bee2e8` | `e3 03 01 aa` | mov x3,x1 | `FALL_THROUGH`
<a id="insn-00bee2ec"></a> `00bee2ec` | `c0 07 00 54` | b.eq 0x00bee3e4 | `CONDITIONAL_JUMP`
<a id="insn-00bee2f0"></a> `00bee2f0` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bee2f4"></a> `00bee2f4` | `0b 20 00 91` | add x11,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bee2f8"></a> `00bee2f8` | `0c 40 00 91` | add x12,x0,#0x10 | `FALL_THROUGH`
<a id="insn-00bee2fc"></a> `00bee2fc` | `2d 00 80 52` | mov w13,#0x1 | `FALL_THROUGH`
<a id="insn-00bee300"></a> `00bee300` | `ee 03 01 aa` | mov x14,x1 | `FALL_THROUGH`
<a id="insn-00bee304"></a> `00bee304` | `05 00 00 14` | b 0x00bee318 | `UNCONDITIONAL_JUMP`
<a id="insn-00bee308"></a> `00bee308` | `6f 00 00 f9` | str x15,[x3] | `FALL_THROUGH`
<a id="insn-00bee30c"></a> `00bee30c` | `ce 21 00 91` | add x14,x14,#0x8 | `FALL_THROUGH`
<a id="insn-00bee310"></a> `00bee310` | `df 01 02 eb` | cmp x14,x2 | `FALL_THROUGH`
<a id="insn-00bee314"></a> `00bee314` | `60 06 00 54` | b.eq 0x00bee3e0 | `CONDITIONAL_JUMP`
<a id="insn-00bee318"></a> `00bee318` | `cf 01 40 f9` | ldr x15,[x14] | `FALL_THROUGH`
<a id="insn-00bee31c"></a> `00bee31c` | `10 00 40 f9` | ldr x16,[x0] | `FALL_THROUGH`
<a id="insn-00bee320"></a> `00bee320` | `ff 01 10 eb` | cmp x15,x16 | `FALL_THROUGH`
<a id="insn-00bee324"></a> `00bee324` | `42 ff ff 54` | b.cs 0x00bee30c | `CONDITIONAL_JUMP`
<a id="insn-00bee328"></a> `00bee328` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bee32c"></a> `00bee32c` | `d0 01 00 f9` | str x16,[x14] | `FALL_THROUGH`
<a id="insn-00bee330"></a> `00bee330` | `0f 00 00 f9` | str x15,[x0] | `FALL_THROUGH`
<a id="insn-00bee334"></a> `00bee334` | `cb fe ff 54` | b.lt 0x00bee30c | `CONDITIONAL_JUMP`
<a id="insn-00bee338"></a> `00bee338` | `71 01 40 f9` | ldr x17,[x11] | `FALL_THROUGH`
<a id="insn-00bee33c"></a> `00bee33c` | `3f 41 00 f1` | cmp x9,#0x10 | `FALL_THROUGH`
<a id="insn-00bee340"></a> `00bee340` | `c1 00 00 54` | b.ne 0x00bee358 | `CONDITIONAL_JUMP`
<a id="insn-00bee344"></a> `00bee344` | `f0 03 0b aa` | mov x16,x11 | `FALL_THROUGH`
<a id="insn-00bee348"></a> `00bee348` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-00bee34c"></a> `00bee34c` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bee350"></a> `00bee350` | `e3 fd ff 54` | b.cc 0x00bee30c | `CONDITIONAL_JUMP`
<a id="insn-00bee354"></a> `00bee354` | `08 00 00 14` | b 0x00bee374 | `UNCONDITIONAL_JUMP`
<a id="insn-00bee358"></a> `00bee358` | `90 01 40 f9` | ldr x16,[x12] | `FALL_THROUGH`
<a id="insn-00bee35c"></a> `00bee35c` | `3f 02 10 eb` | cmp x17,x16 | `FALL_THROUGH`
<a id="insn-00bee360"></a> `00bee360` | `31 82 90 9a` | csel x17,x17,x16,hi | `FALL_THROUGH`
<a id="insn-00bee364"></a> `00bee364` | `90 31 8b 9a` | csel x16,x12,x11,cc | `FALL_THROUGH`
<a id="insn-00bee368"></a> `00bee368` | `a4 25 8d 9a` | cinc x4,x13,cc | `FALL_THROUGH`
<a id="insn-00bee36c"></a> `00bee36c` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bee370"></a> `00bee370` | `e3 fc ff 54` | b.cc 0x00bee30c | `CONDITIONAL_JUMP`
<a id="insn-00bee374"></a> `00bee374` | `e3 03 00 aa` | mov x3,x0 | `FALL_THROUGH`
<a id="insn-00bee378"></a> `00bee378` | `0a 00 00 14` | b 0x00bee3a0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bee37c"></a> `00bee37c` | `e6 03 10 aa` | mov x6,x16 | `FALL_THROUGH`
<a id="insn-00bee380"></a> `00bee380` | `11 02 40 f9` | ldr x17,[x16] | `FALL_THROUGH`
<a id="insn-00bee384"></a> `00bee384` | `c7 8c 40 f8` | ldr x7,[x6, #0x8]! | `FALL_THROUGH`
<a id="insn-00bee388"></a> `00bee388` | `3f 02 07 eb` | cmp x17,x7 | `FALL_THROUGH`
<a id="insn-00bee38c"></a> `00bee38c` | `31 82 87 9a` | csel x17,x17,x7,hi | `FALL_THROUGH`
<a id="insn-00bee390"></a> `00bee390` | `d0 30 90 9a` | csel x16,x6,x16,cc | `FALL_THROUGH`
<a id="insn-00bee394"></a> `00bee394` | `84 30 85 9a` | csel x4,x4,x5,cc | `FALL_THROUGH`
<a id="insn-00bee398"></a> `00bee398` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bee39c"></a> `00bee39c` | `63 fb ff 54` | b.cc 0x00bee308 | `CONDITIONAL_JUMP`
<a id="insn-00bee3a0"></a> `00bee3a0` | `5f 01 04 eb` | cmp x10,x4 | `FALL_THROUGH`
<a id="insn-00bee3a4"></a> `00bee3a4` | `71 00 00 f9` | str x17,[x3] | `FALL_THROUGH`
<a id="insn-00bee3a8"></a> `00bee3a8` | `e3 03 10 aa` | mov x3,x16 | `FALL_THROUGH`
<a id="insn-00bee3ac"></a> `00bee3ac` | `eb fa ff 54` | b.lt 0x00bee308 | `CONDITIONAL_JUMP`
<a id="insn-00bee3b0"></a> `00bee3b0` | `25 00 80 52` | mov w5,#0x1 | `FALL_THROUGH`
<a id="insn-00bee3b4"></a> `00bee3b4` | `90 f8 7f d3` | lsl x16,x4,#0x1 | `FALL_THROUGH`
<a id="insn-00bee3b8"></a> `00bee3b8` | `85 f8 7f b3` | bfm x5,x4,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bee3bc"></a> `00bee3bc` | `04 0a 00 91` | add x4,x16,#0x2 | `FALL_THROUGH`
<a id="insn-00bee3c0"></a> `00bee3c0` | `10 0c 05 8b` | add x16,x0,x5, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bee3c4"></a> `00bee3c4` | `9f 00 08 eb` | cmp x4,x8 | `FALL_THROUGH`
<a id="insn-00bee3c8"></a> `00bee3c8` | `ab fd ff 54` | b.lt 0x00bee37c | `CONDITIONAL_JUMP`
<a id="insn-00bee3cc"></a> `00bee3cc` | `11 02 40 f9` | ldr x17,[x16] | `FALL_THROUGH`
<a id="insn-00bee3d0"></a> `00bee3d0` | `e4 03 05 aa` | mov x4,x5 | `FALL_THROUGH`
<a id="insn-00bee3d4"></a> `00bee3d4` | `3f 02 0f eb` | cmp x17,x15 | `FALL_THROUGH`
<a id="insn-00bee3d8"></a> `00bee3d8` | `42 fe ff 54` | b.cs 0x00bee3a0 | `CONDITIONAL_JUMP`
<a id="insn-00bee3dc"></a> `00bee3dc` | `cb ff ff 17` | b 0x00bee308 | `UNCONDITIONAL_JUMP`
<a id="insn-00bee3e0"></a> `00bee3e0` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bee3e4"></a> `00bee3e4` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bee3e8"></a> `00bee3e8` | `0a 01 00 54` | b.ge 0x00bee408 | `CONDITIONAL_JUMP`
<a id="insn-00bee3ec"></a> `00bee3ec` | `e2 03 03 aa` | mov x2,x3 | `FALL_THROUGH`
<a id="insn-00bee3f0"></a> `00bee3f0` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bee3f4"></a> `00bee3f4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bee3f8"></a> `00bee3f8` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bee3fc"></a> `00bee3fc` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bee400"></a> `00bee400` | `08 05 00 d1` | sub x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bee404"></a> `00bee404` | `4d ff ff 54` | b.le 0x00bee3ec | `CONDITIONAL_JUMP`
<a id="insn-00bee408"></a> `00bee408` | `09 09 00 d1` | sub x9,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bee40c"></a> `00bee40c` | `0a 00 40 f9` | ldr x10,[x0] | `FALL_THROUGH`
<a id="insn-00bee410"></a> `00bee410` | `ed 03 1f aa` | mov x13,xzr | `FALL_THROUGH`
<a id="insn-00bee414"></a> `00bee414` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bee418"></a> `00bee418` | `ec 03 00 aa` | mov x12,x0 | `FALL_THROUGH`
<a id="insn-00bee41c"></a> `00bee41c` | `0b 00 00 14` | b 0x00bee448 | `UNCONDITIONAL_JUMP`
<a id="insn-00bee420"></a> `00bee420` | `0d 0e 41 f8` | ldr x13,[x16, #0x10]! | `FALL_THROUGH`
<a id="insn-00bee424"></a> `00bee424` | `0f 82 5f f8` | ldur x15,[x16, #-0x8] | `FALL_THROUGH`
<a id="insn-00bee428"></a> `00bee428` | `ff 01 0d eb` | cmp x15,x13 | `FALL_THROUGH`
<a id="insn-00bee42c"></a> `00bee42c` | `ef 81 8d 9a` | csel x15,x15,x13,hi | `FALL_THROUGH`
<a id="insn-00bee430"></a> `00bee430` | `09 32 89 9a` | csel x9,x16,x9,cc | `FALL_THROUGH`
<a id="insn-00bee434"></a> `00bee434` | `2d 32 8e 9a` | csel x13,x17,x14,cc | `FALL_THROUGH`
<a id="insn-00bee438"></a> `00bee438` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00bee43c"></a> `00bee43c` | `8f 01 00 f9` | str x15,[x12] | `FALL_THROUGH`
<a id="insn-00bee440"></a> `00bee440` | `ec 03 09 aa` | mov x12,x9 | `FALL_THROUGH`
<a id="insn-00bee444"></a> `00bee444` | `8c 01 00 54` | b.gt 0x00bee474 | `CONDITIONAL_JUMP`
<a id="insn-00bee448"></a> `00bee448` | `a9 f9 7f d3` | lsl x9,x13,#0x1 | `FALL_THROUGH`
<a id="insn-00bee44c"></a> `00bee44c` | `90 0d 0d 8b` | add x16,x12,x13, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bee450"></a> `00bee450` | `2e 00 80 52` | mov w14,#0x1 | `FALL_THROUGH`
<a id="insn-00bee454"></a> `00bee454` | `ae f9 7f b3` | bfm x14,x13,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bee458"></a> `00bee458` | `31 09 00 91` | add x17,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bee45c"></a> `00bee45c` | `09 22 00 91` | add x9,x16,#0x8 | `FALL_THROUGH`
<a id="insn-00bee460"></a> `00bee460` | `3f 02 08 eb` | cmp x17,x8 | `FALL_THROUGH`
<a id="insn-00bee464"></a> `00bee464` | `eb fd ff 54` | b.lt 0x00bee420 | `CONDITIONAL_JUMP`
<a id="insn-00bee468"></a> `00bee468` | `2f 01 40 f9` | ldr x15,[x9] | `FALL_THROUGH`
<a id="insn-00bee46c"></a> `00bee46c` | `ed 03 0e aa` | mov x13,x14 | `FALL_THROUGH`
<a id="insn-00bee470"></a> `00bee470` | `f2 ff ff 17` | b 0x00bee438 | `UNCONDITIONAL_JUMP`
<a id="insn-00bee474"></a> `00bee474` | `21 20 00 d1` | sub x1,x1,#0x8 | `FALL_THROUGH`
<a id="insn-00bee478"></a> `00bee478` | `3f 01 01 eb` | cmp x9,x1 | `FALL_THROUGH`
<a id="insn-00bee47c"></a> `00bee47c` | `e0 fb ff 54` | b.eq 0x00bee3f8 | `CONDITIONAL_JUMP`
<a id="insn-00bee480"></a> `00bee480` | `2b 01 00 cb` | sub x11,x9,x0 | `FALL_THROUGH`
<a id="insn-00bee484"></a> `00bee484` | `2c 00 40 f9` | ldr x12,[x1] | `FALL_THROUGH`
<a id="insn-00bee488"></a> `00bee488` | `6b 21 00 91` | add x11,x11,#0x8 | `FALL_THROUGH`
<a id="insn-00bee48c"></a> `00bee48c` | `6b fd 43 93` | asr x11,x11,#0x3 | `FALL_THROUGH`
<a id="insn-00bee490"></a> `00bee490` | `2c 01 00 f9` | str x12,[x9] | `FALL_THROUGH`
<a id="insn-00bee494"></a> `00bee494` | `2a 00 00 f9` | str x10,[x1] | `FALL_THROUGH`
<a id="insn-00bee498"></a> `00bee498` | `6b 09 00 f1` | subs x11,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00bee49c"></a> `00bee49c` | `0b fb ff 54` | b.lt 0x00bee3fc | `CONDITIONAL_JUMP`
<a id="insn-00bee4a0"></a> `00bee4a0` | `6a fd 41 d3` | lsr x10,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00bee4a4"></a> `00bee4a4` | `2b 01 40 f9` | ldr x11,[x9] | `FALL_THROUGH`
<a id="insn-00bee4a8"></a> `00bee4a8` | `0c 0c 0a 8b` | add x12,x0,x10, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bee4ac"></a> `00bee4ac` | `8d 01 40 f9` | ldr x13,[x12] | `FALL_THROUGH`
<a id="insn-00bee4b0"></a> `00bee4b0` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00bee4b4"></a> `00bee4b4` | `42 fa ff 54` | b.cs 0x00bee3fc | `CONDITIONAL_JUMP`
<a id="insn-00bee4b8"></a> `00bee4b8` | `ee 03 09 aa` | mov x14,x9 | `FALL_THROUGH`
<a id="insn-00bee4bc"></a> `00bee4bc` | `e9 03 0c aa` | mov x9,x12 | `FALL_THROUGH`
<a id="insn-00bee4c0"></a> `00bee4c0` | `cd 01 00 f9` | str x13,[x14] | `FALL_THROUGH`
<a id="insn-00bee4c4"></a> `00bee4c4` | `ea 00 00 b4` | cbz x10,0x00bee4e0 | `CONDITIONAL_JUMP`
<a id="insn-00bee4c8"></a> `00bee4c8` | `4a 05 00 d1` | sub x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bee4cc"></a> `00bee4cc` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bee4d0"></a> `00bee4d0` | `0c 0c 0a 8b` | add x12,x0,x10, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bee4d4"></a> `00bee4d4` | `8d 01 40 f9` | ldr x13,[x12] | `FALL_THROUGH`
<a id="insn-00bee4d8"></a> `00bee4d8` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00bee4dc"></a> `00bee4dc` | `e3 fe ff 54` | b.cc 0x00bee4b8 | `CONDITIONAL_JUMP`
<a id="insn-00bee4e0"></a> `00bee4e0` | `2b 01 00 f9` | str x11,[x9] | `FALL_THROUGH`
<a id="insn-00bee4e4"></a> `00bee4e4` | `c6 ff ff 17` | b 0x00bee3fc | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bee1ec`](#insn-00bee1ec) 範囲 `[['00bee1ec', '00bee1f7']]`
  - `CONDITIONAL_JUMP` [`00bee1f4`](#insn-00bee1f4) → [`00bee3f0`](#insn-00bee3f0)
  - `FALL_THROUGH` [`00bee1f4`](#insn-00bee1f4) → [`00bee1f8`](#insn-00bee1f8)
- ブロック [`00bee1f8`](#insn-00bee1f8) 範囲 `[['00bee1f8', '00bee207']]`
  - `CONDITIONAL_JUMP` [`00bee204`](#insn-00bee204) → [`00bee2e4`](#insn-00bee2e4)
  - `FALL_THROUGH` [`00bee204`](#insn-00bee204) → [`00bee208`](#insn-00bee208)
- ブロック [`00bee208`](#insn-00bee208) 範囲 `[['00bee208', '00bee213']]`
  - `UNCONDITIONAL_JUMP` [`00bee210`](#insn-00bee210) → [`00bee224`](#insn-00bee224)
- ブロック [`00bee214`](#insn-00bee214) 範囲 `[['00bee214', '00bee217']]`
  - `FALL_THROUGH` [`00bee214`](#insn-00bee214) → [`00bee218`](#insn-00bee218)
- ブロック [`00bee218`](#insn-00bee218) 範囲 `[['00bee218', '00bee223']]`
  - `CONDITIONAL_JUMP` [`00bee220`](#insn-00bee220) → [`00bee2e4`](#insn-00bee2e4)
  - `FALL_THROUGH` [`00bee220`](#insn-00bee220) → [`00bee224`](#insn-00bee224)
- ブロック [`00bee224`](#insn-00bee224) 範囲 `[['00bee224', '00bee22b']]`
  - `CONDITIONAL_JUMP` [`00bee228`](#insn-00bee228) → [`00bee218`](#insn-00bee218)
  - `FALL_THROUGH` [`00bee228`](#insn-00bee228) → [`00bee22c`](#insn-00bee22c)
- ブロック [`00bee22c`](#insn-00bee22c) 範囲 `[['00bee22c', '00bee247']]`
  - `CONDITIONAL_JUMP` [`00bee244`](#insn-00bee244) → [`00bee268`](#insn-00bee268)
  - `FALL_THROUGH` [`00bee244`](#insn-00bee244) → [`00bee248`](#insn-00bee248)
- ブロック [`00bee248`](#insn-00bee248) 範囲 `[['00bee248', '00bee267']]`
  - `UNCONDITIONAL_JUMP` [`00bee264`](#insn-00bee264) → [`00bee26c`](#insn-00bee26c)
- ブロック [`00bee268`](#insn-00bee268) 範囲 `[['00bee268', '00bee26b']]`
  - `FALL_THROUGH` [`00bee268`](#insn-00bee268) → [`00bee26c`](#insn-00bee26c)
- ブロック [`00bee26c`](#insn-00bee26c) 範囲 `[['00bee26c', '00bee27b']]`
  - `CONDITIONAL_JUMP` [`00bee278`](#insn-00bee278) → [`00bee2a4`](#insn-00bee2a4)
  - `FALL_THROUGH` [`00bee278`](#insn-00bee278) → [`00bee27c`](#insn-00bee27c)
- ブロック [`00bee27c`](#insn-00bee27c) 範囲 `[['00bee27c', '00bee27f']]`
  - `UNCONDITIONAL_JUMP` [`00bee27c`](#insn-00bee27c) → [`00bee218`](#insn-00bee218)
- ブロック [`00bee280`](#insn-00bee280) 範囲 `[['00bee280', '00bee2a3']]`
  - `CONDITIONAL_JUMP` [`00bee2a0`](#insn-00bee2a0) → [`00bee214`](#insn-00bee214)
  - `FALL_THROUGH` [`00bee2a0`](#insn-00bee2a0) → [`00bee2a4`](#insn-00bee2a4)
- ブロック [`00bee2a4`](#insn-00bee2a4) 範囲 `[['00bee2a4', '00bee2b3']]`
  - `CONDITIONAL_JUMP` [`00bee2b0`](#insn-00bee2b0) → [`00bee214`](#insn-00bee214)
  - `FALL_THROUGH` [`00bee2b0`](#insn-00bee2b0) → [`00bee2b4`](#insn-00bee2b4)
- ブロック [`00bee2b4`](#insn-00bee2b4) 範囲 `[['00bee2b4', '00bee2cf']]`
  - `CONDITIONAL_JUMP` [`00bee2cc`](#insn-00bee2cc) → [`00bee280`](#insn-00bee280)
  - `FALL_THROUGH` [`00bee2cc`](#insn-00bee2cc) → [`00bee2d0`](#insn-00bee2d0)
- ブロック [`00bee2d0`](#insn-00bee2d0) 範囲 `[['00bee2d0', '00bee2df']]`
  - `CONDITIONAL_JUMP` [`00bee2dc`](#insn-00bee2dc) → [`00bee2a4`](#insn-00bee2a4)
  - `FALL_THROUGH` [`00bee2dc`](#insn-00bee2dc) → [`00bee2e0`](#insn-00bee2e0)
- ブロック [`00bee2e0`](#insn-00bee2e0) 範囲 `[['00bee2e0', '00bee2e3']]`
  - `UNCONDITIONAL_JUMP` [`00bee2e0`](#insn-00bee2e0) → [`00bee214`](#insn-00bee214)
- ブロック [`00bee2e4`](#insn-00bee2e4) 範囲 `[['00bee2e4', '00bee2ef']]`
  - `CONDITIONAL_JUMP` [`00bee2ec`](#insn-00bee2ec) → [`00bee3e4`](#insn-00bee3e4)
  - `FALL_THROUGH` [`00bee2ec`](#insn-00bee2ec) → [`00bee2f0`](#insn-00bee2f0)
- ブロック [`00bee2f0`](#insn-00bee2f0) 範囲 `[['00bee2f0', '00bee307']]`
  - `UNCONDITIONAL_JUMP` [`00bee304`](#insn-00bee304) → [`00bee318`](#insn-00bee318)
- ブロック [`00bee308`](#insn-00bee308) 範囲 `[['00bee308', '00bee30b']]`
  - `FALL_THROUGH` [`00bee308`](#insn-00bee308) → [`00bee30c`](#insn-00bee30c)
- ブロック [`00bee30c`](#insn-00bee30c) 範囲 `[['00bee30c', '00bee317']]`
  - `CONDITIONAL_JUMP` [`00bee314`](#insn-00bee314) → [`00bee3e0`](#insn-00bee3e0)
  - `FALL_THROUGH` [`00bee314`](#insn-00bee314) → [`00bee318`](#insn-00bee318)
- ブロック [`00bee318`](#insn-00bee318) 範囲 `[['00bee318', '00bee327']]`
  - `CONDITIONAL_JUMP` [`00bee324`](#insn-00bee324) → [`00bee30c`](#insn-00bee30c)
  - `FALL_THROUGH` [`00bee324`](#insn-00bee324) → [`00bee328`](#insn-00bee328)
- ブロック [`00bee328`](#insn-00bee328) 範囲 `[['00bee328', '00bee32f']]`
  - `FALL_THROUGH` [`00bee32c`](#insn-00bee32c) → [`00bee330`](#insn-00bee330)
- ブロック [`00bee330`](#insn-00bee330) 範囲 `[['00bee330', '00bee337']]`
  - `CONDITIONAL_JUMP` [`00bee334`](#insn-00bee334) → [`00bee30c`](#insn-00bee30c)
  - `FALL_THROUGH` [`00bee334`](#insn-00bee334) → [`00bee338`](#insn-00bee338)
- ブロック [`00bee338`](#insn-00bee338) 範囲 `[['00bee338', '00bee33f']]`
  - `FALL_THROUGH` [`00bee33c`](#insn-00bee33c) → [`00bee340`](#insn-00bee340)
- ブロック [`00bee340`](#insn-00bee340) 範囲 `[['00bee340', '00bee343']]`
  - `CONDITIONAL_JUMP` [`00bee340`](#insn-00bee340) → [`00bee358`](#insn-00bee358)
  - `FALL_THROUGH` [`00bee340`](#insn-00bee340) → [`00bee344`](#insn-00bee344)
- ブロック [`00bee344`](#insn-00bee344) 範囲 `[['00bee344', '00bee34f']]`
  - `FALL_THROUGH` [`00bee34c`](#insn-00bee34c) → [`00bee350`](#insn-00bee350)
- ブロック [`00bee350`](#insn-00bee350) 範囲 `[['00bee350', '00bee353']]`
  - `CONDITIONAL_JUMP` [`00bee350`](#insn-00bee350) → [`00bee30c`](#insn-00bee30c)
  - `FALL_THROUGH` [`00bee350`](#insn-00bee350) → [`00bee354`](#insn-00bee354)
- ブロック [`00bee354`](#insn-00bee354) 範囲 `[['00bee354', '00bee357']]`
  - `UNCONDITIONAL_JUMP` [`00bee354`](#insn-00bee354) → [`00bee374`](#insn-00bee374)
- ブロック [`00bee358`](#insn-00bee358) 範囲 `[['00bee358', '00bee373']]`
  - `CONDITIONAL_JUMP` [`00bee370`](#insn-00bee370) → [`00bee30c`](#insn-00bee30c)
  - `FALL_THROUGH` [`00bee370`](#insn-00bee370) → [`00bee374`](#insn-00bee374)
- ブロック [`00bee374`](#insn-00bee374) 範囲 `[['00bee374', '00bee37b']]`
  - `UNCONDITIONAL_JUMP` [`00bee378`](#insn-00bee378) → [`00bee3a0`](#insn-00bee3a0)
- ブロック [`00bee37c`](#insn-00bee37c) 範囲 `[['00bee37c', '00bee39f']]`
  - `CONDITIONAL_JUMP` [`00bee39c`](#insn-00bee39c) → [`00bee308`](#insn-00bee308)
  - `FALL_THROUGH` [`00bee39c`](#insn-00bee39c) → [`00bee3a0`](#insn-00bee3a0)
- ブロック [`00bee3a0`](#insn-00bee3a0) 範囲 `[['00bee3a0', '00bee3af']]`
  - `CONDITIONAL_JUMP` [`00bee3ac`](#insn-00bee3ac) → [`00bee308`](#insn-00bee308)
  - `FALL_THROUGH` [`00bee3ac`](#insn-00bee3ac) → [`00bee3b0`](#insn-00bee3b0)
- ブロック [`00bee3b0`](#insn-00bee3b0) 範囲 `[['00bee3b0', '00bee3cb']]`
  - `CONDITIONAL_JUMP` [`00bee3c8`](#insn-00bee3c8) → [`00bee37c`](#insn-00bee37c)
  - `FALL_THROUGH` [`00bee3c8`](#insn-00bee3c8) → [`00bee3cc`](#insn-00bee3cc)
- ブロック [`00bee3cc`](#insn-00bee3cc) 範囲 `[['00bee3cc', '00bee3db']]`
  - `CONDITIONAL_JUMP` [`00bee3d8`](#insn-00bee3d8) → [`00bee3a0`](#insn-00bee3a0)
  - `FALL_THROUGH` [`00bee3d8`](#insn-00bee3d8) → [`00bee3dc`](#insn-00bee3dc)
- ブロック [`00bee3dc`](#insn-00bee3dc) 範囲 `[['00bee3dc', '00bee3df']]`
  - `UNCONDITIONAL_JUMP` [`00bee3dc`](#insn-00bee3dc) → [`00bee308`](#insn-00bee308)
- ブロック [`00bee3e0`](#insn-00bee3e0) 範囲 `[['00bee3e0', '00bee3e3']]`
  - `FALL_THROUGH` [`00bee3e0`](#insn-00bee3e0) → [`00bee3e4`](#insn-00bee3e4)
- ブロック [`00bee3e4`](#insn-00bee3e4) 範囲 `[['00bee3e4', '00bee3eb']]`
  - `CONDITIONAL_JUMP` [`00bee3e8`](#insn-00bee3e8) → [`00bee408`](#insn-00bee408)
  - `FALL_THROUGH` [`00bee3e8`](#insn-00bee3e8) → [`00bee3ec`](#insn-00bee3ec)
- ブロック [`00bee3ec`](#insn-00bee3ec) 範囲 `[['00bee3ec', '00bee3ef']]`
  - `FALL_THROUGH` [`00bee3ec`](#insn-00bee3ec) → [`00bee3f0`](#insn-00bee3f0)
- ブロック [`00bee3f0`](#insn-00bee3f0) 範囲 `[['00bee3f0', '00bee3f7']]`
- ブロック [`00bee3f8`](#insn-00bee3f8) 範囲 `[['00bee3f8', '00bee3fb']]`
  - `FALL_THROUGH` [`00bee3f8`](#insn-00bee3f8) → [`00bee3fc`](#insn-00bee3fc)
- ブロック [`00bee3fc`](#insn-00bee3fc) 範囲 `[['00bee3fc', '00bee407']]`
  - `CONDITIONAL_JUMP` [`00bee404`](#insn-00bee404) → [`00bee3ec`](#insn-00bee3ec)
  - `FALL_THROUGH` [`00bee404`](#insn-00bee404) → [`00bee408`](#insn-00bee408)
- ブロック [`00bee408`](#insn-00bee408) 範囲 `[['00bee408', '00bee41f']]`
  - `UNCONDITIONAL_JUMP` [`00bee41c`](#insn-00bee41c) → [`00bee448`](#insn-00bee448)
- ブロック [`00bee420`](#insn-00bee420) 範囲 `[['00bee420', '00bee437']]`
  - `FALL_THROUGH` [`00bee434`](#insn-00bee434) → [`00bee438`](#insn-00bee438)
- ブロック [`00bee438`](#insn-00bee438) 範囲 `[['00bee438', '00bee447']]`
  - `CONDITIONAL_JUMP` [`00bee444`](#insn-00bee444) → [`00bee474`](#insn-00bee474)
  - `FALL_THROUGH` [`00bee444`](#insn-00bee444) → [`00bee448`](#insn-00bee448)
- ブロック [`00bee448`](#insn-00bee448) 範囲 `[['00bee448', '00bee44b']]`
  - `FALL_THROUGH` [`00bee448`](#insn-00bee448) → [`00bee44c`](#insn-00bee44c)
- ブロック [`00bee44c`](#insn-00bee44c) 範囲 `[['00bee44c', '00bee467']]`
  - `CONDITIONAL_JUMP` [`00bee464`](#insn-00bee464) → [`00bee420`](#insn-00bee420)
  - `FALL_THROUGH` [`00bee464`](#insn-00bee464) → [`00bee468`](#insn-00bee468)
- ブロック [`00bee468`](#insn-00bee468) 範囲 `[['00bee468', '00bee473']]`
  - `UNCONDITIONAL_JUMP` [`00bee470`](#insn-00bee470) → [`00bee438`](#insn-00bee438)
- ブロック [`00bee474`](#insn-00bee474) 範囲 `[['00bee474', '00bee47f']]`
  - `CONDITIONAL_JUMP` [`00bee47c`](#insn-00bee47c) → [`00bee3f8`](#insn-00bee3f8)
  - `FALL_THROUGH` [`00bee47c`](#insn-00bee47c) → [`00bee480`](#insn-00bee480)
- ブロック [`00bee480`](#insn-00bee480) 範囲 `[['00bee480', '00bee49f']]`
  - `CONDITIONAL_JUMP` [`00bee49c`](#insn-00bee49c) → [`00bee3fc`](#insn-00bee3fc)
  - `FALL_THROUGH` [`00bee49c`](#insn-00bee49c) → [`00bee4a0`](#insn-00bee4a0)
- ブロック [`00bee4a0`](#insn-00bee4a0) 範囲 `[['00bee4a0', '00bee4b7']]`
  - `CONDITIONAL_JUMP` [`00bee4b4`](#insn-00bee4b4) → [`00bee3fc`](#insn-00bee3fc)
  - `FALL_THROUGH` [`00bee4b4`](#insn-00bee4b4) → [`00bee4b8`](#insn-00bee4b8)
- ブロック [`00bee4b8`](#insn-00bee4b8) 範囲 `[['00bee4b8', '00bee4c7']]`
  - `CONDITIONAL_JUMP` [`00bee4c4`](#insn-00bee4c4) → [`00bee4e0`](#insn-00bee4e0)
  - `FALL_THROUGH` [`00bee4c4`](#insn-00bee4c4) → [`00bee4c8`](#insn-00bee4c8)
- ブロック [`00bee4c8`](#insn-00bee4c8) 範囲 `[['00bee4c8', '00bee4df']]`
  - `CONDITIONAL_JUMP` [`00bee4dc`](#insn-00bee4dc) → [`00bee4b8`](#insn-00bee4b8)
  - `FALL_THROUGH` [`00bee4dc`](#insn-00bee4dc) → [`00bee4e0`](#insn-00bee4e0)
- ブロック [`00bee4e0`](#insn-00bee4e0) 範囲 `[['00bee4e0', '00bee4e7']]`
  - `UNCONDITIONAL_JUMP` [`00bee4e4`](#insn-00bee4e4) → [`00bee3fc`](#insn-00bee3fc)

## 命令位置別の参照

- [`00bee1f4`](#insn-00bee1f4) → [`00bee3f0`](#insn-00bee3f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee204`](#insn-00bee204) → [`00bee2e4`](#insn-00bee2e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee210`](#insn-00bee210) → [`00bee224`](#insn-00bee224) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee220`](#insn-00bee220) → [`00bee2e4`](#insn-00bee2e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee228`](#insn-00bee228) → [`00bee218`](#insn-00bee218) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee244`](#insn-00bee244) → [`00bee268`](#insn-00bee268) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee264`](#insn-00bee264) → [`00bee26c`](#insn-00bee26c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee278`](#insn-00bee278) → [`00bee2a4`](#insn-00bee2a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee27c`](#insn-00bee27c) → [`00bee218`](#insn-00bee218) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee2a0`](#insn-00bee2a0) → [`00bee214`](#insn-00bee214) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee2b0`](#insn-00bee2b0) → [`00bee214`](#insn-00bee214) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee2cc`](#insn-00bee2cc) → [`00bee280`](#insn-00bee280) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee2dc`](#insn-00bee2dc) → [`00bee2a4`](#insn-00bee2a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee2e0`](#insn-00bee2e0) → [`00bee214`](#insn-00bee214) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee2ec`](#insn-00bee2ec) → [`00bee3e4`](#insn-00bee3e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee304`](#insn-00bee304) → [`00bee318`](#insn-00bee318) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee314`](#insn-00bee314) → [`00bee3e0`](#insn-00bee3e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee324`](#insn-00bee324) → [`00bee30c`](#insn-00bee30c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee334`](#insn-00bee334) → [`00bee30c`](#insn-00bee30c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee340`](#insn-00bee340) → [`00bee358`](#insn-00bee358) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee350`](#insn-00bee350) → [`00bee30c`](#insn-00bee30c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee354`](#insn-00bee354) → [`00bee374`](#insn-00bee374) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee370`](#insn-00bee370) → [`00bee30c`](#insn-00bee30c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee378`](#insn-00bee378) → [`00bee3a0`](#insn-00bee3a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee39c`](#insn-00bee39c) → [`00bee308`](#insn-00bee308) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee3ac`](#insn-00bee3ac) → [`00bee308`](#insn-00bee308) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee3c8`](#insn-00bee3c8) → [`00bee37c`](#insn-00bee37c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee3d8`](#insn-00bee3d8) → [`00bee3a0`](#insn-00bee3a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee3dc`](#insn-00bee3dc) → [`00bee308`](#insn-00bee308) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee3e8`](#insn-00bee3e8) → [`00bee408`](#insn-00bee408) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee404`](#insn-00bee404) → [`00bee3ec`](#insn-00bee3ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee41c`](#insn-00bee41c) → [`00bee448`](#insn-00bee448) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee444`](#insn-00bee444) → [`00bee474`](#insn-00bee474) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee464`](#insn-00bee464) → [`00bee420`](#insn-00bee420) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee470`](#insn-00bee470) → [`00bee438`](#insn-00bee438) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee47c`](#insn-00bee47c) → [`00bee3f8`](#insn-00bee3f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee49c`](#insn-00bee49c) → [`00bee3fc`](#insn-00bee3fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee4b4`](#insn-00bee4b4) → [`00bee3fc`](#insn-00bee3fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee4c4`](#insn-00bee4c4) → [`00bee4e0`](#insn-00bee4e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee4dc`](#insn-00bee4dc) → [`00bee4b8`](#insn-00bee4b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee4e4`](#insn-00bee4e4) → [`00bee3fc`](#insn-00bee3fc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bee1f4`](#insn-00bee1f4)

~~~json
{
  "source": "00bee1f4",
  "target": "00bee3f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee204`](#insn-00bee204)

~~~json
{
  "source": "00bee204",
  "target": "00bee2e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee210`](#insn-00bee210)

~~~json
{
  "source": "00bee210",
  "target": "00bee224",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee220`](#insn-00bee220)

~~~json
{
  "source": "00bee220",
  "target": "00bee2e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee228`](#insn-00bee228)

~~~json
{
  "source": "00bee228",
  "target": "00bee218",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee244`](#insn-00bee244)

~~~json
{
  "source": "00bee244",
  "target": "00bee268",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee264`](#insn-00bee264)

~~~json
{
  "source": "00bee264",
  "target": "00bee26c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee278`](#insn-00bee278)

~~~json
{
  "source": "00bee278",
  "target": "00bee2a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee27c`](#insn-00bee27c)

~~~json
{
  "source": "00bee27c",
  "target": "00bee218",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee2a0`](#insn-00bee2a0)

~~~json
{
  "source": "00bee2a0",
  "target": "00bee214",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee2b0`](#insn-00bee2b0)

~~~json
{
  "source": "00bee2b0",
  "target": "00bee214",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee2cc`](#insn-00bee2cc)

~~~json
{
  "source": "00bee2cc",
  "target": "00bee280",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee2dc`](#insn-00bee2dc)

~~~json
{
  "source": "00bee2dc",
  "target": "00bee2a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee2e0`](#insn-00bee2e0)

~~~json
{
  "source": "00bee2e0",
  "target": "00bee214",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee2ec`](#insn-00bee2ec)

~~~json
{
  "source": "00bee2ec",
  "target": "00bee3e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee304`](#insn-00bee304)

~~~json
{
  "source": "00bee304",
  "target": "00bee318",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee314`](#insn-00bee314)

~~~json
{
  "source": "00bee314",
  "target": "00bee3e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee324`](#insn-00bee324)

~~~json
{
  "source": "00bee324",
  "target": "00bee30c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee334`](#insn-00bee334)

~~~json
{
  "source": "00bee334",
  "target": "00bee30c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee340`](#insn-00bee340)

~~~json
{
  "source": "00bee340",
  "target": "00bee358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee350`](#insn-00bee350)

~~~json
{
  "source": "00bee350",
  "target": "00bee30c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee354`](#insn-00bee354)

~~~json
{
  "source": "00bee354",
  "target": "00bee374",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee370`](#insn-00bee370)

~~~json
{
  "source": "00bee370",
  "target": "00bee30c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee378`](#insn-00bee378)

~~~json
{
  "source": "00bee378",
  "target": "00bee3a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee39c`](#insn-00bee39c)

~~~json
{
  "source": "00bee39c",
  "target": "00bee308",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee3ac`](#insn-00bee3ac)

~~~json
{
  "source": "00bee3ac",
  "target": "00bee308",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee3c8`](#insn-00bee3c8)

~~~json
{
  "source": "00bee3c8",
  "target": "00bee37c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee3d8`](#insn-00bee3d8)

~~~json
{
  "source": "00bee3d8",
  "target": "00bee3a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee3dc`](#insn-00bee3dc)

~~~json
{
  "source": "00bee3dc",
  "target": "00bee308",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee3e8`](#insn-00bee3e8)

~~~json
{
  "source": "00bee3e8",
  "target": "00bee408",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee404`](#insn-00bee404)

~~~json
{
  "source": "00bee404",
  "target": "00bee3ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee41c`](#insn-00bee41c)

~~~json
{
  "source": "00bee41c",
  "target": "00bee448",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee444`](#insn-00bee444)

~~~json
{
  "source": "00bee444",
  "target": "00bee474",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee464`](#insn-00bee464)

~~~json
{
  "source": "00bee464",
  "target": "00bee420",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee470`](#insn-00bee470)

~~~json
{
  "source": "00bee470",
  "target": "00bee438",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee47c`](#insn-00bee47c)

~~~json
{
  "source": "00bee47c",
  "target": "00bee3f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee49c`](#insn-00bee49c)

~~~json
{
  "source": "00bee49c",
  "target": "00bee3fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee4b4`](#insn-00bee4b4)

~~~json
{
  "source": "00bee4b4",
  "target": "00bee3fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee4c4`](#insn-00bee4c4)

~~~json
{
  "source": "00bee4c4",
  "target": "00bee4e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee4dc`](#insn-00bee4dc)

~~~json
{
  "source": "00bee4dc",
  "target": "00bee4b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee4e4`](#insn-00bee4e4)

~~~json
{
  "source": "00bee4e4",
  "target": "00bee3fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
