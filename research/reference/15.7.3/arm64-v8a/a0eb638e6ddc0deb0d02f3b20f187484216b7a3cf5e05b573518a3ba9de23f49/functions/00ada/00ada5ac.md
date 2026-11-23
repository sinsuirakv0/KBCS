# 00ada5ac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00ada4e4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ada/00ada4e4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-9c31b2e250ba322196b7a927bdbf9774)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00ada5f0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ada/00ada5f0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0060.md#compare-366210fb94ed83d842edd2ef92279d5c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ada5ac",
  "name": "FUN_00ada5ac",
  "size": 396,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "63c02477a73bfe31d139b138e323c4fa4fdfb1c16f29d87e8b2593199a804120",
  "source_text_sha256": "63c02477a73bfe31d139b138e323c4fa4fdfb1c16f29d87e8b2593199a804120",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ada5ac",
        "00ada733"
      ],
      [
        "00ada770",
        "00ada773"
      ]
    ],
    "bytes_sha256": "3e008563ec816cbe618050e8ef5235e5929c3c50eb57d4d041465e24796dfb0b",
    "instruction_count": 99,
    "instruction_bytes": 396,
    "body_bytes": 396,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [0085e130](../0085e/0085e130.md)
- [0085fc1c](../0085f/0085fc1c.md)
- [008710cc](../00871/008710cc.md)
- [00879ea8](../00879/00879ea8.md)

## 呼び出し先

- [00551e14](../00551/00551e14.md)
- [00565f94](../00565/00565f94.md)
- [0056626c](../00566/0056626c.md)
- [00566284](../00566/00566284.md)
- [00566448](../00566/00566448.md)
- [00566978](../00566/00566978.md)
- [00adb874](../00adb/00adb874.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)

## 関連文字列（未確認候補）

~~~text
"tapjoyGetCurrencyBalance"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2143 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00ada5ac(long *param_1)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  ulong uVar6;
  long *plVar7;
  ulong *puVar8;
  undefined8 uVar9;
  long lVar10;
  byte local_90 [16];
  void *local_80;
  long local_78;
  ulong local_70;
  undefined8 uStack_68;
  char *local_60;
  ulong *local_50;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  uVar4 = FUN_00565f94();
  uVar5 = FUN_00566284();
  local_60 = (char *)_Znwm(0x20);
  uVar3 = s_tapjoyGetCurrencyBalance_00294121._16_8_;
  uVar2 = s_tapjoyGetCurrencyBalance_00294121._8_8_;
  uVar9 = s_tapjoyGetCurrencyBalance_00294121._0_8_;
  local_60[0x18] = '\0';
  *(undefined8 *)(local_60 + 0x10) = uVar3;
  *(undefined8 *)(local_60 + 8) = uVar2;
  *(undefined8 *)local_60 = uVar9;
  local_90[0] = 6;
  uStack_68 = _UNK_002b0c68;
  local_70 = _DAT_002b0c60;
  local_90[1] = 0x28;
  local_90[2] = 0x29;
  local_90[3] = 0x56;
  local_90[4] = 0;
  local_78 = FUN_00566448(uVar5,&local_70,local_90,uVar4);
  if ((local_90[0] & 1) != 0) {
    _ZdlPv(local_80);
  }
  if ((local_70 & 1) != 0) {
    _ZdlPv(local_60);
  }
  uVar6 = FUN_0056626c(&local_78);
  if ((uVar6 & 1) == 0) goto LAB_00ada710;
  plVar7 = (long *)param_1[4];
  if (plVar7 == (long *)0x0) {
    local_50 = (ulong *)0x0;
  }
  else if (plVar7 == param_1) {
    local_50 = &local_70;
    (**(code **)(*param_1 + 0x18))(param_1,&local_70);
  }
  else {
    local_50 = (ulong *)(**(code **)(*plVar7 + 0x10))();
  }
  FUN_00adb874(&local_70,&DAT_0109ff60);
  if (local_50 == &local_70) {
    lVar10 = 0x20;
    puVar8 = &local_70;
LAB_00ada6e8:
    (**(code **)(*puVar8 + lVar10))();
  }
  else if (local_50 != (ulong *)0x0) {
    lVar10 = 0x28;
    puVar8 = local_50;
    goto LAB_00ada6e8;
  }
  FUN_00566284();
  uVar9 = FUN_00566978();
  if (local_78 != 0) {
    FUN_00551e14(uVar4,uVar9);
  }
