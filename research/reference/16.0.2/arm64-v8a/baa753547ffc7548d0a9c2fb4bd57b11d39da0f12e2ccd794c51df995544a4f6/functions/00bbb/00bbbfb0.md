# 00bbbfb0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbbf14`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbf14.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0079.md#compare-09a566895a11a4fe17c67bd16f1ea4b4)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0091.md#compare-cdd9e6a302dc74e88a5476a8fe812c16)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbbfb0",
  "name": "_ZN8firebase9messaging38DeliveryMetricsExportToBigQueryEnabledEv",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "15c3c6e3c8d64060505853443549540936f800898ddbf9858dde16c470c8c9cc",
  "source_text_sha256": "15c3c6e3c8d64060505853443549540936f800898ddbf9858dde16c470c8c9cc"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497a88](../00497/00497a88.md)
- [00c5b150](../00c5b/00c5b150.md)

## 疑似コード / UTF-8 406 bytes

~~~c

bool _ZN8firebase9messaging38DeliveryMetricsExportToBigQueryEnabledEv(void)

{
  char cVar1;
  undefined8 uVar2;
  
  if (DAT_01126460 != 0) {
    uVar2 = _ZNK8firebase3App9GetJNIEnvEv();
                    /* try { // try from 00bbbfcc to 00cbbfef has its CatchHandler @ 00bbc808 */
    cVar1 = FUN_00497a88(uVar2,DAT_01126498,DAT_011263e0);
    return cVar1 != '\0';
  }
  return DAT_01126504 == 1;
}

~~~
