# 00b2ccec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b2bcf8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2bcf8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0070.md#compare-d1c61756d8f94c75701b3fe531267c79)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b2ccec",
  "name": "FUN_00b2ccec",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d112cd3313d6d2f26e47d5d44b437f5995ff491f19586fb54987336dba220ad9",
  "source_text_sha256": "d112cd3313d6d2f26e47d5d44b437f5995ff491f19586fb54987336dba220ad9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b2ccec",
        "00b2ce17"
      ],
      [
        "00b2ce54",
        "00b2ce57"
      ]
    ],
    "bytes_sha256": "8457bfa385a734dd545484100c9caea5e2cb9148d524a84b43765c37f41c1a77",
    "instruction_count": 76,
    "instruction_bytes": 304,
    "body_bytes": 304,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [00b2ded8](../00b2d/00b2ded8.md)

## 呼び出し先

- [00576618](../00576/00576618.md)
- [005891cc](../00589/005891cc.md)
- [005894a4](../00589/005894a4.md)
- [005894bc](../00589/005894bc.md)
- [00589680](../00589/00589680.md)
- [00589bb0](../00589/00589bb0.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)

## 関連文字列（未確認候補）

~~~text
"getSafeInsetTop"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2090 bytes

~~~c

void FUN_00b2ccec(void)

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
  plVar4 = (long *)FUN_005891cc();
  uVar5 = FUN_005894bc();
  local_58 = 0x1e;
  local_48 = 0;
  local_57[0] = s_getSafeInsetTop_002a6096[0];
  local_57[1] = s_getSafeInsetTop_002a6096[1];
  local_57[2] = s_getSafeInsetTop_002a6096[2];
  local_57[3] = s_getSafeInsetTop_002a6096[3];
  local_57[4] = s_getSafeInsetTop_002a6096[4];
  local_57[5] = s_getSafeInsetTop_002a6096[5];
  local_57[6] = s_getSafeInsetTop_002a6096[6];
  cStack_50 = s_getSafeInsetTop_002a6096[7];
  acStack_4f[0] = s_getSafeInsetTop_002a6096[8];
  acStack_4f[1] = s_getSafeInsetTop_002a6096[9];
  acStack_4f[2] = s_getSafeInsetTop_002a6096[10];
  acStack_4f[3] = s_getSafeInsetTop_002a6096[0xb];
  acStack_4f[4] = s_getSafeInsetTop_002a6096[0xc];
  acStack_4f[5] = s_getSafeInsetTop_002a6096[0xd];
  acStack_4f[6] = s_getSafeInsetTop_002a6096[0xe];
  local_70[0] = 6;
  local_70[1] = 0x28;
  local_70[2] = 0x29;
  local_70[3] = 0x49;
  local_70[4] = 0;
  local_40 = FUN_00589680(uVar5,&local_58,local_70,plVar4);
  if ((local_70[0] & 1) != 0) {
    _ZdlPv(local_60);
  }
  if ((local_58 & 1) != 0) {
    _ZdlPv((void *)CONCAT71(uStack_47,local_48));
  }
  uVar6 = FUN_005894a4(&local_40);
  if ((uVar6 & 1) != 0) {
    FUN_005894bc();
    uVar5 = FUN_00589bb0();
    if (local_40 != 0) {
      uVar3 = FUN_00576618(plVar4,uVar5);
      cVar2 = (**(code **)(*plVar4 + 0x720))(plVar4);
      if (cVar2 != '\0') {
        (**(code **)(*plVar4 + 0x80))(plVar4);
        (**(code **)(*plVar4 + 0x88))(plVar4);
      }
      goto LAB_00b2cdf4;
    }
  }
  uVar3 = 0;
