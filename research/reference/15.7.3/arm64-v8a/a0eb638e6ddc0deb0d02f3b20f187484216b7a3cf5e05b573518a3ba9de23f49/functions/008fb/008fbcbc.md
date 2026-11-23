# 008fbcbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `008fbcbc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fb/008fbcbc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/no_difference_in_scope-0015.md#compare-bb5a8522ea514a35265aab6a48f57e33)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008fbcbc",
  "name": "FUN_008fbcbc",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "833ac304ea4627eaccc526046110fea582826232597ba87e856d8c4d2f5f47f2",
  "source_text_sha256": "833ac304ea4627eaccc526046110fea582826232597ba87e856d8c4d2f5f47f2"
}
~~~

## 呼び出し元

- [006ddfb8](../006dd/006ddfb8.md)
- [00a34c84](../00a34/00a34c84.md)

## 呼び出し先

- [008f95c0](../008f9/008f95c0.md)
- [008fb5f4](../008fb/008fb5f4.md)

## 疑似コード / UTF-8 268 bytes

~~~c

void FUN_008fbcbc(char *param_1)

{
  if (*param_1 != '\0') {
    if (*(int *)(param_1 + 4) == 1) {
      FUN_008fb5f4(param_1 + 0x18);
      return;
    }
    if (*(int *)(param_1 + 4) == 0) {
      FUN_008f95c0(param_1 + 0x48);
      return;
    }
  }
  return;
}

~~~
