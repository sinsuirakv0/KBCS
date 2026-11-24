# 00baedb0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00baed14`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00baed14.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0038.md#compare-fe69244121f6817490c4463b1a6fd39d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bafda4`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00bafda4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-b16a36579a70997bfb9f13fe7181d885)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baedb0",
  "name": "_ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3setIN11flatbuffers12IncludedFileENS_4lessISA_EENS5_ISA_EEEEEENS_19__map_value_compareIS7_SF_NSB_IS7_EELb1EEENS5_ISF_EEE4findIS7_EENS_21__tree_const_iteratorISF_PNS_11__tree_nodeISF_PvEElEERKT_",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "caa9a3568f6a307a9e6f1df30dd81c4ef6879809cf229f12f146409dfaf22f9c",
  "source_text_sha256": "caa9a3568f6a307a9e6f1df30dd81c4ef6879809cf229f12f146409dfaf22f9c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baedb0",
        "00baeec3"
      ]
    ],
    "bytes_sha256": "2219f86de02493b2b592871a4b218698399c866c861be61873325242e44e6600",
    "instruction_count": 69,
    "instruction_bytes": 276,
    "body_bytes": 276,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5cb30](../00c5c/00c5cb30.md)

## 呼び出し先

- [00c58120](../00c58/00c58120.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2246 bytes

~~~c

long * _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3setIN11flatbuffers12IncludedFileENS_4lessISA_EENS5_ISA_EEEEEENS_19__map_value_compareIS7_SF_NSB_IS7_EELb1EEENS5_ISF_EEE4findIS7_EENS_21__tree_const_iteratorISF_PNS_11__tree_nodeISF_PvEElEERKT_
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
LAB_00baedf0:
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
        if (uVar5 == 0) goto LAB_00baedf0;
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
<a id="insn-00baedb0"></a> `00baedb0` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00baedb4"></a> `00baedb4` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baedb8"></a> `00baedb8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baedbc"></a> `00baedbc` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baedc0"></a> `00baedc0` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00baedc4"></a> `00baedc4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00baedc8"></a> `00baedc8` | `77 8e 40 f8` | ldr x23,[x19, #0x8]! | `FALL_THROUGH`
<a id="insn-00baedcc"></a> `00baedcc` | `f7 06 00 b4` | cbz x23,0x00baeea8 | `CONDITIONAL_JUMP`
<a id="insn-00baedd0"></a> `00baedd0` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00baedd4"></a> `00baedd4` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00baedd8"></a> `00baedd8` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00baeddc"></a> `00baeddc` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00baede0"></a> `00baede0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baede4"></a> `00baede4` | `76 01 89 9a` | csel x22,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00baede8"></a> `00baede8` | `55 15 81 9a` | csinc x21,x10,x1,ne | `FALL_THROUGH`
<a id="insn-00baedec"></a> `00baedec` | `0a 00 00 14` | b 0x00baee14 | `UNCONDITIONAL_JUMP`
<a id="insn-00baedf0"></a> `00baedf0` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00baedf4"></a> `00baedf4` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00baedf8"></a> `00baedf8` | `1f 03 16 eb` | cmp x24,x22 | `FALL_THROUGH`
<a id="insn-00baedfc"></a> `00baedfc` | `00 21 9f 5a` | csinv w0,w8,wzr,cs | `FALL_THROUGH`
<a id="insn-00baee00"></a> `00baee00` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00baee04"></a> `00baee04` | `e8 a7 9f 1a` | cset w8,lt | `FALL_THROUGH`
<a id="insn-00baee08"></a> `00baee08` | `94 b2 97 9a` | csel x20,x20,x23,lt | `FALL_THROUGH`
<a id="insn-00baee0c"></a> `00baee0c` | `f7 5a 68 f8` | ldr x23,[x23, w8, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00baee10"></a> `00baee10` | `37 02 00 b4` | cbz x23,0x00baee54 | `CONDITIONAL_JUMP`
<a id="insn-00baee14"></a> `00baee14` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-00baee18"></a> `00baee18` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00baee1c"></a> `00baee1c` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00baee20"></a> `00baee20` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00baee24"></a> `00baee24` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baee28"></a> `00baee28` | `78 01 8a 9a` | csel x24,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00baee2c"></a> `00baee2c` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00baee30"></a> `00baee30` | `c2 32 98 9a` | csel x2,x22,x24,cc | `FALL_THROUGH`
<a id="insn-00baee34"></a> `00baee34` | `e2 fd ff b4` | cbz x2,0x00baedf0 | `CONDITIONAL_JUMP`
<a id="insn-00baee38"></a> `00baee38` | `ea 1a 40 f9` | ldr x10,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00baee3c"></a> `00baee3c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baee40"></a> `00baee40` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00baee44"></a> `00baee44` | `40 15 88 9a` | csinc x0,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00baee48"></a> `00baee48` | `b6 a4 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00baee4c"></a> `00baee4c` | `a0 fd ff 35` | cbnz w0,0x00baee00 | `CONDITIONAL_JUMP`
<a id="insn-00baee50"></a> `00baee50` | `e8 ff ff 17` | b 0x00baedf0 | `UNCONDITIONAL_JUMP`
<a id="insn-00baee54"></a> `00baee54` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00baee58"></a> `00baee58` | `80 02 00 54` | b.eq 0x00baeea8 | `CONDITIONAL_JUMP`
<a id="insn-00baee5c"></a> `00baee5c` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00baee60"></a> `00baee60` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00baee64"></a> `00baee64` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00baee68"></a> `00baee68` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00baee6c"></a> `00baee6c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baee70"></a> `00baee70` | `77 01 8a 9a` | csel x23,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00baee74"></a> `00baee74` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00baee78"></a> `00baee78` | `e2 32 96 9a` | csel x2,x23,x22,cc | `FALL_THROUGH`
<a id="insn-00baee7c"></a> `00baee7c` | `22 01 00 b4` | cbz x2,0x00baeea0 | `CONDITIONAL_JUMP`
<a id="insn-00baee80"></a> `00baee80` | `8a 1a 40 f9` | ldr x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00baee84"></a> `00baee84` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baee88"></a> `00baee88` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00baee8c"></a> `00baee8c` | `41 15 88 9a` | csinc x1,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00baee90"></a> `00baee90` | `a4 a4 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00baee94"></a> `00baee94` | `60 00 00 34` | cbz w0,0x00baeea0 | `CONDITIONAL_JUMP`
<a id="insn-00baee98"></a> `00baee98` | `80 00 f8 37` | tbnz w0,#0x1f,0x00baeea8 | `CONDITIONAL_JUMP`
<a id="insn-00baee9c"></a> `00baee9c` | `04 00 00 14` | b 0x00baeeac | `UNCONDITIONAL_JUMP`
<a id="insn-00baeea0"></a> `00baeea0` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-00baeea4"></a> `00baeea4` | `42 00 00 54` | b.cs 0x00baeeac | `CONDITIONAL_JUMP`
<a id="insn-00baeea8"></a> `00baeea8` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00baeeac"></a> `00baeeac` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00baeeb0"></a> `00baeeb0` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baeeb4"></a> `00baeeb4` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baeeb8"></a> `00baeeb8` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baeebc"></a> `00baeebc` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00baeec0"></a> `00baeec0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baedb0`](#insn-00baedb0) 範囲 `[['00baedb0', '00baedcf']]`
  - `CONDITIONAL_JUMP` [`00baedcc`](#insn-00baedcc) → [`00baeea8`](#insn-00baeea8)
  - `FALL_THROUGH` [`00baedcc`](#insn-00baedcc) → [`00baedd0`](#insn-00baedd0)
- ブロック [`00baedd0`](#insn-00baedd0) 範囲 `[['00baedd0', '00baedef']]`
  - `UNCONDITIONAL_JUMP` [`00baedec`](#insn-00baedec) → [`00baee14`](#insn-00baee14)
- ブロック [`00baedf0`](#insn-00baedf0) 範囲 `[['00baedf0', '00baedff']]`
  - `FALL_THROUGH` [`00baedfc`](#insn-00baedfc) → [`00baee00`](#insn-00baee00)
- ブロック [`00baee00`](#insn-00baee00) 範囲 `[['00baee00', '00baee13']]`
  - `CONDITIONAL_JUMP` [`00baee10`](#insn-00baee10) → [`00baee54`](#insn-00baee54)
  - `FALL_THROUGH` [`00baee10`](#insn-00baee10) → [`00baee14`](#insn-00baee14)
- ブロック [`00baee14`](#insn-00baee14) 範囲 `[['00baee14', '00baee37']]`
  - `CONDITIONAL_JUMP` [`00baee34`](#insn-00baee34) → [`00baedf0`](#insn-00baedf0)
  - `FALL_THROUGH` [`00baee34`](#insn-00baee34) → [`00baee38`](#insn-00baee38)
- ブロック [`00baee38`](#insn-00baee38) 範囲 `[['00baee38', '00baee4f']]`
  - `CONDITIONAL_JUMP` [`00baee4c`](#insn-00baee4c) → [`00baee00`](#insn-00baee00)
  - `FALL_THROUGH` [`00baee4c`](#insn-00baee4c) → [`00baee50`](#insn-00baee50)
- ブロック [`00baee50`](#insn-00baee50) 範囲 `[['00baee50', '00baee53']]`
  - `UNCONDITIONAL_JUMP` [`00baee50`](#insn-00baee50) → [`00baedf0`](#insn-00baedf0)
- ブロック [`00baee54`](#insn-00baee54) 範囲 `[['00baee54', '00baee5b']]`
  - `CONDITIONAL_JUMP` [`00baee58`](#insn-00baee58) → [`00baeea8`](#insn-00baeea8)
  - `FALL_THROUGH` [`00baee58`](#insn-00baee58) → [`00baee5c`](#insn-00baee5c)
- ブロック [`00baee5c`](#insn-00baee5c) 範囲 `[['00baee5c', '00baee7f']]`
  - `CONDITIONAL_JUMP` [`00baee7c`](#insn-00baee7c) → [`00baeea0`](#insn-00baeea0)
  - `FALL_THROUGH` [`00baee7c`](#insn-00baee7c) → [`00baee80`](#insn-00baee80)
- ブロック [`00baee80`](#insn-00baee80) 範囲 `[['00baee80', '00baee97']]`
  - `CONDITIONAL_JUMP` [`00baee94`](#insn-00baee94) → [`00baeea0`](#insn-00baeea0)
  - `FALL_THROUGH` [`00baee94`](#insn-00baee94) → [`00baee98`](#insn-00baee98)
- ブロック [`00baee98`](#insn-00baee98) 範囲 `[['00baee98', '00baee9b']]`
  - `CONDITIONAL_JUMP` [`00baee98`](#insn-00baee98) → [`00baeea8`](#insn-00baeea8)
  - `FALL_THROUGH` [`00baee98`](#insn-00baee98) → [`00baee9c`](#insn-00baee9c)
- ブロック [`00baee9c`](#insn-00baee9c) 範囲 `[['00baee9c', '00baee9f']]`
  - `UNCONDITIONAL_JUMP` [`00baee9c`](#insn-00baee9c) → [`00baeeac`](#insn-00baeeac)
- ブロック [`00baeea0`](#insn-00baeea0) 範囲 `[['00baeea0', '00baeea7']]`
  - `CONDITIONAL_JUMP` [`00baeea4`](#insn-00baeea4) → [`00baeeac`](#insn-00baeeac)
  - `FALL_THROUGH` [`00baeea4`](#insn-00baeea4) → [`00baeea8`](#insn-00baeea8)
- ブロック [`00baeea8`](#insn-00baeea8) 範囲 `[['00baeea8', '00baeeab']]`
  - `FALL_THROUGH` [`00baeea8`](#insn-00baeea8) → [`00baeeac`](#insn-00baeeac)
- ブロック [`00baeeac`](#insn-00baeeac) 範囲 `[['00baeeac', '00baeec3']]`

## 命令位置別の参照

- [`00baedb0`](#insn-00baedb0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baedb4`](#insn-00baedb4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baedb8`](#insn-00baedb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baedbc`](#insn-00baedbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baedcc`](#insn-00baedcc) → [`00baeea8`](#insn-00baeea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baedec`](#insn-00baedec) → [`00baee14`](#insn-00baee14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baee10`](#insn-00baee10) → [`00baee54`](#insn-00baee54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baee34`](#insn-00baee34) → [`00baedf0`](#insn-00baedf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baee48`](#insn-00baee48) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00baee4c`](#insn-00baee4c) → [`00baee00`](#insn-00baee00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baee50`](#insn-00baee50) → [`00baedf0`](#insn-00baedf0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baee58`](#insn-00baee58) → [`00baeea8`](#insn-00baeea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baee7c`](#insn-00baee7c) → [`00baeea0`](#insn-00baeea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baee90`](#insn-00baee90) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00baee94`](#insn-00baee94) → [`00baeea0`](#insn-00baeea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baee98`](#insn-00baee98) → [`00baeea8`](#insn-00baeea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baee9c`](#insn-00baee9c) → [`00baeeac`](#insn-00baeeac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeea4`](#insn-00baeea4) → [`00baeeac`](#insn-00baeeac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeeb0`](#insn-00baeeb0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeeb4`](#insn-00baeeb4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeeb8`](#insn-00baeeb8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baedb0`](#insn-00baedb0)

~~~json
{
  "source": "00baedb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baedb4`](#insn-00baedb4)

~~~json
{
  "source": "00baedb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baedb8`](#insn-00baedb8)

~~~json
{
  "source": "00baedb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baedbc`](#insn-00baedbc)

~~~json
{
  "source": "00baedbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baedcc`](#insn-00baedcc)

~~~json
{
  "source": "00baedcc",
  "target": "00baeea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baedec`](#insn-00baedec)

~~~json
{
  "source": "00baedec",
  "target": "00baee14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baee10`](#insn-00baee10)

~~~json
{
  "source": "00baee10",
  "target": "00baee54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baee34`](#insn-00baee34)

~~~json
{
  "source": "00baee34",
  "target": "00baedf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baee48`](#insn-00baee48)

~~~json
{
  "source": "00baee48",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baee4c`](#insn-00baee4c)

~~~json
{
  "source": "00baee4c",
  "target": "00baee00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baee50`](#insn-00baee50)

~~~json
{
  "source": "00baee50",
  "target": "00baedf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baee58`](#insn-00baee58)

~~~json
{
  "source": "00baee58",
  "target": "00baeea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baee7c`](#insn-00baee7c)

~~~json
{
  "source": "00baee7c",
  "target": "00baeea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baee90`](#insn-00baee90)

~~~json
{
  "source": "00baee90",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baee94`](#insn-00baee94)

~~~json
{
  "source": "00baee94",
  "target": "00baeea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baee98`](#insn-00baee98)

~~~json
{
  "source": "00baee98",
  "target": "00baeea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baee9c`](#insn-00baee9c)

~~~json
{
  "source": "00baee9c",
  "target": "00baeeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeea4`](#insn-00baeea4)

~~~json
{
  "source": "00baeea4",
  "target": "00baeeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeeb0`](#insn-00baeeb0)

~~~json
{
  "source": "00baeeb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeeb4`](#insn-00baeeb4)

~~~json
{
  "source": "00baeeb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeeb8`](#insn-00baeeb8)

~~~json
{
  "source": "00baeeb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
