# 00bba3dc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bba314`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba314.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/inspection-0006.md#compare-0a4763250ebd5bc48b8540c58e1a22ca)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bba3dc",
  "name": "_ZNSt6__ndk111regex_errorD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f12ebbdbdda6c13cb9a8bf4918e468c60221e0a02afa788337b649383b599b65",
  "source_text_sha256": "f12ebbdbdda6c13cb9a8bf4918e468c60221e0a02afa788337b649383b599b65"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)
- [00bdd920](../00bdd/00bdd920.md)

## 疑似コード / UTF-8 315 bytes

~~~c

void _ZNSt6__ndk111regex_errorD0Ev(void *param_1)

{
                    /* try { // try from 00bba3e8 to 00cba3eb has its CatchHandler @ 00bbad0c */
  _ZNSt6__ndk111regex_errorD1Ev();
                    /* try { // try from 00bba400 to 00cba403 has its CatchHandler @ 00bbacd8 */
  _ZdlPv(param_1);
  return;
}

~~~
