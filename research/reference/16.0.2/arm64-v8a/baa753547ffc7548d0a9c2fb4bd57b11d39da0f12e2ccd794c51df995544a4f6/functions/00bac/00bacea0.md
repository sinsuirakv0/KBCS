# 00bacea0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0082.md#review-8745ec2e022dd5ed3697d564df1357df)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bade94`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bad/00bade94.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-9641250429acf2914f9ba8d1339a2f96)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bacea0",
  "name": "FUN_00bacea0",
  "size": 736,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ea8198534676c489d46334c57d0c277138d7d48d046fbb5180bad38674f9e82f",
  "source_text_sha256": "ea8198534676c489d46334c57d0c277138d7d48d046fbb5180bad38674f9e82f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bacea0",
        "00bad17f"
      ]
    ],
    "bytes_sha256": "1472ca332d8eae5c3149ac223effdd57d5a2e5b36169eaacd914a011768b6f77",
    "instruction_count": 184,
    "instruction_bytes": 736,
    "body_bytes": 736,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bac038](../00bac/00bac038.md)
- [00bad180](../00bad/00bad180.md)

## 呼び出し先

- [00bacc98](../00bac/00bacc98.md)
- [00c58120](../00c58/00c58120.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 7079 bytes

~~~c

int FUN_00bacea0(undefined8 *param_1,undefined8 *param_2,undefined8 *param_3,undefined8 *param_4,
                undefined8 *param_5)

{
  ulong uVar1;
  ulong uVar2;
  size_t sVar3;
  byte bVar4;
  byte bVar5;
  int iVar6;
  int iVar7;
  int iVar8;
  byte *pbVar9;
  byte *pbVar10;
  byte *pbVar11;
  byte *pbVar12;
  
  iVar6 = FUN_00bacc98();
                    /* catch() { ... } // from try @ 00bacae0 with catch @ 00baced8
                       catch() { ... } // from try @ 00bacb88 with catch @ 00baced8
                       catch() { ... } // from try @ 00bacc2c with catch @ 00baced8
                       catch() { ... } // from try @ 00bacce8 with catch @ 00baced8 */
  pbVar11 = (byte *)*param_5;
  pbVar12 = (byte *)*param_4;
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
    bVar4 = *pbVar12;
    bVar5 = *pbVar11;
                    /* catch() { ... } // from try @ 00bacd54 with catch @ 00bacf10 */
                    /* try { // try from 00bacf14 to 00cacfcb has its CatchHandler @ 00bacf14
                       catch() { ... } // from try @ 00bacf14 with catch @ 00bacf14
                       catch() { ... } // from try @ 00bad1d8 with catch @ 00bacf14
                       catch() { ... } // from try @ 00bad494 with catch @ 00bacf14 */
    uVar1 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar12 + 8);
    }
    uVar2 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar11 + 8);
    }
    sVar3 = uVar1;
    if (uVar2 <= uVar1) {
      sVar3 = uVar2;
    }
    if (sVar3 != 0) {
      pbVar9 = *(byte **)(pbVar11 + 0x10);
      pbVar10 = *(byte **)(pbVar12 + 0x10);
      if ((bVar5 & 1) == 0) {
        pbVar9 = pbVar11 + 1;
      }
      if ((bVar4 & 1) == 0) {
        pbVar10 = pbVar12 + 1;
      }
      iVar7 = memcmp(pbVar9,pbVar10,sVar3);
      if (iVar7 != 0) {
        if (-1 < iVar7) {
          return iVar6;
        }
        goto LAB_00bacfa0;
      }
    }
    if (uVar1 <= uVar2) {
      return iVar6;
    }
  }
  else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
    return iVar6;
  }
LAB_00bacfa0:
  *param_4 = pbVar11;
  *param_5 = pbVar12;
  pbVar11 = (byte *)*param_4;
  pbVar12 = (byte *)*param_3;
  iVar7 = iVar6 + 1;
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
    bVar4 = *pbVar12;
                    /* try { // try from 00bacfcc to 00cacfd7 has its CatchHandler @ 00bad690 */
    bVar5 = *pbVar11;
    uVar1 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar12 + 8);
    }
    uVar2 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar11 + 8);
    }
    sVar3 = uVar1;
                    /* try { // try from 00bacff0 to 00cacffb has its CatchHandler @ 00bad68c */
    if (uVar2 <= uVar1) {
      sVar3 = uVar2;
    }
    if (sVar3 != 0) {
      pbVar9 = *(byte **)(pbVar11 + 0x10);
      pbVar10 = *(byte **)(pbVar12 + 0x10);
                    /* try { // try from 00bad004 to 00cad00f has its CatchHandler @ 00bad66c */
      if ((bVar5 & 1) == 0) {
        pbVar9 = pbVar11 + 1;
      }
      if ((bVar4 & 1) == 0) {
        pbVar10 = pbVar12 + 1;
      }
                    /* try { // try from 00bad010 to 00cad01b has its CatchHandler @ 00bad65c */
      iVar8 = memcmp(pbVar9,pbVar10,sVar3);
      if (iVar8 != 0) {
        if (-1 < iVar8) {
          return iVar7;
        }
        goto LAB_00bad030;
      }
    }
    if (uVar1 <= uVar2) {
      return iVar7;
    }
  }
  else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
    return iVar7;
  }
LAB_00bad030:
  *param_3 = pbVar11;
                    /* try { // try from 00bad034 to 00cad03f has its CatchHandler @ 00bad634 */
  *param_4 = pbVar12;
  pbVar11 = (byte *)*param_3;
  pbVar12 = (byte *)*param_2;
  iVar7 = iVar6 + 2;
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
    bVar4 = *pbVar12;
                    /* try { // try from 00bad05c to 00cad067 has its CatchHandler @ 00bad628 */
    bVar5 = *pbVar11;
    uVar1 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar12 + 8);
    }
    uVar2 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar11 + 8);
    }
    sVar3 = uVar1;
                    /* try { // try from 00bad080 to 00cad08b has its CatchHandler @ 00bad624 */
    if (uVar2 <= uVar1) {
      sVar3 = uVar2;
    }
    if (sVar3 != 0) {
      pbVar9 = *(byte **)(pbVar11 + 0x10);
      pbVar10 = *(byte **)(pbVar12 + 0x10);
                    /* try { // try from 00bad090 to 00cad09b has its CatchHandler @ 00bad61c */
      if ((bVar5 & 1) == 0) {
        pbVar9 = pbVar11 + 1;
      }
      if ((bVar4 & 1) == 0) {
        pbVar10 = pbVar12 + 1;
      }
      iVar8 = memcmp(pbVar9,pbVar10,sVar3);
      if (iVar8 != 0) {
        if (-1 < iVar8) {
          return iVar7;
        }
        goto LAB_00bad0c0;
      }
    }
    if (uVar1 <= uVar2) {
      return iVar7;
    }
  }
  else {
                    /* try { // try from 00bad0b0 to 00cad0bb has its CatchHandler @ 00bad608 */
    if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
      return iVar7;
    }
  }
