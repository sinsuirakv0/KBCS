# 00aaf0dc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aaf014`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaf/00aaf014.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/inspection-0001.md#compare-65aa5bd29ec9314c8ab69086e5b86ea6)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aaf0dc",
  "name": "FUN_00aaf0dc",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9836494056f4f4bf9f4c8e86d73b2e95f9e5b73eb0b3c2837d7191f4cbd5a509",
  "source_text_sha256": "9836494056f4f4bf9f4c8e86d73b2e95f9e5b73eb0b3c2837d7191f4cbd5a509"
}
~~~

## 呼び出し元

- [009c5338](../009c5/009c5338.md)

## 呼び出し先

- [0045df50](../0045d/0045df50.md)

## 疑似コード / UTF-8 145 bytes

~~~c

void FUN_00aaf0dc(undefined4 *param_1,undefined8 param_2)

{
  FUN_0045df50(param_2,*param_1);
  FUN_0045df50(param_2,param_1[1]);
  return;
}

~~~
