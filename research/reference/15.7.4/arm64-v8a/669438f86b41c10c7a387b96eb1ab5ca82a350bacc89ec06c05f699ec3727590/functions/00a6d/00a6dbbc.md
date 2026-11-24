# 00a6dbbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a6db78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6db78.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0056.md#compare-b81d3df939e12640777ca7f906ca881c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00acbb50`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbb50.md) · 移動量 `+0x5df94`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0053.md#compare-05cdda2be73a8ab201134fe5992192ab)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a6dbbc",
  "name": "FUN_00a6dbbc",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "88d366e54be122f0f7f08cc0105f0285e511d6d6f41c24ca43bda97500aee09e",
  "source_text_sha256": "88d366e54be122f0f7f08cc0105f0285e511d6d6f41c24ca43bda97500aee09e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a6dbbc",
        "00a6dce7"
      ],
      [
        "00a6dd0c",
        "00a6dd0f"
      ]
    ],
    "bytes_sha256": "ac01dc6c03aa157146909d9443b430041ac4b7d3e69560a0bf2e3f4e45480875",
    "instruction_count": 76,
    "instruction_bytes": 304,
    "body_bytes": 304,
    "indirect": 2,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00900ae0](../00900/00900ae0.md)

## 呼び出し先

- [00a6dee8](../00a6d/00a6dee8.md)
- [00a6df40](../00a6d/00a6df40.md)
- [00bd6e60](../00bd6/00bd6e60.md)
- [00bd6e90](../00bd6/00bd6e90.md)
- [00bdb030](../00bdb/00bdb030.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb090](../00bdb/00bdb090.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1437 bytes

~~~c

void FUN_00a6dbbc(long param_1,long *param_2)

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
  *plVar2 = (long)&PTR__ZNSt6__ndk119__shared_weak_countD2Ev_00c0ded0;
  plVar4 = plVar2 + 1;
  *plVar4 = 0;
  plVar2[2] = 0;
  plVar2[3] = param_1;
  FUN_00bd6e60(1,plVar4);
  plVar5 = *(long **)(lVar6 + 0x38);
  *(long *)(lVar6 + 0x30) = param_1;
  *(long **)(lVar6 + 0x38) = plVar2;
  if ((plVar5 != (long *)0x0) && (lVar6 = FUN_00bd6e90(0xffffffffffffffff,plVar5 + 1), lVar6 == 0))
  {
    (**(code **)(*plVar5 + 0x10))(plVar5);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar5);
  }
  lVar6 = FUN_00bd6e90(0xffffffffffffffff,plVar4);
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
      FUN_00bd6e60(1,lVar6 + 8);
    }
    plVar2 = plVar2 + 2;
  }
  else {
    plVar2 = (long *)FUN_00a6df40(param_1 + 0x40,param_2);
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
<a id="insn-00a6dbbc"></a> `00a6dbbc` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00a6dbc0"></a> `00a6dbc0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a6dbc4"></a> `00a6dbc4` | `f9 13 00 f9` | str x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a6dbc8"></a> `00a6dbc8` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a6dbcc"></a> `00a6dbcc` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a6dbd0"></a> `00a6dbd0` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a6dbd4"></a> `00a6dbd4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00a6dbd8"></a> `00a6dbd8` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00a6dbdc"></a> `00a6dbdc` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00a6dbe0"></a> `00a6dbe0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a6dbe4"></a> `00a6dbe4` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00a6dbe8"></a> `00a6dbe8` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a6dbec"></a> `00a6dbec` | `39 00 40 f9` | ldr x25,[x1] | `FALL_THROUGH`
<a id="insn-00a6dbf0"></a> `00a6dbf0` | `e0 03 00 f9` | str x0,[sp] | `FALL_THROUGH`
<a id="insn-00a6dbf4"></a> `00a6dbf4` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00a6dbf8"></a> `00a6dbf8` | `12 b5 05 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00a6dbfc"></a> `00a6dbfc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00a6dc00"></a> `00a6dc00` | `08 0d 00 90` | adrp x8,0xc0d000 | `FALL_THROUGH`
<a id="insn-00a6dc04"></a> `00a6dc04` | `08 41 3b 91` | add x8,x8,#0xed0 | `FALL_THROUGH`
<a id="insn-00a6dc08"></a> `00a6dc08` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00a6dc0c"></a> `00a6dc0c` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00a6dc10"></a> `00a6dc10` | `df 8e 00 f8` | str xzr,[x22, #0x8]! | `FALL_THROUGH`
<a id="insn-00a6dc14"></a> `00a6dc14` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00a6dc18"></a> `00a6dc18` | `1f 4c 01 a9` | stp xzr,x19,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00a6dc1c"></a> `00a6dc1c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00a6dc20"></a> `00a6dc20` | `90 a4 05 94` | bl 0x00bd6e60 | `UNCONDITIONAL_CALL`
<a id="insn-00a6dc24"></a> `00a6dc24` | `37 1f 40 f9` | ldr x23,[x25, #0x38] | `FALL_THROUGH`
<a id="insn-00a6dc28"></a> `00a6dc28` | `33 57 03 a9` | stp x19,x21,[x25, #0x30] | `FALL_THROUGH`
<a id="insn-00a6dc2c"></a> `00a6dc2c` | `77 01 00 b4` | cbz x23,0x00a6dc58 | `CONDITIONAL_JUMP`
<a id="insn-00a6dc30"></a> `00a6dc30` | `e1 22 00 91` | add x1,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00a6dc34"></a> `00a6dc34` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00a6dc38"></a> `00a6dc38` | `96 a4 05 94` | bl 0x00bd6e90 | `UNCONDITIONAL_CALL`
<a id="insn-00a6dc3c"></a> `00a6dc3c` | `e0 00 00 b5` | cbnz x0,0x00a6dc58 | `CONDITIONAL_JUMP`
<a id="insn-00a6dc40"></a> `00a6dc40` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00a6dc44"></a> `00a6dc44` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00a6dc48"></a> `00a6dc48` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00a6dc4c"></a> `00a6dc4c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00a6dc50"></a> `00a6dc50` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00a6dc54"></a> `00a6dc54` | `f7 b4 05 94` | bl 0x00bdb030 | `UNCONDITIONAL_CALL`
<a id="insn-00a6dc58"></a> `00a6dc58` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00a6dc5c"></a> `00a6dc5c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00a6dc60"></a> `00a6dc60` | `8c a4 05 94` | bl 0x00bd6e90 | `UNCONDITIONAL_CALL`
<a id="insn-00a6dc64"></a> `00a6dc64` | `e0 00 00 b5` | cbnz x0,0x00a6dc80 | `CONDITIONAL_JUMP`
<a id="insn-00a6dc68"></a> `00a6dc68` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00a6dc6c"></a> `00a6dc6c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00a6dc70"></a> `00a6dc70` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00a6dc74"></a> `00a6dc74` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00a6dc78"></a> `00a6dc78` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00a6dc7c"></a> `00a6dc7c` | `ed b4 05 94` | bl 0x00bdb030 | `UNCONDITIONAL_CALL`
<a id="insn-00a6dc80"></a> `00a6dc80` | `75 a2 44 a9` | ldp x21,x8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00a6dc84"></a> `00a6dc84` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00a6dc88"></a> `00a6dc88` | `22 01 00 54` | b.cs 0x00a6dcac | `CONDITIONAL_JUMP`
<a id="insn-00a6dc8c"></a> `00a6dc8c` | `89 22 40 a9` | ldp x9,x8,[x20] | `FALL_THROUGH`
<a id="insn-00a6dc90"></a> `00a6dc90` | `a9 22 00 a9` | stp x9,x8,[x21] | `FALL_THROUGH`
<a id="insn-00a6dc94"></a> `00a6dc94` | `88 00 00 b4` | cbz x8,0x00a6dca4 | `CONDITIONAL_JUMP`
<a id="insn-00a6dc98"></a> `00a6dc98` | `01 21 00 91` | add x1,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00a6dc9c"></a> `00a6dc9c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00a6dca0"></a> `00a6dca0` | `70 a4 05 94` | bl 0x00bd6e60 | `UNCONDITIONAL_CALL`
<a id="insn-00a6dca4"></a> `00a6dca4` | `a0 42 00 91` | add x0,x21,#0x10 | `FALL_THROUGH`
<a id="insn-00a6dca8"></a> `00a6dca8` | `04 00 00 14` | b 0x00a6dcb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00a6dcac"></a> `00a6dcac` | `60 02 01 91` | add x0,x19,#0x40 | `FALL_THROUGH`
<a id="insn-00a6dcb0"></a> `00a6dcb0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00a6dcb4"></a> `00a6dcb4` | `a3 00 00 94` | bl 0x00a6df40 | `UNCONDITIONAL_CALL`
<a id="insn-00a6dcb8"></a> `00a6dcb8` | `60 26 00 f9` | str x0,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00a6dcbc"></a> `00a6dcbc` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00a6dcc0"></a> `00a6dcc0` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a6dcc4"></a> `00a6dcc4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a6dcc8"></a> `00a6dcc8` | `21 02 00 54` | b.ne 0x00a6dd0c | `CONDITIONAL_JUMP`
<a id="insn-00a6dccc"></a> `00a6dccc` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a6dcd0"></a> `00a6dcd0` | `f9 13 40 f9` | ldr x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a6dcd4"></a> `00a6dcd4` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a6dcd8"></a> `00a6dcd8` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a6dcdc"></a> `00a6dcdc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a6dce0"></a> `00a6dce0` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00a6dce4"></a> `00a6dce4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a6dd0c"></a> `00a6dd0c` | `e1 b4 05 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a6dbbc`](#insn-00a6dbbc) 範囲 `[['00a6dbbc', '00a6dc2f']]`
  - `CONDITIONAL_JUMP` [`00a6dc2c`](#insn-00a6dc2c) → [`00a6dc58`](#insn-00a6dc58)
  - `FALL_THROUGH` [`00a6dc2c`](#insn-00a6dc2c) → [`00a6dc30`](#insn-00a6dc30)
- ブロック [`00a6dc30`](#insn-00a6dc30) 範囲 `[['00a6dc30', '00a6dc3f']]`
  - `CONDITIONAL_JUMP` [`00a6dc3c`](#insn-00a6dc3c) → [`00a6dc58`](#insn-00a6dc58)
  - `FALL_THROUGH` [`00a6dc3c`](#insn-00a6dc3c) → [`00a6dc40`](#insn-00a6dc40)
- ブロック [`00a6dc40`](#insn-00a6dc40) 範囲 `[['00a6dc40', '00a6dc57']]`
  - `FALL_THROUGH` [`00a6dc54`](#insn-00a6dc54) → [`00a6dc58`](#insn-00a6dc58)
- ブロック [`00a6dc58`](#insn-00a6dc58) 範囲 `[['00a6dc58', '00a6dc67']]`
  - `CONDITIONAL_JUMP` [`00a6dc64`](#insn-00a6dc64) → [`00a6dc80`](#insn-00a6dc80)
  - `FALL_THROUGH` [`00a6dc64`](#insn-00a6dc64) → [`00a6dc68`](#insn-00a6dc68)
- ブロック [`00a6dc68`](#insn-00a6dc68) 範囲 `[['00a6dc68', '00a6dc7f']]`
  - `FALL_THROUGH` [`00a6dc7c`](#insn-00a6dc7c) → [`00a6dc80`](#insn-00a6dc80)
- ブロック [`00a6dc80`](#insn-00a6dc80) 範囲 `[['00a6dc80', '00a6dc8b']]`
  - `CONDITIONAL_JUMP` [`00a6dc88`](#insn-00a6dc88) → [`00a6dcac`](#insn-00a6dcac)
  - `FALL_THROUGH` [`00a6dc88`](#insn-00a6dc88) → [`00a6dc8c`](#insn-00a6dc8c)
- ブロック [`00a6dc8c`](#insn-00a6dc8c) 範囲 `[['00a6dc8c', '00a6dc97']]`
  - `CONDITIONAL_JUMP` [`00a6dc94`](#insn-00a6dc94) → [`00a6dca4`](#insn-00a6dca4)
  - `FALL_THROUGH` [`00a6dc94`](#insn-00a6dc94) → [`00a6dc98`](#insn-00a6dc98)
- ブロック [`00a6dc98`](#insn-00a6dc98) 範囲 `[['00a6dc98', '00a6dca3']]`
  - `FALL_THROUGH` [`00a6dca0`](#insn-00a6dca0) → [`00a6dca4`](#insn-00a6dca4)
- ブロック [`00a6dca4`](#insn-00a6dca4) 範囲 `[['00a6dca4', '00a6dcab']]`
  - `UNCONDITIONAL_JUMP` [`00a6dca8`](#insn-00a6dca8) → [`00a6dcb8`](#insn-00a6dcb8)
- ブロック [`00a6dcac`](#insn-00a6dcac) 範囲 `[['00a6dcac', '00a6dcb7']]`
  - `FALL_THROUGH` [`00a6dcb4`](#insn-00a6dcb4) → [`00a6dcb8`](#insn-00a6dcb8)
- ブロック [`00a6dcb8`](#insn-00a6dcb8) 範囲 `[['00a6dcb8', '00a6dccb']]`
  - `CONDITIONAL_JUMP` [`00a6dcc8`](#insn-00a6dcc8) → [`00a6dd0c`](#insn-00a6dd0c)
  - `FALL_THROUGH` [`00a6dcc8`](#insn-00a6dcc8) → [`00a6dccc`](#insn-00a6dccc)
- ブロック [`00a6dccc`](#insn-00a6dccc) 範囲 `[['00a6dccc', '00a6dce7']]`
- ブロック [`00a6dd0c`](#insn-00a6dd0c) 範囲 `[['00a6dd0c', '00a6dd0f']]`

## 命令位置別の参照

- [`00a6dbc0`](#insn-00a6dbc0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dbc4`](#insn-00a6dbc4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dbc8`](#insn-00a6dbc8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dbcc`](#insn-00a6dbcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dbd0`](#insn-00a6dbd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dbe8`](#insn-00a6dbe8) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dbf0`](#insn-00a6dbf0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dbf8`](#insn-00a6dbf8) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00a6dc0c`](#insn-00a6dc0c) → `00c0ded0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00a6dc20`](#insn-00a6dc20) → [`00bd6e60`](../00bd6/00bd6e60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e60` · 推定シンボル `None` · 推定型 `None`
- [`00a6dc2c`](#insn-00a6dc2c) → [`00a6dc58`](#insn-00a6dc58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dc38`](#insn-00a6dc38) → [`00bd6e90`](../00bd6/00bd6e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e90` · 推定シンボル `None` · 推定型 `None`
- [`00a6dc3c`](#insn-00a6dc3c) → [`00a6dc58`](#insn-00a6dc58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dc54`](#insn-00a6dc54) → [`00bdb030`](../00bdb/00bdb030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb030` · 推定シンボル `None` · 推定型 `None`
- [`00a6dc60`](#insn-00a6dc60) → [`00bd6e90`](../00bd6/00bd6e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e90` · 推定シンボル `None` · 推定型 `None`
- [`00a6dc64`](#insn-00a6dc64) → [`00a6dc80`](#insn-00a6dc80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dc70`](#insn-00a6dc70) → `00c0dee0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00a6dc74`](#insn-00a6dc74) → [`00a6dee8`](00a6dee8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00a6dee8` · 推定シンボル `None` · 推定型 `None`
- [`00a6dc7c`](#insn-00a6dc7c) → [`00bdb030`](../00bdb/00bdb030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb030` · 推定シンボル `None` · 推定型 `None`
- [`00a6dc88`](#insn-00a6dc88) → [`00a6dcac`](#insn-00a6dcac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dc94`](#insn-00a6dc94) → [`00a6dca4`](#insn-00a6dca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dca0`](#insn-00a6dca0) → [`00bd6e60`](../00bd6/00bd6e60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e60` · 推定シンボル `None` · 推定型 `None`
- [`00a6dca8`](#insn-00a6dca8) → [`00a6dcb8`](#insn-00a6dcb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dcb4`](#insn-00a6dcb4) → [`00a6df40`](00a6df40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a6df40` · 推定シンボル `None` · 推定型 `None`
- [`00a6dcc0`](#insn-00a6dcc0) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dcc8`](#insn-00a6dcc8) → [`00a6dd0c`](#insn-00a6dd0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dccc`](#insn-00a6dccc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dcd0`](#insn-00a6dcd0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dcd4`](#insn-00a6dcd4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dcd8`](#insn-00a6dcd8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dcdc`](#insn-00a6dcdc) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6dd0c`](#insn-00a6dd0c) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a6dbc0`](#insn-00a6dbc0)

~~~json
{
  "source": "00a6dbc0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dbc4`](#insn-00a6dbc4)

~~~json
{
  "source": "00a6dbc4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dbc8`](#insn-00a6dbc8)

~~~json
{
  "source": "00a6dbc8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dbcc`](#insn-00a6dbcc)

~~~json
{
  "source": "00a6dbcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dbd0`](#insn-00a6dbd0)

~~~json
{
  "source": "00a6dbd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dbe8`](#insn-00a6dbe8)

~~~json
{
  "source": "00a6dbe8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dbf0`](#insn-00a6dbf0)

~~~json
{
  "source": "00a6dbf0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dbf8`](#insn-00a6dbf8)

~~~json
{
  "source": "00a6dbf8",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dc0c`](#insn-00a6dc0c)

~~~json
{
  "source": "00a6dc0c",
  "target": "00c0ded0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0ded0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a6dc20`](#insn-00a6dc20)

~~~json
{
  "source": "00a6dc20",
  "target": "00bd6e60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dc2c`](#insn-00a6dc2c)

~~~json
{
  "source": "00a6dc2c",
  "target": "00a6dc58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dc38`](#insn-00a6dc38)

~~~json
{
  "source": "00a6dc38",
  "target": "00bd6e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dc3c`](#insn-00a6dc3c)

~~~json
{
  "source": "00a6dc3c",
  "target": "00a6dc58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dc54`](#insn-00a6dc54)

~~~json
{
  "source": "00a6dc54",
  "target": "00bdb030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dc60`](#insn-00a6dc60)

~~~json
{
  "source": "00a6dc60",
  "target": "00bd6e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dc64`](#insn-00a6dc64)

~~~json
{
  "source": "00a6dc64",
  "target": "00a6dc80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dc70`](#insn-00a6dc70)

~~~json
{
  "source": "00a6dc70",
  "target": "00c0dee0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0dee0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a6dc74`](#insn-00a6dc74)

~~~json
{
  "source": "00a6dc74",
  "target": "00a6dee8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dc7c`](#insn-00a6dc7c)

~~~json
{
  "source": "00a6dc7c",
  "target": "00bdb030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dc88`](#insn-00a6dc88)

~~~json
{
  "source": "00a6dc88",
  "target": "00a6dcac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dc94`](#insn-00a6dc94)

~~~json
{
  "source": "00a6dc94",
  "target": "00a6dca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dca0`](#insn-00a6dca0)

~~~json
{
  "source": "00a6dca0",
  "target": "00bd6e60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dca8`](#insn-00a6dca8)

~~~json
{
  "source": "00a6dca8",
  "target": "00a6dcb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dcb4`](#insn-00a6dcb4)

~~~json
{
  "source": "00a6dcb4",
  "target": "00a6df40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6dcc0`](#insn-00a6dcc0)

~~~json
{
  "source": "00a6dcc0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dcc8`](#insn-00a6dcc8)

~~~json
{
  "source": "00a6dcc8",
  "target": "00a6dd0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dccc`](#insn-00a6dccc)

~~~json
{
  "source": "00a6dccc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dcd0`](#insn-00a6dcd0)

~~~json
{
  "source": "00a6dcd0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dcd4`](#insn-00a6dcd4)

~~~json
{
  "source": "00a6dcd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dcd8`](#insn-00a6dcd8)

~~~json
{
  "source": "00a6dcd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dcdc`](#insn-00a6dcdc)

~~~json
{
  "source": "00a6dcdc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6dd0c`](#insn-00a6dd0c)

~~~json
{
  "source": "00a6dd0c",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
