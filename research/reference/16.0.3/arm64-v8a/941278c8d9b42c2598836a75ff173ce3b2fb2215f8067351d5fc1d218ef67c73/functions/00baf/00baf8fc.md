# 00baf8fc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bae908`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae908.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-90f7d8abc49f8ce231375fa30d75d0ab)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baf8fc",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_15__tree_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT_",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "33bdd80085e64cddc43e95d31bedd1281e0b3a1507111828cc6fd1fe310d573a",
  "source_text_sha256": "33bdd80085e64cddc43e95d31bedd1281e0b3a1507111828cc6fd1fe310d573a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baf8fc",
        "00bafa0f"
      ]
    ],
    "bytes_sha256": "6b69846013837d8688427e90ad36c1cd89beb76f17e9cdff6affd15995109c30",
    "instruction_count": 69,
    "instruction_bytes": 276,
    "body_bytes": 276,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5dfb0](../00c5d/00c5dfb0.md)

## 呼び出し先

- [00c590f0](../00c59/00c590f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2204 bytes

~~~c

long * _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_15__tree_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT_
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
LAB_00baf93c:
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
        if (uVar5 == 0) goto LAB_00baf93c;
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
<a id="insn-00baf8fc"></a> `00baf8fc` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00baf900"></a> `00baf900` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baf904"></a> `00baf904` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baf908"></a> `00baf908` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baf90c"></a> `00baf90c` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00baf910"></a> `00baf910` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00baf914"></a> `00baf914` | `77 8e 40 f8` | ldr x23,[x19, #0x8]! | `FALL_THROUGH`
<a id="insn-00baf918"></a> `00baf918` | `f7 06 00 b4` | cbz x23,0x00baf9f4 | `CONDITIONAL_JUMP`
<a id="insn-00baf91c"></a> `00baf91c` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00baf920"></a> `00baf920` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00baf924"></a> `00baf924` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00baf928"></a> `00baf928` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00baf92c"></a> `00baf92c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baf930"></a> `00baf930` | `76 01 89 9a` | csel x22,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00baf934"></a> `00baf934` | `55 15 81 9a` | csinc x21,x10,x1,ne | `FALL_THROUGH`
<a id="insn-00baf938"></a> `00baf938` | `0a 00 00 14` | b 0x00baf960 | `UNCONDITIONAL_JUMP`
<a id="insn-00baf93c"></a> `00baf93c` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00baf940"></a> `00baf940` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00baf944"></a> `00baf944` | `1f 03 16 eb` | cmp x24,x22 | `FALL_THROUGH`
<a id="insn-00baf948"></a> `00baf948` | `00 21 9f 5a` | csinv w0,w8,wzr,cs | `FALL_THROUGH`
<a id="insn-00baf94c"></a> `00baf94c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00baf950"></a> `00baf950` | `e8 a7 9f 1a` | cset w8,lt | `FALL_THROUGH`
<a id="insn-00baf954"></a> `00baf954` | `94 b2 97 9a` | csel x20,x20,x23,lt | `FALL_THROUGH`
<a id="insn-00baf958"></a> `00baf958` | `f7 5a 68 f8` | ldr x23,[x23, w8, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00baf95c"></a> `00baf95c` | `37 02 00 b4` | cbz x23,0x00baf9a0 | `CONDITIONAL_JUMP`
<a id="insn-00baf960"></a> `00baf960` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-00baf964"></a> `00baf964` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00baf968"></a> `00baf968` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00baf96c"></a> `00baf96c` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00baf970"></a> `00baf970` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baf974"></a> `00baf974` | `78 01 8a 9a` | csel x24,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00baf978"></a> `00baf978` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00baf97c"></a> `00baf97c` | `c2 32 98 9a` | csel x2,x22,x24,cc | `FALL_THROUGH`
<a id="insn-00baf980"></a> `00baf980` | `e2 fd ff b4` | cbz x2,0x00baf93c | `CONDITIONAL_JUMP`
<a id="insn-00baf984"></a> `00baf984` | `ea 1a 40 f9` | ldr x10,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00baf988"></a> `00baf988` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baf98c"></a> `00baf98c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00baf990"></a> `00baf990` | `40 15 88 9a` | csinc x0,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00baf994"></a> `00baf994` | `d7 a5 02 94` | bl 0x00c590f0 | `UNCONDITIONAL_CALL`
<a id="insn-00baf998"></a> `00baf998` | `a0 fd ff 35` | cbnz w0,0x00baf94c | `CONDITIONAL_JUMP`
<a id="insn-00baf99c"></a> `00baf99c` | `e8 ff ff 17` | b 0x00baf93c | `UNCONDITIONAL_JUMP`
<a id="insn-00baf9a0"></a> `00baf9a0` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00baf9a4"></a> `00baf9a4` | `80 02 00 54` | b.eq 0x00baf9f4 | `CONDITIONAL_JUMP`
<a id="insn-00baf9a8"></a> `00baf9a8` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00baf9ac"></a> `00baf9ac` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00baf9b0"></a> `00baf9b0` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00baf9b4"></a> `00baf9b4` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00baf9b8"></a> `00baf9b8` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baf9bc"></a> `00baf9bc` | `77 01 8a 9a` | csel x23,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00baf9c0"></a> `00baf9c0` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00baf9c4"></a> `00baf9c4` | `e2 32 96 9a` | csel x2,x23,x22,cc | `FALL_THROUGH`
<a id="insn-00baf9c8"></a> `00baf9c8` | `22 01 00 b4` | cbz x2,0x00baf9ec | `CONDITIONAL_JUMP`
<a id="insn-00baf9cc"></a> `00baf9cc` | `8a 1a 40 f9` | ldr x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00baf9d0"></a> `00baf9d0` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baf9d4"></a> `00baf9d4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00baf9d8"></a> `00baf9d8` | `41 15 88 9a` | csinc x1,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00baf9dc"></a> `00baf9dc` | `c5 a5 02 94` | bl 0x00c590f0 | `UNCONDITIONAL_CALL`
<a id="insn-00baf9e0"></a> `00baf9e0` | `60 00 00 34` | cbz w0,0x00baf9ec | `CONDITIONAL_JUMP`
<a id="insn-00baf9e4"></a> `00baf9e4` | `80 00 f8 37` | tbnz w0,#0x1f,0x00baf9f4 | `CONDITIONAL_JUMP`
<a id="insn-00baf9e8"></a> `00baf9e8` | `04 00 00 14` | b 0x00baf9f8 | `UNCONDITIONAL_JUMP`
<a id="insn-00baf9ec"></a> `00baf9ec` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-00baf9f0"></a> `00baf9f0` | `42 00 00 54` | b.cs 0x00baf9f8 | `CONDITIONAL_JUMP`
<a id="insn-00baf9f4"></a> `00baf9f4` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00baf9f8"></a> `00baf9f8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00baf9fc"></a> `00baf9fc` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bafa00"></a> `00bafa00` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bafa04"></a> `00bafa04` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bafa08"></a> `00bafa08` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bafa0c"></a> `00bafa0c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baf8fc`](#insn-00baf8fc) 範囲 `[['00baf8fc', '00baf91b']]`
  - `CONDITIONAL_JUMP` [`00baf918`](#insn-00baf918) → [`00baf9f4`](#insn-00baf9f4)
  - `FALL_THROUGH` [`00baf918`](#insn-00baf918) → [`00baf91c`](#insn-00baf91c)
- ブロック [`00baf91c`](#insn-00baf91c) 範囲 `[['00baf91c', '00baf93b']]`
  - `UNCONDITIONAL_JUMP` [`00baf938`](#insn-00baf938) → [`00baf960`](#insn-00baf960)
- ブロック [`00baf93c`](#insn-00baf93c) 範囲 `[['00baf93c', '00baf94b']]`
  - `FALL_THROUGH` [`00baf948`](#insn-00baf948) → [`00baf94c`](#insn-00baf94c)
- ブロック [`00baf94c`](#insn-00baf94c) 範囲 `[['00baf94c', '00baf95f']]`
  - `CONDITIONAL_JUMP` [`00baf95c`](#insn-00baf95c) → [`00baf9a0`](#insn-00baf9a0)
  - `FALL_THROUGH` [`00baf95c`](#insn-00baf95c) → [`00baf960`](#insn-00baf960)
- ブロック [`00baf960`](#insn-00baf960) 範囲 `[['00baf960', '00baf983']]`
  - `CONDITIONAL_JUMP` [`00baf980`](#insn-00baf980) → [`00baf93c`](#insn-00baf93c)
  - `FALL_THROUGH` [`00baf980`](#insn-00baf980) → [`00baf984`](#insn-00baf984)
- ブロック [`00baf984`](#insn-00baf984) 範囲 `[['00baf984', '00baf99b']]`
  - `CONDITIONAL_JUMP` [`00baf998`](#insn-00baf998) → [`00baf94c`](#insn-00baf94c)
  - `FALL_THROUGH` [`00baf998`](#insn-00baf998) → [`00baf99c`](#insn-00baf99c)
- ブロック [`00baf99c`](#insn-00baf99c) 範囲 `[['00baf99c', '00baf99f']]`
  - `UNCONDITIONAL_JUMP` [`00baf99c`](#insn-00baf99c) → [`00baf93c`](#insn-00baf93c)
- ブロック [`00baf9a0`](#insn-00baf9a0) 範囲 `[['00baf9a0', '00baf9a7']]`
  - `CONDITIONAL_JUMP` [`00baf9a4`](#insn-00baf9a4) → [`00baf9f4`](#insn-00baf9f4)
  - `FALL_THROUGH` [`00baf9a4`](#insn-00baf9a4) → [`00baf9a8`](#insn-00baf9a8)
- ブロック [`00baf9a8`](#insn-00baf9a8) 範囲 `[['00baf9a8', '00baf9cb']]`
  - `CONDITIONAL_JUMP` [`00baf9c8`](#insn-00baf9c8) → [`00baf9ec`](#insn-00baf9ec)
  - `FALL_THROUGH` [`00baf9c8`](#insn-00baf9c8) → [`00baf9cc`](#insn-00baf9cc)
- ブロック [`00baf9cc`](#insn-00baf9cc) 範囲 `[['00baf9cc', '00baf9e3']]`
  - `CONDITIONAL_JUMP` [`00baf9e0`](#insn-00baf9e0) → [`00baf9ec`](#insn-00baf9ec)
  - `FALL_THROUGH` [`00baf9e0`](#insn-00baf9e0) → [`00baf9e4`](#insn-00baf9e4)
- ブロック [`00baf9e4`](#insn-00baf9e4) 範囲 `[['00baf9e4', '00baf9e7']]`
  - `CONDITIONAL_JUMP` [`00baf9e4`](#insn-00baf9e4) → [`00baf9f4`](#insn-00baf9f4)
  - `FALL_THROUGH` [`00baf9e4`](#insn-00baf9e4) → [`00baf9e8`](#insn-00baf9e8)
- ブロック [`00baf9e8`](#insn-00baf9e8) 範囲 `[['00baf9e8', '00baf9eb']]`
  - `UNCONDITIONAL_JUMP` [`00baf9e8`](#insn-00baf9e8) → [`00baf9f8`](#insn-00baf9f8)
- ブロック [`00baf9ec`](#insn-00baf9ec) 範囲 `[['00baf9ec', '00baf9f3']]`
  - `CONDITIONAL_JUMP` [`00baf9f0`](#insn-00baf9f0) → [`00baf9f8`](#insn-00baf9f8)
  - `FALL_THROUGH` [`00baf9f0`](#insn-00baf9f0) → [`00baf9f4`](#insn-00baf9f4)
- ブロック [`00baf9f4`](#insn-00baf9f4) 範囲 `[['00baf9f4', '00baf9f7']]`
  - `FALL_THROUGH` [`00baf9f4`](#insn-00baf9f4) → [`00baf9f8`](#insn-00baf9f8)
- ブロック [`00baf9f8`](#insn-00baf9f8) 範囲 `[['00baf9f8', '00bafa0f']]`

## 命令位置別の参照

- [`00baf8fc`](#insn-00baf8fc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf900`](#insn-00baf900) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf904`](#insn-00baf904) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf908`](#insn-00baf908) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf918`](#insn-00baf918) → [`00baf9f4`](#insn-00baf9f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf938`](#insn-00baf938) → [`00baf960`](#insn-00baf960) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf95c`](#insn-00baf95c) → [`00baf9a0`](#insn-00baf9a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf980`](#insn-00baf980) → [`00baf93c`](#insn-00baf93c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf994`](#insn-00baf994) → [`00c590f0`](../00c59/00c590f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590f0` · 推定シンボル `None` · 推定型 `None`
- [`00baf998`](#insn-00baf998) → [`00baf94c`](#insn-00baf94c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf99c`](#insn-00baf99c) → [`00baf93c`](#insn-00baf93c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf9a4`](#insn-00baf9a4) → [`00baf9f4`](#insn-00baf9f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf9c8`](#insn-00baf9c8) → [`00baf9ec`](#insn-00baf9ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf9dc`](#insn-00baf9dc) → [`00c590f0`](../00c59/00c590f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590f0` · 推定シンボル `None` · 推定型 `None`
- [`00baf9e0`](#insn-00baf9e0) → [`00baf9ec`](#insn-00baf9ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf9e4`](#insn-00baf9e4) → [`00baf9f4`](#insn-00baf9f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf9e8`](#insn-00baf9e8) → [`00baf9f8`](#insn-00baf9f8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf9f0`](#insn-00baf9f0) → [`00baf9f8`](#insn-00baf9f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf9fc`](#insn-00baf9fc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafa00`](#insn-00bafa00) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafa04`](#insn-00bafa04) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baf8fc`](#insn-00baf8fc)

~~~json
{
  "source": "00baf8fc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf900`](#insn-00baf900)

~~~json
{
  "source": "00baf900",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf904`](#insn-00baf904)

~~~json
{
  "source": "00baf904",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf908`](#insn-00baf908)

~~~json
{
  "source": "00baf908",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf918`](#insn-00baf918)

~~~json
{
  "source": "00baf918",
  "target": "00baf9f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf938`](#insn-00baf938)

~~~json
{
  "source": "00baf938",
  "target": "00baf960",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf95c`](#insn-00baf95c)

~~~json
{
  "source": "00baf95c",
  "target": "00baf9a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf980`](#insn-00baf980)

~~~json
{
  "source": "00baf980",
  "target": "00baf93c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf994`](#insn-00baf994)

~~~json
{
  "source": "00baf994",
  "target": "00c590f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf998`](#insn-00baf998)

~~~json
{
  "source": "00baf998",
  "target": "00baf94c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf99c`](#insn-00baf99c)

~~~json
{
  "source": "00baf99c",
  "target": "00baf93c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf9a4`](#insn-00baf9a4)

~~~json
{
  "source": "00baf9a4",
  "target": "00baf9f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf9c8`](#insn-00baf9c8)

~~~json
{
  "source": "00baf9c8",
  "target": "00baf9ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf9dc`](#insn-00baf9dc)

~~~json
{
  "source": "00baf9dc",
  "target": "00c590f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf9e0`](#insn-00baf9e0)

~~~json
{
  "source": "00baf9e0",
  "target": "00baf9ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf9e4`](#insn-00baf9e4)

~~~json
{
  "source": "00baf9e4",
  "target": "00baf9f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf9e8`](#insn-00baf9e8)

~~~json
{
  "source": "00baf9e8",
  "target": "00baf9f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf9f0`](#insn-00baf9f0)

~~~json
{
  "source": "00baf9f0",
  "target": "00baf9f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf9fc`](#insn-00baf9fc)

~~~json
{
  "source": "00baf9fc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafa00`](#insn-00bafa00)

~~~json
{
  "source": "00bafa00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafa04`](#insn-00bafa04)

~~~json
{
  "source": "00bafa04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
