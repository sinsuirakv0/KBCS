# 00baeb7c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00baeae0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00baeae0.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0010.md#compare-e2b489ddef2b29ddc1d6c9bc6900a78b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bafb70`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00bafb70.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-d92e6b7c2ac7289194ec5f93c9518f8f)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baeb7c",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers4TypeEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_15__tree_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT_",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a3af7cd452cc510a4c85092a95fd5c9af9f157cd5d194678da374bf97865b12d",
  "source_text_sha256": "a3af7cd452cc510a4c85092a95fd5c9af9f157cd5d194678da374bf97865b12d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baeb7c",
        "00baec8f"
      ]
    ],
    "bytes_sha256": "c5f1cd043f5fbee8046d14c376c1394c4945f1aa62f4249a02f62712cd1a9ab3",
    "instruction_count": 69,
    "instruction_bytes": 276,
    "body_bytes": 276,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5cf60](../00c5c/00c5cf60.md)

## 呼び出し先

- [00c58120](../00c58/00c58120.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2298 bytes

~~~c

long * _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers4TypeEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_15__tree_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT_
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
                    /* try { // try from 00baebf0 to 00caf7cb has its CatchHandler @ 00bafa78 */
      uVar1 = (ulong)(bVar4 >> 1);
      if ((bVar4 & 1) != 0) {
        uVar1 = plVar10[5];
      }
      sVar2 = uVar3;
      if (uVar1 <= uVar3) {
        sVar2 = uVar1;
      }
      if (sVar2 == 0) {
LAB_00baebbc:
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
        if (uVar5 == 0) goto LAB_00baebbc;
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
<a id="insn-00baeb7c"></a> `00baeb7c` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00baeb80"></a> `00baeb80` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baeb84"></a> `00baeb84` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baeb88"></a> `00baeb88` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baeb8c"></a> `00baeb8c` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00baeb90"></a> `00baeb90` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00baeb94"></a> `00baeb94` | `77 8e 40 f8` | ldr x23,[x19, #0x8]! | `FALL_THROUGH`
<a id="insn-00baeb98"></a> `00baeb98` | `f7 06 00 b4` | cbz x23,0x00baec74 | `CONDITIONAL_JUMP`
<a id="insn-00baeb9c"></a> `00baeb9c` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00baeba0"></a> `00baeba0` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00baeba4"></a> `00baeba4` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00baeba8"></a> `00baeba8` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00baebac"></a> `00baebac` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baebb0"></a> `00baebb0` | `76 01 89 9a` | csel x22,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00baebb4"></a> `00baebb4` | `55 15 81 9a` | csinc x21,x10,x1,ne | `FALL_THROUGH`
<a id="insn-00baebb8"></a> `00baebb8` | `0a 00 00 14` | b 0x00baebe0 | `UNCONDITIONAL_JUMP`
<a id="insn-00baebbc"></a> `00baebbc` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00baebc0"></a> `00baebc0` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00baebc4"></a> `00baebc4` | `1f 03 16 eb` | cmp x24,x22 | `FALL_THROUGH`
<a id="insn-00baebc8"></a> `00baebc8` | `00 21 9f 5a` | csinv w0,w8,wzr,cs | `FALL_THROUGH`
<a id="insn-00baebcc"></a> `00baebcc` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00baebd0"></a> `00baebd0` | `e8 a7 9f 1a` | cset w8,lt | `FALL_THROUGH`
<a id="insn-00baebd4"></a> `00baebd4` | `94 b2 97 9a` | csel x20,x20,x23,lt | `FALL_THROUGH`
<a id="insn-00baebd8"></a> `00baebd8` | `f7 5a 68 f8` | ldr x23,[x23, w8, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00baebdc"></a> `00baebdc` | `37 02 00 b4` | cbz x23,0x00baec20 | `CONDITIONAL_JUMP`
<a id="insn-00baebe0"></a> `00baebe0` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-00baebe4"></a> `00baebe4` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00baebe8"></a> `00baebe8` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00baebec"></a> `00baebec` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00baebf0"></a> `00baebf0` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baebf4"></a> `00baebf4` | `78 01 8a 9a` | csel x24,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00baebf8"></a> `00baebf8` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00baebfc"></a> `00baebfc` | `c2 32 98 9a` | csel x2,x22,x24,cc | `FALL_THROUGH`
<a id="insn-00baec00"></a> `00baec00` | `e2 fd ff b4` | cbz x2,0x00baebbc | `CONDITIONAL_JUMP`
<a id="insn-00baec04"></a> `00baec04` | `ea 1a 40 f9` | ldr x10,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00baec08"></a> `00baec08` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baec0c"></a> `00baec0c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00baec10"></a> `00baec10` | `40 15 88 9a` | csinc x0,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00baec14"></a> `00baec14` | `43 a5 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00baec18"></a> `00baec18` | `a0 fd ff 35` | cbnz w0,0x00baebcc | `CONDITIONAL_JUMP`
<a id="insn-00baec1c"></a> `00baec1c` | `e8 ff ff 17` | b 0x00baebbc | `UNCONDITIONAL_JUMP`
<a id="insn-00baec20"></a> `00baec20` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00baec24"></a> `00baec24` | `80 02 00 54` | b.eq 0x00baec74 | `CONDITIONAL_JUMP`
<a id="insn-00baec28"></a> `00baec28` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00baec2c"></a> `00baec2c` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00baec30"></a> `00baec30` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00baec34"></a> `00baec34` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00baec38"></a> `00baec38` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baec3c"></a> `00baec3c` | `77 01 8a 9a` | csel x23,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00baec40"></a> `00baec40` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00baec44"></a> `00baec44` | `e2 32 96 9a` | csel x2,x23,x22,cc | `FALL_THROUGH`
<a id="insn-00baec48"></a> `00baec48` | `22 01 00 b4` | cbz x2,0x00baec6c | `CONDITIONAL_JUMP`
<a id="insn-00baec4c"></a> `00baec4c` | `8a 1a 40 f9` | ldr x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00baec50"></a> `00baec50` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baec54"></a> `00baec54` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00baec58"></a> `00baec58` | `41 15 88 9a` | csinc x1,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00baec5c"></a> `00baec5c` | `31 a5 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00baec60"></a> `00baec60` | `60 00 00 34` | cbz w0,0x00baec6c | `CONDITIONAL_JUMP`
<a id="insn-00baec64"></a> `00baec64` | `80 00 f8 37` | tbnz w0,#0x1f,0x00baec74 | `CONDITIONAL_JUMP`
<a id="insn-00baec68"></a> `00baec68` | `04 00 00 14` | b 0x00baec78 | `UNCONDITIONAL_JUMP`
<a id="insn-00baec6c"></a> `00baec6c` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-00baec70"></a> `00baec70` | `42 00 00 54` | b.cs 0x00baec78 | `CONDITIONAL_JUMP`
<a id="insn-00baec74"></a> `00baec74` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00baec78"></a> `00baec78` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00baec7c"></a> `00baec7c` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baec80"></a> `00baec80` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baec84"></a> `00baec84` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baec88"></a> `00baec88` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00baec8c"></a> `00baec8c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baeb7c`](#insn-00baeb7c) 範囲 `[['00baeb7c', '00baeb9b']]`
  - `CONDITIONAL_JUMP` [`00baeb98`](#insn-00baeb98) → [`00baec74`](#insn-00baec74)
  - `FALL_THROUGH` [`00baeb98`](#insn-00baeb98) → [`00baeb9c`](#insn-00baeb9c)
- ブロック [`00baeb9c`](#insn-00baeb9c) 範囲 `[['00baeb9c', '00baebbb']]`
  - `UNCONDITIONAL_JUMP` [`00baebb8`](#insn-00baebb8) → [`00baebe0`](#insn-00baebe0)
- ブロック [`00baebbc`](#insn-00baebbc) 範囲 `[['00baebbc', '00baebcb']]`
  - `FALL_THROUGH` [`00baebc8`](#insn-00baebc8) → [`00baebcc`](#insn-00baebcc)
- ブロック [`00baebcc`](#insn-00baebcc) 範囲 `[['00baebcc', '00baebdf']]`
  - `CONDITIONAL_JUMP` [`00baebdc`](#insn-00baebdc) → [`00baec20`](#insn-00baec20)
  - `FALL_THROUGH` [`00baebdc`](#insn-00baebdc) → [`00baebe0`](#insn-00baebe0)
- ブロック [`00baebe0`](#insn-00baebe0) 範囲 `[['00baebe0', '00baebef']]`
  - `FALL_THROUGH` [`00baebec`](#insn-00baebec) → [`00baebf0`](#insn-00baebf0)
- ブロック [`00baebf0`](#insn-00baebf0) 範囲 `[['00baebf0', '00baec03']]`
  - `CONDITIONAL_JUMP` [`00baec00`](#insn-00baec00) → [`00baebbc`](#insn-00baebbc)
  - `FALL_THROUGH` [`00baec00`](#insn-00baec00) → [`00baec04`](#insn-00baec04)
- ブロック [`00baec04`](#insn-00baec04) 範囲 `[['00baec04', '00baec1b']]`
  - `CONDITIONAL_JUMP` [`00baec18`](#insn-00baec18) → [`00baebcc`](#insn-00baebcc)
  - `FALL_THROUGH` [`00baec18`](#insn-00baec18) → [`00baec1c`](#insn-00baec1c)
- ブロック [`00baec1c`](#insn-00baec1c) 範囲 `[['00baec1c', '00baec1f']]`
  - `UNCONDITIONAL_JUMP` [`00baec1c`](#insn-00baec1c) → [`00baebbc`](#insn-00baebbc)
- ブロック [`00baec20`](#insn-00baec20) 範囲 `[['00baec20', '00baec27']]`
  - `CONDITIONAL_JUMP` [`00baec24`](#insn-00baec24) → [`00baec74`](#insn-00baec74)
  - `FALL_THROUGH` [`00baec24`](#insn-00baec24) → [`00baec28`](#insn-00baec28)
- ブロック [`00baec28`](#insn-00baec28) 範囲 `[['00baec28', '00baec4b']]`
  - `CONDITIONAL_JUMP` [`00baec48`](#insn-00baec48) → [`00baec6c`](#insn-00baec6c)
  - `FALL_THROUGH` [`00baec48`](#insn-00baec48) → [`00baec4c`](#insn-00baec4c)
- ブロック [`00baec4c`](#insn-00baec4c) 範囲 `[['00baec4c', '00baec63']]`
  - `CONDITIONAL_JUMP` [`00baec60`](#insn-00baec60) → [`00baec6c`](#insn-00baec6c)
  - `FALL_THROUGH` [`00baec60`](#insn-00baec60) → [`00baec64`](#insn-00baec64)
- ブロック [`00baec64`](#insn-00baec64) 範囲 `[['00baec64', '00baec67']]`
  - `CONDITIONAL_JUMP` [`00baec64`](#insn-00baec64) → [`00baec74`](#insn-00baec74)
  - `FALL_THROUGH` [`00baec64`](#insn-00baec64) → [`00baec68`](#insn-00baec68)
- ブロック [`00baec68`](#insn-00baec68) 範囲 `[['00baec68', '00baec6b']]`
  - `UNCONDITIONAL_JUMP` [`00baec68`](#insn-00baec68) → [`00baec78`](#insn-00baec78)
- ブロック [`00baec6c`](#insn-00baec6c) 範囲 `[['00baec6c', '00baec73']]`
  - `CONDITIONAL_JUMP` [`00baec70`](#insn-00baec70) → [`00baec78`](#insn-00baec78)
  - `FALL_THROUGH` [`00baec70`](#insn-00baec70) → [`00baec74`](#insn-00baec74)
- ブロック [`00baec74`](#insn-00baec74) 範囲 `[['00baec74', '00baec77']]`
  - `FALL_THROUGH` [`00baec74`](#insn-00baec74) → [`00baec78`](#insn-00baec78)
- ブロック [`00baec78`](#insn-00baec78) 範囲 `[['00baec78', '00baec8f']]`

## 命令位置別の参照

- [`00baeb7c`](#insn-00baeb7c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeb80`](#insn-00baeb80) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeb84`](#insn-00baeb84) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeb88`](#insn-00baeb88) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeb98`](#insn-00baeb98) → [`00baec74`](#insn-00baec74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baebb8`](#insn-00baebb8) → [`00baebe0`](#insn-00baebe0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baebdc`](#insn-00baebdc) → [`00baec20`](#insn-00baec20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec00`](#insn-00baec00) → [`00baebbc`](#insn-00baebbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec14`](#insn-00baec14) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00baec18`](#insn-00baec18) → [`00baebcc`](#insn-00baebcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec1c`](#insn-00baec1c) → [`00baebbc`](#insn-00baebbc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec24`](#insn-00baec24) → [`00baec74`](#insn-00baec74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec48`](#insn-00baec48) → [`00baec6c`](#insn-00baec6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec5c`](#insn-00baec5c) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00baec60`](#insn-00baec60) → [`00baec6c`](#insn-00baec6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec64`](#insn-00baec64) → [`00baec74`](#insn-00baec74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec68`](#insn-00baec68) → [`00baec78`](#insn-00baec78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec70`](#insn-00baec70) → [`00baec78`](#insn-00baec78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec7c`](#insn-00baec7c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec80`](#insn-00baec80) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec84`](#insn-00baec84) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baeb7c`](#insn-00baeb7c)

~~~json
{
  "source": "00baeb7c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeb80`](#insn-00baeb80)

~~~json
{
  "source": "00baeb80",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeb84`](#insn-00baeb84)

~~~json
{
  "source": "00baeb84",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeb88`](#insn-00baeb88)

~~~json
{
  "source": "00baeb88",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeb98`](#insn-00baeb98)

~~~json
{
  "source": "00baeb98",
  "target": "00baec74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baebb8`](#insn-00baebb8)

~~~json
{
  "source": "00baebb8",
  "target": "00baebe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baebdc`](#insn-00baebdc)

~~~json
{
  "source": "00baebdc",
  "target": "00baec20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec00`](#insn-00baec00)

~~~json
{
  "source": "00baec00",
  "target": "00baebbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec14`](#insn-00baec14)

~~~json
{
  "source": "00baec14",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baec18`](#insn-00baec18)

~~~json
{
  "source": "00baec18",
  "target": "00baebcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec1c`](#insn-00baec1c)

~~~json
{
  "source": "00baec1c",
  "target": "00baebbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec24`](#insn-00baec24)

~~~json
{
  "source": "00baec24",
  "target": "00baec74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec48`](#insn-00baec48)

~~~json
{
  "source": "00baec48",
  "target": "00baec6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec5c`](#insn-00baec5c)

~~~json
{
  "source": "00baec5c",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baec60`](#insn-00baec60)

~~~json
{
  "source": "00baec60",
  "target": "00baec6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec64`](#insn-00baec64)

~~~json
{
  "source": "00baec64",
  "target": "00baec74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec68`](#insn-00baec68)

~~~json
{
  "source": "00baec68",
  "target": "00baec78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec70`](#insn-00baec70)

~~~json
{
  "source": "00baec70",
  "target": "00baec78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec7c`](#insn-00baec7c)

~~~json
{
  "source": "00baec7c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec80`](#insn-00baec80)

~~~json
{
  "source": "00baec80",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec84`](#insn-00baec84)

~~~json
{
  "source": "00baec84",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
