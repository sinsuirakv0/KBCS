# 00ada6ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ada774`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ada/00ada774.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-37a0b8f2bf009978cb4105bffa0229bc)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ada6ac",
  "name": "FUN_00ada6ac",
  "size": 388,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "80eb49b5d17c275969d0d2992a3bb018a2294e141494beca29c39e68fe207f56",
  "source_text_sha256": "80eb49b5d17c275969d0d2992a3bb018a2294e141494beca29c39e68fe207f56",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ada6ac",
        "00ada82b"
      ],
      [
        "00ada868",
        "00ada86b"
      ]
    ],
    "bytes_sha256": "e9770cb5109d2cf9bfce970224e9ae1f267925d7fade6583ad651da7c5fde241",
    "instruction_count": 97,
    "instruction_bytes": 388,
    "body_bytes": 388,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [0085f63c](../0085f/0085f63c.md)
- [00871208](../00871/00871208.md)
- [00879fe4](../00879/00879fe4.md)

## 呼び出し先

- [00551e14](../00551/00551e14.md)
- [00565f94](../00565/00565f94.md)
- [0056626c](../00566/0056626c.md)
- [00566284](../00566/00566284.md)
- [00566448](../00566/00566448.md)
- [00566978](../00566/00566978.md)
- [00adb7ac](../00adb/00adb7ac.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 関連文字列（未確認候補）

~~~text
"tapjoySpendCurrency"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2707 bytes

~~~c

void FUN_00ada6ac(undefined4 param_1,long *param_2)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  ulong uVar4;
  long *plVar5;
  byte *pbVar6;
  long lVar7;
  byte local_90 [16];
  void *local_80;
  long local_78;
  byte local_70;
  char acStack_6f [8];
  undefined7 uStack_67;
  undefined4 uStack_60;
  uint uStack_5c;
  byte *local_50;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  uVar2 = FUN_00565f94();
  uVar3 = FUN_00566284();
  local_70 = 0x26;
  local_90[0] = 8;
  uStack_5c = uStack_5c & 0xffffff00;
  uStack_67 = (undefined7)s_tapjoySpendCurrency_0029523a._8_8_;
  uStack_60 = CONCAT31(0x79636e,SUB81(s_tapjoySpendCurrency_0029523a._8_8_,7));
  acStack_6f[0] = s_tapjoySpendCurrency_0029523a[0];
  acStack_6f[1] = s_tapjoySpendCurrency_0029523a[1];
  acStack_6f[2] = s_tapjoySpendCurrency_0029523a[2];
  acStack_6f[3] = s_tapjoySpendCurrency_0029523a[3];
  acStack_6f[4] = s_tapjoySpendCurrency_0029523a[4];
  acStack_6f[5] = s_tapjoySpendCurrency_0029523a[5];
  acStack_6f[6] = s_tapjoySpendCurrency_0029523a[6];
  acStack_6f[7] = s_tapjoySpendCurrency_0029523a[7];
  local_90[1] = 0x28;
  local_90[2] = 0x49;
  local_90[3] = 0x29;
  local_90[4] = 0x56;
  local_90[5] = 0;
  local_78 = FUN_00566448(uVar3,&local_70,local_90,uVar2);
  if ((local_90[0] & 1) != 0) {
    _ZdlPv(local_80);
  }
  if ((local_70 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_5c,uStack_60));
  }
                    /* try { // try from 00ada754 to 00bda8bb has its CatchHandler @ 00ada754
                       catch() { ... } // from try @ 00ada754 with catch @ 00ada754
                       catch() { ... } // from try @ 00ada8ec with catch @ 00ada754
                       catch() { ... } // from try @ 00ada9dc with catch @ 00ada754 */
  uVar4 = FUN_0056626c(&local_78);
  if ((uVar4 & 1) == 0) goto LAB_00ada808;
  plVar5 = (long *)param_2[4];
  if (plVar5 == (long *)0x0) {
    local_50 = (byte *)0x0;
  }
  else if (plVar5 == param_2) {
    local_50 = &local_70;
    (**(code **)(*param_2 + 0x18))(param_2,&local_70);
  }
  else {
    local_50 = (byte *)(**(code **)(*plVar5 + 0x10))();
  }
  FUN_00adb7ac(&local_70,&DAT_0109fed0);
  if (local_50 == &local_70) {
    lVar7 = 0x20;
    pbVar6 = &local_70;
LAB_00ada7dc:
    (**(code **)(*(long *)pbVar6 + lVar7))();
  }
  else if (local_50 != (byte *)0x0) {
    lVar7 = 0x28;
    pbVar6 = local_50;
    goto LAB_00ada7dc;
  }
  FUN_00566284();
  uVar3 = FUN_00566978();
  if (local_78 != 0) {
    FUN_00551e14(uVar2,uVar3,local_78,param_1);
  }
