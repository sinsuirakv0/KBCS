# 00beab5c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 要確認
  - [v16.0.2 → v16.0.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/review-0006.md#review-031c270083f5ecfbc130560ee6bd4a4e)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00beab5c",
  "name": "FUN_00beab5c",
  "size": 764,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bcc16b1a25919ea5b407fcaacf9bdaf581746e48d1f8329c8419114ad85d1c06",
  "source_text_sha256": "bcc16b1a25919ea5b407fcaacf9bdaf581746e48d1f8329c8419114ad85d1c06",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00beab5c",
        "00beae57"
      ]
    ],
    "bytes_sha256": "50eb489d317f27a0c4cad66122c79fe08b0b20aa42e7d878a0085be0b497e192",
    "instruction_count": 191,
    "instruction_bytes": 764,
    "body_bytes": 764,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be3a30](../00be3/00be3a30.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6477 bytes

~~~c

uint * FUN_00beab5c(uint *param_1,uint *param_2,uint *param_3)

{
  uint *puVar1;
  ulong uVar2;
  uint uVar3;
  uint uVar4;
  bool bVar5;
  uint *puVar6;
  ulong uVar7;
  long lVar8;
  uint *puVar9;
  ulong uVar10;
  long lVar11;
  uint *puVar12;
  uint *puVar13;
  ulong uVar14;
  uint *puVar15;
  uint uVar16;
  uint uVar17;
  
  if (param_1 != param_2) {
    lVar8 = (long)param_2 - (long)param_1 >> 2;
    if (1 < lVar8) {
      uVar10 = lVar8 - 2U >> 1;
      uVar7 = uVar10;
      do {
        if ((long)uVar7 <= (long)uVar10) {
          uVar2 = (uVar7 & 0x3fffffffffffffff) << 1 | 1;
          uVar14 = (uVar7 & 0x3fffffffffffffff) * 2 + 2;
          puVar12 = param_1 + uVar2;
          if ((long)uVar14 < lVar8) {
            uVar17 = *puVar12;
            uVar3 = puVar12[1];
            uVar16 = uVar17;
            if (uVar17 <= uVar3) {
              uVar16 = uVar3;
            }
            puVar13 = puVar12 + 1;
            if (uVar3 <= uVar17) {
              puVar13 = puVar12;
              uVar14 = uVar2;
            }
          }
          else {
            uVar16 = *puVar12;
            puVar13 = puVar12;
            uVar14 = uVar2;
          }
          uVar17 = param_1[uVar7];
          puVar12 = param_1 + uVar7;
          if (uVar17 <= uVar16) {
            do {
              while( true ) {
                puVar9 = puVar13;
                *puVar12 = uVar16;
                if ((long)uVar10 < (long)uVar14) goto LAB_00beab84;
                uVar2 = uVar14 << 1 | 1;
                uVar14 = uVar14 * 2 + 2;
                puVar6 = param_1 + uVar2;
                puVar12 = puVar9;
                if ((long)uVar14 < lVar8) break;
                uVar16 = *puVar6;
                puVar13 = puVar6;
                uVar14 = uVar2;
                if (uVar16 < uVar17) goto LAB_00beab84;
              }
              uVar3 = *puVar6;
              uVar4 = puVar6[1];
              uVar16 = uVar3;
              if (uVar3 <= uVar4) {
                uVar16 = uVar4;
              }
              puVar13 = puVar6 + 1;
              if (uVar4 <= uVar3) {
                uVar14 = uVar2;
                puVar13 = puVar6;
              }
            } while (uVar17 <= uVar16);
LAB_00beab84:
            *puVar9 = uVar17;
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
        uVar16 = *puVar9;
        if (uVar16 < *param_1) {
          *puVar9 = *param_1;
          *param_1 = uVar16;
          if (1 < lVar8) {
            uVar17 = *puVar13;
            if ((long)param_2 - (long)param_1 == 8) {
              uVar7 = 1;
              puVar12 = puVar13;
            }
            else {
              uVar3 = param_1[2];
              bVar5 = uVar3 <= uVar17;
              if (uVar17 <= uVar3) {
                uVar17 = uVar3;
              }
              puVar12 = param_1 + 2;
                    /* try { // try from 00beacd4 to 00cead07 has its CatchHandler @ 00beb310 */
              if (bVar5) {
                puVar12 = puVar13;
              }
              uVar7 = 1;
              if (!bVar5) {
                uVar7 = 2;
              }
            }
            puVar6 = param_1;
            if (uVar16 <= uVar17) {
              do {
                while( true ) {
                  puVar15 = puVar12;
                  *puVar6 = uVar17;
                  if ((long)(lVar8 - 2U >> 1) < (long)uVar7) goto LAB_00beac78;
                  uVar10 = uVar7 << 1 | 1;
                  uVar7 = uVar7 * 2 + 2;
                  puVar1 = param_1 + uVar10;
                  puVar6 = puVar15;
                  if ((long)uVar7 < lVar8) break;
                  uVar17 = *puVar1;
                  uVar7 = uVar10;
                  puVar12 = puVar1;
                  if (uVar17 < uVar16) goto LAB_00beac78;
                }
                uVar3 = *puVar1;
                uVar4 = puVar1[1];
                uVar17 = uVar3;
                if (uVar3 <= uVar4) {
                  uVar17 = uVar4;
                }
                puVar12 = puVar1 + 1;
                if (uVar4 <= uVar3) {
                  uVar7 = uVar10;
                  puVar12 = puVar1;
                }
                    /* try { // try from 00bead08 to 00ceaf23 has its CatchHandler @ 00be231c */
              } while (uVar16 <= uVar17);
LAB_00beac78:
              *puVar15 = uVar16;
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
        uVar16 = *param_1;
        uVar7 = 0;
        puVar12 = param_1;
        do {
          uVar14 = uVar7 << 1 | 1;
          uVar10 = uVar7 * 2 + 2;
          puVar13 = puVar12 + uVar7 + 1;
          if ((long)uVar10 < lVar8) {
            uVar4 = puVar12[uVar7 + 2];
            uVar3 = puVar12[uVar7 + 1];
            uVar17 = uVar3;
            if (uVar3 <= uVar4) {
              uVar17 = uVar4;
            }
            puVar9 = puVar12 + uVar7 + 2;
            uVar7 = uVar10;
            if (uVar4 <= uVar3) {
              puVar9 = puVar13;
              uVar7 = uVar14;
            }
          }
          else {
            uVar17 = *puVar13;
            puVar9 = puVar13;
            uVar7 = uVar14;
          }
          *puVar12 = uVar17;
          puVar12 = puVar9;
        } while ((long)uVar7 <= (long)(lVar8 - 2U >> 1));
        param_2 = param_2 + -1;
        if (puVar9 == param_2) {
          *puVar9 = uVar16;
        }
        else {
          lVar11 = (long)puVar9 + (4 - (long)param_1) >> 2;
          *puVar9 = *param_2;
          *param_2 = uVar16;
          if (1 < lVar11) {
            uVar7 = lVar11 - 2U >> 1;
            uVar16 = *puVar9;
            uVar17 = param_1[uVar7];
            puVar12 = param_1 + uVar7;
            if (uVar17 < uVar16) {
              do {
                puVar13 = puVar12;
                *puVar9 = uVar17;
                if (uVar7 == 0) break;
                uVar7 = uVar7 - 1 >> 1;
                uVar17 = param_1[uVar7];
                puVar9 = puVar13;
                puVar12 = param_1 + uVar7;
              } while (uVar17 < uVar16);
              *puVar13 = uVar16;
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
<a id="insn-00beab5c"></a> `00beab5c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00beab60"></a> `00beab60` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-00beab64"></a> `00beab64` | `e0 0f 00 54` | b.eq 0x00bead60 | `CONDITIONAL_JUMP`
<a id="insn-00beab68"></a> `00beab68` | `29 00 00 cb` | sub x9,x1,x0 | `FALL_THROUGH`
<a id="insn-00beab6c"></a> `00beab6c` | `28 fd 42 93` | asr x8,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00beab70"></a> `00beab70` | `0a 09 00 f1` | subs x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00beab74"></a> `00beab74` | `0b 07 00 54` | b.lt 0x00beac54 | `CONDITIONAL_JUMP`
<a id="insn-00beab78"></a> `00beab78` | `4b fd 41 d3` | lsr x11,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00beab7c"></a> `00beab7c` | `ec 03 0b aa` | mov x12,x11 | `FALL_THROUGH`
<a id="insn-00beab80"></a> `00beab80` | `05 00 00 14` | b 0x00beab94 | `UNCONDITIONAL_JUMP`
<a id="insn-00beab84"></a> `00beab84` | `0f 02 00 b9` | str w15,[x16] | `FALL_THROUGH`
<a id="insn-00beab88"></a> `00beab88` | `9f 01 00 f1` | cmp x12,#0x0 | `FALL_THROUGH`
<a id="insn-00beab8c"></a> `00beab8c` | `8c 05 00 d1` | sub x12,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00beab90"></a> `00beab90` | `2d 06 00 54` | b.le 0x00beac54 | `CONDITIONAL_JUMP`
<a id="insn-00beab94"></a> `00beab94` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-00beab98"></a> `00beab98` | `8b ff ff 54` | b.lt 0x00beab88 | `CONDITIONAL_JUMP`
<a id="insn-00beab9c"></a> `00beab9c` | `2e 00 80 52` | mov w14,#0x1 | `FALL_THROUGH`
<a id="insn-00beaba0"></a> `00beaba0` | `8d f5 7f d3` | ubfiz x13,x12,#0x1,#0x3e | `FALL_THROUGH`
<a id="insn-00beaba4"></a> `00beaba4` | `8e f5 7f b3` | bfm x14,x12,#0x3f,#0x3d | `FALL_THROUGH`
<a id="insn-00beaba8"></a> `00beaba8` | `af 09 00 91` | add x15,x13,#0x2 | `FALL_THROUGH`
<a id="insn-00beabac"></a> `00beabac` | `0d 08 0e 8b` | add x13,x0,x14, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00beabb0"></a> `00beabb0` | `ff 01 08 eb` | cmp x15,x8 | `FALL_THROUGH`
<a id="insn-00beabb4"></a> `00beabb4` | `2a 01 00 54` | b.ge 0x00beabd8 | `CONDITIONAL_JUMP`
<a id="insn-00beabb8"></a> `00beabb8` | `f0 03 0d aa` | mov x16,x13 | `FALL_THROUGH`
<a id="insn-00beabbc"></a> `00beabbc` | `b1 01 40 b9` | ldr w17,[x13] | `FALL_THROUGH`
<a id="insn-00beabc0"></a> `00beabc0` | `03 4e 40 b8` | ldr w3,[x16, #0x4]! | `FALL_THROUGH`
<a id="insn-00beabc4"></a> `00beabc4` | `3f 02 03 6b` | cmp w17,w3 | `FALL_THROUGH`
<a id="insn-00beabc8"></a> `00beabc8` | `31 82 83 1a` | csel w17,w17,w3,hi | `FALL_THROUGH`
<a id="insn-00beabcc"></a> `00beabcc` | `0d 32 8d 9a` | csel x13,x16,x13,cc | `FALL_THROUGH`
<a id="insn-00beabd0"></a> `00beabd0` | `ee 31 8e 9a` | csel x14,x15,x14,cc | `FALL_THROUGH`
<a id="insn-00beabd4"></a> `00beabd4` | `02 00 00 14` | b 0x00beabdc | `UNCONDITIONAL_JUMP`
<a id="insn-00beabd8"></a> `00beabd8` | `b1 01 40 b9` | ldr w17,[x13] | `FALL_THROUGH`
<a id="insn-00beabdc"></a> `00beabdc` | `10 08 0c 8b` | add x16,x0,x12, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00beabe0"></a> `00beabe0` | `0f 02 40 b9` | ldr w15,[x16] | `FALL_THROUGH`
<a id="insn-00beabe4"></a> `00beabe4` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00beabe8"></a> `00beabe8` | `62 01 00 54` | b.cs 0x00beac14 | `CONDITIONAL_JUMP`
<a id="insn-00beabec"></a> `00beabec` | `e7 ff ff 17` | b 0x00beab88 | `UNCONDITIONAL_JUMP`
<a id="insn-00beabf0"></a> `00beabf0` | `e4 03 0d aa` | mov x4,x13 | `FALL_THROUGH`
<a id="insn-00beabf4"></a> `00beabf4` | `b1 01 40 b9` | ldr w17,[x13] | `FALL_THROUGH`
<a id="insn-00beabf8"></a> `00beabf8` | `85 4c 40 b8` | ldr w5,[x4, #0x4]! | `FALL_THROUGH`
<a id="insn-00beabfc"></a> `00beabfc` | `3f 02 05 6b` | cmp w17,w5 | `FALL_THROUGH`
<a id="insn-00beac00"></a> `00beac00` | `31 82 85 1a` | csel w17,w17,w5,hi | `FALL_THROUGH`
<a id="insn-00beac04"></a> `00beac04` | `8d 30 8d 9a` | csel x13,x4,x13,cc | `FALL_THROUGH`
<a id="insn-00beac08"></a> `00beac08` | `ce 31 83 9a` | csel x14,x14,x3,cc | `FALL_THROUGH`
<a id="insn-00beac0c"></a> `00beac0c` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00beac10"></a> `00beac10` | `a3 fb ff 54` | b.cc 0x00beab84 | `CONDITIONAL_JUMP`
<a id="insn-00beac14"></a> `00beac14` | `7f 01 0e eb` | cmp x11,x14 | `FALL_THROUGH`
<a id="insn-00beac18"></a> `00beac18` | `11 02 00 b9` | str w17,[x16] | `FALL_THROUGH`
<a id="insn-00beac1c"></a> `00beac1c` | `f0 03 0d aa` | mov x16,x13 | `FALL_THROUGH`
<a id="insn-00beac20"></a> `00beac20` | `2b fb ff 54` | b.lt 0x00beab84 | `CONDITIONAL_JUMP`
<a id="insn-00beac24"></a> `00beac24` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00beac28"></a> `00beac28` | `cd f9 7f d3` | lsl x13,x14,#0x1 | `FALL_THROUGH`
<a id="insn-00beac2c"></a> `00beac2c` | `c3 f9 7f b3` | bfm x3,x14,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00beac30"></a> `00beac30` | `ae 09 00 91` | add x14,x13,#0x2 | `FALL_THROUGH`
<a id="insn-00beac34"></a> `00beac34` | `0d 08 03 8b` | add x13,x0,x3, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00beac38"></a> `00beac38` | `df 01 08 eb` | cmp x14,x8 | `FALL_THROUGH`
<a id="insn-00beac3c"></a> `00beac3c` | `ab fd ff 54` | b.lt 0x00beabf0 | `CONDITIONAL_JUMP`
<a id="insn-00beac40"></a> `00beac40` | `b1 01 40 b9` | ldr w17,[x13] | `FALL_THROUGH`
<a id="insn-00beac44"></a> `00beac44` | `ee 03 03 aa` | mov x14,x3 | `FALL_THROUGH`
<a id="insn-00beac48"></a> `00beac48` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00beac4c"></a> `00beac4c` | `42 fe ff 54` | b.cs 0x00beac14 | `CONDITIONAL_JUMP`
<a id="insn-00beac50"></a> `00beac50` | `cd ff ff 17` | b 0x00beab84 | `UNCONDITIONAL_JUMP`
<a id="insn-00beac54"></a> `00beac54` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-00beac58"></a> `00beac58` | `e3 03 01 aa` | mov x3,x1 | `FALL_THROUGH`
<a id="insn-00beac5c"></a> `00beac5c` | `c0 07 00 54` | b.eq 0x00bead54 | `CONDITIONAL_JUMP`
<a id="insn-00beac60"></a> `00beac60` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00beac64"></a> `00beac64` | `0b 10 00 91` | add x11,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00beac68"></a> `00beac68` | `0c 20 00 91` | add x12,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00beac6c"></a> `00beac6c` | `2d 00 80 52` | mov w13,#0x1 | `FALL_THROUGH`
<a id="insn-00beac70"></a> `00beac70` | `ee 03 01 aa` | mov x14,x1 | `FALL_THROUGH`
<a id="insn-00beac74"></a> `00beac74` | `05 00 00 14` | b 0x00beac88 | `UNCONDITIONAL_JUMP`
<a id="insn-00beac78"></a> `00beac78` | `6f 00 00 b9` | str w15,[x3] | `FALL_THROUGH`
<a id="insn-00beac7c"></a> `00beac7c` | `ce 11 00 91` | add x14,x14,#0x4 | `FALL_THROUGH`
<a id="insn-00beac80"></a> `00beac80` | `df 01 02 eb` | cmp x14,x2 | `FALL_THROUGH`
<a id="insn-00beac84"></a> `00beac84` | `60 06 00 54` | b.eq 0x00bead50 | `CONDITIONAL_JUMP`
<a id="insn-00beac88"></a> `00beac88` | `cf 01 40 b9` | ldr w15,[x14] | `FALL_THROUGH`
<a id="insn-00beac8c"></a> `00beac8c` | `10 00 40 b9` | ldr w16,[x0] | `FALL_THROUGH`
<a id="insn-00beac90"></a> `00beac90` | `ff 01 10 6b` | cmp w15,w16 | `FALL_THROUGH`
<a id="insn-00beac94"></a> `00beac94` | `42 ff ff 54` | b.cs 0x00beac7c | `CONDITIONAL_JUMP`
<a id="insn-00beac98"></a> `00beac98` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00beac9c"></a> `00beac9c` | `d0 01 00 b9` | str w16,[x14] | `FALL_THROUGH`
<a id="insn-00beaca0"></a> `00beaca0` | `0f 00 00 b9` | str w15,[x0] | `FALL_THROUGH`
<a id="insn-00beaca4"></a> `00beaca4` | `cb fe ff 54` | b.lt 0x00beac7c | `CONDITIONAL_JUMP`
<a id="insn-00beaca8"></a> `00beaca8` | `71 01 40 b9` | ldr w17,[x11] | `FALL_THROUGH`
<a id="insn-00beacac"></a> `00beacac` | `3f 21 00 f1` | cmp x9,#0x8 | `FALL_THROUGH`
<a id="insn-00beacb0"></a> `00beacb0` | `c1 00 00 54` | b.ne 0x00beacc8 | `CONDITIONAL_JUMP`
<a id="insn-00beacb4"></a> `00beacb4` | `f0 03 0b aa` | mov x16,x11 | `FALL_THROUGH`
<a id="insn-00beacb8"></a> `00beacb8` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-00beacbc"></a> `00beacbc` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00beacc0"></a> `00beacc0` | `e3 fd ff 54` | b.cc 0x00beac7c | `CONDITIONAL_JUMP`
<a id="insn-00beacc4"></a> `00beacc4` | `08 00 00 14` | b 0x00beace4 | `UNCONDITIONAL_JUMP`
<a id="insn-00beacc8"></a> `00beacc8` | `90 01 40 b9` | ldr w16,[x12] | `FALL_THROUGH`
<a id="insn-00beaccc"></a> `00beaccc` | `3f 02 10 6b` | cmp w17,w16 | `FALL_THROUGH`
<a id="insn-00beacd0"></a> `00beacd0` | `31 82 90 1a` | csel w17,w17,w16,hi | `FALL_THROUGH`
<a id="insn-00beacd4"></a> `00beacd4` | `90 31 8b 9a` | csel x16,x12,x11,cc | `FALL_THROUGH`
<a id="insn-00beacd8"></a> `00beacd8` | `a4 25 8d 9a` | cinc x4,x13,cc | `FALL_THROUGH`
<a id="insn-00beacdc"></a> `00beacdc` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00beace0"></a> `00beace0` | `e3 fc ff 54` | b.cc 0x00beac7c | `CONDITIONAL_JUMP`
<a id="insn-00beace4"></a> `00beace4` | `e3 03 00 aa` | mov x3,x0 | `FALL_THROUGH`
<a id="insn-00beace8"></a> `00beace8` | `0a 00 00 14` | b 0x00bead10 | `UNCONDITIONAL_JUMP`
<a id="insn-00beacec"></a> `00beacec` | `e6 03 10 aa` | mov x6,x16 | `FALL_THROUGH`
<a id="insn-00beacf0"></a> `00beacf0` | `11 02 40 b9` | ldr w17,[x16] | `FALL_THROUGH`
<a id="insn-00beacf4"></a> `00beacf4` | `c7 4c 40 b8` | ldr w7,[x6, #0x4]! | `FALL_THROUGH`
<a id="insn-00beacf8"></a> `00beacf8` | `3f 02 07 6b` | cmp w17,w7 | `FALL_THROUGH`
<a id="insn-00beacfc"></a> `00beacfc` | `31 82 87 1a` | csel w17,w17,w7,hi | `FALL_THROUGH`
<a id="insn-00bead00"></a> `00bead00` | `d0 30 90 9a` | csel x16,x6,x16,cc | `FALL_THROUGH`
<a id="insn-00bead04"></a> `00bead04` | `84 30 85 9a` | csel x4,x4,x5,cc | `FALL_THROUGH`
<a id="insn-00bead08"></a> `00bead08` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bead0c"></a> `00bead0c` | `63 fb ff 54` | b.cc 0x00beac78 | `CONDITIONAL_JUMP`
<a id="insn-00bead10"></a> `00bead10` | `5f 01 04 eb` | cmp x10,x4 | `FALL_THROUGH`
<a id="insn-00bead14"></a> `00bead14` | `71 00 00 b9` | str w17,[x3] | `FALL_THROUGH`
<a id="insn-00bead18"></a> `00bead18` | `e3 03 10 aa` | mov x3,x16 | `FALL_THROUGH`
<a id="insn-00bead1c"></a> `00bead1c` | `eb fa ff 54` | b.lt 0x00beac78 | `CONDITIONAL_JUMP`
<a id="insn-00bead20"></a> `00bead20` | `25 00 80 52` | mov w5,#0x1 | `FALL_THROUGH`
<a id="insn-00bead24"></a> `00bead24` | `90 f8 7f d3` | lsl x16,x4,#0x1 | `FALL_THROUGH`
<a id="insn-00bead28"></a> `00bead28` | `85 f8 7f b3` | bfm x5,x4,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00bead2c"></a> `00bead2c` | `04 0a 00 91` | add x4,x16,#0x2 | `FALL_THROUGH`
<a id="insn-00bead30"></a> `00bead30` | `10 08 05 8b` | add x16,x0,x5, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bead34"></a> `00bead34` | `9f 00 08 eb` | cmp x4,x8 | `FALL_THROUGH`
<a id="insn-00bead38"></a> `00bead38` | `ab fd ff 54` | b.lt 0x00beacec | `CONDITIONAL_JUMP`
<a id="insn-00bead3c"></a> `00bead3c` | `11 02 40 b9` | ldr w17,[x16] | `FALL_THROUGH`
<a id="insn-00bead40"></a> `00bead40` | `e4 03 05 aa` | mov x4,x5 | `FALL_THROUGH`
<a id="insn-00bead44"></a> `00bead44` | `3f 02 0f 6b` | cmp w17,w15 | `FALL_THROUGH`
<a id="insn-00bead48"></a> `00bead48` | `42 fe ff 54` | b.cs 0x00bead10 | `CONDITIONAL_JUMP`
<a id="insn-00bead4c"></a> `00bead4c` | `cb ff ff 17` | b 0x00beac78 | `UNCONDITIONAL_JUMP`
<a id="insn-00bead50"></a> `00bead50` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bead54"></a> `00bead54` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bead58"></a> `00bead58` | `0a 01 00 54` | b.ge 0x00bead78 | `CONDITIONAL_JUMP`
<a id="insn-00bead5c"></a> `00bead5c` | `e2 03 03 aa` | mov x2,x3 | `FALL_THROUGH`
<a id="insn-00bead60"></a> `00bead60` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bead64"></a> `00bead64` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bead68"></a> `00bead68` | `2a 01 00 b9` | str w10,[x9] | `FALL_THROUGH`
<a id="insn-00bead6c"></a> `00bead6c` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bead70"></a> `00bead70` | `08 05 00 d1` | sub x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bead74"></a> `00bead74` | `4d ff ff 54` | b.le 0x00bead5c | `CONDITIONAL_JUMP`
<a id="insn-00bead78"></a> `00bead78` | `09 09 00 d1` | sub x9,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bead7c"></a> `00bead7c` | `0a 00 40 b9` | ldr w10,[x0] | `FALL_THROUGH`
<a id="insn-00bead80"></a> `00bead80` | `ed 03 1f aa` | mov x13,xzr | `FALL_THROUGH`
<a id="insn-00bead84"></a> `00bead84` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bead88"></a> `00bead88` | `ec 03 00 aa` | mov x12,x0 | `FALL_THROUGH`
<a id="insn-00bead8c"></a> `00bead8c` | `0b 00 00 14` | b 0x00beadb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bead90"></a> `00bead90` | `0d 8e 40 b8` | ldr w13,[x16, #0x8]! | `FALL_THROUGH`
<a id="insn-00bead94"></a> `00bead94` | `0f c2 5f b8` | ldur w15,[x16, #-0x4] | `FALL_THROUGH`
<a id="insn-00bead98"></a> `00bead98` | `ff 01 0d 6b` | cmp w15,w13 | `FALL_THROUGH`
<a id="insn-00bead9c"></a> `00bead9c` | `ef 81 8d 1a` | csel w15,w15,w13,hi | `FALL_THROUGH`
<a id="insn-00beada0"></a> `00beada0` | `09 32 89 9a` | csel x9,x16,x9,cc | `FALL_THROUGH`
<a id="insn-00beada4"></a> `00beada4` | `2d 32 8e 9a` | csel x13,x17,x14,cc | `FALL_THROUGH`
<a id="insn-00beada8"></a> `00beada8` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00beadac"></a> `00beadac` | `8f 01 00 b9` | str w15,[x12] | `FALL_THROUGH`
<a id="insn-00beadb0"></a> `00beadb0` | `ec 03 09 aa` | mov x12,x9 | `FALL_THROUGH`
<a id="insn-00beadb4"></a> `00beadb4` | `8c 01 00 54` | b.gt 0x00beade4 | `CONDITIONAL_JUMP`
<a id="insn-00beadb8"></a> `00beadb8` | `a9 f9 7f d3` | lsl x9,x13,#0x1 | `FALL_THROUGH`
<a id="insn-00beadbc"></a> `00beadbc` | `90 09 0d 8b` | add x16,x12,x13, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00beadc0"></a> `00beadc0` | `2e 00 80 52` | mov w14,#0x1 | `FALL_THROUGH`
<a id="insn-00beadc4"></a> `00beadc4` | `ae f9 7f b3` | bfm x14,x13,#0x3f,#0x3e | `FALL_THROUGH`
<a id="insn-00beadc8"></a> `00beadc8` | `31 09 00 91` | add x17,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00beadcc"></a> `00beadcc` | `09 12 00 91` | add x9,x16,#0x4 | `FALL_THROUGH`
<a id="insn-00beadd0"></a> `00beadd0` | `3f 02 08 eb` | cmp x17,x8 | `FALL_THROUGH`
<a id="insn-00beadd4"></a> `00beadd4` | `eb fd ff 54` | b.lt 0x00bead90 | `CONDITIONAL_JUMP`
<a id="insn-00beadd8"></a> `00beadd8` | `2f 01 40 b9` | ldr w15,[x9] | `FALL_THROUGH`
<a id="insn-00beaddc"></a> `00beaddc` | `ed 03 0e aa` | mov x13,x14 | `FALL_THROUGH`
<a id="insn-00beade0"></a> `00beade0` | `f2 ff ff 17` | b 0x00beada8 | `UNCONDITIONAL_JUMP`
<a id="insn-00beade4"></a> `00beade4` | `21 10 00 d1` | sub x1,x1,#0x4 | `FALL_THROUGH`
<a id="insn-00beade8"></a> `00beade8` | `3f 01 01 eb` | cmp x9,x1 | `FALL_THROUGH`
<a id="insn-00beadec"></a> `00beadec` | `e0 fb ff 54` | b.eq 0x00bead68 | `CONDITIONAL_JUMP`
<a id="insn-00beadf0"></a> `00beadf0` | `2b 01 00 cb` | sub x11,x9,x0 | `FALL_THROUGH`
<a id="insn-00beadf4"></a> `00beadf4` | `2c 00 40 b9` | ldr w12,[x1] | `FALL_THROUGH`
<a id="insn-00beadf8"></a> `00beadf8` | `6b 11 00 91` | add x11,x11,#0x4 | `FALL_THROUGH`
<a id="insn-00beadfc"></a> `00beadfc` | `6b fd 42 93` | asr x11,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00beae00"></a> `00beae00` | `2c 01 00 b9` | str w12,[x9] | `FALL_THROUGH`
<a id="insn-00beae04"></a> `00beae04` | `2a 00 00 b9` | str w10,[x1] | `FALL_THROUGH`
<a id="insn-00beae08"></a> `00beae08` | `6b 09 00 f1` | subs x11,x11,#0x2 | `FALL_THROUGH`
<a id="insn-00beae0c"></a> `00beae0c` | `0b fb ff 54` | b.lt 0x00bead6c | `CONDITIONAL_JUMP`
<a id="insn-00beae10"></a> `00beae10` | `6a fd 41 d3` | lsr x10,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00beae14"></a> `00beae14` | `2b 01 40 b9` | ldr w11,[x9] | `FALL_THROUGH`
<a id="insn-00beae18"></a> `00beae18` | `0c 08 0a 8b` | add x12,x0,x10, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00beae1c"></a> `00beae1c` | `8d 01 40 b9` | ldr w13,[x12] | `FALL_THROUGH`
<a id="insn-00beae20"></a> `00beae20` | `bf 01 0b 6b` | cmp w13,w11 | `FALL_THROUGH`
<a id="insn-00beae24"></a> `00beae24` | `42 fa ff 54` | b.cs 0x00bead6c | `CONDITIONAL_JUMP`
<a id="insn-00beae28"></a> `00beae28` | `ee 03 09 aa` | mov x14,x9 | `FALL_THROUGH`
<a id="insn-00beae2c"></a> `00beae2c` | `e9 03 0c aa` | mov x9,x12 | `FALL_THROUGH`
<a id="insn-00beae30"></a> `00beae30` | `cd 01 00 b9` | str w13,[x14] | `FALL_THROUGH`
<a id="insn-00beae34"></a> `00beae34` | `ea 00 00 b4` | cbz x10,0x00beae50 | `CONDITIONAL_JUMP`
<a id="insn-00beae38"></a> `00beae38` | `4a 05 00 d1` | sub x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00beae3c"></a> `00beae3c` | `4a fd 41 d3` | lsr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00beae40"></a> `00beae40` | `0c 08 0a 8b` | add x12,x0,x10, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00beae44"></a> `00beae44` | `8d 01 40 b9` | ldr w13,[x12] | `FALL_THROUGH`
<a id="insn-00beae48"></a> `00beae48` | `bf 01 0b 6b` | cmp w13,w11 | `FALL_THROUGH`
<a id="insn-00beae4c"></a> `00beae4c` | `e3 fe ff 54` | b.cc 0x00beae28 | `CONDITIONAL_JUMP`
<a id="insn-00beae50"></a> `00beae50` | `2b 01 00 b9` | str w11,[x9] | `FALL_THROUGH`
<a id="insn-00beae54"></a> `00beae54` | `c6 ff ff 17` | b 0x00bead6c | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00beab5c`](#insn-00beab5c) 範囲 `[['00beab5c', '00beab67']]`
  - `CONDITIONAL_JUMP` [`00beab64`](#insn-00beab64) → [`00bead60`](#insn-00bead60)
  - `FALL_THROUGH` [`00beab64`](#insn-00beab64) → [`00beab68`](#insn-00beab68)
- ブロック [`00beab68`](#insn-00beab68) 範囲 `[['00beab68', '00beab77']]`
  - `CONDITIONAL_JUMP` [`00beab74`](#insn-00beab74) → [`00beac54`](#insn-00beac54)
  - `FALL_THROUGH` [`00beab74`](#insn-00beab74) → [`00beab78`](#insn-00beab78)
- ブロック [`00beab78`](#insn-00beab78) 範囲 `[['00beab78', '00beab83']]`
  - `UNCONDITIONAL_JUMP` [`00beab80`](#insn-00beab80) → [`00beab94`](#insn-00beab94)
- ブロック [`00beab84`](#insn-00beab84) 範囲 `[['00beab84', '00beab87']]`
  - `FALL_THROUGH` [`00beab84`](#insn-00beab84) → [`00beab88`](#insn-00beab88)
- ブロック [`00beab88`](#insn-00beab88) 範囲 `[['00beab88', '00beab93']]`
  - `CONDITIONAL_JUMP` [`00beab90`](#insn-00beab90) → [`00beac54`](#insn-00beac54)
  - `FALL_THROUGH` [`00beab90`](#insn-00beab90) → [`00beab94`](#insn-00beab94)
- ブロック [`00beab94`](#insn-00beab94) 範囲 `[['00beab94', '00beab9b']]`
  - `CONDITIONAL_JUMP` [`00beab98`](#insn-00beab98) → [`00beab88`](#insn-00beab88)
  - `FALL_THROUGH` [`00beab98`](#insn-00beab98) → [`00beab9c`](#insn-00beab9c)
- ブロック [`00beab9c`](#insn-00beab9c) 範囲 `[['00beab9c', '00beabb7']]`
  - `CONDITIONAL_JUMP` [`00beabb4`](#insn-00beabb4) → [`00beabd8`](#insn-00beabd8)
  - `FALL_THROUGH` [`00beabb4`](#insn-00beabb4) → [`00beabb8`](#insn-00beabb8)
- ブロック [`00beabb8`](#insn-00beabb8) 範囲 `[['00beabb8', '00beabd7']]`
  - `UNCONDITIONAL_JUMP` [`00beabd4`](#insn-00beabd4) → [`00beabdc`](#insn-00beabdc)
- ブロック [`00beabd8`](#insn-00beabd8) 範囲 `[['00beabd8', '00beabdb']]`
  - `FALL_THROUGH` [`00beabd8`](#insn-00beabd8) → [`00beabdc`](#insn-00beabdc)
- ブロック [`00beabdc`](#insn-00beabdc) 範囲 `[['00beabdc', '00beabeb']]`
  - `CONDITIONAL_JUMP` [`00beabe8`](#insn-00beabe8) → [`00beac14`](#insn-00beac14)
  - `FALL_THROUGH` [`00beabe8`](#insn-00beabe8) → [`00beabec`](#insn-00beabec)
- ブロック [`00beabec`](#insn-00beabec) 範囲 `[['00beabec', '00beabef']]`
  - `UNCONDITIONAL_JUMP` [`00beabec`](#insn-00beabec) → [`00beab88`](#insn-00beab88)
- ブロック [`00beabf0`](#insn-00beabf0) 範囲 `[['00beabf0', '00beac13']]`
  - `CONDITIONAL_JUMP` [`00beac10`](#insn-00beac10) → [`00beab84`](#insn-00beab84)
  - `FALL_THROUGH` [`00beac10`](#insn-00beac10) → [`00beac14`](#insn-00beac14)
- ブロック [`00beac14`](#insn-00beac14) 範囲 `[['00beac14', '00beac23']]`
  - `CONDITIONAL_JUMP` [`00beac20`](#insn-00beac20) → [`00beab84`](#insn-00beab84)
  - `FALL_THROUGH` [`00beac20`](#insn-00beac20) → [`00beac24`](#insn-00beac24)
- ブロック [`00beac24`](#insn-00beac24) 範囲 `[['00beac24', '00beac3f']]`
  - `CONDITIONAL_JUMP` [`00beac3c`](#insn-00beac3c) → [`00beabf0`](#insn-00beabf0)
  - `FALL_THROUGH` [`00beac3c`](#insn-00beac3c) → [`00beac40`](#insn-00beac40)
- ブロック [`00beac40`](#insn-00beac40) 範囲 `[['00beac40', '00beac4f']]`
  - `CONDITIONAL_JUMP` [`00beac4c`](#insn-00beac4c) → [`00beac14`](#insn-00beac14)
  - `FALL_THROUGH` [`00beac4c`](#insn-00beac4c) → [`00beac50`](#insn-00beac50)
- ブロック [`00beac50`](#insn-00beac50) 範囲 `[['00beac50', '00beac53']]`
  - `UNCONDITIONAL_JUMP` [`00beac50`](#insn-00beac50) → [`00beab84`](#insn-00beab84)
- ブロック [`00beac54`](#insn-00beac54) 範囲 `[['00beac54', '00beac5f']]`
  - `CONDITIONAL_JUMP` [`00beac5c`](#insn-00beac5c) → [`00bead54`](#insn-00bead54)
  - `FALL_THROUGH` [`00beac5c`](#insn-00beac5c) → [`00beac60`](#insn-00beac60)
- ブロック [`00beac60`](#insn-00beac60) 範囲 `[['00beac60', '00beac77']]`
  - `UNCONDITIONAL_JUMP` [`00beac74`](#insn-00beac74) → [`00beac88`](#insn-00beac88)
- ブロック [`00beac78`](#insn-00beac78) 範囲 `[['00beac78', '00beac7b']]`
  - `FALL_THROUGH` [`00beac78`](#insn-00beac78) → [`00beac7c`](#insn-00beac7c)
- ブロック [`00beac7c`](#insn-00beac7c) 範囲 `[['00beac7c', '00beac87']]`
  - `CONDITIONAL_JUMP` [`00beac84`](#insn-00beac84) → [`00bead50`](#insn-00bead50)
  - `FALL_THROUGH` [`00beac84`](#insn-00beac84) → [`00beac88`](#insn-00beac88)
- ブロック [`00beac88`](#insn-00beac88) 範囲 `[['00beac88', '00beac97']]`
  - `CONDITIONAL_JUMP` [`00beac94`](#insn-00beac94) → [`00beac7c`](#insn-00beac7c)
  - `FALL_THROUGH` [`00beac94`](#insn-00beac94) → [`00beac98`](#insn-00beac98)
- ブロック [`00beac98`](#insn-00beac98) 範囲 `[['00beac98', '00beaca7']]`
  - `CONDITIONAL_JUMP` [`00beaca4`](#insn-00beaca4) → [`00beac7c`](#insn-00beac7c)
  - `FALL_THROUGH` [`00beaca4`](#insn-00beaca4) → [`00beaca8`](#insn-00beaca8)
- ブロック [`00beaca8`](#insn-00beaca8) 範囲 `[['00beaca8', '00beacb3']]`
  - `CONDITIONAL_JUMP` [`00beacb0`](#insn-00beacb0) → [`00beacc8`](#insn-00beacc8)
  - `FALL_THROUGH` [`00beacb0`](#insn-00beacb0) → [`00beacb4`](#insn-00beacb4)
- ブロック [`00beacb4`](#insn-00beacb4) 範囲 `[['00beacb4', '00beacc3']]`
  - `CONDITIONAL_JUMP` [`00beacc0`](#insn-00beacc0) → [`00beac7c`](#insn-00beac7c)
  - `FALL_THROUGH` [`00beacc0`](#insn-00beacc0) → [`00beacc4`](#insn-00beacc4)
- ブロック [`00beacc4`](#insn-00beacc4) 範囲 `[['00beacc4', '00beacc7']]`
  - `UNCONDITIONAL_JUMP` [`00beacc4`](#insn-00beacc4) → [`00beace4`](#insn-00beace4)
- ブロック [`00beacc8`](#insn-00beacc8) 範囲 `[['00beacc8', '00beacd3']]`
  - `FALL_THROUGH` [`00beacd0`](#insn-00beacd0) → [`00beacd4`](#insn-00beacd4)
- ブロック [`00beacd4`](#insn-00beacd4) 範囲 `[['00beacd4', '00beace3']]`
  - `CONDITIONAL_JUMP` [`00beace0`](#insn-00beace0) → [`00beac7c`](#insn-00beac7c)
  - `FALL_THROUGH` [`00beace0`](#insn-00beace0) → [`00beace4`](#insn-00beace4)
- ブロック [`00beace4`](#insn-00beace4) 範囲 `[['00beace4', '00beaceb']]`
  - `UNCONDITIONAL_JUMP` [`00beace8`](#insn-00beace8) → [`00bead10`](#insn-00bead10)
- ブロック [`00beacec`](#insn-00beacec) 範囲 `[['00beacec', '00bead07']]`
  - `FALL_THROUGH` [`00bead04`](#insn-00bead04) → [`00bead08`](#insn-00bead08)
- ブロック [`00bead08`](#insn-00bead08) 範囲 `[['00bead08', '00bead0f']]`
  - `CONDITIONAL_JUMP` [`00bead0c`](#insn-00bead0c) → [`00beac78`](#insn-00beac78)
  - `FALL_THROUGH` [`00bead0c`](#insn-00bead0c) → [`00bead10`](#insn-00bead10)
- ブロック [`00bead10`](#insn-00bead10) 範囲 `[['00bead10', '00bead1f']]`
  - `CONDITIONAL_JUMP` [`00bead1c`](#insn-00bead1c) → [`00beac78`](#insn-00beac78)
  - `FALL_THROUGH` [`00bead1c`](#insn-00bead1c) → [`00bead20`](#insn-00bead20)
- ブロック [`00bead20`](#insn-00bead20) 範囲 `[['00bead20', '00bead3b']]`
  - `CONDITIONAL_JUMP` [`00bead38`](#insn-00bead38) → [`00beacec`](#insn-00beacec)
  - `FALL_THROUGH` [`00bead38`](#insn-00bead38) → [`00bead3c`](#insn-00bead3c)
- ブロック [`00bead3c`](#insn-00bead3c) 範囲 `[['00bead3c', '00bead4b']]`
  - `CONDITIONAL_JUMP` [`00bead48`](#insn-00bead48) → [`00bead10`](#insn-00bead10)
  - `FALL_THROUGH` [`00bead48`](#insn-00bead48) → [`00bead4c`](#insn-00bead4c)
- ブロック [`00bead4c`](#insn-00bead4c) 範囲 `[['00bead4c', '00bead4f']]`
  - `UNCONDITIONAL_JUMP` [`00bead4c`](#insn-00bead4c) → [`00beac78`](#insn-00beac78)
- ブロック [`00bead50`](#insn-00bead50) 範囲 `[['00bead50', '00bead53']]`
  - `FALL_THROUGH` [`00bead50`](#insn-00bead50) → [`00bead54`](#insn-00bead54)
- ブロック [`00bead54`](#insn-00bead54) 範囲 `[['00bead54', '00bead5b']]`
  - `CONDITIONAL_JUMP` [`00bead58`](#insn-00bead58) → [`00bead78`](#insn-00bead78)
  - `FALL_THROUGH` [`00bead58`](#insn-00bead58) → [`00bead5c`](#insn-00bead5c)
- ブロック [`00bead5c`](#insn-00bead5c) 範囲 `[['00bead5c', '00bead5f']]`
  - `FALL_THROUGH` [`00bead5c`](#insn-00bead5c) → [`00bead60`](#insn-00bead60)
- ブロック [`00bead60`](#insn-00bead60) 範囲 `[['00bead60', '00bead67']]`
- ブロック [`00bead68`](#insn-00bead68) 範囲 `[['00bead68', '00bead6b']]`
  - `FALL_THROUGH` [`00bead68`](#insn-00bead68) → [`00bead6c`](#insn-00bead6c)
- ブロック [`00bead6c`](#insn-00bead6c) 範囲 `[['00bead6c', '00bead77']]`
  - `CONDITIONAL_JUMP` [`00bead74`](#insn-00bead74) → [`00bead5c`](#insn-00bead5c)
  - `FALL_THROUGH` [`00bead74`](#insn-00bead74) → [`00bead78`](#insn-00bead78)
- ブロック [`00bead78`](#insn-00bead78) 範囲 `[['00bead78', '00bead8f']]`
  - `UNCONDITIONAL_JUMP` [`00bead8c`](#insn-00bead8c) → [`00beadb8`](#insn-00beadb8)
- ブロック [`00bead90`](#insn-00bead90) 範囲 `[['00bead90', '00beada7']]`
  - `FALL_THROUGH` [`00beada4`](#insn-00beada4) → [`00beada8`](#insn-00beada8)
- ブロック [`00beada8`](#insn-00beada8) 範囲 `[['00beada8', '00beadb7']]`
  - `CONDITIONAL_JUMP` [`00beadb4`](#insn-00beadb4) → [`00beade4`](#insn-00beade4)
  - `FALL_THROUGH` [`00beadb4`](#insn-00beadb4) → [`00beadb8`](#insn-00beadb8)
- ブロック [`00beadb8`](#insn-00beadb8) 範囲 `[['00beadb8', '00beadd7']]`
  - `CONDITIONAL_JUMP` [`00beadd4`](#insn-00beadd4) → [`00bead90`](#insn-00bead90)
  - `FALL_THROUGH` [`00beadd4`](#insn-00beadd4) → [`00beadd8`](#insn-00beadd8)
- ブロック [`00beadd8`](#insn-00beadd8) 範囲 `[['00beadd8', '00beade3']]`
  - `UNCONDITIONAL_JUMP` [`00beade0`](#insn-00beade0) → [`00beada8`](#insn-00beada8)
- ブロック [`00beade4`](#insn-00beade4) 範囲 `[['00beade4', '00beadef']]`
  - `CONDITIONAL_JUMP` [`00beadec`](#insn-00beadec) → [`00bead68`](#insn-00bead68)
  - `FALL_THROUGH` [`00beadec`](#insn-00beadec) → [`00beadf0`](#insn-00beadf0)
- ブロック [`00beadf0`](#insn-00beadf0) 範囲 `[['00beadf0', '00beae0f']]`
  - `CONDITIONAL_JUMP` [`00beae0c`](#insn-00beae0c) → [`00bead6c`](#insn-00bead6c)
  - `FALL_THROUGH` [`00beae0c`](#insn-00beae0c) → [`00beae10`](#insn-00beae10)
- ブロック [`00beae10`](#insn-00beae10) 範囲 `[['00beae10', '00beae27']]`
  - `CONDITIONAL_JUMP` [`00beae24`](#insn-00beae24) → [`00bead6c`](#insn-00bead6c)
  - `FALL_THROUGH` [`00beae24`](#insn-00beae24) → [`00beae28`](#insn-00beae28)
- ブロック [`00beae28`](#insn-00beae28) 範囲 `[['00beae28', '00beae37']]`
  - `CONDITIONAL_JUMP` [`00beae34`](#insn-00beae34) → [`00beae50`](#insn-00beae50)
  - `FALL_THROUGH` [`00beae34`](#insn-00beae34) → [`00beae38`](#insn-00beae38)
- ブロック [`00beae38`](#insn-00beae38) 範囲 `[['00beae38', '00beae4f']]`
  - `CONDITIONAL_JUMP` [`00beae4c`](#insn-00beae4c) → [`00beae28`](#insn-00beae28)
  - `FALL_THROUGH` [`00beae4c`](#insn-00beae4c) → [`00beae50`](#insn-00beae50)
- ブロック [`00beae50`](#insn-00beae50) 範囲 `[['00beae50', '00beae57']]`
  - `UNCONDITIONAL_JUMP` [`00beae54`](#insn-00beae54) → [`00bead6c`](#insn-00bead6c)

## 命令位置別の参照

- [`00beab64`](#insn-00beab64) → [`00bead60`](#insn-00bead60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beab74`](#insn-00beab74) → [`00beac54`](#insn-00beac54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beab80`](#insn-00beab80) → [`00beab94`](#insn-00beab94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beab90`](#insn-00beab90) → [`00beac54`](#insn-00beac54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beab98`](#insn-00beab98) → [`00beab88`](#insn-00beab88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beabb4`](#insn-00beabb4) → [`00beabd8`](#insn-00beabd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beabd4`](#insn-00beabd4) → [`00beabdc`](#insn-00beabdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beabe8`](#insn-00beabe8) → [`00beac14`](#insn-00beac14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beabec`](#insn-00beabec) → [`00beab88`](#insn-00beab88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beac10`](#insn-00beac10) → [`00beab84`](#insn-00beab84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beac20`](#insn-00beac20) → [`00beab84`](#insn-00beab84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beac3c`](#insn-00beac3c) → [`00beabf0`](#insn-00beabf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beac4c`](#insn-00beac4c) → [`00beac14`](#insn-00beac14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beac50`](#insn-00beac50) → [`00beab84`](#insn-00beab84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beac5c`](#insn-00beac5c) → [`00bead54`](#insn-00bead54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beac74`](#insn-00beac74) → [`00beac88`](#insn-00beac88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beac84`](#insn-00beac84) → [`00bead50`](#insn-00bead50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beac94`](#insn-00beac94) → [`00beac7c`](#insn-00beac7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaca4`](#insn-00beaca4) → [`00beac7c`](#insn-00beac7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beacb0`](#insn-00beacb0) → [`00beacc8`](#insn-00beacc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beacc0`](#insn-00beacc0) → [`00beac7c`](#insn-00beac7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beacc4`](#insn-00beacc4) → [`00beace4`](#insn-00beace4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beace0`](#insn-00beace0) → [`00beac7c`](#insn-00beac7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beace8`](#insn-00beace8) → [`00bead10`](#insn-00bead10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bead0c`](#insn-00bead0c) → [`00beac78`](#insn-00beac78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bead1c`](#insn-00bead1c) → [`00beac78`](#insn-00beac78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bead38`](#insn-00bead38) → [`00beacec`](#insn-00beacec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bead48`](#insn-00bead48) → [`00bead10`](#insn-00bead10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bead4c`](#insn-00bead4c) → [`00beac78`](#insn-00beac78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bead58`](#insn-00bead58) → [`00bead78`](#insn-00bead78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bead74`](#insn-00bead74) → [`00bead5c`](#insn-00bead5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bead8c`](#insn-00bead8c) → [`00beadb8`](#insn-00beadb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beadb4`](#insn-00beadb4) → [`00beade4`](#insn-00beade4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beadd4`](#insn-00beadd4) → [`00bead90`](#insn-00bead90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beade0`](#insn-00beade0) → [`00beada8`](#insn-00beada8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beadec`](#insn-00beadec) → [`00bead68`](#insn-00bead68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beae0c`](#insn-00beae0c) → [`00bead6c`](#insn-00bead6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beae24`](#insn-00beae24) → [`00bead6c`](#insn-00bead6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beae34`](#insn-00beae34) → [`00beae50`](#insn-00beae50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beae4c`](#insn-00beae4c) → [`00beae28`](#insn-00beae28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beae54`](#insn-00beae54) → [`00bead6c`](#insn-00bead6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00beab64`](#insn-00beab64)

~~~json
{
  "source": "00beab64",
  "target": "00bead60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beab74`](#insn-00beab74)

~~~json
{
  "source": "00beab74",
  "target": "00beac54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beab80`](#insn-00beab80)

~~~json
{
  "source": "00beab80",
  "target": "00beab94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beab90`](#insn-00beab90)

~~~json
{
  "source": "00beab90",
  "target": "00beac54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beab98`](#insn-00beab98)

~~~json
{
  "source": "00beab98",
  "target": "00beab88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beabb4`](#insn-00beabb4)

~~~json
{
  "source": "00beabb4",
  "target": "00beabd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beabd4`](#insn-00beabd4)

~~~json
{
  "source": "00beabd4",
  "target": "00beabdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beabe8`](#insn-00beabe8)

~~~json
{
  "source": "00beabe8",
  "target": "00beac14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beabec`](#insn-00beabec)

~~~json
{
  "source": "00beabec",
  "target": "00beab88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beac10`](#insn-00beac10)

~~~json
{
  "source": "00beac10",
  "target": "00beab84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beac20`](#insn-00beac20)

~~~json
{
  "source": "00beac20",
  "target": "00beab84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beac3c`](#insn-00beac3c)

~~~json
{
  "source": "00beac3c",
  "target": "00beabf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beac4c`](#insn-00beac4c)

~~~json
{
  "source": "00beac4c",
  "target": "00beac14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beac50`](#insn-00beac50)

~~~json
{
  "source": "00beac50",
  "target": "00beab84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beac5c`](#insn-00beac5c)

~~~json
{
  "source": "00beac5c",
  "target": "00bead54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beac74`](#insn-00beac74)

~~~json
{
  "source": "00beac74",
  "target": "00beac88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beac84`](#insn-00beac84)

~~~json
{
  "source": "00beac84",
  "target": "00bead50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beac94`](#insn-00beac94)

~~~json
{
  "source": "00beac94",
  "target": "00beac7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaca4`](#insn-00beaca4)

~~~json
{
  "source": "00beaca4",
  "target": "00beac7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beacb0`](#insn-00beacb0)

~~~json
{
  "source": "00beacb0",
  "target": "00beacc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beacc0`](#insn-00beacc0)

~~~json
{
  "source": "00beacc0",
  "target": "00beac7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beacc4`](#insn-00beacc4)

~~~json
{
  "source": "00beacc4",
  "target": "00beace4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beace0`](#insn-00beace0)

~~~json
{
  "source": "00beace0",
  "target": "00beac7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beace8`](#insn-00beace8)

~~~json
{
  "source": "00beace8",
  "target": "00bead10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bead0c`](#insn-00bead0c)

~~~json
{
  "source": "00bead0c",
  "target": "00beac78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bead1c`](#insn-00bead1c)

~~~json
{
  "source": "00bead1c",
  "target": "00beac78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bead38`](#insn-00bead38)

~~~json
{
  "source": "00bead38",
  "target": "00beacec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bead48`](#insn-00bead48)

~~~json
{
  "source": "00bead48",
  "target": "00bead10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bead4c`](#insn-00bead4c)

~~~json
{
  "source": "00bead4c",
  "target": "00beac78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bead58`](#insn-00bead58)

~~~json
{
  "source": "00bead58",
  "target": "00bead78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bead74`](#insn-00bead74)

~~~json
{
  "source": "00bead74",
  "target": "00bead5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bead8c`](#insn-00bead8c)

~~~json
{
  "source": "00bead8c",
  "target": "00beadb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beadb4`](#insn-00beadb4)

~~~json
{
  "source": "00beadb4",
  "target": "00beade4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beadd4`](#insn-00beadd4)

~~~json
{
  "source": "00beadd4",
  "target": "00bead90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beade0`](#insn-00beade0)

~~~json
{
  "source": "00beade0",
  "target": "00beada8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beadec`](#insn-00beadec)

~~~json
{
  "source": "00beadec",
  "target": "00bead68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beae0c`](#insn-00beae0c)

~~~json
{
  "source": "00beae0c",
  "target": "00bead6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beae24`](#insn-00beae24)

~~~json
{
  "source": "00beae24",
  "target": "00bead6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beae34`](#insn-00beae34)

~~~json
{
  "source": "00beae34",
  "target": "00beae50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beae4c`](#insn-00beae4c)

~~~json
{
  "source": "00beae4c",
  "target": "00beae28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beae54`](#insn-00beae54)

~~~json
{
  "source": "00beae54",
  "target": "00bead6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
