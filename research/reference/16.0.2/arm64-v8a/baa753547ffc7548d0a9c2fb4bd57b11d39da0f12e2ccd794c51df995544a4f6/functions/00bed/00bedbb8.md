# 00bedbb8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0082.md#review-2f620d5d89229bc05ded7a14d4e124c2)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 要確認
  - [v16.0.2 → v16.0.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/review-0044.md#review-2f620d5d89229bc05ded7a14d4e124c2)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bedbb8",
  "name": "FUN_00bedbb8",
  "size": 672,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fde264796bd08401ddd50d154cff0c3089f2bd109fc6964ea19fc7be43088ec0",
  "source_text_sha256": "fde264796bd08401ddd50d154cff0c3089f2bd109fc6964ea19fc7be43088ec0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bedbb8",
        "00bede57"
      ]
    ],
    "bytes_sha256": "c4f8ca832dfc5c48cf28509b6f6dc14e62c359d18a8a870b97a0274be4f133eb",
    "instruction_count": 168,
    "instruction_bytes": 672,
    "body_bytes": 672,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be71ac](../00be7/00be71ac.md)

## 呼び出し先

- [00bede58](../00bed/00bede58.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4555 bytes

~~~c

bool FUN_00bedbb8(ulong *param_1,ulong *param_2)

{
  long lVar1;
  ulong uVar2;
  ulong uVar3;
  int iVar4;
  ulong uVar5;
  ulong *puVar6;
  long lVar7;
  ulong uVar8;
  ulong *puVar9;
  ulong *puVar10;
  ulong uVar11;
  long lVar12;
  ulong *puVar13;
  
  uVar3 = (long)param_2 - (long)param_1 >> 3;
  if (2 < (long)uVar3) {
    if (uVar3 == 3) {
      uVar3 = *param_1;
      uVar5 = param_1[1];
      uVar11 = param_2[-1];
      if (uVar3 <= uVar5) {
        if (uVar5 <= uVar11) {
          return true;
        }
        param_1[1] = uVar11;
        param_2[-1] = uVar5;
        uVar3 = *param_1;
        if (param_1[1] < uVar3) {
          *param_1 = param_1[1];
          param_1[1] = uVar3;
          return true;
        }
        return true;
      }
      if (uVar11 < uVar5) {
        *param_1 = uVar11;
      }
      else {
        *param_1 = uVar5;
        param_1[1] = uVar3;
        if (uVar3 <= param_2[-1]) {
          return true;
        }
        param_1[1] = param_2[-1];
      }
      goto LAB_00bede2c;
    }
    if (uVar3 != 4) {
      if (uVar3 == 5) {
        FUN_00bede58(param_1,param_1 + 1,param_1 + 2,param_1 + 3,param_2 + -1);
        return true;
      }
      goto LAB_00bedc48;
    }
    uVar5 = *param_1;
    puVar10 = param_1 + 1;
    uVar3 = *puVar10;
    puVar6 = param_1 + 2;
    uVar11 = *puVar6;
    puVar9 = param_1;
    if (uVar3 < uVar5) {
      uVar2 = uVar5;
      puVar13 = puVar6;
                    /* try { // try from 00bedcb4 to 00cedcbb has its CatchHandler @ 00bedd0c */
      if (uVar3 <= uVar11) {
                    /* try { // try from 00bedcbc to 00ceddff has its CatchHandler @ 00bed9ec */
        *param_1 = uVar3;
        param_1[1] = uVar5;
        uVar3 = uVar11;
        puVar9 = puVar10;
        goto joined_r0x00beddc4;
      }
    }
    else {
      uVar8 = uVar11;
      if (uVar3 <= uVar11) goto LAB_00bedddc;
      *puVar10 = uVar11;
      *puVar6 = uVar3;
      puVar13 = puVar10;
      uVar2 = uVar3;
joined_r0x00beddc4:
      uVar8 = uVar3;
      if (uVar5 <= uVar11) goto LAB_00bedddc;
    }
    *puVar9 = uVar11;
    *puVar13 = uVar5;
    uVar8 = uVar2;
LAB_00bedddc:
                    /* catch() { ... } // from try @ 00beda9c with catch @ 00bedde0 */
    if (uVar8 <= param_2[-1]) {
      return true;
    }
    *puVar6 = param_2[-1];
    param_2[-1] = uVar8;
    uVar5 = *puVar6;
    uVar3 = *puVar10;
    if (uVar5 < uVar3) {
      uVar11 = *param_1;
      param_1[1] = uVar5;
      param_1[2] = uVar3;
      if (uVar5 < uVar11) {
        *param_1 = uVar5;
        param_1[1] = uVar11;
        return true;
      }
      return true;
    }
    return true;
  }
  if (uVar3 < 2) {
    return true;
  }
  if (uVar3 == 2) {
    uVar3 = *param_1;
    if (uVar3 <= param_2[-1]) {
      return true;
    }
    *param_1 = param_2[-1];
LAB_00bede2c:
    param_2[-1] = uVar3;
    return true;
  }
LAB_00bedc48:
  uVar3 = *param_1;
  puVar6 = param_1 + 1;
  uVar11 = *puVar6;
  puVar10 = param_1 + 2;
  uVar5 = *puVar10;
  puVar9 = param_1;
  if (uVar11 < uVar3) {
    puVar13 = puVar10;
    if (uVar11 <= uVar5) {
      *param_1 = uVar11;
      param_1[1] = uVar3;
      puVar9 = puVar6;
      goto joined_r0x00bedd18;
    }
  }
  else {
    if (uVar11 <= uVar5) goto LAB_00bedd24;
                    /* catch() { ... } // from try @ 00bedcb4 with catch @ 00bedd0c */
    *puVar6 = uVar5;
    *puVar10 = uVar11;
    puVar13 = puVar6;
joined_r0x00bedd18:
    if (uVar3 <= uVar5) goto LAB_00bedd24;
  }
  *puVar9 = uVar5;
  *puVar13 = uVar3;
LAB_00bedd24:
  if (param_1 + 3 != param_2) {
    iVar4 = 0;
    lVar7 = 0x18;
    puVar9 = param_1 + 3;
    do {
      puVar6 = puVar9;
      uVar5 = *puVar6;
      uVar3 = *puVar10;
      lVar12 = lVar7;
      if (uVar5 < uVar3) {
        do {
          lVar1 = lVar12 + -8;
          *(ulong *)((long)param_1 + lVar12) = uVar3;
          puVar9 = param_1;
          if (lVar1 == 0) goto LAB_00bedd40;
          uVar3 = *(ulong *)((long)param_1 + lVar12 + -0x10);
          lVar12 = lVar1;
        } while (uVar5 < uVar3);
        puVar9 = (ulong *)((long)param_1 + lVar1);
LAB_00bedd40:
        iVar4 = iVar4 + 1;
                    /* catch() { ... } // from try @ 00beda90 with catch @ 00bedd44 */
        *puVar9 = uVar5;
        if (iVar4 == 8) {
          return puVar6 + 1 == param_2;
        }
      }
                    /* catch() { ... } // from try @ 00bedad8 with catch @ 00bedd54 */
      lVar7 = lVar7 + 8;
      puVar9 = puVar6 + 1;
      puVar10 = puVar6;
    } while (puVar6 + 1 != param_2);
  }
  return true;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bedbb8"></a> `00bedbb8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bedbbc"></a> `00bedbbc` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bedbc0"></a> `00bedbc0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bedbc4"></a> `00bedbc4` | `28 00 00 cb` | sub x8,x1,x0 | `FALL_THROUGH`
<a id="insn-00bedbc8"></a> `00bedbc8` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bedbcc"></a> `00bedbcc` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bedbd0"></a> `00bedbd0` | `4c 01 00 54` | b.gt 0x00bedbf8 | `CONDITIONAL_JUMP`
<a id="insn-00bedbd4"></a> `00bedbd4` | `23 13 00 54` | b.cc 0x00bede38 | `CONDITIONAL_JUMP`
<a id="insn-00bedbd8"></a> `00bedbd8` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bedbdc"></a> `00bedbdc` | `61 03 00 54` | b.ne 0x00bedc48 | `CONDITIONAL_JUMP`
<a id="insn-00bedbe0"></a> `00bedbe0` | `29 80 5f f8` | ldur x9,[x1, #-0x8] | `FALL_THROUGH`
<a id="insn-00bedbe4"></a> `00bedbe4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bedbe8"></a> `00bedbe8` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bedbec"></a> `00bedbec` | `62 12 00 54` | b.cs 0x00bede38 | `CONDITIONAL_JUMP`
<a id="insn-00bedbf0"></a> `00bedbf0` | `09 00 00 f9` | str x9,[x0] | `FALL_THROUGH`
<a id="insn-00bedbf4"></a> `00bedbf4` | `8e 00 00 14` | b 0x00bede2c | `UNCONDITIONAL_JUMP`
<a id="insn-00bedbf8"></a> `00bedbf8` | `1f 0d 00 f1` | cmp x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bedbfc"></a> `00bedbfc` | `60 01 00 54` | b.eq 0x00bedc28 | `CONDITIONAL_JUMP`
<a id="insn-00bedc00"></a> `00bedc00` | `1f 11 00 f1` | cmp x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bedc04"></a> `00bedc04` | `40 04 00 54` | b.eq 0x00bedc8c | `CONDITIONAL_JUMP`
<a id="insn-00bedc08"></a> `00bedc08` | `1f 15 00 f1` | cmp x8,#0x5 | `FALL_THROUGH`
<a id="insn-00bedc0c"></a> `00bedc0c` | `e1 01 00 54` | b.ne 0x00bedc48 | `CONDITIONAL_JUMP`
<a id="insn-00bedc10"></a> `00bedc10` | `24 20 00 d1` | sub x4,x1,#0x8 | `FALL_THROUGH`
<a id="insn-00bedc14"></a> `00bedc14` | `01 20 00 91` | add x1,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bedc18"></a> `00bedc18` | `02 40 00 91` | add x2,x0,#0x10 | `FALL_THROUGH`
<a id="insn-00bedc1c"></a> `00bedc1c` | `03 60 00 91` | add x3,x0,#0x18 | `FALL_THROUGH`
<a id="insn-00bedc20"></a> `00bedc20` | `8e 00 00 94` | bl 0x00bede58 | `UNCONDITIONAL_CALL`
<a id="insn-00bedc24"></a> `00bedc24` | `85 00 00 14` | b 0x00bede38 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedc28"></a> `00bedc28` | `08 24 40 a9` | ldp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00bedc2c"></a> `00bedc2c` | `2a 80 5f f8` | ldur x10,[x1, #-0x8] | `FALL_THROUGH`
<a id="insn-00bedc30"></a> `00bedc30` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bedc34"></a> `00bedc34` | `22 05 00 54` | b.cs 0x00bedcd8 | `CONDITIONAL_JUMP`
<a id="insn-00bedc38"></a> `00bedc38` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bedc3c"></a> `00bedc3c` | `e2 0e 00 54` | b.cs 0x00bede18 | `CONDITIONAL_JUMP`
<a id="insn-00bedc40"></a> `00bedc40` | `0a 00 00 f9` | str x10,[x0] | `FALL_THROUGH`
<a id="insn-00bedc44"></a> `00bedc44` | `7a 00 00 14` | b 0x00bede2c | `UNCONDITIONAL_JUMP`
<a id="insn-00bedc48"></a> `00bedc48` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00bedc4c"></a> `00bedc4c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bedc50"></a> `00bedc50` | `eb 03 00 aa` | mov x11,x0 | `FALL_THROUGH`
<a id="insn-00bedc54"></a> `00bedc54` | `4c 8d 40 f8` | ldr x12,[x10, #0x8]! | `FALL_THROUGH`
<a id="insn-00bedc58"></a> `00bedc58` | `69 0d 41 f8` | ldr x9,[x11, #0x10]! | `FALL_THROUGH`
<a id="insn-00bedc5c"></a> `00bedc5c` | `9f 01 08 eb` | cmp x12,x8 | `FALL_THROUGH`
<a id="insn-00bedc60"></a> `00bedc60` | `e2 04 00 54` | b.cs 0x00bedcfc | `CONDITIONAL_JUMP`
<a id="insn-00bedc64"></a> `00bedc64` | `3f 01 0c eb` | cmp x9,x12 | `FALL_THROUGH`
<a id="insn-00bedc68"></a> `00bedc68` | `ed 03 00 aa` | mov x13,x0 | `FALL_THROUGH`
<a id="insn-00bedc6c"></a> `00bedc6c` | `ee 03 0b aa` | mov x14,x11 | `FALL_THROUGH`
<a id="insn-00bedc70"></a> `00bedc70` | `63 05 00 54` | b.cc 0x00bedd1c | `CONDITIONAL_JUMP`
<a id="insn-00bedc74"></a> `00bedc74` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bedc78"></a> `00bedc78` | `ed 03 0a aa` | mov x13,x10 | `FALL_THROUGH`
<a id="insn-00bedc7c"></a> `00bedc7c` | `ee 03 0b aa` | mov x14,x11 | `FALL_THROUGH`
<a id="insn-00bedc80"></a> `00bedc80` | `0c 20 00 a9` | stp x12,x8,[x0] | `FALL_THROUGH`
<a id="insn-00bedc84"></a> `00bedc84` | `c3 04 00 54` | b.cc 0x00bedd1c | `CONDITIONAL_JUMP`
<a id="insn-00bedc88"></a> `00bedc88` | `27 00 00 14` | b 0x00bedd24 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedc8c"></a> `00bedc8c` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bedc90"></a> `00bedc90` | `0b 00 40 f9` | ldr x11,[x0] | `FALL_THROUGH`
<a id="insn-00bedc94"></a> `00bedc94` | `e9 03 00 aa` | mov x9,x0 | `FALL_THROUGH`
<a id="insn-00bedc98"></a> `00bedc98` | `0a 8d 40 f8` | ldr x10,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00bedc9c"></a> `00bedc9c` | `2c 0d 41 f8` | ldr x12,[x9, #0x10]! | `FALL_THROUGH`
<a id="insn-00bedca0"></a> `00bedca0` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-00bedca4"></a> `00bedca4` | `02 08 00 54` | b.cs 0x00bedda4 | `CONDITIONAL_JUMP`
<a id="insn-00bedca8"></a> `00bedca8` | `9f 01 0a eb` | cmp x12,x10 | `FALL_THROUGH`
<a id="insn-00bedcac"></a> `00bedcac` | `ed 03 00 aa` | mov x13,x0 | `FALL_THROUGH`
<a id="insn-00bedcb0"></a> `00bedcb0` | `ee 03 09 aa` | mov x14,x9 | `FALL_THROUGH`
<a id="insn-00bedcb4"></a> `00bedcb4` | `e2 03 0b aa` | mov x2,x11 | `FALL_THROUGH`
<a id="insn-00bedcb8"></a> `00bedcb8` | `83 08 00 54` | b.cc 0x00beddc8 | `CONDITIONAL_JUMP`
<a id="insn-00bedcbc"></a> `00bedcbc` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bedcc0"></a> `00bedcc0` | `ed 03 08 aa` | mov x13,x8 | `FALL_THROUGH`
<a id="insn-00bedcc4"></a> `00bedcc4` | `ee 03 09 aa` | mov x14,x9 | `FALL_THROUGH`
<a id="insn-00bedcc8"></a> `00bedcc8` | `e2 03 0b aa` | mov x2,x11 | `FALL_THROUGH`
<a id="insn-00bedccc"></a> `00bedccc` | `0a 2c 00 a9` | stp x10,x11,[x0] | `FALL_THROUGH`
<a id="insn-00bedcd0"></a> `00bedcd0` | `c3 07 00 54` | b.cc 0x00beddc8 | `CONDITIONAL_JUMP`
<a id="insn-00bedcd4"></a> `00bedcd4` | `41 00 00 14` | b 0x00beddd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedcd8"></a> `00bedcd8` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bedcdc"></a> `00bedcdc` | `e2 0a 00 54` | b.cs 0x00bede38 | `CONDITIONAL_JUMP`
<a id="insn-00bedce0"></a> `00bedce0` | `0a 04 00 f9` | str x10,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bedce4"></a> `00bedce4` | `29 80 1f f8` | stur x9,[x1, #-0x8] | `FALL_THROUGH`
<a id="insn-00bedce8"></a> `00bedce8` | `08 24 40 a9` | ldp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00bedcec"></a> `00bedcec` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bedcf0"></a> `00bedcf0` | `42 0a 00 54` | b.cs 0x00bede38 | `CONDITIONAL_JUMP`
<a id="insn-00bedcf4"></a> `00bedcf4` | `09 20 00 a9` | stp x9,x8,[x0] | `FALL_THROUGH`
<a id="insn-00bedcf8"></a> `00bedcf8` | `50 00 00 14` | b 0x00bede38 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedcfc"></a> `00bedcfc` | `3f 01 0c eb` | cmp x9,x12 | `FALL_THROUGH`
<a id="insn-00bedd00"></a> `00bedd00` | `22 01 00 54` | b.cs 0x00bedd24 | `CONDITIONAL_JUMP`
<a id="insn-00bedd04"></a> `00bedd04` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bedd08"></a> `00bedd08` | `ed 03 00 aa` | mov x13,x0 | `FALL_THROUGH`
<a id="insn-00bedd0c"></a> `00bedd0c` | `ee 03 0a aa` | mov x14,x10 | `FALL_THROUGH`
<a id="insn-00bedd10"></a> `00bedd10` | `49 01 00 f9` | str x9,[x10] | `FALL_THROUGH`
<a id="insn-00bedd14"></a> `00bedd14` | `6c 01 00 f9` | str x12,[x11] | `FALL_THROUGH`
<a id="insn-00bedd18"></a> `00bedd18` | `62 00 00 54` | b.cs 0x00bedd24 | `CONDITIONAL_JUMP`
<a id="insn-00bedd1c"></a> `00bedd1c` | `a9 01 00 f9` | str x9,[x13] | `FALL_THROUGH`
<a id="insn-00bedd20"></a> `00bedd20` | `c8 01 00 f9` | str x8,[x14] | `FALL_THROUGH`
<a id="insn-00bedd24"></a> `00bedd24` | `08 60 00 91` | add x8,x0,#0x18 | `FALL_THROUGH`
<a id="insn-00bedd28"></a> `00bedd28` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00bedd2c"></a> `00bedd2c` | `60 08 00 54` | b.eq 0x00bede38 | `CONDITIONAL_JUMP`
<a id="insn-00bedd30"></a> `00bedd30` | `e9 03 1f 2a` | mov w9,wzr | `FALL_THROUGH`
<a id="insn-00bedd34"></a> `00bedd34` | `0a 03 80 52` | mov w10,#0x18 | `FALL_THROUGH`
<a id="insn-00bedd38"></a> `00bedd38` | `0c 00 00 14` | b 0x00bedd68 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedd3c"></a> `00bedd3c` | `eb 03 00 aa` | mov x11,x0 | `FALL_THROUGH`
<a id="insn-00bedd40"></a> `00bedd40` | `29 05 00 11` | add w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bedd44"></a> `00bedd44` | `6c 01 00 f9` | str x12,[x11] | `FALL_THROUGH`
<a id="insn-00bedd48"></a> `00bedd48` | `3f 21 00 71` | cmp w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bedd4c"></a> `00bedd4c` | `e0 07 00 54` | b.eq 0x00bede48 | `CONDITIONAL_JUMP`
<a id="insn-00bedd50"></a> `00bedd50` | `0c 21 00 91` | add x12,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bedd54"></a> `00bedd54` | `eb 03 08 aa` | mov x11,x8 | `FALL_THROUGH`
<a id="insn-00bedd58"></a> `00bedd58` | `4a 21 00 91` | add x10,x10,#0x8 | `FALL_THROUGH`
<a id="insn-00bedd5c"></a> `00bedd5c` | `9f 01 01 eb` | cmp x12,x1 | `FALL_THROUGH`
<a id="insn-00bedd60"></a> `00bedd60` | `e8 03 0c aa` | mov x8,x12 | `FALL_THROUGH`
<a id="insn-00bedd64"></a> `00bedd64` | `a0 06 00 54` | b.eq 0x00bede38 | `CONDITIONAL_JUMP`
<a id="insn-00bedd68"></a> `00bedd68` | `0c 01 40 f9` | ldr x12,[x8] | `FALL_THROUGH`
<a id="insn-00bedd6c"></a> `00bedd6c` | `6b 01 40 f9` | ldr x11,[x11] | `FALL_THROUGH`
<a id="insn-00bedd70"></a> `00bedd70` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bedd74"></a> `00bedd74` | `e2 fe ff 54` | b.cs 0x00bedd50 | `CONDITIONAL_JUMP`
<a id="insn-00bedd78"></a> `00bedd78` | `ee 03 0a aa` | mov x14,x10 | `FALL_THROUGH`
<a id="insn-00bedd7c"></a> `00bedd7c` | `cd 21 00 f1` | subs x13,x14,#0x8 | `FALL_THROUGH`
<a id="insn-00bedd80"></a> `00bedd80` | `0b 68 2e f8` | str x11,[x0, x14, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bedd84"></a> `00bedd84` | `c0 fd ff 54` | b.eq 0x00bedd3c | `CONDITIONAL_JUMP`
<a id="insn-00bedd88"></a> `00bedd88` | `0b 00 0e 8b` | add x11,x0,x14 | `FALL_THROUGH`
<a id="insn-00bedd8c"></a> `00bedd8c` | `ee 03 0d aa` | mov x14,x13 | `FALL_THROUGH`
<a id="insn-00bedd90"></a> `00bedd90` | `6b 01 5f f8` | ldur x11,[x11, #-0x10] | `FALL_THROUGH`
<a id="insn-00bedd94"></a> `00bedd94` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bedd98"></a> `00bedd98` | `23 ff ff 54` | b.cc 0x00bedd7c | `CONDITIONAL_JUMP`
<a id="insn-00bedd9c"></a> `00bedd9c` | `0b 00 0d 8b` | add x11,x0,x13 | `FALL_THROUGH`
<a id="insn-00bedda0"></a> `00bedda0` | `e8 ff ff 17` | b 0x00bedd40 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedda4"></a> `00bedda4` | `9f 01 0a eb` | cmp x12,x10 | `FALL_THROUGH`
<a id="insn-00bedda8"></a> `00bedda8` | `82 01 00 54` | b.cs 0x00beddd8 | `CONDITIONAL_JUMP`
<a id="insn-00beddac"></a> `00beddac` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00beddb0"></a> `00beddb0` | `ed 03 00 aa` | mov x13,x0 | `FALL_THROUGH`
<a id="insn-00beddb4"></a> `00beddb4` | `ee 03 08 aa` | mov x14,x8 | `FALL_THROUGH`
<a id="insn-00beddb8"></a> `00beddb8` | `e2 03 0a aa` | mov x2,x10 | `FALL_THROUGH`
<a id="insn-00beddbc"></a> `00beddbc` | `0c 01 00 f9` | str x12,[x8] | `FALL_THROUGH`
<a id="insn-00beddc0"></a> `00beddc0` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00beddc4"></a> `00beddc4` | `c2 00 00 54` | b.cs 0x00bedddc | `CONDITIONAL_JUMP`
<a id="insn-00beddc8"></a> `00beddc8` | `ea 03 02 aa` | mov x10,x2 | `FALL_THROUGH`
<a id="insn-00beddcc"></a> `00beddcc` | `ac 01 00 f9` | str x12,[x13] | `FALL_THROUGH`
<a id="insn-00beddd0"></a> `00beddd0` | `cb 01 00 f9` | str x11,[x14] | `FALL_THROUGH`
<a id="insn-00beddd4"></a> `00beddd4` | `02 00 00 14` | b 0x00bedddc | `UNCONDITIONAL_JUMP`
<a id="insn-00beddd8"></a> `00beddd8` | `ea 03 0c aa` | mov x10,x12 | `FALL_THROUGH`
<a id="insn-00bedddc"></a> `00bedddc` | `2b 80 5f f8` | ldur x11,[x1, #-0x8] | `FALL_THROUGH`
<a id="insn-00bedde0"></a> `00bedde0` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bedde4"></a> `00bedde4` | `a2 02 00 54` | b.cs 0x00bede38 | `CONDITIONAL_JUMP`
<a id="insn-00bedde8"></a> `00bedde8` | `2b 01 00 f9` | str x11,[x9] | `FALL_THROUGH`
<a id="insn-00beddec"></a> `00beddec` | `2a 80 1f f8` | stur x10,[x1, #-0x8] | `FALL_THROUGH`
<a id="insn-00beddf0"></a> `00beddf0` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00beddf4"></a> `00beddf4` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00beddf8"></a> `00beddf8` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00beddfc"></a> `00beddfc` | `e2 01 00 54` | b.cs 0x00bede38 | `CONDITIONAL_JUMP`
<a id="insn-00bede00"></a> `00bede00` | `0a 00 40 f9` | ldr x10,[x0] | `FALL_THROUGH`
<a id="insn-00bede04"></a> `00bede04` | `09 a0 00 a9` | stp x9,x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bede08"></a> `00bede08` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bede0c"></a> `00bede0c` | `62 01 00 54` | b.cs 0x00bede38 | `CONDITIONAL_JUMP`
<a id="insn-00bede10"></a> `00bede10` | `09 28 00 a9` | stp x9,x10,[x0] | `FALL_THROUGH`
<a id="insn-00bede14"></a> `00bede14` | `09 00 00 14` | b 0x00bede38 | `UNCONDITIONAL_JUMP`
<a id="insn-00bede18"></a> `00bede18` | `09 20 00 a9` | stp x9,x8,[x0] | `FALL_THROUGH`
<a id="insn-00bede1c"></a> `00bede1c` | `29 80 5f f8` | ldur x9,[x1, #-0x8] | `FALL_THROUGH`
<a id="insn-00bede20"></a> `00bede20` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bede24"></a> `00bede24` | `a2 00 00 54` | b.cs 0x00bede38 | `CONDITIONAL_JUMP`
<a id="insn-00bede28"></a> `00bede28` | `09 04 00 f9` | str x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bede2c"></a> `00bede2c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bede30"></a> `00bede30` | `28 80 1f f8` | stur x8,[x1, #-0x8] | `FALL_THROUGH`
<a id="insn-00bede34"></a> `00bede34` | `02 00 00 14` | b 0x00bede3c | `UNCONDITIONAL_JUMP`
<a id="insn-00bede38"></a> `00bede38` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bede3c"></a> `00bede3c` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bede40"></a> `00bede40` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bede44"></a> `00bede44` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bede48"></a> `00bede48` | `08 21 00 91` | add x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bede4c"></a> `00bede4c` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00bede50"></a> `00bede50` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bede54"></a> `00bede54` | `fa ff ff 17` | b 0x00bede3c | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bedbb8`](#insn-00bedbb8) 範囲 `[['00bedbb8', '00bedbd3']]`
  - `CONDITIONAL_JUMP` [`00bedbd0`](#insn-00bedbd0) → [`00bedbf8`](#insn-00bedbf8)
  - `FALL_THROUGH` [`00bedbd0`](#insn-00bedbd0) → [`00bedbd4`](#insn-00bedbd4)
- ブロック [`00bedbd4`](#insn-00bedbd4) 範囲 `[['00bedbd4', '00bedbd7']]`
  - `CONDITIONAL_JUMP` [`00bedbd4`](#insn-00bedbd4) → [`00bede38`](#insn-00bede38)
  - `FALL_THROUGH` [`00bedbd4`](#insn-00bedbd4) → [`00bedbd8`](#insn-00bedbd8)
- ブロック [`00bedbd8`](#insn-00bedbd8) 範囲 `[['00bedbd8', '00bedbdf']]`
  - `CONDITIONAL_JUMP` [`00bedbdc`](#insn-00bedbdc) → [`00bedc48`](#insn-00bedc48)
  - `FALL_THROUGH` [`00bedbdc`](#insn-00bedbdc) → [`00bedbe0`](#insn-00bedbe0)
- ブロック [`00bedbe0`](#insn-00bedbe0) 範囲 `[['00bedbe0', '00bedbef']]`
  - `CONDITIONAL_JUMP` [`00bedbec`](#insn-00bedbec) → [`00bede38`](#insn-00bede38)
  - `FALL_THROUGH` [`00bedbec`](#insn-00bedbec) → [`00bedbf0`](#insn-00bedbf0)
- ブロック [`00bedbf0`](#insn-00bedbf0) 範囲 `[['00bedbf0', '00bedbf7']]`
  - `UNCONDITIONAL_JUMP` [`00bedbf4`](#insn-00bedbf4) → [`00bede2c`](#insn-00bede2c)
- ブロック [`00bedbf8`](#insn-00bedbf8) 範囲 `[['00bedbf8', '00bedbff']]`
  - `CONDITIONAL_JUMP` [`00bedbfc`](#insn-00bedbfc) → [`00bedc28`](#insn-00bedc28)
  - `FALL_THROUGH` [`00bedbfc`](#insn-00bedbfc) → [`00bedc00`](#insn-00bedc00)
- ブロック [`00bedc00`](#insn-00bedc00) 範囲 `[['00bedc00', '00bedc07']]`
  - `CONDITIONAL_JUMP` [`00bedc04`](#insn-00bedc04) → [`00bedc8c`](#insn-00bedc8c)
  - `FALL_THROUGH` [`00bedc04`](#insn-00bedc04) → [`00bedc08`](#insn-00bedc08)
- ブロック [`00bedc08`](#insn-00bedc08) 範囲 `[['00bedc08', '00bedc0f']]`
  - `CONDITIONAL_JUMP` [`00bedc0c`](#insn-00bedc0c) → [`00bedc48`](#insn-00bedc48)
  - `FALL_THROUGH` [`00bedc0c`](#insn-00bedc0c) → [`00bedc10`](#insn-00bedc10)
- ブロック [`00bedc10`](#insn-00bedc10) 範囲 `[['00bedc10', '00bedc27']]`
  - `UNCONDITIONAL_JUMP` [`00bedc24`](#insn-00bedc24) → [`00bede38`](#insn-00bede38)
- ブロック [`00bedc28`](#insn-00bedc28) 範囲 `[['00bedc28', '00bedc37']]`
  - `CONDITIONAL_JUMP` [`00bedc34`](#insn-00bedc34) → [`00bedcd8`](#insn-00bedcd8)
  - `FALL_THROUGH` [`00bedc34`](#insn-00bedc34) → [`00bedc38`](#insn-00bedc38)
- ブロック [`00bedc38`](#insn-00bedc38) 範囲 `[['00bedc38', '00bedc3f']]`
  - `CONDITIONAL_JUMP` [`00bedc3c`](#insn-00bedc3c) → [`00bede18`](#insn-00bede18)
  - `FALL_THROUGH` [`00bedc3c`](#insn-00bedc3c) → [`00bedc40`](#insn-00bedc40)
- ブロック [`00bedc40`](#insn-00bedc40) 範囲 `[['00bedc40', '00bedc47']]`
  - `UNCONDITIONAL_JUMP` [`00bedc44`](#insn-00bedc44) → [`00bede2c`](#insn-00bede2c)
- ブロック [`00bedc48`](#insn-00bedc48) 範囲 `[['00bedc48', '00bedc63']]`
  - `CONDITIONAL_JUMP` [`00bedc60`](#insn-00bedc60) → [`00bedcfc`](#insn-00bedcfc)
  - `FALL_THROUGH` [`00bedc60`](#insn-00bedc60) → [`00bedc64`](#insn-00bedc64)
- ブロック [`00bedc64`](#insn-00bedc64) 範囲 `[['00bedc64', '00bedc73']]`
  - `CONDITIONAL_JUMP` [`00bedc70`](#insn-00bedc70) → [`00bedd1c`](#insn-00bedd1c)
  - `FALL_THROUGH` [`00bedc70`](#insn-00bedc70) → [`00bedc74`](#insn-00bedc74)
- ブロック [`00bedc74`](#insn-00bedc74) 範囲 `[['00bedc74', '00bedc87']]`
  - `CONDITIONAL_JUMP` [`00bedc84`](#insn-00bedc84) → [`00bedd1c`](#insn-00bedd1c)
  - `FALL_THROUGH` [`00bedc84`](#insn-00bedc84) → [`00bedc88`](#insn-00bedc88)
- ブロック [`00bedc88`](#insn-00bedc88) 範囲 `[['00bedc88', '00bedc8b']]`
  - `UNCONDITIONAL_JUMP` [`00bedc88`](#insn-00bedc88) → [`00bedd24`](#insn-00bedd24)
- ブロック [`00bedc8c`](#insn-00bedc8c) 範囲 `[['00bedc8c', '00bedca7']]`
  - `CONDITIONAL_JUMP` [`00bedca4`](#insn-00bedca4) → [`00bedda4`](#insn-00bedda4)
  - `FALL_THROUGH` [`00bedca4`](#insn-00bedca4) → [`00bedca8`](#insn-00bedca8)
- ブロック [`00bedca8`](#insn-00bedca8) 範囲 `[['00bedca8', '00bedcb3']]`
  - `FALL_THROUGH` [`00bedcb0`](#insn-00bedcb0) → [`00bedcb4`](#insn-00bedcb4)
- ブロック [`00bedcb4`](#insn-00bedcb4) 範囲 `[['00bedcb4', '00bedcbb']]`
  - `CONDITIONAL_JUMP` [`00bedcb8`](#insn-00bedcb8) → [`00beddc8`](#insn-00beddc8)
  - `FALL_THROUGH` [`00bedcb8`](#insn-00bedcb8) → [`00bedcbc`](#insn-00bedcbc)
- ブロック [`00bedcbc`](#insn-00bedcbc) 範囲 `[['00bedcbc', '00bedcd3']]`
  - `CONDITIONAL_JUMP` [`00bedcd0`](#insn-00bedcd0) → [`00beddc8`](#insn-00beddc8)
  - `FALL_THROUGH` [`00bedcd0`](#insn-00bedcd0) → [`00bedcd4`](#insn-00bedcd4)
- ブロック [`00bedcd4`](#insn-00bedcd4) 範囲 `[['00bedcd4', '00bedcd7']]`
  - `UNCONDITIONAL_JUMP` [`00bedcd4`](#insn-00bedcd4) → [`00beddd8`](#insn-00beddd8)
- ブロック [`00bedcd8`](#insn-00bedcd8) 範囲 `[['00bedcd8', '00bedcdf']]`
  - `CONDITIONAL_JUMP` [`00bedcdc`](#insn-00bedcdc) → [`00bede38`](#insn-00bede38)
  - `FALL_THROUGH` [`00bedcdc`](#insn-00bedcdc) → [`00bedce0`](#insn-00bedce0)
- ブロック [`00bedce0`](#insn-00bedce0) 範囲 `[['00bedce0', '00bedcf3']]`
  - `CONDITIONAL_JUMP` [`00bedcf0`](#insn-00bedcf0) → [`00bede38`](#insn-00bede38)
  - `FALL_THROUGH` [`00bedcf0`](#insn-00bedcf0) → [`00bedcf4`](#insn-00bedcf4)
- ブロック [`00bedcf4`](#insn-00bedcf4) 範囲 `[['00bedcf4', '00bedcfb']]`
  - `UNCONDITIONAL_JUMP` [`00bedcf8`](#insn-00bedcf8) → [`00bede38`](#insn-00bede38)
- ブロック [`00bedcfc`](#insn-00bedcfc) 範囲 `[['00bedcfc', '00bedd03']]`
  - `CONDITIONAL_JUMP` [`00bedd00`](#insn-00bedd00) → [`00bedd24`](#insn-00bedd24)
  - `FALL_THROUGH` [`00bedd00`](#insn-00bedd00) → [`00bedd04`](#insn-00bedd04)
- ブロック [`00bedd04`](#insn-00bedd04) 範囲 `[['00bedd04', '00bedd0b']]`
  - `FALL_THROUGH` [`00bedd08`](#insn-00bedd08) → [`00bedd0c`](#insn-00bedd0c)
- ブロック [`00bedd0c`](#insn-00bedd0c) 範囲 `[['00bedd0c', '00bedd1b']]`
  - `CONDITIONAL_JUMP` [`00bedd18`](#insn-00bedd18) → [`00bedd24`](#insn-00bedd24)
  - `FALL_THROUGH` [`00bedd18`](#insn-00bedd18) → [`00bedd1c`](#insn-00bedd1c)
- ブロック [`00bedd1c`](#insn-00bedd1c) 範囲 `[['00bedd1c', '00bedd23']]`
  - `FALL_THROUGH` [`00bedd20`](#insn-00bedd20) → [`00bedd24`](#insn-00bedd24)
- ブロック [`00bedd24`](#insn-00bedd24) 範囲 `[['00bedd24', '00bedd2f']]`
  - `CONDITIONAL_JUMP` [`00bedd2c`](#insn-00bedd2c) → [`00bede38`](#insn-00bede38)
  - `FALL_THROUGH` [`00bedd2c`](#insn-00bedd2c) → [`00bedd30`](#insn-00bedd30)
- ブロック [`00bedd30`](#insn-00bedd30) 範囲 `[['00bedd30', '00bedd3b']]`
  - `UNCONDITIONAL_JUMP` [`00bedd38`](#insn-00bedd38) → [`00bedd68`](#insn-00bedd68)
- ブロック [`00bedd3c`](#insn-00bedd3c) 範囲 `[['00bedd3c', '00bedd3f']]`
  - `FALL_THROUGH` [`00bedd3c`](#insn-00bedd3c) → [`00bedd40`](#insn-00bedd40)
- ブロック [`00bedd40`](#insn-00bedd40) 範囲 `[['00bedd40', '00bedd43']]`
  - `FALL_THROUGH` [`00bedd40`](#insn-00bedd40) → [`00bedd44`](#insn-00bedd44)
- ブロック [`00bedd44`](#insn-00bedd44) 範囲 `[['00bedd44', '00bedd4f']]`
  - `CONDITIONAL_JUMP` [`00bedd4c`](#insn-00bedd4c) → [`00bede48`](#insn-00bede48)
  - `FALL_THROUGH` [`00bedd4c`](#insn-00bedd4c) → [`00bedd50`](#insn-00bedd50)
- ブロック [`00bedd50`](#insn-00bedd50) 範囲 `[['00bedd50', '00bedd53']]`
  - `FALL_THROUGH` [`00bedd50`](#insn-00bedd50) → [`00bedd54`](#insn-00bedd54)
- ブロック [`00bedd54`](#insn-00bedd54) 範囲 `[['00bedd54', '00bedd67']]`
  - `CONDITIONAL_JUMP` [`00bedd64`](#insn-00bedd64) → [`00bede38`](#insn-00bede38)
  - `FALL_THROUGH` [`00bedd64`](#insn-00bedd64) → [`00bedd68`](#insn-00bedd68)
- ブロック [`00bedd68`](#insn-00bedd68) 範囲 `[['00bedd68', '00bedd77']]`
  - `CONDITIONAL_JUMP` [`00bedd74`](#insn-00bedd74) → [`00bedd50`](#insn-00bedd50)
  - `FALL_THROUGH` [`00bedd74`](#insn-00bedd74) → [`00bedd78`](#insn-00bedd78)
- ブロック [`00bedd78`](#insn-00bedd78) 範囲 `[['00bedd78', '00bedd7b']]`
  - `FALL_THROUGH` [`00bedd78`](#insn-00bedd78) → [`00bedd7c`](#insn-00bedd7c)
- ブロック [`00bedd7c`](#insn-00bedd7c) 範囲 `[['00bedd7c', '00bedd87']]`
  - `CONDITIONAL_JUMP` [`00bedd84`](#insn-00bedd84) → [`00bedd3c`](#insn-00bedd3c)
  - `FALL_THROUGH` [`00bedd84`](#insn-00bedd84) → [`00bedd88`](#insn-00bedd88)
- ブロック [`00bedd88`](#insn-00bedd88) 範囲 `[['00bedd88', '00bedd9b']]`
  - `CONDITIONAL_JUMP` [`00bedd98`](#insn-00bedd98) → [`00bedd7c`](#insn-00bedd7c)
  - `FALL_THROUGH` [`00bedd98`](#insn-00bedd98) → [`00bedd9c`](#insn-00bedd9c)
- ブロック [`00bedd9c`](#insn-00bedd9c) 範囲 `[['00bedd9c', '00bedda3']]`
  - `UNCONDITIONAL_JUMP` [`00bedda0`](#insn-00bedda0) → [`00bedd40`](#insn-00bedd40)
- ブロック [`00bedda4`](#insn-00bedda4) 範囲 `[['00bedda4', '00beddab']]`
  - `CONDITIONAL_JUMP` [`00bedda8`](#insn-00bedda8) → [`00beddd8`](#insn-00beddd8)
  - `FALL_THROUGH` [`00bedda8`](#insn-00bedda8) → [`00beddac`](#insn-00beddac)
- ブロック [`00beddac`](#insn-00beddac) 範囲 `[['00beddac', '00beddc7']]`
  - `CONDITIONAL_JUMP` [`00beddc4`](#insn-00beddc4) → [`00bedddc`](#insn-00bedddc)
  - `FALL_THROUGH` [`00beddc4`](#insn-00beddc4) → [`00beddc8`](#insn-00beddc8)
- ブロック [`00beddc8`](#insn-00beddc8) 範囲 `[['00beddc8', '00beddd7']]`
  - `UNCONDITIONAL_JUMP` [`00beddd4`](#insn-00beddd4) → [`00bedddc`](#insn-00bedddc)
- ブロック [`00beddd8`](#insn-00beddd8) 範囲 `[['00beddd8', '00bedddb']]`
  - `FALL_THROUGH` [`00beddd8`](#insn-00beddd8) → [`00bedddc`](#insn-00bedddc)
- ブロック [`00bedddc`](#insn-00bedddc) 範囲 `[['00bedddc', '00bedddf']]`
  - `FALL_THROUGH` [`00bedddc`](#insn-00bedddc) → [`00bedde0`](#insn-00bedde0)
- ブロック [`00bedde0`](#insn-00bedde0) 範囲 `[['00bedde0', '00bedde7']]`
  - `CONDITIONAL_JUMP` [`00bedde4`](#insn-00bedde4) → [`00bede38`](#insn-00bede38)
  - `FALL_THROUGH` [`00bedde4`](#insn-00bedde4) → [`00bedde8`](#insn-00bedde8)
- ブロック [`00bedde8`](#insn-00bedde8) 範囲 `[['00bedde8', '00beddff']]`
  - `CONDITIONAL_JUMP` [`00beddfc`](#insn-00beddfc) → [`00bede38`](#insn-00bede38)
  - `FALL_THROUGH` [`00beddfc`](#insn-00beddfc) → [`00bede00`](#insn-00bede00)
- ブロック [`00bede00`](#insn-00bede00) 範囲 `[['00bede00', '00bede0f']]`
  - `CONDITIONAL_JUMP` [`00bede0c`](#insn-00bede0c) → [`00bede38`](#insn-00bede38)
  - `FALL_THROUGH` [`00bede0c`](#insn-00bede0c) → [`00bede10`](#insn-00bede10)
- ブロック [`00bede10`](#insn-00bede10) 範囲 `[['00bede10', '00bede17']]`
  - `UNCONDITIONAL_JUMP` [`00bede14`](#insn-00bede14) → [`00bede38`](#insn-00bede38)
- ブロック [`00bede18`](#insn-00bede18) 範囲 `[['00bede18', '00bede27']]`
  - `CONDITIONAL_JUMP` [`00bede24`](#insn-00bede24) → [`00bede38`](#insn-00bede38)
  - `FALL_THROUGH` [`00bede24`](#insn-00bede24) → [`00bede28`](#insn-00bede28)
- ブロック [`00bede28`](#insn-00bede28) 範囲 `[['00bede28', '00bede2b']]`
  - `FALL_THROUGH` [`00bede28`](#insn-00bede28) → [`00bede2c`](#insn-00bede2c)
- ブロック [`00bede2c`](#insn-00bede2c) 範囲 `[['00bede2c', '00bede37']]`
  - `UNCONDITIONAL_JUMP` [`00bede34`](#insn-00bede34) → [`00bede3c`](#insn-00bede3c)
- ブロック [`00bede38`](#insn-00bede38) 範囲 `[['00bede38', '00bede3b']]`
  - `FALL_THROUGH` [`00bede38`](#insn-00bede38) → [`00bede3c`](#insn-00bede3c)
- ブロック [`00bede3c`](#insn-00bede3c) 範囲 `[['00bede3c', '00bede47']]`
- ブロック [`00bede48`](#insn-00bede48) 範囲 `[['00bede48', '00bede57']]`
  - `UNCONDITIONAL_JUMP` [`00bede54`](#insn-00bede54) → [`00bede3c`](#insn-00bede3c)

## 命令位置別の参照

- [`00bedbbc`](#insn-00bedbbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedbd0`](#insn-00bedbd0) → [`00bedbf8`](#insn-00bedbf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedbd4`](#insn-00bedbd4) → [`00bede38`](#insn-00bede38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedbdc`](#insn-00bedbdc) → [`00bedc48`](#insn-00bedc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedbec`](#insn-00bedbec) → [`00bede38`](#insn-00bede38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedbf4`](#insn-00bedbf4) → [`00bede2c`](#insn-00bede2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedbfc`](#insn-00bedbfc) → [`00bedc28`](#insn-00bedc28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc04`](#insn-00bedc04) → [`00bedc8c`](#insn-00bedc8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc0c`](#insn-00bedc0c) → [`00bedc48`](#insn-00bedc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc20`](#insn-00bedc20) → [`00bede58`](00bede58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bede58` · 推定シンボル `None` · 推定型 `None`
- [`00bedc24`](#insn-00bedc24) → [`00bede38`](#insn-00bede38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc34`](#insn-00bedc34) → [`00bedcd8`](#insn-00bedcd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc3c`](#insn-00bedc3c) → [`00bede18`](#insn-00bede18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc44`](#insn-00bedc44) → [`00bede2c`](#insn-00bede2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc60`](#insn-00bedc60) → [`00bedcfc`](#insn-00bedcfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc70`](#insn-00bedc70) → [`00bedd1c`](#insn-00bedd1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc84`](#insn-00bedc84) → [`00bedd1c`](#insn-00bedd1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc88`](#insn-00bedc88) → [`00bedd24`](#insn-00bedd24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedca4`](#insn-00bedca4) → [`00bedda4`](#insn-00bedda4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedcb8`](#insn-00bedcb8) → [`00beddc8`](#insn-00beddc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedcd0`](#insn-00bedcd0) → [`00beddc8`](#insn-00beddc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedcd4`](#insn-00bedcd4) → [`00beddd8`](#insn-00beddd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedcdc`](#insn-00bedcdc) → [`00bede38`](#insn-00bede38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedcf0`](#insn-00bedcf0) → [`00bede38`](#insn-00bede38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedcf8`](#insn-00bedcf8) → [`00bede38`](#insn-00bede38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd00`](#insn-00bedd00) → [`00bedd24`](#insn-00bedd24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd18`](#insn-00bedd18) → [`00bedd24`](#insn-00bedd24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd2c`](#insn-00bedd2c) → [`00bede38`](#insn-00bede38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd38`](#insn-00bedd38) → [`00bedd68`](#insn-00bedd68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd4c`](#insn-00bedd4c) → [`00bede48`](#insn-00bede48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd64`](#insn-00bedd64) → [`00bede38`](#insn-00bede38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd74`](#insn-00bedd74) → [`00bedd50`](#insn-00bedd50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd84`](#insn-00bedd84) → [`00bedd3c`](#insn-00bedd3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd98`](#insn-00bedd98) → [`00bedd7c`](#insn-00bedd7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedda0`](#insn-00bedda0) → [`00bedd40`](#insn-00bedd40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedda8`](#insn-00bedda8) → [`00beddd8`](#insn-00beddd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beddc4`](#insn-00beddc4) → [`00bedddc`](#insn-00bedddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beddd4`](#insn-00beddd4) → [`00bedddc`](#insn-00bedddc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedde4`](#insn-00bedde4) → [`00bede38`](#insn-00bede38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beddfc`](#insn-00beddfc) → [`00bede38`](#insn-00bede38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bede0c`](#insn-00bede0c) → [`00bede38`](#insn-00bede38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bede14`](#insn-00bede14) → [`00bede38`](#insn-00bede38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bede24`](#insn-00bede24) → [`00bede38`](#insn-00bede38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bede34`](#insn-00bede34) → [`00bede3c`](#insn-00bede3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bede3c`](#insn-00bede3c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bede54`](#insn-00bede54) → [`00bede3c`](#insn-00bede3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bedbbc`](#insn-00bedbbc)

~~~json
{
  "source": "00bedbbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedbd0`](#insn-00bedbd0)

~~~json
{
  "source": "00bedbd0",
  "target": "00bedbf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedbd4`](#insn-00bedbd4)

~~~json
{
  "source": "00bedbd4",
  "target": "00bede38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedbdc`](#insn-00bedbdc)

~~~json
{
  "source": "00bedbdc",
  "target": "00bedc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedbec`](#insn-00bedbec)

~~~json
{
  "source": "00bedbec",
  "target": "00bede38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedbf4`](#insn-00bedbf4)

~~~json
{
  "source": "00bedbf4",
  "target": "00bede2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedbfc`](#insn-00bedbfc)

~~~json
{
  "source": "00bedbfc",
  "target": "00bedc28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc04`](#insn-00bedc04)

~~~json
{
  "source": "00bedc04",
  "target": "00bedc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc0c`](#insn-00bedc0c)

~~~json
{
  "source": "00bedc0c",
  "target": "00bedc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc20`](#insn-00bedc20)

~~~json
{
  "source": "00bedc20",
  "target": "00bede58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bedc24`](#insn-00bedc24)

~~~json
{
  "source": "00bedc24",
  "target": "00bede38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc34`](#insn-00bedc34)

~~~json
{
  "source": "00bedc34",
  "target": "00bedcd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc3c`](#insn-00bedc3c)

~~~json
{
  "source": "00bedc3c",
  "target": "00bede18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc44`](#insn-00bedc44)

~~~json
{
  "source": "00bedc44",
  "target": "00bede2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc60`](#insn-00bedc60)

~~~json
{
  "source": "00bedc60",
  "target": "00bedcfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc70`](#insn-00bedc70)

~~~json
{
  "source": "00bedc70",
  "target": "00bedd1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc84`](#insn-00bedc84)

~~~json
{
  "source": "00bedc84",
  "target": "00bedd1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc88`](#insn-00bedc88)

~~~json
{
  "source": "00bedc88",
  "target": "00bedd24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedca4`](#insn-00bedca4)

~~~json
{
  "source": "00bedca4",
  "target": "00bedda4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedcb8`](#insn-00bedcb8)

~~~json
{
  "source": "00bedcb8",
  "target": "00beddc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedcd0`](#insn-00bedcd0)

~~~json
{
  "source": "00bedcd0",
  "target": "00beddc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedcd4`](#insn-00bedcd4)

~~~json
{
  "source": "00bedcd4",
  "target": "00beddd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedcdc`](#insn-00bedcdc)

~~~json
{
  "source": "00bedcdc",
  "target": "00bede38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedcf0`](#insn-00bedcf0)

~~~json
{
  "source": "00bedcf0",
  "target": "00bede38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedcf8`](#insn-00bedcf8)

~~~json
{
  "source": "00bedcf8",
  "target": "00bede38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd00`](#insn-00bedd00)

~~~json
{
  "source": "00bedd00",
  "target": "00bedd24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd18`](#insn-00bedd18)

~~~json
{
  "source": "00bedd18",
  "target": "00bedd24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd2c`](#insn-00bedd2c)

~~~json
{
  "source": "00bedd2c",
  "target": "00bede38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd38`](#insn-00bedd38)

~~~json
{
  "source": "00bedd38",
  "target": "00bedd68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd4c`](#insn-00bedd4c)

~~~json
{
  "source": "00bedd4c",
  "target": "00bede48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd64`](#insn-00bedd64)

~~~json
{
  "source": "00bedd64",
  "target": "00bede38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd74`](#insn-00bedd74)

~~~json
{
  "source": "00bedd74",
  "target": "00bedd50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd84`](#insn-00bedd84)

~~~json
{
  "source": "00bedd84",
  "target": "00bedd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd98`](#insn-00bedd98)

~~~json
{
  "source": "00bedd98",
  "target": "00bedd7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedda0`](#insn-00bedda0)

~~~json
{
  "source": "00bedda0",
  "target": "00bedd40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedda8`](#insn-00bedda8)

~~~json
{
  "source": "00bedda8",
  "target": "00beddd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beddc4`](#insn-00beddc4)

~~~json
{
  "source": "00beddc4",
  "target": "00bedddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beddd4`](#insn-00beddd4)

~~~json
{
  "source": "00beddd4",
  "target": "00bedddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedde4`](#insn-00bedde4)

~~~json
{
  "source": "00bedde4",
  "target": "00bede38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beddfc`](#insn-00beddfc)

~~~json
{
  "source": "00beddfc",
  "target": "00bede38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bede0c`](#insn-00bede0c)

~~~json
{
  "source": "00bede0c",
  "target": "00bede38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bede14`](#insn-00bede14)

~~~json
{
  "source": "00bede14",
  "target": "00bede38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bede24`](#insn-00bede24)

~~~json
{
  "source": "00bede24",
  "target": "00bede38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bede34`](#insn-00bede34)

~~~json
{
  "source": "00bede34",
  "target": "00bede3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bede3c`](#insn-00bede3c)

~~~json
{
  "source": "00bede3c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bede54`](#insn-00bede54)

~~~json
{
  "source": "00bede54",
  "target": "00bede3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
