# 00aa1dac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aa1bb0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa1/00aa1bb0.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0004.md#compare-9e8d38899d8c96c97c19c23871619b5f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aa1e1c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aa1/00aa1e1c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0005.md#compare-3a38c670c1233c14b1bdddd01928e894)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa1dac",
  "name": "FUN_00aa1dac",
  "size": 284,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "db4c0530df0aaa57ff60b47b497ad4c19f700847a92c8969a36e63006012dcec",
  "source_text_sha256": "db4c0530df0aaa57ff60b47b497ad4c19f700847a92c8969a36e63006012dcec",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aa1dac",
        "00aa1ec7"
      ]
    ],
    "bytes_sha256": "e246a7af95229e7b6cb665e00c8141c3fdb1275aa90c24cecf5e836736fa54c7",
    "instruction_count": 71,
    "instruction_bytes": 284,
    "body_bytes": 284,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00aa0268](../00aa0/00aa0268.md)

## 呼び出し先

- [0043bba4](../0043b/0043bba4.md)
- [00aa1aa0](../00aa1/00aa1aa0.md)
- [00aa1c48](../00aa1/00aa1c48.md)
- [00c57ee0](../00c57/00c57ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1757 bytes

~~~c

void FUN_00aa1dac(long *param_1,long *param_2,long *param_3)

{
  long lVar1;
  bool bVar2;
  long *plVar3;
  undefined8 *puVar4;
  undefined1 auStack_70 [8];
  undefined8 local_68;
  undefined8 *apuStack_60 [3];
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  do {
    while( true ) {
      if (param_2 == param_3) {
        if (*(long *)(lVar1 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
          __stack_chk_fail();
        }
        return;
      }
      plVar3 = (long *)FUN_00aa1aa0(param_1,param_1 + 1,&local_68,auStack_70,param_2 + 4);
      if (*plVar3 != 0) break;
      FUN_00aa1c48(apuStack_60,param_1,param_2 + 4);
                    /* try { // try from 00aa1e38 to 00ba1e3b has its CatchHandler @ 00aa2a90 */
      *apuStack_60[0] = 0;
      apuStack_60[0][1] = 0;
                    /* try { // try from 00aa1e3c to 00ba1f63 has its CatchHandler @ 00aa1600 */
      apuStack_60[0][2] = local_68;
      *plVar3 = (long)apuStack_60[0];
      puVar4 = apuStack_60[0];
      if (*(long *)*param_1 != 0) {
        *param_1 = *(long *)*param_1;
        puVar4 = (undefined8 *)*plVar3;
      }
      FUN_0043bba4(param_1[1],puVar4);
      param_1[2] = param_1[2] + 1;
      plVar3 = (long *)param_2[1];
      if ((long *)param_2[1] == (long *)0x0) goto LAB_00aa1e84;
LAB_00aa1e74:
      do {
        param_2 = plVar3;
        plVar3 = (long *)*param_2;
      } while ((long *)*param_2 != (long *)0x0);
    }
    plVar3 = (long *)param_2[1];
    if ((long *)param_2[1] != (long *)0x0) goto LAB_00aa1e74;
LAB_00aa1e84:
    do {
      plVar3 = (long *)param_2[2];
      bVar2 = (long *)*plVar3 != param_2;
      param_2 = plVar3;
    } while (bVar2);
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aa1dac"></a> `00aa1dac` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00aa1db0"></a> `00aa1db0` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aa1db4"></a> `00aa1db4` | `f7 23 00 f9` | str x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aa1db8"></a> `00aa1db8` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aa1dbc"></a> `00aa1dbc` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aa1dc0"></a> `00aa1dc0` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aa1dc4"></a> `00aa1dc4` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aa1dc8"></a> `00aa1dc8` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00aa1dcc"></a> `00aa1dcc` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-00aa1dd0"></a> `00aa1dd0` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aa1dd4"></a> `00aa1dd4` | `40 06 00 54` | b.eq 0x00aa1e9c | `CONDITIONAL_JUMP`
<a id="insn-00aa1dd8"></a> `00aa1dd8` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00aa1ddc"></a> `00aa1ddc` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00aa1de0"></a> `00aa1de0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aa1de4"></a> `00aa1de4` | `04 00 00 14` | b 0x00aa1df4 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa1de8"></a> `00aa1de8` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00aa1dec"></a> `00aa1dec` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00aa1df0"></a> `00aa1df0` | `60 05 00 54` | b.eq 0x00aa1e9c | `CONDITIONAL_JUMP`
<a id="insn-00aa1df4"></a> `00aa1df4` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aa1df8"></a> `00aa1df8` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aa1dfc"></a> `00aa1dfc` | `e3 03 00 91` | mov x3,sp | `FALL_THROUGH`
<a id="insn-00aa1e00"></a> `00aa1e00` | `a4 82 00 91` | add x4,x21,#0x20 | `FALL_THROUGH`
<a id="insn-00aa1e04"></a> `00aa1e04` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aa1e08"></a> `00aa1e08` | `26 ff ff 97` | bl 0x00aa1aa0 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1e0c"></a> `00aa1e0c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00aa1e10"></a> `00aa1e10` | `88 00 00 b4` | cbz x8,0x00aa1e20 | `CONDITIONAL_JUMP`
<a id="insn-00aa1e14"></a> `00aa1e14` | `a9 06 40 f9` | ldr x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00aa1e18"></a> `00aa1e18` | `e9 02 00 b5` | cbnz x9,0x00aa1e74 | `CONDITIONAL_JUMP`
<a id="insn-00aa1e1c"></a> `00aa1e1c` | `1a 00 00 14` | b 0x00aa1e84 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa1e20"></a> `00aa1e20` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00aa1e24"></a> `00aa1e24` | `e8 43 00 91` | add x8,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aa1e28"></a> `00aa1e28` | `a1 82 00 91` | add x1,x21,#0x20 | `FALL_THROUGH`
<a id="insn-00aa1e2c"></a> `00aa1e2c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aa1e30"></a> `00aa1e30` | `86 ff ff 97` | bl 0x00aa1c48 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1e34"></a> `00aa1e34` | `e8 87 40 a9` | ldp x8,x1,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aa1e38"></a> `00aa1e38` | `3f 7c 00 a9` | stp xzr,xzr,[x1] | `FALL_THROUGH`
<a id="insn-00aa1e3c"></a> `00aa1e3c` | `28 08 00 f9` | str x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00aa1e40"></a> `00aa1e40` | `c1 02 00 f9` | str x1,[x22] | `FALL_THROUGH`
<a id="insn-00aa1e44"></a> `00aa1e44` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aa1e48"></a> `00aa1e48` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aa1e4c"></a> `00aa1e4c` | `68 00 00 b4` | cbz x8,0x00aa1e58 | `CONDITIONAL_JUMP`
<a id="insn-00aa1e50"></a> `00aa1e50` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00aa1e54"></a> `00aa1e54` | `c1 02 40 f9` | ldr x1,[x22] | `FALL_THROUGH`
<a id="insn-00aa1e58"></a> `00aa1e58` | `80 06 40 f9` | ldr x0,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00aa1e5c"></a> `00aa1e5c` | `52 67 e6 97` | bl 0x0043bba4 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1e60"></a> `00aa1e60` | `88 0a 40 f9` | ldr x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00aa1e64"></a> `00aa1e64` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aa1e68"></a> `00aa1e68` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00aa1e6c"></a> `00aa1e6c` | `a9 06 40 f9` | ldr x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00aa1e70"></a> `00aa1e70` | `a9 00 00 b4` | cbz x9,0x00aa1e84 | `CONDITIONAL_JUMP`
<a id="insn-00aa1e74"></a> `00aa1e74` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00aa1e78"></a> `00aa1e78` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00aa1e7c"></a> `00aa1e7c` | `c9 ff ff b5` | cbnz x9,0x00aa1e74 | `CONDITIONAL_JUMP`
<a id="insn-00aa1e80"></a> `00aa1e80` | `da ff ff 17` | b 0x00aa1de8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa1e84"></a> `00aa1e84` | `a8 0a 40 f9` | ldr x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00aa1e88"></a> `00aa1e88` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00aa1e8c"></a> `00aa1e8c` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00aa1e90"></a> `00aa1e90` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00aa1e94"></a> `00aa1e94` | `81 ff ff 54` | b.ne 0x00aa1e84 | `CONDITIONAL_JUMP`
<a id="insn-00aa1e98"></a> `00aa1e98` | `d4 ff ff 17` | b 0x00aa1de8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa1e9c"></a> `00aa1e9c` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00aa1ea0"></a> `00aa1ea0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aa1ea4"></a> `00aa1ea4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aa1ea8"></a> `00aa1ea8` | `e1 00 00 54` | b.ne 0x00aa1ec4 | `CONDITIONAL_JUMP`
<a id="insn-00aa1eac"></a> `00aa1eac` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aa1eb0"></a> `00aa1eb0` | `f7 23 40 f9` | ldr x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aa1eb4"></a> `00aa1eb4` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aa1eb8"></a> `00aa1eb8` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aa1ebc"></a> `00aa1ebc` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00aa1ec0"></a> `00aa1ec0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aa1ec4"></a> `00aa1ec4` | `07 d8 06 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aa1dac`](#insn-00aa1dac) 範囲 `[['00aa1dac', '00aa1dd7']]`
  - `CONDITIONAL_JUMP` [`00aa1dd4`](#insn-00aa1dd4) → [`00aa1e9c`](#insn-00aa1e9c)
  - `FALL_THROUGH` [`00aa1dd4`](#insn-00aa1dd4) → [`00aa1dd8`](#insn-00aa1dd8)
- ブロック [`00aa1dd8`](#insn-00aa1dd8) 範囲 `[['00aa1dd8', '00aa1de7']]`
  - `UNCONDITIONAL_JUMP` [`00aa1de4`](#insn-00aa1de4) → [`00aa1df4`](#insn-00aa1df4)
- ブロック [`00aa1de8`](#insn-00aa1de8) 範囲 `[['00aa1de8', '00aa1df3']]`
  - `CONDITIONAL_JUMP` [`00aa1df0`](#insn-00aa1df0) → [`00aa1e9c`](#insn-00aa1e9c)
  - `FALL_THROUGH` [`00aa1df0`](#insn-00aa1df0) → [`00aa1df4`](#insn-00aa1df4)
- ブロック [`00aa1df4`](#insn-00aa1df4) 範囲 `[['00aa1df4', '00aa1e13']]`
  - `CONDITIONAL_JUMP` [`00aa1e10`](#insn-00aa1e10) → [`00aa1e20`](#insn-00aa1e20)
  - `FALL_THROUGH` [`00aa1e10`](#insn-00aa1e10) → [`00aa1e14`](#insn-00aa1e14)
- ブロック [`00aa1e14`](#insn-00aa1e14) 範囲 `[['00aa1e14', '00aa1e1b']]`
  - `CONDITIONAL_JUMP` [`00aa1e18`](#insn-00aa1e18) → [`00aa1e74`](#insn-00aa1e74)
  - `FALL_THROUGH` [`00aa1e18`](#insn-00aa1e18) → [`00aa1e1c`](#insn-00aa1e1c)
- ブロック [`00aa1e1c`](#insn-00aa1e1c) 範囲 `[['00aa1e1c', '00aa1e1f']]`
  - `UNCONDITIONAL_JUMP` [`00aa1e1c`](#insn-00aa1e1c) → [`00aa1e84`](#insn-00aa1e84)
- ブロック [`00aa1e20`](#insn-00aa1e20) 範囲 `[['00aa1e20', '00aa1e37']]`
  - `FALL_THROUGH` [`00aa1e34`](#insn-00aa1e34) → [`00aa1e38`](#insn-00aa1e38)
- ブロック [`00aa1e38`](#insn-00aa1e38) 範囲 `[['00aa1e38', '00aa1e3b']]`
  - `FALL_THROUGH` [`00aa1e38`](#insn-00aa1e38) → [`00aa1e3c`](#insn-00aa1e3c)
- ブロック [`00aa1e3c`](#insn-00aa1e3c) 範囲 `[['00aa1e3c', '00aa1e4f']]`
  - `CONDITIONAL_JUMP` [`00aa1e4c`](#insn-00aa1e4c) → [`00aa1e58`](#insn-00aa1e58)
  - `FALL_THROUGH` [`00aa1e4c`](#insn-00aa1e4c) → [`00aa1e50`](#insn-00aa1e50)
- ブロック [`00aa1e50`](#insn-00aa1e50) 範囲 `[['00aa1e50', '00aa1e57']]`
  - `FALL_THROUGH` [`00aa1e54`](#insn-00aa1e54) → [`00aa1e58`](#insn-00aa1e58)
- ブロック [`00aa1e58`](#insn-00aa1e58) 範囲 `[['00aa1e58', '00aa1e73']]`
  - `CONDITIONAL_JUMP` [`00aa1e70`](#insn-00aa1e70) → [`00aa1e84`](#insn-00aa1e84)
  - `FALL_THROUGH` [`00aa1e70`](#insn-00aa1e70) → [`00aa1e74`](#insn-00aa1e74)
- ブロック [`00aa1e74`](#insn-00aa1e74) 範囲 `[['00aa1e74', '00aa1e7f']]`
  - `CONDITIONAL_JUMP` [`00aa1e7c`](#insn-00aa1e7c) → [`00aa1e74`](#insn-00aa1e74)
  - `FALL_THROUGH` [`00aa1e7c`](#insn-00aa1e7c) → [`00aa1e80`](#insn-00aa1e80)
- ブロック [`00aa1e80`](#insn-00aa1e80) 範囲 `[['00aa1e80', '00aa1e83']]`
  - `UNCONDITIONAL_JUMP` [`00aa1e80`](#insn-00aa1e80) → [`00aa1de8`](#insn-00aa1de8)
- ブロック [`00aa1e84`](#insn-00aa1e84) 範囲 `[['00aa1e84', '00aa1e97']]`
  - `CONDITIONAL_JUMP` [`00aa1e94`](#insn-00aa1e94) → [`00aa1e84`](#insn-00aa1e84)
  - `FALL_THROUGH` [`00aa1e94`](#insn-00aa1e94) → [`00aa1e98`](#insn-00aa1e98)
- ブロック [`00aa1e98`](#insn-00aa1e98) 範囲 `[['00aa1e98', '00aa1e9b']]`
  - `UNCONDITIONAL_JUMP` [`00aa1e98`](#insn-00aa1e98) → [`00aa1de8`](#insn-00aa1de8)
- ブロック [`00aa1e9c`](#insn-00aa1e9c) 範囲 `[['00aa1e9c', '00aa1eab']]`
  - `CONDITIONAL_JUMP` [`00aa1ea8`](#insn-00aa1ea8) → [`00aa1ec4`](#insn-00aa1ec4)
  - `FALL_THROUGH` [`00aa1ea8`](#insn-00aa1ea8) → [`00aa1eac`](#insn-00aa1eac)
- ブロック [`00aa1eac`](#insn-00aa1eac) 範囲 `[['00aa1eac', '00aa1ec3']]`
- ブロック [`00aa1ec4`](#insn-00aa1ec4) 範囲 `[['00aa1ec4', '00aa1ec7']]`

## 命令位置別の参照

- [`00aa1db0`](#insn-00aa1db0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1db4`](#insn-00aa1db4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1db8`](#insn-00aa1db8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1dbc`](#insn-00aa1dbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1dd0`](#insn-00aa1dd0) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1dd4`](#insn-00aa1dd4) → [`00aa1e9c`](#insn-00aa1e9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1de4`](#insn-00aa1de4) → [`00aa1df4`](#insn-00aa1df4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1df0`](#insn-00aa1df0) → [`00aa1e9c`](#insn-00aa1e9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e08`](#insn-00aa1e08) → [`00aa1aa0`](00aa1aa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aa1aa0` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e10`](#insn-00aa1e10) → [`00aa1e20`](#insn-00aa1e20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e18`](#insn-00aa1e18) → [`00aa1e74`](#insn-00aa1e74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e1c`](#insn-00aa1e1c) → [`00aa1e84`](#insn-00aa1e84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e30`](#insn-00aa1e30) → [`00aa1c48`](00aa1c48.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aa1c48` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e34`](#insn-00aa1e34) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e4c`](#insn-00aa1e4c) → [`00aa1e58`](#insn-00aa1e58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e5c`](#insn-00aa1e5c) → [`0043bba4`](../0043b/0043bba4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bba4` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e70`](#insn-00aa1e70) → [`00aa1e84`](#insn-00aa1e84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e7c`](#insn-00aa1e7c) → [`00aa1e74`](#insn-00aa1e74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e80`](#insn-00aa1e80) → [`00aa1de8`](#insn-00aa1de8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e94`](#insn-00aa1e94) → [`00aa1e84`](#insn-00aa1e84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1e98`](#insn-00aa1e98) → [`00aa1de8`](#insn-00aa1de8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1ea0`](#insn-00aa1ea0) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1ea8`](#insn-00aa1ea8) → [`00aa1ec4`](#insn-00aa1ec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1eac`](#insn-00aa1eac) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1eb0`](#insn-00aa1eb0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1eb4`](#insn-00aa1eb4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1eb8`](#insn-00aa1eb8) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1ec4`](#insn-00aa1ec4) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aa1db0`](#insn-00aa1db0)

~~~json
{
  "source": "00aa1db0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1db4`](#insn-00aa1db4)

~~~json
{
  "source": "00aa1db4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1db8`](#insn-00aa1db8)

~~~json
{
  "source": "00aa1db8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1dbc`](#insn-00aa1dbc)

~~~json
{
  "source": "00aa1dbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1dd0`](#insn-00aa1dd0)

~~~json
{
  "source": "00aa1dd0",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1dd4`](#insn-00aa1dd4)

~~~json
{
  "source": "00aa1dd4",
  "target": "00aa1e9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1de4`](#insn-00aa1de4)

~~~json
{
  "source": "00aa1de4",
  "target": "00aa1df4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1df0`](#insn-00aa1df0)

~~~json
{
  "source": "00aa1df0",
  "target": "00aa1e9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1e08`](#insn-00aa1e08)

~~~json
{
  "source": "00aa1e08",
  "target": "00aa1aa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1e10`](#insn-00aa1e10)

~~~json
{
  "source": "00aa1e10",
  "target": "00aa1e20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1e18`](#insn-00aa1e18)

~~~json
{
  "source": "00aa1e18",
  "target": "00aa1e74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1e1c`](#insn-00aa1e1c)

~~~json
{
  "source": "00aa1e1c",
  "target": "00aa1e84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1e30`](#insn-00aa1e30)

~~~json
{
  "source": "00aa1e30",
  "target": "00aa1c48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1e34`](#insn-00aa1e34)

~~~json
{
  "source": "00aa1e34",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1e4c`](#insn-00aa1e4c)

~~~json
{
  "source": "00aa1e4c",
  "target": "00aa1e58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1e5c`](#insn-00aa1e5c)

~~~json
{
  "source": "00aa1e5c",
  "target": "0043bba4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1e70`](#insn-00aa1e70)

~~~json
{
  "source": "00aa1e70",
  "target": "00aa1e84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1e7c`](#insn-00aa1e7c)

~~~json
{
  "source": "00aa1e7c",
  "target": "00aa1e74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1e80`](#insn-00aa1e80)

~~~json
{
  "source": "00aa1e80",
  "target": "00aa1de8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1e94`](#insn-00aa1e94)

~~~json
{
  "source": "00aa1e94",
  "target": "00aa1e84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1e98`](#insn-00aa1e98)

~~~json
{
  "source": "00aa1e98",
  "target": "00aa1de8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1ea0`](#insn-00aa1ea0)

~~~json
{
  "source": "00aa1ea0",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1ea8`](#insn-00aa1ea8)

~~~json
{
  "source": "00aa1ea8",
  "target": "00aa1ec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1eac`](#insn-00aa1eac)

~~~json
{
  "source": "00aa1eac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1eb0`](#insn-00aa1eb0)

~~~json
{
  "source": "00aa1eb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1eb4`](#insn-00aa1eb4)

~~~json
{
  "source": "00aa1eb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1eb8`](#insn-00aa1eb8)

~~~json
{
  "source": "00aa1eb8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1ec4`](#insn-00aa1ec4)

~~~json
{
  "source": "00aa1ec4",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
