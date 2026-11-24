# 00bacbfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bac7d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bac/00bac7d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0009.md#compare-9c3bc351ced885b3ed079a351f65bd8f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0043.md#review-65c4feb51470cdea8ddd777d79451d9b)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bacbfc",
  "name": "FUN_00bacbfc",
  "size": 520,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a340bc3814cac81fbd5d648a5966233b6841c944a993b86d33104265c44dcf71",
  "source_text_sha256": "a340bc3814cac81fbd5d648a5966233b6841c944a993b86d33104265c44dcf71",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bacbfc",
        "00bace03"
      ]
    ],
    "bytes_sha256": "5f8c751a8f1368e82a2799120cb0f564be713211ff3cb44d641aa9ae77181cb0",
    "instruction_count": 130,
    "instruction_bytes": 520,
    "body_bytes": 520,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00babf9c](../00bab/00babf9c.md)
- [00bace04](../00bac/00bace04.md)
- [00bad0e4](../00bad/00bad0e4.md)

## 呼び出し先

- [00bac950](../00bac/00bac950.md)
- [00c58050](../00c58/00c58050.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5695 bytes

~~~c

int FUN_00bacbfc(undefined8 *param_1,undefined8 *param_2,undefined8 *param_3,undefined8 *param_4)

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
  
                    /* try { // try from 00bacc14 to 00cacc1f has its CatchHandler @ 00bacda4 */
  iVar6 = FUN_00bac950();
  pbVar11 = (byte *)*param_4;
  pbVar12 = (byte *)*param_3;
                    /* try { // try from 00bacc40 to 00cacc4b has its CatchHandler @ 00bacd94 */
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
    bVar4 = *pbVar12;
    bVar5 = *pbVar11;
                    /* try { // try from 00bacc64 to 00cacc6f has its CatchHandler @ 00bacd90 */
    uVar1 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar12 + 8);
    }
    uVar2 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar11 + 8);
    }
    sVar3 = uVar1;
                    /* try { // try from 00bacc78 to 00cacc7f has its CatchHandler @ 00bace68 */
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
                    /* try { // try from 00bacc9c to 00cacca7 has its CatchHandler @ 00bacd80 */
      if (iVar7 != 0) {
        if (-1 < iVar7) {
          return iVar6;
        }
        goto LAB_00baccb8;
      }
    }
    if (uVar1 <= uVar2) {
      return iVar6;
    }
  }
  else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
    return iVar6;
  }
LAB_00baccb8:
  *param_3 = pbVar11;
                    /* try { // try from 00baccbc to 00caccc7 has its CatchHandler @ 00bacd7c */
  *param_4 = pbVar12;
  pbVar11 = (byte *)*param_3;
  pbVar12 = (byte *)*param_2;
                    /* try { // try from 00baccc8 to 00cacce3 has its CatchHandler @ 00bace1c */
  iVar7 = iVar6 + 1;
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
    bVar4 = *pbVar12;
                    /* try { // try from 00bacce4 to 00cacd53 has its CatchHandler @ 00bacea0 */
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
        goto LAB_00bacd48;
      }
    }
    if (uVar1 <= uVar2) {
      return iVar7;
    }
  }
  else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
    return iVar7;
  }
LAB_00bacd48:
  *param_2 = pbVar11;
  *param_3 = pbVar12;
  pbVar11 = (byte *)*param_2;
                    /* try { // try from 00bacd54 to 00cacea3 has its CatchHandler @ 00bac9f4 */
  pbVar12 = (byte *)*param_1;
  iVar7 = iVar6 + 2;
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
    bVar4 = *pbVar12;
    bVar5 = *pbVar11;
                    /* catch() { ... } // from try @ 00baccbc with catch @ 00bacd7c */
                    /* catch() { ... } // from try @ 00bacc9c with catch @ 00bacd80 */
    uVar1 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar12 + 8);
    }
    uVar2 = (ulong)(bVar5 >> 1);
                    /* catch() { ... } // from try @ 00bacc64 with catch @ 00bacd90 */
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar11 + 8);
    }
                    /* catch() { ... } // from try @ 00bacc40 with catch @ 00bacd94 */
    sVar3 = uVar1;
    if (uVar2 <= uVar1) {
      sVar3 = uVar2;
    }
    if (sVar3 != 0) {
      pbVar9 = *(byte **)(pbVar11 + 0x10);
                    /* catch() { ... } // from try @ 00bacc14 with catch @ 00bacda4 */
      pbVar10 = *(byte **)(pbVar12 + 0x10);
                    /* catch() { ... } // from try @ 00bacbf4 with catch @ 00bacda8 */
      if ((bVar5 & 1) == 0) {
        pbVar9 = pbVar11 + 1;
      }
      if ((bVar4 & 1) == 0) {
        pbVar10 = pbVar12 + 1;
      }
                    /* catch() { ... } // from try @ 00bacba8 with catch @ 00bacdb8 */
      iVar8 = memcmp(pbVar9,pbVar10,sVar3);
                    /* catch() { ... } // from try @ 00bacb84 with catch @ 00bacdbc */
      if (iVar8 != 0) {
        if (-1 < iVar8) {
          return iVar7;
        }
        goto LAB_00bacdcc;
      }
    }
                    /* catch() { ... } // from try @ 00baca94 with catch @ 00bacdf8 */
    if (uVar1 <= uVar2) {
      return iVar7;
    }
  }
  else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
    return iVar7;
  }
