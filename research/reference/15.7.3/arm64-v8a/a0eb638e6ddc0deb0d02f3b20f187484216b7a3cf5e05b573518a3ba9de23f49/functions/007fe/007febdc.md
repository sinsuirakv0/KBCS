# 007febdc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `007febdc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007fe/007febdc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/machine_only_observed-0028.md#compare-8be07645f483a68967e0bcf5a6e803e7)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `007febdc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007fe/007febdc.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/machine_only_observed-0029.md#compare-c1d01f9117392665766718706eb66b97)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007febdc",
  "name": "FUN_007febdc",
  "size": 1340,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "036611e95b71880673fe547c6943b948ec2c12b47546f7560f4038846f60c292",
  "source_text_sha256": "036611e95b71880673fe547c6943b948ec2c12b47546f7560f4038846f60c292",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007febdc",
        "007ff117"
      ]
    ],
    "bytes_sha256": "e9ee51ca5b55118d51286550703ecf9c5f0d7ef9f6387ca5121f2ec75adb2be2",
    "instruction_count": 335,
    "instruction_bytes": 1340,
    "body_bytes": 1340,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [007fe2f0](../007fe/007fe2f0.md)
- [007febdc](../007fe/007febdc.md)

## 呼び出し先

- [007fc484](../007fc/007fc484.md)
- [007fe674](../007fe/007fe674.md)
- [007febdc](../007fe/007febdc.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb0a0](../00bdb/00bdb0a0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 9896 bytes

~~~c

void FUN_007febdc(undefined8 *param_1,undefined8 *param_2,undefined8 *param_3,undefined8 *param_4,
                 long param_5,long param_6,undefined8 *param_7,long param_8)

{
  long lVar1;
  long lVar2;
  bool bVar3;
  ulong uVar4;
  ulong uVar5;
  ulong uVar6;
  undefined1 uVar7;
  long lVar8;
  long lVar9;
  undefined8 *puVar10;
  undefined8 *puVar11;
  undefined8 *puVar12;
  long lVar13;
  undefined8 *puVar14;
  undefined8 *puVar15;
  ulong uVar16;
  undefined8 uVar17;
  undefined8 uVar18;
  undefined8 *local_110;
  long local_100;
  undefined8 local_f8;
  undefined8 local_f0;
  undefined8 uStack_e8;
  undefined4 local_e0;
  undefined8 local_d0;
  undefined8 uStack_c8;
  undefined4 local_c0;
  undefined8 local_b0;
  undefined8 uStack_a8;
  undefined4 local_a0;
  undefined8 local_90;
  undefined8 uStack_88;
  undefined4 local_80;
  long local_70;
  
  lVar2 = tpidr_el0;
  local_70 = *(long *)(lVar2 + 0x28);
  local_110 = param_3;
  local_100 = param_6;
  if (param_6 != 0) {
    while ((param_8 < local_100 && (param_8 < param_5))) {
      if (param_5 == 0) goto LAB_007ff0e4;
      lVar9 = 0;
      lVar13 = -param_5;
      while( true ) {
        uStack_c8 = param_2[1];
        local_d0 = *param_2;
        local_c0 = *(undefined4 *)(param_2 + 2);
        puVar11 = (undefined8 *)((long)param_1 + lVar9);
        uStack_e8 = puVar11[1];
        local_f0 = *puVar11;
        local_e0 = *(undefined4 *)(puVar11 + 2);
        uVar4 = FUN_007fe674(param_4,&local_d0,&local_f0);
        if ((uVar4 & 1) != 0) break;
        bVar3 = lVar13 == -1;
        lVar13 = lVar13 + 1;
        lVar9 = lVar9 + 0x14;
        if (bVar3) goto LAB_007ff0e4;
      }
      param_5 = -lVar13;
      if (param_5 < local_100) {
        lVar8 = local_100;
        if (local_100 < 0) {
          lVar8 = local_100 + 1;
        }
        lVar8 = lVar8 >> 1;
        puVar15 = (undefined8 *)((long)param_2 + lVar8 * 0x14);
        lVar1 = (long)param_2 + (-lVar9 - (long)param_1);
        puVar10 = param_2;
        if (lVar1 != 0) {
          uVar4 = (lVar1 >> 2) * -0x3333333333333333;
          puVar10 = puVar11;
          do {
            uVar16 = uVar4 >> 1;
            uStack_88 = puVar15[1];
            local_90 = *puVar15;
            local_80 = *(undefined4 *)(puVar15 + 2);
            puVar12 = (undefined8 *)((long)puVar10 + uVar16 * 0x14);
            uStack_a8 = puVar12[1];
            local_b0 = *puVar12;
            local_a0 = *(undefined4 *)(puVar12 + 2);
            uVar5 = FUN_007fe674(param_4,&local_90,&local_b0);
            uVar6 = uVar4 + ~uVar16;
            uVar4 = uVar16;
            if ((uVar5 & 1) == 0) {
              uVar4 = uVar6;
              puVar10 = (undefined8 *)((long)puVar12 + 0x14);
            }
          } while (uVar4 != 0);
        }
        param_5 = ((long)puVar10 + (-lVar9 - (long)param_1) >> 2) * -0x3333333333333333;
      }
      else {
        if (lVar13 == -1) {
          param_1 = (undefined8 *)((long)param_1 + lVar9);
          uVar18 = param_2[1];
          uVar17 = *param_2;
          local_80 = *(undefined4 *)(param_1 + 2);
          uStack_88 = param_1[1];
          local_90 = *param_1;
                    /* try { // try from 007ff078 to 008ff083 has its CatchHandler @ 007ff7e0 */
          *(undefined1 *)(param_1 + 2) = *(undefined1 *)(param_2 + 2);
          param_1[1] = uVar18;
          *param_1 = uVar17;
          param_2[1] = uStack_88;
          *param_2 = local_90;
          *(undefined1 *)(param_2 + 2) = (undefined1)local_80;
          goto LAB_007ff0e4;
        }
        if (param_5 < 0) {
          param_5 = param_5 + 1;
        }
        param_5 = param_5 >> 1;
        local_f8 = *param_4;
        puVar10 = (undefined8 *)((long)param_1 + lVar9 + param_5 * 0x14);
        puVar15 = param_2;
        if (param_2 != local_110) {
          uVar4 = ((long)local_110 - (long)param_2 >> 2) * -0x3333333333333333;
          do {
            uVar5 = uVar4 >> 1;
            puVar12 = (undefined8 *)((long)puVar15 + uVar5 * 0x14);
            local_80 = *(undefined4 *)(puVar12 + 2);
            uStack_88 = puVar12[1];
            local_90 = *puVar12;
            local_a0 = *(undefined4 *)(puVar10 + 2);
            uStack_a8 = puVar10[1];
            local_b0 = *puVar10;
            uVar6 = FUN_007fe674(&local_f8,&local_90,&local_b0);
            uVar4 = uVar4 + ~uVar5;
            puVar12 = (undefined8 *)((long)puVar12 + 0x14);
            if ((uVar6 & 1) == 0) {
              uVar4 = uVar5;
              puVar12 = puVar15;
            }
            puVar15 = puVar12;
          } while (uVar4 != 0);
        }
        lVar8 = ((long)puVar15 - (long)param_2 >> 2) * -0x3333333333333333;
      }
      puVar12 = (undefined8 *)FUN_007fc484(puVar10,param_2,puVar15);
      if (param_5 + lVar8 < (local_100 - (param_5 + lVar8)) - lVar13) {
        FUN_007febdc((long)param_1 + lVar9,puVar10,puVar12,param_4,param_5,lVar8,param_7,param_8);
        puVar10 = puVar15;
        puVar11 = puVar12;
        lVar8 = local_100 - lVar8;
        param_5 = -lVar13 - param_5;
      }
      else {
        FUN_007febdc(puVar12,puVar15,local_110,param_4,-lVar13 - param_5,local_100 - lVar8,param_7,
                     param_8);
        local_110 = puVar12;
      }
      param_2 = puVar10;
      param_1 = puVar11;
      local_100 = lVar8;
      if (lVar8 == 0) goto LAB_007ff0e4;
    }
    if (local_100 < param_5) {
      if (local_110 != param_2) {
        lVar13 = 0;
        do {
          puVar11 = (undefined8 *)((long)param_2 + lVar13);
          puVar10 = (undefined8 *)((long)param_7 + lVar13);
          lVar13 = lVar13 + 0x14;
          uVar18 = puVar11[1];
          uVar17 = *puVar11;
          *(undefined4 *)(puVar10 + 2) = *(undefined4 *)(puVar11 + 2);
          puVar10[1] = uVar18;
          *puVar10 = uVar17;
        } while ((undefined8 *)((long)param_2 + lVar13) != local_110);
        puVar11 = (undefined8 *)((long)param_7 + lVar13);
        while (puVar10 = (undefined8 *)((long)local_110 + -0x14), param_2 != param_1) {
          local_80 = *(undefined4 *)((long)puVar11 + -4);
          uStack_88 = *(undefined8 *)((long)puVar11 + -0xc);
          local_90 = *(undefined8 *)((long)puVar11 + -0x14);
          puVar14 = (undefined8 *)((long)puVar11 + -0x14);
          local_a0 = *(undefined4 *)((long)param_2 + -4);
          uStack_a8 = *(undefined8 *)((long)param_2 + -0xc);
          local_b0 = *(undefined8 *)((long)param_2 + -0x14);
          uVar4 = FUN_007fe674(param_4,&local_90,&local_b0);
          puVar15 = (undefined8 *)((long)param_2 + -0x14);
          puVar12 = (undefined8 *)((long)param_2 + -0x14);
          if ((uVar4 & 1) == 0) {
            puVar15 = param_2;
            puVar11 = puVar14;
            puVar12 = puVar14;
          }
          uVar18 = puVar12[1];
          uVar17 = *puVar12;
          *(undefined1 *)((long)local_110 + -4) = *(undefined1 *)(puVar12 + 2);
          *(undefined8 *)((long)local_110 + -0xc) = uVar18;
          *puVar10 = uVar17;
          param_2 = puVar15;
          local_110 = puVar10;
          if (puVar11 == param_7) goto LAB_007ff0e4;
        }
        lVar13 = 0;
        do {
          puVar15 = (undefined8 *)((long)puVar10 + lVar13);
          lVar9 = lVar13 + -0x14;
          uVar18 = *(undefined8 *)((long)puVar11 + lVar13 + -0xc);
          uVar17 = *(undefined8 *)((long)puVar11 + lVar13 + -0x14);
          *(undefined1 *)(puVar15 + 2) = *(undefined1 *)((long)puVar11 + lVar13 + -4);
          puVar15[1] = uVar18;
          *puVar15 = uVar17;
          lVar13 = lVar9;
        } while ((undefined8 *)((long)puVar11 + lVar9) != param_7);
      }
      goto LAB_007ff0e4;
    }
    if (param_1 == param_2) goto LAB_007ff0e4;
                    /* catch() { ... } // from try @ 007ff140 with catch @ 007fefc8
                       catch() { ... } // from try @ 007ff500 with catch @ 007fefc8
                       catch() { ... } // from try @ 007ff6e4 with catch @ 007fefc8 */
    lVar13 = 0;
    do {
      puVar11 = (undefined8 *)((long)param_1 + lVar13);
      puVar10 = (undefined8 *)((long)param_7 + lVar13);
      lVar13 = lVar13 + 0x14;
      uVar18 = puVar11[1];
      uVar17 = *puVar11;
      *(undefined4 *)(puVar10 + 2) = *(undefined4 *)(puVar11 + 2);
      puVar10[1] = uVar18;
      *puVar10 = uVar17;
    } while ((undefined8 *)((long)param_1 + lVar13) != param_2);
    puVar11 = param_7;
    do {
      if (param_2 == local_110) {
                    /* try { // try from 007ff0dc to 008ff13f has its CatchHandler @ 007ff7f8 */
        memmove(param_1,puVar11,(long)param_7 + (lVar13 - (long)puVar11) + -3);
        break;
      }
      local_80 = *(undefined4 *)(param_2 + 2);
      uStack_88 = param_2[1];
      local_90 = *param_2;
                    /* try { // try from 007ff030 to 008ff033 has its CatchHandler @ 007ff7e4 */
                    /* try { // try from 007ff03c to 008ff077 has its CatchHandler @ 007ff7f0 */
      local_a0 = *(undefined4 *)(puVar11 + 2);
      uStack_a8 = puVar11[1];
      local_b0 = *puVar11;
      uVar4 = FUN_007fe674(param_4,&local_90,&local_b0);
      if ((uVar4 & 1) == 0) {
        uVar7 = *(undefined1 *)(puVar11 + 2);
        puVar10 = (undefined8 *)((long)puVar11 + 0x14);
        uVar18 = puVar11[1];
        uVar17 = *puVar11;
      }
      else {
        uVar7 = *(undefined1 *)(param_2 + 2);
        uVar18 = param_2[1];
        uVar17 = *param_2;
        puVar10 = puVar11;
        param_2 = (undefined8 *)((long)param_2 + 0x14);
      }
      *(undefined1 *)(param_1 + 2) = uVar7;
      param_1[1] = uVar18;
      *param_1 = uVar17;
      param_1 = (undefined8 *)((long)param_1 + 0x14);
      puVar11 = puVar10;
    } while ((undefined8 *)((long)param_7 + lVar13) != puVar10);
  }
LAB_007ff0e4:
  if (*(long *)(lVar2 + 0x28) == local_70) {
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
<a id="insn-007febdc"></a> `007febdc` | `ff 03 05 d1` | sub sp,sp,#0x140 | `FALL_THROUGH`
<a id="insn-007febe0"></a> `007febe0` | `fd 7b 0e a9` | stp x29,x30,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-007febe4"></a> `007febe4` | `fc 6f 0f a9` | stp x28,x27,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-007febe8"></a> `007febe8` | `fa 67 10 a9` | stp x26,x25,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-007febec"></a> `007febec` | `f8 5f 11 a9` | stp x24,x23,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-007febf0"></a> `007febf0` | `f6 57 12 a9` | stp x22,x21,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-007febf4"></a> `007febf4` | `f4 4f 13 a9` | stp x20,x19,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-007febf8"></a> `007febf8` | `fd 83 03 91` | add x29,sp,#0xe0 | `FALL_THROUGH`
<a id="insn-007febfc"></a> `007febfc` | `e2 1f 03 a9` | stp x2,x7,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007fec00"></a> `007fec00` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-007fec04"></a> `007fec04` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-007fec08"></a> `007fec08` | `a8 03 1f f8` | stur x8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-007fec0c"></a> `007fec0c` | `e5 23 00 f9` | str x5,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-007fec10"></a> `007fec10` | `a5 26 00 b4` | cbz x5,0x007ff0e4 | `CONDITIONAL_JUMP`
<a id="insn-007fec14"></a> `007fec14` | `fa 03 06 aa` | mov x26,x6 | `FALL_THROUGH`
<a id="insn-007fec18"></a> `007fec18` | `fc 03 04 aa` | mov x28,x4 | `FALL_THROUGH`
<a id="insn-007fec1c"></a> `007fec1c` | `fb 03 03 aa` | mov x27,x3 | `FALL_THROUGH`
<a id="insn-007fec20"></a> `007fec20` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-007fec24"></a> `007fec24` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-007fec28"></a> `007fec28` | `e8 a7 43 a9` | ldp x8,x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-007fec2c"></a> `007fec2c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-007fec30"></a> `007fec30` | `ad 16 00 54` | b.le 0x007fef04 | `CONDITIONAL_JUMP`
<a id="insn-007fec34"></a> `007fec34` | `9f 03 08 eb` | cmp x28,x8 | `FALL_THROUGH`
<a id="insn-007fec38"></a> `007fec38` | `6d 16 00 54` | b.le 0x007fef04 | `CONDITIONAL_JUMP`
<a id="insn-007fec3c"></a> `007fec3c` | `5c 25 00 b4` | cbz x28,0x007ff0e4 | `CONDITIONAL_JUMP`
<a id="insn-007fec40"></a> `007fec40` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-007fec44"></a> `007fec44` | `f8 03 1c cb` | neg x24,x28 | `FALL_THROUGH`
<a id="insn-007fec48"></a> `007fec48` | `a0 02 c0 3d` | ldr q0,[x21] | `FALL_THROUGH`
<a id="insn-007fec4c"></a> `007fec4c` | `a8 12 40 b9` | ldr w8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-007fec50"></a> `007fec50` | `f6 02 13 8b` | add x22,x23,x19 | `FALL_THROUGH`
<a id="insn-007fec54"></a> `007fec54` | `e1 c3 01 91` | add x1,sp,#0x70 | `FALL_THROUGH`
<a id="insn-007fec58"></a> `007fec58` | `e2 43 01 91` | add x2,sp,#0x50 | `FALL_THROUGH`
<a id="insn-007fec5c"></a> `007fec5c` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-007fec60"></a> `007fec60` | `e0 1f 80 3d` | str q0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-007fec64"></a> `007fec64` | `e8 83 00 b9` | str w8,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-007fec68"></a> `007fec68` | `c0 02 c0 3d` | ldr q0,[x22] | `FALL_THROUGH`
<a id="insn-007fec6c"></a> `007fec6c` | `c8 12 40 b9` | ldr w8,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-007fec70"></a> `007fec70` | `e0 17 80 3d` | str q0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007fec74"></a> `007fec74` | `e8 63 00 b9` | str w8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-007fec78"></a> `007fec78` | `7f fe ff 97` | bl 0x007fe674 | `UNCONDITIONAL_CALL`
<a id="insn-007fec7c"></a> `007fec7c` | `a0 00 00 37` | tbnz w0,#0x0,0x007fec90 | `CONDITIONAL_JUMP`
<a id="insn-007fec80"></a> `007fec80` | `18 07 00 b1` | adds x24,x24,#0x1 | `FALL_THROUGH`
<a id="insn-007fec84"></a> `007fec84` | `73 52 00 91` | add x19,x19,#0x14 | `FALL_THROUGH`
<a id="insn-007fec88"></a> `007fec88` | `03 fe ff 54` | b.cc 0x007fec48 | `CONDITIONAL_JUMP`
<a id="insn-007fec8c"></a> `007fec8c` | `16 01 00 14` | b 0x007ff0e4 | `UNCONDITIONAL_JUMP`
<a id="insn-007fec90"></a> `007fec90` | `eb 23 40 f9` | ldr x11,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-007fec94"></a> `007fec94` | `e8 03 18 cb` | neg x8,x24 | `FALL_THROUGH`
<a id="insn-007fec98"></a> `007fec98` | `89 02 80 52` | mov w9,#0x14 | `FALL_THROUGH`
<a id="insn-007fec9c"></a> `007fec9c` | `fa d3 01 a9` | stp x26,x20,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-007feca0"></a> `007feca0` | `1f 01 0b eb` | cmp x8,x11 | `FALL_THROUGH`
<a id="insn-007feca4"></a> `007feca4` | `fb 17 00 f9` | str x27,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-007feca8"></a> `007feca8` | `2a 06 00 54` | b.ge 0x007fed6c | `CONDITIONAL_JUMP`
<a id="insn-007fecac"></a> `007fecac` | `7f 01 00 f1` | cmp x11,#0x0 | `FALL_THROUGH`
<a id="insn-007fecb0"></a> `007fecb0` | `fb 03 15 aa` | mov x27,x21 | `FALL_THROUGH`
<a id="insn-007fecb4"></a> `007fecb4` | `68 a5 8b 9a` | cinc x8,x11,lt | `FALL_THROUGH`
<a id="insn-007fecb8"></a> `007fecb8` | `08 fd 41 93` | asr x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-007fecbc"></a> `007fecbc` | `1a 55 09 9b` | madd x26,x8,x9,x21 | `FALL_THROUGH`
<a id="insn-007fecc0"></a> `007fecc0` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fecc4"></a> `007fecc4` | `a8 02 17 cb` | sub x8,x21,x23 | `FALL_THROUGH`
<a id="insn-007fecc8"></a> `007fecc8` | `08 01 13 eb` | subs x8,x8,x19 | `FALL_THROUGH`
<a id="insn-007feccc"></a> `007feccc` | `00 04 00 54` | b.eq 0x007fed4c | `CONDITIONAL_JUMP`
<a id="insn-007fecd0"></a> `007fecd0` | `08 fd 42 93` | asr x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-007fecd4"></a> `007fecd4` | `ea e7 02 b2` | orr x10,xzr,#-0x3333333333333334 | `FALL_THROUGH`
<a id="insn-007fecd8"></a> `007fecd8` | `f7 07 00 f9` | str x23,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-007fecdc"></a> `007fecdc` | `aa 99 99 f2` | movk x10,#0xcccd | `FALL_THROUGH`
<a id="insn-007fece0"></a> `007fece0` | `f7 17 40 f9` | ldr x23,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-007fece4"></a> `007fece4` | `fb 03 16 aa` | mov x27,x22 | `FALL_THROUGH`
<a id="insn-007fece8"></a> `007fece8` | `19 7d 0a 9b` | mul x25,x8,x10 | `FALL_THROUGH`
<a id="insn-007fecec"></a> `007fecec` | `3c ff 41 d3` | lsr x28,x25,#0x1 | `FALL_THROUGH`
<a id="insn-007fecf0"></a> `007fecf0` | `40 03 c0 3d` | ldr q0,[x26] | `FALL_THROUGH`
<a id="insn-007fecf4"></a> `007fecf4` | `48 13 40 b9` | ldr w8,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-007fecf8"></a> `007fecf8` | `a1 c3 00 d1` | sub x1,x29,#0x30 | `FALL_THROUGH`
<a id="insn-007fecfc"></a> `007fecfc` | `a2 43 01 d1` | sub x2,x29,#0x50 | `FALL_THROUGH`
<a id="insn-007fed00"></a> `007fed00` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-007fed04"></a> `007fed04` | `94 6f 09 9b` | madd x20,x28,x9,x27 | `FALL_THROUGH`
<a id="insn-007fed08"></a> `007fed08` | `a0 03 9d 3c` | stur q0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-007fed0c"></a> `007fed0c` | `a8 03 1e b8` | stur w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-007fed10"></a> `007fed10` | `80 02 c0 3d` | ldr q0,[x20] | `FALL_THROUGH`
<a id="insn-007fed14"></a> `007fed14` | `88 12 40 b9` | ldr w8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-007fed18"></a> `007fed18` | `a0 03 9b 3c` | stur q0,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-007fed1c"></a> `007fed1c` | `a8 03 1c b8` | stur w8,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-007fed20"></a> `007fed20` | `55 fe ff 97` | bl 0x007fe674 | `UNCONDITIONAL_CALL`
<a id="insn-007fed24"></a> `007fed24` | `e8 03 3c aa` | mvn x8,x28 | `FALL_THROUGH`
<a id="insn-007fed28"></a> `007fed28` | `1f 00 00 72` | tst w0,#0x1 | `FALL_THROUGH`
<a id="insn-007fed2c"></a> `007fed2c` | `89 52 00 91` | add x9,x20,#0x14 | `FALL_THROUGH`
<a id="insn-007fed30"></a> `007fed30` | `28 03 08 8b` | add x8,x25,x8 | `FALL_THROUGH`
<a id="insn-007fed34"></a> `007fed34` | `7b 13 89 9a` | csel x27,x27,x9,ne | `FALL_THROUGH`
<a id="insn-007fed38"></a> `007fed38` | `89 02 80 52` | mov w9,#0x14 | `FALL_THROUGH`
<a id="insn-007fed3c"></a> `007fed3c` | `99 13 88 9a` | csel x25,x28,x8,ne | `FALL_THROUGH`
<a id="insn-007fed40"></a> `007fed40` | `79 fd ff b5` | cbnz x25,0x007fecec | `CONDITIONAL_JUMP`
<a id="insn-007fed44"></a> `007fed44` | `f7 07 40 f9` | ldr x23,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-007fed48"></a> `007fed48` | `eb 23 40 f9` | ldr x11,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-007fed4c"></a> `007fed4c` | `68 03 17 cb` | sub x8,x27,x23 | `FALL_THROUGH`
<a id="insn-007fed50"></a> `007fed50` | `e9 e7 02 b2` | orr x9,xzr,#-0x3333333333333334 | `FALL_THROUGH`
<a id="insn-007fed54"></a> `007fed54` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fed58"></a> `007fed58` | `08 01 13 cb` | sub x8,x8,x19 | `FALL_THROUGH`
<a id="insn-007fed5c"></a> `007fed5c` | `a9 99 99 f2` | movk x9,#0xcccd | `FALL_THROUGH`
<a id="insn-007fed60"></a> `007fed60` | `08 fd 42 93` | asr x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-007fed64"></a> `007fed64` | `0c 7d 09 9b` | mul x12,x8,x9 | `FALL_THROUGH`
<a id="insn-007fed68"></a> `007fed68` | `33 00 00 14` | b 0x007fee34 | `UNCONDITIONAL_JUMP`
<a id="insn-007fed6c"></a> `007fed6c` | `1f 07 00 b1` | cmn x24,#0x1 | `FALL_THROUGH`
<a id="insn-007fed70"></a> `007fed70` | `a0 17 00 54` | b.eq 0x007ff064 | `CONDITIONAL_JUMP`
<a id="insn-007fed74"></a> `007fed74` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-007fed78"></a> `007fed78` | `ea 1b 40 f9` | ldr x10,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007fed7c"></a> `007fed7c` | `fa 03 15 aa` | mov x26,x21 | `FALL_THROUGH`
<a id="insn-007fed80"></a> `007fed80` | `08 a5 88 9a` | cinc x8,x8,lt | `FALL_THROUGH`
<a id="insn-007fed84"></a> `007fed84` | `0c fd 41 93` | asr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-007fed88"></a> `007fed88` | `bf 02 0a eb` | cmp x21,x10 | `FALL_THROUGH`
<a id="insn-007fed8c"></a> `007fed8c` | `88 5d 09 9b` | madd x8,x12,x9,x23 | `FALL_THROUGH`
<a id="insn-007fed90"></a> `007fed90` | `69 03 40 f9` | ldr x9,[x27] | `FALL_THROUGH`
<a id="insn-007fed94"></a> `007fed94` | `e9 27 00 f9` | str x9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-007fed98"></a> `007fed98` | `1b 01 13 8b` | add x27,x8,x19 | `FALL_THROUGH`
<a id="insn-007fed9c"></a> `007fed9c` | `20 04 00 54` | b.eq 0x007fee20 | `CONDITIONAL_JUMP`
<a id="insn-007feda0"></a> `007feda0` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007feda4"></a> `007feda4` | `e9 e7 02 b2` | orr x9,xzr,#-0x3333333333333334 | `FALL_THROUGH`
<a id="insn-007feda8"></a> `007feda8` | `fa 03 15 aa` | mov x26,x21 | `FALL_THROUGH`
<a id="insn-007fedac"></a> `007fedac` | `a9 99 99 f2` | movk x9,#0xcccd | `FALL_THROUGH`
<a id="insn-007fedb0"></a> `007fedb0` | `ec 0b 00 f9` | str x12,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fedb4"></a> `007fedb4` | `08 01 15 cb` | sub x8,x8,x21 | `FALL_THROUGH`
<a id="insn-007fedb8"></a> `007fedb8` | `08 fd 42 93` | asr x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-007fedbc"></a> `007fedbc` | `19 7d 09 9b` | mul x25,x8,x9 | `FALL_THROUGH`
<a id="insn-007fedc0"></a> `007fedc0` | `34 ff 41 d3` | lsr x20,x25,#0x1 | `FALL_THROUGH`
<a id="insn-007fedc4"></a> `007fedc4` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-007fedc8"></a> `007fedc8` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-007fedcc"></a> `007fedcc` | `a1 c3 00 d1` | sub x1,x29,#0x30 | `FALL_THROUGH`
<a id="insn-007fedd0"></a> `007fedd0` | `a2 43 01 d1` | sub x2,x29,#0x50 | `FALL_THROUGH`
<a id="insn-007fedd4"></a> `007fedd4` | `9c 6a 08 9b` | madd x28,x20,x8,x26 | `FALL_THROUGH`
<a id="insn-007fedd8"></a> `007fedd8` | `88 13 40 b9` | ldr w8,[x28, #0x10] | `FALL_THROUGH`
<a id="insn-007feddc"></a> `007feddc` | `80 03 c0 3d` | ldr q0,[x28] | `FALL_THROUGH`
<a id="insn-007fede0"></a> `007fede0` | `a8 03 1e b8` | stur w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-007fede4"></a> `007fede4` | `a0 03 9d 3c` | stur q0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-007fede8"></a> `007fede8` | `68 13 40 b9` | ldr w8,[x27, #0x10] | `FALL_THROUGH`
<a id="insn-007fedec"></a> `007fedec` | `60 03 c0 3d` | ldr q0,[x27] | `FALL_THROUGH`
<a id="insn-007fedf0"></a> `007fedf0` | `a8 03 1c b8` | stur w8,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-007fedf4"></a> `007fedf4` | `a0 03 9b 3c` | stur q0,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-007fedf8"></a> `007fedf8` | `1f fe ff 97` | bl 0x007fe674 | `UNCONDITIONAL_CALL`
<a id="insn-007fedfc"></a> `007fedfc` | `e8 03 34 aa` | mvn x8,x20 | `FALL_THROUGH`
<a id="insn-007fee00"></a> `007fee00` | `1f 00 00 72` | tst w0,#0x1 | `FALL_THROUGH`
<a id="insn-007fee04"></a> `007fee04` | `89 53 00 91` | add x9,x28,#0x14 | `FALL_THROUGH`
<a id="insn-007fee08"></a> `007fee08` | `28 03 08 8b` | add x8,x25,x8 | `FALL_THROUGH`
<a id="insn-007fee0c"></a> `007fee0c` | `3a 11 9a 9a` | csel x26,x9,x26,ne | `FALL_THROUGH`
<a id="insn-007fee10"></a> `007fee10` | `19 11 94 9a` | csel x25,x8,x20,ne | `FALL_THROUGH`
<a id="insn-007fee14"></a> `007fee14` | `79 fd ff b5` | cbnz x25,0x007fedc0 | `CONDITIONAL_JUMP`
<a id="insn-007fee18"></a> `007fee18` | `eb 23 40 f9` | ldr x11,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-007fee1c"></a> `007fee1c` | `ec 0b 40 f9` | ldr x12,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fee20"></a> `007fee20` | `48 03 15 cb` | sub x8,x26,x21 | `FALL_THROUGH`
<a id="insn-007fee24"></a> `007fee24` | `e9 e7 02 b2` | orr x9,xzr,#-0x3333333333333334 | `FALL_THROUGH`
<a id="insn-007fee28"></a> `007fee28` | `08 fd 42 93` | asr x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-007fee2c"></a> `007fee2c` | `a9 99 99 f2` | movk x9,#0xcccd | `FALL_THROUGH`
<a id="insn-007fee30"></a> `007fee30` | `19 7d 09 9b` | mul x25,x8,x9 | `FALL_THROUGH`
<a id="insn-007fee34"></a> `007fee34` | `e8 03 0c cb` | neg x8,x12 | `FALL_THROUGH`
<a id="insn-007fee38"></a> `007fee38` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-007fee3c"></a> `007fee3c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-007fee40"></a> `007fee40` | `1c 01 18 cb` | sub x28,x8,x24 | `FALL_THROUGH`
<a id="insn-007fee44"></a> `007fee44` | `68 01 19 cb` | sub x8,x11,x25 | `FALL_THROUGH`
<a id="insn-007fee48"></a> `007fee48` | `e2 03 1a aa` | mov x2,x26 | `FALL_THROUGH`
<a id="insn-007fee4c"></a> `007fee4c` | `e8 23 00 f9` | str x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-007fee50"></a> `007fee50` | `f5 03 0b aa` | mov x21,x11 | `FALL_THROUGH`
<a id="insn-007fee54"></a> `007fee54` | `f4 03 0c aa` | mov x20,x12 | `FALL_THROUGH`
<a id="insn-007fee58"></a> `007fee58` | `8b f5 ff 97` | bl 0x007fc484 | `UNCONDITIONAL_CALL`
<a id="insn-007fee5c"></a> `007fee5c` | `88 02 19 8b` | add x8,x20,x25 | `FALL_THROUGH`
<a id="insn-007fee60"></a> `007fee60` | `e4 03 14 aa` | mov x4,x20 | `FALL_THROUGH`
<a id="insn-007fee64"></a> `007fee64` | `a9 02 08 cb` | sub x9,x21,x8 | `FALL_THROUGH`
<a id="insn-007fee68"></a> `007fee68` | `29 01 18 cb` | sub x9,x9,x24 | `FALL_THROUGH`
<a id="insn-007fee6c"></a> `007fee6c` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-007fee70"></a> `007fee70` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-007fee74"></a> `007fee74` | `2a 02 00 54` | b.ge 0x007feeb8 | `CONDITIONAL_JUMP`
<a id="insn-007fee78"></a> `007fee78` | `e0 02 13 8b` | add x0,x23,x19 | `FALL_THROUGH`
<a id="insn-007fee7c"></a> `007fee7c` | `e1 03 1b aa` | mov x1,x27 | `FALL_THROUGH`
<a id="insn-007fee80"></a> `007fee80` | `fb 17 40 f9` | ldr x27,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-007fee84"></a> `007fee84` | `f3 0f 40 f9` | ldr x19,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-007fee88"></a> `007fee88` | `e7 1f 40 f9` | ldr x7,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-007fee8c"></a> `007fee8c` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-007fee90"></a> `007fee90` | `e3 03 1b aa` | mov x3,x27 | `FALL_THROUGH`
<a id="insn-007fee94"></a> `007fee94` | `e5 03 19 aa` | mov x5,x25 | `FALL_THROUGH`
<a id="insn-007fee98"></a> `007fee98` | `e6 03 13 aa` | mov x6,x19 | `FALL_THROUGH`
<a id="insn-007fee9c"></a> `007fee9c` | `50 ff ff 97` | bl 0x007febdc | `UNCONDITIONAL_CALL`
<a id="insn-007feea0"></a> `007feea0` | `f4 13 40 f9` | ldr x20,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007feea4"></a> `007feea4` | `f9 23 40 f9` | ldr x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-007feea8"></a> `007feea8` | `f6 03 18 aa` | mov x22,x24 | `FALL_THROUGH`
<a id="insn-007feeac"></a> `007feeac` | `f5 03 1a aa` | mov x21,x26 | `FALL_THROUGH`
<a id="insn-007feeb0"></a> `007feeb0` | `fa 03 13 aa` | mov x26,x19 | `FALL_THROUGH`
<a id="insn-007feeb4"></a> `007feeb4` | `10 00 00 14` | b 0x007feef4 | `UNCONDITIONAL_JUMP`
<a id="insn-007feeb8"></a> `007feeb8` | `f3 8b 42 a9` | ldp x19,x2,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-007feebc"></a> `007feebc` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-007feec0"></a> `007feec0` | `e7 97 43 a9` | ldp x7,x5,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-007feec4"></a> `007feec4` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-007feec8"></a> `007feec8` | `fa 0f 40 f9` | ldr x26,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-007feecc"></a> `007feecc` | `f7 03 04 aa` | mov x23,x4 | `FALL_THROUGH`
<a id="insn-007feed0"></a> `007feed0` | `e4 03 1c aa` | mov x4,x28 | `FALL_THROUGH`
<a id="insn-007feed4"></a> `007feed4` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-007feed8"></a> `007feed8` | `e6 03 1a aa` | mov x6,x26 | `FALL_THROUGH`
<a id="insn-007feedc"></a> `007feedc` | `40 ff ff 97` | bl 0x007febdc | `UNCONDITIONAL_CALL`
<a id="insn-007feee0"></a> `007feee0` | `f4 13 40 f9` | ldr x20,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007feee4"></a> `007feee4` | `f5 03 1b aa` | mov x21,x27 | `FALL_THROUGH`
<a id="insn-007feee8"></a> `007feee8` | `fb 03 13 aa` | mov x27,x19 | `FALL_THROUGH`
<a id="insn-007feeec"></a> `007feeec` | `fc 03 17 aa` | mov x28,x23 | `FALL_THROUGH`
<a id="insn-007feef0"></a> `007feef0` | `f8 1b 00 f9` | str x24,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007feef4"></a> `007feef4` | `f7 03 16 aa` | mov x23,x22 | `FALL_THROUGH`
<a id="insn-007feef8"></a> `007feef8` | `f9 23 00 f9` | str x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-007feefc"></a> `007feefc` | `79 e9 ff b5` | cbnz x25,0x007fec28 | `CONDITIONAL_JUMP`
<a id="insn-007fef00"></a> `007fef00` | `79 00 00 14` | b 0x007ff0e4 | `UNCONDITIONAL_JUMP`
<a id="insn-007fef04"></a> `007fef04` | `9f 03 09 eb` | cmp x28,x9 | `FALL_THROUGH`
<a id="insn-007fef08"></a> `007fef08` | `ad 05 00 54` | b.le 0x007fefbc | `CONDITIONAL_JUMP`
<a id="insn-007fef0c"></a> `007fef0c` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007fef10"></a> `007fef10` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-007fef14"></a> `007fef14` | `80 0e 00 54` | b.eq 0x007ff0e4 | `CONDITIONAL_JUMP`
<a id="insn-007fef18"></a> `007fef18` | `ec 1b 40 f9` | ldr x12,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007fef1c"></a> `007fef1c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-007fef20"></a> `007fef20` | `a9 02 08 8b` | add x9,x21,x8 | `FALL_THROUGH`
<a id="insn-007fef24"></a> `007fef24` | `4a 03 08 8b` | add x10,x26,x8 | `FALL_THROUGH`
<a id="insn-007fef28"></a> `007fef28` | `08 51 00 91` | add x8,x8,#0x14 | `FALL_THROUGH`
<a id="insn-007fef2c"></a> `007fef2c` | `2b 11 40 b9` | ldr w11,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-007fef30"></a> `007fef30` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-007fef34"></a> `007fef34` | `a9 02 08 8b` | add x9,x21,x8 | `FALL_THROUGH`
<a id="insn-007fef38"></a> `007fef38` | `3f 01 0c eb` | cmp x9,x12 | `FALL_THROUGH`
<a id="insn-007fef3c"></a> `007fef3c` | `4b 11 00 b9` | str w11,[x10, #0x10] | `FALL_THROUGH`
<a id="insn-007fef40"></a> `007fef40` | `40 01 80 3d` | str q0,[x10] | `FALL_THROUGH`
<a id="insn-007fef44"></a> `007fef44` | `e1 fe ff 54` | b.ne 0x007fef20 | `CONDITIONAL_JUMP`
<a id="insn-007fef48"></a> `007fef48` | `93 51 00 d1` | sub x19,x12,#0x14 | `FALL_THROUGH`
<a id="insn-007fef4c"></a> `007fef4c` | `56 03 08 8b` | add x22,x26,x8 | `FALL_THROUGH`
<a id="insn-007fef50"></a> `007fef50` | `bf 02 17 eb` | cmp x21,x23 | `FALL_THROUGH`
<a id="insn-007fef54"></a> `007fef54` | `40 0a 00 54` | b.eq 0x007ff09c | `CONDITIONAL_JUMP`
<a id="insn-007fef58"></a> `007fef58` | `c8 c2 5f b8` | ldur w8,[x22, #-0x4] | `FALL_THROUGH`
<a id="insn-007fef5c"></a> `007fef5c` | `c0 c2 de 3c` | ldur q0,[x22, #-0x14] | `FALL_THROUGH`
<a id="insn-007fef60"></a> `007fef60` | `a1 c3 00 d1` | sub x1,x29,#0x30 | `FALL_THROUGH`
<a id="insn-007fef64"></a> `007fef64` | `a2 43 01 d1` | sub x2,x29,#0x50 | `FALL_THROUGH`
<a id="insn-007fef68"></a> `007fef68` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-007fef6c"></a> `007fef6c` | `b8 52 00 d1` | sub x24,x21,#0x14 | `FALL_THROUGH`
<a id="insn-007fef70"></a> `007fef70` | `a8 03 1e b8` | stur w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-007fef74"></a> `007fef74` | `d9 52 00 d1` | sub x25,x22,#0x14 | `FALL_THROUGH`
<a id="insn-007fef78"></a> `007fef78` | `a0 03 9d 3c` | stur q0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-007fef7c"></a> `007fef7c` | `a8 c2 5f b8` | ldur w8,[x21, #-0x4] | `FALL_THROUGH`
<a id="insn-007fef80"></a> `007fef80` | `a0 c2 de 3c` | ldur q0,[x21, #-0x14] | `FALL_THROUGH`
<a id="insn-007fef84"></a> `007fef84` | `a8 03 1c b8` | stur w8,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-007fef88"></a> `007fef88` | `a0 03 9b 3c` | stur q0,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-007fef8c"></a> `007fef8c` | `ba fd ff 97` | bl 0x007fe674 | `UNCONDITIONAL_CALL`
<a id="insn-007fef90"></a> `007fef90` | `1f 00 00 72` | tst w0,#0x1 | `FALL_THROUGH`
<a id="insn-007fef94"></a> `007fef94` | `08 13 99 9a` | csel x8,x24,x25,ne | `FALL_THROUGH`
<a id="insn-007fef98"></a> `007fef98` | `d6 12 99 9a` | csel x22,x22,x25,ne | `FALL_THROUGH`
<a id="insn-007fef9c"></a> `007fef9c` | `15 13 95 9a` | csel x21,x24,x21,ne | `FALL_THROUGH`
<a id="insn-007fefa0"></a> `007fefa0` | `09 41 40 39` | ldrb w9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-007fefa4"></a> `007fefa4` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-007fefa8"></a> `007fefa8` | `df 02 1a eb` | cmp x22,x26 | `FALL_THROUGH`
<a id="insn-007fefac"></a> `007fefac` | `69 42 00 39` | strb w9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-007fefb0"></a> `007fefb0` | `60 c6 9e 3c` | str q0,[x19], #-0x14 | `FALL_THROUGH`
<a id="insn-007fefb4"></a> `007fefb4` | `e1 fc ff 54` | b.ne 0x007fef50 | `CONDITIONAL_JUMP`
<a id="insn-007fefb8"></a> `007fefb8` | `4b 00 00 14` | b 0x007ff0e4 | `UNCONDITIONAL_JUMP`
<a id="insn-007fefbc"></a> `007fefbc` | `f9 1b 40 f9` | ldr x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007fefc0"></a> `007fefc0` | `ff 02 15 eb` | cmp x23,x21 | `FALL_THROUGH`
<a id="insn-007fefc4"></a> `007fefc4` | `00 09 00 54` | b.eq 0x007ff0e4 | `CONDITIONAL_JUMP`
<a id="insn-007fefc8"></a> `007fefc8` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-007fefcc"></a> `007fefcc` | `e8 02 16 8b` | add x8,x23,x22 | `FALL_THROUGH`
<a id="insn-007fefd0"></a> `007fefd0` | `49 03 16 8b` | add x9,x26,x22 | `FALL_THROUGH`
<a id="insn-007fefd4"></a> `007fefd4` | `d6 52 00 91` | add x22,x22,#0x14 | `FALL_THROUGH`
<a id="insn-007fefd8"></a> `007fefd8` | `0a 11 40 b9` | ldr w10,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-007fefdc"></a> `007fefdc` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-007fefe0"></a> `007fefe0` | `e8 02 16 8b` | add x8,x23,x22 | `FALL_THROUGH`
<a id="insn-007fefe4"></a> `007fefe4` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-007fefe8"></a> `007fefe8` | `2a 11 00 b9` | str w10,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-007fefec"></a> `007fefec` | `20 01 80 3d` | str q0,[x9] | `FALL_THROUGH`
<a id="insn-007feff0"></a> `007feff0` | `e1 fe ff 54` | b.ne 0x007fefcc | `CONDITIONAL_JUMP`
<a id="insn-007feff4"></a> `007feff4` | `58 03 16 8b` | add x24,x26,x22 | `FALL_THROUGH`
<a id="insn-007feff8"></a> `007feff8` | `f3 03 1a aa` | mov x19,x26 | `FALL_THROUGH`
<a id="insn-007feffc"></a> `007feffc` | `08 00 00 14` | b 0x007ff01c | `UNCONDITIONAL_JUMP`
<a id="insn-007ff000"></a> `007ff000` | `68 42 40 39` | ldrb w8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-007ff004"></a> `007ff004` | `60 46 c1 3c` | ldr q0,[x19], #0x14 | `FALL_THROUGH`
<a id="insn-007ff008"></a> `007ff008` | `e8 42 00 39` | strb w8,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-007ff00c"></a> `007ff00c` | `e0 02 80 3d` | str q0,[x23] | `FALL_THROUGH`
<a id="insn-007ff010"></a> `007ff010` | `1f 03 13 eb` | cmp x24,x19 | `FALL_THROUGH`
<a id="insn-007ff014"></a> `007ff014` | `f7 52 00 91` | add x23,x23,#0x14 | `FALL_THROUGH`
<a id="insn-007ff018"></a> `007ff018` | `60 06 00 54` | b.eq 0x007ff0e4 | `CONDITIONAL_JUMP`
<a id="insn-007ff01c"></a> `007ff01c` | `bf 02 19 eb` | cmp x21,x25 | `FALL_THROUGH`
<a id="insn-007ff020"></a> `007ff020` | `60 05 00 54` | b.eq 0x007ff0cc | `CONDITIONAL_JUMP`
<a id="insn-007ff024"></a> `007ff024` | `a8 12 40 b9` | ldr w8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-007ff028"></a> `007ff028` | `a0 02 c0 3d` | ldr q0,[x21] | `FALL_THROUGH`
<a id="insn-007ff02c"></a> `007ff02c` | `a1 c3 00 d1` | sub x1,x29,#0x30 | `FALL_THROUGH`
<a id="insn-007ff030"></a> `007ff030` | `a2 43 01 d1` | sub x2,x29,#0x50 | `FALL_THROUGH`
<a id="insn-007ff034"></a> `007ff034` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-007ff038"></a> `007ff038` | `a8 03 1e b8` | stur w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-007ff03c"></a> `007ff03c` | `a0 03 9d 3c` | stur q0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-007ff040"></a> `007ff040` | `68 12 40 b9` | ldr w8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-007ff044"></a> `007ff044` | `60 02 c0 3d` | ldr q0,[x19] | `FALL_THROUGH`
<a id="insn-007ff048"></a> `007ff048` | `a8 03 1c b8` | stur w8,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-007ff04c"></a> `007ff04c` | `a0 03 9b 3c` | stur q0,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-007ff050"></a> `007ff050` | `89 fd ff 97` | bl 0x007fe674 | `UNCONDITIONAL_CALL`
<a id="insn-007ff054"></a> `007ff054` | `60 fd 07 36` | tbz w0,#0x0,0x007ff000 | `CONDITIONAL_JUMP`
<a id="insn-007ff058"></a> `007ff058` | `a8 42 40 39` | ldrb w8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-007ff05c"></a> `007ff05c` | `a0 46 c1 3c` | ldr q0,[x21], #0x14 | `FALL_THROUGH`
<a id="insn-007ff060"></a> `007ff060` | `ea ff ff 17` | b 0x007ff008 | `UNCONDITIONAL_JUMP`
<a id="insn-007ff064"></a> `007ff064` | `e8 02 13 8b` | add x8,x23,x19 | `FALL_THROUGH`
<a id="insn-007ff068"></a> `007ff068` | `aa 42 40 39` | ldrb w10,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-007ff06c"></a> `007ff06c` | `a1 02 c0 3d` | ldr q1,[x21] | `FALL_THROUGH`
<a id="insn-007ff070"></a> `007ff070` | `09 11 40 b9` | ldr w9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-007ff074"></a> `007ff074` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-007ff078"></a> `007ff078` | `a9 03 1e b8` | stur w9,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-007ff07c"></a> `007ff07c` | `a0 03 9d 3c` | stur q0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-007ff080"></a> `007ff080` | `0a 41 00 39` | strb w10,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-007ff084"></a> `007ff084` | `01 01 80 3d` | str q1,[x8] | `FALL_THROUGH`
<a id="insn-007ff088"></a> `007ff088` | `a0 03 dd 3c` | ldur q0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-007ff08c"></a> `007ff08c` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-007ff090"></a> `007ff090` | `a0 02 80 3d` | str q0,[x21] | `FALL_THROUGH`
<a id="insn-007ff094"></a> `007ff094` | `a8 42 00 39` | strb w8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-007ff098"></a> `007ff098` | `13 00 00 14` | b 0x007ff0e4 | `UNCONDITIONAL_JUMP`
<a id="insn-007ff09c"></a> `007ff09c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-007ff0a0"></a> `007ff0a0` | `c9 02 08 8b` | add x9,x22,x8 | `FALL_THROUGH`
<a id="insn-007ff0a4"></a> `007ff0a4` | `6a 02 08 8b` | add x10,x19,x8 | `FALL_THROUGH`
<a id="insn-007ff0a8"></a> `007ff0a8` | `08 51 00 d1` | sub x8,x8,#0x14 | `FALL_THROUGH`
<a id="insn-007ff0ac"></a> `007ff0ac` | `2b c1 5f 38` | ldurb w11,[x9, #-0x4] | `FALL_THROUGH`
<a id="insn-007ff0b0"></a> `007ff0b0` | `20 c1 de 3c` | ldur q0,[x9, #-0x14] | `FALL_THROUGH`
<a id="insn-007ff0b4"></a> `007ff0b4` | `c9 02 08 8b` | add x9,x22,x8 | `FALL_THROUGH`
<a id="insn-007ff0b8"></a> `007ff0b8` | `3f 01 1a eb` | cmp x9,x26 | `FALL_THROUGH`
<a id="insn-007ff0bc"></a> `007ff0bc` | `4b 41 00 39` | strb w11,[x10, #0x10] | `FALL_THROUGH`
<a id="insn-007ff0c0"></a> `007ff0c0` | `40 01 80 3d` | str q0,[x10] | `FALL_THROUGH`
<a id="insn-007ff0c4"></a> `007ff0c4` | `e1 fe ff 54` | b.ne 0x007ff0a0 | `CONDITIONAL_JUMP`
<a id="insn-007ff0c8"></a> `007ff0c8` | `07 00 00 14` | b 0x007ff0e4 | `UNCONDITIONAL_JUMP`
<a id="insn-007ff0cc"></a> `007ff0cc` | `48 03 13 cb` | sub x8,x26,x19 | `FALL_THROUGH`
<a id="insn-007ff0d0"></a> `007ff0d0` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-007ff0d4"></a> `007ff0d4` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-007ff0d8"></a> `007ff0d8` | `08 01 16 8b` | add x8,x8,x22 | `FALL_THROUGH`
<a id="insn-007ff0dc"></a> `007ff0dc` | `02 0d 00 d1` | sub x2,x8,#0x3 | `FALL_THROUGH`
<a id="insn-007ff0e0"></a> `007ff0e0` | `f0 6f 0f 94` | bl 0x00bdb0a0 | `UNCONDITIONAL_CALL`
<a id="insn-007ff0e4"></a> `007ff0e4` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-007ff0e8"></a> `007ff0e8` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-007ff0ec"></a> `007ff0ec` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-007ff0f0"></a> `007ff0f0` | `21 01 00 54` | b.ne 0x007ff114 | `CONDITIONAL_JUMP`
<a id="insn-007ff0f4"></a> `007ff0f4` | `f4 4f 53 a9` | ldp x20,x19,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-007ff0f8"></a> `007ff0f8` | `f6 57 52 a9` | ldp x22,x21,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-007ff0fc"></a> `007ff0fc` | `f8 5f 51 a9` | ldp x24,x23,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-007ff100"></a> `007ff100` | `fa 67 50 a9` | ldp x26,x25,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-007ff104"></a> `007ff104` | `fc 6f 4f a9` | ldp x28,x27,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-007ff108"></a> `007ff108` | `fd 7b 4e a9` | ldp x29,x30,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-007ff10c"></a> `007ff10c` | `ff 03 05 91` | add sp,sp,#0x140 | `FALL_THROUGH`
<a id="insn-007ff110"></a> `007ff110` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-007ff114"></a> `007ff114` | `cb 6f 0f 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007febdc`](#insn-007febdc) 範囲 `[['007febdc', '007fec13']]`
  - `CONDITIONAL_JUMP` [`007fec10`](#insn-007fec10) → [`007ff0e4`](#insn-007ff0e4)
  - `FALL_THROUGH` [`007fec10`](#insn-007fec10) → [`007fec14`](#insn-007fec14)
- ブロック [`007fec14`](#insn-007fec14) 範囲 `[['007fec14', '007fec27']]`
  - `FALL_THROUGH` [`007fec24`](#insn-007fec24) → [`007fec28`](#insn-007fec28)
- ブロック [`007fec28`](#insn-007fec28) 範囲 `[['007fec28', '007fec33']]`
  - `CONDITIONAL_JUMP` [`007fec30`](#insn-007fec30) → [`007fef04`](#insn-007fef04)
  - `FALL_THROUGH` [`007fec30`](#insn-007fec30) → [`007fec34`](#insn-007fec34)
- ブロック [`007fec34`](#insn-007fec34) 範囲 `[['007fec34', '007fec3b']]`
  - `CONDITIONAL_JUMP` [`007fec38`](#insn-007fec38) → [`007fef04`](#insn-007fef04)
  - `FALL_THROUGH` [`007fec38`](#insn-007fec38) → [`007fec3c`](#insn-007fec3c)
- ブロック [`007fec3c`](#insn-007fec3c) 範囲 `[['007fec3c', '007fec3f']]`
  - `CONDITIONAL_JUMP` [`007fec3c`](#insn-007fec3c) → [`007ff0e4`](#insn-007ff0e4)
  - `FALL_THROUGH` [`007fec3c`](#insn-007fec3c) → [`007fec40`](#insn-007fec40)
- ブロック [`007fec40`](#insn-007fec40) 範囲 `[['007fec40', '007fec47']]`
  - `FALL_THROUGH` [`007fec44`](#insn-007fec44) → [`007fec48`](#insn-007fec48)
- ブロック [`007fec48`](#insn-007fec48) 範囲 `[['007fec48', '007fec7f']]`
  - `CONDITIONAL_JUMP` [`007fec7c`](#insn-007fec7c) → [`007fec90`](#insn-007fec90)
  - `FALL_THROUGH` [`007fec7c`](#insn-007fec7c) → [`007fec80`](#insn-007fec80)
- ブロック [`007fec80`](#insn-007fec80) 範囲 `[['007fec80', '007fec8b']]`
  - `CONDITIONAL_JUMP` [`007fec88`](#insn-007fec88) → [`007fec48`](#insn-007fec48)
  - `FALL_THROUGH` [`007fec88`](#insn-007fec88) → [`007fec8c`](#insn-007fec8c)
- ブロック [`007fec8c`](#insn-007fec8c) 範囲 `[['007fec8c', '007fec8f']]`
  - `UNCONDITIONAL_JUMP` [`007fec8c`](#insn-007fec8c) → [`007ff0e4`](#insn-007ff0e4)
- ブロック [`007fec90`](#insn-007fec90) 範囲 `[['007fec90', '007fecab']]`
  - `CONDITIONAL_JUMP` [`007feca8`](#insn-007feca8) → [`007fed6c`](#insn-007fed6c)
  - `FALL_THROUGH` [`007feca8`](#insn-007feca8) → [`007fecac`](#insn-007fecac)
- ブロック [`007fecac`](#insn-007fecac) 範囲 `[['007fecac', '007feccf']]`
  - `CONDITIONAL_JUMP` [`007feccc`](#insn-007feccc) → [`007fed4c`](#insn-007fed4c)
  - `FALL_THROUGH` [`007feccc`](#insn-007feccc) → [`007fecd0`](#insn-007fecd0)
- ブロック [`007fecd0`](#insn-007fecd0) 範囲 `[['007fecd0', '007feceb']]`
  - `FALL_THROUGH` [`007fece8`](#insn-007fece8) → [`007fecec`](#insn-007fecec)
- ブロック [`007fecec`](#insn-007fecec) 範囲 `[['007fecec', '007fed43']]`
  - `CONDITIONAL_JUMP` [`007fed40`](#insn-007fed40) → [`007fecec`](#insn-007fecec)
  - `FALL_THROUGH` [`007fed40`](#insn-007fed40) → [`007fed44`](#insn-007fed44)
- ブロック [`007fed44`](#insn-007fed44) 範囲 `[['007fed44', '007fed4b']]`
  - `FALL_THROUGH` [`007fed48`](#insn-007fed48) → [`007fed4c`](#insn-007fed4c)
- ブロック [`007fed4c`](#insn-007fed4c) 範囲 `[['007fed4c', '007fed6b']]`
  - `UNCONDITIONAL_JUMP` [`007fed68`](#insn-007fed68) → [`007fee34`](#insn-007fee34)
- ブロック [`007fed6c`](#insn-007fed6c) 範囲 `[['007fed6c', '007fed73']]`
  - `CONDITIONAL_JUMP` [`007fed70`](#insn-007fed70) → [`007ff064`](#insn-007ff064)
  - `FALL_THROUGH` [`007fed70`](#insn-007fed70) → [`007fed74`](#insn-007fed74)
- ブロック [`007fed74`](#insn-007fed74) 範囲 `[['007fed74', '007fed9f']]`
  - `CONDITIONAL_JUMP` [`007fed9c`](#insn-007fed9c) → [`007fee20`](#insn-007fee20)
  - `FALL_THROUGH` [`007fed9c`](#insn-007fed9c) → [`007feda0`](#insn-007feda0)
- ブロック [`007feda0`](#insn-007feda0) 範囲 `[['007feda0', '007fedbf']]`
  - `FALL_THROUGH` [`007fedbc`](#insn-007fedbc) → [`007fedc0`](#insn-007fedc0)
- ブロック [`007fedc0`](#insn-007fedc0) 範囲 `[['007fedc0', '007fee17']]`
  - `CONDITIONAL_JUMP` [`007fee14`](#insn-007fee14) → [`007fedc0`](#insn-007fedc0)
  - `FALL_THROUGH` [`007fee14`](#insn-007fee14) → [`007fee18`](#insn-007fee18)
- ブロック [`007fee18`](#insn-007fee18) 範囲 `[['007fee18', '007fee1f']]`
  - `FALL_THROUGH` [`007fee1c`](#insn-007fee1c) → [`007fee20`](#insn-007fee20)
- ブロック [`007fee20`](#insn-007fee20) 範囲 `[['007fee20', '007fee33']]`
  - `FALL_THROUGH` [`007fee30`](#insn-007fee30) → [`007fee34`](#insn-007fee34)
- ブロック [`007fee34`](#insn-007fee34) 範囲 `[['007fee34', '007fee77']]`
  - `CONDITIONAL_JUMP` [`007fee74`](#insn-007fee74) → [`007feeb8`](#insn-007feeb8)
  - `FALL_THROUGH` [`007fee74`](#insn-007fee74) → [`007fee78`](#insn-007fee78)
- ブロック [`007fee78`](#insn-007fee78) 範囲 `[['007fee78', '007feeb7']]`
  - `UNCONDITIONAL_JUMP` [`007feeb4`](#insn-007feeb4) → [`007feef4`](#insn-007feef4)
- ブロック [`007feeb8`](#insn-007feeb8) 範囲 `[['007feeb8', '007feef3']]`
  - `FALL_THROUGH` [`007feef0`](#insn-007feef0) → [`007feef4`](#insn-007feef4)
- ブロック [`007feef4`](#insn-007feef4) 範囲 `[['007feef4', '007feeff']]`
  - `CONDITIONAL_JUMP` [`007feefc`](#insn-007feefc) → [`007fec28`](#insn-007fec28)
  - `FALL_THROUGH` [`007feefc`](#insn-007feefc) → [`007fef00`](#insn-007fef00)
- ブロック [`007fef00`](#insn-007fef00) 範囲 `[['007fef00', '007fef03']]`
  - `UNCONDITIONAL_JUMP` [`007fef00`](#insn-007fef00) → [`007ff0e4`](#insn-007ff0e4)
- ブロック [`007fef04`](#insn-007fef04) 範囲 `[['007fef04', '007fef0b']]`
  - `CONDITIONAL_JUMP` [`007fef08`](#insn-007fef08) → [`007fefbc`](#insn-007fefbc)
  - `FALL_THROUGH` [`007fef08`](#insn-007fef08) → [`007fef0c`](#insn-007fef0c)
- ブロック [`007fef0c`](#insn-007fef0c) 範囲 `[['007fef0c', '007fef17']]`
  - `CONDITIONAL_JUMP` [`007fef14`](#insn-007fef14) → [`007ff0e4`](#insn-007ff0e4)
  - `FALL_THROUGH` [`007fef14`](#insn-007fef14) → [`007fef18`](#insn-007fef18)
- ブロック [`007fef18`](#insn-007fef18) 範囲 `[['007fef18', '007fef1f']]`
  - `FALL_THROUGH` [`007fef1c`](#insn-007fef1c) → [`007fef20`](#insn-007fef20)
- ブロック [`007fef20`](#insn-007fef20) 範囲 `[['007fef20', '007fef47']]`
  - `CONDITIONAL_JUMP` [`007fef44`](#insn-007fef44) → [`007fef20`](#insn-007fef20)
  - `FALL_THROUGH` [`007fef44`](#insn-007fef44) → [`007fef48`](#insn-007fef48)
- ブロック [`007fef48`](#insn-007fef48) 範囲 `[['007fef48', '007fef4f']]`
  - `FALL_THROUGH` [`007fef4c`](#insn-007fef4c) → [`007fef50`](#insn-007fef50)
- ブロック [`007fef50`](#insn-007fef50) 範囲 `[['007fef50', '007fef57']]`
  - `CONDITIONAL_JUMP` [`007fef54`](#insn-007fef54) → [`007ff09c`](#insn-007ff09c)
  - `FALL_THROUGH` [`007fef54`](#insn-007fef54) → [`007fef58`](#insn-007fef58)
- ブロック [`007fef58`](#insn-007fef58) 範囲 `[['007fef58', '007fefb7']]`
  - `CONDITIONAL_JUMP` [`007fefb4`](#insn-007fefb4) → [`007fef50`](#insn-007fef50)
  - `FALL_THROUGH` [`007fefb4`](#insn-007fefb4) → [`007fefb8`](#insn-007fefb8)
- ブロック [`007fefb8`](#insn-007fefb8) 範囲 `[['007fefb8', '007fefbb']]`
  - `UNCONDITIONAL_JUMP` [`007fefb8`](#insn-007fefb8) → [`007ff0e4`](#insn-007ff0e4)
- ブロック [`007fefbc`](#insn-007fefbc) 範囲 `[['007fefbc', '007fefc7']]`
  - `CONDITIONAL_JUMP` [`007fefc4`](#insn-007fefc4) → [`007ff0e4`](#insn-007ff0e4)
  - `FALL_THROUGH` [`007fefc4`](#insn-007fefc4) → [`007fefc8`](#insn-007fefc8)
- ブロック [`007fefc8`](#insn-007fefc8) 範囲 `[['007fefc8', '007fefcb']]`
  - `FALL_THROUGH` [`007fefc8`](#insn-007fefc8) → [`007fefcc`](#insn-007fefcc)
- ブロック [`007fefcc`](#insn-007fefcc) 範囲 `[['007fefcc', '007feff3']]`
  - `CONDITIONAL_JUMP` [`007feff0`](#insn-007feff0) → [`007fefcc`](#insn-007fefcc)
  - `FALL_THROUGH` [`007feff0`](#insn-007feff0) → [`007feff4`](#insn-007feff4)
- ブロック [`007feff4`](#insn-007feff4) 範囲 `[['007feff4', '007fefff']]`
  - `UNCONDITIONAL_JUMP` [`007feffc`](#insn-007feffc) → [`007ff01c`](#insn-007ff01c)
- ブロック [`007ff000`](#insn-007ff000) 範囲 `[['007ff000', '007ff007']]`
  - `FALL_THROUGH` [`007ff004`](#insn-007ff004) → [`007ff008`](#insn-007ff008)
- ブロック [`007ff008`](#insn-007ff008) 範囲 `[['007ff008', '007ff01b']]`
  - `CONDITIONAL_JUMP` [`007ff018`](#insn-007ff018) → [`007ff0e4`](#insn-007ff0e4)
  - `FALL_THROUGH` [`007ff018`](#insn-007ff018) → [`007ff01c`](#insn-007ff01c)
- ブロック [`007ff01c`](#insn-007ff01c) 範囲 `[['007ff01c', '007ff023']]`
  - `CONDITIONAL_JUMP` [`007ff020`](#insn-007ff020) → [`007ff0cc`](#insn-007ff0cc)
  - `FALL_THROUGH` [`007ff020`](#insn-007ff020) → [`007ff024`](#insn-007ff024)
- ブロック [`007ff024`](#insn-007ff024) 範囲 `[['007ff024', '007ff02f']]`
  - `FALL_THROUGH` [`007ff02c`](#insn-007ff02c) → [`007ff030`](#insn-007ff030)
- ブロック [`007ff030`](#insn-007ff030) 範囲 `[['007ff030', '007ff03b']]`
  - `FALL_THROUGH` [`007ff038`](#insn-007ff038) → [`007ff03c`](#insn-007ff03c)
- ブロック [`007ff03c`](#insn-007ff03c) 範囲 `[['007ff03c', '007ff057']]`
  - `CONDITIONAL_JUMP` [`007ff054`](#insn-007ff054) → [`007ff000`](#insn-007ff000)
  - `FALL_THROUGH` [`007ff054`](#insn-007ff054) → [`007ff058`](#insn-007ff058)
- ブロック [`007ff058`](#insn-007ff058) 範囲 `[['007ff058', '007ff063']]`
  - `UNCONDITIONAL_JUMP` [`007ff060`](#insn-007ff060) → [`007ff008`](#insn-007ff008)
- ブロック [`007ff064`](#insn-007ff064) 範囲 `[['007ff064', '007ff077']]`
  - `FALL_THROUGH` [`007ff074`](#insn-007ff074) → [`007ff078`](#insn-007ff078)
- ブロック [`007ff078`](#insn-007ff078) 範囲 `[['007ff078', '007ff09b']]`
  - `UNCONDITIONAL_JUMP` [`007ff098`](#insn-007ff098) → [`007ff0e4`](#insn-007ff0e4)
- ブロック [`007ff09c`](#insn-007ff09c) 範囲 `[['007ff09c', '007ff09f']]`
  - `FALL_THROUGH` [`007ff09c`](#insn-007ff09c) → [`007ff0a0`](#insn-007ff0a0)
- ブロック [`007ff0a0`](#insn-007ff0a0) 範囲 `[['007ff0a0', '007ff0c7']]`
  - `CONDITIONAL_JUMP` [`007ff0c4`](#insn-007ff0c4) → [`007ff0a0`](#insn-007ff0a0)
  - `FALL_THROUGH` [`007ff0c4`](#insn-007ff0c4) → [`007ff0c8`](#insn-007ff0c8)
- ブロック [`007ff0c8`](#insn-007ff0c8) 範囲 `[['007ff0c8', '007ff0cb']]`
  - `UNCONDITIONAL_JUMP` [`007ff0c8`](#insn-007ff0c8) → [`007ff0e4`](#insn-007ff0e4)
- ブロック [`007ff0cc`](#insn-007ff0cc) 範囲 `[['007ff0cc', '007ff0db']]`
  - `FALL_THROUGH` [`007ff0d8`](#insn-007ff0d8) → [`007ff0dc`](#insn-007ff0dc)
- ブロック [`007ff0dc`](#insn-007ff0dc) 範囲 `[['007ff0dc', '007ff0e3']]`
  - `FALL_THROUGH` [`007ff0e0`](#insn-007ff0e0) → [`007ff0e4`](#insn-007ff0e4)
- ブロック [`007ff0e4`](#insn-007ff0e4) 範囲 `[['007ff0e4', '007ff0f3']]`
  - `CONDITIONAL_JUMP` [`007ff0f0`](#insn-007ff0f0) → [`007ff114`](#insn-007ff114)
  - `FALL_THROUGH` [`007ff0f0`](#insn-007ff0f0) → [`007ff0f4`](#insn-007ff0f4)
- ブロック [`007ff0f4`](#insn-007ff0f4) 範囲 `[['007ff0f4', '007ff113']]`
- ブロック [`007ff114`](#insn-007ff114) 範囲 `[['007ff114', '007ff117']]`

## 命令位置別の参照

- [`007febe0`](#insn-007febe0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007febe4`](#insn-007febe4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007febe8`](#insn-007febe8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007febec`](#insn-007febec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007febf0`](#insn-007febf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007febf4`](#insn-007febf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007febfc`](#insn-007febfc) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fec08`](#insn-007fec08) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fec0c`](#insn-007fec0c) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fec10`](#insn-007fec10) → [`007ff0e4`](#insn-007ff0e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fec28`](#insn-007fec28) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fec30`](#insn-007fec30) → [`007fef04`](#insn-007fef04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fec38`](#insn-007fec38) → [`007fef04`](#insn-007fef04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fec3c`](#insn-007fec3c) → [`007ff0e4`](#insn-007ff0e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fec60`](#insn-007fec60) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fec64`](#insn-007fec64) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fec70`](#insn-007fec70) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fec74`](#insn-007fec74) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fec78`](#insn-007fec78) → [`007fe674`](007fe674.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007fe674` · 推定シンボル `None` · 推定型 `None`
- [`007fec7c`](#insn-007fec7c) → [`007fec90`](#insn-007fec90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fec88`](#insn-007fec88) → [`007fec48`](#insn-007fec48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fec8c`](#insn-007fec8c) → [`007ff0e4`](#insn-007ff0e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fec90`](#insn-007fec90) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fec9c`](#insn-007fec9c) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007feca4`](#insn-007feca4) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007feca8`](#insn-007feca8) → [`007fed6c`](#insn-007fed6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fecc0`](#insn-007fecc0) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007feccc`](#insn-007feccc) → [`007fed4c`](#insn-007fed4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fecd8`](#insn-007fecd8) → `Stack[-0x138]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fece0`](#insn-007fece0) → `Stack[-0x118]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fed08`](#insn-007fed08) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fed0c`](#insn-007fed0c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fed18`](#insn-007fed18) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fed1c`](#insn-007fed1c) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fed20`](#insn-007fed20) → [`007fe674`](007fe674.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007fe674` · 推定シンボル `None` · 推定型 `None`
- [`007fed40`](#insn-007fed40) → [`007fecec`](#insn-007fecec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fed44`](#insn-007fed44) → `Stack[-0x138]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fed48`](#insn-007fed48) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fed54`](#insn-007fed54) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fed68`](#insn-007fed68) → [`007fee34`](#insn-007fee34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fed70`](#insn-007fed70) → [`007ff064`](#insn-007ff064) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fed78`](#insn-007fed78) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fed94`](#insn-007fed94) → `Stack[-0xf8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fed9c`](#insn-007fed9c) → [`007fee20`](#insn-007fee20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007feda0`](#insn-007feda0) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fedb0`](#insn-007fedb0) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fede0`](#insn-007fede0) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fede4`](#insn-007fede4) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fedf0`](#insn-007fedf0) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fedf4`](#insn-007fedf4) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fedf8`](#insn-007fedf8) → [`007fe674`](007fe674.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007fe674` · 推定シンボル `None` · 推定型 `None`
- [`007fee14`](#insn-007fee14) → [`007fedc0`](#insn-007fedc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fee18`](#insn-007fee18) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fee1c`](#insn-007fee1c) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fee4c`](#insn-007fee4c) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fee58`](#insn-007fee58) → [`007fc484`](../007fc/007fc484.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007fc484` · 推定シンボル `None` · 推定型 `None`
- [`007fee74`](#insn-007fee74) → [`007feeb8`](#insn-007feeb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fee80`](#insn-007fee80) → `Stack[-0x118]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fee84`](#insn-007fee84) → `Stack[-0x128]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fee88`](#insn-007fee88) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fee9c`](#insn-007fee9c) → [`007febdc`](#insn-007febdc) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007febdc` · 推定シンボル `None` · 推定型 `None`
- [`007feea0`](#insn-007feea0) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007feea4`](#insn-007feea4) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007feeb4`](#insn-007feeb4) → [`007feef4`](#insn-007feef4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007feeb8`](#insn-007feeb8) → `Stack[-0x118]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007feec0`](#insn-007feec0) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007feec8`](#insn-007feec8) → `Stack[-0x128]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007feedc`](#insn-007feedc) → [`007febdc`](#insn-007febdc) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007febdc` · 推定シンボル `None` · 推定型 `None`
- [`007feee0`](#insn-007feee0) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007feef0`](#insn-007feef0) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007feef8`](#insn-007feef8) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007feefc`](#insn-007feefc) → [`007fec28`](#insn-007fec28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fef00`](#insn-007fef00) → [`007ff0e4`](#insn-007ff0e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fef08`](#insn-007fef08) → [`007fefbc`](#insn-007fefbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fef0c`](#insn-007fef0c) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fef14`](#insn-007fef14) → [`007ff0e4`](#insn-007ff0e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fef18`](#insn-007fef18) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fef44`](#insn-007fef44) → [`007fef20`](#insn-007fef20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fef54`](#insn-007fef54) → [`007ff09c`](#insn-007ff09c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fef70`](#insn-007fef70) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fef78`](#insn-007fef78) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fef84`](#insn-007fef84) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fef88`](#insn-007fef88) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fef8c`](#insn-007fef8c) → [`007fe674`](007fe674.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007fe674` · 推定シンボル `None` · 推定型 `None`
- [`007fefb4`](#insn-007fefb4) → [`007fef50`](#insn-007fef50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fefb8`](#insn-007fefb8) → [`007ff0e4`](#insn-007ff0e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fefbc`](#insn-007fefbc) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fefc4`](#insn-007fefc4) → [`007ff0e4`](#insn-007ff0e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007feff0`](#insn-007feff0) → [`007fefcc`](#insn-007fefcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007feffc`](#insn-007feffc) → [`007ff01c`](#insn-007ff01c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff018`](#insn-007ff018) → [`007ff0e4`](#insn-007ff0e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff020`](#insn-007ff020) → [`007ff0cc`](#insn-007ff0cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff038`](#insn-007ff038) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff03c`](#insn-007ff03c) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff048`](#insn-007ff048) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff04c`](#insn-007ff04c) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff050`](#insn-007ff050) → [`007fe674`](007fe674.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007fe674` · 推定シンボル `None` · 推定型 `None`
- [`007ff054`](#insn-007ff054) → [`007ff000`](#insn-007ff000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff060`](#insn-007ff060) → [`007ff008`](#insn-007ff008) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff078`](#insn-007ff078) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff07c`](#insn-007ff07c) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff088`](#insn-007ff088) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff08c`](#insn-007ff08c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff098`](#insn-007ff098) → [`007ff0e4`](#insn-007ff0e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff0c4`](#insn-007ff0c4) → [`007ff0a0`](#insn-007ff0a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff0c8`](#insn-007ff0c8) → [`007ff0e4`](#insn-007ff0e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff0e0`](#insn-007ff0e0) → [`00bdb0a0`](../00bdb/00bdb0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0a0` · 推定シンボル `None` · 推定型 `None`
- [`007ff0e8`](#insn-007ff0e8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff0f0`](#insn-007ff0f0) → [`007ff114`](#insn-007ff114) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff0f4`](#insn-007ff0f4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff0f8`](#insn-007ff0f8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff0fc`](#insn-007ff0fc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff100`](#insn-007ff100) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff104`](#insn-007ff104) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff108`](#insn-007ff108) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ff114`](#insn-007ff114) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007febe0`](#insn-007febe0)

~~~json
{
  "source": "007febe0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007febe4`](#insn-007febe4)

~~~json
{
  "source": "007febe4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007febe8`](#insn-007febe8)

~~~json
{
  "source": "007febe8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007febec`](#insn-007febec)

~~~json
{
  "source": "007febec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007febf0`](#insn-007febf0)

~~~json
{
  "source": "007febf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007febf4`](#insn-007febf4)

~~~json
{
  "source": "007febf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007febfc`](#insn-007febfc)

~~~json
{
  "source": "007febfc",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fec08`](#insn-007fec08)

~~~json
{
  "source": "007fec08",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fec0c`](#insn-007fec0c)

~~~json
{
  "source": "007fec0c",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fec10`](#insn-007fec10)

~~~json
{
  "source": "007fec10",
  "target": "007ff0e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fec28`](#insn-007fec28)

~~~json
{
  "source": "007fec28",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fec30`](#insn-007fec30)

~~~json
{
  "source": "007fec30",
  "target": "007fef04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fec38`](#insn-007fec38)

~~~json
{
  "source": "007fec38",
  "target": "007fef04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fec3c`](#insn-007fec3c)

~~~json
{
  "source": "007fec3c",
  "target": "007ff0e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fec60`](#insn-007fec60)

~~~json
{
  "source": "007fec60",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fec64`](#insn-007fec64)

~~~json
{
  "source": "007fec64",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fec70`](#insn-007fec70)

~~~json
{
  "source": "007fec70",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fec74`](#insn-007fec74)

~~~json
{
  "source": "007fec74",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fec78`](#insn-007fec78)

~~~json
{
  "source": "007fec78",
  "target": "007fe674",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fec7c`](#insn-007fec7c)

~~~json
{
  "source": "007fec7c",
  "target": "007fec90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fec88`](#insn-007fec88)

~~~json
{
  "source": "007fec88",
  "target": "007fec48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fec8c`](#insn-007fec8c)

~~~json
{
  "source": "007fec8c",
  "target": "007ff0e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fec90`](#insn-007fec90)

~~~json
{
  "source": "007fec90",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fec9c`](#insn-007fec9c)

~~~json
{
  "source": "007fec9c",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007feca4`](#insn-007feca4)

~~~json
{
  "source": "007feca4",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007feca8`](#insn-007feca8)

~~~json
{
  "source": "007feca8",
  "target": "007fed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fecc0`](#insn-007fecc0)

~~~json
{
  "source": "007fecc0",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007feccc`](#insn-007feccc)

~~~json
{
  "source": "007feccc",
  "target": "007fed4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fecd8`](#insn-007fecd8)

~~~json
{
  "source": "007fecd8",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fece0`](#insn-007fece0)

~~~json
{
  "source": "007fece0",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fed08`](#insn-007fed08)

~~~json
{
  "source": "007fed08",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fed0c`](#insn-007fed0c)

~~~json
{
  "source": "007fed0c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fed18`](#insn-007fed18)

~~~json
{
  "source": "007fed18",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fed1c`](#insn-007fed1c)

~~~json
{
  "source": "007fed1c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fed20`](#insn-007fed20)

~~~json
{
  "source": "007fed20",
  "target": "007fe674",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fed40`](#insn-007fed40)

~~~json
{
  "source": "007fed40",
  "target": "007fecec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fed44`](#insn-007fed44)

~~~json
{
  "source": "007fed44",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fed48`](#insn-007fed48)

~~~json
{
  "source": "007fed48",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fed54`](#insn-007fed54)

~~~json
{
  "source": "007fed54",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fed68`](#insn-007fed68)

~~~json
{
  "source": "007fed68",
  "target": "007fee34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fed70`](#insn-007fed70)

~~~json
{
  "source": "007fed70",
  "target": "007ff064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fed78`](#insn-007fed78)

~~~json
{
  "source": "007fed78",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fed94`](#insn-007fed94)

~~~json
{
  "source": "007fed94",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fed9c`](#insn-007fed9c)

~~~json
{
  "source": "007fed9c",
  "target": "007fee20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007feda0`](#insn-007feda0)

~~~json
{
  "source": "007feda0",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fedb0`](#insn-007fedb0)

~~~json
{
  "source": "007fedb0",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fede0`](#insn-007fede0)

~~~json
{
  "source": "007fede0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fede4`](#insn-007fede4)

~~~json
{
  "source": "007fede4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fedf0`](#insn-007fedf0)

~~~json
{
  "source": "007fedf0",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fedf4`](#insn-007fedf4)

~~~json
{
  "source": "007fedf4",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fedf8`](#insn-007fedf8)

~~~json
{
  "source": "007fedf8",
  "target": "007fe674",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fee14`](#insn-007fee14)

~~~json
{
  "source": "007fee14",
  "target": "007fedc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fee18`](#insn-007fee18)

~~~json
{
  "source": "007fee18",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fee1c`](#insn-007fee1c)

~~~json
{
  "source": "007fee1c",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fee4c`](#insn-007fee4c)

~~~json
{
  "source": "007fee4c",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fee58`](#insn-007fee58)

~~~json
{
  "source": "007fee58",
  "target": "007fc484",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fee74`](#insn-007fee74)

~~~json
{
  "source": "007fee74",
  "target": "007feeb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fee80`](#insn-007fee80)

~~~json
{
  "source": "007fee80",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fee84`](#insn-007fee84)

~~~json
{
  "source": "007fee84",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fee88`](#insn-007fee88)

~~~json
{
  "source": "007fee88",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fee9c`](#insn-007fee9c)

~~~json
{
  "source": "007fee9c",
  "target": "007febdc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007feea0`](#insn-007feea0)

~~~json
{
  "source": "007feea0",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007feea4`](#insn-007feea4)

~~~json
{
  "source": "007feea4",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007feeb4`](#insn-007feeb4)

~~~json
{
  "source": "007feeb4",
  "target": "007feef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007feeb8`](#insn-007feeb8)

~~~json
{
  "source": "007feeb8",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007feec0`](#insn-007feec0)

~~~json
{
  "source": "007feec0",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007feec8`](#insn-007feec8)

~~~json
{
  "source": "007feec8",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007feedc`](#insn-007feedc)

~~~json
{
  "source": "007feedc",
  "target": "007febdc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007feee0`](#insn-007feee0)

~~~json
{
  "source": "007feee0",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007feef0`](#insn-007feef0)

~~~json
{
  "source": "007feef0",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007feef8`](#insn-007feef8)

~~~json
{
  "source": "007feef8",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007feefc`](#insn-007feefc)

~~~json
{
  "source": "007feefc",
  "target": "007fec28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fef00`](#insn-007fef00)

~~~json
{
  "source": "007fef00",
  "target": "007ff0e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fef08`](#insn-007fef08)

~~~json
{
  "source": "007fef08",
  "target": "007fefbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fef0c`](#insn-007fef0c)

~~~json
{
  "source": "007fef0c",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fef14`](#insn-007fef14)

~~~json
{
  "source": "007fef14",
  "target": "007ff0e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fef18`](#insn-007fef18)

~~~json
{
  "source": "007fef18",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fef44`](#insn-007fef44)

~~~json
{
  "source": "007fef44",
  "target": "007fef20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fef54`](#insn-007fef54)

~~~json
{
  "source": "007fef54",
  "target": "007ff09c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fef70`](#insn-007fef70)

~~~json
{
  "source": "007fef70",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fef78`](#insn-007fef78)

~~~json
{
  "source": "007fef78",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fef84`](#insn-007fef84)

~~~json
{
  "source": "007fef84",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fef88`](#insn-007fef88)

~~~json
{
  "source": "007fef88",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fef8c`](#insn-007fef8c)

~~~json
{
  "source": "007fef8c",
  "target": "007fe674",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fefb4`](#insn-007fefb4)

~~~json
{
  "source": "007fefb4",
  "target": "007fef50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fefb8`](#insn-007fefb8)

~~~json
{
  "source": "007fefb8",
  "target": "007ff0e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fefbc`](#insn-007fefbc)

~~~json
{
  "source": "007fefbc",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fefc4`](#insn-007fefc4)

~~~json
{
  "source": "007fefc4",
  "target": "007ff0e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007feff0`](#insn-007feff0)

~~~json
{
  "source": "007feff0",
  "target": "007fefcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007feffc`](#insn-007feffc)

~~~json
{
  "source": "007feffc",
  "target": "007ff01c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff018`](#insn-007ff018)

~~~json
{
  "source": "007ff018",
  "target": "007ff0e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff020`](#insn-007ff020)

~~~json
{
  "source": "007ff020",
  "target": "007ff0cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff038`](#insn-007ff038)

~~~json
{
  "source": "007ff038",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff03c`](#insn-007ff03c)

~~~json
{
  "source": "007ff03c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff048`](#insn-007ff048)

~~~json
{
  "source": "007ff048",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff04c`](#insn-007ff04c)

~~~json
{
  "source": "007ff04c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff050`](#insn-007ff050)

~~~json
{
  "source": "007ff050",
  "target": "007fe674",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ff054`](#insn-007ff054)

~~~json
{
  "source": "007ff054",
  "target": "007ff000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff060`](#insn-007ff060)

~~~json
{
  "source": "007ff060",
  "target": "007ff008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff078`](#insn-007ff078)

~~~json
{
  "source": "007ff078",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff07c`](#insn-007ff07c)

~~~json
{
  "source": "007ff07c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff088`](#insn-007ff088)

~~~json
{
  "source": "007ff088",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff08c`](#insn-007ff08c)

~~~json
{
  "source": "007ff08c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff098`](#insn-007ff098)

~~~json
{
  "source": "007ff098",
  "target": "007ff0e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff0c4`](#insn-007ff0c4)

~~~json
{
  "source": "007ff0c4",
  "target": "007ff0a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff0c8`](#insn-007ff0c8)

~~~json
{
  "source": "007ff0c8",
  "target": "007ff0e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff0e0`](#insn-007ff0e0)

~~~json
{
  "source": "007ff0e0",
  "target": "00bdb0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ff0e8`](#insn-007ff0e8)

~~~json
{
  "source": "007ff0e8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff0f0`](#insn-007ff0f0)

~~~json
{
  "source": "007ff0f0",
  "target": "007ff114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff0f4`](#insn-007ff0f4)

~~~json
{
  "source": "007ff0f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff0f8`](#insn-007ff0f8)

~~~json
{
  "source": "007ff0f8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff0fc`](#insn-007ff0fc)

~~~json
{
  "source": "007ff0fc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff100`](#insn-007ff100)

~~~json
{
  "source": "007ff100",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff104`](#insn-007ff104)

~~~json
{
  "source": "007ff104",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff108`](#insn-007ff108)

~~~json
{
  "source": "007ff108",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ff114`](#insn-007ff114)

~~~json
{
  "source": "007ff114",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
