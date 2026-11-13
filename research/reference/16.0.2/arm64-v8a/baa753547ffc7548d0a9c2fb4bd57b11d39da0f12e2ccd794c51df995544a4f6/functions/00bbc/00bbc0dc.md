# 00bbc0dc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bbc0dc",
  "name": "_ZN8firebase9messaging8RegisterEv",
  "size": 468,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "280bce1eab6b5d75f1c10ea20457ef94483df0c8b8cc845cef369a3e7c227806",
  "source_text_sha256": "280bce1eab6b5d75f1c10ea20457ef94483df0c8b8cc845cef369a3e7c227806"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497874](../00497/00497874.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5aad0](../00c5a/00c5aad0.md)
- [00c5aae0](../00c5a/00c5aae0.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5acb0](../00c5a/00c5acb0.md)
- [00c5ad40](../00c5a/00c5ad40.md)
- [00c5ad70](../00c5a/00c5ad70.md)
- [00c5ae70](../00c5a/00c5ae70.md)
- [00c5aea0](../00c5a/00c5aea0.md)
- [00c5aed0](../00c5a/00c5aed0.md)
- [00c5af10](../00c5a/00c5af10.md)
- [00c5b010](../00c5b/00c5b010.md)
- [00c5b030](../00c5b/00c5b030.md)
- [00c5b040](../00c5b/00c5b040.md)
- [00c5b0d0](../00c5b/00c5b0d0.md)
- [00c5b150](../00c5b/00c5b150.md)
- [00c5d340](../00c5d/00c5d340.md)

## 関連文字列（未確認候補）

~~~text
"Messaging"
"Messaging not initialized."
"internal::IsInitialized()"
~~~

## 疑似コード / UTF-8 3062 bytes

~~~c

void _ZN8firebase9messaging8RegisterEv(long param_1)

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
  
  uVar4 = DAT_01126470;
                    /* try { // try from 00bbc0e0 to 00cbc17b has its CatchHandler @ 00bbc850 */
  lVar3 = tpidr_el0;
  local_48 = *(long *)(lVar3 + 0x28);
  if (DAT_01126460 == 0) {
    _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
    _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
                    /* try { // try from 00bbc1f8 to 00cbc21f has its CatchHandler @ 00bbc7f8 */
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    _ZN8firebase5Mutex7AcquireEv(DAT_01126470);
    uVar5 = _ZN8firebase9messaging10FutureData3GetEv();
    _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E(local_78,uVar5,5,0,0);
    _ZN8firebase12FutureHandleC1ERKS0_(local_60,local_78);
    _ZN8firebase12FutureHandleD2Ev(local_78);
    plVar6 = (long *)_ZNK8firebase3App9GetJNIEnvEv(DAT_01126460);
    uVar7 = FUN_00497874(plVar6,DAT_01126498,DAT_01126400);
                    /* try { // try from 00bbc17c to 00cbc1f7 has its CatchHandler @ 00bbb99c */
    _ZN8firebase4util27GetAndClearExceptionMessageEP7_JNIEnv(local_78,plVar6);
    uVar1 = (ulong)(local_78[0] >> 1);
    if ((local_78[0] & 1) != 0) {
      uVar1 = local_70;
    }
    if (uVar1 == 0) {
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (plVar6,uVar7,FUN_00bbc344,local_60[0],"Messaging");
    }
    else {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_88,local_60);
      pvVar2 = (void *)((ulong)local_78 | 1);
      if ((local_78[0] & 1) != 0) {
        pvVar2 = local_68;
      }
      _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
                (uVar5,auStack_88,0xffffffff,pvVar2,auStack_50);
      _ZN8firebase12FutureHandleD2Ev(auStack_88);
    }
    (**(code **)(*plVar6 + 0xb8))(plVar6,uVar7);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar6);
                    /* try { // try from 00bbc254 to 00cbc25f has its CatchHandler @ 00bbc7c0 */
    _ZN8firebase6FutureIvEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,uVar5,local_60);
    if ((local_78[0] & 1) != 0) {
      _ZdlPv(local_68);
    }
    _ZN8firebase12FutureHandleD2Ev(local_60);
    _ZN8firebase5Mutex7ReleaseEv(uVar4);
  }
  if (*(long *)(lVar3 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00bbc2ac to 00cbc2cf has its CatchHandler @ 00bbc7c8 */
  __stack_chk_fail();
}

~~~
