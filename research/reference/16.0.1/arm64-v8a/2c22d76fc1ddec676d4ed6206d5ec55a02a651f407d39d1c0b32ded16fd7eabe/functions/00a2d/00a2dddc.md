# 00a2dddc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00a2dbe4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2d/00a2dbe4.md) · 移動量 `+0x1f8`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0033.md#compare-952dfec40de97547edd6a6dbc49f72c5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00a2de30`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2d/00a2de30.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0032.md#compare-16beb2983aaccc4037da6913bfdc603f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a2dddc",
  "name": "FUN_00a2dddc",
  "size": 600,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "49be9be86752d039ca7e895eca198b29b7a5fdcf0839a1e9a0433e974f665bc9",
  "source_text_sha256": "49be9be86752d039ca7e895eca198b29b7a5fdcf0839a1e9a0433e974f665bc9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a2dddc",
        "00a2e02f"
      ],
      [
        "00a2e060",
        "00a2e063"
      ]
    ],
    "bytes_sha256": "a87e02159fcbf27fc4836b006e408447b129dda5835eb61a761f0d2f651e60ba",
    "instruction_count": 150,
    "instruction_bytes": 600,
    "body_bytes": 600,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a2b2e8](../00a2b/00a2b2e8.md)

## 呼び出し先

