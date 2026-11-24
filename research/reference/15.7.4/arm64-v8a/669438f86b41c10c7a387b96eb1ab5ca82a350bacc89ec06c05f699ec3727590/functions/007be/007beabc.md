# 007beabc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `007beabc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007be/007beabc.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/machine_only_observed-0025.md#compare-e1a4aae83773652359ce8bf33477fef8)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `007f0c58`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0c58.md) · 移動量 `+0x3219c`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0007.md#compare-6e9c0d011ac1b1659723d2c5505064e2)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007beabc",
  "name": "FUN_007beabc",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0944b1ceb76945adc1bdb2944f105b8b0acf00249c2ca27bc1bffb49d46f6f5a",
  "source_text_sha256": "0944b1ceb76945adc1bdb2944f105b8b0acf00249c2ca27bc1bffb49d46f6f5a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007beabc",
        "007bebaf"
      ],
      [
        "007bebf4",
        "007bebf7"
      ]
    ],
    "bytes_sha256": "cf4a70cf928173bc338c37100b96270f722224616af2d50996f55bac0150a9b3",
    "instruction_count": 62,
    "instruction_bytes": 248,
    "body_bytes": 248,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0078adc4](../0078a/0078adc4.md)

## 呼び出し先

- [00418fe0](../00418/00418fe0.md)
- [007bebf8](../007be/007bebf8.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1116 bytes

~~~c

void FUN_007beabc(undefined8 param_1,undefined8 param_2,undefined4 param_3,undefined4 param_4,
                 ulong *param_5,ulong *param_6)

{
  byte bVar1;
  long lVar2;
  ulong local_80;
  ulong uStack_78;
  void *local_70;
  ulong local_60;
  ulong uStack_58;
  void *local_50;
  long local_48;
  
  lVar2 = tpidr_el0;
  local_48 = *(long *)(lVar2 + 0x28);
  if ((*param_5 & 1) == 0) {
    uStack_58 = param_5[1];
    local_60 = *param_5;
    local_50 = (void *)param_5[2];
    bVar1 = (byte)*param_6;
  }
  else {
    FUN_00418fe0(&local_60,param_5[2],param_5[1]);
    bVar1 = (byte)*param_6;
  }
  if ((bVar1 & 1) == 0) {
    uStack_78 = param_6[1];
    local_80 = *param_6;
    local_70 = (void *)param_6[2];
  }
  else {
    FUN_00418fe0(&local_80,param_6[2],param_6[1]);
  }
  FUN_007bebf8(param_1,param_2,0,param_3,param_4,&local_60,&local_80);
  if ((local_80 & 1) != 0) {
    _ZdlPv(local_70);
  }
  if ((local_60 & 1) != 0) {
    _ZdlPv(local_50);
  }
  if (*(long *)(lVar2 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007beabc"></a> `007beabc` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-007beac0"></a> `007beac0` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-007beac4"></a> `007beac4` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007beac8"></a> `007beac8` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-007beacc"></a> `007beacc` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-007bead0"></a> `007bead0` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-007bead4"></a> `007bead4` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-007bead8"></a> `007bead8` | `f7 03 04 aa` | mov x23,x4 | `FALL_THROUGH`
<a id="insn-007beadc"></a> `007beadc` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-007beae0"></a> `007beae0` | `09 17 40 f9` | ldr x9,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-007beae4"></a> `007beae4` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-007beae8"></a> `007beae8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-007beaec"></a> `007beaec` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-007beaf0"></a> `007beaf0` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-007beaf4"></a> `007beaf4` | `69 00 40 39` | ldrb w9,[x3] | `FALL_THROUGH`
<a id="insn-007beaf8"></a> `007beaf8` | `69 01 00 37` | tbnz w9,#0x0,0x007beb24 | `CONDITIONAL_JUMP`
<a id="insn-007beafc"></a> `007beafc` | `60 00 c0 3d` | ldr q0,[x3] | `FALL_THROUGH`
<a id="insn-007beb00"></a> `007beb00` | `68 08 40 f9` | ldr x8,[x3, #0x10] | `FALL_THROUGH`
<a id="insn-007beb04"></a> `007beb04` | `e0 0b 80 3d` | str q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007beb08"></a> `007beb08` | `e8 1b 00 f9` | str x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007beb0c"></a> `007beb0c` | `e8 02 40 39` | ldrb w8,[x23] | `FALL_THROUGH`
<a id="insn-007beb10"></a> `007beb10` | `48 01 00 36` | tbz w8,#0x0,0x007beb38 | `CONDITIONAL_JUMP`
<a id="insn-007beb14"></a> `007beb14` | `e2 86 40 a9` | ldp x2,x1,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-007beb18"></a> `007beb18` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-007beb1c"></a> `007beb1c` | `31 69 f1 97` | bl 0x00418fe0 | `UNCONDITIONAL_CALL`
<a id="insn-007beb20"></a> `007beb20` | `0a 00 00 14` | b 0x007beb48 | `UNCONDITIONAL_JUMP`
<a id="insn-007beb24"></a> `007beb24` | `62 84 40 a9` | ldp x2,x1,[x3, #0x8] | `FALL_THROUGH`
<a id="insn-007beb28"></a> `007beb28` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-007beb2c"></a> `007beb2c` | `2d 69 f1 97` | bl 0x00418fe0 | `UNCONDITIONAL_CALL`
<a id="insn-007beb30"></a> `007beb30` | `e8 02 40 39` | ldrb w8,[x23] | `FALL_THROUGH`
<a id="insn-007beb34"></a> `007beb34` | `08 ff 07 37` | tbnz w8,#0x0,0x007beb14 | `CONDITIONAL_JUMP`
<a id="insn-007beb38"></a> `007beb38` | `e0 02 c0 3d` | ldr q0,[x23] | `FALL_THROUGH`
<a id="insn-007beb3c"></a> `007beb3c` | `e8 0a 40 f9` | ldr x8,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-007beb40"></a> `007beb40` | `e0 03 80 3d` | str q0,[sp] | `FALL_THROUGH`
<a id="insn-007beb44"></a> `007beb44` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007beb48"></a> `007beb48` | `e4 83 00 91` | add x4,sp,#0x20 | `FALL_THROUGH`
<a id="insn-007beb4c"></a> `007beb4c` | `e5 03 00 91` | mov x5,sp | `FALL_THROUGH`
<a id="insn-007beb50"></a> `007beb50` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-007beb54"></a> `007beb54` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-007beb58"></a> `007beb58` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-007beb5c"></a> `007beb5c` | `e2 03 14 2a` | mov w2,w20 | `FALL_THROUGH`
<a id="insn-007beb60"></a> `007beb60` | `e3 03 13 2a` | mov w3,w19 | `FALL_THROUGH`
<a id="insn-007beb64"></a> `007beb64` | `25 00 00 94` | bl 0x007bebf8 | `UNCONDITIONAL_CALL`
<a id="insn-007beb68"></a> `007beb68` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-007beb6c"></a> `007beb6c` | `68 00 00 36` | tbz w8,#0x0,0x007beb78 | `CONDITIONAL_JUMP`
<a id="insn-007beb70"></a> `007beb70` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007beb74"></a> `007beb74` | `3b 71 10 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-007beb78"></a> `007beb78` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007beb7c"></a> `007beb7c` | `68 00 00 36` | tbz w8,#0x0,0x007beb88 | `CONDITIONAL_JUMP`
<a id="insn-007beb80"></a> `007beb80` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007beb84"></a> `007beb84` | `37 71 10 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-007beb88"></a> `007beb88` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-007beb8c"></a> `007beb8c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-007beb90"></a> `007beb90` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-007beb94"></a> `007beb94` | `01 03 00 54` | b.ne 0x007bebf4 | `CONDITIONAL_JUMP`
<a id="insn-007beb98"></a> `007beb98` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-007beb9c"></a> `007beb9c` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-007beba0"></a> `007beba0` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007beba4"></a> `007beba4` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-007beba8"></a> `007beba8` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-007bebac"></a> `007bebac` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-007bebf4"></a> `007bebf4` | `27 71 10 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007beabc`](#insn-007beabc) 範囲 `[['007beabc', '007beafb']]`
  - `CONDITIONAL_JUMP` [`007beaf8`](#insn-007beaf8) → [`007beb24`](#insn-007beb24)
  - `FALL_THROUGH` [`007beaf8`](#insn-007beaf8) → [`007beafc`](#insn-007beafc)
- ブロック [`007beafc`](#insn-007beafc) 範囲 `[['007beafc', '007beb13']]`
  - `CONDITIONAL_JUMP` [`007beb10`](#insn-007beb10) → [`007beb38`](#insn-007beb38)
  - `FALL_THROUGH` [`007beb10`](#insn-007beb10) → [`007beb14`](#insn-007beb14)
- ブロック [`007beb14`](#insn-007beb14) 範囲 `[['007beb14', '007beb23']]`
  - `UNCONDITIONAL_JUMP` [`007beb20`](#insn-007beb20) → [`007beb48`](#insn-007beb48)
- ブロック [`007beb24`](#insn-007beb24) 範囲 `[['007beb24', '007beb37']]`
  - `CONDITIONAL_JUMP` [`007beb34`](#insn-007beb34) → [`007beb14`](#insn-007beb14)
  - `FALL_THROUGH` [`007beb34`](#insn-007beb34) → [`007beb38`](#insn-007beb38)
- ブロック [`007beb38`](#insn-007beb38) 範囲 `[['007beb38', '007beb47']]`
  - `FALL_THROUGH` [`007beb44`](#insn-007beb44) → [`007beb48`](#insn-007beb48)
- ブロック [`007beb48`](#insn-007beb48) 範囲 `[['007beb48', '007beb6f']]`
  - `CONDITIONAL_JUMP` [`007beb6c`](#insn-007beb6c) → [`007beb78`](#insn-007beb78)
  - `FALL_THROUGH` [`007beb6c`](#insn-007beb6c) → [`007beb70`](#insn-007beb70)
- ブロック [`007beb70`](#insn-007beb70) 範囲 `[['007beb70', '007beb77']]`
  - `FALL_THROUGH` [`007beb74`](#insn-007beb74) → [`007beb78`](#insn-007beb78)
- ブロック [`007beb78`](#insn-007beb78) 範囲 `[['007beb78', '007beb7f']]`
  - `CONDITIONAL_JUMP` [`007beb7c`](#insn-007beb7c) → [`007beb88`](#insn-007beb88)
  - `FALL_THROUGH` [`007beb7c`](#insn-007beb7c) → [`007beb80`](#insn-007beb80)
- ブロック [`007beb80`](#insn-007beb80) 範囲 `[['007beb80', '007beb87']]`
  - `FALL_THROUGH` [`007beb84`](#insn-007beb84) → [`007beb88`](#insn-007beb88)
- ブロック [`007beb88`](#insn-007beb88) 範囲 `[['007beb88', '007beb97']]`
  - `CONDITIONAL_JUMP` [`007beb94`](#insn-007beb94) → [`007bebf4`](#insn-007bebf4)
  - `FALL_THROUGH` [`007beb94`](#insn-007beb94) → [`007beb98`](#insn-007beb98)
- ブロック [`007beb98`](#insn-007beb98) 範囲 `[['007beb98', '007bebaf']]`
- ブロック [`007bebf4`](#insn-007bebf4) 範囲 `[['007bebf4', '007bebf7']]`

## 命令位置別の参照

- [`007beac0`](#insn-007beac0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007beac4`](#insn-007beac4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007beac8`](#insn-007beac8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007beacc`](#insn-007beacc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007beaf0`](#insn-007beaf0) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007beaf8`](#insn-007beaf8) → [`007beb24`](#insn-007beb24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007beb04`](#insn-007beb04) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007beb08`](#insn-007beb08) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007beb10`](#insn-007beb10) → [`007beb38`](#insn-007beb38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007beb1c`](#insn-007beb1c) → [`00418fe0`](../00418/00418fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418fe0` · 推定シンボル `None` · 推定型 `None`
- [`007beb20`](#insn-007beb20) → [`007beb48`](#insn-007beb48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007beb2c`](#insn-007beb2c) → [`00418fe0`](../00418/00418fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418fe0` · 推定シンボル `None` · 推定型 `None`
- [`007beb34`](#insn-007beb34) → [`007beb14`](#insn-007beb14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007beb40`](#insn-007beb40) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007beb44`](#insn-007beb44) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007beb64`](#insn-007beb64) → [`007bebf8`](007bebf8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007bebf8` · 推定シンボル `None` · 推定型 `None`
- [`007beb68`](#insn-007beb68) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007beb6c`](#insn-007beb6c) → [`007beb78`](#insn-007beb78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007beb70`](#insn-007beb70) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007beb74`](#insn-007beb74) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`007beb78`](#insn-007beb78) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007beb7c`](#insn-007beb7c) → [`007beb88`](#insn-007beb88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007beb80`](#insn-007beb80) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007beb84`](#insn-007beb84) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`007beb8c`](#insn-007beb8c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007beb94`](#insn-007beb94) → [`007bebf4`](#insn-007bebf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007beb98`](#insn-007beb98) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007beb9c`](#insn-007beb9c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007beba0`](#insn-007beba0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007beba4`](#insn-007beba4) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bebf4`](#insn-007bebf4) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007beac0`](#insn-007beac0)

~~~json
{
  "source": "007beac0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007beac4`](#insn-007beac4)

~~~json
{
  "source": "007beac4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007beac8`](#insn-007beac8)

~~~json
{
  "source": "007beac8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007beacc`](#insn-007beacc)

~~~json
{
  "source": "007beacc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007beaf0`](#insn-007beaf0)

~~~json
{
  "source": "007beaf0",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007beaf8`](#insn-007beaf8)

~~~json
{
  "source": "007beaf8",
  "target": "007beb24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007beb04`](#insn-007beb04)

~~~json
{
  "source": "007beb04",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007beb08`](#insn-007beb08)

~~~json
{
  "source": "007beb08",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007beb10`](#insn-007beb10)

~~~json
{
  "source": "007beb10",
  "target": "007beb38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007beb1c`](#insn-007beb1c)

~~~json
{
  "source": "007beb1c",
  "target": "00418fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007beb20`](#insn-007beb20)

~~~json
{
  "source": "007beb20",
  "target": "007beb48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007beb2c`](#insn-007beb2c)

~~~json
{
  "source": "007beb2c",
  "target": "00418fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007beb34`](#insn-007beb34)

~~~json
{
  "source": "007beb34",
  "target": "007beb14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007beb40`](#insn-007beb40)

~~~json
{
  "source": "007beb40",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007beb44`](#insn-007beb44)

~~~json
{
  "source": "007beb44",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007beb64`](#insn-007beb64)

~~~json
{
  "source": "007beb64",
  "target": "007bebf8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007beb68`](#insn-007beb68)

~~~json
{
  "source": "007beb68",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007beb6c`](#insn-007beb6c)

~~~json
{
  "source": "007beb6c",
  "target": "007beb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007beb70`](#insn-007beb70)

~~~json
{
  "source": "007beb70",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007beb74`](#insn-007beb74)

~~~json
{
  "source": "007beb74",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007beb78`](#insn-007beb78)

~~~json
{
  "source": "007beb78",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007beb7c`](#insn-007beb7c)

~~~json
{
  "source": "007beb7c",
  "target": "007beb88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007beb80`](#insn-007beb80)

~~~json
{
  "source": "007beb80",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007beb84`](#insn-007beb84)

~~~json
{
  "source": "007beb84",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007beb8c`](#insn-007beb8c)

~~~json
{
  "source": "007beb8c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007beb94`](#insn-007beb94)

~~~json
{
  "source": "007beb94",
  "target": "007bebf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007beb98`](#insn-007beb98)

~~~json
{
  "source": "007beb98",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007beb9c`](#insn-007beb9c)

~~~json
{
  "source": "007beb9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007beba0`](#insn-007beba0)

~~~json
{
  "source": "007beba0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007beba4`](#insn-007beba4)

~~~json
{
  "source": "007beba4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bebf4`](#insn-007bebf4)

~~~json
{
  "source": "007bebf4",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