LAB_00bacdcc:
                    /* catch() { ... } // from try @ 00bacb58 with catch @ 00bacdcc */
                    /* catch() { ... } // from try @ 00bacb38 with catch @ 00bacdd0 */
  *param_1 = pbVar11;
  *param_2 = pbVar12;
                    /* catch() { ... } // from try @ 00bacb04 with catch @ 00bacde0 */
                    /* catch() { ... } // from try @ 00bacae0 with catch @ 00bacde4 */
                    /* catch() { ... } // from try @ 00bacab4 with catch @ 00bacdf4 */
  return iVar6 + 3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bacbfc"></a> `00bacbfc` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00bacc00"></a> `00bacc00` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bacc04"></a> `00bacc04` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bacc08"></a> `00bacc08` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bacc0c"></a> `00bacc0c` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bacc10"></a> `00bacc10` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bacc14"></a> `00bacc14` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bacc18"></a> `00bacc18` | `f8 03 03 aa` | mov x24,x3 | `FALL_THROUGH`
<a id="insn-00bacc1c"></a> `00bacc1c` | `f7 03 02 aa` | mov x23,x2 | `FALL_THROUGH`
<a id="insn-00bacc20"></a> `00bacc20` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bacc24"></a> `00bacc24` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bacc28"></a> `00bacc28` | `4a ff ff 97` | bl 0x00bac950 | `UNCONDITIONAL_CALL`
<a id="insn-00bacc2c"></a> `00bacc2c` | `19 03 40 f9` | ldr x25,[x24] | `FALL_THROUGH`
<a id="insn-00bacc30"></a> `00bacc30` | `fa 02 40 f9` | ldr x26,[x23] | `FALL_THROUGH`
<a id="insn-00bacc34"></a> `00bacc34` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00bacc38"></a> `00bacc38` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00bacc3c"></a> `00bacc3c` | `28 43 40 f9` | ldr x8,[x25, #0x80] | `FALL_THROUGH`
<a id="insn-00bacc40"></a> `00bacc40` | `49 43 40 f9` | ldr x9,[x26, #0x80] | `FALL_THROUGH`
<a id="insn-00bacc44"></a> `00bacc44` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bacc48"></a> `00bacc48` | `01 03 00 54` | b.ne 0x00bacca8 | `CONDITIONAL_JUMP`
<a id="insn-00bacc4c"></a> `00bacc4c` | `48 03 40 39` | ldrb w8,[x26] | `FALL_THROUGH`
<a id="insn-00bacc50"></a> `00bacc50` | `4a 07 40 f9` | ldr x10,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00bacc54"></a> `00bacc54` | `29 03 40 39` | ldrb w9,[x25] | `FALL_THROUGH`
<a id="insn-00bacc58"></a> `00bacc58` | `2b 07 40 f9` | ldr x11,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00bacc5c"></a> `00bacc5c` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacc60"></a> `00bacc60` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacc64"></a> `00bacc64` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacc68"></a> `00bacc68` | `9b 01 8a 9a` | csel x27,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bacc6c"></a> `00bacc6c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacc70"></a> `00bacc70` | `bc 01 8b 9a` | csel x28,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bacc74"></a> `00bacc74` | `7f 03 1c eb` | cmp x27,x28 | `FALL_THROUGH`
<a id="insn-00bacc78"></a> `00bacc78` | `62 33 9c 9a` | csel x2,x27,x28,cc | `FALL_THROUGH`
<a id="insn-00bacc7c"></a> `00bacc7c` | `a2 01 00 b4` | cbz x2,0x00baccb0 | `CONDITIONAL_JUMP`
<a id="insn-00bacc80"></a> `00bacc80` | `2a 0b 40 f9` | ldr x10,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00bacc84"></a> `00bacc84` | `4b 0b 40 f9` | ldr x11,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00bacc88"></a> `00bacc88` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacc8c"></a> `00bacc8c` | `40 15 99 9a` | csinc x0,x10,x25,ne | `FALL_THROUGH`
<a id="insn-00bacc90"></a> `00bacc90` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacc94"></a> `00bacc94` | `61 15 9a 9a` | csinc x1,x11,x26,ne | `FALL_THROUGH`
<a id="insn-00bacc98"></a> `00bacc98` | `ee ac 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00bacc9c"></a> `00bacc9c` | `a0 00 00 34` | cbz w0,0x00baccb0 | `CONDITIONAL_JUMP`
<a id="insn-00bacca0"></a> `00bacca0` | `c0 00 f8 37` | tbnz w0,#0x1f,0x00baccb8 | `CONDITIONAL_JUMP`
<a id="insn-00bacca4"></a> `00bacca4` | `4d 00 00 14` | b 0x00bacdd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacca8"></a> `00bacca8` | `83 00 00 54` | b.cc 0x00baccb8 | `CONDITIONAL_JUMP`
<a id="insn-00baccac"></a> `00baccac` | `4b 00 00 14` | b 0x00bacdd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00baccb0"></a> `00baccb0` | `9f 03 1b eb` | cmp x28,x27 | `FALL_THROUGH`
<a id="insn-00baccb4"></a> `00baccb4` | `22 09 00 54` | b.cs 0x00bacdd8 | `CONDITIONAL_JUMP`
<a id="insn-00baccb8"></a> `00baccb8` | `f9 02 00 f9` | str x25,[x23] | `FALL_THROUGH`
<a id="insn-00baccbc"></a> `00baccbc` | `1a 03 00 f9` | str x26,[x24] | `FALL_THROUGH`
<a id="insn-00baccc0"></a> `00baccc0` | `f8 02 40 f9` | ldr x24,[x23] | `FALL_THROUGH`
<a id="insn-00baccc4"></a> `00baccc4` | `79 02 40 f9` | ldr x25,[x19] | `FALL_THROUGH`
<a id="insn-00baccc8"></a> `00baccc8` | `b6 06 00 11` | add w22,w21,#0x1 | `FALL_THROUGH`
<a id="insn-00bacccc"></a> `00bacccc` | `08 43 40 f9` | ldr x8,[x24, #0x80] | `FALL_THROUGH`
<a id="insn-00baccd0"></a> `00baccd0` | `29 43 40 f9` | ldr x9,[x25, #0x80] | `FALL_THROUGH`
<a id="insn-00baccd4"></a> `00baccd4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00baccd8"></a> `00baccd8` | `01 03 00 54` | b.ne 0x00bacd38 | `CONDITIONAL_JUMP`
<a id="insn-00baccdc"></a> `00baccdc` | `28 03 40 39` | ldrb w8,[x25] | `FALL_THROUGH`
<a id="insn-00bacce0"></a> `00bacce0` | `2a 07 40 f9` | ldr x10,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00bacce4"></a> `00bacce4` | `09 03 40 39` | ldrb w9,[x24] | `FALL_THROUGH`
<a id="insn-00bacce8"></a> `00bacce8` | `0b 07 40 f9` | ldr x11,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00baccec"></a> `00baccec` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00baccf0"></a> `00baccf0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baccf4"></a> `00baccf4` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00baccf8"></a> `00baccf8` | `9a 01 8a 9a` | csel x26,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00baccfc"></a> `00baccfc` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacd00"></a> `00bacd00` | `bb 01 8b 9a` | csel x27,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bacd04"></a> `00bacd04` | `5f 03 1b eb` | cmp x26,x27 | `FALL_THROUGH`
<a id="insn-00bacd08"></a> `00bacd08` | `42 33 9b 9a` | csel x2,x26,x27,cc | `FALL_THROUGH`
<a id="insn-00bacd0c"></a> `00bacd0c` | `a2 01 00 b4` | cbz x2,0x00bacd40 | `CONDITIONAL_JUMP`
<a id="insn-00bacd10"></a> `00bacd10` | `0a 0b 40 f9` | ldr x10,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bacd14"></a> `00bacd14` | `2b 0b 40 f9` | ldr x11,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00bacd18"></a> `00bacd18` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacd1c"></a> `00bacd1c` | `40 15 98 9a` | csinc x0,x10,x24,ne | `FALL_THROUGH`
<a id="insn-00bacd20"></a> `00bacd20` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacd24"></a> `00bacd24` | `61 15 99 9a` | csinc x1,x11,x25,ne | `FALL_THROUGH`
<a id="insn-00bacd28"></a> `00bacd28` | `ca ac 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00bacd2c"></a> `00bacd2c` | `a0 00 00 34` | cbz w0,0x00bacd40 | `CONDITIONAL_JUMP`
<a id="insn-00bacd30"></a> `00bacd30` | `c0 00 f8 37` | tbnz w0,#0x1f,0x00bacd48 | `CONDITIONAL_JUMP`
<a id="insn-00bacd34"></a> `00bacd34` | `29 00 00 14` | b 0x00bacdd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacd38"></a> `00bacd38` | `83 00 00 54` | b.cc 0x00bacd48 | `CONDITIONAL_JUMP`
<a id="insn-00bacd3c"></a> `00bacd3c` | `27 00 00 14` | b 0x00bacdd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacd40"></a> `00bacd40` | `7f 03 1a eb` | cmp x27,x26 | `FALL_THROUGH`
<a id="insn-00bacd44"></a> `00bacd44` | `a2 04 00 54` | b.cs 0x00bacdd8 | `CONDITIONAL_JUMP`
<a id="insn-00bacd48"></a> `00bacd48` | `78 02 00 f9` | str x24,[x19] | `FALL_THROUGH`
<a id="insn-00bacd4c"></a> `00bacd4c` | `f9 02 00 f9` | str x25,[x23] | `FALL_THROUGH`
<a id="insn-00bacd50"></a> `00bacd50` | `77 02 40 f9` | ldr x23,[x19] | `FALL_THROUGH`
<a id="insn-00bacd54"></a> `00bacd54` | `98 02 40 f9` | ldr x24,[x20] | `FALL_THROUGH`
<a id="insn-00bacd58"></a> `00bacd58` | `b6 0a 00 11` | add w22,w21,#0x2 | `FALL_THROUGH`
<a id="insn-00bacd5c"></a> `00bacd5c` | `e8 42 40 f9` | ldr x8,[x23, #0x80] | `FALL_THROUGH`
<a id="insn-00bacd60"></a> `00bacd60` | `09 43 40 f9` | ldr x9,[x24, #0x80] | `FALL_THROUGH`
<a id="insn-00bacd64"></a> `00bacd64` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bacd68"></a> `00bacd68` | `01 03 00 54` | b.ne 0x00bacdc8 | `CONDITIONAL_JUMP`
<a id="insn-00bacd6c"></a> `00bacd6c` | `08 03 40 39` | ldrb w8,[x24] | `FALL_THROUGH`
<a id="insn-00bacd70"></a> `00bacd70` | `0a 07 40 f9` | ldr x10,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00bacd74"></a> `00bacd74` | `e9 02 40 39` | ldrb w9,[x23] | `FALL_THROUGH`
<a id="insn-00bacd78"></a> `00bacd78` | `eb 06 40 f9` | ldr x11,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bacd7c"></a> `00bacd7c` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacd80"></a> `00bacd80` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacd84"></a> `00bacd84` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacd88"></a> `00bacd88` | `99 01 8a 9a` | csel x25,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bacd8c"></a> `00bacd8c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacd90"></a> `00bacd90` | `ba 01 8b 9a` | csel x26,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bacd94"></a> `00bacd94` | `3f 03 1a eb` | cmp x25,x26 | `FALL_THROUGH`
<a id="insn-00bacd98"></a> `00bacd98` | `22 33 9a 9a` | csel x2,x25,x26,cc | `FALL_THROUGH`
<a id="insn-00bacd9c"></a> `00bacd9c` | `e2 02 00 b4` | cbz x2,0x00bacdf8 | `CONDITIONAL_JUMP`
<a id="insn-00bacda0"></a> `00bacda0` | `ea 0a 40 f9` | ldr x10,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00bacda4"></a> `00bacda4` | `0b 0b 40 f9` | ldr x11,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bacda8"></a> `00bacda8` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacdac"></a> `00bacdac` | `40 15 97 9a` | csinc x0,x10,x23,ne | `FALL_THROUGH`
<a id="insn-00bacdb0"></a> `00bacdb0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacdb4"></a> `00bacdb4` | `61 15 98 9a` | csinc x1,x11,x24,ne | `FALL_THROUGH`
<a id="insn-00bacdb8"></a> `00bacdb8` | `a6 ac 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00bacdbc"></a> `00bacdbc` | `e0 01 00 34` | cbz w0,0x00bacdf8 | `CONDITIONAL_JUMP`
<a id="insn-00bacdc0"></a> `00bacdc0` | `60 00 f8 37` | tbnz w0,#0x1f,0x00bacdcc | `CONDITIONAL_JUMP`
<a id="insn-00bacdc4"></a> `00bacdc4` | `05 00 00 14` | b 0x00bacdd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacdc8"></a> `00bacdc8` | `82 00 00 54` | b.cs 0x00bacdd8 | `CONDITIONAL_JUMP`
<a id="insn-00bacdcc"></a> `00bacdcc` | `b6 0e 00 11` | add w22,w21,#0x3 | `FALL_THROUGH`
<a id="insn-00bacdd0"></a> `00bacdd0` | `97 02 00 f9` | str x23,[x20] | `FALL_THROUGH`
<a id="insn-00bacdd4"></a> `00bacdd4` | `78 02 00 f9` | str x24,[x19] | `FALL_THROUGH`
<a id="insn-00bacdd8"></a> `00bacdd8` | `e0 03 16 2a` | mov w0,w22 | `FALL_THROUGH`
<a id="insn-00bacddc"></a> `00bacddc` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bacde0"></a> `00bacde0` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bacde4"></a> `00bacde4` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bacde8"></a> `00bacde8` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bacdec"></a> `00bacdec` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bacdf0"></a> `00bacdf0` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00bacdf4"></a> `00bacdf4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bacdf8"></a> `00bacdf8` | `5f 03 19 eb` | cmp x26,x25 | `FALL_THROUGH`
<a id="insn-00bacdfc"></a> `00bacdfc` | `83 fe ff 54` | b.cc 0x00bacdcc | `CONDITIONAL_JUMP`
<a id="insn-00bace00"></a> `00bace00` | `f6 ff ff 17` | b 0x00bacdd8 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bacbfc`](#insn-00bacbfc) 範囲 `[['00bacbfc', '00bacc13']]`
  - `FALL_THROUGH` [`00bacc10`](#insn-00bacc10) → [`00bacc14`](#insn-00bacc14)
- ブロック [`00bacc14`](#insn-00bacc14) 範囲 `[['00bacc14', '00bacc3f']]`
  - `FALL_THROUGH` [`00bacc3c`](#insn-00bacc3c) → [`00bacc40`](#insn-00bacc40)
- ブロック [`00bacc40`](#insn-00bacc40) 範囲 `[['00bacc40', '00bacc4b']]`
  - `CONDITIONAL_JUMP` [`00bacc48`](#insn-00bacc48) → [`00bacca8`](#insn-00bacca8)
  - `FALL_THROUGH` [`00bacc48`](#insn-00bacc48) → [`00bacc4c`](#insn-00bacc4c)
- ブロック [`00bacc4c`](#insn-00bacc4c) 範囲 `[['00bacc4c', '00bacc63']]`
  - `FALL_THROUGH` [`00bacc60`](#insn-00bacc60) → [`00bacc64`](#insn-00bacc64)
- ブロック [`00bacc64`](#insn-00bacc64) 範囲 `[['00bacc64', '00bacc77']]`
  - `FALL_THROUGH` [`00bacc74`](#insn-00bacc74) → [`00bacc78`](#insn-00bacc78)
- ブロック [`00bacc78`](#insn-00bacc78) 範囲 `[['00bacc78', '00bacc7f']]`
  - `CONDITIONAL_JUMP` [`00bacc7c`](#insn-00bacc7c) → [`00baccb0`](#insn-00baccb0)
  - `FALL_THROUGH` [`00bacc7c`](#insn-00bacc7c) → [`00bacc80`](#insn-00bacc80)
- ブロック [`00bacc80`](#insn-00bacc80) 範囲 `[['00bacc80', '00bacc9b']]`
  - `FALL_THROUGH` [`00bacc98`](#insn-00bacc98) → [`00bacc9c`](#insn-00bacc9c)
- ブロック [`00bacc9c`](#insn-00bacc9c) 範囲 `[['00bacc9c', '00bacc9f']]`
  - `CONDITIONAL_JUMP` [`00bacc9c`](#insn-00bacc9c) → [`00baccb0`](#insn-00baccb0)
  - `FALL_THROUGH` [`00bacc9c`](#insn-00bacc9c) → [`00bacca0`](#insn-00bacca0)
- ブロック [`00bacca0`](#insn-00bacca0) 範囲 `[['00bacca0', '00bacca3']]`
  - `CONDITIONAL_JUMP` [`00bacca0`](#insn-00bacca0) → [`00baccb8`](#insn-00baccb8)
  - `FALL_THROUGH` [`00bacca0`](#insn-00bacca0) → [`00bacca4`](#insn-00bacca4)
- ブロック [`00bacca4`](#insn-00bacca4) 範囲 `[['00bacca4', '00bacca7']]`
  - `UNCONDITIONAL_JUMP` [`00bacca4`](#insn-00bacca4) → [`00bacdd8`](#insn-00bacdd8)
- ブロック [`00bacca8`](#insn-00bacca8) 範囲 `[['00bacca8', '00baccab']]`
  - `CONDITIONAL_JUMP` [`00bacca8`](#insn-00bacca8) → [`00baccb8`](#insn-00baccb8)
  - `FALL_THROUGH` [`00bacca8`](#insn-00bacca8) → [`00baccac`](#insn-00baccac)
- ブロック [`00baccac`](#insn-00baccac) 範囲 `[['00baccac', '00baccaf']]`
  - `UNCONDITIONAL_JUMP` [`00baccac`](#insn-00baccac) → [`00bacdd8`](#insn-00bacdd8)
- ブロック [`00baccb0`](#insn-00baccb0) 範囲 `[['00baccb0', '00baccb7']]`
  - `CONDITIONAL_JUMP` [`00baccb4`](#insn-00baccb4) → [`00bacdd8`](#insn-00bacdd8)
  - `FALL_THROUGH` [`00baccb4`](#insn-00baccb4) → [`00baccb8`](#insn-00baccb8)
- ブロック [`00baccb8`](#insn-00baccb8) 範囲 `[['00baccb8', '00baccbb']]`
  - `FALL_THROUGH` [`00baccb8`](#insn-00baccb8) → [`00baccbc`](#insn-00baccbc)
- ブロック [`00baccbc`](#insn-00baccbc) 範囲 `[['00baccbc', '00baccc7']]`
  - `FALL_THROUGH` [`00baccc4`](#insn-00baccc4) → [`00baccc8`](#insn-00baccc8)
- ブロック [`00baccc8`](#insn-00baccc8) 範囲 `[['00baccc8', '00baccdb']]`
  - `CONDITIONAL_JUMP` [`00baccd8`](#insn-00baccd8) → [`00bacd38`](#insn-00bacd38)
  - `FALL_THROUGH` [`00baccd8`](#insn-00baccd8) → [`00baccdc`](#insn-00baccdc)
- ブロック [`00baccdc`](#insn-00baccdc) 範囲 `[['00baccdc', '00bacce3']]`
  - `FALL_THROUGH` [`00bacce0`](#insn-00bacce0) → [`00bacce4`](#insn-00bacce4)
- ブロック [`00bacce4`](#insn-00bacce4) 範囲 `[['00bacce4', '00bacd0f']]`
  - `CONDITIONAL_JUMP` [`00bacd0c`](#insn-00bacd0c) → [`00bacd40`](#insn-00bacd40)
  - `FALL_THROUGH` [`00bacd0c`](#insn-00bacd0c) → [`00bacd10`](#insn-00bacd10)
- ブロック [`00bacd10`](#insn-00bacd10) 範囲 `[['00bacd10', '00bacd2f']]`
  - `CONDITIONAL_JUMP` [`00bacd2c`](#insn-00bacd2c) → [`00bacd40`](#insn-00bacd40)
  - `FALL_THROUGH` [`00bacd2c`](#insn-00bacd2c) → [`00bacd30`](#insn-00bacd30)
- ブロック [`00bacd30`](#insn-00bacd30) 範囲 `[['00bacd30', '00bacd33']]`
  - `CONDITIONAL_JUMP` [`00bacd30`](#insn-00bacd30) → [`00bacd48`](#insn-00bacd48)
  - `FALL_THROUGH` [`00bacd30`](#insn-00bacd30) → [`00bacd34`](#insn-00bacd34)
- ブロック [`00bacd34`](#insn-00bacd34) 範囲 `[['00bacd34', '00bacd37']]`
  - `UNCONDITIONAL_JUMP` [`00bacd34`](#insn-00bacd34) → [`00bacdd8`](#insn-00bacdd8)
- ブロック [`00bacd38`](#insn-00bacd38) 範囲 `[['00bacd38', '00bacd3b']]`
  - `CONDITIONAL_JUMP` [`00bacd38`](#insn-00bacd38) → [`00bacd48`](#insn-00bacd48)
  - `FALL_THROUGH` [`00bacd38`](#insn-00bacd38) → [`00bacd3c`](#insn-00bacd3c)
- ブロック [`00bacd3c`](#insn-00bacd3c) 範囲 `[['00bacd3c', '00bacd3f']]`
  - `UNCONDITIONAL_JUMP` [`00bacd3c`](#insn-00bacd3c) → [`00bacdd8`](#insn-00bacdd8)
- ブロック [`00bacd40`](#insn-00bacd40) 範囲 `[['00bacd40', '00bacd47']]`
  - `CONDITIONAL_JUMP` [`00bacd44`](#insn-00bacd44) → [`00bacdd8`](#insn-00bacdd8)
  - `FALL_THROUGH` [`00bacd44`](#insn-00bacd44) → [`00bacd48`](#insn-00bacd48)
- ブロック [`00bacd48`](#insn-00bacd48) 範囲 `[['00bacd48', '00bacd53']]`
  - `FALL_THROUGH` [`00bacd50`](#insn-00bacd50) → [`00bacd54`](#insn-00bacd54)
- ブロック [`00bacd54`](#insn-00bacd54) 範囲 `[['00bacd54', '00bacd6b']]`
  - `CONDITIONAL_JUMP` [`00bacd68`](#insn-00bacd68) → [`00bacdc8`](#insn-00bacdc8)
  - `FALL_THROUGH` [`00bacd68`](#insn-00bacd68) → [`00bacd6c`](#insn-00bacd6c)
- ブロック [`00bacd6c`](#insn-00bacd6c) 範囲 `[['00bacd6c', '00bacd7b']]`
  - `FALL_THROUGH` [`00bacd78`](#insn-00bacd78) → [`00bacd7c`](#insn-00bacd7c)
- ブロック [`00bacd7c`](#insn-00bacd7c) 範囲 `[['00bacd7c', '00bacd7f']]`
  - `FALL_THROUGH` [`00bacd7c`](#insn-00bacd7c) → [`00bacd80`](#insn-00bacd80)
- ブロック [`00bacd80`](#insn-00bacd80) 範囲 `[['00bacd80', '00bacd8f']]`
  - `FALL_THROUGH` [`00bacd8c`](#insn-00bacd8c) → [`00bacd90`](#insn-00bacd90)
- ブロック [`00bacd90`](#insn-00bacd90) 範囲 `[['00bacd90', '00bacd93']]`
  - `FALL_THROUGH` [`00bacd90`](#insn-00bacd90) → [`00bacd94`](#insn-00bacd94)
- ブロック [`00bacd94`](#insn-00bacd94) 範囲 `[['00bacd94', '00bacd9f']]`
  - `CONDITIONAL_JUMP` [`00bacd9c`](#insn-00bacd9c) → [`00bacdf8`](#insn-00bacdf8)
  - `FALL_THROUGH` [`00bacd9c`](#insn-00bacd9c) → [`00bacda0`](#insn-00bacda0)
- ブロック [`00bacda0`](#insn-00bacda0) 範囲 `[['00bacda0', '00bacda3']]`
  - `FALL_THROUGH` [`00bacda0`](#insn-00bacda0) → [`00bacda4`](#insn-00bacda4)
- ブロック [`00bacda4`](#insn-00bacda4) 範囲 `[['00bacda4', '00bacda7']]`
  - `FALL_THROUGH` [`00bacda4`](#insn-00bacda4) → [`00bacda8`](#insn-00bacda8)
- ブロック [`00bacda8`](#insn-00bacda8) 範囲 `[['00bacda8', '00bacdb7']]`
  - `FALL_THROUGH` [`00bacdb4`](#insn-00bacdb4) → [`00bacdb8`](#insn-00bacdb8)
- ブロック [`00bacdb8`](#insn-00bacdb8) 範囲 `[['00bacdb8', '00bacdbb']]`
  - `FALL_THROUGH` [`00bacdb8`](#insn-00bacdb8) → [`00bacdbc`](#insn-00bacdbc)
- ブロック [`00bacdbc`](#insn-00bacdbc) 範囲 `[['00bacdbc', '00bacdbf']]`
  - `CONDITIONAL_JUMP` [`00bacdbc`](#insn-00bacdbc) → [`00bacdf8`](#insn-00bacdf8)
  - `FALL_THROUGH` [`00bacdbc`](#insn-00bacdbc) → [`00bacdc0`](#insn-00bacdc0)
- ブロック [`00bacdc0`](#insn-00bacdc0) 範囲 `[['00bacdc0', '00bacdc3']]`
  - `CONDITIONAL_JUMP` [`00bacdc0`](#insn-00bacdc0) → [`00bacdcc`](#insn-00bacdcc)
  - `FALL_THROUGH` [`00bacdc0`](#insn-00bacdc0) → [`00bacdc4`](#insn-00bacdc4)
- ブロック [`00bacdc4`](#insn-00bacdc4) 範囲 `[['00bacdc4', '00bacdc7']]`
  - `UNCONDITIONAL_JUMP` [`00bacdc4`](#insn-00bacdc4) → [`00bacdd8`](#insn-00bacdd8)
- ブロック [`00bacdc8`](#insn-00bacdc8) 範囲 `[['00bacdc8', '00bacdcb']]`
  - `CONDITIONAL_JUMP` [`00bacdc8`](#insn-00bacdc8) → [`00bacdd8`](#insn-00bacdd8)
  - `FALL_THROUGH` [`00bacdc8`](#insn-00bacdc8) → [`00bacdcc`](#insn-00bacdcc)
- ブロック [`00bacdcc`](#insn-00bacdcc) 範囲 `[['00bacdcc', '00bacdcf']]`
  - `FALL_THROUGH` [`00bacdcc`](#insn-00bacdcc) → [`00bacdd0`](#insn-00bacdd0)
- ブロック [`00bacdd0`](#insn-00bacdd0) 範囲 `[['00bacdd0', '00bacdd7']]`
  - `FALL_THROUGH` [`00bacdd4`](#insn-00bacdd4) → [`00bacdd8`](#insn-00bacdd8)
- ブロック [`00bacdd8`](#insn-00bacdd8) 範囲 `[['00bacdd8', '00bacddf']]`
  - `FALL_THROUGH` [`00bacddc`](#insn-00bacddc) → [`00bacde0`](#insn-00bacde0)
- ブロック [`00bacde0`](#insn-00bacde0) 範囲 `[['00bacde0', '00bacde3']]`
  - `FALL_THROUGH` [`00bacde0`](#insn-00bacde0) → [`00bacde4`](#insn-00bacde4)
- ブロック [`00bacde4`](#insn-00bacde4) 範囲 `[['00bacde4', '00bacdf3']]`
  - `FALL_THROUGH` [`00bacdf0`](#insn-00bacdf0) → [`00bacdf4`](#insn-00bacdf4)
- ブロック [`00bacdf4`](#insn-00bacdf4) 範囲 `[['00bacdf4', '00bacdf7']]`
- ブロック [`00bacdf8`](#insn-00bacdf8) 範囲 `[['00bacdf8', '00bacdff']]`
  - `CONDITIONAL_JUMP` [`00bacdfc`](#insn-00bacdfc) → [`00bacdcc`](#insn-00bacdcc)
  - `FALL_THROUGH` [`00bacdfc`](#insn-00bacdfc) → [`00bace00`](#insn-00bace00)
- ブロック [`00bace00`](#insn-00bace00) 範囲 `[['00bace00', '00bace03']]`
  - `UNCONDITIONAL_JUMP` [`00bace00`](#insn-00bace00) → [`00bacdd8`](#insn-00bacdd8)

## 命令位置別の参照

- [`00bacbfc`](#insn-00bacbfc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc00`](#insn-00bacc00) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc04`](#insn-00bacc04) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc08`](#insn-00bacc08) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc0c`](#insn-00bacc0c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc10`](#insn-00bacc10) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc28`](#insn-00bacc28) → [`00bac950`](00bac950.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bac950` · 推定シンボル `None` · 推定型 `None`
- [`00bacc48`](#insn-00bacc48) → [`00bacca8`](#insn-00bacca8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc7c`](#insn-00bacc7c) → [`00baccb0`](#insn-00baccb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc98`](#insn-00bacc98) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00bacc9c`](#insn-00bacc9c) → [`00baccb0`](#insn-00baccb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacca0`](#insn-00bacca0) → [`00baccb8`](#insn-00baccb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacca4`](#insn-00bacca4) → [`00bacdd8`](#insn-00bacdd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacca8`](#insn-00bacca8) → [`00baccb8`](#insn-00baccb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baccac`](#insn-00baccac) → [`00bacdd8`](#insn-00bacdd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baccb4`](#insn-00baccb4) → [`00bacdd8`](#insn-00bacdd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baccd8`](#insn-00baccd8) → [`00bacd38`](#insn-00bacd38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd0c`](#insn-00bacd0c) → [`00bacd40`](#insn-00bacd40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd28`](#insn-00bacd28) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00bacd2c`](#insn-00bacd2c) → [`00bacd40`](#insn-00bacd40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd30`](#insn-00bacd30) → [`00bacd48`](#insn-00bacd48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd34`](#insn-00bacd34) → [`00bacdd8`](#insn-00bacdd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd38`](#insn-00bacd38) → [`00bacd48`](#insn-00bacd48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd3c`](#insn-00bacd3c) → [`00bacdd8`](#insn-00bacdd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd44`](#insn-00bacd44) → [`00bacdd8`](#insn-00bacdd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd68`](#insn-00bacd68) → [`00bacdc8`](#insn-00bacdc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd9c`](#insn-00bacd9c) → [`00bacdf8`](#insn-00bacdf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacdb8`](#insn-00bacdb8) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00bacdbc`](#insn-00bacdbc) → [`00bacdf8`](#insn-00bacdf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacdc0`](#insn-00bacdc0) → [`00bacdcc`](#insn-00bacdcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacdc4`](#insn-00bacdc4) → [`00bacdd8`](#insn-00bacdd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacdc8`](#insn-00bacdc8) → [`00bacdd8`](#insn-00bacdd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacddc`](#insn-00bacddc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacde0`](#insn-00bacde0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacde4`](#insn-00bacde4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacde8`](#insn-00bacde8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacdec`](#insn-00bacdec) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacdfc`](#insn-00bacdfc) → [`00bacdcc`](#insn-00bacdcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace00`](#insn-00bace00) → [`00bacdd8`](#insn-00bacdd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bacbfc`](#insn-00bacbfc)

~~~json
{
  "source": "00bacbfc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc00`](#insn-00bacc00)

~~~json
{
  "source": "00bacc00",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc04`](#insn-00bacc04)

~~~json
{
  "source": "00bacc04",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc08`](#insn-00bacc08)

~~~json
{
  "source": "00bacc08",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc0c`](#insn-00bacc0c)

~~~json
{
  "source": "00bacc0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc10`](#insn-00bacc10)

~~~json
{
  "source": "00bacc10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc28`](#insn-00bacc28)

~~~json
{
  "source": "00bacc28",
  "target": "00bac950",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bacc48`](#insn-00bacc48)

~~~json
{
  "source": "00bacc48",
  "target": "00bacca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc7c`](#insn-00bacc7c)

~~~json
{
  "source": "00bacc7c",
  "target": "00baccb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc98`](#insn-00bacc98)

~~~json
{
  "source": "00bacc98",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bacc9c`](#insn-00bacc9c)

~~~json
{
  "source": "00bacc9c",
  "target": "00baccb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacca0`](#insn-00bacca0)

~~~json
{
  "source": "00bacca0",
  "target": "00baccb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacca4`](#insn-00bacca4)

~~~json
{
  "source": "00bacca4",
  "target": "00bacdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacca8`](#insn-00bacca8)

~~~json
{
  "source": "00bacca8",
  "target": "00baccb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baccac`](#insn-00baccac)

~~~json
{
  "source": "00baccac",
  "target": "00bacdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baccb4`](#insn-00baccb4)

~~~json
{
  "source": "00baccb4",
  "target": "00bacdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baccd8`](#insn-00baccd8)

~~~json
{
  "source": "00baccd8",
  "target": "00bacd38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd0c`](#insn-00bacd0c)

~~~json
{
  "source": "00bacd0c",
  "target": "00bacd40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd28`](#insn-00bacd28)

~~~json
{
  "source": "00bacd28",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bacd2c`](#insn-00bacd2c)

~~~json
{
  "source": "00bacd2c",
  "target": "00bacd40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd30`](#insn-00bacd30)

~~~json
{
  "source": "00bacd30",
  "target": "00bacd48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd34`](#insn-00bacd34)

~~~json
{
  "source": "00bacd34",
  "target": "00bacdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd38`](#insn-00bacd38)

~~~json
{
  "source": "00bacd38",
  "target": "00bacd48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd3c`](#insn-00bacd3c)

~~~json
{
  "source": "00bacd3c",
  "target": "00bacdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd44`](#insn-00bacd44)

~~~json
{
  "source": "00bacd44",
  "target": "00bacdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd68`](#insn-00bacd68)

~~~json
{
  "source": "00bacd68",
  "target": "00bacdc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd9c`](#insn-00bacd9c)

~~~json
{
  "source": "00bacd9c",
  "target": "00bacdf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacdb8`](#insn-00bacdb8)

~~~json
{
  "source": "00bacdb8",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bacdbc`](#insn-00bacdbc)

~~~json
{
  "source": "00bacdbc",
  "target": "00bacdf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacdc0`](#insn-00bacdc0)

~~~json
{
  "source": "00bacdc0",
  "target": "00bacdcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacdc4`](#insn-00bacdc4)

~~~json
{
  "source": "00bacdc4",
  "target": "00bacdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacdc8`](#insn-00bacdc8)

~~~json
{
  "source": "00bacdc8",
  "target": "00bacdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacddc`](#insn-00bacddc)

~~~json
{
  "source": "00bacddc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacde0`](#insn-00bacde0)

~~~json
{
  "source": "00bacde0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacde4`](#insn-00bacde4)

~~~json
{
  "source": "00bacde4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacde8`](#insn-00bacde8)

~~~json
{
  "source": "00bacde8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacdec`](#insn-00bacdec)

~~~json
{
  "source": "00bacdec",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacdfc`](#insn-00bacdfc)

~~~json
{
  "source": "00bacdfc",
  "target": "00bacdcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace00`](#insn-00bace00)

~~~json
{
  "source": "00bace00",
  "target": "00bacdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
