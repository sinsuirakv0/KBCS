# 00bfaac4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfa69c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa69c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-1f9db51c5a24ef443e7cfb7a8dadd92d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfab60`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfab60.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-26522fa960208ee8d4f2c74c2738d3d0)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfaac4",
  "name": "FUN_00bfaac4",
  "size": 240,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "905f9b7d60c3362f7a7a28d1131ce1a89ec422ae2595ca39443a1e5eb16fce9c",
  "source_text_sha256": "905f9b7d60c3362f7a7a28d1131ce1a89ec422ae2595ca39443a1e5eb16fce9c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfaac4",
        "00bfabb3"
      ]
    ],
    "bytes_sha256": "176396c356fe9549a55f33d61cbe9a40ef2442481e8da06d489fc0245a5a71d9",
    "instruction_count": 60,
    "instruction_bytes": 240,
    "body_bytes": 240,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bfac40](../00bfa/00bfac40.md)

## 呼び出し先

- [00bfac64](../00bfa/00bfac64.md)
- [00c53cd0](../00c53/00c53cd0.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c58000](../00c58/00c58000.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1577 bytes

~~~c

void FUN_00bfaac4(long *param_1,long param_2)

{
  ulong uVar1;
  long *plVar2;
  long lVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  size_t __n;
  ulong uVar6;
  long lVar7;
  ulong uVar8;
  void *__src;
  long lVar9;
  long *plVar10;
  
  plVar2 = (long *)param_1[1];
  if (plVar2 < (long *)param_1[2]) {
    plVar10 = plVar2 + 1;
    *plVar2 = param_2;
  }
  else {
    __src = (void *)*param_1;
    __n = (long)plVar2 - (long)__src;
    lVar9 = (long)__n >> 3;
    uVar1 = lVar9 + 1;
    if (uVar1 >> 0x3d != 0) {
      puVar4 = (undefined8 *)FUN_00bfac64(param_1);
      puVar5 = (undefined8 *)_Znwm(0x30);
      *puVar4 = puVar5;
      puVar5[1] = 0;
      *puVar5 = 0;
      puVar5[3] = 0;
      puVar5[2] = 0;
      puVar5[5] = 0;
      puVar5[4] = 0;
      return;
    }
    uVar6 = param_1[2] - (long)__src;
    uVar8 = (long)uVar6 >> 2;
    if (uVar8 <= uVar1) {
      uVar8 = uVar1;
    }
    if (0x7ffffffffffffff7 < uVar6) {
      uVar8 = 0x1fffffffffffffff;
    }
    if (uVar8 == 0) {
      lVar3 = 0;
      lVar7 = lVar9;
    }
    else {
      lVar3 = _Znwm(uVar8 << 3);
      __src = (void *)*param_1;
      __n = param_1[1] - (long)__src;
      lVar7 = (long)__n >> 3;
    }
    plVar2 = (long *)(lVar3 + lVar9 * 8);
    plVar10 = plVar2 + 1;
    *plVar2 = param_2;
    memcpy(plVar2 + -lVar7,__src,__n);
    *param_1 = (long)(plVar2 + -lVar7);
    param_1[1] = (long)plVar10;
    param_1[2] = lVar3 + uVar8 * 8;
    if (__src != (void *)0x0) {
      _ZdlPv(__src);
    }
  }
  param_1[1] = (long)plVar10;
  FUN_00c53cd0(1,param_2 + 8);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfaac4"></a> `00bfaac4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfaac8"></a> `00bfaac8` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bfaacc"></a> `00bfaacc` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfaad0"></a> `00bfaad0` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfaad4"></a> `00bfaad4` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfaad8"></a> `00bfaad8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfaadc"></a> `00bfaadc` | `17 a0 40 a9` | ldp x23,x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bfaae0"></a> `00bfaae0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfaae4"></a> `00bfaae4` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bfaae8"></a> `00bfaae8` | `ff 02 08 eb` | cmp x23,x8 | `FALL_THROUGH`
<a id="insn-00bfaaec"></a> `00bfaaec` | `62 00 00 54` | b.cs 0x00bfaaf8 | `CONDITIONAL_JUMP`
<a id="insn-00bfaaf0"></a> `00bfaaf0` | `f4 86 00 f8` | str x20,[x23], #0x8 | `FALL_THROUGH`
<a id="insn-00bfaaf4"></a> `00bfaaf4` | `24 00 00 14` | b 0x00bfab84 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfaaf8"></a> `00bfaaf8` | `75 02 40 f9` | ldr x21,[x19] | `FALL_THROUGH`
<a id="insn-00bfaafc"></a> `00bfaafc` | `e2 02 15 cb` | sub x2,x23,x21 | `FALL_THROUGH`
<a id="insn-00bfab00"></a> `00bfab00` | `56 fc 43 93` | asr x22,x2,#0x3 | `FALL_THROUGH`
<a id="insn-00bfab04"></a> `00bfab04` | `c9 06 00 91` | add x9,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00bfab08"></a> `00bfab08` | `2a fd 7d d3` | lsr x10,x9,#0x3d | `FALL_THROUGH`
<a id="insn-00bfab0c"></a> `00bfab0c` | `0a 05 00 b5` | cbnz x10,0x00bfabac | `CONDITIONAL_JUMP`
<a id="insn-00bfab10"></a> `00bfab10` | `08 01 15 cb` | sub x8,x8,x21 | `FALL_THROUGH`
<a id="insn-00bfab14"></a> `00bfab14` | `eb ef 7d b2` | orr x11,xzr,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-00bfab18"></a> `00bfab18` | `0a fd 42 93` | asr x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bfab1c"></a> `00bfab1c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bfab20"></a> `00bfab20` | `49 81 89 9a` | csel x9,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00bfab24"></a> `00bfab24` | `1f 01 0b eb` | cmp x8,x11 | `FALL_THROUGH`
<a id="insn-00bfab28"></a> `00bfab28` | `08 00 fc 92` | mov x8,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bfab2c"></a> `00bfab2c` | `38 31 88 9a` | csel x24,x9,x8,cc | `FALL_THROUGH`
<a id="insn-00bfab30"></a> `00bfab30` | `f8 00 00 b4` | cbz x24,0x00bfab4c | `CONDITIONAL_JUMP`
<a id="insn-00bfab34"></a> `00bfab34` | `00 f3 7d d3` | lsl x0,x24,#0x3 | `FALL_THROUGH`
<a id="insn-00bfab38"></a> `00bfab38` | `d6 74 01 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bfab3c"></a> `00bfab3c` | `75 22 40 a9` | ldp x21,x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfab40"></a> `00bfab40` | `02 01 15 cb` | sub x2,x8,x21 | `FALL_THROUGH`
<a id="insn-00bfab44"></a> `00bfab44` | `48 fc 43 93` | asr x8,x2,#0x3 | `FALL_THROUGH`
<a id="insn-00bfab48"></a> `00bfab48` | `03 00 00 14` | b 0x00bfab54 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfab4c"></a> `00bfab4c` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bfab50"></a> `00bfab50` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00bfab54"></a> `00bfab54` | `17 0c 16 8b` | add x23,x0,x22, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bfab58"></a> `00bfab58` | `18 0c 18 8b` | add x24,x0,x24, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bfab5c"></a> `00bfab5c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bfab60"></a> `00bfab60` | `f6 0e 08 cb` | sub x22,x23,x8, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bfab64"></a> `00bfab64` | `f4 86 00 f8` | str x20,[x23], #0x8 | `FALL_THROUGH`
<a id="insn-00bfab68"></a> `00bfab68` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bfab6c"></a> `00bfab6c` | `25 75 01 94` | bl 0x00c58000 | `UNCONDITIONAL_CALL`
<a id="insn-00bfab70"></a> `00bfab70` | `76 5e 00 a9` | stp x22,x23,[x19] | `FALL_THROUGH`
<a id="insn-00bfab74"></a> `00bfab74` | `78 0a 00 f9` | str x24,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bfab78"></a> `00bfab78` | `75 00 00 b4` | cbz x21,0x00bfab84 | `CONDITIONAL_JUMP`
<a id="insn-00bfab7c"></a> `00bfab7c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bfab80"></a> `00bfab80` | `cc 74 01 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfab84"></a> `00bfab84` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00bfab88"></a> `00bfab88` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfab8c"></a> `00bfab8c` | `77 06 00 f9` | str x23,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfab90"></a> `00bfab90` | `50 64 01 94` | bl 0x00c53cd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfab94"></a> `00bfab94` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfab98"></a> `00bfab98` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfab9c"></a> `00bfab9c` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfaba0"></a> `00bfaba0` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bfaba4"></a> `00bfaba4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfaba8"></a> `00bfaba8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfabac"></a> `00bfabac` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfabb0"></a> `00bfabb0` | `2d 00 00 94` | bl 0x00bfac64 | `UNCONDITIONAL_CALL`

## 基本ブロックと分岐先

- ブロック [`00bfaac4`](#insn-00bfaac4) 範囲 `[['00bfaac4', '00bfaaef']]`
  - `CONDITIONAL_JUMP` [`00bfaaec`](#insn-00bfaaec) → [`00bfaaf8`](#insn-00bfaaf8)
  - `FALL_THROUGH` [`00bfaaec`](#insn-00bfaaec) → [`00bfaaf0`](#insn-00bfaaf0)
- ブロック [`00bfaaf0`](#insn-00bfaaf0) 範囲 `[['00bfaaf0', '00bfaaf7']]`
  - `UNCONDITIONAL_JUMP` [`00bfaaf4`](#insn-00bfaaf4) → [`00bfab84`](#insn-00bfab84)
- ブロック [`00bfaaf8`](#insn-00bfaaf8) 範囲 `[['00bfaaf8', '00bfab0f']]`
  - `CONDITIONAL_JUMP` [`00bfab0c`](#insn-00bfab0c) → [`00bfabac`](#insn-00bfabac)
  - `FALL_THROUGH` [`00bfab0c`](#insn-00bfab0c) → [`00bfab10`](#insn-00bfab10)
- ブロック [`00bfab10`](#insn-00bfab10) 範囲 `[['00bfab10', '00bfab33']]`
  - `CONDITIONAL_JUMP` [`00bfab30`](#insn-00bfab30) → [`00bfab4c`](#insn-00bfab4c)
  - `FALL_THROUGH` [`00bfab30`](#insn-00bfab30) → [`00bfab34`](#insn-00bfab34)
- ブロック [`00bfab34`](#insn-00bfab34) 範囲 `[['00bfab34', '00bfab4b']]`
  - `UNCONDITIONAL_JUMP` [`00bfab48`](#insn-00bfab48) → [`00bfab54`](#insn-00bfab54)
- ブロック [`00bfab4c`](#insn-00bfab4c) 範囲 `[['00bfab4c', '00bfab53']]`
  - `FALL_THROUGH` [`00bfab50`](#insn-00bfab50) → [`00bfab54`](#insn-00bfab54)
- ブロック [`00bfab54`](#insn-00bfab54) 範囲 `[['00bfab54', '00bfab7b']]`
  - `CONDITIONAL_JUMP` [`00bfab78`](#insn-00bfab78) → [`00bfab84`](#insn-00bfab84)
  - `FALL_THROUGH` [`00bfab78`](#insn-00bfab78) → [`00bfab7c`](#insn-00bfab7c)
- ブロック [`00bfab7c`](#insn-00bfab7c) 範囲 `[['00bfab7c', '00bfab83']]`
  - `FALL_THROUGH` [`00bfab80`](#insn-00bfab80) → [`00bfab84`](#insn-00bfab84)
- ブロック [`00bfab84`](#insn-00bfab84) 範囲 `[['00bfab84', '00bfabab']]`
- ブロック [`00bfabac`](#insn-00bfabac) 範囲 `[['00bfabac', '00bfabb3']]`
  - `FALL_THROUGH` [`00bfabb0`](#insn-00bfabb0) → [`00bfabb4`](00bfabb4.md)

## 命令位置別の参照

- [`00bfaac8`](#insn-00bfaac8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaacc`](#insn-00bfaacc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaad0`](#insn-00bfaad0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaad4`](#insn-00bfaad4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaaec`](#insn-00bfaaec) → [`00bfaaf8`](#insn-00bfaaf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaaf4`](#insn-00bfaaf4) → [`00bfab84`](#insn-00bfab84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfab0c`](#insn-00bfab0c) → [`00bfabac`](#insn-00bfabac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfab30`](#insn-00bfab30) → [`00bfab4c`](#insn-00bfab4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfab38`](#insn-00bfab38) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bfab48`](#insn-00bfab48) → [`00bfab54`](#insn-00bfab54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfab6c`](#insn-00bfab6c) → [`00c58000`](../00c58/00c58000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58000` · 推定シンボル `None` · 推定型 `None`
- [`00bfab78`](#insn-00bfab78) → [`00bfab84`](#insn-00bfab84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfab80`](#insn-00bfab80) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bfab90`](#insn-00bfab90) → [`00c53cd0`](../00c53/00c53cd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53cd0` · 推定シンボル `None` · 推定型 `None`
- [`00bfab94`](#insn-00bfab94) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfab98`](#insn-00bfab98) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfab9c`](#insn-00bfab9c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaba0`](#insn-00bfaba0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfabb0`](#insn-00bfabb0) → [`00bfac64`](00bfac64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bfac64` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfaac8`](#insn-00bfaac8)

~~~json
{
  "source": "00bfaac8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaacc`](#insn-00bfaacc)

~~~json
{
  "source": "00bfaacc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaad0`](#insn-00bfaad0)

~~~json
{
  "source": "00bfaad0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaad4`](#insn-00bfaad4)

~~~json
{
  "source": "00bfaad4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaaec`](#insn-00bfaaec)

~~~json
{
  "source": "00bfaaec",
  "target": "00bfaaf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaaf4`](#insn-00bfaaf4)

~~~json
{
  "source": "00bfaaf4",
  "target": "00bfab84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfab0c`](#insn-00bfab0c)

~~~json
{
  "source": "00bfab0c",
  "target": "00bfabac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfab30`](#insn-00bfab30)

~~~json
{
  "source": "00bfab30",
  "target": "00bfab4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfab38`](#insn-00bfab38)

~~~json
{
  "source": "00bfab38",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfab48`](#insn-00bfab48)

~~~json
{
  "source": "00bfab48",
  "target": "00bfab54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfab6c`](#insn-00bfab6c)

~~~json
{
  "source": "00bfab6c",
  "target": "00c58000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfab78`](#insn-00bfab78)

~~~json
{
  "source": "00bfab78",
  "target": "00bfab84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfab80`](#insn-00bfab80)

~~~json
{
  "source": "00bfab80",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfab90`](#insn-00bfab90)

~~~json
{
  "source": "00bfab90",
  "target": "00c53cd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfab94`](#insn-00bfab94)

~~~json
{
  "source": "00bfab94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfab98`](#insn-00bfab98)

~~~json
{
  "source": "00bfab98",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfab9c`](#insn-00bfab9c)

~~~json
{
  "source": "00bfab9c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaba0`](#insn-00bfaba0)

~~~json
{
  "source": "00bfaba0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfabb0`](#insn-00bfabb0)

~~~json
{
  "source": "00bfabb0",
  "target": "00bfac64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