LAB_00ada808:
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
<a id="insn-00ada6ac"></a> `00ada6ac` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00ada6b0"></a> `00ada6b0` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ada6b4"></a> `00ada6b4` | `f6 57 07 a9` | stp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ada6b8"></a> `00ada6b8` | `f4 4f 08 a9` | stp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00ada6bc"></a> `00ada6bc` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00ada6c0"></a> `00ada6c0` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00ada6c4"></a> `00ada6c4` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00ada6c8"></a> `00ada6c8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00ada6cc"></a> `00ada6cc` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00ada6d0"></a> `00ada6d0` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ada6d4"></a> `00ada6d4` | `30 2e ea 97` | bl 0x00565f94 | `UNCONDITIONAL_CALL`
<a id="insn-00ada6d8"></a> `00ada6d8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00ada6dc"></a> `00ada6dc` | `ea 2e ea 97` | bl 0x00566284 | `UNCONDITIONAL_CALL`
<a id="insn-00ada6e0"></a> `00ada6e0` | `c8 04 80 52` | mov w8,#0x26 | `FALL_THROUGH`
<a id="insn-00ada6e4"></a> `00ada6e4` | `c9 bd ff f0` | adrp x9,0x295000 | `FALL_THROUGH`
<a id="insn-00ada6e8"></a> `00ada6e8` | `29 e9 08 91` | add x9,x9,#0x23a | `FALL_THROUGH`
<a id="insn-00ada6ec"></a> `00ada6ec` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ada6f0"></a> `00ada6f0` | `08 01 80 52` | mov w8,#0x8 | `FALL_THROUGH`
<a id="insn-00ada6f4"></a> `00ada6f4` | `aa cc 8d 52` | mov w10,#0x6e65 | `FALL_THROUGH`
<a id="insn-00ada6f8"></a> `00ada6f8` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00ada6fc"></a> `00ada6fc` | `e8 03 00 39` | strb w8,[sp] | `FALL_THROUGH`
<a id="insn-00ada700"></a> `00ada700` | `08 25 89 52` | mov w8,#0x4928 | `FALL_THROUGH`
<a id="insn-00ada704"></a> `00ada704` | `6a 2c af 72` | movk w10,#0x7963, LSL #16 | `FALL_THROUGH`
<a id="insn-00ada708"></a> `00ada708` | `28 c5 aa 72` | movk w8,#0x5629, LSL #16 | `FALL_THROUGH`
<a id="insn-00ada70c"></a> `00ada70c` | `ff d3 00 39` | strb wzr,[sp, #0x34] | `FALL_THROUGH`
<a id="insn-00ada710"></a> `00ada710` | `ea 33 00 b9` | str w10,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ada714"></a> `00ada714` | `e0 13 82 3c` | stur q0,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00ada718"></a> `00ada718` | `e8 13 00 b8` | stur w8,[sp, #0x1] | `FALL_THROUGH`
<a id="insn-00ada71c"></a> `00ada71c` | `ff 17 00 39` | strb wzr,[sp, #0x5] | `FALL_THROUGH`
<a id="insn-00ada720"></a> `00ada720` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ada724"></a> `00ada724` | `e2 03 00 91` | mov x2,sp | `FALL_THROUGH`
<a id="insn-00ada728"></a> `00ada728` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00ada72c"></a> `00ada72c` | `47 2f ea 97` | bl 0x00566448 | `UNCONDITIONAL_CALL`
<a id="insn-00ada730"></a> `00ada730` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00ada734"></a> `00ada734` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ada738"></a> `00ada738` | `68 00 00 36` | tbz w8,#0x0,0x00ada744 | `CONDITIONAL_JUMP`
<a id="insn-00ada73c"></a> `00ada73c` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ada740"></a> `00ada740` | `08 02 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00ada744"></a> `00ada744` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ada748"></a> `00ada748` | `68 00 00 36` | tbz w8,#0x0,0x00ada754 | `CONDITIONAL_JUMP`
<a id="insn-00ada74c"></a> `00ada74c` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ada750"></a> `00ada750` | `04 02 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00ada754"></a> `00ada754` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00ada758"></a> `00ada758` | `c5 2e ea 97` | bl 0x0056626c | `UNCONDITIONAL_CALL`
<a id="insn-00ada75c"></a> `00ada75c` | `60 05 00 36` | tbz w0,#0x0,0x00ada808 | `CONDITIONAL_JUMP`
<a id="insn-00ada760"></a> `00ada760` | `a0 12 40 f9` | ldr x0,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00ada764"></a> `00ada764` | `00 01 00 b4` | cbz x0,0x00ada784 | `CONDITIONAL_JUMP`
<a id="insn-00ada768"></a> `00ada768` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-00ada76c"></a> `00ada76c` | `00 01 00 54` | b.eq 0x00ada78c | `CONDITIONAL_JUMP`
<a id="insn-00ada770"></a> `00ada770` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ada774"></a> `00ada774` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ada778"></a> `00ada778` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ada77c"></a> `00ada77c` | `e0 23 00 f9` | str x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ada780"></a> `00ada780` | `0a 00 00 14` | b 0x00ada7a8 | `UNCONDITIONAL_JUMP`
<a id="insn-00ada784"></a> `00ada784` | `ff 23 00 f9` | str xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ada788"></a> `00ada788` | `08 00 00 14` | b 0x00ada7a8 | `UNCONDITIONAL_JUMP`
<a id="insn-00ada78c"></a> `00ada78c` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ada790"></a> `00ada790` | `a9 02 40 f9` | ldr x9,[x21] | `FALL_THROUGH`
<a id="insn-00ada794"></a> `00ada794` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ada798"></a> `00ada798` | `e8 23 00 f9` | str x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ada79c"></a> `00ada79c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ada7a0"></a> `00ada7a0` | `28 0d 40 f9` | ldr x8,[x9, #0x18] | `FALL_THROUGH`
<a id="insn-00ada7a4"></a> `00ada7a4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ada7a8"></a> `00ada7a8` | `21 2e 00 b0` | adrp x1,0x109f000 | `FALL_THROUGH`
<a id="insn-00ada7ac"></a> `00ada7ac` | `21 40 3b 91` | add x1,x1,#0xed0 | `FALL_THROUGH`
<a id="insn-00ada7b0"></a> `00ada7b0` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ada7b4"></a> `00ada7b4` | `f5 83 00 91` | add x21,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ada7b8"></a> `00ada7b8` | `fd 03 00 94` | bl 0x00adb7ac | `UNCONDITIONAL_CALL`
<a id="insn-00ada7bc"></a> `00ada7bc` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ada7c0"></a> `00ada7c0` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-00ada7c4"></a> `00ada7c4` | `80 00 00 54` | b.eq 0x00ada7d4 | `CONDITIONAL_JUMP`
<a id="insn-00ada7c8"></a> `00ada7c8` | `00 01 00 b4` | cbz x0,0x00ada7e8 | `CONDITIONAL_JUMP`
<a id="insn-00ada7cc"></a> `00ada7cc` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00ada7d0"></a> `00ada7d0` | `03 00 00 14` | b 0x00ada7dc | `UNCONDITIONAL_JUMP`
<a id="insn-00ada7d4"></a> `00ada7d4` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00ada7d8"></a> `00ada7d8` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ada7dc"></a> `00ada7dc` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00ada7e0"></a> `00ada7e0` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ada7e4"></a> `00ada7e4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ada7e8"></a> `00ada7e8` | `a7 2e ea 97` | bl 0x00566284 | `UNCONDITIONAL_CALL`
<a id="insn-00ada7ec"></a> `00ada7ec` | `63 30 ea 97` | bl 0x00566978 | `UNCONDITIONAL_CALL`
<a id="insn-00ada7f0"></a> `00ada7f0` | `e2 0f 40 f9` | ldr x2,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ada7f4"></a> `00ada7f4` | `a2 00 00 b4` | cbz x2,0x00ada808 | `CONDITIONAL_JUMP`
<a id="insn-00ada7f8"></a> `00ada7f8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ada7fc"></a> `00ada7fc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ada800"></a> `00ada800` | `e3 03 13 2a` | mov w3,w19 | `FALL_THROUGH`
<a id="insn-00ada804"></a> `00ada804` | `84 dd e9 97` | bl 0x00551e14 | `UNCONDITIONAL_CALL`
<a id="insn-00ada808"></a> `00ada808` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00ada80c"></a> `00ada80c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ada810"></a> `00ada810` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ada814"></a> `00ada814` | `a1 02 00 54` | b.ne 0x00ada868 | `CONDITIONAL_JUMP`
<a id="insn-00ada818"></a> `00ada818` | `f4 4f 48 a9` | ldp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00ada81c"></a> `00ada81c` | `f6 57 47 a9` | ldp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ada820"></a> `00ada820` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ada824"></a> `00ada824` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00ada828"></a> `00ada828` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ada868"></a> `00ada868` | `ca 01 04 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ada6ac`](#insn-00ada6ac) 範囲 `[['00ada6ac', '00ada73b']]`
  - `CONDITIONAL_JUMP` [`00ada738`](#insn-00ada738) → [`00ada744`](#insn-00ada744)
  - `FALL_THROUGH` [`00ada738`](#insn-00ada738) → [`00ada73c`](#insn-00ada73c)
- ブロック [`00ada73c`](#insn-00ada73c) 範囲 `[['00ada73c', '00ada743']]`
  - `FALL_THROUGH` [`00ada740`](#insn-00ada740) → [`00ada744`](#insn-00ada744)
- ブロック [`00ada744`](#insn-00ada744) 範囲 `[['00ada744', '00ada74b']]`
  - `CONDITIONAL_JUMP` [`00ada748`](#insn-00ada748) → [`00ada754`](#insn-00ada754)
  - `FALL_THROUGH` [`00ada748`](#insn-00ada748) → [`00ada74c`](#insn-00ada74c)
- ブロック [`00ada74c`](#insn-00ada74c) 範囲 `[['00ada74c', '00ada753']]`
  - `FALL_THROUGH` [`00ada750`](#insn-00ada750) → [`00ada754`](#insn-00ada754)
- ブロック [`00ada754`](#insn-00ada754) 範囲 `[['00ada754', '00ada75f']]`
  - `CONDITIONAL_JUMP` [`00ada75c`](#insn-00ada75c) → [`00ada808`](#insn-00ada808)
  - `FALL_THROUGH` [`00ada75c`](#insn-00ada75c) → [`00ada760`](#insn-00ada760)
- ブロック [`00ada760`](#insn-00ada760) 範囲 `[['00ada760', '00ada767']]`
  - `CONDITIONAL_JUMP` [`00ada764`](#insn-00ada764) → [`00ada784`](#insn-00ada784)
  - `FALL_THROUGH` [`00ada764`](#insn-00ada764) → [`00ada768`](#insn-00ada768)
- ブロック [`00ada768`](#insn-00ada768) 範囲 `[['00ada768', '00ada76f']]`
  - `CONDITIONAL_JUMP` [`00ada76c`](#insn-00ada76c) → [`00ada78c`](#insn-00ada78c)
  - `FALL_THROUGH` [`00ada76c`](#insn-00ada76c) → [`00ada770`](#insn-00ada770)
- ブロック [`00ada770`](#insn-00ada770) 範囲 `[['00ada770', '00ada783']]`
  - `UNCONDITIONAL_JUMP` [`00ada780`](#insn-00ada780) → [`00ada7a8`](#insn-00ada7a8)
- ブロック [`00ada784`](#insn-00ada784) 範囲 `[['00ada784', '00ada78b']]`
  - `UNCONDITIONAL_JUMP` [`00ada788`](#insn-00ada788) → [`00ada7a8`](#insn-00ada7a8)
- ブロック [`00ada78c`](#insn-00ada78c) 範囲 `[['00ada78c', '00ada7a7']]`
  - `FALL_THROUGH` [`00ada7a4`](#insn-00ada7a4) → [`00ada7a8`](#insn-00ada7a8)
- ブロック [`00ada7a8`](#insn-00ada7a8) 範囲 `[['00ada7a8', '00ada7c7']]`
  - `CONDITIONAL_JUMP` [`00ada7c4`](#insn-00ada7c4) → [`00ada7d4`](#insn-00ada7d4)
  - `FALL_THROUGH` [`00ada7c4`](#insn-00ada7c4) → [`00ada7c8`](#insn-00ada7c8)
- ブロック [`00ada7c8`](#insn-00ada7c8) 範囲 `[['00ada7c8', '00ada7cb']]`
  - `CONDITIONAL_JUMP` [`00ada7c8`](#insn-00ada7c8) → [`00ada7e8`](#insn-00ada7e8)
  - `FALL_THROUGH` [`00ada7c8`](#insn-00ada7c8) → [`00ada7cc`](#insn-00ada7cc)
- ブロック [`00ada7cc`](#insn-00ada7cc) 範囲 `[['00ada7cc', '00ada7d3']]`
  - `UNCONDITIONAL_JUMP` [`00ada7d0`](#insn-00ada7d0) → [`00ada7dc`](#insn-00ada7dc)
- ブロック [`00ada7d4`](#insn-00ada7d4) 範囲 `[['00ada7d4', '00ada7db']]`
  - `FALL_THROUGH` [`00ada7d8`](#insn-00ada7d8) → [`00ada7dc`](#insn-00ada7dc)
- ブロック [`00ada7dc`](#insn-00ada7dc) 範囲 `[['00ada7dc', '00ada7e7']]`
  - `FALL_THROUGH` [`00ada7e4`](#insn-00ada7e4) → [`00ada7e8`](#insn-00ada7e8)
- ブロック [`00ada7e8`](#insn-00ada7e8) 範囲 `[['00ada7e8', '00ada7f7']]`
  - `CONDITIONAL_JUMP` [`00ada7f4`](#insn-00ada7f4) → [`00ada808`](#insn-00ada808)
  - `FALL_THROUGH` [`00ada7f4`](#insn-00ada7f4) → [`00ada7f8`](#insn-00ada7f8)
- ブロック [`00ada7f8`](#insn-00ada7f8) 範囲 `[['00ada7f8', '00ada807']]`
  - `FALL_THROUGH` [`00ada804`](#insn-00ada804) → [`00ada808`](#insn-00ada808)
- ブロック [`00ada808`](#insn-00ada808) 範囲 `[['00ada808', '00ada817']]`
  - `CONDITIONAL_JUMP` [`00ada814`](#insn-00ada814) → [`00ada868`](#insn-00ada868)
  - `FALL_THROUGH` [`00ada814`](#insn-00ada814) → [`00ada818`](#insn-00ada818)
- ブロック [`00ada818`](#insn-00ada818) 範囲 `[['00ada818', '00ada82b']]`
- ブロック [`00ada868`](#insn-00ada868) 範囲 `[['00ada868', '00ada86b']]`

## 命令位置別の参照

- [`00ada6b0`](#insn-00ada6b0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada6b4`](#insn-00ada6b4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada6b8`](#insn-00ada6b8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada6d0`](#insn-00ada6d0) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada6d4`](#insn-00ada6d4) → [`00565f94`](../00565/00565f94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00565f94` · 推定シンボル `None` · 推定型 `None`
- [`00ada6dc`](#insn-00ada6dc) → [`00566284`](../00566/00566284.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566284` · 推定シンボル `None` · 推定型 `None`
- [`00ada6ec`](#insn-00ada6ec) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada6f8`](#insn-00ada6f8) → `0029523a`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ada6fc`](#insn-00ada6fc) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada70c`](#insn-00ada70c) → `Stack[-0x5c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada710`](#insn-00ada710) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada714`](#insn-00ada714) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada718`](#insn-00ada718) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada71c`](#insn-00ada71c) → `Stack[-0x8b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada72c`](#insn-00ada72c) → [`00566448`](../00566/00566448.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566448` · 推定シンボル `None` · 推定型 `None`
- [`00ada730`](#insn-00ada730) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada734`](#insn-00ada734) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada738`](#insn-00ada738) → [`00ada744`](#insn-00ada744) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada73c`](#insn-00ada73c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada740`](#insn-00ada740) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00ada744`](#insn-00ada744) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada748`](#insn-00ada748) → [`00ada754`](#insn-00ada754) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada74c`](#insn-00ada74c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada750`](#insn-00ada750) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00ada758`](#insn-00ada758) → [`0056626c`](../00566/0056626c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0056626c` · 推定シンボル `None` · 推定型 `None`
- [`00ada75c`](#insn-00ada75c) → [`00ada808`](#insn-00ada808) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada764`](#insn-00ada764) → [`00ada784`](#insn-00ada784) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada76c`](#insn-00ada76c) → [`00ada78c`](#insn-00ada78c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada77c`](#insn-00ada77c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada780`](#insn-00ada780) → [`00ada7a8`](#insn-00ada7a8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada784`](#insn-00ada784) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada788`](#insn-00ada788) → [`00ada7a8`](#insn-00ada7a8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada798`](#insn-00ada798) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada7ac`](#insn-00ada7ac) → `0109fed0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada7b8`](#insn-00ada7b8) → [`00adb7ac`](../00adb/00adb7ac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adb7ac` · 推定シンボル `None` · 推定型 `None`
- [`00ada7bc`](#insn-00ada7bc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada7c4`](#insn-00ada7c4) → [`00ada7d4`](#insn-00ada7d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada7c8`](#insn-00ada7c8) → [`00ada7e8`](#insn-00ada7e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada7d0`](#insn-00ada7d0) → [`00ada7dc`](#insn-00ada7dc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada7dc`](#insn-00ada7dc) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada7e8`](#insn-00ada7e8) → [`00566284`](../00566/00566284.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566284` · 推定シンボル `None` · 推定型 `None`
- [`00ada7ec`](#insn-00ada7ec) → [`00566978`](../00566/00566978.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566978` · 推定シンボル `None` · 推定型 `None`
- [`00ada7f0`](#insn-00ada7f0) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada7f4`](#insn-00ada7f4) → [`00ada808`](#insn-00ada808) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada804`](#insn-00ada804) → [`00551e14`](../00551/00551e14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00551e14` · 推定シンボル `None` · 推定型 `None`
- [`00ada80c`](#insn-00ada80c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada814`](#insn-00ada814) → [`00ada868`](#insn-00ada868) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada818`](#insn-00ada818) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada81c`](#insn-00ada81c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada820`](#insn-00ada820) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ada868`](#insn-00ada868) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ada6b0`](#insn-00ada6b0)

~~~json
{
  "source": "00ada6b0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada6b4`](#insn-00ada6b4)

~~~json
{
  "source": "00ada6b4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada6b8`](#insn-00ada6b8)

~~~json
{
  "source": "00ada6b8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada6d0`](#insn-00ada6d0)

~~~json
{
  "source": "00ada6d0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada6d4`](#insn-00ada6d4)

~~~json
{
  "source": "00ada6d4",
  "target": "00565f94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ada6dc`](#insn-00ada6dc)

~~~json
{
  "source": "00ada6dc",
  "target": "00566284",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ada6ec`](#insn-00ada6ec)

~~~json
{
  "source": "00ada6ec",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada6f8`](#insn-00ada6f8)

~~~json
{
  "source": "00ada6f8",
  "target": "0029523a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029523a",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "7461706a6f795370656e6443757272656e637900",
  "capture_start": "0029523a",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ada6fc`](#insn-00ada6fc)

~~~json
{
  "source": "00ada6fc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada70c`](#insn-00ada70c)

~~~json
{
  "source": "00ada70c",
  "target": "Stack[-0x5c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada710`](#insn-00ada710)

~~~json
{
  "source": "00ada710",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada714`](#insn-00ada714)

~~~json
{
  "source": "00ada714",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada718`](#insn-00ada718)

~~~json
{
  "source": "00ada718",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada71c`](#insn-00ada71c)

~~~json
{
  "source": "00ada71c",
  "target": "Stack[-0x8b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada72c`](#insn-00ada72c)

~~~json
{
  "source": "00ada72c",
  "target": "00566448",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ada730`](#insn-00ada730)

~~~json
{
  "source": "00ada730",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada734`](#insn-00ada734)

~~~json
{
  "source": "00ada734",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada738`](#insn-00ada738)

~~~json
{
  "source": "00ada738",
  "target": "00ada744",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada73c`](#insn-00ada73c)

~~~json
{
  "source": "00ada73c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada740`](#insn-00ada740)

~~~json
{
  "source": "00ada740",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ada744`](#insn-00ada744)

~~~json
{
  "source": "00ada744",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada748`](#insn-00ada748)

~~~json
{
  "source": "00ada748",
  "target": "00ada754",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada74c`](#insn-00ada74c)

~~~json
{
  "source": "00ada74c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada750`](#insn-00ada750)

~~~json
{
  "source": "00ada750",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ada758`](#insn-00ada758)

~~~json
{
  "source": "00ada758",
  "target": "0056626c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ada75c`](#insn-00ada75c)

~~~json
{
  "source": "00ada75c",
  "target": "00ada808",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada764`](#insn-00ada764)

~~~json
{
  "source": "00ada764",
  "target": "00ada784",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada76c`](#insn-00ada76c)

~~~json
{
  "source": "00ada76c",
  "target": "00ada78c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada77c`](#insn-00ada77c)

~~~json
{
  "source": "00ada77c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada780`](#insn-00ada780)

~~~json
{
  "source": "00ada780",
  "target": "00ada7a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada784`](#insn-00ada784)

~~~json
{
  "source": "00ada784",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada788`](#insn-00ada788)

~~~json
{
  "source": "00ada788",
  "target": "00ada7a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada798`](#insn-00ada798)

~~~json
{
  "source": "00ada798",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada7ac`](#insn-00ada7ac)

~~~json
{
  "source": "00ada7ac",
  "target": "0109fed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada7b8`](#insn-00ada7b8)

~~~json
{
  "source": "00ada7b8",
  "target": "00adb7ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ada7bc`](#insn-00ada7bc)

~~~json
{
  "source": "00ada7bc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada7c4`](#insn-00ada7c4)

~~~json
{
  "source": "00ada7c4",
  "target": "00ada7d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada7c8`](#insn-00ada7c8)

~~~json
{
  "source": "00ada7c8",
  "target": "00ada7e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada7d0`](#insn-00ada7d0)

~~~json
{
  "source": "00ada7d0",
  "target": "00ada7dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada7dc`](#insn-00ada7dc)

~~~json
{
  "source": "00ada7dc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada7e8`](#insn-00ada7e8)

~~~json
{
  "source": "00ada7e8",
  "target": "00566284",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ada7ec`](#insn-00ada7ec)

~~~json
{
  "source": "00ada7ec",
  "target": "00566978",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ada7f0`](#insn-00ada7f0)

~~~json
{
  "source": "00ada7f0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada7f4`](#insn-00ada7f4)

~~~json
{
  "source": "00ada7f4",
  "target": "00ada808",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada804`](#insn-00ada804)

~~~json
{
  "source": "00ada804",
  "target": "00551e14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ada80c`](#insn-00ada80c)

~~~json
{
  "source": "00ada80c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada814`](#insn-00ada814)

~~~json
{
  "source": "00ada814",
  "target": "00ada868",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada818`](#insn-00ada818)

~~~json
{
  "source": "00ada818",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada81c`](#insn-00ada81c)

~~~json
{
  "source": "00ada81c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada820`](#insn-00ada820)

~~~json
{
  "source": "00ada820",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ada868`](#insn-00ada868)

~~~json
{
  "source": "00ada868",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
