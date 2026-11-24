# 00bffde8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bffd4c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffd4c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0087.md#compare-caa0a95c40298b14b0fe3f7eb2a931c1)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0099.md#compare-62f4a5cb47b2216b99497f7b32b691fd)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffde8",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEC1ERKS3_",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "557d7bba883a128b8e46c9c19849a3917adf3f6d3cf64b9432e55636566cdb37",
  "source_text_sha256": "557d7bba883a128b8e46c9c19849a3917adf3f6d3cf64b9432e55636566cdb37"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a8a0](../00c5a/00c5a8a0.md)

## 疑似コード / UTF-8 585 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEC1ERKS3_(long *param_1,long param_2)

{
  long lVar1;
  
  *param_1 = (long)(PTR__ZTVNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEE_00c9bc00 + 0x10);
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
