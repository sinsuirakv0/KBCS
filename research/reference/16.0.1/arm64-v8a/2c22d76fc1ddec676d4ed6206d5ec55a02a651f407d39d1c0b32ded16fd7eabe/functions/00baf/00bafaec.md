# 00bafaec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00baf6c4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf6c4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0009.md#compare-5805639db4419c957fef1e962bd51c4b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bafb88`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00bafb88.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0078.md#compare-e29e7383f86f994d31cb44160797d6e7)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bafaec",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers10ServiceDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0b1cc717fd7456270472834adbab8244f39879a13fa7825d08faec7f92f89581",
  "source_text_sha256": "0b1cc717fd7456270472834adbab8244f39879a13fa7825d08faec7f92f89581",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bafaec",
        "00bafc0b"
      ]
    ],
    "bytes_sha256": "ed3d4370e37d60b2a36c42ebcc0dab05efa8d0a996c298396bcb4087f7133ea7",
    "instruction_count": 72,
    "instruction_bytes": 288,
    "body_bytes": 288,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5ce60](../00c5c/00c5ce60.md)

## 呼び出し先

- [00c58050](../00c58/00c58050.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2585 bytes

~~~c

long * _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers10ServiceDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_
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
                    /* try { // try from 00bafb50 to 00cafb5f has its CatchHandler @ 00bb002c */
      plVar7 = plVar6;
      bVar3 = *(byte *)(plVar7 + 4);
                    /* try { // try from 00bafb60 to 00cafe57 has its CatchHandler @ 00bb0038 */
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
      if (iVar4 < 0) goto LAB_00bafba0;
LAB_00bafbb8:
      if ((bVar3 & 1) == 0) {
        __s1_00 = (void *)((long)plVar7 + 0x21);
      }
      iVar4 = memcmp(__s1_00,__s1,__n);
      if (iVar4 == 0) goto LAB_00bafb38;
      if (-1 < iVar4) goto LAB_00bafbd4;
LAB_00bafb40:
      plVar5 = plVar7 + 1;
                    /* try { // try from 00bafb44 to 00cafb4f has its CatchHandler @ 00bb0030 */
      plVar6 = (long *)*plVar5;
      if ((long *)*plVar5 == (long *)0x0) {
LAB_00bafbd4:
        *param_2 = plVar7;
        return plVar5;
      }
    }
    if (uVar1 <= uVar2) {
      if (__n != 0) {
        __s1_00 = (void *)plVar7[6];
        goto LAB_00bafbb8;
      }
LAB_00bafb38:
                    /* try { // try from 00bafb38 to 00cafb3f has its CatchHandler @ 00bb0034 */
      if (uVar2 <= uVar1) goto LAB_00bafbd4;
      goto LAB_00bafb40;
    }
