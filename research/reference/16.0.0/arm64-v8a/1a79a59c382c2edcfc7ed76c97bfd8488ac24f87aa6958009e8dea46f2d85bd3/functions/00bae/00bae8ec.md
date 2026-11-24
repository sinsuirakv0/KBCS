# 00bae8ec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 対応未確定
  - [v15.7.4 → v16.0.0 版の比較一覧](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/README.md)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00baed14`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00baed14.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0078.md#compare-29dd8699fdef0c72ef6e4d41b1150493)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bae8ec",
  "name": "_ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3setIN11flatbuffers12IncludedFileENS_4lessISA_EENS5_ISA_EEEEEENS_19__map_value_compareIS7_SF_NSB_IS7_EELb1EEENS5_ISF_EEE4findIS7_EENS_21__tree_const_iteratorISF_PNS_11__tree_nodeISF_PvEElEERKT_",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "da52ae3a6e05bbb32fb6df1c8f4551491240a875ef10a9b986bf19da33aad397",
  "source_text_sha256": "da52ae3a6e05bbb32fb6df1c8f4551491240a875ef10a9b986bf19da33aad397",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bae8ec",
        "00bae9ff"
      ]
    ],
    "bytes_sha256": "84af13b7479fc7b43dae11afd0b60f6d2bb400787ffa874a0929afd96207b696",
    "instruction_count": 69,
    "instruction_bytes": 276,
    "body_bytes": 276,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5c660](../00c5c/00c5c660.md)

## 呼び出し先

- [00c57c50](../00c57/00c57c50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2343 bytes

~~~c

long * _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3setIN11flatbuffers12IncludedFileENS_4lessISA_EENS5_ISA_EEEEEENS_19__map_value_compareIS7_SF_NSB_IS7_EELb1EEENS5_ISF_EEE4findIS7_EENS_21__tree_const_iteratorISF_PNS_11__tree_nodeISF_PvEElEERKT_
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
LAB_00bae92c:
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
                    /* try { // try from 00bae984 to 00caf55f has its CatchHandler @ 00baf80c */
        uVar5 = memcmp(pvVar7,__s2,sVar2);
        if (uVar5 == 0) goto LAB_00bae92c;
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
<a id="insn-00bae8ec"></a> `00bae8ec` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bae8f0"></a> `00bae8f0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bae8f4"></a> `00bae8f4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bae8f8"></a> `00bae8f8` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bae8fc"></a> `00bae8fc` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bae900"></a> `00bae900` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bae904"></a> `00bae904` | `77 8e 40 f8` | ldr x23,[x19, #0x8]! | `FALL_THROUGH`
<a id="insn-00bae908"></a> `00bae908` | `f7 06 00 b4` | cbz x23,0x00bae9e4 | `CONDITIONAL_JUMP`
<a id="insn-00bae90c"></a> `00bae90c` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00bae910"></a> `00bae910` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bae914"></a> `00bae914` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00bae918"></a> `00bae918` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bae91c"></a> `00bae91c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bae920"></a> `00bae920` | `76 01 89 9a` | csel x22,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00bae924"></a> `00bae924` | `55 15 81 9a` | csinc x21,x10,x1,ne | `FALL_THROUGH`
<a id="insn-00bae928"></a> `00bae928` | `0a 00 00 14` | b 0x00bae950 | `UNCONDITIONAL_JUMP`
<a id="insn-00bae92c"></a> `00bae92c` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00bae930"></a> `00bae930` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00bae934"></a> `00bae934` | `1f 03 16 eb` | cmp x24,x22 | `FALL_THROUGH`
<a id="insn-00bae938"></a> `00bae938` | `00 21 9f 5a` | csinv w0,w8,wzr,cs | `FALL_THROUGH`
<a id="insn-00bae93c"></a> `00bae93c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bae940"></a> `00bae940` | `e8 a7 9f 1a` | cset w8,lt | `FALL_THROUGH`
<a id="insn-00bae944"></a> `00bae944` | `94 b2 97 9a` | csel x20,x20,x23,lt | `FALL_THROUGH`
<a id="insn-00bae948"></a> `00bae948` | `f7 5a 68 f8` | ldr x23,[x23, w8, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bae94c"></a> `00bae94c` | `37 02 00 b4` | cbz x23,0x00bae990 | `CONDITIONAL_JUMP`
<a id="insn-00bae950"></a> `00bae950` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-00bae954"></a> `00bae954` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00bae958"></a> `00bae958` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bae95c"></a> `00bae95c` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bae960"></a> `00bae960` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bae964"></a> `00bae964` | `78 01 8a 9a` | csel x24,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00bae968"></a> `00bae968` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00bae96c"></a> `00bae96c` | `c2 32 98 9a` | csel x2,x22,x24,cc | `FALL_THROUGH`
<a id="insn-00bae970"></a> `00bae970` | `e2 fd ff b4` | cbz x2,0x00bae92c | `CONDITIONAL_JUMP`
<a id="insn-00bae974"></a> `00bae974` | `ea 1a 40 f9` | ldr x10,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00bae978"></a> `00bae978` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bae97c"></a> `00bae97c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bae980"></a> `00bae980` | `40 15 88 9a` | csinc x0,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00bae984"></a> `00bae984` | `b3 a4 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bae988"></a> `00bae988` | `a0 fd ff 35` | cbnz w0,0x00bae93c | `CONDITIONAL_JUMP`
<a id="insn-00bae98c"></a> `00bae98c` | `e8 ff ff 17` | b 0x00bae92c | `UNCONDITIONAL_JUMP`
<a id="insn-00bae990"></a> `00bae990` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00bae994"></a> `00bae994` | `80 02 00 54` | b.eq 0x00bae9e4 | `CONDITIONAL_JUMP`
<a id="insn-00bae998"></a> `00bae998` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00bae99c"></a> `00bae99c` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00bae9a0"></a> `00bae9a0` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bae9a4"></a> `00bae9a4` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bae9a8"></a> `00bae9a8` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bae9ac"></a> `00bae9ac` | `77 01 8a 9a` | csel x23,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00bae9b0"></a> `00bae9b0` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00bae9b4"></a> `00bae9b4` | `e2 32 96 9a` | csel x2,x23,x22,cc | `FALL_THROUGH`
<a id="insn-00bae9b8"></a> `00bae9b8` | `22 01 00 b4` | cbz x2,0x00bae9dc | `CONDITIONAL_JUMP`
<a id="insn-00bae9bc"></a> `00bae9bc` | `8a 1a 40 f9` | ldr x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00bae9c0"></a> `00bae9c0` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bae9c4"></a> `00bae9c4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bae9c8"></a> `00bae9c8` | `41 15 88 9a` | csinc x1,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00bae9cc"></a> `00bae9cc` | `a1 a4 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bae9d0"></a> `00bae9d0` | `60 00 00 34` | cbz w0,0x00bae9dc | `CONDITIONAL_JUMP`
<a id="insn-00bae9d4"></a> `00bae9d4` | `80 00 f8 37` | tbnz w0,#0x1f,0x00bae9e4 | `CONDITIONAL_JUMP`
<a id="insn-00bae9d8"></a> `00bae9d8` | `04 00 00 14` | b 0x00bae9e8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bae9dc"></a> `00bae9dc` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-00bae9e0"></a> `00bae9e0` | `42 00 00 54` | b.cs 0x00bae9e8 | `CONDITIONAL_JUMP`
<a id="insn-00bae9e4"></a> `00bae9e4` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00bae9e8"></a> `00bae9e8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bae9ec"></a> `00bae9ec` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bae9f0"></a> `00bae9f0` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bae9f4"></a> `00bae9f4` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bae9f8"></a> `00bae9f8` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bae9fc"></a> `00bae9fc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bae8ec`](#insn-00bae8ec) 範囲 `[['00bae8ec', '00bae90b']]`
  - `CONDITIONAL_JUMP` [`00bae908`](#insn-00bae908) → [`00bae9e4`](#insn-00bae9e4)
  - `FALL_THROUGH` [`00bae908`](#insn-00bae908) → [`00bae90c`](#insn-00bae90c)
- ブロック [`00bae90c`](#insn-00bae90c) 範囲 `[['00bae90c', '00bae92b']]`
  - `UNCONDITIONAL_JUMP` [`00bae928`](#insn-00bae928) → [`00bae950`](#insn-00bae950)
- ブロック [`00bae92c`](#insn-00bae92c) 範囲 `[['00bae92c', '00bae93b']]`
  - `FALL_THROUGH` [`00bae938`](#insn-00bae938) → [`00bae93c`](#insn-00bae93c)
- ブロック [`00bae93c`](#insn-00bae93c) 範囲 `[['00bae93c', '00bae94f']]`
  - `CONDITIONAL_JUMP` [`00bae94c`](#insn-00bae94c) → [`00bae990`](#insn-00bae990)
  - `FALL_THROUGH` [`00bae94c`](#insn-00bae94c) → [`00bae950`](#insn-00bae950)
- ブロック [`00bae950`](#insn-00bae950) 範囲 `[['00bae950', '00bae973']]`
  - `CONDITIONAL_JUMP` [`00bae970`](#insn-00bae970) → [`00bae92c`](#insn-00bae92c)
  - `FALL_THROUGH` [`00bae970`](#insn-00bae970) → [`00bae974`](#insn-00bae974)
- ブロック [`00bae974`](#insn-00bae974) 範囲 `[['00bae974', '00bae983']]`
  - `FALL_THROUGH` [`00bae980`](#insn-00bae980) → [`00bae984`](#insn-00bae984)
- ブロック [`00bae984`](#insn-00bae984) 範囲 `[['00bae984', '00bae98b']]`
  - `CONDITIONAL_JUMP` [`00bae988`](#insn-00bae988) → [`00bae93c`](#insn-00bae93c)
  - `FALL_THROUGH` [`00bae988`](#insn-00bae988) → [`00bae98c`](#insn-00bae98c)
- ブロック [`00bae98c`](#insn-00bae98c) 範囲 `[['00bae98c', '00bae98f']]`
  - `UNCONDITIONAL_JUMP` [`00bae98c`](#insn-00bae98c) → [`00bae92c`](#insn-00bae92c)
- ブロック [`00bae990`](#insn-00bae990) 範囲 `[['00bae990', '00bae997']]`
  - `CONDITIONAL_JUMP` [`00bae994`](#insn-00bae994) → [`00bae9e4`](#insn-00bae9e4)
  - `FALL_THROUGH` [`00bae994`](#insn-00bae994) → [`00bae998`](#insn-00bae998)
- ブロック [`00bae998`](#insn-00bae998) 範囲 `[['00bae998', '00bae9bb']]`
  - `CONDITIONAL_JUMP` [`00bae9b8`](#insn-00bae9b8) → [`00bae9dc`](#insn-00bae9dc)
  - `FALL_THROUGH` [`00bae9b8`](#insn-00bae9b8) → [`00bae9bc`](#insn-00bae9bc)
- ブロック [`00bae9bc`](#insn-00bae9bc) 範囲 `[['00bae9bc', '00bae9d3']]`
  - `CONDITIONAL_JUMP` [`00bae9d0`](#insn-00bae9d0) → [`00bae9dc`](#insn-00bae9dc)
  - `FALL_THROUGH` [`00bae9d0`](#insn-00bae9d0) → [`00bae9d4`](#insn-00bae9d4)
- ブロック [`00bae9d4`](#insn-00bae9d4) 範囲 `[['00bae9d4', '00bae9d7']]`
  - `CONDITIONAL_JUMP` [`00bae9d4`](#insn-00bae9d4) → [`00bae9e4`](#insn-00bae9e4)
  - `FALL_THROUGH` [`00bae9d4`](#insn-00bae9d4) → [`00bae9d8`](#insn-00bae9d8)
- ブロック [`00bae9d8`](#insn-00bae9d8) 範囲 `[['00bae9d8', '00bae9db']]`
  - `UNCONDITIONAL_JUMP` [`00bae9d8`](#insn-00bae9d8) → [`00bae9e8`](#insn-00bae9e8)
- ブロック [`00bae9dc`](#insn-00bae9dc) 範囲 `[['00bae9dc', '00bae9e3']]`
  - `CONDITIONAL_JUMP` [`00bae9e0`](#insn-00bae9e0) → [`00bae9e8`](#insn-00bae9e8)
  - `FALL_THROUGH` [`00bae9e0`](#insn-00bae9e0) → [`00bae9e4`](#insn-00bae9e4)
- ブロック [`00bae9e4`](#insn-00bae9e4) 範囲 `[['00bae9e4', '00bae9e7']]`
  - `FALL_THROUGH` [`00bae9e4`](#insn-00bae9e4) → [`00bae9e8`](#insn-00bae9e8)
- ブロック [`00bae9e8`](#insn-00bae9e8) 範囲 `[['00bae9e8', '00bae9ff']]`

## 命令位置別の参照

- [`00bae8ec`](#insn-00bae8ec) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae8f0`](#insn-00bae8f0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae8f4`](#insn-00bae8f4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae8f8`](#insn-00bae8f8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae908`](#insn-00bae908) → [`00bae9e4`](#insn-00bae9e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae928`](#insn-00bae928) → [`00bae950`](#insn-00bae950) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae94c`](#insn-00bae94c) → [`00bae990`](#insn-00bae990) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae970`](#insn-00bae970) → [`00bae92c`](#insn-00bae92c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae984`](#insn-00bae984) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bae988`](#insn-00bae988) → [`00bae93c`](#insn-00bae93c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae98c`](#insn-00bae98c) → [`00bae92c`](#insn-00bae92c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae994`](#insn-00bae994) → [`00bae9e4`](#insn-00bae9e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae9b8`](#insn-00bae9b8) → [`00bae9dc`](#insn-00bae9dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae9cc`](#insn-00bae9cc) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bae9d0`](#insn-00bae9d0) → [`00bae9dc`](#insn-00bae9dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae9d4`](#insn-00bae9d4) → [`00bae9e4`](#insn-00bae9e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae9d8`](#insn-00bae9d8) → [`00bae9e8`](#insn-00bae9e8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae9e0`](#insn-00bae9e0) → [`00bae9e8`](#insn-00bae9e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae9ec`](#insn-00bae9ec) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae9f0`](#insn-00bae9f0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bae9f4`](#insn-00bae9f4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bae8ec`](#insn-00bae8ec)

~~~json
{
  "source": "00bae8ec",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae8f0`](#insn-00bae8f0)

~~~json
{
  "source": "00bae8f0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae8f4`](#insn-00bae8f4)

~~~json
{
  "source": "00bae8f4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae8f8`](#insn-00bae8f8)

~~~json
{
  "source": "00bae8f8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae908`](#insn-00bae908)

~~~json
{
  "source": "00bae908",
  "target": "00bae9e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae928`](#insn-00bae928)

~~~json
{
  "source": "00bae928",
  "target": "00bae950",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae94c`](#insn-00bae94c)

~~~json
{
  "source": "00bae94c",
  "target": "00bae990",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae970`](#insn-00bae970)

~~~json
{
  "source": "00bae970",
  "target": "00bae92c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae984`](#insn-00bae984)

~~~json
{
  "source": "00bae984",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bae988`](#insn-00bae988)

~~~json
{
  "source": "00bae988",
  "target": "00bae93c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae98c`](#insn-00bae98c)

~~~json
{
  "source": "00bae98c",
  "target": "00bae92c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae994`](#insn-00bae994)

~~~json
{
  "source": "00bae994",
  "target": "00bae9e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae9b8`](#insn-00bae9b8)

~~~json
{
  "source": "00bae9b8",
  "target": "00bae9dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae9cc`](#insn-00bae9cc)

~~~json
{
  "source": "00bae9cc",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bae9d0`](#insn-00bae9d0)

~~~json
{
  "source": "00bae9d0",
  "target": "00bae9dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae9d4`](#insn-00bae9d4)

~~~json
{
  "source": "00bae9d4",
  "target": "00bae9e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae9d8`](#insn-00bae9d8)

~~~json
{
  "source": "00bae9d8",
  "target": "00bae9e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae9e0`](#insn-00bae9e0)

~~~json
{
  "source": "00bae9e0",
  "target": "00bae9e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae9ec`](#insn-00bae9ec)

~~~json
{
  "source": "00bae9ec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae9f0`](#insn-00bae9f0)

~~~json
{
  "source": "00bae9f0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bae9f4`](#insn-00bae9f4)

~~~json
{
  "source": "00bae9f4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
