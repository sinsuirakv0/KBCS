# 00affedc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00affab4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aff/00affab4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0066.md#compare-4b2c04c0ab5d08a4af66f44f5f678b59)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/high-0009.md#compare-2b8b335c8af32e0a2d36850d37f28fc8)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00affedc",
  "name": "FUN_00affedc",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "af5a2662d8f83cc95094d35993ddb5fde654ce72ffe496b5fecf7926be2d7e90",
  "source_text_sha256": "af5a2662d8f83cc95094d35993ddb5fde654ce72ffe496b5fecf7926be2d7e90"
}
~~~

## 呼び出し元

- [00a4f3b4](../00a4f/00a4f3b4.md)

## 呼び出し先

- [005e7420](../005e7/005e7420.md)
- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 479 bytes

~~~c

undefined4 FUN_00affedc(int param_1,int param_2,int param_3)

{
  undefined4 *puVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_008514f8();
  uVar3 = FUN_005e7420(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  lVar2 = FUN_008514f8();
  puVar1 = (undefined4 *)((long)__DT_JMPREL + lVar2 + ((long)param_2 + 2) * 0x1c4 + 0x180c);
  if ((uVar3 & 1) != 0) {
    puVar1 = (undefined4 *)(lVar2 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9f6e4);
  }
  return *puVar1;
}

~~~
