# 00bbada4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbad60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbad60.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/high-0011.md#compare-9249a6428f32e2e45e546a150f8c1764)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbada4",
  "name": "_ZNKSt13bad_exception4whatEv",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8dd61e146edab738f57ac0bf3b288b75ad6c371a37c804dd9012da334d12e066",
  "source_text_sha256": "8dd61e146edab738f57ac0bf3b288b75ad6c371a37c804dd9012da334d12e066"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 関連文字列（未確認候補）

~~~text
"std::bad_exception"
~~~

## 疑似コード / UTF-8 341 bytes

~~~c

char * _ZNKSt13bad_exception4whatEv(void)

{
                    /* catch() { ... } // from try @ 00bb59f0 with catch @ 00bbada8 */
                    /* catch() { ... } // from try @ 00bb5278 with catch @ 00bbadac */
                    /* catch() { ... } // from try @ 00bb4e98 with catch @ 00bbadb0 */
  return "std::bad_exception";
}

~~~
