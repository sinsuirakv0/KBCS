# 00afab6c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00afaaa4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afaaa4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0002.md#compare-7ec817c705a2a0abaac241dc735e0513)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00afabb0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afabb0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-4181f339f0e103f6989ddefca5b18f8d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afab6c",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDataENS_14default_deleteISB_EEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISQ_EERKT_",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "053bd38bdb0dfa6083eed5031f4cf47c004e545cffa67e921d28712f73c214ab",
  "source_text_sha256": "053bd38bdb0dfa6083eed5031f4cf47c004e545cffa67e921d28712f73c214ab",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afab6c",
        "00afac8b"
      ]
    ],
    "bytes_sha256": "5b04d848a54b6d1b107ba3b0c80b8ae9744e380ca3e2e957e24ab573032b29a3",
    "instruction_count": 72,
    "instruction_bytes": 288,
    "body_bytes": 288,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bde930](../00bde/00bde930.md)

## 呼び出し先

- [00bdb1b0](../00bdb/00bdb1b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2728 bytes

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
  
                    /* try { // try from 00afab78 to 00bfab8b has its CatchHandler @ 00aff518 */
  plVar5 = (long *)(param_1 + 8);
  plVar6 = (long *)*plVar5;
  if (plVar6 == (long *)0x0) {
    *param_2 = plVar5;
                    /* try { // try from 00afac7c to 00bfac9b has its CatchHandler @ 00afff3c */
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
                    /* try { // try from 00afac10 to 00bfac17 has its CatchHandler @ 00b001dc */
      if (iVar4 < 0) goto LAB_00afac20;
LAB_00afac38:
      if ((bVar3 & 1) == 0) {
        __s1_00 = (void *)((long)plVar7 + 0x21);
      }
      iVar4 = memcmp(__s1_00,__s1,__n);
      if (iVar4 == 0) goto LAB_00afabb8;
      if (-1 < iVar4) goto LAB_00afac54;
LAB_00afabc0:
      plVar5 = plVar7 + 1;
                    /* try { // try from 00afabc4 to 00bfabcb has its CatchHandler @ 00b00238 */
      plVar6 = (long *)*plVar5;
      if ((long *)*plVar5 == (long *)0x0) {
LAB_00afac54:
        *param_2 = plVar7;
        return plVar5;
      }
    }
                    /* try { // try from 00afac18 to 00bfac27 has its CatchHandler @ 00b00254 */
    if (uVar1 <= uVar2) {
      if (__n != 0) {
        __s1_00 = (void *)plVar7[6];
        goto LAB_00afac38;
      }
LAB_00afabb8:
      if (uVar2 <= uVar1) goto LAB_00afac54;
      goto LAB_00afabc0;
    }
LAB_00afac20:
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
<a id="insn-00afab6c"></a> `00afab6c` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00afab70"></a> `00afab70` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afab74"></a> `00afab74` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afab78"></a> `00afab78` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afab7c"></a> `00afab7c` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afab80"></a> `00afab80` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afab84"></a> `00afab84` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00afab88"></a> `00afab88` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00afab8c"></a> `00afab8c` | `97 8e 40 f8` | ldr x23,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00afab90"></a> `00afab90` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00afab94"></a> `00afab94` | `57 06 00 b4` | cbz x23,0x00afac5c | `CONDITIONAL_JUMP`
<a id="insn-00afab98"></a> `00afab98` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00afab9c"></a> `00afab9c` | `49 a8 40 a9` | ldp x9,x10,[x2, #0x8] | `FALL_THROUGH`
<a id="insn-00afaba0"></a> `00afaba0` | `14 20 00 91` | add x20,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00afaba4"></a> `00afaba4` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afaba8"></a> `00afaba8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afabac"></a> `00afabac` | `78 01 89 9a` | csel x24,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00afabb0"></a> `00afabb0` | `55 15 82 9a` | csinc x21,x10,x2,ne | `FALL_THROUGH`
<a id="insn-00afabb4"></a> `00afabb4` | `07 00 00 14` | b 0x00afabd0 | `UNCONDITIONAL_JUMP`
<a id="insn-00afabb8"></a> `00afabb8` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00afabbc"></a> `00afabbc` | `c2 04 00 54` | b.cs 0x00afac54 | `CONDITIONAL_JUMP`
<a id="insn-00afabc0"></a> `00afabc0` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00afabc4"></a> `00afabc4` | `88 8e 40 f8` | ldr x8,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00afabc8"></a> `00afabc8` | `68 04 00 b4` | cbz x8,0x00afac54 | `CONDITIONAL_JUMP`
<a id="insn-00afabcc"></a> `00afabcc` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00afabd0"></a> `00afabd0` | `fa 03 17 aa` | mov x26,x23 | `FALL_THROUGH`
<a id="insn-00afabd4"></a> `00afabd4` | `5b 0f 42 38` | ldrb w27,[x26, #0x20]! | `FALL_THROUGH`
<a id="insn-00afabd8"></a> `00afabd8` | `48 07 40 f9` | ldr x8,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00afabdc"></a> `00afabdc` | `69 ff 41 d3` | lsr x9,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00afabe0"></a> `00afabe0` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00afabe4"></a> `00afabe4` | `39 01 88 9a` | csel x25,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00afabe8"></a> `00afabe8` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00afabec"></a> `00afabec` | `36 33 98 9a` | csel x22,x25,x24,cc | `FALL_THROUGH`
<a id="insn-00afabf0"></a> `00afabf0` | `56 01 00 b4` | cbz x22,0x00afac18 | `CONDITIONAL_JUMP`
<a id="insn-00afabf4"></a> `00afabf4` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00afabf8"></a> `00afabf8` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00afabfc"></a> `00afabfc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afac00"></a> `00afac00` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00afac04"></a> `00afac04` | `81 17 9a 9a` | csinc x1,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00afac08"></a> `00afac08` | `6a 81 03 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00afac0c"></a> `00afac0c` | `60 00 00 34` | cbz w0,0x00afac18 | `CONDITIONAL_JUMP`
<a id="insn-00afac10"></a> `00afac10` | `80 00 f8 37` | tbnz w0,#0x1f,0x00afac20 | `CONDITIONAL_JUMP`
<a id="insn-00afac14"></a> `00afac14` | `09 00 00 14` | b 0x00afac38 | `UNCONDITIONAL_JUMP`
<a id="insn-00afac18"></a> `00afac18` | `1f 03 19 eb` | cmp x24,x25 | `FALL_THROUGH`
<a id="insn-00afac1c"></a> `00afac1c` | `a2 00 00 54` | b.cs 0x00afac30 | `CONDITIONAL_JUMP`
<a id="insn-00afac20"></a> `00afac20` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00afac24"></a> `00afac24` | `08 02 00 b4` | cbz x8,0x00afac64 | `CONDITIONAL_JUMP`
<a id="insn-00afac28"></a> `00afac28` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00afac2c"></a> `00afac2c` | `e8 ff ff 17` | b 0x00afabcc | `UNCONDITIONAL_JUMP`
<a id="insn-00afac30"></a> `00afac30` | `56 fc ff b4` | cbz x22,0x00afabb8 | `CONDITIONAL_JUMP`
<a id="insn-00afac34"></a> `00afac34` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00afac38"></a> `00afac38` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00afac3c"></a> `00afac3c` | `80 17 9a 9a` | csinc x0,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00afac40"></a> `00afac40` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00afac44"></a> `00afac44` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00afac48"></a> `00afac48` | `5a 81 03 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00afac4c"></a> `00afac4c` | `60 fb ff 34` | cbz w0,0x00afabb8 | `CONDITIONAL_JUMP`
<a id="insn-00afac50"></a> `00afac50` | `80 fb ff 37` | tbnz w0,#0x1f,0x00afabc0 | `CONDITIONAL_JUMP`
<a id="insn-00afac54"></a> `00afac54` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00afac58"></a> `00afac58` | `05 00 00 14` | b 0x00afac6c | `UNCONDITIONAL_JUMP`
<a id="insn-00afac5c"></a> `00afac5c` | `74 02 00 f9` | str x20,[x19] | `FALL_THROUGH`
<a id="insn-00afac60"></a> `00afac60` | `03 00 00 14` | b 0x00afac6c | `UNCONDITIONAL_JUMP`
<a id="insn-00afac64"></a> `00afac64` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00afac68"></a> `00afac68` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00afac6c"></a> `00afac6c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afac70"></a> `00afac70` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afac74"></a> `00afac74` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afac78"></a> `00afac78` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afac7c"></a> `00afac7c` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afac80"></a> `00afac80` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afac84"></a> `00afac84` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00afac88"></a> `00afac88` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afab6c`](#insn-00afab6c) 範囲 `[['00afab6c', '00afab77']]`
  - `FALL_THROUGH` [`00afab74`](#insn-00afab74) → [`00afab78`](#insn-00afab78)
- ブロック [`00afab78`](#insn-00afab78) 範囲 `[['00afab78', '00afab97']]`
  - `CONDITIONAL_JUMP` [`00afab94`](#insn-00afab94) → [`00afac5c`](#insn-00afac5c)
  - `FALL_THROUGH` [`00afab94`](#insn-00afab94) → [`00afab98`](#insn-00afab98)
- ブロック [`00afab98`](#insn-00afab98) 範囲 `[['00afab98', '00afabb7']]`
  - `UNCONDITIONAL_JUMP` [`00afabb4`](#insn-00afabb4) → [`00afabd0`](#insn-00afabd0)
- ブロック [`00afabb8`](#insn-00afabb8) 範囲 `[['00afabb8', '00afabbf']]`
  - `CONDITIONAL_JUMP` [`00afabbc`](#insn-00afabbc) → [`00afac54`](#insn-00afac54)
  - `FALL_THROUGH` [`00afabbc`](#insn-00afabbc) → [`00afabc0`](#insn-00afabc0)
- ブロック [`00afabc0`](#insn-00afabc0) 範囲 `[['00afabc0', '00afabc3']]`
  - `FALL_THROUGH` [`00afabc0`](#insn-00afabc0) → [`00afabc4`](#insn-00afabc4)
- ブロック [`00afabc4`](#insn-00afabc4) 範囲 `[['00afabc4', '00afabcb']]`
  - `CONDITIONAL_JUMP` [`00afabc8`](#insn-00afabc8) → [`00afac54`](#insn-00afac54)
  - `FALL_THROUGH` [`00afabc8`](#insn-00afabc8) → [`00afabcc`](#insn-00afabcc)
- ブロック [`00afabcc`](#insn-00afabcc) 範囲 `[['00afabcc', '00afabcf']]`
  - `FALL_THROUGH` [`00afabcc`](#insn-00afabcc) → [`00afabd0`](#insn-00afabd0)
- ブロック [`00afabd0`](#insn-00afabd0) 範囲 `[['00afabd0', '00afabf3']]`
  - `CONDITIONAL_JUMP` [`00afabf0`](#insn-00afabf0) → [`00afac18`](#insn-00afac18)
  - `FALL_THROUGH` [`00afabf0`](#insn-00afabf0) → [`00afabf4`](#insn-00afabf4)
- ブロック [`00afabf4`](#insn-00afabf4) 範囲 `[['00afabf4', '00afac0f']]`
  - `CONDITIONAL_JUMP` [`00afac0c`](#insn-00afac0c) → [`00afac18`](#insn-00afac18)
  - `FALL_THROUGH` [`00afac0c`](#insn-00afac0c) → [`00afac10`](#insn-00afac10)
- ブロック [`00afac10`](#insn-00afac10) 範囲 `[['00afac10', '00afac13']]`
  - `CONDITIONAL_JUMP` [`00afac10`](#insn-00afac10) → [`00afac20`](#insn-00afac20)
  - `FALL_THROUGH` [`00afac10`](#insn-00afac10) → [`00afac14`](#insn-00afac14)
- ブロック [`00afac14`](#insn-00afac14) 範囲 `[['00afac14', '00afac17']]`
  - `UNCONDITIONAL_JUMP` [`00afac14`](#insn-00afac14) → [`00afac38`](#insn-00afac38)
- ブロック [`00afac18`](#insn-00afac18) 範囲 `[['00afac18', '00afac1f']]`
  - `CONDITIONAL_JUMP` [`00afac1c`](#insn-00afac1c) → [`00afac30`](#insn-00afac30)
  - `FALL_THROUGH` [`00afac1c`](#insn-00afac1c) → [`00afac20`](#insn-00afac20)
- ブロック [`00afac20`](#insn-00afac20) 範囲 `[['00afac20', '00afac27']]`
  - `CONDITIONAL_JUMP` [`00afac24`](#insn-00afac24) → [`00afac64`](#insn-00afac64)
  - `FALL_THROUGH` [`00afac24`](#insn-00afac24) → [`00afac28`](#insn-00afac28)
- ブロック [`00afac28`](#insn-00afac28) 範囲 `[['00afac28', '00afac2f']]`
  - `UNCONDITIONAL_JUMP` [`00afac2c`](#insn-00afac2c) → [`00afabcc`](#insn-00afabcc)
- ブロック [`00afac30`](#insn-00afac30) 範囲 `[['00afac30', '00afac33']]`
  - `CONDITIONAL_JUMP` [`00afac30`](#insn-00afac30) → [`00afabb8`](#insn-00afabb8)
  - `FALL_THROUGH` [`00afac30`](#insn-00afac30) → [`00afac34`](#insn-00afac34)
- ブロック [`00afac34`](#insn-00afac34) 範囲 `[['00afac34', '00afac37']]`
  - `FALL_THROUGH` [`00afac34`](#insn-00afac34) → [`00afac38`](#insn-00afac38)
- ブロック [`00afac38`](#insn-00afac38) 範囲 `[['00afac38', '00afac4f']]`
  - `CONDITIONAL_JUMP` [`00afac4c`](#insn-00afac4c) → [`00afabb8`](#insn-00afabb8)
  - `FALL_THROUGH` [`00afac4c`](#insn-00afac4c) → [`00afac50`](#insn-00afac50)
- ブロック [`00afac50`](#insn-00afac50) 範囲 `[['00afac50', '00afac53']]`
  - `CONDITIONAL_JUMP` [`00afac50`](#insn-00afac50) → [`00afabc0`](#insn-00afabc0)
  - `FALL_THROUGH` [`00afac50`](#insn-00afac50) → [`00afac54`](#insn-00afac54)
- ブロック [`00afac54`](#insn-00afac54) 範囲 `[['00afac54', '00afac5b']]`
  - `UNCONDITIONAL_JUMP` [`00afac58`](#insn-00afac58) → [`00afac6c`](#insn-00afac6c)
- ブロック [`00afac5c`](#insn-00afac5c) 範囲 `[['00afac5c', '00afac63']]`
  - `UNCONDITIONAL_JUMP` [`00afac60`](#insn-00afac60) → [`00afac6c`](#insn-00afac6c)
- ブロック [`00afac64`](#insn-00afac64) 範囲 `[['00afac64', '00afac6b']]`
  - `FALL_THROUGH` [`00afac68`](#insn-00afac68) → [`00afac6c`](#insn-00afac6c)
- ブロック [`00afac6c`](#insn-00afac6c) 範囲 `[['00afac6c', '00afac7b']]`
  - `FALL_THROUGH` [`00afac78`](#insn-00afac78) → [`00afac7c`](#insn-00afac7c)
- ブロック [`00afac7c`](#insn-00afac7c) 範囲 `[['00afac7c', '00afac8b']]`

## 命令位置別の参照

- [`00afab6c`](#insn-00afab6c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab70`](#insn-00afab70) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab74`](#insn-00afab74) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab78`](#insn-00afab78) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab7c`](#insn-00afab7c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab80`](#insn-00afab80) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab94`](#insn-00afab94) → [`00afac5c`](#insn-00afac5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afabb4`](#insn-00afabb4) → [`00afabd0`](#insn-00afabd0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afabbc`](#insn-00afabbc) → [`00afac54`](#insn-00afac54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afabc8`](#insn-00afabc8) → [`00afac54`](#insn-00afac54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afabf0`](#insn-00afabf0) → [`00afac18`](#insn-00afac18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac08`](#insn-00afac08) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00afac0c`](#insn-00afac0c) → [`00afac18`](#insn-00afac18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac10`](#insn-00afac10) → [`00afac20`](#insn-00afac20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac14`](#insn-00afac14) → [`00afac38`](#insn-00afac38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac1c`](#insn-00afac1c) → [`00afac30`](#insn-00afac30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac24`](#insn-00afac24) → [`00afac64`](#insn-00afac64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac2c`](#insn-00afac2c) → [`00afabcc`](#insn-00afabcc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac30`](#insn-00afac30) → [`00afabb8`](#insn-00afabb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac48`](#insn-00afac48) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00afac4c`](#insn-00afac4c) → [`00afabb8`](#insn-00afabb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac50`](#insn-00afac50) → [`00afabc0`](#insn-00afabc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac58`](#insn-00afac58) → [`00afac6c`](#insn-00afac6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac60`](#insn-00afac60) → [`00afac6c`](#insn-00afac6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac70`](#insn-00afac70) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac74`](#insn-00afac74) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac78`](#insn-00afac78) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac7c`](#insn-00afac7c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac80`](#insn-00afac80) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afab6c`](#insn-00afab6c)

~~~json
{
  "source": "00afab6c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab70`](#insn-00afab70)

~~~json
{
  "source": "00afab70",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab74`](#insn-00afab74)

~~~json
{
  "source": "00afab74",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab78`](#insn-00afab78)

~~~json
{
  "source": "00afab78",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab7c`](#insn-00afab7c)

~~~json
{
  "source": "00afab7c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab80`](#insn-00afab80)

~~~json
{
  "source": "00afab80",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab94`](#insn-00afab94)

~~~json
{
  "source": "00afab94",
  "target": "00afac5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afabb4`](#insn-00afabb4)

~~~json
{
  "source": "00afabb4",
  "target": "00afabd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afabbc`](#insn-00afabbc)

~~~json
{
  "source": "00afabbc",
  "target": "00afac54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afabc8`](#insn-00afabc8)

~~~json
{
  "source": "00afabc8",
  "target": "00afac54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afabf0`](#insn-00afabf0)

~~~json
{
  "source": "00afabf0",
  "target": "00afac18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac08`](#insn-00afac08)

~~~json
{
  "source": "00afac08",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afac0c`](#insn-00afac0c)

~~~json
{
  "source": "00afac0c",
  "target": "00afac18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac10`](#insn-00afac10)

~~~json
{
  "source": "00afac10",
  "target": "00afac20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac14`](#insn-00afac14)

~~~json
{
  "source": "00afac14",
  "target": "00afac38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac1c`](#insn-00afac1c)

~~~json
{
  "source": "00afac1c",
  "target": "00afac30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac24`](#insn-00afac24)

~~~json
{
  "source": "00afac24",
  "target": "00afac64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac2c`](#insn-00afac2c)

~~~json
{
  "source": "00afac2c",
  "target": "00afabcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac30`](#insn-00afac30)

~~~json
{
  "source": "00afac30",
  "target": "00afabb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac48`](#insn-00afac48)

~~~json
{
  "source": "00afac48",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afac4c`](#insn-00afac4c)

~~~json
{
  "source": "00afac4c",
  "target": "00afabb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac50`](#insn-00afac50)

~~~json
{
  "source": "00afac50",
  "target": "00afabc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac58`](#insn-00afac58)

~~~json
{
  "source": "00afac58",
  "target": "00afac6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac60`](#insn-00afac60)

~~~json
{
  "source": "00afac60",
  "target": "00afac6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac70`](#insn-00afac70)

~~~json
{
  "source": "00afac70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac74`](#insn-00afac74)

~~~json
{
  "source": "00afac74",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac78`](#insn-00afac78)

~~~json
{
  "source": "00afac78",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac7c`](#insn-00afac7c)

~~~json
{
  "source": "00afac7c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac80`](#insn-00afac80)

~~~json
{
  "source": "00afac80",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
