# 00bafca8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bafc0c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00bafc0c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0038.md#compare-bb47807f90e9247e7b38dfbfd0cffea5)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bb0c9c`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0c9c.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-a1a7144b9c8a2c852fc565e84d25319c)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bafca8",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7RPCCallEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_15__tree_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT_",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e9c035760d1177ccc5be81ba15e86b7c4bee5810cf1121f40c9416ee579a3490",
  "source_text_sha256": "e9c035760d1177ccc5be81ba15e86b7c4bee5810cf1121f40c9416ee579a3490",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bafca8",
        "00bafdbb"
      ]
    ],
    "bytes_sha256": "d4686518107f02630ea05d41264edb942dd509cf20fd4bee38c4e0a026df681e",
    "instruction_count": 69,
    "instruction_bytes": 276,
    "body_bytes": 276,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d000](../00c5d/00c5d000.md)

## 呼び出し先

- [00c58120](../00c58/00c58120.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2204 bytes

~~~c

long * _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7RPCCallEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_15__tree_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT_
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
LAB_00bafce8:
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
        if (uVar5 == 0) goto LAB_00bafce8;
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
<a id="insn-00bafca8"></a> `00bafca8` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bafcac"></a> `00bafcac` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bafcb0"></a> `00bafcb0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bafcb4"></a> `00bafcb4` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bafcb8"></a> `00bafcb8` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bafcbc"></a> `00bafcbc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bafcc0"></a> `00bafcc0` | `77 8e 40 f8` | ldr x23,[x19, #0x8]! | `FALL_THROUGH`
<a id="insn-00bafcc4"></a> `00bafcc4` | `f7 06 00 b4` | cbz x23,0x00bafda0 | `CONDITIONAL_JUMP`
<a id="insn-00bafcc8"></a> `00bafcc8` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00bafccc"></a> `00bafccc` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bafcd0"></a> `00bafcd0` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00bafcd4"></a> `00bafcd4` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bafcd8"></a> `00bafcd8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bafcdc"></a> `00bafcdc` | `76 01 89 9a` | csel x22,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00bafce0"></a> `00bafce0` | `55 15 81 9a` | csinc x21,x10,x1,ne | `FALL_THROUGH`
<a id="insn-00bafce4"></a> `00bafce4` | `0a 00 00 14` | b 0x00bafd0c | `UNCONDITIONAL_JUMP`
<a id="insn-00bafce8"></a> `00bafce8` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00bafcec"></a> `00bafcec` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00bafcf0"></a> `00bafcf0` | `1f 03 16 eb` | cmp x24,x22 | `FALL_THROUGH`
<a id="insn-00bafcf4"></a> `00bafcf4` | `00 21 9f 5a` | csinv w0,w8,wzr,cs | `FALL_THROUGH`
<a id="insn-00bafcf8"></a> `00bafcf8` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bafcfc"></a> `00bafcfc` | `e8 a7 9f 1a` | cset w8,lt | `FALL_THROUGH`
<a id="insn-00bafd00"></a> `00bafd00` | `94 b2 97 9a` | csel x20,x20,x23,lt | `FALL_THROUGH`
<a id="insn-00bafd04"></a> `00bafd04` | `f7 5a 68 f8` | ldr x23,[x23, w8, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bafd08"></a> `00bafd08` | `37 02 00 b4` | cbz x23,0x00bafd4c | `CONDITIONAL_JUMP`
<a id="insn-00bafd0c"></a> `00bafd0c` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-00bafd10"></a> `00bafd10` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00bafd14"></a> `00bafd14` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bafd18"></a> `00bafd18` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bafd1c"></a> `00bafd1c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bafd20"></a> `00bafd20` | `78 01 8a 9a` | csel x24,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00bafd24"></a> `00bafd24` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00bafd28"></a> `00bafd28` | `c2 32 98 9a` | csel x2,x22,x24,cc | `FALL_THROUGH`
<a id="insn-00bafd2c"></a> `00bafd2c` | `e2 fd ff b4` | cbz x2,0x00bafce8 | `CONDITIONAL_JUMP`
<a id="insn-00bafd30"></a> `00bafd30` | `ea 1a 40 f9` | ldr x10,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00bafd34"></a> `00bafd34` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bafd38"></a> `00bafd38` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bafd3c"></a> `00bafd3c` | `40 15 88 9a` | csinc x0,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00bafd40"></a> `00bafd40` | `f8 a0 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00bafd44"></a> `00bafd44` | `a0 fd ff 35` | cbnz w0,0x00bafcf8 | `CONDITIONAL_JUMP`
<a id="insn-00bafd48"></a> `00bafd48` | `e8 ff ff 17` | b 0x00bafce8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafd4c"></a> `00bafd4c` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00bafd50"></a> `00bafd50` | `80 02 00 54` | b.eq 0x00bafda0 | `CONDITIONAL_JUMP`
<a id="insn-00bafd54"></a> `00bafd54` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00bafd58"></a> `00bafd58` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00bafd5c"></a> `00bafd5c` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bafd60"></a> `00bafd60` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bafd64"></a> `00bafd64` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bafd68"></a> `00bafd68` | `77 01 8a 9a` | csel x23,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00bafd6c"></a> `00bafd6c` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00bafd70"></a> `00bafd70` | `e2 32 96 9a` | csel x2,x23,x22,cc | `FALL_THROUGH`
<a id="insn-00bafd74"></a> `00bafd74` | `22 01 00 b4` | cbz x2,0x00bafd98 | `CONDITIONAL_JUMP`
<a id="insn-00bafd78"></a> `00bafd78` | `8a 1a 40 f9` | ldr x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00bafd7c"></a> `00bafd7c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bafd80"></a> `00bafd80` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bafd84"></a> `00bafd84` | `41 15 88 9a` | csinc x1,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00bafd88"></a> `00bafd88` | `e6 a0 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00bafd8c"></a> `00bafd8c` | `60 00 00 34` | cbz w0,0x00bafd98 | `CONDITIONAL_JUMP`
<a id="insn-00bafd90"></a> `00bafd90` | `80 00 f8 37` | tbnz w0,#0x1f,0x00bafda0 | `CONDITIONAL_JUMP`
<a id="insn-00bafd94"></a> `00bafd94` | `04 00 00 14` | b 0x00bafda4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafd98"></a> `00bafd98` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-00bafd9c"></a> `00bafd9c` | `42 00 00 54` | b.cs 0x00bafda4 | `CONDITIONAL_JUMP`
<a id="insn-00bafda0"></a> `00bafda0` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00bafda4"></a> `00bafda4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bafda8"></a> `00bafda8` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bafdac"></a> `00bafdac` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bafdb0"></a> `00bafdb0` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bafdb4"></a> `00bafdb4` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bafdb8"></a> `00bafdb8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bafca8`](#insn-00bafca8) 範囲 `[['00bafca8', '00bafcc7']]`
  - `CONDITIONAL_JUMP` [`00bafcc4`](#insn-00bafcc4) → [`00bafda0`](#insn-00bafda0)
  - `FALL_THROUGH` [`00bafcc4`](#insn-00bafcc4) → [`00bafcc8`](#insn-00bafcc8)
- ブロック [`00bafcc8`](#insn-00bafcc8) 範囲 `[['00bafcc8', '00bafce7']]`
  - `UNCONDITIONAL_JUMP` [`00bafce4`](#insn-00bafce4) → [`00bafd0c`](#insn-00bafd0c)
- ブロック [`00bafce8`](#insn-00bafce8) 範囲 `[['00bafce8', '00bafcf7']]`
  - `FALL_THROUGH` [`00bafcf4`](#insn-00bafcf4) → [`00bafcf8`](#insn-00bafcf8)
- ブロック [`00bafcf8`](#insn-00bafcf8) 範囲 `[['00bafcf8', '00bafd0b']]`
  - `CONDITIONAL_JUMP` [`00bafd08`](#insn-00bafd08) → [`00bafd4c`](#insn-00bafd4c)
  - `FALL_THROUGH` [`00bafd08`](#insn-00bafd08) → [`00bafd0c`](#insn-00bafd0c)
- ブロック [`00bafd0c`](#insn-00bafd0c) 範囲 `[['00bafd0c', '00bafd2f']]`
  - `CONDITIONAL_JUMP` [`00bafd2c`](#insn-00bafd2c) → [`00bafce8`](#insn-00bafce8)
  - `FALL_THROUGH` [`00bafd2c`](#insn-00bafd2c) → [`00bafd30`](#insn-00bafd30)
- ブロック [`00bafd30`](#insn-00bafd30) 範囲 `[['00bafd30', '00bafd47']]`
  - `CONDITIONAL_JUMP` [`00bafd44`](#insn-00bafd44) → [`00bafcf8`](#insn-00bafcf8)
  - `FALL_THROUGH` [`00bafd44`](#insn-00bafd44) → [`00bafd48`](#insn-00bafd48)
- ブロック [`00bafd48`](#insn-00bafd48) 範囲 `[['00bafd48', '00bafd4b']]`
  - `UNCONDITIONAL_JUMP` [`00bafd48`](#insn-00bafd48) → [`00bafce8`](#insn-00bafce8)
- ブロック [`00bafd4c`](#insn-00bafd4c) 範囲 `[['00bafd4c', '00bafd53']]`
  - `CONDITIONAL_JUMP` [`00bafd50`](#insn-00bafd50) → [`00bafda0`](#insn-00bafda0)
  - `FALL_THROUGH` [`00bafd50`](#insn-00bafd50) → [`00bafd54`](#insn-00bafd54)
- ブロック [`00bafd54`](#insn-00bafd54) 範囲 `[['00bafd54', '00bafd77']]`
  - `CONDITIONAL_JUMP` [`00bafd74`](#insn-00bafd74) → [`00bafd98`](#insn-00bafd98)
  - `FALL_THROUGH` [`00bafd74`](#insn-00bafd74) → [`00bafd78`](#insn-00bafd78)
- ブロック [`00bafd78`](#insn-00bafd78) 範囲 `[['00bafd78', '00bafd8f']]`
  - `CONDITIONAL_JUMP` [`00bafd8c`](#insn-00bafd8c) → [`00bafd98`](#insn-00bafd98)
  - `FALL_THROUGH` [`00bafd8c`](#insn-00bafd8c) → [`00bafd90`](#insn-00bafd90)
- ブロック [`00bafd90`](#insn-00bafd90) 範囲 `[['00bafd90', '00bafd93']]`
  - `CONDITIONAL_JUMP` [`00bafd90`](#insn-00bafd90) → [`00bafda0`](#insn-00bafda0)
  - `FALL_THROUGH` [`00bafd90`](#insn-00bafd90) → [`00bafd94`](#insn-00bafd94)
- ブロック [`00bafd94`](#insn-00bafd94) 範囲 `[['00bafd94', '00bafd97']]`
  - `UNCONDITIONAL_JUMP` [`00bafd94`](#insn-00bafd94) → [`00bafda4`](#insn-00bafda4)
- ブロック [`00bafd98`](#insn-00bafd98) 範囲 `[['00bafd98', '00bafd9f']]`
  - `CONDITIONAL_JUMP` [`00bafd9c`](#insn-00bafd9c) → [`00bafda4`](#insn-00bafda4)
  - `FALL_THROUGH` [`00bafd9c`](#insn-00bafd9c) → [`00bafda0`](#insn-00bafda0)
- ブロック [`00bafda0`](#insn-00bafda0) 範囲 `[['00bafda0', '00bafda3']]`
  - `FALL_THROUGH` [`00bafda0`](#insn-00bafda0) → [`00bafda4`](#insn-00bafda4)
- ブロック [`00bafda4`](#insn-00bafda4) 範囲 `[['00bafda4', '00bafdbb']]`

## 命令位置別の参照

- [`00bafca8`](#insn-00bafca8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafcac`](#insn-00bafcac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafcb0`](#insn-00bafcb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafcb4`](#insn-00bafcb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafcc4`](#insn-00bafcc4) → [`00bafda0`](#insn-00bafda0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafce4`](#insn-00bafce4) → [`00bafd0c`](#insn-00bafd0c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd08`](#insn-00bafd08) → [`00bafd4c`](#insn-00bafd4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd2c`](#insn-00bafd2c) → [`00bafce8`](#insn-00bafce8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd40`](#insn-00bafd40) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00bafd44`](#insn-00bafd44) → [`00bafcf8`](#insn-00bafcf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd48`](#insn-00bafd48) → [`00bafce8`](#insn-00bafce8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd50`](#insn-00bafd50) → [`00bafda0`](#insn-00bafda0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd74`](#insn-00bafd74) → [`00bafd98`](#insn-00bafd98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd88`](#insn-00bafd88) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00bafd8c`](#insn-00bafd8c) → [`00bafd98`](#insn-00bafd98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd90`](#insn-00bafd90) → [`00bafda0`](#insn-00bafda0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd94`](#insn-00bafd94) → [`00bafda4`](#insn-00bafda4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd9c`](#insn-00bafd9c) → [`00bafda4`](#insn-00bafda4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafda8`](#insn-00bafda8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafdac`](#insn-00bafdac) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafdb0`](#insn-00bafdb0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bafca8`](#insn-00bafca8)

~~~json
{
  "source": "00bafca8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafcac`](#insn-00bafcac)

~~~json
{
  "source": "00bafcac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafcb0`](#insn-00bafcb0)

~~~json
{
  "source": "00bafcb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafcb4`](#insn-00bafcb4)

~~~json
{
  "source": "00bafcb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafcc4`](#insn-00bafcc4)

~~~json
{
  "source": "00bafcc4",
  "target": "00bafda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafce4`](#insn-00bafce4)

~~~json
{
  "source": "00bafce4",
  "target": "00bafd0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd08`](#insn-00bafd08)

~~~json
{
  "source": "00bafd08",
  "target": "00bafd4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd2c`](#insn-00bafd2c)

~~~json
{
  "source": "00bafd2c",
  "target": "00bafce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd40`](#insn-00bafd40)

~~~json
{
  "source": "00bafd40",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafd44`](#insn-00bafd44)

~~~json
{
  "source": "00bafd44",
  "target": "00bafcf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd48`](#insn-00bafd48)

~~~json
{
  "source": "00bafd48",
  "target": "00bafce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd50`](#insn-00bafd50)

~~~json
{
  "source": "00bafd50",
  "target": "00bafda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd74`](#insn-00bafd74)

~~~json
{
  "source": "00bafd74",
  "target": "00bafd98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd88`](#insn-00bafd88)

~~~json
{
  "source": "00bafd88",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafd8c`](#insn-00bafd8c)

~~~json
{
  "source": "00bafd8c",
  "target": "00bafd98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd90`](#insn-00bafd90)

~~~json
{
  "source": "00bafd90",
  "target": "00bafda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd94`](#insn-00bafd94)

~~~json
{
  "source": "00bafd94",
  "target": "00bafda4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd9c`](#insn-00bafd9c)

~~~json
{
  "source": "00bafd9c",
  "target": "00bafda4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafda8`](#insn-00bafda8)

~~~json
{
  "source": "00bafda8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafdac`](#insn-00bafdac)

~~~json
{
  "source": "00bafdac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafdb0`](#insn-00bafdb0)

~~~json
{
  "source": "00bafdb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
