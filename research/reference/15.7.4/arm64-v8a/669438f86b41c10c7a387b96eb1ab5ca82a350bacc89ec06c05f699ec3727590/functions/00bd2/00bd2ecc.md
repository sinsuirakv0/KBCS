# 00bd2ecc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bd2e88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2e88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0019.md#compare-81b2dd3bcd63a4d3f8122cc803183d1a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c4f914`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f914.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0078.md#compare-5bcdf055f5f72e7c77298582f3b4b216)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd2ecc",
  "name": "FUN_00bd2ecc",
  "size": 364,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "afa4c995a754e5b60027253beab1fa629dceb2ae398aa8e0ffb1592709ed4134",
  "source_text_sha256": "afa4c995a754e5b60027253beab1fa629dceb2ae398aa8e0ffb1592709ed4134",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd2ecc",
        "00bd3037"
      ]
    ],
    "bytes_sha256": "a0b8f72a6ac1ec6f5b77f99e2ea73f150cfebd1a93406b690273fa3e63948229",
    "instruction_count": 91,
    "instruction_bytes": 364,
    "body_bytes": 364,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb1b0](../00bdb/00bdb1b0.md)
- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2290 bytes

~~~c

void FUN_00bd2ecc(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  void *pvVar2;
  long lVar3;
  size_t __size;
  size_t sVar4;
  void *__src;
  long *plVar5;
  
                    /* catch() { ... } // from try @ 00bd30bc with catch @ 00bd2ee0 */
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
    pvVar2 = realloc(pvVar2,sVar4);
    *param_2 = pvVar2;
    if (pvVar2 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar3 = param_2[1];
  }
  *(undefined1 *)((long)pvVar2 + lVar3) = 0x3c;
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
                    /* try { // try from 00bd3034 to 00cd30bb has its CatchHandler @ 00bd31a0 */
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
  *(undefined1 *)((long)pvVar2 + lVar3) = 0x3e;
  param_2[1] = param_2[1] + 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd2ecc"></a> `00bd2ecc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bd2ed0"></a> `00bd2ed0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bd2ed4"></a> `00bd2ed4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2ed8"></a> `00bd2ed8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd2edc"></a> `00bd2edc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bd2ee0"></a> `00bd2ee0` | `15 08 40 f9` | ldr x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2ee4"></a> `00bd2ee4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bd2ee8"></a> `00bd2ee8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bd2eec"></a> `00bd2eec` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bd2ef0"></a> `00bd2ef0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bd2ef4"></a> `00bd2ef4` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bd2ef8"></a> `00bd2ef8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd2efc"></a> `00bd2efc` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bd2f00"></a> `00bd2f00` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bd2f04"></a> `00bd2f04` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bd2f08"></a> `00bd2f08` | `c0 00 00 54` | b.eq 0x00bd2f20 | `CONDITIONAL_JUMP`
<a id="insn-00bd2f0c"></a> `00bd2f0c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bd2f10"></a> `00bd2f10` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bd2f14"></a> `00bd2f14` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bd2f18"></a> `00bd2f18` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bd2f1c"></a> `00bd2f1c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd2f20"></a> `00bd2f20` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2f24"></a> `00bd2f24` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd2f28"></a> `00bd2f28` | `0a 05 00 91` | add x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2f2c"></a> `00bd2f2c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bd2f30"></a> `00bd2f30` | `49 01 00 54` | b.ls 0x00bd2f58 | `CONDITIONAL_JUMP`
<a id="insn-00bd2f34"></a> `00bd2f34` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2f38"></a> `00bd2f38` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bd2f3c"></a> `00bd2f3c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bd2f40"></a> `00bd2f40` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bd2f44"></a> `00bd2f44` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2f48"></a> `00bd2f48` | `c2 28 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bd2f4c"></a> `00bd2f4c` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd2f50"></a> `00bd2f50` | `e0 06 00 b4` | cbz x0,0x00bd302c | `CONDITIONAL_JUMP`
<a id="insn-00bd2f54"></a> `00bd2f54` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2f58"></a> `00bd2f58` | `89 07 80 52` | mov w9,#0x3c | `FALL_THROUGH`
<a id="insn-00bd2f5c"></a> `00bd2f5c` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bd2f60"></a> `00bd2f60` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2f64"></a> `00bd2f64` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2f68"></a> `00bd2f68` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2f6c"></a> `00bd2f6c` | `95 12 40 f9` | ldr x21,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00bd2f70"></a> `00bd2f70` | `f5 02 00 b4` | cbz x21,0x00bd2fcc | `CONDITIONAL_JUMP`
<a id="insn-00bd2f74"></a> `00bd2f74` | `6a 0a 40 f9` | ldr x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2f78"></a> `00bd2f78` | `09 01 15 8b` | add x9,x8,x21 | `FALL_THROUGH`
<a id="insn-00bd2f7c"></a> `00bd2f7c` | `94 0e 40 f9` | ldr x20,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00bd2f80"></a> `00bd2f80` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd2f84"></a> `00bd2f84` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bd2f88"></a> `00bd2f88` | `49 01 00 54` | b.ls 0x00bd2fb0 | `CONDITIONAL_JUMP`
<a id="insn-00bd2f8c"></a> `00bd2f8c` | `48 f9 7f d3` | lsl x8,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2f90"></a> `00bd2f90` | `29 81 0f 91` | add x9,x9,#0x3e0 | `FALL_THROUGH`
<a id="insn-00bd2f94"></a> `00bd2f94` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bd2f98"></a> `00bd2f98` | `01 81 89 9a` | csel x1,x8,x9,hi | `FALL_THROUGH`
<a id="insn-00bd2f9c"></a> `00bd2f9c` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2fa0"></a> `00bd2fa0` | `ac 28 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bd2fa4"></a> `00bd2fa4` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd2fa8"></a> `00bd2fa8` | `60 04 00 b4` | cbz x0,0x00bd3034 | `CONDITIONAL_JUMP`
<a id="insn-00bd2fac"></a> `00bd2fac` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2fb0"></a> `00bd2fb0` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00bd2fb4"></a> `00bd2fb4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bd2fb8"></a> `00bd2fb8` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bd2fbc"></a> `00bd2fbc` | `7d 20 00 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd2fc0"></a> `00bd2fc0` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2fc4"></a> `00bd2fc4` | `08 01 15 8b` | add x8,x8,x21 | `FALL_THROUGH`
<a id="insn-00bd2fc8"></a> `00bd2fc8` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2fcc"></a> `00bd2fcc` | `69 0a 40 f9` | ldr x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2fd0"></a> `00bd2fd0` | `0a 05 00 91` | add x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2fd4"></a> `00bd2fd4` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd2fd8"></a> `00bd2fd8` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bd2fdc"></a> `00bd2fdc` | `49 01 00 54` | b.ls 0x00bd3004 | `CONDITIONAL_JUMP`
<a id="insn-00bd2fe0"></a> `00bd2fe0` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2fe4"></a> `00bd2fe4` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bd2fe8"></a> `00bd2fe8` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bd2fec"></a> `00bd2fec` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bd2ff0"></a> `00bd2ff0` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2ff4"></a> `00bd2ff4` | `97 28 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bd2ff8"></a> `00bd2ff8` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd2ffc"></a> `00bd2ffc` | `a0 01 00 b4` | cbz x0,0x00bd3030 | `CONDITIONAL_JUMP`
<a id="insn-00bd3000"></a> `00bd3000` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd3004"></a> `00bd3004` | `c9 07 80 52` | mov w9,#0x3e | `FALL_THROUGH`
<a id="insn-00bd3008"></a> `00bd3008` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bd300c"></a> `00bd300c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd3010"></a> `00bd3010` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bd3014"></a> `00bd3014` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd3018"></a> `00bd3018` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd301c"></a> `00bd301c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd3020"></a> `00bd3020` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bd3024"></a> `00bd3024` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bd3028"></a> `00bd3028` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bd302c"></a> `00bd302c` | `a5 2c 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`
<a id="insn-00bd3030"></a> `00bd3030` | `a4 2c 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`
<a id="insn-00bd3034"></a> `00bd3034` | `a3 2c 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd2ecc`](#insn-00bd2ecc) 範囲 `[['00bd2ecc', '00bd2edf']]`
  - `FALL_THROUGH` [`00bd2edc`](#insn-00bd2edc) → [`00bd2ee0`](#insn-00bd2ee0)
- ブロック [`00bd2ee0`](#insn-00bd2ee0) 範囲 `[['00bd2ee0', '00bd2f0b']]`
  - `CONDITIONAL_JUMP` [`00bd2f08`](#insn-00bd2f08) → [`00bd2f20`](#insn-00bd2f20)
  - `FALL_THROUGH` [`00bd2f08`](#insn-00bd2f08) → [`00bd2f0c`](#insn-00bd2f0c)
- ブロック [`00bd2f0c`](#insn-00bd2f0c) 範囲 `[['00bd2f0c', '00bd2f1f']]`
  - `FALL_THROUGH` [`00bd2f1c`](#insn-00bd2f1c) → [`00bd2f20`](#insn-00bd2f20)
- ブロック [`00bd2f20`](#insn-00bd2f20) 範囲 `[['00bd2f20', '00bd2f33']]`
  - `CONDITIONAL_JUMP` [`00bd2f30`](#insn-00bd2f30) → [`00bd2f58`](#insn-00bd2f58)
  - `FALL_THROUGH` [`00bd2f30`](#insn-00bd2f30) → [`00bd2f34`](#insn-00bd2f34)
- ブロック [`00bd2f34`](#insn-00bd2f34) 範囲 `[['00bd2f34', '00bd2f53']]`
  - `CONDITIONAL_JUMP` [`00bd2f50`](#insn-00bd2f50) → [`00bd302c`](#insn-00bd302c)
  - `FALL_THROUGH` [`00bd2f50`](#insn-00bd2f50) → [`00bd2f54`](#insn-00bd2f54)
- ブロック [`00bd2f54`](#insn-00bd2f54) 範囲 `[['00bd2f54', '00bd2f57']]`
  - `FALL_THROUGH` [`00bd2f54`](#insn-00bd2f54) → [`00bd2f58`](#insn-00bd2f58)
- ブロック [`00bd2f58`](#insn-00bd2f58) 範囲 `[['00bd2f58', '00bd2f73']]`
  - `CONDITIONAL_JUMP` [`00bd2f70`](#insn-00bd2f70) → [`00bd2fcc`](#insn-00bd2fcc)
  - `FALL_THROUGH` [`00bd2f70`](#insn-00bd2f70) → [`00bd2f74`](#insn-00bd2f74)
- ブロック [`00bd2f74`](#insn-00bd2f74) 範囲 `[['00bd2f74', '00bd2f8b']]`
  - `CONDITIONAL_JUMP` [`00bd2f88`](#insn-00bd2f88) → [`00bd2fb0`](#insn-00bd2fb0)
  - `FALL_THROUGH` [`00bd2f88`](#insn-00bd2f88) → [`00bd2f8c`](#insn-00bd2f8c)
- ブロック [`00bd2f8c`](#insn-00bd2f8c) 範囲 `[['00bd2f8c', '00bd2fab']]`
  - `CONDITIONAL_JUMP` [`00bd2fa8`](#insn-00bd2fa8) → [`00bd3034`](#insn-00bd3034)
  - `FALL_THROUGH` [`00bd2fa8`](#insn-00bd2fa8) → [`00bd2fac`](#insn-00bd2fac)
- ブロック [`00bd2fac`](#insn-00bd2fac) 範囲 `[['00bd2fac', '00bd2faf']]`
  - `FALL_THROUGH` [`00bd2fac`](#insn-00bd2fac) → [`00bd2fb0`](#insn-00bd2fb0)
- ブロック [`00bd2fb0`](#insn-00bd2fb0) 範囲 `[['00bd2fb0', '00bd2fcb']]`
  - `FALL_THROUGH` [`00bd2fc8`](#insn-00bd2fc8) → [`00bd2fcc`](#insn-00bd2fcc)
- ブロック [`00bd2fcc`](#insn-00bd2fcc) 範囲 `[['00bd2fcc', '00bd2fdf']]`
  - `CONDITIONAL_JUMP` [`00bd2fdc`](#insn-00bd2fdc) → [`00bd3004`](#insn-00bd3004)
  - `FALL_THROUGH` [`00bd2fdc`](#insn-00bd2fdc) → [`00bd2fe0`](#insn-00bd2fe0)
- ブロック [`00bd2fe0`](#insn-00bd2fe0) 範囲 `[['00bd2fe0', '00bd2fff']]`
  - `CONDITIONAL_JUMP` [`00bd2ffc`](#insn-00bd2ffc) → [`00bd3030`](#insn-00bd3030)
  - `FALL_THROUGH` [`00bd2ffc`](#insn-00bd2ffc) → [`00bd3000`](#insn-00bd3000)
- ブロック [`00bd3000`](#insn-00bd3000) 範囲 `[['00bd3000', '00bd3003']]`
  - `FALL_THROUGH` [`00bd3000`](#insn-00bd3000) → [`00bd3004`](#insn-00bd3004)
- ブロック [`00bd3004`](#insn-00bd3004) 範囲 `[['00bd3004', '00bd302b']]`
- ブロック [`00bd302c`](#insn-00bd302c) 範囲 `[['00bd302c', '00bd302f']]`
- ブロック [`00bd3030`](#insn-00bd3030) 範囲 `[['00bd3030', '00bd3033']]`
- ブロック [`00bd3034`](#insn-00bd3034) 範囲 `[['00bd3034', '00bd3037']]`

## 命令位置別の参照

- [`00bd2ed0`](#insn-00bd2ed0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2ed4`](#insn-00bd2ed4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2ed8`](#insn-00bd2ed8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2f08`](#insn-00bd2f08) → [`00bd2f20`](#insn-00bd2f20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2f30`](#insn-00bd2f30) → [`00bd2f58`](#insn-00bd2f58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2f48`](#insn-00bd2f48) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bd2f50`](#insn-00bd2f50) → [`00bd302c`](#insn-00bd302c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2f70`](#insn-00bd2f70) → [`00bd2fcc`](#insn-00bd2fcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2f88`](#insn-00bd2f88) → [`00bd2fb0`](#insn-00bd2fb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2fa0`](#insn-00bd2fa0) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bd2fa8`](#insn-00bd2fa8) → [`00bd3034`](#insn-00bd3034) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2fbc`](#insn-00bd2fbc) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00bd2fdc`](#insn-00bd2fdc) → [`00bd3004`](#insn-00bd3004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2ff4`](#insn-00bd2ff4) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bd2ffc`](#insn-00bd2ffc) → [`00bd3030`](#insn-00bd3030) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3018`](#insn-00bd3018) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd301c`](#insn-00bd301c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3020`](#insn-00bd3020) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd302c`](#insn-00bd302c) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`
- [`00bd3030`](#insn-00bd3030) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`
- [`00bd3034`](#insn-00bd3034) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd2ed0`](#insn-00bd2ed0)

~~~json
{
  "source": "00bd2ed0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2ed4`](#insn-00bd2ed4)

~~~json
{
  "source": "00bd2ed4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2ed8`](#insn-00bd2ed8)

~~~json
{
  "source": "00bd2ed8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2f08`](#insn-00bd2f08)

~~~json
{
  "source": "00bd2f08",
  "target": "00bd2f20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2f30`](#insn-00bd2f30)

~~~json
{
  "source": "00bd2f30",
  "target": "00bd2f58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2f48`](#insn-00bd2f48)

~~~json
{
  "source": "00bd2f48",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2f50`](#insn-00bd2f50)

~~~json
{
  "source": "00bd2f50",
  "target": "00bd302c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2f70`](#insn-00bd2f70)

~~~json
{
  "source": "00bd2f70",
  "target": "00bd2fcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2f88`](#insn-00bd2f88)

~~~json
{
  "source": "00bd2f88",
  "target": "00bd2fb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2fa0`](#insn-00bd2fa0)

~~~json
{
  "source": "00bd2fa0",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2fa8`](#insn-00bd2fa8)

~~~json
{
  "source": "00bd2fa8",
  "target": "00bd3034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2fbc`](#insn-00bd2fbc)

~~~json
{
  "source": "00bd2fbc",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2fdc`](#insn-00bd2fdc)

~~~json
{
  "source": "00bd2fdc",
  "target": "00bd3004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2ff4`](#insn-00bd2ff4)

~~~json
{
  "source": "00bd2ff4",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2ffc`](#insn-00bd2ffc)

~~~json
{
  "source": "00bd2ffc",
  "target": "00bd3030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3018`](#insn-00bd3018)

~~~json
{
  "source": "00bd3018",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd301c`](#insn-00bd301c)

~~~json
{
  "source": "00bd301c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3020`](#insn-00bd3020)

~~~json
{
  "source": "00bd3020",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd302c`](#insn-00bd302c)

~~~json
{
  "source": "00bd302c",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd3030`](#insn-00bd3030)

~~~json
{
  "source": "00bd3030",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd3034`](#insn-00bd3034)

~~~json
{
  "source": "00bd3034",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
