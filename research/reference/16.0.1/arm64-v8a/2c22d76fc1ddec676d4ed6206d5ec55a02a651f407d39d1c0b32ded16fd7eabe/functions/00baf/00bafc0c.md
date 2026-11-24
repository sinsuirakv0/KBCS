# 00bafc0c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00baf7e4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf7e4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0078.md#compare-2a3ea756d1982ecc667b384991589ed3)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bafca8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00bafca8.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0038.md#compare-bb47807f90e9247e7b38dfbfd0cffea5)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bafc0c",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7RPCCallEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_15__tree_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT_",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f65e5deaf6b2bcd6d6cef52e92f01bd075ec4a675381e239cdbb3cff7f8930fd",
  "source_text_sha256": "f65e5deaf6b2bcd6d6cef52e92f01bd075ec4a675381e239cdbb3cff7f8930fd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bafc0c",
        "00bafd1f"
      ]
    ],
    "bytes_sha256": "adecf181b27117d5b947edaf9a8e66f503cc357ddcc8deb28076ee0bede26420",
    "instruction_count": 69,
    "instruction_bytes": 276,
    "body_bytes": 276,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5cf30](../00c5c/00c5cf30.md)

## 呼び出し先

- [00c58050](../00c58/00c58050.md)

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
LAB_00bafc4c:
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
        if (uVar5 == 0) goto LAB_00bafc4c;
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
<a id="insn-00bafc0c"></a> `00bafc0c` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bafc10"></a> `00bafc10` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bafc14"></a> `00bafc14` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bafc18"></a> `00bafc18` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bafc1c"></a> `00bafc1c` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bafc20"></a> `00bafc20` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bafc24"></a> `00bafc24` | `77 8e 40 f8` | ldr x23,[x19, #0x8]! | `FALL_THROUGH`
<a id="insn-00bafc28"></a> `00bafc28` | `f7 06 00 b4` | cbz x23,0x00bafd04 | `CONDITIONAL_JUMP`
<a id="insn-00bafc2c"></a> `00bafc2c` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00bafc30"></a> `00bafc30` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bafc34"></a> `00bafc34` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00bafc38"></a> `00bafc38` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bafc3c"></a> `00bafc3c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bafc40"></a> `00bafc40` | `76 01 89 9a` | csel x22,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00bafc44"></a> `00bafc44` | `55 15 81 9a` | csinc x21,x10,x1,ne | `FALL_THROUGH`
<a id="insn-00bafc48"></a> `00bafc48` | `0a 00 00 14` | b 0x00bafc70 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafc4c"></a> `00bafc4c` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00bafc50"></a> `00bafc50` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00bafc54"></a> `00bafc54` | `1f 03 16 eb` | cmp x24,x22 | `FALL_THROUGH`
<a id="insn-00bafc58"></a> `00bafc58` | `00 21 9f 5a` | csinv w0,w8,wzr,cs | `FALL_THROUGH`
<a id="insn-00bafc5c"></a> `00bafc5c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bafc60"></a> `00bafc60` | `e8 a7 9f 1a` | cset w8,lt | `FALL_THROUGH`
<a id="insn-00bafc64"></a> `00bafc64` | `94 b2 97 9a` | csel x20,x20,x23,lt | `FALL_THROUGH`
<a id="insn-00bafc68"></a> `00bafc68` | `f7 5a 68 f8` | ldr x23,[x23, w8, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bafc6c"></a> `00bafc6c` | `37 02 00 b4` | cbz x23,0x00bafcb0 | `CONDITIONAL_JUMP`
<a id="insn-00bafc70"></a> `00bafc70` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-00bafc74"></a> `00bafc74` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00bafc78"></a> `00bafc78` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bafc7c"></a> `00bafc7c` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bafc80"></a> `00bafc80` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bafc84"></a> `00bafc84` | `78 01 8a 9a` | csel x24,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00bafc88"></a> `00bafc88` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00bafc8c"></a> `00bafc8c` | `c2 32 98 9a` | csel x2,x22,x24,cc | `FALL_THROUGH`
<a id="insn-00bafc90"></a> `00bafc90` | `e2 fd ff b4` | cbz x2,0x00bafc4c | `CONDITIONAL_JUMP`
<a id="insn-00bafc94"></a> `00bafc94` | `ea 1a 40 f9` | ldr x10,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00bafc98"></a> `00bafc98` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bafc9c"></a> `00bafc9c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bafca0"></a> `00bafca0` | `40 15 88 9a` | csinc x0,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00bafca4"></a> `00bafca4` | `eb a0 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00bafca8"></a> `00bafca8` | `a0 fd ff 35` | cbnz w0,0x00bafc5c | `CONDITIONAL_JUMP`
<a id="insn-00bafcac"></a> `00bafcac` | `e8 ff ff 17` | b 0x00bafc4c | `UNCONDITIONAL_JUMP`
<a id="insn-00bafcb0"></a> `00bafcb0` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00bafcb4"></a> `00bafcb4` | `80 02 00 54` | b.eq 0x00bafd04 | `CONDITIONAL_JUMP`
<a id="insn-00bafcb8"></a> `00bafcb8` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00bafcbc"></a> `00bafcbc` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00bafcc0"></a> `00bafcc0` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bafcc4"></a> `00bafcc4` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bafcc8"></a> `00bafcc8` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bafccc"></a> `00bafccc` | `77 01 8a 9a` | csel x23,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00bafcd0"></a> `00bafcd0` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00bafcd4"></a> `00bafcd4` | `e2 32 96 9a` | csel x2,x23,x22,cc | `FALL_THROUGH`
<a id="insn-00bafcd8"></a> `00bafcd8` | `22 01 00 b4` | cbz x2,0x00bafcfc | `CONDITIONAL_JUMP`
<a id="insn-00bafcdc"></a> `00bafcdc` | `8a 1a 40 f9` | ldr x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00bafce0"></a> `00bafce0` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bafce4"></a> `00bafce4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bafce8"></a> `00bafce8` | `41 15 88 9a` | csinc x1,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00bafcec"></a> `00bafcec` | `d9 a0 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00bafcf0"></a> `00bafcf0` | `60 00 00 34` | cbz w0,0x00bafcfc | `CONDITIONAL_JUMP`
<a id="insn-00bafcf4"></a> `00bafcf4` | `80 00 f8 37` | tbnz w0,#0x1f,0x00bafd04 | `CONDITIONAL_JUMP`
<a id="insn-00bafcf8"></a> `00bafcf8` | `04 00 00 14` | b 0x00bafd08 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafcfc"></a> `00bafcfc` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-00bafd00"></a> `00bafd00` | `42 00 00 54` | b.cs 0x00bafd08 | `CONDITIONAL_JUMP`
<a id="insn-00bafd04"></a> `00bafd04` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00bafd08"></a> `00bafd08` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bafd0c"></a> `00bafd0c` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bafd10"></a> `00bafd10` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bafd14"></a> `00bafd14` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bafd18"></a> `00bafd18` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bafd1c"></a> `00bafd1c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bafc0c`](#insn-00bafc0c) 範囲 `[['00bafc0c', '00bafc2b']]`
  - `CONDITIONAL_JUMP` [`00bafc28`](#insn-00bafc28) → [`00bafd04`](#insn-00bafd04)
  - `FALL_THROUGH` [`00bafc28`](#insn-00bafc28) → [`00bafc2c`](#insn-00bafc2c)
- ブロック [`00bafc2c`](#insn-00bafc2c) 範囲 `[['00bafc2c', '00bafc4b']]`
  - `UNCONDITIONAL_JUMP` [`00bafc48`](#insn-00bafc48) → [`00bafc70`](#insn-00bafc70)
- ブロック [`00bafc4c`](#insn-00bafc4c) 範囲 `[['00bafc4c', '00bafc5b']]`
  - `FALL_THROUGH` [`00bafc58`](#insn-00bafc58) → [`00bafc5c`](#insn-00bafc5c)
- ブロック [`00bafc5c`](#insn-00bafc5c) 範囲 `[['00bafc5c', '00bafc6f']]`
  - `CONDITIONAL_JUMP` [`00bafc6c`](#insn-00bafc6c) → [`00bafcb0`](#insn-00bafcb0)
  - `FALL_THROUGH` [`00bafc6c`](#insn-00bafc6c) → [`00bafc70`](#insn-00bafc70)
- ブロック [`00bafc70`](#insn-00bafc70) 範囲 `[['00bafc70', '00bafc93']]`
  - `CONDITIONAL_JUMP` [`00bafc90`](#insn-00bafc90) → [`00bafc4c`](#insn-00bafc4c)
  - `FALL_THROUGH` [`00bafc90`](#insn-00bafc90) → [`00bafc94`](#insn-00bafc94)
- ブロック [`00bafc94`](#insn-00bafc94) 範囲 `[['00bafc94', '00bafcab']]`
  - `CONDITIONAL_JUMP` [`00bafca8`](#insn-00bafca8) → [`00bafc5c`](#insn-00bafc5c)
  - `FALL_THROUGH` [`00bafca8`](#insn-00bafca8) → [`00bafcac`](#insn-00bafcac)
- ブロック [`00bafcac`](#insn-00bafcac) 範囲 `[['00bafcac', '00bafcaf']]`
  - `UNCONDITIONAL_JUMP` [`00bafcac`](#insn-00bafcac) → [`00bafc4c`](#insn-00bafc4c)
- ブロック [`00bafcb0`](#insn-00bafcb0) 範囲 `[['00bafcb0', '00bafcb7']]`
  - `CONDITIONAL_JUMP` [`00bafcb4`](#insn-00bafcb4) → [`00bafd04`](#insn-00bafd04)
  - `FALL_THROUGH` [`00bafcb4`](#insn-00bafcb4) → [`00bafcb8`](#insn-00bafcb8)
- ブロック [`00bafcb8`](#insn-00bafcb8) 範囲 `[['00bafcb8', '00bafcdb']]`
  - `CONDITIONAL_JUMP` [`00bafcd8`](#insn-00bafcd8) → [`00bafcfc`](#insn-00bafcfc)
  - `FALL_THROUGH` [`00bafcd8`](#insn-00bafcd8) → [`00bafcdc`](#insn-00bafcdc)
- ブロック [`00bafcdc`](#insn-00bafcdc) 範囲 `[['00bafcdc', '00bafcf3']]`
  - `CONDITIONAL_JUMP` [`00bafcf0`](#insn-00bafcf0) → [`00bafcfc`](#insn-00bafcfc)
  - `FALL_THROUGH` [`00bafcf0`](#insn-00bafcf0) → [`00bafcf4`](#insn-00bafcf4)
- ブロック [`00bafcf4`](#insn-00bafcf4) 範囲 `[['00bafcf4', '00bafcf7']]`
  - `CONDITIONAL_JUMP` [`00bafcf4`](#insn-00bafcf4) → [`00bafd04`](#insn-00bafd04)
  - `FALL_THROUGH` [`00bafcf4`](#insn-00bafcf4) → [`00bafcf8`](#insn-00bafcf8)
- ブロック [`00bafcf8`](#insn-00bafcf8) 範囲 `[['00bafcf8', '00bafcfb']]`
  - `UNCONDITIONAL_JUMP` [`00bafcf8`](#insn-00bafcf8) → [`00bafd08`](#insn-00bafd08)
- ブロック [`00bafcfc`](#insn-00bafcfc) 範囲 `[['00bafcfc', '00bafd03']]`
  - `CONDITIONAL_JUMP` [`00bafd00`](#insn-00bafd00) → [`00bafd08`](#insn-00bafd08)
  - `FALL_THROUGH` [`00bafd00`](#insn-00bafd00) → [`00bafd04`](#insn-00bafd04)
- ブロック [`00bafd04`](#insn-00bafd04) 範囲 `[['00bafd04', '00bafd07']]`
  - `FALL_THROUGH` [`00bafd04`](#insn-00bafd04) → [`00bafd08`](#insn-00bafd08)
- ブロック [`00bafd08`](#insn-00bafd08) 範囲 `[['00bafd08', '00bafd1f']]`

## 命令位置別の参照

- [`00bafc0c`](#insn-00bafc0c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc10`](#insn-00bafc10) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc14`](#insn-00bafc14) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc18`](#insn-00bafc18) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc28`](#insn-00bafc28) → [`00bafd04`](#insn-00bafd04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc48`](#insn-00bafc48) → [`00bafc70`](#insn-00bafc70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc6c`](#insn-00bafc6c) → [`00bafcb0`](#insn-00bafcb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc90`](#insn-00bafc90) → [`00bafc4c`](#insn-00bafc4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafca4`](#insn-00bafca4) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00bafca8`](#insn-00bafca8) → [`00bafc5c`](#insn-00bafc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafcac`](#insn-00bafcac) → [`00bafc4c`](#insn-00bafc4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafcb4`](#insn-00bafcb4) → [`00bafd04`](#insn-00bafd04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafcd8`](#insn-00bafcd8) → [`00bafcfc`](#insn-00bafcfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafcec`](#insn-00bafcec) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00bafcf0`](#insn-00bafcf0) → [`00bafcfc`](#insn-00bafcfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafcf4`](#insn-00bafcf4) → [`00bafd04`](#insn-00bafd04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafcf8`](#insn-00bafcf8) → [`00bafd08`](#insn-00bafd08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd00`](#insn-00bafd00) → [`00bafd08`](#insn-00bafd08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd0c`](#insn-00bafd0c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd10`](#insn-00bafd10) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafd14`](#insn-00bafd14) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bafc0c`](#insn-00bafc0c)

~~~json
{
  "source": "00bafc0c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc10`](#insn-00bafc10)

~~~json
{
  "source": "00bafc10",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc14`](#insn-00bafc14)

~~~json
{
  "source": "00bafc14",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc18`](#insn-00bafc18)

~~~json
{
  "source": "00bafc18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc28`](#insn-00bafc28)

~~~json
{
  "source": "00bafc28",
  "target": "00bafd04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc48`](#insn-00bafc48)

~~~json
{
  "source": "00bafc48",
  "target": "00bafc70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc6c`](#insn-00bafc6c)

~~~json
{
  "source": "00bafc6c",
  "target": "00bafcb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc90`](#insn-00bafc90)

~~~json
{
  "source": "00bafc90",
  "target": "00bafc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafca4`](#insn-00bafca4)

~~~json
{
  "source": "00bafca4",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafca8`](#insn-00bafca8)

~~~json
{
  "source": "00bafca8",
  "target": "00bafc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafcac`](#insn-00bafcac)

~~~json
{
  "source": "00bafcac",
  "target": "00bafc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafcb4`](#insn-00bafcb4)

~~~json
{
  "source": "00bafcb4",
  "target": "00bafd04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafcd8`](#insn-00bafcd8)

~~~json
{
  "source": "00bafcd8",
  "target": "00bafcfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafcec`](#insn-00bafcec)

~~~json
{
  "source": "00bafcec",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafcf0`](#insn-00bafcf0)

~~~json
{
  "source": "00bafcf0",
  "target": "00bafcfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafcf4`](#insn-00bafcf4)

~~~json
{
  "source": "00bafcf4",
  "target": "00bafd04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafcf8`](#insn-00bafcf8)

~~~json
{
  "source": "00bafcf8",
  "target": "00bafd08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd00`](#insn-00bafd00)

~~~json
{
  "source": "00bafd00",
  "target": "00bafd08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd0c`](#insn-00bafd0c)

~~~json
{
  "source": "00bafd0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd10`](#insn-00bafd10)

~~~json
{
  "source": "00bafd10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafd14`](#insn-00bafd14)

~~~json
{
  "source": "00bafd14",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
