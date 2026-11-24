# 00baffd0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b446a0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b446a0.md) · 移動量 `+0x6b930`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0063.md#compare-ea322c70d82dd8ff4dad63f75cbd7be1)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bb03f8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb03f8.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0038.md#compare-9bb325c974b6f82c47addc87be2a159f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baffd0",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3setIN11flatbuffers12IncludedFileENS_4lessISA_EENS5_ISA_EEEEEENS_19__map_value_compareIS7_SF_NSB_IS7_EELb1EEENS5_ISF_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISP_EERKT_",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e177df462aaaa8e3436bc480c522cd3534a7e6597ec5eefb8f5c01f4535be28a",
  "source_text_sha256": "e177df462aaaa8e3436bc480c522cd3534a7e6597ec5eefb8f5c01f4535be28a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baffd0",
        "00bb00ef"
      ]
    ],
    "bytes_sha256": "2908253fa9a5004c6c6ccb0082ff2a43fa4e5438f23783508c804947edb46b8f",
    "instruction_count": 72,
    "instruction_bytes": 288,
    "body_bytes": 288,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5ca50](../00c5c/00c5ca50.md)

## 呼び出し先

- [00c57c50](../00c57/00c57c50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2228 bytes

~~~c

long * _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3setIN11flatbuffers12IncludedFileENS_4lessISA_EENS5_ISA_EEEEEENS_19__map_value_compareIS7_SF_NSB_IS7_EELb1EEENS5_ISF_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISP_EERKT_
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
      if (iVar4 < 0) goto LAB_00bb0084;
LAB_00bb009c:
      if ((bVar3 & 1) == 0) {
        __s1_00 = (void *)((long)plVar7 + 0x21);
      }
      iVar4 = memcmp(__s1_00,__s1,__n);
      if (iVar4 == 0) goto LAB_00bb001c;
      if (-1 < iVar4) goto LAB_00bb00b8;
LAB_00bb0024:
      plVar5 = plVar7 + 1;
      plVar6 = (long *)*plVar5;
      if ((long *)*plVar5 == (long *)0x0) {
LAB_00bb00b8:
        *param_2 = plVar7;
        return plVar5;
      }
    }
    if (uVar1 <= uVar2) {
      if (__n != 0) {
        __s1_00 = (void *)plVar7[6];
        goto LAB_00bb009c;
      }
LAB_00bb001c:
      if (uVar2 <= uVar1) goto LAB_00bb00b8;
      goto LAB_00bb0024;
    }
