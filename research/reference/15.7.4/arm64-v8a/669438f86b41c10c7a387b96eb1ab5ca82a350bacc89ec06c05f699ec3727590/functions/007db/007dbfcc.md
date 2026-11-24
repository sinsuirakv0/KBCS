# 007dbfcc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `007dbfcc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007db/007dbfcc.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/machine_only_observed-0028.md#compare-8e1aad5753f459bcca12d791376aab99)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00810848`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810848.md) · 移動量 `+0x3487c`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0036.md#compare-3bf4b09522b185c28c51f9f43496c3e8)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007dbfcc",
  "name": "FUN_007dbfcc",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "91b7774a1b1b884a42551e58eafbe65bdf49e46052cce7df4ba56f0beb6eefb4",
  "source_text_sha256": "91b7774a1b1b884a42551e58eafbe65bdf49e46052cce7df4ba56f0beb6eefb4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007dbfcc",
        "007dc0fb"
      ]
    ],
    "bytes_sha256": "a29466ea076a91d59289863b7deb6582d7f2ab0d866ba89f21eef8182de75fc1",
    "instruction_count": 76,
    "instruction_bytes": 304,
    "body_bytes": 304,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [007db2f0](../007db/007db2f0.md)

## 呼び出し先

- [007bfcc8](../007bf/007bfcc8.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb0f0](../00bdb/00bdb0f0.md)
- [00bdb1b0](../00bdb/00bdb1b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4217 bytes

~~~c

void FUN_007dbfcc(undefined8 *param_1,void *param_2,long param_3,ulong param_4)

{
  void *__src;
  ulong uVar1;
  undefined8 *puVar2;
  undefined8 *puVar3;
  void *pvVar4;
  long lVar5;
  size_t sVar6;
  ulong uVar7;
  undefined8 *puVar8;
  undefined8 *puVar9;
  void *pvVar10;
  undefined1 auVar11 [16];
  
  uVar7 = param_1[2];
  pvVar10 = (void *)*param_1;
  if (param_4 <= (ulong)((long)(uVar7 - (long)pvVar10) >> 4)) {
    sVar6 = (long)param_1[1] - (long)pvVar10;
    pvVar4 = param_2;
    if (((ulong)((long)sVar6 >> 4) < param_4) &&
       (pvVar4 = (void *)((long)param_2 + sVar6), (void *)param_1[1] != pvVar10)) {
                    /* try { // try from 007dc0a8 to 008dc0af has its CatchHandler @ 007dd318 */
      memmove(pvVar10,param_2,sVar6);
      pvVar10 = (void *)param_1[1];
    }
    sVar6 = param_3 - (long)pvVar4;
    if (sVar6 != 0) {
      memmove(pvVar10,pvVar4,sVar6);
    }
LAB_007dc0d8:
                    /* try { // try from 007dc0dc to 008dc0e3 has its CatchHandler @ 007dd5a0 */
    param_1[1] = (long)pvVar10 + sVar6;
    return;
  }
  lVar5 = param_3;
  if (pvVar10 != (void *)0x0) {
    param_1[1] = pvVar10;
    _ZdlPv(pvVar10);
    uVar7 = 0;
    *param_1 = 0;
    param_1[1] = 0;
    param_1[2] = 0;
  }
  if (param_4 >> 0x3c == 0) {
    uVar1 = (long)uVar7 >> 3;
    if ((ulong)((long)uVar7 >> 3) <= param_4) {
      uVar1 = param_4;
    }
                    /* try { // try from 007dc03c to 008dc047 has its CatchHandler @ 007dd388 */
    if (0x7fffffffffffffef < uVar7) {
      uVar1 = 0xfffffffffffffff;
    }
    if (uVar1 >> 0x3c == 0) {
      pvVar10 = (void *)_Znwm(uVar1 * 0x10);
      sVar6 = param_3 - (long)param_2;
                    /* try { // try from 007dc068 to 008dc083 has its CatchHandler @ 007dd350 */
      *param_1 = pvVar10;
      param_1[1] = pvVar10;
      param_1[2] = (void *)((long)pvVar10 + uVar1 * 0x10);
      if (sVar6 != 0) {
        memcpy(pvVar10,param_2,sVar6);
      }
      goto LAB_007dc0d8;
    }
  }
                    /* try { // try from 007dc0f8 to 008dc0ff has its CatchHandler @ 007dd59c */
  auVar11 = FUN_007bfcc8(param_1);
  pvVar4 = auVar11._8_8_;
  puVar2 = auVar11._0_8_;
  uVar7 = puVar2[2];
  pvVar10 = (void *)*puVar2;
  if ((ulong)((long)(uVar7 - (long)pvVar10) >> 3) < param_4) {
    if (pvVar10 != (void *)0x0) {
      puVar2[1] = pvVar10;
      _ZdlPv(pvVar10);
      uVar7 = 0;
      *puVar2 = 0;
      puVar2[1] = 0;
      puVar2[2] = 0;
    }
    if (param_4 >> 0x3d == 0) {
      uVar1 = (long)uVar7 >> 2;
      if ((ulong)((long)uVar7 >> 2) <= param_4) {
        uVar1 = param_4;
      }
      if (0x7ffffffffffffff7 < uVar7) {
        uVar1 = 0x1fffffffffffffff;
      }
      if (uVar1 >> 0x3d == 0) {
        pvVar10 = (void *)_Znwm(uVar1 * 8);
        sVar6 = lVar5 - (long)pvVar4;
        *puVar2 = pvVar10;
        puVar2[1] = pvVar10;
        puVar2[2] = (void *)((long)pvVar10 + uVar1 * 8);
        if (sVar6 != 0) {
          memcpy(pvVar10,pvVar4,sVar6);
        }
        goto LAB_007dc208;
      }
    }
    auVar11 = FUN_007bfcdc(puVar2);
    puVar2 = auVar11._8_8_;
    if (puVar2 == (undefined8 *)0x0) {
      return;
    }
    FUN_007dc22c(auVar11._0_8_,*puVar2);
    FUN_007dc22c(auVar11._0_8_,puVar2[1]);
    puVar9 = (undefined8 *)puVar2[5];
    if (puVar9 != (undefined8 *)0x0) {
      puVar8 = (undefined8 *)puVar2[6];
      puVar3 = puVar9;
      if (puVar8 != puVar9) {
        do {
          puVar3 = puVar8 + -5;
          pvVar10 = (void *)*puVar3;
          if (pvVar10 != (void *)0x0) {
            puVar8[-4] = pvVar10;
            _ZdlPv(pvVar10);
          }
          puVar8 = puVar3;
        } while (puVar3 != puVar9);
        puVar3 = (undefined8 *)puVar2[5];
      }
      puVar2[6] = puVar9;
      _ZdlPv(puVar3);
    }
    _ZdlPv(puVar2);
    return;
  }
  sVar6 = (long)puVar2[1] - (long)pvVar10;
  __src = pvVar4;
  if (((ulong)((long)sVar6 >> 3) < param_4) &&
     (__src = (void *)((long)pvVar4 + sVar6), (void *)puVar2[1] != pvVar10)) {
    memmove(pvVar10,pvVar4,sVar6);
    pvVar10 = (void *)puVar2[1];
  }
  sVar6 = lVar5 - (long)__src;
  if (sVar6 != 0) {
    memmove(pvVar10,__src,sVar6);
  }
LAB_007dc208:
  puVar2[1] = (long)pvVar10 + sVar6;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007dbfcc"></a> `007dbfcc` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-007dbfd0"></a> `007dbfd0` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007dbfd4"></a> `007dbfd4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007dbfd8"></a> `007dbfd8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007dbfdc"></a> `007dbfdc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007dbfe0"></a> `007dbfe0` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-007dbfe4"></a> `007dbfe4` | `15 00 40 f9` | ldr x21,[x0] | `FALL_THROUGH`
<a id="insn-007dbfe8"></a> `007dbfe8` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-007dbfec"></a> `007dbfec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-007dbff0"></a> `007dbff0` | `09 01 15 cb` | sub x9,x8,x21 | `FALL_THROUGH`
<a id="insn-007dbff4"></a> `007dbff4` | `7f 10 89 eb` | cmp x3,x9, ASR #0x4 | `FALL_THROUGH`
<a id="insn-007dbff8"></a> `007dbff8` | `89 04 00 54` | b.ls 0x007dc088 | `CONDITIONAL_JUMP`
<a id="insn-007dbffc"></a> `007dbffc` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-007dc000"></a> `007dc000` | `35 01 00 b4` | cbz x21,0x007dc024 | `CONDITIONAL_JUMP`
<a id="insn-007dc004"></a> `007dc004` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-007dc008"></a> `007dc008` | `75 06 00 f9` | str x21,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-007dc00c"></a> `007dc00c` | `f5 03 03 aa` | mov x21,x3 | `FALL_THROUGH`
<a id="insn-007dc010"></a> `007dc010` | `14 fc 0f 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-007dc014"></a> `007dc014` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-007dc018"></a> `007dc018` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-007dc01c"></a> `007dc01c` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-007dc020"></a> `007dc020` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-007dc024"></a> `007dc024` | `69 fc 7c d3` | lsr x9,x3,#0x3c | `FALL_THROUGH`
<a id="insn-007dc028"></a> `007dc028` | `69 06 00 b5` | cbnz x9,0x007dc0f4 | `CONDITIONAL_JUMP`
<a id="insn-007dc02c"></a> `007dc02c` | `09 fd 43 93` | asr x9,x8,#0x3 | `FALL_THROUGH`
<a id="insn-007dc030"></a> `007dc030` | `ea eb 7c b2` | orr x10,xzr,#0x7ffffffffffffff0 | `FALL_THROUGH`
<a id="insn-007dc034"></a> `007dc034` | `3f 01 03 eb` | cmp x9,x3 | `FALL_THROUGH`
<a id="insn-007dc038"></a> `007dc038` | `29 81 83 9a` | csel x9,x9,x3,hi | `FALL_THROUGH`
<a id="insn-007dc03c"></a> `007dc03c` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-007dc040"></a> `007dc040` | `08 00 fe 92` | mov x8,#0xfffffffffffffff | `FALL_THROUGH`
<a id="insn-007dc044"></a> `007dc044` | `28 31 88 9a` | csel x8,x9,x8,cc | `FALL_THROUGH`
<a id="insn-007dc048"></a> `007dc048` | `09 fd 7c d3` | lsr x9,x8,#0x3c | `FALL_THROUGH`
<a id="insn-007dc04c"></a> `007dc04c` | `49 05 00 b5` | cbnz x9,0x007dc0f4 | `CONDITIONAL_JUMP`
<a id="insn-007dc050"></a> `007dc050` | `16 ed 7c d3` | lsl x22,x8,#0x4 | `FALL_THROUGH`
<a id="insn-007dc054"></a> `007dc054` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-007dc058"></a> `007dc058` | `fa fb 0f 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-007dc05c"></a> `007dc05c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-007dc060"></a> `007dc060` | `94 02 17 eb` | subs x20,x20,x23 | `FALL_THROUGH`
<a id="insn-007dc064"></a> `007dc064` | `08 00 16 8b` | add x8,x0,x22 | `FALL_THROUGH`
<a id="insn-007dc068"></a> `007dc068` | `60 02 00 a9` | stp x0,x0,[x19] | `FALL_THROUGH`
<a id="insn-007dc06c"></a> `007dc06c` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-007dc070"></a> `007dc070` | `40 03 00 54` | b.eq 0x007dc0d8 | `CONDITIONAL_JUMP`
<a id="insn-007dc074"></a> `007dc074` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-007dc078"></a> `007dc078` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-007dc07c"></a> `007dc07c` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-007dc080"></a> `007dc080` | `4c fc 0f 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-007dc084"></a> `007dc084` | `15 00 00 14` | b 0x007dc0d8 | `UNCONDITIONAL_JUMP`
<a id="insn-007dc088"></a> `007dc088` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-007dc08c"></a> `007dc08c` | `02 01 15 cb` | sub x2,x8,x21 | `FALL_THROUGH`
<a id="insn-007dc090"></a> `007dc090` | `7f 10 82 eb` | cmp x3,x2, ASR #0x4 | `FALL_THROUGH`
<a id="insn-007dc094"></a> `007dc094` | `89 01 00 54` | b.ls 0x007dc0c4 | `CONDITIONAL_JUMP`
<a id="insn-007dc098"></a> `007dc098` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-007dc09c"></a> `007dc09c` | `36 00 02 8b` | add x22,x1,x2 | `FALL_THROUGH`
<a id="insn-007dc0a0"></a> `007dc0a0` | `80 00 00 54` | b.eq 0x007dc0b0 | `CONDITIONAL_JUMP`
<a id="insn-007dc0a4"></a> `007dc0a4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-007dc0a8"></a> `007dc0a8` | `12 fc 0f 94` | bl 0x00bdb0f0 | `UNCONDITIONAL_CALL`
<a id="insn-007dc0ac"></a> `007dc0ac` | `75 06 40 f9` | ldr x21,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-007dc0b0"></a> `007dc0b0` | `94 02 16 eb` | subs x20,x20,x22 | `FALL_THROUGH`
<a id="insn-007dc0b4"></a> `007dc0b4` | `20 01 00 54` | b.eq 0x007dc0d8 | `CONDITIONAL_JUMP`
<a id="insn-007dc0b8"></a> `007dc0b8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-007dc0bc"></a> `007dc0bc` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-007dc0c0"></a> `007dc0c0` | `04 00 00 14` | b 0x007dc0d0 | `UNCONDITIONAL_JUMP`
<a id="insn-007dc0c4"></a> `007dc0c4` | `94 02 01 eb` | subs x20,x20,x1 | `FALL_THROUGH`
<a id="insn-007dc0c8"></a> `007dc0c8` | `80 00 00 54` | b.eq 0x007dc0d8 | `CONDITIONAL_JUMP`
<a id="insn-007dc0cc"></a> `007dc0cc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-007dc0d0"></a> `007dc0d0` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-007dc0d4"></a> `007dc0d4` | `07 fc 0f 94` | bl 0x00bdb0f0 | `UNCONDITIONAL_CALL`
<a id="insn-007dc0d8"></a> `007dc0d8` | `a8 02 14 8b` | add x8,x21,x20 | `FALL_THROUGH`
<a id="insn-007dc0dc"></a> `007dc0dc` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-007dc0e0"></a> `007dc0e0` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007dc0e4"></a> `007dc0e4` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007dc0e8"></a> `007dc0e8` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007dc0ec"></a> `007dc0ec` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-007dc0f0"></a> `007dc0f0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-007dc0f4"></a> `007dc0f4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007dc0f8"></a> `007dc0f8` | `f4 8e ff 97` | bl 0x007bfcc8 | `UNCONDITIONAL_CALL`

## 基本ブロックと分岐先

- ブロック [`007dbfcc`](#insn-007dbfcc) 範囲 `[['007dbfcc', '007dbffb']]`
  - `CONDITIONAL_JUMP` [`007dbff8`](#insn-007dbff8) → [`007dc088`](#insn-007dc088)
  - `FALL_THROUGH` [`007dbff8`](#insn-007dbff8) → [`007dbffc`](#insn-007dbffc)
- ブロック [`007dbffc`](#insn-007dbffc) 範囲 `[['007dbffc', '007dc003']]`
  - `CONDITIONAL_JUMP` [`007dc000`](#insn-007dc000) → [`007dc024`](#insn-007dc024)
  - `FALL_THROUGH` [`007dc000`](#insn-007dc000) → [`007dc004`](#insn-007dc004)
- ブロック [`007dc004`](#insn-007dc004) 範囲 `[['007dc004', '007dc023']]`
  - `FALL_THROUGH` [`007dc020`](#insn-007dc020) → [`007dc024`](#insn-007dc024)
- ブロック [`007dc024`](#insn-007dc024) 範囲 `[['007dc024', '007dc02b']]`
  - `CONDITIONAL_JUMP` [`007dc028`](#insn-007dc028) → [`007dc0f4`](#insn-007dc0f4)
  - `FALL_THROUGH` [`007dc028`](#insn-007dc028) → [`007dc02c`](#insn-007dc02c)
- ブロック [`007dc02c`](#insn-007dc02c) 範囲 `[['007dc02c', '007dc03b']]`
  - `FALL_THROUGH` [`007dc038`](#insn-007dc038) → [`007dc03c`](#insn-007dc03c)
- ブロック [`007dc03c`](#insn-007dc03c) 範囲 `[['007dc03c', '007dc04f']]`
  - `CONDITIONAL_JUMP` [`007dc04c`](#insn-007dc04c) → [`007dc0f4`](#insn-007dc0f4)
  - `FALL_THROUGH` [`007dc04c`](#insn-007dc04c) → [`007dc050`](#insn-007dc050)
- ブロック [`007dc050`](#insn-007dc050) 範囲 `[['007dc050', '007dc067']]`
  - `FALL_THROUGH` [`007dc064`](#insn-007dc064) → [`007dc068`](#insn-007dc068)
- ブロック [`007dc068`](#insn-007dc068) 範囲 `[['007dc068', '007dc073']]`
  - `CONDITIONAL_JUMP` [`007dc070`](#insn-007dc070) → [`007dc0d8`](#insn-007dc0d8)
  - `FALL_THROUGH` [`007dc070`](#insn-007dc070) → [`007dc074`](#insn-007dc074)
- ブロック [`007dc074`](#insn-007dc074) 範囲 `[['007dc074', '007dc087']]`
  - `UNCONDITIONAL_JUMP` [`007dc084`](#insn-007dc084) → [`007dc0d8`](#insn-007dc0d8)
- ブロック [`007dc088`](#insn-007dc088) 範囲 `[['007dc088', '007dc097']]`
  - `CONDITIONAL_JUMP` [`007dc094`](#insn-007dc094) → [`007dc0c4`](#insn-007dc0c4)
  - `FALL_THROUGH` [`007dc094`](#insn-007dc094) → [`007dc098`](#insn-007dc098)
- ブロック [`007dc098`](#insn-007dc098) 範囲 `[['007dc098', '007dc0a3']]`
  - `CONDITIONAL_JUMP` [`007dc0a0`](#insn-007dc0a0) → [`007dc0b0`](#insn-007dc0b0)
  - `FALL_THROUGH` [`007dc0a0`](#insn-007dc0a0) → [`007dc0a4`](#insn-007dc0a4)
- ブロック [`007dc0a4`](#insn-007dc0a4) 範囲 `[['007dc0a4', '007dc0a7']]`
  - `FALL_THROUGH` [`007dc0a4`](#insn-007dc0a4) → [`007dc0a8`](#insn-007dc0a8)
- ブロック [`007dc0a8`](#insn-007dc0a8) 範囲 `[['007dc0a8', '007dc0af']]`
  - `FALL_THROUGH` [`007dc0ac`](#insn-007dc0ac) → [`007dc0b0`](#insn-007dc0b0)
- ブロック [`007dc0b0`](#insn-007dc0b0) 範囲 `[['007dc0b0', '007dc0b7']]`
  - `CONDITIONAL_JUMP` [`007dc0b4`](#insn-007dc0b4) → [`007dc0d8`](#insn-007dc0d8)
  - `FALL_THROUGH` [`007dc0b4`](#insn-007dc0b4) → [`007dc0b8`](#insn-007dc0b8)
- ブロック [`007dc0b8`](#insn-007dc0b8) 範囲 `[['007dc0b8', '007dc0c3']]`
  - `UNCONDITIONAL_JUMP` [`007dc0c0`](#insn-007dc0c0) → [`007dc0d0`](#insn-007dc0d0)
- ブロック [`007dc0c4`](#insn-007dc0c4) 範囲 `[['007dc0c4', '007dc0cb']]`
  - `CONDITIONAL_JUMP` [`007dc0c8`](#insn-007dc0c8) → [`007dc0d8`](#insn-007dc0d8)
  - `FALL_THROUGH` [`007dc0c8`](#insn-007dc0c8) → [`007dc0cc`](#insn-007dc0cc)
- ブロック [`007dc0cc`](#insn-007dc0cc) 範囲 `[['007dc0cc', '007dc0cf']]`
  - `FALL_THROUGH` [`007dc0cc`](#insn-007dc0cc) → [`007dc0d0`](#insn-007dc0d0)
- ブロック [`007dc0d0`](#insn-007dc0d0) 範囲 `[['007dc0d0', '007dc0d7']]`
  - `FALL_THROUGH` [`007dc0d4`](#insn-007dc0d4) → [`007dc0d8`](#insn-007dc0d8)
- ブロック [`007dc0d8`](#insn-007dc0d8) 範囲 `[['007dc0d8', '007dc0db']]`
  - `FALL_THROUGH` [`007dc0d8`](#insn-007dc0d8) → [`007dc0dc`](#insn-007dc0dc)
- ブロック [`007dc0dc`](#insn-007dc0dc) 範囲 `[['007dc0dc', '007dc0f3']]`
- ブロック [`007dc0f4`](#insn-007dc0f4) 範囲 `[['007dc0f4', '007dc0f7']]`
  - `FALL_THROUGH` [`007dc0f4`](#insn-007dc0f4) → [`007dc0f8`](#insn-007dc0f8)
- ブロック [`007dc0f8`](#insn-007dc0f8) 範囲 `[['007dc0f8', '007dc0fb']]`
  - `FALL_THROUGH` [`007dc0f8`](#insn-007dc0f8) → [`007dc0fc`](../007dc/007dc0fc.md)

## 命令位置別の参照

- [`007dbfcc`](#insn-007dbfcc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007dbfd0`](#insn-007dbfd0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007dbfd4`](#insn-007dbfd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007dbfd8`](#insn-007dbfd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007dbff8`](#insn-007dbff8) → [`007dc088`](#insn-007dc088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007dc000`](#insn-007dc000) → [`007dc024`](#insn-007dc024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007dc010`](#insn-007dc010) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`007dc028`](#insn-007dc028) → [`007dc0f4`](#insn-007dc0f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007dc04c`](#insn-007dc04c) → [`007dc0f4`](#insn-007dc0f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007dc058`](#insn-007dc058) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`007dc070`](#insn-007dc070) → [`007dc0d8`](#insn-007dc0d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007dc080`](#insn-007dc080) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`007dc084`](#insn-007dc084) → [`007dc0d8`](#insn-007dc0d8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007dc094`](#insn-007dc094) → [`007dc0c4`](#insn-007dc0c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007dc0a0`](#insn-007dc0a0) → [`007dc0b0`](#insn-007dc0b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007dc0a8`](#insn-007dc0a8) → [`00bdb0f0`](../00bdb/00bdb0f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0f0` · 推定シンボル `None` · 推定型 `None`
- [`007dc0b4`](#insn-007dc0b4) → [`007dc0d8`](#insn-007dc0d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007dc0c0`](#insn-007dc0c0) → [`007dc0d0`](#insn-007dc0d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007dc0c8`](#insn-007dc0c8) → [`007dc0d8`](#insn-007dc0d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007dc0d4`](#insn-007dc0d4) → [`00bdb0f0`](../00bdb/00bdb0f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0f0` · 推定シンボル `None` · 推定型 `None`
- [`007dc0e0`](#insn-007dc0e0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007dc0e4`](#insn-007dc0e4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007dc0e8`](#insn-007dc0e8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007dc0ec`](#insn-007dc0ec) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007dc0f8`](#insn-007dc0f8) → [`007bfcc8`](../007bf/007bfcc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007bfcc8` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007dbfcc`](#insn-007dbfcc)

~~~json
{
  "source": "007dbfcc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007dbfd0`](#insn-007dbfd0)

~~~json
{
  "source": "007dbfd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007dbfd4`](#insn-007dbfd4)

~~~json
{
  "source": "007dbfd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007dbfd8`](#insn-007dbfd8)

~~~json
{
  "source": "007dbfd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007dbff8`](#insn-007dbff8)

~~~json
{
  "source": "007dbff8",
  "target": "007dc088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007dc000`](#insn-007dc000)

~~~json
{
  "source": "007dc000",
  "target": "007dc024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007dc010`](#insn-007dc010)

~~~json
{
  "source": "007dc010",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007dc028`](#insn-007dc028)

~~~json
{
  "source": "007dc028",
  "target": "007dc0f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007dc04c`](#insn-007dc04c)

~~~json
{
  "source": "007dc04c",
  "target": "007dc0f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007dc058`](#insn-007dc058)

~~~json
{
  "source": "007dc058",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007dc070`](#insn-007dc070)

~~~json
{
  "source": "007dc070",
  "target": "007dc0d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007dc080`](#insn-007dc080)

~~~json
{
  "source": "007dc080",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007dc084`](#insn-007dc084)

~~~json
{
  "source": "007dc084",
  "target": "007dc0d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007dc094`](#insn-007dc094)

~~~json
{
  "source": "007dc094",
  "target": "007dc0c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007dc0a0`](#insn-007dc0a0)

~~~json
{
  "source": "007dc0a0",
  "target": "007dc0b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007dc0a8`](#insn-007dc0a8)

~~~json
{
  "source": "007dc0a8",
  "target": "00bdb0f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007dc0b4`](#insn-007dc0b4)

~~~json
{
  "source": "007dc0b4",
  "target": "007dc0d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007dc0c0`](#insn-007dc0c0)

~~~json
{
  "source": "007dc0c0",
  "target": "007dc0d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007dc0c8`](#insn-007dc0c8)

~~~json
{
  "source": "007dc0c8",
  "target": "007dc0d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007dc0d4`](#insn-007dc0d4)

~~~json
{
  "source": "007dc0d4",
  "target": "00bdb0f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007dc0e0`](#insn-007dc0e0)

~~~json
{
  "source": "007dc0e0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007dc0e4`](#insn-007dc0e4)

~~~json
{
  "source": "007dc0e4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007dc0e8`](#insn-007dc0e8)

~~~json
{
  "source": "007dc0e8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007dc0ec`](#insn-007dc0ec)

~~~json
{
  "source": "007dc0ec",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007dc0f8`](#insn-007dc0f8)

~~~json
{
  "source": "007dc0f8",
  "target": "007bfcc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
