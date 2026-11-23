# 00bdae9c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 対応未確定
  - [v15.7.3 → v15.7.4 版の比較一覧](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/README.md)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdae9c",
  "name": "FUN_00bdae9c",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d378de2315dae509f9da866b4583f3081a7ffcbf99acd629b8c63db1a06e998d",
  "source_text_sha256": "d378de2315dae509f9da866b4583f3081a7ffcbf99acd629b8c63db1a06e998d"
}
~~~

## 呼び出し元

- [00b07fc8](../00b07/00b07fc8.md)

## 呼び出し先

- [00b08008](../00b08/00b08008.md)

## 疑似コード / UTF-8 155 bytes

~~~c

void FUN_00bdae9c(undefined8 param_1,undefined8 param_2)

{
  long in_x9;
  
  FUN_00b08008(param_1,param_2,*(undefined8 *)(in_x9 + 0xea8));
  return;
}

~~~
