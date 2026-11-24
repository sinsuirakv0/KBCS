# 00baccbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0174.md#review-288c4b292609e3a2c4415f5c4cc27b85)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bad0e4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bad/00bad0e4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0078.md#compare-1a77907c72504f999399c2a9afcbad87)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baccbc",
  "name": "FUN_00baccbc",
  "size": 788,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "370a2e8a4b76d52d0178bc0f030a61df1c493df2b3d97f304025552de6e19597",
  "source_text_sha256": "370a2e8a4b76d52d0178bc0f030a61df1c493df2b3d97f304025552de6e19597",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baccbc",
        "00bacfcf"
      ]
    ],
    "bytes_sha256": "0430819cadb4bd0df3500a21036b395b3165e02d1ebeaa5512122569579d89ee",
    "instruction_count": 197,
    "instruction_bytes": 788,
    "body_bytes": 788,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00babb74](../00bab/00babb74.md)

## 呼び出し先

- [00bac528](../00bac/00bac528.md)
- [00bac7d4](../00bac/00bac7d4.md)
- [00bac9dc](../00bac/00bac9dc.md)
- [00c57c50](../00c57/00c57c50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 7446 bytes

~~~c

bool FUN_00baccbc(undefined8 *param_1,undefined8 *param_2)

{
  ulong uVar1;
  ulong uVar2;
  size_t sVar3;
  byte bVar4;
  byte bVar5;
  int iVar6;
  undefined8 *puVar7;
  byte *pbVar8;
  byte *pbVar9;
  byte *pbVar10;
  undefined8 *puVar11;
  long lVar12;
  byte *pbVar13;
  undefined8 *puVar14;
  ulong uVar15;
  long lVar16;
  long lVar17;
  int local_6c;
  
  switch((long)param_2 - (long)param_1 >> 3) {
  case 0:
  case 1:
    break;
  case 2:
    pbVar10 = (byte *)param_2[-1];
    pbVar13 = (byte *)*param_1;
    if (*(ulong *)(pbVar10 + 0x80) == *(ulong *)(pbVar13 + 0x80)) {
      bVar4 = *pbVar13;
      bVar5 = *pbVar10;
      uVar15 = (ulong)(bVar4 >> 1);
      if ((bVar4 & 1) != 0) {
        uVar15 = *(ulong *)(pbVar13 + 8);
      }
      uVar1 = (ulong)(bVar5 >> 1);
      if ((bVar5 & 1) != 0) {
        uVar1 = *(ulong *)(pbVar10 + 8);
      }
      sVar3 = uVar15;
      if (uVar1 <= uVar15) {
        sVar3 = uVar1;
      }
      if (sVar3 != 0) {
        pbVar8 = *(byte **)(pbVar10 + 0x10);
                    /* try { // try from 00bacd60 to 00cacd6b has its CatchHandler @ 00bad424 */
        pbVar9 = *(byte **)(pbVar13 + 0x10);
        if ((bVar5 & 1) == 0) {
          pbVar8 = pbVar10 + 1;
        }
        if ((bVar4 & 1) == 0) {
          pbVar9 = pbVar13 + 1;
        }
        iVar6 = memcmp(pbVar8,pbVar9,sVar3);
        if (iVar6 != 0) {
          if (-1 < iVar6) {
            return true;
          }
          goto LAB_00bacf88;
        }
      }
      if (uVar15 <= uVar1) {
        return true;
      }
    }
    else if (*(ulong *)(pbVar13 + 0x80) <= *(ulong *)(pbVar10 + 0x80)) {
      return true;
    }
LAB_00bacf88:
    *param_1 = pbVar10;
    param_2[-1] = pbVar13;
    break;
  case 3:
    FUN_00bac528(param_1,param_1 + 1,param_2 + -1);
    break;
  case 4:
    FUN_00bac7d4(param_1,param_1 + 1,param_1 + 2,param_2 + -1);
    break;
  case 5:
                    /* try { // try from 00bacf6c to 00cacfbf has its CatchHandler @ 00bacca8 */
    FUN_00bac9dc(param_1,param_1 + 1,param_1 + 2,param_1 + 3,param_2 + -1);
    break;
  default:
                    /* try { // try from 00bacd84 to 00cacd8f has its CatchHandler @ 00bad420 */
    FUN_00bac528(param_1,param_1 + 1,param_1 + 2);
                    /* try { // try from 00bacd98 to 00cacda3 has its CatchHandler @ 00bad400 */
    if (param_1 + 3 != param_2) {
                    /* try { // try from 00bacda4 to 00cacdaf has its CatchHandler @ 00bad3f0 */
      lVar12 = 0;
      local_6c = 0;
      puVar14 = param_1 + 3;
      puVar11 = param_1 + 2;
      do {
        puVar7 = puVar14;
        pbVar13 = (byte *)*puVar7;
        pbVar10 = (byte *)*puVar11;
                    /* try { // try from 00bacdf0 to 00cacdfb has its CatchHandler @ 00bad3bc */
        uVar15 = *(ulong *)(pbVar13 + 0x80);
        if (uVar15 == *(ulong *)(pbVar10 + 0x80)) {
          bVar4 = *pbVar10;
          bVar5 = *pbVar13;
                    /* try { // try from 00bace14 to 00cace1f has its CatchHandler @ 00bad3b8 */
          uVar1 = (ulong)(bVar4 >> 1);
          if ((bVar4 & 1) != 0) {
            uVar1 = *(ulong *)(pbVar10 + 8);
          }
                    /* try { // try from 00bace24 to 00cace2f has its CatchHandler @ 00bad3b0 */
          uVar2 = (ulong)(bVar5 >> 1);
          if ((bVar5 & 1) != 0) {
            uVar2 = *(ulong *)(pbVar13 + 8);
          }
          sVar3 = uVar1;
          if (uVar2 <= uVar1) {
            sVar3 = uVar2;
          }
          if (sVar3 != 0) {
            pbVar8 = *(byte **)(pbVar13 + 0x10);
            pbVar9 = *(byte **)(pbVar10 + 0x10);
                    /* try { // try from 00bace44 to 00cace4f has its CatchHandler @ 00bad39c */
            if ((bVar5 & 1) == 0) {
              pbVar8 = pbVar13 + 1;
            }
            if ((bVar4 & 1) == 0) {
              pbVar9 = pbVar10 + 1;
            }
            iVar6 = memcmp(pbVar8,pbVar9,sVar3);
            if (iVar6 != 0) {
              if (iVar6 < 0) goto LAB_00bace78;
              goto LAB_00bacdd4;
            }
          }
                    /* try { // try from 00bace70 to 00cace7b has its CatchHandler @ 00bad390 */
          if (uVar2 < uVar1) {
LAB_00bace78:
            *puVar7 = pbVar10;
            puVar14 = puVar11;
            if (puVar11 != param_1) {
              lVar17 = lVar12;
                    /* try { // try from 00bace94 to 00cace9f has its CatchHandler @ 00bad38c */
              do {
                pbVar10 = *(byte **)((long)param_1 + lVar17 + 8);
                if (uVar15 == *(ulong *)(pbVar10 + 0x80)) {
                    /* try { // try from 00bacec4 to 00cacecf has its CatchHandler @ 00bad370 */
                  bVar4 = *pbVar10;
                  bVar5 = *pbVar13;
                    /* try { // try from 00baced0 to 00cacedb has its CatchHandler @ 00bad36c */
                    /* try { // try from 00bacedc to 00cacee7 has its CatchHandler @ 00bad368 */
                  uVar1 = (ulong)(bVar4 >> 1);
                  if ((bVar4 & 1) != 0) {
                    uVar1 = *(ulong *)(pbVar10 + 8);
                  }
                  uVar2 = (ulong)(bVar5 >> 1);
                    /* try { // try from 00bacee8 to 00cacef3 has its CatchHandler @ 00bad364 */
                  if ((bVar5 & 1) != 0) {
                    uVar2 = *(ulong *)(pbVar13 + 8);
                  }
                  sVar3 = uVar1;
                  if (uVar2 <= uVar1) {
                    sVar3 = uVar2;
                  }
                  puVar14 = puVar11;
                  if (sVar3 != 0) {
                    /* try { // try from 00bacf04 to 00cacf1f has its CatchHandler @ 00bad434 */
                    pbVar9 = *(byte **)(pbVar10 + 0x10);
                    pbVar8 = pbVar13 + 1;
                    if ((bVar5 & 1) != 0) {
                      pbVar8 = *(byte **)(pbVar13 + 0x10);
                    }
                    if ((bVar4 & 1) == 0) {
                      pbVar9 = pbVar10 + 1;
                    }
                    iVar6 = memcmp(pbVar8,pbVar9,sVar3);
                    if (iVar6 != 0) {
                      if (iVar6 < 0) goto LAB_00bace9c;
                      break;
                    }
                  }
                  if (uVar1 <= uVar2) break;
                }
                else if (*(ulong *)(pbVar10 + 0x80) <= uVar15) {
                  puVar14 = (undefined8 *)((long)param_1 + lVar17 + 0x10);
                  break;
                }
LAB_00bace9c:
                lVar16 = lVar17 + -8;
                puVar11 = puVar11 + -1;
                    /* try { // try from 00bacea4 to 00caceaf has its CatchHandler @ 00bad384 */
                *(byte **)((long)param_1 + lVar17 + 0x10) = pbVar10;
                puVar14 = param_1;
                lVar17 = lVar16;
              } while (lVar16 != -0x10);
            }
            *puVar14 = pbVar13;
            local_6c = local_6c + 1;
                    /* try { // try from 00bacdc8 to 00cacdd3 has its CatchHandler @ 00bad3c8 */
            if (local_6c == 8) {
                    /* try { // try from 00bacfc0 to 00cacfcb has its CatchHandler @ 00bad35c */
              return puVar7 + 1 == param_2;
            }
          }
        }
        else if (uVar15 < *(ulong *)(pbVar10 + 0x80)) goto LAB_00bace78;
LAB_00bacdd4:
        lVar12 = lVar12 + 8;
        puVar14 = puVar7 + 1;
        puVar11 = puVar7;
      } while (puVar7 + 1 != param_2);
    }
  }
  return true;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baccbc"></a> `00baccbc` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00baccc0"></a> `00baccc0` | `fc 6f 02 a9` | stp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baccc4"></a> `00baccc4` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baccc8"></a> `00baccc8` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bacccc"></a> `00bacccc` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00baccd0"></a> `00baccd0` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00baccd4"></a> `00baccd4` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00baccd8"></a> `00baccd8` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00baccdc"></a> `00baccdc` | `28 00 00 cb` | sub x8,x1,x0 | `FALL_THROUGH`
<a id="insn-00bacce0"></a> `00bacce0` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bacce4"></a> `00bacce4` | `fb 03 01 aa` | mov x27,x1 | `FALL_THROUGH`
<a id="insn-00bacce8"></a> `00bacce8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00baccec"></a> `00baccec` | `1f 15 00 f1` | cmp x8,#0x5 | `FALL_THROUGH`
<a id="insn-00baccf0"></a> `00baccf0` | `a8 04 00 54` | b.hi 0x00bacd84 | `CONDITIONAL_JUMP`
<a id="insn-00baccf4"></a> `00baccf4` | `09 bb ff d0` | adrp x9,0x30e000 | `FALL_THROUGH`
<a id="insn-00baccf8"></a> `00baccf8` | `29 19 07 91` | add x9,x9,#0x1c6 | `FALL_THROUGH`
<a id="insn-00baccfc"></a> `00baccfc` | `aa 00 00 10` | adr x10,0xbacd10 | `FALL_THROUGH`
<a id="insn-00bacd00"></a> `00bacd00` | `2b 69 68 38` | ldrb w11,[x9, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bacd04"></a> `00bacd04` | `4a 09 0b 8b` | add x10,x10,x11, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bacd08"></a> `00bacd08` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bacd0c"></a> `00bacd0c` | `40 01 1f d6` | br x10 | `COMPUTED_JUMP`
<a id="insn-00bacd10"></a> `00bacd10` | `74 83 5f f8` | ldur x20,[x27, #-0x8] | `FALL_THROUGH`
<a id="insn-00bacd14"></a> `00bacd14` | `75 02 40 f9` | ldr x21,[x19] | `FALL_THROUGH`
<a id="insn-00bacd18"></a> `00bacd18` | `88 42 40 f9` | ldr x8,[x20, #0x80] | `FALL_THROUGH`
<a id="insn-00bacd1c"></a> `00bacd1c` | `a9 42 40 f9` | ldr x9,[x21, #0x80] | `FALL_THROUGH`
<a id="insn-00bacd20"></a> `00bacd20` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bacd24"></a> `00bacd24` | `01 13 00 54` | b.ne 0x00bacf84 | `CONDITIONAL_JUMP`
<a id="insn-00bacd28"></a> `00bacd28` | `a8 02 40 39` | ldrb w8,[x21] | `FALL_THROUGH`
<a id="insn-00bacd2c"></a> `00bacd2c` | `aa 06 40 f9` | ldr x10,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bacd30"></a> `00bacd30` | `89 02 40 39` | ldrb w9,[x20] | `FALL_THROUGH`
<a id="insn-00bacd34"></a> `00bacd34` | `8b 06 40 f9` | ldr x11,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bacd38"></a> `00bacd38` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacd3c"></a> `00bacd3c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacd40"></a> `00bacd40` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacd44"></a> `00bacd44` | `96 01 8a 9a` | csel x22,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bacd48"></a> `00bacd48` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacd4c"></a> `00bacd4c` | `b7 01 8b 9a` | csel x23,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bacd50"></a> `00bacd50` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-00bacd54"></a> `00bacd54` | `c2 32 97 9a` | csel x2,x22,x23,cc | `FALL_THROUGH`
<a id="insn-00bacd58"></a> `00bacd58` | `e2 12 00 b4` | cbz x2,0x00bacfb4 | `CONDITIONAL_JUMP`
<a id="insn-00bacd5c"></a> `00bacd5c` | `8a 0a 40 f9` | ldr x10,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bacd60"></a> `00bacd60` | `ab 0a 40 f9` | ldr x11,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bacd64"></a> `00bacd64` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacd68"></a> `00bacd68` | `40 15 94 9a` | csinc x0,x10,x20,ne | `FALL_THROUGH`
<a id="insn-00bacd6c"></a> `00bacd6c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacd70"></a> `00bacd70` | `61 15 95 9a` | csinc x1,x11,x21,ne | `FALL_THROUGH`
<a id="insn-00bacd74"></a> `00bacd74` | `b7 ab 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bacd78"></a> `00bacd78` | `e0 11 00 34` | cbz w0,0x00bacfb4 | `CONDITIONAL_JUMP`
<a id="insn-00bacd7c"></a> `00bacd7c` | `60 10 f8 37` | tbnz w0,#0x1f,0x00bacf88 | `CONDITIONAL_JUMP`
<a id="insn-00bacd80"></a> `00bacd80` | `84 00 00 14` | b 0x00bacf90 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacd84"></a> `00bacd84` | `75 42 00 91` | add x21,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00bacd88"></a> `00bacd88` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00bacd8c"></a> `00bacd8c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bacd90"></a> `00bacd90` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bacd94"></a> `00bacd94` | `e5 fd ff 97` | bl 0x00bac528 | `UNCONDITIONAL_CALL`
<a id="insn-00bacd98"></a> `00bacd98` | `68 62 00 91` | add x8,x19,#0x18 | `FALL_THROUGH`
<a id="insn-00bacd9c"></a> `00bacd9c` | `1f 01 1b eb` | cmp x8,x27 | `FALL_THROUGH`
<a id="insn-00bacda0"></a> `00bacda0` | `80 0f 00 54` | b.eq 0x00bacf90 | `CONDITIONAL_JUMP`
<a id="insn-00bacda4"></a> `00bacda4` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-00bacda8"></a> `00bacda8` | `ff 17 00 b9` | str wzr,[sp, #0x14] | `FALL_THROUGH`
<a id="insn-00bacdac"></a> `00bacdac` | `fb 07 00 f9` | str x27,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bacdb0"></a> `00bacdb0` | `0d 00 00 14` | b 0x00bacde4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacdb4"></a> `00bacdb4` | `f9 03 13 aa` | mov x25,x19 | `FALL_THROUGH`
<a id="insn-00bacdb8"></a> `00bacdb8` | `f5 6f 40 a9` | ldp x21,x27,[sp] | `FALL_THROUGH`
<a id="insn-00bacdbc"></a> `00bacdbc` | `e8 17 40 b9` | ldr w8,[sp, #0x14] | `FALL_THROUGH`
<a id="insn-00bacdc0"></a> `00bacdc0` | `38 03 00 f9` | str x24,[x25] | `FALL_THROUGH`
<a id="insn-00bacdc4"></a> `00bacdc4` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacdc8"></a> `00bacdc8` | `1f 21 00 71` | cmp w8,#0x8 | `FALL_THROUGH`
<a id="insn-00bacdcc"></a> `00bacdcc` | `e8 17 00 b9` | str w8,[sp, #0x14] | `FALL_THROUGH`
<a id="insn-00bacdd0"></a> `00bacdd0` | `80 0f 00 54` | b.eq 0x00bacfc0 | `CONDITIONAL_JUMP`
<a id="insn-00bacdd4"></a> `00bacdd4` | `a8 22 00 91` | add x8,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00bacdd8"></a> `00bacdd8` | `1f 01 1b eb` | cmp x8,x27 | `FALL_THROUGH`
<a id="insn-00bacddc"></a> `00bacddc` | `d6 22 00 91` | add x22,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00bacde0"></a> `00bacde0` | `80 0d 00 54` | b.eq 0x00bacf90 | `CONDITIONAL_JUMP`
<a id="insn-00bacde4"></a> `00bacde4` | `f9 03 15 aa` | mov x25,x21 | `FALL_THROUGH`
<a id="insn-00bacde8"></a> `00bacde8` | `18 01 40 f9` | ldr x24,[x8] | `FALL_THROUGH`
<a id="insn-00bacdec"></a> `00bacdec` | `34 03 40 f9` | ldr x20,[x25] | `FALL_THROUGH`
<a id="insn-00bacdf0"></a> `00bacdf0` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00bacdf4"></a> `00bacdf4` | `1a 43 40 f9` | ldr x26,[x24, #0x80] | `FALL_THROUGH`
<a id="insn-00bacdf8"></a> `00bacdf8` | `88 42 40 f9` | ldr x8,[x20, #0x80] | `FALL_THROUGH`
<a id="insn-00bacdfc"></a> `00bacdfc` | `5f 03 08 eb` | cmp x26,x8 | `FALL_THROUGH`
<a id="insn-00bace00"></a> `00bace00` | `21 03 00 54` | b.ne 0x00bace64 | `CONDITIONAL_JUMP`
<a id="insn-00bace04"></a> `00bace04` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-00bace08"></a> `00bace08` | `8a 06 40 f9` | ldr x10,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bace0c"></a> `00bace0c` | `09 03 40 39` | ldrb w9,[x24] | `FALL_THROUGH`
<a id="insn-00bace10"></a> `00bace10` | `0b 07 40 f9` | ldr x11,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00bace14"></a> `00bace14` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bace18"></a> `00bace18` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bace1c"></a> `00bace1c` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bace20"></a> `00bace20` | `97 01 8a 9a` | csel x23,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bace24"></a> `00bace24` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bace28"></a> `00bace28` | `bb 01 8b 9a` | csel x27,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bace2c"></a> `00bace2c` | `ff 02 1b eb` | cmp x23,x27 | `FALL_THROUGH`
<a id="insn-00bace30"></a> `00bace30` | `e2 32 9b 9a` | csel x2,x23,x27,cc | `FALL_THROUGH`
<a id="insn-00bace34"></a> `00bace34` | `c2 01 00 b4` | cbz x2,0x00bace6c | `CONDITIONAL_JUMP`
<a id="insn-00bace38"></a> `00bace38` | `0a 0b 40 f9` | ldr x10,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bace3c"></a> `00bace3c` | `8b 0a 40 f9` | ldr x11,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bace40"></a> `00bace40` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bace44"></a> `00bace44` | `40 15 98 9a` | csinc x0,x10,x24,ne | `FALL_THROUGH`
<a id="insn-00bace48"></a> `00bace48` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bace4c"></a> `00bace4c` | `61 15 94 9a` | csinc x1,x11,x20,ne | `FALL_THROUGH`
<a id="insn-00bace50"></a> `00bace50` | `80 ab 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bace54"></a> `00bace54` | `c0 00 00 34` | cbz w0,0x00bace6c | `CONDITIONAL_JUMP`
<a id="insn-00bace58"></a> `00bace58` | `fb 07 40 f9` | ldr x27,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bace5c"></a> `00bace5c` | `c0 fb ff 36` | tbz w0,#0x1f,0x00bacdd4 | `CONDITIONAL_JUMP`
<a id="insn-00bace60"></a> `00bace60` | `06 00 00 14` | b 0x00bace78 | `UNCONDITIONAL_JUMP`
<a id="insn-00bace64"></a> `00bace64` | `82 fb ff 54` | b.cs 0x00bacdd4 | `CONDITIONAL_JUMP`
<a id="insn-00bace68"></a> `00bace68` | `04 00 00 14` | b 0x00bace78 | `UNCONDITIONAL_JUMP`
<a id="insn-00bace6c"></a> `00bace6c` | `7f 03 17 eb` | cmp x27,x23 | `FALL_THROUGH`
<a id="insn-00bace70"></a> `00bace70` | `fb 07 40 f9` | ldr x27,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bace74"></a> `00bace74` | `02 fb ff 54` | b.cs 0x00bacdd4 | `CONDITIONAL_JUMP`
<a id="insn-00bace78"></a> `00bace78` | `3f 03 13 eb` | cmp x25,x19 | `FALL_THROUGH`
<a id="insn-00bace7c"></a> `00bace7c` | `b4 02 00 f9` | str x20,[x21] | `FALL_THROUGH`
<a id="insn-00bace80"></a> `00bace80` | `e0 f9 ff 54` | b.eq 0x00bacdbc | `CONDITIONAL_JUMP`
<a id="insn-00bace84"></a> `00bace84` | `08 07 00 91` | add x8,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00bace88"></a> `00bace88` | `fb 03 16 aa` | mov x27,x22 | `FALL_THROUGH`
<a id="insn-00bace8c"></a> `00bace8c` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bace90"></a> `00bace90` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bace94"></a> `00bace94` | `07 00 00 14` | b 0x00baceb0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bace98"></a> `00bace98` | `c2 04 00 54` | b.cs 0x00bacf30 | `CONDITIONAL_JUMP`
<a id="insn-00bace9c"></a> `00bace9c` | `7b 23 00 d1` | sub x27,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00bacea0"></a> `00bacea0` | `39 23 00 d1` | sub x25,x25,#0x8 | `FALL_THROUGH`
<a id="insn-00bacea4"></a> `00bacea4` | `7f 43 00 b1` | cmn x27,#0x10 | `FALL_THROUGH`
<a id="insn-00bacea8"></a> `00bacea8` | `97 0a 00 f9` | str x23,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00baceac"></a> `00baceac` | `40 f8 ff 54` | b.eq 0x00bacdb4 | `CONDITIONAL_JUMP`
<a id="insn-00baceb0"></a> `00baceb0` | `74 02 1b 8b` | add x20,x19,x27 | `FALL_THROUGH`
<a id="insn-00baceb4"></a> `00baceb4` | `97 06 40 f9` | ldr x23,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00baceb8"></a> `00baceb8` | `e8 42 40 f9` | ldr x8,[x23, #0x80] | `FALL_THROUGH`
<a id="insn-00bacebc"></a> `00bacebc` | `5f 03 08 eb` | cmp x26,x8 | `FALL_THROUGH`
<a id="insn-00bacec0"></a> `00bacec0` | `c1 fe ff 54` | b.ne 0x00bace98 | `CONDITIONAL_JUMP`
<a id="insn-00bacec4"></a> `00bacec4` | `e8 02 40 39` | ldrb w8,[x23] | `FALL_THROUGH`
<a id="insn-00bacec8"></a> `00bacec8` | `ea 06 40 f9` | ldr x10,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bacecc"></a> `00bacecc` | `09 03 40 39` | ldrb w9,[x24] | `FALL_THROUGH`
<a id="insn-00baced0"></a> `00baced0` | `0b 07 40 f9` | ldr x11,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00baced4"></a> `00baced4` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00baced8"></a> `00baced8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacedc"></a> `00bacedc` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacee0"></a> `00bacee0` | `9c 01 8a 9a` | csel x28,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bacee4"></a> `00bacee4` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacee8"></a> `00bacee8` | `b5 01 8b 9a` | csel x21,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00baceec"></a> `00baceec` | `9f 03 15 eb` | cmp x28,x21 | `FALL_THROUGH`
<a id="insn-00bacef0"></a> `00bacef0` | `82 33 95 9a` | csel x2,x28,x21,cc | `FALL_THROUGH`
<a id="insn-00bacef4"></a> `00bacef4` | `82 01 00 b4` | cbz x2,0x00bacf24 | `CONDITIONAL_JUMP`
<a id="insn-00bacef8"></a> `00bacef8` | `0a 0b 40 f9` | ldr x10,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bacefc"></a> `00bacefc` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bacf00"></a> `00bacf00` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bacf04"></a> `00bacf04` | `eb 0a 40 f9` | ldr x11,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00bacf08"></a> `00bacf08` | `20 01 8a 9a` | csel x0,x9,x10,eq | `FALL_THROUGH`
<a id="insn-00bacf0c"></a> `00bacf0c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacf10"></a> `00bacf10` | `61 15 97 9a` | csinc x1,x11,x23,ne | `FALL_THROUGH`
<a id="insn-00bacf14"></a> `00bacf14` | `4f ab 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bacf18"></a> `00bacf18` | `60 00 00 34` | cbz w0,0x00bacf24 | `CONDITIONAL_JUMP`
<a id="insn-00bacf1c"></a> `00bacf1c` | `00 fc ff 37` | tbnz w0,#0x1f,0x00bace9c | `CONDITIONAL_JUMP`
<a id="insn-00bacf20"></a> `00bacf20` | `a6 ff ff 17` | b 0x00bacdb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacf24"></a> `00bacf24` | `bf 02 1c eb` | cmp x21,x28 | `FALL_THROUGH`
<a id="insn-00bacf28"></a> `00bacf28` | `a3 fb ff 54` | b.cc 0x00bace9c | `CONDITIONAL_JUMP`
<a id="insn-00bacf2c"></a> `00bacf2c` | `a3 ff ff 17` | b 0x00bacdb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacf30"></a> `00bacf30` | `68 02 1b 8b` | add x8,x19,x27 | `FALL_THROUGH`
<a id="insn-00bacf34"></a> `00bacf34` | `19 41 00 91` | add x25,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bacf38"></a> `00bacf38` | `a0 ff ff 17` | b 0x00bacdb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacf3c"></a> `00bacf3c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00bacf40"></a> `00bacf40` | `62 23 00 d1` | sub x2,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00bacf44"></a> `00bacf44` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bacf48"></a> `00bacf48` | `78 fd ff 97` | bl 0x00bac528 | `UNCONDITIONAL_CALL`
<a id="insn-00bacf4c"></a> `00bacf4c` | `11 00 00 14` | b 0x00bacf90 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacf50"></a> `00bacf50` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00bacf54"></a> `00bacf54` | `62 42 00 91` | add x2,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00bacf58"></a> `00bacf58` | `63 23 00 d1` | sub x3,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00bacf5c"></a> `00bacf5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bacf60"></a> `00bacf60` | `1d fe ff 97` | bl 0x00bac7d4 | `UNCONDITIONAL_CALL`
<a id="insn-00bacf64"></a> `00bacf64` | `0b 00 00 14` | b 0x00bacf90 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacf68"></a> `00bacf68` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00bacf6c"></a> `00bacf6c` | `62 42 00 91` | add x2,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00bacf70"></a> `00bacf70` | `63 62 00 91` | add x3,x19,#0x18 | `FALL_THROUGH`
<a id="insn-00bacf74"></a> `00bacf74` | `64 23 00 d1` | sub x4,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00bacf78"></a> `00bacf78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bacf7c"></a> `00bacf7c` | `98 fe ff 97` | bl 0x00bac9dc | `UNCONDITIONAL_CALL`
<a id="insn-00bacf80"></a> `00bacf80` | `04 00 00 14` | b 0x00bacf90 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacf84"></a> `00bacf84` | `62 00 00 54` | b.cs 0x00bacf90 | `CONDITIONAL_JUMP`
<a id="insn-00bacf88"></a> `00bacf88` | `74 02 00 f9` | str x20,[x19] | `FALL_THROUGH`
<a id="insn-00bacf8c"></a> `00bacf8c` | `75 83 1f f8` | stur x21,[x27, #-0x8] | `FALL_THROUGH`
<a id="insn-00bacf90"></a> `00bacf90` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bacf94"></a> `00bacf94` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bacf98"></a> `00bacf98` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bacf9c"></a> `00bacf9c` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bacfa0"></a> `00bacfa0` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bacfa4"></a> `00bacfa4` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bacfa8"></a> `00bacfa8` | `fc 6f 42 a9` | ldp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bacfac"></a> `00bacfac` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bacfb0"></a> `00bacfb0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bacfb4"></a> `00bacfb4` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00bacfb8"></a> `00bacfb8` | `c2 fe ff 54` | b.cs 0x00bacf90 | `CONDITIONAL_JUMP`
<a id="insn-00bacfbc"></a> `00bacfbc` | `f3 ff ff 17` | b 0x00bacf88 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacfc0"></a> `00bacfc0` | `a8 22 00 91` | add x8,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00bacfc4"></a> `00bacfc4` | `1f 01 1b eb` | cmp x8,x27 | `FALL_THROUGH`
<a id="insn-00bacfc8"></a> `00bacfc8` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bacfcc"></a> `00bacfcc` | `f2 ff ff 17` | b 0x00bacf94 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00baccbc`](#insn-00baccbc) 範囲 `[['00baccbc', '00baccf3']]`
  - `CONDITIONAL_JUMP` [`00baccf0`](#insn-00baccf0) → [`00bacd84`](#insn-00bacd84)
  - `FALL_THROUGH` [`00baccf0`](#insn-00baccf0) → [`00baccf4`](#insn-00baccf4)
- ブロック [`00baccf4`](#insn-00baccf4) 範囲 `[['00baccf4', '00bacd0b']]`
  - `FALL_THROUGH` [`00bacd08`](#insn-00bacd08) → [`00bacd0c`](#insn-00bacd0c)
- ブロック [`00bacd0c`](#insn-00bacd0c) 範囲 `[['00bacd0c', '00bacd0f']]`
  - `COMPUTED_JUMP` [`00bacd0c`](#insn-00bacd0c) → [`00bacf94`](#insn-00bacf94)
  - `COMPUTED_JUMP` [`00bacd0c`](#insn-00bacd0c) → [`00bacd10`](#insn-00bacd10)
  - `COMPUTED_JUMP` [`00bacd0c`](#insn-00bacd0c) → [`00bacf3c`](#insn-00bacf3c)
  - `COMPUTED_JUMP` [`00bacd0c`](#insn-00bacd0c) → [`00bacf50`](#insn-00bacf50)
  - `COMPUTED_JUMP` [`00bacd0c`](#insn-00bacd0c) → [`00bacf68`](#insn-00bacf68)
- ブロック [`00bacd10`](#insn-00bacd10) 範囲 `[['00bacd10', '00bacd27']]`
  - `CONDITIONAL_JUMP` [`00bacd24`](#insn-00bacd24) → [`00bacf84`](#insn-00bacf84)
  - `FALL_THROUGH` [`00bacd24`](#insn-00bacd24) → [`00bacd28`](#insn-00bacd28)
- ブロック [`00bacd28`](#insn-00bacd28) 範囲 `[['00bacd28', '00bacd5b']]`
  - `CONDITIONAL_JUMP` [`00bacd58`](#insn-00bacd58) → [`00bacfb4`](#insn-00bacfb4)
  - `FALL_THROUGH` [`00bacd58`](#insn-00bacd58) → [`00bacd5c`](#insn-00bacd5c)
- ブロック [`00bacd5c`](#insn-00bacd5c) 範囲 `[['00bacd5c', '00bacd5f']]`
  - `FALL_THROUGH` [`00bacd5c`](#insn-00bacd5c) → [`00bacd60`](#insn-00bacd60)
- ブロック [`00bacd60`](#insn-00bacd60) 範囲 `[['00bacd60', '00bacd7b']]`
  - `CONDITIONAL_JUMP` [`00bacd78`](#insn-00bacd78) → [`00bacfb4`](#insn-00bacfb4)
  - `FALL_THROUGH` [`00bacd78`](#insn-00bacd78) → [`00bacd7c`](#insn-00bacd7c)
- ブロック [`00bacd7c`](#insn-00bacd7c) 範囲 `[['00bacd7c', '00bacd7f']]`
  - `CONDITIONAL_JUMP` [`00bacd7c`](#insn-00bacd7c) → [`00bacf88`](#insn-00bacf88)
  - `FALL_THROUGH` [`00bacd7c`](#insn-00bacd7c) → [`00bacd80`](#insn-00bacd80)
- ブロック [`00bacd80`](#insn-00bacd80) 範囲 `[['00bacd80', '00bacd83']]`
  - `UNCONDITIONAL_JUMP` [`00bacd80`](#insn-00bacd80) → [`00bacf90`](#insn-00bacf90)
- ブロック [`00bacd84`](#insn-00bacd84) 範囲 `[['00bacd84', '00bacd97']]`
  - `FALL_THROUGH` [`00bacd94`](#insn-00bacd94) → [`00bacd98`](#insn-00bacd98)
- ブロック [`00bacd98`](#insn-00bacd98) 範囲 `[['00bacd98', '00bacda3']]`
  - `CONDITIONAL_JUMP` [`00bacda0`](#insn-00bacda0) → [`00bacf90`](#insn-00bacf90)
  - `FALL_THROUGH` [`00bacda0`](#insn-00bacda0) → [`00bacda4`](#insn-00bacda4)
- ブロック [`00bacda4`](#insn-00bacda4) 範囲 `[['00bacda4', '00bacdb3']]`
  - `UNCONDITIONAL_JUMP` [`00bacdb0`](#insn-00bacdb0) → [`00bacde4`](#insn-00bacde4)
- ブロック [`00bacdb4`](#insn-00bacdb4) 範囲 `[['00bacdb4', '00bacdb7']]`
  - `FALL_THROUGH` [`00bacdb4`](#insn-00bacdb4) → [`00bacdb8`](#insn-00bacdb8)
- ブロック [`00bacdb8`](#insn-00bacdb8) 範囲 `[['00bacdb8', '00bacdbb']]`
  - `FALL_THROUGH` [`00bacdb8`](#insn-00bacdb8) → [`00bacdbc`](#insn-00bacdbc)
- ブロック [`00bacdbc`](#insn-00bacdbc) 範囲 `[['00bacdbc', '00bacdc7']]`
  - `FALL_THROUGH` [`00bacdc4`](#insn-00bacdc4) → [`00bacdc8`](#insn-00bacdc8)
- ブロック [`00bacdc8`](#insn-00bacdc8) 範囲 `[['00bacdc8', '00bacdd3']]`
  - `CONDITIONAL_JUMP` [`00bacdd0`](#insn-00bacdd0) → [`00bacfc0`](#insn-00bacfc0)
  - `FALL_THROUGH` [`00bacdd0`](#insn-00bacdd0) → [`00bacdd4`](#insn-00bacdd4)
- ブロック [`00bacdd4`](#insn-00bacdd4) 範囲 `[['00bacdd4', '00bacde3']]`
  - `CONDITIONAL_JUMP` [`00bacde0`](#insn-00bacde0) → [`00bacf90`](#insn-00bacf90)
  - `FALL_THROUGH` [`00bacde0`](#insn-00bacde0) → [`00bacde4`](#insn-00bacde4)
- ブロック [`00bacde4`](#insn-00bacde4) 範囲 `[['00bacde4', '00bacdef']]`
  - `FALL_THROUGH` [`00bacdec`](#insn-00bacdec) → [`00bacdf0`](#insn-00bacdf0)
- ブロック [`00bacdf0`](#insn-00bacdf0) 範囲 `[['00bacdf0', '00bace03']]`
  - `CONDITIONAL_JUMP` [`00bace00`](#insn-00bace00) → [`00bace64`](#insn-00bace64)
  - `FALL_THROUGH` [`00bace00`](#insn-00bace00) → [`00bace04`](#insn-00bace04)
- ブロック [`00bace04`](#insn-00bace04) 範囲 `[['00bace04', '00bace13']]`
  - `FALL_THROUGH` [`00bace10`](#insn-00bace10) → [`00bace14`](#insn-00bace14)
- ブロック [`00bace14`](#insn-00bace14) 範囲 `[['00bace14', '00bace23']]`
  - `FALL_THROUGH` [`00bace20`](#insn-00bace20) → [`00bace24`](#insn-00bace24)
- ブロック [`00bace24`](#insn-00bace24) 範囲 `[['00bace24', '00bace37']]`
  - `CONDITIONAL_JUMP` [`00bace34`](#insn-00bace34) → [`00bace6c`](#insn-00bace6c)
  - `FALL_THROUGH` [`00bace34`](#insn-00bace34) → [`00bace38`](#insn-00bace38)
- ブロック [`00bace38`](#insn-00bace38) 範囲 `[['00bace38', '00bace43']]`
  - `FALL_THROUGH` [`00bace40`](#insn-00bace40) → [`00bace44`](#insn-00bace44)
- ブロック [`00bace44`](#insn-00bace44) 範囲 `[['00bace44', '00bace57']]`
  - `CONDITIONAL_JUMP` [`00bace54`](#insn-00bace54) → [`00bace6c`](#insn-00bace6c)
  - `FALL_THROUGH` [`00bace54`](#insn-00bace54) → [`00bace58`](#insn-00bace58)
- ブロック [`00bace58`](#insn-00bace58) 範囲 `[['00bace58', '00bace5f']]`
  - `CONDITIONAL_JUMP` [`00bace5c`](#insn-00bace5c) → [`00bacdd4`](#insn-00bacdd4)
  - `FALL_THROUGH` [`00bace5c`](#insn-00bace5c) → [`00bace60`](#insn-00bace60)
- ブロック [`00bace60`](#insn-00bace60) 範囲 `[['00bace60', '00bace63']]`
  - `UNCONDITIONAL_JUMP` [`00bace60`](#insn-00bace60) → [`00bace78`](#insn-00bace78)
- ブロック [`00bace64`](#insn-00bace64) 範囲 `[['00bace64', '00bace67']]`
  - `CONDITIONAL_JUMP` [`00bace64`](#insn-00bace64) → [`00bacdd4`](#insn-00bacdd4)
  - `FALL_THROUGH` [`00bace64`](#insn-00bace64) → [`00bace68`](#insn-00bace68)
- ブロック [`00bace68`](#insn-00bace68) 範囲 `[['00bace68', '00bace6b']]`
  - `UNCONDITIONAL_JUMP` [`00bace68`](#insn-00bace68) → [`00bace78`](#insn-00bace78)
- ブロック [`00bace6c`](#insn-00bace6c) 範囲 `[['00bace6c', '00bace6f']]`
  - `FALL_THROUGH` [`00bace6c`](#insn-00bace6c) → [`00bace70`](#insn-00bace70)
- ブロック [`00bace70`](#insn-00bace70) 範囲 `[['00bace70', '00bace77']]`
  - `CONDITIONAL_JUMP` [`00bace74`](#insn-00bace74) → [`00bacdd4`](#insn-00bacdd4)
  - `FALL_THROUGH` [`00bace74`](#insn-00bace74) → [`00bace78`](#insn-00bace78)
- ブロック [`00bace78`](#insn-00bace78) 範囲 `[['00bace78', '00bace83']]`
  - `CONDITIONAL_JUMP` [`00bace80`](#insn-00bace80) → [`00bacdbc`](#insn-00bacdbc)
  - `FALL_THROUGH` [`00bace80`](#insn-00bace80) → [`00bace84`](#insn-00bace84)
- ブロック [`00bace84`](#insn-00bace84) 範囲 `[['00bace84', '00bace93']]`
  - `FALL_THROUGH` [`00bace90`](#insn-00bace90) → [`00bace94`](#insn-00bace94)
- ブロック [`00bace94`](#insn-00bace94) 範囲 `[['00bace94', '00bace97']]`
  - `UNCONDITIONAL_JUMP` [`00bace94`](#insn-00bace94) → [`00baceb0`](#insn-00baceb0)
- ブロック [`00bace98`](#insn-00bace98) 範囲 `[['00bace98', '00bace9b']]`
  - `CONDITIONAL_JUMP` [`00bace98`](#insn-00bace98) → [`00bacf30`](#insn-00bacf30)
  - `FALL_THROUGH` [`00bace98`](#insn-00bace98) → [`00bace9c`](#insn-00bace9c)
- ブロック [`00bace9c`](#insn-00bace9c) 範囲 `[['00bace9c', '00bacea3']]`
  - `FALL_THROUGH` [`00bacea0`](#insn-00bacea0) → [`00bacea4`](#insn-00bacea4)
- ブロック [`00bacea4`](#insn-00bacea4) 範囲 `[['00bacea4', '00baceaf']]`
  - `CONDITIONAL_JUMP` [`00baceac`](#insn-00baceac) → [`00bacdb4`](#insn-00bacdb4)
  - `FALL_THROUGH` [`00baceac`](#insn-00baceac) → [`00baceb0`](#insn-00baceb0)
- ブロック [`00baceb0`](#insn-00baceb0) 範囲 `[['00baceb0', '00bacec3']]`
  - `CONDITIONAL_JUMP` [`00bacec0`](#insn-00bacec0) → [`00bace98`](#insn-00bace98)
  - `FALL_THROUGH` [`00bacec0`](#insn-00bacec0) → [`00bacec4`](#insn-00bacec4)
- ブロック [`00bacec4`](#insn-00bacec4) 範囲 `[['00bacec4', '00bacecf']]`
  - `FALL_THROUGH` [`00bacecc`](#insn-00bacecc) → [`00baced0`](#insn-00baced0)
- ブロック [`00baced0`](#insn-00baced0) 範囲 `[['00baced0', '00bacedb']]`
  - `FALL_THROUGH` [`00baced8`](#insn-00baced8) → [`00bacedc`](#insn-00bacedc)
- ブロック [`00bacedc`](#insn-00bacedc) 範囲 `[['00bacedc', '00bacee7']]`
  - `FALL_THROUGH` [`00bacee4`](#insn-00bacee4) → [`00bacee8`](#insn-00bacee8)
- ブロック [`00bacee8`](#insn-00bacee8) 範囲 `[['00bacee8', '00bacef7']]`
  - `CONDITIONAL_JUMP` [`00bacef4`](#insn-00bacef4) → [`00bacf24`](#insn-00bacf24)
  - `FALL_THROUGH` [`00bacef4`](#insn-00bacef4) → [`00bacef8`](#insn-00bacef8)
- ブロック [`00bacef8`](#insn-00bacef8) 範囲 `[['00bacef8', '00bacf03']]`
  - `FALL_THROUGH` [`00bacf00`](#insn-00bacf00) → [`00bacf04`](#insn-00bacf04)
- ブロック [`00bacf04`](#insn-00bacf04) 範囲 `[['00bacf04', '00bacf1b']]`
  - `CONDITIONAL_JUMP` [`00bacf18`](#insn-00bacf18) → [`00bacf24`](#insn-00bacf24)
  - `FALL_THROUGH` [`00bacf18`](#insn-00bacf18) → [`00bacf1c`](#insn-00bacf1c)
- ブロック [`00bacf1c`](#insn-00bacf1c) 範囲 `[['00bacf1c', '00bacf1f']]`
  - `CONDITIONAL_JUMP` [`00bacf1c`](#insn-00bacf1c) → [`00bace9c`](#insn-00bace9c)
  - `FALL_THROUGH` [`00bacf1c`](#insn-00bacf1c) → [`00bacf20`](#insn-00bacf20)
- ブロック [`00bacf20`](#insn-00bacf20) 範囲 `[['00bacf20', '00bacf23']]`
  - `UNCONDITIONAL_JUMP` [`00bacf20`](#insn-00bacf20) → [`00bacdb8`](#insn-00bacdb8)
- ブロック [`00bacf24`](#insn-00bacf24) 範囲 `[['00bacf24', '00bacf2b']]`
  - `CONDITIONAL_JUMP` [`00bacf28`](#insn-00bacf28) → [`00bace9c`](#insn-00bace9c)
  - `FALL_THROUGH` [`00bacf28`](#insn-00bacf28) → [`00bacf2c`](#insn-00bacf2c)
- ブロック [`00bacf2c`](#insn-00bacf2c) 範囲 `[['00bacf2c', '00bacf2f']]`
  - `UNCONDITIONAL_JUMP` [`00bacf2c`](#insn-00bacf2c) → [`00bacdb8`](#insn-00bacdb8)
- ブロック [`00bacf30`](#insn-00bacf30) 範囲 `[['00bacf30', '00bacf3b']]`
  - `UNCONDITIONAL_JUMP` [`00bacf38`](#insn-00bacf38) → [`00bacdb8`](#insn-00bacdb8)
- ブロック [`00bacf3c`](#insn-00bacf3c) 範囲 `[['00bacf3c', '00bacf4f']]`
  - `UNCONDITIONAL_JUMP` [`00bacf4c`](#insn-00bacf4c) → [`00bacf90`](#insn-00bacf90)
- ブロック [`00bacf50`](#insn-00bacf50) 範囲 `[['00bacf50', '00bacf67']]`
  - `UNCONDITIONAL_JUMP` [`00bacf64`](#insn-00bacf64) → [`00bacf90`](#insn-00bacf90)
- ブロック [`00bacf68`](#insn-00bacf68) 範囲 `[['00bacf68', '00bacf6b']]`
  - `FALL_THROUGH` [`00bacf68`](#insn-00bacf68) → [`00bacf6c`](#insn-00bacf6c)
- ブロック [`00bacf6c`](#insn-00bacf6c) 範囲 `[['00bacf6c', '00bacf83']]`
  - `UNCONDITIONAL_JUMP` [`00bacf80`](#insn-00bacf80) → [`00bacf90`](#insn-00bacf90)
- ブロック [`00bacf84`](#insn-00bacf84) 範囲 `[['00bacf84', '00bacf87']]`
  - `CONDITIONAL_JUMP` [`00bacf84`](#insn-00bacf84) → [`00bacf90`](#insn-00bacf90)
  - `FALL_THROUGH` [`00bacf84`](#insn-00bacf84) → [`00bacf88`](#insn-00bacf88)
- ブロック [`00bacf88`](#insn-00bacf88) 範囲 `[['00bacf88', '00bacf8f']]`
  - `FALL_THROUGH` [`00bacf8c`](#insn-00bacf8c) → [`00bacf90`](#insn-00bacf90)
- ブロック [`00bacf90`](#insn-00bacf90) 範囲 `[['00bacf90', '00bacf93']]`
  - `FALL_THROUGH` [`00bacf90`](#insn-00bacf90) → [`00bacf94`](#insn-00bacf94)
- ブロック [`00bacf94`](#insn-00bacf94) 範囲 `[['00bacf94', '00bacfb3']]`
- ブロック [`00bacfb4`](#insn-00bacfb4) 範囲 `[['00bacfb4', '00bacfbb']]`
  - `CONDITIONAL_JUMP` [`00bacfb8`](#insn-00bacfb8) → [`00bacf90`](#insn-00bacf90)
  - `FALL_THROUGH` [`00bacfb8`](#insn-00bacfb8) → [`00bacfbc`](#insn-00bacfbc)
- ブロック [`00bacfbc`](#insn-00bacfbc) 範囲 `[['00bacfbc', '00bacfbf']]`
  - `UNCONDITIONAL_JUMP` [`00bacfbc`](#insn-00bacfbc) → [`00bacf88`](#insn-00bacf88)
- ブロック [`00bacfc0`](#insn-00bacfc0) 範囲 `[['00bacfc0', '00bacfcf']]`
  - `UNCONDITIONAL_JUMP` [`00bacfcc`](#insn-00bacfcc) → [`00bacf94`](#insn-00bacf94)

## 命令位置別の参照

- [`00baccc0`](#insn-00baccc0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baccc4`](#insn-00baccc4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baccc8`](#insn-00baccc8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacccc`](#insn-00bacccc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baccd0`](#insn-00baccd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baccd4`](#insn-00baccd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baccf0`](#insn-00baccf0) → [`00bacd84`](#insn-00bacd84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bacd0c::default` · 推定型 `None`
- [`00bacd00`](#insn-00bacd00) → `0030e1c6`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bacd0c::switchdataD_0030e1c6` · 推定型 `byte`
- [`00bacd0c`](#insn-00bacd0c) → [`00bacf94`](#insn-00bacf94) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bacd0c::caseD_0` · 推定型 `None`
- [`00bacd0c`](#insn-00bacd0c) → [`00bacd10`](#insn-00bacd10) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bacd0c::caseD_2` · 推定型 `None`
- [`00bacd0c`](#insn-00bacd0c) → [`00bacf3c`](#insn-00bacf3c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bacd0c::caseD_3` · 推定型 `None`
- [`00bacd0c`](#insn-00bacd0c) → [`00bacf50`](#insn-00bacf50) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bacd0c::caseD_4` · 推定型 `None`
- [`00bacd0c`](#insn-00bacd0c) → [`00bacf68`](#insn-00bacf68) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bacd0c::caseD_5` · 推定型 `None`
- [`00bacd24`](#insn-00bacd24) → [`00bacf84`](#insn-00bacf84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd58`](#insn-00bacd58) → [`00bacfb4`](#insn-00bacfb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd74`](#insn-00bacd74) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bacd78`](#insn-00bacd78) → [`00bacfb4`](#insn-00bacfb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd7c`](#insn-00bacd7c) → [`00bacf88`](#insn-00bacf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd80`](#insn-00bacd80) → [`00bacf90`](#insn-00bacf90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacd94`](#insn-00bacd94) → [`00bac528`](00bac528.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bac528` · 推定シンボル `None` · 推定型 `None`
- [`00bacda0`](#insn-00bacda0) → [`00bacf90`](#insn-00bacf90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacda8`](#insn-00bacda8) → `Stack[-0x6c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacdac`](#insn-00bacdac) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacdb0`](#insn-00bacdb0) → [`00bacde4`](#insn-00bacde4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacdb8`](#insn-00bacdb8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacdbc`](#insn-00bacdbc) → `Stack[-0x6c]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacdcc`](#insn-00bacdcc) → `Stack[-0x6c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacdd0`](#insn-00bacdd0) → [`00bacfc0`](#insn-00bacfc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacde0`](#insn-00bacde0) → [`00bacf90`](#insn-00bacf90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace00`](#insn-00bace00) → [`00bace64`](#insn-00bace64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace34`](#insn-00bace34) → [`00bace6c`](#insn-00bace6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace50`](#insn-00bace50) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bace54`](#insn-00bace54) → [`00bace6c`](#insn-00bace6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace58`](#insn-00bace58) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace5c`](#insn-00bace5c) → [`00bacdd4`](#insn-00bacdd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace60`](#insn-00bace60) → [`00bace78`](#insn-00bace78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace64`](#insn-00bace64) → [`00bacdd4`](#insn-00bacdd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace68`](#insn-00bace68) → [`00bace78`](#insn-00bace78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace70`](#insn-00bace70) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace74`](#insn-00bace74) → [`00bacdd4`](#insn-00bacdd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace80`](#insn-00bace80) → [`00bacdbc`](#insn-00bacdbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace8c`](#insn-00bace8c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace90`](#insn-00bace90) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace94`](#insn-00bace94) → [`00baceb0`](#insn-00baceb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bace98`](#insn-00bace98) → [`00bacf30`](#insn-00bacf30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baceac`](#insn-00baceac) → [`00bacdb4`](#insn-00bacdb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacec0`](#insn-00bacec0) → [`00bace98`](#insn-00bace98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacef4`](#insn-00bacef4) → [`00bacf24`](#insn-00bacf24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf00`](#insn-00bacf00) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf14`](#insn-00bacf14) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bacf18`](#insn-00bacf18) → [`00bacf24`](#insn-00bacf24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf1c`](#insn-00bacf1c) → [`00bace9c`](#insn-00bace9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf20`](#insn-00bacf20) → [`00bacdb8`](#insn-00bacdb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf28`](#insn-00bacf28) → [`00bace9c`](#insn-00bace9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf2c`](#insn-00bacf2c) → [`00bacdb8`](#insn-00bacdb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf38`](#insn-00bacf38) → [`00bacdb8`](#insn-00bacdb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf48`](#insn-00bacf48) → [`00bac528`](00bac528.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bac528` · 推定シンボル `None` · 推定型 `None`
- [`00bacf4c`](#insn-00bacf4c) → [`00bacf90`](#insn-00bacf90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf60`](#insn-00bacf60) → [`00bac7d4`](00bac7d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bac7d4` · 推定シンボル `None` · 推定型 `None`
- [`00bacf64`](#insn-00bacf64) → [`00bacf90`](#insn-00bacf90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf7c`](#insn-00bacf7c) → [`00bac9dc`](00bac9dc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bac9dc` · 推定シンボル `None` · 推定型 `None`
- [`00bacf80`](#insn-00bacf80) → [`00bacf90`](#insn-00bacf90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf84`](#insn-00bacf84) → [`00bacf90`](#insn-00bacf90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf94`](#insn-00bacf94) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf98`](#insn-00bacf98) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf9c`](#insn-00bacf9c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacfa0`](#insn-00bacfa0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacfa4`](#insn-00bacfa4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacfa8`](#insn-00bacfa8) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacfb8`](#insn-00bacfb8) → [`00bacf90`](#insn-00bacf90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacfbc`](#insn-00bacfbc) → [`00bacf88`](#insn-00bacf88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacfcc`](#insn-00bacfcc) → [`00bacf94`](#insn-00bacf94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bacd0c::caseD_0` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baccc0`](#insn-00baccc0)

~~~json
{
  "source": "00baccc0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baccc4`](#insn-00baccc4)

~~~json
{
  "source": "00baccc4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baccc8`](#insn-00baccc8)

~~~json
{
  "source": "00baccc8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacccc`](#insn-00bacccc)

~~~json
{
  "source": "00bacccc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baccd0`](#insn-00baccd0)

~~~json
{
  "source": "00baccd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baccd4`](#insn-00baccd4)

~~~json
{
  "source": "00baccd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baccf0`](#insn-00baccf0)

~~~json
{
  "source": "00baccf0",
  "target": "00bacd84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd00`](#insn-00bacd00)

~~~json
{
  "source": "00bacd00",
  "target": "0030e1c6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e1c6",
  "offset": 0,
  "size": 1,
  "datatype": "byte",
  "bytes": "a1",
  "capture_start": "0030e1c6",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bacd0c`](#insn-00bacd0c)

~~~json
{
  "source": "00bacd0c",
  "target": "00bacf94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd0c`](#insn-00bacd0c)

~~~json
{
  "source": "00bacd0c",
  "target": "00bacd10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd0c`](#insn-00bacd0c)

~~~json
{
  "source": "00bacd0c",
  "target": "00bacf3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd0c`](#insn-00bacd0c)

~~~json
{
  "source": "00bacd0c",
  "target": "00bacf50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd0c`](#insn-00bacd0c)

~~~json
{
  "source": "00bacd0c",
  "target": "00bacf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd24`](#insn-00bacd24)

~~~json
{
  "source": "00bacd24",
  "target": "00bacf84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd58`](#insn-00bacd58)

~~~json
{
  "source": "00bacd58",
  "target": "00bacfb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd74`](#insn-00bacd74)

~~~json
{
  "source": "00bacd74",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bacd78`](#insn-00bacd78)

~~~json
{
  "source": "00bacd78",
  "target": "00bacfb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd7c`](#insn-00bacd7c)

~~~json
{
  "source": "00bacd7c",
  "target": "00bacf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd80`](#insn-00bacd80)

~~~json
{
  "source": "00bacd80",
  "target": "00bacf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacd94`](#insn-00bacd94)

~~~json
{
  "source": "00bacd94",
  "target": "00bac528",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bacda0`](#insn-00bacda0)

~~~json
{
  "source": "00bacda0",
  "target": "00bacf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacda8`](#insn-00bacda8)

~~~json
{
  "source": "00bacda8",
  "target": "Stack[-0x6c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacdac`](#insn-00bacdac)

~~~json
{
  "source": "00bacdac",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacdb0`](#insn-00bacdb0)

~~~json
{
  "source": "00bacdb0",
  "target": "00bacde4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacdb8`](#insn-00bacdb8)

~~~json
{
  "source": "00bacdb8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacdbc`](#insn-00bacdbc)

~~~json
{
  "source": "00bacdbc",
  "target": "Stack[-0x6c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacdcc`](#insn-00bacdcc)

~~~json
{
  "source": "00bacdcc",
  "target": "Stack[-0x6c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacdd0`](#insn-00bacdd0)

~~~json
{
  "source": "00bacdd0",
  "target": "00bacfc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacde0`](#insn-00bacde0)

~~~json
{
  "source": "00bacde0",
  "target": "00bacf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace00`](#insn-00bace00)

~~~json
{
  "source": "00bace00",
  "target": "00bace64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace34`](#insn-00bace34)

~~~json
{
  "source": "00bace34",
  "target": "00bace6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace50`](#insn-00bace50)

~~~json
{
  "source": "00bace50",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bace54`](#insn-00bace54)

~~~json
{
  "source": "00bace54",
  "target": "00bace6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace58`](#insn-00bace58)

~~~json
{
  "source": "00bace58",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace5c`](#insn-00bace5c)

~~~json
{
  "source": "00bace5c",
  "target": "00bacdd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace60`](#insn-00bace60)

~~~json
{
  "source": "00bace60",
  "target": "00bace78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace64`](#insn-00bace64)

~~~json
{
  "source": "00bace64",
  "target": "00bacdd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace68`](#insn-00bace68)

~~~json
{
  "source": "00bace68",
  "target": "00bace78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace70`](#insn-00bace70)

~~~json
{
  "source": "00bace70",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace74`](#insn-00bace74)

~~~json
{
  "source": "00bace74",
  "target": "00bacdd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace80`](#insn-00bace80)

~~~json
{
  "source": "00bace80",
  "target": "00bacdbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace8c`](#insn-00bace8c)

~~~json
{
  "source": "00bace8c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace90`](#insn-00bace90)

~~~json
{
  "source": "00bace90",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace94`](#insn-00bace94)

~~~json
{
  "source": "00bace94",
  "target": "00baceb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bace98`](#insn-00bace98)

~~~json
{
  "source": "00bace98",
  "target": "00bacf30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baceac`](#insn-00baceac)

~~~json
{
  "source": "00baceac",
  "target": "00bacdb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacec0`](#insn-00bacec0)

~~~json
{
  "source": "00bacec0",
  "target": "00bace98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacef4`](#insn-00bacef4)

~~~json
{
  "source": "00bacef4",
  "target": "00bacf24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf00`](#insn-00bacf00)

~~~json
{
  "source": "00bacf00",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf14`](#insn-00bacf14)

~~~json
{
  "source": "00bacf14",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bacf18`](#insn-00bacf18)

~~~json
{
  "source": "00bacf18",
  "target": "00bacf24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf1c`](#insn-00bacf1c)

~~~json
{
  "source": "00bacf1c",
  "target": "00bace9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf20`](#insn-00bacf20)

~~~json
{
  "source": "00bacf20",
  "target": "00bacdb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf28`](#insn-00bacf28)

~~~json
{
  "source": "00bacf28",
  "target": "00bace9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf2c`](#insn-00bacf2c)

~~~json
{
  "source": "00bacf2c",
  "target": "00bacdb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf38`](#insn-00bacf38)

~~~json
{
  "source": "00bacf38",
  "target": "00bacdb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf48`](#insn-00bacf48)

~~~json
{
  "source": "00bacf48",
  "target": "00bac528",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bacf4c`](#insn-00bacf4c)

~~~json
{
  "source": "00bacf4c",
  "target": "00bacf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf60`](#insn-00bacf60)

~~~json
{
  "source": "00bacf60",
  "target": "00bac7d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bacf64`](#insn-00bacf64)

~~~json
{
  "source": "00bacf64",
  "target": "00bacf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf7c`](#insn-00bacf7c)

~~~json
{
  "source": "00bacf7c",
  "target": "00bac9dc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bacf80`](#insn-00bacf80)

~~~json
{
  "source": "00bacf80",
  "target": "00bacf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf84`](#insn-00bacf84)

~~~json
{
  "source": "00bacf84",
  "target": "00bacf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf94`](#insn-00bacf94)

~~~json
{
  "source": "00bacf94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf98`](#insn-00bacf98)

~~~json
{
  "source": "00bacf98",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf9c`](#insn-00bacf9c)

~~~json
{
  "source": "00bacf9c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacfa0`](#insn-00bacfa0)

~~~json
{
  "source": "00bacfa0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacfa4`](#insn-00bacfa4)

~~~json
{
  "source": "00bacfa4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacfa8`](#insn-00bacfa8)

~~~json
{
  "source": "00bacfa8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacfb8`](#insn-00bacfb8)

~~~json
{
  "source": "00bacfb8",
  "target": "00bacf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacfbc`](#insn-00bacfbc)

~~~json
{
  "source": "00bacfbc",
  "target": "00bacf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacfcc`](#insn-00bacfcc)

~~~json
{
  "source": "00bacfcc",
  "target": "00bacf94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
