# 00acbe7c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a6dee8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dee8.md) · 移動量 `+0x5df94`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/inspection-0018.md#compare-e0c99f67cc80cb14c82fa0c19097556d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbe7c",
  "name": "FUN_00acbe7c",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9ec548f80c2b98a6f35f9d2ad5a9c3f952246a5c0938f7fecd3f9ada677a267a",
  "source_text_sha256": "9ec548f80c2b98a6f35f9d2ad5a9c3f952246a5c0938f7fecd3f9ada677a267a"
}
~~~

## 呼び出し元

- [00acbb50](../00acb/00acbb50.md)

## 呼び出し先

- [00acb88c](../00acb/00acb88c.md)
- [00c57ab0](../00c57/00c57ab0.md)

## 疑似コード / UTF-8 195 bytes

~~~c

void FUN_00acbe7c(long param_1)

{
  void *__ptr;
  
  __ptr = *(void **)(param_1 + 0x18);
  if (__ptr != (void *)0x0) {
    FUN_00acb88c(__ptr);
    _ZdlPv(__ptr);
    return;
  }
  return;
}

~~~
