# 00adb2ac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00adb268`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb268.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0007.md#compare-7eeaf3d90e40f81f8f573aeb7337b48c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b3ac84`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3ac84.md) · 移動量 `+0x5f9d8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0055.md#compare-23c25decdd946dc67869ed5186261f51)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adb2ac",
  "name": "FUN_00adb2ac",
  "size": 284,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e0de78bf7572dd15e99c73c3cf089118e63ac27d35fcf8a5590a345dca99aac4",
  "source_text_sha256": "e0de78bf7572dd15e99c73c3cf089118e63ac27d35fcf8a5590a345dca99aac4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adb2ac",
        "00adb3c3"
      ],
      [
        "00adb3ec",
        "00adb3ef"
      ]
    ],
    "bytes_sha256": "e4855b216d496b9161bc5a837c9d6aa260d581572853f619add0120d6e37d148",
    "instruction_count": 71,
    "instruction_bytes": 284,
    "body_bytes": 284,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ad9b64](../00ad9/00ad9b64.md)

## 呼び出し先

- [00418fe0](../00418/00418fe0.md)
- [00419064](../00419/00419064.md)
- [00adb3f0](../00adb/00adb3f0.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb090](../00bdb/00bdb090.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2207 bytes

~~~c

undefined8 * FUN_00adb2ac(long *param_1,undefined8 param_2,undefined8 param_3,undefined8 *param_4)

{
  long lVar1;
  undefined8 *puVar2;
  undefined8 uVar3;
  undefined8 *puVar4;
  byte *pbVar5;
  undefined8 *puVar6;
  undefined8 uVar7;
  undefined8 local_68;
  undefined8 *local_60;
  long *local_58;
  undefined1 local_50;
  long local_48;
  
                    /* try { // try from 00adb2b0 to 00bdb2c7 has its CatchHandler @ 00adb8d8 */
  lVar1 = tpidr_el0;
                    /* try { // try from 00adb2c8 to 00bdb3a7 has its CatchHandler @ 00adb014 */
  local_48 = *(long *)(lVar1 + 0x28);
  puVar2 = (undefined8 *)FUN_00adb3f0(param_1,&local_68,param_2);
  puVar6 = (undefined8 *)*puVar2;
  if (puVar6 == (undefined8 *)0x0) {
    puVar6 = (undefined8 *)_Znwm(0xd0);
    pbVar5 = (byte *)*param_4;
    local_50 = 0;
    local_60 = puVar6;
    local_58 = param_1 + 1;
    if ((*pbVar5 & 1) == 0) {
      uVar7 = *(undefined8 *)(pbVar5 + 8);
      uVar3 = *(undefined8 *)pbVar5;
      puVar6[6] = *(undefined8 *)(pbVar5 + 0x10);
      puVar6[5] = uVar7;
      puVar6[4] = uVar3;
    }
    else {
      FUN_00418fe0(puVar6 + 4,*(undefined8 *)(pbVar5 + 0x10),*(undefined8 *)(pbVar5 + 8));
    }
    *puVar6 = 0;
    puVar6[1] = 0;
    puVar6[2] = local_68;
    puVar6[0xb] = 0;
    puVar6[10] = 0;
    puVar6[0xd] = 0;
    puVar6[0xc] = 0;
    puVar6[0xf] = 0;
    puVar6[0xe] = 0;
    puVar6[0x11] = 0;
    puVar6[0x10] = 0;
    puVar6[0x13] = 0;
    puVar6[0x12] = 0;
    puVar6[0x15] = 0;
    puVar6[0x14] = 0;
    puVar6[0x17] = 0;
    puVar6[0x16] = 0;
    puVar6[0x19] = 0;
    puVar6[0x18] = 0;
    puVar6[9] = 0;
    puVar6[8] = 0;
    *puVar2 = puVar6;
    puVar4 = puVar6;
    if (*(long *)*param_1 != 0) {
      *param_1 = *(long *)*param_1;
      puVar4 = (undefined8 *)*puVar2;
    }
    puVar2 = (undefined8 *)FUN_00419064(param_1[1],puVar4);
    uVar3 = 1;
    param_1[2] = param_1[2] + 1;
  }
  else {
    uVar3 = 0;
  }
  if (*(long *)(lVar1 + 0x28) == local_48) {
                    /* try { // try from 00adb3a8 to 00bdb4f7 has its CatchHandler @ 00adb9f0 */
    return puVar6;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(puVar2,uVar3);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00adb2ac"></a> `00adb2ac` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00adb2b0"></a> `00adb2b0` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adb2b4"></a> `00adb2b4` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adb2b8"></a> `00adb2b8` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adb2bc"></a> `00adb2bc` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00adb2c0"></a> `00adb2c0` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00adb2c4"></a> `00adb2c4` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00adb2c8"></a> `00adb2c8` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00adb2cc"></a> `00adb2cc` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00adb2d0"></a> `00adb2d0` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00adb2d4"></a> `00adb2d4` | `f5 03 03 aa` | mov x21,x3 | `FALL_THROUGH`
<a id="insn-00adb2d8"></a> `00adb2d8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00adb2dc"></a> `00adb2dc` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adb2e0"></a> `00adb2e0` | `44 00 00 94` | bl 0x00adb3f0 | `UNCONDITIONAL_CALL`
<a id="insn-00adb2e4"></a> `00adb2e4` | `14 00 40 f9` | ldr x20,[x0] | `FALL_THROUGH`
<a id="insn-00adb2e8"></a> `00adb2e8` | `74 00 00 b4` | cbz x20,0x00adb2f4 | `CONDITIONAL_JUMP`
<a id="insn-00adb2ec"></a> `00adb2ec` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00adb2f0"></a> `00adb2f0` | `2a 00 00 14` | b 0x00adb398 | `UNCONDITIONAL_JUMP`
<a id="insn-00adb2f4"></a> `00adb2f4` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00adb2f8"></a> `00adb2f8` | `00 1a 80 52` | mov w0,#0xd0 | `FALL_THROUGH`
<a id="insn-00adb2fc"></a> `00adb2fc` | `78 22 00 91` | add x24,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00adb300"></a> `00adb300` | `50 ff 03 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00adb304"></a> `00adb304` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00adb308"></a> `00adb308` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00adb30c"></a> `00adb30c` | `e0 0b 00 f9` | str x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adb310"></a> `00adb310` | `f8 0f 00 f9` | str x24,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00adb314"></a> `00adb314` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00adb318"></a> `00adb318` | `ff 83 00 39` | strb wzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adb31c"></a> `00adb31c` | `c9 00 00 37` | tbnz w9,#0x0,0x00adb334 | `CONDITIONAL_JUMP`
<a id="insn-00adb320"></a> `00adb320` | `09 09 40 f9` | ldr x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00adb324"></a> `00adb324` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00adb328"></a> `00adb328` | `89 02 03 f8` | stur x9,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00adb32c"></a> `00adb32c` | `80 02 82 3c` | stur q0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00adb330"></a> `00adb330` | `04 00 00 14` | b 0x00adb340 | `UNCONDITIONAL_JUMP`
<a id="insn-00adb334"></a> `00adb334` | `02 85 40 a9` | ldp x2,x1,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00adb338"></a> `00adb338` | `80 82 00 91` | add x0,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00adb33c"></a> `00adb33c` | `29 f7 e4 97` | bl 0x00418fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00adb340"></a> `00adb340` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00adb344"></a> `00adb344` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00adb348"></a> `00adb348` | `9f 7e 00 a9` | stp xzr,xzr,[x20] | `FALL_THROUGH`
<a id="insn-00adb34c"></a> `00adb34c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00adb350"></a> `00adb350` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00adb354"></a> `00adb354` | `80 82 02 ad` | stp q0,q0,[x20, #0x50] | `FALL_THROUGH`
<a id="insn-00adb358"></a> `00adb358` | `80 82 03 ad` | stp q0,q0,[x20, #0x70] | `FALL_THROUGH`
<a id="insn-00adb35c"></a> `00adb35c` | `80 82 04 ad` | stp q0,q0,[x20, #0x90] | `FALL_THROUGH`
<a id="insn-00adb360"></a> `00adb360` | `80 82 05 ad` | stp q0,q0,[x20, #0xb0] | `FALL_THROUGH`
<a id="insn-00adb364"></a> `00adb364` | `80 12 80 3d` | str q0,[x20, #0x40] | `FALL_THROUGH`
<a id="insn-00adb368"></a> `00adb368` | `f4 02 00 f9` | str x20,[x23] | `FALL_THROUGH`
<a id="insn-00adb36c"></a> `00adb36c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00adb370"></a> `00adb370` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00adb374"></a> `00adb374` | `68 00 00 b4` | cbz x8,0x00adb380 | `CONDITIONAL_JUMP`
<a id="insn-00adb378"></a> `00adb378` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00adb37c"></a> `00adb37c` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-00adb380"></a> `00adb380` | `60 06 40 f9` | ldr x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00adb384"></a> `00adb384` | `38 f7 e4 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00adb388"></a> `00adb388` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00adb38c"></a> `00adb38c` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00adb390"></a> `00adb390` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00adb394"></a> `00adb394` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00adb398"></a> `00adb398` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00adb39c"></a> `00adb39c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00adb3a0"></a> `00adb3a0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00adb3a4"></a> `00adb3a4` | `41 02 00 54` | b.ne 0x00adb3ec | `CONDITIONAL_JUMP`
<a id="insn-00adb3a8"></a> `00adb3a8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00adb3ac"></a> `00adb3ac` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00adb3b0"></a> `00adb3b0` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00adb3b4"></a> `00adb3b4` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adb3b8"></a> `00adb3b8` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adb3bc"></a> `00adb3bc` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00adb3c0"></a> `00adb3c0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00adb3ec"></a> `00adb3ec` | `29 ff 03 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adb2ac`](#insn-00adb2ac) 範囲 `[['00adb2ac', '00adb2af']]`
  - `FALL_THROUGH` [`00adb2ac`](#insn-00adb2ac) → [`00adb2b0`](#insn-00adb2b0)
- ブロック [`00adb2b0`](#insn-00adb2b0) 範囲 `[['00adb2b0', '00adb2c7']]`
  - `FALL_THROUGH` [`00adb2c4`](#insn-00adb2c4) → [`00adb2c8`](#insn-00adb2c8)
- ブロック [`00adb2c8`](#insn-00adb2c8) 範囲 `[['00adb2c8', '00adb2eb']]`
  - `CONDITIONAL_JUMP` [`00adb2e8`](#insn-00adb2e8) → [`00adb2f4`](#insn-00adb2f4)
  - `FALL_THROUGH` [`00adb2e8`](#insn-00adb2e8) → [`00adb2ec`](#insn-00adb2ec)
- ブロック [`00adb2ec`](#insn-00adb2ec) 範囲 `[['00adb2ec', '00adb2f3']]`
  - `UNCONDITIONAL_JUMP` [`00adb2f0`](#insn-00adb2f0) → [`00adb398`](#insn-00adb398)
- ブロック [`00adb2f4`](#insn-00adb2f4) 範囲 `[['00adb2f4', '00adb31f']]`
  - `CONDITIONAL_JUMP` [`00adb31c`](#insn-00adb31c) → [`00adb334`](#insn-00adb334)
  - `FALL_THROUGH` [`00adb31c`](#insn-00adb31c) → [`00adb320`](#insn-00adb320)
- ブロック [`00adb320`](#insn-00adb320) 範囲 `[['00adb320', '00adb333']]`
  - `UNCONDITIONAL_JUMP` [`00adb330`](#insn-00adb330) → [`00adb340`](#insn-00adb340)
- ブロック [`00adb334`](#insn-00adb334) 範囲 `[['00adb334', '00adb33f']]`
  - `FALL_THROUGH` [`00adb33c`](#insn-00adb33c) → [`00adb340`](#insn-00adb340)
- ブロック [`00adb340`](#insn-00adb340) 範囲 `[['00adb340', '00adb377']]`
  - `CONDITIONAL_JUMP` [`00adb374`](#insn-00adb374) → [`00adb380`](#insn-00adb380)
  - `FALL_THROUGH` [`00adb374`](#insn-00adb374) → [`00adb378`](#insn-00adb378)
- ブロック [`00adb378`](#insn-00adb378) 範囲 `[['00adb378', '00adb37f']]`
  - `FALL_THROUGH` [`00adb37c`](#insn-00adb37c) → [`00adb380`](#insn-00adb380)
- ブロック [`00adb380`](#insn-00adb380) 範囲 `[['00adb380', '00adb397']]`
  - `FALL_THROUGH` [`00adb394`](#insn-00adb394) → [`00adb398`](#insn-00adb398)
- ブロック [`00adb398`](#insn-00adb398) 範囲 `[['00adb398', '00adb3a7']]`
  - `CONDITIONAL_JUMP` [`00adb3a4`](#insn-00adb3a4) → [`00adb3ec`](#insn-00adb3ec)
  - `FALL_THROUGH` [`00adb3a4`](#insn-00adb3a4) → [`00adb3a8`](#insn-00adb3a8)
- ブロック [`00adb3a8`](#insn-00adb3a8) 範囲 `[['00adb3a8', '00adb3c3']]`
- ブロック [`00adb3ec`](#insn-00adb3ec) 範囲 `[['00adb3ec', '00adb3ef']]`

## 命令位置別の参照

- [`00adb2b0`](#insn-00adb2b0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb2b4`](#insn-00adb2b4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb2b8`](#insn-00adb2b8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb2bc`](#insn-00adb2bc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb2dc`](#insn-00adb2dc) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb2e0`](#insn-00adb2e0) → [`00adb3f0`](00adb3f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adb3f0` · 推定シンボル `None` · 推定型 `None`
- [`00adb2e8`](#insn-00adb2e8) → [`00adb2f4`](#insn-00adb2f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb2f0`](#insn-00adb2f0) → [`00adb398`](#insn-00adb398) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb300`](#insn-00adb300) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00adb30c`](#insn-00adb30c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb310`](#insn-00adb310) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb318`](#insn-00adb318) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb31c`](#insn-00adb31c) → [`00adb334`](#insn-00adb334) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb330`](#insn-00adb330) → [`00adb340`](#insn-00adb340) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb33c`](#insn-00adb33c) → [`00418fe0`](../00418/00418fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418fe0` · 推定シンボル `None` · 推定型 `None`
- [`00adb344`](#insn-00adb344) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb374`](#insn-00adb374) → [`00adb380`](#insn-00adb380) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb384`](#insn-00adb384) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00adb39c`](#insn-00adb39c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb3a4`](#insn-00adb3a4) → [`00adb3ec`](#insn-00adb3ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb3ac`](#insn-00adb3ac) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb3b0`](#insn-00adb3b0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb3b4`](#insn-00adb3b4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb3b8`](#insn-00adb3b8) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb3ec`](#insn-00adb3ec) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adb2b0`](#insn-00adb2b0)

~~~json
{
  "source": "00adb2b0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb2b4`](#insn-00adb2b4)

~~~json
{
  "source": "00adb2b4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb2b8`](#insn-00adb2b8)

~~~json
{
  "source": "00adb2b8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb2bc`](#insn-00adb2bc)

~~~json
{
  "source": "00adb2bc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb2dc`](#insn-00adb2dc)

~~~json
{
  "source": "00adb2dc",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb2e0`](#insn-00adb2e0)

~~~json
{
  "source": "00adb2e0",
  "target": "00adb3f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adb2e8`](#insn-00adb2e8)

~~~json
{
  "source": "00adb2e8",
  "target": "00adb2f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb2f0`](#insn-00adb2f0)

~~~json
{
  "source": "00adb2f0",
  "target": "00adb398",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb300`](#insn-00adb300)

~~~json
{
  "source": "00adb300",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adb30c`](#insn-00adb30c)

~~~json
{
  "source": "00adb30c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb310`](#insn-00adb310)

~~~json
{
  "source": "00adb310",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb318`](#insn-00adb318)

~~~json
{
  "source": "00adb318",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb31c`](#insn-00adb31c)

~~~json
{
  "source": "00adb31c",
  "target": "00adb334",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb330`](#insn-00adb330)

~~~json
{
  "source": "00adb330",
  "target": "00adb340",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb33c`](#insn-00adb33c)

~~~json
{
  "source": "00adb33c",
  "target": "00418fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adb344`](#insn-00adb344)

~~~json
{
  "source": "00adb344",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb374`](#insn-00adb374)

~~~json
{
  "source": "00adb374",
  "target": "00adb380",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb384`](#insn-00adb384)

~~~json
{
  "source": "00adb384",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adb39c`](#insn-00adb39c)

~~~json
{
  "source": "00adb39c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb3a4`](#insn-00adb3a4)

~~~json
{
  "source": "00adb3a4",
  "target": "00adb3ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb3ac`](#insn-00adb3ac)

~~~json
{
  "source": "00adb3ac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb3b0`](#insn-00adb3b0)

~~~json
{
  "source": "00adb3b0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb3b4`](#insn-00adb3b4)

~~~json
{
  "source": "00adb3b4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb3b8`](#insn-00adb3b8)

~~~json
{
  "source": "00adb3b8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb3ec`](#insn-00adb3ec)

~~~json
{
  "source": "00adb3ec",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
