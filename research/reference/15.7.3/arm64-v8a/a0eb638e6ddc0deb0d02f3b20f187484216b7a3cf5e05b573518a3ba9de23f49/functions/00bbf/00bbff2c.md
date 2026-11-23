# 00bbff2c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbfe64`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbfe64.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-4adf1c40939be4962c12b59b92658506)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bbff70`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbff70.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-ac070929a58c79cb0bf04958d27aa4bf)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbff2c",
  "name": "FUN_00bbff2c",
  "size": 348,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d932ff9ccbba6e0c3a52a714174705e52694548abbfd5f71d81a98f3681a81fb",
  "source_text_sha256": "d932ff9ccbba6e0c3a52a714174705e52694548abbfd5f71d81a98f3681a81fb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbff2c",
        "00bc0087"
      ]
    ],
    "bytes_sha256": "45ad14b4b98a0d4042db61f73790a4a59f7c3e191d8ec6b95bfcf3dddd4d9bb4",
    "instruction_count": 87,
    "instruction_bytes": 348,
    "body_bytes": 348,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bbd2c4](../00bbd/00bbd2c4.md)
- [00bbfa8c](../00bbf/00bbfa8c.md)
- [00bc1710](../00bc1/00bc1710.md)
- [00bc245c](../00bc2/00bc245c.md)
- [00bc2ec8](../00bc2/00bc2ec8.md)
- [00bc5b0c](../00bc5/00bc5b0c.md)
- [00bc5fdc](../00bc5/00bc5fdc.md)
- [00bc966c](../00bc9/00bc966c.md)
- [00bca980](../00bca/00bca980.md)
- [00bd118c](../00bd1/00bd118c.md)

## 呼び出し先

- [00bbb158](../00bbb/00bbb158.md)
- [00bdb0a0](../00bdb/00bdb0a0.md)
- [00bdb180](../00bdb/00bdb180.md)
- [00bdd180](../00bdd/00bdd180.md)

## 関連文字列（未確認候補）

~~~text
"%s:%d: %s"
"out/llvm-project/libcxxabi/src/demangle/ItaniumDemangle.h"
"shrinkToSize() can't expand!"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2275 bytes

~~~c

undefined1  [16] FUN_00bbff2c(long param_1,ulong param_2)

