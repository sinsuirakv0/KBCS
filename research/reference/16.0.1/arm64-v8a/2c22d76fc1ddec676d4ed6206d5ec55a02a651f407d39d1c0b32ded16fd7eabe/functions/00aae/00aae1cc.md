# 00aae1cc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aadfd0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aadfd0.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-82b7d888aa33a47b035d27c736273bd5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aae23c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aae/00aae23c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0064.md#compare-f66cfa722d522fe18bcba50921ab2662)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aae1cc",
  "name": "FUN_00aae1cc",
  "size": 268,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "05b381d2458457e7f12195191b15e1cd4af28555fcf200f17d2ab3dcbea03cfe",
  "source_text_sha256": "05b381d2458457e7f12195191b15e1cd4af28555fcf200f17d2ab3dcbea03cfe",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aae1cc",
        "00aae2d3"
      ],
      [
        "00aae2f8",
        "00aae2fb"
      ]
    ],
    "bytes_sha256": "bb545ee0074a4811b2e93ad4455bb0127db2cd2bfeba1978fad2717e18fbacfb",
    "instruction_count": 67,
    "instruction_bytes": 268,
    "body_bytes": 268,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00aa78e0](../00aa7/00aa78e0.md)
- [00aa84a4](../00aa8/00aa84a4.md)

## 呼び出し先

