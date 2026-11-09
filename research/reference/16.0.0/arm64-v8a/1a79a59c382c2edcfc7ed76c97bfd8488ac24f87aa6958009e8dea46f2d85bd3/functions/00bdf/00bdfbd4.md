# 00bdfbd4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bdfbd4",
  "name": "_ZN8firebase4auth4User6UnlinkEPKc",
  "size": 440,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d6c76afe4e8f3d0e732125a21420b187e6692f8df60dec08cc068c05513cda00",
  "source_text_sha256": "d6c76afe4e8f3d0e732125a21420b187e6692f8df60dec08cc068c05513cda00"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [004977f4](../00497/004977f4.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5a690](../00c5a/00c5a690.md)
- [00c5a7e0](../00c5a/00c5a7e0.md)
- [00c5a870](../00c5a/00c5a870.md)
- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5ab40](../00c5a/00c5ab40.md)
- [00c5ac80](../00c5a/00c5ac80.md)
- [00c5d800](../00c5d/00c5d800.md)
- [00c5d8d0](../00c5d/00c5d8d0.md)
- [00c5d930](../00c5d/00c5d930.md)

## 疑似コード / UTF-8 3186 bytes

~~~c

void _ZN8firebase4auth4User6UnlinkEPKc(long param_1,long param_2,undefined8 param_3)

{
  long lVar1;
  undefined *puVar2;
  long *plVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  ulong uVar6;
  long lVar7;
  long lVar8;
  long lVar9;
  undefined8 *puVar10;
  undefined1 auStack_78 [16];
  undefined1 auStack_68 [16];
  long local_58;
  
                    /* try { // try from 00bdfbdc to 00cdfc0f has its CatchHandler @ 00be01dc */
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  lVar9 = *(long *)(param_2 + 0x98);
  if ((lVar9 == 0) || (*(long *)(lVar9 + 0x200) == 0)) {
                    /* try { // try from 00bdfcf0 to 00cdfcf7 has its CatchHandler @ 00be02ac */
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    lVar9 = lVar9 + 0x10;
    _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEi
              (auStack_68,lVar9,0x15);
    plVar3 = (long *)_ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
                    /* try { // try from 00bdfc3c to 00cdfc47 has its CatchHandler @ 00be02ac */
    uVar4 = (**(code **)(*plVar3 + 0x538))(plVar3,param_3);
                    /* try { // try from 00bdfc54 to 00cdfc87 has its CatchHandler @ 00be01e0 */
    uVar5 = FUN_004977f4(plVar3,*(undefined8 *)(*(long *)(param_2 + 0x98) + 0x200),DAT_01126968,
                         uVar4);
    (**(code **)(*plVar3 + 0xb8))(plVar3,uVar4);
    uVar6 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                      (plVar3,lVar9,auStack_68);
    if ((uVar6 & 1) == 0) {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,auStack_68);
      puVar10 = *(undefined8 **)(param_2 + 0x98);
      uVar4 = _ZNK8firebase3App9GetJNIEnvEv(*puVar10);
      lVar7 = _Znwm(0x20);
      _ZN8firebase12FutureHandleC1ERKS0_(lVar7,auStack_78);
      puVar2 = 
      PTR__ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv_00c9b620
      ;
      *(undefined8 **)(lVar7 + 0x10) = puVar10;
      *(undefined **)(lVar7 + 0x18) = puVar2;
      if ((*(byte *)(puVar10 + 0x28) & 1) == 0) {
        lVar8 = (long)puVar10 + 0x141;
      }
      else {
        lVar8 = puVar10[0x2a];
      }
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (uVar4,uVar5,
                 PTR__ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9b600
                 ,lVar7,lVar8);
      _ZN8firebase12FutureHandleD2Ev(auStack_78);
      (**(code **)(*plVar3 + 0xb8))(plVar3,uVar5);
    }
    _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,lVar9,auStack_68);
    _ZN8firebase12FutureHandleD2Ev(auStack_68);
  }
  if (*(long *)(lVar1 + 0x28) == local_58) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
