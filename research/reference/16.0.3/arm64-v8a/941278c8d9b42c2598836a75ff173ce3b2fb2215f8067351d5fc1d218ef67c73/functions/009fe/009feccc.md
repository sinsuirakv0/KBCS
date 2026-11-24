# 009feccc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `009fdd20`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdd20.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0026.md#compare-d01fbd67f7810bb6a8d33f39bce13c51)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009feccc",
  "name": "FUN_009feccc",
  "size": 712,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fb85f1f69c1049193c6b18dd746e1b9619d292da814e748a89e05baaad10376d",
  "source_text_sha256": "fb85f1f69c1049193c6b18dd746e1b9619d292da814e748a89e05baaad10376d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009feccc",
        "009fef93"
      ]
    ],
    "bytes_sha256": "21a3b463de438455381b34d4a4df974e8a3c5b43af94ba7c65cfe4d6e2bb6d19",
    "instruction_count": 178,
    "instruction_bytes": 712,
    "body_bytes": 712,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [009fa2c8](../009fa/009fa2c8.md)
- [009feccc](../009fe/009feccc.md)
- [009fef94](../009fe/009fef94.md)

## 呼び出し先

- [009feccc](../009fe/009feccc.md)
- [009fef94](../009fe/009fef94.md)
- [009ff20c](../009ff/009ff20c.md)
- [00c58f80](../00c58/00c58f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5052 bytes

~~~c

void FUN_009feccc(undefined8 *param_1,undefined8 *param_2,ulong param_3,undefined8 *param_4,
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
              if (lVar10 == 0) goto LAB_009fed98;
              lVar13 = lVar10 + -0xc;
            } while (iVar9 < *(int *)(puVar6 + -1));
            puVar5 = (undefined8 *)((long)param_1 + lVar10);
LAB_009fed98:
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
        FUN_009feccc(param_1,lVar4,uVar11);
        FUN_009feccc(lVar4,param_2,lVar13,param_4,param_5);
        if (*(long *)(lVar2 + 0x28) == lVar3) {
          FUN_009ff20c(param_1,lVar4,param_2,uVar11,lVar13,param_4,param_5);
          return;
        }
        goto LAB_009fef90;
      }
                    /* try { // try from 009feeac to 00afeebb has its CatchHandler @ 009ff4e4 */
      FUN_009fef94(param_1,lVar4,uVar11);
      puVar12 = (undefined8 *)((long)param_4 + uVar11 * 0xc);
      FUN_009fef94(lVar4,param_2,lVar13,puVar12);
                    /* try { // try from 009feed4 to 00afeedf has its CatchHandler @ 009ff3e0 */
      puVar5 = (undefined8 *)((long)param_4 + param_3 * 0xc);
      puVar6 = puVar12;
      do {
                    /* try { // try from 009fef00 to 00afef07 has its CatchHandler @ 009ff3bc */
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
          goto LAB_009fed00;
        }
                    /* try { // try from 009fef08 to 00afefab has its CatchHandler @ 009fe500 */
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
                    /* try { // try from 009feef0 to 00afeefb has its CatchHandler @ 009ff3cc */
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
LAB_009fed00:
  if (*(long *)(lVar2 + 0x28) == lVar3) {
    return;
  }
