# 00bcf4fc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bcf4fc",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth4Auth20FetchProvidersResultEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS8_iSA_RKT0_",
  "size": 264,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ed06c0b2f0fc7bce82e0fbde729c09e596e53e09e61a19830dd36d3463386268",
  "source_text_sha256": "ed06c0b2f0fc7bce82e0fbde729c09e596e53e09e61a19830dd36d3463386268"
}
~~~

## 呼び出し元

- [00c5d7d0](../00c5d/00c5d7d0.md)

## 呼び出し先

- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)
- [00c5aa30](../00c5a/00c5aa30.md)
- [00c5aa50](../00c5a/00c5aa50.md)
- [00c5aa60](../00c5a/00c5aa60.md)
- [00c5aa70](../00c5a/00c5aa70.md)
- [00c5aa80](../00c5a/00c5aa80.md)
- [00c5aa90](../00c5a/00c5aa90.md)
- [00c5ac00](../00c5a/00c5ac00.md)
- [00c5ac70](../00c5a/00c5ac70.md)

## 関連文字列（未確認候補）

~~~text
"GetFutureStatus(handle) == kFutureStatusPending"
~~~

## 疑似コード / UTF-8 2636 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth4Auth20FetchProvidersResultEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS8_iSA_RKT0_
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
                    /* try { // try from 00bcf574 to 00ccf57f has its CatchHandler @ 00bcf5cc */
  _ZN8firebase26ReferenceCountedFutureImpl15SetBackingErrorEPNS_17FutureBackingDataEiPKc
            (param_1,lVar2,param_3,param_4);
                    /* catch() { ... } // from try @ 00bcf3ec with catch @ 00bcf580
                       try { // try from 00bcf580 to 00ccf5fb has its CatchHandler @ 00bcf2f8 */
                    /* catch() { ... } // from try @ 00bcf3a8 with catch @ 00bcf584 */
  _ZN8firebase26ReferenceCountedFutureImpl11BackingDataEPNS_17FutureBackingDataE(param_1,lVar2);
                    /* catch() { ... } // from try @ 00bcf35c with catch @ 00bcf588 */
  _ZN8firebase26ReferenceCountedFutureImpl14CompleteHandleERKNS_12FutureHandleE(param_1,param_2);
                    /* catch() { ... } // from try @ 00bcf494 with catch @ 00bcf59c */
  _ZN8firebase26ReferenceCountedFutureImpl13CompleteProxyEPNS_17FutureBackingDataE(param_1,lVar2);
                    /* catch() { ... } // from try @ 00bcf4cc with catch @ 00bcf5a4 */
  _ZN8firebase26ReferenceCountedFutureImpl27ReleaseMutexAndRunCallbacksERKNS_12FutureHandleE
            (param_1,param_2);
  uVar3 = _ZNK8firebase26ReferenceCountedFutureImpl11is_orphanedEv(param_1);
  if ((uVar3 & 1) != 0) {
                    /* catch() { ... } // from try @ 00bcf328 with catch @ 00bcf5cc
                       catch() { ... } // from try @ 00bcf36c with catch @ 00bcf5cc
                       catch() { ... } // from try @ 00bcf3b8 with catch @ 00bcf5cc
                       catch() { ... } // from try @ 00bcf450 with catch @ 00bcf5cc
                       catch() { ... } // from try @ 00bcf574 with catch @ 00bcf5cc */
                    /* WARNING: Could not recover jumptable at 0x00bcf5d4. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*param_1 + 8))(param_1);
    return;
  }
  return;
}

~~~
