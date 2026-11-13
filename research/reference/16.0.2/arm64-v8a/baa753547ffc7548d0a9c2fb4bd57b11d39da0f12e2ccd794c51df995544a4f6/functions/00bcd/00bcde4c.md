# 00bcde4c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bcde4c",
  "name": "_ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_4Auth20FetchProvidersResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fea7e615e59ea2afc10979236807e2bc4df7e5dfd0e62c67fec0099e5dd597d8",
  "source_text_sha256": "fea7e615e59ea2afc10979236807e2bc4df7e5dfd0e62c67fec0099e5dd597d8"
}
~~~

## 呼び出し元

- [00c5ddb0](../00c5d/00c5ddb0.md)

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5aed0](../00c5a/00c5aed0.md)
- [00c5dca0](../00c5d/00c5dca0.md)
- [00c5dde0](../00c5d/00c5dde0.md)

## 疑似コード / UTF-8 1849 bytes

~~~c

undefined8
_ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_4Auth20FetchProvidersResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
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
                    /* try { // try from 00bcde68 to 00ccde6f has its CatchHandler @ 00bce950 */
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
                    /* try { // try from 00bcdea4 to 00ccdeab has its CatchHandler @ 00bce948 */
    pvVar1 = (void *)((ulong)&local_58 | 1);
    if ((local_58 & 1) != 0) {
      pvVar1 = local_48;
    }
    _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth4Auth20FetchProvidersResultEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS8_iSA_RKT0_
              (param_2,auStack_68,iVar3,pvVar1,auStack_40);
    _ZN8firebase12FutureHandleD2Ev(auStack_68);
    uVar4 = 1;
  }
  if ((local_58 & 1) != 0) {
                    /* try { // try from 00bcded8 to 00ccdef7 has its CatchHandler @ 00bce938 */
    _ZdlPv(local_48);
  }
  if (*(long *)(lVar2 + 0x28) == local_38) {
                    /* try { // try from 00bcdf04 to 00ccdf23 has its CatchHandler @ 00bce928 */
    return uVar4;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