LAB_00ada710:
  if (*(long *)(lVar1 + 0x28) == local_38) {
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
<a id="insn-00ada5ac"></a> `00ada5ac` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00ada5b0"></a> `00ada5b0` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ada5b4"></a> `00ada5b4` | `f6 57 07 a9` | stp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ada5b8"></a> `00ada5b8` | `f4 4f 08 a9` | stp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00ada5bc"></a> `00ada5bc` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00ada5c0"></a> `00ada5c0` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00ada5c4"></a> `00ada5c4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00ada5c8"></a> `00ada5c8` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00ada5cc"></a> `00ada5cc` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ada5d0"></a> `00ada5d0` | `71 2e ea 97` | bl 0x00565f94 | `UNCONDITIONAL_CALL`
<a id="insn-00ada5d4"></a> `00ada5d4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ada5d8"></a> `00ada5d8` | `2b 2f ea 97` | bl 0x00566284 | `UNCONDITIONAL_CALL`
<a id="insn-00ada5dc"></a> `00ada5dc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ada5e0"></a> `00ada5e0` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00ada5e4"></a> `00ada5e4` | `83 02 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00ada5e8"></a> `00ada5e8` | `c8 bd ff d0` | adrp x8,0x294000 | `FALL_THROUGH`
<a id="insn-00ada5ec"></a> `00ada5ec` | `08 85 04 91` | add x8,x8,#0x121 | `FALL_THROUGH`
<a id="insn-00ada5f0"></a> `00ada5f0` | `a9 be ff d0` | adrp x9,0x2b0000 | `FALL_THROUGH`
<a id="insn-00ada5f4"></a> `00ada5f4` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00ada5f8"></a> `00ada5f8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ada5fc"></a> `00ada5fc` | `e0 1b 00 f9` | str x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ada600"></a> `00ada600` | `1f 60 00 39` | strb wzr,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00ada604"></a> `00ada604` | `08 08 00 f9` | str x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00ada608"></a> `00ada608` | `c8 00 80 52` | mov w8,#0x6 | `FALL_THROUGH`
<a id="insn-00ada60c"></a> `00ada60c` | `00 00 80 3d` | str q0,[x0] | `FALL_THROUGH`
<a id="insn-00ada610"></a> `00ada610` | `20 19 c3 3d` | ldr q0,[x9, #0xc60] | `FALL_THROUGH`
<a id="insn-00ada614"></a> `00ada614` | `e8 03 00 39` | strb w8,[sp] | `FALL_THROUGH`
<a id="insn-00ada618"></a> `00ada618` | `08 25 85 52` | mov w8,#0x2928 | `FALL_THROUGH`
<a id="insn-00ada61c"></a> `00ada61c` | `c8 0a a0 72` | movk w8,#0x56, LSL #16 | `FALL_THROUGH`
<a id="insn-00ada620"></a> `00ada620` | `e0 0b 80 3d` | str q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ada624"></a> `00ada624` | `e8 13 00 b8` | stur w8,[sp, #0x1] | `FALL_THROUGH`
<a id="insn-00ada628"></a> `00ada628` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ada62c"></a> `00ada62c` | `e2 03 00 91` | mov x2,sp | `FALL_THROUGH`
<a id="insn-00ada630"></a> `00ada630` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ada634"></a> `00ada634` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-00ada638"></a> `00ada638` | `84 2f ea 97` | bl 0x00566448 | `UNCONDITIONAL_CALL`
<a id="insn-00ada63c"></a> `00ada63c` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00ada640"></a> `00ada640` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ada644"></a> `00ada644` | `68 00 00 36` | tbz w8,#0x0,0x00ada650 | `CONDITIONAL_JUMP`
<a id="insn-00ada648"></a> `00ada648` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ada64c"></a> `00ada64c` | `71 02 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00ada650"></a> `00ada650` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ada654"></a> `00ada654` | `68 00 00 36` | tbz w8,#0x0,0x00ada660 | `CONDITIONAL_JUMP`
<a id="insn-00ada658"></a> `00ada658` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ada65c"></a> `00ada65c` | `6d 02 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00ada660"></a> `00ada660` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00ada664"></a> `00ada664` | `02 2f ea 97` | bl 0x0056626c | `UNCONDITIONAL_CALL`
<a id="insn-00ada668"></a> `00ada668` | `40 05 00 36` | tbz w0,#0x0,0x00ada710 | `CONDITIONAL_JUMP`
<a id="insn-00ada66c"></a> `00ada66c` | `80 12 40 f9` | ldr x0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00ada670"></a> `00ada670` | `00 01 00 b4` | cbz x0,0x00ada690 | `CONDITIONAL_JUMP`
<a id="insn-00ada674"></a> `00ada674` | `1f 00 14 eb` | cmp x0,x20 | `FALL_THROUGH`
<a id="insn-00ada678"></a> `00ada678` | `00 01 00 54` | b.eq 0x00ada698 | `CONDITIONAL_JUMP`
<a id="insn-00ada67c"></a> `00ada67c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ada680"></a> `00ada680` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ada684"></a> `00ada684` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ada688"></a> `00ada688` | `e0 23 00 f9` | str x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ada68c"></a> `00ada68c` | `0a 00 00 14` | b 0x00ada6b4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ada690"></a> `00ada690` | `ff 23 00 f9` | str xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ada694"></a> `00ada694` | `08 00 00 14` | b 0x00ada6b4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ada698"></a> `00ada698` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ada69c"></a> `00ada69c` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00ada6a0"></a> `00ada6a0` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ada6a4"></a> `00ada6a4` | `e8 23 00 f9` | str x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ada6a8"></a> `00ada6a8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ada6ac"></a> `00ada6ac` | `28 0d 40 f9` | ldr x8,[x9, #0x18] | `FALL_THROUGH`
<a id="insn-00ada6b0"></a> `00ada6b0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ada6b4"></a> `00ada6b4` | `21 2e 00 b0` | adrp x1,0x109f000 | `FALL_THROUGH`
<a id="insn-00ada6b8"></a> `00ada6b8` | `21 80 3d 91` | add x1,x1,#0xf60 | `FALL_THROUGH`
<a id="insn-00ada6bc"></a> `00ada6bc` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ada6c0"></a> `00ada6c0` | `f4 83 00 91` | add x20,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ada6c4"></a> `00ada6c4` | `6c 04 00 94` | bl 0x00adb874 | `UNCONDITIONAL_CALL`
<a id="insn-00ada6c8"></a> `00ada6c8` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ada6cc"></a> `00ada6cc` | `1f 00 14 eb` | cmp x0,x20 | `FALL_THROUGH`
<a id="insn-00ada6d0"></a> `00ada6d0` | `80 00 00 54` | b.eq 0x00ada6e0 | `CONDITIONAL_JUMP`
<a id="insn-00ada6d4"></a> `00ada6d4` | `00 01 00 b4` | cbz x0,0x00ada6f4 | `CONDITIONAL_JUMP`
<a id="insn-00ada6d8"></a> `00ada6d8` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00ada6dc"></a> `00ada6dc` | `03 00 00 14` | b 0x00ada6e8 | `UNCONDITIONAL_JUMP`
<a id="insn-00ada6e0"></a> `00ada6e0` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00ada6e4"></a> `00ada6e4` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ada6e8"></a> `00ada6e8` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00ada6ec"></a> `00ada6ec` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ada6f0"></a> `00ada6f0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ada6f4"></a> `00ada6f4` | `e4 2e ea 97` | bl 0x00566284 | `UNCONDITIONAL_CALL`
<a id="insn-00ada6f8"></a> `00ada6f8` | `a0 30 ea 97` | bl 0x00566978 | `UNCONDITIONAL_CALL`
<a id="insn-00ada6fc"></a> `00ada6fc` | `e2 0f 40 f9` | ldr x2,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ada700"></a> `00ada700` | `82 00 00 b4` | cbz x2,0x00ada710 | `CONDITIONAL_JUMP`
<a id="insn-00ada704"></a> `00ada704` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ada708"></a> `00ada708` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ada70c"></a> `00ada70c` | `c2 dd e9 97` | bl 0x00551e14 | `UNCONDITIONAL_CALL`
<a id="insn-00ada710"></a> `00ada710` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00ada714"></a> `00ada714` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ada718"></a> `00ada718` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ada71c"></a> `00ada71c` | `a1 02 00 54` | b.ne 0x00ada770 | `CONDITIONAL_JUMP`
<a id="insn-00ada720"></a> `00ada720` | `f4 4f 48 a9` | ldp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00ada724"></a> `00ada724` | `f6 57 47 a9` | ldp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ada728"></a> `00ada728` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ada72c"></a> `00ada72c` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00ada730"></a> `00ada730` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ada770"></a> `00ada770` | `34 02 04 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ada5ac`](#insn-00ada5ac) 範囲 `[['00ada5ac', '00ada647']]`
  - `CONDITIONAL_JUMP` [`00ada644`](#insn-00ada644) → [`00ada650`](#insn-00ada650)
  - `FALL_THROUGH` [`00ada644`](#insn-00ada644) → [`00ada648`](#insn-00ada648)
- ブロック [`00ada648`](#insn-00ada648) 範囲 `[['00ada648', '00ada64f']]`
  - `FALL_THROUGH` [`00ada64c`](#insn-00ada64c) → [`00ada650`](#insn-00ada650)
- ブロック [`00ada650`](#insn-00ada650) 範囲 `[['00ada650', '00ada657']]`
  - `CONDITIONAL_JUMP` [`00ada654`](#insn-00ada654) → [`00ada660`](#insn-00ada660)
  - `FALL_THROUGH` [`00ada654`](#insn-00ada654) → [`00ada658`](#insn-00ada658)
- ブロック [`00ada658`](#insn-00ada658) 範囲 `[['00ada658', '00ada65f']]`
  - `FALL_THROUGH` [`00ada65c`](#insn-00ada65c) → [`00ada660`](#insn-00ada660)
- ブロック [`00ada660`](#insn-00ada660) 範囲 `[['00ada660', '00ada66b']]`
  - `CONDITIONAL_JUMP` [`00ada668`](#insn-00ada668) → [`00ada710`](#insn-00ada710)
  - `FALL_THROUGH` [`00ada668`](#insn-00ada668) → [`00ada66c`](#insn-00ada66c)
- ブロック [`00ada66c`](#insn-00ada66c) 範囲 `[['00ada66c', '00ada673']]`
  - `CONDITIONAL_JUMP` [`00ada670`](#insn-00ada670) → [`00ada690`](#insn-00ada690)
  - `FALL_THROUGH` [`00ada670`](#insn-00ada670) → [`00ada674`](#insn-00ada674)
- ブロック [`00ada674`](#insn-00ada674) 範囲 `[['00ada674', '00ada67b']]`
  - `CONDITIONAL_JUMP` [`00ada678`](#insn-00ada678) → [`00ada698`](#insn-00ada698)
  - `FALL_THROUGH` [`00ada678`](#insn-00ada678) → [`00ada67c`](#insn-00ada67c)
- ブロック [`00ada67c`](#insn-00ada67c) 範囲 `[['00ada67c', '00ada68f']]`
  - `UNCONDITIONAL_JUMP` [`00ada68c`](#insn-00ada68c) → [`00ada6b4`](#insn-00ada6b4)
- ブロック [`00ada690`](#insn-00ada690) 範囲 `[['00ada690', '00ada697']]`
  - `UNCONDITIONAL_JUMP` [`00ada694`](#insn-00ada694) → [`00ada6b4`](#insn-00ada6b4)
- ブロック [`00ada698`](#insn-00ada698) 範囲 `[['00ada698', '00ada6b3']]`
  - `FALL_THROUGH` [`00ada6b0`](#insn-00ada6b0) → [`00ada6b4`](#insn-00ada6b4)
- ブロック [`00ada6b4`](#insn-00ada6b4) 範囲 `[['00ada6b4', '00ada6d3']]`
  - `CONDITIONAL_JUMP` [`00ada6d0`](#insn-00ada6d0) → [`00ada6e0`](#insn-00ada6e0)
  - `FALL_THROUGH` [`00ada6d0`](#insn-00ada6d0) → [`00ada6d4`](#insn-00ada6d4)
- ブロック [`00ada6d4`](#insn-00ada6d4) 範囲 `[['00ada6d4', '00ada6d7']]`
  - `CONDITIONAL_JUMP` [`00ada6d4`](#insn-00ada6d4) → [`00ada6f4`](#insn-00ada6f4)
  - `FALL_THROUGH` [`00ada6d4`](#insn-00ada6d4) → [`00ada6d8`](#insn-00ada6d8)
- ブロック [`00ada6d8`](#insn-00ada6d8) 範囲 `[['00ada6d8', '00ada6df']]`
  - `UNCONDITIONAL_JUMP` [`00ada6dc`](#insn-00ada6dc) → [`00ada6e8`](#insn-00ada6e8)
- ブロック [`00ada6e0`](#insn-00ada6e0) 範囲 `[['00ada6e0', '00ada6e7']]`
  - `FALL_THROUGH` [`00ada6e4`](#insn-00ada6e4) → [`00ada6e8`](#insn-00ada6e8)
- ブロック [`00ada6e8`](#insn-00ada6e8) 範囲 `[['00ada6e8', '00ada6f3']]`
  - `FALL_THROUGH` [`00ada6f0`](#insn-00ada6f0) → [`00ada6f4`](#insn-00ada6f4)
- ブロック [`00ada6f4`](#insn-00ada6f4) 範囲 `[['00ada6f4', '00ada703']]`
  - `CONDITIONAL_JUMP` [`00ada700`](#insn-00ada700) → [`00ada710`](#insn-00ada710)
  - `FALL_THROUGH` [`00ada700`](#insn-00ada700) → [`00ada704`](#insn-00ada704)
- ブロック [`00ada704`](#insn-00ada704) 範囲 `[['00ada704', '00ada70f']]`
  - `FALL_THROUGH` [`00ada70c`](#insn-00ada70c) → [`00ada710`](#insn-00ada710)
- ブロック [`00ada710`](#insn-00ada710) 範囲 `[['00ada710', '00ada71f']]`
  - `CONDITIONAL_JUMP` [`00ada71c`](#insn-00ada71c) → [`00ada770`](#insn-00ada770)
  - `FALL_THROUGH` [`00ada71c`](#insn-00ada71c) → [`00ada720`](#insn-00ada720)
- ブロック [`00ada720`](#insn-00ada720) 範囲 `[['00ada720', '00ada733']]`
- ブロック [`00ada770`](#insn-00ada770) 範囲 `[['00ada770', '00ada773']]`

## 命令位置別の参照

- [`00ada5b0`](#insn-00ada5b0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada5b4`](#insn-00ada5b4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada5b8`](#insn-00ada5b8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada5cc`](#insn-00ada5cc) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada5d0`](#insn-00ada5d0) → [`00565f94`](../00565/00565f94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00565f94` · 推定シンボル `None` · 推定型 `None`
- [`00ada5d8`](#insn-00ada5d8) → [`00566284`](../00566/00566284.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566284` · 推定シンボル `None` · 推定型 `None`
- [`00ada5e4`](#insn-00ada5e4) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00ada5f4`](#insn-00ada5f4) → `00294121`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ada5f8`](#insn-00ada5f8) → `00294131`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ada5fc`](#insn-00ada5fc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada610`](#insn-00ada610) → `002b0c60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada614`](#insn-00ada614) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada620`](#insn-00ada620) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada624`](#insn-00ada624) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada638`](#insn-00ada638) → [`00566448`](../00566/00566448.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566448` · 推定シンボル `None` · 推定型 `None`
- [`00ada63c`](#insn-00ada63c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada640`](#insn-00ada640) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada644`](#insn-00ada644) → [`00ada650`](#insn-00ada650) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada648`](#insn-00ada648) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada64c`](#insn-00ada64c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00ada650`](#insn-00ada650) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada654`](#insn-00ada654) → [`00ada660`](#insn-00ada660) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada658`](#insn-00ada658) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada65c`](#insn-00ada65c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00ada664`](#insn-00ada664) → [`0056626c`](../00566/0056626c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0056626c` · 推定シンボル `None` · 推定型 `None`
- [`00ada668`](#insn-00ada668) → [`00ada710`](#insn-00ada710) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada670`](#insn-00ada670) → [`00ada690`](#insn-00ada690) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada678`](#insn-00ada678) → [`00ada698`](#insn-00ada698) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada688`](#insn-00ada688) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada68c`](#insn-00ada68c) → [`00ada6b4`](#insn-00ada6b4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada690`](#insn-00ada690) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada694`](#insn-00ada694) → [`00ada6b4`](#insn-00ada6b4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada6a4`](#insn-00ada6a4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada6b8`](#insn-00ada6b8) → `0109ff60`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada6c4`](#insn-00ada6c4) → [`00adb874`](../00adb/00adb874.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adb874` · 推定シンボル `None` · 推定型 `None`
- [`00ada6c8`](#insn-00ada6c8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada6d0`](#insn-00ada6d0) → [`00ada6e0`](#insn-00ada6e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada6d4`](#insn-00ada6d4) → [`00ada6f4`](#insn-00ada6f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada6dc`](#insn-00ada6dc) → [`00ada6e8`](#insn-00ada6e8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada6e8`](#insn-00ada6e8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada6f4`](#insn-00ada6f4) → [`00566284`](../00566/00566284.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566284` · 推定シンボル `None` · 推定型 `None`
- [`00ada6f8`](#insn-00ada6f8) → [`00566978`](../00566/00566978.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566978` · 推定シンボル `None` · 推定型 `None`
- [`00ada6fc`](#insn-00ada6fc) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada700`](#insn-00ada700) → [`00ada710`](#insn-00ada710) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada70c`](#insn-00ada70c) → [`00551e14`](../00551/00551e14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00551e14` · 推定シンボル `None` · 推定型 `None`
- [`00ada714`](#insn-00ada714) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada71c`](#insn-00ada71c) → [`00ada770`](#insn-00ada770) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada720`](#insn-00ada720) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada724`](#insn-00ada724) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada728`](#insn-00ada728) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada770`](#insn-00ada770) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ada5b0`](#insn-00ada5b0)

~~~json
{
  "source": "00ada5b0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada5b4`](#insn-00ada5b4)

~~~json
{
  "source": "00ada5b4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada5b8`](#insn-00ada5b8)

~~~json
{
  "source": "00ada5b8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada5cc`](#insn-00ada5cc)

~~~json
{
  "source": "00ada5cc",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada5d0`](#insn-00ada5d0)

~~~json
{
  "source": "00ada5d0",
  "target": "00565f94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ada5d8`](#insn-00ada5d8)

~~~json
{
  "source": "00ada5d8",
  "target": "00566284",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ada5e4`](#insn-00ada5e4)

~~~json
{
  "source": "00ada5e4",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ada5f4`](#insn-00ada5f4)

~~~json
{
  "source": "00ada5f4",
  "target": "00294121",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00294121",
  "offset": 0,
  "size": 25,
  "datatype": "string",
  "bytes": "7461706a6f7947657443757272656e637942616c616e636500",
  "capture_start": "00294121",
  "capture_bytes": 25,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ada5f8`](#insn-00ada5f8)

~~~json
{
  "source": "00ada5f8",
  "target": "00294131",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00294121",
  "offset": 16,
  "size": 25,
  "datatype": "string",
  "bytes": "7461706a6f7947657443757272656e637942616c616e636500",
  "capture_start": "00294121",
  "capture_bytes": 25,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ada5fc`](#insn-00ada5fc)

~~~json
{
  "source": "00ada5fc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada610`](#insn-00ada610)

~~~json
{
  "source": "00ada610",
  "target": "002b0c60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada614`](#insn-00ada614)

~~~json
{
  "source": "00ada614",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada620`](#insn-00ada620)

~~~json
{
  "source": "00ada620",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada624`](#insn-00ada624)

~~~json
{
  "source": "00ada624",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada638`](#insn-00ada638)

~~~json
{
  "source": "00ada638",
  "target": "00566448",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ada63c`](#insn-00ada63c)

~~~json
{
  "source": "00ada63c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada640`](#insn-00ada640)

~~~json
{
  "source": "00ada640",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada644`](#insn-00ada644)

~~~json
{
  "source": "00ada644",
  "target": "00ada650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada648`](#insn-00ada648)

~~~json
{
  "source": "00ada648",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada64c`](#insn-00ada64c)

~~~json
{
  "source": "00ada64c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ada650`](#insn-00ada650)

~~~json
{
  "source": "00ada650",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada654`](#insn-00ada654)

~~~json
{
  "source": "00ada654",
  "target": "00ada660",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada658`](#insn-00ada658)

~~~json
{
  "source": "00ada658",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada65c`](#insn-00ada65c)

~~~json
{
  "source": "00ada65c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ada664`](#insn-00ada664)

~~~json
{
  "source": "00ada664",
  "target": "0056626c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ada668`](#insn-00ada668)

~~~json
{
  "source": "00ada668",
  "target": "00ada710",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada670`](#insn-00ada670)

~~~json
{
  "source": "00ada670",
  "target": "00ada690",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada678`](#insn-00ada678)

~~~json
{
  "source": "00ada678",
  "target": "00ada698",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada688`](#insn-00ada688)

~~~json
{
  "source": "00ada688",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada68c`](#insn-00ada68c)

~~~json
{
  "source": "00ada68c",
  "target": "00ada6b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada690`](#insn-00ada690)

~~~json
{
  "source": "00ada690",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada694`](#insn-00ada694)

~~~json
{
  "source": "00ada694",
  "target": "00ada6b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada6a4`](#insn-00ada6a4)

~~~json
{
  "source": "00ada6a4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada6b8`](#insn-00ada6b8)

~~~json
{
  "source": "00ada6b8",
  "target": "0109ff60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada6c4`](#insn-00ada6c4)

~~~json
{
  "source": "00ada6c4",
  "target": "00adb874",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ada6c8`](#insn-00ada6c8)

~~~json
{
  "source": "00ada6c8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada6d0`](#insn-00ada6d0)

~~~json
{
  "source": "00ada6d0",
  "target": "00ada6e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada6d4`](#insn-00ada6d4)

~~~json
{
  "source": "00ada6d4",
  "target": "00ada6f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada6dc`](#insn-00ada6dc)

~~~json
{
  "source": "00ada6dc",
  "target": "00ada6e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada6e8`](#insn-00ada6e8)

~~~json
{
  "source": "00ada6e8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada6f4`](#insn-00ada6f4)

~~~json
{
  "source": "00ada6f4",
  "target": "00566284",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ada6f8`](#insn-00ada6f8)

~~~json
{
  "source": "00ada6f8",
  "target": "00566978",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ada6fc`](#insn-00ada6fc)

~~~json
{
  "source": "00ada6fc",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada700`](#insn-00ada700)

~~~json
{
  "source": "00ada700",
  "target": "00ada710",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada70c`](#insn-00ada70c)

~~~json
{
  "source": "00ada70c",
  "target": "00551e14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ada714`](#insn-00ada714)

~~~json
{
  "source": "00ada714",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada71c`](#insn-00ada71c)

~~~json
{
  "source": "00ada71c",
  "target": "00ada770",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada720`](#insn-00ada720)

~~~json
{
  "source": "00ada720",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada724`](#insn-00ada724)

~~~json
{
  "source": "00ada724",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada728`](#insn-00ada728)

~~~json
{
  "source": "00ada728",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada770`](#insn-00ada770)

~~~json
{
  "source": "00ada770",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
