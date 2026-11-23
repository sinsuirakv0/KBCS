# 00bf3fcc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b77584`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77584.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0071.md#compare-5d3c567d8116ad9134cbac8b75fbdaf5)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf3fcc",
  "name": "FUN_00bf3fcc",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fc0a66bb4e5c7940a94dc44d63c144f2622f62b16de045a618ecc2d5e9667bd9",
  "source_text_sha256": "fc0a66bb4e5c7940a94dc44d63c144f2622f62b16de045a618ecc2d5e9667bd9"
}
~~~

## 呼び出し元

- [00bf3fc4](../00bf3/00bf3fc4.md)

## 呼び出し先

- [00bf2f78](../00bf2/00bf2f78.md)
- [00c5dc00](../00c5d/00c5dc00.md)

## 疑似コード / UTF-8 157 bytes

~~~c

void FUN_00bf3fcc(undefined8 param_1,wchar_t *param_2)

{
  size_t sVar1;
  
  sVar1 = wcslen(param_2);
  FUN_00bf2f78(param_1,param_2,sVar1);
  return;
}

~~~
