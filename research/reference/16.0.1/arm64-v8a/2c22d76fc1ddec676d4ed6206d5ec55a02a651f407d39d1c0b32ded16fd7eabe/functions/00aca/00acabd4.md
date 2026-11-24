# 00acabd4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aca9d8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca9d8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/high-0007.md#compare-d3c763fd67b0316acf6661267e43a0d5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acac44`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aca/00acac44.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/high-0008.md#compare-d0bf4e38fde113b2565ab01b62539ed9)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acabd4",
  "name": "FUN_00acabd4",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "95e567a8a76353566504c71df91884abca034a093dd979ee08837847757e3aa9",
  "source_text_sha256": "95e567a8a76353566504c71df91884abca034a093dd979ee08837847757e3aa9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acabd4",
        "00acacc7"
      ]
    ],
    "bytes_sha256": "932ef51d331fb260600f0520f4a53cc6b6b827aefe9b1daa8068997c0689c39e",
    "instruction_count": 61,
    "instruction_bytes": 244,
    "body_bytes": 244,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [0078bd58](../0078b/0078bd58.md)
- [0078bfc4](../0078b/0078bfc4.md)
- [0078df38](../0078d/0078df38.md)
- [0078e6a4](../0078e/0078e6a4.md)
- [0078e91c](../0078e/0078e91c.md)
- [0078eb30](../0078e/0078eb30.md)
- [00838ba0](../00838/00838ba0.md)
- [008cf91c](../008cf/008cf91c.md)
- [008d0710](../008d0/008d0710.md)
- [008d8404](../008d8/008d8404.md)
- [008d9534](../008d9/008d9534.md)
- [008fd500](../008fd/008fd500.md)
- [009015dc](../00901/009015dc.md)
- [009d0320](../009d0/009d0320.md)
- [00a3ce18](../00a3c/00a3ce18.md)
- [00a40d90](../00a40/00a40d90.md)
- [00a73530](../00a73/00a73530.md)
- [00ac3350](../00ac3/00ac3350.md)

## 呼び出し先