LAB_00bad0c0:
  *param_2 = pbVar11;
  *param_3 = pbVar12;
  pbVar11 = (byte *)*param_2;
  pbVar12 = (byte *)*param_1;
  iVar7 = iVar6 + 3;
                    /* try { // try from 00bad0dc to 00cad0e7 has its CatchHandler @ 00bad5fc */
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
    bVar4 = *pbVar12;
    bVar5 = *pbVar11;
    uVar1 = (ulong)(bVar4 >> 1);
                    /* try { // try from 00bad100 to 00cad10b has its CatchHandler @ 00bad5f8 */
    if ((bVar4 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar12 + 8);
    }
    uVar2 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar11 + 8);
    }
    sVar3 = uVar1;
                    /* try { // try from 00bad110 to 00cad11b has its CatchHandler @ 00bad5f0 */
    if (uVar2 <= uVar1) {
      sVar3 = uVar2;
    }
    if (sVar3 != 0) {
      pbVar9 = *(byte **)(pbVar11 + 0x10);
      pbVar10 = *(byte **)(pbVar12 + 0x10);
      if ((bVar5 & 1) == 0) {
        pbVar9 = pbVar11 + 1;
      }
      if ((bVar4 & 1) == 0) {
        pbVar10 = pbVar12 + 1;
      }
                    /* try { // try from 00bad130 to 00cad13b has its CatchHandler @ 00bad5dc */
      iVar8 = memcmp(pbVar9,pbVar10,sVar3);
      if (iVar8 != 0) {
        if (-1 < iVar8) {
          return iVar7;
        }
        goto LAB_00bad144;
      }
    }
    if (uVar1 <= uVar2) {
      return iVar7;
    }
  }
  else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
    return iVar7;
  }
LAB_00bad144:
                    /* try { // try from 00bad148 to 00cad153 has its CatchHandler @ 00bad5d4 */
  *param_1 = pbVar11;
  *param_2 = pbVar12;
                    /* try { // try from 00bad154 to 00cad15f has its CatchHandler @ 00bad5d0 */
                    /* try { // try from 00bad170 to 00cad18b has its CatchHandler @ 00bad6a0 */
  return iVar6 + 4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bacea0"></a> `00bacea0` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bacea4"></a> `00bacea4` | `fc 6f 01 a9` | stp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bacea8"></a> `00bacea8` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baceac"></a> `00baceac` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baceb0"></a> `00baceb0` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00baceb4"></a> `00baceb4` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00baceb8"></a> `00baceb8` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bacebc"></a> `00bacebc` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bacec0"></a> `00bacec0` | `f9 03 04 aa` | mov x25,x4 | `FALL_THROUGH`
