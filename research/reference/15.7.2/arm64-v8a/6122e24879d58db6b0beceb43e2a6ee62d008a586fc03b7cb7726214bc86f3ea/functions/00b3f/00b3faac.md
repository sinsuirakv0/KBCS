# 00b3faac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b3fb74`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3fb74.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0002.md#compare-2274b27a33605c4460519fd85839baa5)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b3faac",
  "name": "_ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_21__tree_const_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT_",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "19f665169335825e5616094b1f6e3e6cfcabc1bc68735318d6cac59303ea792e",
  "source_text_sha256": "19f665169335825e5616094b1f6e3e6cfcabc1bc68735318d6cac59303ea792e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b3faac",
        "00b3fbbf"
      ]
    ],
    "bytes_sha256": "ec3efceb7a7983e2eb074de10bcc2f4011f02ed8a86d2fe42daf7435068c6380",
    "instruction_count": 69,
    "instruction_bytes": 276,
    "body_bytes": 276,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdfbc0](../00bdf/00bdfbc0.md)

## 呼び出し先

- [00bdb100](../00bdb/00bdb100.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2212 bytes

~~~c

long * _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_21__tree_const_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT_
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
      if (sVar2 == 0) {
LAB_00b3faec:
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
        if (uVar5 == 0) goto LAB_00b3faec;
      }
      if ((int)uVar5 >= 0) {
        plVar9 = plVar10;
      }
      plVar10 = (long *)plVar10[(int)uVar5 < 0];
    } while (plVar10 != (long *)0x0);
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
  return plVar8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b3faac"></a> `00b3faac` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00b3fab0"></a> `00b3fab0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b3fab4"></a> `00b3fab4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b3fab8"></a> `00b3fab8` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b3fabc"></a> `00b3fabc` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b3fac0"></a> `00b3fac0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b3fac4"></a> `00b3fac4` | `77 8e 40 f8` | ldr x23,[x19, #0x8]! | `FALL_THROUGH`
<a id="insn-00b3fac8"></a> `00b3fac8` | `f7 06 00 b4` | cbz x23,0x00b3fba4 | `CONDITIONAL_JUMP`
<a id="insn-00b3facc"></a> `00b3facc` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00b3fad0"></a> `00b3fad0` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00b3fad4"></a> `00b3fad4` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00b3fad8"></a> `00b3fad8` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b3fadc"></a> `00b3fadc` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b3fae0"></a> `00b3fae0` | `76 01 89 9a` | csel x22,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00b3fae4"></a> `00b3fae4` | `55 15 81 9a` | csinc x21,x10,x1,ne | `FALL_THROUGH`
<a id="insn-00b3fae8"></a> `00b3fae8` | `0a 00 00 14` | b 0x00b3fb10 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3faec"></a> `00b3faec` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00b3faf0"></a> `00b3faf0` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00b3faf4"></a> `00b3faf4` | `1f 03 16 eb` | cmp x24,x22 | `FALL_THROUGH`
<a id="insn-00b3faf8"></a> `00b3faf8` | `00 21 9f 5a` | csinv w0,w8,wzr,cs | `FALL_THROUGH`
<a id="insn-00b3fafc"></a> `00b3fafc` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00b3fb00"></a> `00b3fb00` | `e8 a7 9f 1a` | cset w8,lt | `FALL_THROUGH`
<a id="insn-00b3fb04"></a> `00b3fb04` | `94 b2 97 9a` | csel x20,x20,x23,lt | `FALL_THROUGH`
<a id="insn-00b3fb08"></a> `00b3fb08` | `f7 5a 68 f8` | ldr x23,[x23, w8, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00b3fb0c"></a> `00b3fb0c` | `37 02 00 b4` | cbz x23,0x00b3fb50 | `CONDITIONAL_JUMP`
<a id="insn-00b3fb10"></a> `00b3fb10` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-00b3fb14"></a> `00b3fb14` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00b3fb18"></a> `00b3fb18` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b3fb1c"></a> `00b3fb1c` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b3fb20"></a> `00b3fb20` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b3fb24"></a> `00b3fb24` | `78 01 8a 9a` | csel x24,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00b3fb28"></a> `00b3fb28` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00b3fb2c"></a> `00b3fb2c` | `c2 32 98 9a` | csel x2,x22,x24,cc | `FALL_THROUGH`
<a id="insn-00b3fb30"></a> `00b3fb30` | `e2 fd ff b4` | cbz x2,0x00b3faec | `CONDITIONAL_JUMP`
<a id="insn-00b3fb34"></a> `00b3fb34` | `ea 1a 40 f9` | ldr x10,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00b3fb38"></a> `00b3fb38` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b3fb3c"></a> `00b3fb3c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b3fb40"></a> `00b3fb40` | `40 15 88 9a` | csinc x0,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00b3fb44"></a> `00b3fb44` | `6f 6d 02 94` | bl 0x00bdb100 | `UNCONDITIONAL_CALL`
<a id="insn-00b3fb48"></a> `00b3fb48` | `a0 fd ff 35` | cbnz w0,0x00b3fafc | `CONDITIONAL_JUMP`
<a id="insn-00b3fb4c"></a> `00b3fb4c` | `e8 ff ff 17` | b 0x00b3faec | `UNCONDITIONAL_JUMP`
<a id="insn-00b3fb50"></a> `00b3fb50` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00b3fb54"></a> `00b3fb54` | `80 02 00 54` | b.eq 0x00b3fba4 | `CONDITIONAL_JUMP`
<a id="insn-00b3fb58"></a> `00b3fb58` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00b3fb5c"></a> `00b3fb5c` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00b3fb60"></a> `00b3fb60` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b3fb64"></a> `00b3fb64` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b3fb68"></a> `00b3fb68` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b3fb6c"></a> `00b3fb6c` | `77 01 8a 9a` | csel x23,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00b3fb70"></a> `00b3fb70` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00b3fb74"></a> `00b3fb74` | `e2 32 96 9a` | csel x2,x23,x22,cc | `FALL_THROUGH`
<a id="insn-00b3fb78"></a> `00b3fb78` | `22 01 00 b4` | cbz x2,0x00b3fb9c | `CONDITIONAL_JUMP`
<a id="insn-00b3fb7c"></a> `00b3fb7c` | `8a 1a 40 f9` | ldr x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00b3fb80"></a> `00b3fb80` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b3fb84"></a> `00b3fb84` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b3fb88"></a> `00b3fb88` | `41 15 88 9a` | csinc x1,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00b3fb8c"></a> `00b3fb8c` | `5d 6d 02 94` | bl 0x00bdb100 | `UNCONDITIONAL_CALL`
<a id="insn-00b3fb90"></a> `00b3fb90` | `60 00 00 34` | cbz w0,0x00b3fb9c | `CONDITIONAL_JUMP`
<a id="insn-00b3fb94"></a> `00b3fb94` | `80 00 f8 37` | tbnz w0,#0x1f,0x00b3fba4 | `CONDITIONAL_JUMP`
<a id="insn-00b3fb98"></a> `00b3fb98` | `04 00 00 14` | b 0x00b3fba8 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3fb9c"></a> `00b3fb9c` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-00b3fba0"></a> `00b3fba0` | `42 00 00 54` | b.cs 0x00b3fba8 | `CONDITIONAL_JUMP`
<a id="insn-00b3fba4"></a> `00b3fba4` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00b3fba8"></a> `00b3fba8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b3fbac"></a> `00b3fbac` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b3fbb0"></a> `00b3fbb0` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b3fbb4"></a> `00b3fbb4` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b3fbb8"></a> `00b3fbb8` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00b3fbbc"></a> `00b3fbbc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b3faac`](#insn-00b3faac) 範囲 `[['00b3faac', '00b3facb']]`
  - `CONDITIONAL_JUMP` [`00b3fac8`](#insn-00b3fac8) → [`00b3fba4`](#insn-00b3fba4)
  - `FALL_THROUGH` [`00b3fac8`](#insn-00b3fac8) → [`00b3facc`](#insn-00b3facc)
- ブロック [`00b3facc`](#insn-00b3facc) 範囲 `[['00b3facc', '00b3faeb']]`
  - `UNCONDITIONAL_JUMP` [`00b3fae8`](#insn-00b3fae8) → [`00b3fb10`](#insn-00b3fb10)
- ブロック [`00b3faec`](#insn-00b3faec) 範囲 `[['00b3faec', '00b3fafb']]`
  - `FALL_THROUGH` [`00b3faf8`](#insn-00b3faf8) → [`00b3fafc`](#insn-00b3fafc)
- ブロック [`00b3fafc`](#insn-00b3fafc) 範囲 `[['00b3fafc', '00b3fb0f']]`
  - `CONDITIONAL_JUMP` [`00b3fb0c`](#insn-00b3fb0c) → [`00b3fb50`](#insn-00b3fb50)
  - `FALL_THROUGH` [`00b3fb0c`](#insn-00b3fb0c) → [`00b3fb10`](#insn-00b3fb10)
- ブロック [`00b3fb10`](#insn-00b3fb10) 範囲 `[['00b3fb10', '00b3fb33']]`
  - `CONDITIONAL_JUMP` [`00b3fb30`](#insn-00b3fb30) → [`00b3faec`](#insn-00b3faec)
  - `FALL_THROUGH` [`00b3fb30`](#insn-00b3fb30) → [`00b3fb34`](#insn-00b3fb34)
- ブロック [`00b3fb34`](#insn-00b3fb34) 範囲 `[['00b3fb34', '00b3fb4b']]`
  - `CONDITIONAL_JUMP` [`00b3fb48`](#insn-00b3fb48) → [`00b3fafc`](#insn-00b3fafc)
  - `FALL_THROUGH` [`00b3fb48`](#insn-00b3fb48) → [`00b3fb4c`](#insn-00b3fb4c)
- ブロック [`00b3fb4c`](#insn-00b3fb4c) 範囲 `[['00b3fb4c', '00b3fb4f']]`
  - `UNCONDITIONAL_JUMP` [`00b3fb4c`](#insn-00b3fb4c) → [`00b3faec`](#insn-00b3faec)
- ブロック [`00b3fb50`](#insn-00b3fb50) 範囲 `[['00b3fb50', '00b3fb57']]`
  - `CONDITIONAL_JUMP` [`00b3fb54`](#insn-00b3fb54) → [`00b3fba4`](#insn-00b3fba4)
  - `FALL_THROUGH` [`00b3fb54`](#insn-00b3fb54) → [`00b3fb58`](#insn-00b3fb58)
- ブロック [`00b3fb58`](#insn-00b3fb58) 範囲 `[['00b3fb58', '00b3fb7b']]`
  - `CONDITIONAL_JUMP` [`00b3fb78`](#insn-00b3fb78) → [`00b3fb9c`](#insn-00b3fb9c)
  - `FALL_THROUGH` [`00b3fb78`](#insn-00b3fb78) → [`00b3fb7c`](#insn-00b3fb7c)
- ブロック [`00b3fb7c`](#insn-00b3fb7c) 範囲 `[['00b3fb7c', '00b3fb93']]`
  - `CONDITIONAL_JUMP` [`00b3fb90`](#insn-00b3fb90) → [`00b3fb9c`](#insn-00b3fb9c)
  - `FALL_THROUGH` [`00b3fb90`](#insn-00b3fb90) → [`00b3fb94`](#insn-00b3fb94)
- ブロック [`00b3fb94`](#insn-00b3fb94) 範囲 `[['00b3fb94', '00b3fb97']]`
  - `CONDITIONAL_JUMP` [`00b3fb94`](#insn-00b3fb94) → [`00b3fba4`](#insn-00b3fba4)
  - `FALL_THROUGH` [`00b3fb94`](#insn-00b3fb94) → [`00b3fb98`](#insn-00b3fb98)
- ブロック [`00b3fb98`](#insn-00b3fb98) 範囲 `[['00b3fb98', '00b3fb9b']]`
  - `UNCONDITIONAL_JUMP` [`00b3fb98`](#insn-00b3fb98) → [`00b3fba8`](#insn-00b3fba8)
- ブロック [`00b3fb9c`](#insn-00b3fb9c) 範囲 `[['00b3fb9c', '00b3fba3']]`
  - `CONDITIONAL_JUMP` [`00b3fba0`](#insn-00b3fba0) → [`00b3fba8`](#insn-00b3fba8)
  - `FALL_THROUGH` [`00b3fba0`](#insn-00b3fba0) → [`00b3fba4`](#insn-00b3fba4)
- ブロック [`00b3fba4`](#insn-00b3fba4) 範囲 `[['00b3fba4', '00b3fba7']]`
  - `FALL_THROUGH` [`00b3fba4`](#insn-00b3fba4) → [`00b3fba8`](#insn-00b3fba8)
- ブロック [`00b3fba8`](#insn-00b3fba8) 範囲 `[['00b3fba8', '00b3fbbf']]`

## 命令位置別の参照

- [`00b3faac`](#insn-00b3faac) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fab0`](#insn-00b3fab0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fab4`](#insn-00b3fab4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fab8`](#insn-00b3fab8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fac8`](#insn-00b3fac8) → [`00b3fba4`](#insn-00b3fba4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fae8`](#insn-00b3fae8) → [`00b3fb10`](#insn-00b3fb10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fb0c`](#insn-00b3fb0c) → [`00b3fb50`](#insn-00b3fb50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fb30`](#insn-00b3fb30) → [`00b3faec`](#insn-00b3faec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fb44`](#insn-00b3fb44) → [`00bdb100`](../00bdb/00bdb100.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb100` · 推定シンボル `None` · 推定型 `None`
- [`00b3fb48`](#insn-00b3fb48) → [`00b3fafc`](#insn-00b3fafc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fb4c`](#insn-00b3fb4c) → [`00b3faec`](#insn-00b3faec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fb54`](#insn-00b3fb54) → [`00b3fba4`](#insn-00b3fba4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fb78`](#insn-00b3fb78) → [`00b3fb9c`](#insn-00b3fb9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fb8c`](#insn-00b3fb8c) → [`00bdb100`](../00bdb/00bdb100.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb100` · 推定シンボル `None` · 推定型 `None`
- [`00b3fb90`](#insn-00b3fb90) → [`00b3fb9c`](#insn-00b3fb9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fb94`](#insn-00b3fb94) → [`00b3fba4`](#insn-00b3fba4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fb98`](#insn-00b3fb98) → [`00b3fba8`](#insn-00b3fba8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fba0`](#insn-00b3fba0) → [`00b3fba8`](#insn-00b3fba8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fbac`](#insn-00b3fbac) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fbb0`](#insn-00b3fbb0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3fbb4`](#insn-00b3fbb4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b3faac`](#insn-00b3faac)

~~~json
{
  "source": "00b3faac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fab0`](#insn-00b3fab0)

~~~json
{
  "source": "00b3fab0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fab4`](#insn-00b3fab4)

~~~json
{
  "source": "00b3fab4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fab8`](#insn-00b3fab8)

~~~json
{
  "source": "00b3fab8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fac8`](#insn-00b3fac8)

~~~json
{
  "source": "00b3fac8",
  "target": "00b3fba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fae8`](#insn-00b3fae8)

~~~json
{
  "source": "00b3fae8",
  "target": "00b3fb10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fb0c`](#insn-00b3fb0c)

~~~json
{
  "source": "00b3fb0c",
  "target": "00b3fb50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fb30`](#insn-00b3fb30)

~~~json
{
  "source": "00b3fb30",
  "target": "00b3faec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fb44`](#insn-00b3fb44)

~~~json
{
  "source": "00b3fb44",
  "target": "00bdb100",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3fb48`](#insn-00b3fb48)

~~~json
{
  "source": "00b3fb48",
  "target": "00b3fafc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fb4c`](#insn-00b3fb4c)

~~~json
{
  "source": "00b3fb4c",
  "target": "00b3faec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fb54`](#insn-00b3fb54)

~~~json
{
  "source": "00b3fb54",
  "target": "00b3fba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fb78`](#insn-00b3fb78)

~~~json
{
  "source": "00b3fb78",
  "target": "00b3fb9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fb8c`](#insn-00b3fb8c)

~~~json
{
  "source": "00b3fb8c",
  "target": "00bdb100",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3fb90`](#insn-00b3fb90)

~~~json
{
  "source": "00b3fb90",
  "target": "00b3fb9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fb94`](#insn-00b3fb94)

~~~json
{
  "source": "00b3fb94",
  "target": "00b3fba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fb98`](#insn-00b3fb98)

~~~json
{
  "source": "00b3fb98",
  "target": "00b3fba8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fba0`](#insn-00b3fba0)

~~~json
{
  "source": "00b3fba0",
  "target": "00b3fba8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fbac`](#insn-00b3fbac)

~~~json
{
  "source": "00b3fbac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fbb0`](#insn-00b3fbb0)

~~~json
{
  "source": "00b3fbb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3fbb4`](#insn-00b3fbb4)

~~~json
{
  "source": "00b3fbb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
