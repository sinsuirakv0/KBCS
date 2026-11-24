# 00bac9ec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0082.md#review-96c7d150df8b164d84cd9641b3c150c9)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bad9e0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bad/00bad9e0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-328362bc79c95113131986635d41c836)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bac9ec",
  "name": "FUN_00bac9ec",
  "size": 684,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "05748742102e8d1ef861a58f532fcbaef1d359518cf53c5b981a0dc6ee1b8d78",
  "source_text_sha256": "05748742102e8d1ef861a58f532fcbaef1d359518cf53c5b981a0dc6ee1b8d78",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bac9ec",
        "00bacc97"
      ]
    ],
    "bytes_sha256": "a331fb5dcfe35e9b19b354b0b90996755eb168ab3871f7837d0ba6db04ad8ae5",
    "instruction_count": 171,
    "instruction_bytes": 684,
    "body_bytes": 684,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bac038](../00bac/00bac038.md)
- [00bacc98](../00bac/00bacc98.md)
- [00bad180](../00bad/00bad180.md)

## 呼び出し先

- [00c58120](../00c58/00c58120.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6813 bytes

~~~c

undefined8 FUN_00bac9ec(undefined8 *param_1,undefined8 *param_2,undefined8 *param_3)

{
  ulong uVar1;
  ulong uVar2;
  size_t sVar3;
  byte bVar4;
  byte bVar5;
  uint uVar6;
  uint uVar7;
  int iVar8;
  byte *pbVar9;
  byte *pbVar10;
  byte *__s2;
  byte *pbVar11;
  byte *pbVar12;
  ulong uVar13;
  ulong uVar14;
  
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac84c with catch @ 00baca08
                        */
  pbVar12 = (byte *)*param_2;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac828 with catch @ 00baca0c
                        */
  pbVar11 = (byte *)*param_1;
  uVar14 = *(ulong *)(pbVar12 + 0x80);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac94c with catch @ 00baca1c
                        */
  uVar13 = *(ulong *)(pbVar11 + 0x80);
  if (uVar14 == uVar13) {
    bVar4 = *pbVar11;
    bVar5 = *pbVar12;
    uVar2 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar11 + 8);
    }
    uVar1 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar12 + 8);
    }
    sVar3 = uVar2;
    if (uVar1 <= uVar2) {
      sVar3 = uVar1;
    }
    if (sVar3 == 0) {
LAB_00baca80:
      uVar6 = 0;
      if (uVar1 < uVar2) {
        uVar6 = 0xffffffff;
      }
    }
    else {
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac96c with catch @ 00baca60
                        */
      pbVar9 = *(byte **)(pbVar12 + 0x10);
                    /* catch() { ... } // from try @ 00bacdc4 with catch @ 00baca64 */
      pbVar10 = *(byte **)(pbVar11 + 0x10);
      if ((bVar5 & 1) == 0) {
        pbVar9 = pbVar12 + 1;
      }
      if ((bVar4 & 1) == 0) {
        pbVar10 = pbVar11 + 1;
      }
      uVar6 = memcmp(pbVar9,pbVar10,sVar3);
      if (uVar6 == 0) goto LAB_00baca80;
    }
    uVar6 = uVar6 >> 0x1f;
  }
  else {
    uVar6 = (uint)(uVar14 < uVar13);
  }
  pbVar9 = (byte *)*param_3;
                    /* try { // try from 00bacaa8 to 00cacab3 has its CatchHandler @ 00bace7c */
  if (*(ulong *)(pbVar9 + 0x80) == uVar14) {
    bVar4 = *pbVar12;
    bVar5 = *pbVar9;
    uVar14 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar14 = *(ulong *)(pbVar12 + 8);
    }
                    /* try { // try from 00bacacc to 00cacad7 has its CatchHandler @ 00bace78 */
    uVar2 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar9 + 8);
    }
    sVar3 = uVar14;
    if (uVar2 <= uVar14) {
      sVar3 = uVar2;
    }
    if (sVar3 != 0) {
                    /* try { // try from 00bacae0 to 00cacae7 has its CatchHandler @ 00baced8 */
      pbVar10 = *(byte **)(pbVar9 + 0x10);
      __s2 = *(byte **)(pbVar12 + 0x10);
      if ((bVar5 & 1) == 0) {
        pbVar10 = pbVar9 + 1;
      }
      if ((bVar4 & 1) == 0) {
        __s2 = pbVar12 + 1;
      }
      uVar7 = memcmp(pbVar10,__s2,sVar3);
      if (uVar7 != 0) {
        uVar7 = uVar7 >> 0x1f;
                    /* try { // try from 00bacb04 to 00cacb0f has its CatchHandler @ 00bace68 */
        goto joined_r0x00bacb8c;
      }
    }
                    /* try { // try from 00bacba8 to 00cacbb3 has its CatchHandler @ 00bace40 */
    uVar7 = 0;
    if (uVar2 < uVar14) {
      uVar7 = 0xffffffff;
    }
    uVar7 = uVar7 >> 0x1f;
  }
  else {
                    /* try { // try from 00bacb88 to 00cacb8b has its CatchHandler @ 00baced8 */
    uVar7 = (uint)(*(ulong *)(pbVar9 + 0x80) < uVar14);
  }
joined_r0x00bacb8c:
  if (uVar6 == 0) {
    if (uVar7 == 0) {
      return 0;
    }
    *param_2 = pbVar9;
    *param_3 = pbVar12;
    pbVar11 = (byte *)*param_2;
    pbVar12 = (byte *)*param_1;
                    /* try { // try from 00bacb24 to 00cacb2f has its CatchHandler @ 00bace64 */
    if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
      bVar4 = *pbVar12;
      bVar5 = *pbVar11;
      uVar13 = (ulong)(bVar4 >> 1);
      if ((bVar4 & 1) != 0) {
        uVar13 = *(ulong *)(pbVar12 + 8);
      }
      uVar14 = (ulong)(bVar5 >> 1);
                    /* try { // try from 00bacb50 to 00cacb5b has its CatchHandler @ 00bace54 */
      if ((bVar5 & 1) != 0) {
        uVar14 = *(ulong *)(pbVar11 + 8);
      }
      sVar3 = uVar13;
      if (uVar14 <= uVar13) {
        sVar3 = uVar14;
      }
      if (sVar3 != 0) {
        pbVar9 = *(byte **)(pbVar11 + 0x10);
        pbVar10 = *(byte **)(pbVar12 + 0x10);
        if ((bVar5 & 1) == 0) {
          pbVar9 = pbVar11 + 1;
        }
                    /* try { // try from 00bacb74 to 00cacb7f has its CatchHandler @ 00bace50 */
        if ((bVar4 & 1) == 0) {
          pbVar10 = pbVar12 + 1;
        }
        iVar8 = memcmp(pbVar9,pbVar10,sVar3);
        if (iVar8 != 0) {
          if (-1 < iVar8) {
            return 1;
          }
          goto LAB_00bacc54;
        }
      }
      if (uVar13 <= uVar14) {
        return 1;
      }
    }
    else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
      return 1;
    }
