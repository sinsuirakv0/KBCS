# 00bbbcdc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bbbcdc",
  "name": "FUN_00bbbcdc",
  "size": 444,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d1bc3d638d885641760719ada7586978f20d0a7c5ac5b9c6137a6f8b9bfcceff",
  "source_text_sha256": "d1bc3d638d885641760719ada7586978f20d0a7c5ac5b9c6137a6f8b9bfcceff"
}
~~~

## 呼び出し元

- [00bbba0c](../00bbb/00bbba0c.md)
- [00bbd25c](../00bbd/00bbd25c.md)

## 呼び出し先

- [00497874](../00497/00497874.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ae70](../00c5a/00c5ae70.md)
- [00c5aed0](../00c5a/00c5aed0.md)
- [00c5b010](../00c5b/00c5b010.md)
- [00c5b020](../00c5b/00c5b020.md)
- [00c5b030](../00c5b/00c5b030.md)
- [00c5b150](../00c5b/00c5b150.md)
- [00c5b200](../00c5b/00c5b200.md)
- [00c5d340](../00c5d/00c5d340.md)

## 関連文字列（未確認候補）

~~~text
"Messaging"
"Unsubscribe from topic %s"
~~~

## 疑似コード / UTF-8 2399 bytes

~~~c

void FUN_00bbbcdc(undefined8 param_1,undefined8 param_2)

{
  void *pvVar1;
  long lVar2;
  char cVar3;
  long *plVar4;
  undefined8 uVar5;
  long lVar6;
  undefined8 uVar7;
  undefined1 auStack_78 [16];
  byte local_68 [16];
  void *local_58;
  undefined1 auStack_50 [8];
  long local_48;
  
  lVar2 = tpidr_el0;
  local_48 = *(long *)(lVar2 + 0x28);
  _ZN8firebase8LogDebugEPKcz("Unsubscribe from topic %s",param_1);
  plVar4 = (long *)_ZNK8firebase3App9GetJNIEnvEv(DAT_01126460);
  uVar5 = (**(code **)(*plVar4 + 0x538))(plVar4,param_1);
                    /* try { // try from 00bbbd48 to 00cbbd53 has its CatchHandler @ 00bbc81c */
  lVar6 = FUN_00497874(plVar4,DAT_01126498,DAT_011263d0,uVar5);
  cVar3 = (**(code **)(*plVar4 + 0x720))(plVar4);
  if (cVar3 == '\0') {
    if (lVar6 != 0) {
      uVar7 = _Znwm(0x10);
      _ZN8firebase12FutureHandleC1ERKS0_(uVar7,param_2);
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (plVar4,lVar6,FUN_00bbd4fc,uVar7,"Messaging");
                    /* try { // try from 00bbbe3c to 00cbbedb has its CatchHandler @ 00bbc838 */
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar4);
      (**(code **)(*plVar4 + 0xb8))(plVar4,lVar6);
    }
  }
  else {
    uVar7 = (**(code **)(*plVar4 + 0x78))(plVar4);
                    /* try { // try from 00bbbd90 to 00cbbd9b has its CatchHandler @ 00bbc820 */
    (**(code **)(*plVar4 + 0x88))(plVar4);
    _ZN8firebase4util23GetMessageFromExceptionEP7_JNIEnvP8_jobject(local_68,plVar4,uVar7);
    uVar7 = _ZN8firebase9messaging10FutureData3GetEv();
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,param_2);
    pvVar1 = (void *)((ulong)local_68 | 1);
    if ((local_68[0] & 1) != 0) {
      pvVar1 = local_58;
    }
    _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
              (uVar7,auStack_78,2,pvVar1,auStack_50);
    _ZN8firebase12FutureHandleD2Ev(auStack_78);
                    /* try { // try from 00bbbdf4 to 00cbbdff has its CatchHandler @ 00bbc818 */
    if ((local_68[0] & 1) != 0) {
      _ZdlPv(local_58);
    }
  }
  (**(code **)(*plVar4 + 0xb8))(plVar4,uVar5);
  if (*(long *)(lVar2 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
