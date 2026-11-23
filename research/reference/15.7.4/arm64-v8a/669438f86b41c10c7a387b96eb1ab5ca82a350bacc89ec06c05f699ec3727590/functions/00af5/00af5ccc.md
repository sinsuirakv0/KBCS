# 00af5ccc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00af5c88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5c88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/inspection-0008.md#compare-ae9c9d0508853699c943e8e7015429ea)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af5ccc",
  "name": "_ZN8firebase4util15ContinueBuilderEP7_JNIEnvP8_jobjectS4_",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6ced2c64190f39fb3bb0136b08365f0188b3c03c2fee3805cd2a27a8049278a9",
  "source_text_sha256": "6ced2c64190f39fb3bb0136b08365f0188b3c03c2fee3805cd2a27a8049278a9"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 582 bytes

~~~c

undefined8
_ZN8firebase4util15ContinueBuilderEP7_JNIEnvP8_jobjectS4_
          (long *param_1,undefined8 param_2,undefined8 param_3)

{
                    /* try { // try from 00af5cd0 to 00bf5cd7 has its CatchHandler @ 00affbec */
                    /* try { // try from 00af5cdc to 00bf5ce3 has its CatchHandler @ 00affbe0 */
  (**(code **)(*param_1 + 0xb8))();
                    /* try { // try from 00af5ce8 to 00bf5cef has its CatchHandler @ 00affbd4 */
                    /* try { // try from 00af5cf4 to 00bf5cfb has its CatchHandler @ 00affbc8 */
  return param_3;
}

~~~