LAB_009fef90:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009feccc"></a> `009feccc` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-009fecd0"></a> `009fecd0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009fecd4"></a> `009fecd4` | `fb 1b 00 f9` | str x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009fecd8"></a> `009fecd8` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009fecdc"></a> `009fecdc` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009fece0"></a> `009fece0` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009fece4"></a> `009fece4` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-009fece8"></a> `009fece8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-009fecec"></a> `009fecec` | `5b d0 3b d5` | mrs x27,tpidr_el0 | `FALL_THROUGH`
<a id="insn-009fecf0"></a> `009fecf0` | `68 17 40 f9` | ldr x8,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-009fecf4"></a> `009fecf4` | `5f 08 00 f1` | cmp x2,#0x2 | `FALL_THROUGH`
<a id="insn-009fecf8"></a> `009fecf8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009fecfc"></a> `009fecfc` | `a2 01 00 54` | b.cs 0x009fed30 | `CONDITIONAL_JUMP`
<a id="insn-009fed00"></a> `009fed00` | `68 17 40 f9` | ldr x8,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-009fed04"></a> `009fed04` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009fed08"></a> `009fed08` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009fed0c"></a> `009fed0c` | `21 14 00 54` | b.ne 0x009fef90 | `CONDITIONAL_JUMP`
<a id="insn-009fed10"></a> `009fed10` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-009fed14"></a> `009fed14` | `fb 1b 40 f9` | ldr x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009fed18"></a> `009fed18` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009fed1c"></a> `009fed1c` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009fed20"></a> `009fed20` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009fed24"></a> `009fed24` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009fed28"></a> `009fed28` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-009fed2c"></a> `009fed2c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-009fed30"></a> `009fed30` | `e1 01 00 54` | b.ne 0x009fed6c | `CONDITIONAL_JUMP`
<a id="insn-009fed34"></a> `009fed34` | `28 80 5f b8` | ldur w8,[x1, #-0x8] | `FALL_THROUGH`
<a id="insn-009fed38"></a> `009fed38` | `09 04 40 b9` | ldr w9,[x0, #0x4] | `FALL_THROUGH`
<a id="insn-009fed3c"></a> `009fed3c` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-009fed40"></a> `009fed40` | `0a fe ff 54` | b.ge 0x009fed00 | `CONDITIONAL_JUMP`
<a id="insn-009fed44"></a> `009fed44` | `28 30 00 d1` | sub x8,x1,#0xc | `FALL_THROUGH`
<a id="insn-009fed48"></a> `009fed48` | `0b 00 40 f9` | ldr x11,[x0] | `FALL_THROUGH`
<a id="insn-009fed4c"></a> `009fed4c` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-009fed50"></a> `009fed50` | `0a 09 40 b9` | ldr w10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-009fed54"></a> `009fed54` | `09 00 00 f9` | str x9,[x0] | `FALL_THROUGH`
<a id="insn-009fed58"></a> `009fed58` | `09 08 40 b9` | ldr w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-009fed5c"></a> `009fed5c` | `0a 08 00 b9` | str w10,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-009fed60"></a> `009fed60` | `0b 01 00 f9` | str x11,[x8] | `FALL_THROUGH`
<a id="insn-009fed64"></a> `009fed64` | `09 09 00 b9` | str w9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-009fed68"></a> `009fed68` | `e6 ff ff 17` | b 0x009fed00 | `UNCONDITIONAL_JUMP`
<a id="insn-009fed6c"></a> `009fed6c` | `5f 00 02 f1` | cmp x2,#0x80 | `FALL_THROUGH`
<a id="insn-009fed70"></a> `009fed70` | `cc 04 00 54` | b.gt 0x009fee08 | `CONDITIONAL_JUMP`
<a id="insn-009fed74"></a> `009fed74` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-009fed78"></a> `009fed78` | `40 fc ff 54` | b.eq 0x009fed00 | `CONDITIONAL_JUMP`
<a id="insn-009fed7c"></a> `009fed7c` | `0a 30 00 91` | add x10,x0,#0xc | `FALL_THROUGH`
<a id="insn-009fed80"></a> `009fed80` | `5f 01 01 eb` | cmp x10,x1 | `FALL_THROUGH`
<a id="insn-009fed84"></a> `009fed84` | `e0 fb ff 54` | b.eq 0x009fed00 | `CONDITIONAL_JUMP`
<a id="insn-009fed88"></a> `009fed88` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-009fed8c"></a> `009fed8c` | `eb 03 00 aa` | mov x11,x0 | `FALL_THROUGH`
<a id="insn-009fed90"></a> `009fed90` | `09 00 00 14` | b 0x009fedb4 | `UNCONDITIONAL_JUMP`
<a id="insn-009fed94"></a> `009fed94` | `ec 03 00 aa` | mov x12,x0 | `FALL_THROUGH`
<a id="insn-009fed98"></a> `009fed98` | `8a 01 00 f9` | str x10,[x12] | `FALL_THROUGH`
<a id="insn-009fed9c"></a> `009fed9c` | `8b 09 00 b9` | str w11,[x12, #0x8] | `FALL_THROUGH`
<a id="insn-009feda0"></a> `009feda0` | `2a 31 00 91` | add x10,x9,#0xc | `FALL_THROUGH`
<a id="insn-009feda4"></a> `009feda4` | `08 31 00 91` | add x8,x8,#0xc | `FALL_THROUGH`
<a id="insn-009feda8"></a> `009feda8` | `eb 03 09 aa` | mov x11,x9 | `FALL_THROUGH`
<a id="insn-009fedac"></a> `009fedac` | `5f 01 01 eb` | cmp x10,x1 | `FALL_THROUGH`
<a id="insn-009fedb0"></a> `009fedb0` | `80 fa ff 54` | b.eq 0x009fed00 | `CONDITIONAL_JUMP`
<a id="insn-009fedb4"></a> `009fedb4` | `e9 03 0a aa` | mov x9,x10 | `FALL_THROUGH`
<a id="insn-009fedb8"></a> `009fedb8` | `4a 01 40 f9` | ldr x10,[x10] | `FALL_THROUGH`
<a id="insn-009fedbc"></a> `009fedbc` | `6d 05 40 b9` | ldr w13,[x11, #0x4] | `FALL_THROUGH`
<a id="insn-009fedc0"></a> `009fedc0` | `4c fd 60 d3` | lsr x12,x10,#0x20 | `FALL_THROUGH`
<a id="insn-009fedc4"></a> `009fedc4` | `9f 01 0d 6b` | cmp w12,w13 | `FALL_THROUGH`
<a id="insn-009fedc8"></a> `009fedc8` | `ca fe ff 54` | b.ge 0x009feda0 | `CONDITIONAL_JUMP`
<a id="insn-009fedcc"></a> `009fedcc` | `6b 15 40 b9` | ldr w11,[x11, #0x14] | `FALL_THROUGH`
<a id="insn-009fedd0"></a> `009fedd0` | `ed 03 08 aa` | mov x13,x8 | `FALL_THROUGH`
<a id="insn-009fedd4"></a> `009fedd4` | `0e 00 0d 8b` | add x14,x0,x13 | `FALL_THROUGH`
<a id="insn-009fedd8"></a> `009fedd8` | `cf 01 40 f9` | ldr x15,[x14] | `FALL_THROUGH`
<a id="insn-009feddc"></a> `009feddc` | `d0 09 40 b9` | ldr w16,[x14, #0x8] | `FALL_THROUGH`
<a id="insn-009fede0"></a> `009fede0` | `cf c1 00 f8` | stur x15,[x14, #0xc] | `FALL_THROUGH`
<a id="insn-009fede4"></a> `009fede4` | `d0 15 00 b9` | str w16,[x14, #0x14] | `FALL_THROUGH`
<a id="insn-009fede8"></a> `009fede8` | `6d fd ff b4` | cbz x13,0x009fed94 | `CONDITIONAL_JUMP`
<a id="insn-009fedec"></a> `009fedec` | `ce 81 5f b8` | ldur w14,[x14, #-0x8] | `FALL_THROUGH`
<a id="insn-009fedf0"></a> `009fedf0` | `ad 31 00 d1` | sub x13,x13,#0xc | `FALL_THROUGH`
<a id="insn-009fedf4"></a> `009fedf4` | `9f 01 0e 6b` | cmp w12,w14 | `FALL_THROUGH`
<a id="insn-009fedf8"></a> `009fedf8` | `eb fe ff 54` | b.lt 0x009fedd4 | `CONDITIONAL_JUMP`
<a id="insn-009fedfc"></a> `009fedfc` | `0c 00 0d 8b` | add x12,x0,x13 | `FALL_THROUGH`
<a id="insn-009fee00"></a> `009fee00` | `8c 31 00 91` | add x12,x12,#0xc | `FALL_THROUGH`
<a id="insn-009fee04"></a> `009fee04` | `e5 ff ff 17` | b 0x009fed98 | `UNCONDITIONAL_JUMP`
<a id="insn-009fee08"></a> `009fee08` | `53 fc 41 d3` | lsr x19,x2,#0x1 | `FALL_THROUGH`
<a id="insn-009fee0c"></a> `009fee0c` | `88 01 80 52` | mov w8,#0xc | `FALL_THROUGH`
<a id="insn-009fee10"></a> `009fee10` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-009fee14"></a> `009fee14` | `5f 00 04 eb` | cmp x2,x4 | `FALL_THROUGH`
<a id="insn-009fee18"></a> `009fee18` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-009fee1c"></a> `009fee1c` | `75 02 08 9b` | madd x21,x19,x8,x0 | `FALL_THROUGH`
<a id="insn-009fee20"></a> `009fee20` | `56 00 13 cb` | sub x22,x2,x19 | `FALL_THROUGH`
<a id="insn-009fee24"></a> `009fee24` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-009fee28"></a> `009fee28` | `0d 04 00 54` | b.le 0x009feea8 | `CONDITIONAL_JUMP`
<a id="insn-009fee2c"></a> `009fee2c` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-009fee30"></a> `009fee30` | `f9 03 03 aa` | mov x25,x3 | `FALL_THROUGH`
<a id="insn-009fee34"></a> `009fee34` | `fa 03 04 aa` | mov x26,x4 | `FALL_THROUGH`
<a id="insn-009fee38"></a> `009fee38` | `a5 ff ff 97` | bl 0x009feccc | `UNCONDITIONAL_CALL`
<a id="insn-009fee3c"></a> `009fee3c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009fee40"></a> `009fee40` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-009fee44"></a> `009fee44` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-009fee48"></a> `009fee48` | `e3 03 19 aa` | mov x3,x25 | `FALL_THROUGH`
<a id="insn-009fee4c"></a> `009fee4c` | `e4 03 1a aa` | mov x4,x26 | `FALL_THROUGH`
<a id="insn-009fee50"></a> `009fee50` | `f8 03 19 aa` | mov x24,x25 | `FALL_THROUGH`
<a id="insn-009fee54"></a> `009fee54` | `f9 03 1a aa` | mov x25,x26 | `FALL_THROUGH`
<a id="insn-009fee58"></a> `009fee58` | `9d ff ff 97` | bl 0x009feccc | `UNCONDITIONAL_CALL`
<a id="insn-009fee5c"></a> `009fee5c` | `68 17 40 f9` | ldr x8,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-009fee60"></a> `009fee60` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009fee64"></a> `009fee64` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009fee68"></a> `009fee68` | `41 09 00 54` | b.ne 0x009fef90 | `CONDITIONAL_JUMP`
<a id="insn-009fee6c"></a> `009fee6c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-009fee70"></a> `009fee70` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-009fee74"></a> `009fee74` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-009fee78"></a> `009fee78` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-009fee7c"></a> `009fee7c` | `e4 03 16 aa` | mov x4,x22 | `FALL_THROUGH`
<a id="insn-009fee80"></a> `009fee80` | `e5 03 18 aa` | mov x5,x24 | `FALL_THROUGH`
<a id="insn-009fee84"></a> `009fee84` | `e6 03 19 aa` | mov x6,x25 | `FALL_THROUGH`
<a id="insn-009fee88"></a> `009fee88` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-009fee8c"></a> `009fee8c` | `fb 1b 40 f9` | ldr x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009fee90"></a> `009fee90` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009fee94"></a> `009fee94` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009fee98"></a> `009fee98` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009fee9c"></a> `009fee9c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009feea0"></a> `009feea0` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-009feea4"></a> `009feea4` | `da 00 00 14` | b 0x009ff20c | `CALL_TERMINATOR`
<a id="insn-009feea8"></a> `009feea8` | `f9 03 02 aa` | mov x25,x2 | `FALL_THROUGH`
<a id="insn-009feeac"></a> `009feeac` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-009feeb0"></a> `009feeb0` | `f8 03 03 aa` | mov x24,x3 | `FALL_THROUGH`
<a id="insn-009feeb4"></a> `009feeb4` | `38 00 00 94` | bl 0x009fef94 | `UNCONDITIONAL_CALL`
<a id="insn-009feeb8"></a> `009feeb8` | `9a 01 80 52` | mov w26,#0xc | `FALL_THROUGH`
<a id="insn-009feebc"></a> `009feebc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009feec0"></a> `009feec0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-009feec4"></a> `009feec4` | `73 62 1a 9b` | madd x19,x19,x26,x24 | `FALL_THROUGH`
<a id="insn-009feec8"></a> `009feec8` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-009feecc"></a> `009feecc` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-009feed0"></a> `009feed0` | `31 00 00 94` | bl 0x009fef94 | `UNCONDITIONAL_CALL`
<a id="insn-009feed4"></a> `009feed4` | `28 63 1a 9b` | madd x8,x25,x26,x24 | `FALL_THROUGH`
<a id="insn-009feed8"></a> `009feed8` | `e9 03 13 aa` | mov x9,x19 | `FALL_THROUGH`
<a id="insn-009feedc"></a> `009feedc` | `08 00 00 14` | b 0x009feefc | `UNCONDITIONAL_JUMP`
<a id="insn-009feee0"></a> `009feee0` | `0a 0b 40 b9` | ldr w10,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-009feee4"></a> `009feee4` | `0b c7 40 f8` | ldr x11,[x24], #0xc | `FALL_THROUGH`
<a id="insn-009feee8"></a> `009feee8` | `ea 0a 00 b9` | str w10,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-009feeec"></a> `009feeec` | `eb 02 00 f9` | str x11,[x23] | `FALL_THROUGH`
<a id="insn-009feef0"></a> `009feef0` | `1f 03 13 eb` | cmp x24,x19 | `FALL_THROUGH`
<a id="insn-009feef4"></a> `009feef4` | `f7 32 00 91` | add x23,x23,#0xc | `FALL_THROUGH`
<a id="insn-009feef8"></a> `009feef8` | `00 03 00 54` | b.eq 0x009fef58 | `CONDITIONAL_JUMP`
<a id="insn-009feefc"></a> `009feefc` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-009fef00"></a> `009fef00` | `00 01 00 54` | b.eq 0x009fef20 | `CONDITIONAL_JUMP`
<a id="insn-009fef04"></a> `009fef04` | `2a 05 40 b9` | ldr w10,[x9, #0x4] | `FALL_THROUGH`
<a id="insn-009fef08"></a> `009fef08` | `0b 07 40 b9` | ldr w11,[x24, #0x4] | `FALL_THROUGH`
<a id="insn-009fef0c"></a> `009fef0c` | `5f 01 0b 6b` | cmp w10,w11 | `FALL_THROUGH`
<a id="insn-009fef10"></a> `009fef10` | `8a fe ff 54` | b.ge 0x009feee0 | `CONDITIONAL_JUMP`
<a id="insn-009fef14"></a> `009fef14` | `2a 09 40 b9` | ldr w10,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-009fef18"></a> `009fef18` | `2b c5 40 f8` | ldr x11,[x9], #0xc | `FALL_THROUGH`
<a id="insn-009fef1c"></a> `009fef1c` | `f3 ff ff 17` | b 0x009feee8 | `UNCONDITIONAL_JUMP`
<a id="insn-009fef20"></a> `009fef20` | `1f 03 13 eb` | cmp x24,x19 | `FALL_THROUGH`
<a id="insn-009fef24"></a> `009fef24` | `e0 ee ff 54` | b.eq 0x009fed00 | `CONDITIONAL_JUMP`
<a id="insn-009fef28"></a> `009fef28` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-009fef2c"></a> `009fef2c` | `09 03 08 8b` | add x9,x24,x8 | `FALL_THROUGH`
<a id="insn-009fef30"></a> `009fef30` | `ea 02 08 8b` | add x10,x23,x8 | `FALL_THROUGH`
<a id="insn-009fef34"></a> `009fef34` | `08 31 00 91` | add x8,x8,#0xc | `FALL_THROUGH`
<a id="insn-009fef38"></a> `009fef38` | `2b 09 40 b9` | ldr w11,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-009fef3c"></a> `009fef3c` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-009fef40"></a> `009fef40` | `0c 03 08 8b` | add x12,x24,x8 | `FALL_THROUGH`
<a id="insn-009fef44"></a> `009fef44` | `9f 01 13 eb` | cmp x12,x19 | `FALL_THROUGH`
<a id="insn-009fef48"></a> `009fef48` | `4b 09 00 b9` | str w11,[x10, #0x8] | `FALL_THROUGH`
<a id="insn-009fef4c"></a> `009fef4c` | `49 01 00 f9` | str x9,[x10] | `FALL_THROUGH`
<a id="insn-009fef50"></a> `009fef50` | `e1 fe ff 54` | b.ne 0x009fef2c | `CONDITIONAL_JUMP`
<a id="insn-009fef54"></a> `009fef54` | `6b ff ff 17` | b 0x009fed00 | `UNCONDITIONAL_JUMP`
<a id="insn-009fef58"></a> `009fef58` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-009fef5c"></a> `009fef5c` | `20 ed ff 54` | b.eq 0x009fed00 | `CONDITIONAL_JUMP`
<a id="insn-009fef60"></a> `009fef60` | `ea 03 1f aa` | mov x10,xzr | `FALL_THROUGH`
<a id="insn-009fef64"></a> `009fef64` | `2b 01 0a 8b` | add x11,x9,x10 | `FALL_THROUGH`
<a id="insn-009fef68"></a> `009fef68` | `ec 02 0a 8b` | add x12,x23,x10 | `FALL_THROUGH`
<a id="insn-009fef6c"></a> `009fef6c` | `4a 31 00 91` | add x10,x10,#0xc | `FALL_THROUGH`
<a id="insn-009fef70"></a> `009fef70` | `6d 09 40 b9` | ldr w13,[x11, #0x8] | `FALL_THROUGH`
<a id="insn-009fef74"></a> `009fef74` | `6b 01 40 f9` | ldr x11,[x11] | `FALL_THROUGH`
<a id="insn-009fef78"></a> `009fef78` | `2e 01 0a 8b` | add x14,x9,x10 | `FALL_THROUGH`
<a id="insn-009fef7c"></a> `009fef7c` | `df 01 08 eb` | cmp x14,x8 | `FALL_THROUGH`
<a id="insn-009fef80"></a> `009fef80` | `8d 09 00 b9` | str w13,[x12, #0x8] | `FALL_THROUGH`
<a id="insn-009fef84"></a> `009fef84` | `8b 01 00 f9` | str x11,[x12] | `FALL_THROUGH`
<a id="insn-009fef88"></a> `009fef88` | `e1 fe ff 54` | b.ne 0x009fef64 | `CONDITIONAL_JUMP`
<a id="insn-009fef8c"></a> `009fef8c` | `5d ff ff 17` | b 0x009fed00 | `UNCONDITIONAL_JUMP`
<a id="insn-009fef90"></a> `009fef90` | `fc 67 09 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009feccc`](#insn-009feccc) 範囲 `[['009feccc', '009fecff']]`
  - `CONDITIONAL_JUMP` [`009fecfc`](#insn-009fecfc) → [`009fed30`](#insn-009fed30)
  - `FALL_THROUGH` [`009fecfc`](#insn-009fecfc) → [`009fed00`](#insn-009fed00)
- ブロック [`009fed00`](#insn-009fed00) 範囲 `[['009fed00', '009fed0f']]`
  - `CONDITIONAL_JUMP` [`009fed0c`](#insn-009fed0c) → [`009fef90`](#insn-009fef90)
  - `FALL_THROUGH` [`009fed0c`](#insn-009fed0c) → [`009fed10`](#insn-009fed10)
- ブロック [`009fed10`](#insn-009fed10) 範囲 `[['009fed10', '009fed2f']]`
- ブロック [`009fed30`](#insn-009fed30) 範囲 `[['009fed30', '009fed33']]`
  - `CONDITIONAL_JUMP` [`009fed30`](#insn-009fed30) → [`009fed6c`](#insn-009fed6c)
  - `FALL_THROUGH` [`009fed30`](#insn-009fed30) → [`009fed34`](#insn-009fed34)
- ブロック [`009fed34`](#insn-009fed34) 範囲 `[['009fed34', '009fed43']]`
  - `CONDITIONAL_JUMP` [`009fed40`](#insn-009fed40) → [`009fed00`](#insn-009fed00)
  - `FALL_THROUGH` [`009fed40`](#insn-009fed40) → [`009fed44`](#insn-009fed44)
- ブロック [`009fed44`](#insn-009fed44) 範囲 `[['009fed44', '009fed6b']]`
  - `UNCONDITIONAL_JUMP` [`009fed68`](#insn-009fed68) → [`009fed00`](#insn-009fed00)
- ブロック [`009fed6c`](#insn-009fed6c) 範囲 `[['009fed6c', '009fed73']]`
  - `CONDITIONAL_JUMP` [`009fed70`](#insn-009fed70) → [`009fee08`](#insn-009fee08)
  - `FALL_THROUGH` [`009fed70`](#insn-009fed70) → [`009fed74`](#insn-009fed74)
- ブロック [`009fed74`](#insn-009fed74) 範囲 `[['009fed74', '009fed7b']]`
  - `CONDITIONAL_JUMP` [`009fed78`](#insn-009fed78) → [`009fed00`](#insn-009fed00)
  - `FALL_THROUGH` [`009fed78`](#insn-009fed78) → [`009fed7c`](#insn-009fed7c)
- ブロック [`009fed7c`](#insn-009fed7c) 範囲 `[['009fed7c', '009fed87']]`
  - `CONDITIONAL_JUMP` [`009fed84`](#insn-009fed84) → [`009fed00`](#insn-009fed00)
  - `FALL_THROUGH` [`009fed84`](#insn-009fed84) → [`009fed88`](#insn-009fed88)
- ブロック [`009fed88`](#insn-009fed88) 範囲 `[['009fed88', '009fed93']]`
  - `UNCONDITIONAL_JUMP` [`009fed90`](#insn-009fed90) → [`009fedb4`](#insn-009fedb4)
- ブロック [`009fed94`](#insn-009fed94) 範囲 `[['009fed94', '009fed97']]`
  - `FALL_THROUGH` [`009fed94`](#insn-009fed94) → [`009fed98`](#insn-009fed98)
- ブロック [`009fed98`](#insn-009fed98) 範囲 `[['009fed98', '009fed9f']]`
  - `FALL_THROUGH` [`009fed9c`](#insn-009fed9c) → [`009feda0`](#insn-009feda0)
- ブロック [`009feda0`](#insn-009feda0) 範囲 `[['009feda0', '009fedb3']]`
  - `CONDITIONAL_JUMP` [`009fedb0`](#insn-009fedb0) → [`009fed00`](#insn-009fed00)
  - `FALL_THROUGH` [`009fedb0`](#insn-009fedb0) → [`009fedb4`](#insn-009fedb4)
- ブロック [`009fedb4`](#insn-009fedb4) 範囲 `[['009fedb4', '009fedcb']]`
  - `CONDITIONAL_JUMP` [`009fedc8`](#insn-009fedc8) → [`009feda0`](#insn-009feda0)
  - `FALL_THROUGH` [`009fedc8`](#insn-009fedc8) → [`009fedcc`](#insn-009fedcc)
- ブロック [`009fedcc`](#insn-009fedcc) 範囲 `[['009fedcc', '009fedd3']]`
  - `FALL_THROUGH` [`009fedd0`](#insn-009fedd0) → [`009fedd4`](#insn-009fedd4)
- ブロック [`009fedd4`](#insn-009fedd4) 範囲 `[['009fedd4', '009fedeb']]`
  - `CONDITIONAL_JUMP` [`009fede8`](#insn-009fede8) → [`009fed94`](#insn-009fed94)
  - `FALL_THROUGH` [`009fede8`](#insn-009fede8) → [`009fedec`](#insn-009fedec)
- ブロック [`009fedec`](#insn-009fedec) 範囲 `[['009fedec', '009fedfb']]`
  - `CONDITIONAL_JUMP` [`009fedf8`](#insn-009fedf8) → [`009fedd4`](#insn-009fedd4)
  - `FALL_THROUGH` [`009fedf8`](#insn-009fedf8) → [`009fedfc`](#insn-009fedfc)
- ブロック [`009fedfc`](#insn-009fedfc) 範囲 `[['009fedfc', '009fee07']]`
  - `UNCONDITIONAL_JUMP` [`009fee04`](#insn-009fee04) → [`009fed98`](#insn-009fed98)
- ブロック [`009fee08`](#insn-009fee08) 範囲 `[['009fee08', '009fee2b']]`
  - `CONDITIONAL_JUMP` [`009fee28`](#insn-009fee28) → [`009feea8`](#insn-009feea8)
  - `FALL_THROUGH` [`009fee28`](#insn-009fee28) → [`009fee2c`](#insn-009fee2c)
- ブロック [`009fee2c`](#insn-009fee2c) 範囲 `[['009fee2c', '009fee6b']]`
  - `CONDITIONAL_JUMP` [`009fee68`](#insn-009fee68) → [`009fef90`](#insn-009fef90)
  - `FALL_THROUGH` [`009fee68`](#insn-009fee68) → [`009fee6c`](#insn-009fee6c)
- ブロック [`009fee6c`](#insn-009fee6c) 範囲 `[['009fee6c', '009feea7']]`
- ブロック [`009feea8`](#insn-009feea8) 範囲 `[['009feea8', '009feeab']]`
  - `FALL_THROUGH` [`009feea8`](#insn-009feea8) → [`009feeac`](#insn-009feeac)
- ブロック [`009feeac`](#insn-009feeac) 範囲 `[['009feeac', '009feed3']]`
  - `FALL_THROUGH` [`009feed0`](#insn-009feed0) → [`009feed4`](#insn-009feed4)
- ブロック [`009feed4`](#insn-009feed4) 範囲 `[['009feed4', '009feedf']]`
  - `UNCONDITIONAL_JUMP` [`009feedc`](#insn-009feedc) → [`009feefc`](#insn-009feefc)
- ブロック [`009feee0`](#insn-009feee0) 範囲 `[['009feee0', '009feee7']]`
  - `FALL_THROUGH` [`009feee4`](#insn-009feee4) → [`009feee8`](#insn-009feee8)
- ブロック [`009feee8`](#insn-009feee8) 範囲 `[['009feee8', '009feeef']]`
  - `FALL_THROUGH` [`009feeec`](#insn-009feeec) → [`009feef0`](#insn-009feef0)
- ブロック [`009feef0`](#insn-009feef0) 範囲 `[['009feef0', '009feefb']]`
  - `CONDITIONAL_JUMP` [`009feef8`](#insn-009feef8) → [`009fef58`](#insn-009fef58)
  - `FALL_THROUGH` [`009feef8`](#insn-009feef8) → [`009feefc`](#insn-009feefc)
- ブロック [`009feefc`](#insn-009feefc) 範囲 `[['009feefc', '009feeff']]`
  - `FALL_THROUGH` [`009feefc`](#insn-009feefc) → [`009fef00`](#insn-009fef00)
- ブロック [`009fef00`](#insn-009fef00) 範囲 `[['009fef00', '009fef03']]`
  - `CONDITIONAL_JUMP` [`009fef00`](#insn-009fef00) → [`009fef20`](#insn-009fef20)
  - `FALL_THROUGH` [`009fef00`](#insn-009fef00) → [`009fef04`](#insn-009fef04)
- ブロック [`009fef04`](#insn-009fef04) 範囲 `[['009fef04', '009fef07']]`
  - `FALL_THROUGH` [`009fef04`](#insn-009fef04) → [`009fef08`](#insn-009fef08)
- ブロック [`009fef08`](#insn-009fef08) 範囲 `[['009fef08', '009fef13']]`
  - `CONDITIONAL_JUMP` [`009fef10`](#insn-009fef10) → [`009feee0`](#insn-009feee0)
  - `FALL_THROUGH` [`009fef10`](#insn-009fef10) → [`009fef14`](#insn-009fef14)
- ブロック [`009fef14`](#insn-009fef14) 範囲 `[['009fef14', '009fef1f']]`
  - `UNCONDITIONAL_JUMP` [`009fef1c`](#insn-009fef1c) → [`009feee8`](#insn-009feee8)
- ブロック [`009fef20`](#insn-009fef20) 範囲 `[['009fef20', '009fef27']]`
  - `CONDITIONAL_JUMP` [`009fef24`](#insn-009fef24) → [`009fed00`](#insn-009fed00)
  - `FALL_THROUGH` [`009fef24`](#insn-009fef24) → [`009fef28`](#insn-009fef28)
- ブロック [`009fef28`](#insn-009fef28) 範囲 `[['009fef28', '009fef2b']]`
  - `FALL_THROUGH` [`009fef28`](#insn-009fef28) → [`009fef2c`](#insn-009fef2c)
- ブロック [`009fef2c`](#insn-009fef2c) 範囲 `[['009fef2c', '009fef53']]`
  - `CONDITIONAL_JUMP` [`009fef50`](#insn-009fef50) → [`009fef2c`](#insn-009fef2c)
  - `FALL_THROUGH` [`009fef50`](#insn-009fef50) → [`009fef54`](#insn-009fef54)
- ブロック [`009fef54`](#insn-009fef54) 範囲 `[['009fef54', '009fef57']]`
  - `UNCONDITIONAL_JUMP` [`009fef54`](#insn-009fef54) → [`009fed00`](#insn-009fed00)
- ブロック [`009fef58`](#insn-009fef58) 範囲 `[['009fef58', '009fef5f']]`
  - `CONDITIONAL_JUMP` [`009fef5c`](#insn-009fef5c) → [`009fed00`](#insn-009fed00)
  - `FALL_THROUGH` [`009fef5c`](#insn-009fef5c) → [`009fef60`](#insn-009fef60)
- ブロック [`009fef60`](#insn-009fef60) 範囲 `[['009fef60', '009fef63']]`
  - `FALL_THROUGH` [`009fef60`](#insn-009fef60) → [`009fef64`](#insn-009fef64)
- ブロック [`009fef64`](#insn-009fef64) 範囲 `[['009fef64', '009fef8b']]`
  - `CONDITIONAL_JUMP` [`009fef88`](#insn-009fef88) → [`009fef64`](#insn-009fef64)
  - `FALL_THROUGH` [`009fef88`](#insn-009fef88) → [`009fef8c`](#insn-009fef8c)
- ブロック [`009fef8c`](#insn-009fef8c) 範囲 `[['009fef8c', '009fef8f']]`
  - `UNCONDITIONAL_JUMP` [`009fef8c`](#insn-009fef8c) → [`009fed00`](#insn-009fed00)
- ブロック [`009fef90`](#insn-009fef90) 範囲 `[['009fef90', '009fef93']]`

## 命令位置別の参照

- [`009fecd0`](#insn-009fecd0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fecd4`](#insn-009fecd4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fecd8`](#insn-009fecd8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fecdc`](#insn-009fecdc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fece0`](#insn-009fece0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fece4`](#insn-009fece4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fecf8`](#insn-009fecf8) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fecfc`](#insn-009fecfc) → [`009fed30`](#insn-009fed30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fed04`](#insn-009fed04) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fed0c`](#insn-009fed0c) → [`009fef90`](#insn-009fef90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fed10`](#insn-009fed10) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fed14`](#insn-009fed14) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fed18`](#insn-009fed18) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fed1c`](#insn-009fed1c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fed20`](#insn-009fed20) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fed24`](#insn-009fed24) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fed30`](#insn-009fed30) → [`009fed6c`](#insn-009fed6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fed40`](#insn-009fed40) → [`009fed00`](#insn-009fed00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fed68`](#insn-009fed68) → [`009fed00`](#insn-009fed00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fed70`](#insn-009fed70) → [`009fee08`](#insn-009fee08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fed78`](#insn-009fed78) → [`009fed00`](#insn-009fed00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fed84`](#insn-009fed84) → [`009fed00`](#insn-009fed00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fed90`](#insn-009fed90) → [`009fedb4`](#insn-009fedb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fedb0`](#insn-009fedb0) → [`009fed00`](#insn-009fed00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fedc8`](#insn-009fedc8) → [`009feda0`](#insn-009feda0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fede8`](#insn-009fede8) → [`009fed94`](#insn-009fed94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fedf8`](#insn-009fedf8) → [`009fedd4`](#insn-009fedd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fee04`](#insn-009fee04) → [`009fed98`](#insn-009fed98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fee28`](#insn-009fee28) → [`009feea8`](#insn-009feea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fee38`](#insn-009fee38) → [`009feccc`](#insn-009feccc) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009feccc` · 推定シンボル `None` · 推定型 `None`
- [`009fee58`](#insn-009fee58) → [`009feccc`](#insn-009feccc) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009feccc` · 推定シンボル `None` · 推定型 `None`
- [`009fee60`](#insn-009fee60) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fee68`](#insn-009fee68) → [`009fef90`](#insn-009fef90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fee88`](#insn-009fee88) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fee8c`](#insn-009fee8c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fee90`](#insn-009fee90) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fee94`](#insn-009fee94) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fee98`](#insn-009fee98) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fee9c`](#insn-009fee9c) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009feea4`](#insn-009feea4) → [`009ff20c`](../009ff/009ff20c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009ff20c` · 推定シンボル `None` · 推定型 `None`
- [`009feeb4`](#insn-009feeb4) → [`009fef94`](009fef94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009fef94` · 推定シンボル `None` · 推定型 `None`
- [`009feed0`](#insn-009feed0) → [`009fef94`](009fef94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009fef94` · 推定シンボル `None` · 推定型 `None`
- [`009feedc`](#insn-009feedc) → [`009feefc`](#insn-009feefc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009feef8`](#insn-009feef8) → [`009fef58`](#insn-009fef58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fef00`](#insn-009fef00) → [`009fef20`](#insn-009fef20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fef10`](#insn-009fef10) → [`009feee0`](#insn-009feee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fef1c`](#insn-009fef1c) → [`009feee8`](#insn-009feee8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fef24`](#insn-009fef24) → [`009fed00`](#insn-009fed00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fef50`](#insn-009fef50) → [`009fef2c`](#insn-009fef2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fef54`](#insn-009fef54) → [`009fed00`](#insn-009fed00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fef5c`](#insn-009fef5c) → [`009fed00`](#insn-009fed00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fef88`](#insn-009fef88) → [`009fef64`](#insn-009fef64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fef8c`](#insn-009fef8c) → [`009fed00`](#insn-009fed00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fef90`](#insn-009fef90) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009fecd0`](#insn-009fecd0)

~~~json
{
  "source": "009fecd0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fecd4`](#insn-009fecd4)

~~~json
{
  "source": "009fecd4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fecd8`](#insn-009fecd8)

~~~json
{
  "source": "009fecd8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fecdc`](#insn-009fecdc)

~~~json
{
  "source": "009fecdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fece0`](#insn-009fece0)

~~~json
{
  "source": "009fece0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fece4`](#insn-009fece4)

~~~json
{
  "source": "009fece4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fecf8`](#insn-009fecf8)

~~~json
{
  "source": "009fecf8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fecfc`](#insn-009fecfc)

~~~json
{
  "source": "009fecfc",
  "target": "009fed30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fed04`](#insn-009fed04)

~~~json
{
  "source": "009fed04",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fed0c`](#insn-009fed0c)

~~~json
{
  "source": "009fed0c",
  "target": "009fef90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fed10`](#insn-009fed10)

~~~json
{
  "source": "009fed10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fed14`](#insn-009fed14)

~~~json
{
  "source": "009fed14",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fed18`](#insn-009fed18)

~~~json
{
  "source": "009fed18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fed1c`](#insn-009fed1c)

~~~json
{
  "source": "009fed1c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fed20`](#insn-009fed20)

~~~json
{
  "source": "009fed20",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fed24`](#insn-009fed24)

~~~json
{
  "source": "009fed24",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fed30`](#insn-009fed30)

~~~json
{
  "source": "009fed30",
  "target": "009fed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fed40`](#insn-009fed40)

~~~json
{
  "source": "009fed40",
  "target": "009fed00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fed68`](#insn-009fed68)

~~~json
{
  "source": "009fed68",
  "target": "009fed00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fed70`](#insn-009fed70)

~~~json
{
  "source": "009fed70",
  "target": "009fee08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fed78`](#insn-009fed78)

~~~json
{
  "source": "009fed78",
  "target": "009fed00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fed84`](#insn-009fed84)

~~~json
{
  "source": "009fed84",
  "target": "009fed00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fed90`](#insn-009fed90)

~~~json
{
  "source": "009fed90",
  "target": "009fedb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fedb0`](#insn-009fedb0)

~~~json
{
  "source": "009fedb0",
  "target": "009fed00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fedc8`](#insn-009fedc8)

~~~json
{
  "source": "009fedc8",
  "target": "009feda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fede8`](#insn-009fede8)

~~~json
{
  "source": "009fede8",
  "target": "009fed94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fedf8`](#insn-009fedf8)

~~~json
{
  "source": "009fedf8",
  "target": "009fedd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fee04`](#insn-009fee04)

~~~json
{
  "source": "009fee04",
  "target": "009fed98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fee28`](#insn-009fee28)

~~~json
{
  "source": "009fee28",
  "target": "009feea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fee38`](#insn-009fee38)

~~~json
{
  "source": "009fee38",
  "target": "009feccc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fee58`](#insn-009fee58)

~~~json
{
  "source": "009fee58",
  "target": "009feccc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009fee60`](#insn-009fee60)

~~~json
{
  "source": "009fee60",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fee68`](#insn-009fee68)

~~~json
{
  "source": "009fee68",
  "target": "009fef90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fee88`](#insn-009fee88)

~~~json
{
  "source": "009fee88",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fee8c`](#insn-009fee8c)

~~~json
{
  "source": "009fee8c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fee90`](#insn-009fee90)

~~~json
{
  "source": "009fee90",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fee94`](#insn-009fee94)

~~~json
{
  "source": "009fee94",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fee98`](#insn-009fee98)

~~~json
{
  "source": "009fee98",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fee9c`](#insn-009fee9c)

~~~json
{
  "source": "009fee9c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009feea4`](#insn-009feea4)

~~~json
{
  "source": "009feea4",
  "target": "009ff20c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009feeb4`](#insn-009feeb4)

~~~json
{
  "source": "009feeb4",
  "target": "009fef94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009feed0`](#insn-009feed0)

~~~json
{
  "source": "009feed0",
  "target": "009fef94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009feedc`](#insn-009feedc)

~~~json
{
  "source": "009feedc",
  "target": "009feefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009feef8`](#insn-009feef8)

~~~json
{
  "source": "009feef8",
  "target": "009fef58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fef00`](#insn-009fef00)

~~~json
{
  "source": "009fef00",
  "target": "009fef20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fef10`](#insn-009fef10)

~~~json
{
  "source": "009fef10",
  "target": "009feee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fef1c`](#insn-009fef1c)

~~~json
{
  "source": "009fef1c",
  "target": "009feee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fef24`](#insn-009fef24)

~~~json
{
  "source": "009fef24",
  "target": "009fed00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fef50`](#insn-009fef50)

~~~json
{
  "source": "009fef50",
  "target": "009fef2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fef54`](#insn-009fef54)

~~~json
{
  "source": "009fef54",
  "target": "009fed00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fef5c`](#insn-009fef5c)

~~~json
{
  "source": "009fef5c",
  "target": "009fed00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fef88`](#insn-009fef88)

~~~json
{
  "source": "009fef88",
  "target": "009fef64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fef8c`](#insn-009fef8c)

~~~json
{
  "source": "009fef8c",
  "target": "009fed00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fef90`](#insn-009fef90)

~~~json
{
  "source": "009fef90",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
