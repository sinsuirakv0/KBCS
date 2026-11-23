# 00bbadb4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbad70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbad70.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/high-0011.md#compare-5844462e2d64d9547f7db1d84372cc68)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbadb4",
  "name": "_ZNSt9bad_allocC2Ev",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "77fbc1ab5ba5cd4aec0194ac4358ceb0d20d1513a5c91ee597a163dcc2dde125",
  "source_text_sha256": "77fbc1ab5ba5cd4aec0194ac4358ceb0d20d1513a5c91ee597a163dcc2dde125"
}
~~~

## 呼び出し元

- [00bdbbf0](../00bdb/00bdbbf0.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 551 bytes

~~~c

void _ZNSt9bad_allocC2Ev(long *param_1)

{
                    /* catch() { ... } // from try @ 00bb46f8 with catch @ 00bbadb8 */
                    /* catch() { ... } // from try @ 00bb76a0 with catch @ 00bbadbc */
                    /* catch() { ... } // from try @ 00bb76b8 with catch @ 00bbadc0 */
                    /* catch() { ... } // from try @ 00bb72f0 with catch @ 00bbadc4 */
  *param_1 = (long)(PTR__ZTVSt9bad_alloc_00c1c018 + 0x10);
                    /* catch() { ... } // from try @ 00bb7308 with catch @ 00bbadc8 */
  return;
}

~~~
