# 00afabc4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afac8c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afac8c.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0062.md#compare-ed4661111446de13cd8d70b9772f090d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afabc4",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDataENS_14default_deleteISB_EEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE4findIS7_EENS_15__tree_iteratorISF_PNS_11__tree_nodeISF_PvEElEERKT_",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "42d0ca355845d9457afcf862b48602c8b1fae9db1941ba25d61a82fd48a9a0ef",
  "source_text_sha256": "42d0ca355845d9457afcf862b48602c8b1fae9db1941ba25d61a82fd48a9a0ef",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afabc4",
        "00afacd7"
      ]
    ],
    "bytes_sha256": "661d38112a3da6820880cd3fcefcad56d1d5bd85cecb99a146f89e58ecc203b1",
    "instruction_count": 69,
    "instruction_bytes": 276,
    "body_bytes": 276,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bde890](../00bde/00bde890.md)

## 呼び出し先

- [00bdb100](../00bdb/00bdb100.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2836 bytes

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
  
                    /* try { // try from 00afabc4 to 00bfabcb has its CatchHandler @ 00b00238 */
  plVar8 = (long *)(param_1 + 8);
  plVar10 = (long *)*plVar8;
  if (plVar10 != (long *)0x0) {
    uVar3 = *(ulong *)(param_2 + 8);
    __s2 = *(byte **)(param_2 + 0x10);
    plVar9 = plVar8;
    if ((*param_2 & 1) == 0) {
      __s2 = param_2 + 1;
      uVar3 = (ulong)(*param_2 >> 1);
    }
    do {
                    /* try { // try from 00afac28 to 00bfac33 has its CatchHandler @ 00b0023c */
      bVar4 = *(byte *)(plVar10 + 4);
      uVar1 = (ulong)(bVar4 >> 1);
      if ((bVar4 & 1) != 0) {
        uVar1 = plVar10[5];
      }
      sVar2 = uVar3;
      if (uVar1 <= uVar3) {
        sVar2 = uVar1;
      }
      if (sVar2 == 0) {
LAB_00afac04:
        uVar5 = (uint)(uVar3 < uVar1);
                    /* try { // try from 00afac10 to 00bfac17 has its CatchHandler @ 00b001dc */
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
        if (uVar5 == 0) goto LAB_00afac04;
      }
                    /* try { // try from 00afac18 to 00bfac27 has its CatchHandler @ 00b00254 */
      if ((int)uVar5 >= 0) {
        plVar9 = plVar10;
      }
      plVar10 = (long *)plVar10[(int)uVar5 < 0];
    } while (plVar10 != (long *)0x0);
    if (plVar9 != plVar8) {
      bVar4 = *(byte *)(plVar9 + 4);
                    /* try { // try from 00afac7c to 00bfac9b has its CatchHandler @ 00afff3c */
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
                    /* try { // try from 00afacc4 to 00bfacd3 has its CatchHandler @ 00aff514 */
  return plVar8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afabc4"></a> `00afabc4` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00afabc8"></a> `00afabc8` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afabcc"></a> `00afabcc` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afabd0"></a> `00afabd0` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afabd4"></a> `00afabd4` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00afabd8"></a> `00afabd8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afabdc"></a> `00afabdc` | `77 8e 40 f8` | ldr x23,[x19, #0x8]! | `FALL_THROUGH`
<a id="insn-00afabe0"></a> `00afabe0` | `f7 06 00 b4` | cbz x23,0x00afacbc | `CONDITIONAL_JUMP`
<a id="insn-00afabe4"></a> `00afabe4` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00afabe8"></a> `00afabe8` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00afabec"></a> `00afabec` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00afabf0"></a> `00afabf0` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afabf4"></a> `00afabf4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afabf8"></a> `00afabf8` | `76 01 89 9a` | csel x22,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00afabfc"></a> `00afabfc` | `55 15 81 9a` | csinc x21,x10,x1,ne | `FALL_THROUGH`
<a id="insn-00afac00"></a> `00afac00` | `0a 00 00 14` | b 0x00afac28 | `UNCONDITIONAL_JUMP`
<a id="insn-00afac04"></a> `00afac04` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00afac08"></a> `00afac08` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00afac0c"></a> `00afac0c` | `1f 03 16 eb` | cmp x24,x22 | `FALL_THROUGH`
<a id="insn-00afac10"></a> `00afac10` | `00 21 9f 5a` | csinv w0,w8,wzr,cs | `FALL_THROUGH`
<a id="insn-00afac14"></a> `00afac14` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00afac18"></a> `00afac18` | `e8 a7 9f 1a` | cset w8,lt | `FALL_THROUGH`
<a id="insn-00afac1c"></a> `00afac1c` | `94 b2 97 9a` | csel x20,x20,x23,lt | `FALL_THROUGH`
<a id="insn-00afac20"></a> `00afac20` | `f7 5a 68 f8` | ldr x23,[x23, w8, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00afac24"></a> `00afac24` | `37 02 00 b4` | cbz x23,0x00afac68 | `CONDITIONAL_JUMP`
<a id="insn-00afac28"></a> `00afac28` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-00afac2c"></a> `00afac2c` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00afac30"></a> `00afac30` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00afac34"></a> `00afac34` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00afac38"></a> `00afac38` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00afac3c"></a> `00afac3c` | `78 01 8a 9a` | csel x24,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00afac40"></a> `00afac40` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00afac44"></a> `00afac44` | `c2 32 98 9a` | csel x2,x22,x24,cc | `FALL_THROUGH`
<a id="insn-00afac48"></a> `00afac48` | `e2 fd ff b4` | cbz x2,0x00afac04 | `CONDITIONAL_JUMP`
<a id="insn-00afac4c"></a> `00afac4c` | `ea 1a 40 f9` | ldr x10,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00afac50"></a> `00afac50` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00afac54"></a> `00afac54` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00afac58"></a> `00afac58` | `40 15 88 9a` | csinc x0,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00afac5c"></a> `00afac5c` | `29 81 03 94` | bl 0x00bdb100 | `UNCONDITIONAL_CALL`
<a id="insn-00afac60"></a> `00afac60` | `a0 fd ff 35` | cbnz w0,0x00afac14 | `CONDITIONAL_JUMP`
<a id="insn-00afac64"></a> `00afac64` | `e8 ff ff 17` | b 0x00afac04 | `UNCONDITIONAL_JUMP`
<a id="insn-00afac68"></a> `00afac68` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00afac6c"></a> `00afac6c` | `80 02 00 54` | b.eq 0x00afacbc | `CONDITIONAL_JUMP`
<a id="insn-00afac70"></a> `00afac70` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00afac74"></a> `00afac74` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00afac78"></a> `00afac78` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00afac7c"></a> `00afac7c` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00afac80"></a> `00afac80` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00afac84"></a> `00afac84` | `77 01 8a 9a` | csel x23,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00afac88"></a> `00afac88` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00afac8c"></a> `00afac8c` | `e2 32 96 9a` | csel x2,x23,x22,cc | `FALL_THROUGH`
<a id="insn-00afac90"></a> `00afac90` | `22 01 00 b4` | cbz x2,0x00afacb4 | `CONDITIONAL_JUMP`
<a id="insn-00afac94"></a> `00afac94` | `8a 1a 40 f9` | ldr x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00afac98"></a> `00afac98` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00afac9c"></a> `00afac9c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afaca0"></a> `00afaca0` | `41 15 88 9a` | csinc x1,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00afaca4"></a> `00afaca4` | `17 81 03 94` | bl 0x00bdb100 | `UNCONDITIONAL_CALL`
<a id="insn-00afaca8"></a> `00afaca8` | `60 00 00 34` | cbz w0,0x00afacb4 | `CONDITIONAL_JUMP`
<a id="insn-00afacac"></a> `00afacac` | `80 00 f8 37` | tbnz w0,#0x1f,0x00afacbc | `CONDITIONAL_JUMP`
<a id="insn-00afacb0"></a> `00afacb0` | `04 00 00 14` | b 0x00afacc0 | `UNCONDITIONAL_JUMP`
<a id="insn-00afacb4"></a> `00afacb4` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-00afacb8"></a> `00afacb8` | `42 00 00 54` | b.cs 0x00afacc0 | `CONDITIONAL_JUMP`
<a id="insn-00afacbc"></a> `00afacbc` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00afacc0"></a> `00afacc0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afacc4"></a> `00afacc4` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afacc8"></a> `00afacc8` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afaccc"></a> `00afaccc` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afacd0"></a> `00afacd0` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00afacd4"></a> `00afacd4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afabc4`](#insn-00afabc4) 範囲 `[['00afabc4', '00afabe3']]`
  - `CONDITIONAL_JUMP` [`00afabe0`](#insn-00afabe0) → [`00afacbc`](#insn-00afacbc)
  - `FALL_THROUGH` [`00afabe0`](#insn-00afabe0) → [`00afabe4`](#insn-00afabe4)
- ブロック [`00afabe4`](#insn-00afabe4) 範囲 `[['00afabe4', '00afac03']]`
  - `UNCONDITIONAL_JUMP` [`00afac00`](#insn-00afac00) → [`00afac28`](#insn-00afac28)
- ブロック [`00afac04`](#insn-00afac04) 範囲 `[['00afac04', '00afac0f']]`
  - `FALL_THROUGH` [`00afac0c`](#insn-00afac0c) → [`00afac10`](#insn-00afac10)
- ブロック [`00afac10`](#insn-00afac10) 範囲 `[['00afac10', '00afac13']]`
  - `FALL_THROUGH` [`00afac10`](#insn-00afac10) → [`00afac14`](#insn-00afac14)
- ブロック [`00afac14`](#insn-00afac14) 範囲 `[['00afac14', '00afac17']]`
  - `FALL_THROUGH` [`00afac14`](#insn-00afac14) → [`00afac18`](#insn-00afac18)
- ブロック [`00afac18`](#insn-00afac18) 範囲 `[['00afac18', '00afac27']]`
  - `CONDITIONAL_JUMP` [`00afac24`](#insn-00afac24) → [`00afac68`](#insn-00afac68)
  - `FALL_THROUGH` [`00afac24`](#insn-00afac24) → [`00afac28`](#insn-00afac28)
- ブロック [`00afac28`](#insn-00afac28) 範囲 `[['00afac28', '00afac4b']]`
  - `CONDITIONAL_JUMP` [`00afac48`](#insn-00afac48) → [`00afac04`](#insn-00afac04)
  - `FALL_THROUGH` [`00afac48`](#insn-00afac48) → [`00afac4c`](#insn-00afac4c)
- ブロック [`00afac4c`](#insn-00afac4c) 範囲 `[['00afac4c', '00afac63']]`
  - `CONDITIONAL_JUMP` [`00afac60`](#insn-00afac60) → [`00afac14`](#insn-00afac14)
  - `FALL_THROUGH` [`00afac60`](#insn-00afac60) → [`00afac64`](#insn-00afac64)
- ブロック [`00afac64`](#insn-00afac64) 範囲 `[['00afac64', '00afac67']]`
  - `UNCONDITIONAL_JUMP` [`00afac64`](#insn-00afac64) → [`00afac04`](#insn-00afac04)
- ブロック [`00afac68`](#insn-00afac68) 範囲 `[['00afac68', '00afac6f']]`
  - `CONDITIONAL_JUMP` [`00afac6c`](#insn-00afac6c) → [`00afacbc`](#insn-00afacbc)
  - `FALL_THROUGH` [`00afac6c`](#insn-00afac6c) → [`00afac70`](#insn-00afac70)
- ブロック [`00afac70`](#insn-00afac70) 範囲 `[['00afac70', '00afac7b']]`
  - `FALL_THROUGH` [`00afac78`](#insn-00afac78) → [`00afac7c`](#insn-00afac7c)
- ブロック [`00afac7c`](#insn-00afac7c) 範囲 `[['00afac7c', '00afac93']]`
  - `CONDITIONAL_JUMP` [`00afac90`](#insn-00afac90) → [`00afacb4`](#insn-00afacb4)
  - `FALL_THROUGH` [`00afac90`](#insn-00afac90) → [`00afac94`](#insn-00afac94)
- ブロック [`00afac94`](#insn-00afac94) 範囲 `[['00afac94', '00afacab']]`
  - `CONDITIONAL_JUMP` [`00afaca8`](#insn-00afaca8) → [`00afacb4`](#insn-00afacb4)
  - `FALL_THROUGH` [`00afaca8`](#insn-00afaca8) → [`00afacac`](#insn-00afacac)
- ブロック [`00afacac`](#insn-00afacac) 範囲 `[['00afacac', '00afacaf']]`
  - `CONDITIONAL_JUMP` [`00afacac`](#insn-00afacac) → [`00afacbc`](#insn-00afacbc)
  - `FALL_THROUGH` [`00afacac`](#insn-00afacac) → [`00afacb0`](#insn-00afacb0)
- ブロック [`00afacb0`](#insn-00afacb0) 範囲 `[['00afacb0', '00afacb3']]`
  - `UNCONDITIONAL_JUMP` [`00afacb0`](#insn-00afacb0) → [`00afacc0`](#insn-00afacc0)
- ブロック [`00afacb4`](#insn-00afacb4) 範囲 `[['00afacb4', '00afacbb']]`
  - `CONDITIONAL_JUMP` [`00afacb8`](#insn-00afacb8) → [`00afacc0`](#insn-00afacc0)
  - `FALL_THROUGH` [`00afacb8`](#insn-00afacb8) → [`00afacbc`](#insn-00afacbc)
- ブロック [`00afacbc`](#insn-00afacbc) 範囲 `[['00afacbc', '00afacbf']]`
  - `FALL_THROUGH` [`00afacbc`](#insn-00afacbc) → [`00afacc0`](#insn-00afacc0)
- ブロック [`00afacc0`](#insn-00afacc0) 範囲 `[['00afacc0', '00afacc3']]`
  - `FALL_THROUGH` [`00afacc0`](#insn-00afacc0) → [`00afacc4`](#insn-00afacc4)
- ブロック [`00afacc4`](#insn-00afacc4) 範囲 `[['00afacc4', '00afacd7']]`

## 命令位置別の参照

- [`00afabc4`](#insn-00afabc4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afabc8`](#insn-00afabc8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afabcc`](#insn-00afabcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afabd0`](#insn-00afabd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afabe0`](#insn-00afabe0) → [`00afacbc`](#insn-00afacbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac00`](#insn-00afac00) → [`00afac28`](#insn-00afac28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac24`](#insn-00afac24) → [`00afac68`](#insn-00afac68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac48`](#insn-00afac48) → [`00afac04`](#insn-00afac04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac5c`](#insn-00afac5c) → [`00bdb100`](../00bdb/00bdb100.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb100` · 推定シンボル `None` · 推定型 `None`
- [`00afac60`](#insn-00afac60) → [`00afac14`](#insn-00afac14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac64`](#insn-00afac64) → [`00afac04`](#insn-00afac04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac6c`](#insn-00afac6c) → [`00afacbc`](#insn-00afacbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac90`](#insn-00afac90) → [`00afacb4`](#insn-00afacb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaca4`](#insn-00afaca4) → [`00bdb100`](../00bdb/00bdb100.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb100` · 推定シンボル `None` · 推定型 `None`
- [`00afaca8`](#insn-00afaca8) → [`00afacb4`](#insn-00afacb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afacac`](#insn-00afacac) → [`00afacbc`](#insn-00afacbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afacb0`](#insn-00afacb0) → [`00afacc0`](#insn-00afacc0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afacb8`](#insn-00afacb8) → [`00afacc0`](#insn-00afacc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afacc4`](#insn-00afacc4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afacc8`](#insn-00afacc8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaccc`](#insn-00afaccc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afabc4`](#insn-00afabc4)

~~~json
{
  "source": "00afabc4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afabc8`](#insn-00afabc8)

~~~json
{
  "source": "00afabc8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afabcc`](#insn-00afabcc)

~~~json
{
  "source": "00afabcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afabd0`](#insn-00afabd0)

~~~json
{
  "source": "00afabd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afabe0`](#insn-00afabe0)

~~~json
{
  "source": "00afabe0",
  "target": "00afacbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac00`](#insn-00afac00)

~~~json
{
  "source": "00afac00",
  "target": "00afac28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac24`](#insn-00afac24)

~~~json
{
  "source": "00afac24",
  "target": "00afac68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac48`](#insn-00afac48)

~~~json
{
  "source": "00afac48",
  "target": "00afac04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac5c`](#insn-00afac5c)

~~~json
{
  "source": "00afac5c",
  "target": "00bdb100",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afac60`](#insn-00afac60)

~~~json
{
  "source": "00afac60",
  "target": "00afac14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac64`](#insn-00afac64)

~~~json
{
  "source": "00afac64",
  "target": "00afac04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac6c`](#insn-00afac6c)

~~~json
{
  "source": "00afac6c",
  "target": "00afacbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac90`](#insn-00afac90)

~~~json
{
  "source": "00afac90",
  "target": "00afacb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaca4`](#insn-00afaca4)

~~~json
{
  "source": "00afaca4",
  "target": "00bdb100",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaca8`](#insn-00afaca8)

~~~json
{
  "source": "00afaca8",
  "target": "00afacb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afacac`](#insn-00afacac)

~~~json
{
  "source": "00afacac",
  "target": "00afacbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afacb0`](#insn-00afacb0)

~~~json
{
  "source": "00afacb0",
  "target": "00afacc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afacb8`](#insn-00afacb8)

~~~json
{
  "source": "00afacb8",
  "target": "00afacc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afacc4`](#insn-00afacc4)

~~~json
{
  "source": "00afacc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afacc8`](#insn-00afacc8)

~~~json
{
  "source": "00afacc8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaccc`](#insn-00afaccc)

~~~json
{
  "source": "00afaccc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
