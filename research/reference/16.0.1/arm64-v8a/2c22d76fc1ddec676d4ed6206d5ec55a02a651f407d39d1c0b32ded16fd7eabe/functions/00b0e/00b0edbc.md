# 00b0edbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b0e994`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e994.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0037.md#compare-dff6e0d364b07790fc605fa3efd56e2d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0037.md#compare-0d8233a1056290d8f956f5e9bef4dbab)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b0edbc",
  "name": "FUN_00b0edbc",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3c8bab51d6d15fa17081a7c27e509f5667d1843abf841ef99d13eb01e4655f5f",
  "source_text_sha256": "3c8bab51d6d15fa17081a7c27e509f5667d1843abf841ef99d13eb01e4655f5f"
}
~~~

## 呼び出し元

- [00a1a750](../00a1a/00a1a750.md)

## 呼び出し先

- [004802f8](../00480/004802f8.md)
- [004803f0](../00480/004803f0.md)

## 疑似コード / UTF-8 1132 bytes

~~~c

void FUN_00b0edbc(undefined4 *param_1,undefined8 param_2,uint param_3)

{
  byte bVar1;
  undefined4 uVar2;
  int iVar3;
  
  uVar2 = FUN_004803f0(param_2);
  *param_1 = uVar2;
  uVar2 = FUN_004803f0(param_2);
  param_1[3] = uVar2;
  uVar2 = FUN_004803f0(param_2);
  param_1[5] = uVar2;
  uVar2 = FUN_004803f0(param_2);
  param_1[4] = uVar2;
  uVar2 = FUN_004803f0(param_2);
  param_1[1] = uVar2;
  iVar3 = FUN_004803f0(param_2);
  *(bool *)(param_1 + 7) = iVar3 != 0;
  iVar3 = FUN_004803f0(param_2);
  *(bool *)((long)param_1 + 0x1d) = iVar3 != 0;
  iVar3 = FUN_004803f0(param_2);
  *(bool *)((long)param_1 + 0x1e) = iVar3 != 0;
  iVar3 = FUN_004803f0(param_2);
  *(bool *)((long)param_1 + 0x1f) = iVar3 != 0;
  uVar2 = FUN_004803f0(param_2);
  param_1[2] = uVar2;
  if (0x23 < (int)param_3) {
    iVar3 = FUN_004803f0(param_2);
    *(bool *)(param_1 + 8) = iVar3 != 0;
    if (0x9dc < param_3 >> 5) {
      iVar3 = FUN_004803f0(param_2);
      *(bool *)(param_1 + 9) = iVar3 != 0;
      if (0x18703 < param_3) {
        bVar1 = FUN_004802f8(param_2);
        *(byte *)(param_1 + 0xb) = bVar1 & 1;
      }
    }
  }
  return;
}

~~~
