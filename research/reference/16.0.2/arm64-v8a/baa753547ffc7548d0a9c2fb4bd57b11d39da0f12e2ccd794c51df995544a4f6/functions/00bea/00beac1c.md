# 00beac1c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0006.md#review-99d491f5274a0ccc9a5d06931f5b27c5)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 要確認
  - [v16.0.2 → v16.0.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/review-0003.md#review-99d491f5274a0ccc9a5d06931f5b27c5)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00beac1c",
  "name": "FUN_00beac1c",
  "size": 704,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1f7386be9917f78ef3e968ca59e690499eb5a1d8ba4a544d8e663ea935976f20",
  "source_text_sha256": "1f7386be9917f78ef3e968ca59e690499eb5a1d8ba4a544d8e663ea935976f20",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00beac1c",
        "00beaedb"
      ]
    ],
    "bytes_sha256": "fa9135bba19631e3852ebdf4b361394e2254a4dd42e1739b1112c90804684cf1",
    "instruction_count": 176,
    "instruction_bytes": 704,
    "body_bytes": 704,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be3fbc](../00be3/00be3fbc.md)

## 呼び出し先

- [00beaedc](../00bea/00beaedc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4307 bytes

~~~c

bool FUN_00beac1c(short *param_1,short *param_2)

{
  short sVar1;
  long lVar2;
  short sVar3;
  short sVar4;
  ulong uVar5;
  int iVar6;
  short sVar7;
  short *psVar8;
  long lVar9;
  short sVar10;
  short *psVar11;
  short *psVar12;
  long lVar13;
  short *psVar14;
  
  uVar5 = (long)param_2 - (long)param_1 >> 1;
  if (2 < (long)uVar5) {
    if (uVar5 == 3) {
      sVar10 = param_1[1];
      sVar4 = *param_1;
      sVar1 = param_2[-1];
      if (sVar4 <= sVar10) {
        if (sVar10 <= sVar1) {
          return true;
        }
        param_1[1] = sVar1;
        param_2[-1] = sVar10;
        sVar4 = *param_1;
        if (param_1[1] < sVar4) {
          *param_1 = param_1[1];
          param_1[1] = sVar4;
          return true;
        }
        return true;
      }
      if (sVar1 < sVar10) {
        *param_1 = sVar1;
      }
      else {
        *param_1 = sVar10;
        param_1[1] = sVar4;
        if (sVar4 <= param_2[-1]) {
          return true;
        }
        param_1[1] = param_2[-1];
      }
      goto LAB_00beaeb0;
    }
    if (uVar5 != 4) {
      if (uVar5 == 5) {
        FUN_00beaedc(param_1,param_1 + 1,param_1 + 2,param_1 + 3,param_2 + -1);
        return true;
      }
      goto LAB_00beacb0;
    }
    sVar4 = *param_1;
    psVar12 = param_1 + 1;
    sVar10 = *psVar12;
    psVar8 = param_1 + 2;
    sVar1 = *psVar8;
    psVar11 = param_1;
    if (sVar10 < sVar4) {
      psVar14 = psVar8;
      sVar3 = sVar4;
      if (sVar10 <= sVar1) {
        *param_1 = sVar10;
        param_1[1] = sVar4;
        sVar10 = sVar1;
        psVar11 = psVar12;
        goto joined_r0x00beae3c;
      }
    }
    else {
      sVar7 = sVar1;
      if (sVar10 <= sVar1) goto LAB_00beae54;
      *psVar12 = sVar1;
      *psVar8 = sVar10;
      psVar14 = psVar12;
      sVar3 = sVar10;
joined_r0x00beae3c:
      sVar7 = sVar10;
      if (sVar4 <= sVar1) goto LAB_00beae54;
    }
    *psVar11 = sVar1;
    *psVar14 = sVar4;
    sVar7 = sVar3;
LAB_00beae54:
    if (sVar7 <= param_2[-1]) {
      return true;
    }
    *psVar8 = param_2[-1];
    param_2[-1] = sVar7;
    sVar4 = *psVar8;
    sVar10 = *psVar12;
    if (sVar4 < sVar10) {
      sVar1 = *param_1;
      param_1[1] = sVar4;
      param_1[2] = sVar10;
      if (sVar4 < sVar1) {
                    /* try { // try from 00beae8c to 00ceafef has its CatchHandler @ 00beae8c
                       catch() { ... } // from try @ 00beae8c with catch @ 00beae8c
                       catch() { ... } // from try @ 00beaff8 with catch @ 00beae8c */
        *param_1 = sVar4;
        param_1[1] = sVar1;
        return true;
      }
      return true;
    }
    return true;
  }
  if (uVar5 < 2) {
    return true;
  }
  if (uVar5 == 2) {
    sVar4 = *param_1;
    if (sVar4 <= param_2[-1]) {
      return true;
    }
    *param_1 = param_2[-1];
LAB_00beaeb0:
    param_2[-1] = sVar4;
    return true;
  }
LAB_00beacb0:
  sVar4 = *param_1;
  psVar8 = param_1 + 1;
  sVar10 = *psVar8;
  psVar12 = param_1 + 2;
  sVar1 = *psVar12;
  psVar11 = param_1;
  if (sVar10 < sVar4) {
    psVar14 = psVar12;
    if (sVar10 <= sVar1) {
      *param_1 = sVar10;
      param_1[1] = sVar4;
      psVar11 = psVar8;
      goto joined_r0x00bead90;
    }
  }
  else {
    if (sVar10 <= sVar1) goto LAB_00bead9c;
    *psVar8 = sVar1;
    *psVar12 = sVar10;
    psVar14 = psVar8;
joined_r0x00bead90:
    if (sVar4 <= sVar1) goto LAB_00bead9c;
  }
  *psVar11 = sVar1;
  *psVar14 = sVar4;
LAB_00bead9c:
  if (param_1 + 3 != param_2) {
    iVar6 = 0;
    lVar9 = 6;
    psVar11 = param_1 + 3;
    do {
      psVar8 = psVar11;
      sVar4 = *psVar8;
      sVar10 = *psVar12;
      lVar13 = lVar9;
      if (sVar4 < sVar10) {
        do {
          lVar2 = lVar13 + -2;
          *(short *)((long)param_1 + lVar13) = sVar10;
          psVar11 = param_1;
          if (lVar2 == 0) goto LAB_00beadb8;
          sVar10 = *(short *)((long)param_1 + lVar13 + -4);
          lVar13 = lVar2;
        } while (sVar4 < sVar10);
        psVar11 = (short *)((long)param_1 + lVar2);
LAB_00beadb8:
        iVar6 = iVar6 + 1;
        *psVar11 = sVar4;
        if (iVar6 == 8) {
          return psVar8 + 1 == param_2;
        }
      }
      lVar9 = lVar9 + 2;
      psVar11 = psVar8 + 1;
      psVar12 = psVar8;
    } while (psVar8 + 1 != param_2);
  }
  return true;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00beac1c"></a> `00beac1c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00beac20"></a> `00beac20` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00beac24"></a> `00beac24` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00beac28"></a> `00beac28` | `28 00 00 cb` | sub x8,x1,x0 | `FALL_THROUGH`
<a id="insn-00beac2c"></a> `00beac2c` | `08 fd 41 93` | asr x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00beac30"></a> `00beac30` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00beac34"></a> `00beac34` | `4c 01 00 54` | b.gt 0x00beac5c | `CONDITIONAL_JUMP`
<a id="insn-00beac38"></a> `00beac38` | `23 14 00 54` | b.cc 0x00beaebc | `CONDITIONAL_JUMP`
<a id="insn-00beac3c"></a> `00beac3c` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00beac40"></a> `00beac40` | `81 03 00 54` | b.ne 0x00beacb0 | `CONDITIONAL_JUMP`
<a id="insn-00beac44"></a> `00beac44` | `29 e0 df 78` | ldursh w9,[x1, #-0x2] | `FALL_THROUGH`
<a id="insn-00beac48"></a> `00beac48` | `08 00 c0 79` | ldrsh w8,[x0] | `FALL_THROUGH`
<a id="insn-00beac4c"></a> `00beac4c` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00beac50"></a> `00beac50` | `6a 13 00 54` | b.ge 0x00beaebc | `CONDITIONAL_JUMP`
<a id="insn-00beac54"></a> `00beac54` | `09 00 00 79` | strh w9,[x0] | `FALL_THROUGH`
<a id="insn-00beac58"></a> `00beac58` | `96 00 00 14` | b 0x00beaeb0 | `UNCONDITIONAL_JUMP`
<a id="insn-00beac5c"></a> `00beac5c` | `1f 0d 00 f1` | cmp x8,#0x3 | `FALL_THROUGH`
<a id="insn-00beac60"></a> `00beac60` | `60 01 00 54` | b.eq 0x00beac8c | `CONDITIONAL_JUMP`
<a id="insn-00beac64"></a> `00beac64` | `1f 11 00 f1` | cmp x8,#0x4 | `FALL_THROUGH`
<a id="insn-00beac68"></a> `00beac68` | `80 04 00 54` | b.eq 0x00beacf8 | `CONDITIONAL_JUMP`
<a id="insn-00beac6c"></a> `00beac6c` | `1f 15 00 f1` | cmp x8,#0x5 | `FALL_THROUGH`
<a id="insn-00beac70"></a> `00beac70` | `01 02 00 54` | b.ne 0x00beacb0 | `CONDITIONAL_JUMP`
<a id="insn-00beac74"></a> `00beac74` | `24 08 00 d1` | sub x4,x1,#0x2 | `FALL_THROUGH`
<a id="insn-00beac78"></a> `00beac78` | `01 08 00 91` | add x1,x0,#0x2 | `FALL_THROUGH`
<a id="insn-00beac7c"></a> `00beac7c` | `02 10 00 91` | add x2,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00beac80"></a> `00beac80` | `03 18 00 91` | add x3,x0,#0x6 | `FALL_THROUGH`
<a id="insn-00beac84"></a> `00beac84` | `96 00 00 94` | bl 0x00beaedc | `UNCONDITIONAL_CALL`
<a id="insn-00beac88"></a> `00beac88` | `8d 00 00 14` | b 0x00beaebc | `UNCONDITIONAL_JUMP`
<a id="insn-00beac8c"></a> `00beac8c` | `09 04 c0 79` | ldrsh w9,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00beac90"></a> `00beac90` | `08 00 c0 79` | ldrsh w8,[x0] | `FALL_THROUGH`
<a id="insn-00beac94"></a> `00beac94` | `2a e0 df 78` | ldursh w10,[x1, #-0x2] | `FALL_THROUGH`
<a id="insn-00beac98"></a> `00beac98` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00beac9c"></a> `00beac9c` | `6a 05 00 54` | b.ge 0x00bead48 | `CONDITIONAL_JUMP`
<a id="insn-00beaca0"></a> `00beaca0` | `5f 01 09 6b` | cmp w10,w9 | `FALL_THROUGH`
<a id="insn-00beaca4"></a> `00beaca4` | `aa 0f 00 54` | b.ge 0x00beae98 | `CONDITIONAL_JUMP`
<a id="insn-00beaca8"></a> `00beaca8` | `0a 00 00 79` | strh w10,[x0] | `FALL_THROUGH`
<a id="insn-00beacac"></a> `00beacac` | `81 00 00 14` | b 0x00beaeb0 | `UNCONDITIONAL_JUMP`
<a id="insn-00beacb0"></a> `00beacb0` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00beacb4"></a> `00beacb4` | `08 00 c0 79` | ldrsh w8,[x0] | `FALL_THROUGH`
<a id="insn-00beacb8"></a> `00beacb8` | `eb 03 00 aa` | mov x11,x0 | `FALL_THROUGH`
<a id="insn-00beacbc"></a> `00beacbc` | `4c 2d c0 78` | ldrsh w12,[x10, #0x2]! | `FALL_THROUGH`
<a id="insn-00beacc0"></a> `00beacc0` | `69 4d c0 78` | ldrsh w9,[x11, #0x4]! | `FALL_THROUGH`
<a id="insn-00beacc4"></a> `00beacc4` | `9f 01 08 6b` | cmp w12,w8 | `FALL_THROUGH`
<a id="insn-00beacc8"></a> `00beacc8` | `6a 05 00 54` | b.ge 0x00bead74 | `CONDITIONAL_JUMP`
<a id="insn-00beaccc"></a> `00beaccc` | `3f 01 0c 6b` | cmp w9,w12 | `FALL_THROUGH`
<a id="insn-00beacd0"></a> `00beacd0` | `ed 03 00 aa` | mov x13,x0 | `FALL_THROUGH`
<a id="insn-00beacd4"></a> `00beacd4` | `ee 03 0b aa` | mov x14,x11 | `FALL_THROUGH`
<a id="insn-00beacd8"></a> `00beacd8` | `eb 05 00 54` | b.lt 0x00bead94 | `CONDITIONAL_JUMP`
<a id="insn-00beacdc"></a> `00beacdc` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00beace0"></a> `00beace0` | `ed 03 0a aa` | mov x13,x10 | `FALL_THROUGH`
<a id="insn-00beace4"></a> `00beace4` | `ee 03 0b aa` | mov x14,x11 | `FALL_THROUGH`
<a id="insn-00beace8"></a> `00beace8` | `0c 00 00 79` | strh w12,[x0] | `FALL_THROUGH`
<a id="insn-00beacec"></a> `00beacec` | `08 04 00 79` | strh w8,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00beacf0"></a> `00beacf0` | `2b 05 00 54` | b.lt 0x00bead94 | `CONDITIONAL_JUMP`
<a id="insn-00beacf4"></a> `00beacf4` | `2a 00 00 14` | b 0x00bead9c | `UNCONDITIONAL_JUMP`
<a id="insn-00beacf8"></a> `00beacf8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00beacfc"></a> `00beacfc` | `0b 00 c0 79` | ldrsh w11,[x0] | `FALL_THROUGH`
<a id="insn-00bead00"></a> `00bead00` | `e9 03 00 aa` | mov x9,x0 | `FALL_THROUGH`
<a id="insn-00bead04"></a> `00bead04` | `0a 2d c0 78` | ldrsh w10,[x8, #0x2]! | `FALL_THROUGH`
<a id="insn-00bead08"></a> `00bead08` | `2c 4d c0 78` | ldrsh w12,[x9, #0x4]! | `FALL_THROUGH`
<a id="insn-00bead0c"></a> `00bead0c` | `5f 01 0b 6b` | cmp w10,w11 | `FALL_THROUGH`
<a id="insn-00bead10"></a> `00bead10` | `6a 08 00 54` | b.ge 0x00beae1c | `CONDITIONAL_JUMP`
<a id="insn-00bead14"></a> `00bead14` | `9f 01 0a 6b` | cmp w12,w10 | `FALL_THROUGH`
<a id="insn-00bead18"></a> `00bead18` | `ed 03 00 aa` | mov x13,x0 | `FALL_THROUGH`
<a id="insn-00bead1c"></a> `00bead1c` | `ee 03 09 aa` | mov x14,x9 | `FALL_THROUGH`
<a id="insn-00bead20"></a> `00bead20` | `e2 03 0b 2a` | mov w2,w11 | `FALL_THROUGH`
<a id="insn-00bead24"></a> `00bead24` | `eb 08 00 54` | b.lt 0x00beae40 | `CONDITIONAL_JUMP`
<a id="insn-00bead28"></a> `00bead28` | `9f 01 0b 6b` | cmp w12,w11 | `FALL_THROUGH`
<a id="insn-00bead2c"></a> `00bead2c` | `ed 03 08 aa` | mov x13,x8 | `FALL_THROUGH`
<a id="insn-00bead30"></a> `00bead30` | `ee 03 09 aa` | mov x14,x9 | `FALL_THROUGH`
<a id="insn-00bead34"></a> `00bead34` | `e2 03 0b 2a` | mov w2,w11 | `FALL_THROUGH`
<a id="insn-00bead38"></a> `00bead38` | `0a 00 00 79` | strh w10,[x0] | `FALL_THROUGH`
<a id="insn-00bead3c"></a> `00bead3c` | `0b 04 00 79` | strh w11,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00bead40"></a> `00bead40` | `0b 08 00 54` | b.lt 0x00beae40 | `CONDITIONAL_JUMP`
<a id="insn-00bead44"></a> `00bead44` | `43 00 00 14` | b 0x00beae50 | `UNCONDITIONAL_JUMP`
<a id="insn-00bead48"></a> `00bead48` | `5f 01 09 6b` | cmp w10,w9 | `FALL_THROUGH`
<a id="insn-00bead4c"></a> `00bead4c` | `8a 0b 00 54` | b.ge 0x00beaebc | `CONDITIONAL_JUMP`
<a id="insn-00bead50"></a> `00bead50` | `0a 04 00 79` | strh w10,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00bead54"></a> `00bead54` | `29 e0 1f 78` | sturh w9,[x1, #-0x2] | `FALL_THROUGH`
<a id="insn-00bead58"></a> `00bead58` | `09 04 c0 79` | ldrsh w9,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00bead5c"></a> `00bead5c` | `08 00 c0 79` | ldrsh w8,[x0] | `FALL_THROUGH`
<a id="insn-00bead60"></a> `00bead60` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00bead64"></a> `00bead64` | `ca 0a 00 54` | b.ge 0x00beaebc | `CONDITIONAL_JUMP`
<a id="insn-00bead68"></a> `00bead68` | `09 00 00 79` | strh w9,[x0] | `FALL_THROUGH`
<a id="insn-00bead6c"></a> `00bead6c` | `08 04 00 79` | strh w8,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00bead70"></a> `00bead70` | `53 00 00 14` | b 0x00beaebc | `UNCONDITIONAL_JUMP`
<a id="insn-00bead74"></a> `00bead74` | `3f 01 0c 6b` | cmp w9,w12 | `FALL_THROUGH`
<a id="insn-00bead78"></a> `00bead78` | `2a 01 00 54` | b.ge 0x00bead9c | `CONDITIONAL_JUMP`
<a id="insn-00bead7c"></a> `00bead7c` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00bead80"></a> `00bead80` | `ed 03 00 aa` | mov x13,x0 | `FALL_THROUGH`
<a id="insn-00bead84"></a> `00bead84` | `ee 03 0a aa` | mov x14,x10 | `FALL_THROUGH`
<a id="insn-00bead88"></a> `00bead88` | `49 01 00 79` | strh w9,[x10] | `FALL_THROUGH`
<a id="insn-00bead8c"></a> `00bead8c` | `6c 01 00 79` | strh w12,[x11] | `FALL_THROUGH`
<a id="insn-00bead90"></a> `00bead90` | `6a 00 00 54` | b.ge 0x00bead9c | `CONDITIONAL_JUMP`
<a id="insn-00bead94"></a> `00bead94` | `a9 01 00 79` | strh w9,[x13] | `FALL_THROUGH`
<a id="insn-00bead98"></a> `00bead98` | `c8 01 00 79` | strh w8,[x14] | `FALL_THROUGH`
<a id="insn-00bead9c"></a> `00bead9c` | `08 18 00 91` | add x8,x0,#0x6 | `FALL_THROUGH`
<a id="insn-00beada0"></a> `00beada0` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00beada4"></a> `00beada4` | `c0 08 00 54` | b.eq 0x00beaebc | `CONDITIONAL_JUMP`
<a id="insn-00beada8"></a> `00beada8` | `e9 03 1f 2a` | mov w9,wzr | `FALL_THROUGH`
<a id="insn-00beadac"></a> `00beadac` | `ca 00 80 52` | mov w10,#0x6 | `FALL_THROUGH`
<a id="insn-00beadb0"></a> `00beadb0` | `0c 00 00 14` | b 0x00beade0 | `UNCONDITIONAL_JUMP`
<a id="insn-00beadb4"></a> `00beadb4` | `eb 03 00 aa` | mov x11,x0 | `FALL_THROUGH`
<a id="insn-00beadb8"></a> `00beadb8` | `29 05 00 11` | add w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00beadbc"></a> `00beadbc` | `6c 01 00 79` | strh w12,[x11] | `FALL_THROUGH`
<a id="insn-00beadc0"></a> `00beadc0` | `3f 21 00 71` | cmp w9,#0x8 | `FALL_THROUGH`
<a id="insn-00beadc4"></a> `00beadc4` | `40 08 00 54` | b.eq 0x00beaecc | `CONDITIONAL_JUMP`
<a id="insn-00beadc8"></a> `00beadc8` | `0c 09 00 91` | add x12,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00beadcc"></a> `00beadcc` | `eb 03 08 aa` | mov x11,x8 | `FALL_THROUGH`
<a id="insn-00beadd0"></a> `00beadd0` | `4a 09 00 91` | add x10,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00beadd4"></a> `00beadd4` | `9f 01 01 eb` | cmp x12,x1 | `FALL_THROUGH`
<a id="insn-00beadd8"></a> `00beadd8` | `e8 03 0c aa` | mov x8,x12 | `FALL_THROUGH`
<a id="insn-00beaddc"></a> `00beaddc` | `00 07 00 54` | b.eq 0x00beaebc | `CONDITIONAL_JUMP`
<a id="insn-00beade0"></a> `00beade0` | `0c 01 c0 79` | ldrsh w12,[x8] | `FALL_THROUGH`
<a id="insn-00beade4"></a> `00beade4` | `6b 01 c0 79` | ldrsh w11,[x11] | `FALL_THROUGH`
<a id="insn-00beade8"></a> `00beade8` | `9f 01 0b 6b` | cmp w12,w11 | `FALL_THROUGH`
<a id="insn-00beadec"></a> `00beadec` | `ea fe ff 54` | b.ge 0x00beadc8 | `CONDITIONAL_JUMP`
<a id="insn-00beadf0"></a> `00beadf0` | `ee 03 0a aa` | mov x14,x10 | `FALL_THROUGH`
<a id="insn-00beadf4"></a> `00beadf4` | `cd 09 00 f1` | subs x13,x14,#0x2 | `FALL_THROUGH`
<a id="insn-00beadf8"></a> `00beadf8` | `0b 68 2e 78` | strh w11,[x0, x14, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00beadfc"></a> `00beadfc` | `c0 fd ff 54` | b.eq 0x00beadb4 | `CONDITIONAL_JUMP`
<a id="insn-00beae00"></a> `00beae00` | `0b 00 0e 8b` | add x11,x0,x14 | `FALL_THROUGH`
<a id="insn-00beae04"></a> `00beae04` | `ee 03 0d aa` | mov x14,x13 | `FALL_THROUGH`
<a id="insn-00beae08"></a> `00beae08` | `6b c1 df 78` | ldursh w11,[x11, #-0x4] | `FALL_THROUGH`
<a id="insn-00beae0c"></a> `00beae0c` | `9f 01 0b 6b` | cmp w12,w11 | `FALL_THROUGH`
<a id="insn-00beae10"></a> `00beae10` | `2b ff ff 54` | b.lt 0x00beadf4 | `CONDITIONAL_JUMP`
<a id="insn-00beae14"></a> `00beae14` | `0b 00 0d 8b` | add x11,x0,x13 | `FALL_THROUGH`
<a id="insn-00beae18"></a> `00beae18` | `e8 ff ff 17` | b 0x00beadb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00beae1c"></a> `00beae1c` | `9f 01 0a 6b` | cmp w12,w10 | `FALL_THROUGH`
<a id="insn-00beae20"></a> `00beae20` | `8a 01 00 54` | b.ge 0x00beae50 | `CONDITIONAL_JUMP`
<a id="insn-00beae24"></a> `00beae24` | `9f 01 0b 6b` | cmp w12,w11 | `FALL_THROUGH`
<a id="insn-00beae28"></a> `00beae28` | `ed 03 00 aa` | mov x13,x0 | `FALL_THROUGH`
<a id="insn-00beae2c"></a> `00beae2c` | `ee 03 08 aa` | mov x14,x8 | `FALL_THROUGH`
<a id="insn-00beae30"></a> `00beae30` | `e2 03 0a 2a` | mov w2,w10 | `FALL_THROUGH`
<a id="insn-00beae34"></a> `00beae34` | `0c 01 00 79` | strh w12,[x8] | `FALL_THROUGH`
<a id="insn-00beae38"></a> `00beae38` | `2a 01 00 79` | strh w10,[x9] | `FALL_THROUGH`
<a id="insn-00beae3c"></a> `00beae3c` | `ca 00 00 54` | b.ge 0x00beae54 | `CONDITIONAL_JUMP`
<a id="insn-00beae40"></a> `00beae40` | `ea 03 02 2a` | mov w10,w2 | `FALL_THROUGH`
<a id="insn-00beae44"></a> `00beae44` | `ac 01 00 79` | strh w12,[x13] | `FALL_THROUGH`
<a id="insn-00beae48"></a> `00beae48` | `cb 01 00 79` | strh w11,[x14] | `FALL_THROUGH`
<a id="insn-00beae4c"></a> `00beae4c` | `02 00 00 14` | b 0x00beae54 | `UNCONDITIONAL_JUMP`
<a id="insn-00beae50"></a> `00beae50` | `ea 03 0c 2a` | mov w10,w12 | `FALL_THROUGH`
<a id="insn-00beae54"></a> `00beae54` | `2b e0 df 78` | ldursh w11,[x1, #-0x2] | `FALL_THROUGH`
<a id="insn-00beae58"></a> `00beae58` | `7f 01 0a 6b` | cmp w11,w10 | `FALL_THROUGH`
<a id="insn-00beae5c"></a> `00beae5c` | `0a 03 00 54` | b.ge 0x00beaebc | `CONDITIONAL_JUMP`
<a id="insn-00beae60"></a> `00beae60` | `2b 01 00 79` | strh w11,[x9] | `FALL_THROUGH`
<a id="insn-00beae64"></a> `00beae64` | `2a e0 1f 78` | sturh w10,[x1, #-0x2] | `FALL_THROUGH`
<a id="insn-00beae68"></a> `00beae68` | `29 01 c0 79` | ldrsh w9,[x9] | `FALL_THROUGH`
<a id="insn-00beae6c"></a> `00beae6c` | `08 01 c0 79` | ldrsh w8,[x8] | `FALL_THROUGH`
<a id="insn-00beae70"></a> `00beae70` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00beae74"></a> `00beae74` | `4a 02 00 54` | b.ge 0x00beaebc | `CONDITIONAL_JUMP`
<a id="insn-00beae78"></a> `00beae78` | `0a 00 c0 79` | ldrsh w10,[x0] | `FALL_THROUGH`
<a id="insn-00beae7c"></a> `00beae7c` | `09 04 00 79` | strh w9,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00beae80"></a> `00beae80` | `08 08 00 79` | strh w8,[x0, #0x4] | `FALL_THROUGH`
<a id="insn-00beae84"></a> `00beae84` | `3f 01 0a 6b` | cmp w9,w10 | `FALL_THROUGH`
<a id="insn-00beae88"></a> `00beae88` | `aa 01 00 54` | b.ge 0x00beaebc | `CONDITIONAL_JUMP`
<a id="insn-00beae8c"></a> `00beae8c` | `09 00 00 79` | strh w9,[x0] | `FALL_THROUGH`
<a id="insn-00beae90"></a> `00beae90` | `0a 04 00 79` | strh w10,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00beae94"></a> `00beae94` | `0a 00 00 14` | b 0x00beaebc | `UNCONDITIONAL_JUMP`
<a id="insn-00beae98"></a> `00beae98` | `09 00 00 79` | strh w9,[x0] | `FALL_THROUGH`
<a id="insn-00beae9c"></a> `00beae9c` | `08 04 00 79` | strh w8,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00beaea0"></a> `00beaea0` | `29 e0 df 78` | ldursh w9,[x1, #-0x2] | `FALL_THROUGH`
<a id="insn-00beaea4"></a> `00beaea4` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00beaea8"></a> `00beaea8` | `aa 00 00 54` | b.ge 0x00beaebc | `CONDITIONAL_JUMP`
<a id="insn-00beaeac"></a> `00beaeac` | `09 04 00 79` | strh w9,[x0, #0x2] | `FALL_THROUGH`
<a id="insn-00beaeb0"></a> `00beaeb0` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00beaeb4"></a> `00beaeb4` | `28 e0 1f 78` | sturh w8,[x1, #-0x2] | `FALL_THROUGH`
<a id="insn-00beaeb8"></a> `00beaeb8` | `02 00 00 14` | b 0x00beaec0 | `UNCONDITIONAL_JUMP`
<a id="insn-00beaebc"></a> `00beaebc` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00beaec0"></a> `00beaec0` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00beaec4"></a> `00beaec4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00beaec8"></a> `00beaec8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00beaecc"></a> `00beaecc` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00beaed0"></a> `00beaed0` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00beaed4"></a> `00beaed4` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00beaed8"></a> `00beaed8` | `fa ff ff 17` | b 0x00beaec0 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00beac1c`](#insn-00beac1c) 範囲 `[['00beac1c', '00beac37']]`
  - `CONDITIONAL_JUMP` [`00beac34`](#insn-00beac34) → [`00beac5c`](#insn-00beac5c)
  - `FALL_THROUGH` [`00beac34`](#insn-00beac34) → [`00beac38`](#insn-00beac38)
- ブロック [`00beac38`](#insn-00beac38) 範囲 `[['00beac38', '00beac3b']]`
  - `CONDITIONAL_JUMP` [`00beac38`](#insn-00beac38) → [`00beaebc`](#insn-00beaebc)
  - `FALL_THROUGH` [`00beac38`](#insn-00beac38) → [`00beac3c`](#insn-00beac3c)
- ブロック [`00beac3c`](#insn-00beac3c) 範囲 `[['00beac3c', '00beac43']]`
  - `CONDITIONAL_JUMP` [`00beac40`](#insn-00beac40) → [`00beacb0`](#insn-00beacb0)
  - `FALL_THROUGH` [`00beac40`](#insn-00beac40) → [`00beac44`](#insn-00beac44)
- ブロック [`00beac44`](#insn-00beac44) 範囲 `[['00beac44', '00beac53']]`
  - `CONDITIONAL_JUMP` [`00beac50`](#insn-00beac50) → [`00beaebc`](#insn-00beaebc)
  - `FALL_THROUGH` [`00beac50`](#insn-00beac50) → [`00beac54`](#insn-00beac54)
- ブロック [`00beac54`](#insn-00beac54) 範囲 `[['00beac54', '00beac5b']]`
  - `UNCONDITIONAL_JUMP` [`00beac58`](#insn-00beac58) → [`00beaeb0`](#insn-00beaeb0)
- ブロック [`00beac5c`](#insn-00beac5c) 範囲 `[['00beac5c', '00beac63']]`
  - `CONDITIONAL_JUMP` [`00beac60`](#insn-00beac60) → [`00beac8c`](#insn-00beac8c)
  - `FALL_THROUGH` [`00beac60`](#insn-00beac60) → [`00beac64`](#insn-00beac64)
- ブロック [`00beac64`](#insn-00beac64) 範囲 `[['00beac64', '00beac6b']]`
  - `CONDITIONAL_JUMP` [`00beac68`](#insn-00beac68) → [`00beacf8`](#insn-00beacf8)
  - `FALL_THROUGH` [`00beac68`](#insn-00beac68) → [`00beac6c`](#insn-00beac6c)
- ブロック [`00beac6c`](#insn-00beac6c) 範囲 `[['00beac6c', '00beac73']]`
  - `CONDITIONAL_JUMP` [`00beac70`](#insn-00beac70) → [`00beacb0`](#insn-00beacb0)
  - `FALL_THROUGH` [`00beac70`](#insn-00beac70) → [`00beac74`](#insn-00beac74)
- ブロック [`00beac74`](#insn-00beac74) 範囲 `[['00beac74', '00beac8b']]`
  - `UNCONDITIONAL_JUMP` [`00beac88`](#insn-00beac88) → [`00beaebc`](#insn-00beaebc)
- ブロック [`00beac8c`](#insn-00beac8c) 範囲 `[['00beac8c', '00beac9f']]`
  - `CONDITIONAL_JUMP` [`00beac9c`](#insn-00beac9c) → [`00bead48`](#insn-00bead48)
  - `FALL_THROUGH` [`00beac9c`](#insn-00beac9c) → [`00beaca0`](#insn-00beaca0)
- ブロック [`00beaca0`](#insn-00beaca0) 範囲 `[['00beaca0', '00beaca7']]`
  - `CONDITIONAL_JUMP` [`00beaca4`](#insn-00beaca4) → [`00beae98`](#insn-00beae98)
  - `FALL_THROUGH` [`00beaca4`](#insn-00beaca4) → [`00beaca8`](#insn-00beaca8)
- ブロック [`00beaca8`](#insn-00beaca8) 範囲 `[['00beaca8', '00beacaf']]`
  - `UNCONDITIONAL_JUMP` [`00beacac`](#insn-00beacac) → [`00beaeb0`](#insn-00beaeb0)
- ブロック [`00beacb0`](#insn-00beacb0) 範囲 `[['00beacb0', '00beaccb']]`
  - `CONDITIONAL_JUMP` [`00beacc8`](#insn-00beacc8) → [`00bead74`](#insn-00bead74)
  - `FALL_THROUGH` [`00beacc8`](#insn-00beacc8) → [`00beaccc`](#insn-00beaccc)
- ブロック [`00beaccc`](#insn-00beaccc) 範囲 `[['00beaccc', '00beacdb']]`
  - `CONDITIONAL_JUMP` [`00beacd8`](#insn-00beacd8) → [`00bead94`](#insn-00bead94)
  - `FALL_THROUGH` [`00beacd8`](#insn-00beacd8) → [`00beacdc`](#insn-00beacdc)
- ブロック [`00beacdc`](#insn-00beacdc) 範囲 `[['00beacdc', '00beacf3']]`
  - `CONDITIONAL_JUMP` [`00beacf0`](#insn-00beacf0) → [`00bead94`](#insn-00bead94)
  - `FALL_THROUGH` [`00beacf0`](#insn-00beacf0) → [`00beacf4`](#insn-00beacf4)
- ブロック [`00beacf4`](#insn-00beacf4) 範囲 `[['00beacf4', '00beacf7']]`
  - `UNCONDITIONAL_JUMP` [`00beacf4`](#insn-00beacf4) → [`00bead9c`](#insn-00bead9c)
- ブロック [`00beacf8`](#insn-00beacf8) 範囲 `[['00beacf8', '00bead13']]`
  - `CONDITIONAL_JUMP` [`00bead10`](#insn-00bead10) → [`00beae1c`](#insn-00beae1c)
  - `FALL_THROUGH` [`00bead10`](#insn-00bead10) → [`00bead14`](#insn-00bead14)
- ブロック [`00bead14`](#insn-00bead14) 範囲 `[['00bead14', '00bead27']]`
  - `CONDITIONAL_JUMP` [`00bead24`](#insn-00bead24) → [`00beae40`](#insn-00beae40)
  - `FALL_THROUGH` [`00bead24`](#insn-00bead24) → [`00bead28`](#insn-00bead28)
- ブロック [`00bead28`](#insn-00bead28) 範囲 `[['00bead28', '00bead43']]`
  - `CONDITIONAL_JUMP` [`00bead40`](#insn-00bead40) → [`00beae40`](#insn-00beae40)
  - `FALL_THROUGH` [`00bead40`](#insn-00bead40) → [`00bead44`](#insn-00bead44)
- ブロック [`00bead44`](#insn-00bead44) 範囲 `[['00bead44', '00bead47']]`
  - `UNCONDITIONAL_JUMP` [`00bead44`](#insn-00bead44) → [`00beae50`](#insn-00beae50)
- ブロック [`00bead48`](#insn-00bead48) 範囲 `[['00bead48', '00bead4f']]`
  - `CONDITIONAL_JUMP` [`00bead4c`](#insn-00bead4c) → [`00beaebc`](#insn-00beaebc)
  - `FALL_THROUGH` [`00bead4c`](#insn-00bead4c) → [`00bead50`](#insn-00bead50)
- ブロック [`00bead50`](#insn-00bead50) 範囲 `[['00bead50', '00bead67']]`
  - `CONDITIONAL_JUMP` [`00bead64`](#insn-00bead64) → [`00beaebc`](#insn-00beaebc)
  - `FALL_THROUGH` [`00bead64`](#insn-00bead64) → [`00bead68`](#insn-00bead68)
- ブロック [`00bead68`](#insn-00bead68) 範囲 `[['00bead68', '00bead73']]`
  - `UNCONDITIONAL_JUMP` [`00bead70`](#insn-00bead70) → [`00beaebc`](#insn-00beaebc)
- ブロック [`00bead74`](#insn-00bead74) 範囲 `[['00bead74', '00bead7b']]`
  - `CONDITIONAL_JUMP` [`00bead78`](#insn-00bead78) → [`00bead9c`](#insn-00bead9c)
  - `FALL_THROUGH` [`00bead78`](#insn-00bead78) → [`00bead7c`](#insn-00bead7c)
- ブロック [`00bead7c`](#insn-00bead7c) 範囲 `[['00bead7c', '00bead93']]`
  - `CONDITIONAL_JUMP` [`00bead90`](#insn-00bead90) → [`00bead9c`](#insn-00bead9c)
  - `FALL_THROUGH` [`00bead90`](#insn-00bead90) → [`00bead94`](#insn-00bead94)
- ブロック [`00bead94`](#insn-00bead94) 範囲 `[['00bead94', '00bead9b']]`
  - `FALL_THROUGH` [`00bead98`](#insn-00bead98) → [`00bead9c`](#insn-00bead9c)
- ブロック [`00bead9c`](#insn-00bead9c) 範囲 `[['00bead9c', '00beada7']]`
  - `CONDITIONAL_JUMP` [`00beada4`](#insn-00beada4) → [`00beaebc`](#insn-00beaebc)
  - `FALL_THROUGH` [`00beada4`](#insn-00beada4) → [`00beada8`](#insn-00beada8)
- ブロック [`00beada8`](#insn-00beada8) 範囲 `[['00beada8', '00beadb3']]`
  - `UNCONDITIONAL_JUMP` [`00beadb0`](#insn-00beadb0) → [`00beade0`](#insn-00beade0)
- ブロック [`00beadb4`](#insn-00beadb4) 範囲 `[['00beadb4', '00beadb7']]`
  - `FALL_THROUGH` [`00beadb4`](#insn-00beadb4) → [`00beadb8`](#insn-00beadb8)
- ブロック [`00beadb8`](#insn-00beadb8) 範囲 `[['00beadb8', '00beadc7']]`
  - `CONDITIONAL_JUMP` [`00beadc4`](#insn-00beadc4) → [`00beaecc`](#insn-00beaecc)
  - `FALL_THROUGH` [`00beadc4`](#insn-00beadc4) → [`00beadc8`](#insn-00beadc8)
- ブロック [`00beadc8`](#insn-00beadc8) 範囲 `[['00beadc8', '00beaddf']]`
  - `CONDITIONAL_JUMP` [`00beaddc`](#insn-00beaddc) → [`00beaebc`](#insn-00beaebc)
  - `FALL_THROUGH` [`00beaddc`](#insn-00beaddc) → [`00beade0`](#insn-00beade0)
- ブロック [`00beade0`](#insn-00beade0) 範囲 `[['00beade0', '00beadef']]`
  - `CONDITIONAL_JUMP` [`00beadec`](#insn-00beadec) → [`00beadc8`](#insn-00beadc8)
  - `FALL_THROUGH` [`00beadec`](#insn-00beadec) → [`00beadf0`](#insn-00beadf0)
- ブロック [`00beadf0`](#insn-00beadf0) 範囲 `[['00beadf0', '00beadf3']]`
  - `FALL_THROUGH` [`00beadf0`](#insn-00beadf0) → [`00beadf4`](#insn-00beadf4)
- ブロック [`00beadf4`](#insn-00beadf4) 範囲 `[['00beadf4', '00beadff']]`
  - `CONDITIONAL_JUMP` [`00beadfc`](#insn-00beadfc) → [`00beadb4`](#insn-00beadb4)
  - `FALL_THROUGH` [`00beadfc`](#insn-00beadfc) → [`00beae00`](#insn-00beae00)
- ブロック [`00beae00`](#insn-00beae00) 範囲 `[['00beae00', '00beae13']]`
  - `CONDITIONAL_JUMP` [`00beae10`](#insn-00beae10) → [`00beadf4`](#insn-00beadf4)
  - `FALL_THROUGH` [`00beae10`](#insn-00beae10) → [`00beae14`](#insn-00beae14)
- ブロック [`00beae14`](#insn-00beae14) 範囲 `[['00beae14', '00beae1b']]`
  - `UNCONDITIONAL_JUMP` [`00beae18`](#insn-00beae18) → [`00beadb8`](#insn-00beadb8)
- ブロック [`00beae1c`](#insn-00beae1c) 範囲 `[['00beae1c', '00beae23']]`
  - `CONDITIONAL_JUMP` [`00beae20`](#insn-00beae20) → [`00beae50`](#insn-00beae50)
  - `FALL_THROUGH` [`00beae20`](#insn-00beae20) → [`00beae24`](#insn-00beae24)
- ブロック [`00beae24`](#insn-00beae24) 範囲 `[['00beae24', '00beae3f']]`
  - `CONDITIONAL_JUMP` [`00beae3c`](#insn-00beae3c) → [`00beae54`](#insn-00beae54)
  - `FALL_THROUGH` [`00beae3c`](#insn-00beae3c) → [`00beae40`](#insn-00beae40)
- ブロック [`00beae40`](#insn-00beae40) 範囲 `[['00beae40', '00beae4f']]`
  - `UNCONDITIONAL_JUMP` [`00beae4c`](#insn-00beae4c) → [`00beae54`](#insn-00beae54)
- ブロック [`00beae50`](#insn-00beae50) 範囲 `[['00beae50', '00beae53']]`
  - `FALL_THROUGH` [`00beae50`](#insn-00beae50) → [`00beae54`](#insn-00beae54)
- ブロック [`00beae54`](#insn-00beae54) 範囲 `[['00beae54', '00beae5f']]`
  - `CONDITIONAL_JUMP` [`00beae5c`](#insn-00beae5c) → [`00beaebc`](#insn-00beaebc)
  - `FALL_THROUGH` [`00beae5c`](#insn-00beae5c) → [`00beae60`](#insn-00beae60)
- ブロック [`00beae60`](#insn-00beae60) 範囲 `[['00beae60', '00beae77']]`
  - `CONDITIONAL_JUMP` [`00beae74`](#insn-00beae74) → [`00beaebc`](#insn-00beaebc)
  - `FALL_THROUGH` [`00beae74`](#insn-00beae74) → [`00beae78`](#insn-00beae78)
- ブロック [`00beae78`](#insn-00beae78) 範囲 `[['00beae78', '00beae8b']]`
  - `CONDITIONAL_JUMP` [`00beae88`](#insn-00beae88) → [`00beaebc`](#insn-00beaebc)
  - `FALL_THROUGH` [`00beae88`](#insn-00beae88) → [`00beae8c`](#insn-00beae8c)
- ブロック [`00beae8c`](#insn-00beae8c) 範囲 `[['00beae8c', '00beae97']]`
  - `UNCONDITIONAL_JUMP` [`00beae94`](#insn-00beae94) → [`00beaebc`](#insn-00beaebc)
- ブロック [`00beae98`](#insn-00beae98) 範囲 `[['00beae98', '00beaeab']]`
  - `CONDITIONAL_JUMP` [`00beaea8`](#insn-00beaea8) → [`00beaebc`](#insn-00beaebc)
  - `FALL_THROUGH` [`00beaea8`](#insn-00beaea8) → [`00beaeac`](#insn-00beaeac)
- ブロック [`00beaeac`](#insn-00beaeac) 範囲 `[['00beaeac', '00beaeaf']]`
  - `FALL_THROUGH` [`00beaeac`](#insn-00beaeac) → [`00beaeb0`](#insn-00beaeb0)
- ブロック [`00beaeb0`](#insn-00beaeb0) 範囲 `[['00beaeb0', '00beaebb']]`
  - `UNCONDITIONAL_JUMP` [`00beaeb8`](#insn-00beaeb8) → [`00beaec0`](#insn-00beaec0)
- ブロック [`00beaebc`](#insn-00beaebc) 範囲 `[['00beaebc', '00beaebf']]`
  - `FALL_THROUGH` [`00beaebc`](#insn-00beaebc) → [`00beaec0`](#insn-00beaec0)
- ブロック [`00beaec0`](#insn-00beaec0) 範囲 `[['00beaec0', '00beaecb']]`
- ブロック [`00beaecc`](#insn-00beaecc) 範囲 `[['00beaecc', '00beaedb']]`
  - `UNCONDITIONAL_JUMP` [`00beaed8`](#insn-00beaed8) → [`00beaec0`](#insn-00beaec0)

## 命令位置別の参照

- [`00beac20`](#insn-00beac20) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beac34`](#insn-00beac34) → [`00beac5c`](#insn-00beac5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beac38`](#insn-00beac38) → [`00beaebc`](#insn-00beaebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beac40`](#insn-00beac40) → [`00beacb0`](#insn-00beacb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beac50`](#insn-00beac50) → [`00beaebc`](#insn-00beaebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beac58`](#insn-00beac58) → [`00beaeb0`](#insn-00beaeb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beac60`](#insn-00beac60) → [`00beac8c`](#insn-00beac8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beac68`](#insn-00beac68) → [`00beacf8`](#insn-00beacf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beac70`](#insn-00beac70) → [`00beacb0`](#insn-00beacb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beac84`](#insn-00beac84) → [`00beaedc`](00beaedc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00beaedc` · 推定シンボル `None` · 推定型 `None`
- [`00beac88`](#insn-00beac88) → [`00beaebc`](#insn-00beaebc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beac9c`](#insn-00beac9c) → [`00bead48`](#insn-00bead48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaca4`](#insn-00beaca4) → [`00beae98`](#insn-00beae98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beacac`](#insn-00beacac) → [`00beaeb0`](#insn-00beaeb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beacc8`](#insn-00beacc8) → [`00bead74`](#insn-00bead74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beacd8`](#insn-00beacd8) → [`00bead94`](#insn-00bead94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beacf0`](#insn-00beacf0) → [`00bead94`](#insn-00bead94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beacf4`](#insn-00beacf4) → [`00bead9c`](#insn-00bead9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bead10`](#insn-00bead10) → [`00beae1c`](#insn-00beae1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bead24`](#insn-00bead24) → [`00beae40`](#insn-00beae40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bead40`](#insn-00bead40) → [`00beae40`](#insn-00beae40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bead44`](#insn-00bead44) → [`00beae50`](#insn-00beae50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bead4c`](#insn-00bead4c) → [`00beaebc`](#insn-00beaebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bead64`](#insn-00bead64) → [`00beaebc`](#insn-00beaebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bead70`](#insn-00bead70) → [`00beaebc`](#insn-00beaebc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bead78`](#insn-00bead78) → [`00bead9c`](#insn-00bead9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bead90`](#insn-00bead90) → [`00bead9c`](#insn-00bead9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beada4`](#insn-00beada4) → [`00beaebc`](#insn-00beaebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beadb0`](#insn-00beadb0) → [`00beade0`](#insn-00beade0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beadc4`](#insn-00beadc4) → [`00beaecc`](#insn-00beaecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaddc`](#insn-00beaddc) → [`00beaebc`](#insn-00beaebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beadec`](#insn-00beadec) → [`00beadc8`](#insn-00beadc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beadfc`](#insn-00beadfc) → [`00beadb4`](#insn-00beadb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beae10`](#insn-00beae10) → [`00beadf4`](#insn-00beadf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beae18`](#insn-00beae18) → [`00beadb8`](#insn-00beadb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beae20`](#insn-00beae20) → [`00beae50`](#insn-00beae50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beae3c`](#insn-00beae3c) → [`00beae54`](#insn-00beae54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beae4c`](#insn-00beae4c) → [`00beae54`](#insn-00beae54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beae5c`](#insn-00beae5c) → [`00beaebc`](#insn-00beaebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beae74`](#insn-00beae74) → [`00beaebc`](#insn-00beaebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beae88`](#insn-00beae88) → [`00beaebc`](#insn-00beaebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beae94`](#insn-00beae94) → [`00beaebc`](#insn-00beaebc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaea8`](#insn-00beaea8) → [`00beaebc`](#insn-00beaebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaeb8`](#insn-00beaeb8) → [`00beaec0`](#insn-00beaec0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaec0`](#insn-00beaec0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaed8`](#insn-00beaed8) → [`00beaec0`](#insn-00beaec0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00beac20`](#insn-00beac20)

~~~json
{
  "source": "00beac20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beac34`](#insn-00beac34)

~~~json
{
  "source": "00beac34",
  "target": "00beac5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beac38`](#insn-00beac38)

~~~json
{
  "source": "00beac38",
  "target": "00beaebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beac40`](#insn-00beac40)

~~~json
{
  "source": "00beac40",
  "target": "00beacb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beac50`](#insn-00beac50)

~~~json
{
  "source": "00beac50",
  "target": "00beaebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beac58`](#insn-00beac58)

~~~json
{
  "source": "00beac58",
  "target": "00beaeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beac60`](#insn-00beac60)

~~~json
{
  "source": "00beac60",
  "target": "00beac8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beac68`](#insn-00beac68)

~~~json
{
  "source": "00beac68",
  "target": "00beacf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beac70`](#insn-00beac70)

~~~json
{
  "source": "00beac70",
  "target": "00beacb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beac84`](#insn-00beac84)

~~~json
{
  "source": "00beac84",
  "target": "00beaedc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beac88`](#insn-00beac88)

~~~json
{
  "source": "00beac88",
  "target": "00beaebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beac9c`](#insn-00beac9c)

~~~json
{
  "source": "00beac9c",
  "target": "00bead48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaca4`](#insn-00beaca4)

~~~json
{
  "source": "00beaca4",
  "target": "00beae98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beacac`](#insn-00beacac)

~~~json
{
  "source": "00beacac",
  "target": "00beaeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beacc8`](#insn-00beacc8)

~~~json
{
  "source": "00beacc8",
  "target": "00bead74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beacd8`](#insn-00beacd8)

~~~json
{
  "source": "00beacd8",
  "target": "00bead94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beacf0`](#insn-00beacf0)

~~~json
{
  "source": "00beacf0",
  "target": "00bead94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beacf4`](#insn-00beacf4)

~~~json
{
  "source": "00beacf4",
  "target": "00bead9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bead10`](#insn-00bead10)

~~~json
{
  "source": "00bead10",
  "target": "00beae1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bead24`](#insn-00bead24)

~~~json
{
  "source": "00bead24",
  "target": "00beae40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bead40`](#insn-00bead40)

~~~json
{
  "source": "00bead40",
  "target": "00beae40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bead44`](#insn-00bead44)

~~~json
{
  "source": "00bead44",
  "target": "00beae50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bead4c`](#insn-00bead4c)

~~~json
{
  "source": "00bead4c",
  "target": "00beaebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bead64`](#insn-00bead64)

~~~json
{
  "source": "00bead64",
  "target": "00beaebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bead70`](#insn-00bead70)

~~~json
{
  "source": "00bead70",
  "target": "00beaebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bead78`](#insn-00bead78)

~~~json
{
  "source": "00bead78",
  "target": "00bead9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bead90`](#insn-00bead90)

~~~json
{
  "source": "00bead90",
  "target": "00bead9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beada4`](#insn-00beada4)

~~~json
{
  "source": "00beada4",
  "target": "00beaebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beadb0`](#insn-00beadb0)

~~~json
{
  "source": "00beadb0",
  "target": "00beade0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beadc4`](#insn-00beadc4)

~~~json
{
  "source": "00beadc4",
  "target": "00beaecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaddc`](#insn-00beaddc)

~~~json
{
  "source": "00beaddc",
  "target": "00beaebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beadec`](#insn-00beadec)

~~~json
{
  "source": "00beadec",
  "target": "00beadc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beadfc`](#insn-00beadfc)

~~~json
{
  "source": "00beadfc",
  "target": "00beadb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beae10`](#insn-00beae10)

~~~json
{
  "source": "00beae10",
  "target": "00beadf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beae18`](#insn-00beae18)

~~~json
{
  "source": "00beae18",
  "target": "00beadb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beae20`](#insn-00beae20)

~~~json
{
  "source": "00beae20",
  "target": "00beae50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beae3c`](#insn-00beae3c)

~~~json
{
  "source": "00beae3c",
  "target": "00beae54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beae4c`](#insn-00beae4c)

~~~json
{
  "source": "00beae4c",
  "target": "00beae54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beae5c`](#insn-00beae5c)

~~~json
{
  "source": "00beae5c",
  "target": "00beaebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beae74`](#insn-00beae74)

~~~json
{
  "source": "00beae74",
  "target": "00beaebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beae88`](#insn-00beae88)

~~~json
{
  "source": "00beae88",
  "target": "00beaebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beae94`](#insn-00beae94)

~~~json
{
  "source": "00beae94",
  "target": "00beaebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaea8`](#insn-00beaea8)

~~~json
{
  "source": "00beaea8",
  "target": "00beaebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaeb8`](#insn-00beaeb8)

~~~json
{
  "source": "00beaeb8",
  "target": "00beaec0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaec0`](#insn-00beaec0)

~~~json
{
  "source": "00beaec0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaed8`](#insn-00beaed8)

~~~json
{
  "source": "00beaed8",
  "target": "00beaec0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
