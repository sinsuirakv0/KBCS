# 00b0eedc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b0eab4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0eab4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0037.md#compare-126e707470984468c84ae6c463d29c66)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0037.md#compare-e316d0bdb8209f2614bee64e23a813e1)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b0eedc",
  "name": "FUN_00b0eedc",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "83d494677ea9d2a50c34e7e2af8816b4290d3d2047311d39162a3438e5e1941b",
  "source_text_sha256": "83d494677ea9d2a50c34e7e2af8816b4290d3d2047311d39162a3438e5e1941b"
}
~~~

## 呼び出し元

- [00a223d0](../00a22/00a223d0.md)

## 呼び出し先

- [00480d48](../00480/00480d48.md)
- [00480e28](../00480/00480e28.md)

## 疑似コード / UTF-8 696 bytes

~~~c

void FUN_00b0eedc(undefined4 *param_1,undefined8 param_2)

{
  FUN_00480e28(param_2,*param_1);
  FUN_00480e28(param_2,param_1[3]);
  FUN_00480e28(param_2,param_1[5]);
  FUN_00480e28(param_2,param_1[4]);
  FUN_00480e28(param_2,param_1[1]);
  FUN_00480e28(param_2,*(undefined1 *)(param_1 + 7));
  FUN_00480e28(param_2,*(undefined1 *)((long)param_1 + 0x1d));
  FUN_00480e28(param_2,*(undefined1 *)((long)param_1 + 0x1e));
  FUN_00480e28(param_2,*(undefined1 *)((long)param_1 + 0x1f));
  FUN_00480e28(param_2,param_1[2]);
  FUN_00480e28(param_2,*(undefined1 *)(param_1 + 8));
  FUN_00480e28(param_2,*(undefined1 *)(param_1 + 9));
  FUN_00480d48(param_2,*(undefined1 *)(param_1 + 0xb));
  return;
}

~~~