LAB_00bacc54:
    *param_1 = pbVar11;
    *param_2 = pbVar12;
    return 2;
  }
  if (uVar7 != 0) {
    *param_1 = pbVar9;
    *param_3 = pbVar11;
    return 1;
  }
                    /* try { // try from 00bacbc8 to 00cacbd3 has its CatchHandler @ 00bace3c */
  *param_1 = pbVar12;
  *param_2 = pbVar11;
  pbVar12 = (byte *)*param_3;
  if (*(ulong *)(pbVar12 + 0x80) == uVar13) {
    bVar4 = *pbVar11;
    bVar5 = *pbVar12;
                    /* try { // try from 00bacbf4 to 00cacbff has its CatchHandler @ 00bace2c */
    uVar13 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar13 = *(ulong *)(pbVar11 + 8);
    }
    uVar14 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar14 = *(ulong *)(pbVar12 + 8);
    }
    sVar3 = uVar13;
    if (uVar14 <= uVar13) {
      sVar3 = uVar14;
    }
    if (sVar3 != 0) {
      pbVar9 = *(byte **)(pbVar12 + 0x10);
                    /* try { // try from 00bacc18 to 00cacc23 has its CatchHandler @ 00bace28 */
      pbVar10 = *(byte **)(pbVar11 + 0x10);
      if ((bVar5 & 1) == 0) {
        pbVar9 = pbVar12 + 1;
      }
      if ((bVar4 & 1) == 0) {
        pbVar10 = pbVar11 + 1;
      }
                    /* try { // try from 00bacc2c to 00cacc43 has its CatchHandler @ 00baced8 */
      iVar8 = memcmp(pbVar9,pbVar10,sVar3);
      if (iVar8 != 0) {
        if (-1 < iVar8) {
          return 1;
        }
        goto LAB_00bacc68;
      }
    }
                    /* try { // try from 00bacc64 to 00cacc6f has its CatchHandler @ 00bace18 */
    if (uVar13 <= uVar14) {
      return 1;
    }
  }
  else if (uVar13 <= *(ulong *)(pbVar12 + 0x80)) {
    return 1;
  }
LAB_00bacc68:
  *param_2 = pbVar12;
  *param_3 = pbVar11;
                    /* try { // try from 00bacc84 to 00cacc8f has its CatchHandler @ 00bace14 */
  return 2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bac9ec"></a> `00bac9ec` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00bac9f0"></a> `00bac9f0` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bac9f4"></a> `00bac9f4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bac9f8"></a> `00bac9f8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bac9fc"></a> `00bac9fc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00baca00"></a> `00baca00` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00baca04"></a> `00baca04` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00baca08"></a> `00baca08` | `37 00 40 f9` | ldr x23,[x1] | `FALL_THROUGH`
