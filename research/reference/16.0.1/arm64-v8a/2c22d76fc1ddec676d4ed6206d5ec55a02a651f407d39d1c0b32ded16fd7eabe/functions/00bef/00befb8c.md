# 00befb8c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bef764`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef764.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0039.md#compare-5c934df6712def2892a7ad823941719c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0040.md#compare-18a9c3fdfdf55644b0aeb380da6ea642)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00befb8c",
  "name": "_ZNSt16nested_exceptionD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5f9b4c3ecb8743b3c446c82624c10459684c79cd235c4c6fe645e9a2f4b704da",
  "source_text_sha256": "5f9b4c3ecb8743b3c446c82624c10459684c79cd235c4c6fe645e9a2f4b704da"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)
- [00c5df50](../00c5d/00c5df50.md)

## 疑似コード / UTF-8 117 bytes

~~~c

void _ZNSt16nested_exceptionD0Ev(void *param_1)

{
  _ZNSt16nested_exceptionD2Ev();
  _ZdlPv(param_1);
  return;
}

~~~
