# 00a6aacc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00a6a8d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a8d4.md) · 移動量 `+0x1f8`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0034.md#compare-3d336270af4e5ca8ab730e3eb58758de)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00a6ab3c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a6a/00a6ab3c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0034.md#compare-e502e1562f7d093b25e1c9fa9d626a6d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a6aacc",
  "name": "FUN_00a6aacc",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9d0e18e762b5468bd0b74beb91041483598c88732d7ff4dfc178ac3b1d381144",
  "source_text_sha256": "9d0e18e762b5468bd0b74beb91041483598c88732d7ff4dfc178ac3b1d381144",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a6aacc",
        "00a6abcb"
      ],
      [
        "00a6ac04",
        "00a6ac07"
      ]
    ],
    "bytes_sha256": "50f0f730c98eb43ed45dbf3e0ddfb580015b5eed3ab00042a6c5a7770e0a896e",
    "instruction_count": 65,
    "instruction_bytes": 260,
    "body_bytes": 260,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0093b770](../0093b/0093b770.md)

## 呼び出し先

- [00a6c0e4](../00a6c/00a6c0e4.md)
- [00a6c110](../00a6c/00a6c110.md)
- [00a6c138](../00a6c/00a6c138.md)
- [00a6c160](../00a6c/00a6c160.md)
- [00a6c1e8](../00a6c/00a6c1e8.md)
- [00a6c488](../00a6c/00a6c488.md)
- [00c57ee0](../00c57/00c57ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1353 bytes

~~~c

void FUN_00a6aacc(undefined8 *param_1,long param_2)

{
  long lVar1;
  long lVar2;
  undefined8 local_50;
  undefined8 uStack_48;
  undefined8 local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  lVar2 = *(long *)(param_2 + 0x70);
  param_1[0xe] = 0;
  param_1[3] = 0;
  param_1[2] = 0;
  param_1[5] = 0;
  param_1[4] = 0;
  param_1[7] = 0;
  param_1[6] = 0;
  param_1[9] = 0;
  param_1[8] = 0;
  param_1[0xb] = 0;
  param_1[10] = 0;
  param_1[0xd] = 0;
  param_1[0xc] = 0;
  param_1[1] = 0;
  *param_1 = 0;
  if ((lVar2 != 0) && (lVar2 = FUN_00a6c488(), lVar2 != 0)) {
    FUN_00a6c0e4(&local_50,lVar2);
    param_1[1] = uStack_48;
    *param_1 = local_50;
    param_1[2] = local_40;
    FUN_00a6c110(&local_50,lVar2);
    param_1[4] = uStack_48;
    param_1[3] = local_50;
    param_1[5] = local_40;
    FUN_00a6c138(&local_50,lVar2);
    param_1[7] = uStack_48;
    param_1[6] = local_50;
    param_1[8] = local_40;
    FUN_00a6c160(&local_50,lVar2);
    param_1[10] = uStack_48;
    param_1[9] = local_50;
    param_1[0xb] = local_40;
    FUN_00a6c1e8(&local_50,lVar2);
    param_1[0xd] = uStack_48;
    param_1[0xc] = local_50;
    param_1[0xe] = local_40;
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
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
<a id="insn-00a6aacc"></a> `00a6aacc` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00a6aad0"></a> `00a6aad0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a6aad4"></a> `00a6aad4` | `f5 1b 00 f9` | str x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a6aad8"></a> `00a6aad8` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a6aadc"></a> `00a6aadc` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00a6aae0"></a> `00a6aae0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00a6aae4"></a> `00a6aae4` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00a6aae8"></a> `00a6aae8` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00a6aaec"></a> `00a6aaec` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00a6aaf0"></a> `00a6aaf0` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a6aaf4"></a> `00a6aaf4` | `00 38 40 f9` | ldr x0,[x0, #0x70] | `FALL_THROUGH`
<a id="insn-00a6aaf8"></a> `00a6aaf8` | `7f 3a 00 f9` | str xzr,[x19, #0x70] | `FALL_THROUGH`
<a id="insn-00a6aafc"></a> `00a6aafc` | `60 82 00 ad` | stp q0,q0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00a6ab00"></a> `00a6ab00` | `60 82 01 ad` | stp q0,q0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00a6ab04"></a> `00a6ab04` | `60 82 02 ad` | stp q0,q0,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-00a6ab08"></a> `00a6ab08` | `60 02 80 3d` | str q0,[x19] | `FALL_THROUGH`
<a id="insn-00a6ab0c"></a> `00a6ab0c` | `e0 04 00 b4` | cbz x0,0x00a6aba8 | `CONDITIONAL_JUMP`
<a id="insn-00a6ab10"></a> `00a6ab10` | `5e 06 00 94` | bl 0x00a6c488 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ab14"></a> `00a6ab14` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00a6ab18"></a> `00a6ab18` | `80 04 00 b4` | cbz x0,0x00a6aba8 | `CONDITIONAL_JUMP`
<a id="insn-00a6ab1c"></a> `00a6ab1c` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00a6ab20"></a> `00a6ab20` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a6ab24"></a> `00a6ab24` | `70 05 00 94` | bl 0x00a6c0e4 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ab28"></a> `00a6ab28` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00a6ab2c"></a> `00a6ab2c` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a6ab30"></a> `00a6ab30` | `60 02 80 3d` | str q0,[x19] | `FALL_THROUGH`
<a id="insn-00a6ab34"></a> `00a6ab34` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00a6ab38"></a> `00a6ab38` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00a6ab3c"></a> `00a6ab3c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a6ab40"></a> `00a6ab40` | `74 05 00 94` | bl 0x00a6c110 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ab44"></a> `00a6ab44` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00a6ab48"></a> `00a6ab48` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a6ab4c"></a> `00a6ab4c` | `60 82 81 3c` | stur q0,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00a6ab50"></a> `00a6ab50` | `68 16 00 f9` | str x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00a6ab54"></a> `00a6ab54` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00a6ab58"></a> `00a6ab58` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a6ab5c"></a> `00a6ab5c` | `77 05 00 94` | bl 0x00a6c138 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ab60"></a> `00a6ab60` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00a6ab64"></a> `00a6ab64` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a6ab68"></a> `00a6ab68` | `60 0e 80 3d` | str q0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00a6ab6c"></a> `00a6ab6c` | `68 22 00 f9` | str x8,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00a6ab70"></a> `00a6ab70` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00a6ab74"></a> `00a6ab74` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a6ab78"></a> `00a6ab78` | `7a 05 00 94` | bl 0x00a6c160 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ab7c"></a> `00a6ab7c` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00a6ab80"></a> `00a6ab80` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a6ab84"></a> `00a6ab84` | `60 82 84 3c` | stur q0,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00a6ab88"></a> `00a6ab88` | `68 2e 00 f9` | str x8,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00a6ab8c"></a> `00a6ab8c` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00a6ab90"></a> `00a6ab90` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a6ab94"></a> `00a6ab94` | `95 05 00 94` | bl 0x00a6c1e8 | `UNCONDITIONAL_CALL`
<a id="insn-00a6ab98"></a> `00a6ab98` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00a6ab9c"></a> `00a6ab9c` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a6aba0"></a> `00a6aba0` | `60 1a 80 3d` | str q0,[x19, #0x60] | `FALL_THROUGH`
<a id="insn-00a6aba4"></a> `00a6aba4` | `68 3a 00 f9` | str x8,[x19, #0x70] | `FALL_THROUGH`
<a id="insn-00a6aba8"></a> `00a6aba8` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00a6abac"></a> `00a6abac` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a6abb0"></a> `00a6abb0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a6abb4"></a> `00a6abb4` | `81 02 00 54` | b.ne 0x00a6ac04 | `CONDITIONAL_JUMP`
<a id="insn-00a6abb8"></a> `00a6abb8` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a6abbc"></a> `00a6abbc` | `f5 1b 40 f9` | ldr x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a6abc0"></a> `00a6abc0` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a6abc4"></a> `00a6abc4` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00a6abc8"></a> `00a6abc8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a6ac04"></a> `00a6ac04` | `b7 b4 07 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a6aacc`](#insn-00a6aacc) 範囲 `[['00a6aacc', '00a6ab0f']]`
  - `CONDITIONAL_JUMP` [`00a6ab0c`](#insn-00a6ab0c) → [`00a6aba8`](#insn-00a6aba8)
  - `FALL_THROUGH` [`00a6ab0c`](#insn-00a6ab0c) → [`00a6ab10`](#insn-00a6ab10)
- ブロック [`00a6ab10`](#insn-00a6ab10) 範囲 `[['00a6ab10', '00a6ab1b']]`
  - `CONDITIONAL_JUMP` [`00a6ab18`](#insn-00a6ab18) → [`00a6aba8`](#insn-00a6aba8)
  - `FALL_THROUGH` [`00a6ab18`](#insn-00a6ab18) → [`00a6ab1c`](#insn-00a6ab1c)
- ブロック [`00a6ab1c`](#insn-00a6ab1c) 範囲 `[['00a6ab1c', '00a6aba7']]`
  - `FALL_THROUGH` [`00a6aba4`](#insn-00a6aba4) → [`00a6aba8`](#insn-00a6aba8)
- ブロック [`00a6aba8`](#insn-00a6aba8) 範囲 `[['00a6aba8', '00a6abb7']]`
  - `CONDITIONAL_JUMP` [`00a6abb4`](#insn-00a6abb4) → [`00a6ac04`](#insn-00a6ac04)
  - `FALL_THROUGH` [`00a6abb4`](#insn-00a6abb4) → [`00a6abb8`](#insn-00a6abb8)
- ブロック [`00a6abb8`](#insn-00a6abb8) 範囲 `[['00a6abb8', '00a6abcb']]`
- ブロック [`00a6ac04`](#insn-00a6ac04) 範囲 `[['00a6ac04', '00a6ac07']]`

## 命令位置別の参照

- [`00a6aad0`](#insn-00a6aad0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6aad4`](#insn-00a6aad4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6aad8`](#insn-00a6aad8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6aaf0`](#insn-00a6aaf0) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ab0c`](#insn-00a6ab0c) → [`00a6aba8`](#insn-00a6aba8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ab10`](#insn-00a6ab10) → [`00a6c488`](../00a6c/00a6c488.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a6c488` · 推定シンボル `None` · 推定型 `None`
- [`00a6ab18`](#insn-00a6ab18) → [`00a6aba8`](#insn-00a6aba8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ab24`](#insn-00a6ab24) → [`00a6c0e4`](../00a6c/00a6c0e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a6c0e4` · 推定シンボル `None` · 推定型 `None`
- [`00a6ab28`](#insn-00a6ab28) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ab2c`](#insn-00a6ab2c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ab40`](#insn-00a6ab40) → [`00a6c110`](../00a6c/00a6c110.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a6c110` · 推定シンボル `None` · 推定型 `None`
- [`00a6ab44`](#insn-00a6ab44) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ab48`](#insn-00a6ab48) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ab5c`](#insn-00a6ab5c) → [`00a6c138`](../00a6c/00a6c138.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a6c138` · 推定シンボル `None` · 推定型 `None`
- [`00a6ab60`](#insn-00a6ab60) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ab64`](#insn-00a6ab64) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ab78`](#insn-00a6ab78) → [`00a6c160`](../00a6c/00a6c160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a6c160` · 推定シンボル `None` · 推定型 `None`
- [`00a6ab7c`](#insn-00a6ab7c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ab80`](#insn-00a6ab80) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ab94`](#insn-00a6ab94) → [`00a6c1e8`](../00a6c/00a6c1e8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a6c1e8` · 推定シンボル `None` · 推定型 `None`
- [`00a6ab98`](#insn-00a6ab98) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ab9c`](#insn-00a6ab9c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6abac`](#insn-00a6abac) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6abb4`](#insn-00a6abb4) → [`00a6ac04`](#insn-00a6ac04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6abb8`](#insn-00a6abb8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6abbc`](#insn-00a6abbc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6abc0`](#insn-00a6abc0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6ac04`](#insn-00a6ac04) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a6aad0`](#insn-00a6aad0)

~~~json
{
  "source": "00a6aad0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6aad4`](#insn-00a6aad4)

~~~json
{
  "source": "00a6aad4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6aad8`](#insn-00a6aad8)

~~~json
{
  "source": "00a6aad8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6aaf0`](#insn-00a6aaf0)

~~~json
{
  "source": "00a6aaf0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ab0c`](#insn-00a6ab0c)

~~~json
{
  "source": "00a6ab0c",
  "target": "00a6aba8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ab10`](#insn-00a6ab10)

~~~json
{
  "source": "00a6ab10",
  "target": "00a6c488",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ab18`](#insn-00a6ab18)

~~~json
{
  "source": "00a6ab18",
  "target": "00a6aba8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ab24`](#insn-00a6ab24)

~~~json
{
  "source": "00a6ab24",
  "target": "00a6c0e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ab28`](#insn-00a6ab28)

~~~json
{
  "source": "00a6ab28",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ab2c`](#insn-00a6ab2c)

~~~json
{
  "source": "00a6ab2c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ab40`](#insn-00a6ab40)

~~~json
{
  "source": "00a6ab40",
  "target": "00a6c110",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ab44`](#insn-00a6ab44)

~~~json
{
  "source": "00a6ab44",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ab48`](#insn-00a6ab48)

~~~json
{
  "source": "00a6ab48",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ab5c`](#insn-00a6ab5c)

~~~json
{
  "source": "00a6ab5c",
  "target": "00a6c138",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ab60`](#insn-00a6ab60)

~~~json
{
  "source": "00a6ab60",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ab64`](#insn-00a6ab64)

~~~json
{
  "source": "00a6ab64",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ab78`](#insn-00a6ab78)

~~~json
{
  "source": "00a6ab78",
  "target": "00a6c160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ab7c`](#insn-00a6ab7c)

~~~json
{
  "source": "00a6ab7c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ab80`](#insn-00a6ab80)

~~~json
{
  "source": "00a6ab80",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ab94`](#insn-00a6ab94)

~~~json
{
  "source": "00a6ab94",
  "target": "00a6c1e8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6ab98`](#insn-00a6ab98)

~~~json
{
  "source": "00a6ab98",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ab9c`](#insn-00a6ab9c)

~~~json
{
  "source": "00a6ab9c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6abac`](#insn-00a6abac)

~~~json
{
  "source": "00a6abac",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6abb4`](#insn-00a6abb4)

~~~json
{
  "source": "00a6abb4",
  "target": "00a6ac04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6abb8`](#insn-00a6abb8)

~~~json
{
  "source": "00a6abb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6abbc`](#insn-00a6abbc)

~~~json
{
  "source": "00a6abbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6abc0`](#insn-00a6abc0)

~~~json
{
  "source": "00a6abc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6ac04`](#insn-00a6ac04)

~~~json
{
  "source": "00a6ac04",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
