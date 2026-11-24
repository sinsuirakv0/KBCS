# 00b0caec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b0ca50`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0ca50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/inspection-0037.md#compare-3f4bc19a21260a66c6800b50304b5823)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0031.md#compare-0e4f20c009504ff9bf524445d973befc)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b0caec",
  "name": "FUN_00b0caec",
  "size": 396,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a4c73caa9efe1b563ef7efa498cdc55d72edd57e68ae383eb338d93cd694a269",
  "source_text_sha256": "a4c73caa9efe1b563ef7efa498cdc55d72edd57e68ae383eb338d93cd694a269"
}
~~~

## 呼び出し元

- [00b0af3c](../00b0a/00b0af3c.md)

## 呼び出し先

- [00440f00](../00440/00440f00.md)
- [00b0cac4](../00b0c/00b0cac4.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)

## 疑似コード / UTF-8 2188 bytes

~~~c

undefined8 * FUN_00b0caec(long *param_1,undefined8 *param_2)

{
  ulong uVar1;
  long lVar2;
  void *__ptr;
  long lVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  undefined8 *puVar6;
  long lVar7;
  undefined8 uVar8;
  ulong uVar9;
  undefined8 *__ptr_00;
  undefined8 *puVar10;
  undefined8 uVar11;
  undefined8 uVar12;
  
  lVar3 = param_1[1] - *param_1 >> 3;
  uVar1 = lVar3 * -0x5555555555555555 + 1;
  if (0xaaaaaaaaaaaaaaa < uVar1) {
    FUN_00b0cac4(param_1);
LAB_00b0cc74:
                    /* WARNING: Subroutine does not return */
    FUN_00440f00();
  }
  lVar7 = param_1[2] - *param_1 >> 3;
  uVar9 = lVar7 * 0x5555555555555556;
  if (uVar9 < uVar1 || uVar9 - uVar1 == 0) {
    uVar9 = uVar1;
  }
  if (0x555555555555554 < (ulong)(lVar7 * -0x5555555555555555)) {
    uVar9 = 0xaaaaaaaaaaaaaaa;
  }
  if (uVar9 == 0) {
    lVar7 = 0;
  }
  else {
    if (0xaaaaaaaaaaaaaaa < uVar9) goto LAB_00b0cc74;
    lVar7 = _Znwm(uVar9 * 0x18);
  }
  uVar12 = param_2[1];
  uVar11 = *param_2;
  *param_2 = 0;
  param_2[1] = 0;
  puVar5 = (undefined8 *)(lVar7 + lVar3 * 8);
  uVar8 = param_2[2];
  param_2[2] = 0;
  puVar10 = (undefined8 *)*param_1;
  __ptr_00 = (undefined8 *)param_1[1];
  lVar2 = (long)__ptr_00 - (long)puVar10;
  puVar5[1] = uVar12;
  *puVar5 = uVar11;
  puVar5[2] = uVar8;
  if ((long)__ptr_00 - (long)puVar10 != 0) {
    puVar4 = (undefined8 *)(lVar3 * 8 + ((long)__ptr_00 - (long)puVar10 >> 3) * -8 + lVar7 + 0x10);
    puVar6 = puVar10;
    do {
      *puVar4 = 0;
      uVar8 = *puVar6;
      puVar4[-1] = puVar6[1];
      puVar4[-2] = uVar8;
      *puVar4 = puVar6[2];
      *puVar6 = 0;
      puVar6[1] = 0;
      puVar6[2] = 0;
      puVar6 = puVar6 + 3;
      puVar4 = puVar4 + 3;
    } while (puVar6 != __ptr_00);
    do {
      __ptr = (void *)*puVar10;
      if (__ptr != (void *)0x0) {
        puVar10[1] = __ptr;
        _ZdlPv(__ptr);
      }
      puVar10 = puVar10 + 3;
    } while (puVar10 != __ptr_00);
    __ptr_00 = (undefined8 *)*param_1;
  }
  *param_1 = (long)puVar5 - lVar2;
  param_1[1] = (long)(puVar5 + 3);
  param_1[2] = lVar7 + uVar9 * 0x18;
  if (__ptr_00 != (undefined8 *)0x0) {
    _ZdlPv(__ptr_00);
  }
  return puVar5 + 3;
}

~~~
