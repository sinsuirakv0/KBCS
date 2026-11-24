# 00bffb8c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bffaf0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffaf0.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/machine_only_observed-0023.md#compare-3c414b1f0847e5a53cc5705ce4bdeaf1)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/machine_only_observed-0022.md#compare-b2d0d2c691260f6dde7de9bc61dbc4b6)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffb8c",
  "name": "_ZNKSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6getlocEv",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "edf9af5098433a6669fa230d88f6652b8d857b234542fe3f462f8d9250b066e0",
  "source_text_sha256": "edf9af5098433a6669fa230d88f6652b8d857b234542fe3f462f8d9250b066e0"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a8a0](../00c5a/00c5a8a0.md)

## 疑似コード / UTF-8 170 bytes

~~~c

void _ZNKSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6getlocEv(undefined8 param_1,long param_2)

{
  _ZNSt6__ndk16localeC1ERKS0_(param_1,param_2 + 8);
  return;
}

~~~
