# 00a9abdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a3cce8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3cce8.md) · 移動量 `+0x5def4`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0051.md#compare-05e7b36133f6cce308504705fb2c9cda)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00a9add8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a9a/00a9add8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0062.md#compare-d54388d8e6476b25479c28cf2db8262f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a9abdc",
  "name": "FUN_00a9abdc",
  "size": 312,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b4fd6fd907f67fb8444b1af77b193780eb54cf747bd116f880f117e4ef6f0a48",
  "source_text_sha256": "b4fd6fd907f67fb8444b1af77b193780eb54cf747bd116f880f117e4ef6f0a48",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a9abdc",
        "00a9ad0f"
      ],
      [
        "00a9ad40",
        "00a9ad43"
      ]
    ],
    "bytes_sha256": "8dd583105655c37794b3ccfe906d16f00e7035ed1ee9d47aae5a0e452cd5b83c",
    "instruction_count": 78,
    "instruction_bytes": 312,
    "body_bytes": 312,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a8e3bc](../00a8e/00a8e3bc.md)
- [00a917e4](../00a91/00a917e4.md)

## 呼び出し先

- [00764344](../00764/00764344.md)
- [00887790](../00887/00887790.md)
- [00887798](../00887/00887798.md)
- [008877a0](../00887/008877a0.md)
- [00b32d28](../00b32/00b32d28.md)
- [00b358d8](../00b35/00b358d8.md)
- [00b38f88](../00b38/00b38f88.md)
- [00b390b8](../00b39/00b390b8.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)

## 関連文字列（未確認候補）

~~~text
"jkdblt56ptkw"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1614 bytes

~~~c

void FUN_00a9abdc(long param_1,char *param_2)

