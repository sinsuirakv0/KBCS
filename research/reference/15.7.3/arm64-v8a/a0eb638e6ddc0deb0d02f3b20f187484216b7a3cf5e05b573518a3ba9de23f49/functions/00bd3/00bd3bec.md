# 00bd3bec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bd3b24`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3b24.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0007.md#compare-5e29bd588ba4a312aac33ae8a60b04d3)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bd3c30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3c30.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0019.md#compare-5162b3cde52cf9f6b37ae469f4ddf10c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd3bec",
  "name": "FUN_00bd3bec",
  "size": 340,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7ab5e8dec4bd232e662c2b5eb346aee3aa3d2314944080f5cb844bfad6054110",
  "source_text_sha256": "7ab5e8dec4bd232e662c2b5eb346aee3aa3d2314944080f5cb844bfad6054110",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd3bec",
        "00bd3d3f"
      ]
    ],
    "bytes_sha256": "0d800e9b639f970a414e31110d8d0bec278678ebdd1d7a22c0ac6699330c94d2",
    "instruction_count": 85,
    "instruction_bytes": 340,
    "body_bytes": 340,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdd200](../00bdd/00bdd200.md)
- [00bde270](../00bde/00bde270.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2030 bytes

~~~c

void FUN_00bd3bec(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  void *pvVar2;
  long lVar3;
  size_t sVar4;
  long *plVar5;
  
  plVar5 = *(long **)(param_1 + 0x10);
  (**(code **)(*plVar5 + 0x20))(plVar5);
  if ((*(ushort *)((long)plVar5 + 9) & 0xc0) != 0x40) {
    (**(code **)(*plVar5 + 0x28))(plVar5,param_2);
  }
  lVar3 = param_2[1];
                    /* try { // try from 00bd3c44 to 00cd3c4b has its CatchHandler @ 00bd3e24 */
  pvVar2 = (void *)*param_2;
  if ((ulong)param_2[2] < lVar3 + 8U) {
    sVar4 = param_2[2] * 2;
    uVar1 = lVar3 + 1000;
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
                    /* try { // try from 00bd3c78 to 00cd3c8b has its CatchHandler @ 00bd3e08 */
  *(undefined8 *)((long)pvVar2 + lVar3) = 0x5b726f7463657620;
                    /* try { // try from 00bd3c8c to 00cd3d1f has its CatchHandler @ 00bd3bb8 */
  plVar5 = *(long **)(param_1 + 0x18);
  param_2[1] = param_2[1] + 8;
  if ((plVar5 != (long *)0x0) &&
     ((**(code **)(*plVar5 + 0x20))(plVar5,param_2), (*(ushort *)((long)plVar5 + 9) & 0xc0) != 0x40)
     ) {
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
  *(undefined1 *)((long)pvVar2 + lVar3) = 0x5d;
                    /* try { // try from 00bd3d20 to 00cd3d27 has its CatchHandler @ 00bd3e20 */
  param_2[1] = param_2[1] + 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd3bec"></a> `00bd3bec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bd3bf0"></a> `00bd3bf0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bd3bf4"></a> `00bd3bf4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd3bf8"></a> `00bd3bf8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd3bfc"></a> `00bd3bfc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bd3c00"></a> `00bd3c00` | `15 08 40 f9` | ldr x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bd3c04"></a> `00bd3c04` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bd3c08"></a> `00bd3c08` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bd3c0c"></a> `00bd3c0c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bd3c10"></a> `00bd3c10` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bd3c14"></a> `00bd3c14` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bd3c18"></a> `00bd3c18` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd3c1c"></a> `00bd3c1c` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bd3c20"></a> `00bd3c20` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bd3c24"></a> `00bd3c24` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bd3c28"></a> `00bd3c28` | `c0 00 00 54` | b.eq 0x00bd3c40 | `CONDITIONAL_JUMP`
<a id="insn-00bd3c2c"></a> `00bd3c2c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bd3c30"></a> `00bd3c30` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bd3c34"></a> `00bd3c34` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bd3c38"></a> `00bd3c38` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bd3c3c"></a> `00bd3c3c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd3c40"></a> `00bd3c40` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd3c44"></a> `00bd3c44` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd3c48"></a> `00bd3c48` | `0a 21 00 91` | add x10,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bd3c4c"></a> `00bd3c4c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bd3c50"></a> `00bd3c50` | `49 01 00 54` | b.ls 0x00bd3c78 | `CONDITIONAL_JUMP`
<a id="insn-00bd3c54"></a> `00bd3c54` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bd3c58"></a> `00bd3c58` | `08 a1 0f 91` | add x8,x8,#0x3e8 | `FALL_THROUGH`
<a id="insn-00bd3c5c"></a> `00bd3c5c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bd3c60"></a> `00bd3c60` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bd3c64"></a> `00bd3c64` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bd3c68"></a> `00bd3c68` | `66 25 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bd3c6c"></a> `00bd3c6c` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd3c70"></a> `00bd3c70` | `40 06 00 b4` | cbz x0,0x00bd3d38 | `CONDITIONAL_JUMP`
<a id="insn-00bd3c74"></a> `00bd3c74` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd3c78"></a> `00bd3c78` | `09 c4 8e d2` | mov x9,#0x7620 | `FALL_THROUGH`
<a id="insn-00bd3c7c"></a> `00bd3c7c` | `a9 6c ac f2` | movk x9,#0x6365, LSL #16 | `FALL_THROUGH`
<a id="insn-00bd3c80"></a> `00bd3c80` | `89 ee cd f2` | movk x9,#0x6f74, LSL #32 | `FALL_THROUGH`
<a id="insn-00bd3c84"></a> `00bd3c84` | `49 6e eb f2` | movk x9,#0x5b72, LSL #48 | `FALL_THROUGH`
<a id="insn-00bd3c88"></a> `00bd3c88` | `09 68 28 f8` | str x9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bd3c8c"></a> `00bd3c8c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd3c90"></a> `00bd3c90` | `94 0e 40 f9` | ldr x20,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00bd3c94"></a> `00bd3c94` | `08 21 00 91` | add x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bd3c98"></a> `00bd3c98` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd3c9c"></a> `00bd3c9c` | `f4 01 00 b4` | cbz x20,0x00bd3cd8 | `CONDITIONAL_JUMP`
<a id="insn-00bd3ca0"></a> `00bd3ca0` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bd3ca4"></a> `00bd3ca4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bd3ca8"></a> `00bd3ca8` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bd3cac"></a> `00bd3cac` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bd3cb0"></a> `00bd3cb0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd3cb4"></a> `00bd3cb4` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bd3cb8"></a> `00bd3cb8` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bd3cbc"></a> `00bd3cbc` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bd3cc0"></a> `00bd3cc0` | `c0 00 00 54` | b.eq 0x00bd3cd8 | `CONDITIONAL_JUMP`
<a id="insn-00bd3cc4"></a> `00bd3cc4` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bd3cc8"></a> `00bd3cc8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bd3ccc"></a> `00bd3ccc` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bd3cd0"></a> `00bd3cd0` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bd3cd4"></a> `00bd3cd4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd3cd8"></a> `00bd3cd8` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd3cdc"></a> `00bd3cdc` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd3ce0"></a> `00bd3ce0` | `0a 05 00 91` | add x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bd3ce4"></a> `00bd3ce4` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bd3ce8"></a> `00bd3ce8` | `49 01 00 54` | b.ls 0x00bd3d10 | `CONDITIONAL_JUMP`
<a id="insn-00bd3cec"></a> `00bd3cec` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bd3cf0"></a> `00bd3cf0` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bd3cf4"></a> `00bd3cf4` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bd3cf8"></a> `00bd3cf8` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bd3cfc"></a> `00bd3cfc` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bd3d00"></a> `00bd3d00` | `40 25 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bd3d04"></a> `00bd3d04` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd3d08"></a> `00bd3d08` | `a0 01 00 b4` | cbz x0,0x00bd3d3c | `CONDITIONAL_JUMP`
<a id="insn-00bd3d0c"></a> `00bd3d0c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd3d10"></a> `00bd3d10` | `a9 0b 80 52` | mov w9,#0x5d | `FALL_THROUGH`
<a id="insn-00bd3d14"></a> `00bd3d14` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bd3d18"></a> `00bd3d18` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd3d1c"></a> `00bd3d1c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bd3d20"></a> `00bd3d20` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd3d24"></a> `00bd3d24` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd3d28"></a> `00bd3d28` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd3d2c"></a> `00bd3d2c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bd3d30"></a> `00bd3d30` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bd3d34"></a> `00bd3d34` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bd3d38"></a> `00bd3d38` | `4e 29 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bd3d3c"></a> `00bd3d3c` | `4d 29 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd3bec`](#insn-00bd3bec) 範囲 `[['00bd3bec', '00bd3c2b']]`
  - `CONDITIONAL_JUMP` [`00bd3c28`](#insn-00bd3c28) → [`00bd3c40`](#insn-00bd3c40)
  - `FALL_THROUGH` [`00bd3c28`](#insn-00bd3c28) → [`00bd3c2c`](#insn-00bd3c2c)
- ブロック [`00bd3c2c`](#insn-00bd3c2c) 範囲 `[['00bd3c2c', '00bd3c3f']]`
  - `FALL_THROUGH` [`00bd3c3c`](#insn-00bd3c3c) → [`00bd3c40`](#insn-00bd3c40)
- ブロック [`00bd3c40`](#insn-00bd3c40) 範囲 `[['00bd3c40', '00bd3c43']]`
  - `FALL_THROUGH` [`00bd3c40`](#insn-00bd3c40) → [`00bd3c44`](#insn-00bd3c44)
- ブロック [`00bd3c44`](#insn-00bd3c44) 範囲 `[['00bd3c44', '00bd3c53']]`
  - `CONDITIONAL_JUMP` [`00bd3c50`](#insn-00bd3c50) → [`00bd3c78`](#insn-00bd3c78)
  - `FALL_THROUGH` [`00bd3c50`](#insn-00bd3c50) → [`00bd3c54`](#insn-00bd3c54)
- ブロック [`00bd3c54`](#insn-00bd3c54) 範囲 `[['00bd3c54', '00bd3c73']]`
  - `CONDITIONAL_JUMP` [`00bd3c70`](#insn-00bd3c70) → [`00bd3d38`](#insn-00bd3d38)
  - `FALL_THROUGH` [`00bd3c70`](#insn-00bd3c70) → [`00bd3c74`](#insn-00bd3c74)
- ブロック [`00bd3c74`](#insn-00bd3c74) 範囲 `[['00bd3c74', '00bd3c77']]`
  - `FALL_THROUGH` [`00bd3c74`](#insn-00bd3c74) → [`00bd3c78`](#insn-00bd3c78)
- ブロック [`00bd3c78`](#insn-00bd3c78) 範囲 `[['00bd3c78', '00bd3c8b']]`
  - `FALL_THROUGH` [`00bd3c88`](#insn-00bd3c88) → [`00bd3c8c`](#insn-00bd3c8c)
- ブロック [`00bd3c8c`](#insn-00bd3c8c) 範囲 `[['00bd3c8c', '00bd3c9f']]`
  - `CONDITIONAL_JUMP` [`00bd3c9c`](#insn-00bd3c9c) → [`00bd3cd8`](#insn-00bd3cd8)
  - `FALL_THROUGH` [`00bd3c9c`](#insn-00bd3c9c) → [`00bd3ca0`](#insn-00bd3ca0)
- ブロック [`00bd3ca0`](#insn-00bd3ca0) 範囲 `[['00bd3ca0', '00bd3cc3']]`
  - `CONDITIONAL_JUMP` [`00bd3cc0`](#insn-00bd3cc0) → [`00bd3cd8`](#insn-00bd3cd8)
  - `FALL_THROUGH` [`00bd3cc0`](#insn-00bd3cc0) → [`00bd3cc4`](#insn-00bd3cc4)
- ブロック [`00bd3cc4`](#insn-00bd3cc4) 範囲 `[['00bd3cc4', '00bd3cd7']]`
  - `FALL_THROUGH` [`00bd3cd4`](#insn-00bd3cd4) → [`00bd3cd8`](#insn-00bd3cd8)
- ブロック [`00bd3cd8`](#insn-00bd3cd8) 範囲 `[['00bd3cd8', '00bd3ceb']]`
  - `CONDITIONAL_JUMP` [`00bd3ce8`](#insn-00bd3ce8) → [`00bd3d10`](#insn-00bd3d10)
  - `FALL_THROUGH` [`00bd3ce8`](#insn-00bd3ce8) → [`00bd3cec`](#insn-00bd3cec)
- ブロック [`00bd3cec`](#insn-00bd3cec) 範囲 `[['00bd3cec', '00bd3d0b']]`
  - `CONDITIONAL_JUMP` [`00bd3d08`](#insn-00bd3d08) → [`00bd3d3c`](#insn-00bd3d3c)
  - `FALL_THROUGH` [`00bd3d08`](#insn-00bd3d08) → [`00bd3d0c`](#insn-00bd3d0c)
- ブロック [`00bd3d0c`](#insn-00bd3d0c) 範囲 `[['00bd3d0c', '00bd3d0f']]`
  - `FALL_THROUGH` [`00bd3d0c`](#insn-00bd3d0c) → [`00bd3d10`](#insn-00bd3d10)
- ブロック [`00bd3d10`](#insn-00bd3d10) 範囲 `[['00bd3d10', '00bd3d1f']]`
  - `FALL_THROUGH` [`00bd3d1c`](#insn-00bd3d1c) → [`00bd3d20`](#insn-00bd3d20)
- ブロック [`00bd3d20`](#insn-00bd3d20) 範囲 `[['00bd3d20', '00bd3d37']]`
- ブロック [`00bd3d38`](#insn-00bd3d38) 範囲 `[['00bd3d38', '00bd3d3b']]`
- ブロック [`00bd3d3c`](#insn-00bd3d3c) 範囲 `[['00bd3d3c', '00bd3d3f']]`

## 命令位置別の参照

- [`00bd3bf0`](#insn-00bd3bf0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3bf4`](#insn-00bd3bf4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3bf8`](#insn-00bd3bf8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3c28`](#insn-00bd3c28) → [`00bd3c40`](#insn-00bd3c40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3c50`](#insn-00bd3c50) → [`00bd3c78`](#insn-00bd3c78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3c68`](#insn-00bd3c68) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bd3c70`](#insn-00bd3c70) → [`00bd3d38`](#insn-00bd3d38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3c9c`](#insn-00bd3c9c) → [`00bd3cd8`](#insn-00bd3cd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3cc0`](#insn-00bd3cc0) → [`00bd3cd8`](#insn-00bd3cd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3ce8`](#insn-00bd3ce8) → [`00bd3d10`](#insn-00bd3d10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3d00`](#insn-00bd3d00) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bd3d08`](#insn-00bd3d08) → [`00bd3d3c`](#insn-00bd3d3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3d24`](#insn-00bd3d24) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3d28`](#insn-00bd3d28) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3d2c`](#insn-00bd3d2c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3d38`](#insn-00bd3d38) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bd3d3c`](#insn-00bd3d3c) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd3bf0`](#insn-00bd3bf0)

~~~json
{
  "source": "00bd3bf0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3bf4`](#insn-00bd3bf4)

~~~json
{
  "source": "00bd3bf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3bf8`](#insn-00bd3bf8)

~~~json
{
  "source": "00bd3bf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3c28`](#insn-00bd3c28)

~~~json
{
  "source": "00bd3c28",
  "target": "00bd3c40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3c50`](#insn-00bd3c50)

~~~json
{
  "source": "00bd3c50",
  "target": "00bd3c78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3c68`](#insn-00bd3c68)

~~~json
{
  "source": "00bd3c68",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd3c70`](#insn-00bd3c70)

~~~json
{
  "source": "00bd3c70",
  "target": "00bd3d38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3c9c`](#insn-00bd3c9c)

~~~json
{
  "source": "00bd3c9c",
  "target": "00bd3cd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3cc0`](#insn-00bd3cc0)

~~~json
{
  "source": "00bd3cc0",
  "target": "00bd3cd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3ce8`](#insn-00bd3ce8)

~~~json
{
  "source": "00bd3ce8",
  "target": "00bd3d10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3d00`](#insn-00bd3d00)

~~~json
{
  "source": "00bd3d00",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd3d08`](#insn-00bd3d08)

~~~json
{
  "source": "00bd3d08",
  "target": "00bd3d3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3d24`](#insn-00bd3d24)

~~~json
{
  "source": "00bd3d24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3d28`](#insn-00bd3d28)

~~~json
{
  "source": "00bd3d28",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3d2c`](#insn-00bd3d2c)

~~~json
{
  "source": "00bd3d2c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3d38`](#insn-00bd3d38)

~~~json
{
  "source": "00bd3d38",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd3d3c`](#insn-00bd3d3c)

~~~json
{
  "source": "00bd3d3c",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
