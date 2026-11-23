# 00bcbde4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bcbeac`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbeac.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0007.md#compare-164c16137ff0dd5046c110831f7dda4d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbde4",
  "name": "FUN_00bcbde4",
  "size": 344,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3f8685a154bf10d3b160056b41798462e7a2bd456ed799e18907f3e672e17035",
  "source_text_sha256": "3f8685a154bf10d3b160056b41798462e7a2bd456ed799e18907f3e672e17035",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbde4",
        "00bcbf3b"
      ]
    ],
    "bytes_sha256": "58e47944bcaaf44d7f51b890e5986b081861d6272671042b97319ec62e71122f",
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

- [00bcbf44](../00bcb/00bcbf44.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)
- [00bdd150](../00bdd/00bdd150.md)
- [00bde1c0](../00bde/00bde1c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2540 bytes

~~~c

void FUN_00bcbde4(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  void *pvVar2;
  size_t __size;
  long lVar3;
  size_t sVar4;
  void *__src;
  
  lVar3 = param_2[1];
  pvVar2 = (void *)*param_2;
                    /* try { // try from 00bcbe04 to 00ccbe67 has its CatchHandler @ 00bcbe04
                       catch() { ... } // from try @ 00bcbe04 with catch @ 00bcbe04
                       catch() { ... } // from try @ 00bcbe78 with catch @ 00bcbe04 */
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
                    /* catch() { ... } // from try @ 00bcbe68 with catch @ 00bcbf30 */
      abort();
    }
    lVar3 = param_2[1];
  }
  *(undefined4 *)((long)pvVar2 + lVar3 + 3) = 0x6164626d;
  *(undefined4 *)((long)pvVar2 + lVar3) = 0x6d616c27;
  lVar3 = param_2[1] + 7;
  param_2[1] = lVar3;
                    /* try { // try from 00bcbe68 to 00ccbe77 has its CatchHandler @ 00bcbf30 */
  sVar4 = *(size_t *)(param_1 + 0x48);
  if (sVar4 != 0) {
                    /* try { // try from 00bcbe78 to 00ccbf6f has its CatchHandler @ 00bcbe04 */
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
  FUN_00bcbf44(param_1,param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbde4"></a> `00bcbde4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcbde8"></a> `00bcbde8` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcbdec"></a> `00bcbdec` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbdf0"></a> `00bcbdf0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbdf4"></a> `00bcbdf4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcbdf8"></a> `00bcbdf8` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbdfc"></a> `00bcbdfc` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcbe00"></a> `00bcbe00` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00bcbe04"></a> `00bcbe04` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcbe08"></a> `00bcbe08` | `2b 1d 00 91` | add x11,x9,#0x7 | `FALL_THROUGH`
<a id="insn-00bcbe0c"></a> `00bcbe0c` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bcbe10"></a> `00bcbe10` | `89 01 00 54` | b.ls 0x00bcbe40 | `CONDITIONAL_JUMP`
<a id="insn-00bcbe14"></a> `00bcbe14` | `4a f9 7f d3` | lsl x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbe18"></a> `00bcbe18` | `29 9d 0f 91` | add x9,x9,#0x3e7 | `FALL_THROUGH`
<a id="insn-00bcbe1c"></a> `00bcbe1c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcbe20"></a> `00bcbe20` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcbe24"></a> `00bcbe24` | `41 81 89 9a` | csel x1,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00bcbe28"></a> `00bcbe28` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbe2c"></a> `00bcbe2c` | `c9 44 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbe30"></a> `00bcbe30` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbe34"></a> `00bcbe34` | `e0 07 00 b4` | cbz x0,0x00bcbf30 | `CONDITIONAL_JUMP`
<a id="insn-00bcbe38"></a> `00bcbe38` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbe3c"></a> `00bcbe3c` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bcbe40"></a> `00bcbe40` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bcbe44"></a> `00bcbe44` | `a9 4d 8c 52` | mov w9,#0x626d | `FALL_THROUGH`
<a id="insn-00bcbe48"></a> `00bcbe48` | `ea 84 8d 52` | mov w10,#0x6c27 | `FALL_THROUGH`
<a id="insn-00bcbe4c"></a> `00bcbe4c` | `89 2c ac 72` | movk w9,#0x6164, LSL #16 | `FALL_THROUGH`
<a id="insn-00bcbe50"></a> `00bcbe50` | `2a ac ad 72` | movk w10,#0x6d61, LSL #16 | `FALL_THROUGH`
<a id="insn-00bcbe54"></a> `00bcbe54` | `09 31 00 b8` | stur w9,[x8, #0x3] | `FALL_THROUGH`
<a id="insn-00bcbe58"></a> `00bcbe58` | `0a 01 00 b9` | str w10,[x8] | `FALL_THROUGH`
<a id="insn-00bcbe5c"></a> `00bcbe5c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbe60"></a> `00bcbe60` | `08 1d 00 91` | add x8,x8,#0x7 | `FALL_THROUGH`
<a id="insn-00bcbe64"></a> `00bcbe64` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbe68"></a> `00bcbe68` | `95 26 40 f9` | ldr x21,[x20, #0x48] | `FALL_THROUGH`
<a id="insn-00bcbe6c"></a> `00bcbe6c` | `f5 02 00 b4` | cbz x21,0x00bcbec8 | `CONDITIONAL_JUMP`
<a id="insn-00bcbe70"></a> `00bcbe70` | `6a 0a 40 f9` | ldr x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbe74"></a> `00bcbe74` | `09 01 15 8b` | add x9,x8,x21 | `FALL_THROUGH`
<a id="insn-00bcbe78"></a> `00bcbe78` | `96 22 40 f9` | ldr x22,[x20, #0x40] | `FALL_THROUGH`
<a id="insn-00bcbe7c"></a> `00bcbe7c` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbe80"></a> `00bcbe80` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bcbe84"></a> `00bcbe84` | `49 01 00 54` | b.ls 0x00bcbeac | `CONDITIONAL_JUMP`
<a id="insn-00bcbe88"></a> `00bcbe88` | `48 f9 7f d3` | lsl x8,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbe8c"></a> `00bcbe8c` | `29 81 0f 91` | add x9,x9,#0x3e0 | `FALL_THROUGH`
<a id="insn-00bcbe90"></a> `00bcbe90` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcbe94"></a> `00bcbe94` | `01 81 89 9a` | csel x1,x8,x9,hi | `FALL_THROUGH`
<a id="insn-00bcbe98"></a> `00bcbe98` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbe9c"></a> `00bcbe9c` | `ad 44 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbea0"></a> `00bcbea0` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbea4"></a> `00bcbea4` | `a0 04 00 b4` | cbz x0,0x00bcbf38 | `CONDITIONAL_JUMP`
<a id="insn-00bcbea8"></a> `00bcbea8` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbeac"></a> `00bcbeac` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00bcbeb0"></a> `00bcbeb0` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcbeb4"></a> `00bcbeb4` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bcbeb8"></a> `00bcbeb8` | `7e 3c 00 94` | bl 0x00bdb0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbebc"></a> `00bcbebc` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbec0"></a> `00bcbec0` | `08 01 15 8b` | add x8,x8,x21 | `FALL_THROUGH`
<a id="insn-00bcbec4"></a> `00bcbec4` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbec8"></a> `00bcbec8` | `69 0a 40 f9` | ldr x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbecc"></a> `00bcbecc` | `0a 05 00 91` | add x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbed0"></a> `00bcbed0` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbed4"></a> `00bcbed4` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcbed8"></a> `00bcbed8` | `49 01 00 54` | b.ls 0x00bcbf00 | `CONDITIONAL_JUMP`
<a id="insn-00bcbedc"></a> `00bcbedc` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbee0"></a> `00bcbee0` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bcbee4"></a> `00bcbee4` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcbee8"></a> `00bcbee8` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcbeec"></a> `00bcbeec` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbef0"></a> `00bcbef0` | `98 44 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbef4"></a> `00bcbef4` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbef8"></a> `00bcbef8` | `e0 01 00 b4` | cbz x0,0x00bcbf34 | `CONDITIONAL_JUMP`
<a id="insn-00bcbefc"></a> `00bcbefc` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbf00"></a> `00bcbf00` | `e9 04 80 52` | mov w9,#0x27 | `FALL_THROUGH`
<a id="insn-00bcbf04"></a> `00bcbf04` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bcbf08"></a> `00bcbf08` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcbf0c"></a> `00bcbf0c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbf10"></a> `00bcbf10` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcbf14"></a> `00bcbf14` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbf18"></a> `00bcbf18` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbf1c"></a> `00bcbf1c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbf20"></a> `00bcbf20` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbf24"></a> `00bcbf24` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcbf28"></a> `00bcbf28` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcbf2c"></a> `00bcbf2c` | `06 00 00 14` | b 0x00bcbf44 | `CALL_TERMINATOR`
<a id="insn-00bcbf30"></a> `00bcbf30` | `a4 48 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`
<a id="insn-00bcbf34"></a> `00bcbf34` | `a3 48 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`
<a id="insn-00bcbf38"></a> `00bcbf38` | `a2 48 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbde4`](#insn-00bcbde4) 範囲 `[['00bcbde4', '00bcbe03']]`
  - `FALL_THROUGH` [`00bcbe00`](#insn-00bcbe00) → [`00bcbe04`](#insn-00bcbe04)
- ブロック [`00bcbe04`](#insn-00bcbe04) 範囲 `[['00bcbe04', '00bcbe13']]`
  - `CONDITIONAL_JUMP` [`00bcbe10`](#insn-00bcbe10) → [`00bcbe40`](#insn-00bcbe40)
  - `FALL_THROUGH` [`00bcbe10`](#insn-00bcbe10) → [`00bcbe14`](#insn-00bcbe14)
- ブロック [`00bcbe14`](#insn-00bcbe14) 範囲 `[['00bcbe14', '00bcbe37']]`
  - `CONDITIONAL_JUMP` [`00bcbe34`](#insn-00bcbe34) → [`00bcbf30`](#insn-00bcbf30)
  - `FALL_THROUGH` [`00bcbe34`](#insn-00bcbe34) → [`00bcbe38`](#insn-00bcbe38)
- ブロック [`00bcbe38`](#insn-00bcbe38) 範囲 `[['00bcbe38', '00bcbe3f']]`
  - `FALL_THROUGH` [`00bcbe3c`](#insn-00bcbe3c) → [`00bcbe40`](#insn-00bcbe40)
- ブロック [`00bcbe40`](#insn-00bcbe40) 範囲 `[['00bcbe40', '00bcbe67']]`
  - `FALL_THROUGH` [`00bcbe64`](#insn-00bcbe64) → [`00bcbe68`](#insn-00bcbe68)
- ブロック [`00bcbe68`](#insn-00bcbe68) 範囲 `[['00bcbe68', '00bcbe6f']]`
  - `CONDITIONAL_JUMP` [`00bcbe6c`](#insn-00bcbe6c) → [`00bcbec8`](#insn-00bcbec8)
  - `FALL_THROUGH` [`00bcbe6c`](#insn-00bcbe6c) → [`00bcbe70`](#insn-00bcbe70)
- ブロック [`00bcbe70`](#insn-00bcbe70) 範囲 `[['00bcbe70', '00bcbe77']]`
  - `FALL_THROUGH` [`00bcbe74`](#insn-00bcbe74) → [`00bcbe78`](#insn-00bcbe78)
- ブロック [`00bcbe78`](#insn-00bcbe78) 範囲 `[['00bcbe78', '00bcbe87']]`
  - `CONDITIONAL_JUMP` [`00bcbe84`](#insn-00bcbe84) → [`00bcbeac`](#insn-00bcbeac)
  - `FALL_THROUGH` [`00bcbe84`](#insn-00bcbe84) → [`00bcbe88`](#insn-00bcbe88)
- ブロック [`00bcbe88`](#insn-00bcbe88) 範囲 `[['00bcbe88', '00bcbea7']]`
  - `CONDITIONAL_JUMP` [`00bcbea4`](#insn-00bcbea4) → [`00bcbf38`](#insn-00bcbf38)
  - `FALL_THROUGH` [`00bcbea4`](#insn-00bcbea4) → [`00bcbea8`](#insn-00bcbea8)
- ブロック [`00bcbea8`](#insn-00bcbea8) 範囲 `[['00bcbea8', '00bcbeab']]`
  - `FALL_THROUGH` [`00bcbea8`](#insn-00bcbea8) → [`00bcbeac`](#insn-00bcbeac)
- ブロック [`00bcbeac`](#insn-00bcbeac) 範囲 `[['00bcbeac', '00bcbec7']]`
  - `FALL_THROUGH` [`00bcbec4`](#insn-00bcbec4) → [`00bcbec8`](#insn-00bcbec8)
- ブロック [`00bcbec8`](#insn-00bcbec8) 範囲 `[['00bcbec8', '00bcbedb']]`
  - `CONDITIONAL_JUMP` [`00bcbed8`](#insn-00bcbed8) → [`00bcbf00`](#insn-00bcbf00)
  - `FALL_THROUGH` [`00bcbed8`](#insn-00bcbed8) → [`00bcbedc`](#insn-00bcbedc)
- ブロック [`00bcbedc`](#insn-00bcbedc) 範囲 `[['00bcbedc', '00bcbefb']]`
  - `CONDITIONAL_JUMP` [`00bcbef8`](#insn-00bcbef8) → [`00bcbf34`](#insn-00bcbf34)
  - `FALL_THROUGH` [`00bcbef8`](#insn-00bcbef8) → [`00bcbefc`](#insn-00bcbefc)
- ブロック [`00bcbefc`](#insn-00bcbefc) 範囲 `[['00bcbefc', '00bcbeff']]`
  - `FALL_THROUGH` [`00bcbefc`](#insn-00bcbefc) → [`00bcbf00`](#insn-00bcbf00)
- ブロック [`00bcbf00`](#insn-00bcbf00) 範囲 `[['00bcbf00', '00bcbf2f']]`
- ブロック [`00bcbf30`](#insn-00bcbf30) 範囲 `[['00bcbf30', '00bcbf33']]`
- ブロック [`00bcbf34`](#insn-00bcbf34) 範囲 `[['00bcbf34', '00bcbf37']]`
- ブロック [`00bcbf38`](#insn-00bcbf38) 範囲 `[['00bcbf38', '00bcbf3b']]`

## 命令位置別の参照

- [`00bcbde8`](#insn-00bcbde8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbdec`](#insn-00bcbdec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbdf0`](#insn-00bcbdf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbe10`](#insn-00bcbe10) → [`00bcbe40`](#insn-00bcbe40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbe2c`](#insn-00bcbe2c) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bcbe34`](#insn-00bcbe34) → [`00bcbf30`](#insn-00bcbf30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbe6c`](#insn-00bcbe6c) → [`00bcbec8`](#insn-00bcbec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbe84`](#insn-00bcbe84) → [`00bcbeac`](#insn-00bcbeac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbe9c`](#insn-00bcbe9c) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bcbea4`](#insn-00bcbea4) → [`00bcbf38`](#insn-00bcbf38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbeb8`](#insn-00bcbeb8) → [`00bdb0b0`](../00bdb/00bdb0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbed8`](#insn-00bcbed8) → [`00bcbf00`](#insn-00bcbf00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbef0`](#insn-00bcbef0) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bcbef8`](#insn-00bcbef8) → [`00bcbf34`](#insn-00bcbf34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf1c`](#insn-00bcbf1c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf20`](#insn-00bcbf20) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf24`](#insn-00bcbf24) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf2c`](#insn-00bcbf2c) → [`00bcbf44`](00bcbf44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bcbf44` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf30`](#insn-00bcbf30) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf34`](#insn-00bcbf34) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf38`](#insn-00bcbf38) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbde8`](#insn-00bcbde8)

~~~json
{
  "source": "00bcbde8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbdec`](#insn-00bcbdec)

~~~json
{
  "source": "00bcbdec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbdf0`](#insn-00bcbdf0)

~~~json
{
  "source": "00bcbdf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbe10`](#insn-00bcbe10)

~~~json
{
  "source": "00bcbe10",
  "target": "00bcbe40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbe2c`](#insn-00bcbe2c)

~~~json
{
  "source": "00bcbe2c",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbe34`](#insn-00bcbe34)

~~~json
{
  "source": "00bcbe34",
  "target": "00bcbf30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbe6c`](#insn-00bcbe6c)

~~~json
{
  "source": "00bcbe6c",
  "target": "00bcbec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbe84`](#insn-00bcbe84)

~~~json
{
  "source": "00bcbe84",
  "target": "00bcbeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbe9c`](#insn-00bcbe9c)

~~~json
{
  "source": "00bcbe9c",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbea4`](#insn-00bcbea4)

~~~json
{
  "source": "00bcbea4",
  "target": "00bcbf38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbeb8`](#insn-00bcbeb8)

~~~json
{
  "source": "00bcbeb8",
  "target": "00bdb0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbed8`](#insn-00bcbed8)

~~~json
{
  "source": "00bcbed8",
  "target": "00bcbf00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbef0`](#insn-00bcbef0)

~~~json
{
  "source": "00bcbef0",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbef8`](#insn-00bcbef8)

~~~json
{
  "source": "00bcbef8",
  "target": "00bcbf34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf1c`](#insn-00bcbf1c)

~~~json
{
  "source": "00bcbf1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf20`](#insn-00bcbf20)

~~~json
{
  "source": "00bcbf20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf24`](#insn-00bcbf24)

~~~json
{
  "source": "00bcbf24",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf2c`](#insn-00bcbf2c)

~~~json
{
  "source": "00bcbf2c",
  "target": "00bcbf44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbf30`](#insn-00bcbf30)

~~~json
{
  "source": "00bcbf30",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbf34`](#insn-00bcbf34)

~~~json
{
  "source": "00bcbf34",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbf38`](#insn-00bcbf38)

~~~json
{
  "source": "00bcbf38",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
