# 00b2abcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b2a7a4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a7a4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0037.md#compare-ac7e0152b2e934ce249467542e4c4d43)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b2ac68`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2ac68.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0037.md#compare-0ba0518c28c856d25c826b33acdca748)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b2abcc",
  "name": "FUN_00b2abcc",
  "size": 492,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9464a69311f1457bc9e77a127fc18a6d32f099b4dcbf42a1b2d2d90bbd9ea61d",
  "source_text_sha256": "9464a69311f1457bc9e77a127fc18a6d32f099b4dcbf42a1b2d2d90bbd9ea61d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b2abcc",
        "00b2adb3"
      ],
      [
        "00b2add8",
        "00b2addb"
      ]
    ],
    "bytes_sha256": "e17572b8e564cec6157139f15bbc7e09fed18bdd68e2970bfb853559b2449c8e",
    "instruction_count": 123,
    "instruction_bytes": 492,
    "body_bytes": 492,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b1f428](../00b1f/00b1f428.md)

## 呼び出し先

- [00440ec0](../00440/00440ec0.md)
- [0054075c](../00540/0054075c.md)
- [00794b6c](../00794/00794b6c.md)
- [0080da5c](../0080d/0080da5c.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2596 bytes

~~~c

long FUN_00b2abcc(long *param_1,long *param_2)

{
  ulong uVar1;
  long lVar2;
  long lVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  long lVar6;
  byte *pbVar7;
  long lVar8;
  ulong uVar9;
  undefined8 *puVar10;
  byte *pbVar11;
  byte *pbVar12;
  void *local_80;
  undefined8 *local_78;
  undefined8 *local_70;
  void *pvStack_68;
  long *local_60;
  long local_58;
  
  lVar3 = tpidr_el0;
  local_58 = *(long *)(lVar3 + 0x28);
  lVar6 = param_1[1] - *param_1 >> 3;
  uVar1 = lVar6 * -0x5555555555555555 + 1;
  if (uVar1 < 0xaaaaaaaaaaaaaab) {
    local_60 = param_1 + 2;
    lVar8 = *local_60 - *param_1 >> 3;
    uVar9 = lVar8 * 0x5555555555555556;
    if (uVar9 < uVar1 || uVar9 - uVar1 == 0) {
      uVar9 = uVar1;
    }
    if (0x555555555555554 < (ulong)(lVar8 * -0x5555555555555555)) {
      uVar9 = 0xaaaaaaaaaaaaaaa;
    }
    if (uVar9 == 0) {
      local_80 = (void *)0x0;
    }
    else {
      if (0xaaaaaaaaaaaaaaa < uVar9) goto LAB_00b2ada0;
      local_80 = (void *)_Znwm(uVar9 * 0x18);
    }
    lVar8 = *param_2;
    lVar2 = param_2[1];
    local_78 = (undefined8 *)((long)local_80 + lVar6 * 8);
    pvStack_68 = (void *)((long)local_80 + uVar9 * 0x18);
    local_78[1] = 0;
    local_78[2] = 0;
    *local_78 = 0;
    local_70 = local_78;
    FUN_0054075c(local_78,lVar8,lVar2,(lVar2 - lVar8 >> 3) * -0x5555555555555555);
    local_70 = local_70 + 3;
    FUN_0080da5c(param_1,&local_80);
    puVar5 = local_78;
    lVar6 = param_1[1];
    while (puVar4 = local_70, puVar4 != puVar5) {
      puVar10 = puVar4 + -3;
      pbVar11 = (byte *)*puVar10;
      local_70 = puVar10;
      if (pbVar11 != (byte *)0x0) {
        pbVar7 = (byte *)puVar4[-2];
        pbVar12 = pbVar11;
        if (pbVar7 != pbVar11) {
          do {
            pbVar12 = pbVar7 + -0x18;
            if ((*pbVar12 & 1) != 0) {
              _ZdlPv(*(void **)(pbVar7 + -8));
            }
            pbVar7 = pbVar12;
          } while (pbVar12 != pbVar11);
          pbVar12 = (byte *)*puVar10;
        }
        puVar4[-2] = pbVar11;
        _ZdlPv(pbVar12);
      }
    }
    local_70 = puVar4;
    if (local_80 != (void *)0x0) {
      _ZdlPv(local_80);
    }
    if (*(long *)(lVar3 + 0x28) == local_58) {
      return lVar6;
    }
  }
  else {
    if (*(long *)(lVar3 + 0x28) != local_58) goto LAB_00b2add8;
    FUN_00794b6c(param_1);
LAB_00b2ada0:
    if (*(long *)(lVar3 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
      FUN_00440ec0();
    }
  }
LAB_00b2add8:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b2abcc"></a> `00b2abcc` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00b2abd0"></a> `00b2abd0` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b2abd4"></a> `00b2abd4` | `f9 23 00 f9` | str x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b2abd8"></a> `00b2abd8` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b2abdc"></a> `00b2abdc` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b2abe0"></a> `00b2abe0` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b2abe4"></a> `00b2abe4` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b2abe8"></a> `00b2abe8` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b2abec"></a> `00b2abec` | `eb f3 01 b2` | orr x11,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00b2abf0"></a> `00b2abf0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b2abf4"></a> `00b2abf4` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00b2abf8"></a> `00b2abf8` | `6b 55 95 f2` | movk x11,#0xaaab | `FALL_THROUGH`
<a id="insn-00b2abfc"></a> `00b2abfc` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00b2ac00"></a> `00b2ac00` | `0a 20 40 a9` | ldp x10,x8,[x0] | `FALL_THROUGH`
<a id="insn-00b2ac04"></a> `00b2ac04` | `08 01 0a cb` | sub x8,x8,x10 | `FALL_THROUGH`
<a id="insn-00b2ac08"></a> `00b2ac08` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00b2ac0c"></a> `00b2ac0c` | `16 7d 0b 9b` | mul x22,x8,x11 | `FALL_THROUGH`
<a id="insn-00b2ac10"></a> `00b2ac10` | `e8 f3 01 b2` | orr x8,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00b2ac14"></a> `00b2ac14` | `48 55 e1 f2` | movk x8,#0xaaa, LSL #48 | `FALL_THROUGH`
<a id="insn-00b2ac18"></a> `00b2ac18` | `c9 06 00 91` | add x9,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00b2ac1c"></a> `00b2ac1c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00b2ac20"></a> `00b2ac20` | `48 0b 00 54` | b.hi 0x00b2ad88 | `CONDITIONAL_JUMP`
<a id="insn-00b2ac24"></a> `00b2ac24` | `ec 03 13 aa` | mov x12,x19 | `FALL_THROUGH`
<a id="insn-00b2ac28"></a> `00b2ac28` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00b2ac2c"></a> `00b2ac2c` | `8d 0d 41 f8` | ldr x13,[x12, #0x10]! | `FALL_THROUGH`
<a id="insn-00b2ac30"></a> `00b2ac30` | `ec 13 00 f9` | str x12,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b2ac34"></a> `00b2ac34` | `aa 01 0a cb` | sub x10,x13,x10 | `FALL_THROUGH`
<a id="insn-00b2ac38"></a> `00b2ac38` | `ed f3 00 b2` | orr x13,xzr,#0x5555555555555555 | `FALL_THROUGH`
<a id="insn-00b2ac3c"></a> `00b2ac3c` | `4a fd 43 93` | asr x10,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00b2ac40"></a> `00b2ac40` | `ad aa e0 f2` | movk x13,#0x555, LSL #48 | `FALL_THROUGH`
<a id="insn-00b2ac44"></a> `00b2ac44` | `4a 7d 0b 9b` | mul x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00b2ac48"></a> `00b2ac48` | `4b f9 7f d3` | lsl x11,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00b2ac4c"></a> `00b2ac4c` | `7f 01 09 eb` | cmp x11,x9 | `FALL_THROUGH`
<a id="insn-00b2ac50"></a> `00b2ac50` | `69 81 89 9a` | csel x9,x11,x9,hi | `FALL_THROUGH`
<a id="insn-00b2ac54"></a> `00b2ac54` | `5f 01 0d eb` | cmp x10,x13 | `FALL_THROUGH`
<a id="insn-00b2ac58"></a> `00b2ac58` | `37 31 88 9a` | csel x23,x9,x8,cc | `FALL_THROUGH`
<a id="insn-00b2ac5c"></a> `00b2ac5c` | `f7 00 00 b4` | cbz x23,0x00b2ac78 | `CONDITIONAL_JUMP`
<a id="insn-00b2ac60"></a> `00b2ac60` | `ff 02 08 eb` | cmp x23,x8 | `FALL_THROUGH`
<a id="insn-00b2ac64"></a> `00b2ac64` | `e8 09 00 54` | b.hi 0x00b2ada0 | `CONDITIONAL_JUMP`
<a id="insn-00b2ac68"></a> `00b2ac68` | `e8 06 17 8b` | add x8,x23,x23, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00b2ac6c"></a> `00b2ac6c` | `00 f1 7d d3` | lsl x0,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00b2ac70"></a> `00b2ac70` | `88 b4 04 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00b2ac74"></a> `00b2ac74` | `02 00 00 14` | b 0x00b2ac7c | `UNCONDITIONAL_JUMP`
<a id="insn-00b2ac78"></a> `00b2ac78` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00b2ac7c"></a> `00b2ac7c` | `09 03 80 52` | mov w9,#0x18 | `FALL_THROUGH`
<a id="insn-00b2ac80"></a> `00b2ac80` | `81 0a 40 a9` | ldp x1,x2,[x20] | `FALL_THROUGH`
<a id="insn-00b2ac84"></a> `00b2ac84` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00b2ac88"></a> `00b2ac88` | `c8 02 09 9b` | madd x8,x22,x9,x0 | `FALL_THROUGH`
<a id="insn-00b2ac8c"></a> `00b2ac8c` | `eb f3 01 b2` | orr x11,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00b2ac90"></a> `00b2ac90` | `6b 55 95 f2` | movk x11,#0xaaab | `FALL_THROUGH`
<a id="insn-00b2ac94"></a> `00b2ac94` | `e9 02 09 9b` | madd x9,x23,x9,x0 | `FALL_THROUGH`
<a id="insn-00b2ac98"></a> `00b2ac98` | `4a 00 01 cb` | sub x10,x2,x1 | `FALL_THROUGH`
<a id="insn-00b2ac9c"></a> `00b2ac9c` | `4a fd 43 93` | asr x10,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00b2aca0"></a> `00b2aca0` | `e0 23 00 a9` | stp x0,x8,[sp] | `FALL_THROUGH`
<a id="insn-00b2aca4"></a> `00b2aca4` | `43 7d 0b 9b` | mul x3,x10,x11 | `FALL_THROUGH`
<a id="insn-00b2aca8"></a> `00b2aca8` | `1f fd 00 a9` | stp xzr,xzr,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b2acac"></a> `00b2acac` | `e8 27 01 a9` | stp x8,x9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b2acb0"></a> `00b2acb0` | `1f 01 00 f9` | str xzr,[x8] | `FALL_THROUGH`
<a id="insn-00b2acb4"></a> `00b2acb4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b2acb8"></a> `00b2acb8` | `a9 56 e8 97` | bl 0x0054075c | `UNCONDITIONAL_CALL`
<a id="insn-00b2acbc"></a> `00b2acbc` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b2acc0"></a> `00b2acc0` | `08 61 00 91` | add x8,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00b2acc4"></a> `00b2acc4` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b2acc8"></a> `00b2acc8` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00b2accc"></a> `00b2accc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b2acd0"></a> `00b2acd0` | `63 8b f3 97` | bl 0x0080da5c | `UNCONDITIONAL_CALL`
<a id="insn-00b2acd4"></a> `00b2acd4` | `f4 db 40 a9` | ldp x20,x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b2acd8"></a> `00b2acd8` | `73 06 40 f9` | ldr x19,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b2acdc"></a> `00b2acdc` | `df 02 14 eb` | cmp x22,x20 | `FALL_THROUGH`
<a id="insn-00b2ace0"></a> `00b2ace0` | `60 03 00 54` | b.eq 0x00b2ad4c | `CONDITIONAL_JUMP`
<a id="insn-00b2ace4"></a> `00b2ace4` | `f7 03 16 aa` | mov x23,x22 | `FALL_THROUGH`
<a id="insn-00b2ace8"></a> `00b2ace8` | `08 00 00 14` | b 0x00b2ad08 | `UNCONDITIONAL_JUMP`
<a id="insn-00b2acec"></a> `00b2acec` | `e0 02 40 f9` | ldr x0,[x23] | `FALL_THROUGH`
<a id="insn-00b2acf0"></a> `00b2acf0` | `d8 02 1f f8` | stur x24,[x22, #-0x10] | `FALL_THROUGH`
<a id="insn-00b2acf4"></a> `00b2acf4` | `6f b4 04 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00b2acf8"></a> `00b2acf8` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b2acfc"></a> `00b2acfc` | `ff 02 14 eb` | cmp x23,x20 | `FALL_THROUGH`
<a id="insn-00b2ad00"></a> `00b2ad00` | `f6 03 17 aa` | mov x22,x23 | `FALL_THROUGH`
<a id="insn-00b2ad04"></a> `00b2ad04` | `40 02 00 54` | b.eq 0x00b2ad4c | `CONDITIONAL_JUMP`
<a id="insn-00b2ad08"></a> `00b2ad08` | `f8 8e 5e f8` | ldr x24,[x23, #-0x18]! | `FALL_THROUGH`
<a id="insn-00b2ad0c"></a> `00b2ad0c` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b2ad10"></a> `00b2ad10` | `78 ff ff b4` | cbz x24,0x00b2acfc | `CONDITIONAL_JUMP`
<a id="insn-00b2ad14"></a> `00b2ad14` | `c8 02 5f f8` | ldur x8,[x22, #-0x10] | `FALL_THROUGH`
<a id="insn-00b2ad18"></a> `00b2ad18` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00b2ad1c"></a> `00b2ad1c` | `1f 01 18 eb` | cmp x8,x24 | `FALL_THROUGH`
<a id="insn-00b2ad20"></a> `00b2ad20` | `80 fe ff 54` | b.eq 0x00b2acf0 | `CONDITIONAL_JUMP`
<a id="insn-00b2ad24"></a> `00b2ad24` | `f9 03 08 aa` | mov x25,x8 | `FALL_THROUGH`
<a id="insn-00b2ad28"></a> `00b2ad28` | `04 00 00 14` | b 0x00b2ad38 | `UNCONDITIONAL_JUMP`
<a id="insn-00b2ad2c"></a> `00b2ad2c` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00b2ad30"></a> `00b2ad30` | `e8 03 19 aa` | mov x8,x25 | `FALL_THROUGH`
<a id="insn-00b2ad34"></a> `00b2ad34` | `c0 fd ff 54` | b.eq 0x00b2acec | `CONDITIONAL_JUMP`
<a id="insn-00b2ad38"></a> `00b2ad38` | `29 8f 5e 38` | ldrb w9,[x25, #-0x18]! | `FALL_THROUGH`
<a id="insn-00b2ad3c"></a> `00b2ad3c` | `89 ff 07 36` | tbz w9,#0x0,0x00b2ad2c | `CONDITIONAL_JUMP`
<a id="insn-00b2ad40"></a> `00b2ad40` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00b2ad44"></a> `00b2ad44` | `5b b4 04 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00b2ad48"></a> `00b2ad48` | `f9 ff ff 17` | b 0x00b2ad2c | `UNCONDITIONAL_JUMP`
<a id="insn-00b2ad4c"></a> `00b2ad4c` | `e0 03 40 f9` | ldr x0,[sp] | `FALL_THROUGH`
<a id="insn-00b2ad50"></a> `00b2ad50` | `40 00 00 b4` | cbz x0,0x00b2ad58 | `CONDITIONAL_JUMP`
<a id="insn-00b2ad54"></a> `00b2ad54` | `57 b4 04 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00b2ad58"></a> `00b2ad58` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00b2ad5c"></a> `00b2ad5c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00b2ad60"></a> `00b2ad60` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b2ad64"></a> `00b2ad64` | `a1 03 00 54` | b.ne 0x00b2add8 | `CONDITIONAL_JUMP`
<a id="insn-00b2ad68"></a> `00b2ad68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b2ad6c"></a> `00b2ad6c` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b2ad70"></a> `00b2ad70` | `f9 23 40 f9` | ldr x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b2ad74"></a> `00b2ad74` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b2ad78"></a> `00b2ad78` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b2ad7c"></a> `00b2ad7c` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b2ad80"></a> `00b2ad80` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00b2ad84"></a> `00b2ad84` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b2ad88"></a> `00b2ad88` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00b2ad8c"></a> `00b2ad8c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00b2ad90"></a> `00b2ad90` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b2ad94"></a> `00b2ad94` | `21 02 00 54` | b.ne 0x00b2add8 | `CONDITIONAL_JUMP`
<a id="insn-00b2ad98"></a> `00b2ad98` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b2ad9c"></a> `00b2ad9c` | `74 a7 f1 97` | bl 0x00794b6c | `UNCONDITIONAL_CALL`
<a id="insn-00b2ada0"></a> `00b2ada0` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00b2ada4"></a> `00b2ada4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00b2ada8"></a> `00b2ada8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b2adac"></a> `00b2adac` | `61 01 00 54` | b.ne 0x00b2add8 | `CONDITIONAL_JUMP`
<a id="insn-00b2adb0"></a> `00b2adb0` | `44 58 e4 97` | bl 0x00440ec0 | `CALL_TERMINATOR`
<a id="insn-00b2add8"></a> `00b2add8` | `42 b4 04 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b2abcc`](#insn-00b2abcc) 範囲 `[['00b2abcc', '00b2ac23']]`
  - `CONDITIONAL_JUMP` [`00b2ac20`](#insn-00b2ac20) → [`00b2ad88`](#insn-00b2ad88)
  - `FALL_THROUGH` [`00b2ac20`](#insn-00b2ac20) → [`00b2ac24`](#insn-00b2ac24)
- ブロック [`00b2ac24`](#insn-00b2ac24) 範囲 `[['00b2ac24', '00b2ac5f']]`
  - `CONDITIONAL_JUMP` [`00b2ac5c`](#insn-00b2ac5c) → [`00b2ac78`](#insn-00b2ac78)
  - `FALL_THROUGH` [`00b2ac5c`](#insn-00b2ac5c) → [`00b2ac60`](#insn-00b2ac60)
- ブロック [`00b2ac60`](#insn-00b2ac60) 範囲 `[['00b2ac60', '00b2ac67']]`
  - `CONDITIONAL_JUMP` [`00b2ac64`](#insn-00b2ac64) → [`00b2ada0`](#insn-00b2ada0)
  - `FALL_THROUGH` [`00b2ac64`](#insn-00b2ac64) → [`00b2ac68`](#insn-00b2ac68)
- ブロック [`00b2ac68`](#insn-00b2ac68) 範囲 `[['00b2ac68', '00b2ac77']]`
  - `UNCONDITIONAL_JUMP` [`00b2ac74`](#insn-00b2ac74) → [`00b2ac7c`](#insn-00b2ac7c)
- ブロック [`00b2ac78`](#insn-00b2ac78) 範囲 `[['00b2ac78', '00b2ac7b']]`
  - `FALL_THROUGH` [`00b2ac78`](#insn-00b2ac78) → [`00b2ac7c`](#insn-00b2ac7c)
- ブロック [`00b2ac7c`](#insn-00b2ac7c) 範囲 `[['00b2ac7c', '00b2ace3']]`
  - `CONDITIONAL_JUMP` [`00b2ace0`](#insn-00b2ace0) → [`00b2ad4c`](#insn-00b2ad4c)
  - `FALL_THROUGH` [`00b2ace0`](#insn-00b2ace0) → [`00b2ace4`](#insn-00b2ace4)
- ブロック [`00b2ace4`](#insn-00b2ace4) 範囲 `[['00b2ace4', '00b2aceb']]`
  - `UNCONDITIONAL_JUMP` [`00b2ace8`](#insn-00b2ace8) → [`00b2ad08`](#insn-00b2ad08)
- ブロック [`00b2acec`](#insn-00b2acec) 範囲 `[['00b2acec', '00b2acef']]`
  - `FALL_THROUGH` [`00b2acec`](#insn-00b2acec) → [`00b2acf0`](#insn-00b2acf0)
- ブロック [`00b2acf0`](#insn-00b2acf0) 範囲 `[['00b2acf0', '00b2acfb']]`
  - `FALL_THROUGH` [`00b2acf8`](#insn-00b2acf8) → [`00b2acfc`](#insn-00b2acfc)
- ブロック [`00b2acfc`](#insn-00b2acfc) 範囲 `[['00b2acfc', '00b2ad07']]`
  - `CONDITIONAL_JUMP` [`00b2ad04`](#insn-00b2ad04) → [`00b2ad4c`](#insn-00b2ad4c)
  - `FALL_THROUGH` [`00b2ad04`](#insn-00b2ad04) → [`00b2ad08`](#insn-00b2ad08)
- ブロック [`00b2ad08`](#insn-00b2ad08) 範囲 `[['00b2ad08', '00b2ad13']]`
  - `CONDITIONAL_JUMP` [`00b2ad10`](#insn-00b2ad10) → [`00b2acfc`](#insn-00b2acfc)
  - `FALL_THROUGH` [`00b2ad10`](#insn-00b2ad10) → [`00b2ad14`](#insn-00b2ad14)
- ブロック [`00b2ad14`](#insn-00b2ad14) 範囲 `[['00b2ad14', '00b2ad23']]`
  - `CONDITIONAL_JUMP` [`00b2ad20`](#insn-00b2ad20) → [`00b2acf0`](#insn-00b2acf0)
  - `FALL_THROUGH` [`00b2ad20`](#insn-00b2ad20) → [`00b2ad24`](#insn-00b2ad24)
- ブロック [`00b2ad24`](#insn-00b2ad24) 範囲 `[['00b2ad24', '00b2ad2b']]`
  - `UNCONDITIONAL_JUMP` [`00b2ad28`](#insn-00b2ad28) → [`00b2ad38`](#insn-00b2ad38)
- ブロック [`00b2ad2c`](#insn-00b2ad2c) 範囲 `[['00b2ad2c', '00b2ad37']]`
  - `CONDITIONAL_JUMP` [`00b2ad34`](#insn-00b2ad34) → [`00b2acec`](#insn-00b2acec)
  - `FALL_THROUGH` [`00b2ad34`](#insn-00b2ad34) → [`00b2ad38`](#insn-00b2ad38)
- ブロック [`00b2ad38`](#insn-00b2ad38) 範囲 `[['00b2ad38', '00b2ad3f']]`
  - `CONDITIONAL_JUMP` [`00b2ad3c`](#insn-00b2ad3c) → [`00b2ad2c`](#insn-00b2ad2c)
  - `FALL_THROUGH` [`00b2ad3c`](#insn-00b2ad3c) → [`00b2ad40`](#insn-00b2ad40)
- ブロック [`00b2ad40`](#insn-00b2ad40) 範囲 `[['00b2ad40', '00b2ad4b']]`
  - `UNCONDITIONAL_JUMP` [`00b2ad48`](#insn-00b2ad48) → [`00b2ad2c`](#insn-00b2ad2c)
- ブロック [`00b2ad4c`](#insn-00b2ad4c) 範囲 `[['00b2ad4c', '00b2ad53']]`
  - `CONDITIONAL_JUMP` [`00b2ad50`](#insn-00b2ad50) → [`00b2ad58`](#insn-00b2ad58)
  - `FALL_THROUGH` [`00b2ad50`](#insn-00b2ad50) → [`00b2ad54`](#insn-00b2ad54)
- ブロック [`00b2ad54`](#insn-00b2ad54) 範囲 `[['00b2ad54', '00b2ad57']]`
  - `FALL_THROUGH` [`00b2ad54`](#insn-00b2ad54) → [`00b2ad58`](#insn-00b2ad58)
- ブロック [`00b2ad58`](#insn-00b2ad58) 範囲 `[['00b2ad58', '00b2ad67']]`
  - `CONDITIONAL_JUMP` [`00b2ad64`](#insn-00b2ad64) → [`00b2add8`](#insn-00b2add8)
  - `FALL_THROUGH` [`00b2ad64`](#insn-00b2ad64) → [`00b2ad68`](#insn-00b2ad68)
- ブロック [`00b2ad68`](#insn-00b2ad68) 範囲 `[['00b2ad68', '00b2ad87']]`
- ブロック [`00b2ad88`](#insn-00b2ad88) 範囲 `[['00b2ad88', '00b2ad97']]`
  - `CONDITIONAL_JUMP` [`00b2ad94`](#insn-00b2ad94) → [`00b2add8`](#insn-00b2add8)
  - `FALL_THROUGH` [`00b2ad94`](#insn-00b2ad94) → [`00b2ad98`](#insn-00b2ad98)
- ブロック [`00b2ad98`](#insn-00b2ad98) 範囲 `[['00b2ad98', '00b2ad9f']]`
  - `FALL_THROUGH` [`00b2ad9c`](#insn-00b2ad9c) → [`00b2ada0`](#insn-00b2ada0)
- ブロック [`00b2ada0`](#insn-00b2ada0) 範囲 `[['00b2ada0', '00b2adaf']]`
  - `CONDITIONAL_JUMP` [`00b2adac`](#insn-00b2adac) → [`00b2add8`](#insn-00b2add8)
  - `FALL_THROUGH` [`00b2adac`](#insn-00b2adac) → [`00b2adb0`](#insn-00b2adb0)
- ブロック [`00b2adb0`](#insn-00b2adb0) 範囲 `[['00b2adb0', '00b2adb3']]`
- ブロック [`00b2add8`](#insn-00b2add8) 範囲 `[['00b2add8', '00b2addb']]`

## 命令位置別の参照

- [`00b2abd0`](#insn-00b2abd0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2abd4`](#insn-00b2abd4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2abd8`](#insn-00b2abd8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2abdc`](#insn-00b2abdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2abe0`](#insn-00b2abe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2abfc`](#insn-00b2abfc) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ac20`](#insn-00b2ac20) → [`00b2ad88`](#insn-00b2ad88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ac30`](#insn-00b2ac30) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ac5c`](#insn-00b2ac5c) → [`00b2ac78`](#insn-00b2ac78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ac64`](#insn-00b2ac64) → [`00b2ada0`](#insn-00b2ada0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ac70`](#insn-00b2ac70) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00b2ac74`](#insn-00b2ac74) → [`00b2ac7c`](#insn-00b2ac7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2aca0`](#insn-00b2aca0) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2acac`](#insn-00b2acac) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2acb8`](#insn-00b2acb8) → [`0054075c`](../00540/0054075c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0054075c` · 推定シンボル `None` · 推定型 `None`
- [`00b2acbc`](#insn-00b2acbc) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2acc4`](#insn-00b2acc4) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2acd0`](#insn-00b2acd0) → [`0080da5c`](../0080d/0080da5c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0080da5c` · 推定シンボル `None` · 推定型 `None`
- [`00b2acd4`](#insn-00b2acd4) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ace0`](#insn-00b2ace0) → [`00b2ad4c`](#insn-00b2ad4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ace8`](#insn-00b2ace8) → [`00b2ad08`](#insn-00b2ad08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2acf4`](#insn-00b2acf4) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00b2acf8`](#insn-00b2acf8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ad04`](#insn-00b2ad04) → [`00b2ad4c`](#insn-00b2ad4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ad0c`](#insn-00b2ad0c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ad10`](#insn-00b2ad10) → [`00b2acfc`](#insn-00b2acfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ad20`](#insn-00b2ad20) → [`00b2acf0`](#insn-00b2acf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ad28`](#insn-00b2ad28) → [`00b2ad38`](#insn-00b2ad38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ad34`](#insn-00b2ad34) → [`00b2acec`](#insn-00b2acec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ad3c`](#insn-00b2ad3c) → [`00b2ad2c`](#insn-00b2ad2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ad44`](#insn-00b2ad44) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00b2ad48`](#insn-00b2ad48) → [`00b2ad2c`](#insn-00b2ad2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ad4c`](#insn-00b2ad4c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ad50`](#insn-00b2ad50) → [`00b2ad58`](#insn-00b2ad58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ad54`](#insn-00b2ad54) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00b2ad5c`](#insn-00b2ad5c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ad64`](#insn-00b2ad64) → [`00b2add8`](#insn-00b2add8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ad6c`](#insn-00b2ad6c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ad70`](#insn-00b2ad70) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ad74`](#insn-00b2ad74) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ad78`](#insn-00b2ad78) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ad7c`](#insn-00b2ad7c) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ad8c`](#insn-00b2ad8c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ad94`](#insn-00b2ad94) → [`00b2add8`](#insn-00b2add8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ad9c`](#insn-00b2ad9c) → [`00794b6c`](../00794/00794b6c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00794b6c` · 推定シンボル `None` · 推定型 `None`
- [`00b2ada4`](#insn-00b2ada4) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2adac`](#insn-00b2adac) → [`00b2add8`](#insn-00b2add8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2adb0`](#insn-00b2adb0) → [`00440ec0`](../00440/00440ec0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00440ec0` · 推定シンボル `None` · 推定型 `None`
- [`00b2add8`](#insn-00b2add8) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b2abd0`](#insn-00b2abd0)

~~~json
{
  "source": "00b2abd0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2abd4`](#insn-00b2abd4)

~~~json
{
  "source": "00b2abd4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2abd8`](#insn-00b2abd8)

~~~json
{
  "source": "00b2abd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2abdc`](#insn-00b2abdc)

~~~json
{
  "source": "00b2abdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2abe0`](#insn-00b2abe0)

~~~json
{
  "source": "00b2abe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2abfc`](#insn-00b2abfc)

~~~json
{
  "source": "00b2abfc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ac20`](#insn-00b2ac20)

~~~json
{
  "source": "00b2ac20",
  "target": "00b2ad88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ac30`](#insn-00b2ac30)

~~~json
{
  "source": "00b2ac30",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ac5c`](#insn-00b2ac5c)

~~~json
{
  "source": "00b2ac5c",
  "target": "00b2ac78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ac64`](#insn-00b2ac64)

~~~json
{
  "source": "00b2ac64",
  "target": "00b2ada0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ac70`](#insn-00b2ac70)

~~~json
{
  "source": "00b2ac70",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2ac74`](#insn-00b2ac74)

~~~json
{
  "source": "00b2ac74",
  "target": "00b2ac7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2aca0`](#insn-00b2aca0)

~~~json
{
  "source": "00b2aca0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2acac`](#insn-00b2acac)

~~~json
{
  "source": "00b2acac",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2acb8`](#insn-00b2acb8)

~~~json
{
  "source": "00b2acb8",
  "target": "0054075c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2acbc`](#insn-00b2acbc)

~~~json
{
  "source": "00b2acbc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2acc4`](#insn-00b2acc4)

~~~json
{
  "source": "00b2acc4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2acd0`](#insn-00b2acd0)

~~~json
{
  "source": "00b2acd0",
  "target": "0080da5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2acd4`](#insn-00b2acd4)

~~~json
{
  "source": "00b2acd4",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ace0`](#insn-00b2ace0)

~~~json
{
  "source": "00b2ace0",
  "target": "00b2ad4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ace8`](#insn-00b2ace8)

~~~json
{
  "source": "00b2ace8",
  "target": "00b2ad08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2acf4`](#insn-00b2acf4)

~~~json
{
  "source": "00b2acf4",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2acf8`](#insn-00b2acf8)

~~~json
{
  "source": "00b2acf8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ad04`](#insn-00b2ad04)

~~~json
{
  "source": "00b2ad04",
  "target": "00b2ad4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ad0c`](#insn-00b2ad0c)

~~~json
{
  "source": "00b2ad0c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ad10`](#insn-00b2ad10)

~~~json
{
  "source": "00b2ad10",
  "target": "00b2acfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ad20`](#insn-00b2ad20)

~~~json
{
  "source": "00b2ad20",
  "target": "00b2acf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ad28`](#insn-00b2ad28)

~~~json
{
  "source": "00b2ad28",
  "target": "00b2ad38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ad34`](#insn-00b2ad34)

~~~json
{
  "source": "00b2ad34",
  "target": "00b2acec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ad3c`](#insn-00b2ad3c)

~~~json
{
  "source": "00b2ad3c",
  "target": "00b2ad2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ad44`](#insn-00b2ad44)

~~~json
{
  "source": "00b2ad44",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2ad48`](#insn-00b2ad48)

~~~json
{
  "source": "00b2ad48",
  "target": "00b2ad2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ad4c`](#insn-00b2ad4c)

~~~json
{
  "source": "00b2ad4c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ad50`](#insn-00b2ad50)

~~~json
{
  "source": "00b2ad50",
  "target": "00b2ad58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ad54`](#insn-00b2ad54)

~~~json
{
  "source": "00b2ad54",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2ad5c`](#insn-00b2ad5c)

~~~json
{
  "source": "00b2ad5c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ad64`](#insn-00b2ad64)

~~~json
{
  "source": "00b2ad64",
  "target": "00b2add8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ad6c`](#insn-00b2ad6c)

~~~json
{
  "source": "00b2ad6c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ad70`](#insn-00b2ad70)

~~~json
{
  "source": "00b2ad70",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ad74`](#insn-00b2ad74)

~~~json
{
  "source": "00b2ad74",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ad78`](#insn-00b2ad78)

~~~json
{
  "source": "00b2ad78",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ad7c`](#insn-00b2ad7c)

~~~json
{
  "source": "00b2ad7c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ad8c`](#insn-00b2ad8c)

~~~json
{
  "source": "00b2ad8c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ad94`](#insn-00b2ad94)

~~~json
{
  "source": "00b2ad94",
  "target": "00b2add8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ad9c`](#insn-00b2ad9c)

~~~json
{
  "source": "00b2ad9c",
  "target": "00794b6c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2ada4`](#insn-00b2ada4)

~~~json
{
  "source": "00b2ada4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2adac`](#insn-00b2adac)

~~~json
{
  "source": "00b2adac",
  "target": "00b2add8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2adb0`](#insn-00b2adb0)

~~~json
{
  "source": "00b2adb0",
  "target": "00440ec0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2add8`](#insn-00b2add8)

~~~json
{
  "source": "00b2add8",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