{
  void *__src;
  void *pvVar1;
  undefined8 *puVar2;
  long lVar3;
  size_t __n;
  undefined8 *puVar4;
  long lVar5;
  ulong uVar6;
  ulong uVar7;
  undefined1 auVar8 [16];
  
                    /* try { // try from 00bbff34 to 00cbff3f has its CatchHandler @ 00bc838c */
  lVar5 = *(long *)(param_1 + 0x10);
  pvVar1 = *(void **)(param_1 + 0x18);
  uVar6 = (long)pvVar1 - lVar5 >> 3;
  if (uVar6 < param_2) {
                    /* WARNING: Subroutine does not return */
    FUN_00bbb158("%s:%d: %s","out/llvm-project/libcxxabi/src/demangle/ItaniumDemangle.h",0xaa0,
                 &DAT_00296866);
  }
  __src = (void *)(lVar5 + param_2 * 8);
  puVar4 = *(undefined8 **)(param_1 + 0x1330);
  __n = (long)pvVar1 - (long)__src;
  lVar3 = puVar4[1];
  uVar7 = (ulong)((int)__n + 0xf) & 0xfffffff0;
  puVar2 = puVar4;
  if (0xfef < lVar3 + uVar7) {
    if (0xff0 < uVar7) {
      puVar2 = malloc(uVar7 + 0x10);
      if (puVar2 == (undefined8 *)0x0) {
LAB_00bc0084:
                    /* WARNING: Subroutine does not return */
        _ZSt9terminatev();
      }
      *puVar2 = *puVar4;
      puVar2[1] = 0;
      *puVar4 = puVar2;
      puVar2 = puVar2 + 2;
      goto joined_r0x00bbffec;
    }
    puVar2 = malloc(0x1000);
    if (puVar2 == (undefined8 *)0x0) goto LAB_00bc0084;
    lVar3 = 0;
    *puVar2 = puVar4;
    puVar2[1] = 0;
    *(undefined8 **)(param_1 + 0x1330) = puVar2;
  }
                    /* try { // try from 00bbffd8 to 00cbffdf has its CatchHandler @ 00bc8be8 */
  puVar2[1] = lVar3 + uVar7;
  puVar2 = (undefined8 *)((long)puVar2 + lVar3 + 0x10);
joined_r0x00bbffec:
  if (pvVar1 != __src) {
    memmove(puVar2,__src,__n);
    lVar5 = *(long *)(param_1 + 0x10);
    uVar6 = *(long *)(param_1 + 0x18) - lVar5 >> 3;
  }
  if (param_2 <= uVar6) {
                    /* try { // try from 00bc0018 to 00cc0023 has its CatchHandler @ 00bc8910 */
    auVar8._8_8_ = (long)__n >> 3;
    *(ulong *)(param_1 + 0x18) = lVar5 + param_2 * 8;
    auVar8._0_8_ = puVar2;
    return auVar8;
  }
                    /* WARNING: Subroutine does not return */
  FUN_00bbb158("%s:%d: %s","out/llvm-project/libcxxabi/src/demangle/ItaniumDemangle.h",0x87,
               "shrinkToSize() can\'t expand!");
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbff2c"></a> `00bbff2c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbff30"></a> `00bbff30` | `fd 7b ba a9` | stp x29,x30,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00bbff34"></a> `00bbff34` | `fb 0b 00 f9` | str x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbff38"></a> `00bbff38` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbff3c"></a> `00bbff3c` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbff40"></a> `00bbff40` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbff44"></a> `00bbff44` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbff48"></a> `00bbff48` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbff4c"></a> `00bbff4c` | `18 68 41 a9` | ldp x24,x26,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbff50"></a> `00bbff50` | `48 03 18 cb` | sub x8,x26,x24 | `FALL_THROUGH`
<a id="insn-00bbff54"></a> `00bbff54` | `19 fd 43 93` | asr x25,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bbff58"></a> `00bbff58` | `3f 03 01 eb` | cmp x25,x1 | `FALL_THROUGH`
<a id="insn-00bbff5c"></a> `00bbff5c` | `43 07 00 54` | b.cc 0x00bc0044 | `CONDITIONAL_JUMP`
<a id="insn-00bbff60"></a> `00bbff60` | `16 0f 01 8b` | add x22,x24,x1, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bbff64"></a> `00bbff64` | `17 98 49 f9` | ldr x23,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbff68"></a> `00bbff68` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbff6c"></a> `00bbff6c` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bbff70"></a> `00bbff70` | `55 03 16 cb` | sub x21,x26,x22 | `FALL_THROUGH`
<a id="insn-00bbff74"></a> `00bbff74` | `e8 06 40 f9` | ldr x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bbff78"></a> `00bbff78` | `a9 3e 00 11` | add w9,w21,#0xf | `FALL_THROUGH`
<a id="insn-00bbff7c"></a> `00bbff7c` | `3b 6d 7c 92` | and x27,x9,#0xfffffff0 | `FALL_THROUGH`
<a id="insn-00bbff80"></a> `00bbff80` | `09 01 1b 8b` | add x9,x8,x27 | `FALL_THROUGH`
<a id="insn-00bbff84"></a> `00bbff84` | `3f c1 3f f1` | cmp x9,#0xff0 | `FALL_THROUGH`
<a id="insn-00bbff88"></a> `00bbff88` | `83 02 00 54` | b.cc 0x00bbffd8 | `CONDITIONAL_JUMP`
<a id="insn-00bbff8c"></a> `00bbff8c` | `7f c7 3f f1` | cmp x27,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbff90"></a> `00bbff90` | `63 01 00 54` | b.cc 0x00bbffbc | `CONDITIONAL_JUMP`
<a id="insn-00bbff94"></a> `00bbff94` | `60 43 00 91` | add x0,x27,#0x10 | `FALL_THROUGH`
<a id="insn-00bbff98"></a> `00bbff98` | `7a 74 00 94` | bl 0x00bdd180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbff9c"></a> `00bbff9c` | `40 07 00 b4` | cbz x0,0x00bc0084 | `CONDITIONAL_JUMP`
<a id="insn-00bbffa0"></a> `00bbffa0` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00bbffa4"></a> `00bbffa4` | `08 7c 00 a9` | stp x8,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbffa8"></a> `00bbffa8` | `e0 02 00 f9` | str x0,[x23] | `FALL_THROUGH`
<a id="insn-00bbffac"></a> `00bbffac` | `17 40 00 91` | add x23,x0,#0x10 | `FALL_THROUGH`
<a id="insn-00bbffb0"></a> `00bbffb0` | `5f 03 16 eb` | cmp x26,x22 | `FALL_THROUGH`
<a id="insn-00bbffb4"></a> `00bbffb4` | `e1 01 00 54` | b.ne 0x00bbfff0 | `CONDITIONAL_JUMP`
<a id="insn-00bbffb8"></a> `00bbffb8` | `15 00 00 14` | b 0x00bc000c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbffbc"></a> `00bbffbc` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbffc0"></a> `00bbffc0` | `70 74 00 94` | bl 0x00bdd180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbffc4"></a> `00bbffc4` | `00 06 00 b4` | cbz x0,0x00bc0084 | `CONDITIONAL_JUMP`
<a id="insn-00bbffc8"></a> `00bbffc8` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbffcc"></a> `00bbffcc` | `17 7c 00 a9` | stp x23,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbffd0"></a> `00bbffd0` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bbffd4"></a> `00bbffd4` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbffd8"></a> `00bbffd8` | `09 01 1b 8b` | add x9,x8,x27 | `FALL_THROUGH`
<a id="insn-00bbffdc"></a> `00bbffdc` | `e8 02 08 8b` | add x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00bbffe0"></a> `00bbffe0` | `e9 06 00 f9` | str x9,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bbffe4"></a> `00bbffe4` | `17 41 00 91` | add x23,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bbffe8"></a> `00bbffe8` | `5f 03 16 eb` | cmp x26,x22 | `FALL_THROUGH`
<a id="insn-00bbffec"></a> `00bbffec` | `00 01 00 54` | b.eq 0x00bc000c | `CONDITIONAL_JUMP`
<a id="insn-00bbfff0"></a> `00bbfff0` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbfff4"></a> `00bbfff4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbfff8"></a> `00bbfff8` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bbfffc"></a> `00bbfffc` | `29 6c 00 94` | bl 0x00bdb0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc0000"></a> `00bc0000` | `78 22 41 a9` | ldp x24,x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bc0004"></a> `00bc0004` | `08 01 18 cb` | sub x8,x8,x24 | `FALL_THROUGH`
<a id="insn-00bc0008"></a> `00bc0008` | `19 fd 43 93` | asr x25,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bc000c"></a> `00bc000c` | `3f 03 14 eb` | cmp x25,x20 | `FALL_THROUGH`
<a id="insn-00bc0010"></a> `00bc0010` | `a3 02 00 54` | b.cc 0x00bc0064 | `CONDITIONAL_JUMP`
<a id="insn-00bc0014"></a> `00bc0014` | `08 0f 14 8b` | add x8,x24,x20, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bc0018"></a> `00bc0018` | `a1 fe 43 93` | asr x1,x21,#0x3 | `FALL_THROUGH`
<a id="insn-00bc001c"></a> `00bc001c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bc0020"></a> `00bc0020` | `68 0e 00 f9` | str x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bc0024"></a> `00bc0024` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bc0028"></a> `00bc0028` | `fb 0b 40 f9` | ldr x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc002c"></a> `00bc002c` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bc0030"></a> `00bc0030` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bc0034"></a> `00bc0034` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc0038"></a> `00bc0038` | `fd 7b c6 a8` | ldp x29,x30,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00bc003c"></a> `00bc003c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bc0040"></a> `00bc0040` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bc0044"></a> `00bc0044` | `80 b6 ff b0` | adrp x0,0x291000 | `FALL_THROUGH`
<a id="insn-00bc0048"></a> `00bc0048` | `00 f0 1f 91` | add x0,x0,#0x7fc | `FALL_THROUGH`
<a id="insn-00bc004c"></a> `00bc004c` | `01 b7 ff d0` | adrp x1,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bc0050"></a> `00bc0050` | `21 28 04 91` | add x1,x1,#0x10a | `FALL_THROUGH`
<a id="insn-00bc0054"></a> `00bc0054` | `a3 b6 ff d0` | adrp x3,0x296000 | `FALL_THROUGH`
<a id="insn-00bc0058"></a> `00bc0058` | `63 98 21 91` | add x3,x3,#0x866 | `FALL_THROUGH`
<a id="insn-00bc005c"></a> `00bc005c` | `02 54 81 52` | mov w2,#0xaa0 | `FALL_THROUGH`
<a id="insn-00bc0060"></a> `00bc0060` | `3e ec ff 97` | bl 0x00bbb158 | `CALL_TERMINATOR`
<a id="insn-00bc0064"></a> `00bc0064` | `80 b6 ff b0` | adrp x0,0x291000 | `FALL_THROUGH`
<a id="insn-00bc0068"></a> `00bc0068` | `00 f0 1f 91` | add x0,x0,#0x7fc | `FALL_THROUGH`
<a id="insn-00bc006c"></a> `00bc006c` | `01 b7 ff d0` | adrp x1,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bc0070"></a> `00bc0070` | `21 28 04 91` | add x1,x1,#0x10a | `FALL_THROUGH`
<a id="insn-00bc0074"></a> `00bc0074` | `03 b7 ff d0` | adrp x3,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bc0078"></a> `00bc0078` | `63 10 05 91` | add x3,x3,#0x144 | `FALL_THROUGH`
<a id="insn-00bc007c"></a> `00bc007c` | `e2 10 80 52` | mov w2,#0x87 | `FALL_THROUGH`
<a id="insn-00bc0080"></a> `00bc0080` | `36 ec ff 97` | bl 0x00bbb158 | `CALL_TERMINATOR`
<a id="insn-00bc0084"></a> `00bc0084` | `3f 6c 00 94` | bl 0x00bdb180 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbff2c`](#insn-00bbff2c) 範囲 `[['00bbff2c', '00bbff33']]`
  - `FALL_THROUGH` [`00bbff30`](#insn-00bbff30) → [`00bbff34`](#insn-00bbff34)
- ブロック [`00bbff34`](#insn-00bbff34) 範囲 `[['00bbff34', '00bbff5f']]`
  - `CONDITIONAL_JUMP` [`00bbff5c`](#insn-00bbff5c) → [`00bc0044`](#insn-00bc0044)
  - `FALL_THROUGH` [`00bbff5c`](#insn-00bbff5c) → [`00bbff60`](#insn-00bbff60)
- ブロック [`00bbff60`](#insn-00bbff60) 範囲 `[['00bbff60', '00bbff8b']]`
  - `CONDITIONAL_JUMP` [`00bbff88`](#insn-00bbff88) → [`00bbffd8`](#insn-00bbffd8)
  - `FALL_THROUGH` [`00bbff88`](#insn-00bbff88) → [`00bbff8c`](#insn-00bbff8c)
- ブロック [`00bbff8c`](#insn-00bbff8c) 範囲 `[['00bbff8c', '00bbff93']]`
  - `CONDITIONAL_JUMP` [`00bbff90`](#insn-00bbff90) → [`00bbffbc`](#insn-00bbffbc)
  - `FALL_THROUGH` [`00bbff90`](#insn-00bbff90) → [`00bbff94`](#insn-00bbff94)
- ブロック [`00bbff94`](#insn-00bbff94) 範囲 `[['00bbff94', '00bbff9f']]`
  - `CONDITIONAL_JUMP` [`00bbff9c`](#insn-00bbff9c) → [`00bc0084`](#insn-00bc0084)
  - `FALL_THROUGH` [`00bbff9c`](#insn-00bbff9c) → [`00bbffa0`](#insn-00bbffa0)
- ブロック [`00bbffa0`](#insn-00bbffa0) 範囲 `[['00bbffa0', '00bbffb7']]`
  - `CONDITIONAL_JUMP` [`00bbffb4`](#insn-00bbffb4) → [`00bbfff0`](#insn-00bbfff0)
  - `FALL_THROUGH` [`00bbffb4`](#insn-00bbffb4) → [`00bbffb8`](#insn-00bbffb8)
- ブロック [`00bbffb8`](#insn-00bbffb8) 範囲 `[['00bbffb8', '00bbffbb']]`
  - `UNCONDITIONAL_JUMP` [`00bbffb8`](#insn-00bbffb8) → [`00bc000c`](#insn-00bc000c)
- ブロック [`00bbffbc`](#insn-00bbffbc) 範囲 `[['00bbffbc', '00bbffc7']]`
  - `CONDITIONAL_JUMP` [`00bbffc4`](#insn-00bbffc4) → [`00bc0084`](#insn-00bc0084)
  - `FALL_THROUGH` [`00bbffc4`](#insn-00bbffc4) → [`00bbffc8`](#insn-00bbffc8)
- ブロック [`00bbffc8`](#insn-00bbffc8) 範囲 `[['00bbffc8', '00bbffd7']]`
  - `FALL_THROUGH` [`00bbffd4`](#insn-00bbffd4) → [`00bbffd8`](#insn-00bbffd8)
- ブロック [`00bbffd8`](#insn-00bbffd8) 範囲 `[['00bbffd8', '00bbffef']]`
  - `CONDITIONAL_JUMP` [`00bbffec`](#insn-00bbffec) → [`00bc000c`](#insn-00bc000c)
  - `FALL_THROUGH` [`00bbffec`](#insn-00bbffec) → [`00bbfff0`](#insn-00bbfff0)
- ブロック [`00bbfff0`](#insn-00bbfff0) 範囲 `[['00bbfff0', '00bc000b']]`
  - `FALL_THROUGH` [`00bc0008`](#insn-00bc0008) → [`00bc000c`](#insn-00bc000c)
- ブロック [`00bc000c`](#insn-00bc000c) 範囲 `[['00bc000c', '00bc0013']]`
  - `CONDITIONAL_JUMP` [`00bc0010`](#insn-00bc0010) → [`00bc0064`](#insn-00bc0064)
  - `FALL_THROUGH` [`00bc0010`](#insn-00bc0010) → [`00bc0014`](#insn-00bc0014)
- ブロック [`00bc0014`](#insn-00bc0014) 範囲 `[['00bc0014', '00bc0017']]`
  - `FALL_THROUGH` [`00bc0014`](#insn-00bc0014) → [`00bc0018`](#insn-00bc0018)
- ブロック [`00bc0018`](#insn-00bc0018) 範囲 `[['00bc0018', '00bc0043']]`
- ブロック [`00bc0044`](#insn-00bc0044) 範囲 `[['00bc0044', '00bc0063']]`
- ブロック [`00bc0064`](#insn-00bc0064) 範囲 `[['00bc0064', '00bc0083']]`
- ブロック [`00bc0084`](#insn-00bc0084) 範囲 `[['00bc0084', '00bc0087']]`

## 命令位置別の参照

- [`00bbff30`](#insn-00bbff30) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbff34`](#insn-00bbff34) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbff38`](#insn-00bbff38) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbff3c`](#insn-00bbff3c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbff40`](#insn-00bbff40) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbff44`](#insn-00bbff44) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbff5c`](#insn-00bbff5c) → [`00bc0044`](#insn-00bc0044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbff88`](#insn-00bbff88) → [`00bbffd8`](#insn-00bbffd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbff90`](#insn-00bbff90) → [`00bbffbc`](#insn-00bbffbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbff98`](#insn-00bbff98) → [`00bdd180`](../00bdd/00bdd180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd180` · 推定シンボル `None` · 推定型 `None`
- [`00bbff9c`](#insn-00bbff9c) → [`00bc0084`](#insn-00bc0084) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbffb4`](#insn-00bbffb4) → [`00bbfff0`](#insn-00bbfff0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbffb8`](#insn-00bbffb8) → [`00bc000c`](#insn-00bc000c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbffc0`](#insn-00bbffc0) → [`00bdd180`](../00bdd/00bdd180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd180` · 推定シンボル `None` · 推定型 `None`
- [`00bbffc4`](#insn-00bbffc4) → [`00bc0084`](#insn-00bc0084) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbffec`](#insn-00bbffec) → [`00bc000c`](#insn-00bc000c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfffc`](#insn-00bbfffc) → [`00bdb0a0`](../00bdb/00bdb0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bc0010`](#insn-00bc0010) → [`00bc0064`](#insn-00bc0064) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0024`](#insn-00bc0024) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0028`](#insn-00bc0028) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc002c`](#insn-00bc002c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0030`](#insn-00bc0030) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0034`](#insn-00bc0034) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0038`](#insn-00bc0038) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc0048`](#insn-00bc0048) → `002917fc`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bc0050`](#insn-00bc0050) → `002a210a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bc0058`](#insn-00bc0058) → `00296866`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc0060`](#insn-00bc0060) → [`00bbb158`](../00bbb/00bbb158.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbb158` · 推定シンボル `None` · 推定型 `None`
- [`00bc0068`](#insn-00bc0068) → `002917fc`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bc0070`](#insn-00bc0070) → `002a210a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bc0078`](#insn-00bc0078) → `002a2144`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bc0080`](#insn-00bc0080) → [`00bbb158`](../00bbb/00bbb158.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbb158` · 推定シンボル `None` · 推定型 `None`
- [`00bc0084`](#insn-00bc0084) → [`00bdb180`](../00bdb/00bdb180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb180` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbff30`](#insn-00bbff30)

~~~json
{
  "source": "00bbff30",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbff34`](#insn-00bbff34)

~~~json
{
  "source": "00bbff34",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbff38`](#insn-00bbff38)

~~~json
{
  "source": "00bbff38",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbff3c`](#insn-00bbff3c)

~~~json
{
  "source": "00bbff3c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbff40`](#insn-00bbff40)

~~~json
{
  "source": "00bbff40",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbff44`](#insn-00bbff44)

~~~json
{
  "source": "00bbff44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbff5c`](#insn-00bbff5c)

~~~json
{
  "source": "00bbff5c",
  "target": "00bc0044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbff88`](#insn-00bbff88)

~~~json
{
  "source": "00bbff88",
  "target": "00bbffd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbff90`](#insn-00bbff90)

~~~json
{
  "source": "00bbff90",
  "target": "00bbffbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbff98`](#insn-00bbff98)

~~~json
{
  "source": "00bbff98",
  "target": "00bdd180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbff9c`](#insn-00bbff9c)

~~~json
{
  "source": "00bbff9c",
  "target": "00bc0084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbffb4`](#insn-00bbffb4)

~~~json
{
  "source": "00bbffb4",
  "target": "00bbfff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbffb8`](#insn-00bbffb8)

~~~json
{
  "source": "00bbffb8",
  "target": "00bc000c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbffc0`](#insn-00bbffc0)

~~~json
{
  "source": "00bbffc0",
  "target": "00bdd180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbffc4`](#insn-00bbffc4)

~~~json
{
  "source": "00bbffc4",
  "target": "00bc0084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbffec`](#insn-00bbffec)

~~~json
{
  "source": "00bbffec",
  "target": "00bc000c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfffc`](#insn-00bbfffc)

~~~json
{
  "source": "00bbfffc",
  "target": "00bdb0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc0010`](#insn-00bc0010)

~~~json
{
  "source": "00bc0010",
  "target": "00bc0064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0024`](#insn-00bc0024)

~~~json
{
  "source": "00bc0024",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0028`](#insn-00bc0028)

~~~json
{
  "source": "00bc0028",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc002c`](#insn-00bc002c)

~~~json
{
  "source": "00bc002c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0030`](#insn-00bc0030)

~~~json
{
  "source": "00bc0030",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0034`](#insn-00bc0034)

~~~json
{
  "source": "00bc0034",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0038`](#insn-00bc0038)

~~~json
{
  "source": "00bc0038",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc0048`](#insn-00bc0048)

~~~json
{
  "source": "00bc0048",
  "target": "002917fc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002917fc",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "25733a25643a20257300",
  "capture_start": "002917fc",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bc0050`](#insn-00bc0050)

~~~json
{
  "source": "00bc0050",
  "target": "002a210a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a210a",
  "offset": 0,
  "size": 58,
  "datatype": "string",
  "bytes": "6f75742f6c6c766d2d70726f6a6563742f6c69626378786162692f7372632f64",
  "capture_start": "002a210a",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bc0058`](#insn-00bc0058)

~~~json
{
  "source": "00bc0058",
  "target": "00296866",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00296866",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "00296866",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bc0060`](#insn-00bc0060)

~~~json
{
  "source": "00bc0060",
  "target": "00bbb158",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc0068`](#insn-00bc0068)

~~~json
{
  "source": "00bc0068",
  "target": "002917fc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002917fc",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "25733a25643a20257300",
  "capture_start": "002917fc",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bc0070`](#insn-00bc0070)

~~~json
{
  "source": "00bc0070",
  "target": "002a210a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a210a",
  "offset": 0,
  "size": 58,
  "datatype": "string",
  "bytes": "6f75742f6c6c766d2d70726f6a6563742f6c69626378786162692f7372632f64",
  "capture_start": "002a210a",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bc0078`](#insn-00bc0078)

~~~json
{
  "source": "00bc0078",
  "target": "002a2144",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2144",
  "offset": 0,
  "size": 29,
  "datatype": "string",
  "bytes": "736872696e6b546f53697a6528292063616e277420657870616e642100",
  "capture_start": "002a2144",
  "capture_bytes": 29,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bc0080`](#insn-00bc0080)

~~~json
{
  "source": "00bc0080",
  "target": "00bbb158",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc0084`](#insn-00bc0084)

~~~json
{
  "source": "00bc0084",
  "target": "00bdb180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
