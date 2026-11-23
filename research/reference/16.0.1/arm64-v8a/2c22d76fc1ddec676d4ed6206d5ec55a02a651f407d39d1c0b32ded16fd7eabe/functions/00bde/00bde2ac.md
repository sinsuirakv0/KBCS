# 00bde2ac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdde84`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdde84.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/no_difference_in_scope-0013.md#compare-4c0719b819124ed0320ef38e134c2b2b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/no_difference_in_scope-0014.md#compare-48cfb6ade89d8f764030416beeba5215)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bde2ac",
  "name": "_ZNK8firebase4auth4User8is_validEv",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6fd6b615520bf22e6337b7f1c1f35d308921f20a39fcc03aeabadc0b2a6b79f0",
  "source_text_sha256": "6fd6b615520bf22e6337b7f1c1f35d308921f20a39fcc03aeabadc0b2a6b79f0"
}
~~~

## 呼び出し元

- [00c5aa60](../00c5a/00c5aa60.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 183 bytes

~~~c

bool _ZNK8firebase4auth4User8is_validEv(long param_1)

{
  if (*(long *)(param_1 + 0x98) != 0) {
    return *(long *)(*(long *)(param_1 + 0x98) + 0x200) != 0;
  }
  return false;
}

~~~
