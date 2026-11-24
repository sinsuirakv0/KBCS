# 00baeae0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bae6b8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae6b8.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0038.md#compare-aacb268365590ef8ecb5f985e60e7af0)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00baeb7c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baeb7c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0010.md#compare-e2b489ddef2b29ddc1d6c9bc6900a78b)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baeae0",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers4TypeEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_15__tree_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT_",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b28e9d1a60db24a85cc50c8bf83057a1b8df613d03fbcb0f538dda0c75240835",
  "source_text_sha256": "b28e9d1a60db24a85cc50c8bf83057a1b8df613d03fbcb0f538dda0c75240835",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baeae0",
        "00baebf3"
      ]
    ],
    "bytes_sha256": "b5d84c71312769f8b251e48608f7c72f95ce5c1312f8a5b30cd5466c777ba5f7",
    "instruction_count": 69,
    "instruction_bytes": 276,
    "body_bytes": 276,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5ce90](../00c5c/00c5ce90.md)

## 呼び出し先

- [00c58050](../00c58/00c58050.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2201 bytes

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
      uVar1 = (ulong)(bVar4 >> 1);
      if ((bVar4 & 1) != 0) {
        uVar1 = plVar10[5];
      }
      sVar2 = uVar3;
      if (uVar1 <= uVar3) {
        sVar2 = uVar1;
      }
      if (sVar2 == 0) {
LAB_00baeb20:
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
        if (uVar5 == 0) goto LAB_00baeb20;
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
<a id="insn-00baeae0"></a> `00baeae0` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00baeae4"></a> `00baeae4` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baeae8"></a> `00baeae8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baeaec"></a> `00baeaec` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baeaf0"></a> `00baeaf0` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00baeaf4"></a> `00baeaf4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00baeaf8"></a> `00baeaf8` | `77 8e 40 f8` | ldr x23,[x19, #0x8]! | `FALL_THROUGH`
<a id="insn-00baeafc"></a> `00baeafc` | `f7 06 00 b4` | cbz x23,0x00baebd8 | `CONDITIONAL_JUMP`
<a id="insn-00baeb00"></a> `00baeb00` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00baeb04"></a> `00baeb04` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00baeb08"></a> `00baeb08` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00baeb0c"></a> `00baeb0c` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00baeb10"></a> `00baeb10` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baeb14"></a> `00baeb14` | `76 01 89 9a` | csel x22,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00baeb18"></a> `00baeb18` | `55 15 81 9a` | csinc x21,x10,x1,ne | `FALL_THROUGH`
<a id="insn-00baeb1c"></a> `00baeb1c` | `0a 00 00 14` | b 0x00baeb44 | `UNCONDITIONAL_JUMP`
<a id="insn-00baeb20"></a> `00baeb20` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00baeb24"></a> `00baeb24` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00baeb28"></a> `00baeb28` | `1f 03 16 eb` | cmp x24,x22 | `FALL_THROUGH`
<a id="insn-00baeb2c"></a> `00baeb2c` | `00 21 9f 5a` | csinv w0,w8,wzr,cs | `FALL_THROUGH`
<a id="insn-00baeb30"></a> `00baeb30` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00baeb34"></a> `00baeb34` | `e8 a7 9f 1a` | cset w8,lt | `FALL_THROUGH`
<a id="insn-00baeb38"></a> `00baeb38` | `94 b2 97 9a` | csel x20,x20,x23,lt | `FALL_THROUGH`
<a id="insn-00baeb3c"></a> `00baeb3c` | `f7 5a 68 f8` | ldr x23,[x23, w8, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00baeb40"></a> `00baeb40` | `37 02 00 b4` | cbz x23,0x00baeb84 | `CONDITIONAL_JUMP`
<a id="insn-00baeb44"></a> `00baeb44` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-00baeb48"></a> `00baeb48` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00baeb4c"></a> `00baeb4c` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00baeb50"></a> `00baeb50` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00baeb54"></a> `00baeb54` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baeb58"></a> `00baeb58` | `78 01 8a 9a` | csel x24,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00baeb5c"></a> `00baeb5c` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00baeb60"></a> `00baeb60` | `c2 32 98 9a` | csel x2,x22,x24,cc | `FALL_THROUGH`
<a id="insn-00baeb64"></a> `00baeb64` | `e2 fd ff b4` | cbz x2,0x00baeb20 | `CONDITIONAL_JUMP`
<a id="insn-00baeb68"></a> `00baeb68` | `ea 1a 40 f9` | ldr x10,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00baeb6c"></a> `00baeb6c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baeb70"></a> `00baeb70` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00baeb74"></a> `00baeb74` | `40 15 88 9a` | csinc x0,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00baeb78"></a> `00baeb78` | `36 a5 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00baeb7c"></a> `00baeb7c` | `a0 fd ff 35` | cbnz w0,0x00baeb30 | `CONDITIONAL_JUMP`
<a id="insn-00baeb80"></a> `00baeb80` | `e8 ff ff 17` | b 0x00baeb20 | `UNCONDITIONAL_JUMP`
<a id="insn-00baeb84"></a> `00baeb84` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00baeb88"></a> `00baeb88` | `80 02 00 54` | b.eq 0x00baebd8 | `CONDITIONAL_JUMP`
<a id="insn-00baeb8c"></a> `00baeb8c` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00baeb90"></a> `00baeb90` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00baeb94"></a> `00baeb94` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00baeb98"></a> `00baeb98` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00baeb9c"></a> `00baeb9c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baeba0"></a> `00baeba0` | `77 01 8a 9a` | csel x23,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00baeba4"></a> `00baeba4` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00baeba8"></a> `00baeba8` | `e2 32 96 9a` | csel x2,x23,x22,cc | `FALL_THROUGH`
<a id="insn-00baebac"></a> `00baebac` | `22 01 00 b4` | cbz x2,0x00baebd0 | `CONDITIONAL_JUMP`
<a id="insn-00baebb0"></a> `00baebb0` | `8a 1a 40 f9` | ldr x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00baebb4"></a> `00baebb4` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baebb8"></a> `00baebb8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00baebbc"></a> `00baebbc` | `41 15 88 9a` | csinc x1,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00baebc0"></a> `00baebc0` | `24 a5 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00baebc4"></a> `00baebc4` | `60 00 00 34` | cbz w0,0x00baebd0 | `CONDITIONAL_JUMP`
<a id="insn-00baebc8"></a> `00baebc8` | `80 00 f8 37` | tbnz w0,#0x1f,0x00baebd8 | `CONDITIONAL_JUMP`
<a id="insn-00baebcc"></a> `00baebcc` | `04 00 00 14` | b 0x00baebdc | `UNCONDITIONAL_JUMP`
<a id="insn-00baebd0"></a> `00baebd0` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-00baebd4"></a> `00baebd4` | `42 00 00 54` | b.cs 0x00baebdc | `CONDITIONAL_JUMP`
<a id="insn-00baebd8"></a> `00baebd8` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00baebdc"></a> `00baebdc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00baebe0"></a> `00baebe0` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baebe4"></a> `00baebe4` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baebe8"></a> `00baebe8` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baebec"></a> `00baebec` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00baebf0"></a> `00baebf0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baeae0`](#insn-00baeae0) 範囲 `[['00baeae0', '00baeaff']]`
  - `CONDITIONAL_JUMP` [`00baeafc`](#insn-00baeafc) → [`00baebd8`](#insn-00baebd8)
  - `FALL_THROUGH` [`00baeafc`](#insn-00baeafc) → [`00baeb00`](#insn-00baeb00)
- ブロック [`00baeb00`](#insn-00baeb00) 範囲 `[['00baeb00', '00baeb1f']]`
  - `UNCONDITIONAL_JUMP` [`00baeb1c`](#insn-00baeb1c) → [`00baeb44`](#insn-00baeb44)
- ブロック [`00baeb20`](#insn-00baeb20) 範囲 `[['00baeb20', '00baeb2f']]`
  - `FALL_THROUGH` [`00baeb2c`](#insn-00baeb2c) → [`00baeb30`](#insn-00baeb30)
- ブロック [`00baeb30`](#insn-00baeb30) 範囲 `[['00baeb30', '00baeb43']]`
  - `CONDITIONAL_JUMP` [`00baeb40`](#insn-00baeb40) → [`00baeb84`](#insn-00baeb84)
  - `FALL_THROUGH` [`00baeb40`](#insn-00baeb40) → [`00baeb44`](#insn-00baeb44)
- ブロック [`00baeb44`](#insn-00baeb44) 範囲 `[['00baeb44', '00baeb67']]`
  - `CONDITIONAL_JUMP` [`00baeb64`](#insn-00baeb64) → [`00baeb20`](#insn-00baeb20)
  - `FALL_THROUGH` [`00baeb64`](#insn-00baeb64) → [`00baeb68`](#insn-00baeb68)
- ブロック [`00baeb68`](#insn-00baeb68) 範囲 `[['00baeb68', '00baeb7f']]`
  - `CONDITIONAL_JUMP` [`00baeb7c`](#insn-00baeb7c) → [`00baeb30`](#insn-00baeb30)
  - `FALL_THROUGH` [`00baeb7c`](#insn-00baeb7c) → [`00baeb80`](#insn-00baeb80)
- ブロック [`00baeb80`](#insn-00baeb80) 範囲 `[['00baeb80', '00baeb83']]`
  - `UNCONDITIONAL_JUMP` [`00baeb80`](#insn-00baeb80) → [`00baeb20`](#insn-00baeb20)
- ブロック [`00baeb84`](#insn-00baeb84) 範囲 `[['00baeb84', '00baeb8b']]`
  - `CONDITIONAL_JUMP` [`00baeb88`](#insn-00baeb88) → [`00baebd8`](#insn-00baebd8)
  - `FALL_THROUGH` [`00baeb88`](#insn-00baeb88) → [`00baeb8c`](#insn-00baeb8c)
- ブロック [`00baeb8c`](#insn-00baeb8c) 範囲 `[['00baeb8c', '00baebaf']]`
  - `CONDITIONAL_JUMP` [`00baebac`](#insn-00baebac) → [`00baebd0`](#insn-00baebd0)
  - `FALL_THROUGH` [`00baebac`](#insn-00baebac) → [`00baebb0`](#insn-00baebb0)
- ブロック [`00baebb0`](#insn-00baebb0) 範囲 `[['00baebb0', '00baebc7']]`
  - `CONDITIONAL_JUMP` [`00baebc4`](#insn-00baebc4) → [`00baebd0`](#insn-00baebd0)
  - `FALL_THROUGH` [`00baebc4`](#insn-00baebc4) → [`00baebc8`](#insn-00baebc8)
- ブロック [`00baebc8`](#insn-00baebc8) 範囲 `[['00baebc8', '00baebcb']]`
  - `CONDITIONAL_JUMP` [`00baebc8`](#insn-00baebc8) → [`00baebd8`](#insn-00baebd8)
  - `FALL_THROUGH` [`00baebc8`](#insn-00baebc8) → [`00baebcc`](#insn-00baebcc)
- ブロック [`00baebcc`](#insn-00baebcc) 範囲 `[['00baebcc', '00baebcf']]`
  - `UNCONDITIONAL_JUMP` [`00baebcc`](#insn-00baebcc) → [`00baebdc`](#insn-00baebdc)
- ブロック [`00baebd0`](#insn-00baebd0) 範囲 `[['00baebd0', '00baebd7']]`
  - `CONDITIONAL_JUMP` [`00baebd4`](#insn-00baebd4) → [`00baebdc`](#insn-00baebdc)
  - `FALL_THROUGH` [`00baebd4`](#insn-00baebd4) → [`00baebd8`](#insn-00baebd8)
- ブロック [`00baebd8`](#insn-00baebd8) 範囲 `[['00baebd8', '00baebdb']]`
  - `FALL_THROUGH` [`00baebd8`](#insn-00baebd8) → [`00baebdc`](#insn-00baebdc)
- ブロック [`00baebdc`](#insn-00baebdc) 範囲 `[['00baebdc', '00baebf3']]`

## 命令位置別の参照

- [`00baeae0`](#insn-00baeae0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeae4`](#insn-00baeae4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeae8`](#insn-00baeae8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeaec`](#insn-00baeaec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeafc`](#insn-00baeafc) → [`00baebd8`](#insn-00baebd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeb1c`](#insn-00baeb1c) → [`00baeb44`](#insn-00baeb44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeb40`](#insn-00baeb40) → [`00baeb84`](#insn-00baeb84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeb64`](#insn-00baeb64) → [`00baeb20`](#insn-00baeb20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeb78`](#insn-00baeb78) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00baeb7c`](#insn-00baeb7c) → [`00baeb30`](#insn-00baeb30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeb80`](#insn-00baeb80) → [`00baeb20`](#insn-00baeb20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeb88`](#insn-00baeb88) → [`00baebd8`](#insn-00baebd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baebac`](#insn-00baebac) → [`00baebd0`](#insn-00baebd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baebc0`](#insn-00baebc0) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00baebc4`](#insn-00baebc4) → [`00baebd0`](#insn-00baebd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baebc8`](#insn-00baebc8) → [`00baebd8`](#insn-00baebd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baebcc`](#insn-00baebcc) → [`00baebdc`](#insn-00baebdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baebd4`](#insn-00baebd4) → [`00baebdc`](#insn-00baebdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baebe0`](#insn-00baebe0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baebe4`](#insn-00baebe4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baebe8`](#insn-00baebe8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baeae0`](#insn-00baeae0)

~~~json
{
  "source": "00baeae0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeae4`](#insn-00baeae4)

~~~json
{
  "source": "00baeae4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeae8`](#insn-00baeae8)

~~~json
{
  "source": "00baeae8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeaec`](#insn-00baeaec)

~~~json
{
  "source": "00baeaec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeafc`](#insn-00baeafc)

~~~json
{
  "source": "00baeafc",
  "target": "00baebd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeb1c`](#insn-00baeb1c)

~~~json
{
  "source": "00baeb1c",
  "target": "00baeb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeb40`](#insn-00baeb40)

~~~json
{
  "source": "00baeb40",
  "target": "00baeb84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeb64`](#insn-00baeb64)

~~~json
{
  "source": "00baeb64",
  "target": "00baeb20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeb78`](#insn-00baeb78)

~~~json
{
  "source": "00baeb78",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baeb7c`](#insn-00baeb7c)

~~~json
{
  "source": "00baeb7c",
  "target": "00baeb30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeb80`](#insn-00baeb80)

~~~json
{
  "source": "00baeb80",
  "target": "00baeb20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeb88`](#insn-00baeb88)

~~~json
{
  "source": "00baeb88",
  "target": "00baebd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baebac`](#insn-00baebac)

~~~json
{
  "source": "00baebac",
  "target": "00baebd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baebc0`](#insn-00baebc0)

~~~json
{
  "source": "00baebc0",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baebc4`](#insn-00baebc4)

~~~json
{
  "source": "00baebc4",
  "target": "00baebd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baebc8`](#insn-00baebc8)

~~~json
{
  "source": "00baebc8",
  "target": "00baebd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baebcc`](#insn-00baebcc)

~~~json
{
  "source": "00baebcc",
  "target": "00baebdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baebd4`](#insn-00baebd4)

~~~json
{
  "source": "00baebd4",
  "target": "00baebdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baebe0`](#insn-00baebe0)

~~~json
{
  "source": "00baebe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baebe4`](#insn-00baebe4)

~~~json
{
  "source": "00baebe4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baebe8`](#insn-00baebe8)

~~~json
{
  "source": "00baebe8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
