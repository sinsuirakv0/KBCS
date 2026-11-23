# 007aeedc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/review-0128.md#review-2a6e5ac6d516cd6862cc73a3429f9111)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007aeedc",
  "name": "FUN_007aeedc",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0edc2898be99fbe0cbd645cc583a434960bf48e6337505d89e5de3b4b5f2fd78",
  "source_text_sha256": "0edc2898be99fbe0cbd645cc583a434960bf48e6337505d89e5de3b4b5f2fd78"
}
~~~

## 呼び出し元

- [007ad944](../007ad/007ad944.md)

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)

## 疑似コード / UTF-8 168 bytes

~~~c

void FUN_007aeedc(void *param_1)

{
  if ((*(byte *)((long)param_1 + 8) & 1) != 0) {
    _ZdlPv(*(void **)((long)param_1 + 0x18));
  }
  _ZdlPv(param_1);
  return;
}

~~~
