# 00acafb4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00acadb8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acadb8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0035.md#compare-8d79d6265dfbc2f5316e401da744dc0d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0035.md#compare-20445605167e68edd585463545cbab9c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acafb4",
  "name": "FUN_00acafb4",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e3038d08e80c19faeb132d5462da0ce2621e5bedaa8b0a794ab06fc10931c483",
  "source_text_sha256": "e3038d08e80c19faeb132d5462da0ce2621e5bedaa8b0a794ab06fc10931c483"
}
~~~

## 呼び出し元

- [00788cac](../00788/00788cac.md)
- [0082ee20](../0082e/0082ee20.md)
- [008fe9e4](../008fe/008fe9e4.md)
- [00a3de58](../00a3d/00a3de58.md)
- [00ac0454](../00ac0/00ac0454.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 307 bytes

~~~c

void FUN_00acafb4(long param_1,uint param_2)

{
  undefined4 uVar1;
  
  if ((param_2 & 1) == 0) {
    *(undefined4 *)(param_1 + 0x9c) = 2;
    FUN_008514f8();
    uVar1 = 0xe;
  }
  else {
    uVar1 = 0;
    *(undefined4 *)(param_1 + 0x9c) = 3;
  }
  *(undefined4 *)(param_1 + 0x98) = uVar1;
  return;
}

~~~
