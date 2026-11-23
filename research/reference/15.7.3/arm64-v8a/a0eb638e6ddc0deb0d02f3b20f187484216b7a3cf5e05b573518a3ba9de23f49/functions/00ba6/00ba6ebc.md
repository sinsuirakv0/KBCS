# 00ba6ebc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00ba6df4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba6/00ba6df4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0077.md#compare-dd62dbbe3461d92717fad220505d3437)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00ba6f00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba6/00ba6f00.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0077.md#compare-de827de6f02fe2baa698cd1a106db548)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ba6ebc",
  "name": "FUN_00ba6ebc",
  "size": 280,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "69005f2a43cf3f0ea3d6ca721634c0ceeecf8df1df7fb8ba59072312458f44aa",
  "source_text_sha256": "69005f2a43cf3f0ea3d6ca721634c0ceeecf8df1df7fb8ba59072312458f44aa",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ba6ebc",
        "00ba6fd3"
      ]
    ],
    "bytes_sha256": "23b10b48f15eafada279fe997dcafed572720ea7843b53d5f65a659266aab73f",
    "instruction_count": 70,
    "instruction_bytes": 280,
    "body_bytes": 280,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00ba50c4](../00ba5/00ba50c4.md)

## 呼び出し先

- [00b890a4](../00b89/00b890a4.md)
- [00bb8b90](../00bb8/00bb8b90.md)
- [00bd6e20](../00bd6/00bd6e20.md)
- [00bd6e50](../00bd6/00bd6e50.md)
- [00be0e90](../00be0/00be0e90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1823 bytes

~~~c

void FUN_00ba6ebc(long param_1,long param_2)

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
  
  puVar1 = PTR__ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE_00c1bcc8;
  local_48 = 
  PTR__ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE_00c1bcc8;
  if (*(long *)
       PTR__ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE_00c1bcc8 !=
      -1) {
    local_38 = &local_48;
    local_40 = &local_38;
    _ZNSt6__ndk111__call_onceERVmPvPFvS2_E
              (PTR__ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE_00c1bcc8
               ,&local_40,FUN_00bb9104);
  }
  uVar3 = (ulong)*(int *)(puVar1 + 8);
  uVar8 = uVar3 - 1;
  if ((uVar8 < (ulong)(*(long *)(param_2 + 0x18) - *(long *)(param_2 + 0x10) >> 3)) &&
     (lVar5 = *(long *)(*(long *)(param_2 + 0x10) + uVar8 * 8), lVar5 != 0)) {
    FUN_00bd6e20(1,lVar5 + 8);
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
        FUN_00bb8b90(plVar6,uVar3 - uVar4);
        lVar2 = *plVar6;
      }
    }
    plVar7 = *(long **)(lVar2 + uVar8 * 8);
    if ((plVar7 != (long *)0x0) && (lVar2 = FUN_00bd6e50(0xffffffffffffffff,plVar7 + 1), lVar2 == 0)
       ) {
      (**(code **)(*plVar7 + 0x10))(plVar7);
    }
    *(long *)(*plVar6 + uVar8 * 8) = lVar5;
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_00b890a4();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ba6ebc"></a> `00ba6ebc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00ba6ec0"></a> `00ba6ec0` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00ba6ec4"></a> `00ba6ec4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba6ec8"></a> `00ba6ec8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba6ecc"></a> `00ba6ecc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ba6ed0"></a> `00ba6ed0` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ba6ed4"></a> `00ba6ed4` | `b4 03 00 b0` | adrp x20,0xc1b000 | `FALL_THROUGH`
<a id="insn-00ba6ed8"></a> `00ba6ed8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00ba6edc"></a> `00ba6edc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ba6ee0"></a> `00ba6ee0` | `94 66 46 f9` | ldr x20,[x20, #0xcc8] | `FALL_THROUGH`
<a id="insn-00ba6ee4"></a> `00ba6ee4` | `f4 07 00 f9` | str x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ba6ee8"></a> `00ba6ee8` | `88 fe df c8` | ldar x8,[x20] | `FALL_THROUGH`
<a id="insn-00ba6eec"></a> `00ba6eec` | `1f 05 00 b1` | cmn x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ba6ef0"></a> `00ba6ef0` | `60 01 00 54` | b.eq 0x00ba6f1c | `CONDITIONAL_JUMP`
<a id="insn-00ba6ef4"></a> `00ba6ef4` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00ba6ef8"></a> `00ba6ef8` | `a9 23 00 d1` | sub x9,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00ba6efc"></a> `00ba6efc` | `a0 03 00 b0` | adrp x0,0xc1b000 | `FALL_THROUGH`
<a id="insn-00ba6f00"></a> `00ba6f00` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ba6f04"></a> `00ba6f04` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00ba6f08"></a> `00ba6f08` | `e2 0f 09 10` | adr x2,0xbb9104 | `FALL_THROUGH`
<a id="insn-00ba6f0c"></a> `00ba6f0c` | `e9 0b 00 f9` | str x9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba6f10"></a> `00ba6f10` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ba6f14"></a> `00ba6f14` | `00 64 46 f9` | ldr x0,[x0, #0xcc8] | `FALL_THROUGH`
<a id="insn-00ba6f18"></a> `00ba6f18` | `de e7 00 94` | bl 0x00be0e90 | `UNCONDITIONAL_CALL`
<a id="insn-00ba6f1c"></a> `00ba6f1c` | `68 2a 41 a9` | ldp x8,x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00ba6f20"></a> `00ba6f20` | `89 0a 80 b9` | ldrsw x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00ba6f24"></a> `00ba6f24` | `36 05 00 d1` | sub x22,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00ba6f28"></a> `00ba6f28` | `49 01 08 cb` | sub x9,x10,x8 | `FALL_THROUGH`
<a id="insn-00ba6f2c"></a> `00ba6f2c` | `df 0e 89 eb` | cmp x22,x9, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00ba6f30"></a> `00ba6f30` | `02 05 00 54` | b.cs 0x00ba6fd0 | `CONDITIONAL_JUMP`
<a id="insn-00ba6f34"></a> `00ba6f34` | `13 79 76 f8` | ldr x19,[x8, x22, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00ba6f38"></a> `00ba6f38` | `d3 04 00 b4` | cbz x19,0x00ba6fd0 | `CONDITIONAL_JUMP`
<a id="insn-00ba6f3c"></a> `00ba6f3c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00ba6f40"></a> `00ba6f40` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00ba6f44"></a> `00ba6f44` | `b7 bf 00 94` | bl 0x00bd6e20 | `UNCONDITIONAL_CALL`
<a id="insn-00ba6f48"></a> `00ba6f48` | `f4 03 15 aa` | mov x20,x21 | `FALL_THROUGH`
<a id="insn-00ba6f4c"></a> `00ba6f4c` | `88 26 c1 a9` | ldp x8,x9,[x20, #0x10]! | `FALL_THROUGH`
<a id="insn-00ba6f50"></a> `00ba6f50` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-00ba6f54"></a> `00ba6f54` | `2a fd 43 93` | asr x10,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00ba6f58"></a> `00ba6f58` | `5f 01 16 eb` | cmp x10,x22 | `FALL_THROUGH`
<a id="insn-00ba6f5c"></a> `00ba6f5c` | `68 01 00 54` | b.hi 0x00ba6f88 | `CONDITIONAL_JUMP`
<a id="insn-00ba6f60"></a> `00ba6f60` | `c9 06 00 91` | add x9,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00ba6f64"></a> `00ba6f64` | `21 01 0a eb` | subs x1,x9,x10 | `FALL_THROUGH`
<a id="insn-00ba6f68"></a> `00ba6f68` | `a9 00 00 54` | b.ls 0x00ba6f7c | `CONDITIONAL_JUMP`
<a id="insn-00ba6f6c"></a> `00ba6f6c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ba6f70"></a> `00ba6f70` | `08 47 00 94` | bl 0x00bb8b90 | `UNCONDITIONAL_CALL`
<a id="insn-00ba6f74"></a> `00ba6f74` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00ba6f78"></a> `00ba6f78` | `04 00 00 14` | b 0x00ba6f88 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba6f7c"></a> `00ba6f7c` | `62 00 00 54` | b.cs 0x00ba6f88 | `CONDITIONAL_JUMP`
<a id="insn-00ba6f80"></a> `00ba6f80` | `09 0d 09 8b` | add x9,x8,x9, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00ba6f84"></a> `00ba6f84` | `a9 0e 00 f9` | str x9,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00ba6f88"></a> `00ba6f88` | `15 79 76 f8` | ldr x21,[x8, x22, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00ba6f8c"></a> `00ba6f8c` | `35 01 00 b4` | cbz x21,0x00ba6fb0 | `CONDITIONAL_JUMP`
<a id="insn-00ba6f90"></a> `00ba6f90` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00ba6f94"></a> `00ba6f94` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ba6f98"></a> `00ba6f98` | `ae bf 00 94` | bl 0x00bd6e50 | `UNCONDITIONAL_CALL`
<a id="insn-00ba6f9c"></a> `00ba6f9c` | `a0 00 00 b5` | cbnz x0,0x00ba6fb0 | `CONDITIONAL_JUMP`
<a id="insn-00ba6fa0"></a> `00ba6fa0` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00ba6fa4"></a> `00ba6fa4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ba6fa8"></a> `00ba6fa8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ba6fac"></a> `00ba6fac` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ba6fb0"></a> `00ba6fb0` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00ba6fb4"></a> `00ba6fb4` | `13 79 36 f8` | str x19,[x8, x22, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00ba6fb8"></a> `00ba6fb8` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ba6fbc"></a> `00ba6fbc` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba6fc0"></a> `00ba6fc0` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba6fc4"></a> `00ba6fc4` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00ba6fc8"></a> `00ba6fc8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00ba6fcc"></a> `00ba6fcc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ba6fd0"></a> `00ba6fd0` | `35 88 ff 97` | bl 0x00b890a4 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ba6ebc`](#insn-00ba6ebc) 範囲 `[['00ba6ebc', '00ba6ef3']]`
  - `CONDITIONAL_JUMP` [`00ba6ef0`](#insn-00ba6ef0) → [`00ba6f1c`](#insn-00ba6f1c)
  - `FALL_THROUGH` [`00ba6ef0`](#insn-00ba6ef0) → [`00ba6ef4`](#insn-00ba6ef4)
- ブロック [`00ba6ef4`](#insn-00ba6ef4) 範囲 `[['00ba6ef4', '00ba6f1b']]`
  - `FALL_THROUGH` [`00ba6f18`](#insn-00ba6f18) → [`00ba6f1c`](#insn-00ba6f1c)
- ブロック [`00ba6f1c`](#insn-00ba6f1c) 範囲 `[['00ba6f1c', '00ba6f33']]`
  - `CONDITIONAL_JUMP` [`00ba6f30`](#insn-00ba6f30) → [`00ba6fd0`](#insn-00ba6fd0)
  - `FALL_THROUGH` [`00ba6f30`](#insn-00ba6f30) → [`00ba6f34`](#insn-00ba6f34)
- ブロック [`00ba6f34`](#insn-00ba6f34) 範囲 `[['00ba6f34', '00ba6f3b']]`
  - `CONDITIONAL_JUMP` [`00ba6f38`](#insn-00ba6f38) → [`00ba6fd0`](#insn-00ba6fd0)
  - `FALL_THROUGH` [`00ba6f38`](#insn-00ba6f38) → [`00ba6f3c`](#insn-00ba6f3c)
- ブロック [`00ba6f3c`](#insn-00ba6f3c) 範囲 `[['00ba6f3c', '00ba6f5f']]`
  - `CONDITIONAL_JUMP` [`00ba6f5c`](#insn-00ba6f5c) → [`00ba6f88`](#insn-00ba6f88)
  - `FALL_THROUGH` [`00ba6f5c`](#insn-00ba6f5c) → [`00ba6f60`](#insn-00ba6f60)
- ブロック [`00ba6f60`](#insn-00ba6f60) 範囲 `[['00ba6f60', '00ba6f6b']]`
  - `CONDITIONAL_JUMP` [`00ba6f68`](#insn-00ba6f68) → [`00ba6f7c`](#insn-00ba6f7c)
  - `FALL_THROUGH` [`00ba6f68`](#insn-00ba6f68) → [`00ba6f6c`](#insn-00ba6f6c)
- ブロック [`00ba6f6c`](#insn-00ba6f6c) 範囲 `[['00ba6f6c', '00ba6f7b']]`
  - `UNCONDITIONAL_JUMP` [`00ba6f78`](#insn-00ba6f78) → [`00ba6f88`](#insn-00ba6f88)
- ブロック [`00ba6f7c`](#insn-00ba6f7c) 範囲 `[['00ba6f7c', '00ba6f7f']]`
  - `CONDITIONAL_JUMP` [`00ba6f7c`](#insn-00ba6f7c) → [`00ba6f88`](#insn-00ba6f88)
  - `FALL_THROUGH` [`00ba6f7c`](#insn-00ba6f7c) → [`00ba6f80`](#insn-00ba6f80)
- ブロック [`00ba6f80`](#insn-00ba6f80) 範囲 `[['00ba6f80', '00ba6f87']]`
  - `FALL_THROUGH` [`00ba6f84`](#insn-00ba6f84) → [`00ba6f88`](#insn-00ba6f88)
- ブロック [`00ba6f88`](#insn-00ba6f88) 範囲 `[['00ba6f88', '00ba6f8f']]`
  - `CONDITIONAL_JUMP` [`00ba6f8c`](#insn-00ba6f8c) → [`00ba6fb0`](#insn-00ba6fb0)
  - `FALL_THROUGH` [`00ba6f8c`](#insn-00ba6f8c) → [`00ba6f90`](#insn-00ba6f90)
- ブロック [`00ba6f90`](#insn-00ba6f90) 範囲 `[['00ba6f90', '00ba6f9f']]`
  - `CONDITIONAL_JUMP` [`00ba6f9c`](#insn-00ba6f9c) → [`00ba6fb0`](#insn-00ba6fb0)
  - `FALL_THROUGH` [`00ba6f9c`](#insn-00ba6f9c) → [`00ba6fa0`](#insn-00ba6fa0)
- ブロック [`00ba6fa0`](#insn-00ba6fa0) 範囲 `[['00ba6fa0', '00ba6faf']]`
  - `FALL_THROUGH` [`00ba6fac`](#insn-00ba6fac) → [`00ba6fb0`](#insn-00ba6fb0)
- ブロック [`00ba6fb0`](#insn-00ba6fb0) 範囲 `[['00ba6fb0', '00ba6fcf']]`
- ブロック [`00ba6fd0`](#insn-00ba6fd0) 範囲 `[['00ba6fd0', '00ba6fd3']]`

## 命令位置別の参照

- [`00ba6ec4`](#insn-00ba6ec4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6ec8`](#insn-00ba6ec8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6ecc`](#insn-00ba6ecc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6ee0`](#insn-00ba6ee0) → `00c1bcc8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ba6ee4`](#insn-00ba6ee4) → `010a2840`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE` · 推定型 `undefined8`
- [`00ba6ee4`](#insn-00ba6ee4) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6ee8`](#insn-00ba6ee8) → `010a2840`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE` · 推定型 `undefined8`
- [`00ba6ef0`](#insn-00ba6ef0) → [`00ba6f1c`](#insn-00ba6f1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6f00`](#insn-00ba6f00) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6f08`](#insn-00ba6f08) → [`00bb9104`](../00bb9/00bb9104.md) · `PARAM` · `ANALYSIS` · 関数 `00bb9104` · 推定シンボル `None` · 推定型 `None`
- [`00ba6f0c`](#insn-00ba6f0c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6f14`](#insn-00ba6f14) → `00c1bcc8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ba6f14`](#insn-00ba6f14) → `010a2840`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE` · 推定型 `undefined8`
- [`00ba6f18`](#insn-00ba6f18) → [`00be0e90`](../00be0/00be0e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0e90` · 推定シンボル `None` · 推定型 `None`
- [`00ba6f20`](#insn-00ba6f20) → `010a2848`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00ba6f30`](#insn-00ba6f30) → [`00ba6fd0`](#insn-00ba6fd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6f38`](#insn-00ba6f38) → [`00ba6fd0`](#insn-00ba6fd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6f44`](#insn-00ba6f44) → [`00bd6e20`](../00bd6/00bd6e20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e20` · 推定シンボル `None` · 推定型 `None`
- [`00ba6f5c`](#insn-00ba6f5c) → [`00ba6f88`](#insn-00ba6f88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6f68`](#insn-00ba6f68) → [`00ba6f7c`](#insn-00ba6f7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6f70`](#insn-00ba6f70) → [`00bb8b90`](../00bb8/00bb8b90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bb8b90` · 推定シンボル `None` · 推定型 `None`
- [`00ba6f78`](#insn-00ba6f78) → [`00ba6f88`](#insn-00ba6f88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6f7c`](#insn-00ba6f7c) → [`00ba6f88`](#insn-00ba6f88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6f8c`](#insn-00ba6f8c) → [`00ba6fb0`](#insn-00ba6fb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6f98`](#insn-00ba6f98) → [`00bd6e50`](../00bd6/00bd6e50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e50` · 推定シンボル `None` · 推定型 `None`
- [`00ba6f9c`](#insn-00ba6f9c) → [`00ba6fb0`](#insn-00ba6fb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6fb8`](#insn-00ba6fb8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6fbc`](#insn-00ba6fbc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6fc0`](#insn-00ba6fc0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba6fd0`](#insn-00ba6fd0) → [`00b890a4`](../00b89/00b890a4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b890a4` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ba6ec4`](#insn-00ba6ec4)

~~~json
{
  "source": "00ba6ec4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6ec8`](#insn-00ba6ec8)

~~~json
{
  "source": "00ba6ec8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6ecc`](#insn-00ba6ecc)

~~~json
{
  "source": "00ba6ecc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6ee0`](#insn-00ba6ee0)

~~~json
{
  "source": "00ba6ee0",
  "target": "00c1bcc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bcc8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ba6ee4`](#insn-00ba6ee4)

~~~json
{
  "source": "00ba6ee4",
  "target": "010a2840",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2840",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ba6ee4`](#insn-00ba6ee4)

~~~json
{
  "source": "00ba6ee4",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6ee8`](#insn-00ba6ee8)

~~~json
{
  "source": "00ba6ee8",
  "target": "010a2840",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2840",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ba6ef0`](#insn-00ba6ef0)

~~~json
{
  "source": "00ba6ef0",
  "target": "00ba6f1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6f00`](#insn-00ba6f00)

~~~json
{
  "source": "00ba6f00",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6f08`](#insn-00ba6f08)

~~~json
{
  "source": "00ba6f08",
  "target": "00bb9104",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba6f0c`](#insn-00ba6f0c)

~~~json
{
  "source": "00ba6f0c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6f14`](#insn-00ba6f14)

~~~json
{
  "source": "00ba6f14",
  "target": "00c1bcc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bcc8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ba6f14`](#insn-00ba6f14)

~~~json
{
  "source": "00ba6f14",
  "target": "010a2840",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2840",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ba6f18`](#insn-00ba6f18)

~~~json
{
  "source": "00ba6f18",
  "target": "00be0e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba6f20`](#insn-00ba6f20)

~~~json
{
  "source": "00ba6f20",
  "target": "010a2848",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a2848",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ba6f30`](#insn-00ba6f30)

~~~json
{
  "source": "00ba6f30",
  "target": "00ba6fd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6f38`](#insn-00ba6f38)

~~~json
{
  "source": "00ba6f38",
  "target": "00ba6fd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6f44`](#insn-00ba6f44)

~~~json
{
  "source": "00ba6f44",
  "target": "00bd6e20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba6f5c`](#insn-00ba6f5c)

~~~json
{
  "source": "00ba6f5c",
  "target": "00ba6f88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6f68`](#insn-00ba6f68)

~~~json
{
  "source": "00ba6f68",
  "target": "00ba6f7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6f70`](#insn-00ba6f70)

~~~json
{
  "source": "00ba6f70",
  "target": "00bb8b90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba6f78`](#insn-00ba6f78)

~~~json
{
  "source": "00ba6f78",
  "target": "00ba6f88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6f7c`](#insn-00ba6f7c)

~~~json
{
  "source": "00ba6f7c",
  "target": "00ba6f88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6f8c`](#insn-00ba6f8c)

~~~json
{
  "source": "00ba6f8c",
  "target": "00ba6fb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6f98`](#insn-00ba6f98)

~~~json
{
  "source": "00ba6f98",
  "target": "00bd6e50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba6f9c`](#insn-00ba6f9c)

~~~json
{
  "source": "00ba6f9c",
  "target": "00ba6fb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6fb8`](#insn-00ba6fb8)

~~~json
{
  "source": "00ba6fb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6fbc`](#insn-00ba6fbc)

~~~json
{
  "source": "00ba6fbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6fc0`](#insn-00ba6fc0)

~~~json
{
  "source": "00ba6fc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba6fd0`](#insn-00ba6fd0)

~~~json
{
  "source": "00ba6fd0",
  "target": "00b890a4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
