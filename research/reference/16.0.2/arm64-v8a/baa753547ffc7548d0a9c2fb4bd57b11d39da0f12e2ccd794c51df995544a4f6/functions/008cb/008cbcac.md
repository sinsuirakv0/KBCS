# 008cbcac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `008cbc58`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbc58.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0051.md#compare-47c22a5806e70127da9c11552ad44a07)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `008ccc58`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008cc/008ccc58.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0052.md#compare-695642282e7e861ec51bde26f65c87d8)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008cbcac",
  "name": "FUN_008cbcac",
  "size": 688,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3936043747e230f0c3c2ec5cf279e5e49685ab845d871b9da34b161464f467c8",
  "source_text_sha256": "3936043747e230f0c3c2ec5cf279e5e49685ab845d871b9da34b161464f467c8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008cbcac",
        "008cbf5b"
      ]
    ],
    "bytes_sha256": "47b9ade5e45065778c190fa81f9559f80908ce97774dbeb427af42ae02368178",
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

- [00440f00](../00440/00440f00.md)
- [00470880](../00470/00470880.md)
- [0047ad34](../0047a/0047ad34.md)
- [0047ce14](../0047c/0047ce14.md)
- [00851550](../00851/00851550.md)
- [008bf604](../008bf/008bf604.md)
- [008c38b4](../008c3/008c38b4.md)
- [008c42e4](../008c4/008c42e4.md)
- [008c4668](../008c4/008c4668.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c580d0](../00c58/00c580d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4391 bytes

~~~c

void FUN_008cbcac(long param_1,undefined8 param_2,int *param_3)

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
  
  iVar14 = *param_3;
  if (iVar14 == 4) {
    lVar13 = *(long *)(param_1 + 8);
    lVar7 = FUN_00851550();
    *(undefined4 *)(lVar7 + 0x44e134) = 0;
    lVar7 = FUN_00851550();
    *(undefined8 *)(*(long *)(&DAT_0044ded0 + lVar7) + 0x20) =
         *(undefined8 *)(*(long *)(&DAT_0044ded0 + lVar7) + 0x18);
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
          lVar7 = FUN_00851550();
          lVar7 = *(long *)(&DAT_0044ded0 + lVar7);
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
              FUN_00470880(lVar7 + 0x18);
            }
            uVar10 = (long)*(int **)(lVar7 + 0x28) - (long)__src;
            uVar11 = (long)uVar10 >> 1;
            if (uVar11 <= uVar2) {
              uVar11 = uVar2;
            }
            if (0x7ffffffffffffffb < uVar10) {
              uVar11 = 0x3fffffffffffffff;
            }
            if (uVar11 == 0) {
              __dest = (void *)0x0;
            }
            else {
              if (uVar11 >> 0x3e != 0) {
                    /* WARNING: Subroutine does not return */
                FUN_00440f00();
              }
              __dest = (void *)_Znwm(uVar11 << 2);
                    /* try { // try from 008cbe10 to 009cbe87 has its CatchHandler @ 008ccdb4 */
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
          lVar7 = FUN_00851550();
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
    lVar7 = FUN_00851550();
    lVar8 = FUN_00851550();
    FUN_008c38b4(lVar7 + 0x44dd00,*(undefined4 *)(lVar8 + 0x44e134),1,0xffffffff,bVar12);
    lVar7 = FUN_00851550();
    FUN_008c42e4(lVar7 + 0x44dd00);
                    /* try { // try from 008cbf08 to 009cbf0b has its CatchHandler @ 008ccdfc */
    lVar7 = FUN_00851550();
    FUN_008c4668(lVar7 + 0x44dd00,1);
    lVar7 = FUN_00851550();
                    /* try { // try from 008cbf1c to 009cbf1f has its CatchHandler @ 008cce00 */
                    /* try { // try from 008cbf20 to 009cbf53 has its CatchHandler @ 008ccf34 */
    *(undefined4 *)(lVar7 + 0x44de74) = 0xffffffff;
    FUN_008bf604(lVar13);
    return;
  }
  if (iVar14 == 3) {
    uVar6 = FUN_0047ad34();
    uVar9 = 0xb;
  }
  else {
    if (iVar14 != 0) {
      return;
    }
    uVar6 = FUN_0047ad34();
    uVar9 = 10;
  }
  FUN_0047ce14(uVar6,uVar9,0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008cbcac"></a> `008cbcac` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-008cbcb0"></a> `008cbcb0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008cbcb4"></a> `008cbcb4` | `fc 6f 02 a9` | stp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008cbcb8"></a> `008cbcb8` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008cbcbc"></a> `008cbcbc` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-008cbcc0"></a> `008cbcc0` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-008cbcc4"></a> `008cbcc4` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-008cbcc8"></a> `008cbcc8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-008cbccc"></a> `008cbccc` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-008cbcd0"></a> `008cbcd0` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-008cbcd4"></a> `008cbcd4` | `40 02 00 54` | b.eq 0x008cbd1c | `CONDITIONAL_JUMP`
<a id="insn-008cbcd8"></a> `008cbcd8` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-008cbcdc"></a> `008cbcdc` | `a0 00 00 54` | b.eq 0x008cbcf0 | `CONDITIONAL_JUMP`
<a id="insn-008cbce0"></a> `008cbce0` | `08 0e 00 35` | cbnz w8,0x008cbea0 | `CONDITIONAL_JUMP`
<a id="insn-008cbce4"></a> `008cbce4` | `14 bc ee 97` | bl 0x0047ad34 | `UNCONDITIONAL_CALL`
<a id="insn-008cbce8"></a> `008cbce8` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-008cbcec"></a> `008cbcec` | `03 00 00 14` | b 0x008cbcf8 | `UNCONDITIONAL_JUMP`
<a id="insn-008cbcf0"></a> `008cbcf0` | `11 bc ee 97` | bl 0x0047ad34 | `UNCONDITIONAL_CALL`
<a id="insn-008cbcf4"></a> `008cbcf4` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-008cbcf8"></a> `008cbcf8` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-008cbcfc"></a> `008cbcfc` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-008cbd00"></a> `008cbd00` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-008cbd04"></a> `008cbd04` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-008cbd08"></a> `008cbd08` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008cbd0c"></a> `008cbd0c` | `fc 6f 42 a9` | ldp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008cbd10"></a> `008cbd10` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008cbd14"></a> `008cbd14` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-008cbd18"></a> `008cbd18` | `3f c4 ee 17` | b 0x0047ce14 | `CALL_TERMINATOR`
<a id="insn-008cbd1c"></a> `008cbd1c` | `13 04 40 f9` | ldr x19,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-008cbd20"></a> `008cbd20` | `0c 16 fe 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-008cbd24"></a> `008cbd24` | `88 26 9c 52` | mov w8,#0xe134 | `FALL_THROUGH`
<a id="insn-008cbd28"></a> `008cbd28` | `88 08 a0 72` | movk w8,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-008cbd2c"></a> `008cbd2c` | `1f 68 28 b8` | str wzr,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008cbd30"></a> `008cbd30` | `08 16 fe 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-008cbd34"></a> `008cbd34` | `08 da 9b 52` | mov w8,#0xded0 | `FALL_THROUGH`
<a id="insn-008cbd38"></a> `008cbd38` | `77 c2 00 91` | add x23,x19,#0x30 | `FALL_THROUGH`
<a id="insn-008cbd3c"></a> `008cbd3c` | `f3 07 00 f9` | str x19,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008cbd40"></a> `008cbd40` | `88 08 a0 72` | movk w8,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-008cbd44"></a> `008cbd44` | `08 68 68 f8` | ldr x8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008cbd48"></a> `008cbd48` | `09 0d 40 f9` | ldr x9,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-008cbd4c"></a> `008cbd4c` | `09 11 00 f9` | str x9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-008cbd50"></a> `008cbd50` | `7c 16 40 f9` | ldr x28,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-008cbd54"></a> `008cbd54` | `9f 03 17 eb` | cmp x28,x23 | `FALL_THROUGH`
<a id="insn-008cbd58"></a> `008cbd58` | `40 0b 00 54` | b.eq 0x008cbec0 | `CONDITIONAL_JUMP`
<a id="insn-008cbd5c"></a> `008cbd5c` | `14 da 9b 52` | mov w20,#0xded0 | `FALL_THROUGH`
<a id="insn-008cbd60"></a> `008cbd60` | `95 26 9c 52` | mov w21,#0xe134 | `FALL_THROUGH`
<a id="insn-008cbd64"></a> `008cbd64` | `fb 03 1f 2a` | mov w27,wzr | `FALL_THROUGH`
<a id="insn-008cbd68"></a> `008cbd68` | `94 08 a0 72` | movk w20,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-008cbd6c"></a> `008cbd6c` | `95 08 a0 72` | movk w21,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-008cbd70"></a> `008cbd70` | `36 00 80 52` | mov w22,#0x1 | `FALL_THROUGH`
<a id="insn-008cbd74"></a> `008cbd74` | `05 00 00 14` | b 0x008cbd88 | `UNCONDITIONAL_JUMP`
<a id="insn-008cbd78"></a> `008cbd78` | `1f 01 17 eb` | cmp x8,x23 | `FALL_THROUGH`
<a id="insn-008cbd7c"></a> `008cbd7c` | `fb 03 13 2a` | mov w27,w19 | `FALL_THROUGH`
<a id="insn-008cbd80"></a> `008cbd80` | `fc 03 08 aa` | mov x28,x8 | `FALL_THROUGH`
<a id="insn-008cbd84"></a> `008cbd84` | `00 0a 00 54` | b.eq 0x008cbec4 | `CONDITIONAL_JUMP`
<a id="insn-008cbd88"></a> `008cbd88` | `98 c3 41 f8` | ldur x24,[x28, #0x1c] | `FALL_THROUGH`
<a id="insn-008cbd8c"></a> `008cbd8c` | `1f 93 01 71` | cmp w24,#0x64 | `FALL_THROUGH`
<a id="insn-008cbd90"></a> `008cbd90` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-008cbd94"></a> `008cbd94` | `09 1f 60 f2` | ands x9,x24,#0xff00000000 | `FALL_THROUGH`
<a id="insn-008cbd98"></a> `008cbd98` | `e8 03 88 1a` | csel w8,wzr,w8,eq | `FALL_THROUGH`
<a id="insn-008cbd9c"></a> `008cbd9c` | `13 01 1b 2a` | orr w19,w8,w27 | `FALL_THROUGH`
<a id="insn-008cbda0"></a> `008cbda0` | `89 06 00 b4` | cbz x9,0x008cbe70 | `CONDITIONAL_JUMP`
<a id="insn-008cbda4"></a> `008cbda4` | `68 06 00 37` | tbnz w8,#0x0,0x008cbe70 | `CONDITIONAL_JUMP`
<a id="insn-008cbda8"></a> `008cbda8` | `ea 15 fe 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-008cbdac"></a> `008cbdac` | `13 68 74 f8` | ldr x19,[x0, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008cbdb0"></a> `008cbdb0` | `79 22 42 a9` | ldp x25,x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-008cbdb4"></a> `008cbdb4` | `3f 03 08 eb` | cmp x25,x8 | `FALL_THROUGH`
<a id="insn-008cbdb8"></a> `008cbdb8` | `62 00 00 54` | b.cs 0x008cbdc4 | `CONDITIONAL_JUMP`
<a id="insn-008cbdbc"></a> `008cbdbc` | `38 47 00 b8` | str w24,[x25], #0x4 | `FALL_THROUGH`
<a id="insn-008cbdc0"></a> `008cbdc0` | `28 00 00 14` | b 0x008cbe60 | `UNCONDITIONAL_JUMP`
<a id="insn-008cbdc4"></a> `008cbdc4` | `74 82 41 f8` | ldur x20,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-008cbdc8"></a> `008cbdc8` | `35 03 14 cb` | sub x21,x25,x20 | `FALL_THROUGH`
<a id="insn-008cbdcc"></a> `008cbdcc` | `b9 fe 42 93` | asr x25,x21,#0x2 | `FALL_THROUGH`
<a id="insn-008cbdd0"></a> `008cbdd0` | `29 07 00 91` | add x9,x25,#0x1 | `FALL_THROUGH`
<a id="insn-008cbdd4"></a> `008cbdd4` | `2a fd 7e d3` | lsr x10,x9,#0x3e | `FALL_THROUGH`
<a id="insn-008cbdd8"></a> `008cbdd8` | `ca 0b 00 b5` | cbnz x10,0x008cbf50 | `CONDITIONAL_JUMP`
<a id="insn-008cbddc"></a> `008cbddc` | `08 01 14 cb` | sub x8,x8,x20 | `FALL_THROUGH`
<a id="insn-008cbde0"></a> `008cbde0` | `0a fd 41 93` | asr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-008cbde4"></a> `008cbde4` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-008cbde8"></a> `008cbde8` | `49 81 89 9a` | csel x9,x10,x9,hi | `FALL_THROUGH`
<a id="insn-008cbdec"></a> `008cbdec` | `ea f3 7e b2` | orr x10,xzr,#0x7ffffffffffffffc | `FALL_THROUGH`
<a id="insn-008cbdf0"></a> `008cbdf0` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-008cbdf4"></a> `008cbdf4` | `08 00 f8 92` | mov x8,#0x3fffffffffffffff | `FALL_THROUGH`
<a id="insn-008cbdf8"></a> `008cbdf8` | `3a 31 88 9a` | csel x26,x9,x8,cc | `FALL_THROUGH`
<a id="insn-008cbdfc"></a> `008cbdfc` | `fa 00 00 b4` | cbz x26,0x008cbe18 | `CONDITIONAL_JUMP`
<a id="insn-008cbe00"></a> `008cbe00` | `48 ff 7e d3` | lsr x8,x26,#0x3e | `FALL_THROUGH`
<a id="insn-008cbe04"></a> `008cbe04` | `a8 0a 00 b5` | cbnz x8,0x008cbf58 | `CONDITIONAL_JUMP`
<a id="insn-008cbe08"></a> `008cbe08` | `40 f7 7e d3` | lsl x0,x26,#0x2 | `FALL_THROUGH`
<a id="insn-008cbe0c"></a> `008cbe0c` | `55 30 0e 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-008cbe10"></a> `008cbe10` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-008cbe14"></a> `008cbe14` | `02 00 00 14` | b 0x008cbe1c | `UNCONDITIONAL_JUMP`
<a id="insn-008cbe18"></a> `008cbe18` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-008cbe1c"></a> `008cbe1c` | `d9 0a 19 8b` | add x25,x22,x25, LSL #0x2 | `FALL_THROUGH`
<a id="insn-008cbe20"></a> `008cbe20` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008cbe24"></a> `008cbe24` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-008cbe28"></a> `008cbe28` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-008cbe2c"></a> `008cbe2c` | `da 0a 1a 8b` | add x26,x22,x26, LSL #0x2 | `FALL_THROUGH`
<a id="insn-008cbe30"></a> `008cbe30` | `38 47 00 b8` | str w24,[x25], #0x4 | `FALL_THROUGH`
<a id="insn-008cbe34"></a> `008cbe34` | `a7 30 0e 94` | bl 0x00c580d0 | `UNCONDITIONAL_CALL`
<a id="insn-008cbe38"></a> `008cbe38` | `76 e6 01 a9` | stp x22,x25,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-008cbe3c"></a> `008cbe3c` | `7a 16 00 f9` | str x26,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-008cbe40"></a> `008cbe40` | `74 00 00 b4` | cbz x20,0x008cbe4c | `CONDITIONAL_JUMP`
<a id="insn-008cbe44"></a> `008cbe44` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-008cbe48"></a> `008cbe48` | `4e 30 0e 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-008cbe4c"></a> `008cbe4c` | `14 da 9b 52` | mov w20,#0xded0 | `FALL_THROUGH`
<a id="insn-008cbe50"></a> `008cbe50` | `95 26 9c 52` | mov w21,#0xe134 | `FALL_THROUGH`
<a id="insn-008cbe54"></a> `008cbe54` | `36 00 80 52` | mov w22,#0x1 | `FALL_THROUGH`
<a id="insn-008cbe58"></a> `008cbe58` | `94 08 a0 72` | movk w20,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-008cbe5c"></a> `008cbe5c` | `95 08 a0 72` | movk w21,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-008cbe60"></a> `008cbe60` | `79 12 00 f9` | str x25,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-008cbe64"></a> `008cbe64` | `bb 15 fe 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-008cbe68"></a> `008cbe68` | `f3 03 1b 2a` | mov w19,w27 | `FALL_THROUGH`
<a id="insn-008cbe6c"></a> `008cbe6c` | `16 68 35 b8` | str w22,[x0, x21, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008cbe70"></a> `008cbe70` | `89 07 40 f9` | ldr x9,[x28, #0x8] | `FALL_THROUGH`
<a id="insn-008cbe74"></a> `008cbe74` | `a9 00 00 b4` | cbz x9,0x008cbe88 | `CONDITIONAL_JUMP`
<a id="insn-008cbe78"></a> `008cbe78` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-008cbe7c"></a> `008cbe7c` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-008cbe80"></a> `008cbe80` | `c9 ff ff b5` | cbnz x9,0x008cbe78 | `CONDITIONAL_JUMP`
<a id="insn-008cbe84"></a> `008cbe84` | `bd ff ff 17` | b 0x008cbd78 | `UNCONDITIONAL_JUMP`
<a id="insn-008cbe88"></a> `008cbe88` | `88 0b 40 f9` | ldr x8,[x28, #0x10] | `FALL_THROUGH`
<a id="insn-008cbe8c"></a> `008cbe8c` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-008cbe90"></a> `008cbe90` | `3f 01 1c eb` | cmp x9,x28 | `FALL_THROUGH`
<a id="insn-008cbe94"></a> `008cbe94` | `fc 03 08 aa` | mov x28,x8 | `FALL_THROUGH`
<a id="insn-008cbe98"></a> `008cbe98` | `81 ff ff 54` | b.ne 0x008cbe88 | `CONDITIONAL_JUMP`
<a id="insn-008cbe9c"></a> `008cbe9c` | `b7 ff ff 17` | b 0x008cbd78 | `UNCONDITIONAL_JUMP`
<a id="insn-008cbea0"></a> `008cbea0` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-008cbea4"></a> `008cbea4` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-008cbea8"></a> `008cbea8` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-008cbeac"></a> `008cbeac` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008cbeb0"></a> `008cbeb0` | `fc 6f 42 a9` | ldp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008cbeb4"></a> `008cbeb4` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008cbeb8"></a> `008cbeb8` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-008cbebc"></a> `008cbebc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-008cbec0"></a> `008cbec0` | `f3 03 1f 2a` | mov w19,wzr | `FALL_THROUGH`
<a id="insn-008cbec4"></a> `008cbec4` | `a3 15 fe 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-008cbec8"></a> `008cbec8` | `15 a0 9b 52` | mov w21,#0xdd00 | `FALL_THROUGH`
<a id="insn-008cbecc"></a> `008cbecc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-008cbed0"></a> `008cbed0` | `95 08 a0 72` | movk w21,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-008cbed4"></a> `008cbed4` | `9f 15 fe 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-008cbed8"></a> `008cbed8` | `88 26 9c 52` | mov w8,#0xe134 | `FALL_THROUGH`
<a id="insn-008cbedc"></a> `008cbedc` | `64 02 00 12` | and w4,w19,#0x1 | `FALL_THROUGH`
<a id="insn-008cbee0"></a> `008cbee0` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-008cbee4"></a> `008cbee4` | `88 08 a0 72` | movk w8,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-008cbee8"></a> `008cbee8` | `03 00 80 12` | mov w3,#0xffffffff | `FALL_THROUGH`
<a id="insn-008cbeec"></a> `008cbeec` | `13 00 80 12` | mov w19,#0xffffffff | `FALL_THROUGH`
<a id="insn-008cbef0"></a> `008cbef0` | `01 68 68 b8` | ldr w1,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008cbef4"></a> `008cbef4` | `80 02 15 8b` | add x0,x20,x21 | `FALL_THROUGH`
<a id="insn-008cbef8"></a> `008cbef8` | `6f de ff 97` | bl 0x008c38b4 | `UNCONDITIONAL_CALL`
<a id="insn-008cbefc"></a> `008cbefc` | `95 15 fe 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-008cbf00"></a> `008cbf00` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-008cbf04"></a> `008cbf04` | `f8 e0 ff 97` | bl 0x008c42e4 | `UNCONDITIONAL_CALL`
<a id="insn-008cbf08"></a> `008cbf08` | `92 15 fe 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-008cbf0c"></a> `008cbf0c` | `00 00 15 8b` | add x0,x0,x21 | `FALL_THROUGH`
<a id="insn-008cbf10"></a> `008cbf10` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-008cbf14"></a> `008cbf14` | `d5 e1 ff 97` | bl 0x008c4668 | `UNCONDITIONAL_CALL`
<a id="insn-008cbf18"></a> `008cbf18` | `8e 15 fe 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-008cbf1c"></a> `008cbf1c` | `89 ce 9b 52` | mov w9,#0xde74 | `FALL_THROUGH`
<a id="insn-008cbf20"></a> `008cbf20` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-008cbf24"></a> `008cbf24` | `e0 07 40 f9` | ldr x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008cbf28"></a> `008cbf28` | `89 08 a0 72` | movk w9,#0x44, LSL #16 | `FALL_THROUGH`
<a id="insn-008cbf2c"></a> `008cbf2c` | `13 69 29 b8` | str w19,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008cbf30"></a> `008cbf30` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-008cbf34"></a> `008cbf34` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-008cbf38"></a> `008cbf38` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-008cbf3c"></a> `008cbf3c` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008cbf40"></a> `008cbf40` | `fc 6f 42 a9` | ldp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008cbf44"></a> `008cbf44` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008cbf48"></a> `008cbf48` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-008cbf4c"></a> `008cbf4c` | `ae cd ff 17` | b 0x008bf604 | `CALL_TERMINATOR`
<a id="insn-008cbf50"></a> `008cbf50` | `60 62 00 91` | add x0,x19,#0x18 | `FALL_THROUGH`
<a id="insn-008cbf54"></a> `008cbf54` | `4b 92 ee 97` | bl 0x00470880 | `CALL_TERMINATOR`
<a id="insn-008cbf58"></a> `008cbf58` | `ea d3 ed 97` | bl 0x00440f00 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008cbcac`](#insn-008cbcac) 範囲 `[['008cbcac', '008cbcd7']]`
  - `CONDITIONAL_JUMP` [`008cbcd4`](#insn-008cbcd4) → [`008cbd1c`](#insn-008cbd1c)
  - `FALL_THROUGH` [`008cbcd4`](#insn-008cbcd4) → [`008cbcd8`](#insn-008cbcd8)
- ブロック [`008cbcd8`](#insn-008cbcd8) 範囲 `[['008cbcd8', '008cbcdf']]`
  - `CONDITIONAL_JUMP` [`008cbcdc`](#insn-008cbcdc) → [`008cbcf0`](#insn-008cbcf0)
  - `FALL_THROUGH` [`008cbcdc`](#insn-008cbcdc) → [`008cbce0`](#insn-008cbce0)
- ブロック [`008cbce0`](#insn-008cbce0) 範囲 `[['008cbce0', '008cbce3']]`
  - `CONDITIONAL_JUMP` [`008cbce0`](#insn-008cbce0) → [`008cbea0`](#insn-008cbea0)
  - `FALL_THROUGH` [`008cbce0`](#insn-008cbce0) → [`008cbce4`](#insn-008cbce4)
- ブロック [`008cbce4`](#insn-008cbce4) 範囲 `[['008cbce4', '008cbcef']]`
  - `UNCONDITIONAL_JUMP` [`008cbcec`](#insn-008cbcec) → [`008cbcf8`](#insn-008cbcf8)
- ブロック [`008cbcf0`](#insn-008cbcf0) 範囲 `[['008cbcf0', '008cbcf7']]`
  - `FALL_THROUGH` [`008cbcf4`](#insn-008cbcf4) → [`008cbcf8`](#insn-008cbcf8)
- ブロック [`008cbcf8`](#insn-008cbcf8) 範囲 `[['008cbcf8', '008cbd1b']]`
- ブロック [`008cbd1c`](#insn-008cbd1c) 範囲 `[['008cbd1c', '008cbd5b']]`
  - `CONDITIONAL_JUMP` [`008cbd58`](#insn-008cbd58) → [`008cbec0`](#insn-008cbec0)
  - `FALL_THROUGH` [`008cbd58`](#insn-008cbd58) → [`008cbd5c`](#insn-008cbd5c)
- ブロック [`008cbd5c`](#insn-008cbd5c) 範囲 `[['008cbd5c', '008cbd77']]`
  - `UNCONDITIONAL_JUMP` [`008cbd74`](#insn-008cbd74) → [`008cbd88`](#insn-008cbd88)
- ブロック [`008cbd78`](#insn-008cbd78) 範囲 `[['008cbd78', '008cbd87']]`
  - `CONDITIONAL_JUMP` [`008cbd84`](#insn-008cbd84) → [`008cbec4`](#insn-008cbec4)
  - `FALL_THROUGH` [`008cbd84`](#insn-008cbd84) → [`008cbd88`](#insn-008cbd88)
- ブロック [`008cbd88`](#insn-008cbd88) 範囲 `[['008cbd88', '008cbda3']]`
  - `CONDITIONAL_JUMP` [`008cbda0`](#insn-008cbda0) → [`008cbe70`](#insn-008cbe70)
  - `FALL_THROUGH` [`008cbda0`](#insn-008cbda0) → [`008cbda4`](#insn-008cbda4)
- ブロック [`008cbda4`](#insn-008cbda4) 範囲 `[['008cbda4', '008cbda7']]`
  - `CONDITIONAL_JUMP` [`008cbda4`](#insn-008cbda4) → [`008cbe70`](#insn-008cbe70)
  - `FALL_THROUGH` [`008cbda4`](#insn-008cbda4) → [`008cbda8`](#insn-008cbda8)
- ブロック [`008cbda8`](#insn-008cbda8) 範囲 `[['008cbda8', '008cbdbb']]`
  - `CONDITIONAL_JUMP` [`008cbdb8`](#insn-008cbdb8) → [`008cbdc4`](#insn-008cbdc4)
  - `FALL_THROUGH` [`008cbdb8`](#insn-008cbdb8) → [`008cbdbc`](#insn-008cbdbc)
- ブロック [`008cbdbc`](#insn-008cbdbc) 範囲 `[['008cbdbc', '008cbdc3']]`
  - `UNCONDITIONAL_JUMP` [`008cbdc0`](#insn-008cbdc0) → [`008cbe60`](#insn-008cbe60)
- ブロック [`008cbdc4`](#insn-008cbdc4) 範囲 `[['008cbdc4', '008cbddb']]`
  - `CONDITIONAL_JUMP` [`008cbdd8`](#insn-008cbdd8) → [`008cbf50`](#insn-008cbf50)
  - `FALL_THROUGH` [`008cbdd8`](#insn-008cbdd8) → [`008cbddc`](#insn-008cbddc)
- ブロック [`008cbddc`](#insn-008cbddc) 範囲 `[['008cbddc', '008cbdff']]`
  - `CONDITIONAL_JUMP` [`008cbdfc`](#insn-008cbdfc) → [`008cbe18`](#insn-008cbe18)
  - `FALL_THROUGH` [`008cbdfc`](#insn-008cbdfc) → [`008cbe00`](#insn-008cbe00)
- ブロック [`008cbe00`](#insn-008cbe00) 範囲 `[['008cbe00', '008cbe07']]`
  - `CONDITIONAL_JUMP` [`008cbe04`](#insn-008cbe04) → [`008cbf58`](#insn-008cbf58)
  - `FALL_THROUGH` [`008cbe04`](#insn-008cbe04) → [`008cbe08`](#insn-008cbe08)
- ブロック [`008cbe08`](#insn-008cbe08) 範囲 `[['008cbe08', '008cbe0f']]`
  - `FALL_THROUGH` [`008cbe0c`](#insn-008cbe0c) → [`008cbe10`](#insn-008cbe10)
- ブロック [`008cbe10`](#insn-008cbe10) 範囲 `[['008cbe10', '008cbe17']]`
  - `UNCONDITIONAL_JUMP` [`008cbe14`](#insn-008cbe14) → [`008cbe1c`](#insn-008cbe1c)
- ブロック [`008cbe18`](#insn-008cbe18) 範囲 `[['008cbe18', '008cbe1b']]`
  - `FALL_THROUGH` [`008cbe18`](#insn-008cbe18) → [`008cbe1c`](#insn-008cbe1c)
- ブロック [`008cbe1c`](#insn-008cbe1c) 範囲 `[['008cbe1c', '008cbe43']]`
  - `CONDITIONAL_JUMP` [`008cbe40`](#insn-008cbe40) → [`008cbe4c`](#insn-008cbe4c)
  - `FALL_THROUGH` [`008cbe40`](#insn-008cbe40) → [`008cbe44`](#insn-008cbe44)
- ブロック [`008cbe44`](#insn-008cbe44) 範囲 `[['008cbe44', '008cbe4b']]`
  - `FALL_THROUGH` [`008cbe48`](#insn-008cbe48) → [`008cbe4c`](#insn-008cbe4c)
- ブロック [`008cbe4c`](#insn-008cbe4c) 範囲 `[['008cbe4c', '008cbe5f']]`
  - `FALL_THROUGH` [`008cbe5c`](#insn-008cbe5c) → [`008cbe60`](#insn-008cbe60)
- ブロック [`008cbe60`](#insn-008cbe60) 範囲 `[['008cbe60', '008cbe6f']]`
  - `FALL_THROUGH` [`008cbe6c`](#insn-008cbe6c) → [`008cbe70`](#insn-008cbe70)
- ブロック [`008cbe70`](#insn-008cbe70) 範囲 `[['008cbe70', '008cbe77']]`
  - `CONDITIONAL_JUMP` [`008cbe74`](#insn-008cbe74) → [`008cbe88`](#insn-008cbe88)
  - `FALL_THROUGH` [`008cbe74`](#insn-008cbe74) → [`008cbe78`](#insn-008cbe78)
- ブロック [`008cbe78`](#insn-008cbe78) 範囲 `[['008cbe78', '008cbe83']]`
  - `CONDITIONAL_JUMP` [`008cbe80`](#insn-008cbe80) → [`008cbe78`](#insn-008cbe78)
  - `FALL_THROUGH` [`008cbe80`](#insn-008cbe80) → [`008cbe84`](#insn-008cbe84)
- ブロック [`008cbe84`](#insn-008cbe84) 範囲 `[['008cbe84', '008cbe87']]`
  - `UNCONDITIONAL_JUMP` [`008cbe84`](#insn-008cbe84) → [`008cbd78`](#insn-008cbd78)
- ブロック [`008cbe88`](#insn-008cbe88) 範囲 `[['008cbe88', '008cbe9b']]`
  - `CONDITIONAL_JUMP` [`008cbe98`](#insn-008cbe98) → [`008cbe88`](#insn-008cbe88)
  - `FALL_THROUGH` [`008cbe98`](#insn-008cbe98) → [`008cbe9c`](#insn-008cbe9c)
- ブロック [`008cbe9c`](#insn-008cbe9c) 範囲 `[['008cbe9c', '008cbe9f']]`
  - `UNCONDITIONAL_JUMP` [`008cbe9c`](#insn-008cbe9c) → [`008cbd78`](#insn-008cbd78)
- ブロック [`008cbea0`](#insn-008cbea0) 範囲 `[['008cbea0', '008cbebf']]`
- ブロック [`008cbec0`](#insn-008cbec0) 範囲 `[['008cbec0', '008cbec3']]`
  - `FALL_THROUGH` [`008cbec0`](#insn-008cbec0) → [`008cbec4`](#insn-008cbec4)
- ブロック [`008cbec4`](#insn-008cbec4) 範囲 `[['008cbec4', '008cbf07']]`
  - `FALL_THROUGH` [`008cbf04`](#insn-008cbf04) → [`008cbf08`](#insn-008cbf08)
- ブロック [`008cbf08`](#insn-008cbf08) 範囲 `[['008cbf08', '008cbf1b']]`
  - `FALL_THROUGH` [`008cbf18`](#insn-008cbf18) → [`008cbf1c`](#insn-008cbf1c)
- ブロック [`008cbf1c`](#insn-008cbf1c) 範囲 `[['008cbf1c', '008cbf1f']]`
  - `FALL_THROUGH` [`008cbf1c`](#insn-008cbf1c) → [`008cbf20`](#insn-008cbf20)
- ブロック [`008cbf20`](#insn-008cbf20) 範囲 `[['008cbf20', '008cbf4f']]`
- ブロック [`008cbf50`](#insn-008cbf50) 範囲 `[['008cbf50', '008cbf57']]`
- ブロック [`008cbf58`](#insn-008cbf58) 範囲 `[['008cbf58', '008cbf5b']]`

## 命令位置別の参照

- [`008cbcb0`](#insn-008cbcb0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbcb4`](#insn-008cbcb4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbcb8`](#insn-008cbcb8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbcbc`](#insn-008cbcbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbcc0`](#insn-008cbcc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbcc4`](#insn-008cbcc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbcd4`](#insn-008cbcd4) → [`008cbd1c`](#insn-008cbd1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbcdc`](#insn-008cbcdc) → [`008cbcf0`](#insn-008cbcf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbce0`](#insn-008cbce0) → [`008cbea0`](#insn-008cbea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbce4`](#insn-008cbce4) → [`0047ad34`](../0047a/0047ad34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047ad34` · 推定シンボル `None` · 推定型 `None`
- [`008cbcec`](#insn-008cbcec) → [`008cbcf8`](#insn-008cbcf8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbcf0`](#insn-008cbcf0) → [`0047ad34`](../0047a/0047ad34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047ad34` · 推定シンボル `None` · 推定型 `None`
- [`008cbcfc`](#insn-008cbcfc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbd00`](#insn-008cbd00) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbd04`](#insn-008cbd04) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbd08`](#insn-008cbd08) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbd0c`](#insn-008cbd0c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbd10`](#insn-008cbd10) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbd18`](#insn-008cbd18) → [`0047ce14`](../0047c/0047ce14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047ce14` · 推定シンボル `None` · 推定型 `None`
- [`008cbd20`](#insn-008cbd20) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`008cbd30`](#insn-008cbd30) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`008cbd3c`](#insn-008cbd3c) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbd44`](#insn-008cbd44) → `0044ded0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbd58`](#insn-008cbd58) → [`008cbec0`](#insn-008cbec0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbd74`](#insn-008cbd74) → [`008cbd88`](#insn-008cbd88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbd84`](#insn-008cbd84) → [`008cbec4`](#insn-008cbec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbda0`](#insn-008cbda0) → [`008cbe70`](#insn-008cbe70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbda4`](#insn-008cbda4) → [`008cbe70`](#insn-008cbe70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbda8`](#insn-008cbda8) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`008cbdac`](#insn-008cbdac) → `0044ded0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbdb8`](#insn-008cbdb8) → [`008cbdc4`](#insn-008cbdc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbdc0`](#insn-008cbdc0) → [`008cbe60`](#insn-008cbe60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbdd8`](#insn-008cbdd8) → [`008cbf50`](#insn-008cbf50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbdfc`](#insn-008cbdfc) → [`008cbe18`](#insn-008cbe18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbe04`](#insn-008cbe04) → [`008cbf58`](#insn-008cbf58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbe0c`](#insn-008cbe0c) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`008cbe14`](#insn-008cbe14) → [`008cbe1c`](#insn-008cbe1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbe34`](#insn-008cbe34) → [`00c580d0`](../00c58/00c580d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580d0` · 推定シンボル `None` · 推定型 `None`
- [`008cbe40`](#insn-008cbe40) → [`008cbe4c`](#insn-008cbe4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbe48`](#insn-008cbe48) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`008cbe64`](#insn-008cbe64) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`008cbe74`](#insn-008cbe74) → [`008cbe88`](#insn-008cbe88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbe80`](#insn-008cbe80) → [`008cbe78`](#insn-008cbe78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbe84`](#insn-008cbe84) → [`008cbd78`](#insn-008cbd78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbe98`](#insn-008cbe98) → [`008cbe88`](#insn-008cbe88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbe9c`](#insn-008cbe9c) → [`008cbd78`](#insn-008cbd78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbea0`](#insn-008cbea0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbea4`](#insn-008cbea4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbea8`](#insn-008cbea8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbeac`](#insn-008cbeac) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbeb0`](#insn-008cbeb0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbeb4`](#insn-008cbeb4) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbec4`](#insn-008cbec4) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`008cbed4`](#insn-008cbed4) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`008cbef8`](#insn-008cbef8) → [`008c38b4`](../008c3/008c38b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008c38b4` · 推定シンボル `None` · 推定型 `None`
- [`008cbefc`](#insn-008cbefc) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`008cbf04`](#insn-008cbf04) → [`008c42e4`](../008c4/008c42e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008c42e4` · 推定シンボル `None` · 推定型 `None`
- [`008cbf08`](#insn-008cbf08) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`008cbf14`](#insn-008cbf14) → [`008c4668`](../008c4/008c4668.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008c4668` · 推定シンボル `None` · 推定型 `None`
- [`008cbf18`](#insn-008cbf18) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`008cbf24`](#insn-008cbf24) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbf30`](#insn-008cbf30) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbf34`](#insn-008cbf34) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbf38`](#insn-008cbf38) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbf3c`](#insn-008cbf3c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbf40`](#insn-008cbf40) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbf44`](#insn-008cbf44) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008cbf4c`](#insn-008cbf4c) → [`008bf604`](../008bf/008bf604.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008bf604` · 推定シンボル `None` · 推定型 `None`
- [`008cbf54`](#insn-008cbf54) → [`00470880`](../00470/00470880.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00470880` · 推定シンボル `None` · 推定型 `None`
- [`008cbf58`](#insn-008cbf58) → [`00440f00`](../00440/00440f00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00440f00` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008cbcb0`](#insn-008cbcb0)

~~~json
{
  "source": "008cbcb0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbcb4`](#insn-008cbcb4)

~~~json
{
  "source": "008cbcb4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbcb8`](#insn-008cbcb8)

~~~json
{
  "source": "008cbcb8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbcbc`](#insn-008cbcbc)

~~~json
{
  "source": "008cbcbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbcc0`](#insn-008cbcc0)

~~~json
{
  "source": "008cbcc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbcc4`](#insn-008cbcc4)

~~~json
{
  "source": "008cbcc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbcd4`](#insn-008cbcd4)

~~~json
{
  "source": "008cbcd4",
  "target": "008cbd1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbcdc`](#insn-008cbcdc)

~~~json
{
  "source": "008cbcdc",
  "target": "008cbcf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbce0`](#insn-008cbce0)

~~~json
{
  "source": "008cbce0",
  "target": "008cbea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbce4`](#insn-008cbce4)

~~~json
{
  "source": "008cbce4",
  "target": "0047ad34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbcec`](#insn-008cbcec)

~~~json
{
  "source": "008cbcec",
  "target": "008cbcf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbcf0`](#insn-008cbcf0)

~~~json
{
  "source": "008cbcf0",
  "target": "0047ad34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbcfc`](#insn-008cbcfc)

~~~json
{
  "source": "008cbcfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbd00`](#insn-008cbd00)

~~~json
{
  "source": "008cbd00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbd04`](#insn-008cbd04)

~~~json
{
  "source": "008cbd04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbd08`](#insn-008cbd08)

~~~json
{
  "source": "008cbd08",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbd0c`](#insn-008cbd0c)

~~~json
{
  "source": "008cbd0c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbd10`](#insn-008cbd10)

~~~json
{
  "source": "008cbd10",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbd18`](#insn-008cbd18)

~~~json
{
  "source": "008cbd18",
  "target": "0047ce14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbd20`](#insn-008cbd20)

~~~json
{
  "source": "008cbd20",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbd30`](#insn-008cbd30)

~~~json
{
  "source": "008cbd30",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbd3c`](#insn-008cbd3c)

~~~json
{
  "source": "008cbd3c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbd44`](#insn-008cbd44)

~~~json
{
  "source": "008cbd44",
  "target": "0044ded0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbd58`](#insn-008cbd58)

~~~json
{
  "source": "008cbd58",
  "target": "008cbec0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbd74`](#insn-008cbd74)

~~~json
{
  "source": "008cbd74",
  "target": "008cbd88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbd84`](#insn-008cbd84)

~~~json
{
  "source": "008cbd84",
  "target": "008cbec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbda0`](#insn-008cbda0)

~~~json
{
  "source": "008cbda0",
  "target": "008cbe70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbda4`](#insn-008cbda4)

~~~json
{
  "source": "008cbda4",
  "target": "008cbe70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbda8`](#insn-008cbda8)

~~~json
{
  "source": "008cbda8",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbdac`](#insn-008cbdac)

~~~json
{
  "source": "008cbdac",
  "target": "0044ded0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbdb8`](#insn-008cbdb8)

~~~json
{
  "source": "008cbdb8",
  "target": "008cbdc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbdc0`](#insn-008cbdc0)

~~~json
{
  "source": "008cbdc0",
  "target": "008cbe60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbdd8`](#insn-008cbdd8)

~~~json
{
  "source": "008cbdd8",
  "target": "008cbf50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbdfc`](#insn-008cbdfc)

~~~json
{
  "source": "008cbdfc",
  "target": "008cbe18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbe04`](#insn-008cbe04)

~~~json
{
  "source": "008cbe04",
  "target": "008cbf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbe0c`](#insn-008cbe0c)

~~~json
{
  "source": "008cbe0c",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbe14`](#insn-008cbe14)

~~~json
{
  "source": "008cbe14",
  "target": "008cbe1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbe34`](#insn-008cbe34)

~~~json
{
  "source": "008cbe34",
  "target": "00c580d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbe40`](#insn-008cbe40)

~~~json
{
  "source": "008cbe40",
  "target": "008cbe4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbe48`](#insn-008cbe48)

~~~json
{
  "source": "008cbe48",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbe64`](#insn-008cbe64)

~~~json
{
  "source": "008cbe64",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbe74`](#insn-008cbe74)

~~~json
{
  "source": "008cbe74",
  "target": "008cbe88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbe80`](#insn-008cbe80)

~~~json
{
  "source": "008cbe80",
  "target": "008cbe78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbe84`](#insn-008cbe84)

~~~json
{
  "source": "008cbe84",
  "target": "008cbd78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbe98`](#insn-008cbe98)

~~~json
{
  "source": "008cbe98",
  "target": "008cbe88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbe9c`](#insn-008cbe9c)

~~~json
{
  "source": "008cbe9c",
  "target": "008cbd78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbea0`](#insn-008cbea0)

~~~json
{
  "source": "008cbea0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbea4`](#insn-008cbea4)

~~~json
{
  "source": "008cbea4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbea8`](#insn-008cbea8)

~~~json
{
  "source": "008cbea8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbeac`](#insn-008cbeac)

~~~json
{
  "source": "008cbeac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbeb0`](#insn-008cbeb0)

~~~json
{
  "source": "008cbeb0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbeb4`](#insn-008cbeb4)

~~~json
{
  "source": "008cbeb4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbec4`](#insn-008cbec4)

~~~json
{
  "source": "008cbec4",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbed4`](#insn-008cbed4)

~~~json
{
  "source": "008cbed4",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbef8`](#insn-008cbef8)

~~~json
{
  "source": "008cbef8",
  "target": "008c38b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbefc`](#insn-008cbefc)

~~~json
{
  "source": "008cbefc",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbf04`](#insn-008cbf04)

~~~json
{
  "source": "008cbf04",
  "target": "008c42e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbf08`](#insn-008cbf08)

~~~json
{
  "source": "008cbf08",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbf14`](#insn-008cbf14)

~~~json
{
  "source": "008cbf14",
  "target": "008c4668",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbf18`](#insn-008cbf18)

~~~json
{
  "source": "008cbf18",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbf24`](#insn-008cbf24)

~~~json
{
  "source": "008cbf24",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbf30`](#insn-008cbf30)

~~~json
{
  "source": "008cbf30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbf34`](#insn-008cbf34)

~~~json
{
  "source": "008cbf34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbf38`](#insn-008cbf38)

~~~json
{
  "source": "008cbf38",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbf3c`](#insn-008cbf3c)

~~~json
{
  "source": "008cbf3c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbf40`](#insn-008cbf40)

~~~json
{
  "source": "008cbf40",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbf44`](#insn-008cbf44)

~~~json
{
  "source": "008cbf44",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008cbf4c`](#insn-008cbf4c)

~~~json
{
  "source": "008cbf4c",
  "target": "008bf604",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbf54`](#insn-008cbf54)

~~~json
{
  "source": "008cbf54",
  "target": "00470880",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008cbf58`](#insn-008cbf58)

~~~json
{
  "source": "008cbf58",
  "target": "00440f00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
