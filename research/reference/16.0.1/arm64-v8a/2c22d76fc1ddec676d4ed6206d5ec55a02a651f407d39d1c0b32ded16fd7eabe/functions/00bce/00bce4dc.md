# 00bce4dc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bce4dc",
  "name": "_ZN8firebase4auth4Auth20SignInWithCredentialERKNS0_10CredentialE",
  "size": 420,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "be3f631f9ff131c5fe18efe7a318577dbc351788b4f4163830a29c6090ab0951",
  "source_text_sha256": "be3f631f9ff131c5fe18efe7a318577dbc351788b4f4163830a29c6090ab0951"
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
- [00c5af40](../00c5a/00c5af40.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5dbe0](../00c5d/00c5dbe0.md)
- [00c5dc10](../00c5d/00c5dc10.md)
- [00c5dcf0](../00c5d/00c5dcf0.md)
- [00c5dd50](../00c5d/00c5dd50.md)

## 疑似コード / UTF-8 2921 bytes

~~~c

void _ZN8firebase4auth4Auth20SignInWithCredentialERKNS0_10CredentialE
               (undefined8 param_1,long *param_2,undefined8 *param_3)

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
  undefined1 auStack_90 [16];
  undefined1 auStack_80 [16];
  undefined1 auStack_70 [16];
  undefined1 auStack_60 [8];
  long local_58;
  
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
  lVar1 = *param_2 + 0x10;
  _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth4UserEEENS_16SafeFutureHandleIT_EEi
            (auStack_70,lVar1,2);
  plVar4 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)*param_2);
  if (*(int *)(param_3 + 1) == 0) {
    uVar5 = FUN_00497834(plVar4,*(undefined8 *)(*param_2 + 0x1f8),DAT_011267a0,*param_3);
    uVar6 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_4UserEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                      (plVar4,lVar1,auStack_70);
    if ((uVar6 & 1) == 0) {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_90,auStack_70);
      puVar10 = (undefined8 *)*param_2;
      uVar7 = _ZNK8firebase3App9GetJNIEnvEv(*puVar10);
      lVar8 = _Znwm(0x20);
      _ZN8firebase12FutureHandleC1ERKS0_(lVar8,auStack_90);
      puVar3 = 
      PTR__ZN8firebase4auth22ReadUserFromAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_4UserEEEbPv_00c9ba28
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
                 PTR__ZN8firebase4auth14FutureCallbackINS0_4UserEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9ba10
                 ,lVar8,lVar9);
      _ZN8firebase12FutureHandleD2Ev(auStack_90);
      (**(code **)(*plVar4 + 0xb8))(plVar4,uVar5);
    }
  }
  else {
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_80,auStack_70);
    lVar8 = (long)param_3 + 0x11;
    if ((*(byte *)(param_3 + 2) & 1) != 0) {
      lVar8 = param_3[4];
    }
    _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth4UserEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS7_iS9_RKT0_
              (lVar1,auStack_80,*(undefined4 *)(param_3 + 1),lVar8,auStack_60);
    _ZN8firebase12FutureHandleD2Ev(auStack_80);
  }
  _ZN8firebase6FutureINS_4auth4UserEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
            (param_1,lVar1,auStack_70);
  _ZN8firebase12FutureHandleD2Ev(auStack_70);
  if (*(long *)(lVar2 + 0x28) == local_58) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
