# 00befb0c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bef6e4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef6e4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0086.md#compare-a8d5c05308f5fb9cdde0768dabf47587)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0095.md#compare-67f9ab61d2706e7551f5fd7903552f69)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00befb0c",
  "name": "_ZNSt16nested_exceptionC2Ev",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a83acee3a1d12a3c199bb2987b2e0ae2f296cabb3dc6e06dd77650a9794d5fee",
  "source_text_sha256": "a83acee3a1d12a3c199bb2987b2e0ae2f296cabb3dc6e06dd77650a9794d5fee"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5df40](../00c5d/00c5df40.md)

## 疑似コード / UTF-8 216 bytes

~~~c

void _ZNSt16nested_exceptionC2Ev(long *param_1)

{
  long lVar1;
  
  *param_1 = (long)(PTR__ZTVSt16nested_exception_00c9ba70 + 0x10);
  lVar1 = __cxa_current_primary_exception();
  param_1[1] = lVar1;
  return;
}

~~~
