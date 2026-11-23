# 00bbaaa0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbaa5c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa5c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/high-0011.md#compare-14e3b96a3e3614c43eb7e3b9493b5b91)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbaaa0",
  "name": "_ZSt15get_new_handlerv",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "742bc7ebb3ce42334eb2d14fe727dc8cfeb267a68f078b38d05bd266f013b72e",
  "source_text_sha256": "742bc7ebb3ce42334eb2d14fe727dc8cfeb267a68f078b38d05bd266f013b72e"
}
~~~

## 呼び出し元

- [00be1e20](../00be1/00be1e20.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 277 bytes

~~~c

undefined8 _ZSt15get_new_handlerv(void)

{
                    /* catch() { ... } // from try @ 00bb34c4 with catch @ 00bbaaac */
                    /* catch() { ... } // from try @ 00bb3490 with catch @ 00bbaab0 */
  return *(undefined8 *)PTR___cxa_new_handler_00c1c008;
}

~~~
