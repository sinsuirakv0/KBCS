# 00bcdca0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bcdca0",
  "name": "_ZN8firebase4auth4Auth21SignInWithCustomTokenEPKc",
  "size": 392,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "59e331db3b4be4963a2e5ef2716e24b50b42264189db1e3abdc433fc045c4a2b",
  "source_text_sha256": "59e331db3b4be4963a2e5ef2716e24b50b42264189db1e3abdc433fc045c4a2b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [004977f4](../00497/004977f4.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5a690](../00c5a/00c5a690.md)
- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5ab40](../00c5a/00c5ab40.md)
- [00c5ac80](../00c5a/00c5ac80.md)
- [00c5d800](../00c5d/00c5d800.md)
- [00c5d8d0](../00c5d/00c5d8d0.md)
- [00c5d930](../00c5d/00c5d930.md)

## 疑似コード / UTF-8 2899 bytes

~~~c

void _ZN8firebase4auth4Auth21SignInWithCustomTokenEPKc
               (undefined8 param_1,long *param_2,undefined8 param_3)

{
  long lVar1;
  long lVar2;
  undefined *puVar3;
  long *plVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  ulong uVar7;
  long lVar8;
  long lVar9;
  undefined8 *puVar10;
  undefined1 auStack_78 [16];
  undefined1 auStack_68 [16];
  long local_58;
  
                    /* try { // try from 00bcdcb8 to 00ccdd4b has its CatchHandler @ 00bcc3d4 */
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
  lVar1 = *param_2 + 0x10;
  _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEi
            (auStack_68,lVar1,1);
  plVar4 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)*param_2);
  uVar5 = (**(code **)(*plVar4 + 0x538))(plVar4,param_3);
  uVar6 = FUN_004977f4(plVar4,*(undefined8 *)(*param_2 + 0x1f8),DAT_01126398,uVar5);
  (**(code **)(*plVar4 + 0xb8))(plVar4,uVar5);
                    /* try { // try from 00bcdd4c to 00ccdd53 has its CatchHandler @ 00bce6b4 */
  uVar7 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                    (plVar4,lVar1,auStack_68);
  if ((uVar7 & 1) == 0) {
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,auStack_68);
    puVar10 = (undefined8 *)*param_2;
    uVar5 = _ZNK8firebase3App9GetJNIEnvEv(*puVar10);
    lVar8 = _Znwm(0x20);
                    /* try { // try from 00bcdd7c to 00ccdd93 has its CatchHandler @ 00bce6b0 */
    _ZN8firebase12FutureHandleC1ERKS0_(lVar8,auStack_78);
    puVar3 = 
    PTR__ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv_00c9b620
    ;
    *(undefined8 **)(lVar8 + 0x10) = puVar10;
    *(undefined **)(lVar8 + 0x18) = puVar3;
    if ((*(byte *)(puVar10 + 0x28) & 1) == 0) {
      lVar9 = (long)puVar10 + 0x141;
                    /* try { // try from 00bcdda4 to 00ccddc3 has its CatchHandler @ 00bce6ac */
    }
    else {
      lVar9 = puVar10[0x2a];
    }
    _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
              (uVar5,uVar6,
               PTR__ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9b600
               ,lVar8,lVar9);
                    /* try { // try from 00bcddc4 to 00ccde7b has its CatchHandler @ 00bcc3d4 */
    _ZN8firebase12FutureHandleD2Ev(auStack_78);
    (**(code **)(*plVar4 + 0xb8))(plVar4,uVar6);
  }
  _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
            (param_1,lVar1,auStack_68);
  _ZN8firebase12FutureHandleD2Ev(auStack_68);
  if (*(long *)(lVar2 + 0x28) == local_58) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
