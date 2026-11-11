# 00ba1abc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00ba1abc",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEi",
  "size": 468,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "12a32c3f17f6cffd9ebe3703bd764c502ca556b71b4bbe1aa341d5ecaf206bc1",
  "source_text_sha256": "12a32c3f17f6cffd9ebe3703bd764c502ca556b71b4bbe1aa341d5ecaf206bc1"
}
~~~

## 呼び出し元

- [00c584d0](../00c58/00c584d0.md)

## 呼び出し先

- [00c57ee0](../00c57/00c57ee0.md)
- [00c58270](../00c58/00c58270.md)
- [00c58280](../00c58/00c58280.md)
- [00c58290](../00c58/00c58290.md)
- [00c582a0](../00c58/00c582a0.md)
- [00c58ef0](../00c58/00c58ef0.md)
- [00c5d0f0](../00c5d/00c5d0f0.md)

## 疑似コード / UTF-8 2972 bytes

~~~c

long * _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEi(long *param_1,uint param_2)

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
                                PTR__ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9b838
                               );
    _ZNSt6__ndk16localeD1Ev(auStack_60);
    lVar8 = (long)param_1 + *(long *)(*param_1 + -0x18);
    uVar3 = *(uint *)(lVar8 + 0x90);
    uVar9 = *(undefined8 *)(lVar8 + 0x28);
    if (uVar3 == 0xffffffff) {
      _ZNKSt6__ndk18ios_base6getlocEv(auStack_60,lVar8);
      plVar6 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                                 (auStack_60,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9ac30);
      uVar3 = (**(code **)(*plVar6 + 0x38))(plVar6,0x20);
      _ZNSt6__ndk16localeD1Ev(auStack_60);
      uVar3 = uVar3 & 0xff;
      *(uint *)(lVar8 + 0x90) = uVar3;
    }
    uVar7 = (ulong)param_2;
    if (uVar1 != 8 && uVar1 != 0x40) {
      uVar7 = (long)(int)param_2;
    }
    lVar8 = (**(code **)(*plVar5 + 0x20))(plVar5,uVar9,lVar8,uVar3,uVar7);
    if (lVar8 == 0) {
      lVar8 = (long)param_1 + *(long *)(*param_1 + -0x18);
      _ZNSt6__ndk18ios_base5clearEj(lVar8,*(uint *)(lVar8 + 0x20) | 5);
    }
  }
  lVar8 = *(long *)(*param_1 + -0x18);
  if ((((*(long *)((long)param_1 + lVar8 + 0x28) != 0) &&
       (*(int *)((long)param_1 + lVar8 + 0x20) == 0)) &&
      ((*(byte *)((long)param_1 + lVar8 + 9) >> 5 & 1) != 0)) &&
     ((uVar7 = _ZSt18uncaught_exceptionv(), (uVar7 & 1) == 0 &&
      (iVar4 = (**(code **)(**(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28) + 0x30))
                         (), iVar4 == -1)))) {
                    /* try { // try from 00ba1c48 to 00ca1c9f has its CatchHandler @ 00ba1c48
                       catch() { ... } // from try @ 00ba1c48 with catch @ 00ba1c48
                       catch() { ... } // from try @ 00ba1ca8 with catch @ 00ba1c48
                       catch() { ... } // from try @ 00ba1ce8 with catch @ 00ba1c48 */
    lVar8 = (long)param_1 + *(long *)(*param_1 + -0x18);
    _ZNSt6__ndk18ios_base5clearEj(lVar8,*(uint *)(lVar8 + 0x20) | 1);
  }
  if (*(long *)(lVar2 + 0x28) == local_58) {
    return param_1;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
