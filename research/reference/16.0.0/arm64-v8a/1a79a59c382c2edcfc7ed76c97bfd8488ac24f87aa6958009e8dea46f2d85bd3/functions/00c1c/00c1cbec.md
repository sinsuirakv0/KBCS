# 00c1cbec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00ba01a4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba01a4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0074.md#compare-8c5d4f9bb72698a8a947e1a7453b2099)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00c1d014`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d014.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0088.md#compare-b7f1ddc9e2ec8693bfc71888d47c6245)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c1cbec",
  "name": "_ZNKSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_bRNS_8ios_baseEwRKNS_12basic_stringIwS3_NS_9allocatorIwEEEE",
  "size": 776,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1a7c8d53f00c32b48a3247afd1ac212f1fbeabbf7a9deb52e5e39c8c8c1bcd34",
  "source_text_sha256": "1a7c8d53f00c32b48a3247afd1ac212f1fbeabbf7a9deb52e5e39c8c8c1bcd34",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c1cbec",
        "00c1cef3"
      ]
    ],
    "bytes_sha256": "488f66468499c64f8a65ed230d694e54dec192497e43e1c84d73ba383ead6b11",
    "instruction_count": 194,
    "instruction_bytes": 776,
    "body_bytes": 776,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c05b30](../00c05/00c05b30.md)
