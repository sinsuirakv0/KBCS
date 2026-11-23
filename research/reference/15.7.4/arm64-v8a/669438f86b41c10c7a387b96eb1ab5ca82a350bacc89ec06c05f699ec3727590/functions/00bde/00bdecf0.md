# 00bdecf0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdeca0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeca0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/high-0020.md#compare-c8abb3a581be40f8c55097d4b5d1bf25)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdecf0",
  "name": "_ZN8firebase15CleanupNotifier19UnregisterAllOwnersEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7d3a12316fed88053bb74fdae6261e8d4856fe6d631ad3b1943415e5ab44ff57",
  "source_text_sha256": "7d3a12316fed88053bb74fdae6261e8d4856fe6d631ad3b1943415e5ab44ff57"
}
~~~

## 呼び出し元

- [00afc5f0](../00afc/00afc5f0.md)

## 呼び出し先

- [00afc748](../00afc/00afc748.md)

## 疑似コード / UTF-8 163 bytes

~~~c

void _ZN8firebase15CleanupNotifier19UnregisterAllOwnersEv(void)

{
  (*(code *)PTR__ZN8firebase15CleanupNotifier19UnregisterAllOwnersEv_00c1df30)();
  return;
}

~~~
