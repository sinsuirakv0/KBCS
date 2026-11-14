# 00bbccd0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bbccd0",
  "name": "FUN_00bbccd0",
  "size": 444,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "02a50d351a11fa033bba2f60dca602fecd10ee815a78aaa70e491de35020412a",
  "source_text_sha256": "02a50d351a11fa033bba2f60dca602fecd10ee815a78aaa70e491de35020412a"
}
~~~

## 呼び出し元

- [00bbca00](../00bbc/00bbca00.md)
- [00bbe250](../00bbe/00bbe250.md)

## 呼び出し先

- [00497b94](../00497/00497b94.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5bb30](../00c5b/00c5bb30.md)
- [00c5be40](../00c5b/00c5be40.md)
- [00c5bea0](../00c5b/00c5bea0.md)
- [00c5bfe0](../00c5b/00c5bfe0.md)
- [00c5bff0](../00c5b/00c5bff0.md)
- [00c5c000](../00c5c/00c5c000.md)
- [00c5c120](../00c5c/00c5c120.md)
- [00c5c1d0](../00c5c/00c5c1d0.md)
- [00c5e310](../00c5e/00c5e310.md)

## 関連文字列（未確認候補）

~~~text
"Messaging"
"Unsubscribe from topic %s"
~~~

## 疑似コード / UTF-8 2399 bytes

~~~c

void FUN_00bbccd0(undefined8 param_1,undefined8 param_2)

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
  plVar4 = (long *)_ZNK8firebase3App9GetJNIEnvEv(DAT_01127420);
  uVar5 = (**(code **)(*plVar4 + 0x538))(plVar4,param_1);
                    /* try { // try from 00bbcd3c to 00cbcd47 has its CatchHandler @ 00bbd810 */
  lVar6 = FUN_00497b94(plVar4,DAT_01127458,DAT_01127390,uVar5);
  cVar3 = (**(code **)(*plVar4 + 0x720))(plVar4);
  if (cVar3 == '\0') {
    if (lVar6 != 0) {
      uVar7 = _Znwm(0x10);
      _ZN8firebase12FutureHandleC1ERKS0_(uVar7,param_2);
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (plVar4,lVar6,FUN_00bbe4f0,uVar7,"Messaging");
                    /* try { // try from 00bbce30 to 00cbcecf has its CatchHandler @ 00bbd82c */
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar4);
      (**(code **)(*plVar4 + 0xb8))(plVar4,lVar6);
    }
  }
  else {
    uVar7 = (**(code **)(*plVar4 + 0x78))(plVar4);
                    /* try { // try from 00bbcd84 to 00cbcd8f has its CatchHandler @ 00bbd814 */
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
                    /* try { // try from 00bbcde8 to 00cbcdf3 has its CatchHandler @ 00bbd80c */
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
