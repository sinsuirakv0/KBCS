# 00aaea7c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aaea38`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaea38.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0059.md#compare-f761f0f0575424f035f06f784ced42f0)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b0e50c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e50c.md) · 移動量 `+0x5fa90`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0053.md#compare-e6120ac213fcc120a5ae1bff4d85b07e)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aaea7c",
  "name": "FUN_00aaea7c",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b921744f19dedd6060b303d0f4ae919b6f91ceb54546e8a9118040e40db13ab8",
  "source_text_sha256": "b921744f19dedd6060b303d0f4ae919b6f91ceb54546e8a9118040e40db13ab8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aaea7c",
        "00aaeb73"
      ],
      [
        "00aaebc0",
        "00aaebc3"
      ]
    ],
    "bytes_sha256": "9729f091e5e08e101d19d032ed986726a41ae36cf3440907d7c3ac0ffcd181ec",
    "instruction_count": 63,
    "instruction_bytes": 252,
    "body_bytes": 252,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0076e98c](../0076e/0076e98c.md)
- [00aaebc4](../00aae/00aaebc4.md)

## 呼び出し先

- [00469e20](../00469/00469e20.md)
- [0046fdf4](../0046f/0046fdf4.md)
- [00971a68](../00971/00971a68.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb340](../00bdb/00bdb340.md)

## 関連文字列（未確認候補）

