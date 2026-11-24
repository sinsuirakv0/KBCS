# 006afabc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `006afa7c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006af/006afa7c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0031.md#compare-61772a4baeac112fa9cd036e149ef943)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `006afb14`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006af/006afb14.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0031.md#compare-7482e31b9014c037f157d87a9e591cd0)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006afabc",
  "name": "FUN_006afabc",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3e16be73fe160c32e20a1a33b68d4337e5f8a1e70af9b867adfd42ee2877dd00",
  "source_text_sha256": "3e16be73fe160c32e20a1a33b68d4337e5f8a1e70af9b867adfd42ee2877dd00",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006afabc",
        "006afba3"
      ]
    ],
    "bytes_sha256": "2b64728dac2a1295f95921ddaf0defd0a846599e17e8e7974c5f9bd12bb3970d",
    "instruction_count": 58,
    "instruction_bytes": 232,
    "body_bytes": 232,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [006a6a54](../006a6/006a6a54.md)
- [00811368](../00811/00811368.md)
- [00ab09f4](../00ab0/00ab09f4.md)
- [00c57ee0](../00c57/00c57ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1427 bytes

~~~c

void FUN_006afabc(long param_1,undefined8 param_2,int *param_3)

{
  int iVar1;
  long lVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  long lVar5;
  undefined8 local_58;
  undefined8 uStack_50;
  undefined8 local_48;
  undefined8 uStack_40;
  long local_38;
  
                    /* try { // try from 006afac4 to 007afc77 has its CatchHandler @ 006af8e8 */
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  iVar1 = *param_3;
  if (iVar1 == 4) {
    lVar5 = *(long *)(param_1 + 8);
    FUN_00811368(*(undefined4 *)(lVar5 + (long)*(int *)(param_1 + 0x10) * 8 + 0xa0));
    FUN_00ab09f4(&local_58);
    *(undefined8 *)(lVar5 + 0xf8) = uStack_50;
    *(undefined8 *)(lVar5 + 0xf0) = local_58;
    *(undefined8 *)(lVar5 + 0x108) = uStack_40;
    *(undefined8 *)(lVar5 + 0x100) = local_48;
    FUN_006a6a54(lVar5,*(undefined4 *)(param_1 + 0x10));
  }
  else {
    if (iVar1 == 3) {
      uVar3 = FUN_0047acf4();
      if (*(long *)(lVar2 + 0x28) == local_38) {
        uVar4 = 0xb;
        goto LAB_006afb28;
      }
      goto LAB_006afba0;
    }
    if (iVar1 == 0) {
      uVar3 = FUN_0047acf4();
      if (*(long *)(lVar2 + 0x28) != local_38) goto LAB_006afba0;
      uVar4 = 10;
LAB_006afb28:
      FUN_0047cdd4(uVar3,uVar4,0);
      return;
    }
  }
  if (*(long *)(lVar2 + 0x28) == local_38) {
    return;
  }
LAB_006afba0:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006afabc"></a> `006afabc` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-006afac0"></a> `006afac0` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006afac4"></a> `006afac4` | `f5 23 00 f9` | str x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006afac8"></a> `006afac8` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-006afacc"></a> `006afacc` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-006afad0"></a> `006afad0` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-006afad4"></a> `006afad4` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-006afad8"></a> `006afad8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-006afadc"></a> `006afadc` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-006afae0"></a> `006afae0` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-006afae4"></a> `006afae4` | `e0 02 00 54` | b.eq 0x006afb40 | `CONDITIONAL_JUMP`
<a id="insn-006afae8"></a> `006afae8` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-006afaec"></a> `006afaec` | `20 01 00 54` | b.eq 0x006afb10 | `CONDITIONAL_JUMP`
<a id="insn-006afaf0"></a> `006afaf0` | `68 04 00 35` | cbnz w8,0x006afb7c | `CONDITIONAL_JUMP`
<a id="insn-006afaf4"></a> `006afaf4` | `80 2c f7 97` | bl 0x0047acf4 | `UNCONDITIONAL_CALL`
<a id="insn-006afaf8"></a> `006afaf8` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-006afafc"></a> `006afafc` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-006afb00"></a> `006afb00` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006afb04"></a> `006afb04` | `e1 04 00 54` | b.ne 0x006afba0 | `CONDITIONAL_JUMP`
<a id="insn-006afb08"></a> `006afb08` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-006afb0c"></a> `006afb0c` | `07 00 00 14` | b 0x006afb28 | `UNCONDITIONAL_JUMP`
<a id="insn-006afb10"></a> `006afb10` | `79 2c f7 97` | bl 0x0047acf4 | `UNCONDITIONAL_CALL`
<a id="insn-006afb14"></a> `006afb14` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-006afb18"></a> `006afb18` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-006afb1c"></a> `006afb1c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006afb20"></a> `006afb20` | `01 04 00 54` | b.ne 0x006afba0 | `CONDITIONAL_JUMP`
<a id="insn-006afb24"></a> `006afb24` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-006afb28"></a> `006afb28` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-006afb2c"></a> `006afb2c` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-006afb30"></a> `006afb30` | `f5 23 40 f9` | ldr x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006afb34"></a> `006afb34` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006afb38"></a> `006afb38` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-006afb3c"></a> `006afb3c` | `a6 34 f7 17` | b 0x0047cdd4 | `CALL_TERMINATOR`
<a id="insn-006afb40"></a> `006afb40` | `13 04 40 f9` | ldr x19,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-006afb44"></a> `006afb44` | `08 10 80 b9` | ldrsw x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-006afb48"></a> `006afb48` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-006afb4c"></a> `006afb4c` | `68 0e 08 8b` | add x8,x19,x8, LSL #0x3 | `FALL_THROUGH`
<a id="insn-006afb50"></a> `006afb50` | `08 a1 40 b9` | ldr w8,[x8, #0xa0] | `FALL_THROUGH`
<a id="insn-006afb54"></a> `006afb54` | `e0 03 08 2a` | mov w0,w8 | `FALL_THROUGH`
<a id="insn-006afb58"></a> `006afb58` | `04 86 05 94` | bl 0x00811368 | `UNCONDITIONAL_CALL`
<a id="insn-006afb5c"></a> `006afb5c` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-006afb60"></a> `006afb60` | `a5 03 10 94` | bl 0x00ab09f4 | `UNCONDITIONAL_CALL`
<a id="insn-006afb64"></a> `006afb64` | `e0 83 c0 3c` | ldur q0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-006afb68"></a> `006afb68` | `e1 83 c1 3c` | ldur q1,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-006afb6c"></a> `006afb6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-006afb70"></a> `006afb70` | `60 86 07 ad` | stp q0,q1,[x19, #0xf0] | `FALL_THROUGH`
<a id="insn-006afb74"></a> `006afb74` | `a1 12 40 b9` | ldr w1,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-006afb78"></a> `006afb78` | `b7 db ff 97` | bl 0x006a6a54 | `UNCONDITIONAL_CALL`
<a id="insn-006afb7c"></a> `006afb7c` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-006afb80"></a> `006afb80` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-006afb84"></a> `006afb84` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006afb88"></a> `006afb88` | `c1 00 00 54` | b.ne 0x006afba0 | `CONDITIONAL_JUMP`
<a id="insn-006afb8c"></a> `006afb8c` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-006afb90"></a> `006afb90` | `f5 23 40 f9` | ldr x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006afb94"></a> `006afb94` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006afb98"></a> `006afb98` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-006afb9c"></a> `006afb9c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-006afba0"></a> `006afba0` | `d0 a0 16 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006afabc`](#insn-006afabc) 範囲 `[['006afabc', '006afac3']]`
  - `FALL_THROUGH` [`006afac0`](#insn-006afac0) → [`006afac4`](#insn-006afac4)
- ブロック [`006afac4`](#insn-006afac4) 範囲 `[['006afac4', '006afae7']]`
  - `CONDITIONAL_JUMP` [`006afae4`](#insn-006afae4) → [`006afb40`](#insn-006afb40)
  - `FALL_THROUGH` [`006afae4`](#insn-006afae4) → [`006afae8`](#insn-006afae8)
- ブロック [`006afae8`](#insn-006afae8) 範囲 `[['006afae8', '006afaef']]`
  - `CONDITIONAL_JUMP` [`006afaec`](#insn-006afaec) → [`006afb10`](#insn-006afb10)
  - `FALL_THROUGH` [`006afaec`](#insn-006afaec) → [`006afaf0`](#insn-006afaf0)
- ブロック [`006afaf0`](#insn-006afaf0) 範囲 `[['006afaf0', '006afaf3']]`
  - `CONDITIONAL_JUMP` [`006afaf0`](#insn-006afaf0) → [`006afb7c`](#insn-006afb7c)
  - `FALL_THROUGH` [`006afaf0`](#insn-006afaf0) → [`006afaf4`](#insn-006afaf4)
- ブロック [`006afaf4`](#insn-006afaf4) 範囲 `[['006afaf4', '006afb07']]`
  - `CONDITIONAL_JUMP` [`006afb04`](#insn-006afb04) → [`006afba0`](#insn-006afba0)
  - `FALL_THROUGH` [`006afb04`](#insn-006afb04) → [`006afb08`](#insn-006afb08)
- ブロック [`006afb08`](#insn-006afb08) 範囲 `[['006afb08', '006afb0f']]`
  - `UNCONDITIONAL_JUMP` [`006afb0c`](#insn-006afb0c) → [`006afb28`](#insn-006afb28)
- ブロック [`006afb10`](#insn-006afb10) 範囲 `[['006afb10', '006afb23']]`
  - `CONDITIONAL_JUMP` [`006afb20`](#insn-006afb20) → [`006afba0`](#insn-006afba0)
  - `FALL_THROUGH` [`006afb20`](#insn-006afb20) → [`006afb24`](#insn-006afb24)
- ブロック [`006afb24`](#insn-006afb24) 範囲 `[['006afb24', '006afb27']]`
  - `FALL_THROUGH` [`006afb24`](#insn-006afb24) → [`006afb28`](#insn-006afb28)
- ブロック [`006afb28`](#insn-006afb28) 範囲 `[['006afb28', '006afb3f']]`
- ブロック [`006afb40`](#insn-006afb40) 範囲 `[['006afb40', '006afb7b']]`
  - `FALL_THROUGH` [`006afb78`](#insn-006afb78) → [`006afb7c`](#insn-006afb7c)
- ブロック [`006afb7c`](#insn-006afb7c) 範囲 `[['006afb7c', '006afb8b']]`
  - `CONDITIONAL_JUMP` [`006afb88`](#insn-006afb88) → [`006afba0`](#insn-006afba0)
  - `FALL_THROUGH` [`006afb88`](#insn-006afb88) → [`006afb8c`](#insn-006afb8c)
- ブロック [`006afb8c`](#insn-006afb8c) 範囲 `[['006afb8c', '006afb9f']]`
- ブロック [`006afba0`](#insn-006afba0) 範囲 `[['006afba0', '006afba3']]`

## 命令位置別の参照

- [`006afac0`](#insn-006afac0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afac4`](#insn-006afac4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afac8`](#insn-006afac8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afad8`](#insn-006afad8) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afae4`](#insn-006afae4) → [`006afb40`](#insn-006afb40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afaec`](#insn-006afaec) → [`006afb10`](#insn-006afb10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afaf0`](#insn-006afaf0) → [`006afb7c`](#insn-006afb7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afaf4`](#insn-006afaf4) → [`0047acf4`](../0047a/0047acf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acf4` · 推定シンボル `None` · 推定型 `None`
- [`006afafc`](#insn-006afafc) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afb04`](#insn-006afb04) → [`006afba0`](#insn-006afba0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afb0c`](#insn-006afb0c) → [`006afb28`](#insn-006afb28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afb10`](#insn-006afb10) → [`0047acf4`](../0047a/0047acf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acf4` · 推定シンボル `None` · 推定型 `None`
- [`006afb18`](#insn-006afb18) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afb20`](#insn-006afb20) → [`006afba0`](#insn-006afba0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afb2c`](#insn-006afb2c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afb30`](#insn-006afb30) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afb34`](#insn-006afb34) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afb3c`](#insn-006afb3c) → [`0047cdd4`](../0047c/0047cdd4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cdd4` · 推定シンボル `None` · 推定型 `None`
- [`006afb58`](#insn-006afb58) → [`00811368`](../00811/00811368.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00811368` · 推定シンボル `None` · 推定型 `None`
- [`006afb60`](#insn-006afb60) → [`00ab09f4`](../00ab0/00ab09f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab09f4` · 推定シンボル `None` · 推定型 `None`
- [`006afb64`](#insn-006afb64) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afb68`](#insn-006afb68) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afb78`](#insn-006afb78) → [`006a6a54`](../006a6/006a6a54.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006a6a54` · 推定シンボル `None` · 推定型 `None`
- [`006afb80`](#insn-006afb80) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afb88`](#insn-006afb88) → [`006afba0`](#insn-006afba0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afb8c`](#insn-006afb8c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afb90`](#insn-006afb90) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afb94`](#insn-006afb94) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006afba0`](#insn-006afba0) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006afac0`](#insn-006afac0)

~~~json
{
  "source": "006afac0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afac4`](#insn-006afac4)

~~~json
{
  "source": "006afac4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afac8`](#insn-006afac8)

~~~json
{
  "source": "006afac8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afad8`](#insn-006afad8)

~~~json
{
  "source": "006afad8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afae4`](#insn-006afae4)

~~~json
{
  "source": "006afae4",
  "target": "006afb40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afaec`](#insn-006afaec)

~~~json
{
  "source": "006afaec",
  "target": "006afb10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afaf0`](#insn-006afaf0)

~~~json
{
  "source": "006afaf0",
  "target": "006afb7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afaf4`](#insn-006afaf4)

~~~json
{
  "source": "006afaf4",
  "target": "0047acf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006afafc`](#insn-006afafc)

~~~json
{
  "source": "006afafc",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afb04`](#insn-006afb04)

~~~json
{
  "source": "006afb04",
  "target": "006afba0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afb0c`](#insn-006afb0c)

~~~json
{
  "source": "006afb0c",
  "target": "006afb28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afb10`](#insn-006afb10)

~~~json
{
  "source": "006afb10",
  "target": "0047acf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006afb18`](#insn-006afb18)

~~~json
{
  "source": "006afb18",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afb20`](#insn-006afb20)

~~~json
{
  "source": "006afb20",
  "target": "006afba0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afb2c`](#insn-006afb2c)

~~~json
{
  "source": "006afb2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afb30`](#insn-006afb30)

~~~json
{
  "source": "006afb30",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afb34`](#insn-006afb34)

~~~json
{
  "source": "006afb34",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afb3c`](#insn-006afb3c)

~~~json
{
  "source": "006afb3c",
  "target": "0047cdd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006afb58`](#insn-006afb58)

~~~json
{
  "source": "006afb58",
  "target": "00811368",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006afb60`](#insn-006afb60)

~~~json
{
  "source": "006afb60",
  "target": "00ab09f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006afb64`](#insn-006afb64)

~~~json
{
  "source": "006afb64",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afb68`](#insn-006afb68)

~~~json
{
  "source": "006afb68",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afb78`](#insn-006afb78)

~~~json
{
  "source": "006afb78",
  "target": "006a6a54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006afb80`](#insn-006afb80)

~~~json
{
  "source": "006afb80",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afb88`](#insn-006afb88)

~~~json
{
  "source": "006afb88",
  "target": "006afba0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afb8c`](#insn-006afb8c)

~~~json
{
  "source": "006afb8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afb90`](#insn-006afb90)

~~~json
{
  "source": "006afb90",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afb94`](#insn-006afb94)

~~~json
{
  "source": "006afb94",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006afba0`](#insn-006afba0)

~~~json
{
  "source": "006afba0",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
