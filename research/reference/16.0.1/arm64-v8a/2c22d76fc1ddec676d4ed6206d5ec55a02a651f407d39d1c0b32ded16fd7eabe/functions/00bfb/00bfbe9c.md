# 00bfbe9c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfba74`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfba74.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0086.md#compare-46fe0c195751705105aa8335106dbfe5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0096.md#compare-76ea7feb27f77378ee4b0c96c29496a5)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbe9c",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1Ev",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a456916b9bf9228f7136d6b288c7d72ae25f5128ff94fe6bcea2159818c7aa8a",
  "source_text_sha256": "a456916b9bf9228f7136d6b288c7d72ae25f5128ff94fe6bcea2159818c7aa8a"
}
~~~

## 呼び出し元

- [00c581f0](../00c58/00c581f0.md)

## 呼び出し先

- [00c5a7a0](../00c5a/00c5a7a0.md)

## 疑似コード / UTF-8 340 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1Ev(long *param_1)

{
  *param_1 = (long)(PTR__ZTVNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEE_00c9b848 + 0x10);
  _ZNSt6__ndk16localeC2Ev(param_1 + 1);
  param_1[5] = 0;
  param_1[4] = 0;
  param_1[7] = 0;
  param_1[6] = 0;
  param_1[3] = 0;
  param_1[2] = 0;
  return;
}

~~~
