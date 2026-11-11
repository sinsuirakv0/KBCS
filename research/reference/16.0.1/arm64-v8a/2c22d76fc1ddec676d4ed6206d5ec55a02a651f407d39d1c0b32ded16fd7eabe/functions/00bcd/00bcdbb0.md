# 00bcdbb0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bcdbb0",
  "name": "_ZN8firebase4auth4Auth22FetchProvidersForEmailEPKc",
  "size": 440,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "35a8f2510d1530af8852371f307dac7724d58a1865a9564e95f87346de29f849",
  "source_text_sha256": "35a8f2510d1530af8852371f307dac7724d58a1865a9564e95f87346de29f849"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497834](../00497/00497834.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c5aa90](../00c5a/00c5aa90.md)
- [00c5ae00](../00c5a/00c5ae00.md)
- [00c5ae40](../00c5a/00c5ae40.md)
- [00c5af40](../00c5a/00c5af40.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5dce0](../00c5d/00c5dce0.md)
- [00c5dd40](../00c5d/00c5dd40.md)

## 疑似コード / UTF-8 2921 bytes

~~~c

void _ZN8firebase4auth4Auth22FetchProvidersForEmailEPKc
               (undefined8 param_1,long *param_2,undefined8 param_3)

{
  long lVar1;
  long lVar2;
  undefined8 *puVar3;
  long *plVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  ulong uVar7;
  long lVar8;
  long lVar9;
  undefined1 auStack_88 [16];
  undefined1 auStack_78 [16];
  undefined1 auStack_68 [16];
  long local_58;
  
                    /* try { // try from 00bcdbb4 to 00ccdbbb has its CatchHandler @ 00bcea1c */
                    /* try { // try from 00bcdbbc to 00ccdd5f has its CatchHandler @ 00bcc5d0 */
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
  lVar1 = *param_2 + 0x10;
  puVar3 = (undefined8 *)_Znwm(0x18);
  puVar3[1] = 0;
  puVar3[2] = 0;
  *puVar3 = 0;
  _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E
            (auStack_68,lVar1,0,puVar3,
             PTR__ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth4Auth20FetchProvidersResultEEEvPv_00c9b9f0
            );
  _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,auStack_68);
  _ZN8firebase12FutureHandleD2Ev(auStack_68);
  plVar4 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)*param_2);
  uVar5 = (**(code **)(*plVar4 + 0x538))(plVar4,param_3);
  uVar6 = FUN_00497834(plVar4,*(undefined8 *)(*param_2 + 0x1f8),DAT_01126790,uVar5);
  (**(code **)(*plVar4 + 0xb8))(plVar4,uVar5);
  uVar7 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_4Auth20FetchProvidersResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                    (plVar4,lVar1,auStack_78);
  if ((uVar7 & 1) == 0) {
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_88,auStack_78);
    puVar3 = (undefined8 *)*param_2;
    uVar5 = _ZNK8firebase3App9GetJNIEnvEv(*puVar3);
    lVar8 = _Znwm(0x20);
    _ZN8firebase12FutureHandleC1ERKS0_(lVar8,auStack_88);
    *(undefined8 **)(lVar8 + 0x10) = puVar3;
    *(code **)(lVar8 + 0x18) = FUN_00bcdeb4;
    if ((*(byte *)(puVar3 + 0x28) & 1) == 0) {
      lVar9 = (long)puVar3 + 0x141;
    }
    else {
      lVar9 = puVar3[0x2a];
    }
    _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
              (uVar5,uVar6,
               PTR__ZN8firebase4auth14FutureCallbackINS0_4Auth20FetchProvidersResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9ba08
               ,lVar8,lVar9);
    _ZN8firebase12FutureHandleD2Ev(auStack_88);
    (**(code **)(*plVar4 + 0xb8))(plVar4,uVar6);
  }
  _ZN8firebase6FutureINS_4auth4Auth20FetchProvidersResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
            (param_1,lVar1,auStack_78);
  _ZN8firebase12FutureHandleD2Ev(auStack_78);
  if (*(long *)(lVar2 + 0x28) == local_58) {
                    /* try { // try from 00bcdd60 to 00ccdd77 has its CatchHandler @ 00bcea14 */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
