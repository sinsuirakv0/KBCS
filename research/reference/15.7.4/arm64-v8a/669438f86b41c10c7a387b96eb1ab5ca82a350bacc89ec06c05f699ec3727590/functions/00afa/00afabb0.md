# 00afabb0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afab6c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afab6c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-4181f339f0e103f6989ddefca5b18f8d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b5a934`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a934.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0060.md#compare-bdaf96174836042373b82c87f844940b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afabb0",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDataENS_14default_deleteISB_EEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISQ_EERKT_",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e9c345d92b0f72758e64d528ef179996e547cc6fc375089256b1d04e09ba8c3b",
  "source_text_sha256": "e9c345d92b0f72758e64d528ef179996e547cc6fc375089256b1d04e09ba8c3b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afabb0",
        "00afaccf"
      ]
    ],
    "bytes_sha256": "84fcdecd145f197f71bdcb9cb12577a5d586c16eaf2c0ec2f6ecc36a6861d515",
    "instruction_count": 72,
    "instruction_bytes": 288,
    "body_bytes": 288,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bde980](../00bde/00bde980.md)

## 呼び出し先

- [00bdb200](../00bdb/00bdb200.md)

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
  
                    /* try { // try from 00afabbc to 00bfabcf has its CatchHandler @ 00aff55c */
  plVar5 = (long *)(param_1 + 8);
  plVar6 = (long *)*plVar5;
  if (plVar6 == (long *)0x0) {
    *param_2 = plVar5;
                    /* try { // try from 00afacc0 to 00bfacdf has its CatchHandler @ 00afff80 */
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
                    /* try { // try from 00afac54 to 00bfac5b has its CatchHandler @ 00b00220 */
      if (iVar4 < 0) goto LAB_00afac64;
LAB_00afac7c:
      if ((bVar3 & 1) == 0) {
        __s1_00 = (void *)((long)plVar7 + 0x21);
      }
      iVar4 = memcmp(__s1_00,__s1,__n);
      if (iVar4 == 0) goto LAB_00afabfc;
      if (-1 < iVar4) goto LAB_00afac98;
LAB_00afac04:
      plVar5 = plVar7 + 1;
                    /* try { // try from 00afac08 to 00bfac0f has its CatchHandler @ 00b0027c */
      plVar6 = (long *)*plVar5;
      if ((long *)*plVar5 == (long *)0x0) {
LAB_00afac98:
        *param_2 = plVar7;
        return plVar5;
      }
    }
                    /* try { // try from 00afac5c to 00bfac6b has its CatchHandler @ 00b00298 */
    if (uVar1 <= uVar2) {
      if (__n != 0) {
        __s1_00 = (void *)plVar7[6];
        goto LAB_00afac7c;
      }
LAB_00afabfc:
      if (uVar2 <= uVar1) goto LAB_00afac98;
      goto LAB_00afac04;
    }
