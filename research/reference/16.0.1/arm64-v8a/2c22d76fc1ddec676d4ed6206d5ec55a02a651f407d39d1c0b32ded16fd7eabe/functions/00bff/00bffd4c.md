# 00bffd4c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bff924`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff924.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0087.md#compare-faf079cbfa1188833325054dc78347b0)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0096.md#compare-caa0a95c40298b14b0fe3f7eb2a931c1)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffd4c",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEC1ERKS3_",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fa6c0cda04c4860b015df10c95ebfedcc4128b348336ae41107767b245d793a8",
  "source_text_sha256": "fa6c0cda04c4860b015df10c95ebfedcc4128b348336ae41107767b245d793a8"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a7d0](../00c5a/00c5a7d0.md)

## 疑似コード / UTF-8 585 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEC1ERKS3_(long *param_1,long param_2)

{
  long lVar1;
  
  *param_1 = (long)(PTR__ZTVNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEE_00c9bb30 + 0x10);
  _ZNSt6__ndk16localeC1ERKS0_(param_1 + 1,param_2 + 8);
  lVar1 = *(long *)(param_2 + 0x10);
  param_1[3] = *(long *)(param_2 + 0x18);
  param_1[2] = lVar1;
  lVar1 = *(long *)(param_2 + 0x20);
  param_1[5] = *(long *)(param_2 + 0x28);
  param_1[4] = lVar1;
  lVar1 = *(long *)(param_2 + 0x30);
  param_1[7] = *(long *)(param_2 + 0x38);
  param_1[6] = lVar1;
  return;
}

~~~
