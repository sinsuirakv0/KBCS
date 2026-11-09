# 00c1cbec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

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
  "source_text_sha256": "1a7c8d53f00c32b48a3247afd1ac212f1fbeabbf7a9deb52e5e39c8c8c1bcd34"
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
