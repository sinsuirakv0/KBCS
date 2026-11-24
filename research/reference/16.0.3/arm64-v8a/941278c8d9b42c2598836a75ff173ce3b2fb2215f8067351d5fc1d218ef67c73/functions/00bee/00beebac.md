# 00beebac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 要確認
  - [v16.0.2 → v16.0.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/review-0083.md#review-9989b832c1191af3e2710688acafd5c5)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00beebac",
  "name": "FUN_00beebac",
  "size": 672,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "16c0bfdb5a054746e8bc483993d9729f218c1e7569eb0d9be8521aec2dee3651",
  "source_text_sha256": "16c0bfdb5a054746e8bc483993d9729f218c1e7569eb0d9be8521aec2dee3651",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00beebac",
        "00beee4b"
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

- [00be81a0](../00be8/00be81a0.md)

## 呼び出し先

- [00beee4c](../00bee/00beee4c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4555 bytes

~~~c

bool FUN_00beebac(ulong *param_1,ulong *param_2)

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
      goto LAB_00beee20;
    }
    if (uVar3 != 4) {
      if (uVar3 == 5) {
        FUN_00beee4c(param_1,param_1 + 1,param_1 + 2,param_1 + 3,param_2 + -1);
        return true;
      }
      goto LAB_00beec3c;
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
                    /* try { // try from 00beeca8 to 00ceecaf has its CatchHandler @ 00beed00 */
      if (uVar3 <= uVar11) {
                    /* try { // try from 00beecb0 to 00ceedf3 has its CatchHandler @ 00bee9e0 */
        *param_1 = uVar3;
        param_1[1] = uVar5;
        uVar3 = uVar11;
        puVar9 = puVar10;
        goto joined_r0x00beedb8;
      }
    }
    else {
      uVar8 = uVar11;
      if (uVar3 <= uVar11) goto LAB_00beedd0;
      *puVar10 = uVar11;
      *puVar6 = uVar3;
      puVar13 = puVar10;
      uVar2 = uVar3;
joined_r0x00beedb8:
      uVar8 = uVar3;
      if (uVar5 <= uVar11) goto LAB_00beedd0;
    }
    *puVar9 = uVar11;
    *puVar13 = uVar5;
    uVar8 = uVar2;
LAB_00beedd0:
                    /* catch() { ... } // from try @ 00beea90 with catch @ 00beedd4 */
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
LAB_00beee20:
    param_2[-1] = uVar3;
    return true;
  }
LAB_00beec3c:
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
      goto joined_r0x00beed0c;
    }
  }
  else {
    if (uVar11 <= uVar5) goto LAB_00beed18;
                    /* catch() { ... } // from try @ 00beeca8 with catch @ 00beed00 */
    *puVar6 = uVar5;
    *puVar10 = uVar11;
    puVar13 = puVar6;
joined_r0x00beed0c:
    if (uVar3 <= uVar5) goto LAB_00beed18;
  }
  *puVar9 = uVar5;
  *puVar13 = uVar3;
LAB_00beed18:
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
          if (lVar1 == 0) goto LAB_00beed34;
          uVar3 = *(ulong *)((long)param_1 + lVar12 + -0x10);
          lVar12 = lVar1;
        } while (uVar5 < uVar3);
        puVar9 = (ulong *)((long)param_1 + lVar1);
