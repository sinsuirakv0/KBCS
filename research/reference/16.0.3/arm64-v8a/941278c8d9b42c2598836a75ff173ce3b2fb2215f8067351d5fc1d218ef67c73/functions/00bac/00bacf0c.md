# 00bacf0c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00babf18`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bab/00babf18.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-3c1621421885baba8b6efc1d48f1aa18)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bacf0c",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0cba7ac6ae23aeee96b33b6a5c331da7312a356356d67126b50ef94f6cbd4525",
  "source_text_sha256": "0cba7ac6ae23aeee96b33b6a5c331da7312a356356d67126b50ef94f6cbd4525",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bacf0c",
        "00bad02b"
      ]
    ],
    "bytes_sha256": "fa735bcc1039e5c78256bfd85fda24dbcf3f071bbd43d237543f3e59863f874e",
    "instruction_count": 72,
    "instruction_bytes": 288,
    "body_bytes": 288,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5e020](../00c5e/00c5e020.md)

## 呼び出し先

- [00c590f0](../00c59/00c590f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4283 bytes

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
  
                    /* catch() { ... } // from try @ 00baba88 with catch @ 00bacf10 */
                    /* catch() { ... } // from try @ 00bab8ec with catch @ 00bacf14 */
                    /* catch() { ... } // from try @ 00bab690 with catch @ 00bacf18 */
                    /* catch() { ... } // from try @ 00baaea8 with catch @ 00bacf1c */
                    /* catch() { ... } // from try @ 00baba64 with catch @ 00bacf20 */
  plVar5 = (long *)(param_1 + 8);
  plVar6 = (long *)*plVar5;
                    /* catch() { ... } // from try @ 00bab8c8 with catch @ 00bacf30 */
  if (plVar6 == (long *)0x0) {
    *param_2 = plVar5;
                    /* catch() { ... } // from try @ 00bab80c with catch @ 00bad020 */
    return plVar5;
                    /* catch() { ... } // from try @ 00bab9a8 with catch @ 00bad000 */
  }
  uVar2 = *(ulong *)(param_3 + 8);
  __s1 = *(byte **)(param_3 + 0x10);
                    /* catch() { ... } // from try @ 00bab66c with catch @ 00bacf40 */
  plVar5 = (long *)(param_1 + 8);
  if ((*param_3 & 1) == 0) {
                    /* catch() { ... } // from try @ 00baae88 with catch @ 00bacf50 */
    __s1 = param_3 + 1;
    uVar2 = (ulong)(*param_3 >> 1);
  }
  do {
    while( true ) {
                    /* catch() { ... } // from try @ 00baba14 with catch @ 00bacf70 */
      plVar7 = plVar6;
      bVar3 = *(byte *)(plVar7 + 4);
                    /* catch() { ... } // from try @ 00bab878 with catch @ 00bacf80 */
      uVar1 = (ulong)(bVar3 >> 1);
      if ((bVar3 & 1) != 0) {
        uVar1 = plVar7[5];
      }
      __n = uVar1;
      if (uVar2 <= uVar1) {
        __n = uVar2;
      }
                    /* catch() { ... } // from try @ 00bab61c with catch @ 00bacf90 */
      if (__n == 0) break;
      __s1_00 = (void *)plVar7[6];
      __s2 = __s1_00;
                    /* catch() { ... } // from try @ 00baae38 with catch @ 00bacfa0 */
      if ((bVar3 & 1) == 0) {
        __s2 = (void *)((long)plVar7 + 0x21);
      }
      iVar4 = memcmp(__s1,__s2,__n);
      if (iVar4 == 0) break;
                    /* catch() { ... } // from try @ 00bab9e8 with catch @ 00bacfb0 */
      if (iVar4 < 0) goto LAB_00bacfc0;
LAB_00bacfd8:
      if ((bVar3 & 1) == 0) {
        __s1_00 = (void *)((long)plVar7 + 0x21);
      }
                    /* catch() { ... } // from try @ 00bab5d0 with catch @ 00bacfe0 */
      iVar4 = memcmp(__s1_00,__s1,__n);
      if (iVar4 == 0) goto LAB_00bacf58;
                    /* catch() { ... } // from try @ 00baadec with catch @ 00bacff0 */
      if (-1 < iVar4) goto LAB_00bacff4;
LAB_00bacf60:
      plVar5 = plVar7 + 1;
                    /* catch() { ... } // from try @ 00baba38 with catch @ 00bacf60 */
                    /* catch() { ... } // from try @ 00bab89c with catch @ 00bacf64 */
                    /* catch() { ... } // from try @ 00bab640 with catch @ 00bacf68 */
      plVar6 = (long *)*plVar5;
      if ((long *)*plVar5 == (long *)0x0) {
LAB_00bacff4:
        *param_2 = plVar7;
        return plVar5;
      }
    }
                    /* catch() { ... } // from try @ 00bab5f0 with catch @ 00bacfb8 */
                    /* catch() { ... } // from try @ 00baae0c with catch @ 00bacfbc */
    if (uVar1 <= uVar2) {
                    /* catch() { ... } // from try @ 00bab82c with catch @ 00bacfd0 */
      if (__n != 0) {
        __s1_00 = (void *)plVar7[6];
        goto LAB_00bacfd8;
      }
LAB_00bacf58:
      if (uVar2 <= uVar1) goto LAB_00bacff4;
      goto LAB_00bacf60;
    }
LAB_00bacfc0:
                    /* catch() { ... } // from try @ 00bab9c8 with catch @ 00bacfc0 */
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
<a id="insn-00bacf0c"></a> `00bacf0c` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00bacf10"></a> `00bacf10` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bacf14"></a> `00bacf14` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bacf18"></a> `00bacf18` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bacf1c"></a> `00bacf1c` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bacf20"></a> `00bacf20` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bacf24"></a> `00bacf24` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bacf28"></a> `00bacf28` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bacf2c"></a> `00bacf2c` | `97 8e 40 f8` | ldr x23,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00bacf30"></a> `00bacf30` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bacf34"></a> `00bacf34` | `57 06 00 b4` | cbz x23,0x00bacffc | `CONDITIONAL_JUMP`
<a id="insn-00bacf38"></a> `00bacf38` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00bacf3c"></a> `00bacf3c` | `49 a8 40 a9` | ldp x9,x10,[x2, #0x8] | `FALL_THROUGH`
<a id="insn-00bacf40"></a> `00bacf40` | `14 20 00 91` | add x20,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bacf44"></a> `00bacf44` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacf48"></a> `00bacf48` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bacf4c"></a> `00bacf4c` | `78 01 89 9a` | csel x24,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00bacf50"></a> `00bacf50` | `55 15 82 9a` | csinc x21,x10,x2,ne | `FALL_THROUGH`
<a id="insn-00bacf54"></a> `00bacf54` | `07 00 00 14` | b 0x00bacf70 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacf58"></a> `00bacf58` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00bacf5c"></a> `00bacf5c` | `c2 04 00 54` | b.cs 0x00bacff4 | `CONDITIONAL_JUMP`
<a id="insn-00bacf60"></a> `00bacf60` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00bacf64"></a> `00bacf64` | `88 8e 40 f8` | ldr x8,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00bacf68"></a> `00bacf68` | `68 04 00 b4` | cbz x8,0x00bacff4 | `CONDITIONAL_JUMP`
<a id="insn-00bacf6c"></a> `00bacf6c` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00bacf70"></a> `00bacf70` | `fa 03 17 aa` | mov x26,x23 | `FALL_THROUGH`
<a id="insn-00bacf74"></a> `00bacf74` | `5b 0f 42 38` | ldrb w27,[x26, #0x20]! | `FALL_THROUGH`
<a id="insn-00bacf78"></a> `00bacf78` | `48 07 40 f9` | ldr x8,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00bacf7c"></a> `00bacf7c` | `69 ff 41 d3` | lsr x9,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00bacf80"></a> `00bacf80` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00bacf84"></a> `00bacf84` | `39 01 88 9a` | csel x25,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00bacf88"></a> `00bacf88` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00bacf8c"></a> `00bacf8c` | `36 33 98 9a` | csel x22,x25,x24,cc | `FALL_THROUGH`
<a id="insn-00bacf90"></a> `00bacf90` | `56 01 00 b4` | cbz x22,0x00bacfb8 | `CONDITIONAL_JUMP`
<a id="insn-00bacf94"></a> `00bacf94` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00bacf98"></a> `00bacf98` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00bacf9c"></a> `00bacf9c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bacfa0"></a> `00bacfa0` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bacfa4"></a> `00bacfa4` | `81 17 9a 9a` | csinc x1,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00bacfa8"></a> `00bacfa8` | `52 b0 02 94` | bl 0x00c590f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bacfac"></a> `00bacfac` | `60 00 00 34` | cbz w0,0x00bacfb8 | `CONDITIONAL_JUMP`
<a id="insn-00bacfb0"></a> `00bacfb0` | `80 00 f8 37` | tbnz w0,#0x1f,0x00bacfc0 | `CONDITIONAL_JUMP`
<a id="insn-00bacfb4"></a> `00bacfb4` | `09 00 00 14` | b 0x00bacfd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacfb8"></a> `00bacfb8` | `1f 03 19 eb` | cmp x24,x25 | `FALL_THROUGH`
<a id="insn-00bacfbc"></a> `00bacfbc` | `a2 00 00 54` | b.cs 0x00bacfd0 | `CONDITIONAL_JUMP`
<a id="insn-00bacfc0"></a> `00bacfc0` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00bacfc4"></a> `00bacfc4` | `08 02 00 b4` | cbz x8,0x00bad004 | `CONDITIONAL_JUMP`
<a id="insn-00bacfc8"></a> `00bacfc8` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00bacfcc"></a> `00bacfcc` | `e8 ff ff 17` | b 0x00bacf6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bacfd0"></a> `00bacfd0` | `56 fc ff b4` | cbz x22,0x00bacf58 | `CONDITIONAL_JUMP`
<a id="insn-00bacfd4"></a> `00bacfd4` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00bacfd8"></a> `00bacfd8` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00bacfdc"></a> `00bacfdc` | `80 17 9a 9a` | csinc x0,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00bacfe0"></a> `00bacfe0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bacfe4"></a> `00bacfe4` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bacfe8"></a> `00bacfe8` | `42 b0 02 94` | bl 0x00c590f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bacfec"></a> `00bacfec` | `60 fb ff 34` | cbz w0,0x00bacf58 | `CONDITIONAL_JUMP`
<a id="insn-00bacff0"></a> `00bacff0` | `80 fb ff 37` | tbnz w0,#0x1f,0x00bacf60 | `CONDITIONAL_JUMP`
<a id="insn-00bacff4"></a> `00bacff4` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00bacff8"></a> `00bacff8` | `05 00 00 14` | b 0x00bad00c | `UNCONDITIONAL_JUMP`
<a id="insn-00bacffc"></a> `00bacffc` | `74 02 00 f9` | str x20,[x19] | `FALL_THROUGH`
<a id="insn-00bad000"></a> `00bad000` | `03 00 00 14` | b 0x00bad00c | `UNCONDITIONAL_JUMP`
<a id="insn-00bad004"></a> `00bad004` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00bad008"></a> `00bad008` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00bad00c"></a> `00bad00c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bad010"></a> `00bad010` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bad014"></a> `00bad014` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bad018"></a> `00bad018` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bad01c"></a> `00bad01c` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bad020"></a> `00bad020` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bad024"></a> `00bad024` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00bad028"></a> `00bad028` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bacf0c`](#insn-00bacf0c) 範囲 `[['00bacf0c', '00bacf0f']]`
  - `FALL_THROUGH` [`00bacf0c`](#insn-00bacf0c) → [`00bacf10`](#insn-00bacf10)
- ブロック [`00bacf10`](#insn-00bacf10) 範囲 `[['00bacf10', '00bacf13']]`
  - `FALL_THROUGH` [`00bacf10`](#insn-00bacf10) → [`00bacf14`](#insn-00bacf14)
- ブロック [`00bacf14`](#insn-00bacf14) 範囲 `[['00bacf14', '00bacf17']]`
  - `FALL_THROUGH` [`00bacf14`](#insn-00bacf14) → [`00bacf18`](#insn-00bacf18)
- ブロック [`00bacf18`](#insn-00bacf18) 範囲 `[['00bacf18', '00bacf1b']]`
  - `FALL_THROUGH` [`00bacf18`](#insn-00bacf18) → [`00bacf1c`](#insn-00bacf1c)
- ブロック [`00bacf1c`](#insn-00bacf1c) 範囲 `[['00bacf1c', '00bacf1f']]`
  - `FALL_THROUGH` [`00bacf1c`](#insn-00bacf1c) → [`00bacf20`](#insn-00bacf20)
- ブロック [`00bacf20`](#insn-00bacf20) 範囲 `[['00bacf20', '00bacf2f']]`
  - `FALL_THROUGH` [`00bacf2c`](#insn-00bacf2c) → [`00bacf30`](#insn-00bacf30)
- ブロック [`00bacf30`](#insn-00bacf30) 範囲 `[['00bacf30', '00bacf37']]`
  - `CONDITIONAL_JUMP` [`00bacf34`](#insn-00bacf34) → [`00bacffc`](#insn-00bacffc)
  - `FALL_THROUGH` [`00bacf34`](#insn-00bacf34) → [`00bacf38`](#insn-00bacf38)
- ブロック [`00bacf38`](#insn-00bacf38) 範囲 `[['00bacf38', '00bacf3f']]`
  - `FALL_THROUGH` [`00bacf3c`](#insn-00bacf3c) → [`00bacf40`](#insn-00bacf40)
- ブロック [`00bacf40`](#insn-00bacf40) 範囲 `[['00bacf40', '00bacf4f']]`
  - `FALL_THROUGH` [`00bacf4c`](#insn-00bacf4c) → [`00bacf50`](#insn-00bacf50)
- ブロック [`00bacf50`](#insn-00bacf50) 範囲 `[['00bacf50', '00bacf57']]`
  - `UNCONDITIONAL_JUMP` [`00bacf54`](#insn-00bacf54) → [`00bacf70`](#insn-00bacf70)
- ブロック [`00bacf58`](#insn-00bacf58) 範囲 `[['00bacf58', '00bacf5f']]`
  - `CONDITIONAL_JUMP` [`00bacf5c`](#insn-00bacf5c) → [`00bacff4`](#insn-00bacff4)
  - `FALL_THROUGH` [`00bacf5c`](#insn-00bacf5c) → [`00bacf60`](#insn-00bacf60)
- ブロック [`00bacf60`](#insn-00bacf60) 範囲 `[['00bacf60', '00bacf63']]`
  - `FALL_THROUGH` [`00bacf60`](#insn-00bacf60) → [`00bacf64`](#insn-00bacf64)
- ブロック [`00bacf64`](#insn-00bacf64) 範囲 `[['00bacf64', '00bacf67']]`
  - `FALL_THROUGH` [`00bacf64`](#insn-00bacf64) → [`00bacf68`](#insn-00bacf68)
- ブロック [`00bacf68`](#insn-00bacf68) 範囲 `[['00bacf68', '00bacf6b']]`
  - `CONDITIONAL_JUMP` [`00bacf68`](#insn-00bacf68) → [`00bacff4`](#insn-00bacff4)
  - `FALL_THROUGH` [`00bacf68`](#insn-00bacf68) → [`00bacf6c`](#insn-00bacf6c)
- ブロック [`00bacf6c`](#insn-00bacf6c) 範囲 `[['00bacf6c', '00bacf6f']]`
  - `FALL_THROUGH` [`00bacf6c`](#insn-00bacf6c) → [`00bacf70`](#insn-00bacf70)
- ブロック [`00bacf70`](#insn-00bacf70) 範囲 `[['00bacf70', '00bacf7f']]`
  - `FALL_THROUGH` [`00bacf7c`](#insn-00bacf7c) → [`00bacf80`](#insn-00bacf80)
- ブロック [`00bacf80`](#insn-00bacf80) 範囲 `[['00bacf80', '00bacf8f']]`
  - `FALL_THROUGH` [`00bacf8c`](#insn-00bacf8c) → [`00bacf90`](#insn-00bacf90)
- ブロック [`00bacf90`](#insn-00bacf90) 範囲 `[['00bacf90', '00bacf93']]`
  - `CONDITIONAL_JUMP` [`00bacf90`](#insn-00bacf90) → [`00bacfb8`](#insn-00bacfb8)
  - `FALL_THROUGH` [`00bacf90`](#insn-00bacf90) → [`00bacf94`](#insn-00bacf94)
- ブロック [`00bacf94`](#insn-00bacf94) 範囲 `[['00bacf94', '00bacf9f']]`
  - `FALL_THROUGH` [`00bacf9c`](#insn-00bacf9c) → [`00bacfa0`](#insn-00bacfa0)
- ブロック [`00bacfa0`](#insn-00bacfa0) 範囲 `[['00bacfa0', '00bacfaf']]`
  - `CONDITIONAL_JUMP` [`00bacfac`](#insn-00bacfac) → [`00bacfb8`](#insn-00bacfb8)
  - `FALL_THROUGH` [`00bacfac`](#insn-00bacfac) → [`00bacfb0`](#insn-00bacfb0)
- ブロック [`00bacfb0`](#insn-00bacfb0) 範囲 `[['00bacfb0', '00bacfb3']]`
  - `CONDITIONAL_JUMP` [`00bacfb0`](#insn-00bacfb0) → [`00bacfc0`](#insn-00bacfc0)
  - `FALL_THROUGH` [`00bacfb0`](#insn-00bacfb0) → [`00bacfb4`](#insn-00bacfb4)
- ブロック [`00bacfb4`](#insn-00bacfb4) 範囲 `[['00bacfb4', '00bacfb7']]`
  - `UNCONDITIONAL_JUMP` [`00bacfb4`](#insn-00bacfb4) → [`00bacfd8`](#insn-00bacfd8)
- ブロック [`00bacfb8`](#insn-00bacfb8) 範囲 `[['00bacfb8', '00bacfbb']]`
  - `FALL_THROUGH` [`00bacfb8`](#insn-00bacfb8) → [`00bacfbc`](#insn-00bacfbc)
- ブロック [`00bacfbc`](#insn-00bacfbc) 範囲 `[['00bacfbc', '00bacfbf']]`
  - `CONDITIONAL_JUMP` [`00bacfbc`](#insn-00bacfbc) → [`00bacfd0`](#insn-00bacfd0)
  - `FALL_THROUGH` [`00bacfbc`](#insn-00bacfbc) → [`00bacfc0`](#insn-00bacfc0)
- ブロック [`00bacfc0`](#insn-00bacfc0) 範囲 `[['00bacfc0', '00bacfc7']]`
  - `CONDITIONAL_JUMP` [`00bacfc4`](#insn-00bacfc4) → [`00bad004`](#insn-00bad004)
  - `FALL_THROUGH` [`00bacfc4`](#insn-00bacfc4) → [`00bacfc8`](#insn-00bacfc8)
- ブロック [`00bacfc8`](#insn-00bacfc8) 範囲 `[['00bacfc8', '00bacfcf']]`
  - `UNCONDITIONAL_JUMP` [`00bacfcc`](#insn-00bacfcc) → [`00bacf6c`](#insn-00bacf6c)
- ブロック [`00bacfd0`](#insn-00bacfd0) 範囲 `[['00bacfd0', '00bacfd3']]`
  - `CONDITIONAL_JUMP` [`00bacfd0`](#insn-00bacfd0) → [`00bacf58`](#insn-00bacf58)
  - `FALL_THROUGH` [`00bacfd0`](#insn-00bacfd0) → [`00bacfd4`](#insn-00bacfd4)
- ブロック [`00bacfd4`](#insn-00bacfd4) 範囲 `[['00bacfd4', '00bacfd7']]`
  - `FALL_THROUGH` [`00bacfd4`](#insn-00bacfd4) → [`00bacfd8`](#insn-00bacfd8)
- ブロック [`00bacfd8`](#insn-00bacfd8) 範囲 `[['00bacfd8', '00bacfdf']]`
  - `FALL_THROUGH` [`00bacfdc`](#insn-00bacfdc) → [`00bacfe0`](#insn-00bacfe0)
- ブロック [`00bacfe0`](#insn-00bacfe0) 範囲 `[['00bacfe0', '00bacfef']]`
  - `CONDITIONAL_JUMP` [`00bacfec`](#insn-00bacfec) → [`00bacf58`](#insn-00bacf58)
  - `FALL_THROUGH` [`00bacfec`](#insn-00bacfec) → [`00bacff0`](#insn-00bacff0)
- ブロック [`00bacff0`](#insn-00bacff0) 範囲 `[['00bacff0', '00bacff3']]`
  - `CONDITIONAL_JUMP` [`00bacff0`](#insn-00bacff0) → [`00bacf60`](#insn-00bacf60)
  - `FALL_THROUGH` [`00bacff0`](#insn-00bacff0) → [`00bacff4`](#insn-00bacff4)
- ブロック [`00bacff4`](#insn-00bacff4) 範囲 `[['00bacff4', '00bacffb']]`
  - `UNCONDITIONAL_JUMP` [`00bacff8`](#insn-00bacff8) → [`00bad00c`](#insn-00bad00c)
- ブロック [`00bacffc`](#insn-00bacffc) 範囲 `[['00bacffc', '00bacfff']]`
  - `FALL_THROUGH` [`00bacffc`](#insn-00bacffc) → [`00bad000`](#insn-00bad000)
- ブロック [`00bad000`](#insn-00bad000) 範囲 `[['00bad000', '00bad003']]`
  - `UNCONDITIONAL_JUMP` [`00bad000`](#insn-00bad000) → [`00bad00c`](#insn-00bad00c)
- ブロック [`00bad004`](#insn-00bad004) 範囲 `[['00bad004', '00bad00b']]`
  - `FALL_THROUGH` [`00bad008`](#insn-00bad008) → [`00bad00c`](#insn-00bad00c)
- ブロック [`00bad00c`](#insn-00bad00c) 範囲 `[['00bad00c', '00bad01f']]`
  - `FALL_THROUGH` [`00bad01c`](#insn-00bad01c) → [`00bad020`](#insn-00bad020)
- ブロック [`00bad020`](#insn-00bad020) 範囲 `[['00bad020', '00bad02b']]`

## 命令位置別の参照

- [`00bacf0c`](#insn-00bacf0c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf10`](#insn-00bacf10) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf14`](#insn-00bacf14) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf18`](#insn-00bacf18) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf1c`](#insn-00bacf1c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf20`](#insn-00bacf20) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf34`](#insn-00bacf34) → [`00bacffc`](#insn-00bacffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf54`](#insn-00bacf54) → [`00bacf70`](#insn-00bacf70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf5c`](#insn-00bacf5c) → [`00bacff4`](#insn-00bacff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf68`](#insn-00bacf68) → [`00bacff4`](#insn-00bacff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacf90`](#insn-00bacf90) → [`00bacfb8`](#insn-00bacfb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacfa8`](#insn-00bacfa8) → [`00c590f0`](../00c59/00c590f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590f0` · 推定シンボル `None` · 推定型 `None`
- [`00bacfac`](#insn-00bacfac) → [`00bacfb8`](#insn-00bacfb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacfb0`](#insn-00bacfb0) → [`00bacfc0`](#insn-00bacfc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacfb4`](#insn-00bacfb4) → [`00bacfd8`](#insn-00bacfd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacfbc`](#insn-00bacfbc) → [`00bacfd0`](#insn-00bacfd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacfc4`](#insn-00bacfc4) → [`00bad004`](#insn-00bad004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacfcc`](#insn-00bacfcc) → [`00bacf6c`](#insn-00bacf6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacfd0`](#insn-00bacfd0) → [`00bacf58`](#insn-00bacf58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacfe8`](#insn-00bacfe8) → [`00c590f0`](../00c59/00c590f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590f0` · 推定シンボル `None` · 推定型 `None`
- [`00bacfec`](#insn-00bacfec) → [`00bacf58`](#insn-00bacf58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacff0`](#insn-00bacff0) → [`00bacf60`](#insn-00bacf60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacff8`](#insn-00bacff8) → [`00bad00c`](#insn-00bad00c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad000`](#insn-00bad000) → [`00bad00c`](#insn-00bad00c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad010`](#insn-00bad010) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad014`](#insn-00bad014) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad018`](#insn-00bad018) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad01c`](#insn-00bad01c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad020`](#insn-00bad020) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bacf0c`](#insn-00bacf0c)

~~~json
{
  "source": "00bacf0c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf10`](#insn-00bacf10)

~~~json
{
  "source": "00bacf10",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf14`](#insn-00bacf14)

~~~json
{
  "source": "00bacf14",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf18`](#insn-00bacf18)

~~~json
{
  "source": "00bacf18",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf1c`](#insn-00bacf1c)

~~~json
{
  "source": "00bacf1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf20`](#insn-00bacf20)

~~~json
{
  "source": "00bacf20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf34`](#insn-00bacf34)

~~~json
{
  "source": "00bacf34",
  "target": "00bacffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf54`](#insn-00bacf54)

~~~json
{
  "source": "00bacf54",
  "target": "00bacf70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf5c`](#insn-00bacf5c)

~~~json
{
  "source": "00bacf5c",
  "target": "00bacff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf68`](#insn-00bacf68)

~~~json
{
  "source": "00bacf68",
  "target": "00bacff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacf90`](#insn-00bacf90)

~~~json
{
  "source": "00bacf90",
  "target": "00bacfb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacfa8`](#insn-00bacfa8)

~~~json
{
  "source": "00bacfa8",
  "target": "00c590f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bacfac`](#insn-00bacfac)

~~~json
{
  "source": "00bacfac",
  "target": "00bacfb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacfb0`](#insn-00bacfb0)

~~~json
{
  "source": "00bacfb0",
  "target": "00bacfc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacfb4`](#insn-00bacfb4)

~~~json
{
  "source": "00bacfb4",
  "target": "00bacfd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacfbc`](#insn-00bacfbc)

~~~json
{
  "source": "00bacfbc",
  "target": "00bacfd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacfc4`](#insn-00bacfc4)

~~~json
{
  "source": "00bacfc4",
  "target": "00bad004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacfcc`](#insn-00bacfcc)

~~~json
{
  "source": "00bacfcc",
  "target": "00bacf6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacfd0`](#insn-00bacfd0)

~~~json
{
  "source": "00bacfd0",
  "target": "00bacf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacfe8`](#insn-00bacfe8)

~~~json
{
  "source": "00bacfe8",
  "target": "00c590f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bacfec`](#insn-00bacfec)

~~~json
{
  "source": "00bacfec",
  "target": "00bacf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacff0`](#insn-00bacff0)

~~~json
{
  "source": "00bacff0",
  "target": "00bacf60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacff8`](#insn-00bacff8)

~~~json
{
  "source": "00bacff8",
  "target": "00bad00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad000`](#insn-00bad000)

~~~json
{
  "source": "00bad000",
  "target": "00bad00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad010`](#insn-00bad010)

~~~json
{
  "source": "00bad010",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad014`](#insn-00bad014)

~~~json
{
  "source": "00bad014",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad018`](#insn-00bad018)

~~~json
{
  "source": "00bad018",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad01c`](#insn-00bad01c)

~~~json
{
  "source": "00bad01c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad020`](#insn-00bad020)

~~~json
{
  "source": "00bad020",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
