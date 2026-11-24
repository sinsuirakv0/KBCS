# 00acaad4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aca8d8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca8d8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/high-0007.md#compare-5267d275c78eebbb54eb834ed916875b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acab44`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aca/00acab44.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/high-0008.md#compare-7c5c4a5f9caabbf0831b2b6837986f64)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acaad4",
  "name": "FUN_00acaad4",
  "size": 256,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "814ae293cf440dfe843aadf31be53d921e5b20df0a46b610608b94ea818f6337",
  "source_text_sha256": "814ae293cf440dfe843aadf31be53d921e5b20df0a46b610608b94ea818f6337",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acaad4",
        "00acabd3"
      ]
    ],
    "bytes_sha256": "f018de7d47f61dfde7c8b13038c2d9377529625cf4e6c9c0341f049418eeabd9",
    "instruction_count": 64,
    "instruction_bytes": 256,
    "body_bytes": 256,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [00788cac](../00788/00788cac.md)
- [0082ee20](../0082e/0082ee20.md)
- [008cabc0](../008ca/008cabc0.md)
- [008d1c40](../008d1/008d1c40.md)
- [008fe9e4](../008fe/008fe9e4.md)
- [00a3de58](../00a3d/00a3de58.md)
- [00a73530](../00a73/00a73530.md)
- [00ac0454](../00ac0/00ac0454.md)

## 呼び出し先

