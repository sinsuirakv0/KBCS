# 00bab6cc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bab6cc",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEs",
  "size": 468,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fe5207afacb334e1c653378fc6879cb0a2c4adb6bb4126955b832c82dde9df62",
  "source_text_sha256": "fe5207afacb334e1c653378fc6879cb0a2c4adb6bb4126955b832c82dde9df62"
}
~~~

## 呼び出し元

- [00c5c750](../00c5c/00c5c750.md)

## 呼び出し先

- [00c57ae0](../00c57/00c57ae0.md)
- [00c57e70](../00c57/00c57e70.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57ea0](../00c57/00c57ea0.md)
- [00c58af0](../00c58/00c58af0.md)
- [00c5ccf0](../00c5c/00c5ccf0.md)

## 疑似コード / UTF-8 5689 bytes

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
  
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
  lVar8 = *(long *)(*param_1 + -0x18);
  if (*(int *)((long)param_1 + lVar8 + 0x20) == 0) {
    if (*(long *)((long)param_1 + lVar8 + 0x88) != 0) {
      _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5flushEv();
      lVar8 = *(long *)(*param_1 + -0x18);
    }
    uVar1 = *(uint *)((long)param_1 + lVar8 + 8) & 0x4a;
    _ZNKSt6__ndk18ios_base6getlocEv(auStack_60);
    plVar5 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                               (auStack_60,
                                PTR__ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9b438
                               );
                    /* try { // try from 00bab754 to 00cab75f has its CatchHandler @ 00babffc */
    _ZNSt6__ndk16localeD1Ev(auStack_60);
                    /* catch() { ... } // from try @ 00bab390 with catch @ 00bab760
                       try { // try from 00bab760 to 00cac06b has its CatchHandler @ 00ba9230 */
    lVar8 = (long)param_1 + *(long *)(*param_1 + -0x18);
                    /* catch() { ... } // from try @ 00bab380 with catch @ 00bab764 */
    uVar3 = *(uint *)(lVar8 + 0x90);
                    /* catch() { ... } // from try @ 00baaff8 with catch @ 00bab768 */
    uVar9 = *(undefined8 *)(lVar8 + 0x28);
                    /* catch() { ... } // from try @ 00baafe8 with catch @ 00bab76c */
                    /* catch() { ... } // from try @ 00bab684 with catch @ 00bab770 */
    if (uVar3 == 0xffffffff) {
                    /* catch() { ... } // from try @ 00bab65c with catch @ 00bab774 */
      _ZNKSt6__ndk18ios_base6getlocEv(auStack_60,lVar8);
                    /* catch() { ... } // from try @ 00bab630 with catch @ 00bab784 */
                    /* catch() { ... } // from try @ 00bab2e0 with catch @ 00bab788 */
                    /* catch() { ... } // from try @ 00bab2c4 with catch @ 00bab78c */
      plVar6 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                                 (auStack_60,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9a830);
                    /* catch() { ... } // from try @ 00bab298 with catch @ 00bab79c */
      uVar3 = (**(code **)(*plVar6 + 0x38))(plVar6,0x20);
                    /* catch() { ... } // from try @ 00bab60c with catch @ 00bab7a0 */
      _ZNSt6__ndk16localeD1Ev(auStack_60);
      uVar3 = uVar3 & 0xff;
                    /* catch() { ... } // from try @ 00bab5e0 with catch @ 00bab7b0 */
      *(uint *)(lVar8 + 0x90) = uVar3;
    }
                    /* catch() { ... } // from try @ 00bab5bc with catch @ 00bab7b4 */
                    /* catch() { ... } // from try @ 00bab274 with catch @ 00bab7c4 */
    uVar7 = (ulong)param_2;
    if (uVar1 != 8 && uVar1 != 0x40) {
      uVar7 = (long)(short)param_2;
    }
                    /* catch() { ... } // from try @ 00bab248 with catch @ 00bab7d4 */
                    /* catch() { ... } // from try @ 00bab224 with catch @ 00bab7d8 */
    lVar8 = (**(code **)(*plVar5 + 0x20))(plVar5,uVar9,lVar8,uVar3,uVar7);
    if (lVar8 == 0) {
                    /* catch() { ... } // from try @ 00bab590 with catch @ 00bab7e8 */
                    /* catch() { ... } // from try @ 00bab56c with catch @ 00bab7ec */
      lVar8 = (long)param_1 + *(long *)(*param_1 + -0x18);
                    /* catch() { ... } // from try @ 00bab540 with catch @ 00bab7fc */
                    /* catch() { ... } // from try @ 00bab1f8 with catch @ 00bab800 */
      _ZNSt6__ndk18ios_base5clearEj(lVar8,*(uint *)(lVar8 + 0x20) | 5);
    }
  }
                    /* catch() { ... } // from try @ 00bab1d4 with catch @ 00bab804 */
  lVar8 = *(long *)(*param_1 + -0x18);
                    /* catch() { ... } // from try @ 00bab1a8 with catch @ 00bab814 */
                    /* catch() { ... } // from try @ 00bab520 with catch @ 00bab818 */
                    /* catch() { ... } // from try @ 00bab4f4 with catch @ 00bab828 */
                    /* catch() { ... } // from try @ 00bab4d0 with catch @ 00bab82c */
                    /* catch() { ... } // from try @ 00bab188 with catch @ 00bab83c */
                    /* catch() { ... } // from try @ 00bab15c with catch @ 00bab84c */
                    /* catch() { ... } // from try @ 00bab138 with catch @ 00bab850 */
  if ((((*(long *)((long)param_1 + lVar8 + 0x28) != 0) &&
       (*(int *)((long)param_1 + lVar8 + 0x20) == 0)) &&
      ((*(byte *)((long)param_1 + lVar8 + 9) >> 5 & 1) != 0)) &&
     ((uVar7 = _ZSt18uncaught_exceptionv(), (uVar7 & 1) == 0 &&
      (iVar4 = (**(code **)(**(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28) + 0x30))
                         (), iVar4 == -1)))) {
    lVar8 = (long)param_1 + *(long *)(*param_1 + -0x18);
                    /* catch() { ... } // from try @ 00bab4a4 with catch @ 00bab860 */
                    /* catch() { ... } // from try @ 00bab484 with catch @ 00bab864 */
    _ZNSt6__ndk18ios_base5clearEj(lVar8,*(uint *)(lVar8 + 0x20) | 1);
  }
                    /* catch() { ... } // from try @ 00bab10c with catch @ 00bab874 */
                    /* catch() { ... } // from try @ 00bab0ec with catch @ 00bab878 */
  if (*(long *)(lVar2 + 0x28) == local_58) {
                    /* catch() { ... } // from try @ 00bab464 with catch @ 00bab888 */
    return param_1;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
