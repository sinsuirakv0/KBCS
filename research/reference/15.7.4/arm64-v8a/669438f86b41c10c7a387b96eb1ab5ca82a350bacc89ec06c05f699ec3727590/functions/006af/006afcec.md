# 006afcec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `006afcec`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afcec.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/reference_unresolved-0009.md#compare-c588ecef966704efb89047846ce76089)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `006d9aa8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9aa8.md) · 移動量 `+0x29dbc`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0030.md#compare-456843a9153dcb685344f93d4f3cc671)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006afcec",
  "name": "FUN_006afcec",
  "size": 300,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c1a5e05d50490ced9691a512ba9678c6e317a787834eb3f5720a4994ad1bc76a",
  "source_text_sha256": "c1a5e05d50490ced9691a512ba9678c6e317a787834eb3f5720a4994ad1bc76a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006afcec",
        "006afe13"
      ],
      [
        "006afe38",
        "006afe3b"
      ]
    ],
    "bytes_sha256": "9ecc3a2f49e41e96642a03292b568207182f046d45a32713b362fe336313b015",
    "instruction_count": 75,
    "instruction_bytes": 300,
    "body_bytes": 300,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00457e1c](../00457/00457e1c.md)
- [00459efc](../00459/00459efc.md)
- [00666298](../00666/00666298.md)
- [006abb50](../006ab/006abb50.md)
- [0081f580](../0081f/0081f580.md)
- [00bd6e60](../00bd6/00bd6e60.md)
- [00bd6e90](../00bd6/00bd6e90.md)
- [00bdb030](../00bdb/00bdb030.md)
- [00bdb090](../00bdb/00bdb090.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1537 bytes

~~~c

void FUN_006afcec(long param_1,undefined8 param_2,int *param_3)

{
  int iVar1;
  long lVar2;
  long *plVar3;
  undefined8 uVar4;
  long lVar5;
  undefined8 uVar6;
  long lVar7;
  undefined8 local_48;
  long *local_40;
  long local_38;
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  iVar1 = *param_3;
  if (iVar1 == 4) {
    lVar7 = *(long *)(param_1 + 8);
    FUN_006abb50(lVar7);
    lVar5 = FUN_0081f580();
    local_48 = *(undefined8 *)(lVar7 + 0x100);
    local_40 = *(long **)(lVar7 + 0x108);
    if (local_40 != (long *)0x0) {
      FUN_00bd6e60(1,local_40 + 1);
    }
    FUN_00666298(lVar5 + 0x16f0,&local_48);
    plVar3 = local_40;
    if ((local_40 != (long *)0x0) &&
       (lVar5 = FUN_00bd6e90(0xffffffffffffffff,local_40 + 1), lVar5 == 0)) {
      (**(code **)(*plVar3 + 0x10))(plVar3);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar3);
    }
    lVar5 = FUN_0081f580();
    *(undefined4 *)(lVar5 + 0x472b28) = 1;
  }
  else {
    if (iVar1 == 3) {
      uVar4 = FUN_00457e1c();
      if (*(long *)(lVar2 + 0x28) == local_38) {
        uVar6 = 0xb;
        goto LAB_006afd58;
      }
      goto LAB_006afe38;
    }
    if (iVar1 == 0) {
      uVar4 = FUN_00457e1c();
      if (*(long *)(lVar2 + 0x28) != local_38) goto LAB_006afe38;
      uVar6 = 10;
LAB_006afd58:
      FUN_00459efc(uVar4,uVar6,0);
      return;
    }
  }
  if (*(long *)(lVar2 + 0x28) == local_38) {
    return;
  }
LAB_006afe38:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006afcec"></a> `006afcec` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-006afcf0"></a> `006afcf0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006afcf4"></a> `006afcf4` | `f5 1b 00 f9` | str x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006afcf8"></a> `006afcf8` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006afcfc"></a> `006afcfc` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-006afd00"></a> `006afd00` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-006afd04"></a> `006afd04` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-006afd08"></a> `006afd08` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-006afd0c"></a> `006afd0c` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-006afd10"></a> `006afd10` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-006afd14"></a> `006afd14` | `e0 02 00 54` | b.eq 0x006afd70 | `CONDITIONAL_JUMP`
<a id="insn-006afd18"></a> `006afd18` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-006afd1c"></a> `006afd1c` | `20 01 00 54` | b.eq 0x006afd40 | `CONDITIONAL_JUMP`
<a id="insn-006afd20"></a> `006afd20` | `88 06 00 35` | cbnz w8,0x006afdf0 | `CONDITIONAL_JUMP`
<a id="insn-006afd24"></a> `006afd24` | `3e a0 f6 97` | bl 0x00457e1c | `UNCONDITIONAL_CALL`
<a id="insn-006afd28"></a> `006afd28` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-006afd2c"></a> `006afd2c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-006afd30"></a> `006afd30` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006afd34"></a> `006afd34` | `21 08 00 54` | b.ne 0x006afe38 | `CONDITIONAL_JUMP`
<a id="insn-006afd38"></a> `006afd38` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-006afd3c"></a> `006afd3c` | `07 00 00 14` | b 0x006afd58 | `UNCONDITIONAL_JUMP`
<a id="insn-006afd40"></a> `006afd40` | `37 a0 f6 97` | bl 0x00457e1c | `UNCONDITIONAL_CALL`
<a id="insn-006afd44"></a> `006afd44` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-006afd48"></a> `006afd48` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-006afd4c"></a> `006afd4c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006afd50"></a> `006afd50` | `41 07 00 54` | b.ne 0x006afe38 | `CONDITIONAL_JUMP`
<a id="insn-006afd54"></a> `006afd54` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-006afd58"></a> `006afd58` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-006afd5c"></a> `006afd5c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006afd60"></a> `006afd60` | `f5 1b 40 f9` | ldr x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006afd64"></a> `006afd64` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006afd68"></a> `006afd68` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-006afd6c"></a> `006afd6c` | `64 a8 f6 17` | b 0x00459efc | `CALL_TERMINATOR`
<a id="insn-006afd70"></a> `006afd70` | `14 04 40 f9` | ldr x20,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-006afd74"></a> `006afd74` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006afd78"></a> `006afd78` | `76 ef ff 97` | bl 0x006abb50 | `UNCONDITIONAL_CALL`
<a id="insn-006afd7c"></a> `006afd7c` | `01 be 05 94` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-006afd80"></a> `006afd80` | `89 22 50 a9` | ldp x9,x8,[x20, #0x100] | `FALL_THROUGH`
<a id="insn-006afd84"></a> `006afd84` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-006afd88"></a> `006afd88` | `14 de 82 52` | mov w20,#0x16f0 | `FALL_THROUGH`
<a id="insn-006afd8c"></a> `006afd8c` | `e9 a3 00 a9` | stp x9,x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-006afd90"></a> `006afd90` | `88 00 00 b4` | cbz x8,0x006afda0 | `CONDITIONAL_JUMP`
<a id="insn-006afd94"></a> `006afd94` | `01 21 00 91` | add x1,x8,#0x8 | `FALL_THROUGH`
<a id="insn-006afd98"></a> `006afd98` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-006afd9c"></a> `006afd9c` | `31 9c 14 94` | bl 0x00bd6e60 | `UNCONDITIONAL_CALL`
<a id="insn-006afda0"></a> `006afda0` | `60 02 14 8b` | add x0,x19,x20 | `FALL_THROUGH`
<a id="insn-006afda4"></a> `006afda4` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-006afda8"></a> `006afda8` | `3c d9 fe 97` | bl 0x00666298 | `UNCONDITIONAL_CALL`
<a id="insn-006afdac"></a> `006afdac` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006afdb0"></a> `006afdb0` | `73 01 00 b4` | cbz x19,0x006afddc | `CONDITIONAL_JUMP`
<a id="insn-006afdb4"></a> `006afdb4` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-006afdb8"></a> `006afdb8` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-006afdbc"></a> `006afdbc` | `35 9c 14 94` | bl 0x00bd6e90 | `UNCONDITIONAL_CALL`
<a id="insn-006afdc0"></a> `006afdc0` | `e0 00 00 b5` | cbnz x0,0x006afddc | `CONDITIONAL_JUMP`
<a id="insn-006afdc4"></a> `006afdc4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-006afdc8"></a> `006afdc8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-006afdcc"></a> `006afdcc` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-006afdd0"></a> `006afdd0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-006afdd4"></a> `006afdd4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-006afdd8"></a> `006afdd8` | `96 ac 14 94` | bl 0x00bdb030 | `UNCONDITIONAL_CALL`
<a id="insn-006afddc"></a> `006afddc` | `e9 bd 05 94` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-006afde0"></a> `006afde0` | `08 65 85 52` | mov w8,#0x2b28 | `FALL_THROUGH`
<a id="insn-006afde4"></a> `006afde4` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-006afde8"></a> `006afde8` | `e8 08 a0 72` | movk w8,#0x47, LSL #16 | `FALL_THROUGH`
<a id="insn-006afdec"></a> `006afdec` | `09 68 28 b8` | str w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-006afdf0"></a> `006afdf0` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-006afdf4"></a> `006afdf4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-006afdf8"></a> `006afdf8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006afdfc"></a> `006afdfc` | `e1 01 00 54` | b.ne 0x006afe38 | `CONDITIONAL_JUMP`
<a id="insn-006afe00"></a> `006afe00` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006afe04"></a> `006afe04` | `f5 1b 40 f9` | ldr x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006afe08"></a> `006afe08` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006afe0c"></a> `006afe0c` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-006afe10"></a> `006afe10` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-006afe38"></a> `006afe38` | `96 ac 14 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006afcec`](#insn-006afcec) 範囲 `[['006afcec', '006afd17']]`
  - `CONDITIONAL_JUMP` [`006afd14`](#insn-006afd14) → [`006afd70`](#insn-006afd70)
  - `FALL_THROUGH` [`006afd14`](#insn-006afd14) → [`006afd18`](#insn-006afd18)
- ブロック [`006afd18`](#insn-006afd18) 範囲 `[['006afd18', '006afd1f']]`
  - `CONDITIONAL_JUMP` [`006afd1c`](#insn-006afd1c) → [`006afd40`](#insn-006afd40)
  - `FALL_THROUGH` [`006afd1c`](#insn-006afd1c) → [`006afd20`](#insn-006afd20)
- ブロック [`006afd20`](#insn-006afd20) 範囲 `[['006afd20', '006afd23']]`
  - `CONDITIONAL_JUMP` [`006afd20`](#insn-006afd20) → [`006afdf0`](#insn-006afdf0)
  - `FALL_THROUGH` [`006afd20`](#insn-006afd20) → [`006afd24`](#insn-006afd24)
- ブロック [`006afd24`](#insn-006afd24) 範囲 `[['006afd24', '006afd37']]`
  - `CONDITIONAL_JUMP` [`006afd34`](#insn-006afd34) → [`006afe38`](#insn-006afe38)
  - `FALL_THROUGH` [`006afd34`](#insn-006afd34) → [`006afd38`](#insn-006afd38)
- ブロック [`006afd38`](#insn-006afd38) 範囲 `[['006afd38', '006afd3f']]`
  - `UNCONDITIONAL_JUMP` [`006afd3c`](#insn-006afd3c) → [`006afd58`](#insn-006afd58)
- ブロック [`006afd40`](#insn-006afd40) 範囲 `[['006afd40', '006afd53']]`
  - `CONDITIONAL_JUMP` [`006afd50`](#insn-006afd50) → [`006afe38`](#insn-006afe38)
  - `FALL_THROUGH` [`006afd50`](#insn-006afd50) → [`006afd54`](#insn-006afd54)
- ブロック [`006afd54`](#insn-006afd54) 範囲 `[['006afd54', '006afd57']]`
  - `FALL_THROUGH` [`006afd54`](#insn-006afd54) → [`006afd58`](#insn-006afd58)
- ブロック [`006afd58`](#insn-006afd58) 範囲 `[['006afd58', '006afd6f']]`
- ブロック [`006afd70`](#insn-006afd70) 範囲 `[['006afd70', '006afd93']]`
  - `CONDITIONAL_JUMP` [`006afd90`](#insn-006afd90) → [`006afda0`](#insn-006afda0)
  - `FALL_THROUGH` [`006afd90`](#insn-006afd90) → [`006afd94`](#insn-006afd94)
- ブロック [`006afd94`](#insn-006afd94) 範囲 `[['006afd94', '006afd9f']]`
  - `FALL_THROUGH` [`006afd9c`](#insn-006afd9c) → [`006afda0`](#insn-006afda0)
- ブロック [`006afda0`](#insn-006afda0) 範囲 `[['006afda0', '006afdb3']]`
  - `CONDITIONAL_JUMP` [`006afdb0`](#insn-006afdb0) → [`006afddc`](#insn-006afddc)
  - `FALL_THROUGH` [`006afdb0`](#insn-006afdb0) → [`006afdb4`](#insn-006afdb4)
- ブロック [`006afdb4`](#insn-006afdb4) 範囲 `[['006afdb4', '006afdc3']]`
  - `CONDITIONAL_JUMP` [`006afdc0`](#insn-006afdc0) → [`006afddc`](#insn-006afddc)
  - `FALL_THROUGH` [`006afdc0`](#insn-006afdc0) → [`006afdc4`](#insn-006afdc4)
- ブロック [`006afdc4`](#insn-006afdc4) 範囲 `[['006afdc4', '006afddb']]`
  - `FALL_THROUGH` [`006afdd8`](#insn-006afdd8) → [`006afddc`](#insn-006afddc)
- ブロック [`006afddc`](#insn-006afddc) 範囲 `[['006afddc', '006afdef']]`
  - `FALL_THROUGH` [`006afdec`](#insn-006afdec) → [`006afdf0`](#insn-006afdf0)
- ブロック [`006afdf0`](#insn-006afdf0) 範囲 `[['006afdf0', '006afdff']]`
  - `CONDITIONAL_JUMP` [`006afdfc`](#insn-006afdfc) → [`006afe38`](#insn-006afe38)
  - `FALL_THROUGH` [`006afdfc`](#insn-006afdfc) → [`006afe00`](#insn-006afe00)
- ブロック [`006afe00`](#insn-006afe00) 範囲 `[['006afe00', '006afe13']]`
- ブロック [`006afe38`](#insn-006afe38) 範囲 `[['006afe38', '006afe3b']]`

## 命令位置別の参照

- [`006afcf0`](#insn-006afcf0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afcf4`](#insn-006afcf4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afcf8`](#insn-006afcf8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afd08`](#insn-006afd08) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afd14`](#insn-006afd14) → [`006afd70`](#insn-006afd70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afd1c`](#insn-006afd1c) → [`006afd40`](#insn-006afd40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afd20`](#insn-006afd20) → [`006afdf0`](#insn-006afdf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afd24`](#insn-006afd24) → [`00457e1c`](../00457/00457e1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00457e1c` · 推定シンボル `None` · 推定型 `None`
- [`006afd2c`](#insn-006afd2c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afd34`](#insn-006afd34) → [`006afe38`](#insn-006afe38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afd3c`](#insn-006afd3c) → [`006afd58`](#insn-006afd58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afd40`](#insn-006afd40) → [`00457e1c`](../00457/00457e1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00457e1c` · 推定シンボル `None` · 推定型 `None`
- [`006afd48`](#insn-006afd48) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afd50`](#insn-006afd50) → [`006afe38`](#insn-006afe38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afd5c`](#insn-006afd5c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afd60`](#insn-006afd60) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afd64`](#insn-006afd64) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afd6c`](#insn-006afd6c) → [`00459efc`](../00459/00459efc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00459efc` · 推定シンボル `None` · 推定型 `None`
- [`006afd78`](#insn-006afd78) → [`006abb50`](../006ab/006abb50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006abb50` · 推定シンボル `None` · 推定型 `None`
- [`006afd7c`](#insn-006afd7c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`006afd8c`](#insn-006afd8c) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afd90`](#insn-006afd90) → [`006afda0`](#insn-006afda0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afd9c`](#insn-006afd9c) → [`00bd6e60`](../00bd6/00bd6e60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e60` · 推定シンボル `None` · 推定型 `None`
- [`006afda8`](#insn-006afda8) → [`00666298`](../00666/00666298.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00666298` · 推定シンボル `None` · 推定型 `None`
- [`006afdac`](#insn-006afdac) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afdb0`](#insn-006afdb0) → [`006afddc`](#insn-006afddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afdbc`](#insn-006afdbc) → [`00bd6e90`](../00bd6/00bd6e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e90` · 推定シンボル `None` · 推定型 `None`
- [`006afdc0`](#insn-006afdc0) → [`006afddc`](#insn-006afddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afdd8`](#insn-006afdd8) → [`00bdb030`](../00bdb/00bdb030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb030` · 推定シンボル `None` · 推定型 `None`
- [`006afddc`](#insn-006afddc) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`006afdf4`](#insn-006afdf4) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afdfc`](#insn-006afdfc) → [`006afe38`](#insn-006afe38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afe00`](#insn-006afe00) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afe04`](#insn-006afe04) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afe08`](#insn-006afe08) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afe38`](#insn-006afe38) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006afcf0`](#insn-006afcf0)

~~~json
{
  "source": "006afcf0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afcf4`](#insn-006afcf4)

~~~json
{
  "source": "006afcf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afcf8`](#insn-006afcf8)

~~~json
{
  "source": "006afcf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afd08`](#insn-006afd08)

~~~json
{
  "source": "006afd08",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afd14`](#insn-006afd14)

~~~json
{
  "source": "006afd14",
  "target": "006afd70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afd1c`](#insn-006afd1c)

~~~json
{
  "source": "006afd1c",
  "target": "006afd40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afd20`](#insn-006afd20)

~~~json
{
  "source": "006afd20",
  "target": "006afdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afd24`](#insn-006afd24)

~~~json
{
  "source": "006afd24",
  "target": "00457e1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006afd2c`](#insn-006afd2c)

~~~json
{
  "source": "006afd2c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afd34`](#insn-006afd34)

~~~json
{
  "source": "006afd34",
  "target": "006afe38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afd3c`](#insn-006afd3c)

~~~json
{
  "source": "006afd3c",
  "target": "006afd58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afd40`](#insn-006afd40)

~~~json
{
  "source": "006afd40",
  "target": "00457e1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006afd48`](#insn-006afd48)

~~~json
{
  "source": "006afd48",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afd50`](#insn-006afd50)

~~~json
{
  "source": "006afd50",
  "target": "006afe38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afd5c`](#insn-006afd5c)

~~~json
{
  "source": "006afd5c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afd60`](#insn-006afd60)

~~~json
{
  "source": "006afd60",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afd64`](#insn-006afd64)

~~~json
{
  "source": "006afd64",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afd6c`](#insn-006afd6c)

~~~json
{
  "source": "006afd6c",
  "target": "00459efc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006afd78`](#insn-006afd78)

~~~json
{
  "source": "006afd78",
  "target": "006abb50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006afd7c`](#insn-006afd7c)

~~~json
{
  "source": "006afd7c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006afd8c`](#insn-006afd8c)

~~~json
{
  "source": "006afd8c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afd90`](#insn-006afd90)

~~~json
{
  "source": "006afd90",
  "target": "006afda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afd9c`](#insn-006afd9c)

~~~json
{
  "source": "006afd9c",
  "target": "00bd6e60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006afda8`](#insn-006afda8)

~~~json
{
  "source": "006afda8",
  "target": "00666298",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006afdac`](#insn-006afdac)

~~~json
{
  "source": "006afdac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afdb0`](#insn-006afdb0)

~~~json
{
  "source": "006afdb0",
  "target": "006afddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afdbc`](#insn-006afdbc)

~~~json
{
  "source": "006afdbc",
  "target": "00bd6e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006afdc0`](#insn-006afdc0)

~~~json
{
  "source": "006afdc0",
  "target": "006afddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afdd8`](#insn-006afdd8)

~~~json
{
  "source": "006afdd8",
  "target": "00bdb030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006afddc`](#insn-006afddc)

~~~json
{
  "source": "006afddc",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006afdf4`](#insn-006afdf4)

~~~json
{
  "source": "006afdf4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afdfc`](#insn-006afdfc)

~~~json
{
  "source": "006afdfc",
  "target": "006afe38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afe00`](#insn-006afe00)

~~~json
{
  "source": "006afe00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afe04`](#insn-006afe04)

~~~json
{
  "source": "006afe04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afe08`](#insn-006afe08)

~~~json
{
  "source": "006afe08",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afe38`](#insn-006afe38)

~~~json
{
  "source": "006afe38",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
