# 00b2fddc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b2fd40`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2fd40.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0069.md#compare-6dfeceeb811372cb4e57525685795cc0)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00b30dd0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b30/00b30dd0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0031.md#compare-2fdf88ab2ebb09ce1b4d7b83e6182977)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b2fddc",
  "name": "FUN_00b2fddc",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "54c4bf73545be37d03da2edf8f9fbf6d4ac0792797d3201860d6b186a0e5a373",
  "source_text_sha256": "54c4bf73545be37d03da2edf8f9fbf6d4ac0792797d3201860d6b186a0e5a373",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b2fddc",
        "00b2fecb"
      ],
      [
        "00b2ff10",
        "00b2ff13"
      ]
    ],
    "bytes_sha256": "e4fd9810b46cf55b22ed1eefbcc311ea20d098d5172688eeccf84b75e17f481d",
    "instruction_count": 61,
    "instruction_bytes": 244,
    "body_bytes": 244,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b2faa8](../00b2f/00b2faa8.md)

## 呼び出し先

- [0043bb60](../0043b/0043bb60.md)
- [00b308b4](../00b30/00b308b4.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1439 bytes

~~~c

void FUN_00b2fddc(undefined8 param_1,undefined8 param_2,ulong *param_3,undefined8 param_4,
                 undefined4 param_5)

{
  long lVar1;
  ulong uVar2;
  ulong uVar3;
  void *pvVar4;
  ulong local_80;
  ulong uStack_78;
  void *local_70;
  ulong local_60;
  ulong uStack_58;
  void *local_50;
  long local_48;
  
                    /* try { // try from 00b2fde4 to 00c2fdeb has its CatchHandler @ 00b2fe58 */
                    /* try { // try from 00b2fdec to 00c2fedb has its CatchHandler @ 00b2fd70 */
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  if ((*param_3 & 1) == 0) {
    uStack_78 = param_3[1];
    local_80 = *param_3;
    local_70 = (void *)param_3[2];
  }
  else {
    FUN_0043bb60(&local_80,param_3[2],param_3[1]);
  }
  uVar2 = local_80;
  uVar3 = uStack_78;
  pvVar4 = local_70;
  if ((local_80 & 1) != 0) {
    FUN_0043bb60(&local_60,local_70,uStack_78);
    uVar2 = local_60;
    uVar3 = uStack_58;
    pvVar4 = local_50;
  }
  local_50 = pvVar4;
  uStack_58 = uVar3;
  local_60 = uVar2;
  FUN_00b308b4(param_1,param_2,0,&local_60,param_4,param_5);
  if ((local_60 & 1) != 0) {
    _ZdlPv(local_50);
  }
  if ((local_80 & 1) != 0) {
    _ZdlPv(local_70);
  }
                    /* catch() { ... } // from try @ 00b2fdd8 with catch @ 00b2feac */
  if (*(long *)(lVar1 + 0x28) == local_48) {
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
<a id="insn-00b2fddc"></a> `00b2fddc` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00b2fde0"></a> `00b2fde0` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b2fde4"></a> `00b2fde4` | `f7 2b 00 f9` | str x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b2fde8"></a> `00b2fde8` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b2fdec"></a> `00b2fdec` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b2fdf0"></a> `00b2fdf0` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00b2fdf4"></a> `00b2fdf4` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b2fdf8"></a> `00b2fdf8` | `f3 03 03 2a` | mov w19,w3 | `FALL_THROUGH`
<a id="insn-00b2fdfc"></a> `00b2fdfc` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00b2fe00"></a> `00b2fe00` | `e9 16 40 f9` | ldr x9,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00b2fe04"></a> `00b2fe04` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b2fe08"></a> `00b2fe08` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00b2fe0c"></a> `00b2fe0c` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00b2fe10"></a> `00b2fe10` | `29 00 40 39` | ldrb w9,[x1] | `FALL_THROUGH`
<a id="insn-00b2fe14"></a> `00b2fe14` | `69 01 00 37` | tbnz w9,#0x0,0x00b2fe40 | `CONDITIONAL_JUMP`
<a id="insn-00b2fe18"></a> `00b2fe18` | `20 00 c0 3d` | ldr q0,[x1] | `FALL_THROUGH`
<a id="insn-00b2fe1c"></a> `00b2fe1c` | `28 08 40 f9` | ldr x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00b2fe20"></a> `00b2fe20` | `e0 03 80 3d` | str q0,[sp] | `FALL_THROUGH`
<a id="insn-00b2fe24"></a> `00b2fe24` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b2fe28"></a> `00b2fe28` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00b2fe2c"></a> `00b2fe2c` | `68 01 00 36` | tbz w8,#0x0,0x00b2fe58 | `CONDITIONAL_JUMP`
<a id="insn-00b2fe30"></a> `00b2fe30` | `e2 87 40 a9` | ldp x2,x1,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b2fe34"></a> `00b2fe34` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b2fe38"></a> `00b2fe38` | `4a 2f e4 97` | bl 0x0043bb60 | `UNCONDITIONAL_CALL`
<a id="insn-00b2fe3c"></a> `00b2fe3c` | `0b 00 00 14` | b 0x00b2fe68 | `UNCONDITIONAL_JUMP`
<a id="insn-00b2fe40"></a> `00b2fe40` | `22 a0 40 a9` | ldp x2,x8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00b2fe44"></a> `00b2fe44` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00b2fe48"></a> `00b2fe48` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00b2fe4c"></a> `00b2fe4c` | `45 2f e4 97` | bl 0x0043bb60 | `UNCONDITIONAL_CALL`
<a id="insn-00b2fe50"></a> `00b2fe50` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00b2fe54"></a> `00b2fe54` | `e8 fe 07 37` | tbnz w8,#0x0,0x00b2fe30 | `CONDITIONAL_JUMP`
<a id="insn-00b2fe58"></a> `00b2fe58` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00b2fe5c"></a> `00b2fe5c` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b2fe60"></a> `00b2fe60` | `e0 0b 80 3d` | str q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b2fe64"></a> `00b2fe64` | `e8 1b 00 f9` | str x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b2fe68"></a> `00b2fe68` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b2fe6c"></a> `00b2fe6c` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00b2fe70"></a> `00b2fe70` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b2fe74"></a> `00b2fe74` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00b2fe78"></a> `00b2fe78` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00b2fe7c"></a> `00b2fe7c` | `e4 03 13 2a` | mov w4,w19 | `FALL_THROUGH`
<a id="insn-00b2fe80"></a> `00b2fe80` | `8d 02 00 94` | bl 0x00b308b4 | `UNCONDITIONAL_CALL`
<a id="insn-00b2fe84"></a> `00b2fe84` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b2fe88"></a> `00b2fe88` | `68 00 00 36` | tbz w8,#0x0,0x00b2fe94 | `CONDITIONAL_JUMP`
<a id="insn-00b2fe8c"></a> `00b2fe8c` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b2fe90"></a> `00b2fe90` | `3c a0 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b2fe94"></a> `00b2fe94` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00b2fe98"></a> `00b2fe98` | `68 00 00 36` | tbz w8,#0x0,0x00b2fea4 | `CONDITIONAL_JUMP`
<a id="insn-00b2fe9c"></a> `00b2fe9c` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b2fea0"></a> `00b2fea0` | `38 a0 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b2fea4"></a> `00b2fea4` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00b2fea8"></a> `00b2fea8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00b2feac"></a> `00b2feac` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b2feb0"></a> `00b2feb0` | `01 03 00 54` | b.ne 0x00b2ff10 | `CONDITIONAL_JUMP`
<a id="insn-00b2feb4"></a> `00b2feb4` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b2feb8"></a> `00b2feb8` | `f7 2b 40 f9` | ldr x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b2febc"></a> `00b2febc` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b2fec0"></a> `00b2fec0` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b2fec4"></a> `00b2fec4` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00b2fec8"></a> `00b2fec8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b2ff10"></a> `00b2ff10` | `28 a0 04 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b2fddc`](#insn-00b2fddc) 範囲 `[['00b2fddc', '00b2fde3']]`
  - `FALL_THROUGH` [`00b2fde0`](#insn-00b2fde0) → [`00b2fde4`](#insn-00b2fde4)
- ブロック [`00b2fde4`](#insn-00b2fde4) 範囲 `[['00b2fde4', '00b2fdeb']]`
  - `FALL_THROUGH` [`00b2fde8`](#insn-00b2fde8) → [`00b2fdec`](#insn-00b2fdec)
- ブロック [`00b2fdec`](#insn-00b2fdec) 範囲 `[['00b2fdec', '00b2fe17']]`
  - `CONDITIONAL_JUMP` [`00b2fe14`](#insn-00b2fe14) → [`00b2fe40`](#insn-00b2fe40)
  - `FALL_THROUGH` [`00b2fe14`](#insn-00b2fe14) → [`00b2fe18`](#insn-00b2fe18)
- ブロック [`00b2fe18`](#insn-00b2fe18) 範囲 `[['00b2fe18', '00b2fe2f']]`
  - `CONDITIONAL_JUMP` [`00b2fe2c`](#insn-00b2fe2c) → [`00b2fe58`](#insn-00b2fe58)
  - `FALL_THROUGH` [`00b2fe2c`](#insn-00b2fe2c) → [`00b2fe30`](#insn-00b2fe30)
- ブロック [`00b2fe30`](#insn-00b2fe30) 範囲 `[['00b2fe30', '00b2fe3f']]`
  - `UNCONDITIONAL_JUMP` [`00b2fe3c`](#insn-00b2fe3c) → [`00b2fe68`](#insn-00b2fe68)
- ブロック [`00b2fe40`](#insn-00b2fe40) 範囲 `[['00b2fe40', '00b2fe57']]`
  - `CONDITIONAL_JUMP` [`00b2fe54`](#insn-00b2fe54) → [`00b2fe30`](#insn-00b2fe30)
  - `FALL_THROUGH` [`00b2fe54`](#insn-00b2fe54) → [`00b2fe58`](#insn-00b2fe58)
- ブロック [`00b2fe58`](#insn-00b2fe58) 範囲 `[['00b2fe58', '00b2fe67']]`
  - `FALL_THROUGH` [`00b2fe64`](#insn-00b2fe64) → [`00b2fe68`](#insn-00b2fe68)
- ブロック [`00b2fe68`](#insn-00b2fe68) 範囲 `[['00b2fe68', '00b2fe8b']]`
  - `CONDITIONAL_JUMP` [`00b2fe88`](#insn-00b2fe88) → [`00b2fe94`](#insn-00b2fe94)
  - `FALL_THROUGH` [`00b2fe88`](#insn-00b2fe88) → [`00b2fe8c`](#insn-00b2fe8c)
- ブロック [`00b2fe8c`](#insn-00b2fe8c) 範囲 `[['00b2fe8c', '00b2fe93']]`
  - `FALL_THROUGH` [`00b2fe90`](#insn-00b2fe90) → [`00b2fe94`](#insn-00b2fe94)
- ブロック [`00b2fe94`](#insn-00b2fe94) 範囲 `[['00b2fe94', '00b2fe9b']]`
  - `CONDITIONAL_JUMP` [`00b2fe98`](#insn-00b2fe98) → [`00b2fea4`](#insn-00b2fea4)
  - `FALL_THROUGH` [`00b2fe98`](#insn-00b2fe98) → [`00b2fe9c`](#insn-00b2fe9c)
- ブロック [`00b2fe9c`](#insn-00b2fe9c) 範囲 `[['00b2fe9c', '00b2fea3']]`
  - `FALL_THROUGH` [`00b2fea0`](#insn-00b2fea0) → [`00b2fea4`](#insn-00b2fea4)
- ブロック [`00b2fea4`](#insn-00b2fea4) 範囲 `[['00b2fea4', '00b2feab']]`
  - `FALL_THROUGH` [`00b2fea8`](#insn-00b2fea8) → [`00b2feac`](#insn-00b2feac)
- ブロック [`00b2feac`](#insn-00b2feac) 範囲 `[['00b2feac', '00b2feb3']]`
  - `CONDITIONAL_JUMP` [`00b2feb0`](#insn-00b2feb0) → [`00b2ff10`](#insn-00b2ff10)
  - `FALL_THROUGH` [`00b2feb0`](#insn-00b2feb0) → [`00b2feb4`](#insn-00b2feb4)
- ブロック [`00b2feb4`](#insn-00b2feb4) 範囲 `[['00b2feb4', '00b2fecb']]`
- ブロック [`00b2ff10`](#insn-00b2ff10) 範囲 `[['00b2ff10', '00b2ff13']]`

## 命令位置別の参照

- [`00b2fde0`](#insn-00b2fde0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2fde4`](#insn-00b2fde4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2fde8`](#insn-00b2fde8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2fdec`](#insn-00b2fdec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2fe0c`](#insn-00b2fe0c) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2fe14`](#insn-00b2fe14) → [`00b2fe40`](#insn-00b2fe40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2fe20`](#insn-00b2fe20) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2fe24`](#insn-00b2fe24) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2fe28`](#insn-00b2fe28) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2fe2c`](#insn-00b2fe2c) → [`00b2fe58`](#insn-00b2fe58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2fe30`](#insn-00b2fe30) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2fe38`](#insn-00b2fe38) → [`0043bb60`](../0043b/0043bb60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb60` · 推定シンボル `None` · 推定型 `None`
- [`00b2fe3c`](#insn-00b2fe3c) → [`00b2fe68`](#insn-00b2fe68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2fe4c`](#insn-00b2fe4c) → [`0043bb60`](../0043b/0043bb60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb60` · 推定シンボル `None` · 推定型 `None`
- [`00b2fe50`](#insn-00b2fe50) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2fe54`](#insn-00b2fe54) → [`00b2fe30`](#insn-00b2fe30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2fe58`](#insn-00b2fe58) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2fe5c`](#insn-00b2fe5c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2fe60`](#insn-00b2fe60) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2fe64`](#insn-00b2fe64) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2fe80`](#insn-00b2fe80) → [`00b308b4`](../00b30/00b308b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b308b4` · 推定シンボル `None` · 推定型 `None`
- [`00b2fe84`](#insn-00b2fe84) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2fe88`](#insn-00b2fe88) → [`00b2fe94`](#insn-00b2fe94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2fe8c`](#insn-00b2fe8c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2fe90`](#insn-00b2fe90) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b2fe94`](#insn-00b2fe94) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2fe98`](#insn-00b2fe98) → [`00b2fea4`](#insn-00b2fea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2fe9c`](#insn-00b2fe9c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2fea0`](#insn-00b2fea0) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b2fea8`](#insn-00b2fea8) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2feb0`](#insn-00b2feb0) → [`00b2ff10`](#insn-00b2ff10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2feb4`](#insn-00b2feb4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2feb8`](#insn-00b2feb8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2febc`](#insn-00b2febc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2fec0`](#insn-00b2fec0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ff10`](#insn-00b2ff10) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b2fde0`](#insn-00b2fde0)

~~~json
{
  "source": "00b2fde0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2fde4`](#insn-00b2fde4)

~~~json
{
  "source": "00b2fde4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2fde8`](#insn-00b2fde8)

~~~json
{
  "source": "00b2fde8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2fdec`](#insn-00b2fdec)

~~~json
{
  "source": "00b2fdec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2fe0c`](#insn-00b2fe0c)

~~~json
{
  "source": "00b2fe0c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2fe14`](#insn-00b2fe14)

~~~json
{
  "source": "00b2fe14",
  "target": "00b2fe40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2fe20`](#insn-00b2fe20)

~~~json
{
  "source": "00b2fe20",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2fe24`](#insn-00b2fe24)

~~~json
{
  "source": "00b2fe24",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2fe28`](#insn-00b2fe28)

~~~json
{
  "source": "00b2fe28",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2fe2c`](#insn-00b2fe2c)

~~~json
{
  "source": "00b2fe2c",
  "target": "00b2fe58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2fe30`](#insn-00b2fe30)

~~~json
{
  "source": "00b2fe30",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2fe38`](#insn-00b2fe38)

~~~json
{
  "source": "00b2fe38",
  "target": "0043bb60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2fe3c`](#insn-00b2fe3c)

~~~json
{
  "source": "00b2fe3c",
  "target": "00b2fe68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2fe4c`](#insn-00b2fe4c)

~~~json
{
  "source": "00b2fe4c",
  "target": "0043bb60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2fe50`](#insn-00b2fe50)

~~~json
{
  "source": "00b2fe50",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2fe54`](#insn-00b2fe54)

~~~json
{
  "source": "00b2fe54",
  "target": "00b2fe30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2fe58`](#insn-00b2fe58)

~~~json
{
  "source": "00b2fe58",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2fe5c`](#insn-00b2fe5c)

~~~json
{
  "source": "00b2fe5c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2fe60`](#insn-00b2fe60)

~~~json
{
  "source": "00b2fe60",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2fe64`](#insn-00b2fe64)

~~~json
{
  "source": "00b2fe64",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2fe80`](#insn-00b2fe80)

~~~json
{
  "source": "00b2fe80",
  "target": "00b308b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2fe84`](#insn-00b2fe84)

~~~json
{
  "source": "00b2fe84",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2fe88`](#insn-00b2fe88)

~~~json
{
  "source": "00b2fe88",
  "target": "00b2fe94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2fe8c`](#insn-00b2fe8c)

~~~json
{
  "source": "00b2fe8c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2fe90`](#insn-00b2fe90)

~~~json
{
  "source": "00b2fe90",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2fe94`](#insn-00b2fe94)

~~~json
{
  "source": "00b2fe94",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2fe98`](#insn-00b2fe98)

~~~json
{
  "source": "00b2fe98",
  "target": "00b2fea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2fe9c`](#insn-00b2fe9c)

~~~json
{
  "source": "00b2fe9c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2fea0`](#insn-00b2fea0)

~~~json
{
  "source": "00b2fea0",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2fea8`](#insn-00b2fea8)

~~~json
{
  "source": "00b2fea8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2feb0`](#insn-00b2feb0)

~~~json
{
  "source": "00b2feb0",
  "target": "00b2ff10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2feb4`](#insn-00b2feb4)

~~~json
{
  "source": "00b2feb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2feb8`](#insn-00b2feb8)

~~~json
{
  "source": "00b2feb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2febc`](#insn-00b2febc)

~~~json
{
  "source": "00b2febc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2fec0`](#insn-00b2fec0)

~~~json
{
  "source": "00b2fec0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ff10`](#insn-00b2ff10)

~~~json
{
  "source": "00b2ff10",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
