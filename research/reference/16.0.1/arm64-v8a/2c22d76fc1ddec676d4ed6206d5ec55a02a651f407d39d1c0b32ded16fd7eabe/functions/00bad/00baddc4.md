# 00baddc4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bad99c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bad/00bad99c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0009.md#compare-8515b7b84693160b846e53fa56d2e0d8)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bade60`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bad/00bade60.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0010.md#compare-7a7ddbf3da5baef87ff775fa6e6ceb5c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baddc4",
  "name": "FUN_00baddc4",
  "size": 684,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9e54edfe0c1ca16fc43532f97c9c53950db12a8891c99508e5c2d1482fcaa516",
  "source_text_sha256": "9e54edfe0c1ca16fc43532f97c9c53950db12a8891c99508e5c2d1482fcaa516",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baddc4",
        "00bae06f"
      ]
    ],
    "bytes_sha256": "5b3412e935e160983d42b4a95fa8c1ea164288d8fa0e5874046fefa62d5e6b21",
    "instruction_count": 171,
    "instruction_bytes": 684,
    "body_bytes": 684,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bad3f8](../00bad/00bad3f8.md)
- [00bae070](../00bae/00bae070.md)
- [00bae558](../00bae/00bae558.md)

## 呼び出し先

- [00c58050](../00c58/00c58050.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6282 bytes

~~~c

undefined8 FUN_00baddc4(undefined8 *param_1,undefined8 *param_2,undefined8 *param_3)

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
  long lVar13;
  long lVar14;
  
                    /* catch() { ... } // from try @ 00badc30 with catch @ 00baddd0 */
  pbVar12 = (byte *)*param_2;
  pbVar11 = (byte *)*param_1;
  lVar14 = *(long *)(pbVar12 + 0x80);
  lVar13 = *(long *)(pbVar11 + 0x80);
  if (lVar14 == lVar13) {
    bVar4 = *pbVar11;
                    /* catch() { ... } // from try @ 00badc1c with catch @ 00bade0c */
    bVar5 = *pbVar12;
                    /* catch() { ... } // from try @ 00badc04 with catch @ 00bade1c */
    uVar1 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar11 + 8);
    }
    uVar2 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar12 + 8);
    }
                    /* catch() { ... } // from try @ 00badadc with catch @ 00bade2c */
    sVar3 = uVar1;
                    /* catch() { ... } // from try @ 00badc24 with catch @ 00bade30 */
    if (uVar2 <= uVar1) {
      sVar3 = uVar2;
    }
    if (sVar3 == 0) {
LAB_00bade58:
      uVar6 = 0;
                    /* catch() { ... } // from try @ 00bada04 with catch @ 00bade64 */
      if (uVar2 < uVar1) {
        uVar6 = 0xffffffff;
      }
    }
    else {
      pbVar9 = *(byte **)(pbVar12 + 0x10);
      pbVar10 = *(byte **)(pbVar11 + 0x10);
      if ((bVar5 & 1) == 0) {
        pbVar9 = pbVar12 + 1;
      }
      if ((bVar4 & 1) == 0) {
        pbVar10 = pbVar11 + 1;
      }
      uVar6 = memcmp(pbVar9,pbVar10,sVar3);
      if (uVar6 == 0) goto LAB_00bade58;
    }
                    /* catch() { ... } // from try @ 00bad774 with catch @ 00bade68 */
    uVar6 = uVar6 >> 0x1f;
  }
  else {
    uVar6 = (uint)(lVar14 < lVar13);
  }
  pbVar9 = (byte *)*param_3;
  if (*(long *)(pbVar9 + 0x80) == lVar14) {
    bVar4 = *pbVar12;
    bVar5 = *pbVar9;
                    /* catch() { ... } // from try @ 00bad768 with catch @ 00bade9c */
    uVar1 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar12 + 8);
    }
    uVar2 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar9 + 8);
    }
    sVar3 = uVar1;
    if (uVar2 <= uVar1) {
      sVar3 = uVar2;
    }
    if (sVar3 != 0) {
      pbVar10 = *(byte **)(pbVar9 + 0x10);
      __s2 = *(byte **)(pbVar12 + 0x10);
                    /* catch() { ... } // from try @ 00bad71c with catch @ 00badec0 */
      if ((bVar5 & 1) == 0) {
        pbVar10 = pbVar9 + 1;
      }
                    /* catch() { ... } // from try @ 00bad704 with catch @ 00badec8 */
      if ((bVar4 & 1) == 0) {
        __s2 = pbVar12 + 1;
      }
                    /* catch() { ... } // from try @ 00bad7b4 with catch @ 00baded0
                       catch() { ... } // from try @ 00bad9e8 with catch @ 00baded0 */
      uVar7 = memcmp(pbVar10,__s2,sVar3);
                    /* catch() { ... } // from try @ 00bad8fc with catch @ 00baded4 */
      if (uVar7 != 0) {
        uVar7 = uVar7 >> 0x1f;
        goto joined_r0x00badf64;
      }
    }
    uVar7 = 0;
    if (uVar2 < uVar1) {
      uVar7 = 0xffffffff;
    }
    uVar7 = uVar7 >> 0x1f;
  }
  else {
    uVar7 = (uint)(*(long *)(pbVar9 + 0x80) < lVar14);
  }
joined_r0x00badf64:
  if (uVar6 == 0) {
    if (uVar7 == 0) {
      return 0;
    }
    *param_2 = pbVar9;
    *param_3 = pbVar12;
    pbVar11 = (byte *)*param_2;
    pbVar12 = (byte *)*param_1;
                    /* catch() { ... } // from try @ 00bad7fc with catch @ 00badef4 */
    if (*(long *)(pbVar11 + 0x80) == *(long *)(pbVar12 + 0x80)) {
                    /* catch() { ... } // from try @ 00bad7ec with catch @ 00badf04 */
      bVar4 = *pbVar12;
                    /* catch() { ... } // from try @ 00bad7e0 with catch @ 00badf08 */
      bVar5 = *pbVar11;
                    /* catch() { ... } // from try @ 00badbac with catch @ 00badf10
                       catch() { ... } // from try @ 00badd88 with catch @ 00badf10 */
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
            return 1;
          }
          goto LAB_00bae02c;
        }
      }
      if (uVar1 <= uVar2) {
        return 1;
      }
    }
    else if (*(long *)(pbVar12 + 0x80) <= *(long *)(pbVar11 + 0x80)) {
      return 1;
    }
