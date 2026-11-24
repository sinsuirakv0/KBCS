# 00acbda4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00acbd60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acbd60.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0059.md#compare-717888041fb4b00d744fb48cbdfcc232)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b2b834`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b834.md) · 移動量 `+0x5fa90`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0054.md#compare-010ccc81fe427e36a35f102ddae89513)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbda4",
  "name": "FUN_00acbda4",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aba472b56121b388ad8136ae7441e715cf47b40ef868e8d461d3d1d2ff058f25",
  "source_text_sha256": "aba472b56121b388ad8136ae7441e715cf47b40ef868e8d461d3d1d2ff058f25",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acbda4",
        "00acbecf"
      ],
      [
        "00acbf0c",
        "00acbf0f"
      ]
    ],
    "bytes_sha256": "8e231c1981b829fd9f0ef858f09820a4bfbf6ff72dca0a9483e64229ad63e67d",
    "instruction_count": 76,
    "instruction_bytes": 304,
    "body_bytes": 304,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [00accf90](../00acc/00accf90.md)

## 呼び出し先

- [005533e0](../00553/005533e0.md)
- [00565f94](../00565/00565f94.md)
- [0056626c](../00566/0056626c.md)
- [00566284](../00566/00566284.md)
- [00566448](../00566/00566448.md)
- [00566978](../00566/00566978.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)

## 関連文字列（未確認候補）

~~~text
"getSafeInsetTop"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2090 bytes

~~~c

void FUN_00acbda4(void)

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
  char local_57 [7];
  char cStack_50;
  char acStack_4f [7];
  undefined1 local_48;
  undefined7 uStack_47;
  long local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  plVar4 = (long *)FUN_00565f94();
  uVar5 = FUN_00566284();
  local_58 = 0x1e;
  local_48 = 0;
  local_57[0] = s_getSafeInsetTop_002963ac[0];
  local_57[1] = s_getSafeInsetTop_002963ac[1];
  local_57[2] = s_getSafeInsetTop_002963ac[2];
  local_57[3] = s_getSafeInsetTop_002963ac[3];
  local_57[4] = s_getSafeInsetTop_002963ac[4];
  local_57[5] = s_getSafeInsetTop_002963ac[5];
  local_57[6] = s_getSafeInsetTop_002963ac[6];
  cStack_50 = s_getSafeInsetTop_002963ac[7];
  acStack_4f[0] = s_getSafeInsetTop_002963ac[8];
  acStack_4f[1] = s_getSafeInsetTop_002963ac[9];
  acStack_4f[2] = s_getSafeInsetTop_002963ac[10];
  acStack_4f[3] = s_getSafeInsetTop_002963ac[0xb];
  acStack_4f[4] = s_getSafeInsetTop_002963ac[0xc];
  acStack_4f[5] = s_getSafeInsetTop_002963ac[0xd];
  acStack_4f[6] = s_getSafeInsetTop_002963ac[0xe];
  local_70[0] = 6;
  local_70[1] = 0x28;
  local_70[2] = 0x29;
  local_70[3] = 0x49;
  local_70[4] = 0;
  local_40 = FUN_00566448(uVar5,&local_58,local_70,plVar4);
  if ((local_70[0] & 1) != 0) {
    _ZdlPv(local_60);
  }
  if ((local_58 & 1) != 0) {
    _ZdlPv((void *)CONCAT71(uStack_47,local_48));
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
      goto LAB_00acbeac;
    }
  }
  uVar3 = 0;
