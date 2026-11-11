# 00bcf6fc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bcf6fc",
  "name": "_ZN8firebase4auth29CheckAndCompleteFutureOnErrorIvEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2cb774b8b29fceab434bea459de44f0db3f80fe56a6b880b8211052d7d829a7b",
  "source_text_sha256": "2cb774b8b29fceab434bea459de44f0db3f80fe56a6b880b8211052d7d829a7b"
}
~~~

## 呼び出し元

- [00c5dd00](../00c5d/00c5dd00.md)

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c5aa90](../00c5a/00c5aa90.md)
- [00c5ada0](../00c5a/00c5ada0.md)
- [00c5ae00](../00c5a/00c5ae00.md)
- [00c5dd10](../00c5d/00c5dd10.md)

## 疑似コード / UTF-8 2444 bytes

~~~c

undefined8
_ZN8firebase4auth29CheckAndCompleteFutureOnErrorIvEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
          (undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  void *pvVar1;
  long lVar2;
  int iVar3;
  undefined8 uVar4;
  undefined1 auStack_68 [16];
  ulong local_58;
  undefined8 local_50;
  void *local_48;
  undefined1 auStack_40 [8];
  long local_38;
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  local_50 = 0;
  local_48 = (void *)0x0;
  local_58 = 0;
  iVar3 = _ZN8firebase4auth30CheckAndClearJniAuthExceptionsEP7_JNIEnvPNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE
                    (param_1,&local_58);
  if (iVar3 == 0) {
    uVar4 = 0;
  }
  else {
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_68,param_3);
    pvVar1 = (void *)((ulong)&local_58 | 1);
    if ((local_58 & 1) != 0) {
      pvVar1 = local_48;
    }
                    /* try { // try from 00bcf770 to 00ccf77b has its CatchHandler @ 00bcf7c8 */
    _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
              (param_2,auStack_68,iVar3,pvVar1,auStack_40);
    _ZN8firebase12FutureHandleD2Ev(auStack_68);
                    /* catch() { ... } // from try @ 00bcf5e8 with catch @ 00bcf77c
                       try { // try from 00bcf77c to 00ccf7f7 has its CatchHandler @ 00bcf4f4 */
    uVar4 = 1;
                    /* catch() { ... } // from try @ 00bcf5a4 with catch @ 00bcf780 */
                    /* catch() { ... } // from try @ 00bcf558 with catch @ 00bcf784 */
  }
  if ((local_58 & 1) != 0) {
    _ZdlPv(local_48);
  }
                    /* catch() { ... } // from try @ 00bcf690 with catch @ 00bcf798 */
  if (*(long *)(lVar2 + 0x28) == local_38) {
                    /* catch() { ... } // from try @ 00bcf6c8 with catch @ 00bcf7a0 */
    return uVar4;
  }
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00bcf524 with catch @ 00bcf7c8
                       catch() { ... } // from try @ 00bcf568 with catch @ 00bcf7c8
                       catch() { ... } // from try @ 00bcf5b4 with catch @ 00bcf7c8
                       catch() { ... } // from try @ 00bcf64c with catch @ 00bcf7c8
                       catch() { ... } // from try @ 00bcf770 with catch @ 00bcf7c8 */
  __stack_chk_fail();
}

~~~
