# 004cadbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `004cadbc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ca/004cadbc.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0009.md#compare-90b7aedafbd67d1210397a1b67a583cd)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `004edc54`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edc54.md) · 移動量 `+0x22e98`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0010.md#compare-c37ee5c0dc3c7ab6e350ae541a494c22)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004cadbc",
  "name": "_ZN5Botan5PKCS88load_keyERNS_10DataSourceERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7f03daa5e3070a4ee5206e74777bde065328da6c7e488b1c394f7ee5cf3cbeef",
  "source_text_sha256": "7f03daa5e3070a4ee5206e74777bde065328da6c7e488b1c394f7ee5cf3cbeef",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004cadbc",
        "004caeab"
      ],
      [
        "004caf00",
        "004caf03"
      ]
    ],
    "bytes_sha256": "06241c85d1e110312522cf7055033a7368aa5358a793d0dd903c49ee9e8c1c54",
    "instruction_count": 61,
    "instruction_bytes": 244,
    "body_bytes": 244,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdc7e0](../00bdc/00bdc7e0.md)

## 呼び出し先

- [00418fe0](../00418/00418fe0.md)
- [004c9e38](../004c9/004c9e38.md)
- [005229d4](../00522/005229d4.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1174 bytes

~~~c

void _ZN5Botan5PKCS88load_keyERNS_10DataSourceERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE
               (undefined8 param_1,undefined8 param_2,ulong *param_3)

{
  long lVar1;
  long *plVar2;
  ulong local_90;
  ulong uStack_88;
  void *local_80;
  undefined1 auStack_70 [32];
  long *local_50;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  if ((*param_3 & 1) == 0) {
    uStack_88 = param_3[1];
    local_90 = *param_3;
    local_80 = (void *)param_3[2];
  }
  else {
    FUN_00418fe0(&local_90,param_3[2],param_3[1]);
  }
  local_50 = (long *)0x0;
  plVar2 = (long *)_Znwm(0x20);
  *plVar2 = (long)&PTR_FUN_00bed560;
  if ((local_90 & 1) == 0) {
    plVar2[2] = uStack_88;
    plVar2[1] = local_90;
    plVar2[3] = (long)local_80;
  }
  else {
    FUN_00418fe0(plVar2 + 1,local_80,uStack_88);
  }
  local_50 = plVar2;
  FUN_004c9e38(param_1,param_2,auStack_70,1);
  (**(code **)(*plVar2 + 0x28))(plVar2);
  if ((local_90 & 1) != 0) {
    _ZdlPv(local_80);
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
<a id="insn-004cadbc"></a> `004cadbc` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-004cadc0"></a> `004cadc0` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004cadc4"></a> `004cadc4` | `f6 57 07 a9` | stp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004cadc8"></a> `004cadc8` | `f4 4f 08 a9` | stp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-004cadcc"></a> `004cadcc` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-004cadd0"></a> `004cadd0` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004cadd4"></a> `004cadd4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004cadd8"></a> `004cadd8` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-004caddc"></a> `004caddc` | `c9 16 40 f9` | ldr x9,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-004cade0"></a> `004cade0` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004cade4"></a> `004cade4` | `29 00 40 39` | ldrb w9,[x1] | `FALL_THROUGH`
<a id="insn-004cade8"></a> `004cade8` | `c9 00 00 37` | tbnz w9,#0x0,0x004cae00 | `CONDITIONAL_JUMP`
<a id="insn-004cadec"></a> `004cadec` | `20 00 c0 3d` | ldr q0,[x1] | `FALL_THROUGH`
<a id="insn-004cadf0"></a> `004cadf0` | `28 08 40 f9` | ldr x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-004cadf4"></a> `004cadf4` | `e0 03 80 3d` | str q0,[sp] | `FALL_THROUGH`
<a id="insn-004cadf8"></a> `004cadf8` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004cadfc"></a> `004cadfc` | `05 00 00 14` | b 0x004cae10 | `UNCONDITIONAL_JUMP`
<a id="insn-004cae00"></a> `004cae00` | `22 a0 40 a9` | ldp x2,x8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-004cae04"></a> `004cae04` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004cae08"></a> `004cae08` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-004cae0c"></a> `004cae0c` | `75 38 fd 97` | bl 0x00418fe0 | `UNCONDITIONAL_CALL`
<a id="insn-004cae10"></a> `004cae10` | `ff 23 00 f9` | str xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004cae14"></a> `004cae14` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-004cae18"></a> `004cae18` | `8a 40 1c 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-004cae1c"></a> `004cae1c` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-004cae20"></a> `004cae20` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-004cae24"></a> `004cae24` | `09 39 00 f0` | adrp x9,0xbed000 | `FALL_THROUGH`
<a id="insn-004cae28"></a> `004cae28` | `29 81 15 91` | add x9,x9,#0x560 | `FALL_THROUGH`
<a id="insn-004cae2c"></a> `004cae2c` | `09 84 00 f8` | str x9,[x0], #0x8 | `FALL_THROUGH`
<a id="insn-004cae30"></a> `004cae30` | `c8 00 00 37` | tbnz w8,#0x0,0x004cae48 | `CONDITIONAL_JUMP`
<a id="insn-004cae34"></a> `004cae34` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-004cae38"></a> `004cae38` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004cae3c"></a> `004cae3c` | `00 00 80 3d` | str q0,[x0] | `FALL_THROUGH`
<a id="insn-004cae40"></a> `004cae40` | `08 08 00 f9` | str x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004cae44"></a> `004cae44` | `03 00 00 14` | b 0x004cae50 | `UNCONDITIONAL_JUMP`
<a id="insn-004cae48"></a> `004cae48` | `e2 87 40 a9` | ldp x2,x1,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004cae4c"></a> `004cae4c` | `65 38 fd 97` | bl 0x00418fe0 | `UNCONDITIONAL_CALL`
<a id="insn-004cae50"></a> `004cae50` | `f5 23 00 f9` | str x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004cae54"></a> `004cae54` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004cae58"></a> `004cae58` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-004cae5c"></a> `004cae5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004cae60"></a> `004cae60` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-004cae64"></a> `004cae64` | `f5 fb ff 97` | bl 0x004c9e38 | `UNCONDITIONAL_CALL`
<a id="insn-004cae68"></a> `004cae68` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-004cae6c"></a> `004cae6c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-004cae70"></a> `004cae70` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004cae74"></a> `004cae74` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004cae78"></a> `004cae78` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-004cae7c"></a> `004cae7c` | `68 00 00 36` | tbz w8,#0x0,0x004cae88 | `CONDITIONAL_JUMP`
<a id="insn-004cae80"></a> `004cae80` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004cae84"></a> `004cae84` | `77 40 1c 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-004cae88"></a> `004cae88` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-004cae8c"></a> `004cae8c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004cae90"></a> `004cae90` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004cae94"></a> `004cae94` | `61 03 00 54` | b.ne 0x004caf00 | `CONDITIONAL_JUMP`
<a id="insn-004cae98"></a> `004cae98` | `f4 4f 48 a9` | ldp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-004cae9c"></a> `004cae9c` | `f6 57 47 a9` | ldp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004caea0"></a> `004caea0` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004caea4"></a> `004caea4` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-004caea8"></a> `004caea8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004caf00"></a> `004caf00` | `64 40 1c 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004cadbc`](#insn-004cadbc) 範囲 `[['004cadbc', '004cadeb']]`
  - `CONDITIONAL_JUMP` [`004cade8`](#insn-004cade8) → [`004cae00`](#insn-004cae00)
  - `FALL_THROUGH` [`004cade8`](#insn-004cade8) → [`004cadec`](#insn-004cadec)
- ブロック [`004cadec`](#insn-004cadec) 範囲 `[['004cadec', '004cadff']]`
  - `UNCONDITIONAL_JUMP` [`004cadfc`](#insn-004cadfc) → [`004cae10`](#insn-004cae10)
- ブロック [`004cae00`](#insn-004cae00) 範囲 `[['004cae00', '004cae0f']]`
  - `FALL_THROUGH` [`004cae0c`](#insn-004cae0c) → [`004cae10`](#insn-004cae10)
- ブロック [`004cae10`](#insn-004cae10) 範囲 `[['004cae10', '004cae33']]`
  - `CONDITIONAL_JUMP` [`004cae30`](#insn-004cae30) → [`004cae48`](#insn-004cae48)
  - `FALL_THROUGH` [`004cae30`](#insn-004cae30) → [`004cae34`](#insn-004cae34)
- ブロック [`004cae34`](#insn-004cae34) 範囲 `[['004cae34', '004cae47']]`
  - `UNCONDITIONAL_JUMP` [`004cae44`](#insn-004cae44) → [`004cae50`](#insn-004cae50)
- ブロック [`004cae48`](#insn-004cae48) 範囲 `[['004cae48', '004cae4f']]`
  - `FALL_THROUGH` [`004cae4c`](#insn-004cae4c) → [`004cae50`](#insn-004cae50)
- ブロック [`004cae50`](#insn-004cae50) 範囲 `[['004cae50', '004cae7f']]`
  - `CONDITIONAL_JUMP` [`004cae7c`](#insn-004cae7c) → [`004cae88`](#insn-004cae88)
  - `FALL_THROUGH` [`004cae7c`](#insn-004cae7c) → [`004cae80`](#insn-004cae80)
- ブロック [`004cae80`](#insn-004cae80) 範囲 `[['004cae80', '004cae87']]`
  - `FALL_THROUGH` [`004cae84`](#insn-004cae84) → [`004cae88`](#insn-004cae88)
- ブロック [`004cae88`](#insn-004cae88) 範囲 `[['004cae88', '004cae97']]`
  - `CONDITIONAL_JUMP` [`004cae94`](#insn-004cae94) → [`004caf00`](#insn-004caf00)
  - `FALL_THROUGH` [`004cae94`](#insn-004cae94) → [`004cae98`](#insn-004cae98)
- ブロック [`004cae98`](#insn-004cae98) 範囲 `[['004cae98', '004caeab']]`
- ブロック [`004caf00`](#insn-004caf00) 範囲 `[['004caf00', '004caf03']]`

## 命令位置別の参照

- [`004cadc0`](#insn-004cadc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cadc4`](#insn-004cadc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cadc8`](#insn-004cadc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cade0`](#insn-004cade0) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cade8`](#insn-004cade8) → [`004cae00`](#insn-004cae00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cadf4`](#insn-004cadf4) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cadf8`](#insn-004cadf8) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cadfc`](#insn-004cadfc) → [`004cae10`](#insn-004cae10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cae0c`](#insn-004cae0c) → [`00418fe0`](../00418/00418fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418fe0` · 推定シンボル `None` · 推定型 `None`
- [`004cae10`](#insn-004cae10) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cae18`](#insn-004cae18) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`004cae1c`](#insn-004cae1c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cae2c`](#insn-004cae2c) → `00bed560`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`004cae30`](#insn-004cae30) → [`004cae48`](#insn-004cae48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cae34`](#insn-004cae34) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cae38`](#insn-004cae38) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cae44`](#insn-004cae44) → [`004cae50`](#insn-004cae50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cae48`](#insn-004cae48) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cae4c`](#insn-004cae4c) → [`00418fe0`](../00418/00418fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418fe0` · 推定シンボル `None` · 推定型 `None`
- [`004cae50`](#insn-004cae50) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cae64`](#insn-004cae64) → [`004c9e38`](../004c9/004c9e38.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004c9e38` · 推定シンボル `None` · 推定型 `None`
- [`004cae70`](#insn-004cae70) → `00bed588`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`004cae74`](#insn-004cae74) → [`005229d4`](../00522/005229d4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `005229d4` · 推定シンボル `None` · 推定型 `None`
- [`004cae78`](#insn-004cae78) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cae7c`](#insn-004cae7c) → [`004cae88`](#insn-004cae88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cae80`](#insn-004cae80) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cae84`](#insn-004cae84) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`004cae8c`](#insn-004cae8c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cae94`](#insn-004cae94) → [`004caf00`](#insn-004caf00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cae98`](#insn-004cae98) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cae9c`](#insn-004cae9c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004caea0`](#insn-004caea0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004caf00`](#insn-004caf00) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004cadc0`](#insn-004cadc0)

~~~json
{
  "source": "004cadc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cadc4`](#insn-004cadc4)

~~~json
{
  "source": "004cadc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cadc8`](#insn-004cadc8)

~~~json
{
  "source": "004cadc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cade0`](#insn-004cade0)

~~~json
{
  "source": "004cade0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cade8`](#insn-004cade8)

~~~json
{
  "source": "004cade8",
  "target": "004cae00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cadf4`](#insn-004cadf4)

~~~json
{
  "source": "004cadf4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cadf8`](#insn-004cadf8)

~~~json
{
  "source": "004cadf8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cadfc`](#insn-004cadfc)

~~~json
{
  "source": "004cadfc",
  "target": "004cae10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cae0c`](#insn-004cae0c)

~~~json
{
  "source": "004cae0c",
  "target": "00418fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cae10`](#insn-004cae10)

~~~json
{
  "source": "004cae10",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cae18`](#insn-004cae18)

~~~json
{
  "source": "004cae18",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cae1c`](#insn-004cae1c)

~~~json
{
  "source": "004cae1c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cae2c`](#insn-004cae2c)

~~~json
{
  "source": "004cae2c",
  "target": "00bed560",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00bed560",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004cae30`](#insn-004cae30)

~~~json
{
  "source": "004cae30",
  "target": "004cae48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cae34`](#insn-004cae34)

~~~json
{
  "source": "004cae34",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cae38`](#insn-004cae38)

~~~json
{
  "source": "004cae38",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cae44`](#insn-004cae44)

~~~json
{
  "source": "004cae44",
  "target": "004cae50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cae48`](#insn-004cae48)

~~~json
{
  "source": "004cae48",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cae4c`](#insn-004cae4c)

~~~json
{
  "source": "004cae4c",
  "target": "00418fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cae50`](#insn-004cae50)

~~~json
{
  "source": "004cae50",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cae64`](#insn-004cae64)

~~~json
{
  "source": "004cae64",
  "target": "004c9e38",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cae70`](#insn-004cae70)

~~~json
{
  "source": "004cae70",
  "target": "00bed588",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00bed588",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004cae74`](#insn-004cae74)

~~~json
{
  "source": "004cae74",
  "target": "005229d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cae78`](#insn-004cae78)

~~~json
{
  "source": "004cae78",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cae7c`](#insn-004cae7c)

~~~json
{
  "source": "004cae7c",
  "target": "004cae88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cae80`](#insn-004cae80)

~~~json
{
  "source": "004cae80",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cae84`](#insn-004cae84)

~~~json
{
  "source": "004cae84",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cae8c`](#insn-004cae8c)

~~~json
{
  "source": "004cae8c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cae94`](#insn-004cae94)

~~~json
{
  "source": "004cae94",
  "target": "004caf00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cae98`](#insn-004cae98)

~~~json
{
  "source": "004cae98",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cae9c`](#insn-004cae9c)

~~~json
{
  "source": "004cae9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004caea0`](#insn-004caea0)

~~~json
{
  "source": "004caea0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004caf00`](#insn-004caf00)

~~~json
{
  "source": "004caf00",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
