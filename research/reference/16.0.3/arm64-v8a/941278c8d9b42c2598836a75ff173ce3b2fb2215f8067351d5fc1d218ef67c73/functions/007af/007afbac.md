# 007afbac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `007af188`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007af/007af188.md) · 移動量 `+0xa24`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0040.md#compare-26a50b73db46d8d412caf5eadb5e1edf)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007afbac",
  "name": "FUN_007afbac",
  "size": 308,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "881d8eef944a5304589298d5b50318822f0f9ddee785d7c1e4e930c88d5b646e",
  "source_text_sha256": "881d8eef944a5304589298d5b50318822f0f9ddee785d7c1e4e930c88d5b646e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007afbac",
        "007afcdb"
      ],
      [
        "007afd20",
        "007afd23"
      ]
    ],
    "bytes_sha256": "316138a4da699ae89d8efd55c1c7744bd0a6e3de0502906ab9d998093450edc0",
    "instruction_count": 77,
    "instruction_bytes": 308,
    "body_bytes": 308,
    "indirect": 2,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [007abbbc](../007ab/007abbbc.md)

## 呼び出し先

- [00598230](../00598/00598230.md)
- [005b772c](../005b7/005b772c.md)
- [00c54d60](../00c54/00c54d60.md)
- [00c54d90](../00c54/00c54d90.md)
- [00c58f20](../00c58/00c58f20.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f80](../00c58/00c58f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1402 bytes

~~~c

void FUN_007afbac(long *param_1,undefined8 param_2,undefined8 *param_3)

{
  long *plVar1;
  long lVar2;
  long *plVar3;
  long *plVar4;
  long lVar5;
  long *local_50;
  long local_48;
  
  lVar2 = tpidr_el0;
  local_48 = *(long *)(lVar2 + 0x28);
  plVar4 = (long *)_Znwm(0xb0);
  *plVar4 = (long)&PTR_FUN_00c71660;
  local_50 = (long *)*param_3;
  *param_3 = 0;
  plVar1 = plVar4 + 4;
  plVar4[2] = 0;
  plVar4[1] = 0;
  FUN_00598230(plVar1,&local_50);
  plVar3 = local_50;
  local_50 = (long *)0x0;
  if (plVar3 != (long *)0x0) {
    (**(code **)(*plVar3 + 8))();
  }
  lVar5 = plVar4[6];
  *param_1 = (long)plVar1;
  param_1[1] = (long)plVar4;
  if (lVar5 == 0) {
    FUN_00c54d60(1,plVar4 + 1);
    FUN_00c54d60(1,plVar4 + 2);
    plVar4[5] = (long)plVar1;
    plVar4[6] = (long)plVar4;
  }
  else {
    if (*(long *)(lVar5 + 8) != -1) goto LAB_007afcb4;
    FUN_00c54d60(1,plVar4 + 1);
    FUN_00c54d60(1,plVar4 + 2);
    plVar4[5] = (long)plVar1;
    plVar4[6] = (long)plVar4;
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(lVar5);
  }
  lVar5 = FUN_00c54d90(0xffffffffffffffff,plVar4 + 1);
  if (lVar5 == 0) {
    (**(code **)(*plVar4 + 0x10))(plVar4);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
  }
LAB_007afcb4:
  if (*(long *)(lVar2 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007afbac"></a> `007afbac` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-007afbb0"></a> `007afbb0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007afbb4"></a> `007afbb4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007afbb8"></a> `007afbb8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007afbbc"></a> `007afbbc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-007afbc0"></a> `007afbc0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-007afbc4"></a> `007afbc4` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-007afbc8"></a> `007afbc8` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-007afbcc"></a> `007afbcc` | `00 16 80 52` | mov w0,#0xb0 | `FALL_THROUGH`
<a id="insn-007afbd0"></a> `007afbd0` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-007afbd4"></a> `007afbd4` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-007afbd8"></a> `007afbd8` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-007afbdc"></a> `007afbdc` | `d5 a4 12 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-007afbe0"></a> `007afbe0` | `08 26 00 d0` | adrp x8,0xc71000 | `FALL_THROUGH`
<a id="insn-007afbe4"></a> `007afbe4` | `08 81 19 91` | add x8,x8,#0x660 | `FALL_THROUGH`
<a id="insn-007afbe8"></a> `007afbe8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-007afbec"></a> `007afbec` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-007afbf0"></a> `007afbf0` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-007afbf4"></a> `007afbf4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-007afbf8"></a> `007afbf8` | `bf 02 00 f9` | str xzr,[x21] | `FALL_THROUGH`
<a id="insn-007afbfc"></a> `007afbfc` | `15 80 00 91` | add x21,x0,#0x20 | `FALL_THROUGH`
<a id="insn-007afc00"></a> `007afc00` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-007afc04"></a> `007afc04` | `9f 8e 00 f8` | str xzr,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-007afc08"></a> `007afc08` | `e8 03 00 f9` | str x8,[sp] | `FALL_THROUGH`
<a id="insn-007afc0c"></a> `007afc0c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-007afc10"></a> `007afc10` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-007afc14"></a> `007afc14` | `87 a1 f7 97` | bl 0x00598230 | `UNCONDITIONAL_CALL`
<a id="insn-007afc18"></a> `007afc18` | `e0 03 40 f9` | ldr x0,[sp] | `FALL_THROUGH`
<a id="insn-007afc1c"></a> `007afc1c` | `ff 03 00 f9` | str xzr,[sp] | `FALL_THROUGH`
<a id="insn-007afc20"></a> `007afc20` | `80 00 00 b4` | cbz x0,0x007afc30 | `CONDITIONAL_JUMP`
<a id="insn-007afc24"></a> `007afc24` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-007afc28"></a> `007afc28` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-007afc2c"></a> `007afc2c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007afc30"></a> `007afc30` | `77 1a 40 f9` | ldr x23,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-007afc34"></a> `007afc34` | `d5 4e 00 a9` | stp x21,x19,[x22] | `FALL_THROUGH`
<a id="insn-007afc38"></a> `007afc38` | `d7 01 00 b4` | cbz x23,0x007afc70 | `CONDITIONAL_JUMP`
<a id="insn-007afc3c"></a> `007afc3c` | `e8 06 40 f9` | ldr x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-007afc40"></a> `007afc40` | `1f 05 00 b1` | cmn x8,#0x1 | `FALL_THROUGH`
<a id="insn-007afc44"></a> `007afc44` | `81 03 00 54` | b.ne 0x007afcb4 | `CONDITIONAL_JUMP`
<a id="insn-007afc48"></a> `007afc48` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-007afc4c"></a> `007afc4c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-007afc50"></a> `007afc50` | `44 94 12 94` | bl 0x00c54d60 | `UNCONDITIONAL_CALL`
<a id="insn-007afc54"></a> `007afc54` | `61 42 00 91` | add x1,x19,#0x10 | `FALL_THROUGH`
<a id="insn-007afc58"></a> `007afc58` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-007afc5c"></a> `007afc5c` | `41 94 12 94` | bl 0x00c54d60 | `UNCONDITIONAL_CALL`
<a id="insn-007afc60"></a> `007afc60` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-007afc64"></a> `007afc64` | `75 ce 02 a9` | stp x21,x19,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-007afc68"></a> `007afc68` | `ae a4 12 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-007afc6c"></a> `007afc6c` | `08 00 00 14` | b 0x007afc8c | `UNCONDITIONAL_JUMP`
<a id="insn-007afc70"></a> `007afc70` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-007afc74"></a> `007afc74` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-007afc78"></a> `007afc78` | `3a 94 12 94` | bl 0x00c54d60 | `UNCONDITIONAL_CALL`
<a id="insn-007afc7c"></a> `007afc7c` | `61 42 00 91` | add x1,x19,#0x10 | `FALL_THROUGH`
<a id="insn-007afc80"></a> `007afc80` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-007afc84"></a> `007afc84` | `37 94 12 94` | bl 0x00c54d60 | `UNCONDITIONAL_CALL`
<a id="insn-007afc88"></a> `007afc88` | `75 ce 02 a9` | stp x21,x19,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-007afc8c"></a> `007afc8c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-007afc90"></a> `007afc90` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-007afc94"></a> `007afc94` | `3f 94 12 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-007afc98"></a> `007afc98` | `e0 00 00 b5` | cbnz x0,0x007afcb4 | `CONDITIONAL_JUMP`
<a id="insn-007afc9c"></a> `007afc9c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-007afca0"></a> `007afca0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007afca4"></a> `007afca4` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-007afca8"></a> `007afca8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007afcac"></a> `007afcac` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007afcb0"></a> `007afcb0` | `9c a4 12 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-007afcb4"></a> `007afcb4` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-007afcb8"></a> `007afcb8` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-007afcbc"></a> `007afcbc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-007afcc0"></a> `007afcc0` | `01 03 00 54` | b.ne 0x007afd20 | `CONDITIONAL_JUMP`
<a id="insn-007afcc4"></a> `007afcc4` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-007afcc8"></a> `007afcc8` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007afccc"></a> `007afccc` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007afcd0"></a> `007afcd0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007afcd4"></a> `007afcd4` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-007afcd8"></a> `007afcd8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-007afd20"></a> `007afd20` | `98 a4 12 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007afbac`](#insn-007afbac) 範囲 `[['007afbac', '007afc23']]`
  - `CONDITIONAL_JUMP` [`007afc20`](#insn-007afc20) → [`007afc30`](#insn-007afc30)
  - `FALL_THROUGH` [`007afc20`](#insn-007afc20) → [`007afc24`](#insn-007afc24)
- ブロック [`007afc24`](#insn-007afc24) 範囲 `[['007afc24', '007afc2f']]`
  - `FALL_THROUGH` [`007afc2c`](#insn-007afc2c) → [`007afc30`](#insn-007afc30)
- ブロック [`007afc30`](#insn-007afc30) 範囲 `[['007afc30', '007afc3b']]`
  - `CONDITIONAL_JUMP` [`007afc38`](#insn-007afc38) → [`007afc70`](#insn-007afc70)
  - `FALL_THROUGH` [`007afc38`](#insn-007afc38) → [`007afc3c`](#insn-007afc3c)
- ブロック [`007afc3c`](#insn-007afc3c) 範囲 `[['007afc3c', '007afc47']]`
  - `CONDITIONAL_JUMP` [`007afc44`](#insn-007afc44) → [`007afcb4`](#insn-007afcb4)
  - `FALL_THROUGH` [`007afc44`](#insn-007afc44) → [`007afc48`](#insn-007afc48)
- ブロック [`007afc48`](#insn-007afc48) 範囲 `[['007afc48', '007afc6f']]`
  - `UNCONDITIONAL_JUMP` [`007afc6c`](#insn-007afc6c) → [`007afc8c`](#insn-007afc8c)
- ブロック [`007afc70`](#insn-007afc70) 範囲 `[['007afc70', '007afc8b']]`
  - `FALL_THROUGH` [`007afc88`](#insn-007afc88) → [`007afc8c`](#insn-007afc8c)
- ブロック [`007afc8c`](#insn-007afc8c) 範囲 `[['007afc8c', '007afc9b']]`
  - `CONDITIONAL_JUMP` [`007afc98`](#insn-007afc98) → [`007afcb4`](#insn-007afcb4)
  - `FALL_THROUGH` [`007afc98`](#insn-007afc98) → [`007afc9c`](#insn-007afc9c)
- ブロック [`007afc9c`](#insn-007afc9c) 範囲 `[['007afc9c', '007afcb3']]`
  - `FALL_THROUGH` [`007afcb0`](#insn-007afcb0) → [`007afcb4`](#insn-007afcb4)
- ブロック [`007afcb4`](#insn-007afcb4) 範囲 `[['007afcb4', '007afcc3']]`
  - `CONDITIONAL_JUMP` [`007afcc0`](#insn-007afcc0) → [`007afd20`](#insn-007afd20)
  - `FALL_THROUGH` [`007afcc0`](#insn-007afcc0) → [`007afcc4`](#insn-007afcc4)
- ブロック [`007afcc4`](#insn-007afcc4) 範囲 `[['007afcc4', '007afcdb']]`
- ブロック [`007afd20`](#insn-007afd20) 範囲 `[['007afd20', '007afd23']]`

## 命令位置別の参照

- [`007afbb0`](#insn-007afbb0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afbb4`](#insn-007afbb4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afbb8`](#insn-007afbb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afbbc`](#insn-007afbbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afbd8`](#insn-007afbd8) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afbdc`](#insn-007afbdc) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`007afbec`](#insn-007afbec) → `00c71660`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`007afc08`](#insn-007afc08) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afc14`](#insn-007afc14) → [`00598230`](../00598/00598230.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00598230` · 推定シンボル `None` · 推定型 `None`
- [`007afc18`](#insn-007afc18) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afc1c`](#insn-007afc1c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afc20`](#insn-007afc20) → [`007afc30`](#insn-007afc30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afc38`](#insn-007afc38) → [`007afc70`](#insn-007afc70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afc44`](#insn-007afc44) → [`007afcb4`](#insn-007afcb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afc50`](#insn-007afc50) → [`00c54d60`](../00c54/00c54d60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d60` · 推定シンボル `None` · 推定型 `None`
- [`007afc5c`](#insn-007afc5c) → [`00c54d60`](../00c54/00c54d60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d60` · 推定シンボル `None` · 推定型 `None`
- [`007afc68`](#insn-007afc68) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`007afc6c`](#insn-007afc6c) → [`007afc8c`](#insn-007afc8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afc78`](#insn-007afc78) → [`00c54d60`](../00c54/00c54d60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d60` · 推定シンボル `None` · 推定型 `None`
- [`007afc84`](#insn-007afc84) → [`00c54d60`](../00c54/00c54d60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d60` · 推定シンボル `None` · 推定型 `None`
- [`007afc94`](#insn-007afc94) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`007afc98`](#insn-007afc98) → [`007afcb4`](#insn-007afcb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afca4`](#insn-007afca4) → `00c71670`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007afca8`](#insn-007afca8) → [`005b772c`](../005b7/005b772c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `005b772c` · 推定シンボル `None` · 推定型 `None`
- [`007afcb0`](#insn-007afcb0) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`007afcb8`](#insn-007afcb8) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afcc0`](#insn-007afcc0) → [`007afd20`](#insn-007afd20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afcc4`](#insn-007afcc4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afcc8`](#insn-007afcc8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afccc`](#insn-007afccc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afcd0`](#insn-007afcd0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afd20`](#insn-007afd20) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007afbb0`](#insn-007afbb0)

~~~json
{
  "source": "007afbb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afbb4`](#insn-007afbb4)

~~~json
{
  "source": "007afbb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afbb8`](#insn-007afbb8)

~~~json
{
  "source": "007afbb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afbbc`](#insn-007afbbc)

~~~json
{
  "source": "007afbbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afbd8`](#insn-007afbd8)

~~~json
{
  "source": "007afbd8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afbdc`](#insn-007afbdc)

~~~json
{
  "source": "007afbdc",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007afbec`](#insn-007afbec)

~~~json
{
  "source": "007afbec",
  "target": "00c71660",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c71660",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007afc08`](#insn-007afc08)

~~~json
{
  "source": "007afc08",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afc14`](#insn-007afc14)

~~~json
{
  "source": "007afc14",
  "target": "00598230",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007afc18`](#insn-007afc18)

~~~json
{
  "source": "007afc18",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afc1c`](#insn-007afc1c)

~~~json
{
  "source": "007afc1c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afc20`](#insn-007afc20)

~~~json
{
  "source": "007afc20",
  "target": "007afc30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afc38`](#insn-007afc38)

~~~json
{
  "source": "007afc38",
  "target": "007afc70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afc44`](#insn-007afc44)

~~~json
{
  "source": "007afc44",
  "target": "007afcb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afc50`](#insn-007afc50)

~~~json
{
  "source": "007afc50",
  "target": "00c54d60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007afc5c`](#insn-007afc5c)

~~~json
{
  "source": "007afc5c",
  "target": "00c54d60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007afc68`](#insn-007afc68)

~~~json
{
  "source": "007afc68",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007afc6c`](#insn-007afc6c)

~~~json
{
  "source": "007afc6c",
  "target": "007afc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afc78`](#insn-007afc78)

~~~json
{
  "source": "007afc78",
  "target": "00c54d60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007afc84`](#insn-007afc84)

~~~json
{
  "source": "007afc84",
  "target": "00c54d60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007afc94`](#insn-007afc94)

~~~json
{
  "source": "007afc94",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007afc98`](#insn-007afc98)

~~~json
{
  "source": "007afc98",
  "target": "007afcb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afca4`](#insn-007afca4)

~~~json
{
  "source": "007afca4",
  "target": "00c71670",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c71670",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007afca8`](#insn-007afca8)

~~~json
{
  "source": "007afca8",
  "target": "005b772c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007afcb0`](#insn-007afcb0)

~~~json
{
  "source": "007afcb0",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007afcb8`](#insn-007afcb8)

~~~json
{
  "source": "007afcb8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afcc0`](#insn-007afcc0)

~~~json
{
  "source": "007afcc0",
  "target": "007afd20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afcc4`](#insn-007afcc4)

~~~json
{
  "source": "007afcc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afcc8`](#insn-007afcc8)

~~~json
{
  "source": "007afcc8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afccc`](#insn-007afccc)

~~~json
{
  "source": "007afccc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afcd0`](#insn-007afcd0)

~~~json
{
  "source": "007afcd0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afd20`](#insn-007afd20)

~~~json
{
  "source": "007afd20",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
