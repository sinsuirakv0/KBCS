# 00bdccf4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bdccf4",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth10AuthResultEZNS2_35FederatedAuthProviderFutureCallbackIS3_EEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPvEUlSD_E_EEvRKNS_12FutureHandleEiSC_RKT0_",
  "size": 312,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9eea8b2d5dc9eb1c3fed70076b6fb6f3c672759deb326e3af00a70f2da2fdbdb",
  "source_text_sha256": "9eea8b2d5dc9eb1c3fed70076b6fb6f3c672759deb326e3af00a70f2da2fdbdb"
}
~~~

## 呼び出し元

- [00c5de90](../00c5d/00c5de90.md)

## 呼び出し先

- [00c5aad0](../00c5a/00c5aad0.md)
- [00c5aae0](../00c5a/00c5aae0.md)
- [00c5af00](../00c5a/00c5af00.md)
- [00c5af20](../00c5a/00c5af20.md)
- [00c5af30](../00c5a/00c5af30.md)
- [00c5af40](../00c5a/00c5af40.md)
- [00c5af50](../00c5a/00c5af50.md)
- [00c5af60](../00c5a/00c5af60.md)
- [00c5b0d0](../00c5b/00c5b0d0.md)
- [00c5b140](../00c5b/00c5b140.md)

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
  
                    /* try { // try from 00bdcd04 to 00cdcd0f has its CatchHandler @ 00bdec48 */
                    /* try { // try from 00bdcd10 to 00cdcd1f has its CatchHandler @ 00bdec40 */
                    /* try { // try from 00bdcd20 to 00cdcd2b has its CatchHandler @ 00bdec3c */
  _ZN8firebase5Mutex7AcquireEv(param_1 + 1);
                    /* try { // try from 00bdcd2c to 00cdcd43 has its CatchHandler @ 00bdec38 */
  lVar2 = _ZN8firebase26ReferenceCountedFutureImpl17BackingFromHandleEm(param_1,*param_2);
  if (lVar2 == 0) {
    _ZN8firebase5Mutex7ReleaseEv(param_1 + 1);
    return;
  }
                    /* try { // try from 00bdcd44 to 00cdd75f has its CatchHandler @ 00bd6fbc */
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
                    /* WARNING: Could not recover jumptable at 0x00bdcdf4. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*param_1 + 8))(param_1);
    return;
  }
  return;
}

~~~
