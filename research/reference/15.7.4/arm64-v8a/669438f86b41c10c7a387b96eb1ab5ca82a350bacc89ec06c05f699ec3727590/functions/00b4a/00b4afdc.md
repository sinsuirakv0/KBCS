# 00b4afdc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b4af98`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4af98.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/priority-0068.md#compare-bc30a8625b63d55fec868b5605b828d3)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4afdc",
  "name": "_ZN8firebase9messaging27registration_intent_service12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8b2d0a43dd972d7b1a1517f60d1c783eaa6cf9a07d9351aa6007044503a60bd3",
  "source_text_sha256": "8b2d0a43dd972d7b1a1517f60d1c783eaa6cf9a07d9351aa6007044503a60bd3"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde0e0](../00bde/00bde0e0.md)

## 疑似コード / UTF-8 698 bytes

~~~c

void _ZN8firebase9messaging27registration_intent_service12ReleaseClassEP7_JNIEnv(long *param_1)

{
                    /* try { // try from 00b4aff4 to 00c4afff has its CatchHandler @ 00b4b1b0 */
  if (DAT_010a1058 != 0) {
    if (DAT_010a1060 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a1060 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
                    /* try { // try from 00b4b024 to 00c4b02f has its CatchHandler @ 00b4b188 */
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a1058);
    DAT_010a1058 = 0;
  }
                    /* try { // try from 00b4b044 to 00c4b04f has its CatchHandler @ 00b4b184 */
  return;
}

~~~
