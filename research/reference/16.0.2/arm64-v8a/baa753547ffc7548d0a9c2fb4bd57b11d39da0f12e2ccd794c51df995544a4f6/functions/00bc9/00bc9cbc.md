# 00bc9cbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bc9cbc",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_13remote_config10ConfigInfoEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS7_iS9_RKT0_",
  "size": 264,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1c577f6794ae523662fa5a756c9a2110699df70c7a864ff7e5966410a343150c",
  "source_text_sha256": "1c577f6794ae523662fa5a756c9a2110699df70c7a864ff7e5966410a343150c"
}
~~~

## 呼び出し元

- [00c5d9c0](../00c5d/00c5d9c0.md)

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

## 疑似コード / UTF-8 1873 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_13remote_config10ConfigInfoEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS7_iS9_RKT0_
               (long *param_1,undefined8 *param_2,undefined4 param_3,undefined8 param_4)

{
  int iVar1;
  long lVar2;
  ulong uVar3;
  
  _ZN8firebase5Mutex7AcquireEv(param_1 + 1);
  lVar2 = _ZN8firebase26ReferenceCountedFutureImpl17BackingFromHandleEm(param_1,*param_2);
  if (lVar2 == 0) {
    _ZN8firebase5Mutex7ReleaseEv(param_1 + 1);
    return;
  }
  iVar1 = (**(code **)(*param_1 + 0x20))(param_1,param_2);
  if (iVar1 != 1) {
    _ZN8firebase9LogAssertEPKcz("GetFutureStatus(handle) == kFutureStatusPending");
  }
                    /* try { // try from 00bc9d38 to 00cc9d4f has its CatchHandler @ 00bc9f3c */
  _ZN8firebase26ReferenceCountedFutureImpl15SetBackingErrorEPNS_17FutureBackingDataEiPKc
            (param_1,lVar2,param_3,param_4);
  _ZN8firebase26ReferenceCountedFutureImpl11BackingDataEPNS_17FutureBackingDataE(param_1,lVar2);
  _ZN8firebase26ReferenceCountedFutureImpl14CompleteHandleERKNS_12FutureHandleE(param_1,param_2);
                    /* try { // try from 00bc9d58 to 00cc9d87 has its CatchHandler @ 00bc9f98 */
  _ZN8firebase26ReferenceCountedFutureImpl13CompleteProxyEPNS_17FutureBackingDataE(param_1,lVar2);
  _ZN8firebase26ReferenceCountedFutureImpl27ReleaseMutexAndRunCallbacksERKNS_12FutureHandleE
            (param_1,param_2);
  uVar3 = _ZNK8firebase26ReferenceCountedFutureImpl11is_orphanedEv(param_1);
  if ((uVar3 & 1) != 0) {
                    /* try { // try from 00bc9d88 to 00cc9e07 has its CatchHandler @ 00bc9b5c */
                    /* WARNING: Could not recover jumptable at 0x00bc9d94. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*param_1 + 8))(param_1);
    return;
  }
  return;
}

~~~
