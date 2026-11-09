# 00bbc9ec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bbc9ec",
  "name": "_ZN8firebase9messaging11DeleteTokenEv",
  "size": 468,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0458a94bfc36673b64c0faeed5bb391da1431e8a1cf3a38ef6dba405cc3fdaad",
  "source_text_sha256": "0458a94bfc36673b64c0faeed5bb391da1431e8a1cf3a38ef6dba405cc3fdaad"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [004977f4](../00497/004977f4.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)
- [00c5a690](../00c5a/00c5a690.md)
- [00c5a7e0](../00c5a/00c5a7e0.md)
- [00c5a870](../00c5a/00c5a870.md)
- [00c5a8a0](../00c5a/00c5a8a0.md)
- [00c5a9a0](../00c5a/00c5a9a0.md)
- [00c5a9d0](../00c5a/00c5a9d0.md)
- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5aa40](../00c5a/00c5aa40.md)
- [00c5ab40](../00c5a/00c5ab40.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ab70](../00c5a/00c5ab70.md)
- [00c5ac00](../00c5a/00c5ac00.md)
- [00c5ac80](../00c5a/00c5ac80.md)
- [00c5ce70](../00c5c/00c5ce70.md)

## 関連文字列（未確認候補）

~~~text
"Messaging"
"Messaging not initialized."
"internal::IsInitialized()"
~~~

## 疑似コード / UTF-8 2969 bytes

~~~c

void _ZN8firebase9messaging11DeleteTokenEv(long param_1)

{
  ulong uVar1;
  void *pvVar2;
  long lVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  long *plVar6;
  undefined8 uVar7;
  undefined1 auStack_88 [16];
  byte local_78 [8];
  ulong local_70;
  void *local_68;
  undefined8 local_60 [2];
  undefined1 auStack_50 [8];
  long local_48;
  
  uVar4 = DAT_01125f70;
  lVar3 = tpidr_el0;
  local_48 = *(long *)(lVar3 + 0x28);
  if (DAT_01125f60 == 0) {
    _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
    _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    _ZN8firebase5Mutex7AcquireEv(DAT_01125f70);
    uVar5 = _ZN8firebase9messaging10FutureData3GetEv();
                    /* try { // try from 00bbca3c to 00cbca7f has its CatchHandler @ 00bbc6dc */
    _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E(local_78,uVar5,4,0,0);
    _ZN8firebase12FutureHandleC1ERKS0_(local_60,local_78);
    _ZN8firebase12FutureHandleD2Ev(local_78);
    plVar6 = (long *)_ZNK8firebase3App9GetJNIEnvEv(DAT_01125f60);
    uVar7 = FUN_004977f4(plVar6,DAT_01125f98,DAT_01125ef8);
                    /* try { // try from 00bbca80 to 00cbca83 has its CatchHandler @ 00bbcc2c */
    _ZN8firebase4util27GetAndClearExceptionMessageEP7_JNIEnv(local_78,plVar6);
    uVar1 = (ulong)(local_78[0] >> 1);
    if ((local_78[0] & 1) != 0) {
      uVar1 = local_70;
    }
    if (uVar1 == 0) {
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (plVar6,uVar7,FUN_00bbbe80,local_60[0],"Messaging");
    }
    else {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_88,local_60);
      pvVar2 = (void *)((ulong)local_78 | 1);
      if ((local_78[0] & 1) != 0) {
        pvVar2 = local_68;
      }
      _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
                (uVar5,auStack_88,0xffffffff,pvVar2,auStack_50);
                    /* try { // try from 00bbcae0 to 00cbcae7 has its CatchHandler @ 00bbcc70 */
      _ZN8firebase12FutureHandleD2Ev(auStack_88);
    }
    (**(code **)(*plVar6 + 0xb8))(plVar6,uVar7);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar6);
    _ZN8firebase6FutureIvEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,uVar5,local_60);
    if ((local_78[0] & 1) != 0) {
      _ZdlPv(local_68);
    }
    _ZN8firebase12FutureHandleD2Ev(local_60);
    _ZN8firebase5Mutex7ReleaseEv(uVar4);
  }
  if (*(long *)(lVar3 + 0x28) == local_48) {
                    /* try { // try from 00bbcbac to 00cbcbb3 has its CatchHandler @ 00bbcc80 */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
