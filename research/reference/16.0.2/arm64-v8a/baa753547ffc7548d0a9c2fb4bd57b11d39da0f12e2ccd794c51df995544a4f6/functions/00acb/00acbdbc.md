# 00acbdbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acbd4c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acbd4c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0065.md#compare-23c957628b1360d0635b63e8a23f9ca0)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00accdb0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00accdb0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-548099bb1380129798ae0dd8e9896dc3)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbdbc",
  "name": "FUN_00acbdbc",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b39654d81be393e24180ac8826fa75989ef1ce3c74852f53e70bdf7452fe60d9",
  "source_text_sha256": "b39654d81be393e24180ac8826fa75989ef1ce3c74852f53e70bdf7452fe60d9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acbdbc",
        "00acbee7"
      ],
      [
        "00acbf0c",
        "00acbf0f"
      ]
    ],
    "bytes_sha256": "79723c19cb539fe11ef56e3891d4fe4e722c9809468281a6a544bd42b6c23e57",
    "instruction_count": 76,
    "instruction_bytes": 304,
    "body_bytes": 304,
    "indirect": 2,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00935704](../00935/00935704.md)

## 呼び出し先

- [00acc0e8](../00acc/00acc0e8.md)
- [00acc140](../00acc/00acc140.md)
- [00c53d70](../00c53/00c53d70.md)
- [00c53da0](../00c53/00c53da0.md)
- [00c57f50](../00c57/00c57f50.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57fb0](../00c57/00c57fb0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1437 bytes

~~~c

void FUN_00acbdbc(long param_1,long *param_2)

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
  *plVar2 = (long)&PTR__ZNSt6__ndk119__shared_weak_countD1Ev_00c8d9c0;
  plVar4 = plVar2 + 1;
  *plVar4 = 0;
  plVar2[2] = 0;
  plVar2[3] = param_1;
  FUN_00c53d70(1,plVar4);
  plVar5 = *(long **)(lVar6 + 0x38);
  *(long *)(lVar6 + 0x30) = param_1;
  *(long **)(lVar6 + 0x38) = plVar2;
  if ((plVar5 != (long *)0x0) && (lVar6 = FUN_00c53da0(0xffffffffffffffff,plVar5 + 1), lVar6 == 0))
  {
    (**(code **)(*plVar5 + 0x10))(plVar5);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar5);
  }
  lVar6 = FUN_00c53da0(0xffffffffffffffff,plVar4);
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
      FUN_00c53d70(1,lVar6 + 8);
    }
    plVar2 = plVar2 + 2;
  }
  else {
    plVar2 = (long *)FUN_00acc140(param_1 + 0x40,param_2);
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
<a id="insn-00acbdbc"></a> `00acbdbc` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acbdc0"></a> `00acbdc0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acbdc4"></a> `00acbdc4` | `f9 13 00 f9` | str x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acbdc8"></a> `00acbdc8` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acbdcc"></a> `00acbdcc` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acbdd0"></a> `00acbdd0` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acbdd4"></a> `00acbdd4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00acbdd8"></a> `00acbdd8` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acbddc"></a> `00acbddc` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00acbde0"></a> `00acbde0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acbde4"></a> `00acbde4` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00acbde8"></a> `00acbde8` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acbdec"></a> `00acbdec` | `39 00 40 f9` | ldr x25,[x1] | `FALL_THROUGH`
<a id="insn-00acbdf0"></a> `00acbdf0` | `e0 03 00 f9` | str x0,[sp] | `FALL_THROUGH`
<a id="insn-00acbdf4"></a> `00acbdf4` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00acbdf8"></a> `00acbdf8` | `5a 30 06 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00acbdfc"></a> `00acbdfc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00acbe00"></a> `00acbe00` | `08 0e 00 d0` | adrp x8,0xc8d000 | `FALL_THROUGH`
<a id="insn-00acbe04"></a> `00acbe04` | `08 01 27 91` | add x8,x8,#0x9c0 | `FALL_THROUGH`
<a id="insn-00acbe08"></a> `00acbe08` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00acbe0c"></a> `00acbe0c` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00acbe10"></a> `00acbe10` | `df 8e 00 f8` | str xzr,[x22, #0x8]! | `FALL_THROUGH`
<a id="insn-00acbe14"></a> `00acbe14` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00acbe18"></a> `00acbe18` | `1f 4c 01 a9` | stp xzr,x19,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00acbe1c"></a> `00acbe1c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00acbe20"></a> `00acbe20` | `d4 1f 06 94` | bl 0x00c53d70 | `UNCONDITIONAL_CALL`
<a id="insn-00acbe24"></a> `00acbe24` | `37 1f 40 f9` | ldr x23,[x25, #0x38] | `FALL_THROUGH`
<a id="insn-00acbe28"></a> `00acbe28` | `33 57 03 a9` | stp x19,x21,[x25, #0x30] | `FALL_THROUGH`
<a id="insn-00acbe2c"></a> `00acbe2c` | `77 01 00 b4` | cbz x23,0x00acbe58 | `CONDITIONAL_JUMP`
<a id="insn-00acbe30"></a> `00acbe30` | `e1 22 00 91` | add x1,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00acbe34"></a> `00acbe34` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acbe38"></a> `00acbe38` | `da 1f 06 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-00acbe3c"></a> `00acbe3c` | `e0 00 00 b5` | cbnz x0,0x00acbe58 | `CONDITIONAL_JUMP`
<a id="insn-00acbe40"></a> `00acbe40` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00acbe44"></a> `00acbe44` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00acbe48"></a> `00acbe48` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acbe4c"></a> `00acbe4c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbe50"></a> `00acbe50` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00acbe54"></a> `00acbe54` | `3f 30 06 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-00acbe58"></a> `00acbe58` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acbe5c"></a> `00acbe5c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00acbe60"></a> `00acbe60` | `d0 1f 06 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-00acbe64"></a> `00acbe64` | `e0 00 00 b5` | cbnz x0,0x00acbe80 | `CONDITIONAL_JUMP`
<a id="insn-00acbe68"></a> `00acbe68` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00acbe6c"></a> `00acbe6c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00acbe70"></a> `00acbe70` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acbe74"></a> `00acbe74` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbe78"></a> `00acbe78` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00acbe7c"></a> `00acbe7c` | `35 30 06 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-00acbe80"></a> `00acbe80` | `75 a2 44 a9` | ldp x21,x8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00acbe84"></a> `00acbe84` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00acbe88"></a> `00acbe88` | `22 01 00 54` | b.cs 0x00acbeac | `CONDITIONAL_JUMP`
<a id="insn-00acbe8c"></a> `00acbe8c` | `89 22 40 a9` | ldp x9,x8,[x20] | `FALL_THROUGH`
<a id="insn-00acbe90"></a> `00acbe90` | `a9 22 00 a9` | stp x9,x8,[x21] | `FALL_THROUGH`
<a id="insn-00acbe94"></a> `00acbe94` | `88 00 00 b4` | cbz x8,0x00acbea4 | `CONDITIONAL_JUMP`
<a id="insn-00acbe98"></a> `00acbe98` | `01 21 00 91` | add x1,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00acbe9c"></a> `00acbe9c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00acbea0"></a> `00acbea0` | `b4 1f 06 94` | bl 0x00c53d70 | `UNCONDITIONAL_CALL`
<a id="insn-00acbea4"></a> `00acbea4` | `a0 42 00 91` | add x0,x21,#0x10 | `FALL_THROUGH`
<a id="insn-00acbea8"></a> `00acbea8` | `04 00 00 14` | b 0x00acbeb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00acbeac"></a> `00acbeac` | `60 02 01 91` | add x0,x19,#0x40 | `FALL_THROUGH`
<a id="insn-00acbeb0"></a> `00acbeb0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00acbeb4"></a> `00acbeb4` | `a3 00 00 94` | bl 0x00acc140 | `UNCONDITIONAL_CALL`
<a id="insn-00acbeb8"></a> `00acbeb8` | `60 26 00 f9` | str x0,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00acbebc"></a> `00acbebc` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00acbec0"></a> `00acbec0` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acbec4"></a> `00acbec4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acbec8"></a> `00acbec8` | `21 02 00 54` | b.ne 0x00acbf0c | `CONDITIONAL_JUMP`
<a id="insn-00acbecc"></a> `00acbecc` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acbed0"></a> `00acbed0` | `f9 13 40 f9` | ldr x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acbed4"></a> `00acbed4` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acbed8"></a> `00acbed8` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acbedc"></a> `00acbedc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acbee0"></a> `00acbee0` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acbee4"></a> `00acbee4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acbf0c"></a> `00acbf0c` | `29 30 06 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acbdbc`](#insn-00acbdbc) 範囲 `[['00acbdbc', '00acbe2f']]`
  - `CONDITIONAL_JUMP` [`00acbe2c`](#insn-00acbe2c) → [`00acbe58`](#insn-00acbe58)
  - `FALL_THROUGH` [`00acbe2c`](#insn-00acbe2c) → [`00acbe30`](#insn-00acbe30)
- ブロック [`00acbe30`](#insn-00acbe30) 範囲 `[['00acbe30', '00acbe3f']]`
  - `CONDITIONAL_JUMP` [`00acbe3c`](#insn-00acbe3c) → [`00acbe58`](#insn-00acbe58)
  - `FALL_THROUGH` [`00acbe3c`](#insn-00acbe3c) → [`00acbe40`](#insn-00acbe40)
- ブロック [`00acbe40`](#insn-00acbe40) 範囲 `[['00acbe40', '00acbe57']]`
  - `FALL_THROUGH` [`00acbe54`](#insn-00acbe54) → [`00acbe58`](#insn-00acbe58)
- ブロック [`00acbe58`](#insn-00acbe58) 範囲 `[['00acbe58', '00acbe67']]`
  - `CONDITIONAL_JUMP` [`00acbe64`](#insn-00acbe64) → [`00acbe80`](#insn-00acbe80)
  - `FALL_THROUGH` [`00acbe64`](#insn-00acbe64) → [`00acbe68`](#insn-00acbe68)
- ブロック [`00acbe68`](#insn-00acbe68) 範囲 `[['00acbe68', '00acbe7f']]`
  - `FALL_THROUGH` [`00acbe7c`](#insn-00acbe7c) → [`00acbe80`](#insn-00acbe80)
- ブロック [`00acbe80`](#insn-00acbe80) 範囲 `[['00acbe80', '00acbe8b']]`
  - `CONDITIONAL_JUMP` [`00acbe88`](#insn-00acbe88) → [`00acbeac`](#insn-00acbeac)
  - `FALL_THROUGH` [`00acbe88`](#insn-00acbe88) → [`00acbe8c`](#insn-00acbe8c)
- ブロック [`00acbe8c`](#insn-00acbe8c) 範囲 `[['00acbe8c', '00acbe97']]`
  - `CONDITIONAL_JUMP` [`00acbe94`](#insn-00acbe94) → [`00acbea4`](#insn-00acbea4)
  - `FALL_THROUGH` [`00acbe94`](#insn-00acbe94) → [`00acbe98`](#insn-00acbe98)
- ブロック [`00acbe98`](#insn-00acbe98) 範囲 `[['00acbe98', '00acbea3']]`
  - `FALL_THROUGH` [`00acbea0`](#insn-00acbea0) → [`00acbea4`](#insn-00acbea4)
- ブロック [`00acbea4`](#insn-00acbea4) 範囲 `[['00acbea4', '00acbeab']]`
  - `UNCONDITIONAL_JUMP` [`00acbea8`](#insn-00acbea8) → [`00acbeb8`](#insn-00acbeb8)
- ブロック [`00acbeac`](#insn-00acbeac) 範囲 `[['00acbeac', '00acbeb7']]`
  - `FALL_THROUGH` [`00acbeb4`](#insn-00acbeb4) → [`00acbeb8`](#insn-00acbeb8)
- ブロック [`00acbeb8`](#insn-00acbeb8) 範囲 `[['00acbeb8', '00acbecb']]`
  - `CONDITIONAL_JUMP` [`00acbec8`](#insn-00acbec8) → [`00acbf0c`](#insn-00acbf0c)
  - `FALL_THROUGH` [`00acbec8`](#insn-00acbec8) → [`00acbecc`](#insn-00acbecc)
- ブロック [`00acbecc`](#insn-00acbecc) 範囲 `[['00acbecc', '00acbee7']]`
- ブロック [`00acbf0c`](#insn-00acbf0c) 範囲 `[['00acbf0c', '00acbf0f']]`

## 命令位置別の参照

- [`00acbdc0`](#insn-00acbdc0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbdc4`](#insn-00acbdc4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbdc8`](#insn-00acbdc8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbdcc`](#insn-00acbdcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbdd0`](#insn-00acbdd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbde8`](#insn-00acbde8) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbdf0`](#insn-00acbdf0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbdf8`](#insn-00acbdf8) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00acbe0c`](#insn-00acbe0c) → `00c8d9c0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acbe20`](#insn-00acbe20) → [`00c53d70`](../00c53/00c53d70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d70` · 推定シンボル `None` · 推定型 `None`
- [`00acbe2c`](#insn-00acbe2c) → [`00acbe58`](#insn-00acbe58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe38`](#insn-00acbe38) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`00acbe3c`](#insn-00acbe3c) → [`00acbe58`](#insn-00acbe58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe54`](#insn-00acbe54) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`00acbe60`](#insn-00acbe60) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`00acbe64`](#insn-00acbe64) → [`00acbe80`](#insn-00acbe80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe70`](#insn-00acbe70) → `00c8d9d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00acbe74`](#insn-00acbe74) → [`00acc0e8`](../00acc/00acc0e8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00acc0e8` · 推定シンボル `None` · 推定型 `None`
- [`00acbe7c`](#insn-00acbe7c) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`00acbe88`](#insn-00acbe88) → [`00acbeac`](#insn-00acbeac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe94`](#insn-00acbe94) → [`00acbea4`](#insn-00acbea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbea0`](#insn-00acbea0) → [`00c53d70`](../00c53/00c53d70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d70` · 推定シンボル `None` · 推定型 `None`
- [`00acbea8`](#insn-00acbea8) → [`00acbeb8`](#insn-00acbeb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbeb4`](#insn-00acbeb4) → [`00acc140`](../00acc/00acc140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00acc140` · 推定シンボル `None` · 推定型 `None`
- [`00acbec0`](#insn-00acbec0) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbec8`](#insn-00acbec8) → [`00acbf0c`](#insn-00acbf0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbecc`](#insn-00acbecc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbed0`](#insn-00acbed0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbed4`](#insn-00acbed4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbed8`](#insn-00acbed8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbedc`](#insn-00acbedc) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf0c`](#insn-00acbf0c) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acbdc0`](#insn-00acbdc0)

~~~json
{
  "source": "00acbdc0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbdc4`](#insn-00acbdc4)

~~~json
{
  "source": "00acbdc4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbdc8`](#insn-00acbdc8)

~~~json
{
  "source": "00acbdc8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbdcc`](#insn-00acbdcc)

~~~json
{
  "source": "00acbdcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbdd0`](#insn-00acbdd0)

~~~json
{
  "source": "00acbdd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbde8`](#insn-00acbde8)

~~~json
{
  "source": "00acbde8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbdf0`](#insn-00acbdf0)

~~~json
{
  "source": "00acbdf0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbdf8`](#insn-00acbdf8)

~~~json
{
  "source": "00acbdf8",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbe0c`](#insn-00acbe0c)

~~~json
{
  "source": "00acbe0c",
  "target": "00c8d9c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8d9c0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acbe20`](#insn-00acbe20)

~~~json
{
  "source": "00acbe20",
  "target": "00c53d70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbe2c`](#insn-00acbe2c)

~~~json
{
  "source": "00acbe2c",
  "target": "00acbe58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe38`](#insn-00acbe38)

~~~json
{
  "source": "00acbe38",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbe3c`](#insn-00acbe3c)

~~~json
{
  "source": "00acbe3c",
  "target": "00acbe58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe54`](#insn-00acbe54)

~~~json
{
  "source": "00acbe54",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbe60`](#insn-00acbe60)

~~~json
{
  "source": "00acbe60",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbe64`](#insn-00acbe64)

~~~json
{
  "source": "00acbe64",
  "target": "00acbe80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe70`](#insn-00acbe70)

~~~json
{
  "source": "00acbe70",
  "target": "00c8d9d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8d9d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acbe74`](#insn-00acbe74)

~~~json
{
  "source": "00acbe74",
  "target": "00acc0e8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbe7c`](#insn-00acbe7c)

~~~json
{
  "source": "00acbe7c",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbe88`](#insn-00acbe88)

~~~json
{
  "source": "00acbe88",
  "target": "00acbeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe94`](#insn-00acbe94)

~~~json
{
  "source": "00acbe94",
  "target": "00acbea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbea0`](#insn-00acbea0)

~~~json
{
  "source": "00acbea0",
  "target": "00c53d70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbea8`](#insn-00acbea8)

~~~json
{
  "source": "00acbea8",
  "target": "00acbeb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbeb4`](#insn-00acbeb4)

~~~json
{
  "source": "00acbeb4",
  "target": "00acc140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbec0`](#insn-00acbec0)

~~~json
{
  "source": "00acbec0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbec8`](#insn-00acbec8)

~~~json
{
  "source": "00acbec8",
  "target": "00acbf0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbecc`](#insn-00acbecc)

~~~json
{
  "source": "00acbecc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbed0`](#insn-00acbed0)

~~~json
{
  "source": "00acbed0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbed4`](#insn-00acbed4)

~~~json
{
  "source": "00acbed4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbed8`](#insn-00acbed8)

~~~json
{
  "source": "00acbed8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbedc`](#insn-00acbedc)

~~~json
{
  "source": "00acbedc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf0c`](#insn-00acbf0c)

~~~json
{
  "source": "00acbf0c",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
