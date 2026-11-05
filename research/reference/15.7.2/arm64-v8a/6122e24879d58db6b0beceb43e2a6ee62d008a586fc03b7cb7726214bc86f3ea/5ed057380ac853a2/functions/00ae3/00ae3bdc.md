# 00ae3bdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00ae3bdc.md)

## 関数情報

~~~json
{
  "address": "00ae3bdc",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIiZNS0_26CompleteWithResultInternalIiEEvRKNS_12FutureHandleEiPKcRKT_EUlPiE_EEvS5_iS7_RKT0_",
  "size": 292,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d4e8e9555b05303c6de4c2983767d552b2662f3af24881834f3c06accce1974d",
  "source_text_sha256": "d4e8e9555b05303c6de4c2983767d552b2662f3af24881834f3c06accce1974d"
}
~~~
## 呼び出し元

- [00bdde10](../00bdd/00bdde10.md)

## 呼び出し先

- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)
- [00bddeb0](../00bdd/00bddeb0.md)
- [00bdded0](../00bdd/00bdded0.md)
- [00bddee0](../00bdd/00bddee0.md)
- [00bddef0](../00bdd/00bddef0.md)
- [00bddf00](../00bdd/00bddf00.md)
- [00bddf10](../00bdd/00bddf10.md)
- [00bde080](../00bde/00bde080.md)
- [00bde0f0](../00bde/00bde0f0.md)

## 関連文字列（未確認候補）

~~~text
"GetFutureStatus(handle) == kFutureStatusPending"
~~~
## 疑似コード 1/1 / UTF-8 2249 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIiZNS0_26CompleteWithResultInternalIiEEvRKNS_12FutureHandleEiPKcRKT_EUlPiE_EEvS5_iS7_RKT0_
               (long *param_1,undefined8 *param_2,undefined4 param_3,undefined8 param_4,
               undefined4 *param_5)

{
  int iVar1;
  long lVar2;
  undefined4 *puVar3;
  ulong uVar4;
  
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
                    /* try { // try from 00ae3c58 to 00be3c9f has its CatchHandler @ 00ae3c58
                       catch() { ... } // from try @ 00ae3c58 with catch @ 00ae3c58
                       catch() { ... } // from try @ 00ae3cac with catch @ 00ae3c58 */
  _ZN8firebase26ReferenceCountedFutureImpl15SetBackingErrorEPNS_17FutureBackingDataEiPKc
            (param_1,lVar2,param_3,param_4);
  puVar3 = (undefined4 *)
           _ZN8firebase26ReferenceCountedFutureImpl11BackingDataEPNS_17FutureBackingDataE
                     (param_1,lVar2);
  *puVar3 = *param_5;
  _ZN8firebase26ReferenceCountedFutureImpl14CompleteHandleERKNS_12FutureHandleE(param_1,param_2);
  _ZN8firebase26ReferenceCountedFutureImpl13CompleteProxyEPNS_17FutureBackingDataE(param_1,lVar2);
  _ZN8firebase26ReferenceCountedFutureImpl27ReleaseMutexAndRunCallbacksERKNS_12FutureHandleE
            (param_1,param_2);
                    /* try { // try from 00ae3ca0 to 00be3cab has its CatchHandler @ 00ae3cfc */
  uVar4 = _ZNK8firebase26ReferenceCountedFutureImpl11is_orphanedEv(param_1);
  if ((uVar4 & 1) != 0) {
                    /* try { // try from 00ae3cac to 00be3d4b has its CatchHandler @ 00ae3c58 */
                    /* WARNING: Could not recover jumptable at 0x00ae3cc8. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*param_1 + 8))(param_1);
    return;
  }
                    /* catch() { ... } // from try @ 00ae3ca0 with catch @ 00ae3cfc */
  return;
}

~~~
