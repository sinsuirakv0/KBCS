# 00bac9dc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0174.md#review-60ffe3a56eca669ad07e900d3ac260b0)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bace04`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bac/00bace04.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0078.md#compare-0e95c680586a5bc6e904ef5c08a124b0)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bac9dc",
  "name": "FUN_00bac9dc",
  "size": 736,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a32da9991f5090460fc8052fd86edec18e4fbb90041a9c3f4c005190d0e89a65",
  "source_text_sha256": "a32da9991f5090460fc8052fd86edec18e4fbb90041a9c3f4c005190d0e89a65",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bac9dc",
        "00baccbb"
      ]
    ],
    "bytes_sha256": "4b70baf147d9e03c1f42ee652f5bb304a12b6d8a7ee2a492b6a394c71ca55c78",
    "instruction_count": 184,
    "instruction_bytes": 736,
    "body_bytes": 736,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00babb74](../00bab/00babb74.md)
- [00baccbc](../00bac/00baccbc.md)

## 呼び出し先

- [00bac7d4](../00bac/00bac7d4.md)
- [00c57c50](../00c57/00c57c50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 7778 bytes

~~~c

int FUN_00bac9dc(undefined8 *param_1,undefined8 *param_2,undefined8 *param_3,undefined8 *param_4,
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
  
                    /* try { // try from 00bac9f8 to 00caca03 has its CatchHandler @ 00bacbac */
  iVar6 = FUN_00bac7d4();
  pbVar11 = (byte *)*param_5;
                    /* try { // try from 00baca18 to 00caca23 has its CatchHandler @ 00bacba8 */
  pbVar12 = (byte *)*param_4;
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
    bVar4 = *pbVar12;
    bVar5 = *pbVar11;
                    /* try { // try from 00baca44 to 00caca4f has its CatchHandler @ 00bacb98 */
    uVar1 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar12 + 8);
    }
                    /* try { // try from 00baca68 to 00caca73 has its CatchHandler @ 00bacb94 */
    uVar2 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar11 + 8);
    }
    sVar3 = uVar1;
    if (uVar2 <= uVar1) {
      sVar3 = uVar2;
    }
    if (sVar3 != 0) {
                    /* try { // try from 00baca7c to 00caca83 has its CatchHandler @ 00bacc6c */
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
                    /* try { // try from 00bacaa0 to 00cacaab has its CatchHandler @ 00bacb84 */
        if (-1 < iVar7) {
          return iVar6;
        }
        goto LAB_00bacadc;
      }
    }
                    /* try { // try from 00bacac0 to 00cacacb has its CatchHandler @ 00bacb80 */
                    /* try { // try from 00bacacc to 00cacae7 has its CatchHandler @ 00bacc20 */
    if (uVar1 <= uVar2) {
      return iVar6;
    }
  }
  else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
    return iVar6;
  }
LAB_00bacadc:
  *param_4 = pbVar11;
  *param_5 = pbVar12;
  pbVar11 = (byte *)*param_4;
                    /* try { // try from 00bacae8 to 00cacb57 has its CatchHandler @ 00bacca4 */
  pbVar12 = (byte *)*param_3;
  iVar7 = iVar6 + 1;
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
    bVar4 = *pbVar12;
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
      iVar8 = memcmp(pbVar9,pbVar10,sVar3);
      if (iVar8 != 0) {
        if (-1 < iVar8) {
          return iVar7;
        }
        goto LAB_00bacb6c;
      }
    }
    if (uVar1 <= uVar2) {
      return iVar7;
    }
  }
  else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
    return iVar7;
  }
LAB_00bacb6c:
  *param_3 = pbVar11;
  *param_4 = pbVar12;
  pbVar11 = (byte *)*param_3;
  pbVar12 = (byte *)*param_2;
  iVar7 = iVar6 + 2;
                    /* catch() { ... } // from try @ 00bacac0 with catch @ 00bacb80 */
                    /* catch() { ... } // from try @ 00bacaa0 with catch @ 00bacb84 */
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
    bVar4 = *pbVar12;
                    /* catch() { ... } // from try @ 00baca68 with catch @ 00bacb94 */
                    /* catch() { ... } // from try @ 00baca44 with catch @ 00bacb98 */
    bVar5 = *pbVar11;
                    /* catch() { ... } // from try @ 00baca18 with catch @ 00bacba8 */
    uVar1 = (ulong)(bVar4 >> 1);
                    /* catch() { ... } // from try @ 00bac9f8 with catch @ 00bacbac */
    if ((bVar4 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar12 + 8);
    }
    uVar2 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar11 + 8);
    }
    sVar3 = uVar1;
                    /* catch() { ... } // from try @ 00bac9ac with catch @ 00bacbbc */
    if (uVar2 <= uVar1) {
      sVar3 = uVar2;
    }
                    /* catch() { ... } // from try @ 00bac988 with catch @ 00bacbc0 */
    if (sVar3 != 0) {
      pbVar9 = *(byte **)(pbVar11 + 0x10);
      pbVar10 = *(byte **)(pbVar12 + 0x10);
                    /* catch() { ... } // from try @ 00bac95c with catch @ 00bacbd0 */
      if ((bVar5 & 1) == 0) {
        pbVar9 = pbVar11 + 1;
      }
                    /* catch() { ... } // from try @ 00bac93c with catch @ 00bacbd4 */
      if ((bVar4 & 1) == 0) {
        pbVar10 = pbVar12 + 1;
      }
      iVar8 = memcmp(pbVar9,pbVar10,sVar3);
      if (iVar8 != 0) {
                    /* catch() { ... } // from try @ 00bac908 with catch @ 00bacbe4 */
        if (-1 < iVar8) {
          return iVar7;
        }
        goto LAB_00bacbfc;
      }
    }
                    /* catch() { ... } // from try @ 00bac8b8 with catch @ 00bacbf8 */
    if (uVar1 <= uVar2) {
      return iVar7;
    }
  }
  else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
    return iVar7;
  }
LAB_00bacbfc:
                    /* catch() { ... } // from try @ 00bac898 with catch @ 00bacbfc */
  *param_2 = pbVar11;
  *param_3 = pbVar12;
  pbVar11 = (byte *)*param_2;
  pbVar12 = (byte *)*param_1;
                    /* catch() { ... } // from try @ 00bac860 with catch @ 00bacc0c */
  iVar7 = iVar6 + 3;
                    /* catch() { ... } // from try @ 00bac83c with catch @ 00bacc10 */
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
                    /* catch() { ... } // from try @ 00bacacc with catch @ 00bacc20 */
    bVar4 = *pbVar12;
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
                    /* catch() { ... } // from try @ 00bac874 with catch @ 00bacc6c
                       catch() { ... } // from try @ 00bac91c with catch @ 00bacc6c
                       catch() { ... } // from try @ 00bac9c0 with catch @ 00bacc6c
                       catch() { ... } // from try @ 00baca7c with catch @ 00bacc6c */
      iVar8 = memcmp(pbVar9,pbVar10,sVar3);
      if (iVar8 != 0) {
        if (-1 < iVar8) {
          return iVar7;
        }
        goto LAB_00bacc80;
      }
    }
    if (uVar1 <= uVar2) {
      return iVar7;
    }
  }
  else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
    return iVar7;
  }
