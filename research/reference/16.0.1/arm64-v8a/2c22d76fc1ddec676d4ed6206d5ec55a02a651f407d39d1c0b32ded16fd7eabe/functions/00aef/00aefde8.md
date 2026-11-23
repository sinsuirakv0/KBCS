# 00aefde8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/review-0083.md#review-43635c374d687dca43a999988aa59f81)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/review-0040.md#review-43635c374d687dca43a999988aa59f81)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aefde8",
  "name": "FUN_00aefde8",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9c93dae53c3dd045951cc8e5da7424abc04170af9ba2cb43c34e76f36ba9fd77",
  "source_text_sha256": "9c93dae53c3dd045951cc8e5da7424abc04170af9ba2cb43c34e76f36ba9fd77"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 614 bytes

~~~c

long FUN_00aefde8(long param_1,long param_2)

{
                    /* catch() { ... } // from try @ 00aeff9c with catch @ 00aefde8
                       catch() { ... } // from try @ 00af00cc with catch @ 00aefde8
                       catch() { ... } // from try @ 00af0280 with catch @ 00aefde8
                       catch() { ... } // from try @ 00af0434 with catch @ 00aefde8 */
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) !=
      "ZZN13MyApplication16UnitAdoptioninitEvENK3$_5clEP9NewButton20NewButtonChangeStateEUlP9NewDialogP9aGraphicsE_"
     ) {
    param_1 = 0;
  }
  return param_1;
}

~~~
