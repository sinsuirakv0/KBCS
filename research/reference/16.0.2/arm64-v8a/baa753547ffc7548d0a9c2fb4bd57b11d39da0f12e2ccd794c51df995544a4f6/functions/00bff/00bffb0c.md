# 00bffb0c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bffa70`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffa70.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/inspection-0042.md#compare-75ae7d52c521e2d3f95164e6d1c51820)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0039.md#compare-243c2492d9eeda408d696eea544254b0)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffb0c",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEED0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ac317ab8a7097e5a3b4341ec91f1407d827f9b02f055aa340a7083fe49651ae9",
  "source_text_sha256": "ac317ab8a7097e5a3b4341ec91f1407d827f9b02f055aa340a7083fe49651ae9"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)
- [00c5e4a0](../00c5e/00c5e4a0.md)

## 疑似コード / UTF-8 175 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEED0Ev(void *param_1)

{
  _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEED2Ev();
  _ZdlPv(param_1);
  return;
}

~~~
