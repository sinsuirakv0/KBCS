# 00bcddb8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bcdd74`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcdd74.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0079.md#compare-c4cd245190a7576bf36f1d201e5a1b92)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c4a800`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a800.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0078.md#compare-e5ed7c4c5459d077cb874c1748ca4859)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcddb8",
  "name": "FUN_00bcddb8",
  "size": 284,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0070c3976e6c58d57214010c2637ce437db4bd794da1573bc889a8280b679883",
  "source_text_sha256": "0070c3976e6c58d57214010c2637ce437db4bd794da1573bc889a8280b679883",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcddb8",
        "00bcded3"
      ]
    ],
    "bytes_sha256": "7746f518ced7ed8636d328841e24def273acfaebc1991ee1aff7864c501496de",
    "instruction_count": 71,
    "instruction_bytes": 284,
    "body_bytes": 284,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

## 関連文字列（未確認候補）

~~~text
" requires "
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1856 bytes

~~~c

void FUN_00bcddb8(long param_1,undefined8 *param_2)

{
  char *pcVar1;
  undefined8 uVar2;
  void *pvVar3;
  long lVar4;
  ulong uVar5;
  size_t sVar6;
  long *plVar7;
  
  lVar4 = param_2[1];
  pvVar3 = (void *)*param_2;
  if ((ulong)param_2[2] < lVar4 + 10U) {
    sVar6 = param_2[2] * 2;
    uVar5 = lVar4 + 0x3ea;
    if (sVar6 < uVar5 || sVar6 - uVar5 == 0) {
      sVar6 = uVar5;
    }
    param_2[2] = sVar6;
    pvVar3 = realloc(pvVar3,sVar6);
                    /* catch() { ... } // from try @ 00bce15c with catch @ 00bcde00
                       catch() { ... } // from try @ 00bce254 with catch @ 00bcde00 */
    *param_2 = pvVar3;
    if (pvVar3 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar4 = param_2[1];
  }
  uVar2 = s_requires_002af7ec._0_8_;
  pcVar1 = (char *)((long)pvVar3 + lVar4);
  pcVar1[8] = 's';
  pcVar1[9] = ' ';
  *(undefined8 *)pcVar1 = uVar2;
  plVar7 = *(long **)(param_1 + 0x10);
  lVar4 = *plVar7;
  param_2[1] = param_2[1] + 10;
  (**(code **)(lVar4 + 0x20))(plVar7,param_2);
  if ((*(ushort *)((long)plVar7 + 9) & 0xc0) != 0x40) {
    (**(code **)(*plVar7 + 0x28))(plVar7,param_2);
  }
  lVar4 = param_2[1];
  pvVar3 = (void *)*param_2;
  uVar5 = lVar4 + 1;
  if ((ulong)param_2[2] < uVar5) {
    sVar6 = param_2[2] * 2;
    uVar5 = lVar4 + 0x3e1;
    if (sVar6 < uVar5 || sVar6 - uVar5 == 0) {
      sVar6 = uVar5;
    }
    param_2[2] = sVar6;
    pvVar3 = realloc(pvVar3,sVar6);
    *param_2 = pvVar3;
    if (pvVar3 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar4 = param_2[1];
    uVar5 = lVar4 + 1;
  }
                    /* try { // try from 00bcdeb0 to 00ccdecb has its CatchHandler @ 00bce58c */
  param_2[1] = uVar5;
  *(undefined1 *)((long)pvVar3 + lVar4) = 0x3b;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcddb8"></a> `00bcddb8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcddbc"></a> `00bcddbc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcddc0"></a> `00bcddc0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcddc4"></a> `00bcddc4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcddc8"></a> `00bcddc8` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bcddcc"></a> `00bcddcc` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcddd0"></a> `00bcddd0` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00bcddd4"></a> `00bcddd4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcddd8"></a> `00bcddd8` | `2b 29 00 91` | add x11,x9,#0xa | `FALL_THROUGH`
<a id="insn-00bcdddc"></a> `00bcdddc` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bcdde0"></a> `00bcdde0` | `89 01 00 54` | b.ls 0x00bcde10 | `CONDITIONAL_JUMP`
<a id="insn-00bcdde4"></a> `00bcdde4` | `4a f9 7f d3` | lsl x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdde8"></a> `00bcdde8` | `29 a9 0f 91` | add x9,x9,#0x3ea | `FALL_THROUGH`
<a id="insn-00bcddec"></a> `00bcddec` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcddf0"></a> `00bcddf0` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcddf4"></a> `00bcddf4` | `41 81 89 9a` | csel x1,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00bcddf8"></a> `00bcddf8` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcddfc"></a> `00bcddfc` | `15 3d 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bcde00"></a> `00bcde00` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcde04"></a> `00bcde04` | `40 06 00 b4` | cbz x0,0x00bcdecc | `CONDITIONAL_JUMP`
<a id="insn-00bcde08"></a> `00bcde08` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcde0c"></a> `00bcde0c` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bcde10"></a> `00bcde10` | `0a b7 ff d0` | adrp x10,0x2af000 | `FALL_THROUGH`
<a id="insn-00bcde14"></a> `00bcde14` | `4a b1 1f 91` | add x10,x10,#0x7ec | `FALL_THROUGH`
<a id="insn-00bcde18"></a> `00bcde18` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bcde1c"></a> `00bcde1c` | `4a 01 40 f9` | ldr x10,[x10] | `FALL_THROUGH`
<a id="insn-00bcde20"></a> `00bcde20` | `69 0e 84 52` | mov w9,#0x2073 | `FALL_THROUGH`
<a id="insn-00bcde24"></a> `00bcde24` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcde28"></a> `00bcde28` | `09 11 00 79` | strh w9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bcde2c"></a> `00bcde2c` | `0a 01 00 f9` | str x10,[x8] | `FALL_THROUGH`
<a id="insn-00bcde30"></a> `00bcde30` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcde34"></a> `00bcde34` | `94 0a 40 f9` | ldr x20,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bcde38"></a> `00bcde38` | `08 29 00 91` | add x8,x8,#0xa | `FALL_THROUGH`
<a id="insn-00bcde3c"></a> `00bcde3c` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00bcde40"></a> `00bcde40` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcde44"></a> `00bcde44` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcde48"></a> `00bcde48` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00bcde4c"></a> `00bcde4c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcde50"></a> `00bcde50` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bcde54"></a> `00bcde54` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bcde58"></a> `00bcde58` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bcde5c"></a> `00bcde5c` | `c0 00 00 54` | b.eq 0x00bcde74 | `CONDITIONAL_JUMP`
<a id="insn-00bcde60"></a> `00bcde60` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcde64"></a> `00bcde64` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcde68"></a> `00bcde68` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcde6c"></a> `00bcde6c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bcde70"></a> `00bcde70` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcde74"></a> `00bcde74` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcde78"></a> `00bcde78` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcde7c"></a> `00bcde7c` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcde80"></a> `00bcde80` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bcde84"></a> `00bcde84` | `69 01 00 54` | b.ls 0x00bcdeb0 | `CONDITIONAL_JUMP`
<a id="insn-00bcde88"></a> `00bcde88` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcde8c"></a> `00bcde8c` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bcde90"></a> `00bcde90` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcde94"></a> `00bcde94` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcde98"></a> `00bcde98` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcde9c"></a> `00bcde9c` | `ed 3c 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdea0"></a> `00bcdea0` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcdea4"></a> `00bcdea4` | `60 01 00 b4` | cbz x0,0x00bcded0 | `CONDITIONAL_JUMP`
<a id="insn-00bcdea8"></a> `00bcdea8` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdeac"></a> `00bcdeac` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdeb0"></a> `00bcdeb0` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdeb4"></a> `00bcdeb4` | `69 07 80 52` | mov w9,#0x3b | `FALL_THROUGH`
<a id="insn-00bcdeb8"></a> `00bcdeb8` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bcdebc"></a> `00bcdebc` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdec0"></a> `00bcdec0` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcdec4"></a> `00bcdec4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcdec8"></a> `00bcdec8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcdecc"></a> `00bcdecc` | `fd 40 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`
<a id="insn-00bcded0"></a> `00bcded0` | `fc 40 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcddb8`](#insn-00bcddb8) 範囲 `[['00bcddb8', '00bcdde3']]`
  - `CONDITIONAL_JUMP` [`00bcdde0`](#insn-00bcdde0) → [`00bcde10`](#insn-00bcde10)
  - `FALL_THROUGH` [`00bcdde0`](#insn-00bcdde0) → [`00bcdde4`](#insn-00bcdde4)
- ブロック [`00bcdde4`](#insn-00bcdde4) 範囲 `[['00bcdde4', '00bcddff']]`
  - `FALL_THROUGH` [`00bcddfc`](#insn-00bcddfc) → [`00bcde00`](#insn-00bcde00)
- ブロック [`00bcde00`](#insn-00bcde00) 範囲 `[['00bcde00', '00bcde07']]`
  - `CONDITIONAL_JUMP` [`00bcde04`](#insn-00bcde04) → [`00bcdecc`](#insn-00bcdecc)
  - `FALL_THROUGH` [`00bcde04`](#insn-00bcde04) → [`00bcde08`](#insn-00bcde08)
- ブロック [`00bcde08`](#insn-00bcde08) 範囲 `[['00bcde08', '00bcde0f']]`
  - `FALL_THROUGH` [`00bcde0c`](#insn-00bcde0c) → [`00bcde10`](#insn-00bcde10)
- ブロック [`00bcde10`](#insn-00bcde10) 範囲 `[['00bcde10', '00bcde5f']]`
  - `CONDITIONAL_JUMP` [`00bcde5c`](#insn-00bcde5c) → [`00bcde74`](#insn-00bcde74)
  - `FALL_THROUGH` [`00bcde5c`](#insn-00bcde5c) → [`00bcde60`](#insn-00bcde60)
- ブロック [`00bcde60`](#insn-00bcde60) 範囲 `[['00bcde60', '00bcde73']]`
  - `FALL_THROUGH` [`00bcde70`](#insn-00bcde70) → [`00bcde74`](#insn-00bcde74)
- ブロック [`00bcde74`](#insn-00bcde74) 範囲 `[['00bcde74', '00bcde87']]`
  - `CONDITIONAL_JUMP` [`00bcde84`](#insn-00bcde84) → [`00bcdeb0`](#insn-00bcdeb0)
  - `FALL_THROUGH` [`00bcde84`](#insn-00bcde84) → [`00bcde88`](#insn-00bcde88)
- ブロック [`00bcde88`](#insn-00bcde88) 範囲 `[['00bcde88', '00bcdea7']]`
  - `CONDITIONAL_JUMP` [`00bcdea4`](#insn-00bcdea4) → [`00bcded0`](#insn-00bcded0)
  - `FALL_THROUGH` [`00bcdea4`](#insn-00bcdea4) → [`00bcdea8`](#insn-00bcdea8)
- ブロック [`00bcdea8`](#insn-00bcdea8) 範囲 `[['00bcdea8', '00bcdeaf']]`
  - `FALL_THROUGH` [`00bcdeac`](#insn-00bcdeac) → [`00bcdeb0`](#insn-00bcdeb0)
- ブロック [`00bcdeb0`](#insn-00bcdeb0) 範囲 `[['00bcdeb0', '00bcdecb']]`
- ブロック [`00bcdecc`](#insn-00bcdecc) 範囲 `[['00bcdecc', '00bcdecf']]`
- ブロック [`00bcded0`](#insn-00bcded0) 範囲 `[['00bcded0', '00bcded3']]`

## 命令位置別の参照

- [`00bcddbc`](#insn-00bcddbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcddc0`](#insn-00bcddc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdde0`](#insn-00bcdde0) → [`00bcde10`](#insn-00bcde10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcddfc`](#insn-00bcddfc) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bcde04`](#insn-00bcde04) → [`00bcdecc`](#insn-00bcdecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde1c`](#insn-00bcde1c) → `002af7ec`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcde5c`](#insn-00bcde5c) → [`00bcde74`](#insn-00bcde74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde84`](#insn-00bcde84) → [`00bcdeb0`](#insn-00bcdeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde9c`](#insn-00bcde9c) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bcdea4`](#insn-00bcdea4) → [`00bcded0`](#insn-00bcded0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdebc`](#insn-00bcdebc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdec0`](#insn-00bcdec0) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdecc`](#insn-00bcdecc) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`
- [`00bcded0`](#insn-00bcded0) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcddbc`](#insn-00bcddbc)

~~~json
{
  "source": "00bcddbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcddc0`](#insn-00bcddc0)

~~~json
{
  "source": "00bcddc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdde0`](#insn-00bcdde0)

~~~json
{
  "source": "00bcdde0",
  "target": "00bcde10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcddfc`](#insn-00bcddfc)

~~~json
{
  "source": "00bcddfc",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcde04`](#insn-00bcde04)

~~~json
{
  "source": "00bcde04",
  "target": "00bcdecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde1c`](#insn-00bcde1c)

~~~json
{
  "source": "00bcde1c",
  "target": "002af7ec",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002af7ec",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "2072657175697265732000",
  "capture_start": "002af7ec",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcde5c`](#insn-00bcde5c)

~~~json
{
  "source": "00bcde5c",
  "target": "00bcde74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde84`](#insn-00bcde84)

~~~json
{
  "source": "00bcde84",
  "target": "00bcdeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde9c`](#insn-00bcde9c)

~~~json
{
  "source": "00bcde9c",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdea4`](#insn-00bcdea4)

~~~json
{
  "source": "00bcdea4",
  "target": "00bcded0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdebc`](#insn-00bcdebc)

~~~json
{
  "source": "00bcdebc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdec0`](#insn-00bcdec0)

~~~json
{
  "source": "00bcdec0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdecc`](#insn-00bcdecc)

~~~json
{
  "source": "00bcdecc",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcded0`](#insn-00bcded0)

~~~json
{
  "source": "00bcded0",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