- [00c114bc](../00c11/00c114bc.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57e70](../00c57/00c57e70.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c58260](../00c58/00c58260.md)
- [00c59c20](../00c59/00c59c20.md)
- [00c5dae0](../00c5d/00c5dae0.md)
- [00c5db80](../00c5d/00c5db80.md)
- [00c5e310](../00c5e/00c5e310.md)
- [00c5e320](../00c5e/00c5e320.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 11675 bytes

~~~c

undefined8
_ZNKSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_bRNS_8ios_baseEwRKNS_12basic_stringIwS3_NS_9allocatorIwEEEE
          (undefined8 param_1,undefined8 param_2,uint param_3,long param_4,undefined4 param_5,
          byte *param_6)

{
  ulong uVar1;
  ulong uVar2;
  byte *pbVar3;
  int iVar4;
  byte bVar5;
  undefined *puVar6;
  bool bVar7;
  int iVar8;
  undefined ***__ptr;
  undefined8 uVar9;
  ulong uVar10;
  long *plVar11;
  undefined ***pppuVar12;
  undefined8 local_270;
  undefined8 uStack_268;
  undefined **local_260 [50];
  int local_cc;
  ulong local_c8;
  ulong local_c0;
  void *local_b8;
  undefined *local_b0;
  ulong local_a8;
  void *local_a0;
  undefined ***local_98;
  undefined8 uStack_90;
  void *local_88;
  undefined4 local_7c;
  undefined4 uStack_78;
  undefined1 auStack_74 [4];
  long local_70 [2];
  
                    /* catch() { ... } // from try @ 00c1bdd0 with catch @ 00c1cbfc */
                    /* catch() { ... } // from try @ 00c1bdc4 with catch @ 00c1cc10 */
                    /* catch() { ... } // from try @ 00c1bd7c with catch @ 00c1cc14 */
                    /* catch() { ... } // from try @ 00c1bbe4 with catch @ 00c1cc18 */
  _ZNKSt6__ndk18ios_base6getlocEv(local_70,param_4);
  puVar6 = PTR__ZNSt6__ndk15ctypeIwE2idE_00c9b740;
                    /* catch() { ... } // from try @ 00c1bbd4 with catch @ 00c1cc30 */
  local_b0 = PTR__ZNSt6__ndk15ctypeIwE2idE_00c9b740;
                    /* catch() { ... } // from try @ 00c1bbc8 with catch @ 00c1cc44 */
                    /* catch() { ... } // from try @ 00c1bb8c with catch @ 00c1cc48 */
  if (*(long *)PTR__ZNSt6__ndk15ctypeIwE2idE_00c9b740 != -1) {
                    /* catch() { ... } // from try @ 00c1ba54 with catch @ 00c1cc4c */
    local_260[0] = &local_b0;
    local_98 = local_260;
                    /* catch() { ... } // from try @ 00c1ba44 with catch @ 00c1cc64 */
    _ZNSt6__ndk111__call_onceERVmPvPFvS2_E
              (PTR__ZNSt6__ndk15ctypeIwE2idE_00c9b740,&local_98,FUN_00c35b90);
  }
                    /* catch() { ... } // from try @ 00c1ba38 with catch @ 00c1cc78 */
                    /* catch() { ... } // from try @ 00c1b9f8 with catch @ 00c1cc7c */
                    /* catch() { ... } // from try @ 00c1b97c with catch @ 00c1cc80 */
                    /* catch() { ... } // from try @ 00c1b7f4 with catch @ 00c1cc90 */
  if (((ulong)(*(long *)(local_70[0] + 0x18) - *(long *)(local_70[0] + 0x10) >> 3) <=
       (long)*(int *)(puVar6 + 8) - 1U) ||
     (plVar11 = *(long **)(*(long *)(local_70[0] + 0x10) + ((long)*(int *)(puVar6 + 8) - 1U) * 8),
     plVar11 == (long *)0x0)) {
                    /* WARNING: Subroutine does not return */
    FUN_00c05b30();
  }
  bVar5 = *param_6;
  uVar1 = (ulong)(bVar5 >> 1);
  if ((bVar5 & 1) != 0) {
    uVar1 = *(ulong *)(param_6 + 8);
  }
                    /* catch() { ... } // from try @ 00c1b7e4 with catch @ 00c1cca8 */
  if (uVar1 == 0) {
    bVar7 = false;
  }
  else {
    pbVar3 = param_6 + 4;
                    /* catch() { ... } // from try @ 00c1b7d8 with catch @ 00c1ccbc */
    if ((bVar5 & 1) != 0) {
      pbVar3 = *(byte **)(param_6 + 0x10);
    }
                    /* catch() { ... } // from try @ 00c1b794 with catch @ 00c1ccc0 */
    iVar4 = *(int *)pbVar3;
                    /* catch() { ... } // from try @ 00c1b694 with catch @ 00c1ccc4 */
    iVar8 = (**(code **)(*plVar11 + 0x58))(plVar11,0x2d);
    bVar7 = iVar4 == iVar8;
                    /* catch() { ... } // from try @ 00c1b684 with catch @ 00c1ccdc */
  }
  local_98 = (undefined ***)0x0;
  uStack_90 = 0;
  local_88 = (void *)0x0;
                    /* catch() { ... } // from try @ 00c1b678 with catch @ 00c1ccf0 */
  local_b0 = (undefined *)0x0;
  local_a8 = 0;
                    /* catch() { ... } // from try @ 00c1b630 with catch @ 00c1ccf4 */
  local_a0 = (void *)0x0;
                    /* catch() { ... } // from try @ 00c1b480 with catch @ 00c1ccf8 */
  local_c8 = 0;
  local_c0 = 0;
  local_b8 = (void *)0x0;
                    /* catch() { ... } // from try @ 00c1b470 with catch @ 00c1cd10 */
  _ZNSt6__ndk111__money_putIwE13__gather_infoEbbRKNS_6localeERNS_10money_base7patternERwS8_RNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERNS9_IwNSA_IwEENSC_IwEEEESJ_Ri
            (param_3 & 1,bVar7,local_70,auStack_74,&uStack_78,&local_7c,&local_98,&local_b0,
             &local_c8,&local_cc);
  bVar5 = *param_6;
  uVar1 = (ulong)(bVar5 >> 1);
                    /* catch() { ... } // from try @ 00c1b464 with catch @ 00c1cd48 */
  if ((bVar5 & 1) != 0) {
    uVar1 = *(ulong *)(param_6 + 8);
  }
  if (local_cc < (int)uVar1) {
                    /* catch() { ... } // from try @ 00c1b414 with catch @ 00c1cd58 */
                    /* catch() { ... } // from try @ 00c1b408 with catch @ 00c1cd5c */
                    /* catch() { ... } // from try @ 00c1bc44 with catch @ 00c1cd64
                       catch() { ... } // from try @ 00c1bc84 with catch @ 00c1cd64
                       catch() { ... } // from try @ 00c1bcc8 with catch @ 00c1cd64 */
                    /* catch() { ... } // from try @ 00c1bc38 with catch @ 00c1cd68
                       catch() { ... } // from try @ 00c1bc78 with catch @ 00c1cd68
                       catch() { ... } // from try @ 00c1bcbc with catch @ 00c1cd68 */
                    /* catch() { ... } // from try @ 00c1c8f8 with catch @ 00c1cd6c */
    uVar10 = (ulong)((byte)local_c8 >> 1);
                    /* catch() { ... } // from try @ 00c1b84c with catch @ 00c1cd70 */
    if ((local_c8 & 1) != 0) {
      uVar10 = local_c0;
    }
                    /* catch() { ... } // from try @ 00c1c434 with catch @ 00c1cd74 */
                    /* catch() { ... } // from try @ 00c1c2f0 with catch @ 00c1cd78 */
    uVar2 = (ulong)((byte)local_b0 >> 1);
    if (((ulong)local_b0 & 1) != 0) {
      uVar2 = local_a8;
    }
    uVar10 = (uVar1 * 2 - (long)local_cc) + uVar10 + uVar2 + 1;
  }
  else {
                    /* catch() { ... } // from try @ 00c1c5f4 with catch @ 00c1cd94 */
                    /* catch() { ... } // from try @ 00c1cb68 with catch @ 00c1cd98
                       catch() { ... } // from try @ 00c1cb9c with catch @ 00c1cd98 */
                    /* catch() { ... } // from try @ 00c1cb4c with catch @ 00c1cd9c
                       catch() { ... } // from try @ 00c1cb84 with catch @ 00c1cd9c */
                    /* catch() { ... } // from try @ 00c1c408 with catch @ 00c1cda0 */
                    /* catch() { ... } // from try @ 00c1c2c0 with catch @ 00c1cda4 */
                    /* catch() { ... } // from try @ 00c1bf58 with catch @ 00c1cda8 */
    uVar10 = (ulong)((byte)local_c8 >> 1);
    if ((local_c8 & 1) != 0) {
      uVar10 = local_c0;
    }
    uVar2 = (ulong)((byte)local_b0 >> 1);
                    /* catch() { ... } // from try @ 00c1c838 with catch @ 00c1cdb8 */
    if (((ulong)local_b0 & 1) != 0) {
      uVar2 = local_a8;
    }
                    /* catch() { ... } // from try @ 00c1b628 with catch @ 00c1cdbc
                       catch() { ... } // from try @ 00c1b78c with catch @ 00c1cdbc
                       catch() { ... } // from try @ 00c1b840 with catch @ 00c1cdbc
                       catch() { ... } // from try @ 00c1b94c with catch @ 00c1cdbc
                       catch() { ... } // from try @ 00c1bb84 with catch @ 00c1cdbc
                       catch() { ... } // from try @ 00c1bd00 with catch @ 00c1cdbc
                       catch() { ... } // from try @ 00c1c024 with catch @ 00c1cdbc
                       catch() { ... } // from try @ 00c1c134 with catch @ 00c1cdbc
                       catch() { ... } // from try @ 00c1c1e0 with catch @ 00c1cdbc
                       catch() { ... } // from try @ 00c1c640 with catch @ 00c1cdbc
                       catch() { ... } // from try @ 00c1c95c with catch @ 00c1cdbc */
                    /* catch() { ... } // from try @ 00c1cae8 with catch @ 00c1cdc0
                       catch() { ... } // from try @ 00c1cb34 with catch @ 00c1cdc0 */
                    /* catch() { ... } // from try @ 00c1cacc with catch @ 00c1cdc4
                       catch() { ... } // from try @ 00c1cb1c with catch @ 00c1cdc4 */
    uVar10 = (long)local_cc + uVar10 + uVar2 + 2;
  }
                    /* catch() { ... } // from try @ 00c1cab0 with catch @ 00c1cdc8
                       catch() { ... } // from try @ 00c1cb04 with catch @ 00c1cdc8 */
                    /* catch() { ... } // from try @ 00c1bf10 with catch @ 00c1cdcc */
  if (100 < uVar10) {
    __ptr = malloc(uVar10 << 2);
    pppuVar12 = __ptr;
    if (__ptr != (undefined ***)0x0) goto LAB_00c1cdf4;
    _ZSt17__throw_bad_allocv();
  }
  __ptr = (undefined ***)0x0;
  pppuVar12 = local_260;
LAB_00c1cdf4:
  pbVar3 = param_6 + 4;
  if ((bVar5 & 1) != 0) {
    pbVar3 = *(byte **)(param_6 + 0x10);
  }
                    /* catch() { ... } // from try @ 00c1beb0 with catch @ 00c1ce40 */
                    /* catch() { ... } // from try @ 00c1b9d4 with catch @ 00c1ce44 */
                    /* catch() { ... } // from try @ 00c1bb24 with catch @ 00c1ce48 */
                    /* catch() { ... } // from try @ 00c1c3ac with catch @ 00c1ce4c */
                    /* catch() { ... } // from try @ 00c1c244 with catch @ 00c1ce50 */
  _ZNSt6__ndk111__money_putIwE8__formatEPwRS2_S3_jPKwS5_RKNS_5ctypeIwEEbRKNS_10money_base7patternEwwRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERKNSE_IwNSF_IwEENSH_IwEEEESQ_i
            (pppuVar12,&uStack_268,&local_270,*(undefined4 *)(param_4 + 8),pbVar3,pbVar3 + uVar1 * 4
             ,plVar11,bVar7,auStack_74,uStack_78,local_7c,&local_98,&local_b0,&local_c8,local_cc);
                    /* catch() { ... } // from try @ 00c1c0a0 with catch @ 00c1ce54 */
                    /* catch() { ... } // from try @ 00c1bea0 with catch @ 00c1ce58 */
                    /* catch() { ... } // from try @ 00c1b730 with catch @ 00c1ce5c */
                    /* catch() { ... } // from try @ 00c1b9c8 with catch @ 00c1ce60 */
                    /* catch() { ... } // from try @ 00c1b528 with catch @ 00c1ce64 */
                    /* catch() { ... } // from try @ 00c1c77c with catch @ 00c1ce68 */
  uVar9 = FUN_00c114bc(param_2,pppuVar12,uStack_268,local_270,param_4,param_5);
                    /* catch() { ... } // from try @ 00c1c6d4 with catch @ 00c1ce6c */
                    /* catch() { ... } // from try @ 00c1c3cc with catch @ 00c1ce70 */
  if (__ptr != (undefined ***)0x0) {
                    /* catch() { ... } // from try @ 00c1c6c8 with catch @ 00c1ce74
                       catch() { ... } // from try @ 00c1c828 with catch @ 00c1ce74 */
                    /* catch() { ... } // from try @ 00c1c4cc with catch @ 00c1ce78 */
    free(__ptr);
  }
                    /* catch() { ... } // from try @ 00c1c264 with catch @ 00c1ce7c */
                    /* catch() { ... } // from try @ 00c1bec0 with catch @ 00c1ce80 */
  if ((local_c8 & 1) != 0) {
    _ZdlPv(local_b8);
  }
  if (((ulong)local_b0 & 1) != 0) {
    _ZdlPv(local_a0);
  }
  if (((ulong)local_98 & 1) != 0) {
    _ZdlPv(local_88);
  }
  _ZNSt6__ndk16localeD1Ev(local_70);
                    /* catch() { ... } // from try @ 00c1b534 with catch @ 00c1ceb0 */
                    /* catch() { ... } // from try @ 00c1c0a8 with catch @ 00c1ceb4 */
                    /* catch() { ... } // from try @ 00c1c528 with catch @ 00c1ceb8 */
                    /* catch() { ... } // from try @ 00c1bb60 with catch @ 00c1cebc */
                    /* catch() { ... } // from try @ 00c1b768 with catch @ 00c1cec0 */
  return uVar9;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c1cbec"></a> `00c1cbec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c1cbf0"></a> `00c1cbf0` | `fd 7b ba a9` | stp x29,x30,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00c1cbf4"></a> `00c1cbf4` | `fc 6f 01 a9` | stp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c1cbf8"></a> `00c1cbf8` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c1cbfc"></a> `00c1cbfc` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c1cc00"></a> `00c1cc00` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00c1cc04"></a> `00c1cc04` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00c1cc08"></a> `00c1cc08` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00c1cc0c"></a> `00c1cc0c` | `ff 43 09 d1` | sub sp,sp,#0x250 | `FALL_THROUGH`
<a id="insn-00c1cc10"></a> `00c1cc10` | `a8 43 00 d1` | sub x8,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00c1cc14"></a> `00c1cc14` | `e0 03 03 aa` | mov x0,x3 | `FALL_THROUGH`
<a id="insn-00c1cc18"></a> `00c1cc18` | `f6 03 05 aa` | mov x22,x5 | `FALL_THROUGH`
<a id="insn-00c1cc1c"></a> `00c1cc1c` | `fa 03 04 2a` | mov w26,w4 | `FALL_THROUGH`
<a id="insn-00c1cc20"></a> `00c1cc20` | `f4 03 03 aa` | mov x20,x3 | `FALL_THROUGH`
<a id="insn-00c1cc24"></a> `00c1cc24` | `f9 03 02 2a` | mov w25,w2 | `FALL_THROUGH`
<a id="insn-00c1cc28"></a> `00c1cc28` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00c1cc2c"></a> `00c1cc2c` | `91 ec 00 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00c1cc30"></a> `00c1cc30` | `f7 03 00 f0` | adrp x23,0xc9b000 | `FALL_THROUGH`
<a id="insn-00c1cc34"></a> `00c1cc34` | `f7 a2 43 f9` | ldr x23,[x23, #0x740] | `FALL_THROUGH`
<a id="insn-00c1cc38"></a> `00c1cc38` | `b3 03 5f f8` | ldur x19,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00c1cc3c"></a> `00c1cc3c` | `b7 03 1b f8` | stur x23,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00c1cc40"></a> `00c1cc40` | `e8 fe df c8` | ldar x8,[x23] | `FALL_THROUGH`
<a id="insn-00c1cc44"></a> `00c1cc44` | `1f 05 00 b1` | cmn x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c1cc48"></a> `00c1cc48` | `60 01 00 54` | b.eq 0x00c1cc74 | `CONDITIONAL_JUMP`
<a id="insn-00c1cc4c"></a> `00c1cc4c` | `a8 43 01 d1` | sub x8,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00c1cc50"></a> `00c1cc50` | `e9 43 01 91` | add x9,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00c1cc54"></a> `00c1cc54` | `e8 2b 00 f9` | str x8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00c1cc58"></a> `00c1cc58` | `a9 83 1c f8` | stur x9,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00c1cc5c"></a> `00c1cc5c` | `e0 03 00 f0` | adrp x0,0xc9b000 | `FALL_THROUGH`
<a id="insn-00c1cc60"></a> `00c1cc60` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00c1cc64"></a> `00c1cc64` | `62 79 0c 10` | adr x2,0xc35b90 | `FALL_THROUGH`
<a id="insn-00c1cc68"></a> `00c1cc68` | `00 a0 43 f9` | ldr x0,[x0, #0x740] | `FALL_THROUGH`
<a id="insn-00c1cc6c"></a> `00c1cc6c` | `a1 e3 00 d1` | sub x1,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00c1cc70"></a> `00c1cc70` | `9c 03 01 94` | bl 0x00c5dae0 | `UNCONDITIONAL_CALL`
<a id="insn-00c1cc74"></a> `00c1cc74` | `68 2a 41 a9` | ldp x8,x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c1cc78"></a> `00c1cc78` | `e9 0a 80 b9` | ldrsw x9,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00c1cc7c"></a> `00c1cc7c` | `29 05 00 d1` | sub x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00c1cc80"></a> `00c1cc80` | `4a 01 08 cb` | sub x10,x10,x8 | `FALL_THROUGH`
<a id="insn-00c1cc84"></a> `00c1cc84` | `3f 0d 8a eb` | cmp x9,x10, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00c1cc88"></a> `00c1cc88` | `42 13 00 54` | b.cs 0x00c1cef0 | `CONDITIONAL_JUMP`
<a id="insn-00c1cc8c"></a> `00c1cc8c` | `17 79 69 f8` | ldr x23,[x8, x9, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00c1cc90"></a> `00c1cc90` | `17 13 00 b4` | cbz x23,0x00c1cef0 | `CONDITIONAL_JUMP`
<a id="insn-00c1cc94"></a> `00c1cc94` | `c8 02 40 39` | ldrb w8,[x22] | `FALL_THROUGH`
<a id="insn-00c1cc98"></a> `00c1cc98` | `c9 06 40 f9` | ldr x9,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00c1cc9c"></a> `00c1cc9c` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c1cca0"></a> `00c1cca0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00c1cca4"></a> `00c1cca4` | `49 01 89 9a` | csel x9,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00c1cca8"></a> `00c1cca8` | `c9 01 00 b4` | cbz x9,0x00c1cce0 | `CONDITIONAL_JUMP`
<a id="insn-00c1ccac"></a> `00c1ccac` | `c9 0a 40 f9` | ldr x9,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00c1ccb0"></a> `00c1ccb0` | `ca 12 00 91` | add x10,x22,#0x4 | `FALL_THROUGH`
<a id="insn-00c1ccb4"></a> `00c1ccb4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00c1ccb8"></a> `00c1ccb8` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00c1ccbc"></a> `00c1ccbc` | `49 01 89 9a` | csel x9,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00c1ccc0"></a> `00c1ccc0` | `33 01 40 b9` | ldr w19,[x9] | `FALL_THROUGH`
<a id="insn-00c1ccc4"></a> `00c1ccc4` | `08 2d 40 f9` | ldr x8,[x8, #0x58] | `FALL_THROUGH`
<a id="insn-00c1ccc8"></a> `00c1ccc8` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00c1cccc"></a> `00c1cccc` | `a1 05 80 52` | mov w1,#0x2d | `FALL_THROUGH`
<a id="insn-00c1ccd0"></a> `00c1ccd0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c1ccd4"></a> `00c1ccd4` | `7f 02 00 6b` | cmp w19,w0 | `FALL_THROUGH`
<a id="insn-00c1ccd8"></a> `00c1ccd8` | `f8 17 9f 1a` | cset w24,eq | `FALL_THROUGH`
<a id="insn-00c1ccdc"></a> `00c1ccdc` | `02 00 00 14` | b 0x00c1cce4 | `UNCONDITIONAL_JUMP`
<a id="insn-00c1cce0"></a> `00c1cce0` | `f8 03 1f 2a` | mov w24,wzr | `FALL_THROUGH`
<a id="insn-00c1cce4"></a> `00c1cce4` | `f4 1f 00 f9` | str x20,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00c1cce8"></a> `00c1cce8` | `bf ff 3c a9` | stp xzr,xzr,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00c1ccec"></a> `00c1ccec` | `bf 83 1d f8` | stur xzr,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00c1ccf0"></a> `00c1ccf0` | `bf 7f 3b a9` | stp xzr,xzr,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00c1ccf4"></a> `00c1ccf4` | `bf 03 1c f8` | stur xzr,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00c1ccf8"></a> `00c1ccf8` | `bf ff 39 a9` | stp xzr,xzr,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00c1ccfc"></a> `00c1ccfc` | `bf 83 1a f8` | stur xzr,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-00c1cd00"></a> `00c1cd00` | `a8 b3 01 d1` | sub x8,x29,#0x6c | `FALL_THROUGH`
<a id="insn-00c1cd04"></a> `00c1cd04` | `a9 a3 01 d1` | sub x9,x29,#0x68 | `FALL_THROUGH`
<a id="insn-00c1cd08"></a> `00c1cd08` | `20 03 00 12` | and w0,w25,#0x1 | `FALL_THROUGH`
<a id="insn-00c1cd0c"></a> `00c1cd0c` | `a2 43 00 d1` | sub x2,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00c1cd10"></a> `00c1cd10` | `a3 53 00 d1` | sub x3,x29,#0x14 | `FALL_THROUGH`
<a id="insn-00c1cd14"></a> `00c1cd14` | `a4 63 00 d1` | sub x4,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00c1cd18"></a> `00c1cd18` | `a5 73 00 d1` | sub x5,x29,#0x1c | `FALL_THROUGH`
<a id="insn-00c1cd1c"></a> `00c1cd1c` | `a6 e3 00 d1` | sub x6,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00c1cd20"></a> `00c1cd20` | `a7 43 01 d1` | sub x7,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00c1cd24"></a> `00c1cd24` | `e1 03 18 2a` | mov w1,w24 | `FALL_THROUGH`
<a id="insn-00c1cd28"></a> `00c1cd28` | `e9 23 00 a9` | stp x9,x8,[sp] | `FALL_THROUGH`
<a id="insn-00c1cd2c"></a> `00c1cd2c` | `79 05 01 94` | bl 0x00c5e310 | `UNCONDITIONAL_CALL`
<a id="insn-00c1cd30"></a> `00c1cd30` | `dc 02 40 39` | ldrb w28,[x22] | `FALL_THROUGH`
<a id="insn-00c1cd34"></a> `00c1cd34` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00c1cd38"></a> `00c1cd38` | `f4 03 15 aa` | mov x20,x21 | `FALL_THROUGH`
<a id="insn-00c1cd3c"></a> `00c1cd3c` | `bb 43 99 b8` | ldursw x27,[x29, #-0x6c] | `FALL_THROUGH`
<a id="insn-00c1cd40"></a> `00c1cd40` | `89 ff 41 d3` | lsr x9,x28,#0x1 | `FALL_THROUGH`
<a id="insn-00c1cd44"></a> `00c1cd44` | `9f 03 00 72` | tst w28,#0x1 | `FALL_THROUGH`
<a id="insn-00c1cd48"></a> `00c1cd48` | `33 01 88 9a` | csel x19,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00c1cd4c"></a> `00c1cd4c` | `7f 03 13 6b` | cmp w27,w19 | `FALL_THROUGH`
<a id="insn-00c1cd50"></a> `00c1cd50` | `2a 02 00 54` | b.ge 0x00c1cd94 | `CONDITIONAL_JUMP`
<a id="insn-00c1cd54"></a> `00c1cd54` | `a8 83 59 38` | ldurb w8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00c1cd58"></a> `00c1cd58` | `a9 03 5b 38` | ldurb w9,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00c1cd5c"></a> `00c1cd5c` | `aa 03 5a f8` | ldur x10,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00c1cd60"></a> `00c1cd60` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c1cd64"></a> `00c1cd64` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00c1cd68"></a> `00c1cd68` | `a8 83 5b f8` | ldur x8,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00c1cd6c"></a> `00c1cd6c` | `2c fd 41 d3` | lsr x12,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00c1cd70"></a> `00c1cd70` | `6a 01 8a 9a` | csel x10,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00c1cd74"></a> `00c1cd74` | `6b 02 1b cb` | sub x11,x19,x27 | `FALL_THROUGH`
<a id="insn-00c1cd78"></a> `00c1cd78` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00c1cd7c"></a> `00c1cd7c` | `88 01 88 9a` | csel x8,x12,x8,eq | `FALL_THROUGH`
<a id="insn-00c1cd80"></a> `00c1cd80` | `69 07 0b 8b` | add x9,x27,x11, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00c1cd84"></a> `00c1cd84` | `48 01 08 8b` | add x8,x10,x8 | `FALL_THROUGH`
<a id="insn-00c1cd88"></a> `00c1cd88` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00c1cd8c"></a> `00c1cd8c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c1cd90"></a> `00c1cd90` | `0e 00 00 14` | b 0x00c1cdc8 | `UNCONDITIONAL_JUMP`
<a id="insn-00c1cd94"></a> `00c1cd94` | `a8 83 59 38` | ldurb w8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00c1cd98"></a> `00c1cd98` | `a9 03 5b 38` | ldurb w9,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00c1cd9c"></a> `00c1cd9c` | `aa 03 5a f8` | ldur x10,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00c1cda0"></a> `00c1cda0` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c1cda4"></a> `00c1cda4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00c1cda8"></a> `00c1cda8` | `a8 83 5b f8` | ldur x8,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00c1cdac"></a> `00c1cdac` | `2c fd 41 d3` | lsr x12,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00c1cdb0"></a> `00c1cdb0` | `6a 01 8a 9a` | csel x10,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00c1cdb4"></a> `00c1cdb4` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00c1cdb8"></a> `00c1cdb8` | `88 01 88 9a` | csel x8,x12,x8,eq | `FALL_THROUGH`
<a id="insn-00c1cdbc"></a> `00c1cdbc` | `69 03 0a 8b` | add x9,x27,x10 | `FALL_THROUGH`
<a id="insn-00c1cdc0"></a> `00c1cdc0` | `28 01 08 8b` | add x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00c1cdc4"></a> `00c1cdc4` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00c1cdc8"></a> `00c1cdc8` | `f5 03 1a 2a` | mov w21,w26 | `FALL_THROUGH`
<a id="insn-00c1cdcc"></a> `00c1cdcc` | `1f 95 01 f1` | cmp x8,#0x65 | `FALL_THROUGH`
<a id="insn-00c1cdd0"></a> `00c1cdd0` | `e3 00 00 54` | b.cc 0x00c1cdec | `CONDITIONAL_JUMP`
<a id="insn-00c1cdd4"></a> `00c1cdd4` | `00 f5 7e d3` | lsl x0,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00c1cdd8"></a> `00c1cdd8` | `92 f3 00 94` | bl 0x00c59c20 | `UNCONDITIONAL_CALL`
<a id="insn-00c1cddc"></a> `00c1cddc` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00c1cde0"></a> `00c1cde0` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00c1cde4"></a> `00c1cde4` | `80 00 00 b5` | cbnz x0,0x00c1cdf4 | `CONDITIONAL_JUMP`
<a id="insn-00c1cde8"></a> `00c1cde8` | `66 03 01 94` | bl 0x00c5db80 | `UNCONDITIONAL_CALL`
<a id="insn-00c1cdec"></a> `00c1cdec` | `f9 03 1f aa` | mov x25,xzr | `FALL_THROUGH`
<a id="insn-00c1cdf0"></a> `00c1cdf0` | `fa 43 01 91` | add x26,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00c1cdf4"></a> `00c1cdf4` | `c8 0a 40 f9` | ldr x8,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00c1cdf8"></a> `00c1cdf8` | `c9 12 00 91` | add x9,x22,#0x4 | `FALL_THROUGH`
<a id="insn-00c1cdfc"></a> `00c1cdfc` | `9f 03 00 72` | tst w28,#0x1 | `FALL_THROUGH`
<a id="insn-00c1ce00"></a> `00c1ce00` | `f6 1f 40 f9` | ldr x22,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00c1ce04"></a> `00c1ce04` | `24 01 88 9a` | csel x4,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00c1ce08"></a> `00c1ce08` | `a9 a3 7c 29` | ldp w9,w8,[x29, #-0x1c] | `FALL_THROUGH`
<a id="insn-00c1ce0c"></a> `00c1ce0c` | `c3 0a 40 b9` | ldr w3,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00c1ce10"></a> `00c1ce10` | `85 08 13 8b` | add x5,x4,x19, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00c1ce14"></a> `00c1ce14` | `aa a3 01 d1` | sub x10,x29,#0x68 | `FALL_THROUGH`
<a id="insn-00c1ce18"></a> `00c1ce18` | `ab 43 01 d1` | sub x11,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00c1ce1c"></a> `00c1ce1c` | `e1 23 01 91` | add x1,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00c1ce20"></a> `00c1ce20` | `eb 2b 02 a9` | stp x11,x10,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c1ce24"></a> `00c1ce24` | `aa e3 00 d1` | sub x10,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00c1ce28"></a> `00c1ce28` | `e2 03 01 91` | add x2,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00c1ce2c"></a> `00c1ce2c` | `ea 0f 00 f9` | str x10,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00c1ce30"></a> `00c1ce30` | `aa 53 00 d1` | sub x10,x29,#0x14 | `FALL_THROUGH`
<a id="insn-00c1ce34"></a> `00c1ce34` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00c1ce38"></a> `00c1ce38` | `e6 03 17 aa` | mov x6,x23 | `FALL_THROUGH`
<a id="insn-00c1ce3c"></a> `00c1ce3c` | `e7 03 18 2a` | mov w7,w24 | `FALL_THROUGH`
<a id="insn-00c1ce40"></a> `00c1ce40` | `fb 33 00 b9` | str w27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c1ce44"></a> `00c1ce44` | `e9 13 00 b9` | str w9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c1ce48"></a> `00c1ce48` | `e8 0b 00 b9` | str w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00c1ce4c"></a> `00c1ce4c` | `ea 03 00 f9` | str x10,[sp] | `FALL_THROUGH`
<a id="insn-00c1ce50"></a> `00c1ce50` | `34 05 01 94` | bl 0x00c5e320 | `UNCONDITIONAL_CALL`
<a id="insn-00c1ce54"></a> `00c1ce54` | `e3 0b 44 a9` | ldp x3,x2,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00c1ce58"></a> `00c1ce58` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00c1ce5c"></a> `00c1ce5c` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00c1ce60"></a> `00c1ce60` | `e4 03 16 aa` | mov x4,x22 | `FALL_THROUGH`
<a id="insn-00c1ce64"></a> `00c1ce64` | `e5 03 15 2a` | mov w5,w21 | `FALL_THROUGH`
<a id="insn-00c1ce68"></a> `00c1ce68` | `95 d1 ff 97` | bl 0x00c114bc | `UNCONDITIONAL_CALL`
<a id="insn-00c1ce6c"></a> `00c1ce6c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00c1ce70"></a> `00c1ce70` | `79 00 00 b4` | cbz x25,0x00c1ce7c | `CONDITIONAL_JUMP`
<a id="insn-00c1ce74"></a> `00c1ce74` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00c1ce78"></a> `00c1ce78` | `fa ec 00 94` | bl 0x00c58260 | `UNCONDITIONAL_CALL`
<a id="insn-00c1ce7c"></a> `00c1ce7c` | `a8 83 59 38` | ldurb w8,[x29, #-0x68] | `FALL_THROUGH`
<a id="insn-00c1ce80"></a> `00c1ce80` | `68 02 00 37` | tbnz w8,#0x0,0x00c1cecc | `CONDITIONAL_JUMP`
<a id="insn-00c1ce84"></a> `00c1ce84` | `a8 03 5b 38` | ldurb w8,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00c1ce88"></a> `00c1ce88` | `a8 02 00 37` | tbnz w8,#0x0,0x00c1cedc | `CONDITIONAL_JUMP`
<a id="insn-00c1ce8c"></a> `00c1ce8c` | `a8 83 5c 38` | ldurb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00c1ce90"></a> `00c1ce90` | `68 00 00 36` | tbz w8,#0x0,0x00c1ce9c | `CONDITIONAL_JUMP`
<a id="insn-00c1ce94"></a> `00c1ce94` | `a0 83 5d f8` | ldur x0,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00c1ce98"></a> `00c1ce98` | `06 eb 00 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00c1ce9c"></a> `00c1ce9c` | `a0 43 00 d1` | sub x0,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00c1cea0"></a> `00c1cea0` | `fc eb 00 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00c1cea4"></a> `00c1cea4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00c1cea8"></a> `00c1cea8` | `ff 43 09 91` | add sp,sp,#0x250 | `FALL_THROUGH`
<a id="insn-00c1ceac"></a> `00c1ceac` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00c1ceb0"></a> `00c1ceb0` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00c1ceb4"></a> `00c1ceb4` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c1ceb8"></a> `00c1ceb8` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c1cebc"></a> `00c1cebc` | `fc 6f 41 a9` | ldp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c1cec0"></a> `00c1cec0` | `fd 7b c6 a8` | ldp x29,x30,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00c1cec4"></a> `00c1cec4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c1cec8"></a> `00c1cec8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c1cecc"></a> `00c1cecc` | `a0 83 5a f8` | ldur x0,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-00c1ced0"></a> `00c1ced0` | `f8 ea 00 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00c1ced4"></a> `00c1ced4` | `a8 03 5b 38` | ldurb w8,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00c1ced8"></a> `00c1ced8` | `a8 fd 07 36` | tbz w8,#0x0,0x00c1ce8c | `CONDITIONAL_JUMP`
<a id="insn-00c1cedc"></a> `00c1cedc` | `a0 03 5c f8` | ldur x0,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00c1cee0"></a> `00c1cee0` | `f4 ea 00 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00c1cee4"></a> `00c1cee4` | `a8 83 5c 38` | ldurb w8,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00c1cee8"></a> `00c1cee8` | `68 fd 07 37` | tbnz w8,#0x0,0x00c1ce94 | `CONDITIONAL_JUMP`
<a id="insn-00c1ceec"></a> `00c1ceec` | `ec ff ff 17` | b 0x00c1ce9c | `UNCONDITIONAL_JUMP`
<a id="insn-00c1cef0"></a> `00c1cef0` | `10 a3 ff 97` | bl 0x00c05b30 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c1cbec`](#insn-00c1cbec) 範囲 `[['00c1cbec', '00c1cbfb']]`
  - `FALL_THROUGH` [`00c1cbf8`](#insn-00c1cbf8) → [`00c1cbfc`](#insn-00c1cbfc)
- ブロック [`00c1cbfc`](#insn-00c1cbfc) 範囲 `[['00c1cbfc', '00c1cc0f']]`
  - `FALL_THROUGH` [`00c1cc0c`](#insn-00c1cc0c) → [`00c1cc10`](#insn-00c1cc10)
- ブロック [`00c1cc10`](#insn-00c1cc10) 範囲 `[['00c1cc10', '00c1cc13']]`
  - `FALL_THROUGH` [`00c1cc10`](#insn-00c1cc10) → [`00c1cc14`](#insn-00c1cc14)
- ブロック [`00c1cc14`](#insn-00c1cc14) 範囲 `[['00c1cc14', '00c1cc17']]`
  - `FALL_THROUGH` [`00c1cc14`](#insn-00c1cc14) → [`00c1cc18`](#insn-00c1cc18)
- ブロック [`00c1cc18`](#insn-00c1cc18) 範囲 `[['00c1cc18', '00c1cc2f']]`
  - `FALL_THROUGH` [`00c1cc2c`](#insn-00c1cc2c) → [`00c1cc30`](#insn-00c1cc30)
- ブロック [`00c1cc30`](#insn-00c1cc30) 範囲 `[['00c1cc30', '00c1cc43']]`
  - `FALL_THROUGH` [`00c1cc40`](#insn-00c1cc40) → [`00c1cc44`](#insn-00c1cc44)
- ブロック [`00c1cc44`](#insn-00c1cc44) 範囲 `[['00c1cc44', '00c1cc47']]`
  - `FALL_THROUGH` [`00c1cc44`](#insn-00c1cc44) → [`00c1cc48`](#insn-00c1cc48)
- ブロック [`00c1cc48`](#insn-00c1cc48) 範囲 `[['00c1cc48', '00c1cc4b']]`
  - `CONDITIONAL_JUMP` [`00c1cc48`](#insn-00c1cc48) → [`00c1cc74`](#insn-00c1cc74)
  - `FALL_THROUGH` [`00c1cc48`](#insn-00c1cc48) → [`00c1cc4c`](#insn-00c1cc4c)
- ブロック [`00c1cc4c`](#insn-00c1cc4c) 範囲 `[['00c1cc4c', '00c1cc63']]`
  - `FALL_THROUGH` [`00c1cc60`](#insn-00c1cc60) → [`00c1cc64`](#insn-00c1cc64)
- ブロック [`00c1cc64`](#insn-00c1cc64) 範囲 `[['00c1cc64', '00c1cc73']]`
  - `FALL_THROUGH` [`00c1cc70`](#insn-00c1cc70) → [`00c1cc74`](#insn-00c1cc74)
- ブロック [`00c1cc74`](#insn-00c1cc74) 範囲 `[['00c1cc74', '00c1cc77']]`
  - `FALL_THROUGH` [`00c1cc74`](#insn-00c1cc74) → [`00c1cc78`](#insn-00c1cc78)
- ブロック [`00c1cc78`](#insn-00c1cc78) 範囲 `[['00c1cc78', '00c1cc7b']]`
  - `FALL_THROUGH` [`00c1cc78`](#insn-00c1cc78) → [`00c1cc7c`](#insn-00c1cc7c)
- ブロック [`00c1cc7c`](#insn-00c1cc7c) 範囲 `[['00c1cc7c', '00c1cc7f']]`
  - `FALL_THROUGH` [`00c1cc7c`](#insn-00c1cc7c) → [`00c1cc80`](#insn-00c1cc80)
- ブロック [`00c1cc80`](#insn-00c1cc80) 範囲 `[['00c1cc80', '00c1cc8b']]`
  - `CONDITIONAL_JUMP` [`00c1cc88`](#insn-00c1cc88) → [`00c1cef0`](#insn-00c1cef0)
  - `FALL_THROUGH` [`00c1cc88`](#insn-00c1cc88) → [`00c1cc8c`](#insn-00c1cc8c)
- ブロック [`00c1cc8c`](#insn-00c1cc8c) 範囲 `[['00c1cc8c', '00c1cc8f']]`
  - `FALL_THROUGH` [`00c1cc8c`](#insn-00c1cc8c) → [`00c1cc90`](#insn-00c1cc90)
- ブロック [`00c1cc90`](#insn-00c1cc90) 範囲 `[['00c1cc90', '00c1cc93']]`
  - `CONDITIONAL_JUMP` [`00c1cc90`](#insn-00c1cc90) → [`00c1cef0`](#insn-00c1cef0)
  - `FALL_THROUGH` [`00c1cc90`](#insn-00c1cc90) → [`00c1cc94`](#insn-00c1cc94)
- ブロック [`00c1cc94`](#insn-00c1cc94) 範囲 `[['00c1cc94', '00c1cca7']]`
  - `FALL_THROUGH` [`00c1cca4`](#insn-00c1cca4) → [`00c1cca8`](#insn-00c1cca8)
- ブロック [`00c1cca8`](#insn-00c1cca8) 範囲 `[['00c1cca8', '00c1ccab']]`
  - `CONDITIONAL_JUMP` [`00c1cca8`](#insn-00c1cca8) → [`00c1cce0`](#insn-00c1cce0)
  - `FALL_THROUGH` [`00c1cca8`](#insn-00c1cca8) → [`00c1ccac`](#insn-00c1ccac)
- ブロック [`00c1ccac`](#insn-00c1ccac) 範囲 `[['00c1ccac', '00c1ccbb']]`
  - `FALL_THROUGH` [`00c1ccb8`](#insn-00c1ccb8) → [`00c1ccbc`](#insn-00c1ccbc)
- ブロック [`00c1ccbc`](#insn-00c1ccbc) 範囲 `[['00c1ccbc', '00c1ccbf']]`
  - `FALL_THROUGH` [`00c1ccbc`](#insn-00c1ccbc) → [`00c1ccc0`](#insn-00c1ccc0)
- ブロック [`00c1ccc0`](#insn-00c1ccc0) 範囲 `[['00c1ccc0', '00c1ccc3']]`
  - `FALL_THROUGH` [`00c1ccc0`](#insn-00c1ccc0) → [`00c1ccc4`](#insn-00c1ccc4)
- ブロック [`00c1ccc4`](#insn-00c1ccc4) 範囲 `[['00c1ccc4', '00c1ccdb']]`
  - `FALL_THROUGH` [`00c1ccd8`](#insn-00c1ccd8) → [`00c1ccdc`](#insn-00c1ccdc)
- ブロック [`00c1ccdc`](#insn-00c1ccdc) 範囲 `[['00c1ccdc', '00c1ccdf']]`
  - `UNCONDITIONAL_JUMP` [`00c1ccdc`](#insn-00c1ccdc) → [`00c1cce4`](#insn-00c1cce4)
- ブロック [`00c1cce0`](#insn-00c1cce0) 範囲 `[['00c1cce0', '00c1cce3']]`
  - `FALL_THROUGH` [`00c1cce0`](#insn-00c1cce0) → [`00c1cce4`](#insn-00c1cce4)
- ブロック [`00c1cce4`](#insn-00c1cce4) 範囲 `[['00c1cce4', '00c1ccef']]`
  - `FALL_THROUGH` [`00c1ccec`](#insn-00c1ccec) → [`00c1ccf0`](#insn-00c1ccf0)
- ブロック [`00c1ccf0`](#insn-00c1ccf0) 範囲 `[['00c1ccf0', '00c1ccf3']]`
  - `FALL_THROUGH` [`00c1ccf0`](#insn-00c1ccf0) → [`00c1ccf4`](#insn-00c1ccf4)
- ブロック [`00c1ccf4`](#insn-00c1ccf4) 範囲 `[['00c1ccf4', '00c1ccf7']]`
  - `FALL_THROUGH` [`00c1ccf4`](#insn-00c1ccf4) → [`00c1ccf8`](#insn-00c1ccf8)
- ブロック [`00c1ccf8`](#insn-00c1ccf8) 範囲 `[['00c1ccf8', '00c1cd0f']]`
  - `FALL_THROUGH` [`00c1cd0c`](#insn-00c1cd0c) → [`00c1cd10`](#insn-00c1cd10)
- ブロック [`00c1cd10`](#insn-00c1cd10) 範囲 `[['00c1cd10', '00c1cd47']]`
  - `FALL_THROUGH` [`00c1cd44`](#insn-00c1cd44) → [`00c1cd48`](#insn-00c1cd48)
- ブロック [`00c1cd48`](#insn-00c1cd48) 範囲 `[['00c1cd48', '00c1cd53']]`
  - `CONDITIONAL_JUMP` [`00c1cd50`](#insn-00c1cd50) → [`00c1cd94`](#insn-00c1cd94)
  - `FALL_THROUGH` [`00c1cd50`](#insn-00c1cd50) → [`00c1cd54`](#insn-00c1cd54)
- ブロック [`00c1cd54`](#insn-00c1cd54) 範囲 `[['00c1cd54', '00c1cd57']]`
  - `FALL_THROUGH` [`00c1cd54`](#insn-00c1cd54) → [`00c1cd58`](#insn-00c1cd58)
- ブロック [`00c1cd58`](#insn-00c1cd58) 範囲 `[['00c1cd58', '00c1cd5b']]`
  - `FALL_THROUGH` [`00c1cd58`](#insn-00c1cd58) → [`00c1cd5c`](#insn-00c1cd5c)
- ブロック [`00c1cd5c`](#insn-00c1cd5c) 範囲 `[['00c1cd5c', '00c1cd63']]`
  - `FALL_THROUGH` [`00c1cd60`](#insn-00c1cd60) → [`00c1cd64`](#insn-00c1cd64)
- ブロック [`00c1cd64`](#insn-00c1cd64) 範囲 `[['00c1cd64', '00c1cd67']]`
  - `FALL_THROUGH` [`00c1cd64`](#insn-00c1cd64) → [`00c1cd68`](#insn-00c1cd68)
- ブロック [`00c1cd68`](#insn-00c1cd68) 範囲 `[['00c1cd68', '00c1cd6b']]`
  - `FALL_THROUGH` [`00c1cd68`](#insn-00c1cd68) → [`00c1cd6c`](#insn-00c1cd6c)
- ブロック [`00c1cd6c`](#insn-00c1cd6c) 範囲 `[['00c1cd6c', '00c1cd6f']]`
  - `FALL_THROUGH` [`00c1cd6c`](#insn-00c1cd6c) → [`00c1cd70`](#insn-00c1cd70)
- ブロック [`00c1cd70`](#insn-00c1cd70) 範囲 `[['00c1cd70', '00c1cd73']]`
  - `FALL_THROUGH` [`00c1cd70`](#insn-00c1cd70) → [`00c1cd74`](#insn-00c1cd74)
- ブロック [`00c1cd74`](#insn-00c1cd74) 範囲 `[['00c1cd74', '00c1cd77']]`
  - `FALL_THROUGH` [`00c1cd74`](#insn-00c1cd74) → [`00c1cd78`](#insn-00c1cd78)
- ブロック [`00c1cd78`](#insn-00c1cd78) 範囲 `[['00c1cd78', '00c1cd93']]`
  - `UNCONDITIONAL_JUMP` [`00c1cd90`](#insn-00c1cd90) → [`00c1cdc8`](#insn-00c1cdc8)
- ブロック [`00c1cd94`](#insn-00c1cd94) 範囲 `[['00c1cd94', '00c1cd97']]`
  - `FALL_THROUGH` [`00c1cd94`](#insn-00c1cd94) → [`00c1cd98`](#insn-00c1cd98)
- ブロック [`00c1cd98`](#insn-00c1cd98) 範囲 `[['00c1cd98', '00c1cd9b']]`
  - `FALL_THROUGH` [`00c1cd98`](#insn-00c1cd98) → [`00c1cd9c`](#insn-00c1cd9c)
- ブロック [`00c1cd9c`](#insn-00c1cd9c) 範囲 `[['00c1cd9c', '00c1cd9f']]`
  - `FALL_THROUGH` [`00c1cd9c`](#insn-00c1cd9c) → [`00c1cda0`](#insn-00c1cda0)
- ブロック [`00c1cda0`](#insn-00c1cda0) 範囲 `[['00c1cda0', '00c1cda3']]`
  - `FALL_THROUGH` [`00c1cda0`](#insn-00c1cda0) → [`00c1cda4`](#insn-00c1cda4)
- ブロック [`00c1cda4`](#insn-00c1cda4) 範囲 `[['00c1cda4', '00c1cda7']]`
  - `FALL_THROUGH` [`00c1cda4`](#insn-00c1cda4) → [`00c1cda8`](#insn-00c1cda8)
- ブロック [`00c1cda8`](#insn-00c1cda8) 範囲 `[['00c1cda8', '00c1cdb7']]`
  - `FALL_THROUGH` [`00c1cdb4`](#insn-00c1cdb4) → [`00c1cdb8`](#insn-00c1cdb8)
- ブロック [`00c1cdb8`](#insn-00c1cdb8) 範囲 `[['00c1cdb8', '00c1cdbb']]`
  - `FALL_THROUGH` [`00c1cdb8`](#insn-00c1cdb8) → [`00c1cdbc`](#insn-00c1cdbc)
- ブロック [`00c1cdbc`](#insn-00c1cdbc) 範囲 `[['00c1cdbc', '00c1cdbf']]`
  - `FALL_THROUGH` [`00c1cdbc`](#insn-00c1cdbc) → [`00c1cdc0`](#insn-00c1cdc0)
- ブロック [`00c1cdc0`](#insn-00c1cdc0) 範囲 `[['00c1cdc0', '00c1cdc3']]`
  - `FALL_THROUGH` [`00c1cdc0`](#insn-00c1cdc0) → [`00c1cdc4`](#insn-00c1cdc4)
- ブロック [`00c1cdc4`](#insn-00c1cdc4) 範囲 `[['00c1cdc4', '00c1cdc7']]`
  - `FALL_THROUGH` [`00c1cdc4`](#insn-00c1cdc4) → [`00c1cdc8`](#insn-00c1cdc8)
- ブロック [`00c1cdc8`](#insn-00c1cdc8) 範囲 `[['00c1cdc8', '00c1cdcb']]`
  - `FALL_THROUGH` [`00c1cdc8`](#insn-00c1cdc8) → [`00c1cdcc`](#insn-00c1cdcc)
- ブロック [`00c1cdcc`](#insn-00c1cdcc) 範囲 `[['00c1cdcc', '00c1cdd3']]`
  - `CONDITIONAL_JUMP` [`00c1cdd0`](#insn-00c1cdd0) → [`00c1cdec`](#insn-00c1cdec)
  - `FALL_THROUGH` [`00c1cdd0`](#insn-00c1cdd0) → [`00c1cdd4`](#insn-00c1cdd4)
- ブロック [`00c1cdd4`](#insn-00c1cdd4) 範囲 `[['00c1cdd4', '00c1cde7']]`
  - `CONDITIONAL_JUMP` [`00c1cde4`](#insn-00c1cde4) → [`00c1cdf4`](#insn-00c1cdf4)
  - `FALL_THROUGH` [`00c1cde4`](#insn-00c1cde4) → [`00c1cde8`](#insn-00c1cde8)
- ブロック [`00c1cde8`](#insn-00c1cde8) 範囲 `[['00c1cde8', '00c1cdeb']]`
  - `FALL_THROUGH` [`00c1cde8`](#insn-00c1cde8) → [`00c1cdec`](#insn-00c1cdec)
- ブロック [`00c1cdec`](#insn-00c1cdec) 範囲 `[['00c1cdec', '00c1cdf3']]`
  - `FALL_THROUGH` [`00c1cdf0`](#insn-00c1cdf0) → [`00c1cdf4`](#insn-00c1cdf4)
- ブロック [`00c1cdf4`](#insn-00c1cdf4) 範囲 `[['00c1cdf4', '00c1ce3f']]`
  - `FALL_THROUGH` [`00c1ce3c`](#insn-00c1ce3c) → [`00c1ce40`](#insn-00c1ce40)
- ブロック [`00c1ce40`](#insn-00c1ce40) 範囲 `[['00c1ce40', '00c1ce43']]`
  - `FALL_THROUGH` [`00c1ce40`](#insn-00c1ce40) → [`00c1ce44`](#insn-00c1ce44)
- ブロック [`00c1ce44`](#insn-00c1ce44) 範囲 `[['00c1ce44', '00c1ce47']]`
  - `FALL_THROUGH` [`00c1ce44`](#insn-00c1ce44) → [`00c1ce48`](#insn-00c1ce48)
- ブロック [`00c1ce48`](#insn-00c1ce48) 範囲 `[['00c1ce48', '00c1ce4b']]`
  - `FALL_THROUGH` [`00c1ce48`](#insn-00c1ce48) → [`00c1ce4c`](#insn-00c1ce4c)
- ブロック [`00c1ce4c`](#insn-00c1ce4c) 範囲 `[['00c1ce4c', '00c1ce4f']]`
  - `FALL_THROUGH` [`00c1ce4c`](#insn-00c1ce4c) → [`00c1ce50`](#insn-00c1ce50)
- ブロック [`00c1ce50`](#insn-00c1ce50) 範囲 `[['00c1ce50', '00c1ce53']]`
  - `FALL_THROUGH` [`00c1ce50`](#insn-00c1ce50) → [`00c1ce54`](#insn-00c1ce54)
- ブロック [`00c1ce54`](#insn-00c1ce54) 範囲 `[['00c1ce54', '00c1ce57']]`
  - `FALL_THROUGH` [`00c1ce54`](#insn-00c1ce54) → [`00c1ce58`](#insn-00c1ce58)
- ブロック [`00c1ce58`](#insn-00c1ce58) 範囲 `[['00c1ce58', '00c1ce5b']]`
  - `FALL_THROUGH` [`00c1ce58`](#insn-00c1ce58) → [`00c1ce5c`](#insn-00c1ce5c)
- ブロック [`00c1ce5c`](#insn-00c1ce5c) 範囲 `[['00c1ce5c', '00c1ce5f']]`
  - `FALL_THROUGH` [`00c1ce5c`](#insn-00c1ce5c) → [`00c1ce60`](#insn-00c1ce60)
- ブロック [`00c1ce60`](#insn-00c1ce60) 範囲 `[['00c1ce60', '00c1ce63']]`
  - `FALL_THROUGH` [`00c1ce60`](#insn-00c1ce60) → [`00c1ce64`](#insn-00c1ce64)
- ブロック [`00c1ce64`](#insn-00c1ce64) 範囲 `[['00c1ce64', '00c1ce67']]`
  - `FALL_THROUGH` [`00c1ce64`](#insn-00c1ce64) → [`00c1ce68`](#insn-00c1ce68)
- ブロック [`00c1ce68`](#insn-00c1ce68) 範囲 `[['00c1ce68', '00c1ce6b']]`
  - `FALL_THROUGH` [`00c1ce68`](#insn-00c1ce68) → [`00c1ce6c`](#insn-00c1ce6c)
- ブロック [`00c1ce6c`](#insn-00c1ce6c) 範囲 `[['00c1ce6c', '00c1ce6f']]`
  - `FALL_THROUGH` [`00c1ce6c`](#insn-00c1ce6c) → [`00c1ce70`](#insn-00c1ce70)
- ブロック [`00c1ce70`](#insn-00c1ce70) 範囲 `[['00c1ce70', '00c1ce73']]`
  - `CONDITIONAL_JUMP` [`00c1ce70`](#insn-00c1ce70) → [`00c1ce7c`](#insn-00c1ce7c)
  - `FALL_THROUGH` [`00c1ce70`](#insn-00c1ce70) → [`00c1ce74`](#insn-00c1ce74)
- ブロック [`00c1ce74`](#insn-00c1ce74) 範囲 `[['00c1ce74', '00c1ce77']]`
  - `FALL_THROUGH` [`00c1ce74`](#insn-00c1ce74) → [`00c1ce78`](#insn-00c1ce78)
- ブロック [`00c1ce78`](#insn-00c1ce78) 範囲 `[['00c1ce78', '00c1ce7b']]`
  - `FALL_THROUGH` [`00c1ce78`](#insn-00c1ce78) → [`00c1ce7c`](#insn-00c1ce7c)
- ブロック [`00c1ce7c`](#insn-00c1ce7c) 範囲 `[['00c1ce7c', '00c1ce7f']]`
  - `FALL_THROUGH` [`00c1ce7c`](#insn-00c1ce7c) → [`00c1ce80`](#insn-00c1ce80)
- ブロック [`00c1ce80`](#insn-00c1ce80) 範囲 `[['00c1ce80', '00c1ce83']]`
  - `CONDITIONAL_JUMP` [`00c1ce80`](#insn-00c1ce80) → [`00c1cecc`](#insn-00c1cecc)
  - `FALL_THROUGH` [`00c1ce80`](#insn-00c1ce80) → [`00c1ce84`](#insn-00c1ce84)
- ブロック [`00c1ce84`](#insn-00c1ce84) 範囲 `[['00c1ce84', '00c1ce8b']]`
  - `CONDITIONAL_JUMP` [`00c1ce88`](#insn-00c1ce88) → [`00c1cedc`](#insn-00c1cedc)
  - `FALL_THROUGH` [`00c1ce88`](#insn-00c1ce88) → [`00c1ce8c`](#insn-00c1ce8c)
- ブロック [`00c1ce8c`](#insn-00c1ce8c) 範囲 `[['00c1ce8c', '00c1ce93']]`
  - `CONDITIONAL_JUMP` [`00c1ce90`](#insn-00c1ce90) → [`00c1ce9c`](#insn-00c1ce9c)
  - `FALL_THROUGH` [`00c1ce90`](#insn-00c1ce90) → [`00c1ce94`](#insn-00c1ce94)
- ブロック [`00c1ce94`](#insn-00c1ce94) 範囲 `[['00c1ce94', '00c1ce9b']]`
  - `FALL_THROUGH` [`00c1ce98`](#insn-00c1ce98) → [`00c1ce9c`](#insn-00c1ce9c)
- ブロック [`00c1ce9c`](#insn-00c1ce9c) 範囲 `[['00c1ce9c', '00c1ceaf']]`
  - `FALL_THROUGH` [`00c1ceac`](#insn-00c1ceac) → [`00c1ceb0`](#insn-00c1ceb0)
- ブロック [`00c1ceb0`](#insn-00c1ceb0) 範囲 `[['00c1ceb0', '00c1ceb3']]`
  - `FALL_THROUGH` [`00c1ceb0`](#insn-00c1ceb0) → [`00c1ceb4`](#insn-00c1ceb4)
- ブロック [`00c1ceb4`](#insn-00c1ceb4) 範囲 `[['00c1ceb4', '00c1ceb7']]`
  - `FALL_THROUGH` [`00c1ceb4`](#insn-00c1ceb4) → [`00c1ceb8`](#insn-00c1ceb8)
- ブロック [`00c1ceb8`](#insn-00c1ceb8) 範囲 `[['00c1ceb8', '00c1cebb']]`
  - `FALL_THROUGH` [`00c1ceb8`](#insn-00c1ceb8) → [`00c1cebc`](#insn-00c1cebc)
- ブロック [`00c1cebc`](#insn-00c1cebc) 範囲 `[['00c1cebc', '00c1cebf']]`
  - `FALL_THROUGH` [`00c1cebc`](#insn-00c1cebc) → [`00c1cec0`](#insn-00c1cec0)
- ブロック [`00c1cec0`](#insn-00c1cec0) 範囲 `[['00c1cec0', '00c1cecb']]`
- ブロック [`00c1cecc`](#insn-00c1cecc) 範囲 `[['00c1cecc', '00c1cedb']]`
  - `CONDITIONAL_JUMP` [`00c1ced8`](#insn-00c1ced8) → [`00c1ce8c`](#insn-00c1ce8c)
  - `FALL_THROUGH` [`00c1ced8`](#insn-00c1ced8) → [`00c1cedc`](#insn-00c1cedc)
- ブロック [`00c1cedc`](#insn-00c1cedc) 範囲 `[['00c1cedc', '00c1ceeb']]`
  - `CONDITIONAL_JUMP` [`00c1cee8`](#insn-00c1cee8) → [`00c1ce94`](#insn-00c1ce94)
  - `FALL_THROUGH` [`00c1cee8`](#insn-00c1cee8) → [`00c1ceec`](#insn-00c1ceec)
- ブロック [`00c1ceec`](#insn-00c1ceec) 範囲 `[['00c1ceec', '00c1ceef']]`
  - `UNCONDITIONAL_JUMP` [`00c1ceec`](#insn-00c1ceec) → [`00c1ce9c`](#insn-00c1ce9c)
- ブロック [`00c1cef0`](#insn-00c1cef0) 範囲 `[['00c1cef0', '00c1cef3']]`

## 命令位置別の参照

- [`00c1cbf0`](#insn-00c1cbf0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cbf4`](#insn-00c1cbf4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cbf8`](#insn-00c1cbf8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cbfc`](#insn-00c1cbfc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cc00`](#insn-00c1cc00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cc04`](#insn-00c1cc04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cc2c`](#insn-00c1cc2c) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00c1cc34`](#insn-00c1cc34) → `00c9b740`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00c1cc38`](#insn-00c1cc38) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cc3c`](#insn-00c1cc3c) → `01127a08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIwE2idE` · 推定型 `undefined8`
- [`00c1cc3c`](#insn-00c1cc3c) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cc40`](#insn-00c1cc40) → `01127a08`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIwE2idE` · 推定型 `undefined8`
- [`00c1cc48`](#insn-00c1cc48) → [`00c1cc74`](#insn-00c1cc74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cc54`](#insn-00c1cc54) → `Stack[-0x260]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cc58`](#insn-00c1cc58) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cc64`](#insn-00c1cc64) → [`00c35b90`](../00c35/00c35b90.md) · `PARAM` · `ANALYSIS` · 関数 `00c35b90` · 推定シンボル `None` · 推定型 `None`
- [`00c1cc68`](#insn-00c1cc68) → `00c9b740`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00c1cc68`](#insn-00c1cc68) → `01127a08`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIwE2idE` · 推定型 `undefined8`
- [`00c1cc70`](#insn-00c1cc70) → [`00c5dae0`](../00c5d/00c5dae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dae0` · 推定シンボル `None` · 推定型 `None`
- [`00c1cc78`](#insn-00c1cc78) → `01127a10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00c1cc88`](#insn-00c1cc88) → [`00c1cef0`](#insn-00c1cef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cc90`](#insn-00c1cc90) → [`00c1cef0`](#insn-00c1cef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cca8`](#insn-00c1cca8) → [`00c1cce0`](#insn-00c1cce0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ccdc`](#insn-00c1ccdc) → [`00c1cce4`](#insn-00c1cce4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cce4`](#insn-00c1cce4) → `Stack[-0x278]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cce8`](#insn-00c1cce8) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ccec`](#insn-00c1ccec) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ccf0`](#insn-00c1ccf0) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ccf4`](#insn-00c1ccf4) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ccf8`](#insn-00c1ccf8) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ccfc`](#insn-00c1ccfc) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cd28`](#insn-00c1cd28) → `Stack[-0x2b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cd2c`](#insn-00c1cd2c) → [`00c5e310`](../00c5e/00c5e310.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e310` · 推定シンボル `None` · 推定型 `None`
- [`00c1cd3c`](#insn-00c1cd3c) → `Stack[-0xcc]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cd50`](#insn-00c1cd50) → [`00c1cd94`](#insn-00c1cd94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cd54`](#insn-00c1cd54) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cd58`](#insn-00c1cd58) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cd5c`](#insn-00c1cd5c) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cd68`](#insn-00c1cd68) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cd90`](#insn-00c1cd90) → [`00c1cdc8`](#insn-00c1cdc8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cd94`](#insn-00c1cd94) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cd98`](#insn-00c1cd98) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cd9c`](#insn-00c1cd9c) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cda8`](#insn-00c1cda8) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cdd0`](#insn-00c1cdd0) → [`00c1cdec`](#insn-00c1cdec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cdd8`](#insn-00c1cdd8) → [`00c59c20`](../00c59/00c59c20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59c20` · 推定シンボル `None` · 推定型 `None`
- [`00c1cde4`](#insn-00c1cde4) → [`00c1cdf4`](#insn-00c1cdf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cde8`](#insn-00c1cde8) → [`00c5db80`](../00c5d/00c5db80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5db80` · 推定シンボル `None` · 推定型 `None`
- [`00c1ce00`](#insn-00c1ce00) → `Stack[-0x278]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ce08`](#insn-00c1ce08) → `Stack[-0x7c]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ce20`](#insn-00c1ce20) → `Stack[-0x290]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ce2c`](#insn-00c1ce2c) → `Stack[-0x298]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ce40`](#insn-00c1ce40) → `Stack[-0x280]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ce44`](#insn-00c1ce44) → `Stack[-0x2a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ce48`](#insn-00c1ce48) → `Stack[-0x2a8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ce4c`](#insn-00c1ce4c) → `Stack[-0x2b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ce50`](#insn-00c1ce50) → [`00c5e320`](../00c5e/00c5e320.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e320` · 推定シンボル `None` · 推定型 `None`
- [`00c1ce54`](#insn-00c1ce54) → `Stack[-0x270]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ce68`](#insn-00c1ce68) → [`00c114bc`](../00c11/00c114bc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c114bc` · 推定シンボル `None` · 推定型 `None`
- [`00c1ce70`](#insn-00c1ce70) → [`00c1ce7c`](#insn-00c1ce7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ce78`](#insn-00c1ce78) → [`00c58260`](../00c58/00c58260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58260` · 推定シンボル `None` · 推定型 `None`
- [`00c1ce7c`](#insn-00c1ce7c) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ce80`](#insn-00c1ce80) → [`00c1cecc`](#insn-00c1cecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ce84`](#insn-00c1ce84) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ce88`](#insn-00c1ce88) → [`00c1cedc`](#insn-00c1cedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ce8c`](#insn-00c1ce8c) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ce90`](#insn-00c1ce90) → [`00c1ce9c`](#insn-00c1ce9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ce94`](#insn-00c1ce94) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ce98`](#insn-00c1ce98) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00c1cea0`](#insn-00c1cea0) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00c1ceac`](#insn-00c1ceac) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ceb0`](#insn-00c1ceb0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ceb4`](#insn-00c1ceb4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ceb8`](#insn-00c1ceb8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cebc`](#insn-00c1cebc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cec0`](#insn-00c1cec0) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cecc`](#insn-00c1cecc) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ced0`](#insn-00c1ced0) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00c1ced4`](#insn-00c1ced4) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ced8`](#insn-00c1ced8) → [`00c1ce8c`](#insn-00c1ce8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cedc`](#insn-00c1cedc) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cee0`](#insn-00c1cee0) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00c1cee4`](#insn-00c1cee4) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cee8`](#insn-00c1cee8) → [`00c1ce94`](#insn-00c1ce94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1ceec`](#insn-00c1ceec) → [`00c1ce9c`](#insn-00c1ce9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1cef0`](#insn-00c1cef0) → [`00c05b30`](../00c05/00c05b30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c05b30` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c1cbf0`](#insn-00c1cbf0)

~~~json
{
  "source": "00c1cbf0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cbf4`](#insn-00c1cbf4)

~~~json
{
  "source": "00c1cbf4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cbf8`](#insn-00c1cbf8)

~~~json
{
  "source": "00c1cbf8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cbfc`](#insn-00c1cbfc)

~~~json
{
  "source": "00c1cbfc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cc00`](#insn-00c1cc00)

~~~json
{
  "source": "00c1cc00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cc04`](#insn-00c1cc04)

~~~json
{
  "source": "00c1cc04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cc2c`](#insn-00c1cc2c)

~~~json
{
  "source": "00c1cc2c",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1cc34`](#insn-00c1cc34)

~~~json
{
  "source": "00c1cc34",
  "target": "00c9b740",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b740",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c1cc38`](#insn-00c1cc38)

~~~json
{
  "source": "00c1cc38",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cc3c`](#insn-00c1cc3c)

~~~json
{
  "source": "00c1cc3c",
  "target": "01127a08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127a08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c1cc3c`](#insn-00c1cc3c)

~~~json
{
  "source": "00c1cc3c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cc40`](#insn-00c1cc40)

~~~json
{
  "source": "00c1cc40",
  "target": "01127a08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127a08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c1cc48`](#insn-00c1cc48)

~~~json
{
  "source": "00c1cc48",
  "target": "00c1cc74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cc54`](#insn-00c1cc54)

~~~json
{
  "source": "00c1cc54",
  "target": "Stack[-0x260]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cc58`](#insn-00c1cc58)

~~~json
{
  "source": "00c1cc58",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cc64`](#insn-00c1cc64)

~~~json
{
  "source": "00c1cc64",
  "target": "00c35b90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1cc68`](#insn-00c1cc68)

~~~json
{
  "source": "00c1cc68",
  "target": "00c9b740",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b740",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c1cc68`](#insn-00c1cc68)

~~~json
{
  "source": "00c1cc68",
  "target": "01127a08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127a08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c1cc70`](#insn-00c1cc70)

~~~json
{
  "source": "00c1cc70",
  "target": "00c5dae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1cc78`](#insn-00c1cc78)

~~~json
{
  "source": "00c1cc78",
  "target": "01127a10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127a10",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c1cc88`](#insn-00c1cc88)

~~~json
{
  "source": "00c1cc88",
  "target": "00c1cef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cc90`](#insn-00c1cc90)

~~~json
{
  "source": "00c1cc90",
  "target": "00c1cef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cca8`](#insn-00c1cca8)

~~~json
{
  "source": "00c1cca8",
  "target": "00c1cce0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ccdc`](#insn-00c1ccdc)

~~~json
{
  "source": "00c1ccdc",
  "target": "00c1cce4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cce4`](#insn-00c1cce4)

~~~json
{
  "source": "00c1cce4",
  "target": "Stack[-0x278]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cce8`](#insn-00c1cce8)

~~~json
{
  "source": "00c1cce8",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ccec`](#insn-00c1ccec)

~~~json
{
  "source": "00c1ccec",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ccf0`](#insn-00c1ccf0)

~~~json
{
  "source": "00c1ccf0",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ccf4`](#insn-00c1ccf4)

~~~json
{
  "source": "00c1ccf4",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ccf8`](#insn-00c1ccf8)

~~~json
{
  "source": "00c1ccf8",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ccfc`](#insn-00c1ccfc)

~~~json
{
  "source": "00c1ccfc",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cd28`](#insn-00c1cd28)

~~~json
{
  "source": "00c1cd28",
  "target": "Stack[-0x2b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cd2c`](#insn-00c1cd2c)

~~~json
{
  "source": "00c1cd2c",
  "target": "00c5e310",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1cd3c`](#insn-00c1cd3c)

~~~json
{
  "source": "00c1cd3c",
  "target": "Stack[-0xcc]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cd50`](#insn-00c1cd50)

~~~json
{
  "source": "00c1cd50",
  "target": "00c1cd94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cd54`](#insn-00c1cd54)

~~~json
{
  "source": "00c1cd54",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cd58`](#insn-00c1cd58)

~~~json
{
  "source": "00c1cd58",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cd5c`](#insn-00c1cd5c)

~~~json
{
  "source": "00c1cd5c",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cd68`](#insn-00c1cd68)

~~~json
{
  "source": "00c1cd68",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cd90`](#insn-00c1cd90)

~~~json
{
  "source": "00c1cd90",
  "target": "00c1cdc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cd94`](#insn-00c1cd94)

~~~json
{
  "source": "00c1cd94",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cd98`](#insn-00c1cd98)

~~~json
{
  "source": "00c1cd98",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cd9c`](#insn-00c1cd9c)

~~~json
{
  "source": "00c1cd9c",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cda8`](#insn-00c1cda8)

~~~json
{
  "source": "00c1cda8",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cdd0`](#insn-00c1cdd0)

~~~json
{
  "source": "00c1cdd0",
  "target": "00c1cdec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cdd8`](#insn-00c1cdd8)

~~~json
{
  "source": "00c1cdd8",
  "target": "00c59c20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1cde4`](#insn-00c1cde4)

~~~json
{
  "source": "00c1cde4",
  "target": "00c1cdf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cde8`](#insn-00c1cde8)

~~~json
{
  "source": "00c1cde8",
  "target": "00c5db80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1ce00`](#insn-00c1ce00)

~~~json
{
  "source": "00c1ce00",
  "target": "Stack[-0x278]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ce08`](#insn-00c1ce08)

~~~json
{
  "source": "00c1ce08",
  "target": "Stack[-0x7c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ce20`](#insn-00c1ce20)

~~~json
{
  "source": "00c1ce20",
  "target": "Stack[-0x290]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ce2c`](#insn-00c1ce2c)

~~~json
{
  "source": "00c1ce2c",
  "target": "Stack[-0x298]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ce40`](#insn-00c1ce40)

~~~json
{
  "source": "00c1ce40",
  "target": "Stack[-0x280]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ce44`](#insn-00c1ce44)

~~~json
{
  "source": "00c1ce44",
  "target": "Stack[-0x2a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ce48`](#insn-00c1ce48)

~~~json
{
  "source": "00c1ce48",
  "target": "Stack[-0x2a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ce4c`](#insn-00c1ce4c)

~~~json
{
  "source": "00c1ce4c",
  "target": "Stack[-0x2b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ce50`](#insn-00c1ce50)

~~~json
{
  "source": "00c1ce50",
  "target": "00c5e320",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1ce54`](#insn-00c1ce54)

~~~json
{
  "source": "00c1ce54",
  "target": "Stack[-0x270]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ce68`](#insn-00c1ce68)

~~~json
{
  "source": "00c1ce68",
  "target": "00c114bc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1ce70`](#insn-00c1ce70)

~~~json
{
  "source": "00c1ce70",
  "target": "00c1ce7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ce78`](#insn-00c1ce78)

~~~json
{
  "source": "00c1ce78",
  "target": "00c58260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1ce7c`](#insn-00c1ce7c)

~~~json
{
  "source": "00c1ce7c",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ce80`](#insn-00c1ce80)

~~~json
{
  "source": "00c1ce80",
  "target": "00c1cecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ce84`](#insn-00c1ce84)

~~~json
{
  "source": "00c1ce84",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ce88`](#insn-00c1ce88)

~~~json
{
  "source": "00c1ce88",
  "target": "00c1cedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ce8c`](#insn-00c1ce8c)

~~~json
{
  "source": "00c1ce8c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ce90`](#insn-00c1ce90)

~~~json
{
  "source": "00c1ce90",
  "target": "00c1ce9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ce94`](#insn-00c1ce94)

~~~json
{
  "source": "00c1ce94",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ce98`](#insn-00c1ce98)

~~~json
{
  "source": "00c1ce98",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1cea0`](#insn-00c1cea0)

~~~json
{
  "source": "00c1cea0",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1ceac`](#insn-00c1ceac)

~~~json
{
  "source": "00c1ceac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ceb0`](#insn-00c1ceb0)

~~~json
{
  "source": "00c1ceb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ceb4`](#insn-00c1ceb4)

~~~json
{
  "source": "00c1ceb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ceb8`](#insn-00c1ceb8)

~~~json
{
  "source": "00c1ceb8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cebc`](#insn-00c1cebc)

~~~json
{
  "source": "00c1cebc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cec0`](#insn-00c1cec0)

~~~json
{
  "source": "00c1cec0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cecc`](#insn-00c1cecc)

~~~json
{
  "source": "00c1cecc",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ced0`](#insn-00c1ced0)

~~~json
{
  "source": "00c1ced0",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1ced4`](#insn-00c1ced4)

~~~json
{
  "source": "00c1ced4",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ced8`](#insn-00c1ced8)

~~~json
{
  "source": "00c1ced8",
  "target": "00c1ce8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cedc`](#insn-00c1cedc)

~~~json
{
  "source": "00c1cedc",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cee0`](#insn-00c1cee0)

~~~json
{
  "source": "00c1cee0",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1cee4`](#insn-00c1cee4)

~~~json
{
  "source": "00c1cee4",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cee8`](#insn-00c1cee8)

~~~json
{
  "source": "00c1cee8",
  "target": "00c1ce94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1ceec`](#insn-00c1ceec)

~~~json
{
  "source": "00c1ceec",
  "target": "00c1ce9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1cef0`](#insn-00c1cef0)

~~~json
{
  "source": "00c1cef0",
  "target": "00c05b30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
