# 00baf6fc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baf6b8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf6b8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/inspection-0017.md#compare-378ef66a7ec1c7b48e3f2aa627b718a3)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baf6fc",
  "name": "_ZNSt6__ndk115numpunct_bynameIcED0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "073c302c2409df54ca7c43bbc1a1ae51eeadc21200bb1121eeb63aaa1c094f50",
  "source_text_sha256": "073c302c2409df54ca7c43bbc1a1ae51eeadc21200bb1121eeb63aaa1c094f50"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00be1c90](../00be1/00be1c90.md)

## 疑似コード / UTF-8 666 bytes

~~~c

void _ZNSt6__ndk115numpunct_bynameIcED0Ev(void *param_1)

{
                    /* try { // try from 00baf700 to 00caf70b has its CatchHandler @ 00baf710 */
                    /* catch() { ... } // from try @ 00baf58c with catch @ 00baf70c
                       try { // try from 00baf70c to 00caf73b has its CatchHandler @ 00baf554 */
                    /* catch() { ... } // from try @ 00baf700 with catch @ 00baf710 */
  _ZNSt6__ndk18numpunctIcED1Ev();
                    /* catch() { ... } // from try @ 00baf5c8 with catch @ 00baf714 */
                    /* catch() { ... } // from try @ 00baf5ec with catch @ 00baf718 */
  _ZdlPv(param_1);
  return;
}

~~~
