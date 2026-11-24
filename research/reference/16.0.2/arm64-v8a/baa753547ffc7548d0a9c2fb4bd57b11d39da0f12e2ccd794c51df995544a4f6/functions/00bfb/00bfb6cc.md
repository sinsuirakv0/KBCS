# 00bfb6cc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfb630`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb630.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/inspection-0041.md#compare-8d3205166a170fb1df84c6a63216f034)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0039.md#compare-bbf569e92eb392cead5468cd2aec41b6)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfb6cc",
  "name": "_ZNSt6__ndk18ios_base7copyfmtERKS0_",
  "size": 688,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b67b69acf7dcb784668b08e1a57eb853e1444e917f18b082240fc5ef1ec76d11",
  "source_text_sha256": "b67b69acf7dcb784668b08e1a57eb853e1444e917f18b082240fc5ef1ec76d11"
}
~~~

## 呼び出し元

- [00c5e3e0](../00c5e/00c5e3e0.md)

## 呼び出し先

- [00c53ffc](../00c53/00c53ffc.md)
- [00c58730](../00c58/00c58730.md)
- [00c5a0f0](../00c5a/00c5a0f0.md)
- [00c5e050](../00c5e/00c5e050.md)
- [00c5e3b0](../00c5e/00c5e3b0.md)

## 疑似コード / UTF-8 4411 bytes

~~~c

void _ZNSt6__ndk18ios_base7copyfmtERKS0_(long param_1,long param_2)

