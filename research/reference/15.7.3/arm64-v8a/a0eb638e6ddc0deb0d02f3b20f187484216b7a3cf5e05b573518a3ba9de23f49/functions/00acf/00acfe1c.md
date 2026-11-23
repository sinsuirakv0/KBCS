# 00acfe1c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00acfd54`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acf/00acfd54.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-08de87e69e43018e25d420b16037dd6c)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00acfe60`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfe60.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0007.md#compare-b2eb5918ebbade3be2088abb60972b5d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acfe1c",
  "name": "FUN_00acfe1c",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8996fe12d166231d0754b7b204f982936d0d42bf80582f2d121530c8ace0eca5",
  "source_text_sha256": "8996fe12d166231d0754b7b204f982936d0d42bf80582f2d121530c8ace0eca5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acfe1c",
        "00acff0b"
      ],
      [
        "00acff50",
        "00acff53"
      ]
    ],
    "bytes_sha256": "9d41dc2b9c76162151b788ebd60165617efe05d56ecb374703803ac9d57d7e7a",
    "instruction_count": 61,
    "instruction_bytes": 244,
    "body_bytes": 244,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00acfae8](../00acf/00acfae8.md)

## 呼び出し先

- [00418fe0](../00418/00418fe0.md)
- [00ad08f4](../00ad0/00ad08f4.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1158 bytes

~~~c

void FUN_00acfe1c(undefined8 param_1,undefined8 param_2,ulong *param_3,undefined8 param_4,
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
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  if ((*param_3 & 1) == 0) {
    uStack_78 = param_3[1];
    local_80 = *param_3;
    local_70 = (void *)param_3[2];
  }
  else {
    FUN_00418fe0(&local_80,param_3[2],param_3[1]);
  }
  uVar2 = local_80;
  uVar3 = uStack_78;
  pvVar4 = local_70;
  if ((local_80 & 1) != 0) {
    FUN_00418fe0(&local_60,local_70,uStack_78);
    uVar2 = local_60;
    uVar3 = uStack_58;
    pvVar4 = local_50;
  }
  local_50 = pvVar4;
  uStack_58 = uVar3;
  local_60 = uVar2;
  FUN_00ad08f4(param_1,param_2,0,&local_60,param_4,param_5);
  if ((local_60 & 1) != 0) {
    _ZdlPv(local_50);
  }
  if ((local_80 & 1) != 0) {
    _ZdlPv(local_70);
  }
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
<a id="insn-00acfe1c"></a> `00acfe1c` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00acfe20"></a> `00acfe20` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acfe24"></a> `00acfe24` | `f7 2b 00 f9` | str x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acfe28"></a> `00acfe28` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acfe2c"></a> `00acfe2c` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acfe30"></a> `00acfe30` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00acfe34"></a> `00acfe34` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acfe38"></a> `00acfe38` | `f3 03 03 2a` | mov w19,w3 | `FALL_THROUGH`
<a id="insn-00acfe3c"></a> `00acfe3c` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00acfe40"></a> `00acfe40` | `e9 16 40 f9` | ldr x9,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00acfe44"></a> `00acfe44` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00acfe48"></a> `00acfe48` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00acfe4c"></a> `00acfe4c` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acfe50"></a> `00acfe50` | `29 00 40 39` | ldrb w9,[x1] | `FALL_THROUGH`
<a id="insn-00acfe54"></a> `00acfe54` | `69 01 00 37` | tbnz w9,#0x0,0x00acfe80 | `CONDITIONAL_JUMP`
<a id="insn-00acfe58"></a> `00acfe58` | `20 00 c0 3d` | ldr q0,[x1] | `FALL_THROUGH`
<a id="insn-00acfe5c"></a> `00acfe5c` | `28 08 40 f9` | ldr x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00acfe60"></a> `00acfe60` | `e0 03 80 3d` | str q0,[sp] | `FALL_THROUGH`
<a id="insn-00acfe64"></a> `00acfe64` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acfe68"></a> `00acfe68` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00acfe6c"></a> `00acfe6c` | `68 01 00 36` | tbz w8,#0x0,0x00acfe98 | `CONDITIONAL_JUMP`
<a id="insn-00acfe70"></a> `00acfe70` | `e2 87 40 a9` | ldp x2,x1,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acfe74"></a> `00acfe74` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00acfe78"></a> `00acfe78` | `5a 24 e5 97` | bl 0x00418fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00acfe7c"></a> `00acfe7c` | `0b 00 00 14` | b 0x00acfea8 | `UNCONDITIONAL_JUMP`
<a id="insn-00acfe80"></a> `00acfe80` | `22 a0 40 a9` | ldp x2,x8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00acfe84"></a> `00acfe84` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00acfe88"></a> `00acfe88` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00acfe8c"></a> `00acfe8c` | `55 24 e5 97` | bl 0x00418fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00acfe90"></a> `00acfe90` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00acfe94"></a> `00acfe94` | `e8 fe 07 37` | tbnz w8,#0x0,0x00acfe70 | `CONDITIONAL_JUMP`
<a id="insn-00acfe98"></a> `00acfe98` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00acfe9c"></a> `00acfe9c` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acfea0"></a> `00acfea0` | `e0 0b 80 3d` | str q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acfea4"></a> `00acfea4` | `e8 1b 00 f9` | str x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acfea8"></a> `00acfea8` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00acfeac"></a> `00acfeac` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00acfeb0"></a> `00acfeb0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00acfeb4"></a> `00acfeb4` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00acfeb8"></a> `00acfeb8` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00acfebc"></a> `00acfebc` | `e4 03 13 2a` | mov w4,w19 | `FALL_THROUGH`
<a id="insn-00acfec0"></a> `00acfec0` | `8d 02 00 94` | bl 0x00ad08f4 | `UNCONDITIONAL_CALL`
<a id="insn-00acfec4"></a> `00acfec4` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acfec8"></a> `00acfec8` | `68 00 00 36` | tbz w8,#0x0,0x00acfed4 | `CONDITIONAL_JUMP`
<a id="insn-00acfecc"></a> `00acfecc` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acfed0"></a> `00acfed0` | `50 2c 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00acfed4"></a> `00acfed4` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00acfed8"></a> `00acfed8` | `68 00 00 36` | tbz w8,#0x0,0x00acfee4 | `CONDITIONAL_JUMP`
<a id="insn-00acfedc"></a> `00acfedc` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acfee0"></a> `00acfee0` | `4c 2c 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00acfee4"></a> `00acfee4` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00acfee8"></a> `00acfee8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acfeec"></a> `00acfeec` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acfef0"></a> `00acfef0` | `01 03 00 54` | b.ne 0x00acff50 | `CONDITIONAL_JUMP`
<a id="insn-00acfef4"></a> `00acfef4` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acfef8"></a> `00acfef8` | `f7 2b 40 f9` | ldr x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acfefc"></a> `00acfefc` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acff00"></a> `00acff00` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acff04"></a> `00acff04` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00acff08"></a> `00acff08` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acff50"></a> `00acff50` | `3c 2c 04 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acfe1c`](#insn-00acfe1c) 範囲 `[['00acfe1c', '00acfe57']]`
  - `CONDITIONAL_JUMP` [`00acfe54`](#insn-00acfe54) → [`00acfe80`](#insn-00acfe80)
  - `FALL_THROUGH` [`00acfe54`](#insn-00acfe54) → [`00acfe58`](#insn-00acfe58)
- ブロック [`00acfe58`](#insn-00acfe58) 範囲 `[['00acfe58', '00acfe6f']]`
  - `CONDITIONAL_JUMP` [`00acfe6c`](#insn-00acfe6c) → [`00acfe98`](#insn-00acfe98)
  - `FALL_THROUGH` [`00acfe6c`](#insn-00acfe6c) → [`00acfe70`](#insn-00acfe70)
- ブロック [`00acfe70`](#insn-00acfe70) 範囲 `[['00acfe70', '00acfe7f']]`
  - `UNCONDITIONAL_JUMP` [`00acfe7c`](#insn-00acfe7c) → [`00acfea8`](#insn-00acfea8)
- ブロック [`00acfe80`](#insn-00acfe80) 範囲 `[['00acfe80', '00acfe97']]`
  - `CONDITIONAL_JUMP` [`00acfe94`](#insn-00acfe94) → [`00acfe70`](#insn-00acfe70)
  - `FALL_THROUGH` [`00acfe94`](#insn-00acfe94) → [`00acfe98`](#insn-00acfe98)
- ブロック [`00acfe98`](#insn-00acfe98) 範囲 `[['00acfe98', '00acfea7']]`
  - `FALL_THROUGH` [`00acfea4`](#insn-00acfea4) → [`00acfea8`](#insn-00acfea8)
- ブロック [`00acfea8`](#insn-00acfea8) 範囲 `[['00acfea8', '00acfecb']]`
  - `CONDITIONAL_JUMP` [`00acfec8`](#insn-00acfec8) → [`00acfed4`](#insn-00acfed4)
  - `FALL_THROUGH` [`00acfec8`](#insn-00acfec8) → [`00acfecc`](#insn-00acfecc)
- ブロック [`00acfecc`](#insn-00acfecc) 範囲 `[['00acfecc', '00acfed3']]`
  - `FALL_THROUGH` [`00acfed0`](#insn-00acfed0) → [`00acfed4`](#insn-00acfed4)
- ブロック [`00acfed4`](#insn-00acfed4) 範囲 `[['00acfed4', '00acfedb']]`
  - `CONDITIONAL_JUMP` [`00acfed8`](#insn-00acfed8) → [`00acfee4`](#insn-00acfee4)
  - `FALL_THROUGH` [`00acfed8`](#insn-00acfed8) → [`00acfedc`](#insn-00acfedc)
- ブロック [`00acfedc`](#insn-00acfedc) 範囲 `[['00acfedc', '00acfee3']]`
  - `FALL_THROUGH` [`00acfee0`](#insn-00acfee0) → [`00acfee4`](#insn-00acfee4)
- ブロック [`00acfee4`](#insn-00acfee4) 範囲 `[['00acfee4', '00acfef3']]`
  - `CONDITIONAL_JUMP` [`00acfef0`](#insn-00acfef0) → [`00acff50`](#insn-00acff50)
  - `FALL_THROUGH` [`00acfef0`](#insn-00acfef0) → [`00acfef4`](#insn-00acfef4)
- ブロック [`00acfef4`](#insn-00acfef4) 範囲 `[['00acfef4', '00acff0b']]`
- ブロック [`00acff50`](#insn-00acff50) 範囲 `[['00acff50', '00acff53']]`

## 命令位置別の参照

- [`00acfe20`](#insn-00acfe20) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe24`](#insn-00acfe24) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe28`](#insn-00acfe28) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe2c`](#insn-00acfe2c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe4c`](#insn-00acfe4c) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe54`](#insn-00acfe54) → [`00acfe80`](#insn-00acfe80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe60`](#insn-00acfe60) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe64`](#insn-00acfe64) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe68`](#insn-00acfe68) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe6c`](#insn-00acfe6c) → [`00acfe98`](#insn-00acfe98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe70`](#insn-00acfe70) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe78`](#insn-00acfe78) → [`00418fe0`](../00418/00418fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418fe0` · 推定シンボル `None` · 推定型 `None`
- [`00acfe7c`](#insn-00acfe7c) → [`00acfea8`](#insn-00acfea8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe8c`](#insn-00acfe8c) → [`00418fe0`](../00418/00418fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418fe0` · 推定シンボル `None` · 推定型 `None`
- [`00acfe90`](#insn-00acfe90) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe94`](#insn-00acfe94) → [`00acfe70`](#insn-00acfe70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe98`](#insn-00acfe98) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe9c`](#insn-00acfe9c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfea0`](#insn-00acfea0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfea4`](#insn-00acfea4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfec0`](#insn-00acfec0) → [`00ad08f4`](../00ad0/00ad08f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ad08f4` · 推定シンボル `None` · 推定型 `None`
- [`00acfec4`](#insn-00acfec4) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfec8`](#insn-00acfec8) → [`00acfed4`](#insn-00acfed4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfecc`](#insn-00acfecc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfed0`](#insn-00acfed0) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00acfed4`](#insn-00acfed4) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfed8`](#insn-00acfed8) → [`00acfee4`](#insn-00acfee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfedc`](#insn-00acfedc) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfee0`](#insn-00acfee0) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00acfee8`](#insn-00acfee8) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfef0`](#insn-00acfef0) → [`00acff50`](#insn-00acff50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfef4`](#insn-00acfef4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfef8`](#insn-00acfef8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfefc`](#insn-00acfefc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff00`](#insn-00acff00) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff50`](#insn-00acff50) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acfe20`](#insn-00acfe20)

~~~json
{
  "source": "00acfe20",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe24`](#insn-00acfe24)

~~~json
{
  "source": "00acfe24",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe28`](#insn-00acfe28)

~~~json
{
  "source": "00acfe28",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe2c`](#insn-00acfe2c)

~~~json
{
  "source": "00acfe2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe4c`](#insn-00acfe4c)

~~~json
{
  "source": "00acfe4c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe54`](#insn-00acfe54)

~~~json
{
  "source": "00acfe54",
  "target": "00acfe80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe60`](#insn-00acfe60)

~~~json
{
  "source": "00acfe60",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe64`](#insn-00acfe64)

~~~json
{
  "source": "00acfe64",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe68`](#insn-00acfe68)

~~~json
{
  "source": "00acfe68",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe6c`](#insn-00acfe6c)

~~~json
{
  "source": "00acfe6c",
  "target": "00acfe98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe70`](#insn-00acfe70)

~~~json
{
  "source": "00acfe70",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe78`](#insn-00acfe78)

~~~json
{
  "source": "00acfe78",
  "target": "00418fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfe7c`](#insn-00acfe7c)

~~~json
{
  "source": "00acfe7c",
  "target": "00acfea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe8c`](#insn-00acfe8c)

~~~json
{
  "source": "00acfe8c",
  "target": "00418fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfe90`](#insn-00acfe90)

~~~json
{
  "source": "00acfe90",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe94`](#insn-00acfe94)

~~~json
{
  "source": "00acfe94",
  "target": "00acfe70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe98`](#insn-00acfe98)

~~~json
{
  "source": "00acfe98",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe9c`](#insn-00acfe9c)

~~~json
{
  "source": "00acfe9c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfea0`](#insn-00acfea0)

~~~json
{
  "source": "00acfea0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfea4`](#insn-00acfea4)

~~~json
{
  "source": "00acfea4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfec0`](#insn-00acfec0)

~~~json
{
  "source": "00acfec0",
  "target": "00ad08f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfec4`](#insn-00acfec4)

~~~json
{
  "source": "00acfec4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfec8`](#insn-00acfec8)

~~~json
{
  "source": "00acfec8",
  "target": "00acfed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfecc`](#insn-00acfecc)

~~~json
{
  "source": "00acfecc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfed0`](#insn-00acfed0)

~~~json
{
  "source": "00acfed0",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfed4`](#insn-00acfed4)

~~~json
{
  "source": "00acfed4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfed8`](#insn-00acfed8)

~~~json
{
  "source": "00acfed8",
  "target": "00acfee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfedc`](#insn-00acfedc)

~~~json
{
  "source": "00acfedc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfee0`](#insn-00acfee0)

~~~json
{
  "source": "00acfee0",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfee8`](#insn-00acfee8)

~~~json
{
  "source": "00acfee8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfef0`](#insn-00acfef0)

~~~json
{
  "source": "00acfef0",
  "target": "00acff50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfef4`](#insn-00acfef4)

~~~json
{
  "source": "00acfef4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfef8`](#insn-00acfef8)

~~~json
{
  "source": "00acfef8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfefc`](#insn-00acfefc)

~~~json
{
  "source": "00acfefc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff00`](#insn-00acff00)

~~~json
{
  "source": "00acff00",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff50`](#insn-00acff50)

~~~json
{
  "source": "00acff50",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