LAB_00bae02c:
    *param_1 = pbVar11;
    *param_2 = pbVar12;
    return 2;
  }
  if (uVar7 != 0) {
    *param_1 = pbVar9;
    *param_3 = pbVar11;
    return 1;
  }
  *param_1 = pbVar12;
  *param_2 = pbVar11;
  pbVar12 = (byte *)*param_3;
  if (*(long *)(pbVar12 + 0x80) == lVar13) {
    bVar4 = *pbVar11;
    bVar5 = *pbVar12;
    uVar1 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar11 + 8);
    }
    uVar2 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar12 + 8);
    }
    sVar3 = uVar1;
    if (uVar2 <= uVar1) {
      sVar3 = uVar2;
    }
    if (sVar3 != 0) {
      pbVar9 = *(byte **)(pbVar12 + 0x10);
      pbVar10 = *(byte **)(pbVar11 + 0x10);
      if ((bVar5 & 1) == 0) {
        pbVar9 = pbVar12 + 1;
      }
      if ((bVar4 & 1) == 0) {
        pbVar10 = pbVar11 + 1;
      }
      iVar8 = memcmp(pbVar9,pbVar10,sVar3);
      if (iVar8 != 0) {
        if (-1 < iVar8) {
          return 1;
        }
        goto LAB_00bae040;
      }
    }
    if (uVar1 <= uVar2) {
      return 1;
    }
  }
  else if (lVar13 <= *(long *)(pbVar12 + 0x80)) {
    return 1;
  }
LAB_00bae040:
  *param_2 = pbVar12;
  *param_3 = pbVar11;
  return 2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baddc4"></a> `00baddc4` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00baddc8"></a> `00baddc8` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baddcc"></a> `00baddcc` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baddd0"></a> `00baddd0` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baddd4"></a> `00baddd4` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00baddd8"></a> `00baddd8` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00badddc"></a> `00badddc` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00badde0"></a> `00badde0` | `37 00 40 f9` | ldr x23,[x1] | `FALL_THROUGH`
