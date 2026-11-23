# 00acbecc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00acbe04`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acbe04.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0056.md#compare-3b38589a3adf30c93f0c87697863f5bb)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00acbf10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acbf10.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0059.md#compare-af8b491f78ade279d6c931987ff9d8be)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbecc",
  "name": "FUN_00acbecc",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "61b4a42f893a3676389a35a3dd690f1d9711445d06fe4620a2d8d7d554ce2474",
  "source_text_sha256": "61b4a42f893a3676389a35a3dd690f1d9711445d06fe4620a2d8d7d554ce2474",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acbecc",
        "00acbff7"
      ],
      [
        "00acc034",
        "00acc037"
      ]
    ],
    "bytes_sha256": "fc65d70d54ff24af01044634de63cbf418d60f33054e04adf660d82e5e550b54",
    "instruction_count": 76,
    "instruction_bytes": 304,
    "body_bytes": 304,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [00accf4c](../00acc/00accf4c.md)

## 呼び出し先

- [005533e0](../00553/005533e0.md)
- [00565f94](../00565/00565f94.md)
- [0056626c](../00566/0056626c.md)
- [00566284](../00566/00566284.md)
- [00566448](../00566/00566448.md)
- [00566978](../00566/00566978.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)

## 関連文字列（未確認候補）

~~~text
"getSafeInsetBottom"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1977 bytes

~~~c

void FUN_00acbecc(void)

{
  long lVar1;
  char cVar2;
  undefined4 uVar3;
  long *plVar4;
  undefined8 uVar5;
  ulong uVar6;
  byte local_70 [16];
  void *local_60;
  byte local_58;
  char local_57 [8];
  undefined7 uStack_4f;
  char cStack_48;
  undefined2 uStack_47;
  undefined1 uStack_45;
  undefined4 uStack_44;
  long local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  plVar4 = (long *)FUN_00565f94();
  uVar5 = FUN_00566284();
  local_58 = 0x24;
  local_70[0] = 6;
  uStack_47 = 0x6d6f;
  uStack_4f = (undefined7)s_getSafeInsetBottom_0029bcec._8_8_;
  cStack_48 = SUB81(s_getSafeInsetBottom_0029bcec._8_8_,7);
  local_57[0] = s_getSafeInsetBottom_0029bcec[0];
  local_57[1] = s_getSafeInsetBottom_0029bcec[1];
  local_57[2] = s_getSafeInsetBottom_0029bcec[2];
  local_57[3] = s_getSafeInsetBottom_0029bcec[3];
  local_57[4] = s_getSafeInsetBottom_0029bcec[4];
  local_57[5] = s_getSafeInsetBottom_0029bcec[5];
  local_57[6] = s_getSafeInsetBottom_0029bcec[6];
  local_57[7] = s_getSafeInsetBottom_0029bcec[7];
  uStack_45 = 0;
  local_70[1] = 0x28;
  local_70[2] = 0x29;
  local_70[3] = 0x49;
  local_70[4] = 0;
  local_40 = FUN_00566448(uVar5,&local_58,local_70,plVar4);
  if ((local_70[0] & 1) != 0) {
    _ZdlPv(local_60);
  }
  if ((local_58 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_44,CONCAT13(uStack_45,CONCAT21(uStack_47,cStack_48))));
  }
  uVar6 = FUN_0056626c(&local_40);
  if ((uVar6 & 1) != 0) {
    FUN_00566284();
    uVar5 = FUN_00566978();
    if (local_40 != 0) {
      uVar3 = FUN_005533e0(plVar4,uVar5);
      cVar2 = (**(code **)(*plVar4 + 0x720))(plVar4);
      if (cVar2 != '\0') {
        (**(code **)(*plVar4 + 0x80))(plVar4);
        (**(code **)(*plVar4 + 0x88))(plVar4);
      }
      goto LAB_00acbfd4;
    }
  }
  uVar3 = 0;
LAB_00acbfd4:
  if (*(long *)(lVar1 + 0x28) != local_38) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail(uVar3);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acbecc"></a> `00acbecc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00acbed0"></a> `00acbed0` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acbed4"></a> `00acbed4` | `f5 2b 00 f9` | str x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acbed8"></a> `00acbed8` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acbedc"></a> `00acbedc` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00acbee0"></a> `00acbee0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acbee4"></a> `00acbee4` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acbee8"></a> `00acbee8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acbeec"></a> `00acbeec` | `2a 68 ea 97` | bl 0x00565f94 | `UNCONDITIONAL_CALL`
