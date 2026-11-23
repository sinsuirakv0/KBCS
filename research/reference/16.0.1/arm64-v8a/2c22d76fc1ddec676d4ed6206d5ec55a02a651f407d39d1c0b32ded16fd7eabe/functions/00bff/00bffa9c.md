# 00bffa9c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bff674`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff674.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0041.md#compare-e52bb78123c35d02284021faddd3eba8)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0042.md#compare-930d82f9f14d214c4d75bfd379a24ed7)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffa9c",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE8pubimbueERKNS_6localeE",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ffa2f4192e6e6f2c9d5fca00554f8c7023612d6c406120e64f29e1130c471f21",
  "source_text_sha256": "ffa2f4192e6e6f2c9d5fca00554f8c7023612d6c406120e64f29e1130c471f21"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a7d0](../00c5a/00c5a7d0.md)
- [00c5e2e0](../00c5e/00c5e2e0.md)

## 疑似コード / UTF-8 307 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE8pubimbueERKNS_6localeE
               (undefined8 param_1,long *param_2,undefined8 param_3)

{
  (**(code **)(*param_2 + 0x10))();
  _ZNSt6__ndk16localeC1ERKS0_(param_1,param_2 + 1);
  _ZNSt6__ndk16localeaSERKS0_(param_2 + 1,param_3);
  return;
}

~~~
