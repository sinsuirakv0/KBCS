# 00bff9dc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bff5b4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff5b4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0041.md#compare-dea141d6c7cf5e8bbcda67cff69d8cfb)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0042.md#compare-76f1ca43dbd212d5429f063c7976451c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bff9dc",
  "name": "_ZNSt6__ndk19basic_iosIwNS_11char_traitsIwEEE7copyfmtERKS3_",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6e98b28c97b222eb442b40729b3cd923bff1c326909c559ca050449c40d68a10",
  "source_text_sha256": "6e98b28c97b222eb442b40729b3cd923bff1c326909c559ca050449c40d68a10"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c582a0](../00c58/00c582a0.md)
- [00c5e2d0](../00c5e/00c5e2d0.md)
- [00c5e310](../00c5e/00c5e310.md)

## 疑似コード / UTF-8 674 bytes

~~~c

long _ZNSt6__ndk19basic_iosIwNS_11char_traitsIwEEE7copyfmtERKS3_(long param_1,long param_2)

{
  undefined4 uVar1;
  
  if (param_1 != param_2) {
    _ZNSt6__ndk18ios_base16__call_callbacksENS0_5eventE(param_1,0);
    _ZNSt6__ndk18ios_base7copyfmtERKS0_(param_1,param_2);
    uVar1 = *(undefined4 *)(param_2 + 0x90);
    *(undefined8 *)(param_1 + 0x88) = *(undefined8 *)(param_2 + 0x88);
    *(undefined4 *)(param_1 + 0x90) = uVar1;
    _ZNSt6__ndk18ios_base16__call_callbacksENS0_5eventE(param_1,2);
    *(undefined4 *)(param_1 + 0x24) = *(undefined4 *)(param_2 + 0x24);
    _ZNSt6__ndk18ios_base5clearEj(param_1,*(undefined4 *)(param_1 + 0x20));
  }
  return param_1;
}

~~~
