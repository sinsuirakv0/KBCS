# 00badc8c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bacc98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bac/00bacc98.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-bd2765dc1975509b5088d41f9a07cdd8)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00badc8c",
  "name": "FUN_00badc8c",
  "size": 520,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0bcf55a0873947dc5df6005a28008f053ef4401023a6fdb142b7efc8ac4eb513",
  "source_text_sha256": "0bcf55a0873947dc5df6005a28008f053ef4401023a6fdb142b7efc8ac4eb513",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00badc8c",
        "00bade93"
      ]
    ],
    "bytes_sha256": "8cc38dc94d52dc20f192ddcd4829b99856216d1837a2f3193d2070566d3a674a",
    "instruction_count": 130,
    "instruction_bytes": 520,
    "body_bytes": 520,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bad02c](../00bad/00bad02c.md)
- [00bade94](../00bad/00bade94.md)
- [00bae174](../00bae/00bae174.md)

## 呼び出し先

- [00bad9e0](../00bad/00bad9e0.md)
- [00c590f0](../00c59/00c590f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5873 bytes

~~~c

int FUN_00badc8c(undefined8 *param_1,undefined8 *param_2,undefined8 *param_3,undefined8 *param_4)

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
  
                    /* try { // try from 00badca4 to 00cadcaf has its CatchHandler @ 00baddf8 */
  iVar6 = FUN_00bad9e0();
  pbVar11 = (byte *)*param_4;
  pbVar12 = (byte *)*param_3;
                    /* try { // try from 00badcc8 to 00cadcd3 has its CatchHandler @ 00baddf4 */
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
                    /* try { // try from 00badcdc to 00cadce3 has its CatchHandler @ 00badecc */
    bVar4 = *pbVar12;
    bVar5 = *pbVar11;
    uVar1 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar12 + 8);
    }
    uVar2 = (ulong)(bVar5 >> 1);
                    /* try { // try from 00badd00 to 00cadd0b has its CatchHandler @ 00badde4 */
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
                    /* try { // try from 00badd20 to 00cadd2b has its CatchHandler @ 00badde0 */
      if ((bVar4 & 1) == 0) {
        pbVar10 = pbVar12 + 1;
      }
      iVar7 = memcmp(pbVar9,pbVar10,sVar3);
                    /* try { // try from 00badd2c to 00cadd47 has its CatchHandler @ 00bade80 */
      if (iVar7 != 0) {
        if (-1 < iVar7) {
          return iVar6;
        }
        goto LAB_00badd48;
      }
    }
    if (uVar1 <= uVar2) {
      return iVar6;
    }
  }
  else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
    return iVar6;
  }
LAB_00badd48:
                    /* try { // try from 00badd48 to 00caddb7 has its CatchHandler @ 00badf04 */
  *param_3 = pbVar11;
  *param_4 = pbVar12;
  pbVar11 = (byte *)*param_3;
  pbVar12 = (byte *)*param_2;
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
                    /* try { // try from 00baddb8 to 00cadf07 has its CatchHandler @ 00bada58 */
      iVar8 = memcmp(pbVar9,pbVar10,sVar3);
      if (iVar8 != 0) {
        if (-1 < iVar8) {
          return iVar7;
        }
        goto LAB_00baddd8;
      }
    }
    if (uVar1 <= uVar2) {
      return iVar7;
    }
  }
  else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
    return iVar7;
  }
LAB_00baddd8:
  *param_2 = pbVar11;
  *param_3 = pbVar12;
                    /* catch() { ... } // from try @ 00badd20 with catch @ 00badde0 */
  pbVar11 = (byte *)*param_2;
                    /* catch() { ... } // from try @ 00badd00 with catch @ 00badde4 */
  pbVar12 = (byte *)*param_1;
  iVar7 = iVar6 + 2;
                    /* catch() { ... } // from try @ 00badcc8 with catch @ 00baddf4 */
                    /* catch() { ... } // from try @ 00badca4 with catch @ 00baddf8 */
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
    bVar4 = *pbVar12;
    bVar5 = *pbVar11;
                    /* catch() { ... } // from try @ 00badc78 with catch @ 00bade08 */
                    /* catch() { ... } // from try @ 00badc58 with catch @ 00bade0c */
    uVar1 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar12 + 8);
    }
                    /* catch() { ... } // from try @ 00badc0c with catch @ 00bade1c */
    uVar2 = (ulong)(bVar5 >> 1);
                    /* catch() { ... } // from try @ 00badbe8 with catch @ 00bade20 */
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar11 + 8);
    }
    sVar3 = uVar1;
    if (uVar2 <= uVar1) {
      sVar3 = uVar2;
    }
    if (sVar3 != 0) {
                    /* catch() { ... } // from try @ 00badbbc with catch @ 00bade30 */
      pbVar9 = *(byte **)(pbVar11 + 0x10);
                    /* catch() { ... } // from try @ 00badb9c with catch @ 00bade34 */
      pbVar10 = *(byte **)(pbVar12 + 0x10);
      if ((bVar5 & 1) == 0) {
        pbVar9 = pbVar11 + 1;
      }
                    /* catch() { ... } // from try @ 00badb68 with catch @ 00bade44 */
      if ((bVar4 & 1) == 0) {
        pbVar10 = pbVar12 + 1;
      }
                    /* catch() { ... } // from try @ 00badb44 with catch @ 00bade48 */
      iVar8 = memcmp(pbVar9,pbVar10,sVar3);
      if (iVar8 != 0) {
        if (-1 < iVar8) {
          return iVar7;
        }
        goto LAB_00bade5c;
      }
    }
    if (uVar1 <= uVar2) {
      return iVar7;
    }
  }
  else {
                    /* catch() { ... } // from try @ 00badb18 with catch @ 00bade58 */
    if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
      return iVar7;
    }
  }
