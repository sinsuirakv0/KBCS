# 009aadec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `009aad98`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009aa/009aad98.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/detail_skipped-0005.md#compare-33ed992959a856a7950e454877417220)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/detail_skipped-0006.md#compare-5389272f99eccb74aa7404c1beb8f6ff)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009aadec",
  "name": "FUN_009aadec",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5d3be1689cb7692e97e54ce3529037af092f9ceac913006a10f51d442902f0e8",
  "source_text_sha256": "5d3be1689cb7692e97e54ce3529037af092f9ceac913006a10f51d442902f0e8"
}
~~~

## 呼び出し元

- [009b5d94](../009b5/009b5d94.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 113 bytes

~~~c

void FUN_009aadec(long param_1,undefined1 param_2)

{
  *(undefined1 *)(param_1 + 0x35) = param_2;
  return;
}

~~~
