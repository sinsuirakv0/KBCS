# 00bcade4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bca9bc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bca/00bca9bc.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0039.md#compare-e308a3780c8d134432002b5c37c2e50a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0040.md#compare-7819ca8cc67b9cb24f51a92a578992b5)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcade4",
  "name": "_ZN8firebase4auth4AuthD1Ev",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "24ea105ea03fed0548be79cb4a5abe623bea50a6c8ec0f767ed972224ff698b6",
  "source_text_sha256": "24ea105ea03fed0548be79cb4a5abe623bea50a6c8ec0f767ed972224ff698b6"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5da30](../00c5d/00c5da30.md)

## 疑似コード / UTF-8 101 bytes

~~~c

void _ZN8firebase4auth4AuthD1Ev(void)

{
  _ZN8firebase4auth4Auth14DeleteInternalEv();
  return;
}

~~~
