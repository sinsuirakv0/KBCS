# 00b7edcc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b7ed88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ed88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/inspection-0014.md#compare-159b6ced24ade15b38d0d423f3ad43e1)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b7edcc",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE8pubimbueERKNS_6localeE",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b618ca873f154b734ca720951478c68919994b2b749791c6ece2f0c31ae4f6c5",
  "source_text_sha256": "b618ca873f154b734ca720951478c68919994b2b749791c6ece2f0c31ae4f6c5"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdd980](../00bdd/00bdd980.md)
- [00be12e0](../00be1/00be12e0.md)

## 疑似コード / UTF-8 307 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE8pubimbueERKNS_6localeE
               (undefined8 param_1,long *param_2,undefined8 param_3)

{
  (**(code **)(*param_2 + 0x10))();
  _ZNSt6__ndk16localeC1ERKS0_(param_1,param_2 + 1);
  _ZNSt6__ndk16localeaSERKS0_(param_2 + 1,param_3);
  return;
}

~~~
