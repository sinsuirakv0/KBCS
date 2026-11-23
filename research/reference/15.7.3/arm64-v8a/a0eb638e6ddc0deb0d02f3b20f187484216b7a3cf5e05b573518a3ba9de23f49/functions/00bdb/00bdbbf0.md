# 00bdbbf0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdbb40`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbb40.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/high-0012.md#compare-fed5bc607f3ca776aa4438134646e511)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbbf0",
  "name": "_ZN5Botan6BigInt13binary_decodeEPKhm",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b69550cae17c19103d246af2f7b2a54dc2337ed1f545d97fd35419ddf83de266",
  "source_text_sha256": "b69550cae17c19103d246af2f7b2a54dc2337ed1f545d97fd35419ddf83de266"
}
~~~

## 呼び出し元

- [0048ddf0](../0048d/0048ddf0.md)
- [0048df5c](../0048d/0048df5c.md)
- [00497a4c](../00497/00497a4c.md)
- [004b5004](../004b5/004b5004.md)
- [004ccf4c](../004cc/004ccf4c.md)
- [004e0734](../004e0/004e0734.md)
- [004e66d0](../004e6/004e66d0.md)
- [004e939c](../004e9/004e939c.md)

## 呼び出し先

- [00494840](../00494/00494840.md)

## 疑似コード / UTF-8 131 bytes

~~~c

void _ZN5Botan6BigInt13binary_decodeEPKhm(void)

{
  (*(code *)PTR__ZN5Botan6BigInt13binary_decodeEPKhm_00c1c688)();
  return;
}

~~~
