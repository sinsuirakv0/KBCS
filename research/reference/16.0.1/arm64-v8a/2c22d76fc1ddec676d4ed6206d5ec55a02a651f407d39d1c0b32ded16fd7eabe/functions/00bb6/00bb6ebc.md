# 00bb6ebc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bb6a94`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6a94.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0079.md#compare-7bf8adb6e343ec67eb98b15aa836e109)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0088.md#compare-cb90b704b7451d6f5f73a6e889a2369d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb6ebc",
  "name": "_ZN8firebase9messaging16PollableListenerD0Ev",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b087bd9efc7b807144014561e42b1f86b10abb513c673ad91ab6d0ba26efc3a8",
  "source_text_sha256": "b087bd9efc7b807144014561e42b1f86b10abb513c673ad91ab6d0ba26efc3a8"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)
- [00c5aac0](../00c5a/00c5aac0.md)
- [00c5d380](../00c5d/00c5d380.md)

## 疑似コード / UTF-8 397 bytes

~~~c

void _ZN8firebase9messaging16PollableListenerD0Ev(long *param_1)

{
  void *__ptr;
  
  __ptr = (void *)param_1[1];
  *param_1 = (long)(PTR__ZTVN8firebase9messaging16PollableListenerE_00c9b900 + 0x10);
  if (__ptr != (void *)0x0) {
    _ZN8firebase9messaging20PollableListenerImplD2Ev(__ptr);
    _ZdlPv(__ptr);
  }
  _ZN8firebase9messaging8ListenerD2Ev(param_1);
  _ZdlPv(param_1);
  return;
}

~~~
