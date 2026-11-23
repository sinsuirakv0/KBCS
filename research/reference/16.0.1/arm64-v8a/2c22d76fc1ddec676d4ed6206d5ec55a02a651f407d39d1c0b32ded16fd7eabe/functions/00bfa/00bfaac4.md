# 00bfaac4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfa69c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa69c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0041.md#compare-1f9db51c5a24ef443e7cfb7a8dadd92d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0042.md#compare-26522fa960208ee8d4f2c74c2738d3d0)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfaac4",
  "name": "FUN_00bfaac4",
  "size": 240,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "905f9b7d60c3362f7a7a28d1131ce1a89ec422ae2595ca39443a1e5eb16fce9c",
  "source_text_sha256": "905f9b7d60c3362f7a7a28d1131ce1a89ec422ae2595ca39443a1e5eb16fce9c"
}
~~~

## 呼び出し元

- [00bfac40](../00bfa/00bfac40.md)

## 呼び出し先

- [00bfac64](../00bfa/00bfac64.md)
- [00c53cd0](../00c53/00c53cd0.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c58000](../00c58/00c58000.md)

## 疑似コード / UTF-8 1577 bytes

~~~c

void FUN_00bfaac4(long *param_1,long param_2)

{
  ulong uVar1;
  long *plVar2;
  long lVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  size_t __n;
  ulong uVar6;
  long lVar7;
  ulong uVar8;
  void *__src;
  long lVar9;
  long *plVar10;
  
  plVar2 = (long *)param_1[1];
  if (plVar2 < (long *)param_1[2]) {
    plVar10 = plVar2 + 1;
    *plVar2 = param_2;
  }
  else {
    __src = (void *)*param_1;
    __n = (long)plVar2 - (long)__src;
    lVar9 = (long)__n >> 3;
    uVar1 = lVar9 + 1;
    if (uVar1 >> 0x3d != 0) {
      puVar4 = (undefined8 *)FUN_00bfac64(param_1);
      puVar5 = (undefined8 *)_Znwm(0x30);
      *puVar4 = puVar5;
      puVar5[1] = 0;
      *puVar5 = 0;
      puVar5[3] = 0;
      puVar5[2] = 0;
      puVar5[5] = 0;
      puVar5[4] = 0;
      return;
    }
    uVar6 = param_1[2] - (long)__src;
    uVar8 = (long)uVar6 >> 2;
    if (uVar8 <= uVar1) {
      uVar8 = uVar1;
    }
    if (0x7ffffffffffffff7 < uVar6) {
      uVar8 = 0x1fffffffffffffff;
    }
    if (uVar8 == 0) {
      lVar3 = 0;
      lVar7 = lVar9;
    }
    else {
      lVar3 = _Znwm(uVar8 << 3);
      __src = (void *)*param_1;
      __n = param_1[1] - (long)__src;
      lVar7 = (long)__n >> 3;
    }
    plVar2 = (long *)(lVar3 + lVar9 * 8);
    plVar10 = plVar2 + 1;
    *plVar2 = param_2;
    memcpy(plVar2 + -lVar7,__src,__n);
    *param_1 = (long)(plVar2 + -lVar7);
    param_1[1] = (long)plVar10;
    param_1[2] = lVar3 + uVar8 * 8;
    if (__src != (void *)0x0) {
      _ZdlPv(__src);
    }
  }
  param_1[1] = (long)plVar10;
  FUN_00c53cd0(1,param_2 + 8);
  return;
}

~~~
