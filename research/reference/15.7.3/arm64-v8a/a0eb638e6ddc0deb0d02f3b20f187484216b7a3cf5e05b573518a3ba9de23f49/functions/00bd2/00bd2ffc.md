# 00bd2ffc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bd2f34`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2f34.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0007.md#compare-7bdbb218fe28d24bd190fd8c7e717a71)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bd3040`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3040.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0019.md#compare-a47ba5820744877a766457e4f6abf0d6)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd2ffc",
  "name": "FUN_00bd2ffc",
  "size": 364,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6c6806a025b03dfeeba65f8c1f77cb16923fcb14c824c4cb2ab5ccffd32598b4",
  "source_text_sha256": "6c6806a025b03dfeeba65f8c1f77cb16923fcb14c824c4cb2ab5ccffd32598b4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd2ffc",
        "00bd3167"
      ]
    ],
    "bytes_sha256": "6e5d7c969dec33fad512981cda4475489a678451ad195d80e4af72c0bb6b11b6",
    "instruction_count": 91,
    "instruction_bytes": 364,
    "body_bytes": 364,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb160](../00bdb/00bdb160.md)
- [00bdd200](../00bdd/00bdd200.md)
- [00bde270](../00bde/00bde270.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2178 bytes

~~~c

void FUN_00bd2ffc(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  void *pvVar2;
  long lVar3;
  size_t __size;
  size_t sVar4;
  long *plVar5;
  void *__src;
  
  plVar5 = *(long **)(param_1 + 0x10);
  (**(code **)(*plVar5 + 0x20))(plVar5);
  if ((*(ushort *)((long)plVar5 + 9) & 0xc0) != 0x40) {
    (**(code **)(*plVar5 + 0x28))(plVar5,param_2);
  }
  lVar3 = param_2[1];
  pvVar2 = (void *)*param_2;
  if ((ulong)param_2[2] < lVar3 + 1U) {
    sVar4 = param_2[2] * 2;
    uVar1 = lVar3 + 0x3e1;
    if (sVar4 < uVar1 || sVar4 - uVar1 == 0) {
      sVar4 = uVar1;
    }
    param_2[2] = sVar4;
                    /* try { // try from 00bd3078 to 00cd322b has its CatchHandler @ 00bd2e9c */
    pvVar2 = realloc(pvVar2,sVar4);
    *param_2 = pvVar2;
    if (pvVar2 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar3 = param_2[1];
  }
  *(undefined1 *)((long)pvVar2 + lVar3) = 0x20;
  lVar3 = param_2[1] + 1;
  param_2[1] = lVar3;
  sVar4 = *(size_t *)(param_1 + 0x20);
  if (sVar4 != 0) {
    __src = *(void **)(param_1 + 0x18);
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
    param_2[1] = param_2[1] + sVar4;
  }
  plVar5 = *(long **)(param_1 + 0x28);
  if ((plVar5 != (long *)0x0) &&
     ((**(code **)(*plVar5 + 0x20))(plVar5,param_2), (*(ushort *)((long)plVar5 + 9) & 0xc0) != 0x40)
     ) {
                    /* WARNING: Could not recover jumptable at 0x00bd315c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
                    /* catch() { ... } // from try @ 00bd2ff0 with catch @ 00bd315c */
    (**(code **)(*plVar5 + 0x28))(plVar5,param_2);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd2ffc"></a> `00bd2ffc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bd3000"></a> `00bd3000` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bd3004"></a> `00bd3004` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd3008"></a> `00bd3008` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd300c"></a> `00bd300c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bd3010"></a> `00bd3010` | `15 08 40 f9` | ldr x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bd3014"></a> `00bd3014` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bd3018"></a> `00bd3018` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bd301c"></a> `00bd301c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bd3020"></a> `00bd3020` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bd3024"></a> `00bd3024` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bd3028"></a> `00bd3028` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd302c"></a> `00bd302c` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bd3030"></a> `00bd3030` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bd3034"></a> `00bd3034` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bd3038"></a> `00bd3038` | `c0 00 00 54` | b.eq 0x00bd3050 | `CONDITIONAL_JUMP`
<a id="insn-00bd303c"></a> `00bd303c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bd3040"></a> `00bd3040` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bd3044"></a> `00bd3044` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bd3048"></a> `00bd3048` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bd304c"></a> `00bd304c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd3050"></a> `00bd3050` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd3054"></a> `00bd3054` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd3058"></a> `00bd3058` | `0a 05 00 91` | add x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bd305c"></a> `00bd305c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bd3060"></a> `00bd3060` | `49 01 00 54` | b.ls 0x00bd3088 | `CONDITIONAL_JUMP`
<a id="insn-00bd3064"></a> `00bd3064` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bd3068"></a> `00bd3068` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bd306c"></a> `00bd306c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bd3070"></a> `00bd3070` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bd3074"></a> `00bd3074` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bd3078"></a> `00bd3078` | `62 28 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bd307c"></a> `00bd307c` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd3080"></a> `00bd3080` | `00 07 00 b4` | cbz x0,0x00bd3160 | `CONDITIONAL_JUMP`
<a id="insn-00bd3084"></a> `00bd3084` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd3088"></a> `00bd3088` | `09 04 80 52` | mov w9,#0x20 | `FALL_THROUGH`
<a id="insn-00bd308c"></a> `00bd308c` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bd3090"></a> `00bd3090` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd3094"></a> `00bd3094` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bd3098"></a> `00bd3098` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd309c"></a> `00bd309c` | `95 12 40 f9` | ldr x21,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00bd30a0"></a> `00bd30a0` | `f5 02 00 b4` | cbz x21,0x00bd30fc | `CONDITIONAL_JUMP`
<a id="insn-00bd30a4"></a> `00bd30a4` | `6a 0a 40 f9` | ldr x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bd30a8"></a> `00bd30a8` | `09 01 15 8b` | add x9,x8,x21 | `FALL_THROUGH`
<a id="insn-00bd30ac"></a> `00bd30ac` | `96 0e 40 f9` | ldr x22,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00bd30b0"></a> `00bd30b0` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd30b4"></a> `00bd30b4` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bd30b8"></a> `00bd30b8` | `49 01 00 54` | b.ls 0x00bd30e0 | `CONDITIONAL_JUMP`
<a id="insn-00bd30bc"></a> `00bd30bc` | `48 f9 7f d3` | lsl x8,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bd30c0"></a> `00bd30c0` | `29 81 0f 91` | add x9,x9,#0x3e0 | `FALL_THROUGH`
<a id="insn-00bd30c4"></a> `00bd30c4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bd30c8"></a> `00bd30c8` | `01 81 89 9a` | csel x1,x8,x9,hi | `FALL_THROUGH`
<a id="insn-00bd30cc"></a> `00bd30cc` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bd30d0"></a> `00bd30d0` | `4c 28 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bd30d4"></a> `00bd30d4` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd30d8"></a> `00bd30d8` | `60 04 00 b4` | cbz x0,0x00bd3164 | `CONDITIONAL_JUMP`
<a id="insn-00bd30dc"></a> `00bd30dc` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd30e0"></a> `00bd30e0` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00bd30e4"></a> `00bd30e4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bd30e8"></a> `00bd30e8` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bd30ec"></a> `00bd30ec` | `1d 20 00 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-00bd30f0"></a> `00bd30f0` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd30f4"></a> `00bd30f4` | `08 01 15 8b` | add x8,x8,x21 | `FALL_THROUGH`
<a id="insn-00bd30f8"></a> `00bd30f8` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd30fc"></a> `00bd30fc` | `94 16 40 f9` | ldr x20,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bd3100"></a> `00bd3100` | `54 01 00 b4` | cbz x20,0x00bd3128 | `CONDITIONAL_JUMP`
<a id="insn-00bd3104"></a> `00bd3104` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bd3108"></a> `00bd3108` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bd310c"></a> `00bd310c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bd3110"></a> `00bd3110` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bd3114"></a> `00bd3114` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd3118"></a> `00bd3118` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bd311c"></a> `00bd311c` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bd3120"></a> `00bd3120` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bd3124"></a> `00bd3124` | `c1 00 00 54` | b.ne 0x00bd313c | `CONDITIONAL_JUMP`
<a id="insn-00bd3128"></a> `00bd3128` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd312c"></a> `00bd312c` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd3130"></a> `00bd3130` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bd3134"></a> `00bd3134` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bd3138"></a> `00bd3138` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bd313c"></a> `00bd313c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bd3140"></a> `00bd3140` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bd3144"></a> `00bd3144` | `10 15 40 f9` | ldr x16,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bd3148"></a> `00bd3148` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bd314c"></a> `00bd314c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd3150"></a> `00bd3150` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd3154"></a> `00bd3154` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bd3158"></a> `00bd3158` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bd315c"></a> `00bd315c` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00bd3160"></a> `00bd3160` | `44 2c 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bd3164"></a> `00bd3164` | `43 2c 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd2ffc`](#insn-00bd2ffc) 範囲 `[['00bd2ffc', '00bd303b']]`
  - `CONDITIONAL_JUMP` [`00bd3038`](#insn-00bd3038) → [`00bd3050`](#insn-00bd3050)
  - `FALL_THROUGH` [`00bd3038`](#insn-00bd3038) → [`00bd303c`](#insn-00bd303c)
- ブロック [`00bd303c`](#insn-00bd303c) 範囲 `[['00bd303c', '00bd304f']]`
  - `FALL_THROUGH` [`00bd304c`](#insn-00bd304c) → [`00bd3050`](#insn-00bd3050)
- ブロック [`00bd3050`](#insn-00bd3050) 範囲 `[['00bd3050', '00bd3063']]`
  - `CONDITIONAL_JUMP` [`00bd3060`](#insn-00bd3060) → [`00bd3088`](#insn-00bd3088)
  - `FALL_THROUGH` [`00bd3060`](#insn-00bd3060) → [`00bd3064`](#insn-00bd3064)
- ブロック [`00bd3064`](#insn-00bd3064) 範囲 `[['00bd3064', '00bd3077']]`
  - `FALL_THROUGH` [`00bd3074`](#insn-00bd3074) → [`00bd3078`](#insn-00bd3078)
- ブロック [`00bd3078`](#insn-00bd3078) 範囲 `[['00bd3078', '00bd3083']]`
  - `CONDITIONAL_JUMP` [`00bd3080`](#insn-00bd3080) → [`00bd3160`](#insn-00bd3160)
  - `FALL_THROUGH` [`00bd3080`](#insn-00bd3080) → [`00bd3084`](#insn-00bd3084)
- ブロック [`00bd3084`](#insn-00bd3084) 範囲 `[['00bd3084', '00bd3087']]`
  - `FALL_THROUGH` [`00bd3084`](#insn-00bd3084) → [`00bd3088`](#insn-00bd3088)
- ブロック [`00bd3088`](#insn-00bd3088) 範囲 `[['00bd3088', '00bd30a3']]`
  - `CONDITIONAL_JUMP` [`00bd30a0`](#insn-00bd30a0) → [`00bd30fc`](#insn-00bd30fc)
  - `FALL_THROUGH` [`00bd30a0`](#insn-00bd30a0) → [`00bd30a4`](#insn-00bd30a4)
- ブロック [`00bd30a4`](#insn-00bd30a4) 範囲 `[['00bd30a4', '00bd30bb']]`
  - `CONDITIONAL_JUMP` [`00bd30b8`](#insn-00bd30b8) → [`00bd30e0`](#insn-00bd30e0)
  - `FALL_THROUGH` [`00bd30b8`](#insn-00bd30b8) → [`00bd30bc`](#insn-00bd30bc)
- ブロック [`00bd30bc`](#insn-00bd30bc) 範囲 `[['00bd30bc', '00bd30db']]`
  - `CONDITIONAL_JUMP` [`00bd30d8`](#insn-00bd30d8) → [`00bd3164`](#insn-00bd3164)
  - `FALL_THROUGH` [`00bd30d8`](#insn-00bd30d8) → [`00bd30dc`](#insn-00bd30dc)
- ブロック [`00bd30dc`](#insn-00bd30dc) 範囲 `[['00bd30dc', '00bd30df']]`
  - `FALL_THROUGH` [`00bd30dc`](#insn-00bd30dc) → [`00bd30e0`](#insn-00bd30e0)
- ブロック [`00bd30e0`](#insn-00bd30e0) 範囲 `[['00bd30e0', '00bd30fb']]`
  - `FALL_THROUGH` [`00bd30f8`](#insn-00bd30f8) → [`00bd30fc`](#insn-00bd30fc)
- ブロック [`00bd30fc`](#insn-00bd30fc) 範囲 `[['00bd30fc', '00bd3103']]`
  - `CONDITIONAL_JUMP` [`00bd3100`](#insn-00bd3100) → [`00bd3128`](#insn-00bd3128)
  - `FALL_THROUGH` [`00bd3100`](#insn-00bd3100) → [`00bd3104`](#insn-00bd3104)
- ブロック [`00bd3104`](#insn-00bd3104) 範囲 `[['00bd3104', '00bd3127']]`
  - `CONDITIONAL_JUMP` [`00bd3124`](#insn-00bd3124) → [`00bd313c`](#insn-00bd313c)
  - `FALL_THROUGH` [`00bd3124`](#insn-00bd3124) → [`00bd3128`](#insn-00bd3128)
- ブロック [`00bd3128`](#insn-00bd3128) 範囲 `[['00bd3128', '00bd313b']]`
- ブロック [`00bd313c`](#insn-00bd313c) 範囲 `[['00bd313c', '00bd315b']]`
  - `FALL_THROUGH` [`00bd3158`](#insn-00bd3158) → [`00bd315c`](#insn-00bd315c)
- ブロック [`00bd315c`](#insn-00bd315c) 範囲 `[['00bd315c', '00bd315f']]`
- ブロック [`00bd3160`](#insn-00bd3160) 範囲 `[['00bd3160', '00bd3163']]`
- ブロック [`00bd3164`](#insn-00bd3164) 範囲 `[['00bd3164', '00bd3167']]`

## 命令位置別の参照

- [`00bd3000`](#insn-00bd3000) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3004`](#insn-00bd3004) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3008`](#insn-00bd3008) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3038`](#insn-00bd3038) → [`00bd3050`](#insn-00bd3050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3060`](#insn-00bd3060) → [`00bd3088`](#insn-00bd3088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3078`](#insn-00bd3078) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bd3080`](#insn-00bd3080) → [`00bd3160`](#insn-00bd3160) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd30a0`](#insn-00bd30a0) → [`00bd30fc`](#insn-00bd30fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd30b8`](#insn-00bd30b8) → [`00bd30e0`](#insn-00bd30e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd30d0`](#insn-00bd30d0) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bd30d8`](#insn-00bd30d8) → [`00bd3164`](#insn-00bd3164) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd30ec`](#insn-00bd30ec) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`00bd3100`](#insn-00bd3100) → [`00bd3128`](#insn-00bd3128) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3124`](#insn-00bd3124) → [`00bd313c`](#insn-00bd313c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3128`](#insn-00bd3128) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd312c`](#insn-00bd312c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3130`](#insn-00bd3130) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd314c`](#insn-00bd314c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3150`](#insn-00bd3150) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3154`](#insn-00bd3154) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3160`](#insn-00bd3160) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bd3164`](#insn-00bd3164) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd3000`](#insn-00bd3000)

~~~json
{
  "source": "00bd3000",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3004`](#insn-00bd3004)

~~~json
{
  "source": "00bd3004",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3008`](#insn-00bd3008)

~~~json
{
  "source": "00bd3008",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3038`](#insn-00bd3038)

~~~json
{
  "source": "00bd3038",
  "target": "00bd3050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3060`](#insn-00bd3060)

~~~json
{
  "source": "00bd3060",
  "target": "00bd3088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3078`](#insn-00bd3078)

~~~json
{
  "source": "00bd3078",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd3080`](#insn-00bd3080)

~~~json
{
  "source": "00bd3080",
  "target": "00bd3160",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd30a0`](#insn-00bd30a0)

~~~json
{
  "source": "00bd30a0",
  "target": "00bd30fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd30b8`](#insn-00bd30b8)

~~~json
{
  "source": "00bd30b8",
  "target": "00bd30e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd30d0`](#insn-00bd30d0)

~~~json
{
  "source": "00bd30d0",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd30d8`](#insn-00bd30d8)

~~~json
{
  "source": "00bd30d8",
  "target": "00bd3164",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd30ec`](#insn-00bd30ec)

~~~json
{
  "source": "00bd30ec",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd3100`](#insn-00bd3100)

~~~json
{
  "source": "00bd3100",
  "target": "00bd3128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3124`](#insn-00bd3124)

~~~json
{
  "source": "00bd3124",
  "target": "00bd313c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3128`](#insn-00bd3128)

~~~json
{
  "source": "00bd3128",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd312c`](#insn-00bd312c)

~~~json
{
  "source": "00bd312c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3130`](#insn-00bd3130)

~~~json
{
  "source": "00bd3130",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd314c`](#insn-00bd314c)

~~~json
{
  "source": "00bd314c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3150`](#insn-00bd3150)

~~~json
{
  "source": "00bd3150",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3154`](#insn-00bd3154)

~~~json
{
  "source": "00bd3154",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3160`](#insn-00bd3160)

~~~json
{
  "source": "00bd3160",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd3164`](#insn-00bd3164)

~~~json
{
  "source": "00bd3164",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