<a id="insn-00badde4"></a> `00badde4` | `16 00 40 f9` | ldr x22,[x0] | `FALL_THROUGH`
<a id="insn-00badde8"></a> `00badde8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00baddec"></a> `00baddec` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00baddf0"></a> `00baddf0` | `fb 42 40 f9` | ldr x27,[x23, #0x80] | `FALL_THROUGH`
<a id="insn-00baddf4"></a> `00baddf4` | `d8 42 40 f9` | ldr x24,[x22, #0x80] | `FALL_THROUGH`
<a id="insn-00baddf8"></a> `00baddf8` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-00baddfc"></a> `00baddfc` | `7f 03 18 eb` | cmp x27,x24 | `FALL_THROUGH`
<a id="insn-00bade00"></a> `00bade00` | `81 03 00 54` | b.ne 0x00bade70 | `CONDITIONAL_JUMP`
<a id="insn-00bade04"></a> `00bade04` | `c8 02 40 39` | ldrb w8,[x22] | `FALL_THROUGH`
<a id="insn-00bade08"></a> `00bade08` | `ca 06 40 f9` | ldr x10,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bade0c"></a> `00bade0c` | `e9 02 40 39` | ldrb w9,[x23] | `FALL_THROUGH`
<a id="insn-00bade10"></a> `00bade10` | `eb 06 40 f9` | ldr x11,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bade14"></a> `00bade14` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bade18"></a> `00bade18` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bade1c"></a> `00bade1c` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bade20"></a> `00bade20` | `99 01 8a 9a` | csel x25,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bade24"></a> `00bade24` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bade28"></a> `00bade28` | `ba 01 8b 9a` | csel x26,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bade2c"></a> `00bade2c` | `3f 03 1a eb` | cmp x25,x26 | `FALL_THROUGH`
<a id="insn-00bade30"></a> `00bade30` | `22 33 9a 9a` | csel x2,x25,x26,cc | `FALL_THROUGH`
<a id="insn-00bade34"></a> `00bade34` | `22 01 00 b4` | cbz x2,0x00bade58 | `CONDITIONAL_JUMP`
<a id="insn-00bade38"></a> `00bade38` | `ea 0a 40 f9` | ldr x10,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00bade3c"></a> `00bade3c` | `cb 0a 40 f9` | ldr x11,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00bade40"></a> `00bade40` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bade44"></a> `00bade44` | `40 15 97 9a` | csinc x0,x10,x23,ne | `FALL_THROUGH`
<a id="insn-00bade48"></a> `00bade48` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bade4c"></a> `00bade4c` | `61 15 96 9a` | csinc x1,x11,x22,ne | `FALL_THROUGH`
<a id="insn-00bade50"></a> `00bade50` | `80 a8 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00bade54"></a> `00bade54` | `a0 00 00 35` | cbnz w0,0x00bade68 | `CONDITIONAL_JUMP`
<a id="insn-00bade58"></a> `00bade58` | `3f 03 1a eb` | cmp x25,x26 | `FALL_THROUGH`
<a id="insn-00bade5c"></a> `00bade5c` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00bade60"></a> `00bade60` | `5f 03 19 eb` | cmp x26,x25 | `FALL_THROUGH`
<a id="insn-00bade64"></a> `00bade64` | `00 21 9f 5a` | csinv w0,w8,wzr,cs | `FALL_THROUGH`
<a id="insn-00bade68"></a> `00bade68` | `1a 7c 1f 53` | lsr w26,w0,#0x1f | `FALL_THROUGH`
<a id="insn-00bade6c"></a> `00bade6c` | `02 00 00 14` | b 0x00bade74 | `UNCONDITIONAL_JUMP`
<a id="insn-00bade70"></a> `00bade70` | `fa a7 9f 1a` | cset w26,lt | `FALL_THROUGH`
<a id="insn-00bade74"></a> `00bade74` | `b9 02 40 f9` | ldr x25,[x21] | `FALL_THROUGH`
<a id="insn-00bade78"></a> `00bade78` | `28 43 40 f9` | ldr x8,[x25, #0x80] | `FALL_THROUGH`
<a id="insn-00bade7c"></a> `00bade7c` | `1f 01 1b eb` | cmp x8,x27 | `FALL_THROUGH`
<a id="insn-00bade80"></a> `00bade80` | `01 07 00 54` | b.ne 0x00badf60 | `CONDITIONAL_JUMP`
<a id="insn-00bade84"></a> `00bade84` | `e8 02 40 39` | ldrb w8,[x23] | `FALL_THROUGH`
<a id="insn-00bade88"></a> `00bade88` | `ea 06 40 f9` | ldr x10,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bade8c"></a> `00bade8c` | `29 03 40 39` | ldrb w9,[x25] | `FALL_THROUGH`
<a id="insn-00bade90"></a> `00bade90` | `2b 07 40 f9` | ldr x11,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00bade94"></a> `00bade94` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bade98"></a> `00bade98` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bade9c"></a> `00bade9c` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00badea0"></a> `00badea0` | `9b 01 8a 9a` | csel x27,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00badea4"></a> `00badea4` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00badea8"></a> `00badea8` | `bc 01 8b 9a` | csel x28,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00badeac"></a> `00badeac` | `7f 03 1c eb` | cmp x27,x28 | `FALL_THROUGH`
<a id="insn-00badeb0"></a> `00badeb0` | `62 33 9c 9a` | csel x2,x27,x28,cc | `FALL_THROUGH`
<a id="insn-00badeb4"></a> `00badeb4` | `42 06 00 b4` | cbz x2,0x00badf7c | `CONDITIONAL_JUMP`
<a id="insn-00badeb8"></a> `00badeb8` | `2a 0b 40 f9` | ldr x10,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00badebc"></a> `00badebc` | `eb 0a 40 f9` | ldr x11,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00badec0"></a> `00badec0` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00badec4"></a> `00badec4` | `40 15 99 9a` | csinc x0,x10,x25,ne | `FALL_THROUGH`
<a id="insn-00badec8"></a> `00badec8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00badecc"></a> `00badecc` | `61 15 97 9a` | csinc x1,x11,x23,ne | `FALL_THROUGH`
<a id="insn-00baded0"></a> `00baded0` | `60 a8 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00baded4"></a> `00baded4` | `40 05 00 34` | cbz w0,0x00badf7c | `CONDITIONAL_JUMP`
<a id="insn-00baded8"></a> `00baded8` | `08 7c 1f 53` | lsr w8,w0,#0x1f | `FALL_THROUGH`
<a id="insn-00badedc"></a> `00badedc` | `7a 04 00 37` | tbnz w26,#0x0,0x00badf68 | `CONDITIONAL_JUMP`
<a id="insn-00badee0"></a> `00badee0` | `c8 05 00 34` | cbz w8,0x00badf98 | `CONDITIONAL_JUMP`
<a id="insn-00badee4"></a> `00badee4` | `79 02 00 f9` | str x25,[x19] | `FALL_THROUGH`
<a id="insn-00badee8"></a> `00badee8` | `b7 02 00 f9` | str x23,[x21] | `FALL_THROUGH`
<a id="insn-00badeec"></a> `00badeec` | `75 02 40 f9` | ldr x21,[x19] | `FALL_THROUGH`
<a id="insn-00badef0"></a> `00badef0` | `96 02 40 f9` | ldr x22,[x20] | `FALL_THROUGH`
<a id="insn-00badef4"></a> `00badef4` | `a8 42 40 f9` | ldr x8,[x21, #0x80] | `FALL_THROUGH`
<a id="insn-00badef8"></a> `00badef8` | `c9 42 40 f9` | ldr x9,[x22, #0x80] | `FALL_THROUGH`
<a id="insn-00badefc"></a> `00badefc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00badf00"></a> `00badf00` | `a1 08 00 54` | b.ne 0x00bae014 | `CONDITIONAL_JUMP`
<a id="insn-00badf04"></a> `00badf04` | `c8 02 40 39` | ldrb w8,[x22] | `FALL_THROUGH`
<a id="insn-00badf08"></a> `00badf08` | `ca 06 40 f9` | ldr x10,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00badf0c"></a> `00badf0c` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00badf10"></a> `00badf10` | `ab 06 40 f9` | ldr x11,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00badf14"></a> `00badf14` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00badf18"></a> `00badf18` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00badf1c"></a> `00badf1c` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00badf20"></a> `00badf20` | `97 01 8a 9a` | csel x23,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00badf24"></a> `00badf24` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00badf28"></a> `00badf28` | `b8 01 8b 9a` | csel x24,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00badf2c"></a> `00badf2c` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-00badf30"></a> `00badf30` | `e2 32 98 9a` | csel x2,x23,x24,cc | `FALL_THROUGH`
<a id="insn-00badf34"></a> `00badf34` | `82 07 00 b4` | cbz x2,0x00bae024 | `CONDITIONAL_JUMP`
<a id="insn-00badf38"></a> `00badf38` | `aa 0a 40 f9` | ldr x10,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00badf3c"></a> `00badf3c` | `cb 0a 40 f9` | ldr x11,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00badf40"></a> `00badf40` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00badf44"></a> `00badf44` | `40 15 95 9a` | csinc x0,x10,x21,ne | `FALL_THROUGH`
<a id="insn-00badf48"></a> `00badf48` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00badf4c"></a> `00badf4c` | `61 15 96 9a` | csinc x1,x11,x22,ne | `FALL_THROUGH`
<a id="insn-00badf50"></a> `00badf50` | `40 a8 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00badf54"></a> `00badf54` | `80 06 00 34` | cbz w0,0x00bae024 | `CONDITIONAL_JUMP`
<a id="insn-00badf58"></a> `00badf58` | `a0 06 f8 37` | tbnz w0,#0x1f,0x00bae02c | `CONDITIONAL_JUMP`
<a id="insn-00badf5c"></a> `00badf5c` | `3d 00 00 14` | b 0x00bae050 | `UNCONDITIONAL_JUMP`
<a id="insn-00badf60"></a> `00badf60` | `e8 a7 9f 1a` | cset w8,lt | `FALL_THROUGH`
<a id="insn-00badf64"></a> `00badf64` | `fa fb 07 36` | tbz w26,#0x0,0x00badee0 | `CONDITIONAL_JUMP`
<a id="insn-00badf68"></a> `00badf68` | `c8 01 00 34` | cbz w8,0x00badfa0 | `CONDITIONAL_JUMP`
<a id="insn-00badf6c"></a> `00badf6c` | `99 02 00 f9` | str x25,[x20] | `FALL_THROUGH`
<a id="insn-00badf70"></a> `00badf70` | `b6 02 00 f9` | str x22,[x21] | `FALL_THROUGH`
<a id="insn-00badf74"></a> `00badf74` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00badf78"></a> `00badf78` | `37 00 00 14` | b 0x00bae054 | `UNCONDITIONAL_JUMP`
<a id="insn-00badf7c"></a> `00badf7c` | `7f 03 1c eb` | cmp x27,x28 | `FALL_THROUGH`
<a id="insn-00badf80"></a> `00badf80` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00badf84"></a> `00badf84` | `9f 03 1b eb` | cmp x28,x27 | `FALL_THROUGH`
<a id="insn-00badf88"></a> `00badf88` | `00 21 9f 5a` | csinv w0,w8,wzr,cs | `FALL_THROUGH`
<a id="insn-00badf8c"></a> `00badf8c` | `08 7c 1f 53` | lsr w8,w0,#0x1f | `FALL_THROUGH`
<a id="insn-00badf90"></a> `00badf90` | `da fe 07 37` | tbnz w26,#0x0,0x00badf68 | `CONDITIONAL_JUMP`
<a id="insn-00badf94"></a> `00badf94` | `d3 ff ff 17` | b 0x00badee0 | `UNCONDITIONAL_JUMP`
<a id="insn-00badf98"></a> `00badf98` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00badf9c"></a> `00badf9c` | `2e 00 00 14` | b 0x00bae054 | `UNCONDITIONAL_JUMP`
<a id="insn-00badfa0"></a> `00badfa0` | `97 02 00 f9` | str x23,[x20] | `FALL_THROUGH`
<a id="insn-00badfa4"></a> `00badfa4` | `76 02 00 f9` | str x22,[x19] | `FALL_THROUGH`
<a id="insn-00badfa8"></a> `00badfa8` | `b4 02 40 f9` | ldr x20,[x21] | `FALL_THROUGH`
<a id="insn-00badfac"></a> `00badfac` | `88 42 40 f9` | ldr x8,[x20, #0x80] | `FALL_THROUGH`
<a id="insn-00badfb0"></a> `00badfb0` | `1f 01 18 eb` | cmp x8,x24 | `FALL_THROUGH`
<a id="insn-00badfb4"></a> `00badfb4` | `41 03 00 54` | b.ne 0x00bae01c | `CONDITIONAL_JUMP`
<a id="insn-00badfb8"></a> `00badfb8` | `c8 02 40 39` | ldrb w8,[x22] | `FALL_THROUGH`
<a id="insn-00badfbc"></a> `00badfbc` | `ca 06 40 f9` | ldr x10,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00badfc0"></a> `00badfc0` | `89 02 40 39` | ldrb w9,[x20] | `FALL_THROUGH`
<a id="insn-00badfc4"></a> `00badfc4` | `8b 06 40 f9` | ldr x11,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00badfc8"></a> `00badfc8` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00badfcc"></a> `00badfcc` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00badfd0"></a> `00badfd0` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00badfd4"></a> `00badfd4` | `97 01 8a 9a` | csel x23,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00badfd8"></a> `00badfd8` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00badfdc"></a> `00badfdc` | `b8 01 8b 9a` | csel x24,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00badfe0"></a> `00badfe0` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-00badfe4"></a> `00badfe4` | `e2 32 98 9a` | csel x2,x23,x24,cc | `FALL_THROUGH`
<a id="insn-00badfe8"></a> `00badfe8` | `82 02 00 b4` | cbz x2,0x00bae038 | `CONDITIONAL_JUMP`
<a id="insn-00badfec"></a> `00badfec` | `8a 0a 40 f9` | ldr x10,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00badff0"></a> `00badff0` | `cb 0a 40 f9` | ldr x11,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00badff4"></a> `00badff4` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00badff8"></a> `00badff8` | `40 15 94 9a` | csinc x0,x10,x20,ne | `FALL_THROUGH`
<a id="insn-00badffc"></a> `00badffc` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bae000"></a> `00bae000` | `61 15 96 9a` | csinc x1,x11,x22,ne | `FALL_THROUGH`
<a id="insn-00bae004"></a> `00bae004` | `13 a8 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00bae008"></a> `00bae008` | `80 01 00 34` | cbz w0,0x00bae038 | `CONDITIONAL_JUMP`
<a id="insn-00bae00c"></a> `00bae00c` | `20 02 f8 36` | tbz w0,#0x1f,0x00bae050 | `CONDITIONAL_JUMP`
<a id="insn-00bae010"></a> `00bae010` | `0c 00 00 14` | b 0x00bae040 | `UNCONDITIONAL_JUMP`
<a id="insn-00bae014"></a> `00bae014` | `ea 01 00 54` | b.ge 0x00bae050 | `CONDITIONAL_JUMP`
<a id="insn-00bae018"></a> `00bae018` | `05 00 00 14` | b 0x00bae02c | `UNCONDITIONAL_JUMP`
<a id="insn-00bae01c"></a> `00bae01c` | `aa 01 00 54` | b.ge 0x00bae050 | `CONDITIONAL_JUMP`
<a id="insn-00bae020"></a> `00bae020` | `08 00 00 14` | b 0x00bae040 | `UNCONDITIONAL_JUMP`
<a id="insn-00bae024"></a> `00bae024` | `1f 03 17 eb` | cmp x24,x23 | `FALL_THROUGH`
<a id="insn-00bae028"></a> `00bae028` | `42 01 00 54` | b.cs 0x00bae050 | `CONDITIONAL_JUMP`
<a id="insn-00bae02c"></a> `00bae02c` | `95 02 00 f9` | str x21,[x20] | `FALL_THROUGH`
<a id="insn-00bae030"></a> `00bae030` | `76 02 00 f9` | str x22,[x19] | `FALL_THROUGH`
<a id="insn-00bae034"></a> `00bae034` | `05 00 00 14` | b 0x00bae048 | `UNCONDITIONAL_JUMP`
<a id="insn-00bae038"></a> `00bae038` | `1f 03 17 eb` | cmp x24,x23 | `FALL_THROUGH`
<a id="insn-00bae03c"></a> `00bae03c` | `a2 00 00 54` | b.cs 0x00bae050 | `CONDITIONAL_JUMP`
<a id="insn-00bae040"></a> `00bae040` | `74 02 00 f9` | str x20,[x19] | `FALL_THROUGH`
<a id="insn-00bae044"></a> `00bae044` | `b6 02 00 f9` | str x22,[x21] | `FALL_THROUGH`
<a id="insn-00bae048"></a> `00bae048` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00bae04c"></a> `00bae04c` | `02 00 00 14` | b 0x00bae054 | `UNCONDITIONAL_JUMP`
<a id="insn-00bae050"></a> `00bae050` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bae054"></a> `00bae054` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bae058"></a> `00bae058` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bae05c"></a> `00bae05c` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bae060"></a> `00bae060` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bae064"></a> `00bae064` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bae068"></a> `00bae068` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00bae06c"></a> `00bae06c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baddc4`](#insn-00baddc4) 範囲 `[['00baddc4', '00baddcf']]`
  - `FALL_THROUGH` [`00baddcc`](#insn-00baddcc) → [`00baddd0`](#insn-00baddd0)
- ブロック [`00baddd0`](#insn-00baddd0) 範囲 `[['00baddd0', '00bade03']]`
  - `CONDITIONAL_JUMP` [`00bade00`](#insn-00bade00) → [`00bade70`](#insn-00bade70)
  - `FALL_THROUGH` [`00bade00`](#insn-00bade00) → [`00bade04`](#insn-00bade04)
- ブロック [`00bade04`](#insn-00bade04) 範囲 `[['00bade04', '00bade0b']]`
  - `FALL_THROUGH` [`00bade08`](#insn-00bade08) → [`00bade0c`](#insn-00bade0c)
- ブロック [`00bade0c`](#insn-00bade0c) 範囲 `[['00bade0c', '00bade1b']]`
  - `FALL_THROUGH` [`00bade18`](#insn-00bade18) → [`00bade1c`](#insn-00bade1c)
- ブロック [`00bade1c`](#insn-00bade1c) 範囲 `[['00bade1c', '00bade2b']]`
  - `FALL_THROUGH` [`00bade28`](#insn-00bade28) → [`00bade2c`](#insn-00bade2c)
- ブロック [`00bade2c`](#insn-00bade2c) 範囲 `[['00bade2c', '00bade2f']]`
  - `FALL_THROUGH` [`00bade2c`](#insn-00bade2c) → [`00bade30`](#insn-00bade30)
- ブロック [`00bade30`](#insn-00bade30) 範囲 `[['00bade30', '00bade37']]`
  - `CONDITIONAL_JUMP` [`00bade34`](#insn-00bade34) → [`00bade58`](#insn-00bade58)
  - `FALL_THROUGH` [`00bade34`](#insn-00bade34) → [`00bade38`](#insn-00bade38)
- ブロック [`00bade38`](#insn-00bade38) 範囲 `[['00bade38', '00bade57']]`
  - `CONDITIONAL_JUMP` [`00bade54`](#insn-00bade54) → [`00bade68`](#insn-00bade68)
  - `FALL_THROUGH` [`00bade54`](#insn-00bade54) → [`00bade58`](#insn-00bade58)
- ブロック [`00bade58`](#insn-00bade58) 範囲 `[['00bade58', '00bade63']]`
  - `FALL_THROUGH` [`00bade60`](#insn-00bade60) → [`00bade64`](#insn-00bade64)
- ブロック [`00bade64`](#insn-00bade64) 範囲 `[['00bade64', '00bade67']]`
  - `FALL_THROUGH` [`00bade64`](#insn-00bade64) → [`00bade68`](#insn-00bade68)
- ブロック [`00bade68`](#insn-00bade68) 範囲 `[['00bade68', '00bade6f']]`
  - `UNCONDITIONAL_JUMP` [`00bade6c`](#insn-00bade6c) → [`00bade74`](#insn-00bade74)
- ブロック [`00bade70`](#insn-00bade70) 範囲 `[['00bade70', '00bade73']]`
  - `FALL_THROUGH` [`00bade70`](#insn-00bade70) → [`00bade74`](#insn-00bade74)
- ブロック [`00bade74`](#insn-00bade74) 範囲 `[['00bade74', '00bade83']]`
  - `CONDITIONAL_JUMP` [`00bade80`](#insn-00bade80) → [`00badf60`](#insn-00badf60)
  - `FALL_THROUGH` [`00bade80`](#insn-00bade80) → [`00bade84`](#insn-00bade84)
- ブロック [`00bade84`](#insn-00bade84) 範囲 `[['00bade84', '00bade9b']]`
  - `FALL_THROUGH` [`00bade98`](#insn-00bade98) → [`00bade9c`](#insn-00bade9c)
- ブロック [`00bade9c`](#insn-00bade9c) 範囲 `[['00bade9c', '00badeb7']]`
  - `CONDITIONAL_JUMP` [`00badeb4`](#insn-00badeb4) → [`00badf7c`](#insn-00badf7c)
  - `FALL_THROUGH` [`00badeb4`](#insn-00badeb4) → [`00badeb8`](#insn-00badeb8)
- ブロック [`00badeb8`](#insn-00badeb8) 範囲 `[['00badeb8', '00badebf']]`
  - `FALL_THROUGH` [`00badebc`](#insn-00badebc) → [`00badec0`](#insn-00badec0)
- ブロック [`00badec0`](#insn-00badec0) 範囲 `[['00badec0', '00badec7']]`
  - `FALL_THROUGH` [`00badec4`](#insn-00badec4) → [`00badec8`](#insn-00badec8)
- ブロック [`00badec8`](#insn-00badec8) 範囲 `[['00badec8', '00badecf']]`
  - `FALL_THROUGH` [`00badecc`](#insn-00badecc) → [`00baded0`](#insn-00baded0)
- ブロック [`00baded0`](#insn-00baded0) 範囲 `[['00baded0', '00baded3']]`
  - `FALL_THROUGH` [`00baded0`](#insn-00baded0) → [`00baded4`](#insn-00baded4)
- ブロック [`00baded4`](#insn-00baded4) 範囲 `[['00baded4', '00baded7']]`
  - `CONDITIONAL_JUMP` [`00baded4`](#insn-00baded4) → [`00badf7c`](#insn-00badf7c)
  - `FALL_THROUGH` [`00baded4`](#insn-00baded4) → [`00baded8`](#insn-00baded8)
- ブロック [`00baded8`](#insn-00baded8) 範囲 `[['00baded8', '00badedf']]`
  - `CONDITIONAL_JUMP` [`00badedc`](#insn-00badedc) → [`00badf68`](#insn-00badf68)
  - `FALL_THROUGH` [`00badedc`](#insn-00badedc) → [`00badee0`](#insn-00badee0)
- ブロック [`00badee0`](#insn-00badee0) 範囲 `[['00badee0', '00badee3']]`
  - `CONDITIONAL_JUMP` [`00badee0`](#insn-00badee0) → [`00badf98`](#insn-00badf98)
  - `FALL_THROUGH` [`00badee0`](#insn-00badee0) → [`00badee4`](#insn-00badee4)
- ブロック [`00badee4`](#insn-00badee4) 範囲 `[['00badee4', '00badef3']]`
  - `FALL_THROUGH` [`00badef0`](#insn-00badef0) → [`00badef4`](#insn-00badef4)
- ブロック [`00badef4`](#insn-00badef4) 範囲 `[['00badef4', '00badf03']]`
  - `CONDITIONAL_JUMP` [`00badf00`](#insn-00badf00) → [`00bae014`](#insn-00bae014)
  - `FALL_THROUGH` [`00badf00`](#insn-00badf00) → [`00badf04`](#insn-00badf04)
- ブロック [`00badf04`](#insn-00badf04) 範囲 `[['00badf04', '00badf07']]`
  - `FALL_THROUGH` [`00badf04`](#insn-00badf04) → [`00badf08`](#insn-00badf08)
- ブロック [`00badf08`](#insn-00badf08) 範囲 `[['00badf08', '00badf0f']]`
  - `FALL_THROUGH` [`00badf0c`](#insn-00badf0c) → [`00badf10`](#insn-00badf10)
- ブロック [`00badf10`](#insn-00badf10) 範囲 `[['00badf10', '00badf37']]`
  - `CONDITIONAL_JUMP` [`00badf34`](#insn-00badf34) → [`00bae024`](#insn-00bae024)
  - `FALL_THROUGH` [`00badf34`](#insn-00badf34) → [`00badf38`](#insn-00badf38)
- ブロック [`00badf38`](#insn-00badf38) 範囲 `[['00badf38', '00badf57']]`
  - `CONDITIONAL_JUMP` [`00badf54`](#insn-00badf54) → [`00bae024`](#insn-00bae024)
  - `FALL_THROUGH` [`00badf54`](#insn-00badf54) → [`00badf58`](#insn-00badf58)
- ブロック [`00badf58`](#insn-00badf58) 範囲 `[['00badf58', '00badf5b']]`
  - `CONDITIONAL_JUMP` [`00badf58`](#insn-00badf58) → [`00bae02c`](#insn-00bae02c)
  - `FALL_THROUGH` [`00badf58`](#insn-00badf58) → [`00badf5c`](#insn-00badf5c)
- ブロック [`00badf5c`](#insn-00badf5c) 範囲 `[['00badf5c', '00badf5f']]`
  - `UNCONDITIONAL_JUMP` [`00badf5c`](#insn-00badf5c) → [`00bae050`](#insn-00bae050)
- ブロック [`00badf60`](#insn-00badf60) 範囲 `[['00badf60', '00badf67']]`
  - `CONDITIONAL_JUMP` [`00badf64`](#insn-00badf64) → [`00badee0`](#insn-00badee0)
  - `FALL_THROUGH` [`00badf64`](#insn-00badf64) → [`00badf68`](#insn-00badf68)
- ブロック [`00badf68`](#insn-00badf68) 範囲 `[['00badf68', '00badf6b']]`
  - `CONDITIONAL_JUMP` [`00badf68`](#insn-00badf68) → [`00badfa0`](#insn-00badfa0)
  - `FALL_THROUGH` [`00badf68`](#insn-00badf68) → [`00badf6c`](#insn-00badf6c)
- ブロック [`00badf6c`](#insn-00badf6c) 範囲 `[['00badf6c', '00badf7b']]`
  - `UNCONDITIONAL_JUMP` [`00badf78`](#insn-00badf78) → [`00bae054`](#insn-00bae054)
- ブロック [`00badf7c`](#insn-00badf7c) 範囲 `[['00badf7c', '00badf93']]`
  - `CONDITIONAL_JUMP` [`00badf90`](#insn-00badf90) → [`00badf68`](#insn-00badf68)
  - `FALL_THROUGH` [`00badf90`](#insn-00badf90) → [`00badf94`](#insn-00badf94)
- ブロック [`00badf94`](#insn-00badf94) 範囲 `[['00badf94', '00badf97']]`
  - `UNCONDITIONAL_JUMP` [`00badf94`](#insn-00badf94) → [`00badee0`](#insn-00badee0)
- ブロック [`00badf98`](#insn-00badf98) 範囲 `[['00badf98', '00badf9f']]`
  - `UNCONDITIONAL_JUMP` [`00badf9c`](#insn-00badf9c) → [`00bae054`](#insn-00bae054)
- ブロック [`00badfa0`](#insn-00badfa0) 範囲 `[['00badfa0', '00badfb7']]`
  - `CONDITIONAL_JUMP` [`00badfb4`](#insn-00badfb4) → [`00bae01c`](#insn-00bae01c)
  - `FALL_THROUGH` [`00badfb4`](#insn-00badfb4) → [`00badfb8`](#insn-00badfb8)
- ブロック [`00badfb8`](#insn-00badfb8) 範囲 `[['00badfb8', '00badfeb']]`
  - `CONDITIONAL_JUMP` [`00badfe8`](#insn-00badfe8) → [`00bae038`](#insn-00bae038)
  - `FALL_THROUGH` [`00badfe8`](#insn-00badfe8) → [`00badfec`](#insn-00badfec)
- ブロック [`00badfec`](#insn-00badfec) 範囲 `[['00badfec', '00bae00b']]`
  - `CONDITIONAL_JUMP` [`00bae008`](#insn-00bae008) → [`00bae038`](#insn-00bae038)
  - `FALL_THROUGH` [`00bae008`](#insn-00bae008) → [`00bae00c`](#insn-00bae00c)
- ブロック [`00bae00c`](#insn-00bae00c) 範囲 `[['00bae00c', '00bae00f']]`
  - `CONDITIONAL_JUMP` [`00bae00c`](#insn-00bae00c) → [`00bae050`](#insn-00bae050)
  - `FALL_THROUGH` [`00bae00c`](#insn-00bae00c) → [`00bae010`](#insn-00bae010)
- ブロック [`00bae010`](#insn-00bae010) 範囲 `[['00bae010', '00bae013']]`
  - `UNCONDITIONAL_JUMP` [`00bae010`](#insn-00bae010) → [`00bae040`](#insn-00bae040)
- ブロック [`00bae014`](#insn-00bae014) 範囲 `[['00bae014', '00bae017']]`
  - `CONDITIONAL_JUMP` [`00bae014`](#insn-00bae014) → [`00bae050`](#insn-00bae050)
  - `FALL_THROUGH` [`00bae014`](#insn-00bae014) → [`00bae018`](#insn-00bae018)
- ブロック [`00bae018`](#insn-00bae018) 範囲 `[['00bae018', '00bae01b']]`
  - `UNCONDITIONAL_JUMP` [`00bae018`](#insn-00bae018) → [`00bae02c`](#insn-00bae02c)
- ブロック [`00bae01c`](#insn-00bae01c) 範囲 `[['00bae01c', '00bae01f']]`
  - `CONDITIONAL_JUMP` [`00bae01c`](#insn-00bae01c) → [`00bae050`](#insn-00bae050)
  - `FALL_THROUGH` [`00bae01c`](#insn-00bae01c) → [`00bae020`](#insn-00bae020)
- ブロック [`00bae020`](#insn-00bae020) 範囲 `[['00bae020', '00bae023']]`
  - `UNCONDITIONAL_JUMP` [`00bae020`](#insn-00bae020) → [`00bae040`](#insn-00bae040)
- ブロック [`00bae024`](#insn-00bae024) 範囲 `[['00bae024', '00bae02b']]`
  - `CONDITIONAL_JUMP` [`00bae028`](#insn-00bae028) → [`00bae050`](#insn-00bae050)
  - `FALL_THROUGH` [`00bae028`](#insn-00bae028) → [`00bae02c`](#insn-00bae02c)
- ブロック [`00bae02c`](#insn-00bae02c) 範囲 `[['00bae02c', '00bae037']]`
  - `UNCONDITIONAL_JUMP` [`00bae034`](#insn-00bae034) → [`00bae048`](#insn-00bae048)
- ブロック [`00bae038`](#insn-00bae038) 範囲 `[['00bae038', '00bae03f']]`
  - `CONDITIONAL_JUMP` [`00bae03c`](#insn-00bae03c) → [`00bae050`](#insn-00bae050)
  - `FALL_THROUGH` [`00bae03c`](#insn-00bae03c) → [`00bae040`](#insn-00bae040)
- ブロック [`00bae040`](#insn-00bae040) 範囲 `[['00bae040', '00bae047']]`
  - `FALL_THROUGH` [`00bae044`](#insn-00bae044) → [`00bae048`](#insn-00bae048)
- ブロック [`00bae048`](#insn-00bae048) 範囲 `[['00bae048', '00bae04f']]`
  - `UNCONDITIONAL_JUMP` [`00bae04c`](#insn-00bae04c) → [`00bae054`](#insn-00bae054)
- ブロック [`00bae050`](#insn-00bae050) 範囲 `[['00bae050', '00bae053']]`
  - `FALL_THROUGH` [`00bae050`](#insn-00bae050) → [`00bae054`](#insn-00bae054)
- ブロック [`00bae054`](#insn-00bae054) 範囲 `[['00bae054', '00bae06f']]`

## 命令位置別の参照

- [`00baddc4`](#insn-00baddc4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baddc8`](#insn-00baddc8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baddcc`](#insn-00baddcc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baddd0`](#insn-00baddd0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baddd4`](#insn-00baddd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baddd8`](#insn-00baddd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bade00`](#insn-00bade00) → [`00bade70`](#insn-00bade70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bade34`](#insn-00bade34) → [`00bade58`](#insn-00bade58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bade50`](#insn-00bade50) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00bade54`](#insn-00bade54) → [`00bade68`](#insn-00bade68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bade6c`](#insn-00bade6c) → [`00bade74`](#insn-00bade74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bade80`](#insn-00bade80) → [`00badf60`](#insn-00badf60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badeb4`](#insn-00badeb4) → [`00badf7c`](#insn-00badf7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baded0`](#insn-00baded0) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00baded4`](#insn-00baded4) → [`00badf7c`](#insn-00badf7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badedc`](#insn-00badedc) → [`00badf68`](#insn-00badf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badee0`](#insn-00badee0) → [`00badf98`](#insn-00badf98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badf00`](#insn-00badf00) → [`00bae014`](#insn-00bae014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badf34`](#insn-00badf34) → [`00bae024`](#insn-00bae024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badf50`](#insn-00badf50) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00badf54`](#insn-00badf54) → [`00bae024`](#insn-00bae024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badf58`](#insn-00badf58) → [`00bae02c`](#insn-00bae02c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badf5c`](#insn-00badf5c) → [`00bae050`](#insn-00bae050) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badf64`](#insn-00badf64) → [`00badee0`](#insn-00badee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badf68`](#insn-00badf68) → [`00badfa0`](#insn-00badfa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badf78`](#insn-00badf78) → [`00bae054`](#insn-00bae054) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badf90`](#insn-00badf90) → [`00badf68`](#insn-00badf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badf94`](#insn-00badf94) → [`00badee0`](#insn-00badee0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badf9c`](#insn-00badf9c) → [`00bae054`](#insn-00bae054) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badfb4`](#insn-00badfb4) → [`00bae01c`](#insn-00bae01c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badfe8`](#insn-00badfe8) → [`00bae038`](#insn-00bae038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae004`](#insn-00bae004) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00bae008`](#insn-00bae008) → [`00bae038`](#insn-00bae038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae00c`](#insn-00bae00c) → [`00bae050`](#insn-00bae050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae010`](#insn-00bae010) → [`00bae040`](#insn-00bae040) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae014`](#insn-00bae014) → [`00bae050`](#insn-00bae050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae018`](#insn-00bae018) → [`00bae02c`](#insn-00bae02c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae01c`](#insn-00bae01c) → [`00bae050`](#insn-00bae050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae020`](#insn-00bae020) → [`00bae040`](#insn-00bae040) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae028`](#insn-00bae028) → [`00bae050`](#insn-00bae050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae034`](#insn-00bae034) → [`00bae048`](#insn-00bae048) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae03c`](#insn-00bae03c) → [`00bae050`](#insn-00bae050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae04c`](#insn-00bae04c) → [`00bae054`](#insn-00bae054) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae054`](#insn-00bae054) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae058`](#insn-00bae058) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae05c`](#insn-00bae05c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae060`](#insn-00bae060) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae064`](#insn-00bae064) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baddc4`](#insn-00baddc4)

~~~json
{
  "source": "00baddc4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baddc8`](#insn-00baddc8)

~~~json
{
  "source": "00baddc8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baddcc`](#insn-00baddcc)

~~~json
{
  "source": "00baddcc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baddd0`](#insn-00baddd0)

~~~json
{
  "source": "00baddd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baddd4`](#insn-00baddd4)

~~~json
{
  "source": "00baddd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baddd8`](#insn-00baddd8)

~~~json
{
  "source": "00baddd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bade00`](#insn-00bade00)

~~~json
{
  "source": "00bade00",
  "target": "00bade70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bade34`](#insn-00bade34)

~~~json
{
  "source": "00bade34",
  "target": "00bade58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bade50`](#insn-00bade50)

~~~json
{
  "source": "00bade50",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
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
- 参照命令 [`00bade6c`](#insn-00bade6c)

~~~json
{
  "source": "00bade6c",
  "target": "00bade74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bade80`](#insn-00bade80)

~~~json
{
  "source": "00bade80",
  "target": "00badf60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badeb4`](#insn-00badeb4)

~~~json
{
  "source": "00badeb4",
  "target": "00badf7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baded0`](#insn-00baded0)

~~~json
{
  "source": "00baded0",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baded4`](#insn-00baded4)

~~~json
{
  "source": "00baded4",
  "target": "00badf7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badedc`](#insn-00badedc)

~~~json
{
  "source": "00badedc",
  "target": "00badf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badee0`](#insn-00badee0)

~~~json
{
  "source": "00badee0",
  "target": "00badf98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badf00`](#insn-00badf00)

~~~json
{
  "source": "00badf00",
  "target": "00bae014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badf34`](#insn-00badf34)

~~~json
{
  "source": "00badf34",
  "target": "00bae024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badf50`](#insn-00badf50)

~~~json
{
  "source": "00badf50",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00badf54`](#insn-00badf54)

~~~json
{
  "source": "00badf54",
  "target": "00bae024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badf58`](#insn-00badf58)

~~~json
{
  "source": "00badf58",
  "target": "00bae02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badf5c`](#insn-00badf5c)

~~~json
{
  "source": "00badf5c",
  "target": "00bae050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badf64`](#insn-00badf64)

~~~json
{
  "source": "00badf64",
  "target": "00badee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badf68`](#insn-00badf68)

~~~json
{
  "source": "00badf68",
  "target": "00badfa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badf78`](#insn-00badf78)

~~~json
{
  "source": "00badf78",
  "target": "00bae054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badf90`](#insn-00badf90)

~~~json
{
  "source": "00badf90",
  "target": "00badf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badf94`](#insn-00badf94)

~~~json
{
  "source": "00badf94",
  "target": "00badee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badf9c`](#insn-00badf9c)

~~~json
{
  "source": "00badf9c",
  "target": "00bae054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badfb4`](#insn-00badfb4)

~~~json
{
  "source": "00badfb4",
  "target": "00bae01c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badfe8`](#insn-00badfe8)

~~~json
{
  "source": "00badfe8",
  "target": "00bae038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae004`](#insn-00bae004)

~~~json
{
  "source": "00bae004",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bae008`](#insn-00bae008)

~~~json
{
  "source": "00bae008",
  "target": "00bae038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae00c`](#insn-00bae00c)

~~~json
{
  "source": "00bae00c",
  "target": "00bae050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae010`](#insn-00bae010)

~~~json
{
  "source": "00bae010",
  "target": "00bae040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae014`](#insn-00bae014)

~~~json
{
  "source": "00bae014",
  "target": "00bae050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae018`](#insn-00bae018)

~~~json
{
  "source": "00bae018",
  "target": "00bae02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae01c`](#insn-00bae01c)

~~~json
{
  "source": "00bae01c",
  "target": "00bae050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae020`](#insn-00bae020)

~~~json
{
  "source": "00bae020",
  "target": "00bae040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae028`](#insn-00bae028)

~~~json
{
  "source": "00bae028",
  "target": "00bae050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae034`](#insn-00bae034)

~~~json
{
  "source": "00bae034",
  "target": "00bae048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae03c`](#insn-00bae03c)

~~~json
{
  "source": "00bae03c",
  "target": "00bae050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae04c`](#insn-00bae04c)

~~~json
{
  "source": "00bae04c",
  "target": "00bae054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae054`](#insn-00bae054)

~~~json
{
  "source": "00bae054",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae058`](#insn-00bae058)

~~~json
{
  "source": "00bae058",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae05c`](#insn-00bae05c)

~~~json
{
  "source": "00bae05c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae060`](#insn-00bae060)

~~~json
{
  "source": "00bae060",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae064`](#insn-00bae064)

~~~json
{
  "source": "00bae064",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