LAB_00bade5c:
                    /* catch() { ... } // from try @ 00badaf8 with catch @ 00bade5c */
  *param_1 = pbVar11;
  *param_2 = pbVar12;
                    /* catch() { ... } // from try @ 00badac0 with catch @ 00bade6c */
                    /* catch() { ... } // from try @ 00bada9c with catch @ 00bade70 */
                    /* catch() { ... } // from try @ 00badd2c with catch @ 00bade80 */
  return iVar6 + 3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00badc8c"></a> `00badc8c` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00badc90"></a> `00badc90` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00badc94"></a> `00badc94` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00badc98"></a> `00badc98` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00badc9c"></a> `00badc9c` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00badca0"></a> `00badca0` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00badca4"></a> `00badca4` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00badca8"></a> `00badca8` | `f8 03 03 aa` | mov x24,x3 | `FALL_THROUGH`
<a id="insn-00badcac"></a> `00badcac` | `f7 03 02 aa` | mov x23,x2 | `FALL_THROUGH`
<a id="insn-00badcb0"></a> `00badcb0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00badcb4"></a> `00badcb4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00badcb8"></a> `00badcb8` | `4a ff ff 97` | bl 0x00bad9e0 | `UNCONDITIONAL_CALL`
<a id="insn-00badcbc"></a> `00badcbc` | `19 03 40 f9` | ldr x25,[x24] | `FALL_THROUGH`
<a id="insn-00badcc0"></a> `00badcc0` | `fa 02 40 f9` | ldr x26,[x23] | `FALL_THROUGH`
<a id="insn-00badcc4"></a> `00badcc4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00badcc8"></a> `00badcc8` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00badccc"></a> `00badccc` | `28 43 40 f9` | ldr x8,[x25, #0x80] | `FALL_THROUGH`
<a id="insn-00badcd0"></a> `00badcd0` | `49 43 40 f9` | ldr x9,[x26, #0x80] | `FALL_THROUGH`
<a id="insn-00badcd4"></a> `00badcd4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00badcd8"></a> `00badcd8` | `01 03 00 54` | b.ne 0x00badd38 | `CONDITIONAL_JUMP`
<a id="insn-00badcdc"></a> `00badcdc` | `48 03 40 39` | ldrb w8,[x26] | `FALL_THROUGH`
<a id="insn-00badce0"></a> `00badce0` | `4a 07 40 f9` | ldr x10,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00badce4"></a> `00badce4` | `29 03 40 39` | ldrb w9,[x25] | `FALL_THROUGH`
<a id="insn-00badce8"></a> `00badce8` | `2b 07 40 f9` | ldr x11,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00badcec"></a> `00badcec` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00badcf0"></a> `00badcf0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00badcf4"></a> `00badcf4` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00badcf8"></a> `00badcf8` | `9b 01 8a 9a` | csel x27,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00badcfc"></a> `00badcfc` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00badd00"></a> `00badd00` | `bc 01 8b 9a` | csel x28,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00badd04"></a> `00badd04` | `7f 03 1c eb` | cmp x27,x28 | `FALL_THROUGH`
<a id="insn-00badd08"></a> `00badd08` | `62 33 9c 9a` | csel x2,x27,x28,cc | `FALL_THROUGH`
<a id="insn-00badd0c"></a> `00badd0c` | `a2 01 00 b4` | cbz x2,0x00badd40 | `CONDITIONAL_JUMP`
<a id="insn-00badd10"></a> `00badd10` | `2a 0b 40 f9` | ldr x10,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00badd14"></a> `00badd14` | `4b 0b 40 f9` | ldr x11,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00badd18"></a> `00badd18` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00badd1c"></a> `00badd1c` | `40 15 99 9a` | csinc x0,x10,x25,ne | `FALL_THROUGH`
<a id="insn-00badd20"></a> `00badd20` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00badd24"></a> `00badd24` | `61 15 9a 9a` | csinc x1,x11,x26,ne | `FALL_THROUGH`
<a id="insn-00badd28"></a> `00badd28` | `f2 ac 02 94` | bl 0x00c590f0 | `UNCONDITIONAL_CALL`
<a id="insn-00badd2c"></a> `00badd2c` | `a0 00 00 34` | cbz w0,0x00badd40 | `CONDITIONAL_JUMP`
<a id="insn-00badd30"></a> `00badd30` | `c0 00 f8 37` | tbnz w0,#0x1f,0x00badd48 | `CONDITIONAL_JUMP`
<a id="insn-00badd34"></a> `00badd34` | `4d 00 00 14` | b 0x00bade68 | `UNCONDITIONAL_JUMP`
<a id="insn-00badd38"></a> `00badd38` | `83 00 00 54` | b.cc 0x00badd48 | `CONDITIONAL_JUMP`
<a id="insn-00badd3c"></a> `00badd3c` | `4b 00 00 14` | b 0x00bade68 | `UNCONDITIONAL_JUMP`
<a id="insn-00badd40"></a> `00badd40` | `9f 03 1b eb` | cmp x28,x27 | `FALL_THROUGH`
<a id="insn-00badd44"></a> `00badd44` | `22 09 00 54` | b.cs 0x00bade68 | `CONDITIONAL_JUMP`
<a id="insn-00badd48"></a> `00badd48` | `f9 02 00 f9` | str x25,[x23] | `FALL_THROUGH`
<a id="insn-00badd4c"></a> `00badd4c` | `1a 03 00 f9` | str x26,[x24] | `FALL_THROUGH`
<a id="insn-00badd50"></a> `00badd50` | `f8 02 40 f9` | ldr x24,[x23] | `FALL_THROUGH`
<a id="insn-00badd54"></a> `00badd54` | `79 02 40 f9` | ldr x25,[x19] | `FALL_THROUGH`
<a id="insn-00badd58"></a> `00badd58` | `b6 06 00 11` | add w22,w21,#0x1 | `FALL_THROUGH`
<a id="insn-00badd5c"></a> `00badd5c` | `08 43 40 f9` | ldr x8,[x24, #0x80] | `FALL_THROUGH`
<a id="insn-00badd60"></a> `00badd60` | `29 43 40 f9` | ldr x9,[x25, #0x80] | `FALL_THROUGH`
<a id="insn-00badd64"></a> `00badd64` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00badd68"></a> `00badd68` | `01 03 00 54` | b.ne 0x00baddc8 | `CONDITIONAL_JUMP`
<a id="insn-00badd6c"></a> `00badd6c` | `28 03 40 39` | ldrb w8,[x25] | `FALL_THROUGH`
<a id="insn-00badd70"></a> `00badd70` | `2a 07 40 f9` | ldr x10,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00badd74"></a> `00badd74` | `09 03 40 39` | ldrb w9,[x24] | `FALL_THROUGH`
<a id="insn-00badd78"></a> `00badd78` | `0b 07 40 f9` | ldr x11,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00badd7c"></a> `00badd7c` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00badd80"></a> `00badd80` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00badd84"></a> `00badd84` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00badd88"></a> `00badd88` | `9a 01 8a 9a` | csel x26,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00badd8c"></a> `00badd8c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00badd90"></a> `00badd90` | `bb 01 8b 9a` | csel x27,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00badd94"></a> `00badd94` | `5f 03 1b eb` | cmp x26,x27 | `FALL_THROUGH`
<a id="insn-00badd98"></a> `00badd98` | `42 33 9b 9a` | csel x2,x26,x27,cc | `FALL_THROUGH`
<a id="insn-00badd9c"></a> `00badd9c` | `a2 01 00 b4` | cbz x2,0x00baddd0 | `CONDITIONAL_JUMP`
<a id="insn-00badda0"></a> `00badda0` | `0a 0b 40 f9` | ldr x10,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00badda4"></a> `00badda4` | `2b 0b 40 f9` | ldr x11,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00badda8"></a> `00badda8` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baddac"></a> `00baddac` | `40 15 98 9a` | csinc x0,x10,x24,ne | `FALL_THROUGH`
<a id="insn-00baddb0"></a> `00baddb0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baddb4"></a> `00baddb4` | `61 15 99 9a` | csinc x1,x11,x25,ne | `FALL_THROUGH`
<a id="insn-00baddb8"></a> `00baddb8` | `ce ac 02 94` | bl 0x00c590f0 | `UNCONDITIONAL_CALL`
<a id="insn-00baddbc"></a> `00baddbc` | `a0 00 00 34` | cbz w0,0x00baddd0 | `CONDITIONAL_JUMP`
<a id="insn-00baddc0"></a> `00baddc0` | `c0 00 f8 37` | tbnz w0,#0x1f,0x00baddd8 | `CONDITIONAL_JUMP`
<a id="insn-00baddc4"></a> `00baddc4` | `29 00 00 14` | b 0x00bade68 | `UNCONDITIONAL_JUMP`
<a id="insn-00baddc8"></a> `00baddc8` | `83 00 00 54` | b.cc 0x00baddd8 | `CONDITIONAL_JUMP`
<a id="insn-00baddcc"></a> `00baddcc` | `27 00 00 14` | b 0x00bade68 | `UNCONDITIONAL_JUMP`
<a id="insn-00baddd0"></a> `00baddd0` | `7f 03 1a eb` | cmp x27,x26 | `FALL_THROUGH`
<a id="insn-00baddd4"></a> `00baddd4` | `a2 04 00 54` | b.cs 0x00bade68 | `CONDITIONAL_JUMP`
<a id="insn-00baddd8"></a> `00baddd8` | `78 02 00 f9` | str x24,[x19] | `FALL_THROUGH`
<a id="insn-00badddc"></a> `00badddc` | `f9 02 00 f9` | str x25,[x23] | `FALL_THROUGH`
<a id="insn-00badde0"></a> `00badde0` | `77 02 40 f9` | ldr x23,[x19] | `FALL_THROUGH`
<a id="insn-00badde4"></a> `00badde4` | `98 02 40 f9` | ldr x24,[x20] | `FALL_THROUGH`
<a id="insn-00badde8"></a> `00badde8` | `b6 0a 00 11` | add w22,w21,#0x2 | `FALL_THROUGH`
<a id="insn-00baddec"></a> `00baddec` | `e8 42 40 f9` | ldr x8,[x23, #0x80] | `FALL_THROUGH`
<a id="insn-00baddf0"></a> `00baddf0` | `09 43 40 f9` | ldr x9,[x24, #0x80] | `FALL_THROUGH`
<a id="insn-00baddf4"></a> `00baddf4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00baddf8"></a> `00baddf8` | `01 03 00 54` | b.ne 0x00bade58 | `CONDITIONAL_JUMP`
<a id="insn-00baddfc"></a> `00baddfc` | `08 03 40 39` | ldrb w8,[x24] | `FALL_THROUGH`
<a id="insn-00bade00"></a> `00bade00` | `0a 07 40 f9` | ldr x10,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00bade04"></a> `00bade04` | `e9 02 40 39` | ldrb w9,[x23] | `FALL_THROUGH`
<a id="insn-00bade08"></a> `00bade08` | `eb 06 40 f9` | ldr x11,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bade0c"></a> `00bade0c` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bade10"></a> `00bade10` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bade14"></a> `00bade14` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bade18"></a> `00bade18` | `99 01 8a 9a` | csel x25,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bade1c"></a> `00bade1c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bade20"></a> `00bade20` | `ba 01 8b 9a` | csel x26,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bade24"></a> `00bade24` | `3f 03 1a eb` | cmp x25,x26 | `FALL_THROUGH`
<a id="insn-00bade28"></a> `00bade28` | `22 33 9a 9a` | csel x2,x25,x26,cc | `FALL_THROUGH`
<a id="insn-00bade2c"></a> `00bade2c` | `e2 02 00 b4` | cbz x2,0x00bade88 | `CONDITIONAL_JUMP`
<a id="insn-00bade30"></a> `00bade30` | `ea 0a 40 f9` | ldr x10,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00bade34"></a> `00bade34` | `0b 0b 40 f9` | ldr x11,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bade38"></a> `00bade38` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bade3c"></a> `00bade3c` | `40 15 97 9a` | csinc x0,x10,x23,ne | `FALL_THROUGH`
<a id="insn-00bade40"></a> `00bade40` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bade44"></a> `00bade44` | `61 15 98 9a` | csinc x1,x11,x24,ne | `FALL_THROUGH`
<a id="insn-00bade48"></a> `00bade48` | `aa ac 02 94` | bl 0x00c590f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bade4c"></a> `00bade4c` | `e0 01 00 34` | cbz w0,0x00bade88 | `CONDITIONAL_JUMP`
<a id="insn-00bade50"></a> `00bade50` | `60 00 f8 37` | tbnz w0,#0x1f,0x00bade5c | `CONDITIONAL_JUMP`
<a id="insn-00bade54"></a> `00bade54` | `05 00 00 14` | b 0x00bade68 | `UNCONDITIONAL_JUMP`
<a id="insn-00bade58"></a> `00bade58` | `82 00 00 54` | b.cs 0x00bade68 | `CONDITIONAL_JUMP`
<a id="insn-00bade5c"></a> `00bade5c` | `b6 0e 00 11` | add w22,w21,#0x3 | `FALL_THROUGH`
<a id="insn-00bade60"></a> `00bade60` | `97 02 00 f9` | str x23,[x20] | `FALL_THROUGH`
<a id="insn-00bade64"></a> `00bade64` | `78 02 00 f9` | str x24,[x19] | `FALL_THROUGH`
<a id="insn-00bade68"></a> `00bade68` | `e0 03 16 2a` | mov w0,w22 | `FALL_THROUGH`
<a id="insn-00bade6c"></a> `00bade6c` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bade70"></a> `00bade70` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bade74"></a> `00bade74` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bade78"></a> `00bade78` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bade7c"></a> `00bade7c` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bade80"></a> `00bade80` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00bade84"></a> `00bade84` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bade88"></a> `00bade88` | `5f 03 19 eb` | cmp x26,x25 | `FALL_THROUGH`
<a id="insn-00bade8c"></a> `00bade8c` | `83 fe ff 54` | b.cc 0x00bade5c | `CONDITIONAL_JUMP`
<a id="insn-00bade90"></a> `00bade90` | `f6 ff ff 17` | b 0x00bade68 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00badc8c`](#insn-00badc8c) 範囲 `[['00badc8c', '00badca3']]`
  - `FALL_THROUGH` [`00badca0`](#insn-00badca0) → [`00badca4`](#insn-00badca4)
- ブロック [`00badca4`](#insn-00badca4) 範囲 `[['00badca4', '00badcc7']]`
  - `FALL_THROUGH` [`00badcc4`](#insn-00badcc4) → [`00badcc8`](#insn-00badcc8)
- ブロック [`00badcc8`](#insn-00badcc8) 範囲 `[['00badcc8', '00badcdb']]`
  - `CONDITIONAL_JUMP` [`00badcd8`](#insn-00badcd8) → [`00badd38`](#insn-00badd38)
  - `FALL_THROUGH` [`00badcd8`](#insn-00badcd8) → [`00badcdc`](#insn-00badcdc)
- ブロック [`00badcdc`](#insn-00badcdc) 範囲 `[['00badcdc', '00badcff']]`
  - `FALL_THROUGH` [`00badcfc`](#insn-00badcfc) → [`00badd00`](#insn-00badd00)
- ブロック [`00badd00`](#insn-00badd00) 範囲 `[['00badd00', '00badd0f']]`
  - `CONDITIONAL_JUMP` [`00badd0c`](#insn-00badd0c) → [`00badd40`](#insn-00badd40)
  - `FALL_THROUGH` [`00badd0c`](#insn-00badd0c) → [`00badd10`](#insn-00badd10)
- ブロック [`00badd10`](#insn-00badd10) 範囲 `[['00badd10', '00badd1f']]`
  - `FALL_THROUGH` [`00badd1c`](#insn-00badd1c) → [`00badd20`](#insn-00badd20)
- ブロック [`00badd20`](#insn-00badd20) 範囲 `[['00badd20', '00badd2b']]`
  - `FALL_THROUGH` [`00badd28`](#insn-00badd28) → [`00badd2c`](#insn-00badd2c)
- ブロック [`00badd2c`](#insn-00badd2c) 範囲 `[['00badd2c', '00badd2f']]`
  - `CONDITIONAL_JUMP` [`00badd2c`](#insn-00badd2c) → [`00badd40`](#insn-00badd40)
  - `FALL_THROUGH` [`00badd2c`](#insn-00badd2c) → [`00badd30`](#insn-00badd30)
- ブロック [`00badd30`](#insn-00badd30) 範囲 `[['00badd30', '00badd33']]`
  - `CONDITIONAL_JUMP` [`00badd30`](#insn-00badd30) → [`00badd48`](#insn-00badd48)
  - `FALL_THROUGH` [`00badd30`](#insn-00badd30) → [`00badd34`](#insn-00badd34)
- ブロック [`00badd34`](#insn-00badd34) 範囲 `[['00badd34', '00badd37']]`
  - `UNCONDITIONAL_JUMP` [`00badd34`](#insn-00badd34) → [`00bade68`](#insn-00bade68)
- ブロック [`00badd38`](#insn-00badd38) 範囲 `[['00badd38', '00badd3b']]`
  - `CONDITIONAL_JUMP` [`00badd38`](#insn-00badd38) → [`00badd48`](#insn-00badd48)
  - `FALL_THROUGH` [`00badd38`](#insn-00badd38) → [`00badd3c`](#insn-00badd3c)
- ブロック [`00badd3c`](#insn-00badd3c) 範囲 `[['00badd3c', '00badd3f']]`
  - `UNCONDITIONAL_JUMP` [`00badd3c`](#insn-00badd3c) → [`00bade68`](#insn-00bade68)
- ブロック [`00badd40`](#insn-00badd40) 範囲 `[['00badd40', '00badd47']]`
  - `CONDITIONAL_JUMP` [`00badd44`](#insn-00badd44) → [`00bade68`](#insn-00bade68)
  - `FALL_THROUGH` [`00badd44`](#insn-00badd44) → [`00badd48`](#insn-00badd48)
- ブロック [`00badd48`](#insn-00badd48) 範囲 `[['00badd48', '00badd6b']]`
  - `CONDITIONAL_JUMP` [`00badd68`](#insn-00badd68) → [`00baddc8`](#insn-00baddc8)
  - `FALL_THROUGH` [`00badd68`](#insn-00badd68) → [`00badd6c`](#insn-00badd6c)
- ブロック [`00badd6c`](#insn-00badd6c) 範囲 `[['00badd6c', '00badd9f']]`
  - `CONDITIONAL_JUMP` [`00badd9c`](#insn-00badd9c) → [`00baddd0`](#insn-00baddd0)
  - `FALL_THROUGH` [`00badd9c`](#insn-00badd9c) → [`00badda0`](#insn-00badda0)
- ブロック [`00badda0`](#insn-00badda0) 範囲 `[['00badda0', '00baddb7']]`
  - `FALL_THROUGH` [`00baddb4`](#insn-00baddb4) → [`00baddb8`](#insn-00baddb8)
- ブロック [`00baddb8`](#insn-00baddb8) 範囲 `[['00baddb8', '00baddbf']]`
  - `CONDITIONAL_JUMP` [`00baddbc`](#insn-00baddbc) → [`00baddd0`](#insn-00baddd0)
  - `FALL_THROUGH` [`00baddbc`](#insn-00baddbc) → [`00baddc0`](#insn-00baddc0)
- ブロック [`00baddc0`](#insn-00baddc0) 範囲 `[['00baddc0', '00baddc3']]`
  - `CONDITIONAL_JUMP` [`00baddc0`](#insn-00baddc0) → [`00baddd8`](#insn-00baddd8)
  - `FALL_THROUGH` [`00baddc0`](#insn-00baddc0) → [`00baddc4`](#insn-00baddc4)
- ブロック [`00baddc4`](#insn-00baddc4) 範囲 `[['00baddc4', '00baddc7']]`
  - `UNCONDITIONAL_JUMP` [`00baddc4`](#insn-00baddc4) → [`00bade68`](#insn-00bade68)
- ブロック [`00baddc8`](#insn-00baddc8) 範囲 `[['00baddc8', '00baddcb']]`
  - `CONDITIONAL_JUMP` [`00baddc8`](#insn-00baddc8) → [`00baddd8`](#insn-00baddd8)
  - `FALL_THROUGH` [`00baddc8`](#insn-00baddc8) → [`00baddcc`](#insn-00baddcc)
- ブロック [`00baddcc`](#insn-00baddcc) 範囲 `[['00baddcc', '00baddcf']]`
  - `UNCONDITIONAL_JUMP` [`00baddcc`](#insn-00baddcc) → [`00bade68`](#insn-00bade68)
- ブロック [`00baddd0`](#insn-00baddd0) 範囲 `[['00baddd0', '00baddd7']]`
  - `CONDITIONAL_JUMP` [`00baddd4`](#insn-00baddd4) → [`00bade68`](#insn-00bade68)
  - `FALL_THROUGH` [`00baddd4`](#insn-00baddd4) → [`00baddd8`](#insn-00baddd8)
- ブロック [`00baddd8`](#insn-00baddd8) 範囲 `[['00baddd8', '00badddf']]`
  - `FALL_THROUGH` [`00badddc`](#insn-00badddc) → [`00badde0`](#insn-00badde0)
- ブロック [`00badde0`](#insn-00badde0) 範囲 `[['00badde0', '00badde3']]`
  - `FALL_THROUGH` [`00badde0`](#insn-00badde0) → [`00badde4`](#insn-00badde4)
- ブロック [`00badde4`](#insn-00badde4) 範囲 `[['00badde4', '00baddf3']]`
  - `FALL_THROUGH` [`00baddf0`](#insn-00baddf0) → [`00baddf4`](#insn-00baddf4)
- ブロック [`00baddf4`](#insn-00baddf4) 範囲 `[['00baddf4', '00baddf7']]`
  - `FALL_THROUGH` [`00baddf4`](#insn-00baddf4) → [`00baddf8`](#insn-00baddf8)
- ブロック [`00baddf8`](#insn-00baddf8) 範囲 `[['00baddf8', '00baddfb']]`
  - `CONDITIONAL_JUMP` [`00baddf8`](#insn-00baddf8) → [`00bade58`](#insn-00bade58)
  - `FALL_THROUGH` [`00baddf8`](#insn-00baddf8) → [`00baddfc`](#insn-00baddfc)
- ブロック [`00baddfc`](#insn-00baddfc) 範囲 `[['00baddfc', '00bade07']]`
  - `FALL_THROUGH` [`00bade04`](#insn-00bade04) → [`00bade08`](#insn-00bade08)
- ブロック [`00bade08`](#insn-00bade08) 範囲 `[['00bade08', '00bade0b']]`
  - `FALL_THROUGH` [`00bade08`](#insn-00bade08) → [`00bade0c`](#insn-00bade0c)
- ブロック [`00bade0c`](#insn-00bade0c) 範囲 `[['00bade0c', '00bade1b']]`
  - `FALL_THROUGH` [`00bade18`](#insn-00bade18) → [`00bade1c`](#insn-00bade1c)
- ブロック [`00bade1c`](#insn-00bade1c) 範囲 `[['00bade1c', '00bade1f']]`
  - `FALL_THROUGH` [`00bade1c`](#insn-00bade1c) → [`00bade20`](#insn-00bade20)
- ブロック [`00bade20`](#insn-00bade20) 範囲 `[['00bade20', '00bade2f']]`
  - `CONDITIONAL_JUMP` [`00bade2c`](#insn-00bade2c) → [`00bade88`](#insn-00bade88)
  - `FALL_THROUGH` [`00bade2c`](#insn-00bade2c) → [`00bade30`](#insn-00bade30)
- ブロック [`00bade30`](#insn-00bade30) 範囲 `[['00bade30', '00bade33']]`
  - `FALL_THROUGH` [`00bade30`](#insn-00bade30) → [`00bade34`](#insn-00bade34)
- ブロック [`00bade34`](#insn-00bade34) 範囲 `[['00bade34', '00bade43']]`
  - `FALL_THROUGH` [`00bade40`](#insn-00bade40) → [`00bade44`](#insn-00bade44)
- ブロック [`00bade44`](#insn-00bade44) 範囲 `[['00bade44', '00bade47']]`
  - `FALL_THROUGH` [`00bade44`](#insn-00bade44) → [`00bade48`](#insn-00bade48)
- ブロック [`00bade48`](#insn-00bade48) 範囲 `[['00bade48', '00bade4f']]`
  - `CONDITIONAL_JUMP` [`00bade4c`](#insn-00bade4c) → [`00bade88`](#insn-00bade88)
  - `FALL_THROUGH` [`00bade4c`](#insn-00bade4c) → [`00bade50`](#insn-00bade50)
- ブロック [`00bade50`](#insn-00bade50) 範囲 `[['00bade50', '00bade53']]`
  - `CONDITIONAL_JUMP` [`00bade50`](#insn-00bade50) → [`00bade5c`](#insn-00bade5c)
  - `FALL_THROUGH` [`00bade50`](#insn-00bade50) → [`00bade54`](#insn-00bade54)
- ブロック [`00bade54`](#insn-00bade54) 範囲 `[['00bade54', '00bade57']]`
  - `UNCONDITIONAL_JUMP` [`00bade54`](#insn-00bade54) → [`00bade68`](#insn-00bade68)
- ブロック [`00bade58`](#insn-00bade58) 範囲 `[['00bade58', '00bade5b']]`
  - `CONDITIONAL_JUMP` [`00bade58`](#insn-00bade58) → [`00bade68`](#insn-00bade68)
  - `FALL_THROUGH` [`00bade58`](#insn-00bade58) → [`00bade5c`](#insn-00bade5c)
- ブロック [`00bade5c`](#insn-00bade5c) 範囲 `[['00bade5c', '00bade67']]`
  - `FALL_THROUGH` [`00bade64`](#insn-00bade64) → [`00bade68`](#insn-00bade68)
- ブロック [`00bade68`](#insn-00bade68) 範囲 `[['00bade68', '00bade6b']]`
  - `FALL_THROUGH` [`00bade68`](#insn-00bade68) → [`00bade6c`](#insn-00bade6c)
- ブロック [`00bade6c`](#insn-00bade6c) 範囲 `[['00bade6c', '00bade6f']]`
  - `FALL_THROUGH` [`00bade6c`](#insn-00bade6c) → [`00bade70`](#insn-00bade70)
- ブロック [`00bade70`](#insn-00bade70) 範囲 `[['00bade70', '00bade7f']]`
  - `FALL_THROUGH` [`00bade7c`](#insn-00bade7c) → [`00bade80`](#insn-00bade80)
- ブロック [`00bade80`](#insn-00bade80) 範囲 `[['00bade80', '00bade87']]`
- ブロック [`00bade88`](#insn-00bade88) 範囲 `[['00bade88', '00bade8f']]`
  - `CONDITIONAL_JUMP` [`00bade8c`](#insn-00bade8c) → [`00bade5c`](#insn-00bade5c)
  - `FALL_THROUGH` [`00bade8c`](#insn-00bade8c) → [`00bade90`](#insn-00bade90)
- ブロック [`00bade90`](#insn-00bade90) 範囲 `[['00bade90', '00bade93']]`
  - `UNCONDITIONAL_JUMP` [`00bade90`](#insn-00bade90) → [`00bade68`](#insn-00bade68)

## 命令位置別の参照

- [`00badc8c`](#insn-00badc8c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badc90`](#insn-00badc90) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badc94`](#insn-00badc94) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badc98`](#insn-00badc98) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badc9c`](#insn-00badc9c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badca0`](#insn-00badca0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badcb8`](#insn-00badcb8) → [`00bad9e0`](00bad9e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bad9e0` · 推定シンボル `None` · 推定型 `None`
- [`00badcd8`](#insn-00badcd8) → [`00badd38`](#insn-00badd38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badd0c`](#insn-00badd0c) → [`00badd40`](#insn-00badd40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badd28`](#insn-00badd28) → [`00c590f0`](../00c59/00c590f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590f0` · 推定シンボル `None` · 推定型 `None`
- [`00badd2c`](#insn-00badd2c) → [`00badd40`](#insn-00badd40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badd30`](#insn-00badd30) → [`00badd48`](#insn-00badd48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badd34`](#insn-00badd34) → [`00bade68`](#insn-00bade68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badd38`](#insn-00badd38) → [`00badd48`](#insn-00badd48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badd3c`](#insn-00badd3c) → [`00bade68`](#insn-00bade68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badd44`](#insn-00badd44) → [`00bade68`](#insn-00bade68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badd68`](#insn-00badd68) → [`00baddc8`](#insn-00baddc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badd9c`](#insn-00badd9c) → [`00baddd0`](#insn-00baddd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baddb8`](#insn-00baddb8) → [`00c590f0`](../00c59/00c590f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590f0` · 推定シンボル `None` · 推定型 `None`
- [`00baddbc`](#insn-00baddbc) → [`00baddd0`](#insn-00baddd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baddc0`](#insn-00baddc0) → [`00baddd8`](#insn-00baddd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baddc4`](#insn-00baddc4) → [`00bade68`](#insn-00bade68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baddc8`](#insn-00baddc8) → [`00baddd8`](#insn-00baddd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baddcc`](#insn-00baddcc) → [`00bade68`](#insn-00bade68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baddd4`](#insn-00baddd4) → [`00bade68`](#insn-00bade68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baddf8`](#insn-00baddf8) → [`00bade58`](#insn-00bade58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bade2c`](#insn-00bade2c) → [`00bade88`](#insn-00bade88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bade48`](#insn-00bade48) → [`00c590f0`](../00c59/00c590f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590f0` · 推定シンボル `None` · 推定型 `None`
- [`00bade4c`](#insn-00bade4c) → [`00bade88`](#insn-00bade88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bade50`](#insn-00bade50) → [`00bade5c`](#insn-00bade5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bade54`](#insn-00bade54) → [`00bade68`](#insn-00bade68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bade58`](#insn-00bade58) → [`00bade68`](#insn-00bade68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bade6c`](#insn-00bade6c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bade70`](#insn-00bade70) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bade74`](#insn-00bade74) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bade78`](#insn-00bade78) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bade7c`](#insn-00bade7c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bade8c`](#insn-00bade8c) → [`00bade5c`](#insn-00bade5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bade90`](#insn-00bade90) → [`00bade68`](#insn-00bade68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00badc8c`](#insn-00badc8c)

~~~json
{
  "source": "00badc8c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badc90`](#insn-00badc90)

~~~json
{
  "source": "00badc90",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badc94`](#insn-00badc94)

~~~json
{
  "source": "00badc94",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badc98`](#insn-00badc98)

~~~json
{
  "source": "00badc98",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badc9c`](#insn-00badc9c)

~~~json
{
  "source": "00badc9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badca0`](#insn-00badca0)

~~~json
{
  "source": "00badca0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badcb8`](#insn-00badcb8)

~~~json
{
  "source": "00badcb8",
  "target": "00bad9e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00badcd8`](#insn-00badcd8)

~~~json
{
  "source": "00badcd8",
  "target": "00badd38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badd0c`](#insn-00badd0c)

~~~json
{
  "source": "00badd0c",
  "target": "00badd40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badd28`](#insn-00badd28)

~~~json
{
  "source": "00badd28",
  "target": "00c590f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00badd2c`](#insn-00badd2c)

~~~json
{
  "source": "00badd2c",
  "target": "00badd40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badd30`](#insn-00badd30)

~~~json
{
  "source": "00badd30",
  "target": "00badd48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badd34`](#insn-00badd34)

~~~json
{
  "source": "00badd34",
  "target": "00bade68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badd38`](#insn-00badd38)

~~~json
{
  "source": "00badd38",
  "target": "00badd48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badd3c`](#insn-00badd3c)

~~~json
{
  "source": "00badd3c",
  "target": "00bade68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badd44`](#insn-00badd44)

~~~json
{
  "source": "00badd44",
  "target": "00bade68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badd68`](#insn-00badd68)

~~~json
{
  "source": "00badd68",
  "target": "00baddc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badd9c`](#insn-00badd9c)

~~~json
{
  "source": "00badd9c",
  "target": "00baddd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baddb8`](#insn-00baddb8)

~~~json
{
  "source": "00baddb8",
  "target": "00c590f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baddbc`](#insn-00baddbc)

~~~json
{
  "source": "00baddbc",
  "target": "00baddd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baddc0`](#insn-00baddc0)

~~~json
{
  "source": "00baddc0",
  "target": "00baddd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baddc4`](#insn-00baddc4)

~~~json
{
  "source": "00baddc4",
  "target": "00bade68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baddc8`](#insn-00baddc8)

~~~json
{
  "source": "00baddc8",
  "target": "00baddd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baddcc`](#insn-00baddcc)

~~~json
{
  "source": "00baddcc",
  "target": "00bade68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baddd4`](#insn-00baddd4)

~~~json
{
  "source": "00baddd4",
  "target": "00bade68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baddf8`](#insn-00baddf8)

~~~json
{
  "source": "00baddf8",
  "target": "00bade58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bade2c`](#insn-00bade2c)

~~~json
{
  "source": "00bade2c",
  "target": "00bade88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bade48`](#insn-00bade48)

~~~json
{
  "source": "00bade48",
  "target": "00c590f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bade4c`](#insn-00bade4c)

~~~json
{
  "source": "00bade4c",
  "target": "00bade88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bade50`](#insn-00bade50)

~~~json
{
  "source": "00bade50",
  "target": "00bade5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bade54`](#insn-00bade54)

~~~json
{
  "source": "00bade54",
  "target": "00bade68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bade58`](#insn-00bade58)

~~~json
{
  "source": "00bade58",
  "target": "00bade68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bade6c`](#insn-00bade6c)

~~~json
{
  "source": "00bade6c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bade70`](#insn-00bade70)

~~~json
{
  "source": "00bade70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bade74`](#insn-00bade74)

~~~json
{
  "source": "00bade74",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bade78`](#insn-00bade78)

~~~json
{
  "source": "00bade78",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bade7c`](#insn-00bade7c)

~~~json
{
  "source": "00bade7c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bade8c`](#insn-00bade8c)

~~~json
{
  "source": "00bade8c",
  "target": "00bade5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bade90`](#insn-00bade90)

~~~json
{
  "source": "00bade90",
  "target": "00bade68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
