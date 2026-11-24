# 00afba2c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afb990`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afb/00afb990.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/alignment_unresolved-0007.md#compare-c1544a7bddfd152229a6e00de2a6bfb4)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0080.md#compare-46237aa4dd893ab40a05f8b622fc52d4)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afba2c",
  "name": "FUN_00afba2c",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7d92ab254f0fecad4d40b39a270aeac1934392f7a53392bf7ce27ca044d9ddaf",
  "source_text_sha256": "7d92ab254f0fecad4d40b39a270aeac1934392f7a53392bf7ce27ca044d9ddaf"
}
~~~

## 呼び出し元

- [00710330](../00710/00710330.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 411 bytes

~~~c

void FUN_00afba2c(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
                    /* try { // try from 00afba30 to 00bfba3b has its CatchHandler @ 00afcae8 */
                    /* try { // try from 00afba3c to 00bfba7b has its CatchHandler @ 00afb4a0 */
  lVar1 = FUN_00851550();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c2c) = param_3;
  return;
}

~~~