- [0057bea8](../0057b/0057bea8.md)
- [008514f8](../00851/008514f8.md)
- [00ac9594](../00ac9/00ac9594.md)
- [00c57ee0](../00c57/00c57ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1052 bytes

~~~c

void FUN_00acabd4(long param_1,long *param_2)

{
  long lVar1;
  long lVar2;
  long *plVar3;
  long *plVar4;
  long local_70 [4];
  long *local_50;
  long local_38;
  
  plVar4 = local_70;
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  lVar2 = FUN_008514f8();
  plVar3 = (long *)param_2[4];
  *(undefined1 *)((long)&fde_table_entry_00332a20.data_loc + lVar2 + 1) = 1;
  if (plVar3 == (long *)0x0) {
    local_50 = (long *)0x0;
  }
  else if (plVar3 == param_2) {
    local_50 = local_70;
    (**(code **)(*param_2 + 0x18))(param_2,local_70);
  }
  else {
    local_50 = (long *)(**(code **)(*plVar3 + 0x10))();
  }
  FUN_0057bea8(local_70,param_1 + 0xe0);
  if (local_50 == local_70) {
    lVar2 = 0x20;
  }
  else {
    if (local_50 == (long *)0x0) goto LAB_00acac98;
    lVar2 = 0x28;
    plVar4 = local_50;
  }
  (**(code **)(*plVar4 + lVar2))();
LAB_00acac98:
  FUN_00ac9594(param_1);
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
<a id="insn-00acabd4"></a> `00acabd4` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00acabd8"></a> `00acabd8` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acabdc"></a> `00acabdc` | `f5 2b 00 f9` | str x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acabe0"></a> `00acabe0` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acabe4"></a> `00acabe4` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00acabe8"></a> `00acabe8` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acabec"></a> `00acabec` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00acabf0"></a> `00acabf0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acabf4"></a> `00acabf4` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acabf8"></a> `00acabf8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acabfc"></a> `00acabfc` | `3f 1a f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acac00"></a> `00acac00` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00acac04"></a> `00acac04` | `80 12 40 f9` | ldr x0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00acac08"></a> `00acac08` | `a9 44 85 52` | mov w9,#0x2a25 | `FALL_THROUGH`
<a id="insn-00acac0c"></a> `00acac0c` | `69 06 a0 72` | movk w9,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00acac10"></a> `00acac10` | `2a 00 80 52` | mov w10,#0x1 | `FALL_THROUGH`
<a id="insn-00acac14"></a> `00acac14` | `0a 69 29 38` | strb w10,[x8, x9, LSL ] | `FALL_THROUGH`
<a id="insn-00acac18"></a> `00acac18` | `00 01 00 b4` | cbz x0,0x00acac38 | `CONDITIONAL_JUMP`
<a id="insn-00acac1c"></a> `00acac1c` | `1f 00 14 eb` | cmp x0,x20 | `FALL_THROUGH`
<a id="insn-00acac20"></a> `00acac20` | `00 01 00 54` | b.eq 0x00acac40 | `CONDITIONAL_JUMP`
<a id="insn-00acac24"></a> `00acac24` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00acac28"></a> `00acac28` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acac2c"></a> `00acac2c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acac30"></a> `00acac30` | `e0 13 00 f9` | str x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acac34"></a> `00acac34` | `0a 00 00 14` | b 0x00acac5c | `UNCONDITIONAL_JUMP`
<a id="insn-00acac38"></a> `00acac38` | `ff 13 00 f9` | str xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acac3c"></a> `00acac3c` | `08 00 00 14` | b 0x00acac5c | `UNCONDITIONAL_JUMP`
<a id="insn-00acac40"></a> `00acac40` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00acac44"></a> `00acac44` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00acac48"></a> `00acac48` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00acac4c"></a> `00acac4c` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acac50"></a> `00acac50` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acac54"></a> `00acac54` | `28 0d 40 f9` | ldr x8,[x9, #0x18] | `FALL_THROUGH`
<a id="insn-00acac58"></a> `00acac58` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acac5c"></a> `00acac5c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00acac60"></a> `00acac60` | `61 82 03 91` | add x1,x19,#0xe0 | `FALL_THROUGH`
<a id="insn-00acac64"></a> `00acac64` | `f4 03 00 91` | mov x20,sp | `FALL_THROUGH`
<a id="insn-00acac68"></a> `00acac68` | `90 c4 ea 97` | bl 0x0057bea8 | `UNCONDITIONAL_CALL`
<a id="insn-00acac6c"></a> `00acac6c` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acac70"></a> `00acac70` | `1f 00 14 eb` | cmp x0,x20 | `FALL_THROUGH`
<a id="insn-00acac74"></a> `00acac74` | `80 00 00 54` | b.eq 0x00acac84 | `CONDITIONAL_JUMP`
<a id="insn-00acac78"></a> `00acac78` | `00 01 00 b4` | cbz x0,0x00acac98 | `CONDITIONAL_JUMP`
<a id="insn-00acac7c"></a> `00acac7c` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00acac80"></a> `00acac80` | `03 00 00 14` | b 0x00acac8c | `UNCONDITIONAL_JUMP`
<a id="insn-00acac84"></a> `00acac84` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00acac88"></a> `00acac88` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00acac8c"></a> `00acac8c` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00acac90"></a> `00acac90` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acac94"></a> `00acac94` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acac98"></a> `00acac98` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acac9c"></a> `00acac9c` | `3e fa ff 97` | bl 0x00ac9594 | `UNCONDITIONAL_CALL`
<a id="insn-00acaca0"></a> `00acaca0` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acaca4"></a> `00acaca4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acaca8"></a> `00acaca8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acacac"></a> `00acacac` | `c1 00 00 54` | b.ne 0x00acacc4 | `CONDITIONAL_JUMP`
<a id="insn-00acacb0"></a> `00acacb0` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acacb4"></a> `00acacb4` | `f5 2b 40 f9` | ldr x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acacb8"></a> `00acacb8` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acacbc"></a> `00acacbc` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00acacc0"></a> `00acacc0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acacc4"></a> `00acacc4` | `87 34 06 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acabd4`](#insn-00acabd4) 範囲 `[['00acabd4', '00acac1b']]`
  - `CONDITIONAL_JUMP` [`00acac18`](#insn-00acac18) → [`00acac38`](#insn-00acac38)
  - `FALL_THROUGH` [`00acac18`](#insn-00acac18) → [`00acac1c`](#insn-00acac1c)
- ブロック [`00acac1c`](#insn-00acac1c) 範囲 `[['00acac1c', '00acac23']]`
  - `CONDITIONAL_JUMP` [`00acac20`](#insn-00acac20) → [`00acac40`](#insn-00acac40)
  - `FALL_THROUGH` [`00acac20`](#insn-00acac20) → [`00acac24`](#insn-00acac24)
- ブロック [`00acac24`](#insn-00acac24) 範囲 `[['00acac24', '00acac37']]`
  - `UNCONDITIONAL_JUMP` [`00acac34`](#insn-00acac34) → [`00acac5c`](#insn-00acac5c)
- ブロック [`00acac38`](#insn-00acac38) 範囲 `[['00acac38', '00acac3f']]`
  - `UNCONDITIONAL_JUMP` [`00acac3c`](#insn-00acac3c) → [`00acac5c`](#insn-00acac5c)
- ブロック [`00acac40`](#insn-00acac40) 範囲 `[['00acac40', '00acac5b']]`
  - `FALL_THROUGH` [`00acac58`](#insn-00acac58) → [`00acac5c`](#insn-00acac5c)
- ブロック [`00acac5c`](#insn-00acac5c) 範囲 `[['00acac5c', '00acac77']]`
  - `CONDITIONAL_JUMP` [`00acac74`](#insn-00acac74) → [`00acac84`](#insn-00acac84)
  - `FALL_THROUGH` [`00acac74`](#insn-00acac74) → [`00acac78`](#insn-00acac78)
- ブロック [`00acac78`](#insn-00acac78) 範囲 `[['00acac78', '00acac7b']]`
  - `CONDITIONAL_JUMP` [`00acac78`](#insn-00acac78) → [`00acac98`](#insn-00acac98)
  - `FALL_THROUGH` [`00acac78`](#insn-00acac78) → [`00acac7c`](#insn-00acac7c)
- ブロック [`00acac7c`](#insn-00acac7c) 範囲 `[['00acac7c', '00acac83']]`
  - `UNCONDITIONAL_JUMP` [`00acac80`](#insn-00acac80) → [`00acac8c`](#insn-00acac8c)
- ブロック [`00acac84`](#insn-00acac84) 範囲 `[['00acac84', '00acac8b']]`
  - `FALL_THROUGH` [`00acac88`](#insn-00acac88) → [`00acac8c`](#insn-00acac8c)
- ブロック [`00acac8c`](#insn-00acac8c) 範囲 `[['00acac8c', '00acac97']]`
  - `FALL_THROUGH` [`00acac94`](#insn-00acac94) → [`00acac98`](#insn-00acac98)
- ブロック [`00acac98`](#insn-00acac98) 範囲 `[['00acac98', '00acacaf']]`
  - `CONDITIONAL_JUMP` [`00acacac`](#insn-00acacac) → [`00acacc4`](#insn-00acacc4)
  - `FALL_THROUGH` [`00acacac`](#insn-00acacac) → [`00acacb0`](#insn-00acacb0)
- ブロック [`00acacb0`](#insn-00acacb0) 範囲 `[['00acacb0', '00acacc3']]`
- ブロック [`00acacc4`](#insn-00acacc4) 範囲 `[['00acacc4', '00acacc7']]`

## 命令位置別の参照

- [`00acabd8`](#insn-00acabd8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acabdc`](#insn-00acabdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acabe0`](#insn-00acabe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acabf8`](#insn-00acabf8) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acabfc`](#insn-00acabfc) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00acac14`](#insn-00acac14) → `00332a25`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acac18`](#insn-00acac18) → [`00acac38`](#insn-00acac38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acac20`](#insn-00acac20) → [`00acac40`](#insn-00acac40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acac30`](#insn-00acac30) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acac34`](#insn-00acac34) → [`00acac5c`](#insn-00acac5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acac38`](#insn-00acac38) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acac3c`](#insn-00acac3c) → [`00acac5c`](#insn-00acac5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acac4c`](#insn-00acac4c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acac68`](#insn-00acac68) → [`0057bea8`](../0057b/0057bea8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0057bea8` · 推定シンボル `None` · 推定型 `None`
- [`00acac6c`](#insn-00acac6c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acac74`](#insn-00acac74) → [`00acac84`](#insn-00acac84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acac78`](#insn-00acac78) → [`00acac98`](#insn-00acac98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acac80`](#insn-00acac80) → [`00acac8c`](#insn-00acac8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acac8c`](#insn-00acac8c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acac9c`](#insn-00acac9c) → [`00ac9594`](../00ac9/00ac9594.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac9594` · 推定シンボル `None` · 推定型 `None`
- [`00acaca4`](#insn-00acaca4) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acacac`](#insn-00acacac) → [`00acacc4`](#insn-00acacc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acacb0`](#insn-00acacb0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acacb4`](#insn-00acacb4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acacb8`](#insn-00acacb8) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acacc4`](#insn-00acacc4) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acabd8`](#insn-00acabd8)

~~~json
{
  "source": "00acabd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acabdc`](#insn-00acabdc)

~~~json
{
  "source": "00acabdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acabe0`](#insn-00acabe0)

~~~json
{
  "source": "00acabe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acabf8`](#insn-00acabf8)

~~~json
{
  "source": "00acabf8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acabfc`](#insn-00acabfc)

~~~json
{
  "source": "00acabfc",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acac14`](#insn-00acac14)

~~~json
{
  "source": "00acac14",
  "target": "00332a25",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 5,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e4f96800bc470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acac18`](#insn-00acac18)

~~~json
{
  "source": "00acac18",
  "target": "00acac38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acac20`](#insn-00acac20)

~~~json
{
  "source": "00acac20",
  "target": "00acac40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acac30`](#insn-00acac30)

~~~json
{
  "source": "00acac30",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acac34`](#insn-00acac34)

~~~json
{
  "source": "00acac34",
  "target": "00acac5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acac38`](#insn-00acac38)

~~~json
{
  "source": "00acac38",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acac3c`](#insn-00acac3c)

~~~json
{
  "source": "00acac3c",
  "target": "00acac5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acac4c`](#insn-00acac4c)

~~~json
{
  "source": "00acac4c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acac68`](#insn-00acac68)

~~~json
{
  "source": "00acac68",
  "target": "0057bea8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acac6c`](#insn-00acac6c)

~~~json
{
  "source": "00acac6c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acac74`](#insn-00acac74)

~~~json
{
  "source": "00acac74",
  "target": "00acac84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acac78`](#insn-00acac78)

~~~json
{
  "source": "00acac78",
  "target": "00acac98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acac80`](#insn-00acac80)

~~~json
{
  "source": "00acac80",
  "target": "00acac8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acac8c`](#insn-00acac8c)

~~~json
{
  "source": "00acac8c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acac9c`](#insn-00acac9c)

~~~json
{
  "source": "00acac9c",
  "target": "00ac9594",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaca4`](#insn-00acaca4)

~~~json
{
  "source": "00acaca4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acacac`](#insn-00acacac)

~~~json
{
  "source": "00acacac",
  "target": "00acacc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acacb0`](#insn-00acacb0)

~~~json
{
  "source": "00acacb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acacb4`](#insn-00acacb4)

~~~json
{
  "source": "00acacb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acacb8`](#insn-00acacb8)

~~~json
{
  "source": "00acacb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acacc4`](#insn-00acacc4)

~~~json
{
  "source": "00acacc4",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
