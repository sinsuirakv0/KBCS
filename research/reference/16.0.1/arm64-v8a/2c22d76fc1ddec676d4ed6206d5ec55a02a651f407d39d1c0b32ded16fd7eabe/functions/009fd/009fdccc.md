# 009fdccc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `009fdb30`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fdb30.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0033.md#compare-d8e93194571f9dd35e27b6339dae854f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `009fdd20`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdd20.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0032.md#compare-109623109a0a290626ce693ceaa2e4d8)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009fdccc",
  "name": "FUN_009fdccc",
  "size": 712,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cb0b20f0d4f71347146e8d396449a7a129770a3e5f43dde0f524354350596b4c",
  "source_text_sha256": "cb0b20f0d4f71347146e8d396449a7a129770a3e5f43dde0f524354350596b4c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009fdccc",
        "009fdf93"
      ]
    ],
    "bytes_sha256": "5787b968b00e9e48777b6e78651a56dbf07598cc790e15b0cd03b3768fe0634e",
    "instruction_count": 178,
    "instruction_bytes": 712,
    "body_bytes": 712,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [009f92c8](../009f9/009f92c8.md)
- [009fdccc](../009fd/009fdccc.md)
- [009fdf94](../009fd/009fdf94.md)

## 呼び出し先

- [009fdccc](../009fd/009fdccc.md)
- [009fdf94](../009fd/009fdf94.md)
- [009fe20c](../009fe/009fe20c.md)
- [00c57ee0](../00c57/00c57ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5052 bytes

~~~c

void FUN_009fdccc(undefined8 *param_1,undefined8 *param_2,ulong param_3,undefined8 *param_4,
                 long param_5)

{
  undefined4 uVar1;
  long lVar2;
  long lVar3;
  long lVar4;
  undefined8 *puVar5;
  undefined8 *puVar6;
  undefined4 uVar7;
  undefined8 uVar8;
  int iVar9;
  long lVar10;
  ulong uVar11;
  undefined8 *puVar12;
  long lVar13;
  undefined8 *puVar14;
  
  lVar2 = tpidr_el0;
  lVar3 = *(long *)(lVar2 + 0x28);
  if (1 < param_3) {
    if (param_3 == 2) {
      if (*(int *)(param_2 + -1) < *(int *)((long)param_1 + 4)) {
        uVar8 = *param_1;
        uVar7 = *(undefined4 *)((long)param_2 + -4);
        *param_1 = *(undefined8 *)((long)param_2 + -0xc);
        uVar1 = *(undefined4 *)(param_1 + 1);
        *(undefined4 *)(param_1 + 1) = uVar7;
        *(undefined8 *)((long)param_2 + -0xc) = uVar8;
        *(undefined4 *)((long)param_2 + -4) = uVar1;
      }
    }
    else if ((long)param_3 < 0x81) {
      if ((param_1 != param_2) && ((undefined8 *)((long)param_1 + 0xc) != param_2)) {
        lVar4 = 0;
        puVar6 = (undefined8 *)((long)param_1 + 0xc);
        puVar5 = param_1;
        do {
          puVar12 = puVar6;
          uVar8 = *puVar12;
          iVar9 = (int)((ulong)uVar8 >> 0x20);
          if (iVar9 < *(int *)((long)puVar5 + 4)) {
            uVar7 = *(undefined4 *)((long)puVar5 + 0x14);
            lVar13 = lVar4;
            do {
              lVar10 = lVar13;
              puVar6 = (undefined8 *)((long)param_1 + lVar10);
              *(undefined8 *)((long)puVar6 + 0xc) = *puVar6;
              *(undefined4 *)((long)puVar6 + 0x14) = *(undefined4 *)(puVar6 + 1);
              puVar5 = param_1;
              if (lVar10 == 0) goto LAB_009fdd98;
              lVar13 = lVar10 + -0xc;
            } while (iVar9 < *(int *)(puVar6 + -1));
            puVar5 = (undefined8 *)((long)param_1 + lVar10);
LAB_009fdd98:
            *puVar5 = uVar8;
            *(undefined4 *)(puVar5 + 1) = uVar7;
          }
          lVar4 = lVar4 + 0xc;
          puVar6 = (undefined8 *)((long)puVar12 + 0xc);
          puVar5 = puVar12;
        } while ((undefined8 *)((long)puVar12 + 0xc) != param_2);
      }
    }
    else {
      uVar11 = param_3 >> 1;
      lVar4 = (long)param_1 + uVar11 * 0xc;
      lVar13 = param_3 - uVar11;
      if (param_5 < (long)param_3) {
        FUN_009fdccc(param_1,lVar4,uVar11);
        FUN_009fdccc(lVar4,param_2,lVar13,param_4,param_5);
        if (*(long *)(lVar2 + 0x28) == lVar3) {
          FUN_009fe20c(param_1,lVar4,param_2,uVar11,lVar13,param_4,param_5);
          return;
        }
        goto LAB_009fdf90;
      }
                    /* try { // try from 009fdeac to 00afdebb has its CatchHandler @ 009fe4e4 */
      FUN_009fdf94(param_1,lVar4,uVar11);
      puVar12 = (undefined8 *)((long)param_4 + uVar11 * 0xc);
      FUN_009fdf94(lVar4,param_2,lVar13,puVar12);
                    /* try { // try from 009fded4 to 00afdedf has its CatchHandler @ 009fe3e0 */
      puVar5 = (undefined8 *)((long)param_4 + param_3 * 0xc);
      puVar6 = puVar12;
      do {
                    /* try { // try from 009fdf00 to 00afdf07 has its CatchHandler @ 009fe3bc */
        if (puVar6 == puVar5) {
          if (param_4 != puVar12) {
            lVar4 = 0;
            do {
              puVar6 = (undefined8 *)((long)param_4 + lVar4);
              puVar5 = (undefined8 *)((long)param_1 + lVar4);
              lVar4 = lVar4 + 0xc;
              uVar8 = *puVar6;
              *(undefined4 *)(puVar5 + 1) = *(undefined4 *)(puVar6 + 1);
              *puVar5 = uVar8;
            } while ((undefined8 *)((long)param_4 + lVar4) != puVar12);
          }
          goto LAB_009fdd00;
        }
                    /* try { // try from 009fdf08 to 00afdfab has its CatchHandler @ 009fd500 */
        if (*(int *)((long)puVar6 + 4) < *(int *)((long)param_4 + 4)) {
          uVar7 = *(undefined4 *)(puVar6 + 1);
          uVar8 = *puVar6;
          puVar6 = (undefined8 *)((long)puVar6 + 0xc);
          puVar14 = param_4;
        }
        else {
          uVar7 = *(undefined4 *)(param_4 + 1);
          puVar14 = (undefined8 *)((long)param_4 + 0xc);
          uVar8 = *param_4;
        }
        *(undefined4 *)(param_1 + 1) = uVar7;
        *param_1 = uVar8;
                    /* try { // try from 009fdef0 to 00afdefb has its CatchHandler @ 009fe3cc */
        param_1 = (undefined8 *)((long)param_1 + 0xc);
        param_4 = puVar14;
      } while (puVar14 != puVar12);
      if (puVar6 != puVar5) {
        lVar4 = 0;
        do {
          puVar12 = (undefined8 *)((long)puVar6 + lVar4);
          puVar14 = (undefined8 *)((long)param_1 + lVar4);
          lVar4 = lVar4 + 0xc;
          uVar8 = *puVar12;
          *(undefined4 *)(puVar14 + 1) = *(undefined4 *)(puVar12 + 1);
          *puVar14 = uVar8;
        } while ((undefined8 *)((long)puVar6 + lVar4) != puVar5);
      }
    }
  }
LAB_009fdd00:
  if (*(long *)(lVar2 + 0x28) == lVar3) {
    return;
  }
LAB_009fdf90:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009fdccc"></a> `009fdccc` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-009fdcd0"></a> `009fdcd0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009fdcd4"></a> `009fdcd4` | `fb 1b 00 f9` | str x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009fdcd8"></a> `009fdcd8` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009fdcdc"></a> `009fdcdc` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009fdce0"></a> `009fdce0` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009fdce4"></a> `009fdce4` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-009fdce8"></a> `009fdce8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-009fdcec"></a> `009fdcec` | `5b d0 3b d5` | mrs x27,tpidr_el0 | `FALL_THROUGH`
<a id="insn-009fdcf0"></a> `009fdcf0` | `68 17 40 f9` | ldr x8,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-009fdcf4"></a> `009fdcf4` | `5f 08 00 f1` | cmp x2,#0x2 | `FALL_THROUGH`
<a id="insn-009fdcf8"></a> `009fdcf8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009fdcfc"></a> `009fdcfc` | `a2 01 00 54` | b.cs 0x009fdd30 | `CONDITIONAL_JUMP`
<a id="insn-009fdd00"></a> `009fdd00` | `68 17 40 f9` | ldr x8,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-009fdd04"></a> `009fdd04` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009fdd08"></a> `009fdd08` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009fdd0c"></a> `009fdd0c` | `21 14 00 54` | b.ne 0x009fdf90 | `CONDITIONAL_JUMP`
<a id="insn-009fdd10"></a> `009fdd10` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-009fdd14"></a> `009fdd14` | `fb 1b 40 f9` | ldr x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009fdd18"></a> `009fdd18` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009fdd1c"></a> `009fdd1c` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009fdd20"></a> `009fdd20` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009fdd24"></a> `009fdd24` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009fdd28"></a> `009fdd28` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-009fdd2c"></a> `009fdd2c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-009fdd30"></a> `009fdd30` | `e1 01 00 54` | b.ne 0x009fdd6c | `CONDITIONAL_JUMP`
<a id="insn-009fdd34"></a> `009fdd34` | `28 80 5f b8` | ldur w8,[x1, #-0x8] | `FALL_THROUGH`
<a id="insn-009fdd38"></a> `009fdd38` | `09 04 40 b9` | ldr w9,[x0, #0x4] | `FALL_THROUGH`
<a id="insn-009fdd3c"></a> `009fdd3c` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-009fdd40"></a> `009fdd40` | `0a fe ff 54` | b.ge 0x009fdd00 | `CONDITIONAL_JUMP`
<a id="insn-009fdd44"></a> `009fdd44` | `28 30 00 d1` | sub x8,x1,#0xc | `FALL_THROUGH`
<a id="insn-009fdd48"></a> `009fdd48` | `0b 00 40 f9` | ldr x11,[x0] | `FALL_THROUGH`
<a id="insn-009fdd4c"></a> `009fdd4c` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-009fdd50"></a> `009fdd50` | `0a 09 40 b9` | ldr w10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-009fdd54"></a> `009fdd54` | `09 00 00 f9` | str x9,[x0] | `FALL_THROUGH`
<a id="insn-009fdd58"></a> `009fdd58` | `09 08 40 b9` | ldr w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-009fdd5c"></a> `009fdd5c` | `0a 08 00 b9` | str w10,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-009fdd60"></a> `009fdd60` | `0b 01 00 f9` | str x11,[x8] | `FALL_THROUGH`
<a id="insn-009fdd64"></a> `009fdd64` | `09 09 00 b9` | str w9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-009fdd68"></a> `009fdd68` | `e6 ff ff 17` | b 0x009fdd00 | `UNCONDITIONAL_JUMP`
<a id="insn-009fdd6c"></a> `009fdd6c` | `5f 00 02 f1` | cmp x2,#0x80 | `FALL_THROUGH`
<a id="insn-009fdd70"></a> `009fdd70` | `cc 04 00 54` | b.gt 0x009fde08 | `CONDITIONAL_JUMP`
<a id="insn-009fdd74"></a> `009fdd74` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-009fdd78"></a> `009fdd78` | `40 fc ff 54` | b.eq 0x009fdd00 | `CONDITIONAL_JUMP`
<a id="insn-009fdd7c"></a> `009fdd7c` | `0a 30 00 91` | add x10,x0,#0xc | `FALL_THROUGH`
<a id="insn-009fdd80"></a> `009fdd80` | `5f 01 01 eb` | cmp x10,x1 | `FALL_THROUGH`
<a id="insn-009fdd84"></a> `009fdd84` | `e0 fb ff 54` | b.eq 0x009fdd00 | `CONDITIONAL_JUMP`
<a id="insn-009fdd88"></a> `009fdd88` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-009fdd8c"></a> `009fdd8c` | `eb 03 00 aa` | mov x11,x0 | `FALL_THROUGH`
<a id="insn-009fdd90"></a> `009fdd90` | `09 00 00 14` | b 0x009fddb4 | `UNCONDITIONAL_JUMP`
<a id="insn-009fdd94"></a> `009fdd94` | `ec 03 00 aa` | mov x12,x0 | `FALL_THROUGH`
<a id="insn-009fdd98"></a> `009fdd98` | `8a 01 00 f9` | str x10,[x12] | `FALL_THROUGH`
<a id="insn-009fdd9c"></a> `009fdd9c` | `8b 09 00 b9` | str w11,[x12, #0x8] | `FALL_THROUGH`
<a id="insn-009fdda0"></a> `009fdda0` | `2a 31 00 91` | add x10,x9,#0xc | `FALL_THROUGH`
<a id="insn-009fdda4"></a> `009fdda4` | `08 31 00 91` | add x8,x8,#0xc | `FALL_THROUGH`
<a id="insn-009fdda8"></a> `009fdda8` | `eb 03 09 aa` | mov x11,x9 | `FALL_THROUGH`
<a id="insn-009fddac"></a> `009fddac` | `5f 01 01 eb` | cmp x10,x1 | `FALL_THROUGH`
<a id="insn-009fddb0"></a> `009fddb0` | `80 fa ff 54` | b.eq 0x009fdd00 | `CONDITIONAL_JUMP`
<a id="insn-009fddb4"></a> `009fddb4` | `e9 03 0a aa` | mov x9,x10 | `FALL_THROUGH`
<a id="insn-009fddb8"></a> `009fddb8` | `4a 01 40 f9` | ldr x10,[x10] | `FALL_THROUGH`
<a id="insn-009fddbc"></a> `009fddbc` | `6d 05 40 b9` | ldr w13,[x11, #0x4] | `FALL_THROUGH`
<a id="insn-009fddc0"></a> `009fddc0` | `4c fd 60 d3` | lsr x12,x10,#0x20 | `FALL_THROUGH`
<a id="insn-009fddc4"></a> `009fddc4` | `9f 01 0d 6b` | cmp w12,w13 | `FALL_THROUGH`
<a id="insn-009fddc8"></a> `009fddc8` | `ca fe ff 54` | b.ge 0x009fdda0 | `CONDITIONAL_JUMP`
<a id="insn-009fddcc"></a> `009fddcc` | `6b 15 40 b9` | ldr w11,[x11, #0x14] | `FALL_THROUGH`
<a id="insn-009fddd0"></a> `009fddd0` | `ed 03 08 aa` | mov x13,x8 | `FALL_THROUGH`
<a id="insn-009fddd4"></a> `009fddd4` | `0e 00 0d 8b` | add x14,x0,x13 | `FALL_THROUGH`
<a id="insn-009fddd8"></a> `009fddd8` | `cf 01 40 f9` | ldr x15,[x14] | `FALL_THROUGH`
<a id="insn-009fdddc"></a> `009fdddc` | `d0 09 40 b9` | ldr w16,[x14, #0x8] | `FALL_THROUGH`
<a id="insn-009fdde0"></a> `009fdde0` | `cf c1 00 f8` | stur x15,[x14, #0xc] | `FALL_THROUGH`
<a id="insn-009fdde4"></a> `009fdde4` | `d0 15 00 b9` | str w16,[x14, #0x14] | `FALL_THROUGH`
<a id="insn-009fdde8"></a> `009fdde8` | `6d fd ff b4` | cbz x13,0x009fdd94 | `CONDITIONAL_JUMP`
<a id="insn-009fddec"></a> `009fddec` | `ce 81 5f b8` | ldur w14,[x14, #-0x8] | `FALL_THROUGH`
<a id="insn-009fddf0"></a> `009fddf0` | `ad 31 00 d1` | sub x13,x13,#0xc | `FALL_THROUGH`
<a id="insn-009fddf4"></a> `009fddf4` | `9f 01 0e 6b` | cmp w12,w14 | `FALL_THROUGH`
<a id="insn-009fddf8"></a> `009fddf8` | `eb fe ff 54` | b.lt 0x009fddd4 | `CONDITIONAL_JUMP`
<a id="insn-009fddfc"></a> `009fddfc` | `0c 00 0d 8b` | add x12,x0,x13 | `FALL_THROUGH`
<a id="insn-009fde00"></a> `009fde00` | `8c 31 00 91` | add x12,x12,#0xc | `FALL_THROUGH`
<a id="insn-009fde04"></a> `009fde04` | `e5 ff ff 17` | b 0x009fdd98 | `UNCONDITIONAL_JUMP`
<a id="insn-009fde08"></a> `009fde08` | `53 fc 41 d3` | lsr x19,x2,#0x1 | `FALL_THROUGH`
<a id="insn-009fde0c"></a> `009fde0c` | `88 01 80 52` | mov w8,#0xc | `FALL_THROUGH`
<a id="insn-009fde10"></a> `009fde10` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-009fde14"></a> `009fde14` | `5f 00 04 eb` | cmp x2,x4 | `FALL_THROUGH`
<a id="insn-009fde18"></a> `009fde18` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-009fde1c"></a> `009fde1c` | `75 02 08 9b` | madd x21,x19,x8,x0 | `FALL_THROUGH`
<a id="insn-009fde20"></a> `009fde20` | `56 00 13 cb` | sub x22,x2,x19 | `FALL_THROUGH`
<a id="insn-009fde24"></a> `009fde24` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-009fde28"></a> `009fde28` | `0d 04 00 54` | b.le 0x009fdea8 | `CONDITIONAL_JUMP`
<a id="insn-009fde2c"></a> `009fde2c` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-009fde30"></a> `009fde30` | `f9 03 03 aa` | mov x25,x3 | `FALL_THROUGH`
<a id="insn-009fde34"></a> `009fde34` | `fa 03 04 aa` | mov x26,x4 | `FALL_THROUGH`
<a id="insn-009fde38"></a> `009fde38` | `a5 ff ff 97` | bl 0x009fdccc | `UNCONDITIONAL_CALL`
<a id="insn-009fde3c"></a> `009fde3c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009fde40"></a> `009fde40` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-009fde44"></a> `009fde44` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-009fde48"></a> `009fde48` | `e3 03 19 aa` | mov x3,x25 | `FALL_THROUGH`
<a id="insn-009fde4c"></a> `009fde4c` | `e4 03 1a aa` | mov x4,x26 | `FALL_THROUGH`
<a id="insn-009fde50"></a> `009fde50` | `f8 03 19 aa` | mov x24,x25 | `FALL_THROUGH`
<a id="insn-009fde54"></a> `009fde54` | `f9 03 1a aa` | mov x25,x26 | `FALL_THROUGH`
<a id="insn-009fde58"></a> `009fde58` | `9d ff ff 97` | bl 0x009fdccc | `UNCONDITIONAL_CALL`
<a id="insn-009fde5c"></a> `009fde5c` | `68 17 40 f9` | ldr x8,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-009fde60"></a> `009fde60` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009fde64"></a> `009fde64` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009fde68"></a> `009fde68` | `41 09 00 54` | b.ne 0x009fdf90 | `CONDITIONAL_JUMP`
<a id="insn-009fde6c"></a> `009fde6c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-009fde70"></a> `009fde70` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-009fde74"></a> `009fde74` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-009fde78"></a> `009fde78` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-009fde7c"></a> `009fde7c` | `e4 03 16 aa` | mov x4,x22 | `FALL_THROUGH`
<a id="insn-009fde80"></a> `009fde80` | `e5 03 18 aa` | mov x5,x24 | `FALL_THROUGH`
<a id="insn-009fde84"></a> `009fde84` | `e6 03 19 aa` | mov x6,x25 | `FALL_THROUGH`
<a id="insn-009fde88"></a> `009fde88` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-009fde8c"></a> `009fde8c` | `fb 1b 40 f9` | ldr x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009fde90"></a> `009fde90` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009fde94"></a> `009fde94` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009fde98"></a> `009fde98` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009fde9c"></a> `009fde9c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009fdea0"></a> `009fdea0` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-009fdea4"></a> `009fdea4` | `da 00 00 14` | b 0x009fe20c | `CALL_TERMINATOR`
<a id="insn-009fdea8"></a> `009fdea8` | `f9 03 02 aa` | mov x25,x2 | `FALL_THROUGH`
<a id="insn-009fdeac"></a> `009fdeac` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-009fdeb0"></a> `009fdeb0` | `f8 03 03 aa` | mov x24,x3 | `FALL_THROUGH`
<a id="insn-009fdeb4"></a> `009fdeb4` | `38 00 00 94` | bl 0x009fdf94 | `UNCONDITIONAL_CALL`
<a id="insn-009fdeb8"></a> `009fdeb8` | `9a 01 80 52` | mov w26,#0xc | `FALL_THROUGH`
<a id="insn-009fdebc"></a> `009fdebc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009fdec0"></a> `009fdec0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-009fdec4"></a> `009fdec4` | `73 62 1a 9b` | madd x19,x19,x26,x24 | `FALL_THROUGH`
<a id="insn-009fdec8"></a> `009fdec8` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-009fdecc"></a> `009fdecc` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-009fded0"></a> `009fded0` | `31 00 00 94` | bl 0x009fdf94 | `UNCONDITIONAL_CALL`
<a id="insn-009fded4"></a> `009fded4` | `28 63 1a 9b` | madd x8,x25,x26,x24 | `FALL_THROUGH`
<a id="insn-009fded8"></a> `009fded8` | `e9 03 13 aa` | mov x9,x19 | `FALL_THROUGH`
<a id="insn-009fdedc"></a> `009fdedc` | `08 00 00 14` | b 0x009fdefc | `UNCONDITIONAL_JUMP`
<a id="insn-009fdee0"></a> `009fdee0` | `0a 0b 40 b9` | ldr w10,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-009fdee4"></a> `009fdee4` | `0b c7 40 f8` | ldr x11,[x24], #0xc | `FALL_THROUGH`
<a id="insn-009fdee8"></a> `009fdee8` | `ea 0a 00 b9` | str w10,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-009fdeec"></a> `009fdeec` | `eb 02 00 f9` | str x11,[x23] | `FALL_THROUGH`
<a id="insn-009fdef0"></a> `009fdef0` | `1f 03 13 eb` | cmp x24,x19 | `FALL_THROUGH`
<a id="insn-009fdef4"></a> `009fdef4` | `f7 32 00 91` | add x23,x23,#0xc | `FALL_THROUGH`
<a id="insn-009fdef8"></a> `009fdef8` | `00 03 00 54` | b.eq 0x009fdf58 | `CONDITIONAL_JUMP`
<a id="insn-009fdefc"></a> `009fdefc` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-009fdf00"></a> `009fdf00` | `00 01 00 54` | b.eq 0x009fdf20 | `CONDITIONAL_JUMP`
<a id="insn-009fdf04"></a> `009fdf04` | `2a 05 40 b9` | ldr w10,[x9, #0x4] | `FALL_THROUGH`
<a id="insn-009fdf08"></a> `009fdf08` | `0b 07 40 b9` | ldr w11,[x24, #0x4] | `FALL_THROUGH`
<a id="insn-009fdf0c"></a> `009fdf0c` | `5f 01 0b 6b` | cmp w10,w11 | `FALL_THROUGH`
<a id="insn-009fdf10"></a> `009fdf10` | `8a fe ff 54` | b.ge 0x009fdee0 | `CONDITIONAL_JUMP`
<a id="insn-009fdf14"></a> `009fdf14` | `2a 09 40 b9` | ldr w10,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-009fdf18"></a> `009fdf18` | `2b c5 40 f8` | ldr x11,[x9], #0xc | `FALL_THROUGH`
<a id="insn-009fdf1c"></a> `009fdf1c` | `f3 ff ff 17` | b 0x009fdee8 | `UNCONDITIONAL_JUMP`
<a id="insn-009fdf20"></a> `009fdf20` | `1f 03 13 eb` | cmp x24,x19 | `FALL_THROUGH`
<a id="insn-009fdf24"></a> `009fdf24` | `e0 ee ff 54` | b.eq 0x009fdd00 | `CONDITIONAL_JUMP`
<a id="insn-009fdf28"></a> `009fdf28` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-009fdf2c"></a> `009fdf2c` | `09 03 08 8b` | add x9,x24,x8 | `FALL_THROUGH`
<a id="insn-009fdf30"></a> `009fdf30` | `ea 02 08 8b` | add x10,x23,x8 | `FALL_THROUGH`
<a id="insn-009fdf34"></a> `009fdf34` | `08 31 00 91` | add x8,x8,#0xc | `FALL_THROUGH`
<a id="insn-009fdf38"></a> `009fdf38` | `2b 09 40 b9` | ldr w11,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-009fdf3c"></a> `009fdf3c` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-009fdf40"></a> `009fdf40` | `0c 03 08 8b` | add x12,x24,x8 | `FALL_THROUGH`
<a id="insn-009fdf44"></a> `009fdf44` | `9f 01 13 eb` | cmp x12,x19 | `FALL_THROUGH`
<a id="insn-009fdf48"></a> `009fdf48` | `4b 09 00 b9` | str w11,[x10, #0x8] | `FALL_THROUGH`
<a id="insn-009fdf4c"></a> `009fdf4c` | `49 01 00 f9` | str x9,[x10] | `FALL_THROUGH`
<a id="insn-009fdf50"></a> `009fdf50` | `e1 fe ff 54` | b.ne 0x009fdf2c | `CONDITIONAL_JUMP`
<a id="insn-009fdf54"></a> `009fdf54` | `6b ff ff 17` | b 0x009fdd00 | `UNCONDITIONAL_JUMP`
<a id="insn-009fdf58"></a> `009fdf58` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-009fdf5c"></a> `009fdf5c` | `20 ed ff 54` | b.eq 0x009fdd00 | `CONDITIONAL_JUMP`
<a id="insn-009fdf60"></a> `009fdf60` | `ea 03 1f aa` | mov x10,xzr | `FALL_THROUGH`
<a id="insn-009fdf64"></a> `009fdf64` | `2b 01 0a 8b` | add x11,x9,x10 | `FALL_THROUGH`
<a id="insn-009fdf68"></a> `009fdf68` | `ec 02 0a 8b` | add x12,x23,x10 | `FALL_THROUGH`
<a id="insn-009fdf6c"></a> `009fdf6c` | `4a 31 00 91` | add x10,x10,#0xc | `FALL_THROUGH`
<a id="insn-009fdf70"></a> `009fdf70` | `6d 09 40 b9` | ldr w13,[x11, #0x8] | `FALL_THROUGH`
<a id="insn-009fdf74"></a> `009fdf74` | `6b 01 40 f9` | ldr x11,[x11] | `FALL_THROUGH`
<a id="insn-009fdf78"></a> `009fdf78` | `2e 01 0a 8b` | add x14,x9,x10 | `FALL_THROUGH`
<a id="insn-009fdf7c"></a> `009fdf7c` | `df 01 08 eb` | cmp x14,x8 | `FALL_THROUGH`
<a id="insn-009fdf80"></a> `009fdf80` | `8d 09 00 b9` | str w13,[x12, #0x8] | `FALL_THROUGH`
<a id="insn-009fdf84"></a> `009fdf84` | `8b 01 00 f9` | str x11,[x12] | `FALL_THROUGH`
<a id="insn-009fdf88"></a> `009fdf88` | `e1 fe ff 54` | b.ne 0x009fdf64 | `CONDITIONAL_JUMP`
<a id="insn-009fdf8c"></a> `009fdf8c` | `5d ff ff 17` | b 0x009fdd00 | `UNCONDITIONAL_JUMP`
<a id="insn-009fdf90"></a> `009fdf90` | `d4 67 09 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009fdccc`](#insn-009fdccc) 範囲 `[['009fdccc', '009fdcff']]`
  - `CONDITIONAL_JUMP` [`009fdcfc`](#insn-009fdcfc) → [`009fdd30`](#insn-009fdd30)
  - `FALL_THROUGH` [`009fdcfc`](#insn-009fdcfc) → [`009fdd00`](#insn-009fdd00)
- ブロック [`009fdd00`](#insn-009fdd00) 範囲 `[['009fdd00', '009fdd0f']]`
  - `CONDITIONAL_JUMP` [`009fdd0c`](#insn-009fdd0c) → [`009fdf90`](#insn-009fdf90)
  - `FALL_THROUGH` [`009fdd0c`](#insn-009fdd0c) → [`009fdd10`](#insn-009fdd10)
- ブロック [`009fdd10`](#insn-009fdd10) 範囲 `[['009fdd10', '009fdd2f']]`
- ブロック [`009fdd30`](#insn-009fdd30) 範囲 `[['009fdd30', '009fdd33']]`
  - `CONDITIONAL_JUMP` [`009fdd30`](#insn-009fdd30) → [`009fdd6c`](#insn-009fdd6c)
  - `FALL_THROUGH` [`009fdd30`](#insn-009fdd30) → [`009fdd34`](#insn-009fdd34)
- ブロック [`009fdd34`](#insn-009fdd34) 範囲 `[['009fdd34', '009fdd43']]`
  - `CONDITIONAL_JUMP` [`009fdd40`](#insn-009fdd40) → [`009fdd00`](#insn-009fdd00)
  - `FALL_THROUGH` [`009fdd40`](#insn-009fdd40) → [`009fdd44`](#insn-009fdd44)
- ブロック [`009fdd44`](#insn-009fdd44) 範囲 `[['009fdd44', '009fdd6b']]`
  - `UNCONDITIONAL_JUMP` [`009fdd68`](#insn-009fdd68) → [`009fdd00`](#insn-009fdd00)
- ブロック [`009fdd6c`](#insn-009fdd6c) 範囲 `[['009fdd6c', '009fdd73']]`
  - `CONDITIONAL_JUMP` [`009fdd70`](#insn-009fdd70) → [`009fde08`](#insn-009fde08)
  - `FALL_THROUGH` [`009fdd70`](#insn-009fdd70) → [`009fdd74`](#insn-009fdd74)
- ブロック [`009fdd74`](#insn-009fdd74) 範囲 `[['009fdd74', '009fdd7b']]`
  - `CONDITIONAL_JUMP` [`009fdd78`](#insn-009fdd78) → [`009fdd00`](#insn-009fdd00)
  - `FALL_THROUGH` [`009fdd78`](#insn-009fdd78) → [`009fdd7c`](#insn-009fdd7c)
- ブロック [`009fdd7c`](#insn-009fdd7c) 範囲 `[['009fdd7c', '009fdd87']]`
  - `CONDITIONAL_JUMP` [`009fdd84`](#insn-009fdd84) → [`009fdd00`](#insn-009fdd00)
  - `FALL_THROUGH` [`009fdd84`](#insn-009fdd84) → [`009fdd88`](#insn-009fdd88)
- ブロック [`009fdd88`](#insn-009fdd88) 範囲 `[['009fdd88', '009fdd93']]`
  - `UNCONDITIONAL_JUMP` [`009fdd90`](#insn-009fdd90) → [`009fddb4`](#insn-009fddb4)
- ブロック [`009fdd94`](#insn-009fdd94) 範囲 `[['009fdd94', '009fdd97']]`
  - `FALL_THROUGH` [`009fdd94`](#insn-009fdd94) → [`009fdd98`](#insn-009fdd98)
- ブロック [`009fdd98`](#insn-009fdd98) 範囲 `[['009fdd98', '009fdd9f']]`
  - `FALL_THROUGH` [`009fdd9c`](#insn-009fdd9c) → [`009fdda0`](#insn-009fdda0)
- ブロック [`009fdda0`](#insn-009fdda0) 範囲 `[['009fdda0', '009fddb3']]`
  - `CONDITIONAL_JUMP` [`009fddb0`](#insn-009fddb0) → [`009fdd00`](#insn-009fdd00)
  - `FALL_THROUGH` [`009fddb0`](#insn-009fddb0) → [`009fddb4`](#insn-009fddb4)
- ブロック [`009fddb4`](#insn-009fddb4) 範囲 `[['009fddb4', '009fddcb']]`
  - `CONDITIONAL_JUMP` [`009fddc8`](#insn-009fddc8) → [`009fdda0`](#insn-009fdda0)
  - `FALL_THROUGH` [`009fddc8`](#insn-009fddc8) → [`009fddcc`](#insn-009fddcc)
- ブロック [`009fddcc`](#insn-009fddcc) 範囲 `[['009fddcc', '009fddd3']]`
  - `FALL_THROUGH` [`009fddd0`](#insn-009fddd0) → [`009fddd4`](#insn-009fddd4)
- ブロック [`009fddd4`](#insn-009fddd4) 範囲 `[['009fddd4', '009fddeb']]`
  - `CONDITIONAL_JUMP` [`009fdde8`](#insn-009fdde8) → [`009fdd94`](#insn-009fdd94)
  - `FALL_THROUGH` [`009fdde8`](#insn-009fdde8) → [`009fddec`](#insn-009fddec)
- ブロック [`009fddec`](#insn-009fddec) 範囲 `[['009fddec', '009fddfb']]`
  - `CONDITIONAL_JUMP` [`009fddf8`](#insn-009fddf8) → [`009fddd4`](#insn-009fddd4)
  - `FALL_THROUGH` [`009fddf8`](#insn-009fddf8) → [`009fddfc`](#insn-009fddfc)
- ブロック [`009fddfc`](#insn-009fddfc) 範囲 `[['009fddfc', '009fde07']]`
  - `UNCONDITIONAL_JUMP` [`009fde04`](#insn-009fde04) → [`009fdd98`](#insn-009fdd98)
- ブロック [`009fde08`](#insn-009fde08) 範囲 `[['009fde08', '009fde2b']]`
  - `CONDITIONAL_JUMP` [`009fde28`](#insn-009fde28) → [`009fdea8`](#insn-009fdea8)
  - `FALL_THROUGH` [`009fde28`](#insn-009fde28) → [`009fde2c`](#insn-009fde2c)
- ブロック [`009fde2c`](#insn-009fde2c) 範囲 `[['009fde2c', '009fde6b']]`
  - `CONDITIONAL_JUMP` [`009fde68`](#insn-009fde68) → [`009fdf90`](#insn-009fdf90)
  - `FALL_THROUGH` [`009fde68`](#insn-009fde68) → [`009fde6c`](#insn-009fde6c)
- ブロック [`009fde6c`](#insn-009fde6c) 範囲 `[['009fde6c', '009fdea7']]`
- ブロック [`009fdea8`](#insn-009fdea8) 範囲 `[['009fdea8', '009fdeab']]`
  - `FALL_THROUGH` [`009fdea8`](#insn-009fdea8) → [`009fdeac`](#insn-009fdeac)
- ブロック [`009fdeac`](#insn-009fdeac) 範囲 `[['009fdeac', '009fded3']]`
  - `FALL_THROUGH` [`009fded0`](#insn-009fded0) → [`009fded4`](#insn-009fded4)
- ブロック [`009fded4`](#insn-009fded4) 範囲 `[['009fded4', '009fdedf']]`
  - `UNCONDITIONAL_JUMP` [`009fdedc`](#insn-009fdedc) → [`009fdefc`](#insn-009fdefc)
- ブロック [`009fdee0`](#insn-009fdee0) 範囲 `[['009fdee0', '009fdee7']]`
  - `FALL_THROUGH` [`009fdee4`](#insn-009fdee4) → [`009fdee8`](#insn-009fdee8)
- ブロック [`009fdee8`](#insn-009fdee8) 範囲 `[['009fdee8', '009fdeef']]`
  - `FALL_THROUGH` [`009fdeec`](#insn-009fdeec) → [`009fdef0`](#insn-009fdef0)
- ブロック [`009fdef0`](#insn-009fdef0) 範囲 `[['009fdef0', '009fdefb']]`
  - `CONDITIONAL_JUMP` [`009fdef8`](#insn-009fdef8) → [`009fdf58`](#insn-009fdf58)
  - `FALL_THROUGH` [`009fdef8`](#insn-009fdef8) → [`009fdefc`](#insn-009fdefc)
- ブロック [`009fdefc`](#insn-009fdefc) 範囲 `[['009fdefc', '009fdeff']]`
  - `FALL_THROUGH` [`009fdefc`](#insn-009fdefc) → [`009fdf00`](#insn-009fdf00)
- ブロック [`009fdf00`](#insn-009fdf00) 範囲 `[['009fdf00', '009fdf03']]`
  - `CONDITIONAL_JUMP` [`009fdf00`](#insn-009fdf00) → [`009fdf20`](#insn-009fdf20)
  - `FALL_THROUGH` [`009fdf00`](#insn-009fdf00) → [`009fdf04`](#insn-009fdf04)
- ブロック [`009fdf04`](#insn-009fdf04) 範囲 `[['009fdf04', '009fdf07']]`
  - `FALL_THROUGH` [`009fdf04`](#insn-009fdf04) → [`009fdf08`](#insn-009fdf08)
- ブロック [`009fdf08`](#insn-009fdf08) 範囲 `[['009fdf08', '009fdf13']]`
  - `CONDITIONAL_JUMP` [`009fdf10`](#insn-009fdf10) → [`009fdee0`](#insn-009fdee0)
  - `FALL_THROUGH` [`009fdf10`](#insn-009fdf10) → [`009fdf14`](#insn-009fdf14)
- ブロック [`009fdf14`](#insn-009fdf14) 範囲 `[['009fdf14', '009fdf1f']]`
  - `UNCONDITIONAL_JUMP` [`009fdf1c`](#insn-009fdf1c) → [`009fdee8`](#insn-009fdee8)
- ブロック [`009fdf20`](#insn-009fdf20) 範囲 `[['009fdf20', '009fdf27']]`
  - `CONDITIONAL_JUMP` [`009fdf24`](#insn-009fdf24) → [`009fdd00`](#insn-009fdd00)
  - `FALL_THROUGH` [`009fdf24`](#insn-009fdf24) → [`009fdf28`](#insn-009fdf28)
- ブロック [`009fdf28`](#insn-009fdf28) 範囲 `[['009fdf28', '009fdf2b']]`
  - `FALL_THROUGH` [`009fdf28`](#insn-009fdf28) → [`009fdf2c`](#insn-009fdf2c)
- ブロック [`009fdf2c`](#insn-009fdf2c) 範囲 `[['009fdf2c', '009fdf53']]`
  - `CONDITIONAL_JUMP` [`009fdf50`](#insn-009fdf50) → [`009fdf2c`](#insn-009fdf2c)
  - `FALL_THROUGH` [`009fdf50`](#insn-009fdf50) → [`009fdf54`](#insn-009fdf54)
- ブロック [`009fdf54`](#insn-009fdf54) 範囲 `[['009fdf54', '009fdf57']]`
  - `UNCONDITIONAL_JUMP` [`009fdf54`](#insn-009fdf54) → [`009fdd00`](#insn-009fdd00)
- ブロック [`009fdf58`](#insn-009fdf58) 範囲 `[['009fdf58', '009fdf5f']]`
  - `CONDITIONAL_JUMP` [`009fdf5c`](#insn-009fdf5c) → [`009fdd00`](#insn-009fdd00)
  - `FALL_THROUGH` [`009fdf5c`](#insn-009fdf5c) → [`009fdf60`](#insn-009fdf60)
- ブロック [`009fdf60`](#insn-009fdf60) 範囲 `[['009fdf60', '009fdf63']]`
  - `FALL_THROUGH` [`009fdf60`](#insn-009fdf60) → [`009fdf64`](#insn-009fdf64)
- ブロック [`009fdf64`](#insn-009fdf64) 範囲 `[['009fdf64', '009fdf8b']]`
  - `CONDITIONAL_JUMP` [`009fdf88`](#insn-009fdf88) → [`009fdf64`](#insn-009fdf64)
  - `FALL_THROUGH` [`009fdf88`](#insn-009fdf88) → [`009fdf8c`](#insn-009fdf8c)
- ブロック [`009fdf8c`](#insn-009fdf8c) 範囲 `[['009fdf8c', '009fdf8f']]`
  - `UNCONDITIONAL_JUMP` [`009fdf8c`](#insn-009fdf8c) → [`009fdd00`](#insn-009fdd00)
- ブロック [`009fdf90`](#insn-009fdf90) 範囲 `[['009fdf90', '009fdf93']]`

## 命令位置別の参照

- [`009fdcd0`](#insn-009fdcd0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdcd4`](#insn-009fdcd4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdcd8`](#insn-009fdcd8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdcdc`](#insn-009fdcdc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdce0`](#insn-009fdce0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdce4`](#insn-009fdce4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdcf8`](#insn-009fdcf8) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdcfc`](#insn-009fdcfc) → [`009fdd30`](#insn-009fdd30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdd04`](#insn-009fdd04) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdd0c`](#insn-009fdd0c) → [`009fdf90`](#insn-009fdf90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdd10`](#insn-009fdd10) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdd14`](#insn-009fdd14) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdd18`](#insn-009fdd18) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdd1c`](#insn-009fdd1c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdd20`](#insn-009fdd20) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdd24`](#insn-009fdd24) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdd30`](#insn-009fdd30) → [`009fdd6c`](#insn-009fdd6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdd40`](#insn-009fdd40) → [`009fdd00`](#insn-009fdd00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdd68`](#insn-009fdd68) → [`009fdd00`](#insn-009fdd00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdd70`](#insn-009fdd70) → [`009fde08`](#insn-009fde08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdd78`](#insn-009fdd78) → [`009fdd00`](#insn-009fdd00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdd84`](#insn-009fdd84) → [`009fdd00`](#insn-009fdd00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdd90`](#insn-009fdd90) → [`009fddb4`](#insn-009fddb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fddb0`](#insn-009fddb0) → [`009fdd00`](#insn-009fdd00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fddc8`](#insn-009fddc8) → [`009fdda0`](#insn-009fdda0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdde8`](#insn-009fdde8) → [`009fdd94`](#insn-009fdd94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fddf8`](#insn-009fddf8) → [`009fddd4`](#insn-009fddd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fde04`](#insn-009fde04) → [`009fdd98`](#insn-009fdd98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fde28`](#insn-009fde28) → [`009fdea8`](#insn-009fdea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fde38`](#insn-009fde38) → [`009fdccc`](#insn-009fdccc) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009fdccc` · 推定シンボル `None` · 推定型 `None`
- [`009fde58`](#insn-009fde58) → [`009fdccc`](#insn-009fdccc) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009fdccc` · 推定シンボル `None` · 推定型 `None`
- [`009fde60`](#insn-009fde60) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fde68`](#insn-009fde68) → [`009fdf90`](#insn-009fdf90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fde88`](#insn-009fde88) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fde8c`](#insn-009fde8c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fde90`](#insn-009fde90) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fde94`](#insn-009fde94) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fde98`](#insn-009fde98) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fde9c`](#insn-009fde9c) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdea4`](#insn-009fdea4) → [`009fe20c`](../009fe/009fe20c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009fe20c` · 推定シンボル `None` · 推定型 `None`
- [`009fdeb4`](#insn-009fdeb4) → [`009fdf94`](009fdf94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009fdf94` · 推定シンボル `None` · 推定型 `None`
- [`009fded0`](#insn-009fded0) → [`009fdf94`](009fdf94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009fdf94` · 推定シンボル `None` · 推定型 `None`
- [`009fdedc`](#insn-009fdedc) → [`009fdefc`](#insn-009fdefc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdef8`](#insn-009fdef8) → [`009fdf58`](#insn-009fdf58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdf00`](#insn-009fdf00) → [`009fdf20`](#insn-009fdf20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdf10`](#insn-009fdf10) → [`009fdee0`](#insn-009fdee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdf1c`](#insn-009fdf1c) → [`009fdee8`](#insn-009fdee8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdf24`](#insn-009fdf24) → [`009fdd00`](#insn-009fdd00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdf50`](#insn-009fdf50) → [`009fdf2c`](#insn-009fdf2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdf54`](#insn-009fdf54) → [`009fdd00`](#insn-009fdd00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdf5c`](#insn-009fdf5c) → [`009fdd00`](#insn-009fdd00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdf88`](#insn-009fdf88) → [`009fdf64`](#insn-009fdf64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdf8c`](#insn-009fdf8c) → [`009fdd00`](#insn-009fdd00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fdf90`](#insn-009fdf90) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009fdcd0`](#insn-009fdcd0)

~~~json
{
  "source": "009fdcd0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdcd4`](#insn-009fdcd4)

~~~json
{
  "source": "009fdcd4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdcd8`](#insn-009fdcd8)

~~~json
{
  "source": "009fdcd8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdcdc`](#insn-009fdcdc)

~~~json
{
  "source": "009fdcdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdce0`](#insn-009fdce0)

~~~json
{
  "source": "009fdce0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdce4`](#insn-009fdce4)

~~~json
{
  "source": "009fdce4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdcf8`](#insn-009fdcf8)

~~~json
{
  "source": "009fdcf8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdcfc`](#insn-009fdcfc)

~~~json
{
  "source": "009fdcfc",
  "target": "009fdd30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdd04`](#insn-009fdd04)

~~~json
{
  "source": "009fdd04",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdd0c`](#insn-009fdd0c)

~~~json
{
  "source": "009fdd0c",
  "target": "009fdf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdd10`](#insn-009fdd10)

~~~json
{
  "source": "009fdd10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdd14`](#insn-009fdd14)

~~~json
{
  "source": "009fdd14",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdd18`](#insn-009fdd18)

~~~json
{
  "source": "009fdd18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdd1c`](#insn-009fdd1c)

~~~json
{
  "source": "009fdd1c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdd20`](#insn-009fdd20)

~~~json
{
  "source": "009fdd20",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdd24`](#insn-009fdd24)

~~~json
{
  "source": "009fdd24",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdd30`](#insn-009fdd30)

~~~json
{
  "source": "009fdd30",
  "target": "009fdd6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdd40`](#insn-009fdd40)

~~~json
{
  "source": "009fdd40",
  "target": "009fdd00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdd68`](#insn-009fdd68)

~~~json
{
  "source": "009fdd68",
  "target": "009fdd00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdd70`](#insn-009fdd70)

~~~json
{
  "source": "009fdd70",
  "target": "009fde08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdd78`](#insn-009fdd78)

~~~json
{
  "source": "009fdd78",
  "target": "009fdd00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdd84`](#insn-009fdd84)

~~~json
{
  "source": "009fdd84",
  "target": "009fdd00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdd90`](#insn-009fdd90)

~~~json
{
  "source": "009fdd90",
  "target": "009fddb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fddb0`](#insn-009fddb0)

~~~json
{
  "source": "009fddb0",
  "target": "009fdd00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fddc8`](#insn-009fddc8)

~~~json
{
  "source": "009fddc8",
  "target": "009fdda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdde8`](#insn-009fdde8)

~~~json
{
  "source": "009fdde8",
  "target": "009fdd94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fddf8`](#insn-009fddf8)

~~~json
{
  "source": "009fddf8",
  "target": "009fddd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fde04`](#insn-009fde04)

~~~json
{
  "source": "009fde04",
  "target": "009fdd98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fde28`](#insn-009fde28)

~~~json
{
  "source": "009fde28",
  "target": "009fdea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fde38`](#insn-009fde38)

~~~json
{
  "source": "009fde38",
  "target": "009fdccc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fde58`](#insn-009fde58)

~~~json
{
  "source": "009fde58",
  "target": "009fdccc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fde60`](#insn-009fde60)

~~~json
{
  "source": "009fde60",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fde68`](#insn-009fde68)

~~~json
{
  "source": "009fde68",
  "target": "009fdf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fde88`](#insn-009fde88)

~~~json
{
  "source": "009fde88",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fde8c`](#insn-009fde8c)

~~~json
{
  "source": "009fde8c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fde90`](#insn-009fde90)

~~~json
{
  "source": "009fde90",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fde94`](#insn-009fde94)

~~~json
{
  "source": "009fde94",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fde98`](#insn-009fde98)

~~~json
{
  "source": "009fde98",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fde9c`](#insn-009fde9c)

~~~json
{
  "source": "009fde9c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdea4`](#insn-009fdea4)

~~~json
{
  "source": "009fdea4",
  "target": "009fe20c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fdeb4`](#insn-009fdeb4)

~~~json
{
  "source": "009fdeb4",
  "target": "009fdf94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fded0`](#insn-009fded0)

~~~json
{
  "source": "009fded0",
  "target": "009fdf94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fdedc`](#insn-009fdedc)

~~~json
{
  "source": "009fdedc",
  "target": "009fdefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdef8`](#insn-009fdef8)

~~~json
{
  "source": "009fdef8",
  "target": "009fdf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdf00`](#insn-009fdf00)

~~~json
{
  "source": "009fdf00",
  "target": "009fdf20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdf10`](#insn-009fdf10)

~~~json
{
  "source": "009fdf10",
  "target": "009fdee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdf1c`](#insn-009fdf1c)

~~~json
{
  "source": "009fdf1c",
  "target": "009fdee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdf24`](#insn-009fdf24)

~~~json
{
  "source": "009fdf24",
  "target": "009fdd00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdf50`](#insn-009fdf50)

~~~json
{
  "source": "009fdf50",
  "target": "009fdf2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdf54`](#insn-009fdf54)

~~~json
{
  "source": "009fdf54",
  "target": "009fdd00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdf5c`](#insn-009fdf5c)

~~~json
{
  "source": "009fdf5c",
  "target": "009fdd00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdf88`](#insn-009fdf88)

~~~json
{
  "source": "009fdf88",
  "target": "009fdf64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdf8c`](#insn-009fdf8c)

~~~json
{
  "source": "009fdf8c",
  "target": "009fdd00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fdf90`](#insn-009fdf90)

~~~json
{
  "source": "009fdf90",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