~~~text
"if (typeof %s === 'function') %s(%s);"
"if (typeof %s === 'function') %s('%s');"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1994 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00aaea7c(byte *param_1,byte *param_2,ulong param_3)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  byte *pbVar6;
  byte *pbVar7;
  byte local_68 [16];
  void *local_58;
  ulong local_50;
  undefined8 uStack_48;
  char *local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  local_40 = (char *)_Znwm(0x28);
  uVar4 = s_if__typeof__s______function____s_0029fe91._16_8_;
  uVar3 = s_if__typeof__s______function____s_0029fe91._0_8_;
  uVar5 = CONCAT35(s_if__typeof__s______function____s_0029fe91._29_3_,
                   s_if__typeof__s______function____s_0029fe91._24_5_);
  uVar2 = CONCAT53(s_if__typeof__s______function____s_0029fe91._32_5_,
                   s_if__typeof__s______function____s_0029fe91._29_3_);
  uStack_48 = _UNK_002b1758;
  local_50 = _DAT_002b1750;
  *(undefined8 *)(local_40 + 8) = s_if__typeof__s______function____s_0029fe91._8_8_;
  *(undefined8 *)local_40 = uVar3;
  *(undefined8 *)(local_40 + 0x18) = uVar5;
  *(undefined8 *)(local_40 + 0x10) = uVar4;
  *(undefined8 *)(local_40 + 0x1d) = uVar2;
  local_40[0x25] = '\0';
  if ((param_3 & 1) == 0) {
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKc
              (&local_50,"if (typeof %s === \'function\') %s(\'%s\');");
  }
  pbVar7 = *(byte **)(param_1 + 0x10);
  pbVar6 = *(byte **)(param_2 + 0x10);
  if ((*param_1 & 1) == 0) {
    pbVar7 = param_1 + 1;
  }
  if ((*param_2 & 1) == 0) {
    pbVar6 = param_2 + 1;
  }
  FUN_00971a68(local_68,&local_50,0,pbVar7,pbVar7,pbVar6);
  uVar5 = FUN_00469e20();
  FUN_0046fdf4(uVar5,local_68);
  if ((local_68[0] & 1) != 0) {
    _ZdlPv(local_58);
  }
  if ((local_50 & 1) != 0) {
    _ZdlPv(local_40);
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
<a id="insn-00aaea7c"></a> `00aaea7c` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00aaea80"></a> `00aaea80` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aaea84"></a> `00aaea84` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aaea88"></a> `00aaea88` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aaea8c"></a> `00aaea8c` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00aaea90"></a> `00aaea90` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aaea94"></a> `00aaea94` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aaea98"></a> `00aaea98` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00aaea9c"></a> `00aaea9c` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00aaeaa0"></a> `00aaeaa0` | `f5 03 02 2a` | mov w21,w2 | `FALL_THROUGH`
<a id="insn-00aaeaa4"></a> `00aaeaa4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00aaeaa8"></a> `00aaeaa8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aaeaac"></a> `00aaeaac` | `65 b1 04 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00aaeab0"></a> `00aaeab0` | `88 bf ff b0` | adrp x8,0x29f000 | `FALL_THROUGH`
<a id="insn-00aaeab4"></a> `00aaeab4` | `08 45 3a 91` | add x8,x8,#0xe91 | `FALL_THROUGH`
<a id="insn-00aaeab8"></a> `00aaeab8` | `09 c0 ff f0` | adrp x9,0x2b1000 | `FALL_THROUGH`
<a id="insn-00aaeabc"></a> `00aaeabc` | `00 05 40 ad` | ldp q0,q1,[x8] | `FALL_THROUGH`
<a id="insn-00aaeac0"></a> `00aaeac0` | `22 d5 c1 3d` | ldr q2,[x9, #0x750] | `FALL_THROUGH`
<a id="insn-00aaeac4"></a> `00aaeac4` | `08 d1 41 f8` | ldur x8,[x8, #0x1d] | `FALL_THROUGH`
<a id="insn-00aaeac8"></a> `00aaeac8` | `e0 1b 00 f9` | str x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aaeacc"></a> `00aaeacc` | `e2 0b 80 3d` | str q2,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aaead0"></a> `00aaead0` | `00 04 00 ad` | stp q0,q1,[x0] | `FALL_THROUGH`
<a id="insn-00aaead4"></a> `00aaead4` | `08 d0 01 f8` | stur x8,[x0, #0x1d] | `FALL_THROUGH`
<a id="insn-00aaead8"></a> `00aaead8` | `1f 94 00 39` | strb wzr,[x0, #0x25] | `FALL_THROUGH`
<a id="insn-00aaeadc"></a> `00aaeadc` | `b5 00 00 37` | tbnz w21,#0x0,0x00aaeaf0 | `CONDITIONAL_JUMP`
<a id="insn-00aaeae0"></a> `00aaeae0` | `41 bf ff 90` | adrp x1,0x296000 | `FALL_THROUGH`
<a id="insn-00aaeae4"></a> `00aaeae4` | `21 fc 0c 91` | add x1,x1,#0x33f | `FALL_THROUGH`
<a id="insn-00aaeae8"></a> `00aaeae8` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aaeaec"></a> `00aaeaec` | `15 b2 04 94` | bl 0x00bdb340 | `UNCONDITIONAL_CALL`
<a id="insn-00aaeaf0"></a> `00aaeaf0` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-00aaeaf4"></a> `00aaeaf4` | `89 0a 40 f9` | ldr x9,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00aaeaf8"></a> `00aaeaf8` | `6a 02 40 39` | ldrb w10,[x19] | `FALL_THROUGH`
<a id="insn-00aaeafc"></a> `00aaeafc` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aaeb00"></a> `00aaeb00` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aaeb04"></a> `00aaeb04` | `22 15 94 9a` | csinc x2,x9,x20,ne | `FALL_THROUGH`
<a id="insn-00aaeb08"></a> `00aaeb08` | `5f 01 00 72` | tst w10,#0x1 | `FALL_THROUGH`
<a id="insn-00aaeb0c"></a> `00aaeb0c` | `04 15 93 9a` | csinc x4,x8,x19,ne | `FALL_THROUGH`
<a id="insn-00aaeb10"></a> `00aaeb10` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aaeb14"></a> `00aaeb14` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aaeb18"></a> `00aaeb18` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00aaeb1c"></a> `00aaeb1c` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00aaeb20"></a> `00aaeb20` | `d2 0b fb 97` | bl 0x00971a68 | `UNCONDITIONAL_CALL`
<a id="insn-00aaeb24"></a> `00aaeb24` | `bf ec e6 97` | bl 0x00469e20 | `UNCONDITIONAL_CALL`
<a id="insn-00aaeb28"></a> `00aaeb28` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aaeb2c"></a> `00aaeb2c` | `b2 04 e7 97` | bl 0x0046fdf4 | `UNCONDITIONAL_CALL`
<a id="insn-00aaeb30"></a> `00aaeb30` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aaeb34"></a> `00aaeb34` | `68 00 00 36` | tbz w8,#0x0,0x00aaeb40 | `CONDITIONAL_JUMP`
<a id="insn-00aaeb38"></a> `00aaeb38` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aaeb3c"></a> `00aaeb3c` | `49 b1 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aaeb40"></a> `00aaeb40` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aaeb44"></a> `00aaeb44` | `68 00 00 36` | tbz w8,#0x0,0x00aaeb50 | `CONDITIONAL_JUMP`
<a id="insn-00aaeb48"></a> `00aaeb48` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aaeb4c"></a> `00aaeb4c` | `45 b1 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aaeb50"></a> `00aaeb50` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00aaeb54"></a> `00aaeb54` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aaeb58"></a> `00aaeb58` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aaeb5c"></a> `00aaeb5c` | `21 03 00 54` | b.ne 0x00aaebc0 | `CONDITIONAL_JUMP`
<a id="insn-00aaeb60"></a> `00aaeb60` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aaeb64"></a> `00aaeb64` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aaeb68"></a> `00aaeb68` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aaeb6c"></a> `00aaeb6c` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00aaeb70"></a> `00aaeb70` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aaebc0"></a> `00aaebc0` | `34 b1 04 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aaea7c`](#insn-00aaea7c) 範囲 `[['00aaea7c', '00aaeadf']]`
  - `CONDITIONAL_JUMP` [`00aaeadc`](#insn-00aaeadc) → [`00aaeaf0`](#insn-00aaeaf0)
  - `FALL_THROUGH` [`00aaeadc`](#insn-00aaeadc) → [`00aaeae0`](#insn-00aaeae0)
- ブロック [`00aaeae0`](#insn-00aaeae0) 範囲 `[['00aaeae0', '00aaeaef']]`
  - `FALL_THROUGH` [`00aaeaec`](#insn-00aaeaec) → [`00aaeaf0`](#insn-00aaeaf0)
- ブロック [`00aaeaf0`](#insn-00aaeaf0) 範囲 `[['00aaeaf0', '00aaeb37']]`
  - `CONDITIONAL_JUMP` [`00aaeb34`](#insn-00aaeb34) → [`00aaeb40`](#insn-00aaeb40)
  - `FALL_THROUGH` [`00aaeb34`](#insn-00aaeb34) → [`00aaeb38`](#insn-00aaeb38)
- ブロック [`00aaeb38`](#insn-00aaeb38) 範囲 `[['00aaeb38', '00aaeb3f']]`
  - `FALL_THROUGH` [`00aaeb3c`](#insn-00aaeb3c) → [`00aaeb40`](#insn-00aaeb40)
- ブロック [`00aaeb40`](#insn-00aaeb40) 範囲 `[['00aaeb40', '00aaeb47']]`
  - `CONDITIONAL_JUMP` [`00aaeb44`](#insn-00aaeb44) → [`00aaeb50`](#insn-00aaeb50)
  - `FALL_THROUGH` [`00aaeb44`](#insn-00aaeb44) → [`00aaeb48`](#insn-00aaeb48)
- ブロック [`00aaeb48`](#insn-00aaeb48) 範囲 `[['00aaeb48', '00aaeb4f']]`
  - `FALL_THROUGH` [`00aaeb4c`](#insn-00aaeb4c) → [`00aaeb50`](#insn-00aaeb50)
- ブロック [`00aaeb50`](#insn-00aaeb50) 範囲 `[['00aaeb50', '00aaeb5f']]`
  - `CONDITIONAL_JUMP` [`00aaeb5c`](#insn-00aaeb5c) → [`00aaebc0`](#insn-00aaebc0)
  - `FALL_THROUGH` [`00aaeb5c`](#insn-00aaeb5c) → [`00aaeb60`](#insn-00aaeb60)
- ブロック [`00aaeb60`](#insn-00aaeb60) 範囲 `[['00aaeb60', '00aaeb73']]`
- ブロック [`00aaebc0`](#insn-00aaebc0) 範囲 `[['00aaebc0', '00aaebc3']]`

## 命令位置別の参照

- [`00aaea80`](#insn-00aaea80) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaea84`](#insn-00aaea84) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaea88`](#insn-00aaea88) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeaa8`](#insn-00aaeaa8) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeaac`](#insn-00aaeaac) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00aaeabc`](#insn-00aaeabc) → `0029fe91`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aaeabc`](#insn-00aaeabc) → `0029fea1`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aaeac0`](#insn-00aaeac0) → `002b1750`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeac4`](#insn-00aaeac4) → `0029feae`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aaeac8`](#insn-00aaeac8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeacc`](#insn-00aaeacc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeadc`](#insn-00aaeadc) → [`00aaeaf0`](#insn-00aaeaf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeae4`](#insn-00aaeae4) → `0029633f`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aaeaec`](#insn-00aaeaec) → [`00bdb340`](../00bdb/00bdb340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb340` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb20`](#insn-00aaeb20) → [`00971a68`](../00971/00971a68.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00971a68` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb24`](#insn-00aaeb24) → [`00469e20`](../00469/00469e20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469e20` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb2c`](#insn-00aaeb2c) → [`0046fdf4`](../0046f/0046fdf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046fdf4` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb30`](#insn-00aaeb30) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb34`](#insn-00aaeb34) → [`00aaeb40`](#insn-00aaeb40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb38`](#insn-00aaeb38) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb3c`](#insn-00aaeb3c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb40`](#insn-00aaeb40) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb44`](#insn-00aaeb44) → [`00aaeb50`](#insn-00aaeb50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb48`](#insn-00aaeb48) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb4c`](#insn-00aaeb4c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb54`](#insn-00aaeb54) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb5c`](#insn-00aaeb5c) → [`00aaebc0`](#insn-00aaebc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb60`](#insn-00aaeb60) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb64`](#insn-00aaeb64) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeb68`](#insn-00aaeb68) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaebc0`](#insn-00aaebc0) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aaea80`](#insn-00aaea80)

~~~json
{
  "source": "00aaea80",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaea84`](#insn-00aaea84)

~~~json
{
  "source": "00aaea84",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaea88`](#insn-00aaea88)

~~~json
{
  "source": "00aaea88",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeaa8`](#insn-00aaeaa8)

~~~json
{
  "source": "00aaeaa8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeaac`](#insn-00aaeaac)

~~~json
{
  "source": "00aaeaac",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaeabc`](#insn-00aaeabc)

~~~json
{
  "source": "00aaeabc",
  "target": "0029fe91",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029fe91",
  "offset": 0,
  "size": 38,
  "datatype": "string",
  "bytes": "69662028747970656f66202573203d3d3d202766756e6374696f6e2729202573",
  "capture_start": "0029fe91",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aaeabc`](#insn-00aaeabc)

~~~json
{
  "source": "00aaeabc",
  "target": "0029fea1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029fe91",
  "offset": 16,
  "size": 38,
  "datatype": "string",
  "bytes": "69662028747970656f66202573203d3d3d202766756e6374696f6e2729202573",
  "capture_start": "0029fe91",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aaeac0`](#insn-00aaeac0)

~~~json
{
  "source": "00aaeac0",
  "target": "002b1750",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeac4`](#insn-00aaeac4)

~~~json
{
  "source": "00aaeac4",
  "target": "0029feae",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029fe91",
  "offset": 29,
  "size": 38,
  "datatype": "string",
  "bytes": "69662028747970656f66202573203d3d3d202766756e6374696f6e2729202573",
  "capture_start": "0029fe91",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aaeac8`](#insn-00aaeac8)

~~~json
{
  "source": "00aaeac8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeacc`](#insn-00aaeacc)

~~~json
{
  "source": "00aaeacc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeadc`](#insn-00aaeadc)

~~~json
{
  "source": "00aaeadc",
  "target": "00aaeaf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeae4`](#insn-00aaeae4)

~~~json
{
  "source": "00aaeae4",
  "target": "0029633f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029633f",
  "offset": 0,
  "size": 40,
  "datatype": "string",
  "bytes": "69662028747970656f66202573203d3d3d202766756e6374696f6e2729202573",
  "capture_start": "0029633f",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aaeaec`](#insn-00aaeaec)

~~~json
{
  "source": "00aaeaec",
  "target": "00bdb340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaeb20`](#insn-00aaeb20)

~~~json
{
  "source": "00aaeb20",
  "target": "00971a68",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaeb24`](#insn-00aaeb24)

~~~json
{
  "source": "00aaeb24",
  "target": "00469e20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaeb2c`](#insn-00aaeb2c)

~~~json
{
  "source": "00aaeb2c",
  "target": "0046fdf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaeb30`](#insn-00aaeb30)

~~~json
{
  "source": "00aaeb30",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeb34`](#insn-00aaeb34)

~~~json
{
  "source": "00aaeb34",
  "target": "00aaeb40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeb38`](#insn-00aaeb38)

~~~json
{
  "source": "00aaeb38",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeb3c`](#insn-00aaeb3c)

~~~json
{
  "source": "00aaeb3c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaeb40`](#insn-00aaeb40)

~~~json
{
  "source": "00aaeb40",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeb44`](#insn-00aaeb44)

~~~json
{
  "source": "00aaeb44",
  "target": "00aaeb50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeb48`](#insn-00aaeb48)

~~~json
{
  "source": "00aaeb48",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeb4c`](#insn-00aaeb4c)

~~~json
{
  "source": "00aaeb4c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaeb54`](#insn-00aaeb54)

~~~json
{
  "source": "00aaeb54",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeb5c`](#insn-00aaeb5c)

~~~json
{
  "source": "00aaeb5c",
  "target": "00aaebc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeb60`](#insn-00aaeb60)

~~~json
{
  "source": "00aaeb60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeb64`](#insn-00aaeb64)

~~~json
{
  "source": "00aaeb64",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeb68`](#insn-00aaeb68)

~~~json
{
  "source": "00aaeb68",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaebc0`](#insn-00aaebc0)

~~~json
{
  "source": "00aaebc0",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
