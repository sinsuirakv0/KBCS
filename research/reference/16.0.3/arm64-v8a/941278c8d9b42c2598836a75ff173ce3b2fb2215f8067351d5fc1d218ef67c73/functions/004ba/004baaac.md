# 004baaac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `004ba78c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004ba78c.md) · 移動量 `+0x320`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0006.md#compare-e5e6114d66fff1495e49f3f08c4aa0d6)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004baaac",
  "name": "_ZN5BotanrsERKNS_6BigIntEm",
  "size": 472,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e3604d2a6cfd92d5cade5852652548e4c2b671aae1946540add308241ad0b24f",
  "source_text_sha256": "e3604d2a6cfd92d5cade5852652548e4c2b671aae1946540add308241ad0b24f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004baaac",
        "004bac83"
      ]
    ],
    "bytes_sha256": "b662908c0a8ae7933d2428d390b7c2bae855ffc83489d7c56678ef90576acb9b",
    "instruction_count": 118,
    "instruction_bytes": 472,
    "body_bytes": 472,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c59d80](../00c59/00c59d80.md)

## 呼び出し先

- [00c599c0](../00c59/00c599c0.md)
- [00c59be0](../00c59/00c59be0.md)
- [00c59cc0](../00c59/00c59cc0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2923 bytes

~~~c

void _ZN5BotanrsERKNS_6BigIntEm(long *param_1,long *param_2,ulong param_3)

{
  uint uVar1;
  uint uVar2;
  undefined8 *puVar3;
  bool bVar4;
  ulong uVar5;
  long lVar6;
  undefined4 *puVar7;
  ulong uVar8;
  ulong uVar9;
  long lVar10;
  uint uVar11;
  undefined4 *puVar12;
  undefined8 *puVar13;
  long lVar14;
  undefined8 *puVar15;
  ulong uVar16;
  ulong uVar17;
  undefined8 uVar18;
  undefined8 uVar19;
  undefined8 uVar20;
  
  if (param_3 == 0) {
    _ZN5Botan6BigIntC2ERKS0_(param_1,param_2);
    return;
  }
  lVar6 = *param_2;
  lVar14 = param_2[1] - lVar6;
  uVar17 = lVar14 >> 2;
  uVar8 = uVar17;
  if (lVar14 != 0) {
    do {
      if (*(int *)(lVar6 + -4 + uVar8 * 4) != 0) goto LAB_004baaf8;
      uVar8 = uVar8 - 1;
    } while (uVar8 != 0);
LAB_004bac34:
    _ZN5Botan6BigIntC1Em(param_1,0);
    return;
  }
LAB_004baaf8:
  if (uVar8 == 0) goto LAB_004bac34;
  uVar8 = uVar8 - 1;
  if (uVar8 < uVar17) {
    uVar11 = *(uint *)(lVar6 + uVar8 * 4);
  }
  else {
    uVar11 = 0;
  }
  lVar14 = 0x20;
  do {
    if ((uVar11 >> (ulong)((int)lVar14 - 1U & 0x1f) & 1) != 0) break;
    lVar14 = lVar14 + -1;
  } while (lVar14 != 0);
  if (lVar14 + uVar8 * 0x20 <= param_3) goto LAB_004bac34;
  uVar8 = param_3 >> 5;
  if (param_2[1] != lVar6) {
    do {
      if (*(int *)(lVar6 + -4 + uVar17 * 4) != 0) break;
      uVar17 = uVar17 - 1;
    } while (uVar17 != 0);
  }
  _ZN5Botan6BigIntC1ENS0_4SignEm(param_1,(int)param_2[3],uVar17 - uVar8);
  uVar5 = uVar17 - uVar8;
  if (uVar17 < uVar8) {
    return;
  }
  if (uVar5 == 0) {
    return;
  }
  lVar6 = *param_1;
  lVar14 = *param_2;
  param_3 = param_3 & 0x1f;
  if ((uVar5 < 8) || (lVar10 = uVar8 * 4 + lVar14, (ulong)(lVar6 - lVar10) < 0x20)) {
    uVar9 = 0;
  }
  else {
    uVar9 = uVar5 & 0xfffffffffffffff8;
    puVar13 = (undefined8 *)(lVar10 + 0x10);
    puVar15 = (undefined8 *)(lVar6 + 0x10);
    uVar16 = uVar9;
    do {
      puVar3 = puVar13 + -1;
      uVar18 = puVar13[-2];
      uVar20 = puVar13[1];
      uVar19 = *puVar13;
      uVar16 = uVar16 - 8;
      puVar13 = puVar13 + 4;
      puVar15[-1] = *puVar3;
      puVar15[-2] = uVar18;
      puVar15[1] = uVar20;
      *puVar15 = uVar19;
      puVar15 = puVar15 + 4;
    } while (uVar16 != 0);
    if (uVar5 == uVar9) goto LAB_004babec;
  }
  lVar10 = (uVar9 + uVar8) - uVar17;
  puVar7 = (undefined4 *)(lVar14 + uVar9 * 4 + uVar8 * 4);
  puVar12 = (undefined4 *)(lVar6 + uVar9 * 4);
  do {
    bVar4 = lVar10 != -1;
    lVar10 = lVar10 + 1;
    *puVar12 = *puVar7;
    puVar7 = puVar7 + 1;
    puVar12 = puVar12 + 1;
  } while (bVar4);
LAB_004babec:
  if (param_3 != 0) {
    uVar11 = 0;
    do {
      lVar14 = uVar5 * 4;
      uVar5 = uVar5 - 1;
      uVar1 = *(uint *)(lVar6 + -4 + lVar14);
      uVar2 = uVar1 >> param_3 | uVar11;
      uVar11 = uVar1 << (ulong)(0x20U - (int)param_3 & 0x1f);
      *(uint *)(lVar6 + -4 + lVar14) = uVar2;
    } while (uVar5 != 0);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004baaac"></a> `004baaac` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-004baab0"></a> `004baab0` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004baab4"></a> `004baab4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004baab8"></a> `004baab8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004baabc"></a> `004baabc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-004baac0"></a> `004baac0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004baac4"></a> `004baac4` | `61 02 00 b4` | cbz x1,0x004bab10 | `CONDITIONAL_JUMP`
<a id="insn-004baac8"></a> `004baac8` | `6a 2e 40 a9` | ldp x10,x11,[x19] | `FALL_THROUGH`
<a id="insn-004baacc"></a> `004baacc` | `69 01 0a eb` | subs x9,x11,x10 | `FALL_THROUGH`
<a id="insn-004baad0"></a> `004baad0` | `34 fd 42 93` | asr x20,x9,#0x2 | `FALL_THROUGH`
<a id="insn-004baad4"></a> `004baad4` | `49 11 00 d1` | sub x9,x10,#0x4 | `FALL_THROUGH`
<a id="insn-004baad8"></a> `004baad8` | `ec 03 14 aa` | mov x12,x20 | `FALL_THROUGH`
<a id="insn-004baadc"></a> `004baadc` | `e0 00 00 54` | b.eq 0x004baaf8 | `CONDITIONAL_JUMP`
<a id="insn-004baae0"></a> `004baae0` | `ec 03 14 aa` | mov x12,x20 | `FALL_THROUGH`
<a id="insn-004baae4"></a> `004baae4` | `2d 79 6c b8` | ldr w13,[x9, x12, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004baae8"></a> `004baae8` | `8d 00 00 35` | cbnz w13,0x004baaf8 | `CONDITIONAL_JUMP`
<a id="insn-004baaec"></a> `004baaec` | `8c 05 00 f1` | subs x12,x12,#0x1 | `FALL_THROUGH`
<a id="insn-004baaf0"></a> `004baaf0` | `a1 ff ff 54` | b.ne 0x004baae4 | `CONDITIONAL_JUMP`
<a id="insn-004baaf4"></a> `004baaf4` | `50 00 00 14` | b 0x004bac34 | `UNCONDITIONAL_JUMP`
<a id="insn-004baaf8"></a> `004baaf8` | `ec 09 00 b4` | cbz x12,0x004bac34 | `CONDITIONAL_JUMP`
<a id="insn-004baafc"></a> `004baafc` | `8c 05 00 d1` | sub x12,x12,#0x1 | `FALL_THROUGH`
<a id="insn-004bab00"></a> `004bab00` | `9f 02 0c eb` | cmp x20,x12 | `FALL_THROUGH`
<a id="insn-004bab04"></a> `004bab04` | `49 01 00 54` | b.ls 0x004bab2c | `CONDITIONAL_JUMP`
<a id="insn-004bab08"></a> `004bab08` | `4d 79 6c b8` | ldr w13,[x10, x12, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004bab0c"></a> `004bab0c` | `09 00 00 14` | b 0x004bab30 | `UNCONDITIONAL_JUMP`
<a id="insn-004bab10"></a> `004bab10` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-004bab14"></a> `004bab14` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-004bab18"></a> `004bab18` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004bab1c"></a> `004bab1c` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004bab20"></a> `004bab20` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004bab24"></a> `004bab24` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-004bab28"></a> `004bab28` | `2e 7c 1e 14` | b 0x00c59be0 | `CALL_TERMINATOR`
<a id="insn-004bab2c"></a> `004bab2c` | `ed 03 1f 2a` | mov w13,wzr | `FALL_THROUGH`
<a id="insn-004bab30"></a> `004bab30` | `8c e9 7b d3` | lsl x12,x12,#0x5 | `FALL_THROUGH`
<a id="insn-004bab34"></a> `004bab34` | `0e 04 80 52` | mov w14,#0x20 | `FALL_THROUGH`
<a id="insn-004bab38"></a> `004bab38` | `cf 05 00 51` | sub w15,w14,#0x1 | `FALL_THROUGH`
<a id="insn-004bab3c"></a> `004bab3c` | `af 25 cf 1a` | lsr w15,w13,w15 | `FALL_THROUGH`
<a id="insn-004bab40"></a> `004bab40` | `6f 00 00 37` | tbnz w15,#0x0,0x004bab4c | `CONDITIONAL_JUMP`
<a id="insn-004bab44"></a> `004bab44` | `ce 05 00 f1` | subs x14,x14,#0x1 | `FALL_THROUGH`
<a id="insn-004bab48"></a> `004bab48` | `81 ff ff 54` | b.ne 0x004bab38 | `CONDITIONAL_JUMP`
<a id="insn-004bab4c"></a> `004bab4c` | `cc 01 0c 8b` | add x12,x14,x12 | `FALL_THROUGH`
<a id="insn-004bab50"></a> `004bab50` | `9f 01 01 eb` | cmp x12,x1 | `FALL_THROUGH`
<a id="insn-004bab54"></a> `004bab54` | `09 07 00 54` | b.ls 0x004bac34 | `CONDITIONAL_JUMP`
<a id="insn-004bab58"></a> `004bab58` | `35 fc 45 d3` | lsr x21,x1,#0x5 | `FALL_THROUGH`
<a id="insn-004bab5c"></a> `004bab5c` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-004bab60"></a> `004bab60` | `a0 00 00 54` | b.eq 0x004bab74 | `CONDITIONAL_JUMP`
<a id="insn-004bab64"></a> `004bab64` | `2a 79 74 b8` | ldr w10,[x9, x20, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004bab68"></a> `004bab68` | `6a 00 00 35` | cbnz w10,0x004bab74 | `CONDITIONAL_JUMP`
<a id="insn-004bab6c"></a> `004bab6c` | `94 06 00 f1` | subs x20,x20,#0x1 | `FALL_THROUGH`
<a id="insn-004bab70"></a> `004bab70` | `a1 ff ff 54` | b.ne 0x004bab64 | `CONDITIONAL_JUMP`
<a id="insn-004bab74"></a> `004bab74` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-004bab78"></a> `004bab78` | `61 1a 40 b9` | ldr w1,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-004bab7c"></a> `004bab7c` | `82 02 15 eb` | subs x2,x20,x21 | `FALL_THROUGH`
<a id="insn-004bab80"></a> `004bab80` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-004bab84"></a> `004bab84` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-004bab88"></a> `004bab88` | `4e 7c 1e 94` | bl 0x00c59cc0 | `UNCONDITIONAL_CALL`
<a id="insn-004bab8c"></a> `004bab8c` | `88 02 15 eb` | subs x8,x20,x21 | `FALL_THROUGH`
<a id="insn-004bab90"></a> `004bab90` | `83 04 00 54` | b.cc 0x004bac20 | `CONDITIONAL_JUMP`
<a id="insn-004bab94"></a> `004bab94` | `68 04 00 b4` | cbz x8,0x004bac20 | `CONDITIONAL_JUMP`
<a id="insn-004bab98"></a> `004bab98` | `ea 02 40 f9` | ldr x10,[x23] | `FALL_THROUGH`
<a id="insn-004bab9c"></a> `004bab9c` | `6b 02 40 f9` | ldr x11,[x19] | `FALL_THROUGH`
<a id="insn-004baba0"></a> `004baba0` | `1f 21 00 f1` | cmp x8,#0x8 | `FALL_THROUGH`
<a id="insn-004baba4"></a> `004baba4` | `c9 12 40 92` | and x9,x22,#0x1f | `FALL_THROUGH`
<a id="insn-004baba8"></a> `004baba8` | `c3 00 00 54` | b.cc 0x004babc0 | `CONDITIONAL_JUMP`
<a id="insn-004babac"></a> `004babac` | `ac f6 7e d3` | lsl x12,x21,#0x2 | `FALL_THROUGH`
<a id="insn-004babb0"></a> `004babb0` | `8d 01 0b 8b` | add x13,x12,x11 | `FALL_THROUGH`
<a id="insn-004babb4"></a> `004babb4` | `4c 01 0d cb` | sub x12,x10,x13 | `FALL_THROUGH`
<a id="insn-004babb8"></a> `004babb8` | `9f 81 00 f1` | cmp x12,#0x20 | `FALL_THROUGH`
<a id="insn-004babbc"></a> `004babbc` | `a2 04 00 54` | b.cs 0x004bac50 | `CONDITIONAL_JUMP`
<a id="insn-004babc0"></a> `004babc0` | `ec 03 1f aa` | mov x12,xzr | `FALL_THROUGH`
<a id="insn-004babc4"></a> `004babc4` | `8d f5 7e d3` | lsl x13,x12,#0x2 | `FALL_THROUGH`
<a id="insn-004babc8"></a> `004babc8` | `8c 01 15 8b` | add x12,x12,x21 | `FALL_THROUGH`
<a id="insn-004babcc"></a> `004babcc` | `8c 01 14 cb` | sub x12,x12,x20 | `FALL_THROUGH`
<a id="insn-004babd0"></a> `004babd0` | `ae 09 15 8b` | add x14,x13,x21, LSL #0x2 | `FALL_THROUGH`
<a id="insn-004babd4"></a> `004babd4` | `4d 01 0d 8b` | add x13,x10,x13 | `FALL_THROUGH`
<a id="insn-004babd8"></a> `004babd8` | `6b 01 0e 8b` | add x11,x11,x14 | `FALL_THROUGH`
<a id="insn-004babdc"></a> `004babdc` | `6e 45 40 b8` | ldr w14,[x11], #0x4 | `FALL_THROUGH`
<a id="insn-004babe0"></a> `004babe0` | `8c 05 00 b1` | adds x12,x12,#0x1 | `FALL_THROUGH`
<a id="insn-004babe4"></a> `004babe4` | `ae 45 00 b8` | str w14,[x13], #0x4 | `FALL_THROUGH`
<a id="insn-004babe8"></a> `004babe8` | `a3 ff ff 54` | b.cc 0x004babdc | `CONDITIONAL_JUMP`
<a id="insn-004babec"></a> `004babec` | `a9 01 00 b4` | cbz x9,0x004bac20 | `CONDITIONAL_JUMP`
<a id="insn-004babf0"></a> `004babf0` | `0c 04 80 52` | mov w12,#0x20 | `FALL_THROUGH`
<a id="insn-004babf4"></a> `004babf4` | `eb 03 1f 2a` | mov w11,wzr | `FALL_THROUGH`
<a id="insn-004babf8"></a> `004babf8` | `4a 11 00 d1` | sub x10,x10,#0x4 | `FALL_THROUGH`
<a id="insn-004babfc"></a> `004babfc` | `8c 01 09 4b` | sub w12,w12,w9 | `FALL_THROUGH`
<a id="insn-004bac00"></a> `004bac00` | `0d f5 7e d3` | lsl x13,x8,#0x2 | `FALL_THROUGH`
<a id="insn-004bac04"></a> `004bac04` | `08 05 00 f1` | subs x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004bac08"></a> `004bac08` | `4e 69 6d b8` | ldr w14,[x10, x13, LSL #0x0] | `FALL_THROUGH`
<a id="insn-004bac0c"></a> `004bac0c` | `cf 25 c9 1a` | lsr w15,w14,w9 | `FALL_THROUGH`
<a id="insn-004bac10"></a> `004bac10` | `ef 01 0b 2a` | orr w15,w15,w11 | `FALL_THROUGH`
<a id="insn-004bac14"></a> `004bac14` | `cb 21 cc 1a` | lsl w11,w14,w12 | `FALL_THROUGH`
<a id="insn-004bac18"></a> `004bac18` | `4f 69 2d b8` | str w15,[x10, x13, LSL #0x0] | `FALL_THROUGH`
<a id="insn-004bac1c"></a> `004bac1c` | `21 ff ff 54` | b.ne 0x004bac00 | `CONDITIONAL_JUMP`
<a id="insn-004bac20"></a> `004bac20` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004bac24"></a> `004bac24` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004bac28"></a> `004bac28` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004bac2c"></a> `004bac2c` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-004bac30"></a> `004bac30` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004bac34"></a> `004bac34` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-004bac38"></a> `004bac38` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-004bac3c"></a> `004bac3c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004bac40"></a> `004bac40` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004bac44"></a> `004bac44` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004bac48"></a> `004bac48` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-004bac4c"></a> `004bac4c` | `5d 7b 1e 14` | b 0x00c599c0 | `CALL_TERMINATOR`
<a id="insn-004bac50"></a> `004bac50` | `0c f1 7d 92` | and x12,x8,#-0x8 | `FALL_THROUGH`
<a id="insn-004bac54"></a> `004bac54` | `ad 41 00 91` | add x13,x13,#0x10 | `FALL_THROUGH`
<a id="insn-004bac58"></a> `004bac58` | `4e 41 00 91` | add x14,x10,#0x10 | `FALL_THROUGH`
<a id="insn-004bac5c"></a> `004bac5c` | `ef 03 0c aa` | mov x15,x12 | `FALL_THROUGH`
<a id="insn-004bac60"></a> `004bac60` | `a0 85 7f ad` | ldp q0,q1,[x13, #-0x10] | `FALL_THROUGH`
<a id="insn-004bac64"></a> `004bac64` | `ef 21 00 f1` | subs x15,x15,#0x8 | `FALL_THROUGH`
<a id="insn-004bac68"></a> `004bac68` | `ad 81 00 91` | add x13,x13,#0x20 | `FALL_THROUGH`
<a id="insn-004bac6c"></a> `004bac6c` | `c0 85 3f ad` | stp q0,q1,[x14, #-0x10] | `FALL_THROUGH`
<a id="insn-004bac70"></a> `004bac70` | `ce 81 00 91` | add x14,x14,#0x20 | `FALL_THROUGH`
<a id="insn-004bac74"></a> `004bac74` | `61 ff ff 54` | b.ne 0x004bac60 | `CONDITIONAL_JUMP`
<a id="insn-004bac78"></a> `004bac78` | `1f 01 0c eb` | cmp x8,x12 | `FALL_THROUGH`
<a id="insn-004bac7c"></a> `004bac7c` | `80 fb ff 54` | b.eq 0x004babec | `CONDITIONAL_JUMP`
<a id="insn-004bac80"></a> `004bac80` | `d1 ff ff 17` | b 0x004babc4 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`004baaac`](#insn-004baaac) 範囲 `[['004baaac', '004baac7']]`
  - `CONDITIONAL_JUMP` [`004baac4`](#insn-004baac4) → [`004bab10`](#insn-004bab10)
  - `FALL_THROUGH` [`004baac4`](#insn-004baac4) → [`004baac8`](#insn-004baac8)
- ブロック [`004baac8`](#insn-004baac8) 範囲 `[['004baac8', '004baadf']]`
  - `CONDITIONAL_JUMP` [`004baadc`](#insn-004baadc) → [`004baaf8`](#insn-004baaf8)
  - `FALL_THROUGH` [`004baadc`](#insn-004baadc) → [`004baae0`](#insn-004baae0)
- ブロック [`004baae0`](#insn-004baae0) 範囲 `[['004baae0', '004baae3']]`
  - `FALL_THROUGH` [`004baae0`](#insn-004baae0) → [`004baae4`](#insn-004baae4)
- ブロック [`004baae4`](#insn-004baae4) 範囲 `[['004baae4', '004baaeb']]`
  - `CONDITIONAL_JUMP` [`004baae8`](#insn-004baae8) → [`004baaf8`](#insn-004baaf8)
  - `FALL_THROUGH` [`004baae8`](#insn-004baae8) → [`004baaec`](#insn-004baaec)
- ブロック [`004baaec`](#insn-004baaec) 範囲 `[['004baaec', '004baaf3']]`
  - `CONDITIONAL_JUMP` [`004baaf0`](#insn-004baaf0) → [`004baae4`](#insn-004baae4)
  - `FALL_THROUGH` [`004baaf0`](#insn-004baaf0) → [`004baaf4`](#insn-004baaf4)
- ブロック [`004baaf4`](#insn-004baaf4) 範囲 `[['004baaf4', '004baaf7']]`
  - `UNCONDITIONAL_JUMP` [`004baaf4`](#insn-004baaf4) → [`004bac34`](#insn-004bac34)
- ブロック [`004baaf8`](#insn-004baaf8) 範囲 `[['004baaf8', '004baafb']]`
  - `CONDITIONAL_JUMP` [`004baaf8`](#insn-004baaf8) → [`004bac34`](#insn-004bac34)
  - `FALL_THROUGH` [`004baaf8`](#insn-004baaf8) → [`004baafc`](#insn-004baafc)
- ブロック [`004baafc`](#insn-004baafc) 範囲 `[['004baafc', '004bab07']]`
  - `CONDITIONAL_JUMP` [`004bab04`](#insn-004bab04) → [`004bab2c`](#insn-004bab2c)
  - `FALL_THROUGH` [`004bab04`](#insn-004bab04) → [`004bab08`](#insn-004bab08)
- ブロック [`004bab08`](#insn-004bab08) 範囲 `[['004bab08', '004bab0f']]`
  - `UNCONDITIONAL_JUMP` [`004bab0c`](#insn-004bab0c) → [`004bab30`](#insn-004bab30)
- ブロック [`004bab10`](#insn-004bab10) 範囲 `[['004bab10', '004bab2b']]`
- ブロック [`004bab2c`](#insn-004bab2c) 範囲 `[['004bab2c', '004bab2f']]`
  - `FALL_THROUGH` [`004bab2c`](#insn-004bab2c) → [`004bab30`](#insn-004bab30)
- ブロック [`004bab30`](#insn-004bab30) 範囲 `[['004bab30', '004bab37']]`
  - `FALL_THROUGH` [`004bab34`](#insn-004bab34) → [`004bab38`](#insn-004bab38)
- ブロック [`004bab38`](#insn-004bab38) 範囲 `[['004bab38', '004bab43']]`
  - `CONDITIONAL_JUMP` [`004bab40`](#insn-004bab40) → [`004bab4c`](#insn-004bab4c)
  - `FALL_THROUGH` [`004bab40`](#insn-004bab40) → [`004bab44`](#insn-004bab44)
- ブロック [`004bab44`](#insn-004bab44) 範囲 `[['004bab44', '004bab4b']]`
  - `CONDITIONAL_JUMP` [`004bab48`](#insn-004bab48) → [`004bab38`](#insn-004bab38)
  - `FALL_THROUGH` [`004bab48`](#insn-004bab48) → [`004bab4c`](#insn-004bab4c)
- ブロック [`004bab4c`](#insn-004bab4c) 範囲 `[['004bab4c', '004bab57']]`
  - `CONDITIONAL_JUMP` [`004bab54`](#insn-004bab54) → [`004bac34`](#insn-004bac34)
  - `FALL_THROUGH` [`004bab54`](#insn-004bab54) → [`004bab58`](#insn-004bab58)
- ブロック [`004bab58`](#insn-004bab58) 範囲 `[['004bab58', '004bab63']]`
  - `CONDITIONAL_JUMP` [`004bab60`](#insn-004bab60) → [`004bab74`](#insn-004bab74)
  - `FALL_THROUGH` [`004bab60`](#insn-004bab60) → [`004bab64`](#insn-004bab64)
- ブロック [`004bab64`](#insn-004bab64) 範囲 `[['004bab64', '004bab6b']]`
  - `CONDITIONAL_JUMP` [`004bab68`](#insn-004bab68) → [`004bab74`](#insn-004bab74)
  - `FALL_THROUGH` [`004bab68`](#insn-004bab68) → [`004bab6c`](#insn-004bab6c)
- ブロック [`004bab6c`](#insn-004bab6c) 範囲 `[['004bab6c', '004bab73']]`
  - `CONDITIONAL_JUMP` [`004bab70`](#insn-004bab70) → [`004bab64`](#insn-004bab64)
  - `FALL_THROUGH` [`004bab70`](#insn-004bab70) → [`004bab74`](#insn-004bab74)
- ブロック [`004bab74`](#insn-004bab74) 範囲 `[['004bab74', '004bab93']]`
  - `CONDITIONAL_JUMP` [`004bab90`](#insn-004bab90) → [`004bac20`](#insn-004bac20)
  - `FALL_THROUGH` [`004bab90`](#insn-004bab90) → [`004bab94`](#insn-004bab94)
- ブロック [`004bab94`](#insn-004bab94) 範囲 `[['004bab94', '004bab97']]`
  - `CONDITIONAL_JUMP` [`004bab94`](#insn-004bab94) → [`004bac20`](#insn-004bac20)
  - `FALL_THROUGH` [`004bab94`](#insn-004bab94) → [`004bab98`](#insn-004bab98)
- ブロック [`004bab98`](#insn-004bab98) 範囲 `[['004bab98', '004babab']]`
  - `CONDITIONAL_JUMP` [`004baba8`](#insn-004baba8) → [`004babc0`](#insn-004babc0)
  - `FALL_THROUGH` [`004baba8`](#insn-004baba8) → [`004babac`](#insn-004babac)
- ブロック [`004babac`](#insn-004babac) 範囲 `[['004babac', '004babbf']]`
  - `CONDITIONAL_JUMP` [`004babbc`](#insn-004babbc) → [`004bac50`](#insn-004bac50)
  - `FALL_THROUGH` [`004babbc`](#insn-004babbc) → [`004babc0`](#insn-004babc0)
- ブロック [`004babc0`](#insn-004babc0) 範囲 `[['004babc0', '004babc3']]`
  - `FALL_THROUGH` [`004babc0`](#insn-004babc0) → [`004babc4`](#insn-004babc4)
- ブロック [`004babc4`](#insn-004babc4) 範囲 `[['004babc4', '004babdb']]`
  - `FALL_THROUGH` [`004babd8`](#insn-004babd8) → [`004babdc`](#insn-004babdc)
- ブロック [`004babdc`](#insn-004babdc) 範囲 `[['004babdc', '004babeb']]`
  - `CONDITIONAL_JUMP` [`004babe8`](#insn-004babe8) → [`004babdc`](#insn-004babdc)
  - `FALL_THROUGH` [`004babe8`](#insn-004babe8) → [`004babec`](#insn-004babec)
- ブロック [`004babec`](#insn-004babec) 範囲 `[['004babec', '004babef']]`
  - `CONDITIONAL_JUMP` [`004babec`](#insn-004babec) → [`004bac20`](#insn-004bac20)
  - `FALL_THROUGH` [`004babec`](#insn-004babec) → [`004babf0`](#insn-004babf0)
- ブロック [`004babf0`](#insn-004babf0) 範囲 `[['004babf0', '004babff']]`
  - `FALL_THROUGH` [`004babfc`](#insn-004babfc) → [`004bac00`](#insn-004bac00)
- ブロック [`004bac00`](#insn-004bac00) 範囲 `[['004bac00', '004bac1f']]`
  - `CONDITIONAL_JUMP` [`004bac1c`](#insn-004bac1c) → [`004bac00`](#insn-004bac00)
  - `FALL_THROUGH` [`004bac1c`](#insn-004bac1c) → [`004bac20`](#insn-004bac20)
- ブロック [`004bac20`](#insn-004bac20) 範囲 `[['004bac20', '004bac33']]`
- ブロック [`004bac34`](#insn-004bac34) 範囲 `[['004bac34', '004bac4f']]`
- ブロック [`004bac50`](#insn-004bac50) 範囲 `[['004bac50', '004bac5f']]`
  - `FALL_THROUGH` [`004bac5c`](#insn-004bac5c) → [`004bac60`](#insn-004bac60)
- ブロック [`004bac60`](#insn-004bac60) 範囲 `[['004bac60', '004bac77']]`
  - `CONDITIONAL_JUMP` [`004bac74`](#insn-004bac74) → [`004bac60`](#insn-004bac60)
  - `FALL_THROUGH` [`004bac74`](#insn-004bac74) → [`004bac78`](#insn-004bac78)
- ブロック [`004bac78`](#insn-004bac78) 範囲 `[['004bac78', '004bac7f']]`
  - `CONDITIONAL_JUMP` [`004bac7c`](#insn-004bac7c) → [`004babec`](#insn-004babec)
  - `FALL_THROUGH` [`004bac7c`](#insn-004bac7c) → [`004bac80`](#insn-004bac80)
- ブロック [`004bac80`](#insn-004bac80) 範囲 `[['004bac80', '004bac83']]`
  - `UNCONDITIONAL_JUMP` [`004bac80`](#insn-004bac80) → [`004babc4`](#insn-004babc4)

## 命令位置別の参照

- [`004baaac`](#insn-004baaac) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004baab0`](#insn-004baab0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004baab4`](#insn-004baab4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004baab8`](#insn-004baab8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004baac4`](#insn-004baac4) → [`004bab10`](#insn-004bab10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004baadc`](#insn-004baadc) → [`004baaf8`](#insn-004baaf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004baae8`](#insn-004baae8) → [`004baaf8`](#insn-004baaf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004baaf0`](#insn-004baaf0) → [`004baae4`](#insn-004baae4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004baaf4`](#insn-004baaf4) → [`004bac34`](#insn-004bac34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004baaf8`](#insn-004baaf8) → [`004bac34`](#insn-004bac34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bab04`](#insn-004bab04) → [`004bab2c`](#insn-004bab2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bab0c`](#insn-004bab0c) → [`004bab30`](#insn-004bab30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bab18`](#insn-004bab18) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bab1c`](#insn-004bab1c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bab20`](#insn-004bab20) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bab24`](#insn-004bab24) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bab28`](#insn-004bab28) → [`00c59be0`](../00c59/00c59be0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59be0` · 推定シンボル `None` · 推定型 `None`
- [`004bab40`](#insn-004bab40) → [`004bab4c`](#insn-004bab4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bab48`](#insn-004bab48) → [`004bab38`](#insn-004bab38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bab54`](#insn-004bab54) → [`004bac34`](#insn-004bac34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bab60`](#insn-004bab60) → [`004bab74`](#insn-004bab74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bab68`](#insn-004bab68) → [`004bab74`](#insn-004bab74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bab70`](#insn-004bab70) → [`004bab64`](#insn-004bab64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bab88`](#insn-004bab88) → [`00c59cc0`](../00c59/00c59cc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59cc0` · 推定シンボル `None` · 推定型 `None`
- [`004bab90`](#insn-004bab90) → [`004bac20`](#insn-004bac20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bab94`](#insn-004bab94) → [`004bac20`](#insn-004bac20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004baba8`](#insn-004baba8) → [`004babc0`](#insn-004babc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004babbc`](#insn-004babbc) → [`004bac50`](#insn-004bac50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004babe8`](#insn-004babe8) → [`004babdc`](#insn-004babdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004babec`](#insn-004babec) → [`004bac20`](#insn-004bac20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bac1c`](#insn-004bac1c) → [`004bac00`](#insn-004bac00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bac20`](#insn-004bac20) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bac24`](#insn-004bac24) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bac28`](#insn-004bac28) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bac2c`](#insn-004bac2c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bac3c`](#insn-004bac3c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bac40`](#insn-004bac40) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bac44`](#insn-004bac44) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bac48`](#insn-004bac48) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bac4c`](#insn-004bac4c) → [`00c599c0`](../00c59/00c599c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c599c0` · 推定シンボル `None` · 推定型 `None`
- [`004bac74`](#insn-004bac74) → [`004bac60`](#insn-004bac60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bac7c`](#insn-004bac7c) → [`004babec`](#insn-004babec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bac80`](#insn-004bac80) → [`004babc4`](#insn-004babc4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004baaac`](#insn-004baaac)

~~~json
{
  "source": "004baaac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004baab0`](#insn-004baab0)

~~~json
{
  "source": "004baab0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004baab4`](#insn-004baab4)

~~~json
{
  "source": "004baab4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004baab8`](#insn-004baab8)

~~~json
{
  "source": "004baab8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004baac4`](#insn-004baac4)

~~~json
{
  "source": "004baac4",
  "target": "004bab10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004baadc`](#insn-004baadc)

~~~json
{
  "source": "004baadc",
  "target": "004baaf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004baae8`](#insn-004baae8)

~~~json
{
  "source": "004baae8",
  "target": "004baaf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004baaf0`](#insn-004baaf0)

~~~json
{
  "source": "004baaf0",
  "target": "004baae4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004baaf4`](#insn-004baaf4)

~~~json
{
  "source": "004baaf4",
  "target": "004bac34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004baaf8`](#insn-004baaf8)

~~~json
{
  "source": "004baaf8",
  "target": "004bac34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bab04`](#insn-004bab04)

~~~json
{
  "source": "004bab04",
  "target": "004bab2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bab0c`](#insn-004bab0c)

~~~json
{
  "source": "004bab0c",
  "target": "004bab30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bab18`](#insn-004bab18)

~~~json
{
  "source": "004bab18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bab1c`](#insn-004bab1c)

~~~json
{
  "source": "004bab1c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bab20`](#insn-004bab20)

~~~json
{
  "source": "004bab20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bab24`](#insn-004bab24)

~~~json
{
  "source": "004bab24",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bab28`](#insn-004bab28)

~~~json
{
  "source": "004bab28",
  "target": "00c59be0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bab40`](#insn-004bab40)

~~~json
{
  "source": "004bab40",
  "target": "004bab4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bab48`](#insn-004bab48)

~~~json
{
  "source": "004bab48",
  "target": "004bab38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bab54`](#insn-004bab54)

~~~json
{
  "source": "004bab54",
  "target": "004bac34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bab60`](#insn-004bab60)

~~~json
{
  "source": "004bab60",
  "target": "004bab74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bab68`](#insn-004bab68)

~~~json
{
  "source": "004bab68",
  "target": "004bab74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bab70`](#insn-004bab70)

~~~json
{
  "source": "004bab70",
  "target": "004bab64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bab88`](#insn-004bab88)

~~~json
{
  "source": "004bab88",
  "target": "00c59cc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bab90`](#insn-004bab90)

~~~json
{
  "source": "004bab90",
  "target": "004bac20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bab94`](#insn-004bab94)

~~~json
{
  "source": "004bab94",
  "target": "004bac20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004baba8`](#insn-004baba8)

~~~json
{
  "source": "004baba8",
  "target": "004babc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004babbc`](#insn-004babbc)

~~~json
{
  "source": "004babbc",
  "target": "004bac50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004babe8`](#insn-004babe8)

~~~json
{
  "source": "004babe8",
  "target": "004babdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004babec`](#insn-004babec)

~~~json
{
  "source": "004babec",
  "target": "004bac20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bac1c`](#insn-004bac1c)

~~~json
{
  "source": "004bac1c",
  "target": "004bac00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bac20`](#insn-004bac20)

~~~json
{
  "source": "004bac20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bac24`](#insn-004bac24)

~~~json
{
  "source": "004bac24",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bac28`](#insn-004bac28)

~~~json
{
  "source": "004bac28",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bac2c`](#insn-004bac2c)

~~~json
{
  "source": "004bac2c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bac3c`](#insn-004bac3c)

~~~json
{
  "source": "004bac3c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bac40`](#insn-004bac40)

~~~json
{
  "source": "004bac40",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bac44`](#insn-004bac44)

~~~json
{
  "source": "004bac44",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bac48`](#insn-004bac48)

~~~json
{
  "source": "004bac48",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bac4c`](#insn-004bac4c)

~~~json
{
  "source": "004bac4c",
  "target": "00c599c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bac74`](#insn-004bac74)

~~~json
{
  "source": "004bac74",
  "target": "004bac60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bac7c`](#insn-004bac7c)

~~~json
{
  "source": "004bac7c",
  "target": "004babec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bac80`](#insn-004bac80)

~~~json
{
  "source": "004bac80",
  "target": "004babc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
