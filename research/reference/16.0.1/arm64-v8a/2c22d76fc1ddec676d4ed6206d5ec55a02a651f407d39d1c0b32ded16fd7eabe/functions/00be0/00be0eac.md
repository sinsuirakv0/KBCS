# 00be0eac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00be0a84`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0a84.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/high-0010.md#compare-77ee09f4342f579bee4f16cd7932f328)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/high-0011.md#compare-fe52c7503df0e61eae27874c1fa07cf1)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00be0eac",
  "name": "_ZN8firebase4auth4User6DeleteEv",
  "size": 416,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "829407e523b711f403444e0f00d8b4a25f5d83e7c4f04e414ed5ad21b08568d1",
  "source_text_sha256": "829407e523b711f403444e0f00d8b4a25f5d83e7c4f04e414ed5ad21b08568d1"
}
~~~

## 呼び出し元

- [00c5aa80](../00c5a/00c5aa80.md)

## 呼び出し先

- [00497834](../00497/00497834.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c5aa90](../00c5a/00c5aa90.md)
- [00c5abe0](../00c5a/00c5abe0.md)
- [00c5ac70](../00c5a/00c5ac70.md)
- [00c5add0](../00c5a/00c5add0.md)
- [00c5ae00](../00c5a/00c5ae00.md)
- [00c5ae40](../00c5a/00c5ae40.md)
- [00c5af40](../00c5a/00c5af40.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5dd00](../00c5d/00c5dd00.md)

## 疑似コード / UTF-8 2904 bytes

~~~c

void _ZN8firebase4auth4User6DeleteEv(long param_1,long param_2)

{
  long lVar1;
  long *plVar2;
  undefined8 uVar3;
  ulong uVar4;
  undefined8 uVar5;
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
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    lVar8 = lVar8 + 0x10;
                    /* try { // try from 00be0ef0 to 00ce0efb has its CatchHandler @ 00be1120 */
    _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E(auStack_68,lVar8,0x18,0,0);
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,auStack_68);
    _ZN8firebase12FutureHandleD2Ev(auStack_68);
                    /* try { // try from 00be0f20 to 00ce0f2b has its CatchHandler @ 00be1110 */
    plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
                    /* try { // try from 00be0f2c to 00ce0f47 has its CatchHandler @ 00be1130 */
    uVar3 = FUN_00497834(plVar2,*(undefined8 *)(*(long *)(param_2 + 0x98) + 0x200),DAT_01126d90);
                    /* try { // try from 00be0f48 to 00ce11af has its CatchHandler @ 00be0c3c */
    uVar4 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorIvEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                      (plVar2,lVar8,auStack_78);
    if ((uVar4 & 1) == 0) {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_88,auStack_78);
      puVar9 = *(undefined8 **)(param_2 + 0x98);
      uVar5 = _ZNK8firebase3App9GetJNIEnvEv(*puVar9);
      lVar6 = _Znwm(0x20);
      _ZN8firebase12FutureHandleC1ERKS0_(lVar6,auStack_88);
      *(undefined8 **)(lVar6 + 0x10) = puVar9;
      *(code **)(lVar6 + 0x18) = FUN_00be129c;
      if ((*(byte *)(puVar9 + 0x28) & 1) == 0) {
        lVar7 = (long)puVar9 + 0x141;
      }
      else {
        lVar7 = puVar9[0x2a];
      }
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (uVar5,uVar3,
                 PTR__ZN8firebase4auth14FutureCallbackIvEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9ba18
                 ,lVar6,lVar7);
      _ZN8firebase12FutureHandleD2Ev(auStack_88);
      (**(code **)(*plVar2 + 0xb8))(plVar2,uVar3);
    }
    _ZN8firebase6FutureIvEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,lVar8,auStack_78);
    _ZN8firebase12FutureHandleD2Ev(auStack_78);
  }
  if (*(long *)(lVar1 + 0x28) == local_58) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
