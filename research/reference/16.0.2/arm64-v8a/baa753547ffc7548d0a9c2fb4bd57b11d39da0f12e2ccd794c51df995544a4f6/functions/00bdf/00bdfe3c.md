# 00bdfe3c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdfda0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdfda0.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0085.md#compare-0853697accafd364dbed3cefb98ef7e1)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/high-0011.md#compare-a2a22a47993c719609753924199258a0)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfe3c",
  "name": "_ZN8firebase4auth4User18LinkWithCredentialERKNS0_10CredentialE",
  "size": 396,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6def15d97b008ef90eee851e5d50a481d6ff3961a187182ff6d6cdc4e3e9cdb0",
  "source_text_sha256": "6def15d97b008ef90eee851e5d50a481d6ff3961a187182ff6d6cdc4e3e9cdb0"
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
- [00c5aed0](../00c5a/00c5aed0.md)
- [00c5b010](../00c5b/00c5b010.md)
- [00c5b150](../00c5b/00c5b150.md)
- [00c5dcd0](../00c5d/00c5dcd0.md)
- [00c5dda0](../00c5d/00c5dda0.md)
- [00c5de00](../00c5d/00c5de00.md)

## 疑似コード / UTF-8 3320 bytes

~~~c

void _ZN8firebase4auth4User18LinkWithCredentialERKNS0_10CredentialE
               (long param_1,long param_2,undefined8 *param_3)

{
  long lVar1;
  undefined *puVar2;
  long *plVar3;
  undefined8 uVar4;
  ulong uVar5;
  undefined8 uVar6;
  long lVar7;
  long lVar8;
  long lVar9;
  undefined8 *puVar10;
  undefined1 auStack_78 [16];
  undefined1 auStack_68 [16];
  long local_58;
  
                    /* try { // try from 00bdfe50 to 00cdfe5b has its CatchHandler @ 00be0804 */
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  lVar9 = *(long *)(param_2 + 0x98);
  if ((lVar9 == 0) || (*(long *)(lVar9 + 0x200) == 0)) {
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    lVar9 = lVar9 + 0x10;
    _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEi
              (auStack_68,lVar9,0x12);
    plVar3 = (long *)_ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
    uVar4 = FUN_00497874(plVar3,*(undefined8 *)(*(long *)(param_2 + 0x98) + 0x200),DAT_01126e60,
                         *param_3);
                    /* try { // try from 00bdfec0 to 00cdfeef has its CatchHandler @ 00be07a8 */
    uVar5 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                      (plVar3,lVar9,auStack_68);
    if ((uVar5 & 1) == 0) {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,auStack_68);
      puVar10 = *(undefined8 **)(param_2 + 0x98);
      uVar6 = _ZNK8firebase3App9GetJNIEnvEv(*puVar10);
      lVar7 = _Znwm(0x20);
      _ZN8firebase12FutureHandleC1ERKS0_(lVar7,auStack_78);
      puVar2 = 
      PTR__ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv_00c9baf0
      ;
                    /* try { // try from 00bdff04 to 00cdff0f has its CatchHandler @ 00be07a4 */
      *(undefined8 **)(lVar7 + 0x10) = puVar10;
      *(undefined **)(lVar7 + 0x18) = puVar2;
      if ((*(byte *)(puVar10 + 0x28) & 1) == 0) {
                    /* try { // try from 00bdff1c to 00cdff4f has its CatchHandler @ 00be0590 */
        lVar8 = (long)puVar10 + 0x141;
      }
      else {
        lVar8 = puVar10[0x2a];
      }
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (uVar6,uVar4,
                 PTR__ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9bad0
                 ,lVar7,lVar8);
      _ZN8firebase12FutureHandleD2Ev(auStack_78);
                    /* try { // try from 00bdff7c to 00cdff87 has its CatchHandler @ 00be07a8 */
      (**(code **)(*plVar3 + 0xb8))(plVar3,uVar4);
    }
    _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,lVar9,auStack_68);
                    /* try { // try from 00bdff94 to 00cdffc7 has its CatchHandler @ 00be0594 */
    _ZN8firebase12FutureHandleD2Ev(auStack_68);
  }
  if (*(long *)(lVar1 + 0x28) == local_58) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
