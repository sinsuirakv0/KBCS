# 00af8edc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00af8ab4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8ab4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/alignment_unresolved-0006.md#compare-fdd5230580d7cb7b43896611853d0823)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0036.md#compare-dfadb93fa6d9b9c951f653b3b4b85548)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af8edc",
  "name": "FUN_00af8edc",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "093fc55f9e6d291bd3c8388619ccaa4e856a4b40df4937f0e3f969363af7719c",
  "source_text_sha256": "093fc55f9e6d291bd3c8388619ccaa4e856a4b40df4937f0e3f969363af7719c"
}
~~~

## 呼び出し元

- [007102d8](../00710/007102d8.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 385 bytes

~~~c

undefined4 FUN_00af8edc(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
                    /* try { // try from 00af8f08 to 00bf8f0f has its CatchHandler @ 00af9200 */
                    /* try { // try from 00af8f10 to 00bf8f43 has its CatchHandler @ 00af8cac */
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x8499c);
}

~~~