{
  char *pcVar1;
  long lVar2;
  long lVar3;
  undefined8 uVar4;
  byte local_50;
  char local_4f [8];
  undefined4 local_47;
  undefined1 local_43;
  char *local_40;
  long local_38;
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  lVar3 = *(long *)(param_1 + 8);
  if (*param_2 == '\0') {
    FUN_00b390b8(0);
    FUN_00b358d8(0);
    FUN_00887790(*(undefined8 *)(lVar3 + 0x22a0),0);
  }
  else {
    FUN_00b390b8(1);
    FUN_00b358d8(1);
    FUN_00887790(*(undefined8 *)(lVar3 + 0x22a0),1);
    local_50 = 0x18;
    local_47 = 0x776b7470;
    local_4f[0] = s_jkdblt56ptkw_002af15d[0];
    local_4f[1] = s_jkdblt56ptkw_002af15d[1];
    local_4f[2] = s_jkdblt56ptkw_002af15d[2];
    local_4f[3] = s_jkdblt56ptkw_002af15d[3];
    local_4f[4] = s_jkdblt56ptkw_002af15d[4];
    local_4f[5] = s_jkdblt56ptkw_002af15d[5];
    local_4f[6] = s_jkdblt56ptkw_002af15d[6];
    local_4f[7] = s_jkdblt56ptkw_002af15d[7];
    local_43 = 0;
    FUN_00b32d28(&local_50,&DAT_01123d08);
    if ((local_50 & 1) != 0) {
      _ZdlPv(local_40);
    }
  }
  FUN_00b38f88(*(int *)(lVar3 + 0x1dd8) == -1);
  FUN_00887798(*(undefined8 *)(lVar3 + 0x22a0),*(int *)(lVar3 + 0x1dd8) == -1);
  uVar4 = *(undefined8 *)(lVar3 + 0x22a0);
  FUN_00764344(&local_50,lVar3);
  pcVar1 = local_40;
  if ((local_50 & 1) == 0) {
    pcVar1 = local_4f;
  }
  FUN_008877a0(uVar4,pcVar1);
  if ((local_50 & 1) != 0) {
    _ZdlPv(local_40);
  }
  if (*(long *)(lVar2 + 0x28) == local_38) {
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
<a id="insn-00a9abdc"></a> `00a9abdc` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00a9abe0"></a> `00a9abe0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a9abe4"></a> `00a9abe4` | `f5 1b 00 f9` | str x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a9abe8"></a> `00a9abe8` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a9abec"></a> `00a9abec` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00a9abf0"></a> `00a9abf0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00a9abf4"></a> `00a9abf4` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00a9abf8"></a> `00a9abf8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a9abfc"></a> `00a9abfc` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00a9ac00"></a> `00a9ac00` | `13 04 40 f9` | ldr x19,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00a9ac04"></a> `00a9ac04` | `68 03 00 34` | cbz w8,0x00a9ac70 | `CONDITIONAL_JUMP`
<a id="insn-00a9ac08"></a> `00a9ac08` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00a9ac0c"></a> `00a9ac0c` | `2b 79 02 94` | bl 0x00b390b8 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ac10"></a> `00a9ac10` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00a9ac14"></a> `00a9ac14` | `31 6b 02 94` | bl 0x00b358d8 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ac18"></a> `00a9ac18` | `60 52 51 f9` | ldr x0,[x19, #0x22a0] | `FALL_THROUGH`
<a id="insn-00a9ac1c"></a> `00a9ac1c` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00a9ac20"></a> `00a9ac20` | `dc b2 f7 97` | bl 0x00887790 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ac24"></a> `00a9ac24` | `a9 c0 ff b0` | adrp x9,0x2af000 | `FALL_THROUGH`
<a id="insn-00a9ac28"></a> `00a9ac28` | `29 75 05 91` | add x9,x9,#0x15d | `FALL_THROUGH`
<a id="insn-00a9ac2c"></a> `00a9ac2c` | `0a 8e 8e 52` | mov w10,#0x7470 | `FALL_THROUGH`
<a id="insn-00a9ac30"></a> `00a9ac30` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00a9ac34"></a> `00a9ac34` | `08 03 80 52` | mov w8,#0x18 | `FALL_THROUGH`
<a id="insn-00a9ac38"></a> `00a9ac38` | `6a ed ae 72` | movk w10,#0x776b, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9ac3c"></a> `00a9ac3c` | `e8 03 00 39` | strb w8,[sp] | `FALL_THROUGH`
<a id="insn-00a9ac40"></a> `00a9ac40` | `ea 93 00 b8` | stur w10,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-00a9ac44"></a> `00a9ac44` | `e9 13 00 f8` | stur x9,[sp, #0x1] | `FALL_THROUGH`
<a id="insn-00a9ac48"></a> `00a9ac48` | `ff 37 00 39` | strb wzr,[sp, #0xd] | `FALL_THROUGH`
<a id="insn-00a9ac4c"></a> `00a9ac4c` | `41 34 00 b0` | adrp x1,0x1123000 | `FALL_THROUGH`
<a id="insn-00a9ac50"></a> `00a9ac50` | `21 20 34 91` | add x1,x1,#0xd08 | `FALL_THROUGH`
<a id="insn-00a9ac54"></a> `00a9ac54` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00a9ac58"></a> `00a9ac58` | `34 60 02 94` | bl 0x00b32d28 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ac5c"></a> `00a9ac5c` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00a9ac60"></a> `00a9ac60` | `68 01 00 36` | tbz w8,#0x0,0x00a9ac8c | `CONDITIONAL_JUMP`
<a id="insn-00a9ac64"></a> `00a9ac64` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9ac68"></a> `00a9ac68` | `92 f3 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ac6c"></a> `00a9ac6c` | `08 00 00 14` | b 0x00a9ac8c | `UNCONDITIONAL_JUMP`
<a id="insn-00a9ac70"></a> `00a9ac70` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00a9ac74"></a> `00a9ac74` | `11 79 02 94` | bl 0x00b390b8 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ac78"></a> `00a9ac78` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00a9ac7c"></a> `00a9ac7c` | `17 6b 02 94` | bl 0x00b358d8 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ac80"></a> `00a9ac80` | `60 52 51 f9` | ldr x0,[x19, #0x22a0] | `FALL_THROUGH`
<a id="insn-00a9ac84"></a> `00a9ac84` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00a9ac88"></a> `00a9ac88` | `c2 b2 f7 97` | bl 0x00887790 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ac8c"></a> `00a9ac8c` | `68 da 5d b9` | ldr w8,[x19, #0x1dd8] | `FALL_THROUGH`
<a id="insn-00a9ac90"></a> `00a9ac90` | `1f 05 00 31` | cmn w8,#0x1 | `FALL_THROUGH`
<a id="insn-00a9ac94"></a> `00a9ac94` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00a9ac98"></a> `00a9ac98` | `bc 78 02 94` | bl 0x00b38f88 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ac9c"></a> `00a9ac9c` | `68 da 5d b9` | ldr w8,[x19, #0x1dd8] | `FALL_THROUGH`
<a id="insn-00a9aca0"></a> `00a9aca0` | `60 52 51 f9` | ldr x0,[x19, #0x22a0] | `FALL_THROUGH`
<a id="insn-00a9aca4"></a> `00a9aca4` | `1f 05 00 31` | cmn w8,#0x1 | `FALL_THROUGH`
<a id="insn-00a9aca8"></a> `00a9aca8` | `e1 17 9f 1a` | cset w1,eq | `FALL_THROUGH`
<a id="insn-00a9acac"></a> `00a9acac` | `bb b2 f7 97` | bl 0x00887798 | `UNCONDITIONAL_CALL`
<a id="insn-00a9acb0"></a> `00a9acb0` | `74 52 51 f9` | ldr x20,[x19, #0x22a0] | `FALL_THROUGH`
<a id="insn-00a9acb4"></a> `00a9acb4` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00a9acb8"></a> `00a9acb8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a9acbc"></a> `00a9acbc` | `f3 03 00 91` | mov x19,sp | `FALL_THROUGH`
<a id="insn-00a9acc0"></a> `00a9acc0` | `a1 25 f3 97` | bl 0x00764344 | `UNCONDITIONAL_CALL`
<a id="insn-00a9acc4"></a> `00a9acc4` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00a9acc8"></a> `00a9acc8` | `e9 0b 40 f9` | ldr x9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9accc"></a> `00a9accc` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00a9acd0"></a> `00a9acd0` | `21 15 93 9a` | csinc x1,x9,x19,ne | `FALL_THROUGH`
<a id="insn-00a9acd4"></a> `00a9acd4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a9acd8"></a> `00a9acd8` | `b2 b2 f7 97` | bl 0x008877a0 | `UNCONDITIONAL_CALL`
<a id="insn-00a9acdc"></a> `00a9acdc` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00a9ace0"></a> `00a9ace0` | `68 00 00 36` | tbz w8,#0x0,0x00a9acec | `CONDITIONAL_JUMP`
<a id="insn-00a9ace4"></a> `00a9ace4` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9ace8"></a> `00a9ace8` | `72 f3 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00a9acec"></a> `00a9acec` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00a9acf0"></a> `00a9acf0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a9acf4"></a> `00a9acf4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a9acf8"></a> `00a9acf8` | `41 02 00 54` | b.ne 0x00a9ad40 | `CONDITIONAL_JUMP`
<a id="insn-00a9acfc"></a> `00a9acfc` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a9ad00"></a> `00a9ad00` | `f5 1b 40 f9` | ldr x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a9ad04"></a> `00a9ad04` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a9ad08"></a> `00a9ad08` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00a9ad0c"></a> `00a9ad0c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a9ad40"></a> `00a9ad40` | `68 f3 06 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a9abdc`](#insn-00a9abdc) 範囲 `[['00a9abdc', '00a9ac07']]`
  - `CONDITIONAL_JUMP` [`00a9ac04`](#insn-00a9ac04) → [`00a9ac70`](#insn-00a9ac70)
  - `FALL_THROUGH` [`00a9ac04`](#insn-00a9ac04) → [`00a9ac08`](#insn-00a9ac08)
- ブロック [`00a9ac08`](#insn-00a9ac08) 範囲 `[['00a9ac08', '00a9ac63']]`
  - `CONDITIONAL_JUMP` [`00a9ac60`](#insn-00a9ac60) → [`00a9ac8c`](#insn-00a9ac8c)
  - `FALL_THROUGH` [`00a9ac60`](#insn-00a9ac60) → [`00a9ac64`](#insn-00a9ac64)
- ブロック [`00a9ac64`](#insn-00a9ac64) 範囲 `[['00a9ac64', '00a9ac6f']]`
  - `UNCONDITIONAL_JUMP` [`00a9ac6c`](#insn-00a9ac6c) → [`00a9ac8c`](#insn-00a9ac8c)
- ブロック [`00a9ac70`](#insn-00a9ac70) 範囲 `[['00a9ac70', '00a9ac8b']]`
  - `FALL_THROUGH` [`00a9ac88`](#insn-00a9ac88) → [`00a9ac8c`](#insn-00a9ac8c)
- ブロック [`00a9ac8c`](#insn-00a9ac8c) 範囲 `[['00a9ac8c', '00a9ace3']]`
  - `CONDITIONAL_JUMP` [`00a9ace0`](#insn-00a9ace0) → [`00a9acec`](#insn-00a9acec)
  - `FALL_THROUGH` [`00a9ace0`](#insn-00a9ace0) → [`00a9ace4`](#insn-00a9ace4)
- ブロック [`00a9ace4`](#insn-00a9ace4) 範囲 `[['00a9ace4', '00a9aceb']]`
  - `FALL_THROUGH` [`00a9ace8`](#insn-00a9ace8) → [`00a9acec`](#insn-00a9acec)
- ブロック [`00a9acec`](#insn-00a9acec) 範囲 `[['00a9acec', '00a9acfb']]`
  - `CONDITIONAL_JUMP` [`00a9acf8`](#insn-00a9acf8) → [`00a9ad40`](#insn-00a9ad40)
  - `FALL_THROUGH` [`00a9acf8`](#insn-00a9acf8) → [`00a9acfc`](#insn-00a9acfc)
- ブロック [`00a9acfc`](#insn-00a9acfc) 範囲 `[['00a9acfc', '00a9ad0f']]`
- ブロック [`00a9ad40`](#insn-00a9ad40) 範囲 `[['00a9ad40', '00a9ad43']]`

## 命令位置別の参照

- [`00a9abe0`](#insn-00a9abe0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9abe4`](#insn-00a9abe4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9abe8`](#insn-00a9abe8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9abf8`](#insn-00a9abf8) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac04`](#insn-00a9ac04) → [`00a9ac70`](#insn-00a9ac70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac0c`](#insn-00a9ac0c) → [`00b390b8`](../00b39/00b390b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b390b8` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac14`](#insn-00a9ac14) → [`00b358d8`](../00b35/00b358d8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b358d8` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac20`](#insn-00a9ac20) → [`00887790`](../00887/00887790.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00887790` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac30`](#insn-00a9ac30) → `002af15d`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00a9ac3c`](#insn-00a9ac3c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac40`](#insn-00a9ac40) → `Stack[-0x47]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac44`](#insn-00a9ac44) → `Stack[-0x4f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac48`](#insn-00a9ac48) → `Stack[-0x43]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac50`](#insn-00a9ac50) → `01123d08`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00a9ac58`](#insn-00a9ac58) → [`00b32d28`](../00b32/00b32d28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b32d28` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac5c`](#insn-00a9ac5c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac60`](#insn-00a9ac60) → [`00a9ac8c`](#insn-00a9ac8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac64`](#insn-00a9ac64) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac68`](#insn-00a9ac68) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac6c`](#insn-00a9ac6c) → [`00a9ac8c`](#insn-00a9ac8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac74`](#insn-00a9ac74) → [`00b390b8`](../00b39/00b390b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b390b8` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac7c`](#insn-00a9ac7c) → [`00b358d8`](../00b35/00b358d8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b358d8` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac88`](#insn-00a9ac88) → [`00887790`](../00887/00887790.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00887790` · 推定シンボル `None` · 推定型 `None`
- [`00a9ac98`](#insn-00a9ac98) → [`00b38f88`](../00b38/00b38f88.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b38f88` · 推定シンボル `None` · 推定型 `None`
- [`00a9acac`](#insn-00a9acac) → [`00887798`](../00887/00887798.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00887798` · 推定シンボル `None` · 推定型 `None`
- [`00a9acc0`](#insn-00a9acc0) → [`00764344`](../00764/00764344.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00764344` · 推定シンボル `None` · 推定型 `None`
- [`00a9acc4`](#insn-00a9acc4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9acc8`](#insn-00a9acc8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9acd8`](#insn-00a9acd8) → [`008877a0`](../00887/008877a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008877a0` · 推定シンボル `None` · 推定型 `None`
- [`00a9acdc`](#insn-00a9acdc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ace0`](#insn-00a9ace0) → [`00a9acec`](#insn-00a9acec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ace4`](#insn-00a9ace4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ace8`](#insn-00a9ace8) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00a9acf0`](#insn-00a9acf0) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9acf8`](#insn-00a9acf8) → [`00a9ad40`](#insn-00a9ad40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9acfc`](#insn-00a9acfc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ad00`](#insn-00a9ad00) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ad04`](#insn-00a9ad04) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ad40`](#insn-00a9ad40) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a9abe0`](#insn-00a9abe0)

~~~json
{
  "source": "00a9abe0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9abe4`](#insn-00a9abe4)

~~~json
{
  "source": "00a9abe4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9abe8`](#insn-00a9abe8)

~~~json
{
  "source": "00a9abe8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9abf8`](#insn-00a9abf8)

~~~json
{
  "source": "00a9abf8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ac04`](#insn-00a9ac04)

~~~json
{
  "source": "00a9ac04",
  "target": "00a9ac70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ac0c`](#insn-00a9ac0c)

~~~json
{
  "source": "00a9ac0c",
  "target": "00b390b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ac14`](#insn-00a9ac14)

~~~json
{
  "source": "00a9ac14",
  "target": "00b358d8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ac20`](#insn-00a9ac20)

~~~json
{
  "source": "00a9ac20",
  "target": "00887790",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ac30`](#insn-00a9ac30)

~~~json
{
  "source": "00a9ac30",
  "target": "002af15d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002af15d",
  "offset": 0,
  "size": 13,
  "datatype": "string",
  "bytes": "6a6b64626c74353670746b7700",
  "capture_start": "002af15d",
  "capture_bytes": 13,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00a9ac3c`](#insn-00a9ac3c)

~~~json
{
  "source": "00a9ac3c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ac40`](#insn-00a9ac40)

~~~json
{
  "source": "00a9ac40",
  "target": "Stack[-0x47]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ac44`](#insn-00a9ac44)

~~~json
{
  "source": "00a9ac44",
  "target": "Stack[-0x4f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ac48`](#insn-00a9ac48)

~~~json
{
  "source": "00a9ac48",
  "target": "Stack[-0x43]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ac50`](#insn-00a9ac50)

~~~json
{
  "source": "00a9ac50",
  "target": "01123d08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01123d08",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a9ac58`](#insn-00a9ac58)

~~~json
{
  "source": "00a9ac58",
  "target": "00b32d28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ac5c`](#insn-00a9ac5c)

~~~json
{
  "source": "00a9ac5c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ac60`](#insn-00a9ac60)

~~~json
{
  "source": "00a9ac60",
  "target": "00a9ac8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ac64`](#insn-00a9ac64)

~~~json
{
  "source": "00a9ac64",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ac68`](#insn-00a9ac68)

~~~json
{
  "source": "00a9ac68",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ac6c`](#insn-00a9ac6c)

~~~json
{
  "source": "00a9ac6c",
  "target": "00a9ac8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ac74`](#insn-00a9ac74)

~~~json
{
  "source": "00a9ac74",
  "target": "00b390b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ac7c`](#insn-00a9ac7c)

~~~json
{
  "source": "00a9ac7c",
  "target": "00b358d8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ac88`](#insn-00a9ac88)

~~~json
{
  "source": "00a9ac88",
  "target": "00887790",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ac98`](#insn-00a9ac98)

~~~json
{
  "source": "00a9ac98",
  "target": "00b38f88",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9acac`](#insn-00a9acac)

~~~json
{
  "source": "00a9acac",
  "target": "00887798",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9acc0`](#insn-00a9acc0)

~~~json
{
  "source": "00a9acc0",
  "target": "00764344",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9acc4`](#insn-00a9acc4)

~~~json
{
  "source": "00a9acc4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9acc8`](#insn-00a9acc8)

~~~json
{
  "source": "00a9acc8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9acd8`](#insn-00a9acd8)

~~~json
{
  "source": "00a9acd8",
  "target": "008877a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9acdc`](#insn-00a9acdc)

~~~json
{
  "source": "00a9acdc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ace0`](#insn-00a9ace0)

~~~json
{
  "source": "00a9ace0",
  "target": "00a9acec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ace4`](#insn-00a9ace4)

~~~json
{
  "source": "00a9ace4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ace8`](#insn-00a9ace8)

~~~json
{
  "source": "00a9ace8",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9acf0`](#insn-00a9acf0)

~~~json
{
  "source": "00a9acf0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9acf8`](#insn-00a9acf8)

~~~json
{
  "source": "00a9acf8",
  "target": "00a9ad40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9acfc`](#insn-00a9acfc)

~~~json
{
  "source": "00a9acfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ad00`](#insn-00a9ad00)

~~~json
{
  "source": "00a9ad00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ad04`](#insn-00a9ad04)

~~~json
{
  "source": "00a9ad04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ad40`](#insn-00a9ad40)

~~~json
{
  "source": "00a9ad40",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
