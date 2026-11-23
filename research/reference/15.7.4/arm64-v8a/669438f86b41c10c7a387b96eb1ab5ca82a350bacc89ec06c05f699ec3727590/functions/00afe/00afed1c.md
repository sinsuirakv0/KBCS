# 00afed1c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afecd8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afecd8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/inspection-0008.md#compare-aa2bdc18d2e40c20a96a4f9cb323a6ea)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afed1c",
  "name": "_ZN8firebase26ReferenceCountedFutureImplD0Ev",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a9ad010502a1a246bb61a9dca977afaf76f1e1f31c463b98debf1a03cd224ada",
  "source_text_sha256": "a9ad010502a1a246bb61a9dca977afaf76f1e1f31c463b98debf1a03cd224ada"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00bdee20](../00bde/00bdee20.md)

## 疑似コード / UTF-8 325 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImplD0Ev(void *param_1)

{
                    /* catch() { ... } // from try @ 00afdb74 with catch @ 00afed1c */
                    /* catch() { ... } // from try @ 00af6ff4 with catch @ 00afed20 */
  _ZN8firebase26ReferenceCountedFutureImplD1Ev();
  _ZdlPv(param_1);
  return;
}

~~~
