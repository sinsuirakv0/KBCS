# 008cbabc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0145.md#review-ea795bdd928a67beafa649f083ac6dc3)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `008cbc58`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbc58.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0049.md#compare-265fcfee10051633fb4ee4d85631e0a0)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008cbabc",
  "name": "FUN_008cbabc",
  "size": 688,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9ef2baff6d6527183749618460ade3697358ca32473d3bf57d64f5b745029b82",
  "source_text_sha256": "9ef2baff6d6527183749618460ade3697358ca32473d3bf57d64f5b745029b82",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008cbabc",
        "008cbd6b"
      ]
    ],
    "bytes_sha256": "c2685ffe0c29563128682018093778f82663a4718b5280d9ac51100c33e2c8d9",
    "instruction_count": 172,
    "instruction_bytes": 688,
    "body_bytes": 688,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00440e80](../00440/00440e80.md)
- [00470800](../00470/00470800.md)
- [0047acb4](../0047a/0047acb4.md)
- [0047cd94](../0047c/0047cd94.md)
- [008514b8](../00851/008514b8.md)
- [008bf568](../008bf/008bf568.md)
- [008c3818](../008c3/008c3818.md)
- [008c41ac](../008c4/008c41ac.md)
- [008c4530](../008c4/008c4530.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57c00](../00c57/00c57c00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4294 bytes

~~~c

void FUN_008cbabc(long param_1,undefined8 param_2,int *param_3)

{
  int *piVar1;
  ulong uVar2;
  int *piVar3;
  long *plVar4;
  bool bVar5;
  undefined8 uVar6;
  long lVar7;
  void *__dest;
  long lVar8;
  undefined8 uVar9;
  ulong uVar10;
  ulong uVar11;
  byte bVar12;
  long lVar13;
  void *__src;
  int iVar14;
  int *piVar15;
  byte bVar16;
  long *plVar17;
  long *plVar18;
  
                    /* try { // try from 008cbacc to 009cbbeb has its CatchHandler @ 008cb5a0 */
  iVar14 = *param_3;
  if (iVar14 == 4) {
    lVar13 = *(long *)(param_1 + 8);
    lVar7 = FUN_008514b8();
    *(undefined4 *)(lVar7 + 0x44e134) = 0;
    lVar7 = FUN_008514b8();
    *(undefined8 *)(*(long *)(lVar7 + 0x44ded0) + 0x20) =
         *(undefined8 *)(*(long *)(lVar7 + 0x44ded0) + 0x18);
    plVar17 = *(long **)(lVar13 + 0x28);
    if (plVar17 == (long *)(lVar13 + 0x30)) {
      bVar12 = 0;
    }
    else {
      bVar16 = 0;
      do {
        iVar14 = (int)*(ulong *)((long)plVar17 + 0x1c);
        uVar2 = *(ulong *)((long)plVar17 + 0x1c) & 0xff00000000;
        bVar12 = (uVar2 != 0 && iVar14 == 100) | bVar16;
        if ((uVar2 != 0) && (uVar2 == 0 || iVar14 != 100)) {
          lVar7 = FUN_008514b8();
          lVar7 = *(long *)(lVar7 + 0x44ded0);
          piVar3 = *(int **)(lVar7 + 0x20);
          if (piVar3 < *(int **)(lVar7 + 0x28)) {
            piVar15 = piVar3 + 1;
            *piVar3 = iVar14;
          }
          else {
            __src = *(void **)(lVar7 + 0x18);
            lVar8 = (long)piVar3 - (long)__src >> 2;
            uVar2 = lVar8 + 1;
            if (uVar2 >> 0x3e != 0) {
                    /* WARNING: Subroutine does not return */
              FUN_00470800(lVar7 + 0x18);
            }
                    /* try { // try from 008cbbec to 009cbc03 has its CatchHandler @ 008cccdc */
            uVar10 = (long)*(int **)(lVar7 + 0x28) - (long)__src;
            uVar11 = (long)uVar10 >> 1;
            if (uVar11 <= uVar2) {
              uVar11 = uVar2;
            }
                    /* try { // try from 008cbc04 to 009cbd77 has its CatchHandler @ 008cb5a0 */
            if (0x7ffffffffffffffb < uVar10) {
              uVar11 = 0x3fffffffffffffff;
            }
            if (uVar11 == 0) {
              __dest = (void *)0x0;
            }
            else {
              if (uVar11 >> 0x3e != 0) {
                    /* WARNING: Subroutine does not return */
                FUN_00440e80();
              }
              __dest = (void *)_Znwm(uVar11 << 2);
            }
            piVar1 = (int *)((long)__dest + lVar8 * 4);
            piVar15 = piVar1 + 1;
            *piVar1 = iVar14;
            memcpy(__dest,__src,(long)piVar3 - (long)__src);
            *(void **)(lVar7 + 0x18) = __dest;
            *(int **)(lVar7 + 0x20) = piVar15;
            *(void **)(lVar7 + 0x28) = (void *)((long)__dest + uVar11 * 4);
            if (__src != (void *)0x0) {
              _ZdlPv(__src);
            }
          }
          *(int **)(lVar7 + 0x20) = piVar15;
          lVar7 = FUN_008514b8();
          *(undefined4 *)(lVar7 + 0x44e134) = 1;
          bVar12 = bVar16;
        }
        plVar4 = (long *)plVar17[1];
        plVar18 = plVar17;
        if ((long *)plVar17[1] == (long *)0x0) {
          do {
            plVar17 = (long *)plVar18[2];
            bVar5 = (long *)*plVar17 != plVar18;
            plVar18 = plVar17;
          } while (bVar5);
        }
        else {
          do {
            plVar17 = plVar4;
            plVar4 = (long *)*plVar17;
          } while ((long *)*plVar17 != (long *)0x0);
        }
        bVar16 = bVar12;
      } while (plVar17 != (long *)(lVar13 + 0x30));
    }
    lVar7 = FUN_008514b8();
    lVar8 = FUN_008514b8();
    FUN_008c3818(&DAT_0044dd00 + lVar7,*(undefined4 *)(lVar8 + 0x44e134),1,0xffffffff,bVar12);
    lVar7 = FUN_008514b8();
    FUN_008c41ac(&DAT_0044dd00 + lVar7);
    lVar7 = FUN_008514b8();
    FUN_008c4530(&DAT_0044dd00 + lVar7,1);
    lVar7 = FUN_008514b8();
    *(undefined4 *)(lVar7 + 0x44de74) = 0xffffffff;
    FUN_008bf568(lVar13);
    return;
  }
  if (iVar14 == 3) {
    uVar6 = FUN_0047acb4();
    uVar9 = 0xb;
  }
  else {
    if (iVar14 != 0) {
      return;
    }
    uVar6 = FUN_0047acb4();
    uVar9 = 10;
  }
  FUN_0047cd94(uVar6,uVar9,0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008cbabc"></a> `008cbabc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-008cbac0"></a> `008cbac0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008cbac4"></a> `008cbac4` | `fc 6f 02 a9` | stp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008cbac8"></a> `008cbac8` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008cbacc"></a> `008cbacc` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-008cbad0"></a> `008cbad0` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-008cbad4"></a> `008cbad4` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-008cbad8"></a> `008cbad8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-008cbadc"></a> `008cbadc` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-008cbae0"></a> `008cbae0` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-008cbae4"></a> `008cbae4` | `40 02 00 54` | b.eq 0x008cbb2c | `CONDITIONAL_JUMP`
<a id="insn-008cbae8"></a> `008cbae8` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-008cbaec"></a> `008cbaec` | `a0 00 00 54` | b.eq 0x008cbb00 | `CONDITIONAL_JUMP`
<a id="insn-008cbaf0"></a> `008cbaf0` | `08 0e 00 35` | cbnz w8,0x008cbcb0 | `CONDITIONAL_JUMP`
<a id="insn-008cbaf4"></a> `008cbaf4` | `70 bc ee 97` | bl 0x0047acb4 | `UNCONDITIONAL_CALL`
<a id="insn-008cbaf8"></a> `008cbaf8` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-008cbafc"></a> `008cbafc` | `03 00 00 14` | b 0x008cbb08 | `UNCONDITIONAL_JUMP`
<a id="insn-008cbb00"></a> `008cbb00` | `6d bc ee 97` | bl 0x0047acb4 | `UNCONDITIONAL_CALL`
<a id="insn-008cbb04"></a> `008cbb04` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-008cbb08"></a> `008cbb08` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-008cbb0c"></a> `008cbb0c` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-008cbb10"></a> `008cbb10` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-008cbb14"></a> `008cbb14` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-008cbb18"></a> `008cbb18` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008cbb1c"></a> `008cbb1c` | `fc 6f 42 a9` | ldp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008cbb20"></a> `008cbb20` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008cbb24"></a> `008cbb24` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-008cbb28"></a> `008cbb28` | `9b c4 ee 17` | b 0x0047cd94 | `CALL_TERMINATOR`
<a id="insn-008cbb2c"></a> `008cbb2c` | `13 04 40 f9` | ldr x19,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-008cbb30"></a> `008cbb30` | `62 16 fe 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-008cbb34"></a> `008cbb34` | `88 26 9c 52` | mov w8,#0xe134 | `FALL_THROUGH`
<a id="insn-008cbb38"></a> `008cbb38` | `88 08 a0 72` | movk w8,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-008cbb3c"></a> `008cbb3c` | `1f 68 28 b8` | str wzr,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008cbb40"></a> `008cbb40` | `5e 16 fe 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-008cbb44"></a> `008cbb44` | `08 da 9b 52` | mov w8,#0xded0 | `FALL_THROUGH`
<a id="insn-008cbb48"></a> `008cbb48` | `77 c2 00 91` | add x23,x19,#0x30 | `FALL_THROUGH`
<a id="insn-008cbb4c"></a> `008cbb4c` | `f3 07 00 f9` | str x19,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008cbb50"></a> `008cbb50` | `88 08 a0 72` | movk w8,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-008cbb54"></a> `008cbb54` | `08 68 68 f8` | ldr x8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008cbb58"></a> `008cbb58` | `09 0d 40 f9` | ldr x9,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-008cbb5c"></a> `008cbb5c` | `09 11 00 f9` | str x9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-008cbb60"></a> `008cbb60` | `7c 16 40 f9` | ldr x28,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-008cbb64"></a> `008cbb64` | `9f 03 17 eb` | cmp x28,x23 | `FALL_THROUGH`
<a id="insn-008cbb68"></a> `008cbb68` | `40 0b 00 54` | b.eq 0x008cbcd0 | `CONDITIONAL_JUMP`
<a id="insn-008cbb6c"></a> `008cbb6c` | `14 da 9b 52` | mov w20,#0xded0 | `FALL_THROUGH`
<a id="insn-008cbb70"></a> `008cbb70` | `95 26 9c 52` | mov w21,#0xe134 | `FALL_THROUGH`
<a id="insn-008cbb74"></a> `008cbb74` | `fb 03 1f 2a` | mov w27,wzr | `FALL_THROUGH`
<a id="insn-008cbb78"></a> `008cbb78` | `94 08 a0 72` | movk w20,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-008cbb7c"></a> `008cbb7c` | `95 08 a0 72` | movk w21,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-008cbb80"></a> `008cbb80` | `36 00 80 52` | mov w22,#0x1 | `FALL_THROUGH`
<a id="insn-008cbb84"></a> `008cbb84` | `05 00 00 14` | b 0x008cbb98 | `UNCONDITIONAL_JUMP`
<a id="insn-008cbb88"></a> `008cbb88` | `1f 01 17 eb` | cmp x8,x23 | `FALL_THROUGH`
<a id="insn-008cbb8c"></a> `008cbb8c` | `fb 03 13 2a` | mov w27,w19 | `FALL_THROUGH`
<a id="insn-008cbb90"></a> `008cbb90` | `fc 03 08 aa` | mov x28,x8 | `FALL_THROUGH`
<a id="insn-008cbb94"></a> `008cbb94` | `00 0a 00 54` | b.eq 0x008cbcd4 | `CONDITIONAL_JUMP`
<a id="insn-008cbb98"></a> `008cbb98` | `98 c3 41 f8` | ldur x24,[x28, #0x1c] | `FALL_THROUGH`
<a id="insn-008cbb9c"></a> `008cbb9c` | `1f 93 01 71` | cmp w24,#0x64 | `FALL_THROUGH`
<a id="insn-008cbba0"></a> `008cbba0` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-008cbba4"></a> `008cbba4` | `09 1f 60 f2` | ands x9,x24,#0xff00000000 | `FALL_THROUGH`
<a id="insn-008cbba8"></a> `008cbba8` | `e8 03 88 1a` | csel w8,wzr,w8,eq | `FALL_THROUGH`
<a id="insn-008cbbac"></a> `008cbbac` | `13 01 1b 2a` | orr w19,w8,w27 | `FALL_THROUGH`
<a id="insn-008cbbb0"></a> `008cbbb0` | `89 06 00 b4` | cbz x9,0x008cbc80 | `CONDITIONAL_JUMP`
<a id="insn-008cbbb4"></a> `008cbbb4` | `68 06 00 37` | tbnz w8,#0x0,0x008cbc80 | `CONDITIONAL_JUMP`
<a id="insn-008cbbb8"></a> `008cbbb8` | `40 16 fe 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-008cbbbc"></a> `008cbbbc` | `13 68 74 f8` | ldr x19,[x0, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008cbbc0"></a> `008cbbc0` | `79 22 42 a9` | ldp x25,x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-008cbbc4"></a> `008cbbc4` | `3f 03 08 eb` | cmp x25,x8 | `FALL_THROUGH`
<a id="insn-008cbbc8"></a> `008cbbc8` | `62 00 00 54` | b.cs 0x008cbbd4 | `CONDITIONAL_JUMP`
<a id="insn-008cbbcc"></a> `008cbbcc` | `38 47 00 b8` | str w24,[x25], #0x4 | `FALL_THROUGH`
<a id="insn-008cbbd0"></a> `008cbbd0` | `28 00 00 14` | b 0x008cbc70 | `UNCONDITIONAL_JUMP`
<a id="insn-008cbbd4"></a> `008cbbd4` | `74 82 41 f8` | ldur x20,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-008cbbd8"></a> `008cbbd8` | `35 03 14 cb` | sub x21,x25,x20 | `FALL_THROUGH`
<a id="insn-008cbbdc"></a> `008cbbdc` | `b9 fe 42 93` | asr x25,x21,#0x2 | `FALL_THROUGH`
<a id="insn-008cbbe0"></a> `008cbbe0` | `29 07 00 91` | add x9,x25,#0x1 | `FALL_THROUGH`
<a id="insn-008cbbe4"></a> `008cbbe4` | `2a fd 7e d3` | lsr x10,x9,#0x3e | `FALL_THROUGH`
<a id="insn-008cbbe8"></a> `008cbbe8` | `ca 0b 00 b5` | cbnz x10,0x008cbd60 | `CONDITIONAL_JUMP`
<a id="insn-008cbbec"></a> `008cbbec` | `08 01 14 cb` | sub x8,x8,x20 | `FALL_THROUGH`
<a id="insn-008cbbf0"></a> `008cbbf0` | `0a fd 41 93` | asr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-008cbbf4"></a> `008cbbf4` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-008cbbf8"></a> `008cbbf8` | `49 81 89 9a` | csel x9,x10,x9,hi | `FALL_THROUGH`
<a id="insn-008cbbfc"></a> `008cbbfc` | `ea f3 7e b2` | orr x10,xzr,#0x7ffffffffffffffc | `FALL_THROUGH`
<a id="insn-008cbc00"></a> `008cbc00` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-008cbc04"></a> `008cbc04` | `08 00 f8 92` | mov x8,#0x3fffffffffffffff | `FALL_THROUGH`
<a id="insn-008cbc08"></a> `008cbc08` | `3a 31 88 9a` | csel x26,x9,x8,cc | `FALL_THROUGH`
<a id="insn-008cbc0c"></a> `008cbc0c` | `fa 00 00 b4` | cbz x26,0x008cbc28 | `CONDITIONAL_JUMP`
<a id="insn-008cbc10"></a> `008cbc10` | `48 ff 7e d3` | lsr x8,x26,#0x3e | `FALL_THROUGH`
<a id="insn-008cbc14"></a> `008cbc14` | `a8 0a 00 b5` | cbnz x8,0x008cbd68 | `CONDITIONAL_JUMP`
<a id="insn-008cbc18"></a> `008cbc18` | `40 f7 7e d3` | lsl x0,x26,#0x2 | `FALL_THROUGH`
<a id="insn-008cbc1c"></a> `008cbc1c` | `9d 2f 0e 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-008cbc20"></a> `008cbc20` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-008cbc24"></a> `008cbc24` | `02 00 00 14` | b 0x008cbc2c | `UNCONDITIONAL_JUMP`
<a id="insn-008cbc28"></a> `008cbc28` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-008cbc2c"></a> `008cbc2c` | `d9 0a 19 8b` | add x25,x22,x25, LSL #0x2 | `FALL_THROUGH`
<a id="insn-008cbc30"></a> `008cbc30` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008cbc34"></a> `008cbc34` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-008cbc38"></a> `008cbc38` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-008cbc3c"></a> `008cbc3c` | `da 0a 1a 8b` | add x26,x22,x26, LSL #0x2 | `FALL_THROUGH`
<a id="insn-008cbc40"></a> `008cbc40` | `38 47 00 b8` | str w24,[x25], #0x4 | `FALL_THROUGH`
<a id="insn-008cbc44"></a> `008cbc44` | `ef 2f 0e 94` | bl 0x00c57c00 | `UNCONDITIONAL_CALL`
<a id="insn-008cbc48"></a> `008cbc48` | `76 e6 01 a9` | stp x22,x25,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-008cbc4c"></a> `008cbc4c` | `7a 16 00 f9` | str x26,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-008cbc50"></a> `008cbc50` | `74 00 00 b4` | cbz x20,0x008cbc5c | `CONDITIONAL_JUMP`
<a id="insn-008cbc54"></a> `008cbc54` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-008cbc58"></a> `008cbc58` | `96 2f 0e 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-008cbc5c"></a> `008cbc5c` | `14 da 9b 52` | mov w20,#0xded0 | `FALL_THROUGH`
<a id="insn-008cbc60"></a> `008cbc60` | `95 26 9c 52` | mov w21,#0xe134 | `FALL_THROUGH`
<a id="insn-008cbc64"></a> `008cbc64` | `36 00 80 52` | mov w22,#0x1 | `FALL_THROUGH`
<a id="insn-008cbc68"></a> `008cbc68` | `94 08 a0 72` | movk w20,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-008cbc6c"></a> `008cbc6c` | `95 08 a0 72` | movk w21,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-008cbc70"></a> `008cbc70` | `79 12 00 f9` | str x25,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-008cbc74"></a> `008cbc74` | `11 16 fe 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-008cbc78"></a> `008cbc78` | `f3 03 1b 2a` | mov w19,w27 | `FALL_THROUGH`
<a id="insn-008cbc7c"></a> `008cbc7c` | `16 68 35 b8` | str w22,[x0, x21, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008cbc80"></a> `008cbc80` | `89 07 40 f9` | ldr x9,[x28, #0x8] | `FALL_THROUGH`
<a id="insn-008cbc84"></a> `008cbc84` | `a9 00 00 b4` | cbz x9,0x008cbc98 | `CONDITIONAL_JUMP`
<a id="insn-008cbc88"></a> `008cbc88` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-008cbc8c"></a> `008cbc8c` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-008cbc90"></a> `008cbc90` | `c9 ff ff b5` | cbnz x9,0x008cbc88 | `CONDITIONAL_JUMP`
<a id="insn-008cbc94"></a> `008cbc94` | `bd ff ff 17` | b 0x008cbb88 | `UNCONDITIONAL_JUMP`
<a id="insn-008cbc98"></a> `008cbc98` | `88 0b 40 f9` | ldr x8,[x28, #0x10] | `FALL_THROUGH`
<a id="insn-008cbc9c"></a> `008cbc9c` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-008cbca0"></a> `008cbca0` | `3f 01 1c eb` | cmp x9,x28 | `FALL_THROUGH`
<a id="insn-008cbca4"></a> `008cbca4` | `fc 03 08 aa` | mov x28,x8 | `FALL_THROUGH`
<a id="insn-008cbca8"></a> `008cbca8` | `81 ff ff 54` | b.ne 0x008cbc98 | `CONDITIONAL_JUMP`
<a id="insn-008cbcac"></a> `008cbcac` | `b7 ff ff 17` | b 0x008cbb88 | `UNCONDITIONAL_JUMP`
<a id="insn-008cbcb0"></a> `008cbcb0` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-008cbcb4"></a> `008cbcb4` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-008cbcb8"></a> `008cbcb8` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-008cbcbc"></a> `008cbcbc` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008cbcc0"></a> `008cbcc0` | `fc 6f 42 a9` | ldp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008cbcc4"></a> `008cbcc4` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008cbcc8"></a> `008cbcc8` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-008cbccc"></a> `008cbccc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-008cbcd0"></a> `008cbcd0` | `f3 03 1f 2a` | mov w19,wzr | `FALL_THROUGH`
<a id="insn-008cbcd4"></a> `008cbcd4` | `f9 15 fe 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-008cbcd8"></a> `008cbcd8` | `15 a0 9b 52` | mov w21,#0xdd00 | `FALL_THROUGH`
<a id="insn-008cbcdc"></a> `008cbcdc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-008cbce0"></a> `008cbce0` | `95 08 a0 72` | movk w21,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-008cbce4"></a> `008cbce4` | `f5 15 fe 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-008cbce8"></a> `008cbce8` | `88 26 9c 52` | mov w8,#0xe134 | `FALL_THROUGH`
<a id="insn-008cbcec"></a> `008cbcec` | `64 02 00 12` | and w4,w19,#0x1 | `FALL_THROUGH`
<a id="insn-008cbcf0"></a> `008cbcf0` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-008cbcf4"></a> `008cbcf4` | `88 08 a0 72` | movk w8,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-008cbcf8"></a> `008cbcf8` | `03 00 80 12` | mov w3,#0xffffffff | `FALL_THROUGH`
<a id="insn-008cbcfc"></a> `008cbcfc` | `13 00 80 12` | mov w19,#0xffffffff | `FALL_THROUGH`
<a id="insn-008cbd00"></a> `008cbd00` | `01 68 68 b8` | ldr w1,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008cbd04"></a> `008cbd04` | `80 02 15 8b` | add x0,x20,x21 | `FALL_THROUGH`
<a id="insn-008cbd08"></a> `008cbd08` | `c4 de ff 97` | bl 0x008c3818 | `UNCONDITIONAL_CALL`
<a id="insn-008cbd0c"></a> `008cbd0c` | `eb 15 fe 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-008cbd10"></a> `008cbd10` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-008cbd14"></a> `008cbd14` | `26 e1 ff 97` | bl 0x008c41ac | `UNCONDITIONAL_CALL`
<a id="insn-008cbd18"></a> `008cbd18` | `e8 15 fe 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-008cbd1c"></a> `008cbd1c` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-008cbd20"></a> `008cbd20` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-008cbd24"></a> `008cbd24` | `03 e2 ff 97` | bl 0x008c4530 | `UNCONDITIONAL_CALL`
<a id="insn-008cbd28"></a> `008cbd28` | `e4 15 fe 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-008cbd2c"></a> `008cbd2c` | `89 ce 9b 52` | mov w9,#0xde74 | `FALL_THROUGH`
<a id="insn-008cbd30"></a> `008cbd30` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-008cbd34"></a> `008cbd34` | `e0 07 40 f9` | ldr x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008cbd38"></a> `008cbd38` | `89 08 a0 72` | movk w9,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-008cbd3c"></a> `008cbd3c` | `13 69 29 b8` | str w19,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008cbd40"></a> `008cbd40` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-008cbd44"></a> `008cbd44` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-008cbd48"></a> `008cbd48` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-008cbd4c"></a> `008cbd4c` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008cbd50"></a> `008cbd50` | `fc 6f 42 a9` | ldp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008cbd54"></a> `008cbd54` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008cbd58"></a> `008cbd58` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-008cbd5c"></a> `008cbd5c` | `03 ce ff 17` | b 0x008bf568 | `CALL_TERMINATOR`
<a id="insn-008cbd60"></a> `008cbd60` | `60 62 00 91` | add x0,x19,#0x18 | `FALL_THROUGH`
<a id="insn-008cbd64"></a> `008cbd64` | `a7 92 ee 97` | bl 0x00470800 | `CALL_TERMINATOR`
<a id="insn-008cbd68"></a> `008cbd68` | `46 d4 ed 97` | bl 0x00440e80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008cbabc`](#insn-008cbabc) 範囲 `[['008cbabc', '008cbacb']]`
  - `FALL_THROUGH` [`008cbac8`](#insn-008cbac8) → [`008cbacc`](#insn-008cbacc)
- ブロック [`008cbacc`](#insn-008cbacc) 範囲 `[['008cbacc', '008cbae7']]`
  - `CONDITIONAL_JUMP` [`008cbae4`](#insn-008cbae4) → [`008cbb2c`](#insn-008cbb2c)
  - `FALL_THROUGH` [`008cbae4`](#insn-008cbae4) → [`008cbae8`](#insn-008cbae8)
- ブロック [`008cbae8`](#insn-008cbae8) 範囲 `[['008cbae8', '008cbaef']]`
  - `CONDITIONAL_JUMP` [`008cbaec`](#insn-008cbaec) → [`008cbb00`](#insn-008cbb00)
  - `FALL_THROUGH` [`008cbaec`](#insn-008cbaec) → [`008cbaf0`](#insn-008cbaf0)
- ブロック [`008cbaf0`](#insn-008cbaf0) 範囲 `[['008cbaf0', '008cbaf3']]`
  - `CONDITIONAL_JUMP` [`008cbaf0`](#insn-008cbaf0) → [`008cbcb0`](#insn-008cbcb0)
  - `FALL_THROUGH` [`008cbaf0`](#insn-008cbaf0) → [`008cbaf4`](#insn-008cbaf4)
- ブロック [`008cbaf4`](#insn-008cbaf4) 範囲 `[['008cbaf4', '008cbaff']]`
  - `UNCONDITIONAL_JUMP` [`008cbafc`](#insn-008cbafc) → [`008cbb08`](#insn-008cbb08)
- ブロック [`008cbb00`](#insn-008cbb00) 範囲 `[['008cbb00', '008cbb07']]`
  - `FALL_THROUGH` [`008cbb04`](#insn-008cbb04) → [`008cbb08`](#insn-008cbb08)
- ブロック [`008cbb08`](#insn-008cbb08) 範囲 `[['008cbb08', '008cbb2b']]`
- ブロック [`008cbb2c`](#insn-008cbb2c) 範囲 `[['008cbb2c', '008cbb6b']]`
  - `CONDITIONAL_JUMP` [`008cbb68`](#insn-008cbb68) → [`008cbcd0`](#insn-008cbcd0)
  - `FALL_THROUGH` [`008cbb68`](#insn-008cbb68) → [`008cbb6c`](#insn-008cbb6c)
- ブロック [`008cbb6c`](#insn-008cbb6c) 範囲 `[['008cbb6c', '008cbb87']]`
  - `UNCONDITIONAL_JUMP` [`008cbb84`](#insn-008cbb84) → [`008cbb98`](#insn-008cbb98)
- ブロック [`008cbb88`](#insn-008cbb88) 範囲 `[['008cbb88', '008cbb97']]`
  - `CONDITIONAL_JUMP` [`008cbb94`](#insn-008cbb94) → [`008cbcd4`](#insn-008cbcd4)
  - `FALL_THROUGH` [`008cbb94`](#insn-008cbb94) → [`008cbb98`](#insn-008cbb98)
- ブロック [`008cbb98`](#insn-008cbb98) 範囲 `[['008cbb98', '008cbbb3']]`
  - `CONDITIONAL_JUMP` [`008cbbb0`](#insn-008cbbb0) → [`008cbc80`](#insn-008cbc80)
  - `FALL_THROUGH` [`008cbbb0`](#insn-008cbbb0) → [`008cbbb4`](#insn-008cbbb4)
- ブロック [`008cbbb4`](#insn-008cbbb4) 範囲 `[['008cbbb4', '008cbbb7']]`
  - `CONDITIONAL_JUMP` [`008cbbb4`](#insn-008cbbb4) → [`008cbc80`](#insn-008cbc80)
  - `FALL_THROUGH` [`008cbbb4`](#insn-008cbbb4) → [`008cbbb8`](#insn-008cbbb8)
- ブロック [`008cbbb8`](#insn-008cbbb8) 範囲 `[['008cbbb8', '008cbbcb']]`
  - `CONDITIONAL_JUMP` [`008cbbc8`](#insn-008cbbc8) → [`008cbbd4`](#insn-008cbbd4)
  - `FALL_THROUGH` [`008cbbc8`](#insn-008cbbc8) → [`008cbbcc`](#insn-008cbbcc)
- ブロック [`008cbbcc`](#insn-008cbbcc) 範囲 `[['008cbbcc', '008cbbd3']]`
  - `UNCONDITIONAL_JUMP` [`008cbbd0`](#insn-008cbbd0) → [`008cbc70`](#insn-008cbc70)
- ブロック [`008cbbd4`](#insn-008cbbd4) 範囲 `[['008cbbd4', '008cbbeb']]`
  - `CONDITIONAL_JUMP` [`008cbbe8`](#insn-008cbbe8) → [`008cbd60`](#insn-008cbd60)
  - `FALL_THROUGH` [`008cbbe8`](#insn-008cbbe8) → [`008cbbec`](#insn-008cbbec)
- ブロック [`008cbbec`](#insn-008cbbec) 範囲 `[['008cbbec', '008cbc03']]`
  - `FALL_THROUGH` [`008cbc00`](#insn-008cbc00) → [`008cbc04`](#insn-008cbc04)
- ブロック [`008cbc04`](#insn-008cbc04) 範囲 `[['008cbc04', '008cbc0f']]`
  - `CONDITIONAL_JUMP` [`008cbc0c`](#insn-008cbc0c) → [`008cbc28`](#insn-008cbc28)
  - `FALL_THROUGH` [`008cbc0c`](#insn-008cbc0c) → [`008cbc10`](#insn-008cbc10)
- ブロック [`008cbc10`](#insn-008cbc10) 範囲 `[['008cbc10', '008cbc17']]`
  - `CONDITIONAL_JUMP` [`008cbc14`](#insn-008cbc14) → [`008cbd68`](#insn-008cbd68)
  - `FALL_THROUGH` [`008cbc14`](#insn-008cbc14) → [`008cbc18`](#insn-008cbc18)
- ブロック [`008cbc18`](#insn-008cbc18) 範囲 `[['008cbc18', '008cbc27']]`
  - `UNCONDITIONAL_JUMP` [`008cbc24`](#insn-008cbc24) → [`008cbc2c`](#insn-008cbc2c)
- ブロック [`008cbc28`](#insn-008cbc28) 範囲 `[['008cbc28', '008cbc2b']]`
  - `FALL_THROUGH` [`008cbc28`](#insn-008cbc28) → [`008cbc2c`](#insn-008cbc2c)
- ブロック [`008cbc2c`](#insn-008cbc2c) 範囲 `[['008cbc2c', '008cbc53']]`
  - `CONDITIONAL_JUMP` [`008cbc50`](#insn-008cbc50) → [`008cbc5c`](#insn-008cbc5c)
  - `FALL_THROUGH` [`008cbc50`](#insn-008cbc50) → [`008cbc54`](#insn-008cbc54)
- ブロック [`008cbc54`](#insn-008cbc54) 範囲 `[['008cbc54', '008cbc5b']]`
  - `FALL_THROUGH` [`008cbc58`](#insn-008cbc58) → [`008cbc5c`](#insn-008cbc5c)
- ブロック [`008cbc5c`](#insn-008cbc5c) 範囲 `[['008cbc5c', '008cbc6f']]`
  - `FALL_THROUGH` [`008cbc6c`](#insn-008cbc6c) → [`008cbc70`](#insn-008cbc70)
- ブロック [`008cbc70`](#insn-008cbc70) 範囲 `[['008cbc70', '008cbc7f']]`
  - `FALL_THROUGH` [`008cbc7c`](#insn-008cbc7c) → [`008cbc80`](#insn-008cbc80)
- ブロック [`008cbc80`](#insn-008cbc80) 範囲 `[['008cbc80', '008cbc87']]`
  - `CONDITIONAL_JUMP` [`008cbc84`](#insn-008cbc84) → [`008cbc98`](#insn-008cbc98)
  - `FALL_THROUGH` [`008cbc84`](#insn-008cbc84) → [`008cbc88`](#insn-008cbc88)
- ブロック [`008cbc88`](#insn-008cbc88) 範囲 `[['008cbc88', '008cbc93']]`
  - `CONDITIONAL_JUMP` [`008cbc90`](#insn-008cbc90) → [`008cbc88`](#insn-008cbc88)
  - `FALL_THROUGH` [`008cbc90`](#insn-008cbc90) → [`008cbc94`](#insn-008cbc94)
- ブロック [`008cbc94`](#insn-008cbc94) 範囲 `[['008cbc94', '008cbc97']]`
  - `UNCONDITIONAL_JUMP` [`008cbc94`](#insn-008cbc94) → [`008cbb88`](#insn-008cbb88)
- ブロック [`008cbc98`](#insn-008cbc98) 範囲 `[['008cbc98', '008cbcab']]`
  - `CONDITIONAL_JUMP` [`008cbca8`](#insn-008cbca8) → [`008cbc98`](#insn-008cbc98)
  - `FALL_THROUGH` [`008cbca8`](#insn-008cbca8) → [`008cbcac`](#insn-008cbcac)
- ブロック [`008cbcac`](#insn-008cbcac) 範囲 `[['008cbcac', '008cbcaf']]`
  - `UNCONDITIONAL_JUMP` [`008cbcac`](#insn-008cbcac) → [`008cbb88`](#insn-008cbb88)
- ブロック [`008cbcb0`](#insn-008cbcb0) 範囲 `[['008cbcb0', '008cbccf']]`
- ブロック [`008cbcd0`](#insn-008cbcd0) 範囲 `[['008cbcd0', '008cbcd3']]`
  - `FALL_THROUGH` [`008cbcd0`](#insn-008cbcd0) → [`008cbcd4`](#insn-008cbcd4)
- ブロック [`008cbcd4`](#insn-008cbcd4) 範囲 `[['008cbcd4', '008cbd5f']]`
- ブロック [`008cbd60`](#insn-008cbd60) 範囲 `[['008cbd60', '008cbd67']]`
- ブロック [`008cbd68`](#insn-008cbd68) 範囲 `[['008cbd68', '008cbd6b']]`

## 命令位置別の参照

- [`008cbac0`](#insn-008cbac0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbac4`](#insn-008cbac4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbac8`](#insn-008cbac8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbacc`](#insn-008cbacc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbad0`](#insn-008cbad0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbad4`](#insn-008cbad4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbae4`](#insn-008cbae4) → [`008cbb2c`](#insn-008cbb2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbaec`](#insn-008cbaec) → [`008cbb00`](#insn-008cbb00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbaf0`](#insn-008cbaf0) → [`008cbcb0`](#insn-008cbcb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbaf4`](#insn-008cbaf4) → [`0047acb4`](../0047a/0047acb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acb4` · 推定シンボル `None` · 推定型 `None`
- [`008cbafc`](#insn-008cbafc) → [`008cbb08`](#insn-008cbb08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbb00`](#insn-008cbb00) → [`0047acb4`](../0047a/0047acb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acb4` · 推定シンボル `None` · 推定型 `None`
- [`008cbb0c`](#insn-008cbb0c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbb10`](#insn-008cbb10) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbb14`](#insn-008cbb14) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbb18`](#insn-008cbb18) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbb1c`](#insn-008cbb1c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbb20`](#insn-008cbb20) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbb28`](#insn-008cbb28) → [`0047cd94`](../0047c/0047cd94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cd94` · 推定シンボル `None` · 推定型 `None`
- [`008cbb30`](#insn-008cbb30) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`008cbb40`](#insn-008cbb40) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`008cbb4c`](#insn-008cbb4c) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbb68`](#insn-008cbb68) → [`008cbcd0`](#insn-008cbcd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbb84`](#insn-008cbb84) → [`008cbb98`](#insn-008cbb98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbb94`](#insn-008cbb94) → [`008cbcd4`](#insn-008cbcd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbbb0`](#insn-008cbbb0) → [`008cbc80`](#insn-008cbc80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbbb4`](#insn-008cbbb4) → [`008cbc80`](#insn-008cbc80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbbb8`](#insn-008cbbb8) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`008cbbc8`](#insn-008cbbc8) → [`008cbbd4`](#insn-008cbbd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbbd0`](#insn-008cbbd0) → [`008cbc70`](#insn-008cbc70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbbe8`](#insn-008cbbe8) → [`008cbd60`](#insn-008cbd60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbc0c`](#insn-008cbc0c) → [`008cbc28`](#insn-008cbc28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbc14`](#insn-008cbc14) → [`008cbd68`](#insn-008cbd68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbc1c`](#insn-008cbc1c) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`008cbc24`](#insn-008cbc24) → [`008cbc2c`](#insn-008cbc2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbc44`](#insn-008cbc44) → [`00c57c00`](../00c57/00c57c00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c00` · 推定シンボル `None` · 推定型 `None`
- [`008cbc50`](#insn-008cbc50) → [`008cbc5c`](#insn-008cbc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbc58`](#insn-008cbc58) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`008cbc74`](#insn-008cbc74) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`008cbc84`](#insn-008cbc84) → [`008cbc98`](#insn-008cbc98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbc90`](#insn-008cbc90) → [`008cbc88`](#insn-008cbc88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbc94`](#insn-008cbc94) → [`008cbb88`](#insn-008cbb88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbca8`](#insn-008cbca8) → [`008cbc98`](#insn-008cbc98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbcac`](#insn-008cbcac) → [`008cbb88`](#insn-008cbb88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbcb0`](#insn-008cbcb0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbcb4`](#insn-008cbcb4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbcb8`](#insn-008cbcb8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbcbc`](#insn-008cbcbc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbcc0`](#insn-008cbcc0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbcc4`](#insn-008cbcc4) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbcd4`](#insn-008cbcd4) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`008cbce4`](#insn-008cbce4) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`008cbd08`](#insn-008cbd08) → [`008c3818`](../008c3/008c3818.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008c3818` · 推定シンボル `None` · 推定型 `None`
- [`008cbd0c`](#insn-008cbd0c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`008cbd14`](#insn-008cbd14) → [`008c41ac`](../008c4/008c41ac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008c41ac` · 推定シンボル `None` · 推定型 `None`
- [`008cbd18`](#insn-008cbd18) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`008cbd24`](#insn-008cbd24) → [`008c4530`](../008c4/008c4530.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008c4530` · 推定シンボル `None` · 推定型 `None`
- [`008cbd28`](#insn-008cbd28) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`008cbd34`](#insn-008cbd34) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbd40`](#insn-008cbd40) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbd44`](#insn-008cbd44) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbd48`](#insn-008cbd48) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbd4c`](#insn-008cbd4c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbd50`](#insn-008cbd50) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbd54`](#insn-008cbd54) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbd5c`](#insn-008cbd5c) → [`008bf568`](../008bf/008bf568.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008bf568` · 推定シンボル `None` · 推定型 `None`
- [`008cbd64`](#insn-008cbd64) → [`00470800`](../00470/00470800.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00470800` · 推定シンボル `None` · 推定型 `None`
- [`008cbd68`](#insn-008cbd68) → [`00440e80`](../00440/00440e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00440e80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008cbac0`](#insn-008cbac0)

~~~json
{
  "source": "008cbac0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbac4`](#insn-008cbac4)

~~~json
{
  "source": "008cbac4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbac8`](#insn-008cbac8)

~~~json
{
  "source": "008cbac8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbacc`](#insn-008cbacc)

~~~json
{
  "source": "008cbacc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbad0`](#insn-008cbad0)

~~~json
{
  "source": "008cbad0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbad4`](#insn-008cbad4)

~~~json
{
  "source": "008cbad4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbae4`](#insn-008cbae4)

~~~json
{
  "source": "008cbae4",
  "target": "008cbb2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbaec`](#insn-008cbaec)

~~~json
{
  "source": "008cbaec",
  "target": "008cbb00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbaf0`](#insn-008cbaf0)

~~~json
{
  "source": "008cbaf0",
  "target": "008cbcb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbaf4`](#insn-008cbaf4)

~~~json
{
  "source": "008cbaf4",
  "target": "0047acb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbafc`](#insn-008cbafc)

~~~json
{
  "source": "008cbafc",
  "target": "008cbb08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbb00`](#insn-008cbb00)

~~~json
{
  "source": "008cbb00",
  "target": "0047acb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbb0c`](#insn-008cbb0c)

~~~json
{
  "source": "008cbb0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbb10`](#insn-008cbb10)

~~~json
{
  "source": "008cbb10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbb14`](#insn-008cbb14)

~~~json
{
  "source": "008cbb14",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbb18`](#insn-008cbb18)

~~~json
{
  "source": "008cbb18",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbb1c`](#insn-008cbb1c)

~~~json
{
  "source": "008cbb1c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbb20`](#insn-008cbb20)

~~~json
{
  "source": "008cbb20",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbb28`](#insn-008cbb28)

~~~json
{
  "source": "008cbb28",
  "target": "0047cd94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbb30`](#insn-008cbb30)

~~~json
{
  "source": "008cbb30",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbb40`](#insn-008cbb40)

~~~json
{
  "source": "008cbb40",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbb4c`](#insn-008cbb4c)

~~~json
{
  "source": "008cbb4c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbb68`](#insn-008cbb68)

~~~json
{
  "source": "008cbb68",
  "target": "008cbcd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbb84`](#insn-008cbb84)

~~~json
{
  "source": "008cbb84",
  "target": "008cbb98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbb94`](#insn-008cbb94)

~~~json
{
  "source": "008cbb94",
  "target": "008cbcd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbbb0`](#insn-008cbbb0)

~~~json
{
  "source": "008cbbb0",
  "target": "008cbc80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbbb4`](#insn-008cbbb4)

~~~json
{
  "source": "008cbbb4",
  "target": "008cbc80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbbb8`](#insn-008cbbb8)

~~~json
{
  "source": "008cbbb8",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbbc8`](#insn-008cbbc8)

~~~json
{
  "source": "008cbbc8",
  "target": "008cbbd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbbd0`](#insn-008cbbd0)

~~~json
{
  "source": "008cbbd0",
  "target": "008cbc70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbbe8`](#insn-008cbbe8)

~~~json
{
  "source": "008cbbe8",
  "target": "008cbd60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbc0c`](#insn-008cbc0c)

~~~json
{
  "source": "008cbc0c",
  "target": "008cbc28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbc14`](#insn-008cbc14)

~~~json
{
  "source": "008cbc14",
  "target": "008cbd68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbc1c`](#insn-008cbc1c)

~~~json
{
  "source": "008cbc1c",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbc24`](#insn-008cbc24)

~~~json
{
  "source": "008cbc24",
  "target": "008cbc2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbc44`](#insn-008cbc44)

~~~json
{
  "source": "008cbc44",
  "target": "00c57c00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbc50`](#insn-008cbc50)

~~~json
{
  "source": "008cbc50",
  "target": "008cbc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbc58`](#insn-008cbc58)

~~~json
{
  "source": "008cbc58",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbc74`](#insn-008cbc74)

~~~json
{
  "source": "008cbc74",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbc84`](#insn-008cbc84)

~~~json
{
  "source": "008cbc84",
  "target": "008cbc98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbc90`](#insn-008cbc90)

~~~json
{
  "source": "008cbc90",
  "target": "008cbc88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbc94`](#insn-008cbc94)

~~~json
{
  "source": "008cbc94",
  "target": "008cbb88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbca8`](#insn-008cbca8)

~~~json
{
  "source": "008cbca8",
  "target": "008cbc98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbcac`](#insn-008cbcac)

~~~json
{
  "source": "008cbcac",
  "target": "008cbb88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbcb0`](#insn-008cbcb0)

~~~json
{
  "source": "008cbcb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbcb4`](#insn-008cbcb4)

~~~json
{
  "source": "008cbcb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbcb8`](#insn-008cbcb8)

~~~json
{
  "source": "008cbcb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbcbc`](#insn-008cbcbc)

~~~json
{
  "source": "008cbcbc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbcc0`](#insn-008cbcc0)

~~~json
{
  "source": "008cbcc0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbcc4`](#insn-008cbcc4)

~~~json
{
  "source": "008cbcc4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbcd4`](#insn-008cbcd4)

~~~json
{
  "source": "008cbcd4",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbce4`](#insn-008cbce4)

~~~json
{
  "source": "008cbce4",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbd08`](#insn-008cbd08)

~~~json
{
  "source": "008cbd08",
  "target": "008c3818",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbd0c`](#insn-008cbd0c)

~~~json
{
  "source": "008cbd0c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbd14`](#insn-008cbd14)

~~~json
{
  "source": "008cbd14",
  "target": "008c41ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbd18`](#insn-008cbd18)

~~~json
{
  "source": "008cbd18",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbd24`](#insn-008cbd24)

~~~json
{
  "source": "008cbd24",
  "target": "008c4530",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbd28`](#insn-008cbd28)

~~~json
{
  "source": "008cbd28",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbd34`](#insn-008cbd34)

~~~json
{
  "source": "008cbd34",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbd40`](#insn-008cbd40)

~~~json
{
  "source": "008cbd40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbd44`](#insn-008cbd44)

~~~json
{
  "source": "008cbd44",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbd48`](#insn-008cbd48)

~~~json
{
  "source": "008cbd48",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbd4c`](#insn-008cbd4c)

~~~json
{
  "source": "008cbd4c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbd50`](#insn-008cbd50)

~~~json
{
  "source": "008cbd50",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbd54`](#insn-008cbd54)

~~~json
{
  "source": "008cbd54",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbd5c`](#insn-008cbd5c)

~~~json
{
  "source": "008cbd5c",
  "target": "008bf568",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbd64`](#insn-008cbd64)

~~~json
{
  "source": "008cbd64",
  "target": "00470800",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbd68`](#insn-008cbd68)

~~~json
{
  "source": "008cbd68",
  "target": "00440e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
