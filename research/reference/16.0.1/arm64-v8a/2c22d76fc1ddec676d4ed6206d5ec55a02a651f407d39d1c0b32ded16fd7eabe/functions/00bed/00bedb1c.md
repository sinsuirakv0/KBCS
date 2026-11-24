# 00bedb1c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0085.md#review-3193b6301107544bf77922ab0d2191d8)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0044.md#review-3193b6301107544bf77922ab0d2191d8)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bedb1c",
  "name": "FUN_00bedb1c",
  "size": 672,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bf4b1c66c126620e2c4c8b8891051d403f13a6d5c9beb36ff2b3dbe133151752",
  "source_text_sha256": "bf4b1c66c126620e2c4c8b8891051d403f13a6d5c9beb36ff2b3dbe133151752",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bedb1c",
        "00beddbb"
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

- [00be7110](../00be7/00be7110.md)

## 呼び出し先

- [00beddbc](../00bed/00beddbc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4555 bytes

~~~c

bool FUN_00bedb1c(ulong *param_1,ulong *param_2)

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
      goto LAB_00bedd90;
    }
    if (uVar3 != 4) {
      if (uVar3 == 5) {
        FUN_00beddbc(param_1,param_1 + 1,param_1 + 2,param_1 + 3,param_2 + -1);
        return true;
      }
      goto LAB_00bedbac;
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
                    /* try { // try from 00bedc18 to 00cedc1f has its CatchHandler @ 00bedc70 */
      if (uVar3 <= uVar11) {
                    /* try { // try from 00bedc20 to 00cedd63 has its CatchHandler @ 00bed950 */
        *param_1 = uVar3;
        param_1[1] = uVar5;
        uVar3 = uVar11;
        puVar9 = puVar10;
        goto joined_r0x00bedd28;
      }
    }
    else {
      uVar8 = uVar11;
      if (uVar3 <= uVar11) goto LAB_00bedd40;
      *puVar10 = uVar11;
      *puVar6 = uVar3;
      puVar13 = puVar10;
      uVar2 = uVar3;
joined_r0x00bedd28:
      uVar8 = uVar3;
      if (uVar5 <= uVar11) goto LAB_00bedd40;
    }
    *puVar9 = uVar11;
    *puVar13 = uVar5;
    uVar8 = uVar2;
LAB_00bedd40:
                    /* catch() { ... } // from try @ 00beda00 with catch @ 00bedd44 */
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
LAB_00bedd90:
    param_2[-1] = uVar3;
    return true;
  }
LAB_00bedbac:
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
      goto joined_r0x00bedc7c;
    }
  }
  else {
    if (uVar11 <= uVar5) goto LAB_00bedc88;
                    /* catch() { ... } // from try @ 00bedc18 with catch @ 00bedc70 */
    *puVar6 = uVar5;
    *puVar10 = uVar11;
    puVar13 = puVar6;
joined_r0x00bedc7c:
    if (uVar3 <= uVar5) goto LAB_00bedc88;
  }
  *puVar9 = uVar5;
  *puVar13 = uVar3;
LAB_00bedc88:
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
          if (lVar1 == 0) goto LAB_00bedca4;
          uVar3 = *(ulong *)((long)param_1 + lVar12 + -0x10);
          lVar12 = lVar1;
        } while (uVar5 < uVar3);
        puVar9 = (ulong *)((long)param_1 + lVar1);
