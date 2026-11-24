# 00afacd0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afac8c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afac8c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-c88651b0f6ac1d162c1b80a6567d9942)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b5aa54`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5aa54.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0015.md#compare-93a8477cb6a53298f65e676e5614d61e)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afacd0",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDataENS_14default_deleteISB_EEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE4findIS7_EENS_15__tree_iteratorISF_PNS_11__tree_nodeISF_PvEElEERKT_",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f89570611937f2216082477b96ce724c5170eea25f84d3a1cc0b82c8733d7bf0",
  "source_text_sha256": "f89570611937f2216082477b96ce724c5170eea25f84d3a1cc0b82c8733d7bf0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afacd0",
        "00afade3"
      ]
    ],
    "bytes_sha256": "32de8d492600d39db54cae8f6d34f74a61e5af53df76a6b42eb7aa7cc1666289",
    "instruction_count": 69,
    "instruction_bytes": 276,
    "body_bytes": 276,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bde990](../00bde/00bde990.md)

## 呼び出し先

- [00bdb200](../00bdb/00bdb200.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2739 bytes

~~~c

long * _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDataENS_14default_deleteISB_EEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE4findIS7_EENS_15__tree_iteratorISF_PNS_11__tree_nodeISF_PvEElEERKT_
                 (long param_1,byte *param_2)

{
  ulong uVar1;
  size_t sVar2;
  ulong uVar3;
  byte *__s2;
  byte bVar4;
  uint uVar5;
  int iVar6;
  void *pvVar7;
  long *plVar8;
  long *plVar9;
  long *plVar10;
  
  plVar8 = (long *)(param_1 + 8);
  plVar10 = (long *)*plVar8;
  if (plVar10 != (long *)0x0) {
    uVar3 = *(ulong *)(param_2 + 8);
    __s2 = *(byte **)(param_2 + 0x10);
    plVar9 = plVar8;
    if ((*param_2 & 1) == 0) {
                    /* try { // try from 00afad08 to 00bfad17 has its CatchHandler @ 00aff558 */
      __s2 = param_2 + 1;
      uVar3 = (ulong)(*param_2 >> 1);
    }
    do {
      bVar4 = *(byte *)(plVar10 + 4);
      uVar1 = (ulong)(bVar4 >> 1);
      if ((bVar4 & 1) != 0) {
        uVar1 = plVar10[5];
      }
      sVar2 = uVar3;
      if (uVar1 <= uVar3) {
        sVar2 = uVar1;
      }
                    /* try { // try from 00afad54 to 00bfad67 has its CatchHandler @ 00aff554 */
      if (sVar2 == 0) {
LAB_00afad10:
        uVar5 = (uint)(uVar3 < uVar1);
        if (uVar1 < uVar3) {
          uVar5 = 0xffffffff;
        }
      }
      else {
        pvVar7 = (void *)plVar10[6];
        if ((bVar4 & 1) == 0) {
          pvVar7 = (void *)((long)plVar10 + 0x21);
        }
        uVar5 = memcmp(pvVar7,__s2,sVar2);
        if (uVar5 == 0) goto LAB_00afad10;
      }
      if ((int)uVar5 >= 0) {
        plVar9 = plVar10;
      }
      plVar10 = (long *)plVar10[(int)uVar5 < 0];
    } while (plVar10 != (long *)0x0);
                    /* try { // try from 00afad78 to 00bfad7f has its CatchHandler @ 00aff550 */
    if (plVar9 != plVar8) {
      bVar4 = *(byte *)(plVar9 + 4);
      uVar1 = (ulong)(bVar4 >> 1);
      if ((bVar4 & 1) != 0) {
        uVar1 = plVar9[5];
      }
      sVar2 = uVar1;
      if (uVar3 <= uVar1) {
        sVar2 = uVar3;
      }
      if (sVar2 != 0) {
        pvVar7 = (void *)plVar9[6];
                    /* try { // try from 00afada8 to 00bfadbb has its CatchHandler @ 00aff54c */
        if ((bVar4 & 1) == 0) {
          pvVar7 = (void *)((long)plVar9 + 0x21);
        }
        iVar6 = memcmp(__s2,pvVar7,sVar2);
        if (iVar6 != 0) {
          if (iVar6 < 0) {
            return plVar8;
          }
          return plVar9;
        }
      }
      if (uVar1 <= uVar3) {
        return plVar9;
      }
    }
  }
                    /* try { // try from 00afadcc to 00bfadef has its CatchHandler @ 00b003c0 */
  return plVar8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afacd0"></a> `00afacd0` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00afacd4"></a> `00afacd4` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afacd8"></a> `00afacd8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afacdc"></a> `00afacdc` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aface0"></a> `00aface0` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aface4"></a> `00aface4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aface8"></a> `00aface8` | `77 8e 40 f8` | ldr x23,[x19, #0x8]! | `FALL_THROUGH`
<a id="insn-00afacec"></a> `00afacec` | `f7 06 00 b4` | cbz x23,0x00afadc8 | `CONDITIONAL_JUMP`
<a id="insn-00afacf0"></a> `00afacf0` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00afacf4"></a> `00afacf4` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00afacf8"></a> `00afacf8` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00afacfc"></a> `00afacfc` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afad00"></a> `00afad00` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afad04"></a> `00afad04` | `76 01 89 9a` | csel x22,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00afad08"></a> `00afad08` | `55 15 81 9a` | csinc x21,x10,x1,ne | `FALL_THROUGH`
<a id="insn-00afad0c"></a> `00afad0c` | `0a 00 00 14` | b 0x00afad34 | `UNCONDITIONAL_JUMP`
<a id="insn-00afad10"></a> `00afad10` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00afad14"></a> `00afad14` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00afad18"></a> `00afad18` | `1f 03 16 eb` | cmp x24,x22 | `FALL_THROUGH`
<a id="insn-00afad1c"></a> `00afad1c` | `00 21 9f 5a` | csinv w0,w8,wzr,cs | `FALL_THROUGH`
<a id="insn-00afad20"></a> `00afad20` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00afad24"></a> `00afad24` | `e8 a7 9f 1a` | cset w8,lt | `FALL_THROUGH`
<a id="insn-00afad28"></a> `00afad28` | `94 b2 97 9a` | csel x20,x20,x23,lt | `FALL_THROUGH`
<a id="insn-00afad2c"></a> `00afad2c` | `f7 5a 68 f8` | ldr x23,[x23, w8, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00afad30"></a> `00afad30` | `37 02 00 b4` | cbz x23,0x00afad74 | `CONDITIONAL_JUMP`
<a id="insn-00afad34"></a> `00afad34` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-00afad38"></a> `00afad38` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00afad3c"></a> `00afad3c` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00afad40"></a> `00afad40` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00afad44"></a> `00afad44` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00afad48"></a> `00afad48` | `78 01 8a 9a` | csel x24,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00afad4c"></a> `00afad4c` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00afad50"></a> `00afad50` | `c2 32 98 9a` | csel x2,x22,x24,cc | `FALL_THROUGH`
<a id="insn-00afad54"></a> `00afad54` | `e2 fd ff b4` | cbz x2,0x00afad10 | `CONDITIONAL_JUMP`
<a id="insn-00afad58"></a> `00afad58` | `ea 1a 40 f9` | ldr x10,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00afad5c"></a> `00afad5c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00afad60"></a> `00afad60` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00afad64"></a> `00afad64` | `40 15 88 9a` | csinc x0,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00afad68"></a> `00afad68` | `26 81 03 94` | bl 0x00bdb200 | `UNCONDITIONAL_CALL`
<a id="insn-00afad6c"></a> `00afad6c` | `a0 fd ff 35` | cbnz w0,0x00afad20 | `CONDITIONAL_JUMP`
<a id="insn-00afad70"></a> `00afad70` | `e8 ff ff 17` | b 0x00afad10 | `UNCONDITIONAL_JUMP`
<a id="insn-00afad74"></a> `00afad74` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00afad78"></a> `00afad78` | `80 02 00 54` | b.eq 0x00afadc8 | `CONDITIONAL_JUMP`
<a id="insn-00afad7c"></a> `00afad7c` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00afad80"></a> `00afad80` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00afad84"></a> `00afad84` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00afad88"></a> `00afad88` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00afad8c"></a> `00afad8c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00afad90"></a> `00afad90` | `77 01 8a 9a` | csel x23,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00afad94"></a> `00afad94` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00afad98"></a> `00afad98` | `e2 32 96 9a` | csel x2,x23,x22,cc | `FALL_THROUGH`
<a id="insn-00afad9c"></a> `00afad9c` | `22 01 00 b4` | cbz x2,0x00afadc0 | `CONDITIONAL_JUMP`
<a id="insn-00afada0"></a> `00afada0` | `8a 1a 40 f9` | ldr x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00afada4"></a> `00afada4` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00afada8"></a> `00afada8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afadac"></a> `00afadac` | `41 15 88 9a` | csinc x1,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00afadb0"></a> `00afadb0` | `14 81 03 94` | bl 0x00bdb200 | `UNCONDITIONAL_CALL`
<a id="insn-00afadb4"></a> `00afadb4` | `60 00 00 34` | cbz w0,0x00afadc0 | `CONDITIONAL_JUMP`
<a id="insn-00afadb8"></a> `00afadb8` | `80 00 f8 37` | tbnz w0,#0x1f,0x00afadc8 | `CONDITIONAL_JUMP`
<a id="insn-00afadbc"></a> `00afadbc` | `04 00 00 14` | b 0x00afadcc | `UNCONDITIONAL_JUMP`
<a id="insn-00afadc0"></a> `00afadc0` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-00afadc4"></a> `00afadc4` | `42 00 00 54` | b.cs 0x00afadcc | `CONDITIONAL_JUMP`
<a id="insn-00afadc8"></a> `00afadc8` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00afadcc"></a> `00afadcc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afadd0"></a> `00afadd0` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afadd4"></a> `00afadd4` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afadd8"></a> `00afadd8` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afaddc"></a> `00afaddc` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00afade0"></a> `00afade0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afacd0`](#insn-00afacd0) 範囲 `[['00afacd0', '00afacef']]`
  - `CONDITIONAL_JUMP` [`00afacec`](#insn-00afacec) → [`00afadc8`](#insn-00afadc8)
  - `FALL_THROUGH` [`00afacec`](#insn-00afacec) → [`00afacf0`](#insn-00afacf0)
- ブロック [`00afacf0`](#insn-00afacf0) 範囲 `[['00afacf0', '00afad07']]`
  - `FALL_THROUGH` [`00afad04`](#insn-00afad04) → [`00afad08`](#insn-00afad08)
- ブロック [`00afad08`](#insn-00afad08) 範囲 `[['00afad08', '00afad0f']]`
  - `UNCONDITIONAL_JUMP` [`00afad0c`](#insn-00afad0c) → [`00afad34`](#insn-00afad34)
- ブロック [`00afad10`](#insn-00afad10) 範囲 `[['00afad10', '00afad1f']]`
  - `FALL_THROUGH` [`00afad1c`](#insn-00afad1c) → [`00afad20`](#insn-00afad20)
- ブロック [`00afad20`](#insn-00afad20) 範囲 `[['00afad20', '00afad33']]`
  - `CONDITIONAL_JUMP` [`00afad30`](#insn-00afad30) → [`00afad74`](#insn-00afad74)
  - `FALL_THROUGH` [`00afad30`](#insn-00afad30) → [`00afad34`](#insn-00afad34)
- ブロック [`00afad34`](#insn-00afad34) 範囲 `[['00afad34', '00afad53']]`
  - `FALL_THROUGH` [`00afad50`](#insn-00afad50) → [`00afad54`](#insn-00afad54)
- ブロック [`00afad54`](#insn-00afad54) 範囲 `[['00afad54', '00afad57']]`
  - `CONDITIONAL_JUMP` [`00afad54`](#insn-00afad54) → [`00afad10`](#insn-00afad10)
  - `FALL_THROUGH` [`00afad54`](#insn-00afad54) → [`00afad58`](#insn-00afad58)
- ブロック [`00afad58`](#insn-00afad58) 範囲 `[['00afad58', '00afad6f']]`
  - `CONDITIONAL_JUMP` [`00afad6c`](#insn-00afad6c) → [`00afad20`](#insn-00afad20)
  - `FALL_THROUGH` [`00afad6c`](#insn-00afad6c) → [`00afad70`](#insn-00afad70)
- ブロック [`00afad70`](#insn-00afad70) 範囲 `[['00afad70', '00afad73']]`
  - `UNCONDITIONAL_JUMP` [`00afad70`](#insn-00afad70) → [`00afad10`](#insn-00afad10)
- ブロック [`00afad74`](#insn-00afad74) 範囲 `[['00afad74', '00afad77']]`
  - `FALL_THROUGH` [`00afad74`](#insn-00afad74) → [`00afad78`](#insn-00afad78)
- ブロック [`00afad78`](#insn-00afad78) 範囲 `[['00afad78', '00afad7b']]`
  - `CONDITIONAL_JUMP` [`00afad78`](#insn-00afad78) → [`00afadc8`](#insn-00afadc8)
  - `FALL_THROUGH` [`00afad78`](#insn-00afad78) → [`00afad7c`](#insn-00afad7c)
- ブロック [`00afad7c`](#insn-00afad7c) 範囲 `[['00afad7c', '00afad9f']]`
  - `CONDITIONAL_JUMP` [`00afad9c`](#insn-00afad9c) → [`00afadc0`](#insn-00afadc0)
  - `FALL_THROUGH` [`00afad9c`](#insn-00afad9c) → [`00afada0`](#insn-00afada0)
- ブロック [`00afada0`](#insn-00afada0) 範囲 `[['00afada0', '00afada7']]`
  - `FALL_THROUGH` [`00afada4`](#insn-00afada4) → [`00afada8`](#insn-00afada8)
- ブロック [`00afada8`](#insn-00afada8) 範囲 `[['00afada8', '00afadb7']]`
  - `CONDITIONAL_JUMP` [`00afadb4`](#insn-00afadb4) → [`00afadc0`](#insn-00afadc0)
  - `FALL_THROUGH` [`00afadb4`](#insn-00afadb4) → [`00afadb8`](#insn-00afadb8)
- ブロック [`00afadb8`](#insn-00afadb8) 範囲 `[['00afadb8', '00afadbb']]`
  - `CONDITIONAL_JUMP` [`00afadb8`](#insn-00afadb8) → [`00afadc8`](#insn-00afadc8)
  - `FALL_THROUGH` [`00afadb8`](#insn-00afadb8) → [`00afadbc`](#insn-00afadbc)
- ブロック [`00afadbc`](#insn-00afadbc) 範囲 `[['00afadbc', '00afadbf']]`
  - `UNCONDITIONAL_JUMP` [`00afadbc`](#insn-00afadbc) → [`00afadcc`](#insn-00afadcc)
- ブロック [`00afadc0`](#insn-00afadc0) 範囲 `[['00afadc0', '00afadc7']]`
  - `CONDITIONAL_JUMP` [`00afadc4`](#insn-00afadc4) → [`00afadcc`](#insn-00afadcc)
  - `FALL_THROUGH` [`00afadc4`](#insn-00afadc4) → [`00afadc8`](#insn-00afadc8)
- ブロック [`00afadc8`](#insn-00afadc8) 範囲 `[['00afadc8', '00afadcb']]`
  - `FALL_THROUGH` [`00afadc8`](#insn-00afadc8) → [`00afadcc`](#insn-00afadcc)
- ブロック [`00afadcc`](#insn-00afadcc) 範囲 `[['00afadcc', '00afade3']]`

## 命令位置別の参照

- [`00afacd0`](#insn-00afacd0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afacd4`](#insn-00afacd4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afacd8`](#insn-00afacd8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afacdc`](#insn-00afacdc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afacec`](#insn-00afacec) → [`00afadc8`](#insn-00afadc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad0c`](#insn-00afad0c) → [`00afad34`](#insn-00afad34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad30`](#insn-00afad30) → [`00afad74`](#insn-00afad74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad54`](#insn-00afad54) → [`00afad10`](#insn-00afad10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad68`](#insn-00afad68) → [`00bdb200`](../00bdb/00bdb200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb200` · 推定シンボル `None` · 推定型 `None`
- [`00afad6c`](#insn-00afad6c) → [`00afad20`](#insn-00afad20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad70`](#insn-00afad70) → [`00afad10`](#insn-00afad10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad78`](#insn-00afad78) → [`00afadc8`](#insn-00afadc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad9c`](#insn-00afad9c) → [`00afadc0`](#insn-00afadc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afadb0`](#insn-00afadb0) → [`00bdb200`](../00bdb/00bdb200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb200` · 推定シンボル `None` · 推定型 `None`
- [`00afadb4`](#insn-00afadb4) → [`00afadc0`](#insn-00afadc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afadb8`](#insn-00afadb8) → [`00afadc8`](#insn-00afadc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afadbc`](#insn-00afadbc) → [`00afadcc`](#insn-00afadcc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afadc4`](#insn-00afadc4) → [`00afadcc`](#insn-00afadcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afadd0`](#insn-00afadd0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afadd4`](#insn-00afadd4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afadd8`](#insn-00afadd8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afacd0`](#insn-00afacd0)

~~~json
{
  "source": "00afacd0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afacd4`](#insn-00afacd4)

~~~json
{
  "source": "00afacd4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afacd8`](#insn-00afacd8)

~~~json
{
  "source": "00afacd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afacdc`](#insn-00afacdc)

~~~json
{
  "source": "00afacdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afacec`](#insn-00afacec)

~~~json
{
  "source": "00afacec",
  "target": "00afadc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad0c`](#insn-00afad0c)

~~~json
{
  "source": "00afad0c",
  "target": "00afad34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad30`](#insn-00afad30)

~~~json
{
  "source": "00afad30",
  "target": "00afad74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad54`](#insn-00afad54)

~~~json
{
  "source": "00afad54",
  "target": "00afad10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad68`](#insn-00afad68)

~~~json
{
  "source": "00afad68",
  "target": "00bdb200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afad6c`](#insn-00afad6c)

~~~json
{
  "source": "00afad6c",
  "target": "00afad20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad70`](#insn-00afad70)

~~~json
{
  "source": "00afad70",
  "target": "00afad10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad78`](#insn-00afad78)

~~~json
{
  "source": "00afad78",
  "target": "00afadc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad9c`](#insn-00afad9c)

~~~json
{
  "source": "00afad9c",
  "target": "00afadc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afadb0`](#insn-00afadb0)

~~~json
{
  "source": "00afadb0",
  "target": "00bdb200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afadb4`](#insn-00afadb4)

~~~json
{
  "source": "00afadb4",
  "target": "00afadc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afadb8`](#insn-00afadb8)

~~~json
{
  "source": "00afadb8",
  "target": "00afadc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afadbc`](#insn-00afadbc)

~~~json
{
  "source": "00afadbc",
  "target": "00afadcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afadc4`](#insn-00afadc4)

~~~json
{
  "source": "00afadc4",
  "target": "00afadcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afadd0`](#insn-00afadd0)

~~~json
{
  "source": "00afadd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afadd4`](#insn-00afadd4)

~~~json
{
  "source": "00afadd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afadd8`](#insn-00afadd8)

~~~json
{
  "source": "00afadd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