LAB_00afac64:
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
<a id="insn-00afabb0"></a> `00afabb0` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00afabb4"></a> `00afabb4` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afabb8"></a> `00afabb8` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afabbc"></a> `00afabbc` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afabc0"></a> `00afabc0` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afabc4"></a> `00afabc4` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afabc8"></a> `00afabc8` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00afabcc"></a> `00afabcc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00afabd0"></a> `00afabd0` | `97 8e 40 f8` | ldr x23,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00afabd4"></a> `00afabd4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00afabd8"></a> `00afabd8` | `57 06 00 b4` | cbz x23,0x00afaca0 | `CONDITIONAL_JUMP`
<a id="insn-00afabdc"></a> `00afabdc` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00afabe0"></a> `00afabe0` | `49 a8 40 a9` | ldp x9,x10,[x2, #0x8] | `FALL_THROUGH`
<a id="insn-00afabe4"></a> `00afabe4` | `14 20 00 91` | add x20,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00afabe8"></a> `00afabe8` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afabec"></a> `00afabec` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afabf0"></a> `00afabf0` | `78 01 89 9a` | csel x24,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00afabf4"></a> `00afabf4` | `55 15 82 9a` | csinc x21,x10,x2,ne | `FALL_THROUGH`
<a id="insn-00afabf8"></a> `00afabf8` | `07 00 00 14` | b 0x00afac14 | `UNCONDITIONAL_JUMP`
<a id="insn-00afabfc"></a> `00afabfc` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00afac00"></a> `00afac00` | `c2 04 00 54` | b.cs 0x00afac98 | `CONDITIONAL_JUMP`
<a id="insn-00afac04"></a> `00afac04` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00afac08"></a> `00afac08` | `88 8e 40 f8` | ldr x8,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00afac0c"></a> `00afac0c` | `68 04 00 b4` | cbz x8,0x00afac98 | `CONDITIONAL_JUMP`
<a id="insn-00afac10"></a> `00afac10` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00afac14"></a> `00afac14` | `fa 03 17 aa` | mov x26,x23 | `FALL_THROUGH`
<a id="insn-00afac18"></a> `00afac18` | `5b 0f 42 38` | ldrb w27,[x26, #0x20]! | `FALL_THROUGH`
<a id="insn-00afac1c"></a> `00afac1c` | `48 07 40 f9` | ldr x8,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00afac20"></a> `00afac20` | `69 ff 41 d3` | lsr x9,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00afac24"></a> `00afac24` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00afac28"></a> `00afac28` | `39 01 88 9a` | csel x25,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00afac2c"></a> `00afac2c` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00afac30"></a> `00afac30` | `36 33 98 9a` | csel x22,x25,x24,cc | `FALL_THROUGH`
<a id="insn-00afac34"></a> `00afac34` | `56 01 00 b4` | cbz x22,0x00afac5c | `CONDITIONAL_JUMP`
<a id="insn-00afac38"></a> `00afac38` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00afac3c"></a> `00afac3c` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00afac40"></a> `00afac40` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afac44"></a> `00afac44` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00afac48"></a> `00afac48` | `81 17 9a 9a` | csinc x1,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00afac4c"></a> `00afac4c` | `6d 81 03 94` | bl 0x00bdb200 | `UNCONDITIONAL_CALL`
<a id="insn-00afac50"></a> `00afac50` | `60 00 00 34` | cbz w0,0x00afac5c | `CONDITIONAL_JUMP`
<a id="insn-00afac54"></a> `00afac54` | `80 00 f8 37` | tbnz w0,#0x1f,0x00afac64 | `CONDITIONAL_JUMP`
<a id="insn-00afac58"></a> `00afac58` | `09 00 00 14` | b 0x00afac7c | `UNCONDITIONAL_JUMP`
<a id="insn-00afac5c"></a> `00afac5c` | `1f 03 19 eb` | cmp x24,x25 | `FALL_THROUGH`
<a id="insn-00afac60"></a> `00afac60` | `a2 00 00 54` | b.cs 0x00afac74 | `CONDITIONAL_JUMP`
<a id="insn-00afac64"></a> `00afac64` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00afac68"></a> `00afac68` | `08 02 00 b4` | cbz x8,0x00afaca8 | `CONDITIONAL_JUMP`
<a id="insn-00afac6c"></a> `00afac6c` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00afac70"></a> `00afac70` | `e8 ff ff 17` | b 0x00afac10 | `UNCONDITIONAL_JUMP`
<a id="insn-00afac74"></a> `00afac74` | `56 fc ff b4` | cbz x22,0x00afabfc | `CONDITIONAL_JUMP`
<a id="insn-00afac78"></a> `00afac78` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00afac7c"></a> `00afac7c` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00afac80"></a> `00afac80` | `80 17 9a 9a` | csinc x0,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00afac84"></a> `00afac84` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00afac88"></a> `00afac88` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00afac8c"></a> `00afac8c` | `5d 81 03 94` | bl 0x00bdb200 | `UNCONDITIONAL_CALL`
<a id="insn-00afac90"></a> `00afac90` | `60 fb ff 34` | cbz w0,0x00afabfc | `CONDITIONAL_JUMP`
<a id="insn-00afac94"></a> `00afac94` | `80 fb ff 37` | tbnz w0,#0x1f,0x00afac04 | `CONDITIONAL_JUMP`
<a id="insn-00afac98"></a> `00afac98` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00afac9c"></a> `00afac9c` | `05 00 00 14` | b 0x00afacb0 | `UNCONDITIONAL_JUMP`
<a id="insn-00afaca0"></a> `00afaca0` | `74 02 00 f9` | str x20,[x19] | `FALL_THROUGH`
<a id="insn-00afaca4"></a> `00afaca4` | `03 00 00 14` | b 0x00afacb0 | `UNCONDITIONAL_JUMP`
<a id="insn-00afaca8"></a> `00afaca8` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00afacac"></a> `00afacac` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00afacb0"></a> `00afacb0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afacb4"></a> `00afacb4` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afacb8"></a> `00afacb8` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afacbc"></a> `00afacbc` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afacc0"></a> `00afacc0` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afacc4"></a> `00afacc4` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afacc8"></a> `00afacc8` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00afaccc"></a> `00afaccc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afabb0`](#insn-00afabb0) 範囲 `[['00afabb0', '00afabbb']]`
  - `FALL_THROUGH` [`00afabb8`](#insn-00afabb8) → [`00afabbc`](#insn-00afabbc)
- ブロック [`00afabbc`](#insn-00afabbc) 範囲 `[['00afabbc', '00afabdb']]`
  - `CONDITIONAL_JUMP` [`00afabd8`](#insn-00afabd8) → [`00afaca0`](#insn-00afaca0)
  - `FALL_THROUGH` [`00afabd8`](#insn-00afabd8) → [`00afabdc`](#insn-00afabdc)
- ブロック [`00afabdc`](#insn-00afabdc) 範囲 `[['00afabdc', '00afabfb']]`
  - `UNCONDITIONAL_JUMP` [`00afabf8`](#insn-00afabf8) → [`00afac14`](#insn-00afac14)
- ブロック [`00afabfc`](#insn-00afabfc) 範囲 `[['00afabfc', '00afac03']]`
  - `CONDITIONAL_JUMP` [`00afac00`](#insn-00afac00) → [`00afac98`](#insn-00afac98)
  - `FALL_THROUGH` [`00afac00`](#insn-00afac00) → [`00afac04`](#insn-00afac04)
- ブロック [`00afac04`](#insn-00afac04) 範囲 `[['00afac04', '00afac07']]`
  - `FALL_THROUGH` [`00afac04`](#insn-00afac04) → [`00afac08`](#insn-00afac08)
- ブロック [`00afac08`](#insn-00afac08) 範囲 `[['00afac08', '00afac0f']]`
  - `CONDITIONAL_JUMP` [`00afac0c`](#insn-00afac0c) → [`00afac98`](#insn-00afac98)
  - `FALL_THROUGH` [`00afac0c`](#insn-00afac0c) → [`00afac10`](#insn-00afac10)
- ブロック [`00afac10`](#insn-00afac10) 範囲 `[['00afac10', '00afac13']]`
  - `FALL_THROUGH` [`00afac10`](#insn-00afac10) → [`00afac14`](#insn-00afac14)
- ブロック [`00afac14`](#insn-00afac14) 範囲 `[['00afac14', '00afac37']]`
  - `CONDITIONAL_JUMP` [`00afac34`](#insn-00afac34) → [`00afac5c`](#insn-00afac5c)
  - `FALL_THROUGH` [`00afac34`](#insn-00afac34) → [`00afac38`](#insn-00afac38)
- ブロック [`00afac38`](#insn-00afac38) 範囲 `[['00afac38', '00afac53']]`
  - `CONDITIONAL_JUMP` [`00afac50`](#insn-00afac50) → [`00afac5c`](#insn-00afac5c)
  - `FALL_THROUGH` [`00afac50`](#insn-00afac50) → [`00afac54`](#insn-00afac54)
- ブロック [`00afac54`](#insn-00afac54) 範囲 `[['00afac54', '00afac57']]`
  - `CONDITIONAL_JUMP` [`00afac54`](#insn-00afac54) → [`00afac64`](#insn-00afac64)
  - `FALL_THROUGH` [`00afac54`](#insn-00afac54) → [`00afac58`](#insn-00afac58)
- ブロック [`00afac58`](#insn-00afac58) 範囲 `[['00afac58', '00afac5b']]`
  - `UNCONDITIONAL_JUMP` [`00afac58`](#insn-00afac58) → [`00afac7c`](#insn-00afac7c)
- ブロック [`00afac5c`](#insn-00afac5c) 範囲 `[['00afac5c', '00afac63']]`
  - `CONDITIONAL_JUMP` [`00afac60`](#insn-00afac60) → [`00afac74`](#insn-00afac74)
  - `FALL_THROUGH` [`00afac60`](#insn-00afac60) → [`00afac64`](#insn-00afac64)
- ブロック [`00afac64`](#insn-00afac64) 範囲 `[['00afac64', '00afac6b']]`
  - `CONDITIONAL_JUMP` [`00afac68`](#insn-00afac68) → [`00afaca8`](#insn-00afaca8)
  - `FALL_THROUGH` [`00afac68`](#insn-00afac68) → [`00afac6c`](#insn-00afac6c)
- ブロック [`00afac6c`](#insn-00afac6c) 範囲 `[['00afac6c', '00afac73']]`
  - `UNCONDITIONAL_JUMP` [`00afac70`](#insn-00afac70) → [`00afac10`](#insn-00afac10)
- ブロック [`00afac74`](#insn-00afac74) 範囲 `[['00afac74', '00afac77']]`
  - `CONDITIONAL_JUMP` [`00afac74`](#insn-00afac74) → [`00afabfc`](#insn-00afabfc)
  - `FALL_THROUGH` [`00afac74`](#insn-00afac74) → [`00afac78`](#insn-00afac78)
- ブロック [`00afac78`](#insn-00afac78) 範囲 `[['00afac78', '00afac7b']]`
  - `FALL_THROUGH` [`00afac78`](#insn-00afac78) → [`00afac7c`](#insn-00afac7c)
- ブロック [`00afac7c`](#insn-00afac7c) 範囲 `[['00afac7c', '00afac93']]`
  - `CONDITIONAL_JUMP` [`00afac90`](#insn-00afac90) → [`00afabfc`](#insn-00afabfc)
  - `FALL_THROUGH` [`00afac90`](#insn-00afac90) → [`00afac94`](#insn-00afac94)
- ブロック [`00afac94`](#insn-00afac94) 範囲 `[['00afac94', '00afac97']]`
  - `CONDITIONAL_JUMP` [`00afac94`](#insn-00afac94) → [`00afac04`](#insn-00afac04)
  - `FALL_THROUGH` [`00afac94`](#insn-00afac94) → [`00afac98`](#insn-00afac98)
- ブロック [`00afac98`](#insn-00afac98) 範囲 `[['00afac98', '00afac9f']]`
  - `UNCONDITIONAL_JUMP` [`00afac9c`](#insn-00afac9c) → [`00afacb0`](#insn-00afacb0)
- ブロック [`00afaca0`](#insn-00afaca0) 範囲 `[['00afaca0', '00afaca7']]`
  - `UNCONDITIONAL_JUMP` [`00afaca4`](#insn-00afaca4) → [`00afacb0`](#insn-00afacb0)
- ブロック [`00afaca8`](#insn-00afaca8) 範囲 `[['00afaca8', '00afacaf']]`
  - `FALL_THROUGH` [`00afacac`](#insn-00afacac) → [`00afacb0`](#insn-00afacb0)
- ブロック [`00afacb0`](#insn-00afacb0) 範囲 `[['00afacb0', '00afacbf']]`
  - `FALL_THROUGH` [`00afacbc`](#insn-00afacbc) → [`00afacc0`](#insn-00afacc0)
- ブロック [`00afacc0`](#insn-00afacc0) 範囲 `[['00afacc0', '00afaccf']]`

## 命令位置別の参照

- [`00afabb0`](#insn-00afabb0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afabb4`](#insn-00afabb4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afabb8`](#insn-00afabb8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afabbc`](#insn-00afabbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afabc0`](#insn-00afabc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afabc4`](#insn-00afabc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afabd8`](#insn-00afabd8) → [`00afaca0`](#insn-00afaca0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afabf8`](#insn-00afabf8) → [`00afac14`](#insn-00afac14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac00`](#insn-00afac00) → [`00afac98`](#insn-00afac98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac0c`](#insn-00afac0c) → [`00afac98`](#insn-00afac98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac34`](#insn-00afac34) → [`00afac5c`](#insn-00afac5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac4c`](#insn-00afac4c) → [`00bdb200`](../00bdb/00bdb200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb200` · 推定シンボル `None` · 推定型 `None`
- [`00afac50`](#insn-00afac50) → [`00afac5c`](#insn-00afac5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac54`](#insn-00afac54) → [`00afac64`](#insn-00afac64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac58`](#insn-00afac58) → [`00afac7c`](#insn-00afac7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac60`](#insn-00afac60) → [`00afac74`](#insn-00afac74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac68`](#insn-00afac68) → [`00afaca8`](#insn-00afaca8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac70`](#insn-00afac70) → [`00afac10`](#insn-00afac10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac74`](#insn-00afac74) → [`00afabfc`](#insn-00afabfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac8c`](#insn-00afac8c) → [`00bdb200`](../00bdb/00bdb200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb200` · 推定シンボル `None` · 推定型 `None`
- [`00afac90`](#insn-00afac90) → [`00afabfc`](#insn-00afabfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac94`](#insn-00afac94) → [`00afac04`](#insn-00afac04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afac9c`](#insn-00afac9c) → [`00afacb0`](#insn-00afacb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaca4`](#insn-00afaca4) → [`00afacb0`](#insn-00afacb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afacb4`](#insn-00afacb4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afacb8`](#insn-00afacb8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afacbc`](#insn-00afacbc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afacc0`](#insn-00afacc0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afacc4`](#insn-00afacc4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afabb0`](#insn-00afabb0)

~~~json
{
  "source": "00afabb0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afabb4`](#insn-00afabb4)

~~~json
{
  "source": "00afabb4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afabb8`](#insn-00afabb8)

~~~json
{
  "source": "00afabb8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afabbc`](#insn-00afabbc)

~~~json
{
  "source": "00afabbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afabc0`](#insn-00afabc0)

~~~json
{
  "source": "00afabc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afabc4`](#insn-00afabc4)

~~~json
{
  "source": "00afabc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afabd8`](#insn-00afabd8)

~~~json
{
  "source": "00afabd8",
  "target": "00afaca0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afabf8`](#insn-00afabf8)

~~~json
{
  "source": "00afabf8",
  "target": "00afac14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac00`](#insn-00afac00)

~~~json
{
  "source": "00afac00",
  "target": "00afac98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac0c`](#insn-00afac0c)

~~~json
{
  "source": "00afac0c",
  "target": "00afac98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac34`](#insn-00afac34)

~~~json
{
  "source": "00afac34",
  "target": "00afac5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac4c`](#insn-00afac4c)

~~~json
{
  "source": "00afac4c",
  "target": "00bdb200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afac50`](#insn-00afac50)

~~~json
{
  "source": "00afac50",
  "target": "00afac5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac54`](#insn-00afac54)

~~~json
{
  "source": "00afac54",
  "target": "00afac64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac58`](#insn-00afac58)

~~~json
{
  "source": "00afac58",
  "target": "00afac7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac60`](#insn-00afac60)

~~~json
{
  "source": "00afac60",
  "target": "00afac74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac68`](#insn-00afac68)

~~~json
{
  "source": "00afac68",
  "target": "00afaca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac70`](#insn-00afac70)

~~~json
{
  "source": "00afac70",
  "target": "00afac10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac74`](#insn-00afac74)

~~~json
{
  "source": "00afac74",
  "target": "00afabfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac8c`](#insn-00afac8c)

~~~json
{
  "source": "00afac8c",
  "target": "00bdb200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afac90`](#insn-00afac90)

~~~json
{
  "source": "00afac90",
  "target": "00afabfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac94`](#insn-00afac94)

~~~json
{
  "source": "00afac94",
  "target": "00afac04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afac9c`](#insn-00afac9c)

~~~json
{
  "source": "00afac9c",
  "target": "00afacb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaca4`](#insn-00afaca4)

~~~json
{
  "source": "00afaca4",
  "target": "00afacb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afacb4`](#insn-00afacb4)

~~~json
{
  "source": "00afacb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afacb8`](#insn-00afacb8)

~~~json
{
  "source": "00afacb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afacbc`](#insn-00afacbc)

~~~json
{
  "source": "00afacbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afacc0`](#insn-00afacc0)

~~~json
{
  "source": "00afacc0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afacc4`](#insn-00afacc4)

~~~json
{
  "source": "00afacc4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
