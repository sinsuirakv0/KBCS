# 00bbba0c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bbba0c",
  "name": "_ZN8firebase9messaging11UnsubscribeEPKc",
  "size": 552,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "92eb66a55f1eae08cd0d4e7f6c05219a45cd8aef6613b365cc53bba28558c869",
  "source_text_sha256": "92eb66a55f1eae08cd0d4e7f6c05219a45cd8aef6613b365cc53bba28558c869"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bbbcdc](../00bbb/00bbbcdc.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5aad0](../00c5a/00c5aad0.md)
- [00c5aae0](../00c5a/00c5aae0.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5acb0](../00c5a/00c5acb0.md)
- [00c5ad40](../00c5a/00c5ad40.md)
- [00c5ad70](../00c5a/00c5ad70.md)
- [00c5ae70](../00c5a/00c5ae70.md)
- [00c5aea0](../00c5a/00c5aea0.md)
- [00c5aed0](../00c5a/00c5aed0.md)
- [00c5af10](../00c5a/00c5af10.md)
- [00c5b0d0](../00c5b/00c5b0d0.md)
- [00c5b690](../00c5b/00c5b690.md)
- [00c5bd30](../00c5b/00c5bd30.md)
- [00c5d340](../00c5d/00c5d340.md)
- [00c5d6a0](../00c5d/00c5d6a0.md)

## 関連文字列（未確認候補）

~~~text
"Cannot update subscription for unknown reason."
"Cannot update subscription when SetTokenRegistrationOnInitEnabled is set to false."
"Messaging not initialized."
"internal::IsInitialized()"
~~~

## 疑似コード / UTF-8 4041 bytes

~~~c

void _ZN8firebase9messaging11UnsubscribeEPKc(long param_1,undefined8 param_2)

{
  ulong *puVar1;
  long lVar2;
  undefined8 uVar3;
  long lVar4;
  undefined8 uVar5;
  undefined1 *puVar6;
  undefined1 auStack_b0 [16];
  ulong local_a0;
  ulong uStack_98;
  void *local_90;
  undefined1 auStack_88 [16];
  undefined1 auStack_78 [16];
  undefined1 auStack_68 [16];
  long local_58;
  
  uVar3 = DAT_01126470;
  puVar6 = auStack_b0;
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
  if (DAT_01126460 == 0) {
    _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
    _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
                    /* try { // try from 00bbbacc to 00cbbaf3 has its CatchHandler @ 00bbc804 */
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
    goto LAB_00bbbbdc;
  }
  _ZN8firebase5Mutex7AcquireEv(DAT_01126470);
  uVar5 = _ZN8firebase9messaging10FutureData3GetEv();
                    /* try { // try from 00bbba64 to 00cbba6f has its CatchHandler @ 00bbc7dc */
  _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E(&local_a0,uVar5,1,0,0);
  _ZN8firebase12FutureHandleC1ERKS0_(auStack_68,&local_a0);
  _ZN8firebase12FutureHandleD2Ev(&local_a0);
  lVar4 = DAT_01126480;
  if (DAT_01126508 == '\x01') {
    FUN_00bbbcdc(param_2,auStack_68);
  }
  else {
    if (DAT_01126500 == 2) {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,auStack_68);
      _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
                (uVar5,auStack_78,3,
                 "Cannot update subscription when SetTokenRegistrationOnInitEnabled is set to false."
                 ,&local_a0);
      puVar6 = auStack_78;
    }
    else {
      if (DAT_01126480 != 0) {
                    /* try { // try from 00bbbb34 to 00cbbb3f has its CatchHandler @ 00bbc7d8 */
        _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc
                  (&local_a0,param_2);
        _ZN8firebase12FutureHandleC1ERKS0_(auStack_88,auStack_68);
        puVar1 = *(ulong **)(lVar4 + 8);
        if (puVar1 < *(ulong **)(lVar4 + 0x10)) {
          puVar1[2] = (ulong)local_90;
          puVar1[1] = uStack_98;
          *puVar1 = local_a0;
          uStack_98 = 0;
          local_90 = (void *)0x0;
          local_a0 = 0;
                    /* try { // try from 00bbbb7c to 00cbbba3 has its CatchHandler @ 00bbc800 */
          _ZN8firebase12FutureHandleC1EOS0_(puVar1 + 3,auStack_88);
          *(ulong **)(lVar4 + 8) = puVar1 + 5;
        }
        else {
          _ZNSt6__ndk16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase16SafeFutureHandleIvEEEENS5_ISB_EEE21__push_back_slow_pathISB_EEvOT_
                    (lVar4,&local_a0);
        }
        _ZN8firebase12FutureHandleD2Ev(auStack_88);
                    /* try { // try from 00bbbc20 to 00cbbc47 has its CatchHandler @ 00bbc7fc */
        if ((local_a0 & 1) != 0) {
          _ZdlPv(local_90);
        }
        goto LAB_00bbbbbc;
      }
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_b0,auStack_68);
      _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
                (uVar5,auStack_b0,4,"Cannot update subscription for unknown reason.",&local_a0);
    }
    _ZN8firebase12FutureHandleD2Ev(puVar6);
  }
LAB_00bbbbbc:
  _ZN8firebase6FutureIvEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
            (param_1,uVar5,auStack_68);
  _ZN8firebase12FutureHandleD2Ev(auStack_68);
  _ZN8firebase5Mutex7ReleaseEv(uVar3);
LAB_00bbbbdc:
                    /* try { // try from 00bbbbe4 to 00cbbbef has its CatchHandler @ 00bbc7d4 */
  if (*(long *)(lVar2 + 0x28) == local_58) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