LAB_00acbeac:
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
<a id="insn-00acbda4"></a> `00acbda4` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00acbda8"></a> `00acbda8` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acbdac"></a> `00acbdac` | `f5 2b 00 f9` | str x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acbdb0"></a> `00acbdb0` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acbdb4"></a> `00acbdb4` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00acbdb8"></a> `00acbdb8` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acbdbc"></a> `00acbdbc` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acbdc0"></a> `00acbdc0` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acbdc4"></a> `00acbdc4` | `74 68 ea 97` | bl 0x00565f94 | `UNCONDITIONAL_CALL`
<a id="insn-00acbdc8"></a> `00acbdc8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acbdcc"></a> `00acbdcc` | `2e 69 ea 97` | bl 0x00566284 | `UNCONDITIONAL_CALL`
<a id="insn-00acbdd0"></a> `00acbdd0` | `c8 03 80 52` | mov w8,#0x1e | `FALL_THROUGH`
<a id="insn-00acbdd4"></a> `00acbdd4` | `49 be ff f0` | adrp x9,0x296000 | `FALL_THROUGH`
<a id="insn-00acbdd8"></a> `00acbdd8` | `29 b1 0e 91` | add x9,x9,#0x3ac | `FALL_THROUGH`
<a id="insn-00acbddc"></a> `00acbddc` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00acbde0"></a> `00acbde0` | `e8 63 00 39` | strb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00acbde4"></a> `00acbde4` | `28 71 40 f8` | ldur x8,[x9, #0x7] | `FALL_THROUGH`
<a id="insn-00acbde8"></a> `00acbde8` | `ff a3 00 39` | strb wzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00acbdec"></a> `00acbdec` | `ea 93 01 f8` | stur x10,[sp, #0x19] | `FALL_THROUGH`
<a id="insn-00acbdf0"></a> `00acbdf0` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acbdf4"></a> `00acbdf4` | `c8 00 80 52` | mov w8,#0x6 | `FALL_THROUGH`
<a id="insn-00acbdf8"></a> `00acbdf8` | `e8 03 00 39` | strb w8,[sp] | `FALL_THROUGH`
<a id="insn-00acbdfc"></a> `00acbdfc` | `08 25 85 52` | mov w8,#0x2928 | `FALL_THROUGH`
<a id="insn-00acbe00"></a> `00acbe00` | `28 09 a0 72` | movk w8,#0x49, LSL #16 | `FALL_THROUGH`
<a id="insn-00acbe04"></a> `00acbe04` | `e8 13 00 b8` | stur w8,[sp, #0x1] | `FALL_THROUGH`
<a id="insn-00acbe08"></a> `00acbe08` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00acbe0c"></a> `00acbe0c` | `e2 03 00 91` | mov x2,sp | `FALL_THROUGH`
<a id="insn-00acbe10"></a> `00acbe10` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-00acbe14"></a> `00acbe14` | `8d 69 ea 97` | bl 0x00566448 | `UNCONDITIONAL_CALL`
<a id="insn-00acbe18"></a> `00acbe18` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00acbe1c"></a> `00acbe1c` | `a0 03 1f f8` | stur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00acbe20"></a> `00acbe20` | `68 00 00 36` | tbz w8,#0x0,0x00acbe2c | `CONDITIONAL_JUMP`
<a id="insn-00acbe24"></a> `00acbe24` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acbe28"></a> `00acbe28` | `8e 3c 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00acbe2c"></a> `00acbe2c` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00acbe30"></a> `00acbe30` | `68 00 00 36` | tbz w8,#0x0,0x00acbe3c | `CONDITIONAL_JUMP`
<a id="insn-00acbe34"></a> `00acbe34` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00acbe38"></a> `00acbe38` | `8a 3c 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00acbe3c"></a> `00acbe3c` | `a0 43 00 d1` | sub x0,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00acbe40"></a> `00acbe40` | `0b 69 ea 97` | bl 0x0056626c | `UNCONDITIONAL_CALL`
<a id="insn-00acbe44"></a> `00acbe44` | `20 03 00 36` | tbz w0,#0x0,0x00acbea8 | `CONDITIONAL_JUMP`
<a id="insn-00acbe48"></a> `00acbe48` | `0f 69 ea 97` | bl 0x00566284 | `UNCONDITIONAL_CALL`
<a id="insn-00acbe4c"></a> `00acbe4c` | `cb 6a ea 97` | bl 0x00566978 | `UNCONDITIONAL_CALL`
<a id="insn-00acbe50"></a> `00acbe50` | `a2 03 5f f8` | ldur x2,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00acbe54"></a> `00acbe54` | `a2 02 00 b4` | cbz x2,0x00acbea8 | `CONDITIONAL_JUMP`
<a id="insn-00acbe58"></a> `00acbe58` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00acbe5c"></a> `00acbe5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acbe60"></a> `00acbe60` | `60 1d ea 97` | bl 0x005533e0 | `UNCONDITIONAL_CALL`
<a id="insn-00acbe64"></a> `00acbe64` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00acbe68"></a> `00acbe68` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00acbe6c"></a> `00acbe6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acbe70"></a> `00acbe70` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00acbe74"></a> `00acbe74` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbe78"></a> `00acbe78` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00acbe7c"></a> `00acbe7c` | `20 01 00 54` | b.eq 0x00acbea0 | `CONDITIONAL_JUMP`
<a id="insn-00acbe80"></a> `00acbe80` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00acbe84"></a> `00acbe84` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acbe88"></a> `00acbe88` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00acbe8c"></a> `00acbe8c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbe90"></a> `00acbe90` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00acbe94"></a> `00acbe94` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acbe98"></a> `00acbe98` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00acbe9c"></a> `00acbe9c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbea0"></a> `00acbea0` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00acbea4"></a> `00acbea4` | `02 00 00 14` | b 0x00acbeac | `UNCONDITIONAL_JUMP`
<a id="insn-00acbea8"></a> `00acbea8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00acbeac"></a> `00acbeac` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acbeb0"></a> `00acbeb0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acbeb4"></a> `00acbeb4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acbeb8"></a> `00acbeb8` | `a1 02 00 54` | b.ne 0x00acbf0c | `CONDITIONAL_JUMP`
<a id="insn-00acbebc"></a> `00acbebc` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acbec0"></a> `00acbec0` | `f5 2b 40 f9` | ldr x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acbec4"></a> `00acbec4` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acbec8"></a> `00acbec8` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00acbecc"></a> `00acbecc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acbf0c"></a> `00acbf0c` | `61 3c 04 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acbda4`](#insn-00acbda4) 範囲 `[['00acbda4', '00acbe23']]`
  - `CONDITIONAL_JUMP` [`00acbe20`](#insn-00acbe20) → [`00acbe2c`](#insn-00acbe2c)
  - `FALL_THROUGH` [`00acbe20`](#insn-00acbe20) → [`00acbe24`](#insn-00acbe24)
- ブロック [`00acbe24`](#insn-00acbe24) 範囲 `[['00acbe24', '00acbe2b']]`
  - `FALL_THROUGH` [`00acbe28`](#insn-00acbe28) → [`00acbe2c`](#insn-00acbe2c)
- ブロック [`00acbe2c`](#insn-00acbe2c) 範囲 `[['00acbe2c', '00acbe33']]`
  - `CONDITIONAL_JUMP` [`00acbe30`](#insn-00acbe30) → [`00acbe3c`](#insn-00acbe3c)
  - `FALL_THROUGH` [`00acbe30`](#insn-00acbe30) → [`00acbe34`](#insn-00acbe34)
- ブロック [`00acbe34`](#insn-00acbe34) 範囲 `[['00acbe34', '00acbe3b']]`
  - `FALL_THROUGH` [`00acbe38`](#insn-00acbe38) → [`00acbe3c`](#insn-00acbe3c)
- ブロック [`00acbe3c`](#insn-00acbe3c) 範囲 `[['00acbe3c', '00acbe47']]`
  - `CONDITIONAL_JUMP` [`00acbe44`](#insn-00acbe44) → [`00acbea8`](#insn-00acbea8)
  - `FALL_THROUGH` [`00acbe44`](#insn-00acbe44) → [`00acbe48`](#insn-00acbe48)
- ブロック [`00acbe48`](#insn-00acbe48) 範囲 `[['00acbe48', '00acbe57']]`
  - `CONDITIONAL_JUMP` [`00acbe54`](#insn-00acbe54) → [`00acbea8`](#insn-00acbea8)
  - `FALL_THROUGH` [`00acbe54`](#insn-00acbe54) → [`00acbe58`](#insn-00acbe58)
- ブロック [`00acbe58`](#insn-00acbe58) 範囲 `[['00acbe58', '00acbe7f']]`
  - `CONDITIONAL_JUMP` [`00acbe7c`](#insn-00acbe7c) → [`00acbea0`](#insn-00acbea0)
  - `FALL_THROUGH` [`00acbe7c`](#insn-00acbe7c) → [`00acbe80`](#insn-00acbe80)
- ブロック [`00acbe80`](#insn-00acbe80) 範囲 `[['00acbe80', '00acbe9f']]`
  - `FALL_THROUGH` [`00acbe9c`](#insn-00acbe9c) → [`00acbea0`](#insn-00acbea0)
- ブロック [`00acbea0`](#insn-00acbea0) 範囲 `[['00acbea0', '00acbea7']]`
  - `UNCONDITIONAL_JUMP` [`00acbea4`](#insn-00acbea4) → [`00acbeac`](#insn-00acbeac)
- ブロック [`00acbea8`](#insn-00acbea8) 範囲 `[['00acbea8', '00acbeab']]`
  - `FALL_THROUGH` [`00acbea8`](#insn-00acbea8) → [`00acbeac`](#insn-00acbeac)
- ブロック [`00acbeac`](#insn-00acbeac) 範囲 `[['00acbeac', '00acbebb']]`
  - `CONDITIONAL_JUMP` [`00acbeb8`](#insn-00acbeb8) → [`00acbf0c`](#insn-00acbf0c)
  - `FALL_THROUGH` [`00acbeb8`](#insn-00acbeb8) → [`00acbebc`](#insn-00acbebc)
- ブロック [`00acbebc`](#insn-00acbebc) 範囲 `[['00acbebc', '00acbecf']]`
- ブロック [`00acbf0c`](#insn-00acbf0c) 範囲 `[['00acbf0c', '00acbf0f']]`

## 命令位置別の参照

- [`00acbda8`](#insn-00acbda8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbdac`](#insn-00acbdac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbdb0`](#insn-00acbdb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbdc0`](#insn-00acbdc0) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbdc4`](#insn-00acbdc4) → [`00565f94`](../00565/00565f94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00565f94` · 推定シンボル `None` · 推定型 `None`
- [`00acbdcc`](#insn-00acbdcc) → [`00566284`](../00566/00566284.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566284` · 推定シンボル `None` · 推定型 `None`
- [`00acbddc`](#insn-00acbddc) → `002963ac`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acbde0`](#insn-00acbde0) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbde4`](#insn-00acbde4) → `002963b3`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acbde8`](#insn-00acbde8) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbdec`](#insn-00acbdec) → `Stack[-0x57]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbdf0`](#insn-00acbdf0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbdf8`](#insn-00acbdf8) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe04`](#insn-00acbe04) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe14`](#insn-00acbe14) → [`00566448`](../00566/00566448.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566448` · 推定シンボル `None` · 推定型 `None`
- [`00acbe18`](#insn-00acbe18) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe1c`](#insn-00acbe1c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe20`](#insn-00acbe20) → [`00acbe2c`](#insn-00acbe2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe24`](#insn-00acbe24) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe28`](#insn-00acbe28) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00acbe2c`](#insn-00acbe2c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe30`](#insn-00acbe30) → [`00acbe3c`](#insn-00acbe3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe34`](#insn-00acbe34) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe38`](#insn-00acbe38) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00acbe40`](#insn-00acbe40) → [`0056626c`](../00566/0056626c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0056626c` · 推定シンボル `None` · 推定型 `None`
- [`00acbe44`](#insn-00acbe44) → [`00acbea8`](#insn-00acbea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe48`](#insn-00acbe48) → [`00566284`](../00566/00566284.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566284` · 推定シンボル `None` · 推定型 `None`
- [`00acbe4c`](#insn-00acbe4c) → [`00566978`](../00566/00566978.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566978` · 推定シンボル `None` · 推定型 `None`
- [`00acbe50`](#insn-00acbe50) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe54`](#insn-00acbe54) → [`00acbea8`](#insn-00acbea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe60`](#insn-00acbe60) → [`005533e0`](../00553/005533e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005533e0` · 推定シンボル `None` · 推定型 `None`
- [`00acbe7c`](#insn-00acbe7c) → [`00acbea0`](#insn-00acbea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbea4`](#insn-00acbea4) → [`00acbeac`](#insn-00acbeac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbeb0`](#insn-00acbeb0) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbeb8`](#insn-00acbeb8) → [`00acbf0c`](#insn-00acbf0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbebc`](#insn-00acbebc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbec0`](#insn-00acbec0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbec4`](#insn-00acbec4) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf0c`](#insn-00acbf0c) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acbda8`](#insn-00acbda8)

~~~json
{
  "source": "00acbda8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbdac`](#insn-00acbdac)

~~~json
{
  "source": "00acbdac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbdb0`](#insn-00acbdb0)

~~~json
{
  "source": "00acbdb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbdc0`](#insn-00acbdc0)

~~~json
{
  "source": "00acbdc0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbdc4`](#insn-00acbdc4)

~~~json
{
  "source": "00acbdc4",
  "target": "00565f94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbdcc`](#insn-00acbdcc)

~~~json
{
  "source": "00acbdcc",
  "target": "00566284",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbddc`](#insn-00acbddc)

~~~json
{
  "source": "00acbddc",
  "target": "002963ac",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002963ac",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "67657453616665496e736574546f7000",
  "capture_start": "002963ac",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acbde0`](#insn-00acbde0)

~~~json
{
  "source": "00acbde0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbde4`](#insn-00acbde4)

~~~json
{
  "source": "00acbde4",
  "target": "002963b3",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002963ac",
  "offset": 7,
  "size": 16,
  "datatype": "string",
  "bytes": "67657453616665496e736574546f7000",
  "capture_start": "002963ac",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acbde8`](#insn-00acbde8)

~~~json
{
  "source": "00acbde8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbdec`](#insn-00acbdec)

~~~json
{
  "source": "00acbdec",
  "target": "Stack[-0x57]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbdf0`](#insn-00acbdf0)

~~~json
{
  "source": "00acbdf0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbdf8`](#insn-00acbdf8)

~~~json
{
  "source": "00acbdf8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe04`](#insn-00acbe04)

~~~json
{
  "source": "00acbe04",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe14`](#insn-00acbe14)

~~~json
{
  "source": "00acbe14",
  "target": "00566448",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbe18`](#insn-00acbe18)

~~~json
{
  "source": "00acbe18",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe1c`](#insn-00acbe1c)

~~~json
{
  "source": "00acbe1c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe20`](#insn-00acbe20)

~~~json
{
  "source": "00acbe20",
  "target": "00acbe2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe24`](#insn-00acbe24)

~~~json
{
  "source": "00acbe24",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe28`](#insn-00acbe28)

~~~json
{
  "source": "00acbe28",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbe2c`](#insn-00acbe2c)

~~~json
{
  "source": "00acbe2c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe30`](#insn-00acbe30)

~~~json
{
  "source": "00acbe30",
  "target": "00acbe3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe34`](#insn-00acbe34)

~~~json
{
  "source": "00acbe34",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe38`](#insn-00acbe38)

~~~json
{
  "source": "00acbe38",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbe40`](#insn-00acbe40)

~~~json
{
  "source": "00acbe40",
  "target": "0056626c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbe44`](#insn-00acbe44)

~~~json
{
  "source": "00acbe44",
  "target": "00acbea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe48`](#insn-00acbe48)

~~~json
{
  "source": "00acbe48",
  "target": "00566284",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbe4c`](#insn-00acbe4c)

~~~json
{
  "source": "00acbe4c",
  "target": "00566978",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbe50`](#insn-00acbe50)

~~~json
{
  "source": "00acbe50",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe54`](#insn-00acbe54)

~~~json
{
  "source": "00acbe54",
  "target": "00acbea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe60`](#insn-00acbe60)

~~~json
{
  "source": "00acbe60",
  "target": "005533e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbe7c`](#insn-00acbe7c)

~~~json
{
  "source": "00acbe7c",
  "target": "00acbea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbea4`](#insn-00acbea4)

~~~json
{
  "source": "00acbea4",
  "target": "00acbeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbeb0`](#insn-00acbeb0)

~~~json
{
  "source": "00acbeb0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbeb8`](#insn-00acbeb8)

~~~json
{
  "source": "00acbeb8",
  "target": "00acbf0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbebc`](#insn-00acbebc)

~~~json
{
  "source": "00acbebc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbec0`](#insn-00acbec0)

~~~json
{
  "source": "00acbec0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbec4`](#insn-00acbec4)

~~~json
{
  "source": "00acbec4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf0c`](#insn-00acbf0c)

~~~json
{
  "source": "00acbf0c",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
