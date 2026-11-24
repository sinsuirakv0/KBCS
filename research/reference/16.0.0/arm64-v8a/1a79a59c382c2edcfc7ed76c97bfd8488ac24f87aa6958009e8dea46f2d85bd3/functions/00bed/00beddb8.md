# 00beddb8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0175.md#review-2a5c84bb92f03675ccce97000e33c3fe)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0045.md#review-2a5c84bb92f03675ccce97000e33c3fe)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00beddb8",
  "name": "FUN_00beddb8",
  "size": 672,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9eab096f37bfea793651ba5732bad1046855dee3d7ee11e614456302826c63e8",
  "source_text_sha256": "9eab096f37bfea793651ba5732bad1046855dee3d7ee11e614456302826c63e8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00beddb8",
        "00bee057"
      ]
    ],
    "bytes_sha256": "8a1ee76f03bc978eea52dbaa7b33694bae5da5734a61d13669052b168f98e801",
    "instruction_count": 168,
    "instruction_bytes": 672,
    "body_bytes": 672,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be7400](../00be7/00be7400.md)

## 呼び出し先

- [00bee058](../00bee/00bee058.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4363 bytes

~~~c

bool FUN_00beddb8(float *param_1,float *param_2)

{
  long lVar1;
  ulong uVar2;
  float *pfVar3;
  int iVar4;
  float *pfVar5;
  float *pfVar6;
  long lVar7;
  float *pfVar8;
  long lVar9;
  float fVar10;
  float fVar11;
  float fVar12;
  float fVar13;
  float fVar14;
  
  uVar2 = (long)param_2 - (long)param_1 >> 2;
  if (2 < (long)uVar2) {
    if (uVar2 == 3) {
      fVar10 = *param_1;
      fVar12 = param_1[1];
      fVar13 = param_2[-1];
                    /* try { // try from 00bede30 to 00cee037 has its CatchHandler @ 00bed9b8 */
      if (fVar10 <= fVar12) {
        if (fVar12 <= fVar13) {
          return true;
        }
        param_1[1] = fVar13;
        param_2[-1] = fVar12;
        fVar10 = *param_1;
        if (param_1[1] < fVar10) {
          *param_1 = param_1[1];
          param_1[1] = fVar10;
          return true;
        }
        return true;
      }
      if (fVar12 <= fVar13) {
        *param_1 = fVar12;
        param_1[1] = fVar10;
        if (fVar10 <= param_2[-1]) {
          return true;
        }
        param_1[1] = param_2[-1];
      }
      else {
        *param_1 = fVar13;
      }
      goto LAB_00bee02c;
    }
    if (uVar2 != 4) {
      if (uVar2 == 5) {
        FUN_00bee058(param_1,param_1 + 1,param_1 + 2,param_1 + 3,param_2 + -1);
        return true;
      }
      goto LAB_00bede48;
    }
    fVar12 = *param_1;
    pfVar8 = param_1 + 1;
    fVar10 = *pfVar8;
    pfVar3 = param_1 + 2;
    fVar13 = *pfVar3;
    pfVar5 = param_1;
    if (fVar12 <= fVar10) {
      fVar11 = fVar13;
      if (fVar10 <= fVar13) goto LAB_00bedfdc;
      *pfVar8 = fVar13;
      *pfVar3 = fVar10;
      pfVar6 = pfVar8;
      fVar14 = fVar10;
joined_r0x00bedfc4:
      fVar11 = fVar10;
      if (fVar12 <= fVar13) goto LAB_00bedfdc;
    }
    else {
      pfVar6 = pfVar3;
      fVar14 = fVar12;
      if (fVar10 <= fVar13) {
        *param_1 = fVar10;
        param_1[1] = fVar12;
        fVar10 = fVar13;
        pfVar5 = pfVar8;
        goto joined_r0x00bedfc4;
      }
    }
    *pfVar5 = fVar13;
    *pfVar6 = fVar12;
    fVar11 = fVar14;
LAB_00bedfdc:
    if (fVar11 <= param_2[-1]) {
      return true;
    }
    *pfVar3 = param_2[-1];
    param_2[-1] = fVar11;
    fVar10 = *pfVar3;
    fVar12 = *pfVar8;
    if (fVar10 < fVar12) {
      fVar13 = *param_1;
      param_1[1] = fVar10;
      param_1[2] = fVar12;
      if (fVar10 < fVar13) {
        *param_1 = fVar10;
        param_1[1] = fVar13;
        return true;
      }
      return true;
    }
    return true;
  }
  if (uVar2 < 2) {
    return true;
  }
  if (uVar2 == 2) {
    fVar10 = *param_1;
    if (fVar10 <= param_2[-1]) {
      return true;
    }
    *param_1 = param_2[-1];
LAB_00bee02c:
    param_2[-1] = fVar10;
    return true;
  }
LAB_00bede48:
  fVar10 = *param_1;
  pfVar3 = param_1 + 1;
  fVar13 = *pfVar3;
  pfVar8 = param_1 + 2;
  fVar12 = *pfVar8;
  pfVar5 = param_1;
  if (fVar10 <= fVar13) {
    if (fVar13 <= fVar12) goto LAB_00bedf24;
    *pfVar3 = fVar12;
    *pfVar8 = fVar13;
    pfVar6 = pfVar3;
joined_r0x00bedf18:
    if (fVar10 <= fVar12) goto LAB_00bedf24;
  }
  else {
    pfVar6 = pfVar8;
    if (fVar13 <= fVar12) {
      *param_1 = fVar13;
      param_1[1] = fVar10;
      pfVar5 = pfVar3;
      goto joined_r0x00bedf18;
    }
  }
  *pfVar5 = fVar12;
  *pfVar6 = fVar10;
LAB_00bedf24:
  if (param_1 + 3 != param_2) {
    iVar4 = 0;
    lVar7 = 0xc;
    pfVar5 = param_1 + 3;
    do {
      pfVar3 = pfVar5;
      fVar10 = *pfVar3;
      fVar12 = *pfVar8;
      lVar9 = lVar7;
      if (fVar10 < fVar12) {
        do {
          lVar1 = lVar9 + -4;
          *(float *)((long)param_1 + lVar9) = fVar12;
          pfVar5 = param_1;
          if (lVar1 == 0) goto LAB_00bedf40;
          fVar12 = *(float *)((long)param_1 + lVar9 + -8);
          lVar9 = lVar1;
        } while (fVar10 < fVar12);
        pfVar5 = (float *)((long)param_1 + lVar1);
LAB_00bedf40:
        iVar4 = iVar4 + 1;
        *pfVar5 = fVar10;
        if (iVar4 == 8) {
                    /* try { // try from 00bee048 to 00cee057 has its CatchHandler @ 00bee220 */
          return pfVar3 + 1 == param_2;
        }
      }
      lVar7 = lVar7 + 4;
      pfVar5 = pfVar3 + 1;
      pfVar8 = pfVar3;
    } while (pfVar3 + 1 != param_2);
  }
                    /* try { // try from 00bee038 to 00cee043 has its CatchHandler @ 00bee230 */
  return true;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00beddb8"></a> `00beddb8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00beddbc"></a> `00beddbc` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00beddc0"></a> `00beddc0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00beddc4"></a> `00beddc4` | `28 00 00 cb` | sub x8,x1,x0 | `FALL_THROUGH`
<a id="insn-00beddc8"></a> `00beddc8` | `08 fd 42 93` | asr x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00beddcc"></a> `00beddcc` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00beddd0"></a> `00beddd0` | `4c 01 00 54` | b.gt 0x00beddf8 | `CONDITIONAL_JUMP`
<a id="insn-00beddd4"></a> `00beddd4` | `23 13 00 54` | b.cc 0x00bee038 | `CONDITIONAL_JUMP`
<a id="insn-00beddd8"></a> `00beddd8` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bedddc"></a> `00bedddc` | `61 03 00 54` | b.ne 0x00bede48 | `CONDITIONAL_JUMP`
<a id="insn-00bedde0"></a> `00bedde0` | `21 c0 5f bc` | ldur s1,[x1, #-0x4] | `FALL_THROUGH`
<a id="insn-00bedde4"></a> `00bedde4` | `00 00 40 bd` | ldr s0,[x0] | `FALL_THROUGH`
<a id="insn-00bedde8"></a> `00bedde8` | `20 20 20 1e` | fcmp s1,s0 | `FALL_THROUGH`
<a id="insn-00beddec"></a> `00beddec` | `65 12 00 54` | b.pl 0x00bee038 | `CONDITIONAL_JUMP`
<a id="insn-00beddf0"></a> `00beddf0` | `01 00 00 bd` | str s1,[x0] | `FALL_THROUGH`
<a id="insn-00beddf4"></a> `00beddf4` | `8e 00 00 14` | b 0x00bee02c | `UNCONDITIONAL_JUMP`
<a id="insn-00beddf8"></a> `00beddf8` | `1f 0d 00 f1` | cmp x8,#0x3 | `FALL_THROUGH`
<a id="insn-00beddfc"></a> `00beddfc` | `60 01 00 54` | b.eq 0x00bede28 | `CONDITIONAL_JUMP`
<a id="insn-00bede00"></a> `00bede00` | `1f 11 00 f1` | cmp x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bede04"></a> `00bede04` | `40 04 00 54` | b.eq 0x00bede8c | `CONDITIONAL_JUMP`
<a id="insn-00bede08"></a> `00bede08` | `1f 15 00 f1` | cmp x8,#0x5 | `FALL_THROUGH`
<a id="insn-00bede0c"></a> `00bede0c` | `e1 01 00 54` | b.ne 0x00bede48 | `CONDITIONAL_JUMP`
<a id="insn-00bede10"></a> `00bede10` | `24 10 00 d1` | sub x4,x1,#0x4 | `FALL_THROUGH`
<a id="insn-00bede14"></a> `00bede14` | `01 10 00 91` | add x1,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00bede18"></a> `00bede18` | `02 20 00 91` | add x2,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bede1c"></a> `00bede1c` | `03 30 00 91` | add x3,x0,#0xc | `FALL_THROUGH`
<a id="insn-00bede20"></a> `00bede20` | `8e 00 00 94` | bl 0x00bee058 | `UNCONDITIONAL_CALL`
<a id="insn-00bede24"></a> `00bede24` | `85 00 00 14` | b 0x00bee038 | `UNCONDITIONAL_JUMP`
<a id="insn-00bede28"></a> `00bede28` | `00 04 40 2d` | ldp s0,s1,[x0] | `FALL_THROUGH`
<a id="insn-00bede2c"></a> `00bede2c` | `22 c0 5f bc` | ldur s2,[x1, #-0x4] | `FALL_THROUGH`
<a id="insn-00bede30"></a> `00bede30` | `20 20 20 1e` | fcmp s1,s0 | `FALL_THROUGH`
<a id="insn-00bede34"></a> `00bede34` | `25 05 00 54` | b.pl 0x00beded8 | `CONDITIONAL_JUMP`
<a id="insn-00bede38"></a> `00bede38` | `40 20 21 1e` | fcmp s2,s1 | `FALL_THROUGH`
<a id="insn-00bede3c"></a> `00bede3c` | `e5 0e 00 54` | b.pl 0x00bee018 | `CONDITIONAL_JUMP`
<a id="insn-00bede40"></a> `00bede40` | `02 00 00 bd` | str s2,[x0] | `FALL_THROUGH`
<a id="insn-00bede44"></a> `00bede44` | `7a 00 00 14` | b 0x00bee02c | `UNCONDITIONAL_JUMP`
<a id="insn-00bede48"></a> `00bede48` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bede4c"></a> `00bede4c` | `00 00 40 bd` | ldr s0,[x0] | `FALL_THROUGH`
<a id="insn-00bede50"></a> `00bede50` | `eb 03 00 aa` | mov x11,x0 | `FALL_THROUGH`
<a id="insn-00bede54"></a> `00bede54` | `02 4d 40 bc` | ldr s2,[x8, #0x4]! | `FALL_THROUGH`
<a id="insn-00bede58"></a> `00bede58` | `61 8d 40 bc` | ldr s1,[x11, #0x8]! | `FALL_THROUGH`
<a id="insn-00bede5c"></a> `00bede5c` | `40 20 20 1e` | fcmp s2,s0 | `FALL_THROUGH`
<a id="insn-00bede60"></a> `00bede60` | `e5 04 00 54` | b.pl 0x00bedefc | `CONDITIONAL_JUMP`
<a id="insn-00bede64"></a> `00bede64` | `20 20 22 1e` | fcmp s1,s2 | `FALL_THROUGH`
<a id="insn-00bede68"></a> `00bede68` | `e9 03 00 aa` | mov x9,x0 | `FALL_THROUGH`
<a id="insn-00bede6c"></a> `00bede6c` | `ea 03 0b aa` | mov x10,x11 | `FALL_THROUGH`
<a id="insn-00bede70"></a> `00bede70` | `64 05 00 54` | b.mi 0x00bedf1c | `CONDITIONAL_JUMP`
<a id="insn-00bede74"></a> `00bede74` | `20 20 20 1e` | fcmp s1,s0 | `FALL_THROUGH`
<a id="insn-00bede78"></a> `00bede78` | `e9 03 08 aa` | mov x9,x8 | `FALL_THROUGH`
<a id="insn-00bede7c"></a> `00bede7c` | `ea 03 0b aa` | mov x10,x11 | `FALL_THROUGH`
<a id="insn-00bede80"></a> `00bede80` | `02 00 00 2d` | stp s2,s0,[x0] | `FALL_THROUGH`
<a id="insn-00bede84"></a> `00bede84` | `c4 04 00 54` | b.mi 0x00bedf1c | `CONDITIONAL_JUMP`
<a id="insn-00bede88"></a> `00bede88` | `27 00 00 14` | b 0x00bedf24 | `UNCONDITIONAL_JUMP`
<a id="insn-00bede8c"></a> `00bede8c` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bede90"></a> `00bede90` | `01 00 40 bd` | ldr s1,[x0] | `FALL_THROUGH`
<a id="insn-00bede94"></a> `00bede94` | `e9 03 00 aa` | mov x9,x0 | `FALL_THROUGH`
<a id="insn-00bede98"></a> `00bede98` | `00 4d 40 bc` | ldr s0,[x8, #0x4]! | `FALL_THROUGH`
<a id="insn-00bede9c"></a> `00bede9c` | `22 8d 40 bc` | ldr s2,[x9, #0x8]! | `FALL_THROUGH`
<a id="insn-00bedea0"></a> `00bedea0` | `00 20 21 1e` | fcmp s0,s1 | `FALL_THROUGH`
<a id="insn-00bedea4"></a> `00bedea4` | `05 08 00 54` | b.pl 0x00bedfa4 | `CONDITIONAL_JUMP`
<a id="insn-00bedea8"></a> `00bedea8` | `23 40 20 1e` | fmov s3,s1 | `FALL_THROUGH`
<a id="insn-00bedeac"></a> `00bedeac` | `40 20 20 1e` | fcmp s2,s0 | `FALL_THROUGH`
<a id="insn-00bedeb0"></a> `00bedeb0` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00bedeb4"></a> `00bedeb4` | `eb 03 09 aa` | mov x11,x9 | `FALL_THROUGH`
<a id="insn-00bedeb8"></a> `00bedeb8` | `84 08 00 54` | b.mi 0x00bedfc8 | `CONDITIONAL_JUMP`
<a id="insn-00bedebc"></a> `00bedebc` | `23 40 20 1e` | fmov s3,s1 | `FALL_THROUGH`
<a id="insn-00bedec0"></a> `00bedec0` | `40 20 21 1e` | fcmp s2,s1 | `FALL_THROUGH`
<a id="insn-00bedec4"></a> `00bedec4` | `ea 03 08 aa` | mov x10,x8 | `FALL_THROUGH`
<a id="insn-00bedec8"></a> `00bedec8` | `eb 03 09 aa` | mov x11,x9 | `FALL_THROUGH`
<a id="insn-00bedecc"></a> `00bedecc` | `00 04 00 2d` | stp s0,s1,[x0] | `FALL_THROUGH`
<a id="insn-00beded0"></a> `00beded0` | `c4 07 00 54` | b.mi 0x00bedfc8 | `CONDITIONAL_JUMP`
<a id="insn-00beded4"></a> `00beded4` | `41 00 00 14` | b 0x00bedfd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00beded8"></a> `00beded8` | `40 20 21 1e` | fcmp s2,s1 | `FALL_THROUGH`
<a id="insn-00bededc"></a> `00bededc` | `e5 0a 00 54` | b.pl 0x00bee038 | `CONDITIONAL_JUMP`
<a id="insn-00bedee0"></a> `00bedee0` | `02 04 00 bd` | str s2,[x0, #0x4] | `FALL_THROUGH`
<a id="insn-00bedee4"></a> `00bedee4` | `21 c0 1f bc` | stur s1,[x1, #-0x4] | `FALL_THROUGH`
<a id="insn-00bedee8"></a> `00bedee8` | `00 04 40 2d` | ldp s0,s1,[x0] | `FALL_THROUGH`
<a id="insn-00bedeec"></a> `00bedeec` | `20 20 20 1e` | fcmp s1,s0 | `FALL_THROUGH`
<a id="insn-00bedef0"></a> `00bedef0` | `45 0a 00 54` | b.pl 0x00bee038 | `CONDITIONAL_JUMP`
<a id="insn-00bedef4"></a> `00bedef4` | `01 00 00 2d` | stp s1,s0,[x0] | `FALL_THROUGH`
<a id="insn-00bedef8"></a> `00bedef8` | `50 00 00 14` | b 0x00bee038 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedefc"></a> `00bedefc` | `20 20 22 1e` | fcmp s1,s2 | `FALL_THROUGH`
<a id="insn-00bedf00"></a> `00bedf00` | `25 01 00 54` | b.pl 0x00bedf24 | `CONDITIONAL_JUMP`
<a id="insn-00bedf04"></a> `00bedf04` | `20 20 20 1e` | fcmp s1,s0 | `FALL_THROUGH`
<a id="insn-00bedf08"></a> `00bedf08` | `e9 03 00 aa` | mov x9,x0 | `FALL_THROUGH`
<a id="insn-00bedf0c"></a> `00bedf0c` | `ea 03 08 aa` | mov x10,x8 | `FALL_THROUGH`
<a id="insn-00bedf10"></a> `00bedf10` | `01 01 00 bd` | str s1,[x8] | `FALL_THROUGH`
<a id="insn-00bedf14"></a> `00bedf14` | `62 01 00 bd` | str s2,[x11] | `FALL_THROUGH`
<a id="insn-00bedf18"></a> `00bedf18` | `65 00 00 54` | b.pl 0x00bedf24 | `CONDITIONAL_JUMP`
<a id="insn-00bedf1c"></a> `00bedf1c` | `21 01 00 bd` | str s1,[x9] | `FALL_THROUGH`
<a id="insn-00bedf20"></a> `00bedf20` | `40 01 00 bd` | str s0,[x10] | `FALL_THROUGH`
<a id="insn-00bedf24"></a> `00bedf24` | `08 30 00 91` | add x8,x0,#0xc | `FALL_THROUGH`
<a id="insn-00bedf28"></a> `00bedf28` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00bedf2c"></a> `00bedf2c` | `60 08 00 54` | b.eq 0x00bee038 | `CONDITIONAL_JUMP`
<a id="insn-00bedf30"></a> `00bedf30` | `e9 03 1f 2a` | mov w9,wzr | `FALL_THROUGH`
<a id="insn-00bedf34"></a> `00bedf34` | `8a 01 80 52` | mov w10,#0xc | `FALL_THROUGH`
<a id="insn-00bedf38"></a> `00bedf38` | `0c 00 00 14` | b 0x00bedf68 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedf3c"></a> `00bedf3c` | `eb 03 00 aa` | mov x11,x0 | `FALL_THROUGH`
<a id="insn-00bedf40"></a> `00bedf40` | `29 05 00 11` | add w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bedf44"></a> `00bedf44` | `60 01 00 bd` | str s0,[x11] | `FALL_THROUGH`
<a id="insn-00bedf48"></a> `00bedf48` | `3f 21 00 71` | cmp w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bedf4c"></a> `00bedf4c` | `e0 07 00 54` | b.eq 0x00bee048 | `CONDITIONAL_JUMP`
<a id="insn-00bedf50"></a> `00bedf50` | `0c 11 00 91` | add x12,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bedf54"></a> `00bedf54` | `eb 03 08 aa` | mov x11,x8 | `FALL_THROUGH`
<a id="insn-00bedf58"></a> `00bedf58` | `4a 11 00 91` | add x10,x10,#0x4 | `FALL_THROUGH`
<a id="insn-00bedf5c"></a> `00bedf5c` | `9f 01 01 eb` | cmp x12,x1 | `FALL_THROUGH`
<a id="insn-00bedf60"></a> `00bedf60` | `e8 03 0c aa` | mov x8,x12 | `FALL_THROUGH`
<a id="insn-00bedf64"></a> `00bedf64` | `a0 06 00 54` | b.eq 0x00bee038 | `CONDITIONAL_JUMP`
<a id="insn-00bedf68"></a> `00bedf68` | `00 01 40 bd` | ldr s0,[x8] | `FALL_THROUGH`
<a id="insn-00bedf6c"></a> `00bedf6c` | `61 01 40 bd` | ldr s1,[x11] | `FALL_THROUGH`
<a id="insn-00bedf70"></a> `00bedf70` | `00 20 21 1e` | fcmp s0,s1 | `FALL_THROUGH`
<a id="insn-00bedf74"></a> `00bedf74` | `e5 fe ff 54` | b.pl 0x00bedf50 | `CONDITIONAL_JUMP`
<a id="insn-00bedf78"></a> `00bedf78` | `eb 03 0a aa` | mov x11,x10 | `FALL_THROUGH`
<a id="insn-00bedf7c"></a> `00bedf7c` | `6c 11 00 f1` | subs x12,x11,#0x4 | `FALL_THROUGH`
<a id="insn-00bedf80"></a> `00bedf80` | `01 68 2b bc` | str s1,[x0,x11] | `FALL_THROUGH`
<a id="insn-00bedf84"></a> `00bedf84` | `c0 fd ff 54` | b.eq 0x00bedf3c | `CONDITIONAL_JUMP`
<a id="insn-00bedf88"></a> `00bedf88` | `0b 00 0b 8b` | add x11,x0,x11 | `FALL_THROUGH`
<a id="insn-00bedf8c"></a> `00bedf8c` | `61 81 5f bc` | ldur s1,[x11, #-0x8] | `FALL_THROUGH`
<a id="insn-00bedf90"></a> `00bedf90` | `eb 03 0c aa` | mov x11,x12 | `FALL_THROUGH`
<a id="insn-00bedf94"></a> `00bedf94` | `00 20 21 1e` | fcmp s0,s1 | `FALL_THROUGH`
<a id="insn-00bedf98"></a> `00bedf98` | `24 ff ff 54` | b.mi 0x00bedf7c | `CONDITIONAL_JUMP`
<a id="insn-00bedf9c"></a> `00bedf9c` | `0b 00 0c 8b` | add x11,x0,x12 | `FALL_THROUGH`
<a id="insn-00bedfa0"></a> `00bedfa0` | `e8 ff ff 17` | b 0x00bedf40 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedfa4"></a> `00bedfa4` | `40 20 20 1e` | fcmp s2,s0 | `FALL_THROUGH`
<a id="insn-00bedfa8"></a> `00bedfa8` | `85 01 00 54` | b.pl 0x00bedfd8 | `CONDITIONAL_JUMP`
<a id="insn-00bedfac"></a> `00bedfac` | `03 40 20 1e` | fmov s3,s0 | `FALL_THROUGH`
<a id="insn-00bedfb0"></a> `00bedfb0` | `40 20 21 1e` | fcmp s2,s1 | `FALL_THROUGH`
<a id="insn-00bedfb4"></a> `00bedfb4` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00bedfb8"></a> `00bedfb8` | `eb 03 08 aa` | mov x11,x8 | `FALL_THROUGH`
<a id="insn-00bedfbc"></a> `00bedfbc` | `02 01 00 bd` | str s2,[x8] | `FALL_THROUGH`
<a id="insn-00bedfc0"></a> `00bedfc0` | `20 01 00 bd` | str s0,[x9] | `FALL_THROUGH`
<a id="insn-00bedfc4"></a> `00bedfc4` | `c5 00 00 54` | b.pl 0x00bedfdc | `CONDITIONAL_JUMP`
<a id="insn-00bedfc8"></a> `00bedfc8` | `60 40 20 1e` | fmov s0,s3 | `FALL_THROUGH`
<a id="insn-00bedfcc"></a> `00bedfcc` | `42 01 00 bd` | str s2,[x10] | `FALL_THROUGH`
<a id="insn-00bedfd0"></a> `00bedfd0` | `61 01 00 bd` | str s1,[x11] | `FALL_THROUGH`
<a id="insn-00bedfd4"></a> `00bedfd4` | `02 00 00 14` | b 0x00bedfdc | `UNCONDITIONAL_JUMP`
<a id="insn-00bedfd8"></a> `00bedfd8` | `40 40 20 1e` | fmov s0,s2 | `FALL_THROUGH`
<a id="insn-00bedfdc"></a> `00bedfdc` | `21 c0 5f bc` | ldur s1,[x1, #-0x4] | `FALL_THROUGH`
<a id="insn-00bedfe0"></a> `00bedfe0` | `20 20 20 1e` | fcmp s1,s0 | `FALL_THROUGH`
<a id="insn-00bedfe4"></a> `00bedfe4` | `a5 02 00 54` | b.pl 0x00bee038 | `CONDITIONAL_JUMP`
<a id="insn-00bedfe8"></a> `00bedfe8` | `21 01 00 bd` | str s1,[x9] | `FALL_THROUGH`
<a id="insn-00bedfec"></a> `00bedfec` | `20 c0 1f bc` | stur s0,[x1, #-0x4] | `FALL_THROUGH`
<a id="insn-00bedff0"></a> `00bedff0` | `20 01 40 bd` | ldr s0,[x9] | `FALL_THROUGH`
<a id="insn-00bedff4"></a> `00bedff4` | `01 01 40 bd` | ldr s1,[x8] | `FALL_THROUGH`
<a id="insn-00bedff8"></a> `00bedff8` | `00 20 21 1e` | fcmp s0,s1 | `FALL_THROUGH`
<a id="insn-00bedffc"></a> `00bedffc` | `e5 01 00 54` | b.pl 0x00bee038 | `CONDITIONAL_JUMP`
<a id="insn-00bee000"></a> `00bee000` | `02 00 40 bd` | ldr s2,[x0] | `FALL_THROUGH`
<a id="insn-00bee004"></a> `00bee004` | `00 84 00 2d` | stp s0,s1,[x0, #0x4] | `FALL_THROUGH`
<a id="insn-00bee008"></a> `00bee008` | `00 20 22 1e` | fcmp s0,s2 | `FALL_THROUGH`
<a id="insn-00bee00c"></a> `00bee00c` | `65 01 00 54` | b.pl 0x00bee038 | `CONDITIONAL_JUMP`
<a id="insn-00bee010"></a> `00bee010` | `00 08 00 2d` | stp s0,s2,[x0] | `FALL_THROUGH`
<a id="insn-00bee014"></a> `00bee014` | `09 00 00 14` | b 0x00bee038 | `UNCONDITIONAL_JUMP`
<a id="insn-00bee018"></a> `00bee018` | `01 00 00 2d` | stp s1,s0,[x0] | `FALL_THROUGH`
<a id="insn-00bee01c"></a> `00bee01c` | `21 c0 5f bc` | ldur s1,[x1, #-0x4] | `FALL_THROUGH`
<a id="insn-00bee020"></a> `00bee020` | `20 20 20 1e` | fcmp s1,s0 | `FALL_THROUGH`
<a id="insn-00bee024"></a> `00bee024` | `a5 00 00 54` | b.pl 0x00bee038 | `CONDITIONAL_JUMP`
<a id="insn-00bee028"></a> `00bee028` | `01 04 00 bd` | str s1,[x0, #0x4] | `FALL_THROUGH`
<a id="insn-00bee02c"></a> `00bee02c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bee030"></a> `00bee030` | `20 c0 1f bc` | stur s0,[x1, #-0x4] | `FALL_THROUGH`
<a id="insn-00bee034"></a> `00bee034` | `02 00 00 14` | b 0x00bee03c | `UNCONDITIONAL_JUMP`
<a id="insn-00bee038"></a> `00bee038` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bee03c"></a> `00bee03c` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bee040"></a> `00bee040` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bee044"></a> `00bee044` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bee048"></a> `00bee048` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bee04c"></a> `00bee04c` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00bee050"></a> `00bee050` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bee054"></a> `00bee054` | `fa ff ff 17` | b 0x00bee03c | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00beddb8`](#insn-00beddb8) 範囲 `[['00beddb8', '00beddd3']]`
  - `CONDITIONAL_JUMP` [`00beddd0`](#insn-00beddd0) → [`00beddf8`](#insn-00beddf8)
  - `FALL_THROUGH` [`00beddd0`](#insn-00beddd0) → [`00beddd4`](#insn-00beddd4)
- ブロック [`00beddd4`](#insn-00beddd4) 範囲 `[['00beddd4', '00beddd7']]`
  - `CONDITIONAL_JUMP` [`00beddd4`](#insn-00beddd4) → [`00bee038`](#insn-00bee038)
  - `FALL_THROUGH` [`00beddd4`](#insn-00beddd4) → [`00beddd8`](#insn-00beddd8)
- ブロック [`00beddd8`](#insn-00beddd8) 範囲 `[['00beddd8', '00bedddf']]`
  - `CONDITIONAL_JUMP` [`00bedddc`](#insn-00bedddc) → [`00bede48`](#insn-00bede48)
  - `FALL_THROUGH` [`00bedddc`](#insn-00bedddc) → [`00bedde0`](#insn-00bedde0)
- ブロック [`00bedde0`](#insn-00bedde0) 範囲 `[['00bedde0', '00beddef']]`
  - `CONDITIONAL_JUMP` [`00beddec`](#insn-00beddec) → [`00bee038`](#insn-00bee038)
  - `FALL_THROUGH` [`00beddec`](#insn-00beddec) → [`00beddf0`](#insn-00beddf0)
- ブロック [`00beddf0`](#insn-00beddf0) 範囲 `[['00beddf0', '00beddf7']]`
  - `UNCONDITIONAL_JUMP` [`00beddf4`](#insn-00beddf4) → [`00bee02c`](#insn-00bee02c)
- ブロック [`00beddf8`](#insn-00beddf8) 範囲 `[['00beddf8', '00beddff']]`
  - `CONDITIONAL_JUMP` [`00beddfc`](#insn-00beddfc) → [`00bede28`](#insn-00bede28)
  - `FALL_THROUGH` [`00beddfc`](#insn-00beddfc) → [`00bede00`](#insn-00bede00)
- ブロック [`00bede00`](#insn-00bede00) 範囲 `[['00bede00', '00bede07']]`
  - `CONDITIONAL_JUMP` [`00bede04`](#insn-00bede04) → [`00bede8c`](#insn-00bede8c)
  - `FALL_THROUGH` [`00bede04`](#insn-00bede04) → [`00bede08`](#insn-00bede08)
- ブロック [`00bede08`](#insn-00bede08) 範囲 `[['00bede08', '00bede0f']]`
  - `CONDITIONAL_JUMP` [`00bede0c`](#insn-00bede0c) → [`00bede48`](#insn-00bede48)
  - `FALL_THROUGH` [`00bede0c`](#insn-00bede0c) → [`00bede10`](#insn-00bede10)
- ブロック [`00bede10`](#insn-00bede10) 範囲 `[['00bede10', '00bede27']]`
  - `UNCONDITIONAL_JUMP` [`00bede24`](#insn-00bede24) → [`00bee038`](#insn-00bee038)
- ブロック [`00bede28`](#insn-00bede28) 範囲 `[['00bede28', '00bede2f']]`
  - `FALL_THROUGH` [`00bede2c`](#insn-00bede2c) → [`00bede30`](#insn-00bede30)
- ブロック [`00bede30`](#insn-00bede30) 範囲 `[['00bede30', '00bede37']]`
  - `CONDITIONAL_JUMP` [`00bede34`](#insn-00bede34) → [`00beded8`](#insn-00beded8)
  - `FALL_THROUGH` [`00bede34`](#insn-00bede34) → [`00bede38`](#insn-00bede38)
- ブロック [`00bede38`](#insn-00bede38) 範囲 `[['00bede38', '00bede3f']]`
  - `CONDITIONAL_JUMP` [`00bede3c`](#insn-00bede3c) → [`00bee018`](#insn-00bee018)
  - `FALL_THROUGH` [`00bede3c`](#insn-00bede3c) → [`00bede40`](#insn-00bede40)
- ブロック [`00bede40`](#insn-00bede40) 範囲 `[['00bede40', '00bede47']]`
  - `UNCONDITIONAL_JUMP` [`00bede44`](#insn-00bede44) → [`00bee02c`](#insn-00bee02c)
- ブロック [`00bede48`](#insn-00bede48) 範囲 `[['00bede48', '00bede63']]`
  - `CONDITIONAL_JUMP` [`00bede60`](#insn-00bede60) → [`00bedefc`](#insn-00bedefc)
  - `FALL_THROUGH` [`00bede60`](#insn-00bede60) → [`00bede64`](#insn-00bede64)
- ブロック [`00bede64`](#insn-00bede64) 範囲 `[['00bede64', '00bede73']]`
  - `CONDITIONAL_JUMP` [`00bede70`](#insn-00bede70) → [`00bedf1c`](#insn-00bedf1c)
  - `FALL_THROUGH` [`00bede70`](#insn-00bede70) → [`00bede74`](#insn-00bede74)
- ブロック [`00bede74`](#insn-00bede74) 範囲 `[['00bede74', '00bede87']]`
  - `CONDITIONAL_JUMP` [`00bede84`](#insn-00bede84) → [`00bedf1c`](#insn-00bedf1c)
  - `FALL_THROUGH` [`00bede84`](#insn-00bede84) → [`00bede88`](#insn-00bede88)
- ブロック [`00bede88`](#insn-00bede88) 範囲 `[['00bede88', '00bede8b']]`
  - `UNCONDITIONAL_JUMP` [`00bede88`](#insn-00bede88) → [`00bedf24`](#insn-00bedf24)
- ブロック [`00bede8c`](#insn-00bede8c) 範囲 `[['00bede8c', '00bedea7']]`
  - `CONDITIONAL_JUMP` [`00bedea4`](#insn-00bedea4) → [`00bedfa4`](#insn-00bedfa4)
  - `FALL_THROUGH` [`00bedea4`](#insn-00bedea4) → [`00bedea8`](#insn-00bedea8)
- ブロック [`00bedea8`](#insn-00bedea8) 範囲 `[['00bedea8', '00bedebb']]`
  - `CONDITIONAL_JUMP` [`00bedeb8`](#insn-00bedeb8) → [`00bedfc8`](#insn-00bedfc8)
  - `FALL_THROUGH` [`00bedeb8`](#insn-00bedeb8) → [`00bedebc`](#insn-00bedebc)
- ブロック [`00bedebc`](#insn-00bedebc) 範囲 `[['00bedebc', '00beded3']]`
  - `CONDITIONAL_JUMP` [`00beded0`](#insn-00beded0) → [`00bedfc8`](#insn-00bedfc8)
  - `FALL_THROUGH` [`00beded0`](#insn-00beded0) → [`00beded4`](#insn-00beded4)
- ブロック [`00beded4`](#insn-00beded4) 範囲 `[['00beded4', '00beded7']]`
  - `UNCONDITIONAL_JUMP` [`00beded4`](#insn-00beded4) → [`00bedfd8`](#insn-00bedfd8)
- ブロック [`00beded8`](#insn-00beded8) 範囲 `[['00beded8', '00bededf']]`
  - `CONDITIONAL_JUMP` [`00bededc`](#insn-00bededc) → [`00bee038`](#insn-00bee038)
  - `FALL_THROUGH` [`00bededc`](#insn-00bededc) → [`00bedee0`](#insn-00bedee0)
- ブロック [`00bedee0`](#insn-00bedee0) 範囲 `[['00bedee0', '00bedef3']]`
  - `CONDITIONAL_JUMP` [`00bedef0`](#insn-00bedef0) → [`00bee038`](#insn-00bee038)
  - `FALL_THROUGH` [`00bedef0`](#insn-00bedef0) → [`00bedef4`](#insn-00bedef4)
- ブロック [`00bedef4`](#insn-00bedef4) 範囲 `[['00bedef4', '00bedefb']]`
  - `UNCONDITIONAL_JUMP` [`00bedef8`](#insn-00bedef8) → [`00bee038`](#insn-00bee038)
- ブロック [`00bedefc`](#insn-00bedefc) 範囲 `[['00bedefc', '00bedf03']]`
  - `CONDITIONAL_JUMP` [`00bedf00`](#insn-00bedf00) → [`00bedf24`](#insn-00bedf24)
  - `FALL_THROUGH` [`00bedf00`](#insn-00bedf00) → [`00bedf04`](#insn-00bedf04)
- ブロック [`00bedf04`](#insn-00bedf04) 範囲 `[['00bedf04', '00bedf1b']]`
  - `CONDITIONAL_JUMP` [`00bedf18`](#insn-00bedf18) → [`00bedf24`](#insn-00bedf24)
  - `FALL_THROUGH` [`00bedf18`](#insn-00bedf18) → [`00bedf1c`](#insn-00bedf1c)
- ブロック [`00bedf1c`](#insn-00bedf1c) 範囲 `[['00bedf1c', '00bedf23']]`
  - `FALL_THROUGH` [`00bedf20`](#insn-00bedf20) → [`00bedf24`](#insn-00bedf24)
- ブロック [`00bedf24`](#insn-00bedf24) 範囲 `[['00bedf24', '00bedf2f']]`
  - `CONDITIONAL_JUMP` [`00bedf2c`](#insn-00bedf2c) → [`00bee038`](#insn-00bee038)
  - `FALL_THROUGH` [`00bedf2c`](#insn-00bedf2c) → [`00bedf30`](#insn-00bedf30)
- ブロック [`00bedf30`](#insn-00bedf30) 範囲 `[['00bedf30', '00bedf3b']]`
  - `UNCONDITIONAL_JUMP` [`00bedf38`](#insn-00bedf38) → [`00bedf68`](#insn-00bedf68)
- ブロック [`00bedf3c`](#insn-00bedf3c) 範囲 `[['00bedf3c', '00bedf3f']]`
  - `FALL_THROUGH` [`00bedf3c`](#insn-00bedf3c) → [`00bedf40`](#insn-00bedf40)
- ブロック [`00bedf40`](#insn-00bedf40) 範囲 `[['00bedf40', '00bedf4f']]`
  - `CONDITIONAL_JUMP` [`00bedf4c`](#insn-00bedf4c) → [`00bee048`](#insn-00bee048)
  - `FALL_THROUGH` [`00bedf4c`](#insn-00bedf4c) → [`00bedf50`](#insn-00bedf50)
- ブロック [`00bedf50`](#insn-00bedf50) 範囲 `[['00bedf50', '00bedf67']]`
  - `CONDITIONAL_JUMP` [`00bedf64`](#insn-00bedf64) → [`00bee038`](#insn-00bee038)
  - `FALL_THROUGH` [`00bedf64`](#insn-00bedf64) → [`00bedf68`](#insn-00bedf68)
- ブロック [`00bedf68`](#insn-00bedf68) 範囲 `[['00bedf68', '00bedf77']]`
  - `CONDITIONAL_JUMP` [`00bedf74`](#insn-00bedf74) → [`00bedf50`](#insn-00bedf50)
  - `FALL_THROUGH` [`00bedf74`](#insn-00bedf74) → [`00bedf78`](#insn-00bedf78)
- ブロック [`00bedf78`](#insn-00bedf78) 範囲 `[['00bedf78', '00bedf7b']]`
  - `FALL_THROUGH` [`00bedf78`](#insn-00bedf78) → [`00bedf7c`](#insn-00bedf7c)
- ブロック [`00bedf7c`](#insn-00bedf7c) 範囲 `[['00bedf7c', '00bedf87']]`
  - `CONDITIONAL_JUMP` [`00bedf84`](#insn-00bedf84) → [`00bedf3c`](#insn-00bedf3c)
  - `FALL_THROUGH` [`00bedf84`](#insn-00bedf84) → [`00bedf88`](#insn-00bedf88)
- ブロック [`00bedf88`](#insn-00bedf88) 範囲 `[['00bedf88', '00bedf9b']]`
  - `CONDITIONAL_JUMP` [`00bedf98`](#insn-00bedf98) → [`00bedf7c`](#insn-00bedf7c)
  - `FALL_THROUGH` [`00bedf98`](#insn-00bedf98) → [`00bedf9c`](#insn-00bedf9c)
- ブロック [`00bedf9c`](#insn-00bedf9c) 範囲 `[['00bedf9c', '00bedfa3']]`
  - `UNCONDITIONAL_JUMP` [`00bedfa0`](#insn-00bedfa0) → [`00bedf40`](#insn-00bedf40)
- ブロック [`00bedfa4`](#insn-00bedfa4) 範囲 `[['00bedfa4', '00bedfab']]`
  - `CONDITIONAL_JUMP` [`00bedfa8`](#insn-00bedfa8) → [`00bedfd8`](#insn-00bedfd8)
  - `FALL_THROUGH` [`00bedfa8`](#insn-00bedfa8) → [`00bedfac`](#insn-00bedfac)
- ブロック [`00bedfac`](#insn-00bedfac) 範囲 `[['00bedfac', '00bedfc7']]`
  - `CONDITIONAL_JUMP` [`00bedfc4`](#insn-00bedfc4) → [`00bedfdc`](#insn-00bedfdc)
  - `FALL_THROUGH` [`00bedfc4`](#insn-00bedfc4) → [`00bedfc8`](#insn-00bedfc8)
- ブロック [`00bedfc8`](#insn-00bedfc8) 範囲 `[['00bedfc8', '00bedfd7']]`
  - `UNCONDITIONAL_JUMP` [`00bedfd4`](#insn-00bedfd4) → [`00bedfdc`](#insn-00bedfdc)
- ブロック [`00bedfd8`](#insn-00bedfd8) 範囲 `[['00bedfd8', '00bedfdb']]`
  - `FALL_THROUGH` [`00bedfd8`](#insn-00bedfd8) → [`00bedfdc`](#insn-00bedfdc)
- ブロック [`00bedfdc`](#insn-00bedfdc) 範囲 `[['00bedfdc', '00bedfe7']]`
  - `CONDITIONAL_JUMP` [`00bedfe4`](#insn-00bedfe4) → [`00bee038`](#insn-00bee038)
  - `FALL_THROUGH` [`00bedfe4`](#insn-00bedfe4) → [`00bedfe8`](#insn-00bedfe8)
- ブロック [`00bedfe8`](#insn-00bedfe8) 範囲 `[['00bedfe8', '00bedfff']]`
  - `CONDITIONAL_JUMP` [`00bedffc`](#insn-00bedffc) → [`00bee038`](#insn-00bee038)
  - `FALL_THROUGH` [`00bedffc`](#insn-00bedffc) → [`00bee000`](#insn-00bee000)
- ブロック [`00bee000`](#insn-00bee000) 範囲 `[['00bee000', '00bee00f']]`
  - `CONDITIONAL_JUMP` [`00bee00c`](#insn-00bee00c) → [`00bee038`](#insn-00bee038)
  - `FALL_THROUGH` [`00bee00c`](#insn-00bee00c) → [`00bee010`](#insn-00bee010)
- ブロック [`00bee010`](#insn-00bee010) 範囲 `[['00bee010', '00bee017']]`
  - `UNCONDITIONAL_JUMP` [`00bee014`](#insn-00bee014) → [`00bee038`](#insn-00bee038)
- ブロック [`00bee018`](#insn-00bee018) 範囲 `[['00bee018', '00bee027']]`
  - `CONDITIONAL_JUMP` [`00bee024`](#insn-00bee024) → [`00bee038`](#insn-00bee038)
  - `FALL_THROUGH` [`00bee024`](#insn-00bee024) → [`00bee028`](#insn-00bee028)
- ブロック [`00bee028`](#insn-00bee028) 範囲 `[['00bee028', '00bee02b']]`
  - `FALL_THROUGH` [`00bee028`](#insn-00bee028) → [`00bee02c`](#insn-00bee02c)
- ブロック [`00bee02c`](#insn-00bee02c) 範囲 `[['00bee02c', '00bee037']]`
  - `UNCONDITIONAL_JUMP` [`00bee034`](#insn-00bee034) → [`00bee03c`](#insn-00bee03c)
- ブロック [`00bee038`](#insn-00bee038) 範囲 `[['00bee038', '00bee03b']]`
  - `FALL_THROUGH` [`00bee038`](#insn-00bee038) → [`00bee03c`](#insn-00bee03c)
- ブロック [`00bee03c`](#insn-00bee03c) 範囲 `[['00bee03c', '00bee047']]`
- ブロック [`00bee048`](#insn-00bee048) 範囲 `[['00bee048', '00bee057']]`
  - `UNCONDITIONAL_JUMP` [`00bee054`](#insn-00bee054) → [`00bee03c`](#insn-00bee03c)

## 命令位置別の参照

- [`00beddbc`](#insn-00beddbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beddd0`](#insn-00beddd0) → [`00beddf8`](#insn-00beddf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beddd4`](#insn-00beddd4) → [`00bee038`](#insn-00bee038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedddc`](#insn-00bedddc) → [`00bede48`](#insn-00bede48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beddec`](#insn-00beddec) → [`00bee038`](#insn-00bee038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beddf4`](#insn-00beddf4) → [`00bee02c`](#insn-00bee02c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beddfc`](#insn-00beddfc) → [`00bede28`](#insn-00bede28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bede04`](#insn-00bede04) → [`00bede8c`](#insn-00bede8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bede0c`](#insn-00bede0c) → [`00bede48`](#insn-00bede48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bede20`](#insn-00bede20) → [`00bee058`](../00bee/00bee058.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bee058` · 推定シンボル `None` · 推定型 `None`
- [`00bede24`](#insn-00bede24) → [`00bee038`](#insn-00bee038) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bede34`](#insn-00bede34) → [`00beded8`](#insn-00beded8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bede3c`](#insn-00bede3c) → [`00bee018`](#insn-00bee018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bede44`](#insn-00bede44) → [`00bee02c`](#insn-00bee02c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bede60`](#insn-00bede60) → [`00bedefc`](#insn-00bedefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bede70`](#insn-00bede70) → [`00bedf1c`](#insn-00bedf1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bede84`](#insn-00bede84) → [`00bedf1c`](#insn-00bedf1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bede88`](#insn-00bede88) → [`00bedf24`](#insn-00bedf24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedea4`](#insn-00bedea4) → [`00bedfa4`](#insn-00bedfa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedeb8`](#insn-00bedeb8) → [`00bedfc8`](#insn-00bedfc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beded0`](#insn-00beded0) → [`00bedfc8`](#insn-00bedfc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beded4`](#insn-00beded4) → [`00bedfd8`](#insn-00bedfd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bededc`](#insn-00bededc) → [`00bee038`](#insn-00bee038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedef0`](#insn-00bedef0) → [`00bee038`](#insn-00bee038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedef8`](#insn-00bedef8) → [`00bee038`](#insn-00bee038) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedf00`](#insn-00bedf00) → [`00bedf24`](#insn-00bedf24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedf18`](#insn-00bedf18) → [`00bedf24`](#insn-00bedf24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedf2c`](#insn-00bedf2c) → [`00bee038`](#insn-00bee038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedf38`](#insn-00bedf38) → [`00bedf68`](#insn-00bedf68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedf4c`](#insn-00bedf4c) → [`00bee048`](#insn-00bee048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedf64`](#insn-00bedf64) → [`00bee038`](#insn-00bee038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedf74`](#insn-00bedf74) → [`00bedf50`](#insn-00bedf50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedf84`](#insn-00bedf84) → [`00bedf3c`](#insn-00bedf3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedf98`](#insn-00bedf98) → [`00bedf7c`](#insn-00bedf7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedfa0`](#insn-00bedfa0) → [`00bedf40`](#insn-00bedf40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedfa8`](#insn-00bedfa8) → [`00bedfd8`](#insn-00bedfd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedfc4`](#insn-00bedfc4) → [`00bedfdc`](#insn-00bedfdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedfd4`](#insn-00bedfd4) → [`00bedfdc`](#insn-00bedfdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedfe4`](#insn-00bedfe4) → [`00bee038`](#insn-00bee038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedffc`](#insn-00bedffc) → [`00bee038`](#insn-00bee038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee00c`](#insn-00bee00c) → [`00bee038`](#insn-00bee038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee014`](#insn-00bee014) → [`00bee038`](#insn-00bee038) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee024`](#insn-00bee024) → [`00bee038`](#insn-00bee038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee034`](#insn-00bee034) → [`00bee03c`](#insn-00bee03c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee03c`](#insn-00bee03c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bee054`](#insn-00bee054) → [`00bee03c`](#insn-00bee03c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00beddbc`](#insn-00beddbc)

~~~json
{
  "source": "00beddbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beddd0`](#insn-00beddd0)

~~~json
{
  "source": "00beddd0",
  "target": "00beddf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beddd4`](#insn-00beddd4)

~~~json
{
  "source": "00beddd4",
  "target": "00bee038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedddc`](#insn-00bedddc)

~~~json
{
  "source": "00bedddc",
  "target": "00bede48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beddec`](#insn-00beddec)

~~~json
{
  "source": "00beddec",
  "target": "00bee038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beddf4`](#insn-00beddf4)

~~~json
{
  "source": "00beddf4",
  "target": "00bee02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beddfc`](#insn-00beddfc)

~~~json
{
  "source": "00beddfc",
  "target": "00bede28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bede04`](#insn-00bede04)

~~~json
{
  "source": "00bede04",
  "target": "00bede8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bede0c`](#insn-00bede0c)

~~~json
{
  "source": "00bede0c",
  "target": "00bede48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bede20`](#insn-00bede20)

~~~json
{
  "source": "00bede20",
  "target": "00bee058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bede24`](#insn-00bede24)

~~~json
{
  "source": "00bede24",
  "target": "00bee038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bede34`](#insn-00bede34)

~~~json
{
  "source": "00bede34",
  "target": "00beded8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bede3c`](#insn-00bede3c)

~~~json
{
  "source": "00bede3c",
  "target": "00bee018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bede44`](#insn-00bede44)

~~~json
{
  "source": "00bede44",
  "target": "00bee02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bede60`](#insn-00bede60)

~~~json
{
  "source": "00bede60",
  "target": "00bedefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bede70`](#insn-00bede70)

~~~json
{
  "source": "00bede70",
  "target": "00bedf1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bede84`](#insn-00bede84)

~~~json
{
  "source": "00bede84",
  "target": "00bedf1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bede88`](#insn-00bede88)

~~~json
{
  "source": "00bede88",
  "target": "00bedf24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedea4`](#insn-00bedea4)

~~~json
{
  "source": "00bedea4",
  "target": "00bedfa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedeb8`](#insn-00bedeb8)

~~~json
{
  "source": "00bedeb8",
  "target": "00bedfc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beded0`](#insn-00beded0)

~~~json
{
  "source": "00beded0",
  "target": "00bedfc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beded4`](#insn-00beded4)

~~~json
{
  "source": "00beded4",
  "target": "00bedfd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bededc`](#insn-00bededc)

~~~json
{
  "source": "00bededc",
  "target": "00bee038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedef0`](#insn-00bedef0)

~~~json
{
  "source": "00bedef0",
  "target": "00bee038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedef8`](#insn-00bedef8)

~~~json
{
  "source": "00bedef8",
  "target": "00bee038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedf00`](#insn-00bedf00)

~~~json
{
  "source": "00bedf00",
  "target": "00bedf24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedf18`](#insn-00bedf18)

~~~json
{
  "source": "00bedf18",
  "target": "00bedf24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedf2c`](#insn-00bedf2c)

~~~json
{
  "source": "00bedf2c",
  "target": "00bee038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedf38`](#insn-00bedf38)

~~~json
{
  "source": "00bedf38",
  "target": "00bedf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedf4c`](#insn-00bedf4c)

~~~json
{
  "source": "00bedf4c",
  "target": "00bee048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedf64`](#insn-00bedf64)

~~~json
{
  "source": "00bedf64",
  "target": "00bee038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedf74`](#insn-00bedf74)

~~~json
{
  "source": "00bedf74",
  "target": "00bedf50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedf84`](#insn-00bedf84)

~~~json
{
  "source": "00bedf84",
  "target": "00bedf3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedf98`](#insn-00bedf98)

~~~json
{
  "source": "00bedf98",
  "target": "00bedf7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedfa0`](#insn-00bedfa0)

~~~json
{
  "source": "00bedfa0",
  "target": "00bedf40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedfa8`](#insn-00bedfa8)

~~~json
{
  "source": "00bedfa8",
  "target": "00bedfd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedfc4`](#insn-00bedfc4)

~~~json
{
  "source": "00bedfc4",
  "target": "00bedfdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedfd4`](#insn-00bedfd4)

~~~json
{
  "source": "00bedfd4",
  "target": "00bedfdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedfe4`](#insn-00bedfe4)

~~~json
{
  "source": "00bedfe4",
  "target": "00bee038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedffc`](#insn-00bedffc)

~~~json
{
  "source": "00bedffc",
  "target": "00bee038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee00c`](#insn-00bee00c)

~~~json
{
  "source": "00bee00c",
  "target": "00bee038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee014`](#insn-00bee014)

~~~json
{
  "source": "00bee014",
  "target": "00bee038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee024`](#insn-00bee024)

~~~json
{
  "source": "00bee024",
  "target": "00bee038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee034`](#insn-00bee034)

~~~json
{
  "source": "00bee034",
  "target": "00bee03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee03c`](#insn-00bee03c)

~~~json
{
  "source": "00bee03c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bee054`](#insn-00bee054)

~~~json
{
  "source": "00bee054",
  "target": "00bee03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
