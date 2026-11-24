# 00bfa1ac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfa110`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa110.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/inspection-0041.md#compare-971d012776bb25562fedb806da48076d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0039.md#compare-d528d5c8bb035f6741cce93fc7537d61)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfa1ac",
  "name": "_ZNSt6__ndk15mutexD1Ev",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3a2b9013c09a966ea36207ba466a9119a371d55235d5a815814c0461f2f827cd",
  "source_text_sha256": "3a2b9013c09a966ea36207ba466a9119a371d55235d5a815814c0461f2f827cd"
}
~~~

## 呼び出し元

- [00c57f30](../00c57/00c57f30.md)

## 呼び出し先

- [00c5b760](../00c5b/00c5b760.md)

## 疑似コード / UTF-8 134 bytes

~~~c

int _ZNSt6__ndk15mutexD1Ev(pthread_mutex_t *param_1)

{
  int iVar1;
  
  iVar1 = pthread_mutex_destroy(param_1);
  return iVar1;
}

~~~
