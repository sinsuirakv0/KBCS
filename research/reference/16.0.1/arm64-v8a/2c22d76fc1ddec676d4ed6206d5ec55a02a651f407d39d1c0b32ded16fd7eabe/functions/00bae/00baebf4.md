# 00baebf4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bae7cc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae7cc.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0038.md#compare-a82e46adb10c5e94fcbfcf914fdde51b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00baec90`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baec90.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0038.md#compare-3c7fd51b104f3cf348b294283d998dd7)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baebf4",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers4TypeEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "48db6cb7a40c13227abe35729d0d844544de1b06d9795e9c1d9e02b66a52b9d5",
  "source_text_sha256": "48db6cb7a40c13227abe35729d0d844544de1b06d9795e9c1d9e02b66a52b9d5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baebf4",
        "00baed13"
      ]
    ],
    "bytes_sha256": "df8c93f3242938d2f33ec9f488389ea4b91425ecae53763098f4b57fe3829a6f",
    "instruction_count": 72,
    "instruction_bytes": 288,
    "body_bytes": 288,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5ce80](../00c5c/00c5ce80.md)

## 呼び出し先

- [00c58050](../00c58/00c58050.md)

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
      if (iVar4 < 0) goto LAB_00baeca8;
LAB_00baecc0:
      if ((bVar3 & 1) == 0) {
        __s1_00 = (void *)((long)plVar7 + 0x21);
      }
      iVar4 = memcmp(__s1_00,__s1,__n);
      if (iVar4 == 0) goto LAB_00baec40;
      if (-1 < iVar4) goto LAB_00baecdc;
LAB_00baec48:
      plVar5 = plVar7 + 1;
      plVar6 = (long *)*plVar5;
      if ((long *)*plVar5 == (long *)0x0) {
LAB_00baecdc:
        *param_2 = plVar7;
        return plVar5;
      }
    }
    if (uVar1 <= uVar2) {
      if (__n != 0) {
        __s1_00 = (void *)plVar7[6];
        goto LAB_00baecc0;
      }
LAB_00baec40:
      if (uVar2 <= uVar1) goto LAB_00baecdc;
      goto LAB_00baec48;
    }
