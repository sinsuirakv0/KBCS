# 00bdfddc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bdfddc",
  "name": "_ZN8firebase4auth4User27UpdatePhoneNumberCredentialERKNS0_19PhoneAuthCredentialE",
  "size": 492,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "07ca7934dfd2af7da302140af6ae02e7f0ca8c33320610869651fa37bd7e441e",
  "source_text_sha256": "07ca7934dfd2af7da302140af6ae02e7f0ca8c33320610869651fa37bd7e441e"
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
- [00c5d7e0](../00c5d/00c5d7e0.md)
- [00c5d810](../00c5d/00c5d810.md)
- [00c5d8f0](../00c5d/00c5d8f0.md)
- [00c5d950](../00c5d/00c5d950.md)
- [00c5da10](../00c5d/00c5da10.md)

## 関連文字列（未確認候補）

~~~text
"Credential is not a phone credential."
~~~

## 疑似コード / UTF-8 4190 bytes

~~~c

void _ZN8firebase4auth4User27UpdatePhoneNumberCredentialERKNS0_19PhoneAuthCredentialE
               (long param_1,long param_2,undefined8 *param_3)

{
  long lVar1;
  undefined *puVar2;
  char cVar3;
  long *plVar4;
  undefined8 uVar5;
  ulong uVar6;
  long lVar7;
  long lVar8;
  long lVar9;
  undefined8 uVar10;
  undefined8 *puVar11;
  undefined1 auStack_90 [16];
  undefined1 auStack_80 [16];
  undefined1 auStack_70 [16];
  undefined1 auStack_60 [8];
  long local_58;
  
                    /* try { // try from 00bdfdf0 to 00cdfdff has its CatchHandler @ 00be01e4 */
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  lVar9 = *(long *)(param_2 + 0x98);
  if ((lVar9 == 0) || (*(long *)(lVar9 + 0x200) == 0)) {
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
                    /* try { // try from 00bdfefc to 00cdff07 has its CatchHandler @ 00be02e8 */
    *(undefined8 *)(param_1 + 0x28) = 0;
                    /* try { // try from 00bdff08 to 00cdff3b has its CatchHandler @ 00be02f8 */
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    lVar9 = lVar9 + 0x10;
    _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth4UserEEENS_16SafeFutureHandleIT_EEi
              (auStack_70,lVar9,0x16);
    plVar4 = (long *)_ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
    uVar10 = *param_3;
    uVar5 = _ZN8firebase4auth15phonecredential8GetClassEv();
    cVar3 = (**(code **)(*plVar4 + 0x100))(plVar4,uVar10,uVar5);
    if (cVar3 == '\0') {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_90,auStack_70);
      _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth4UserEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS7_iS9_RKT0_
                (lVar9,auStack_90,4,"Credential is not a phone credential.",auStack_60);
      _ZN8firebase12FutureHandleD2Ev(auStack_90);
    }
    else {
                    /* try { // try from 00bdfe74 to 00cdfe77 has its CatchHandler @ 00be0358 */
      uVar5 = FUN_004977f4(plVar4,*(undefined8 *)(*(long *)(param_2 + 0x98) + 0x200),DAT_01126970,
                           uVar10);
      uVar6 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_4UserEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                        (plVar4,lVar9,auStack_70);
      if ((uVar6 & 1) == 0) {
                    /* try { // try from 00bdfea8 to 00cdfeaf has its CatchHandler @ 00be0324 */
        _ZN8firebase12FutureHandleC1ERKS0_(auStack_80,auStack_70);
        puVar11 = *(undefined8 **)(param_2 + 0x98);
                    /* try { // try from 00bdfeb0 to 00cdfefb has its CatchHandler @ 00bdf01c */
        uVar10 = _ZNK8firebase3App9GetJNIEnvEv(*puVar11);
        lVar7 = _Znwm(0x20);
        _ZN8firebase12FutureHandleC1ERKS0_(lVar7,auStack_80);
        puVar2 = 
        PTR__ZN8firebase4auth22ReadUserFromAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_4UserEEEbPv_00c9b628
        ;
        *(undefined8 **)(lVar7 + 0x10) = puVar11;
        *(undefined **)(lVar7 + 0x18) = puVar2;
        if ((*(byte *)(puVar11 + 0x28) & 1) == 0) {
          lVar8 = (long)puVar11 + 0x141;
        }
        else {
          lVar8 = puVar11[0x2a];
        }
        _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                  (uVar10,uVar5,
                   PTR__ZN8firebase4auth14FutureCallbackINS0_4UserEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9b610
                   ,lVar7,lVar8);
        _ZN8firebase12FutureHandleD2Ev(auStack_80);
                    /* try { // try from 00bdff6c to 00cdff73 has its CatchHandler @ 00be02b4 */
        (**(code **)(*plVar4 + 0xb8))(plVar4,uVar5);
      }
    }
    _ZN8firebase6FutureINS_4auth4UserEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,lVar9,auStack_70);
                    /* try { // try from 00bdff90 to 00cdffdb has its CatchHandler @ 00be0358 */
    _ZN8firebase12FutureHandleD2Ev(auStack_70);
  }
  if (*(long *)(lVar1 + 0x28) == local_58) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
