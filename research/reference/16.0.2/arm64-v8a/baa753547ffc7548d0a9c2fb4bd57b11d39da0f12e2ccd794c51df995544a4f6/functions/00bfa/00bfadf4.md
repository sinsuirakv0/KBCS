# 00bfadf4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfad58`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfad58.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/inspection-0041.md#compare-20003a1c7729fa1dcfeba1f37098c86c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0039.md#compare-d2af5fa10dd6cc688fe5eb764313944c)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfadf4",
  "name": "_ZNSt6__ndk113random_deviceD1Ev",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "972ed633fa8eb8b3ab5a15472706f5ea320d386143d89d93d243c151d808cea3",
  "source_text_sha256": "972ed633fa8eb8b3ab5a15472706f5ea320d386143d89d93d243c151d808cea3"
}
~~~

## 呼び出し元

- [00c584a0](../00c58/00c584a0.md)

## 呼び出し先

- [00c598a0](../00c59/00c598a0.md)

## 疑似コード / UTF-8 116 bytes

~~~c

int _ZNSt6__ndk113random_deviceD1Ev(int *param_1)

{
  int iVar1;
  
  iVar1 = close(*param_1);
  return iVar1;
}

~~~