LAB_00bafba0:
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
<a id="insn-00bafaec"></a> `00bafaec` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00bafaf0"></a> `00bafaf0` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bafaf4"></a> `00bafaf4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bafaf8"></a> `00bafaf8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bafafc"></a> `00bafafc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bafb00"></a> `00bafb00` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bafb04"></a> `00bafb04` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bafb08"></a> `00bafb08` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bafb0c"></a> `00bafb0c` | `97 8e 40 f8` | ldr x23,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00bafb10"></a> `00bafb10` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bafb14"></a> `00bafb14` | `57 06 00 b4` | cbz x23,0x00bafbdc | `CONDITIONAL_JUMP`
<a id="insn-00bafb18"></a> `00bafb18` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00bafb1c"></a> `00bafb1c` | `49 a8 40 a9` | ldp x9,x10,[x2, #0x8] | `FALL_THROUGH`
<a id="insn-00bafb20"></a> `00bafb20` | `14 20 00 91` | add x20,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bafb24"></a> `00bafb24` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bafb28"></a> `00bafb28` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bafb2c"></a> `00bafb2c` | `78 01 89 9a` | csel x24,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00bafb30"></a> `00bafb30` | `55 15 82 9a` | csinc x21,x10,x2,ne | `FALL_THROUGH`
<a id="insn-00bafb34"></a> `00bafb34` | `07 00 00 14` | b 0x00bafb50 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafb38"></a> `00bafb38` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00bafb3c"></a> `00bafb3c` | `c2 04 00 54` | b.cs 0x00bafbd4 | `CONDITIONAL_JUMP`
<a id="insn-00bafb40"></a> `00bafb40` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00bafb44"></a> `00bafb44` | `88 8e 40 f8` | ldr x8,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00bafb48"></a> `00bafb48` | `68 04 00 b4` | cbz x8,0x00bafbd4 | `CONDITIONAL_JUMP`
<a id="insn-00bafb4c"></a> `00bafb4c` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00bafb50"></a> `00bafb50` | `fa 03 17 aa` | mov x26,x23 | `FALL_THROUGH`
<a id="insn-00bafb54"></a> `00bafb54` | `5b 0f 42 38` | ldrb w27,[x26, #0x20]! | `FALL_THROUGH`
<a id="insn-00bafb58"></a> `00bafb58` | `48 07 40 f9` | ldr x8,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00bafb5c"></a> `00bafb5c` | `69 ff 41 d3` | lsr x9,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00bafb60"></a> `00bafb60` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00bafb64"></a> `00bafb64` | `39 01 88 9a` | csel x25,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00bafb68"></a> `00bafb68` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00bafb6c"></a> `00bafb6c` | `36 33 98 9a` | csel x22,x25,x24,cc | `FALL_THROUGH`
<a id="insn-00bafb70"></a> `00bafb70` | `56 01 00 b4` | cbz x22,0x00bafb98 | `CONDITIONAL_JUMP`
<a id="insn-00bafb74"></a> `00bafb74` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00bafb78"></a> `00bafb78` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00bafb7c"></a> `00bafb7c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bafb80"></a> `00bafb80` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bafb84"></a> `00bafb84` | `81 17 9a 9a` | csinc x1,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00bafb88"></a> `00bafb88` | `32 a1 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00bafb8c"></a> `00bafb8c` | `60 00 00 34` | cbz w0,0x00bafb98 | `CONDITIONAL_JUMP`
<a id="insn-00bafb90"></a> `00bafb90` | `80 00 f8 37` | tbnz w0,#0x1f,0x00bafba0 | `CONDITIONAL_JUMP`
<a id="insn-00bafb94"></a> `00bafb94` | `09 00 00 14` | b 0x00bafbb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafb98"></a> `00bafb98` | `1f 03 19 eb` | cmp x24,x25 | `FALL_THROUGH`
<a id="insn-00bafb9c"></a> `00bafb9c` | `a2 00 00 54` | b.cs 0x00bafbb0 | `CONDITIONAL_JUMP`
<a id="insn-00bafba0"></a> `00bafba0` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00bafba4"></a> `00bafba4` | `08 02 00 b4` | cbz x8,0x00bafbe4 | `CONDITIONAL_JUMP`
<a id="insn-00bafba8"></a> `00bafba8` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00bafbac"></a> `00bafbac` | `e8 ff ff 17` | b 0x00bafb4c | `UNCONDITIONAL_JUMP`
<a id="insn-00bafbb0"></a> `00bafbb0` | `56 fc ff b4` | cbz x22,0x00bafb38 | `CONDITIONAL_JUMP`
<a id="insn-00bafbb4"></a> `00bafbb4` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00bafbb8"></a> `00bafbb8` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00bafbbc"></a> `00bafbbc` | `80 17 9a 9a` | csinc x0,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00bafbc0"></a> `00bafbc0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bafbc4"></a> `00bafbc4` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bafbc8"></a> `00bafbc8` | `22 a1 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00bafbcc"></a> `00bafbcc` | `60 fb ff 34` | cbz w0,0x00bafb38 | `CONDITIONAL_JUMP`
<a id="insn-00bafbd0"></a> `00bafbd0` | `80 fb ff 37` | tbnz w0,#0x1f,0x00bafb40 | `CONDITIONAL_JUMP`
<a id="insn-00bafbd4"></a> `00bafbd4` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00bafbd8"></a> `00bafbd8` | `05 00 00 14` | b 0x00bafbec | `UNCONDITIONAL_JUMP`
<a id="insn-00bafbdc"></a> `00bafbdc` | `74 02 00 f9` | str x20,[x19] | `FALL_THROUGH`
<a id="insn-00bafbe0"></a> `00bafbe0` | `03 00 00 14` | b 0x00bafbec | `UNCONDITIONAL_JUMP`
<a id="insn-00bafbe4"></a> `00bafbe4` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00bafbe8"></a> `00bafbe8` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00bafbec"></a> `00bafbec` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bafbf0"></a> `00bafbf0` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bafbf4"></a> `00bafbf4` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bafbf8"></a> `00bafbf8` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bafbfc"></a> `00bafbfc` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bafc00"></a> `00bafc00` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bafc04"></a> `00bafc04` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00bafc08"></a> `00bafc08` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bafaec`](#insn-00bafaec) 範囲 `[['00bafaec', '00bafb17']]`
  - `CONDITIONAL_JUMP` [`00bafb14`](#insn-00bafb14) → [`00bafbdc`](#insn-00bafbdc)
  - `FALL_THROUGH` [`00bafb14`](#insn-00bafb14) → [`00bafb18`](#insn-00bafb18)
- ブロック [`00bafb18`](#insn-00bafb18) 範囲 `[['00bafb18', '00bafb37']]`
  - `UNCONDITIONAL_JUMP` [`00bafb34`](#insn-00bafb34) → [`00bafb50`](#insn-00bafb50)
- ブロック [`00bafb38`](#insn-00bafb38) 範囲 `[['00bafb38', '00bafb3f']]`
  - `CONDITIONAL_JUMP` [`00bafb3c`](#insn-00bafb3c) → [`00bafbd4`](#insn-00bafbd4)
  - `FALL_THROUGH` [`00bafb3c`](#insn-00bafb3c) → [`00bafb40`](#insn-00bafb40)
- ブロック [`00bafb40`](#insn-00bafb40) 範囲 `[['00bafb40', '00bafb43']]`
  - `FALL_THROUGH` [`00bafb40`](#insn-00bafb40) → [`00bafb44`](#insn-00bafb44)
- ブロック [`00bafb44`](#insn-00bafb44) 範囲 `[['00bafb44', '00bafb4b']]`
  - `CONDITIONAL_JUMP` [`00bafb48`](#insn-00bafb48) → [`00bafbd4`](#insn-00bafbd4)
  - `FALL_THROUGH` [`00bafb48`](#insn-00bafb48) → [`00bafb4c`](#insn-00bafb4c)
- ブロック [`00bafb4c`](#insn-00bafb4c) 範囲 `[['00bafb4c', '00bafb4f']]`
  - `FALL_THROUGH` [`00bafb4c`](#insn-00bafb4c) → [`00bafb50`](#insn-00bafb50)
- ブロック [`00bafb50`](#insn-00bafb50) 範囲 `[['00bafb50', '00bafb5f']]`
  - `FALL_THROUGH` [`00bafb5c`](#insn-00bafb5c) → [`00bafb60`](#insn-00bafb60)
- ブロック [`00bafb60`](#insn-00bafb60) 範囲 `[['00bafb60', '00bafb73']]`
  - `CONDITIONAL_JUMP` [`00bafb70`](#insn-00bafb70) → [`00bafb98`](#insn-00bafb98)
  - `FALL_THROUGH` [`00bafb70`](#insn-00bafb70) → [`00bafb74`](#insn-00bafb74)
- ブロック [`00bafb74`](#insn-00bafb74) 範囲 `[['00bafb74', '00bafb8f']]`
  - `CONDITIONAL_JUMP` [`00bafb8c`](#insn-00bafb8c) → [`00bafb98`](#insn-00bafb98)
  - `FALL_THROUGH` [`00bafb8c`](#insn-00bafb8c) → [`00bafb90`](#insn-00bafb90)
- ブロック [`00bafb90`](#insn-00bafb90) 範囲 `[['00bafb90', '00bafb93']]`
  - `CONDITIONAL_JUMP` [`00bafb90`](#insn-00bafb90) → [`00bafba0`](#insn-00bafba0)
  - `FALL_THROUGH` [`00bafb90`](#insn-00bafb90) → [`00bafb94`](#insn-00bafb94)
- ブロック [`00bafb94`](#insn-00bafb94) 範囲 `[['00bafb94', '00bafb97']]`
  - `UNCONDITIONAL_JUMP` [`00bafb94`](#insn-00bafb94) → [`00bafbb8`](#insn-00bafbb8)
- ブロック [`00bafb98`](#insn-00bafb98) 範囲 `[['00bafb98', '00bafb9f']]`
  - `CONDITIONAL_JUMP` [`00bafb9c`](#insn-00bafb9c) → [`00bafbb0`](#insn-00bafbb0)
  - `FALL_THROUGH` [`00bafb9c`](#insn-00bafb9c) → [`00bafba0`](#insn-00bafba0)
- ブロック [`00bafba0`](#insn-00bafba0) 範囲 `[['00bafba0', '00bafba7']]`
  - `CONDITIONAL_JUMP` [`00bafba4`](#insn-00bafba4) → [`00bafbe4`](#insn-00bafbe4)
  - `FALL_THROUGH` [`00bafba4`](#insn-00bafba4) → [`00bafba8`](#insn-00bafba8)
- ブロック [`00bafba8`](#insn-00bafba8) 範囲 `[['00bafba8', '00bafbaf']]`
  - `UNCONDITIONAL_JUMP` [`00bafbac`](#insn-00bafbac) → [`00bafb4c`](#insn-00bafb4c)
- ブロック [`00bafbb0`](#insn-00bafbb0) 範囲 `[['00bafbb0', '00bafbb3']]`
  - `CONDITIONAL_JUMP` [`00bafbb0`](#insn-00bafbb0) → [`00bafb38`](#insn-00bafb38)
  - `FALL_THROUGH` [`00bafbb0`](#insn-00bafbb0) → [`00bafbb4`](#insn-00bafbb4)
- ブロック [`00bafbb4`](#insn-00bafbb4) 範囲 `[['00bafbb4', '00bafbb7']]`
  - `FALL_THROUGH` [`00bafbb4`](#insn-00bafbb4) → [`00bafbb8`](#insn-00bafbb8)
- ブロック [`00bafbb8`](#insn-00bafbb8) 範囲 `[['00bafbb8', '00bafbcf']]`
  - `CONDITIONAL_JUMP` [`00bafbcc`](#insn-00bafbcc) → [`00bafb38`](#insn-00bafb38)
  - `FALL_THROUGH` [`00bafbcc`](#insn-00bafbcc) → [`00bafbd0`](#insn-00bafbd0)
- ブロック [`00bafbd0`](#insn-00bafbd0) 範囲 `[['00bafbd0', '00bafbd3']]`
  - `CONDITIONAL_JUMP` [`00bafbd0`](#insn-00bafbd0) → [`00bafb40`](#insn-00bafb40)
  - `FALL_THROUGH` [`00bafbd0`](#insn-00bafbd0) → [`00bafbd4`](#insn-00bafbd4)
- ブロック [`00bafbd4`](#insn-00bafbd4) 範囲 `[['00bafbd4', '00bafbdb']]`
  - `UNCONDITIONAL_JUMP` [`00bafbd8`](#insn-00bafbd8) → [`00bafbec`](#insn-00bafbec)
- ブロック [`00bafbdc`](#insn-00bafbdc) 範囲 `[['00bafbdc', '00bafbe3']]`
  - `UNCONDITIONAL_JUMP` [`00bafbe0`](#insn-00bafbe0) → [`00bafbec`](#insn-00bafbec)
- ブロック [`00bafbe4`](#insn-00bafbe4) 範囲 `[['00bafbe4', '00bafbeb']]`
  - `FALL_THROUGH` [`00bafbe8`](#insn-00bafbe8) → [`00bafbec`](#insn-00bafbec)
- ブロック [`00bafbec`](#insn-00bafbec) 範囲 `[['00bafbec', '00bafc0b']]`

## 命令位置別の参照

- [`00bafaec`](#insn-00bafaec) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafaf0`](#insn-00bafaf0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafaf4`](#insn-00bafaf4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafaf8`](#insn-00bafaf8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafafc`](#insn-00bafafc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafb00`](#insn-00bafb00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafb14`](#insn-00bafb14) → [`00bafbdc`](#insn-00bafbdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafb34`](#insn-00bafb34) → [`00bafb50`](#insn-00bafb50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafb3c`](#insn-00bafb3c) → [`00bafbd4`](#insn-00bafbd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafb48`](#insn-00bafb48) → [`00bafbd4`](#insn-00bafbd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafb70`](#insn-00bafb70) → [`00bafb98`](#insn-00bafb98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafb88`](#insn-00bafb88) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00bafb8c`](#insn-00bafb8c) → [`00bafb98`](#insn-00bafb98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafb90`](#insn-00bafb90) → [`00bafba0`](#insn-00bafba0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafb94`](#insn-00bafb94) → [`00bafbb8`](#insn-00bafbb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafb9c`](#insn-00bafb9c) → [`00bafbb0`](#insn-00bafbb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafba4`](#insn-00bafba4) → [`00bafbe4`](#insn-00bafbe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafbac`](#insn-00bafbac) → [`00bafb4c`](#insn-00bafb4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafbb0`](#insn-00bafbb0) → [`00bafb38`](#insn-00bafb38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafbc8`](#insn-00bafbc8) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00bafbcc`](#insn-00bafbcc) → [`00bafb38`](#insn-00bafb38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafbd0`](#insn-00bafbd0) → [`00bafb40`](#insn-00bafb40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafbd8`](#insn-00bafbd8) → [`00bafbec`](#insn-00bafbec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafbe0`](#insn-00bafbe0) → [`00bafbec`](#insn-00bafbec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafbf0`](#insn-00bafbf0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafbf4`](#insn-00bafbf4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafbf8`](#insn-00bafbf8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafbfc`](#insn-00bafbfc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafc00`](#insn-00bafc00) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bafaec`](#insn-00bafaec)

~~~json
{
  "source": "00bafaec",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafaf0`](#insn-00bafaf0)

~~~json
{
  "source": "00bafaf0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafaf4`](#insn-00bafaf4)

~~~json
{
  "source": "00bafaf4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafaf8`](#insn-00bafaf8)

~~~json
{
  "source": "00bafaf8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafafc`](#insn-00bafafc)

~~~json
{
  "source": "00bafafc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafb00`](#insn-00bafb00)

~~~json
{
  "source": "00bafb00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafb14`](#insn-00bafb14)

~~~json
{
  "source": "00bafb14",
  "target": "00bafbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafb34`](#insn-00bafb34)

~~~json
{
  "source": "00bafb34",
  "target": "00bafb50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafb3c`](#insn-00bafb3c)

~~~json
{
  "source": "00bafb3c",
  "target": "00bafbd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafb48`](#insn-00bafb48)

~~~json
{
  "source": "00bafb48",
  "target": "00bafbd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafb70`](#insn-00bafb70)

~~~json
{
  "source": "00bafb70",
  "target": "00bafb98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafb88`](#insn-00bafb88)

~~~json
{
  "source": "00bafb88",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafb8c`](#insn-00bafb8c)

~~~json
{
  "source": "00bafb8c",
  "target": "00bafb98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafb90`](#insn-00bafb90)

~~~json
{
  "source": "00bafb90",
  "target": "00bafba0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafb94`](#insn-00bafb94)

~~~json
{
  "source": "00bafb94",
  "target": "00bafbb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafb9c`](#insn-00bafb9c)

~~~json
{
  "source": "00bafb9c",
  "target": "00bafbb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafba4`](#insn-00bafba4)

~~~json
{
  "source": "00bafba4",
  "target": "00bafbe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafbac`](#insn-00bafbac)

~~~json
{
  "source": "00bafbac",
  "target": "00bafb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafbb0`](#insn-00bafbb0)

~~~json
{
  "source": "00bafbb0",
  "target": "00bafb38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafbc8`](#insn-00bafbc8)

~~~json
{
  "source": "00bafbc8",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafbcc`](#insn-00bafbcc)

~~~json
{
  "source": "00bafbcc",
  "target": "00bafb38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafbd0`](#insn-00bafbd0)

~~~json
{
  "source": "00bafbd0",
  "target": "00bafb40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafbd8`](#insn-00bafbd8)

~~~json
{
  "source": "00bafbd8",
  "target": "00bafbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafbe0`](#insn-00bafbe0)

~~~json
{
  "source": "00bafbe0",
  "target": "00bafbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafbf0`](#insn-00bafbf0)

~~~json
{
  "source": "00bafbf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafbf4`](#insn-00bafbf4)

~~~json
{
  "source": "00bafbf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafbf8`](#insn-00bafbf8)

~~~json
{
  "source": "00bafbf8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafbfc`](#insn-00bafbfc)

~~~json
{
  "source": "00bafbfc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafc00`](#insn-00bafc00)

~~~json
{
  "source": "00bafc00",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
