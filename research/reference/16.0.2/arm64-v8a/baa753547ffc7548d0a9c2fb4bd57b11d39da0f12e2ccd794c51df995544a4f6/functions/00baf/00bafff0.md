# 00bafff0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00baff54`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00baff54.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0078.md#compare-1ff1aa8f2d5c0764ae45709c7967ad21)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bb0fe4`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0fe4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-82709b8ecf6b160daf97d786fda37761)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bafff0",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fad5501724178bc0c309a5f5f4e65268501d570ff1d1aea09b2377ff1c246b74",
  "source_text_sha256": "fad5501724178bc0c309a5f5f4e65268501d570ff1d1aea09b2377ff1c246b74",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bafff0",
        "00bb010f"
      ]
    ],
    "bytes_sha256": "e9e354792f94898a8a8dcf5fa413ffe2a05f221616a3c01215405c4da6ccd9e8",
    "instruction_count": 72,
    "instruction_bytes": 288,
    "body_bytes": 288,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5cf90](../00c5c/00c5cf90.md)

## 呼び出し先

- [00c58120](../00c58/00c58120.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2906 bytes

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
                    /* try { // try from 00bb0060 to 00cb007b has its CatchHandler @ 00bb0098 */
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
                    /* catch() { ... } // from try @ 00baff80 with catch @ 00bb007c
                       try { // try from 00bb007c to 00cb00d3 has its CatchHandler @ 00bafaa4 */
      __s2 = __s1_00;
                    /* catch() { ... } // from try @ 00bafb50 with catch @ 00bb0080 */
      if ((bVar3 & 1) == 0) {
        __s2 = (void *)((long)plVar7 + 0x21);
      }
      iVar4 = memcmp(__s1,__s2,__n);
      if (iVar4 == 0) break;
      if (iVar4 < 0) goto LAB_00bb00a4;
LAB_00bb00bc:
      if ((bVar3 & 1) == 0) {
        __s1_00 = (void *)((long)plVar7 + 0x21);
      }
      iVar4 = memcmp(__s1_00,__s1,__n);
      if (iVar4 == 0) goto LAB_00bb003c;
      if (-1 < iVar4) goto LAB_00bb00d8;
LAB_00bb0044:
      plVar5 = plVar7 + 1;
      plVar6 = (long *)*plVar5;
      if ((long *)*plVar5 == (long *)0x0) {
LAB_00bb00d8:
        *param_2 = plVar7;
        return plVar5;
      }
    }
                    /* catch() { ... } // from try @ 00bafbc0 with catch @ 00bb009c */
                    /* catch() { ... } // from try @ 00bafbb4 with catch @ 00bb00a0 */
    if (uVar1 <= uVar2) {
      if (__n != 0) {
        __s1_00 = (void *)plVar7[6];
        goto LAB_00bb00bc;
      }
LAB_00bb003c:
      if (uVar2 <= uVar1) goto LAB_00bb00d8;
      goto LAB_00bb0044;
    }
