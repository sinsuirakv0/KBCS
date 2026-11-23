# 00a0cfec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00a0cfec`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a0c/00a0cfec.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/no_difference_in_scope-0018.md#compare-7ad6fc248216a690bf3696fe781f067f)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a0cfec",
  "name": "FUN_00a0cfec",
  "size": 128,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9b15a2ec88979455a3a5d97a02868cec721a190d8d4ff553cfc002be1d38588a",
  "source_text_sha256": "9b15a2ec88979455a3a5d97a02868cec721a190d8d4ff553cfc002be1d38588a"
}
~~~

## 呼び出し元

- [006eccf4](../006ec/006eccf4.md)
- [009f4a74](../009f4/009f4a74.md)

## 呼び出し先

- [00a0cdf4](../00a0c/00a0cdf4.md)
- [00a0e088](../00a0e/00a0e088.md)
- [00a0e40c](../00a0e/00a0e40c.md)

## 疑似コード / UTF-8 714 bytes

~~~c

void FUN_00a0cfec(long param_1,undefined4 param_2,undefined8 param_3,undefined8 param_4,
                 undefined8 param_5)

{
  int iVar1;
  
                    /* try { // try from 00a0d008 to 00b0d00f has its CatchHandler @ 00a0d41c */
                    /* try { // try from 00a0d010 to 00b0d663 has its CatchHandler @ 00a0a31c */
  FUN_00a0e40c(*(undefined8 *)(param_1 + 0x70),*(undefined4 *)(param_1 + 0x7c));
  iVar1 = FUN_00a0e088();
  if (iVar1 == 0) {
    iVar1 = FUN_00a0cdf4(param_1,param_2,param_3,param_4,param_5);
  }
  else {
    iVar1 = 0;
  }
  iVar1 = *(int *)(param_1 + 0x88) + iVar1;
  if (0x3b9ac9fe < iVar1) {
    iVar1 = 999999999;
  }
  *(int *)(param_1 + 0x88) = iVar1;
  return;
}

~~~
