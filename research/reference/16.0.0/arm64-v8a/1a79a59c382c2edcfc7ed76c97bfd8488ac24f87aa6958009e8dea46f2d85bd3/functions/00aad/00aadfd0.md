# 00aadfd0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a4ffac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4ffac.md) · 移動量 `+0x5e024`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0052.md#compare-91132e8be2cba8f477c9a18616273c6f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aae1cc`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aae/00aae1cc.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-82b7d888aa33a47b035d27c736273bd5)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aadfd0",
  "name": "FUN_00aadfd0",
  "size": 268,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4bcc36f1cf5a4b7d1dc7a01680c5248d1f6f7989b02d86ff9c538f8c7031d28f",
  "source_text_sha256": "4bcc36f1cf5a4b7d1dc7a01680c5248d1f6f7989b02d86ff9c538f8c7031d28f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aadfd0",
        "00aae0d7"
      ],
      [
        "00aae0fc",
        "00aae0ff"
      ]
    ],
    "bytes_sha256": "795d864f9a289e3aeddec56a6d482f6128a7f48dd54ff875935424db89c57d8c",
    "instruction_count": 67,
    "instruction_bytes": 268,
    "body_bytes": 268,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00aa76e4](../00aa7/00aa76e4.md)
- [00aa82a8](../00aa8/00aa82a8.md)

## 呼び出し先