- [0043bb20](../0043b/0043bb20.md)
- [0043bba4](../0043b/0043bba4.md)
- [00aae2fc](../00aae/00aae2fc.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57ee0](../00c57/00c57ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2336 bytes

~~~c

undefined8 * FUN_00aae1cc(long *param_1,undefined8 param_2,undefined8 param_3,undefined4 *param_4)

{
  byte bVar1;
  long lVar2;
  undefined8 *puVar3;
  undefined8 uVar4;
  undefined8 *puVar5;
  undefined8 *puVar6;
  undefined8 uVar7;
  undefined1 auStack_70 [8];
  undefined8 local_68;
  undefined8 *local_60;
  long *plStack_58;
  undefined1 local_50;
  long local_48;
  
  lVar2 = tpidr_el0;
  local_48 = *(long *)(lVar2 + 0x28);
  puVar3 = (undefined8 *)FUN_00aae2fc(param_1,param_2,&local_68,auStack_70,param_3);
  puVar6 = (undefined8 *)*puVar3;
  if (puVar6 == (undefined8 *)0x0) {
    puVar6 = (undefined8 *)_Znwm(0x40);
    bVar1 = *(byte *)(param_4 + 2);
    local_50 = 0;
    *(undefined4 *)(puVar6 + 4) = *param_4;
                    /* catch() { ... } // from try @ 00aae18c with catch @ 00aae244 */
    local_60 = puVar6;
    plStack_58 = param_1 + 1;
    if ((bVar1 & 1) == 0) {
      uVar7 = *(undefined8 *)(param_4 + 2);
      uVar4 = *(undefined8 *)(param_4 + 6);
      puVar6[6] = *(undefined8 *)(param_4 + 4);
      puVar6[5] = uVar7;
      puVar6[7] = uVar4;
    }
    else {
      FUN_0043bb20(puVar6 + 5,*(undefined8 *)(param_4 + 6),*(undefined8 *)(param_4 + 4));
    }
                    /* try { // try from 00aae26c to 00bae2db has its CatchHandler @ 00aae26c
                       catch() { ... } // from try @ 00aae26c with catch @ 00aae26c
                       catch() { ... } // from try @ 00aae330 with catch @ 00aae26c
                       catch() { ... } // from try @ 00aae39c with catch @ 00aae26c
                       catch() { ... } // from try @ 00aae44c with catch @ 00aae26c
                       catch() { ... } // from try @ 00aae5a0 with catch @ 00aae26c */
    *puVar6 = 0;
    puVar6[1] = 0;
    puVar6[2] = local_68;
    *puVar3 = puVar6;
    puVar5 = puVar6;
    if (*(long *)*param_1 != 0) {
      *param_1 = *(long *)*param_1;
      puVar5 = (undefined8 *)*puVar3;
    }
    puVar3 = (undefined8 *)FUN_0043bba4(param_1[1],puVar5);
    uVar4 = 1;
    param_1[2] = param_1[2] + 1;
  }
  else {
    uVar4 = 0;
  }
  if (*(long *)(lVar2 + 0x28) == local_48) {
    return puVar6;
  }
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00aae2f8 to 00bae303 has its CatchHandler @ 00aae8d4 */
  __stack_chk_fail(puVar3,uVar4);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aae1cc"></a> `00aae1cc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00aae1d0"></a> `00aae1d0` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aae1d4"></a> `00aae1d4` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aae1d8"></a> `00aae1d8` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aae1dc"></a> `00aae1dc` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aae1e0"></a> `00aae1e0` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aae1e4"></a> `00aae1e4` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aae1e8"></a> `00aae1e8` | `f5 03 03 aa` | mov x21,x3 | `FALL_THROUGH`
<a id="insn-00aae1ec"></a> `00aae1ec` | `e4 03 02 aa` | mov x4,x2 | `FALL_THROUGH`
<a id="insn-00aae1f0"></a> `00aae1f0` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00aae1f4"></a> `00aae1f4` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aae1f8"></a> `00aae1f8` | `e3 03 00 91` | mov x3,sp | `FALL_THROUGH`
<a id="insn-00aae1fc"></a> `00aae1fc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aae200"></a> `00aae200` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aae204"></a> `00aae204` | `3e 00 00 94` | bl 0x00aae2fc | `UNCONDITIONAL_CALL`
<a id="insn-00aae208"></a> `00aae208` | `14 00 40 f9` | ldr x20,[x0] | `FALL_THROUGH`
<a id="insn-00aae20c"></a> `00aae20c` | `74 00 00 b4` | cbz x20,0x00aae218 | `CONDITIONAL_JUMP`
<a id="insn-00aae210"></a> `00aae210` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00aae214"></a> `00aae214` | `25 00 00 14` | b 0x00aae2a8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aae218"></a> `00aae218` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00aae21c"></a> `00aae21c` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00aae220"></a> `00aae220` | `78 22 00 91` | add x24,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aae224"></a> `00aae224` | `1b a7 06 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00aae228"></a> `00aae228` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00aae22c"></a> `00aae22c` | `a9 02 40 b9` | ldr w9,[x21] | `FALL_THROUGH`
<a id="insn-00aae230"></a> `00aae230` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aae234"></a> `00aae234` | `0a 8d 40 38` | ldrb w10,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00aae238"></a> `00aae238` | `e0 63 01 a9` | stp x0,x24,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aae23c"></a> `00aae23c` | `ff 83 00 39` | strb wzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aae240"></a> `00aae240` | `09 20 00 b9` | str w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00aae244"></a> `00aae244` | `ca 00 00 37` | tbnz w10,#0x0,0x00aae25c | `CONDITIONAL_JUMP`
<a id="insn-00aae248"></a> `00aae248` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00aae24c"></a> `00aae24c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aae250"></a> `00aae250` | `80 82 82 3c` | stur q0,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aae254"></a> `00aae254` | `88 82 03 f8` | stur x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00aae258"></a> `00aae258` | `04 00 00 14` | b 0x00aae268 | `UNCONDITIONAL_JUMP`
<a id="insn-00aae25c"></a> `00aae25c` | `a2 06 41 a9` | ldp x2,x1,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00aae260"></a> `00aae260` | `80 a2 00 91` | add x0,x20,#0x28 | `FALL_THROUGH`
<a id="insn-00aae264"></a> `00aae264` | `2f 36 e6 97` | bl 0x0043bb20 | `UNCONDITIONAL_CALL`
<a id="insn-00aae268"></a> `00aae268` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aae26c"></a> `00aae26c` | `9f 7e 00 a9` | stp xzr,xzr,[x20] | `FALL_THROUGH`
<a id="insn-00aae270"></a> `00aae270` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00aae274"></a> `00aae274` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00aae278"></a> `00aae278` | `f4 02 00 f9` | str x20,[x23] | `FALL_THROUGH`
<a id="insn-00aae27c"></a> `00aae27c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aae280"></a> `00aae280` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aae284"></a> `00aae284` | `68 00 00 b4` | cbz x8,0x00aae290 | `CONDITIONAL_JUMP`
<a id="insn-00aae288"></a> `00aae288` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00aae28c"></a> `00aae28c` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-00aae290"></a> `00aae290` | `60 06 40 f9` | ldr x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00aae294"></a> `00aae294` | `44 36 e6 97` | bl 0x0043bba4 | `UNCONDITIONAL_CALL`
<a id="insn-00aae298"></a> `00aae298` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aae29c"></a> `00aae29c` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aae2a0"></a> `00aae2a0` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aae2a4"></a> `00aae2a4` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aae2a8"></a> `00aae2a8` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00aae2ac"></a> `00aae2ac` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aae2b0"></a> `00aae2b0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aae2b4"></a> `00aae2b4` | `21 02 00 54` | b.ne 0x00aae2f8 | `CONDITIONAL_JUMP`
<a id="insn-00aae2b8"></a> `00aae2b8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aae2bc"></a> `00aae2bc` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aae2c0"></a> `00aae2c0` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aae2c4"></a> `00aae2c4` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aae2c8"></a> `00aae2c8` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aae2cc"></a> `00aae2cc` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00aae2d0"></a> `00aae2d0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aae2f8"></a> `00aae2f8` | `fa a6 06 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aae1cc`](#insn-00aae1cc) 範囲 `[['00aae1cc', '00aae20f']]`
  - `CONDITIONAL_JUMP` [`00aae20c`](#insn-00aae20c) → [`00aae218`](#insn-00aae218)
  - `FALL_THROUGH` [`00aae20c`](#insn-00aae20c) → [`00aae210`](#insn-00aae210)
- ブロック [`00aae210`](#insn-00aae210) 範囲 `[['00aae210', '00aae217']]`
  - `UNCONDITIONAL_JUMP` [`00aae214`](#insn-00aae214) → [`00aae2a8`](#insn-00aae2a8)
- ブロック [`00aae218`](#insn-00aae218) 範囲 `[['00aae218', '00aae243']]`
  - `FALL_THROUGH` [`00aae240`](#insn-00aae240) → [`00aae244`](#insn-00aae244)
- ブロック [`00aae244`](#insn-00aae244) 範囲 `[['00aae244', '00aae247']]`
  - `CONDITIONAL_JUMP` [`00aae244`](#insn-00aae244) → [`00aae25c`](#insn-00aae25c)
  - `FALL_THROUGH` [`00aae244`](#insn-00aae244) → [`00aae248`](#insn-00aae248)
- ブロック [`00aae248`](#insn-00aae248) 範囲 `[['00aae248', '00aae25b']]`
  - `UNCONDITIONAL_JUMP` [`00aae258`](#insn-00aae258) → [`00aae268`](#insn-00aae268)
- ブロック [`00aae25c`](#insn-00aae25c) 範囲 `[['00aae25c', '00aae267']]`
  - `FALL_THROUGH` [`00aae264`](#insn-00aae264) → [`00aae268`](#insn-00aae268)
- ブロック [`00aae268`](#insn-00aae268) 範囲 `[['00aae268', '00aae26b']]`
  - `FALL_THROUGH` [`00aae268`](#insn-00aae268) → [`00aae26c`](#insn-00aae26c)
- ブロック [`00aae26c`](#insn-00aae26c) 範囲 `[['00aae26c', '00aae287']]`
  - `CONDITIONAL_JUMP` [`00aae284`](#insn-00aae284) → [`00aae290`](#insn-00aae290)
  - `FALL_THROUGH` [`00aae284`](#insn-00aae284) → [`00aae288`](#insn-00aae288)
- ブロック [`00aae288`](#insn-00aae288) 範囲 `[['00aae288', '00aae28f']]`
  - `FALL_THROUGH` [`00aae28c`](#insn-00aae28c) → [`00aae290`](#insn-00aae290)
- ブロック [`00aae290`](#insn-00aae290) 範囲 `[['00aae290', '00aae2a7']]`
  - `FALL_THROUGH` [`00aae2a4`](#insn-00aae2a4) → [`00aae2a8`](#insn-00aae2a8)
- ブロック [`00aae2a8`](#insn-00aae2a8) 範囲 `[['00aae2a8', '00aae2b7']]`
  - `CONDITIONAL_JUMP` [`00aae2b4`](#insn-00aae2b4) → [`00aae2f8`](#insn-00aae2f8)
  - `FALL_THROUGH` [`00aae2b4`](#insn-00aae2b4) → [`00aae2b8`](#insn-00aae2b8)
- ブロック [`00aae2b8`](#insn-00aae2b8) 範囲 `[['00aae2b8', '00aae2d3']]`
- ブロック [`00aae2f8`](#insn-00aae2f8) 範囲 `[['00aae2f8', '00aae2fb']]`

## 命令位置別の参照

- [`00aae1d0`](#insn-00aae1d0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae1d4`](#insn-00aae1d4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae1d8`](#insn-00aae1d8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae1dc`](#insn-00aae1dc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae200`](#insn-00aae200) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae204`](#insn-00aae204) → [`00aae2fc`](00aae2fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aae2fc` · 推定シンボル `None` · 推定型 `None`
- [`00aae20c`](#insn-00aae20c) → [`00aae218`](#insn-00aae218) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae214`](#insn-00aae214) → [`00aae2a8`](#insn-00aae2a8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae224`](#insn-00aae224) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00aae238`](#insn-00aae238) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae23c`](#insn-00aae23c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae244`](#insn-00aae244) → [`00aae25c`](#insn-00aae25c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae258`](#insn-00aae258) → [`00aae268`](#insn-00aae268) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae264`](#insn-00aae264) → [`0043bb20`](../0043b/0043bb20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb20` · 推定シンボル `None` · 推定型 `None`
- [`00aae268`](#insn-00aae268) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae284`](#insn-00aae284) → [`00aae290`](#insn-00aae290) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae294`](#insn-00aae294) → [`0043bba4`](../0043b/0043bba4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bba4` · 推定シンボル `None` · 推定型 `None`
- [`00aae2ac`](#insn-00aae2ac) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae2b4`](#insn-00aae2b4) → [`00aae2f8`](#insn-00aae2f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae2bc`](#insn-00aae2bc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae2c0`](#insn-00aae2c0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae2c4`](#insn-00aae2c4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae2c8`](#insn-00aae2c8) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae2f8`](#insn-00aae2f8) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aae1d0`](#insn-00aae1d0)

~~~json
{
  "source": "00aae1d0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae1d4`](#insn-00aae1d4)

~~~json
{
  "source": "00aae1d4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae1d8`](#insn-00aae1d8)

~~~json
{
  "source": "00aae1d8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae1dc`](#insn-00aae1dc)

~~~json
{
  "source": "00aae1dc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae200`](#insn-00aae200)

~~~json
{
  "source": "00aae200",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae204`](#insn-00aae204)

~~~json
{
  "source": "00aae204",
  "target": "00aae2fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae20c`](#insn-00aae20c)

~~~json
{
  "source": "00aae20c",
  "target": "00aae218",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae214`](#insn-00aae214)

~~~json
{
  "source": "00aae214",
  "target": "00aae2a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae224`](#insn-00aae224)

~~~json
{
  "source": "00aae224",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae238`](#insn-00aae238)

~~~json
{
  "source": "00aae238",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae23c`](#insn-00aae23c)

~~~json
{
  "source": "00aae23c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae244`](#insn-00aae244)

~~~json
{
  "source": "00aae244",
  "target": "00aae25c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae258`](#insn-00aae258)

~~~json
{
  "source": "00aae258",
  "target": "00aae268",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae264`](#insn-00aae264)

~~~json
{
  "source": "00aae264",
  "target": "0043bb20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae268`](#insn-00aae268)

~~~json
{
  "source": "00aae268",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae284`](#insn-00aae284)

~~~json
{
  "source": "00aae284",
  "target": "00aae290",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae294`](#insn-00aae294)

~~~json
{
  "source": "00aae294",
  "target": "0043bba4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae2ac`](#insn-00aae2ac)

~~~json
{
  "source": "00aae2ac",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae2b4`](#insn-00aae2b4)

~~~json
{
  "source": "00aae2b4",
  "target": "00aae2f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae2bc`](#insn-00aae2bc)

~~~json
{
  "source": "00aae2bc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae2c0`](#insn-00aae2c0)

~~~json
{
  "source": "00aae2c0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae2c4`](#insn-00aae2c4)

~~~json
{
  "source": "00aae2c4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae2c8`](#insn-00aae2c8)

~~~json
{
  "source": "00aae2c8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae2f8`](#insn-00aae2f8)

~~~json
{
  "source": "00aae2f8",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
