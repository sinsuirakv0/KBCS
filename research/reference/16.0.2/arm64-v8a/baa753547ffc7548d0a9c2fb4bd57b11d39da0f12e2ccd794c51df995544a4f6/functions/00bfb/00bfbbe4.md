# 00bfbbe4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfbb48`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbb48.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/machine_only_observed-0022.md#compare-92a62699c03451d31314ea089479dfe0)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/machine_only_observed-0022.md#compare-a43224e68374f181d96466aa8e1d4897)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbbe4",
  "name": "_ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev",
  "size": 8,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7aad78d5ee02cd9a543a3b578a4fbc03a1974e4f9f0c76a3d883e486885d4b06",
  "source_text_sha256": "7aad78d5ee02cd9a543a3b578a4fbc03a1974e4f9f0c76a3d883e486885d4b06"
}
~~~

## 呼び出し元

- [00c58090](../00c58/00c58090.md)
- [00c5e410](../00c5e/00c5e410.md)

## 呼び出し先

- [00c5d1b0](../00c5d/00c5d1b0.md)

## 疑似コード / UTF-8 109 bytes

~~~c

void _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev(void)

{
  _ZNSt6__ndk18ios_baseD1Ev();
  return;
}

~~~
