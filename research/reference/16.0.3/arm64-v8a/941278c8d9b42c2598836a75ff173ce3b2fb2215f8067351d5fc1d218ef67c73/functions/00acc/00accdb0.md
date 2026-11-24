# 00accdb0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acbdbc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acbdbc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-548099bb1380129798ae0dd8e9896dc3)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00accdb0",
  "name": "FUN_00accdb0",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a913480e9ec37ca6678394d680ed3ef69d2f88e98a9742ed7b53a230e49c8f1e",
  "source_text_sha256": "a913480e9ec37ca6678394d680ed3ef69d2f88e98a9742ed7b53a230e49c8f1e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00accdb0",
        "00accedb"
      ],
      [
        "00accf00",
        "00accf03"
      ]
    ],
    "bytes_sha256": "8ae9af626bc9bb43252b7a4975efb5bc338ce9dc02f62ffe9c2fae1b5a2a479b",
    "instruction_count": 76,
    "instruction_bytes": 304,
    "body_bytes": 304,
    "indirect": 2,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [009366b0](../00936/009366b0.md)

## 呼び出し先

- [00acd0dc](../00acd/00acd0dc.md)
- [00acd134](../00acd/00acd134.md)
- [00c54d60](../00c54/00c54d60.md)
- [00c54d90](../00c54/00c54d90.md)
- [00c58f20](../00c58/00c58f20.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f80](../00c58/00c58f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1437 bytes

~~~c

void FUN_00accdb0(long param_1,long *param_2)

{
  long lVar1;
  long *plVar2;
  long lVar3;
  long *plVar4;
  long *plVar5;
  long lVar6;
  
  lVar1 = tpidr_el0;
  lVar3 = *(long *)(lVar1 + 0x28);
  lVar6 = *param_2;
  plVar2 = (long *)_Znwm(0x20);
  *plVar2 = (long)&PTR__ZNSt6__ndk119__shared_weak_countD1Ev_00c8e990;
  plVar4 = plVar2 + 1;
  *plVar4 = 0;
  plVar2[2] = 0;
  plVar2[3] = param_1;
  FUN_00c54d60(1,plVar4);
  plVar5 = *(long **)(lVar6 + 0x38);
  *(long *)(lVar6 + 0x30) = param_1;
  *(long **)(lVar6 + 0x38) = plVar2;
  if ((plVar5 != (long *)0x0) && (lVar6 = FUN_00c54d90(0xffffffffffffffff,plVar5 + 1), lVar6 == 0))
  {
    (**(code **)(*plVar5 + 0x10))(plVar5);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar5);
  }
  lVar6 = FUN_00c54d90(0xffffffffffffffff,plVar4);
  if (lVar6 == 0) {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = *(long **)(param_1 + 0x48);
  if (plVar2 < *(long **)(param_1 + 0x50)) {
    lVar6 = param_2[1];
    *plVar2 = *param_2;
    plVar2[1] = lVar6;
    if (lVar6 != 0) {
      FUN_00c54d60(1,lVar6 + 8);
    }
    plVar2 = plVar2 + 2;
  }
  else {
    plVar2 = (long *)FUN_00acd134(param_1 + 0x40,param_2);
  }
  *(long **)(param_1 + 0x48) = plVar2;
  if (*(long *)(lVar1 + 0x28) == lVar3) {
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
<a id="insn-00accdb0"></a> `00accdb0` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00accdb4"></a> `00accdb4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00accdb8"></a> `00accdb8` | `f9 13 00 f9` | str x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00accdbc"></a> `00accdbc` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00accdc0"></a> `00accdc0` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00accdc4"></a> `00accdc4` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00accdc8"></a> `00accdc8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00accdcc"></a> `00accdcc` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00accdd0"></a> `00accdd0` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00accdd4"></a> `00accdd4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00accdd8"></a> `00accdd8` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00accddc"></a> `00accddc` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00accde0"></a> `00accde0` | `39 00 40 f9` | ldr x25,[x1] | `FALL_THROUGH`
<a id="insn-00accde4"></a> `00accde4` | `e0 03 00 f9` | str x0,[sp] | `FALL_THROUGH`
<a id="insn-00accde8"></a> `00accde8` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00accdec"></a> `00accdec` | `51 30 06 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00accdf0"></a> `00accdf0` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00accdf4"></a> `00accdf4` | `08 0e 00 d0` | adrp x8,0xc8e000 | `FALL_THROUGH`
<a id="insn-00accdf8"></a> `00accdf8` | `08 41 26 91` | add x8,x8,#0x990 | `FALL_THROUGH`
<a id="insn-00accdfc"></a> `00accdfc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00acce00"></a> `00acce00` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00acce04"></a> `00acce04` | `df 8e 00 f8` | str xzr,[x22, #0x8]! | `FALL_THROUGH`
<a id="insn-00acce08"></a> `00acce08` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00acce0c"></a> `00acce0c` | `1f 4c 01 a9` | stp xzr,x19,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00acce10"></a> `00acce10` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00acce14"></a> `00acce14` | `d3 1f 06 94` | bl 0x00c54d60 | `UNCONDITIONAL_CALL`
<a id="insn-00acce18"></a> `00acce18` | `37 1f 40 f9` | ldr x23,[x25, #0x38] | `FALL_THROUGH`
<a id="insn-00acce1c"></a> `00acce1c` | `33 57 03 a9` | stp x19,x21,[x25, #0x30] | `FALL_THROUGH`
<a id="insn-00acce20"></a> `00acce20` | `77 01 00 b4` | cbz x23,0x00acce4c | `CONDITIONAL_JUMP`
<a id="insn-00acce24"></a> `00acce24` | `e1 22 00 91` | add x1,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00acce28"></a> `00acce28` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acce2c"></a> `00acce2c` | `d9 1f 06 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-00acce30"></a> `00acce30` | `e0 00 00 b5` | cbnz x0,0x00acce4c | `CONDITIONAL_JUMP`
<a id="insn-00acce34"></a> `00acce34` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00acce38"></a> `00acce38` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00acce3c"></a> `00acce3c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acce40"></a> `00acce40` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acce44"></a> `00acce44` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00acce48"></a> `00acce48` | `36 30 06 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-00acce4c"></a> `00acce4c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acce50"></a> `00acce50` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00acce54"></a> `00acce54` | `cf 1f 06 94` | bl 0x00c54d90 | `UNCONDITIONAL_CALL`
<a id="insn-00acce58"></a> `00acce58` | `e0 00 00 b5` | cbnz x0,0x00acce74 | `CONDITIONAL_JUMP`
<a id="insn-00acce5c"></a> `00acce5c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00acce60"></a> `00acce60` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00acce64"></a> `00acce64` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acce68"></a> `00acce68` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acce6c"></a> `00acce6c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00acce70"></a> `00acce70` | `2c 30 06 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-00acce74"></a> `00acce74` | `75 a2 44 a9` | ldp x21,x8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00acce78"></a> `00acce78` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00acce7c"></a> `00acce7c` | `22 01 00 54` | b.cs 0x00accea0 | `CONDITIONAL_JUMP`
<a id="insn-00acce80"></a> `00acce80` | `89 22 40 a9` | ldp x9,x8,[x20] | `FALL_THROUGH`
<a id="insn-00acce84"></a> `00acce84` | `a9 22 00 a9` | stp x9,x8,[x21] | `FALL_THROUGH`
<a id="insn-00acce88"></a> `00acce88` | `88 00 00 b4` | cbz x8,0x00acce98 | `CONDITIONAL_JUMP`
<a id="insn-00acce8c"></a> `00acce8c` | `01 21 00 91` | add x1,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00acce90"></a> `00acce90` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00acce94"></a> `00acce94` | `b3 1f 06 94` | bl 0x00c54d60 | `UNCONDITIONAL_CALL`
<a id="insn-00acce98"></a> `00acce98` | `a0 42 00 91` | add x0,x21,#0x10 | `FALL_THROUGH`
<a id="insn-00acce9c"></a> `00acce9c` | `04 00 00 14` | b 0x00acceac | `UNCONDITIONAL_JUMP`
<a id="insn-00accea0"></a> `00accea0` | `60 02 01 91` | add x0,x19,#0x40 | `FALL_THROUGH`
<a id="insn-00accea4"></a> `00accea4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00accea8"></a> `00accea8` | `a3 00 00 94` | bl 0x00acd134 | `UNCONDITIONAL_CALL`
<a id="insn-00acceac"></a> `00acceac` | `60 26 00 f9` | str x0,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00acceb0"></a> `00acceb0` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00acceb4"></a> `00acceb4` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acceb8"></a> `00acceb8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00accebc"></a> `00accebc` | `21 02 00 54` | b.ne 0x00accf00 | `CONDITIONAL_JUMP`
<a id="insn-00accec0"></a> `00accec0` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00accec4"></a> `00accec4` | `f9 13 40 f9` | ldr x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00accec8"></a> `00accec8` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00accecc"></a> `00accecc` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acced0"></a> `00acced0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acced4"></a> `00acced4` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acced8"></a> `00acced8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00accf00"></a> `00accf00` | `20 30 06 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00accdb0`](#insn-00accdb0) 範囲 `[['00accdb0', '00acce23']]`
  - `CONDITIONAL_JUMP` [`00acce20`](#insn-00acce20) → [`00acce4c`](#insn-00acce4c)
  - `FALL_THROUGH` [`00acce20`](#insn-00acce20) → [`00acce24`](#insn-00acce24)
- ブロック [`00acce24`](#insn-00acce24) 範囲 `[['00acce24', '00acce33']]`
  - `CONDITIONAL_JUMP` [`00acce30`](#insn-00acce30) → [`00acce4c`](#insn-00acce4c)
  - `FALL_THROUGH` [`00acce30`](#insn-00acce30) → [`00acce34`](#insn-00acce34)
- ブロック [`00acce34`](#insn-00acce34) 範囲 `[['00acce34', '00acce4b']]`
  - `FALL_THROUGH` [`00acce48`](#insn-00acce48) → [`00acce4c`](#insn-00acce4c)
- ブロック [`00acce4c`](#insn-00acce4c) 範囲 `[['00acce4c', '00acce5b']]`
  - `CONDITIONAL_JUMP` [`00acce58`](#insn-00acce58) → [`00acce74`](#insn-00acce74)
  - `FALL_THROUGH` [`00acce58`](#insn-00acce58) → [`00acce5c`](#insn-00acce5c)
- ブロック [`00acce5c`](#insn-00acce5c) 範囲 `[['00acce5c', '00acce73']]`
  - `FALL_THROUGH` [`00acce70`](#insn-00acce70) → [`00acce74`](#insn-00acce74)
- ブロック [`00acce74`](#insn-00acce74) 範囲 `[['00acce74', '00acce7f']]`
  - `CONDITIONAL_JUMP` [`00acce7c`](#insn-00acce7c) → [`00accea0`](#insn-00accea0)
  - `FALL_THROUGH` [`00acce7c`](#insn-00acce7c) → [`00acce80`](#insn-00acce80)
- ブロック [`00acce80`](#insn-00acce80) 範囲 `[['00acce80', '00acce8b']]`
  - `CONDITIONAL_JUMP` [`00acce88`](#insn-00acce88) → [`00acce98`](#insn-00acce98)
  - `FALL_THROUGH` [`00acce88`](#insn-00acce88) → [`00acce8c`](#insn-00acce8c)
- ブロック [`00acce8c`](#insn-00acce8c) 範囲 `[['00acce8c', '00acce97']]`
  - `FALL_THROUGH` [`00acce94`](#insn-00acce94) → [`00acce98`](#insn-00acce98)
- ブロック [`00acce98`](#insn-00acce98) 範囲 `[['00acce98', '00acce9f']]`
  - `UNCONDITIONAL_JUMP` [`00acce9c`](#insn-00acce9c) → [`00acceac`](#insn-00acceac)
- ブロック [`00accea0`](#insn-00accea0) 範囲 `[['00accea0', '00acceab']]`
  - `FALL_THROUGH` [`00accea8`](#insn-00accea8) → [`00acceac`](#insn-00acceac)
- ブロック [`00acceac`](#insn-00acceac) 範囲 `[['00acceac', '00accebf']]`
  - `CONDITIONAL_JUMP` [`00accebc`](#insn-00accebc) → [`00accf00`](#insn-00accf00)
  - `FALL_THROUGH` [`00accebc`](#insn-00accebc) → [`00accec0`](#insn-00accec0)
- ブロック [`00accec0`](#insn-00accec0) 範囲 `[['00accec0', '00accedb']]`
- ブロック [`00accf00`](#insn-00accf00) 範囲 `[['00accf00', '00accf03']]`

## 命令位置別の参照

- [`00accdb4`](#insn-00accdb4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accdb8`](#insn-00accdb8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accdbc`](#insn-00accdbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accdc0`](#insn-00accdc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accdc4`](#insn-00accdc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accddc`](#insn-00accddc) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accde4`](#insn-00accde4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accdec`](#insn-00accdec) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00acce00`](#insn-00acce00) → `00c8e990`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acce14`](#insn-00acce14) → [`00c54d60`](../00c54/00c54d60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d60` · 推定シンボル `None` · 推定型 `None`
- [`00acce20`](#insn-00acce20) → [`00acce4c`](#insn-00acce4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acce2c`](#insn-00acce2c) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`00acce30`](#insn-00acce30) → [`00acce4c`](#insn-00acce4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acce48`](#insn-00acce48) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`00acce54`](#insn-00acce54) → [`00c54d90`](../00c54/00c54d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d90` · 推定シンボル `None` · 推定型 `None`
- [`00acce58`](#insn-00acce58) → [`00acce74`](#insn-00acce74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acce64`](#insn-00acce64) → `00c8e9a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00acce68`](#insn-00acce68) → [`00acd0dc`](../00acd/00acd0dc.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00acd0dc` · 推定シンボル `None` · 推定型 `None`
- [`00acce70`](#insn-00acce70) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`00acce7c`](#insn-00acce7c) → [`00accea0`](#insn-00accea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acce88`](#insn-00acce88) → [`00acce98`](#insn-00acce98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acce94`](#insn-00acce94) → [`00c54d60`](../00c54/00c54d60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54d60` · 推定シンボル `None` · 推定型 `None`
- [`00acce9c`](#insn-00acce9c) → [`00acceac`](#insn-00acceac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accea8`](#insn-00accea8) → [`00acd134`](../00acd/00acd134.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00acd134` · 推定シンボル `None` · 推定型 `None`
- [`00acceb4`](#insn-00acceb4) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accebc`](#insn-00accebc) → [`00accf00`](#insn-00accf00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accec0`](#insn-00accec0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accec4`](#insn-00accec4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accec8`](#insn-00accec8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accecc`](#insn-00accecc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acced0`](#insn-00acced0) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00accf00`](#insn-00accf00) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00accdb4`](#insn-00accdb4)

~~~json
{
  "source": "00accdb4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accdb8`](#insn-00accdb8)

~~~json
{
  "source": "00accdb8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accdbc`](#insn-00accdbc)

~~~json
{
  "source": "00accdbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accdc0`](#insn-00accdc0)

~~~json
{
  "source": "00accdc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accdc4`](#insn-00accdc4)

~~~json
{
  "source": "00accdc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accddc`](#insn-00accddc)

~~~json
{
  "source": "00accddc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accde4`](#insn-00accde4)

~~~json
{
  "source": "00accde4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accdec`](#insn-00accdec)

~~~json
{
  "source": "00accdec",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acce00`](#insn-00acce00)

~~~json
{
  "source": "00acce00",
  "target": "00c8e990",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8e990",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acce14`](#insn-00acce14)

~~~json
{
  "source": "00acce14",
  "target": "00c54d60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acce20`](#insn-00acce20)

~~~json
{
  "source": "00acce20",
  "target": "00acce4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acce2c`](#insn-00acce2c)

~~~json
{
  "source": "00acce2c",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acce30`](#insn-00acce30)

~~~json
{
  "source": "00acce30",
  "target": "00acce4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acce48`](#insn-00acce48)

~~~json
{
  "source": "00acce48",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acce54`](#insn-00acce54)

~~~json
{
  "source": "00acce54",
  "target": "00c54d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acce58`](#insn-00acce58)

~~~json
{
  "source": "00acce58",
  "target": "00acce74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acce64`](#insn-00acce64)

~~~json
{
  "source": "00acce64",
  "target": "00c8e9a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8e9a0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acce68`](#insn-00acce68)

~~~json
{
  "source": "00acce68",
  "target": "00acd0dc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acce70`](#insn-00acce70)

~~~json
{
  "source": "00acce70",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acce7c`](#insn-00acce7c)

~~~json
{
  "source": "00acce7c",
  "target": "00accea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acce88`](#insn-00acce88)

~~~json
{
  "source": "00acce88",
  "target": "00acce98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acce94`](#insn-00acce94)

~~~json
{
  "source": "00acce94",
  "target": "00c54d60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acce9c`](#insn-00acce9c)

~~~json
{
  "source": "00acce9c",
  "target": "00acceac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accea8`](#insn-00accea8)

~~~json
{
  "source": "00accea8",
  "target": "00acd134",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acceb4`](#insn-00acceb4)

~~~json
{
  "source": "00acceb4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accebc`](#insn-00accebc)

~~~json
{
  "source": "00accebc",
  "target": "00accf00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accec0`](#insn-00accec0)

~~~json
{
  "source": "00accec0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accec4`](#insn-00accec4)

~~~json
{
  "source": "00accec4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accec8`](#insn-00accec8)

~~~json
{
  "source": "00accec8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accecc`](#insn-00accecc)

~~~json
{
  "source": "00accecc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acced0`](#insn-00acced0)

~~~json
{
  "source": "00acced0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00accf00`](#insn-00accf00)

~~~json
{
  "source": "00accf00",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