LAB_00b2cdf4:
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
<a id="insn-00b2ccec"></a> `00b2ccec` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00b2ccf0"></a> `00b2ccf0` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b2ccf4"></a> `00b2ccf4` | `f5 2b 00 f9` | str x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b2ccf8"></a> `00b2ccf8` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b2ccfc"></a> `00b2ccfc` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00b2cd00"></a> `00b2cd00` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b2cd04"></a> `00b2cd04` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00b2cd08"></a> `00b2cd08` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00b2cd0c"></a> `00b2cd0c` | `30 71 e9 97` | bl 0x005891cc | `UNCONDITIONAL_CALL`
<a id="insn-00b2cd10"></a> `00b2cd10` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b2cd14"></a> `00b2cd14` | `ea 71 e9 97` | bl 0x005894bc | `UNCONDITIONAL_CALL`
<a id="insn-00b2cd18"></a> `00b2cd18` | `c8 03 80 52` | mov w8,#0x1e | `FALL_THROUGH`
<a id="insn-00b2cd1c"></a> `00b2cd1c` | `c9 bb ff d0` | adrp x9,0x2a6000 | `FALL_THROUGH`
<a id="insn-00b2cd20"></a> `00b2cd20` | `29 59 02 91` | add x9,x9,#0x96 | `FALL_THROUGH`
<a id="insn-00b2cd24"></a> `00b2cd24` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00b2cd28"></a> `00b2cd28` | `e8 63 00 39` | strb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b2cd2c"></a> `00b2cd2c` | `28 71 40 f8` | ldur x8,[x9, #0x7] | `FALL_THROUGH`
<a id="insn-00b2cd30"></a> `00b2cd30` | `ff a3 00 39` | strb wzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b2cd34"></a> `00b2cd34` | `ea 93 01 f8` | stur x10,[sp, #0x19] | `FALL_THROUGH`
<a id="insn-00b2cd38"></a> `00b2cd38` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b2cd3c"></a> `00b2cd3c` | `c8 00 80 52` | mov w8,#0x6 | `FALL_THROUGH`
<a id="insn-00b2cd40"></a> `00b2cd40` | `e8 03 00 39` | strb w8,[sp] | `FALL_THROUGH`
<a id="insn-00b2cd44"></a> `00b2cd44` | `08 25 85 52` | mov w8,#0x2928 | `FALL_THROUGH`
<a id="insn-00b2cd48"></a> `00b2cd48` | `28 09 a0 72` | movk w8,#0x49, LSL #16 | `FALL_THROUGH`
<a id="insn-00b2cd4c"></a> `00b2cd4c` | `e8 13 00 b8` | stur w8,[sp, #0x1] | `FALL_THROUGH`
<a id="insn-00b2cd50"></a> `00b2cd50` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00b2cd54"></a> `00b2cd54` | `e2 03 00 91` | mov x2,sp | `FALL_THROUGH`
<a id="insn-00b2cd58"></a> `00b2cd58` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-00b2cd5c"></a> `00b2cd5c` | `49 72 e9 97` | bl 0x00589680 | `UNCONDITIONAL_CALL`
<a id="insn-00b2cd60"></a> `00b2cd60` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00b2cd64"></a> `00b2cd64` | `a0 03 1f f8` | stur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00b2cd68"></a> `00b2cd68` | `68 00 00 36` | tbz w8,#0x0,0x00b2cd74 | `CONDITIONAL_JUMP`
<a id="insn-00b2cd6c"></a> `00b2cd6c` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b2cd70"></a> `00b2cd70` | `78 b0 04 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b2cd74"></a> `00b2cd74` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b2cd78"></a> `00b2cd78` | `68 00 00 36` | tbz w8,#0x0,0x00b2cd84 | `CONDITIONAL_JUMP`
<a id="insn-00b2cd7c"></a> `00b2cd7c` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b2cd80"></a> `00b2cd80` | `74 b0 04 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b2cd84"></a> `00b2cd84` | `a0 43 00 d1` | sub x0,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00b2cd88"></a> `00b2cd88` | `c7 71 e9 97` | bl 0x005894a4 | `UNCONDITIONAL_CALL`
<a id="insn-00b2cd8c"></a> `00b2cd8c` | `20 03 00 36` | tbz w0,#0x0,0x00b2cdf0 | `CONDITIONAL_JUMP`
<a id="insn-00b2cd90"></a> `00b2cd90` | `cb 71 e9 97` | bl 0x005894bc | `UNCONDITIONAL_CALL`
<a id="insn-00b2cd94"></a> `00b2cd94` | `87 73 e9 97` | bl 0x00589bb0 | `UNCONDITIONAL_CALL`
<a id="insn-00b2cd98"></a> `00b2cd98` | `a2 03 5f f8` | ldur x2,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00b2cd9c"></a> `00b2cd9c` | `a2 02 00 b4` | cbz x2,0x00b2cdf0 | `CONDITIONAL_JUMP`
<a id="insn-00b2cda0"></a> `00b2cda0` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00b2cda4"></a> `00b2cda4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b2cda8"></a> `00b2cda8` | `1c 26 e9 97` | bl 0x00576618 | `UNCONDITIONAL_CALL`
<a id="insn-00b2cdac"></a> `00b2cdac` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b2cdb0"></a> `00b2cdb0` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00b2cdb4"></a> `00b2cdb4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b2cdb8"></a> `00b2cdb8` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00b2cdbc"></a> `00b2cdbc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b2cdc0"></a> `00b2cdc0` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00b2cdc4"></a> `00b2cdc4` | `20 01 00 54` | b.eq 0x00b2cde8 | `CONDITIONAL_JUMP`
<a id="insn-00b2cdc8"></a> `00b2cdc8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b2cdcc"></a> `00b2cdcc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b2cdd0"></a> `00b2cdd0` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00b2cdd4"></a> `00b2cdd4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b2cdd8"></a> `00b2cdd8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b2cddc"></a> `00b2cddc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b2cde0"></a> `00b2cde0` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00b2cde4"></a> `00b2cde4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b2cde8"></a> `00b2cde8` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00b2cdec"></a> `00b2cdec` | `02 00 00 14` | b 0x00b2cdf4 | `UNCONDITIONAL_JUMP`
<a id="insn-00b2cdf0"></a> `00b2cdf0` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b2cdf4"></a> `00b2cdf4` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00b2cdf8"></a> `00b2cdf8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00b2cdfc"></a> `00b2cdfc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b2ce00"></a> `00b2ce00` | `a1 02 00 54` | b.ne 0x00b2ce54 | `CONDITIONAL_JUMP`
<a id="insn-00b2ce04"></a> `00b2ce04` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b2ce08"></a> `00b2ce08` | `f5 2b 40 f9` | ldr x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b2ce0c"></a> `00b2ce0c` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b2ce10"></a> `00b2ce10` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00b2ce14"></a> `00b2ce14` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b2ce54"></a> `00b2ce54` | `4b b0 04 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b2ccec`](#insn-00b2ccec) 範囲 `[['00b2ccec', '00b2cd6b']]`
  - `CONDITIONAL_JUMP` [`00b2cd68`](#insn-00b2cd68) → [`00b2cd74`](#insn-00b2cd74)
  - `FALL_THROUGH` [`00b2cd68`](#insn-00b2cd68) → [`00b2cd6c`](#insn-00b2cd6c)
- ブロック [`00b2cd6c`](#insn-00b2cd6c) 範囲 `[['00b2cd6c', '00b2cd73']]`
  - `FALL_THROUGH` [`00b2cd70`](#insn-00b2cd70) → [`00b2cd74`](#insn-00b2cd74)
- ブロック [`00b2cd74`](#insn-00b2cd74) 範囲 `[['00b2cd74', '00b2cd7b']]`
  - `CONDITIONAL_JUMP` [`00b2cd78`](#insn-00b2cd78) → [`00b2cd84`](#insn-00b2cd84)
  - `FALL_THROUGH` [`00b2cd78`](#insn-00b2cd78) → [`00b2cd7c`](#insn-00b2cd7c)
- ブロック [`00b2cd7c`](#insn-00b2cd7c) 範囲 `[['00b2cd7c', '00b2cd83']]`
  - `FALL_THROUGH` [`00b2cd80`](#insn-00b2cd80) → [`00b2cd84`](#insn-00b2cd84)
- ブロック [`00b2cd84`](#insn-00b2cd84) 範囲 `[['00b2cd84', '00b2cd8f']]`
  - `CONDITIONAL_JUMP` [`00b2cd8c`](#insn-00b2cd8c) → [`00b2cdf0`](#insn-00b2cdf0)
  - `FALL_THROUGH` [`00b2cd8c`](#insn-00b2cd8c) → [`00b2cd90`](#insn-00b2cd90)
- ブロック [`00b2cd90`](#insn-00b2cd90) 範囲 `[['00b2cd90', '00b2cd9f']]`
  - `CONDITIONAL_JUMP` [`00b2cd9c`](#insn-00b2cd9c) → [`00b2cdf0`](#insn-00b2cdf0)
  - `FALL_THROUGH` [`00b2cd9c`](#insn-00b2cd9c) → [`00b2cda0`](#insn-00b2cda0)
- ブロック [`00b2cda0`](#insn-00b2cda0) 範囲 `[['00b2cda0', '00b2cdc7']]`
  - `CONDITIONAL_JUMP` [`00b2cdc4`](#insn-00b2cdc4) → [`00b2cde8`](#insn-00b2cde8)
  - `FALL_THROUGH` [`00b2cdc4`](#insn-00b2cdc4) → [`00b2cdc8`](#insn-00b2cdc8)
- ブロック [`00b2cdc8`](#insn-00b2cdc8) 範囲 `[['00b2cdc8', '00b2cde7']]`
  - `FALL_THROUGH` [`00b2cde4`](#insn-00b2cde4) → [`00b2cde8`](#insn-00b2cde8)
- ブロック [`00b2cde8`](#insn-00b2cde8) 範囲 `[['00b2cde8', '00b2cdef']]`
  - `UNCONDITIONAL_JUMP` [`00b2cdec`](#insn-00b2cdec) → [`00b2cdf4`](#insn-00b2cdf4)
- ブロック [`00b2cdf0`](#insn-00b2cdf0) 範囲 `[['00b2cdf0', '00b2cdf3']]`
  - `FALL_THROUGH` [`00b2cdf0`](#insn-00b2cdf0) → [`00b2cdf4`](#insn-00b2cdf4)
- ブロック [`00b2cdf4`](#insn-00b2cdf4) 範囲 `[['00b2cdf4', '00b2ce03']]`
  - `CONDITIONAL_JUMP` [`00b2ce00`](#insn-00b2ce00) → [`00b2ce54`](#insn-00b2ce54)
  - `FALL_THROUGH` [`00b2ce00`](#insn-00b2ce00) → [`00b2ce04`](#insn-00b2ce04)
- ブロック [`00b2ce04`](#insn-00b2ce04) 範囲 `[['00b2ce04', '00b2ce17']]`
- ブロック [`00b2ce54`](#insn-00b2ce54) 範囲 `[['00b2ce54', '00b2ce57']]`

## 命令位置別の参照

- [`00b2ccf0`](#insn-00b2ccf0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ccf4`](#insn-00b2ccf4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ccf8`](#insn-00b2ccf8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2cd08`](#insn-00b2cd08) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2cd0c`](#insn-00b2cd0c) → [`005891cc`](../00589/005891cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005891cc` · 推定シンボル `None` · 推定型 `None`
- [`00b2cd14`](#insn-00b2cd14) → [`005894bc`](../00589/005894bc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005894bc` · 推定シンボル `None` · 推定型 `None`
- [`00b2cd24`](#insn-00b2cd24) → `002a6096`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b2cd28`](#insn-00b2cd28) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2cd2c`](#insn-00b2cd2c) → `002a609d`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b2cd30`](#insn-00b2cd30) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2cd34`](#insn-00b2cd34) → `Stack[-0x57]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2cd38`](#insn-00b2cd38) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2cd40`](#insn-00b2cd40) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2cd4c`](#insn-00b2cd4c) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2cd5c`](#insn-00b2cd5c) → [`00589680`](../00589/00589680.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00589680` · 推定シンボル `None` · 推定型 `None`
- [`00b2cd60`](#insn-00b2cd60) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2cd64`](#insn-00b2cd64) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2cd68`](#insn-00b2cd68) → [`00b2cd74`](#insn-00b2cd74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2cd6c`](#insn-00b2cd6c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2cd70`](#insn-00b2cd70) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b2cd74`](#insn-00b2cd74) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2cd78`](#insn-00b2cd78) → [`00b2cd84`](#insn-00b2cd84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2cd7c`](#insn-00b2cd7c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2cd80`](#insn-00b2cd80) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b2cd88`](#insn-00b2cd88) → [`005894a4`](../00589/005894a4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005894a4` · 推定シンボル `None` · 推定型 `None`
- [`00b2cd8c`](#insn-00b2cd8c) → [`00b2cdf0`](#insn-00b2cdf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2cd90`](#insn-00b2cd90) → [`005894bc`](../00589/005894bc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005894bc` · 推定シンボル `None` · 推定型 `None`
- [`00b2cd94`](#insn-00b2cd94) → [`00589bb0`](../00589/00589bb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00589bb0` · 推定シンボル `None` · 推定型 `None`
- [`00b2cd98`](#insn-00b2cd98) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2cd9c`](#insn-00b2cd9c) → [`00b2cdf0`](#insn-00b2cdf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2cda8`](#insn-00b2cda8) → [`00576618`](../00576/00576618.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00576618` · 推定シンボル `None` · 推定型 `None`
- [`00b2cdc4`](#insn-00b2cdc4) → [`00b2cde8`](#insn-00b2cde8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2cdec`](#insn-00b2cdec) → [`00b2cdf4`](#insn-00b2cdf4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2cdf8`](#insn-00b2cdf8) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ce00`](#insn-00b2ce00) → [`00b2ce54`](#insn-00b2ce54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ce04`](#insn-00b2ce04) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ce08`](#insn-00b2ce08) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ce0c`](#insn-00b2ce0c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ce54`](#insn-00b2ce54) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b2ccf0`](#insn-00b2ccf0)

~~~json
{
  "source": "00b2ccf0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ccf4`](#insn-00b2ccf4)

~~~json
{
  "source": "00b2ccf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ccf8`](#insn-00b2ccf8)

~~~json
{
  "source": "00b2ccf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2cd08`](#insn-00b2cd08)

~~~json
{
  "source": "00b2cd08",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2cd0c`](#insn-00b2cd0c)

~~~json
{
  "source": "00b2cd0c",
  "target": "005891cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2cd14`](#insn-00b2cd14)

~~~json
{
  "source": "00b2cd14",
  "target": "005894bc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2cd24`](#insn-00b2cd24)

~~~json
{
  "source": "00b2cd24",
  "target": "002a6096",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a6096",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "67657453616665496e736574546f7000",
  "capture_start": "002a6096",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b2cd28`](#insn-00b2cd28)

~~~json
{
  "source": "00b2cd28",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2cd2c`](#insn-00b2cd2c)

~~~json
{
  "source": "00b2cd2c",
  "target": "002a609d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a6096",
  "offset": 7,
  "size": 16,
  "datatype": "string",
  "bytes": "67657453616665496e736574546f7000",
  "capture_start": "002a6096",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b2cd30`](#insn-00b2cd30)

~~~json
{
  "source": "00b2cd30",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2cd34`](#insn-00b2cd34)

~~~json
{
  "source": "00b2cd34",
  "target": "Stack[-0x57]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2cd38`](#insn-00b2cd38)

~~~json
{
  "source": "00b2cd38",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2cd40`](#insn-00b2cd40)

~~~json
{
  "source": "00b2cd40",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2cd4c`](#insn-00b2cd4c)

~~~json
{
  "source": "00b2cd4c",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2cd5c`](#insn-00b2cd5c)

~~~json
{
  "source": "00b2cd5c",
  "target": "00589680",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2cd60`](#insn-00b2cd60)

~~~json
{
  "source": "00b2cd60",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2cd64`](#insn-00b2cd64)

~~~json
{
  "source": "00b2cd64",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2cd68`](#insn-00b2cd68)

~~~json
{
  "source": "00b2cd68",
  "target": "00b2cd74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2cd6c`](#insn-00b2cd6c)

~~~json
{
  "source": "00b2cd6c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2cd70`](#insn-00b2cd70)

~~~json
{
  "source": "00b2cd70",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2cd74`](#insn-00b2cd74)

~~~json
{
  "source": "00b2cd74",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2cd78`](#insn-00b2cd78)

~~~json
{
  "source": "00b2cd78",
  "target": "00b2cd84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2cd7c`](#insn-00b2cd7c)

~~~json
{
  "source": "00b2cd7c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2cd80`](#insn-00b2cd80)

~~~json
{
  "source": "00b2cd80",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2cd88`](#insn-00b2cd88)

~~~json
{
  "source": "00b2cd88",
  "target": "005894a4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2cd8c`](#insn-00b2cd8c)

~~~json
{
  "source": "00b2cd8c",
  "target": "00b2cdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2cd90`](#insn-00b2cd90)

~~~json
{
  "source": "00b2cd90",
  "target": "005894bc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2cd94`](#insn-00b2cd94)

~~~json
{
  "source": "00b2cd94",
  "target": "00589bb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2cd98`](#insn-00b2cd98)

~~~json
{
  "source": "00b2cd98",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2cd9c`](#insn-00b2cd9c)

~~~json
{
  "source": "00b2cd9c",
  "target": "00b2cdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2cda8`](#insn-00b2cda8)

~~~json
{
  "source": "00b2cda8",
  "target": "00576618",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2cdc4`](#insn-00b2cdc4)

~~~json
{
  "source": "00b2cdc4",
  "target": "00b2cde8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2cdec`](#insn-00b2cdec)

~~~json
{
  "source": "00b2cdec",
  "target": "00b2cdf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2cdf8`](#insn-00b2cdf8)

~~~json
{
  "source": "00b2cdf8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ce00`](#insn-00b2ce00)

~~~json
{
  "source": "00b2ce00",
  "target": "00b2ce54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ce04`](#insn-00b2ce04)

~~~json
{
  "source": "00b2ce04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ce08`](#insn-00b2ce08)

~~~json
{
  "source": "00b2ce08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ce0c`](#insn-00b2ce0c)

~~~json
{
  "source": "00b2ce0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ce54`](#insn-00b2ce54)

~~~json
{
  "source": "00b2ce54",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