{
  ulong uVar1;
  void *__ptr;
  void *__ptr_00;
  void *__ptr_01;
  undefined8 uVar2;
  ulong uVar3;
  long lVar4;
  long lVar5;
  void *unaff_x19;
  void *pvVar6;
  void *unaff_x23;
  undefined8 uVar7;
  
  pvVar6 = *(void **)(param_2 + 0x48);
  if (*(void **)(param_1 + 0x50) < pvVar6) {
    __ptr = malloc((long)pvVar6 << 3);
    if (__ptr == (void *)0x0) {
      _ZSt17__throw_bad_allocv();
LAB_00bfb934:
      uVar2 = _ZSt17__throw_bad_allocv();
      if (unaff_x23 != (void *)0x0) {
        free(unaff_x23);
      }
      if (pvVar6 != (void *)0x0) {
        free(pvVar6);
      }
      if (unaff_x19 != (void *)0x0) {
        free(unaff_x19);
                    /* WARNING: Subroutine does not return */
        FUN_00c53ffc(uVar2);
      }
                    /* WARNING: Subroutine does not return */
      FUN_00c53ffc(uVar2);
    }
    __ptr_00 = malloc((long)pvVar6 << 2);
    unaff_x19 = __ptr;
    if (__ptr_00 == (void *)0x0) goto LAB_00bfb934;
  }
  else {
    __ptr_00 = (void *)0x0;
    __ptr = (void *)0x0;
  }
  if (*(ulong *)(param_1 + 0x68) < *(ulong *)(param_2 + 0x60)) {
    pvVar6 = malloc(*(ulong *)(param_2 + 0x60) << 3);
    if (pvVar6 == (void *)0x0) {
      _ZSt17__throw_bad_allocv();
      goto LAB_00bfb74c;
    }
  }
  else {
LAB_00bfb74c:
    pvVar6 = (void *)0x0;
  }
  if (*(ulong *)(param_1 + 0x80) < *(ulong *)(param_2 + 0x78)) {
    __ptr_01 = malloc(*(ulong *)(param_2 + 0x78) << 3);
    if (__ptr_01 != (void *)0x0) goto LAB_00bfb778;
    _ZSt17__throw_bad_allocv();
  }
  __ptr_01 = (void *)0x0;
LAB_00bfb778:
  uVar7 = *(undefined8 *)(param_2 + 0x18);
  uVar2 = *(undefined8 *)(param_2 + 0x10);
  *(undefined4 *)(param_1 + 8) = *(undefined4 *)(param_2 + 8);
  *(undefined8 *)(param_1 + 0x18) = uVar7;
  *(undefined8 *)(param_1 + 0x10) = uVar2;
  _ZNSt6__ndk16localeaSERKS0_(param_1 + 0x30,param_2 + 0x30);
  if (*(ulong *)(param_1 + 0x50) < *(ulong *)(param_2 + 0x48)) {
    free(*(void **)(param_1 + 0x38));
    *(void **)(param_1 + 0x38) = __ptr;
    free(*(void **)(param_1 + 0x40));
    uVar2 = *(undefined8 *)(param_2 + 0x48);
    __ptr = (void *)0x0;
    *(void **)(param_1 + 0x40) = __ptr_00;
    __ptr_00 = (void *)0x0;
    *(undefined8 *)(param_1 + 0x50) = uVar2;
  }
  *(undefined8 *)(param_1 + 0x48) = 0;
  if (*(long *)(param_2 + 0x48) != 0) {
    uVar3 = 0;
    do {
      lVar4 = uVar3 * 8;
      lVar5 = uVar3 * 4;
      uVar3 = uVar3 + 1;
      uVar2 = *(undefined8 *)(*(long *)(param_2 + 0x38) + lVar4);
      *(ulong *)(param_1 + 0x48) = uVar3;
      *(undefined8 *)(*(long *)(param_1 + 0x38) + lVar4) = uVar2;
      uVar1 = *(ulong *)(param_2 + 0x48);
      *(undefined4 *)(*(long *)(param_1 + 0x40) + lVar5) =
           *(undefined4 *)(*(long *)(param_2 + 0x40) + lVar5);
    } while (uVar3 < uVar1);
  }
  if (*(ulong *)(param_1 + 0x68) < *(ulong *)(param_2 + 0x60)) {
    free(*(void **)(param_1 + 0x58));
    uVar2 = *(undefined8 *)(param_2 + 0x60);
    *(void **)(param_1 + 0x58) = pvVar6;
    pvVar6 = (void *)0x0;
    *(undefined8 *)(param_1 + 0x68) = uVar2;
  }
  *(undefined8 *)(param_1 + 0x60) = 0;
  if (*(long *)(param_2 + 0x60) != 0) {
    lVar4 = *(long *)(param_2 + 0x58);
    lVar5 = *(long *)(param_1 + 0x58);
    uVar3 = 0;
    do {
      *(undefined8 *)(lVar5 + uVar3 * 8) = *(undefined8 *)(lVar4 + uVar3 * 8);
      uVar3 = *(long *)(param_1 + 0x60) + 1;
      *(ulong *)(param_1 + 0x60) = uVar3;
    } while (uVar3 < *(ulong *)(param_2 + 0x60));
  }
  if (*(ulong *)(param_1 + 0x80) < *(ulong *)(param_2 + 0x78)) {
    free(*(void **)(param_1 + 0x70));
    uVar2 = *(undefined8 *)(param_2 + 0x78);
    *(void **)(param_1 + 0x70) = __ptr_01;
    __ptr_01 = (void *)0x0;
    *(undefined8 *)(param_1 + 0x80) = uVar2;
  }
  *(undefined8 *)(param_1 + 0x78) = 0;
  if (*(long *)(param_2 + 0x78) != 0) {
    uVar3 = 0;
    do {
      lVar4 = uVar3 * 8;
      uVar3 = uVar3 + 1;
      *(ulong *)(param_1 + 0x78) = uVar3;
      uVar1 = *(ulong *)(param_2 + 0x78);
      *(undefined8 *)(*(long *)(param_1 + 0x70) + lVar4) =
           *(undefined8 *)(*(long *)(param_2 + 0x70) + lVar4);
    } while (uVar3 < uVar1);
  }
  if (__ptr_01 != (void *)0x0) {
    free(__ptr_01);
  }
  if (pvVar6 != (void *)0x0) {
    free(pvVar6);
  }
  if (__ptr_00 != (void *)0x0) {
    free(__ptr_00);
  }
  if (__ptr != (void *)0x0) {
    free(__ptr);
    return;
  }
  return;
}

~~~
