# 00bceb9c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bceb9c",
  "name": "_ZN8firebase4auth4Auth17SignInAnonymouslyEv",
  "size": 340,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "41e96f138b874be64e5df5b4c7a895ca83f956e3882cc592c4dd672928a2951c",
  "source_text_sha256": "41e96f138b874be64e5df5b4c7a895ca83f956e3882cc592c4dd672928a2951c"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497874](../00497/00497874.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5aed0](../00c5a/00c5aed0.md)
- [00c5b010](../00c5b/00c5b010.md)
- [00c5b150](../00c5b/00c5b150.md)
- [00c5dcd0](../00c5d/00c5dcd0.md)
- [00c5dda0](../00c5d/00c5dda0.md)
- [00c5de00](../00c5d/00c5de00.md)

## 疑似コード / UTF-8 2527 bytes

~~~c

void _ZN8firebase4auth4Auth17SignInAnonymouslyEv(undefined8 param_1,long *param_2)

{
  long lVar1;
  long lVar2;
  undefined *puVar3;
  long *plVar4;
  undefined8 uVar5;
  ulong uVar6;
  undefined8 uVar7;
  long lVar8;
  long lVar9;
  undefined8 *puVar10;
  undefined1 auStack_78 [16];
  undefined1 auStack_68 [16];
  long local_58;
  
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
  lVar1 = *param_2 + 0x10;
  _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEi
            (auStack_68,lVar1,4);
  plVar4 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)*param_2);
  uVar5 = FUN_00497874(plVar4,*(undefined8 *)(*param_2 + 0x1f8),DAT_011268a8);
  uVar6 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                    (plVar4,lVar1,auStack_68);
  if ((uVar6 & 1) == 0) {
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,auStack_68);
    puVar10 = (undefined8 *)*param_2;
    uVar7 = _ZNK8firebase3App9GetJNIEnvEv(*puVar10);
    lVar8 = _Znwm(0x20);
    _ZN8firebase12FutureHandleC1ERKS0_(lVar8,auStack_78);
    puVar3 = 
    PTR__ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv_00c9baf0
    ;
    *(undefined8 **)(lVar8 + 0x10) = puVar10;
    *(undefined **)(lVar8 + 0x18) = puVar3;
    if ((*(byte *)(puVar10 + 0x28) & 1) == 0) {
      lVar9 = (long)puVar10 + 0x141;
    }
    else {
      lVar9 = puVar10[0x2a];
    }
    _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
              (uVar7,uVar5,
               PTR__ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9bad0
               ,lVar8,lVar9);
    _ZN8firebase12FutureHandleD2Ev(auStack_78);
    (**(code **)(*plVar4 + 0xb8))(plVar4,uVar5);
  }
  _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
            (param_1,lVar1,auStack_68);
  _ZN8firebase12FutureHandleD2Ev(auStack_68);
                    /* try { // try from 00bcecc4 to 00ccee53 has its CatchHandler @ 00bcecc4
                       catch() { ... } // from try @ 00bcecc4 with catch @ 00bcecc4
                       catch() { ... } // from try @ 00bcee5c with catch @ 00bcecc4 */
  if (*(long *)(lVar2 + 0x28) == local_58) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
