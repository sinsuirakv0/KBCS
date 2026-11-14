# 00bddce8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bddce8",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth10AuthResultEZNS2_35FederatedAuthProviderFutureCallbackIS3_EEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPvEUlSD_E_EEvRKNS_12FutureHandleEiSC_RKT0_",
  "size": 312,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "536d0a23aba0318ada7a7ed8392598ed1a6c1b4fd4ef233e4bca874545b204aa",
  "source_text_sha256": "536d0a23aba0318ada7a7ed8392598ed1a6c1b4fd4ef233e4bca874545b204aa"
}
~~~

## 呼び出し元

- [00c5ee60](../00c5e/00c5ee60.md)

## 呼び出し先

- [00c5baa0](../00c5b/00c5baa0.md)
- [00c5bab0](../00c5b/00c5bab0.md)
- [00c5bed0](../00c5b/00c5bed0.md)
- [00c5bef0](../00c5b/00c5bef0.md)
- [00c5bf00](../00c5b/00c5bf00.md)
- [00c5bf10](../00c5b/00c5bf10.md)
- [00c5bf20](../00c5b/00c5bf20.md)
- [00c5bf30](../00c5b/00c5bf30.md)
- [00c5c0a0](../00c5c/00c5c0a0.md)
- [00c5c110](../00c5c/00c5c110.md)

## 関連文字列（未確認候補）

~~~text
"GetFutureStatus(handle) == kFutureStatusPending"
~~~

## 疑似コード / UTF-8 2368 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth10AuthResultEZNS2_35FederatedAuthProviderFutureCallbackIS3_EEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPvEUlSD_E_EEvRKNS_12FutureHandleEiSC_RKT0_
               (long *param_1,undefined8 *param_2,undefined4 param_3,undefined8 param_4,
               undefined8 *param_5)

{
  int iVar1;
  long lVar2;
  undefined8 uVar3;
  ulong uVar4;
  code *pcVar5;
  
                    /* try { // try from 00bddcf8 to 00cddd03 has its CatchHandler @ 00bdfc3c */
                    /* try { // try from 00bddd04 to 00cddd13 has its CatchHandler @ 00bdfc34 */
                    /* try { // try from 00bddd14 to 00cddd1f has its CatchHandler @ 00bdfc30 */
  _ZN8firebase5Mutex7AcquireEv(param_1 + 1);
                    /* try { // try from 00bddd20 to 00cddd37 has its CatchHandler @ 00bdfc2c */
  lVar2 = _ZN8firebase26ReferenceCountedFutureImpl17BackingFromHandleEm(param_1,*param_2);
  if (lVar2 == 0) {
    _ZN8firebase5Mutex7ReleaseEv(param_1 + 1);
    return;
  }
                    /* try { // try from 00bddd38 to 00cde753 has its CatchHandler @ 00bd7fb0 */
  iVar1 = (**(code **)(*param_1 + 0x20))(param_1,param_2);
  if (iVar1 != 1) {
    _ZN8firebase9LogAssertEPKcz("GetFutureStatus(handle) == kFutureStatusPending");
  }
  _ZN8firebase26ReferenceCountedFutureImpl15SetBackingErrorEPNS_17FutureBackingDataEiPKc
            (param_1,lVar2,param_3,param_4);
  uVar3 = _ZN8firebase26ReferenceCountedFutureImpl11BackingDataEPNS_17FutureBackingDataE
                    (param_1,lVar2);
  pcVar5 = *(code **)(param_5[2] + 0x18);
  if (pcVar5 != (code *)0x0) {
    (*pcVar5)(*param_5,param_5[2],*(undefined1 *)(param_5 + 1),uVar3);
  }
  _ZN8firebase26ReferenceCountedFutureImpl14CompleteHandleERKNS_12FutureHandleE(param_1,param_2);
  _ZN8firebase26ReferenceCountedFutureImpl13CompleteProxyEPNS_17FutureBackingDataE(param_1,lVar2);
  _ZN8firebase26ReferenceCountedFutureImpl27ReleaseMutexAndRunCallbacksERKNS_12FutureHandleE
            (param_1,param_2);
  uVar4 = _ZNK8firebase26ReferenceCountedFutureImpl11is_orphanedEv(param_1);
  if ((uVar4 & 1) != 0) {
                    /* WARNING: Could not recover jumptable at 0x00bddde8. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*param_1 + 8))(param_1);
    return;
  }
  return;
}

~~~