LAB_00bedca4:
        iVar4 = iVar4 + 1;
                    /* catch() { ... } // from try @ 00bed9f4 with catch @ 00bedca8 */
        *puVar9 = uVar5;
        if (iVar4 == 8) {
          return puVar6 + 1 == param_2;
        }
      }
                    /* catch() { ... } // from try @ 00beda3c with catch @ 00bedcb8 */
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
<a id="insn-00bedb1c"></a> `00bedb1c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bedb20"></a> `00bedb20` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bedb24"></a> `00bedb24` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bedb28"></a> `00bedb28` | `28 00 00 cb` | sub x8,x1,x0 | `FALL_THROUGH`
<a id="insn-00bedb2c"></a> `00bedb2c` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bedb30"></a> `00bedb30` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bedb34"></a> `00bedb34` | `4c 01 00 54` | b.gt 0x00bedb5c | `CONDITIONAL_JUMP`
<a id="insn-00bedb38"></a> `00bedb38` | `23 13 00 54` | b.cc 0x00bedd9c | `CONDITIONAL_JUMP`
<a id="insn-00bedb3c"></a> `00bedb3c` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bedb40"></a> `00bedb40` | `61 03 00 54` | b.ne 0x00bedbac | `CONDITIONAL_JUMP`
<a id="insn-00bedb44"></a> `00bedb44` | `29 80 5f f8` | ldur x9,[x1, #-0x8] | `FALL_THROUGH`
<a id="insn-00bedb48"></a> `00bedb48` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bedb4c"></a> `00bedb4c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bedb50"></a> `00bedb50` | `62 12 00 54` | b.cs 0x00bedd9c | `CONDITIONAL_JUMP`
<a id="insn-00bedb54"></a> `00bedb54` | `09 00 00 f9` | str x9,[x0] | `FALL_THROUGH`
<a id="insn-00bedb58"></a> `00bedb58` | `8e 00 00 14` | b 0x00bedd90 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedb5c"></a> `00bedb5c` | `1f 0d 00 f1` | cmp x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bedb60"></a> `00bedb60` | `60 01 00 54` | b.eq 0x00bedb8c | `CONDITIONAL_JUMP`
<a id="insn-00bedb64"></a> `00bedb64` | `1f 11 00 f1` | cmp x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bedb68"></a> `00bedb68` | `40 04 00 54` | b.eq 0x00bedbf0 | `CONDITIONAL_JUMP`
<a id="insn-00bedb6c"></a> `00bedb6c` | `1f 15 00 f1` | cmp x8,#0x5 | `FALL_THROUGH`
<a id="insn-00bedb70"></a> `00bedb70` | `e1 01 00 54` | b.ne 0x00bedbac | `CONDITIONAL_JUMP`
<a id="insn-00bedb74"></a> `00bedb74` | `24 20 00 d1` | sub x4,x1,#0x8 | `FALL_THROUGH`
<a id="insn-00bedb78"></a> `00bedb78` | `01 20 00 91` | add x1,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bedb7c"></a> `00bedb7c` | `02 40 00 91` | add x2,x0,#0x10 | `FALL_THROUGH`
<a id="insn-00bedb80"></a> `00bedb80` | `03 60 00 91` | add x3,x0,#0x18 | `FALL_THROUGH`
<a id="insn-00bedb84"></a> `00bedb84` | `8e 00 00 94` | bl 0x00beddbc | `UNCONDITIONAL_CALL`
<a id="insn-00bedb88"></a> `00bedb88` | `85 00 00 14` | b 0x00bedd9c | `UNCONDITIONAL_JUMP`
<a id="insn-00bedb8c"></a> `00bedb8c` | `08 24 40 a9` | ldp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00bedb90"></a> `00bedb90` | `2a 80 5f f8` | ldur x10,[x1, #-0x8] | `FALL_THROUGH`
<a id="insn-00bedb94"></a> `00bedb94` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bedb98"></a> `00bedb98` | `22 05 00 54` | b.cs 0x00bedc3c | `CONDITIONAL_JUMP`
<a id="insn-00bedb9c"></a> `00bedb9c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bedba0"></a> `00bedba0` | `e2 0e 00 54` | b.cs 0x00bedd7c | `CONDITIONAL_JUMP`
<a id="insn-00bedba4"></a> `00bedba4` | `0a 00 00 f9` | str x10,[x0] | `FALL_THROUGH`
<a id="insn-00bedba8"></a> `00bedba8` | `7a 00 00 14` | b 0x00bedd90 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedbac"></a> `00bedbac` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00bedbb0"></a> `00bedbb0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bedbb4"></a> `00bedbb4` | `eb 03 00 aa` | mov x11,x0 | `FALL_THROUGH`
<a id="insn-00bedbb8"></a> `00bedbb8` | `4c 8d 40 f8` | ldr x12,[x10, #0x8]! | `FALL_THROUGH`
<a id="insn-00bedbbc"></a> `00bedbbc` | `69 0d 41 f8` | ldr x9,[x11, #0x10]! | `FALL_THROUGH`
<a id="insn-00bedbc0"></a> `00bedbc0` | `9f 01 08 eb` | cmp x12,x8 | `FALL_THROUGH`
<a id="insn-00bedbc4"></a> `00bedbc4` | `e2 04 00 54` | b.cs 0x00bedc60 | `CONDITIONAL_JUMP`
<a id="insn-00bedbc8"></a> `00bedbc8` | `3f 01 0c eb` | cmp x9,x12 | `FALL_THROUGH`
<a id="insn-00bedbcc"></a> `00bedbcc` | `ed 03 00 aa` | mov x13,x0 | `FALL_THROUGH`
<a id="insn-00bedbd0"></a> `00bedbd0` | `ee 03 0b aa` | mov x14,x11 | `FALL_THROUGH`
<a id="insn-00bedbd4"></a> `00bedbd4` | `63 05 00 54` | b.cc 0x00bedc80 | `CONDITIONAL_JUMP`
<a id="insn-00bedbd8"></a> `00bedbd8` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bedbdc"></a> `00bedbdc` | `ed 03 0a aa` | mov x13,x10 | `FALL_THROUGH`
<a id="insn-00bedbe0"></a> `00bedbe0` | `ee 03 0b aa` | mov x14,x11 | `FALL_THROUGH`
<a id="insn-00bedbe4"></a> `00bedbe4` | `0c 20 00 a9` | stp x12,x8,[x0] | `FALL_THROUGH`
<a id="insn-00bedbe8"></a> `00bedbe8` | `c3 04 00 54` | b.cc 0x00bedc80 | `CONDITIONAL_JUMP`
<a id="insn-00bedbec"></a> `00bedbec` | `27 00 00 14` | b 0x00bedc88 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedbf0"></a> `00bedbf0` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bedbf4"></a> `00bedbf4` | `0b 00 40 f9` | ldr x11,[x0] | `FALL_THROUGH`
<a id="insn-00bedbf8"></a> `00bedbf8` | `e9 03 00 aa` | mov x9,x0 | `FALL_THROUGH`
<a id="insn-00bedbfc"></a> `00bedbfc` | `0a 8d 40 f8` | ldr x10,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00bedc00"></a> `00bedc00` | `2c 0d 41 f8` | ldr x12,[x9, #0x10]! | `FALL_THROUGH`
<a id="insn-00bedc04"></a> `00bedc04` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-00bedc08"></a> `00bedc08` | `02 08 00 54` | b.cs 0x00bedd08 | `CONDITIONAL_JUMP`
<a id="insn-00bedc0c"></a> `00bedc0c` | `9f 01 0a eb` | cmp x12,x10 | `FALL_THROUGH`
<a id="insn-00bedc10"></a> `00bedc10` | `ed 03 00 aa` | mov x13,x0 | `FALL_THROUGH`
<a id="insn-00bedc14"></a> `00bedc14` | `ee 03 09 aa` | mov x14,x9 | `FALL_THROUGH`
<a id="insn-00bedc18"></a> `00bedc18` | `e2 03 0b aa` | mov x2,x11 | `FALL_THROUGH`
<a id="insn-00bedc1c"></a> `00bedc1c` | `83 08 00 54` | b.cc 0x00bedd2c | `CONDITIONAL_JUMP`
<a id="insn-00bedc20"></a> `00bedc20` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bedc24"></a> `00bedc24` | `ed 03 08 aa` | mov x13,x8 | `FALL_THROUGH`
<a id="insn-00bedc28"></a> `00bedc28` | `ee 03 09 aa` | mov x14,x9 | `FALL_THROUGH`
<a id="insn-00bedc2c"></a> `00bedc2c` | `e2 03 0b aa` | mov x2,x11 | `FALL_THROUGH`
<a id="insn-00bedc30"></a> `00bedc30` | `0a 2c 00 a9` | stp x10,x11,[x0] | `FALL_THROUGH`
<a id="insn-00bedc34"></a> `00bedc34` | `c3 07 00 54` | b.cc 0x00bedd2c | `CONDITIONAL_JUMP`
<a id="insn-00bedc38"></a> `00bedc38` | `41 00 00 14` | b 0x00bedd3c | `UNCONDITIONAL_JUMP`
<a id="insn-00bedc3c"></a> `00bedc3c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bedc40"></a> `00bedc40` | `e2 0a 00 54` | b.cs 0x00bedd9c | `CONDITIONAL_JUMP`
<a id="insn-00bedc44"></a> `00bedc44` | `0a 04 00 f9` | str x10,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bedc48"></a> `00bedc48` | `29 80 1f f8` | stur x9,[x1, #-0x8] | `FALL_THROUGH`
<a id="insn-00bedc4c"></a> `00bedc4c` | `08 24 40 a9` | ldp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00bedc50"></a> `00bedc50` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bedc54"></a> `00bedc54` | `42 0a 00 54` | b.cs 0x00bedd9c | `CONDITIONAL_JUMP`
<a id="insn-00bedc58"></a> `00bedc58` | `09 20 00 a9` | stp x9,x8,[x0] | `FALL_THROUGH`
<a id="insn-00bedc5c"></a> `00bedc5c` | `50 00 00 14` | b 0x00bedd9c | `UNCONDITIONAL_JUMP`
<a id="insn-00bedc60"></a> `00bedc60` | `3f 01 0c eb` | cmp x9,x12 | `FALL_THROUGH`
<a id="insn-00bedc64"></a> `00bedc64` | `22 01 00 54` | b.cs 0x00bedc88 | `CONDITIONAL_JUMP`
<a id="insn-00bedc68"></a> `00bedc68` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bedc6c"></a> `00bedc6c` | `ed 03 00 aa` | mov x13,x0 | `FALL_THROUGH`
<a id="insn-00bedc70"></a> `00bedc70` | `ee 03 0a aa` | mov x14,x10 | `FALL_THROUGH`
<a id="insn-00bedc74"></a> `00bedc74` | `49 01 00 f9` | str x9,[x10] | `FALL_THROUGH`
<a id="insn-00bedc78"></a> `00bedc78` | `6c 01 00 f9` | str x12,[x11] | `FALL_THROUGH`
<a id="insn-00bedc7c"></a> `00bedc7c` | `62 00 00 54` | b.cs 0x00bedc88 | `CONDITIONAL_JUMP`
<a id="insn-00bedc80"></a> `00bedc80` | `a9 01 00 f9` | str x9,[x13] | `FALL_THROUGH`
<a id="insn-00bedc84"></a> `00bedc84` | `c8 01 00 f9` | str x8,[x14] | `FALL_THROUGH`
<a id="insn-00bedc88"></a> `00bedc88` | `08 60 00 91` | add x8,x0,#0x18 | `FALL_THROUGH`
<a id="insn-00bedc8c"></a> `00bedc8c` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00bedc90"></a> `00bedc90` | `60 08 00 54` | b.eq 0x00bedd9c | `CONDITIONAL_JUMP`
<a id="insn-00bedc94"></a> `00bedc94` | `e9 03 1f 2a` | mov w9,wzr | `FALL_THROUGH`
<a id="insn-00bedc98"></a> `00bedc98` | `0a 03 80 52` | mov w10,#0x18 | `FALL_THROUGH`
<a id="insn-00bedc9c"></a> `00bedc9c` | `0c 00 00 14` | b 0x00bedccc | `UNCONDITIONAL_JUMP`
<a id="insn-00bedca0"></a> `00bedca0` | `eb 03 00 aa` | mov x11,x0 | `FALL_THROUGH`
<a id="insn-00bedca4"></a> `00bedca4` | `29 05 00 11` | add w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bedca8"></a> `00bedca8` | `6c 01 00 f9` | str x12,[x11] | `FALL_THROUGH`
<a id="insn-00bedcac"></a> `00bedcac` | `3f 21 00 71` | cmp w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bedcb0"></a> `00bedcb0` | `e0 07 00 54` | b.eq 0x00beddac | `CONDITIONAL_JUMP`
<a id="insn-00bedcb4"></a> `00bedcb4` | `0c 21 00 91` | add x12,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bedcb8"></a> `00bedcb8` | `eb 03 08 aa` | mov x11,x8 | `FALL_THROUGH`
<a id="insn-00bedcbc"></a> `00bedcbc` | `4a 21 00 91` | add x10,x10,#0x8 | `FALL_THROUGH`
<a id="insn-00bedcc0"></a> `00bedcc0` | `9f 01 01 eb` | cmp x12,x1 | `FALL_THROUGH`
<a id="insn-00bedcc4"></a> `00bedcc4` | `e8 03 0c aa` | mov x8,x12 | `FALL_THROUGH`
<a id="insn-00bedcc8"></a> `00bedcc8` | `a0 06 00 54` | b.eq 0x00bedd9c | `CONDITIONAL_JUMP`
<a id="insn-00bedccc"></a> `00bedccc` | `0c 01 40 f9` | ldr x12,[x8] | `FALL_THROUGH`
<a id="insn-00bedcd0"></a> `00bedcd0` | `6b 01 40 f9` | ldr x11,[x11] | `FALL_THROUGH`
<a id="insn-00bedcd4"></a> `00bedcd4` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bedcd8"></a> `00bedcd8` | `e2 fe ff 54` | b.cs 0x00bedcb4 | `CONDITIONAL_JUMP`
<a id="insn-00bedcdc"></a> `00bedcdc` | `ee 03 0a aa` | mov x14,x10 | `FALL_THROUGH`
<a id="insn-00bedce0"></a> `00bedce0` | `cd 21 00 f1` | subs x13,x14,#0x8 | `FALL_THROUGH`
<a id="insn-00bedce4"></a> `00bedce4` | `0b 68 2e f8` | str x11,[x0, x14, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bedce8"></a> `00bedce8` | `c0 fd ff 54` | b.eq 0x00bedca0 | `CONDITIONAL_JUMP`
<a id="insn-00bedcec"></a> `00bedcec` | `0b 00 0e 8b` | add x11,x0,x14 | `FALL_THROUGH`
<a id="insn-00bedcf0"></a> `00bedcf0` | `ee 03 0d aa` | mov x14,x13 | `FALL_THROUGH`
<a id="insn-00bedcf4"></a> `00bedcf4` | `6b 01 5f f8` | ldur x11,[x11, #-0x10] | `FALL_THROUGH`
<a id="insn-00bedcf8"></a> `00bedcf8` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bedcfc"></a> `00bedcfc` | `23 ff ff 54` | b.cc 0x00bedce0 | `CONDITIONAL_JUMP`
<a id="insn-00bedd00"></a> `00bedd00` | `0b 00 0d 8b` | add x11,x0,x13 | `FALL_THROUGH`
<a id="insn-00bedd04"></a> `00bedd04` | `e8 ff ff 17` | b 0x00bedca4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedd08"></a> `00bedd08` | `9f 01 0a eb` | cmp x12,x10 | `FALL_THROUGH`
<a id="insn-00bedd0c"></a> `00bedd0c` | `82 01 00 54` | b.cs 0x00bedd3c | `CONDITIONAL_JUMP`
<a id="insn-00bedd10"></a> `00bedd10` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00bedd14"></a> `00bedd14` | `ed 03 00 aa` | mov x13,x0 | `FALL_THROUGH`
<a id="insn-00bedd18"></a> `00bedd18` | `ee 03 08 aa` | mov x14,x8 | `FALL_THROUGH`
<a id="insn-00bedd1c"></a> `00bedd1c` | `e2 03 0a aa` | mov x2,x10 | `FALL_THROUGH`
<a id="insn-00bedd20"></a> `00bedd20` | `0c 01 00 f9` | str x12,[x8] | `FALL_THROUGH`
<a id="insn-00bedd24"></a> `00bedd24` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00bedd28"></a> `00bedd28` | `c2 00 00 54` | b.cs 0x00bedd40 | `CONDITIONAL_JUMP`
<a id="insn-00bedd2c"></a> `00bedd2c` | `ea 03 02 aa` | mov x10,x2 | `FALL_THROUGH`
<a id="insn-00bedd30"></a> `00bedd30` | `ac 01 00 f9` | str x12,[x13] | `FALL_THROUGH`
<a id="insn-00bedd34"></a> `00bedd34` | `cb 01 00 f9` | str x11,[x14] | `FALL_THROUGH`
<a id="insn-00bedd38"></a> `00bedd38` | `02 00 00 14` | b 0x00bedd40 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedd3c"></a> `00bedd3c` | `ea 03 0c aa` | mov x10,x12 | `FALL_THROUGH`
<a id="insn-00bedd40"></a> `00bedd40` | `2b 80 5f f8` | ldur x11,[x1, #-0x8] | `FALL_THROUGH`
<a id="insn-00bedd44"></a> `00bedd44` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bedd48"></a> `00bedd48` | `a2 02 00 54` | b.cs 0x00bedd9c | `CONDITIONAL_JUMP`
<a id="insn-00bedd4c"></a> `00bedd4c` | `2b 01 00 f9` | str x11,[x9] | `FALL_THROUGH`
<a id="insn-00bedd50"></a> `00bedd50` | `2a 80 1f f8` | stur x10,[x1, #-0x8] | `FALL_THROUGH`
<a id="insn-00bedd54"></a> `00bedd54` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00bedd58"></a> `00bedd58` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bedd5c"></a> `00bedd5c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bedd60"></a> `00bedd60` | `e2 01 00 54` | b.cs 0x00bedd9c | `CONDITIONAL_JUMP`
<a id="insn-00bedd64"></a> `00bedd64` | `0a 00 40 f9` | ldr x10,[x0] | `FALL_THROUGH`
<a id="insn-00bedd68"></a> `00bedd68` | `09 a0 00 a9` | stp x9,x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bedd6c"></a> `00bedd6c` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bedd70"></a> `00bedd70` | `62 01 00 54` | b.cs 0x00bedd9c | `CONDITIONAL_JUMP`
<a id="insn-00bedd74"></a> `00bedd74` | `09 28 00 a9` | stp x9,x10,[x0] | `FALL_THROUGH`
<a id="insn-00bedd78"></a> `00bedd78` | `09 00 00 14` | b 0x00bedd9c | `UNCONDITIONAL_JUMP`
<a id="insn-00bedd7c"></a> `00bedd7c` | `09 20 00 a9` | stp x9,x8,[x0] | `FALL_THROUGH`
<a id="insn-00bedd80"></a> `00bedd80` | `29 80 5f f8` | ldur x9,[x1, #-0x8] | `FALL_THROUGH`
<a id="insn-00bedd84"></a> `00bedd84` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bedd88"></a> `00bedd88` | `a2 00 00 54` | b.cs 0x00bedd9c | `CONDITIONAL_JUMP`
<a id="insn-00bedd8c"></a> `00bedd8c` | `09 04 00 f9` | str x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bedd90"></a> `00bedd90` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bedd94"></a> `00bedd94` | `28 80 1f f8` | stur x8,[x1, #-0x8] | `FALL_THROUGH`
<a id="insn-00bedd98"></a> `00bedd98` | `02 00 00 14` | b 0x00bedda0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bedd9c"></a> `00bedd9c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bedda0"></a> `00bedda0` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bedda4"></a> `00bedda4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bedda8"></a> `00bedda8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00beddac"></a> `00beddac` | `08 21 00 91` | add x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00beddb0"></a> `00beddb0` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00beddb4"></a> `00beddb4` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00beddb8"></a> `00beddb8` | `fa ff ff 17` | b 0x00bedda0 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bedb1c`](#insn-00bedb1c) 範囲 `[['00bedb1c', '00bedb37']]`
  - `CONDITIONAL_JUMP` [`00bedb34`](#insn-00bedb34) → [`00bedb5c`](#insn-00bedb5c)
  - `FALL_THROUGH` [`00bedb34`](#insn-00bedb34) → [`00bedb38`](#insn-00bedb38)
- ブロック [`00bedb38`](#insn-00bedb38) 範囲 `[['00bedb38', '00bedb3b']]`
  - `CONDITIONAL_JUMP` [`00bedb38`](#insn-00bedb38) → [`00bedd9c`](#insn-00bedd9c)
  - `FALL_THROUGH` [`00bedb38`](#insn-00bedb38) → [`00bedb3c`](#insn-00bedb3c)
- ブロック [`00bedb3c`](#insn-00bedb3c) 範囲 `[['00bedb3c', '00bedb43']]`
  - `CONDITIONAL_JUMP` [`00bedb40`](#insn-00bedb40) → [`00bedbac`](#insn-00bedbac)
  - `FALL_THROUGH` [`00bedb40`](#insn-00bedb40) → [`00bedb44`](#insn-00bedb44)
- ブロック [`00bedb44`](#insn-00bedb44) 範囲 `[['00bedb44', '00bedb53']]`
  - `CONDITIONAL_JUMP` [`00bedb50`](#insn-00bedb50) → [`00bedd9c`](#insn-00bedd9c)
  - `FALL_THROUGH` [`00bedb50`](#insn-00bedb50) → [`00bedb54`](#insn-00bedb54)
- ブロック [`00bedb54`](#insn-00bedb54) 範囲 `[['00bedb54', '00bedb5b']]`
  - `UNCONDITIONAL_JUMP` [`00bedb58`](#insn-00bedb58) → [`00bedd90`](#insn-00bedd90)
- ブロック [`00bedb5c`](#insn-00bedb5c) 範囲 `[['00bedb5c', '00bedb63']]`
  - `CONDITIONAL_JUMP` [`00bedb60`](#insn-00bedb60) → [`00bedb8c`](#insn-00bedb8c)
  - `FALL_THROUGH` [`00bedb60`](#insn-00bedb60) → [`00bedb64`](#insn-00bedb64)
- ブロック [`00bedb64`](#insn-00bedb64) 範囲 `[['00bedb64', '00bedb6b']]`
  - `CONDITIONAL_JUMP` [`00bedb68`](#insn-00bedb68) → [`00bedbf0`](#insn-00bedbf0)
  - `FALL_THROUGH` [`00bedb68`](#insn-00bedb68) → [`00bedb6c`](#insn-00bedb6c)
- ブロック [`00bedb6c`](#insn-00bedb6c) 範囲 `[['00bedb6c', '00bedb73']]`
  - `CONDITIONAL_JUMP` [`00bedb70`](#insn-00bedb70) → [`00bedbac`](#insn-00bedbac)
  - `FALL_THROUGH` [`00bedb70`](#insn-00bedb70) → [`00bedb74`](#insn-00bedb74)
- ブロック [`00bedb74`](#insn-00bedb74) 範囲 `[['00bedb74', '00bedb8b']]`
  - `UNCONDITIONAL_JUMP` [`00bedb88`](#insn-00bedb88) → [`00bedd9c`](#insn-00bedd9c)
- ブロック [`00bedb8c`](#insn-00bedb8c) 範囲 `[['00bedb8c', '00bedb9b']]`
  - `CONDITIONAL_JUMP` [`00bedb98`](#insn-00bedb98) → [`00bedc3c`](#insn-00bedc3c)
  - `FALL_THROUGH` [`00bedb98`](#insn-00bedb98) → [`00bedb9c`](#insn-00bedb9c)
- ブロック [`00bedb9c`](#insn-00bedb9c) 範囲 `[['00bedb9c', '00bedba3']]`
  - `CONDITIONAL_JUMP` [`00bedba0`](#insn-00bedba0) → [`00bedd7c`](#insn-00bedd7c)
  - `FALL_THROUGH` [`00bedba0`](#insn-00bedba0) → [`00bedba4`](#insn-00bedba4)
- ブロック [`00bedba4`](#insn-00bedba4) 範囲 `[['00bedba4', '00bedbab']]`
  - `UNCONDITIONAL_JUMP` [`00bedba8`](#insn-00bedba8) → [`00bedd90`](#insn-00bedd90)
- ブロック [`00bedbac`](#insn-00bedbac) 範囲 `[['00bedbac', '00bedbc7']]`
  - `CONDITIONAL_JUMP` [`00bedbc4`](#insn-00bedbc4) → [`00bedc60`](#insn-00bedc60)
  - `FALL_THROUGH` [`00bedbc4`](#insn-00bedbc4) → [`00bedbc8`](#insn-00bedbc8)
- ブロック [`00bedbc8`](#insn-00bedbc8) 範囲 `[['00bedbc8', '00bedbd7']]`
  - `CONDITIONAL_JUMP` [`00bedbd4`](#insn-00bedbd4) → [`00bedc80`](#insn-00bedc80)
  - `FALL_THROUGH` [`00bedbd4`](#insn-00bedbd4) → [`00bedbd8`](#insn-00bedbd8)
- ブロック [`00bedbd8`](#insn-00bedbd8) 範囲 `[['00bedbd8', '00bedbeb']]`
  - `CONDITIONAL_JUMP` [`00bedbe8`](#insn-00bedbe8) → [`00bedc80`](#insn-00bedc80)
  - `FALL_THROUGH` [`00bedbe8`](#insn-00bedbe8) → [`00bedbec`](#insn-00bedbec)
- ブロック [`00bedbec`](#insn-00bedbec) 範囲 `[['00bedbec', '00bedbef']]`
  - `UNCONDITIONAL_JUMP` [`00bedbec`](#insn-00bedbec) → [`00bedc88`](#insn-00bedc88)
- ブロック [`00bedbf0`](#insn-00bedbf0) 範囲 `[['00bedbf0', '00bedc0b']]`
  - `CONDITIONAL_JUMP` [`00bedc08`](#insn-00bedc08) → [`00bedd08`](#insn-00bedd08)
  - `FALL_THROUGH` [`00bedc08`](#insn-00bedc08) → [`00bedc0c`](#insn-00bedc0c)
- ブロック [`00bedc0c`](#insn-00bedc0c) 範囲 `[['00bedc0c', '00bedc17']]`
  - `FALL_THROUGH` [`00bedc14`](#insn-00bedc14) → [`00bedc18`](#insn-00bedc18)
- ブロック [`00bedc18`](#insn-00bedc18) 範囲 `[['00bedc18', '00bedc1f']]`
  - `CONDITIONAL_JUMP` [`00bedc1c`](#insn-00bedc1c) → [`00bedd2c`](#insn-00bedd2c)
  - `FALL_THROUGH` [`00bedc1c`](#insn-00bedc1c) → [`00bedc20`](#insn-00bedc20)
- ブロック [`00bedc20`](#insn-00bedc20) 範囲 `[['00bedc20', '00bedc37']]`
  - `CONDITIONAL_JUMP` [`00bedc34`](#insn-00bedc34) → [`00bedd2c`](#insn-00bedd2c)
  - `FALL_THROUGH` [`00bedc34`](#insn-00bedc34) → [`00bedc38`](#insn-00bedc38)
- ブロック [`00bedc38`](#insn-00bedc38) 範囲 `[['00bedc38', '00bedc3b']]`
  - `UNCONDITIONAL_JUMP` [`00bedc38`](#insn-00bedc38) → [`00bedd3c`](#insn-00bedd3c)
- ブロック [`00bedc3c`](#insn-00bedc3c) 範囲 `[['00bedc3c', '00bedc43']]`
  - `CONDITIONAL_JUMP` [`00bedc40`](#insn-00bedc40) → [`00bedd9c`](#insn-00bedd9c)
  - `FALL_THROUGH` [`00bedc40`](#insn-00bedc40) → [`00bedc44`](#insn-00bedc44)
- ブロック [`00bedc44`](#insn-00bedc44) 範囲 `[['00bedc44', '00bedc57']]`
  - `CONDITIONAL_JUMP` [`00bedc54`](#insn-00bedc54) → [`00bedd9c`](#insn-00bedd9c)
  - `FALL_THROUGH` [`00bedc54`](#insn-00bedc54) → [`00bedc58`](#insn-00bedc58)
- ブロック [`00bedc58`](#insn-00bedc58) 範囲 `[['00bedc58', '00bedc5f']]`
  - `UNCONDITIONAL_JUMP` [`00bedc5c`](#insn-00bedc5c) → [`00bedd9c`](#insn-00bedd9c)
- ブロック [`00bedc60`](#insn-00bedc60) 範囲 `[['00bedc60', '00bedc67']]`
  - `CONDITIONAL_JUMP` [`00bedc64`](#insn-00bedc64) → [`00bedc88`](#insn-00bedc88)
  - `FALL_THROUGH` [`00bedc64`](#insn-00bedc64) → [`00bedc68`](#insn-00bedc68)
- ブロック [`00bedc68`](#insn-00bedc68) 範囲 `[['00bedc68', '00bedc6f']]`
  - `FALL_THROUGH` [`00bedc6c`](#insn-00bedc6c) → [`00bedc70`](#insn-00bedc70)
- ブロック [`00bedc70`](#insn-00bedc70) 範囲 `[['00bedc70', '00bedc7f']]`
  - `CONDITIONAL_JUMP` [`00bedc7c`](#insn-00bedc7c) → [`00bedc88`](#insn-00bedc88)
  - `FALL_THROUGH` [`00bedc7c`](#insn-00bedc7c) → [`00bedc80`](#insn-00bedc80)
- ブロック [`00bedc80`](#insn-00bedc80) 範囲 `[['00bedc80', '00bedc87']]`
  - `FALL_THROUGH` [`00bedc84`](#insn-00bedc84) → [`00bedc88`](#insn-00bedc88)
- ブロック [`00bedc88`](#insn-00bedc88) 範囲 `[['00bedc88', '00bedc93']]`
  - `CONDITIONAL_JUMP` [`00bedc90`](#insn-00bedc90) → [`00bedd9c`](#insn-00bedd9c)
  - `FALL_THROUGH` [`00bedc90`](#insn-00bedc90) → [`00bedc94`](#insn-00bedc94)
- ブロック [`00bedc94`](#insn-00bedc94) 範囲 `[['00bedc94', '00bedc9f']]`
  - `UNCONDITIONAL_JUMP` [`00bedc9c`](#insn-00bedc9c) → [`00bedccc`](#insn-00bedccc)
- ブロック [`00bedca0`](#insn-00bedca0) 範囲 `[['00bedca0', '00bedca3']]`
  - `FALL_THROUGH` [`00bedca0`](#insn-00bedca0) → [`00bedca4`](#insn-00bedca4)
- ブロック [`00bedca4`](#insn-00bedca4) 範囲 `[['00bedca4', '00bedca7']]`
  - `FALL_THROUGH` [`00bedca4`](#insn-00bedca4) → [`00bedca8`](#insn-00bedca8)
- ブロック [`00bedca8`](#insn-00bedca8) 範囲 `[['00bedca8', '00bedcb3']]`
  - `CONDITIONAL_JUMP` [`00bedcb0`](#insn-00bedcb0) → [`00beddac`](#insn-00beddac)
  - `FALL_THROUGH` [`00bedcb0`](#insn-00bedcb0) → [`00bedcb4`](#insn-00bedcb4)
- ブロック [`00bedcb4`](#insn-00bedcb4) 範囲 `[['00bedcb4', '00bedcb7']]`
  - `FALL_THROUGH` [`00bedcb4`](#insn-00bedcb4) → [`00bedcb8`](#insn-00bedcb8)
- ブロック [`00bedcb8`](#insn-00bedcb8) 範囲 `[['00bedcb8', '00bedccb']]`
  - `CONDITIONAL_JUMP` [`00bedcc8`](#insn-00bedcc8) → [`00bedd9c`](#insn-00bedd9c)
  - `FALL_THROUGH` [`00bedcc8`](#insn-00bedcc8) → [`00bedccc`](#insn-00bedccc)
- ブロック [`00bedccc`](#insn-00bedccc) 範囲 `[['00bedccc', '00bedcdb']]`
  - `CONDITIONAL_JUMP` [`00bedcd8`](#insn-00bedcd8) → [`00bedcb4`](#insn-00bedcb4)
  - `FALL_THROUGH` [`00bedcd8`](#insn-00bedcd8) → [`00bedcdc`](#insn-00bedcdc)
- ブロック [`00bedcdc`](#insn-00bedcdc) 範囲 `[['00bedcdc', '00bedcdf']]`
  - `FALL_THROUGH` [`00bedcdc`](#insn-00bedcdc) → [`00bedce0`](#insn-00bedce0)
- ブロック [`00bedce0`](#insn-00bedce0) 範囲 `[['00bedce0', '00bedceb']]`
  - `CONDITIONAL_JUMP` [`00bedce8`](#insn-00bedce8) → [`00bedca0`](#insn-00bedca0)
  - `FALL_THROUGH` [`00bedce8`](#insn-00bedce8) → [`00bedcec`](#insn-00bedcec)
- ブロック [`00bedcec`](#insn-00bedcec) 範囲 `[['00bedcec', '00bedcff']]`
  - `CONDITIONAL_JUMP` [`00bedcfc`](#insn-00bedcfc) → [`00bedce0`](#insn-00bedce0)
  - `FALL_THROUGH` [`00bedcfc`](#insn-00bedcfc) → [`00bedd00`](#insn-00bedd00)
- ブロック [`00bedd00`](#insn-00bedd00) 範囲 `[['00bedd00', '00bedd07']]`
  - `UNCONDITIONAL_JUMP` [`00bedd04`](#insn-00bedd04) → [`00bedca4`](#insn-00bedca4)
- ブロック [`00bedd08`](#insn-00bedd08) 範囲 `[['00bedd08', '00bedd0f']]`
  - `CONDITIONAL_JUMP` [`00bedd0c`](#insn-00bedd0c) → [`00bedd3c`](#insn-00bedd3c)
  - `FALL_THROUGH` [`00bedd0c`](#insn-00bedd0c) → [`00bedd10`](#insn-00bedd10)
- ブロック [`00bedd10`](#insn-00bedd10) 範囲 `[['00bedd10', '00bedd2b']]`
  - `CONDITIONAL_JUMP` [`00bedd28`](#insn-00bedd28) → [`00bedd40`](#insn-00bedd40)
  - `FALL_THROUGH` [`00bedd28`](#insn-00bedd28) → [`00bedd2c`](#insn-00bedd2c)
- ブロック [`00bedd2c`](#insn-00bedd2c) 範囲 `[['00bedd2c', '00bedd3b']]`
  - `UNCONDITIONAL_JUMP` [`00bedd38`](#insn-00bedd38) → [`00bedd40`](#insn-00bedd40)
- ブロック [`00bedd3c`](#insn-00bedd3c) 範囲 `[['00bedd3c', '00bedd3f']]`
  - `FALL_THROUGH` [`00bedd3c`](#insn-00bedd3c) → [`00bedd40`](#insn-00bedd40)
- ブロック [`00bedd40`](#insn-00bedd40) 範囲 `[['00bedd40', '00bedd43']]`
  - `FALL_THROUGH` [`00bedd40`](#insn-00bedd40) → [`00bedd44`](#insn-00bedd44)
- ブロック [`00bedd44`](#insn-00bedd44) 範囲 `[['00bedd44', '00bedd4b']]`
  - `CONDITIONAL_JUMP` [`00bedd48`](#insn-00bedd48) → [`00bedd9c`](#insn-00bedd9c)
  - `FALL_THROUGH` [`00bedd48`](#insn-00bedd48) → [`00bedd4c`](#insn-00bedd4c)
- ブロック [`00bedd4c`](#insn-00bedd4c) 範囲 `[['00bedd4c', '00bedd63']]`
  - `CONDITIONAL_JUMP` [`00bedd60`](#insn-00bedd60) → [`00bedd9c`](#insn-00bedd9c)
  - `FALL_THROUGH` [`00bedd60`](#insn-00bedd60) → [`00bedd64`](#insn-00bedd64)
- ブロック [`00bedd64`](#insn-00bedd64) 範囲 `[['00bedd64', '00bedd73']]`
  - `CONDITIONAL_JUMP` [`00bedd70`](#insn-00bedd70) → [`00bedd9c`](#insn-00bedd9c)
  - `FALL_THROUGH` [`00bedd70`](#insn-00bedd70) → [`00bedd74`](#insn-00bedd74)
- ブロック [`00bedd74`](#insn-00bedd74) 範囲 `[['00bedd74', '00bedd7b']]`
  - `UNCONDITIONAL_JUMP` [`00bedd78`](#insn-00bedd78) → [`00bedd9c`](#insn-00bedd9c)
- ブロック [`00bedd7c`](#insn-00bedd7c) 範囲 `[['00bedd7c', '00bedd8b']]`
  - `CONDITIONAL_JUMP` [`00bedd88`](#insn-00bedd88) → [`00bedd9c`](#insn-00bedd9c)
  - `FALL_THROUGH` [`00bedd88`](#insn-00bedd88) → [`00bedd8c`](#insn-00bedd8c)
- ブロック [`00bedd8c`](#insn-00bedd8c) 範囲 `[['00bedd8c', '00bedd8f']]`
  - `FALL_THROUGH` [`00bedd8c`](#insn-00bedd8c) → [`00bedd90`](#insn-00bedd90)
- ブロック [`00bedd90`](#insn-00bedd90) 範囲 `[['00bedd90', '00bedd9b']]`
  - `UNCONDITIONAL_JUMP` [`00bedd98`](#insn-00bedd98) → [`00bedda0`](#insn-00bedda0)
- ブロック [`00bedd9c`](#insn-00bedd9c) 範囲 `[['00bedd9c', '00bedd9f']]`
  - `FALL_THROUGH` [`00bedd9c`](#insn-00bedd9c) → [`00bedda0`](#insn-00bedda0)
- ブロック [`00bedda0`](#insn-00bedda0) 範囲 `[['00bedda0', '00beddab']]`
- ブロック [`00beddac`](#insn-00beddac) 範囲 `[['00beddac', '00beddbb']]`
  - `UNCONDITIONAL_JUMP` [`00beddb8`](#insn-00beddb8) → [`00bedda0`](#insn-00bedda0)

## 命令位置別の参照

- [`00bedb20`](#insn-00bedb20) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedb34`](#insn-00bedb34) → [`00bedb5c`](#insn-00bedb5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedb38`](#insn-00bedb38) → [`00bedd9c`](#insn-00bedd9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedb40`](#insn-00bedb40) → [`00bedbac`](#insn-00bedbac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedb50`](#insn-00bedb50) → [`00bedd9c`](#insn-00bedd9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedb58`](#insn-00bedb58) → [`00bedd90`](#insn-00bedd90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedb60`](#insn-00bedb60) → [`00bedb8c`](#insn-00bedb8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedb68`](#insn-00bedb68) → [`00bedbf0`](#insn-00bedbf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedb70`](#insn-00bedb70) → [`00bedbac`](#insn-00bedbac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedb84`](#insn-00bedb84) → [`00beddbc`](00beddbc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00beddbc` · 推定シンボル `None` · 推定型 `None`
- [`00bedb88`](#insn-00bedb88) → [`00bedd9c`](#insn-00bedd9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedb98`](#insn-00bedb98) → [`00bedc3c`](#insn-00bedc3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedba0`](#insn-00bedba0) → [`00bedd7c`](#insn-00bedd7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedba8`](#insn-00bedba8) → [`00bedd90`](#insn-00bedd90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedbc4`](#insn-00bedbc4) → [`00bedc60`](#insn-00bedc60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedbd4`](#insn-00bedbd4) → [`00bedc80`](#insn-00bedc80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedbe8`](#insn-00bedbe8) → [`00bedc80`](#insn-00bedc80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedbec`](#insn-00bedbec) → [`00bedc88`](#insn-00bedc88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc08`](#insn-00bedc08) → [`00bedd08`](#insn-00bedd08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc1c`](#insn-00bedc1c) → [`00bedd2c`](#insn-00bedd2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc34`](#insn-00bedc34) → [`00bedd2c`](#insn-00bedd2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc38`](#insn-00bedc38) → [`00bedd3c`](#insn-00bedd3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc40`](#insn-00bedc40) → [`00bedd9c`](#insn-00bedd9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc54`](#insn-00bedc54) → [`00bedd9c`](#insn-00bedd9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc5c`](#insn-00bedc5c) → [`00bedd9c`](#insn-00bedd9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc64`](#insn-00bedc64) → [`00bedc88`](#insn-00bedc88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc7c`](#insn-00bedc7c) → [`00bedc88`](#insn-00bedc88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc90`](#insn-00bedc90) → [`00bedd9c`](#insn-00bedd9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedc9c`](#insn-00bedc9c) → [`00bedccc`](#insn-00bedccc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedcb0`](#insn-00bedcb0) → [`00beddac`](#insn-00beddac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedcc8`](#insn-00bedcc8) → [`00bedd9c`](#insn-00bedd9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedcd8`](#insn-00bedcd8) → [`00bedcb4`](#insn-00bedcb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedce8`](#insn-00bedce8) → [`00bedca0`](#insn-00bedca0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedcfc`](#insn-00bedcfc) → [`00bedce0`](#insn-00bedce0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd04`](#insn-00bedd04) → [`00bedca4`](#insn-00bedca4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd0c`](#insn-00bedd0c) → [`00bedd3c`](#insn-00bedd3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd28`](#insn-00bedd28) → [`00bedd40`](#insn-00bedd40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd38`](#insn-00bedd38) → [`00bedd40`](#insn-00bedd40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd48`](#insn-00bedd48) → [`00bedd9c`](#insn-00bedd9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd60`](#insn-00bedd60) → [`00bedd9c`](#insn-00bedd9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd70`](#insn-00bedd70) → [`00bedd9c`](#insn-00bedd9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd78`](#insn-00bedd78) → [`00bedd9c`](#insn-00bedd9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd88`](#insn-00bedd88) → [`00bedd9c`](#insn-00bedd9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedd98`](#insn-00bedd98) → [`00bedda0`](#insn-00bedda0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedda0`](#insn-00bedda0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beddb8`](#insn-00beddb8) → [`00bedda0`](#insn-00bedda0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bedb20`](#insn-00bedb20)

~~~json
{
  "source": "00bedb20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedb34`](#insn-00bedb34)

~~~json
{
  "source": "00bedb34",
  "target": "00bedb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedb38`](#insn-00bedb38)

~~~json
{
  "source": "00bedb38",
  "target": "00bedd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedb40`](#insn-00bedb40)

~~~json
{
  "source": "00bedb40",
  "target": "00bedbac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedb50`](#insn-00bedb50)

~~~json
{
  "source": "00bedb50",
  "target": "00bedd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedb58`](#insn-00bedb58)

~~~json
{
  "source": "00bedb58",
  "target": "00bedd90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedb60`](#insn-00bedb60)

~~~json
{
  "source": "00bedb60",
  "target": "00bedb8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedb68`](#insn-00bedb68)

~~~json
{
  "source": "00bedb68",
  "target": "00bedbf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedb70`](#insn-00bedb70)

~~~json
{
  "source": "00bedb70",
  "target": "00bedbac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedb84`](#insn-00bedb84)

~~~json
{
  "source": "00bedb84",
  "target": "00beddbc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bedb88`](#insn-00bedb88)

~~~json
{
  "source": "00bedb88",
  "target": "00bedd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedb98`](#insn-00bedb98)

~~~json
{
  "source": "00bedb98",
  "target": "00bedc3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedba0`](#insn-00bedba0)

~~~json
{
  "source": "00bedba0",
  "target": "00bedd7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedba8`](#insn-00bedba8)

~~~json
{
  "source": "00bedba8",
  "target": "00bedd90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedbc4`](#insn-00bedbc4)

~~~json
{
  "source": "00bedbc4",
  "target": "00bedc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedbd4`](#insn-00bedbd4)

~~~json
{
  "source": "00bedbd4",
  "target": "00bedc80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedbe8`](#insn-00bedbe8)

~~~json
{
  "source": "00bedbe8",
  "target": "00bedc80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedbec`](#insn-00bedbec)

~~~json
{
  "source": "00bedbec",
  "target": "00bedc88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc08`](#insn-00bedc08)

~~~json
{
  "source": "00bedc08",
  "target": "00bedd08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc1c`](#insn-00bedc1c)

~~~json
{
  "source": "00bedc1c",
  "target": "00bedd2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc34`](#insn-00bedc34)

~~~json
{
  "source": "00bedc34",
  "target": "00bedd2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc38`](#insn-00bedc38)

~~~json
{
  "source": "00bedc38",
  "target": "00bedd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc40`](#insn-00bedc40)

~~~json
{
  "source": "00bedc40",
  "target": "00bedd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc54`](#insn-00bedc54)

~~~json
{
  "source": "00bedc54",
  "target": "00bedd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc5c`](#insn-00bedc5c)

~~~json
{
  "source": "00bedc5c",
  "target": "00bedd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc64`](#insn-00bedc64)

~~~json
{
  "source": "00bedc64",
  "target": "00bedc88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc7c`](#insn-00bedc7c)

~~~json
{
  "source": "00bedc7c",
  "target": "00bedc88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc90`](#insn-00bedc90)

~~~json
{
  "source": "00bedc90",
  "target": "00bedd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedc9c`](#insn-00bedc9c)

~~~json
{
  "source": "00bedc9c",
  "target": "00bedccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedcb0`](#insn-00bedcb0)

~~~json
{
  "source": "00bedcb0",
  "target": "00beddac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedcc8`](#insn-00bedcc8)

~~~json
{
  "source": "00bedcc8",
  "target": "00bedd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedcd8`](#insn-00bedcd8)

~~~json
{
  "source": "00bedcd8",
  "target": "00bedcb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedce8`](#insn-00bedce8)

~~~json
{
  "source": "00bedce8",
  "target": "00bedca0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedcfc`](#insn-00bedcfc)

~~~json
{
  "source": "00bedcfc",
  "target": "00bedce0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd04`](#insn-00bedd04)

~~~json
{
  "source": "00bedd04",
  "target": "00bedca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd0c`](#insn-00bedd0c)

~~~json
{
  "source": "00bedd0c",
  "target": "00bedd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd28`](#insn-00bedd28)

~~~json
{
  "source": "00bedd28",
  "target": "00bedd40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd38`](#insn-00bedd38)

~~~json
{
  "source": "00bedd38",
  "target": "00bedd40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd48`](#insn-00bedd48)

~~~json
{
  "source": "00bedd48",
  "target": "00bedd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd60`](#insn-00bedd60)

~~~json
{
  "source": "00bedd60",
  "target": "00bedd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd70`](#insn-00bedd70)

~~~json
{
  "source": "00bedd70",
  "target": "00bedd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd78`](#insn-00bedd78)

~~~json
{
  "source": "00bedd78",
  "target": "00bedd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd88`](#insn-00bedd88)

~~~json
{
  "source": "00bedd88",
  "target": "00bedd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedd98`](#insn-00bedd98)

~~~json
{
  "source": "00bedd98",
  "target": "00bedda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedda0`](#insn-00bedda0)

~~~json
{
  "source": "00bedda0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beddb8`](#insn-00beddb8)

~~~json
{
  "source": "00beddb8",
  "target": "00bedda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
