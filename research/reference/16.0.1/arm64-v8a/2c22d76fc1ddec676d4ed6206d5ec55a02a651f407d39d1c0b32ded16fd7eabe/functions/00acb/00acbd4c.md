# 00acbd4c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00acbb50`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbb50.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0064.md#compare-c1f11c90456b7eec9ccab322eb16ffc3)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acbdbc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acbdbc.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0065.md#compare-23c957628b1360d0635b63e8a23f9ca0)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbd4c",
  "name": "FUN_00acbd4c",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "456e5ed42d0239afb100c0eaf48a6fdb797436dce20fe70299cc61b2c25ddeb6",
  "source_text_sha256": "456e5ed42d0239afb100c0eaf48a6fdb797436dce20fe70299cc61b2c25ddeb6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acbd4c",
        "00acbe77"
      ],
      [
        "00acbe9c",
        "00acbe9f"
      ]
    ],
    "bytes_sha256": "87720e37e2c627511d8672017fbc4ca0db30f0b7ccd79ab171c850711d50f11a",
    "instruction_count": 76,
    "instruction_bytes": 304,
    "body_bytes": 304,
    "indirect": 2,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [009356b0](../00935/009356b0.md)

## 呼び出し先

- [00acc078](../00acc/00acc078.md)
- [00acc0d0](../00acc/00acc0d0.md)
- [00c53cd0](../00c53/00c53cd0.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57ee0](../00c57/00c57ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1437 bytes

~~~c

void FUN_00acbd4c(long param_1,long *param_2)

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
  *plVar2 = (long)&PTR__ZNSt6__ndk119__shared_weak_countD1Ev_00c8d8f0;
  plVar4 = plVar2 + 1;
  *plVar4 = 0;
  plVar2[2] = 0;
  plVar2[3] = param_1;
  FUN_00c53cd0(1,plVar4);
  plVar5 = *(long **)(lVar6 + 0x38);
  *(long *)(lVar6 + 0x30) = param_1;
  *(long **)(lVar6 + 0x38) = plVar2;
  if ((plVar5 != (long *)0x0) && (lVar6 = FUN_00c53d00(0xffffffffffffffff,plVar5 + 1), lVar6 == 0))
  {
    (**(code **)(*plVar5 + 0x10))(plVar5);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar5);
  }
  lVar6 = FUN_00c53d00(0xffffffffffffffff,plVar4);
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
      FUN_00c53cd0(1,lVar6 + 8);
    }
    plVar2 = plVar2 + 2;
  }
  else {
    plVar2 = (long *)FUN_00acc0d0(param_1 + 0x40,param_2);
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
<a id="insn-00acbd4c"></a> `00acbd4c` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acbd50"></a> `00acbd50` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acbd54"></a> `00acbd54` | `f9 13 00 f9` | str x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acbd58"></a> `00acbd58` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acbd5c"></a> `00acbd5c` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acbd60"></a> `00acbd60` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acbd64"></a> `00acbd64` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00acbd68"></a> `00acbd68` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acbd6c"></a> `00acbd6c` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00acbd70"></a> `00acbd70` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acbd74"></a> `00acbd74` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00acbd78"></a> `00acbd78` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acbd7c"></a> `00acbd7c` | `39 00 40 f9` | ldr x25,[x1] | `FALL_THROUGH`
<a id="insn-00acbd80"></a> `00acbd80` | `e0 03 00 f9` | str x0,[sp] | `FALL_THROUGH`
<a id="insn-00acbd84"></a> `00acbd84` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00acbd88"></a> `00acbd88` | `42 30 06 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00acbd8c"></a> `00acbd8c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00acbd90"></a> `00acbd90` | `08 0e 00 d0` | adrp x8,0xc8d000 | `FALL_THROUGH`
<a id="insn-00acbd94"></a> `00acbd94` | `08 c1 23 91` | add x8,x8,#0x8f0 | `FALL_THROUGH`
<a id="insn-00acbd98"></a> `00acbd98` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00acbd9c"></a> `00acbd9c` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00acbda0"></a> `00acbda0` | `df 8e 00 f8` | str xzr,[x22, #0x8]! | `FALL_THROUGH`
<a id="insn-00acbda4"></a> `00acbda4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00acbda8"></a> `00acbda8` | `1f 4c 01 a9` | stp xzr,x19,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00acbdac"></a> `00acbdac` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00acbdb0"></a> `00acbdb0` | `c8 1f 06 94` | bl 0x00c53cd0 | `UNCONDITIONAL_CALL`
<a id="insn-00acbdb4"></a> `00acbdb4` | `37 1f 40 f9` | ldr x23,[x25, #0x38] | `FALL_THROUGH`
<a id="insn-00acbdb8"></a> `00acbdb8` | `33 57 03 a9` | stp x19,x21,[x25, #0x30] | `FALL_THROUGH`
<a id="insn-00acbdbc"></a> `00acbdbc` | `77 01 00 b4` | cbz x23,0x00acbde8 | `CONDITIONAL_JUMP`
<a id="insn-00acbdc0"></a> `00acbdc0` | `e1 22 00 91` | add x1,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00acbdc4"></a> `00acbdc4` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acbdc8"></a> `00acbdc8` | `ce 1f 06 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00acbdcc"></a> `00acbdcc` | `e0 00 00 b5` | cbnz x0,0x00acbde8 | `CONDITIONAL_JUMP`
<a id="insn-00acbdd0"></a> `00acbdd0` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00acbdd4"></a> `00acbdd4` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00acbdd8"></a> `00acbdd8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acbddc"></a> `00acbddc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbde0"></a> `00acbde0` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00acbde4"></a> `00acbde4` | `27 30 06 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00acbde8"></a> `00acbde8` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acbdec"></a> `00acbdec` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00acbdf0"></a> `00acbdf0` | `c4 1f 06 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00acbdf4"></a> `00acbdf4` | `e0 00 00 b5` | cbnz x0,0x00acbe10 | `CONDITIONAL_JUMP`
<a id="insn-00acbdf8"></a> `00acbdf8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00acbdfc"></a> `00acbdfc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00acbe00"></a> `00acbe00` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acbe04"></a> `00acbe04` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbe08"></a> `00acbe08` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00acbe0c"></a> `00acbe0c` | `1d 30 06 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00acbe10"></a> `00acbe10` | `75 a2 44 a9` | ldp x21,x8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00acbe14"></a> `00acbe14` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00acbe18"></a> `00acbe18` | `22 01 00 54` | b.cs 0x00acbe3c | `CONDITIONAL_JUMP`
<a id="insn-00acbe1c"></a> `00acbe1c` | `89 22 40 a9` | ldp x9,x8,[x20] | `FALL_THROUGH`
<a id="insn-00acbe20"></a> `00acbe20` | `a9 22 00 a9` | stp x9,x8,[x21] | `FALL_THROUGH`
<a id="insn-00acbe24"></a> `00acbe24` | `88 00 00 b4` | cbz x8,0x00acbe34 | `CONDITIONAL_JUMP`
<a id="insn-00acbe28"></a> `00acbe28` | `01 21 00 91` | add x1,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00acbe2c"></a> `00acbe2c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00acbe30"></a> `00acbe30` | `a8 1f 06 94` | bl 0x00c53cd0 | `UNCONDITIONAL_CALL`
<a id="insn-00acbe34"></a> `00acbe34` | `a0 42 00 91` | add x0,x21,#0x10 | `FALL_THROUGH`
<a id="insn-00acbe38"></a> `00acbe38` | `04 00 00 14` | b 0x00acbe48 | `UNCONDITIONAL_JUMP`
<a id="insn-00acbe3c"></a> `00acbe3c` | `60 02 01 91` | add x0,x19,#0x40 | `FALL_THROUGH`
<a id="insn-00acbe40"></a> `00acbe40` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00acbe44"></a> `00acbe44` | `a3 00 00 94` | bl 0x00acc0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00acbe48"></a> `00acbe48` | `60 26 00 f9` | str x0,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00acbe4c"></a> `00acbe4c` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00acbe50"></a> `00acbe50` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acbe54"></a> `00acbe54` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acbe58"></a> `00acbe58` | `21 02 00 54` | b.ne 0x00acbe9c | `CONDITIONAL_JUMP`
<a id="insn-00acbe5c"></a> `00acbe5c` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acbe60"></a> `00acbe60` | `f9 13 40 f9` | ldr x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acbe64"></a> `00acbe64` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acbe68"></a> `00acbe68` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acbe6c"></a> `00acbe6c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acbe70"></a> `00acbe70` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acbe74"></a> `00acbe74` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acbe9c"></a> `00acbe9c` | `11 30 06 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acbd4c`](#insn-00acbd4c) 範囲 `[['00acbd4c', '00acbdbf']]`
  - `CONDITIONAL_JUMP` [`00acbdbc`](#insn-00acbdbc) → [`00acbde8`](#insn-00acbde8)
  - `FALL_THROUGH` [`00acbdbc`](#insn-00acbdbc) → [`00acbdc0`](#insn-00acbdc0)
- ブロック [`00acbdc0`](#insn-00acbdc0) 範囲 `[['00acbdc0', '00acbdcf']]`
  - `CONDITIONAL_JUMP` [`00acbdcc`](#insn-00acbdcc) → [`00acbde8`](#insn-00acbde8)
  - `FALL_THROUGH` [`00acbdcc`](#insn-00acbdcc) → [`00acbdd0`](#insn-00acbdd0)
- ブロック [`00acbdd0`](#insn-00acbdd0) 範囲 `[['00acbdd0', '00acbde7']]`
  - `FALL_THROUGH` [`00acbde4`](#insn-00acbde4) → [`00acbde8`](#insn-00acbde8)
- ブロック [`00acbde8`](#insn-00acbde8) 範囲 `[['00acbde8', '00acbdf7']]`
  - `CONDITIONAL_JUMP` [`00acbdf4`](#insn-00acbdf4) → [`00acbe10`](#insn-00acbe10)
  - `FALL_THROUGH` [`00acbdf4`](#insn-00acbdf4) → [`00acbdf8`](#insn-00acbdf8)
- ブロック [`00acbdf8`](#insn-00acbdf8) 範囲 `[['00acbdf8', '00acbe0f']]`
  - `FALL_THROUGH` [`00acbe0c`](#insn-00acbe0c) → [`00acbe10`](#insn-00acbe10)
- ブロック [`00acbe10`](#insn-00acbe10) 範囲 `[['00acbe10', '00acbe1b']]`
  - `CONDITIONAL_JUMP` [`00acbe18`](#insn-00acbe18) → [`00acbe3c`](#insn-00acbe3c)
  - `FALL_THROUGH` [`00acbe18`](#insn-00acbe18) → [`00acbe1c`](#insn-00acbe1c)
- ブロック [`00acbe1c`](#insn-00acbe1c) 範囲 `[['00acbe1c', '00acbe27']]`
  - `CONDITIONAL_JUMP` [`00acbe24`](#insn-00acbe24) → [`00acbe34`](#insn-00acbe34)
  - `FALL_THROUGH` [`00acbe24`](#insn-00acbe24) → [`00acbe28`](#insn-00acbe28)
- ブロック [`00acbe28`](#insn-00acbe28) 範囲 `[['00acbe28', '00acbe33']]`
  - `FALL_THROUGH` [`00acbe30`](#insn-00acbe30) → [`00acbe34`](#insn-00acbe34)
- ブロック [`00acbe34`](#insn-00acbe34) 範囲 `[['00acbe34', '00acbe3b']]`
  - `UNCONDITIONAL_JUMP` [`00acbe38`](#insn-00acbe38) → [`00acbe48`](#insn-00acbe48)
- ブロック [`00acbe3c`](#insn-00acbe3c) 範囲 `[['00acbe3c', '00acbe47']]`
  - `FALL_THROUGH` [`00acbe44`](#insn-00acbe44) → [`00acbe48`](#insn-00acbe48)
- ブロック [`00acbe48`](#insn-00acbe48) 範囲 `[['00acbe48', '00acbe5b']]`
  - `CONDITIONAL_JUMP` [`00acbe58`](#insn-00acbe58) → [`00acbe9c`](#insn-00acbe9c)
  - `FALL_THROUGH` [`00acbe58`](#insn-00acbe58) → [`00acbe5c`](#insn-00acbe5c)
- ブロック [`00acbe5c`](#insn-00acbe5c) 範囲 `[['00acbe5c', '00acbe77']]`
- ブロック [`00acbe9c`](#insn-00acbe9c) 範囲 `[['00acbe9c', '00acbe9f']]`

## 命令位置別の参照

- [`00acbd50`](#insn-00acbd50) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd54`](#insn-00acbd54) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd58`](#insn-00acbd58) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd5c`](#insn-00acbd5c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd60`](#insn-00acbd60) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd78`](#insn-00acbd78) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd80`](#insn-00acbd80) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd88`](#insn-00acbd88) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00acbd9c`](#insn-00acbd9c) → `00c8d8f0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acbdb0`](#insn-00acbdb0) → [`00c53cd0`](../00c53/00c53cd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53cd0` · 推定シンボル `None` · 推定型 `None`
- [`00acbdbc`](#insn-00acbdbc) → [`00acbde8`](#insn-00acbde8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbdc8`](#insn-00acbdc8) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00acbdcc`](#insn-00acbdcc) → [`00acbde8`](#insn-00acbde8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbde4`](#insn-00acbde4) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00acbdf0`](#insn-00acbdf0) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00acbdf4`](#insn-00acbdf4) → [`00acbe10`](#insn-00acbe10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe00`](#insn-00acbe00) → `00c8d900`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00acbe04`](#insn-00acbe04) → [`00acc078`](../00acc/00acc078.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00acc078` · 推定シンボル `None` · 推定型 `None`
- [`00acbe0c`](#insn-00acbe0c) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00acbe18`](#insn-00acbe18) → [`00acbe3c`](#insn-00acbe3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe24`](#insn-00acbe24) → [`00acbe34`](#insn-00acbe34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe30`](#insn-00acbe30) → [`00c53cd0`](../00c53/00c53cd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53cd0` · 推定シンボル `None` · 推定型 `None`
- [`00acbe38`](#insn-00acbe38) → [`00acbe48`](#insn-00acbe48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe44`](#insn-00acbe44) → [`00acc0d0`](../00acc/00acc0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00acc0d0` · 推定シンボル `None` · 推定型 `None`
- [`00acbe50`](#insn-00acbe50) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe58`](#insn-00acbe58) → [`00acbe9c`](#insn-00acbe9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe5c`](#insn-00acbe5c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe60`](#insn-00acbe60) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe64`](#insn-00acbe64) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe68`](#insn-00acbe68) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe6c`](#insn-00acbe6c) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbe9c`](#insn-00acbe9c) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acbd50`](#insn-00acbd50)

~~~json
{
  "source": "00acbd50",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd54`](#insn-00acbd54)

~~~json
{
  "source": "00acbd54",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd58`](#insn-00acbd58)

~~~json
{
  "source": "00acbd58",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd5c`](#insn-00acbd5c)

~~~json
{
  "source": "00acbd5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd60`](#insn-00acbd60)

~~~json
{
  "source": "00acbd60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd78`](#insn-00acbd78)

~~~json
{
  "source": "00acbd78",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd80`](#insn-00acbd80)

~~~json
{
  "source": "00acbd80",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd88`](#insn-00acbd88)

~~~json
{
  "source": "00acbd88",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbd9c`](#insn-00acbd9c)

~~~json
{
  "source": "00acbd9c",
  "target": "00c8d8f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8d8f0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acbdb0`](#insn-00acbdb0)

~~~json
{
  "source": "00acbdb0",
  "target": "00c53cd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbdbc`](#insn-00acbdbc)

~~~json
{
  "source": "00acbdbc",
  "target": "00acbde8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbdc8`](#insn-00acbdc8)

~~~json
{
  "source": "00acbdc8",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbdcc`](#insn-00acbdcc)

~~~json
{
  "source": "00acbdcc",
  "target": "00acbde8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbde4`](#insn-00acbde4)

~~~json
{
  "source": "00acbde4",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbdf0`](#insn-00acbdf0)

~~~json
{
  "source": "00acbdf0",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbdf4`](#insn-00acbdf4)

~~~json
{
  "source": "00acbdf4",
  "target": "00acbe10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe00`](#insn-00acbe00)

~~~json
{
  "source": "00acbe00",
  "target": "00c8d900",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8d900",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acbe04`](#insn-00acbe04)

~~~json
{
  "source": "00acbe04",
  "target": "00acc078",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbe0c`](#insn-00acbe0c)

~~~json
{
  "source": "00acbe0c",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbe18`](#insn-00acbe18)

~~~json
{
  "source": "00acbe18",
  "target": "00acbe3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe24`](#insn-00acbe24)

~~~json
{
  "source": "00acbe24",
  "target": "00acbe34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe30`](#insn-00acbe30)

~~~json
{
  "source": "00acbe30",
  "target": "00c53cd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbe38`](#insn-00acbe38)

~~~json
{
  "source": "00acbe38",
  "target": "00acbe48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe44`](#insn-00acbe44)

~~~json
{
  "source": "00acbe44",
  "target": "00acc0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbe50`](#insn-00acbe50)

~~~json
{
  "source": "00acbe50",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe58`](#insn-00acbe58)

~~~json
{
  "source": "00acbe58",
  "target": "00acbe9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe5c`](#insn-00acbe5c)

~~~json
{
  "source": "00acbe5c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe60`](#insn-00acbe60)

~~~json
{
  "source": "00acbe60",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe64`](#insn-00acbe64)

~~~json
{
  "source": "00acbe64",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe68`](#insn-00acbe68)

~~~json
{
  "source": "00acbe68",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe6c`](#insn-00acbe6c)

~~~json
{
  "source": "00acbe6c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbe9c`](#insn-00acbe9c)

~~~json
{
  "source": "00acbe9c",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
