# 008abbbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/review-0144.md#review-4cb444785aad41cf258df0e11eef1a4c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008abbbc",
  "name": "FUN_008abbbc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fff10a3c9e61a8d532172239213c079cc2119c1df35aa03e1ce5a7846abad954",
  "source_text_sha256": "fff10a3c9e61a8d532172239213c079cc2119c1df35aa03e1ce5a7846abad954"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 461 bytes

~~~c

long FUN_008abbbc(long param_1,long param_2)

{
                    /* catch() { ... } // from try @ 008ab770 with catch @ 008abbc4 */
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) !=
      "ZN17MyUtilityListener22miniBrowserLinkClickedERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEE3$_2"
     ) {
    param_1 = 0;
  }
                    /* catch() { ... } // from try @ 008ab758 with catch @ 008abbd4 */
  return param_1;
}

~~~
