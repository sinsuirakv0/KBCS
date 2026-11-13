# 00bcefb4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bcefb4",
  "name": "_ZN8firebase4auth4Auth30CreateUserWithEmailAndPasswordEPKcS3_",
  "size": 568,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d6073ffa1c6818ad8b7468d6c0f4f46c2ae7159ad5d8ecc59214a05860420774",
  "source_text_sha256": "d6073ffa1c6818ad8b7468d6c0f4f46c2ae7159ad5d8ecc59214a05860420774"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497874](../00497/00497874.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c580b0](../00c58/00c580b0.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5aed0](../00c5a/00c5aed0.md)
- [00c5b010](../00c5b/00c5b010.md)
- [00c5b150](../00c5b/00c5b150.md)
- [00c5dc90](../00c5d/00c5dc90.md)
- [00c5dcd0](../00c5d/00c5dcd0.md)
- [00c5dda0](../00c5d/00c5dda0.md)
- [00c5de00](../00c5d/00c5de00.md)

## 関連文字列（未確認候補）

~~~text
"Empty email or password are not allowed."
~~~

## 疑似コード / UTF-8 3683 bytes

~~~c

void _ZN8firebase4auth4Auth30CreateUserWithEmailAndPasswordEPKcS3_
               (undefined8 param_1,long *param_2,char *param_3,char *param_4)

{
  long lVar1;
  long lVar2;
  undefined *puVar3;
  size_t sVar4;
  long *plVar5;
  undefined8 uVar6;
  undefined8 uVar7;
  undefined8 uVar8;
  ulong uVar9;
  long lVar10;
  long lVar11;
  undefined4 uVar12;
  undefined8 *puVar13;
  undefined1 auStack_90 [16];
  undefined1 auStack_80 [16];
  undefined1 auStack_70 [16];
  undefined1 auStack_60 [8];
  long local_58;
  
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
  lVar1 = *param_2 + 0x10;
  _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEi
            (auStack_70,lVar1,7);
  if ((((param_3 == (char *)0x0) || (sVar4 = strlen(param_3), param_4 == (char *)0x0)) ||
      (sVar4 == 0)) || (sVar4 = strlen(param_4), sVar4 == 0)) {
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_80,auStack_70);
    uVar12 = 0x25;
    if (param_3 != (char *)0x0) {
      sVar4 = strlen(param_3);
      uVar12 = 0x25;
      if (sVar4 != 0) {
        uVar12 = 0x26;
      }
    }
    _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth10AuthResultEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS7_iS9_RKT0_
              (lVar1,auStack_80,uVar12,"Empty email or password are not allowed.",auStack_60);
    _ZN8firebase12FutureHandleD2Ev(auStack_80);
    _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,lVar1,auStack_70);
  }
  else {
    plVar5 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)*param_2);
    uVar6 = (**(code **)(*plVar5 + 0x538))(plVar5,param_3);
    uVar7 = (**(code **)(*plVar5 + 0x538))(plVar5,param_4);
    uVar8 = FUN_00497874(plVar5,*(undefined8 *)(*param_2 + 0x1f8),DAT_011268b8,uVar6,uVar7);
    (**(code **)(*plVar5 + 0xb8))(plVar5,uVar6);
    (**(code **)(*plVar5 + 0xb8))(plVar5,uVar7);
    uVar9 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                      (plVar5,lVar1,auStack_70);
    if ((uVar9 & 1) == 0) {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_90,auStack_70);
      puVar13 = (undefined8 *)*param_2;
      uVar6 = _ZNK8firebase3App9GetJNIEnvEv(*puVar13);
      lVar10 = _Znwm(0x20);
      _ZN8firebase12FutureHandleC1ERKS0_(lVar10,auStack_90);
      puVar3 = 
      PTR__ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv_00c9baf0
      ;
      *(undefined8 **)(lVar10 + 0x10) = puVar13;
      *(undefined **)(lVar10 + 0x18) = puVar3;
      if ((*(byte *)(puVar13 + 0x28) & 1) == 0) {
        lVar11 = (long)puVar13 + 0x141;
      }
      else {
        lVar11 = puVar13[0x2a];
      }
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (uVar6,uVar8,
                 PTR__ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9bad0
                 ,lVar10,lVar11);
      _ZN8firebase12FutureHandleD2Ev(auStack_90);
      (**(code **)(*plVar5 + 0xb8))(plVar5,uVar8);
    }
    _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,lVar1,auStack_70);
  }
  _ZN8firebase12FutureHandleD2Ev(auStack_70);
  if (*(long *)(lVar2 + 0x28) != local_58) {
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00bcf1e8 to 00ccf1ef has its CatchHandler @ 00bcf1f0 */
    __stack_chk_fail();
  }
  return;
}

~~~
