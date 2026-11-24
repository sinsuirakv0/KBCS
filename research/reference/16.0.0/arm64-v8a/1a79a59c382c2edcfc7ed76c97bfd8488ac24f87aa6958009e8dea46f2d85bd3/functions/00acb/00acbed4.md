# 00acbed4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a6df40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6df40.md) · 移動量 `+0x5df94`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0053.md#compare-ad3d93f25b1c2dc742e229b3aa3d899b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acc0d0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acc/00acc0d0.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0035.md#compare-b0086508cad5cdaabd4ea69bd99b3d79)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbed4",
  "name": "FUN_00acbed4",
  "size": 348,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "45f1e31d99ba938d0b238e954c54b7ebe208c1324b0cea9fc0afb2066453b34e",
  "source_text_sha256": "45f1e31d99ba938d0b238e954c54b7ebe208c1324b0cea9fc0afb2066453b34e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acbed4",
        "00acc02f"
      ]
    ],
    "bytes_sha256": "80bb6b4a0e77d723e86bdc5835df724e1b145e06a51586ee96093e1912684c11",
    "instruction_count": 87,
    "instruction_bytes": 348,
    "body_bytes": 348,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00acbb50](../00acb/00acbb50.md)

## 呼び出し先

- [00440e80](../00440/00440e80.md)
- [00acc030](../00acc/00acc030.md)
- [00c538b0](../00c53/00c538b0.md)
- [00c538e0](../00c53/00c538e0.md)
- [00c57a80](../00c57/00c57a80.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2122 bytes

~~~c

undefined8 * FUN_00acbed4(long *param_1,undefined8 *param_2)

{
  ulong uVar1;
  undefined8 *puVar2;
  long lVar3;
  long lVar4;
  undefined8 *puVar5;
  undefined8 *puVar6;
  undefined8 *puVar7;
  ulong uVar8;
  undefined8 *__ptr;
  long *plVar9;
  undefined8 *puVar10;
  long lVar11;
  undefined8 uVar12;
  
  __ptr = (undefined8 *)*param_1;
  puVar10 = (undefined8 *)param_1[1];
  lVar11 = (long)puVar10 - (long)__ptr >> 4;
  uVar1 = lVar11 + 1;
  if (uVar1 >> 0x3c != 0) {
    FUN_00acc030(param_1);
LAB_00acc02c:
                    /* WARNING: Subroutine does not return */
    FUN_00440e80();
  }
  uVar8 = param_1[2] - (long)__ptr >> 3;
  if (uVar8 <= uVar1) {
    uVar8 = uVar1;
  }
  if (0x7fffffffffffffef < (ulong)(param_1[2] - (long)__ptr)) {
    uVar8 = 0xfffffffffffffff;
  }
  if (uVar8 == 0) {
    lVar3 = 0;
  }
  else {
    if (uVar8 >> 0x3c != 0) goto LAB_00acc02c;
    lVar3 = _Znwm(uVar8 << 4);
  }
  lVar4 = param_2[1];
  uVar12 = *param_2;
  puVar2 = (undefined8 *)(lVar3 + lVar11 * 0x10);
  puVar2[1] = lVar4;
  *puVar2 = uVar12;
  if (lVar4 != 0) {
    FUN_00c538b0(1,lVar4 + 8);
    __ptr = (undefined8 *)*param_1;
    puVar10 = (undefined8 *)param_1[1];
    lVar11 = (long)puVar10 - (long)__ptr >> 4;
  }
  puVar5 = puVar2 + lVar11 * -2;
  puVar6 = __ptr;
  if (__ptr != puVar10) {
    do {
      uVar12 = *puVar6;
      puVar5[1] = puVar6[1];
      *puVar5 = uVar12;
      puVar7 = puVar6 + 2;
      *puVar6 = 0;
      puVar6[1] = 0;
      puVar5 = puVar5 + 2;
      puVar6 = puVar7;
    } while (puVar7 != puVar10);
    do {
      plVar9 = (long *)__ptr[1];
      if ((plVar9 != (long *)0x0) &&
         (lVar4 = FUN_00c538e0(0xffffffffffffffff,plVar9 + 1), lVar4 == 0)) {
        (**(code **)(*plVar9 + 0x10))(plVar9);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
      }
      __ptr = __ptr + 2;
    } while (__ptr != puVar10);
    __ptr = (undefined8 *)*param_1;
  }
  *param_1 = (long)(puVar2 + lVar11 * -2);
  param_1[1] = (long)(puVar2 + 2);
  param_1[2] = lVar3 + uVar8 * 0x10;
  if (__ptr != (undefined8 *)0x0) {
    _ZdlPv(__ptr);
  }
  return puVar2 + 2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acbed4"></a> `00acbed4` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00acbed8"></a> `00acbed8` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acbedc"></a> `00acbedc` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acbee0"></a> `00acbee0` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acbee4"></a> `00acbee4` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acbee8"></a> `00acbee8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acbeec"></a> `00acbeec` | `14 5c 40 a9` | ldp x20,x23,[x0] | `FALL_THROUGH`
<a id="insn-00acbef0"></a> `00acbef0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acbef4"></a> `00acbef4` | `e8 02 14 cb` | sub x8,x23,x20 | `FALL_THROUGH`
<a id="insn-00acbef8"></a> `00acbef8` | `19 fd 44 93` | asr x25,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00acbefc"></a> `00acbefc` | `28 07 00 91` | add x8,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00acbf00"></a> `00acbf00` | `09 fd 7c d3` | lsr x9,x8,#0x3c | `FALL_THROUGH`
<a id="insn-00acbf04"></a> `00acbf04` | `09 09 00 b5` | cbnz x9,0x00acc024 | `CONDITIONAL_JUMP`
<a id="insn-00acbf08"></a> `00acbf08` | `69 0a 40 f9` | ldr x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00acbf0c"></a> `00acbf0c` | `eb eb 7c b2` | orr x11,xzr,#0x7ffffffffffffff0 | `FALL_THROUGH`
<a id="insn-00acbf10"></a> `00acbf10` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00acbf14"></a> `00acbf14` | `29 01 14 cb` | sub x9,x9,x20 | `FALL_THROUGH`
<a id="insn-00acbf18"></a> `00acbf18` | `2a fd 43 93` | asr x10,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00acbf1c"></a> `00acbf1c` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00acbf20"></a> `00acbf20` | `48 81 88 9a` | csel x8,x10,x8,hi | `FALL_THROUGH`
<a id="insn-00acbf24"></a> `00acbf24` | `3f 01 0b eb` | cmp x9,x11 | `FALL_THROUGH`
<a id="insn-00acbf28"></a> `00acbf28` | `09 00 fe 92` | mov x9,#0xfffffffffffffff | `FALL_THROUGH`
<a id="insn-00acbf2c"></a> `00acbf2c` | `18 31 89 9a` | csel x24,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00acbf30"></a> `00acbf30` | `f8 00 00 b4` | cbz x24,0x00acbf4c | `CONDITIONAL_JUMP`
<a id="insn-00acbf34"></a> `00acbf34` | `08 ff 7c d3` | lsr x8,x24,#0x3c | `FALL_THROUGH`
<a id="insn-00acbf38"></a> `00acbf38` | `a8 07 00 b5` | cbnz x8,0x00acc02c | `CONDITIONAL_JUMP`
<a id="insn-00acbf3c"></a> `00acbf3c` | `00 ef 7c d3` | lsl x0,x24,#0x4 | `FALL_THROUGH`
<a id="insn-00acbf40"></a> `00acbf40` | `d4 2e 06 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00acbf44"></a> `00acbf44` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00acbf48"></a> `00acbf48` | `02 00 00 14` | b 0x00acbf50 | `UNCONDITIONAL_JUMP`
<a id="insn-00acbf4c"></a> `00acbf4c` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00acbf50"></a> `00acbf50` | `c0 02 c0 3d` | ldr q0,[x22] | `FALL_THROUGH`
<a id="insn-00acbf54"></a> `00acbf54` | `b6 12 19 8b` | add x22,x21,x25, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00acbf58"></a> `00acbf58` | `08 3c 18 4e` | mov x8,v0.D[0x1] | `FALL_THROUGH`
<a id="insn-00acbf5c"></a> `00acbf5c` | `c0 02 80 3d` | str q0,[x22] | `FALL_THROUGH`
<a id="insn-00acbf60"></a> `00acbf60` | `e8 00 00 b4` | cbz x8,0x00acbf7c | `CONDITIONAL_JUMP`
<a id="insn-00acbf64"></a> `00acbf64` | `01 21 00 91` | add x1,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00acbf68"></a> `00acbf68` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00acbf6c"></a> `00acbf6c` | `51 1e 06 94` | bl 0x00c538b0 | `UNCONDITIONAL_CALL`
<a id="insn-00acbf70"></a> `00acbf70` | `74 5e 40 a9` | ldp x20,x23,[x19] | `FALL_THROUGH`
<a id="insn-00acbf74"></a> `00acbf74` | `e8 02 14 cb` | sub x8,x23,x20 | `FALL_THROUGH`
<a id="insn-00acbf78"></a> `00acbf78` | `19 fd 44 93` | asr x25,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00acbf7c"></a> `00acbf7c` | `b8 12 18 8b` | add x24,x21,x24, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00acbf80"></a> `00acbf80` | `d9 12 19 cb` | sub x25,x22,x25, LSL #0x4 | `FALL_THROUGH`
<a id="insn-00acbf84"></a> `00acbf84` | `9f 02 17 eb` | cmp x20,x23 | `FALL_THROUGH`
<a id="insn-00acbf88"></a> `00acbf88` | `d5 42 00 91` | add x21,x22,#0x10 | `FALL_THROUGH`
<a id="insn-00acbf8c"></a> `00acbf8c` | `40 03 00 54` | b.eq 0x00acbff4 | `CONDITIONAL_JUMP`
<a id="insn-00acbf90"></a> `00acbf90` | `e8 03 19 aa` | mov x8,x25 | `FALL_THROUGH`
<a id="insn-00acbf94"></a> `00acbf94` | `e9 03 14 aa` | mov x9,x20 | `FALL_THROUGH`
<a id="insn-00acbf98"></a> `00acbf98` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00acbf9c"></a> `00acbf9c` | `00 05 81 3c` | str q0,[x8], #0x10 | `FALL_THROUGH`
<a id="insn-00acbfa0"></a> `00acbfa0` | `3f 7d 81 a8` | stp xzr,xzr,[x9], #0x10 | `FALL_THROUGH`
<a id="insn-00acbfa4"></a> `00acbfa4` | `3f 01 17 eb` | cmp x9,x23 | `FALL_THROUGH`
<a id="insn-00acbfa8"></a> `00acbfa8` | `81 ff ff 54` | b.ne 0x00acbf98 | `CONDITIONAL_JUMP`
<a id="insn-00acbfac"></a> `00acbfac` | `04 00 00 14` | b 0x00acbfbc | `UNCONDITIONAL_JUMP`
<a id="insn-00acbfb0"></a> `00acbfb0` | `94 42 00 91` | add x20,x20,#0x10 | `FALL_THROUGH`
<a id="insn-00acbfb4"></a> `00acbfb4` | `9f 02 17 eb` | cmp x20,x23 | `FALL_THROUGH`
<a id="insn-00acbfb8"></a> `00acbfb8` | `c0 01 00 54` | b.eq 0x00acbff0 | `CONDITIONAL_JUMP`
<a id="insn-00acbfbc"></a> `00acbfbc` | `96 06 40 f9` | ldr x22,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00acbfc0"></a> `00acbfc0` | `96 ff ff b4` | cbz x22,0x00acbfb0 | `CONDITIONAL_JUMP`
<a id="insn-00acbfc4"></a> `00acbfc4` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00acbfc8"></a> `00acbfc8` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acbfcc"></a> `00acbfcc` | `45 1e 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00acbfd0"></a> `00acbfd0` | `00 ff ff b5` | cbnz x0,0x00acbfb0 | `CONDITIONAL_JUMP`
<a id="insn-00acbfd4"></a> `00acbfd4` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00acbfd8"></a> `00acbfd8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00acbfdc"></a> `00acbfdc` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acbfe0"></a> `00acbfe0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbfe4"></a> `00acbfe4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00acbfe8"></a> `00acbfe8` | `a6 2e 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00acbfec"></a> `00acbfec` | `f1 ff ff 17` | b 0x00acbfb0 | `UNCONDITIONAL_JUMP`
<a id="insn-00acbff0"></a> `00acbff0` | `74 02 40 f9` | ldr x20,[x19] | `FALL_THROUGH`
<a id="insn-00acbff4"></a> `00acbff4` | `79 56 00 a9` | stp x25,x21,[x19] | `FALL_THROUGH`
<a id="insn-00acbff8"></a> `00acbff8` | `78 0a 00 f9` | str x24,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00acbffc"></a> `00acbffc` | `74 00 00 b4` | cbz x20,0x00acc008 | `CONDITIONAL_JUMP`
<a id="insn-00acc000"></a> `00acc000` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acc004"></a> `00acc004` | `ab 2e 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00acc008"></a> `00acc008` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00acc00c"></a> `00acc00c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acc010"></a> `00acc010` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acc014"></a> `00acc014` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acc018"></a> `00acc018` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acc01c"></a> `00acc01c` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00acc020"></a> `00acc020` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acc024"></a> `00acc024` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acc028"></a> `00acc028` | `02 00 00 94` | bl 0x00acc030 | `UNCONDITIONAL_CALL`
<a id="insn-00acc02c"></a> `00acc02c` | `95 d3 e5 97` | bl 0x00440e80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acbed4`](#insn-00acbed4) 範囲 `[['00acbed4', '00acbf07']]`
  - `CONDITIONAL_JUMP` [`00acbf04`](#insn-00acbf04) → [`00acc024`](#insn-00acc024)
  - `FALL_THROUGH` [`00acbf04`](#insn-00acbf04) → [`00acbf08`](#insn-00acbf08)
- ブロック [`00acbf08`](#insn-00acbf08) 範囲 `[['00acbf08', '00acbf33']]`
  - `CONDITIONAL_JUMP` [`00acbf30`](#insn-00acbf30) → [`00acbf4c`](#insn-00acbf4c)
  - `FALL_THROUGH` [`00acbf30`](#insn-00acbf30) → [`00acbf34`](#insn-00acbf34)
- ブロック [`00acbf34`](#insn-00acbf34) 範囲 `[['00acbf34', '00acbf3b']]`
  - `CONDITIONAL_JUMP` [`00acbf38`](#insn-00acbf38) → [`00acc02c`](#insn-00acc02c)
  - `FALL_THROUGH` [`00acbf38`](#insn-00acbf38) → [`00acbf3c`](#insn-00acbf3c)
- ブロック [`00acbf3c`](#insn-00acbf3c) 範囲 `[['00acbf3c', '00acbf4b']]`
  - `UNCONDITIONAL_JUMP` [`00acbf48`](#insn-00acbf48) → [`00acbf50`](#insn-00acbf50)
- ブロック [`00acbf4c`](#insn-00acbf4c) 範囲 `[['00acbf4c', '00acbf4f']]`
  - `FALL_THROUGH` [`00acbf4c`](#insn-00acbf4c) → [`00acbf50`](#insn-00acbf50)
- ブロック [`00acbf50`](#insn-00acbf50) 範囲 `[['00acbf50', '00acbf63']]`
  - `CONDITIONAL_JUMP` [`00acbf60`](#insn-00acbf60) → [`00acbf7c`](#insn-00acbf7c)
  - `FALL_THROUGH` [`00acbf60`](#insn-00acbf60) → [`00acbf64`](#insn-00acbf64)
- ブロック [`00acbf64`](#insn-00acbf64) 範囲 `[['00acbf64', '00acbf7b']]`
  - `FALL_THROUGH` [`00acbf78`](#insn-00acbf78) → [`00acbf7c`](#insn-00acbf7c)
- ブロック [`00acbf7c`](#insn-00acbf7c) 範囲 `[['00acbf7c', '00acbf8f']]`
  - `CONDITIONAL_JUMP` [`00acbf8c`](#insn-00acbf8c) → [`00acbff4`](#insn-00acbff4)
  - `FALL_THROUGH` [`00acbf8c`](#insn-00acbf8c) → [`00acbf90`](#insn-00acbf90)
- ブロック [`00acbf90`](#insn-00acbf90) 範囲 `[['00acbf90', '00acbf97']]`
  - `FALL_THROUGH` [`00acbf94`](#insn-00acbf94) → [`00acbf98`](#insn-00acbf98)
- ブロック [`00acbf98`](#insn-00acbf98) 範囲 `[['00acbf98', '00acbfab']]`
  - `CONDITIONAL_JUMP` [`00acbfa8`](#insn-00acbfa8) → [`00acbf98`](#insn-00acbf98)
  - `FALL_THROUGH` [`00acbfa8`](#insn-00acbfa8) → [`00acbfac`](#insn-00acbfac)
- ブロック [`00acbfac`](#insn-00acbfac) 範囲 `[['00acbfac', '00acbfaf']]`
  - `UNCONDITIONAL_JUMP` [`00acbfac`](#insn-00acbfac) → [`00acbfbc`](#insn-00acbfbc)
- ブロック [`00acbfb0`](#insn-00acbfb0) 範囲 `[['00acbfb0', '00acbfbb']]`
  - `CONDITIONAL_JUMP` [`00acbfb8`](#insn-00acbfb8) → [`00acbff0`](#insn-00acbff0)
  - `FALL_THROUGH` [`00acbfb8`](#insn-00acbfb8) → [`00acbfbc`](#insn-00acbfbc)
- ブロック [`00acbfbc`](#insn-00acbfbc) 範囲 `[['00acbfbc', '00acbfc3']]`
  - `CONDITIONAL_JUMP` [`00acbfc0`](#insn-00acbfc0) → [`00acbfb0`](#insn-00acbfb0)
  - `FALL_THROUGH` [`00acbfc0`](#insn-00acbfc0) → [`00acbfc4`](#insn-00acbfc4)
- ブロック [`00acbfc4`](#insn-00acbfc4) 範囲 `[['00acbfc4', '00acbfd3']]`
  - `CONDITIONAL_JUMP` [`00acbfd0`](#insn-00acbfd0) → [`00acbfb0`](#insn-00acbfb0)
  - `FALL_THROUGH` [`00acbfd0`](#insn-00acbfd0) → [`00acbfd4`](#insn-00acbfd4)
- ブロック [`00acbfd4`](#insn-00acbfd4) 範囲 `[['00acbfd4', '00acbfef']]`
  - `UNCONDITIONAL_JUMP` [`00acbfec`](#insn-00acbfec) → [`00acbfb0`](#insn-00acbfb0)
- ブロック [`00acbff0`](#insn-00acbff0) 範囲 `[['00acbff0', '00acbff3']]`
  - `FALL_THROUGH` [`00acbff0`](#insn-00acbff0) → [`00acbff4`](#insn-00acbff4)
- ブロック [`00acbff4`](#insn-00acbff4) 範囲 `[['00acbff4', '00acbfff']]`
  - `CONDITIONAL_JUMP` [`00acbffc`](#insn-00acbffc) → [`00acc008`](#insn-00acc008)
  - `FALL_THROUGH` [`00acbffc`](#insn-00acbffc) → [`00acc000`](#insn-00acc000)
- ブロック [`00acc000`](#insn-00acc000) 範囲 `[['00acc000', '00acc007']]`
  - `FALL_THROUGH` [`00acc004`](#insn-00acc004) → [`00acc008`](#insn-00acc008)
- ブロック [`00acc008`](#insn-00acc008) 範囲 `[['00acc008', '00acc023']]`
- ブロック [`00acc024`](#insn-00acc024) 範囲 `[['00acc024', '00acc02b']]`
  - `FALL_THROUGH` [`00acc028`](#insn-00acc028) → [`00acc02c`](#insn-00acc02c)
- ブロック [`00acc02c`](#insn-00acc02c) 範囲 `[['00acc02c', '00acc02f']]`

## 命令位置別の参照

- [`00acbed4`](#insn-00acbed4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbed8`](#insn-00acbed8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbedc`](#insn-00acbedc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbee0`](#insn-00acbee0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbee4`](#insn-00acbee4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf04`](#insn-00acbf04) → [`00acc024`](#insn-00acc024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf30`](#insn-00acbf30) → [`00acbf4c`](#insn-00acbf4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf38`](#insn-00acbf38) → [`00acc02c`](#insn-00acc02c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf40`](#insn-00acbf40) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00acbf48`](#insn-00acbf48) → [`00acbf50`](#insn-00acbf50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf60`](#insn-00acbf60) → [`00acbf7c`](#insn-00acbf7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf6c`](#insn-00acbf6c) → [`00c538b0`](../00c53/00c538b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538b0` · 推定シンボル `None` · 推定型 `None`
- [`00acbf8c`](#insn-00acbf8c) → [`00acbff4`](#insn-00acbff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfa8`](#insn-00acbfa8) → [`00acbf98`](#insn-00acbf98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfac`](#insn-00acbfac) → [`00acbfbc`](#insn-00acbfbc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfb8`](#insn-00acbfb8) → [`00acbff0`](#insn-00acbff0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfc0`](#insn-00acbfc0) → [`00acbfb0`](#insn-00acbfb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfcc`](#insn-00acbfcc) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00acbfd0`](#insn-00acbfd0) → [`00acbfb0`](#insn-00acbfb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbfe8`](#insn-00acbfe8) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00acbfec`](#insn-00acbfec) → [`00acbfb0`](#insn-00acbfb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbffc`](#insn-00acbffc) → [`00acc008`](#insn-00acc008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc004`](#insn-00acc004) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00acc00c`](#insn-00acc00c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc010`](#insn-00acc010) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc014`](#insn-00acc014) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc018`](#insn-00acc018) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc01c`](#insn-00acc01c) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acc028`](#insn-00acc028) → [`00acc030`](../00acc/00acc030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00acc030` · 推定シンボル `None` · 推定型 `None`
- [`00acc02c`](#insn-00acc02c) → [`00440e80`](../00440/00440e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00440e80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acbed4`](#insn-00acbed4)

~~~json
{
  "source": "00acbed4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbed8`](#insn-00acbed8)

~~~json
{
  "source": "00acbed8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbedc`](#insn-00acbedc)

~~~json
{
  "source": "00acbedc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbee0`](#insn-00acbee0)

~~~json
{
  "source": "00acbee0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbee4`](#insn-00acbee4)

~~~json
{
  "source": "00acbee4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf04`](#insn-00acbf04)

~~~json
{
  "source": "00acbf04",
  "target": "00acc024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf30`](#insn-00acbf30)

~~~json
{
  "source": "00acbf30",
  "target": "00acbf4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf38`](#insn-00acbf38)

~~~json
{
  "source": "00acbf38",
  "target": "00acc02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf40`](#insn-00acbf40)

~~~json
{
  "source": "00acbf40",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbf48`](#insn-00acbf48)

~~~json
{
  "source": "00acbf48",
  "target": "00acbf50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf60`](#insn-00acbf60)

~~~json
{
  "source": "00acbf60",
  "target": "00acbf7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf6c`](#insn-00acbf6c)

~~~json
{
  "source": "00acbf6c",
  "target": "00c538b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbf8c`](#insn-00acbf8c)

~~~json
{
  "source": "00acbf8c",
  "target": "00acbff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfa8`](#insn-00acbfa8)

~~~json
{
  "source": "00acbfa8",
  "target": "00acbf98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfac`](#insn-00acbfac)

~~~json
{
  "source": "00acbfac",
  "target": "00acbfbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfb8`](#insn-00acbfb8)

~~~json
{
  "source": "00acbfb8",
  "target": "00acbff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfc0`](#insn-00acbfc0)

~~~json
{
  "source": "00acbfc0",
  "target": "00acbfb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfcc`](#insn-00acbfcc)

~~~json
{
  "source": "00acbfcc",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbfd0`](#insn-00acbfd0)

~~~json
{
  "source": "00acbfd0",
  "target": "00acbfb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbfe8`](#insn-00acbfe8)

~~~json
{
  "source": "00acbfe8",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbfec`](#insn-00acbfec)

~~~json
{
  "source": "00acbfec",
  "target": "00acbfb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbffc`](#insn-00acbffc)

~~~json
{
  "source": "00acbffc",
  "target": "00acc008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc004`](#insn-00acc004)

~~~json
{
  "source": "00acc004",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acc00c`](#insn-00acc00c)

~~~json
{
  "source": "00acc00c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc010`](#insn-00acc010)

~~~json
{
  "source": "00acc010",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc014`](#insn-00acc014)

~~~json
{
  "source": "00acc014",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc018`](#insn-00acc018)

~~~json
{
  "source": "00acc018",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc01c`](#insn-00acc01c)

~~~json
{
  "source": "00acc01c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acc028`](#insn-00acc028)

~~~json
{
  "source": "00acc028",
  "target": "00acc030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acc02c`](#insn-00acc02c)

~~~json
{
  "source": "00acc02c",
  "target": "00440e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