LAB_00bacc80:
  *param_1 = pbVar11;
  *param_2 = pbVar12;
                    /* catch() { ... } // from try @ 00bacae8 with catch @ 00bacca4 */
                    /* try { // try from 00bacca8 to 00cacd5f has its CatchHandler @ 00bacca8
                       catch() { ... } // from try @ 00bacca8 with catch @ 00bacca8
                       catch() { ... } // from try @ 00bacf6c with catch @ 00bacca8
                       catch() { ... } // from try @ 00bad228 with catch @ 00bacca8 */
  return iVar6 + 4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bac9dc"></a> `00bac9dc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bac9e0"></a> `00bac9e0` | `fc 6f 01 a9` | stp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bac9e4"></a> `00bac9e4` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bac9e8"></a> `00bac9e8` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bac9ec"></a> `00bac9ec` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bac9f0"></a> `00bac9f0` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bac9f4"></a> `00bac9f4` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bac9f8"></a> `00bac9f8` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bac9fc"></a> `00bac9fc` | `f9 03 04 aa` | mov x25,x4 | `FALL_THROUGH`
<a id="insn-00baca00"></a> `00baca00` | `f8 03 03 aa` | mov x24,x3 | `FALL_THROUGH`
<a id="insn-00baca04"></a> `00baca04` | `f7 03 02 aa` | mov x23,x2 | `FALL_THROUGH`
<a id="insn-00baca08"></a> `00baca08` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00baca0c"></a> `00baca0c` | `fc 03 00 aa` | mov x28,x0 | `FALL_THROUGH`
<a id="insn-00baca10"></a> `00baca10` | `71 ff ff 97` | bl 0x00bac7d4 | `UNCONDITIONAL_CALL`
<a id="insn-00baca14"></a> `00baca14` | `3a 03 40 f9` | ldr x26,[x25] | `FALL_THROUGH`
<a id="insn-00baca18"></a> `00baca18` | `1b 03 40 f9` | ldr x27,[x24] | `FALL_THROUGH`
<a id="insn-00baca1c"></a> `00baca1c` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00baca20"></a> `00baca20` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00baca24"></a> `00baca24` | `48 43 40 f9` | ldr x8,[x26, #0x80] | `FALL_THROUGH`
<a id="insn-00baca28"></a> `00baca28` | `69 43 40 f9` | ldr x9,[x27, #0x80] | `FALL_THROUGH`
<a id="insn-00baca2c"></a> `00baca2c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00baca30"></a> `00baca30` | `41 04 00 54` | b.ne 0x00bacab8 | `CONDITIONAL_JUMP`
<a id="insn-00baca34"></a> `00baca34` | `68 03 40 39` | ldrb w8,[x27] | `FALL_THROUGH`
<a id="insn-00baca38"></a> `00baca38` | `6a 07 40 f9` | ldr x10,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-00baca3c"></a> `00baca3c` | `49 03 40 39` | ldrb w9,[x26] | `FALL_THROUGH`
<a id="insn-00baca40"></a> `00baca40` | `4b 07 40 f9` | ldr x11,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00baca44"></a> `00baca44` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00baca48"></a> `00baca48` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baca4c"></a> `00baca4c` | `f7 07 00 f9` | str x23,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00baca50"></a> `00baca50` | `f7 03 16 2a` | mov w23,w22 | `FALL_THROUGH`
<a id="insn-00baca54"></a> `00baca54` | `f6 03 15 2a` | mov w22,w21 | `FALL_THROUGH`
<a id="insn-00baca58"></a> `00baca58` | `f5 03 13 aa` | mov x21,x19 | `FALL_THROUGH`
<a id="insn-00baca5c"></a> `00baca5c` | `f3 03 1c aa` | mov x19,x28 | `FALL_THROUGH`
<a id="insn-00baca60"></a> `00baca60` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00baca64"></a> `00baca64` | `9c 01 8a 9a` | csel x28,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00baca68"></a> `00baca68` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baca6c"></a> `00baca6c` | `b4 01 8b 9a` | csel x20,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00baca70"></a> `00baca70` | `9f 03 14 eb` | cmp x28,x20 | `FALL_THROUGH`
<a id="insn-00baca74"></a> `00baca74` | `82 33 94 9a` | csel x2,x28,x20,cc | `FALL_THROUGH`
<a id="insn-00baca78"></a> `00baca78` | `42 02 00 b4` | cbz x2,0x00bacac0 | `CONDITIONAL_JUMP`
<a id="insn-00baca7c"></a> `00baca7c` | `4a 0b 40 f9` | ldr x10,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00baca80"></a> `00baca80` | `6b 0b 40 f9` | ldr x11,[x27, #0x10] | `FALL_THROUGH`
<a id="insn-00baca84"></a> `00baca84` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baca88"></a> `00baca88` | `40 15 9a 9a` | csinc x0,x10,x26,ne | `FALL_THROUGH`
<a id="insn-00baca8c"></a> `00baca8c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baca90"></a> `00baca90` | `61 15 9b 9a` | csinc x1,x11,x27,ne | `FALL_THROUGH`
<a id="insn-00baca94"></a> `00baca94` | `6f ac 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00baca98"></a> `00baca98` | `40 01 00 34` | cbz w0,0x00bacac0 | `CONDITIONAL_JUMP`
<a id="insn-00baca9c"></a> `00baca9c` | `fc 03 13 aa` | mov x28,x19 | `FALL_THROUGH`
<a id="insn-00bacaa0"></a> `00bacaa0` | `f3 03 15 aa` | mov x19,x21 | `FALL_THROUGH`
<a id="insn-00bacaa4"></a> `00bacaa4` | `f5 03 16 2a` | mov w21,w22 | `FALL_THROUGH`
<a id="insn-00bacaa8"></a> `00bacaa8` | `f6 03 17 2a` | mov w22,w23 | `FALL_THROUGH`
<a id="insn-00bacaac"></a> `00bacaac` | `f7 07 40 f9` | ldr x23,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bacab0"></a> `00bacab0` | `60 01 f8 37` | tbnz w0,#0x1f,0x00bacadc | `CONDITIONAL_JUMP`
<a id="insn-00bacab4"></a> `00bacab4` | `76 00 00 14` | b 0x00bacc8c | `UNCONDITIONAL_JUMP`
<a id="insn-00bacab8"></a> `00bacab8` | `23 01 00 54` | b.cc 0x00bacadc | `CONDITIONAL_JUMP`
<a id="insn-00bacabc"></a> `00bacabc` | `74 00 00 14` | b 0x00bacc8c | `UNCONDITIONAL_JUMP`
<a id="insn-00bacac0"></a> `00bacac0` | `9f 02 1c eb` | cmp x20,x28 | `FALL_THROUGH`
<a id="insn-00bacac4"></a> `00bacac4` | `fc 03 13 aa` | mov x28,x19 | `FALL_THROUGH`
<a id="insn-00bacac8"></a> `00bacac8` | `f3 03 15 aa` | mov x19,x21 | `FALL_THROUGH`
<a id="insn-00bacacc"></a> `00bacacc` | `f5 03 16 2a` | mov w21,w22 | `FALL_THROUGH`
<a id="insn-00bacad0"></a> `00bacad0` | `f6 03 17 2a` | mov w22,w23 | `FALL_THROUGH`
<a id="insn-00bacad4"></a> `00bacad4` | `f7 07 40 f9` | ldr x23,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bacad8"></a> `00bacad8` | `a2 0d 00 54` | b.cs 0x00bacc8c | `CONDITIONAL_JUMP`
<a id="insn-00bacadc"></a> `00bacadc` | `1a 03 00 f9` | str x26,[x24] | `FALL_THROUGH`
<a id="insn-00bacae0"></a> `00bacae0` | `3b 03 00 f9` | str x27,[x25] | `FALL_THROUGH`
<a id="insn-00bacae4"></a> `00bacae4` | `19 03 40 f9` | ldr x25,[x24] | `FALL_THROUGH`
<a id="insn-00bacae8"></a> `00bacae8` | `fa 02 40 f9` | ldr x26,[x23] | `FALL_THROUGH`
<a id="insn-00bacaec"></a> `00bacaec` | `b6 06 00 11` | add w22,w21,#0x1 | `FALL_THROUGH`
<a id="insn-00bacaf0"></a> `00bacaf0` | `28 43 40 f9` | ldr x8,[x25, #0x80] | `FALL_THROUGH`
<a id="insn-00bacaf4"></a> `00bacaf4` | `49 43 40 f9` | ldr x9,[x26, #0x80] | `FALL_THROUGH`
<a id="insn-00bacaf8"></a> `00bacaf8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bacafc"></a> `00bacafc` | `01 03 00 54` | b.ne 0x00bacb5c | `CONDITIONAL_JUMP`
<a id="insn-00bacb00"></a> `00bacb00` | `48 03 40 39` | ldrb w8,[x26] | `FALL_THROUGH`
<a id="insn-00bacb04"></a> `00bacb04` | `4a 07 40 f9` | ldr x10,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00bacb08"></a> `00bacb08` | `29 03 40 39` | ldrb w9,[x25] | `FALL_THROUGH`
<a id="insn-00bacb0c"></a> `00bacb0c` | `2b 07 40 f9` | ldr x11,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00bacb10"></a> `00bacb10` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacb14"></a> `00bacb14` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacb18"></a> `00bacb18` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacb1c"></a> `00bacb1c` | `9b 01 8a 9a` | csel x27,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bacb20"></a> `00bacb20` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacb24"></a> `00bacb24` | `b4 01 8b 9a` | csel x20,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bacb28"></a> `00bacb28` | `7f 03 14 eb` | cmp x27,x20 | `FALL_THROUGH`
<a id="insn-00bacb2c"></a> `00bacb2c` | `62 33 94 9a` | csel x2,x27,x20,cc | `FALL_THROUGH`
<a id="insn-00bacb30"></a> `00bacb30` | `a2 01 00 b4` | cbz x2,0x00bacb64 | `CONDITIONAL_JUMP`
<a id="insn-00bacb34"></a> `00bacb34` | `2a 0b 40 f9` | ldr x10,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00bacb38"></a> `00bacb38` | `4b 0b 40 f9` | ldr x11,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00bacb3c"></a> `00bacb3c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacb40"></a> `00bacb40` | `40 15 99 9a` | csinc x0,x10,x25,ne | `FALL_THROUGH`
<a id="insn-00bacb44"></a> `00bacb44` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacb48"></a> `00bacb48` | `61 15 9a 9a` | csinc x1,x11,x26,ne | `FALL_THROUGH`
<a id="insn-00bacb4c"></a> `00bacb4c` | `41 ac 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bacb50"></a> `00bacb50` | `a0 00 00 34` | cbz w0,0x00bacb64 | `CONDITIONAL_JUMP`
<a id="insn-00bacb54"></a> `00bacb54` | `c0 00 f8 37` | tbnz w0,#0x1f,0x00bacb6c | `CONDITIONAL_JUMP`
<a id="insn-00bacb58"></a> `00bacb58` | `4d 00 00 14` | b 0x00bacc8c | `UNCONDITIONAL_JUMP`
<a id="insn-00bacb5c"></a> `00bacb5c` | `83 00 00 54` | b.cc 0x00bacb6c | `CONDITIONAL_JUMP`
<a id="insn-00bacb60"></a> `00bacb60` | `4b 00 00 14` | b 0x00bacc8c | `UNCONDITIONAL_JUMP`
<a id="insn-00bacb64"></a> `00bacb64` | `9f 02 1b eb` | cmp x20,x27 | `FALL_THROUGH`
<a id="insn-00bacb68"></a> `00bacb68` | `22 09 00 54` | b.cs 0x00bacc8c | `CONDITIONAL_JUMP`
<a id="insn-00bacb6c"></a> `00bacb6c` | `f9 02 00 f9` | str x25,[x23] | `FALL_THROUGH`
<a id="insn-00bacb70"></a> `00bacb70` | `1a 03 00 f9` | str x26,[x24] | `FALL_THROUGH`
<a id="insn-00bacb74"></a> `00bacb74` | `f8 02 40 f9` | ldr x24,[x23] | `FALL_THROUGH`
<a id="insn-00bacb78"></a> `00bacb78` | `79 02 40 f9` | ldr x25,[x19] | `FALL_THROUGH`
<a id="insn-00bacb7c"></a> `00bacb7c` | `b6 0a 00 11` | add w22,w21,#0x2 | `FALL_THROUGH`
<a id="insn-00bacb80"></a> `00bacb80` | `08 43 40 f9` | ldr x8,[x24, #0x80] | `FALL_THROUGH`
<a id="insn-00bacb84"></a> `00bacb84` | `29 43 40 f9` | ldr x9,[x25, #0x80] | `FALL_THROUGH`
<a id="insn-00bacb88"></a> `00bacb88` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bacb8c"></a> `00bacb8c` | `01 03 00 54` | b.ne 0x00bacbec | `CONDITIONAL_JUMP`
<a id="insn-00bacb90"></a> `00bacb90` | `28 03 40 39` | ldrb w8,[x25] | `FALL_THROUGH`
<a id="insn-00bacb94"></a> `00bacb94` | `2a 07 40 f9` | ldr x10,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00bacb98"></a> `00bacb98` | `09 03 40 39` | ldrb w9,[x24] | `FALL_THROUGH`
<a id="insn-00bacb9c"></a> `00bacb9c` | `0b 07 40 f9` | ldr x11,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00bacba0"></a> `00bacba0` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacba4"></a> `00bacba4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacba8"></a> `00bacba8` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacbac"></a> `00bacbac` | `9a 01 8a 9a` | csel x26,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bacbb0"></a> `00bacbb0` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacbb4"></a> `00bacbb4` | `b4 01 8b 9a` | csel x20,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bacbb8"></a> `00bacbb8` | `5f 03 14 eb` | cmp x26,x20 | `FALL_THROUGH`
<a id="insn-00bacbbc"></a> `00bacbbc` | `42 33 94 9a` | csel x2,x26,x20,cc | `FALL_THROUGH`
<a id="insn-00bacbc0"></a> `00bacbc0` | `a2 01 00 b4` | cbz x2,0x00bacbf4 | `CONDITIONAL_JUMP`
<a id="insn-00bacbc4"></a> `00bacbc4` | `0a 0b 40 f9` | ldr x10,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bacbc8"></a> `00bacbc8` | `2b 0b 40 f9` | ldr x11,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00bacbcc"></a> `00bacbcc` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacbd0"></a> `00bacbd0` | `40 15 98 9a` | csinc x0,x10,x24,ne | `FALL_THROUGH`
<a id="insn-00bacbd4"></a> `00bacbd4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacbd8"></a> `00bacbd8` | `61 15 99 9a` | csinc x1,x11,x25,ne | `FALL_THROUGH`
<a id="insn-00bacbdc"></a> `00bacbdc` | `1d ac 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bacbe0"></a> `00bacbe0` | `a0 00 00 34` | cbz w0,0x00bacbf4 | `CONDITIONAL_JUMP`
<a id="insn-00bacbe4"></a> `00bacbe4` | `c0 00 f8 37` | tbnz w0,#0x1f,0x00bacbfc | `CONDITIONAL_JUMP`
<a id="insn-00bacbe8"></a> `00bacbe8` | `29 00 00 14` | b 0x00bacc8c | `UNCONDITIONAL_JUMP`
<a id="insn-00bacbec"></a> `00bacbec` | `83 00 00 54` | b.cc 0x00bacbfc | `CONDITIONAL_JUMP`
<a id="insn-00bacbf0"></a> `00bacbf0` | `27 00 00 14` | b 0x00bacc8c | `UNCONDITIONAL_JUMP`
<a id="insn-00bacbf4"></a> `00bacbf4` | `9f 02 1a eb` | cmp x20,x26 | `FALL_THROUGH`
<a id="insn-00bacbf8"></a> `00bacbf8` | `a2 04 00 54` | b.cs 0x00bacc8c | `CONDITIONAL_JUMP`
<a id="insn-00bacbfc"></a> `00bacbfc` | `78 02 00 f9` | str x24,[x19] | `FALL_THROUGH`
<a id="insn-00bacc00"></a> `00bacc00` | `f9 02 00 f9` | str x25,[x23] | `FALL_THROUGH`
<a id="insn-00bacc04"></a> `00bacc04` | `77 02 40 f9` | ldr x23,[x19] | `FALL_THROUGH`
<a id="insn-00bacc08"></a> `00bacc08` | `98 03 40 f9` | ldr x24,[x28] | `FALL_THROUGH`
<a id="insn-00bacc0c"></a> `00bacc0c` | `b6 0e 00 11` | add w22,w21,#0x3 | `FALL_THROUGH`
<a id="insn-00bacc10"></a> `00bacc10` | `e8 42 40 f9` | ldr x8,[x23, #0x80] | `FALL_THROUGH`
<a id="insn-00bacc14"></a> `00bacc14` | `09 43 40 f9` | ldr x9,[x24, #0x80] | `FALL_THROUGH`
<a id="insn-00bacc18"></a> `00bacc18` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bacc1c"></a> `00bacc1c` | `01 03 00 54` | b.ne 0x00bacc7c | `CONDITIONAL_JUMP`
<a id="insn-00bacc20"></a> `00bacc20` | `08 03 40 39` | ldrb w8,[x24] | `FALL_THROUGH`
<a id="insn-00bacc24"></a> `00bacc24` | `0a 07 40 f9` | ldr x10,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00bacc28"></a> `00bacc28` | `e9 02 40 39` | ldrb w9,[x23] | `FALL_THROUGH`
<a id="insn-00bacc2c"></a> `00bacc2c` | `eb 06 40 f9` | ldr x11,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bacc30"></a> `00bacc30` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacc34"></a> `00bacc34` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacc38"></a> `00bacc38` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacc3c"></a> `00bacc3c` | `99 01 8a 9a` | csel x25,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bacc40"></a> `00bacc40` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacc44"></a> `00bacc44` | `b4 01 8b 9a` | csel x20,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bacc48"></a> `00bacc48` | `3f 03 14 eb` | cmp x25,x20 | `FALL_THROUGH`
<a id="insn-00bacc4c"></a> `00bacc4c` | `22 33 94 9a` | csel x2,x25,x20,cc | `FALL_THROUGH`
<a id="insn-00bacc50"></a> `00bacc50` | `02 03 00 b4` | cbz x2,0x00baccb0 | `CONDITIONAL_JUMP`
<a id="insn-00bacc54"></a> `00bacc54` | `ea 0a 40 f9` | ldr x10,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00bacc58"></a> `00bacc58` | `0b 0b 40 f9` | ldr x11,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bacc5c"></a> `00bacc5c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacc60"></a> `00bacc60` | `40 15 97 9a` | csinc x0,x10,x23,ne | `FALL_THROUGH`
<a id="insn-00bacc64"></a> `00bacc64` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacc68"></a> `00bacc68` | `61 15 98 9a` | csinc x1,x11,x24,ne | `FALL_THROUGH`
<a id="insn-00bacc6c"></a> `00bacc6c` | `f9 ab 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bacc70"></a> `00bacc70` | `00 02 00 34` | cbz w0,0x00baccb0 | `CONDITIONAL_JUMP`
<a id="insn-00bacc74"></a> `00bacc74` | `60 00 f8 37` | tbnz w0,#0x1f,0x00bacc80 | `CONDITIONAL_JUMP`
<a id="insn-00bacc78"></a> `00bacc78` | `05 00 00 14` | b 0x00bacc8c | `UNCONDITIONAL_JUMP`
<a id="insn-00bacc7c"></a> `00bacc7c` | `82 00 00 54` | b.cs 0x00bacc8c | `CONDITIONAL_JUMP`
<a id="insn-00bacc80"></a> `00bacc80` | `b6 12 00 11` | add w22,w21,#0x4 | `FALL_THROUGH`
<a id="insn-00bacc84"></a> `00bacc84` | `97 03 00 f9` | str x23,[x28] | `FALL_THROUGH`
<a id="insn-00bacc88"></a> `00bacc88` | `78 02 00 f9` | str x24,[x19] | `FALL_THROUGH`
<a id="insn-00bacc8c"></a> `00bacc8c` | `e0 03 16 2a` | mov w0,w22 | `FALL_THROUGH`
<a id="insn-00bacc90"></a> `00bacc90` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bacc94"></a> `00bacc94` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bacc98"></a> `00bacc98` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bacc9c"></a> `00bacc9c` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bacca0"></a> `00bacca0` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bacca4"></a> `00bacca4` | `fc 6f 41 a9` | ldp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bacca8"></a> `00bacca8` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00baccac"></a> `00baccac` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00baccb0"></a> `00baccb0` | `9f 02 19 eb` | cmp x20,x25 | `FALL_THROUGH`
<a id="insn-00baccb4"></a> `00baccb4` | `63 fe ff 54` | b.cc 0x00bacc80 | `CONDITIONAL_JUMP`
<a id="insn-00baccb8"></a> `00baccb8` | `f5 ff ff 17` | b 0x00bacc8c | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bac9dc`](#insn-00bac9dc) 範囲 `[['00bac9dc', '00bac9f7']]`
  - `FALL_THROUGH` [`00bac9f4`](#insn-00bac9f4) → [`00bac9f8`](#insn-00bac9f8)
- ブロック [`00bac9f8`](#insn-00bac9f8) 範囲 `[['00bac9f8', '00baca17']]`
  - `FALL_THROUGH` [`00baca14`](#insn-00baca14) → [`00baca18`](#insn-00baca18)
- ブロック [`00baca18`](#insn-00baca18) 範囲 `[['00baca18', '00baca33']]`
  - `CONDITIONAL_JUMP` [`00baca30`](#insn-00baca30) → [`00bacab8`](#insn-00bacab8)
  - `FALL_THROUGH` [`00baca30`](#insn-00baca30) → [`00baca34`](#insn-00baca34)
- ブロック [`00baca34`](#insn-00baca34) 範囲 `[['00baca34', '00baca43']]`
  - `FALL_THROUGH` [`00baca40`](#insn-00baca40) → [`00baca44`](#insn-00baca44)
- ブロック [`00baca44`](#insn-00baca44) 範囲 `[['00baca44', '00baca67']]`
  - `FALL_THROUGH` [`00baca64`](#insn-00baca64) → [`00baca68`](#insn-00baca68)
- ブロック [`00baca68`](#insn-00baca68) 範囲 `[['00baca68', '00baca7b']]`
  - `CONDITIONAL_JUMP` [`00baca78`](#insn-00baca78) → [`00bacac0`](#insn-00bacac0)
  - `FALL_THROUGH` [`00baca78`](#insn-00baca78) → [`00baca7c`](#insn-00baca7c)
- ブロック [`00baca7c`](#insn-00baca7c) 範囲 `[['00baca7c', '00baca9b']]`
  - `CONDITIONAL_JUMP` [`00baca98`](#insn-00baca98) → [`00bacac0`](#insn-00bacac0)
  - `FALL_THROUGH` [`00baca98`](#insn-00baca98) → [`00baca9c`](#insn-00baca9c)
- ブロック [`00baca9c`](#insn-00baca9c) 範囲 `[['00baca9c', '00baca9f']]`
  - `FALL_THROUGH` [`00baca9c`](#insn-00baca9c) → [`00bacaa0`](#insn-00bacaa0)
- ブロック [`00bacaa0`](#insn-00bacaa0) 範囲 `[['00bacaa0', '00bacab3']]`
  - `CONDITIONAL_JUMP` [`00bacab0`](#insn-00bacab0) → [`00bacadc`](#insn-00bacadc)
  - `FALL_THROUGH` [`00bacab0`](#insn-00bacab0) → [`00bacab4`](#insn-00bacab4)
- ブロック [`00bacab4`](#insn-00bacab4) 範囲 `[['00bacab4', '00bacab7']]`
  - `UNCONDITIONAL_JUMP` [`00bacab4`](#insn-00bacab4) → [`00bacc8c`](#insn-00bacc8c)
- ブロック [`00bacab8`](#insn-00bacab8) 範囲 `[['00bacab8', '00bacabb']]`
  - `CONDITIONAL_JUMP` [`00bacab8`](#insn-00bacab8) → [`00bacadc`](#insn-00bacadc)
  - `FALL_THROUGH` [`00bacab8`](#insn-00bacab8) → [`00bacabc`](#insn-00bacabc)
- ブロック [`00bacabc`](#insn-00bacabc) 範囲 `[['00bacabc', '00bacabf']]`
  - `UNCONDITIONAL_JUMP` [`00bacabc`](#insn-00bacabc) → [`00bacc8c`](#insn-00bacc8c)
- ブロック [`00bacac0`](#insn-00bacac0) 範囲 `[['00bacac0', '00bacacb']]`
  - `FALL_THROUGH` [`00bacac8`](#insn-00bacac8) → [`00bacacc`](#insn-00bacacc)
- ブロック [`00bacacc`](#insn-00bacacc) 範囲 `[['00bacacc', '00bacadb']]`
  - `CONDITIONAL_JUMP` [`00bacad8`](#insn-00bacad8) → [`00bacc8c`](#insn-00bacc8c)
  - `FALL_THROUGH` [`00bacad8`](#insn-00bacad8) → [`00bacadc`](#insn-00bacadc)
- ブロック [`00bacadc`](#insn-00bacadc) 範囲 `[['00bacadc', '00bacae7']]`
  - `FALL_THROUGH` [`00bacae4`](#insn-00bacae4) → [`00bacae8`](#insn-00bacae8)
- ブロック [`00bacae8`](#insn-00bacae8) 範囲 `[['00bacae8', '00bacaff']]`
  - `CONDITIONAL_JUMP` [`00bacafc`](#insn-00bacafc) → [`00bacb5c`](#insn-00bacb5c)
  - `FALL_THROUGH` [`00bacafc`](#insn-00bacafc) → [`00bacb00`](#insn-00bacb00)
- ブロック [`00bacb00`](#insn-00bacb00) 範囲 `[['00bacb00', '00bacb33']]`
  - `CONDITIONAL_JUMP` [`00bacb30`](#insn-00bacb30) → [`00bacb64`](#insn-00bacb64)
  - `FALL_THROUGH` [`00bacb30`](#insn-00bacb30) → [`00bacb34`](#insn-00bacb34)
- ブロック [`00bacb34`](#insn-00bacb34) 範囲 `[['00bacb34', '00bacb53']]`
  - `CONDITIONAL_JUMP` [`00bacb50`](#insn-00bacb50) → [`00bacb64`](#insn-00bacb64)
  - `FALL_THROUGH` [`00bacb50`](#insn-00bacb50) → [`00bacb54`](#insn-00bacb54)
- ブロック [`00bacb54`](#insn-00bacb54) 範囲 `[['00bacb54', '00bacb57']]`
  - `CONDITIONAL_JUMP` [`00bacb54`](#insn-00bacb54) → [`00bacb6c`](#insn-00bacb6c)
  - `FALL_THROUGH` [`00bacb54`](#insn-00bacb54) → [`00bacb58`](#insn-00bacb58)
- ブロック [`00bacb58`](#insn-00bacb58) 範囲 `[['00bacb58', '00bacb5b']]`
  - `UNCONDITIONAL_JUMP` [`00bacb58`](#insn-00bacb58) → [`00bacc8c`](#insn-00bacc8c)
- ブロック [`00bacb5c`](#insn-00bacb5c) 範囲 `[['00bacb5c', '00bacb5f']]`
  - `CONDITIONAL_JUMP` [`00bacb5c`](#insn-00bacb5c) → [`00bacb6c`](#insn-00bacb6c)
  - `FALL_THROUGH` [`00bacb5c`](#insn-00bacb5c) → [`00bacb60`](#insn-00bacb60)
- ブロック [`00bacb60`](#insn-00bacb60) 範囲 `[['00bacb60', '00bacb63']]`
  - `UNCONDITIONAL_JUMP` [`00bacb60`](#insn-00bacb60) → [`00bacc8c`](#insn-00bacc8c)
- ブロック [`00bacb64`](#insn-00bacb64) 範囲 `[['00bacb64', '00bacb6b']]`
  - `CONDITIONAL_JUMP` [`00bacb68`](#insn-00bacb68) → [`00bacc8c`](#insn-00bacc8c)
  - `FALL_THROUGH` [`00bacb68`](#insn-00bacb68) → [`00bacb6c`](#insn-00bacb6c)
- ブロック [`00bacb6c`](#insn-00bacb6c) 範囲 `[['00bacb6c', '00bacb7f']]`
  - `FALL_THROUGH` [`00bacb7c`](#insn-00bacb7c) → [`00bacb80`](#insn-00bacb80)
- ブロック [`00bacb80`](#insn-00bacb80) 範囲 `[['00bacb80', '00bacb83']]`
  - `FALL_THROUGH` [`00bacb80`](#insn-00bacb80) → [`00bacb84`](#insn-00bacb84)
- ブロック [`00bacb84`](#insn-00bacb84) 範囲 `[['00bacb84', '00bacb8f']]`
  - `CONDITIONAL_JUMP` [`00bacb8c`](#insn-00bacb8c) → [`00bacbec`](#insn-00bacbec)
  - `FALL_THROUGH` [`00bacb8c`](#insn-00bacb8c) → [`00bacb90`](#insn-00bacb90)
- ブロック [`00bacb90`](#insn-00bacb90) 範囲 `[['00bacb90', '00bacb93']]`
  - `FALL_THROUGH` [`00bacb90`](#insn-00bacb90) → [`00bacb94`](#insn-00bacb94)
- ブロック [`00bacb94`](#insn-00bacb94) 範囲 `[['00bacb94', '00bacb97']]`
  - `FALL_THROUGH` [`00bacb94`](#insn-00bacb94) → [`00bacb98`](#insn-00bacb98)
- ブロック [`00bacb98`](#insn-00bacb98) 範囲 `[['00bacb98', '00bacba7']]`
  - `FALL_THROUGH` [`00bacba4`](#insn-00bacba4) → [`00bacba8`](#insn-00bacba8)
- ブロック [`00bacba8`](#insn-00bacba8) 範囲 `[['00bacba8', '00bacbab']]`
  - `FALL_THROUGH` [`00bacba8`](#insn-00bacba8) → [`00bacbac`](#insn-00bacbac)
- ブロック [`00bacbac`](#insn-00bacbac) 範囲 `[['00bacbac', '00bacbbb']]`
  - `FALL_THROUGH` [`00bacbb8`](#insn-00bacbb8) → [`00bacbbc`](#insn-00bacbbc)
- ブロック [`00bacbbc`](#insn-00bacbbc) 範囲 `[['00bacbbc', '00bacbbf']]`
  - `FALL_THROUGH` [`00bacbbc`](#insn-00bacbbc) → [`00bacbc0`](#insn-00bacbc0)
- ブロック [`00bacbc0`](#insn-00bacbc0) 範囲 `[['00bacbc0', '00bacbc3']]`
  - `CONDITIONAL_JUMP` [`00bacbc0`](#insn-00bacbc0) → [`00bacbf4`](#insn-00bacbf4)
  - `FALL_THROUGH` [`00bacbc0`](#insn-00bacbc0) → [`00bacbc4`](#insn-00bacbc4)
- ブロック [`00bacbc4`](#insn-00bacbc4) 範囲 `[['00bacbc4', '00bacbcf']]`
  - `FALL_THROUGH` [`00bacbcc`](#insn-00bacbcc) → [`00bacbd0`](#insn-00bacbd0)
- ブロック [`00bacbd0`](#insn-00bacbd0) 範囲 `[['00bacbd0', '00bacbd3']]`
  - `FALL_THROUGH` [`00bacbd0`](#insn-00bacbd0) → [`00bacbd4`](#insn-00bacbd4)
- ブロック [`00bacbd4`](#insn-00bacbd4) 範囲 `[['00bacbd4', '00bacbe3']]`
  - `CONDITIONAL_JUMP` [`00bacbe0`](#insn-00bacbe0) → [`00bacbf4`](#insn-00bacbf4)
  - `FALL_THROUGH` [`00bacbe0`](#insn-00bacbe0) → [`00bacbe4`](#insn-00bacbe4)
- ブロック [`00bacbe4`](#insn-00bacbe4) 範囲 `[['00bacbe4', '00bacbe7']]`
  - `CONDITIONAL_JUMP` [`00bacbe4`](#insn-00bacbe4) → [`00bacbfc`](#insn-00bacbfc)
  - `FALL_THROUGH` [`00bacbe4`](#insn-00bacbe4) → [`00bacbe8`](#insn-00bacbe8)
- ブロック [`00bacbe8`](#insn-00bacbe8) 範囲 `[['00bacbe8', '00bacbeb']]`
  - `UNCONDITIONAL_JUMP` [`00bacbe8`](#insn-00bacbe8) → [`00bacc8c`](#insn-00bacc8c)
- ブロック [`00bacbec`](#insn-00bacbec) 範囲 `[['00bacbec', '00bacbef']]`
  - `CONDITIONAL_JUMP` [`00bacbec`](#insn-00bacbec) → [`00bacbfc`](#insn-00bacbfc)
  - `FALL_THROUGH` [`00bacbec`](#insn-00bacbec) → [`00bacbf0`](#insn-00bacbf0)
- ブロック [`00bacbf0`](#insn-00bacbf0) 範囲 `[['00bacbf0', '00bacbf3']]`
  - `UNCONDITIONAL_JUMP` [`00bacbf0`](#insn-00bacbf0) → [`00bacc8c`](#insn-00bacc8c)
- ブロック [`00bacbf4`](#insn-00bacbf4) 範囲 `[['00bacbf4', '00bacbf7']]`
  - `FALL_THROUGH` [`00bacbf4`](#insn-00bacbf4) → [`00bacbf8`](#insn-00bacbf8)
- ブロック [`00bacbf8`](#insn-00bacbf8) 範囲 `[['00bacbf8', '00bacbfb']]`
  - `CONDITIONAL_JUMP` [`00bacbf8`](#insn-00bacbf8) → [`00bacc8c`](#insn-00bacc8c)
  - `FALL_THROUGH` [`00bacbf8`](#insn-00bacbf8) → [`00bacbfc`](#insn-00bacbfc)
- ブロック [`00bacbfc`](#insn-00bacbfc) 範囲 `[['00bacbfc', '00bacc0b']]`
  - `FALL_THROUGH` [`00bacc08`](#insn-00bacc08) → [`00bacc0c`](#insn-00bacc0c)
- ブロック [`00bacc0c`](#insn-00bacc0c) 範囲 `[['00bacc0c', '00bacc0f']]`
  - `FALL_THROUGH` [`00bacc0c`](#insn-00bacc0c) → [`00bacc10`](#insn-00bacc10)
- ブロック [`00bacc10`](#insn-00bacc10) 範囲 `[['00bacc10', '00bacc1f']]`
  - `CONDITIONAL_JUMP` [`00bacc1c`](#insn-00bacc1c) → [`00bacc7c`](#insn-00bacc7c)
  - `FALL_THROUGH` [`00bacc1c`](#insn-00bacc1c) → [`00bacc20`](#insn-00bacc20)
- ブロック [`00bacc20`](#insn-00bacc20) 範囲 `[['00bacc20', '00bacc53']]`
  - `CONDITIONAL_JUMP` [`00bacc50`](#insn-00bacc50) → [`00baccb0`](#insn-00baccb0)
  - `FALL_THROUGH` [`00bacc50`](#insn-00bacc50) → [`00bacc54`](#insn-00bacc54)
- ブロック [`00bacc54`](#insn-00bacc54) 範囲 `[['00bacc54', '00bacc6b']]`
  - `FALL_THROUGH` [`00bacc68`](#insn-00bacc68) → [`00bacc6c`](#insn-00bacc6c)
- ブロック [`00bacc6c`](#insn-00bacc6c) 範囲 `[['00bacc6c', '00bacc73']]`
  - `CONDITIONAL_JUMP` [`00bacc70`](#insn-00bacc70) → [`00baccb0`](#insn-00baccb0)
  - `FALL_THROUGH` [`00bacc70`](#insn-00bacc70) → [`00bacc74`](#insn-00bacc74)
- ブロック [`00bacc74`](#insn-00bacc74) 範囲 `[['00bacc74', '00bacc77']]`
  - `CONDITIONAL_JUMP` [`00bacc74`](#insn-00bacc74) → [`00bacc80`](#insn-00bacc80)
  - `FALL_THROUGH` [`00bacc74`](#insn-00bacc74) → [`00bacc78`](#insn-00bacc78)
- ブロック [`00bacc78`](#insn-00bacc78) 範囲 `[['00bacc78', '00bacc7b']]`
  - `UNCONDITIONAL_JUMP` [`00bacc78`](#insn-00bacc78) → [`00bacc8c`](#insn-00bacc8c)
- ブロック [`00bacc7c`](#insn-00bacc7c) 範囲 `[['00bacc7c', '00bacc7f']]`
  - `CONDITIONAL_JUMP` [`00bacc7c`](#insn-00bacc7c) → [`00bacc8c`](#insn-00bacc8c)
  - `FALL_THROUGH` [`00bacc7c`](#insn-00bacc7c) → [`00bacc80`](#insn-00bacc80)
- ブロック [`00bacc80`](#insn-00bacc80) 範囲 `[['00bacc80', '00bacc8b']]`
  - `FALL_THROUGH` [`00bacc88`](#insn-00bacc88) → [`00bacc8c`](#insn-00bacc8c)
- ブロック [`00bacc8c`](#insn-00bacc8c) 範囲 `[['00bacc8c', '00bacca3']]`
  - `FALL_THROUGH` [`00bacca0`](#insn-00bacca0) → [`00bacca4`](#insn-00bacca4)
- ブロック [`00bacca4`](#insn-00bacca4) 範囲 `[['00bacca4', '00bacca7']]`
  - `FALL_THROUGH` [`00bacca4`](#insn-00bacca4) → [`00bacca8`](#insn-00bacca8)
- ブロック [`00bacca8`](#insn-00bacca8) 範囲 `[['00bacca8', '00baccaf']]`
- ブロック [`00baccb0`](#insn-00baccb0) 範囲 `[['00baccb0', '00baccb7']]`
  - `CONDITIONAL_JUMP` [`00baccb4`](#insn-00baccb4) → [`00bacc80`](#insn-00bacc80)
  - `FALL_THROUGH` [`00baccb4`](#insn-00baccb4) → [`00baccb8`](#insn-00baccb8)
- ブロック [`00baccb8`](#insn-00baccb8) 範囲 `[['00baccb8', '00baccbb']]`
  - `UNCONDITIONAL_JUMP` [`00baccb8`](#insn-00baccb8) → [`00bacc8c`](#insn-00bacc8c)

## 命令位置別の参照

- [`00bac9e0`](#insn-00bac9e0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac9e4`](#insn-00bac9e4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac9e8`](#insn-00bac9e8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac9ec`](#insn-00bac9ec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac9f0`](#insn-00bac9f0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac9f4`](#insn-00bac9f4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baca10`](#insn-00baca10) → [`00bac7d4`](00bac7d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bac7d4` · 推定シンボル `None` · 推定型 `None`
- [`00baca30`](#insn-00baca30) → [`00bacab8`](#insn-00bacab8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baca4c`](#insn-00baca4c) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baca78`](#insn-00baca78) → [`00bacac0`](#insn-00bacac0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baca94`](#insn-00baca94) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00baca98`](#insn-00baca98) → [`00bacac0`](#insn-00bacac0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacaac`](#insn-00bacaac) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacab0`](#insn-00bacab0) → [`00bacadc`](#insn-00bacadc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacab4`](#insn-00bacab4) → [`00bacc8c`](#insn-00bacc8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacab8`](#insn-00bacab8) → [`00bacadc`](#insn-00bacadc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacabc`](#insn-00bacabc) → [`00bacc8c`](#insn-00bacc8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacad4`](#insn-00bacad4) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacad8`](#insn-00bacad8) → [`00bacc8c`](#insn-00bacc8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacafc`](#insn-00bacafc) → [`00bacb5c`](#insn-00bacb5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb30`](#insn-00bacb30) → [`00bacb64`](#insn-00bacb64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb4c`](#insn-00bacb4c) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bacb50`](#insn-00bacb50) → [`00bacb64`](#insn-00bacb64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb54`](#insn-00bacb54) → [`00bacb6c`](#insn-00bacb6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb58`](#insn-00bacb58) → [`00bacc8c`](#insn-00bacc8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb5c`](#insn-00bacb5c) → [`00bacb6c`](#insn-00bacb6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb60`](#insn-00bacb60) → [`00bacc8c`](#insn-00bacc8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb68`](#insn-00bacb68) → [`00bacc8c`](#insn-00bacc8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb8c`](#insn-00bacb8c) → [`00bacbec`](#insn-00bacbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacbc0`](#insn-00bacbc0) → [`00bacbf4`](#insn-00bacbf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacbdc`](#insn-00bacbdc) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bacbe0`](#insn-00bacbe0) → [`00bacbf4`](#insn-00bacbf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacbe4`](#insn-00bacbe4) → [`00bacbfc`](#insn-00bacbfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacbe8`](#insn-00bacbe8) → [`00bacc8c`](#insn-00bacc8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacbec`](#insn-00bacbec) → [`00bacbfc`](#insn-00bacbfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacbf0`](#insn-00bacbf0) → [`00bacc8c`](#insn-00bacc8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacbf8`](#insn-00bacbf8) → [`00bacc8c`](#insn-00bacc8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc1c`](#insn-00bacc1c) → [`00bacc7c`](#insn-00bacc7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc50`](#insn-00bacc50) → [`00baccb0`](#insn-00baccb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc6c`](#insn-00bacc6c) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bacc70`](#insn-00bacc70) → [`00baccb0`](#insn-00baccb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc74`](#insn-00bacc74) → [`00bacc80`](#insn-00bacc80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc78`](#insn-00bacc78) → [`00bacc8c`](#insn-00bacc8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc7c`](#insn-00bacc7c) → [`00bacc8c`](#insn-00bacc8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc90`](#insn-00bacc90) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc94`](#insn-00bacc94) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc98`](#insn-00bacc98) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc9c`](#insn-00bacc9c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacca0`](#insn-00bacca0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacca4`](#insn-00bacca4) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baccb4`](#insn-00baccb4) → [`00bacc80`](#insn-00bacc80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baccb8`](#insn-00baccb8) → [`00bacc8c`](#insn-00bacc8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bac9e0`](#insn-00bac9e0)

~~~json
{
  "source": "00bac9e0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac9e4`](#insn-00bac9e4)

~~~json
{
  "source": "00bac9e4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac9e8`](#insn-00bac9e8)

~~~json
{
  "source": "00bac9e8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac9ec`](#insn-00bac9ec)

~~~json
{
  "source": "00bac9ec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac9f0`](#insn-00bac9f0)

~~~json
{
  "source": "00bac9f0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac9f4`](#insn-00bac9f4)

~~~json
{
  "source": "00bac9f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baca10`](#insn-00baca10)

~~~json
{
  "source": "00baca10",
  "target": "00bac7d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baca30`](#insn-00baca30)

~~~json
{
  "source": "00baca30",
  "target": "00bacab8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baca4c`](#insn-00baca4c)

~~~json
{
  "source": "00baca4c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baca78`](#insn-00baca78)

~~~json
{
  "source": "00baca78",
  "target": "00bacac0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baca94`](#insn-00baca94)

~~~json
{
  "source": "00baca94",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baca98`](#insn-00baca98)

~~~json
{
  "source": "00baca98",
  "target": "00bacac0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacaac`](#insn-00bacaac)

~~~json
{
  "source": "00bacaac",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacab0`](#insn-00bacab0)

~~~json
{
  "source": "00bacab0",
  "target": "00bacadc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacab4`](#insn-00bacab4)

~~~json
{
  "source": "00bacab4",
  "target": "00bacc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacab8`](#insn-00bacab8)

~~~json
{
  "source": "00bacab8",
  "target": "00bacadc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacabc`](#insn-00bacabc)

~~~json
{
  "source": "00bacabc",
  "target": "00bacc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacad4`](#insn-00bacad4)

~~~json
{
  "source": "00bacad4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacad8`](#insn-00bacad8)

~~~json
{
  "source": "00bacad8",
  "target": "00bacc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacafc`](#insn-00bacafc)

~~~json
{
  "source": "00bacafc",
  "target": "00bacb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb30`](#insn-00bacb30)

~~~json
{
  "source": "00bacb30",
  "target": "00bacb64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb4c`](#insn-00bacb4c)

~~~json
{
  "source": "00bacb4c",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bacb50`](#insn-00bacb50)

~~~json
{
  "source": "00bacb50",
  "target": "00bacb64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb54`](#insn-00bacb54)

~~~json
{
  "source": "00bacb54",
  "target": "00bacb6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb58`](#insn-00bacb58)

~~~json
{
  "source": "00bacb58",
  "target": "00bacc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb5c`](#insn-00bacb5c)

~~~json
{
  "source": "00bacb5c",
  "target": "00bacb6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb60`](#insn-00bacb60)

~~~json
{
  "source": "00bacb60",
  "target": "00bacc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb68`](#insn-00bacb68)

~~~json
{
  "source": "00bacb68",
  "target": "00bacc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb8c`](#insn-00bacb8c)

~~~json
{
  "source": "00bacb8c",
  "target": "00bacbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacbc0`](#insn-00bacbc0)

~~~json
{
  "source": "00bacbc0",
  "target": "00bacbf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacbdc`](#insn-00bacbdc)

~~~json
{
  "source": "00bacbdc",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bacbe0`](#insn-00bacbe0)

~~~json
{
  "source": "00bacbe0",
  "target": "00bacbf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacbe4`](#insn-00bacbe4)

~~~json
{
  "source": "00bacbe4",
  "target": "00bacbfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacbe8`](#insn-00bacbe8)

~~~json
{
  "source": "00bacbe8",
  "target": "00bacc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacbec`](#insn-00bacbec)

~~~json
{
  "source": "00bacbec",
  "target": "00bacbfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacbf0`](#insn-00bacbf0)

~~~json
{
  "source": "00bacbf0",
  "target": "00bacc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacbf8`](#insn-00bacbf8)

~~~json
{
  "source": "00bacbf8",
  "target": "00bacc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc1c`](#insn-00bacc1c)

~~~json
{
  "source": "00bacc1c",
  "target": "00bacc7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc50`](#insn-00bacc50)

~~~json
{
  "source": "00bacc50",
  "target": "00baccb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc6c`](#insn-00bacc6c)

~~~json
{
  "source": "00bacc6c",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bacc70`](#insn-00bacc70)

~~~json
{
  "source": "00bacc70",
  "target": "00baccb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc74`](#insn-00bacc74)

~~~json
{
  "source": "00bacc74",
  "target": "00bacc80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc78`](#insn-00bacc78)

~~~json
{
  "source": "00bacc78",
  "target": "00bacc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc7c`](#insn-00bacc7c)

~~~json
{
  "source": "00bacc7c",
  "target": "00bacc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc90`](#insn-00bacc90)

~~~json
{
  "source": "00bacc90",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc94`](#insn-00bacc94)

~~~json
{
  "source": "00bacc94",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc98`](#insn-00bacc98)

~~~json
{
  "source": "00bacc98",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc9c`](#insn-00bacc9c)

~~~json
{
  "source": "00bacc9c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacca0`](#insn-00bacca0)

~~~json
{
  "source": "00bacca0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacca4`](#insn-00bacca4)

~~~json
{
  "source": "00bacca4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baccb4`](#insn-00baccb4)

~~~json
{
  "source": "00baccb4",
  "target": "00bacc80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baccb8`](#insn-00baccb8)

~~~json
{
  "source": "00baccb8",
  "target": "00bacc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
