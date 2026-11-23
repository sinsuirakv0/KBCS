# 00af7fac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00af7b84`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7b84.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/alignment_unresolved-0005.md#compare-25333646068d3b75b55eebb24fc8f897)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0071.md#compare-272a7c72308b306c96aa0540627c97a9)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af7fac",
  "name": "FUN_00af7fac",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "68e4d63d9f10efefe2b2fda09f7b57868324aa2458a9abe0e4b99f329c5010fc",
  "source_text_sha256": "68e4d63d9f10efefe2b2fda09f7b57868324aa2458a9abe0e4b99f329c5010fc"
}
~~~

## 呼び出し元

- [00a4f3b4](../00a4f/00a4f3b4.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 411 bytes

~~~c

void FUN_00af7fac(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
                    /* try { // try from 00af7fe0 to 00bf7feb has its CatchHandler @ 00af8554 */
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84af0) = param_3;
                    /* try { // try from 00af7fec to 00bf802f has its CatchHandler @ 00af7de0 */
  return;
}

~~~
