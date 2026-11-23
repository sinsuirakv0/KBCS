# 00ac8ddc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00ac8be0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8be0.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/no_difference_in_scope-0012.md#compare-c286b883f8f2717fe1580b002db60849)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/no_difference_in_scope-0013.md#compare-ed49fa90e3aea138dda74fe1d71a155a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ac8ddc",
  "name": "FUN_00ac8ddc",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f7894d32cef2af6f1be9914a6c8d425f920168e941e0f22b1ba300bd57a5ca49",
  "source_text_sha256": "f7894d32cef2af6f1be9914a6c8d425f920168e941e0f22b1ba300bd57a5ca49"
}
~~~

## 呼び出し元

- [00789c50](../00789/00789c50.md)
- [00789de0](../00789/00789de0.md)
- [0078bd58](../0078b/0078bd58.md)
- [0078bfc4](../0078b/0078bfc4.md)
- [0078df38](../0078d/0078df38.md)
- [0078e91c](../0078e/0078e91c.md)
- [0078eb30](../0078e/0078eb30.md)
- [0082c864](../0082c/0082c864.md)
- [0082cd18](../0082c/0082cd18.md)
- [0082d7a8](../0082d/0082d7a8.md)
- [00a72594](../00a72/00a72594.md)
- [00a75dac](../00a75/00a75dac.md)
- [00a79c04](../00a79/00a79c04.md)
- [00ac0a9c](../00ac0/00ac0a9c.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 87 bytes

~~~c

undefined4 FUN_00ac8ddc(long param_1)

{
  return *(undefined4 *)(param_1 + 0x60);
}

~~~
