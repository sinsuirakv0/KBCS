# 00b5bdec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b5adf8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5adf8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0032.md#compare-54deb9c67cd6d978c4c6fd20f7eea1b6)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5bdec",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDataENS_14default_deleteISB_EEEEEENS_19__map_value_compareIS7_SF_NS_4lessIS7_EELb1EEENS5_ISF_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISQ_EERKT_",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a90b736d762a8907393ab7ecd943de9608cc5ee848fde3dca389334ce273d461",
  "source_text_sha256": "a90b736d762a8907393ab7ecd943de9608cc5ee848fde3dca389334ce273d461",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5bdec",
        "00b5bf0b"
      ]
    ],
    "bytes_sha256": "facc98ff6289efcbe4917c7e4e24dfa70379eb6de515967a7d7e8a4acd554893",
    "instruction_count": 72,
    "instruction_bytes": 288,
    "body_bytes": 288,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5c8a0](../00c5c/00c5c8a0.md)

## 呼び出し先

- [00c590f0](../00c59/00c590f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2243 bytes

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
      if (iVar4 < 0) goto LAB_00b5bea0;
LAB_00b5beb8:
      if ((bVar3 & 1) == 0) {
        __s1_00 = (void *)((long)plVar7 + 0x21);
      }
      iVar4 = memcmp(__s1_00,__s1,__n);
      if (iVar4 == 0) goto LAB_00b5be38;
      if (-1 < iVar4) goto LAB_00b5bed4;
LAB_00b5be40:
      plVar5 = plVar7 + 1;
      plVar6 = (long *)*plVar5;
      if ((long *)*plVar5 == (long *)0x0) {
LAB_00b5bed4:
        *param_2 = plVar7;
        return plVar5;
      }
    }
    if (uVar1 <= uVar2) {
      if (__n != 0) {
        __s1_00 = (void *)plVar7[6];
        goto LAB_00b5beb8;
      }
LAB_00b5be38:
      if (uVar2 <= uVar1) goto LAB_00b5bed4;
      goto LAB_00b5be40;
    }
