# 00ac2ddc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a64e24`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64e24.md) · 移動量 `+0x5dfb8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0052.md#compare-ed7e5e8221d67c2463971176f39e4093)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00ac2fd8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac2/00ac2fd8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0064.md#compare-f6c5ed306354e297eb55c75aa4af2e07)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ac2ddc",
  "name": "FUN_00ac2ddc",
  "size": 376,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ecc5b57878b541972287c66d541f168f265a326858b894ee75fdf8a30c235723",
  "source_text_sha256": "ecc5b57878b541972287c66d541f168f265a326858b894ee75fdf8a30c235723",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ac2ddc",
        "00ac2f53"
      ]
    ],
    "bytes_sha256": "194e3ff20d4027cb750f91b480977bed91eca1f2eadfc472511f9fce1b0d9bee",
    "instruction_count": 94,
    "instruction_bytes": 376,
    "body_bytes": 376,
    "indirect": 6,
    "unresolved": 6
  }
}
~~~

## 呼び出し元

- [00ac2f54](../00ac2/00ac2f54.md)

## 呼び出し先

- [006822e4](../00682/006822e4.md)
- [0078dc6c](../0078d/0078dc6c.md)
- [00c538e0](../00c53/00c538e0.md)
- [00c57a80](../00c57/00c57a80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1903 bytes

~~~c

void FUN_00ac2ddc(undefined8 *param_1)

{
  long lVar1;
  long *plVar2;
  
  plVar2 = (long *)param_1[0x8d];
  *param_1 = &PTR_FUN_00c8d020;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
                    /* try { // try from 00ac2e24 to 00bc2e73 has its CatchHandler @ 00ac3114 */
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[0x8b];
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[0x89];
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[0x87];
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[0x85];
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  FUN_0078dc6c(param_1 + 0x7a);
  FUN_0078dc6c(param_1 + 0x70);
  FUN_0078dc6c(param_1 + 0x66);
  FUN_0078dc6c(param_1 + 0x5c);
  plVar2 = (long *)param_1[0x5b];
  *param_1 = &PTR_FUN_00c74410;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  FUN_006822e4(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ac2ddc"></a> `00ac2ddc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ac2de0"></a> `00ac2de0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ac2de4"></a> `00ac2de4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00ac2de8"></a> `00ac2de8` | `14 34 42 f9` | ldr x20,[x0, #0x468] | `FALL_THROUGH`
<a id="insn-00ac2dec"></a> `00ac2dec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ac2df0"></a> `00ac2df0` | `48 0e 00 f0` | adrp x8,0xc8d000 | `FALL_THROUGH`
<a id="insn-00ac2df4"></a> `00ac2df4` | `08 81 00 91` | add x8,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00ac2df8"></a> `00ac2df8` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00ac2dfc"></a> `00ac2dfc` | `74 01 00 b4` | cbz x20,0x00ac2e28 | `CONDITIONAL_JUMP`
<a id="insn-00ac2e00"></a> `00ac2e00` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00ac2e04"></a> `00ac2e04` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ac2e08"></a> `00ac2e08` | `b6 42 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac2e0c"></a> `00ac2e0c` | `e0 00 00 b5` | cbnz x0,0x00ac2e28 | `CONDITIONAL_JUMP`
<a id="insn-00ac2e10"></a> `00ac2e10` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00ac2e14"></a> `00ac2e14` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac2e18"></a> `00ac2e18` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ac2e1c"></a> `00ac2e1c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac2e20"></a> `00ac2e20` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac2e24"></a> `00ac2e24` | `17 53 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00ac2e28"></a> `00ac2e28` | `74 2e 42 f9` | ldr x20,[x19, #0x458] | `FALL_THROUGH`
<a id="insn-00ac2e2c"></a> `00ac2e2c` | `74 01 00 b4` | cbz x20,0x00ac2e58 | `CONDITIONAL_JUMP`
<a id="insn-00ac2e30"></a> `00ac2e30` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00ac2e34"></a> `00ac2e34` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ac2e38"></a> `00ac2e38` | `aa 42 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac2e3c"></a> `00ac2e3c` | `e0 00 00 b5` | cbnz x0,0x00ac2e58 | `CONDITIONAL_JUMP`
<a id="insn-00ac2e40"></a> `00ac2e40` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00ac2e44"></a> `00ac2e44` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac2e48"></a> `00ac2e48` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ac2e4c"></a> `00ac2e4c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac2e50"></a> `00ac2e50` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac2e54"></a> `00ac2e54` | `0b 53 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00ac2e58"></a> `00ac2e58` | `74 26 42 f9` | ldr x20,[x19, #0x448] | `FALL_THROUGH`
<a id="insn-00ac2e5c"></a> `00ac2e5c` | `74 01 00 b4` | cbz x20,0x00ac2e88 | `CONDITIONAL_JUMP`
<a id="insn-00ac2e60"></a> `00ac2e60` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00ac2e64"></a> `00ac2e64` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ac2e68"></a> `00ac2e68` | `9e 42 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac2e6c"></a> `00ac2e6c` | `e0 00 00 b5` | cbnz x0,0x00ac2e88 | `CONDITIONAL_JUMP`
<a id="insn-00ac2e70"></a> `00ac2e70` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00ac2e74"></a> `00ac2e74` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac2e78"></a> `00ac2e78` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ac2e7c"></a> `00ac2e7c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac2e80"></a> `00ac2e80` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac2e84"></a> `00ac2e84` | `ff 52 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00ac2e88"></a> `00ac2e88` | `74 1e 42 f9` | ldr x20,[x19, #0x438] | `FALL_THROUGH`
<a id="insn-00ac2e8c"></a> `00ac2e8c` | `74 01 00 b4` | cbz x20,0x00ac2eb8 | `CONDITIONAL_JUMP`
<a id="insn-00ac2e90"></a> `00ac2e90` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00ac2e94"></a> `00ac2e94` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ac2e98"></a> `00ac2e98` | `92 42 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac2e9c"></a> `00ac2e9c` | `e0 00 00 b5` | cbnz x0,0x00ac2eb8 | `CONDITIONAL_JUMP`
<a id="insn-00ac2ea0"></a> `00ac2ea0` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00ac2ea4"></a> `00ac2ea4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac2ea8"></a> `00ac2ea8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ac2eac"></a> `00ac2eac` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac2eb0"></a> `00ac2eb0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac2eb4"></a> `00ac2eb4` | `f3 52 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00ac2eb8"></a> `00ac2eb8` | `74 16 42 f9` | ldr x20,[x19, #0x428] | `FALL_THROUGH`
<a id="insn-00ac2ebc"></a> `00ac2ebc` | `74 01 00 b4` | cbz x20,0x00ac2ee8 | `CONDITIONAL_JUMP`
<a id="insn-00ac2ec0"></a> `00ac2ec0` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00ac2ec4"></a> `00ac2ec4` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ac2ec8"></a> `00ac2ec8` | `86 42 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac2ecc"></a> `00ac2ecc` | `e0 00 00 b5` | cbnz x0,0x00ac2ee8 | `CONDITIONAL_JUMP`
<a id="insn-00ac2ed0"></a> `00ac2ed0` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00ac2ed4"></a> `00ac2ed4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac2ed8"></a> `00ac2ed8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ac2edc"></a> `00ac2edc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac2ee0"></a> `00ac2ee0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac2ee4"></a> `00ac2ee4` | `e7 52 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00ac2ee8"></a> `00ac2ee8` | `60 42 0f 91` | add x0,x19,#0x3d0 | `FALL_THROUGH`
<a id="insn-00ac2eec"></a> `00ac2eec` | `60 2b f3 97` | bl 0x0078dc6c | `UNCONDITIONAL_CALL`
<a id="insn-00ac2ef0"></a> `00ac2ef0` | `60 02 0e 91` | add x0,x19,#0x380 | `FALL_THROUGH`
<a id="insn-00ac2ef4"></a> `00ac2ef4` | `5e 2b f3 97` | bl 0x0078dc6c | `UNCONDITIONAL_CALL`
<a id="insn-00ac2ef8"></a> `00ac2ef8` | `60 c2 0c 91` | add x0,x19,#0x330 | `FALL_THROUGH`
<a id="insn-00ac2efc"></a> `00ac2efc` | `5c 2b f3 97` | bl 0x0078dc6c | `UNCONDITIONAL_CALL`
<a id="insn-00ac2f00"></a> `00ac2f00` | `60 82 0b 91` | add x0,x19,#0x2e0 | `FALL_THROUGH`
<a id="insn-00ac2f04"></a> `00ac2f04` | `5a 2b f3 97` | bl 0x0078dc6c | `UNCONDITIONAL_CALL`
<a id="insn-00ac2f08"></a> `00ac2f08` | `74 6e 41 f9` | ldr x20,[x19, #0x2d8] | `FALL_THROUGH`
<a id="insn-00ac2f0c"></a> `00ac2f0c` | `88 0d 00 d0` | adrp x8,0xc74000 | `FALL_THROUGH`
<a id="insn-00ac2f10"></a> `00ac2f10` | `08 41 10 91` | add x8,x8,#0x410 | `FALL_THROUGH`
<a id="insn-00ac2f14"></a> `00ac2f14` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00ac2f18"></a> `00ac2f18` | `74 01 00 b4` | cbz x20,0x00ac2f44 | `CONDITIONAL_JUMP`
<a id="insn-00ac2f1c"></a> `00ac2f1c` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00ac2f20"></a> `00ac2f20` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ac2f24"></a> `00ac2f24` | `6f 42 06 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-00ac2f28"></a> `00ac2f28` | `e0 00 00 b5` | cbnz x0,0x00ac2f44 | `CONDITIONAL_JUMP`
<a id="insn-00ac2f2c"></a> `00ac2f2c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00ac2f30"></a> `00ac2f30` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac2f34"></a> `00ac2f34` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ac2f38"></a> `00ac2f38` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac2f3c"></a> `00ac2f3c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ac2f40"></a> `00ac2f40` | `d0 52 06 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00ac2f44"></a> `00ac2f44` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ac2f48"></a> `00ac2f48` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ac2f4c"></a> `00ac2f4c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ac2f50"></a> `00ac2f50` | `e5 fc ee 17` | b 0x006822e4 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ac2ddc`](#insn-00ac2ddc) 範囲 `[['00ac2ddc', '00ac2dff']]`
  - `CONDITIONAL_JUMP` [`00ac2dfc`](#insn-00ac2dfc) → [`00ac2e28`](#insn-00ac2e28)
  - `FALL_THROUGH` [`00ac2dfc`](#insn-00ac2dfc) → [`00ac2e00`](#insn-00ac2e00)
- ブロック [`00ac2e00`](#insn-00ac2e00) 範囲 `[['00ac2e00', '00ac2e0f']]`
  - `CONDITIONAL_JUMP` [`00ac2e0c`](#insn-00ac2e0c) → [`00ac2e28`](#insn-00ac2e28)
  - `FALL_THROUGH` [`00ac2e0c`](#insn-00ac2e0c) → [`00ac2e10`](#insn-00ac2e10)
- ブロック [`00ac2e10`](#insn-00ac2e10) 範囲 `[['00ac2e10', '00ac2e23']]`
  - `FALL_THROUGH` [`00ac2e20`](#insn-00ac2e20) → [`00ac2e24`](#insn-00ac2e24)
- ブロック [`00ac2e24`](#insn-00ac2e24) 範囲 `[['00ac2e24', '00ac2e27']]`
  - `FALL_THROUGH` [`00ac2e24`](#insn-00ac2e24) → [`00ac2e28`](#insn-00ac2e28)
- ブロック [`00ac2e28`](#insn-00ac2e28) 範囲 `[['00ac2e28', '00ac2e2f']]`
  - `CONDITIONAL_JUMP` [`00ac2e2c`](#insn-00ac2e2c) → [`00ac2e58`](#insn-00ac2e58)
  - `FALL_THROUGH` [`00ac2e2c`](#insn-00ac2e2c) → [`00ac2e30`](#insn-00ac2e30)
- ブロック [`00ac2e30`](#insn-00ac2e30) 範囲 `[['00ac2e30', '00ac2e3f']]`
  - `CONDITIONAL_JUMP` [`00ac2e3c`](#insn-00ac2e3c) → [`00ac2e58`](#insn-00ac2e58)
  - `FALL_THROUGH` [`00ac2e3c`](#insn-00ac2e3c) → [`00ac2e40`](#insn-00ac2e40)
- ブロック [`00ac2e40`](#insn-00ac2e40) 範囲 `[['00ac2e40', '00ac2e57']]`
  - `FALL_THROUGH` [`00ac2e54`](#insn-00ac2e54) → [`00ac2e58`](#insn-00ac2e58)
- ブロック [`00ac2e58`](#insn-00ac2e58) 範囲 `[['00ac2e58', '00ac2e5f']]`
  - `CONDITIONAL_JUMP` [`00ac2e5c`](#insn-00ac2e5c) → [`00ac2e88`](#insn-00ac2e88)
  - `FALL_THROUGH` [`00ac2e5c`](#insn-00ac2e5c) → [`00ac2e60`](#insn-00ac2e60)
- ブロック [`00ac2e60`](#insn-00ac2e60) 範囲 `[['00ac2e60', '00ac2e6f']]`
  - `CONDITIONAL_JUMP` [`00ac2e6c`](#insn-00ac2e6c) → [`00ac2e88`](#insn-00ac2e88)
  - `FALL_THROUGH` [`00ac2e6c`](#insn-00ac2e6c) → [`00ac2e70`](#insn-00ac2e70)
- ブロック [`00ac2e70`](#insn-00ac2e70) 範囲 `[['00ac2e70', '00ac2e87']]`
  - `FALL_THROUGH` [`00ac2e84`](#insn-00ac2e84) → [`00ac2e88`](#insn-00ac2e88)
- ブロック [`00ac2e88`](#insn-00ac2e88) 範囲 `[['00ac2e88', '00ac2e8f']]`
  - `CONDITIONAL_JUMP` [`00ac2e8c`](#insn-00ac2e8c) → [`00ac2eb8`](#insn-00ac2eb8)
  - `FALL_THROUGH` [`00ac2e8c`](#insn-00ac2e8c) → [`00ac2e90`](#insn-00ac2e90)
- ブロック [`00ac2e90`](#insn-00ac2e90) 範囲 `[['00ac2e90', '00ac2e9f']]`
  - `CONDITIONAL_JUMP` [`00ac2e9c`](#insn-00ac2e9c) → [`00ac2eb8`](#insn-00ac2eb8)
  - `FALL_THROUGH` [`00ac2e9c`](#insn-00ac2e9c) → [`00ac2ea0`](#insn-00ac2ea0)
- ブロック [`00ac2ea0`](#insn-00ac2ea0) 範囲 `[['00ac2ea0', '00ac2eb7']]`
  - `FALL_THROUGH` [`00ac2eb4`](#insn-00ac2eb4) → [`00ac2eb8`](#insn-00ac2eb8)
- ブロック [`00ac2eb8`](#insn-00ac2eb8) 範囲 `[['00ac2eb8', '00ac2ebf']]`
  - `CONDITIONAL_JUMP` [`00ac2ebc`](#insn-00ac2ebc) → [`00ac2ee8`](#insn-00ac2ee8)
  - `FALL_THROUGH` [`00ac2ebc`](#insn-00ac2ebc) → [`00ac2ec0`](#insn-00ac2ec0)
- ブロック [`00ac2ec0`](#insn-00ac2ec0) 範囲 `[['00ac2ec0', '00ac2ecf']]`
  - `CONDITIONAL_JUMP` [`00ac2ecc`](#insn-00ac2ecc) → [`00ac2ee8`](#insn-00ac2ee8)
  - `FALL_THROUGH` [`00ac2ecc`](#insn-00ac2ecc) → [`00ac2ed0`](#insn-00ac2ed0)
- ブロック [`00ac2ed0`](#insn-00ac2ed0) 範囲 `[['00ac2ed0', '00ac2ee7']]`
  - `FALL_THROUGH` [`00ac2ee4`](#insn-00ac2ee4) → [`00ac2ee8`](#insn-00ac2ee8)
- ブロック [`00ac2ee8`](#insn-00ac2ee8) 範囲 `[['00ac2ee8', '00ac2f1b']]`
  - `CONDITIONAL_JUMP` [`00ac2f18`](#insn-00ac2f18) → [`00ac2f44`](#insn-00ac2f44)
  - `FALL_THROUGH` [`00ac2f18`](#insn-00ac2f18) → [`00ac2f1c`](#insn-00ac2f1c)
- ブロック [`00ac2f1c`](#insn-00ac2f1c) 範囲 `[['00ac2f1c', '00ac2f2b']]`
  - `CONDITIONAL_JUMP` [`00ac2f28`](#insn-00ac2f28) → [`00ac2f44`](#insn-00ac2f44)
  - `FALL_THROUGH` [`00ac2f28`](#insn-00ac2f28) → [`00ac2f2c`](#insn-00ac2f2c)
- ブロック [`00ac2f2c`](#insn-00ac2f2c) 範囲 `[['00ac2f2c', '00ac2f43']]`
  - `FALL_THROUGH` [`00ac2f40`](#insn-00ac2f40) → [`00ac2f44`](#insn-00ac2f44)
- ブロック [`00ac2f44`](#insn-00ac2f44) 範囲 `[['00ac2f44', '00ac2f53']]`

## 命令位置別の参照

- [`00ac2ddc`](#insn-00ac2ddc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac2de0`](#insn-00ac2de0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac2df8`](#insn-00ac2df8) → `00c8d020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ac2dfc`](#insn-00ac2dfc) → [`00ac2e28`](#insn-00ac2e28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac2e08`](#insn-00ac2e08) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00ac2e0c`](#insn-00ac2e0c) → [`00ac2e28`](#insn-00ac2e28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac2e24`](#insn-00ac2e24) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00ac2e2c`](#insn-00ac2e2c) → [`00ac2e58`](#insn-00ac2e58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac2e38`](#insn-00ac2e38) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00ac2e3c`](#insn-00ac2e3c) → [`00ac2e58`](#insn-00ac2e58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac2e54`](#insn-00ac2e54) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00ac2e5c`](#insn-00ac2e5c) → [`00ac2e88`](#insn-00ac2e88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac2e68`](#insn-00ac2e68) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00ac2e6c`](#insn-00ac2e6c) → [`00ac2e88`](#insn-00ac2e88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac2e84`](#insn-00ac2e84) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00ac2e8c`](#insn-00ac2e8c) → [`00ac2eb8`](#insn-00ac2eb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac2e98`](#insn-00ac2e98) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00ac2e9c`](#insn-00ac2e9c) → [`00ac2eb8`](#insn-00ac2eb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac2eb4`](#insn-00ac2eb4) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00ac2ebc`](#insn-00ac2ebc) → [`00ac2ee8`](#insn-00ac2ee8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac2ec8`](#insn-00ac2ec8) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00ac2ecc`](#insn-00ac2ecc) → [`00ac2ee8`](#insn-00ac2ee8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac2ee4`](#insn-00ac2ee4) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00ac2eec`](#insn-00ac2eec) → [`0078dc6c`](../0078d/0078dc6c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0078dc6c` · 推定シンボル `None` · 推定型 `None`
- [`00ac2ef4`](#insn-00ac2ef4) → [`0078dc6c`](../0078d/0078dc6c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0078dc6c` · 推定シンボル `None` · 推定型 `None`
- [`00ac2efc`](#insn-00ac2efc) → [`0078dc6c`](../0078d/0078dc6c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0078dc6c` · 推定シンボル `None` · 推定型 `None`
- [`00ac2f04`](#insn-00ac2f04) → [`0078dc6c`](../0078d/0078dc6c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0078dc6c` · 推定シンボル `None` · 推定型 `None`
- [`00ac2f14`](#insn-00ac2f14) → `00c74410`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ac2f18`](#insn-00ac2f18) → [`00ac2f44`](#insn-00ac2f44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac2f24`](#insn-00ac2f24) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`00ac2f28`](#insn-00ac2f28) → [`00ac2f44`](#insn-00ac2f44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac2f40`](#insn-00ac2f40) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00ac2f48`](#insn-00ac2f48) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac2f4c`](#insn-00ac2f4c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac2f50`](#insn-00ac2f50) → [`006822e4`](../00682/006822e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006822e4` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ac2ddc`](#insn-00ac2ddc)

~~~json
{
  "source": "00ac2ddc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac2de0`](#insn-00ac2de0)

~~~json
{
  "source": "00ac2de0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac2df8`](#insn-00ac2df8)

~~~json
{
  "source": "00ac2df8",
  "target": "00c8d020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8d020",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ac2dfc`](#insn-00ac2dfc)

~~~json
{
  "source": "00ac2dfc",
  "target": "00ac2e28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac2e08`](#insn-00ac2e08)

~~~json
{
  "source": "00ac2e08",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac2e0c`](#insn-00ac2e0c)

~~~json
{
  "source": "00ac2e0c",
  "target": "00ac2e28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac2e24`](#insn-00ac2e24)

~~~json
{
  "source": "00ac2e24",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac2e2c`](#insn-00ac2e2c)

~~~json
{
  "source": "00ac2e2c",
  "target": "00ac2e58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac2e38`](#insn-00ac2e38)

~~~json
{
  "source": "00ac2e38",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac2e3c`](#insn-00ac2e3c)

~~~json
{
  "source": "00ac2e3c",
  "target": "00ac2e58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac2e54`](#insn-00ac2e54)

~~~json
{
  "source": "00ac2e54",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac2e5c`](#insn-00ac2e5c)

~~~json
{
  "source": "00ac2e5c",
  "target": "00ac2e88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac2e68`](#insn-00ac2e68)

~~~json
{
  "source": "00ac2e68",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac2e6c`](#insn-00ac2e6c)

~~~json
{
  "source": "00ac2e6c",
  "target": "00ac2e88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac2e84`](#insn-00ac2e84)

~~~json
{
  "source": "00ac2e84",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac2e8c`](#insn-00ac2e8c)

~~~json
{
  "source": "00ac2e8c",
  "target": "00ac2eb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac2e98`](#insn-00ac2e98)

~~~json
{
  "source": "00ac2e98",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac2e9c`](#insn-00ac2e9c)

~~~json
{
  "source": "00ac2e9c",
  "target": "00ac2eb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac2eb4`](#insn-00ac2eb4)

~~~json
{
  "source": "00ac2eb4",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac2ebc`](#insn-00ac2ebc)

~~~json
{
  "source": "00ac2ebc",
  "target": "00ac2ee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac2ec8`](#insn-00ac2ec8)

~~~json
{
  "source": "00ac2ec8",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac2ecc`](#insn-00ac2ecc)

~~~json
{
  "source": "00ac2ecc",
  "target": "00ac2ee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac2ee4`](#insn-00ac2ee4)

~~~json
{
  "source": "00ac2ee4",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac2eec`](#insn-00ac2eec)

~~~json
{
  "source": "00ac2eec",
  "target": "0078dc6c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac2ef4`](#insn-00ac2ef4)

~~~json
{
  "source": "00ac2ef4",
  "target": "0078dc6c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac2efc`](#insn-00ac2efc)

~~~json
{
  "source": "00ac2efc",
  "target": "0078dc6c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac2f04`](#insn-00ac2f04)

~~~json
{
  "source": "00ac2f04",
  "target": "0078dc6c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac2f14`](#insn-00ac2f14)

~~~json
{
  "source": "00ac2f14",
  "target": "00c74410",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c74410",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ac2f18`](#insn-00ac2f18)

~~~json
{
  "source": "00ac2f18",
  "target": "00ac2f44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac2f24`](#insn-00ac2f24)

~~~json
{
  "source": "00ac2f24",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac2f28`](#insn-00ac2f28)

~~~json
{
  "source": "00ac2f28",
  "target": "00ac2f44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac2f40`](#insn-00ac2f40)

~~~json
{
  "source": "00ac2f40",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac2f48`](#insn-00ac2f48)

~~~json
{
  "source": "00ac2f48",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac2f4c`](#insn-00ac2f4c)

~~~json
{
  "source": "00ac2f4c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac2f50`](#insn-00ac2f50)

~~~json
{
  "source": "00ac2f50",
  "target": "006822e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
