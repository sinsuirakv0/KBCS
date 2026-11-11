# 00babcc8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00babcc8",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEt",
  "size": 436,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e1e7d791faaa9151d6b36ad9a68f5a528b109f34c903cd5d1db52f34531ae5a6",
  "source_text_sha256": "e1e7d791faaa9151d6b36ad9a68f5a528b109f34c903cd5d1db52f34531ae5a6"
}
~~~

## 呼び出し元

- [00c5cb60](../00c5c/00c5cb60.md)

## 呼び出し先

- [00c57ee0](../00c57/00c57ee0.md)
- [00c58270](../00c58/00c58270.md)
- [00c58280](../00c58/00c58280.md)
- [00c58290](../00c58/00c58290.md)
- [00c582a0](../00c58/00c582a0.md)
- [00c58ef0](../00c58/00c58ef0.md)
- [00c5d0f0](../00c5d/00c5d0f0.md)

## 疑似コード / UTF-8 5172 bytes

~~~c

long * _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEt(long *param_1,undefined2 param_2)

{
  long lVar1;
  uint uVar2;
  int iVar3;
  long *plVar4;
  long *plVar5;
  ulong uVar6;
  long lVar7;
  undefined8 uVar8;
  undefined1 auStack_60 [8];
  long local_58;
  
                    /* catch() { ... } // from try @ 00ba9f9c with catch @ 00babccc */
                    /* catch() { ... } // from try @ 00baaf6c with catch @ 00babcdc */
                    /* catch() { ... } // from try @ 00baaf4c with catch @ 00babce0 */
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
                    /* catch() { ... } // from try @ 00baac64 with catch @ 00babcf0 */
                    /* catch() { ... } // from try @ 00baac44 with catch @ 00babcf4 */
  lVar7 = *(long *)(*param_1 + -0x18);
                    /* catch() { ... } // from try @ 00baa288 with catch @ 00babd04 */
  if (*(int *)((long)param_1 + lVar7 + 0x20) == 0) {
                    /* catch() { ... } // from try @ 00baa268 with catch @ 00babd08 */
    if (*(long *)((long)param_1 + lVar7 + 0x88) != 0) {
      _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5flushEv();
                    /* catch() { ... } // from try @ 00ba9f70 with catch @ 00babd18 */
                    /* catch() { ... } // from try @ 00ba9f50 with catch @ 00babd1c */
      lVar7 = *(long *)(*param_1 + -0x18);
    }
    _ZNKSt6__ndk18ios_base6getlocEv(auStack_60,(long)param_1 + lVar7);
                    /* catch() { ... } // from try @ 00baaf2c with catch @ 00babd2c */
    plVar4 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                               (auStack_60,
                                PTR__ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9b838
                               );
    _ZNSt6__ndk16localeD1Ev(auStack_60);
                    /* catch() { ... } // from try @ 00baaf18 with catch @ 00babd4c */
                    /* catch() { ... } // from try @ 00baac24 with catch @ 00babd50 */
    lVar7 = (long)param_1 + *(long *)(*param_1 + -0x18);
    uVar2 = *(uint *)(lVar7 + 0x90);
    uVar8 = *(undefined8 *)(lVar7 + 0x28);
    if (uVar2 == 0xffffffff) {
      _ZNKSt6__ndk18ios_base6getlocEv(auStack_60,lVar7);
                    /* catch() { ... } // from try @ 00baac10 with catch @ 00babd70 */
                    /* catch() { ... } // from try @ 00baa248 with catch @ 00babd74 */
      plVar5 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                                 (auStack_60,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9ac30);
      uVar2 = (**(code **)(*plVar5 + 0x38))(plVar5,0x20);
                    /* catch() { ... } // from try @ 00baa234 with catch @ 00babd94 */
                    /* catch() { ... } // from try @ 00ba9f30 with catch @ 00babd98 */
      _ZNSt6__ndk16localeD1Ev(auStack_60);
      uVar2 = uVar2 & 0xff;
      *(uint *)(lVar7 + 0x90) = uVar2;
    }
                    /* catch() { ... } // from try @ 00ba9f1c with catch @ 00babdb8 */
                    /* catch() { ... } // from try @ 00baaef4 with catch @ 00babdbc */
    lVar7 = (**(code **)(*plVar4 + 0x30))(plVar4,uVar8,lVar7,uVar2,param_2);
                    /* catch() { ... } // from try @ 00baabec with catch @ 00babdc0 */
    if (lVar7 == 0) {
                    /* catch() { ... } // from try @ 00baab4c with catch @ 00babdc4 */
                    /* catch() { ... } // from try @ 00baaac4 with catch @ 00babdc8 */
                    /* catch() { ... } // from try @ 00baa210 with catch @ 00babdd0 */
      lVar7 = (long)param_1 + *(long *)(*param_1 + -0x18);
                    /* catch() { ... } // from try @ 00ba9ef8 with catch @ 00babdd4 */
                    /* catch() { ... } // from try @ 00bab88c with catch @ 00babdd8 */
                    /* catch() { ... } // from try @ 00bab4e8 with catch @ 00babddc */
      _ZNSt6__ndk18ios_base5clearEj(lVar7,*(uint *)(lVar7 + 0x20) | 5);
    }
  }
  lVar7 = *(long *)(*param_1 + -0x18);
  if ((((*(long *)((long)param_1 + lVar7 + 0x28) != 0) &&
       (*(int *)((long)param_1 + lVar7 + 0x20) == 0)) &&
      ((*(byte *)((long)param_1 + lVar7 + 9) >> 5 & 1) != 0)) &&
     ((uVar6 = _ZSt18uncaught_exceptionv(), (uVar6 & 1) == 0 &&
      (iVar3 = (**(code **)(**(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28) + 0x30))
                         (), iVar3 == -1)))) {
    lVar7 = (long)param_1 + *(long *)(*param_1 + -0x18);
                    /* catch() { ... } // from try @ 00bab5e0 with catch @ 00babe44 */
    _ZNSt6__ndk18ios_base5clearEj(lVar7,*(uint *)(lVar7 + 0x20) | 1);
  }
                    /* catch() { ... } // from try @ 00bab248 with catch @ 00babe48 */
  if (*(long *)(lVar1 + 0x28) == local_58) {
                    /* catch() { ... } // from try @ 00bab150 with catch @ 00babe5c */
                    /* catch() { ... } // from try @ 00baae44 with catch @ 00babe60 */
                    /* catch() { ... } // from try @ 00baa464 with catch @ 00babe64 */
                    /* catch() { ... } // from try @ 00baa14c with catch @ 00babe68 */
    return param_1;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
