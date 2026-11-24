# 00bafedc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bafe40`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00bafe40.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0010.md#compare-e43469f1427955805bbcc7344c45945a)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bb0ed0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0ed0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-db76076d808c3df7e29742e748c7eb2a)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bafedc",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_15__tree_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT_",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "67b65a8543145704fb3746838679e3b416a81ceec192a0d13ec6090eff8aa367",
  "source_text_sha256": "67b65a8543145704fb3746838679e3b416a81ceec192a0d13ec6090eff8aa367",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bafedc",
        "00baffef"
      ]
    ],
    "bytes_sha256": "39654c05bec9450575844210d6cb6c02b79752a0871c511f996dd5bf974e7bb6",
    "instruction_count": 69,
    "instruction_bytes": 276,
    "body_bytes": 276,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5cfc0](../00c5c/00c5cfc0.md)

## 呼び出し先

- [00c58120](../00c58/00c58120.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2301 bytes

~~~c

long * _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_15__tree_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT_
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
LAB_00baff1c:
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
        if (uVar5 == 0) goto LAB_00baff1c;
      }
      if ((int)uVar5 >= 0) {
        plVar9 = plVar10;
      }
      plVar10 = (long *)plVar10[(int)uVar5 < 0];
    } while (plVar10 != (long *)0x0);
                    /* try { // try from 00baff80 to 00caff87 has its CatchHandler @ 00bb007c */
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
<a id="insn-00bafedc"></a> `00bafedc` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bafee0"></a> `00bafee0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bafee4"></a> `00bafee4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bafee8"></a> `00bafee8` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bafeec"></a> `00bafeec` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bafef0"></a> `00bafef0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bafef4"></a> `00bafef4` | `77 8e 40 f8` | ldr x23,[x19, #0x8]! | `FALL_THROUGH`
<a id="insn-00bafef8"></a> `00bafef8` | `f7 06 00 b4` | cbz x23,0x00baffd4 | `CONDITIONAL_JUMP`
<a id="insn-00bafefc"></a> `00bafefc` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00baff00"></a> `00baff00` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00baff04"></a> `00baff04` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00baff08"></a> `00baff08` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00baff0c"></a> `00baff0c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baff10"></a> `00baff10` | `76 01 89 9a` | csel x22,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00baff14"></a> `00baff14` | `55 15 81 9a` | csinc x21,x10,x1,ne | `FALL_THROUGH`
<a id="insn-00baff18"></a> `00baff18` | `0a 00 00 14` | b 0x00baff40 | `UNCONDITIONAL_JUMP`
<a id="insn-00baff1c"></a> `00baff1c` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00baff20"></a> `00baff20` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00baff24"></a> `00baff24` | `1f 03 16 eb` | cmp x24,x22 | `FALL_THROUGH`
<a id="insn-00baff28"></a> `00baff28` | `00 21 9f 5a` | csinv w0,w8,wzr,cs | `FALL_THROUGH`
<a id="insn-00baff2c"></a> `00baff2c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00baff30"></a> `00baff30` | `e8 a7 9f 1a` | cset w8,lt | `FALL_THROUGH`
<a id="insn-00baff34"></a> `00baff34` | `94 b2 97 9a` | csel x20,x20,x23,lt | `FALL_THROUGH`
<a id="insn-00baff38"></a> `00baff38` | `f7 5a 68 f8` | ldr x23,[x23, w8, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00baff3c"></a> `00baff3c` | `37 02 00 b4` | cbz x23,0x00baff80 | `CONDITIONAL_JUMP`
<a id="insn-00baff40"></a> `00baff40` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-00baff44"></a> `00baff44` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00baff48"></a> `00baff48` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00baff4c"></a> `00baff4c` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00baff50"></a> `00baff50` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baff54"></a> `00baff54` | `78 01 8a 9a` | csel x24,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00baff58"></a> `00baff58` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00baff5c"></a> `00baff5c` | `c2 32 98 9a` | csel x2,x22,x24,cc | `FALL_THROUGH`
<a id="insn-00baff60"></a> `00baff60` | `e2 fd ff b4` | cbz x2,0x00baff1c | `CONDITIONAL_JUMP`
<a id="insn-00baff64"></a> `00baff64` | `ea 1a 40 f9` | ldr x10,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00baff68"></a> `00baff68` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baff6c"></a> `00baff6c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00baff70"></a> `00baff70` | `40 15 88 9a` | csinc x0,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00baff74"></a> `00baff74` | `6b a0 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00baff78"></a> `00baff78` | `a0 fd ff 35` | cbnz w0,0x00baff2c | `CONDITIONAL_JUMP`
<a id="insn-00baff7c"></a> `00baff7c` | `e8 ff ff 17` | b 0x00baff1c | `UNCONDITIONAL_JUMP`
<a id="insn-00baff80"></a> `00baff80` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00baff84"></a> `00baff84` | `80 02 00 54` | b.eq 0x00baffd4 | `CONDITIONAL_JUMP`
<a id="insn-00baff88"></a> `00baff88` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00baff8c"></a> `00baff8c` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00baff90"></a> `00baff90` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00baff94"></a> `00baff94` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00baff98"></a> `00baff98` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baff9c"></a> `00baff9c` | `77 01 8a 9a` | csel x23,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00baffa0"></a> `00baffa0` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00baffa4"></a> `00baffa4` | `e2 32 96 9a` | csel x2,x23,x22,cc | `FALL_THROUGH`
<a id="insn-00baffa8"></a> `00baffa8` | `22 01 00 b4` | cbz x2,0x00baffcc | `CONDITIONAL_JUMP`
<a id="insn-00baffac"></a> `00baffac` | `8a 1a 40 f9` | ldr x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00baffb0"></a> `00baffb0` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baffb4"></a> `00baffb4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00baffb8"></a> `00baffb8` | `41 15 88 9a` | csinc x1,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00baffbc"></a> `00baffbc` | `59 a0 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00baffc0"></a> `00baffc0` | `60 00 00 34` | cbz w0,0x00baffcc | `CONDITIONAL_JUMP`
<a id="insn-00baffc4"></a> `00baffc4` | `80 00 f8 37` | tbnz w0,#0x1f,0x00baffd4 | `CONDITIONAL_JUMP`
<a id="insn-00baffc8"></a> `00baffc8` | `04 00 00 14` | b 0x00baffd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00baffcc"></a> `00baffcc` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-00baffd0"></a> `00baffd0` | `42 00 00 54` | b.cs 0x00baffd8 | `CONDITIONAL_JUMP`
<a id="insn-00baffd4"></a> `00baffd4` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00baffd8"></a> `00baffd8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00baffdc"></a> `00baffdc` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baffe0"></a> `00baffe0` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baffe4"></a> `00baffe4` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baffe8"></a> `00baffe8` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00baffec"></a> `00baffec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bafedc`](#insn-00bafedc) 範囲 `[['00bafedc', '00bafefb']]`
  - `CONDITIONAL_JUMP` [`00bafef8`](#insn-00bafef8) → [`00baffd4`](#insn-00baffd4)
  - `FALL_THROUGH` [`00bafef8`](#insn-00bafef8) → [`00bafefc`](#insn-00bafefc)
- ブロック [`00bafefc`](#insn-00bafefc) 範囲 `[['00bafefc', '00baff1b']]`
  - `UNCONDITIONAL_JUMP` [`00baff18`](#insn-00baff18) → [`00baff40`](#insn-00baff40)
- ブロック [`00baff1c`](#insn-00baff1c) 範囲 `[['00baff1c', '00baff2b']]`
  - `FALL_THROUGH` [`00baff28`](#insn-00baff28) → [`00baff2c`](#insn-00baff2c)
- ブロック [`00baff2c`](#insn-00baff2c) 範囲 `[['00baff2c', '00baff3f']]`
  - `CONDITIONAL_JUMP` [`00baff3c`](#insn-00baff3c) → [`00baff80`](#insn-00baff80)
  - `FALL_THROUGH` [`00baff3c`](#insn-00baff3c) → [`00baff40`](#insn-00baff40)
- ブロック [`00baff40`](#insn-00baff40) 範囲 `[['00baff40', '00baff63']]`
  - `CONDITIONAL_JUMP` [`00baff60`](#insn-00baff60) → [`00baff1c`](#insn-00baff1c)
  - `FALL_THROUGH` [`00baff60`](#insn-00baff60) → [`00baff64`](#insn-00baff64)
- ブロック [`00baff64`](#insn-00baff64) 範囲 `[['00baff64', '00baff7b']]`
  - `CONDITIONAL_JUMP` [`00baff78`](#insn-00baff78) → [`00baff2c`](#insn-00baff2c)
  - `FALL_THROUGH` [`00baff78`](#insn-00baff78) → [`00baff7c`](#insn-00baff7c)
- ブロック [`00baff7c`](#insn-00baff7c) 範囲 `[['00baff7c', '00baff7f']]`
  - `UNCONDITIONAL_JUMP` [`00baff7c`](#insn-00baff7c) → [`00baff1c`](#insn-00baff1c)
- ブロック [`00baff80`](#insn-00baff80) 範囲 `[['00baff80', '00baff87']]`
  - `CONDITIONAL_JUMP` [`00baff84`](#insn-00baff84) → [`00baffd4`](#insn-00baffd4)
  - `FALL_THROUGH` [`00baff84`](#insn-00baff84) → [`00baff88`](#insn-00baff88)
- ブロック [`00baff88`](#insn-00baff88) 範囲 `[['00baff88', '00baffab']]`
  - `CONDITIONAL_JUMP` [`00baffa8`](#insn-00baffa8) → [`00baffcc`](#insn-00baffcc)
  - `FALL_THROUGH` [`00baffa8`](#insn-00baffa8) → [`00baffac`](#insn-00baffac)
- ブロック [`00baffac`](#insn-00baffac) 範囲 `[['00baffac', '00baffc3']]`
  - `CONDITIONAL_JUMP` [`00baffc0`](#insn-00baffc0) → [`00baffcc`](#insn-00baffcc)
  - `FALL_THROUGH` [`00baffc0`](#insn-00baffc0) → [`00baffc4`](#insn-00baffc4)
- ブロック [`00baffc4`](#insn-00baffc4) 範囲 `[['00baffc4', '00baffc7']]`
  - `CONDITIONAL_JUMP` [`00baffc4`](#insn-00baffc4) → [`00baffd4`](#insn-00baffd4)
  - `FALL_THROUGH` [`00baffc4`](#insn-00baffc4) → [`00baffc8`](#insn-00baffc8)
- ブロック [`00baffc8`](#insn-00baffc8) 範囲 `[['00baffc8', '00baffcb']]`
  - `UNCONDITIONAL_JUMP` [`00baffc8`](#insn-00baffc8) → [`00baffd8`](#insn-00baffd8)
- ブロック [`00baffcc`](#insn-00baffcc) 範囲 `[['00baffcc', '00baffd3']]`
  - `CONDITIONAL_JUMP` [`00baffd0`](#insn-00baffd0) → [`00baffd8`](#insn-00baffd8)
  - `FALL_THROUGH` [`00baffd0`](#insn-00baffd0) → [`00baffd4`](#insn-00baffd4)
- ブロック [`00baffd4`](#insn-00baffd4) 範囲 `[['00baffd4', '00baffd7']]`
  - `FALL_THROUGH` [`00baffd4`](#insn-00baffd4) → [`00baffd8`](#insn-00baffd8)
- ブロック [`00baffd8`](#insn-00baffd8) 範囲 `[['00baffd8', '00baffef']]`

## 命令位置別の参照

- [`00bafedc`](#insn-00bafedc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafee0`](#insn-00bafee0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafee4`](#insn-00bafee4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafee8`](#insn-00bafee8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafef8`](#insn-00bafef8) → [`00baffd4`](#insn-00baffd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baff18`](#insn-00baff18) → [`00baff40`](#insn-00baff40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baff3c`](#insn-00baff3c) → [`00baff80`](#insn-00baff80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baff60`](#insn-00baff60) → [`00baff1c`](#insn-00baff1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baff74`](#insn-00baff74) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00baff78`](#insn-00baff78) → [`00baff2c`](#insn-00baff2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baff7c`](#insn-00baff7c) → [`00baff1c`](#insn-00baff1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baff84`](#insn-00baff84) → [`00baffd4`](#insn-00baffd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffa8`](#insn-00baffa8) → [`00baffcc`](#insn-00baffcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffbc`](#insn-00baffbc) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00baffc0`](#insn-00baffc0) → [`00baffcc`](#insn-00baffcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffc4`](#insn-00baffc4) → [`00baffd4`](#insn-00baffd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffc8`](#insn-00baffc8) → [`00baffd8`](#insn-00baffd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffd0`](#insn-00baffd0) → [`00baffd8`](#insn-00baffd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffdc`](#insn-00baffdc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffe0`](#insn-00baffe0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffe4`](#insn-00baffe4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bafedc`](#insn-00bafedc)

~~~json
{
  "source": "00bafedc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafee0`](#insn-00bafee0)

~~~json
{
  "source": "00bafee0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafee4`](#insn-00bafee4)

~~~json
{
  "source": "00bafee4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafee8`](#insn-00bafee8)

~~~json
{
  "source": "00bafee8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafef8`](#insn-00bafef8)

~~~json
{
  "source": "00bafef8",
  "target": "00baffd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baff18`](#insn-00baff18)

~~~json
{
  "source": "00baff18",
  "target": "00baff40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baff3c`](#insn-00baff3c)

~~~json
{
  "source": "00baff3c",
  "target": "00baff80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baff60`](#insn-00baff60)

~~~json
{
  "source": "00baff60",
  "target": "00baff1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baff74`](#insn-00baff74)

~~~json
{
  "source": "00baff74",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baff78`](#insn-00baff78)

~~~json
{
  "source": "00baff78",
  "target": "00baff2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baff7c`](#insn-00baff7c)

~~~json
{
  "source": "00baff7c",
  "target": "00baff1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baff84`](#insn-00baff84)

~~~json
{
  "source": "00baff84",
  "target": "00baffd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baffa8`](#insn-00baffa8)

~~~json
{
  "source": "00baffa8",
  "target": "00baffcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baffbc`](#insn-00baffbc)

~~~json
{
  "source": "00baffbc",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baffc0`](#insn-00baffc0)

~~~json
{
  "source": "00baffc0",
  "target": "00baffcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baffc4`](#insn-00baffc4)

~~~json
{
  "source": "00baffc4",
  "target": "00baffd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baffc8`](#insn-00baffc8)

~~~json
{
  "source": "00baffc8",
  "target": "00baffd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baffd0`](#insn-00baffd0)

~~~json
{
  "source": "00baffd0",
  "target": "00baffd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baffdc`](#insn-00baffdc)

~~~json
{
  "source": "00baffdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baffe0`](#insn-00baffe0)

~~~json
{
  "source": "00baffe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baffe4`](#insn-00baffe4)

~~~json
{
  "source": "00baffe4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
