# 00bdafd0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 要確認
  - [v15.7.3 → v15.7.4 候補と検査根拠](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/review-0039.md#review-31c843b0b6b3aeb52e7d220fcefc4128)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdafd0",
  "name": "<EXTERNAL>::__cxa_finalize",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ee454707ff51c2b811bc691a4bcda28d1b92bd4f7346af5204f67639ee4dd61f",
  "source_text_sha256": "ee454707ff51c2b811bc691a4bcda28d1b92bd4f7346af5204f67639ee4dd61f"
}
~~~

## 呼び出し元

- [004182d0](../00418/004182d0.md)

## 呼び出し先

- [010a5000](../010a5/010a5000.md)

## 疑似コード / UTF-8 87 bytes

~~~c

void __cxa_finalize(void)

{
  (*(code *)PTR___cxa_finalize_00c1c0a0)();
  return;
}

~~~
