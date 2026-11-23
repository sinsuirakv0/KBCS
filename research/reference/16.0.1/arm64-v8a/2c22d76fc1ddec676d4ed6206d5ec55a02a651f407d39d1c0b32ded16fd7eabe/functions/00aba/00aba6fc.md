# 00aba6fc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aba500`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aba/00aba500.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0035.md#compare-911cb75e70df42b7434ce96e212501f1)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0035.md#compare-ac1de9f69ec985593430645205177071)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aba6fc",
  "name": "FUN_00aba6fc",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "97eaf635c28f3406172d3a413bf794c29af4aa8dcf067db01133c67460621767",
  "source_text_sha256": "97eaf635c28f3406172d3a413bf794c29af4aa8dcf067db01133c67460621767"
}
~~~

## 呼び出し元

- [005fe66c](../005fe/005fe66c.md)
- [00605254](../00605/00605254.md)
- [007bda44](../007bd/007bda44.md)
- [007caac8](../007ca/007caac8.md)
- [007df0e8](../007df/007df0e8.md)
- [007efca8](../007ef/007efca8.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)
- [00b3e410](../00b3e/00b3e410.md)

## 疑似コード / UTF-8 121 bytes

~~~c

void FUN_00aba6fc(void)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
  FUN_00b3e410(lVar1 + 0x2350,0xa1);
  return;
}

~~~