- [0057bea8](../0057b/0057bea8.md)
- [008514f8](../00851/008514f8.md)
- [00c57ee0](../00c57/00c57ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1127 bytes

~~~c

void FUN_00acaad4(long param_1,long *param_2)

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
  *(undefined1 *)((long)&fde_table_entry_00332a20.data_loc + lVar2) = 1;
  lVar2 = FUN_008514f8();
  plVar3 = (long *)param_2[4];
  *(undefined4 *)((long)&fde_table_entry_00334170.data_loc + lVar2) = 0x129;
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
  FUN_0057bea8(local_70,param_1 + 0x110);
  if (local_50 == local_70) {
    lVar2 = 0x20;
  }
  else {
    if (local_50 == (long *)0x0) goto LAB_00acabac;
    lVar2 = 0x28;
    plVar4 = local_50;
  }
  (**(code **)(*plVar4 + lVar2))();
LAB_00acabac:
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
<a id="insn-00acaad4"></a> `00acaad4` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00acaad8"></a> `00acaad8` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acaadc"></a> `00acaadc` | `f5 2b 00 f9` | str x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acaae0"></a> `00acaae0` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acaae4"></a> `00acaae4` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00acaae8"></a> `00acaae8` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acaaec"></a> `00acaaec` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00acaaf0"></a> `00acaaf0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acaaf4"></a> `00acaaf4` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acaaf8"></a> `00acaaf8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acaafc"></a> `00acaafc` | `7f 1a f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acab00"></a> `00acab00` | `88 44 85 52` | mov w8,#0x2a24 | `FALL_THROUGH`
<a id="insn-00acab04"></a> `00acab04` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00acab08"></a> `00acab08` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00acab0c"></a> `00acab0c` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00acab10"></a> `00acab10` | `7a 1a f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acab14"></a> `00acab14` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00acab18"></a> `00acab18` | `80 12 40 f9` | ldr x0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00acab1c"></a> `00acab1c` | `89 2e 88 52` | mov w9,#0x4174 | `FALL_THROUGH`
<a id="insn-00acab20"></a> `00acab20` | `69 06 a0 72` | movk w9,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00acab24"></a> `00acab24` | `2a 25 80 52` | mov w10,#0x129 | `FALL_THROUGH`
<a id="insn-00acab28"></a> `00acab28` | `0a 69 29 b8` | str w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acab2c"></a> `00acab2c` | `00 01 00 b4` | cbz x0,0x00acab4c | `CONDITIONAL_JUMP`
<a id="insn-00acab30"></a> `00acab30` | `1f 00 14 eb` | cmp x0,x20 | `FALL_THROUGH`
<a id="insn-00acab34"></a> `00acab34` | `00 01 00 54` | b.eq 0x00acab54 | `CONDITIONAL_JUMP`
<a id="insn-00acab38"></a> `00acab38` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00acab3c"></a> `00acab3c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acab40"></a> `00acab40` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acab44"></a> `00acab44` | `e0 13 00 f9` | str x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acab48"></a> `00acab48` | `0a 00 00 14` | b 0x00acab70 | `UNCONDITIONAL_JUMP`
<a id="insn-00acab4c"></a> `00acab4c` | `ff 13 00 f9` | str xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acab50"></a> `00acab50` | `08 00 00 14` | b 0x00acab70 | `UNCONDITIONAL_JUMP`
<a id="insn-00acab54"></a> `00acab54` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00acab58"></a> `00acab58` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00acab5c"></a> `00acab5c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00acab60"></a> `00acab60` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acab64"></a> `00acab64` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acab68"></a> `00acab68` | `28 0d 40 f9` | ldr x8,[x9, #0x18] | `FALL_THROUGH`
<a id="insn-00acab6c"></a> `00acab6c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acab70"></a> `00acab70` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00acab74"></a> `00acab74` | `61 42 04 91` | add x1,x19,#0x110 | `FALL_THROUGH`
<a id="insn-00acab78"></a> `00acab78` | `f3 03 00 91` | mov x19,sp | `FALL_THROUGH`
<a id="insn-00acab7c"></a> `00acab7c` | `cb c4 ea 97` | bl 0x0057bea8 | `UNCONDITIONAL_CALL`
<a id="insn-00acab80"></a> `00acab80` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acab84"></a> `00acab84` | `1f 00 13 eb` | cmp x0,x19 | `FALL_THROUGH`
<a id="insn-00acab88"></a> `00acab88` | `80 00 00 54` | b.eq 0x00acab98 | `CONDITIONAL_JUMP`
<a id="insn-00acab8c"></a> `00acab8c` | `00 01 00 b4` | cbz x0,0x00acabac | `CONDITIONAL_JUMP`
<a id="insn-00acab90"></a> `00acab90` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00acab94"></a> `00acab94` | `03 00 00 14` | b 0x00acaba0 | `UNCONDITIONAL_JUMP`
<a id="insn-00acab98"></a> `00acab98` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00acab9c"></a> `00acab9c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00acaba0"></a> `00acaba0` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00acaba4"></a> `00acaba4` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acaba8"></a> `00acaba8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acabac"></a> `00acabac` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acabb0"></a> `00acabb0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acabb4"></a> `00acabb4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acabb8"></a> `00acabb8` | `c1 00 00 54` | b.ne 0x00acabd0 | `CONDITIONAL_JUMP`
<a id="insn-00acabbc"></a> `00acabbc` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acabc0"></a> `00acabc0` | `f5 2b 40 f9` | ldr x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acabc4"></a> `00acabc4` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acabc8"></a> `00acabc8` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00acabcc"></a> `00acabcc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acabd0"></a> `00acabd0` | `c4 34 06 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acaad4`](#insn-00acaad4) 範囲 `[['00acaad4', '00acab2f']]`
  - `CONDITIONAL_JUMP` [`00acab2c`](#insn-00acab2c) → [`00acab4c`](#insn-00acab4c)
  - `FALL_THROUGH` [`00acab2c`](#insn-00acab2c) → [`00acab30`](#insn-00acab30)
- ブロック [`00acab30`](#insn-00acab30) 範囲 `[['00acab30', '00acab37']]`
  - `CONDITIONAL_JUMP` [`00acab34`](#insn-00acab34) → [`00acab54`](#insn-00acab54)
  - `FALL_THROUGH` [`00acab34`](#insn-00acab34) → [`00acab38`](#insn-00acab38)
- ブロック [`00acab38`](#insn-00acab38) 範囲 `[['00acab38', '00acab4b']]`
  - `UNCONDITIONAL_JUMP` [`00acab48`](#insn-00acab48) → [`00acab70`](#insn-00acab70)
- ブロック [`00acab4c`](#insn-00acab4c) 範囲 `[['00acab4c', '00acab53']]`
  - `UNCONDITIONAL_JUMP` [`00acab50`](#insn-00acab50) → [`00acab70`](#insn-00acab70)
- ブロック [`00acab54`](#insn-00acab54) 範囲 `[['00acab54', '00acab6f']]`
  - `FALL_THROUGH` [`00acab6c`](#insn-00acab6c) → [`00acab70`](#insn-00acab70)
- ブロック [`00acab70`](#insn-00acab70) 範囲 `[['00acab70', '00acab8b']]`
  - `CONDITIONAL_JUMP` [`00acab88`](#insn-00acab88) → [`00acab98`](#insn-00acab98)
  - `FALL_THROUGH` [`00acab88`](#insn-00acab88) → [`00acab8c`](#insn-00acab8c)
- ブロック [`00acab8c`](#insn-00acab8c) 範囲 `[['00acab8c', '00acab8f']]`
  - `CONDITIONAL_JUMP` [`00acab8c`](#insn-00acab8c) → [`00acabac`](#insn-00acabac)
  - `FALL_THROUGH` [`00acab8c`](#insn-00acab8c) → [`00acab90`](#insn-00acab90)
- ブロック [`00acab90`](#insn-00acab90) 範囲 `[['00acab90', '00acab97']]`
  - `UNCONDITIONAL_JUMP` [`00acab94`](#insn-00acab94) → [`00acaba0`](#insn-00acaba0)
- ブロック [`00acab98`](#insn-00acab98) 範囲 `[['00acab98', '00acab9f']]`
  - `FALL_THROUGH` [`00acab9c`](#insn-00acab9c) → [`00acaba0`](#insn-00acaba0)
- ブロック [`00acaba0`](#insn-00acaba0) 範囲 `[['00acaba0', '00acabab']]`
  - `FALL_THROUGH` [`00acaba8`](#insn-00acaba8) → [`00acabac`](#insn-00acabac)
- ブロック [`00acabac`](#insn-00acabac) 範囲 `[['00acabac', '00acabbb']]`
  - `CONDITIONAL_JUMP` [`00acabb8`](#insn-00acabb8) → [`00acabd0`](#insn-00acabd0)
  - `FALL_THROUGH` [`00acabb8`](#insn-00acabb8) → [`00acabbc`](#insn-00acabbc)
- ブロック [`00acabbc`](#insn-00acabbc) 範囲 `[['00acabbc', '00acabcf']]`
- ブロック [`00acabd0`](#insn-00acabd0) 範囲 `[['00acabd0', '00acabd3']]`

## 命令位置別の参照

- [`00acaad8`](#insn-00acaad8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaadc`](#insn-00acaadc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaae0`](#insn-00acaae0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaaf8`](#insn-00acaaf8) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaafc`](#insn-00acaafc) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00acab0c`](#insn-00acab0c) → `00332a24`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acab10`](#insn-00acab10) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00acab28`](#insn-00acab28) → `00334174`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acab2c`](#insn-00acab2c) → [`00acab4c`](#insn-00acab4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab34`](#insn-00acab34) → [`00acab54`](#insn-00acab54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab44`](#insn-00acab44) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab48`](#insn-00acab48) → [`00acab70`](#insn-00acab70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab4c`](#insn-00acab4c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab50`](#insn-00acab50) → [`00acab70`](#insn-00acab70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab60`](#insn-00acab60) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab7c`](#insn-00acab7c) → [`0057bea8`](../0057b/0057bea8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0057bea8` · 推定シンボル `None` · 推定型 `None`
- [`00acab80`](#insn-00acab80) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab88`](#insn-00acab88) → [`00acab98`](#insn-00acab98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab8c`](#insn-00acab8c) → [`00acabac`](#insn-00acabac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab94`](#insn-00acab94) → [`00acaba0`](#insn-00acaba0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaba0`](#insn-00acaba0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acabb0`](#insn-00acabb0) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acabb8`](#insn-00acabb8) → [`00acabd0`](#insn-00acabd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acabbc`](#insn-00acabbc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acabc0`](#insn-00acabc0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acabc4`](#insn-00acabc4) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acabd0`](#insn-00acabd0) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acaad8`](#insn-00acaad8)

~~~json
{
  "source": "00acaad8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaadc`](#insn-00acaadc)

~~~json
{
  "source": "00acaadc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaae0`](#insn-00acaae0)

~~~json
{
  "source": "00acaae0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaaf8`](#insn-00acaaf8)

~~~json
{
  "source": "00acaaf8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaafc`](#insn-00acaafc)

~~~json
{
  "source": "00acaafc",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acab0c`](#insn-00acab0c)

~~~json
{
  "source": "00acab0c",
  "target": "00332a24",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e4f96800bc470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acab10`](#insn-00acab10)

~~~json
{
  "source": "00acab10",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acab28`](#insn-00acab28)

~~~json
{
  "source": "00acab28",
  "target": "00334174",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334170",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "6c266d00bc950900",
  "capture_start": "00334170",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acab2c`](#insn-00acab2c)

~~~json
{
  "source": "00acab2c",
  "target": "00acab4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab34`](#insn-00acab34)

~~~json
{
  "source": "00acab34",
  "target": "00acab54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab44`](#insn-00acab44)

~~~json
{
  "source": "00acab44",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab48`](#insn-00acab48)

~~~json
{
  "source": "00acab48",
  "target": "00acab70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab4c`](#insn-00acab4c)

~~~json
{
  "source": "00acab4c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab50`](#insn-00acab50)

~~~json
{
  "source": "00acab50",
  "target": "00acab70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab60`](#insn-00acab60)

~~~json
{
  "source": "00acab60",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab7c`](#insn-00acab7c)

~~~json
{
  "source": "00acab7c",
  "target": "0057bea8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acab80`](#insn-00acab80)

~~~json
{
  "source": "00acab80",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab88`](#insn-00acab88)

~~~json
{
  "source": "00acab88",
  "target": "00acab98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab8c`](#insn-00acab8c)

~~~json
{
  "source": "00acab8c",
  "target": "00acabac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab94`](#insn-00acab94)

~~~json
{
  "source": "00acab94",
  "target": "00acaba0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaba0`](#insn-00acaba0)

~~~json
{
  "source": "00acaba0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acabb0`](#insn-00acabb0)

~~~json
{
  "source": "00acabb0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acabb8`](#insn-00acabb8)

~~~json
{
  "source": "00acabb8",
  "target": "00acabd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acabbc`](#insn-00acabbc)

~~~json
{
  "source": "00acabbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acabc0`](#insn-00acabc0)

~~~json
{
  "source": "00acabc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acabc4`](#insn-00acabc4)

~~~json
{
  "source": "00acabc4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acabd0`](#insn-00acabd0)

~~~json
{
  "source": "00acabd0",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
