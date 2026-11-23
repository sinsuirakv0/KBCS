# 00afaaa4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afab6c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afab6c.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0002.md#compare-7ec817c705a2a0abaac241dc735e0513)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afaaa4",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDataENS_14default_deleteISB_EEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISQ_EERKT_",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "19a1845204c425822f4fe2287f76ed83defa261c334674375e3f9910fa7cc47d",
  "source_text_sha256": "19a1845204c425822f4fe2287f76ed83defa261c334674375e3f9910fa7cc47d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afaaa4",
        "00afabc3"
      ]
    ],
    "bytes_sha256": "8080368a04624a59f1db0707f61d6019d757b6207de3ecf39da96da51d72da42",
    "instruction_count": 72,
    "instruction_bytes": 288,
    "body_bytes": 288,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bde880](../00bde/00bde880.md)

## 呼び出し先

- [00bdb100](../00bdb/00bdb100.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2534 bytes

~~~c

long * _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDataENS_14default_deleteISB_EEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISQ_EERKT_
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
  
                    /* try { // try from 00afaab0 to 00bfaacf has its CatchHandler @ 00afff40 */
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
                    /* try { // try from 00afab48 to 00bfab4f has its CatchHandler @ 00aff51c */
      if (iVar4 < 0) goto LAB_00afab58;
LAB_00afab70:
      if ((bVar3 & 1) == 0) {
        __s1_00 = (void *)((long)plVar7 + 0x21);
      }
                    /* try { // try from 00afab78 to 00bfab8b has its CatchHandler @ 00aff518 */
      iVar4 = memcmp(__s1_00,__s1,__n);
      if (iVar4 == 0) goto LAB_00afaaf0;
      if (-1 < iVar4) goto LAB_00afab8c;
LAB_00afaaf8:
      plVar5 = plVar7 + 1;
      plVar6 = (long *)*plVar5;
      if ((long *)*plVar5 == (long *)0x0) {
LAB_00afab8c:
        *param_2 = plVar7;
        return plVar5;
      }
    }
    if (uVar1 <= uVar2) {
      if (__n != 0) {
        __s1_00 = (void *)plVar7[6];
        goto LAB_00afab70;
      }
LAB_00afaaf0:
      if (uVar2 <= uVar1) goto LAB_00afab8c;
      goto LAB_00afaaf8;
    }
