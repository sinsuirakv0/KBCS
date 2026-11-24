# 00b3affc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b3abd4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3abd4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0007.md#compare-09acd760a7a8fe178e3d1eccfcd3bb98)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0043.md#review-a25f1c9528bffc14a280f8101732eb9f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b3affc",
  "name": "FUN_00b3affc",
  "size": 176,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "16e3c1ea25b4784a3377ba6f42321a2e9750c75f17af8706fac2732f65183eb5",
  "source_text_sha256": "16e3c1ea25b4784a3377ba6f42321a2e9750c75f17af8706fac2732f65183eb5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b3affc",
        "00b3b0ab"
      ]
    ],
    "bytes_sha256": "f67b401a96e646db71c96dfd305dc5a4ecb8bc2d5a35e07c84fb910cf78f6366",
    "instruction_count": 44,
    "instruction_bytes": 176,
    "body_bytes": 176,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00b38f10](../00b38/00b38f10.md)
- [00b3affc](../00b3a/00b3affc.md)

## 呼び出し先

- [00b3affc](../00b3a/00b3affc.md)
- [00c57eb0](../00c57/00c57eb0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2023 bytes

~~~c

void FUN_00b3affc(undefined8 param_1,undefined8 *param_2)

{
  long *plVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  
  if (param_2 == (undefined8 *)0x0) {
    return;
  }
  FUN_00b3affc(param_1,*param_2);
  FUN_00b3affc(param_1,param_2[1]);
                    /* try { // try from 00b3b028 to 00c3b02f has its CatchHandler @ 00b3b034 */
  plVar1 = (long *)param_2[0x12];
  plVar2 = param_2 + 0xe;
                    /* catch() { ... } // from try @ 00b3ad80 with catch @ 00b3b030
                       try { // try from 00b3b030 to 00c3b0bb has its CatchHandler @ 00b3aac8 */
  plVar3 = param_2 + 8;
                    /* catch() { ... } // from try @ 00b3b028 with catch @ 00b3b034 */
  if (plVar1 == plVar2) {
                    /* catch() { ... } // from try @ 00b3ad8c with catch @ 00b3b04c */
    lVar4 = 0x20;
LAB_00b3b054:
    (**(code **)(*plVar2 + lVar4))();
  }
  else if (plVar1 != (long *)0x0) {
    lVar4 = 0x28;
    plVar2 = plVar1;
    goto LAB_00b3b054;
  }
                    /* catch() { ... } // from try @ 00b3af80 with catch @ 00b3b060 */
  plVar2 = (long *)param_2[0xc];
  if (plVar2 == plVar3) {
                    /* catch() { ... } // from try @ 00b3af6c with catch @ 00b3b078 */
    lVar4 = 0x20;
                    /* catch() { ... } // from try @ 00b3acc8 with catch @ 00b3b07c */
  }
  else {
    if (plVar2 == (long *)0x0) goto LAB_00b3b08c;
    lVar4 = 0x28;
    plVar3 = plVar2;
  }
                    /* catch() { ... } // from try @ 00b3ac84 with catch @ 00b3b080 */
                    /* catch() { ... } // from try @ 00b3ab58 with catch @ 00b3b084 */
                    /* catch() { ... } // from try @ 00b3acdc with catch @ 00b3b088
                       catch() { ... } // from try @ 00b3ae84 with catch @ 00b3b088
                       catch() { ... } // from try @ 00b3afb4 with catch @ 00b3b088 */
  (**(code **)(*plVar3 + lVar4))();
LAB_00b3b08c:
  if ((*(byte *)(param_2 + 4) & 1) != 0) {
    _ZdlPv((void *)param_2[6]);
  }
  _ZdlPv(param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b3affc"></a> `00b3affc` | `61 02 00 b4` | cbz x1,0x00b3b048 | `CONDITIONAL_JUMP`
<a id="insn-00b3b000"></a> `00b3b000` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b3b004"></a> `00b3b004` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b3b008"></a> `00b3b008` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00b3b00c"></a> `00b3b00c` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00b3b010"></a> `00b3b010` | `21 00 40 f9` | ldr x1,[x1] | `FALL_THROUGH`
<a id="insn-00b3b014"></a> `00b3b014` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b3b018"></a> `00b3b018` | `f9 ff ff 97` | bl 0x00b3affc | `UNCONDITIONAL_CALL`
<a id="insn-00b3b01c"></a> `00b3b01c` | `61 06 40 f9` | ldr x1,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b3b020"></a> `00b3b020` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b3b024"></a> `00b3b024` | `f6 ff ff 97` | bl 0x00b3affc | `UNCONDITIONAL_CALL`
<a id="insn-00b3b028"></a> `00b3b028` | `60 4a 40 f9` | ldr x0,[x19, #0x90] | `FALL_THROUGH`
<a id="insn-00b3b02c"></a> `00b3b02c` | `69 c2 01 91` | add x9,x19,#0x70 | `FALL_THROUGH`
<a id="insn-00b3b030"></a> `00b3b030` | `74 02 01 91` | add x20,x19,#0x40 | `FALL_THROUGH`
<a id="insn-00b3b034"></a> `00b3b034` | `1f 00 09 eb` | cmp x0,x9 | `FALL_THROUGH`
<a id="insn-00b3b038"></a> `00b3b038` | `a0 00 00 54` | b.eq 0x00b3b04c | `CONDITIONAL_JUMP`
<a id="insn-00b3b03c"></a> `00b3b03c` | `20 01 00 b4` | cbz x0,0x00b3b060 | `CONDITIONAL_JUMP`
<a id="insn-00b3b040"></a> `00b3b040` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00b3b044"></a> `00b3b044` | `04 00 00 14` | b 0x00b3b054 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3b048"></a> `00b3b048` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b3b04c"></a> `00b3b04c` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00b3b050"></a> `00b3b050` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-00b3b054"></a> `00b3b054` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00b3b058"></a> `00b3b058` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b3b05c"></a> `00b3b05c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b3b060"></a> `00b3b060` | `60 32 40 f9` | ldr x0,[x19, #0x60] | `FALL_THROUGH`
<a id="insn-00b3b064"></a> `00b3b064` | `1f 00 14 eb` | cmp x0,x20 | `FALL_THROUGH`
<a id="insn-00b3b068"></a> `00b3b068` | `80 00 00 54` | b.eq 0x00b3b078 | `CONDITIONAL_JUMP`
<a id="insn-00b3b06c"></a> `00b3b06c` | `00 01 00 b4` | cbz x0,0x00b3b08c | `CONDITIONAL_JUMP`
<a id="insn-00b3b070"></a> `00b3b070` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00b3b074"></a> `00b3b074` | `03 00 00 14` | b 0x00b3b080 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3b078"></a> `00b3b078` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00b3b07c"></a> `00b3b07c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b3b080"></a> `00b3b080` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00b3b084"></a> `00b3b084` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b3b088"></a> `00b3b088` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b3b08c"></a> `00b3b08c` | `68 82 40 39` | ldrb w8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00b3b090"></a> `00b3b090` | `68 00 00 36` | tbz w8,#0x0,0x00b3b09c | `CONDITIONAL_JUMP`
<a id="insn-00b3b094"></a> `00b3b094` | `60 1a 40 f9` | ldr x0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b3b098"></a> `00b3b098` | `86 73 04 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00b3b09c"></a> `00b3b09c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b3b0a0"></a> `00b3b0a0` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b3b0a4"></a> `00b3b0a4` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b3b0a8"></a> `00b3b0a8` | `82 73 04 14` | b 0x00c57eb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b3affc`](#insn-00b3affc) 範囲 `[['00b3affc', '00b3afff']]`
  - `CONDITIONAL_JUMP` [`00b3affc`](#insn-00b3affc) → [`00b3b048`](#insn-00b3b048)
  - `FALL_THROUGH` [`00b3affc`](#insn-00b3affc) → [`00b3b000`](#insn-00b3b000)
- ブロック [`00b3b000`](#insn-00b3b000) 範囲 `[['00b3b000', '00b3b027']]`
  - `FALL_THROUGH` [`00b3b024`](#insn-00b3b024) → [`00b3b028`](#insn-00b3b028)
- ブロック [`00b3b028`](#insn-00b3b028) 範囲 `[['00b3b028', '00b3b02f']]`
  - `FALL_THROUGH` [`00b3b02c`](#insn-00b3b02c) → [`00b3b030`](#insn-00b3b030)
- ブロック [`00b3b030`](#insn-00b3b030) 範囲 `[['00b3b030', '00b3b033']]`
  - `FALL_THROUGH` [`00b3b030`](#insn-00b3b030) → [`00b3b034`](#insn-00b3b034)
- ブロック [`00b3b034`](#insn-00b3b034) 範囲 `[['00b3b034', '00b3b03b']]`
  - `CONDITIONAL_JUMP` [`00b3b038`](#insn-00b3b038) → [`00b3b04c`](#insn-00b3b04c)
  - `FALL_THROUGH` [`00b3b038`](#insn-00b3b038) → [`00b3b03c`](#insn-00b3b03c)
- ブロック [`00b3b03c`](#insn-00b3b03c) 範囲 `[['00b3b03c', '00b3b03f']]`
  - `CONDITIONAL_JUMP` [`00b3b03c`](#insn-00b3b03c) → [`00b3b060`](#insn-00b3b060)
  - `FALL_THROUGH` [`00b3b03c`](#insn-00b3b03c) → [`00b3b040`](#insn-00b3b040)
- ブロック [`00b3b040`](#insn-00b3b040) 範囲 `[['00b3b040', '00b3b047']]`
  - `UNCONDITIONAL_JUMP` [`00b3b044`](#insn-00b3b044) → [`00b3b054`](#insn-00b3b054)
- ブロック [`00b3b048`](#insn-00b3b048) 範囲 `[['00b3b048', '00b3b04b']]`
- ブロック [`00b3b04c`](#insn-00b3b04c) 範囲 `[['00b3b04c', '00b3b053']]`
  - `FALL_THROUGH` [`00b3b050`](#insn-00b3b050) → [`00b3b054`](#insn-00b3b054)
- ブロック [`00b3b054`](#insn-00b3b054) 範囲 `[['00b3b054', '00b3b05f']]`
  - `FALL_THROUGH` [`00b3b05c`](#insn-00b3b05c) → [`00b3b060`](#insn-00b3b060)
- ブロック [`00b3b060`](#insn-00b3b060) 範囲 `[['00b3b060', '00b3b06b']]`
  - `CONDITIONAL_JUMP` [`00b3b068`](#insn-00b3b068) → [`00b3b078`](#insn-00b3b078)
  - `FALL_THROUGH` [`00b3b068`](#insn-00b3b068) → [`00b3b06c`](#insn-00b3b06c)
- ブロック [`00b3b06c`](#insn-00b3b06c) 範囲 `[['00b3b06c', '00b3b06f']]`
  - `CONDITIONAL_JUMP` [`00b3b06c`](#insn-00b3b06c) → [`00b3b08c`](#insn-00b3b08c)
  - `FALL_THROUGH` [`00b3b06c`](#insn-00b3b06c) → [`00b3b070`](#insn-00b3b070)
- ブロック [`00b3b070`](#insn-00b3b070) 範囲 `[['00b3b070', '00b3b077']]`
  - `UNCONDITIONAL_JUMP` [`00b3b074`](#insn-00b3b074) → [`00b3b080`](#insn-00b3b080)
- ブロック [`00b3b078`](#insn-00b3b078) 範囲 `[['00b3b078', '00b3b07b']]`
  - `FALL_THROUGH` [`00b3b078`](#insn-00b3b078) → [`00b3b07c`](#insn-00b3b07c)
- ブロック [`00b3b07c`](#insn-00b3b07c) 範囲 `[['00b3b07c', '00b3b07f']]`
  - `FALL_THROUGH` [`00b3b07c`](#insn-00b3b07c) → [`00b3b080`](#insn-00b3b080)
- ブロック [`00b3b080`](#insn-00b3b080) 範囲 `[['00b3b080', '00b3b083']]`
  - `FALL_THROUGH` [`00b3b080`](#insn-00b3b080) → [`00b3b084`](#insn-00b3b084)
- ブロック [`00b3b084`](#insn-00b3b084) 範囲 `[['00b3b084', '00b3b087']]`
  - `FALL_THROUGH` [`00b3b084`](#insn-00b3b084) → [`00b3b088`](#insn-00b3b088)
- ブロック [`00b3b088`](#insn-00b3b088) 範囲 `[['00b3b088', '00b3b08b']]`
  - `FALL_THROUGH` [`00b3b088`](#insn-00b3b088) → [`00b3b08c`](#insn-00b3b08c)
- ブロック [`00b3b08c`](#insn-00b3b08c) 範囲 `[['00b3b08c', '00b3b093']]`
  - `CONDITIONAL_JUMP` [`00b3b090`](#insn-00b3b090) → [`00b3b09c`](#insn-00b3b09c)
  - `FALL_THROUGH` [`00b3b090`](#insn-00b3b090) → [`00b3b094`](#insn-00b3b094)
- ブロック [`00b3b094`](#insn-00b3b094) 範囲 `[['00b3b094', '00b3b09b']]`
  - `FALL_THROUGH` [`00b3b098`](#insn-00b3b098) → [`00b3b09c`](#insn-00b3b09c)
- ブロック [`00b3b09c`](#insn-00b3b09c) 範囲 `[['00b3b09c', '00b3b0ab']]`

## 命令位置別の参照

- [`00b3affc`](#insn-00b3affc) → [`00b3b048`](#insn-00b3b048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3b000`](#insn-00b3b000) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3b004`](#insn-00b3b004) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3b018`](#insn-00b3b018) → [`00b3affc`](#insn-00b3affc) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b3affc` · 推定シンボル `None` · 推定型 `None`
- [`00b3b024`](#insn-00b3b024) → [`00b3affc`](#insn-00b3affc) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b3affc` · 推定シンボル `None` · 推定型 `None`
- [`00b3b038`](#insn-00b3b038) → [`00b3b04c`](#insn-00b3b04c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3b03c`](#insn-00b3b03c) → [`00b3b060`](#insn-00b3b060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3b044`](#insn-00b3b044) → [`00b3b054`](#insn-00b3b054) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3b068`](#insn-00b3b068) → [`00b3b078`](#insn-00b3b078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3b06c`](#insn-00b3b06c) → [`00b3b08c`](#insn-00b3b08c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3b074`](#insn-00b3b074) → [`00b3b080`](#insn-00b3b080) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3b090`](#insn-00b3b090) → [`00b3b09c`](#insn-00b3b09c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3b098`](#insn-00b3b098) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00b3b0a0`](#insn-00b3b0a0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3b0a4`](#insn-00b3b0a4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3b0a8`](#insn-00b3b0a8) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b3affc`](#insn-00b3affc)

~~~json
{
  "source": "00b3affc",
  "target": "00b3b048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3b000`](#insn-00b3b000)

~~~json
{
  "source": "00b3b000",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3b004`](#insn-00b3b004)

~~~json
{
  "source": "00b3b004",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3b018`](#insn-00b3b018)

~~~json
{
  "source": "00b3b018",
  "target": "00b3affc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3b024`](#insn-00b3b024)

~~~json
{
  "source": "00b3b024",
  "target": "00b3affc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3b038`](#insn-00b3b038)

~~~json
{
  "source": "00b3b038",
  "target": "00b3b04c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3b03c`](#insn-00b3b03c)

~~~json
{
  "source": "00b3b03c",
  "target": "00b3b060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3b044`](#insn-00b3b044)

~~~json
{
  "source": "00b3b044",
  "target": "00b3b054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3b068`](#insn-00b3b068)

~~~json
{
  "source": "00b3b068",
  "target": "00b3b078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3b06c`](#insn-00b3b06c)

~~~json
{
  "source": "00b3b06c",
  "target": "00b3b08c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3b074`](#insn-00b3b074)

~~~json
{
  "source": "00b3b074",
  "target": "00b3b080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3b090`](#insn-00b3b090)

~~~json
{
  "source": "00b3b090",
  "target": "00b3b09c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3b098`](#insn-00b3b098)

~~~json
{
  "source": "00b3b098",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3b0a0`](#insn-00b3b0a0)

~~~json
{
  "source": "00b3b0a0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3b0a4`](#insn-00b3b0a4)

~~~json
{
  "source": "00b3b0a4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3b0a8`](#insn-00b3b0a8)

~~~json
{
  "source": "00b3b0a8",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
