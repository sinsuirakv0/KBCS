# 00bfaff0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfabc8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfabc8.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0041.md#compare-0e2ed90b512dbc4f1295225d3078ceb9)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0042.md#compare-ece620a77bb6261c61a6350e09c557ff)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfaff0",
  "name": "_ZNSt6__ndk18ios_base16__call_callbacksENS0_5eventE",
  "size": 100,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f7c615eb1abe66b22ab504021d2274f2299fe8d352036e9f726beacc7befff8c",
  "source_text_sha256": "f7c615eb1abe66b22ab504021d2274f2299fe8d352036e9f726beacc7befff8c"
}
~~~

## 呼び出し元

- [00c5e2d0](../00c5e/00c5e2d0.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 423 bytes

~~~c

void _ZNSt6__ndk18ios_base16__call_callbacksENS0_5eventE(long param_1,undefined4 param_2)

{
  long lVar1;
  
  if (*(long *)(param_1 + 0x48) != 0) {
    lVar1 = *(long *)(param_1 + 0x48) + -1;
    do {
      (**(code **)(*(long *)(param_1 + 0x38) + lVar1 * 8))
                (param_2,param_1,*(undefined4 *)(*(long *)(param_1 + 0x40) + lVar1 * 4));
      lVar1 = lVar1 + -1;
    } while (lVar1 != -1);
  }
  return;
}

~~~
