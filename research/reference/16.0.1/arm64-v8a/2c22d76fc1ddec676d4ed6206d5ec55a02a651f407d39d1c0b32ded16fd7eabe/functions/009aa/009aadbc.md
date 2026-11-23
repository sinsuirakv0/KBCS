# 009aadbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `009aac20`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009aa/009aac20.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/no_difference_in_scope-0010.md#compare-a8a7242d1b96df01b303330deb8b2d7b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/no_difference_in_scope-0010.md#compare-0afbeb0f7edce20aa98080876342c516)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009aadbc",
  "name": "FUN_009aadbc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8610a3fe1d9e68e1183c1ed4e7a486e3c4dcf15d504acfffde30ea102793e510",
  "source_text_sha256": "8610a3fe1d9e68e1183c1ed4e7a486e3c4dcf15d504acfffde30ea102793e510"
}
~~~

## 呼び出し元

- [007644e4](../00764/007644e4.md)
- [009afea8](../009af/009afea8.md)
- [009b5d74](../009b5/009b5d74.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 306 bytes

~~~c

void FUN_009aadbc(undefined8 *param_1,long param_2)

{
  undefined4 uVar1;
  undefined8 uVar2;
  
  uVar2 = *(undefined8 *)(param_2 + 0x4c);
  uVar1 = *(undefined4 *)(param_2 + 0x5c);
  param_1[1] = *(undefined8 *)(param_2 + 0x54);
  *param_1 = uVar2;
  *(undefined4 *)(param_1 + 2) = uVar1;
  return;
}

~~~
