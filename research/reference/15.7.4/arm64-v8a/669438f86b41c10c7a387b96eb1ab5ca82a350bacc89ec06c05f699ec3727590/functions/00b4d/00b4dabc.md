# 00b4dabc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00b4d9b0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4d/00b4d9b0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00b4dabc",
  "name": "FUN_00b4dabc",
  "size": 444,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0bdd87f7f791b260509162e2a94dd934b4d82b12003acabf9150fc28886b8c4b",
  "source_text_sha256": "0bdd87f7f791b260509162e2a94dd934b4d82b12003acabf9150fc28886b8c4b"
}
~~~

## 呼び出し元

- [00b4d7ec](../00b4d/00b4d7ec.md)
- [00b4e948](../00b4e/00b4e948.md)

## 呼び出し先

- [0047495c](../00474/0047495c.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bddc40](../00bdd/00bddc40.md)
- [00bddf80](../00bdd/00bddf80.md)
- [00bde0c0](../00bde/00bde0c0.md)
- [00bde0d0](../00bde/00bde0d0.md)
- [00bde0e0](../00bde/00bde0e0.md)
- [00bde200](../00bde/00bde200.md)
- [00bde2b0](../00bde/00bde2b0.md)
- [00bdee00](../00bde/00bdee00.md)
- [00be0300](../00be0/00be0300.md)

## 関連文字列（未確認候補）

~~~text
"Messaging"
"Unsubscribe from topic %s"
~~~

## 疑似コード / UTF-8 4795 bytes

~~~c

void FUN_00b4dabc(undefined8 param_1,undefined8 param_2)

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
  
                    /* catch() { ... } // from try @ 00b4cd4c with catch @ 00b4dabc */
                    /* catch() { ... } // from try @ 00b4cd2c with catch @ 00b4dac0 */
                    /* catch() { ... } // from try @ 00b4ca44 with catch @ 00b4dad0 */
                    /* catch() { ... } // from try @ 00b4ca24 with catch @ 00b4dad4 */
  lVar2 = tpidr_el0;
  local_48 = *(long *)(lVar2 + 0x28);
                    /* catch() { ... } // from try @ 00b4c068 with catch @ 00b4dae4 */
                    /* catch() { ... } // from try @ 00b4c048 with catch @ 00b4dae8 */
  _ZN8firebase8LogDebugEPKcz("Unsubscribe from topic %s",param_1);
                    /* catch() { ... } // from try @ 00b4bd50 with catch @ 00b4daf8 */
                    /* catch() { ... } // from try @ 00b4bd30 with catch @ 00b4dafc */
  plVar4 = (long *)_ZNK8firebase3App9GetJNIEnvEv(DAT_010a10a0);
                    /* catch() { ... } // from try @ 00b4cd0c with catch @ 00b4db0c */
  uVar5 = (**(code **)(*plVar4 + 0x538))(plVar4,param_1);
                    /* catch() { ... } // from try @ 00b4ccf8 with catch @ 00b4db2c */
                    /* catch() { ... } // from try @ 00b4ca04 with catch @ 00b4db30 */
  lVar6 = FUN_0047495c(plVar4,DAT_010a10d8,DAT_010a1020,uVar5);
  cVar3 = (**(code **)(*plVar4 + 0x720))(plVar4);
                    /* catch() { ... } // from try @ 00b4c9f0 with catch @ 00b4db50 */
  if (cVar3 == '\0') {
    if (lVar6 != 0) {
      uVar7 = _Znwm(0x10);
      _ZN8firebase12FutureHandleC1ERKS0_(uVar7,param_2);
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (plVar4,lVar6,FUN_00b4eb58,uVar7,"Messaging");
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar4);
                    /* catch() { ... } // from try @ 00b4d3c0 with catch @ 00b4dc24 */
                    /* catch() { ... } // from try @ 00b4d028 with catch @ 00b4dc28 */
      (**(code **)(*plVar4 + 0xb8))(plVar4,lVar6);
    }
  }
  else {
                    /* catch() { ... } // from try @ 00b4c028 with catch @ 00b4db54 */
    uVar7 = (**(code **)(*plVar4 + 0x78))(plVar4);
                    /* catch() { ... } // from try @ 00b4c014 with catch @ 00b4db74 */
    (**(code **)(*plVar4 + 0x88))(plVar4);
                    /* catch() { ... } // from try @ 00b4bd10 with catch @ 00b4db78 */
    _ZN8firebase4util23GetMessageFromExceptionEP7_JNIEnvP8_jobject(local_68,plVar4,uVar7);
    uVar7 = _ZN8firebase9messaging10FutureData3GetEv();
                    /* catch() { ... } // from try @ 00b4bcfc with catch @ 00b4db98 */
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,param_2);
                    /* catch() { ... } // from try @ 00b4ccd4 with catch @ 00b4db9c */
                    /* catch() { ... } // from try @ 00b4c9cc with catch @ 00b4dba0 */
                    /* catch() { ... } // from try @ 00b4c92c with catch @ 00b4dba4 */
                    /* catch() { ... } // from try @ 00b4c8a4 with catch @ 00b4dba8 */
    pvVar1 = (void *)((ulong)local_68 | 1);
                    /* catch() { ... } // from try @ 00b4bff0 with catch @ 00b4dbb0 */
    if ((local_68[0] & 1) != 0) {
      pvVar1 = local_58;
    }
                    /* catch() { ... } // from try @ 00b4bcd8 with catch @ 00b4dbb4 */
                    /* catch() { ... } // from try @ 00b4d66c with catch @ 00b4dbb8 */
                    /* catch() { ... } // from try @ 00b4d2c8 with catch @ 00b4dbbc */
    _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
              (uVar7,auStack_78,2,pvVar1,auStack_50);
    _ZN8firebase12FutureHandleD1Ev(auStack_78);
    if ((local_68[0] & 1) != 0) {
      _ZdlPv(local_58);
    }
  }
                    /* catch() { ... } // from try @ 00b4cf30 with catch @ 00b4dc3c */
                    /* catch() { ... } // from try @ 00b4cc24 with catch @ 00b4dc40 */
                    /* catch() { ... } // from try @ 00b4c244 with catch @ 00b4dc44 */
                    /* catch() { ... } // from try @ 00b4bf2c with catch @ 00b4dc48 */
  (**(code **)(*plVar4 + 0xb8))(plVar4,uVar5);
  if (*(long *)(lVar2 + 0x28) == local_48) {
                    /* catch() { ... } // from try @ 00b4c4b0 with catch @ 00b4dc64 */
                    /* catch() { ... } // from try @ 00b4c490 with catch @ 00b4dc68 */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