<a id="insn-00bacec4"></a> `00bacec4` | `f8 03 03 aa` | mov x24,x3 | `FALL_THROUGH`
<a id="insn-00bacec8"></a> `00bacec8` | `f7 03 02 aa` | mov x23,x2 | `FALL_THROUGH`
<a id="insn-00bacecc"></a> `00bacecc` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00baced0"></a> `00baced0` | `fc 03 00 aa` | mov x28,x0 | `FALL_THROUGH`
<a id="insn-00baced4"></a> `00baced4` | `71 ff ff 97` | bl 0x00bacc98 | `UNCONDITIONAL_CALL`
<a id="insn-00baced8"></a> `00baced8` | `3a 03 40 f9` | ldr x26,[x25] | `FALL_THROUGH`
<a id="insn-00bacedc"></a> `00bacedc` | `1b 03 40 f9` | ldr x27,[x24] | `FALL_THROUGH`
<a id="insn-00bacee0"></a> `00bacee0` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00bacee4"></a> `00bacee4` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00bacee8"></a> `00bacee8` | `48 43 40 f9` | ldr x8,[x26, #0x80] | `FALL_THROUGH`
<a id="insn-00baceec"></a> `00baceec` | `69 43 40 f9` | ldr x9,[x27, #0x80] | `FALL_THROUGH`
<a id="insn-00bacef0"></a> `00bacef0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bacef4"></a> `00bacef4` | `41 04 00 54` | b.ne 0x00bacf7c | `CONDITIONAL_JUMP`
<a id="insn-00bacef8"></a> `00bacef8` | `68 03 40 39` | ldrb w8,[x27] | `FALL_THROUGH`
<a id="insn-00bacefc"></a> `00bacefc` | `6a 07 40 f9` | ldr x10,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-00bacf00"></a> `00bacf00` | `49 03 40 39` | ldrb w9,[x26] | `FALL_THROUGH`
<a id="insn-00bacf04"></a> `00bacf04` | `4b 07 40 f9` | ldr x11,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00bacf08"></a> `00bacf08` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacf0c"></a> `00bacf0c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacf10"></a> `00bacf10` | `f7 07 00 f9` | str x23,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bacf14"></a> `00bacf14` | `f7 03 16 2a` | mov w23,w22 | `FALL_THROUGH`
<a id="insn-00bacf18"></a> `00bacf18` | `f6 03 15 2a` | mov w22,w21 | `FALL_THROUGH`
<a id="insn-00bacf1c"></a> `00bacf1c` | `f5 03 13 aa` | mov x21,x19 | `FALL_THROUGH`
<a id="insn-00bacf20"></a> `00bacf20` | `f3 03 1c aa` | mov x19,x28 | `FALL_THROUGH`
<a id="insn-00bacf24"></a> `00bacf24` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacf28"></a> `00bacf28` | `9c 01 8a 9a` | csel x28,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bacf2c"></a> `00bacf2c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacf30"></a> `00bacf30` | `b4 01 8b 9a` | csel x20,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bacf34"></a> `00bacf34` | `9f 03 14 eb` | cmp x28,x20 | `FALL_THROUGH`
<a id="insn-00bacf38"></a> `00bacf38` | `82 33 94 9a` | csel x2,x28,x20,cc | `FALL_THROUGH`
<a id="insn-00bacf3c"></a> `00bacf3c` | `42 02 00 b4` | cbz x2,0x00bacf84 | `CONDITIONAL_JUMP`
<a id="insn-00bacf40"></a> `00bacf40` | `4a 0b 40 f9` | ldr x10,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00bacf44"></a> `00bacf44` | `6b 0b 40 f9` | ldr x11,[x27, #0x10] | `FALL_THROUGH`
<a id="insn-00bacf48"></a> `00bacf48` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacf4c"></a> `00bacf4c` | `40 15 9a 9a` | csinc x0,x10,x26,ne | `FALL_THROUGH`
<a id="insn-00bacf50"></a> `00bacf50` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacf54"></a> `00bacf54` | `61 15 9b 9a` | csinc x1,x11,x27,ne | `FALL_THROUGH`
<a id="insn-00bacf58"></a> `00bacf58` | `72 ac 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00bacf5c"></a> `00bacf5c` | `40 01 00 34` | cbz w0,0x00bacf84 | `CONDITIONAL_JUMP`
<a id="insn-00bacf60"></a> `00bacf60` | `fc 03 13 aa` | mov x28,x19 | `FALL_THROUGH`
<a id="insn-00bacf64"></a> `00bacf64` | `f3 03 15 aa` | mov x19,x21 | `FALL_THROUGH`
<a id="insn-00bacf68"></a> `00bacf68` | `f5 03 16 2a` | mov w21,w22 | `FALL_THROUGH`
<a id="insn-00bacf6c"></a> `00bacf6c` | `f6 03 17 2a` | mov w22,w23 | `FALL_THROUGH`
<a id="insn-00bacf70"></a> `00bacf70` | `f7 07 40 f9` | ldr x23,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bacf74"></a> `00bacf74` | `60 01 f8 37` | tbnz w0,#0x1f,0x00bacfa0 | `CONDITIONAL_JUMP`
<a id="insn-00bacf78"></a> `00bacf78` | `76 00 00 14` | b 0x00bad150 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacf7c"></a> `00bacf7c` | `23 01 00 54` | b.cc 0x00bacfa0 | `CONDITIONAL_JUMP`
<a id="insn-00bacf80"></a> `00bacf80` | `74 00 00 14` | b 0x00bad150 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacf84"></a> `00bacf84` | `9f 02 1c eb` | cmp x20,x28 | `FALL_THROUGH`
<a id="insn-00bacf88"></a> `00bacf88` | `fc 03 13 aa` | mov x28,x19 | `FALL_THROUGH`
<a id="insn-00bacf8c"></a> `00bacf8c` | `f3 03 15 aa` | mov x19,x21 | `FALL_THROUGH`
<a id="insn-00bacf90"></a> `00bacf90` | `f5 03 16 2a` | mov w21,w22 | `FALL_THROUGH`
<a id="insn-00bacf94"></a> `00bacf94` | `f6 03 17 2a` | mov w22,w23 | `FALL_THROUGH`
<a id="insn-00bacf98"></a> `00bacf98` | `f7 07 40 f9` | ldr x23,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bacf9c"></a> `00bacf9c` | `a2 0d 00 54` | b.cs 0x00bad150 | `CONDITIONAL_JUMP`
<a id="insn-00bacfa0"></a> `00bacfa0` | `1a 03 00 f9` | str x26,[x24] | `FALL_THROUGH`
<a id="insn-00bacfa4"></a> `00bacfa4` | `3b 03 00 f9` | str x27,[x25] | `FALL_THROUGH`
<a id="insn-00bacfa8"></a> `00bacfa8` | `19 03 40 f9` | ldr x25,[x24] | `FALL_THROUGH`
<a id="insn-00bacfac"></a> `00bacfac` | `fa 02 40 f9` | ldr x26,[x23] | `FALL_THROUGH`
<a id="insn-00bacfb0"></a> `00bacfb0` | `b6 06 00 11` | add w22,w21,#0x1 | `FALL_THROUGH`
<a id="insn-00bacfb4"></a> `00bacfb4` | `28 43 40 f9` | ldr x8,[x25, #0x80] | `FALL_THROUGH`
<a id="insn-00bacfb8"></a> `00bacfb8` | `49 43 40 f9` | ldr x9,[x26, #0x80] | `FALL_THROUGH`
<a id="insn-00bacfbc"></a> `00bacfbc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bacfc0"></a> `00bacfc0` | `01 03 00 54` | b.ne 0x00bad020 | `CONDITIONAL_JUMP`
<a id="insn-00bacfc4"></a> `00bacfc4` | `48 03 40 39` | ldrb w8,[x26] | `FALL_THROUGH`
<a id="insn-00bacfc8"></a> `00bacfc8` | `4a 07 40 f9` | ldr x10,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00bacfcc"></a> `00bacfcc` | `29 03 40 39` | ldrb w9,[x25] | `FALL_THROUGH`
<a id="insn-00bacfd0"></a> `00bacfd0` | `2b 07 40 f9` | ldr x11,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00bacfd4"></a> `00bacfd4` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacfd8"></a> `00bacfd8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacfdc"></a> `00bacfdc` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacfe0"></a> `00bacfe0` | `9b 01 8a 9a` | csel x27,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bacfe4"></a> `00bacfe4` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacfe8"></a> `00bacfe8` | `b4 01 8b 9a` | csel x20,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bacfec"></a> `00bacfec` | `7f 03 14 eb` | cmp x27,x20 | `FALL_THROUGH`
<a id="insn-00bacff0"></a> `00bacff0` | `62 33 94 9a` | csel x2,x27,x20,cc | `FALL_THROUGH`
<a id="insn-00bacff4"></a> `00bacff4` | `a2 01 00 b4` | cbz x2,0x00bad028 | `CONDITIONAL_JUMP`
<a id="insn-00bacff8"></a> `00bacff8` | `2a 0b 40 f9` | ldr x10,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00bacffc"></a> `00bacffc` | `4b 0b 40 f9` | ldr x11,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00bad000"></a> `00bad000` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad004"></a> `00bad004` | `40 15 99 9a` | csinc x0,x10,x25,ne | `FALL_THROUGH`
<a id="insn-00bad008"></a> `00bad008` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad00c"></a> `00bad00c` | `61 15 9a 9a` | csinc x1,x11,x26,ne | `FALL_THROUGH`
<a id="insn-00bad010"></a> `00bad010` | `44 ac 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00bad014"></a> `00bad014` | `a0 00 00 34` | cbz w0,0x00bad028 | `CONDITIONAL_JUMP`
<a id="insn-00bad018"></a> `00bad018` | `c0 00 f8 37` | tbnz w0,#0x1f,0x00bad030 | `CONDITIONAL_JUMP`
<a id="insn-00bad01c"></a> `00bad01c` | `4d 00 00 14` | b 0x00bad150 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad020"></a> `00bad020` | `83 00 00 54` | b.cc 0x00bad030 | `CONDITIONAL_JUMP`
<a id="insn-00bad024"></a> `00bad024` | `4b 00 00 14` | b 0x00bad150 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad028"></a> `00bad028` | `9f 02 1b eb` | cmp x20,x27 | `FALL_THROUGH`
<a id="insn-00bad02c"></a> `00bad02c` | `22 09 00 54` | b.cs 0x00bad150 | `CONDITIONAL_JUMP`
<a id="insn-00bad030"></a> `00bad030` | `f9 02 00 f9` | str x25,[x23] | `FALL_THROUGH`
<a id="insn-00bad034"></a> `00bad034` | `1a 03 00 f9` | str x26,[x24] | `FALL_THROUGH`
<a id="insn-00bad038"></a> `00bad038` | `f8 02 40 f9` | ldr x24,[x23] | `FALL_THROUGH`
<a id="insn-00bad03c"></a> `00bad03c` | `79 02 40 f9` | ldr x25,[x19] | `FALL_THROUGH`
<a id="insn-00bad040"></a> `00bad040` | `b6 0a 00 11` | add w22,w21,#0x2 | `FALL_THROUGH`
<a id="insn-00bad044"></a> `00bad044` | `08 43 40 f9` | ldr x8,[x24, #0x80] | `FALL_THROUGH`
<a id="insn-00bad048"></a> `00bad048` | `29 43 40 f9` | ldr x9,[x25, #0x80] | `FALL_THROUGH`
<a id="insn-00bad04c"></a> `00bad04c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bad050"></a> `00bad050` | `01 03 00 54` | b.ne 0x00bad0b0 | `CONDITIONAL_JUMP`
<a id="insn-00bad054"></a> `00bad054` | `28 03 40 39` | ldrb w8,[x25] | `FALL_THROUGH`
<a id="insn-00bad058"></a> `00bad058` | `2a 07 40 f9` | ldr x10,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00bad05c"></a> `00bad05c` | `09 03 40 39` | ldrb w9,[x24] | `FALL_THROUGH`
<a id="insn-00bad060"></a> `00bad060` | `0b 07 40 f9` | ldr x11,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00bad064"></a> `00bad064` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad068"></a> `00bad068` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad06c"></a> `00bad06c` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad070"></a> `00bad070` | `9a 01 8a 9a` | csel x26,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bad074"></a> `00bad074` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad078"></a> `00bad078` | `b4 01 8b 9a` | csel x20,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bad07c"></a> `00bad07c` | `5f 03 14 eb` | cmp x26,x20 | `FALL_THROUGH`
<a id="insn-00bad080"></a> `00bad080` | `42 33 94 9a` | csel x2,x26,x20,cc | `FALL_THROUGH`
<a id="insn-00bad084"></a> `00bad084` | `a2 01 00 b4` | cbz x2,0x00bad0b8 | `CONDITIONAL_JUMP`
<a id="insn-00bad088"></a> `00bad088` | `0a 0b 40 f9` | ldr x10,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bad08c"></a> `00bad08c` | `2b 0b 40 f9` | ldr x11,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00bad090"></a> `00bad090` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad094"></a> `00bad094` | `40 15 98 9a` | csinc x0,x10,x24,ne | `FALL_THROUGH`
<a id="insn-00bad098"></a> `00bad098` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad09c"></a> `00bad09c` | `61 15 99 9a` | csinc x1,x11,x25,ne | `FALL_THROUGH`
<a id="insn-00bad0a0"></a> `00bad0a0` | `20 ac 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00bad0a4"></a> `00bad0a4` | `a0 00 00 34` | cbz w0,0x00bad0b8 | `CONDITIONAL_JUMP`
<a id="insn-00bad0a8"></a> `00bad0a8` | `c0 00 f8 37` | tbnz w0,#0x1f,0x00bad0c0 | `CONDITIONAL_JUMP`
<a id="insn-00bad0ac"></a> `00bad0ac` | `29 00 00 14` | b 0x00bad150 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad0b0"></a> `00bad0b0` | `83 00 00 54` | b.cc 0x00bad0c0 | `CONDITIONAL_JUMP`
<a id="insn-00bad0b4"></a> `00bad0b4` | `27 00 00 14` | b 0x00bad150 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad0b8"></a> `00bad0b8` | `9f 02 1a eb` | cmp x20,x26 | `FALL_THROUGH`
<a id="insn-00bad0bc"></a> `00bad0bc` | `a2 04 00 54` | b.cs 0x00bad150 | `CONDITIONAL_JUMP`
<a id="insn-00bad0c0"></a> `00bad0c0` | `78 02 00 f9` | str x24,[x19] | `FALL_THROUGH`
<a id="insn-00bad0c4"></a> `00bad0c4` | `f9 02 00 f9` | str x25,[x23] | `FALL_THROUGH`
<a id="insn-00bad0c8"></a> `00bad0c8` | `77 02 40 f9` | ldr x23,[x19] | `FALL_THROUGH`
<a id="insn-00bad0cc"></a> `00bad0cc` | `98 03 40 f9` | ldr x24,[x28] | `FALL_THROUGH`
<a id="insn-00bad0d0"></a> `00bad0d0` | `b6 0e 00 11` | add w22,w21,#0x3 | `FALL_THROUGH`
<a id="insn-00bad0d4"></a> `00bad0d4` | `e8 42 40 f9` | ldr x8,[x23, #0x80] | `FALL_THROUGH`
<a id="insn-00bad0d8"></a> `00bad0d8` | `09 43 40 f9` | ldr x9,[x24, #0x80] | `FALL_THROUGH`
<a id="insn-00bad0dc"></a> `00bad0dc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bad0e0"></a> `00bad0e0` | `01 03 00 54` | b.ne 0x00bad140 | `CONDITIONAL_JUMP`
<a id="insn-00bad0e4"></a> `00bad0e4` | `08 03 40 39` | ldrb w8,[x24] | `FALL_THROUGH`
<a id="insn-00bad0e8"></a> `00bad0e8` | `0a 07 40 f9` | ldr x10,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00bad0ec"></a> `00bad0ec` | `e9 02 40 39` | ldrb w9,[x23] | `FALL_THROUGH`
<a id="insn-00bad0f0"></a> `00bad0f0` | `eb 06 40 f9` | ldr x11,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bad0f4"></a> `00bad0f4` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad0f8"></a> `00bad0f8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad0fc"></a> `00bad0fc` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad100"></a> `00bad100` | `99 01 8a 9a` | csel x25,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bad104"></a> `00bad104` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad108"></a> `00bad108` | `b4 01 8b 9a` | csel x20,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bad10c"></a> `00bad10c` | `3f 03 14 eb` | cmp x25,x20 | `FALL_THROUGH`
<a id="insn-00bad110"></a> `00bad110` | `22 33 94 9a` | csel x2,x25,x20,cc | `FALL_THROUGH`
<a id="insn-00bad114"></a> `00bad114` | `02 03 00 b4` | cbz x2,0x00bad174 | `CONDITIONAL_JUMP`
<a id="insn-00bad118"></a> `00bad118` | `ea 0a 40 f9` | ldr x10,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00bad11c"></a> `00bad11c` | `0b 0b 40 f9` | ldr x11,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bad120"></a> `00bad120` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad124"></a> `00bad124` | `40 15 97 9a` | csinc x0,x10,x23,ne | `FALL_THROUGH`
<a id="insn-00bad128"></a> `00bad128` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad12c"></a> `00bad12c` | `61 15 98 9a` | csinc x1,x11,x24,ne | `FALL_THROUGH`
<a id="insn-00bad130"></a> `00bad130` | `fc ab 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00bad134"></a> `00bad134` | `00 02 00 34` | cbz w0,0x00bad174 | `CONDITIONAL_JUMP`
<a id="insn-00bad138"></a> `00bad138` | `60 00 f8 37` | tbnz w0,#0x1f,0x00bad144 | `CONDITIONAL_JUMP`
<a id="insn-00bad13c"></a> `00bad13c` | `05 00 00 14` | b 0x00bad150 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad140"></a> `00bad140` | `82 00 00 54` | b.cs 0x00bad150 | `CONDITIONAL_JUMP`
<a id="insn-00bad144"></a> `00bad144` | `b6 12 00 11` | add w22,w21,#0x4 | `FALL_THROUGH`
<a id="insn-00bad148"></a> `00bad148` | `97 03 00 f9` | str x23,[x28] | `FALL_THROUGH`
<a id="insn-00bad14c"></a> `00bad14c` | `78 02 00 f9` | str x24,[x19] | `FALL_THROUGH`
<a id="insn-00bad150"></a> `00bad150` | `e0 03 16 2a` | mov w0,w22 | `FALL_THROUGH`
<a id="insn-00bad154"></a> `00bad154` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bad158"></a> `00bad158` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bad15c"></a> `00bad15c` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bad160"></a> `00bad160` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bad164"></a> `00bad164` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bad168"></a> `00bad168` | `fc 6f 41 a9` | ldp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bad16c"></a> `00bad16c` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bad170"></a> `00bad170` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bad174"></a> `00bad174` | `9f 02 19 eb` | cmp x20,x25 | `FALL_THROUGH`
<a id="insn-00bad178"></a> `00bad178` | `63 fe ff 54` | b.cc 0x00bad144 | `CONDITIONAL_JUMP`
<a id="insn-00bad17c"></a> `00bad17c` | `f5 ff ff 17` | b 0x00bad150 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bacea0`](#insn-00bacea0) 範囲 `[['00bacea0', '00baced7']]`
  - `FALL_THROUGH` [`00baced4`](#insn-00baced4) → [`00baced8`](#insn-00baced8)
- ブロック [`00baced8`](#insn-00baced8) 範囲 `[['00baced8', '00bacef7']]`
  - `CONDITIONAL_JUMP` [`00bacef4`](#insn-00bacef4) → [`00bacf7c`](#insn-00bacf7c)
  - `FALL_THROUGH` [`00bacef4`](#insn-00bacef4) → [`00bacef8`](#insn-00bacef8)
- ブロック [`00bacef8`](#insn-00bacef8) 範囲 `[['00bacef8', '00bacf0f']]`
  - `FALL_THROUGH` [`00bacf0c`](#insn-00bacf0c) → [`00bacf10`](#insn-00bacf10)
- ブロック [`00bacf10`](#insn-00bacf10) 範囲 `[['00bacf10', '00bacf13']]`
  - `FALL_THROUGH` [`00bacf10`](#insn-00bacf10) → [`00bacf14`](#insn-00bacf14)
- ブロック [`00bacf14`](#insn-00bacf14) 範囲 `[['00bacf14', '00bacf3f']]`
  - `CONDITIONAL_JUMP` [`00bacf3c`](#insn-00bacf3c) → [`00bacf84`](#insn-00bacf84)
  - `FALL_THROUGH` [`00bacf3c`](#insn-00bacf3c) → [`00bacf40`](#insn-00bacf40)
- ブロック [`00bacf40`](#insn-00bacf40) 範囲 `[['00bacf40', '00bacf5f']]`
  - `CONDITIONAL_JUMP` [`00bacf5c`](#insn-00bacf5c) → [`00bacf84`](#insn-00bacf84)
  - `FALL_THROUGH` [`00bacf5c`](#insn-00bacf5c) → [`00bacf60`](#insn-00bacf60)
- ブロック [`00bacf60`](#insn-00bacf60) 範囲 `[['00bacf60', '00bacf77']]`
  - `CONDITIONAL_JUMP` [`00bacf74`](#insn-00bacf74) → [`00bacfa0`](#insn-00bacfa0)
  - `FALL_THROUGH` [`00bacf74`](#insn-00bacf74) → [`00bacf78`](#insn-00bacf78)
- ブロック [`00bacf78`](#insn-00bacf78) 範囲 `[['00bacf78', '00bacf7b']]`
  - `UNCONDITIONAL_JUMP` [`00bacf78`](#insn-00bacf78) → [`00bad150`](#insn-00bad150)
- ブロック [`00bacf7c`](#insn-00bacf7c) 範囲 `[['00bacf7c', '00bacf7f']]`
  - `CONDITIONAL_JUMP` [`00bacf7c`](#insn-00bacf7c) → [`00bacfa0`](#insn-00bacfa0)
  - `FALL_THROUGH` [`00bacf7c`](#insn-00bacf7c) → [`00bacf80`](#insn-00bacf80)
- ブロック [`00bacf80`](#insn-00bacf80) 範囲 `[['00bacf80', '00bacf83']]`
  - `UNCONDITIONAL_JUMP` [`00bacf80`](#insn-00bacf80) → [`00bad150`](#insn-00bad150)
- ブロック [`00bacf84`](#insn-00bacf84) 範囲 `[['00bacf84', '00bacf9f']]`
  - `CONDITIONAL_JUMP` [`00bacf9c`](#insn-00bacf9c) → [`00bad150`](#insn-00bad150)
  - `FALL_THROUGH` [`00bacf9c`](#insn-00bacf9c) → [`00bacfa0`](#insn-00bacfa0)
- ブロック [`00bacfa0`](#insn-00bacfa0) 範囲 `[['00bacfa0', '00bacfc3']]`
  - `CONDITIONAL_JUMP` [`00bacfc0`](#insn-00bacfc0) → [`00bad020`](#insn-00bad020)
  - `FALL_THROUGH` [`00bacfc0`](#insn-00bacfc0) → [`00bacfc4`](#insn-00bacfc4)
- ブロック [`00bacfc4`](#insn-00bacfc4) 範囲 `[['00bacfc4', '00bacfcb']]`
  - `FALL_THROUGH` [`00bacfc8`](#insn-00bacfc8) → [`00bacfcc`](#insn-00bacfcc)
- ブロック [`00bacfcc`](#insn-00bacfcc) 範囲 `[['00bacfcc', '00bacfef']]`
  - `FALL_THROUGH` [`00bacfec`](#insn-00bacfec) → [`00bacff0`](#insn-00bacff0)
- ブロック [`00bacff0`](#insn-00bacff0) 範囲 `[['00bacff0', '00bacff7']]`
  - `CONDITIONAL_JUMP` [`00bacff4`](#insn-00bacff4) → [`00bad028`](#insn-00bad028)
  - `FALL_THROUGH` [`00bacff4`](#insn-00bacff4) → [`00bacff8`](#insn-00bacff8)
- ブロック [`00bacff8`](#insn-00bacff8) 範囲 `[['00bacff8', '00bad003']]`
  - `FALL_THROUGH` [`00bad000`](#insn-00bad000) → [`00bad004`](#insn-00bad004)
- ブロック [`00bad004`](#insn-00bad004) 範囲 `[['00bad004', '00bad00f']]`
  - `FALL_THROUGH` [`00bad00c`](#insn-00bad00c) → [`00bad010`](#insn-00bad010)
- ブロック [`00bad010`](#insn-00bad010) 範囲 `[['00bad010', '00bad017']]`
  - `CONDITIONAL_JUMP` [`00bad014`](#insn-00bad014) → [`00bad028`](#insn-00bad028)
  - `FALL_THROUGH` [`00bad014`](#insn-00bad014) → [`00bad018`](#insn-00bad018)
- ブロック [`00bad018`](#insn-00bad018) 範囲 `[['00bad018', '00bad01b']]`
  - `CONDITIONAL_JUMP` [`00bad018`](#insn-00bad018) → [`00bad030`](#insn-00bad030)
  - `FALL_THROUGH` [`00bad018`](#insn-00bad018) → [`00bad01c`](#insn-00bad01c)
- ブロック [`00bad01c`](#insn-00bad01c) 範囲 `[['00bad01c', '00bad01f']]`
  - `UNCONDITIONAL_JUMP` [`00bad01c`](#insn-00bad01c) → [`00bad150`](#insn-00bad150)
- ブロック [`00bad020`](#insn-00bad020) 範囲 `[['00bad020', '00bad023']]`
  - `CONDITIONAL_JUMP` [`00bad020`](#insn-00bad020) → [`00bad030`](#insn-00bad030)
  - `FALL_THROUGH` [`00bad020`](#insn-00bad020) → [`00bad024`](#insn-00bad024)
- ブロック [`00bad024`](#insn-00bad024) 範囲 `[['00bad024', '00bad027']]`
  - `UNCONDITIONAL_JUMP` [`00bad024`](#insn-00bad024) → [`00bad150`](#insn-00bad150)
- ブロック [`00bad028`](#insn-00bad028) 範囲 `[['00bad028', '00bad02f']]`
  - `CONDITIONAL_JUMP` [`00bad02c`](#insn-00bad02c) → [`00bad150`](#insn-00bad150)
  - `FALL_THROUGH` [`00bad02c`](#insn-00bad02c) → [`00bad030`](#insn-00bad030)
- ブロック [`00bad030`](#insn-00bad030) 範囲 `[['00bad030', '00bad033']]`
  - `FALL_THROUGH` [`00bad030`](#insn-00bad030) → [`00bad034`](#insn-00bad034)
- ブロック [`00bad034`](#insn-00bad034) 範囲 `[['00bad034', '00bad053']]`
  - `CONDITIONAL_JUMP` [`00bad050`](#insn-00bad050) → [`00bad0b0`](#insn-00bad0b0)
  - `FALL_THROUGH` [`00bad050`](#insn-00bad050) → [`00bad054`](#insn-00bad054)
- ブロック [`00bad054`](#insn-00bad054) 範囲 `[['00bad054', '00bad05b']]`
  - `FALL_THROUGH` [`00bad058`](#insn-00bad058) → [`00bad05c`](#insn-00bad05c)
- ブロック [`00bad05c`](#insn-00bad05c) 範囲 `[['00bad05c', '00bad07f']]`
  - `FALL_THROUGH` [`00bad07c`](#insn-00bad07c) → [`00bad080`](#insn-00bad080)
- ブロック [`00bad080`](#insn-00bad080) 範囲 `[['00bad080', '00bad087']]`
  - `CONDITIONAL_JUMP` [`00bad084`](#insn-00bad084) → [`00bad0b8`](#insn-00bad0b8)
  - `FALL_THROUGH` [`00bad084`](#insn-00bad084) → [`00bad088`](#insn-00bad088)
- ブロック [`00bad088`](#insn-00bad088) 範囲 `[['00bad088', '00bad08f']]`
  - `FALL_THROUGH` [`00bad08c`](#insn-00bad08c) → [`00bad090`](#insn-00bad090)
- ブロック [`00bad090`](#insn-00bad090) 範囲 `[['00bad090', '00bad0a7']]`
  - `CONDITIONAL_JUMP` [`00bad0a4`](#insn-00bad0a4) → [`00bad0b8`](#insn-00bad0b8)
  - `FALL_THROUGH` [`00bad0a4`](#insn-00bad0a4) → [`00bad0a8`](#insn-00bad0a8)
- ブロック [`00bad0a8`](#insn-00bad0a8) 範囲 `[['00bad0a8', '00bad0ab']]`
  - `CONDITIONAL_JUMP` [`00bad0a8`](#insn-00bad0a8) → [`00bad0c0`](#insn-00bad0c0)
  - `FALL_THROUGH` [`00bad0a8`](#insn-00bad0a8) → [`00bad0ac`](#insn-00bad0ac)
- ブロック [`00bad0ac`](#insn-00bad0ac) 範囲 `[['00bad0ac', '00bad0af']]`
  - `UNCONDITIONAL_JUMP` [`00bad0ac`](#insn-00bad0ac) → [`00bad150`](#insn-00bad150)
- ブロック [`00bad0b0`](#insn-00bad0b0) 範囲 `[['00bad0b0', '00bad0b3']]`
  - `CONDITIONAL_JUMP` [`00bad0b0`](#insn-00bad0b0) → [`00bad0c0`](#insn-00bad0c0)
  - `FALL_THROUGH` [`00bad0b0`](#insn-00bad0b0) → [`00bad0b4`](#insn-00bad0b4)
- ブロック [`00bad0b4`](#insn-00bad0b4) 範囲 `[['00bad0b4', '00bad0b7']]`
  - `UNCONDITIONAL_JUMP` [`00bad0b4`](#insn-00bad0b4) → [`00bad150`](#insn-00bad150)
- ブロック [`00bad0b8`](#insn-00bad0b8) 範囲 `[['00bad0b8', '00bad0bf']]`
  - `CONDITIONAL_JUMP` [`00bad0bc`](#insn-00bad0bc) → [`00bad150`](#insn-00bad150)
  - `FALL_THROUGH` [`00bad0bc`](#insn-00bad0bc) → [`00bad0c0`](#insn-00bad0c0)
- ブロック [`00bad0c0`](#insn-00bad0c0) 範囲 `[['00bad0c0', '00bad0db']]`
  - `FALL_THROUGH` [`00bad0d8`](#insn-00bad0d8) → [`00bad0dc`](#insn-00bad0dc)
- ブロック [`00bad0dc`](#insn-00bad0dc) 範囲 `[['00bad0dc', '00bad0e3']]`
  - `CONDITIONAL_JUMP` [`00bad0e0`](#insn-00bad0e0) → [`00bad140`](#insn-00bad140)
  - `FALL_THROUGH` [`00bad0e0`](#insn-00bad0e0) → [`00bad0e4`](#insn-00bad0e4)
- ブロック [`00bad0e4`](#insn-00bad0e4) 範囲 `[['00bad0e4', '00bad0ff']]`
  - `FALL_THROUGH` [`00bad0fc`](#insn-00bad0fc) → [`00bad100`](#insn-00bad100)
- ブロック [`00bad100`](#insn-00bad100) 範囲 `[['00bad100', '00bad10f']]`
  - `FALL_THROUGH` [`00bad10c`](#insn-00bad10c) → [`00bad110`](#insn-00bad110)
- ブロック [`00bad110`](#insn-00bad110) 範囲 `[['00bad110', '00bad117']]`
  - `CONDITIONAL_JUMP` [`00bad114`](#insn-00bad114) → [`00bad174`](#insn-00bad174)
  - `FALL_THROUGH` [`00bad114`](#insn-00bad114) → [`00bad118`](#insn-00bad118)
- ブロック [`00bad118`](#insn-00bad118) 範囲 `[['00bad118', '00bad12f']]`
  - `FALL_THROUGH` [`00bad12c`](#insn-00bad12c) → [`00bad130`](#insn-00bad130)
- ブロック [`00bad130`](#insn-00bad130) 範囲 `[['00bad130', '00bad137']]`
  - `CONDITIONAL_JUMP` [`00bad134`](#insn-00bad134) → [`00bad174`](#insn-00bad174)
  - `FALL_THROUGH` [`00bad134`](#insn-00bad134) → [`00bad138`](#insn-00bad138)
- ブロック [`00bad138`](#insn-00bad138) 範囲 `[['00bad138', '00bad13b']]`
  - `CONDITIONAL_JUMP` [`00bad138`](#insn-00bad138) → [`00bad144`](#insn-00bad144)
  - `FALL_THROUGH` [`00bad138`](#insn-00bad138) → [`00bad13c`](#insn-00bad13c)
- ブロック [`00bad13c`](#insn-00bad13c) 範囲 `[['00bad13c', '00bad13f']]`
  - `UNCONDITIONAL_JUMP` [`00bad13c`](#insn-00bad13c) → [`00bad150`](#insn-00bad150)
- ブロック [`00bad140`](#insn-00bad140) 範囲 `[['00bad140', '00bad143']]`
  - `CONDITIONAL_JUMP` [`00bad140`](#insn-00bad140) → [`00bad150`](#insn-00bad150)
  - `FALL_THROUGH` [`00bad140`](#insn-00bad140) → [`00bad144`](#insn-00bad144)
- ブロック [`00bad144`](#insn-00bad144) 範囲 `[['00bad144', '00bad147']]`
  - `FALL_THROUGH` [`00bad144`](#insn-00bad144) → [`00bad148`](#insn-00bad148)
- ブロック [`00bad148`](#insn-00bad148) 範囲 `[['00bad148', '00bad14f']]`
  - `FALL_THROUGH` [`00bad14c`](#insn-00bad14c) → [`00bad150`](#insn-00bad150)
- ブロック [`00bad150`](#insn-00bad150) 範囲 `[['00bad150', '00bad153']]`
  - `FALL_THROUGH` [`00bad150`](#insn-00bad150) → [`00bad154`](#insn-00bad154)
- ブロック [`00bad154`](#insn-00bad154) 範囲 `[['00bad154', '00bad16f']]`
  - `FALL_THROUGH` [`00bad16c`](#insn-00bad16c) → [`00bad170`](#insn-00bad170)
- ブロック [`00bad170`](#insn-00bad170) 範囲 `[['00bad170', '00bad173']]`
- ブロック [`00bad174`](#insn-00bad174) 範囲 `[['00bad174', '00bad17b']]`
  - `CONDITIONAL_JUMP` [`00bad178`](#insn-00bad178) → [`00bad144`](#insn-00bad144)
  - `FALL_THROUGH` [`00bad178`](#insn-00bad178) → [`00bad17c`](#insn-00bad17c)
- ブロック [`00bad17c`](#insn-00bad17c) 範囲 `[['00bad17c', '00bad17f']]`
  - `UNCONDITIONAL_JUMP` [`00bad17c`](#insn-00bad17c) → [`00bad150`](#insn-00bad150)

## 命令位置別の参照

- [`00bacea4`](#insn-00bacea4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacea8`](#insn-00bacea8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baceac`](#insn-00baceac) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baceb0`](#insn-00baceb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baceb4`](#insn-00baceb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baceb8`](#insn-00baceb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baced4`](#insn-00baced4) → [`00bacc98`](00bacc98.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bacc98` · 推定シンボル `None` · 推定型 `None`
- [`00bacef4`](#insn-00bacef4) → [`00bacf7c`](#insn-00bacf7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf10`](#insn-00bacf10) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf3c`](#insn-00bacf3c) → [`00bacf84`](#insn-00bacf84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf58`](#insn-00bacf58) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00bacf5c`](#insn-00bacf5c) → [`00bacf84`](#insn-00bacf84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf70`](#insn-00bacf70) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf74`](#insn-00bacf74) → [`00bacfa0`](#insn-00bacfa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf78`](#insn-00bacf78) → [`00bad150`](#insn-00bad150) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf7c`](#insn-00bacf7c) → [`00bacfa0`](#insn-00bacfa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf80`](#insn-00bacf80) → [`00bad150`](#insn-00bad150) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf98`](#insn-00bacf98) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf9c`](#insn-00bacf9c) → [`00bad150`](#insn-00bad150) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacfc0`](#insn-00bacfc0) → [`00bad020`](#insn-00bad020) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacff4`](#insn-00bacff4) → [`00bad028`](#insn-00bad028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad010`](#insn-00bad010) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00bad014`](#insn-00bad014) → [`00bad028`](#insn-00bad028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad018`](#insn-00bad018) → [`00bad030`](#insn-00bad030) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad01c`](#insn-00bad01c) → [`00bad150`](#insn-00bad150) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad020`](#insn-00bad020) → [`00bad030`](#insn-00bad030) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad024`](#insn-00bad024) → [`00bad150`](#insn-00bad150) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad02c`](#insn-00bad02c) → [`00bad150`](#insn-00bad150) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad050`](#insn-00bad050) → [`00bad0b0`](#insn-00bad0b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad084`](#insn-00bad084) → [`00bad0b8`](#insn-00bad0b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad0a0`](#insn-00bad0a0) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00bad0a4`](#insn-00bad0a4) → [`00bad0b8`](#insn-00bad0b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad0a8`](#insn-00bad0a8) → [`00bad0c0`](#insn-00bad0c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad0ac`](#insn-00bad0ac) → [`00bad150`](#insn-00bad150) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad0b0`](#insn-00bad0b0) → [`00bad0c0`](#insn-00bad0c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad0b4`](#insn-00bad0b4) → [`00bad150`](#insn-00bad150) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad0bc`](#insn-00bad0bc) → [`00bad150`](#insn-00bad150) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad0e0`](#insn-00bad0e0) → [`00bad140`](#insn-00bad140) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad114`](#insn-00bad114) → [`00bad174`](#insn-00bad174) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad130`](#insn-00bad130) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00bad134`](#insn-00bad134) → [`00bad174`](#insn-00bad174) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad138`](#insn-00bad138) → [`00bad144`](#insn-00bad144) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad13c`](#insn-00bad13c) → [`00bad150`](#insn-00bad150) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad140`](#insn-00bad140) → [`00bad150`](#insn-00bad150) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad154`](#insn-00bad154) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad158`](#insn-00bad158) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad15c`](#insn-00bad15c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad160`](#insn-00bad160) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad164`](#insn-00bad164) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad168`](#insn-00bad168) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad178`](#insn-00bad178) → [`00bad144`](#insn-00bad144) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad17c`](#insn-00bad17c) → [`00bad150`](#insn-00bad150) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bacea4`](#insn-00bacea4)

~~~json
{
  "source": "00bacea4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacea8`](#insn-00bacea8)

~~~json
{
  "source": "00bacea8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baceac`](#insn-00baceac)

~~~json
{
  "source": "00baceac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baceb0`](#insn-00baceb0)

~~~json
{
  "source": "00baceb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baceb4`](#insn-00baceb4)

~~~json
{
  "source": "00baceb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baceb8`](#insn-00baceb8)

~~~json
{
  "source": "00baceb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baced4`](#insn-00baced4)

~~~json
{
  "source": "00baced4",
  "target": "00bacc98",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bacef4`](#insn-00bacef4)

~~~json
{
  "source": "00bacef4",
  "target": "00bacf7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf10`](#insn-00bacf10)

~~~json
{
  "source": "00bacf10",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf3c`](#insn-00bacf3c)

~~~json
{
  "source": "00bacf3c",
  "target": "00bacf84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf58`](#insn-00bacf58)

~~~json
{
  "source": "00bacf58",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bacf5c`](#insn-00bacf5c)

~~~json
{
  "source": "00bacf5c",
  "target": "00bacf84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf70`](#insn-00bacf70)

~~~json
{
  "source": "00bacf70",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf74`](#insn-00bacf74)

~~~json
{
  "source": "00bacf74",
  "target": "00bacfa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf78`](#insn-00bacf78)

~~~json
{
  "source": "00bacf78",
  "target": "00bad150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf7c`](#insn-00bacf7c)

~~~json
{
  "source": "00bacf7c",
  "target": "00bacfa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf80`](#insn-00bacf80)

~~~json
{
  "source": "00bacf80",
  "target": "00bad150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf98`](#insn-00bacf98)

~~~json
{
  "source": "00bacf98",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf9c`](#insn-00bacf9c)

~~~json
{
  "source": "00bacf9c",
  "target": "00bad150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacfc0`](#insn-00bacfc0)

~~~json
{
  "source": "00bacfc0",
  "target": "00bad020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacff4`](#insn-00bacff4)

~~~json
{
  "source": "00bacff4",
  "target": "00bad028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad010`](#insn-00bad010)

~~~json
{
  "source": "00bad010",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad014`](#insn-00bad014)

~~~json
{
  "source": "00bad014",
  "target": "00bad028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad018`](#insn-00bad018)

~~~json
{
  "source": "00bad018",
  "target": "00bad030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad01c`](#insn-00bad01c)

~~~json
{
  "source": "00bad01c",
  "target": "00bad150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad020`](#insn-00bad020)

~~~json
{
  "source": "00bad020",
  "target": "00bad030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad024`](#insn-00bad024)

~~~json
{
  "source": "00bad024",
  "target": "00bad150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad02c`](#insn-00bad02c)

~~~json
{
  "source": "00bad02c",
  "target": "00bad150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad050`](#insn-00bad050)

~~~json
{
  "source": "00bad050",
  "target": "00bad0b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad084`](#insn-00bad084)

~~~json
{
  "source": "00bad084",
  "target": "00bad0b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad0a0`](#insn-00bad0a0)

~~~json
{
  "source": "00bad0a0",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad0a4`](#insn-00bad0a4)

~~~json
{
  "source": "00bad0a4",
  "target": "00bad0b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad0a8`](#insn-00bad0a8)

~~~json
{
  "source": "00bad0a8",
  "target": "00bad0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad0ac`](#insn-00bad0ac)

~~~json
{
  "source": "00bad0ac",
  "target": "00bad150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad0b0`](#insn-00bad0b0)

~~~json
{
  "source": "00bad0b0",
  "target": "00bad0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad0b4`](#insn-00bad0b4)

~~~json
{
  "source": "00bad0b4",
  "target": "00bad150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad0bc`](#insn-00bad0bc)

~~~json
{
  "source": "00bad0bc",
  "target": "00bad150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad0e0`](#insn-00bad0e0)

~~~json
{
  "source": "00bad0e0",
  "target": "00bad140",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad114`](#insn-00bad114)

~~~json
{
  "source": "00bad114",
  "target": "00bad174",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad130`](#insn-00bad130)

~~~json
{
  "source": "00bad130",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad134`](#insn-00bad134)

~~~json
{
  "source": "00bad134",
  "target": "00bad174",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad138`](#insn-00bad138)

~~~json
{
  "source": "00bad138",
  "target": "00bad144",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad13c`](#insn-00bad13c)

~~~json
{
  "source": "00bad13c",
  "target": "00bad150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad140`](#insn-00bad140)

~~~json
{
  "source": "00bad140",
  "target": "00bad150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad154`](#insn-00bad154)

~~~json
{
  "source": "00bad154",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad158`](#insn-00bad158)

~~~json
{
  "source": "00bad158",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad15c`](#insn-00bad15c)

~~~json
{
  "source": "00bad15c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad160`](#insn-00bad160)

~~~json
{
  "source": "00bad160",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad164`](#insn-00bad164)

~~~json
{
  "source": "00bad164",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad168`](#insn-00bad168)

~~~json
{
  "source": "00bad168",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad178`](#insn-00bad178)

~~~json
{
  "source": "00bad178",
  "target": "00bad144",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad17c`](#insn-00bad17c)

~~~json
{
  "source": "00bad17c",
  "target": "00bad150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
