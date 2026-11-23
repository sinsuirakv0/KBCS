# 00bfbaa8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfb680`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb680.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0041.md#compare-c62b2ab8d297bd0ab97f7243d6235d93)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0042.md#compare-88132b8f589595a3de6bbd3b71748b2a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbaa8",
  "name": "_ZNSt6__ndk18ios_base33__set_badbit_and_consider_rethrowEv",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "54b1080809d51488145875c832f580a81e87c981d15c92371446a7849832a727",
  "source_text_sha256": "54b1080809d51488145875c832f580a81e87c981d15c92371446a7849832a727"
}
~~~

## 呼び出し元

- [00c582c0](../00c58/00c582c0.md)

## 呼び出し先

- [00c58500](../00c58/00c58500.md)

## 疑似コード / UTF-8 509 bytes

~~~c

ulong _ZNSt6__ndk18ios_base33__set_badbit_and_consider_rethrowEv(ulong param_1)

{
  undefined1 uVar1;
  ulong uVar2;
  
  *(uint *)(param_1 + 0x20) = *(uint *)(param_1 + 0x20) | 1;
  if ((*(byte *)(param_1 + 0x24) & 1) == 0) {
    return param_1;
  }
  uVar2 = __cxa_rethrow();
  *(uint *)(uVar2 + 0x20) = *(uint *)(uVar2 + 0x20) | 4;
  if ((*(byte *)(uVar2 + 0x24) >> 2 & 1) == 0) {
    return uVar2;
  }
  uVar1 = __cxa_rethrow();
  uVar2 = (ulong)DAT_00ca4808;
  DAT_00ca4808 = uVar1;
  return uVar2;
}

~~~
