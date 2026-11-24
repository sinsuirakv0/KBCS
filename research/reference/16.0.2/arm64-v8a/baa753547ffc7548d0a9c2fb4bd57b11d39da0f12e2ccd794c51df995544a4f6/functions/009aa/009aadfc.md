# 009aadfc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `009aada8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009aa/009aada8.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/no_difference_in_scope-0010.md#compare-667080bfbee17349c8fb43bb19b38900)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/no_difference_in_scope-0010.md#compare-951d734f1948bc9afca7fbc18d94e577)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009aadfc",
  "name": "FUN_009aadfc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e37cd428056f67c48765ed97866d71edeede6a02ae66b09ed26f411cb3c16da0",
  "source_text_sha256": "e37cd428056f67c48765ed97866d71edeede6a02ae66b09ed26f411cb3c16da0"
}
~~~

## 呼び出し元

- [009afefc](../009af/009afefc.md)
- [009b5db8](../009b5/009b5db8.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 306 bytes

~~~c

void FUN_009aadfc(undefined8 *param_1,long param_2)

{
  undefined4 uVar1;
  undefined8 uVar2;
  
  uVar2 = *(undefined8 *)(param_2 + 0x38);
  uVar1 = *(undefined4 *)(param_2 + 0x48);
  param_1[1] = *(undefined8 *)(param_2 + 0x40);
  *param_1 = uVar2;
  *(undefined4 *)(param_1 + 2) = uVar1;
  return;
}

~~~
