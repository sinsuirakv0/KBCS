# 00bae7cc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b42fa0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b42/00b42fa0.md) · 移動量 `+0x6b82c`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0016.md#compare-8776ca5804450ed62e754c569854fd87)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00baebf4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00baebf4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0038.md#compare-a82e46adb10c5e94fcbfcf914fdde51b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bae7cc",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers4TypeEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5c4d520ce0359660832430bea6ce56efd26ef317ae66e9b5dcaee1ce5efa9745",
  "source_text_sha256": "5c4d520ce0359660832430bea6ce56efd26ef317ae66e9b5dcaee1ce5efa9745",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bae7cc",
        "00bae8eb"
      ]
    ],
    "bytes_sha256": "da4a1934a4ed4e17b4c27f9859747903f6c30fc1caa79c4816273d6dc32bd655",
    "instruction_count": 72,
    "instruction_bytes": 288,
    "body_bytes": 288,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5ca80](../00c5c/00c5ca80.md)

## 呼び出し先

- [00c57c50](../00c57/00c57c50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2190 bytes

~~~c

long * _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers4TypeEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_
                 (long param_1,undefined8 *param_2,byte *param_3)

{
  ulong uVar1;
  size_t __n;
  void *__s2;
  ulong uVar2;
  byte *__s1;
  byte bVar3;
  int iVar4;
  long *plVar5;
  long *plVar6;
  long *plVar7;
  void *__s1_00;
  
  plVar5 = (long *)(param_1 + 8);
  plVar6 = (long *)*plVar5;
  if (plVar6 == (long *)0x0) {
    *param_2 = plVar5;
    return plVar5;
  }
  uVar2 = *(ulong *)(param_3 + 8);
  __s1 = *(byte **)(param_3 + 0x10);
  plVar5 = (long *)(param_1 + 8);
  if ((*param_3 & 1) == 0) {
    __s1 = param_3 + 1;
    uVar2 = (ulong)(*param_3 >> 1);
  }
  do {
    while( true ) {
      plVar7 = plVar6;
      bVar3 = *(byte *)(plVar7 + 4);
      uVar1 = (ulong)(bVar3 >> 1);
      if ((bVar3 & 1) != 0) {
        uVar1 = plVar7[5];
      }
      __n = uVar1;
      if (uVar2 <= uVar1) {
        __n = uVar2;
      }
      if (__n == 0) break;
      __s1_00 = (void *)plVar7[6];
      __s2 = __s1_00;
      if ((bVar3 & 1) == 0) {
        __s2 = (void *)((long)plVar7 + 0x21);
      }
      iVar4 = memcmp(__s1,__s2,__n);
      if (iVar4 == 0) break;
      if (iVar4 < 0) goto LAB_00bae880;
LAB_00bae898:
      if ((bVar3 & 1) == 0) {
        __s1_00 = (void *)((long)plVar7 + 0x21);
      }
      iVar4 = memcmp(__s1_00,__s1,__n);
      if (iVar4 == 0) goto LAB_00bae818;
      if (-1 < iVar4) goto LAB_00bae8b4;
LAB_00bae820:
      plVar5 = plVar7 + 1;
      plVar6 = (long *)*plVar5;
      if ((long *)*plVar5 == (long *)0x0) {
LAB_00bae8b4:
        *param_2 = plVar7;
        return plVar5;
      }
    }
    if (uVar1 <= uVar2) {
      if (__n != 0) {
        __s1_00 = (void *)plVar7[6];
        goto LAB_00bae898;
      }
LAB_00bae818:
      if (uVar2 <= uVar1) goto LAB_00bae8b4;
      goto LAB_00bae820;
    }
LAB_00bae880:
    plVar5 = plVar7;
    plVar6 = (long *)*plVar7;
    if ((long *)*plVar7 == (long *)0x0) {
      *param_2 = plVar7;
      return plVar7;
    }
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bae7cc"></a> `00bae7cc` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00bae7d0"></a> `00bae7d0` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bae7d4"></a> `00bae7d4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bae7d8"></a> `00bae7d8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bae7dc"></a> `00bae7dc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bae7e0"></a> `00bae7e0` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bae7e4"></a> `00bae7e4` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bae7e8"></a> `00bae7e8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bae7ec"></a> `00bae7ec` | `97 8e 40 f8` | ldr x23,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00bae7f0"></a> `00bae7f0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bae7f4"></a> `00bae7f4` | `57 06 00 b4` | cbz x23,0x00bae8bc | `CONDITIONAL_JUMP`
<a id="insn-00bae7f8"></a> `00bae7f8` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00bae7fc"></a> `00bae7fc` | `49 a8 40 a9` | ldp x9,x10,[x2, #0x8] | `FALL_THROUGH`
<a id="insn-00bae800"></a> `00bae800` | `14 20 00 91` | add x20,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bae804"></a> `00bae804` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bae808"></a> `00bae808` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bae80c"></a> `00bae80c` | `78 01 89 9a` | csel x24,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00bae810"></a> `00bae810` | `55 15 82 9a` | csinc x21,x10,x2,ne | `FALL_THROUGH`
<a id="insn-00bae814"></a> `00bae814` | `07 00 00 14` | b 0x00bae830 | `UNCONDITIONAL_JUMP`
<a id="insn-00bae818"></a> `00bae818` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00bae81c"></a> `00bae81c` | `c2 04 00 54` | b.cs 0x00bae8b4 | `CONDITIONAL_JUMP`
<a id="insn-00bae820"></a> `00bae820` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00bae824"></a> `00bae824` | `88 8e 40 f8` | ldr x8,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00bae828"></a> `00bae828` | `68 04 00 b4` | cbz x8,0x00bae8b4 | `CONDITIONAL_JUMP`
<a id="insn-00bae82c"></a> `00bae82c` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00bae830"></a> `00bae830` | `fa 03 17 aa` | mov x26,x23 | `FALL_THROUGH`
<a id="insn-00bae834"></a> `00bae834` | `5b 0f 42 38` | ldrb w27,[x26, #0x20]! | `FALL_THROUGH`
<a id="insn-00bae838"></a> `00bae838` | `48 07 40 f9` | ldr x8,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00bae83c"></a> `00bae83c` | `69 ff 41 d3` | lsr x9,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00bae840"></a> `00bae840` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00bae844"></a> `00bae844` | `39 01 88 9a` | csel x25,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00bae848"></a> `00bae848` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00bae84c"></a> `00bae84c` | `36 33 98 9a` | csel x22,x25,x24,cc | `FALL_THROUGH`
<a id="insn-00bae850"></a> `00bae850` | `56 01 00 b4` | cbz x22,0x00bae878 | `CONDITIONAL_JUMP`
<a id="insn-00bae854"></a> `00bae854` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00bae858"></a> `00bae858` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00bae85c"></a> `00bae85c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bae860"></a> `00bae860` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bae864"></a> `00bae864` | `81 17 9a 9a` | csinc x1,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00bae868"></a> `00bae868` | `fa a4 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bae86c"></a> `00bae86c` | `60 00 00 34` | cbz w0,0x00bae878 | `CONDITIONAL_JUMP`
<a id="insn-00bae870"></a> `00bae870` | `80 00 f8 37` | tbnz w0,#0x1f,0x00bae880 | `CONDITIONAL_JUMP`
<a id="insn-00bae874"></a> `00bae874` | `09 00 00 14` | b 0x00bae898 | `UNCONDITIONAL_JUMP`
<a id="insn-00bae878"></a> `00bae878` | `1f 03 19 eb` | cmp x24,x25 | `FALL_THROUGH`
<a id="insn-00bae87c"></a> `00bae87c` | `a2 00 00 54` | b.cs 0x00bae890 | `CONDITIONAL_JUMP`
<a id="insn-00bae880"></a> `00bae880` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00bae884"></a> `00bae884` | `08 02 00 b4` | cbz x8,0x00bae8c4 | `CONDITIONAL_JUMP`
<a id="insn-00bae888"></a> `00bae888` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00bae88c"></a> `00bae88c` | `e8 ff ff 17` | b 0x00bae82c | `UNCONDITIONAL_JUMP`
<a id="insn-00bae890"></a> `00bae890` | `56 fc ff b4` | cbz x22,0x00bae818 | `CONDITIONAL_JUMP`
<a id="insn-00bae894"></a> `00bae894` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00bae898"></a> `00bae898` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00bae89c"></a> `00bae89c` | `80 17 9a 9a` | csinc x0,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00bae8a0"></a> `00bae8a0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bae8a4"></a> `00bae8a4` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bae8a8"></a> `00bae8a8` | `ea a4 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bae8ac"></a> `00bae8ac` | `60 fb ff 34` | cbz w0,0x00bae818 | `CONDITIONAL_JUMP`
<a id="insn-00bae8b0"></a> `00bae8b0` | `80 fb ff 37` | tbnz w0,#0x1f,0x00bae820 | `CONDITIONAL_JUMP`
<a id="insn-00bae8b4"></a> `00bae8b4` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00bae8b8"></a> `00bae8b8` | `05 00 00 14` | b 0x00bae8cc | `UNCONDITIONAL_JUMP`
<a id="insn-00bae8bc"></a> `00bae8bc` | `74 02 00 f9` | str x20,[x19] | `FALL_THROUGH`
<a id="insn-00bae8c0"></a> `00bae8c0` | `03 00 00 14` | b 0x00bae8cc | `UNCONDITIONAL_JUMP`
<a id="insn-00bae8c4"></a> `00bae8c4` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00bae8c8"></a> `00bae8c8` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00bae8cc"></a> `00bae8cc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bae8d0"></a> `00bae8d0` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bae8d4"></a> `00bae8d4` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bae8d8"></a> `00bae8d8` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bae8dc"></a> `00bae8dc` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bae8e0"></a> `00bae8e0` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bae8e4"></a> `00bae8e4` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00bae8e8"></a> `00bae8e8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bae7cc`](#insn-00bae7cc) 範囲 `[['00bae7cc', '00bae7f7']]`
  - `CONDITIONAL_JUMP` [`00bae7f4`](#insn-00bae7f4) → [`00bae8bc`](#insn-00bae8bc)
  - `FALL_THROUGH` [`00bae7f4`](#insn-00bae7f4) → [`00bae7f8`](#insn-00bae7f8)
- ブロック [`00bae7f8`](#insn-00bae7f8) 範囲 `[['00bae7f8', '00bae817']]`
  - `UNCONDITIONAL_JUMP` [`00bae814`](#insn-00bae814) → [`00bae830`](#insn-00bae830)
- ブロック [`00bae818`](#insn-00bae818) 範囲 `[['00bae818', '00bae81f']]`
  - `CONDITIONAL_JUMP` [`00bae81c`](#insn-00bae81c) → [`00bae8b4`](#insn-00bae8b4)
  - `FALL_THROUGH` [`00bae81c`](#insn-00bae81c) → [`00bae820`](#insn-00bae820)
- ブロック [`00bae820`](#insn-00bae820) 範囲 `[['00bae820', '00bae82b']]`
  - `CONDITIONAL_JUMP` [`00bae828`](#insn-00bae828) → [`00bae8b4`](#insn-00bae8b4)
  - `FALL_THROUGH` [`00bae828`](#insn-00bae828) → [`00bae82c`](#insn-00bae82c)
- ブロック [`00bae82c`](#insn-00bae82c) 範囲 `[['00bae82c', '00bae82f']]`
  - `FALL_THROUGH` [`00bae82c`](#insn-00bae82c) → [`00bae830`](#insn-00bae830)
- ブロック [`00bae830`](#insn-00bae830) 範囲 `[['00bae830', '00bae853']]`
  - `CONDITIONAL_JUMP` [`00bae850`](#insn-00bae850) → [`00bae878`](#insn-00bae878)
  - `FALL_THROUGH` [`00bae850`](#insn-00bae850) → [`00bae854`](#insn-00bae854)
- ブロック [`00bae854`](#insn-00bae854) 範囲 `[['00bae854', '00bae86f']]`
  - `CONDITIONAL_JUMP` [`00bae86c`](#insn-00bae86c) → [`00bae878`](#insn-00bae878)
  - `FALL_THROUGH` [`00bae86c`](#insn-00bae86c) → [`00bae870`](#insn-00bae870)
- ブロック [`00bae870`](#insn-00bae870) 範囲 `[['00bae870', '00bae873']]`
  - `CONDITIONAL_JUMP` [`00bae870`](#insn-00bae870) → [`00bae880`](#insn-00bae880)
  - `FALL_THROUGH` [`00bae870`](#insn-00bae870) → [`00bae874`](#insn-00bae874)
- ブロック [`00bae874`](#insn-00bae874) 範囲 `[['00bae874', '00bae877']]`
  - `UNCONDITIONAL_JUMP` [`00bae874`](#insn-00bae874) → [`00bae898`](#insn-00bae898)
- ブロック [`00bae878`](#insn-00bae878) 範囲 `[['00bae878', '00bae87f']]`
  - `CONDITIONAL_JUMP` [`00bae87c`](#insn-00bae87c) → [`00bae890`](#insn-00bae890)
  - `FALL_THROUGH` [`00bae87c`](#insn-00bae87c) → [`00bae880`](#insn-00bae880)
- ブロック [`00bae880`](#insn-00bae880) 範囲 `[['00bae880', '00bae887']]`
  - `CONDITIONAL_JUMP` [`00bae884`](#insn-00bae884) → [`00bae8c4`](#insn-00bae8c4)
  - `FALL_THROUGH` [`00bae884`](#insn-00bae884) → [`00bae888`](#insn-00bae888)
- ブロック [`00bae888`](#insn-00bae888) 範囲 `[['00bae888', '00bae88f']]`
  - `UNCONDITIONAL_JUMP` [`00bae88c`](#insn-00bae88c) → [`00bae82c`](#insn-00bae82c)
- ブロック [`00bae890`](#insn-00bae890) 範囲 `[['00bae890', '00bae893']]`
  - `CONDITIONAL_JUMP` [`00bae890`](#insn-00bae890) → [`00bae818`](#insn-00bae818)
  - `FALL_THROUGH` [`00bae890`](#insn-00bae890) → [`00bae894`](#insn-00bae894)
- ブロック [`00bae894`](#insn-00bae894) 範囲 `[['00bae894', '00bae897']]`
  - `FALL_THROUGH` [`00bae894`](#insn-00bae894) → [`00bae898`](#insn-00bae898)
- ブロック [`00bae898`](#insn-00bae898) 範囲 `[['00bae898', '00bae8af']]`
  - `CONDITIONAL_JUMP` [`00bae8ac`](#insn-00bae8ac) → [`00bae818`](#insn-00bae818)
  - `FALL_THROUGH` [`00bae8ac`](#insn-00bae8ac) → [`00bae8b0`](#insn-00bae8b0)
- ブロック [`00bae8b0`](#insn-00bae8b0) 範囲 `[['00bae8b0', '00bae8b3']]`
  - `CONDITIONAL_JUMP` [`00bae8b0`](#insn-00bae8b0) → [`00bae820`](#insn-00bae820)
  - `FALL_THROUGH` [`00bae8b0`](#insn-00bae8b0) → [`00bae8b4`](#insn-00bae8b4)
- ブロック [`00bae8b4`](#insn-00bae8b4) 範囲 `[['00bae8b4', '00bae8bb']]`
  - `UNCONDITIONAL_JUMP` [`00bae8b8`](#insn-00bae8b8) → [`00bae8cc`](#insn-00bae8cc)
- ブロック [`00bae8bc`](#insn-00bae8bc) 範囲 `[['00bae8bc', '00bae8c3']]`
  - `UNCONDITIONAL_JUMP` [`00bae8c0`](#insn-00bae8c0) → [`00bae8cc`](#insn-00bae8cc)
- ブロック [`00bae8c4`](#insn-00bae8c4) 範囲 `[['00bae8c4', '00bae8cb']]`
  - `FALL_THROUGH` [`00bae8c8`](#insn-00bae8c8) → [`00bae8cc`](#insn-00bae8cc)
- ブロック [`00bae8cc`](#insn-00bae8cc) 範囲 `[['00bae8cc', '00bae8eb']]`

## 命令位置別の参照

- [`00bae7cc`](#insn-00bae7cc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae7d0`](#insn-00bae7d0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae7d4`](#insn-00bae7d4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae7d8`](#insn-00bae7d8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae7dc`](#insn-00bae7dc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae7e0`](#insn-00bae7e0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae7f4`](#insn-00bae7f4) → [`00bae8bc`](#insn-00bae8bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae814`](#insn-00bae814) → [`00bae830`](#insn-00bae830) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae81c`](#insn-00bae81c) → [`00bae8b4`](#insn-00bae8b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae828`](#insn-00bae828) → [`00bae8b4`](#insn-00bae8b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae850`](#insn-00bae850) → [`00bae878`](#insn-00bae878) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae868`](#insn-00bae868) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bae86c`](#insn-00bae86c) → [`00bae878`](#insn-00bae878) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae870`](#insn-00bae870) → [`00bae880`](#insn-00bae880) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae874`](#insn-00bae874) → [`00bae898`](#insn-00bae898) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae87c`](#insn-00bae87c) → [`00bae890`](#insn-00bae890) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae884`](#insn-00bae884) → [`00bae8c4`](#insn-00bae8c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae88c`](#insn-00bae88c) → [`00bae82c`](#insn-00bae82c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae890`](#insn-00bae890) → [`00bae818`](#insn-00bae818) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae8a8`](#insn-00bae8a8) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bae8ac`](#insn-00bae8ac) → [`00bae818`](#insn-00bae818) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae8b0`](#insn-00bae8b0) → [`00bae820`](#insn-00bae820) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae8b8`](#insn-00bae8b8) → [`00bae8cc`](#insn-00bae8cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae8c0`](#insn-00bae8c0) → [`00bae8cc`](#insn-00bae8cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae8d0`](#insn-00bae8d0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae8d4`](#insn-00bae8d4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae8d8`](#insn-00bae8d8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae8dc`](#insn-00bae8dc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae8e0`](#insn-00bae8e0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bae7cc`](#insn-00bae7cc)

~~~json
{
  "source": "00bae7cc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae7d0`](#insn-00bae7d0)

~~~json
{
  "source": "00bae7d0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae7d4`](#insn-00bae7d4)

~~~json
{
  "source": "00bae7d4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae7d8`](#insn-00bae7d8)

~~~json
{
  "source": "00bae7d8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae7dc`](#insn-00bae7dc)

~~~json
{
  "source": "00bae7dc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae7e0`](#insn-00bae7e0)

~~~json
{
  "source": "00bae7e0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae7f4`](#insn-00bae7f4)

~~~json
{
  "source": "00bae7f4",
  "target": "00bae8bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae814`](#insn-00bae814)

~~~json
{
  "source": "00bae814",
  "target": "00bae830",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae81c`](#insn-00bae81c)

~~~json
{
  "source": "00bae81c",
  "target": "00bae8b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae828`](#insn-00bae828)

~~~json
{
  "source": "00bae828",
  "target": "00bae8b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae850`](#insn-00bae850)

~~~json
{
  "source": "00bae850",
  "target": "00bae878",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae868`](#insn-00bae868)

~~~json
{
  "source": "00bae868",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bae86c`](#insn-00bae86c)

~~~json
{
  "source": "00bae86c",
  "target": "00bae878",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae870`](#insn-00bae870)

~~~json
{
  "source": "00bae870",
  "target": "00bae880",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae874`](#insn-00bae874)

~~~json
{
  "source": "00bae874",
  "target": "00bae898",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae87c`](#insn-00bae87c)

~~~json
{
  "source": "00bae87c",
  "target": "00bae890",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae884`](#insn-00bae884)

~~~json
{
  "source": "00bae884",
  "target": "00bae8c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae88c`](#insn-00bae88c)

~~~json
{
  "source": "00bae88c",
  "target": "00bae82c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae890`](#insn-00bae890)

~~~json
{
  "source": "00bae890",
  "target": "00bae818",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae8a8`](#insn-00bae8a8)

~~~json
{
  "source": "00bae8a8",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bae8ac`](#insn-00bae8ac)

~~~json
{
  "source": "00bae8ac",
  "target": "00bae818",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae8b0`](#insn-00bae8b0)

~~~json
{
  "source": "00bae8b0",
  "target": "00bae820",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae8b8`](#insn-00bae8b8)

~~~json
{
  "source": "00bae8b8",
  "target": "00bae8cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae8c0`](#insn-00bae8c0)

~~~json
{
  "source": "00bae8c0",
  "target": "00bae8cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae8d0`](#insn-00bae8d0)

~~~json
{
  "source": "00bae8d0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae8d4`](#insn-00bae8d4)

~~~json
{
  "source": "00bae8d4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae8d8`](#insn-00bae8d8)

~~~json
{
  "source": "00bae8d8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae8dc`](#insn-00bae8dc)

~~~json
{
  "source": "00bae8dc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae8e0`](#insn-00bae8e0)

~~~json
{
  "source": "00bae8e0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