LAB_00afab58:
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
<a id="insn-00afaaa4"></a> `00afaaa4` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00afaaa8"></a> `00afaaa8` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afaaac"></a> `00afaaac` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afaab0"></a> `00afaab0` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afaab4"></a> `00afaab4` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afaab8"></a> `00afaab8` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afaabc"></a> `00afaabc` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00afaac0"></a> `00afaac0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00afaac4"></a> `00afaac4` | `97 8e 40 f8` | ldr x23,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00afaac8"></a> `00afaac8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00afaacc"></a> `00afaacc` | `57 06 00 b4` | cbz x23,0x00afab94 | `CONDITIONAL_JUMP`
<a id="insn-00afaad0"></a> `00afaad0` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00afaad4"></a> `00afaad4` | `49 a8 40 a9` | ldp x9,x10,[x2, #0x8] | `FALL_THROUGH`
<a id="insn-00afaad8"></a> `00afaad8` | `14 20 00 91` | add x20,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00afaadc"></a> `00afaadc` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afaae0"></a> `00afaae0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afaae4"></a> `00afaae4` | `78 01 89 9a` | csel x24,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00afaae8"></a> `00afaae8` | `55 15 82 9a` | csinc x21,x10,x2,ne | `FALL_THROUGH`
<a id="insn-00afaaec"></a> `00afaaec` | `07 00 00 14` | b 0x00afab08 | `UNCONDITIONAL_JUMP`
<a id="insn-00afaaf0"></a> `00afaaf0` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00afaaf4"></a> `00afaaf4` | `c2 04 00 54` | b.cs 0x00afab8c | `CONDITIONAL_JUMP`
<a id="insn-00afaaf8"></a> `00afaaf8` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00afaafc"></a> `00afaafc` | `88 8e 40 f8` | ldr x8,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00afab00"></a> `00afab00` | `68 04 00 b4` | cbz x8,0x00afab8c | `CONDITIONAL_JUMP`
<a id="insn-00afab04"></a> `00afab04` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00afab08"></a> `00afab08` | `fa 03 17 aa` | mov x26,x23 | `FALL_THROUGH`
<a id="insn-00afab0c"></a> `00afab0c` | `5b 0f 42 38` | ldrb w27,[x26, #0x20]! | `FALL_THROUGH`
<a id="insn-00afab10"></a> `00afab10` | `48 07 40 f9` | ldr x8,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00afab14"></a> `00afab14` | `69 ff 41 d3` | lsr x9,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00afab18"></a> `00afab18` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00afab1c"></a> `00afab1c` | `39 01 88 9a` | csel x25,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00afab20"></a> `00afab20` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00afab24"></a> `00afab24` | `36 33 98 9a` | csel x22,x25,x24,cc | `FALL_THROUGH`
<a id="insn-00afab28"></a> `00afab28` | `56 01 00 b4` | cbz x22,0x00afab50 | `CONDITIONAL_JUMP`
<a id="insn-00afab2c"></a> `00afab2c` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00afab30"></a> `00afab30` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00afab34"></a> `00afab34` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afab38"></a> `00afab38` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00afab3c"></a> `00afab3c` | `81 17 9a 9a` | csinc x1,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00afab40"></a> `00afab40` | `70 81 03 94` | bl 0x00bdb100 | `UNCONDITIONAL_CALL`
<a id="insn-00afab44"></a> `00afab44` | `60 00 00 34` | cbz w0,0x00afab50 | `CONDITIONAL_JUMP`
<a id="insn-00afab48"></a> `00afab48` | `80 00 f8 37` | tbnz w0,#0x1f,0x00afab58 | `CONDITIONAL_JUMP`
<a id="insn-00afab4c"></a> `00afab4c` | `09 00 00 14` | b 0x00afab70 | `UNCONDITIONAL_JUMP`
<a id="insn-00afab50"></a> `00afab50` | `1f 03 19 eb` | cmp x24,x25 | `FALL_THROUGH`
<a id="insn-00afab54"></a> `00afab54` | `a2 00 00 54` | b.cs 0x00afab68 | `CONDITIONAL_JUMP`
<a id="insn-00afab58"></a> `00afab58` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00afab5c"></a> `00afab5c` | `08 02 00 b4` | cbz x8,0x00afab9c | `CONDITIONAL_JUMP`
<a id="insn-00afab60"></a> `00afab60` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00afab64"></a> `00afab64` | `e8 ff ff 17` | b 0x00afab04 | `UNCONDITIONAL_JUMP`
<a id="insn-00afab68"></a> `00afab68` | `56 fc ff b4` | cbz x22,0x00afaaf0 | `CONDITIONAL_JUMP`
<a id="insn-00afab6c"></a> `00afab6c` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00afab70"></a> `00afab70` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00afab74"></a> `00afab74` | `80 17 9a 9a` | csinc x0,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00afab78"></a> `00afab78` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00afab7c"></a> `00afab7c` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00afab80"></a> `00afab80` | `60 81 03 94` | bl 0x00bdb100 | `UNCONDITIONAL_CALL`
<a id="insn-00afab84"></a> `00afab84` | `60 fb ff 34` | cbz w0,0x00afaaf0 | `CONDITIONAL_JUMP`
<a id="insn-00afab88"></a> `00afab88` | `80 fb ff 37` | tbnz w0,#0x1f,0x00afaaf8 | `CONDITIONAL_JUMP`
<a id="insn-00afab8c"></a> `00afab8c` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00afab90"></a> `00afab90` | `05 00 00 14` | b 0x00afaba4 | `UNCONDITIONAL_JUMP`
<a id="insn-00afab94"></a> `00afab94` | `74 02 00 f9` | str x20,[x19] | `FALL_THROUGH`
<a id="insn-00afab98"></a> `00afab98` | `03 00 00 14` | b 0x00afaba4 | `UNCONDITIONAL_JUMP`
<a id="insn-00afab9c"></a> `00afab9c` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00afaba0"></a> `00afaba0` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00afaba4"></a> `00afaba4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afaba8"></a> `00afaba8` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afabac"></a> `00afabac` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afabb0"></a> `00afabb0` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afabb4"></a> `00afabb4` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afabb8"></a> `00afabb8` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afabbc"></a> `00afabbc` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00afabc0"></a> `00afabc0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afaaa4`](#insn-00afaaa4) 範囲 `[['00afaaa4', '00afaaaf']]`
  - `FALL_THROUGH` [`00afaaac`](#insn-00afaaac) → [`00afaab0`](#insn-00afaab0)
- ブロック [`00afaab0`](#insn-00afaab0) 範囲 `[['00afaab0', '00afaacf']]`
  - `CONDITIONAL_JUMP` [`00afaacc`](#insn-00afaacc) → [`00afab94`](#insn-00afab94)
  - `FALL_THROUGH` [`00afaacc`](#insn-00afaacc) → [`00afaad0`](#insn-00afaad0)
- ブロック [`00afaad0`](#insn-00afaad0) 範囲 `[['00afaad0', '00afaaef']]`
  - `UNCONDITIONAL_JUMP` [`00afaaec`](#insn-00afaaec) → [`00afab08`](#insn-00afab08)
- ブロック [`00afaaf0`](#insn-00afaaf0) 範囲 `[['00afaaf0', '00afaaf7']]`
  - `CONDITIONAL_JUMP` [`00afaaf4`](#insn-00afaaf4) → [`00afab8c`](#insn-00afab8c)
  - `FALL_THROUGH` [`00afaaf4`](#insn-00afaaf4) → [`00afaaf8`](#insn-00afaaf8)
- ブロック [`00afaaf8`](#insn-00afaaf8) 範囲 `[['00afaaf8', '00afab03']]`
  - `CONDITIONAL_JUMP` [`00afab00`](#insn-00afab00) → [`00afab8c`](#insn-00afab8c)
  - `FALL_THROUGH` [`00afab00`](#insn-00afab00) → [`00afab04`](#insn-00afab04)
- ブロック [`00afab04`](#insn-00afab04) 範囲 `[['00afab04', '00afab07']]`
  - `FALL_THROUGH` [`00afab04`](#insn-00afab04) → [`00afab08`](#insn-00afab08)
- ブロック [`00afab08`](#insn-00afab08) 範囲 `[['00afab08', '00afab2b']]`
  - `CONDITIONAL_JUMP` [`00afab28`](#insn-00afab28) → [`00afab50`](#insn-00afab50)
  - `FALL_THROUGH` [`00afab28`](#insn-00afab28) → [`00afab2c`](#insn-00afab2c)
- ブロック [`00afab2c`](#insn-00afab2c) 範囲 `[['00afab2c', '00afab47']]`
  - `CONDITIONAL_JUMP` [`00afab44`](#insn-00afab44) → [`00afab50`](#insn-00afab50)
  - `FALL_THROUGH` [`00afab44`](#insn-00afab44) → [`00afab48`](#insn-00afab48)
- ブロック [`00afab48`](#insn-00afab48) 範囲 `[['00afab48', '00afab4b']]`
  - `CONDITIONAL_JUMP` [`00afab48`](#insn-00afab48) → [`00afab58`](#insn-00afab58)
  - `FALL_THROUGH` [`00afab48`](#insn-00afab48) → [`00afab4c`](#insn-00afab4c)
- ブロック [`00afab4c`](#insn-00afab4c) 範囲 `[['00afab4c', '00afab4f']]`
  - `UNCONDITIONAL_JUMP` [`00afab4c`](#insn-00afab4c) → [`00afab70`](#insn-00afab70)
- ブロック [`00afab50`](#insn-00afab50) 範囲 `[['00afab50', '00afab57']]`
  - `CONDITIONAL_JUMP` [`00afab54`](#insn-00afab54) → [`00afab68`](#insn-00afab68)
  - `FALL_THROUGH` [`00afab54`](#insn-00afab54) → [`00afab58`](#insn-00afab58)
- ブロック [`00afab58`](#insn-00afab58) 範囲 `[['00afab58', '00afab5f']]`
  - `CONDITIONAL_JUMP` [`00afab5c`](#insn-00afab5c) → [`00afab9c`](#insn-00afab9c)
  - `FALL_THROUGH` [`00afab5c`](#insn-00afab5c) → [`00afab60`](#insn-00afab60)
- ブロック [`00afab60`](#insn-00afab60) 範囲 `[['00afab60', '00afab67']]`
  - `UNCONDITIONAL_JUMP` [`00afab64`](#insn-00afab64) → [`00afab04`](#insn-00afab04)
- ブロック [`00afab68`](#insn-00afab68) 範囲 `[['00afab68', '00afab6b']]`
  - `CONDITIONAL_JUMP` [`00afab68`](#insn-00afab68) → [`00afaaf0`](#insn-00afaaf0)
  - `FALL_THROUGH` [`00afab68`](#insn-00afab68) → [`00afab6c`](#insn-00afab6c)
- ブロック [`00afab6c`](#insn-00afab6c) 範囲 `[['00afab6c', '00afab6f']]`
  - `FALL_THROUGH` [`00afab6c`](#insn-00afab6c) → [`00afab70`](#insn-00afab70)
- ブロック [`00afab70`](#insn-00afab70) 範囲 `[['00afab70', '00afab77']]`
  - `FALL_THROUGH` [`00afab74`](#insn-00afab74) → [`00afab78`](#insn-00afab78)
- ブロック [`00afab78`](#insn-00afab78) 範囲 `[['00afab78', '00afab87']]`
  - `CONDITIONAL_JUMP` [`00afab84`](#insn-00afab84) → [`00afaaf0`](#insn-00afaaf0)
  - `FALL_THROUGH` [`00afab84`](#insn-00afab84) → [`00afab88`](#insn-00afab88)
- ブロック [`00afab88`](#insn-00afab88) 範囲 `[['00afab88', '00afab8b']]`
  - `CONDITIONAL_JUMP` [`00afab88`](#insn-00afab88) → [`00afaaf8`](#insn-00afaaf8)
  - `FALL_THROUGH` [`00afab88`](#insn-00afab88) → [`00afab8c`](#insn-00afab8c)
- ブロック [`00afab8c`](#insn-00afab8c) 範囲 `[['00afab8c', '00afab93']]`
  - `UNCONDITIONAL_JUMP` [`00afab90`](#insn-00afab90) → [`00afaba4`](#insn-00afaba4)
- ブロック [`00afab94`](#insn-00afab94) 範囲 `[['00afab94', '00afab9b']]`
  - `UNCONDITIONAL_JUMP` [`00afab98`](#insn-00afab98) → [`00afaba4`](#insn-00afaba4)
- ブロック [`00afab9c`](#insn-00afab9c) 範囲 `[['00afab9c', '00afaba3']]`
  - `FALL_THROUGH` [`00afaba0`](#insn-00afaba0) → [`00afaba4`](#insn-00afaba4)
- ブロック [`00afaba4`](#insn-00afaba4) 範囲 `[['00afaba4', '00afabc3']]`

## 命令位置別の参照

- [`00afaaa4`](#insn-00afaaa4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaaa8`](#insn-00afaaa8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaaac`](#insn-00afaaac) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaab0`](#insn-00afaab0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaab4`](#insn-00afaab4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaab8`](#insn-00afaab8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaacc`](#insn-00afaacc) → [`00afab94`](#insn-00afab94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaaec`](#insn-00afaaec) → [`00afab08`](#insn-00afab08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaaf4`](#insn-00afaaf4) → [`00afab8c`](#insn-00afab8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab00`](#insn-00afab00) → [`00afab8c`](#insn-00afab8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab28`](#insn-00afab28) → [`00afab50`](#insn-00afab50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab40`](#insn-00afab40) → [`00bdb100`](../00bdb/00bdb100.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb100` · 推定シンボル `None` · 推定型 `None`
- [`00afab44`](#insn-00afab44) → [`00afab50`](#insn-00afab50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab48`](#insn-00afab48) → [`00afab58`](#insn-00afab58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab4c`](#insn-00afab4c) → [`00afab70`](#insn-00afab70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab54`](#insn-00afab54) → [`00afab68`](#insn-00afab68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab5c`](#insn-00afab5c) → [`00afab9c`](#insn-00afab9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab64`](#insn-00afab64) → [`00afab04`](#insn-00afab04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab68`](#insn-00afab68) → [`00afaaf0`](#insn-00afaaf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab80`](#insn-00afab80) → [`00bdb100`](../00bdb/00bdb100.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb100` · 推定シンボル `None` · 推定型 `None`
- [`00afab84`](#insn-00afab84) → [`00afaaf0`](#insn-00afaaf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab88`](#insn-00afab88) → [`00afaaf8`](#insn-00afaaf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab90`](#insn-00afab90) → [`00afaba4`](#insn-00afaba4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab98`](#insn-00afab98) → [`00afaba4`](#insn-00afaba4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaba8`](#insn-00afaba8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afabac`](#insn-00afabac) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afabb0`](#insn-00afabb0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afabb4`](#insn-00afabb4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afabb8`](#insn-00afabb8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afaaa4`](#insn-00afaaa4)

~~~json
{
  "source": "00afaaa4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaaa8`](#insn-00afaaa8)

~~~json
{
  "source": "00afaaa8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaaac`](#insn-00afaaac)

~~~json
{
  "source": "00afaaac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaab0`](#insn-00afaab0)

~~~json
{
  "source": "00afaab0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaab4`](#insn-00afaab4)

~~~json
{
  "source": "00afaab4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaab8`](#insn-00afaab8)

~~~json
{
  "source": "00afaab8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaacc`](#insn-00afaacc)

~~~json
{
  "source": "00afaacc",
  "target": "00afab94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaaec`](#insn-00afaaec)

~~~json
{
  "source": "00afaaec",
  "target": "00afab08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaaf4`](#insn-00afaaf4)

~~~json
{
  "source": "00afaaf4",
  "target": "00afab8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab00`](#insn-00afab00)

~~~json
{
  "source": "00afab00",
  "target": "00afab8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab28`](#insn-00afab28)

~~~json
{
  "source": "00afab28",
  "target": "00afab50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab40`](#insn-00afab40)

~~~json
{
  "source": "00afab40",
  "target": "00bdb100",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afab44`](#insn-00afab44)

~~~json
{
  "source": "00afab44",
  "target": "00afab50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab48`](#insn-00afab48)

~~~json
{
  "source": "00afab48",
  "target": "00afab58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab4c`](#insn-00afab4c)

~~~json
{
  "source": "00afab4c",
  "target": "00afab70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab54`](#insn-00afab54)

~~~json
{
  "source": "00afab54",
  "target": "00afab68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab5c`](#insn-00afab5c)

~~~json
{
  "source": "00afab5c",
  "target": "00afab9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab64`](#insn-00afab64)

~~~json
{
  "source": "00afab64",
  "target": "00afab04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab68`](#insn-00afab68)

~~~json
{
  "source": "00afab68",
  "target": "00afaaf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab80`](#insn-00afab80)

~~~json
{
  "source": "00afab80",
  "target": "00bdb100",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afab84`](#insn-00afab84)

~~~json
{
  "source": "00afab84",
  "target": "00afaaf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab88`](#insn-00afab88)

~~~json
{
  "source": "00afab88",
  "target": "00afaaf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab90`](#insn-00afab90)

~~~json
{
  "source": "00afab90",
  "target": "00afaba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab98`](#insn-00afab98)

~~~json
{
  "source": "00afab98",
  "target": "00afaba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaba8`](#insn-00afaba8)

~~~json
{
  "source": "00afaba8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afabac`](#insn-00afabac)

~~~json
{
  "source": "00afabac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afabb0`](#insn-00afabb0)

~~~json
{
  "source": "00afabb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afabb4`](#insn-00afabb4)

~~~json
{
  "source": "00afabb4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afabb8`](#insn-00afabb8)

~~~json
{
  "source": "00afabb8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
