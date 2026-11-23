# 00bcdfb0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5eab0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5eab0.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0067.md#compare-ea9f495f397cdf341b7ce001427dff43)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcdfb0",
  "name": "_ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4c8e2bc1df85ab6b767abf7249144127d2c4c1fe92afcc72a6bee778f1704d97",
  "source_text_sha256": "4c8e2bc1df85ab6b767abf7249144127d2c4c1fe92afcc72a6bee778f1704d97"
}
~~~

## 呼び出し元

- [00c5d8d0](../00c5d/00c5d8d0.md)

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5a690](../00c5a/00c5a690.md)
- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5d7c0](../00c5d/00c5d7c0.md)
- [00c5d910](../00c5d/00c5d910.md)

## 疑似コード / UTF-8 1819 bytes

~~~c

undefined8
_ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
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
  
                    /* try { // try from 00bcdfb8 to 00ccdfd3 has its CatchHandler @ 00bce694 */
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
                    /* try { // try from 00bcdfd4 to 00cce02f has its CatchHandler @ 00bcc3d4 */
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
    _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth10AuthResultEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS7_iS9_RKT0_
              (param_2,auStack_68,iVar3,pvVar1,auStack_40);
    _ZN8firebase12FutureHandleD2Ev(auStack_68);
                    /* try { // try from 00bce030 to 00cce03f has its CatchHandler @ 00bce744 */
    uVar4 = 1;
  }
  if ((local_58 & 1) != 0) {
                    /* try { // try from 00bce040 to 00cce95f has its CatchHandler @ 00bcc3d4 */
    _ZdlPv(local_48);
  }
  if (*(long *)(lVar2 + 0x28) == local_38) {
    return uVar4;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
