# 00b8fdbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b8fd20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8f/00b8fd20.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0077.md#compare-ceb19efde9c5be6c0f5fe901e34f17f3)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/high-0009.md#compare-e5e49fc78b92e0e3290dbe1bddeb648c)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b8fdbc",
  "name": "_ZN11flatbuffers21FlatBufferBuilderImplILb0EE26CreateVectorOfSortedTablesIN10reflection4EnumENSt6__ndk19allocatorINS_6OffsetIS4_EEEEEENS7_INS_6VectorINS7_IT_EEjEEEEPNS5_6vectorISC_T0_EE",
  "size": 472,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4eea3dea745383cd53e694abdadd5af9d805ae12c5a004eb3cb6a27293965554",
  "source_text_sha256": "4eea3dea745383cd53e694abdadd5af9d805ae12c5a004eb3cb6a27293965554"
}
~~~

## 呼び出し元

- [00c5c3b0](../00c5c/00c5c3b0.md)

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5a920](../00c5a/00c5a920.md)
- [00c5c270](../00c5c/00c5c270.md)
- [00c5c320](../00c5c/00c5c320.md)
- [00c5c350](../00c5c/00c5c350.md)
- [00c5cbd0](../00c5c/00c5cbd0.md)

## 疑似コード / UTF-8 3870 bytes

~~~c

undefined4
_ZN11flatbuffers21FlatBufferBuilderImplILb0EE26CreateVectorOfSortedTablesIN10reflection4EnumENSt6__ndk19allocatorINS_6OffsetIS4_EEEEEENS7_INS_6VectorINS7_IT_EEjEEEEPNS5_6vectorISC_T0_EE
          (long param_1,long *param_2)

{
  uint uVar1;
  undefined *puVar2;
  undefined *puVar3;
  int iVar4;
  long lVar5;
  undefined *puVar6;
  undefined4 uVar7;
  void *__ptr;
  int iVar8;
  ulong uVar9;
  long lVar10;
  ulong uVar11;
  ulong uVar12;
  ulong uVar13;
  long local_70;
  long local_68;
  
  puVar6 = PTR__ZSt7nothrow_00c9b5f0;
  lVar5 = tpidr_el0;
  local_68 = *(long *)(lVar5 + 0x28);
  puVar3 = (undefined *)*param_2;
  uVar13 = param_2[1] - (long)puVar3;
  puVar2 = 
  PTR__ZZN11flatbuffers4dataINS_6OffsetIN10reflection4EnumEEENSt6__ndk19allocatorIS4_EEEEPT_RNS5_6vectorIS8_T0_EEE1t_00c9b928
  ;
  if (puVar3 != (undefined *)param_2[1]) {
    puVar2 = puVar3;
  }
  uVar11 = (long)uVar13 >> 2;
  local_70 = param_1;
  if (0x200 < (long)uVar13) {
    uVar12 = uVar11;
    if (0x1ffffffffffffffe < (long)uVar11) {
      uVar12 = 0x1fffffffffffffff;
    }
    do {
      __ptr = (void *)_ZnwmRKSt9nothrow_t(uVar12 << 2,puVar6);
      if (__ptr != (void *)0x0) {
                    /* try { // try from 00b8fe64 to 00c8fe6f has its CatchHandler @ 00b914f0 */
        _ZNSt6__ndk113__stable_sortIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6_EEEEvT0_SC_T_NS_15iterator_traitsISC_E15difference_typeEPNSF_10value_typeEl
                  (puVar2,puVar2 + uVar13,&local_70,uVar11,__ptr,uVar12);
                    /* try { // try from 00b8fe88 to 00c8fea3 has its CatchHandler @ 00b914d0 */
        _ZdlPv(__ptr);
        goto LAB_00b8fe8c;
      }
      uVar12 = uVar12 >> 1;
    } while (uVar12 != 0);
  }
  _ZNSt6__ndk113__stable_sortIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6_EEEEvT0_SC_T_NS_15iterator_traitsISC_E15difference_typeEPNSF_10value_typeEl
            (puVar2,puVar2 + uVar13,&local_70,uVar11,0,0);
LAB_00b8fe8c:
  _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11StartVectorINS_6OffsetEjEEvmmm(param_1,uVar11,4,4);
  uVar12 = uVar13;
  while (uVar12 != 0) {
    uVar11 = uVar11 - 1;
    iVar4 = *(int *)(puVar2 + uVar11 * 4);
    if (*(ulong *)(param_1 + 0x68) < 4) {
      *(undefined8 *)(param_1 + 0x68) = 4;
    }
    iVar8 = *(int *)(param_1 + 0x30);
                    /* try { // try from 00b8fee0 to 00c8feeb has its CatchHandler @ 00b914c8 */
    uVar1 = -iVar8 & 3;
    uVar12 = (ulong)uVar1;
    if (uVar1 != 0) {
      lVar10 = *(long *)(param_1 + 0x40);
      if ((uint)((int)lVar10 - *(int *)(param_1 + 0x48)) < uVar12) {
                    /* try { // try from 00b8ff04 to 00c8ff27 has its CatchHandler @ 00b914f8 */
        _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_1,uVar12);
        lVar10 = *(long *)(param_1 + 0x40);
        iVar8 = *(int *)(param_1 + 0x30);
      }
      *(undefined1 **)(param_1 + 0x40) = (undefined1 *)(lVar10 - uVar12);
      *(uint *)(param_1 + 0x30) = iVar8 + uVar1;
                    /* try { // try from 00b8ff28 to 00c9000b has its CatchHandler @ 00b8e624 */
      *(undefined1 *)(lVar10 - uVar12) = 0;
      if (uVar1 != 1) {
        uVar9 = 1;
        do {
          *(undefined1 *)(*(long *)(param_1 + 0x40) + uVar9) = 0;
          uVar9 = uVar9 + 1;
        } while (uVar12 != uVar9);
      }
    }
    _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIjjEET0_T_
              (param_1,(*(int *)(param_1 + 0x30) - iVar4) + 4);
    uVar12 = uVar11;
  }
  *(undefined1 *)(param_1 + 0x60) = 0;
  uVar7 = _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIjjEET0_T_(param_1,uVar13 >> 2);
  if (*(long *)(lVar5 + 0x28) == local_68) {
    return uVar7;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
