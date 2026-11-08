# 00b6eeac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00b6eeac",
  "name": "_ZN8firebase4auth4User8GetTokenEb",
  "size": 512,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5addd8f962c8fe7736ef0115899bd1086e370b781081229a65978a951f68129a",
  "source_text_sha256": "5addd8f962c8fe7736ef0115899bd1086e370b781081229a65978a951f68129a"
}
~~~

## 呼び出し元

- [00bddbb0](../00bdd/00bddbb0.md)

## 呼び出し先

- [0047495c](../00474/0047495c.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)
- [00bddbf0](../00bdd/00bddbf0.md)
- [00bddd30](../00bdd/00bddd30.md)
- [00bdddc0](../00bdd/00bdddc0.md)
- [00bddef0](../00bdd/00bddef0.md)
- [00bddf30](../00bdd/00bddf30.md)
- [00bddf70](../00bdd/00bddf70.md)
- [00bde070](../00bde/00bde070.md)
- [00bde1b0](../00bde/00bde1b0.md)
- [00be0e60](../00be0/00be0e60.md)

## 疑似コード / UTF-8 4148 bytes

~~~c

void _ZN8firebase4auth4User8GetTokenEb(long param_1,long param_2,byte param_3)

{
  long lVar1;
  undefined *puVar2;
  undefined8 *puVar3;
  long *plVar4;
  undefined8 uVar5;
  ulong uVar6;
  undefined8 uVar7;
  long lVar8;
  long lVar9;
  long lVar10;
  undefined1 auStack_88 [16];
  undefined1 auStack_78 [16];
  undefined1 auStack_68 [16];
  long local_58;
  
                    /* try { // try from 00b6eeb4 to 00c6eebf has its CatchHandler @ 00b70834 */
                    /* try { // try from 00b6eec0 to 00c6ef53 has its CatchHandler @ 00b6e3fc */
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  lVar9 = *(long *)(param_2 + 0x98);
  if ((lVar9 == 0) || (*(long *)(lVar9 + 0x200) == 0)) {
    _ZN8firebase5MutexC2ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    lVar9 = lVar9 + 0x10;
    puVar3 = (undefined8 *)_Znwm(0x18);
    puVar3[1] = 0;
    puVar3[2] = 0;
    *puVar3 = 0;
    _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E
              (auStack_68,lVar9,9,puVar3,
               PTR__ZN8firebase26ReferenceCountedFutureImpl7DeleteTINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvPv_00c1b868
              );
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,auStack_68);
    _ZN8firebase12FutureHandleD1Ev(auStack_68);
    plVar4 = (long *)_ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
    lVar10 = *(long *)(param_2 + 0x98);
    lVar8 = lVar10 + 700;
    _ZN8firebase5Mutex7AcquireEv(lVar8);
                    /* try { // try from 00b6ef54 to 00c6ef5f has its CatchHandler @ 00b707d4 */
    *(byte *)(lVar10 + 0x2b8) = param_3 & 1;
    _ZN8firebase5Mutex7ReleaseEv(lVar8);
                    /* try { // try from 00b6ef7c to 00c6ef97 has its CatchHandler @ 00b707e4 */
    uVar5 = FUN_0047495c(plVar4,*(undefined8 *)(*(long *)(param_2 + 0x98) + 0x200),DAT_010a19f0,
                         param_3 & 1);
    uVar6 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                      (plVar4,lVar9,auStack_78);
    if ((uVar6 & 1) == 0) {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_88,auStack_78);
      puVar3 = *(undefined8 **)(param_2 + 0x98);
      uVar7 = _ZNK8firebase3App9GetJNIEnvEv(*puVar3);
      lVar8 = _Znwm(0x20);
      _ZN8firebase12FutureHandleC1ERKS0_(lVar8,auStack_88);
      puVar2 = 
      PTR__ZN8firebase4auth15ReadTokenResultEP8_jobjectPNS0_18FutureCallbackDataINSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEEEEbPv_00c1bbd8
      ;
      *(undefined8 **)(lVar8 + 0x10) = puVar3;
      *(undefined **)(lVar8 + 0x18) = puVar2;
      if ((*(byte *)(puVar3 + 0x28) & 1) == 0) {
        lVar10 = (long)puVar3 + 0x141;
      }
      else {
        lVar10 = puVar3[0x2a];
      }
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (uVar7,uVar5,
                 PTR__ZN8firebase4auth14FutureCallbackINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c1bbd0
                 ,lVar8,lVar10);
      _ZN8firebase12FutureHandleD1Ev(auStack_88);
      (**(code **)(*plVar4 + 0xb8))(plVar4,uVar5);
    }
    else {
                    /* try { // try from 00b6ef98 to 00c6f0db has its CatchHandler @ 00b6e3fc */
      lVar10 = *(long *)(param_2 + 0x98);
      lVar8 = lVar10 + 700;
      _ZN8firebase5Mutex7AcquireEv(lVar8);
      *(undefined1 *)(lVar10 + 0x2b8) = 0;
      _ZN8firebase5Mutex7ReleaseEv(lVar8);
    }
    _ZN8firebase6FutureINSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,lVar9,auStack_78);
    _ZN8firebase12FutureHandleD1Ev(auStack_78);
  }
  if (*(long *)(lVar1 + 0x28) == local_58) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
