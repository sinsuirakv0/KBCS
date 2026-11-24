# 007afefc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0128.md#review-f6e3df6ce2eef0662fb9e115c39dc517)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `007aff3c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007aff3c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0039.md#compare-f8a1b64f7a7cea5bd4a73c4b4fd376b8)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007afefc",
  "name": "FUN_007afefc",
  "size": 308,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1b1500ac236955005b31f944d162f77346a482377c6b2d2d558f35cfd6572d22",
  "source_text_sha256": "1b1500ac236955005b31f944d162f77346a482377c6b2d2d558f35cfd6572d22",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007afefc",
        "007b002b"
      ],
      [
        "007b0070",
        "007b0073"
      ]
    ],
    "bytes_sha256": "64606dfb03776cab7415e4aa3b98ed13f9f2fe2c0328d54b18520340414187a7",
    "instruction_count": 77,
    "instruction_bytes": 308,
    "body_bytes": 308,
    "indirect": 2,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [007adedc](../007ad/007adedc.md)

## 呼び出し先

- [00597e90](../00597/00597e90.md)
- [005b72fc](../005b7/005b72fc.md)
- [00c538b0](../00c53/00c538b0.md)
- [00c538e0](../00c53/00c538e0.md)
- [00c57a80](../00c57/00c57a80.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ae0](../00c57/00c57ae0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1499 bytes

~~~c

void FUN_007afefc(long *param_1,undefined8 param_2,undefined8 *param_3)

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
  *plVar4 = (long)&PTR_FUN_00c701c0;
  local_50 = (long *)*param_3;
  *param_3 = 0;
  plVar1 = plVar4 + 4;
  plVar4[2] = 0;
  plVar4[1] = 0;
  FUN_00597e90(plVar1,&local_50);
  plVar3 = local_50;
  local_50 = (long *)0x0;
  if (plVar3 != (long *)0x0) {
    (**(code **)(*plVar3 + 8))();
  }
  lVar5 = plVar4[6];
  *param_1 = (long)plVar1;
  param_1[1] = (long)plVar4;
  if (lVar5 == 0) {
    FUN_00c538b0(1,plVar4 + 1);
    FUN_00c538b0(1,plVar4 + 2);
    plVar4[5] = (long)plVar1;
    plVar4[6] = (long)plVar4;
  }
  else {
    if (*(long *)(lVar5 + 8) != -1) goto LAB_007b0004;
    FUN_00c538b0(1,plVar4 + 1);
    FUN_00c538b0(1,plVar4 + 2);
    plVar4[5] = (long)plVar1;
    plVar4[6] = (long)plVar4;
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(lVar5);
                    /* try { // try from 007affbc to 008b0043 has its CatchHandler @ 007b0128 */
  }
  lVar5 = FUN_00c538e0(0xffffffffffffffff,plVar4 + 1);
  if (lVar5 == 0) {
    (**(code **)(*plVar4 + 0x10))(plVar4);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
  }
LAB_007b0004:
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
<a id="insn-007afefc"></a> `007afefc` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-007aff00"></a> `007aff00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007aff04"></a> `007aff04` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007aff08"></a> `007aff08` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007aff0c"></a> `007aff0c` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-007aff10"></a> `007aff10` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-007aff14"></a> `007aff14` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-007aff18"></a> `007aff18` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-007aff1c"></a> `007aff1c` | `00 16 80 52` | mov w0,#0xb0 | `FALL_THROUGH`
<a id="insn-007aff20"></a> `007aff20` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-007aff24"></a> `007aff24` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-007aff28"></a> `007aff28` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-007aff2c"></a> `007aff2c` | `d9 9e 12 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-007aff30"></a> `007aff30` | `08 26 00 b0` | adrp x8,0xc70000 | `FALL_THROUGH`
<a id="insn-007aff34"></a> `007aff34` | `08 01 07 91` | add x8,x8,#0x1c0 | `FALL_THROUGH`
<a id="insn-007aff38"></a> `007aff38` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-007aff3c"></a> `007aff3c` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-007aff40"></a> `007aff40` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-007aff44"></a> `007aff44` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-007aff48"></a> `007aff48` | `bf 02 00 f9` | str xzr,[x21] | `FALL_THROUGH`
<a id="insn-007aff4c"></a> `007aff4c` | `15 80 00 91` | add x21,x0,#0x20 | `FALL_THROUGH`
<a id="insn-007aff50"></a> `007aff50` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-007aff54"></a> `007aff54` | `9f 8e 00 f8` | str xzr,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-007aff58"></a> `007aff58` | `e8 03 00 f9` | str x8,[sp] | `FALL_THROUGH`
<a id="insn-007aff5c"></a> `007aff5c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-007aff60"></a> `007aff60` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-007aff64"></a> `007aff64` | `cb 9f f7 97` | bl 0x00597e90 | `UNCONDITIONAL_CALL`
<a id="insn-007aff68"></a> `007aff68` | `e0 03 40 f9` | ldr x0,[sp] | `FALL_THROUGH`
<a id="insn-007aff6c"></a> `007aff6c` | `ff 03 00 f9` | str xzr,[sp] | `FALL_THROUGH`
<a id="insn-007aff70"></a> `007aff70` | `80 00 00 b4` | cbz x0,0x007aff80 | `CONDITIONAL_JUMP`
<a id="insn-007aff74"></a> `007aff74` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-007aff78"></a> `007aff78` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-007aff7c"></a> `007aff7c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007aff80"></a> `007aff80` | `77 1a 40 f9` | ldr x23,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-007aff84"></a> `007aff84` | `d5 4e 00 a9` | stp x21,x19,[x22] | `FALL_THROUGH`
<a id="insn-007aff88"></a> `007aff88` | `d7 01 00 b4` | cbz x23,0x007affc0 | `CONDITIONAL_JUMP`
<a id="insn-007aff8c"></a> `007aff8c` | `e8 06 40 f9` | ldr x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-007aff90"></a> `007aff90` | `1f 05 00 b1` | cmn x8,#0x1 | `FALL_THROUGH`
<a id="insn-007aff94"></a> `007aff94` | `81 03 00 54` | b.ne 0x007b0004 | `CONDITIONAL_JUMP`
<a id="insn-007aff98"></a> `007aff98` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-007aff9c"></a> `007aff9c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-007affa0"></a> `007affa0` | `44 8e 12 94` | bl 0x00c538b0 | `UNCONDITIONAL_CALL`
<a id="insn-007affa4"></a> `007affa4` | `61 42 00 91` | add x1,x19,#0x10 | `FALL_THROUGH`
<a id="insn-007affa8"></a> `007affa8` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-007affac"></a> `007affac` | `41 8e 12 94` | bl 0x00c538b0 | `UNCONDITIONAL_CALL`
<a id="insn-007affb0"></a> `007affb0` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-007affb4"></a> `007affb4` | `75 ce 02 a9` | stp x21,x19,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-007affb8"></a> `007affb8` | `b2 9e 12 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-007affbc"></a> `007affbc` | `08 00 00 14` | b 0x007affdc | `UNCONDITIONAL_JUMP`
<a id="insn-007affc0"></a> `007affc0` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-007affc4"></a> `007affc4` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-007affc8"></a> `007affc8` | `3a 8e 12 94` | bl 0x00c538b0 | `UNCONDITIONAL_CALL`
<a id="insn-007affcc"></a> `007affcc` | `61 42 00 91` | add x1,x19,#0x10 | `FALL_THROUGH`
<a id="insn-007affd0"></a> `007affd0` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-007affd4"></a> `007affd4` | `37 8e 12 94` | bl 0x00c538b0 | `UNCONDITIONAL_CALL`
<a id="insn-007affd8"></a> `007affd8` | `75 ce 02 a9` | stp x21,x19,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-007affdc"></a> `007affdc` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-007affe0"></a> `007affe0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-007affe4"></a> `007affe4` | `3f 8e 12 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-007affe8"></a> `007affe8` | `e0 00 00 b5` | cbnz x0,0x007b0004 | `CONDITIONAL_JUMP`
<a id="insn-007affec"></a> `007affec` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-007afff0"></a> `007afff0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007afff4"></a> `007afff4` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-007afff8"></a> `007afff8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007afffc"></a> `007afffc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007b0000"></a> `007b0000` | `a0 9e 12 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-007b0004"></a> `007b0004` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-007b0008"></a> `007b0008` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-007b000c"></a> `007b000c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-007b0010"></a> `007b0010` | `01 03 00 54` | b.ne 0x007b0070 | `CONDITIONAL_JUMP`
<a id="insn-007b0014"></a> `007b0014` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-007b0018"></a> `007b0018` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007b001c"></a> `007b001c` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007b0020"></a> `007b0020` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007b0024"></a> `007b0024` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-007b0028"></a> `007b0028` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-007b0070"></a> `007b0070` | `9c 9e 12 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007afefc`](#insn-007afefc) 範囲 `[['007afefc', '007aff73']]`
  - `CONDITIONAL_JUMP` [`007aff70`](#insn-007aff70) → [`007aff80`](#insn-007aff80)
  - `FALL_THROUGH` [`007aff70`](#insn-007aff70) → [`007aff74`](#insn-007aff74)
- ブロック [`007aff74`](#insn-007aff74) 範囲 `[['007aff74', '007aff7f']]`
  - `FALL_THROUGH` [`007aff7c`](#insn-007aff7c) → [`007aff80`](#insn-007aff80)
- ブロック [`007aff80`](#insn-007aff80) 範囲 `[['007aff80', '007aff8b']]`
  - `CONDITIONAL_JUMP` [`007aff88`](#insn-007aff88) → [`007affc0`](#insn-007affc0)
  - `FALL_THROUGH` [`007aff88`](#insn-007aff88) → [`007aff8c`](#insn-007aff8c)
- ブロック [`007aff8c`](#insn-007aff8c) 範囲 `[['007aff8c', '007aff97']]`
  - `CONDITIONAL_JUMP` [`007aff94`](#insn-007aff94) → [`007b0004`](#insn-007b0004)
  - `FALL_THROUGH` [`007aff94`](#insn-007aff94) → [`007aff98`](#insn-007aff98)
- ブロック [`007aff98`](#insn-007aff98) 範囲 `[['007aff98', '007affbb']]`
  - `FALL_THROUGH` [`007affb8`](#insn-007affb8) → [`007affbc`](#insn-007affbc)
- ブロック [`007affbc`](#insn-007affbc) 範囲 `[['007affbc', '007affbf']]`
  - `UNCONDITIONAL_JUMP` [`007affbc`](#insn-007affbc) → [`007affdc`](#insn-007affdc)
- ブロック [`007affc0`](#insn-007affc0) 範囲 `[['007affc0', '007affdb']]`
  - `FALL_THROUGH` [`007affd8`](#insn-007affd8) → [`007affdc`](#insn-007affdc)
- ブロック [`007affdc`](#insn-007affdc) 範囲 `[['007affdc', '007affeb']]`
  - `CONDITIONAL_JUMP` [`007affe8`](#insn-007affe8) → [`007b0004`](#insn-007b0004)
  - `FALL_THROUGH` [`007affe8`](#insn-007affe8) → [`007affec`](#insn-007affec)
- ブロック [`007affec`](#insn-007affec) 範囲 `[['007affec', '007b0003']]`
  - `FALL_THROUGH` [`007b0000`](#insn-007b0000) → [`007b0004`](#insn-007b0004)
- ブロック [`007b0004`](#insn-007b0004) 範囲 `[['007b0004', '007b0013']]`
  - `CONDITIONAL_JUMP` [`007b0010`](#insn-007b0010) → [`007b0070`](#insn-007b0070)
  - `FALL_THROUGH` [`007b0010`](#insn-007b0010) → [`007b0014`](#insn-007b0014)
- ブロック [`007b0014`](#insn-007b0014) 範囲 `[['007b0014', '007b002b']]`
- ブロック [`007b0070`](#insn-007b0070) 範囲 `[['007b0070', '007b0073']]`

## 命令位置別の参照

- [`007aff00`](#insn-007aff00) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aff04`](#insn-007aff04) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aff08`](#insn-007aff08) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aff0c`](#insn-007aff0c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aff28`](#insn-007aff28) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aff2c`](#insn-007aff2c) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`007aff3c`](#insn-007aff3c) → `00c701c0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`007aff58`](#insn-007aff58) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aff64`](#insn-007aff64) → [`00597e90`](../00597/00597e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00597e90` · 推定シンボル `None` · 推定型 `None`
- [`007aff68`](#insn-007aff68) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aff6c`](#insn-007aff6c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aff70`](#insn-007aff70) → [`007aff80`](#insn-007aff80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aff88`](#insn-007aff88) → [`007affc0`](#insn-007affc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aff94`](#insn-007aff94) → [`007b0004`](#insn-007b0004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007affa0`](#insn-007affa0) → [`00c538b0`](../00c53/00c538b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538b0` · 推定シンボル `None` · 推定型 `None`
- [`007affac`](#insn-007affac) → [`00c538b0`](../00c53/00c538b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538b0` · 推定シンボル `None` · 推定型 `None`
- [`007affb8`](#insn-007affb8) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`007affbc`](#insn-007affbc) → [`007affdc`](#insn-007affdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007affc8`](#insn-007affc8) → [`00c538b0`](../00c53/00c538b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538b0` · 推定シンボル `None` · 推定型 `None`
- [`007affd4`](#insn-007affd4) → [`00c538b0`](../00c53/00c538b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538b0` · 推定シンボル `None` · 推定型 `None`
- [`007affe4`](#insn-007affe4) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`007affe8`](#insn-007affe8) → [`007b0004`](#insn-007b0004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007afff4`](#insn-007afff4) → `00c701d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007afff8`](#insn-007afff8) → [`005b72fc`](../005b7/005b72fc.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `005b72fc` · 推定シンボル `None` · 推定型 `None`
- [`007b0000`](#insn-007b0000) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`007b0008`](#insn-007b0008) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007b0010`](#insn-007b0010) → [`007b0070`](#insn-007b0070) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007b0014`](#insn-007b0014) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007b0018`](#insn-007b0018) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007b001c`](#insn-007b001c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007b0020`](#insn-007b0020) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007b0070`](#insn-007b0070) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007aff00`](#insn-007aff00)

~~~json
{
  "source": "007aff00",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aff04`](#insn-007aff04)

~~~json
{
  "source": "007aff04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aff08`](#insn-007aff08)

~~~json
{
  "source": "007aff08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aff0c`](#insn-007aff0c)

~~~json
{
  "source": "007aff0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aff28`](#insn-007aff28)

~~~json
{
  "source": "007aff28",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aff2c`](#insn-007aff2c)

~~~json
{
  "source": "007aff2c",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007aff3c`](#insn-007aff3c)

~~~json
{
  "source": "007aff3c",
  "target": "00c701c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c701c0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007aff58`](#insn-007aff58)

~~~json
{
  "source": "007aff58",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aff64`](#insn-007aff64)

~~~json
{
  "source": "007aff64",
  "target": "00597e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007aff68`](#insn-007aff68)

~~~json
{
  "source": "007aff68",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aff6c`](#insn-007aff6c)

~~~json
{
  "source": "007aff6c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aff70`](#insn-007aff70)

~~~json
{
  "source": "007aff70",
  "target": "007aff80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aff88`](#insn-007aff88)

~~~json
{
  "source": "007aff88",
  "target": "007affc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aff94`](#insn-007aff94)

~~~json
{
  "source": "007aff94",
  "target": "007b0004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007affa0`](#insn-007affa0)

~~~json
{
  "source": "007affa0",
  "target": "00c538b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007affac`](#insn-007affac)

~~~json
{
  "source": "007affac",
  "target": "00c538b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007affb8`](#insn-007affb8)

~~~json
{
  "source": "007affb8",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007affbc`](#insn-007affbc)

~~~json
{
  "source": "007affbc",
  "target": "007affdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007affc8`](#insn-007affc8)

~~~json
{
  "source": "007affc8",
  "target": "00c538b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007affd4`](#insn-007affd4)

~~~json
{
  "source": "007affd4",
  "target": "00c538b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007affe4`](#insn-007affe4)

~~~json
{
  "source": "007affe4",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007affe8`](#insn-007affe8)

~~~json
{
  "source": "007affe8",
  "target": "007b0004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007afff4`](#insn-007afff4)

~~~json
{
  "source": "007afff4",
  "target": "00c701d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c701d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007afff8`](#insn-007afff8)

~~~json
{
  "source": "007afff8",
  "target": "005b72fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007b0000`](#insn-007b0000)

~~~json
{
  "source": "007b0000",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007b0008`](#insn-007b0008)

~~~json
{
  "source": "007b0008",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007b0010`](#insn-007b0010)

~~~json
{
  "source": "007b0010",
  "target": "007b0070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007b0014`](#insn-007b0014)

~~~json
{
  "source": "007b0014",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007b0018`](#insn-007b0018)

~~~json
{
  "source": "007b0018",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007b001c`](#insn-007b001c)

~~~json
{
  "source": "007b001c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007b0020`](#insn-007b0020)

~~~json
{
  "source": "007b0020",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007b0070`](#insn-007b0070)

~~~json
{
  "source": "007b0070",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
