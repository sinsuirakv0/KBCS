# 004cafdc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `004cafdc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ca/004cafdc.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0009.md#compare-94a124afd936b422df71fa4ff7671e15)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `004ede74`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004ede74.md) · 移動量 `+0x22e98`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0010.md#compare-5fda5e7549e03bc4a540a8891b26d7b4)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004cafdc",
  "name": "_ZN5Botan5PKCS88copy_keyERKNS_11Private_KeyE",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b274a087e562cf1407ee6c39d16acb249a3225661e046a6657275fe880809188",
  "source_text_sha256": "b274a087e562cf1407ee6c39d16acb249a3225661e046a6657275fe880809188",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004cafdc",
        "004cb0cb"
      ],
      [
        "004cb13c",
        "004cb13f"
      ]
    ],
    "bytes_sha256": "93798162fb5d9bc8fec92a85a1a1f1c723bd1446ea291db2adec63ba788860eb",
    "instruction_count": 61,
    "instruction_bytes": 244,
    "body_bytes": 244,
    "indirect": 2,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdc800](../00bdc/00bdc800.md)

## 呼び出し先

- [004c9e38](../004c9/004c9e38.md)
- [00522a98](../00522/00522a98.md)
- [00522a9c](../00522/00522a9c.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb810](../00bdb/00bdb810.md)
- [00bdc670](../00bdc/00bdc670.md)
- [00bdc7a0](../00bdc/00bdc7a0.md)
- [010a5058](../010a5/010a5058.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1281 bytes

~~~c

void _ZN5Botan5PKCS88copy_keyERKNS_11Private_KeyE(undefined8 param_1)

{
  long lVar1;
  undefined ***pppuVar2;
  long lVar3;
  undefined1 auStack_98 [8];
  void *local_90;
  void *local_88;
  long local_80;
  undefined **local_70 [2];
  void *local_60;
  undefined ***local_50;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  _ZN5Botan5PKCS810PEM_encodeERKNS_11Private_KeyE(local_70);
  _ZN5Botan17DataSource_MemoryC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
            (auStack_98,local_70);
  if (((byte)local_70[0] & 1) != 0) {
    _ZdlPv(local_60);
  }
  local_70[0] = &PTR_FUN_00bed5f0;
  local_50 = local_70;
  FUN_004c9e38(param_1,auStack_98,local_70,0);
  if (local_50 == local_70) {
    lVar3 = 0x20;
    pppuVar2 = local_70;
  }
  else {
    if (local_50 == (undefined ***)0x0) goto LAB_004cb078;
    lVar3 = 0x28;
    pppuVar2 = local_50;
  }
  (**(code **)((long)*pppuVar2 + lVar3))();
LAB_004cb078:
  if (local_90 != (void *)0x0) {
    local_88 = local_90;
    (*(code *)PTR_memset_00bea778)(local_90,0,local_80 - (long)local_90);
    free(local_90);
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
<a id="insn-004cafdc"></a> `004cafdc` | `ff 83 02 d1` | sub sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-004cafe0"></a> `004cafe0` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004cafe4"></a> `004cafe4` | `f5 43 00 f9` | str x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-004cafe8"></a> `004cafe8` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-004cafec"></a> `004cafec` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-004caff0"></a> `004caff0` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004caff4"></a> `004caff4` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-004caff8"></a> `004caff8` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-004caffc"></a> `004caffc` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004cb000"></a> `004cb000` | `e8 c3 00 91` | add x8,sp,#0x30 | `FALL_THROUGH`
<a id="insn-004cb004"></a> `004cb004` | `e7 45 1c 94` | bl 0x00bdc7a0 | `UNCONDITIONAL_CALL`
<a id="insn-004cb008"></a> `004cb008` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-004cb00c"></a> `004cb00c` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-004cb010"></a> `004cb010` | `98 45 1c 94` | bl 0x00bdc670 | `UNCONDITIONAL_CALL`
<a id="insn-004cb014"></a> `004cb014` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004cb018"></a> `004cb018` | `68 00 00 36` | tbz w8,#0x0,0x004cb024 | `CONDITIONAL_JUMP`
<a id="insn-004cb01c"></a> `004cb01c` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004cb020"></a> `004cb020` | `10 40 1c 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-004cb024"></a> `004cb024` | `08 39 00 d0` | adrp x8,0xbed000 | `FALL_THROUGH`
<a id="insn-004cb028"></a> `004cb028` | `08 c1 17 91` | add x8,x8,#0x5f0 | `FALL_THROUGH`
<a id="insn-004cb02c"></a> `004cb02c` | `f5 c3 00 91` | add x21,sp,#0x30 | `FALL_THROUGH`
<a id="insn-004cb030"></a> `004cb030` | `e8 1b 00 f9` | str x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004cb034"></a> `004cb034` | `f5 2b 00 f9` | str x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004cb038"></a> `004cb038` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-004cb03c"></a> `004cb03c` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-004cb040"></a> `004cb040` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-004cb044"></a> `004cb044` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-004cb048"></a> `004cb048` | `7c fb ff 97` | bl 0x004c9e38 | `UNCONDITIONAL_CALL`
<a id="insn-004cb04c"></a> `004cb04c` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004cb050"></a> `004cb050` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-004cb054"></a> `004cb054` | `80 00 00 54` | b.eq 0x004cb064 | `CONDITIONAL_JUMP`
<a id="insn-004cb058"></a> `004cb058` | `00 01 00 b4` | cbz x0,0x004cb078 | `CONDITIONAL_JUMP`
<a id="insn-004cb05c"></a> `004cb05c` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-004cb060"></a> `004cb060` | `03 00 00 14` | b 0x004cb06c | `UNCONDITIONAL_JUMP`
<a id="insn-004cb064"></a> `004cb064` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-004cb068"></a> `004cb068` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-004cb06c"></a> `004cb06c` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-004cb070"></a> `004cb070` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-004cb074"></a> `004cb074` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004cb078"></a> `004cb078` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004cb07c"></a> `004cb07c` | `73 01 00 b4` | cbz x19,0x004cb0a8 | `CONDITIONAL_JUMP`
<a id="insn-004cb080"></a> `004cb080` | `f3 0f 00 f9` | str x19,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-004cb084"></a> `004cb084` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004cb088"></a> `004cb088` | `e9 38 00 f0` | adrp x9,0xbea000 | `FALL_THROUGH`
<a id="insn-004cb08c"></a> `004cb08c` | `29 bd 43 f9` | ldr x9,[x9, #0x778] | `FALL_THROUGH`
<a id="insn-004cb090"></a> `004cb090` | `02 01 13 cb` | sub x2,x8,x19 | `FALL_THROUGH`
<a id="insn-004cb094"></a> `004cb094` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004cb098"></a> `004cb098` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004cb09c"></a> `004cb09c` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004cb0a0"></a> `004cb0a0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004cb0a4"></a> `004cb0a4` | `db 41 1c 94` | bl 0x00bdb810 | `UNCONDITIONAL_CALL`
<a id="insn-004cb0a8"></a> `004cb0a8` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-004cb0ac"></a> `004cb0ac` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004cb0b0"></a> `004cb0b0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004cb0b4"></a> `004cb0b4` | `41 04 00 54` | b.ne 0x004cb13c | `CONDITIONAL_JUMP`
<a id="insn-004cb0b8"></a> `004cb0b8` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-004cb0bc"></a> `004cb0bc` | `f5 43 40 f9` | ldr x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-004cb0c0"></a> `004cb0c0` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004cb0c4"></a> `004cb0c4` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-004cb0c8"></a> `004cb0c8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004cb13c"></a> `004cb13c` | `d5 3f 1c 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004cafdc`](#insn-004cafdc) 範囲 `[['004cafdc', '004cb01b']]`
  - `CONDITIONAL_JUMP` [`004cb018`](#insn-004cb018) → [`004cb024`](#insn-004cb024)
  - `FALL_THROUGH` [`004cb018`](#insn-004cb018) → [`004cb01c`](#insn-004cb01c)
- ブロック [`004cb01c`](#insn-004cb01c) 範囲 `[['004cb01c', '004cb023']]`
  - `FALL_THROUGH` [`004cb020`](#insn-004cb020) → [`004cb024`](#insn-004cb024)
- ブロック [`004cb024`](#insn-004cb024) 範囲 `[['004cb024', '004cb057']]`
  - `CONDITIONAL_JUMP` [`004cb054`](#insn-004cb054) → [`004cb064`](#insn-004cb064)
  - `FALL_THROUGH` [`004cb054`](#insn-004cb054) → [`004cb058`](#insn-004cb058)
- ブロック [`004cb058`](#insn-004cb058) 範囲 `[['004cb058', '004cb05b']]`
  - `CONDITIONAL_JUMP` [`004cb058`](#insn-004cb058) → [`004cb078`](#insn-004cb078)
  - `FALL_THROUGH` [`004cb058`](#insn-004cb058) → [`004cb05c`](#insn-004cb05c)
- ブロック [`004cb05c`](#insn-004cb05c) 範囲 `[['004cb05c', '004cb063']]`
  - `UNCONDITIONAL_JUMP` [`004cb060`](#insn-004cb060) → [`004cb06c`](#insn-004cb06c)
- ブロック [`004cb064`](#insn-004cb064) 範囲 `[['004cb064', '004cb06b']]`
  - `FALL_THROUGH` [`004cb068`](#insn-004cb068) → [`004cb06c`](#insn-004cb06c)
- ブロック [`004cb06c`](#insn-004cb06c) 範囲 `[['004cb06c', '004cb077']]`
  - `FALL_THROUGH` [`004cb074`](#insn-004cb074) → [`004cb078`](#insn-004cb078)
- ブロック [`004cb078`](#insn-004cb078) 範囲 `[['004cb078', '004cb07f']]`
  - `CONDITIONAL_JUMP` [`004cb07c`](#insn-004cb07c) → [`004cb0a8`](#insn-004cb0a8)
  - `FALL_THROUGH` [`004cb07c`](#insn-004cb07c) → [`004cb080`](#insn-004cb080)
- ブロック [`004cb080`](#insn-004cb080) 範囲 `[['004cb080', '004cb0a7']]`
  - `FALL_THROUGH` [`004cb0a4`](#insn-004cb0a4) → [`004cb0a8`](#insn-004cb0a8)
- ブロック [`004cb0a8`](#insn-004cb0a8) 範囲 `[['004cb0a8', '004cb0b7']]`
  - `CONDITIONAL_JUMP` [`004cb0b4`](#insn-004cb0b4) → [`004cb13c`](#insn-004cb13c)
  - `FALL_THROUGH` [`004cb0b4`](#insn-004cb0b4) → [`004cb0b8`](#insn-004cb0b8)
- ブロック [`004cb0b8`](#insn-004cb0b8) 範囲 `[['004cb0b8', '004cb0cb']]`
- ブロック [`004cb13c`](#insn-004cb13c) 範囲 `[['004cb13c', '004cb13f']]`

## 命令位置別の参照

- [`004cafe0`](#insn-004cafe0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cafe4`](#insn-004cafe4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cafe8`](#insn-004cafe8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004caffc`](#insn-004caffc) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cb004`](#insn-004cb004) → [`00bdc7a0`](../00bdc/00bdc7a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdc7a0` · 推定シンボル `None` · 推定型 `None`
- [`004cb010`](#insn-004cb010) → [`00bdc670`](../00bdc/00bdc670.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdc670` · 推定シンボル `None` · 推定型 `None`
- [`004cb014`](#insn-004cb014) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cb018`](#insn-004cb018) → [`004cb024`](#insn-004cb024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cb01c`](#insn-004cb01c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cb020`](#insn-004cb020) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`004cb030`](#insn-004cb030) → `00bed5f0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`004cb030`](#insn-004cb030) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cb034`](#insn-004cb034) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cb048`](#insn-004cb048) → [`004c9e38`](../004c9/004c9e38.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004c9e38` · 推定シンボル `None` · 推定型 `None`
- [`004cb04c`](#insn-004cb04c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cb054`](#insn-004cb054) → [`004cb064`](#insn-004cb064) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cb058`](#insn-004cb058) → [`004cb078`](#insn-004cb078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cb060`](#insn-004cb060) → [`004cb06c`](#insn-004cb06c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cb06c`](#insn-004cb06c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cb070`](#insn-004cb070) → `00bed610`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004cb070`](#insn-004cb070) → `00bed618`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`004cb074`](#insn-004cb074) → [`00522a98`](../00522/00522a98.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00522a98` · 推定シンボル `None` · 推定型 `None`
- [`004cb074`](#insn-004cb074) → [`00522a9c`](../00522/00522a9c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00522a9c` · 推定シンボル `None` · 推定型 `None`
- [`004cb078`](#insn-004cb078) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cb07c`](#insn-004cb07c) → [`004cb0a8`](#insn-004cb0a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cb080`](#insn-004cb080) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cb084`](#insn-004cb084) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cb08c`](#insn-004cb08c) → `00bea778`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004cb09c`](#insn-004cb09c) → [`010a5058`](../010a5/010a5058.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `010a5058` · 推定シンボル `None` · 推定型 `None`
- [`004cb0a4`](#insn-004cb0a4) → [`00bdb810`](../00bdb/00bdb810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb810` · 推定シンボル `None` · 推定型 `None`
- [`004cb0ac`](#insn-004cb0ac) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cb0b4`](#insn-004cb0b4) → [`004cb13c`](#insn-004cb13c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cb0b8`](#insn-004cb0b8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cb0bc`](#insn-004cb0bc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cb0c0`](#insn-004cb0c0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cb13c`](#insn-004cb13c) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004cafe0`](#insn-004cafe0)

~~~json
{
  "source": "004cafe0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cafe4`](#insn-004cafe4)

~~~json
{
  "source": "004cafe4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cafe8`](#insn-004cafe8)

~~~json
{
  "source": "004cafe8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004caffc`](#insn-004caffc)

~~~json
{
  "source": "004caffc",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cb004`](#insn-004cb004)

~~~json
{
  "source": "004cb004",
  "target": "00bdc7a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cb010`](#insn-004cb010)

~~~json
{
  "source": "004cb010",
  "target": "00bdc670",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cb014`](#insn-004cb014)

~~~json
{
  "source": "004cb014",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cb018`](#insn-004cb018)

~~~json
{
  "source": "004cb018",
  "target": "004cb024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cb01c`](#insn-004cb01c)

~~~json
{
  "source": "004cb01c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cb020`](#insn-004cb020)

~~~json
{
  "source": "004cb020",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cb030`](#insn-004cb030)

~~~json
{
  "source": "004cb030",
  "target": "00bed5f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00bed5f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004cb030`](#insn-004cb030)

~~~json
{
  "source": "004cb030",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cb034`](#insn-004cb034)

~~~json
{
  "source": "004cb034",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cb048`](#insn-004cb048)

~~~json
{
  "source": "004cb048",
  "target": "004c9e38",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cb04c`](#insn-004cb04c)

~~~json
{
  "source": "004cb04c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cb054`](#insn-004cb054)

~~~json
{
  "source": "004cb054",
  "target": "004cb064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cb058`](#insn-004cb058)

~~~json
{
  "source": "004cb058",
  "target": "004cb078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cb060`](#insn-004cb060)

~~~json
{
  "source": "004cb060",
  "target": "004cb06c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cb06c`](#insn-004cb06c)

~~~json
{
  "source": "004cb06c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cb070`](#insn-004cb070)

~~~json
{
  "source": "004cb070",
  "target": "00bed610",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00bed610",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004cb070`](#insn-004cb070)

~~~json
{
  "source": "004cb070",
  "target": "00bed618",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00bed618",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004cb074`](#insn-004cb074)

~~~json
{
  "source": "004cb074",
  "target": "00522a98",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cb074`](#insn-004cb074)

~~~json
{
  "source": "004cb074",
  "target": "00522a9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cb078`](#insn-004cb078)

~~~json
{
  "source": "004cb078",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cb07c`](#insn-004cb07c)

~~~json
{
  "source": "004cb07c",
  "target": "004cb0a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cb080`](#insn-004cb080)

~~~json
{
  "source": "004cb080",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cb084`](#insn-004cb084)

~~~json
{
  "source": "004cb084",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cb08c`](#insn-004cb08c)

~~~json
{
  "source": "004cb08c",
  "target": "00bea778",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00bea778",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004cb09c`](#insn-004cb09c)

~~~json
{
  "source": "004cb09c",
  "target": "010a5058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cb0a4`](#insn-004cb0a4)

~~~json
{
  "source": "004cb0a4",
  "target": "00bdb810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cb0ac`](#insn-004cb0ac)

~~~json
{
  "source": "004cb0ac",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cb0b4`](#insn-004cb0b4)

~~~json
{
  "source": "004cb0b4",
  "target": "004cb13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cb0b8`](#insn-004cb0b8)

~~~json
{
  "source": "004cb0b8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cb0bc`](#insn-004cb0bc)

~~~json
{
  "source": "004cb0bc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cb0c0`](#insn-004cb0c0)

~~~json
{
  "source": "004cb0c0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cb13c`](#insn-004cb13c)

~~~json
{
  "source": "004cb13c",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