LAB_00baeca8:
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
<a id="insn-00baebf4"></a> `00baebf4` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00baebf8"></a> `00baebf8` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baebfc"></a> `00baebfc` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baec00"></a> `00baec00` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baec04"></a> `00baec04` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00baec08"></a> `00baec08` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00baec0c"></a> `00baec0c` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00baec10"></a> `00baec10` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00baec14"></a> `00baec14` | `97 8e 40 f8` | ldr x23,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00baec18"></a> `00baec18` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00baec1c"></a> `00baec1c` | `57 06 00 b4` | cbz x23,0x00baece4 | `CONDITIONAL_JUMP`
<a id="insn-00baec20"></a> `00baec20` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00baec24"></a> `00baec24` | `49 a8 40 a9` | ldp x9,x10,[x2, #0x8] | `FALL_THROUGH`
<a id="insn-00baec28"></a> `00baec28` | `14 20 00 91` | add x20,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00baec2c"></a> `00baec2c` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00baec30"></a> `00baec30` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baec34"></a> `00baec34` | `78 01 89 9a` | csel x24,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00baec38"></a> `00baec38` | `55 15 82 9a` | csinc x21,x10,x2,ne | `FALL_THROUGH`
<a id="insn-00baec3c"></a> `00baec3c` | `07 00 00 14` | b 0x00baec58 | `UNCONDITIONAL_JUMP`
<a id="insn-00baec40"></a> `00baec40` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00baec44"></a> `00baec44` | `c2 04 00 54` | b.cs 0x00baecdc | `CONDITIONAL_JUMP`
<a id="insn-00baec48"></a> `00baec48` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00baec4c"></a> `00baec4c` | `88 8e 40 f8` | ldr x8,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00baec50"></a> `00baec50` | `68 04 00 b4` | cbz x8,0x00baecdc | `CONDITIONAL_JUMP`
<a id="insn-00baec54"></a> `00baec54` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00baec58"></a> `00baec58` | `fa 03 17 aa` | mov x26,x23 | `FALL_THROUGH`
<a id="insn-00baec5c"></a> `00baec5c` | `5b 0f 42 38` | ldrb w27,[x26, #0x20]! | `FALL_THROUGH`
<a id="insn-00baec60"></a> `00baec60` | `48 07 40 f9` | ldr x8,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00baec64"></a> `00baec64` | `69 ff 41 d3` | lsr x9,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00baec68"></a> `00baec68` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00baec6c"></a> `00baec6c` | `39 01 88 9a` | csel x25,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00baec70"></a> `00baec70` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00baec74"></a> `00baec74` | `36 33 98 9a` | csel x22,x25,x24,cc | `FALL_THROUGH`
<a id="insn-00baec78"></a> `00baec78` | `56 01 00 b4` | cbz x22,0x00baeca0 | `CONDITIONAL_JUMP`
<a id="insn-00baec7c"></a> `00baec7c` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00baec80"></a> `00baec80` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00baec84"></a> `00baec84` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00baec88"></a> `00baec88` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00baec8c"></a> `00baec8c` | `81 17 9a 9a` | csinc x1,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00baec90"></a> `00baec90` | `f0 a4 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00baec94"></a> `00baec94` | `60 00 00 34` | cbz w0,0x00baeca0 | `CONDITIONAL_JUMP`
<a id="insn-00baec98"></a> `00baec98` | `80 00 f8 37` | tbnz w0,#0x1f,0x00baeca8 | `CONDITIONAL_JUMP`
<a id="insn-00baec9c"></a> `00baec9c` | `09 00 00 14` | b 0x00baecc0 | `UNCONDITIONAL_JUMP`
<a id="insn-00baeca0"></a> `00baeca0` | `1f 03 19 eb` | cmp x24,x25 | `FALL_THROUGH`
<a id="insn-00baeca4"></a> `00baeca4` | `a2 00 00 54` | b.cs 0x00baecb8 | `CONDITIONAL_JUMP`
<a id="insn-00baeca8"></a> `00baeca8` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00baecac"></a> `00baecac` | `08 02 00 b4` | cbz x8,0x00baecec | `CONDITIONAL_JUMP`
<a id="insn-00baecb0"></a> `00baecb0` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00baecb4"></a> `00baecb4` | `e8 ff ff 17` | b 0x00baec54 | `UNCONDITIONAL_JUMP`
<a id="insn-00baecb8"></a> `00baecb8` | `56 fc ff b4` | cbz x22,0x00baec40 | `CONDITIONAL_JUMP`
<a id="insn-00baecbc"></a> `00baecbc` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00baecc0"></a> `00baecc0` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00baecc4"></a> `00baecc4` | `80 17 9a 9a` | csinc x0,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00baecc8"></a> `00baecc8` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00baeccc"></a> `00baeccc` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00baecd0"></a> `00baecd0` | `e0 a4 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00baecd4"></a> `00baecd4` | `60 fb ff 34` | cbz w0,0x00baec40 | `CONDITIONAL_JUMP`
<a id="insn-00baecd8"></a> `00baecd8` | `80 fb ff 37` | tbnz w0,#0x1f,0x00baec48 | `CONDITIONAL_JUMP`
<a id="insn-00baecdc"></a> `00baecdc` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00baece0"></a> `00baece0` | `05 00 00 14` | b 0x00baecf4 | `UNCONDITIONAL_JUMP`
<a id="insn-00baece4"></a> `00baece4` | `74 02 00 f9` | str x20,[x19] | `FALL_THROUGH`
<a id="insn-00baece8"></a> `00baece8` | `03 00 00 14` | b 0x00baecf4 | `UNCONDITIONAL_JUMP`
<a id="insn-00baecec"></a> `00baecec` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00baecf0"></a> `00baecf0` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00baecf4"></a> `00baecf4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00baecf8"></a> `00baecf8` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00baecfc"></a> `00baecfc` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00baed00"></a> `00baed00` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baed04"></a> `00baed04` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baed08"></a> `00baed08` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baed0c"></a> `00baed0c` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00baed10"></a> `00baed10` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baebf4`](#insn-00baebf4) 範囲 `[['00baebf4', '00baec1f']]`
  - `CONDITIONAL_JUMP` [`00baec1c`](#insn-00baec1c) → [`00baece4`](#insn-00baece4)
  - `FALL_THROUGH` [`00baec1c`](#insn-00baec1c) → [`00baec20`](#insn-00baec20)
- ブロック [`00baec20`](#insn-00baec20) 範囲 `[['00baec20', '00baec3f']]`
  - `UNCONDITIONAL_JUMP` [`00baec3c`](#insn-00baec3c) → [`00baec58`](#insn-00baec58)
- ブロック [`00baec40`](#insn-00baec40) 範囲 `[['00baec40', '00baec47']]`
  - `CONDITIONAL_JUMP` [`00baec44`](#insn-00baec44) → [`00baecdc`](#insn-00baecdc)
  - `FALL_THROUGH` [`00baec44`](#insn-00baec44) → [`00baec48`](#insn-00baec48)
- ブロック [`00baec48`](#insn-00baec48) 範囲 `[['00baec48', '00baec53']]`
  - `CONDITIONAL_JUMP` [`00baec50`](#insn-00baec50) → [`00baecdc`](#insn-00baecdc)
  - `FALL_THROUGH` [`00baec50`](#insn-00baec50) → [`00baec54`](#insn-00baec54)
- ブロック [`00baec54`](#insn-00baec54) 範囲 `[['00baec54', '00baec57']]`
  - `FALL_THROUGH` [`00baec54`](#insn-00baec54) → [`00baec58`](#insn-00baec58)
- ブロック [`00baec58`](#insn-00baec58) 範囲 `[['00baec58', '00baec7b']]`
  - `CONDITIONAL_JUMP` [`00baec78`](#insn-00baec78) → [`00baeca0`](#insn-00baeca0)
  - `FALL_THROUGH` [`00baec78`](#insn-00baec78) → [`00baec7c`](#insn-00baec7c)
- ブロック [`00baec7c`](#insn-00baec7c) 範囲 `[['00baec7c', '00baec97']]`
  - `CONDITIONAL_JUMP` [`00baec94`](#insn-00baec94) → [`00baeca0`](#insn-00baeca0)
  - `FALL_THROUGH` [`00baec94`](#insn-00baec94) → [`00baec98`](#insn-00baec98)
- ブロック [`00baec98`](#insn-00baec98) 範囲 `[['00baec98', '00baec9b']]`
  - `CONDITIONAL_JUMP` [`00baec98`](#insn-00baec98) → [`00baeca8`](#insn-00baeca8)
  - `FALL_THROUGH` [`00baec98`](#insn-00baec98) → [`00baec9c`](#insn-00baec9c)
- ブロック [`00baec9c`](#insn-00baec9c) 範囲 `[['00baec9c', '00baec9f']]`
  - `UNCONDITIONAL_JUMP` [`00baec9c`](#insn-00baec9c) → [`00baecc0`](#insn-00baecc0)
- ブロック [`00baeca0`](#insn-00baeca0) 範囲 `[['00baeca0', '00baeca7']]`
  - `CONDITIONAL_JUMP` [`00baeca4`](#insn-00baeca4) → [`00baecb8`](#insn-00baecb8)
  - `FALL_THROUGH` [`00baeca4`](#insn-00baeca4) → [`00baeca8`](#insn-00baeca8)
- ブロック [`00baeca8`](#insn-00baeca8) 範囲 `[['00baeca8', '00baecaf']]`
  - `CONDITIONAL_JUMP` [`00baecac`](#insn-00baecac) → [`00baecec`](#insn-00baecec)
  - `FALL_THROUGH` [`00baecac`](#insn-00baecac) → [`00baecb0`](#insn-00baecb0)
- ブロック [`00baecb0`](#insn-00baecb0) 範囲 `[['00baecb0', '00baecb7']]`
  - `UNCONDITIONAL_JUMP` [`00baecb4`](#insn-00baecb4) → [`00baec54`](#insn-00baec54)
- ブロック [`00baecb8`](#insn-00baecb8) 範囲 `[['00baecb8', '00baecbb']]`
  - `CONDITIONAL_JUMP` [`00baecb8`](#insn-00baecb8) → [`00baec40`](#insn-00baec40)
  - `FALL_THROUGH` [`00baecb8`](#insn-00baecb8) → [`00baecbc`](#insn-00baecbc)
- ブロック [`00baecbc`](#insn-00baecbc) 範囲 `[['00baecbc', '00baecbf']]`
  - `FALL_THROUGH` [`00baecbc`](#insn-00baecbc) → [`00baecc0`](#insn-00baecc0)
- ブロック [`00baecc0`](#insn-00baecc0) 範囲 `[['00baecc0', '00baecd7']]`
  - `CONDITIONAL_JUMP` [`00baecd4`](#insn-00baecd4) → [`00baec40`](#insn-00baec40)
  - `FALL_THROUGH` [`00baecd4`](#insn-00baecd4) → [`00baecd8`](#insn-00baecd8)
- ブロック [`00baecd8`](#insn-00baecd8) 範囲 `[['00baecd8', '00baecdb']]`
  - `CONDITIONAL_JUMP` [`00baecd8`](#insn-00baecd8) → [`00baec48`](#insn-00baec48)
  - `FALL_THROUGH` [`00baecd8`](#insn-00baecd8) → [`00baecdc`](#insn-00baecdc)
- ブロック [`00baecdc`](#insn-00baecdc) 範囲 `[['00baecdc', '00baece3']]`
  - `UNCONDITIONAL_JUMP` [`00baece0`](#insn-00baece0) → [`00baecf4`](#insn-00baecf4)
- ブロック [`00baece4`](#insn-00baece4) 範囲 `[['00baece4', '00baeceb']]`
  - `UNCONDITIONAL_JUMP` [`00baece8`](#insn-00baece8) → [`00baecf4`](#insn-00baecf4)
- ブロック [`00baecec`](#insn-00baecec) 範囲 `[['00baecec', '00baecf3']]`
  - `FALL_THROUGH` [`00baecf0`](#insn-00baecf0) → [`00baecf4`](#insn-00baecf4)
- ブロック [`00baecf4`](#insn-00baecf4) 範囲 `[['00baecf4', '00baed13']]`

## 命令位置別の参照

- [`00baebf4`](#insn-00baebf4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baebf8`](#insn-00baebf8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baebfc`](#insn-00baebfc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec00`](#insn-00baec00) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec04`](#insn-00baec04) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec08`](#insn-00baec08) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec1c`](#insn-00baec1c) → [`00baece4`](#insn-00baece4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec3c`](#insn-00baec3c) → [`00baec58`](#insn-00baec58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec44`](#insn-00baec44) → [`00baecdc`](#insn-00baecdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec50`](#insn-00baec50) → [`00baecdc`](#insn-00baecdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec78`](#insn-00baec78) → [`00baeca0`](#insn-00baeca0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec90`](#insn-00baec90) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00baec94`](#insn-00baec94) → [`00baeca0`](#insn-00baeca0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec98`](#insn-00baec98) → [`00baeca8`](#insn-00baeca8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baec9c`](#insn-00baec9c) → [`00baecc0`](#insn-00baecc0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeca4`](#insn-00baeca4) → [`00baecb8`](#insn-00baecb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baecac`](#insn-00baecac) → [`00baecec`](#insn-00baecec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baecb4`](#insn-00baecb4) → [`00baec54`](#insn-00baec54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baecb8`](#insn-00baecb8) → [`00baec40`](#insn-00baec40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baecd0`](#insn-00baecd0) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00baecd4`](#insn-00baecd4) → [`00baec40`](#insn-00baec40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baecd8`](#insn-00baecd8) → [`00baec48`](#insn-00baec48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baece0`](#insn-00baece0) → [`00baecf4`](#insn-00baecf4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baece8`](#insn-00baece8) → [`00baecf4`](#insn-00baecf4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baecf8`](#insn-00baecf8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baecfc`](#insn-00baecfc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baed00`](#insn-00baed00) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baed04`](#insn-00baed04) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baed08`](#insn-00baed08) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baebf4`](#insn-00baebf4)

~~~json
{
  "source": "00baebf4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baebf8`](#insn-00baebf8)

~~~json
{
  "source": "00baebf8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baebfc`](#insn-00baebfc)

~~~json
{
  "source": "00baebfc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec00`](#insn-00baec00)

~~~json
{
  "source": "00baec00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec04`](#insn-00baec04)

~~~json
{
  "source": "00baec04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec08`](#insn-00baec08)

~~~json
{
  "source": "00baec08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec1c`](#insn-00baec1c)

~~~json
{
  "source": "00baec1c",
  "target": "00baece4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec3c`](#insn-00baec3c)

~~~json
{
  "source": "00baec3c",
  "target": "00baec58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec44`](#insn-00baec44)

~~~json
{
  "source": "00baec44",
  "target": "00baecdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec50`](#insn-00baec50)

~~~json
{
  "source": "00baec50",
  "target": "00baecdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec78`](#insn-00baec78)

~~~json
{
  "source": "00baec78",
  "target": "00baeca0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec90`](#insn-00baec90)

~~~json
{
  "source": "00baec90",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baec94`](#insn-00baec94)

~~~json
{
  "source": "00baec94",
  "target": "00baeca0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec98`](#insn-00baec98)

~~~json
{
  "source": "00baec98",
  "target": "00baeca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baec9c`](#insn-00baec9c)

~~~json
{
  "source": "00baec9c",
  "target": "00baecc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeca4`](#insn-00baeca4)

~~~json
{
  "source": "00baeca4",
  "target": "00baecb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baecac`](#insn-00baecac)

~~~json
{
  "source": "00baecac",
  "target": "00baecec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baecb4`](#insn-00baecb4)

~~~json
{
  "source": "00baecb4",
  "target": "00baec54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baecb8`](#insn-00baecb8)

~~~json
{
  "source": "00baecb8",
  "target": "00baec40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baecd0`](#insn-00baecd0)

~~~json
{
  "source": "00baecd0",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baecd4`](#insn-00baecd4)

~~~json
{
  "source": "00baecd4",
  "target": "00baec40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baecd8`](#insn-00baecd8)

~~~json
{
  "source": "00baecd8",
  "target": "00baec48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baece0`](#insn-00baece0)

~~~json
{
  "source": "00baece0",
  "target": "00baecf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baece8`](#insn-00baece8)

~~~json
{
  "source": "00baece8",
  "target": "00baecf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baecf8`](#insn-00baecf8)

~~~json
{
  "source": "00baecf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baecfc`](#insn-00baecfc)

~~~json
{
  "source": "00baecfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baed00`](#insn-00baed00)

~~~json
{
  "source": "00baed00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baed04`](#insn-00baed04)

~~~json
{
  "source": "00baed04",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baed08`](#insn-00baed08)

~~~json
{
  "source": "00baed08",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
