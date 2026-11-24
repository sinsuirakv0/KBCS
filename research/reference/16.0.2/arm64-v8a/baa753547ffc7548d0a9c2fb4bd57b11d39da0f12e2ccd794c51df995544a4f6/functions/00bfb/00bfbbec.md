# 00bfbbec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfbb50`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbb50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/inspection-0041.md#compare-cea63bcd13e52694f761ee4ca26a612b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0039.md#compare-81f8c58ae8e46beb16079a078d600e9d)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbbec",
  "name": "_ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "67bfe29a72f6e96397eba1abfdf93da23d29996393dc0d5b352ad13be166092b",
  "source_text_sha256": "67bfe29a72f6e96397eba1abfdf93da23d29996393dc0d5b352ad13be166092b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)
- [00c5e410](../00c5e/00c5e410.md)

## 疑似コード / UTF-8 161 bytes

~~~c

void _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED0Ev(void *param_1)

{
  _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev();
  _ZdlPv(param_1);
  return;
}

~~~