<a id="insn-00baca0c"></a> `00baca0c` | `16 00 40 f9` | ldr x22,[x0] | `FALL_THROUGH`
<a id="insn-00baca10"></a> `00baca10` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00baca14"></a> `00baca14` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00baca18"></a> `00baca18` | `fb 42 40 f9` | ldr x27,[x23, #0x80] | `FALL_THROUGH`
<a id="insn-00baca1c"></a> `00baca1c` | `d8 42 40 f9` | ldr x24,[x22, #0x80] | `FALL_THROUGH`
<a id="insn-00baca20"></a> `00baca20` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-00baca24"></a> `00baca24` | `7f 03 18 eb` | cmp x27,x24 | `FALL_THROUGH`
<a id="insn-00baca28"></a> `00baca28` | `81 03 00 54` | b.ne 0x00baca98 | `CONDITIONAL_JUMP`
<a id="insn-00baca2c"></a> `00baca2c` | `c8 02 40 39` | ldrb w8,[x22] | `FALL_THROUGH`
<a id="insn-00baca30"></a> `00baca30` | `ca 06 40 f9` | ldr x10,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00baca34"></a> `00baca34` | `e9 02 40 39` | ldrb w9,[x23] | `FALL_THROUGH`
<a id="insn-00baca38"></a> `00baca38` | `eb 06 40 f9` | ldr x11,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00baca3c"></a> `00baca3c` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00baca40"></a> `00baca40` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baca44"></a> `00baca44` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00baca48"></a> `00baca48` | `99 01 8a 9a` | csel x25,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00baca4c"></a> `00baca4c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baca50"></a> `00baca50` | `ba 01 8b 9a` | csel x26,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00baca54"></a> `00baca54` | `3f 03 1a eb` | cmp x25,x26 | `FALL_THROUGH`
<a id="insn-00baca58"></a> `00baca58` | `22 33 9a 9a` | csel x2,x25,x26,cc | `FALL_THROUGH`
<a id="insn-00baca5c"></a> `00baca5c` | `22 01 00 b4` | cbz x2,0x00baca80 | `CONDITIONAL_JUMP`
<a id="insn-00baca60"></a> `00baca60` | `ea 0a 40 f9` | ldr x10,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00baca64"></a> `00baca64` | `cb 0a 40 f9` | ldr x11,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baca68"></a> `00baca68` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baca6c"></a> `00baca6c` | `40 15 97 9a` | csinc x0,x10,x23,ne | `FALL_THROUGH`
<a id="insn-00baca70"></a> `00baca70` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baca74"></a> `00baca74` | `61 15 96 9a` | csinc x1,x11,x22,ne | `FALL_THROUGH`
<a id="insn-00baca78"></a> `00baca78` | `aa ad 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00baca7c"></a> `00baca7c` | `a0 00 00 35` | cbnz w0,0x00baca90 | `CONDITIONAL_JUMP`
<a id="insn-00baca80"></a> `00baca80` | `3f 03 1a eb` | cmp x25,x26 | `FALL_THROUGH`
<a id="insn-00baca84"></a> `00baca84` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00baca88"></a> `00baca88` | `5f 03 19 eb` | cmp x26,x25 | `FALL_THROUGH`
<a id="insn-00baca8c"></a> `00baca8c` | `00 21 9f 5a` | csinv w0,w8,wzr,cs | `FALL_THROUGH`
<a id="insn-00baca90"></a> `00baca90` | `1a 7c 1f 53` | lsr w26,w0,#0x1f | `FALL_THROUGH`
<a id="insn-00baca94"></a> `00baca94` | `02 00 00 14` | b 0x00baca9c | `UNCONDITIONAL_JUMP`
<a id="insn-00baca98"></a> `00baca98` | `fa 27 9f 1a` | cset w26,cc | `FALL_THROUGH`
<a id="insn-00baca9c"></a> `00baca9c` | `b9 02 40 f9` | ldr x25,[x21] | `FALL_THROUGH`
<a id="insn-00bacaa0"></a> `00bacaa0` | `28 43 40 f9` | ldr x8,[x25, #0x80] | `FALL_THROUGH`
<a id="insn-00bacaa4"></a> `00bacaa4` | `1f 01 1b eb` | cmp x8,x27 | `FALL_THROUGH`
<a id="insn-00bacaa8"></a> `00bacaa8` | `01 07 00 54` | b.ne 0x00bacb88 | `CONDITIONAL_JUMP`
<a id="insn-00bacaac"></a> `00bacaac` | `e8 02 40 39` | ldrb w8,[x23] | `FALL_THROUGH`
<a id="insn-00bacab0"></a> `00bacab0` | `ea 06 40 f9` | ldr x10,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bacab4"></a> `00bacab4` | `29 03 40 39` | ldrb w9,[x25] | `FALL_THROUGH`
<a id="insn-00bacab8"></a> `00bacab8` | `2b 07 40 f9` | ldr x11,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00bacabc"></a> `00bacabc` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacac0"></a> `00bacac0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacac4"></a> `00bacac4` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacac8"></a> `00bacac8` | `9b 01 8a 9a` | csel x27,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bacacc"></a> `00bacacc` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacad0"></a> `00bacad0` | `bc 01 8b 9a` | csel x28,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bacad4"></a> `00bacad4` | `7f 03 1c eb` | cmp x27,x28 | `FALL_THROUGH`
<a id="insn-00bacad8"></a> `00bacad8` | `62 33 9c 9a` | csel x2,x27,x28,cc | `FALL_THROUGH`
<a id="insn-00bacadc"></a> `00bacadc` | `42 06 00 b4` | cbz x2,0x00bacba4 | `CONDITIONAL_JUMP`
<a id="insn-00bacae0"></a> `00bacae0` | `2a 0b 40 f9` | ldr x10,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00bacae4"></a> `00bacae4` | `eb 0a 40 f9` | ldr x11,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00bacae8"></a> `00bacae8` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacaec"></a> `00bacaec` | `40 15 99 9a` | csinc x0,x10,x25,ne | `FALL_THROUGH`
<a id="insn-00bacaf0"></a> `00bacaf0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacaf4"></a> `00bacaf4` | `61 15 97 9a` | csinc x1,x11,x23,ne | `FALL_THROUGH`
<a id="insn-00bacaf8"></a> `00bacaf8` | `8a ad 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00bacafc"></a> `00bacafc` | `40 05 00 34` | cbz w0,0x00bacba4 | `CONDITIONAL_JUMP`
<a id="insn-00bacb00"></a> `00bacb00` | `08 7c 1f 53` | lsr w8,w0,#0x1f | `FALL_THROUGH`
<a id="insn-00bacb04"></a> `00bacb04` | `7a 04 00 37` | tbnz w26,#0x0,0x00bacb90 | `CONDITIONAL_JUMP`
<a id="insn-00bacb08"></a> `00bacb08` | `c8 05 00 34` | cbz w8,0x00bacbc0 | `CONDITIONAL_JUMP`
<a id="insn-00bacb0c"></a> `00bacb0c` | `79 02 00 f9` | str x25,[x19] | `FALL_THROUGH`
<a id="insn-00bacb10"></a> `00bacb10` | `b7 02 00 f9` | str x23,[x21] | `FALL_THROUGH`
<a id="insn-00bacb14"></a> `00bacb14` | `75 02 40 f9` | ldr x21,[x19] | `FALL_THROUGH`
<a id="insn-00bacb18"></a> `00bacb18` | `96 02 40 f9` | ldr x22,[x20] | `FALL_THROUGH`
<a id="insn-00bacb1c"></a> `00bacb1c` | `a8 42 40 f9` | ldr x8,[x21, #0x80] | `FALL_THROUGH`
<a id="insn-00bacb20"></a> `00bacb20` | `c9 42 40 f9` | ldr x9,[x22, #0x80] | `FALL_THROUGH`
<a id="insn-00bacb24"></a> `00bacb24` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bacb28"></a> `00bacb28` | `a1 08 00 54` | b.ne 0x00bacc3c | `CONDITIONAL_JUMP`
<a id="insn-00bacb2c"></a> `00bacb2c` | `c8 02 40 39` | ldrb w8,[x22] | `FALL_THROUGH`
<a id="insn-00bacb30"></a> `00bacb30` | `ca 06 40 f9` | ldr x10,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bacb34"></a> `00bacb34` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bacb38"></a> `00bacb38` | `ab 06 40 f9` | ldr x11,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bacb3c"></a> `00bacb3c` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacb40"></a> `00bacb40` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacb44"></a> `00bacb44` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacb48"></a> `00bacb48` | `97 01 8a 9a` | csel x23,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bacb4c"></a> `00bacb4c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacb50"></a> `00bacb50` | `b8 01 8b 9a` | csel x24,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bacb54"></a> `00bacb54` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-00bacb58"></a> `00bacb58` | `e2 32 98 9a` | csel x2,x23,x24,cc | `FALL_THROUGH`
<a id="insn-00bacb5c"></a> `00bacb5c` | `82 07 00 b4` | cbz x2,0x00bacc4c | `CONDITIONAL_JUMP`
<a id="insn-00bacb60"></a> `00bacb60` | `aa 0a 40 f9` | ldr x10,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bacb64"></a> `00bacb64` | `cb 0a 40 f9` | ldr x11,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00bacb68"></a> `00bacb68` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacb6c"></a> `00bacb6c` | `40 15 95 9a` | csinc x0,x10,x21,ne | `FALL_THROUGH`
<a id="insn-00bacb70"></a> `00bacb70` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacb74"></a> `00bacb74` | `61 15 96 9a` | csinc x1,x11,x22,ne | `FALL_THROUGH`
<a id="insn-00bacb78"></a> `00bacb78` | `6a ad 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00bacb7c"></a> `00bacb7c` | `80 06 00 34` | cbz w0,0x00bacc4c | `CONDITIONAL_JUMP`
<a id="insn-00bacb80"></a> `00bacb80` | `a0 06 f8 37` | tbnz w0,#0x1f,0x00bacc54 | `CONDITIONAL_JUMP`
<a id="insn-00bacb84"></a> `00bacb84` | `3d 00 00 14` | b 0x00bacc78 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacb88"></a> `00bacb88` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00bacb8c"></a> `00bacb8c` | `fa fb 07 36` | tbz w26,#0x0,0x00bacb08 | `CONDITIONAL_JUMP`
<a id="insn-00bacb90"></a> `00bacb90` | `c8 01 00 34` | cbz w8,0x00bacbc8 | `CONDITIONAL_JUMP`
<a id="insn-00bacb94"></a> `00bacb94` | `99 02 00 f9` | str x25,[x20] | `FALL_THROUGH`
<a id="insn-00bacb98"></a> `00bacb98` | `b6 02 00 f9` | str x22,[x21] | `FALL_THROUGH`
<a id="insn-00bacb9c"></a> `00bacb9c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bacba0"></a> `00bacba0` | `37 00 00 14` | b 0x00bacc7c | `UNCONDITIONAL_JUMP`
<a id="insn-00bacba4"></a> `00bacba4` | `7f 03 1c eb` | cmp x27,x28 | `FALL_THROUGH`
<a id="insn-00bacba8"></a> `00bacba8` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00bacbac"></a> `00bacbac` | `9f 03 1b eb` | cmp x28,x27 | `FALL_THROUGH`
<a id="insn-00bacbb0"></a> `00bacbb0` | `00 21 9f 5a` | csinv w0,w8,wzr,cs | `FALL_THROUGH`
<a id="insn-00bacbb4"></a> `00bacbb4` | `08 7c 1f 53` | lsr w8,w0,#0x1f | `FALL_THROUGH`
<a id="insn-00bacbb8"></a> `00bacbb8` | `da fe 07 37` | tbnz w26,#0x0,0x00bacb90 | `CONDITIONAL_JUMP`
<a id="insn-00bacbbc"></a> `00bacbbc` | `d3 ff ff 17` | b 0x00bacb08 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacbc0"></a> `00bacbc0` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bacbc4"></a> `00bacbc4` | `2e 00 00 14` | b 0x00bacc7c | `UNCONDITIONAL_JUMP`
<a id="insn-00bacbc8"></a> `00bacbc8` | `97 02 00 f9` | str x23,[x20] | `FALL_THROUGH`
<a id="insn-00bacbcc"></a> `00bacbcc` | `76 02 00 f9` | str x22,[x19] | `FALL_THROUGH`
<a id="insn-00bacbd0"></a> `00bacbd0` | `b4 02 40 f9` | ldr x20,[x21] | `FALL_THROUGH`
<a id="insn-00bacbd4"></a> `00bacbd4` | `88 42 40 f9` | ldr x8,[x20, #0x80] | `FALL_THROUGH`
<a id="insn-00bacbd8"></a> `00bacbd8` | `1f 01 18 eb` | cmp x8,x24 | `FALL_THROUGH`
<a id="insn-00bacbdc"></a> `00bacbdc` | `41 03 00 54` | b.ne 0x00bacc44 | `CONDITIONAL_JUMP`
<a id="insn-00bacbe0"></a> `00bacbe0` | `c8 02 40 39` | ldrb w8,[x22] | `FALL_THROUGH`
<a id="insn-00bacbe4"></a> `00bacbe4` | `ca 06 40 f9` | ldr x10,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bacbe8"></a> `00bacbe8` | `89 02 40 39` | ldrb w9,[x20] | `FALL_THROUGH`
<a id="insn-00bacbec"></a> `00bacbec` | `8b 06 40 f9` | ldr x11,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bacbf0"></a> `00bacbf0` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacbf4"></a> `00bacbf4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacbf8"></a> `00bacbf8` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacbfc"></a> `00bacbfc` | `97 01 8a 9a` | csel x23,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bacc00"></a> `00bacc00` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacc04"></a> `00bacc04` | `b8 01 8b 9a` | csel x24,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bacc08"></a> `00bacc08` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-00bacc0c"></a> `00bacc0c` | `e2 32 98 9a` | csel x2,x23,x24,cc | `FALL_THROUGH`
<a id="insn-00bacc10"></a> `00bacc10` | `82 02 00 b4` | cbz x2,0x00bacc60 | `CONDITIONAL_JUMP`
<a id="insn-00bacc14"></a> `00bacc14` | `8a 0a 40 f9` | ldr x10,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bacc18"></a> `00bacc18` | `cb 0a 40 f9` | ldr x11,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00bacc1c"></a> `00bacc1c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacc20"></a> `00bacc20` | `40 15 94 9a` | csinc x0,x10,x20,ne | `FALL_THROUGH`
<a id="insn-00bacc24"></a> `00bacc24` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacc28"></a> `00bacc28` | `61 15 96 9a` | csinc x1,x11,x22,ne | `FALL_THROUGH`
<a id="insn-00bacc2c"></a> `00bacc2c` | `3d ad 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00bacc30"></a> `00bacc30` | `80 01 00 34` | cbz w0,0x00bacc60 | `CONDITIONAL_JUMP`
<a id="insn-00bacc34"></a> `00bacc34` | `20 02 f8 36` | tbz w0,#0x1f,0x00bacc78 | `CONDITIONAL_JUMP`
<a id="insn-00bacc38"></a> `00bacc38` | `0c 00 00 14` | b 0x00bacc68 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacc3c"></a> `00bacc3c` | `e2 01 00 54` | b.cs 0x00bacc78 | `CONDITIONAL_JUMP`
<a id="insn-00bacc40"></a> `00bacc40` | `05 00 00 14` | b 0x00bacc54 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacc44"></a> `00bacc44` | `a2 01 00 54` | b.cs 0x00bacc78 | `CONDITIONAL_JUMP`
<a id="insn-00bacc48"></a> `00bacc48` | `08 00 00 14` | b 0x00bacc68 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacc4c"></a> `00bacc4c` | `1f 03 17 eb` | cmp x24,x23 | `FALL_THROUGH`
<a id="insn-00bacc50"></a> `00bacc50` | `42 01 00 54` | b.cs 0x00bacc78 | `CONDITIONAL_JUMP`
<a id="insn-00bacc54"></a> `00bacc54` | `95 02 00 f9` | str x21,[x20] | `FALL_THROUGH`
<a id="insn-00bacc58"></a> `00bacc58` | `76 02 00 f9` | str x22,[x19] | `FALL_THROUGH`
<a id="insn-00bacc5c"></a> `00bacc5c` | `05 00 00 14` | b 0x00bacc70 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacc60"></a> `00bacc60` | `1f 03 17 eb` | cmp x24,x23 | `FALL_THROUGH`
<a id="insn-00bacc64"></a> `00bacc64` | `a2 00 00 54` | b.cs 0x00bacc78 | `CONDITIONAL_JUMP`
<a id="insn-00bacc68"></a> `00bacc68` | `74 02 00 f9` | str x20,[x19] | `FALL_THROUGH`
<a id="insn-00bacc6c"></a> `00bacc6c` | `b6 02 00 f9` | str x22,[x21] | `FALL_THROUGH`
<a id="insn-00bacc70"></a> `00bacc70` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00bacc74"></a> `00bacc74` | `02 00 00 14` | b 0x00bacc7c | `UNCONDITIONAL_JUMP`
<a id="insn-00bacc78"></a> `00bacc78` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bacc7c"></a> `00bacc7c` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bacc80"></a> `00bacc80` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bacc84"></a> `00bacc84` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bacc88"></a> `00bacc88` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bacc8c"></a> `00bacc8c` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bacc90"></a> `00bacc90` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00bacc94"></a> `00bacc94` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bac9ec`](#insn-00bac9ec) 範囲 `[['00bac9ec', '00baca07']]`
  - `FALL_THROUGH` [`00baca04`](#insn-00baca04) → [`00baca08`](#insn-00baca08)
- ブロック [`00baca08`](#insn-00baca08) 範囲 `[['00baca08', '00baca0b']]`
  - `FALL_THROUGH` [`00baca08`](#insn-00baca08) → [`00baca0c`](#insn-00baca0c)
- ブロック [`00baca0c`](#insn-00baca0c) 範囲 `[['00baca0c', '00baca1b']]`
  - `FALL_THROUGH` [`00baca18`](#insn-00baca18) → [`00baca1c`](#insn-00baca1c)
- ブロック [`00baca1c`](#insn-00baca1c) 範囲 `[['00baca1c', '00baca2b']]`
  - `CONDITIONAL_JUMP` [`00baca28`](#insn-00baca28) → [`00baca98`](#insn-00baca98)
  - `FALL_THROUGH` [`00baca28`](#insn-00baca28) → [`00baca2c`](#insn-00baca2c)
- ブロック [`00baca2c`](#insn-00baca2c) 範囲 `[['00baca2c', '00baca5f']]`
  - `CONDITIONAL_JUMP` [`00baca5c`](#insn-00baca5c) → [`00baca80`](#insn-00baca80)
  - `FALL_THROUGH` [`00baca5c`](#insn-00baca5c) → [`00baca60`](#insn-00baca60)
- ブロック [`00baca60`](#insn-00baca60) 範囲 `[['00baca60', '00baca63']]`
  - `FALL_THROUGH` [`00baca60`](#insn-00baca60) → [`00baca64`](#insn-00baca64)
- ブロック [`00baca64`](#insn-00baca64) 範囲 `[['00baca64', '00baca7f']]`
  - `CONDITIONAL_JUMP` [`00baca7c`](#insn-00baca7c) → [`00baca90`](#insn-00baca90)
  - `FALL_THROUGH` [`00baca7c`](#insn-00baca7c) → [`00baca80`](#insn-00baca80)
- ブロック [`00baca80`](#insn-00baca80) 範囲 `[['00baca80', '00baca8f']]`
  - `FALL_THROUGH` [`00baca8c`](#insn-00baca8c) → [`00baca90`](#insn-00baca90)
- ブロック [`00baca90`](#insn-00baca90) 範囲 `[['00baca90', '00baca97']]`
  - `UNCONDITIONAL_JUMP` [`00baca94`](#insn-00baca94) → [`00baca9c`](#insn-00baca9c)
- ブロック [`00baca98`](#insn-00baca98) 範囲 `[['00baca98', '00baca9b']]`
  - `FALL_THROUGH` [`00baca98`](#insn-00baca98) → [`00baca9c`](#insn-00baca9c)
- ブロック [`00baca9c`](#insn-00baca9c) 範囲 `[['00baca9c', '00bacaa7']]`
  - `FALL_THROUGH` [`00bacaa4`](#insn-00bacaa4) → [`00bacaa8`](#insn-00bacaa8)
- ブロック [`00bacaa8`](#insn-00bacaa8) 範囲 `[['00bacaa8', '00bacaab']]`
  - `CONDITIONAL_JUMP` [`00bacaa8`](#insn-00bacaa8) → [`00bacb88`](#insn-00bacb88)
  - `FALL_THROUGH` [`00bacaa8`](#insn-00bacaa8) → [`00bacaac`](#insn-00bacaac)
- ブロック [`00bacaac`](#insn-00bacaac) 範囲 `[['00bacaac', '00bacacb']]`
  - `FALL_THROUGH` [`00bacac8`](#insn-00bacac8) → [`00bacacc`](#insn-00bacacc)
- ブロック [`00bacacc`](#insn-00bacacc) 範囲 `[['00bacacc', '00bacadf']]`
  - `CONDITIONAL_JUMP` [`00bacadc`](#insn-00bacadc) → [`00bacba4`](#insn-00bacba4)
  - `FALL_THROUGH` [`00bacadc`](#insn-00bacadc) → [`00bacae0`](#insn-00bacae0)
- ブロック [`00bacae0`](#insn-00bacae0) 範囲 `[['00bacae0', '00bacaff']]`
  - `CONDITIONAL_JUMP` [`00bacafc`](#insn-00bacafc) → [`00bacba4`](#insn-00bacba4)
  - `FALL_THROUGH` [`00bacafc`](#insn-00bacafc) → [`00bacb00`](#insn-00bacb00)
- ブロック [`00bacb00`](#insn-00bacb00) 範囲 `[['00bacb00', '00bacb03']]`
  - `FALL_THROUGH` [`00bacb00`](#insn-00bacb00) → [`00bacb04`](#insn-00bacb04)
- ブロック [`00bacb04`](#insn-00bacb04) 範囲 `[['00bacb04', '00bacb07']]`
  - `CONDITIONAL_JUMP` [`00bacb04`](#insn-00bacb04) → [`00bacb90`](#insn-00bacb90)
  - `FALL_THROUGH` [`00bacb04`](#insn-00bacb04) → [`00bacb08`](#insn-00bacb08)
- ブロック [`00bacb08`](#insn-00bacb08) 範囲 `[['00bacb08', '00bacb0b']]`
  - `CONDITIONAL_JUMP` [`00bacb08`](#insn-00bacb08) → [`00bacbc0`](#insn-00bacbc0)
  - `FALL_THROUGH` [`00bacb08`](#insn-00bacb08) → [`00bacb0c`](#insn-00bacb0c)
- ブロック [`00bacb0c`](#insn-00bacb0c) 範囲 `[['00bacb0c', '00bacb23']]`
  - `FALL_THROUGH` [`00bacb20`](#insn-00bacb20) → [`00bacb24`](#insn-00bacb24)
- ブロック [`00bacb24`](#insn-00bacb24) 範囲 `[['00bacb24', '00bacb2b']]`
  - `CONDITIONAL_JUMP` [`00bacb28`](#insn-00bacb28) → [`00bacc3c`](#insn-00bacc3c)
  - `FALL_THROUGH` [`00bacb28`](#insn-00bacb28) → [`00bacb2c`](#insn-00bacb2c)
- ブロック [`00bacb2c`](#insn-00bacb2c) 範囲 `[['00bacb2c', '00bacb4f']]`
  - `FALL_THROUGH` [`00bacb4c`](#insn-00bacb4c) → [`00bacb50`](#insn-00bacb50)
- ブロック [`00bacb50`](#insn-00bacb50) 範囲 `[['00bacb50', '00bacb5f']]`
  - `CONDITIONAL_JUMP` [`00bacb5c`](#insn-00bacb5c) → [`00bacc4c`](#insn-00bacc4c)
  - `FALL_THROUGH` [`00bacb5c`](#insn-00bacb5c) → [`00bacb60`](#insn-00bacb60)
- ブロック [`00bacb60`](#insn-00bacb60) 範囲 `[['00bacb60', '00bacb73']]`
  - `FALL_THROUGH` [`00bacb70`](#insn-00bacb70) → [`00bacb74`](#insn-00bacb74)
- ブロック [`00bacb74`](#insn-00bacb74) 範囲 `[['00bacb74', '00bacb7f']]`
  - `CONDITIONAL_JUMP` [`00bacb7c`](#insn-00bacb7c) → [`00bacc4c`](#insn-00bacc4c)
  - `FALL_THROUGH` [`00bacb7c`](#insn-00bacb7c) → [`00bacb80`](#insn-00bacb80)
- ブロック [`00bacb80`](#insn-00bacb80) 範囲 `[['00bacb80', '00bacb83']]`
  - `CONDITIONAL_JUMP` [`00bacb80`](#insn-00bacb80) → [`00bacc54`](#insn-00bacc54)
  - `FALL_THROUGH` [`00bacb80`](#insn-00bacb80) → [`00bacb84`](#insn-00bacb84)
- ブロック [`00bacb84`](#insn-00bacb84) 範囲 `[['00bacb84', '00bacb87']]`
  - `UNCONDITIONAL_JUMP` [`00bacb84`](#insn-00bacb84) → [`00bacc78`](#insn-00bacc78)
- ブロック [`00bacb88`](#insn-00bacb88) 範囲 `[['00bacb88', '00bacb8f']]`
  - `CONDITIONAL_JUMP` [`00bacb8c`](#insn-00bacb8c) → [`00bacb08`](#insn-00bacb08)
  - `FALL_THROUGH` [`00bacb8c`](#insn-00bacb8c) → [`00bacb90`](#insn-00bacb90)
- ブロック [`00bacb90`](#insn-00bacb90) 範囲 `[['00bacb90', '00bacb93']]`
  - `CONDITIONAL_JUMP` [`00bacb90`](#insn-00bacb90) → [`00bacbc8`](#insn-00bacbc8)
  - `FALL_THROUGH` [`00bacb90`](#insn-00bacb90) → [`00bacb94`](#insn-00bacb94)
- ブロック [`00bacb94`](#insn-00bacb94) 範囲 `[['00bacb94', '00bacba3']]`
  - `UNCONDITIONAL_JUMP` [`00bacba0`](#insn-00bacba0) → [`00bacc7c`](#insn-00bacc7c)
- ブロック [`00bacba4`](#insn-00bacba4) 範囲 `[['00bacba4', '00bacba7']]`
  - `FALL_THROUGH` [`00bacba4`](#insn-00bacba4) → [`00bacba8`](#insn-00bacba8)
- ブロック [`00bacba8`](#insn-00bacba8) 範囲 `[['00bacba8', '00bacbbb']]`
  - `CONDITIONAL_JUMP` [`00bacbb8`](#insn-00bacbb8) → [`00bacb90`](#insn-00bacb90)
  - `FALL_THROUGH` [`00bacbb8`](#insn-00bacbb8) → [`00bacbbc`](#insn-00bacbbc)
- ブロック [`00bacbbc`](#insn-00bacbbc) 範囲 `[['00bacbbc', '00bacbbf']]`
  - `UNCONDITIONAL_JUMP` [`00bacbbc`](#insn-00bacbbc) → [`00bacb08`](#insn-00bacb08)
- ブロック [`00bacbc0`](#insn-00bacbc0) 範囲 `[['00bacbc0', '00bacbc7']]`
  - `UNCONDITIONAL_JUMP` [`00bacbc4`](#insn-00bacbc4) → [`00bacc7c`](#insn-00bacc7c)
- ブロック [`00bacbc8`](#insn-00bacbc8) 範囲 `[['00bacbc8', '00bacbdf']]`
  - `CONDITIONAL_JUMP` [`00bacbdc`](#insn-00bacbdc) → [`00bacc44`](#insn-00bacc44)
  - `FALL_THROUGH` [`00bacbdc`](#insn-00bacbdc) → [`00bacbe0`](#insn-00bacbe0)
- ブロック [`00bacbe0`](#insn-00bacbe0) 範囲 `[['00bacbe0', '00bacbf3']]`
  - `FALL_THROUGH` [`00bacbf0`](#insn-00bacbf0) → [`00bacbf4`](#insn-00bacbf4)
- ブロック [`00bacbf4`](#insn-00bacbf4) 範囲 `[['00bacbf4', '00bacc13']]`
  - `CONDITIONAL_JUMP` [`00bacc10`](#insn-00bacc10) → [`00bacc60`](#insn-00bacc60)
  - `FALL_THROUGH` [`00bacc10`](#insn-00bacc10) → [`00bacc14`](#insn-00bacc14)
- ブロック [`00bacc14`](#insn-00bacc14) 範囲 `[['00bacc14', '00bacc17']]`
  - `FALL_THROUGH` [`00bacc14`](#insn-00bacc14) → [`00bacc18`](#insn-00bacc18)
- ブロック [`00bacc18`](#insn-00bacc18) 範囲 `[['00bacc18', '00bacc2b']]`
  - `FALL_THROUGH` [`00bacc28`](#insn-00bacc28) → [`00bacc2c`](#insn-00bacc2c)
- ブロック [`00bacc2c`](#insn-00bacc2c) 範囲 `[['00bacc2c', '00bacc33']]`
  - `CONDITIONAL_JUMP` [`00bacc30`](#insn-00bacc30) → [`00bacc60`](#insn-00bacc60)
  - `FALL_THROUGH` [`00bacc30`](#insn-00bacc30) → [`00bacc34`](#insn-00bacc34)
- ブロック [`00bacc34`](#insn-00bacc34) 範囲 `[['00bacc34', '00bacc37']]`
  - `CONDITIONAL_JUMP` [`00bacc34`](#insn-00bacc34) → [`00bacc78`](#insn-00bacc78)
  - `FALL_THROUGH` [`00bacc34`](#insn-00bacc34) → [`00bacc38`](#insn-00bacc38)
- ブロック [`00bacc38`](#insn-00bacc38) 範囲 `[['00bacc38', '00bacc3b']]`
  - `UNCONDITIONAL_JUMP` [`00bacc38`](#insn-00bacc38) → [`00bacc68`](#insn-00bacc68)
- ブロック [`00bacc3c`](#insn-00bacc3c) 範囲 `[['00bacc3c', '00bacc3f']]`
  - `CONDITIONAL_JUMP` [`00bacc3c`](#insn-00bacc3c) → [`00bacc78`](#insn-00bacc78)
  - `FALL_THROUGH` [`00bacc3c`](#insn-00bacc3c) → [`00bacc40`](#insn-00bacc40)
- ブロック [`00bacc40`](#insn-00bacc40) 範囲 `[['00bacc40', '00bacc43']]`
  - `UNCONDITIONAL_JUMP` [`00bacc40`](#insn-00bacc40) → [`00bacc54`](#insn-00bacc54)
- ブロック [`00bacc44`](#insn-00bacc44) 範囲 `[['00bacc44', '00bacc47']]`
  - `CONDITIONAL_JUMP` [`00bacc44`](#insn-00bacc44) → [`00bacc78`](#insn-00bacc78)
  - `FALL_THROUGH` [`00bacc44`](#insn-00bacc44) → [`00bacc48`](#insn-00bacc48)
- ブロック [`00bacc48`](#insn-00bacc48) 範囲 `[['00bacc48', '00bacc4b']]`
  - `UNCONDITIONAL_JUMP` [`00bacc48`](#insn-00bacc48) → [`00bacc68`](#insn-00bacc68)
- ブロック [`00bacc4c`](#insn-00bacc4c) 範囲 `[['00bacc4c', '00bacc53']]`
  - `CONDITIONAL_JUMP` [`00bacc50`](#insn-00bacc50) → [`00bacc78`](#insn-00bacc78)
  - `FALL_THROUGH` [`00bacc50`](#insn-00bacc50) → [`00bacc54`](#insn-00bacc54)
- ブロック [`00bacc54`](#insn-00bacc54) 範囲 `[['00bacc54', '00bacc5f']]`
  - `UNCONDITIONAL_JUMP` [`00bacc5c`](#insn-00bacc5c) → [`00bacc70`](#insn-00bacc70)
- ブロック [`00bacc60`](#insn-00bacc60) 範囲 `[['00bacc60', '00bacc63']]`
  - `FALL_THROUGH` [`00bacc60`](#insn-00bacc60) → [`00bacc64`](#insn-00bacc64)
- ブロック [`00bacc64`](#insn-00bacc64) 範囲 `[['00bacc64', '00bacc67']]`
  - `CONDITIONAL_JUMP` [`00bacc64`](#insn-00bacc64) → [`00bacc78`](#insn-00bacc78)
  - `FALL_THROUGH` [`00bacc64`](#insn-00bacc64) → [`00bacc68`](#insn-00bacc68)
- ブロック [`00bacc68`](#insn-00bacc68) 範囲 `[['00bacc68', '00bacc6f']]`
  - `FALL_THROUGH` [`00bacc6c`](#insn-00bacc6c) → [`00bacc70`](#insn-00bacc70)
- ブロック [`00bacc70`](#insn-00bacc70) 範囲 `[['00bacc70', '00bacc77']]`
  - `UNCONDITIONAL_JUMP` [`00bacc74`](#insn-00bacc74) → [`00bacc7c`](#insn-00bacc7c)
- ブロック [`00bacc78`](#insn-00bacc78) 範囲 `[['00bacc78', '00bacc7b']]`
  - `FALL_THROUGH` [`00bacc78`](#insn-00bacc78) → [`00bacc7c`](#insn-00bacc7c)
- ブロック [`00bacc7c`](#insn-00bacc7c) 範囲 `[['00bacc7c', '00bacc83']]`
  - `FALL_THROUGH` [`00bacc80`](#insn-00bacc80) → [`00bacc84`](#insn-00bacc84)
- ブロック [`00bacc84`](#insn-00bacc84) 範囲 `[['00bacc84', '00bacc97']]`

## 命令位置別の参照

- [`00bac9ec`](#insn-00bac9ec) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac9f0`](#insn-00bac9f0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac9f4`](#insn-00bac9f4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac9f8`](#insn-00bac9f8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac9fc`](#insn-00bac9fc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baca00`](#insn-00baca00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baca28`](#insn-00baca28) → [`00baca98`](#insn-00baca98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baca5c`](#insn-00baca5c) → [`00baca80`](#insn-00baca80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baca78`](#insn-00baca78) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00baca7c`](#insn-00baca7c) → [`00baca90`](#insn-00baca90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baca94`](#insn-00baca94) → [`00baca9c`](#insn-00baca9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacaa8`](#insn-00bacaa8) → [`00bacb88`](#insn-00bacb88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacadc`](#insn-00bacadc) → [`00bacba4`](#insn-00bacba4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacaf8`](#insn-00bacaf8) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00bacafc`](#insn-00bacafc) → [`00bacba4`](#insn-00bacba4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb04`](#insn-00bacb04) → [`00bacb90`](#insn-00bacb90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb08`](#insn-00bacb08) → [`00bacbc0`](#insn-00bacbc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb28`](#insn-00bacb28) → [`00bacc3c`](#insn-00bacc3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb5c`](#insn-00bacb5c) → [`00bacc4c`](#insn-00bacc4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb78`](#insn-00bacb78) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00bacb7c`](#insn-00bacb7c) → [`00bacc4c`](#insn-00bacc4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb80`](#insn-00bacb80) → [`00bacc54`](#insn-00bacc54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb84`](#insn-00bacb84) → [`00bacc78`](#insn-00bacc78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb8c`](#insn-00bacb8c) → [`00bacb08`](#insn-00bacb08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb90`](#insn-00bacb90) → [`00bacbc8`](#insn-00bacbc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacba0`](#insn-00bacba0) → [`00bacc7c`](#insn-00bacc7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacbb8`](#insn-00bacbb8) → [`00bacb90`](#insn-00bacb90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacbbc`](#insn-00bacbbc) → [`00bacb08`](#insn-00bacb08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacbc4`](#insn-00bacbc4) → [`00bacc7c`](#insn-00bacc7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacbdc`](#insn-00bacbdc) → [`00bacc44`](#insn-00bacc44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc10`](#insn-00bacc10) → [`00bacc60`](#insn-00bacc60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc2c`](#insn-00bacc2c) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00bacc30`](#insn-00bacc30) → [`00bacc60`](#insn-00bacc60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc34`](#insn-00bacc34) → [`00bacc78`](#insn-00bacc78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc38`](#insn-00bacc38) → [`00bacc68`](#insn-00bacc68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc3c`](#insn-00bacc3c) → [`00bacc78`](#insn-00bacc78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc40`](#insn-00bacc40) → [`00bacc54`](#insn-00bacc54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc44`](#insn-00bacc44) → [`00bacc78`](#insn-00bacc78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc48`](#insn-00bacc48) → [`00bacc68`](#insn-00bacc68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc50`](#insn-00bacc50) → [`00bacc78`](#insn-00bacc78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc5c`](#insn-00bacc5c) → [`00bacc70`](#insn-00bacc70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc64`](#insn-00bacc64) → [`00bacc78`](#insn-00bacc78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc74`](#insn-00bacc74) → [`00bacc7c`](#insn-00bacc7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc7c`](#insn-00bacc7c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc80`](#insn-00bacc80) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc84`](#insn-00bacc84) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc88`](#insn-00bacc88) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc8c`](#insn-00bacc8c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bac9ec`](#insn-00bac9ec)

~~~json
{
  "source": "00bac9ec",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac9f0`](#insn-00bac9f0)

~~~json
{
  "source": "00bac9f0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac9f4`](#insn-00bac9f4)

~~~json
{
  "source": "00bac9f4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac9f8`](#insn-00bac9f8)

~~~json
{
  "source": "00bac9f8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac9fc`](#insn-00bac9fc)

~~~json
{
  "source": "00bac9fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baca00`](#insn-00baca00)

~~~json
{
  "source": "00baca00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baca28`](#insn-00baca28)

~~~json
{
  "source": "00baca28",
  "target": "00baca98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baca5c`](#insn-00baca5c)

~~~json
{
  "source": "00baca5c",
  "target": "00baca80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baca78`](#insn-00baca78)

~~~json
{
  "source": "00baca78",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baca7c`](#insn-00baca7c)

~~~json
{
  "source": "00baca7c",
  "target": "00baca90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baca94`](#insn-00baca94)

~~~json
{
  "source": "00baca94",
  "target": "00baca9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacaa8`](#insn-00bacaa8)

~~~json
{
  "source": "00bacaa8",
  "target": "00bacb88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacadc`](#insn-00bacadc)

~~~json
{
  "source": "00bacadc",
  "target": "00bacba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacaf8`](#insn-00bacaf8)

~~~json
{
  "source": "00bacaf8",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bacafc`](#insn-00bacafc)

~~~json
{
  "source": "00bacafc",
  "target": "00bacba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb04`](#insn-00bacb04)

~~~json
{
  "source": "00bacb04",
  "target": "00bacb90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb08`](#insn-00bacb08)

~~~json
{
  "source": "00bacb08",
  "target": "00bacbc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb28`](#insn-00bacb28)

~~~json
{
  "source": "00bacb28",
  "target": "00bacc3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb5c`](#insn-00bacb5c)

~~~json
{
  "source": "00bacb5c",
  "target": "00bacc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb78`](#insn-00bacb78)

~~~json
{
  "source": "00bacb78",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bacb7c`](#insn-00bacb7c)

~~~json
{
  "source": "00bacb7c",
  "target": "00bacc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb80`](#insn-00bacb80)

~~~json
{
  "source": "00bacb80",
  "target": "00bacc54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb84`](#insn-00bacb84)

~~~json
{
  "source": "00bacb84",
  "target": "00bacc78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb8c`](#insn-00bacb8c)

~~~json
{
  "source": "00bacb8c",
  "target": "00bacb08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb90`](#insn-00bacb90)

~~~json
{
  "source": "00bacb90",
  "target": "00bacbc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacba0`](#insn-00bacba0)

~~~json
{
  "source": "00bacba0",
  "target": "00bacc7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacbb8`](#insn-00bacbb8)

~~~json
{
  "source": "00bacbb8",
  "target": "00bacb90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacbbc`](#insn-00bacbbc)

~~~json
{
  "source": "00bacbbc",
  "target": "00bacb08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacbc4`](#insn-00bacbc4)

~~~json
{
  "source": "00bacbc4",
  "target": "00bacc7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacbdc`](#insn-00bacbdc)

~~~json
{
  "source": "00bacbdc",
  "target": "00bacc44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc10`](#insn-00bacc10)

~~~json
{
  "source": "00bacc10",
  "target": "00bacc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc2c`](#insn-00bacc2c)

~~~json
{
  "source": "00bacc2c",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bacc30`](#insn-00bacc30)

~~~json
{
  "source": "00bacc30",
  "target": "00bacc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc34`](#insn-00bacc34)

~~~json
{
  "source": "00bacc34",
  "target": "00bacc78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc38`](#insn-00bacc38)

~~~json
{
  "source": "00bacc38",
  "target": "00bacc68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc3c`](#insn-00bacc3c)

~~~json
{
  "source": "00bacc3c",
  "target": "00bacc78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc40`](#insn-00bacc40)

~~~json
{
  "source": "00bacc40",
  "target": "00bacc54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc44`](#insn-00bacc44)

~~~json
{
  "source": "00bacc44",
  "target": "00bacc78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc48`](#insn-00bacc48)

~~~json
{
  "source": "00bacc48",
  "target": "00bacc68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc50`](#insn-00bacc50)

~~~json
{
  "source": "00bacc50",
  "target": "00bacc78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc5c`](#insn-00bacc5c)

~~~json
{
  "source": "00bacc5c",
  "target": "00bacc70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc64`](#insn-00bacc64)

~~~json
{
  "source": "00bacc64",
  "target": "00bacc78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc74`](#insn-00bacc74)

~~~json
{
  "source": "00bacc74",
  "target": "00bacc7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc7c`](#insn-00bacc7c)

~~~json
{
  "source": "00bacc7c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc80`](#insn-00bacc80)

~~~json
{
  "source": "00bacc80",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc84`](#insn-00bacc84)

~~~json
{
  "source": "00bacc84",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc88`](#insn-00bacc88)

~~~json
{
  "source": "00bacc88",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc8c`](#insn-00bacc8c)

~~~json
{
  "source": "00bacc8c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
