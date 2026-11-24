# 00c1fcfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c1f8d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f8d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0088.md#compare-b2019e6ac6e5ba206e105495fc00e530)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00c1fd98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1f/00c1fd98.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0088.md#compare-1d66147f999d756f85c581ed7729cd88)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c1fcfc",
  "name": "FUN_00c1fcfc",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7f96602729d47183da60b8363a8f154b582798c34e14b824b905b93055197216",
  "source_text_sha256": "7f96602729d47183da60b8363a8f154b582798c34e14b824b905b93055197216",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c1fcfc",
        "00c1fdf7"
      ]
    ],
    "bytes_sha256": "77f29f9bdf48a25001f2c4bd4a011dc06bef45ebad98ac4df9bd66333854806a",
    "instruction_count": 63,
    "instruction_bytes": 252,
    "body_bytes": 252,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00c1f48c](../00c1f/00c1f48c.md)
- [00c21928](../00c21/00c21928.md)

## 呼び出し先

- [00c35a44](../00c35/00c35a44.md)
- [00c53cd0](../00c53/00c53cd0.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c5dee0](../00c5d/00c5dee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1775 bytes

~~~c

void FUN_00c1fcfc(long param_1,long param_2)

{
  undefined *puVar1;
  ulong uVar2;
  long lVar3;
  ulong uVar4;
  long *plVar5;
  long *plVar6;
  ulong uVar7;
  undefined *local_48;
  undefined8 **local_40;
  undefined **local_38;
  
  puVar1 = PTR__ZNSt6__ndk17collateIwE2idE_00c9bc08;
  local_48 = PTR__ZNSt6__ndk17collateIwE2idE_00c9bc08;
  if (*(long *)PTR__ZNSt6__ndk17collateIwE2idE_00c9bc08 != -1) {
    local_38 = &local_48;
    local_40 = &local_38;
    _ZNSt6__ndk111__call_onceERVmPvPFvS2_E
              (PTR__ZNSt6__ndk17collateIwE2idE_00c9bc08,&local_40,FUN_00c35fb8);
  }
  uVar2 = (ulong)*(int *)(puVar1 + 8);
  uVar7 = uVar2 - 1;
  FUN_00c53cd0(1,param_2 + 8);
  plVar5 = (long *)(param_1 + 0x10);
  lVar3 = *plVar5;
                    /* try { // try from 00c1fd7c to 00d1fd8f has its CatchHandler @ 00c286a0 */
  uVar4 = *(long *)(param_1 + 0x18) - lVar3 >> 3;
  if (uVar4 <= uVar7) {
    if (uVar2 < uVar4 || uVar2 - uVar4 == 0) {
      if (uVar2 < uVar4) {
                    /* try { // try from 00c1fda8 to 00d1fdb3 has its CatchHandler @ 00c282b0 */
        *(ulong *)(param_1 + 0x18) = lVar3 + uVar2 * 8;
      }
    }
    else {
      FUN_00c35a44(plVar5,uVar2 - uVar4);
      lVar3 = *plVar5;
    }
  }
  plVar6 = *(long **)(lVar3 + uVar7 * 8);
                    /* try { // try from 00c1fdb4 to 00d1fdbf has its CatchHandler @ 00c282a0 */
                    /* try { // try from 00c1fdc0 to 00d1fdcb has its CatchHandler @ 00c28290 */
  if ((plVar6 != (long *)0x0) && (lVar3 = FUN_00c53d00(0xffffffffffffffff,plVar6 + 1), lVar3 == 0))
  {
                    /* try { // try from 00c1fdcc to 00d1fe33 has its CatchHandler @ 00c1f428 */
    (**(code **)(*plVar6 + 0x10))(plVar6);
  }
  *(long *)(*plVar5 + uVar7 * 8) = param_2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c1fcfc"></a> `00c1fcfc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c1fd00"></a> `00c1fd00` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00c1fd04"></a> `00c1fd04` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c1fd08"></a> `00c1fd08` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c1fd0c"></a> `00c1fd0c` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00c1fd10"></a> `00c1fd10` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00c1fd14"></a> `00c1fd14` | `f4 03 00 90` | adrp x20,0xc9b000 | `FALL_THROUGH`
<a id="insn-00c1fd18"></a> `00c1fd18` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00c1fd1c"></a> `00c1fd1c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00c1fd20"></a> `00c1fd20` | `94 06 46 f9` | ldr x20,[x20, #0xc08] | `FALL_THROUGH`
<a id="insn-00c1fd24"></a> `00c1fd24` | `f4 07 00 f9` | str x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00c1fd28"></a> `00c1fd28` | `88 fe df c8` | ldar x8,[x20] | `FALL_THROUGH`
<a id="insn-00c1fd2c"></a> `00c1fd2c` | `1f 05 00 b1` | cmn x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c1fd30"></a> `00c1fd30` | `60 01 00 54` | b.eq 0x00c1fd5c | `CONDITIONAL_JUMP`
<a id="insn-00c1fd34"></a> `00c1fd34` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00c1fd38"></a> `00c1fd38` | `a9 23 00 d1` | sub x9,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00c1fd3c"></a> `00c1fd3c` | `e0 03 00 90` | adrp x0,0xc9b000 | `FALL_THROUGH`
<a id="insn-00c1fd40"></a> `00c1fd40` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00c1fd44"></a> `00c1fd44` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00c1fd48"></a> `00c1fd48` | `82 13 0b 10` | adr x2,0xc35fb8 | `FALL_THROUGH`
<a id="insn-00c1fd4c"></a> `00c1fd4c` | `e9 0b 00 f9` | str x9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c1fd50"></a> `00c1fd50` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00c1fd54"></a> `00c1fd54` | `00 04 46 f9` | ldr x0,[x0, #0xc08] | `FALL_THROUGH`
<a id="insn-00c1fd58"></a> `00c1fd58` | `62 f8 00 94` | bl 0x00c5dee0 | `UNCONDITIONAL_CALL`
<a id="insn-00c1fd5c"></a> `00c1fd5c` | `88 0a 80 b9` | ldrsw x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00c1fd60"></a> `00c1fd60` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00c1fd64"></a> `00c1fd64` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00c1fd68"></a> `00c1fd68` | `16 05 00 d1` | sub x22,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c1fd6c"></a> `00c1fd6c` | `d9 cf 00 94` | bl 0x00c53cd0 | `UNCONDITIONAL_CALL`
<a id="insn-00c1fd70"></a> `00c1fd70` | `f4 03 15 aa` | mov x20,x21 | `FALL_THROUGH`
<a id="insn-00c1fd74"></a> `00c1fd74` | `88 26 c1 a9` | ldp x8,x9,[x20, #0x10]! | `FALL_THROUGH`
<a id="insn-00c1fd78"></a> `00c1fd78` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-00c1fd7c"></a> `00c1fd7c` | `2a fd 43 93` | asr x10,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00c1fd80"></a> `00c1fd80` | `5f 01 16 eb` | cmp x10,x22 | `FALL_THROUGH`
<a id="insn-00c1fd84"></a> `00c1fd84` | `68 01 00 54` | b.hi 0x00c1fdb0 | `CONDITIONAL_JUMP`
<a id="insn-00c1fd88"></a> `00c1fd88` | `c9 06 00 91` | add x9,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00c1fd8c"></a> `00c1fd8c` | `21 01 0a eb` | subs x1,x9,x10 | `FALL_THROUGH`
<a id="insn-00c1fd90"></a> `00c1fd90` | `a9 00 00 54` | b.ls 0x00c1fda4 | `CONDITIONAL_JUMP`
<a id="insn-00c1fd94"></a> `00c1fd94` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00c1fd98"></a> `00c1fd98` | `2b 57 00 94` | bl 0x00c35a44 | `UNCONDITIONAL_CALL`
<a id="insn-00c1fd9c"></a> `00c1fd9c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00c1fda0"></a> `00c1fda0` | `04 00 00 14` | b 0x00c1fdb0 | `UNCONDITIONAL_JUMP`
<a id="insn-00c1fda4"></a> `00c1fda4` | `62 00 00 54` | b.cs 0x00c1fdb0 | `CONDITIONAL_JUMP`
<a id="insn-00c1fda8"></a> `00c1fda8` | `09 0d 09 8b` | add x9,x8,x9, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00c1fdac"></a> `00c1fdac` | `a9 0e 00 f9` | str x9,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00c1fdb0"></a> `00c1fdb0` | `15 79 76 f8` | ldr x21,[x8, x22, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00c1fdb4"></a> `00c1fdb4` | `35 01 00 b4` | cbz x21,0x00c1fdd8 | `CONDITIONAL_JUMP`
<a id="insn-00c1fdb8"></a> `00c1fdb8` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00c1fdbc"></a> `00c1fdbc` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00c1fdc0"></a> `00c1fdc0` | `d0 cf 00 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00c1fdc4"></a> `00c1fdc4` | `a0 00 00 b5` | cbnz x0,0x00c1fdd8 | `CONDITIONAL_JUMP`
<a id="insn-00c1fdc8"></a> `00c1fdc8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c1fdcc"></a> `00c1fdcc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c1fdd0"></a> `00c1fdd0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00c1fdd4"></a> `00c1fdd4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c1fdd8"></a> `00c1fdd8` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00c1fddc"></a> `00c1fddc` | `13 79 36 f8` | str x19,[x8, x22, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00c1fde0"></a> `00c1fde0` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00c1fde4"></a> `00c1fde4` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c1fde8"></a> `00c1fde8` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c1fdec"></a> `00c1fdec` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00c1fdf0"></a> `00c1fdf0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c1fdf4"></a> `00c1fdf4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c1fcfc`](#insn-00c1fcfc) 範囲 `[['00c1fcfc', '00c1fd33']]`
  - `CONDITIONAL_JUMP` [`00c1fd30`](#insn-00c1fd30) → [`00c1fd5c`](#insn-00c1fd5c)
  - `FALL_THROUGH` [`00c1fd30`](#insn-00c1fd30) → [`00c1fd34`](#insn-00c1fd34)
- ブロック [`00c1fd34`](#insn-00c1fd34) 範囲 `[['00c1fd34', '00c1fd5b']]`
  - `FALL_THROUGH` [`00c1fd58`](#insn-00c1fd58) → [`00c1fd5c`](#insn-00c1fd5c)
- ブロック [`00c1fd5c`](#insn-00c1fd5c) 範囲 `[['00c1fd5c', '00c1fd7b']]`
  - `FALL_THROUGH` [`00c1fd78`](#insn-00c1fd78) → [`00c1fd7c`](#insn-00c1fd7c)
- ブロック [`00c1fd7c`](#insn-00c1fd7c) 範囲 `[['00c1fd7c', '00c1fd87']]`
  - `CONDITIONAL_JUMP` [`00c1fd84`](#insn-00c1fd84) → [`00c1fdb0`](#insn-00c1fdb0)
  - `FALL_THROUGH` [`00c1fd84`](#insn-00c1fd84) → [`00c1fd88`](#insn-00c1fd88)
- ブロック [`00c1fd88`](#insn-00c1fd88) 範囲 `[['00c1fd88', '00c1fd93']]`
  - `CONDITIONAL_JUMP` [`00c1fd90`](#insn-00c1fd90) → [`00c1fda4`](#insn-00c1fda4)
  - `FALL_THROUGH` [`00c1fd90`](#insn-00c1fd90) → [`00c1fd94`](#insn-00c1fd94)
- ブロック [`00c1fd94`](#insn-00c1fd94) 範囲 `[['00c1fd94', '00c1fda3']]`
  - `UNCONDITIONAL_JUMP` [`00c1fda0`](#insn-00c1fda0) → [`00c1fdb0`](#insn-00c1fdb0)
- ブロック [`00c1fda4`](#insn-00c1fda4) 範囲 `[['00c1fda4', '00c1fda7']]`
  - `CONDITIONAL_JUMP` [`00c1fda4`](#insn-00c1fda4) → [`00c1fdb0`](#insn-00c1fdb0)
  - `FALL_THROUGH` [`00c1fda4`](#insn-00c1fda4) → [`00c1fda8`](#insn-00c1fda8)
- ブロック [`00c1fda8`](#insn-00c1fda8) 範囲 `[['00c1fda8', '00c1fdaf']]`
  - `FALL_THROUGH` [`00c1fdac`](#insn-00c1fdac) → [`00c1fdb0`](#insn-00c1fdb0)
- ブロック [`00c1fdb0`](#insn-00c1fdb0) 範囲 `[['00c1fdb0', '00c1fdb3']]`
  - `FALL_THROUGH` [`00c1fdb0`](#insn-00c1fdb0) → [`00c1fdb4`](#insn-00c1fdb4)
- ブロック [`00c1fdb4`](#insn-00c1fdb4) 範囲 `[['00c1fdb4', '00c1fdb7']]`
  - `CONDITIONAL_JUMP` [`00c1fdb4`](#insn-00c1fdb4) → [`00c1fdd8`](#insn-00c1fdd8)
  - `FALL_THROUGH` [`00c1fdb4`](#insn-00c1fdb4) → [`00c1fdb8`](#insn-00c1fdb8)
- ブロック [`00c1fdb8`](#insn-00c1fdb8) 範囲 `[['00c1fdb8', '00c1fdbf']]`
  - `FALL_THROUGH` [`00c1fdbc`](#insn-00c1fdbc) → [`00c1fdc0`](#insn-00c1fdc0)
- ブロック [`00c1fdc0`](#insn-00c1fdc0) 範囲 `[['00c1fdc0', '00c1fdc7']]`
  - `CONDITIONAL_JUMP` [`00c1fdc4`](#insn-00c1fdc4) → [`00c1fdd8`](#insn-00c1fdd8)
  - `FALL_THROUGH` [`00c1fdc4`](#insn-00c1fdc4) → [`00c1fdc8`](#insn-00c1fdc8)
- ブロック [`00c1fdc8`](#insn-00c1fdc8) 範囲 `[['00c1fdc8', '00c1fdcb']]`
  - `FALL_THROUGH` [`00c1fdc8`](#insn-00c1fdc8) → [`00c1fdcc`](#insn-00c1fdcc)
- ブロック [`00c1fdcc`](#insn-00c1fdcc) 範囲 `[['00c1fdcc', '00c1fdd7']]`
  - `FALL_THROUGH` [`00c1fdd4`](#insn-00c1fdd4) → [`00c1fdd8`](#insn-00c1fdd8)
- ブロック [`00c1fdd8`](#insn-00c1fdd8) 範囲 `[['00c1fdd8', '00c1fdf7']]`

## 命令位置別の参照

- [`00c1fd04`](#insn-00c1fd04) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1fd08`](#insn-00c1fd08) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1fd0c`](#insn-00c1fd0c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1fd20`](#insn-00c1fd20) → `00c9bc08`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00c1fd24`](#insn-00c1fd24) → `01127b68`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17collateIwE2idE` · 推定型 `undefined8`
- [`00c1fd24`](#insn-00c1fd24) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1fd28`](#insn-00c1fd28) → `01127b68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17collateIwE2idE` · 推定型 `undefined8`
- [`00c1fd30`](#insn-00c1fd30) → [`00c1fd5c`](#insn-00c1fd5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1fd40`](#insn-00c1fd40) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1fd48`](#insn-00c1fd48) → [`00c35fb8`](../00c35/00c35fb8.md) · `PARAM` · `ANALYSIS` · 関数 `00c35fb8` · 推定シンボル `None` · 推定型 `None`
- [`00c1fd4c`](#insn-00c1fd4c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1fd54`](#insn-00c1fd54) → `00c9bc08`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00c1fd54`](#insn-00c1fd54) → `01127b68`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17collateIwE2idE` · 推定型 `undefined8`
- [`00c1fd58`](#insn-00c1fd58) → [`00c5dee0`](../00c5d/00c5dee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dee0` · 推定シンボル `None` · 推定型 `None`
- [`00c1fd5c`](#insn-00c1fd5c) → `01127b70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00c1fd6c`](#insn-00c1fd6c) → [`00c53cd0`](../00c53/00c53cd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53cd0` · 推定シンボル `None` · 推定型 `None`
- [`00c1fd84`](#insn-00c1fd84) → [`00c1fdb0`](#insn-00c1fdb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1fd90`](#insn-00c1fd90) → [`00c1fda4`](#insn-00c1fda4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1fd98`](#insn-00c1fd98) → [`00c35a44`](../00c35/00c35a44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c35a44` · 推定シンボル `None` · 推定型 `None`
- [`00c1fda0`](#insn-00c1fda0) → [`00c1fdb0`](#insn-00c1fdb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1fda4`](#insn-00c1fda4) → [`00c1fdb0`](#insn-00c1fdb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1fdb4`](#insn-00c1fdb4) → [`00c1fdd8`](#insn-00c1fdd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1fdc0`](#insn-00c1fdc0) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00c1fdc4`](#insn-00c1fdc4) → [`00c1fdd8`](#insn-00c1fdd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1fde0`](#insn-00c1fde0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1fde4`](#insn-00c1fde4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1fde8`](#insn-00c1fde8) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c1fd04`](#insn-00c1fd04)

~~~json
{
  "source": "00c1fd04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1fd08`](#insn-00c1fd08)

~~~json
{
  "source": "00c1fd08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1fd0c`](#insn-00c1fd0c)

~~~json
{
  "source": "00c1fd0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1fd20`](#insn-00c1fd20)

~~~json
{
  "source": "00c1fd20",
  "target": "00c9bc08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bc08",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c1fd24`](#insn-00c1fd24)

~~~json
{
  "source": "00c1fd24",
  "target": "01127b68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127b68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c1fd24`](#insn-00c1fd24)

~~~json
{
  "source": "00c1fd24",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1fd28`](#insn-00c1fd28)

~~~json
{
  "source": "00c1fd28",
  "target": "01127b68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127b68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c1fd30`](#insn-00c1fd30)

~~~json
{
  "source": "00c1fd30",
  "target": "00c1fd5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1fd40`](#insn-00c1fd40)

~~~json
{
  "source": "00c1fd40",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1fd48`](#insn-00c1fd48)

~~~json
{
  "source": "00c1fd48",
  "target": "00c35fb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1fd4c`](#insn-00c1fd4c)

~~~json
{
  "source": "00c1fd4c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1fd54`](#insn-00c1fd54)

~~~json
{
  "source": "00c1fd54",
  "target": "00c9bc08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bc08",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c1fd54`](#insn-00c1fd54)

~~~json
{
  "source": "00c1fd54",
  "target": "01127b68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127b68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c1fd58`](#insn-00c1fd58)

~~~json
{
  "source": "00c1fd58",
  "target": "00c5dee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1fd5c`](#insn-00c1fd5c)

~~~json
{
  "source": "00c1fd5c",
  "target": "01127b70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127b70",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c1fd6c`](#insn-00c1fd6c)

~~~json
{
  "source": "00c1fd6c",
  "target": "00c53cd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1fd84`](#insn-00c1fd84)

~~~json
{
  "source": "00c1fd84",
  "target": "00c1fdb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1fd90`](#insn-00c1fd90)

~~~json
{
  "source": "00c1fd90",
  "target": "00c1fda4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1fd98`](#insn-00c1fd98)

~~~json
{
  "source": "00c1fd98",
  "target": "00c35a44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1fda0`](#insn-00c1fda0)

~~~json
{
  "source": "00c1fda0",
  "target": "00c1fdb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1fda4`](#insn-00c1fda4)

~~~json
{
  "source": "00c1fda4",
  "target": "00c1fdb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1fdb4`](#insn-00c1fdb4)

~~~json
{
  "source": "00c1fdb4",
  "target": "00c1fdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1fdc0`](#insn-00c1fdc0)

~~~json
{
  "source": "00c1fdc0",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1fdc4`](#insn-00c1fdc4)

~~~json
{
  "source": "00c1fdc4",
  "target": "00c1fdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1fde0`](#insn-00c1fde0)

~~~json
{
  "source": "00c1fde0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1fde4`](#insn-00c1fde4)

~~~json
{
  "source": "00c1fde4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1fde8`](#insn-00c1fde8)

~~~json
{
  "source": "00c1fde8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
