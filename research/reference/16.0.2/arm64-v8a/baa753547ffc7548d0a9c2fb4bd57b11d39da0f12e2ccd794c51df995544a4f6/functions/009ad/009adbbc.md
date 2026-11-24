# 009adbbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `009adb68`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ad/009adb68.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/no_difference_in_scope-0010.md#compare-99d5a683c7125162d3e08b2a8b869bb2)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/no_difference_in_scope-0010.md#compare-d8cdd49aeec1fb4c2295772f21d84116)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009adbbc",
  "name": "FUN_009adbbc",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6033cc417b5b12d3e5d0fb605889b1918d3d5e7dfe8e838e10d389fc565402da",
  "source_text_sha256": "6033cc417b5b12d3e5d0fb605889b1918d3d5e7dfe8e838e10d389fc565402da"
}
~~~

## 呼び出し元

- [009b892c](../009b8/009b892c.md)
- [009b9738](../009b9/009b9738.md)
- [009b9794](../009b9/009b9794.md)
- [009ba090](../009ba/009ba090.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 87 bytes

~~~c

ulong FUN_009adbbc(long *param_1)

{
  return (ulong)(param_1[1] - *param_1) >> 4;
}

~~~