LAB_00beed34:
        iVar4 = iVar4 + 1;
                    /* catch() { ... } // from try @ 00beea84 with catch @ 00beed38 */
        *puVar9 = uVar5;
        if (iVar4 == 8) {
          return puVar6 + 1 == param_2;
        }
      }
                    /* catch() { ... } // from try @ 00beeacc with catch @ 00beed48 */
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
<a id="insn-00beebac"></a> `00beebac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00beebb0"></a> `00beebb0` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00beebb4"></a> `00beebb4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00beebb8"></a> `00beebb8` | `28 00 00 cb` | sub x8,x1,x0 | `FALL_THROUGH`
<a id="insn-00beebbc"></a> `00beebbc` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00beebc0"></a> `00beebc0` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00beebc4"></a> `00beebc4` | `4c 01 00 54` | b.gt 0x00beebec | `CONDITIONAL_JUMP`
<a id="insn-00beebc8"></a> `00beebc8` | `23 13 00 54` | b.cc 0x00beee2c | `CONDITIONAL_JUMP`
<a id="insn-00beebcc"></a> `00beebcc` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00beebd0"></a> `00beebd0` | `61 03 00 54` | b.ne 0x00beec3c | `CONDITIONAL_JUMP`
<a id="insn-00beebd4"></a> `00beebd4` | `29 80 5f f8` | ldur x9,[x1, #-0x8] | `FALL_THROUGH`
<a id="insn-00beebd8"></a> `00beebd8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00beebdc"></a> `00beebdc` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00beebe0"></a> `00beebe0` | `62 12 00 54` | b.cs 0x00beee2c | `CONDITIONAL_JUMP`
<a id="insn-00beebe4"></a> `00beebe4` | `09 00 00 f9` | str x9,[x0] | `FALL_THROUGH`
<a id="insn-00beebe8"></a> `00beebe8` | `8e 00 00 14` | b 0x00beee20 | `UNCONDITIONAL_JUMP`
<a id="insn-00beebec"></a> `00beebec` | `1f 0d 00 f1` | cmp x8,#0x3 | `FALL_THROUGH`
<a id="insn-00beebf0"></a> `00beebf0` | `60 01 00 54` | b.eq 0x00beec1c | `CONDITIONAL_JUMP`
<a id="insn-00beebf4"></a> `00beebf4` | `1f 11 00 f1` | cmp x8,#0x4 | `FALL_THROUGH`
<a id="insn-00beebf8"></a> `00beebf8` | `40 04 00 54` | b.eq 0x00beec80 | `CONDITIONAL_JUMP`
<a id="insn-00beebfc"></a> `00beebfc` | `1f 15 00 f1` | cmp x8,#0x5 | `FALL_THROUGH`
<a id="insn-00beec00"></a> `00beec00` | `e1 01 00 54` | b.ne 0x00beec3c | `CONDITIONAL_JUMP`
<a id="insn-00beec04"></a> `00beec04` | `24 20 00 d1` | sub x4,x1,#0x8 | `FALL_THROUGH`
<a id="insn-00beec08"></a> `00beec08` | `01 20 00 91` | add x1,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00beec0c"></a> `00beec0c` | `02 40 00 91` | add x2,x0,#0x10 | `FALL_THROUGH`
<a id="insn-00beec10"></a> `00beec10` | `03 60 00 91` | add x3,x0,#0x18 | `FALL_THROUGH`
<a id="insn-00beec14"></a> `00beec14` | `8e 00 00 94` | bl 0x00beee4c | `UNCONDITIONAL_CALL`
<a id="insn-00beec18"></a> `00beec18` | `85 00 00 14` | b 0x00beee2c | `UNCONDITIONAL_JUMP`
<a id="insn-00beec1c"></a> `00beec1c` | `08 24 40 a9` | ldp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00beec20"></a> `00beec20` | `2a 80 5f f8` | ldur x10,[x1, #-0x8] | `FALL_THROUGH`
<a id="insn-00beec24"></a> `00beec24` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00beec28"></a> `00beec28` | `22 05 00 54` | b.cs 0x00beeccc | `CONDITIONAL_JUMP`
<a id="insn-00beec2c"></a> `00beec2c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00beec30"></a> `00beec30` | `e2 0e 00 54` | b.cs 0x00beee0c | `CONDITIONAL_JUMP`
<a id="insn-00beec34"></a> `00beec34` | `0a 00 00 f9` | str x10,[x0] | `FALL_THROUGH`
<a id="insn-00beec38"></a> `00beec38` | `7a 00 00 14` | b 0x00beee20 | `UNCONDITIONAL_JUMP`
<a id="insn-00beec3c"></a> `00beec3c` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00beec40"></a> `00beec40` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00beec44"></a> `00beec44` | `eb 03 00 aa` | mov x11,x0 | `FALL_THROUGH`
<a id="insn-00beec48"></a> `00beec48` | `4c 8d 40 f8` | ldr x12,[x10, #0x8]! | `FALL_THROUGH`
<a id="insn-00beec4c"></a> `00beec4c` | `69 0d 41 f8` | ldr x9,[x11, #0x10]! | `FALL_THROUGH`
<a id="insn-00beec50"></a> `00beec50` | `9f 01 08 eb` | cmp x12,x8 | `FALL_THROUGH`
<a id="insn-00beec54"></a> `00beec54` | `e2 04 00 54` | b.cs 0x00beecf0 | `CONDITIONAL_JUMP`
<a id="insn-00beec58"></a> `00beec58` | `3f 01 0c eb` | cmp x9,x12 | `FALL_THROUGH`
<a id="insn-00beec5c"></a> `00beec5c` | `ed 03 00 aa` | mov x13,x0 | `FALL_THROUGH`
<a id="insn-00beec60"></a> `00beec60` | `ee 03 0b aa` | mov x14,x11 | `FALL_THROUGH`
<a id="insn-00beec64"></a> `00beec64` | `63 05 00 54` | b.cc 0x00beed10 | `CONDITIONAL_JUMP`
<a id="insn-00beec68"></a> `00beec68` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00beec6c"></a> `00beec6c` | `ed 03 0a aa` | mov x13,x10 | `FALL_THROUGH`
<a id="insn-00beec70"></a> `00beec70` | `ee 03 0b aa` | mov x14,x11 | `FALL_THROUGH`
<a id="insn-00beec74"></a> `00beec74` | `0c 20 00 a9` | stp x12,x8,[x0] | `FALL_THROUGH`
<a id="insn-00beec78"></a> `00beec78` | `c3 04 00 54` | b.cc 0x00beed10 | `CONDITIONAL_JUMP`
<a id="insn-00beec7c"></a> `00beec7c` | `27 00 00 14` | b 0x00beed18 | `UNCONDITIONAL_JUMP`
<a id="insn-00beec80"></a> `00beec80` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00beec84"></a> `00beec84` | `0b 00 40 f9` | ldr x11,[x0] | `FALL_THROUGH`
<a id="insn-00beec88"></a> `00beec88` | `e9 03 00 aa` | mov x9,x0 | `FALL_THROUGH`
<a id="insn-00beec8c"></a> `00beec8c` | `0a 8d 40 f8` | ldr x10,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00beec90"></a> `00beec90` | `2c 0d 41 f8` | ldr x12,[x9, #0x10]! | `FALL_THROUGH`
<a id="insn-00beec94"></a> `00beec94` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-00beec98"></a> `00beec98` | `02 08 00 54` | b.cs 0x00beed98 | `CONDITIONAL_JUMP`
<a id="insn-00beec9c"></a> `00beec9c` | `9f 01 0a eb` | cmp x12,x10 | `FALL_THROUGH`
<a id="insn-00beeca0"></a> `00beeca0` | `ed 03 00 aa` | mov x13,x0 | `FALL_THROUGH`
<a id="insn-00beeca4"></a> `00beeca4` | `ee 03 09 aa` | mov x14,x9 | `FALL_THROUGH`
<a id="insn-00beeca8"></a> `00beeca8` | `e2 03 0b aa` | mov x2,x11 | `FALL_THROUGH`
<a id="insn-00beecac"></a> `00beecac` | `83 08 00 54` | b.cc 0x00beedbc | `CONDITIONAL_JUMP`
<a id="insn-00beecb0"></a> `00beecb0` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00beecb4"></a> `00beecb4` | `ed 03 08 aa` | mov x13,x8 | `FALL_THROUGH`
<a id="insn-00beecb8"></a> `00beecb8` | `ee 03 09 aa` | mov x14,x9 | `FALL_THROUGH`
<a id="insn-00beecbc"></a> `00beecbc` | `e2 03 0b aa` | mov x2,x11 | `FALL_THROUGH`
<a id="insn-00beecc0"></a> `00beecc0` | `0a 2c 00 a9` | stp x10,x11,[x0] | `FALL_THROUGH`
<a id="insn-00beecc4"></a> `00beecc4` | `c3 07 00 54` | b.cc 0x00beedbc | `CONDITIONAL_JUMP`
<a id="insn-00beecc8"></a> `00beecc8` | `41 00 00 14` | b 0x00beedcc | `UNCONDITIONAL_JUMP`
<a id="insn-00beeccc"></a> `00beeccc` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00beecd0"></a> `00beecd0` | `e2 0a 00 54` | b.cs 0x00beee2c | `CONDITIONAL_JUMP`
<a id="insn-00beecd4"></a> `00beecd4` | `0a 04 00 f9` | str x10,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00beecd8"></a> `00beecd8` | `29 80 1f f8` | stur x9,[x1, #-0x8] | `FALL_THROUGH`
<a id="insn-00beecdc"></a> `00beecdc` | `08 24 40 a9` | ldp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00beece0"></a> `00beece0` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00beece4"></a> `00beece4` | `42 0a 00 54` | b.cs 0x00beee2c | `CONDITIONAL_JUMP`
<a id="insn-00beece8"></a> `00beece8` | `09 20 00 a9` | stp x9,x8,[x0] | `FALL_THROUGH`
<a id="insn-00beecec"></a> `00beecec` | `50 00 00 14` | b 0x00beee2c | `UNCONDITIONAL_JUMP`
<a id="insn-00beecf0"></a> `00beecf0` | `3f 01 0c eb` | cmp x9,x12 | `FALL_THROUGH`
<a id="insn-00beecf4"></a> `00beecf4` | `22 01 00 54` | b.cs 0x00beed18 | `CONDITIONAL_JUMP`
<a id="insn-00beecf8"></a> `00beecf8` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00beecfc"></a> `00beecfc` | `ed 03 00 aa` | mov x13,x0 | `FALL_THROUGH`
<a id="insn-00beed00"></a> `00beed00` | `ee 03 0a aa` | mov x14,x10 | `FALL_THROUGH`
<a id="insn-00beed04"></a> `00beed04` | `49 01 00 f9` | str x9,[x10] | `FALL_THROUGH`
<a id="insn-00beed08"></a> `00beed08` | `6c 01 00 f9` | str x12,[x11] | `FALL_THROUGH`
<a id="insn-00beed0c"></a> `00beed0c` | `62 00 00 54` | b.cs 0x00beed18 | `CONDITIONAL_JUMP`
<a id="insn-00beed10"></a> `00beed10` | `a9 01 00 f9` | str x9,[x13] | `FALL_THROUGH`
<a id="insn-00beed14"></a> `00beed14` | `c8 01 00 f9` | str x8,[x14] | `FALL_THROUGH`
<a id="insn-00beed18"></a> `00beed18` | `08 60 00 91` | add x8,x0,#0x18 | `FALL_THROUGH`
<a id="insn-00beed1c"></a> `00beed1c` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00beed20"></a> `00beed20` | `60 08 00 54` | b.eq 0x00beee2c | `CONDITIONAL_JUMP`
<a id="insn-00beed24"></a> `00beed24` | `e9 03 1f 2a` | mov w9,wzr | `FALL_THROUGH`
<a id="insn-00beed28"></a> `00beed28` | `0a 03 80 52` | mov w10,#0x18 | `FALL_THROUGH`
<a id="insn-00beed2c"></a> `00beed2c` | `0c 00 00 14` | b 0x00beed5c | `UNCONDITIONAL_JUMP`
<a id="insn-00beed30"></a> `00beed30` | `eb 03 00 aa` | mov x11,x0 | `FALL_THROUGH`
<a id="insn-00beed34"></a> `00beed34` | `29 05 00 11` | add w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00beed38"></a> `00beed38` | `6c 01 00 f9` | str x12,[x11] | `FALL_THROUGH`
<a id="insn-00beed3c"></a> `00beed3c` | `3f 21 00 71` | cmp w9,#0x8 | `FALL_THROUGH`
<a id="insn-00beed40"></a> `00beed40` | `e0 07 00 54` | b.eq 0x00beee3c | `CONDITIONAL_JUMP`
<a id="insn-00beed44"></a> `00beed44` | `0c 21 00 91` | add x12,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00beed48"></a> `00beed48` | `eb 03 08 aa` | mov x11,x8 | `FALL_THROUGH`
<a id="insn-00beed4c"></a> `00beed4c` | `4a 21 00 91` | add x10,x10,#0x8 | `FALL_THROUGH`
<a id="insn-00beed50"></a> `00beed50` | `9f 01 01 eb` | cmp x12,x1 | `FALL_THROUGH`
<a id="insn-00beed54"></a> `00beed54` | `e8 03 0c aa` | mov x8,x12 | `FALL_THROUGH`
<a id="insn-00beed58"></a> `00beed58` | `a0 06 00 54` | b.eq 0x00beee2c | `CONDITIONAL_JUMP`
<a id="insn-00beed5c"></a> `00beed5c` | `0c 01 40 f9` | ldr x12,[x8] | `FALL_THROUGH`
<a id="insn-00beed60"></a> `00beed60` | `6b 01 40 f9` | ldr x11,[x11] | `FALL_THROUGH`
<a id="insn-00beed64"></a> `00beed64` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00beed68"></a> `00beed68` | `e2 fe ff 54` | b.cs 0x00beed44 | `CONDITIONAL_JUMP`
<a id="insn-00beed6c"></a> `00beed6c` | `ee 03 0a aa` | mov x14,x10 | `FALL_THROUGH`
<a id="insn-00beed70"></a> `00beed70` | `cd 21 00 f1` | subs x13,x14,#0x8 | `FALL_THROUGH`
<a id="insn-00beed74"></a> `00beed74` | `0b 68 2e f8` | str x11,[x0, x14, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00beed78"></a> `00beed78` | `c0 fd ff 54` | b.eq 0x00beed30 | `CONDITIONAL_JUMP`
<a id="insn-00beed7c"></a> `00beed7c` | `0b 00 0e 8b` | add x11,x0,x14 | `FALL_THROUGH`
<a id="insn-00beed80"></a> `00beed80` | `ee 03 0d aa` | mov x14,x13 | `FALL_THROUGH`
<a id="insn-00beed84"></a> `00beed84` | `6b 01 5f f8` | ldur x11,[x11, #-0x10] | `FALL_THROUGH`
<a id="insn-00beed88"></a> `00beed88` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00beed8c"></a> `00beed8c` | `23 ff ff 54` | b.cc 0x00beed70 | `CONDITIONAL_JUMP`
<a id="insn-00beed90"></a> `00beed90` | `0b 00 0d 8b` | add x11,x0,x13 | `FALL_THROUGH`
<a id="insn-00beed94"></a> `00beed94` | `e8 ff ff 17` | b 0x00beed34 | `UNCONDITIONAL_JUMP`
<a id="insn-00beed98"></a> `00beed98` | `9f 01 0a eb` | cmp x12,x10 | `FALL_THROUGH`
<a id="insn-00beed9c"></a> `00beed9c` | `82 01 00 54` | b.cs 0x00beedcc | `CONDITIONAL_JUMP`
<a id="insn-00beeda0"></a> `00beeda0` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00beeda4"></a> `00beeda4` | `ed 03 00 aa` | mov x13,x0 | `FALL_THROUGH`
<a id="insn-00beeda8"></a> `00beeda8` | `ee 03 08 aa` | mov x14,x8 | `FALL_THROUGH`
<a id="insn-00beedac"></a> `00beedac` | `e2 03 0a aa` | mov x2,x10 | `FALL_THROUGH`
<a id="insn-00beedb0"></a> `00beedb0` | `0c 01 00 f9` | str x12,[x8] | `FALL_THROUGH`
<a id="insn-00beedb4"></a> `00beedb4` | `2a 01 00 f9` | str x10,[x9] | `FALL_THROUGH`
<a id="insn-00beedb8"></a> `00beedb8` | `c2 00 00 54` | b.cs 0x00beedd0 | `CONDITIONAL_JUMP`
<a id="insn-00beedbc"></a> `00beedbc` | `ea 03 02 aa` | mov x10,x2 | `FALL_THROUGH`
<a id="insn-00beedc0"></a> `00beedc0` | `ac 01 00 f9` | str x12,[x13] | `FALL_THROUGH`
<a id="insn-00beedc4"></a> `00beedc4` | `cb 01 00 f9` | str x11,[x14] | `FALL_THROUGH`
<a id="insn-00beedc8"></a> `00beedc8` | `02 00 00 14` | b 0x00beedd0 | `UNCONDITIONAL_JUMP`
<a id="insn-00beedcc"></a> `00beedcc` | `ea 03 0c aa` | mov x10,x12 | `FALL_THROUGH`
<a id="insn-00beedd0"></a> `00beedd0` | `2b 80 5f f8` | ldur x11,[x1, #-0x8] | `FALL_THROUGH`
<a id="insn-00beedd4"></a> `00beedd4` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00beedd8"></a> `00beedd8` | `a2 02 00 54` | b.cs 0x00beee2c | `CONDITIONAL_JUMP`
<a id="insn-00beeddc"></a> `00beeddc` | `2b 01 00 f9` | str x11,[x9] | `FALL_THROUGH`
<a id="insn-00beede0"></a> `00beede0` | `2a 80 1f f8` | stur x10,[x1, #-0x8] | `FALL_THROUGH`
<a id="insn-00beede4"></a> `00beede4` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00beede8"></a> `00beede8` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00beedec"></a> `00beedec` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00beedf0"></a> `00beedf0` | `e2 01 00 54` | b.cs 0x00beee2c | `CONDITIONAL_JUMP`
<a id="insn-00beedf4"></a> `00beedf4` | `0a 00 40 f9` | ldr x10,[x0] | `FALL_THROUGH`
<a id="insn-00beedf8"></a> `00beedf8` | `09 a0 00 a9` | stp x9,x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00beedfc"></a> `00beedfc` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00beee00"></a> `00beee00` | `62 01 00 54` | b.cs 0x00beee2c | `CONDITIONAL_JUMP`
<a id="insn-00beee04"></a> `00beee04` | `09 28 00 a9` | stp x9,x10,[x0] | `FALL_THROUGH`
<a id="insn-00beee08"></a> `00beee08` | `09 00 00 14` | b 0x00beee2c | `UNCONDITIONAL_JUMP`
<a id="insn-00beee0c"></a> `00beee0c` | `09 20 00 a9` | stp x9,x8,[x0] | `FALL_THROUGH`
<a id="insn-00beee10"></a> `00beee10` | `29 80 5f f8` | ldur x9,[x1, #-0x8] | `FALL_THROUGH`
<a id="insn-00beee14"></a> `00beee14` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00beee18"></a> `00beee18` | `a2 00 00 54` | b.cs 0x00beee2c | `CONDITIONAL_JUMP`
<a id="insn-00beee1c"></a> `00beee1c` | `09 04 00 f9` | str x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00beee20"></a> `00beee20` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00beee24"></a> `00beee24` | `28 80 1f f8` | stur x8,[x1, #-0x8] | `FALL_THROUGH`
<a id="insn-00beee28"></a> `00beee28` | `02 00 00 14` | b 0x00beee30 | `UNCONDITIONAL_JUMP`
<a id="insn-00beee2c"></a> `00beee2c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00beee30"></a> `00beee30` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00beee34"></a> `00beee34` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00beee38"></a> `00beee38` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00beee3c"></a> `00beee3c` | `08 21 00 91` | add x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00beee40"></a> `00beee40` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00beee44"></a> `00beee44` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00beee48"></a> `00beee48` | `fa ff ff 17` | b 0x00beee30 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00beebac`](#insn-00beebac) 範囲 `[['00beebac', '00beebc7']]`
  - `CONDITIONAL_JUMP` [`00beebc4`](#insn-00beebc4) → [`00beebec`](#insn-00beebec)
  - `FALL_THROUGH` [`00beebc4`](#insn-00beebc4) → [`00beebc8`](#insn-00beebc8)
- ブロック [`00beebc8`](#insn-00beebc8) 範囲 `[['00beebc8', '00beebcb']]`
  - `CONDITIONAL_JUMP` [`00beebc8`](#insn-00beebc8) → [`00beee2c`](#insn-00beee2c)
  - `FALL_THROUGH` [`00beebc8`](#insn-00beebc8) → [`00beebcc`](#insn-00beebcc)
- ブロック [`00beebcc`](#insn-00beebcc) 範囲 `[['00beebcc', '00beebd3']]`
  - `CONDITIONAL_JUMP` [`00beebd0`](#insn-00beebd0) → [`00beec3c`](#insn-00beec3c)
  - `FALL_THROUGH` [`00beebd0`](#insn-00beebd0) → [`00beebd4`](#insn-00beebd4)
- ブロック [`00beebd4`](#insn-00beebd4) 範囲 `[['00beebd4', '00beebe3']]`
  - `CONDITIONAL_JUMP` [`00beebe0`](#insn-00beebe0) → [`00beee2c`](#insn-00beee2c)
  - `FALL_THROUGH` [`00beebe0`](#insn-00beebe0) → [`00beebe4`](#insn-00beebe4)
- ブロック [`00beebe4`](#insn-00beebe4) 範囲 `[['00beebe4', '00beebeb']]`
  - `UNCONDITIONAL_JUMP` [`00beebe8`](#insn-00beebe8) → [`00beee20`](#insn-00beee20)
- ブロック [`00beebec`](#insn-00beebec) 範囲 `[['00beebec', '00beebf3']]`
  - `CONDITIONAL_JUMP` [`00beebf0`](#insn-00beebf0) → [`00beec1c`](#insn-00beec1c)
  - `FALL_THROUGH` [`00beebf0`](#insn-00beebf0) → [`00beebf4`](#insn-00beebf4)
- ブロック [`00beebf4`](#insn-00beebf4) 範囲 `[['00beebf4', '00beebfb']]`
  - `CONDITIONAL_JUMP` [`00beebf8`](#insn-00beebf8) → [`00beec80`](#insn-00beec80)
  - `FALL_THROUGH` [`00beebf8`](#insn-00beebf8) → [`00beebfc`](#insn-00beebfc)
- ブロック [`00beebfc`](#insn-00beebfc) 範囲 `[['00beebfc', '00beec03']]`
  - `CONDITIONAL_JUMP` [`00beec00`](#insn-00beec00) → [`00beec3c`](#insn-00beec3c)
  - `FALL_THROUGH` [`00beec00`](#insn-00beec00) → [`00beec04`](#insn-00beec04)
- ブロック [`00beec04`](#insn-00beec04) 範囲 `[['00beec04', '00beec1b']]`
  - `UNCONDITIONAL_JUMP` [`00beec18`](#insn-00beec18) → [`00beee2c`](#insn-00beee2c)
- ブロック [`00beec1c`](#insn-00beec1c) 範囲 `[['00beec1c', '00beec2b']]`
  - `CONDITIONAL_JUMP` [`00beec28`](#insn-00beec28) → [`00beeccc`](#insn-00beeccc)
  - `FALL_THROUGH` [`00beec28`](#insn-00beec28) → [`00beec2c`](#insn-00beec2c)
- ブロック [`00beec2c`](#insn-00beec2c) 範囲 `[['00beec2c', '00beec33']]`
  - `CONDITIONAL_JUMP` [`00beec30`](#insn-00beec30) → [`00beee0c`](#insn-00beee0c)
  - `FALL_THROUGH` [`00beec30`](#insn-00beec30) → [`00beec34`](#insn-00beec34)
- ブロック [`00beec34`](#insn-00beec34) 範囲 `[['00beec34', '00beec3b']]`
  - `UNCONDITIONAL_JUMP` [`00beec38`](#insn-00beec38) → [`00beee20`](#insn-00beee20)
- ブロック [`00beec3c`](#insn-00beec3c) 範囲 `[['00beec3c', '00beec57']]`
  - `CONDITIONAL_JUMP` [`00beec54`](#insn-00beec54) → [`00beecf0`](#insn-00beecf0)
  - `FALL_THROUGH` [`00beec54`](#insn-00beec54) → [`00beec58`](#insn-00beec58)
- ブロック [`00beec58`](#insn-00beec58) 範囲 `[['00beec58', '00beec67']]`
  - `CONDITIONAL_JUMP` [`00beec64`](#insn-00beec64) → [`00beed10`](#insn-00beed10)
  - `FALL_THROUGH` [`00beec64`](#insn-00beec64) → [`00beec68`](#insn-00beec68)
- ブロック [`00beec68`](#insn-00beec68) 範囲 `[['00beec68', '00beec7b']]`
  - `CONDITIONAL_JUMP` [`00beec78`](#insn-00beec78) → [`00beed10`](#insn-00beed10)
  - `FALL_THROUGH` [`00beec78`](#insn-00beec78) → [`00beec7c`](#insn-00beec7c)
- ブロック [`00beec7c`](#insn-00beec7c) 範囲 `[['00beec7c', '00beec7f']]`
  - `UNCONDITIONAL_JUMP` [`00beec7c`](#insn-00beec7c) → [`00beed18`](#insn-00beed18)
- ブロック [`00beec80`](#insn-00beec80) 範囲 `[['00beec80', '00beec9b']]`
  - `CONDITIONAL_JUMP` [`00beec98`](#insn-00beec98) → [`00beed98`](#insn-00beed98)
  - `FALL_THROUGH` [`00beec98`](#insn-00beec98) → [`00beec9c`](#insn-00beec9c)
- ブロック [`00beec9c`](#insn-00beec9c) 範囲 `[['00beec9c', '00beeca7']]`
  - `FALL_THROUGH` [`00beeca4`](#insn-00beeca4) → [`00beeca8`](#insn-00beeca8)
- ブロック [`00beeca8`](#insn-00beeca8) 範囲 `[['00beeca8', '00beecaf']]`
  - `CONDITIONAL_JUMP` [`00beecac`](#insn-00beecac) → [`00beedbc`](#insn-00beedbc)
  - `FALL_THROUGH` [`00beecac`](#insn-00beecac) → [`00beecb0`](#insn-00beecb0)
- ブロック [`00beecb0`](#insn-00beecb0) 範囲 `[['00beecb0', '00beecc7']]`
  - `CONDITIONAL_JUMP` [`00beecc4`](#insn-00beecc4) → [`00beedbc`](#insn-00beedbc)
  - `FALL_THROUGH` [`00beecc4`](#insn-00beecc4) → [`00beecc8`](#insn-00beecc8)
- ブロック [`00beecc8`](#insn-00beecc8) 範囲 `[['00beecc8', '00beeccb']]`
  - `UNCONDITIONAL_JUMP` [`00beecc8`](#insn-00beecc8) → [`00beedcc`](#insn-00beedcc)
- ブロック [`00beeccc`](#insn-00beeccc) 範囲 `[['00beeccc', '00beecd3']]`
  - `CONDITIONAL_JUMP` [`00beecd0`](#insn-00beecd0) → [`00beee2c`](#insn-00beee2c)
  - `FALL_THROUGH` [`00beecd0`](#insn-00beecd0) → [`00beecd4`](#insn-00beecd4)
- ブロック [`00beecd4`](#insn-00beecd4) 範囲 `[['00beecd4', '00beece7']]`
  - `CONDITIONAL_JUMP` [`00beece4`](#insn-00beece4) → [`00beee2c`](#insn-00beee2c)
  - `FALL_THROUGH` [`00beece4`](#insn-00beece4) → [`00beece8`](#insn-00beece8)
- ブロック [`00beece8`](#insn-00beece8) 範囲 `[['00beece8', '00beecef']]`
  - `UNCONDITIONAL_JUMP` [`00beecec`](#insn-00beecec) → [`00beee2c`](#insn-00beee2c)
- ブロック [`00beecf0`](#insn-00beecf0) 範囲 `[['00beecf0', '00beecf7']]`
  - `CONDITIONAL_JUMP` [`00beecf4`](#insn-00beecf4) → [`00beed18`](#insn-00beed18)
  - `FALL_THROUGH` [`00beecf4`](#insn-00beecf4) → [`00beecf8`](#insn-00beecf8)
- ブロック [`00beecf8`](#insn-00beecf8) 範囲 `[['00beecf8', '00beecff']]`
  - `FALL_THROUGH` [`00beecfc`](#insn-00beecfc) → [`00beed00`](#insn-00beed00)
- ブロック [`00beed00`](#insn-00beed00) 範囲 `[['00beed00', '00beed0f']]`
  - `CONDITIONAL_JUMP` [`00beed0c`](#insn-00beed0c) → [`00beed18`](#insn-00beed18)
  - `FALL_THROUGH` [`00beed0c`](#insn-00beed0c) → [`00beed10`](#insn-00beed10)
- ブロック [`00beed10`](#insn-00beed10) 範囲 `[['00beed10', '00beed17']]`
  - `FALL_THROUGH` [`00beed14`](#insn-00beed14) → [`00beed18`](#insn-00beed18)
- ブロック [`00beed18`](#insn-00beed18) 範囲 `[['00beed18', '00beed23']]`
  - `CONDITIONAL_JUMP` [`00beed20`](#insn-00beed20) → [`00beee2c`](#insn-00beee2c)
  - `FALL_THROUGH` [`00beed20`](#insn-00beed20) → [`00beed24`](#insn-00beed24)
- ブロック [`00beed24`](#insn-00beed24) 範囲 `[['00beed24', '00beed2f']]`
  - `UNCONDITIONAL_JUMP` [`00beed2c`](#insn-00beed2c) → [`00beed5c`](#insn-00beed5c)
- ブロック [`00beed30`](#insn-00beed30) 範囲 `[['00beed30', '00beed33']]`
  - `FALL_THROUGH` [`00beed30`](#insn-00beed30) → [`00beed34`](#insn-00beed34)
- ブロック [`00beed34`](#insn-00beed34) 範囲 `[['00beed34', '00beed37']]`
  - `FALL_THROUGH` [`00beed34`](#insn-00beed34) → [`00beed38`](#insn-00beed38)
- ブロック [`00beed38`](#insn-00beed38) 範囲 `[['00beed38', '00beed43']]`
  - `CONDITIONAL_JUMP` [`00beed40`](#insn-00beed40) → [`00beee3c`](#insn-00beee3c)
  - `FALL_THROUGH` [`00beed40`](#insn-00beed40) → [`00beed44`](#insn-00beed44)
- ブロック [`00beed44`](#insn-00beed44) 範囲 `[['00beed44', '00beed47']]`
  - `FALL_THROUGH` [`00beed44`](#insn-00beed44) → [`00beed48`](#insn-00beed48)
- ブロック [`00beed48`](#insn-00beed48) 範囲 `[['00beed48', '00beed5b']]`
  - `CONDITIONAL_JUMP` [`00beed58`](#insn-00beed58) → [`00beee2c`](#insn-00beee2c)
  - `FALL_THROUGH` [`00beed58`](#insn-00beed58) → [`00beed5c`](#insn-00beed5c)
- ブロック [`00beed5c`](#insn-00beed5c) 範囲 `[['00beed5c', '00beed6b']]`
  - `CONDITIONAL_JUMP` [`00beed68`](#insn-00beed68) → [`00beed44`](#insn-00beed44)
  - `FALL_THROUGH` [`00beed68`](#insn-00beed68) → [`00beed6c`](#insn-00beed6c)
- ブロック [`00beed6c`](#insn-00beed6c) 範囲 `[['00beed6c', '00beed6f']]`
  - `FALL_THROUGH` [`00beed6c`](#insn-00beed6c) → [`00beed70`](#insn-00beed70)
- ブロック [`00beed70`](#insn-00beed70) 範囲 `[['00beed70', '00beed7b']]`
  - `CONDITIONAL_JUMP` [`00beed78`](#insn-00beed78) → [`00beed30`](#insn-00beed30)
  - `FALL_THROUGH` [`00beed78`](#insn-00beed78) → [`00beed7c`](#insn-00beed7c)
- ブロック [`00beed7c`](#insn-00beed7c) 範囲 `[['00beed7c', '00beed8f']]`
  - `CONDITIONAL_JUMP` [`00beed8c`](#insn-00beed8c) → [`00beed70`](#insn-00beed70)
  - `FALL_THROUGH` [`00beed8c`](#insn-00beed8c) → [`00beed90`](#insn-00beed90)
- ブロック [`00beed90`](#insn-00beed90) 範囲 `[['00beed90', '00beed97']]`
  - `UNCONDITIONAL_JUMP` [`00beed94`](#insn-00beed94) → [`00beed34`](#insn-00beed34)
- ブロック [`00beed98`](#insn-00beed98) 範囲 `[['00beed98', '00beed9f']]`
  - `CONDITIONAL_JUMP` [`00beed9c`](#insn-00beed9c) → [`00beedcc`](#insn-00beedcc)
  - `FALL_THROUGH` [`00beed9c`](#insn-00beed9c) → [`00beeda0`](#insn-00beeda0)
- ブロック [`00beeda0`](#insn-00beeda0) 範囲 `[['00beeda0', '00beedbb']]`
  - `CONDITIONAL_JUMP` [`00beedb8`](#insn-00beedb8) → [`00beedd0`](#insn-00beedd0)
  - `FALL_THROUGH` [`00beedb8`](#insn-00beedb8) → [`00beedbc`](#insn-00beedbc)
- ブロック [`00beedbc`](#insn-00beedbc) 範囲 `[['00beedbc', '00beedcb']]`
  - `UNCONDITIONAL_JUMP` [`00beedc8`](#insn-00beedc8) → [`00beedd0`](#insn-00beedd0)
- ブロック [`00beedcc`](#insn-00beedcc) 範囲 `[['00beedcc', '00beedcf']]`
  - `FALL_THROUGH` [`00beedcc`](#insn-00beedcc) → [`00beedd0`](#insn-00beedd0)
- ブロック [`00beedd0`](#insn-00beedd0) 範囲 `[['00beedd0', '00beedd3']]`
  - `FALL_THROUGH` [`00beedd0`](#insn-00beedd0) → [`00beedd4`](#insn-00beedd4)
- ブロック [`00beedd4`](#insn-00beedd4) 範囲 `[['00beedd4', '00beeddb']]`
  - `CONDITIONAL_JUMP` [`00beedd8`](#insn-00beedd8) → [`00beee2c`](#insn-00beee2c)
  - `FALL_THROUGH` [`00beedd8`](#insn-00beedd8) → [`00beeddc`](#insn-00beeddc)
- ブロック [`00beeddc`](#insn-00beeddc) 範囲 `[['00beeddc', '00beedf3']]`
  - `CONDITIONAL_JUMP` [`00beedf0`](#insn-00beedf0) → [`00beee2c`](#insn-00beee2c)
  - `FALL_THROUGH` [`00beedf0`](#insn-00beedf0) → [`00beedf4`](#insn-00beedf4)
- ブロック [`00beedf4`](#insn-00beedf4) 範囲 `[['00beedf4', '00beee03']]`
  - `CONDITIONAL_JUMP` [`00beee00`](#insn-00beee00) → [`00beee2c`](#insn-00beee2c)
  - `FALL_THROUGH` [`00beee00`](#insn-00beee00) → [`00beee04`](#insn-00beee04)
- ブロック [`00beee04`](#insn-00beee04) 範囲 `[['00beee04', '00beee0b']]`
  - `UNCONDITIONAL_JUMP` [`00beee08`](#insn-00beee08) → [`00beee2c`](#insn-00beee2c)
- ブロック [`00beee0c`](#insn-00beee0c) 範囲 `[['00beee0c', '00beee1b']]`
  - `CONDITIONAL_JUMP` [`00beee18`](#insn-00beee18) → [`00beee2c`](#insn-00beee2c)
  - `FALL_THROUGH` [`00beee18`](#insn-00beee18) → [`00beee1c`](#insn-00beee1c)
- ブロック [`00beee1c`](#insn-00beee1c) 範囲 `[['00beee1c', '00beee1f']]`
  - `FALL_THROUGH` [`00beee1c`](#insn-00beee1c) → [`00beee20`](#insn-00beee20)
- ブロック [`00beee20`](#insn-00beee20) 範囲 `[['00beee20', '00beee2b']]`
  - `UNCONDITIONAL_JUMP` [`00beee28`](#insn-00beee28) → [`00beee30`](#insn-00beee30)
- ブロック [`00beee2c`](#insn-00beee2c) 範囲 `[['00beee2c', '00beee2f']]`
  - `FALL_THROUGH` [`00beee2c`](#insn-00beee2c) → [`00beee30`](#insn-00beee30)
- ブロック [`00beee30`](#insn-00beee30) 範囲 `[['00beee30', '00beee3b']]`
- ブロック [`00beee3c`](#insn-00beee3c) 範囲 `[['00beee3c', '00beee4b']]`
  - `UNCONDITIONAL_JUMP` [`00beee48`](#insn-00beee48) → [`00beee30`](#insn-00beee30)

## 命令位置別の参照

- [`00beebb0`](#insn-00beebb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beebc4`](#insn-00beebc4) → [`00beebec`](#insn-00beebec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beebc8`](#insn-00beebc8) → [`00beee2c`](#insn-00beee2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beebd0`](#insn-00beebd0) → [`00beec3c`](#insn-00beec3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beebe0`](#insn-00beebe0) → [`00beee2c`](#insn-00beee2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beebe8`](#insn-00beebe8) → [`00beee20`](#insn-00beee20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beebf0`](#insn-00beebf0) → [`00beec1c`](#insn-00beec1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beebf8`](#insn-00beebf8) → [`00beec80`](#insn-00beec80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec00`](#insn-00beec00) → [`00beec3c`](#insn-00beec3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec14`](#insn-00beec14) → [`00beee4c`](00beee4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00beee4c` · 推定シンボル `None` · 推定型 `None`
- [`00beec18`](#insn-00beec18) → [`00beee2c`](#insn-00beee2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec28`](#insn-00beec28) → [`00beeccc`](#insn-00beeccc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec30`](#insn-00beec30) → [`00beee0c`](#insn-00beee0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec38`](#insn-00beec38) → [`00beee20`](#insn-00beee20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec54`](#insn-00beec54) → [`00beecf0`](#insn-00beecf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec64`](#insn-00beec64) → [`00beed10`](#insn-00beed10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec78`](#insn-00beec78) → [`00beed10`](#insn-00beed10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec7c`](#insn-00beec7c) → [`00beed18`](#insn-00beed18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec98`](#insn-00beec98) → [`00beed98`](#insn-00beed98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beecac`](#insn-00beecac) → [`00beedbc`](#insn-00beedbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beecc4`](#insn-00beecc4) → [`00beedbc`](#insn-00beedbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beecc8`](#insn-00beecc8) → [`00beedcc`](#insn-00beedcc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beecd0`](#insn-00beecd0) → [`00beee2c`](#insn-00beee2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beece4`](#insn-00beece4) → [`00beee2c`](#insn-00beee2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beecec`](#insn-00beecec) → [`00beee2c`](#insn-00beee2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beecf4`](#insn-00beecf4) → [`00beed18`](#insn-00beed18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed0c`](#insn-00beed0c) → [`00beed18`](#insn-00beed18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed20`](#insn-00beed20) → [`00beee2c`](#insn-00beee2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed2c`](#insn-00beed2c) → [`00beed5c`](#insn-00beed5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed40`](#insn-00beed40) → [`00beee3c`](#insn-00beee3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed58`](#insn-00beed58) → [`00beee2c`](#insn-00beee2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed68`](#insn-00beed68) → [`00beed44`](#insn-00beed44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed78`](#insn-00beed78) → [`00beed30`](#insn-00beed30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed8c`](#insn-00beed8c) → [`00beed70`](#insn-00beed70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed94`](#insn-00beed94) → [`00beed34`](#insn-00beed34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed9c`](#insn-00beed9c) → [`00beedcc`](#insn-00beedcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beedb8`](#insn-00beedb8) → [`00beedd0`](#insn-00beedd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beedc8`](#insn-00beedc8) → [`00beedd0`](#insn-00beedd0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beedd8`](#insn-00beedd8) → [`00beee2c`](#insn-00beee2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beedf0`](#insn-00beedf0) → [`00beee2c`](#insn-00beee2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee00`](#insn-00beee00) → [`00beee2c`](#insn-00beee2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee08`](#insn-00beee08) → [`00beee2c`](#insn-00beee2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee18`](#insn-00beee18) → [`00beee2c`](#insn-00beee2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee28`](#insn-00beee28) → [`00beee30`](#insn-00beee30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee30`](#insn-00beee30) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee48`](#insn-00beee48) → [`00beee30`](#insn-00beee30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00beebb0`](#insn-00beebb0)

~~~json
{
  "source": "00beebb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beebc4`](#insn-00beebc4)

~~~json
{
  "source": "00beebc4",
  "target": "00beebec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beebc8`](#insn-00beebc8)

~~~json
{
  "source": "00beebc8",
  "target": "00beee2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beebd0`](#insn-00beebd0)

~~~json
{
  "source": "00beebd0",
  "target": "00beec3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beebe0`](#insn-00beebe0)

~~~json
{
  "source": "00beebe0",
  "target": "00beee2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beebe8`](#insn-00beebe8)

~~~json
{
  "source": "00beebe8",
  "target": "00beee20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beebf0`](#insn-00beebf0)

~~~json
{
  "source": "00beebf0",
  "target": "00beec1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beebf8`](#insn-00beebf8)

~~~json
{
  "source": "00beebf8",
  "target": "00beec80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec00`](#insn-00beec00)

~~~json
{
  "source": "00beec00",
  "target": "00beec3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec14`](#insn-00beec14)

~~~json
{
  "source": "00beec14",
  "target": "00beee4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beec18`](#insn-00beec18)

~~~json
{
  "source": "00beec18",
  "target": "00beee2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec28`](#insn-00beec28)

~~~json
{
  "source": "00beec28",
  "target": "00beeccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec30`](#insn-00beec30)

~~~json
{
  "source": "00beec30",
  "target": "00beee0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec38`](#insn-00beec38)

~~~json
{
  "source": "00beec38",
  "target": "00beee20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec54`](#insn-00beec54)

~~~json
{
  "source": "00beec54",
  "target": "00beecf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec64`](#insn-00beec64)

~~~json
{
  "source": "00beec64",
  "target": "00beed10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec78`](#insn-00beec78)

~~~json
{
  "source": "00beec78",
  "target": "00beed10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec7c`](#insn-00beec7c)

~~~json
{
  "source": "00beec7c",
  "target": "00beed18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec98`](#insn-00beec98)

~~~json
{
  "source": "00beec98",
  "target": "00beed98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beecac`](#insn-00beecac)

~~~json
{
  "source": "00beecac",
  "target": "00beedbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beecc4`](#insn-00beecc4)

~~~json
{
  "source": "00beecc4",
  "target": "00beedbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beecc8`](#insn-00beecc8)

~~~json
{
  "source": "00beecc8",
  "target": "00beedcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beecd0`](#insn-00beecd0)

~~~json
{
  "source": "00beecd0",
  "target": "00beee2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beece4`](#insn-00beece4)

~~~json
{
  "source": "00beece4",
  "target": "00beee2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beecec`](#insn-00beecec)

~~~json
{
  "source": "00beecec",
  "target": "00beee2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beecf4`](#insn-00beecf4)

~~~json
{
  "source": "00beecf4",
  "target": "00beed18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed0c`](#insn-00beed0c)

~~~json
{
  "source": "00beed0c",
  "target": "00beed18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed20`](#insn-00beed20)

~~~json
{
  "source": "00beed20",
  "target": "00beee2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed2c`](#insn-00beed2c)

~~~json
{
  "source": "00beed2c",
  "target": "00beed5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed40`](#insn-00beed40)

~~~json
{
  "source": "00beed40",
  "target": "00beee3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed58`](#insn-00beed58)

~~~json
{
  "source": "00beed58",
  "target": "00beee2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed68`](#insn-00beed68)

~~~json
{
  "source": "00beed68",
  "target": "00beed44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed78`](#insn-00beed78)

~~~json
{
  "source": "00beed78",
  "target": "00beed30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed8c`](#insn-00beed8c)

~~~json
{
  "source": "00beed8c",
  "target": "00beed70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed94`](#insn-00beed94)

~~~json
{
  "source": "00beed94",
  "target": "00beed34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed9c`](#insn-00beed9c)

~~~json
{
  "source": "00beed9c",
  "target": "00beedcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beedb8`](#insn-00beedb8)

~~~json
{
  "source": "00beedb8",
  "target": "00beedd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beedc8`](#insn-00beedc8)

~~~json
{
  "source": "00beedc8",
  "target": "00beedd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beedd8`](#insn-00beedd8)

~~~json
{
  "source": "00beedd8",
  "target": "00beee2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beedf0`](#insn-00beedf0)

~~~json
{
  "source": "00beedf0",
  "target": "00beee2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee00`](#insn-00beee00)

~~~json
{
  "source": "00beee00",
  "target": "00beee2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee08`](#insn-00beee08)

~~~json
{
  "source": "00beee08",
  "target": "00beee2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee18`](#insn-00beee18)

~~~json
{
  "source": "00beee18",
  "target": "00beee2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee28`](#insn-00beee28)

~~~json
{
  "source": "00beee28",
  "target": "00beee30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee30`](#insn-00beee30)

~~~json
{
  "source": "00beee30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee48`](#insn-00beee48)

~~~json
{
  "source": "00beee48",
  "target": "00beee30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
