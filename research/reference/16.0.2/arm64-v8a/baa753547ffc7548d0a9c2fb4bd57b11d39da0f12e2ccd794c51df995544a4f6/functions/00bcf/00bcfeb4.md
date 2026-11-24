# 00bcfeb4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcfe18`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfe18.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0082.md#compare-839d045baf102f8e0824d55e5ea49299)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0094.md#compare-4e8c4b689c74f26cd1fc59d065f984d5)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcfeb4",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth10AuthResultEZNS2_14FutureCallbackIS3_EEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPvEUlSD_E_EEvRKNS_12FutureHandleEiSC_RKT0_",
  "size": 312,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2ecd746e30504d468b921b8c209009b5ef98a572891d21cfc735db997492c5c5",
  "source_text_sha256": "2ecd746e30504d468b921b8c209009b5ef98a572891d21cfc735db997492c5c5"
}
~~~

## 呼び出し元

- [00c5dc60](../00c5d/00c5dc60.md)

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

## 疑似コード / UTF-8 2250 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth10AuthResultEZNS2_14FutureCallbackIS3_EEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPvEUlSD_E_EEvRKNS_12FutureHandleEiSC_RKT0_
               (long *param_1,undefined8 *param_2,undefined4 param_3,undefined8 param_4,
               undefined8 *param_5)

{
  int iVar1;
  long lVar2;
  undefined8 uVar3;
  ulong uVar4;
  code *pcVar5;
  
  _ZN8firebase5Mutex7AcquireEv(param_1 + 1);
  lVar2 = _ZN8firebase26ReferenceCountedFutureImpl17BackingFromHandleEm(param_1,*param_2);
  if (lVar2 == 0) {
    _ZN8firebase5Mutex7ReleaseEv(param_1 + 1);
    return;
  }
                    /* try { // try from 00bcff10 to 00ccff1b has its CatchHandler @ 00bd03e0 */
  iVar1 = (**(code **)(*param_1 + 0x20))(param_1,param_2);
  if (iVar1 != 1) {
                    /* try { // try from 00bcff1c to 00ccff7b has its CatchHandler @ 00bcfd30 */
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
                    /* try { // try from 00bcff7c to 00ccff97 has its CatchHandler @ 00bd03e4 */
  _ZN8firebase26ReferenceCountedFutureImpl27ReleaseMutexAndRunCallbacksERKNS_12FutureHandleE
            (param_1,param_2);
  uVar4 = _ZNK8firebase26ReferenceCountedFutureImpl11is_orphanedEv(param_1);
  if ((uVar4 & 1) != 0) {
                    /* try { // try from 00bcff98 to 00ccffeb has its CatchHandler @ 00bcfd30 */
                    /* WARNING: Could not recover jumptable at 0x00bcffb4. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*param_1 + 8))(param_1);
    return;
  }
  return;
}

~~~
