# 00ba6dbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ba6d78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6d78.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0077.md#compare-0d4963b0fe51a02787d188813bfc7d7e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c23804`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23804.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0075.md#compare-2327850a2b880e053baac11d66bfe4bd)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ba6dbc",
  "name": "FUN_00ba6dbc",
  "size": 280,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "38941201ec23c4f6a808348bebfc7f56eaf9371edc74e4fcbc8e9130d9d606b4",
  "source_text_sha256": "38941201ec23c4f6a808348bebfc7f56eaf9371edc74e4fcbc8e9130d9d606b4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ba6dbc",
        "00ba6ed3"
      ]
    ],
    "bytes_sha256": "828a32b171a2fcb9a3afca7b1b87ef07ed3399b30763c90befd69fb47d1a1a01",
    "instruction_count": 70,
    "instruction_bytes": 280,
    "body_bytes": 280,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00ba5108](../00ba5/00ba5108.md)

## 呼び出し先

- [00b890e8](../00b89/00b890e8.md)
- [00bb8bd4](../00bb8/00bb8bd4.md)
- [00bd6e60](../00bd6/00bd6e60.md)
- [00bd6e90](../00bd6/00bd6e90.md)
- [00be0ee0](../00be0/00be0ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1823 bytes

~~~c

void FUN_00ba6dbc(long param_1,long param_2)

{
  undefined *puVar1;
  long lVar2;
  ulong uVar3;
  ulong uVar4;
  long lVar5;
  long *plVar6;
  long *plVar7;
  ulong uVar8;
  undefined *local_48;
  undefined8 **local_40;
  undefined **local_38;
  
  puVar1 = PTR__ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c1bce0;
  local_48 = 
  PTR__ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c1bce0;
  if (*(long *)
       PTR__ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c1bce0 !=
      -1) {
    local_38 = &local_48;
    local_40 = &local_38;
    _ZNSt6__ndk111__call_onceERVmPvPFvS2_E
              (PTR__ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c1bce0
               ,&local_40,FUN_00bb9148);
  }
  uVar3 = (ulong)*(int *)(puVar1 + 8);
  uVar8 = uVar3 - 1;
  if ((uVar8 < (ulong)(*(long *)(param_2 + 0x18) - *(long *)(param_2 + 0x10) >> 3)) &&
     (lVar5 = *(long *)(*(long *)(param_2 + 0x10) + uVar8 * 8), lVar5 != 0)) {
    FUN_00bd6e60(1,lVar5 + 8);
    plVar6 = (long *)(param_1 + 0x10);
    lVar2 = *plVar6;
    uVar4 = *(long *)(param_1 + 0x18) - lVar2 >> 3;
    if (uVar4 <= uVar8) {
      if (uVar3 < uVar4 || uVar3 - uVar4 == 0) {
        if (uVar3 < uVar4) {
          *(ulong *)(param_1 + 0x18) = lVar2 + uVar3 * 8;
        }
      }
      else {
        FUN_00bb8bd4(plVar6,uVar3 - uVar4);
        lVar2 = *plVar6;
      }
    }
    plVar7 = *(long **)(lVar2 + uVar8 * 8);
    if ((plVar7 != (long *)0x0) && (lVar2 = FUN_00bd6e90(0xffffffffffffffff,plVar7 + 1), lVar2 == 0)
       ) {
      (**(code **)(*plVar7 + 0x10))(plVar7);
    }
    *(long *)(*plVar6 + uVar8 * 8) = lVar5;
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_00b890e8();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ba6dbc"></a> `00ba6dbc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00ba6dc0"></a> `00ba6dc0` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00ba6dc4"></a> `00ba6dc4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba6dc8"></a> `00ba6dc8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba6dcc"></a> `00ba6dcc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ba6dd0"></a> `00ba6dd0` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ba6dd4"></a> `00ba6dd4` | `b4 03 00 b0` | adrp x20,0xc1b000 | `FALL_THROUGH`
<a id="insn-00ba6dd8"></a> `00ba6dd8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00ba6ddc"></a> `00ba6ddc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ba6de0"></a> `00ba6de0` | `94 72 46 f9` | ldr x20,[x20, #0xce0] | `FALL_THROUGH`
<a id="insn-00ba6de4"></a> `00ba6de4` | `f4 07 00 f9` | str x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ba6de8"></a> `00ba6de8` | `88 fe df c8` | ldar x8,[x20] | `FALL_THROUGH`
<a id="insn-00ba6dec"></a> `00ba6dec` | `1f 05 00 b1` | cmn x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ba6df0"></a> `00ba6df0` | `60 01 00 54` | b.eq 0x00ba6e1c | `CONDITIONAL_JUMP`
<a id="insn-00ba6df4"></a> `00ba6df4` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00ba6df8"></a> `00ba6df8` | `a9 23 00 d1` | sub x9,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00ba6dfc"></a> `00ba6dfc` | `a0 03 00 b0` | adrp x0,0xc1b000 | `FALL_THROUGH`
<a id="insn-00ba6e00"></a> `00ba6e00` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ba6e04"></a> `00ba6e04` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00ba6e08"></a> `00ba6e08` | `02 1a 09 10` | adr x2,0xbb9148 | `FALL_THROUGH`
<a id="insn-00ba6e0c"></a> `00ba6e0c` | `e9 0b 00 f9` | str x9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba6e10"></a> `00ba6e10` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ba6e14"></a> `00ba6e14` | `00 70 46 f9` | ldr x0,[x0, #0xce0] | `FALL_THROUGH`
<a id="insn-00ba6e18"></a> `00ba6e18` | `32 e8 00 94` | bl 0x00be0ee0 | `UNCONDITIONAL_CALL`
<a id="insn-00ba6e1c"></a> `00ba6e1c` | `68 2a 41 a9` | ldp x8,x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00ba6e20"></a> `00ba6e20` | `89 0a 80 b9` | ldrsw x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00ba6e24"></a> `00ba6e24` | `36 05 00 d1` | sub x22,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00ba6e28"></a> `00ba6e28` | `49 01 08 cb` | sub x9,x10,x8 | `FALL_THROUGH`
<a id="insn-00ba6e2c"></a> `00ba6e2c` | `df 0e 89 eb` | cmp x22,x9, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00ba6e30"></a> `00ba6e30` | `02 05 00 54` | b.cs 0x00ba6ed0 | `CONDITIONAL_JUMP`
<a id="insn-00ba6e34"></a> `00ba6e34` | `13 79 76 f8` | ldr x19,[x8, x22, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00ba6e38"></a> `00ba6e38` | `d3 04 00 b4` | cbz x19,0x00ba6ed0 | `CONDITIONAL_JUMP`
<a id="insn-00ba6e3c"></a> `00ba6e3c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00ba6e40"></a> `00ba6e40` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00ba6e44"></a> `00ba6e44` | `07 c0 00 94` | bl 0x00bd6e60 | `UNCONDITIONAL_CALL`
<a id="insn-00ba6e48"></a> `00ba6e48` | `f4 03 15 aa` | mov x20,x21 | `FALL_THROUGH`
<a id="insn-00ba6e4c"></a> `00ba6e4c` | `88 26 c1 a9` | ldp x8,x9,[x20, #0x10]! | `FALL_THROUGH`
<a id="insn-00ba6e50"></a> `00ba6e50` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-00ba6e54"></a> `00ba6e54` | `2a fd 43 93` | asr x10,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00ba6e58"></a> `00ba6e58` | `5f 01 16 eb` | cmp x10,x22 | `FALL_THROUGH`
<a id="insn-00ba6e5c"></a> `00ba6e5c` | `68 01 00 54` | b.hi 0x00ba6e88 | `CONDITIONAL_JUMP`
<a id="insn-00ba6e60"></a> `00ba6e60` | `c9 06 00 91` | add x9,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00ba6e64"></a> `00ba6e64` | `21 01 0a eb` | subs x1,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba6e68"></a> `00ba6e68` | `a9 00 00 54` | b.ls 0x00ba6e7c | `CONDITIONAL_JUMP`
<a id="insn-00ba6e6c"></a> `00ba6e6c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ba6e70"></a> `00ba6e70` | `59 47 00 94` | bl 0x00bb8bd4 | `UNCONDITIONAL_CALL`
<a id="insn-00ba6e74"></a> `00ba6e74` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00ba6e78"></a> `00ba6e78` | `04 00 00 14` | b 0x00ba6e88 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba6e7c"></a> `00ba6e7c` | `62 00 00 54` | b.cs 0x00ba6e88 | `CONDITIONAL_JUMP`
<a id="insn-00ba6e80"></a> `00ba6e80` | `09 0d 09 8b` | add x9,x8,x9, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00ba6e84"></a> `00ba6e84` | `a9 0e 00 f9` | str x9,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00ba6e88"></a> `00ba6e88` | `15 79 76 f8` | ldr x21,[x8, x22, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00ba6e8c"></a> `00ba6e8c` | `35 01 00 b4` | cbz x21,0x00ba6eb0 | `CONDITIONAL_JUMP`
<a id="insn-00ba6e90"></a> `00ba6e90` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00ba6e94"></a> `00ba6e94` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ba6e98"></a> `00ba6e98` | `fe bf 00 94` | bl 0x00bd6e90 | `UNCONDITIONAL_CALL`
<a id="insn-00ba6e9c"></a> `00ba6e9c` | `a0 00 00 b5` | cbnz x0,0x00ba6eb0 | `CONDITIONAL_JUMP`
<a id="insn-00ba6ea0"></a> `00ba6ea0` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00ba6ea4"></a> `00ba6ea4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ba6ea8"></a> `00ba6ea8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ba6eac"></a> `00ba6eac` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ba6eb0"></a> `00ba6eb0` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00ba6eb4"></a> `00ba6eb4` | `13 79 36 f8` | str x19,[x8, x22, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00ba6eb8"></a> `00ba6eb8` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ba6ebc"></a> `00ba6ebc` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba6ec0"></a> `00ba6ec0` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba6ec4"></a> `00ba6ec4` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00ba6ec8"></a> `00ba6ec8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00ba6ecc"></a> `00ba6ecc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ba6ed0"></a> `00ba6ed0` | `86 88 ff 97` | bl 0x00b890e8 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ba6dbc`](#insn-00ba6dbc) 範囲 `[['00ba6dbc', '00ba6df3']]`
  - `CONDITIONAL_JUMP` [`00ba6df0`](#insn-00ba6df0) → [`00ba6e1c`](#insn-00ba6e1c)
  - `FALL_THROUGH` [`00ba6df0`](#insn-00ba6df0) → [`00ba6df4`](#insn-00ba6df4)
- ブロック [`00ba6df4`](#insn-00ba6df4) 範囲 `[['00ba6df4', '00ba6e1b']]`
  - `FALL_THROUGH` [`00ba6e18`](#insn-00ba6e18) → [`00ba6e1c`](#insn-00ba6e1c)
- ブロック [`00ba6e1c`](#insn-00ba6e1c) 範囲 `[['00ba6e1c', '00ba6e33']]`
  - `CONDITIONAL_JUMP` [`00ba6e30`](#insn-00ba6e30) → [`00ba6ed0`](#insn-00ba6ed0)
  - `FALL_THROUGH` [`00ba6e30`](#insn-00ba6e30) → [`00ba6e34`](#insn-00ba6e34)
- ブロック [`00ba6e34`](#insn-00ba6e34) 範囲 `[['00ba6e34', '00ba6e3b']]`
  - `CONDITIONAL_JUMP` [`00ba6e38`](#insn-00ba6e38) → [`00ba6ed0`](#insn-00ba6ed0)
  - `FALL_THROUGH` [`00ba6e38`](#insn-00ba6e38) → [`00ba6e3c`](#insn-00ba6e3c)
- ブロック [`00ba6e3c`](#insn-00ba6e3c) 範囲 `[['00ba6e3c', '00ba6e5f']]`
  - `CONDITIONAL_JUMP` [`00ba6e5c`](#insn-00ba6e5c) → [`00ba6e88`](#insn-00ba6e88)
  - `FALL_THROUGH` [`00ba6e5c`](#insn-00ba6e5c) → [`00ba6e60`](#insn-00ba6e60)
- ブロック [`00ba6e60`](#insn-00ba6e60) 範囲 `[['00ba6e60', '00ba6e6b']]`
  - `CONDITIONAL_JUMP` [`00ba6e68`](#insn-00ba6e68) → [`00ba6e7c`](#insn-00ba6e7c)
  - `FALL_THROUGH` [`00ba6e68`](#insn-00ba6e68) → [`00ba6e6c`](#insn-00ba6e6c)
- ブロック [`00ba6e6c`](#insn-00ba6e6c) 範囲 `[['00ba6e6c', '00ba6e7b']]`
  - `UNCONDITIONAL_JUMP` [`00ba6e78`](#insn-00ba6e78) → [`00ba6e88`](#insn-00ba6e88)
- ブロック [`00ba6e7c`](#insn-00ba6e7c) 範囲 `[['00ba6e7c', '00ba6e7f']]`
  - `CONDITIONAL_JUMP` [`00ba6e7c`](#insn-00ba6e7c) → [`00ba6e88`](#insn-00ba6e88)
  - `FALL_THROUGH` [`00ba6e7c`](#insn-00ba6e7c) → [`00ba6e80`](#insn-00ba6e80)
- ブロック [`00ba6e80`](#insn-00ba6e80) 範囲 `[['00ba6e80', '00ba6e87']]`
  - `FALL_THROUGH` [`00ba6e84`](#insn-00ba6e84) → [`00ba6e88`](#insn-00ba6e88)
- ブロック [`00ba6e88`](#insn-00ba6e88) 範囲 `[['00ba6e88', '00ba6e8f']]`
  - `CONDITIONAL_JUMP` [`00ba6e8c`](#insn-00ba6e8c) → [`00ba6eb0`](#insn-00ba6eb0)
  - `FALL_THROUGH` [`00ba6e8c`](#insn-00ba6e8c) → [`00ba6e90`](#insn-00ba6e90)
- ブロック [`00ba6e90`](#insn-00ba6e90) 範囲 `[['00ba6e90', '00ba6e9f']]`
  - `CONDITIONAL_JUMP` [`00ba6e9c`](#insn-00ba6e9c) → [`00ba6eb0`](#insn-00ba6eb0)
  - `FALL_THROUGH` [`00ba6e9c`](#insn-00ba6e9c) → [`00ba6ea0`](#insn-00ba6ea0)
- ブロック [`00ba6ea0`](#insn-00ba6ea0) 範囲 `[['00ba6ea0', '00ba6eaf']]`
  - `FALL_THROUGH` [`00ba6eac`](#insn-00ba6eac) → [`00ba6eb0`](#insn-00ba6eb0)
- ブロック [`00ba6eb0`](#insn-00ba6eb0) 範囲 `[['00ba6eb0', '00ba6ecf']]`
- ブロック [`00ba6ed0`](#insn-00ba6ed0) 範囲 `[['00ba6ed0', '00ba6ed3']]`

## 命令位置別の参照

- [`00ba6dc4`](#insn-00ba6dc4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6dc8`](#insn-00ba6dc8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6dcc`](#insn-00ba6dcc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6de0`](#insn-00ba6de0) → `00c1bce0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ba6de4`](#insn-00ba6de4) → `010a2870`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00ba6de4`](#insn-00ba6de4) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6de8`](#insn-00ba6de8) → `010a2870`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00ba6df0`](#insn-00ba6df0) → [`00ba6e1c`](#insn-00ba6e1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6e00`](#insn-00ba6e00) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6e08`](#insn-00ba6e08) → [`00bb9148`](../00bb9/00bb9148.md) · `PARAM` · `ANALYSIS` · 関数 `00bb9148` · 推定シンボル `None` · 推定型 `None`
- [`00ba6e0c`](#insn-00ba6e0c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6e14`](#insn-00ba6e14) → `00c1bce0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ba6e14`](#insn-00ba6e14) → `010a2870`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00ba6e18`](#insn-00ba6e18) → [`00be0ee0`](../00be0/00be0ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0ee0` · 推定シンボル `None` · 推定型 `None`
- [`00ba6e20`](#insn-00ba6e20) → `010a2878`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00ba6e30`](#insn-00ba6e30) → [`00ba6ed0`](#insn-00ba6ed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6e38`](#insn-00ba6e38) → [`00ba6ed0`](#insn-00ba6ed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6e44`](#insn-00ba6e44) → [`00bd6e60`](../00bd6/00bd6e60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e60` · 推定シンボル `None` · 推定型 `None`
- [`00ba6e5c`](#insn-00ba6e5c) → [`00ba6e88`](#insn-00ba6e88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6e68`](#insn-00ba6e68) → [`00ba6e7c`](#insn-00ba6e7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6e70`](#insn-00ba6e70) → [`00bb8bd4`](../00bb8/00bb8bd4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bb8bd4` · 推定シンボル `None` · 推定型 `None`
- [`00ba6e78`](#insn-00ba6e78) → [`00ba6e88`](#insn-00ba6e88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6e7c`](#insn-00ba6e7c) → [`00ba6e88`](#insn-00ba6e88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6e8c`](#insn-00ba6e8c) → [`00ba6eb0`](#insn-00ba6eb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6e98`](#insn-00ba6e98) → [`00bd6e90`](../00bd6/00bd6e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e90` · 推定シンボル `None` · 推定型 `None`
- [`00ba6e9c`](#insn-00ba6e9c) → [`00ba6eb0`](#insn-00ba6eb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6eb8`](#insn-00ba6eb8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6ebc`](#insn-00ba6ebc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6ec0`](#insn-00ba6ec0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6ed0`](#insn-00ba6ed0) → [`00b890e8`](../00b89/00b890e8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b890e8` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ba6dc4`](#insn-00ba6dc4)

~~~json
{
  "source": "00ba6dc4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6dc8`](#insn-00ba6dc8)

~~~json
{
  "source": "00ba6dc8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6dcc`](#insn-00ba6dcc)

~~~json
{
  "source": "00ba6dcc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6de0`](#insn-00ba6de0)

~~~json
{
  "source": "00ba6de0",
  "target": "00c1bce0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bce0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ba6de4`](#insn-00ba6de4)

~~~json
{
  "source": "00ba6de4",
  "target": "010a2870",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2870",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ba6de4`](#insn-00ba6de4)

~~~json
{
  "source": "00ba6de4",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6de8`](#insn-00ba6de8)

~~~json
{
  "source": "00ba6de8",
  "target": "010a2870",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2870",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ba6df0`](#insn-00ba6df0)

~~~json
{
  "source": "00ba6df0",
  "target": "00ba6e1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6e00`](#insn-00ba6e00)

~~~json
{
  "source": "00ba6e00",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6e08`](#insn-00ba6e08)

~~~json
{
  "source": "00ba6e08",
  "target": "00bb9148",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba6e0c`](#insn-00ba6e0c)

~~~json
{
  "source": "00ba6e0c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6e14`](#insn-00ba6e14)

~~~json
{
  "source": "00ba6e14",
  "target": "00c1bce0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bce0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ba6e14`](#insn-00ba6e14)

~~~json
{
  "source": "00ba6e14",
  "target": "010a2870",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2870",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ba6e18`](#insn-00ba6e18)

~~~json
{
  "source": "00ba6e18",
  "target": "00be0ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba6e20`](#insn-00ba6e20)

~~~json
{
  "source": "00ba6e20",
  "target": "010a2878",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2878",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ba6e30`](#insn-00ba6e30)

~~~json
{
  "source": "00ba6e30",
  "target": "00ba6ed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6e38`](#insn-00ba6e38)

~~~json
{
  "source": "00ba6e38",
  "target": "00ba6ed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6e44`](#insn-00ba6e44)

~~~json
{
  "source": "00ba6e44",
  "target": "00bd6e60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba6e5c`](#insn-00ba6e5c)

~~~json
{
  "source": "00ba6e5c",
  "target": "00ba6e88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6e68`](#insn-00ba6e68)

~~~json
{
  "source": "00ba6e68",
  "target": "00ba6e7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6e70`](#insn-00ba6e70)

~~~json
{
  "source": "00ba6e70",
  "target": "00bb8bd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba6e78`](#insn-00ba6e78)

~~~json
{
  "source": "00ba6e78",
  "target": "00ba6e88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6e7c`](#insn-00ba6e7c)

~~~json
{
  "source": "00ba6e7c",
  "target": "00ba6e88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6e8c`](#insn-00ba6e8c)

~~~json
{
  "source": "00ba6e8c",
  "target": "00ba6eb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6e98`](#insn-00ba6e98)

~~~json
{
  "source": "00ba6e98",
  "target": "00bd6e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba6e9c`](#insn-00ba6e9c)

~~~json
{
  "source": "00ba6e9c",
  "target": "00ba6eb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6eb8`](#insn-00ba6eb8)

~~~json
{
  "source": "00ba6eb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6ebc`](#insn-00ba6ebc)

~~~json
{
  "source": "00ba6ebc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6ec0`](#insn-00ba6ec0)

~~~json
{
  "source": "00ba6ec0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6ed0`](#insn-00ba6ed0)

~~~json
{
  "source": "00ba6ed0",
  "target": "00b890e8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
