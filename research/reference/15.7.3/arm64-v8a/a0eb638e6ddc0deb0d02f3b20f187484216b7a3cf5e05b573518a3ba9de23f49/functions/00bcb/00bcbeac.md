# 00bcbeac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bcbde4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbde4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0007.md#compare-164c16137ff0dd5046c110831f7dda4d)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bcbef0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbef0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-c6fb1769378b687d10e77bf825bafc53)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbeac",
  "name": "FUN_00bcbeac",
  "size": 344,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9910335382f8d99d14cbc92536bee8bc4de299a5e11532096bb38a2a60d6ee17",
  "source_text_sha256": "9910335382f8d99d14cbc92536bee8bc4de299a5e11532096bb38a2a60d6ee17",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbeac",
        "00bcc003"
      ]
    ],
    "bytes_sha256": "c84998bf50003e7727897c6e9839176339d3fff7acd4aca8e0194a7ab3f68f7f",
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

- [00bcc00c](../00bcc/00bcc00c.md)
- [00bdb160](../00bdb/00bdb160.md)
- [00bdd200](../00bdd/00bdd200.md)
- [00bde270](../00bde/00bde270.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2540 bytes

~~~c

void FUN_00bcbeac(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  void *pvVar2;
  size_t __size;
  long lVar3;
  size_t sVar4;
  void *__src;
  
  lVar3 = param_2[1];
  pvVar2 = (void *)*param_2;
                    /* try { // try from 00bcbecc to 00ccbf2f has its CatchHandler @ 00bcbecc
                       catch() { ... } // from try @ 00bcbecc with catch @ 00bcbecc
                       catch() { ... } // from try @ 00bcbf40 with catch @ 00bcbecc */
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
                    /* catch() { ... } // from try @ 00bcbf30 with catch @ 00bcbff8 */
      abort();
    }
    lVar3 = param_2[1];
  }
  *(undefined4 *)((long)pvVar2 + lVar3 + 3) = 0x6164626d;
  *(undefined4 *)((long)pvVar2 + lVar3) = 0x6d616c27;
  lVar3 = param_2[1] + 7;
  param_2[1] = lVar3;
                    /* try { // try from 00bcbf30 to 00ccbf3f has its CatchHandler @ 00bcbff8 */
  sVar4 = *(size_t *)(param_1 + 0x48);
  if (sVar4 != 0) {
                    /* try { // try from 00bcbf40 to 00ccc037 has its CatchHandler @ 00bcbecc */
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
  FUN_00bcc00c(param_1,param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbeac"></a> `00bcbeac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcbeb0"></a> `00bcbeb0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcbeb4"></a> `00bcbeb4` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbeb8"></a> `00bcbeb8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbebc"></a> `00bcbebc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcbec0"></a> `00bcbec0` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbec4"></a> `00bcbec4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcbec8"></a> `00bcbec8` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00bcbecc"></a> `00bcbecc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcbed0"></a> `00bcbed0` | `2b 1d 00 91` | add x11,x9,#0x7 | `FALL_THROUGH`
<a id="insn-00bcbed4"></a> `00bcbed4` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bcbed8"></a> `00bcbed8` | `89 01 00 54` | b.ls 0x00bcbf08 | `CONDITIONAL_JUMP`
<a id="insn-00bcbedc"></a> `00bcbedc` | `4a f9 7f d3` | lsl x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbee0"></a> `00bcbee0` | `29 9d 0f 91` | add x9,x9,#0x3e7 | `FALL_THROUGH`
<a id="insn-00bcbee4"></a> `00bcbee4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcbee8"></a> `00bcbee8` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcbeec"></a> `00bcbeec` | `41 81 89 9a` | csel x1,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00bcbef0"></a> `00bcbef0` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbef4"></a> `00bcbef4` | `c3 44 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbef8"></a> `00bcbef8` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbefc"></a> `00bcbefc` | `e0 07 00 b4` | cbz x0,0x00bcbff8 | `CONDITIONAL_JUMP`
<a id="insn-00bcbf00"></a> `00bcbf00` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbf04"></a> `00bcbf04` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bcbf08"></a> `00bcbf08` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bcbf0c"></a> `00bcbf0c` | `a9 4d 8c 52` | mov w9,#0x626d | `FALL_THROUGH`
<a id="insn-00bcbf10"></a> `00bcbf10` | `ea 84 8d 52` | mov w10,#0x6c27 | `FALL_THROUGH`
<a id="insn-00bcbf14"></a> `00bcbf14` | `89 2c ac 72` | movk w9,#0x6164, LSL #16 | `FALL_THROUGH`
<a id="insn-00bcbf18"></a> `00bcbf18` | `2a ac ad 72` | movk w10,#0x6d61, LSL #16 | `FALL_THROUGH`
<a id="insn-00bcbf1c"></a> `00bcbf1c` | `09 31 00 b8` | stur w9,[x8, #0x3] | `FALL_THROUGH`
<a id="insn-00bcbf20"></a> `00bcbf20` | `0a 01 00 b9` | str w10,[x8] | `FALL_THROUGH`
<a id="insn-00bcbf24"></a> `00bcbf24` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbf28"></a> `00bcbf28` | `08 1d 00 91` | add x8,x8,#0x7 | `FALL_THROUGH`
<a id="insn-00bcbf2c"></a> `00bcbf2c` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbf30"></a> `00bcbf30` | `95 26 40 f9` | ldr x21,[x20, #0x48] | `FALL_THROUGH`
<a id="insn-00bcbf34"></a> `00bcbf34` | `f5 02 00 b4` | cbz x21,0x00bcbf90 | `CONDITIONAL_JUMP`
<a id="insn-00bcbf38"></a> `00bcbf38` | `6a 0a 40 f9` | ldr x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbf3c"></a> `00bcbf3c` | `09 01 15 8b` | add x9,x8,x21 | `FALL_THROUGH`
<a id="insn-00bcbf40"></a> `00bcbf40` | `96 22 40 f9` | ldr x22,[x20, #0x40] | `FALL_THROUGH`
<a id="insn-00bcbf44"></a> `00bcbf44` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbf48"></a> `00bcbf48` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bcbf4c"></a> `00bcbf4c` | `49 01 00 54` | b.ls 0x00bcbf74 | `CONDITIONAL_JUMP`
<a id="insn-00bcbf50"></a> `00bcbf50` | `48 f9 7f d3` | lsl x8,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbf54"></a> `00bcbf54` | `29 81 0f 91` | add x9,x9,#0x3e0 | `FALL_THROUGH`
<a id="insn-00bcbf58"></a> `00bcbf58` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcbf5c"></a> `00bcbf5c` | `01 81 89 9a` | csel x1,x8,x9,hi | `FALL_THROUGH`
<a id="insn-00bcbf60"></a> `00bcbf60` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbf64"></a> `00bcbf64` | `a7 44 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbf68"></a> `00bcbf68` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbf6c"></a> `00bcbf6c` | `a0 04 00 b4` | cbz x0,0x00bcc000 | `CONDITIONAL_JUMP`
<a id="insn-00bcbf70"></a> `00bcbf70` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbf74"></a> `00bcbf74` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00bcbf78"></a> `00bcbf78` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcbf7c"></a> `00bcbf7c` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bcbf80"></a> `00bcbf80` | `78 3c 00 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbf84"></a> `00bcbf84` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbf88"></a> `00bcbf88` | `08 01 15 8b` | add x8,x8,x21 | `FALL_THROUGH`
<a id="insn-00bcbf8c"></a> `00bcbf8c` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbf90"></a> `00bcbf90` | `69 0a 40 f9` | ldr x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbf94"></a> `00bcbf94` | `0a 05 00 91` | add x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbf98"></a> `00bcbf98` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbf9c"></a> `00bcbf9c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcbfa0"></a> `00bcbfa0` | `49 01 00 54` | b.ls 0x00bcbfc8 | `CONDITIONAL_JUMP`
<a id="insn-00bcbfa4"></a> `00bcbfa4` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbfa8"></a> `00bcbfa8` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bcbfac"></a> `00bcbfac` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcbfb0"></a> `00bcbfb0` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcbfb4"></a> `00bcbfb4` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbfb8"></a> `00bcbfb8` | `92 44 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbfbc"></a> `00bcbfbc` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbfc0"></a> `00bcbfc0` | `e0 01 00 b4` | cbz x0,0x00bcbffc | `CONDITIONAL_JUMP`
<a id="insn-00bcbfc4"></a> `00bcbfc4` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbfc8"></a> `00bcbfc8` | `e9 04 80 52` | mov w9,#0x27 | `FALL_THROUGH`
<a id="insn-00bcbfcc"></a> `00bcbfcc` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bcbfd0"></a> `00bcbfd0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcbfd4"></a> `00bcbfd4` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbfd8"></a> `00bcbfd8` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcbfdc"></a> `00bcbfdc` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbfe0"></a> `00bcbfe0` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbfe4"></a> `00bcbfe4` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbfe8"></a> `00bcbfe8` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbfec"></a> `00bcbfec` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcbff0"></a> `00bcbff0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcbff4"></a> `00bcbff4` | `06 00 00 14` | b 0x00bcc00c | `CALL_TERMINATOR`
<a id="insn-00bcbff8"></a> `00bcbff8` | `9e 48 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bcbffc"></a> `00bcbffc` | `9d 48 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bcc000"></a> `00bcc000` | `9c 48 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbeac`](#insn-00bcbeac) 範囲 `[['00bcbeac', '00bcbecb']]`
  - `FALL_THROUGH` [`00bcbec8`](#insn-00bcbec8) → [`00bcbecc`](#insn-00bcbecc)
- ブロック [`00bcbecc`](#insn-00bcbecc) 範囲 `[['00bcbecc', '00bcbedb']]`
  - `CONDITIONAL_JUMP` [`00bcbed8`](#insn-00bcbed8) → [`00bcbf08`](#insn-00bcbf08)
  - `FALL_THROUGH` [`00bcbed8`](#insn-00bcbed8) → [`00bcbedc`](#insn-00bcbedc)
- ブロック [`00bcbedc`](#insn-00bcbedc) 範囲 `[['00bcbedc', '00bcbeff']]`
  - `CONDITIONAL_JUMP` [`00bcbefc`](#insn-00bcbefc) → [`00bcbff8`](#insn-00bcbff8)
  - `FALL_THROUGH` [`00bcbefc`](#insn-00bcbefc) → [`00bcbf00`](#insn-00bcbf00)
- ブロック [`00bcbf00`](#insn-00bcbf00) 範囲 `[['00bcbf00', '00bcbf07']]`
  - `FALL_THROUGH` [`00bcbf04`](#insn-00bcbf04) → [`00bcbf08`](#insn-00bcbf08)
- ブロック [`00bcbf08`](#insn-00bcbf08) 範囲 `[['00bcbf08', '00bcbf2f']]`
  - `FALL_THROUGH` [`00bcbf2c`](#insn-00bcbf2c) → [`00bcbf30`](#insn-00bcbf30)
- ブロック [`00bcbf30`](#insn-00bcbf30) 範囲 `[['00bcbf30', '00bcbf37']]`
  - `CONDITIONAL_JUMP` [`00bcbf34`](#insn-00bcbf34) → [`00bcbf90`](#insn-00bcbf90)
  - `FALL_THROUGH` [`00bcbf34`](#insn-00bcbf34) → [`00bcbf38`](#insn-00bcbf38)
- ブロック [`00bcbf38`](#insn-00bcbf38) 範囲 `[['00bcbf38', '00bcbf3f']]`
  - `FALL_THROUGH` [`00bcbf3c`](#insn-00bcbf3c) → [`00bcbf40`](#insn-00bcbf40)
- ブロック [`00bcbf40`](#insn-00bcbf40) 範囲 `[['00bcbf40', '00bcbf4f']]`
  - `CONDITIONAL_JUMP` [`00bcbf4c`](#insn-00bcbf4c) → [`00bcbf74`](#insn-00bcbf74)
  - `FALL_THROUGH` [`00bcbf4c`](#insn-00bcbf4c) → [`00bcbf50`](#insn-00bcbf50)
- ブロック [`00bcbf50`](#insn-00bcbf50) 範囲 `[['00bcbf50', '00bcbf6f']]`
  - `CONDITIONAL_JUMP` [`00bcbf6c`](#insn-00bcbf6c) → [`00bcc000`](#insn-00bcc000)
  - `FALL_THROUGH` [`00bcbf6c`](#insn-00bcbf6c) → [`00bcbf70`](#insn-00bcbf70)
- ブロック [`00bcbf70`](#insn-00bcbf70) 範囲 `[['00bcbf70', '00bcbf73']]`
  - `FALL_THROUGH` [`00bcbf70`](#insn-00bcbf70) → [`00bcbf74`](#insn-00bcbf74)
- ブロック [`00bcbf74`](#insn-00bcbf74) 範囲 `[['00bcbf74', '00bcbf8f']]`
  - `FALL_THROUGH` [`00bcbf8c`](#insn-00bcbf8c) → [`00bcbf90`](#insn-00bcbf90)
- ブロック [`00bcbf90`](#insn-00bcbf90) 範囲 `[['00bcbf90', '00bcbfa3']]`
  - `CONDITIONAL_JUMP` [`00bcbfa0`](#insn-00bcbfa0) → [`00bcbfc8`](#insn-00bcbfc8)
  - `FALL_THROUGH` [`00bcbfa0`](#insn-00bcbfa0) → [`00bcbfa4`](#insn-00bcbfa4)
- ブロック [`00bcbfa4`](#insn-00bcbfa4) 範囲 `[['00bcbfa4', '00bcbfc3']]`
  - `CONDITIONAL_JUMP` [`00bcbfc0`](#insn-00bcbfc0) → [`00bcbffc`](#insn-00bcbffc)
  - `FALL_THROUGH` [`00bcbfc0`](#insn-00bcbfc0) → [`00bcbfc4`](#insn-00bcbfc4)
- ブロック [`00bcbfc4`](#insn-00bcbfc4) 範囲 `[['00bcbfc4', '00bcbfc7']]`
  - `FALL_THROUGH` [`00bcbfc4`](#insn-00bcbfc4) → [`00bcbfc8`](#insn-00bcbfc8)
- ブロック [`00bcbfc8`](#insn-00bcbfc8) 範囲 `[['00bcbfc8', '00bcbff7']]`
- ブロック [`00bcbff8`](#insn-00bcbff8) 範囲 `[['00bcbff8', '00bcbffb']]`
- ブロック [`00bcbffc`](#insn-00bcbffc) 範囲 `[['00bcbffc', '00bcbfff']]`
- ブロック [`00bcc000`](#insn-00bcc000) 範囲 `[['00bcc000', '00bcc003']]`

## 命令位置別の参照

- [`00bcbeb0`](#insn-00bcbeb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbeb4`](#insn-00bcbeb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbeb8`](#insn-00bcbeb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbed8`](#insn-00bcbed8) → [`00bcbf08`](#insn-00bcbf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbef4`](#insn-00bcbef4) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bcbefc`](#insn-00bcbefc) → [`00bcbff8`](#insn-00bcbff8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf34`](#insn-00bcbf34) → [`00bcbf90`](#insn-00bcbf90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf4c`](#insn-00bcbf4c) → [`00bcbf74`](#insn-00bcbf74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf64`](#insn-00bcbf64) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf6c`](#insn-00bcbf6c) → [`00bcc000`](#insn-00bcc000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf80`](#insn-00bcbf80) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfa0`](#insn-00bcbfa0) → [`00bcbfc8`](#insn-00bcbfc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfb8`](#insn-00bcbfb8) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfc0`](#insn-00bcbfc0) → [`00bcbffc`](#insn-00bcbffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfe4`](#insn-00bcbfe4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfe8`](#insn-00bcbfe8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfec`](#insn-00bcbfec) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbff4`](#insn-00bcbff4) → [`00bcc00c`](../00bcc/00bcc00c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bcc00c` · 推定シンボル `None` · 推定型 `None`
- [`00bcbff8`](#insn-00bcbff8) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bcbffc`](#insn-00bcbffc) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bcc000`](#insn-00bcc000) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbeb0`](#insn-00bcbeb0)

~~~json
{
  "source": "00bcbeb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbeb4`](#insn-00bcbeb4)

~~~json
{
  "source": "00bcbeb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbeb8`](#insn-00bcbeb8)

~~~json
{
  "source": "00bcbeb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbed8`](#insn-00bcbed8)

~~~json
{
  "source": "00bcbed8",
  "target": "00bcbf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbef4`](#insn-00bcbef4)

~~~json
{
  "source": "00bcbef4",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbefc`](#insn-00bcbefc)

~~~json
{
  "source": "00bcbefc",
  "target": "00bcbff8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf34`](#insn-00bcbf34)

~~~json
{
  "source": "00bcbf34",
  "target": "00bcbf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf4c`](#insn-00bcbf4c)

~~~json
{
  "source": "00bcbf4c",
  "target": "00bcbf74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf64`](#insn-00bcbf64)

~~~json
{
  "source": "00bcbf64",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbf6c`](#insn-00bcbf6c)

~~~json
{
  "source": "00bcbf6c",
  "target": "00bcc000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf80`](#insn-00bcbf80)

~~~json
{
  "source": "00bcbf80",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbfa0`](#insn-00bcbfa0)

~~~json
{
  "source": "00bcbfa0",
  "target": "00bcbfc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfb8`](#insn-00bcbfb8)

~~~json
{
  "source": "00bcbfb8",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbfc0`](#insn-00bcbfc0)

~~~json
{
  "source": "00bcbfc0",
  "target": "00bcbffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfe4`](#insn-00bcbfe4)

~~~json
{
  "source": "00bcbfe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfe8`](#insn-00bcbfe8)

~~~json
{
  "source": "00bcbfe8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfec`](#insn-00bcbfec)

~~~json
{
  "source": "00bcbfec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbff4`](#insn-00bcbff4)

~~~json
{
  "source": "00bcbff4",
  "target": "00bcc00c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbff8`](#insn-00bcbff8)

~~~json
{
  "source": "00bcbff8",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbffc`](#insn-00bcbffc)

~~~json
{
  "source": "00bcbffc",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcc000`](#insn-00bcc000)

~~~json
{
  "source": "00bcc000",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
