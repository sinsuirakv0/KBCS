# 00bfabf0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfa7c8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa7c8.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0041.md#compare-a5610e2a13cc9f2dbeb3f3b2b2a10ebb)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0042.md#compare-2bbb432faa287affe7cc9baa43ed28ed)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfabf0",
  "name": "_ZNSt6__ndk115__thread_structD1Ev",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e1514a8542a25f4aa387c17e64e04c04f510f9eb235192d5b2ba74cc3dc3421e",
  "source_text_sha256": "e1514a8542a25f4aa387c17e64e04c04f510f9eb235192d5b2ba74cc3dc3421e"
}
~~~

## 呼び出し元

- [00c58150](../00c58/00c58150.md)

## 呼び出し先

- [00bfa8fc](../00bfa/00bfa8fc.md)
- [00c57eb0](../00c57/00c57eb0.md)

## 疑似コード / UTF-8 213 bytes

~~~c

void _ZNSt6__ndk115__thread_structD1Ev(undefined8 *param_1)

{
  void *__ptr;
  
  __ptr = (void *)*param_1;
  if (__ptr != (void *)0x0) {
    FUN_00bfa8fc(__ptr);
    _ZdlPv(__ptr);
    return;
  }
  return;
}

~~~
