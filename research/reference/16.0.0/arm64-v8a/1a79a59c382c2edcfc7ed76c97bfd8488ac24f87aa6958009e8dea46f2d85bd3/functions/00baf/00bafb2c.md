# 00bafb2c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b441ec`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b441ec.md) · 移動量 `+0x6b940`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0063.md#compare-273fe9962c72f8a55e757da71d1b11e7)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00baff54`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00baff54.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0078.md#compare-69530ba7481a623e8e53b6b83b447453)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bafb2c",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "87a877aaaaa4fd0849d3b6a73fa389d61cc0e7db627cbe688a2c58308f25ccac",
  "source_text_sha256": "87a877aaaaa4fd0849d3b6a73fa389d61cc0e7db627cbe688a2c58308f25ccac",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bafb2c",
        "00bafc4b"
      ]
    ],
    "bytes_sha256": "ff93e0a0734f57f28091232b4f9fb8a0045056572abc8944fe7819108d9d342f",
    "instruction_count": 72,
    "instruction_bytes": 288,
    "body_bytes": 288,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5cac0](../00c5c/00c5cac0.md)

## 呼び出し先

- [00c57c50](../00c57/00c57c50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2193 bytes

~~~c

long * _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_
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
      if (iVar4 < 0) goto LAB_00bafbe0;
LAB_00bafbf8:
      if ((bVar3 & 1) == 0) {
        __s1_00 = (void *)((long)plVar7 + 0x21);
      }
      iVar4 = memcmp(__s1_00,__s1,__n);
      if (iVar4 == 0) goto LAB_00bafb78;
      if (-1 < iVar4) goto LAB_00bafc14;
LAB_00bafb80:
      plVar5 = plVar7 + 1;
      plVar6 = (long *)*plVar5;
      if ((long *)*plVar5 == (long *)0x0) {
LAB_00bafc14:
        *param_2 = plVar7;
        return plVar5;
      }
    }
    if (uVar1 <= uVar2) {
      if (__n != 0) {
        __s1_00 = (void *)plVar7[6];
        goto LAB_00bafbf8;
      }
LAB_00bafb78:
      if (uVar2 <= uVar1) goto LAB_00bafc14;
      goto LAB_00bafb80;
    }
