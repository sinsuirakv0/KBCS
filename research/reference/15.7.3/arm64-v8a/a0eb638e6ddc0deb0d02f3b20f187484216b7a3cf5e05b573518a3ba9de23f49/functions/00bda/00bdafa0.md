# 00bdafa0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdaef0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaef0.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/high-0010.md#compare-6a521decf7d584cac88c8343734655ee)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdafa0",
  "name": "<EXTERNAL>::__register_atfork",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1973a956e5ab21db6d8309a7ac966dc79665ee5da574a895ab429a5c1b5dc115",
  "source_text_sha256": "1973a956e5ab21db6d8309a7ac966dc79665ee5da574a895ab429a5c1b5dc115"
}
~~~

## 呼び出し元

- [00418320](../00418/00418320.md)

## 呼び出し先

- [010a5010](../010a5/010a5010.md)

## 疑似コード / UTF-8 93 bytes

~~~c

void __register_atfork(void)

{
  (*(code *)PTR___register_atfork_00c1c060)();
  return;
}

~~~
