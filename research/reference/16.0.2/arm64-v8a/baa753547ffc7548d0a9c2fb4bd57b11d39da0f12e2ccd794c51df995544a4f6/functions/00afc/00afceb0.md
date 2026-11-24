# 00afceb0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afce14`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afce14.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/inspection-0036.md#compare-de97b1cf44a23c6e1e4ec3bd3414a34e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0030.md#compare-d631537b233127753c3455d2da428b32)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afceb0",
  "name": "FUN_00afceb0",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aeb09e14fc6d10af145ecea71e8aff960d03cca6820cf4852ff647a776dbab44",
  "source_text_sha256": "aeb09e14fc6d10af145ecea71e8aff960d03cca6820cf4852ff647a776dbab44"
}
~~~

## 呼び出し元

- [005f2da8](../005f2/005f2da8.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 248 bytes

~~~c

void FUN_00afceb0(int param_1,int param_2,int param_3)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
  lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar1 + 0x84c70) = *(int *)(lVar1 + 0x84c70) + param_3;
  return;
}

~~~
