# 00afdb2c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00afda64`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afda64.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0002.md#compare-a0f623381625a1e2e7811fd8922cfd08)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00afdb70`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afdb70.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-f54e482cf6c8b578e9e329d60ce43163)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afdb2c",
  "name": "_ZNK8firebase4Path14FrontDirectoryEv",
  "size": 216,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ade0712361917ed5e6ad4a47f106a04c135a2fd8a8c301c36b046f40a168bd3e",
  "source_text_sha256": "ade0712361917ed5e6ad4a47f106a04c135a2fd8a8c301c36b046f40a168bd3e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afdb2c",
        "00afdc03"
      ]
    ],
    "bytes_sha256": "7fb6701760b3620b85c20079895ec56d7e03bc877c3935c9d2b460828c8ce44c",
    "instruction_count": 54,
    "instruction_bytes": 216,
    "body_bytes": 216,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdece0](../00bde/00bdece0.md)
- [00bdecf0](../00bde/00bdecf0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1816 bytes

~~~c

void _ZNK8firebase4Path14FrontDirectoryEv(undefined8 *param_1,byte *param_2)

{
  byte bVar1;
  long lVar2;
  byte *pbVar3;
  byte *pbVar4;
  byte *pbVar5;
  byte *local_50;
  byte *local_48;
  long local_38;
  
                    /* try { // try from 00afdb30 to 00bfdb3b has its CatchHandler @ 00afecd8 */
                    /* try { // try from 00afdb40 to 00bfdb5b has its CatchHandler @ 00afecd4 */
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  if ((*param_2 & 1) == 0) {
    if (*param_2 >> 1 == 0) {
LAB_00afdbbc:
      *param_1 = 0;
      param_1[1] = 0;
                    /* try { // try from 00afdbc0 to 00bfdbdb has its CatchHandler @ 00afeccc */
      param_1[2] = 0;
      goto LAB_00afdbdc;
    }
  }
  else if (*(long *)(param_2 + 8) == 0) goto LAB_00afdbbc;
                    /* try { // try from 00afdb60 to 00bfdb6f has its CatchHandler @ 00b0037c */
  _ZNK8firebase4Path14GetDirectoriesEv(&local_50);
  _ZN8firebase4Path16NormalizeSlashesERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
            (param_1,local_50);
  pbVar4 = local_50;
  if (local_50 != (byte *)0x0) {
    if (local_48 != local_50) {
      bVar1 = local_48[-0x18];
      pbVar5 = local_48 + -0x18;
      while( true ) {
        pbVar3 = pbVar5;
        if ((bVar1 & 1) != 0) {
          _ZdlPv(*(void **)(local_48 + -8));
                    /* try { // try from 00afdbb0 to 00bfdbbb has its CatchHandler @ 00afecd0 */
        }
        if (pbVar4 == pbVar3) break;
        bVar1 = pbVar3[-0x18];
        pbVar5 = pbVar3 + -0x18;
        local_48 = pbVar3;
      }
    }
    local_48 = pbVar4;
    _ZdlPv(local_50);
  }
LAB_00afdbdc:
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
<a id="insn-00afdb2c"></a> `00afdb2c` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00afdb30"></a> `00afdb30` | `f5 13 00 f9` | str x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afdb34"></a> `00afdb34` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afdb38"></a> `00afdb38` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afdb3c"></a> `00afdb3c` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00afdb40"></a> `00afdb40` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00afdb44"></a> `00afdb44` | `89 16 40 f9` | ldr x9,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00afdb48"></a> `00afdb48` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00afdb4c"></a> `00afdb4c` | `e9 0f 00 f9` | str x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00afdb50"></a> `00afdb50` | `09 00 40 39` | ldrb w9,[x0] | `FALL_THROUGH`
<a id="insn-00afdb54"></a> `00afdb54` | `09 03 00 37` | tbnz w9,#0x0,0x00afdbb4 | `CONDITIONAL_JUMP`
<a id="insn-00afdb58"></a> `00afdb58` | `28 fd 41 d3` | lsr x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00afdb5c"></a> `00afdb5c` | `08 03 00 b4` | cbz x8,0x00afdbbc | `CONDITIONAL_JUMP`
<a id="insn-00afdb60"></a> `00afdb60` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00afdb64"></a> `00afdb64` | `63 84 03 94` | bl 0x00bdecf0 | `UNCONDITIONAL_CALL`
<a id="insn-00afdb68"></a> `00afdb68` | `e0 03 40 f9` | ldr x0,[sp] | `FALL_THROUGH`
<a id="insn-00afdb6c"></a> `00afdb6c` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00afdb70"></a> `00afdb70` | `5c 84 03 94` | bl 0x00bdece0 | `UNCONDITIONAL_CALL`
<a id="insn-00afdb74"></a> `00afdb74` | `f3 03 40 f9` | ldr x19,[sp] | `FALL_THROUGH`
<a id="insn-00afdb78"></a> `00afdb78` | `33 03 00 b4` | cbz x19,0x00afdbdc | `CONDITIONAL_JUMP`
<a id="insn-00afdb7c"></a> `00afdb7c` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00afdb80"></a> `00afdb80` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00afdb84"></a> `00afdb84` | `60 02 00 54` | b.eq 0x00afdbd0 | `CONDITIONAL_JUMP`
<a id="insn-00afdb88"></a> `00afdb88` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00afdb8c"></a> `00afdb8c` | `a9 8e 5e 38` | ldrb w9,[x21, #-0x18]! | `FALL_THROUGH`
<a id="insn-00afdb90"></a> `00afdb90` | `c9 00 00 37` | tbnz w9,#0x0,0x00afdba8 | `CONDITIONAL_JUMP`
<a id="insn-00afdb94"></a> `00afdb94` | `7f 02 15 eb` | cmp x19,x21 | `FALL_THROUGH`
<a id="insn-00afdb98"></a> `00afdb98` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00afdb9c"></a> `00afdb9c` | `60 01 00 54` | b.eq 0x00afdbc8 | `CONDITIONAL_JUMP`
<a id="insn-00afdba0"></a> `00afdba0` | `a9 8e 5e 38` | ldrb w9,[x21, #-0x18]! | `FALL_THROUGH`
<a id="insn-00afdba4"></a> `00afdba4` | `89 ff 07 36` | tbz w9,#0x0,0x00afdb94 | `CONDITIONAL_JUMP`
<a id="insn-00afdba8"></a> `00afdba8` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00afdbac"></a> `00afdbac` | `19 75 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00afdbb0"></a> `00afdbb0` | `f9 ff ff 17` | b 0x00afdb94 | `UNCONDITIONAL_JUMP`
<a id="insn-00afdbb4"></a> `00afdbb4` | `08 04 40 f9` | ldr x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00afdbb8"></a> `00afdbb8` | `48 fd ff b5` | cbnz x8,0x00afdb60 | `CONDITIONAL_JUMP`
<a id="insn-00afdbbc"></a> `00afdbbc` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00afdbc0"></a> `00afdbc0` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00afdbc4"></a> `00afdbc4` | `06 00 00 14` | b 0x00afdbdc | `UNCONDITIONAL_JUMP`
<a id="insn-00afdbc8"></a> `00afdbc8` | `e0 03 40 f9` | ldr x0,[sp] | `FALL_THROUGH`
<a id="insn-00afdbcc"></a> `00afdbcc` | `02 00 00 14` | b 0x00afdbd4 | `UNCONDITIONAL_JUMP`
<a id="insn-00afdbd0"></a> `00afdbd0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afdbd4"></a> `00afdbd4` | `f3 07 00 f9` | str x19,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00afdbd8"></a> `00afdbd8` | `0e 75 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00afdbdc"></a> `00afdbdc` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00afdbe0"></a> `00afdbe0` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00afdbe4"></a> `00afdbe4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00afdbe8"></a> `00afdbe8` | `c1 00 00 54` | b.ne 0x00afdc00 | `CONDITIONAL_JUMP`
<a id="insn-00afdbec"></a> `00afdbec` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afdbf0"></a> `00afdbf0` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afdbf4"></a> `00afdbf4` | `f5 13 40 f9` | ldr x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afdbf8"></a> `00afdbf8` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00afdbfc"></a> `00afdbfc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afdc00"></a> `00afdc00` | `10 75 03 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afdb2c`](#insn-00afdb2c) 範囲 `[['00afdb2c', '00afdb2f']]`
  - `FALL_THROUGH` [`00afdb2c`](#insn-00afdb2c) → [`00afdb30`](#insn-00afdb30)
- ブロック [`00afdb30`](#insn-00afdb30) 範囲 `[['00afdb30', '00afdb3f']]`
  - `FALL_THROUGH` [`00afdb3c`](#insn-00afdb3c) → [`00afdb40`](#insn-00afdb40)
- ブロック [`00afdb40`](#insn-00afdb40) 範囲 `[['00afdb40', '00afdb57']]`
  - `CONDITIONAL_JUMP` [`00afdb54`](#insn-00afdb54) → [`00afdbb4`](#insn-00afdbb4)
  - `FALL_THROUGH` [`00afdb54`](#insn-00afdb54) → [`00afdb58`](#insn-00afdb58)
- ブロック [`00afdb58`](#insn-00afdb58) 範囲 `[['00afdb58', '00afdb5f']]`
  - `CONDITIONAL_JUMP` [`00afdb5c`](#insn-00afdb5c) → [`00afdbbc`](#insn-00afdbbc)
  - `FALL_THROUGH` [`00afdb5c`](#insn-00afdb5c) → [`00afdb60`](#insn-00afdb60)
- ブロック [`00afdb60`](#insn-00afdb60) 範囲 `[['00afdb60', '00afdb7b']]`
  - `CONDITIONAL_JUMP` [`00afdb78`](#insn-00afdb78) → [`00afdbdc`](#insn-00afdbdc)
  - `FALL_THROUGH` [`00afdb78`](#insn-00afdb78) → [`00afdb7c`](#insn-00afdb7c)
- ブロック [`00afdb7c`](#insn-00afdb7c) 範囲 `[['00afdb7c', '00afdb87']]`
  - `CONDITIONAL_JUMP` [`00afdb84`](#insn-00afdb84) → [`00afdbd0`](#insn-00afdbd0)
  - `FALL_THROUGH` [`00afdb84`](#insn-00afdb84) → [`00afdb88`](#insn-00afdb88)
- ブロック [`00afdb88`](#insn-00afdb88) 範囲 `[['00afdb88', '00afdb93']]`
  - `CONDITIONAL_JUMP` [`00afdb90`](#insn-00afdb90) → [`00afdba8`](#insn-00afdba8)
  - `FALL_THROUGH` [`00afdb90`](#insn-00afdb90) → [`00afdb94`](#insn-00afdb94)
- ブロック [`00afdb94`](#insn-00afdb94) 範囲 `[['00afdb94', '00afdb9f']]`
  - `CONDITIONAL_JUMP` [`00afdb9c`](#insn-00afdb9c) → [`00afdbc8`](#insn-00afdbc8)
  - `FALL_THROUGH` [`00afdb9c`](#insn-00afdb9c) → [`00afdba0`](#insn-00afdba0)
- ブロック [`00afdba0`](#insn-00afdba0) 範囲 `[['00afdba0', '00afdba7']]`
  - `CONDITIONAL_JUMP` [`00afdba4`](#insn-00afdba4) → [`00afdb94`](#insn-00afdb94)
  - `FALL_THROUGH` [`00afdba4`](#insn-00afdba4) → [`00afdba8`](#insn-00afdba8)
- ブロック [`00afdba8`](#insn-00afdba8) 範囲 `[['00afdba8', '00afdbaf']]`
  - `FALL_THROUGH` [`00afdbac`](#insn-00afdbac) → [`00afdbb0`](#insn-00afdbb0)
- ブロック [`00afdbb0`](#insn-00afdbb0) 範囲 `[['00afdbb0', '00afdbb3']]`
  - `UNCONDITIONAL_JUMP` [`00afdbb0`](#insn-00afdbb0) → [`00afdb94`](#insn-00afdb94)
- ブロック [`00afdbb4`](#insn-00afdbb4) 範囲 `[['00afdbb4', '00afdbbb']]`
  - `CONDITIONAL_JUMP` [`00afdbb8`](#insn-00afdbb8) → [`00afdb60`](#insn-00afdb60)
  - `FALL_THROUGH` [`00afdbb8`](#insn-00afdbb8) → [`00afdbbc`](#insn-00afdbbc)
- ブロック [`00afdbbc`](#insn-00afdbbc) 範囲 `[['00afdbbc', '00afdbbf']]`
  - `FALL_THROUGH` [`00afdbbc`](#insn-00afdbbc) → [`00afdbc0`](#insn-00afdbc0)
- ブロック [`00afdbc0`](#insn-00afdbc0) 範囲 `[['00afdbc0', '00afdbc7']]`
  - `UNCONDITIONAL_JUMP` [`00afdbc4`](#insn-00afdbc4) → [`00afdbdc`](#insn-00afdbdc)
- ブロック [`00afdbc8`](#insn-00afdbc8) 範囲 `[['00afdbc8', '00afdbcf']]`
  - `UNCONDITIONAL_JUMP` [`00afdbcc`](#insn-00afdbcc) → [`00afdbd4`](#insn-00afdbd4)
- ブロック [`00afdbd0`](#insn-00afdbd0) 範囲 `[['00afdbd0', '00afdbd3']]`
  - `FALL_THROUGH` [`00afdbd0`](#insn-00afdbd0) → [`00afdbd4`](#insn-00afdbd4)
- ブロック [`00afdbd4`](#insn-00afdbd4) 範囲 `[['00afdbd4', '00afdbdb']]`
  - `FALL_THROUGH` [`00afdbd8`](#insn-00afdbd8) → [`00afdbdc`](#insn-00afdbdc)
- ブロック [`00afdbdc`](#insn-00afdbdc) 範囲 `[['00afdbdc', '00afdbeb']]`
  - `CONDITIONAL_JUMP` [`00afdbe8`](#insn-00afdbe8) → [`00afdc00`](#insn-00afdc00)
  - `FALL_THROUGH` [`00afdbe8`](#insn-00afdbe8) → [`00afdbec`](#insn-00afdbec)
- ブロック [`00afdbec`](#insn-00afdbec) 範囲 `[['00afdbec', '00afdbff']]`
- ブロック [`00afdc00`](#insn-00afdc00) 範囲 `[['00afdc00', '00afdc03']]`

## 命令位置別の参照

- [`00afdb30`](#insn-00afdb30) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdb34`](#insn-00afdb34) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdb38`](#insn-00afdb38) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdb4c`](#insn-00afdb4c) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdb54`](#insn-00afdb54) → [`00afdbb4`](#insn-00afdbb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdb5c`](#insn-00afdb5c) → [`00afdbbc`](#insn-00afdbbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdb64`](#insn-00afdb64) → [`00bdecf0`](../00bde/00bdecf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdecf0` · 推定シンボル `None` · 推定型 `None`
- [`00afdb68`](#insn-00afdb68) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdb70`](#insn-00afdb70) → [`00bdece0`](../00bde/00bdece0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdece0` · 推定シンボル `None` · 推定型 `None`
- [`00afdb74`](#insn-00afdb74) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdb78`](#insn-00afdb78) → [`00afdbdc`](#insn-00afdbdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdb7c`](#insn-00afdb7c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdb84`](#insn-00afdb84) → [`00afdbd0`](#insn-00afdbd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdb90`](#insn-00afdb90) → [`00afdba8`](#insn-00afdba8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdb9c`](#insn-00afdb9c) → [`00afdbc8`](#insn-00afdbc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdba4`](#insn-00afdba4) → [`00afdb94`](#insn-00afdb94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbac`](#insn-00afdbac) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00afdbb0`](#insn-00afdbb0) → [`00afdb94`](#insn-00afdb94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbb8`](#insn-00afdbb8) → [`00afdb60`](#insn-00afdb60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbc4`](#insn-00afdbc4) → [`00afdbdc`](#insn-00afdbdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbc8`](#insn-00afdbc8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbcc`](#insn-00afdbcc) → [`00afdbd4`](#insn-00afdbd4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbd4`](#insn-00afdbd4) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbd8`](#insn-00afdbd8) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00afdbe0`](#insn-00afdbe0) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbe8`](#insn-00afdbe8) → [`00afdc00`](#insn-00afdc00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbec`](#insn-00afdbec) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbf0`](#insn-00afdbf0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbf4`](#insn-00afdbf4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdc00`](#insn-00afdc00) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afdb30`](#insn-00afdb30)

~~~json
{
  "source": "00afdb30",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdb34`](#insn-00afdb34)

~~~json
{
  "source": "00afdb34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdb38`](#insn-00afdb38)

~~~json
{
  "source": "00afdb38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdb4c`](#insn-00afdb4c)

~~~json
{
  "source": "00afdb4c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdb54`](#insn-00afdb54)

~~~json
{
  "source": "00afdb54",
  "target": "00afdbb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdb5c`](#insn-00afdb5c)

~~~json
{
  "source": "00afdb5c",
  "target": "00afdbbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdb64`](#insn-00afdb64)

~~~json
{
  "source": "00afdb64",
  "target": "00bdecf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdb68`](#insn-00afdb68)

~~~json
{
  "source": "00afdb68",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdb70`](#insn-00afdb70)

~~~json
{
  "source": "00afdb70",
  "target": "00bdece0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdb74`](#insn-00afdb74)

~~~json
{
  "source": "00afdb74",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdb78`](#insn-00afdb78)

~~~json
{
  "source": "00afdb78",
  "target": "00afdbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdb7c`](#insn-00afdb7c)

~~~json
{
  "source": "00afdb7c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdb84`](#insn-00afdb84)

~~~json
{
  "source": "00afdb84",
  "target": "00afdbd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdb90`](#insn-00afdb90)

~~~json
{
  "source": "00afdb90",
  "target": "00afdba8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdb9c`](#insn-00afdb9c)

~~~json
{
  "source": "00afdb9c",
  "target": "00afdbc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdba4`](#insn-00afdba4)

~~~json
{
  "source": "00afdba4",
  "target": "00afdb94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbac`](#insn-00afdbac)

~~~json
{
  "source": "00afdbac",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdbb0`](#insn-00afdbb0)

~~~json
{
  "source": "00afdbb0",
  "target": "00afdb94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbb8`](#insn-00afdbb8)

~~~json
{
  "source": "00afdbb8",
  "target": "00afdb60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbc4`](#insn-00afdbc4)

~~~json
{
  "source": "00afdbc4",
  "target": "00afdbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbc8`](#insn-00afdbc8)

~~~json
{
  "source": "00afdbc8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbcc`](#insn-00afdbcc)

~~~json
{
  "source": "00afdbcc",
  "target": "00afdbd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbd4`](#insn-00afdbd4)

~~~json
{
  "source": "00afdbd4",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbd8`](#insn-00afdbd8)

~~~json
{
  "source": "00afdbd8",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdbe0`](#insn-00afdbe0)

~~~json
{
  "source": "00afdbe0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbe8`](#insn-00afdbe8)

~~~json
{
  "source": "00afdbe8",
  "target": "00afdc00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbec`](#insn-00afdbec)

~~~json
{
  "source": "00afdbec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbf0`](#insn-00afdbf0)

~~~json
{
  "source": "00afdbf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbf4`](#insn-00afdbf4)

~~~json
{
  "source": "00afdbf4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdc00`](#insn-00afdc00)

~~~json
{
  "source": "00afdc00",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
