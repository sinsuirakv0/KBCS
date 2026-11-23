# 00bddcf0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bddc40`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc40.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/high-0016.md#compare-9e8eba9009910d930bfef095fcdf57eb)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddcf0",
  "name": "_ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "457c2f52339952835e4d1a39d7aadefbbbe0ad6669005b94c0dbfc0fd8afa583",
  "source_text_sha256": "457c2f52339952835e4d1a39d7aadefbbbe0ad6669005b94c0dbfc0fd8afa583"
}
~~~

## 呼び出し元

- [00ae0f70](../00ae0/00ae0f70.md)
- [00af5a60](../00af5/00af5a60.md)
- [00b061ec](../00b06/00b061ec.md)
- [00b06ce0](../00b06/00b06ce0.md)
- [00b07f84](../00b07/00b07f84.md)
- [00b0dc70](../00b0d/00b0dc70.md)
- [00b0df30](../00b0d/00b0df30.md)
- [00b4c480](../00b4c/00b4c480.md)
- [00b54af4](../00b54/00b54af4.md)
- [00b5dce8](../00b5d/00b5dce8.md)
- [00b5e148](../00b5e/00b5e148.md)
- [00b69ab8](../00b69/00b69ab8.md)
- [00b69f14](../00b69/00b69f14.md)
- [00b6a060](../00b6a/00b6a060.md)
- [00b6a1ac](../00b6a/00b6a1ac.md)
- [00b6a350](../00b6a/00b6a350.md)
- [00b6a49c](../00b6a/00b6a49c.md)
- [00b6a620](../00b6a/00b6a620.md)
- [00b6a7e4](../00b6a/00b6a7e4.md)
- [00b6b64c](../00b6b/00b6b64c.md)
- [00b6b7c8](../00b6b/00b6b7c8.md)
- [00b6c2cc](../00b6c/00b6c2cc.md)

## 呼び出し先

- [00ae1264](../00ae1/00ae1264.md)

## 疑似コード / UTF-8 177 bytes

~~~c

void _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz(void)

{
  (*(code *)PTR__ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz_00c1d708)();
  return;
}

~~~
