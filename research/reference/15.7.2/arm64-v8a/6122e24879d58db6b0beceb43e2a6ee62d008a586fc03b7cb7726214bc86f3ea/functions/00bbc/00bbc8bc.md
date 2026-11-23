# 00bbc8bc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbc984`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbc984.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0006.md#compare-a4116abaa1797123a3227ab1e4dedd9c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbc8bc",
  "name": "FUN_00bbc8bc",
  "size": 324,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4012f46ba1f4ca5b21198430e7113deda3f20263b9d9caab9de8251d2522d1f1",
  "source_text_sha256": "4012f46ba1f4ca5b21198430e7113deda3f20263b9d9caab9de8251d2522d1f1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbc8bc",
        "00bbc9ff"
      ]
    ],
    "bytes_sha256": "c163c4bde9d6a32d1bbde640999b1189a0e72e11e746693a638483762e8fa0d8",
    "instruction_count": 81,
    "instruction_bytes": 324,
    "body_bytes": 324,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde8d0](../00bde/00bde8d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1626 bytes

~~~c

void FUN_00bbc8bc(long param_1,long param_2,long param_3,long param_4,int param_5,ulong param_6)

{
  int iVar1;
  long lVar2;
  
  lVar2 = *(long *)(param_2 + 0x10);
  if ((param_6 & 1) == 0) {
    if (*(long *)(param_1 + 8) != *(long *)(lVar2 + 8)) goto LAB_00bbc978;
  }
  else if ((lVar2 != param_1) &&
          (iVar1 = strcmp(*(char **)(param_1 + 8),*(char **)(lVar2 + 8)), iVar1 != 0)) {
LAB_00bbc978:
                    /* try { // try from 00bbc98c to 00cbc9a3 has its CatchHandler @ 00bbd31c */
                    /* WARNING: Could not recover jumptable at 0x00bbc99c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(**(long **)(param_1 + 0x10) + 0x28))();
    return;
  }
                    /* try { // try from 00bbc930 to 00cbc947 has its CatchHandler @ 00bbd2dc */
  *(undefined1 *)(param_2 + 0x4d) = 1;
  if (*(long *)(param_2 + 8) != param_4) {
    return;
  }
  *(undefined1 *)(param_2 + 0x4c) = 1;
  if (*(long *)(param_2 + 0x20) == 0) {
    *(long *)(param_2 + 0x20) = param_3;
    *(int *)(param_2 + 0x30) = param_5;
    *(undefined4 *)(param_2 + 0x3c) = 1;
    iVar1 = param_5;
  }
  else {
    if (*(long *)(param_2 + 0x20) != param_3) {
      *(int *)(param_2 + 0x3c) = *(int *)(param_2 + 0x3c) + 1;
      goto LAB_00bbc9e0;
    }
    iVar1 = *(int *)(param_2 + 0x30);
    if (*(int *)(param_2 + 0x30) == 2) {
      *(int *)(param_2 + 0x30) = param_5;
      iVar1 = param_5;
    }
  }
  if (iVar1 != 1) {
    return;
  }
  if (*(int *)(param_2 + 0x48) != 1) {
    return;
  }
LAB_00bbc9e0:
  *(undefined1 *)(param_2 + 0x4e) = 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbc8bc"></a> `00bbc8bc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbc8c0"></a> `00bbc8c0` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bbc8c4"></a> `00bbc8c4` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbc8c8"></a> `00bbc8c8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbc8cc"></a> `00bbc8cc` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbc8d0"></a> `00bbc8d0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbc8d4"></a> `00bbc8d4` | `29 08 40 f9` | ldr x9,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00bbc8d8"></a> `00bbc8d8` | `85 04 00 36` | tbz w5,#0x0,0x00bbc968 | `CONDITIONAL_JUMP`
<a id="insn-00bbc8dc"></a> `00bbc8dc` | `3f 01 00 eb` | cmp x9,x0 | `FALL_THROUGH`
<a id="insn-00bbc8e0"></a> `00bbc8e0` | `80 02 00 54` | b.eq 0x00bbc930 | `CONDITIONAL_JUMP`
<a id="insn-00bbc8e4"></a> `00bbc8e4` | `08 04 40 f9` | ldr x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbc8e8"></a> `00bbc8e8` | `29 05 40 f9` | ldr x9,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bbc8ec"></a> `00bbc8ec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbc8f0"></a> `00bbc8f0` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bbc8f4"></a> `00bbc8f4` | `f6 03 04 2a` | mov w22,w4 | `FALL_THROUGH`
<a id="insn-00bbc8f8"></a> `00bbc8f8` | `f7 03 02 aa` | mov x23,x2 | `FALL_THROUGH`
<a id="insn-00bbc8fc"></a> `00bbc8fc` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bbc900"></a> `00bbc900` | `e1 03 09 aa` | mov x1,x9 | `FALL_THROUGH`
<a id="insn-00bbc904"></a> `00bbc904` | `f5 03 03 aa` | mov x21,x3 | `FALL_THROUGH`
<a id="insn-00bbc908"></a> `00bbc908` | `f8 03 05 2a` | mov w24,w5 | `FALL_THROUGH`
<a id="insn-00bbc90c"></a> `00bbc90c` | `f1 87 00 94` | bl 0x00bde8d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc910"></a> `00bbc910` | `e5 03 18 2a` | mov w5,w24 | `FALL_THROUGH`
<a id="insn-00bbc914"></a> `00bbc914` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-00bbc918"></a> `00bbc918` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00bbc91c"></a> `00bbc91c` | `e4 03 16 2a` | mov w4,w22 | `FALL_THROUGH`
<a id="insn-00bbc920"></a> `00bbc920` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbc924"></a> `00bbc924` | `e8 03 00 2a` | mov w8,w0 | `FALL_THROUGH`
<a id="insn-00bbc928"></a> `00bbc928` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbc92c"></a> `00bbc92c` | `68 02 00 35` | cbnz w8,0x00bbc978 | `CONDITIONAL_JUMP`
<a id="insn-00bbc930"></a> `00bbc930` | `29 04 40 f9` | ldr x9,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bbc934"></a> `00bbc934` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbc938"></a> `00bbc938` | `28 34 01 39` | strb w8,[x1, #0x4d] | `FALL_THROUGH`
<a id="insn-00bbc93c"></a> `00bbc93c` | `3f 01 03 eb` | cmp x9,x3 | `FALL_THROUGH`
<a id="insn-00bbc940"></a> `00bbc940` | `41 05 00 54` | b.ne 0x00bbc9e8 | `CONDITIONAL_JUMP`
<a id="insn-00bbc944"></a> `00bbc944` | `29 10 40 f9` | ldr x9,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bbc948"></a> `00bbc948` | `28 30 01 39` | strb w8,[x1, #0x4c] | `FALL_THROUGH`
<a id="insn-00bbc94c"></a> `00bbc94c` | `a9 02 00 b4` | cbz x9,0x00bbc9a0 | `CONDITIONAL_JUMP`
<a id="insn-00bbc950"></a> `00bbc950` | `3f 01 02 eb` | cmp x9,x2 | `FALL_THROUGH`
<a id="insn-00bbc954"></a> `00bbc954` | `20 03 00 54` | b.eq 0x00bbc9b8 | `CONDITIONAL_JUMP`
<a id="insn-00bbc958"></a> `00bbc958` | `28 3c 40 b9` | ldr w8,[x1, #0x3c] | `FALL_THROUGH`
<a id="insn-00bbc95c"></a> `00bbc95c` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbc960"></a> `00bbc960` | `28 3c 00 b9` | str w8,[x1, #0x3c] | `FALL_THROUGH`
<a id="insn-00bbc964"></a> `00bbc964` | `1f 00 00 14` | b 0x00bbc9e0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbc968"></a> `00bbc968` | `08 04 40 f9` | ldr x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbc96c"></a> `00bbc96c` | `29 05 40 f9` | ldr x9,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bbc970"></a> `00bbc970` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbc974"></a> `00bbc974` | `e0 fd ff 54` | b.eq 0x00bbc930 | `CONDITIONAL_JUMP`
<a id="insn-00bbc978"></a> `00bbc978` | `00 08 40 f9` | ldr x0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbc97c"></a> `00bbc97c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbc980"></a> `00bbc980` | `10 15 40 f9` | ldr x16,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bbc984"></a> `00bbc984` | `a5 00 00 12` | and w5,w5,#0x1 | `FALL_THROUGH`
<a id="insn-00bbc988"></a> `00bbc988` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbc98c"></a> `00bbc98c` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbc990"></a> `00bbc990` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbc994"></a> `00bbc994` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bbc998"></a> `00bbc998` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbc99c"></a> `00bbc99c` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00bbc9a0"></a> `00bbc9a0` | `9f 04 00 71` | cmp w4,#0x1 | `FALL_THROUGH`
<a id="insn-00bbc9a4"></a> `00bbc9a4` | `22 10 00 f9` | str x2,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bbc9a8"></a> `00bbc9a8` | `24 30 00 b9` | str w4,[x1, #0x30] | `FALL_THROUGH`
<a id="insn-00bbc9ac"></a> `00bbc9ac` | `28 3c 00 b9` | str w8,[x1, #0x3c] | `FALL_THROUGH`
<a id="insn-00bbc9b0"></a> `00bbc9b0` | `20 01 00 54` | b.eq 0x00bbc9d4 | `CONDITIONAL_JUMP`
<a id="insn-00bbc9b4"></a> `00bbc9b4` | `0d 00 00 14` | b 0x00bbc9e8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbc9b8"></a> `00bbc9b8` | `28 30 40 b9` | ldr w8,[x1, #0x30] | `FALL_THROUGH`
<a id="insn-00bbc9bc"></a> `00bbc9bc` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbc9c0"></a> `00bbc9c0` | `61 00 00 54` | b.ne 0x00bbc9cc | `CONDITIONAL_JUMP`
<a id="insn-00bbc9c4"></a> `00bbc9c4` | `e8 03 04 2a` | mov w8,w4 | `FALL_THROUGH`
<a id="insn-00bbc9c8"></a> `00bbc9c8` | `24 30 00 b9` | str w4,[x1, #0x30] | `FALL_THROUGH`
<a id="insn-00bbc9cc"></a> `00bbc9cc` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbc9d0"></a> `00bbc9d0` | `c1 00 00 54` | b.ne 0x00bbc9e8 | `CONDITIONAL_JUMP`
<a id="insn-00bbc9d4"></a> `00bbc9d4` | `28 48 40 b9` | ldr w8,[x1, #0x48] | `FALL_THROUGH`
<a id="insn-00bbc9d8"></a> `00bbc9d8` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbc9dc"></a> `00bbc9dc` | `61 00 00 54` | b.ne 0x00bbc9e8 | `CONDITIONAL_JUMP`
<a id="insn-00bbc9e0"></a> `00bbc9e0` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbc9e4"></a> `00bbc9e4` | `28 38 01 39` | strb w8,[x1, #0x4e] | `FALL_THROUGH`
<a id="insn-00bbc9e8"></a> `00bbc9e8` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbc9ec"></a> `00bbc9ec` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbc9f0"></a> `00bbc9f0` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbc9f4"></a> `00bbc9f4` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bbc9f8"></a> `00bbc9f8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbc9fc"></a> `00bbc9fc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbc8bc`](#insn-00bbc8bc) 範囲 `[['00bbc8bc', '00bbc8db']]`
  - `CONDITIONAL_JUMP` [`00bbc8d8`](#insn-00bbc8d8) → [`00bbc968`](#insn-00bbc968)
  - `FALL_THROUGH` [`00bbc8d8`](#insn-00bbc8d8) → [`00bbc8dc`](#insn-00bbc8dc)
- ブロック [`00bbc8dc`](#insn-00bbc8dc) 範囲 `[['00bbc8dc', '00bbc8e3']]`
  - `CONDITIONAL_JUMP` [`00bbc8e0`](#insn-00bbc8e0) → [`00bbc930`](#insn-00bbc930)
  - `FALL_THROUGH` [`00bbc8e0`](#insn-00bbc8e0) → [`00bbc8e4`](#insn-00bbc8e4)
- ブロック [`00bbc8e4`](#insn-00bbc8e4) 範囲 `[['00bbc8e4', '00bbc92f']]`
  - `CONDITIONAL_JUMP` [`00bbc92c`](#insn-00bbc92c) → [`00bbc978`](#insn-00bbc978)
  - `FALL_THROUGH` [`00bbc92c`](#insn-00bbc92c) → [`00bbc930`](#insn-00bbc930)
- ブロック [`00bbc930`](#insn-00bbc930) 範囲 `[['00bbc930', '00bbc943']]`
  - `CONDITIONAL_JUMP` [`00bbc940`](#insn-00bbc940) → [`00bbc9e8`](#insn-00bbc9e8)
  - `FALL_THROUGH` [`00bbc940`](#insn-00bbc940) → [`00bbc944`](#insn-00bbc944)
- ブロック [`00bbc944`](#insn-00bbc944) 範囲 `[['00bbc944', '00bbc94f']]`
  - `CONDITIONAL_JUMP` [`00bbc94c`](#insn-00bbc94c) → [`00bbc9a0`](#insn-00bbc9a0)
  - `FALL_THROUGH` [`00bbc94c`](#insn-00bbc94c) → [`00bbc950`](#insn-00bbc950)
- ブロック [`00bbc950`](#insn-00bbc950) 範囲 `[['00bbc950', '00bbc957']]`
  - `CONDITIONAL_JUMP` [`00bbc954`](#insn-00bbc954) → [`00bbc9b8`](#insn-00bbc9b8)
  - `FALL_THROUGH` [`00bbc954`](#insn-00bbc954) → [`00bbc958`](#insn-00bbc958)
- ブロック [`00bbc958`](#insn-00bbc958) 範囲 `[['00bbc958', '00bbc967']]`
  - `UNCONDITIONAL_JUMP` [`00bbc964`](#insn-00bbc964) → [`00bbc9e0`](#insn-00bbc9e0)
- ブロック [`00bbc968`](#insn-00bbc968) 範囲 `[['00bbc968', '00bbc977']]`
  - `CONDITIONAL_JUMP` [`00bbc974`](#insn-00bbc974) → [`00bbc930`](#insn-00bbc930)
  - `FALL_THROUGH` [`00bbc974`](#insn-00bbc974) → [`00bbc978`](#insn-00bbc978)
- ブロック [`00bbc978`](#insn-00bbc978) 範囲 `[['00bbc978', '00bbc98b']]`
  - `FALL_THROUGH` [`00bbc988`](#insn-00bbc988) → [`00bbc98c`](#insn-00bbc98c)
- ブロック [`00bbc98c`](#insn-00bbc98c) 範囲 `[['00bbc98c', '00bbc99f']]`
- ブロック [`00bbc9a0`](#insn-00bbc9a0) 範囲 `[['00bbc9a0', '00bbc9b3']]`
  - `CONDITIONAL_JUMP` [`00bbc9b0`](#insn-00bbc9b0) → [`00bbc9d4`](#insn-00bbc9d4)
  - `FALL_THROUGH` [`00bbc9b0`](#insn-00bbc9b0) → [`00bbc9b4`](#insn-00bbc9b4)
- ブロック [`00bbc9b4`](#insn-00bbc9b4) 範囲 `[['00bbc9b4', '00bbc9b7']]`
  - `UNCONDITIONAL_JUMP` [`00bbc9b4`](#insn-00bbc9b4) → [`00bbc9e8`](#insn-00bbc9e8)
- ブロック [`00bbc9b8`](#insn-00bbc9b8) 範囲 `[['00bbc9b8', '00bbc9c3']]`
  - `CONDITIONAL_JUMP` [`00bbc9c0`](#insn-00bbc9c0) → [`00bbc9cc`](#insn-00bbc9cc)
  - `FALL_THROUGH` [`00bbc9c0`](#insn-00bbc9c0) → [`00bbc9c4`](#insn-00bbc9c4)
- ブロック [`00bbc9c4`](#insn-00bbc9c4) 範囲 `[['00bbc9c4', '00bbc9cb']]`
  - `FALL_THROUGH` [`00bbc9c8`](#insn-00bbc9c8) → [`00bbc9cc`](#insn-00bbc9cc)
- ブロック [`00bbc9cc`](#insn-00bbc9cc) 範囲 `[['00bbc9cc', '00bbc9d3']]`
  - `CONDITIONAL_JUMP` [`00bbc9d0`](#insn-00bbc9d0) → [`00bbc9e8`](#insn-00bbc9e8)
  - `FALL_THROUGH` [`00bbc9d0`](#insn-00bbc9d0) → [`00bbc9d4`](#insn-00bbc9d4)
- ブロック [`00bbc9d4`](#insn-00bbc9d4) 範囲 `[['00bbc9d4', '00bbc9df']]`
  - `CONDITIONAL_JUMP` [`00bbc9dc`](#insn-00bbc9dc) → [`00bbc9e8`](#insn-00bbc9e8)
  - `FALL_THROUGH` [`00bbc9dc`](#insn-00bbc9dc) → [`00bbc9e0`](#insn-00bbc9e0)
- ブロック [`00bbc9e0`](#insn-00bbc9e0) 範囲 `[['00bbc9e0', '00bbc9e7']]`
  - `FALL_THROUGH` [`00bbc9e4`](#insn-00bbc9e4) → [`00bbc9e8`](#insn-00bbc9e8)
- ブロック [`00bbc9e8`](#insn-00bbc9e8) 範囲 `[['00bbc9e8', '00bbc9ff']]`

## 命令位置別の参照

- [`00bbc8c0`](#insn-00bbc8c0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc8c4`](#insn-00bbc8c4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc8c8`](#insn-00bbc8c8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc8cc`](#insn-00bbc8cc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc8d8`](#insn-00bbc8d8) → [`00bbc968`](#insn-00bbc968) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc8e0`](#insn-00bbc8e0) → [`00bbc930`](#insn-00bbc930) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc90c`](#insn-00bbc90c) → [`00bde8d0`](../00bde/00bde8d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde8d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbc92c`](#insn-00bbc92c) → [`00bbc978`](#insn-00bbc978) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc940`](#insn-00bbc940) → [`00bbc9e8`](#insn-00bbc9e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc94c`](#insn-00bbc94c) → [`00bbc9a0`](#insn-00bbc9a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc954`](#insn-00bbc954) → [`00bbc9b8`](#insn-00bbc9b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc964`](#insn-00bbc964) → [`00bbc9e0`](#insn-00bbc9e0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc974`](#insn-00bbc974) → [`00bbc930`](#insn-00bbc930) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc988`](#insn-00bbc988) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc98c`](#insn-00bbc98c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc990`](#insn-00bbc990) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc994`](#insn-00bbc994) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc9b0`](#insn-00bbc9b0) → [`00bbc9d4`](#insn-00bbc9d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc9b4`](#insn-00bbc9b4) → [`00bbc9e8`](#insn-00bbc9e8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc9c0`](#insn-00bbc9c0) → [`00bbc9cc`](#insn-00bbc9cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc9d0`](#insn-00bbc9d0) → [`00bbc9e8`](#insn-00bbc9e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc9dc`](#insn-00bbc9dc) → [`00bbc9e8`](#insn-00bbc9e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc9e8`](#insn-00bbc9e8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc9ec`](#insn-00bbc9ec) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc9f0`](#insn-00bbc9f0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc9f4`](#insn-00bbc9f4) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbc8c0`](#insn-00bbc8c0)

~~~json
{
  "source": "00bbc8c0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc8c4`](#insn-00bbc8c4)

~~~json
{
  "source": "00bbc8c4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc8c8`](#insn-00bbc8c8)

~~~json
{
  "source": "00bbc8c8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc8cc`](#insn-00bbc8cc)

~~~json
{
  "source": "00bbc8cc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc8d8`](#insn-00bbc8d8)

~~~json
{
  "source": "00bbc8d8",
  "target": "00bbc968",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc8e0`](#insn-00bbc8e0)

~~~json
{
  "source": "00bbc8e0",
  "target": "00bbc930",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc90c`](#insn-00bbc90c)

~~~json
{
  "source": "00bbc90c",
  "target": "00bde8d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc92c`](#insn-00bbc92c)

~~~json
{
  "source": "00bbc92c",
  "target": "00bbc978",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc940`](#insn-00bbc940)

~~~json
{
  "source": "00bbc940",
  "target": "00bbc9e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc94c`](#insn-00bbc94c)

~~~json
{
  "source": "00bbc94c",
  "target": "00bbc9a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc954`](#insn-00bbc954)

~~~json
{
  "source": "00bbc954",
  "target": "00bbc9b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc964`](#insn-00bbc964)

~~~json
{
  "source": "00bbc964",
  "target": "00bbc9e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc974`](#insn-00bbc974)

~~~json
{
  "source": "00bbc974",
  "target": "00bbc930",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc988`](#insn-00bbc988)

~~~json
{
  "source": "00bbc988",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc98c`](#insn-00bbc98c)

~~~json
{
  "source": "00bbc98c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc990`](#insn-00bbc990)

~~~json
{
  "source": "00bbc990",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc994`](#insn-00bbc994)

~~~json
{
  "source": "00bbc994",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc9b0`](#insn-00bbc9b0)

~~~json
{
  "source": "00bbc9b0",
  "target": "00bbc9d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc9b4`](#insn-00bbc9b4)

~~~json
{
  "source": "00bbc9b4",
  "target": "00bbc9e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc9c0`](#insn-00bbc9c0)

~~~json
{
  "source": "00bbc9c0",
  "target": "00bbc9cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc9d0`](#insn-00bbc9d0)

~~~json
{
  "source": "00bbc9d0",
  "target": "00bbc9e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc9dc`](#insn-00bbc9dc)

~~~json
{
  "source": "00bbc9dc",
  "target": "00bbc9e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc9e8`](#insn-00bbc9e8)

~~~json
{
  "source": "00bbc9e8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc9ec`](#insn-00bbc9ec)

~~~json
{
  "source": "00bbc9ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc9f0`](#insn-00bbc9f0)

~~~json
{
  "source": "00bbc9f0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc9f4`](#insn-00bbc9f4)

~~~json
{
  "source": "00bbc9f4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
