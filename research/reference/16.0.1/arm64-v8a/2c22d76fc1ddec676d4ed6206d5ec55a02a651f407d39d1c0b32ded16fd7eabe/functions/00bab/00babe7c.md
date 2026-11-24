# 00babe7c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00baba54`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bab/00baba54.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0078.md#compare-a7937db785484c6f53db0f1987149039)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00babf18`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bab/00babf18.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0078.md#compare-0f03fbca9717c2c20ca42c6ffc00095d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00babe7c",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b8649d53eace244423d68236fd3a8285bddc68a18fad11d9acd56f0cdaf472d9",
  "source_text_sha256": "b8649d53eace244423d68236fd3a8285bddc68a18fad11d9acd56f0cdaf472d9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00babe7c",
        "00babf9b"
      ]
    ],
    "bytes_sha256": "89c42582bcb0383d222aea5e82ed1ca6ae62ff9c6d959e2b22b9737c7f81b161",
    "instruction_count": 72,
    "instruction_bytes": 288,
    "body_bytes": 288,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5cf80](../00c5c/00c5cf80.md)

## 呼び出し先

- [00c58050](../00c58/00c58050.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4457 bytes

~~~c

long * _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_
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
  
                    /* catch() { ... } // from try @ 00baa6d0 with catch @ 00babe84 */
                    /* catch() { ... } // from try @ 00baa6b0 with catch @ 00babe88 */
                    /* catch() { ... } // from try @ 00baa67c with catch @ 00babe98 */
                    /* catch() { ... } // from try @ 00baa658 with catch @ 00babe9c */
  plVar5 = (long *)(param_1 + 8);
  plVar6 = (long *)*plVar5;
  if (plVar6 == (long *)0x0) {
                    /* catch() { ... } // from try @ 00baa7c8 with catch @ 00babf6c */
    *param_2 = plVar5;
                    /* catch() { ... } // from try @ 00baa56c with catch @ 00babf7c */
                    /* catch() { ... } // from try @ 00ba9d88 with catch @ 00babf8c */
    return plVar5;
  }
                    /* catch() { ... } // from try @ 00baaa24 with catch @ 00babeac */
  uVar2 = *(ulong *)(param_3 + 8);
  __s1 = *(byte **)(param_3 + 0x10);
                    /* catch() { ... } // from try @ 00baa888 with catch @ 00babeb0 */
                    /* catch() { ... } // from try @ 00baa62c with catch @ 00babeb4 */
                    /* catch() { ... } // from try @ 00ba9e44 with catch @ 00babeb8 */
  plVar5 = (long *)(param_1 + 8);
                    /* catch() { ... } // from try @ 00baaa00 with catch @ 00babebc */
  if ((*param_3 & 1) == 0) {
    __s1 = param_3 + 1;
    uVar2 = (ulong)(*param_3 >> 1);
  }
  do {
    while( true ) {
      plVar7 = plVar6;
      bVar3 = *(byte *)(plVar7 + 4);
                    /* catch() { ... } // from try @ 00ba9e24 with catch @ 00babeec */
      uVar1 = (ulong)(bVar3 >> 1);
      if ((bVar3 & 1) != 0) {
        uVar1 = plVar7[5];
      }
      __n = uVar1;
                    /* catch() { ... } // from try @ 00baa9d4 with catch @ 00babefc */
      if (uVar2 <= uVar1) {
        __n = uVar2;
      }
                    /* catch() { ... } // from try @ 00baa838 with catch @ 00babf00 */
      if (__n == 0) break;
                    /* catch() { ... } // from try @ 00baa5dc with catch @ 00babf04 */
      __s1_00 = (void *)plVar7[6];
                    /* catch() { ... } // from try @ 00ba9df8 with catch @ 00babf08 */
      __s2 = __s1_00;
                    /* catch() { ... } // from try @ 00baa9b0 with catch @ 00babf0c */
      if ((bVar3 & 1) == 0) {
        __s2 = (void *)((long)plVar7 + 0x21);
      }
      iVar4 = memcmp(__s1,__s2,__n);
                    /* catch() { ... } // from try @ 00baa814 with catch @ 00babf1c */
      if (iVar4 == 0) break;
      if (iVar4 < 0) goto LAB_00babf30;
LAB_00babf48:
                    /* catch() { ... } // from try @ 00baa984 with catch @ 00babf4c */
      if ((bVar3 & 1) == 0) {
        __s1_00 = (void *)((long)plVar7 + 0x21);
      }
                    /* catch() { ... } // from try @ 00baa7e8 with catch @ 00babf50 */
                    /* catch() { ... } // from try @ 00baa58c with catch @ 00babf54 */
                    /* catch() { ... } // from try @ 00ba9da8 with catch @ 00babf58 */
      iVar4 = memcmp(__s1_00,__s1,__n);
                    /* catch() { ... } // from try @ 00baa964 with catch @ 00babf5c */
      if (iVar4 == 0) goto LAB_00babec8;
      if (-1 < iVar4) goto LAB_00babf64;
LAB_00babed0:
      plVar5 = plVar7 + 1;
      plVar6 = (long *)*plVar5;
      if ((long *)*plVar5 == (long *)0x0) {
LAB_00babf64:
        *param_2 = plVar7;
        return plVar5;
      }
    }
                    /* catch() { ... } // from try @ 00baa5b8 with catch @ 00babf2c */
    if (uVar1 <= uVar2) {
      if (__n != 0) {
        __s1_00 = (void *)plVar7[6];
        goto LAB_00babf48;
      }
LAB_00babec8:
                    /* catch() { ... } // from try @ 00baa864 with catch @ 00babecc */
      if (uVar2 <= uVar1) goto LAB_00babf64;
      goto LAB_00babed0;
    }
LAB_00babf30:
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
<a id="insn-00babe7c"></a> `00babe7c` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00babe80"></a> `00babe80` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00babe84"></a> `00babe84` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00babe88"></a> `00babe88` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00babe8c"></a> `00babe8c` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00babe90"></a> `00babe90` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00babe94"></a> `00babe94` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00babe98"></a> `00babe98` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00babe9c"></a> `00babe9c` | `97 8e 40 f8` | ldr x23,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00babea0"></a> `00babea0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00babea4"></a> `00babea4` | `57 06 00 b4` | cbz x23,0x00babf6c | `CONDITIONAL_JUMP`
<a id="insn-00babea8"></a> `00babea8` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00babeac"></a> `00babeac` | `49 a8 40 a9` | ldp x9,x10,[x2, #0x8] | `FALL_THROUGH`
<a id="insn-00babeb0"></a> `00babeb0` | `14 20 00 91` | add x20,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00babeb4"></a> `00babeb4` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00babeb8"></a> `00babeb8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00babebc"></a> `00babebc` | `78 01 89 9a` | csel x24,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00babec0"></a> `00babec0` | `55 15 82 9a` | csinc x21,x10,x2,ne | `FALL_THROUGH`
<a id="insn-00babec4"></a> `00babec4` | `07 00 00 14` | b 0x00babee0 | `UNCONDITIONAL_JUMP`
<a id="insn-00babec8"></a> `00babec8` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00babecc"></a> `00babecc` | `c2 04 00 54` | b.cs 0x00babf64 | `CONDITIONAL_JUMP`
<a id="insn-00babed0"></a> `00babed0` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00babed4"></a> `00babed4` | `88 8e 40 f8` | ldr x8,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00babed8"></a> `00babed8` | `68 04 00 b4` | cbz x8,0x00babf64 | `CONDITIONAL_JUMP`
<a id="insn-00babedc"></a> `00babedc` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00babee0"></a> `00babee0` | `fa 03 17 aa` | mov x26,x23 | `FALL_THROUGH`
<a id="insn-00babee4"></a> `00babee4` | `5b 0f 42 38` | ldrb w27,[x26, #0x20]! | `FALL_THROUGH`
<a id="insn-00babee8"></a> `00babee8` | `48 07 40 f9` | ldr x8,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00babeec"></a> `00babeec` | `69 ff 41 d3` | lsr x9,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00babef0"></a> `00babef0` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00babef4"></a> `00babef4` | `39 01 88 9a` | csel x25,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00babef8"></a> `00babef8` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00babefc"></a> `00babefc` | `36 33 98 9a` | csel x22,x25,x24,cc | `FALL_THROUGH`
<a id="insn-00babf00"></a> `00babf00` | `56 01 00 b4` | cbz x22,0x00babf28 | `CONDITIONAL_JUMP`
<a id="insn-00babf04"></a> `00babf04` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00babf08"></a> `00babf08` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00babf0c"></a> `00babf0c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00babf10"></a> `00babf10` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00babf14"></a> `00babf14` | `81 17 9a 9a` | csinc x1,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00babf18"></a> `00babf18` | `4e b0 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00babf1c"></a> `00babf1c` | `60 00 00 34` | cbz w0,0x00babf28 | `CONDITIONAL_JUMP`
<a id="insn-00babf20"></a> `00babf20` | `80 00 f8 37` | tbnz w0,#0x1f,0x00babf30 | `CONDITIONAL_JUMP`
<a id="insn-00babf24"></a> `00babf24` | `09 00 00 14` | b 0x00babf48 | `UNCONDITIONAL_JUMP`
<a id="insn-00babf28"></a> `00babf28` | `1f 03 19 eb` | cmp x24,x25 | `FALL_THROUGH`
<a id="insn-00babf2c"></a> `00babf2c` | `a2 00 00 54` | b.cs 0x00babf40 | `CONDITIONAL_JUMP`
<a id="insn-00babf30"></a> `00babf30` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00babf34"></a> `00babf34` | `08 02 00 b4` | cbz x8,0x00babf74 | `CONDITIONAL_JUMP`
<a id="insn-00babf38"></a> `00babf38` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00babf3c"></a> `00babf3c` | `e8 ff ff 17` | b 0x00babedc | `UNCONDITIONAL_JUMP`
<a id="insn-00babf40"></a> `00babf40` | `56 fc ff b4` | cbz x22,0x00babec8 | `CONDITIONAL_JUMP`
<a id="insn-00babf44"></a> `00babf44` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00babf48"></a> `00babf48` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00babf4c"></a> `00babf4c` | `80 17 9a 9a` | csinc x0,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00babf50"></a> `00babf50` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00babf54"></a> `00babf54` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00babf58"></a> `00babf58` | `3e b0 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00babf5c"></a> `00babf5c` | `60 fb ff 34` | cbz w0,0x00babec8 | `CONDITIONAL_JUMP`
<a id="insn-00babf60"></a> `00babf60` | `80 fb ff 37` | tbnz w0,#0x1f,0x00babed0 | `CONDITIONAL_JUMP`
<a id="insn-00babf64"></a> `00babf64` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00babf68"></a> `00babf68` | `05 00 00 14` | b 0x00babf7c | `UNCONDITIONAL_JUMP`
<a id="insn-00babf6c"></a> `00babf6c` | `74 02 00 f9` | str x20,[x19] | `FALL_THROUGH`
<a id="insn-00babf70"></a> `00babf70` | `03 00 00 14` | b 0x00babf7c | `UNCONDITIONAL_JUMP`
<a id="insn-00babf74"></a> `00babf74` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00babf78"></a> `00babf78` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00babf7c"></a> `00babf7c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00babf80"></a> `00babf80` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00babf84"></a> `00babf84` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00babf88"></a> `00babf88` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00babf8c"></a> `00babf8c` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00babf90"></a> `00babf90` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00babf94"></a> `00babf94` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00babf98"></a> `00babf98` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00babe7c`](#insn-00babe7c) 範囲 `[['00babe7c', '00babe83']]`
  - `FALL_THROUGH` [`00babe80`](#insn-00babe80) → [`00babe84`](#insn-00babe84)
- ブロック [`00babe84`](#insn-00babe84) 範囲 `[['00babe84', '00babe87']]`
  - `FALL_THROUGH` [`00babe84`](#insn-00babe84) → [`00babe88`](#insn-00babe88)
- ブロック [`00babe88`](#insn-00babe88) 範囲 `[['00babe88', '00babe97']]`
  - `FALL_THROUGH` [`00babe94`](#insn-00babe94) → [`00babe98`](#insn-00babe98)
- ブロック [`00babe98`](#insn-00babe98) 範囲 `[['00babe98', '00babe9b']]`
  - `FALL_THROUGH` [`00babe98`](#insn-00babe98) → [`00babe9c`](#insn-00babe9c)
- ブロック [`00babe9c`](#insn-00babe9c) 範囲 `[['00babe9c', '00babea7']]`
  - `CONDITIONAL_JUMP` [`00babea4`](#insn-00babea4) → [`00babf6c`](#insn-00babf6c)
  - `FALL_THROUGH` [`00babea4`](#insn-00babea4) → [`00babea8`](#insn-00babea8)
- ブロック [`00babea8`](#insn-00babea8) 範囲 `[['00babea8', '00babeab']]`
  - `FALL_THROUGH` [`00babea8`](#insn-00babea8) → [`00babeac`](#insn-00babeac)
- ブロック [`00babeac`](#insn-00babeac) 範囲 `[['00babeac', '00babeaf']]`
  - `FALL_THROUGH` [`00babeac`](#insn-00babeac) → [`00babeb0`](#insn-00babeb0)
- ブロック [`00babeb0`](#insn-00babeb0) 範囲 `[['00babeb0', '00babeb3']]`
  - `FALL_THROUGH` [`00babeb0`](#insn-00babeb0) → [`00babeb4`](#insn-00babeb4)
- ブロック [`00babeb4`](#insn-00babeb4) 範囲 `[['00babeb4', '00babeb7']]`
  - `FALL_THROUGH` [`00babeb4`](#insn-00babeb4) → [`00babeb8`](#insn-00babeb8)
- ブロック [`00babeb8`](#insn-00babeb8) 範囲 `[['00babeb8', '00babebb']]`
  - `FALL_THROUGH` [`00babeb8`](#insn-00babeb8) → [`00babebc`](#insn-00babebc)
- ブロック [`00babebc`](#insn-00babebc) 範囲 `[['00babebc', '00babec7']]`
  - `UNCONDITIONAL_JUMP` [`00babec4`](#insn-00babec4) → [`00babee0`](#insn-00babee0)
- ブロック [`00babec8`](#insn-00babec8) 範囲 `[['00babec8', '00babecb']]`
  - `FALL_THROUGH` [`00babec8`](#insn-00babec8) → [`00babecc`](#insn-00babecc)
- ブロック [`00babecc`](#insn-00babecc) 範囲 `[['00babecc', '00babecf']]`
  - `CONDITIONAL_JUMP` [`00babecc`](#insn-00babecc) → [`00babf64`](#insn-00babf64)
  - `FALL_THROUGH` [`00babecc`](#insn-00babecc) → [`00babed0`](#insn-00babed0)
- ブロック [`00babed0`](#insn-00babed0) 範囲 `[['00babed0', '00babedb']]`
  - `CONDITIONAL_JUMP` [`00babed8`](#insn-00babed8) → [`00babf64`](#insn-00babf64)
  - `FALL_THROUGH` [`00babed8`](#insn-00babed8) → [`00babedc`](#insn-00babedc)
- ブロック [`00babedc`](#insn-00babedc) 範囲 `[['00babedc', '00babedf']]`
  - `FALL_THROUGH` [`00babedc`](#insn-00babedc) → [`00babee0`](#insn-00babee0)
- ブロック [`00babee0`](#insn-00babee0) 範囲 `[['00babee0', '00babeeb']]`
  - `FALL_THROUGH` [`00babee8`](#insn-00babee8) → [`00babeec`](#insn-00babeec)
- ブロック [`00babeec`](#insn-00babeec) 範囲 `[['00babeec', '00babefb']]`
  - `FALL_THROUGH` [`00babef8`](#insn-00babef8) → [`00babefc`](#insn-00babefc)
- ブロック [`00babefc`](#insn-00babefc) 範囲 `[['00babefc', '00babeff']]`
  - `FALL_THROUGH` [`00babefc`](#insn-00babefc) → [`00babf00`](#insn-00babf00)
- ブロック [`00babf00`](#insn-00babf00) 範囲 `[['00babf00', '00babf03']]`
  - `CONDITIONAL_JUMP` [`00babf00`](#insn-00babf00) → [`00babf28`](#insn-00babf28)
  - `FALL_THROUGH` [`00babf00`](#insn-00babf00) → [`00babf04`](#insn-00babf04)
- ブロック [`00babf04`](#insn-00babf04) 範囲 `[['00babf04', '00babf07']]`
  - `FALL_THROUGH` [`00babf04`](#insn-00babf04) → [`00babf08`](#insn-00babf08)
- ブロック [`00babf08`](#insn-00babf08) 範囲 `[['00babf08', '00babf0b']]`
  - `FALL_THROUGH` [`00babf08`](#insn-00babf08) → [`00babf0c`](#insn-00babf0c)
- ブロック [`00babf0c`](#insn-00babf0c) 範囲 `[['00babf0c', '00babf1b']]`
  - `FALL_THROUGH` [`00babf18`](#insn-00babf18) → [`00babf1c`](#insn-00babf1c)
- ブロック [`00babf1c`](#insn-00babf1c) 範囲 `[['00babf1c', '00babf1f']]`
  - `CONDITIONAL_JUMP` [`00babf1c`](#insn-00babf1c) → [`00babf28`](#insn-00babf28)
  - `FALL_THROUGH` [`00babf1c`](#insn-00babf1c) → [`00babf20`](#insn-00babf20)
- ブロック [`00babf20`](#insn-00babf20) 範囲 `[['00babf20', '00babf23']]`
  - `CONDITIONAL_JUMP` [`00babf20`](#insn-00babf20) → [`00babf30`](#insn-00babf30)
  - `FALL_THROUGH` [`00babf20`](#insn-00babf20) → [`00babf24`](#insn-00babf24)
- ブロック [`00babf24`](#insn-00babf24) 範囲 `[['00babf24', '00babf27']]`
  - `UNCONDITIONAL_JUMP` [`00babf24`](#insn-00babf24) → [`00babf48`](#insn-00babf48)
- ブロック [`00babf28`](#insn-00babf28) 範囲 `[['00babf28', '00babf2b']]`
  - `FALL_THROUGH` [`00babf28`](#insn-00babf28) → [`00babf2c`](#insn-00babf2c)
- ブロック [`00babf2c`](#insn-00babf2c) 範囲 `[['00babf2c', '00babf2f']]`
  - `CONDITIONAL_JUMP` [`00babf2c`](#insn-00babf2c) → [`00babf40`](#insn-00babf40)
  - `FALL_THROUGH` [`00babf2c`](#insn-00babf2c) → [`00babf30`](#insn-00babf30)
- ブロック [`00babf30`](#insn-00babf30) 範囲 `[['00babf30', '00babf37']]`
  - `CONDITIONAL_JUMP` [`00babf34`](#insn-00babf34) → [`00babf74`](#insn-00babf74)
  - `FALL_THROUGH` [`00babf34`](#insn-00babf34) → [`00babf38`](#insn-00babf38)
- ブロック [`00babf38`](#insn-00babf38) 範囲 `[['00babf38', '00babf3b']]`
  - `FALL_THROUGH` [`00babf38`](#insn-00babf38) → [`00babf3c`](#insn-00babf3c)
- ブロック [`00babf3c`](#insn-00babf3c) 範囲 `[['00babf3c', '00babf3f']]`
  - `UNCONDITIONAL_JUMP` [`00babf3c`](#insn-00babf3c) → [`00babedc`](#insn-00babedc)
- ブロック [`00babf40`](#insn-00babf40) 範囲 `[['00babf40', '00babf43']]`
  - `CONDITIONAL_JUMP` [`00babf40`](#insn-00babf40) → [`00babec8`](#insn-00babec8)
  - `FALL_THROUGH` [`00babf40`](#insn-00babf40) → [`00babf44`](#insn-00babf44)
- ブロック [`00babf44`](#insn-00babf44) 範囲 `[['00babf44', '00babf47']]`
  - `FALL_THROUGH` [`00babf44`](#insn-00babf44) → [`00babf48`](#insn-00babf48)
- ブロック [`00babf48`](#insn-00babf48) 範囲 `[['00babf48', '00babf4b']]`
  - `FALL_THROUGH` [`00babf48`](#insn-00babf48) → [`00babf4c`](#insn-00babf4c)
- ブロック [`00babf4c`](#insn-00babf4c) 範囲 `[['00babf4c', '00babf4f']]`
  - `FALL_THROUGH` [`00babf4c`](#insn-00babf4c) → [`00babf50`](#insn-00babf50)
- ブロック [`00babf50`](#insn-00babf50) 範囲 `[['00babf50', '00babf53']]`
  - `FALL_THROUGH` [`00babf50`](#insn-00babf50) → [`00babf54`](#insn-00babf54)
- ブロック [`00babf54`](#insn-00babf54) 範囲 `[['00babf54', '00babf57']]`
  - `FALL_THROUGH` [`00babf54`](#insn-00babf54) → [`00babf58`](#insn-00babf58)
- ブロック [`00babf58`](#insn-00babf58) 範囲 `[['00babf58', '00babf5b']]`
  - `FALL_THROUGH` [`00babf58`](#insn-00babf58) → [`00babf5c`](#insn-00babf5c)
- ブロック [`00babf5c`](#insn-00babf5c) 範囲 `[['00babf5c', '00babf5f']]`
  - `CONDITIONAL_JUMP` [`00babf5c`](#insn-00babf5c) → [`00babec8`](#insn-00babec8)
  - `FALL_THROUGH` [`00babf5c`](#insn-00babf5c) → [`00babf60`](#insn-00babf60)
- ブロック [`00babf60`](#insn-00babf60) 範囲 `[['00babf60', '00babf63']]`
  - `CONDITIONAL_JUMP` [`00babf60`](#insn-00babf60) → [`00babed0`](#insn-00babed0)
  - `FALL_THROUGH` [`00babf60`](#insn-00babf60) → [`00babf64`](#insn-00babf64)
- ブロック [`00babf64`](#insn-00babf64) 範囲 `[['00babf64', '00babf6b']]`
  - `UNCONDITIONAL_JUMP` [`00babf68`](#insn-00babf68) → [`00babf7c`](#insn-00babf7c)
- ブロック [`00babf6c`](#insn-00babf6c) 範囲 `[['00babf6c', '00babf73']]`
  - `UNCONDITIONAL_JUMP` [`00babf70`](#insn-00babf70) → [`00babf7c`](#insn-00babf7c)
- ブロック [`00babf74`](#insn-00babf74) 範囲 `[['00babf74', '00babf7b']]`
  - `FALL_THROUGH` [`00babf78`](#insn-00babf78) → [`00babf7c`](#insn-00babf7c)
- ブロック [`00babf7c`](#insn-00babf7c) 範囲 `[['00babf7c', '00babf8b']]`
  - `FALL_THROUGH` [`00babf88`](#insn-00babf88) → [`00babf8c`](#insn-00babf8c)
- ブロック [`00babf8c`](#insn-00babf8c) 範囲 `[['00babf8c', '00babf9b']]`

## 命令位置別の参照

- [`00babe7c`](#insn-00babe7c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babe80`](#insn-00babe80) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babe84`](#insn-00babe84) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babe88`](#insn-00babe88) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babe8c`](#insn-00babe8c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babe90`](#insn-00babe90) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babea4`](#insn-00babea4) → [`00babf6c`](#insn-00babf6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babec4`](#insn-00babec4) → [`00babee0`](#insn-00babee0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babecc`](#insn-00babecc) → [`00babf64`](#insn-00babf64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babed8`](#insn-00babed8) → [`00babf64`](#insn-00babf64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf00`](#insn-00babf00) → [`00babf28`](#insn-00babf28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf18`](#insn-00babf18) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00babf1c`](#insn-00babf1c) → [`00babf28`](#insn-00babf28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf20`](#insn-00babf20) → [`00babf30`](#insn-00babf30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf24`](#insn-00babf24) → [`00babf48`](#insn-00babf48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf2c`](#insn-00babf2c) → [`00babf40`](#insn-00babf40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf34`](#insn-00babf34) → [`00babf74`](#insn-00babf74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf3c`](#insn-00babf3c) → [`00babedc`](#insn-00babedc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf40`](#insn-00babf40) → [`00babec8`](#insn-00babec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf58`](#insn-00babf58) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00babf5c`](#insn-00babf5c) → [`00babec8`](#insn-00babec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf60`](#insn-00babf60) → [`00babed0`](#insn-00babed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf68`](#insn-00babf68) → [`00babf7c`](#insn-00babf7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf70`](#insn-00babf70) → [`00babf7c`](#insn-00babf7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf80`](#insn-00babf80) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf84`](#insn-00babf84) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf88`](#insn-00babf88) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf8c`](#insn-00babf8c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf90`](#insn-00babf90) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00babe7c`](#insn-00babe7c)

~~~json
{
  "source": "00babe7c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babe80`](#insn-00babe80)

~~~json
{
  "source": "00babe80",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babe84`](#insn-00babe84)

~~~json
{
  "source": "00babe84",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babe88`](#insn-00babe88)

~~~json
{
  "source": "00babe88",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babe8c`](#insn-00babe8c)

~~~json
{
  "source": "00babe8c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babe90`](#insn-00babe90)

~~~json
{
  "source": "00babe90",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babea4`](#insn-00babea4)

~~~json
{
  "source": "00babea4",
  "target": "00babf6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babec4`](#insn-00babec4)

~~~json
{
  "source": "00babec4",
  "target": "00babee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babecc`](#insn-00babecc)

~~~json
{
  "source": "00babecc",
  "target": "00babf64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babed8`](#insn-00babed8)

~~~json
{
  "source": "00babed8",
  "target": "00babf64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf00`](#insn-00babf00)

~~~json
{
  "source": "00babf00",
  "target": "00babf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf18`](#insn-00babf18)

~~~json
{
  "source": "00babf18",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babf1c`](#insn-00babf1c)

~~~json
{
  "source": "00babf1c",
  "target": "00babf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf20`](#insn-00babf20)

~~~json
{
  "source": "00babf20",
  "target": "00babf30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf24`](#insn-00babf24)

~~~json
{
  "source": "00babf24",
  "target": "00babf48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf2c`](#insn-00babf2c)

~~~json
{
  "source": "00babf2c",
  "target": "00babf40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf34`](#insn-00babf34)

~~~json
{
  "source": "00babf34",
  "target": "00babf74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf3c`](#insn-00babf3c)

~~~json
{
  "source": "00babf3c",
  "target": "00babedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf40`](#insn-00babf40)

~~~json
{
  "source": "00babf40",
  "target": "00babec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf58`](#insn-00babf58)

~~~json
{
  "source": "00babf58",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babf5c`](#insn-00babf5c)

~~~json
{
  "source": "00babf5c",
  "target": "00babec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf60`](#insn-00babf60)

~~~json
{
  "source": "00babf60",
  "target": "00babed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf68`](#insn-00babf68)

~~~json
{
  "source": "00babf68",
  "target": "00babf7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf70`](#insn-00babf70)

~~~json
{
  "source": "00babf70",
  "target": "00babf7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf80`](#insn-00babf80)

~~~json
{
  "source": "00babf80",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf84`](#insn-00babf84)

~~~json
{
  "source": "00babf84",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf88`](#insn-00babf88)

~~~json
{
  "source": "00babf88",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf8c`](#insn-00babf8c)

~~~json
{
  "source": "00babf8c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf90`](#insn-00babf90)

~~~json
{
  "source": "00babf90",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
