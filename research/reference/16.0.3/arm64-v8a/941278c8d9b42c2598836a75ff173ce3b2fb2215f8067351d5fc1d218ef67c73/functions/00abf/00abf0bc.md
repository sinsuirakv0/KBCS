# 00abf0bc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00abe0c8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00abe/00abe0c8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0066.md#compare-1846fa1b248480ff22f8487524e59480)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abf0bc",
  "name": "FUN_00abf0bc",
  "size": 600,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d0686c8833ea2ec27b9f2bbb555960d79ff583d95a5e279c81a65edddad2fe60",
  "source_text_sha256": "d0686c8833ea2ec27b9f2bbb555960d79ff583d95a5e279c81a65edddad2fe60",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00abf0bc",
        "00abf313"
      ]
    ],
    "bytes_sha256": "6cc7cc62a12618288b6c541392379e10523d9a30f5af00adaaaca587a337c64c",
    "instruction_count": 150,
    "instruction_bytes": 600,
    "body_bytes": 600,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a271bc](../00a27/00a271bc.md)

## 呼び出し先

- [0043bf04](../0043b/0043bf04.md)
- [00441220](../00441/00441220.md)
- [00470ba0](../00470/00470ba0.md)
- [00480478](../00480/00480478.md)
- [004804d8](../00480/004804d8.md)
- [00480658](../00480/00480658.md)
- [00480750](../00480/00480750.md)
- [005c1b8c](../005c1/005c1b8c.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c590a0](../00c59/00c590a0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4707 bytes

~~~c

void FUN_00abf0bc(long param_1,undefined8 param_2)

{
  ulong uVar1;
  int *piVar2;
  int *piVar3;
  int iVar4;
  char cVar5;
  byte bVar6;
  short sVar7;
  short sVar8;
  undefined4 uVar9;
  undefined8 *puVar10;
  void *__dest;
  undefined8 *puVar11;
  long *plVar12;
  ulong uVar13;
  ulong uVar14;
  undefined8 *puVar15;
  long *plVar16;
  void *__src;
  undefined8 *puVar17;
  int iVar18;
  int *piVar19;
  long lVar20;
  undefined8 *puVar21;
  
  uVar9 = FUN_00480750(param_2);
  *(undefined4 *)(param_1 + 0x60) = uVar9;
  uVar9 = FUN_00480750(param_2);
  *(undefined4 *)(param_1 + 100) = uVar9;
  uVar9 = FUN_00480750(param_2);
  *(undefined4 *)(param_1 + 0x68) = uVar9;
  sVar7 = FUN_004804d8(param_2);
  iVar18 = (int)sVar7;
  puVar15 = (undefined8 *)(param_1 + 0x30);
  *(undefined8 *)(param_1 + 0x38) = *puVar15;
  if (0 < iVar18) {
    do {
      sVar7 = FUN_004804d8(param_2);
                    /* try { // try from 00abf23c to 00bbf243 has its CatchHandler @ 00abf274 */
      piVar3 = *(int **)(param_1 + 0x38);
                    /* try { // try from 00abf244 to 00bbf2df has its CatchHandler @ 00abf07c */
      if (piVar3 < *(int **)(param_1 + 0x40)) {
        piVar19 = piVar3 + 1;
        *piVar3 = (int)sVar7;
      }
      else {
        __src = (void *)*puVar15;
        lVar20 = (long)piVar3 - (long)__src >> 2;
        uVar1 = lVar20 + 1;
        if (uVar1 >> 0x3e != 0) {
                    /* WARNING: Subroutine does not return */
          FUN_00470ba0(puVar15);
        }
        uVar13 = (long)*(int **)(param_1 + 0x40) - (long)__src;
        uVar14 = (long)uVar13 >> 1;
        if (uVar14 <= uVar1) {
          uVar14 = uVar1;
        }
                    /* catch() { ... } // from try @ 00abf23c with catch @ 00abf274 */
        if (0x7ffffffffffffffb < uVar13) {
          uVar14 = 0x3fffffffffffffff;
        }
        if (uVar14 == 0) {
          __dest = (void *)0x0;
        }
        else {
          if (uVar14 >> 0x3e != 0) {
                    /* WARNING: Subroutine does not return */
            FUN_00441220();
          }
                    /* catch() { ... } // from try @ 00abf158 with catch @ 00abf290 */
          __dest = (void *)_Znwm(uVar14 << 2);
        }
        piVar2 = (int *)((long)__dest + lVar20 * 4);
        piVar19 = piVar2 + 1;
        *piVar2 = (int)sVar7;
        memcpy(__dest,__src,(long)piVar3 - (long)__src);
        *(void **)(param_1 + 0x30) = __dest;
        *(int **)(param_1 + 0x38) = piVar19;
        *(void **)(param_1 + 0x40) = (void *)((long)__dest + uVar14 * 4);
        if (__src != (void *)0x0) {
          _ZdlPv(__src);
        }
      }
      iVar18 = iVar18 + -1;
      *(int **)(param_1 + 0x38) = piVar19;
    } while (iVar18 != 0);
  }
  sVar7 = FUN_004804d8(param_2);
  puVar15 = (undefined8 *)(param_1 + 0x50);
  plVar16 = (long *)(param_1 + 0x48);
  FUN_005c1b8c(plVar16,*puVar15);
  *puVar15 = 0;
  *(undefined8 *)(param_1 + 0x58) = 0;
  *(undefined8 **)(param_1 + 0x48) = puVar15;
                    /* try { // try from 00abf158 to 00bbf17b has its CatchHandler @ 00abf290 */
  if (0 < sVar7) {
    iVar18 = 0;
    do {
      sVar8 = FUN_004804d8(param_2);
      iVar4 = (int)sVar8;
      cVar5 = FUN_00480478(param_2);
      puVar11 = (undefined8 *)*puVar15;
      puVar17 = puVar15;
      puVar21 = puVar15;
      if ((undefined8 *)*puVar15 != (undefined8 *)0x0) {
        do {
          while (puVar10 = puVar11, puVar17 = puVar10, iVar4 < *(int *)((long)puVar10 + 0x1c)) {
            puVar11 = (undefined8 *)*puVar10;
            puVar21 = puVar10;
            if ((undefined8 *)*puVar10 == (undefined8 *)0x0) goto LAB_00abf1e8;
          }
          if (iVar4 <= *(int *)((long)puVar10 + 0x1c)) goto LAB_00abf178;
          puVar11 = (undefined8 *)puVar10[1];
        } while ((undefined8 *)puVar10[1] != (undefined8 *)0x0);
        puVar21 = puVar10 + 1;
      }
LAB_00abf1e8:
      puVar10 = (undefined8 *)_Znwm(0x28);
      *puVar10 = 0;
      puVar10[1] = 0;
      puVar10[2] = puVar17;
      *puVar21 = puVar10;
      plVar12 = (long *)*plVar16;
      *(int *)((long)puVar10 + 0x1c) = iVar4;
      *(undefined4 *)(puVar10 + 4) = 0;
      puVar11 = puVar10;
      if (*plVar12 != 0) {
        *plVar16 = *plVar12;
        puVar11 = (undefined8 *)*puVar21;
      }
      FUN_0043bf04(*(undefined8 *)(param_1 + 0x50),puVar11);
      *(long *)(param_1 + 0x58) = *(long *)(param_1 + 0x58) + 1;
LAB_00abf178:
                    /* try { // try from 00abf17c to 00bbf23b has its CatchHandler @ 00abf07c */
      iVar18 = iVar18 + 1;
      *(int *)(puVar10 + 4) = (int)cVar5;
    } while (iVar18 != sVar7);
  }
  bVar6 = FUN_00480658(param_2);
  *(byte *)(param_1 + 0x6c) = bVar6 & 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00abf0bc"></a> `00abf0bc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00abf0c0"></a> `00abf0c0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abf0c4"></a> `00abf0c4` | `fc 6f 02 a9` | stp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abf0c8"></a> `00abf0c8` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abf0cc"></a> `00abf0cc` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abf0d0"></a> `00abf0d0` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abf0d4"></a> `00abf0d4` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abf0d8"></a> `00abf0d8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00abf0dc"></a> `00abf0dc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00abf0e0"></a> `00abf0e0` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00abf0e4"></a> `00abf0e4` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00abf0e8"></a> `00abf0e8` | `9a 05 e7 97` | bl 0x00480750 | `UNCONDITIONAL_CALL`
<a id="insn-00abf0ec"></a> `00abf0ec` | `60 62 00 b9` | str w0,[x19, #0x60] | `FALL_THROUGH`
<a id="insn-00abf0f0"></a> `00abf0f0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abf0f4"></a> `00abf0f4` | `97 05 e7 97` | bl 0x00480750 | `UNCONDITIONAL_CALL`
<a id="insn-00abf0f8"></a> `00abf0f8` | `60 66 00 b9` | str w0,[x19, #0x64] | `FALL_THROUGH`
<a id="insn-00abf0fc"></a> `00abf0fc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abf100"></a> `00abf100` | `94 05 e7 97` | bl 0x00480750 | `UNCONDITIONAL_CALL`
<a id="insn-00abf104"></a> `00abf104` | `60 6a 00 b9` | str w0,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00abf108"></a> `00abf108` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abf10c"></a> `00abf10c` | `f3 04 e7 97` | bl 0x004804d8 | `UNCONDITIONAL_CALL`
<a id="insn-00abf110"></a> `00abf110` | `f5 03 13 aa` | mov x21,x19 | `FALL_THROUGH`
<a id="insn-00abf114"></a> `00abf114` | `19 3c 00 13` | sxth w25,w0 | `FALL_THROUGH`
<a id="insn-00abf118"></a> `00abf118` | `a8 0e 43 f8` | ldr x8,[x21, #0x30]! | `FALL_THROUGH`
<a id="insn-00abf11c"></a> `00abf11c` | `3f 07 00 71` | cmp w25,#0x1 | `FALL_THROUGH`
<a id="insn-00abf120"></a> `00abf120` | `a8 06 00 f9` | str x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00abf124"></a> `00abf124` | `8a 08 00 54` | b.ge 0x00abf234 | `CONDITIONAL_JUMP`
<a id="insn-00abf128"></a> `00abf128` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abf12c"></a> `00abf12c` | `eb 04 e7 97` | bl 0x004804d8 | `UNCONDITIONAL_CALL`
<a id="insn-00abf130"></a> `00abf130` | `f8 03 13 aa` | mov x24,x19 | `FALL_THROUGH`
<a id="insn-00abf134"></a> `00abf134` | `16 3c 00 13` | sxth w22,w0 | `FALL_THROUGH`
<a id="insn-00abf138"></a> `00abf138` | `01 0f 45 f8` | ldr x1,[x24, #0x50]! | `FALL_THROUGH`
<a id="insn-00abf13c"></a> `00abf13c` | `15 23 00 d1` | sub x21,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00abf140"></a> `00abf140` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abf144"></a> `00abf144` | `92 0a ec 97` | bl 0x005c1b8c | `UNCONDITIONAL_CALL`
<a id="insn-00abf148"></a> `00abf148` | `df 06 00 71` | cmp w22,#0x1 | `FALL_THROUGH`
<a id="insn-00abf14c"></a> `00abf14c` | `1f 7f 00 a9` | stp xzr,xzr,[x24] | `FALL_THROUGH`
<a id="insn-00abf150"></a> `00abf150` | `b6 c3 1f b8` | stur w22,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00abf154"></a> `00abf154` | `18 83 1f f8` | stur x24,[x24, #-0x8] | `FALL_THROUGH`
<a id="insn-00abf158"></a> `00abf158` | `0b 0c 00 54` | b.lt 0x00abf2d8 | `CONDITIONAL_JUMP`
<a id="insn-00abf15c"></a> `00abf15c` | `fa 03 1f 2a` | mov w26,wzr | `FALL_THROUGH`
<a id="insn-00abf160"></a> `00abf160` | `0c 00 00 14` | b 0x00abf190 | `UNCONDITIONAL_JUMP`
<a id="insn-00abf164"></a> `00abf164` | `60 2a 40 f9` | ldr x0,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-00abf168"></a> `00abf168` | `67 f3 e5 97` | bl 0x0043bf04 | `UNCONDITIONAL_CALL`
<a id="insn-00abf16c"></a> `00abf16c` | `68 2e 40 f9` | ldr x8,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00abf170"></a> `00abf170` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00abf174"></a> `00abf174` | `68 2e 00 f9` | str x8,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00abf178"></a> `00abf178` | `a9 c3 5f b8` | ldur w9,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00abf17c"></a> `00abf17c` | `c8 1e 00 13` | sxtb w8,w22 | `FALL_THROUGH`
<a id="insn-00abf180"></a> `00abf180` | `5a 07 00 11` | add w26,w26,#0x1 | `FALL_THROUGH`
<a id="insn-00abf184"></a> `00abf184` | `5f 03 09 6b` | cmp w26,w9 | `FALL_THROUGH`
<a id="insn-00abf188"></a> `00abf188` | `e8 22 00 b9` | str w8,[x23, #0x20] | `FALL_THROUGH`
<a id="insn-00abf18c"></a> `00abf18c` | `60 0a 00 54` | b.eq 0x00abf2d8 | `CONDITIONAL_JUMP`
<a id="insn-00abf190"></a> `00abf190` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abf194"></a> `00abf194` | `d1 04 e7 97` | bl 0x004804d8 | `UNCONDITIONAL_CALL`
<a id="insn-00abf198"></a> `00abf198` | `1b 3c 00 13` | sxth w27,w0 | `FALL_THROUGH`
<a id="insn-00abf19c"></a> `00abf19c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abf1a0"></a> `00abf1a0` | `b6 04 e7 97` | bl 0x00480478 | `UNCONDITIONAL_CALL`
<a id="insn-00abf1a4"></a> `00abf1a4` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00abf1a8"></a> `00abf1a8` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00abf1ac"></a> `00abf1ac` | `fc 03 18 aa` | mov x28,x24 | `FALL_THROUGH`
<a id="insn-00abf1b0"></a> `00abf1b0` | `f7 03 18 aa` | mov x23,x24 | `FALL_THROUGH`
<a id="insn-00abf1b4"></a> `00abf1b4` | `a8 00 00 b5` | cbnz x8,0x00abf1c8 | `CONDITIONAL_JUMP`
<a id="insn-00abf1b8"></a> `00abf1b8` | `0c 00 00 14` | b 0x00abf1e8 | `UNCONDITIONAL_JUMP`
<a id="insn-00abf1bc"></a> `00abf1bc` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00abf1c0"></a> `00abf1c0` | `fc 03 17 aa` | mov x28,x23 | `FALL_THROUGH`
<a id="insn-00abf1c4"></a> `00abf1c4` | `28 01 00 b4` | cbz x8,0x00abf1e8 | `CONDITIONAL_JUMP`
<a id="insn-00abf1c8"></a> `00abf1c8` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00abf1cc"></a> `00abf1cc` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00abf1d0"></a> `00abf1d0` | `1f 01 1b 6b` | cmp w8,w27 | `FALL_THROUGH`
<a id="insn-00abf1d4"></a> `00abf1d4` | `4c ff ff 54` | b.gt 0x00abf1bc | `CONDITIONAL_JUMP`
<a id="insn-00abf1d8"></a> `00abf1d8` | `0a fd ff 54` | b.ge 0x00abf178 | `CONDITIONAL_JUMP`
<a id="insn-00abf1dc"></a> `00abf1dc` | `e8 06 40 f9` | ldr x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00abf1e0"></a> `00abf1e0` | `48 ff ff b5` | cbnz x8,0x00abf1c8 | `CONDITIONAL_JUMP`
<a id="insn-00abf1e4"></a> `00abf1e4` | `fc 22 00 91` | add x28,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00abf1e8"></a> `00abf1e8` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00abf1ec"></a> `00abf1ec` | `f9 03 17 aa` | mov x25,x23 | `FALL_THROUGH`
<a id="insn-00abf1f0"></a> `00abf1f0` | `50 67 06 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00abf1f4"></a> `00abf1f4` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00abf1f8"></a> `00abf1f8` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00abf1fc"></a> `00abf1fc` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00abf200"></a> `00abf200` | `19 08 00 f9` | str x25,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00abf204"></a> `00abf204` | `80 03 00 f9` | str x0,[x28] | `FALL_THROUGH`
<a id="insn-00abf208"></a> `00abf208` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00abf20c"></a> `00abf20c` | `1b fc 03 29` | stp w27,wzr,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00abf210"></a> `00abf210` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00abf214"></a> `00abf214` | `88 fa ff b4` | cbz x8,0x00abf164 | `CONDITIONAL_JUMP`
<a id="insn-00abf218"></a> `00abf218` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00abf21c"></a> `00abf21c` | `81 03 40 f9` | ldr x1,[x28] | `FALL_THROUGH`
<a id="insn-00abf220"></a> `00abf220` | `d1 ff ff 17` | b 0x00abf164 | `UNCONDITIONAL_JUMP`
<a id="insn-00abf224"></a> `00abf224` | `5c 47 00 b8` | str w28,[x26], #0x4 | `FALL_THROUGH`
<a id="insn-00abf228"></a> `00abf228` | `39 07 00 71` | subs w25,w25,#0x1 | `FALL_THROUGH`
<a id="insn-00abf22c"></a> `00abf22c` | `7a 1e 00 f9` | str x26,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00abf230"></a> `00abf230` | `c0 f7 ff 54` | b.eq 0x00abf128 | `CONDITIONAL_JUMP`
<a id="insn-00abf234"></a> `00abf234` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abf238"></a> `00abf238` | `a8 04 e7 97` | bl 0x004804d8 | `UNCONDITIONAL_CALL`
<a id="insn-00abf23c"></a> `00abf23c` | `7a a2 43 a9` | ldp x26,x8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00abf240"></a> `00abf240` | `1c 3c 00 13` | sxth w28,w0 | `FALL_THROUGH`
<a id="insn-00abf244"></a> `00abf244` | `5f 03 08 eb` | cmp x26,x8 | `FALL_THROUGH`
<a id="insn-00abf248"></a> `00abf248` | `e3 fe ff 54` | b.cc 0x00abf224 | `CONDITIONAL_JUMP`
<a id="insn-00abf24c"></a> `00abf24c` | `b6 02 40 f9` | ldr x22,[x21] | `FALL_THROUGH`
<a id="insn-00abf250"></a> `00abf250` | `57 03 16 cb` | sub x23,x26,x22 | `FALL_THROUGH`
<a id="insn-00abf254"></a> `00abf254` | `fa fe 42 93` | asr x26,x23,#0x2 | `FALL_THROUGH`
<a id="insn-00abf258"></a> `00abf258` | `49 07 00 91` | add x9,x26,#0x1 | `FALL_THROUGH`
<a id="insn-00abf25c"></a> `00abf25c` | `2a fd 7e d3` | lsr x10,x9,#0x3e | `FALL_THROUGH`
<a id="insn-00abf260"></a> `00abf260` | `4a 05 00 b5` | cbnz x10,0x00abf308 | `CONDITIONAL_JUMP`
<a id="insn-00abf264"></a> `00abf264` | `08 01 16 cb` | sub x8,x8,x22 | `FALL_THROUGH`
<a id="insn-00abf268"></a> `00abf268` | `0a fd 41 93` | asr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00abf26c"></a> `00abf26c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00abf270"></a> `00abf270` | `49 81 89 9a` | csel x9,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00abf274"></a> `00abf274` | `ea f3 7e b2` | orr x10,xzr,#0x7ffffffffffffffc | `FALL_THROUGH`
<a id="insn-00abf278"></a> `00abf278` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-00abf27c"></a> `00abf27c` | `08 00 f8 92` | mov x8,#0x3fffffffffffffff | `FALL_THROUGH`
<a id="insn-00abf280"></a> `00abf280` | `3b 31 88 9a` | csel x27,x9,x8,cc | `FALL_THROUGH`
<a id="insn-00abf284"></a> `00abf284` | `fb 00 00 b4` | cbz x27,0x00abf2a0 | `CONDITIONAL_JUMP`
<a id="insn-00abf288"></a> `00abf288` | `68 ff 7e d3` | lsr x8,x27,#0x3e | `FALL_THROUGH`
<a id="insn-00abf28c"></a> `00abf28c` | `28 04 00 b5` | cbnz x8,0x00abf310 | `CONDITIONAL_JUMP`
<a id="insn-00abf290"></a> `00abf290` | `60 f7 7e d3` | lsl x0,x27,#0x2 | `FALL_THROUGH`
<a id="insn-00abf294"></a> `00abf294` | `27 67 06 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00abf298"></a> `00abf298` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00abf29c"></a> `00abf29c` | `02 00 00 14` | b 0x00abf2a4 | `UNCONDITIONAL_JUMP`
<a id="insn-00abf2a0"></a> `00abf2a0` | `f8 03 1f aa` | mov x24,xzr | `FALL_THROUGH`
<a id="insn-00abf2a4"></a> `00abf2a4` | `1a 0b 1a 8b` | add x26,x24,x26, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00abf2a8"></a> `00abf2a8` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00abf2ac"></a> `00abf2ac` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00abf2b0"></a> `00abf2b0` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00abf2b4"></a> `00abf2b4` | `1b 0b 1b 8b` | add x27,x24,x27, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00abf2b8"></a> `00abf2b8` | `5c 47 00 b8` | str w28,[x26], #0x4 | `FALL_THROUGH`
<a id="insn-00abf2bc"></a> `00abf2bc` | `79 67 06 94` | bl 0x00c590a0 | `UNCONDITIONAL_CALL`
<a id="insn-00abf2c0"></a> `00abf2c0` | `78 6a 03 a9` | stp x24,x26,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00abf2c4"></a> `00abf2c4` | `7b 22 00 f9` | str x27,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00abf2c8"></a> `00abf2c8` | `16 fb ff b4` | cbz x22,0x00abf228 | `CONDITIONAL_JUMP`
<a id="insn-00abf2cc"></a> `00abf2cc` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00abf2d0"></a> `00abf2d0` | `20 67 06 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00abf2d4"></a> `00abf2d4` | `d5 ff ff 17` | b 0x00abf228 | `UNCONDITIONAL_JUMP`
<a id="insn-00abf2d8"></a> `00abf2d8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abf2dc"></a> `00abf2dc` | `df 04 e7 97` | bl 0x00480658 | `UNCONDITIONAL_CALL`
<a id="insn-00abf2e0"></a> `00abf2e0` | `08 00 00 12` | and w8,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00abf2e4"></a> `00abf2e4` | `68 b2 01 39` | strb w8,[x19, #0x6c] | `FALL_THROUGH`
<a id="insn-00abf2e8"></a> `00abf2e8` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abf2ec"></a> `00abf2ec` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abf2f0"></a> `00abf2f0` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abf2f4"></a> `00abf2f4` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abf2f8"></a> `00abf2f8` | `fc 6f 42 a9` | ldp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abf2fc"></a> `00abf2fc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abf300"></a> `00abf300` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00abf304"></a> `00abf304` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00abf308"></a> `00abf308` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abf30c"></a> `00abf30c` | `25 c6 e6 97` | bl 0x00470ba0 | `CALL_TERMINATOR`
<a id="insn-00abf310"></a> `00abf310` | `c4 07 e6 97` | bl 0x00441220 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00abf0bc`](#insn-00abf0bc) 範囲 `[['00abf0bc', '00abf127']]`
  - `CONDITIONAL_JUMP` [`00abf124`](#insn-00abf124) → [`00abf234`](#insn-00abf234)
  - `FALL_THROUGH` [`00abf124`](#insn-00abf124) → [`00abf128`](#insn-00abf128)
- ブロック [`00abf128`](#insn-00abf128) 範囲 `[['00abf128', '00abf157']]`
  - `FALL_THROUGH` [`00abf154`](#insn-00abf154) → [`00abf158`](#insn-00abf158)
- ブロック [`00abf158`](#insn-00abf158) 範囲 `[['00abf158', '00abf15b']]`
  - `CONDITIONAL_JUMP` [`00abf158`](#insn-00abf158) → [`00abf2d8`](#insn-00abf2d8)
  - `FALL_THROUGH` [`00abf158`](#insn-00abf158) → [`00abf15c`](#insn-00abf15c)
- ブロック [`00abf15c`](#insn-00abf15c) 範囲 `[['00abf15c', '00abf163']]`
  - `UNCONDITIONAL_JUMP` [`00abf160`](#insn-00abf160) → [`00abf190`](#insn-00abf190)
- ブロック [`00abf164`](#insn-00abf164) 範囲 `[['00abf164', '00abf177']]`
  - `FALL_THROUGH` [`00abf174`](#insn-00abf174) → [`00abf178`](#insn-00abf178)
- ブロック [`00abf178`](#insn-00abf178) 範囲 `[['00abf178', '00abf17b']]`
  - `FALL_THROUGH` [`00abf178`](#insn-00abf178) → [`00abf17c`](#insn-00abf17c)
- ブロック [`00abf17c`](#insn-00abf17c) 範囲 `[['00abf17c', '00abf18f']]`
  - `CONDITIONAL_JUMP` [`00abf18c`](#insn-00abf18c) → [`00abf2d8`](#insn-00abf2d8)
  - `FALL_THROUGH` [`00abf18c`](#insn-00abf18c) → [`00abf190`](#insn-00abf190)
- ブロック [`00abf190`](#insn-00abf190) 範囲 `[['00abf190', '00abf1b7']]`
  - `CONDITIONAL_JUMP` [`00abf1b4`](#insn-00abf1b4) → [`00abf1c8`](#insn-00abf1c8)
  - `FALL_THROUGH` [`00abf1b4`](#insn-00abf1b4) → [`00abf1b8`](#insn-00abf1b8)
- ブロック [`00abf1b8`](#insn-00abf1b8) 範囲 `[['00abf1b8', '00abf1bb']]`
  - `UNCONDITIONAL_JUMP` [`00abf1b8`](#insn-00abf1b8) → [`00abf1e8`](#insn-00abf1e8)
- ブロック [`00abf1bc`](#insn-00abf1bc) 範囲 `[['00abf1bc', '00abf1c7']]`
  - `CONDITIONAL_JUMP` [`00abf1c4`](#insn-00abf1c4) → [`00abf1e8`](#insn-00abf1e8)
  - `FALL_THROUGH` [`00abf1c4`](#insn-00abf1c4) → [`00abf1c8`](#insn-00abf1c8)
- ブロック [`00abf1c8`](#insn-00abf1c8) 範囲 `[['00abf1c8', '00abf1d7']]`
  - `CONDITIONAL_JUMP` [`00abf1d4`](#insn-00abf1d4) → [`00abf1bc`](#insn-00abf1bc)
  - `FALL_THROUGH` [`00abf1d4`](#insn-00abf1d4) → [`00abf1d8`](#insn-00abf1d8)
- ブロック [`00abf1d8`](#insn-00abf1d8) 範囲 `[['00abf1d8', '00abf1db']]`
  - `CONDITIONAL_JUMP` [`00abf1d8`](#insn-00abf1d8) → [`00abf178`](#insn-00abf178)
  - `FALL_THROUGH` [`00abf1d8`](#insn-00abf1d8) → [`00abf1dc`](#insn-00abf1dc)
- ブロック [`00abf1dc`](#insn-00abf1dc) 範囲 `[['00abf1dc', '00abf1e3']]`
  - `CONDITIONAL_JUMP` [`00abf1e0`](#insn-00abf1e0) → [`00abf1c8`](#insn-00abf1c8)
  - `FALL_THROUGH` [`00abf1e0`](#insn-00abf1e0) → [`00abf1e4`](#insn-00abf1e4)
- ブロック [`00abf1e4`](#insn-00abf1e4) 範囲 `[['00abf1e4', '00abf1e7']]`
  - `FALL_THROUGH` [`00abf1e4`](#insn-00abf1e4) → [`00abf1e8`](#insn-00abf1e8)
- ブロック [`00abf1e8`](#insn-00abf1e8) 範囲 `[['00abf1e8', '00abf217']]`
  - `CONDITIONAL_JUMP` [`00abf214`](#insn-00abf214) → [`00abf164`](#insn-00abf164)
  - `FALL_THROUGH` [`00abf214`](#insn-00abf214) → [`00abf218`](#insn-00abf218)
- ブロック [`00abf218`](#insn-00abf218) 範囲 `[['00abf218', '00abf223']]`
  - `UNCONDITIONAL_JUMP` [`00abf220`](#insn-00abf220) → [`00abf164`](#insn-00abf164)
- ブロック [`00abf224`](#insn-00abf224) 範囲 `[['00abf224', '00abf227']]`
  - `FALL_THROUGH` [`00abf224`](#insn-00abf224) → [`00abf228`](#insn-00abf228)
- ブロック [`00abf228`](#insn-00abf228) 範囲 `[['00abf228', '00abf233']]`
  - `CONDITIONAL_JUMP` [`00abf230`](#insn-00abf230) → [`00abf128`](#insn-00abf128)
  - `FALL_THROUGH` [`00abf230`](#insn-00abf230) → [`00abf234`](#insn-00abf234)
- ブロック [`00abf234`](#insn-00abf234) 範囲 `[['00abf234', '00abf23b']]`
  - `FALL_THROUGH` [`00abf238`](#insn-00abf238) → [`00abf23c`](#insn-00abf23c)
- ブロック [`00abf23c`](#insn-00abf23c) 範囲 `[['00abf23c', '00abf243']]`
  - `FALL_THROUGH` [`00abf240`](#insn-00abf240) → [`00abf244`](#insn-00abf244)
- ブロック [`00abf244`](#insn-00abf244) 範囲 `[['00abf244', '00abf24b']]`
  - `CONDITIONAL_JUMP` [`00abf248`](#insn-00abf248) → [`00abf224`](#insn-00abf224)
  - `FALL_THROUGH` [`00abf248`](#insn-00abf248) → [`00abf24c`](#insn-00abf24c)
- ブロック [`00abf24c`](#insn-00abf24c) 範囲 `[['00abf24c', '00abf263']]`
  - `CONDITIONAL_JUMP` [`00abf260`](#insn-00abf260) → [`00abf308`](#insn-00abf308)
  - `FALL_THROUGH` [`00abf260`](#insn-00abf260) → [`00abf264`](#insn-00abf264)
- ブロック [`00abf264`](#insn-00abf264) 範囲 `[['00abf264', '00abf273']]`
  - `FALL_THROUGH` [`00abf270`](#insn-00abf270) → [`00abf274`](#insn-00abf274)
- ブロック [`00abf274`](#insn-00abf274) 範囲 `[['00abf274', '00abf287']]`
  - `CONDITIONAL_JUMP` [`00abf284`](#insn-00abf284) → [`00abf2a0`](#insn-00abf2a0)
  - `FALL_THROUGH` [`00abf284`](#insn-00abf284) → [`00abf288`](#insn-00abf288)
- ブロック [`00abf288`](#insn-00abf288) 範囲 `[['00abf288', '00abf28f']]`
  - `CONDITIONAL_JUMP` [`00abf28c`](#insn-00abf28c) → [`00abf310`](#insn-00abf310)
  - `FALL_THROUGH` [`00abf28c`](#insn-00abf28c) → [`00abf290`](#insn-00abf290)
- ブロック [`00abf290`](#insn-00abf290) 範囲 `[['00abf290', '00abf29f']]`
  - `UNCONDITIONAL_JUMP` [`00abf29c`](#insn-00abf29c) → [`00abf2a4`](#insn-00abf2a4)
- ブロック [`00abf2a0`](#insn-00abf2a0) 範囲 `[['00abf2a0', '00abf2a3']]`
  - `FALL_THROUGH` [`00abf2a0`](#insn-00abf2a0) → [`00abf2a4`](#insn-00abf2a4)
- ブロック [`00abf2a4`](#insn-00abf2a4) 範囲 `[['00abf2a4', '00abf2cb']]`
  - `CONDITIONAL_JUMP` [`00abf2c8`](#insn-00abf2c8) → [`00abf228`](#insn-00abf228)
  - `FALL_THROUGH` [`00abf2c8`](#insn-00abf2c8) → [`00abf2cc`](#insn-00abf2cc)
- ブロック [`00abf2cc`](#insn-00abf2cc) 範囲 `[['00abf2cc', '00abf2d7']]`
  - `UNCONDITIONAL_JUMP` [`00abf2d4`](#insn-00abf2d4) → [`00abf228`](#insn-00abf228)
- ブロック [`00abf2d8`](#insn-00abf2d8) 範囲 `[['00abf2d8', '00abf307']]`
- ブロック [`00abf308`](#insn-00abf308) 範囲 `[['00abf308', '00abf30f']]`
- ブロック [`00abf310`](#insn-00abf310) 範囲 `[['00abf310', '00abf313']]`

## 命令位置別の参照

- [`00abf0c0`](#insn-00abf0c0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0c4`](#insn-00abf0c4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0c8`](#insn-00abf0c8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0cc`](#insn-00abf0cc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0d0`](#insn-00abf0d0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0d4`](#insn-00abf0d4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0e8`](#insn-00abf0e8) → [`00480750`](../00480/00480750.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480750` · 推定シンボル `None` · 推定型 `None`
- [`00abf0f4`](#insn-00abf0f4) → [`00480750`](../00480/00480750.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480750` · 推定シンボル `None` · 推定型 `None`
- [`00abf100`](#insn-00abf100) → [`00480750`](../00480/00480750.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480750` · 推定シンボル `None` · 推定型 `None`
- [`00abf10c`](#insn-00abf10c) → [`004804d8`](../00480/004804d8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004804d8` · 推定シンボル `None` · 推定型 `None`
- [`00abf124`](#insn-00abf124) → [`00abf234`](#insn-00abf234) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf12c`](#insn-00abf12c) → [`004804d8`](../00480/004804d8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004804d8` · 推定シンボル `None` · 推定型 `None`
- [`00abf144`](#insn-00abf144) → [`005c1b8c`](../005c1/005c1b8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c1b8c` · 推定シンボル `None` · 推定型 `None`
- [`00abf150`](#insn-00abf150) → `Stack[-0x64]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf158`](#insn-00abf158) → [`00abf2d8`](#insn-00abf2d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf160`](#insn-00abf160) → [`00abf190`](#insn-00abf190) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf168`](#insn-00abf168) → [`0043bf04`](../0043b/0043bf04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bf04` · 推定シンボル `None` · 推定型 `None`
- [`00abf178`](#insn-00abf178) → `Stack[-0x64]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf18c`](#insn-00abf18c) → [`00abf2d8`](#insn-00abf2d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf194`](#insn-00abf194) → [`004804d8`](../00480/004804d8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004804d8` · 推定シンボル `None` · 推定型 `None`
- [`00abf1a0`](#insn-00abf1a0) → [`00480478`](../00480/00480478.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480478` · 推定シンボル `None` · 推定型 `None`
- [`00abf1b4`](#insn-00abf1b4) → [`00abf1c8`](#insn-00abf1c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf1b8`](#insn-00abf1b8) → [`00abf1e8`](#insn-00abf1e8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf1c4`](#insn-00abf1c4) → [`00abf1e8`](#insn-00abf1e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf1d4`](#insn-00abf1d4) → [`00abf1bc`](#insn-00abf1bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf1d8`](#insn-00abf1d8) → [`00abf178`](#insn-00abf178) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf1e0`](#insn-00abf1e0) → [`00abf1c8`](#insn-00abf1c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf1f0`](#insn-00abf1f0) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00abf214`](#insn-00abf214) → [`00abf164`](#insn-00abf164) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf220`](#insn-00abf220) → [`00abf164`](#insn-00abf164) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf230`](#insn-00abf230) → [`00abf128`](#insn-00abf128) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf238`](#insn-00abf238) → [`004804d8`](../00480/004804d8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004804d8` · 推定シンボル `None` · 推定型 `None`
- [`00abf248`](#insn-00abf248) → [`00abf224`](#insn-00abf224) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf260`](#insn-00abf260) → [`00abf308`](#insn-00abf308) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf284`](#insn-00abf284) → [`00abf2a0`](#insn-00abf2a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf28c`](#insn-00abf28c) → [`00abf310`](#insn-00abf310) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf294`](#insn-00abf294) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00abf29c`](#insn-00abf29c) → [`00abf2a4`](#insn-00abf2a4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf2bc`](#insn-00abf2bc) → [`00c590a0`](../00c59/00c590a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590a0` · 推定シンボル `None` · 推定型 `None`
- [`00abf2c8`](#insn-00abf2c8) → [`00abf228`](#insn-00abf228) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf2d0`](#insn-00abf2d0) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00abf2d4`](#insn-00abf2d4) → [`00abf228`](#insn-00abf228) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf2dc`](#insn-00abf2dc) → [`00480658`](../00480/00480658.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480658` · 推定シンボル `None` · 推定型 `None`
- [`00abf2e8`](#insn-00abf2e8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf2ec`](#insn-00abf2ec) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf2f0`](#insn-00abf2f0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf2f4`](#insn-00abf2f4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf2f8`](#insn-00abf2f8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf2fc`](#insn-00abf2fc) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf30c`](#insn-00abf30c) → [`00470ba0`](../00470/00470ba0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00470ba0` · 推定シンボル `None` · 推定型 `None`
- [`00abf310`](#insn-00abf310) → [`00441220`](../00441/00441220.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00441220` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00abf0c0`](#insn-00abf0c0)

~~~json
{
  "source": "00abf0c0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0c4`](#insn-00abf0c4)

~~~json
{
  "source": "00abf0c4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0c8`](#insn-00abf0c8)

~~~json
{
  "source": "00abf0c8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0cc`](#insn-00abf0cc)

~~~json
{
  "source": "00abf0cc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0d0`](#insn-00abf0d0)

~~~json
{
  "source": "00abf0d0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0d4`](#insn-00abf0d4)

~~~json
{
  "source": "00abf0d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0e8`](#insn-00abf0e8)

~~~json
{
  "source": "00abf0e8",
  "target": "00480750",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf0f4`](#insn-00abf0f4)

~~~json
{
  "source": "00abf0f4",
  "target": "00480750",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf100`](#insn-00abf100)

~~~json
{
  "source": "00abf100",
  "target": "00480750",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf10c`](#insn-00abf10c)

~~~json
{
  "source": "00abf10c",
  "target": "004804d8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf124`](#insn-00abf124)

~~~json
{
  "source": "00abf124",
  "target": "00abf234",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf12c`](#insn-00abf12c)

~~~json
{
  "source": "00abf12c",
  "target": "004804d8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf144`](#insn-00abf144)

~~~json
{
  "source": "00abf144",
  "target": "005c1b8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf150`](#insn-00abf150)

~~~json
{
  "source": "00abf150",
  "target": "Stack[-0x64]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf158`](#insn-00abf158)

~~~json
{
  "source": "00abf158",
  "target": "00abf2d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf160`](#insn-00abf160)

~~~json
{
  "source": "00abf160",
  "target": "00abf190",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf168`](#insn-00abf168)

~~~json
{
  "source": "00abf168",
  "target": "0043bf04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf178`](#insn-00abf178)

~~~json
{
  "source": "00abf178",
  "target": "Stack[-0x64]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf18c`](#insn-00abf18c)

~~~json
{
  "source": "00abf18c",
  "target": "00abf2d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf194`](#insn-00abf194)

~~~json
{
  "source": "00abf194",
  "target": "004804d8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf1a0`](#insn-00abf1a0)

~~~json
{
  "source": "00abf1a0",
  "target": "00480478",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf1b4`](#insn-00abf1b4)

~~~json
{
  "source": "00abf1b4",
  "target": "00abf1c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf1b8`](#insn-00abf1b8)

~~~json
{
  "source": "00abf1b8",
  "target": "00abf1e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf1c4`](#insn-00abf1c4)

~~~json
{
  "source": "00abf1c4",
  "target": "00abf1e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf1d4`](#insn-00abf1d4)

~~~json
{
  "source": "00abf1d4",
  "target": "00abf1bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf1d8`](#insn-00abf1d8)

~~~json
{
  "source": "00abf1d8",
  "target": "00abf178",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf1e0`](#insn-00abf1e0)

~~~json
{
  "source": "00abf1e0",
  "target": "00abf1c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf1f0`](#insn-00abf1f0)

~~~json
{
  "source": "00abf1f0",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf214`](#insn-00abf214)

~~~json
{
  "source": "00abf214",
  "target": "00abf164",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf220`](#insn-00abf220)

~~~json
{
  "source": "00abf220",
  "target": "00abf164",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf230`](#insn-00abf230)

~~~json
{
  "source": "00abf230",
  "target": "00abf128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf238`](#insn-00abf238)

~~~json
{
  "source": "00abf238",
  "target": "004804d8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf248`](#insn-00abf248)

~~~json
{
  "source": "00abf248",
  "target": "00abf224",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf260`](#insn-00abf260)

~~~json
{
  "source": "00abf260",
  "target": "00abf308",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf284`](#insn-00abf284)

~~~json
{
  "source": "00abf284",
  "target": "00abf2a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf28c`](#insn-00abf28c)

~~~json
{
  "source": "00abf28c",
  "target": "00abf310",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf294`](#insn-00abf294)

~~~json
{
  "source": "00abf294",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf29c`](#insn-00abf29c)

~~~json
{
  "source": "00abf29c",
  "target": "00abf2a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf2bc`](#insn-00abf2bc)

~~~json
{
  "source": "00abf2bc",
  "target": "00c590a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf2c8`](#insn-00abf2c8)

~~~json
{
  "source": "00abf2c8",
  "target": "00abf228",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf2d0`](#insn-00abf2d0)

~~~json
{
  "source": "00abf2d0",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf2d4`](#insn-00abf2d4)

~~~json
{
  "source": "00abf2d4",
  "target": "00abf228",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf2dc`](#insn-00abf2dc)

~~~json
{
  "source": "00abf2dc",
  "target": "00480658",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf2e8`](#insn-00abf2e8)

~~~json
{
  "source": "00abf2e8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf2ec`](#insn-00abf2ec)

~~~json
{
  "source": "00abf2ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf2f0`](#insn-00abf2f0)

~~~json
{
  "source": "00abf2f0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf2f4`](#insn-00abf2f4)

~~~json
{
  "source": "00abf2f4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf2f8`](#insn-00abf2f8)

~~~json
{
  "source": "00abf2f8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf2fc`](#insn-00abf2fc)

~~~json
{
  "source": "00abf2fc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf30c`](#insn-00abf30c)

~~~json
{
  "source": "00abf30c",
  "target": "00470ba0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf310`](#insn-00abf310)

~~~json
{
  "source": "00abf310",
  "target": "00441220",
  "target_space": "ram",
  "resolution": "function"
}
~~~