LAB_00bb00a4:
                    /* catch() { ... } // from try @ 00bafba8 with catch @ 00bb00a4 */
                    /* catch() { ... } // from try @ 00bafbd0 with catch @ 00bb00a8 */
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
<a id="insn-00bafff0"></a> `00bafff0` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00bafff4"></a> `00bafff4` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bafff8"></a> `00bafff8` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bafffc"></a> `00bafffc` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bb0000"></a> `00bb0000` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bb0004"></a> `00bb0004` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bb0008"></a> `00bb0008` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bb000c"></a> `00bb000c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bb0010"></a> `00bb0010` | `97 8e 40 f8` | ldr x23,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00bb0014"></a> `00bb0014` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bb0018"></a> `00bb0018` | `57 06 00 b4` | cbz x23,0x00bb00e0 | `CONDITIONAL_JUMP`
<a id="insn-00bb001c"></a> `00bb001c` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00bb0020"></a> `00bb0020` | `49 a8 40 a9` | ldp x9,x10,[x2, #0x8] | `FALL_THROUGH`
<a id="insn-00bb0024"></a> `00bb0024` | `14 20 00 91` | add x20,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bb0028"></a> `00bb0028` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb002c"></a> `00bb002c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb0030"></a> `00bb0030` | `78 01 89 9a` | csel x24,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00bb0034"></a> `00bb0034` | `55 15 82 9a` | csinc x21,x10,x2,ne | `FALL_THROUGH`
<a id="insn-00bb0038"></a> `00bb0038` | `07 00 00 14` | b 0x00bb0054 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb003c"></a> `00bb003c` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00bb0040"></a> `00bb0040` | `c2 04 00 54` | b.cs 0x00bb00d8 | `CONDITIONAL_JUMP`
<a id="insn-00bb0044"></a> `00bb0044` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00bb0048"></a> `00bb0048` | `88 8e 40 f8` | ldr x8,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00bb004c"></a> `00bb004c` | `68 04 00 b4` | cbz x8,0x00bb00d8 | `CONDITIONAL_JUMP`
<a id="insn-00bb0050"></a> `00bb0050` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00bb0054"></a> `00bb0054` | `fa 03 17 aa` | mov x26,x23 | `FALL_THROUGH`
<a id="insn-00bb0058"></a> `00bb0058` | `5b 0f 42 38` | ldrb w27,[x26, #0x20]! | `FALL_THROUGH`
<a id="insn-00bb005c"></a> `00bb005c` | `48 07 40 f9` | ldr x8,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00bb0060"></a> `00bb0060` | `69 ff 41 d3` | lsr x9,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00bb0064"></a> `00bb0064` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00bb0068"></a> `00bb0068` | `39 01 88 9a` | csel x25,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00bb006c"></a> `00bb006c` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00bb0070"></a> `00bb0070` | `36 33 98 9a` | csel x22,x25,x24,cc | `FALL_THROUGH`
<a id="insn-00bb0074"></a> `00bb0074` | `56 01 00 b4` | cbz x22,0x00bb009c | `CONDITIONAL_JUMP`
<a id="insn-00bb0078"></a> `00bb0078` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00bb007c"></a> `00bb007c` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00bb0080"></a> `00bb0080` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bb0084"></a> `00bb0084` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bb0088"></a> `00bb0088` | `81 17 9a 9a` | csinc x1,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00bb008c"></a> `00bb008c` | `25 a0 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00bb0090"></a> `00bb0090` | `60 00 00 34` | cbz w0,0x00bb009c | `CONDITIONAL_JUMP`
<a id="insn-00bb0094"></a> `00bb0094` | `80 00 f8 37` | tbnz w0,#0x1f,0x00bb00a4 | `CONDITIONAL_JUMP`
<a id="insn-00bb0098"></a> `00bb0098` | `09 00 00 14` | b 0x00bb00bc | `UNCONDITIONAL_JUMP`
<a id="insn-00bb009c"></a> `00bb009c` | `1f 03 19 eb` | cmp x24,x25 | `FALL_THROUGH`
<a id="insn-00bb00a0"></a> `00bb00a0` | `a2 00 00 54` | b.cs 0x00bb00b4 | `CONDITIONAL_JUMP`
<a id="insn-00bb00a4"></a> `00bb00a4` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00bb00a8"></a> `00bb00a8` | `08 02 00 b4` | cbz x8,0x00bb00e8 | `CONDITIONAL_JUMP`
<a id="insn-00bb00ac"></a> `00bb00ac` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00bb00b0"></a> `00bb00b0` | `e8 ff ff 17` | b 0x00bb0050 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb00b4"></a> `00bb00b4` | `56 fc ff b4` | cbz x22,0x00bb003c | `CONDITIONAL_JUMP`
<a id="insn-00bb00b8"></a> `00bb00b8` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00bb00bc"></a> `00bb00bc` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00bb00c0"></a> `00bb00c0` | `80 17 9a 9a` | csinc x0,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00bb00c4"></a> `00bb00c4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bb00c8"></a> `00bb00c8` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bb00cc"></a> `00bb00cc` | `15 a0 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00bb00d0"></a> `00bb00d0` | `60 fb ff 34` | cbz w0,0x00bb003c | `CONDITIONAL_JUMP`
<a id="insn-00bb00d4"></a> `00bb00d4` | `80 fb ff 37` | tbnz w0,#0x1f,0x00bb0044 | `CONDITIONAL_JUMP`
<a id="insn-00bb00d8"></a> `00bb00d8` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00bb00dc"></a> `00bb00dc` | `05 00 00 14` | b 0x00bb00f0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb00e0"></a> `00bb00e0` | `74 02 00 f9` | str x20,[x19] | `FALL_THROUGH`
<a id="insn-00bb00e4"></a> `00bb00e4` | `03 00 00 14` | b 0x00bb00f0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb00e8"></a> `00bb00e8` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00bb00ec"></a> `00bb00ec` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00bb00f0"></a> `00bb00f0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bb00f4"></a> `00bb00f4` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bb00f8"></a> `00bb00f8` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bb00fc"></a> `00bb00fc` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bb0100"></a> `00bb0100` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb0104"></a> `00bb0104` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb0108"></a> `00bb0108` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00bb010c"></a> `00bb010c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bafff0`](#insn-00bafff0) 範囲 `[['00bafff0', '00bb001b']]`
  - `CONDITIONAL_JUMP` [`00bb0018`](#insn-00bb0018) → [`00bb00e0`](#insn-00bb00e0)
  - `FALL_THROUGH` [`00bb0018`](#insn-00bb0018) → [`00bb001c`](#insn-00bb001c)
- ブロック [`00bb001c`](#insn-00bb001c) 範囲 `[['00bb001c', '00bb003b']]`
  - `UNCONDITIONAL_JUMP` [`00bb0038`](#insn-00bb0038) → [`00bb0054`](#insn-00bb0054)
- ブロック [`00bb003c`](#insn-00bb003c) 範囲 `[['00bb003c', '00bb0043']]`
  - `CONDITIONAL_JUMP` [`00bb0040`](#insn-00bb0040) → [`00bb00d8`](#insn-00bb00d8)
  - `FALL_THROUGH` [`00bb0040`](#insn-00bb0040) → [`00bb0044`](#insn-00bb0044)
- ブロック [`00bb0044`](#insn-00bb0044) 範囲 `[['00bb0044', '00bb004f']]`
  - `CONDITIONAL_JUMP` [`00bb004c`](#insn-00bb004c) → [`00bb00d8`](#insn-00bb00d8)
  - `FALL_THROUGH` [`00bb004c`](#insn-00bb004c) → [`00bb0050`](#insn-00bb0050)
- ブロック [`00bb0050`](#insn-00bb0050) 範囲 `[['00bb0050', '00bb0053']]`
  - `FALL_THROUGH` [`00bb0050`](#insn-00bb0050) → [`00bb0054`](#insn-00bb0054)
- ブロック [`00bb0054`](#insn-00bb0054) 範囲 `[['00bb0054', '00bb005f']]`
  - `FALL_THROUGH` [`00bb005c`](#insn-00bb005c) → [`00bb0060`](#insn-00bb0060)
- ブロック [`00bb0060`](#insn-00bb0060) 範囲 `[['00bb0060', '00bb0077']]`
  - `CONDITIONAL_JUMP` [`00bb0074`](#insn-00bb0074) → [`00bb009c`](#insn-00bb009c)
  - `FALL_THROUGH` [`00bb0074`](#insn-00bb0074) → [`00bb0078`](#insn-00bb0078)
- ブロック [`00bb0078`](#insn-00bb0078) 範囲 `[['00bb0078', '00bb007b']]`
  - `FALL_THROUGH` [`00bb0078`](#insn-00bb0078) → [`00bb007c`](#insn-00bb007c)
- ブロック [`00bb007c`](#insn-00bb007c) 範囲 `[['00bb007c', '00bb007f']]`
  - `FALL_THROUGH` [`00bb007c`](#insn-00bb007c) → [`00bb0080`](#insn-00bb0080)
- ブロック [`00bb0080`](#insn-00bb0080) 範囲 `[['00bb0080', '00bb0093']]`
  - `CONDITIONAL_JUMP` [`00bb0090`](#insn-00bb0090) → [`00bb009c`](#insn-00bb009c)
  - `FALL_THROUGH` [`00bb0090`](#insn-00bb0090) → [`00bb0094`](#insn-00bb0094)
- ブロック [`00bb0094`](#insn-00bb0094) 範囲 `[['00bb0094', '00bb0097']]`
  - `CONDITIONAL_JUMP` [`00bb0094`](#insn-00bb0094) → [`00bb00a4`](#insn-00bb00a4)
  - `FALL_THROUGH` [`00bb0094`](#insn-00bb0094) → [`00bb0098`](#insn-00bb0098)
- ブロック [`00bb0098`](#insn-00bb0098) 範囲 `[['00bb0098', '00bb009b']]`
  - `UNCONDITIONAL_JUMP` [`00bb0098`](#insn-00bb0098) → [`00bb00bc`](#insn-00bb00bc)
- ブロック [`00bb009c`](#insn-00bb009c) 範囲 `[['00bb009c', '00bb009f']]`
  - `FALL_THROUGH` [`00bb009c`](#insn-00bb009c) → [`00bb00a0`](#insn-00bb00a0)
- ブロック [`00bb00a0`](#insn-00bb00a0) 範囲 `[['00bb00a0', '00bb00a3']]`
  - `CONDITIONAL_JUMP` [`00bb00a0`](#insn-00bb00a0) → [`00bb00b4`](#insn-00bb00b4)
  - `FALL_THROUGH` [`00bb00a0`](#insn-00bb00a0) → [`00bb00a4`](#insn-00bb00a4)
- ブロック [`00bb00a4`](#insn-00bb00a4) 範囲 `[['00bb00a4', '00bb00a7']]`
  - `FALL_THROUGH` [`00bb00a4`](#insn-00bb00a4) → [`00bb00a8`](#insn-00bb00a8)
- ブロック [`00bb00a8`](#insn-00bb00a8) 範囲 `[['00bb00a8', '00bb00ab']]`
  - `CONDITIONAL_JUMP` [`00bb00a8`](#insn-00bb00a8) → [`00bb00e8`](#insn-00bb00e8)
  - `FALL_THROUGH` [`00bb00a8`](#insn-00bb00a8) → [`00bb00ac`](#insn-00bb00ac)
- ブロック [`00bb00ac`](#insn-00bb00ac) 範囲 `[['00bb00ac', '00bb00b3']]`
  - `UNCONDITIONAL_JUMP` [`00bb00b0`](#insn-00bb00b0) → [`00bb0050`](#insn-00bb0050)
- ブロック [`00bb00b4`](#insn-00bb00b4) 範囲 `[['00bb00b4', '00bb00b7']]`
  - `CONDITIONAL_JUMP` [`00bb00b4`](#insn-00bb00b4) → [`00bb003c`](#insn-00bb003c)
  - `FALL_THROUGH` [`00bb00b4`](#insn-00bb00b4) → [`00bb00b8`](#insn-00bb00b8)
- ブロック [`00bb00b8`](#insn-00bb00b8) 範囲 `[['00bb00b8', '00bb00bb']]`
  - `FALL_THROUGH` [`00bb00b8`](#insn-00bb00b8) → [`00bb00bc`](#insn-00bb00bc)
- ブロック [`00bb00bc`](#insn-00bb00bc) 範囲 `[['00bb00bc', '00bb00d3']]`
  - `CONDITIONAL_JUMP` [`00bb00d0`](#insn-00bb00d0) → [`00bb003c`](#insn-00bb003c)
  - `FALL_THROUGH` [`00bb00d0`](#insn-00bb00d0) → [`00bb00d4`](#insn-00bb00d4)
- ブロック [`00bb00d4`](#insn-00bb00d4) 範囲 `[['00bb00d4', '00bb00d7']]`
  - `CONDITIONAL_JUMP` [`00bb00d4`](#insn-00bb00d4) → [`00bb0044`](#insn-00bb0044)
  - `FALL_THROUGH` [`00bb00d4`](#insn-00bb00d4) → [`00bb00d8`](#insn-00bb00d8)
- ブロック [`00bb00d8`](#insn-00bb00d8) 範囲 `[['00bb00d8', '00bb00df']]`
  - `UNCONDITIONAL_JUMP` [`00bb00dc`](#insn-00bb00dc) → [`00bb00f0`](#insn-00bb00f0)
- ブロック [`00bb00e0`](#insn-00bb00e0) 範囲 `[['00bb00e0', '00bb00e7']]`
  - `UNCONDITIONAL_JUMP` [`00bb00e4`](#insn-00bb00e4) → [`00bb00f0`](#insn-00bb00f0)
- ブロック [`00bb00e8`](#insn-00bb00e8) 範囲 `[['00bb00e8', '00bb00ef']]`
  - `FALL_THROUGH` [`00bb00ec`](#insn-00bb00ec) → [`00bb00f0`](#insn-00bb00f0)
- ブロック [`00bb00f0`](#insn-00bb00f0) 範囲 `[['00bb00f0', '00bb010f']]`

## 命令位置別の参照

- [`00bafff0`](#insn-00bafff0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafff4`](#insn-00bafff4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafff8`](#insn-00bafff8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafffc`](#insn-00bafffc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0000`](#insn-00bb0000) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0004`](#insn-00bb0004) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0018`](#insn-00bb0018) → [`00bb00e0`](#insn-00bb00e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0038`](#insn-00bb0038) → [`00bb0054`](#insn-00bb0054) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0040`](#insn-00bb0040) → [`00bb00d8`](#insn-00bb00d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb004c`](#insn-00bb004c) → [`00bb00d8`](#insn-00bb00d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0074`](#insn-00bb0074) → [`00bb009c`](#insn-00bb009c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb008c`](#insn-00bb008c) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00bb0090`](#insn-00bb0090) → [`00bb009c`](#insn-00bb009c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0094`](#insn-00bb0094) → [`00bb00a4`](#insn-00bb00a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0098`](#insn-00bb0098) → [`00bb00bc`](#insn-00bb00bc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb00a0`](#insn-00bb00a0) → [`00bb00b4`](#insn-00bb00b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb00a8`](#insn-00bb00a8) → [`00bb00e8`](#insn-00bb00e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb00b0`](#insn-00bb00b0) → [`00bb0050`](#insn-00bb0050) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb00b4`](#insn-00bb00b4) → [`00bb003c`](#insn-00bb003c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb00cc`](#insn-00bb00cc) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00bb00d0`](#insn-00bb00d0) → [`00bb003c`](#insn-00bb003c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb00d4`](#insn-00bb00d4) → [`00bb0044`](#insn-00bb0044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb00dc`](#insn-00bb00dc) → [`00bb00f0`](#insn-00bb00f0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb00e4`](#insn-00bb00e4) → [`00bb00f0`](#insn-00bb00f0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb00f4`](#insn-00bb00f4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb00f8`](#insn-00bb00f8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb00fc`](#insn-00bb00fc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0100`](#insn-00bb0100) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb0104`](#insn-00bb0104) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bafff0`](#insn-00bafff0)

~~~json
{
  "source": "00bafff0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafff4`](#insn-00bafff4)

~~~json
{
  "source": "00bafff4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafff8`](#insn-00bafff8)

~~~json
{
  "source": "00bafff8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafffc`](#insn-00bafffc)

~~~json
{
  "source": "00bafffc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0000`](#insn-00bb0000)

~~~json
{
  "source": "00bb0000",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0004`](#insn-00bb0004)

~~~json
{
  "source": "00bb0004",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0018`](#insn-00bb0018)

~~~json
{
  "source": "00bb0018",
  "target": "00bb00e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0038`](#insn-00bb0038)

~~~json
{
  "source": "00bb0038",
  "target": "00bb0054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0040`](#insn-00bb0040)

~~~json
{
  "source": "00bb0040",
  "target": "00bb00d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb004c`](#insn-00bb004c)

~~~json
{
  "source": "00bb004c",
  "target": "00bb00d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0074`](#insn-00bb0074)

~~~json
{
  "source": "00bb0074",
  "target": "00bb009c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb008c`](#insn-00bb008c)

~~~json
{
  "source": "00bb008c",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb0090`](#insn-00bb0090)

~~~json
{
  "source": "00bb0090",
  "target": "00bb009c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0094`](#insn-00bb0094)

~~~json
{
  "source": "00bb0094",
  "target": "00bb00a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0098`](#insn-00bb0098)

~~~json
{
  "source": "00bb0098",
  "target": "00bb00bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb00a0`](#insn-00bb00a0)

~~~json
{
  "source": "00bb00a0",
  "target": "00bb00b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb00a8`](#insn-00bb00a8)

~~~json
{
  "source": "00bb00a8",
  "target": "00bb00e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb00b0`](#insn-00bb00b0)

~~~json
{
  "source": "00bb00b0",
  "target": "00bb0050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb00b4`](#insn-00bb00b4)

~~~json
{
  "source": "00bb00b4",
  "target": "00bb003c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb00cc`](#insn-00bb00cc)

~~~json
{
  "source": "00bb00cc",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb00d0`](#insn-00bb00d0)

~~~json
{
  "source": "00bb00d0",
  "target": "00bb003c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb00d4`](#insn-00bb00d4)

~~~json
{
  "source": "00bb00d4",
  "target": "00bb0044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb00dc`](#insn-00bb00dc)

~~~json
{
  "source": "00bb00dc",
  "target": "00bb00f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb00e4`](#insn-00bb00e4)

~~~json
{
  "source": "00bb00e4",
  "target": "00bb00f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb00f4`](#insn-00bb00f4)

~~~json
{
  "source": "00bb00f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb00f8`](#insn-00bb00f8)

~~~json
{
  "source": "00bb00f8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb00fc`](#insn-00bb00fc)

~~~json
{
  "source": "00bb00fc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0100`](#insn-00bb0100)

~~~json
{
  "source": "00bb0100",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb0104`](#insn-00bb0104)

~~~json
{
  "source": "00bb0104",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
