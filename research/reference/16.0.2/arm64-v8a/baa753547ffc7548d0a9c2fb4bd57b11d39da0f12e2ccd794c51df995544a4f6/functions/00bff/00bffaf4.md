# 00bffaf4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bffa58`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffa58.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/high-0011.md#compare-d76ba899eef25646d09fa2fa7dc7b291)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/high-0012.md#compare-6b0440e83b7e5b282674a737b275ca3e)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffaf4",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEED2Ev",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4e6984b7db699be158f63f9cf296800e8603dfd76050b98eddca526e00fb2b8d",
  "source_text_sha256": "4e6984b7db699be158f63f9cf296800e8603dfd76050b98eddca526e00fb2b8d"
}
~~~

## 呼び出し元

- [00c5e490](../00c5e/00c5e490.md)
- [00c5e4a0](../00c5e/00c5e4a0.md)

## 呼び出し先

- [00c58360](../00c58/00c58360.md)

## 疑似コード / UTF-8 232 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEED2Ev(long *param_1)

{
  *param_1 = (long)(PTR__ZTVNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEE_00c9bc00 + 0x10);
  _ZNSt6__ndk16localeD1Ev(param_1 + 1);
  return;
}

~~~
