# 00bfbcc0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfb898`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb898.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/reference_unresolved-0001.md#compare-c3a8e0b4255bc6cf34a818b2cc591eff)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/reference_unresolved-0001.md#compare-d302f9af8bafc21ca1033671ae30c9f4)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbcc0",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE10pubseekposENS_4fposI9mbstate_tEEj",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "18077c1499bb404858e9f230691d19ad5debb0d27d3a653816554dcb79979b8b",
  "source_text_sha256": "18077c1499bb404858e9f230691d19ad5debb0d27d3a653816554dcb79979b8b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 339 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE10pubseekposENS_4fposI9mbstate_tEEj
               (long *param_1)

{
                    /* WARNING: Could not recover jumptable at 0x00bfbccc. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*param_1 + 0x28))();
  return;
}

~~~
