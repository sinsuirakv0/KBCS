# 00bddcc0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bddc10`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc10.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/high-0016.md#compare-e8b6f92826fdd8f946e05e32e01b56fc)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddcc0",
  "name": "<EXTERNAL>::__umask_chk",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "84428188beee9535ce525bc0af16da85cdee8389e36a7238b37b14b0a335540d",
  "source_text_sha256": "84428188beee9535ce525bc0af16da85cdee8389e36a7238b37b14b0a335540d"
}
~~~

## 呼び出し元

- [00acc304](../00acc/00acc304.md)
- [00b4b4dc](../00b4b/00b4b4dc.md)

## 呼び出し先

- [010a5570](../010a5/010a5570.md)

## 疑似コード / UTF-8 81 bytes

~~~c

void __umask_chk(void)

{
  (*(code *)PTR___umask_chk_00c1d6f0)();
  return;
}

~~~