LAB_00bafbe0:
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
<a id="insn-00bafb2c"></a> `00bafb2c` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00bafb30"></a> `00bafb30` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bafb34"></a> `00bafb34` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bafb38"></a> `00bafb38` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bafb3c"></a> `00bafb3c` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bafb40"></a> `00bafb40` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bafb44"></a> `00bafb44` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bafb48"></a> `00bafb48` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bafb4c"></a> `00bafb4c` | `97 8e 40 f8` | ldr x23,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00bafb50"></a> `00bafb50` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bafb54"></a> `00bafb54` | `57 06 00 b4` | cbz x23,0x00bafc1c | `CONDITIONAL_JUMP`
<a id="insn-00bafb58"></a> `00bafb58` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00bafb5c"></a> `00bafb5c` | `49 a8 40 a9` | ldp x9,x10,[x2, #0x8] | `FALL_THROUGH`
<a id="insn-00bafb60"></a> `00bafb60` | `14 20 00 91` | add x20,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bafb64"></a> `00bafb64` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bafb68"></a> `00bafb68` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bafb6c"></a> `00bafb6c` | `78 01 89 9a` | csel x24,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00bafb70"></a> `00bafb70` | `55 15 82 9a` | csinc x21,x10,x2,ne | `FALL_THROUGH`
<a id="insn-00bafb74"></a> `00bafb74` | `07 00 00 14` | b 0x00bafb90 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafb78"></a> `00bafb78` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00bafb7c"></a> `00bafb7c` | `c2 04 00 54` | b.cs 0x00bafc14 | `CONDITIONAL_JUMP`
<a id="insn-00bafb80"></a> `00bafb80` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00bafb84"></a> `00bafb84` | `88 8e 40 f8` | ldr x8,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00bafb88"></a> `00bafb88` | `68 04 00 b4` | cbz x8,0x00bafc14 | `CONDITIONAL_JUMP`
<a id="insn-00bafb8c"></a> `00bafb8c` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00bafb90"></a> `00bafb90` | `fa 03 17 aa` | mov x26,x23 | `FALL_THROUGH`
<a id="insn-00bafb94"></a> `00bafb94` | `5b 0f 42 38` | ldrb w27,[x26, #0x20]! | `FALL_THROUGH`
<a id="insn-00bafb98"></a> `00bafb98` | `48 07 40 f9` | ldr x8,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00bafb9c"></a> `00bafb9c` | `69 ff 41 d3` | lsr x9,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00bafba0"></a> `00bafba0` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00bafba4"></a> `00bafba4` | `39 01 88 9a` | csel x25,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00bafba8"></a> `00bafba8` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00bafbac"></a> `00bafbac` | `36 33 98 9a` | csel x22,x25,x24,cc | `FALL_THROUGH`
<a id="insn-00bafbb0"></a> `00bafbb0` | `56 01 00 b4` | cbz x22,0x00bafbd8 | `CONDITIONAL_JUMP`
<a id="insn-00bafbb4"></a> `00bafbb4` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00bafbb8"></a> `00bafbb8` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00bafbbc"></a> `00bafbbc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bafbc0"></a> `00bafbc0` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bafbc4"></a> `00bafbc4` | `81 17 9a 9a` | csinc x1,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00bafbc8"></a> `00bafbc8` | `22 a0 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bafbcc"></a> `00bafbcc` | `60 00 00 34` | cbz w0,0x00bafbd8 | `CONDITIONAL_JUMP`
<a id="insn-00bafbd0"></a> `00bafbd0` | `80 00 f8 37` | tbnz w0,#0x1f,0x00bafbe0 | `CONDITIONAL_JUMP`
<a id="insn-00bafbd4"></a> `00bafbd4` | `09 00 00 14` | b 0x00bafbf8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafbd8"></a> `00bafbd8` | `1f 03 19 eb` | cmp x24,x25 | `FALL_THROUGH`
<a id="insn-00bafbdc"></a> `00bafbdc` | `a2 00 00 54` | b.cs 0x00bafbf0 | `CONDITIONAL_JUMP`
<a id="insn-00bafbe0"></a> `00bafbe0` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00bafbe4"></a> `00bafbe4` | `08 02 00 b4` | cbz x8,0x00bafc24 | `CONDITIONAL_JUMP`
<a id="insn-00bafbe8"></a> `00bafbe8` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00bafbec"></a> `00bafbec` | `e8 ff ff 17` | b 0x00bafb8c | `UNCONDITIONAL_JUMP`
<a id="insn-00bafbf0"></a> `00bafbf0` | `56 fc ff b4` | cbz x22,0x00bafb78 | `CONDITIONAL_JUMP`
<a id="insn-00bafbf4"></a> `00bafbf4` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00bafbf8"></a> `00bafbf8` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00bafbfc"></a> `00bafbfc` | `80 17 9a 9a` | csinc x0,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00bafc00"></a> `00bafc00` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bafc04"></a> `00bafc04` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bafc08"></a> `00bafc08` | `12 a0 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bafc0c"></a> `00bafc0c` | `60 fb ff 34` | cbz w0,0x00bafb78 | `CONDITIONAL_JUMP`
<a id="insn-00bafc10"></a> `00bafc10` | `80 fb ff 37` | tbnz w0,#0x1f,0x00bafb80 | `CONDITIONAL_JUMP`
<a id="insn-00bafc14"></a> `00bafc14` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00bafc18"></a> `00bafc18` | `05 00 00 14` | b 0x00bafc2c | `UNCONDITIONAL_JUMP`
<a id="insn-00bafc1c"></a> `00bafc1c` | `74 02 00 f9` | str x20,[x19] | `FALL_THROUGH`
<a id="insn-00bafc20"></a> `00bafc20` | `03 00 00 14` | b 0x00bafc2c | `UNCONDITIONAL_JUMP`
<a id="insn-00bafc24"></a> `00bafc24` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00bafc28"></a> `00bafc28` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00bafc2c"></a> `00bafc2c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bafc30"></a> `00bafc30` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bafc34"></a> `00bafc34` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bafc38"></a> `00bafc38` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bafc3c"></a> `00bafc3c` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bafc40"></a> `00bafc40` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bafc44"></a> `00bafc44` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00bafc48"></a> `00bafc48` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bafb2c`](#insn-00bafb2c) 範囲 `[['00bafb2c', '00bafb57']]`
  - `CONDITIONAL_JUMP` [`00bafb54`](#insn-00bafb54) → [`00bafc1c`](#insn-00bafc1c)
  - `FALL_THROUGH` [`00bafb54`](#insn-00bafb54) → [`00bafb58`](#insn-00bafb58)
- ブロック [`00bafb58`](#insn-00bafb58) 範囲 `[['00bafb58', '00bafb77']]`
  - `UNCONDITIONAL_JUMP` [`00bafb74`](#insn-00bafb74) → [`00bafb90`](#insn-00bafb90)
- ブロック [`00bafb78`](#insn-00bafb78) 範囲 `[['00bafb78', '00bafb7f']]`
  - `CONDITIONAL_JUMP` [`00bafb7c`](#insn-00bafb7c) → [`00bafc14`](#insn-00bafc14)
  - `FALL_THROUGH` [`00bafb7c`](#insn-00bafb7c) → [`00bafb80`](#insn-00bafb80)
- ブロック [`00bafb80`](#insn-00bafb80) 範囲 `[['00bafb80', '00bafb8b']]`
  - `CONDITIONAL_JUMP` [`00bafb88`](#insn-00bafb88) → [`00bafc14`](#insn-00bafc14)
  - `FALL_THROUGH` [`00bafb88`](#insn-00bafb88) → [`00bafb8c`](#insn-00bafb8c)
- ブロック [`00bafb8c`](#insn-00bafb8c) 範囲 `[['00bafb8c', '00bafb8f']]`
  - `FALL_THROUGH` [`00bafb8c`](#insn-00bafb8c) → [`00bafb90`](#insn-00bafb90)
- ブロック [`00bafb90`](#insn-00bafb90) 範囲 `[['00bafb90', '00bafbb3']]`
  - `CONDITIONAL_JUMP` [`00bafbb0`](#insn-00bafbb0) → [`00bafbd8`](#insn-00bafbd8)
  - `FALL_THROUGH` [`00bafbb0`](#insn-00bafbb0) → [`00bafbb4`](#insn-00bafbb4)
- ブロック [`00bafbb4`](#insn-00bafbb4) 範囲 `[['00bafbb4', '00bafbcf']]`
  - `CONDITIONAL_JUMP` [`00bafbcc`](#insn-00bafbcc) → [`00bafbd8`](#insn-00bafbd8)
  - `FALL_THROUGH` [`00bafbcc`](#insn-00bafbcc) → [`00bafbd0`](#insn-00bafbd0)
- ブロック [`00bafbd0`](#insn-00bafbd0) 範囲 `[['00bafbd0', '00bafbd3']]`
  - `CONDITIONAL_JUMP` [`00bafbd0`](#insn-00bafbd0) → [`00bafbe0`](#insn-00bafbe0)
  - `FALL_THROUGH` [`00bafbd0`](#insn-00bafbd0) → [`00bafbd4`](#insn-00bafbd4)
- ブロック [`00bafbd4`](#insn-00bafbd4) 範囲 `[['00bafbd4', '00bafbd7']]`
  - `UNCONDITIONAL_JUMP` [`00bafbd4`](#insn-00bafbd4) → [`00bafbf8`](#insn-00bafbf8)
- ブロック [`00bafbd8`](#insn-00bafbd8) 範囲 `[['00bafbd8', '00bafbdf']]`
  - `CONDITIONAL_JUMP` [`00bafbdc`](#insn-00bafbdc) → [`00bafbf0`](#insn-00bafbf0)
  - `FALL_THROUGH` [`00bafbdc`](#insn-00bafbdc) → [`00bafbe0`](#insn-00bafbe0)
- ブロック [`00bafbe0`](#insn-00bafbe0) 範囲 `[['00bafbe0', '00bafbe7']]`
  - `CONDITIONAL_JUMP` [`00bafbe4`](#insn-00bafbe4) → [`00bafc24`](#insn-00bafc24)
  - `FALL_THROUGH` [`00bafbe4`](#insn-00bafbe4) → [`00bafbe8`](#insn-00bafbe8)
- ブロック [`00bafbe8`](#insn-00bafbe8) 範囲 `[['00bafbe8', '00bafbef']]`
  - `UNCONDITIONAL_JUMP` [`00bafbec`](#insn-00bafbec) → [`00bafb8c`](#insn-00bafb8c)
- ブロック [`00bafbf0`](#insn-00bafbf0) 範囲 `[['00bafbf0', '00bafbf3']]`
  - `CONDITIONAL_JUMP` [`00bafbf0`](#insn-00bafbf0) → [`00bafb78`](#insn-00bafb78)
  - `FALL_THROUGH` [`00bafbf0`](#insn-00bafbf0) → [`00bafbf4`](#insn-00bafbf4)
- ブロック [`00bafbf4`](#insn-00bafbf4) 範囲 `[['00bafbf4', '00bafbf7']]`
  - `FALL_THROUGH` [`00bafbf4`](#insn-00bafbf4) → [`00bafbf8`](#insn-00bafbf8)
- ブロック [`00bafbf8`](#insn-00bafbf8) 範囲 `[['00bafbf8', '00bafc0f']]`
  - `CONDITIONAL_JUMP` [`00bafc0c`](#insn-00bafc0c) → [`00bafb78`](#insn-00bafb78)
  - `FALL_THROUGH` [`00bafc0c`](#insn-00bafc0c) → [`00bafc10`](#insn-00bafc10)
- ブロック [`00bafc10`](#insn-00bafc10) 範囲 `[['00bafc10', '00bafc13']]`
  - `CONDITIONAL_JUMP` [`00bafc10`](#insn-00bafc10) → [`00bafb80`](#insn-00bafb80)
  - `FALL_THROUGH` [`00bafc10`](#insn-00bafc10) → [`00bafc14`](#insn-00bafc14)
- ブロック [`00bafc14`](#insn-00bafc14) 範囲 `[['00bafc14', '00bafc1b']]`
  - `UNCONDITIONAL_JUMP` [`00bafc18`](#insn-00bafc18) → [`00bafc2c`](#insn-00bafc2c)
- ブロック [`00bafc1c`](#insn-00bafc1c) 範囲 `[['00bafc1c', '00bafc23']]`
  - `UNCONDITIONAL_JUMP` [`00bafc20`](#insn-00bafc20) → [`00bafc2c`](#insn-00bafc2c)
- ブロック [`00bafc24`](#insn-00bafc24) 範囲 `[['00bafc24', '00bafc2b']]`
  - `FALL_THROUGH` [`00bafc28`](#insn-00bafc28) → [`00bafc2c`](#insn-00bafc2c)
- ブロック [`00bafc2c`](#insn-00bafc2c) 範囲 `[['00bafc2c', '00bafc4b']]`

## 命令位置別の参照

- [`00bafb2c`](#insn-00bafb2c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafb30`](#insn-00bafb30) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafb34`](#insn-00bafb34) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafb38`](#insn-00bafb38) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafb3c`](#insn-00bafb3c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafb40`](#insn-00bafb40) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafb54`](#insn-00bafb54) → [`00bafc1c`](#insn-00bafc1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafb74`](#insn-00bafb74) → [`00bafb90`](#insn-00bafb90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafb7c`](#insn-00bafb7c) → [`00bafc14`](#insn-00bafc14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafb88`](#insn-00bafb88) → [`00bafc14`](#insn-00bafc14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafbb0`](#insn-00bafbb0) → [`00bafbd8`](#insn-00bafbd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafbc8`](#insn-00bafbc8) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bafbcc`](#insn-00bafbcc) → [`00bafbd8`](#insn-00bafbd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafbd0`](#insn-00bafbd0) → [`00bafbe0`](#insn-00bafbe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafbd4`](#insn-00bafbd4) → [`00bafbf8`](#insn-00bafbf8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafbdc`](#insn-00bafbdc) → [`00bafbf0`](#insn-00bafbf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafbe4`](#insn-00bafbe4) → [`00bafc24`](#insn-00bafc24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafbec`](#insn-00bafbec) → [`00bafb8c`](#insn-00bafb8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafbf0`](#insn-00bafbf0) → [`00bafb78`](#insn-00bafb78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc08`](#insn-00bafc08) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bafc0c`](#insn-00bafc0c) → [`00bafb78`](#insn-00bafb78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc10`](#insn-00bafc10) → [`00bafb80`](#insn-00bafb80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc18`](#insn-00bafc18) → [`00bafc2c`](#insn-00bafc2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc20`](#insn-00bafc20) → [`00bafc2c`](#insn-00bafc2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc30`](#insn-00bafc30) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc34`](#insn-00bafc34) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc38`](#insn-00bafc38) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc3c`](#insn-00bafc3c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc40`](#insn-00bafc40) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bafb2c`](#insn-00bafb2c)

~~~json
{
  "source": "00bafb2c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafb30`](#insn-00bafb30)

~~~json
{
  "source": "00bafb30",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafb34`](#insn-00bafb34)

~~~json
{
  "source": "00bafb34",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafb38`](#insn-00bafb38)

~~~json
{
  "source": "00bafb38",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafb3c`](#insn-00bafb3c)

~~~json
{
  "source": "00bafb3c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafb40`](#insn-00bafb40)

~~~json
{
  "source": "00bafb40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafb54`](#insn-00bafb54)

~~~json
{
  "source": "00bafb54",
  "target": "00bafc1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafb74`](#insn-00bafb74)

~~~json
{
  "source": "00bafb74",
  "target": "00bafb90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafb7c`](#insn-00bafb7c)

~~~json
{
  "source": "00bafb7c",
  "target": "00bafc14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafb88`](#insn-00bafb88)

~~~json
{
  "source": "00bafb88",
  "target": "00bafc14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafbb0`](#insn-00bafbb0)

~~~json
{
  "source": "00bafbb0",
  "target": "00bafbd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafbc8`](#insn-00bafbc8)

~~~json
{
  "source": "00bafbc8",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafbcc`](#insn-00bafbcc)

~~~json
{
  "source": "00bafbcc",
  "target": "00bafbd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafbd0`](#insn-00bafbd0)

~~~json
{
  "source": "00bafbd0",
  "target": "00bafbe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafbd4`](#insn-00bafbd4)

~~~json
{
  "source": "00bafbd4",
  "target": "00bafbf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafbdc`](#insn-00bafbdc)

~~~json
{
  "source": "00bafbdc",
  "target": "00bafbf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafbe4`](#insn-00bafbe4)

~~~json
{
  "source": "00bafbe4",
  "target": "00bafc24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafbec`](#insn-00bafbec)

~~~json
{
  "source": "00bafbec",
  "target": "00bafb8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafbf0`](#insn-00bafbf0)

~~~json
{
  "source": "00bafbf0",
  "target": "00bafb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc08`](#insn-00bafc08)

~~~json
{
  "source": "00bafc08",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafc0c`](#insn-00bafc0c)

~~~json
{
  "source": "00bafc0c",
  "target": "00bafb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc10`](#insn-00bafc10)

~~~json
{
  "source": "00bafc10",
  "target": "00bafb80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc18`](#insn-00bafc18)

~~~json
{
  "source": "00bafc18",
  "target": "00bafc2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc20`](#insn-00bafc20)

~~~json
{
  "source": "00bafc20",
  "target": "00bafc2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc30`](#insn-00bafc30)

~~~json
{
  "source": "00bafc30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc34`](#insn-00bafc34)

~~~json
{
  "source": "00bafc34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc38`](#insn-00bafc38)

~~~json
{
  "source": "00bafc38",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc3c`](#insn-00bafc3c)

~~~json
{
  "source": "00bafc3c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc40`](#insn-00bafc40)

~~~json
{
  "source": "00bafc40",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