- [00480b90](../00480/00480b90.md)
- [00480d48](../00480/00480d48.md)
- [00480e28](../00480/00480e28.md)
- [005c179c](../005c1/005c179c.md)
- [00691800](../00691/00691800.md)
- [00c57ee0](../00c57/00c57ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3340 bytes

~~~c

void FUN_00a2dddc(long *param_1,undefined8 param_2)

{
  undefined4 uVar1;
  byte bVar2;
  long lVar3;
  long lVar4;
  undefined8 *puVar5;
  long *plVar6;
  bool bVar7;
  undefined8 *puVar8;
  long *plVar9;
  long *plVar10;
  undefined8 *puVar11;
  undefined8 *local_80;
  undefined8 local_78;
  ulong local_70;
  long local_68;
  
  lVar3 = tpidr_el0;
  local_68 = *(long *)(lVar3 + 0x28);
  FUN_00480b90(param_2,(short)param_1[5]);
  plVar9 = (long *)param_1[3];
  while (plVar9 != param_1 + 4) {
    bVar2 = *(byte *)(plVar9 + 4);
    FUN_00480b90(param_2,*(undefined4 *)((long)plVar9 + 0x1c));
    FUN_00480d48(param_2,bVar2 & 1);
    plVar6 = (long *)plVar9[1];
    plVar10 = plVar9;
    if ((long *)plVar9[1] == (long *)0x0) {
      do {
        plVar9 = (long *)plVar10[2];
        bVar7 = (long *)*plVar9 != plVar10;
        plVar10 = plVar9;
      } while (bVar7);
    }
    else {
      do {
        plVar9 = plVar6;
        plVar6 = (long *)*plVar9;
      } while ((long *)*plVar9 != (long *)0x0);
    }
  }
  FUN_00480b90(param_2,(short)param_1[8]);
  plVar9 = (long *)param_1[6];
  if (plVar9 != param_1 + 7) {
    do {
      lVar4 = plVar9[4];
      local_78 = 0;
      local_70 = 0;
      local_80 = &local_78;
      FUN_00691800(&local_80,plVar9[5],plVar9 + 6);
      FUN_00480b90(param_2,(int)lVar4);
      FUN_00480b90(param_2,local_70 & 0xffff);
      puVar8 = local_80;
      while (puVar8 != &local_78) {
        uVar1 = *(undefined4 *)(puVar8 + 4);
        FUN_00480b90(param_2,*(undefined4 *)((long)puVar8 + 0x1c));
        FUN_00480b90(param_2,uVar1);
        puVar5 = (undefined8 *)puVar8[1];
        puVar11 = puVar8;
        if ((undefined8 *)puVar8[1] == (undefined8 *)0x0) {
          do {
            puVar8 = (undefined8 *)puVar11[2];
            bVar7 = (undefined8 *)*puVar8 != puVar11;
            puVar11 = puVar8;
          } while (bVar7);
        }
        else {
          do {
            puVar8 = puVar5;
            puVar5 = (undefined8 *)*puVar8;
          } while ((undefined8 *)*puVar8 != (undefined8 *)0x0);
        }
      }
      FUN_005c179c(&local_80,local_78);
      plVar6 = (long *)plVar9[1];
      plVar10 = plVar9;
      if ((long *)plVar9[1] == (long *)0x0) {
        do {
          plVar9 = (long *)plVar10[2];
          bVar7 = (long *)*plVar9 != plVar10;
          plVar10 = plVar9;
        } while (bVar7);
      }
      else {
        do {
          plVar9 = plVar6;
          plVar6 = (long *)*plVar9;
        } while ((long *)*plVar9 != (long *)0x0);
      }
    } while (plVar9 != param_1 + 7);
  }
  FUN_00480b90(param_2,(short)param_1[2]);
  plVar9 = (long *)*param_1;
  while (plVar9 != param_1 + 1) {
    uVar1 = *(undefined4 *)(plVar9 + 4);
    FUN_00480b90(param_2,*(undefined4 *)((long)plVar9 + 0x1c));
    FUN_00480e28(param_2,uVar1);
    plVar6 = (long *)plVar9[1];
    plVar10 = plVar9;
    if ((long *)plVar9[1] == (long *)0x0) {
      do {
        plVar9 = (long *)plVar10[2];
        bVar7 = (long *)*plVar9 != plVar10;
        plVar10 = plVar9;
      } while (bVar7);
    }
    else {
      do {
        plVar9 = plVar6;
        plVar6 = (long *)*plVar9;
      } while ((long *)*plVar9 != (long *)0x0);
    }
  }
  if (*(long *)(lVar3 + 0x28) == local_68) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a2dddc"></a> `00a2dddc` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00a2dde0"></a> `00a2dde0` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a2dde4"></a> `00a2dde4` | `fb 23 00 f9` | str x27,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a2dde8"></a> `00a2dde8` | `fa 67 05 a9` | stp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a2ddec"></a> `00a2ddec` | `f8 5f 06 a9` | stp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00a2ddf0"></a> `00a2ddf0` | `f6 57 07 a9` | stp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a2ddf4"></a> `00a2ddf4` | `f4 4f 08 a9` | stp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00a2ddf8"></a> `00a2ddf8` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00a2ddfc"></a> `00a2ddfc` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00a2de00"></a> `00a2de00` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00a2de04"></a> `00a2de04` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00a2de08"></a> `00a2de08` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00a2de0c"></a> `00a2de0c` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a2de10"></a> `00a2de10` | `08 50 40 79` | ldrh w8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00a2de14"></a> `00a2de14` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00a2de18"></a> `00a2de18` | `e1 03 08 2a` | mov w1,w8 | `FALL_THROUGH`
<a id="insn-00a2de1c"></a> `00a2de1c` | `5d 4b e9 97` | bl 0x00480b90 | `UNCONDITIONAL_CALL`
<a id="insn-00a2de20"></a> `00a2de20` | `97 0e 40 f9` | ldr x23,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00a2de24"></a> `00a2de24` | `95 82 00 91` | add x21,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00a2de28"></a> `00a2de28` | `ff 02 15 eb` | cmp x23,x21 | `FALL_THROUGH`
<a id="insn-00a2de2c"></a> `00a2de2c` | `c1 01 00 54` | b.ne 0x00a2de64 | `CONDITIONAL_JUMP`
<a id="insn-00a2de30"></a> `00a2de30` | `81 82 40 79` | ldrh w1,[x20, #0x40] | `FALL_THROUGH`
<a id="insn-00a2de34"></a> `00a2de34` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a2de38"></a> `00a2de38` | `56 4b e9 97` | bl 0x00480b90 | `UNCONDITIONAL_CALL`
<a id="insn-00a2de3c"></a> `00a2de3c` | `9a 1a 40 f9` | ldr x26,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00a2de40"></a> `00a2de40` | `98 e2 00 91` | add x24,x20,#0x38 | `FALL_THROUGH`
<a id="insn-00a2de44"></a> `00a2de44` | `5f 03 18 eb` | cmp x26,x24 | `FALL_THROUGH`
<a id="insn-00a2de48"></a> `00a2de48` | `40 0a 00 54` | b.eq 0x00a2df90 | `CONDITIONAL_JUMP`
<a id="insn-00a2de4c"></a> `00a2de4c` | `f7 23 00 91` | add x23,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00a2de50"></a> `00a2de50` | `f9 42 00 91` | add x25,x23,#0x10 | `FALL_THROUGH`
<a id="insn-00a2de54"></a> `00a2de54` | `1a 00 00 14` | b 0x00a2debc | `UNCONDITIONAL_JUMP`
<a id="insn-00a2de58"></a> `00a2de58` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00a2de5c"></a> `00a2de5c` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00a2de60"></a> `00a2de60` | `80 fe ff 54` | b.eq 0x00a2de30 | `CONDITIONAL_JUMP`
<a id="insn-00a2de64"></a> `00a2de64` | `e1 1e 40 b9` | ldr w1,[x23, #0x1c] | `FALL_THROUGH`
<a id="insn-00a2de68"></a> `00a2de68` | `f8 82 40 39` | ldrb w24,[x23, #0x20] | `FALL_THROUGH`
<a id="insn-00a2de6c"></a> `00a2de6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a2de70"></a> `00a2de70` | `48 4b e9 97` | bl 0x00480b90 | `UNCONDITIONAL_CALL`
<a id="insn-00a2de74"></a> `00a2de74` | `01 03 00 12` | and w1,w24,#0x1 | `FALL_THROUGH`
<a id="insn-00a2de78"></a> `00a2de78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a2de7c"></a> `00a2de7c` | `b3 4b e9 97` | bl 0x00480d48 | `UNCONDITIONAL_CALL`
<a id="insn-00a2de80"></a> `00a2de80` | `e9 06 40 f9` | ldr x9,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00a2de84"></a> `00a2de84` | `a9 00 00 b4` | cbz x9,0x00a2de98 | `CONDITIONAL_JUMP`
<a id="insn-00a2de88"></a> `00a2de88` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00a2de8c"></a> `00a2de8c` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00a2de90"></a> `00a2de90` | `c9 ff ff b5` | cbnz x9,0x00a2de88 | `CONDITIONAL_JUMP`
<a id="insn-00a2de94"></a> `00a2de94` | `f1 ff ff 17` | b 0x00a2de58 | `UNCONDITIONAL_JUMP`
<a id="insn-00a2de98"></a> `00a2de98` | `e8 0a 40 f9` | ldr x8,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00a2de9c"></a> `00a2de9c` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00a2dea0"></a> `00a2dea0` | `3f 01 17 eb` | cmp x9,x23 | `FALL_THROUGH`
<a id="insn-00a2dea4"></a> `00a2dea4` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00a2dea8"></a> `00a2dea8` | `81 ff ff 54` | b.ne 0x00a2de98 | `CONDITIONAL_JUMP`
<a id="insn-00a2deac"></a> `00a2deac` | `eb ff ff 17` | b 0x00a2de58 | `UNCONDITIONAL_JUMP`
<a id="insn-00a2deb0"></a> `00a2deb0` | `1f 01 18 eb` | cmp x8,x24 | `FALL_THROUGH`
<a id="insn-00a2deb4"></a> `00a2deb4` | `fa 03 08 aa` | mov x26,x8 | `FALL_THROUGH`
<a id="insn-00a2deb8"></a> `00a2deb8` | `c0 06 00 54` | b.eq 0x00a2df90 | `CONDITIONAL_JUMP`
<a id="insn-00a2debc"></a> `00a2debc` | `48 23 40 b9` | ldr w8,[x26, #0x20] | `FALL_THROUGH`
<a id="insn-00a2dec0"></a> `00a2dec0` | `41 17 40 f9` | ldr x1,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00a2dec4"></a> `00a2dec4` | `3f 7f 00 a9` | stp xzr,xzr,[x25] | `FALL_THROUGH`
<a id="insn-00a2dec8"></a> `00a2dec8` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a2decc"></a> `00a2decc` | `e8 0b 00 b9` | str w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a2ded0"></a> `00a2ded0` | `e0 22 00 91` | add x0,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00a2ded4"></a> `00a2ded4` | `42 c3 00 91` | add x2,x26,#0x30 | `FALL_THROUGH`
<a id="insn-00a2ded8"></a> `00a2ded8` | `4a 8e f1 97` | bl 0x00691800 | `UNCONDITIONAL_CALL`
<a id="insn-00a2dedc"></a> `00a2dedc` | `e1 0b 40 b9` | ldr w1,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a2dee0"></a> `00a2dee0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a2dee4"></a> `00a2dee4` | `2b 4b e9 97` | bl 0x00480b90 | `UNCONDITIONAL_CALL`
<a id="insn-00a2dee8"></a> `00a2dee8` | `e1 43 40 79` | ldrh w1,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a2deec"></a> `00a2deec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a2def0"></a> `00a2def0` | `28 4b e9 97` | bl 0x00480b90 | `UNCONDITIONAL_CALL`
<a id="insn-00a2def4"></a> `00a2def4` | `fb 0b 40 f9` | ldr x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a2def8"></a> `00a2def8` | `7f 03 19 eb` | cmp x27,x25 | `FALL_THROUGH`
<a id="insn-00a2defc"></a> `00a2defc` | `a1 01 00 54` | b.ne 0x00a2df30 | `CONDITIONAL_JUMP`
<a id="insn-00a2df00"></a> `00a2df00` | `e1 0f 40 f9` | ldr x1,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00a2df04"></a> `00a2df04` | `e0 22 00 91` | add x0,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00a2df08"></a> `00a2df08` | `25 4e ee 97` | bl 0x005c179c | `UNCONDITIONAL_CALL`
<a id="insn-00a2df0c"></a> `00a2df0c` | `49 07 40 f9` | ldr x9,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00a2df10"></a> `00a2df10` | `49 03 00 b4` | cbz x9,0x00a2df78 | `CONDITIONAL_JUMP`
<a id="insn-00a2df14"></a> `00a2df14` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00a2df18"></a> `00a2df18` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00a2df1c"></a> `00a2df1c` | `c9 ff ff b5` | cbnz x9,0x00a2df14 | `CONDITIONAL_JUMP`
<a id="insn-00a2df20"></a> `00a2df20` | `e4 ff ff 17` | b 0x00a2deb0 | `UNCONDITIONAL_JUMP`
<a id="insn-00a2df24"></a> `00a2df24` | `1f 01 19 eb` | cmp x8,x25 | `FALL_THROUGH`
<a id="insn-00a2df28"></a> `00a2df28` | `fb 03 08 aa` | mov x27,x8 | `FALL_THROUGH`
<a id="insn-00a2df2c"></a> `00a2df2c` | `a0 fe ff 54` | b.eq 0x00a2df00 | `CONDITIONAL_JUMP`
<a id="insn-00a2df30"></a> `00a2df30` | `61 d7 43 29` | ldp w1,w21,[x27, #0x1c] | `FALL_THROUGH`
<a id="insn-00a2df34"></a> `00a2df34` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a2df38"></a> `00a2df38` | `16 4b e9 97` | bl 0x00480b90 | `UNCONDITIONAL_CALL`
<a id="insn-00a2df3c"></a> `00a2df3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a2df40"></a> `00a2df40` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00a2df44"></a> `00a2df44` | `13 4b e9 97` | bl 0x00480b90 | `UNCONDITIONAL_CALL`
<a id="insn-00a2df48"></a> `00a2df48` | `69 07 40 f9` | ldr x9,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-00a2df4c"></a> `00a2df4c` | `a9 00 00 b4` | cbz x9,0x00a2df60 | `CONDITIONAL_JUMP`
<a id="insn-00a2df50"></a> `00a2df50` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00a2df54"></a> `00a2df54` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00a2df58"></a> `00a2df58` | `c9 ff ff b5` | cbnz x9,0x00a2df50 | `CONDITIONAL_JUMP`
<a id="insn-00a2df5c"></a> `00a2df5c` | `f2 ff ff 17` | b 0x00a2df24 | `UNCONDITIONAL_JUMP`
<a id="insn-00a2df60"></a> `00a2df60` | `68 0b 40 f9` | ldr x8,[x27, #0x10] | `FALL_THROUGH`
<a id="insn-00a2df64"></a> `00a2df64` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00a2df68"></a> `00a2df68` | `3f 01 1b eb` | cmp x9,x27 | `FALL_THROUGH`
<a id="insn-00a2df6c"></a> `00a2df6c` | `fb 03 08 aa` | mov x27,x8 | `FALL_THROUGH`
<a id="insn-00a2df70"></a> `00a2df70` | `81 ff ff 54` | b.ne 0x00a2df60 | `CONDITIONAL_JUMP`
<a id="insn-00a2df74"></a> `00a2df74` | `ec ff ff 17` | b 0x00a2df24 | `UNCONDITIONAL_JUMP`
<a id="insn-00a2df78"></a> `00a2df78` | `48 0b 40 f9` | ldr x8,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00a2df7c"></a> `00a2df7c` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00a2df80"></a> `00a2df80` | `3f 01 1a eb` | cmp x9,x26 | `FALL_THROUGH`
<a id="insn-00a2df84"></a> `00a2df84` | `fa 03 08 aa` | mov x26,x8 | `FALL_THROUGH`
<a id="insn-00a2df88"></a> `00a2df88` | `81 ff ff 54` | b.ne 0x00a2df78 | `CONDITIONAL_JUMP`
<a id="insn-00a2df8c"></a> `00a2df8c` | `c9 ff ff 17` | b 0x00a2deb0 | `UNCONDITIONAL_JUMP`
<a id="insn-00a2df90"></a> `00a2df90` | `81 22 40 79` | ldrh w1,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00a2df94"></a> `00a2df94` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a2df98"></a> `00a2df98` | `fe 4a e9 97` | bl 0x00480b90 | `UNCONDITIONAL_CALL`
<a id="insn-00a2df9c"></a> `00a2df9c` | `97 02 40 f9` | ldr x23,[x20] | `FALL_THROUGH`
<a id="insn-00a2dfa0"></a> `00a2dfa0` | `95 22 00 91` | add x21,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00a2dfa4"></a> `00a2dfa4` | `ff 02 15 eb` | cmp x23,x21 | `FALL_THROUGH`
<a id="insn-00a2dfa8"></a> `00a2dfa8` | `01 02 00 54` | b.ne 0x00a2dfe8 | `CONDITIONAL_JUMP`
<a id="insn-00a2dfac"></a> `00a2dfac` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00a2dfb0"></a> `00a2dfb0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a2dfb4"></a> `00a2dfb4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a2dfb8"></a> `00a2dfb8` | `41 05 00 54` | b.ne 0x00a2e060 | `CONDITIONAL_JUMP`
<a id="insn-00a2dfbc"></a> `00a2dfbc` | `f4 4f 48 a9` | ldp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00a2dfc0"></a> `00a2dfc0` | `fb 23 40 f9` | ldr x27,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a2dfc4"></a> `00a2dfc4` | `f6 57 47 a9` | ldp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a2dfc8"></a> `00a2dfc8` | `f8 5f 46 a9` | ldp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00a2dfcc"></a> `00a2dfcc` | `fa 67 45 a9` | ldp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a2dfd0"></a> `00a2dfd0` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a2dfd4"></a> `00a2dfd4` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00a2dfd8"></a> `00a2dfd8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a2dfdc"></a> `00a2dfdc` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00a2dfe0"></a> `00a2dfe0` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00a2dfe4"></a> `00a2dfe4` | `40 fe ff 54` | b.eq 0x00a2dfac | `CONDITIONAL_JUMP`
<a id="insn-00a2dfe8"></a> `00a2dfe8` | `e1 d2 43 29` | ldp w1,w20,[x23, #0x1c] | `FALL_THROUGH`
<a id="insn-00a2dfec"></a> `00a2dfec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a2dff0"></a> `00a2dff0` | `e8 4a e9 97` | bl 0x00480b90 | `UNCONDITIONAL_CALL`
<a id="insn-00a2dff4"></a> `00a2dff4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a2dff8"></a> `00a2dff8` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00a2dffc"></a> `00a2dffc` | `8b 4b e9 97` | bl 0x00480e28 | `UNCONDITIONAL_CALL`
<a id="insn-00a2e000"></a> `00a2e000` | `e9 06 40 f9` | ldr x9,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00a2e004"></a> `00a2e004` | `a9 00 00 b4` | cbz x9,0x00a2e018 | `CONDITIONAL_JUMP`
<a id="insn-00a2e008"></a> `00a2e008` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00a2e00c"></a> `00a2e00c` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00a2e010"></a> `00a2e010` | `c9 ff ff b5` | cbnz x9,0x00a2e008 | `CONDITIONAL_JUMP`
<a id="insn-00a2e014"></a> `00a2e014` | `f2 ff ff 17` | b 0x00a2dfdc | `UNCONDITIONAL_JUMP`
<a id="insn-00a2e018"></a> `00a2e018` | `e8 0a 40 f9` | ldr x8,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00a2e01c"></a> `00a2e01c` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00a2e020"></a> `00a2e020` | `3f 01 17 eb` | cmp x9,x23 | `FALL_THROUGH`
<a id="insn-00a2e024"></a> `00a2e024` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00a2e028"></a> `00a2e028` | `81 ff ff 54` | b.ne 0x00a2e018 | `CONDITIONAL_JUMP`
<a id="insn-00a2e02c"></a> `00a2e02c` | `ec ff ff 17` | b 0x00a2dfdc | `UNCONDITIONAL_JUMP`
<a id="insn-00a2e060"></a> `00a2e060` | `a0 a7 08 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a2dddc`](#insn-00a2dddc) 範囲 `[['00a2dddc', '00a2de2f']]`
  - `CONDITIONAL_JUMP` [`00a2de2c`](#insn-00a2de2c) → [`00a2de64`](#insn-00a2de64)
  - `FALL_THROUGH` [`00a2de2c`](#insn-00a2de2c) → [`00a2de30`](#insn-00a2de30)
- ブロック [`00a2de30`](#insn-00a2de30) 範囲 `[['00a2de30', '00a2de4b']]`
  - `CONDITIONAL_JUMP` [`00a2de48`](#insn-00a2de48) → [`00a2df90`](#insn-00a2df90)
  - `FALL_THROUGH` [`00a2de48`](#insn-00a2de48) → [`00a2de4c`](#insn-00a2de4c)
- ブロック [`00a2de4c`](#insn-00a2de4c) 範囲 `[['00a2de4c', '00a2de57']]`
  - `UNCONDITIONAL_JUMP` [`00a2de54`](#insn-00a2de54) → [`00a2debc`](#insn-00a2debc)
- ブロック [`00a2de58`](#insn-00a2de58) 範囲 `[['00a2de58', '00a2de63']]`
  - `CONDITIONAL_JUMP` [`00a2de60`](#insn-00a2de60) → [`00a2de30`](#insn-00a2de30)
  - `FALL_THROUGH` [`00a2de60`](#insn-00a2de60) → [`00a2de64`](#insn-00a2de64)
- ブロック [`00a2de64`](#insn-00a2de64) 範囲 `[['00a2de64', '00a2de87']]`
  - `CONDITIONAL_JUMP` [`00a2de84`](#insn-00a2de84) → [`00a2de98`](#insn-00a2de98)
  - `FALL_THROUGH` [`00a2de84`](#insn-00a2de84) → [`00a2de88`](#insn-00a2de88)
- ブロック [`00a2de88`](#insn-00a2de88) 範囲 `[['00a2de88', '00a2de93']]`
  - `CONDITIONAL_JUMP` [`00a2de90`](#insn-00a2de90) → [`00a2de88`](#insn-00a2de88)
  - `FALL_THROUGH` [`00a2de90`](#insn-00a2de90) → [`00a2de94`](#insn-00a2de94)
- ブロック [`00a2de94`](#insn-00a2de94) 範囲 `[['00a2de94', '00a2de97']]`
  - `UNCONDITIONAL_JUMP` [`00a2de94`](#insn-00a2de94) → [`00a2de58`](#insn-00a2de58)
- ブロック [`00a2de98`](#insn-00a2de98) 範囲 `[['00a2de98', '00a2deab']]`
  - `CONDITIONAL_JUMP` [`00a2dea8`](#insn-00a2dea8) → [`00a2de98`](#insn-00a2de98)
  - `FALL_THROUGH` [`00a2dea8`](#insn-00a2dea8) → [`00a2deac`](#insn-00a2deac)
- ブロック [`00a2deac`](#insn-00a2deac) 範囲 `[['00a2deac', '00a2deaf']]`
  - `UNCONDITIONAL_JUMP` [`00a2deac`](#insn-00a2deac) → [`00a2de58`](#insn-00a2de58)
- ブロック [`00a2deb0`](#insn-00a2deb0) 範囲 `[['00a2deb0', '00a2debb']]`
  - `CONDITIONAL_JUMP` [`00a2deb8`](#insn-00a2deb8) → [`00a2df90`](#insn-00a2df90)
  - `FALL_THROUGH` [`00a2deb8`](#insn-00a2deb8) → [`00a2debc`](#insn-00a2debc)
- ブロック [`00a2debc`](#insn-00a2debc) 範囲 `[['00a2debc', '00a2deff']]`
  - `CONDITIONAL_JUMP` [`00a2defc`](#insn-00a2defc) → [`00a2df30`](#insn-00a2df30)
  - `FALL_THROUGH` [`00a2defc`](#insn-00a2defc) → [`00a2df00`](#insn-00a2df00)
- ブロック [`00a2df00`](#insn-00a2df00) 範囲 `[['00a2df00', '00a2df13']]`
  - `CONDITIONAL_JUMP` [`00a2df10`](#insn-00a2df10) → [`00a2df78`](#insn-00a2df78)
  - `FALL_THROUGH` [`00a2df10`](#insn-00a2df10) → [`00a2df14`](#insn-00a2df14)
- ブロック [`00a2df14`](#insn-00a2df14) 範囲 `[['00a2df14', '00a2df1f']]`
  - `CONDITIONAL_JUMP` [`00a2df1c`](#insn-00a2df1c) → [`00a2df14`](#insn-00a2df14)
  - `FALL_THROUGH` [`00a2df1c`](#insn-00a2df1c) → [`00a2df20`](#insn-00a2df20)
- ブロック [`00a2df20`](#insn-00a2df20) 範囲 `[['00a2df20', '00a2df23']]`
  - `UNCONDITIONAL_JUMP` [`00a2df20`](#insn-00a2df20) → [`00a2deb0`](#insn-00a2deb0)
- ブロック [`00a2df24`](#insn-00a2df24) 範囲 `[['00a2df24', '00a2df2f']]`
  - `CONDITIONAL_JUMP` [`00a2df2c`](#insn-00a2df2c) → [`00a2df00`](#insn-00a2df00)
  - `FALL_THROUGH` [`00a2df2c`](#insn-00a2df2c) → [`00a2df30`](#insn-00a2df30)
- ブロック [`00a2df30`](#insn-00a2df30) 範囲 `[['00a2df30', '00a2df4f']]`
  - `CONDITIONAL_JUMP` [`00a2df4c`](#insn-00a2df4c) → [`00a2df60`](#insn-00a2df60)
  - `FALL_THROUGH` [`00a2df4c`](#insn-00a2df4c) → [`00a2df50`](#insn-00a2df50)
- ブロック [`00a2df50`](#insn-00a2df50) 範囲 `[['00a2df50', '00a2df5b']]`
  - `CONDITIONAL_JUMP` [`00a2df58`](#insn-00a2df58) → [`00a2df50`](#insn-00a2df50)
  - `FALL_THROUGH` [`00a2df58`](#insn-00a2df58) → [`00a2df5c`](#insn-00a2df5c)
- ブロック [`00a2df5c`](#insn-00a2df5c) 範囲 `[['00a2df5c', '00a2df5f']]`
  - `UNCONDITIONAL_JUMP` [`00a2df5c`](#insn-00a2df5c) → [`00a2df24`](#insn-00a2df24)
- ブロック [`00a2df60`](#insn-00a2df60) 範囲 `[['00a2df60', '00a2df73']]`
  - `CONDITIONAL_JUMP` [`00a2df70`](#insn-00a2df70) → [`00a2df60`](#insn-00a2df60)
  - `FALL_THROUGH` [`00a2df70`](#insn-00a2df70) → [`00a2df74`](#insn-00a2df74)
- ブロック [`00a2df74`](#insn-00a2df74) 範囲 `[['00a2df74', '00a2df77']]`
  - `UNCONDITIONAL_JUMP` [`00a2df74`](#insn-00a2df74) → [`00a2df24`](#insn-00a2df24)
- ブロック [`00a2df78`](#insn-00a2df78) 範囲 `[['00a2df78', '00a2df8b']]`
  - `CONDITIONAL_JUMP` [`00a2df88`](#insn-00a2df88) → [`00a2df78`](#insn-00a2df78)
  - `FALL_THROUGH` [`00a2df88`](#insn-00a2df88) → [`00a2df8c`](#insn-00a2df8c)
- ブロック [`00a2df8c`](#insn-00a2df8c) 範囲 `[['00a2df8c', '00a2df8f']]`
  - `UNCONDITIONAL_JUMP` [`00a2df8c`](#insn-00a2df8c) → [`00a2deb0`](#insn-00a2deb0)
- ブロック [`00a2df90`](#insn-00a2df90) 範囲 `[['00a2df90', '00a2dfab']]`
  - `CONDITIONAL_JUMP` [`00a2dfa8`](#insn-00a2dfa8) → [`00a2dfe8`](#insn-00a2dfe8)
  - `FALL_THROUGH` [`00a2dfa8`](#insn-00a2dfa8) → [`00a2dfac`](#insn-00a2dfac)
- ブロック [`00a2dfac`](#insn-00a2dfac) 範囲 `[['00a2dfac', '00a2dfbb']]`
  - `CONDITIONAL_JUMP` [`00a2dfb8`](#insn-00a2dfb8) → [`00a2e060`](#insn-00a2e060)
  - `FALL_THROUGH` [`00a2dfb8`](#insn-00a2dfb8) → [`00a2dfbc`](#insn-00a2dfbc)
- ブロック [`00a2dfbc`](#insn-00a2dfbc) 範囲 `[['00a2dfbc', '00a2dfdb']]`
- ブロック [`00a2dfdc`](#insn-00a2dfdc) 範囲 `[['00a2dfdc', '00a2dfe7']]`
  - `CONDITIONAL_JUMP` [`00a2dfe4`](#insn-00a2dfe4) → [`00a2dfac`](#insn-00a2dfac)
  - `FALL_THROUGH` [`00a2dfe4`](#insn-00a2dfe4) → [`00a2dfe8`](#insn-00a2dfe8)
- ブロック [`00a2dfe8`](#insn-00a2dfe8) 範囲 `[['00a2dfe8', '00a2e007']]`
  - `CONDITIONAL_JUMP` [`00a2e004`](#insn-00a2e004) → [`00a2e018`](#insn-00a2e018)
  - `FALL_THROUGH` [`00a2e004`](#insn-00a2e004) → [`00a2e008`](#insn-00a2e008)
- ブロック [`00a2e008`](#insn-00a2e008) 範囲 `[['00a2e008', '00a2e013']]`
  - `CONDITIONAL_JUMP` [`00a2e010`](#insn-00a2e010) → [`00a2e008`](#insn-00a2e008)
  - `FALL_THROUGH` [`00a2e010`](#insn-00a2e010) → [`00a2e014`](#insn-00a2e014)
- ブロック [`00a2e014`](#insn-00a2e014) 範囲 `[['00a2e014', '00a2e017']]`
  - `UNCONDITIONAL_JUMP` [`00a2e014`](#insn-00a2e014) → [`00a2dfdc`](#insn-00a2dfdc)
- ブロック [`00a2e018`](#insn-00a2e018) 範囲 `[['00a2e018', '00a2e02b']]`
  - `CONDITIONAL_JUMP` [`00a2e028`](#insn-00a2e028) → [`00a2e018`](#insn-00a2e018)
  - `FALL_THROUGH` [`00a2e028`](#insn-00a2e028) → [`00a2e02c`](#insn-00a2e02c)
- ブロック [`00a2e02c`](#insn-00a2e02c) 範囲 `[['00a2e02c', '00a2e02f']]`
  - `UNCONDITIONAL_JUMP` [`00a2e02c`](#insn-00a2e02c) → [`00a2dfdc`](#insn-00a2dfdc)
- ブロック [`00a2e060`](#insn-00a2e060) 範囲 `[['00a2e060', '00a2e063']]`

## 命令位置別の参照

- [`00a2dde0`](#insn-00a2dde0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2dde4`](#insn-00a2dde4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2dde8`](#insn-00a2dde8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2ddec`](#insn-00a2ddec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2ddf0`](#insn-00a2ddf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2ddf4`](#insn-00a2ddf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2de0c`](#insn-00a2de0c) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2de1c`](#insn-00a2de1c) → [`00480b90`](../00480/00480b90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480b90` · 推定シンボル `None` · 推定型 `None`
- [`00a2de2c`](#insn-00a2de2c) → [`00a2de64`](#insn-00a2de64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2de38`](#insn-00a2de38) → [`00480b90`](../00480/00480b90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480b90` · 推定シンボル `None` · 推定型 `None`
- [`00a2de48`](#insn-00a2de48) → [`00a2df90`](#insn-00a2df90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2de54`](#insn-00a2de54) → [`00a2debc`](#insn-00a2debc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2de60`](#insn-00a2de60) → [`00a2de30`](#insn-00a2de30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2de70`](#insn-00a2de70) → [`00480b90`](../00480/00480b90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480b90` · 推定シンボル `None` · 推定型 `None`
- [`00a2de7c`](#insn-00a2de7c) → [`00480d48`](../00480/00480d48.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480d48` · 推定シンボル `None` · 推定型 `None`
- [`00a2de84`](#insn-00a2de84) → [`00a2de98`](#insn-00a2de98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2de90`](#insn-00a2de90) → [`00a2de88`](#insn-00a2de88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2de94`](#insn-00a2de94) → [`00a2de58`](#insn-00a2de58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2dea8`](#insn-00a2dea8) → [`00a2de98`](#insn-00a2de98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2deac`](#insn-00a2deac) → [`00a2de58`](#insn-00a2de58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2deb8`](#insn-00a2deb8) → [`00a2df90`](#insn-00a2df90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2dec4`](#insn-00a2dec4) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2dec8`](#insn-00a2dec8) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2decc`](#insn-00a2decc) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2ded8`](#insn-00a2ded8) → [`00691800`](../00691/00691800.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00691800` · 推定シンボル `None` · 推定型 `None`
- [`00a2dedc`](#insn-00a2dedc) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2dee4`](#insn-00a2dee4) → [`00480b90`](../00480/00480b90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480b90` · 推定シンボル `None` · 推定型 `None`
- [`00a2dee8`](#insn-00a2dee8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2def0`](#insn-00a2def0) → [`00480b90`](../00480/00480b90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480b90` · 推定シンボル `None` · 推定型 `None`
- [`00a2def4`](#insn-00a2def4) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2defc`](#insn-00a2defc) → [`00a2df30`](#insn-00a2df30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2df00`](#insn-00a2df00) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2df08`](#insn-00a2df08) → [`005c179c`](../005c1/005c179c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c179c` · 推定シンボル `None` · 推定型 `None`
- [`00a2df10`](#insn-00a2df10) → [`00a2df78`](#insn-00a2df78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2df1c`](#insn-00a2df1c) → [`00a2df14`](#insn-00a2df14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2df20`](#insn-00a2df20) → [`00a2deb0`](#insn-00a2deb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2df2c`](#insn-00a2df2c) → [`00a2df00`](#insn-00a2df00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2df30`](#insn-00a2df30) → `Stack[-0x5c]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2df38`](#insn-00a2df38) → [`00480b90`](../00480/00480b90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480b90` · 推定シンボル `None` · 推定型 `None`
- [`00a2df44`](#insn-00a2df44) → [`00480b90`](../00480/00480b90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480b90` · 推定シンボル `None` · 推定型 `None`
- [`00a2df48`](#insn-00a2df48) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2df4c`](#insn-00a2df4c) → [`00a2df60`](#insn-00a2df60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2df58`](#insn-00a2df58) → [`00a2df50`](#insn-00a2df50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2df5c`](#insn-00a2df5c) → [`00a2df24`](#insn-00a2df24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2df60`](#insn-00a2df60) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2df70`](#insn-00a2df70) → [`00a2df60`](#insn-00a2df60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2df74`](#insn-00a2df74) → [`00a2df24`](#insn-00a2df24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2df88`](#insn-00a2df88) → [`00a2df78`](#insn-00a2df78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2df8c`](#insn-00a2df8c) → [`00a2deb0`](#insn-00a2deb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2df98`](#insn-00a2df98) → [`00480b90`](../00480/00480b90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480b90` · 推定シンボル `None` · 推定型 `None`
- [`00a2dfa8`](#insn-00a2dfa8) → [`00a2dfe8`](#insn-00a2dfe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2dfb0`](#insn-00a2dfb0) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2dfb8`](#insn-00a2dfb8) → [`00a2e060`](#insn-00a2e060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2dfbc`](#insn-00a2dfbc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2dfc0`](#insn-00a2dfc0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2dfc4`](#insn-00a2dfc4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2dfc8`](#insn-00a2dfc8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2dfcc`](#insn-00a2dfcc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2dfd0`](#insn-00a2dfd0) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2dfe4`](#insn-00a2dfe4) → [`00a2dfac`](#insn-00a2dfac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2dff0`](#insn-00a2dff0) → [`00480b90`](../00480/00480b90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480b90` · 推定シンボル `None` · 推定型 `None`
- [`00a2dffc`](#insn-00a2dffc) → [`00480e28`](../00480/00480e28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480e28` · 推定シンボル `None` · 推定型 `None`
- [`00a2e004`](#insn-00a2e004) → [`00a2e018`](#insn-00a2e018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2e010`](#insn-00a2e010) → [`00a2e008`](#insn-00a2e008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2e014`](#insn-00a2e014) → [`00a2dfdc`](#insn-00a2dfdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2e028`](#insn-00a2e028) → [`00a2e018`](#insn-00a2e018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2e02c`](#insn-00a2e02c) → [`00a2dfdc`](#insn-00a2dfdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2e060`](#insn-00a2e060) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a2dde0`](#insn-00a2dde0)

~~~json
{
  "source": "00a2dde0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2dde4`](#insn-00a2dde4)

~~~json
{
  "source": "00a2dde4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2dde8`](#insn-00a2dde8)

~~~json
{
  "source": "00a2dde8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2ddec`](#insn-00a2ddec)

~~~json
{
  "source": "00a2ddec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2ddf0`](#insn-00a2ddf0)

~~~json
{
  "source": "00a2ddf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2ddf4`](#insn-00a2ddf4)

~~~json
{
  "source": "00a2ddf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2de0c`](#insn-00a2de0c)

~~~json
{
  "source": "00a2de0c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2de1c`](#insn-00a2de1c)

~~~json
{
  "source": "00a2de1c",
  "target": "00480b90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a2de2c`](#insn-00a2de2c)

~~~json
{
  "source": "00a2de2c",
  "target": "00a2de64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2de38`](#insn-00a2de38)

~~~json
{
  "source": "00a2de38",
  "target": "00480b90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a2de48`](#insn-00a2de48)

~~~json
{
  "source": "00a2de48",
  "target": "00a2df90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2de54`](#insn-00a2de54)

~~~json
{
  "source": "00a2de54",
  "target": "00a2debc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2de60`](#insn-00a2de60)

~~~json
{
  "source": "00a2de60",
  "target": "00a2de30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2de70`](#insn-00a2de70)

~~~json
{
  "source": "00a2de70",
  "target": "00480b90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a2de7c`](#insn-00a2de7c)

~~~json
{
  "source": "00a2de7c",
  "target": "00480d48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a2de84`](#insn-00a2de84)

~~~json
{
  "source": "00a2de84",
  "target": "00a2de98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2de90`](#insn-00a2de90)

~~~json
{
  "source": "00a2de90",
  "target": "00a2de88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2de94`](#insn-00a2de94)

~~~json
{
  "source": "00a2de94",
  "target": "00a2de58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2dea8`](#insn-00a2dea8)

~~~json
{
  "source": "00a2dea8",
  "target": "00a2de98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2deac`](#insn-00a2deac)

~~~json
{
  "source": "00a2deac",
  "target": "00a2de58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2deb8`](#insn-00a2deb8)

~~~json
{
  "source": "00a2deb8",
  "target": "00a2df90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2dec4`](#insn-00a2dec4)

~~~json
{
  "source": "00a2dec4",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2dec8`](#insn-00a2dec8)

~~~json
{
  "source": "00a2dec8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2decc`](#insn-00a2decc)

~~~json
{
  "source": "00a2decc",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2ded8`](#insn-00a2ded8)

~~~json
{
  "source": "00a2ded8",
  "target": "00691800",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a2dedc`](#insn-00a2dedc)

~~~json
{
  "source": "00a2dedc",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2dee4`](#insn-00a2dee4)

~~~json
{
  "source": "00a2dee4",
  "target": "00480b90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a2dee8`](#insn-00a2dee8)

~~~json
{
  "source": "00a2dee8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2def0`](#insn-00a2def0)

~~~json
{
  "source": "00a2def0",
  "target": "00480b90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a2def4`](#insn-00a2def4)

~~~json
{
  "source": "00a2def4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2defc`](#insn-00a2defc)

~~~json
{
  "source": "00a2defc",
  "target": "00a2df30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2df00`](#insn-00a2df00)

~~~json
{
  "source": "00a2df00",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2df08`](#insn-00a2df08)

~~~json
{
  "source": "00a2df08",
  "target": "005c179c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a2df10`](#insn-00a2df10)

~~~json
{
  "source": "00a2df10",
  "target": "00a2df78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2df1c`](#insn-00a2df1c)

~~~json
{
  "source": "00a2df1c",
  "target": "00a2df14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2df20`](#insn-00a2df20)

~~~json
{
  "source": "00a2df20",
  "target": "00a2deb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2df2c`](#insn-00a2df2c)

~~~json
{
  "source": "00a2df2c",
  "target": "00a2df00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2df30`](#insn-00a2df30)

~~~json
{
  "source": "00a2df30",
  "target": "Stack[-0x5c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2df38`](#insn-00a2df38)

~~~json
{
  "source": "00a2df38",
  "target": "00480b90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a2df44`](#insn-00a2df44)

~~~json
{
  "source": "00a2df44",
  "target": "00480b90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a2df48`](#insn-00a2df48)

~~~json
{
  "source": "00a2df48",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2df4c`](#insn-00a2df4c)

~~~json
{
  "source": "00a2df4c",
  "target": "00a2df60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2df58`](#insn-00a2df58)

~~~json
{
  "source": "00a2df58",
  "target": "00a2df50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2df5c`](#insn-00a2df5c)

~~~json
{
  "source": "00a2df5c",
  "target": "00a2df24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2df60`](#insn-00a2df60)

~~~json
{
  "source": "00a2df60",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2df70`](#insn-00a2df70)

~~~json
{
  "source": "00a2df70",
  "target": "00a2df60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2df74`](#insn-00a2df74)

~~~json
{
  "source": "00a2df74",
  "target": "00a2df24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2df88`](#insn-00a2df88)

~~~json
{
  "source": "00a2df88",
  "target": "00a2df78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2df8c`](#insn-00a2df8c)

~~~json
{
  "source": "00a2df8c",
  "target": "00a2deb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2df98`](#insn-00a2df98)

~~~json
{
  "source": "00a2df98",
  "target": "00480b90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a2dfa8`](#insn-00a2dfa8)

~~~json
{
  "source": "00a2dfa8",
  "target": "00a2dfe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2dfb0`](#insn-00a2dfb0)

~~~json
{
  "source": "00a2dfb0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2dfb8`](#insn-00a2dfb8)

~~~json
{
  "source": "00a2dfb8",
  "target": "00a2e060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2dfbc`](#insn-00a2dfbc)

~~~json
{
  "source": "00a2dfbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2dfc0`](#insn-00a2dfc0)

~~~json
{
  "source": "00a2dfc0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2dfc4`](#insn-00a2dfc4)

~~~json
{
  "source": "00a2dfc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2dfc8`](#insn-00a2dfc8)

~~~json
{
  "source": "00a2dfc8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2dfcc`](#insn-00a2dfcc)

~~~json
{
  "source": "00a2dfcc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2dfd0`](#insn-00a2dfd0)

~~~json
{
  "source": "00a2dfd0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2dfe4`](#insn-00a2dfe4)

~~~json
{
  "source": "00a2dfe4",
  "target": "00a2dfac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2dff0`](#insn-00a2dff0)

~~~json
{
  "source": "00a2dff0",
  "target": "00480b90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a2dffc`](#insn-00a2dffc)

~~~json
{
  "source": "00a2dffc",
  "target": "00480e28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a2e004`](#insn-00a2e004)

~~~json
{
  "source": "00a2e004",
  "target": "00a2e018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2e010`](#insn-00a2e010)

~~~json
{
  "source": "00a2e010",
  "target": "00a2e008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2e014`](#insn-00a2e014)

~~~json
{
  "source": "00a2e014",
  "target": "00a2dfdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2e028`](#insn-00a2e028)

~~~json
{
  "source": "00a2e028",
  "target": "00a2e018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2e02c`](#insn-00a2e02c)

~~~json
{
  "source": "00a2e02c",
  "target": "00a2dfdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2e060`](#insn-00a2e060)

~~~json
{
  "source": "00a2e060",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
