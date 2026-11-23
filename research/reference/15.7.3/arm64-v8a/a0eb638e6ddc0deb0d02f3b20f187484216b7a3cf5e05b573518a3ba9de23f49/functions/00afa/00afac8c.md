# 00afac8c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00afabc4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afabc4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0062.md#compare-ed4661111446de13cd8d70b9772f090d)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00afacd0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afacd0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-c88651b0f6ac1d162c1b80a6567d9942)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afac8c",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDataENS_14default_deleteISB_EEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE4findIS7_EENS_15__tree_iteratorISF_PNS_11__tree_nodeISF_PvEElEERKT_",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e473f3f021b35503710624234e233a9e6a1bef4f1ac1840a3f1d2518fe5adf50",
  "source_text_sha256": "e473f3f021b35503710624234e233a9e6a1bef4f1ac1840a3f1d2518fe5adf50",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afac8c",
        "00afad9f"
      ]
    ],
    "bytes_sha256": "87ec10a79fd54f8cd7ea8b2132f38f99d0fd6d74dd0cab9b0257db67de6ba3ee",
    "instruction_count": 69,
    "instruction_bytes": 276,
    "body_bytes": 276,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bde940](../00bde/00bde940.md)

## 呼び出し先

- [00bdb1b0](../00bdb/00bdb1b0.md)

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
                    /* try { // try from 00afacc4 to 00bfacd3 has its CatchHandler @ 00aff514 */
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
                    /* try { // try from 00afad10 to 00bfad23 has its CatchHandler @ 00aff510 */
      if (sVar2 == 0) {
LAB_00afaccc:
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
        if (uVar5 == 0) goto LAB_00afaccc;
      }
      if ((int)uVar5 >= 0) {
        plVar9 = plVar10;
      }
      plVar10 = (long *)plVar10[(int)uVar5 < 0];
    } while (plVar10 != (long *)0x0);
                    /* try { // try from 00afad34 to 00bfad3b has its CatchHandler @ 00aff50c */
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
                    /* try { // try from 00afad64 to 00bfad77 has its CatchHandler @ 00aff508 */
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
                    /* try { // try from 00afad88 to 00bfadab has its CatchHandler @ 00b0037c */
  return plVar8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afac8c"></a> `00afac8c` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00afac90"></a> `00afac90` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afac94"></a> `00afac94` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afac98"></a> `00afac98` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afac9c"></a> `00afac9c` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00afaca0"></a> `00afaca0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afaca4"></a> `00afaca4` | `77 8e 40 f8` | ldr x23,[x19, #0x8]! | `FALL_THROUGH`
<a id="insn-00afaca8"></a> `00afaca8` | `f7 06 00 b4` | cbz x23,0x00afad84 | `CONDITIONAL_JUMP`
<a id="insn-00afacac"></a> `00afacac` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00afacb0"></a> `00afacb0` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00afacb4"></a> `00afacb4` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00afacb8"></a> `00afacb8` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afacbc"></a> `00afacbc` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afacc0"></a> `00afacc0` | `76 01 89 9a` | csel x22,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00afacc4"></a> `00afacc4` | `55 15 81 9a` | csinc x21,x10,x1,ne | `FALL_THROUGH`
<a id="insn-00afacc8"></a> `00afacc8` | `0a 00 00 14` | b 0x00afacf0 | `UNCONDITIONAL_JUMP`
<a id="insn-00afaccc"></a> `00afaccc` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00afacd0"></a> `00afacd0` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00afacd4"></a> `00afacd4` | `1f 03 16 eb` | cmp x24,x22 | `FALL_THROUGH`
<a id="insn-00afacd8"></a> `00afacd8` | `00 21 9f 5a` | csinv w0,w8,wzr,cs | `FALL_THROUGH`
<a id="insn-00afacdc"></a> `00afacdc` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00aface0"></a> `00aface0` | `e8 a7 9f 1a` | cset w8,lt | `FALL_THROUGH`
<a id="insn-00aface4"></a> `00aface4` | `94 b2 97 9a` | csel x20,x20,x23,lt | `FALL_THROUGH`
<a id="insn-00aface8"></a> `00aface8` | `f7 5a 68 f8` | ldr x23,[x23, w8, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00afacec"></a> `00afacec` | `37 02 00 b4` | cbz x23,0x00afad30 | `CONDITIONAL_JUMP`
<a id="insn-00afacf0"></a> `00afacf0` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-00afacf4"></a> `00afacf4` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00afacf8"></a> `00afacf8` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00afacfc"></a> `00afacfc` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00afad00"></a> `00afad00` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00afad04"></a> `00afad04` | `78 01 8a 9a` | csel x24,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00afad08"></a> `00afad08` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00afad0c"></a> `00afad0c` | `c2 32 98 9a` | csel x2,x22,x24,cc | `FALL_THROUGH`
<a id="insn-00afad10"></a> `00afad10` | `e2 fd ff b4` | cbz x2,0x00afaccc | `CONDITIONAL_JUMP`
<a id="insn-00afad14"></a> `00afad14` | `ea 1a 40 f9` | ldr x10,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00afad18"></a> `00afad18` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00afad1c"></a> `00afad1c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00afad20"></a> `00afad20` | `40 15 88 9a` | csinc x0,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00afad24"></a> `00afad24` | `23 81 03 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00afad28"></a> `00afad28` | `a0 fd ff 35` | cbnz w0,0x00afacdc | `CONDITIONAL_JUMP`
<a id="insn-00afad2c"></a> `00afad2c` | `e8 ff ff 17` | b 0x00afaccc | `UNCONDITIONAL_JUMP`
<a id="insn-00afad30"></a> `00afad30` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00afad34"></a> `00afad34` | `80 02 00 54` | b.eq 0x00afad84 | `CONDITIONAL_JUMP`
<a id="insn-00afad38"></a> `00afad38` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00afad3c"></a> `00afad3c` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00afad40"></a> `00afad40` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00afad44"></a> `00afad44` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00afad48"></a> `00afad48` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00afad4c"></a> `00afad4c` | `77 01 8a 9a` | csel x23,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00afad50"></a> `00afad50` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00afad54"></a> `00afad54` | `e2 32 96 9a` | csel x2,x23,x22,cc | `FALL_THROUGH`
<a id="insn-00afad58"></a> `00afad58` | `22 01 00 b4` | cbz x2,0x00afad7c | `CONDITIONAL_JUMP`
<a id="insn-00afad5c"></a> `00afad5c` | `8a 1a 40 f9` | ldr x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00afad60"></a> `00afad60` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00afad64"></a> `00afad64` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afad68"></a> `00afad68` | `41 15 88 9a` | csinc x1,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00afad6c"></a> `00afad6c` | `11 81 03 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00afad70"></a> `00afad70` | `60 00 00 34` | cbz w0,0x00afad7c | `CONDITIONAL_JUMP`
<a id="insn-00afad74"></a> `00afad74` | `80 00 f8 37` | tbnz w0,#0x1f,0x00afad84 | `CONDITIONAL_JUMP`
<a id="insn-00afad78"></a> `00afad78` | `04 00 00 14` | b 0x00afad88 | `UNCONDITIONAL_JUMP`
<a id="insn-00afad7c"></a> `00afad7c` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-00afad80"></a> `00afad80` | `42 00 00 54` | b.cs 0x00afad88 | `CONDITIONAL_JUMP`
<a id="insn-00afad84"></a> `00afad84` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00afad88"></a> `00afad88` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afad8c"></a> `00afad8c` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afad90"></a> `00afad90` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afad94"></a> `00afad94` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afad98"></a> `00afad98` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00afad9c"></a> `00afad9c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afac8c`](#insn-00afac8c) 範囲 `[['00afac8c', '00afacab']]`
  - `CONDITIONAL_JUMP` [`00afaca8`](#insn-00afaca8) → [`00afad84`](#insn-00afad84)
  - `FALL_THROUGH` [`00afaca8`](#insn-00afaca8) → [`00afacac`](#insn-00afacac)
- ブロック [`00afacac`](#insn-00afacac) 範囲 `[['00afacac', '00afacc3']]`
  - `FALL_THROUGH` [`00afacc0`](#insn-00afacc0) → [`00afacc4`](#insn-00afacc4)
- ブロック [`00afacc4`](#insn-00afacc4) 範囲 `[['00afacc4', '00afaccb']]`
  - `UNCONDITIONAL_JUMP` [`00afacc8`](#insn-00afacc8) → [`00afacf0`](#insn-00afacf0)
- ブロック [`00afaccc`](#insn-00afaccc) 範囲 `[['00afaccc', '00afacdb']]`
  - `FALL_THROUGH` [`00afacd8`](#insn-00afacd8) → [`00afacdc`](#insn-00afacdc)
- ブロック [`00afacdc`](#insn-00afacdc) 範囲 `[['00afacdc', '00afacef']]`
  - `CONDITIONAL_JUMP` [`00afacec`](#insn-00afacec) → [`00afad30`](#insn-00afad30)
  - `FALL_THROUGH` [`00afacec`](#insn-00afacec) → [`00afacf0`](#insn-00afacf0)
- ブロック [`00afacf0`](#insn-00afacf0) 範囲 `[['00afacf0', '00afad0f']]`
  - `FALL_THROUGH` [`00afad0c`](#insn-00afad0c) → [`00afad10`](#insn-00afad10)
- ブロック [`00afad10`](#insn-00afad10) 範囲 `[['00afad10', '00afad13']]`
  - `CONDITIONAL_JUMP` [`00afad10`](#insn-00afad10) → [`00afaccc`](#insn-00afaccc)
  - `FALL_THROUGH` [`00afad10`](#insn-00afad10) → [`00afad14`](#insn-00afad14)
- ブロック [`00afad14`](#insn-00afad14) 範囲 `[['00afad14', '00afad2b']]`
  - `CONDITIONAL_JUMP` [`00afad28`](#insn-00afad28) → [`00afacdc`](#insn-00afacdc)
  - `FALL_THROUGH` [`00afad28`](#insn-00afad28) → [`00afad2c`](#insn-00afad2c)
- ブロック [`00afad2c`](#insn-00afad2c) 範囲 `[['00afad2c', '00afad2f']]`
  - `UNCONDITIONAL_JUMP` [`00afad2c`](#insn-00afad2c) → [`00afaccc`](#insn-00afaccc)
- ブロック [`00afad30`](#insn-00afad30) 範囲 `[['00afad30', '00afad33']]`
  - `FALL_THROUGH` [`00afad30`](#insn-00afad30) → [`00afad34`](#insn-00afad34)
- ブロック [`00afad34`](#insn-00afad34) 範囲 `[['00afad34', '00afad37']]`
  - `CONDITIONAL_JUMP` [`00afad34`](#insn-00afad34) → [`00afad84`](#insn-00afad84)
  - `FALL_THROUGH` [`00afad34`](#insn-00afad34) → [`00afad38`](#insn-00afad38)
- ブロック [`00afad38`](#insn-00afad38) 範囲 `[['00afad38', '00afad5b']]`
  - `CONDITIONAL_JUMP` [`00afad58`](#insn-00afad58) → [`00afad7c`](#insn-00afad7c)
  - `FALL_THROUGH` [`00afad58`](#insn-00afad58) → [`00afad5c`](#insn-00afad5c)
- ブロック [`00afad5c`](#insn-00afad5c) 範囲 `[['00afad5c', '00afad63']]`
  - `FALL_THROUGH` [`00afad60`](#insn-00afad60) → [`00afad64`](#insn-00afad64)
- ブロック [`00afad64`](#insn-00afad64) 範囲 `[['00afad64', '00afad73']]`
  - `CONDITIONAL_JUMP` [`00afad70`](#insn-00afad70) → [`00afad7c`](#insn-00afad7c)
  - `FALL_THROUGH` [`00afad70`](#insn-00afad70) → [`00afad74`](#insn-00afad74)
- ブロック [`00afad74`](#insn-00afad74) 範囲 `[['00afad74', '00afad77']]`
  - `CONDITIONAL_JUMP` [`00afad74`](#insn-00afad74) → [`00afad84`](#insn-00afad84)
  - `FALL_THROUGH` [`00afad74`](#insn-00afad74) → [`00afad78`](#insn-00afad78)
- ブロック [`00afad78`](#insn-00afad78) 範囲 `[['00afad78', '00afad7b']]`
  - `UNCONDITIONAL_JUMP` [`00afad78`](#insn-00afad78) → [`00afad88`](#insn-00afad88)
- ブロック [`00afad7c`](#insn-00afad7c) 範囲 `[['00afad7c', '00afad83']]`
  - `CONDITIONAL_JUMP` [`00afad80`](#insn-00afad80) → [`00afad88`](#insn-00afad88)
  - `FALL_THROUGH` [`00afad80`](#insn-00afad80) → [`00afad84`](#insn-00afad84)
- ブロック [`00afad84`](#insn-00afad84) 範囲 `[['00afad84', '00afad87']]`
  - `FALL_THROUGH` [`00afad84`](#insn-00afad84) → [`00afad88`](#insn-00afad88)
- ブロック [`00afad88`](#insn-00afad88) 範囲 `[['00afad88', '00afad9f']]`

## 命令位置別の参照

- [`00afac8c`](#insn-00afac8c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac90`](#insn-00afac90) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac94`](#insn-00afac94) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac98`](#insn-00afac98) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaca8`](#insn-00afaca8) → [`00afad84`](#insn-00afad84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afacc8`](#insn-00afacc8) → [`00afacf0`](#insn-00afacf0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afacec`](#insn-00afacec) → [`00afad30`](#insn-00afad30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad10`](#insn-00afad10) → [`00afaccc`](#insn-00afaccc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad24`](#insn-00afad24) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00afad28`](#insn-00afad28) → [`00afacdc`](#insn-00afacdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad2c`](#insn-00afad2c) → [`00afaccc`](#insn-00afaccc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad34`](#insn-00afad34) → [`00afad84`](#insn-00afad84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad58`](#insn-00afad58) → [`00afad7c`](#insn-00afad7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad6c`](#insn-00afad6c) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00afad70`](#insn-00afad70) → [`00afad7c`](#insn-00afad7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad74`](#insn-00afad74) → [`00afad84`](#insn-00afad84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad78`](#insn-00afad78) → [`00afad88`](#insn-00afad88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad80`](#insn-00afad80) → [`00afad88`](#insn-00afad88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad8c`](#insn-00afad8c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad90`](#insn-00afad90) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad94`](#insn-00afad94) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afac8c`](#insn-00afac8c)

~~~json
{
  "source": "00afac8c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac90`](#insn-00afac90)

~~~json
{
  "source": "00afac90",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac94`](#insn-00afac94)

~~~json
{
  "source": "00afac94",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac98`](#insn-00afac98)

~~~json
{
  "source": "00afac98",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaca8`](#insn-00afaca8)

~~~json
{
  "source": "00afaca8",
  "target": "00afad84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afacc8`](#insn-00afacc8)

~~~json
{
  "source": "00afacc8",
  "target": "00afacf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afacec`](#insn-00afacec)

~~~json
{
  "source": "00afacec",
  "target": "00afad30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad10`](#insn-00afad10)

~~~json
{
  "source": "00afad10",
  "target": "00afaccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad24`](#insn-00afad24)

~~~json
{
  "source": "00afad24",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afad28`](#insn-00afad28)

~~~json
{
  "source": "00afad28",
  "target": "00afacdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad2c`](#insn-00afad2c)

~~~json
{
  "source": "00afad2c",
  "target": "00afaccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad34`](#insn-00afad34)

~~~json
{
  "source": "00afad34",
  "target": "00afad84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad58`](#insn-00afad58)

~~~json
{
  "source": "00afad58",
  "target": "00afad7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad6c`](#insn-00afad6c)

~~~json
{
  "source": "00afad6c",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afad70`](#insn-00afad70)

~~~json
{
  "source": "00afad70",
  "target": "00afad7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad74`](#insn-00afad74)

~~~json
{
  "source": "00afad74",
  "target": "00afad84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad78`](#insn-00afad78)

~~~json
{
  "source": "00afad78",
  "target": "00afad88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad80`](#insn-00afad80)

~~~json
{
  "source": "00afad80",
  "target": "00afad88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad8c`](#insn-00afad8c)

~~~json
{
  "source": "00afad8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad90`](#insn-00afad90)

~~~json
{
  "source": "00afad90",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad94`](#insn-00afad94)

~~~json
{
  "source": "00afad94",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
