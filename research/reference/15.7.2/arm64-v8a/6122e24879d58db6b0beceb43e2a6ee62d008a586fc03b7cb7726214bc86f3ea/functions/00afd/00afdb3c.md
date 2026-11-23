# 00afdb3c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afdc04`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afdc04.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0063.md#compare-dd5e8509f2644e63a4891378f1be38f3)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afdb3c",
  "name": "_ZNK8firebase4Path17PopFrontDirectoryEv",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a4564bd10acc91dcec4463139f5c7b9c83920fe2d0adfac13ced124f9f03f892",
  "source_text_sha256": "a4564bd10acc91dcec4463139f5c7b9c83920fe2d0adfac13ced124f9f03f892",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afdb3c",
        "00afdc33"
      ]
    ],
    "bytes_sha256": "781d661134c65bee3dc785e2345589a21afa3f62a9ef4685d5d69921c8eee2d8",
    "instruction_count": 62,
    "instruction_bytes": 248,
    "body_bytes": 248,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00afd1a0](../00afd/00afd1a0.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdec30](../00bde/00bdec30.md)
- [00bdec40](../00bde/00bdec40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1871 bytes

~~~c

void _ZNK8firebase4Path17PopFrontDirectoryEv(undefined8 *param_1,byte *param_2)

{
  byte bVar1;
  long lVar2;
  byte *pbVar3;
  byte *pbVar4;
  byte *pbVar5;
  byte *local_68;
  byte *local_60;
  byte local_50 [16];
  void *local_40;
  long local_38;
  
                    /* try { // try from 00afdb40 to 00bfdb5b has its CatchHandler @ 00afecd4 */
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
                    /* try { // try from 00afdb60 to 00bfdb6f has its CatchHandler @ 00b0037c */
  if ((*param_2 & 1) == 0) {
    if (*param_2 >> 1 == 0) {
LAB_00afdbec:
      *param_1 = 0;
      param_1[1] = 0;
      param_1[2] = 0;
      goto LAB_00afdc0c;
    }
  }
  else if (*(long *)(param_2 + 8) == 0) goto LAB_00afdbec;
  _ZNK8firebase4Path14GetDirectoriesEv(&local_68);
  FUN_00afd1a0(local_50,local_68 + 0x18,local_60);
  _ZN8firebase4Path16NormalizeSlashesERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
            (param_1,local_50);
  if ((local_50[0] & 1) != 0) {
    _ZdlPv(local_40);
  }
  pbVar4 = local_68;
  if (local_68 != (byte *)0x0) {
                    /* try { // try from 00afdbb0 to 00bfdbbb has its CatchHandler @ 00afecd0 */
    if (local_60 != local_68) {
      bVar1 = local_60[-0x18];
      pbVar5 = local_60 + -0x18;
      while( true ) {
        pbVar3 = pbVar5;
                    /* try { // try from 00afdbc0 to 00bfdbdb has its CatchHandler @ 00afeccc */
        if ((bVar1 & 1) != 0) {
          _ZdlPv(*(void **)(local_60 + -8));
        }
        if (pbVar4 == pbVar3) break;
        bVar1 = pbVar3[-0x18];
        pbVar5 = pbVar3 + -0x18;
        local_60 = pbVar3;
      }
    }
    local_60 = pbVar4;
    _ZdlPv(local_68);
  }
LAB_00afdc0c:
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
<a id="insn-00afdb3c"></a> `00afdb3c` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00afdb40"></a> `00afdb40` | `f5 23 00 f9` | str x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afdb44"></a> `00afdb44` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afdb48"></a> `00afdb48` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00afdb4c"></a> `00afdb4c` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00afdb50"></a> `00afdb50` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00afdb54"></a> `00afdb54` | `89 16 40 f9` | ldr x9,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00afdb58"></a> `00afdb58` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00afdb5c"></a> `00afdb5c` | `a9 83 1d f8` | stur x9,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00afdb60"></a> `00afdb60` | `09 00 40 39` | ldrb w9,[x0] | `FALL_THROUGH`
<a id="insn-00afdb64"></a> `00afdb64` | `09 04 00 37` | tbnz w9,#0x0,0x00afdbe4 | `CONDITIONAL_JUMP`
<a id="insn-00afdb68"></a> `00afdb68` | `28 fd 41 d3` | lsr x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00afdb6c"></a> `00afdb6c` | `08 04 00 b4` | cbz x8,0x00afdbec | `CONDITIONAL_JUMP`
<a id="insn-00afdb70"></a> `00afdb70` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00afdb74"></a> `00afdb74` | `33 84 03 94` | bl 0x00bdec40 | `UNCONDITIONAL_CALL`
<a id="insn-00afdb78"></a> `00afdb78` | `e8 87 40 a9` | ldp x8,x1,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00afdb7c"></a> `00afdb7c` | `00 61 00 91` | add x0,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00afdb80"></a> `00afdb80` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00afdb84"></a> `00afdb84` | `87 fd ff 97` | bl 0x00afd1a0 | `UNCONDITIONAL_CALL`
<a id="insn-00afdb88"></a> `00afdb88` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00afdb8c"></a> `00afdb8c` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00afdb90"></a> `00afdb90` | `28 84 03 94` | bl 0x00bdec30 | `UNCONDITIONAL_CALL`
<a id="insn-00afdb94"></a> `00afdb94` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afdb98"></a> `00afdb98` | `68 00 00 36` | tbz w8,#0x0,0x00afdba4 | `CONDITIONAL_JUMP`
<a id="insn-00afdb9c"></a> `00afdb9c` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afdba0"></a> `00afdba0` | `f0 74 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00afdba4"></a> `00afdba4` | `f3 07 40 f9` | ldr x19,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00afdba8"></a> `00afdba8` | `33 03 00 b4` | cbz x19,0x00afdc0c | `CONDITIONAL_JUMP`
<a id="insn-00afdbac"></a> `00afdbac` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afdbb0"></a> `00afdbb0` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00afdbb4"></a> `00afdbb4` | `60 02 00 54` | b.eq 0x00afdc00 | `CONDITIONAL_JUMP`
<a id="insn-00afdbb8"></a> `00afdbb8` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00afdbbc"></a> `00afdbbc` | `a9 8e 5e 38` | ldrb w9,[x21, #-0x18]! | `FALL_THROUGH`
<a id="insn-00afdbc0"></a> `00afdbc0` | `c9 00 00 37` | tbnz w9,#0x0,0x00afdbd8 | `CONDITIONAL_JUMP`
<a id="insn-00afdbc4"></a> `00afdbc4` | `7f 02 15 eb` | cmp x19,x21 | `FALL_THROUGH`
<a id="insn-00afdbc8"></a> `00afdbc8` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00afdbcc"></a> `00afdbcc` | `60 01 00 54` | b.eq 0x00afdbf8 | `CONDITIONAL_JUMP`
<a id="insn-00afdbd0"></a> `00afdbd0` | `a9 8e 5e 38` | ldrb w9,[x21, #-0x18]! | `FALL_THROUGH`
<a id="insn-00afdbd4"></a> `00afdbd4` | `89 ff 07 36` | tbz w9,#0x0,0x00afdbc4 | `CONDITIONAL_JUMP`
<a id="insn-00afdbd8"></a> `00afdbd8` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00afdbdc"></a> `00afdbdc` | `e1 74 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00afdbe0"></a> `00afdbe0` | `f9 ff ff 17` | b 0x00afdbc4 | `UNCONDITIONAL_JUMP`
<a id="insn-00afdbe4"></a> `00afdbe4` | `08 04 40 f9` | ldr x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00afdbe8"></a> `00afdbe8` | `48 fc ff b5` | cbnz x8,0x00afdb70 | `CONDITIONAL_JUMP`
<a id="insn-00afdbec"></a> `00afdbec` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00afdbf0"></a> `00afdbf0` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00afdbf4"></a> `00afdbf4` | `06 00 00 14` | b 0x00afdc0c | `UNCONDITIONAL_JUMP`
<a id="insn-00afdbf8"></a> `00afdbf8` | `e0 07 40 f9` | ldr x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00afdbfc"></a> `00afdbfc` | `02 00 00 14` | b 0x00afdc04 | `UNCONDITIONAL_JUMP`
<a id="insn-00afdc00"></a> `00afdc00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afdc04"></a> `00afdc04` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afdc08"></a> `00afdc08` | `d6 74 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00afdc0c"></a> `00afdc0c` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00afdc10"></a> `00afdc10` | `a9 83 5d f8` | ldur x9,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00afdc14"></a> `00afdc14` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00afdc18"></a> `00afdc18` | `c1 00 00 54` | b.ne 0x00afdc30 | `CONDITIONAL_JUMP`
<a id="insn-00afdc1c"></a> `00afdc1c` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00afdc20"></a> `00afdc20` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afdc24"></a> `00afdc24` | `f5 23 40 f9` | ldr x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afdc28"></a> `00afdc28` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00afdc2c"></a> `00afdc2c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afdc30"></a> `00afdc30` | `d8 74 03 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afdb3c`](#insn-00afdb3c) 範囲 `[['00afdb3c', '00afdb3f']]`
  - `FALL_THROUGH` [`00afdb3c`](#insn-00afdb3c) → [`00afdb40`](#insn-00afdb40)
- ブロック [`00afdb40`](#insn-00afdb40) 範囲 `[['00afdb40', '00afdb5f']]`
  - `FALL_THROUGH` [`00afdb5c`](#insn-00afdb5c) → [`00afdb60`](#insn-00afdb60)
- ブロック [`00afdb60`](#insn-00afdb60) 範囲 `[['00afdb60', '00afdb67']]`
  - `CONDITIONAL_JUMP` [`00afdb64`](#insn-00afdb64) → [`00afdbe4`](#insn-00afdbe4)
  - `FALL_THROUGH` [`00afdb64`](#insn-00afdb64) → [`00afdb68`](#insn-00afdb68)
- ブロック [`00afdb68`](#insn-00afdb68) 範囲 `[['00afdb68', '00afdb6f']]`
  - `CONDITIONAL_JUMP` [`00afdb6c`](#insn-00afdb6c) → [`00afdbec`](#insn-00afdbec)
  - `FALL_THROUGH` [`00afdb6c`](#insn-00afdb6c) → [`00afdb70`](#insn-00afdb70)
- ブロック [`00afdb70`](#insn-00afdb70) 範囲 `[['00afdb70', '00afdb9b']]`
  - `CONDITIONAL_JUMP` [`00afdb98`](#insn-00afdb98) → [`00afdba4`](#insn-00afdba4)
  - `FALL_THROUGH` [`00afdb98`](#insn-00afdb98) → [`00afdb9c`](#insn-00afdb9c)
- ブロック [`00afdb9c`](#insn-00afdb9c) 範囲 `[['00afdb9c', '00afdba3']]`
  - `FALL_THROUGH` [`00afdba0`](#insn-00afdba0) → [`00afdba4`](#insn-00afdba4)
- ブロック [`00afdba4`](#insn-00afdba4) 範囲 `[['00afdba4', '00afdbab']]`
  - `CONDITIONAL_JUMP` [`00afdba8`](#insn-00afdba8) → [`00afdc0c`](#insn-00afdc0c)
  - `FALL_THROUGH` [`00afdba8`](#insn-00afdba8) → [`00afdbac`](#insn-00afdbac)
- ブロック [`00afdbac`](#insn-00afdbac) 範囲 `[['00afdbac', '00afdbaf']]`
  - `FALL_THROUGH` [`00afdbac`](#insn-00afdbac) → [`00afdbb0`](#insn-00afdbb0)
- ブロック [`00afdbb0`](#insn-00afdbb0) 範囲 `[['00afdbb0', '00afdbb7']]`
  - `CONDITIONAL_JUMP` [`00afdbb4`](#insn-00afdbb4) → [`00afdc00`](#insn-00afdc00)
  - `FALL_THROUGH` [`00afdbb4`](#insn-00afdbb4) → [`00afdbb8`](#insn-00afdbb8)
- ブロック [`00afdbb8`](#insn-00afdbb8) 範囲 `[['00afdbb8', '00afdbbf']]`
  - `FALL_THROUGH` [`00afdbbc`](#insn-00afdbbc) → [`00afdbc0`](#insn-00afdbc0)
- ブロック [`00afdbc0`](#insn-00afdbc0) 範囲 `[['00afdbc0', '00afdbc3']]`
  - `CONDITIONAL_JUMP` [`00afdbc0`](#insn-00afdbc0) → [`00afdbd8`](#insn-00afdbd8)
  - `FALL_THROUGH` [`00afdbc0`](#insn-00afdbc0) → [`00afdbc4`](#insn-00afdbc4)
- ブロック [`00afdbc4`](#insn-00afdbc4) 範囲 `[['00afdbc4', '00afdbcf']]`
  - `CONDITIONAL_JUMP` [`00afdbcc`](#insn-00afdbcc) → [`00afdbf8`](#insn-00afdbf8)
  - `FALL_THROUGH` [`00afdbcc`](#insn-00afdbcc) → [`00afdbd0`](#insn-00afdbd0)
- ブロック [`00afdbd0`](#insn-00afdbd0) 範囲 `[['00afdbd0', '00afdbd7']]`
  - `CONDITIONAL_JUMP` [`00afdbd4`](#insn-00afdbd4) → [`00afdbc4`](#insn-00afdbc4)
  - `FALL_THROUGH` [`00afdbd4`](#insn-00afdbd4) → [`00afdbd8`](#insn-00afdbd8)
- ブロック [`00afdbd8`](#insn-00afdbd8) 範囲 `[['00afdbd8', '00afdbe3']]`
  - `UNCONDITIONAL_JUMP` [`00afdbe0`](#insn-00afdbe0) → [`00afdbc4`](#insn-00afdbc4)
- ブロック [`00afdbe4`](#insn-00afdbe4) 範囲 `[['00afdbe4', '00afdbeb']]`
  - `CONDITIONAL_JUMP` [`00afdbe8`](#insn-00afdbe8) → [`00afdb70`](#insn-00afdb70)
  - `FALL_THROUGH` [`00afdbe8`](#insn-00afdbe8) → [`00afdbec`](#insn-00afdbec)
- ブロック [`00afdbec`](#insn-00afdbec) 範囲 `[['00afdbec', '00afdbf7']]`
  - `UNCONDITIONAL_JUMP` [`00afdbf4`](#insn-00afdbf4) → [`00afdc0c`](#insn-00afdc0c)
- ブロック [`00afdbf8`](#insn-00afdbf8) 範囲 `[['00afdbf8', '00afdbff']]`
  - `UNCONDITIONAL_JUMP` [`00afdbfc`](#insn-00afdbfc) → [`00afdc04`](#insn-00afdc04)
- ブロック [`00afdc00`](#insn-00afdc00) 範囲 `[['00afdc00', '00afdc03']]`
  - `FALL_THROUGH` [`00afdc00`](#insn-00afdc00) → [`00afdc04`](#insn-00afdc04)
- ブロック [`00afdc04`](#insn-00afdc04) 範囲 `[['00afdc04', '00afdc0b']]`
  - `FALL_THROUGH` [`00afdc08`](#insn-00afdc08) → [`00afdc0c`](#insn-00afdc0c)
- ブロック [`00afdc0c`](#insn-00afdc0c) 範囲 `[['00afdc0c', '00afdc1b']]`
  - `CONDITIONAL_JUMP` [`00afdc18`](#insn-00afdc18) → [`00afdc30`](#insn-00afdc30)
  - `FALL_THROUGH` [`00afdc18`](#insn-00afdc18) → [`00afdc1c`](#insn-00afdc1c)
- ブロック [`00afdc1c`](#insn-00afdc1c) 範囲 `[['00afdc1c', '00afdc2f']]`
- ブロック [`00afdc30`](#insn-00afdc30) 範囲 `[['00afdc30', '00afdc33']]`

## 命令位置別の参照

- [`00afdb40`](#insn-00afdb40) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdb44`](#insn-00afdb44) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdb48`](#insn-00afdb48) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdb5c`](#insn-00afdb5c) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdb64`](#insn-00afdb64) → [`00afdbe4`](#insn-00afdbe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdb6c`](#insn-00afdb6c) → [`00afdbec`](#insn-00afdbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdb74`](#insn-00afdb74) → [`00bdec40`](../00bde/00bdec40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdec40` · 推定シンボル `None` · 推定型 `None`
- [`00afdb78`](#insn-00afdb78) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdb84`](#insn-00afdb84) → [`00afd1a0`](00afd1a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00afd1a0` · 推定シンボル `None` · 推定型 `None`
- [`00afdb90`](#insn-00afdb90) → [`00bdec30`](../00bde/00bdec30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdec30` · 推定シンボル `None` · 推定型 `None`
- [`00afdb94`](#insn-00afdb94) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdb98`](#insn-00afdb98) → [`00afdba4`](#insn-00afdba4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdb9c`](#insn-00afdb9c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdba0`](#insn-00afdba0) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00afdba4`](#insn-00afdba4) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdba8`](#insn-00afdba8) → [`00afdc0c`](#insn-00afdc0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbac`](#insn-00afdbac) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbb4`](#insn-00afdbb4) → [`00afdc00`](#insn-00afdc00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbc0`](#insn-00afdbc0) → [`00afdbd8`](#insn-00afdbd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbcc`](#insn-00afdbcc) → [`00afdbf8`](#insn-00afdbf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbd4`](#insn-00afdbd4) → [`00afdbc4`](#insn-00afdbc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbdc`](#insn-00afdbdc) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00afdbe0`](#insn-00afdbe0) → [`00afdbc4`](#insn-00afdbc4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbe8`](#insn-00afdbe8) → [`00afdb70`](#insn-00afdb70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbf4`](#insn-00afdbf4) → [`00afdc0c`](#insn-00afdc0c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbf8`](#insn-00afdbf8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdbfc`](#insn-00afdbfc) → [`00afdc04`](#insn-00afdc04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdc04`](#insn-00afdc04) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdc08`](#insn-00afdc08) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00afdc10`](#insn-00afdc10) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdc18`](#insn-00afdc18) → [`00afdc30`](#insn-00afdc30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdc1c`](#insn-00afdc1c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdc20`](#insn-00afdc20) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdc24`](#insn-00afdc24) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afdc30`](#insn-00afdc30) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afdb40`](#insn-00afdb40)

~~~json
{
  "source": "00afdb40",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdb44`](#insn-00afdb44)

~~~json
{
  "source": "00afdb44",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdb48`](#insn-00afdb48)

~~~json
{
  "source": "00afdb48",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdb5c`](#insn-00afdb5c)

~~~json
{
  "source": "00afdb5c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdb64`](#insn-00afdb64)

~~~json
{
  "source": "00afdb64",
  "target": "00afdbe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdb6c`](#insn-00afdb6c)

~~~json
{
  "source": "00afdb6c",
  "target": "00afdbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdb74`](#insn-00afdb74)

~~~json
{
  "source": "00afdb74",
  "target": "00bdec40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdb78`](#insn-00afdb78)

~~~json
{
  "source": "00afdb78",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdb84`](#insn-00afdb84)

~~~json
{
  "source": "00afdb84",
  "target": "00afd1a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdb90`](#insn-00afdb90)

~~~json
{
  "source": "00afdb90",
  "target": "00bdec30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdb94`](#insn-00afdb94)

~~~json
{
  "source": "00afdb94",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdb98`](#insn-00afdb98)

~~~json
{
  "source": "00afdb98",
  "target": "00afdba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdb9c`](#insn-00afdb9c)

~~~json
{
  "source": "00afdb9c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdba0`](#insn-00afdba0)

~~~json
{
  "source": "00afdba0",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdba4`](#insn-00afdba4)

~~~json
{
  "source": "00afdba4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdba8`](#insn-00afdba8)

~~~json
{
  "source": "00afdba8",
  "target": "00afdc0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbac`](#insn-00afdbac)

~~~json
{
  "source": "00afdbac",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbb4`](#insn-00afdbb4)

~~~json
{
  "source": "00afdbb4",
  "target": "00afdc00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbc0`](#insn-00afdbc0)

~~~json
{
  "source": "00afdbc0",
  "target": "00afdbd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbcc`](#insn-00afdbcc)

~~~json
{
  "source": "00afdbcc",
  "target": "00afdbf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbd4`](#insn-00afdbd4)

~~~json
{
  "source": "00afdbd4",
  "target": "00afdbc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbdc`](#insn-00afdbdc)

~~~json
{
  "source": "00afdbdc",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdbe0`](#insn-00afdbe0)

~~~json
{
  "source": "00afdbe0",
  "target": "00afdbc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbe8`](#insn-00afdbe8)

~~~json
{
  "source": "00afdbe8",
  "target": "00afdb70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbf4`](#insn-00afdbf4)

~~~json
{
  "source": "00afdbf4",
  "target": "00afdc0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbf8`](#insn-00afdbf8)

~~~json
{
  "source": "00afdbf8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdbfc`](#insn-00afdbfc)

~~~json
{
  "source": "00afdbfc",
  "target": "00afdc04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdc04`](#insn-00afdc04)

~~~json
{
  "source": "00afdc04",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdc08`](#insn-00afdc08)

~~~json
{
  "source": "00afdc08",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afdc10`](#insn-00afdc10)

~~~json
{
  "source": "00afdc10",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdc18`](#insn-00afdc18)

~~~json
{
  "source": "00afdc18",
  "target": "00afdc30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdc1c`](#insn-00afdc1c)

~~~json
{
  "source": "00afdc1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdc20`](#insn-00afdc20)

~~~json
{
  "source": "00afdc20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdc24`](#insn-00afdc24)

~~~json
{
  "source": "00afdc24",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afdc30`](#insn-00afdc30)

~~~json
{
  "source": "00afdc30",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
