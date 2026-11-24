# 00bf0ffc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bf0f60`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0f60.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/machine_only_observed-0022.md#compare-80ee406fb285ddf5324840dbf7736346)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/machine_only_observed-0022.md#compare-436aa2441c6ec7eb11b3ca7d4a5354b4)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf0ffc",
  "name": "_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "762f986ee785cfbcd659f0684b8e3f9cc905ba43b9c71808663e528c38a01305",
  "source_text_sha256": "762f986ee785cfbcd659f0684b8e3f9cc905ba43b9c71808663e528c38a01305"
}
~~~

## 呼び出し元

- [00c5e120](../00c5e/00c5e120.md)

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)

## 疑似コード / UTF-8 191 bytes

~~~c

void _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(byte *param_1)

{
  if ((*param_1 & 1) == 0) {
    return;
  }
  _ZdlPv(*(void **)(param_1 + 0x10));
  return;
}

~~~
