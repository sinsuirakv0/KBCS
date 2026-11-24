# 00bcbef0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bcbeac`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbeac.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-c6fb1769378b687d10e77bf825bafc53)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c48938`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48938.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0078.md#compare-ef6155cf819c6dc54dbae01ebbe06334)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbef0",
  "name": "FUN_00bcbef0",
  "size": 344,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6e2ff0ae7684903e82d3524de5e1b534cf6cde326f9f55182e8bde3dfbc1c876",
  "source_text_sha256": "6e2ff0ae7684903e82d3524de5e1b534cf6cde326f9f55182e8bde3dfbc1c876",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbef0",
        "00bcc047"
      ]
    ],
    "bytes_sha256": "9b27f4828fe7cb2c98487dc3f979f2ff040b23988ee9b9fe1d3840ac15e062ff",
    "instruction_count": 86,
    "instruction_bytes": 344,
    "body_bytes": 344,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bcc050](../00bcc/00bcc050.md)
- [00bdb1b0](../00bdb/00bdb1b0.md)
- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2540 bytes

~~~c

void FUN_00bcbef0(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  void *pvVar2;
  size_t __size;
  long lVar3;
  size_t sVar4;
  void *__src;
  
  lVar3 = param_2[1];
  pvVar2 = (void *)*param_2;
                    /* try { // try from 00bcbf10 to 00ccbf73 has its CatchHandler @ 00bcbf10
                       catch() { ... } // from try @ 00bcbf10 with catch @ 00bcbf10
                       catch() { ... } // from try @ 00bcbf84 with catch @ 00bcbf10 */
  if ((ulong)param_2[2] < lVar3 + 7U) {
    sVar4 = param_2[2] * 2;
    uVar1 = lVar3 + 999;
    if (sVar4 < uVar1 || sVar4 - uVar1 == 0) {
      sVar4 = uVar1;
    }
    param_2[2] = sVar4;
    pvVar2 = realloc(pvVar2,sVar4);
    *param_2 = pvVar2;
    if (pvVar2 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00bcbf74 with catch @ 00bcc03c */
      abort();
    }
    lVar3 = param_2[1];
  }
  *(undefined4 *)((long)pvVar2 + lVar3 + 3) = 0x6164626d;
  *(undefined4 *)((long)pvVar2 + lVar3) = 0x6d616c27;
  lVar3 = param_2[1] + 7;
  param_2[1] = lVar3;
                    /* try { // try from 00bcbf74 to 00ccbf83 has its CatchHandler @ 00bcc03c */
  sVar4 = *(size_t *)(param_1 + 0x48);
  if (sVar4 != 0) {
                    /* try { // try from 00bcbf84 to 00ccc07b has its CatchHandler @ 00bcbf10 */
    __src = *(void **)(param_1 + 0x40);
    pvVar2 = (void *)*param_2;
    if ((ulong)param_2[2] < lVar3 + sVar4) {
      __size = param_2[2] * 2;
      uVar1 = lVar3 + sVar4 + 0x3e0;
      if (__size < uVar1 || __size - uVar1 == 0) {
        __size = uVar1;
      }
      param_2[2] = __size;
      pvVar2 = realloc(pvVar2,__size);
      *param_2 = pvVar2;
      if (pvVar2 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar3 = param_2[1];
    }
    memcpy((void *)((long)pvVar2 + lVar3),__src,sVar4);
    lVar3 = param_2[1] + sVar4;
    param_2[1] = lVar3;
  }
  pvVar2 = (void *)*param_2;
  if ((ulong)param_2[2] < lVar3 + 1U) {
    sVar4 = param_2[2] * 2;
    uVar1 = lVar3 + 0x3e1;
    if (sVar4 < uVar1 || sVar4 - uVar1 == 0) {
      sVar4 = uVar1;
    }
    param_2[2] = sVar4;
    pvVar2 = realloc(pvVar2,sVar4);
    *param_2 = pvVar2;
    if (pvVar2 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar3 = param_2[1];
  }
  *(undefined1 *)((long)pvVar2 + lVar3) = 0x27;
  param_2[1] = param_2[1] + 1;
  FUN_00bcc050(param_1,param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbef0"></a> `00bcbef0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcbef4"></a> `00bcbef4` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcbef8"></a> `00bcbef8` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbefc"></a> `00bcbefc` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbf00"></a> `00bcbf00` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcbf04"></a> `00bcbf04` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbf08"></a> `00bcbf08` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcbf0c"></a> `00bcbf0c` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00bcbf10"></a> `00bcbf10` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcbf14"></a> `00bcbf14` | `2b 1d 00 91` | add x11,x9,#0x7 | `FALL_THROUGH`
<a id="insn-00bcbf18"></a> `00bcbf18` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bcbf1c"></a> `00bcbf1c` | `89 01 00 54` | b.ls 0x00bcbf4c | `CONDITIONAL_JUMP`
<a id="insn-00bcbf20"></a> `00bcbf20` | `4a f9 7f d3` | lsl x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbf24"></a> `00bcbf24` | `29 9d 0f 91` | add x9,x9,#0x3e7 | `FALL_THROUGH`
<a id="insn-00bcbf28"></a> `00bcbf28` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcbf2c"></a> `00bcbf2c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcbf30"></a> `00bcbf30` | `41 81 89 9a` | csel x1,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00bcbf34"></a> `00bcbf34` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbf38"></a> `00bcbf38` | `c6 44 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbf3c"></a> `00bcbf3c` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbf40"></a> `00bcbf40` | `e0 07 00 b4` | cbz x0,0x00bcc03c | `CONDITIONAL_JUMP`
<a id="insn-00bcbf44"></a> `00bcbf44` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbf48"></a> `00bcbf48` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bcbf4c"></a> `00bcbf4c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bcbf50"></a> `00bcbf50` | `a9 4d 8c 52` | mov w9,#0x626d | `FALL_THROUGH`
<a id="insn-00bcbf54"></a> `00bcbf54` | `ea 84 8d 52` | mov w10,#0x6c27 | `FALL_THROUGH`
<a id="insn-00bcbf58"></a> `00bcbf58` | `89 2c ac 72` | movk w9,#0x6164, LSL #16 | `FALL_THROUGH`
<a id="insn-00bcbf5c"></a> `00bcbf5c` | `2a ac ad 72` | movk w10,#0x6d61, LSL #16 | `FALL_THROUGH`
<a id="insn-00bcbf60"></a> `00bcbf60` | `09 31 00 b8` | stur w9,[x8, #0x3] | `FALL_THROUGH`
<a id="insn-00bcbf64"></a> `00bcbf64` | `0a 01 00 b9` | str w10,[x8] | `FALL_THROUGH`
<a id="insn-00bcbf68"></a> `00bcbf68` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbf6c"></a> `00bcbf6c` | `08 1d 00 91` | add x8,x8,#0x7 | `FALL_THROUGH`
<a id="insn-00bcbf70"></a> `00bcbf70` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbf74"></a> `00bcbf74` | `95 26 40 f9` | ldr x21,[x20, #0x48] | `FALL_THROUGH`
<a id="insn-00bcbf78"></a> `00bcbf78` | `f5 02 00 b4` | cbz x21,0x00bcbfd4 | `CONDITIONAL_JUMP`
<a id="insn-00bcbf7c"></a> `00bcbf7c` | `6a 0a 40 f9` | ldr x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbf80"></a> `00bcbf80` | `09 01 15 8b` | add x9,x8,x21 | `FALL_THROUGH`
<a id="insn-00bcbf84"></a> `00bcbf84` | `96 22 40 f9` | ldr x22,[x20, #0x40] | `FALL_THROUGH`
<a id="insn-00bcbf88"></a> `00bcbf88` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbf8c"></a> `00bcbf8c` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bcbf90"></a> `00bcbf90` | `49 01 00 54` | b.ls 0x00bcbfb8 | `CONDITIONAL_JUMP`
<a id="insn-00bcbf94"></a> `00bcbf94` | `48 f9 7f d3` | lsl x8,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbf98"></a> `00bcbf98` | `29 81 0f 91` | add x9,x9,#0x3e0 | `FALL_THROUGH`
<a id="insn-00bcbf9c"></a> `00bcbf9c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcbfa0"></a> `00bcbfa0` | `01 81 89 9a` | csel x1,x8,x9,hi | `FALL_THROUGH`
<a id="insn-00bcbfa4"></a> `00bcbfa4` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbfa8"></a> `00bcbfa8` | `aa 44 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbfac"></a> `00bcbfac` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbfb0"></a> `00bcbfb0` | `a0 04 00 b4` | cbz x0,0x00bcc044 | `CONDITIONAL_JUMP`
<a id="insn-00bcbfb4"></a> `00bcbfb4` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbfb8"></a> `00bcbfb8` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00bcbfbc"></a> `00bcbfbc` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcbfc0"></a> `00bcbfc0` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bcbfc4"></a> `00bcbfc4` | `7b 3c 00 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbfc8"></a> `00bcbfc8` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbfcc"></a> `00bcbfcc` | `08 01 15 8b` | add x8,x8,x21 | `FALL_THROUGH`
<a id="insn-00bcbfd0"></a> `00bcbfd0` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbfd4"></a> `00bcbfd4` | `69 0a 40 f9` | ldr x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbfd8"></a> `00bcbfd8` | `0a 05 00 91` | add x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbfdc"></a> `00bcbfdc` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbfe0"></a> `00bcbfe0` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcbfe4"></a> `00bcbfe4` | `49 01 00 54` | b.ls 0x00bcc00c | `CONDITIONAL_JUMP`
<a id="insn-00bcbfe8"></a> `00bcbfe8` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbfec"></a> `00bcbfec` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bcbff0"></a> `00bcbff0` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcbff4"></a> `00bcbff4` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcbff8"></a> `00bcbff8` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbffc"></a> `00bcbffc` | `95 44 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bcc000"></a> `00bcc000` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcc004"></a> `00bcc004` | `e0 01 00 b4` | cbz x0,0x00bcc040 | `CONDITIONAL_JUMP`
<a id="insn-00bcc008"></a> `00bcc008` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcc00c"></a> `00bcc00c` | `e9 04 80 52` | mov w9,#0x27 | `FALL_THROUGH`
<a id="insn-00bcc010"></a> `00bcc010` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bcc014"></a> `00bcc014` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcc018"></a> `00bcc018` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcc01c"></a> `00bcc01c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcc020"></a> `00bcc020` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcc024"></a> `00bcc024` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcc028"></a> `00bcc028` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcc02c"></a> `00bcc02c` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc030"></a> `00bcc030` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcc034"></a> `00bcc034` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcc038"></a> `00bcc038` | `06 00 00 14` | b 0x00bcc050 | `CALL_TERMINATOR`
<a id="insn-00bcc03c"></a> `00bcc03c` | `a1 48 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`
<a id="insn-00bcc040"></a> `00bcc040` | `a0 48 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`
<a id="insn-00bcc044"></a> `00bcc044` | `9f 48 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbef0`](#insn-00bcbef0) 範囲 `[['00bcbef0', '00bcbf0f']]`
  - `FALL_THROUGH` [`00bcbf0c`](#insn-00bcbf0c) → [`00bcbf10`](#insn-00bcbf10)
- ブロック [`00bcbf10`](#insn-00bcbf10) 範囲 `[['00bcbf10', '00bcbf1f']]`
  - `CONDITIONAL_JUMP` [`00bcbf1c`](#insn-00bcbf1c) → [`00bcbf4c`](#insn-00bcbf4c)
  - `FALL_THROUGH` [`00bcbf1c`](#insn-00bcbf1c) → [`00bcbf20`](#insn-00bcbf20)
- ブロック [`00bcbf20`](#insn-00bcbf20) 範囲 `[['00bcbf20', '00bcbf43']]`
  - `CONDITIONAL_JUMP` [`00bcbf40`](#insn-00bcbf40) → [`00bcc03c`](#insn-00bcc03c)
  - `FALL_THROUGH` [`00bcbf40`](#insn-00bcbf40) → [`00bcbf44`](#insn-00bcbf44)
- ブロック [`00bcbf44`](#insn-00bcbf44) 範囲 `[['00bcbf44', '00bcbf4b']]`
  - `FALL_THROUGH` [`00bcbf48`](#insn-00bcbf48) → [`00bcbf4c`](#insn-00bcbf4c)
- ブロック [`00bcbf4c`](#insn-00bcbf4c) 範囲 `[['00bcbf4c', '00bcbf73']]`
  - `FALL_THROUGH` [`00bcbf70`](#insn-00bcbf70) → [`00bcbf74`](#insn-00bcbf74)
- ブロック [`00bcbf74`](#insn-00bcbf74) 範囲 `[['00bcbf74', '00bcbf7b']]`
  - `CONDITIONAL_JUMP` [`00bcbf78`](#insn-00bcbf78) → [`00bcbfd4`](#insn-00bcbfd4)
  - `FALL_THROUGH` [`00bcbf78`](#insn-00bcbf78) → [`00bcbf7c`](#insn-00bcbf7c)
- ブロック [`00bcbf7c`](#insn-00bcbf7c) 範囲 `[['00bcbf7c', '00bcbf83']]`
  - `FALL_THROUGH` [`00bcbf80`](#insn-00bcbf80) → [`00bcbf84`](#insn-00bcbf84)
- ブロック [`00bcbf84`](#insn-00bcbf84) 範囲 `[['00bcbf84', '00bcbf93']]`
  - `CONDITIONAL_JUMP` [`00bcbf90`](#insn-00bcbf90) → [`00bcbfb8`](#insn-00bcbfb8)
  - `FALL_THROUGH` [`00bcbf90`](#insn-00bcbf90) → [`00bcbf94`](#insn-00bcbf94)
- ブロック [`00bcbf94`](#insn-00bcbf94) 範囲 `[['00bcbf94', '00bcbfb3']]`
  - `CONDITIONAL_JUMP` [`00bcbfb0`](#insn-00bcbfb0) → [`00bcc044`](#insn-00bcc044)
  - `FALL_THROUGH` [`00bcbfb0`](#insn-00bcbfb0) → [`00bcbfb4`](#insn-00bcbfb4)
- ブロック [`00bcbfb4`](#insn-00bcbfb4) 範囲 `[['00bcbfb4', '00bcbfb7']]`
  - `FALL_THROUGH` [`00bcbfb4`](#insn-00bcbfb4) → [`00bcbfb8`](#insn-00bcbfb8)
- ブロック [`00bcbfb8`](#insn-00bcbfb8) 範囲 `[['00bcbfb8', '00bcbfd3']]`
  - `FALL_THROUGH` [`00bcbfd0`](#insn-00bcbfd0) → [`00bcbfd4`](#insn-00bcbfd4)
- ブロック [`00bcbfd4`](#insn-00bcbfd4) 範囲 `[['00bcbfd4', '00bcbfe7']]`
  - `CONDITIONAL_JUMP` [`00bcbfe4`](#insn-00bcbfe4) → [`00bcc00c`](#insn-00bcc00c)
  - `FALL_THROUGH` [`00bcbfe4`](#insn-00bcbfe4) → [`00bcbfe8`](#insn-00bcbfe8)
- ブロック [`00bcbfe8`](#insn-00bcbfe8) 範囲 `[['00bcbfe8', '00bcc007']]`
  - `CONDITIONAL_JUMP` [`00bcc004`](#insn-00bcc004) → [`00bcc040`](#insn-00bcc040)
  - `FALL_THROUGH` [`00bcc004`](#insn-00bcc004) → [`00bcc008`](#insn-00bcc008)
- ブロック [`00bcc008`](#insn-00bcc008) 範囲 `[['00bcc008', '00bcc00b']]`
  - `FALL_THROUGH` [`00bcc008`](#insn-00bcc008) → [`00bcc00c`](#insn-00bcc00c)
- ブロック [`00bcc00c`](#insn-00bcc00c) 範囲 `[['00bcc00c', '00bcc03b']]`
- ブロック [`00bcc03c`](#insn-00bcc03c) 範囲 `[['00bcc03c', '00bcc03f']]`
- ブロック [`00bcc040`](#insn-00bcc040) 範囲 `[['00bcc040', '00bcc043']]`
- ブロック [`00bcc044`](#insn-00bcc044) 範囲 `[['00bcc044', '00bcc047']]`

## 命令位置別の参照

- [`00bcbef4`](#insn-00bcbef4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbef8`](#insn-00bcbef8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbefc`](#insn-00bcbefc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf1c`](#insn-00bcbf1c) → [`00bcbf4c`](#insn-00bcbf4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf38`](#insn-00bcbf38) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf40`](#insn-00bcbf40) → [`00bcc03c`](#insn-00bcc03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf78`](#insn-00bcbf78) → [`00bcbfd4`](#insn-00bcbfd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf90`](#insn-00bcbf90) → [`00bcbfb8`](#insn-00bcbfb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfa8`](#insn-00bcbfa8) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfb0`](#insn-00bcbfb0) → [`00bcc044`](#insn-00bcc044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfc4`](#insn-00bcbfc4) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfe4`](#insn-00bcbfe4) → [`00bcc00c`](#insn-00bcc00c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbffc`](#insn-00bcbffc) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bcc004`](#insn-00bcc004) → [`00bcc040`](#insn-00bcc040) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc028`](#insn-00bcc028) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc02c`](#insn-00bcc02c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc030`](#insn-00bcc030) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc038`](#insn-00bcc038) → [`00bcc050`](../00bcc/00bcc050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bcc050` · 推定シンボル `None` · 推定型 `None`
- [`00bcc03c`](#insn-00bcc03c) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`
- [`00bcc040`](#insn-00bcc040) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`
- [`00bcc044`](#insn-00bcc044) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbef4`](#insn-00bcbef4)

~~~json
{
  "source": "00bcbef4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbef8`](#insn-00bcbef8)

~~~json
{
  "source": "00bcbef8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbefc`](#insn-00bcbefc)

~~~json
{
  "source": "00bcbefc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf1c`](#insn-00bcbf1c)

~~~json
{
  "source": "00bcbf1c",
  "target": "00bcbf4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf38`](#insn-00bcbf38)

~~~json
{
  "source": "00bcbf38",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbf40`](#insn-00bcbf40)

~~~json
{
  "source": "00bcbf40",
  "target": "00bcc03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf78`](#insn-00bcbf78)

~~~json
{
  "source": "00bcbf78",
  "target": "00bcbfd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf90`](#insn-00bcbf90)

~~~json
{
  "source": "00bcbf90",
  "target": "00bcbfb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfa8`](#insn-00bcbfa8)

~~~json
{
  "source": "00bcbfa8",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbfb0`](#insn-00bcbfb0)

~~~json
{
  "source": "00bcbfb0",
  "target": "00bcc044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfc4`](#insn-00bcbfc4)

~~~json
{
  "source": "00bcbfc4",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbfe4`](#insn-00bcbfe4)

~~~json
{
  "source": "00bcbfe4",
  "target": "00bcc00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbffc`](#insn-00bcbffc)

~~~json
{
  "source": "00bcbffc",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcc004`](#insn-00bcc004)

~~~json
{
  "source": "00bcc004",
  "target": "00bcc040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc028`](#insn-00bcc028)

~~~json
{
  "source": "00bcc028",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc02c`](#insn-00bcc02c)

~~~json
{
  "source": "00bcc02c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc030`](#insn-00bcc030)

~~~json
{
  "source": "00bcc030",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc038`](#insn-00bcc038)

~~~json
{
  "source": "00bcc038",
  "target": "00bcc050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcc03c`](#insn-00bcc03c)

~~~json
{
  "source": "00bcc03c",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcc040`](#insn-00bcc040)

~~~json
{
  "source": "00bcc040",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcc044`](#insn-00bcc044)

~~~json
{
  "source": "00bcc044",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