<a id="insn-00acbef0"></a> `00acbef0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acbef4"></a> `00acbef4` | `e4 68 ea 97` | bl 0x00566284 | `UNCONDITIONAL_CALL`
<a id="insn-00acbef8"></a> `00acbef8` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-00acbefc"></a> `00acbefc` | `89 be ff 90` | adrp x9,0x29b000 | `FALL_THROUGH`
<a id="insn-00acbf00"></a> `00acbf00` | `29 b1 33 91` | add x9,x9,#0xcec | `FALL_THROUGH`
<a id="insn-00acbf04"></a> `00acbf04` | `e8 63 00 39` | strb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00acbf08"></a> `00acbf08` | `c8 00 80 52` | mov w8,#0x6 | `FALL_THROUGH`
<a id="insn-00acbf0c"></a> `00acbf0c` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00acbf10"></a> `00acbf10` | `e8 03 00 39` | strb w8,[sp] | `FALL_THROUGH`
<a id="insn-00acbf14"></a> `00acbf14` | `08 25 85 52` | mov w8,#0x2928 | `FALL_THROUGH`
<a id="insn-00acbf18"></a> `00acbf18` | `ea ad 8d 52` | mov w10,#0x6d6f | `FALL_THROUGH`
<a id="insn-00acbf1c"></a> `00acbf1c` | `28 09 a0 72` | movk w8,#0x49, LSL #16 | `FALL_THROUGH`
<a id="insn-00acbf20"></a> `00acbf20` | `ea 93 02 78` | sturh w10,[sp, #0x29] | `FALL_THROUGH`
<a id="insn-00acbf24"></a> `00acbf24` | `e0 93 81 3c` | stur q0,[sp, #0x19] | `FALL_THROUGH`
<a id="insn-00acbf28"></a> `00acbf28` | `ff af 00 39` | strb wzr,[sp, #0x2b] | `FALL_THROUGH`
<a id="insn-00acbf2c"></a> `00acbf2c` | `e8 13 00 b8` | stur w8,[sp, #0x1] | `FALL_THROUGH`
<a id="insn-00acbf30"></a> `00acbf30` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00acbf34"></a> `00acbf34` | `e2 03 00 91` | mov x2,sp | `FALL_THROUGH`
<a id="insn-00acbf38"></a> `00acbf38` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-00acbf3c"></a> `00acbf3c` | `43 69 ea 97` | bl 0x00566448 | `UNCONDITIONAL_CALL`
<a id="insn-00acbf40"></a> `00acbf40` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00acbf44"></a> `00acbf44` | `a0 03 1f f8` | stur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00acbf48"></a> `00acbf48` | `68 00 00 36` | tbz w8,#0x0,0x00acbf54 | `CONDITIONAL_JUMP`
<a id="insn-00acbf4c"></a> `00acbf4c` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acbf50"></a> `00acbf50` | `30 3c 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00acbf54"></a> `00acbf54` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00acbf58"></a> `00acbf58` | `68 00 00 36` | tbz w8,#0x0,0x00acbf64 | `CONDITIONAL_JUMP`
<a id="insn-00acbf5c"></a> `00acbf5c` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00acbf60"></a> `00acbf60` | `2c 3c 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00acbf64"></a> `00acbf64` | `a0 43 00 d1` | sub x0,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00acbf68"></a> `00acbf68` | `c1 68 ea 97` | bl 0x0056626c | `UNCONDITIONAL_CALL`
<a id="insn-00acbf6c"></a> `00acbf6c` | `20 03 00 36` | tbz w0,#0x0,0x00acbfd0 | `CONDITIONAL_JUMP`
<a id="insn-00acbf70"></a> `00acbf70` | `c5 68 ea 97` | bl 0x00566284 | `UNCONDITIONAL_CALL`
<a id="insn-00acbf74"></a> `00acbf74` | `81 6a ea 97` | bl 0x00566978 | `UNCONDITIONAL_CALL`
<a id="insn-00acbf78"></a> `00acbf78` | `a2 03 5f f8` | ldur x2,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00acbf7c"></a> `00acbf7c` | `a2 02 00 b4` | cbz x2,0x00acbfd0 | `CONDITIONAL_JUMP`
<a id="insn-00acbf80"></a> `00acbf80` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00acbf84"></a> `00acbf84` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acbf88"></a> `00acbf88` | `16 1d ea 97` | bl 0x005533e0 | `UNCONDITIONAL_CALL`
<a id="insn-00acbf8c"></a> `00acbf8c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00acbf90"></a> `00acbf90` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00acbf94"></a> `00acbf94` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acbf98"></a> `00acbf98` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00acbf9c"></a> `00acbf9c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbfa0"></a> `00acbfa0` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00acbfa4"></a> `00acbfa4` | `20 01 00 54` | b.eq 0x00acbfc8 | `CONDITIONAL_JUMP`
<a id="insn-00acbfa8"></a> `00acbfa8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00acbfac"></a> `00acbfac` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acbfb0"></a> `00acbfb0` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00acbfb4"></a> `00acbfb4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbfb8"></a> `00acbfb8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00acbfbc"></a> `00acbfbc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acbfc0"></a> `00acbfc0` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00acbfc4"></a> `00acbfc4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbfc8"></a> `00acbfc8` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00acbfcc"></a> `00acbfcc` | `02 00 00 14` | b 0x00acbfd4 | `UNCONDITIONAL_JUMP`
<a id="insn-00acbfd0"></a> `00acbfd0` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00acbfd4"></a> `00acbfd4` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acbfd8"></a> `00acbfd8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acbfdc"></a> `00acbfdc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acbfe0"></a> `00acbfe0` | `a1 02 00 54` | b.ne 0x00acc034 | `CONDITIONAL_JUMP`
<a id="insn-00acbfe4"></a> `00acbfe4` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acbfe8"></a> `00acbfe8` | `f5 2b 40 f9` | ldr x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acbfec"></a> `00acbfec` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acbff0"></a> `00acbff0` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00acbff4"></a> `00acbff4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acc034"></a> `00acc034` | `03 3c 04 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acbecc`](#insn-00acbecc) 範囲 `[['00acbecc', '00acbf4b']]`
  - `CONDITIONAL_JUMP` [`00acbf48`](#insn-00acbf48) → [`00acbf54`](#insn-00acbf54)
  - `FALL_THROUGH` [`00acbf48`](#insn-00acbf48) → [`00acbf4c`](#insn-00acbf4c)
- ブロック [`00acbf4c`](#insn-00acbf4c) 範囲 `[['00acbf4c', '00acbf53']]`
  - `FALL_THROUGH` [`00acbf50`](#insn-00acbf50) → [`00acbf54`](#insn-00acbf54)
- ブロック [`00acbf54`](#insn-00acbf54) 範囲 `[['00acbf54', '00acbf5b']]`
  - `CONDITIONAL_JUMP` [`00acbf58`](#insn-00acbf58) → [`00acbf64`](#insn-00acbf64)
  - `FALL_THROUGH` [`00acbf58`](#insn-00acbf58) → [`00acbf5c`](#insn-00acbf5c)
- ブロック [`00acbf5c`](#insn-00acbf5c) 範囲 `[['00acbf5c', '00acbf63']]`
  - `FALL_THROUGH` [`00acbf60`](#insn-00acbf60) → [`00acbf64`](#insn-00acbf64)
- ブロック [`00acbf64`](#insn-00acbf64) 範囲 `[['00acbf64', '00acbf6f']]`
  - `CONDITIONAL_JUMP` [`00acbf6c`](#insn-00acbf6c) → [`00acbfd0`](#insn-00acbfd0)
  - `FALL_THROUGH` [`00acbf6c`](#insn-00acbf6c) → [`00acbf70`](#insn-00acbf70)
- ブロック [`00acbf70`](#insn-00acbf70) 範囲 `[['00acbf70', '00acbf7f']]`
  - `CONDITIONAL_JUMP` [`00acbf7c`](#insn-00acbf7c) → [`00acbfd0`](#insn-00acbfd0)
  - `FALL_THROUGH` [`00acbf7c`](#insn-00acbf7c) → [`00acbf80`](#insn-00acbf80)
- ブロック [`00acbf80`](#insn-00acbf80) 範囲 `[['00acbf80', '00acbfa7']]`
  - `CONDITIONAL_JUMP` [`00acbfa4`](#insn-00acbfa4) → [`00acbfc8`](#insn-00acbfc8)
  - `FALL_THROUGH` [`00acbfa4`](#insn-00acbfa4) → [`00acbfa8`](#insn-00acbfa8)
- ブロック [`00acbfa8`](#insn-00acbfa8) 範囲 `[['00acbfa8', '00acbfc7']]`
  - `FALL_THROUGH` [`00acbfc4`](#insn-00acbfc4) → [`00acbfc8`](#insn-00acbfc8)
- ブロック [`00acbfc8`](#insn-00acbfc8) 範囲 `[['00acbfc8', '00acbfcf']]`
  - `UNCONDITIONAL_JUMP` [`00acbfcc`](#insn-00acbfcc) → [`00acbfd4`](#insn-00acbfd4)
- ブロック [`00acbfd0`](#insn-00acbfd0) 範囲 `[['00acbfd0', '00acbfd3']]`
  - `FALL_THROUGH` [`00acbfd0`](#insn-00acbfd0) → [`00acbfd4`](#insn-00acbfd4)
- ブロック [`00acbfd4`](#insn-00acbfd4) 範囲 `[['00acbfd4', '00acbfe3']]`
  - `CONDITIONAL_JUMP` [`00acbfe0`](#insn-00acbfe0) → [`00acc034`](#insn-00acc034)
  - `FALL_THROUGH` [`00acbfe0`](#insn-00acbfe0) → [`00acbfe4`](#insn-00acbfe4)
- ブロック [`00acbfe4`](#insn-00acbfe4) 範囲 `[['00acbfe4', '00acbff7']]`
- ブロック [`00acc034`](#insn-00acc034) 範囲 `[['00acc034', '00acc037']]`

## 命令位置別の参照

- [`00acbed0`](#insn-00acbed0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbed4`](#insn-00acbed4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbed8`](#insn-00acbed8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbee8`](#insn-00acbee8) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbeec`](#insn-00acbeec) → [`00565f94`](../00565/00565f94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00565f94` · 推定シンボル `None` · 推定型 `None`
- [`00acbef4`](#insn-00acbef4) → [`00566284`](../00566/00566284.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566284` · 推定シンボル `None` · 推定型 `None`
- [`00acbf04`](#insn-00acbf04) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf0c`](#insn-00acbf0c) → `0029bcec`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acbf10`](#insn-00acbf10) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf20`](#insn-00acbf20) → `Stack[-0x47]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf24`](#insn-00acbf24) → `Stack[-0x57]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf28`](#insn-00acbf28) → `Stack[-0x45]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf2c`](#insn-00acbf2c) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf3c`](#insn-00acbf3c) → [`00566448`](../00566/00566448.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566448` · 推定シンボル `None` · 推定型 `None`
- [`00acbf40`](#insn-00acbf40) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf44`](#insn-00acbf44) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf48`](#insn-00acbf48) → [`00acbf54`](#insn-00acbf54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf4c`](#insn-00acbf4c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf50`](#insn-00acbf50) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00acbf54`](#insn-00acbf54) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf58`](#insn-00acbf58) → [`00acbf64`](#insn-00acbf64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf5c`](#insn-00acbf5c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf60`](#insn-00acbf60) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00acbf68`](#insn-00acbf68) → [`0056626c`](../00566/0056626c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0056626c` · 推定シンボル `None` · 推定型 `None`
- [`00acbf6c`](#insn-00acbf6c) → [`00acbfd0`](#insn-00acbfd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf70`](#insn-00acbf70) → [`00566284`](../00566/00566284.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566284` · 推定シンボル `None` · 推定型 `None`
- [`00acbf74`](#insn-00acbf74) → [`00566978`](../00566/00566978.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566978` · 推定シンボル `None` · 推定型 `None`
- [`00acbf78`](#insn-00acbf78) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf7c`](#insn-00acbf7c) → [`00acbfd0`](#insn-00acbfd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf88`](#insn-00acbf88) → [`005533e0`](../00553/005533e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005533e0` · 推定シンボル `None` · 推定型 `None`
- [`00acbfa4`](#insn-00acbfa4) → [`00acbfc8`](#insn-00acbfc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfcc`](#insn-00acbfcc) → [`00acbfd4`](#insn-00acbfd4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfd8`](#insn-00acbfd8) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfe0`](#insn-00acbfe0) → [`00acc034`](#insn-00acc034) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfe4`](#insn-00acbfe4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfe8`](#insn-00acbfe8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfec`](#insn-00acbfec) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc034`](#insn-00acc034) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acbed0`](#insn-00acbed0)

~~~json
{
  "source": "00acbed0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbed4`](#insn-00acbed4)

~~~json
{
  "source": "00acbed4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbed8`](#insn-00acbed8)

~~~json
{
  "source": "00acbed8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbee8`](#insn-00acbee8)

~~~json
{
  "source": "00acbee8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbeec`](#insn-00acbeec)

~~~json
{
  "source": "00acbeec",
  "target": "00565f94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbef4`](#insn-00acbef4)

~~~json
{
  "source": "00acbef4",
  "target": "00566284",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbf04`](#insn-00acbf04)

~~~json
{
  "source": "00acbf04",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf0c`](#insn-00acbf0c)

~~~json
{
  "source": "00acbf0c",
  "target": "0029bcec",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029bcec",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "67657453616665496e736574426f74746f6d00",
  "capture_start": "0029bcec",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acbf10`](#insn-00acbf10)

~~~json
{
  "source": "00acbf10",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf20`](#insn-00acbf20)

~~~json
{
  "source": "00acbf20",
  "target": "Stack[-0x47]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf24`](#insn-00acbf24)

~~~json
{
  "source": "00acbf24",
  "target": "Stack[-0x57]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf28`](#insn-00acbf28)

~~~json
{
  "source": "00acbf28",
  "target": "Stack[-0x45]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf2c`](#insn-00acbf2c)

~~~json
{
  "source": "00acbf2c",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf3c`](#insn-00acbf3c)

~~~json
{
  "source": "00acbf3c",
  "target": "00566448",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbf40`](#insn-00acbf40)

~~~json
{
  "source": "00acbf40",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf44`](#insn-00acbf44)

~~~json
{
  "source": "00acbf44",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf48`](#insn-00acbf48)

~~~json
{
  "source": "00acbf48",
  "target": "00acbf54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf4c`](#insn-00acbf4c)

~~~json
{
  "source": "00acbf4c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf50`](#insn-00acbf50)

~~~json
{
  "source": "00acbf50",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbf54`](#insn-00acbf54)

~~~json
{
  "source": "00acbf54",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf58`](#insn-00acbf58)

~~~json
{
  "source": "00acbf58",
  "target": "00acbf64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf5c`](#insn-00acbf5c)

~~~json
{
  "source": "00acbf5c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf60`](#insn-00acbf60)

~~~json
{
  "source": "00acbf60",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbf68`](#insn-00acbf68)

~~~json
{
  "source": "00acbf68",
  "target": "0056626c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbf6c`](#insn-00acbf6c)

~~~json
{
  "source": "00acbf6c",
  "target": "00acbfd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf70`](#insn-00acbf70)

~~~json
{
  "source": "00acbf70",
  "target": "00566284",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbf74`](#insn-00acbf74)

~~~json
{
  "source": "00acbf74",
  "target": "00566978",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbf78`](#insn-00acbf78)

~~~json
{
  "source": "00acbf78",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf7c`](#insn-00acbf7c)

~~~json
{
  "source": "00acbf7c",
  "target": "00acbfd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf88`](#insn-00acbf88)

~~~json
{
  "source": "00acbf88",
  "target": "005533e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbfa4`](#insn-00acbfa4)

~~~json
{
  "source": "00acbfa4",
  "target": "00acbfc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfcc`](#insn-00acbfcc)

~~~json
{
  "source": "00acbfcc",
  "target": "00acbfd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfd8`](#insn-00acbfd8)

~~~json
{
  "source": "00acbfd8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfe0`](#insn-00acbfe0)

~~~json
{
  "source": "00acbfe0",
  "target": "00acc034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfe4`](#insn-00acbfe4)

~~~json
{
  "source": "00acbfe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfe8`](#insn-00acbfe8)

~~~json
{
  "source": "00acbfe8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfec`](#insn-00acbfec)

~~~json
{
  "source": "00acbfec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc034`](#insn-00acc034)

~~~json
{
  "source": "00acc034",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