LAB_00bb0084:
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
<a id="insn-00baffd0"></a> `00baffd0` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00baffd4"></a> `00baffd4` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baffd8"></a> `00baffd8` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baffdc"></a> `00baffdc` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baffe0"></a> `00baffe0` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00baffe4"></a> `00baffe4` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00baffe8"></a> `00baffe8` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00baffec"></a> `00baffec` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bafff0"></a> `00bafff0` | `97 8e 40 f8` | ldr x23,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00bafff4"></a> `00bafff4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bafff8"></a> `00bafff8` | `57 06 00 b4` | cbz x23,0x00bb00c0 | `CONDITIONAL_JUMP`
<a id="insn-00bafffc"></a> `00bafffc` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00bb0000"></a> `00bb0000` | `49 a8 40 a9` | ldp x9,x10,[x2, #0x8] | `FALL_THROUGH`
<a id="insn-00bb0004"></a> `00bb0004` | `14 20 00 91` | add x20,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bb0008"></a> `00bb0008` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb000c"></a> `00bb000c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb0010"></a> `00bb0010` | `78 01 89 9a` | csel x24,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00bb0014"></a> `00bb0014` | `55 15 82 9a` | csinc x21,x10,x2,ne | `FALL_THROUGH`
<a id="insn-00bb0018"></a> `00bb0018` | `07 00 00 14` | b 0x00bb0034 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb001c"></a> `00bb001c` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00bb0020"></a> `00bb0020` | `c2 04 00 54` | b.cs 0x00bb00b8 | `CONDITIONAL_JUMP`
<a id="insn-00bb0024"></a> `00bb0024` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00bb0028"></a> `00bb0028` | `88 8e 40 f8` | ldr x8,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00bb002c"></a> `00bb002c` | `68 04 00 b4` | cbz x8,0x00bb00b8 | `CONDITIONAL_JUMP`
<a id="insn-00bb0030"></a> `00bb0030` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00bb0034"></a> `00bb0034` | `fa 03 17 aa` | mov x26,x23 | `FALL_THROUGH`
<a id="insn-00bb0038"></a> `00bb0038` | `5b 0f 42 38` | ldrb w27,[x26, #0x20]! | `FALL_THROUGH`
<a id="insn-00bb003c"></a> `00bb003c` | `48 07 40 f9` | ldr x8,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00bb0040"></a> `00bb0040` | `69 ff 41 d3` | lsr x9,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00bb0044"></a> `00bb0044` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00bb0048"></a> `00bb0048` | `39 01 88 9a` | csel x25,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00bb004c"></a> `00bb004c` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00bb0050"></a> `00bb0050` | `36 33 98 9a` | csel x22,x25,x24,cc | `FALL_THROUGH`
<a id="insn-00bb0054"></a> `00bb0054` | `56 01 00 b4` | cbz x22,0x00bb007c | `CONDITIONAL_JUMP`
<a id="insn-00bb0058"></a> `00bb0058` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00bb005c"></a> `00bb005c` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00bb0060"></a> `00bb0060` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bb0064"></a> `00bb0064` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bb0068"></a> `00bb0068` | `81 17 9a 9a` | csinc x1,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00bb006c"></a> `00bb006c` | `f9 9e 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bb0070"></a> `00bb0070` | `60 00 00 34` | cbz w0,0x00bb007c | `CONDITIONAL_JUMP`
<a id="insn-00bb0074"></a> `00bb0074` | `80 00 f8 37` | tbnz w0,#0x1f,0x00bb0084 | `CONDITIONAL_JUMP`
<a id="insn-00bb0078"></a> `00bb0078` | `09 00 00 14` | b 0x00bb009c | `UNCONDITIONAL_JUMP`
<a id="insn-00bb007c"></a> `00bb007c` | `1f 03 19 eb` | cmp x24,x25 | `FALL_THROUGH`
<a id="insn-00bb0080"></a> `00bb0080` | `a2 00 00 54` | b.cs 0x00bb0094 | `CONDITIONAL_JUMP`
<a id="insn-00bb0084"></a> `00bb0084` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00bb0088"></a> `00bb0088` | `08 02 00 b4` | cbz x8,0x00bb00c8 | `CONDITIONAL_JUMP`
<a id="insn-00bb008c"></a> `00bb008c` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00bb0090"></a> `00bb0090` | `e8 ff ff 17` | b 0x00bb0030 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb0094"></a> `00bb0094` | `56 fc ff b4` | cbz x22,0x00bb001c | `CONDITIONAL_JUMP`
<a id="insn-00bb0098"></a> `00bb0098` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00bb009c"></a> `00bb009c` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00bb00a0"></a> `00bb00a0` | `80 17 9a 9a` | csinc x0,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00bb00a4"></a> `00bb00a4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bb00a8"></a> `00bb00a8` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bb00ac"></a> `00bb00ac` | `e9 9e 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bb00b0"></a> `00bb00b0` | `60 fb ff 34` | cbz w0,0x00bb001c | `CONDITIONAL_JUMP`
<a id="insn-00bb00b4"></a> `00bb00b4` | `80 fb ff 37` | tbnz w0,#0x1f,0x00bb0024 | `CONDITIONAL_JUMP`
<a id="insn-00bb00b8"></a> `00bb00b8` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00bb00bc"></a> `00bb00bc` | `05 00 00 14` | b 0x00bb00d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb00c0"></a> `00bb00c0` | `74 02 00 f9` | str x20,[x19] | `FALL_THROUGH`
<a id="insn-00bb00c4"></a> `00bb00c4` | `03 00 00 14` | b 0x00bb00d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb00c8"></a> `00bb00c8` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00bb00cc"></a> `00bb00cc` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00bb00d0"></a> `00bb00d0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bb00d4"></a> `00bb00d4` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bb00d8"></a> `00bb00d8` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bb00dc"></a> `00bb00dc` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bb00e0"></a> `00bb00e0` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb00e4"></a> `00bb00e4` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb00e8"></a> `00bb00e8` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00bb00ec"></a> `00bb00ec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baffd0`](#insn-00baffd0) 範囲 `[['00baffd0', '00bafffb']]`
  - `CONDITIONAL_JUMP` [`00bafff8`](#insn-00bafff8) → [`00bb00c0`](#insn-00bb00c0)
  - `FALL_THROUGH` [`00bafff8`](#insn-00bafff8) → [`00bafffc`](#insn-00bafffc)
- ブロック [`00bafffc`](#insn-00bafffc) 範囲 `[['00bafffc', '00bb001b']]`
  - `UNCONDITIONAL_JUMP` [`00bb0018`](#insn-00bb0018) → [`00bb0034`](#insn-00bb0034)
- ブロック [`00bb001c`](#insn-00bb001c) 範囲 `[['00bb001c', '00bb0023']]`
  - `CONDITIONAL_JUMP` [`00bb0020`](#insn-00bb0020) → [`00bb00b8`](#insn-00bb00b8)
  - `FALL_THROUGH` [`00bb0020`](#insn-00bb0020) → [`00bb0024`](#insn-00bb0024)
- ブロック [`00bb0024`](#insn-00bb0024) 範囲 `[['00bb0024', '00bb002f']]`
  - `CONDITIONAL_JUMP` [`00bb002c`](#insn-00bb002c) → [`00bb00b8`](#insn-00bb00b8)
  - `FALL_THROUGH` [`00bb002c`](#insn-00bb002c) → [`00bb0030`](#insn-00bb0030)
- ブロック [`00bb0030`](#insn-00bb0030) 範囲 `[['00bb0030', '00bb0033']]`
  - `FALL_THROUGH` [`00bb0030`](#insn-00bb0030) → [`00bb0034`](#insn-00bb0034)
- ブロック [`00bb0034`](#insn-00bb0034) 範囲 `[['00bb0034', '00bb0057']]`
  - `CONDITIONAL_JUMP` [`00bb0054`](#insn-00bb0054) → [`00bb007c`](#insn-00bb007c)
  - `FALL_THROUGH` [`00bb0054`](#insn-00bb0054) → [`00bb0058`](#insn-00bb0058)
- ブロック [`00bb0058`](#insn-00bb0058) 範囲 `[['00bb0058', '00bb0073']]`
  - `CONDITIONAL_JUMP` [`00bb0070`](#insn-00bb0070) → [`00bb007c`](#insn-00bb007c)
  - `FALL_THROUGH` [`00bb0070`](#insn-00bb0070) → [`00bb0074`](#insn-00bb0074)
- ブロック [`00bb0074`](#insn-00bb0074) 範囲 `[['00bb0074', '00bb0077']]`
  - `CONDITIONAL_JUMP` [`00bb0074`](#insn-00bb0074) → [`00bb0084`](#insn-00bb0084)
  - `FALL_THROUGH` [`00bb0074`](#insn-00bb0074) → [`00bb0078`](#insn-00bb0078)
- ブロック [`00bb0078`](#insn-00bb0078) 範囲 `[['00bb0078', '00bb007b']]`
  - `UNCONDITIONAL_JUMP` [`00bb0078`](#insn-00bb0078) → [`00bb009c`](#insn-00bb009c)
- ブロック [`00bb007c`](#insn-00bb007c) 範囲 `[['00bb007c', '00bb0083']]`
  - `CONDITIONAL_JUMP` [`00bb0080`](#insn-00bb0080) → [`00bb0094`](#insn-00bb0094)
  - `FALL_THROUGH` [`00bb0080`](#insn-00bb0080) → [`00bb0084`](#insn-00bb0084)
- ブロック [`00bb0084`](#insn-00bb0084) 範囲 `[['00bb0084', '00bb008b']]`
  - `CONDITIONAL_JUMP` [`00bb0088`](#insn-00bb0088) → [`00bb00c8`](#insn-00bb00c8)
  - `FALL_THROUGH` [`00bb0088`](#insn-00bb0088) → [`00bb008c`](#insn-00bb008c)
- ブロック [`00bb008c`](#insn-00bb008c) 範囲 `[['00bb008c', '00bb0093']]`
  - `UNCONDITIONAL_JUMP` [`00bb0090`](#insn-00bb0090) → [`00bb0030`](#insn-00bb0030)
- ブロック [`00bb0094`](#insn-00bb0094) 範囲 `[['00bb0094', '00bb0097']]`
  - `CONDITIONAL_JUMP` [`00bb0094`](#insn-00bb0094) → [`00bb001c`](#insn-00bb001c)
  - `FALL_THROUGH` [`00bb0094`](#insn-00bb0094) → [`00bb0098`](#insn-00bb0098)
- ブロック [`00bb0098`](#insn-00bb0098) 範囲 `[['00bb0098', '00bb009b']]`
  - `FALL_THROUGH` [`00bb0098`](#insn-00bb0098) → [`00bb009c`](#insn-00bb009c)
- ブロック [`00bb009c`](#insn-00bb009c) 範囲 `[['00bb009c', '00bb00b3']]`
  - `CONDITIONAL_JUMP` [`00bb00b0`](#insn-00bb00b0) → [`00bb001c`](#insn-00bb001c)
  - `FALL_THROUGH` [`00bb00b0`](#insn-00bb00b0) → [`00bb00b4`](#insn-00bb00b4)
- ブロック [`00bb00b4`](#insn-00bb00b4) 範囲 `[['00bb00b4', '00bb00b7']]`
  - `CONDITIONAL_JUMP` [`00bb00b4`](#insn-00bb00b4) → [`00bb0024`](#insn-00bb0024)
  - `FALL_THROUGH` [`00bb00b4`](#insn-00bb00b4) → [`00bb00b8`](#insn-00bb00b8)
- ブロック [`00bb00b8`](#insn-00bb00b8) 範囲 `[['00bb00b8', '00bb00bf']]`
  - `UNCONDITIONAL_JUMP` [`00bb00bc`](#insn-00bb00bc) → [`00bb00d0`](#insn-00bb00d0)
- ブロック [`00bb00c0`](#insn-00bb00c0) 範囲 `[['00bb00c0', '00bb00c7']]`
  - `UNCONDITIONAL_JUMP` [`00bb00c4`](#insn-00bb00c4) → [`00bb00d0`](#insn-00bb00d0)
- ブロック [`00bb00c8`](#insn-00bb00c8) 範囲 `[['00bb00c8', '00bb00cf']]`
  - `FALL_THROUGH` [`00bb00cc`](#insn-00bb00cc) → [`00bb00d0`](#insn-00bb00d0)
- ブロック [`00bb00d0`](#insn-00bb00d0) 範囲 `[['00bb00d0', '00bb00ef']]`

## 命令位置別の参照

- [`00baffd0`](#insn-00baffd0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffd4`](#insn-00baffd4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffd8`](#insn-00baffd8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffdc`](#insn-00baffdc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffe0`](#insn-00baffe0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baffe4`](#insn-00baffe4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafff8`](#insn-00bafff8) → [`00bb00c0`](#insn-00bb00c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0018`](#insn-00bb0018) → [`00bb0034`](#insn-00bb0034) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0020`](#insn-00bb0020) → [`00bb00b8`](#insn-00bb00b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb002c`](#insn-00bb002c) → [`00bb00b8`](#insn-00bb00b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0054`](#insn-00bb0054) → [`00bb007c`](#insn-00bb007c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb006c`](#insn-00bb006c) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bb0070`](#insn-00bb0070) → [`00bb007c`](#insn-00bb007c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0074`](#insn-00bb0074) → [`00bb0084`](#insn-00bb0084) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0078`](#insn-00bb0078) → [`00bb009c`](#insn-00bb009c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0080`](#insn-00bb0080) → [`00bb0094`](#insn-00bb0094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0088`](#insn-00bb0088) → [`00bb00c8`](#insn-00bb00c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0090`](#insn-00bb0090) → [`00bb0030`](#insn-00bb0030) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0094`](#insn-00bb0094) → [`00bb001c`](#insn-00bb001c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb00ac`](#insn-00bb00ac) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bb00b0`](#insn-00bb00b0) → [`00bb001c`](#insn-00bb001c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb00b4`](#insn-00bb00b4) → [`00bb0024`](#insn-00bb0024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb00bc`](#insn-00bb00bc) → [`00bb00d0`](#insn-00bb00d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb00c4`](#insn-00bb00c4) → [`00bb00d0`](#insn-00bb00d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb00d4`](#insn-00bb00d4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb00d8`](#insn-00bb00d8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb00dc`](#insn-00bb00dc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb00e0`](#insn-00bb00e0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb00e4`](#insn-00bb00e4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baffd0`](#insn-00baffd0)

~~~json
{
  "source": "00baffd0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baffd4`](#insn-00baffd4)

~~~json
{
  "source": "00baffd4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baffd8`](#insn-00baffd8)

~~~json
{
  "source": "00baffd8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baffdc`](#insn-00baffdc)

~~~json
{
  "source": "00baffdc",
  "target": "Stack[-0x30]",
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
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafff8`](#insn-00bafff8)

~~~json
{
  "source": "00bafff8",
  "target": "00bb00c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0018`](#insn-00bb0018)

~~~json
{
  "source": "00bb0018",
  "target": "00bb0034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0020`](#insn-00bb0020)

~~~json
{
  "source": "00bb0020",
  "target": "00bb00b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb002c`](#insn-00bb002c)

~~~json
{
  "source": "00bb002c",
  "target": "00bb00b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0054`](#insn-00bb0054)

~~~json
{
  "source": "00bb0054",
  "target": "00bb007c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb006c`](#insn-00bb006c)

~~~json
{
  "source": "00bb006c",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb0070`](#insn-00bb0070)

~~~json
{
  "source": "00bb0070",
  "target": "00bb007c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0074`](#insn-00bb0074)

~~~json
{
  "source": "00bb0074",
  "target": "00bb0084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0078`](#insn-00bb0078)

~~~json
{
  "source": "00bb0078",
  "target": "00bb009c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0080`](#insn-00bb0080)

~~~json
{
  "source": "00bb0080",
  "target": "00bb0094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0088`](#insn-00bb0088)

~~~json
{
  "source": "00bb0088",
  "target": "00bb00c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0090`](#insn-00bb0090)

~~~json
{
  "source": "00bb0090",
  "target": "00bb0030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0094`](#insn-00bb0094)

~~~json
{
  "source": "00bb0094",
  "target": "00bb001c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb00ac`](#insn-00bb00ac)

~~~json
{
  "source": "00bb00ac",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb00b0`](#insn-00bb00b0)

~~~json
{
  "source": "00bb00b0",
  "target": "00bb001c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb00b4`](#insn-00bb00b4)

~~~json
{
  "source": "00bb00b4",
  "target": "00bb0024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb00bc`](#insn-00bb00bc)

~~~json
{
  "source": "00bb00bc",
  "target": "00bb00d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb00c4`](#insn-00bb00c4)

~~~json
{
  "source": "00bb00c4",
  "target": "00bb00d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb00d4`](#insn-00bb00d4)

~~~json
{
  "source": "00bb00d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb00d8`](#insn-00bb00d8)

~~~json
{
  "source": "00bb00d8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb00dc`](#insn-00bb00dc)

~~~json
{
  "source": "00bb00dc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb00e0`](#insn-00bb00e0)

~~~json
{
  "source": "00bb00e0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb00e4`](#insn-00bb00e4)

~~~json
{
  "source": "00bb00e4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
