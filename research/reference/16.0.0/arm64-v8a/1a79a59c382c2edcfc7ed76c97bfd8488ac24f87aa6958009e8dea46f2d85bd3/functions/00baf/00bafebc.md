# 00bafebc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b4458c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b4458c.md) · 移動量 `+0x6b930`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0016.md#compare-5859e5ea939102abbd3247c80a0b31e6)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bb02e4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb02e4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0038.md#compare-1812a0e763448aa2a714b38e50f09a39)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bafebc",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_15__tree_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT_",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f52dbe87c0c0d1fe34e77e54a959a669e60d10d9d97b6e5259617c94a6bf4593",
  "source_text_sha256": "f52dbe87c0c0d1fe34e77e54a959a669e60d10d9d97b6e5259617c94a6bf4593",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bafebc",
        "00baffcf"
      ]
    ],
    "bytes_sha256": "67d12c060a2c1308a78b290abf93e5fbc7e48c3eeec26a305843e90d62771b0c",
    "instruction_count": 69,
    "instruction_bytes": 276,
    "body_bytes": 276,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5cb90](../00c5c/00c5cb90.md)

## 呼び出し先

- [00c57c50](../00c57/00c57c50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2206 bytes

~~~c

long * _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_15__tree_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT_
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
LAB_00bafefc:
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
        if (uVar5 == 0) goto LAB_00bafefc;
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
<a id="insn-00bafebc"></a> `00bafebc` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bafec0"></a> `00bafec0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bafec4"></a> `00bafec4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bafec8"></a> `00bafec8` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bafecc"></a> `00bafecc` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bafed0"></a> `00bafed0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bafed4"></a> `00bafed4` | `77 8e 40 f8` | ldr x23,[x19, #0x8]! | `FALL_THROUGH`
<a id="insn-00bafed8"></a> `00bafed8` | `f7 06 00 b4` | cbz x23,0x00baffb4 | `CONDITIONAL_JUMP`
<a id="insn-00bafedc"></a> `00bafedc` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00bafee0"></a> `00bafee0` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bafee4"></a> `00bafee4` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00bafee8"></a> `00bafee8` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bafeec"></a> `00bafeec` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bafef0"></a> `00bafef0` | `76 01 89 9a` | csel x22,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00bafef4"></a> `00bafef4` | `55 15 81 9a` | csinc x21,x10,x1,ne | `FALL_THROUGH`
<a id="insn-00bafef8"></a> `00bafef8` | `0a 00 00 14` | b 0x00baff20 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafefc"></a> `00bafefc` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00baff00"></a> `00baff00` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00baff04"></a> `00baff04` | `1f 03 16 eb` | cmp x24,x22 | `FALL_THROUGH`
<a id="insn-00baff08"></a> `00baff08` | `00 21 9f 5a` | csinv w0,w8,wzr,cs | `FALL_THROUGH`
<a id="insn-00baff0c"></a> `00baff0c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00baff10"></a> `00baff10` | `e8 a7 9f 1a` | cset w8,lt | `FALL_THROUGH`
<a id="insn-00baff14"></a> `00baff14` | `94 b2 97 9a` | csel x20,x20,x23,lt | `FALL_THROUGH`
<a id="insn-00baff18"></a> `00baff18` | `f7 5a 68 f8` | ldr x23,[x23, w8, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00baff1c"></a> `00baff1c` | `37 02 00 b4` | cbz x23,0x00baff60 | `CONDITIONAL_JUMP`
<a id="insn-00baff20"></a> `00baff20` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-00baff24"></a> `00baff24` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00baff28"></a> `00baff28` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00baff2c"></a> `00baff2c` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00baff30"></a> `00baff30` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baff34"></a> `00baff34` | `78 01 8a 9a` | csel x24,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00baff38"></a> `00baff38` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00baff3c"></a> `00baff3c` | `c2 32 98 9a` | csel x2,x22,x24,cc | `FALL_THROUGH`
<a id="insn-00baff40"></a> `00baff40` | `e2 fd ff b4` | cbz x2,0x00bafefc | `CONDITIONAL_JUMP`
<a id="insn-00baff44"></a> `00baff44` | `ea 1a 40 f9` | ldr x10,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00baff48"></a> `00baff48` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baff4c"></a> `00baff4c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00baff50"></a> `00baff50` | `40 15 88 9a` | csinc x0,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00baff54"></a> `00baff54` | `3f 9f 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00baff58"></a> `00baff58` | `a0 fd ff 35` | cbnz w0,0x00baff0c | `CONDITIONAL_JUMP`
<a id="insn-00baff5c"></a> `00baff5c` | `e8 ff ff 17` | b 0x00bafefc | `UNCONDITIONAL_JUMP`
<a id="insn-00baff60"></a> `00baff60` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00baff64"></a> `00baff64` | `80 02 00 54` | b.eq 0x00baffb4 | `CONDITIONAL_JUMP`
<a id="insn-00baff68"></a> `00baff68` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00baff6c"></a> `00baff6c` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00baff70"></a> `00baff70` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00baff74"></a> `00baff74` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00baff78"></a> `00baff78` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baff7c"></a> `00baff7c` | `77 01 8a 9a` | csel x23,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00baff80"></a> `00baff80` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00baff84"></a> `00baff84` | `e2 32 96 9a` | csel x2,x23,x22,cc | `FALL_THROUGH`
<a id="insn-00baff88"></a> `00baff88` | `22 01 00 b4` | cbz x2,0x00baffac | `CONDITIONAL_JUMP`
<a id="insn-00baff8c"></a> `00baff8c` | `8a 1a 40 f9` | ldr x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00baff90"></a> `00baff90` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baff94"></a> `00baff94` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00baff98"></a> `00baff98` | `41 15 88 9a` | csinc x1,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00baff9c"></a> `00baff9c` | `2d 9f 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00baffa0"></a> `00baffa0` | `60 00 00 34` | cbz w0,0x00baffac | `CONDITIONAL_JUMP`
<a id="insn-00baffa4"></a> `00baffa4` | `80 00 f8 37` | tbnz w0,#0x1f,0x00baffb4 | `CONDITIONAL_JUMP`
<a id="insn-00baffa8"></a> `00baffa8` | `04 00 00 14` | b 0x00baffb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00baffac"></a> `00baffac` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-00baffb0"></a> `00baffb0` | `42 00 00 54` | b.cs 0x00baffb8 | `CONDITIONAL_JUMP`
<a id="insn-00baffb4"></a> `00baffb4` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00baffb8"></a> `00baffb8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00baffbc"></a> `00baffbc` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baffc0"></a> `00baffc0` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baffc4"></a> `00baffc4` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baffc8"></a> `00baffc8` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00baffcc"></a> `00baffcc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bafebc`](#insn-00bafebc) 範囲 `[['00bafebc', '00bafedb']]`
  - `CONDITIONAL_JUMP` [`00bafed8`](#insn-00bafed8) → [`00baffb4`](#insn-00baffb4)
  - `FALL_THROUGH` [`00bafed8`](#insn-00bafed8) → [`00bafedc`](#insn-00bafedc)
- ブロック [`00bafedc`](#insn-00bafedc) 範囲 `[['00bafedc', '00bafefb']]`
  - `UNCONDITIONAL_JUMP` [`00bafef8`](#insn-00bafef8) → [`00baff20`](#insn-00baff20)
- ブロック [`00bafefc`](#insn-00bafefc) 範囲 `[['00bafefc', '00baff0b']]`
  - `FALL_THROUGH` [`00baff08`](#insn-00baff08) → [`00baff0c`](#insn-00baff0c)
- ブロック [`00baff0c`](#insn-00baff0c) 範囲 `[['00baff0c', '00baff1f']]`
  - `CONDITIONAL_JUMP` [`00baff1c`](#insn-00baff1c) → [`00baff60`](#insn-00baff60)
  - `FALL_THROUGH` [`00baff1c`](#insn-00baff1c) → [`00baff20`](#insn-00baff20)
- ブロック [`00baff20`](#insn-00baff20) 範囲 `[['00baff20', '00baff43']]`
  - `CONDITIONAL_JUMP` [`00baff40`](#insn-00baff40) → [`00bafefc`](#insn-00bafefc)
  - `FALL_THROUGH` [`00baff40`](#insn-00baff40) → [`00baff44`](#insn-00baff44)
- ブロック [`00baff44`](#insn-00baff44) 範囲 `[['00baff44', '00baff5b']]`
  - `CONDITIONAL_JUMP` [`00baff58`](#insn-00baff58) → [`00baff0c`](#insn-00baff0c)
  - `FALL_THROUGH` [`00baff58`](#insn-00baff58) → [`00baff5c`](#insn-00baff5c)
- ブロック [`00baff5c`](#insn-00baff5c) 範囲 `[['00baff5c', '00baff5f']]`
  - `UNCONDITIONAL_JUMP` [`00baff5c`](#insn-00baff5c) → [`00bafefc`](#insn-00bafefc)
- ブロック [`00baff60`](#insn-00baff60) 範囲 `[['00baff60', '00baff67']]`
  - `CONDITIONAL_JUMP` [`00baff64`](#insn-00baff64) → [`00baffb4`](#insn-00baffb4)
  - `FALL_THROUGH` [`00baff64`](#insn-00baff64) → [`00baff68`](#insn-00baff68)
- ブロック [`00baff68`](#insn-00baff68) 範囲 `[['00baff68', '00baff8b']]`
  - `CONDITIONAL_JUMP` [`00baff88`](#insn-00baff88) → [`00baffac`](#insn-00baffac)
  - `FALL_THROUGH` [`00baff88`](#insn-00baff88) → [`00baff8c`](#insn-00baff8c)
- ブロック [`00baff8c`](#insn-00baff8c) 範囲 `[['00baff8c', '00baffa3']]`
  - `CONDITIONAL_JUMP` [`00baffa0`](#insn-00baffa0) → [`00baffac`](#insn-00baffac)
  - `FALL_THROUGH` [`00baffa0`](#insn-00baffa0) → [`00baffa4`](#insn-00baffa4)
- ブロック [`00baffa4`](#insn-00baffa4) 範囲 `[['00baffa4', '00baffa7']]`
  - `CONDITIONAL_JUMP` [`00baffa4`](#insn-00baffa4) → [`00baffb4`](#insn-00baffb4)
  - `FALL_THROUGH` [`00baffa4`](#insn-00baffa4) → [`00baffa8`](#insn-00baffa8)
- ブロック [`00baffa8`](#insn-00baffa8) 範囲 `[['00baffa8', '00baffab']]`
  - `UNCONDITIONAL_JUMP` [`00baffa8`](#insn-00baffa8) → [`00baffb8`](#insn-00baffb8)
- ブロック [`00baffac`](#insn-00baffac) 範囲 `[['00baffac', '00baffb3']]`
  - `CONDITIONAL_JUMP` [`00baffb0`](#insn-00baffb0) → [`00baffb8`](#insn-00baffb8)
  - `FALL_THROUGH` [`00baffb0`](#insn-00baffb0) → [`00baffb4`](#insn-00baffb4)
- ブロック [`00baffb4`](#insn-00baffb4) 範囲 `[['00baffb4', '00baffb7']]`
  - `FALL_THROUGH` [`00baffb4`](#insn-00baffb4) → [`00baffb8`](#insn-00baffb8)
- ブロック [`00baffb8`](#insn-00baffb8) 範囲 `[['00baffb8', '00baffcf']]`

## 命令位置別の参照

- [`00bafebc`](#insn-00bafebc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafec0`](#insn-00bafec0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafec4`](#insn-00bafec4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafec8`](#insn-00bafec8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafed8`](#insn-00bafed8) → [`00baffb4`](#insn-00baffb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafef8`](#insn-00bafef8) → [`00baff20`](#insn-00baff20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baff1c`](#insn-00baff1c) → [`00baff60`](#insn-00baff60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baff40`](#insn-00baff40) → [`00bafefc`](#insn-00bafefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baff54`](#insn-00baff54) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00baff58`](#insn-00baff58) → [`00baff0c`](#insn-00baff0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baff5c`](#insn-00baff5c) → [`00bafefc`](#insn-00bafefc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baff64`](#insn-00baff64) → [`00baffb4`](#insn-00baffb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baff88`](#insn-00baff88) → [`00baffac`](#insn-00baffac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baff9c`](#insn-00baff9c) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00baffa0`](#insn-00baffa0) → [`00baffac`](#insn-00baffac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffa4`](#insn-00baffa4) → [`00baffb4`](#insn-00baffb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffa8`](#insn-00baffa8) → [`00baffb8`](#insn-00baffb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffb0`](#insn-00baffb0) → [`00baffb8`](#insn-00baffb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffbc`](#insn-00baffbc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffc0`](#insn-00baffc0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffc4`](#insn-00baffc4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bafebc`](#insn-00bafebc)

~~~json
{
  "source": "00bafebc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafec0`](#insn-00bafec0)

~~~json
{
  "source": "00bafec0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafec4`](#insn-00bafec4)

~~~json
{
  "source": "00bafec4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafec8`](#insn-00bafec8)

~~~json
{
  "source": "00bafec8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafed8`](#insn-00bafed8)

~~~json
{
  "source": "00bafed8",
  "target": "00baffb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafef8`](#insn-00bafef8)

~~~json
{
  "source": "00bafef8",
  "target": "00baff20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baff1c`](#insn-00baff1c)

~~~json
{
  "source": "00baff1c",
  "target": "00baff60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baff40`](#insn-00baff40)

~~~json
{
  "source": "00baff40",
  "target": "00bafefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baff54`](#insn-00baff54)

~~~json
{
  "source": "00baff54",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baff58`](#insn-00baff58)

~~~json
{
  "source": "00baff58",
  "target": "00baff0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baff5c`](#insn-00baff5c)

~~~json
{
  "source": "00baff5c",
  "target": "00bafefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baff64`](#insn-00baff64)

~~~json
{
  "source": "00baff64",
  "target": "00baffb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baff88`](#insn-00baff88)

~~~json
{
  "source": "00baff88",
  "target": "00baffac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baff9c`](#insn-00baff9c)

~~~json
{
  "source": "00baff9c",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baffa0`](#insn-00baffa0)

~~~json
{
  "source": "00baffa0",
  "target": "00baffac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baffa4`](#insn-00baffa4)

~~~json
{
  "source": "00baffa4",
  "target": "00baffb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baffa8`](#insn-00baffa8)

~~~json
{
  "source": "00baffa8",
  "target": "00baffb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baffb0`](#insn-00baffb0)

~~~json
{
  "source": "00baffb0",
  "target": "00baffb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baffbc`](#insn-00baffbc)

~~~json
{
  "source": "00baffbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baffc0`](#insn-00baffc0)

~~~json
{
  "source": "00baffc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baffc4`](#insn-00baffc4)

~~~json
{
  "source": "00baffc4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