LAB_00b5bea0:
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
<a id="insn-00b5bdec"></a> `00b5bdec` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00b5bdf0"></a> `00b5bdf0` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5bdf4"></a> `00b5bdf4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5bdf8"></a> `00b5bdf8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5bdfc"></a> `00b5bdfc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b5be00"></a> `00b5be00` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b5be04"></a> `00b5be04` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b5be08"></a> `00b5be08` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b5be0c"></a> `00b5be0c` | `97 8e 40 f8` | ldr x23,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00b5be10"></a> `00b5be10` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00b5be14"></a> `00b5be14` | `57 06 00 b4` | cbz x23,0x00b5bedc | `CONDITIONAL_JUMP`
<a id="insn-00b5be18"></a> `00b5be18` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00b5be1c"></a> `00b5be1c` | `49 a8 40 a9` | ldp x9,x10,[x2, #0x8] | `FALL_THROUGH`
<a id="insn-00b5be20"></a> `00b5be20` | `14 20 00 91` | add x20,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00b5be24"></a> `00b5be24` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b5be28"></a> `00b5be28` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b5be2c"></a> `00b5be2c` | `78 01 89 9a` | csel x24,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00b5be30"></a> `00b5be30` | `55 15 82 9a` | csinc x21,x10,x2,ne | `FALL_THROUGH`
<a id="insn-00b5be34"></a> `00b5be34` | `07 00 00 14` | b 0x00b5be50 | `UNCONDITIONAL_JUMP`
<a id="insn-00b5be38"></a> `00b5be38` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00b5be3c"></a> `00b5be3c` | `c2 04 00 54` | b.cs 0x00b5bed4 | `CONDITIONAL_JUMP`
<a id="insn-00b5be40"></a> `00b5be40` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00b5be44"></a> `00b5be44` | `88 8e 40 f8` | ldr x8,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00b5be48"></a> `00b5be48` | `68 04 00 b4` | cbz x8,0x00b5bed4 | `CONDITIONAL_JUMP`
<a id="insn-00b5be4c"></a> `00b5be4c` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00b5be50"></a> `00b5be50` | `fa 03 17 aa` | mov x26,x23 | `FALL_THROUGH`
<a id="insn-00b5be54"></a> `00b5be54` | `5b 0f 42 38` | ldrb w27,[x26, #0x20]! | `FALL_THROUGH`
<a id="insn-00b5be58"></a> `00b5be58` | `48 07 40 f9` | ldr x8,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00b5be5c"></a> `00b5be5c` | `69 ff 41 d3` | lsr x9,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00b5be60"></a> `00b5be60` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00b5be64"></a> `00b5be64` | `39 01 88 9a` | csel x25,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00b5be68"></a> `00b5be68` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00b5be6c"></a> `00b5be6c` | `36 33 98 9a` | csel x22,x25,x24,cc | `FALL_THROUGH`
<a id="insn-00b5be70"></a> `00b5be70` | `56 01 00 b4` | cbz x22,0x00b5be98 | `CONDITIONAL_JUMP`
<a id="insn-00b5be74"></a> `00b5be74` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00b5be78"></a> `00b5be78` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00b5be7c"></a> `00b5be7c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b5be80"></a> `00b5be80` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00b5be84"></a> `00b5be84` | `81 17 9a 9a` | csinc x1,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00b5be88"></a> `00b5be88` | `9a f4 03 94` | bl 0x00c590f0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5be8c"></a> `00b5be8c` | `60 00 00 34` | cbz w0,0x00b5be98 | `CONDITIONAL_JUMP`
<a id="insn-00b5be90"></a> `00b5be90` | `80 00 f8 37` | tbnz w0,#0x1f,0x00b5bea0 | `CONDITIONAL_JUMP`
<a id="insn-00b5be94"></a> `00b5be94` | `09 00 00 14` | b 0x00b5beb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00b5be98"></a> `00b5be98` | `1f 03 19 eb` | cmp x24,x25 | `FALL_THROUGH`
<a id="insn-00b5be9c"></a> `00b5be9c` | `a2 00 00 54` | b.cs 0x00b5beb0 | `CONDITIONAL_JUMP`
<a id="insn-00b5bea0"></a> `00b5bea0` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00b5bea4"></a> `00b5bea4` | `08 02 00 b4` | cbz x8,0x00b5bee4 | `CONDITIONAL_JUMP`
<a id="insn-00b5bea8"></a> `00b5bea8` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00b5beac"></a> `00b5beac` | `e8 ff ff 17` | b 0x00b5be4c | `UNCONDITIONAL_JUMP`
<a id="insn-00b5beb0"></a> `00b5beb0` | `56 fc ff b4` | cbz x22,0x00b5be38 | `CONDITIONAL_JUMP`
<a id="insn-00b5beb4"></a> `00b5beb4` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00b5beb8"></a> `00b5beb8` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00b5bebc"></a> `00b5bebc` | `80 17 9a 9a` | csinc x0,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00b5bec0"></a> `00b5bec0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b5bec4"></a> `00b5bec4` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00b5bec8"></a> `00b5bec8` | `8a f4 03 94` | bl 0x00c590f0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5becc"></a> `00b5becc` | `60 fb ff 34` | cbz w0,0x00b5be38 | `CONDITIONAL_JUMP`
<a id="insn-00b5bed0"></a> `00b5bed0` | `80 fb ff 37` | tbnz w0,#0x1f,0x00b5be40 | `CONDITIONAL_JUMP`
<a id="insn-00b5bed4"></a> `00b5bed4` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00b5bed8"></a> `00b5bed8` | `05 00 00 14` | b 0x00b5beec | `UNCONDITIONAL_JUMP`
<a id="insn-00b5bedc"></a> `00b5bedc` | `74 02 00 f9` | str x20,[x19] | `FALL_THROUGH`
<a id="insn-00b5bee0"></a> `00b5bee0` | `03 00 00 14` | b 0x00b5beec | `UNCONDITIONAL_JUMP`
<a id="insn-00b5bee4"></a> `00b5bee4` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00b5bee8"></a> `00b5bee8` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00b5beec"></a> `00b5beec` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b5bef0"></a> `00b5bef0` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b5bef4"></a> `00b5bef4` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b5bef8"></a> `00b5bef8` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5befc"></a> `00b5befc` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5bf00"></a> `00b5bf00` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5bf04"></a> `00b5bf04` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00b5bf08"></a> `00b5bf08` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b5bdec`](#insn-00b5bdec) 範囲 `[['00b5bdec', '00b5be17']]`
  - `CONDITIONAL_JUMP` [`00b5be14`](#insn-00b5be14) → [`00b5bedc`](#insn-00b5bedc)
  - `FALL_THROUGH` [`00b5be14`](#insn-00b5be14) → [`00b5be18`](#insn-00b5be18)
- ブロック [`00b5be18`](#insn-00b5be18) 範囲 `[['00b5be18', '00b5be37']]`
  - `UNCONDITIONAL_JUMP` [`00b5be34`](#insn-00b5be34) → [`00b5be50`](#insn-00b5be50)
- ブロック [`00b5be38`](#insn-00b5be38) 範囲 `[['00b5be38', '00b5be3f']]`
  - `CONDITIONAL_JUMP` [`00b5be3c`](#insn-00b5be3c) → [`00b5bed4`](#insn-00b5bed4)
  - `FALL_THROUGH` [`00b5be3c`](#insn-00b5be3c) → [`00b5be40`](#insn-00b5be40)
- ブロック [`00b5be40`](#insn-00b5be40) 範囲 `[['00b5be40', '00b5be4b']]`
  - `CONDITIONAL_JUMP` [`00b5be48`](#insn-00b5be48) → [`00b5bed4`](#insn-00b5bed4)
  - `FALL_THROUGH` [`00b5be48`](#insn-00b5be48) → [`00b5be4c`](#insn-00b5be4c)
- ブロック [`00b5be4c`](#insn-00b5be4c) 範囲 `[['00b5be4c', '00b5be4f']]`
  - `FALL_THROUGH` [`00b5be4c`](#insn-00b5be4c) → [`00b5be50`](#insn-00b5be50)
- ブロック [`00b5be50`](#insn-00b5be50) 範囲 `[['00b5be50', '00b5be73']]`
  - `CONDITIONAL_JUMP` [`00b5be70`](#insn-00b5be70) → [`00b5be98`](#insn-00b5be98)
  - `FALL_THROUGH` [`00b5be70`](#insn-00b5be70) → [`00b5be74`](#insn-00b5be74)
- ブロック [`00b5be74`](#insn-00b5be74) 範囲 `[['00b5be74', '00b5be8f']]`
  - `CONDITIONAL_JUMP` [`00b5be8c`](#insn-00b5be8c) → [`00b5be98`](#insn-00b5be98)
  - `FALL_THROUGH` [`00b5be8c`](#insn-00b5be8c) → [`00b5be90`](#insn-00b5be90)
- ブロック [`00b5be90`](#insn-00b5be90) 範囲 `[['00b5be90', '00b5be93']]`
  - `CONDITIONAL_JUMP` [`00b5be90`](#insn-00b5be90) → [`00b5bea0`](#insn-00b5bea0)
  - `FALL_THROUGH` [`00b5be90`](#insn-00b5be90) → [`00b5be94`](#insn-00b5be94)
- ブロック [`00b5be94`](#insn-00b5be94) 範囲 `[['00b5be94', '00b5be97']]`
  - `UNCONDITIONAL_JUMP` [`00b5be94`](#insn-00b5be94) → [`00b5beb8`](#insn-00b5beb8)
- ブロック [`00b5be98`](#insn-00b5be98) 範囲 `[['00b5be98', '00b5be9f']]`
  - `CONDITIONAL_JUMP` [`00b5be9c`](#insn-00b5be9c) → [`00b5beb0`](#insn-00b5beb0)
  - `FALL_THROUGH` [`00b5be9c`](#insn-00b5be9c) → [`00b5bea0`](#insn-00b5bea0)
- ブロック [`00b5bea0`](#insn-00b5bea0) 範囲 `[['00b5bea0', '00b5bea7']]`
  - `CONDITIONAL_JUMP` [`00b5bea4`](#insn-00b5bea4) → [`00b5bee4`](#insn-00b5bee4)
  - `FALL_THROUGH` [`00b5bea4`](#insn-00b5bea4) → [`00b5bea8`](#insn-00b5bea8)
- ブロック [`00b5bea8`](#insn-00b5bea8) 範囲 `[['00b5bea8', '00b5beaf']]`
  - `UNCONDITIONAL_JUMP` [`00b5beac`](#insn-00b5beac) → [`00b5be4c`](#insn-00b5be4c)
- ブロック [`00b5beb0`](#insn-00b5beb0) 範囲 `[['00b5beb0', '00b5beb3']]`
  - `CONDITIONAL_JUMP` [`00b5beb0`](#insn-00b5beb0) → [`00b5be38`](#insn-00b5be38)
  - `FALL_THROUGH` [`00b5beb0`](#insn-00b5beb0) → [`00b5beb4`](#insn-00b5beb4)
- ブロック [`00b5beb4`](#insn-00b5beb4) 範囲 `[['00b5beb4', '00b5beb7']]`
  - `FALL_THROUGH` [`00b5beb4`](#insn-00b5beb4) → [`00b5beb8`](#insn-00b5beb8)
- ブロック [`00b5beb8`](#insn-00b5beb8) 範囲 `[['00b5beb8', '00b5becf']]`
  - `CONDITIONAL_JUMP` [`00b5becc`](#insn-00b5becc) → [`00b5be38`](#insn-00b5be38)
  - `FALL_THROUGH` [`00b5becc`](#insn-00b5becc) → [`00b5bed0`](#insn-00b5bed0)
- ブロック [`00b5bed0`](#insn-00b5bed0) 範囲 `[['00b5bed0', '00b5bed3']]`
  - `CONDITIONAL_JUMP` [`00b5bed0`](#insn-00b5bed0) → [`00b5be40`](#insn-00b5be40)
  - `FALL_THROUGH` [`00b5bed0`](#insn-00b5bed0) → [`00b5bed4`](#insn-00b5bed4)
- ブロック [`00b5bed4`](#insn-00b5bed4) 範囲 `[['00b5bed4', '00b5bedb']]`
  - `UNCONDITIONAL_JUMP` [`00b5bed8`](#insn-00b5bed8) → [`00b5beec`](#insn-00b5beec)
- ブロック [`00b5bedc`](#insn-00b5bedc) 範囲 `[['00b5bedc', '00b5bee3']]`
  - `UNCONDITIONAL_JUMP` [`00b5bee0`](#insn-00b5bee0) → [`00b5beec`](#insn-00b5beec)
- ブロック [`00b5bee4`](#insn-00b5bee4) 範囲 `[['00b5bee4', '00b5beeb']]`
  - `FALL_THROUGH` [`00b5bee8`](#insn-00b5bee8) → [`00b5beec`](#insn-00b5beec)
- ブロック [`00b5beec`](#insn-00b5beec) 範囲 `[['00b5beec', '00b5bf0b']]`

## 命令位置別の参照

- [`00b5bdec`](#insn-00b5bdec) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bdf0`](#insn-00b5bdf0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bdf4`](#insn-00b5bdf4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bdf8`](#insn-00b5bdf8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bdfc`](#insn-00b5bdfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5be00`](#insn-00b5be00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5be14`](#insn-00b5be14) → [`00b5bedc`](#insn-00b5bedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5be34`](#insn-00b5be34) → [`00b5be50`](#insn-00b5be50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5be3c`](#insn-00b5be3c) → [`00b5bed4`](#insn-00b5bed4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5be48`](#insn-00b5be48) → [`00b5bed4`](#insn-00b5bed4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5be70`](#insn-00b5be70) → [`00b5be98`](#insn-00b5be98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5be88`](#insn-00b5be88) → [`00c590f0`](../00c59/00c590f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590f0` · 推定シンボル `None` · 推定型 `None`
- [`00b5be8c`](#insn-00b5be8c) → [`00b5be98`](#insn-00b5be98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5be90`](#insn-00b5be90) → [`00b5bea0`](#insn-00b5bea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5be94`](#insn-00b5be94) → [`00b5beb8`](#insn-00b5beb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5be9c`](#insn-00b5be9c) → [`00b5beb0`](#insn-00b5beb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bea4`](#insn-00b5bea4) → [`00b5bee4`](#insn-00b5bee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5beac`](#insn-00b5beac) → [`00b5be4c`](#insn-00b5be4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5beb0`](#insn-00b5beb0) → [`00b5be38`](#insn-00b5be38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bec8`](#insn-00b5bec8) → [`00c590f0`](../00c59/00c590f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590f0` · 推定シンボル `None` · 推定型 `None`
- [`00b5becc`](#insn-00b5becc) → [`00b5be38`](#insn-00b5be38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bed0`](#insn-00b5bed0) → [`00b5be40`](#insn-00b5be40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bed8`](#insn-00b5bed8) → [`00b5beec`](#insn-00b5beec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bee0`](#insn-00b5bee0) → [`00b5beec`](#insn-00b5beec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bef0`](#insn-00b5bef0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bef4`](#insn-00b5bef4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bef8`](#insn-00b5bef8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5befc`](#insn-00b5befc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bf00`](#insn-00b5bf00) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5bdec`](#insn-00b5bdec)

~~~json
{
  "source": "00b5bdec",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bdf0`](#insn-00b5bdf0)

~~~json
{
  "source": "00b5bdf0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bdf4`](#insn-00b5bdf4)

~~~json
{
  "source": "00b5bdf4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bdf8`](#insn-00b5bdf8)

~~~json
{
  "source": "00b5bdf8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bdfc`](#insn-00b5bdfc)

~~~json
{
  "source": "00b5bdfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5be00`](#insn-00b5be00)

~~~json
{
  "source": "00b5be00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5be14`](#insn-00b5be14)

~~~json
{
  "source": "00b5be14",
  "target": "00b5bedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5be34`](#insn-00b5be34)

~~~json
{
  "source": "00b5be34",
  "target": "00b5be50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5be3c`](#insn-00b5be3c)

~~~json
{
  "source": "00b5be3c",
  "target": "00b5bed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5be48`](#insn-00b5be48)

~~~json
{
  "source": "00b5be48",
  "target": "00b5bed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5be70`](#insn-00b5be70)

~~~json
{
  "source": "00b5be70",
  "target": "00b5be98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5be88`](#insn-00b5be88)

~~~json
{
  "source": "00b5be88",
  "target": "00c590f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5be8c`](#insn-00b5be8c)

~~~json
{
  "source": "00b5be8c",
  "target": "00b5be98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5be90`](#insn-00b5be90)

~~~json
{
  "source": "00b5be90",
  "target": "00b5bea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5be94`](#insn-00b5be94)

~~~json
{
  "source": "00b5be94",
  "target": "00b5beb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5be9c`](#insn-00b5be9c)

~~~json
{
  "source": "00b5be9c",
  "target": "00b5beb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bea4`](#insn-00b5bea4)

~~~json
{
  "source": "00b5bea4",
  "target": "00b5bee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5beac`](#insn-00b5beac)

~~~json
{
  "source": "00b5beac",
  "target": "00b5be4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5beb0`](#insn-00b5beb0)

~~~json
{
  "source": "00b5beb0",
  "target": "00b5be38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bec8`](#insn-00b5bec8)

~~~json
{
  "source": "00b5bec8",
  "target": "00c590f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5becc`](#insn-00b5becc)

~~~json
{
  "source": "00b5becc",
  "target": "00b5be38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bed0`](#insn-00b5bed0)

~~~json
{
  "source": "00b5bed0",
  "target": "00b5be40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bed8`](#insn-00b5bed8)

~~~json
{
  "source": "00b5bed8",
  "target": "00b5beec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bee0`](#insn-00b5bee0)

~~~json
{
  "source": "00b5bee0",
  "target": "00b5beec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bef0`](#insn-00b5bef0)

~~~json
{
  "source": "00b5bef0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bef4`](#insn-00b5bef4)

~~~json
{
  "source": "00b5bef4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bef8`](#insn-00b5bef8)

~~~json
{
  "source": "00b5bef8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5befc`](#insn-00b5befc)

~~~json
{
  "source": "00b5befc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bf00`](#insn-00b5bf00)

~~~json
{
  "source": "00b5bf00",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
