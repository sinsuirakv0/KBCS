# 00bdf7ec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bdf7ec",
  "name": "_ZN8firebase4auth4User14UpdatePasswordEPKc",
  "size": 460,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8a5ec702ef1c31e7882254916b93b99160bfde5633922650f3f9c7b094ead7fa",
  "source_text_sha256": "8a5ec702ef1c31e7882254916b93b99160bfde5633922650f3f9c7b094ead7fa"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497874](../00497/00497874.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5acb0](../00c5a/00c5acb0.md)
- [00c5ad40](../00c5a/00c5ad40.md)
- [00c5aea0](../00c5a/00c5aea0.md)
- [00c5aed0](../00c5a/00c5aed0.md)
- [00c5af10](../00c5a/00c5af10.md)
- [00c5b010](../00c5b/00c5b010.md)
- [00c5b150](../00c5b/00c5b150.md)
- [00c5ddd0](../00c5d/00c5ddd0.md)

## 疑似コード / UTF-8 3165 bytes

~~~c

void _ZN8firebase4auth4User14UpdatePasswordEPKc(long param_1,long param_2,undefined8 param_3)

{
  long lVar1;
  long *plVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  ulong uVar5;
  long lVar6;
  long lVar7;
  long lVar8;
  undefined8 *puVar9;
  undefined1 auStack_88 [16];
  undefined1 auStack_78 [16];
  undefined1 auStack_68 [16];
  long local_58;
  
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  lVar8 = *(long *)(param_2 + 0x98);
  if ((lVar8 == 0) || (*(long *)(lVar8 + 0x200) == 0)) {
                    /* try { // try from 00bdf91c to 00cdf96b has its CatchHandler @ 00be0864 */
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    lVar8 = lVar8 + 0x10;
    _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E(auStack_68,lVar8,0xb,0,0);
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,auStack_68);
                    /* try { // try from 00bdf858 to 00cdf86f has its CatchHandler @ 00be0840 */
    _ZN8firebase12FutureHandleD2Ev(auStack_68);
    plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
    uVar3 = (**(code **)(*plVar2 + 0x538))(plVar2,param_3);
                    /* try { // try from 00bdf880 to 00cdf893 has its CatchHandler @ 00be07a8 */
    uVar4 = FUN_00497874(plVar2,*(undefined8 *)(*(long *)(param_2 + 0x98) + 0x200),DAT_01126e50,
                         uVar3);
    (**(code **)(*plVar2 + 0xb8))(plVar2,uVar3);
    uVar5 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorIvEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                      (plVar2,lVar8,auStack_78);
    if ((uVar5 & 1) == 0) {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_88,auStack_78);
      puVar9 = *(undefined8 **)(param_2 + 0x98);
      uVar3 = _ZNK8firebase3App9GetJNIEnvEv(*puVar9);
      lVar6 = _Znwm(0x20);
      _ZN8firebase12FutureHandleC1ERKS0_(lVar6,auStack_88);
      *(undefined8 **)(lVar6 + 0x10) = puVar9;
      *(undefined8 *)(lVar6 + 0x18) = 0;
      if ((*(byte *)(puVar9 + 0x28) & 1) == 0) {
        lVar7 = (long)puVar9 + 0x141;
      }
      else {
        lVar7 = puVar9[0x2a];
      }
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (uVar3,uVar4,
                 PTR__ZN8firebase4auth14FutureCallbackIvEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9bae8
                 ,lVar6,lVar7);
      _ZN8firebase12FutureHandleD2Ev(auStack_88);
      (**(code **)(*plVar2 + 0xb8))(plVar2,uVar4);
    }
                    /* try { // try from 00bdf97c to 00cdf9a7 has its CatchHandler @ 00be07a0 */
    _ZN8firebase6FutureIvEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,lVar8,auStack_78);
    _ZN8firebase12FutureHandleD2Ev(auStack_78);
  }
  if (*(long *)(lVar1 + 0x28) == local_58) {
    return;
  }
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00bdf9b4 to 00cdf9e7 has its CatchHandler @ 00be058c */
  __stack_chk_fail();
}

~~~
