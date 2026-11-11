# 00babaf4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00babaf4",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEs",
  "size": 468,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b05840f61492bac19e648aede583f55db4b354bb06cd82bf8de47846ed193008",
  "source_text_sha256": "b05840f61492bac19e648aede583f55db4b354bb06cd82bf8de47846ed193008"
}
~~~

## 呼び出し元

- [00c5cb50](../00c5c/00c5cb50.md)

## 呼び出し先

- [00c57ee0](../00c57/00c57ee0.md)
- [00c58270](../00c58/00c58270.md)
- [00c58280](../00c58/00c58280.md)
- [00c58290](../00c58/00c58290.md)
- [00c582a0](../00c58/00c582a0.md)
- [00c58ef0](../00c58/00c58ef0.md)
- [00c5d0f0](../00c5d/00c5d0f0.md)

## 疑似コード / UTF-8 6716 bytes

~~~c

long * _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEs(long *param_1,ushort param_2)

{
  uint uVar1;
  long lVar2;
  uint uVar3;
  int iVar4;
  long *plVar5;
  long *plVar6;
  ulong uVar7;
  long lVar8;
  undefined8 uVar9;
  undefined1 auStack_60 [8];
  long local_58;
  
                    /* catch() { ... } // from try @ 00bab144 with catch @ 00babafc */
                    /* catch() { ... } // from try @ 00bab124 with catch @ 00babb00 */
                    /* catch() { ... } // from try @ 00baae38 with catch @ 00babb10 */
  lVar2 = tpidr_el0;
                    /* catch() { ... } // from try @ 00baae1c with catch @ 00babb14 */
  local_58 = *(long *)(lVar2 + 0x28);
                    /* catch() { ... } // from try @ 00baa458 with catch @ 00babb24 */
  lVar8 = *(long *)(*param_1 + -0x18);
                    /* catch() { ... } // from try @ 00baa438 with catch @ 00babb28 */
  if (*(int *)((long)param_1 + lVar8 + 0x20) == 0) {
                    /* catch() { ... } // from try @ 00baa140 with catch @ 00babb38 */
                    /* catch() { ... } // from try @ 00baa120 with catch @ 00babb3c */
    if (*(long *)((long)param_1 + lVar8 + 0x88) != 0) {
      _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5flushEv();
      lVar8 = *(long *)(*param_1 + -0x18);
    }
                    /* catch() { ... } // from try @ 00bab0f8 with catch @ 00babb4c */
                    /* catch() { ... } // from try @ 00bab0d4 with catch @ 00babb50 */
    uVar1 = *(uint *)((long)param_1 + lVar8 + 8) & 0x4a;
                    /* catch() { ... } // from try @ 00baadf0 with catch @ 00babb60 */
    _ZNKSt6__ndk18ios_base6getlocEv(auStack_60);
                    /* catch() { ... } // from try @ 00baadcc with catch @ 00babb64 */
    plVar5 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                               (auStack_60,
                                PTR__ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9b838
                               );
                    /* catch() { ... } // from try @ 00baa40c with catch @ 00babb74 */
                    /* catch() { ... } // from try @ 00baa3e8 with catch @ 00babb78 */
    _ZNSt6__ndk16localeD1Ev(auStack_60);
                    /* catch() { ... } // from try @ 00baa0f4 with catch @ 00babb88 */
    lVar8 = (long)param_1 + *(long *)(*param_1 + -0x18);
                    /* catch() { ... } // from try @ 00baa0d0 with catch @ 00babb8c */
    uVar3 = *(uint *)(lVar8 + 0x90);
    uVar9 = *(undefined8 *)(lVar8 + 0x28);
    if (uVar3 == 0xffffffff) {
                    /* catch() { ... } // from try @ 00bab0a8 with catch @ 00babb9c */
                    /* catch() { ... } // from try @ 00bab084 with catch @ 00babba0 */
      _ZNKSt6__ndk18ios_base6getlocEv(auStack_60,lVar8);
                    /* catch() { ... } // from try @ 00baada0 with catch @ 00babbb0 */
                    /* catch() { ... } // from try @ 00baad7c with catch @ 00babbb4 */
      plVar6 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                                 (auStack_60,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9ac30);
                    /* catch() { ... } // from try @ 00baa3bc with catch @ 00babbc4 */
      uVar3 = (**(code **)(*plVar6 + 0x38))(plVar6,0x20);
                    /* catch() { ... } // from try @ 00baa3a0 with catch @ 00babbc8 */
      _ZNSt6__ndk16localeD1Ev(auStack_60);
      uVar3 = uVar3 & 0xff;
                    /* catch() { ... } // from try @ 00baa0a4 with catch @ 00babbd8 */
      *(uint *)(lVar8 + 0x90) = uVar3;
    }
                    /* catch() { ... } // from try @ 00baa088 with catch @ 00babbdc */
                    /* catch() { ... } // from try @ 00bab058 with catch @ 00babbec */
                    /* catch() { ... } // from try @ 00baad50 with catch @ 00babbf0 */
                    /* catch() { ... } // from try @ 00baa374 with catch @ 00babbf4 */
    uVar7 = (ulong)param_2;
                    /* catch() { ... } // from try @ 00baa05c with catch @ 00babbf8 */
    if (uVar1 != 8 && uVar1 != 0x40) {
      uVar7 = (long)(short)param_2;
    }
                    /* catch() { ... } // from try @ 00bab034 with catch @ 00babbfc */
    lVar8 = (**(code **)(*plVar5 + 0x20))(plVar5,uVar9,lVar8,uVar3,uVar7);
                    /* catch() { ... } // from try @ 00bab008 with catch @ 00babc0c */
    if (lVar8 == 0) {
                    /* catch() { ... } // from try @ 00baad2c with catch @ 00babc10 */
      lVar8 = (long)param_1 + *(long *)(*param_1 + -0x18);
                    /* catch() { ... } // from try @ 00baad00 with catch @ 00babc20 */
                    /* catch() { ... } // from try @ 00baa350 with catch @ 00babc24 */
      _ZNSt6__ndk18ios_base5clearEj(lVar8,*(uint *)(lVar8 + 0x20) | 5);
    }
  }
  lVar8 = *(long *)(*param_1 + -0x18);
                    /* catch() { ... } // from try @ 00baa324 with catch @ 00babc34 */
                    /* catch() { ... } // from try @ 00baa038 with catch @ 00babc38 */
                    /* catch() { ... } // from try @ 00baa00c with catch @ 00babc48 */
                    /* catch() { ... } // from try @ 00baafe8 with catch @ 00babc4c */
                    /* catch() { ... } // from try @ 00baafbc with catch @ 00babc5c */
                    /* catch() { ... } // from try @ 00baace0 with catch @ 00babc60 */
                    /* catch() { ... } // from try @ 00baacb4 with catch @ 00babc70 */
                    /* catch() { ... } // from try @ 00baa304 with catch @ 00babc74 */
  if ((((*(long *)((long)param_1 + lVar8 + 0x28) != 0) &&
       (*(int *)((long)param_1 + lVar8 + 0x20) == 0)) &&
      ((*(byte *)((long)param_1 + lVar8 + 9) >> 5 & 1) != 0)) &&
     ((uVar7 = _ZSt18uncaught_exceptionv(), (uVar7 & 1) == 0 &&
      (iVar4 = (**(code **)(**(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28) + 0x30))
                         (), iVar4 == -1)))) {
                    /* catch() { ... } // from try @ 00baa2d8 with catch @ 00babc84 */
    lVar8 = (long)param_1 + *(long *)(*param_1 + -0x18);
                    /* catch() { ... } // from try @ 00ba9fec with catch @ 00babc88 */
    _ZNSt6__ndk18ios_base5clearEj(lVar8,*(uint *)(lVar8 + 0x20) | 1);
  }
                    /* catch() { ... } // from try @ 00ba9fc0 with catch @ 00babc98 */
                    /* catch() { ... } // from try @ 00baaf98 with catch @ 00babc9c */
  if (*(long *)(lVar2 + 0x28) == local_58) {
                    /* catch() { ... } // from try @ 00baac90 with catch @ 00babcac */
                    /* catch() { ... } // from try @ 00baa2b4 with catch @ 00babcbc */
    return param_1;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