- [0043bae0](../0043b/0043bae0.md)
- [0043bb64](../0043b/0043bb64.md)
- [00aae100](../00aae/00aae100.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ae0](../00c57/00c57ae0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2433 bytes

~~~c

undefined8 * FUN_00aadfd0(long *param_1,undefined8 param_2,undefined8 param_3,undefined4 *param_4)

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
                    /* try { // try from 00aadff0 to 00badff7 has its CatchHandler @ 00aae0a8 */
  local_48 = *(long *)(lVar2 + 0x28);
                    /* try { // try from 00aadff8 to 00bae0cf has its CatchHandler @ 00aadf94 */
  puVar3 = (undefined8 *)FUN_00aae100(param_1,param_2,&local_68,auStack_70,param_3);
  puVar6 = (undefined8 *)*puVar3;
  if (puVar6 == (undefined8 *)0x0) {
    puVar6 = (undefined8 *)_Znwm(0x40);
    bVar1 = *(byte *)(param_4 + 2);
    local_50 = 0;
    *(undefined4 *)(puVar6 + 4) = *param_4;
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
      FUN_0043bae0(puVar6 + 5,*(undefined8 *)(param_4 + 6),*(undefined8 *)(param_4 + 4));
    }
    *puVar6 = 0;
    puVar6[1] = 0;
    puVar6[2] = local_68;
    *puVar3 = puVar6;
    puVar5 = puVar6;
    if (*(long *)*param_1 != 0) {
      *param_1 = *(long *)*param_1;
      puVar5 = (undefined8 *)*puVar3;
    }
    puVar3 = (undefined8 *)FUN_0043bb64(param_1[1],puVar5);
    uVar4 = 1;
                    /* catch() { ... } // from try @ 00aadff0 with catch @ 00aae0a8 */
    param_1[2] = param_1[2] + 1;
  }
  else {
    uVar4 = 0;
  }
  if (*(long *)(lVar2 + 0x28) == local_48) {
                    /* try { // try from 00aae0d0 to 00bae13f has its CatchHandler @ 00aae0d0
                       catch() { ... } // from try @ 00aae0d0 with catch @ 00aae0d0
                       catch() { ... } // from try @ 00aae194 with catch @ 00aae0d0
                       catch() { ... } // from try @ 00aae200 with catch @ 00aae0d0
                       catch() { ... } // from try @ 00aae2b0 with catch @ 00aae0d0
                       catch() { ... } // from try @ 00aae404 with catch @ 00aae0d0 */
    return puVar6;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(puVar3,uVar4);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aadfd0"></a> `00aadfd0` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00aadfd4"></a> `00aadfd4` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aadfd8"></a> `00aadfd8` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aadfdc"></a> `00aadfdc` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aadfe0"></a> `00aadfe0` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aadfe4"></a> `00aadfe4` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aadfe8"></a> `00aadfe8` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aadfec"></a> `00aadfec` | `f5 03 03 aa` | mov x21,x3 | `FALL_THROUGH`
<a id="insn-00aadff0"></a> `00aadff0` | `e4 03 02 aa` | mov x4,x2 | `FALL_THROUGH`
<a id="insn-00aadff4"></a> `00aadff4` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00aadff8"></a> `00aadff8` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aadffc"></a> `00aadffc` | `e3 03 00 91` | mov x3,sp | `FALL_THROUGH`
<a id="insn-00aae000"></a> `00aae000` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aae004"></a> `00aae004` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aae008"></a> `00aae008` | `3e 00 00 94` | bl 0x00aae100 | `UNCONDITIONAL_CALL`
<a id="insn-00aae00c"></a> `00aae00c` | `14 00 40 f9` | ldr x20,[x0] | `FALL_THROUGH`
<a id="insn-00aae010"></a> `00aae010` | `74 00 00 b4` | cbz x20,0x00aae01c | `CONDITIONAL_JUMP`
<a id="insn-00aae014"></a> `00aae014` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00aae018"></a> `00aae018` | `25 00 00 14` | b 0x00aae0ac | `UNCONDITIONAL_JUMP`
<a id="insn-00aae01c"></a> `00aae01c` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00aae020"></a> `00aae020` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00aae024"></a> `00aae024` | `78 22 00 91` | add x24,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aae028"></a> `00aae028` | `9a a6 06 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00aae02c"></a> `00aae02c` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00aae030"></a> `00aae030` | `a9 02 40 b9` | ldr w9,[x21] | `FALL_THROUGH`
<a id="insn-00aae034"></a> `00aae034` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aae038"></a> `00aae038` | `0a 8d 40 38` | ldrb w10,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00aae03c"></a> `00aae03c` | `e0 63 01 a9` | stp x0,x24,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aae040"></a> `00aae040` | `ff 83 00 39` | strb wzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aae044"></a> `00aae044` | `09 20 00 b9` | str w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00aae048"></a> `00aae048` | `ca 00 00 37` | tbnz w10,#0x0,0x00aae060 | `CONDITIONAL_JUMP`
<a id="insn-00aae04c"></a> `00aae04c` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00aae050"></a> `00aae050` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aae054"></a> `00aae054` | `80 82 82 3c` | stur q0,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aae058"></a> `00aae058` | `88 82 03 f8` | stur x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00aae05c"></a> `00aae05c` | `04 00 00 14` | b 0x00aae06c | `UNCONDITIONAL_JUMP`
<a id="insn-00aae060"></a> `00aae060` | `a2 06 41 a9` | ldp x2,x1,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00aae064"></a> `00aae064` | `80 a2 00 91` | add x0,x20,#0x28 | `FALL_THROUGH`
<a id="insn-00aae068"></a> `00aae068` | `9e 36 e6 97` | bl 0x0043bae0 | `UNCONDITIONAL_CALL`
<a id="insn-00aae06c"></a> `00aae06c` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aae070"></a> `00aae070` | `9f 7e 00 a9` | stp xzr,xzr,[x20] | `FALL_THROUGH`
<a id="insn-00aae074"></a> `00aae074` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00aae078"></a> `00aae078` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00aae07c"></a> `00aae07c` | `f4 02 00 f9` | str x20,[x23] | `FALL_THROUGH`
<a id="insn-00aae080"></a> `00aae080` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aae084"></a> `00aae084` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aae088"></a> `00aae088` | `68 00 00 b4` | cbz x8,0x00aae094 | `CONDITIONAL_JUMP`
<a id="insn-00aae08c"></a> `00aae08c` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00aae090"></a> `00aae090` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-00aae094"></a> `00aae094` | `60 06 40 f9` | ldr x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00aae098"></a> `00aae098` | `b3 36 e6 97` | bl 0x0043bb64 | `UNCONDITIONAL_CALL`
<a id="insn-00aae09c"></a> `00aae09c` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aae0a0"></a> `00aae0a0` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aae0a4"></a> `00aae0a4` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aae0a8"></a> `00aae0a8` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aae0ac"></a> `00aae0ac` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00aae0b0"></a> `00aae0b0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aae0b4"></a> `00aae0b4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aae0b8"></a> `00aae0b8` | `21 02 00 54` | b.ne 0x00aae0fc | `CONDITIONAL_JUMP`
<a id="insn-00aae0bc"></a> `00aae0bc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aae0c0"></a> `00aae0c0` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aae0c4"></a> `00aae0c4` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aae0c8"></a> `00aae0c8` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aae0cc"></a> `00aae0cc` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aae0d0"></a> `00aae0d0` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00aae0d4"></a> `00aae0d4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aae0fc"></a> `00aae0fc` | `79 a6 06 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aadfd0`](#insn-00aadfd0) 範囲 `[['00aadfd0', '00aadfef']]`
  - `FALL_THROUGH` [`00aadfec`](#insn-00aadfec) → [`00aadff0`](#insn-00aadff0)
- ブロック [`00aadff0`](#insn-00aadff0) 範囲 `[['00aadff0', '00aadff7']]`
  - `FALL_THROUGH` [`00aadff4`](#insn-00aadff4) → [`00aadff8`](#insn-00aadff8)
- ブロック [`00aadff8`](#insn-00aadff8) 範囲 `[['00aadff8', '00aae013']]`
  - `CONDITIONAL_JUMP` [`00aae010`](#insn-00aae010) → [`00aae01c`](#insn-00aae01c)
  - `FALL_THROUGH` [`00aae010`](#insn-00aae010) → [`00aae014`](#insn-00aae014)
- ブロック [`00aae014`](#insn-00aae014) 範囲 `[['00aae014', '00aae01b']]`
  - `UNCONDITIONAL_JUMP` [`00aae018`](#insn-00aae018) → [`00aae0ac`](#insn-00aae0ac)
- ブロック [`00aae01c`](#insn-00aae01c) 範囲 `[['00aae01c', '00aae04b']]`
  - `CONDITIONAL_JUMP` [`00aae048`](#insn-00aae048) → [`00aae060`](#insn-00aae060)
  - `FALL_THROUGH` [`00aae048`](#insn-00aae048) → [`00aae04c`](#insn-00aae04c)
- ブロック [`00aae04c`](#insn-00aae04c) 範囲 `[['00aae04c', '00aae05f']]`
  - `UNCONDITIONAL_JUMP` [`00aae05c`](#insn-00aae05c) → [`00aae06c`](#insn-00aae06c)
- ブロック [`00aae060`](#insn-00aae060) 範囲 `[['00aae060', '00aae06b']]`
  - `FALL_THROUGH` [`00aae068`](#insn-00aae068) → [`00aae06c`](#insn-00aae06c)
- ブロック [`00aae06c`](#insn-00aae06c) 範囲 `[['00aae06c', '00aae08b']]`
  - `CONDITIONAL_JUMP` [`00aae088`](#insn-00aae088) → [`00aae094`](#insn-00aae094)
  - `FALL_THROUGH` [`00aae088`](#insn-00aae088) → [`00aae08c`](#insn-00aae08c)
- ブロック [`00aae08c`](#insn-00aae08c) 範囲 `[['00aae08c', '00aae093']]`
  - `FALL_THROUGH` [`00aae090`](#insn-00aae090) → [`00aae094`](#insn-00aae094)
- ブロック [`00aae094`](#insn-00aae094) 範囲 `[['00aae094', '00aae0a7']]`
  - `FALL_THROUGH` [`00aae0a4`](#insn-00aae0a4) → [`00aae0a8`](#insn-00aae0a8)
- ブロック [`00aae0a8`](#insn-00aae0a8) 範囲 `[['00aae0a8', '00aae0ab']]`
  - `FALL_THROUGH` [`00aae0a8`](#insn-00aae0a8) → [`00aae0ac`](#insn-00aae0ac)
- ブロック [`00aae0ac`](#insn-00aae0ac) 範囲 `[['00aae0ac', '00aae0bb']]`
  - `CONDITIONAL_JUMP` [`00aae0b8`](#insn-00aae0b8) → [`00aae0fc`](#insn-00aae0fc)
  - `FALL_THROUGH` [`00aae0b8`](#insn-00aae0b8) → [`00aae0bc`](#insn-00aae0bc)
- ブロック [`00aae0bc`](#insn-00aae0bc) 範囲 `[['00aae0bc', '00aae0cf']]`
  - `FALL_THROUGH` [`00aae0cc`](#insn-00aae0cc) → [`00aae0d0`](#insn-00aae0d0)
- ブロック [`00aae0d0`](#insn-00aae0d0) 範囲 `[['00aae0d0', '00aae0d7']]`
- ブロック [`00aae0fc`](#insn-00aae0fc) 範囲 `[['00aae0fc', '00aae0ff']]`

## 命令位置別の参照

- [`00aadfd4`](#insn-00aadfd4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadfd8`](#insn-00aadfd8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadfdc`](#insn-00aadfdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aadfe0`](#insn-00aadfe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae004`](#insn-00aae004) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae008`](#insn-00aae008) → [`00aae100`](../00aae/00aae100.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aae100` · 推定シンボル `None` · 推定型 `None`
- [`00aae010`](#insn-00aae010) → [`00aae01c`](#insn-00aae01c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae018`](#insn-00aae018) → [`00aae0ac`](#insn-00aae0ac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae028`](#insn-00aae028) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00aae03c`](#insn-00aae03c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae040`](#insn-00aae040) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae048`](#insn-00aae048) → [`00aae060`](#insn-00aae060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae05c`](#insn-00aae05c) → [`00aae06c`](#insn-00aae06c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae068`](#insn-00aae068) → [`0043bae0`](../0043b/0043bae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bae0` · 推定シンボル `None` · 推定型 `None`
- [`00aae06c`](#insn-00aae06c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae088`](#insn-00aae088) → [`00aae094`](#insn-00aae094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae098`](#insn-00aae098) → [`0043bb64`](../0043b/0043bb64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb64` · 推定シンボル `None` · 推定型 `None`
- [`00aae0b0`](#insn-00aae0b0) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae0b8`](#insn-00aae0b8) → [`00aae0fc`](#insn-00aae0fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae0c0`](#insn-00aae0c0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae0c4`](#insn-00aae0c4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae0c8`](#insn-00aae0c8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae0cc`](#insn-00aae0cc) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aae0fc`](#insn-00aae0fc) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aadfd4`](#insn-00aadfd4)

~~~json
{
  "source": "00aadfd4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadfd8`](#insn-00aadfd8)

~~~json
{
  "source": "00aadfd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadfdc`](#insn-00aadfdc)

~~~json
{
  "source": "00aadfdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aadfe0`](#insn-00aadfe0)

~~~json
{
  "source": "00aadfe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae004`](#insn-00aae004)

~~~json
{
  "source": "00aae004",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae008`](#insn-00aae008)

~~~json
{
  "source": "00aae008",
  "target": "00aae100",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae010`](#insn-00aae010)

~~~json
{
  "source": "00aae010",
  "target": "00aae01c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae018`](#insn-00aae018)

~~~json
{
  "source": "00aae018",
  "target": "00aae0ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae028`](#insn-00aae028)

~~~json
{
  "source": "00aae028",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae03c`](#insn-00aae03c)

~~~json
{
  "source": "00aae03c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae040`](#insn-00aae040)

~~~json
{
  "source": "00aae040",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae048`](#insn-00aae048)

~~~json
{
  "source": "00aae048",
  "target": "00aae060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae05c`](#insn-00aae05c)

~~~json
{
  "source": "00aae05c",
  "target": "00aae06c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae068`](#insn-00aae068)

~~~json
{
  "source": "00aae068",
  "target": "0043bae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae06c`](#insn-00aae06c)

~~~json
{
  "source": "00aae06c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae088`](#insn-00aae088)

~~~json
{
  "source": "00aae088",
  "target": "00aae094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae098`](#insn-00aae098)

~~~json
{
  "source": "00aae098",
  "target": "0043bb64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aae0b0`](#insn-00aae0b0)

~~~json
{
  "source": "00aae0b0",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae0b8`](#insn-00aae0b8)

~~~json
{
  "source": "00aae0b8",
  "target": "00aae0fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae0c0`](#insn-00aae0c0)

~~~json
{
  "source": "00aae0c0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae0c4`](#insn-00aae0c4)

~~~json
{
  "source": "00aae0c4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae0c8`](#insn-00aae0c8)

~~~json
{
  "source": "00aae0c8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae0cc`](#insn-00aae0cc)

~~~json
{
  "source": "00aae0cc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aae0fc`](#insn-00aae0fc)

~~~json
{
  "source": "00aae0fc",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
